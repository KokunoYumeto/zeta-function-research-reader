# Finite Gamma evaluation and the complete power-band metric

This independent derivation checks HK1–HK11 and JB1–JB8 of the supplied *Effective native cutoff geometry*. It proves their finite scalar bounds and gives the stronger constants 83 and 111 below. It also proves the simultaneous bound for every vector of the prescribed coefficient band. The weight, both real half-lines, its complete mass, every coefficient row, and every affine minimum remain in the formulas.

The preceding programme proofs used here are [PJ1–PJ44, original Gamma and jet maps](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/POWER_JET_PROOF.md), [EL1–EL10, exact equilibrium constants](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/ELLIPTIC_LOG_MOMENT_PROOF.md), and [EIQ1–EIQ19, the density and the Euler inequality on the complete positive half-line](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9104d852c6bc5b79e6fc4588c403128a40b7fda3/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/RETAINED_COMPLETE_PROOF_SOURCES.tex#L4384). Their complete source bodies are retained alongside this derivation. The new estimates below do not depend on a limiting zero distribution.

## 1. Original measures and explicit finite constants

For integer \(n\ge36\), retain
\[
 w(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi},\qquad
 d\sigma(y)=w(y)dy,\qquad d\nu_n=|y|^{2n}d\sigma,
 \qquad d_n=\nu_n(\mathbb R).
 \tag{EG1}
\]
The evaluation kernel \(\mathsf K_{n,M}(0,0)\) is the squared norm of evaluation at zero on all complex polynomials of degree at most \(M\), with norm from \(\nu_n\). Thus
\[
 \mathsf K_{n,M}(0,0)^{-1}
 =\min\{\|P\|_{\nu_n}^2:\deg P\le M,\ P(0)=1\}.
 \tag{EG2}
\]
Positive definiteness of every polynomial Gram matrix gives existence and uniqueness of the minimizer. The even and odd subspaces are orthogonal, so the minimizer is even and the kernels at degrees \(2h\) and \(2h+1\) agree exactly. At degree zero, \(d_n\mathsf K_{n,0}(0,0)=1\).

The complete mass is \(d_0=\sqrt{2\pi}\). Indeed the Fourier transform of \(g_a(u)=e^{au-e^u}\) is \(\Gamma(a+it)\). Plancherel and \(x=e^u\) give
\(\int|\Gamma(a+it)|^2dt/(2\pi)=2^{-2a}\Gamma(2a)\). The original coordinate is \(y=2t\); at \(a=1/4\) its factor two gives the asserted mass.

R. A. Askey and R. Roy's [DLMF 5.11.1 and its remainder statement in 5.11(ii)](https://dlmf.nist.gov/5.11#ii) imply, with \(z=1/4+iy/2\), \(y\ge1\),
\[
 \log\Gamma z=(z-1/2)\log z-z+\tfrac12\log(2\pi)+R(z),
 \qquad |R(z)|\le\frac{\sec^2(\arg z/2)}{12|z|}\le\frac1{3y}.
\]
The original equation TeX is retained; the section's error statement, which is prose on the primary site, is recorded as such in the use ledger. Taking real parts, without changing the density, gives
\[
 \log(\sqrt y e^{\pi y/2}w(y))
 =\tfrac12\log2-\tfrac14\log(1+1/(4y^2))
 +y\arctan(1/(2y))-\tfrac12+2\Re R(z).
\]
The inequalities \(x-x^3/3\le\arctan x\le x\) and \(\log(1+x)\le x\) show that this expression lies between
\(\tfrac12\log2-37/48\) and \(\tfrac12\log2+2/3\). These bounds are respectively above \(\log(1/2)\) and below \(\log3\). For \(0<y\le1\), the Gamma integral gives
\( |\Gamma(1/4+iy/2)|\le\Gamma(1/4)<4+e^{-1}<9/2\).
Using \(e^{\pi/2}<8\) and \(2\pi>6\) then gives the following full envelopes:
\[
 \tfrac12 y^{-1/2}e^{-\pi y/2}\le w(y)\quad(y\ge1),
 \qquad w(y)\le32y^{-1/2}e^{-\pi y/2}\quad(y>0).
 \tag{EG3}
\]

Put \(\theta=\pi/2\), \(\alpha=2n-1/2\), and
\(d\lambda_n=|y|^\alpha e^{-\theta|y|}dy\). We give the finite polynomial argument at zero, where the lower pointwise envelope cannot be used. The Laguerre derivative identity, from the finite coefficient formula and parameter relation, is
\[
 (L_j^{(\alpha)})'=-\sum_{i<j}L_i^{(\alpha)}.
\]
In the orthonormal basis on the positive half-line its derivative matrix has entries
\[
 D_{ij}=-\theta\prod_{r=i+1}^j\sqrt{\frac r{r+\alpha}},\qquad i<j.
\]
For degree at most \(2n+2\), every ratio is at most
\((2n+2)/(4n+3/2)\le12/19<16/25\). Each absolute row and column sum is less than \(4\theta\), hence \(\|P'\|\le4\theta\|P\|\).
Integrating the derivatives of \(|P|^2y^\alpha e^{-\theta y}\) and \(|P|^2y^{\alpha-1}e^{-\theta y}\), and writing \(B_j=\int|P|^2y^{\alpha-j}e^{-\theta y}/\|P\|^2\), gives
\[
 \alpha B_1\le9\theta,\qquad
 (\alpha-1)B_2\le\theta B_1+8\theta\sqrt{B_2}.
\]
Solving this quadratic yields \(\|P/y\|\le8\theta\|P\|/n\). Boundary terms vanish since \(\alpha>1\). Apply this to \(P(y)\) and \(P(-y)\), and add their squared norms. Thus the \(\lambda_n\) mass of \(|P|^2\) on \(|y|<1\) is at most \(64\theta^2/n^2<1/4\) of its full norm for \(n\ge36\). Applying (EG3) on the remaining part proves
\[
 \tfrac14\|P\|_{\lambda_n}^2\le\|P\|_{\nu_n}^2
 \le32\|P\|_{\lambda_n}^2,\qquad \deg P\le2n+2.
 \tag{EG4}
\]
The factor \(1/4\) is weaker than the available \(3/8\); using it maintains the supplied constants.

The full auxiliary mass is \(2\Gamma(2n+1/2)(2/\pi)^{2n+1/2}\). Its logarithm, minus \(2n\log n+\eta_0n\), where \(\eta_0=2\log(4/\pi)-2\), is
\[
 \log4+2n\log(1+1/(4n))-\tfrac12+R(2n+1/2).
\]
For positive real argument, \(0<R(x)<1/(12x)\). Bounds \(u-u^2/2\le\log(1+u)\le u\) therefore enclose the last three terms between \(-1/(16n)\) and \(1/(24n)\). Apply (EG4) to the constant polynomial:
\[
 -\frac1{16n}\le r_d(n):=\log d_n-[2n\log n+\eta_0n]
 \le\log128+\frac1{24n}<5.
 \tag{EG5}
\]

The same finite Laguerre expression gives its complete three-term multiplication matrix. Its row and column sums, including the final raising row, are at most \(20n/\theta\) through source degree \(2n+1\). Transfer this bound with (EG4), and use the already proved inverse-moment inequality for the lower bound. With
\[
 \kappa=\sqrt{128},\qquad c=(4\pi\kappa)^{-1},\qquad C=40\kappa/\pi,
\]
one obtains
\[
 cn\|P\|_{\nu_n}\le\|yP\|_{\nu_n}\le Cn\|P\|_{\nu_n},
 \qquad \deg P\le2n+1.
 \tag{EG6}
\]
For the lower estimate use \(\|P\|^2=\langle P/y,yP\rangle\) and Cauchy–Schwarz; \(P/y\) is an integrable rational function in this identity.

## 2. Exact evaluation minimum and the equilibrium profile

Let \(M=2h\ge2\), \(n\ge40\), and \(t=2h/n\le3/2\). For the original variable \(x=y^2/n^2\), write the even admissible polynomial as \(P(y)=R(x)\). The map is a bijection between \(R(0)=1,\deg R\le h\) and the even fibre in (EG2), and
\[
 \|P\|_{\nu_n}^2
 =n^{2n+1}\int_0^\infty x^{n-1/2}w(n\sqrt x)|R(x)|^2dx.
 \tag{EG7}
\]
Both half-lines contribute to (EG7). There is no leading-coefficient condition on \(R\).

Use the proved EIQ equilibrium for the exact potential
\(V_t(x)=(\pi\sqrt x-2\log x)/t\). Write its support as \([a,b]=[u^2,v^2]\), and put \(p=uv\), \(w_0=(u+v)/2\), \(c_0=(v^2-u^2)/4\), \(W=b-a\). To avoid confusion, \(w_0\) is this endpoint average, while \(w(y)\) continues to mean the density (EG1). The endpoints obey
\[
 uK(\sqrt{1-u^2/v^2})=2,\qquad
 vE(\sqrt{1-u^2/v^2})=2(1+t).
\]
The probability density and Euler identities are
\[
 \rho_t(x)=\frac{\sqrt{(b-x)(x-a)}}{4\pi t x}
 \int_0^\infty\frac{\sqrt s\,ds}{(x+s)\sqrt{(a+s)(b+s)}},
 \quad a<x<b,
 \tag{EG8}
\]
\[
 V_t(x)-2\int\log|x-y|d\mu_t(y)\ge\lambda_t
 \quad(x>0),
\]
with equality on \([a,b]\). The retained EL calculation evaluates
\[
 \lambda_t=4+4/t-(4/t)\log w_0-2\log c_0,
 \qquad L_t=\int\log x\,d\mu_t
 =(4/t+2)\log w_0-(2/t)\log p-2.
 \tag{EG9}
\]
These statements use the actual full-domain EIQ density, whose proof obtains its Cauchy transform \((V'_t-Rh)/2\). Since \(h>0\), its Euler derivative is negative to the left of the interval and positive to the right; this verifies precisely the inequality used on both parts of the integration domain below.

Let \(F(z)=2K(\sqrt z)/\pi\), \(a_j=\binom{2j}{j}^2/16^j\), so \(F(z)=\sum a_jz^j\). The unique coordinate \(z_t\in(0,1)\) is specified by
\[
 t=4z_tF'(z_t)/F(z_t),\qquad
 J(t)=2\log F(z_t)-\tfrac t2\log z_t,
 \quad J(0)=0.
 \tag{EG10}
\]
The exact Landen map is \(\sqrt{z_t}=(v-u)/(v+u)\). Substitution into (EG9), using the two retained original Landen equation sources, proves
\[
 J(t)=\eta_0+\tfrac t2(\lambda_t+2L_t),
 \quad
 u=\frac4{\pi(1+\sqrt z)F(z)},\quad
 v=\frac4{\pi(1-\sqrt z)F(z)}.
 \tag{EG11}
\]
No limiting argument is used in this identity. It is the same \(J\) as edition025.

The weights \(a_jz^j/F(z)\) form an auxiliary probability, and differentiation gives \(d t/d\log z=4\operatorname{Var}(j)>0\). Its aspect tends to infinity as \(z\uparrow1\). Differentiating (EG10) gives \(J'(t)=-\tfrac12\log z_t>0\), \(J''(t)<0\). Coefficientwise,
\(4F'\ge F\) and \(4(1-z)F'\le F\). Thus \(z\le t(z)\le z/(1-z)\), and for \(0<t\le1\),
\[
 \frac t2(1-\log t)\le J(t)
 \le\frac{(1+t)\log(1+t)-t\log t}{2}.
 \tag{EG12}
\]
In particular \(nJ(1/n)\le1+\tfrac12\log n\). Concavity also gives \(|J(s)-J(t)|\le J(|s-t|)\).

## 3. Harmonic measure gives the finite lower minimum

The harmonic measure of \([a,b]\) at zero has density
\[
 \omega'_0(x)=\frac{uv}{\pi x\sqrt{(b-x)(x-a)}},
 \qquad g=\log\frac{u+v}{v-u}.
\]
The conformal map \(x=(a+b)/2+(b-a)(\zeta+\zeta^{-1})/4\) sends \(|\zeta|>1\) onto the interval's exterior, and the preimage of zero is \(\zeta_0=-(u+v)/(v-u)\). For \(\deg R\le h,R(0)=1\), the function \(\zeta^{-h}R(x(\zeta))\) is analytic at infinity. Poisson–Jensen, or the subharmonic mean inequality there, gives
\[
 \int\log|R(x)|d\omega_0(x)\ge-hg.
 \tag{EG13}
\]
For the degree-one polynomial \(x-s\), \(s\in[a,b]\), there is no exterior zero. Its equality case gives \(\int\log|x-s|d\omega_0=\log s-g\), including endpoints by integrable limits. Average the Euler equality first in \(x\) against \(\omega_0\), then in \(s\) against \(\mu_t\). It follows that
\(\int V_t d\omega_0+2g=\lambda_t+2L_t\).
Jensen with the positive density \(\omega'_0\) now proves for every admissible \(R\)
\[
 \int_a^b|R|^2e^{-hV_t}x^{-3/4}dx
 \ge Z_t e^{-h(\lambda_t+2L_t)},\qquad
 Z_t=\pi c_0\sqrt p\,w_0^{-5/2}.
 \tag{EG14}
\]
Here the entropy constant has been evaluated, rather than bounded by an unspecified quantity. To check it, the same conformal map gives
\(\int\log x\,d\omega_0=2\log p-2\log w_0\). Applying (EG13)'s root equality at \(a,b\) gives the endpoint logarithms \(2\log u-g\), \(2\log v-g\). Substitute these three values into \(\int\log(x^{-3/4}/\omega'_0)d\omega_0\); since \(e^{-g}=c_0/w_0^2\), the answer is \(\log Z_t\).

## 4. A trial polynomial controls the complete upper minimum

Let \(x_1,\ldots,x_h\) be the midpoint quantiles of \(\mu_t\), let \(P_h(x)=\prod_{i=1}^h(x-x_i)\), and put \(D_t=W\|\rho_t\|_\infty\). Their empirical distribution has CDF error at most \(1/(2h)\). For \(0\le x\le B\), \(B\ge2b+1\), truncate \(\log|x-y|\) below \(\log(W/h)\). As a function of \(y\in[a,b]\) its total variation is at most \(2\log(hB/W)\). Integration by parts against the CDF difference bounds the discrepancy of its average by \(h^{-1}\log(hB/W)\). Its integral excess over the untruncated logarithm is at most
\(2\|\rho_t\|_\infty\int_0^{W/h}\log((W/h)/s)ds=2D_t/h\).
Since the discrete untruncated logarithm is no larger than its truncation, these observations give
\[
 \log|P_h(x)|\le h\int\log|x-y|d\mu_t(y)
 +\log(hB/W)+2D_t.
\]
The bounded variation of \(\log y\) gives
\( |P_h(0)|^2\ge(a/b)e^{2hL_t}\). Therefore the admissible polynomial \(R=P_h/P_h(0)\), together with the full Euler inequality, has its integral over \((0,B]\) bounded by the first term of
\[
 U_t(h)=\frac ba\left[4B^{1/4}(hB/W)^2e^{4D_t}
 +2\sqrt{\frac{2t}{h}}\right].
 \tag{EG15}
\]
For the second term choose \(B\) so that
\[
 (2/t+2)\log x-\frac\pi{2t}\sqrt x\le-\lambda_t
 \quad(x\ge B).
 \tag{EG16}
\]
All roots of \(P_h\) are positive and less than \(B/2\), so \(|P_h(x)|\le x^h\) on this tail. The resulting integrand is bounded by
\((b/a)e^{-h(\lambda_t+2L_t)}x^{-3/4}e^{-h\pi\sqrt x/(2t)}\).
Its integral over \((0,\infty)\), an upper bound for the actual tail, is exactly \(2\sqrt{2t/h}\). Thus
\[
 \int_0^\infty|R|^2e^{-hV_t}x^{-3/4}dx
 \le U_t(h)e^{-h(\lambda_t+2L_t)}.
 \tag{EG17}
\]
This proof includes the original interval next to zero and the unbounded tail.

## 5. Uniform constants down to the first nonzero degree

The exact rational certificate in the companion checker verifies
\[
 \sum_{j=0}^{12}(4j-11/10)a_j(11/20)^j>3/10000,
 \quad \sum_{j=1}^{12}ja_j(11/20)^{j-1}>3/5,
\]
and
\[
 \sum_{j=0}^{10}(4j-3/2)a_j(16/25)^j>1/100,
 \quad \sum_{j=1}^{10}ja_j(16/25)^{j-1}>3/4.
\]
All omitted terms in each comparison are positive. Monotonicity of \(t(z)\) shows \(z_t<11/20\) for \(t\le11/10\), and \(z_t<16/25\) for \(t\le3/2\).

The integral formula for \(F\) gives \(1\le F(z)\le(1-z)^{-1/2}\). By (EG11), on the larger aspect interval, \(u>1/3\), \(v<20/3\), and hence
\[
 1/16<a<b<45,\quad w_0<7,\quad \sqrt p>1/4.
\]
The exact width is
\[
 W=\frac{64\sqrt z}{\pi^2(1-z)^2F(z)^2}
 \ge\frac{4\sqrt z}{1-z}\ge4\sqrt t.
 \tag{EG18}
\]
The last comparison uses \(t\le z/(1-z)\); it proves in particular the weaker supplied bound \(W\ge4\sqrt{t/3}\). Since \(c_0=W/4\), equation (EG14) gives
\(Z_t\ge\sqrt t/2048\). For example use \(c_0\ge\sqrt{t/3}\), \(\sqrt p>1/4\), \(w_0<7\), \(\pi>3\), \(\sqrt3<2\), and \(\sqrt7<3\); these give the stronger floor \(Z_t>\sqrt t/392\).

The density (EG8) gives a uniform bound without multiplying two unnecessary endpoint extremes. Specifically,
\[
 \max_{a<x<b}\frac{\sqrt{(b-x)(x-a)}}x=\frac W{2uv},
 \quad \int_0^\infty\frac{\sqrt s}{(a+s)^2}ds=\frac\pi{2u}.
\]
They yield
\[
 D_t\le\frac{W^2}{16ta\sqrt b}
 =\frac{1+\sqrt z}{\pi(1-z)^3F'(z)}=:D_*(z).
 \tag{EG19}
\]
Differentiate the positive integral for \(F'\): \(F''/F'\le3/[2(1-z)]\). Therefore \((\log D_*)'>0\). At \(z=11/20\), the previous rational lower bound for \(F'\), together with \(\sqrt z<3/4\) and \(\pi>3\), gives \(D_t<70000/6561<11\). At \(z=16/25\) it gives \(D_t<12500/729<18\).

Take \(B=2^{16}\). From (EG9), \(w_0>1/4\), \(c_0\ge\sqrt{t/3}\), and \(t\le3/2\),
\[
 t\lambda_t\le4t+4+4\log4-t\log(t/3)<20.
\]
At \(x=B\), \((2+2t)\log x-(\pi/2)\sqrt x<-20\), and its derivative is negative thereafter; \(5/x<\pi/(4\sqrt x)\) suffices. This proves (EG16) uniformly. Since \(b/a<720\), \(h=tn/2\), and \(W^2\ge16t/3\), equation (EG15) gives
\[
 U_t(h)\le5760B^{9/4}e^{4D_*}n^2,
 \quad D_*=11\text{ for }t\le11/10,
 \quad D_*=18\text{ for }t\le3/2.
 \tag{EG20}
\]
Here is an explicit check of this deliberately generous constant. The first term is at most
\(720\cdot4\cdot3t/64\, B^{9/4}e^{4D_*}n^2\le203B^{9/4}e^{4D_*}n^2\). The second term is \(2880/\sqrt n\), at most \(B^{9/4}e^{4D_*}n^2\) for \(n\ge40\). Their sum is smaller than (EG20).

Since \(n\sqrt a>1\), use the lower envelope (EG3) on the complete equilibrium interval in (EG7); use its upper envelope on the whole positive half-line. Equations (EG14) and (EG17) prove the finite sandwich
\[
 \boxed{\tfrac12 Z_t n^{2n+1/2}e^{-h(\lambda_t+2L_t)}
 \le\mathsf K_{n,2h}(0,0)^{-1}
 \le32U_t(h)n^{2n+1/2}e^{-h(\lambda_t+2L_t)}.}
 \tag{EG21}
\]

Subtract the exact profile (EG11) and insert the complete mass (EG5). For even \(M=2h\ge2\),
\[
 -\frac1{16n}-\frac12\log n-\log(32U_t(h))
 \le\log[d_n\mathsf K_{n,M}(0,0)]-nJ(t)
 \le5-\frac12\log n-\log(Z_t/2).
 \tag{EG22}
\]
In the upper bound, \(nt=2h\ge2\), so the right side is at most \(5+(23/2)\log2<13\). The negative magnitude is at most
\[
 A(D_*)+\tfrac52\log n,\qquad
 A(D_*)=\log184320+36\log2+4D_*+1/640.
\]
It dominates 13. At odd degree use exact parity and (EG12); this adds at most \(1+\frac12\log n\). The elementary certified estimates
\(\log184320<97/8\) and \(\log2<6932/10000\) imply
\[
 A(11)+1<83,\qquad A(18)+1<111.
\]
For completeness, reduce \(184320=2^{17}(45/32)\), and certify each logarithm with
\(\log x=2\sum_{j=0}^{N-1}r^{2j+1}/(2j+1)+\varepsilon_N\),
\(r=(x-1)/(x+1)\), \(0<\varepsilon_N<2r^{2N+1}/[(2N+1)(1-r^2)]\). The companion uses rational arithmetic with \(N=40\). Degree zero is exact, and degree one follows from parity directly. We have proved
\[
 \boxed{\left|\log[d_n\mathsf K_{n,M}(0,0)]-nJ(M/n)\right|
 \le83+3\log(n+2),\quad 0\le M\le\lfloor11n/10\rfloor,\ n\ge40,}
 \tag{EG23}
\]
\[
 \boxed{\left|\log[d_n\mathsf K_{n,M}(0,0)]-nJ(M/n)\right|
 \le111+3\log(n+2),\quad 0\le M\le\lfloor3n/2\rfloor,\ n\ge40.}
 \tag{EG24}
\]
Thus the incoming constants 110 and 150 both hold. The stronger bounds improve the explicit finite remainder; the profile is unchanged. In particular the actual PP28 remainder is at most \([111+3\log(n+2)]/n\), with no unevaluated zero-statistic term.

## 6. Complete coefficient jets and both low cutoffs

Now \(q\ge40\), \(1\le b\le q/10\), \(n=q-b\), and
\[
 J_{q,b}:\mathcal P_M\longrightarrow\mathbb C^b,
 \quad (J_{q,b}P)_r=q^r[y^r]P,
 \quad M=N-n\ge b-1.
\]
Let \(H_{b,N}^{\rm jet}\) denote its attained minimum metric in \(\nu_n\). Multiplication by \(y^n\) maps the entire fibre bijectively onto the original high coefficient band in the power quotient modulo \(y^q\), preserving degree \(N\) and norm exactly:
\[
 P\longmapsto y^nP,\qquad
 \|y^nP\|_\sigma=\|P\|_{\nu_n},\qquad
 [y^nP]\bmod y^q=y^n\sum_{r<b}(J_{q,b}P)_r(y/q)^r.
 \tag{EG25}
\]
This is the full coefficient map, not a map only on diagonal norms.

Set \(\alpha=2n-1/2\) and
\[
 \gamma_r=\frac{r!(\alpha+1)_r}{(\theta q)^{2r}},\quad
 R_b=(b+1)3^b,\quad
 \mathcal L=128R_b^2\max\{\max_{r\le b}\gamma_r,
 (\min_{r\le b}\gamma_r)^{-1}\}.
 \tag{EG26}
\]
The monic Laguerre basis in \(x=y/q\) has coefficient matrix
\(T_{ir}=(-1)^{r-i}\binom ri(\alpha+i+1)_{r-i}/(\theta q)^{r-i}\).
Its inverse has the same entries without the sign. Indeed in a product entry the rising factorials combine to a constant \((\alpha+i+1)_{r-i}\), and the remaining binomial sum is \((1-1)^{r-i}\). Each factor in those entries is less than 2, so both Euclidean operator norms are at most \(R_b\). The orthogonal squared norms divided by the positive half-line mass are exactly \(\gamma_r\). On the negative half-line, the coefficient map is the diagonal unitary \(a_r\mapsto(-1)^ra_r\); it obeys the same bounds. Summing both halves and using (EG4) for both the polynomial and the constant proves
\[
 \mathcal L^{-1}d_nI_b\preceq H^{\rm jet}_{b,q-1},\ H^{\rm jet}_{b,q}
 \preceq\mathcal Ld_nI_b.
 \tag{EG27}
\]
For \(N=q\), the last coefficient is freely minimized: the lower estimate survives since the full coefficient norm is no smaller than the prescribed jet norm, and the zero last coefficient is an admissible lift for the upper estimate.

## 7. Every row of the high covariance and one simultaneous right inverse

For \(j\ge1\), \(N_j=q-1+j\), \(M=j+b-1\), \(L=j-1\). Let \(p_r\) be the orthonormal polynomials for the original \(\nu_n\), and let \(v_r=J_{q,b}p_r\). The complete covariance is
\[
 \mathsf C_M=\sum_{r=0}^M v_rv_r^*=(H^{\rm jet}_{b,N_j})^{-1}.
 \tag{EG28}
\]
The equality follows by the exact minimizing section \(J^*(JJ^*)^{-1}\); its difference from any other lift is orthogonal to its range.

All nonzero roots of the used orthogonal polynomials have modulus at least \(cn\). To verify this directly, push the even measure through \(x=y^2\). Even polynomials are orthogonal for its positive pushforward \(\rho_n\), and odd polynomials have the form \(yS(y^2)\) with \(S\) orthogonal for \(x\rho_n\). Their squared nonzero roots are eigenvalues of the corresponding finite multiplication-by-\(x\) compression. The characteristic determinant and monic orthogonal polynomial satisfy the same three-term recurrence, proving this identification. Its Rayleigh quotients are \(\|yP\|^2/\|P\|^2\); (EG6) puts them between \(c^2n^2\) and \(C^2n^2\). The additional odd root at zero is retained separately. All source degrees used here are at most \(q+2b\le2n+1\).

Put \(B_0=q/(cn)\), \(D_0=\max(1,Cn/q)\), and define exactly
\[
 U=\sum_{2h<b}\binom{\lfloor(q+b)/2\rfloor}{h}^{2}B_0^{4h}
 +B_0^2\sum_{2h+1<b}\binom{\lfloor(q+b-1)/2\rfloor}{h}^{2}B_0^{4h},
\]
\[
 V=\sum_{h=0}^{\lfloor(b-1)/2\rfloor}
 \binom{\lfloor q/2\rfloor+h-1}{h}B_0^{2h},
 \qquad L_*=bV^2D_0^{2(b-1)}.
 \tag{EG29}
\]
The letter \(L_*\) here is a finite jet constant, distinct from the logarithmic moment \(L_t\).
Factor every even orthogonal polynomial as \(p(0)\prod(1-y^2/a_i^2)\). Its \(2h\)-th jet coefficient is bounded by \(|p(0)|\binom{\lfloor M/2\rfloor}{h}B_0^{2h}\). For the odd sector, \(P=yQ\) and (EG6) give
\[
 \sup_{P\ \mathrm{odd},\deg P\le M}\frac{|P'(0)|^2}{\|P\|^2}
 \le(cn)^{-2}\mathsf K_{n,M}(0,0).
\]
Apply the same paired-root estimate to its remaining coefficients and sum all row norms. It yields \(\operatorname{Tr}\mathsf C_M\le U\mathsf K_{n,M}(0,0)\), and positive semidefiniteness gives the full matrix upper bound.

For the opposite direction define
\(H_L(y)=\mathsf K_{n,L}(y,0)/\mathsf K_{n,L}(0,0)\). It has \(H_L(0)=1\), norm squared \(1/\mathsf K_{n,L}(0,0)\), and all its zeros, if any, have modulus at least \(cn\). Reproduction gives \(\langle H_L,y^{2r}\rangle=0\) for \(1\le r\le\lfloor L/2\rfloor\); its pushforward is therefore the degree-\(\lfloor L/2\rfloor\) orthogonal polynomial for \(x\rho_n\), proving that root statement by the same compression. Complete homogeneous coefficients then bound the sum of the first \(b\) coefficients of \(1/H_L(qx)\) by \(V\). For every \(a\in\mathbb C^b\) put
\[
 \mathcal R a(y)=H_L(y)\left[\frac{\sum_{r<b}a_rx^r}{H_L(qx)}\right]_{<b}\Big|_{x=y/q}.
 \tag{EG30}
\]
This is linear and \(J_{q,b}\mathcal R a=a\) exactly. Its degree is at most \(L+b-1\le M\), including \(L=0\), where \(H_L=1\). Coefficient convolution gives a coefficient-sum bound \(\sqrt b V\|a\|_2\). Repeated (EG6), with each raising degree included, gives
\(\|\mathcal R a\|^2\le L_*\|a\|_2^2/\mathsf K_{n,L}(0,0)\).
Taking the actual minimum and inverting proves
\[
 \boxed{\frac{\mathsf K_{n,L}(0,0)}{L_*}I_b
 \preceq(H^{\rm jet}_{b,N_j})^{-1}
 \preceq U\mathsf K_{n,M}(0,0)I_b,\quad1\le j\le q+1.}
 \tag{EG31}
\]
All complex cross-covariances are controlled by the trace estimate and by this simultaneous section.

## 8. Finite every-vector rate and all reference cutoffs

For \(0\le h\le q+b\), applying (EG6) successively to \(P,yP,\ldots,y^{b-1}P\), with the same weight \(\nu_n\), proves
\((cn)^{2b}\|P\|_{\nu_n}^2\le\|P\|_{\nu_q}^2\le(Cn)^{2b}\|P\|_{\nu_n}^2\).
Every degree is at most \(q+2b\le2n+1\). Apply the same inequalities to the constant polynomial and to the evaluation minimum; division is done only after both original masses are retained. Thus
\[
 |\log[d_n\mathsf K_{n,h}(0,0)]-\log[d_q\mathsf K_{q,h}(0,0)]|
 \le2b\log(C/c).
 \tag{EG32}
\]
This avoids applying (EG23) at \(n=q-b<40\); it is applied at the original \(q\ge40\).

Define the explicit error
\[
 \mathcal J=\log\mathcal L+\max(\log L_*,\log U)+2b\log(C/c)
 +83+3\log(q+2)+qJ((b+1)/q).
 \tag{EG33}
\]
Equations (EG27), (EG31), (EG32), and (EG23), with \(M\le q+b\le11q/10\), give for each eigenvalue \(\lambda\) of
\((H^{\rm jet}_{b,N_j})^{-1/2}H^{\rm jet}_{b,q-1}(H^{\rm jet}_{b,N_j})^{-1/2}\),
\[
 \boxed{|\log\lambda-qJ(j/q)|\le\mathcal J,\quad0\le j\le q+1.}
 \tag{EG34}
\]
At \(j=0\) the matrix is exactly the identity. For \(j\ge1\), use \(L=j-1\), \(M=j+b-1\), and \(|J(M/q)-J(j/q)|,|J(L/q)-J(j/q)|\le J((b+1)/q)\). The same bound holds with low metric \(H^{\rm jet}_{b,q}\) for \(j\ge1\). This states the reference range explicitly; the proof of (EG31) is not applied with \(L=-1\).

Equivalently, for every \(a\in\mathbb C^b\),
\[
 e^{-qJ(j/q)-\mathcal J}\,a^*H^{\rm jet}_{b,q-1}a
 \le a^*H^{\rm jet}_{b,N_j}a
 \le e^{-qJ(j/q)+\mathcal J}\,a^*H^{\rm jet}_{b,q-1}a.
 \tag{EG35}
\]
Comparing these two inequalities for any pair \(0\le i,j\le q+1\) gives the complete finite pair estimate: every eigenvalue of \((H^{\rm jet}_{b,N_j})^{-1/2}H^{\rm jet}_{b,N_i}(H^{\rm jet}_{b,N_j})^{-1/2}\) has logarithm within \(2\mathcal J\) of \(q[J(j/q)-J(i/q)]\). This includes either low cutoff in either order, without commuting two Hermitian forms.

Finally the displayed finite sums prove
\(\mathcal J=O(b\log(C_1q/b)+b+\log(q+2))\), for an absolute constant \(C_1\). Indeed \(\binom Nr\le(eN/r)^r\), the factors \(B_0,D_0\) are bounded independently of \(q,b\), and \(r!\ge(r/e)^r\) bounds the inverse \(\gamma_r\). The endpoint term is at most a constant times \((b+1)[1+\log(q/(b+1))]\) by (EG12). The exact finite error (EG33), rather than this order notation, is available for every allowed pair.

## Sources, scope, and reproducibility

The human references actually used are R. A. Askey and R. Roy, DLMF Chapter5, Gamma Function; T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw, DLMF Chapter18, Orthogonal Polynomials, equations [18.5.12](https://dlmf.nist.gov/18.5.E12), [18.9.13](https://dlmf.nist.gov/18.9.E13), [18.9.23](https://dlmf.nist.gov/18.9.E23); and B. C. Carlson, DLMF Chapter19, [19.8.12](https://dlmf.nist.gov/19.8.E12). The original equation TeX files were obtained and read. The retained programme EIQ/EL proofs provide the full positive equilibrium and exact logarithmic moment; the present finite harmonic-measure/quantile sandwich is independently proved in Sections3–5.

`check_effective_gamma.py` certifies the rational series comparisons and constant arithmetic, the entropy and density identities, and exact full-covariance/right-inverse examples. It uses no native-period surrogate and asserts no individual arithmetic-current sign. The physical action, the original arithmetic roots, and the full invariant constraints enter through the unchanged original source maps when the root task receives (EG25) and (EG34)–(EG35).
