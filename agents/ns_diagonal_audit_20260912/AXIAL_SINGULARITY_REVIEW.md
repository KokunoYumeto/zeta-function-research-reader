# Independent review of the sharp axial singularity calculation

2026-09-12. Result: **PASS at the stated local analytic-germ scope**. Source existence and the cutoff-to-axis identification remain imported. No canonical source, publication, or source-owner receipt was changed.

Personally read in full:

- `agents/ns_axial_singularity_20260912/AXIAL_SINGULARITIES.md`, 13,762 bytes, SHA-256 `973920ada7cdf9dba0f97a7e6e47fe425a172b477ef02854ed601568190e2d5a`.
- Its complete `check_axial_singularities.py`, 8,528 bytes, SHA-256 `6641e6c32967364e254b54607f1680643b8ce03ccdd4ed6586720f3b9c17c946`.

The source axial germ and Lagrange derivation had also been read in the parent's new `29r_ns_all_axis_mellin.tex`; the present report's companion `REPORT.md` binds that exact review. This is a content-level mathematical review, not a reliance on routing summaries or green checks.

## Gamma identities and exceptional indices

Write p=1-2h, q=2h only for this review, so D=p/2 and A=1-D. The finite-binomial denominator arguments are exactly 2-qj-D for the even coefficients and 2-qj for the odd coefficients. Their numerators are strictly positive gamma arguments. Therefore the reciprocal-gamma formulas really include every finite-index zero:

    even zero iff qj+D is an integer >=2;
    odd zero iff qj is an integer >=2.

In the reflected products the second gamma arguments are qj-A and qj-1. Restricting to j>A/q and j>1/q respectively makes them positive. The excluded threshold u=1 is correctly handled by reciprocal gamma, not by setting a sine factor equal to zero before its pole cancels. Genuine integers u>=2 do give exact zero after reflection because the remaining gamma envelope is finite. These distinctions are mathematically necessary and present in the proof.

The reflected even phase is

    sin(pi(qj+D))=cos((2j-1)pi h),

and the odd phase is sin(pi qj). The common reflection minus sign produces the displayed factor (-1)^(j+1). No phase sign error was found.

## Envelope and exact radius for every real source parameter

For Gamma(pj+b)Gamma(qj+c)/Gamma(j+1), Stirling yields exponential factor (p^p q^q)^j, power j^(b+c-3/2), and positive constant sqrt(2pi)p^(b-1/2)q^(c-1/2). The pairs (A,-A) and (1,-1) give precisely both reported j^(-3/2) envelopes and constants. Expanding B_2(b)/(2p)+B_2(c)/(2q)-1/12 verifies the two first-correction numerators as well.

The proof does not divide by a trigonometric factor that may vanish. Its lower-limsup step works separately for each parity: both phase sequences are shifted sines with increment delta=pi q, and

    |sin(delta)| <= |sin(theta)|+|sin(theta+delta)|.

Since 0<q<1/50, sin(delta)>0. In every pair of adjacent indices, each individual sequence has a term of magnitude at least sin(delta)/2. Thus each parity has infinitely many such terms even for irrational h with exceptionally small other terms or rational h with an infinite exact-zero subsequence. Combining this with the positive Stirling envelope proves both parity limsups equal sqrt(p^p q^q). Cauchy--Hadamard gives the exact radius

    R=(p^p q^q)^(-1/2).

No uniform-in-h lower bound or h=0 endpoint result has been smuggled into that argument.

## Access on the original inverse sheet

The Lagrange coefficient formula for eta has gamma numerator shifts D+1 and -D; after the extra divisor 2j+1 its envelope again has the required O_h(B^j j^(-3/2)) upper bound. This proves that its actual inverse Taylor series is holomorphic on |x|<R, not merely that a formal inverse exists.

The proposed path starts at eta=0, travels to i/sqrt(q), then along the upper circle |eta|=1/sqrt(q) toward either real critical point. It avoids eta=+1 and -1. Along the imaginary segment the modulus v/(1+v^2)^D increases strictly and remains below R. On the circular open arcs the identity

    |1-r^2 exp(2i theta)|^2=(r^2-1)^2+4r^2 sin^2(theta)

proves the image is strictly inside |x|<R. Before the endpoint, f' has no zero on the path. Successive local inverses therefore agree with the disk's eta(x), starting from their common germ at zero. This is enough to identify the endpoint on the original branch: uniqueness can be propagated along every compact initial part of the path, and eta(x(t)) is the prescribed eta(t). The argument does not presume a global injectivity theorem for the multivalued forward map.

The conjugate lower paths give the other two logarithm limits. On the upper approach to +r, Im(1-eta^2)<0 and sigma=-1; on the upper approach to -r it is positive and sigma=+1. Hence the four endpoint values epsilon R exp(-i sigma pi D) and their phases are correct. All four are distinct for 0<D<1/2. This is real original-sheet accessibility evidence, not a list of critical values on unspecified sheets.

## Puiseux sign and absence of cancellation

Direct differentiation gives

    f''(eta_c)/x_c=2q^2/p,
    1-x/x_c=-(q^2/p)(eta-eta_c)^2+O((eta-eta_c)^3).

The nonvanishing factorization and local holomorphic square root prove an actually convergent Puiseux inverse. Along the specified circle approach, eta-eta_c has imaginary sign -epsilon sigma and 1-x/x_c is positive to leading order. Consequently

    kappa_(epsilon,sigma)=-i epsilon sigma sqrt(p)/q

is the correct leading coefficient for the positive-asymptotic square-root branch. Squaring it gives -p/q^2 as required.

The source profile derivative is

    F'(eta_c)=-(2/q)d_c^(-D)(4+epsilon A j_0 sqrt(q)).

The parenthetical factor cannot vanish over the original parameter interval: A<0.51, j_0<=0.05, sqrt(q)<1, so its deviation from 4 is less than 0.0255. The leading square-root term in W is therefore genuinely nonzero. This proves four true boundary singularities of the actual axial analytic germ, with the previously computed radius. It does not require a coefficient-transfer theorem.

Restoring z=sqrt(nu)tau^D x and w_0=sqrt(nu)tau^(-A)W retains the exact physical radius sqrt(nu)tau^D R and all derivative factors. The result has no premise asserting that the complete smooth radial cutoff field is globally holomorphic.

## Fresh regression reruns

After reading the entire checker, this reviewer executed it in normal and optimized mode. The only in-memory change removed its single receipt-write line; `__file__` retained the original checker path so its source identity check was unchanged. No function, condition, symbolic expression, numerical tolerance, or tested parameter was altered. This avoided overwriting the source owner's frozen receipts while rerunning every test.

Both outputs were:

    AXIAL_SINGULARITIES_CHECK_OK checks=552 optimized=False
    AXIAL_SINGULARITIES_CHECK_OK checks=552 optimized=True

The checker uses explicit raises rather than assertions, so optimization retained all 552 checks. These are supplementary finite and high-precision regressions, not a substitute for the all-real-h proofs reviewed above. No Lean/formal certificate is claimed. In canonical TeX use p_* and q_* for these exact abbreviations to avoid colliding with the source concentration coordinate q.

## Canonical 29s integration and the zeroth-residue transport

The entire initial integration `tex/satellites/29s_ns_axial_branch_radius.tex` was read at 13,886 bytes, SHA-256 `93217d35bfd17d42f7168cd7b096ee9c52162ef8e49de8034a2d0ca8f0586d71`. All coefficient formulas, exceptional-index distinctions, the j=100 resonance example, first-correction constants, original-sheet path and Puiseux signs survived the TeX integration correctly. The source concentration coordinate remains q and the independent abbreviations are now p_*,q_*.

The new final subsection is also mathematically valid on the source's central cutoff-one axis patch. Indeed the extended arithmetic transform gives

    J_0(z,t)=Res_{s=0} M A_h Z_actual(s,z,t)
            =c_{h,0} Z_actual(0,z,t)=c_{h,0} w_0(z,t),
    c_{h,0}=(2^h-1)/4>0.

The inverse is multiplication by c_{h,0}^(-1). Equality on that real open patch makes J_0 real analytic there and identifies its unique holomorphic z germ with c_{h,0} times the previously proved axial germ. No analytic continuation of the full cutoff-dependent radial Mellin integral into complex physical z is assumed. The arithmetic residue germ is what is continued.

The exact scaling z=sqrt(nu)tau^D x gives z_c=sqrt(nu)tau^D x_c and 1-x/x_c=1-z/z_c. Therefore the nonzero Puiseux amplitude is

    c_{h,0} sqrt(nu) tau^(-A) F'(eta_c) kappa_(epsilon,varsigma).

Every factor is nonzero at the fixed source parameters and preterminal time. Multiplication by this nonzero scalar does not alter the Taylor radius or turn any of the four fractional-power terms into a holomorphic one. The derivative root limsup is exactly 1/(sqrt(nu)tau^D R): the fixed nonzero scalar multiplier has n-th root tending to one. This proves the new arithmetic statement by an explicit invertible map, not by analogy. Its singularities are in physical z while the Mellin coordinate remains the fixed endpoint s=0.

Four further exact symbolic regressions passed: both integrated gamma first-correction constants reduce from the Bernoulli-polynomial formula; the physical Puiseux argument transforms exactly as displayed; and the scalar zeroth-residue inverse recovers the unchanged physical axial value. These supplement, not replace, the preceding analytic proof.

A scope precision was sent to the parent: the initial theorem stated actual-source conclusions after merely listing tau>0, whereas the final proof correctly restricted the actual-field identification to the central real-axis patch. The actual source may have different final time/spatial cutoff traces elsewhere. The radius theorem for the explicit analytic formula W holds for every tau>0 after scaling; the assertion about the actual compact axial average must retain the already imported central cutoff-one neighborhood. This is a clarification of the existing source domain, not a new parameter choice or an added source existence claim.

### Final canonical approval

The parent inserted that explicit original-domain clarification before the theorem. The final chapter has 14,377 bytes and SHA-256 `b1c815130ba333b872ddcf8a6b46ad83fac00589b915fc1a5670339826e11f87`. This reviewer read the inserted block and verified that removing only that exact block reconstructs the prior fully reviewed chapter SHA-256 `93217d35bfd17d42f7168cd7b096ee9c52162ef8e49de8034a2d0ca8f0586d71`. Thus there was no unreviewed mathematical delta elsewhere. **Final canonical 29s: PASS, no outstanding mathematical or source-domain correction identified in this review.**
