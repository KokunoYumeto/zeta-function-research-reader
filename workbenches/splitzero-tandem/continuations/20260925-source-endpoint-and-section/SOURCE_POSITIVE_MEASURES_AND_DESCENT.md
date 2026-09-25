# Positive measures on the complete source and exact descent through the original zeta ideal

25 September 2026. Independent derivation SPF0–SPF11. Inner products and Hermitian forms are linear in the first argument.

## SPF0. The prequotient source and the classification

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). The following coefficient spaces, numbers, arithmetic labels, linear operations and integrals occur after the complete arithmetic reconstruction. No coefficient value, addition, parity, coordinate or metric is assigned to \(\tau\). The original branch records remain separate.

Retain the complete Fréchet source before quotienting:
\[
\mathcal B=\{F\text{ entire}:b_{A,M}(F)=
\sup_{|\Re s|\le A}(1+|\Im s|)^M|F(s)|<\infty
\quad(A,M\in\mathbb Z_{\ge0})\},
\]
\[
T_aF(s)=a^sF(s),\qquad \mathsf U_n=nT_{1/n},
\quad a>0,\ n\ge1\text{ a recovered integer}.
\tag{SPF0.1}
\]
The factor \(n\) is the actual integer cover degree. General positive real \(a\) is a coefficient parameter; no fractional-degree cover is asserted.

**Classification.** All jointly continuous positive semidefinite Hermitian forms \(\mathfrak b\) on \(\mathcal B\) satisfying
\[
\mathfrak b(T_nF,G)=\mathfrak b(F,nT_{1/n}G)
\qquad(n\ge1)
\tag{SPF0.2}
\]
are exactly
\[
\boxed{\mathfrak b(F,G)=\int_{\mathbb R}
F(1/2+i\lambda)\overline{G(1/2+i\lambda)}\,d\mu(\lambda),}
\tag{SPF0.3}
\]
where \(\mu\) is a unique positive locally finite Borel measure with polynomial interval mass growth. Explicitly this means that for some finite \(C,d\ge0\),
\[
\mu([j,j+1])\le C(1+|j|)^d\qquad(j\in\mathbb Z).
\tag{SPF0.4}
\]
This is equivalent to the positive-measure temperedness condition
\(\int(1+\lambda^2)^{-r}d\mu(\lambda)<\infty\) for some nonnegative integer \(r\). The zero measure is allowed. No discrete spectral assumption, simplicity assertion, finite-support density hypothesis, or RH assumption enters this source classification.

The original full-jet ideal is
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for every actual nontrivial zero }\rho\text{ of original }\zeta,
\ 0\le j<m_\rho\}.
\tag{SPF0.5}
\]
Descent of the form to the actual Fréchet quotient \(\mathcal Q=\mathcal B/\mathcal I\) holds **exactly** when
\[
\boxed{\operatorname{supp}\mu\subset
\Gamma=\{\lambda\in\mathbb R:\zeta(1/2+i\lambda)=0\}.}
\tag{SPF0.6}
\]
The proof retains the complete original-zeta source multiplier, exceptional values, and all original zero multiplicities. It does not replace \(\zeta\) by that multiplier.

## SPF1. The exact inverse transform of every source vector

Define the auxiliary time-function space
\[
\mathcal E=\left\{h\in C^\infty(\mathbb R):
e_{N,M,j}(h)=\sup_{t\in\mathbb R}
e^{N|t|}(1+|t|)^M|h^{(j)}(t)|<\infty
\quad(N,M,j\in\mathbb Z_{\ge0})\right\}.
\tag{SPF1.1}
\]
The exact transform pair is
\[
\mathcal Lh(s)=\int_{\mathbb R}h(t)e^{(s-1/2)t}dt,
\qquad
\mathcal L^{-1}F(t)=\frac1{2\pi}
\int_{\mathbb R}F(1/2+iy)e^{-iyt}dy.
\tag{SPF1.2}
\]
These are mutually inverse continuous maps \(\mathcal E\leftrightarrow\mathcal B\). Only their source topology and exact integral constants are needed here; no new Mellin–Plancherel norm is asserted.

For the forward assertion, exponential bounds make the first integral entire, including every derivative in \(s\). On a fixed strip, integration by parts \(k\) times in \(t\) writes \((iy)^k\mathcal Lh(\sigma+iy)\) as the integral of the \(k\)-th derivative of \(e^{(\sigma-1/2)t}h(t)\), with its corresponding sign. All endpoint terms vanish by the defining exponential decay. The Leibniz expansion has finitely many terms, each bounded in \(L^1(dt)\), uniformly for \(|\sigma|\le A\), by finitely many \(e_{N,M,j}\) with \(N>A+1\). This proves every \(b_{A,M}\) bound and continuity.

For the inverse assertion, the second integral and all its derivatives in \(t\) converge absolutely because \(F\) decreases faster than every inverse polynomial on that line. If \(a\in\mathbb R\), rectangular contour displacement gives
\[
h^{(j)}(t)=\frac{(-1)^j}{2\pi}
\int_{\mathbb R}(a+iy)^jF(1/2+a+iy)e^{-(a+iy)t}dy.
\tag{SPF1.3}
\]
To justify the displacement, integrate the entire function
\((s-1/2)^jF(s)e^{-(s-1/2)t}\) over the rectangle between the two real parts and heights \(\pm R\). For each fixed \(t\), rapid strip decay bounds the two horizontal integrals by \(C_t(1+R)^{-2}\) after choosing a sufficiently high defining seminorm. They tend to zero; the vertical integrals converge absolutely. This proves (SPF1.3) with its sign before any estimate.

For \(t\ge0\) choose \(a=N+1\), and for \(t<0\) choose \(a=-(N+1)\). Taking \(A\ge N+2\) in the source seminorm gives
\[
|h^{(j)}(t)|\le C_{N,j}b_{A,j+2}(F)e^{-(N+1)|t|}.
\tag{SPF1.4}
\]
Multiplication by \(e^{N|t|}(1+|t|)^M\) has a finite supremum, so \(h\in\mathcal E\) and the inverse is continuous. Fourier inversion on the line \(s=1/2+iy\) proves \(\mathcal Lh=F\) there; the identity theorem proves equality on the whole plane. Conversely Fourier inversion proves \(\mathcal L^{-1}\mathcal Lh=h\). Thus every source vector, not merely a presumed dense subspace, has the exact inverse (SPF1.2).

## SPF2. The positive source completion and the original degree

Continuity of \(\mathfrak b\) supplies \(A,M,C\) with
\[
\mathfrak b(F,F)\le C b_{A,M}(F)^2.
\tag{SPF2.1}
\]
This follows by bounding a continuous form by finitely many defining seminorms and using the increasing seminorm family. Positivity gives Cauchy–Schwarz by expanding \(\mathfrak b(F+zG,F+zG)\); hence its zero-norm space is its full radical. Complete the quotient by that radical to a Hilbert space \(H_{\mathfrak b}\), with continuous dense-image map
\[
\jmath:\mathcal B\longrightarrow H_{\mathfrak b},
\qquad\langle\jmath F,\jmath G\rangle=\mathfrak b(F,G).
\tag{SPF2.2}
\]

The transfer relation and \(\mathsf U_nT_n=nI\) give
\(\mathfrak b(T_nF,T_nG)=n\mathfrak b(F,G)\). Applying this to the inverse maps and composing gives the same identity for all positive rationals. The source action is continuous in its real logarithmic parameter: the integral identity
\(e^{hs}-1=hs\int_0^1e^{uhs}du\) and one additional rapid-strip seminorm prove continuity. Density of the positive rationals and joint continuity of the form therefore give
\[
\mathfrak b(T_aF,T_aG)=a\mathfrak b(F,G)
\quad(a>0).
\tag{SPF2.3}
\]
Consequently
\[
V_t\jmath F=e^{-t/2}\jmath T_{e^t}F
\tag{SPF2.4}
\]
defines a strongly continuous unitary group on the completion. It is first an isometry with inverse on the dense source image. Its extensions are unitary; strong continuity on that dense image and the norm bound prove it everywhere. The exact original map is still
\[
\boxed{\jmath T_{e^t}=e^{t/2}V_t\jmath.}
\tag{SPF2.5}
\]
The factor \(e^{t/2}\), and therefore the degree \(n\), is retained. This is an auxiliary unitary comparison of the original representation, not a replacement of its original operators.

## SPF3. Multiplication is an actual convergent group integral

For \(h\in\mathcal E\), \(G\in\mathcal B\), and \(F=\mathcal Lh\),
\[
b_{A,M}(h(t)e^{t(s-1/2)}G(s))
\le |h(t)|e^{(A+1/2)|t|}b_{A,M}(G).
\tag{SPF3.1}
\]
The right side is integrable. The integrals over compact intervals converge as their intervals exhaust \(\mathbb R\) in every defining source seminorm. Completeness gives their limit in \(\mathcal B\), and continuous point evaluation identifies it:
\[
\int_{\mathbb R}h(t)e^{t(s-1/2)}G(s)dt=F(s)G(s).
\tag{SPF3.2}
\]
Thus both sides are actual source elements. Applying \(\jmath\) and (SPF2.4),
\[
\boxed{V(h)\jmath G=\jmath(FG),\qquad
V(h)=\int_{\mathbb R}h(t)V_tdt.}
\tag{SPF3.3}
\]
The latter is a bounded Hilbert operator of norm at most \(\|h\|_1\). This is a source integral first and its Hilbert image second. It does not assume that arbitrary spectral multipliers preserve the original source.

## SPF4. The Gaussian source is cyclic in every positive receiver

Retain the exact pair
\[
g(s)=e^{(s-1/2)^2},\qquad
\chi(t)=\frac1{2\sqrt\pi}e^{-t^2/4},\qquad
\mathcal L\chi=g,
\]
\[
\phi(\lambda)=\int_{\mathbb R}\chi(t)e^{it\lambda}dt
=e^{-\lambda^2}>0.
\tag{SPF4.1}
\]
The equality follows by the Gaussian integral, first for real \(s-1/2\) by completing its square and then everywhere by entire continuation. In particular \(\chi\in\mathcal E\), \(g\in\mathcal B\), and \(\|\chi\|_1=1\).

For any strongly continuous unitary group, the proved positive-measure construction CFPA.1–CFPA.7 gives, for each \(x\), a finite positive measure \(\nu_x\), of mass \(\|x\|^2\), with
\[
\langle V_tx,x\rangle=\int e^{it\lambda}d\nu_x(\lambda),
\qquad
\|V(h)x\|^2=\int\left|\int h(t)e^{it\lambda}dt\right|^2d\nu_x(\lambda).
\tag{SPF4.2}
\]
That proof uses positive definite functions, Gaussian regularization, Fourier inversion and tightness, and includes uniqueness of the finite measure. It does not assume a discrete spectrum or a spectral multiplicity theorem. In the present case it shows that \(V(\chi)\) is injective: zero norm in its second formula gives \(\int e^{-2\lambda^2}d\nu_x=0\); the strictly positive integrand implies \(\nu_x=0\) and \(x=0\).

Put \(v=\jmath g\), and let
\[
C=\overline{\operatorname{span}\{V_tv:t\in\mathbb R\}}
\subset H_{\mathfrak b}.
\tag{SPF4.3}
\]
This subspace is invariant under every \(V_t\) and its inverse, so its orthogonal projection and the projection \(P\) onto its orthogonal complement commute with every \(V_t\) and every bounded integral \(V(h)\).

Given an arbitrary \(F\in\mathcal B\), obtain its exact \(h=\mathcal L^{-1}F\in\mathcal E\) from SPF1. The two source multiplication identities give
\[
V(\chi)\jmath F=\jmath(gF)=V(h)v.
\tag{SPF4.4}
\]
The right side belongs to \(C\), because its finite-interval integrals and their Hilbert limit belong to that closed subspace. Apply \(P\) and commute it with \(V(\chi)\):
\(V(\chi)P\jmath F=0\). Injectivity gives \(P\jmath F=0\). Since \(\jmath\mathcal B\) is dense, \(P=0\). Therefore
\[
\boxed{C=H_{\mathfrak b}.}
\tag{SPF4.5}
\]
This proves cyclicity, including the zero-space case. No source density of polynomial-Gaussian vectors or finite original jets is presumed.

## SPF5. A complete scalar measure model, with no hidden spectral fibres

Take the finite positive measure \(\nu=\nu_v\) from (SPF4.2). Define on finite sums
\[
W\left(\sum_j a_jV_{t_j}v\right)
=\sum_j a_je^{it_j\lambda}\quad\text{in }L^2(\mathbb R,\nu).
\tag{SPF5.1}
\]
This is well defined and isometric, since the squared norm on either side is
\(\sum_{i,j}a_i\overline{a_j}\int e^{i(t_i-t_j)\lambda}d\nu\).
Its source domain is dense by (SPF4.5). The characters span a dense subspace of \(L^2(\nu)\): a vector orthogonal to every character defines, after complex conjugation, a finite complex measure by Cauchy–Schwarz; its Fourier transform is zero, so it is zero by the finite-measure Fourier uniqueness proved in CFPA. Hence the vector is zero. Thus \(W\) extends to a unitary map onto \(L^2(\nu)\), with
\[
Wv=1,\qquad WV_tW^{-1}=M_{e^{it\lambda}},\qquad
WV(h)W^{-1}=M_{\int h(t)e^{it\lambda}dt}.
\tag{SPF5.2}
\]
The last formula follows by dominated integration for \(h\in L^1\); both sides have norm at most \(\|h\|_1\).

Applying \(W\) to the full equality (SPF4.4) now gives
\[
\phi(\lambda)(W\jmath F)(\lambda)=F(1/2+i\lambda)
\quad\nu\text{-almost everywhere}.
\tag{SPF5.3}
\]
As \(\phi\) is everywhere nonzero, define the locally finite positive Borel measure
\[
\boxed{d\mu(\lambda)=e^{2\lambda^2}d\nu(\lambda).}
\tag{SPF5.4}
\]
It is locally finite because the density is bounded on each compact interval. Multiplication by \(\phi\) is a unitary map \(L^2(\nu)\to L^2(\mu)\): its inverse is division by the same nonzero function with these specified weighted domains. Consequently
\[
\mathcal W=M_\phi W:H_{\mathfrak b}\xrightarrow{\sim}L^2(\mu),
\quad\mathcal W\jmath F=F(1/2+i\lambda),
\quad\mathcal Wv=\phi.
\tag{SPF5.5}
\]
This proves (SPF0.3), absolute convergence of the mixed integral by Cauchy–Schwarz, and completeness of the scalar receiving model. It also proves that the value image of the original source is dense in this \(L^2(\mu)\), by the definition of \(\jmath\) and the proved unitary. No separate finite-support argument is used for a possibly continuous measure.

The original coefficient action in this exact model is
\[
\mathcal W\jmath T_aF(\lambda)
=a^{1/2+i\lambda}F(1/2+i\lambda),
\qquad
\mathsf U_n\longmapsto n^{1/2-i\lambda}.
\tag{SPF5.6}
\]
Both the original degree and the inverse coefficient character remain.

## SPF6. Source continuity forces precisely tempered growth

For \(\gamma\in\mathbb R\), use the actual source Gaussian
\[
g_\gamma(s)=e^{(s-1/2-i\gamma)^2}.
\]
Its source estimate is
\[
b_{A,M}(g_\gamma)\le
e^{(A+1/2)^2}(1+|\gamma|)^M
\sup_{u\in\mathbb R}(1+|u|)^Me^{-u^2}.
\tag{SPF6.1}
\]
Indeed its modulus at \(\sigma+iy\) is
\(e^{(\sigma-1/2)^2-(y-\gamma)^2}\), and
\(1+|y|\le(1+|\gamma|)(1+|y-\gamma|)\).
The remaining supremum is finite. The just-proved scalar model and (SPF2.1) give
\[
\int e^{-2(\lambda-\gamma)^2}d\mu(\lambda)
=\mathfrak b(g_\gamma,g_\gamma)
\le C'(1+|\gamma|)^{2M}.
\tag{SPF6.2}
\]
The integrand is at least \(e^{-2}\) on \([\gamma-1,\gamma+1]\). Therefore
\[
\mu([\gamma-1,\gamma+1])\le e^2C'(1+|\gamma|)^{2M}.
\tag{SPF6.3}
\]
This proves (SPF0.4) and the stronger uniform moving-interval bound, without a zero-spacing hypothesis or a discretization of the spectrum.

For clarity, the growth equivalences require no further analytic theorem. Summing (SPF0.4) over integer intervals proves
\(\mu([-R,R])\le C''(1+R)^{d+1}\). Choosing an integer \(r\) with \(2r>d+1\) and summing the weighted interval masses proves
\[
\int_{\mathbb R}(1+\lambda^2)^{-r}d\mu(\lambda)<\infty.
\tag{SPF6.4}
\]
Conversely a finite integral in (SPF6.4) bounds the mass of \([j,j+1]\) by that integral times
\(\sup_{\lambda\in[j,j+1]}(1+\lambda^2)^r\), a fixed constant times \((1+|j|)^{2r}\). For a positive measure this is the exact temperedness condition being used.

## SPF7. Sufficiency and uniqueness of the positive measure

Let \(\mu\) be any positive locally finite Borel measure satisfying (SPF0.4), or equivalently (SPF6.4). Choose \(M\) with \(2M>d+2\). Then
\[
\int |F(1/2+i\lambda)|^2d\mu(\lambda)
\le b_{1,M}(F)^2
\int(1+|\lambda|)^{-2M}d\mu(\lambda)<\infty.
\tag{SPF7.1}
\]
The last integral converges by partition into unit intervals and the specified growth. Cauchy–Schwarz gives the mixed integral and joint continuity. Positivity is direct. On the line,
\(\overline{n^{1-(1/2+i\lambda)}}=n^{1/2+i\lambda}\), so direct substitution gives exactly (SPF0.2). Thus every indicated measure is permitted.

To prove uniqueness, retain the same Gaussian \(g\). For every real \(t\), the form determines
\[
e^{-t/2}\mathfrak b(T_{e^t}g,g)
=\int_{\mathbb R}e^{it\lambda}e^{-2\lambda^2}d\mu(\lambda).
\tag{SPF7.2}
\]
The weighted measure on the right is finite by (SPF0.4). Fourier uniqueness identifies it from all these values. Since \(e^{-2\lambda^2}\) is everywhere nonzero, it identifies \(\mu\) itself. This completes necessity, sufficiency and uniqueness in (SPF0.3).

Its radical is exactly
\[
\operatorname{rad}\mathfrak b
=\{F\in\mathcal B:F(1/2+i\lambda)=0\quad\mu\text{-almost everywhere}\}.
\tag{SPF7.3}
\]
This is a kernel of a proved map from the original source. It is not an assertion that any of those vectors was already zero in that source.

## SPF8. The complete original-zeta multiplier lies in the original ideal

Retain the entire source vector, with the full original zeta visible:
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
k_0(t)=\frac12e^{t/2}\Sigma f_0(e^t),
\quad\Sigma f(u)=2\sum_{n\ge1}f(nu),
\]
\[
\boxed{\mathcal Lk_0(s)=F_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).}
\tag{SPF8.1}
\]
The entire source computation CFP3 proves it with all constants. To record its original summands directly, on \(\Re s>1\) absolute summation gives
\[
\mathcal Lk_0(s)=\zeta(s)\int_0^\infty f_0(v)v^s\frac{dv}{v},
\]
\[
\int_0^\infty f_0(v)v^s\frac{dv}{v}
=\frac12\pi^{-s/2}\Gamma((s+4)/2)
-\frac34\pi^{-s/2}\Gamma((s+2)/2)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\tag{SPF8.2}
\]
The two endpoint source conditions are \(f_0(0)=0\) and \(\int f_0=0\). Fourier differentiation of the Gaussian proves \(\widehat f_0=f_0\), so Poisson summation gives
\(\Sigma f_0(u)=u^{-1}\Sigma f_0(u^{-1})\), hence \(k_0(-t)=k_0(t)\). For each derivative order \(j\), differentiating the summands for \(t\ge0\) gives a finite polynomial in \(ne^t\), times \(e^{t/2}e^{-\pi n^2e^{2t}}\). Thus for suitable finite \(C_j,D_j\),
\[
|k_0^{(j)}(t)|\le C_j
\exp(D_j|t|-(\pi/2)e^{2|t|}).
\tag{SPF8.3}
\]
For negative \(t\) this follows by differentiating the proved evenness identity. Termwise differentiation is justified by uniform convergence of the polynomial-Gaussian series on every compact interval, and the displayed summable bound controls its positive tail. Therefore \(k_0\in\mathcal E\), and SPF1 proves \(F_0\in\mathcal B\). Entire continuation of the integral proves (SPF8.1) through all exceptional points.

Every exceptional contribution is retained:
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0\quad(r\ge1).
\tag{SPF8.4}
\]
At zero these values use the Gamma principal part \(2/s\) and \(\zeta(0)=-1/2\); at one they use the original zeta residue one. At negative even integers they use the Gamma residue \(2(-1)^r/r!\) and the simple trivial zero of the original zeta. Its derivative and the reflected value follow from the full original functional equation
\[
\zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s).
\tag{SPF8.5}
\]
The sine zero is simple and the remaining factors at \(-2r\) are nonzero, fixing the trivial multiplicity rather than assuming cancellation without its coefficients.

At any actual nontrivial zero \(\rho\), the complete multiplier
\(M_0(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/8\) is a holomorphic nonzero germ. If \(\zeta(\rho+z)=z^{m_\rho}u_\rho(z)\), the exact germ is
\[
F_0(\rho+z)=z^{m_\rho}
\frac{(\rho+z)(\rho+z-1)}8
\pi^{-(\rho+z)/2}\Gamma((\rho+z)/2)u_\rho(z).
\tag{SPF8.6}
\]
All derivatives of this unit remain. Explicitly
\[
F_0^{(r)}=\sum_{j=0}^r\binom rj M_0^{(j)}\zeta^{(r-j)},
\]
\[
M_0^{(j)}(s)=\sum_{j_0+j_1+j_2=j}
\frac{j!}{j_0!j_1!j_2!}
\left(\frac{s(s-1)}8\right)^{(j_0)}
\left(-\frac{\log\pi}2\right)^{j_1}\pi^{-s/2}
2^{-j_2}\Gamma^{(j_2)}(s/2).
\tag{SPF8.7}
\]
The integral supplies the entire derivative at exceptional points. In particular the zeros of this source multiplier are exactly the original nontrivial zeros with unchanged multiplicities. It follows from the actual definition (SPF0.5) that
\[
F_0\in\mathcal I,\qquad F_0\mathcal B\subset\mathcal I.
\tag{SPF8.8}
\]
No equality between \(\mathcal I\) and this principal product ideal is asserted or needed.

## SPF9. Exact descent through the complete original ideal

A positive form descends through \(\mathcal B\to\mathcal Q\) exactly when every vector of \(\mathcal I\) has zero norm. Positivity and Cauchy–Schwarz then kill both mixed terms, proving independence of representatives. Conversely independence forces those norms to vanish. A descended form is continuous in the actual quotient topology, since the quotient map is open and the continuous prequotient form is constant on its fibres in each variable.

If the form descends, apply it to the particular original source vector \(F_0\in\mathcal I\):
\[
0=\mathfrak b(F_0,F_0)
=\int_{\mathbb R}
\left|\frac{(1/2+i\lambda)(-1/2+i\lambda)}8
\pi^{-(1/2+i\lambda)/2}
\Gamma((1/2+i\lambda)/2)\zeta(1/2+i\lambda)\right|^2d\mu(\lambda).
\tag{SPF9.1}
\]
All factors outside \(\zeta\) in this integral are finite and nonzero. Nonnegativity shows that \(\mu\) gives zero measure to their product's nonzero set: it is the union of the sets where that absolute value is at least \(1/j\). Its zero set \(\Gamma\) is closed. Hence \(\operatorname{supp}\mu\subset\Gamma\).

Conversely if this support inclusion holds, each \(F\in\mathcal I\) vanishes at every \(1/2+i\lambda\) on the support; already its zeroth jet is enough. The source form gives it zero norm and therefore descends. This proves both directions of (SPF0.6) while retaining all higher-jet conditions in the ideal. Those higher jets remain actual source classes in the quotient; the theorem determines which observations any positive receiver retains.

The source integral version is also exact: by (SPF3.3),
\[
V(k_0)\jmath G=\jmath(F_0G).
\tag{SPF9.2}
\]
On a descended receiver the right side is zero. On the prequotient scalar receiver the left side is the bounded multiplier by the entire original expression \(F_0(1/2+i\lambda)\). Thus descent is precisely where this proved multiplication operator becomes zero, not where an endpoint, Gamma factor, or original zeta is declared absent.

## SPF10. Recovery of every multiplicity-weighted discrete form

The set \(\Gamma\) is discrete, because it lies in the isolated-zero set of the nonzero entire source function \(F_0\). It is countable, with only finitely many points in each compact interval. Any locally finite measure supported there is uniquely
\[
\mu=\sum_{\rho=1/2+i\gamma\in\mathscr Z}
w_\rho\,\delta_\gamma,
\qquad w_\rho=\mu(\{\gamma\})\ge0.
\tag{SPF10.1}
\]
The interval mass bound gives polynomial growth of each \(w_\rho\). Define the coefficient relative to the original trace multiplicity by
\[
c_\rho=\frac{w_\rho}{m_\rho},\qquad
w_\rho=m_\rho c_\rho.
\tag{SPF10.2}
\]
Then \(c_\rho\) has polynomial growth because \(m_\rho\ge1\), and the descended form is exactly
\[
\mathfrak b([F],[G])=
\sum_{\rho\in\mathscr Z_{\rm line}}m_\rho c_\rho
F(\rho)\overline{G(\rho)}.
\tag{SPF10.3}
\]
Conversely polynomial growth of \(c_\rho\), together with the actual unconditional zero count
\(\sum_{|\Im\rho|\le R}m_\rho=O(R\log(R+2))\), proves the measure (SPF10.1) has polynomial interval mass: each interval sum is bounded by its maximal coefficient times the full multiplicity count in the encompassing bounded-height region. Thus every CFP family is recovered, and no additional restriction is introduced by using a measure.

On each original full multiplicity block, the exact observation is
\[
\mathbb C[z]/(z^{m_\rho})\longrightarrow L^2(\mu),\qquad
\sum_{j=0}^{m_\rho-1}a_jz^j\longmapsto
\begin{cases}a_0\mathbf 1_{\{\gamma\}},&\rho=1/2+i\gamma,
\\0,&\Re\rho\ne1/2.
\end{cases}
\tag{SPF10.4}
\]
The indicator's squared norm is \(w_\rho=m_\rho c_\rho\), and it is zero as an \(L^2\) class if this weight is zero. This map is realized on the actual original global isolators, not on a presumed unrestricted product of jets. It retains the multiplicity in the norm and kills the indicated higher jets only in this receiver. No simplicity theorem is claimed.

## SPF11. What was constructed and which source result it precedes

Before taking the original zeta quotient, every positive tempered measure is permitted; a continuous part is allowed. The complete source action, its unitary comparison, and the cyclic Gaussian construct the exact scalar measure with all domains and integral constants. The Fréchet continuity of the source is what forces polynomial interval growth.

The exact quotient map has a sharper restriction: its full original source vector \(F_0\), with endpoint values \(1/8\), original Gamma factor, powers of \(\pi\), trivial-zero derivative coefficients and full nontrivial multiplicities, forces the measure onto the actual critical-line zeros. The measure model then recovers CFP exactly. The theorem does not infer that every original zero is on that line; it proves the precise descent condition and its kernel data from the source rather than assigning a positive spectrum to the quotient.

The source proof used CFPA.1–CFPA.7, read in full and retained in `CONTINUOUS_POSITIVE_TRANSFER_FORMS.md`, SHA256 `ce8da36c1c6a61acbd2a083751cd86597b4dbb8d2940892592a458f242034d1e`. That appendix proves the scalar positive-measure theorem and finite-measure Fourier uniqueness rather than citing an unexamined Stone theorem. SPF4–SPF5 prove cyclicity and the complete scalar model, which are new receiving steps here. CFP3's Gaussian/Poisson/Mellin calculation was reread and expanded in SPF8 to prove the full source membership. The exact original ideal and global isolators are the retained RD1/RTT0 constructions; SPF10 uses their actual finite-block maps only. No newly located human source is represented as read, no numerical spectrum is substituted for the full divisor, and no publication action is part of this independent derivation.
