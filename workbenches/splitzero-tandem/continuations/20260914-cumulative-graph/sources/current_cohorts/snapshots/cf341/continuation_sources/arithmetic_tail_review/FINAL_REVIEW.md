# Independent review of the actual arithmetic-tail continuation

Date: 2026-09-13. Final status: the complete BT1–23, TW1–21 including TW15a–b, CA1–29, and internal Binet derivation BI1–26 pass. The two requested CA typing clarifications and the single BI26 display typo have been applied and reread. No mathematical correction remains in the reviewed modules. The exact read editions and subsequent additions are identified below.

## Sources actually read in full

1. `arithmetic_tail/tilt_audit/ACTUAL_BOUNDARY_TILT.md`, all 293 lines, BT1–23. SHA-256 `ABD99ECB32D2EA5B7DCCE77AA138E10C44E514FE0CA9D46D2F94963CCBDE3475`.
2. `arithmetic_tail/arithmetic_tail_windows.tex`, all 338 lines, TW1–21. SHA-256 `DE4891590887787C0EE5CF3A5AD54478C51878E31B295A3DB0DFB0B729B4FDF2`.
3. `combined_arithmetic_restriction.tex`, all 310 lines after corrections, CA1–24. SHA-256 `C2874E2A6CB09C31EC9970A31EA6D6E016077469726E98360057E1C57323D11B`.

These paths are relative to `work/rh_counterfactual_20260913/continuation2/`. The inherited-source coverage is recorded separately in `WORK_LOG.md` and `prior_result_audit.md`; this receipt makes no claim that the reviewer reread every inherited repository file during this bounded review.

## Boundary calculation and constants: pass

BT3 retains the exact arithmetic identity, its 1/sqrt(pi) completion factor, and the denominator

\[
|h(1/2+it)|^2=[((t-\gamma)^2+\delta^2)((t+\gamma)^2+\delta^2)]^{2m}.
\]

The centered floor formulas BT4–5 are exact, including integer endpoints and N=1. The bound on the centered integral is N^(−1/2), and the sum bound in BT6 holds at N=1 as well as N≥2. Choosing N=floor(|t|) gives the stated Z_*=2+sqrt(5/2), without a zeta lower bound.

The explicit all-real Gamma constants are correct:

\[
c_\Gamma=\sqrt2e^{-7/6},\qquad C_\Gamma=\sqrt{2\sqrt5}e^{2/3}.
\]

The Binet kernel bound is 0≤kernel≤1/12, so |R(1/4+it/2)|≤1/3. Twice the real part gives precisely the exponent printed in BT9's proof. The two squared-difference identities at lines 137–145 give the required global algebraic prefactors, including t=0. There is no tacit compact-set Gamma minimum.

The compact denominator lower bound is delta^(8m). The tail identity BT13 gives the lower bound (3/4)^(4m)|t|^(8m), and the numerator estimate (t²+1/4)²≤(25/16)|t|⁴ holds on the stated tail. The resulting exponent p=8m−9/2 and beta=p−1/2=8m−5 are correct. All powers in C_comp and C_tail follow with their displayed signs. In particular p≥7/2>1.

The original boundary masses M_h(+pi/2)=M_h(−pi/2) are therefore positive and finite, with the stated bound 2C_h^tilt/(p−1). The absolute derivative orders at the boundary are exactly the integers 0≤j≤8m−6 supplied by j<p−1; no stronger endpoint regularity is asserted. The convolution argument uses parametrizations with determinant of absolute value one and retains M_alpha^(k−1), not a unit mass.

## Full Gram inequality and monic minima: pass

The independent derivation is written in `exact_comparison_review.md`. The proof in TW9–14 agrees with it. On each degree≤N space the Gamma raising and lowering shifts give ||uP||≤2(N+1)||P||; iteration through M multiplications gives D_N=[1+4(N+M)²]^M. Weighted Cauchy–Schwarz gives the lower inequality for every complex polynomial, so minimization on the same affine monic space is legitimate in both directions. The precise result is

\[
\frac{a_k\gamma_n}{D_n}\le\omega_{h,k,n}\le A_k\gamma_n,
\quad\gamma_n=\sqrt2\,n!\Gamma(n+1/2)=\sqrt{2\pi}(2n)!/4^n.
\]

The source coordinate map S=k/2+iu, its inverse, and the separate degree-n monic phase i^(−n) are retained correctly. The phase is not asserted to be one degree-independent algebra homomorphism. At n=0 the original squared norm is mu_h^k and the reference squared norm is sqrt(2pi); neither measure has been divided by its mass.

The logarithms of a_k,A_k have the stated O_h(k+log k) bounds, and log D_n=O_h(log(n+1)+1). Since k≥3, the claimed uniform O_h(k+log(n+1)) error follows even at n=0.

## Exact window constants and four-volume lower bound: pass

TW17 is a correct monotone-sum inequality with 0≤eta_q≤log 2. The adjacent window has the exact ratio multiplier (q−1/2)/(4q−1), between 1/6 and 1/4. Therefore the combined upper Gamma logarithm is at most 4q log(4q/e): the possible excess 2eta_q≤log 4 is canceled by the multiplier's logarithm, which is below −log 4. The combined lower error is at least −log 6. TW18 has both directions correct.

The finite logarithmic errors in TW16 are nonnegative because A_kD_N/a_k≥1 follows by applying the full Gram inequality to any nonzero polynomial. Since q=[1+k(m−1)](k+1)², the errors divided by q tend to zero. Thus both literal q-window limits are 4/e. The text correctly avoids claiming this limit for unspecified n/q or deducing consecutive recurrence asymptotics from the error term.

The coefficient sum of the retained weights is 2q. Inserting the exact norm-sum upper bound into the inherited CJ identity gives the printed delta e/8 constant and E_k, while retaining both original contraction penalties, both phase/control sums, the exact full-multiplicity trace, and the trace slack. TW20 and TW21 follow with their displayed signs. The coefficient four is correctly attributed to the inherited proof.

## Original quotient, adjoints, cochain, and combined bounds: pass after typing edits

CA6 has the correct adjoint order K=JH^(−1)J*, G=K^(−1), R=H^(−1)J*G. Its fibre decomposition and minimization prove CA7 for the identical full remainder map. The fixed sigma has mass sqrt(2pi); it is explicitly distinguished from AT's k-fold Gamma reference of mass (2pi)^(k/2).

Two small typing issues were sent to the parent and have been corrected and reread:

- CA6 now names only H,K,G as square positive invertible matrices and explicitly identifies R:E→P_N as a rectangular right inverse when N>q−1.
- CA8–10 now declare the original complex [V→Theta B] in degrees zero and one and the map V_(h,k):C[S]→B^(tensor k), P↦P(sum D_i)F_h^(tensor k). The observation and eta injection also have explicit domains and codomains.

The original relation difference is chi*kappa_x by monic division. In its explicit theta primitive the i−1 preceding degree-one factors give differential sign (−1)^(i−1), canceling the written sign. The polynomial identity sum h(s_i)Q_i=chi(sum s_i) and h(D)F_h=Theta phi_* prove CA10 exactly. The maps preserve the original supported label and produce the supported zero for the relation difference.

CA12 has the correct asymmetric endpoint constants. CA14 applies the already proved full-source AW spectrum 0^q,1²,2^(q−1) to the literal interpolation between the fixed sigma form and the arithmetic form. The count 1+2(q−1)=2q−1 gives the stated Lambda_k bound. The relative operator is self-adjoint in the fixed sigma metric; no Euclidean Hermiticity assumption is made.

The nonlinear functions in CA15 are inverse. Their derivative is Phi_q'(B)=1/[2q sqrt(1−exp(−B/(2q)))]; multiplying the inherited derivative bound in CA16's proof gives the integrated oscillation constant exactly. The nonlinear result is correctly attributed to EW, rather than claimed as a new all-q extension.

The Gamma polynomial phase and kernel sum in CA18–19 have the correct conjugates and monic factors. The resulting fixed-reference comparison is

\[
|B_{ar}-B_\sigma|=O_h(q(k+\log q))=o(q^2).
\]

CA21 takes extrema only among bounds on the identical scalar. CA23 asserts a vanishing difference divided by q² and explicitly does not assert existence of either separate limit. CA24 follows from the exact lower bound and E_k/q→0. These are valid restrictions on an actual hypothetical packet; the text neither constructs an off-critical zero nor asserts a contradiction.

## Prior-result comparison

The bounded source audit in `prior_result_audit.md` finds no duplicate sharp result in the reviewed inherited chapters. CJ gives log omega=2n log n+O_h(n), and TG gives the exact Gamma reference and actual determinant identities. The present arithmetic proof reduces the error to O_h(k+log(n+1)), which is o(n) in the original windows and determines 4/e. The prior small-value obstruction concerns the unsmoothed one-factor arithmetic multiplier and is not an obstruction to this proved convolution comparison.

## Addendum: original raw moments TW15a–b — pass

The added raw-moment passage, current TW lines 244–271, was read and independently checked. The current TW SHA-256 is `E2ABF620498569E6FE6BD767D7BA68576960AEF20EE30A6BF282AA16EE27640C`.

For u≥1, 1+u≤2u², hence (1+u)^(−1/2)≥1/(sqrt(2)u). The two equal tails give the stated lower reference moment sqrt(2)c_Gamma alpha^(−2n) Gamma(2n,alpha), and the repeated integration-by-parts identity yields its lower bound with exp(−alpha)(2n−1)!. Dropping the factor (1+|u|)^(−1/2)≤1 gives the printed upper bound. Applying the full degree-n form comparison to u^n proves TW15a, and the sole additional factorial loss is 2n. Thus TW15b has the stated uniform O_h(k+log(n+1)) error for n≥1. The mass at n=0 remains separate and unchanged.

## Addendum: old Gamma reference spectral spread CA25–29 — pass

The entire added section, current CA lines 312–415, was read and checked. The current CA SHA-256 is `5319D3F502CFC89F52002382720B88DFB0AA3D8502BECB939343C264611069C3`.

The inherited k-fold Gamma measure and norms in CA25 retain mass (2pi)^(k/2). For its relative form operator, the constant polynomial gives b_+≥mu_h^k/(2pi)^(k/2). Applying the lower relative form bound to the identical degree-2q monic affine space gives b_-≤omega_(h,k,2q)/gamma_(k,2q)^Gamma. TW14 bounds the numerator by A_k gamma_(2q). Substitution gives exactly

\[
\kappa_{old}\ge\max\left\{1,\frac{\mu_h^k}{\sqrt2 A_k\Gamma(k/2)}\frac{\Gamma(2q+k/2)}{\Gamma(2q+1/2)}\right\}.
\]

In CA27 the odd-k product has the claimed bounds. For even k, Gamma-integral Cauchy–Schwarz gives sqrt(n)≤Gamma(n+1)/Gamma(n+1/2)≤sqrt(n+1/2); multiplying the remaining positive factors proves both bounds. The logarithmic upper error is at most k²/(4n), as written. The elementary factorial treatment of Gamma(k/2) proves its asserted error term without a complex Gamma asymptotic.

Consequently the original mass term k log mu_h and the A_k logarithm contribute only O_h(k+log k). For m=1, log(2q)=2log k+O(1); for fixed m≥2 it is 3log k+O_h(1). Division by k log k gives the respective lower limits 1/2 and 1. The fixed-reference log-condition-number upper bound is O_h(k+log k). This contrast is a proved spectral constraint on the actual source; CA29 makes no unsupported conclusion about the orientation or sign of the four-volume correction.

## Addendum: self-contained Binet derivation BI1–26 — pass after corrected display

Fully read `arithmetic_tail/tilt_audit/EXACT_BINET_IDENTITY.md`, all 308 lines, and reread the corrected BI26 display. Final SHA-256 `7C7A4753D400D2979F2CAE9DFA6AE6582AB27ACAAF38AB3284AA94F85FBC71B4`.

The finite Beta integration-by-parts identity and substitution t=x/N prove the Euler integral limit, uniformly on compact subsets of the right half-plane and for the two required derivatives. The locally uniform logarithmic product constructs a genuine holomorphic logarithm and proves Gamma nonvanishing; no nonvanishing premise is assumed. The Gamma/Beta change of variables has absolute Jacobian r, and the two substitutions in B(z,z) give exactly the duplication factor 2^(1−2z). The Gaussian calculation fixes Gamma(1/2)=sqrt(pi).

The explicitly bounded kernel gives an absolutely convergent holomorphic R with |R(z)|≤1/(12 Re z). Direct differentiation of the proposed expression yields the same second-derivative series as the constructed Gamma logarithm. Their difference is affine; the exact recurrence and elementary log(1+y) bounds show its linear coefficient is zero. The exact duplication formula, with all constants retained, then shows its additive coefficient is zero. This proves the Binet identity internally and supplies the earlier Gamma bounds without assuming a Gamma asymptotic or a cited Binet formula.

The first written BI26 display omitted the plus sign before the remainder integral despite the preceding proof using the correct sum. The author inserted the plus sign at line 299, and the reviewer independently reread the correction. There are no remaining issues in this bounded proof audit.

## Addendum: crossed-pair angle refinement CA17a–b and CA21 — mathematical pass

Fully read accompanying `output/Tau_All_Degree_Angle_Transport_2026-09-13/proofs/AGT.tex`, all 365 lines, AGT1–19; SHA-256 `F29095D575553D7EB4D38B757F3788D5D15927247269A5D364687C5089A08E4D`. Read the new CA paragraph and formulas at lines 217–247 and revised CA21 at lines 289–302. The 447-line CA draft at this read has SHA-256 `99E8A5047F7AFE0DF98523314B9668A1FC9DA8A11AC630C84A5038F028DBA971`.

The section difference R_i−R_j has the same zero remainder, lies in the full relation space, and is orthogonal to R_jE. Therefore R_j=Z_jR_i and G_i−G_j=D_ij* M D_ij. With U_i=R_iG_i^(−1/2), the cross matrix U_j* M U_i is G_j^(1/2)G_i^(−1/2); its squared singular values are exactly the eigenvalues of G_i^(−1/2)G_jG_i^(−1/2). This proves the principal-angle/determinant identity with the stated adjoint order and no commuting-Gram assumption. The displayed two-dimensional projection-difference matrices have eigenvalues ±sin(theta), including all zero-angle cases.

The four-volume factors can be paired exactly as (q−1,2q) and (q,2q−1). For the second pair, both q-dimensional section spaces are contained in P_(2q−1) and orthogonal to chi. Positivity of the moment form on nonzero chi makes this ambient subspace have dimension 2q−1. Its two section spaces intersect in dimension at least one, so one principal angle is zero. This includes q=1, when the two cutoffs of that pair coincide. The first pair contributes at most q nonzero angles and the second at most q−1; hence the total is at most d=2q−1.

Their logarithmic costs still sum to precisely B(t), with all original endpoints and their signs retained. Concavity of sqrt(1−exp(−x)) then gives

\[
|B'(t)|\le d\,o(t)\sqrt{1-e^{-B(t)/d}},\qquad d=2q-1.
\]

The positive moment witness remains valid for the new fixed-sigma interpolation: if B=0, the first pair's section images would coincide, forcing 1 to be orthogonal to chi P_q, whereas chi*chi^(#k) lies there and has inner product integral |chi(k/2+iu)|²m_t(u)du>0. Thus B is positive throughout the compact interpolation, and its transformed derivative is legitimate without assumptions on angle-branch differentiability.

The reciprocal derivative is

\[
\frac1{\widehat\Phi_q'(B)}
=(2q-1)\sqrt{1-e^{-B/(2q-1)}},
\quad \widehat\Phi_q(B)=2\operatorname{arcosh}(e^{B/(4q-2)}).
\]

Its inverse is precisely widehatPsi_q(t)=(4q−2)log cosh(t/2). The original spectral oscillation integrates to log(b_max/b_min), at most Lambda_k. This proves CA17b, and the substitutions into both extrema in CA21 are correct. All endpoint masses, source flags, full remainder maps, and the previous constraints remain intact. The companion is explicitly attributed; no claim that the general angle method is new is introduced.

One wording clarification was sent to the parent: in the sentence after CA17a, the factor multiplying o(t), rather than the whole product containing o(t), is the reciprocal derivative of widehatPhi_q. The parent applied this clarification at CA lines 236–237; the reviewer independently reread it. The displayed formulas required no change. Final reviewed CA SHA-256 is `EE8FB79B97F2BFD367D9758661BA067DE98C4AE2A8AA97FB147B5DC34557DA35` (447 lines). This last bounded addition is approved with no remaining corrections.
