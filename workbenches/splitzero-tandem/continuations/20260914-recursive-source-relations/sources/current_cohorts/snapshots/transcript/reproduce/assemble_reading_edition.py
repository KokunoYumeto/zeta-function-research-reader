"""Combine visually verified volumes and seal a portable source bundle."""
from pathlib import Path
import datetime, hashlib, json, zipfile
import fitz

OUT=Path(__file__).resolve().parents[1]
items=[
 ('Passage ledger and supplementary continuation','ledger_publication/ledger.pdf','Ledger-'),
 ('Complete continuation proofs','publication/actual-cohomology-proofs.pdf','Proofs-')
]
target=OUT/'Tau_Base_Transcript_Audit_and_Completed_Proofs.pdf'
combined=fitz.open();toc=[];labels=[];sources=[];offset=0
for title,rel,prefix in items:
 p=OUT/rel
 doc=fitz.open(p)
 if not len(doc):raise RuntimeError('empty volume')
 combined.insert_pdf(doc)
 toc.append([1,title,offset+1])
 for level,label,page in doc.get_toc():
  if page>0:toc.append([level+1,label,offset+page])
 labels.append({'startpage':offset,'prefix':prefix,'style':'D','firstpagenum':1})
 sources.append({'path':rel,'pages':len(doc),'offset':offset,
                 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 offset+=len(doc);doc.close()
combined.set_toc(toc)
combined.set_page_labels(labels)
combined.set_metadata({'title':'Original tau-base cohomology: transcript audit and completed proofs',
 'author':'','subject':'115 passage findings and thirteen complete proof chapters, with provenance and continuation',
 'creator':'LaTeX and PyMuPDF','keywords':'tau base; theta cohomology; transcript audit'})
combined.save(target,garbage=4,deflate=True)
combined.close()

render_dir=OUT/'validation/final_reading_edition'
render_dir.mkdir(parents=True,exist_ok=True)
new=fitz.open(target)
checks=[]
for source in sources:
 doc=fitz.open(OUT/source['path'])
 for i,page in enumerate(doc):
  copied=new[source['offset']+i]
  ok=(page.rect==copied.rect and page.get_text()==copied.get_text()
      and page.get_pixmap(matrix=fitz.Matrix(.25,.25),alpha=False).samples
          ==copied.get_pixmap(matrix=fitz.Matrix(.25,.25),alpha=False).samples)
  if not ok:raise RuntimeError(f"page-copy mismatch {source['path']} {i+1}")
  checks.append({'source':source['path'],'source_page':i+1,'final_page':source['offset']+i+1,'identical_text_geometry_raster':True})
 for local in sorted({0,min(1,len(doc)-1),len(doc)-1}):
  idx=source['offset']+local
  new[idx].get_pixmap(matrix=fitz.Matrix(1.1,1.1),alpha=False).save(render_dir/f'final-page-{idx+1:03d}.png')
 doc.close()
receipt={'status':'PASS','pages':len(new),'sources':sources,'bookmarks':len(toc),
 'all_pages_text_geometry_and_low_resolution_raster_identical':True,'checks':checks,
 'pdf_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'scope':'No page scaling, content editing or raster replacement. Final PDF copies every page of both independently visually inspected source volumes; all pages compared for exact text, geometry and raster equality.'}
new.close()
(render_dir/'COMBINATION_QA.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'pdf':str(target),'pages':offset,'sha256':receipt['pdf_sha256']}))
