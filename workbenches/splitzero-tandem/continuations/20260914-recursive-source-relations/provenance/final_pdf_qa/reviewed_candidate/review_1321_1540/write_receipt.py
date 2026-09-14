from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'RENDER_MANIFEST.json').read_text(encoding='utf-8'))
zooms=json.loads((ROOT/'ZOOM_MANIFEST.json').read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(Path(manifest['pdf']))==manifest['pdf_sha256']
pages=list(range(1321,1541))
assert [r['page'] for r in manifest['pages']]==pages
assert all(r['footer_text']==str(r['page']-2) for r in manifest['pages'])
assert sum(r['replacement_characters'] for r in manifest['pages'])==0
for sheet in manifest['sheets']:
    assert sha(Path(sheet['path']))==sheet['sha256']
for zoom in zooms:
    assert sha(Path(zoom['path']))==zoom['sha256']
receipt={
 'status':'PASS',
 'scope':'Read-only visual layout and glyph rendering review; no mathematical proof acceptance is asserted.',
 'reviewer':'/root/backprop_cumulative_builder/visual_pages_1321_1540',
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pdf_path':manifest['pdf'],'pdf_sha256':manifest['pdf_sha256'],
 'pdf_total_pages':1625,
 'reviewed_actual_one_based_pages':pages,
 'reviewed_actual_page_count':len(pages),
 'printed_page_range':[1319,1538],
 'method':[
  'Rendered every assigned page with Poppler pdftoppm at 100 dpi.',
  'Visually inspected all 19 labelled contact sheets at their original 1260 by 2500 pixel resolution, 12 pages per sheet with 420 pixel cells; the last sheet contains four assigned pages.',
  'Inspected all six selected full-page 200 dpi Poppler zooms at original resolution to verify small source-code blocks, Unicode continuation arrows and wide mathematical displays.',
  'Checked section headings, source attribution blocks, equation placement, headers, footers, sequential numbering and page boundaries on every assigned page.',
  'Cross-checked extracted footers on all 220 pages against the observed printed page offset and found no replacement characters; this supplements the visual check.'
 ],
 'all_assigned_pages_visually_inspected':True,
 'sheets':[{**s,'visually_inspected_original_resolution':True,'finding':'No clipping, collisions, missing-glyph boxes or header/footer defects observed.'} for s in manifest['sheets']],
 'rendered_pages':manifest['pages'],
 'full_page_zooms':[{**z,'visually_inspected_original_resolution':True,'finding':{
  1352:'Small monospaced arithmetic source formulas remain distinct and readable; no line clipping.',
  1368:'Reproduction command block remains readable; the wrapped long command uses a visible continuation arrow and stays inside the text area.',
  1398:'Wide original source/cohomology equations and their tags remain readable inside the page; the final display and footer are distinct.',
  1466:'Lean source Unicode symbols and indentation render distinctly; code remains inside the page and footer is clear.',
  1506:'The wide boxed norm-ratio inequality retains readable fractions, exponents and delimiters without clipping.',
  1523:'Raw-jet identities, Legendre formulas, equation tags and the final display retain distinct glyphs and clear page boundaries.'
 }[z['page']]} for z in zooms],
 'findings':[],
 'automated_supplement':{'replacement_character_count':0,'footer_mismatch_count':0},
 'evidence_manifest_sha256':sha(ROOT/'RENDER_MANIFEST.json'),
 'zoom_manifest_sha256':sha(ROOT/'ZOOM_MANIFEST.json'),
 'read_only_pdf_identity_rechecked':True
}
(ROOT/'REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
(ROOT/'REVIEW_NOTES.md').write_text('''# Final PDF visual review: actual pages 1321–1540

PASS for visual layout and glyph rendering on all 220 assigned pages. Every page was inspected through 19 labelled contact sheets at original resolution. Full-page 200 dpi zooms were additionally inspected for pages 1352, 1368, 1398, 1466, 1506 and 1523.

No clipping, collisions, unreadable glyphs, missing-glyph boxes, malformed headers or footer defects were observed. Printed page numbering consistently runs from 1319 to 1538, the expected two-page front-matter offset. All extracted footer values agree with that offset, and there are no replacement characters in the assigned page text.

The evidence receipt records every reviewed page and the hashes of all page renders, contact sheets and full-page zooms. The PDF identity was rechecked after review. This is a read-only visual review; mathematical claims and source completeness have their separate audits.
''',encoding='utf-8')
print(json.dumps({'receipt':str(ROOT/'REVIEW_RECEIPT.json'),'sha256':sha(ROOT/'REVIEW_RECEIPT.json'),'status':'PASS','pages':220,'sheets':19,'zooms':6}))
