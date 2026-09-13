"""Seal local proof, exact checks, source lineage, and actual visual review."""
from pathlib import Path
import hashlib
import json
import re
import fitz

ROOT=Path(__file__).resolve().parent
NAME='gamma_finite_metric_transfer'
STAMP='20260913'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def require(value,message):
    if not value:
        raise RuntimeError(message)

tex=ROOT/f'{NAME}_{STAMP}.tex'
pdf=ROOT/f'{NAME}_{STAMP}.pdf'
review=ROOT/f'{NAME}_independent_review_{STAMP}.md'
require(review.is_file(),'Independent complete proof review is not present')
replay=json.loads((ROOT/f'{NAME}_validation_{STAMP}.json').read_text())
require(replay['status']=='passed','Exact replay is incomplete')
require(replay['proof_sha256_at_execution']==digest(tex),'Replay proof byte pin differs')
require(replay['checker_sha256']==digest(ROOT/f'{NAME}_check_{STAMP}.py'),'Checker byte pin differs')
log=(ROOT/f'{NAME}_{STAMP}.log').read_text(errors='replace')
defects=re.findall(r'Overfull|Warning|Missing character|^!',log,re.M)
require(not defects,'LaTeX build has unresolved reported defects')
doc=fitz.open(pdf)
require(len(doc)==11,'Unexpected final PDF page count')
outside=[]
for index,page in enumerate(doc):
    for word in page.get_text('words'):
        if word[0]<0 or word[1]<0 or word[2]>page.rect.width or word[3]>page.rect.height:
            outside.append([index+1,word])
require(not outside,'A PDF word leaves its page')
tags=re.findall(r'\\tag\{(GMT\.[^}]+)\}',tex.read_text())
expected=[f'GMT.{j}' for j in range(1,43)]+['GMT.29a','GMT.29b']
require(sorted(tags)==sorted(expected),'The complete displayed equation labels changed')
qa=ROOT/f'{NAME}_qa_{STAMP}'
images=sorted(qa.glob('page-*.png'))
require(len(images)==11,'Final render coverage differs')
qa_record={
    'schema':'gmt-local-proof-build-visual-review-v1','status':'passed',
    'source_sha256':digest(tex),'pdf_sha256':digest(pdf),'pdf_bytes':pdf.stat().st_size,'pages':11,
    'latex_reported_defects':defects,'out_of_page_words':outside,
    'visual_reviewer':'gamma_finite_metric_transfer',
    'visual_method':'All 11 final Poppler page renders actually viewed in three contact sheets; complete equations, margins, headings and page transitions inspected.',
    'reviewed_pages':list(range(1,12)),
    'renders':[{'name':p.name,'sha256':digest(p)} for p in images],
    'contact_sheets':[{'name':p.name,'sha256':digest(p)} for p in sorted(qa.glob('contact-*.png'))],
    'equation_labels':tags,
    'proof_scope':'Complete finite maps and auxiliary bounded calibration; no growing-degree arithmetic estimate or RH assertion.'
}
(ROOT/f'{NAME}_qa_{STAMP}.json').write_text(json.dumps(qa_record,indent=2)+'\n',encoding='utf-8')
files=[]
for path in sorted(ROOT.glob(f'{NAME}*{STAMP}.*')):
    if path.name.endswith(('.aux','.out')) or path.name==f'{NAME}_manifest_{STAMP}.json':
        continue
    if path.is_file():
        files.append({'name':path.name,'bytes':path.stat().st_size,'sha256':digest(path)})
for path in images+sorted(qa.glob('contact-*.png')):
    files.append({'name':path.relative_to(ROOT).as_posix(),'bytes':path.stat().st_size,'sha256':digest(path)})
fe_manifest_path=ROOT/'gamma_finite_error_review_manifest_20260913.json'
fe_manifest=json.loads(fe_manifest_path.read_text())
support=[{'name':fe_manifest_path.name,'bytes':fe_manifest_path.stat().st_size,'sha256':digest(fe_manifest_path)}]
for entry in fe_manifest['files']:
    path=ROOT/entry['name']
    require(path.stat().st_size==entry['bytes'] and digest(path)==entry['sha256'],'FE support manifest byte mismatch')
    support.append(entry)
for name in ['toda_theta_input_tail_result_normal_20260912.json','toda_theta_input_tail_20260912.tex']:
    path=ROOT/name
    support.append({'name':name,'bytes':path.stat().st_size,'sha256':digest(path)})
manifest={
    'schema':'gamma-finite-metric-transfer-complete-files-v1','status':'ready-for-parent-integration',
    'files':files,'supporting_FE_manifest':{'name':fe_manifest_path.name,'sha256':digest(fe_manifest_path)},
    'support_files_for_FE_certificate':support,
    'new_results':['GMT.12--17 finite coefficient and polynomial-test error maps','GMT.19--20 exact boundary-resolvent remainder and derivatives','GMT.24--27 exact two-degree consecutive ratio and source recurrence','GMT.29a--31 certified least-lift coefficients, quadratic loss and quotient-dimensional determinant envelopes','GMT.39--42 positive and bounded calibration with relative Gamma ratio strictly below one'],
    'publication_performed':False,'cumulative_reader_modified':False,'lean_executed':False
}
(ROOT/f'{NAME}_manifest_{STAMP}.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'files':len(files),'source_sha256':digest(tex),'pdf_sha256':digest(pdf),'pages':11}))
