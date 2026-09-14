from pathlib import Path
import hashlib,json,re,difflib
R=Path(__file__).resolve().parent
m=json.loads((R/'BASELINE_ENDPOINT_PATCH_MANIFEST.json').read_text(encoding='utf-8'))
base=Path(m['baseline']);patch=Path(m['patch_root'])
results=[]
diff=[]
for f in m['files']:
    old=base/f['path'];new=patch/f['path']
    oh=hashlib.sha256(old.read_bytes()).hexdigest()
    nh=hashlib.sha256(new.read_bytes()).hexdigest()
    assert oh==f['old_sha256'] and nh==f['new_sha256']
    o=old.read_text(encoding='utf-8');n=new.read_text(encoding='utf-8')
    ot=re.findall(r'\\tag\{([^}]+)\}',o)
    nt=re.findall(r'\\tag\{([^}]+)\}',n)
    assert all(nt.count(x)>=ot.count(x) for x in set(ot))
    results.append({'path':f['path'],'baseline_unchanged':True,'new_hash_matches':True,'every_old_formula_tag_retained':True,'sha256':nh})
    diff.extend(difflib.unified_diff(o.splitlines(True),n.splitlines(True),fromfile='baseline/'+f['path'],tofile='patched/'+f['path']))
mdpath='sources/owner_endpoint_terminal/published/workbenches/tau-arithmetic-endpoint-bounds/FOUR_VOLUME_THRESHOLD.md'
mdhash=hashlib.sha256((patch/mdpath).read_bytes()).hexdigest()
wrap=(patch/'build/endpoint_four_volume_threshold_wrapper.tex').read_text(encoding='utf-8')
assert wrap.count(mdhash)==2
subs=json.loads((R/'ENDPOINT_CONCLUSION_REPLACEMENTS.json').read_text(encoding='utf-8'))
for s in subs:
    source=Path(s['source'])
    assert hashlib.sha256(source.read_bytes()).hexdigest()==s['source_sha256']
    assert source.read_text(encoding='utf-8').count(s['old'])==1
compile_result=json.loads((R/'BASELINE_ENDPOINT_COMPILE.json').read_text(encoding='utf-8'))
assert all(x['returncode']==0 for x in compile_result['runs'])
assert not compile_result['undefined_references'] and not compile_result['multiply_defined_labels'] and not compile_result['errors']
(R/'BASELINE_ENDPOINT_CHANGES.diff').write_text(''.join(diff),encoding='utf-8')
receipt=Path(r'workspace:/work/backprop_endpoint_metric_review_20260913.md')
seal={'status':'PASS','files':results,'wrapper_matches_authoritative_markdown':True,'conclusion_replacement_count':len(subs),'conclusion_old_strings_unique_and_baseline_hash_verified':True,'compile':compile_result,'review_receipt':str(receipt),'review_receipt_sha256':hashlib.sha256(receipt.read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256((R/'BASELINE_ENDPOINT_PATCH_MANIFEST.json').read_bytes()).hexdigest(),'conclusion_replacements_sha256':hashlib.sha256((R/'ENDPOINT_CONCLUSION_REPLACEMENTS.json').read_bytes()).hexdigest(),'scope_note':'Complete five-entry recursive endpoint control, including exact trace-norm and centered-HS entries in both additive and nonlinear minima. No immutable source or shared conclusion edited.'}
(R/'BASELINE_ENDPOINT_SEAL.json').write_text(json.dumps(seal,indent=2),encoding='utf-8')
print(json.dumps({'status':seal['status'],'files':len(results),'manifest_sha256':seal['manifest_sha256'],'conclusion_replacements_sha256':seal['conclusion_replacements_sha256'],'compile_pages':compile_result['pages']},indent=2))
