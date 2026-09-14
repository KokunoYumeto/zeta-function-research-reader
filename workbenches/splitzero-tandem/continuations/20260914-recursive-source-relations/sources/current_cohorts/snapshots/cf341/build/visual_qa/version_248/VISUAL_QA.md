# Final visual QA: 248-page edition

**PASS** for `Tau_Split_Zero_Total_Counterfactual.pdf`, SHA256 `8e13cfb73d11ba00ebf5ba02dfc97b510776c05d0936ebc9aff6d80db2aaac52`.

No clipped equations, label collisions, unintended glyph overlaps, orphan headings, or footer collisions were found. No repairs were needed. This receipt applies only to the recorded PDF bytes.

## Exact coverage and version comparison

All 248 physical PDF pages were rendered with Poppler at 90 dpi and checked for page geometry, absent glyph indicators, duplicate characters, and blank pages.

Against the sealed 224-page edition (SHA256 `08a5293305eb1fd7b0ce22816a2ded717d002bf7a5f44e7177560efbb3a1b5eb`), physical pages **1, 3, and 225–248** are new or changed. The other 222 page bodies match their previously reviewed versions. The 224-page PDF, renderings, review, and metrics remain preserved in `version_224/`.

The intermediate 247-page edition (SHA256 `6aa8f6a5e9ea44c03a4e6544e5a8a5b5714f093a7d626fb07f2e10c1d4973543`) received full-size inspection of pages 1, 3, and 225–240 before the final refinement arrived. The partial receipt and exact intermediate PDF/renderings remain in `version_247/`.

Against that intermediate edition, only final physical pages **3, 231, and 232** have changed body text. All other **245 matched page-body rasters are pixel-identical** in the rectangle `[0,65,745,985]` of the 90-dpi images, which excludes the running header and footer. The appended source pages after the HCA refinement move by one page without changes to their body layouts.

Final-edition full-size review inspected **3, 231–232, and 242–248**, covering every changed page and every previously pending page. Full-size review of final pages **1, 225–230, and 233–241** carries forward through the pixel-identical intermediate page bodies. Thus every page new or changed relative to the 224-page edition has full-size visual coverage, in addition to the existing baseline review.

The final appendix was also inspected in contact sheets covering **226–248**. All four appendix boxed expressions have visual coverage; both boxes on revised page 231, **HCA.29 and HCA.29a**, were additionally inspected in detailed crops. Title, contents, dense HCA formulas, the appended WBR/GF/TC proofs, bibliography, and short chapter endings are legible and correctly spaced.

## Automated checks and limits

The all-page extraction reports zero out-of-crop glyphs, zero missing-glyph candidates, zero duplicate-character candidates, and zero blank pages. The compiler log has no overfull or missing-character entries. Its fifteen underfull paragraph warnings have no observed layout defect. The high-overlap candidates are the same intentional assembled arrows, combining accents, and underbraces already reviewed in the baseline; the appended pages introduce none.

Supporting records are `layout_metrics.json`, `baseline_224_page_mapping_final.json`, `baseline_page_mapping.json` (comparison against 247), `body_raster_comparison.json`, and `FINAL_VISUAL_QA_RECEIPT.json`. This is a visual/layout receipt; mathematical validity and source/provenance closure are handled by the separate proof and repository reviews.
