# The Gamma-power profile at every original cutoff

Independent derivation for the 025 continuation. The unchanged finite Gamma estimates from [024 PJ1–PJ44](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/POWER_JET_PROOF.md) and the original-source return [CK5–CK11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md) are retained. Their source mass, root-gap constants, arithmetic data, and complete minima are not altered. This proof extends their parameter range and supplies the moving-potential argument needed for the new uniform cutoff conclusion.

## PP1. Original Gamma objects and exact parity

Keep
\[
d\sigma(y)=w(y)dy=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}dy,
\quad \sigma(\mathbb R)=\sqrt{2\pi},
\quad d\nu_n=|y|^{2n}d\sigma,
\quad d_n=\int d\nu_n.
\tag{PP1}
\]
Let \(U_j^{[n]}\) be the monic orthogonal polynomial for \(\nu_n\), let \(h_j^{[n]}=\|U_j^{[n]}\|_{\nu_n}^2\), and let \(\mathsf K_{n,M}\) be the complete polynomial reproducing kernel through degree \(M\). Define the actual scalar
\[
F_n(M)=\log[d_n\mathsf K_{n,M}(0,0)].
\tag{PP2}
\]
Since the constant polynomial has norm squared \(d_n\), \(F_n(0)=0\). Positivity of the kernel sum makes \(F_n(M)\) nonnegative and nondecreasing in \(M\).

For \(n\ge36\), the accepted PJ16 and PJ18, including the last raising degree, give fixed \(0<c\le1\le C\) such that
\[
cn\|P\|_{\nu_n}\le\|yP\|_{\nu_n}\le Cn\|P\|_{\nu_n}
\quad(\deg P\le2n+1),
\tag{PP3}
\]
and all nonzero roots of the used \(U_j^{[n]}\), \(j\le2n+2\), lie in
\([-Cn,-cn]\cup[cn,Cn]\). The odd zero at zero is simple and is retained separately. The constants arise from the complete two-half-line Laguerre comparison and its near-zero correction in PJ6–PJ16; no pointwise lower Gamma comparison at zero is used.

For even \(M=2h\), the monic Christoffel–Darboux identity gives
\[
F_n(M)=\log d_n+2\log|U_M^{[n]}(0)|-\log h_M^{[n]}+\log D_{n,M},
\quad D_{n,M}=\frac{(U_{M+1}^{[n]})'(0)}{U_M^{[n]}(0)}.
\tag{PP4}
\]
For \(h\ge1\), the positive roots interlace as
\(0<a_1<b_1<a_2<b_2<\cdots<a_h<b_h\). Hence
\[
1\le D_{n,M}=\prod_{i=1}^h\frac{b_i^2}{a_i^2}
\le\frac{b_h^2}{a_1^2}\le(C/c)^2.
\tag{PP5}
\]
The middle inequality uses \(b_i<a_{i+1}\), so it telescopes. For \(M=0\), \(U_0=1\), \(U_1=y\), and \(D_{n,0}=1\) exactly. For odd \(M\), parity gives the exact same-measure identity
\[
F_n(M)=F_n(M-1).
\tag{PP6}
\]
No change of the power \(n\) is needed for this parity step.

## PP2. Uniform monic norms at positive degree/power ratios

Fix a compact interval \(I=[a_*,b_*]\subset(0,3/2]\). Here \(a_*,b_*\) are ratio bounds, not equilibrium endpoints. Let \(M=2h\) and \(\tau=M/n\in I\). The exact coordinate map is
\[
U_M^{[n]}(y)=n^Mp_h(y^2/n^2),\qquad p_h\text{ monic of degree }h.
\tag{PP7}
\]
Reflection and uniqueness give the parity of the original minimizer, and substituting every even test monomial shows that \(p_h\) is the monic orthogonal polynomial for the full pushforward
\[
d\eta_n(x)=n^{2n+1}x^{n-1/2}w(n\sqrt x)dx,\qquad x>0.
\tag{PP8}
\]
Both real half-lines contribute to this formula. Consequently
\[
h_M^{[n]}=n^{2(n+M)+1}
\min_{\substack{p\text{ monic}\\ \deg p=h}}\int_0^\infty
x^{n-1/2}|p(x)|^2w(n\sqrt x)dx.
\tag{PP9}
\]

The varying potential is exactly
\[
V_\tau(x)=\frac\pi\tau\sqrt x-\frac2\tau\log x,
\qquad hV_\tau(x)=\frac{\pi n}{2}\sqrt x-n\log x.
\tag{PP10}
\]
Use the already proved EIQ family at \((\alpha,\beta)=(2/\tau,\pi/\tau)\). Its probability \(\mu_\tau\) has support \([u_\tau^2,v_\tau^2]\), with
\(u_\tau K(\kappa_\tau)=2\), \(v_\tau E(\kappa_\tau)=2(1+\tau)\), and \(\kappa_\tau^2=1-u_\tau^2/v_\tau^2\). Its Euler constant and logarithmic moment are denoted by \(\lambda_\tau\) and \(L_\tau\). In particular,
\[
V_\tau(x)-2\int\log|x-z|d\mu_\tau(z)
=\lambda_\tau\text{ on its support},
\quad\ge\lambda_\tau\text{ on }(0,\infty).
\tag{PP11}
\]
The parameter continuity proved in EIQ29 puts all these supports inside one compact interval separated from zero, with lengths bounded below. The positive prefactor in EIQ10–EIQ11 is continuous and bounded above and below there. Thus their densities are uniformly bounded and their square-root endpoint entropy integrals are uniformly finite. The constants \(\lambda_\tau\) are bounded on \(I\).

We spell out why the monic argument is uniform rather than applying only its diagonal conclusion. On the support, Jensen against its arcsine probability bounds every monic degree-\(h\) polynomial below by
\(c_Ie^{-h\lambda_\tau}\) in the weight \(e^{-hV_\tau}x^{-3/4}dx\). Indeed the logarithmic potential of that arcsine probability is its log capacity on the interval and no smaller at any complex root; averaging (PP11) against it gives the exact Euler constant. The entropy integral of \(x^{-3/4}\) against the arcsine density is bounded below uniformly because the endpoints stay separated from zero and their distance stays bounded above and below. This lower bound uses only the equilibrium interval.

For the upper bound, choose the \(h\) midpoint quantiles of \(\mu_\tau\) as zeros. Their distribution functions have discrepancy at most \(1/(2h)\). On any fixed bounded \(x\)-interval containing the supports, truncation of \(\log|x-z|\) at distance \(1/h\) has variation \(O_I(\log(h+2))\), and the bounded equilibrium density makes its integral truncation error \(O_I(1/h)\). The integration-by-parts formula for a function of bounded variation against the distribution-function difference therefore gives
\[
\log|p_h(x)|\le h\int\log|x-z|d\mu_\tau(z)+C_I\log(h+2).
\]
Using (PP11), its full bounded-region integral is at most
\(C_I(h+2)^{C_I}e^{-h\lambda_\tau}\), because \(x^{-3/4}\) is integrable at zero. For a sufficiently large common \(B\), all roots are in \((0,B/2)\), and \(|p_h(x)|\le x^h\) for \(x\ge B\). Uniformly over \(\tau\in I\),
\[
(2+2/\tau)\log x-(\pi/\tau)\sqrt x
\le-\lambda_\tau-c_I\sqrt x\qquad(x\ge B).
\]
This follows from \(\log x/\sqrt x\to0\), the bounded \(\lambda_\tau\), and the positive lower bound for \(\pi/\tau\). It bounds the remaining tail integral by a fixed multiple of \(e^{-h\lambda_\tau}\). Thus both ends of the actual integration domain are included.

PJ13 supplies fixed constants \(A,B_0>0\) such that
\[
w(y)\le B_0|y|^{-1/2}e^{-\pi|y|/2}\quad(y\ne0),
\qquad
w(y)\ge A|y|^{-1/2}e^{-\pi|y|/2}\quad(|y|\ge1).
\tag{PP12}
\]
The lower bound applies on every equilibrium interval once \(n\) is large, uniformly over \(I\). Substituting (PP12) in (PP9), the full scale factor is \(n^{2(n+M)+1/2}\), and the remaining weight is exactly \(e^{-hV_\tau}x^{-3/4}dx\). Applying the interval lower bound and the global upper trial just proved gives
\[
\boxed{\log h_M^{[n]}=[2(n+M)+\tfrac12]\log n
-\tfrac M2\lambda_\tau+O_I(\log(n+2)).}
\tag{PP13}
\]
This proves CP17 on its stated compact positive ratio range. It is not applied to \(M/n\to0\). The original mass calculation, unchanged from PJ49, gives
\[
\log d_n=2n\log n+a_dn+r_d(n),\qquad
a_d=2\log(4/\pi)-2,
\quad r_d(n)=O(\log(n+2)).
\tag{PP14}
\]

## PP3. Moving-potential zero statistics on the unbounded domain

Let \(n\to\infty\), \(M=2h\), and \(\tau=M/n\to t\in(0,3/2]\). By PP1 the zeros of \(p_h\) from (PP7) lie in the fixed interval \([c^2,C^2]\). This uses the actual degree \(M+1\le3n/2+1<2n+2\) in the original root-gap bound.

For a positive measure \(\zeta\), let \(D_h(\zeta)\) be its monomial Gram determinant through degree \(h-1\). The exact identities from PJ62 and PJ67 are
\[
D_h(\zeta)=\frac1{h!}\int\prod_{i<j}(x_i-x_j)^2\prod_i d\zeta(x_i),
\tag{PP15}
\]
\[
(-1)^hp_h(-A)=\frac{D_h((A+x)\eta_n)}{D_h(\eta_n)}\quad(A>0).
\tag{PP16}
\]
They follow by expansion of the two Vandermonde determinants and of the monic moment determinant; in particular they retain the full measure factor. Set
\[
\phi(x)=\log(A+x),\quad f_n(z)=\log D_h((A+x)^z\eta_n),
\quad \kappa_n=n^{2n+1/2},
\]
\[
\mathcal F_t(\chi)=\sup_\pi
\left\{\iint\log|x-y|d\pi^2-\int V_t d\pi+\chi\int\phi d\pi\right\}.
\tag{PP17}
\]
The supremum is defined by its bounded-above energy kernel on probabilities on \((0,\infty)\). We prove for the actual moving sequence
\[
\limsup\frac{f_n(h\chi)-h\log\kappa_n}{h^2}
\le\mathcal F_t(\chi),\qquad
\liminf\frac{f_n(0)-h\log\kappa_n}{h^2}
\ge\mathcal F_t(0).
\tag{PP18}
\]

For the upper bound, (PP12) gives globally
\(d\eta_n\le B_0\kappa_n e^{-hV_\tau(x)}x^{-3/4}dx\). Use the probability
\(d\omega_0=(2\sqrt\pi)^{-1}x^{-3/4}e^{-\sqrt x}dx\). Put
\(Q_{\tau,\chi}=V_\tau-\chi\phi\) and
\(K_{\tau,\chi}(x,y)=\log|x-y|-[Q_{\tau,\chi}(x)+Q_{\tau,\chi}(y)]/2\).
The exponent in (PP15) is exactly
\[
\sum_{i\ne j}K_{\tau,\chi}(x_i,x_j)
+\sum_i[\sqrt{x_i}-Q_{\tau,\chi}(x_i)].
\tag{PP19}
\]
The latter summand is bounded above uniformly for \(\tau\) in a compact positive neighborhood of \(t\) within \((0,3/2]\), and \(\chi\) in a fixed small interval. Its square-root coefficient at infinity is at most \(1-2\pi/3<0\); at zero the logarithmic barrier has a uniformly positive coefficient. The factorial and constant prefactors cost only \(O(h\log(h+2))\).

Here is an explicit bound for the moving potential before compactification. Let
\(H(x)=1+\sqrt x+|\log x|\). Then
\[
|V_\tau(x)-V_t(x)|\le e_nH(x),
\qquad e_n=(\pi+2)|1/\tau-1/t|\longrightarrow0.
\tag{PP20}
\]
For a fixed small \(e>0\), eventually
\(K_{\tau,\chi}\le K_{t,\chi}^{(e)}\), where
\(K_{t,\chi}^{(e)}=K_{t,\chi}+e[H(x)+H(y)]/2\).
Take \(e\) sufficiently small that this kernel still has strictly positive barriers at zero and infinity. Its truncation
\(\max(K_{t,\chi}^{(e)},-T)\) is continuous on the compact square obtained by adding zero and infinity. At each boundary and along the diagonal the untruncated kernel tends uniformly to minus infinity. For the empirical probability \(L_h\), omission of the diagonal therefore costs only \(T/h\):
\[
h^{-2}\sum_{i\ne j}K_{\tau,\chi}(x_i,x_j)
\le\iint\max(K_{t,\chi}^{(e)},-T)dL_h^2+T/h.
\]
Integrating against \(\omega_0^h\) bounds its exponential by the maximum of this continuous energy. Let first \(n\to\infty\), then \(T\to\infty\), then \(e\downarrow0\). These maxima decrease to \(\mathcal F_t(\chi)\). To justify both passages, choose maximizing probabilities on the compactification, take a weakly convergent subsequence, compare with every fixed continuous truncation, and only then let the truncation increase. The positive barriers are uniform for all the chosen \(e\), so a limiting boundary mass has energy minus infinity and cannot improve the finite test energy at \(\mu_t\). The kernels decrease pointwise when \(e\downarrow0\). This proves the first bound in (PP18) and gives the missing unbounded-domain justification for moving \(\tau\).

For the lower bound restrict every variable to the fixed support of \(\mu_t\), rather than moving the integration domain. The Gamma lower envelope holds there for all large \(n\). On this compact interval \(V_\tau-V_t\to0\) uniformly by (PP20). Change the measure in (PP15) to \(\mu_t^{\otimes h}\) and apply Jensen. The exponent is
\[
h\log\kappa_n+h(h-1)\iint\log|x-y|d\mu_t^2
-h^2\int V_t d\mu_t+o(h^2)+O(h)-\log(h!).
\]
The entropy integral is finite because the density has the proved square-root endpoints with a positive bounded factor, and this interval is separated from zero. EIQ uniqueness identifies its energy as \(\mathcal F_t(0)\). This proves the second bound in (PP18); the upper bound at zero gives a limit there.

For completeness, the differentiability used next is a property of the variational value, not of an asymptotic remainder. Uniformly for small \(\chi\),
\(K_{t,\chi}\le C_0-c_0[H(x)+H(y)]\) after adjusting the fixed constant. Maximizers exist by the same compactification argument, and testing on \(\mu_t\) bounds their \(H\)-moments. Their \(\phi\)-integrals are uniformly integrable because \(\phi\) is bounded at zero and \(\phi(x)/\sqrt x\to0\) at infinity. Every limit of maximizers as \(\chi\to0\) maximizes the unperturbed energy, by its upper semicontinuity obtained through fixed truncated kernels. EIQ uniqueness forces that limit to be \(\mu_t\). Testing the two potentials on each other's maximizers bounds their secant by the corresponding two \(\phi\)-integrals. Hence
\[
\mathcal F_t'(0)=\int\log(A+x)d\mu_t(x).
\tag{PP21}
\]

Hölder's inequality in (PP15) makes \(f_n\) convex. For fixed \(\epsilon>0\) and \(h\epsilon\ge1\),
\[
\frac{f_n(0)-f_n(-h\epsilon)}{h^2\epsilon}
\le\frac{f_n(1)-f_n(0)}h
\le\frac{f_n(h\epsilon)-f_n(0)}{h^2\epsilon}.
\tag{PP22}
\]
The exact term \(h\log\kappa_n\) cancels. Apply (PP18) in its two stated directions, let \(n\to\infty\), and only then \(\epsilon\downarrow0\). Equations (PP16) and (PP21) show that the zero probability of \(p_h\) has limiting \(\log(A+x)\)-integrals equal to those of \(\mu_t\), for every \(A>0\). All its zeros lie in \([c^2,C^2]\). Every subsequential weak limit is therefore compactly supported. Expansion of \(\log(A+x)\) in powers of \(1/A\), for \(A\) larger than both supports, identifies every moment; polynomial approximation identifies the measures. Thus the zero probabilities converge to \(\mu_t\).

The original root gap makes \(\log x\) a bounded continuous test on their common compact support separated from zero. Since \(\mu_\tau\to\mu_t\) in this same regime, its logarithmic moments satisfy \(L_\tau\to L_t\). Restoring the exact factor \(n^M\) in (PP7) gives
\[
\boxed{\log|U_M^{[n]}(0)|=M\log n+\tfrac M2L_\tau+r_U(n,M),
\quad r_U(n,M)=o(n).}
\tag{PP23}
\]
This holds along every sequence with \(M/n\to t>0\) in the stated range. If the error were not uniform on a fixed compact positive ratio interval, choose a sequence violating uniformity, then take a convergent subsequence of its ratios. The just-proved sequential result contradicts the violation. This proves precisely the compact-positive uniformity claimed in CP22.

## PP4. The two-parameter scalar, with its exact finite remainder

For even \(M\), write the remainder in (PP13) as
\[
r_h(n,M)=\log h_M^{[n]}-[2(n+M)+\tfrac12]\log n+\tfrac M2\lambda_\tau.
\]
Then \(r_h=O_I(\log(n+2))\). Substitution of (PP13), (PP14), and (PP23) into (PP4) gives the exact identity
\[
\boxed{
F_n(M)-n\Phi(\tau)
=r_d(n)-r_h(n,M)+2r_U(n,M)-\tfrac12\log n+\log D_{n,M},
}
\tag{PP24}
\]
\[
\Phi(t)=2\log(4/\pi)-2+tL_t+\tfrac t2\lambda_t.
\tag{PP25}
\]
The term \(-\tfrac12\log n\) is retained here. The leading \(n\log n\) terms cancel; saying that every power of \(n\) cancels exactly would discard this finite term. It is part of the allowed \(O(\log n)+o(n)\) error, so it changes none of the proposed limits.

The general EL3–EL4 formulas, read in the retained024 proof, give the exact dictionary
\[
\Phi(t)=2\log(4/\pi)+2(1+t)\log w_t-2\log z_t-t\log c_t,
\]
where \(w_t=(u_t+v_t)/2\), \(z_t=u_tv_t\), and \(c_t=(v_t^2-u_t^2)/4\). Substituting the actual \(v_t=2(1+t)/E(\kappa_t)\), \(u_t=r_tv_t\), gives
\[
\Phi(t)=2\log\frac{E(\kappa_t)(1+r_t)^{1+t}}
{\pi(1+t)r_t\kappa_t^t}=\mathfrak J(t).
\tag{PP26}
\]
No arithmetic kernel coefficient enters this equality. The original elliptic equations make \(\mathfrak J\) continuous on \((0,3/2]\). At zero, the retained small-modulus expansions give
\(t=\kappa_t^4/16+O(\kappa_t^6)\), \(r_t\to1\), and \(t\log\kappa_t\to0\); hence the displayed quotient tends to one and \(\mathfrak J(t)\to0\). Set \(\mathfrak J(0)=0\).

Equations (PP5) and (PP24) prove uniform convergence on compact positive ratios for even degrees. For odd degrees use (PP6) and uniform continuity of \(\mathfrak J\); the argument is always in the same \(\nu_n\). To prove uniformity at residual degree zero, fix \(0<d<3/2\). For every \(M\le dn\), monotonicity gives
\[
0\le F_n(M)/n\le F_n(\lceil dn\rceil)/n
\longrightarrow\mathfrak J(d).
\tag{PP27}
\]
This also proves nonnegativity and monotonicity of \(\mathfrak J\) by taking fixed positive degree ratios and passing to the limit. Therefore \(0\le\mathfrak J(M/n)\le\mathfrak J(d)\), and
\[
\limsup_n\sup_{M\le dn}|F_n(M)/n-\mathfrak J(M/n)|
\le\mathfrak J(d).
\]
Let \(d\downarrow0\). Combining this with compact-positive convergence proves
\[
\boxed{\epsilon_n^G:={\max}_{0\le M\le\lfloor3n/2\rfloor}
|F_n(M)/n-\mathfrak J(M/n)|\longrightarrow0.}
\tag{PP28}
\]
This proves CP9, including \(M=0\), every finite odd degree, and every sequence with \(M/n\to0\). CP17 is only used where its compact-positive hypothesis holds.

The exact finite matrix for this scalar is also fixed. Put \(h=\lfloor M/2\rfloor\) and
\[
\mathcal A_{ab}=\frac{d_{n+a+b}}{n^{2(a+b)}},\quad0\le a,b\le h.
\tag{PP29}
\]
This is the full even coefficient Gram in the variable \(y^2/n^2\) and the literal \(\nu_n\). The odd block is orthogonal to it. Evaluation at zero gives
\(\mathsf K_{n,M}(0,0)=(\mathcal A^{-1})_{00}\), so
\(e^{F_n(M)}=d_n(\mathcal A^{-1})_{00}\).
Writing the same number as \(((\mathcal A/d_n)^{-1})_{00}\) is an exact matrix identity, not a change to the physical source measure. This is the universally computable scalar remainder in (PP28).

## PP5. Complete growing jets at every one of the original cutoffs

Retain \(q=(k+1)^2\ge40\), \(1\le s\le q/10\), \(n=q-s\),
\(N_j=q-1+j\), \(0\le j\le q+1\). The exact jet map is
\[
J_{q,s}P=(q^a[y^a]P)_{0\le a<s}.
\]
Multiplication by \(y^{q-s}\) is the original norm-preserving map from the \(\nu_n\) problem to the power-quotient fibre. Its permitted polynomial degree is exactly
\[
M_j=N_j-(q-s)=s+j-1.
\tag{PP30}
\]
Let \(H_j^{\rm pow}\) be its attained jet metric. The complete low coefficient estimate PJ19–PJ25 gives
\[
d_ne^{-E(q,s)}I\preceq H_0^{\rm pow}\preceq d_ne^{E(q,s)}I,
\quad E(q,s)=C_*[s\log(C_*q/s)+s+\log(q+2)].
\tag{PP31}
\]

For \(j\ge1\), the coefficient covariance is the full matrix \(J_{q,s}J_{q,s}^*=(H_j^{\rm pow})^{-1}\). The upper bound in PJ28–PJ30 uses the actual root products of every even and odd orthogonal polynomial through degree \(M_j\), and the complete derivative-evaluation norm on the odd sector. Since \(M_j\le q+s<3n/2\), the same binomial bounds and the same \(E(q,s)\) work simultaneously for every \(j\). They yield
\[
(H_j^{\rm pow})^{-1}\preceq e^{E(q,s)}\mathsf K_{n,s+j-1}(0,0)I.
\]

For the opposite inequality use the actual polynomial
\[
H(y)=\mathsf K_{n,j-1}(y,0)/\mathsf K_{n,j-1}(0,0),
\quad
\mathscr S_ja(y)=H(y)\left[\operatorname{rem}_{x^s}
\frac{a(x)}{H(qx)}\right]_{x=y/q}.
\tag{PP32}
\]
Its constant value is \(H(0)=1\), and its nonzero roots obey the same gap. Its squared norm is exactly \(1/\mathsf K_{n,j-1}(0,0)\). The reciprocal coefficients in (PP32) are bounded by the complete homogeneous products of inverse squared roots; their sum through degree \(s-1\) is at most \(\exp(E(q,s)/C)\) after enlarging the fixed constant. The truncated series multiplies back to the entire requested jet \(a\), so
\(J_{q,s}\mathscr S_j=I\) and
\(\deg\mathscr S_ja\le(j-1)+(s-1)=M_j-1\).
Repeated application of (PP3), with each original factor \(1/q\), controls every increasing degree, including the last raising step. Its highest degree is below \(M_j\le q+s<3n/2<2n+2\). Thus
\(\|\mathscr S_ja\|_{\nu_n}^2\le e^{E(q,s)}\|a\|_2^2/\mathsf K_{n,j-1}(0,0)\).
Taking the complete minimum proves
\[
\boxed{
e^{-E(q,s)}\mathsf K_{n,j-1}(0,0)I
\preceq(H_j^{\rm pow})^{-1}
\preceq e^{E(q,s)}\mathsf K_{n,s+j-1}(0,0)I,
\quad1\le j\le q+1.
}
\tag{PP33}
\]
For \(j=1\), the kernel polynomial in (PP32) is exactly \(H=1\); its reciprocal estimate and right inverse remain valid. For \(j=0\), use (PP31) and no negative-index kernel. This proves the entire degree range of CP26.

Combining (PP31) and (PP33) gives for every nonzero coefficient vector
\[
F_n(j-1)-2E(q,s)
\le\log\frac{a^*H_0^{\rm pow}a}{a^*H_j^{\rm pow}a}
\le F_n(s+j-1)+2E(q,s).
\tag{PP34}
\]
All matrices are complete attained minima, not diagonal row estimates.

Define on \([0,3/2]\) the exact modulus of continuity
\(\omega_{\mathfrak J}(h)=\sup_{|u-v|\le h}|\mathfrak J(u)-\mathfrak J(v)|\), and put \(J_* =\max_{[0,3/2]}\mathfrak J\). For \(1\le j\le q+1\) and \(M\in\{j-1,s+j-1\}\), direct subtraction of the two fractions gives
\[
|M/n-j/q|\le\frac{2s+2}{n}.
\]
All these ratios lie in \([0,3/2]\). Consequently the explicit scalar discrepancy in CP28 obeys
\[
V(q,s)\le\omega_{\mathfrak J}((2s+2)/n)+(s/q)J_*.
\tag{PP35}
\]
Using (PP28) at the two actual degrees in (PP34), we obtain the finite uniform estimate
\[
\boxed{
\sup_{0\le j\le q+1}\sup_{a\ne0}
\left|q^{-1}\log\frac{a^*H_0^{\rm pow}a}{a^*H_j^{\rm pow}a}
-\mathfrak J(j/q)\right|
\le\delta(q,s):=2E(q,s)/q+(n/q)\epsilon_n^G+V(q,s).
}
\tag{PP36}
\]
The \(j=0\) term is zero exactly. Since \(n\ge9q/10\), the right side tends to zero whenever \(s/q\to0\). For fixed \(s=\lfloor\epsilon q\rfloor\), (PP35) already gives an error tending to zero when the later limit \(\epsilon\downarrow0\) is taken. The explicit profile identity \(\mathfrak J'(t)=\log[(1+r_t)/(1-r_t)]\), proved by the companion endpoint calculation, makes \(\mathfrak J\) increasing and concave. Thus \(\omega_{\mathfrak J}(h)\le\mathfrak J(h)\), and its endpoint bound \(\mathfrak J(h)=O(h\log(C/h))\) yields the stated stronger estimate
\[
V(q,s)=O\big((s/q)\log(Cq/s)+\log(q+2)/q\big),
\quad
\limsup_{q\to\infty}\delta(q,\lfloor\epsilon q\rfloor)
=O(\epsilon\log(C/\epsilon)).
\tag{PP37}
\]
Uniform continuity alone suffices for the full convergence assertion; no microscopic derivative of a remainder is used.

## PP6. Original invariant constraints and all relative spectra

Keep the original conductor space \(\mathcal C_k\) and every original additional invariant row, denoted together by \(W_k\). The actual kernel is
\(K_k=\mathcal C_k\cap\ker W_k\), of rank \(m=8k-16\); it is the same coefficient space at every cutoff. The CK7 residue-error map has image dimension at most \(v_0+c_R\). On restricting that map to the already constrained kernel, its zero space \(G_k\) has actual codimension
\[
c=\operatorname{codim}_{K_k}G_k
\le\min(m,v_0+c_R).
\tag{PP38}
\]
This uses rank-nullity after restriction, so no condition on the rank of \(W_k\) is needed. In particular no invariant row is replaced by the conductor equation.

Fix \(0<\epsilon<1/10\), choose the CK8 decay exponent, and then a fixed admissible contour \(R\). Set \(s=\lfloor\epsilon q\rfloor\). CK8–CK11 supplies a single injective map
\(A_kp=P_{\ge q-s}U_Q^{-1}p\) from \(G_k\) to the power band, valid at every cutoff. Write \(\rho_k<1\) for its uniform relative norm error, tending exponentially to zero, and \(C_U\) for the squared-norm width in the full-fibre comparison. Explicitly,
\[
\|p-U_QA_kp\|_{G_{N_j}^\sigma}\le\rho_k\|p\|_{G_{N_j}^\sigma},
\quad
e^{-C_U}\|A_kp\|_{G_{N_j}^{\rm pow}}^2
\le\|U_QA_kp\|_{G_{N_j}^\sigma}^2
\le e^{C_U}\|A_kp\|_{G_{N_j}^{\rm pow}}^2.
\]
These estimates hold before and after the complete minimum because \(U_Q(y^qh)=Q_kh\) is an exact bijection between the whole fibres, with the original degree cutoff retained. The map is fixed in \(j\); its image need not be the whole power band or satisfy the invariant rows in those new coordinates. The vectors \(p\) on which the original metric is evaluated still lie in \(G_k\subset K_k\).

Triangle inequality bounds the difference of each pair of endpoint logarithms by
\(2C_U+2\log[(1+\rho_k)/(1-\rho_k)]\). Finally apply the original arithmetic–Gamma form comparison, with \(w_k=\log(u_k/\ell_k)\). It adds at most \(w_k\) to a logarithmic ratio. Therefore on the actual arithmetic good subspace, uniformly for all cutoffs,
\[
\left|\log\frac{\|p\|_{G_{N_0}}^2}{\|p\|_{G_{N_j}}^2}
-q\mathfrak J(j/q)\right|\le q\eta_{k,\epsilon},
\tag{PP39}
\]
\[
\eta_{k,\epsilon}=\delta(q,s)+
\frac{2C_U+2\log[(1+\rho_k)/(1-\rho_k)]+w_k}{q},
\quad
\limsup_k\eta_{k,\epsilon}=O(\epsilon\log(C/\epsilon)).
\tag{PP40}
\]
The constants retain the fixed original arithmetic data and period. This proves the finite content of CP32.

For \(i\le j\), subtract the two inequalities on the same nonzero \(p\). Put
\(d_{ij}=q[\mathfrak J(j/q)-\mathfrak J(i/q)]\). Then
\[
e^{d_{ij}-2q\eta}H_{G,N_j}
\preceq H_{G,N_i}\preceq e^{d_{ij}+2q\eta}H_{G,N_j}.
\tag{PP41}
\]
To relate this exact restriction to the full metric pair, choose any fixed frame inclusion \(I_G:\mathbb C^{m-c}\to\mathbb C^m\). Set
\[
B_{ij}=H_{K,N_j}^{-1/2}H_{K,N_i}H_{K,N_j}^{-1/2},
\quad V_j=H_{K,N_j}^{1/2}I_G(H_{G,N_j})^{-1/2}.
\]
Direct multiplication proves
\[
V_j^*V_j=I,\qquad
V_j^*B_{ij}V_j=(H_{G,N_j})^{-1/2}H_{G,N_i}(H_{G,N_j})^{-1/2}.
\tag{PP42}
\]
Thus the entire compression has spectrum in the interval of (PP41). If the full matrix had more than \(c\) eigenvalues strictly above its upper endpoint, their spectral space would intersect the \((m-c)\)-dimensional image of \(V_j\) nontrivially, contradicting its upper Rayleigh bound. The same argument for the lower endpoint gives at most \(c\) eigenvalues below it. Hence at most \(\min(m,2c)\) full relative eigenvalues are exceptional. No simultaneous diagonalization and no orientation of the invariant rows is assumed.

Nesting and CK5–CK3 give the common coarse bound
\[
0\le\log\lambda_a(B_{ij})\le4C_1q+w_k\le C_0q
\tag{PP43}
\]
for all large \(k\), all \(i\le j\), and every direction. The first inequality is the original source nesting. Also
\(0\le d_{ij}/q\le\mathfrak J(1+1/q)\). Consequently the complete finite bound is
\[
\boxed{
\Omega_{ij}:=\sum_{a=1}^m|\log\lambda_a(B_{ij})-d_{ij}|
\le2mq\eta_{k,\epsilon}
+2(v_0+c_R)q[C_0+\mathfrak J(1+1/q)].
}
\tag{PP44}
\]
One may replace the last \(2(v_0+c_R)\) by \(\min(m,2c)\). This proves CP33 with every original invariant constraint retained.

Take \(k\to\infty\) with \(\epsilon,R\) fixed. Then \(c_R\) is fixed and \(m=8k-16\to\infty\). Divide (PP44) by \(mq\), then let \(\epsilon\downarrow0\). This gives
\[
\boxed{\sup_{0\le i\le j\le q+1}\Omega_{ij}=o(mq).}
\tag{PP45}
\]
There is no simultaneous growing-contour substitution or exchange of these limits. Since the logarithm of a determinant ratio is the sum of the actual relative eigenvalue logarithms, (PP45) also proves the uniform determinant profile CP7. The same argument applies to every specified cutoff-independent subspace of \(\mathcal C_k\) whose actual rank tends to infinity: restrict the fixed residue-error map first, replace \(m\) by that rank, and keep the same finite codimension bound. Additional invariant rows can only reduce this restricted rank; they cannot increase it.

## PP7. Accepted scope and precise correction

CP9, CP17, CP22–CP33, and the resulting CP7–CP8 are established by PP1–PP45 on the retained original domain. The principal added analytic detail is (PP20): a uniform barrier envelope for the moving potentials on the full positive half-line, followed in the proved order by the compactified truncation limits. The small ratio endpoint uses exact monotonicity and parity, rather than evaluating a compact-positive asymptotic at zero. The literal finite scalar remainder includes \(-\tfrac12\log n\), as (PP24) records. No leading coefficient changes.

Human-source formula provenance is inherited from024: R. A. Askey and R. Roy for the original Gamma equations, and T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw for the original Laguerre and Christoffel–Darboux equations. The original equation TeX, hashes, and actual reading coverage are retained in024 SOURCE_READING_USE_LEDGER.json. No new external theorem, independent native-period computation, or current sign is asserted here.
