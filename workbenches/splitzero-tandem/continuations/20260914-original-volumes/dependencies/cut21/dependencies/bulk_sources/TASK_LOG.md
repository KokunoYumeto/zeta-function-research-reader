# Original relation bulk control — durable state

Completed the root-assigned next analytic calculation in this new directory. Existing sealed reader inputs were not touched.

The main proof is ORIGINAL_RELATION_BULK_CONTROL.tex (BRD1–42 plus BRD41a), SHA256 4d6e3df419edcedbe7e66e6f802bdeca6e088d9036c5b4c17692517995ebcba9. It keeps k=4l+1, e=1+k(m−1), q=e(k+1)^2, the full quartet roots and multiplicities, original S coordinates, exact q Jacobian and all Gram dimensions.

The root-requested exterior calculation was completed: log(|chi(c+iy)|²/|y|^(2q))=p2/y²+E, p2=q k(k+2)(d−g)/3, and the full convergent even-root series gives |E|≤q tau²/[2(1−tau)]. At y=qz the m=1 deformation converges to exp((d−g)/(3z²)); fixed m>=2 converges to 1, with exact finite uniform bounds.

The original relation maps and bulk Loewner comparisons were then proved. For actual ranks r=q,q+1 the determinant error is one-sided [−2r DeltaChi, 2r DeltaChi+r DeltaF], with DeltaF the full original sum of t_j²/(q² epsilon²). Both original tails first remain exact positive forms and exact log determinants.

The work then controlled both tails by complete calculations. Gamma Euler-contour upper and reflection lower bounds, explicit shifted Legendre norms/evaluation kernel, and actual ±root pairs prove H_inner<=kappaI H_bulk and H_far<=kappaF H_bulk. With epsilon=2^-10 and outer64, kappaI is bounded by an explicit r² exp(−2q) term and kappaF by 512q exp(−19q)/(59 sqrt(cos1)). Original numerator f factors are retained throughout. The threshold is Rmax/q<=epsilon/2 and tmax/q<=epsilon; k>=2048 sqrt(d+g) suffices, ensuring the density Taylor radius remains strict even at equality.

Thus the complete original high relation determinant ratios equal 2lr log q + log det K_l,r/det K_0,r, up to the proved finite BRD41a error, which is o(q) for each fixed original packet. BRD42 pushes this directly through the exact GSR signed return. The explicit bulk determinant ratios remain the next quantity to evaluate; this calculation assigns no unproved value to them and assumes no tail vanishes.

Independent constants proof IBC1–33 and full tail proof FTC1–26 are alongside the main source, with their own receipts. Root read the main proof and IBC completely; a separate checker read the actual tail implementation. One parameterized-cutoff defect was repaired: the general far-tail estimate now uses F_B and specializes B=64 to recover the fixed original region. Full Euler/keyhole reflection and Legendre norm derivations were added at root request. No unresolved review finding remains. BULK_CONTROL_RECEIPT.json pins all three TeX sources.

Root separately assigned the rank-l contrast improvement to pr31_joint_application; its contrast_transport.tex is an adjacent independent calculation. It is not silently inserted into this finished main proof or into the current reader.


### 2026-09-14T15:26:31.002375+00:00 — full-source Gamma estimate and current next calculation
Root directly completed the BRD final Gamma reflection/Legendre norm/F_B repair reading, all FTC495lines, and all CTR1–54; complete proofs accepted with independent pinned reviews. The actual two high relation determinants now have universal original-Gamma Hankel references with explicit one-sided O(k)=o(q) errors, O(1) for fixedm>=2. All inner/far tails are proved on original and reference source forms. Current whole NOTE/JSR receiving editions are being updated, newreader19 is finishing; sealed46 and frozen2343 remain immutable. Root wrote the next complete low scalar endpoint proof LET1–21, independent review pending, while a disjoint lane derives exact parity and positive Toda/Christoffel recurrence. These next sources stay outside currentreader19. The useful next task is actual growing-degree evaluation of full W_k and its arithmetic receiver, not repeating the finite q36 certificate or source truncation proof. Final46artifacts were sent to mathematical peer and sole publication owner. Existing hourly check retained; no duplicate automation created.
