# Independent full Hurwitz/Laurent integration review — 12 September 2026

Reviewed all mathematical statements in `work/historical_hurwitz_lane_20260912.md`, SHA256 `DF6385B14A3684F562BDC2FC684C8C42765D7BB8068D1BD529938B62991E6A9B`. Re-read the cited original compact-Hurwitz source at lines 722–858 to verify the admissible input and completion conventions. The original historical lane owns the full TeX conversion at `tex/historical_hurwitz_jets.tex`; this reviewer created no duplicate TeX. No Lean process was run.

Two independent focused reviewers checked H1–H13 and J1–J20/S1–S3/C1–C4 respectively. The analytic reviewer additionally obtained an independent check of the multiple-zero construction H10–H13. The present reviewer also derived the same identities directly.

## Result and correction sent

The central result is correct: for every fixed actual nontrivial zero rho of arbitrary exact multiplicity r, the complete monic local zero-cluster germ of the original compact probability Hurwitz family determines every moment of the original measure, and hence the measure itself. No simplicity or RH assumption enters the full-cluster result. The division unit and multiplicity are proved, not assumed as a missing hypothesis. The Laurent jet, involution, collision, and coefficient formulas also check.

One typed wording correction is required at S2. Applying G to a product ring isomorphism produces a map between G(product R_rho), whereas the displayed S2 is a map between product G(R_rho). The displayed S2 itself is correct: its derivation must say to apply G to each individual Phi_(rho,m_rho), then take the product of those semiring isomorphisms. This correction was sent to the historical author and root.

For a nonempty finite index set the exact comparison of these two constructions is the injective semiring homomorphism

iota_R:G(product R_rho)→product G(R_rho),

iota_R(tau)=(tau)_rho,

iota_R((r_rho)^bullet)=(r_rho^bullet)_rho.

Its support image contains only the empty and full support vectors; the factorwise product in S2 retains every independent support vector. It intertwines G(product Phi_rho) with product G(Phi_rho). For an empty index set the displayed iota is not injective: G of the terminal zero ring has two elements, whereas the empty semiring product has one. Thus any added injectivity statement for iota must explicitly say nonempty; S2 itself is valid also as an empty product.

## Exact admissible Hurwitz input and analytic scope

The domain is compactly supported nonnegative Borel probability measures on [0,infinity), with total mass m_0=1. All arguments retain the original support coordinate y, a finite containing interval [0,L], and the marked displacement t. For |t|L<1, every parameter 1+ty stays in the right half-plane, so the Hurwitz branch continued from parameter 1 is unambiguous. The exceptional L=0 input is exactly delta_0 and is handled separately.

The expansion coefficient b_n(s)=(-1)^n(s)_n zeta(s+n)/n! is correct for zeta(s,1+ty). The polynomial bound for the Pochhammer coefficient, the moment bound m_n≤L^n, and the absolutely convergent zeta series for n≥1 give normal convergence on compact sets in the open critical strip. A surrounding compact annulus gives the derivative control needed for contour integrals. At any actual nontrivial zero rho, every b_n(rho), n≥1, is nonzero: all Pochhammer factors are nonzero and Re(rho+n)>1, where the absolutely convergent logarithmic Euler product proves nonvanishing.

The source's completed residue defect should receive its short proof in the standalone reader if it is stated there. With Lambda_(mu,t)=pi^(−s/2)Gamma(s/2)Z_(mu,t), its residue at one is one. The identity zeta(0,a)=1/2−a gives Z_(mu,t)(0)=−1/2−t m_1, and Gamma(s/2)=2/s+O(1) gives residue at zero −1−2t m_1. Their sum is exactly −2t m_1. This matches the original source, including its factor two.

## Simple branch and original-coordinate measure inverse

At a simple zero, the only occurrence of c_N in the coefficient-of-t^N equation is zeta'(rho)c_N; the only occurrence of m_N is m_N b_N(rho). These nonzero coefficients make H4 triangular in both directions. Substituting b_1=−s zeta(s+1) and b_2=s(s+1)zeta(s+2)/2 verifies H5–H6 including the second-order minus sign and factor two.

The Bernstein weights H7 equal the integral of the binomial probabilities binom(M,j)(y/L)^j(1−y/L)^(M−j). They are nonnegative and sum to one. Their nodes remain Lj/M on the original interval. The variance y(L−y)/M gives the uniform-continuity estimate and the Lipschitz error bound Lip(f)L/(2sqrt(M)). Thus the constructed discrete measures converge weakly to the original measure. Two compact inputs admit a common finite support bound, so the reconstruction proves uniqueness even when a bound is not specified in advance.

The endpoint formula lim m_n^(1/n)=sup supp(mu) uses exactly the positivity and nonnegative compact support in the stated domain. The upper bound is immediate. Every interval (a,L_mu] below the true endpoint has positive mass, giving m_n≥a^n mu((a,L_mu]); taking nth roots and a approaching the endpoint proves the lower bound. The zero-endpoint fibre is delta_0. No conclusion for arbitrary signed or noncompact input is silently inserted.

## Full zero-cluster inverse with exact multiplicity

The contour disc lies within the open strip, excludes the pole at one, and contains only the chosen order-r zeta zero at t=0. Uniform convergence and Rouché give exactly r zeros for small complex t, counted with multiplicity. The logarithmic-derivative contour integrals are their displacement power sums. Newton's identities construct a holomorphic monic polynomial P_mu(s,t) of degree r, independent of individual branch enumerations or fractional-power parametrizations.

The quotient unit U_mu is established jointly holomorphic by a fixed inner-contour Cauchy integral of Z/P. For each fixed t the two divisors agree with their exact multiplicities, so the quotient is removable at the roots and has no zeros. Hence Z=UP and U_0=zeta(s)/(s−rho)^r are genuine analytic identities.

Comparing coefficients of t^N gives

m_N b_N(s)=U_N(s)(s−rho)^r+sum_(k=1)^N U_(N−k)(s)P_k(s).

Evaluation at rho yields H12. Rearrangement yields H13; divisibility by (s−rho)^r follows from this established identity, and the central value is the rth derivative divided by r!. Starting from the fully known U_0, these operations recover every moment from the complete cluster germ. They assert an inverse on actual input germs; they do not claim arbitrary polynomial germs satisfy the divisibility or moment-positivity constraints.

Conversely, equal moments through N make the two families differ by t^(N+1) as jointly holomorphic functions near a common contour. An s derivative, division by the nonzero contour denominators, contour integration, and Newton's finite recursion all preserve that order. Thus cluster jets and moment jets through N determine one another. The H7 reconstruction then recovers the whole measure. At r=1 this reduces to H4; r>1 retains the complete cluster without a simplicity assumption.

## Laurent jets, involution coefficients, and local Jordan lengths

For a=log p>0 and z=omega p^(rho−1/2), the truncated exponential maps the Laurent generator to z exp(a(X−rho)) and is a unit. Its difference from z generates the same primary nilpotent ideal because its first coefficient is za≠0. Truncated logarithm gives the exact inverse J3. The kth conormal grade is multiplied by (za)^k, retaining all constants and factorials. The identity exp(aN)−I=N(aI+NB(N)) with invertible second factor proves equality of the kernels of every corresponding power, hence preservation of all local Jordan lengths.

Unit modulus of the mark omega is essential and is explicitly assumed. It gives z_dagger=1/conjugate(z). The spectral and Laurent involutions send X−rho to −(X−rho_dagger) and U−z to −conjugate(z)U⁻¹(U−z_dagger). The latter factor is a unit, which establishes the quotient types. Applying either operation twice returns the original labelled block. Evaluating U verifies the commuting diagram J9.

The full Laurent coefficient formula J11 is correct: expanding (−conjugate(z))^k U^(−k)(U−z_dagger)^k gives at degree ell the coefficient

(−1)^ell binom(ell−1,ell−k) conjugate(z)^(k+ell).

The first conormal coefficient is therefore −conjugate(z)^2. Multiplication by the target za and conjugate-linearity gives exactly −conjugate(z)a on both sides. Higher grades and their nonlinear mixing are retained separately.

The radial and tesserine factors in J13 are correct: log|z|=(Re rho−1/2)log p=(log p)c_(−+)/4. This is a specified real projection; it does not assert the functional equation for the displaced Hurwitz family.

## Single-prime collision image and exact cokernel

Two period values coincide exactly when the original spectral points differ by an integer multiple of 2 pi i/log p. At a common value z, simultaneous Laurent evaluation has kernel (U−z) raised to the maximum visible multiplicity M_z. Distinct values have coprime primary ideals. Consequently J15 is injective with image precisely the compatible truncated Laurent coefficient tuples J16, and its dimension is sum M_z.

Choosing one maximal block per collision class gives the explicitly linear difference map Delta_Z. Setting those maximal coefficients to zero and prescribing all others proves surjectivity. Its kernel is exactly the Laurent image. Thus J20 is an exact sequence of vector spaces, with the first arrow an algebra map and the second explicitly linear. No false algebra-cokernel identification is made.

The labelled product map J18 retains all blocks and is an isomorphism. Reflection permutes collision classes, preserves their maximum multiplicities, and intertwines the maps through the proved local involution. The split-support embedding is inverse image along the collision-class map q. It preserves intersections and unions; direct image q_* preserves unions and is a left inverse on saturated subsets, but the exhibited two-label counterexample correctly shows it does not generally preserve intersections.

The same-centre truncation maps commute with the exponential because the finite series reduce at the actual lower nilpotence order. A supported class whose amplitude truncates to zero lands at supported e and never at external tau.

## Period motion and scope

C1–C3 are the marked exponential/logarithm germ isomorphism for the simple branch H3. The ordered-composition coefficient formula C2 has the correct 1/k! and powers of log p. Its inverse uses the unique logarithm germ based at one. C4 explicitly projects to real coefficients for real t and retains the factor four in c_(−+). These assertions correctly keep the simple-branch scope; the separate full-cluster theorem supplies the arbitrary-multiplicity reconstruction.

No analytic RH estimate follows from these reconstruction or finite-algebra statements, and none is claimed. No claim of novelty has been used in this review. Apart from the factorwise-G wording correction and the requested standalone residue proof, the audited formulas require no repair.

## Final cumulative-integration repair and verification

At the root's explicit request, inspected the final staged TeX beginning at SHA256 `50D3A63242958AE0E20581C3525C5F1FACF06361E57D8ADA3A4911201611A3C8`. It still lacked the three requested additions. Applied the scoped repairs directly to `output/split_zero_rh_tandem_2026-09-12/tex/historical_hurwitz_jets.tex`:

1. S2 now takes the product of the individual G-lifts. Added S4–S5 proving the exact global/product comparison, its naturality, complete support image, and empty-index exception.
2. Added HRes1–HRes2 with a full derivation of the completed-function residue defect −2t m_1. The proof derives both Hurwitz special values from the Mellin integral with the original parameter, including the subtraction constants and holomorphic remainder. It then integrates against the original probability measure and retains both completion factors.
3. Added P1–P7: the two-prime Laurent evaluation map, all exact local kernels, pairwise comaximality, global intersection/product kernel, full CRT isomorphism, and the explicit inverse image of the original coordinate X. The map is named script P_(p,q), preserving the existing theta-map symbol. All multiplicities, phases, logarithmic factors, and nilpotent coefficients remain explicit.
4. Replaced reader-visible personal absolute paths by actual staged relative proof paths and original source hashes. Replaced machine-lane introduction/handoff prose with statements about the mathematical objects and scope. The existing mathematical proofs were retained.

The two focused reviewers independently rechecked the final HRes1–HRes2 and P1–P7/S2/S4/S5 transcriptions and found no defect. The complete section compiled twice under the cumulative XeLaTeX preamble in an isolated work directory, producing 14 pages of XDV with no warnings, undefined references, overfull or underfull boxes on the final pass. This was a source compilation check; cumulative PDF generation and visual QA remain with the root. The initial wrapper invocation had a working-directory mistake, which was corrected; its two stray generated files were removed after verifying the exact workspace path and contents. No cumulative main or build file was modified.

Final TeX SHA256: `4BCC72299DAAAC98EC41C40B38E31A763FEDAB86AA4C457E8E847E5ECB43BD7C`, 41,594 bytes.

The adjacent public source `sources/historical/hurwitz_laurent/PROVENANCE.json` now uses source names and staged relative paths, records the final TeX hash, and retains all original/excerpt hashes and line locators. Its four staged excerpt hashes were independently verified unchanged. Its original metadata bytes are preserved privately at `work/historical_hurwitz_provenance_before_public_repair_20260912.json`, SHA256 `F6517E0227809B5656FC4CE405A8CD87CC8093C82423962C6775FFBF6850E5CB`. Public provenance SHA256: `8606E7245C0670C3FE2D1BA20B8CC093D74A1A4DFCC4B5E8B80DD7B4EE3C153B`.

The old staging script still describes the original report conversion; rerunning it unchanged would replace these reviewed additions. The reviewed TeX bytes and updated provenance above are the ready cumulative-integration source for the next edition. The historical owner has acknowledged the file ownership and will not regenerate it concurrently.
