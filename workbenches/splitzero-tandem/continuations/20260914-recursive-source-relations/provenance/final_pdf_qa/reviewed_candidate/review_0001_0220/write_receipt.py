from pathlib import Path
import hashlib,json,fitz,datetime

HERE=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((HERE/'RENDER_MANIFEST.json').read_text(encoding='utf-8'))
pdf=Path(manifest['pdf'])
assert sha(pdf)==manifest['pdf_sha256']
doc=fitz.open(pdf)
furniture=[]
for n in range(1,221):
 page=doc[n-1]
 header=page.get_textbox(fitz.Rect(0,0,page.rect.width,55))
 footer=page.get_textbox(fitz.Rect(0,785,page.rect.width,page.rect.height))
 expected='' if n==1 else str(2 if n==2 else n-2)
 assert footer.strip()==expected,(n,footer,expected)
 if n>1:
  assert 'Cohomology and Arithmetic Weight Control' in header,(n,header)
  assert '13 September 2026' in header,(n,header)
 furniture.append({'pdf_page':n,'header_literal':header,'footer_literal':footer,'expected_printed_number':expected,'matches':True})
(HERE/'PAGE_FURNITURE_CHECK.json').write_text(json.dumps(furniture,indent=2,ensure_ascii=False),encoding='utf-8')
zooms=[35,36,37,46,69,72,78,110,112,139,146,168,207,208]
pages={p['page']:p for p in manifest['pages']}
for entry in manifest['sheets']+manifest['pages']:
 assert sha(Path(entry['path']))==entry['sha256']
matcher=HERE.parent/'final_delivered_a8264bef'/'PAGE_MATCH_REPORT.json'
match=json.loads(matcher.read_text(encoding='utf-8'))
assert not [p for p in match['anomaly_pages'] if 1<=p<=220]
receipt={
 'schema':'split-zero-visual-review-receipt-v1',
 'reviewer':'/root/backprop_cumulative_builder/visual_pages_0001_0220',
 'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'PASS',
 'scope':'Read-only layout and rendered-glyph visual acceptance for actual one-based PDF pages 1 through 220, inclusive. No mathematical proof acceptance and no claim about pages 221 through 1625.',
 'pdf':str(pdf),'pdf_sha256':sha(pdf),'pdf_page_count':len(doc),
 'assigned_pages':list(range(1,221)),
 'visually_reviewed_pages':list(range(1,221)),
 'unreviewed_assigned_pages':[],
 'method':{'page_renderer':'PyMuPDF / MuPDF','page_raster_dpi':144,'page_image_size':[1191,1684],'contact_sheet_size':[1800,3520],'contact_sheet_grid':'3 columns x 4 rows; last sheet contains 4 actual pages','contact_sheet_cell_width':600,'inspection':'Every labelled contact sheet inspected at original resolution using view_image and original-detail forwarding. Full 144-DPI page images additionally inspected for dense formulas, diagrams, table rows and matrices.','source_or_pdf_mutations':False},
 'inspected_sheets':[dict(s,visually_inspected=True) for s in manifest['sheets']],
 'inspected_full_page_zooms':[dict(pages[n],visually_inspected=True) for n in zooms],
 'all_rendered_page_images':manifest['pages'],
 'findings':[],
 'acceptance_observations':[
  'All 220 assigned page bodies are contained within their pages; no visible clipping, text collision, broken glyph boxes, illegible mathematical symbols or dislocated equation tags found.',
  'Title page, abstract, all 30 contents pages, and transition to Part I were inspected. Long contents entries wrap within their allotted text area and page-number column.',
  'Running headers and the printed date are consistently readable. Page 1 has no printed number; page 2 displays 2; the numbering restarts at 1 on physical page 3 and then increases through 218 on physical page 220. This exact observed front-matter sequence is recorded rather than conflated with physical PDF page numbers.',
  'Full-page inspections confirmed the coefficient and quotient diagrams, moment and polynomial tables, dense chain-projector formulas, parity comparison table, and explicit calibration matrices render with readable glyphs and clear separation.',
  'The separate final matcher records zero page geometry/glyph anomalies in this assigned range. Visual acceptance above comes from rendered inspection, not from the matcher alone.'
 ],
 'supplemental_checks':[
  {'path':str(HERE/'PAGE_FURNITURE_CHECK.json'),'sha256':sha(HERE/'PAGE_FURNITURE_CHECK.json'),'scope':'Literal header/footer extraction cross-check for the same visually inspected pages.'},
  {'path':str(matcher),'sha256':sha(matcher),'scope':'Read-only consultation: zero anomaly pages intersect pages 1–220.'},
  {'path':str(HERE/'RENDER_MANIFEST.json'),'sha256':sha(HERE/'RENDER_MANIFEST.json')},
  {'path':str(HERE/'render_review.py'),'sha256':sha(HERE/'render_review.py')}
 ],
 'final_pdf_sha256_matches_initial':sha(pdf)==manifest['pdf_sha256']
}
out=HERE/'REVIEW_RECEIPT.json'
out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'status':'PASS','reviewed_pages':220,'inspected_sheets':len(manifest['sheets']),'full_page_zooms':zooms,'receipt':str(out),'receipt_sha256':sha(out)},indent=2))
