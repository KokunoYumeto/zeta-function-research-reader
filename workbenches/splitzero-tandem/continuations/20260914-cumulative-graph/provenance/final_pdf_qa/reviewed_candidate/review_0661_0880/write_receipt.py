from pathlib import Path
import fitz,json,hashlib,datetime
root=Path(r'workspace:\work\backpropagation_20260913\page_qa\review_0661_0880')
pdf=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
expected='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
assert sha(pdf)==expected
doc=fitz.open(pdf);pages=list(range(661,881));footer_checks=[]
for n in pages:
 p=doc[n-1];footer=p.get_text(clip=fitz.Rect(0,790,p.rect.width,p.rect.height)).strip()
 footer_checks.append({'page':n,'expected_printed':str(n-2),'actual':footer,'pass':footer==str(n-2)})
zooms=[663,686,704,715,731,759,764,775,803,811,829,842,781,800,847,863,864,877]
receipt={
 'scope':'Read-only rendered visual layout and glyph review; no mathematical proof acceptance asserted.',
 'reviewer':'/root/backprop_cumulative_builder/visual_pages_0661_0880',
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pdf':str(pdf),'pdf_sha256':expected,'total_pdf_pages':len(doc),
 'assigned_actual_one_based_pages':pages,'visually_inspected_actual_one_based_pages':pages,
 'all_assigned_pages_visually_inspected':True,
 'renderer':'Poppler pdftoppm, all assigned pages at 110 DPI RGB PNG; TCL.2 confirmation at 220 DPI.',
 'contact_sheet_method':'12 labelled actual pages per sheet, 3 columns, 4 rows, 420 pixel cells; every sheet opened with view_image detail original.',
 'contact_sheets':json.loads((root/'SHEETS.json').read_text()),
 'full_page_zooms':zooms,
 'zoom_confirmation_files':[{'path':str(root/'zoom220-0811.png'),'sha256':sha(root/'zoom220-0811.png')}],
 'page_png_files':[{'page':n,'path':str(root/f'page-{n:04d}.png'),'sha256':sha(root/f'page-{n:04d}.png')} for n in pages],
 'footer_checks':footer_checks,'all_footer_checks_pass':all(x['pass'] for x in footer_checks),
 'findings':[{'id':'TCL2_TAG_COLLISION','status':'requires_reflow','actual_page':811,'printed_page':809,'equation':'TCL.2','description':'The equation tag (TCL.2) overlaps the K+1 superscript of the rightmost quotient S[Z]/((Z-k rho)^{K+1}) in the second displayed row. Confirmed in original full-page image and 220 DPI re-render. Preserve all mathematical tokens and reflow the displayed rows/tag, then review revised PDF.'}],
 'other_results':[
  'All 19 contact sheets and 18 full-page zooms visually inspected.',
  'Running title and date headers, rules, section transitions, tables, boxes, diagrams, and footers otherwise display cleanly.',
  'All 220 assigned printed footer numbers match actual page minus two.',
  'No clipped page content, missing/replacement glyph blocks, or other confirmed collisions found.',
  'Tag-overlap screening additionally inspected actual pages 781 (SP.8), 800 (TPF.1), and 847 (AAM.26); glyph bounding boxes overlap but actual rendered ink is separated. These are not defects.',
  'The continued provenance table on pages 863–864 has readable repeated column headings and complete rows.',
  'No source or PDF was modified.'
 ],
 'status':'FAIL_REQUIRES_TCL2_REFLOW',
 'evidence_files':[{'path':str(root/x),'sha256':sha(root/x)} for x in ['make_sheets.py','scan_tags.py','GEOMETRY.json','TAG_OVERLAP_SCREEN.json']]
}
(root/'REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'receipt':str(root/'REVIEW_RECEIPT.json'),'sha256':sha(root/'REVIEW_RECEIPT.json'),'status':receipt['status'],'all_footer_checks_pass':receipt['all_footer_checks_pass']}))

