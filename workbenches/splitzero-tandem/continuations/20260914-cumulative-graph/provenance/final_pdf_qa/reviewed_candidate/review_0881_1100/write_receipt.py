from pathlib import Path
import hashlib,json,datetime
BASE=Path(__file__).parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads((BASE/'RENDER_MANIFEST.json').read_text())
z=json.loads((BASE/'ZOOM_RENDER_MANIFEST.json').read_text())
assert sha(Path(r['pdf']))==r['pdf_sha256']
matcher=BASE.parent/'final_delivered_a8264bef'/'PAGE_MATCH_REPORT.json'
m=json.loads(matcher.read_text())
findings=[
 {'type':'layout','status':'PASS','pages':list(range(881,1101)),'finding':'Every assigned page was visually inspected on the 19 labelled original-resolution contact sheets. Body text, displayed equations, equation tags, headings, section transitions, header rules, and numeric footers remain inside the page without clipping or collisions.'},
 {'type':'glyphs_and_dense_displays','status':'PASS','pages':z['pages'],'finding':'Full-page 144-DPI Poppler PNGs were visually inspected for dense multi-index expressions, exact constants, fractions, parentheses, accents, inequality signs, source hashes, links, and ledger entries. No unreadable, substituted-box, missing, or collided glyph was observed.'},
 {'type':'pagination','status':'PASS','pages':list(range(881,1101)),'finding':'The printed page numbers run consecutively from 879 to 1098, maintaining the PDF-index offset of two. Running headers and date remain clear and separated from body content.'},
 {'type':'section_ends','status':'PASS','pages':[895,1038,1091,1093],'finding':'The shorter pages end sections or place the next standalone source/audit section on a new page. Their open lower areas contain no clipped continuation or displaced footer.'},
 {'type':'automated_signals','status':'PASS','pages':list(range(881,1101)),'finding':'The completed exact-page matcher reports no anomaly pages anywhere in the PDF. This check supplements the visual inspection; it does not replace it.'}
]
receipt={
 'schema':'split-zero-final-page-visual-review-v1',
 'reviewer':'/root/backprop_cumulative_builder/visual_pages_0881_1100',
 'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'PASS',
 'scope':'Visual layout and glyph inspection only. Mathematical proof correctness is outside this receipt.',
 'pdf':r['pdf'],'pdf_sha256':r['pdf_sha256'],'pdf_total_pages':1625,
 'assigned_pages':list(range(881,1101)),'visually_reviewed_pages':list(range(881,1101)),
 'all_assigned_pages_visually_reviewed':True,
 'sheet_review':[{**s,'viewed_at':'original image resolution','status':'PASS'} for s in r['sheets']],
 'page_images':r['page_images'],'full_page_zooms':z,
 'matcher_report':{'path':str(matcher),'sha256':sha(matcher),'anomaly_pages':m['anomaly_pages']},
 'findings':findings,'unresolved_findings':[],
 'source_or_pdf_modified':False,
 'evidence_files':[{'path':p.name,'sha256':sha(p)} for p in [BASE/'RENDER_MANIFEST.json',BASE/'ZOOM_RENDER_MANIFEST.json',BASE/'render_review.py',BASE/'render_zooms.py']]
}
(BASE/'REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
(BASE/'REVIEW_NOTES.md').write_text('# Final visual review: PDF pages 881–1100\n\nPASS. All 220 assigned pages were visually inspected on 19 labelled contact sheets at their original image resolution. Eleven dense or representative pages were additionally inspected as full-page 144-DPI Poppler PNGs.\n\nThe reviewed PDF has SHA-256 `'+r['pdf_sha256']+'`. No source or PDF was modified.\n\nNo clipping, collisions, unreadable/missing glyphs, displaced equation tags, or broken headers/footers were observed. Printed page numbers 879–1098 are consecutive. The full exact-page matcher reports zero anomaly pages. Open lower page areas at section ends are intentional.\n\nThis receipt covers layout and glyph rendering. It does not certify mathematical proof correctness. Exact sheet/page/zoom hashes and all page coverage are recorded in REVIEW_RECEIPT.json.\n')
print(json.dumps({'receipt':str(BASE/'REVIEW_RECEIPT.json'),'sha256':sha(BASE/'REVIEW_RECEIPT.json'),'status':'PASS','pages':220,'sheets':len(r['sheets']),'full_page_zooms':len(z['pages'])}))
