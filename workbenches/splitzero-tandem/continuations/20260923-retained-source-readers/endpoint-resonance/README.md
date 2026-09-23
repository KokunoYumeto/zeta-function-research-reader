# The original zeta endpoint, the heat range, and the arithmetic prime class

This continuation computes the arithmetic content of the endpoint that the theta differential filter loses. The complete proofs are in **ENDPOINT_RESONANCE_AND_PRIME_CLASS.tex**, compiled by **NOTE.tex** into the ten-page **NOTE.pdf**. Original coordinates, the full Gamma and pi factors, both endpoint branches, all prime powers, and the full support lattice are retained.

## SZ-20260923-143 — the obstruction is the original endpoint residue

For the original heat family and the complete filter
\[
N_t=-[1+(Z-2t\partial_Z)^2]/64,
\]
the two adjoint Gaussian tests give exactly
\[
\int_{\mathbb R}e^{-Z^2/(4t)}e^{\pm iZ/(2t)}H_t(Z)\,dZ
=\frac{\sqrt{\pi t}}8e^{-1/(4t)}>0.
\]
This value is fixed by the original residue \(\operatorname{Res}_{s=1}\zeta=1\). Therefore no tempered distribution solves \(N_tI=H_t\) for \(t>0\). More precisely, the Schwartz range is exactly the common kernel of these two moments, with an explicit continuous inverse. On the original even source there is one independent moment.

The stronger quotient calculation is \([H_t]=[1/16]\ne0\) in \(\mathcal S'/N_t\mathcal S'\). The theta-only source is an explicit preimage of \(H_t-1/16\); its retained endpoint supplies the rest.

**Complete proofs:** ER1–21. This strengthens ESH1–18 and SZ-20260923-142 from a particular divergent integral to the exact range obstruction.

## SZ-20260923-144 — both continuations survive in an exact source

The map
\[
(U,c_+,c_-)\longmapsto U+c_+B_++c_-B_-
\]
from \(\mathcal S'_{\rm even}\oplus\mathbb C^2\) into distributions is injective. The two original heat continuations are the different inputs \((L_t,-4,0)\) and \((L_t,0,-4)\). Their full filter images are both \(H_t\). All separate Wronskian endpoint values are evaluated, with common difference
\[
-2\sqrt\pi\,t^{-3/2}e^{-1/(4t)}.
\]
The corresponding boundary formula in the original \(s\) coordinate explicitly includes both terms of the derivative of \(\pi^{-s/2}\Gamma(s/2)\).

**Complete proofs:** ER22–26f; independent derivation in **INDEPENDENT_RESONANCE.md**. This continues the two ESH branches without identifying their sources.

## SZ-20260923-145 — the obstruction has an actual arithmetic test

The even Schwartz function
\[
h_t(Z)=e^{-Z^2/(4t)}H_t(Z)\cos(Z/(2t))
\]
has the evaluated prime-boundary class
\[
\beta[(t_p-1)\otimes h_t]
=\ell_p\otimes\left(H_t(0),\frac{\sqrt{\pi t}}8e^{-1/(4t)}\right)\ne0.
\]
The original periodization still sends this class to zero. Its full Mellin transform is evaluated in ER33 as the sum of two original-zeta terms at \(it(s-\tfrac12)\) and \(1+it(s-\tfrac12)\), with every multiplier displayed.

The further source \(f_t=(\partial_Z^2-\tfrac14)h_t\) has zero Mellin endpoint values and the explicit inverse
\[
h_t(Z)=-\int_{\mathbb R}e^{-|Z-y|/2}f_t(y)\,dy .
\]
Its two prime-boundary moments are
\[
\left(
H_t''(0)-\left(\frac1{2t}+\frac1{4t^2}+\frac14\right)H_t(0),
-\frac{\sqrt{\pi t}}{32}e^{-1/(4t)}
\right),
\]
both strictly negative. These are source-moment signs. The complete original-zeta Weil pairing is given separately in ER37–40, with every trivial-zero cutoff and its Gamma boundary retained. Its scalar value and sign have not yet been evaluated.

**Complete proofs:** ER27–40a; independent mathematical review in **INDEPENDENT_REVIEW_ER34_40.md**. This supplies a new evaluated input to the earlier MRT prime-boundary receiver and to the original-zeta arithmetic pairing.

## Human sources and scope

- Brad Rodgers and Terence Tao, [The de Bruijn–Newman constant is non-negative, arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), original TeX equations hoz, sas, phidef, htdef: the original theta coordinate, source and full zeta multiplier.
- Alain Connes, [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, arXiv:math/9811068v1](https://arxiv.org/abs/math/9811068v1), Section III (6)–(19), Appendix II (1)–(11), Theorems 1 and 6: original moment, periodization, measure and explicit-formula conventions. The noncompact Gaussian extension used here is proved in ER37–40.
- N. M. Temme, [DLMF 7.2.2](https://dlmf.nist.gov/7.2.E2): the entire complementary error function convention.
- The programme's exact algebraic prime quotient is compared with [FR15–25](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ec73ac350d0cda3d95c0bd1361bede33166b4d34/workbenches/splitzero-tandem/continuations/20260923-original-zeta-return/NOTE.tex). Its quotient maps are rederived in ER29.

Fourteen exact auxiliary checks passed. Three numerical source-to-zeta comparisons also passed; those quadratures are explicitly non-certified and are not the proofs. Both independent derivation files contain complete mathematical arguments on their stated scope. All ten rendered pages and the figure were inspected. This work does not settle RH or evaluate the remaining scalar Weil pairing.
