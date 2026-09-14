from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((P/'PATCH_MANIFEST.json').read_text(encoding='utf-8'))
for item in m['files']:
    assert sha(Path(item['derived']))==item['derived_sha256']
    assert sha(P/'originals'/item['target_relative'])==item['source_sha256']
original=(P/'originals/tex/cohorts/cf/31_HC.tex').read_text(encoding='utf-8')
derived=(P/'derived/tex/cohorts/cf/31_HC.tex').read_text(encoding='utf-8')
a='For the averaged original phase metrics the already proved stronger\n'
b='\\subsection{The sharper finite comparison'
old=original[original.index(a):original.index(b)]
new=derived[derived.index(a):derived.index(b)]
assert old==new
receipt=json.loads((P/'COMPILE_RECEIPT.json').read_text(encoding='utf-8'))
assert [r['returncode'] for r in receipt['runs']]==[0,0]
assert not receipt['undefined_references'] and not receipt['multiply_defined_labels'] and not receipt['errors']
review=P/'INDEPENDENT_REVIEW.md'
assert review.is_file(), 'Independent review receipt is required for sealing.'
text=review.read_text(encoding='utf-8')
assert 'PASS' in text
m['status']='complete; independently reviewed and compiled'
m['compile_receipt']={'path':str(P/'COMPILE_RECEIPT.json'),'sha256':sha(P/'COMPILE_RECEIPT.json'),'pages':receipt['pages'],'changed_source_overfull':False,'inherited_overfull':'Unmodified recursive_metric_transport.tex RMT16, line 297: 11.33386pt.'}
m['independent_review']={'path':str(review),'sha256':sha(review)}
m['averaged_quotient_preservation']='Text is identical after CRLF to LF conversion; original source bytes are retained exactly under originals/.'
m['additional_read_sources']=[]
B=P.parent.parent/'cumulative_source_v1'
for rel in ['tex/cohorts/cf/30_HT.tex','tex/cohorts/cf/15_PAM.tex']:
    p=B/rel
    m['additional_read_sources'].append({'path':str(p),'sha256':sha(p),'read_scope':'Complete HT1–18' if 'HT.tex' in rel else 'PSC.28–35 exact source-weighted Gram comparison and degree restriction'})
(P/'PATCH_MANIFEST.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print(json.dumps({'manifest_sha256':sha(P/'PATCH_MANIFEST.json'),'files':m['files'],'review_sha256':sha(review)},indent=2))
