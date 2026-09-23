# Independent mathematical check of labelled heat and original theta

Date: 2026-09-23. Read the complete local source LABELLED_HEAT_AND_ORIGINAL_THETA.tex, LH1–15 and concluding LH7 paragraph.

The mathematical formulas checked:

1. LH1 uses the actual \(G_L(\mathbb Z)\). Its zero fiber is \((e)\), and primality follows from the domain property of integer amplitudes. The claim about multiplicative observations distinguishes a support character from an additive ring-valued map correctly.
2. LH2–3 embed the set of original points injectively in a free vector space. Independent lattice coordinates and independent Dirac masses prove this; the two bilinear operations reproduce the original operations on embedded points. Ordinary vector addition is not asserted to reproduce semiring addition.
3. For LH4–6, differentiating the full kernel gives \(\partial_Tk_T=\partial_x^2k_T\), and the Fourier convention gives exactly \(e^{-4\pi^2T\xi^2}\). The injectivity proof is valid: divide a compactly supported smooth test function by this nonvanishing multiplier, then use distribution uniqueness. The inverse is defined on the actual range and is not asserted bounded, continuous, or defined on every tempered distribution.
4. LH7 transports the source operations to the actual heat-image space with the correct domain and codomain. Its explicit sum receiver gives \(k_T(x-a-b)\) and join; its product receiver gives \(k_T(x-ab)\) and meet.
5. LH8–11 retain the top zero term and each lower label. The factor \(x=(4\pi T)^{-1}\) gives the full comparison \(\sum_nk_T(b-n)=\sqrt{x}K(x;b)\). The marked Gaussian is retained with the same prefactor. The change \(n\mapsto-n\) verifies the displacement sign.
6. LH12 is absolutely convergent for \(0<b<1,\ \Re s>1\), with exact marked term \(b^{-s}\), both shifted series, \(\pi^{-s/2}\), and \(\Gamma(s/2)\).
7. LH13 has the exact factor two and the separate marked constant at \(b=0\). The marked constant has no common Mellin convergence half-plane over \((0,\infty)\).
8. LH14 has the correct Fourier coefficient and phase sign. Its \(b=0\) identity gives \(\psi(x)=x^{-1/2}\psi(1/x)+(x^{-1/2}-1)/2\). Splitting the Mellin integral at one yields \(1/(s-1)-1/s\), and substitution on the small-\(x\) integral gives exponent \(-(s+1)/2\). Thus every factor and sign in LH15 checks. The remaining integral is entire by Gaussian domination on compact \(s\)-sets.

No analytic formula defect was found. Three wording repairs were reported to the root task:

* Apply the inverse componentwise to the retained pair \((D-\delta_0,\delta_0)\). An inverse applied only to the summed comb recovers that comb; the retained marking is additional source data.
* Replace the phrase claiming a faithful scalar representation by an exact scalar Mellin representation with the faithful labelled source retained. Scalar \(K(x;b)\) is periodic and even in displacement and does not retain lower support labels.
* In LH7, the finite kernel statement should specify the domain \(\operatorname{span}\{Dv_{1_L},\delta_0v_\lambda:\lambda\in J\}\). On this vector space the kernel of top projection is exactly the span of the displayed lower-coordinate vectors. A single vector \(\mathbf D_J\) is not itself a linear domain with a kernel.

These are precise source-map scopes; the full labelled construction and original-zeta Mellin equations remain valid.
