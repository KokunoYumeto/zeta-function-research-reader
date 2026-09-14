"""Stage three sealed whole AGT support proofs at new, previously absent paths."""
from pathlib import Path
import argparse,base64,hashlib,json,re,shutil
W=Path(__file__).resolve().parent
S=W/'cumulative_next_edition_staging_20260913_v19'
R=S/'reader'
P=W/'actual_tau_cumulative_conversion_20260913/aa_pa_addendum/READY_INPUTS.json'
PREFIX='sources/next_edition/all_degree_review_conversions_v1/'
LOCAL='intake_originals/all_degree_review_conversion_receipts_v1/'
def bp(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def pin(p):return bp(p.read_bytes())
def identity(row):return {k:row[k] for k in ('bytes','sha256')}
def inside(path,root):
    assert path.resolve().is_relative_to(root.resolve()),str(path)

def main(digest):
    assert S.is_dir() and R.is_dir()
    assert pin(P)['sha256']==digest
    d=json.loads(P.read_text(encoding='utf-8'))
    assert d['additional_complete_source_count']==3 and d['additional_complete_math_nodes']==440
    targets=[R/PREFIX,S/LOCAL]
    wrappers=[R/'tex/next_edition'/f'{row["key"]}_complete.tex' for row in d['proofs']]
    receipt=S/'ALL_DEGREE_REVIEW_CONVERSION_STAGE.json'
    selection=S/'ALL_DEGREE_REVIEW_SOURCE_SELECTION_INTERNAL.json'
    for target in targets+wrappers+[receipt,selection]:
        inside(target,S);assert not target.exists(),'Target already exists: '+str(target)
    primary=R/'tex/next_edition/AGT_complete.tex'
    assert primary.is_file();primary_before=pin(primary)
    # Validate the complete sealed inventory before creating any new target.
    for field in ('public_support','local_provenance_only'):
        for row in d[field]:
            src=Path(row['path']);rel=Path(row['relative_path'])
            assert not rel.is_absolute() and '..' not in rel.parts
            assert pin(src)==identity(row)
    ledger=[]
    for field,target in [('public_support',R/PREFIX),('local_provenance_only',S/LOCAL)]:
        target.mkdir(parents=True)
        for row in d[field]:
            src=Path(row['path']);dst=target/Path(row['relative_path']);inside(dst,target)
            dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
            assert pin(dst)==identity(row)
            ledger.append({'role':field,'staged':dst.relative_to(S).as_posix(),**identity(row)})
    routes=[]
    for row in d['proofs']:
        src=R/PREFIX/row['wrapper']['relative_path'];assert pin(src)==identity(row['wrapper'])
        raw=src.read_bytes();prepared=raw;replacements=[]
        for m in list(re.finditer(rb'\\(?:input|path)\{((?:build|sources)/[^}]+)\}',raw)):
            old=m.group(1);new=PREFIX.encode()+old
            assert prepared.count(old)==1
            prepared=prepared.replace(old,new,1)
            replacements.append({'old':base64.b64encode(old).decode(),'new':base64.b64encode(new).decode()})
        inverse=prepared
        for x in reversed(replacements):
            new=base64.b64decode(x['new']);old=base64.b64decode(x['old'])
            assert inverse.count(new)==1;inverse=inverse.replace(new,old,1)
        assert inverse==raw
        out=R/'tex/next_edition'/f'{row["key"]}_complete.tex';out.write_bytes(prepared)
        inputs=re.findall(rb'\\input\{([^}]+)\}',prepared);assert len(inputs)==1
        body=R/inputs[0].decode();inside(body,R/PREFIX);assert body.is_file()
        routes.append({'key':row['key'],'title':row['title'],
            'whole_wrapper':out.relative_to(R).as_posix(),**pin(out),
            'whole_source_body':body.relative_to(R).as_posix(),'whole_source_body_pin':pin(body),
            'original_wrapper':src.relative_to(R).as_posix(),'original_wrapper_pin':bp(raw),
            'exact_path_rebinding':replacements,'inverse_recovers_every_wrapper_byte':True,
            'proof_source_math_or_prose_changed':False,'complete_tags':row['complete_source_equation_tags'],
            'math_nodes':row['math_node_counts'],'proof_status':row['proof_status']})
    shutil.copy2(P,selection);assert pin(selection)==pin(P)
    assert pin(primary)==primary_before
    record={'schema':'next-edition-all-degree-review-complete-conversion-stage-v1',
        'status':'three-whole-supporting-proofs-staged-cumulative-layout-not-yet-accepted',
        'input_manifest':{'path':str(P),**pin(P)},'staged_files':ledger,'readable_routes':routes,
        'source_syntax_check':d['syntax_check'],'primitive_transcription':d['primitive_transcription'],
        'primary_AGT_wrapper_preserved':{'path':primary.relative_to(R).as_posix(),**primary_before},
        'AGT_original_85_file_companion_not_duplicated_or_modified':True,
        'all_targets_checked_absent_before_mutation':True,
        'current_or_baseline_files_changed':False,'new_cumulative_pdf_built':False,'visual_acceptance':False}
    receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
    print(json.dumps({'receipt':str(receipt),**pin(receipt),'complete_proofs':len(routes),
                     'public_files':len(d['public_support']),'local_provenance_files':len(d['local_provenance_only'])}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('manifest_sha256');a=p.parse_args();main(a.manifest_sha256)
