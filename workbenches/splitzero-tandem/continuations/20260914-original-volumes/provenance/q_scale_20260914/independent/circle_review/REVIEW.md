# Independent circle-smearing and stratified-cell review

Date: 2026-09-14. Reviewer: `circle_bound_review`.

Scope: complete independent verification of the proposed quantitative partition-function argument, including the later stratified-cell lower bound. This review does not certify a parent manuscript that has not yet been read. The reviewed input equilibrium source was read in full:

`equilibrium/independent/EXACT_SQRT_LOG_EQUILIBRIUM.tex`

SHA256: `a0a0346a19d0e035a186590dbd69881cdf7a30e8fef602d47bba0932f175e731`.

Verdict: the proposed argument is valid. The stratified lower bound improves the initial independent-identically-distributed lower bound and yields a uniform **O(n)** remainder for the Heine partition function, with both specified base measures. All circle coefficients and signs are as proposed. Details follow so the review is independently checkable.

## 1. Conventions, original domain, and equilibrium data

For positive parameters alpha and beta, retain the original domain x>0 and potential

\[
 V(x)=\beta\sqrt{x}-\alpha\log x.
\]

Let mu(dx)=rho(x)dx be the exact probability measure of EIQ11, supported on [a,b] with 0<a<b and rho positive on (a,b). Write

\[
 I(\eta,\zeta)=\iint\log|z-w|\,d\eta(z)d\zeta(w),\qquad I(\eta)=I(\eta,\eta),
\]

where the real line is included in the complex plane by x -> x+0i. Define

\[
 L_\mu(z)=\int\log|z-t|\,d\mu(t),\quad
 F=I(\mu)-\int V\,d\mu,\quad
 D(x)=V(x)-2L_\mu(x)-\ell.
\]

EIQ17--19 prove D>=0 on the entire original domain x>0 and D=0 on [a,b]. Integrating the equality on the support proves the exact identity

\[
 F=-I(\mu)-\ell. \tag{CR1}
\]

For a positive measure lambda on (0,infinity), distinguish the two actual objects

\[
 Z_{n,\lambda}=\int_{(0,\infty)^n}\exp H_n(x_1,\ldots,x_n)\prod_{i=1}^n d\lambda(x_i),
\]
\[
 H_n=2\sum_{i<j}\log|x_i-x_j|-n\sum_{i=1}^n V(x_i),\qquad
 J_{n,\lambda}=Z_{n,\lambda}/n! . \tag{CR2}
\]

The collision value exp(H_n)=0 is retained. The initial proposal without the factorial concerned Z; the strengthened statement below concerns J. The exact relation log Z=log J+log(n!) retains this change of convention.

The two base measures reviewed are

\[
 d\lambda(x)=dx,\qquad
 d\omega(x)=w(x)dx,\quad w(x)=\tfrac12x^{-1/2}e^{-\sqrt x}.
\]

The substitution x=s^2, dx=2s ds, proves that omega has total mass 1, with all factors included.

## 2. Circle potential and absolute integrability

For each real x and epsilon>0, let c_(x,epsilon) be the pushforward of dtheta/(2pi) on [0,2pi) under theta -> x+epsilon exp(i theta). Its potential is exactly

\[
 \int\log|z-u|\,dc_{x,\varepsilon}(u)
       =\log\max\{\varepsilon,|z-x|\}. \tag{CR3}
\]

For |z-x|<epsilon and |z-x|>epsilon this follows by factoring out the larger radius and integrating the absolutely convergent real part of the series for log(1-q exp(i theta)), |q|<1. At equality of the radii, the integrand is log epsilon+log(2|sin(theta/2)|). Its absolute integrability follows from sin(theta/2) comparable to theta near zero and 2pi-theta near 2pi. Its mean is log epsilon: the elementary identity integral_0^pi log(sin u)du=-pi log2 follows by putting A=integral_0^(pi/2) log(sin u)du=integral_0^(pi/2) log(cos u)du, applying sin(2u)=2sin u cos u, and substituting v=2u. Consequently integral_0^(2pi) log(2|sin(theta/2)|)dtheta=0. This also establishes CR3 on the circle.

All logarithmic energies used here are absolutely integrable, including for coincident or tangent circles. An explicit local bound proves this without a formal appeal to a finite signed integral. Put r=|z-x|. If r<=epsilon/2, then |z-x-epsilon exp(i theta)|>=epsilon/2. If r>=2epsilon, the distance is at least epsilon. In the remaining range epsilon/2<=r<=2epsilon, rotate the angle and use

\[
 |r-\varepsilon e^{i\theta}|^2
 =(r-\varepsilon)^2+4r\varepsilon\sin^2(\theta/2)
 \ge 2\varepsilon^2\sin^2(\theta/2).
\]

Thus the circle average of the negative part of the logarithm is bounded uniformly in z by a finite number depending on epsilon. On any compact set its positive part is bounded as well. This proves absolute integrability of every circle-circle energy by Fubini. For a circle and mu, the negative part can also be bounded using

\[
 \log^-|z-t|\le\log^-|\operatorname{Re}z-t|,\qquad
 \int\log^-|u-t|\rho(t)dt\le 2M,
\]

where M is any bound for rho and integral_(-1)^1 -log|s| ds=2. The same estimate handles mu against itself. The positive parts are bounded on the compact supports. These arguments apply to every finite configuration x_1,...,x_n, even if its maximum is arbitrarily large.

Applying CR3 twice gives

\[
 I(c_{x,\varepsilon})=\log\varepsilon,
\]
\[
 I(c_{x,\varepsilon},c_{y,\varepsilon})
 =\int\log\max\{\varepsilon,|x-y+\varepsilon e^{i\theta}|\}\frac{d\theta}{2\pi}
 \ge\log\max\{\varepsilon,|x-y|\}\ge\log|x-y|. \tag{CR4}
\]

The final right side is minus infinity when x=y, so the comparison remains valid; the left side is finite even then. Tangency also causes no exceptional term.

## 3. The required planar signed-energy inequality

Let nu=(1/n) sum_i c_(x_i,epsilon), and Delta=nu-mu, considered as signed measures on R^2. It has total mass zero. The preceding absolute-integrability estimates apply to |Delta| tensor |Delta| because |Delta|<=nu+mu. The scalar identity EIQ20 applies to Euclidean distance in R^2 without changing its factor 1/2. On every truncated t-interval its integrand has a constant sign for a fixed distance and its absolute integral is at most |log distance|. Dominated convergence for the finite signed product measure therefore gives

\[
 -I(\Delta)=\frac12\int_0^\infty\frac1t
       \iint e^{-t|z-w|^2}\,d\Delta(z)d\Delta(w)\,dt\ge0. \tag{CR5}
\]

The sign is proved by the exact two-dimensional Gaussian Fourier identity

\[
 \iint e^{-t|z-w|^2}\,d\Delta(z)d\Delta(w)
 =\frac1{4\pi t}\int_{\mathbb R^2}
        e^{-|\xi|^2/(4t)}|\widehat\Delta(\xi)|^2d\xi\ge0.
\]

This follows by multiplying the two one-dimensional Gaussian identities in EIQ22; integration against the finite measures is absolutely convergent. No extension of V to the complex plane is used. The complex-plane construction changes only the comparison measures, with its inclusion map and probability weights specified above.

It follows that

\[
 I(\nu)\le 2I(\nu,\mu)-I(\mu). \tag{CR6}
\]

## 4. Upper bound with every coefficient retained

By CR3 and the density bound,

\[
 \int L_\mu(z)dc_{x,\varepsilon}(z)-L_\mu(x)
 =\int_{|t-x|<\varepsilon}\log\frac{\varepsilon}{|t-x|}\rho(t)dt
 \in[0,2M\varepsilon]. \tag{CR7}
\]

The constant is exactly M times integral_(-epsilon)^epsilon log(epsilon/|s|)ds=2M epsilon. CR4--7 now give, in order,

\[
 2\sum_{i<j}\log|x_i-x_j|\le n^2I(\nu)-n\log\varepsilon,
\]
\[
 H_n\le 2n\sum_iL_\mu(x_i)-n^2I(\mu)-n\sum_iV(x_i)
          -n\log\varepsilon+4Mn^2\varepsilon,
\]
\[
 H_n\le n^2F-n\sum_iD(x_i)-n\log\varepsilon+4Mn^2\varepsilon. \tag{CR8}
\]

Thus the proposed self-energy sign, the coefficient 4M, and the factor n multiplying each D are all correct. With epsilon=1/n and C_lambda=integral exp(-D)d lambda, positivity D>=0 and n>=1 give

\[
 \log J_{n,\lambda}
 \le n^2F+n\log n-\log(n!)+4Mn+n\log C_\lambda. \tag{CR9}
\]

For lambda=omega, C_omega<=1 since omega has mass 1. For lambda=dx, C_dx is finite and uniformly bounded on every compact positive parameter set, as proved in section 6 below. The elementary increasing-function integral estimate log(n!)>=integral_1^n log t dt=n log n-n+1 gives the explicit upper

\[
 \log J_{n,\lambda}\le n^2F+(4M+1+\log C_\lambda)n-1. \tag{CR10}
\]

Replacing log C_lambda by log^+ C_lambda yields a weaker upper with a manifestly nonnegative constant when desired.

## 5. Quantile-cell lower bound and the exact factorial

Let a=t_0<t_1<...<t_n=b be the unique quantiles with mu((t_(i-1),t_i))=1/n. Existence and uniqueness follow from continuity and strict positivity of rho on (a,b). Put I_i=(t_(i-1),t_i), Delta_i=t_i-t_(i-1)>0, and p_i=n mu restricted to I_i. Each p_i is a probability measure. It has bounded Lebesgue density n rho and finite logarithmic self and cross energies by the bounds in section 2. For either reviewed lambda, its density relative to lambda is positive almost everywhere under p_i and has finite entropy

\[
 \operatorname{Ent}_\lambda(p_i)=\int\log\frac{dp_i}{d\lambda}\,dp_i.
\]

Indeed rho log rho is absolutely integrable: its negative part integrates to at most (b-a)/e and its positive part to at most log^+ M. For omega, log w is bounded on [a,b], which proves the remaining assertion.

The n! coordinate permutations of I_1 times ... times I_n are pairwise disjoint. The integrand and base product measure in CR2 are symmetric, so their integrals are equal. Boundaries have zero lambda measure. Hence

\[
 J_{n,\lambda}\ge\int_{I_1\times\cdots\times I_n}e^{H_n}\prod_i d\lambda(x_i)
 =\mathbb E_{p_1\otimes\cdots\otimes p_n}
    \exp\!\left(H_n-\sum_i\log\frac{dp_i}{d\lambda}(x_i)\right). \tag{CR11}
\]

The equality uses that dp_i/dlambda is positive inside its open interval. Every summand inside the expectation is integrable, including cross energies of adjacent intervals. Jensen's inequality applies. Since sum_i p_i=n mu, the exact expected pair term is n^2 I(mu)-sum_i I(p_i), and the potential term is -n^2 integral V dmu. Therefore

\[
 \log J_{n,\lambda}\ge n^2F-\sum_iI(p_i)-\sum_i\operatorname{Ent}_\lambda(p_i). \tag{CR12}
\]

Retaining the quantile densities in the entropy sum gives

\[
 \sum_i\operatorname{Ent}_\lambda(p_i)
   =n\log n+n\operatorname{Ent}_\lambda(\mu). \tag{CR13}
\]

Within I_i, the distance is at most Delta_i. Consequently I(p_i)<=log Delta_i. Concavity of the logarithm and sum_i Delta_i=b-a give

\[
 \sum_i I(p_i)\le\sum_i\log\Delta_i
                  \le n\log\frac{b-a}{n}. \tag{CR14}
\]

Substituting CR13--14 proves exactly

\[
 \boxed{\quad
 \log J_{n,\lambda}\ge n^2F-n\bigl[\log(b-a)+\operatorname{Ent}_\lambda(\mu)\bigr].
 \quad} \tag{CR15}
\]

There is no additional factorial and no additional n log n in this inequality. The parent-supplied strengthened formula is accepted. For lambda=dx, log(b-a)+Ent_dx(mu)>=0 also follows from Jensen against the uniform probability density on [a,b], but this extra sign is not needed in the proof.

For comparison, the original iid-mu proof without stratification is valid and yields log Z>=n^2F-n[I(mu)+Ent_lambda(mu)]. It does not give CR15 after dividing by n!: its weaker log(n!) loss is precisely the term removed by the disjoint quantile-cell construction.

## 6. Uniformity for compact positive parameter sets

Let the parameter pair range over a fixed compact subset of (0,infinity)^2. EIQ3--6 and EIQ29 give constants 0<A<=a<b<=B<infinity and a uniform density bound M. One explicit bound follows from the first expression of EIQ10:

\[
 0<h(x)\le\frac{\alpha}{x\sqrt{ab}}\le\frac{\alpha_{\max}}{A^2},
 \qquad
 \rho(x)\le\frac{B\alpha_{\max}}{4\pi A^2}.
\]

The endpoint functions are continuous and b-a>0, so their width also has a positive lower bound on the compact parameter set. The logarithmic energy obeys

\[
 \iint|\log|x-y||d\mu(x)d\mu(y)\le2M+\log(1+B).
\]

The potential is uniformly bounded on [A,B]. Thus ell=integral V dmu-2I(mu) has a uniform absolute bound. Furthermore

\[
 |\operatorname{Ent}_{dx}(\mu)|\le B/e+\log^+ M,
\]

and |Ent_omega(mu)| is uniformly bounded because

\[
 \log w(x)=-\log2-\tfrac12\log x-\sqrt x
\]

is uniformly bounded on [A,B]. The entire lower constant in CR15 is therefore uniform.

For the Lebesgue upper integral, t in [a,b] implies

\[
 \log|x-t|\le\log(1+x)+\log(1+B).
\]

Writing ell_max for a uniform upper bound for ell and beta_min, alpha_min, alpha_max for the positive parameter bounds yields

\[
 e^{-D(x)}\le e^{\ell_{\max}}(1+B)^2(1+x)^2e^{-\beta_{\min}\sqrt x}
 \begin{cases}x^{\alpha_{\min}},&0<x\le1,\\x^{\alpha_{\max}},&x\ge1.\end{cases} \tag{CR16}
\]

The majorant is integrable at zero since alpha_min>0 and at infinity by the substitution x=s^2. Hence C_dx has a finite uniform upper bound. This proves the desired parameter uniformity without discarding either original endpoint.

Combining CR10 and CR15 proves

\[
 \boxed{\log J_{n,\lambda}=n^2F+O(n)}
\]

uniformly for both reviewed lambda and every fixed compact positive parameter set. The equivalent labelled-integral statement is

\[
 \boxed{\log Z_{n,\lambda}=n^2F+\log(n!)+O(n)}.
\]

No bound on finite differences of the O(n) remainder is claimed here. Any later differentiated or neighbouring-parameter estimate must retain this uniform error and derive its own consequence explicitly.

## 7. Final actual-source review of QLG1--32

The complete actual provider was subsequently read, including every displayed equation and every intervening proof:

`q_scale_20260914/independent/QUANTITATIVE_LOG_GAS_PARTITION.tex`

Final accepted SHA256: `52256dd3671db7944c6758ed8a2f7129b7a226a08c433b1f32449985f2137b71`.

The first full read had SHA256 `da2798bd5318a2e819d201693882355d995ce8a5f35399cc77bbeada02a78e85`. The provider then corrected the single LaTeX spacing typo `\int Vp_j,dx` to `\int Vp_j\,dx`. I verified that reversing exactly this replacement in the final bytes reproduces the earlier hash. Thus the final accepted version differs from the fully read version by exactly that checked spacing correction, with no unreviewed mathematical changes.

**Final verdict: ACCEPTED. No mathematical correction is required.** In particular, the finite constants work on the entire displayed rectangle

\[
 \mathcal K=[3/2,5/2]\times[\pi/2,3\pi/2],
\]

including its boundary. This acceptance concerns the actual QLG source and its full proof, superseding the earlier scope limitation that only the proposal had been reviewed.

The equation-by-equation checks are as follows.

1. **QLG1--7:** the density is exactly EIQ10--11 with coefficient beta/(4 pi^2 x); it has the previously proved mass and support. The signs in D, ell, and F agree with CR1. Both base measures, the positive half-line, exponent nV, Vandermonde exponent 2, and Heine factor 1/n! are retained. The substitution x=r^2 gives omega mass 1 exactly.

2. **QLG8:** endpoint continuity and positivity from EIQ3--6 on the compact displayed rectangle prove a_*>0 and B_*<infinity. The extrema define exact constants through the already uniquely specified endpoint integrals. No unstated uniform equilibrium existence assertion enters here.

3. **QLG9:** since x,a,b>=a_*, the auxiliary denominator is at least (a_*+s)^2. Directly,

   \[
   \int_0^\infty\frac{\sqrt s}{(a_*+s)^2}ds
    =\frac2{\sqrt{a_*}}\int_0^\infty\frac{r^2}{(1+r^2)^2}dr
    =\frac\pi{2\sqrt{a_*}}.
   \]

   Multiplying this by beta_+/(4 pi^2 a_*) and by the upper square-root endpoint factor B_*/2 gives precisely

   \[
    M_* = \frac{\beta_+B_*}{16\pi a_*^{3/2}}.
   \]

   The inequality B_* M_*>=1 follows from the integral of the density on its support of length at most B_*.

4. **QLG10--11:** entropy absolute integrability follows from the continuous extension of u|log u| at zero and bounded log w on [a_*,B_*]. The upper bound H_0<=log M_* follows by multiplying log rho<=log M_* by rho and using its mass. For omega, the exact additional term is log 2+(1/2)log x+sqrt x, an increasing function on x>0, so its upper bound at B_* is the one displayed. This remains correct when B_* or M_* is below 1; replacing their logarithms by positive parts is not needed for these inequalities.

5. **QLG12--13:** D>=0 and omega mass 1 give 0<T_omega<=1. The positive-logarithm bound for P is valid on the full original positive half-line; P>=-2M_* follows from the uniform negative-logarithm integral. Consequently ell<=L_* with the displayed +4M_* term. In the Lebesgue integral, e^(-D)=e^ell e^(2P) x^alpha e^(-beta sqrt x). Substituting the stated bounds and x^alpha<=1+x^(5/2) produces exactly T_*, with its factor e^(L_*)(1+B_*)^2 and no omitted Jacobian.

6. **QLG14:** after x=r^2, the entire polynomial in the remaining integral is

   \[
     2r(1+r^2)^2(1+r^5)
       =2(r+2r^3+r^5+r^6+2r^8+r^{10}).
   \]

   Integrating each monomial against exp(-beta_- r) gives the factorials 1!, 2 times 3!, 5!, 6!, 2 times 8!, 10!, with denominator exponents respectively 2,4,6,7,9,11. These agree with every term in QLG14.

7. **QLG15--18:** the signed-energy argument is valid on R^2 with the stated logarithmic integrability, zero mass, scalar factor 1/2, and Fourier factor 1/(4 pi t). The circle-potential identity includes points on the circle through the correctly derived sine integral. The source's shorter absolute-integrability argument is sufficient: on the compact second support the positive part of the first-circle integral is uniformly bounded, and its exact mean log max(epsilon,|x-w|) is bounded below by log epsilon. Thus the negative part's first-circle integral is uniformly bounded as well, justifying Tonelli and all double integrals even for coincident and tangent circles. The self term log epsilon and both cross inequalities are correct.

8. **QLG19--23:** the self-energy subtraction is -n log epsilon; the mean-potential lift is at most 2M_* epsilon; its double-potential contribution is +4M_* n^2 epsilon. The real-domain potential and D remain unchanged. Choosing epsilon=1/n yields QLG22. The factorial inequality, including equality at n=1, gives QLG23 with the final -1 retained. Finiteness of the original integral follows from these proved upper bounds.

9. **QLG24--28:** strict interior positivity gives unique quantiles and positive cell widths. Bounded cell densities and compact support justify every self, cross, and entropy expectation. The n! disjoint coordinate-permuted cells exactly cancel the Heine factor. The expectation of the full original pair and potential exponent is n^2F minus the sum of the cell self energies. The entropy sum is n log n+nH_lambda(mu), and concavity gives the cell-energy bound n log((b-a)/n). Their n log n terms cancel with the displayed signs. This proves QLG28, including strict positivity, for n=1 as well as for larger n.

10. **QLG29--31:** these are the correct finite and uniform consequences. Since log(b-a)+H_lambda(mu)<=L_lambda, the lower bound is at least -nL_lambda. The maxima defining C_0 and C_omega include L_lambda, zero, and the correct upper constant. For lambda_0, log T_lambda<=log T_*<=log^+ T_*; for omega, log T_lambda<=0. The -1 in QLG23 can be dropped for the upper absolute-value estimate. It follows exactly that |log J_n^lambda-n^2F|<=C_lambda n on the whole rectangle. A potentially negative L_omega creates no defect because of the displayed maximum, and would simply strengthen the finite lower bound.

11. **QLG32:** retaining log Z=log J+log(n!) gives its first bound exactly. Since 0<=log(n!)<=n log n for n>=1, its second bound follows by the triangle inequality. No n! or density factor is incorporated into F.

All proof steps in the final QLG provider are covered above. This review establishes the advertised finite-n partition theorem. It does not claim a derivative bound for its O(n) remainder, a finer partition expansion, or a subsequent estimate not present in QLG1--32.
