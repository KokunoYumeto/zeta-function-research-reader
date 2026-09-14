from pathlib import Path
import hashlib,json,datetime,fitz
root=Path(__file__).parent
render=json.loads((root/'RENDER_MANIFEST.json').read_text(encoding='utf-8'))
zooms=json.loads((root/'ZOOM_MANIFEST.json').read_text(encoding='utf-8'))
pdf=Path(render['pdf'])
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==render['sha256']
assert len(render['pages'])==220 and len(render['sheets'])==19 and len(render['page_images'])==220
assert sorted(p for sheet in render['sheets'] for p in sheet['pages'])==list(range(441,661))
for row in render['sheets']+render['page_images']+zooms:
    assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()==row['sha256']
doc=fitz.open(pdf)
numbering=[]
headers=[]
for n in range(441,661):
    page=doc[n-1]
    footer=page.get_text(clip=fitz.Rect(0,785,page.rect.width,page.rect.height))
    header=page.get_text(clip=fitz.Rect(0,0,page.rect.width,55))
    numbering.append({'actual_page':n,'printed_page':n-2,'footer_text':footer,'verified':footer.strip()==str(n-2)})
    headers.append({'actual_page':n,'header_text':header,'verified':header=='Split\u2011Zero Cohomology and Arithmetic Weight Control\n13 September 2026\n'})
assert all(r['verified'] for r in numbering+headers)
receipt={
 'status':'PASS',
 'scope':'Read-only visual layout and glyph QA for actual one-based PDF pages 441–660 inclusive. This receipt does not certify mathematical proofs or pages outside the assigned interval.',
 'pdf_path':str(pdf),'pdf_sha256':render['sha256'],'pdf_total_pages':len(doc),
 'reviewed_actual_pages':list(range(441,661)),
 'reviewed_page_count':220,
 'visual_method':'All 19 labelled contact sheets were opened through view_image at original resolution and individually inspected. Every assigned page appears exactly once in those sheets. Fifteen selected full-page 150 DPI Poppler renders were additionally opened at original resolution for dense equations, wide displays, cases, long hashes, tables, and displayed Python source.',
 'render_method':render['renderer'],'contact_sheet_dimensions_px':[1260,2480],'contact_sheet_cell_dimensions_px':[420,620],
 'contact_sheets_inspected':render['sheets'],
 'page_render_image_hashes':render['page_images'],
 'full_page_zoom_images_inspected':zooms,
 'findings':[],
 'inspection_observations':[
   'No clipping, text collisions, page-edge overflow, black replacement boxes, or visibly unreadable glyphs were found in the assigned pages.',
   'All assigned pages retain the consistent running title and date. Printed page numbering is consecutive 439–658, corresponding to actual PDF page minus two.',
   'Section and subsection headings, wrapped long titles, boxed formulas, equation tags, matrices, quotient diagrams, and the examined source tables remain separated and readable.',
   'Page 569 contains compact monospaced verifier source. Its full-page 150 DPI inspection confirmed readable characters, retained indentation, complete visible line endings, and no clipping.',
   'The supplementary full-page checks covered actual pages 453, 460, 471, 472, 486, 512, 535, 540, 569, 585, 619, 625, 642, 650, and 660.'
 ],
 'supplementary_geometry_anomalies':render['geometry_anomalies'],
 'footer_numbering_checks':numbering,'header_checks':headers,
 'pdf_hash_verified_before_render_and_after_review':True,
 'source_or_pdf_changes':False,
 'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewer':'/root/backprop_cumulative_builder/visual_pages_0441_0660'
}
(root/'REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'REVIEW_LOG.md').write_text('# Final PDF visual review: pages 441–660\n\nAll 220 assigned pages were visually inspected on 19 labelled original-resolution contact sheets, followed by 15 full-page 150 DPI views. No layout or glyph defects were found. This is a visual-layout acceptance only; no mathematical proof acceptance is asserted.\n\nThe checked PDF SHA-256 is `'+render['sha256']+'`. Complete image hashes, coverage, full-page zoom evidence, and all header/footer checks are in `REVIEW_RECEIPT.json`.\n',encoding='utf-8')
print(json.dumps({'receipt':str(root/'REVIEW_RECEIPT.json'),'receipt_sha256':hashlib.sha256((root/'REVIEW_RECEIPT.json').read_bytes()).hexdigest(),'status':'PASS','pages':220,'contact_sheets':19,'full_page_zooms':15}))
