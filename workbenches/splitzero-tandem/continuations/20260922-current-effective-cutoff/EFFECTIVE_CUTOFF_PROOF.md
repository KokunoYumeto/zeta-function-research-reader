---
title: "Effective native cutoff geometry"
subtitle: "A finite Gamma bound, quantitative original-metric transport, and mesoscopic source laws"
author: "Research continuation — calculations and verification prepared in this session"
date: "22 September 2026"
---

# Status, original objects, and principal results

The repository advanced during this calculation. Edition SZ-20260922-025, read at commit `76473e0564b32f7566e191829bf67477c8950f0b`, now contains the complete original cutoff profile, its fixed subquotient consequences, elliptic derivatives and endpoint correction, and phase/heat receivers. Those conclusions are not presented here as new. This continuation strengthens their scalar and localization remainders to explicit finite bounds, obtains an effective single-sequence native rate, and uses that rate to evaluate shrinking-window source responses and their negative mesoscopic curvature. It also gives a separately certified integrated profile. The full derivations are retained so that the quantitative upgrade can be audited rather than inferred from a summary.

The decisive new scalar estimate is (CU7a): it replaces the unevaluated zero-statistic remainder in the newer PP24–PP28 calculation by `150 + 3 log(n+2)` on its entire ratio range. The sharper constant 110 applies on the subrange used in this proof's jet reduction. Section 8 records the exact integration with the newly arrived edition and proves the additional shrinking-window results.

The baseline repository proof is `KokunoYumeto/zeta-function-research-reader`, commit `2b1445b21cc2fcd7e8b7ff34c6aea7139fb6afb5`. Its `COMBINED_KERNEL_AND_RECEIVERS.md` (CK1–19), complete `POWER_JET_PROOF.md` (PJ1–70), and `ELLIPTIC_LOG_MOMENT_PROOF.md` (EL1–14) are inherited inputs. The independent EIQ1–33 equilibrium proof was also read from the original uploaded cumulative source, lines 4364–4812; that exact byte range is included. A failed direct fetch of the much larger GitHub source bank is not counted as reading it. The original current phases are not evaluated by this continuation.

Retain
\[
 k\equiv1\pmod4,\quad q=(k+1)^2,\quad m=8k-16,
 \quad 0<\delta<1/2,\quad\gamma>2,
\]
\[
 Q_k(y)=\prod_{a,b=0}^k
 [y-(2b-k)\gamma+i(2a-k)\delta],
 \quad E_k=\mathbb C[y]/Q_k,\quad M[p]=[yp].
 \tag{CU1}
\]
The original physical action is \(kI/2+iM\). The full observation is \(\Lambda_k\), its kernel is \(K_k\), and \(I_K\) is its fixed coefficient frame. At original polynomial cutoff \(N\), the attained metric is \(G_N\), including the complete native measure and all relation polynomials. Put
\[
 H_{K,N}=I_K^*G_NI_K,\quad
 Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
 L_N=G_N^{-1}\Lambda^*Q_{B,N}.
\]
A matrix star is conjugate transpose in the displayed coefficient frames. Every physical adjoint uses its specified metric. The full source comparison, for every polynomial through degree \(2q\), is
\[
 \ell_k\|P\|_\sigma^2\le\|P\|_{\mu_k}^2\le u_k\|P\|_\sigma^2,
 \quad \kappa_k=u_k/\ell_k,\quad \log\kappa_k=o(q),
\]
\[
 d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy,
 \qquad \sigma(\mathbb R)=\sqrt{2\pi}.
 \tag{CU2}
\]
For quantitative orders one may use the actual stronger finite provider \(\log\kappa_k=O_h(k+\log q)\). The proof states explicitly where even this finite source comparison is needed.

Index the whole original window by
\[
 N_j=q-1+j,\qquad 0\le j\le q+1,\qquad t_j=j/q.
 \tag{CU3}
\]
The original four signs are at \(j=0,1,q,q+1\), not at a newly chosen window. We will use the full interval \(0\le t\le1\) for limits, and a harmless extension to \(11/10\) to include all finite band shifts.

Define
\[
 F(z)=\frac2\pi K(\sqrt z)
 =\sum_{n=0}^{\infty}\frac{\binom{2n}{n}^2}{16^n}z^n,
 \qquad 0\le z<1.
\]
For \(t>0\), let \(z_t\) be the unique solution of
\[
 t=4z_tF'(z_t)/F(z_t).
\]
The profile is
\[
 \boxed{\beta(t)=2\log F(z_t)-\frac t2\log z_t,\qquad\beta(0)=0.}
 \tag{CU4}
\]
At the original endpoint, \(2\beta(1)=C_\partial\), as proved by the retained EL dictionary.

The principal native result is
\[
 \boxed{\sup_{0\le j\le q+1}
 \left|\frac{\log\det H_{K,N_0}-\log\det H_{K,N_j}}{mq}
       -\beta(t_j)\right|\longrightarrow0.}
 \tag{CU5}
\]
A stronger result below controls the mean absolute displacement of **every** logarithmic relative eigenvalue, and applies to fixed coefficient subquotients. It supplies an explicit finite error and an eventual rate
\[
 O_{h,A}\!\left(
 \frac{\log\log(k+e)}{\sqrt{\log(k+e)}}
 +\frac{e^{2\sqrt{\log(k+e)}}}{k}
 +\frac{\log\kappa_k}{q}\right).
 \tag{CU6}
\]
The rate is asserted only once the displayed finite guards hold; the slowly shrinking band used to prove it has a very large sufficient threshold. The scalar Gamma theorem itself has the much sharper uniform bound
\[
 \boxed{\left|\log[d_q\mathsf K_{q,M}(0,0)]-q\beta(M/q)\right|
 \le110+3\log(q+2),}
 \quad q\ge40,\quad 0\le M\le\lfloor11q/10\rfloor,
 \tag{CU7}
\]
where \(d_q=\int |y|^{2q}d\sigma\), and \(\mathsf K_{q,M}\) is the original evaluation kernel in that full measure. The large numerical constant is a deliberately uniform simplification; the parameter-dependent finite sandwich in (HK10) is substantially sharper.
The same proof also yields the full range used by the new PP28:
\[
 \boxed{\left|\log[d_q\mathsf K_{q,M}(0,0)]-q\beta(M/q)\right|
 \le150+3\log(q+2),\quad
 0\le M\le\lfloor3q/2\rfloor,\quad q\ge40.}
 \tag{CU7a}
\]
The cutoff symbols in this scalar theorem are integers, not physical arithmetic indices. Application to the original source is through the maps proved in Sections 3–4.

# 1. The exact scalar profile

## 1.1 Equilibrium dictionary, with every scale retained

For \(t>0\), use the retained equilibrium probability for
\[
 V_t(x)=\frac{\pi\sqrt x-2\log x}{t},\qquad x>0.
\]
Its parameters in EIQ and EL are exactly \((\alpha,\beta_{\rm pot})=(2/t,\pi/t)\). Write its support as \([a_t,b_t]=[u_t^2,v_t^2]\), and set
\[
 r_t=u_t/v_t,\quad \varkappa_t=\sqrt{1-r_t^2},\quad
 w_t=(u_t+v_t)/2,\quad p_t=u_tv_t,\quad c_t=(v_t^2-u_t^2)/4.
\]
The endpoints solve
\[
 u_tK(\varkappa_t)=2,\qquad
 v_tE(\varkappa_t)=2(1+t).
 \tag{PR1}
\]
The exact EIQ density, obtained from its positive Cauchy-transform representation, is
\[
 \rho_t(x)=\frac{\sqrt{(b_t-x)(x-a_t)}}{4\pi t x}
 \int_0^\infty
 \frac{\sqrt s\,ds}{(x+s)\sqrt{(a_t+s)(b_t+s)}}.
 \tag{PR2}
\]
It is zero outside the support, positive inside it, and has mass one. EIQ proves the full Euler inequality, on all of \((0,\infty)\):
\[
 V_t(x)-2\int\log|x-y|\,d\mu_t(y)\ge\lambda_t,
\]
with equality precisely on the support. EL gives
\[
 \lambda_t=4+4/t-(4/t)\log w_t-2\log c_t,
\]
\[
 L_t:=\int\log x\,d\mu_t
 =(4/t+2)\log w_t-(2/t)\log p_t-2.
 \tag{PR3}
\]
Therefore
\[
 \boxed{\beta(t)=2\log(4/\pi)-2+\frac t2(\lambda_t+2L_t)}
\]
\[
 =2\log(4/\pi)+2(1+t)\log w_t-2\log p_t-t\log c_t.
 \tag{PR4}
\]
This exact parameter dictionary, not an extrapolation from \(t=1\), will enter the norm minimum.

## 1.2 Hypergeometric coordinate and strict concavity

Put \(z=((1-r_t)/(1+r_t))^2\). The Landen identities (DLMF 19.8.12), or their power-series verification in the defining elliptic integrals, give
\[
 K(\varkappa_t)=(1+\sqrt z)K(\sqrt z),
\]
\[
 E(\varkappa_t)=\frac{2E(\sqrt z)-(1-z)K(\sqrt z)}{1+\sqrt z}.
\]
Substitution into \(E(\varkappa_t)/(r_tK(\varkappa_t))=1+t\) gives
\[
 t=2\left[\frac{E(\sqrt z)}{(1-z)K(\sqrt z)}-1\right]
 =4zF'(z)/F(z).
 \tag{PR5}
\]
The last equality follows by differentiating the defining integral. Substitution into (PR4) gives exactly (CU4).

Give \(n\ge0\) the probability weight
\(a_nz^n/F(z)\), \(a_n=\binom{2n}{n}^2/16^n\). Then \(t=4\mathbb E_z n\) and
\[
 \frac{dt}{d\log z}=4\operatorname{Var}_z(n)>0.
\]
The aspect runs from zero to infinity, because \(F(z)\) diverges logarithmically while \(F'(z)\) diverges at order \((1-z)^{-1}\). Alternatively, the endpoint uniqueness in EIQ gives the same onto statement. Differentiating (CU4), the terms involving \(z_t'\) cancel, proving
\[
 \boxed{\beta'(t)=-\tfrac12\log z_t>0,\qquad
 \beta''(t)=-\frac1{2z_t t'(z_t)}<0.}
 \tag{PR6}
\]
Thus \(\beta\) is strictly increasing and strictly concave.

The hypergeometric differential equation
\(z(1-z)F''+(1-2z)F'-F/4=0\) gives the exact Riccati form
\[
 4z(1-z)t'(z)=4z(t+1)-(1-z)t^2.
 \tag{PR7}
\]
Equivalently,
\[
 \beta''=-\frac{2(e^{2\beta'}-1)}
 {4(t+1)-t^2(e^{2\beta'}-1)}.
\]
These are scalar equations on the explicitly defined profile; no original arithmetic eigenvalue is replaced by \(z_t\).

Coefficientwise,
\[
 4(1-z)F'(z)=\sum_{n\ge0}\frac{a_n}{n+1}z^n\le F(z),
 \qquad 4F'(z)\ge F(z).
\]
Therefore
\[
 z\le t(z)\le\frac z{1-z},\qquad
 \frac t{1+t}\le z_t\le t.
\]
For \(0<t\le1\), integrating (PR6) yields
\[
 \boxed{\frac t2(1-\log t)\le\beta(t)
 \le\frac{(1+t)\log(1+t)-t\log t}{2}.}
 \tag{PR8}
\]
In particular the error after the first term is between zero and \(t^2/4\). The exact local series begins
\[
 \beta(t)=\frac t2(1-\log t)+\frac7{32}t^2
 -\frac{43}{768}t^3+\frac{497}{24576}t^4
 -\frac{1381}{163840}t^5+O(t^6).
 \tag{PR9}
\]

## 1.3 Certified scalar values and a new integrated value

The integer-interval calculation in `code/certify_profile.py` uses no floating point. All displayed decimals in this table are outward rational intervals.

\needspace{9\baselineskip}

| Quantity | Lower endpoint | Upper endpoint |
|:--|--:|--:|
| \(\beta(1/4)\) | 0.31115542601070381606034394785043 | 0.31115542601070381606034394785044 |
| \(\beta(1/2)\) | 0.47202413882565744657617131470452 | 0.47202413882565744657617131470453 |
| \(\beta(3/4)\) | 0.58720530893796571051071192663424 | 0.58720530893796571051071192663425 |
| \(\beta(1)\) | 0.67714099391264606644199488757692 | 0.67714099391264606644199488757693 |
| \(\beta'(1)\) | 0.32298207997956527877403877885087 | 0.32298207997956527877403877885088 |

The full data additionally include aspects \(1/100\), \(1/10\), \(11/10\), and \(3/2\). The endpoint agrees with the independently retained interval for \(C_\partial/2\).

The integrated profile has the exact one-dimensional representation
\[
 \boxed{\int_0^1\beta(t)\,dt
 =\beta(1)+\frac14\log z_1
 -\frac14\int_0^{z_1}\frac{t(z)^2}{z}\,dz.}
 \tag{PR10}
\]
Integrate \(d\beta=-\frac12\log z\,dt\) by parts twice. The terms at zero vanish because \(t(z)=z+O(z^2)\).

On \(|z|=R<1\), the integral for \(F\) has
\(\Re F(z)\ge[2(1+R)]^{-1/2}\), while
\(|F'(z)|\le[2(1-R)^{3/2}]^{-1}\). Consequently
\[
 |t(z)|^2\le\frac{8R^2(1+R)}{(1-R)^3}.
\]
At \(R=4/5\) this is \(1152\). If the Taylor integral in (PR10) is retained through degree \(L\), its omitted absolute contribution before the factor \(1/4\) is at most
\[
 \frac{1152}{L+1}\frac{(z_1/R)^{L+1}}{1-z_1/R}.
 \tag{PR11}
\]
The calculation uses exact rational division for the coefficients of \(4zF'/F\), degree \(L=224\), and this symmetric tail. It proves
\[
 \boxed{0.436944268921521509525169751272
 <\int_0^1\beta(t)dt
 <0.436944268921521509525169751273.}
 \tag{PR12}
\]
Also,
\[
 \boxed{0.697083979657197470191113447667
 <\frac{\beta(1/2)}{\beta(1)}
 <0.697083979657197470191113447668.}
 \tag{PR13}
\]
These certify the universal scalar profile and its integrals, not the finite native convergence error.

# 2. Effective evaluation of the full Gamma kernel

## 2.1 Explicit Gamma envelopes and mass

Write \(w(y)=|\Gamma(1/4+iy/2)|^2/(2\pi)\). We use the concrete constants
\[
 \boxed{\tfrac12 y^{-1/2}e^{-\pi y/2}\le w(y)\quad(y\ge1),
 \qquad w(y)\le32y^{-1/2}e^{-\pi y/2}\quad(y>0).}
 \tag{HK1}
\]
Here is a proof rather than a qualitative use of Stirling's formula. For \(z=1/4+iy/2\), \(y\ge1\), the first log-Gamma remainder has magnitude at most
\(\sec^2(\arg z/2)/(12|z|)\le1/(3y)\) (DLMF 5.11(ii)). Taking real parts gives
\[
 \log(\sqrt y e^{\pi y/2}w(y))
 =\tfrac12\log2-\tfrac14\log(1+1/(4y^2))
 +y\arctan(1/(2y))-\tfrac12+2\Re R(z).
\]
It lies between \(\tfrac12\log2-37/48\) and \(\tfrac12\log2+2/3\). This is strictly between \(\log(1/2)\) and \(\log3\). For \(0<y\le1\), the Gamma integral gives
\(|\Gamma(1/4+iy/2)|\le\Gamma(1/4)<9/2\); using \(e^{\pi/2}<8\), \(2\pi>6\), yields the stated upper constant 32.

Put \(d\lambda_n=|y|^{2n-1/2}e^{-\pi|y|/2}dy\). The elementary Laguerre derivative bound used in PJ3 implies, on every polynomial of degree at most \(2n+2\), for \(n\ge36\),
\[
 \tfrac14\|P\|_{\lambda_n}^2
 \le\|P\|_{\nu_n}^2\le32\|P\|_{\lambda_n}^2,
 \qquad d\nu_n=|y|^{2n}d\sigma.
 \tag{HK2}
\]
For clarity, the lower half follows by excluding \(|y|<1\) in (HK1): integration by parts in the Laguerre weight gives
\(\|P/y\|_{\lambda_n}\le[8(\pi/2)/n]\|P\|_{\lambda_n}\). Consequently the mass on \( |y|<1\) is at most \(64(\pi/2)^2/n^2\le1/4\) of the full squared norm. The rational expression \(P/y\) is integrable in this weight and is not asserted to be a polynomial. The full PJ3 proof, including its highest allowed degree and both half-lines, is retained as an input to (HK2).

Its mass comparison is particularly explicit. With
\[d_n=\nu_n(\mathbb R),\qquad \eta_0=2\log(4/\pi)-2,\]
Stirling's real remainder for \(\Gamma(2n+1/2)\), combined with (HK2), gives
\[
 \boxed{-\frac1{16n}\le
 \log d_n-[2n\log n+\eta_0n]
 \le\log128+\frac1{24n}<5.}
 \tag{HK3}
\]
Indeed the full mass of \(\lambda_n\) is
\(2\Gamma(2n+1/2)(2/\pi)^{2n+1/2}\); its own remainder is between
\(\log4-1/(16n)\) and \(\log4+1/(24n)\). The factors 2 and the Gamma mass have not been dropped.

## 2.2 Exact change of variable for evaluation, not a monic minimum

Let \(M=2h\ge2\), \(t=M/q\). Symmetry makes the minimum representative of evaluation at zero even. Write it as \(P(y)=R(y^2/q^2)\), where \(\deg R\le h\), \(R(0)=1\). Then
\[
 \boxed{\|P\|_{\nu_q}^2
 =q^{2q+1}\int_0^\infty
 x^{q-1/2}w(q\sqrt x)|R(x)|^2dx.}
 \tag{HK4}
\]
There is no monic factor \(q^{2M}\) in this map: it is the evaluation minimum. The two half-lines contribute exactly the density in (HK4).

The comparison integrand is
\[
 q^{2q+1/2}e^{-hV_t(x)}x^{-3/4}|R(x)|^2.
\]
The upper Gamma bound is global. The lower Gamma bound holds on \([a_t,b_t]\) when \(q u_t\ge1\).

## 2.3 Harmonic-measure lower bound, including its entropy constant

Let \(\omega_0\) be harmonic measure of \([a,b]\) at the exterior point 0:
\[
 d\omega_0(x)=\frac{\sqrt{ab}}{\pi x\sqrt{(b-x)(x-a)}}dx,
 \qquad a=u^2,\ b=v^2.
\]
Put \(g=\log[(u+v)/(v-u)]\). For every polynomial \(R\) of degree at most \(h\), with \(R(0)=1\),
\[
 \int\log|R|\,d\omega_0\ge-hg.
 \tag{HK5}
\]
To prove this, map \(|\zeta|>1\) onto the slit exterior by
\(x=(a+b)/2+(b-a)(\zeta+\zeta^{-1})/4\). The preimage of zero is
\(\zeta_0=-(u+v)/(v-u)\). The analytic function
\(\zeta^{-h}R(x(\zeta))\) is bounded at infinity. Poisson–Jensen at \(\zeta_0\) gives (HK5). For a root \(s\in[a,b]\), the same function for \(R(x)=x-s\) has no zero in the exterior, so equality gives
\(\int\log|x-s|d\omega_0=\log s-g\). Boundary zeros are handled by their integrable logarithmic limits.

Integrating the original Euler equality against \(\omega_0\) therefore gives
\(\int V_t d\omega_0+2g=\lambda_t+2L_t\). Jensen's inequality on the same complete interval now proves
\[
 \int_a^b |R|^2e^{-hV_t}x^{-3/4}dx
 \ge Z_t e^{-h(\lambda_t+2L_t)},
\]
where the entropy constant is exactly
\[
 \boxed{Z_t=\exp\int\log\frac{x^{-3/4}}{\omega_0'(x)}d\omega_0
 =\pi c_t\sqrt{p_t}\,w_t^{-5/2}.}
 \tag{HK6}
\]
For verification,
\(\int\log x\,d\omega_0=2\log p_t-2\log w_t\), and the two endpoint logarithms are \(2\log u_t-g\), \(2\log v_t-g\). Substitution in the density of \(\omega_0\) gives (HK6).

## 2.4 Complete quantile trial upper bound

Let \(W_t=b_t-a_t\), \(D_t=W_t\|\rho_t\|_\infty\), and let \(x_1,\ldots,x_h\) be the midpoint quantiles of the actual equilibrium probability. Put
\(P_h(x)=\prod_i(x-x_i)\) and use the admissible trial \(R=P_h/P_h(0)\).

Its empirical CDF differs from \(\mu_t\)'s by at most \(1/(2h)\). Truncate the logarithm at distance \(W_t/h\), not at a fixed absolute distance. On \(0\le x\le B_*\), with \(B_*\ge2b_t+1\), the truncated logarithm has variation at most \(2\log(hB_*/W_t)\). The difference between its continuous truncated and untruncated integral is at most \(2D_t/h\). Consequently
\[
 \log|P_h(x)|\le h\int\log|x-y|d\mu_t(y)
 +\log(hB_*/W_t)+2D_t.
\]
Also \(|P_h(0)|^2\ge(a_t/b_t)e^{2hL_t}\), by the monotone variation of \(\log x\) on the support.

Choose \(B_*\) so that, for all \(x\ge B_*\),
\[
 (2/t+2)\log x-\frac{\pi}{2t}\sqrt x\le-\lambda_t.
\]
The full Euler inequality gives the integral bound on \((0,B_*]\); on the remaining tail use \(|P_h(x)|\le x^h\). The result, including both regions, is
\[
 \int_0^\infty |R|^2e^{-hV_t}x^{-3/4}dx
 \le U_t(h)e^{-h(\lambda_t+2L_t)},
\]
\[
 \boxed{U_t(h)=\frac{b_t}{a_t}
 \left[4B_*^{1/4}(hB_*/W_t)^2e^{4D_t}
       +2\sqrt{\frac{2\pi}{h(\pi/t)}}\right].}
 \tag{HK7}
\]
This is a linear-space evaluation bound; no zero distribution of the unknown orthogonal polynomial was used.

## 2.5 Uniform finite remainder, including the small-aspect boundary

On \(0<t\le11/10\), the positive coefficient series gives the sharper uniform bound
\[
 z_t<11/20.
\]
Indeed the exact rational inequalities
\[
 -\frac{11}{10}+\sum_{j=1}^{12}(4j-11/10)a_j(11/20)^j
 >\frac3{10000},\qquad
 \sum_{j=1}^{12}ja_j(11/20)^{j-1}>\frac35
\]
prove respectively \(t(11/20)>11/10\) and \(F'(11/20)>3/5\); every omitted coefficient is positive. The endpoint formulas give the conservative bounds
\[
 \frac1{16}<a_t<b_t<45,\qquad
 4\sqrt{t/3}\le W_t\le45\sqrt t.
\]
The density bound has a substantially smaller uniform constant than these separate endpoint bounds suggest. The elementary maximum
\[
 \max_{a<x<b}\frac{\sqrt{(b-x)(x-a)}}x
 =\frac{b-a}{2\sqrt{ab}}
\]
is attained at \(x=2ab/(a+b)\), as direct differentiation verifies. Also
\(\int_0^\infty s^{1/2}(a+s)^{-2}ds=\pi/(2\sqrt a)\).
Applying both estimates inside the complete density (PR2) gives
\[
 D_t\le\frac{W_t^2}{16t a_t\sqrt{b_t}}
 =\frac{1+\sqrt z}{\pi(1-z)^3F'(z)}
 =:D_{\rm bd}(z),\qquad z=z_t.
\]
For the last identity, the exact endpoint formulas are
\[
 u_t=\frac4{\pi(1+\sqrt z)F(z)},\qquad
 v_t=\frac4{\pi(1-\sqrt z)F(z)},\qquad t=4zF'/F.
\]
Differentiating the positive integral for \(F'\) shows
\(F''/F'\le3/[2(1-z)]\). Therefore
\[
 \frac d{dz}\log D_{\rm bd}(z)
 =\frac1{2\sqrt z(1+\sqrt z)}+\frac3{1-z}-\frac{F''}{F'}>0.
\]
At \(z=11/20\), use \(\sqrt z<3/4\), \(\pi>3\), and the displayed rational lower bound for \(F'\). It follows that
\[
 \boxed{D_t<\frac{70000}{6561}<11,\qquad
 Z_t\ge\sqrt t/2048.}
 \tag{HK8}
\]

One uniform choice is \(B_*=2^{16}\). Indeed \(t\lambda_t\le20\) by (PR3) and the endpoint bounds, while
\((2+2t)\log x-(\pi/2)\sqrt x<-20\) at \(x=2^{16}\) and decreases thereafter. With \(h=tq/2\), (HK7) yields
\[
 U_t(h)\le5760 B_*^{9/4}e^{44}q^2.
 \tag{HK9}
\]
For \(q\ge40\), \(q\sqrt{a_t}>1\), so the Gamma lower bound applies.

Combining (HK1), (HK4), (HK6), and (HK7) gives the finite sandwich
\[
 \boxed{\frac12 Z_tq^{2q+1/2}e^{-h(\lambda_t+2L_t)}
 \le\mathsf K_{q,2h}(0,0)^{-1}
 \le32U_t(h)q^{2q+1/2}e^{-h(\lambda_t+2L_t)}.}
 \tag{HK10}
\]
This is the primary finite estimate. It is valid for arbitrary fixed positive aspect when the explicit lower-envelope guard and tail choice hold.

For \(0<t\le11/10\), (HK3), (HK8)–(HK10), and (PR4) prove (CU7) for even \(M\). For odd \(M\), parity gives exactly
\(\mathsf K_{q,M}(0,0)=\mathsf K_{q,M-1}(0,0)\). Concavity and (PR8) give
\[
 q[\beta(M/q)-\beta((M-1)/q)]
 \le q\beta(1/q)\le1+\tfrac12\log q.
\]
The even error is at most a fixed constant plus \((5/2)\log q\); the displayed constant 110 covers all fixed terms, leaving (CU7). At \(M=0\), \(d_q\mathsf K_{q,0}(0,0)=1\) exactly.

To obtain the larger range in (CU7a), use \(0<t\le3/2\). At \(z=16/25\), the first ten nonconstant coefficients of \(4zF'-(3/2)F\), including its constant term \(-3/2\), exceed \(1/100\); the first ten coefficients of \(F'\) exceed \(3/4\). All omitted coefficients are positive. Hence \(z_t<16/25\). The same monotonic density expression gives
\[
 D_t<\frac{9/5}{3(9/25)^3(3/4)}
 =\frac{12500}{729}<18.
\]
The bounds \(1/16<a_t<b_t<45\), \(W_t\ge4\sqrt{t/3}\), and \(Z_t\ge\sqrt t/2048\) persist. These can be checked from the same elementary endpoints: $1\le F(z)\le(1-z)^{-1/2}\le5/3$ and $z\le16/25$ give $u>1/3$ and $v<20/3$. Also
\[
 W_t=\frac{64\sqrt z}{\pi^2(1-z)^2F(z)^2}
 \ge\frac{4\sqrt z}{1-z}\ge4\sqrt t,
\]
since $t\le z/(1-z)$. The weaker width displayed above is therefore valid. In (HK6), use $c_t\ge\sqrt{t/3}$, $\sqrt{p_t}>1/4$, and $w_t<7$ to obtain the stated entropy floor. Finally
\[
 t\lambda_t\le4t+4+4\log4-t\log(t/3)<20
 \quad(0<t\le3/2),
\]
using $-t\log(t/3)\le3/\mathrm e$. The upper width may be replaced by \(60\sqrt t\), which does not worsen the quantile error because its denominator uses the lower width bound. Also \(t\lambda_t\le20\) and the same \(B_*=2^{16}\) remain valid. Thus (HK9) holds with \(e^{72}\) in place of \(e^{44}\). The even logarithmic remainder is bounded by
\(72+9+36+7/2+1+(5/2)\log q\); the remaining odd-degree shift costs at most \(1+(1/2)\log q\). The constant 150 covers these terms for every \(q\ge40\), proving (CU7a).

This proves a uniform \(O(\log q)\) remainder without consuming the monic zero-statistic limit in PJ or PP. The inherited equilibrium Euler theorem and its exact elliptic dictionary remain required. For the newer paper's notation \(F_n(M)=\log[d_n\mathsf K_{n,M}(0,0)]\), its exact PP28 remainder now satisfies
\[
 \boxed{\epsilon_n^G
 =\max_{0\le M\le\lfloor3n/2\rfloor}
 |F_n(M)/n-J(M/n)|
 \le\frac{150+3\log(n+2)}{n}.}
 \tag{HK11}
\]
Here its \(J\) is precisely our \(\beta\), by EP8 and (CU4); no variable or source metric is changed.

# 3. Every vector in a growing power band

This section makes the band error explicit. Its constants can also be replaced by the sharper finite PJ constants without changing any map.

Let \(q\ge40\), \(1\le b\le q/10\), \(n=q-b\). In this section \(b\) is an integer band width, not an equilibrium endpoint. The map
\[
 J_{q,b}P=(q^j[y^j]P)_{j=0}^{b-1}
\]
defines the full attained jet metric \(H^{\rm jet}_{b,N}\) on \(\mathcal P_{N-n}\) in \(d\nu_n\). Multiplication by \(y^n\) identifies its full affine fibres with the high coefficient band modulo \(y^q\), with no change of source degree.

The explicit constants in the multiplication bound PJ16 may now be chosen as
\[
 \kappa_\Gamma=\sqrt{128},\qquad
 c_\Gamma=(4\pi\kappa_\Gamma)^{-1},\qquad
 C_\Gamma=40\kappa_\Gamma/\pi.
 \tag{JB1}
\]
They follow from (HK1)–(HK2), the complete Laguerre derivative estimate, and its final raising row. In particular,
\(c_\Gamma n\|P\|_{\nu_n}\le\|yP\|_{\nu_n}\le C_\Gamma n\|P\|_{\nu_n}\)
through the stated PJ degree guard.

## 3.1 A finite low metric constant

Put \(\alpha=2n-1/2\), \(\vartheta=\pi/2\), and
\[
 \gamma_j=\frac{j!(\alpha+1)_j}{(\vartheta q)^{2j}},\quad
 R_b=(b+1)3^b,
\]
\[
 \mathcal L_{q,b}=128R_b^2
 \max\left\{\max_{0\le j\le b}\gamma_j,
 (\min_{0\le j\le b}\gamma_j)^{-1}\right\}.
 \tag{JB2}
\]
Then at \(N=q-1\) and \(N=q\),
\[
 \mathcal L_{q,b}^{-1}d_n I_b
 \preceq H^{\rm jet}_{b,N}
 \preceq\mathcal L_{q,b}d_n I_b.
 \tag{JB3}
\]
To prove it, in the scaled coefficient variable the monic Laguerre change of basis has entries
\[
 T_{ij}=(-1)^{j-i}\binom ji
 \frac{(\alpha+i+1)_{j-i}}{(\vartheta q)^{j-i}},\qquad i\le j.
\]
Its inverse has the same entry magnitudes; multiplication of the two finite triangular matrices verifies that identity. Since each factor is at most 2 in this range, both operator norms are at most \(R_b\). The orthogonal squared norms divided by their original half-line mass are precisely \(\gamma_j\). Apply (HK2) on both half-lines; its ratio is 128. This bounds the complete degree-\(b\) coefficient Gram. A prescribed jet through degree \(b-1\) has coefficient norm at least the prescribed norm for every lift; choosing its degree-\(b-1\) representative supplies the upper minimum. This proves both cutoffs in (JB3).

## 3.2 Full high covariance, not its diagonal only

For \(j\ge1\), put
\[
 N_j=q-1+j,\quad M=j+b-1,\quad L=j-1,
 \quad B_0=\frac q{c_\Gamma n},\quad D_0=\max(1,C_\Gamma n/q).
\]
For a common bound on all \(0\le j\le q+1\), set
\[
 U_{q,b}=
 \sum_{2h<b}\binom{\lfloor(q+b)/2\rfloor}{h}^{\!2}B_0^{4h}
 +B_0^2\sum_{2h+1<b}
 \binom{\lfloor(q+b-1)/2\rfloor}{h}^{\!2}B_0^{4h},
\]
\[
 V_{q,b}=\sum_{h=0}^{\lfloor(b-1)/2\rfloor}
 \binom{\lfloor q/2\rfloor+h-1}{h}B_0^{2h},
 \qquad L_{q,b}=bV_{q,b}^2D_0^{2(b-1)}.
 \tag{JB4}
\]
Then
\[
 \boxed{\frac{\mathsf K_{n,L}(0,0)}{L_{q,b}}I_b
 \preceq(H^{\rm jet}_{b,N_j})^{-1}
 \preceq U_{q,b}\mathsf K_{n,M}(0,0)I_b.}
 \tag{JB5}
\]
All sums are finite and all entries in these constants are specified.

For the upper covariance, pair the actual orthogonal-polynomial zeros. The even \(2h\)-th divided coefficient is bounded by its constant coefficient times
\(\binom{\lfloor M/2\rfloor}{h}(c_\Gamma n)^{-2h}\). The odd first-derivative evaluation has squared kernel at most \((c_\Gamma n)^{-2}\mathsf K_{n,M}(0,0)\), by the full comparison between the positive pushforward measures \(d\rho_n\) and \(x\,d\rho_n\). The remaining odd coefficients obey the same paired-root bound. After the retained factors \(q^{2h}\) and \(q^{2h+1}\), summing row norms bounds the whole covariance by the first matrix in (JB4). It is not an entrywise-to-Loewner inference without a trace bound.

For the lower covariance, put \(H_L(y)=\mathsf K_{n,L}(y,0)/\mathsf K_{n,L}(0,0)\). Its zeros, if present, have modulus at least \(c_\Gamma n\), since \(yH_L\) is the next odd orthogonal polynomial. The Taylor coefficients of \(H_L^{-1}\), through degree \(b-1\), are bounded by the complete homogeneous coefficients in \(V_{q,b}\). Multiply \(H_L\) by the full truncated inverse times the prescribed jet. This produces a polynomial of degree at most \(L+b-1<M+1\) with exactly that jet. Applying the complete multiplication bound at most \(b-1\) times gives squared norm at most
\(L_{q,b}\|a\|_2^2/\mathsf K_{n,L}(0,0)\). This simultaneous right inverse proves the lower bound in (JB5), including all complex jet combinations.

Changing the weight \(\nu_n\) to \(\nu_q=y^{2b}\nu_n\) gives
\[
 \left|\log[d_n\mathsf K_{n,h}(0,0)]
       -\log[d_q\mathsf K_{q,h}(0,0)]\right|
 \le2b\log(C_\Gamma/c_\Gamma)
 \tag{JB6}
\]
for the present degree range. Apply the full raising bound repeatedly to the same polynomial and to the constant; the mass factors cancel only in the displayed product.

Combining (CU7), (JB3), (JB5), and (JB6), every relative eigenvalue \(\lambda\) of the low jet metric against the cutoff \(N_j\) satisfies
\[
 \boxed{|\log\lambda-q\beta(t_j)|\le\mathcal J_{q,b},}
 \tag{JB7}
\]
where one fully finite choice is
\[
 \begin{split}
 \mathcal J_{q,b}={}&\log\mathcal L_{q,b}
 +\max(\log L_{q,b},\log U_{q,b})
 +2b\log(C_\Gamma/c_\Gamma)\\
 &+110+3\log(q+2)+q\beta((b+1)/q).
 \end{split}
 \tag{JB8}
\]
The last term is the exact concavity bound for the integer degree shifts. In particular
\[
 \mathcal J_{q,b}
 =O\bigl(b\log(Cq/b)+b+\log(q+2)\bigr)
\]
with the fixed additive constant displayed in (JB8). No division of this error by an unjustified fixed rank is made.

# 4. Quantitative localization of the original conductor kernel

The inherited CK construction places a finite-codimension part of the original kernel in a high power band. Here its radius and every tail can be chosen with explicit dependence on \(k\). This turns the endpoint argument into a uniform, quantitative cutoff calculation.

## 4.1 A zero-free circle with a certified modulus bound

Write the exact centred symbol as
\[
 \mathcal E(z)=\sum_s a_se^{\sigma_sz}=z^{v_0}b(z),
 \qquad b(0)=i^{-v_0}\mu_{v_0}/v_0!\ne0.
\]
Put
\[
 B_A=\max(1,\max_s|\sigma_s|),\quad
 A_b=\frac{(\sum_s|a_s|)B_A^{v_0}}{|\mu_{v_0}|}\ge1.
\]
Taylor's remainder gives the global bound
\(|b(z)/b(0)|\le A_b e^{B_A|z|}\).
For \(R\ge2\), define
\[
 N_R=\left\lceil\frac{\log A_b+12B_AR}{\log2}\right\rceil,
 \qquad L_R=\log A_b+6B_AR,
\]
\[
 \boxed{\mathcal M_R=|b(0)|^{-1}e^{2L_R}
 [32(N_R+1)]^{N_R}.}
 \tag{LC1}
\]
There is a radius \(r\in[R,2R]\) containing no zero on its circle, with at most \(N_R\) interior zeros counting multiplicity, such that
\[
 \boxed{\max_{|z|=r}|b(z)^{-1}|\le\mathcal M_R.}
 \tag{LC2}
\]

Here is the proof. Jensen's formula on radius \(12R\) bounds the number of zeros in \(6R\) by \(N_R\). Choose a zero-free outer radius \(S\in[4R,6R]\), and divide \(b/b(0)\) by the finite disk Blaschke product of its zeros in \(S\), with unit phases chosen so that their values at zero are positive (not set equal to one). The quotient is zero-free. Its log modulus is at most \(L_R\) on the boundary. The positive harmonic function \(L_R-\log|b/(b(0)B)|\) has value at zero at most \(L_R\), so Harnack on \(|z|\le2R\) bounds it by \(3L_R\). Hence the quotient modulus is at least \(e^{-2L_R}\).

Choose \(r\in[R,2R]\) at distance at least \(R/[4(N_R+1)]\) from the moduli of all zeros in \(S\). The excluded intervals occupy less than half the radius interval. On that circle every Blaschke factor has modulus at least \([32(N_R+1)]^{-1}\). Their complete product proves (LC2). This is also constructive after certified isolation of the finite zeros; no such isolation is claimed to have been executed for an unspecified native period.

## 4.2 The exact finite-rank subtraction and the retained action defect

Use the auxiliary coefficient norm
\(\|p\|_{c,q}=\sum_jq^j|[y^j]p|\). Under the finite guard \(q\ge40\), \(\rho_k=k\sqrt{\delta^2+\gamma^2}/q\le1/2\), one may use
\[
 \boxed{e^{-10q}\|p\|_{c,q}\le\|[p]\|_{G_N^\sigma}
 \le e^{2q}\|p\|_{c,q},\quad\deg p<q.}
 \tag{LC3}
\]
For the upper bound, \(\|y^j\|_\sigma\le\sqrt{\sqrt{2\pi}}\,2^j j!\) follows from the full Gamma multiplication recurrence, including each raising row. For the lower polynomial bound, expand \(p(qx)\) in the complete Legendre basis on \([1,2]\). The coefficient sum of \(P_j(2x-3)\) is \(P_j(5)\le10^j\). The lower Gamma envelope on \([q,2q]\) yields an exponent at most \(8q\) for every degree through \(2q\). The complete Newton remainder modulo \(Q_k\) has coefficient norm at most \(2^{2q}\): each actual root has scaled modulus at most \(1/2\), and the complete homogeneous divided differences give the sum \((1+2\rho_k)^j\). This proves (LC3) for every original affine representative, rather than just its canonical coefficient representative.

Let \(D=\partial_y\) on degree below \(q\). Its norm in \(\|\cdot\|_{c,q}\) is at most one. On the radius in (LC2), the exact CK6–7 identity is
\[
 b(D)^{-1}=A_r+B_r-L_r,
\]
\[
 A_r=\sum_{j<q}a_jD^j,\quad |a_j|\le\mathcal M_R r^{-j},\quad
 \|B_r\|\le r\mathcal M_R q e^{rq},\quad
 \operatorname{rank}L_r\le N_R.
 \tag{LC4}
\]
The full residue at each nonzero symbol pole is retained. The range of an order-\(a\) pole is spanned by the \(a\) derivatives of the actual truncated exponential. The operator \(B_r\) raises degree strictly.

The published bound $r\mathcal M_Rqe^{rq}$ for this degree-raising term can be improved substantially when $r$ grows. The exact coefficient from $y^n$ to $y^{n+j}$ in $R_zy^n$ is $n!z^{j-1}/(n+j)!$. Thus, in the original auxiliary coefficient norm,
\[
 \|R_z\|_{c,q}
 \le\frac1r\sum_{j=1}^{q-1}\frac{(qr)^j}{j!}
 \quad(|z|=r).
\]
The last terms dominate this finite sum for $r\ge2$: successive ratios backwards are smaller than $1/r$. Using $(q-1)!\ge((q-1)/\mathrm e)^{q-1}$ and $(q/(q-1))^{q-1}<\mathrm e$, one obtains
\[
 \sum_{j=1}^{q-1}\frac{(qr)^j}{j!}
 \le\frac{r}{r-1}\frac{(qr)^{q-1}}{(q-1)!}
 <\frac{(\mathrm e r)^q}{r-1}\le(3r)^q.
\]
The contour factor is exactly $r\mathcal M_R$. Therefore, since $r\le2R$,
\[
 \boxed{\|B_r\|_{c,q}\le\mathcal M_R(6R)^q.}
 \tag{LC4a}
\]
This uses the entire finite truncated exponential, not an infinite-tail approximation or a discarded pole. Its logarithm grows as $q\log R$ rather than $Rq$. It is the further estimate that permits the faster single-sequence rate below.


For \(p\in K_k\), the original conductor gives
\(f=\mathcal Tp=Q_{k-8}\eta\). Let \(f_0=D^{-v_0}_0f\) with all coefficients below \(v_0\) zero. Then
\(p=b(D)^{-1}f_0+l(p)\), with \(\deg l<v_0\). Define the actual subspace
\[
 K_{k,R}=\{p\in K_k:l(p)-L_rf_0=0\}.
\tag{LC5}
\]
It is independent of cutoff and has codimension at most
\(c_R=v_0+N_R\). On it, \(p=(A_r+B_r)f_0\).

Choose an integer \(b\) divisible by eight, with
\[
 8\Delta+8\le b\le q/10,\quad
 \Delta=q-(k-7)^2,\quad \rho=\rho_k<1/2.
\tag{LC6}
\]
Put \(M_T=\sum_s|a_s|e^{|\sigma_s|}\), and define
\[
 \begin{split}
 e_p={}&q^{v_0}M_T\mathcal M_R
 \left[(2+(6R)^q)(1-\rho)^{-q'}2^{q'}\rho^{b/8}
       +2R^{-b/4}\right],\\
 e_U={}&(1-\rho)^{-q}e_p+
 \frac{4^q\rho^{b/2}}{1-\rho},\\
 \zeta_{k,b,R}={}&e^{12q}(1+\rho)^q e_U.
 \end{split}
 \tag{LC7}
\]
These are explicit finite quantities in the original fixed symbol and roots.

The lower polynomial's complete coefficient tail gives
\[
 \|P_{<q'-h}f\|_{c,q}
 \le(1-\rho)^{-q'}2^{q'}\rho^h\|f\|_{c,q}.
\]
Because \(b\ge8\Delta+8\), the part of \(f_0\) below \(q-b/4\) is bounded by the term with \(\rho^{b/8}\) in (LC7). The high part must lose at least \(b/4\) degrees to reach below \(q-b/2\) through \(A_r\), giving \(2\mathcal M_R R^{-b/4}\). The degree-raising \(B_r\) uses only the small low input. This proves the first line of (LC7) as a relative coefficient bound on \(P_{<q-b/2}p\).

Retain the actual triangular map
\[
 U_QF=[Q_k(y)y^{-q}F(y)]_+.
\tag{LC8}
\]
Its norm is at most \((1+\rho)^q\), its inverse norm at most \((1-\rho)^{-q}\), and its inverse coefficient tail beyond depth \(b/2\) is at most \(4^q\rho^{b/2}/(1-\rho)\). These are complete elementary and homogeneous symmetric-function bounds. Thus
\[
 A_{k,b,R}p=P_{\ge q-b}U_Q^{-1}p
\]
satisfies
\[
 \boxed{\|p-U_QA_{k,b,R}p\|_{G_N^\sigma}
 \le\zeta_{k,b,R}\|p\|_{G_N^\sigma}}
 \tag{LC9}
\]
at every cutoff. Equation (LC3) is what transfers the coefficient tail to this relative metric estimate. If \(\zeta<1\), the map is injective on \(K_{k,R}\).

The source's complete CK10–11 comparison gives a fixed \(C_Q\) such that, on every band affine fibre,
\[
 e^{-C_Q}\|F\|_\sigma^2\le\|U_QF\|_\sigma^2\le e^{C_Q}\|F\|_\sigma^2.
 \tag{LC10}
\]
Its mechanism is the complete CK10–11 comparison, not a formal quotient identification. Here is one explicit finite choice of its constant. Put $\epsilon_0=2^{-32}$, $d_*=q+b$, $M_\sigma=\sqrt{2\pi}$, and
\[
 E_Q=\frac{q(\rho/\epsilon_0)^2}{1-(\rho/\epsilon_0)^2},\qquad
 r_Q=\sqrt{M_\sigma}e^{8q}2^q\rho^{q-b}\epsilon_0^{-b},
\]
\[
 i_F=2\sqrt2M_\sigma q^{-1/2}(d_*+1)^2 10^{2d_*}
 e^{\pi q}\epsilon_0^{2(q-b)},
\]
\[
 i_U=8\sqrt2M_\sigma q^{-1/2}(d_*+1)^2 10^{2d_*}
 e^{\pi q}(2\epsilon_0+\rho)^{2q}(2\epsilon_0)^{-2b}.
\]
On the finite guards
\[
 \rho\le\epsilon_0/2,\quad i_F\le1/4,\quad i_U\le1,
 \quad r_Q\le e^{-E_Q/2}/4,
\]
one may take
\[
 \boxed{C_Q=E_Q+2\log2.} \tag{LC10a}
\]
To prove it, write $F(qx)=x^{q-b}h(x)$. Outside $|x|<\epsilon_0$, pairing all actual opposite roots gives the squared logarithmic multiplier bound $E_Q$. The negative Laurent part of $q^{-q}Q_k(qx)x^{-b}h(x)$ has coefficient sum at most $2^q\rho^{q-b}\|h\|_1$. Its full exterior norm relative to $\|F\|_\sigma$ is therefore at most $r_Q$, by the pre-quotient coefficient lower bound used in (LC3). The complete Legendre estimate for $h$ on $[1,2]$ bounds the inner part of $F$ by $i_F\|F\|_\sigma^2$. Cauchy's polynomial-part formula on $|x|=2\epsilon_0$ bounds the inner part of $U_QF$ by $i_U\|F\|_\sigma^2$. Hence
\[
 \frac{\|U_QF\|_\sigma}{\|F\|_\sigma}
 \ge e^{-E_Q/2}\sqrt{1-i_F}-r_Q>\tfrac12e^{-E_Q/2},
\]
\[
 \frac{\|U_QF\|_\sigma}{\|F\|_\sigma}
 \le\sqrt{(e^{E_Q/2}+r_Q)^2+i_U}<2e^{E_Q/2}.
\]
This proves (LC10a). Both inner integrals and the exterior Laurent remainder are explicit. The guards hold eventually uniformly for $b\le q/10$; $E_Q=O_h(1)$. No root is removed.


The arithmetic action itself is not identified with the power model. If \(Q_k=\sum c_jy^j\), its exact defect remains
\[
 \boxed{MU_Q-U_QM_0
 =-[1](c_{q-1},c_{q-2},\ldots,c_0),}
 \tag{LC11}
\]
where \(M_0\) is multiplication modulo \(y^q\). This is verified by polynomial parts on every monomial. All metric statements below use (LC10), not an unproved action intertwiner.

## 4.3 Finite relative spectral estimate and an effective choice

Suppose \(\zeta_{k,b,R}\le1/4\). Set
\[
 A_{k,b,R}^{\rm err}
 =\mathcal J_{q,b}+2C_Q
 +2\log\frac{1+\zeta_{k,b,R}}{1-\zeta_{k,b,R}}
 +\log\kappa_k,
\]
\[
 B_k^{\rm whole}=40q+\log\kappa_k,
 \qquad c_R=\min(m,v_0+N_R).
 \tag{LC12}
\]
The full source nesting and (LC3) imply all relative metric logarithms lie in \([0,B_k^{\rm whole}]\). On the fixed core \(K_{k,R}\), (JB7), (LC9)–(LC10), and the native comparison (CU2) put every relative logarithm within \(A_{k,b,R}^{\rm err}\) of \(q\beta(t_j)\). Generalized eigenvalue interlacing therefore gives
\[
 \boxed{\sum_{i=1}^{m}
 |\log\lambda_i(H_{K,N_j},H_{K,N_0})-q\beta(t_j)|
 \le mA_{k,b,R}^{\rm err}
 +2c_R[B_k^{\rm whole}+q\beta(11/10)].}
 \tag{LC13}
\]
Here \(\lambda_i(H_{K,N_j},H_{K,N_0})\) denotes the spectrum of
\(H_{K,N_j}^{-1/2}H_{K,N_0}H_{K,N_j}^{-1/2}\). At most \(c_R\) directions can lie above the core interval and at most \(c_R\) below it. This is the origin of the factor two; no favorable sign is assigned to the exceptional quotient.

One effective eventual choice is
\[
 L_k=\log(k+e),\qquad
 R_k=e^{2\sqrt{L_k}},\qquad
 b_k=8\left\lceil\frac{32q}{8\sqrt{L_k}}\right\rceil.
 \tag{LC14}
\]
Use it only when (LC6), the complete two-region guards in (LC10a), and $\zeta\le1/4$ hold. All are explicit finite inequalities. They hold eventually. In fact
\[
 \log\mathcal M_R=O_A(R\log(R+2))=o(q),\quad
 b_k/(q)=32/\sqrt{L_k}+O(1/q).
\]
The high-derivative term has exponent
$-(b_k/4)\log R_k\le-16q$ before the $e^{12q}$ coefficient-to-metric cost. The low-degree tail in (LC7) now has exponent at most
\[
 q\log(6R_k)-\frac{b_k}{8}\log(1/\rho_k)+O_h(q+k+\log q)
 =-2q\sqrt{L_k}+O_h(q).
\]
Here $\log(1/\rho_k)=L_k-O_h(1)$; every original lower-root coefficient factor and the primitive's $q^{v_0}$ remain inside the indicated explicit (LC7) constants. The inverse-triangular tail is smaller still. Thus $\zeta\le e^{-q}$ eventually.

The complete exceptional codimension is now
$c_R=O_A(e^{2\sqrt{L_k}})=k^{o(1)}$, while (JB8) gives
\[
 \frac{A_{k,b,R}^{\rm err}}q
 =O_{h,A}\!\left(\frac{\log L_k}{\sqrt{L_k}}
 +\frac{\log\kappa_k}{q}\right).
\]
Consequently the single-sequence native error is
\[
 \boxed{\frac{R_{K,k}}{mq}
 =O_{h,A}\!\left(
 \frac{\log L_k}{\sqrt{L_k}}
 +\frac{e^{2\sqrt{L_k}}}{k}
 +\frac{\log\kappa_k}{q}\right).}
 \tag{LC15}
\]
This improves the rate obtained by using the whole infinite exponential $e^{Rq}$ in the residue bound. Its sufficient threshold is still large, since the chosen band must satisfy $b_k\le q/10$ and every two-region/source guard. It is not advertised as a practical small-$k$ native enclosure. No derivative is taken of an uncontrolled asymptotic remainder.

# 5. Original subquotients, observation layers, and the loss distribution

## 5.1 A simultaneous subquotient theorem

Let \(S_k\subseteq K_k\) and \(R_k\subseteq S_k\) be fixed coefficient subspaces as the cutoff varies. The metric on \(S_k/R_k\) is its full attained metric, not a raw coordinate block; let its rank be \(r_k\). With the notation of (LC12),
\[
 \boxed{\sum_{i=1}^{r_k}|\log\lambda_i-q\beta(t_j)|
 \le r_kA_{k,b,R}^{\rm err}
 +2\min(c_R,r_k)[B_k^{\rm whole}+q\beta(11/10)].}
 \tag{SQ1}
\]
Restriction first intersects the original core with \(S_k\), increasing its codimension by at most \(c_R\). For the quotient, the metric is the inverse compression of the inverse restricted metric. Generalized min–max therefore preserves the same upper and lower exceptional counts. This proves (SQ1) and retains every complete minimum.

For every \(r_k\to\infty\),
\[
 \sup_j\frac1{r_kq}\sum_i|\log\lambda_i-q\beta(t_j)|\longrightarrow0.
 \tag{SQ2}
\]
For this assertion one may first fix an arbitrarily narrow band, then choose its fixed zero-free circle, and only then let \(k\) grow. The core codimension is then fixed and divided by \(r_k\). Letting the band width tend to zero completes the proof. It requires no specified growth rate beyond divergence of the subquotient rank. For an explicit rate, use (SQ1) with the actual ranks and (LC14)–(LC15).

For arbitrary \(0\le r_k\le m\), even bounded ranks,
\[
 \log\frac{\det H_{S/R,N_0}}{\det H_{S/R,N_j}}
 =r_kq\beta(t_j)+o_{h,A}(kq)
\]
uniformly in the subquotient. A universal per-direction limit for a fixed exceptional line is not asserted.

## 5.2 Every actual arithmetic observation layer

Keep the original filtration
\(K_s=\bigcap_{h=0}^s\ker(\Lambda M^h)\), and its complete layer covariance from AP14–16:
\[
 D_{s,N}=F_sH_{s-1,N}^{-1}F_s^*,\qquad
 b_{s,k}=\dim K_{s-1}-\dim K_s.
\]
Its inverse is the actual attained metric on \(K_{s-1}/K_s\). Therefore
\[
 \boxed{\log\frac{\det D_{s,N_j}}{\det D_{s,N_0}}
 =b_{s,k}q\beta(t_j)+o_{h,A}(kq),}
 \tag{SQ3}
\]
with an \(o(b_{s,k}q)\) error when \(b_{s,k}\to\infty\). In particular, the first layer has \(b_{1,k}\ge k-18\) on the original period domain, so its full trajectory is determined in the stronger normalization. At the original four cutoffs,
\[
 -\mathcal R\log\det D_{s,N}
 =b_{s,k}C_\partial q+o(kq).
\]
The ranks still come from the actual conductor and complete invariant observation. They have not been set from a generic chain model.

The earlier two-response secant also inherits this full trajectory. In the original observed metric use the correctly retained combination
\[
 Z_N=12(2I+\mathscr Y_N(2\sigma/3))^{-1}
 -4(I+\mathscr Y_N(\sigma/2))^{-1}-2I.
\]
The current source corrects the outer factor in its derivation; this displayed formula is unchanged. For its original selected coefficient \(p_N=e_{m-h_k}(Z_N)\), the proved per-cutoff comparison to \(\det\Gamma_N\) has logarithmic width \(O_{h,A}(q\log q)\), with \(h_k=O_{h,A}(1)\). The boundary metric changes by \(O(k\log q)\) per direction. Hence
\[
 \boxed{\sup_j\left|
 \frac{\log p_{N_j}-\log p_{N_0}}{mq}-\beta(t_j)\right|\to0.}
 \tag{SQ4}
\]
This is a statement about that selected positive characteristic coefficient, not the zero full secant determinant or the independent complex-current numerator.

## 5.3 A measure of actual cutoff loss

Define the positive discrete measure on \([0,1]\)
\[
 \mu_k=\frac1{mq}\sum_{j=0}^{q-1}
 \log\frac{\det H_{K,N_j}}{\det H_{K,N_{j+1}}}
 \delta_{(j+1)/q}.
 \tag{SQ5}
\]
Its atoms are nonnegative by source nesting. The full cutoff theorem gives
\[
 \boxed{\mu_k\Rightarrow\beta'(t)dt,
 \qquad\mu_k([0,1])\to\beta(1)=C_\partial/2.}
 \tag{SQ6}
\]
No derivative of an \(o(q)\) error is taken: the proof is uniform convergence of the cumulative loss, followed by integration against continuous test functions.

If the normalized cumulative error is at most \(e_k<\beta(1)\), the probability obtained by dividing \(\mu_k\) by its actual total mass has one-dimensional Wasserstein error at most
\[
 \boxed{W_1\left(\mu_k/\mu_k([0,1]),
 \beta'(t)dt/\beta(1)\right)
 \le\frac{2e_k}{\beta(1)-e_k}+\frac1q.}
 \tag{SQ7}
\]
The final \(1/q\) accounts for the chosen step interpolation. It follows by integrating the CDF difference. This probability describes a scalar distribution of determinant loss; no physical source measure or norm has been normalized away.

In particular the first half of the window carries the exact asymptotic fraction in (PR13), approximately 69.7084 percent, not one half. The full cumulative loss also has the new evaluated integrated value
\[
 \boxed{\frac1{mq^2}\sum_{j=0}^{q-1}
 \log\frac{\det H_{K,N_0}}{\det H_{K,N_j}}
 \longrightarrow\int_0^1\beta(t)dt,}
 \tag{SQ8}
\]
whose certified interval is (PR12). This is an explicitly defined additional observable, not a reassignment of the original four-sign total.

# 6. The full original word spectrum through the cutoff interval

Retain the actual word \(T_k=D_k(M)\) and its original root split. Its kernel \(V\) has dimension \(d=q-\Delta=(k-7)^2\), its image \(W\) has dimension \(\Delta=16k-48\), and \(K\cap V=0\). The full boundary-value map \(\pi_\partial\) has kernel \(V\). Its attained metric is
\[
 G_N^\partial=(\pi_\partial G_N^{-1}\pi_\partial^*)^{-1}.
\]
All positive word eigenvalues are those of the inherited image form against this attained boundary metric; the \(d\) exact zero directions remain present.

## 6.1 Uniform localization of the whole image

A polynomial in \(W\) is \(D_kh\), \(\deg h<\Delta\), with every root of \(D_k\) of modulus at most \(R_k=k\sqrt{\delta^2+\gamma^2}\). Unlike the full conductor inverse, this factorization has no finite-symbol-pole correction. If \(b\) satisfies (LC6), define
\[
 e_W=(1-\rho)^{-q}(1-\rho)^{-d}2^d\rho^{b/4}
       +\frac{4^q\rho^{b/2}}{1-\rho},
 \qquad
 \zeta_W=e^{12q}(1+\rho)^q e_W.
 \tag{WE1}
\]
The complete leading-coefficient inversion of \(D_kh\), followed by the same triangular map (LC8), proves (LC9) for every vector of \(W\), with \(\zeta_W\) and with no exceptional quotient. Consequently
\[
 \boxed{e^{-q\beta(t_j)-a_{W,k}}G_{W,N_0}
 \preceq G_{W,N_j}
 \preceq e^{-q\beta(t_j)+a_{W,k}}G_{W,N_0},}
 \tag{WE2}
\]
where
\[
 a_{W,k}=\mathcal J_{q,b}+2C_Q
 +2\log\frac{1+\zeta_W}{1-\zeta_W}+\log\kappa_k.
\]
Use the finite guards \(\zeta_W\le1/4\) and (LC6). The choice
\[
 b=8\left\lceil\frac{128q}{8\log(1/\rho_k)}\right\rceil
 \tag{WE3}
\]
satisfies them eventually, and gives
\[
 a_{W,k}=O_h(q\log\log k/\log k+\log\kappa_k+1)=o(q).
\]
This is a form comparison on all \(\Delta\) image directions, not an inference from their determinant.

## 6.2 A direct finite low-end word band

For completeness the low-end band can be obtained without a large-degree zero law. Put \(\epsilon_*=2^{-32}\), \(T_* =\epsilon_*q\), and require \(R_k\le T_*/2\), \(\Delta\le q/10\), \(d\ge36\). Define
\[
 r_*=R_k/T_*,\qquad
 K_D=2\sqrt2\sqrt{2\pi}\,\Delta^2q^{-1/2}
 10^{2\Delta}e^{\pi q}
 (\epsilon_*+R_k/q)^{2d},
\]
\[
 E_D=\frac{2dr_*}{1-r_*}+\log(1+K_D).
 \tag{WE4}
\]
Then, for every \(\deg h<\Delta\),
\[
 \boxed{e^{-E_D}\|y^dh\|_\sigma^2
 \le\|D_kh\|_\sigma^2\le e^{E_D}\|y^dh\|_\sigma^2.}
 \tag{WE5}
\]
Outside \(|y|<T_*\), sum the logarithmic error from all \(d\) root factors. Inside, the full Legendre evaluation bound on \([q,2q]\) gives the factor \(\Delta^2 10^{2\Delta}/q\); the reference norm on that interval is bounded below by
\(q^{2d}(2\sqrt{2q})^{-1}e^{-\pi q}\int_q^{2q}|h|^2\). Both inner integrals are bounded by \(K_D\) times the reference outer integral. This proves (WE5), including the original region near zero and every nonreal root. Here \(E_D=O_h(k)\) on the eventual domain.

Let \(\mathcal L_{q,\Delta}\) be (JB2), with \(n=d\). In boundary-value coordinates the interpolation matrix is
\(\mathsf V_{ij}=(\omega_i/q)^j\), \(0\le j<\Delta\). Retaining every root difference gives
\[
 \|\mathsf V\|\le\Delta,
 \qquad\|\mathsf V^{-1}\|\le
 V_-:=\Delta\left(\frac{q+R_k}{2\delta}\right)^{\Delta-1}.
\]
The actual word sends a boundary value \(b\) to \(D_kh\), with \(h(\omega_i)=b_i\). Thus (JB2) and (WE5) give its image form in this exact coordinate map.

The original Gamma boundary quotient has the finite bounds
\[
 (A_\partial)^{-1}I\preceq G_N^{\partial,\sigma}\preceq B_\partial I,
\]
\[
 A_\partial=\frac{\Delta e^2}{\sqrt{2\pi}}(2q+1)^{3/2}
 (4q+1)^{R_k+1},\quad
 B_\partial=\Delta\sqrt{2\pi}
 \left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)}.
 \tag{WE6}
\]
These follow from the full evaluation kernel and full lower-degree Lagrange sections. They are the retained original finite boundary constants, with mass \(\sqrt{2\pi}\).

Let \(c_0=2q\log q+\eta_0q\). A common finite error is
\[
 \begin{split}
 e_{0,k}={}&E_D+\log\mathcal L_{q,\Delta}+\log\kappa_k
 +2\log\Delta+2\log\max(1,V_-)\\
 &+\log\max(1,A_\partial)+\log\max(1,B_\partial)
 +\left|\log d_d-c_0\right|.
 \end{split}
 \tag{WE7}
\]
Then all \(\Delta\) positive eigenvalues at \(N_0=q-1\) satisfy
\[
 e^{c_0-e_{0,k}}\le\lambda_j^+(T_k^{\dagger_{G_{N_0}}}T_k)
 \le e^{c_0+e_{0,k}}.
\tag{WE8}
\]
The numerator is the full word image form; the denominator is the attained boundary quotient. Applying the same native comparison to both costs \(\log\kappa_k\), not either source mass independently. By (HK3),
\[
 |\log d_d-c_0|
 \le2\Delta(\log q+1)+|\eta_0|\Delta+5.
\]
Hence \(e_{0,k}=O_h(k\log q)\). This finite derivation can replace the inherited low-end word asymptotic in the following statements.

## 6.3 Uniform positive energy band

Put
\[
 \omega_k=\log\kappa_k+
 \log\max(1,A_\partial)+\log\max(1,B_\partial),\qquad
 e_k^{\rm word}=e_{0,k}+a_{W,k}+\omega_k.
\]
The domain boundary metric changes by at most this fixed logarithmic comparison at every cutoff. Therefore
\[
 \boxed{e^{c_0-q\beta(t_j)-e_k^{\rm word}}
 \le\lambda_l^+(T_k^{\dagger_{G_{N_j}}}T_k)
 \le e^{c_0-q\beta(t_j)+e_k^{\rm word}},}
 \tag{WE9}
\]
for every \(1\le l\le\Delta\), simultaneously in \(j\). Here
\(e_k^{\rm word}=O_h(q\log\log k/\log k+k\log q)=o(q)\)
on the finite guards above.

No eigenvalue is assigned to one of the \(d\) zero directions. The physical word remains \(D_k(M_k)\); its positive square is formed with the actual cutoff metric.

# 7. The entire original cutoff–frequency surface

## 7.1 The kernel-energy logarithms cancel their common cutoff scale

Let
\[
 A_{K,N}=H_{K,N}^{-1/2}I_K^*T_k^*G_NT_kI_KH_{K,N}^{-1/2}>0.
\]
The numerator is the restriction of the inherited image metric under the fixed injective map \(T_kI_K\). Equation (WE2) gives its full relative Loewner band; equation (LC13) gives the full mean-absolute logarithmic change of its denominator.

The required metric perturbation inequality has a direct proof. For a fixed positive form \(B\), move a positive metric by
\(H(s)=H_0^{1/2}e^{sK}H_0^{1/2}\). The representative of \((B,H(s))\) is
\(e^{-sK/2}B_0e^{-sK/2}\). At every differentiability point, each eigenvalue logarithm has derivative \(-u_i^*Ku_i\); at a repeated eigenvalue, diagonalize the compressed derivative on its eigenspace. Thus the sum of absolute derivatives is at most \(\operatorname{Tr}|K|\). Integration gives
\[
 \sum_i|\log\lambda_i(B,H_1)-\log\lambda_i(B,H_0)|
 \le\operatorname{Tr}|\log(H_0^{-1/2}H_1H_0^{-1/2})|.
 \tag{FR1}
\]
All eigenvalues are ordered consistently. This is a metric comparison, not an assumed common eigenvector frame.

Let \(R_{K,k}\) denote the right side of (LC13), uniform in cutoff, and put
\[
 R_{A,k}=R_{K,k}+m a_{W,k}.
\]
Apply (FR1) after multiplying both numerator and denominator at cutoff \(N_j\) by the same scalar \(e^{q\beta(t_j)}\). That simultaneous multiplication leaves the generalized operator unchanged. One obtains
\[
 \boxed{\sup_j\sum_{i=1}^m
 |\log\alpha_{i,N_j}-\log\alpha_{i,N_0}|
 \le R_{A,k}=o(kq),}
 \tag{FR2}
\]
where \(\alpha_{i,N}\) are the actual positive kernel energies.

## 7.2 All positive regularizers, without a hidden endpoint restriction

Use the original response
\[
 \mathscr Y_N(z)=\Lambda z(zI+T_k^{\dagger_{G_N}}T_k)^{-1}L_N,
 \qquad z>0.
\]
The full Schur determinant identity, retaining the entire kernel and all word zeros, is
\[
 \det\mathscr Y_N(z)=
 \frac{\det(I_m+A_{K,N}/z)}
 {\det(I_q+T_k^{\dagger_{G_N}}T_k/z)}.
 \tag{FR3}
\]
The function \(x\mapsto\log(1+e^x/z)\) is 1-Lipschitz for every \(z>0\). Thus (FR2) and (WE9) imply the finite uniform bound
\[
 \boxed{\begin{split}
 \sup_{j,z>0}\bigg|\log\frac{\det\mathscr Y_{N_j}(z)}
 {\det\mathscr Y_{N_0}(z)}
 -\Delta\log\frac{z+e^{c_0}}{z+e^{c_0-q\beta(t_j)}}\bigg|
 \le R_{A,k}+2\Delta e_k^{\rm word}.
 \end{split}}
 \tag{FR4}
\]
Its error is \(o(kq)\). In particular it is valid when the regularizer tends to zero faster than any prescribed exponential; no unresolved original-kernel factor has been held fixed to obtain it.

For
\(\xi_k(z)=(\log z-2q\log q)/q\), the scalar softplus estimate adds at most \(\log2/q\), and yields
\[
 \boxed{\begin{split}
 \sup_{j,z>0}\bigg|
 \frac1{\Delta q}\log\frac{\det\mathscr Y_{N_j}(z)}
 {\det\mathscr Y_{N_0}(z)}
 -\big[(\eta_0-\xi_k(z))_+
 -(\eta_0-\beta(t_j)-\xi_k(z))_+\big]
 \bigg|\longrightarrow0.
 \end{split}}
 \tag{FR5}
\]
This is the cutoff–frequency surface for the unchanged \(\Lambda\). At \(t=1\) it agrees with the integrated endpoint theorem, including its signs. It is not the earlier enlarged observation \(\Lambda_8\).

## 7.3 Every inverse exterior rank

Assume additionally \(d\ge m\), which holds throughout the eventual sequence (and already for \(k\ge21\)). Flattening the positive energy spectrum to its common centre retains the exact primary angles \(\Gamma_N\). The inverse-response spectrum then consists of
\[
 1+x_N\quad(\Delta-m\text{ entries}),\qquad
 \frac{1+x_N}{1+x_N\gamma_{i,N}}\quad(m\text{ entries}),
\]
and \(d-m\) unit entries, where \(x_N=e^{c_0-q\beta(t_j)}/z\). The actual word-energy error changes the logarithm of each nonunit inverse eigenvalue by at most \(e_k^{\rm word}\).

The boundary numerator of \(\Gamma_N\) changes by at most \(\omega_k\) per logarithmic direction. Applying (FR1) to that numerator and \(H_{K,N}\) shows
\[
 \sum_i|\log\gamma_{i,N_j}-\log\gamma_{i,N_0}
             -q\beta(t_j)|\le R_{K,k}+m\omega_k.
\]
Hence \(x_N\gamma_{i,N}\) has cutoff change controlled by the same right side. For \(p_0=\min(p,\Delta)\), if \(p_0\le\Delta-m\), no angle factor occurs in the largest exterior product. Otherwise \(p_0\ge\Delta-m+1=8k-31\), and the entire angle error divided by \(p_0q\) tends to zero. Therefore
\[
 \boxed{\begin{split}
 \sup_{j,z>0}\sup_{1\le p\le q-m}\bigg|
 \frac{\log\|\wedge^p\mathscr Y_{N_0}(z)^{-1}\|
       -\log\|\wedge^p\mathscr Y_{N_j}(z)^{-1}\|}{p_0q}
 -\big[(\eta_0-\xi_k(z))_+
 -(\eta_0-\beta(t_j)-\xi_k(z))_+\big]
 \bigg|\to0.
 \end{split}}
 \tag{FR6}
\]
Each norm is in its original observed metric. The rank-one operator norm and full determinant are included, but no identification with the fixed conductor's inverse is made.

## 7.4 The measured phase becomes an explicit moving interval

For \(z=ie^s\), define the continuous determinant phase by the factorized positive spectrum:
\[
 \Phi_N(s)=(\Delta-m)\pi/2
 +\sum_i\arctan(e^s/\alpha_{i,N})
 -\sum_l\arctan(e^s/\lambda_{l,N}^+).
\tag{FR7}
\]
This is the original scalar measured-determinant phase with its full multiplicities, not the phase of a single response entry. The fixed zero-power term cancels between cutoffs.

For \(K(s)=\arctan e^s\), monotonicity and translation give the exact identity
\[
 \int_{\mathbb R}|K(s-a)-K(s-b)|ds=\frac\pi2|a-b|.
\]
Equations (FR2) and (WE9) therefore imply
\[
 \boxed{\sup_j\left\|
 -\frac2{\pi\Delta}
 [\Phi_{N_j}(c_0+q\,\cdot)-\Phi_{N_0}(c_0+q\,\cdot)]
 -\mathbf1_{(-\beta(t_j),0)}
 \right\|_{L^1(\mathbb R)}
 \le\frac{R_{A,k}}{\Delta q}
 +\frac{2e_k^{\rm word}}q+\frac8{\pi q}.}
 \tag{FR8}
\]
For the last term, \(\arctan u\le u\) bounds the two soft transition tails. This retains both frequency ends. It does not imply pointwise convergence at the interval boundaries or assign the separate complex arithmetic-current sign.

## 7.5 Averaging the original heat over the cutoff interval

Use the common physical heat time
\[
 \tau_k(b)=e^{-c_0+qb}.
\]
The original measured heat is \(\operatorname{Tr}_B[\Lambda e^{-\tau H_N}L_N]\), not the heat of the arithmetic operator compressed first. The exact primary-angle identity gives its zero-energy part
\(d-m+\operatorname{Tr}\Gamma_N\). Moreover the difference between its positive-energy contribution and the full positive trace, after adding \(\operatorname{Tr}\Gamma_N\), lies in \([0,\operatorname{Tr}\Gamma_N]\).

The original finite angle-tail bound and whole-source comparison give a common \(C_{\rm ang}=O_{h,A}(1)\) with \(\operatorname{Tr}\Gamma_N\le C_{\rm ang}\) over the entire window. All the native pole and period factors remain in that finite provider.

Define
\[
 \mathcal H(b)=
 \begin{cases}
 1,&b\le0,\\
 1-\beta^{-1}(b),&0<b<\beta(1),\\
 0,&b\ge\beta(1).
 \end{cases}
\]
Then
\[
 \boxed{\sup_{b\in\mathbb R}\left|
 \frac1{q\Delta}\sum_{j=0}^{q-1}
 \left[\operatorname{Tr}_B\Lambda e^{-\tau_k(b)H_{N_j}}L_{N_j}
 -(d-m)\right]-\mathcal H(b)
 \right|
 \le\frac{25}{4}\frac{e_k^{\rm word}+\log q}{q}
 +\frac4q+\frac{C_{\rm ang}}\Delta.}
 \tag{FR9}
\]
To prove it, outside \(|\beta(t_j)-b|\le\epsilon\), (WE9) bounds the heat by its limiting indicator with error at most \(1/q\), for
\(\epsilon=(e_k^{\rm word}+\log q)/q\). Since \(\beta'\ge\beta'(1)>8/25\) on \((0,1]\), the critical set occupies length at most \((25/4)\epsilon\) and at most two additional grid cells. The measured/full difference is at most \(C_{\rm ang}/\Delta\). This proves (FR9), including both threshold endpoints, without assigning a pointwise critical heat value.

# 8. Integration with edition 025 and new shrinking-window laws

The repository changed from the baseline 024 edition while this work was in progress. Its current complete proof files are `INTEGRATED_PROFILE_AND_RECEIVERS.md` (IR1–24), `POWER_CUTOFF_PROFILE_PROOF.md` (PP1–45), `ELLIPTIC_PROFILE_PROOF.md` (EP1–19), and `PHASE_HEAT_PROOFS.md` (PH1–41), at `76473e0564b32f7566e191829bf67477c8950f0b`. The inspected ranges are recorded in the ledger. The structural full-window, all-pair, fixed-subquotient, and phase/heat results are now upstream results. Their profile is \(J(t)=\beta(t)\). Their proof still retains the monic zero-statistic remainder \(r_U(n,M)=o(n)\) in PP23–28. The new harmonic-measure estimate (HK10) instead treats the evaluation minimum itself, which is why (HK11) does not need a rate for that separate monic statistic.

The native error (LC13) can consequently be calculated from finite constants, and (LC14)–(LC15) supplies a single-sequence rate instead of first fixing a band, then taking \(k\to\infty\), then shrinking the band. This does not imply a useful small numerical threshold; every very conservative eventual guard is retained. The original native period and unit remain fixed.

## 8.1 Quantitative comparison between arbitrary cutoffs

Set
\[
 e_k=\frac{R_{K,k}}{mq},\qquad
 F_k(t_j)=\frac1{mq}\log\frac{\det H_{K,N_0}}{\det H_{K,N_j}}.
\]
Then \(F_k(0)=0\) exactly, and \(|F_k(t_j)-\beta(t_j)|\le e_k\) on every original cutoff. The finite all-direction version is
\[
 \boxed{\sum_{a=1}^m
 \left|\log\lambda_a(H_{K,N_j}^{-1/2}H_{K,N_i}H_{K,N_j}^{-1/2})
 -q[\beta(t_j)-\beta(t_i)]\right|\le2R_{K,k}.}
 \tag{ME1}
\]
For a direct proof, multiply each metric by its specified scalar \(e^{q\beta(t)}\). The sum of absolute relative logarithms from each rescaled metric to \(H_{K,N_0}\) is at most \(R_{K,k}\). Apply the derivative argument of (FR1) along the two concatenated metric geodesics. Its instantaneous trace-norm length is invariant under the explicitly changing isometries; integration bounds the endpoint relative logarithms by the sum of the two lengths. This is not an assumption that different cutoff Grams commute. The same proof applies to the complete fixed subquotients in (SQ1).

## 8.2 A resolved local mean of the actual rank-one source responses

Let \(u_N\) be the remainder class of the next original unit-norm source polynomial. Appending that source gives exactly
\[
 G_{N+1}^{-1}=G_N^{-1}+u_Nu_N^*.
\]
Define the actual total and observed leverages
\[
 \rho_N=u_N^*G_Nu_N,\qquad
 b_N=(\Lambda u_N)^*Q_{B,N}(\Lambda u_N).
\]
The original orthogonal splitting into \(K\) and its attained observation complement gives the exact increment (IR10–13)
\[
 A_{j,k}=\log\frac{\det H_{K,N_j}}{\det H_{K,N_{j+1}}}
 =\log\frac{1+\rho_{N_j}}{1+b_{N_j}}\ge0.
 \tag{ME2}
\]
For a positive integer window length \(L\), put \(h=L/q\), and retain the geometric mean in its literal exponent:
\[
 \mathcal G_{j,L}
 =\left[\prod_{l=j}^{j+L-1}
 \frac{1+b_{N_l}}{1+\rho_{N_l}}\right]^{1/(mL)}.
\]
No individual observed leverage is reconstructed from the product. Telescoping gives
\[
 \boxed{\left|-\log\mathcal G_{j,L}
 -\frac{\beta(t_j+h)-\beta(t_j)}{h}\right|
 \le\frac{2e_k}{h}.}
 \tag{ME3}
\]
At \(j=0\), the right side improves to \(e_k/h\), because the low endpoint is exact.

For \(a>0\), and \(a\le t_j<t_j+h\le1\), let
\[
 M_a=\frac{10(1+a)}{9a}.
\]
On this interval, \(-\beta''\le M_a\). Indeed the variance representation in (PR6) gives
\(\operatorname{Var}(n)\ge p_0p_1=z/(4F(z)^2)\), and
\(F(z)^2\le(1-z)^{-1}\). Using
\(z\ge a/(1+a)\), \(z\le11/20\), proves the bound. Thus
\[
 \boxed{\left|\log\frac{\mathcal G_{j,L}}{\sqrt{z_{t_j}}}\right|
 \le\frac{2e_k}{h}+\frac12M_a h.}
 \tag{ME4}
\]
The target \(\sqrt{z_t}\) follows from the exact identity
\(e^{-\beta'(t)}=\sqrt{z_t}\). It is a scalar value of this precisely defined geometric mean, not an identification of the arithmetic operator with the elliptic coordinate.

Choose the actual integer \(L=\lceil2q\sqrt{e_k/M_a}\rceil\) once it fits in the specified interior interval. Then the right side is at most
\[
 2\sqrt{M_a e_k}+\frac{M_a}{2q}.
 \tag{ME5}
\]
Accordingly this is a shrinking-window calculation whenever the finite bound \(e_k\to0\); each such window still contains a growing number of original source steps. No single-step limit is asserted.

At the initial endpoint there is an equally explicit nonstationary law. For \(h=L/q\le1\), (PR8) and the sharper \(j=0\) error give
\[
 \boxed{
 e^{-h/4-e_k/h}
 \le\frac{\mathcal G_{0,L}}{\sqrt{h/\mathrm e}}
 \le e^{e_k/h}.}
 \tag{ME6}
\]
For any \(h_k\downarrow0\) with \(e_k/h_k\to0\) and integer \(qh_k\),
\(\mathcal G_{0,qh_k}/\sqrt{h_k/\mathrm e}\to1\).
The source mass and all original phases already enter the leverages in (ME2); none is adjusted to force this limit.

## 8.3 Negative mesoscopic curvature of the original determinant loss

The explicit error also permits a second local difference, on windows larger than its square-root scale. Fix \(0<a<1/2\), and use
\[
 L_a=1280\left(\frac{1+a}{a}\right)^3.
\]
On \([a,1]\),
\[
 \boxed{|\beta'''(t)|\le L_a,\qquad -\beta''(t)>1/80.}
 \tag{ME7}
\]
For verification, if \(\kappa_3\) is the third centred moment of the coefficient distribution, then
\[
 \beta'''=\frac{\kappa_3}{32\operatorname{Var}(n)^3}.
\]
Since \(a_n\le1\) and \(F\ge1\), at \(z\le11/20\)
\[
 \mathbb E n^2\le\frac{z(1+z)}{(1-z)^3}\le\frac{6820}{729}<10,
\]
\[
 \mathbb E n^3\le\frac{z(1+4z+z^2)}{(1-z)^4}\le\frac{102740}{2187}.
\]
Also \(\mathbb E n=t/4\le11/40\). Hence
\( |\kappa_3|\le\mathbb E n^3+3(11/40)\mathbb E n^2+2(11/40)^3<55\).
The variance is at least \(9a/[80(1+a)]\) by the proof of (ME4). These rational bounds prove the first part of (ME7); \(\operatorname{Var}(n)<10\) proves the second.

For \(h=L/q\), \(t_j-h\ge a\), and \(t_j+h\le1\), the full finite result is
\[
 \boxed{
 \left|\frac{F_k(t_j+h)-2F_k(t_j)+F_k(t_j-h)}{h^2}
 -\beta''(t_j)\right|
 \le\frac{4e_k}{h^2}+\frac{L_a h}{3}.}
 \tag{ME8}
\]
The three native errors contribute \(4e_k/h^2\). For the profile itself use
\[
 \frac{\beta(t+h)-2\beta(t)+\beta(t-h)}{h^2}
 =\int_{-1}^{1}(1-|u|)\beta''(t+hu)du;
\]
the third-derivative bound costs \(L_ah\int|u|(1-|u|)du=L_ah/3\).
Whenever the right side of (ME8) is below \(1/80\), the native second difference is strictly negative. Thus the mean kernel-volume loss in the later of two adjacent original windows is smaller than in the earlier one. This is a sign theorem for the stated *mesoscopic scalar determinant difference*, not for the separate complex-current product.

Choosing, for example, \(h\asymp e_k^{1/3}\) proves convergence in (ME8). The resulting effective rate follows from (CU6). In contrast, differentiating an unquantified \(o(kq)\) remainder would not justify any shrinking-window conclusion.

## 8.4 An effective native quantile location

For \(0<\theta<1\), let the actual grid quantile be
\[
 \widehat t_{\theta,k}=\min\{t_j:F_k(t_j)\ge\theta F_k(1)\}.
\]
Its target is \(t_\theta=\beta^{-1}(\theta\beta(1))\). The cutoff profile is strictly increasing, and \(\beta'\ge8/25\) on \((0,1]\). The same finite error \(e_k\) therefore gives
\[
 \boxed{|\widehat t_{\theta,k}-t_\theta|
 \le\frac{25}{8}(1+\theta)e_k+\frac1q.}
 \tag{ME9}
\]
If the right side exceeds one, the estimate is still valid but uninformative. Otherwise, below the target by more than \(25(1+\theta)e_k/8\), the upper bound \(F_k\le\beta+e_k\) lies strictly below \(\theta F_k(1)\); above it by the same amount the lower bound lies above the target. Passing to the next grid point costs at most \(1/q\). This proves the statement without bounding an individual jump by its asymptotic derivative.

The new repository already certifies the half-volume location
\[
0.28581630680480845015<t_{1/2}<0.28581630680480845016.
\]
The scalar code included here independently replays that interval by bisection in the exact Landen coordinate and provides 30-decimal outward endpoints. The new native conclusion is the finite error
\[
 \boxed{|\widehat t_{1/2,k}-t_{1/2}|\le\frac{75}{16}e_k+\frac1q.}
 \tag{ME10}
\]
It depends on the actual finite constants in (LC12)–(LC13), not a supplied numerical native packet.

# 9. Verification and scope

The scalar certificate uses integer directed rounding and exact rational coefficients, 260 elliptic terms, and 130 certified bisections on a 90-digit integer grid. Its elliptic tail is bounded by the first omitted positive coefficient divided by \(1-z\); the derivative tail retains its additional linear index factor. The root is bracketed on \((0,16/25)\), and bisection stops with a rational interval, not a floating midpoint. The logarithm uses the convergent atanh series after exact power-of-two range reduction. The independent integrated-profile bound is (PR11).

The finite exact checker tests the hypergeometric coefficient identities, the Riccati equation, series reversion, interval constants, Gamma moments, complete quotient and layer minima, noncommuting metric similarities, and measured determinant and exterior identities. Negative controls include dropping the original mass, replacing a quotient by a raw block, suppressing the word kernel, treating a linear cutoff profile as correct, and replacing the actual measured energy by a compressed arithmetic square.

`REFERENCE_KERNEL_DIAGNOSTICS.json` contains exact rational values of \(d_q\mathsf K_{q,M}(0,0)\) for several finite Gamma reference examples, with separately identified non-interval logarithmic diagnostics. Small examples are not asserted to satisfy an asymptotic native guard. The actual native xi moments, admitted period, and invariant coefficient frames are not numerically supplied by those fixtures.

The new quantitative conclusions are (HK10)/(CU7a), the single-sequence native bound (LC13)–(LC15), the evaluated integrated loss (PR12), and the shrinking-window and native-quantile laws (ME3)–(ME10). The full-cutoff profile, derivative representation, subquotient structure, and qualitative phase/heat limits are also independently present in the new repository edition; the finite errors here can be inserted into those receivers. The separate native complex-current values/signs remain unfinished. No theorem here establishes an offcritical zeta zero or a proof of RH. No remote repository file was modified.

# References and exact source use

The source ledger gives canonical links and read ranges. Standard analytic identities are distinguished from the programme-specific derivations.

National Institute of Standards and Technology. (n.d.). *NIST Digital Library of Mathematical Functions*, §§5.11, 18.23, 19.4, 19.5, and 19.8. https://dlmf.nist.gov/5.11 ; https://dlmf.nist.gov/18.23 ; https://dlmf.nist.gov/19.8 . The log-Gamma remainder, Meixner–Pollaczek convention, elliptic series, and Landen identities are the classical formulas used explicitly above.

Split-Zero research programme. (2026a, September 22). *The original kernel value and its receiving calculations* [CK1–19]. *Zeta-function research reader*, commit `2b1445b21cc2fcd7e8b7ff34c6aea7139fb6afb5`. The fixed-symbol quotient maps, complete original source comparison, and full affine-fibre map are retained in (LC4), (LC8), and (LC10).

Split-Zero research programme. (2026b, September 22). *The complete Gamma-power jet minimum* [PJ1–70]. Same repository and commit. PJ1–23 supplies the finite Laguerre/near-zero comparison and full parity kernels; the finite right-inverse mechanism is independently made explicit in (JB2)–(JB8). The new scalar minimum proof replaces the use of the polynomial zero-statistic limit in this particular step.

Split-Zero research programme. (2026c, September 22). *Exact logarithmic moment and Euler constant* [ELLIPTIC_LOG_MOMENT_PROOF.md, EL1–14]. Same repository and commit. Its evaluated moment and Euler constant are retained in (PR3)–(PR4).

*Exact equilibrium for the square-root logarithmic potential*. (2026). [EIQ1–33, original uploaded cumulative source]. The full positive density, normalization, Euler inequality on both exterior regions, and uniqueness were read in the contiguous original section. The extracted bytes and their SHA-256 are included under `source_extracts/`.

Split-Zero research programme. (2026d, September 22). *The original kernel across the complete cutoff window* [SZ-20260922-025; IR, PP, EP and PH proof files]. Same repository, commit `76473e0564b32f7566e191829bf67477c8950f0b`. The source ledger distinguishes the read portions and mathematical overlaps. In particular (HK11) sharpens PP28 without asserting a rate for its different monic remainder PP23.
