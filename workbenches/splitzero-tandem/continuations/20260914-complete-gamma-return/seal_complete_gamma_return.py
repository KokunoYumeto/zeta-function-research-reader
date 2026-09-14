"""Seal this bounded folder after proof copies and actual page review finish.

No outer-folder writes and no PDF rebuild. The final ZIP includes all current
source/dependency/history/QA files, excluding only itself and post-archive seals.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,zipfile
BASE=Path(__file__).resolve().parent
PDF_SHA='3bd6597135aa0bec23636b122f0d18e83dc722fb44203280653de1def0cd36a0'
def pin(p):return {'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def require(v,msg):
    if not v:raise RuntimeError(msg)
def read(rel):return json.loads((BASE/rel).read_text(encoding='utf-8-sig'))
def write(rel,data):(BASE/rel).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def row(rel):return {'path':rel,**pin(BASE/rel)}
def main():
    require(not (BASE/'DELIVERY_RECEIPT.json').exists(),'Preserve existing final delivery seal')
    pdf=BASE/'Complete_Gamma_Return.pdf';require(pin(pdf)['sha256']==PDF_SHA,'Final PDF differs')
    build=read('BUILD_RECEIPT.json');require(build['pages']==15 and not any(build['warnings'].values()),'Build failed')
    visual=read('qa/ACTUAL_VISUAL_REVIEW.json')
    require(visual['status']=='PASS' and visual['pdf_sha256']==PDF_SHA and visual['pages']==15,'Final actual visual acceptance missing')
    require(not visual.get('pending_defects',[]),'Visual defects remain')
    pages=visual['reviewed_pages'];require(sorted(r['page'] for r in pages)==list(range(1,16)),'Page coverage incomplete')
    for r in pages:
        p=BASE/r['image'];require(pin(p)=={'bytes':r['image_bytes'],'sha256':r['image_sha256']},'Accepted render differs')
    trans=read('SOURCE_TRANSPORTS.json');proofs=[]
    for r in trans['proofs']:
        require(pin(BASE/r['fragment'])==r['fragment_pin'],'Fragment pin differs')
        body=(BASE/r['fragment']).read_text(encoding='utf8')
        require(re.findall(r'\\tag\{([^}]+)\}',body)==r['equation_tags'],'Original equation tags differ')
        for kind in ['pagination_reflow','presentation_reflow']:
            if kind in r:
                for op in reversed(r[kind]['operations']):
                    require(body.count(op['after'])==1,'Inverse display operation ambiguous')
                    body=body.replace(op['after'],op['before'],1)
        for op in reversed(r['operations']):
            if op['kind']=='relative_input_path':
                require(body.count(op['after'])==1,'Inverse input operation ambiguous');body=body.replace(op['after'],op['before'],1)
            elif op['kind']=='source_title_removed':body=body[:op['index']]+op['exact']+body[op['index']:]
            elif op['kind']=='document_wrapper_removal':body=op['prefix']+body+op['suffix']
        require(body==(BASE/r['original']).read_text(encoding='utf8'),'Full author proof inverse differs')
        require(pin(BASE/r['original'])=={'bytes':r['bytes'],'sha256':r['sha256']},'Author bytes differ')
        proofs.append({'name':r['name'],'original':row(r['original']),'compiled_fragment':row(r['fragment']),'all_equation_tags':r['equation_tags'],'exact_full_original_inverse_verified':True})
    require(sum(len(r['all_equation_tags']) for r in proofs)==84,'Expected full84 equation tags')
    actual_inputs=set()
    for line in (BASE/'Complete_Gamma_Return.fls').read_text(encoding='utf8').splitlines():
        if line.startswith('INPUT ') and line.lower().endswith('.tex'):
            p=Path(line[6:]);p=p if p.is_absolute() else BASE/p
            if p.is_relative_to(BASE):actual_inputs.add(p.resolve().relative_to(BASE.resolve()).as_posix())
    require(actual_inputs=={'Complete_Gamma_Return.tex','sources/LET.tex','sources/PHT.tex','sources/HCT.tex'},'Actual TeX closure differs')
    dep=read('provenance/DEPENDENCY_COPY_RECEIPT.json')
    require(dep['all_byte_exact'] and dep['copied_file_count']==241,'Prior source copy incomplete')
    for r in dep['files']:
        require(pin(BASE/r['destination_relative_to_reader'])=={'bytes':r['bytes'],'sha256':r['destination_sha256']},'Prior dependency changed')
    receiving_path='provenance/COMPLETE_GAMMA_RECEIVING_COPY_RECEIPT.json'
    require((BASE/receiving_path).exists(),'Final full receiving copy receipt missing')
    require((BASE/'provenance/proof_acceptance/ROOT_MATHEMATICAL_ACCEPTANCE.json').exists(),'Root full proof acceptance missing')
    workflow=(BASE/'CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md').read_text(encoding='utf8')
    require(len(workflow)==4000,'Workflow length differs')
    authority=read('provenance/FINAL_AUTHORITY_COPY_RECEIPT.json')
    for r in authority['records']:
        require(pin(BASE/r['destination'])=={'bytes':r['bytes'],'sha256':r['sha256']},'Proof authority or prompt copy changed')
    receipt_paths=['BUILD_RECEIPT.json','qa/ACTUAL_VISUAL_REVIEW.json','SOURCE_TRANSPORTS.json','PRESENTATION_REFLOW.json','HCT39_PAGINATION_REFLOW.json','provenance/DEPENDENCY_COPY_RECEIPT.json',receiving_path,'provenance/FINAL_AUTHORITY_COPY_RECEIPT.json','provenance/proof_acceptance/FINAL_PROOF_RECEIPT.json','provenance/proof_acceptance/ROOT_MATHEMATICAL_ACCEPTANCE.json']
    write('BUILD_VISUAL_RECEIPT.json',{'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS: final15-page complete proof build and all-page actual visual acceptance','pdf':row('Complete_Gamma_Return.pdf'),'page_count':15,'whole_proofs':proofs,'compiled_source_closure':[row(p) for p in sorted(actual_inputs)],'actual_visual_scope':'Pages1–13 are byte-identical render transports from the prior actual whole-page review; pages14–15 were actually re-inspected after the sole HCT39 pagination repair. The linked final visual receipt records each page.','mathematical_changes_in_presentation':0,'acceptance_basis':'Complete final mathematical authorities and independent reviews are included verbatim; this packaging receipt verifies source transport and display, and introduces no additional mathematical claim.','receipts':[row(p) for p in receipt_paths]})
    (BASE/'README.md').write_text('''# Complete original Gamma return

Read `Complete_Gamma_Return.pdf` (15 pages), then `00_CONTINUE_THE_PROGRAMME.md`.
The PDF prints the entire LET1–21, PHT1–23 including PHT17a, and HCT1–39
proof bodies. All 84 original equation tags are retained. The continuation
prompt is the exact current mathematical owner's text; the accompanying
`CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md` contains exactly 4,000 characters.

The full editable entrypoint is `Complete_Gamma_Return.tex`. `originals/`
holds all three author documents byte-for-byte. `sources/` holds the full
compiled bodies. `SOURCE_TRANSPORTS.json` records the reversible wrapper,
input-path, line-width, bookmark and single-display pagination changes.
Reversing them reproduces each entire original source. `BUILD_VISUAL_RECEIPT.json`
binds the actual compiled source closure, accepted PDF and all-page review.

The full current receiving successors are in `dependencies/complete_gamma_receiving/`,
including the complete NOTE and JSR texts and their WRC receiving proof.
Their final copy receipt is `provenance/COMPLETE_GAMMA_RECEIVING_COPY_RECEIPT.json`.
The preceding full receivers are retained in `dependencies/current_receiving/`;
`dependencies/bulk_sources/` contains the complete BRD, FTC, CTR and IBC providers;
`dependencies/joint_schur_previous/` retains all preceding textual proof and
provenance dependencies. Its 50 duplicate PDF/ZIP/PNG files are individually
inventoried as omitted in `provenance/DEPENDENCY_COPY_RECEIPT.json`; every textual
proof remains present. Final root and independent proof acceptances are copied
verbatim under `provenance/proof_acceptance/`.

The earlier 2,343-page cumulative volume and the separate 27-, 46- and 33-page
readers retain their historical source cuts. This supplement supplies the full
later proofs and current receiving sources. It does not replace their sealed
PDF bytes. `history/` here preserves the two earlier presentation builds,
including the actual review that found the HCT39 page break; the final PDF has
that display together and no pending visual defects.

For a portable rebuild, use XeLaTeX with the Cambria, Calibri and Consolas fonts
and the packages declared in the main TeX. Run `xelatex -interaction=nonstopmode
-halt-on-error -file-line-error -recorder Complete_Gamma_Return.tex` three times
from an extracted copy. Alternatively, `python prepare_and_build.py build` uses
XeLaTeX on PATH or `XELATEX_BIN` and requires PyMuPDF for the build receipt.
The `prepare`, presentation-repair and sealing commands document one-time
construction steps; existing final source snapshots must be preserved.
Rebuilding can change PDF metadata, so the supplied receipt pins the delivered
PDF rather than promising a binary-identical rebuild.

`Complete_Gamma_Return_Source.zip` contains this complete source/dependency,
PDF, provenance, history and visual-review tree. `ARCHIVE_MANIFEST.json` lists
every archive member; `DELIVERY_RECEIPT.json` records byte-for-byte extraction,
CRC and stable-tree checks. Those two post-archive seals and the ZIP itself are
outside the archive to avoid self-reference. No files outside this folder are
modified by its packaging script.
''',encoding='utf8')
    excluded={'Complete_Gamma_Return_Source.zip','ARCHIVE_MANIFEST.json','DELIVERY_RECEIPT.json'}
    def snapshot():return [row(p.relative_to(BASE).as_posix()) for p in sorted(BASE.rglob('*')) if p.is_file() and p.relative_to(BASE).as_posix() not in excluded]
    before=snapshot();archive=BASE/'Complete_Gamma_Return_Source.zip';require(not archive.exists(),'Preserve existing archive')
    with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for r in before:z.write(BASE/r['path'],r['path'])
    with zipfile.ZipFile(archive) as z:
        require(z.testzip() is None,'Archive CRC failure')
        require(z.namelist()==[r['path'] for r in before],'Archive member inventory differs')
        for r in before:
            raw=z.read(r['path']);require(raw==(BASE/r['path']).read_bytes(),'Archive member bytes differ')
            require(len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'],'Archive member pin differs')
    require(snapshot()==before,'Source tree changed during archive verification')
    write('ARCHIVE_MANIFEST.json',{'scope':'Complete bounded folder before post-archive seals','excluded_self_references':sorted(excluded),'member_count':len(before),'uncompressed_bytes':sum(r['bytes'] for r in before),'files':before})
    write('DELIVERY_RECEIPT.json',{'utc':datetime.now(timezone.utc).isoformat(),'status':'READY: final complete15-page PDF, whole sources and dependencies, exact continuation prompt, durable workflow and verified portable archive','pdf':row('Complete_Gamma_Return.pdf'),'pages':15,'zip':row('Complete_Gamma_Return_Source.zip'),'archive_manifest':row('ARCHIVE_MANIFEST.json'),'archive_members':len(before),'archive_uncompressed_bytes':sum(r['bytes'] for r in before),'all_members_byte_exact':True,'all_member_crc_checks_passed':True,'source_tree_before_after_identical':True,'build_and_visual':row('BUILD_VISUAL_RECEIPT.json'),'continuation_prompt':row('00_CONTINUE_THE_PROGRAMME.md'),'durable_workflow':row('CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md'),'workflow_characters':4000,'final_receiving':row(receiving_path),'outer_folder_modified':False,'remote_publication_performed':False})
    print(json.dumps({'delivery':row('DELIVERY_RECEIPT.json'),**read('DELIVERY_RECEIPT.json')},indent=2))
if __name__=='__main__':main()
