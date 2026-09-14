# Independent review of the parity and Toda transport

Accepted: every definition, displayed identity, and proof in PHT1–19 was read and checked. This is a mathematical source review; no TeX edit, build, PDF inspection, Lean run, or publication was performed.

Reviewed source cut: `PARITY_AND_TODA_TRANSPORT.tex`, PHT1–19, all 303 lines after the author's bounded repairs. This acceptance does not cover a future PHT20+ addition.

Final PHT1–19 cut SHA256: `c92f3f6fcd2498fb26b0e1eedab258117496dc5dbd410a90dd8ca8269bd148ff`.

The earlier whole-source review read all 290 lines at SHA256 `6741ec31e0ff01f3a9347c90f22e535d30523999f13b6d5ed503ad1d901b6ea7`. The final bounded reread checked the corrected PHT3 integration spacing, the added direct Euler/keyhole reflection proof after PHT13, and the finite positive-Gram inverse justification before PHT14. In the reflection proof, the substitution `x=t v` leaves the integral `t^(z-1)/(1+t)`; the printed contour factor and residue give exactly `pi/sin(pi z)`. All three changes are accepted.

Dependency read: `independent_contiguous.tex`, all 414 lines, SHA256 `e01021c3b9b659cd897cc95179391b3bde0de63397405426fef2cda420e81196`. The review specifically checked its Gamma anchors and the exact PHT/HCT interface below. The separately assigned HCT reviewer owns its whole-source receipt.

Additional receiver context read: `../next_bulk_density/ORIGINAL_RELATION_BULK_CONTROL.tex`, lines 589–623 including BRD42, SHA256 `4d6e3df419edcedbe7e66e6f802bdeca6e088d9036c5b4c17692517995ebcba9`. The rest of that accepted proof was not reread. LET and any later arithmetic receiver source were not read or reviewed in this assignment.

## Exact checks

1. **Original measure, mass, and both branches (PHT1–5).** Euler contour rotation has power contribution `exp(-theta |y|/2)` and absolute remaining integral `Gamma(1/4)(cos theta)^(-1/4)`. Squaring and dividing by `2 pi` gives the printed bound. Each branch of `t=y^2` contributes `sigma(sqrt(t))/(2 sqrt(t)) dt`. Their sum has the stated mass and moments. The original Gamma mass is independently anchored by HCT3: substituting `y=2 xi` into the autocorrelation formula gives `sqrt(2 pi) (cosh w)^(-1/2)`, including the factor from `dy=2 dxi`. The two-sheet inverse in PHT4 is exact and its norm identity cancels the two opposite cross terms.

2. **Hilbert-space typing and coordinate coupling (PHT5–6).** The source is `L^2(R,y^(2a)d sigma)` and the target is `L^2(t^a d nu) direct-sum L^2(t^(a+1)d nu)`. The displayed inverse is defined almost everywhere, and the norm identity proves surjectivity as well as isometry. In the target, the domain of the coordinate matrix consists of pairs `(f_e,f_o)` in that direct sum for which
   `integral t^(a+1)|f_e|^2 d nu + integral t^(a+2)|f_o|^2 d nu < infinity`.
   Its output is `(t f_o,f_e)`, so this condition is exactly the transported multiplication domain. The squared-coordinate domain is given by
   `integral t^(a+2)|f_e|^2 d nu + integral t^(a+3)|f_o|^2 d nu < infinity`.
   The inequality `t <= 1+t^2` also gives the intermediate first-coordinate domain. Thus the printed matrix square has its original operator domain and retains the parity coupling of multiplication by `y`.

3. **Full finite parity and the original S frame (PHT7–9).** The even-index column `e_(2j)` crosses exactly `j` smaller odd indices, hence the permutation sign is `(-1)^(n_e(n_e-1)/2)` for both parities of `r`. Congruence makes its two signs cancel. The block moments have shifts `a` and `a+1`, respectively, yielding exactly PHT8; their positive densities make every block positive definite. The coefficient map for substitution `S=c+i y` has diagonal `i^n`, determinant `i^(r(r-1)/2)`, and inverse substitution `(S-c)/i`. Therefore `E* M E` has precisely the stated determinant. Multiplication by `(S-c)^a` contributes `i^a`, with squared modulus one.

4. **Unchanged high ranks and mass (PHT10–12).** For `q=2n`, the product at the two original ranks is exactly
   `Z_a=H_n^(a) H_(n+1)^(a) (H_n^(a+1))^2`.
   The shift ratio in PHT11 and finite logarithmic sum in PHT12 follow by dividing these four factors in place. Their total dimension is `4n+1=2q+1`, so the original mass power is `c_sigma^(2q+1)` before the displayed numerator/denominator cancellation. No rank, degree, or relation multiplicity is changed.

5. **Gamma anchors and positive recurrence interface.** Directly expanding HCT4 and integrating its two generating functions with HCT3 gives the diagonal norms `gamma_0 j! (1/2)_j`. This yields the exact even and odd Hankel anchors HCT19–20 and the starting coefficients `c_n^(0)=(2n+1)(2n+1/2)`, `d_n^(0)=2n(2n-1/2)`. PHT's `A_n^(a)` is HCT's `R_n^(a)=product_(j<n)c_j^(a)`; PHT's permutation matrix is the transpose of HCT's row permutation. The positive qd formulas use `c_(n-1)^(a+1)=e_(n-1)+d_n^(a)` in the denominator, so HCT16 gives the printed `d_n` update, and the sum identity gives the `c_n` update. Every finite endpoint row is retained. Consequently HCT37 computes precisely PHT12's paired shift ratio.

6. **Actual quadratic time domain and derivatives (PHT13–16).** For real `u>=0`, all derivatives of a moment are integrals against higher powers of `t`; at zero their right derivatives follow from the original finite moments. On compact subsets of `Re u>0`, exponential domination gives holomorphic moments. The positive real Gram matrix allows differentiation of the monic polynomial coefficients through its inverse. Reflection gives `sigma(y)>=pi/[Gamma(3/4)^2 cosh(pi y)]>=C exp(-pi |y|)`, so every `u<0` has infinite mass. For the negative tilt, orthogonality gives `partial_u p_j=alpha_j p_(j-1)` and `partial_u h_j=-b_j h_j`. Expanding `t p_j` gives `||t p_j||^2/h_j=alpha_(j+1)+b_j^2+alpha_j`, hence `b_j'=alpha_j-alpha_(j+1)` with the printed sign. Telescoping `-(sum b_j)'` gives `alpha_n=H_(n+1)H_(n-1)/H_n^2`; the constant in PHT16 is exactly one. At `u=0` this is the proved one-sided identity.

7. **Original linear time and the final curvature receiver (PHT17–19).** Applying the two-sheet inverse to multiplication by `exp(theta y/2)` yields exactly the printed hyperbolic matrix. Its inverse is obtained by `theta -> -theta`; as an isometry it goes from the source with weight `exp(theta y)` to the original source. The quadratic multiplier is `exp(-u t/2)` in both components. The convergence strip `|theta|<pi/2` follows by choosing a strictly larger rotation angle below `pi/2`. With the positive linear tilt, the recurrence derivative changes sign, and the second derivative of the full determinant remains the positive norm ratio in PHT18. Parity gives the two formulas in PHT19. In HCT notation these are, respectively, `d_n^(a)` and `c_n^(a)`. The quadratic-flow recurrence coefficient is instead `d_n^(a)c_(n-1)^(a)`, exactly as HCT14 supplies. These identifications preserve both original time variables and their distinct functions of the coordinate operator.

## Receiver scope and disposition

PHT contains the exact paired determinant and curvature receivers above. It contains no new arithmetic bound or low-endpoint substitution. The unchanged surrounding BRD42 convention is `R_k^0-R_k^sigma=-mathfrak T_k`; nothing in PHT changes that sign or evaluates its remaining relation determinant deformation. This review therefore makes no assertion about a later `W_k`, low-endpoint error, or arithmetic correction formula.

No mathematical correction remains for this PHT1–19 cut. The PHT3 integration typography is corrected. The source now also contains its own direct reflection calculation and the explicit justification of polynomial coefficient derivatives. Any later PHT20+ addition should receive its own bounded review and source hash; this receipt does not pre-accept such additions.

## Final source supplement: PHT20–23 and completed operator domains

**Final full-source status: PHT1–23, including PHT17a, accepted. No unresolved mathematical, domain, constant, sign, or indexing findings.** This supplement extends the earlier acceptance by a bounded reading of the actual new spans. The preceding cut and its narrower historical scope are preserved above.

Final complete source: `PARITY_AND_TODA_TRANSPORT.tex`, 427 lines.

Final source SHA-256: `3b5914ff3d99e18f881fc59a372787dadfe1e1ef8aa9ebeefebb62d6a6a9991d`.

Included complete provider: `independent_contiguous.tex`, HCT1–39.

Included provider SHA-256: `e01021c3b9b659cd897cc95179391b3bde0de63397405426fef2cda420e81196`.

The final reviewer read the complete new domains after PHT6, the revised real-parameter premise and all of PHT17a, and all of PHT20–23. The earlier whole-source PHT1–19 review and complete independent HCT1–39 review remain applicable to their unchanged formulas. No source was edited in this final review, and no build or publication is asserted.

1. **Full multiplication domains.** In `K_a=L^2(t^a d nu) direct-sum L^2(t^(a+1)d nu)`, the image `(t v,u)` belongs to the base space exactly when the additional integrals with exponents `a+2` for `v` and `a+1` for `u` are finite. The squared image `(t u,t v)` requires exponents `a+2` for `u` and `a+3` for `v`. Together with base-space membership, `t <= 1+t^2` gives both intermediate first-operator requirements, so the stated square is the operator square on precisely its full domain. The original two-branch norm identity identifies these with the complete original multiplication domains of `y` and `y^2`.

2. **Full weighted cross Gram and inverse.** Put `x=theta sqrt(t)/2`, `C=cosh x`, `S=sinh x`. The actual matrix is `B=[[C,sqrt(t) S],[S/sqrt(t),C]]`. Direct multiplication gives `B* diag(1,t) B=[[C^2+S^2,2 sqrt(t) CS],[2 sqrt(t) CS,t(C^2+S^2)]]`, exactly the printed `G_theta`; replacing `theta` by `-theta` gives its inverse because `C^2-S^2=1`. The sum of the original two weighted branch integrals is the same quadratic form. Hence the full measurable-pair space with finite `G_theta` integral maps isometrically onto `K_a`, with the specified inverse. On the base space its domain is exactly the intersection stated in the source. These statements apply to every real `theta`; the separate `|theta|<pi/2` requirement concerns existence of all polynomial moments. No bounded endomorphism on the unweighted base space is presumed.

3. **Source product and its sign (PHT20–21).** The quotient of source products at `q-1` and `2q-1` leaves exactly the denominator indices `a=q,...,2q-1`. The quotient at `q` and `2q` leaves exactly `a=q+1,...,2q`. Therefore the printed `exp(P_k)=G_(q,l)^(-1)` has the correct two ranges and sign. The distinct symbol `mathscr D_(l,N)` preserves the original GCR/LET product without colliding with the moment determinant `D_(a,r)`.

4. **Low endpoint and all four high factors (PHT22–23).** With the actual all-index moments, `m_(2q+2l)/m_(2q)=mu_(q+l)/mu_q=H_1^(q+l)/H_1^q`. HCT13 at degree zero gives exactly `product_(s=0)^(l-1)c_0^(q+s)`. This factor occurs in the denominator of `exp(W_k)`. The high pair is precisely `Z_(q+l)/Z_q`, so HCT37 supplies the two degree ranges `j=0,...,n-1`, `j=0,...,n` at shift `q+s` and the squared range `j=0,...,n-1` at shift `q+s+1`. Division by the low factor and by `G_(q,l)` gives PHT23 with every original factor retained.

5. **Exact positive evaluation and finite scope.** The starting `c,d` coefficients are the rational Gamma values proved in HCT21, and every subsequent coefficient is obtained by HCT22–23 using positive sums, products and quotients. All factors of `G_(q,l)` are positive rationals. Therefore `mathcal W_(q,l)` is a positive rational and `W_k=log(mathcal W_(q,l))` is an exact finite identity. The largest required coefficient degree is `n` and the largest required shift is `q+l`; the HCT24 initial range through `n+q+l` is sufficient. The original Gamma mass remains in the individual source norms and cancels only in the stated equal-dimension ratios. No bit-complexity estimate or coupled large-rank asymptotic is claimed or supplied by this review.

This supplement verifies the PHT20-defined universal center and its exact conversion to the positive product. It does not perform a second audit of LET's analytic error bounds or assert any additional arithmetic enclosure. Those bounds retain their separate reviewed source and receipt.
