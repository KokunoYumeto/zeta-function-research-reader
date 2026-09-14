# Exact review transfer across repagination

`cross_page_review_transfer.py` compares the reviewed 1,625-page PDF pinned at `a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252` with a caller-pinned final PDF. It preserves and reads the eight existing actual visual-review receipts. The known baseline defects on physical pages 811 and 1137 cannot receive inherited acceptance.

The comparison first indexes literal, unnormalized body glyph sequences and complete 144-DPI RGB page hashes. Complete page-pixel matches transfer only with equal page geometry and no current geometry/glyph anomaly. Otherwise the script requires literal body glyph identity, matching typed glyph geometry, and exact body-band RGB equality across page indices.

The fixed body band starts at 55 points and ends 56.89 points above the page bottom. Boundary-crossing glyphs, vectors, or images are flagged by the original matcher. The integer raster partition retains every pixel; no equation number, sign, or body character is excluded.

A differing printed page number is accepted only when all these checks hold:

1. Both footer glyph sets contain only the expected decimal page number. Header glyph content and geometry remain exact.
2. The complete complement of the union of the old and new numeric glyph boxes has identical pixels. This includes the full body, header, and remaining footer.
3. The entire new numeric box has exactly the pixels and glyph records of the already reviewed baseline page bearing that same printed number. The original, final, and reference glyph images are saved separately.

Every unmatched body, changed header, unexpected footer change, anomaly, or inherited baseline defect enters a queue for actual visual inspection. The script does not declare whole-document visual acceptance. The parent delivery task combines the queue with fresh inspection receipts.

Run with the exact final PDF hash and a fresh output directory beneath `page_qa`. The active authorized run uses:

```powershell
& 'runtime:python\python.exe' `
  'workspace:\work\backpropagation_20260913\page_qa\recovery_transfer\cross_page_review_transfer.py' `
  --new 'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf' `
  --new-sha256 '8bbd9da0d566fc5c5364a50da9b0976f9fcc21834de47822374966707b17c273' `
  --output 'workspace:\work\backpropagation_20260913\page_qa\final_corrected_8bbd9da0'
```

`IN_PROGRESS_QUEUE.json` reports the verified prefix while the process is running. `CROSS_PAGE_RENDER_TRANSFER.json` and `CHANGED_PAGE_VISUAL_QUEUE.json` report the complete final accounting once it finishes. The output manifest pins the produced files. No source or PDF is modified.

Eight bounded positive/negative primitive checks passed in `primitive_checks/PRIMITIVE_CHECKS.json`. They include an exact numeric replacement and rejection of individual unexpected body, header, or numeric-mask pixels. The independent code and exact-input receipt review is in `code_review/EXACT_SCRIPT_AND_RECEIPT_REVIEW.json`; its two generic parser-hardening observations do not affect the exact eight current receipts, which it checked independently. The executing script is preserved at its reviewed hash instead of being altered while comparison is running.
