# Final visual QA receipt: physical pages 37–72

Result: **PASS**. Defects: **none found** in the assigned visual scope.

The inspected PDF is `output/tau_f1_transcript_audit_2026-09-13/publication/actual-cohomology-proofs.pdf`, 719,145 bytes, 98 physical pages, SHA-256 **c42419d417ba87b0d6e3945d2664d96efa245c1136aae4f1cf992165a0e5a42a**. This receipt applies only to that exact PDF.

## Exact coverage

All 36 physical pages from 37 through 72 were visually inspected through the following nine contact sheets in `work/tau_f1_transcript_audit_20260913/publication/renders/c42419d417ba/contacts/`:

| Contact sheet | Physical pages | Visual result |
|---|---|---|
| `contact-037-040.png` | 37, 38, 39, 40 | Chapter 4 opening, source definitions, Mellin maps and inverses fit; no clipping or overlap. |
| `contact-041-044.png` | 41, 42, 43, 44 | Boxed cocycle identities, nested sums, oriented integrals and support homotopies fit; labels remain separate. |
| `contact-045-048.png` | 45, 46, 47, 48 | Extension calculation, maps, source topology and tensor signs remain legible; equations fit margins. |
| `contact-049-052.png` | 49, 50, 51, 52 | Tensor/Gram identities fit; complete source hashes on page 52 wrap legibly; chapter ending is clean. |
| `contact-053-056.png` | 53, 54, 55, 56 | Chapter 5 opening, original spaces and full-jet equations remain visible; calligraphic/script glyphs are distinct. |
| `contact-057-060.png` | 57, 58, 59, 60 | Residue formulas, finite section, diagram and right-adjoint maps fit without collisions. |
| `contact-061-064.png` | 61, 62, 63, 64 | Source provenance on page 61 wraps; Chapter 6 opens correctly; dense Fourier and Mellin calculations remain visible. |
| `contact-065-068.png` | 65, 66, 67, 68 | Syzygy/balancing calculations, boxed identities, maps and source pins fit; no glyph or layout defects. |
| `contact-069-072.png` | 69, 70, 71, 72 | Chapter 7 opening and dense finite-moment/Gram equations fit; labels and proof-end symbols remain visible. |

Individual page images opened at original image detail by this reviewer: **43, 45, 48, 50, 51, 52, 53, 54, 57, 58, 59, 60**. An independent child reviewer opened every individual image for **61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72**. Thus the combined individual-image coverage is **24 pages** in addition to the gap-free contact coverage. All image paths use the exact hash directory `renders/c42419d417ba/` and filenames `page-NN.png`.

Physical pages 50–53 were specifically checked as individual full-page images. Page 52's four source pins are readable and contained within the text block; there is no visible literal `nolinkurl` artifact, clipped hash, or overlapping source entry. Script/calligraphic letters, overbars, hats, superscripts/subscripts, integral limits, nested summation indices, signs, boxes, and equation labels are visually distinct on the sampled dense pages.

The printed footer numbers are physical page minus one, consistently giving 36 through 71 in this range. Running headers and rules are present on body pages. Chapter openings **37, 53, 62, 69** intentionally omit their running headers and use the matching chapter layout. Section and chapter transitions are coherent. No black-square replacement glyph, text/equation overlap, clipped body content, or footer collision was found.

## Binding the inspection to the retained PDF and images

`HEADER_CHECKS.json` records SHA-256 for every assigned individual PNG. It also verifies by exact pixel comparison that every page thumbnail pasted into each inspected contact sheet equals a thumbnail of the corresponding current individual PNG, for all 36 pages.

Fresh independent Poppler renders of physical pages 51 and 52 at 100 dpi were saved only in this review directory as `fresh-51.png` and `fresh-52.png`. They are byte-identical to the supplied individual PNGs: page 51 SHA-256 `6d206c91221e180415af03f06565023c9a8d8272d12a5ee5497bb1f4a9d353af`; page 52 SHA-256 `333e0f47e4841e03f392247a7cd30be2842c7cb71175ee7d08c2511f2f4209d4`.

An apparent repeated-header omission in the tool's full-page image display was resolved using isolated header crops, exact pixel comparisons, and PDF header extraction. It is documented separately in `RESOLVED_DISPLAY_ANOMALY.md`; it is **not** an artifact defect and is excluded from the defect list.

This was read-only visual QA. No PDF, source proof, publication builder, shared source, or supplied render was modified. No mathematical claim validation is implied by this visual receipt.
