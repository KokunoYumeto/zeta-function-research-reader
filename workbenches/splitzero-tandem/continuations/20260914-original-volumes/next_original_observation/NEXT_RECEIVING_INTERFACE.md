# Exact next interface to the frozen MRI and BRI receivers

This separate accepted next-source package leaves the main Cut 22 PDF and its current receivers unchanged. `sources/OPG.tex` contains the original observation calculation OPG1–26. `sources/OPR.tex` proves the exact next receiver interface OPR1–5. The predecessor MRI1–5 and BRI1–9 bodies are preserved byte-for-byte in `provenance/frozen_receivers` and pinned in the dependency map.

The next cumulative receiver successor can incorporate the following substitutions, with the original source order always 1 or k:

1. **MRI1, the actual observation columns.** Insert OPG15–17: `w_j=lambda_(q+j)` and `M_j^obs=sum_(d<q+j)lambda_d lambda_d*`. The columns are exactly those calculated by OPG9 and the complete finite primary formula OPG14. Both sums and the inverse act on the existing actual image of Lambda.
2. **MRI2, the retained kernel vector.** Use OPR1–3 to connect its metric residual with the fixed-section kernel in OPG21. At `D=q+j`, the exact map is `C_s r_j^ker = I(zeta_D - kappa S_(D-1)^s lambda_D)`. Its squared norm in the old quotient kernel Gram is exactly `t_j-xi_j`. The minimum section is at degree `D-1`; the section correction remains.
3. **MRI3, the two ordered factors.** Preserve the existing contractions and use OPR4. The boundary factor is `1+xi_j`; the kernel factor is `1+(t_j-xi_j)/(1+xi_j)`. The denominator and original elimination order remain.
4. **MRI4, the four original endpoints.** OPG18 gives the exact boundary determinant ratio with numerator `det M_(2q) det M_(2q+1)` and denominator `det M_q det M_(q+1)`. Its weights are still `1,2,...,2,1`. The complete kernel/boundary sum remains the original source volume.
5. **MRI5 and BRI2.** OPR5 retains the original source transition verbatim as a mathematical identity. The tensor-source sum receives `H_k+delta_k^sigma`; the fixed-source sum receives `delta_k^sigma`. The new observation formula assigns no new sign or size to either transition.
6. **BRI6 and BRI9.** Their established combined coefficient remains attached to the full kernel/boundary sum. The new OPG/OPR calculation specifies the two individual inputs without assigning either one that combined coefficient. The next quantitative work acts on the actual unit jets, period vectors, cyclic average and the section-corrected kernel norm.

OPG19–26 also supplies the complete coupled action. Its defect `Lambda Y I` and the ambient term `P_k T (I-P_k) V I` remain. The observed-iterate quotient in OPG23–24 supplies a proved invariant action with the original polynomial coefficients; it does not alter the original kernel or replace the recurrence used in these MRI substitutions.

The full original provider editions and exact required proof spans are included. IPM uses dotted tags `IPM.1` through `IPM.7`; this is why a search only for `IPM1` missed its actual proof. The included PGCC1–6 proves the Gamma grid constant in the period determinant, and OGN1–3 proves the full source norms from the canonical IGO transform. No auxiliary source-order selection enters this package.
