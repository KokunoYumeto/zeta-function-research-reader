# Original-zeta harmonic sweeping, the full off-critical distribution, and an exact summation-image test

25 September 2026. Independent mathematical derivation, HSW0–HSW9.

## HSW0. Sources, original objects and scope

The original author TeX of Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, math/9811068v1](https://arxiv.org/abs/math/9811068v1), was read at lines 2221–2890 of the retained file [../connes98_intake/math_9811068v1_author.tex](https://arxiv.org/abs/math/9811068v1). The portion 2607–2717 was reread separately to recover output truncated in the first read. The locators below refer to that source, not a transcription:

- §VIII introduction, lines 2221–2252: weighted quotients, missing multiplicities, and harmonic resonances.
- §VIII Lemma 1 and Corollary 2, lines 2308–2472: positive-characteristic cutoffs.
- §VIII (16), Theorem 5 and (17)–(26), lines 2495–2618: the global formula, endpoint difference and positive cutoff distribution.
- §VIII Lemma 3 and (27)–(29), lines 2620–2708: the harmonic measure formula, in the positive-characteristic setting.
- §VIII (30)–(33), lines 2717–2833: the proposed number-field passage through the angle of the two cutoff projections and prolate spheroidal functions.
- Lines 2837–2890 begin the separate semiclassical count; they do not prove the global characteristic-zero limit used nowhere below.

The full preceding comparison and its original arithmetic formula were read at [VWR0–VWR10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/FULL_VERTICAL_WEIGHT_RETURN.md). The original Mellin quotient and full zero-jet synthesis are [OMS](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), using Ralf Meyer, [math/0412277v3](https://arxiv.org/abs/math/0412277v3). The original two-chart arithmetic sheaf is due to Alain Connes and Caterina Consani, [0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), with the exact source comparison retained in [DCP](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SOURCE_CC_DOUBLE_PULLBACK.md). These sources retain their human authorship. The calculations HSW2–HSW9 are the present independent application to the already reconstructed original coefficient space.

Primitive \(Z_1/\tau\) has no source addition, parity, numerical coordinate or numerical weight here. All sums, complex functions, measures and Hilbert operations below are in the stated receiving spaces. The entire source lattice and the existing coefficient labels stay unchanged. This calculation does not replace a support label by a complex number.

Keep the actual test space
\[
A=\{b\in C^\infty(\mathbb R_{>0}):
p_{N,j}(b)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jb(u)|<\infty
\text{ for every }N,j\ge0\},
\]
\[
S=\{h\in\mathcal S(\mathbb R):h(-v)=h(v),\ h(0)=0,\ \int_{\mathbb R}h(v)\,dv=0\},
\]
\[
\Sigma h(u)=2\sum_{n\ge1}h(nu),\quad J=\Sigma S,\quad Q=A/J,\quad
F(s)=M_0b(s)=\int_0^\infty b(u)u^s\frac{du}{u}.
\tag{HSW0.1}
\]
The image \(J\) is the original closed Fréchet image. The original nontrivial zeros are \(\rho=\beta+i\gamma\), with multiplicity \(m_\rho\); every zero sum below is over distinct zero locations, with \(m_\rho\) explicitly present. The original Mellin ideal consists of functions vanishing to order \(m_\rho\) at every such zero.

## HSW1. Exact test maps to Connes's formula

Restrict to the trivial character of the compact norm-one factor of the rational idèle class group. Its Haar mass is one; the remaining Haar measure is \(du/u\). For \(b\in C_c^\infty(\mathbb R_{>0})\), define, without deleting any density factor,
\[
f_b(u)=u^{1/2}b(u),\qquad
h_b(u)=Rb(u)=u^{-1}b(u^{-1}).
\tag{HSW1.1}
\]
Then the test convention in Connes §VIII, line 2603 is exactly
\[
f_b(u)=u^{-1/2}h_b(u^{-1}).
\tag{HSW1.2}
\]
The Fourier–Mellin convention in his Lemma 3 is
\[
\widehat f_b(z)=\int_0^\infty f_b(u)u^z\frac{du}{u}
=F(\tfrac12+z).
\tag{HSW1.3}
\]
The variable \(z\) in that formula is therefore \(\rho-\tfrac12\), not the original zeta argument \(\rho\).

The inversion \(\widetilde f_b(u)=f_b(u^{-1})\) in source lines 2604–2605 has transform
\[
\widehat{\widetilde f_b}(z)=F(\tfrac12-z).
\tag{HSW1.4}
\]
Reflection of the entire original zero divisor, including multiplicities, proves that summing this expression gives the same total spectral distribution as HSW1.3. Reflection together with conjugation also preserves the harmonic distribution constructed below. Neither test inversion is suppressed.

Let
\[
g_b(x)=e^{x/2}b(e^x).
\]
It is a Schwartz function with every exponential weight. Direct substitution gives
\[
F(\tfrac12+it)=\int_{\mathbb R}g_b(x)e^{itx}\,dx.
\tag{HSW1.5}
\]
The transform has the displayed plus sign and no Fourier multiplier. All later constants use that convention.

Connes's quoted cutoff trace statement initially has compactly supported idèle-class tests. The distributional formulas constructed below extend continuously to the full \(A\). That extension does not assert convergence of his number-field cutoff operators on this larger test space.

## HSW2. Harmonic measure for each actual original zero

For an actual zero put
\[
\delta_\rho=|\beta-\tfrac12|.
\]
If \(\delta_\rho>0\), its harmonic probability measure on the critical line has the explicit density
\[
P_{\delta_\rho}(t-\gamma)\,dt,\qquad
P_\delta(y)=\frac{\delta}{\pi(y^2+\delta^2)}.
\tag{HSW2.1}
\]
If \(\delta_\rho=0\), it is the point mass at \(t=\gamma\). In original \(s\)-coordinates the point of the line is \(s=\tfrac12+it\).

The integral of \(P_\delta\) is one by the arctangent antiderivative. Its exact Fourier identity is
\[
\int_{\mathbb R}e^{itx}P_\delta(t-\gamma)\,dt
=e^{i\gamma x}e^{-\delta|x|}.
\tag{HSW2.2}
\]
For \(x>0\), integrate the rational function times \(e^{itx}\) in the upper half-plane; the pole at \(\gamma+i\delta\) has residue \(e^{i(\gamma+i\delta)x}/(2\pi i)\). The semicircle contribution tends to zero by splitting it into endpoint arcs, where the rational denominator is of order the radius squared, and their complement, where the exponential decays. For \(x<0\) the lower contour has the opposite orientation and gives the same displayed formula. At \(x=0\) it follows from the total mass. This also fixes every sign and factor of \(\pi\).

Define the actual one-zero harmonic observation
\[
\mathcal H_\rho(b)=
\int_{\mathbb R}F(\tfrac12+it)P_{\delta_\rho}(t-\gamma)\,dt
\quad(\delta_\rho>0),
\]
and \(\mathcal H_\rho(b)=F(\rho)\) on the critical line. Fubini is justified by
\(\int|g_b(x)|dx<\infty\) and the probability mass. It yields
\[
\boxed{\mathcal H_\rho(b)=
\int_{\mathbb R}g_b(x)e^{i\gamma x}e^{-\delta_\rho|x|}\,dx.}
\tag{HSW2.3}
\]
By contrast the original zero observation is
\[
F(\rho)=\int_{\mathbb R}g_b(x)e^{i\gamma x}
e^{(\beta-1/2)x}\,dx.
\tag{HSW2.4}
\]
Both integrals converge absolutely. Their distinct kernels have been calculated on the same original test, rather than inferred from a name for the receiving spectrum.

## HSW3. The full infinite harmonic distribution

Write
\[
B_2(F)=\sup_{t\in\mathbb R}(1+|t|)^2|F(\tfrac12+it)|,\qquad
C_2=\sum_\rho m_\rho(1+|\gamma|)^{-2}<\infty.
\]
The finiteness follows from the original zero count \(N(T)=O(T\log(eT))\), by summing over dyadic height intervals. No assertion about their real parts beyond \(0<\beta<1\) is needed.

For every zero,
\[
|\mathcal H_\rho(b)|\le9B_2(F)(1+|\gamma|)^{-2}.
\tag{HSW3.1}
\]
For \(|\gamma|<2\), use the probability mass and \(1\le9(1+|\gamma|)^{-2}\). For \(|\gamma|\ge2\), split at \(|t-\gamma|\le|\gamma|/2\). In that region \(|t|\ge|\gamma|/2\), giving at most \(4B_2(F)(1+|\gamma|)^{-2}\). In its complement,
\[
P_\delta(t-\gamma)\le\frac{4\delta}{\pi\gamma^2}
\le\frac2{\pi\gamma^2},\qquad
\int_{\mathbb R}|F(\tfrac12+it)|dt\le2B_2(F).
\]
This gives at most \(9B_2(F)/(\pi(1+|\gamma|)^2)\) for the second region. Since \(4+9/\pi<9\), HSW3.1 follows. The critical-line point-mass case has the stronger constant one.

Consequently the following distributions are well-defined and continuous on the entire original \(A\):
\[
\mathcal H_{\rm all}(b)=\sum_\rho m_\rho\mathcal H_\rho(b),\qquad
\mathcal H_{\rm off}(b)=\sum_{\beta\ne1/2}m_\rho\mathcal H_\rho(b),
\]
\[
|\mathcal H_{\rm all}(b)|,\ |\mathcal H_{\rm off}(b)|
\le9C_2B_2(F).
\tag{HSW3.2}
\]
Every series here is absolutely convergent.

More concretely,
\[
W_{\rm off}(t)=
\sum_{\beta\ne1/2}
m_\rho\frac{|\beta-1/2|}
{\pi((t-\gamma)^2+|\beta-1/2|^2)}
\tag{HSW3.3}
\]
converges locally uniformly on the real line. On a fixed compact interval, the large-\(|\gamma|\) tail is bounded by a constant multiple of
\(\sum m_\rho/\gamma^2\); the remaining zeros are finite in number and each density is continuous. Thus \(W_{\rm off}\) is continuous, nonnegative, and strictly positive everywhere if there is any off-critical zero.

The full measure is
\[
d\nu_{\rm harm}(t)=
\sum_{\beta=1/2}m_\rho\,\delta_\gamma(dt)
+W_{\rm off}(t)\,dt.
\tag{HSW3.4}
\]
It is a positive tempered measure. Indeed HSW2.2 proves the Poisson convolution identity and hence
\[
\int_{\mathbb R}\frac{P_\delta(t-\gamma)}{1+t^2}\,dt
=\frac{1+\delta}{(1+\delta)^2+\gamma^2}.
\tag{HSW3.5}
\]
Since \(0<\delta<1/2\), the right side is at most
\(3/[2(1+\gamma^2)]\). Summing proves finite weighted mass, including the analogous point-mass terms. Finally,
\[
\mathcal H_{\rm off}(b)=\int_{\mathbb R}F(\tfrac12+it)W_{\rm off}(t)\,dt,\qquad
\mathcal H_{\rm all}(b)=\int_{\mathbb R}F(\tfrac12+it)d\nu_{\rm harm}(t).
\tag{HSW3.6}
\]
Tonelli applied to the absolute integrands, using HSW3.1, proves these identities.

This constructs the rational original-zeta analogue of the harmonic distribution in Connes §VIII Lemma 3. It does not identify it with the limit of a characteristic-zero cutoff trace; that would be a further assertion about those specified operators.

## HSW4. Exact difference from the original off-critical trace

Retain VWR10's original distribution
\[
\Theta_{\rm off}(b)=\sum_{\beta\ne1/2}m_\rho F(\rho).
\]
It descends through \(J\), because every original zero value vanishes on \(J\). Define the exact comparison defect
\[
\mathcal E(b)=\Theta_{\rm off}(b)-\mathcal H_{\rm off}(b).
\tag{HSW4.1}
\]
It is continuous by HSW3 and the original strip estimates.

Horizontal reflection takes \(\rho=\tfrac12+\delta+i\gamma\) to
\(1-\bar\rho=\tfrac12-\delta+i\gamma\), with identical multiplicity. Sum once over the actual right-hand zeros, retaining both members:
\[
\boxed{\mathcal E(b)=
2\sum_{\beta>1/2}m_\rho
\int_{\mathbb R}g_b(x)e^{i\gamma x}
\sinh((\beta-\tfrac12)|x|)\,dx.}
\tag{HSW4.2}
\]
Indeed their two original kernels add to \(2\cosh(\delta x)\), and their two harmonic kernels add to \(2e^{-\delta|x|}\). Their difference is \(2\sinh(\delta|x|)\). The integrals in HSW4.2 form an absolutely summable series because each equals the corresponding two original observations minus two harmonic observations, all already proved summable. The equation does not assert pointwise convergence of an unsmoothed oscillatory kernel sum.

Write the original arithmetic terms in full:
\[
P_\zeta(b)=\sum_{n=2}^\infty\Lambda(n)
\bigl(b(n)+n^{-1}b(n^{-1})\bigr),
\]
\[
A_\infty(b)=\frac1{2\pi}\int_{\mathbb R}F(\tfrac12+it)
\left[
\frac12\psi(\tfrac14+it/2)+\frac12\psi(\tfrac14-it/2)-\log\pi
\right]dt,
\]
where \(\Lambda(p^r)=\log p\) for every \(r\ge1\), and it is zero on other integers. The original explicit formula proved and extended in VWR10 gives the exact global identity
\[
\boxed{\mathcal E(b)
=F(0)+F(1)+A_\infty(b)-P_\zeta(b)-\mathcal H_{\rm all}(b).}
\tag{HSW4.3}
\]
The critical-line sum cancels between the two spectral distributions because its harmonic measures are the same point masses. This is the precise relation among the full arithmetic record, the harmonic potential and the original off-critical distribution.

For every finite trivial-zero cutoff \(M\), keep the unreduced formula
\[
\mathcal E(b)+\sum_{r=1}^M F(-2r)-F(1)
=A_\infty(b)+F(0)+\sum_{r=1}^M F(-2r)
-P_\zeta(b)-\mathcal H_{\rm all}(b).
\tag{HSW4.4}
\]
No limit of the trivial-zero sum is taken. The original return at each such zero still has
\[
\operatorname{Res}_{s=-2r}\frac{F(s)}{\zeta(s)}
=\frac{F(-2r)}{\zeta'(-2r)},\qquad
\zeta'(-2r)=(-1)^r2^{-2r-1}\pi^{-2r}(2r)!\zeta(1+2r).
\tag{HSW4.5}
\]
The multiplier relating the two original zeta arguments is retained:
\[
\zeta(s)=
\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}\zeta(1-s).
\tag{HSW4.6}
\]
Nothing in HSW4.3 replaces \(\zeta\) by its completion.

## HSW5. A fully constructed original summation-image test

The following witness is defined using the actual \(\Sigma\), including its factor two. Put
\[
h_0(v)=
\frac{\log|v|-2}{8\sqrt\pi}
\exp\!\left(-\frac{(\log|v|)^2}{4}\right)\quad(v\ne0),
\qquad h_0(0)=0.
\tag{HSW5.1}
\]
It is real, even and Schwartz. Each ordinary derivative at either endpoint is a finite sum of powers of \(v^{-1}\) and \(\log|v|\) times the displayed Gaussian; its quadratic decay in \(\log|v|\) dominates every such exponential and polynomial. In particular the extension at zero is smooth and flat.

For the full Mellin transform, substitute \(v=\exp x\) and differentiate the Gaussian integral:
\[
\int_{\mathbb R}e^{-x^2/4+sx}\,dx=2\sqrt\pi\,e^{s^2},\qquad
\int_0^\infty h_0(v)v^s\frac{dv}{v}
=\frac{s-1}{2}e^{s^2}.
\tag{HSW5.2}
\]
The first identity follows by completing the square for real \(s\), and for all complex \(s\) by entire continuation justified on compact sets by Gaussian domination. At \(s=1\), HSW5.2 and evenness give \(\int_{\mathbb{R}} h_0=0\). Thus \(h_0\in S\).

Let \(b_0=\Sigma h_0\in J\). The original Mellin calculation, first in \(\Re s>1\), is
\[
G(s)=M_0b_0(s)
=2\zeta(s)\frac{s-1}{2}e^{s^2}
=(s-1)\zeta(s)e^{s^2}.
\tag{HSW5.3}
\]
This identity continues everywhere. At \(s=1\) the actual simple pole of \(\zeta\), with residue one, gives \(G(1)=\exp(1)\); at zero, \(\zeta(0)=-1/2\) gives \(G(0)=1/2\).

On \(A\), define the actual multiplicative convolution
\[
(a*c)(u)=\int_0^\infty a(v)c(u/v)\frac{dv}{v},\qquad
a^\#(u)=u^{-1}\overline{a(u^{-1})}.
\]
Both operations preserve \(A\). In logarithmic coordinates the first is ordinary convolution of functions with every exponential Schwartz bound; differentiating under the integral and using
\(e^{N|x|}\le e^{N|y|}e^{N|x-y|}\) bounds every output derivative by an integrable weighted factor times a bounded weighted factor. The involution follows by substitution and the product rule. Absolute convergence proves \(M_0(a*c)=(M_0a)(M_0c)\), first on any fixed vertical line; every line is allowed by the original endpoint decay. The involution has
\[
M_0(a^\#)(s)=\overline{M_0a(1-\bar s)}.
\tag{HSW5.4}
\]

Now construct
\[
b_\dagger=b_0*b_0^\#=b_0*Rb_0,\qquad
F_\dagger(s)=G(s)\overline{G(1-\bar s)}=G(s)G(1-s).
\tag{HSW5.5}
\]
Reality of \(b_0\) proves the second equality. This is an actual element of \(J\), not merely a formal Mellin expression. An explicit preimage is
\[
h_\dagger(t)=\int_0^\infty Rb_0(v)h_0(t/v)\frac{dv}{v}.
\tag{HSW5.6}
\]
To prove \(h_\dagger\in S\), differentiation contributes \(v^{-j}\), and
\((1+|t|)^N\le\max(1,v)^N(1+|t/v|)^N\). The resulting integral of
\(|Rb_0(v)|v^{-j}\max(1,v)^N\,dv/v\) is finite by \(Rb_0\in A\). This proves every Schwartz seminorm and differentiation under the integral. Evenness and value zero follow from \(h_0\). Fubini gives
\(\int h_\dagger=(\int_0^\infty Rb_0(v)\,dv)(\int h_0)=0\).
Finally, absolute convergence gives
\[
\Sigma h_\dagger(u)=
\int_0^\infty Rb_0(v)\,2\sum_{n\ge1}h_0(nu/v)\frac{dv}{v}
=b_\dagger(u).
\tag{HSW5.7}
\]
For this interchange, the absolute sum of the Schwartz function \(h_0\) is bounded by a constant times \(1+v/u\), and the resulting two moments of \(|Rb_0|\) are finite. Thus the original summation map and its two moment constraints are explicitly retained.

The entire auxiliary Mellin function is
\[
\boxed{F_\dagger(s)=
-s(s-1)\zeta(s)\zeta(1-s)
\exp\!\left(s^2+(1-s)^2\right).}
\tag{HSW5.8}
\]
This is a test function, not a replacement zeta function. Each apparent endpoint singularity has the explicit value
\[
F_\dagger(0)=F_\dagger(1)=\frac{\exp(1)}2.
\tag{HSW5.9}
\]
It vanishes to order \(2m_\rho\) at each original nontrivial zero. It also vanishes at every \(-2r\) and \(1+2r\), \(r\ge1\), by the respective original trivial-zero factors. On the critical line,
\[
F_\dagger(\tfrac12+it)=|G(\tfrac12+it)|^2\ge0.
\tag{HSW5.10}
\]
The restriction is not identically zero, since \(G\) is a nonzero entire function and cannot vanish on a line interval.

## HSW6. Quantitative harmonic value on that original zero class

Since \(b_\dagger\in J\), all original zero traces vanish:
\[
Z(F_\dagger)=0,\qquad \Theta_{\rm off}(b_\dagger)=0.
\tag{HSW6.1}
\]
The critical harmonic terms also vanish. By HSW3 and HSW5,
\[
\boxed{\mathcal H_{\rm all}(b_\dagger)
=\mathcal H_{\rm off}(b_\dagger)
=\int_{\mathbb R}|G(\tfrac12+it)|^2W_{\rm off}(t)\,dt.}
\tag{HSW6.2}
\]
This is finite. If any actual off-critical zero exists, it is strictly positive: its Poisson density is strictly positive everywhere, and the nonzero analytic boundary function has positive squared integral on some, indeed every nonempty, interval.

There is an explicit lower bound attached to every actual reflected pair. For \(T>0\), put
\[
A_T=\int_{-T}^T|G(\tfrac12+it)|^2dt>0.
\]
For a right-hand zero \(\rho=\tfrac12+\delta+i\gamma\), its horizontal pair contributes
\[
\mathcal H_{\rm off}(b_\dagger)\ \ge\
\frac{2m_\rho\delta\,A_T}
{\pi((|\gamma|+T)^2+\delta^2)}.
\tag{HSW6.3}
\]
The denominator bounds \((t-\gamma)^2+\delta^2\) from above on that interval, and every other summand is nonnegative. This retains the full multiplicity and the factor two from horizontal reflection.

Consequently \(\mathcal H_{\rm off}\), or \(\mathcal H_{\rm all}\), can descend as a functional through the actual quotient \(A/J\) only if there are no off-critical zeros. The proof uses the single explicitly constructed element \(b_\dagger\in J\); no off-critical zero was assumed to exist. If all zeros are on the line, \(\mathcal H_{\rm all}=Z\) and \(\mathcal H_{\rm off}=0\), so descent does hold. This computes the precise quotient relation rather than identifying harmonic sweeping with the quotient in advance.

The defect on this test is therefore
\[
\mathcal E(b_\dagger)=
-\int_{\mathbb R}|G(\tfrac12+it)|^2W_{\rm off}(t)\,dt.
\tag{HSW6.4}
\]
The full original arithmetic identity on it is
\[
P_\zeta(b_\dagger)=\exp(1)+A_\infty(b_\dagger).
\tag{HSW6.5}
\]
Both Gamma derivatives in \(A_\infty\), both endpoint halves in HSW5.9, and both prime/repetition terms in \(P_\zeta\) remain. For every finite trivial-zero cutoff, all its \(F_\dagger(-2r)\) terms are zero by HSW5.8, not because they were omitted from the formula.

Under HSW1, \(f_{b_\dagger}=f_{b_0}*f_{b_0}^*\), where the group involution is \(f^*(u)=\overline{f(u^{-1})}\). Indeed multiplication by \(u^{1/2}\) preserves multiplicative convolution and sends \(b_0^\#\) to \(f_{b_0}^*\). Thus the nonnegative harmonic value is exactly a positive-type test of the convention in Connes §VIII (24)–(25), with all density factors proved. Positivity of this harmonic functional alone does not prove equality with the original arithmetic functional.

## HSW6A. Faithful quantitative size of the whole off-critical contribution

The positivity test controls the entire original off-critical divisor by one finite weighted size:
\[
S_{\rm off}=\sum_{\beta\ne1/2}
 \frac{m_\rho|\beta-1/2|}{1+\gamma^2}.
\tag{HSW6A.1}
\]
It is finite by \(0<|\beta-1/2|<1/2\) and the original zero-count estimate. No enumeration or selection of finitely many zeros is substituted for this sum.

All constants in the following estimate are fixed by the single explicit \(G\) in HSW5.3:
\[
A_1=\int_{-1}^1|G(\tfrac12+it)|^2dt,\qquad
L_0=\int_{\mathbb R}|G(\tfrac12+it)|^2dt,
\]
\[
B_0=\sup_{t\in\mathbb R}(1+t^2)|G(\tfrac12+it)|^2,\qquad
M_1=\sup_{\substack{0\le\sigma\le1\\t\in\mathbb R}}
 (1+t^2)|G'(\sigma+it)|.
\tag{HSW6A.2}
\]
Here \(A_1>0\) by the identity theorem, and the remaining quantities are finite because \(G=M_0b_0\) and \(b_0\in A\), including all logarithmic derivative moments. In particular the apparent pole at \(s=1\) in the original formula for \(G\) has the explicit cancellation already computed; it is not a singularity in \(M_1\).

The full estimate is
\[
\boxed{
\frac{4A_1}{9\pi}\,S_{\rm off}
\ \le\ \mathcal H_{\rm off}(b_\dagger)\
\le\frac{18M_1^2+5L_0+8B_0}{\pi}\,S_{\rm off}.}
\tag{HSW6A.3}
\]
We prove both inequalities for each zero before summing.

For a zero \(\rho=\beta+i\gamma\), put \(\delta=|\beta-1/2|>0\). On \(|t|\le1\),
\[
(t-\gamma)^2+\delta^2
\le2t^2+2\gamma^2+\tfrac14
\le\tfrac94(1+\gamma^2).
\]
Insert this denominator bound into the nonnegative integral HSW6.2. Its contribution from the one zero is at least
\(4\delta A_1/[9\pi(1+\gamma^2)]\).

For the upper bound, the fact that this is an actual zero, \(G(\rho)=0\), is essential. It gives the exact identity
\[
\mathcal H_\rho(b_\dagger)
=\frac{\delta}{\pi}
 \int_{\mathbb R}\left|
 \frac{G(\tfrac12+it)}{\tfrac12+it-\rho}\right|^2dt.
\tag{HSW6A.4}
\]
Near \(|t-\gamma|\le1\), integrate \(G'\) along the straight segment from \(\rho\) to \(\tfrac12+it\). Every real part of that segment belongs to \([0,1]\); every imaginary part \(y\) satisfies \(|y-\gamma|\le1\), hence
\(1+\gamma^2\le3(1+y^2)\). Therefore
\[
\left|\frac{G(\tfrac12+it)}{\tfrac12+it-\rho}\right|
\le\frac{3M_1}{1+\gamma^2}.
\]
The integral over this interval of length two is bounded by
\(18M_1^2/(1+\gamma^2)^2\), and hence by
\(18M_1^2/(1+\gamma^2)\).

On \(|t-\gamma|>1\), the denominator squared is at least \((t-\gamma)^2\). When \(|\gamma|\le2\), this gives integral at most \(L_0\), and thus at most \(5L_0/(1+\gamma^2)\). When \(|\gamma|>2\), split the remaining integral into \(|t|<|\gamma|/2\) and \(|t|\ge|\gamma|/2\). In the first part \(|t-\gamma|\ge|\gamma|/2\), giving
\[
\frac{4L_0}{\gamma^2}\le\frac{5L_0}{1+\gamma^2}.
\]
In the second part the numerator is at most \(4B_0/(1+\gamma^2)\), and
\(\int_{|v|>1}v^{-2}dv=2\). Its contribution is at most
\(8B_0/(1+\gamma^2)\). These bounds prove
\[
\int_{\mathbb R}\left|
 \frac{G(\tfrac12+it)}{\tfrac12+it-\rho}\right|^2dt
\le\frac{18M_1^2+5L_0+8B_0}{1+\gamma^2}.
\]
Together with HSW6A.4 this is the stated upper estimate for each zero. Multiply both bounds by the original \(m_\rho\), then sum the nonnegative terms. Absolute convergence, already proved independently, and monotone convergence both justify this step. This proves HSW6A.3.

In particular the failure of harmonic descent on this one original zero class is not subject to cancellation among different zeros. Its magnitude
\(-\mathcal E(b_\dagger)=\mathcal H_{\rm off}(b_\dagger)\)
is quantitatively equivalent, with the displayed fixed constants, to the whole weighted distance \(S_{\rm off}\). No positive lower bound on the distances \(\delta_\rho\) was assumed. The zero relation in HSW6A.4 is precisely what prevents an uncontrolled \(1/\delta_\rho\) loss as zeros approach the critical line.

## HSW6B. Canonical original primary representatives and the exact positive norm sum

There is an exact return of HSW6A.4 to the original \(A\) and \(Q\). For every actual nontrivial zero \(\rho\), define
\[
U_\rho(s)=\frac{G(s)}{s-\rho}.
\tag{HSW6B.1}
\]
It is entire because \(G(\rho)=0\). On every vertical strip away from a fixed disk around \(\rho\), division contributes only a rational factor; inside that disk Taylor division is holomorphic. These observations prove every original Schwartz strip bound for \(U_\rho\). Its unique raw inverse Mellin representative is also given by the two explicit integrals
\[
\boxed{
b_\rho(u)=u^{-\rho}\int_u^\infty v^{\rho-1}b_0(v)\,dv
=-u^{-\rho}\int_0^u v^{\rho-1}b_0(v)\,dv.}
\tag{HSW6B.2}
\]
The equality follows from \(G(\rho)=0\), with both endpoint integrals absolutely convergent. Use the first expression as \(u\to\infty\) and the second as \(u\to0\). Every power bound for \(b_0\) then gives every power bound for \(b_\rho\). Differentiation gives
\[
(L-\rho)b_\rho=b_0,\qquad L=-u\partial_u,
\tag{HSW6B.3}
\]
which proves every Euler-derivative bound by induction. Thus \(b_\rho\in A\). Taking the Mellin transform in HSW6B.3 and using vanishing endpoint terms gives \(M_0b_\rho=U_\rho\), first for \(s\ne\rho\) and then at \(\rho\) by holomorphy. Any two solutions in \(A\) differ by a constant times \(u^{-\rho}\), which cannot belong to \(A\) unless that constant is zero. The representative is therefore canonical for the explicitly fixed \(b_0\).

Write the exact original zero germ as
\[
\zeta(\rho+t)=\frac{\zeta^{(m_\rho)}(\rho)}{m_\rho!}t^{m_\rho}
+O(t^{m_\rho+1}).
\]
The full primary jet of HSW6B.1 is
\[
U_\rho(\rho+t)\equiv
\frac{(\rho-1)\exp(\rho^2)\zeta^{(m_\rho)}(\rho)}{m_\rho!}
t^{m_\rho-1}
\pmod{t^{m_\rho}}.
\tag{HSW6B.4}
\]
Every factor in its leading coefficient is nonzero. At every other original nontrivial zero, all required original jets still vanish, because division by \(s-\rho\) is invertible there. Consequently \([b_\rho]\in Q\) is precisely the nonzero top-jet eigenvector in the original primary block, with the coefficient in HSW6B.4 retained; \((L-\rho)[b_\rho]=0\). When \(m_\rho>1\), this is an eigenvector inside the full primary block, not a claim that its nilpotent extension has disappeared.

The Fourier convention HSW1.5 gives the full Plancherel factor
\[
\int_{\mathbb R}|U_\rho(\tfrac12+it)|^2dt
=2\pi\int_{\mathbb R}|e^{x/2}b_\rho(e^x)|^2dx
=2\pi\int_0^\infty|b_\rho(u)|^2du.
\tag{HSW6B.5}
\]
Insert this into HSW6A.4. For every off-critical zero,
\[
\boxed{\mathcal H_\rho(b_\dagger)
=2|\beta-\tfrac12|\,\|b_\rho\|_{L^2(du)}^2.}
\tag{HSW6B.6}
\]
For an on-line zero the harmonic observation is zero by HSW5.10, so HSW6B.6 remains true with its zero coefficient; the norm itself remains strictly positive. Summing the already proved nonnegative convergent series gives
\[
\boxed{
\mathcal H_{\rm off}(b_\dagger)
=\mathcal H_{\rm all}(b_\dagger)
=2\sum_{\rho\in\mathscr Z}
m_\rho|\Re\rho-\tfrac12|\,\|b_\rho\|_{L^2(du)}^2.}
\tag{HSW6B.7}
\]
Thus the global harmonic defect is an exact positive sum on canonical representatives of actual original primary vectors, including every original multiplicity. The earlier uniform estimates in fact give the following bound for every actual nontrivial zero, including a critical-line zero:
\[
\frac{2A_1}{9\pi(1+\gamma^2)}
\le\|b_\rho\|_{L^2(du)}^2
\le\frac{18M_1^2+5L_0+8B_0}{2\pi(1+\gamma^2)}.
\tag{HSW6B.8}
\]
These are bounds for the specified original representatives, not for arbitrary representatives of their classes. The critical-line extension is proved directly in [HSC5](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/HSW_INDEPENDENT_CHECK.md): estimate the entire quotient G(s)/(s−rho), filling its removable value on the integration line. The denominator bound on [−1,1] and the difference-quotient bounds in HSW6A hold also when the real-part distance is zero. Plancherel then gives HSW6B.8 without dividing by that distance. The complete all-prime source return and Green identity for these same representatives are proved in [OPD1–OPD5](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/ORIGINAL_PRIME_DILATION_FORCING_IDENTITY.md).

The density of \(J\) in ordinary \(L^2(du)\) is the already established [ASD10.6–ASD10.7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ACTUAL_SUPPORTED_DUALITY_INDEPENDENT.md), also retained in [WHR0](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/WEIGHTED_HILBERT_RETURN_AND_EXACT_KERNEL.md); it is not a new result of this note. Thus its quotient norm would be zero. For completeness the same proof can use the specific original \(b_0\) of the present calculation. The map \(b(u)\mapsto e^{x/2}b(e^x)\) is an isometry from \(L^2(du)\) to \(L^2(dx)\). The subspace \(J\) contains every dilation \(T_a b_0\); their images are
\(a^{1/2}g_{b_0}(x-\log a)\). Suppose a vector is orthogonal to all these translates. Plancherel turns the correlation with \(g_{b_0}\) into the inverse Fourier transform of the product of its Fourier transform with the conjugate of \(G(\tfrac12+it)\). That product is integrable by Cauchy–Schwarz. Vanishing of every correlation and uniqueness of the Fourier transform on \(L^1\) force the product to vanish almost everywhere. The factor \(G(\tfrac12+it)\) is nonzero almost everywhere, since its zeros on the line are discrete. Hence the orthogonal vector is zero. The closed span of these actual dilations, and therefore the closure of \(J\), is all of \(L^2(du)\).

Publication source credit: The Fourier L2 identity is classical: R. Roy, F. W. J. Olver, R. A. Askey, R. Wong and W. P. Reinhardt, NIST DLMF Chapter1, [§1.14(i), Parseval formula](https://dlmf.nist.gov/1.14#i). The receiving calculation below retains its own stated Fourier convention and derives the corresponding factors. This pass checked DLMF, not the Titchmarsh predecessor pages cited there.

No norm or inner product on \(Q\) is inferred from HSW6B.7. What it provides is the explicit positive scalar sum of norms of the unique solutions HSW6B.2, tied to the original source vector \(b_0=\Sigma h_0\), with their original quotient classes and all coefficients proved.

## HSW7. The harmonic density retains the entire off-critical divisor

The harmonic density has more information than a critical-line list of eigenvalues. Extend HSW3.3 to a complex argument \(z\):
\[
\mathscr W_{\rm off}(z)=
\sum_{\beta\ne1/2}
m_\rho\frac{\delta_\rho}{\pi((z-\gamma)^2+\delta_\rho^2)}.
\tag{HSW7.1}
\]
On every compact subset avoiding the displayed poles, this series converges uniformly. For \(|z|\le R\) and \(|\gamma|\ge2R+2\), both factors \(z-\gamma\pm i\delta_\rho\) have modulus at least \(|\gamma|/2\), so the summand is bounded by \(2m_\rho/(\pi\gamma^2)\). Only finitely many remaining zero locations occur. This proves a meromorphic function, whose real restriction is \(W_{\rm off}\).

For each horizontal pair \(\tfrac12\pm\delta+i\gamma\) of multiplicity \(m\), its exact rational contribution is
\[
\frac{2m\delta}{\pi((z-\gamma)^2+\delta^2)}
=\frac{m}{\pi i}\left(
\frac1{z-\gamma-i\delta}-\frac1{z-\gamma+i\delta}\right).
\tag{HSW7.2}
\]
No other pair can cancel either pole. A pole location determines its real part \(\gamma\), its distance \(\delta\) from the real line, and its upper or lower half-plane; all pairs contributing at that location are the same pair with their original multiplicity already combined. Hence
\[
\operatorname{Res}_{z=\gamma+i\delta}\mathscr W_{\rm off}
=\frac{m}{\pi i},\qquad
\operatorname{Res}_{z=\gamma-i\delta}\mathscr W_{\rm off}
=-\frac{m}{\pi i}.
\tag{HSW7.3}
\]
The original coordinate map is
\[
s=\tfrac12+iz.
\tag{HSW7.4}
\]
The upper pole gives the original left-hand zero
\(s=\tfrac12-\delta+i\gamma\), and the lower pole gives the original right-hand zero
\(s=\tfrac12+\delta+i\gamma\). HSW7.3 recovers the original integer multiplicity exactly.

Thus the full harmonic density on the line determines the entire original off-critical zero divisor, including multiplicities. Uniqueness is rigorous: its meromorphic extension is unique by the identity theorem on a neighborhood of any real interval, followed by continuation on the connected plane with the discrete pole set removed. Knowledge of the continuous distribution on compact smooth tests determines its density on the real line; no individual cutoff or finite measurement is asserted to perform this continuation stably.

This calculation does not recover every local derivative of \(\zeta\) from the harmonic density alone. The full original residue pairing retains those derivatives as in GZR and VWR8. What HSW7 proves is an exact, faithful encoding of the off-critical divisor by its global harmonic potential. Such encoding is compatible with the failure of descent in HSW6: a functional of the original test can retain spectral information without being a functional on the original quotient.

## HSW8. Cutoff and characteristic dependence: the exact comparison retained

In the original source the semilocal ordered cutoff is
\[
R_\Lambda=\widehat P_\Lambda P_\Lambda.
\]
The orthogonal projection \(Q_\Lambda\) onto the intersection of ranges is a different specified operator. Lemma 1 proves eventual commutation on fixed character sectors in positive characteristic; this is used to pass from the semilocal ordered cutoff to Corollary 2's projection. The global formula (16), lines 2495–2506, then has
\[
\operatorname{Tr}(Q_\Lambda U(h))
=2h(1)\log'\Lambda
+\sum_v\int_{\mathbb Q_v^\times}'\frac{h(u^{-1})}{|1-u|}\,d^*u+o(1)
\tag{HSW8.1}
\]
in the rational notation under discussion. This displayed rational formula is the proposed characteristic-zero analogue, not a theorem proved here by the positive-characteristic statement.

The source's Theorem 5, lines 2523–2540, explicitly assumes a global field of positive characteristic. Its proof keeps \(B_{\Lambda,0}\) and \(Q_{\Lambda,0}\) separate from \(B_\Lambda,Q_\Lambda\), and uses
\[
Q'_{\Lambda,0}=E Q_{\Lambda,0}E^{-1}\le S_\Lambda,\qquad
\Delta_\Lambda(f)=
\operatorname{Tr}((S_\Lambda-Q'_{\Lambda,0})V(f)).
\tag{HSW8.2}
\]
The positive-type assertion concerns this difference, not either trace alone. The intertwining has its full scalar
\[
EU(a)=|a|^{1/2}V(a)E.
\tag{HSW8.3}
\]
The source explicitly says at lines 2615–2616 that its endpoint term \(D\) comes from the distinction between the zero-moment and unrestricted cutoff subspaces. The two endpoint values in HSW4.3 and HSW5.9 therefore cannot be discarded when comparing its positive difference with the actual original zeta formula.

In positive characteristic, the norm subgroup is \(q^{\mathbb Z}\), and Lemma 3 sums centered zero parameters modulo its annihilator. Harmonic measure tested on that periodic transform gives the circle Poisson formula in (29). In the rational calculation above the norm group is \(\mathbb R_{>0}\), and the full real-line density HSW2.1 is used with no periodic identification. These are exact different domains of the same harmonic-measure operation.

The number-field passage in source lines 2747–2833 replaces impossible simultaneous exact compact support in the real and Fourier variables by a prolate spheroidal cutoff. It retains
\[
H_\Lambda=-\partial((\Lambda^2-x^2)\partial)+(2\pi\Lambda x)^2,
\]
and selects the source's even eigenfunctions with index \(n\le4\Lambda^2\), then tensors with the finite-place characteristic function. That discussion is not a proof supplied here of the global asymptotic HSW8.1 or of the required limit of HSW8.2 for the rational field. In particular the full infinite distribution HSW3 was constructed directly and proved convergent; it was not obtained by an unproved interchange of the limits \(\Lambda\to\infty\), number of places and number of zero constraints.

The exact defect that any identification with that harmonic limit must retain is already HSW4.3. On the explicit original zero class HSW5 it is HSW6.4, with the strictly positive lower bound HSW6.3 for each off-critical pair. This is a computed equality of distributions and test maps; it does not promote the characteristic-zero cutoff passage into an established result.

## HSW9. Scope of the result

The calculation supplies three exact global relations on the entire original test space:

1. The original arithmetic defect \(\Theta_{\rm off}\) and the harmonic resonance sum differ by the explicit paired kernel HSW4.2 and the full prime–Gamma–endpoint formula HSW4.3.
2. The single constructive summation-image test \(b_\dagger=\Sigma h_\dagger\) detects the failure of harmonic sweeping to descend to the original quotient: its original zero trace is zero, while every off-critical pair contributes the strictly positive quantity bounded below in HSW6.3. Its complete harmonic value is bounded above and below by fixed positive constants times \(S_{\rm off}\), as proved in HSW6A.3, and equals the exact sum of the canonical original-primary representative norms in HSW6B.7.
3. The full harmonic density has a meromorphic continuation whose poles and residues recover every original off-critical zero and its multiplicity. Thus the harmonic operation does not merely forget those zeros; it carries them in an exact different global observable.

All three use the original \(\zeta\), its prime repetitions, Gamma terms, endpoints, finite trivial-zero contributions, complete multiplicities and actual source summation image. They neither assert that an off-critical zero exists nor prove that the characteristic-zero cutoff identity holds. No numerical purity or positivity premise has been assigned to primitive \(\tau\), and no established support label or coefficient factor was removed.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
