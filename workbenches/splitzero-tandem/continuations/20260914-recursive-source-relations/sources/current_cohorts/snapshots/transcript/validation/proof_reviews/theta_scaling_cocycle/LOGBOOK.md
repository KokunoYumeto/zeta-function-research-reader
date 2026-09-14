# Finite dilation cocycle calculation log

Scope: own this work directory and `output/tau_f1_transcript_audit_2026-09-13/proofs/theta_scaling_cocycle.*`; no shared master, Lean, browser, or publication.

The session user provenance is retained by the parent in `../USER_INPUTS.md`; its existing full transcript log was found on startup. The verbatim newly supplied steering is: “Yeah, it's also allowed to actually do those calculations, not just do redo instructions.”

## 2026-09-13

- Read workspace AGENTS.md completely. Read complete arithmetic_input.tex (A1–A19), primary Tau Base NOTE.md (1–52), and original transcript A1694 completely. Arithmetic source SHA256: a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2. Tau Base source SHA256: d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3.
- A1694 already proves a global continuous section, its dilation cocycle, support-face comparison, and boundary norm formula. Do not claim these as new. New work: actual finite-packet oriented Duhamel formula, all Taylor-unit and nilpotent coefficients, explicit seminorm convergence, finite/global coboundary bridge, full two-leg and tensor formulas.
- Derived `c_t=integral_0^t U_(exp(t-r)) phi_* ell exp(r A) dr`, `U_(exp t)R_ref-R_ref exp(t A)=Theta c_t`, `c_(t+s)=U_(exp t)c_s+c_t exp(s A)`.
- Face homotopies are `(c_t,0)` and `(0,-Fourier(c_t))`; their difference is retained cycle `(c_t,Fourier(c_t))`. Strict simultaneous naturality through both single-face inclusions is impossible for a nonzero c_t. A1694 already identifies this cycle globally; compute its exact finite restriction and synchronization.
- Delegated independent tensor/support sign review to child `review_homotopy_signs`; author remains responsible for topology, boundary mass, and finite/global comparison.

## Remaining work

1. Write complete self-contained MD and editable TeX retaining original two-leg action `(U_a,a U_(1/a))`, dx mass a, polynomial unit epsilon, and full jets.
2. Prove convergence, differentiability, source equations, exact global-section bridge `b_Z=Lambda R_ref`, and explicit tensor signs.
3. Review signs with child findings; compile standalone TeX, inspect log, record reproducible source/output hashes, and send concrete proof files to parent.

## Completion record

- Completed a self-contained 17-page proof in `theta_scaling_cocycle.md` and editable standalone TeX. Added an integration fragment without changing the shared master.
- Proved the finite dilation integral and its full Frechet seminorm estimates, smoothness, derivative, inverse-time and composition laws. Evaluated its original Gaussian kernel using oriented incomplete-gamma intervals with coefficients 2 and -3, and retained every parameter derivative representing nilpotent jets.
- Computed `k_a sigma=c_a-U_a b_Z+b_Z a^A`, `b_Z=Lambda R_ref`, with the exact infinitesimal bridge and unchanged epsilon extension class. Reproved the specific global Lambda construction used by A1694, including the retained cutoff gap.
- Retained both support homotopies, their nonzero H0 difference, the equivariant joint roof, and the nonzero minus-transport Ext class with its shifted-resolution sign. Child review independently verified these and the tensor signs; reviewed and integrated its full proof.
- Derived all tensor jet coefficients, the signed top homotopy, nonzero lower-degree homotopy mismatch, dx mass a^k, exact boundary-pairing identities and integrated infinitesimal defect.
- Root read and confirmed the main formulas. Corrected root-identified missing slash in equation (10). Recomputed the current raw A1694 SHA256 as a87bff4960c0a1742734e9e711780e0533ea76ba6f46ceab1fea115a2fd66f18.
- The PDF skill marker ran successfully once before PDF authoring. Build repaired missing mathrsfs package and preamble ordering locally. Final pdflatex two-pass build succeeded with no warnings, no overfull boxes and no underfull boxes. Long source hashes use xurl line breaks in TeX, preserving their exact bytes.
- Rendered all 17 PDF pages using Poppler, inspected all pages in three contact sheets, and inspected pages 8, 13, and 16 individually for gamma, tensor and pairing formulas. No clipped text, equation tags, missing glyphs, or layout defects observed. Text extraction contains no replacement characters.
- Independent numerical gamma-kernel checks passed 54 cases at 60 decimal digits, covering negative/zero/positive times and parameter derivatives of orders 0, 1, 2. Maximum scaled error 2.13916150176476746183077201848691770770289918299790120200351e-61. Deliberate lost-factor and reversed-orientation mutations were detected. These samples are not certificates of arithmetic zero locations; the proof establishes all complex parameters and all derivative orders used.
- No Lean, browser, remote publication, shared master edits, or unrelated files were used. Remaining parent-owned work is integration and delivery to the original web-session audit.

## Companion review repairs and remote intake continuation

- Parent requested two precise proof repairs after a full independent companion review. Section 6 now explicitly proves that Phi lands in the even Schwartz space and types P_V only on that domain. Section 8 now displays B_D^s=Theta(phi_*ell-D b_Z+b_Z A), derives W^s with both correct boundary terms, and integrates it in new equations (43a)-(43c). Both are completed with proofs, not left as qualifications.
- Rebuilt MD, standalone TeX, integration fragment and PDF together. The revised PDF is 18 pages; moved the source-pin section to its own page to avoid a three-line final-page orphan. All 18 pages were rendered and visually inspected; revised pages 12 and 16 were inspected individually. Build again has no warnings or overfull/underfull boxes. Sealed metadata updated to the revised proof.
- Parent additionally assigned a bounded remote-proof intake. Read both accepted scaling/reflection proofs in full, all supporting prose reviews/acceptance, and accepted UG1-19 formal-unit proof and final review/acceptance in full. Reused complete prior Tau Base/arithmetic reads and inspected the DS66-69 and XD12-22 dependency interfaces, complete primary-source-correction note and complete retained primary review.
- The accepted scaling source at 209385... had a narrow domain defect for the separate algebraic curve power map z^p after fixing arbitrary real p>0. Reported it immediately. Owner corrected that paragraph, leaving the theta action for all p>0; corrected version is 4e4cb6.... Retained both exact accepted original bytes from the archived v19 source and exact owner-corrected bytes, with their different hashes and a verified delta.
- Retained the reflection proof at 111f4c... and formal-unit proof at 9ded24..., full review e32e97... and acceptance ad3980..., supporting check records and nine named source interfaces. All 23 copies match source bytes; total 302,370 copied bytes. No accepted source was modified and no check replay was falsely reported.
- Formal gauge scope is complete. Remaining analytic step sent to parent: evaluate/continue the particular ordered formal pole inverse at nonzero u, calculate nu-pole and contour contributions, and control that actual comparison in original theta Gram/relation-volume topology. Entire finite C_a alone does not establish those analytic claims.
