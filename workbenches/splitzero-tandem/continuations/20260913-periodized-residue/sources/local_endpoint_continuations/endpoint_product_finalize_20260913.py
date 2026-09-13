"""Build the exact support inventory and declared portable check jobs."""
import hashlib,json,re
from pathlib import Path
base=Path(__file__).resolve().parent
def load(name):return json.loads((base/name).read_text(encoding='utf-8'))
def pin(path):
    data=path.read_bytes()
    return {'path':path.relative_to(base).as_posix(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def need(value,why):
    if not value:raise RuntimeError(why)
source=base/'endpoint_product_sharpening_20260913.tex'
pdf=base/'endpoint_product_sharpening_20260913.pdf'
need(pin(source)['sha256']=='b4f9481976ad03bb8e321464f937d3777af15581241ece1f78aaa5c56e49b924','Source changed after complete review')
need(pin(pdf)['sha256']=='d0d803c25cb8a839ea758d1512527f32878c36b457b0c69316b193b16330e668','PDF changed after visual review')
review=load('endpoint_product_full_source_review_receipt_20260913.json')
need(review['passed'],'Full-source review failed')
need(review['reviewed_source']['sha256']==pin(source)['sha256'],'Stale full-source review')
need(review['primary_replay']['sha256']==pin(base/'endpoint_product_replay_20260913.json')['sha256'],'Review must bind the final actual portable replay')
ind=load('endpoint_product_independent_manifest_20260913.json')
for row in ind['files']:need(pin(base/row['path'])==row,'Changed independently reviewed support '+row['path'])
qa=load('endpoint_product_pdf_qa_20260913/visual_review.json')
need(qa['passed'] and qa['physical_pages_covered']==list(range(1,13)),'Visual coverage incomplete')
need(qa['pdf']['sha256']==pin(pdf)['sha256'],'Stale visual coverage')
deps=load('endpoint_product_dependencies_20260913/DEPENDENCIES.json')
for row in deps['sources']:
    actual=pin(base/'endpoint_product_dependencies_20260913'/row['file'])
    need(actual['bytes']==row['bytes'] and actual['sha256']==row['sha256'],'Changed dependency '+row['file'])

jobs=[]
primary=load('endpoint_product_replay_20260913.json')
for row in primary['runs']:
    jobs.append({'id':'ep-source-'+row['mode']+'-'+row['mutant'],'checker':'endpoint_product_check_20260913.py','optimized':row['mode']=='optimized','args':['--mutant',row['mutant'],'--output','fresh-result.json'],'output':'fresh-result.json','expected_exit_code':row['exit_code'],'expected_checks':415,'expected_failed':row['failed_count'],'record':row['record'],'check_count_field':'checks_executed','failed_count_field':'failed_count','companions':[],'scope':'Exact original-coordinate auxiliary source, quotient, radius, phase, window, Schur, transfer and rational-root calculations.'})
ind_receipt=load('endpoint_product_independent_receipt_20260913.json')
for row in ind_receipt['runs']:
    jobs.append({'id':'ep-scalar-'+('optimized' if row['optimized'] else 'normal')+'-'+row['mutation'],'checker':'endpoint_product_independent_checker_20260913.py','optimized':row['optimized'],'args':['--mutation',row['mutation'],'--output','fresh-result.json'],'output':'fresh-result.json','expected_exit_code':row['expected_exit_code'],'expected_checks':row['checks'],'expected_failed':row['failed'],'record':row['path'],'check_count_field':'check_count','failed_count_field':'failed_count','companions':[],'scope':'Independent exact scalar optimizer, window, equality and phase-feasibility calculations.'})
need(len(jobs)==26,'Portable job inventory count')
jobpath=base/'endpoint_product_portable_jobs_20260913.json'
jobpath.write_text(json.dumps({'schema':'endpoint-product-portable-jobs-v1','job_count':26,'jobs':jobs,'required_python_library':'sympy 1.13.1','execution':'Each job runs in its own fresh directory containing the declared checker; record and fixture results have no undeclared source-file dependency.'},indent=2)+'\n',encoding='utf-8')

names=['endpoint_product_sharpening_20260913.tex','endpoint_product_sharpening_20260913.pdf',
'endpoint_product_check_20260913.py','endpoint_product_replay_20260913.py','endpoint_product_replay_20260913.json',
'endpoint_product_README_20260913.md','endpoint_product_logbook_20260913.md',
'endpoint_product_render_20260913.py','endpoint_product_record_qa_20260913.py',
'endpoint_product_finalize_20260913.py','endpoint_product_portable_jobs_20260913.json',
'endpoint_product_independent_manifest_20260913.json']
paths={base/name for name in names}
paths.update(base/row['record'] for row in primary['runs'])
paths.update(base/row['path'] for row in ind['files'])
paths.update((base/'endpoint_product_dependencies_20260913').glob('*'))
paths.update((base/'endpoint_product_pdf_qa_20260913').glob('*'))
paths={p for p in paths if p.is_file()}
files=[pin(p) for p in sorted(paths)]
log=(base/'endpoint_product_sharpening_20260913.log').read_text(encoding='utf-8',errors='replace')
need(not any(x in log for x in ['Overfull \\hbox','Undefined control sequence','Missing character:']),'Unresolved PDF build warning')
manifest={'schema':'endpoint-product-complete-artifacts-v1','title':'Exact window products, sharp endpoint optimization, and original relation costs','proof':pin(source),'pdf':pin(pdf),'page_count':12,'tags':re.findall(r'\\tag\{(EP\.[^}]+)\}',source.read_text(encoding='utf-8')),'complete_proof_review':pin(base/'endpoint_product_full_source_review_receipt_20260913.json'),'visual_review':pin(base/'endpoint_product_pdf_qa_20260913/visual_review.json'),'portable_jobs':pin(jobpath),'file_count':len(files),'bytes':sum(r['bytes'] for r in files),'files':files,'scope':'Complete EP proof and exact auxiliary checks; actual arithmetic norm and balanced-window proofs are retained in full as dependencies. No arithmetic volume upper bound, numerical analytic constant certificate or Lean execution is claimed.','omitted_native_helpers':['endpoint_product_prepare_sources_20260913.py: native intake paths only; all exact copied dependencies are present.'],'pdf_build_warning_counts':{'overfull':0,'undefined_control':0,'missing_character':0,'underfull':log.count('Underfull \\hbox')}}
dest=base/'endpoint_product_manifest_20260913.json'
dest.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'manifest':pin(dest),'files':len(files),'bytes':manifest['bytes'],'jobs':26,'pages':12}))
