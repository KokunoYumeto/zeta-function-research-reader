"""Record the performed visual review against exact rendered bytes."""
import hashlib,json
from pathlib import Path
base=Path(__file__).resolve().parent
qa=base/'endpoint_product_pdf_qa_20260913'
render=json.loads((qa/'render_receipt.json').read_text(encoding='utf-8'))
pdf=base/'endpoint_product_sharpening_20260913.pdf'
pdfhash=hashlib.sha256(pdf.read_bytes()).hexdigest()
if pdfhash!='d0d803c25cb8a839ea758d1512527f32878c36b457b0c69316b193b16330e668' or render['pdf']['sha256']!=pdfhash:raise RuntimeError('Reviewed PDF bytes changed')
for row in render['pages']+render['contacts']:
    if hashlib.sha256((qa/row['file']).read_bytes()).hexdigest()!=row['sha256']:raise RuntimeError('Reviewed render changed')
record={'schema':'endpoint-product-visual-review-v1','pdf':render['pdf'],'page_count':12,'reviewer':'endpoint_product_sharpening','contact_sheets_viewed':[r['file'] for r in render['contacts']],'physical_pages_covered':list(range(1,13)),'full_page_pngs_viewed':['page-02.png','page-07.png','page-09.png','page-12.png'],'clipping':False,'overlap':False,'missing_glyphs':False,'illegible_formula':False,'passed':True,'notes':['Every page viewed on the three contact sheets; original rendered page PNGs inspected for the recurrence, raw transfer, arithmetic penalty, and certified root interval.','The final compile contains zero overfull, undefined-control or missing-character warnings; one underfull prose paragraph remains visually legible.']}
(qa/'visual_review.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'pdf_sha256':pdfhash,'pages':12}))
