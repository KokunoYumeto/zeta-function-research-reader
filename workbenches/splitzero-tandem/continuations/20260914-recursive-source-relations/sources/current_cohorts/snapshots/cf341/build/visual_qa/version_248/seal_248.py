from pathlib import Path
import hashlib, json, shutil
from datetime import datetime, timezone

q=Path(__file__).resolve().parent
pdf=q.parents[1]/'Tau_Split_Zero_Total_Counterfactual.pdf'
expected='8e13cfb73d11ba00ebf5ba02dfc97b510776c05d0936ebc9aff6d80db2aaac52'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
metrics=json.loads((q/'layout_metrics.json').read_text())
map247=json.loads((q/'baseline_page_mapping.json').read_text())
map224=json.loads((q/'baseline_224_page_mapping_final.json').read_text())
rasters=json.loads((q/'body_raster_comparison.json').read_text())
assert metrics['pages']==248 and metrics['sha256']==expected
assert rasters['compared_pages']==245 and not rasters['differing_body_raster_pages']
direct=[3,231,232]+list(range(242,249))
assert set(direct)==set(map247['pages_requiring_visual_review'])
counts={k:sum(len(row[k]) for row in metrics['page_results']) for k in ['outside_crop','missing_glyph_candidates','duplicate_chars']}
assert not any(counts.values())
assert all(row['chars'] for row in metrics['page_results'])
assert not any('Overfull' in line or 'Missing character' in line for line in metrics['log_layout_warnings'])
receipt={
 'status':'PASS',
 'scope':'Read-only visual and page-layout QA; no mathematical proof certification.',
 'sealed_utc':datetime.now(timezone.utc).isoformat(),
 'pdf_filename':pdf.name,'sha256':expected,'pages':248,
 'all_pages_rendered_and_geometry_checked':True,'render_engine':'Poppler pdftoppm','render_dpi':90,
 'frozen_224_sha256':map224['frozen_baseline_sha256'],
 'intermediate_247_sha256':map247['frozen_baseline_sha256'],
 'new_or_changed_pages_relative_to_224':map224['new_or_changed_pages'],
 'new_or_changed_pages_relative_to_247':map247['new_or_changed_pages'],
 'full_size_pages_inspected_in_final_248_edition':direct,
 'full_size_review_inherited_from_pixel_identical_247_page_bodies':[1]+list(range(225,231))+list(range(233,242)),
 'unchanged_224_page_bodies_reusing_sealed_baseline_visual_review':222,
 'matched_page_bodies_compared_by_raster':245,
 'body_raster_mismatches':[],
 'final_appendix_contact_sheets_inspected':['contact-226-234.png','contact-235-243.png','contact-244-248.png'],
 'new_or_changed_appendix_boxed_expressions_reviewed':4,
 'updated_boxes_inspected_in_detail':['HCA.29','HCA.29a'],
 'geometry_counts':counts,
 'blank_pages':[],
 'overfull_or_missing_character_log_entries':[],
 'high_overlap_review':'Only previously reviewed intentional arrow components, accents and underbraces; no new candidates on appended pages.',
 'visual_defects':[],'repairs':[],
 'valid_only_for_recorded_sha256':True,
}
(q/'FINAL_VISUAL_QA_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
report=f'''# Final visual QA: 248-page edition

**PASS** for `Tau_Split_Zero_Total_Counterfactual.pdf`, SHA256 `{expected}`.

No clipped equations, label collisions, unintended glyph overlaps, orphan headings, or footer collisions were found. No repairs were needed. This receipt applies only to the recorded PDF bytes.

## Exact coverage and version comparison

All 248 physical PDF pages were rendered with Poppler at 90 dpi and checked for page geometry, absent glyph indicators, duplicate characters, and blank pages.

Against the sealed 224-page edition (SHA256 `{map224['frozen_baseline_sha256']}`), physical pages **1, 3, and 225–248** are new or changed. The other 222 page bodies match their previously reviewed versions. The 224-page PDF, renderings, review, and metrics remain preserved in `version_224/`.

The intermediate 247-page edition (SHA256 `{map247['frozen_baseline_sha256']}`) received full-size inspection of pages 1, 3, and 225–240 before the final refinement arrived. The partial receipt and exact intermediate PDF/renderings remain in `version_247/`.

Against that intermediate edition, only final physical pages **3, 231, and 232** have changed body text. All other **245 matched page-body rasters are pixel-identical** in the rectangle `[0,65,745,985]` of the 90-dpi images, which excludes the running header and footer. The appended source pages after the HCA refinement move by one page without changes to their body layouts.

Final-edition full-size review inspected **3, 231–232, and 242–248**, covering every changed page and every previously pending page. Full-size review of final pages **1, 225–230, and 233–241** carries forward through the pixel-identical intermediate page bodies. Thus every page new or changed relative to the 224-page edition has full-size visual coverage, in addition to the existing baseline review.

The final appendix was also inspected in contact sheets covering **226–248**. All four appendix boxed expressions have visual coverage; both boxes on revised page 231, **HCA.29 and HCA.29a**, were additionally inspected in detailed crops. Title, contents, dense HCA formulas, the appended WBR/GF/TC proofs, bibliography, and short chapter endings are legible and correctly spaced.

## Automated checks and limits

The all-page extraction reports zero out-of-crop glyphs, zero missing-glyph candidates, zero duplicate-character candidates, and zero blank pages. The compiler log has no overfull or missing-character entries. Its fifteen underfull paragraph warnings have no observed layout defect. The high-overlap candidates are the same intentional assembled arrows, combining accents, and underbraces already reviewed in the baseline; the appended pages introduce none.

Supporting records are `layout_metrics.json`, `baseline_224_page_mapping_final.json`, `baseline_page_mapping.json` (comparison against 247), `body_raster_comparison.json`, and `FINAL_VISUAL_QA_RECEIPT.json`. This is a visual/layout receipt; mathematical validity and source/provenance closure are handled by the separate proof and repository reviews.
'''
(q/'VISUAL_QA.md').write_text(report,encoding='utf-8')
snapshot=q/'version_248'
snapshot.mkdir(exist_ok=True)
for p in list(q.iterdir()):
 if p.is_file():
  shutil.copy2(p,snapshot/p.name)
shutil.copy2(pdf,snapshot/pdf.name)
print(json.dumps({'status':'PASS','pages':248,'sha256':expected,'report':str(q/'VISUAL_QA.md'),'versioned_snapshot':str(snapshot)},indent=2))
