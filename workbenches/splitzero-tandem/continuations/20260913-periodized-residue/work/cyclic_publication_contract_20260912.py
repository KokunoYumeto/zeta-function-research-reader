"""Read-only identity and path checks shared by the cyclic edition workflow.

The edition specification names the complete intended additions. Counts are
derived from the final build; they are never used to substitute for membership.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import zipfile

W=Path(__file__).resolve().parents[1]
R=W/'output/split_zero_rh_tandem_2026-09-12'
BASE=R/'release_20260912f'
SPEC=W/'work/cyclic_publication_spec_20260912.json'
BASE_PINS={
    'PUBLIC_SOURCE_MANIFEST.json':'19f04640264ac408bdc8d55ac3b596efbb6fdb72b4fd46363e2db65d08595da0',
    'README.md':'4d51baec80a89b71413b217a5baf4cafe4b1f36af59948217a664fb191b79bac',
    'scripts/build_reader.py':'2f3c0c62d5e4cfa31d34da0556bf5976fa8a3abd88532ef5b2201754010e3c0b',
}
CORE_PROOFS={'nested_relative_frame_transition','nested_relative_frame_density',
             'nested_normal_observation','cyclic_sum_metric_connection','cyclic_sum_conormal'}
CORE_SOURCE_HASHES={
    '2cdfd5b25631464f9500dc5fd07c4c8f5c927c8877eb1bf076307ec5dcbc2e8c',
    '18f86ad411d0dfafc003aabddf25bccae2d38dcc4006c4d27e5be8aece9347b8',
    'c7050e1c2f76b31b72af1d237efd29f656fd34a92492e5a11f76d8bc55b2acd9',
    '202d7e9111c0a88fdd30c15554f3dd1e0907b2fc4fb2e11da129c97b10a053fd',
}

def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def relative(raw):
    value=str(raw).replace('\\','/')
    p=PurePosixPath(value)
    if not value or p.is_absolute() or ':' in value or any(s in ('','..','.') for s in value.split('/')):
        raise RuntimeError('Unsafe or noncanonical package-relative path: '+value)
    return p.as_posix()

def contained(root,raw):
    root=Path(root).resolve();p=root/relative(raw)
    if not p.resolve().is_relative_to(root):raise RuntimeError('Path leaves the intended package root')
    return p

def edition_spec(path=SPEC):
    spec=read(path)
    proofs=spec['new_proofs']
    if len(proofs)!=len(set(proofs)) or not CORE_PROOFS.issubset(set(proofs)):
        raise RuntimeError('Edition specification must retain every core continuation proof')
    for name in proofs:
        if '/' in relative(name) or name.endswith('.tex'):raise RuntimeError('Proof entries must be basenames without .tex')
    sources=spec['source_witnesses']
    if not CORE_SOURCE_HASHES.issubset({row['sha256'] for row in sources}):
        raise RuntimeError('All four newly supplied complete mathematical witnesses are required')
    for row in sources:relative(row['path'])
    return spec

def verify_base():
    for rel,digest in BASE_PINS.items():
        if sha(contained(BASE,rel))!=digest:raise RuntimeError('Immutable F baseline changed: '+rel)
    manifest=read(BASE/'PUBLIC_SOURCE_MANIFEST.json')
    names=[]
    for row in manifest['files']:
        rel=relative(row['path']);names.append(rel);path=contained(BASE,rel)
        if sha(path)!=row['sha256'] or path.stat().st_size!=row['bytes']:
            raise RuntimeError('Immutable F member changed: '+rel)
    expected=set(names)|set(BASE_PINS)
    actual={p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}
    if len(names)!=len(set(names)) or len(expected)!=544 or actual!=expected:
        raise RuntimeError('The complete immutable F inventory must contain its accepted 544 files')
    return manifest

def package_members(spec):
    """Verify all original ZIP/Git bytes; return exact/metadata public entries."""
    result=[]
    for package in spec.get('source_packages',[]):
        stage_rel=relative(package['stage']);stage=contained(R,stage_rel)
        provenance_rel=stage_rel+'/'+relative(package.get('provenance','LOCAL_STAGING_PROVENANCE.json'))
        prov=read(contained(R,provenance_rel))
        result.append({'path':provenance_rel,'role':'complete source staging provenance','exact_source_bytes':False})
        if package['kind']=='zip':
            archive_rel=stage_rel+'/'+relative(package['archive'])
            archive=contained(R,archive_rel)
            if sha(archive)!=package['sha256'] or archive.stat().st_size!=package['bytes']:
                raise RuntimeError('Original supplied archive identity differs: '+archive_rel)
            if prov['archive_sha256']!=package['sha256']:
                raise RuntimeError('Archive provenance identity differs: '+provenance_rel)
            entries=prov['files'];indexed={relative(row['archive_entry']):row for row in entries}
            with zipfile.ZipFile(archive) as z:
                infos=[info for info in z.infolist() if not info.is_dir()]
                if len(indexed)!=len(entries) or len(infos)!=package['members'] or len(infos)!=len(indexed) or {info.filename for info in infos}!=set(indexed):
                    raise RuntimeError('Original archive and its complete provenance membership differ')
                for info in infos:
                    rel=stage_rel+'/'+relative(info.filename);path=contained(R,rel);data=z.read(info)
                    if path.read_bytes()!=data or sha(path)!=indexed[info.filename]['sha256'] or len(data)!=indexed[info.filename]['bytes']:
                        raise RuntimeError('Original archive member changed: '+rel)
                    result.append({'path':rel,'role':'exact supplied archive member','exact_source_bytes':True})
            result.append({'path':archive_rel,'role':'exact supplied archive','exact_source_bytes':True})
        elif package['kind']=='git':
            if prov['implementation_commit']!=package['commit']:
                raise RuntimeError('Source repository revision differs from the selected delivery')
            entries=prov['source_files']
            if len(entries)!=package['members']:raise RuntimeError('Incomplete original Git delivery')
            for row in entries:
                rel=stage_rel+'/'+relative(row['path']);path=contained(R,rel);data=path.read_bytes()
                blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
                if sha(path)!=row['sha256'] or len(data)!=row['bytes'] or blob!=row['git_blob_sha1']:
                    raise RuntimeError('Original Git blob changed: '+rel)
                result.append({'path':rel,'role':'exact supplied Git source blob','exact_source_bytes':True})
            for directory in package.get('evidence_directories',[]):
                root=contained(stage,directory)
                for p in sorted(root.rglob('*')):
                    if p.is_file():result.append({'path':p.relative_to(R).as_posix(),'role':'observed remote source and CI evidence; no local Lean run','exact_source_bytes':False})
        else:raise RuntimeError('Unknown source package kind')
    return result

def required_current_paths(receipt):
    required=set(receipt['tex_inputs'])|{
        'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf',
        'build/build_receipt.json','build/source_receipt.json','build/source_appendices.tex',
        'build/source_audit_20260912g.json','build/qa/qa_receipt.json','build/qa/visual_review.json',
        'logbook/cyclic_final_integration_review_20260912.md','logbook/THEOREM_CROSSWALK.md',
        'scripts/build_paper.py','scripts/cyclic_source_appendix_adapter.py',
    }
    for row in receipt['source_notes']:required.update((row['source'],row['converted']))
    return {relative(rel) for rel in required}

def verify_production_receipts(root,receipt):
    root=Path(root)
    if read(root/'build/source_receipt.json')!=receipt['source_notes']:
        raise RuntimeError('Source conversion receipt differs from the compiled build receipt')
    audit=read(root/'build/source_audit_20260912g.json')
    if audit.get('pdf_sha256')!=receipt['pdf_sha256'] or audit.get('proof_fragments')!=len(receipt['tex_inputs'])-1 or audit.get('complete_source_appendices')!=len(receipt['source_notes']):
        raise RuntimeError('Final source audit must identify the current PDF and exact proof/source counts')
    audit_rows=audit['checks']+audit['sources']
    indexed={relative(row['path']):row for row in audit_rows}
    required=set(receipt['tex_inputs'])|{row['source'] for row in receipt['source_notes']}
    if len(indexed)!=len(audit_rows) or not required.issubset(set(indexed)):
        raise RuntimeError('Final source audit must cover every original proof and source witness')
    for rel in required:
        row=indexed[rel]
        matched=row.get('matches') if rel in receipt['tex_inputs'] else row.get('original_preserved')
        if matched is not True or sha(contained(root,rel))!=row['sha256']:
            raise RuntimeError('Source audit identity changed: '+rel)
    for row in receipt['source_notes']:
        audited=indexed[row['source']]
        if audited.get('converted')!=row['converted'] or sha(contained(root,row['converted']))!=audited.get('converted_sha256'):
            raise RuntimeError('Converted appendix changed after the final source audit: '+row['converted'])
