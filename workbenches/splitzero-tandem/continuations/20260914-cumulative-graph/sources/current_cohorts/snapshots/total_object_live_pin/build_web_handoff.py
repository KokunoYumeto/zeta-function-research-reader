"""Assemble a flat, source-pinned web-session handoff with fewer than20 files."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import re
import shutil
import zipfile
from datetime import datetime

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'work/rh_counterfactual_20260913'
TOTAL=WORK/'total_object'
OUT=ROOT/'output/Mixed_Support_Web_Continuation_2026-09-13'
MIXED=ROOT/'output/Deligne_Mixed_Control_Continuation_2026-09-13'
OLD=ROOT/'output/tau_split_zero_counterfactual_continuation_20260913'
WEIL=ROOT/'output/Deligne_Weil_II_S20_LaTeX/typed_latex'
records=[]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p,want):
    if sha(p).lower()!=want.lower():raise RuntimeError('Source changed: '+str(p))
def record(dst,srcs,transformation):
    records.append({'file':dst.name,'bytes':dst.stat().st_size,'sha256':sha(dst),'transformation':transformation,'sources':[{'path':str(s),'sha256':sha(s),'bytes':s.stat().st_size} for s in srcs]})
def copy(name,src):
    dst=OUT/name
    shutil.copyfile(src,dst)
    record(dst,[src],'identity bytes')
def join(name,sources,intro):
    dst=OUT/name
    # Source bytes stay complete contiguous blocks, including original line endings.
    blocks=[intro.encode('utf8')+b'\n']
    for p in sources:
        blocks.extend([('\n\n===== BEGIN COMPLETE SOURCE: '+p.name+'; SHA256 '+sha(p)+' =====\n').encode('utf8'),p.read_bytes(),('\n===== END COMPLETE SOURCE: '+p.name+' =====\n').encode('utf8')])
    dst.write_bytes(b''.join(blocks))
    for p in sources:
        if p.read_bytes() not in dst.read_bytes():raise RuntimeError('Body loss: '+str(p))
    record(dst,sources,'Complete source byte blocks with explicit boundaries; no mathematical-body edits. Text container, not a standalone TeX compilation unit.')

def flatten_old():
    archive=ROOT/'output/Tau_Split_Zero_Total_Counterfactual_Source_248page_Intermediate.zip'
    pin(archive,'68fb2e420f9753cdefb0456a907b794840c43e953d9b68acbc2e04fed2aa74e9')
    z=zipfile.ZipFile(archive)
    base=PurePosixPath(OLD.name)/'tex'
    names=set(z.namelist())
    visited=[]
    pattern=re.compile(r'(?m)^([ \t]*)\\(?:input|include)\{([^}]+)\}')
    def expand(p,stack=()):
        if p in stack:raise RuntimeError('Cyclic TeX input')
        visited.append(p)
        text=z.read(p.as_posix()).decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
        def sub(m):
            rel=PurePosixPath(m[2]); rel=rel if rel.suffix else rel.with_suffix('.tex')
            candidates=[base/rel,p.parent/rel,PurePosixPath(OLD.name)/rel]
            target=next((q for q in candidates if q.as_posix() in names),None)
            if target is None:raise RuntimeError('Missing TeX input '+m[2])
            return '\n% BEGIN INLINED '+m[2]+'\n'+expand(target,stack+(p,))+'\n% END INLINED '+m[2]+'\n'
        return pattern.sub(sub,text)
    body=expand(base/'main.tex')
    z.close()
    if pattern.search(body):raise RuntimeError('Unexpanded TeX input')
    dst=OUT/'03_PRECEDING_COUNTERFACTUAL_COMPLETE.tex'
    dst.write_text('% Preserved 248-page intermediate: current TO/CAU and mixed additions are supplied separately in files01 and02.\n'+body,encoding='utf8')
    record(dst,[archive],'Recursively inline every line-start TeX input/include from the pinned preserved248-page ZIP, retaining complete input text with boundaries. Existing old edition, not a newly compiled manuscript; live cumulative edits do not alter this snapshot.')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--primary-sha',required=True)
    parser.add_argument('--analytic-dir',type=Path,required=True)
    args=parser.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    pin(MIXED/'COMPLETE_CONTROL_WORK.tex','78f16ab6df3629232e143aa6e7caf40cd3fb88a16ed040f1f3947fc3bd0b20c4')
    pin(MIXED/'FOLDER_MANIFEST.json','0a5d9502fa29e1b38e49becb12f26883de959b5f364968d5d85b4a38ae5f478b')
    manifest=json.loads((MIXED/'FOLDER_MANIFEST.json').read_text(encoding='utf8'))
    for row in manifest['files']:pin(MIXED/row['path'],row['sha256'])
    primary=TOTAL/'single_primary_boundary_control.tex'
    pin(primary,args.primary_sha)
    pin(TOTAL/'full_mixed_carrier_attachment.tex','5e960b547592a83952e88ff65ec22577f182c652a7be48c1da1dcbdb91df7abf')
    intro=TOTAL/'WEB_PROMPT_INTRO.md'
    prior=MIXED/'PROMPT.md'
    detail=prior.read_text(encoding='utf-8-sig')
    detail=detail.replace('Read COMPLETE_CONTROL_WORK.tex and DELIGNE_USAGE_OVERVIEW.md before continuing.','Read 01_MIXED_SUPPORT_CONTROL_COMPLETE.tex and the overview included in 10_EXACT_COMPARISONS_AND_REUSE.md before continuing.')
    detail=detail.replace('The counterfactual owner is integrating the coefficient-face diagram and the actual Weil II dyadic bootstrap separately.','The current coefficient-face diagram and complete Weil II dyadic bootstrap are now included as files02 and06.')
    detail=detail.replace('The local Zeta, counterfactual-integration, and transcript-audit tasks have been notified.','The supplied sources incorporate the coordinating calculations.')
    detail=detail.replace('Its actual inertia, graded multiplicities, and comparison with the original marked coefficient fibre still need calculation. Continue from this proved boundary result.','The additional single-primary marked t=0 inertia calculation is now supplied in file09. Continue from that result to the full mixed packet, its tensor-invariant characters, graded multiplicities and original-source comparison.')
    detail=detail.replace('Work first on the one-factor original family at u = 0 with t retained, then at its marked t = 0 fibre.','Reuse the completed single-primary marked t=0 calculation in file09. Continue on the one-factor original family at u=0 with t retained and with the full mixed packet, then carry the result through the ordered tensor family.')
    detail=detail.replace('Start with explicit original primary blocks and their coupling, proving every coordinate map and its inverse when you use local coordinates.','Reuse the explicit original single-primary block maps already supplied, and calculate the coupling of the full packet blocks, proving every additional coordinate map and its inverse.')
    prompt=OUT/'00_PROMPT.md'
    prompt.write_text(intro.read_text(encoding='utf-8-sig')+'\n'+detail,encoding='utf8')
    record(prompt,[intro,prior],'Current explicit task followed by complete preceding detailed continuation prompt with attachment filenames and coordination status updated.')
    copy('01_MIXED_SUPPORT_CONTROL_COMPLETE.tex',MIXED/'COMPLETE_CONTROL_WORK.tex')
    join('02_CURRENT_OBJECT_AND_SOURCE_MAPS.txt',[TOTAL/n for n in ['total_object.tex','coherent_assembly.tex','full_mixed_carrier_attachment.tex','coefficient_face_cochain_attachment.tex','mixed_amplification_identity.tex']], 'Current complete construction and exact source maps. TO/CAU supersede the older corresponding bodies in file03; all other inherited maps remain inputs. MFC/CFA/MAI are complete additional modules, with their original equation tags.')
    flatten_old()
    copy('04_ORIGINAL_PROGRAMME.pdf',OLD/'original_programme/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
    join('05_ORIGINAL_MIXED_CARRIERS.txt',[Path('reference-library:/Chatnotes/split_zero_projective_monads_surcomplex/split_support_absolute_arithmetic_curve_v5.tex'),ROOT/'output/split_zero_rh_tandem_2026-09-12/sources/Split_Support_Adelic_Weights_2026-09-11/sources/mixed_support_ledger.tex'],'Complete original mixed-carrier source witnesses. Retain original conventions and use the proved exact MFC attachment in file02.')
    join('06_DELIGNE_AMPLIFICATION_PROOFS.txt',[TOTAL/n for n in ['deligne_amplification.tex','weil_ii_amplification.tex','weil_ii_dyadic_bootstrap.tex']],'Complete proofs of the cited Deligne amplification mechanisms. WDB treats the final Weil II dyadic bootstrap. These arguments are not assertions of their arithmetic realization.')
    copy('07_WEIL_II_CURRENT_FRENCH.tex',WEIL/'S20_FR_record_export.tex')
    copy('08_WEIL_II_CURRENT_ENGLISH.tex',WEIL/'S20_EN_record_export.tex')
    copy('09_SINGLE_PRIMARY_BOUNDARY_CONTROL.tex',primary)
    intake=ROOT/'work/tau_f1_transcript_audit_20260913/continuation_intake'
    join('10_EXACT_COMPARISONS_AND_REUSE.md',[TOTAL/'WEB_SOURCE_READING_CORRECTIONS.md',MIXED/'DELIGNE_USAGE_OVERVIEW.md',intake/'MCF_READ.md',intake/'FILTRATIONS_READ.md',intake/'MARKED_METRIC_READ.md',TOTAL/'WEIL_II_SOURCE_LOCATOR.md'],'Complete exact comparison and reuse records. Historical scope statements refer to their recorded dates; current full bodies in files01/02/09 and explicit current reading corrections control subsequent completed calculations.')
    am=json.loads((args.analytic_dir/'MANIFEST.json').read_text(encoding='utf8'))
    analytic=[args.analytic_dir/row['git_path'] for row in am['files']]
    for p,row in zip(analytic,am['files']):pin(p,row['sha256'])
    if not all(p.is_file() for p in analytic):raise RuntimeError('Incomplete existing analytic input')
    join('11_EXISTING_ADAPTIVE_ARITHMETIC_CONTROL.md',analytic,'Complete already merged PR29 analytic controls; supplied as existing work, not new results of this continuation. Use the exact original source metrics and signed four-endpoint identities.')
    expected={'00_PROMPT.md','01_MIXED_SUPPORT_CONTROL_COMPLETE.tex','02_CURRENT_OBJECT_AND_SOURCE_MAPS.txt','03_PRECEDING_COUNTERFACTUAL_COMPLETE.tex','04_ORIGINAL_PROGRAMME.pdf','05_ORIGINAL_MIXED_CARRIERS.txt','06_DELIGNE_AMPLIFICATION_PROOFS.txt','07_WEIL_II_CURRENT_FRENCH.tex','08_WEIL_II_CURRENT_ENGLISH.tex','09_SINGLE_PRIMARY_BOUNDARY_CONTROL.tex','10_EXACT_COMPARISONS_AND_REUSE.md','11_EXISTING_ADAPTIVE_ARITHMETIC_CONTROL.md','12_SOURCE_MANIFEST.json'}
    extra={p.name for p in OUT.iterdir()}-expected
    if extra:raise RuntimeError('Unexpected items in drag folder: '+repr(extra))
    result={'created':datetime.now().astimezone().isoformat(),'file_count_including_manifest':13,'one_drag_limit':20,'no_remote_upload_performed':True,'files':records,'validation':{'main_package_pins':'PASS','complete_byte_block_retention':'PASS','flattened_old_inputs':'PASS','primary_source_pin':'PASS','MFC_source_pin':'PASS'}}
    (OUT/'12_SOURCE_MANIFEST.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf8')
    for row in records:pin(OUT/row['file'],row['sha256'])
    if {p.name for p in OUT.iterdir()}!=expected:raise RuntimeError('File count mismatch')
    print(json.dumps({'folder':str(OUT),'files':13,'bytes':sum(p.stat().st_size for p in OUT.iterdir()),'manifest_sha256':sha(OUT/'12_SOURCE_MANIFEST.json')},indent=2))

if __name__=='__main__':main()
