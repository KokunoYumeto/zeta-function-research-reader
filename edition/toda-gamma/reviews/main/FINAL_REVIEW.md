# Independent main-reader integration QA

Decision: PASS for the exact repaired candidate below. No unresolved blocker was found in this bounded integration, navigation, source-preservation, added-proof, and layout review. This is a recommendation to the parent reviewer; this task did not promote, publish, or edit the mathematical source/PDF.

## Immutable candidate

- File: `../main_candidate/main.pdf`.
- 482 pages; 3,963,102 bytes.
- SHA-256: `8328222255737fa49c95d1f5aa6d30e981a072daeba68d297d8e838eb03b4676`.
- Build receipt: `../MAIN_CANDIDATE_BUILD.json`, SHA-256 `45f1ed5db6f0b5b914d82807e2474e762ea2fed71b67f175dee66543dca266cd`.
- TVB chapter SHA-256: `ccb55547440ec6b6fb3c9e0dda1a7a38616227a7795bf79d2f34f7d252bfe598`.
- Repaired Gamma chapter SHA-256: `a544e328249544463afa9445badbc5be9d55152a7068556b0b40219e7022998b`.
- Canonical `tex/main.pdf` was still the frozen 454-page baseline at review time, SHA-256 `ba51eb6261dc61da6ed72309c8d90e1714854054bc98a679105c9e2c3907af05`.

The machine receipt `repaired/MACHINE_QA.json` records all 59 candidate TeX paths, byte sizes and SHA-256 values; all 57 baseline TeX entries; complete reviewed input pins; render hashes; destination details; and 441 passing checks. The separate `FINAL_QA_SEAL.json` binds the actual human-readable review scope and these receipts. A machine-only receipt deliberately does not self-assert completed visual inspection.

## Source preservation and build

The complete four added source files were read: `TVB_HEADER.tex`, `GAMMA_HEADER.tex`, `GAMMA_PRIMITIVE.tex`, and `GAMMA_TODA_JOIN.tex`. Both complete mechanical recipes were read (`integrate_toda_reader.py`, the actual filename corresponding to the requested Toda recipe, and `integrate_gamma_reader.py`). Their pure transformation functions alone were evaluated from their ASTs; no recipe module-level code or source/PDF writer was executed.

The full transformed chapter strings agree exactly with candidate bytes and the transfer receipts. The original-source pins agree. All 10 Toda section headings and 49 explicit TVB equation tags survive. The complete Gamma source body, original section headings, equation tags/references, and labels survive the specified presentation transformations; the seven-row numerical table retains its values and the displayed chain is vertically typeset. The added literal primitive and complete GJ.1–GJ.8 join agree exactly with the reviewed additions.

All 59 candidate TeX files match their build snapshot and corresponding live TeX sources. All 56 inherited non-wrapper TeX files are byte-identical to the 454-page baseline; the old main wrapper differs only by the two new chapter input lines. All 57 frozen baseline snapshot files also match their pins.

The three recorded build passes have return code zero and matching retained log hashes. Recorded peak RSS values are 155,725,824; 156,459,008; and 156,160,000 bytes. These are verified owner build-record values, not independently remeasured build performance. The complete current main log was scanned: no overfull boxes, missing characters, undefined references/citations or controls, missing/duplicate destinations, or LaTeX errors were found. No build or heavy mathematics was repeated here.

## Added mathematical statements actually checked

GJ.1–GJ.4 preserve the original arithmetic measure, mass and gamma scale: the coefficient function is `(1+z^2)^(-lambda) M_h(arctan z)/c_lambda`, its real inverse uses `c_lambda sec(theta)^(2 lambda)`, and its value at zero is `mu_h/c_lambda`, not one. The generating-function substitution agrees with the primary [DLMF 18.23.7](https://dlmf.nist.gov/18.23.E7). The logarithm branches, unit-disk domain, real inverse interval, right-half-plane map, and compact-subset domination argument were read and checked. This is not an exchange justified merely by formal series notation.

GJ.5–GJ.8 correctly use degree `2N+j` for both source and full-relation Gram derivative integrands; the finite coefficient power, change of basis, Schur complement, inverse derivative recursion, and separate empty relation block at `N=q-1` preserve that dependence. Adjacent volumes require degree `2N+2`. The corresponding degree and nonzero/empty quotient qualifications in the added headers were checked.

GD.32a–GD.32b were checked against original TVB.8–TVB.9 and the surrounding GD definitions: the relation-correction vector is retained, the actual successive monic divisions supply the tensor primitive, both differential signs cancel, and the primitive has degree `k-1`. The boundary and its primitive are not identified. Empty relation blocks give zero correction/primitive.

No growing-`N,k` uniform estimate, subcubic conclusion, all-zero assertion, Lean certificate, interval certification of the Gamma numerical table, or independent proof audit of the entire inherited manuscript is claimed. The retained Gamma numerical agreement is explicitly described as regression evidence, not a certified error bound. Earlier standalone mathematical/source intake remains separate evidence, not an assertion that this task replayed it.

## Navigation and actual visual scope

Physical pages 9–10 and 425–455 were rendered at 110 dpi and all 33 were directly inspected in six contact sheets. Native full-page images were additionally directly inspected for pages 9–10 and 426–453: every new dense equation page, all boxed displays, the table (447), literal primitive (448), chain (450), analytic transform (451–452), finite-jet proof (452–453), and adjacent chapter transitions. Pages 425, 454 and 455 were inspected at contact-sheet scale only. This is not a claim that all 482 pages received a new visual review.

All PDF internal link page destinations were scanned for resolution. The 34 relevant outline entries (31 new and three adjacent inherited entries) were individually checked against their actual heading text at the named destination and their visible TOC links. All 36 relevant internal links resolve. Seven external annotation segments occur in the bounded range, six inherited; the sole new URI is the exact primary DLMF generating-function link and survives transfer. No claim is made to have fetched all inherited external links. The selected-page word bounding boxes do not cross the checked page/body margins; visual review found no clipping, collision, missing glyph, broken table, or unusable display.

One actual defect was found in initial PDF SHA-256 `26058d91b71e3b5ddae6552b36c3f261c6f3421d29019a61ecac026b26ceeb05`: physical page 10 concatenated the TOC number `42.12` with its title. The parent repaired only the optional TOC spacing in the GJ heading and rebuilt. The repaired page 10 was directly inspected at native size and is correct. Byte/hash reconstruction proves that this is the only change in the GJ source and integrated chapter; the other 58 candidate dependencies are unchanged from the first candidate. All 32 other images in the full 33-page bounded render set are byte-identical before/after repair. No all-482-page before/after pixel comparison was possible from the retained initial evidence, and none is asserted. Initial receipt and renders remain preserved beside the separate `repaired` evidence.

The PDF skill informed the distinction between contact-sheet and native-page review, the explicit render evidence, and the refusal to infer visual success from text/log checks alone. Its read-only route was used; no PDF authoring marker was added.
