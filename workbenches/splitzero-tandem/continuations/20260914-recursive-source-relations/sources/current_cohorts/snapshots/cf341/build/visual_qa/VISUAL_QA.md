# Final visual QA: 341-page mixed edition

**PASS** for `Tau_Split_Zero_Total_Counterfactual.pdf`, SHA256 `b923ea59918ad74e9573ac867de283b7da6c6fea127ed428cfa6148ed1cbabd7`.

No clipped expressions, equation-label collisions, unintended glyph overlaps, broken glyphs, orphan headings, or footer collisions were found. No source/PDF edits or repairs were made during this QA. This receipt applies only to the recorded PDF bytes.

## Exact coverage

All 341 physical pages were rendered with Poppler at 90 dpi and checked for text/crop geometry, missing glyph indicators, duplicate characters, and blank pages.

The sealed 248-page baseline has SHA256 `8e13cfb73d11ba00ebf5ba02dfc97b510776c05d0936ebc9aff6d80db2aaac52` and remains preserved with its review receipts in `version_248/`. Header/footer-stripped text comparison identifies **158 new or changed pages**. The other **183 page-body rasters are pixel-identical** to matching previously reviewed baseline page bodies in the pixel rectangle `[0,65,745,985]`, which excludes the running header and footer.

The new/changed physical pages are **2-3, 5-95, 118, 122-131, 133, 138, 153, 169, 174-175, 177, 180-183, 185, 195, 205, 215, 220-221, 223, 225-227, 230, 236, 239, 251, 263-264, 266, 268, 277, 282, 286, 290, 297, 303-304, 312, 322-324, 328-341**.

Full-size individual visual inspection in this edition covers **1-95, 118, 122-131, 328-341**: 120 physical pages, including title/contents, all of pages 1-95, the added Weil II material, and the complete marked-product appendix. Two read-only reviewers inspected every page in ranges 1-54 and 55-95; their exact-hash reports are `VISUAL_QA_341_PAGES_1_54.md` and `VISUAL_QA_341_PAGES_55_95.md`. The completed front-matter render was rechecked after rendering finished.

All **65 later changed pages** were inspected in eight contact sheets, `changed-remainder-341-01.png` through `changed-remainder-341-08.png`: **118, 122-131, 133, 138, 153, 169, 174-175, 177, 180-183, 185, 195, 205, 215, 220-221, 223, 225-227, 230, 236, 239, 251, 263-264, 266, 268, 277, 282, 286, 290, 297, 303-304, 312, 322-324, 328-341**. These include changed chapter/theorem numbers in reused body material as well as the new material inspected full size. All 158 new/changed pages therefore have current visual coverage, while the 183 identical page bodies retain the sealed baseline visual review.

All **22 detected boxed regions** on changed pages were additionally inspected in `boxed-details-01.png` and `boxed-details-02.png`. This count is a detector-region count: a multi-box display can contribute more than one region. All boxes and their equation numbers remain intact. Dense equations, the fibre table, diagrams, chapter transitions, the final appendix, and the end-page source paragraph are legible and contained.

## Automated checks and limits

The all-page extraction reports zero glyphs outside crop boxes, zero missing-glyph candidates, zero duplicate-character candidates, and zero blank pages. The compiler log has no overfull or missing-character entries. Eighteen underfull paragraph warnings have no observed clipping or collision. High-overlap candidates consist of intentional arrow components, combining accents, and underbraces, which were checked in the relevant full-size pages.

Supporting records are `layout_metrics.json`, `baseline_page_mapping.json`, `body_raster_comparison.json`, `boxed_detail_index.json`, and `FINAL_VISUAL_QA_RECEIPT.json`. This is a visual/layout receipt. Mathematical validity, provenance, and theorem/reference closure belong to the separate proof and repository reviews. The receipt does not concern later tensor material excluded from this PDF.
