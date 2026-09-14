from pathlib import Path
import hashlib, json, shutil
from datetime import datetime, timezone

q=Path(__file__).resolve().parent
pdf=q.parents[1]/'Tau_Split_Zero_Total_Counterfactual.pdf'
expected='b923ea59918ad74e9573ac867de283b7da6c6fea127ed428cfa6148ed1cbabd7'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
metrics=json.loads((q/'layout_metrics.json').read_text())
mapping=json.loads((q/'baseline_page_mapping.json').read_text())
rasters=json.loads((q/'body_raster_comparison.json').read_text())
boxes=json.loads((q/'boxed_detail_index.json').read_text())
assert metrics['pages']==341 and metrics['sha256']==expected
assert mapping['continuation_sha256']==expected
assert rasters['compared_pages']==183 and not rasters['differing_body_raster_pages']
assert len(mapping['new_or_changed_pages'])==158 and len(boxes)==22
counts={k:sum(len(row[k]) for row in metrics['page_results']) for k in ['outside_crop','missing_glyph_candidates','duplicate_chars']}
assert not any(counts.values())
assert all(row['chars'] for row in metrics['page_results'])
assert not any('Overfull' in line or 'Missing character' in line for line in metrics['log_layout_warnings'])
delegated=['VISUAL_QA_341_PAGES_1_54.md','VISUAL_QA_341_PAGES_55_95.md']
for filename in delegated:
    assert expected in (q/filename).read_text()
full_size=list(range(1,96))+[118]+list(range(122,132))+list(range(328,342))
later=[n for n in mapping['new_or_changed_pages'] if n>95]
assert len(later)==65
def ranges(numbers):
    out=[]
    start=last=None
    for number in sorted(numbers):
        if start is None: start=last=number
        elif number==last+1: last=number
        else:
            out.append(str(start) if start==last else f'{start}-{last}')
            start=last=number
    if start is not None: out.append(str(start) if start==last else f'{start}-{last}')
    return ', '.join(out)
receipt={
 'status':'PASS',
 'scope':'Read-only visual and page-layout QA; no mathematical proof certification.',
 'sealed_utc':datetime.now(timezone.utc).isoformat(),
 'pdf_filename':pdf.name,'sha256':expected,'pages':341,
 'all_pages_rendered_and_geometry_checked':True,'render_engine':'Poppler pdftoppm','render_dpi':90,
 'frozen_248_sha256':mapping['frozen_baseline_sha256'],
 'new_or_changed_pages_relative_to_248':mapping['new_or_changed_pages'],
 'full_size_pages_inspected_in_341_edition':full_size,
 'later_changed_pages_inspected_in_contact_sheets':later,
 'matched_page_bodies_compared_by_raster':183,
 'body_raster_mismatches':[],
 'raster_comparison_crop_pixels':[0,65,745,985],
 'unchanged_page_bodies_reusing_sealed_baseline_visual_review':183,
 'delegated_read_only_review_reports':delegated,
 'detected_boxed_regions_inspected_in_detail':22,
 'geometry_counts':counts,
 'blank_pages':[],
 'overfull_or_missing_character_log_entries':[],
 'high_overlap_review':'Candidates are intentional assembled arrows, combining accents, and underbraces; no unintended visual collision found.',
 'visual_defects':[],'repairs':[],
 'valid_only_for_recorded_sha256':True,
}
(q/'FINAL_VISUAL_QA_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
report=f'''# Final visual QA: 341-page mixed edition

**PASS** for `Tau_Split_Zero_Total_Counterfactual.pdf`, SHA256 `{expected}`.

No clipped expressions, equation-label collisions, unintended glyph overlaps, broken glyphs, orphan headings, or footer collisions were found. No source/PDF edits or repairs were made during this QA. This receipt applies only to the recorded PDF bytes.

## Exact coverage

All 341 physical pages were rendered with Poppler at 90 dpi and checked for text/crop geometry, missing glyph indicators, duplicate characters, and blank pages.

The sealed 248-page baseline has SHA256 `{mapping['frozen_baseline_sha256']}` and remains preserved with its review receipts in `version_248/`. Header/footer-stripped text comparison identifies **158 new or changed pages**. The other **183 page-body rasters are pixel-identical** to matching previously reviewed baseline page bodies in the pixel rectangle `[0,65,745,985]`, which excludes the running header and footer.

The new/changed physical pages are **{ranges(mapping['new_or_changed_pages'])}**.

Full-size individual visual inspection in this edition covers **{ranges(full_size)}**: 120 physical pages, including title/contents, all of pages 1-95, the added Weil II material, and the complete marked-product appendix. Two read-only reviewers inspected every page in ranges 1-54 and 55-95; their exact-hash reports are `{delegated[0]}` and `{delegated[1]}`. The completed front-matter render was rechecked after rendering finished.

All **65 later changed pages** were inspected in eight contact sheets, `changed-remainder-341-01.png` through `changed-remainder-341-08.png`: **{ranges(later)}**. These include changed chapter/theorem numbers in reused body material as well as the new material inspected full size. All 158 new/changed pages therefore have current visual coverage, while the 183 identical page bodies retain the sealed baseline visual review.

All **22 detected boxed regions** on changed pages were additionally inspected in `boxed-details-01.png` and `boxed-details-02.png`. This count is a detector-region count: a multi-box display can contribute more than one region. All boxes and their equation numbers remain intact. Dense equations, the fibre table, diagrams, chapter transitions, the final appendix, and the end-page source paragraph are legible and contained.

## Automated checks and limits

The all-page extraction reports zero glyphs outside crop boxes, zero missing-glyph candidates, zero duplicate-character candidates, and zero blank pages. The compiler log has no overfull or missing-character entries. Eighteen underfull paragraph warnings have no observed clipping or collision. High-overlap candidates consist of intentional arrow components, combining accents, and underbraces, which were checked in the relevant full-size pages.

Supporting records are `layout_metrics.json`, `baseline_page_mapping.json`, `body_raster_comparison.json`, `boxed_detail_index.json`, and `FINAL_VISUAL_QA_RECEIPT.json`. This is a visual/layout receipt. Mathematical validity, provenance, and theorem/reference closure belong to the separate proof and repository reviews. The receipt does not concern later tensor material excluded from this PDF.
'''
(q/'VISUAL_QA.md').write_text(report,encoding='utf-8')
snapshot=q/'version_341'
snapshot.mkdir(exist_ok=True)
files=[q/'VISUAL_QA.md',q/'FINAL_VISUAL_QA_RECEIPT.json',q/'layout_metrics.json',q/'baseline_page_mapping.json',q/'body_raster_comparison.json',q/'boxed_detail_index.json']
files += [q/name for name in delegated]
files += [q/f'page-{n:03}.png' for n in range(1,342)]
files += [q/f'text-{n:03}.txt' for n in range(1,342)]
files += [q/f'contact-{n:03}-{min(n+8,341):03}.png' for n in range(1,342,9)]
files += [q/f'changed-remainder-341-{n:02}.png' for n in range(1,9)]
files += [q/f'boxed-details-{n:02}.png' for n in range(1,3)]
files += [q/name for name in ['check_layout.py','compare_248.py','compare_body_rasters_248.py','inspection_details.py','contact_remainder_341.py','seal_341.py']]
for p in files:
    assert p.is_file(),p
    shutil.copy2(p,snapshot/p.name)
shutil.copy2(pdf,snapshot/pdf.name)
print(json.dumps({'status':'PASS','pages':341,'sha256':expected,'full_size_review_pages':len(full_size),'later_changed_contact_pages':len(later),'report':str(q/'VISUAL_QA.md'),'versioned_snapshot':str(snapshot)},indent=2))
