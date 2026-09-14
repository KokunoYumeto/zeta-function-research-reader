from pathlib import Path
import hashlib,json,datetime
P=Path(__file__).parent
pdf=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
expected='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
zoom=[1113,1136,1137,1144,1179,1199,1205,1208,1219,1222,1233,1244,1249,1257,1258,1263,1265,1267,1276,1278,1283,1291,1295,1297,1300,1309,1310,1318]
def pin(f): return {'path':str(f.relative_to(P)), 'bytes':f.stat().st_size, 'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
d={
 'schema':'split-zero-cumulative-visual-review-v1',
 'reviewer':'/root/backprop_cumulative_builder/visual_pages_1101_1320',
 'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'NEEDS_CORRECTION',
 'pdf':str(pdf),'pdf_sha256':expected,'pdf_page_count':1625,
 'assigned_pages':list(range(1101,1321)), 'reviewed_pages':list(range(1101,1321)),
 'all_assigned_pages_visually_inspected':True,
 'method':'Every labelled contact sheet viewed at original 1680x1878 resolution, with each of 220 full-page 420px cells inspected; 28 selected dense or suspicious pages additionally viewed as full 144 DPI Poppler PNGs at original resolution.',
 'renderer':'Poppler pdftoppm',
 'full_resolution_pages_visually_inspected':zoom,
 'contact_sheets':[pin(f) for f in sorted((P/'sheets').glob('*.png'))],
 'full_resolution_images':[pin(f) for f in sorted((P/'zooms').glob('*.png'))],
 'thumbnail_images':[pin(f) for f in sorted((P/'thumbs').glob('*.png'))],
 'layout_check':{'clipping':'PASS','collisions':'PASS','legible_glyphs':'PASS','heading_hierarchy_and_transitions':'PASS','headers_and_footers':'PASS','page_numbering':'PASS; printed labels run 1099 through 1318, consistently actual PDF index minus 2','equation_labels':'PASS'},
 'semantic_rendering_check':'FAIL: one exponent-to-footnote conversion found and confirmed in active TeX.',
 'findings':[{
  'id':'VR1137-DEGREE-EXPONENT','severity':'must_correct','pdf_page':1137,'printed_page':1135,'section':'228.3.12 BF12',
  'observed':'N(2R)=2 followed by footnote marker 1, and q=2 followed by footnote marker 2; the bottom footnotes both read K:Q.',
  'source_confirmation':'tex/cohorts/transcript/LEDGER_COMPLETE.tex:3994-3995 contains N(2R)=2\\footnote{K:Q}\\textgreater1 and q=2\\footnote{K:Q}q.',
  'meaning':'The intended field-degree exponent [K:Q] appears to have been parsed as a Markdown footnote. The original source must govern the reversible correction.',
  'image':'zooms/page_1137.png','reported_to_parent':True,'resolved':False}],
 'informational_observations':['Sparse terminal pages 1145 and 1167 retain actual final source lines and have intact headers and footers.','Part IV transition at PDF 1202 and Part V at 1254 are followed by complete proof material; Part VI at 1312 is intentionally a part title page.','Original transcript ledger preserves literal inline source syntax; the distinct footnote conversion on 1137 is separately flagged.'],
 'matcher':{'path':str(P.parent/'final_delivered_a8264bef'/'PAGE_MATCH_REPORT.json'),'sha256':hashlib.sha256((P.parent/'final_delivered_a8264bef'/'PAGE_MATCH_REPORT.json').read_bytes()).hexdigest(),'assigned_anomaly_pages':[]},
 'scope':'Read-only visual layout and glyph inspection. Mathematical proof acceptance is a separate audit. No source or PDF was modified.',
 'source_or_pdf_mutations':False}
(P/'REVIEW_RECEIPT.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
(P/'REVIEW.md').write_text('''# Visual review of PDF pages 1101–1320

All 220 assigned pages were visually inspected on 19 labelled contact sheets at original resolution. Twenty-eight selected pages were also inspected as full 144 DPI Poppler images. Headers, footers, numbering, section transitions, formula placement, tables and glyphs are clean.

One correction is required before acceptance: on PDF page 1137 (printed 1135), section 228.3.12 BF12, the field-degree exponent is presented as numbered footnotes. The active TeX `tex/cohorts/transcript/LEDGER_COMPLETE.tex`, lines 3994–3995, confirms two `\\footnote{K:Q}` insertions where the intended exponent is apparently `[K:Q]`. The full source must govern the correction. The evidence image is `zooms/page_1137.png`. This defect was reported immediately to the cumulative builder.

No other defect was found, including in the dense ISM/RMT and restored R62 displays. No source or PDF was modified. `REVIEW_RECEIPT.json` pins the exact reviewed PDF and all inspected sheets and full-page images, lists complete page coverage, and records the unresolved defect. This receipt does not accept a later rebuilt PDF automatically.
''',encoding='utf-8')
print(json.dumps({'status':d['status'],'receipt':str(P/'REVIEW_RECEIPT.json'),'sha256':hashlib.sha256((P/'REVIEW_RECEIPT.json').read_bytes()).hexdigest(),'reviewed_pages':len(d['reviewed_pages']),'full_resolution_pages':len(zoom)}))
