from pathlib import Path
import json,hashlib,datetime,fitz
O=Path(r'workspace:\work\backpropagation_20260913\page_qa\review_0221_0440')
render=json.loads((O/'RENDER_MANIFEST.json').read_text())
pdf=Path(render['pdf'])
pin=render['pdf_sha256']
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==pin
matchpath=O.parent/'final_delivered_a8264bef/PAGE_MATCH_REPORT.json'
match=json.loads(matchpath.read_text())
records=[r for r in match['page_records'] if 221<=r['page']<=440]
assert len(records)==220
assert not any(r['anomalies'] for r in records)
zooms=[226,248,260,265,267,294,298,300,301,314,322,323,324,337,346,348,349,350,351,352,353,354,355,356,357,358,359,360,393,400,408,413,423,431,433,435]
doc=fitz.open(pdf)
footer=[]
for n in range(221,441):
 p=doc[n-1]
 val=p.get_text(clip=fitz.Rect(0,785,p.rect.width,p.rect.height)).strip()
 footer.append({'pdf_page':n,'printed_footer':val,'expected':str(n-2),'matches':val==str(n-2)})
assert all(x['matches'] for x in footer)
receipt={
 'schema':'split-zero.final-pdf-visual-range-review.v1',
 'reviewer':'/root/backprop_cumulative_builder/visual_pages_0221_0440',
 'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'PASS',
 'scope':'Read-only visual layout and glyph acceptance for assigned one-based PDF pages 221 through 440, inclusive. Mathematical validity is outside this visual-review receipt.',
 'pdf':str(pdf),'pdf_sha256':pin,'pdf_page_count':len(doc),'pdf_sha256_before_and_after_identical':True,
 'assigned_page_range':[221,440], 'visually_reviewed_pages':list(range(221,441)),
 'all_assigned_pages_visually_reviewed':True,
 'contact_sheet_count':len(render['sheets']),
 'contact_sheets_inspected_at_original_resolution':render['sheets'],
 'full_size_zoom_pages':zooms,
 'full_size_zooms':[r for r in render['pages'] if r['page'] in zooms],
 'all_rendered_page_images':render['pages'],
 'rendering':{'engine':'Poppler pdftoppm','page_png_width_pixels':840,'contact_cell_width_pixels':420,'pages_per_sheet':12,'contact_columns':3,'contact_rows':4,'label':'actual one-based PDF page number'},
 'review_observations':[
  'Every assigned page was viewed in its labelled contact cell. All 19 sheets were displayed at original resolution. The final sheet contains pages 437 through 440; its remaining grey cells are empty by construction.',
  'Dense displays, long fractions, matrices, rational tables, literal source blocks, signed-metric propagation, hyperlinked citations and parameter-connection formulas on the 36 recorded pages were additionally inspected at full PNG resolution.',
  'No clipped text, formula, table or equation label was observed. Long displays that place their tag on a separate lower line remain inside the body area and clear of the footer.',
  'No collisions, missing-glyph boxes, illegible mathematical glyphs or broken table rules were observed. Literal source notation in Sections 47 and 48 is readable at full PNG resolution and was preserved as rendered.',
  'Running headers and their date remain aligned above the rule on every assigned page. Printed footers run consecutively from 219 through 438, consistent with actual PDF pages 221 through 440. The explicit read-only footer extraction check agrees on all 220 pages.',
  'Section headings and transitions retain clear spacing. The range ends during the beginning of Section 61 on PDF page 440; continuation beyond the assigned range belongs to the adjacent review.'
 ],
 'findings':[], 'unresolved_findings':[], 'source_or_pdf_edits':[],
 'matcher_support':{'report':str(matchpath),'sha256':hashlib.sha256(matchpath.read_bytes()).hexdigest(),'assigned_page_records':len(records),'anomaly_pages_in_range':[],'automatic_inherited_body_matches_in_range':sum(r.get('automatic_body_acceptance',False) for r in records),'visual_queue_pages_in_range':sum(r.get('visual_review_required',False) for r in records),'note':'Matcher support supplements the visual review; it does not substitute for the recorded page inspections.'},
 'footer_crosscheck':footer,
 'render_manifest_sha256':hashlib.sha256((O/'RENDER_MANIFEST.json').read_bytes()).hexdigest(),
 'render_script_sha256':hashlib.sha256((O/'render.py').read_bytes()).hexdigest(),
 'skill':r'local:user-profile\.codex\plugins\cache\openai-primary-runtime\pdf\26.905.11957\skills\pdf\SKILL.md',
 'artifact_marker':'Not run: this task performs read-only renders and review, as required by the PDF skill.'
}
assert set(receipt['visually_reviewed_pages'])==set(range(221,441))
out=O/'REVIEW_RECEIPT.json';out.write_text(json.dumps(receipt,indent=2),encoding='utf-8')
(O/'REVIEW_NOTES.md').write_text('# Final PDF visual review: pages 221–440\n\nPASS. Every assigned page was inspected across 19 labelled contact sheets at original resolution. The 36 pages listed in REVIEW_RECEIPT.json were also inspected as full 840-pixel PNGs. No clipping, collisions, missing glyphs, unreadable symbols, broken table rules, or header/footer defects were observed. All 220 printed footers were visually checked and independently matched to PDF page minus two.\n\nThe PDF SHA-256 remained '+pin+' before and after review. The matcher reports no anomalies in this range. Mathematical proof validity is handled by the separate proof audit. No source or PDF was edited.\n',encoding='utf-8')
print(json.dumps({'receipt':str(out),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'pages':len(receipt['visually_reviewed_pages']),'full_zooms':len(zooms),'sheets':len(render['sheets']),'matcher':receipt['matcher_support']},indent=2))
