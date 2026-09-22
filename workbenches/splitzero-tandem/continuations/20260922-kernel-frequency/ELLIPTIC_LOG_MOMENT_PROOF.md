# The logarithmic equilibrium moment and the original kernel coefficient

The diagonal Gamma calculation uses a logarithmic zero statistic. This note evaluates that statistic directly in the retained equilibrium family. It proves its equality with the previously supplied elliptic coefficient; a numerical resemblance is not used to identify the constants.

## EL1. The retained equilibrium family

For \(\alpha,\beta>0\), retain the potential
\[
 V_{\alpha,\beta}(x)=\beta\sqrt{x}-\alpha\log x,\qquad x>0,
\]
and its equilibrium probability \(\mu_{\alpha,\beta}\). The complete retained EIQ1–33 proof establishes existence, uniqueness, a single support interval \([u^2,v^2]\subset(0,\infty)\), the full Euler inequality, and smooth parameter dependence. Its endpoint equations are
\[
 r=\frac uv,\quad\kappa=\sqrt{1-r^2},\quad
 uK(\kappa)=\frac{\alpha\pi}{\beta},\qquad
 vE(\kappa)=\frac{(\alpha+2)\pi}{\beta}.
 \tag{EL1}
\]
Here \(K(\kappa)=\int_0^{\pi/2}(1-\kappa^2\sin^2t)^{-1/2}dt\) and
\(E(\kappa)=\int_0^{\pi/2}(1-\kappa^2\sin^2t)^{1/2}dt\).
The letter \(E\) in these elliptic formulas is not the arithmetic vector space. Define
\[
 w=\frac{u+v}{2},\qquad z=uv,\qquad c=\frac{v^2-u^2}{4},\qquad
 L(\alpha,\beta)=\int\log x\,d\mu_{\alpha,\beta}(x).
 \tag{EL2}
\]
These are the unchanged endpoints and logarithmic statistic of EIQ26 and EIQ33. The result is
\[
 \boxed{L(\alpha,\beta)=2(\alpha+1)\log w-\alpha\log z-2.}
 \tag{EL3}
\]

## EL2. Euler constant and its derivative

Let \(\ell\) denote the Euler constant with sign convention
\(V(x)-2\int\log|x-y|d\mu(y)=\ell\) on the support. Average this identity against the arcsine probability
\(d\omega(x)=dx/[\pi\sqrt{(v^2-x)(x-u^2)}]\). Its logarithmic potential is \(\log c\) at every point of this interval. One can verify this directly by putting \(x=(u^2+v^2)/2+(v^2-u^2)\cos t/2\) and integrating the Fourier series of the logarithm; the endpoint logarithmic singularities are integrable. The same substitution, or the two absolutely convergent Fourier series in EIQ27, gives
\[
 \int\log x\,d\omega=2\log w,\qquad
 \int\sqrt{x}\,d\omega=\frac{2vE(\kappa)}\pi.
\]
The second identity follows by writing \(x=v^2(1-\kappa^2\sin^2(t/2))\) and changing variables to \(t/2\). Equation EL1 therefore gives the exact constant
\[
 \ell=2(\alpha+2)-2\alpha\log w-2\log c.
 \tag{EL4}
\]

Fix \(\beta\) and differentiate in \(\alpha\). The required endpoint derivative identities are
\[
 \alpha\frac{w'}w+\frac{c'}c=1,
 \qquad 2(\alpha+1)\frac{w'}w=\alpha\frac{z'}z.
 \tag{EL5}
\]
Here and below a prime means \(\partial_\alpha\) with \(\beta\) fixed. To prove these identities without assuming an endpoint response, use \(r\) as the parameter. Differentiating the defining elliptic integrals gives
\[
 E_r=\frac{r(K-E)}{1-r^2},\qquad
 K_r=\frac{rK-E/r}{1-r^2}.
 \tag{EL6}
\]
For the second formula, differentiate under the integral and integrate the derivative of
\(\sin t\cos t/\sqrt{1-\kappa^2\sin^2t}\); its endpoints vanish. This proves the usual derivative identity, with the complementary-modulus chain factor included. The first follows immediately by differentiation under the integral.

The exact rational dictionary is
\[
 \alpha=\frac{2rK}{E-rK},\quad
 v=\frac{(\alpha+2)\pi}{\beta E},\quad
 w=\frac{(1+r)v}{2},\quad z=rv^2,\quad c=\frac{(1-r^2)v^2}{4}.
\]
Set \(a_r=d\alpha/dr\) and \(v_r/v=a_r/(\alpha+2)-E_r/E\). Substitution of EL6 yields
\[
 a_r=\frac{2(K-E)(E-r^2K)}{(E-rK)^2(1-r^2)}>0,
\]
\[
 \alpha\left(\frac{v_r}v+\frac1{1+r}\right)
 +2\frac{v_r}v-\frac{2r}{1-r^2}=a_r,
\]
\[
 2(\alpha+1)\left(\frac{v_r}v+\frac1{1+r}\right)
 -\alpha\left(2\frac{v_r}v+\frac1r\right)=0.
 \tag{EL7}
\]
For example multiply these equalities by \((E-rK)^2(1-r^2)\), substitute the two derivatives in EL6, and the coefficients of \(E^2,EK,K^2\) cancel separately. The exact symbolic checker retains those rational substitutions. The factors in \(a_r\) are positive by the defining integrals: \(K>E\) and \(E>r^2K\). Dividing by \(a_r\) proves EL5. Differentiating EL4 now gives
\[
 \ell'=-2\log w.
 \tag{EL8}
\]

## EL3. Determination of the integration constant

Write the minimum logarithmic energy as
\(\mathcal E=\int V\,d\mu-\iint\log|x-y|d\mu d\mu\).
The exact dilation \(x\mapsto t^2x\) changes this energy by
\(\beta(t-1)\int\sqrt{x}\,d\mu-2(\alpha+1)\log t\).
It has derivative zero at \(t=1\), hence
\(\beta\int\sqrt{x}\,d\mu=2(\alpha+1)\), the retained EIQ31 identity. Combining this with the integrated Euler identity gives
\[
 \mathcal E=\frac{2(\alpha+1)-\alpha L+\ell}{2}.
\]
Comparison of each minimizer with the neighbouring parameter's minimizer gives \(\partial_\alpha\mathcal E=-L\): the two energy difference quotients lie between the negatives of the two logarithmic moments, and their continuity, proved in EIQ29–30, gives the derivative. Thus
\[
 \alpha L'-L=2+\ell'=2-2\log w.
 \tag{EL9}
\]
The candidate \(L_*=2(\alpha+1)\log w-\alpha\log z-2\) satisfies the identical equation by EL5. Consequently \((L-L_*)/\alpha\) is constant in \(\alpha>0\). The limit at zero alone would not determine that constant. We determine it at large \(\alpha\).

Put \(s=\kappa^2\). Expansion of the defining integrands by the binomial series near zero, with its uniformly convergent remainder, gives
\[
 K=\frac\pi2(1+s/4+9s^2/64+O(s^3)),\quad
 E=\frac\pi2(1-s/4-3s^2/64+O(s^3)),
\]
\[
 r=1-s/2-s^2/8+O(s^3),\quad
 E-rK=\frac\pi{32}s^2+O(s^3),\quad
 \alpha=\frac{32}{s^2}(1+O(s)).
 \tag{EL10}
\]
Thus \(u,v\) are both comparable to \(\alpha\), and the support bounds imply
\(2\log u\le L\le2\log v\), so \(L=O(\log\alpha)\). Also
\[
 \frac{w^2}{z}=\frac{(1+r)^2}{4r}
 =1+\frac{(1-r)^2}{4r}=1+O(1/\alpha).
\]
Therefore \(L_*=2\log w+\alpha\log(w^2/z)-2=O(\log\alpha)\). Their difference divided by \(\alpha\) tends to zero. Its constant value is zero, proving EL3 for every \(\alpha,\beta>0\). This fixes the integration constant rather than selecting it from a desired kernel value.

## EL4. Exact return to the diagonal Gamma coefficient

The original diagonal uses \(\alpha=2,\beta=\pi\). Equations EL1–4 give
\[
 uK=2,\quad vE=4,\quad
 L(2,\pi)=6\log w-2\log z-2,
 \quad\ell=8-4\log w-2\log c.
 \tag{EL11}
\]
The retained monic profile has \(\psi(1)=2-2\log2-\ell/4\); hence it is exactly
\(\psi(1)=\log(w\sqrt c/4)\). The full diagonal expression proved in PJ50 is
\[
 \beta_{\rm diag}=2\log(4/\pi)-2\psi(1)+L(2,\pi)+2-4\log2.
\]
Substitution of EL11, with every constant kept, proves
\[
 \beta_{\rm diag}=2\log\frac{4w^2}{\pi z\sqrt c}
 =2\log\frac{E(\kappa)(1+r)^2}{2\pi r\kappa}
 =\frac{C_\partial}{2}.
 \tag{EL12}
\]
The last equality is the original coefficient definition in the supplied kernel manuscript (8.1). The middle equality uses precisely \(v=4/E\), \(u=rv\), \(w=2(1+r)/E\), \(z=16r/E^2\), \(\sqrt c=2\kappa/E\). It therefore proves the connection between the logarithmic zero statistic and that earlier constant. No arithmetic rank has been used to infer it.

## EL5. Reproducible interval arithmetic

The companion `root_checks/check_constant_interval.py` uses integer intervals with denominator \(10^{90}\). Addition and subtraction are exact endpoint operations; multiplication and division use floor and ceiling integer divisions; square roots use integer square roots. Its elliptic coefficients obey
\[
 a_0=1,\qquad a_{j+1}/a_j=((2j+1)/(2j+2))^2,
\]
\[
 2K/\pi=\sum_{j\ge0}a_j(1-r^2)^j,\qquad
 2E/\pi=1-\sum_{j\ge1}\frac{a_j(1-r^2)^j}{2j-1}.
 \tag{EL13}
\]
The defining integral and the binomial series prove both identities. Since \(a_j\) decreases, after degree \(N\) the first tail is at most the next term divided by \(r^2\), and the second tail is at most that bound divided by \(2N+1\). The equation \(E-2rK=0\) is tested with \(N=4096\). After enclosing its signs at the supplied decimal endpoints, 90 integer bisections shrink the root interval. Strict increase of \(\alpha(r)\) in EL7 proves uniqueness at \(\alpha=2\).

The coefficient is computed without a numerical value for \(\pi\), because \(E/\pi=(2E/\pi)/2\) cancels it in EL12. The logarithm is enclosed by \(\log x=2\sum_{j\ge0}t^{2j+1}/(2j+1)\), \(t=(x-1)/(x+1)\), using 110 terms and tail at most \(2t^{221}/[221(1-t^2)]\). Integration of the finite geometric series proves this remainder. The resulting outward interval certifies
\[
 \boxed{10.83425590260233706<8C_\partial<10.83425590260233707.}
 \tag{EL14}
\]
The full 90-digit endpoints are saved in the accompanying JSON. This is a certificate for the universal equilibrium coefficient. It evaluates neither a hypothetical off-line zeta zero nor an original arithmetic period.

## Sources and reading coverage

The exact equilibrium measure, global Euler inequality, parameter regularity and variational derivative are proved in the retained [EIQ1–33 source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9104d852c6bc5b79e6fc4588c403128a40b7fda3/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/RETAINED_COMPLETE_PROOF_SOURCES.tex#L4384), especially EIQ26 at line4697, EIQ29–30 at lines4760–4785 and EIQ31–33 at lines4800–4821. Those complete proof bodies were read for this calculation. The present endpoint formula EL3 is derived above, rather than attributed to that earlier integral formula.

B. C. Carlson, [DLMF Chapter19, Elliptic Integrals](https://dlmf.nist.gov/19), Sections19.4–19.5, is the human reference for the elliptic derivatives and expansions. The current equation-TeX fetch returned HTTP403 and is recorded as unavailable; no downloaded source is claimed. EL6 and EL10–13 include the elementary derivations used here. The publication source must retain this distinction between the human reference and the newly written proof.
