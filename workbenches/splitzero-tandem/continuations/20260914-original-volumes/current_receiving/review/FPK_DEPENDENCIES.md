# Fixed-packet Gamma kernel: exact source-dependency audit

Audit date: 2026-09-14. Reviewer: `mixed_row_morphism_review/fpk_source_dependencies`.

The assignment was to read the complete original fixed-packet kernel proof, locate and read the immediate mathematical providers needed by its actual claims, and return exact complete file locations and SHA256 pins. The parent subsequently fixed the scope to the claims used by the current TWA/FPK/TW calculation. This report does not turn unrelated later sections of a retained historical file into additional prerequisites for the fixed-packet theorem. No original mathematical source was edited, and no publication or compilation was performed.

## Result and scope

The original FPK source contains all 29 displayed formulas and their proof bodies. The cumulative `FPK.tex` copy identified below is byte-identical. Its fixed-packet asymptotic proof is available and was read completely. Its required Gamma generating-integral, polynomial-phase, orthogonality, and norm proofs are available in TG.7–TG.14 and were read completely. FPK independently proves its finite minimum-norm jet Gram, its confluent coordinate determinant, its coefficient asymptotics, and every limiting full jet block.

The finite FPK theorem fixes the original `k`, `chi`, all roots and all multiplicities while the source degree `N` tends to infinity. It proves no uniform remainder for changing `k` or `chi`, and no sign for a signed four-window difference. A later use at changing packet/order cannot be justified by these fixed-packet limits alone.

The cohomology injection AT2–AT2a occurs in FPK's source-realization paragraph after the fixed-packet theorem. That injection is not used to prove FPK.1–FPK.29 as a finite polynomial/jet determinant statement. Its original arithmetic realization nevertheless has exact source providers A1–A10 and CC.1–CC.6, identified below. Their required proof bodies were read; all original units, sum coordinates, and collided multiplicities remain present.

This is a claim-level dependency audit, not a claim that adding FPK and TG makes every section of the cumulative research paper standalone. The packaging owner must retain the required source bodies and their provider edges. A file's presence or hash is not evidence that an unread proof has been audited.

## Complete files and immutable pins

All paths in this table are real absolute paths. Byte counts and hashes were calculated from the original file bytes; line locators are one-based decoded text lines.

| ID | Complete file | SHA256 | Bytes / lines | Reading performed |
|---|---|---|---:|---|
| FPK | `C:/Users/[[user]]/Documents/math/work/rh_counterfactual_20260913/continuation2/fixed_packet_kernel/fixed_gamma_full_jet_asymptotic.tex` | `fb64e10661cfe211b5466fef341a87d6b881768c13b0863d9fcf78c2201217e4` | 20045 / 491 | Every line and proof body; FPK.1–29. |
| FPK cumulative copy | `C:/Users/[[user]]/Documents/math/work/rh_counterfactual_20260913/total_object/propagation_metric/compile/tex/continuation/FPK.tex` | `fb64e10661cfe211b5466fef341a87d6b881768c13b0863d9fcf78c2201217e4` | 20045 / 491 | Byte-identical to the fully read original. |
| TG | `C:/Users/[[user]]/Documents/math/work/rh_counterfactual_20260913/shared_thread_audit/segment29_40/sources/theta_gamma_reference.tex` | `a379a1e19de4ce885680e14bda466a37b4c1eb25228c19b931d573f58be167f9` | 22656 / 516 | Entire file read; FPK-required proofs TG.7–14 checked. Later external assertions are not independently verified by that reading. |
| AT | `C:/Users/[[user]]/Documents/math/work/rh_counterfactual_20260913/total_object/propagation_metric/compile/tex/modules/AT.tex` | `438fd058f4745056945a3a747eaeb63f2b36a0f146335ed72018acdb28b93727` | 30042 / 655 | Entire file read; dependency scope here AT2–AT6 and proof through AT10. |
| GC | `C:/Users/[[user]]/Documents/math/output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/gamma_exact_coefficient_join.tex` | `6830ccf4e3a24beae858ae38d46a254c1af350d47741178d63a830b796d005aa` | 39727 / 891 | Lines 1–260 read, including complete GC.1–15 proof bodies. Later source not audited here. |
| A | `C:/Users/[[user]]/Documents/math/output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/arithmetic_input.tex` | `a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2` | 14644 / 383 | Entire file read, including full A1–10 source, inverse, and packet-section proofs. |
| CC | `C:/Users/[[user]]/Documents/math/output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/cyclic_sum_conormal.tex` | `1182806be9a6e1ecde9b594a195a8cd3fa17b7259540fcd5617d044d06b05e79` | 48528 / 1161 | Lines 1–200 read; complete required CC.1–6 theorem and proof. Later source not audited here. |

The older `proof_inputs/AT.tex` is a different edition: `C:/Users/[[user]]/Documents/math/output/tau_split_zero_counterfactual_reconstruction_20260913/proof_inputs/AT.tex`, SHA256 `9fa19a509edf91f5aa0a9cb4762485449196d0b1ff521f2445f791fa3290cc75`, 17558 bytes / 409 lines. This audit read the current 655-line AT edition above. The two pins must not be interchanged.

## Required incoming claims, with their actual proof locations

| Receiving formulas / paragraph | Incoming mathematical claim | Exact provider and proof body | Status |
|---|---|---|---|
| FPK.1–2, FPK.7 | Fixed measure `sigma(u)=|Gamma(1/4+iu/2)|^2/(2pi)`; monic generating family; original norms and phases | TG.3 at line 33; full beta/Fourier/exponential-integrability/generating derivation TG.7–14, lines 77–190. FPK.7 then explicitly substitutes the original `S=c+w` coordinate into that generating function. | Required complete proof read and checked. |
| FPK.3–6 | Full normalized Taylor map, onto finite observation, minimum-norm quotient Gram, and exact confluent Vandermonde | Proved within FPK, lines 32–81. AT3–6, lines 54–115, gives the original remainder exact sequence and Gram convention; its full minimum-section and oriented Schur proof is lines 147–192. | Required proof internal to FPK; AT convention verified. |
| FPK.8–13 | Two singularities, exact leading constants, differentiated uniform coefficient remainder for fixed compact parameter sets | Entire proof internal to FPK, lines 84–196: subtract both finite singular lists, control the smooth circle remainder by repeated integration by parts, evaluate exact binomial/Gamma coefficients, prove the Gamma ratio by a beta integral, and retain the original polynomial norm. | Entire proof read. No external Darboux theorem or orthogonal-polynomial asymptotic is imported. |
| FPK.14–20 | Full off-critical and critical jet blocks, all mixed block limits, positivity of each limit | Internal FPK, lines 198–370. Complete analytic-germ inverse on off-critical blocks, full logarithmic derivative terms, small-index estimates, integrable Riemann sums, alternating pairing, critical logarithmic moments, and the two-region Cauchy–Schwarz argument are explicit. | Entire proof read. No diagonal-only replacement. |
| FPK.21–25 | Entire determinant constant and exponents, original CRT frame recovered | Internal FPK, lines 372–425, using FPK.3, 8, 14, 16–20. | Entire proof read; all fixed invertible coordinate factors are undone. |
| FPK.26–29 | Original tensor-Gamma comparison density, its mass, its polynomial norms, and constants | AT4 at lines 67–79 states the density and mass but cites the supplied source notes. The literal convolution proof is GC.10–13, lines 162–215. TG.7–14 proves the general positive Gamma-parameter norm formula. FPK.26–29 explicitly applies it with parameter `k/4` and full scalar mass. | All required provider proofs read. AT4 alone is a definition/source citation, not the convolution proof. |
| FPK paragraph after theorem; AT2–AT2a realization | Original arithmetic section `sigma_h:E_h -> Q`, full Taylor unit `upsilon_h=j_h(g/h)`, and same original tensor sum observation | A1–A10, lines 27–255: actual theta spaces, source multiplier, Euler inverses, full jet quotient, arithmetic section with inverse unit, and direct sum/projector. CC.1–6, lines 12–128: actual local finite algebra, all collided sum roots and maximum nilpotent orders, algebra injection `alpha`, and module injection `eta=M_U alpha` with full unit. | Required original-realization proof bodies read. This chain is separate from the finite FPK determinant proof. |
| AT4–AT5 positivity and moments, when original arithmetic source is invoked | Actual seed `g=2xi`, entire packet quotient, rapid strip decay, finite moments, positive mass | GC.1–9, lines 22–159: explicit theta seed, Gaussian Fourier/periodization calculation, Mellin identity including all factors, contour-rotation decay, inverse Mellin source, and actual density/Laplace integral. A1–A10 gives the exact source/section maps. | Required local proof bodies read. |

The GC convolution computation is literal:

\[
r_\lambda(u)=\frac{|\Gamma(\lambda+iu/2)|^2}{2\pi},\qquad
c_\lambda=2^{1-2\lambda}\Gamma(2\lambda),\qquad
\widehat r_\lambda(y)=c_\lambda(\cosh y)^{-2\lambda},
\]
\[
r_\lambda^{*k}=\frac{c_\lambda^k}{c_{k\lambda}}r_{k\lambda}.
\]

At the already existing order `lambda=1/4`, `c_lambda=sqrt(2pi)`, giving exactly AT4/FPK.26 and the mass `(2pi)^(k/2)`. The original source coordinate remains `S=k/2+iu`. No independent comparison order is chosen. FPK.27 follows by multiplying TG.11–12 at `lambda=k/4` by this same density scalar, not by assigning a unit mass.

The source-realization edge retains the complete unit as follows. A10 constructs `sigma_h=q R_ref` and proves that `R_ref(u)` has Mellin transform `(g/h) rem_h(upsilon_h^{-1}u)`. For an original polynomial `P`, the difference between `P` and `rem_h(upsilon_h^{-1}[upsilon_h P]_h)` is divisible by the original monic `h`; A3 and the proved Euler inverse identify its source image as a theta boundary. Thus `q(P(D)F_h)=sigma_h([upsilon_h P]_h)` with the original unit. Tensoring this actual equality in the original ordered factors and applying CC.6 at `r=1` yields AT2–AT2a. CC.2 gives the inverse of each full local unit by a finite nilpotent series and never erases its higher Taylor coefficients. AT3–AT6 then perform the finite monic-division and minimum-norm calculations directly on those same remainder coordinates.

## Exact FPK tag locators

All locations below refer to both byte-identical FPK files.

| Tag | Line | Tag | Line | Tag | Line |
|---|---:|---|---:|---|---:|
| FPK.1 | 18 | FPK.11 | 125 | FPK.21 | 374 |
| FPK.2 | 25 | FPK.12 | 150 | FPK.22 | 380 |
| FPK.3 | 39 | FPK.13 | 159 | FPK.23 | 393 |
| FPK.4 | 48 | FPK.14 | 213 | FPK.24 | 399 |
| FPK.5 | 55 | FPK.15 | 228 | FPK.25 | 406 |
| FPK.6 | 69 | FPK.16 | 260 | FPK.26 | 449 |
| FPK.7 | 92 | FPK.17 | 297 | FPK.27 | 457 |
| FPK.8 | 99 | FPK.18 | 305 | FPK.28 | 467 |
| FPK.9 | 106 | FPK.19 | 321 | FPK.29 | 484 |
| FPK.10 | 113 | FPK.20 | 368 | — | — |

## Foundational imports and honest closure boundary

TG.7–14 includes a beta-integral proof, the Fourier-inversion Gaussian approximation for its integrable transform, contour-shift exponential moments, dominated coefficient extraction, and the recurrence/norm derivation. NIST DLMF is mentioned for agreement of conventions; the required norms do not depend on reading NIST. Gamma recurrence, its holomorphic/nonvanishing properties on the relevant half-plane, basic Cauchy/Fourier calculus, finite-dimensional determinant algebra, and ordinary polynomial division are foundational facts used by this proof. This audit did not newly prove all of complex analysis.

GC.12 uses finite-measure Fourier uniqueness and multiplication of transforms. Both Gamma transforms in that identity are integrable, and its density equality is also obtained using the preceding Gaussian-regularized inversion argument. The citation to Fourier uniqueness must not be confused with a separate unproved Gamma-order conjecture.

A1–A10 actually constructs the theta map, Euler inverses, finite arithmetic section, and its full unit. Its proof invokes Schwartz Poisson summation for the general source, the elementary Möbius divisor identity, ordinary analytic continuation and Mellin/Fourier injectivity, rather than re-proving every foundational result. GC.3 gives the explicit Gaussian transform and periodization for the required seed. CC.1–6 proves its finite algebra claims by original-variable CRT, Bézout identities, exact monomial ideals, multinomial coefficients, and the retained nilpotent unit inverse.

The ambient tau-base derived pushforward in AT1 is an additional original-programme realization claim. Its full reproduction is not part of the finite FPK theorem or this requested AT2–AT6 dependency audit. The located source `C:/Users/[[user]]/Documents/math/output/tau_split_zero_counterfactual_reconstruction_20260913/proof_inputs/TAU.tex` has SHA256 `73878f1aa0fd9cf59c3fbfc9479a577ad550a5385841668b54e14943fff02e94` (49096 bytes / 1044 lines); only its opening source descriptions were read here. It must not be marked fully audited on this receipt.

## Unrelated later TG imports recorded without enlarging the FPK requirement

For provenance, the full TG file's later arithmetic formulas TG.16–22 refer to KL.23, KL.24, KL.27, and KL.32. Their exact complete provider is `C:/Users/[[user]]/Documents/math/output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/kernel_layer_continuation.tex`, SHA256 `a970bb6c108328045b5b3ec3009028a732949bdb1768f33a868d4c02307c2ae0` (28891 bytes / 651 lines). That file was read completely during this audit. KL.31–32 in turn imports the terminal identity KT.4; its located complete provider is `C:/Users/[[user]]/Documents/math/output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/kernel_terminal_continuation.tex`, SHA256 `6932e3c4d350aece95c003083d8938668d60bd81b2ebceba6eb1b78a510b2e9f` (36391 bytes / 897 lines). KT was located and hashed, not read here.

TG.25–28 also refers to the precise hypotheses of Lubinsky–Mhaskar–Saff (1988), and uses Hardy's infinitely-many-critical-zeros theorem. Those external proof bodies were not independently read in this bounded task. They are not incoming claims for FPK.1–29. The later Romik/Inoue discussion similarly does not supply an input to FPK's internal coefficient-asymptotic proof.

The entire `cyclic_sum_metric_connection.tex` was also read while locating the original sum map: `C:/Users/[[user]]/Documents/math/output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/cyclic_sum_metric_connection.tex`, SHA256 `7532559a5ec885504078d1b095c2bc7525b64d582cb6b8be967be3da480cb22d` (14194 bytes / 328 lines). Its CM.1–2 points to CC's complete original annihilator/unit construction. Its later normal-energy and frame-density inputs are outside the present FPK dependency scope.

## Delivery

The exact FPK, TG and AT pins were sent to the parent reviewer, the current-volume builder, and the receiving-text owner. The ready GC/A/CC pins and the finite-theorem versus original-realization distinction were also sent to all three. The standalone proof requirement remains a real packaging requirement: retain the actual required bodies, preserve complete originals for provenance, and record the exact selected proof spans. This report does not certify the uninspected contents of a delivered ZIP or a final PDF.
