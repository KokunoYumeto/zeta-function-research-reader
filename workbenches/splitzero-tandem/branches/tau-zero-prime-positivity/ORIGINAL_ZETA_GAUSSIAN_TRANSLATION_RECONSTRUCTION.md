# Original zeta under Gaussian translation of the test

This derivation starts with the original meromorphic zeta function and its full signed divisor. Gaussian translation heat changes the test and fixes every zeta zero. At positive translation-heat time its full trivial-zero sum diverges for every real translation. The exact finite-cutoff original trace, the Gamma boundary with the same growing terms, and their invertible augmented comparison are constructed below. Their compensated receiver has the entire coefficient tower and the exact negative index proved here.

The incoming source is PRIME_TRANSLATION_EXTENSION.tex, PWG1–28, read in full from the supplied Shift_Synchronization_Arithmetic_20260923 archive. One numerical identity in PWG28 needs correction:
\(B_2(1/8)=16/\mathrm e+4\), not \(32/\mathrm e+4\).
The stated \(6\cdot10^{-44}\) tail bound remains valid. Its earlier larger expression was an upper bound, and the corrected calculation below gives a stronger intermediate constant.

## 1. Original objects, measures, and factors

Use the original zeta function, its logarithmic Euler derivative, and every Gamma and endpoint factor:
\[
\begin{aligned}
j(s)&=\frac{\zeta'(s)}{\zeta(s)}
=-\sum_{n\ge2}\Lambda(n)n^{-s},\qquad \Re s>1,\\
B(s)&=\pi^{-s/2}\Gamma(s/2),\qquad
\kappa(s)=-\frac{\log\pi}{2}+\frac12\psi(s/2),\\
C(s)&=\tfrac12s(s-1)B(s),\qquad
q(s)=\frac1s+\frac1{s-1}+\kappa(s).
\end{aligned}
\tag{OZG1}
\]
Here \(\Lambda(p^k)=\log p\) and all other \(\Lambda(n)\) are zero. The divisor and reflection formulas, proved directly from the original theta formula in OZC3–8, are
\[
\begin{aligned}
\operatorname{div}\zeta
&=\sum_\rho m_\rho[\rho]+\sum_{m\ge1}[-2m]-[1],\\
\operatorname{div}C&=[1]-\sum_{m\ge1}[-2m],\\
j(s)+j(1-s)&=-\kappa(s)-\kappa(1-s).
\end{aligned}
\tag{OZG2}
\]
Every nontrivial zero satisfies \(0<\Re\rho<1\), and its multiplicity is positive. The zero count is \(N(R)=O(R\log(R+2))\). No completed zeta function replaces the original function in these formulas.

The full local units remain present. At \(s=-2m+h\), Gamma recurrence gives
\[
\begin{aligned}
C(-2m+h)&=h^{-1}c_m(h),\qquad \zeta(-2m+h)=h\,u_m(h),\\
c_m(h)&=(-1)^m\frac{2m(2m+1)\pi^m}{m!}
\left(1-\frac h{2m}\right)\left(1-\frac h{2m+1}\right)
\pi^{-h/2}\Gamma(1+h/2)
\prod_{l=1}^m(1-h/(2l))^{-1}.
\end{aligned}
\tag{OZG2a}
\]
Both \(c_m\) and \(u_m\) are nonvanishing units. At \(s=1+h\),
\(C=h\,c_1^{\rm pole}(h)\), \(\zeta=h^{-1}u_1^{\rm pole}(h)\), where
\(c_1^{\rm pole}(h)=\tfrac12(1+h)\pi^{-(1+h)/2}\Gamma((1+h)/2)\),
\(c_1^{\rm pole}(0)=1/2\), and \(u_1^{\rm pole}(0)=1\).
Consequently the logarithmic derivatives have their signed \(1/h\) terms plus the complete unit logarithmic derivatives. For the entire tests used here, the latter products are holomorphic in the small fixed-point discs and have residue zero. This proves their zero contribution to those particular local residues; the full units remain in the logarithmic derivatives and in every boundary integral. Translation heat changes the tests, not these original units.

Retain the classical bump, its fixed radius, and the original differential filter:
\[
\begin{aligned}
r&=1/64,\quad a_j=r2^{-j},\quad
b_r=*_{j\ge1}\frac{\mathbf1_{[-a_j,a_j]}}{2a_j},\\
G_r(z)&=\prod_{j\ge1}\frac{\sinh(a_jz)}{a_jz}
=\int_{-r}^{r}b_r(v)e^{-zv}\,dv,\qquad
T=D_v^2-\tfrac14,\\
f_r&=Tb_r,\quad k_r=b_r*b_r,\quad h_r=f_r*f_r=T^2k_r,\quad d=2r=1/32.
\end{aligned}
\tag{OZG3}
\]
The probability law of the uniformly convergent sum of independent interval variables gives the density and its support. Its Fourier product decreases faster than every inverse power: any prescribed number of its first factors supplies that bound, while the remaining factors have modulus at most one. Fourier inversion therefore gives a smooth even nonnegative density, flat at its support endpoints. It has mass one. The product is locally normally convergent, since the deviations of the factors from one are \(O(a_j^2)\) on compact sets. Its only zeros are \(128\pi i k\), \(k\ne0\), with multiplicity \(1+\nu_2(|k|)\), by the zeros of the individual factors and the convergent nonzero logarithm of the remaining tail. This is the classical Arias de Reyna bump with the original UP coordinate map, not a new density.

The retained Mellin convention gives
\[
M_f(s)=\int_{\mathbb R}f(v)e^{-(s-1/2)v}\,dv,\qquad
F(s)=M_{f_r}(s)=s(s-1)G_r(s-1/2).
\tag{OZG4}
\]
Integration by parts proves the two factors, and \(F(0)=F(1)=0\). The original \(F\) is nonzero at every off-critical nontrivial zero. All its derivatives decay faster than every inverse power of height on any fixed real strip.

For the exact multiplicative dictionary define
\[
(\mathcal V f)(x)=x^{-1/2}f(-\log x),\quad
\int_0^\infty(\mathcal V f)(x)x^s\,\frac{dx}{x}=M_f(s),\quad
\|\mathcal V f\|_{L^2(dx)}=\|f\|_{L^2(dv)}.
\tag{OZG5}
\]
Substitution \(v=-\log x\) proves both assertions. It also gives
\(\mathcal V(f^\#)(x)=x^{-1}\overline{\mathcal V f(1/x)}\),
\(\mathcal V(f*g)=\mathcal V f *_\times\mathcal V g\), and
\(\mathcal V(f(\cdot-a))(x)=e^{a/2}\mathcal V f(e^a x)\).
Differentiation proves
\(\mathcal V D_v\mathcal V^{-1}=-xD_x-1/2\).
Thus translation by \(\log p\) is the unitary dilation
\(u(x)\mapsto\sqrt p\,u(px)\) with the displayed measure.

## 2. Gaussian test heat and its exact entire receiver

For real \(\epsilon>0\), define
\[
\gamma_\epsilon(v)=\frac{e^{-v^2/(4\epsilon)}}{\sqrt{4\pi\epsilon}},
\quad f_\epsilon=\gamma_{\epsilon/2}*f_r,\quad
h_\epsilon=\gamma_\epsilon*h_r,\quad
A_{\epsilon,a}(s)=e^{\epsilon(s-1/2)^2+a(s-1/2)}F(s)^2.
\tag{OZG6}
\]
Completing the square in the absolutely convergent Gaussian integral gives
\[
M_{f_\epsilon}(s)=e^{\epsilon(s-1/2)^2/2}F(s),\qquad
M_{h_\epsilon(\cdot+a)}(s)=A_{\epsilon,a}(s).
\tag{OZG7}
\]
The second equality follows first for real \(a\), then for complex \(a\) by analytic continuation; Gaussian convolution of the compact \(h_r\) is entire and has Gaussian decay along any fixed horizontal line. The factor \(\epsilon/2\) in each test slot is essential. The two endpoints remain exactly zero, with their multipliers \(e^{\epsilon/4\mp a/2}\) retained.

Put \(c_\rho=\rho-1/2\), \(w_\rho=m_\rho F(\rho)^2\), and
\[
K_\epsilon(a)=\sum_\rho w_\rho e^{\epsilon c_\rho^2+ac_\rho}.
\tag{OZG8}
\]
The unsmoothed weights obey
\(\sum_\rho|w_\rho|(1+|\Im\rho|)^n<\infty\) for every integer \(n\ge0\), by the zero count and the compact-test bounds. Writing \(a=A+iB\), \(c_\rho=x+iy\), \(|x|\le1/2\), gives
\[
\left|e^{\epsilon c_\rho^2+ac_\rho}\right|
\le e^{\epsilon/4+|A|/2-\epsilon y^2+|B||y|}
\le e^{\epsilon/4+|A|/2+B^2/(4\epsilon)}.
\tag{OZG9}
\]
Thus the series and every fixed derivative converge normally on complex \(a\)-compact sets and on compact positive \(\epsilon\)-intervals. It is entire in \(a\), real and even for real \(a\), and
\[
\partial_\epsilon K_\epsilon=\partial_a^2K_\epsilon,\qquad
K_\epsilon=\gamma_\epsilon*K_0.
\tag{OZG10}
\]
For the convolution assertion, the bound \(|K_0(x)|\le C_re^{|x|/2}\) makes the Gaussian integral absolutely convergent; termwise integration is dominated by the same weight sum and gives \(e^{\epsilon c_\rho^2}\). The initial Gaussian limit holds locally with every real \(a\)-derivative. This heat fixes all \(\rho\). It is not the heat equation that moves the zeros of the returned family \(\zeta_t\).

The distinction is explicit also on source functions: Gaussian convolution has Fourier multiplier \(e^{-\epsilon y^2}\), so it is injective and a contraction on \(L^2(dv)\); its inverse on its range need not be bounded. Under (OZG5) its generator is \((xD_x+1/2)^2\). This is different from the full original-zeta equation
\(4\partial_t\zeta_t=\zeta_t''+2q\zeta_t'+(q'+q^2)\zeta_t\).

## 3. The full trivial-zero sum and its exact obstruction

Set \(R_m=2m+1/2\). The actual trivial-zero entry is
\[
d_m(\epsilon,a)=A_{\epsilon,a}(-2m)
=4m^2(2m+1)^2
e^{\epsilon R_m^2-aR_m}G_r(R_m)^2.
\tag{OZG11}
\]
For real \(a,\epsilon\) every entry is positive. Evenness, nonnegativity, and mass one give
\[
1\le G_r(R)=\int b_r(v)\cosh(Rv)\,dv\le e^{rR},\qquad R\ge0.
\tag{OZG12}
\]
Therefore, for every \(\epsilon>0\) and every real \(a\),
\[
d_m(\epsilon,a)\longrightarrow+\infty,\qquad
\sum_{m\ge1}d_m(\epsilon,a)=+\infty,\qquad
\lim_{m\to\infty}\frac{\log d_m(\epsilon,a)}{R_m^2}=\epsilon.
\tag{OZG13}
\]
The positive quadratic factor dominates every retained linear exponent. In particular the lost full-sum domain is not merely the region of small translations.

Write \(U_N(\epsilon,a)=\sum_{m=1}^Nd_m(\epsilon,a)\). Since \(G_r(R)\) is increasing for \(R>0\), the ratio of consecutive entries is bounded below by
\[
\frac{d_{m+1}}{d_m}\ge
\exp\{4\epsilon R_m+4\epsilon-2a\}\longrightarrow+\infty.
\tag{OZG14}
\]
The polynomial prefactor is increasing as well. Hence
\[
U_N/d_N\longrightarrow1,\qquad
\frac{\log U_N}{R_N^2}\longrightarrow\epsilon.
\tag{OZG15}
\]
To prove the first limit, fix any \(q>1\). Beyond a fixed index the ratios are at least \(q\), so the late part of the sum is bounded by \(d_N\sum_{j\ge0}q^{-j}\); the finitely many early terms divided by \(d_N\) tend to zero. Taking the upper limit and then \(q\to\infty\) proves the assertion. The second follows from (OZG13).

For comparison, at \(\epsilon=0\) the exact summability domain is \(a\ge d=1/32\). Repeated integration by parts gives
\[
|G_r(R)|\le \|b_r^{(L)}\|_1 R^{-L}e^{rR}.
\tag{OZG16}
\]
For \(a\ge2r\), the entries are \(O(m^{4-2L})\), summable for \(L\ge3\), including the boundary. For \(a<2r\), choose \(r'<r\) with \(2r'>a\). The independent-interval construction gives positive mass in every interval adjacent to an endpoint: restrict finitely many variables to their upper endpoint neighborhoods and bound the remaining total radius. Thus \(G_r(R)\ge c_{r'}e^{r'R}\), and the summands fail to tend to zero. For negative \(\epsilon\), the fixed trivial-zero series alone converges for every real \(a\), by its Gaussian upper bound from (OZG12). This last statement does not assert existence of a moving-zero or nontrivial-zero heat sum at negative translation time.

Thus, for every \(a\ge d\), the fixed-sector limits do not commute:
\[
\lim_{\epsilon\downarrow0}\lim_{N\to\infty}U_N(\epsilon,a)=+\infty,
\qquad
\lim_{N\to\infty}\lim_{\epsilon\downarrow0}U_N(\epsilon,a)
=U_\infty(0,a)<\infty.
\tag{OZG17}
\]
Every finite entry is analytic in \(\epsilon,a\); the failure lies in the domain of infinite summation.

There is a concrete object for this obstruction. Let \(\mathcal P=\mathbb C^{\mathbb N}\) as a vector space, let \(\Sigma:\ell^1\to\mathbb C\) be ordinary summation, and retain
\[
\mathfrak o_{\epsilon,a}=[(d_m(\epsilon,a))_m]\in\mathcal P/\ell^1 .
\tag{OZG18}
\]
For \(\epsilon>0\), \(\mathfrak o_{\epsilon,a}\ne0\) by (OZG13); at \(\epsilon=0,a\ge d\) it is zero. This is an algebraic quotient; no Hausdorff quotient topology is asserted. The completion-divisor sequence is \(-d\), whose class is the exact negative of (OZG18).

The largest elementary paired-sum domain needed here is
\[
\mathcal D_\Sigma=\{(x,y)\in\mathcal P^2:x+y\in\ell^1\},\qquad
(x,y)\longmapsto\Sigma(x+y).
\tag{OZG19}
\]
The actual pair \((d,-d)\) belongs to this domain even though neither component belongs to \(\ell^1\). Retaining both entries and then adding is a specified map. It does not assign a value to either divergent individual sum. The equivalent finite-cutoff construction, with all Gamma terms still present, is proved next.

## 4. Original-zeta contours and the retained Gamma boundary

Let \(A=A_{\epsilon,a}\), first for real \(\epsilon>0,a\), and let
\[
I_c(H)=\frac1{2\pi i}\int_{\Re s=c}H(s)\,ds,\quad
b_N=-2N-1,\quad \sigma>1,
\]
\[
V_N(A)=K_\epsilon(a)+U_N(\epsilon,a)-A(1).
\tag{OZG20}
\]
Each vertical line is integrated upward. In any fixed real strip, \(A\) and all its derivatives decrease faster than every inverse power of height, with an additional Gaussian factor \(e^{-\epsilon y^2}\). The constants depend on the strip; they are not uniform as \(b_N\to-\infty\).

The original argument principle gives
\[
V_N(A)=I_\sigma(Aj)-I_{b_N}(Aj).
\tag{OZG21}
\]
Indeed the enclosed real divisor points are precisely \(1,-2,\ldots,-2N\), with their signed orders from (OZG2). To justify exhaustion in height, use the genus-one logarithmic-derivative expansion of the explicitly factored auxiliary \(C\zeta\), subtract the full \(q\), and choose heights a distance at least \(Y^{-3}\) from adjacent zero ordinates. The zero count leaves an allowed height in each sufficiently large unit interval. Near zero terms then have polynomial growth and the paired tails are \(O(\log Y)\). The Gaussian vertical decay on the fixed strip makes the horizontal integrals tend to zero. The vertical lines converge absolutely, using the original reflection (OZG2) on the left and the Euler series on the right. This proves (OZG21) for each finite \(N\); it does not move a boundary to negative infinity.

Retain the actual reflected Gamma boundary
\[
\mathcal G_N(A)=
I_{b_N}\bigl(A(s)\{\kappa(s)+\kappa(1-s)\}\bigr).
\tag{OZG22}
\]
Insert the original reflection into the left edge of (OZG21), substitute \(s\mapsto1-s\), and move the resulting Euler half-plane line to \(\sigma\). No poles are crossed in that shift. Fourier inversion with the same Mellin convention gives
\[
\begin{aligned}
V_N(A)&=-P_\epsilon(a)+\mathcal G_N(A),\\
P_\epsilon(a)&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\{h_\epsilon(a+\log n)+h_\epsilon(a-\log n)\}.
\end{aligned}
\tag{OZG23}
\]
The infinite prime sum converges absolutely by the Gaussian bounds proved in Section 7. Alternatively absolute convergence of the Euler series and the vertical test bound justifies the Fourier inversion first, and gives the same convergent sum.

The residues of \(\kappa(s)+\kappa(1-s)\) are \(-1\) at \(0,-2,-4,\ldots\) and \(+1\) at \(1,3,5,\ldots\). Shifting its line from \(b_N\) to \(1/2\) crosses exactly \(0,-2,\ldots,-2N\). Therefore
\[
\begin{aligned}
\mathcal G_N(A)&=A_\infty(h_\epsilon(\cdot+a))+A(0)+U_N(\epsilon,a),\\
A_\infty(h)&=\frac1{2\pi}\int_{\mathbb R}\widehat h(y)
\{\Re\psi(1/4+iy/2)-\log\pi\}\,dy .
\end{aligned}
\tag{OZG24}
\]
The sign follows from
\(I_{1/2}-I_{b_N}=-A(0)-U_N\). Both endpoint evaluations are zero for the present test, but their factors and evaluated values remain stated.

The full retained identities, valid at every finite cutoff, are
\[
\boxed{\begin{aligned}
V_N&=K_\epsilon+U_N-A(1),\\
\mathcal G_N&=A_\infty+A(0)+U_N,\\
V_N-U_N+A(1)&=A(0)+A(1)+A_\infty-P_\epsilon=K_\epsilon.
\end{aligned}}
\tag{OZG25}
\]
The Gamma boundary and original signed trace both have the positive quadratic growth (OZG15); their difference has the displayed finite value. The entire completion factor itself gives the separate exact contour
\[
I_\sigma(Aq)-I_{b_N}(Aq)=A(1)-U_N.
\tag{OZG26}
\]
This follows either from its full factorization or from its divisor, with the same finite contour justification. Thus the endpoint polynomial and Gamma factor have both been retained.

Increasing \(N\) adds \(d_{N+1}\) to \(V_N,U_N,\mathcal G_N\) and subtracts it from (OZG26). Keep the entire sequence of these increments. The map
\[
(K,d)\longmapsto
\bigl((K+\sum_{m\le N}d_m)_N,\ d\bigr)
\tag{OZG27}
\]
is injective, with inverse \(K=V_0\) for the present endpoint-zero test. The receiving map \(V_N-U_N\) is independent of \(N\). This is the finite-cutoff form of (OZG19), with the actual arithmetic boundary identified.

## 5. Entire coefficient tower and exact raw corrections

Define actual source tests and their Mellin transforms by
\[
g_j=\frac{D_v^j f_\epsilon}{j!},\qquad
M_{g_j}(s)=\frac{(s-1/2)^j}{j!}
e^{\epsilon(s-1/2)^2/2}F(s).
\tag{OZG28}
\]
Integration by parts has no boundary term because the functions and all derivatives have Gaussian tails. All endpoint evaluations still vanish.

The compensated coefficient form of these tests is
\[
\mathcal C_{\epsilon,jk}
=\frac{(-1)^j}{j!k!}K_\epsilon^{(j+k)}(0)
=\sum_\rho m_\rho e^{\epsilon c_\rho^2}F(\rho)^2
\frac{(-1)^jc_\rho^{j+k}}{j!k!}.
\tag{OZG29}
\]
The sign comes from the exact reflected factor
\(\overline{M_{g_j}(1-\bar s)}=(-1)^j(s-1/2)^j
e^{\epsilon(s-1/2)^2/2}F(s)/j!\).
The matrix is real Hermitian because \(K_\epsilon\) is real even.

The original signed finite-cutoff coefficient matrix is
\[
\mathcal R_{\epsilon,N,jk}
=\mathcal C_{\epsilon,jk}+\mathcal D_{\epsilon,N,jk},\qquad
\mathcal D_{\epsilon,N,jk}
=\frac{(-1)^k}{j!k!}
\sum_{m=1}^{N}d_m(\epsilon,0)R_m^{j+k}.
\tag{OZG30}
\]
The completion-divisor coefficient is \(-\mathcal D_{\epsilon,N,jk}\), with its pole entry zero. Formula (OZG30) follows by evaluating the original reflected test at \(s=-2m\), where \(c=-R_m\). For \(N\ge1\),
\[
\mathcal R_{\epsilon,N,01}-\mathcal R_{\epsilon,N,10}
=-2\sum_{m=1}^{N}d_m(\epsilon,0)R_m<0.
\tag{OZG31}
\]
Thus even each finite raw correction is generally non-Hermitian. Every entry in its infinite fixed-divisor sum diverges in modulus, with sign \((-1)^k\). A raw negative diagonal cannot be substituted for negativity of the compensated Hermitian form.

The exact evolution laws are
\[
\partial_\epsilon\mathcal C_{\epsilon,jk}
=-(j+1)(k+1)\mathcal C_{\epsilon,j+1,k+1}
\]
\[
=\tfrac12\{(j+1)(j+2)\mathcal C_{\epsilon,j+2,k}
+(k+1)(k+2)\mathcal C_{\epsilon,j,k+2}\}.
\tag{OZG32}
\]
They follow by differentiating (OZG29) and comparing its signs and factorials. The finite-cutoff matrices \(\mathcal R,\mathcal D\) obey the same identities separately, by (OZG30). They require the higher displayed rows; a finite block alone is not a closed evolution.

## 6. All-zero detection and the exact negative index

For every fixed \(\epsilon>0\),
\[
\mathrm{RH}\quad\Longleftrightarrow\quad
K_\epsilon\text{ bounded on }[0,\infty)
\quad\Longleftrightarrow\quad
|K_\epsilon(a)|\le K_\epsilon(0)\quad(a\ge0).
\tag{OZG33}
\]
Under RH, each \(c_\rho=i\gamma_\rho\), the original \(F(\rho)\) is real, and every weight is \(m_\rho F(\rho)^2e^{-\epsilon\gamma_\rho^2}\ge0\). The triangle inequality proves the last condition. Conversely boundedness makes the Laplace transform holomorphic on \(\Re w>0\). On \(\Re w>1/2\), absolute convergence gives its exact expression
\[
\int_0^\infty e^{-wa}K_\epsilon(a)\,da
=\sum_\rho\frac{w_\rho e^{\epsilon c_\rho^2}}{w-c_\rho}.
\tag{OZG34}
\]
This sum is normally meromorphic on the whole plane. Each off-critical residue is nonzero by (OZG4) and the nonvanishing Gaussian multiplier. The connectedness of the complement of the discrete pole set and the identity theorem rule out any pole in \(\Re w>0\). Reflection rules out the left half of the critical strip as well. This proves the converse without omitting multiplicities.

The entire function gives an absolutely convergent two-variable expansion
\[
K_\epsilon(b-a)=\sum_{j,k\ge0}
\mathcal C_{\epsilon,jk}a^jb^k .
\tag{OZG35}
\]
If every initial coefficient block is positive semidefinite, substitution of any finite real translation set and passage through square truncations prove positivity of its full translation matrix. Its two-point submatrix then gives the last bound in (OZG33). Under RH, the Gram series in (OZG29) proves positivity of every block. Hence
\[
\mathrm{RH}\quad\Longleftrightarrow\quad
[\mathcal C_{\epsilon,jk}]_{0\le j,k\le n}\succeq0
\quad\text{for every }n.
\tag{OZG36}
\]
This is a proved equivalence, not a proof of the inequalities.

The complete negative index is also exact. Let \(\mathcal Z_*\) consist of the nontrivial zeros with \(F(\rho)\ne0\), let
\[
\mathcal H_*=\ell^2(\mathcal Z_*,m),\quad
(Ju)_\rho=u_{\rho^\#},\quad \rho^\#=1-\bar\rho,\quad
\alpha_\rho=F(\rho)e^{\epsilon c_\rho^2/2}.
\tag{OZG37}
\]
This reflection-stable set contains every off-critical zero. The omitted points are critical and remove only positive directions. The equal multiplicities on exchanged points make \(J\) a self-adjoint involution. For polynomials \(P\), set
\((V_P)_\rho=\alpha_\rho P(c_\rho)\).
Gaussian decay puts every such vector in \(\mathcal H_*\). The identities
\(\bar\alpha_{\rho^\#}=\alpha_\rho\) and
\(c_{\rho^\#}=-\bar c_\rho\) prove that
\(\langle JV_P,V_Q\rangle\) in the divided-power basis is exactly (OZG29).

These polynomial vectors are dense. If \(u\) is orthogonal to all of them, form
\[
H_u(z)=\sum_{\rho\in\mathcal Z_*}
m_\rho\bar u_\rho\alpha_\rho e^{c_\rho z}.
\tag{OZG38}
\]
Cauchy–Schwarz and Gaussian decay prove normal convergence and normal differentiability on every complex compact set. All derivatives at zero vanish, so \(H_u\) is identically zero. On the positive real half-line its absolute value is at most
\(e^{z/2}\|u\|(\sum m_\rho|\alpha_\rho|^2)^{1/2}\).
Its Laplace transform on \(\Re w>1/2\) is therefore
\(\sum m_\rho\bar u_\rho\alpha_\rho/(w-c_\rho)=0\).
This series is normally meromorphic: its coefficients are absolutely summable by Cauchy–Schwarz, and the high-height denominators give a further bound. Its residue at \(c_\rho\) is \(m_\rho\bar u_\rho\alpha_\rho\). The identity theorem and \(\alpha_\rho\ne0\) force \(u=0\), proving density.

Let \(\kappa_-\) be the number of distinct two-point reflection orbits in the actual nontrivial zero set, allowing infinity. Each contributes one negative direction to \(J\); a critical point contributes none. A negative polynomial subspace injects into the negative spectral subspace, giving an upper bound \(\kappa_-\). Conversely approximate any finite negative orthonormal family by \(V_P\). If the column error has norm less than \(1/4\), its Gram error is at most \(2/4+1/16<1\), preserving negative definiteness. Finitely many approximants lie in one finite degree block. Thus
\[
\boxed{\sup_n n_-\bigl([\mathcal C_{\epsilon,jk}]_{0\le j,k\le n}\bigr)
=\kappa_-\qquad(\epsilon>0).}
\tag{OZG39}
\]
The original multiplicities remain in all Hilbert weights. This index belongs to the compensated augmented receiver, not to the divergent full raw sum or its non-Hermitian cutoff matrices.

## 7. Complete arithmetic formula and explicit error bounds

The original Gamma boundary and prime terms yield, for every real \(a\),
\[
\begin{aligned}
K_\epsilon(a)={}&-(\gamma_{\rm E}+\log\pi)h_\epsilon(a)\\
&+\int_0^\infty
\frac{e^{-x}h_\epsilon(a)-\tfrac12e^{-x/4}
\{h_\epsilon(a+x/2)+h_\epsilon(a-x/2)\}}
{1-e^{-x}}\,dx\\
&-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\{h_\epsilon(a+\log n)+h_\epsilon(a-\log n)\}.
\end{aligned}
\tag{OZG40}
\]
This is (OZG25) with its actual endpoint-zero values, not a prime-window formula with compact support assumed after smoothing. It also follows by Gaussian convolution of the entire original OZC/PW distribution. The near-zero Gamma numerator is kept together:
\[
(e^{-x}-e^{-x/4})h(a)
-\tfrac12e^{-x/4}\{h(a+x/2)+h(a-x/2)-2h(a)\}.
\tag{OZG41}
\]
Its two terms are \(O(x)\) and \(O(x^2)\); division by \(1-e^{-x}\) is locally bounded. At infinity the exponential factors are integrable. These bounds and the following prime majorant justify Fubini and all fixed translation derivatives.

For each nonnegative integer \(l\), define
\[
\mathcal B_l(\epsilon)=\frac{l!}{2^l}
\sum_{j=0}^{\lfloor l/2\rfloor}
\frac{\epsilon^{-(l-j)}}{j!(l-2j)!}
\left(\frac{4\epsilon(l-2j)}{\mathrm e}\right)^{(l-2j)/2},
\tag{OZG42}
\]
where the last factor is one at \(l-2j=0\). The exact polynomial derivative of the Gaussian and the maximum
\(\sup_x|x|^d e^{-x^2/(8\epsilon)}
=(4\epsilon d/\mathrm e)^{d/2}\) prove
\[
|\gamma_\epsilon^{(l)}(x)|
\le(4\pi\epsilon)^{-1/2}\mathcal B_l(\epsilon)
e^{-x^2/(8\epsilon)} .
\tag{OZG43}
\]
Indeed the \(j\)th derivative-polynomial coefficient is
\(l!(-1)^{l-j}x^{l-2j}/(2^l\epsilon^{l-j}j!(l-2j)!)\).
Split its Gaussian factor into two equal exponents and apply the displayed maximum to one.

Retain
\[
\mathcal C_{\epsilon,l}=(4\pi\epsilon)^{-1/2}
\{\mathcal B_{l+4}+\tfrac12\mathcal B_{l+2}
+\tfrac1{16}\mathcal B_l\}.
\tag{OZG44}
\]
Since \(k_r\) is a probability measure supported in \([-d,d]\), convolution and the full filter \(D^4-\tfrac12D^2+\tfrac1{16}\) give
\[
|h_\epsilon^{(l)}(a\pm\log n)|
\le\mathcal C_{\epsilon,l}
e^{-(\log n-A-d)^2/(8\epsilon)}
\quad(|a|\le A,\ \log n>A+d).
\tag{OZG45}
\]
Put \(B=A+d\), \(c_B=B+2\epsilon\), and assume
\(\log N\ge\max(B,2)\). Then the complete omitted prime contribution satisfies
\[
\sup_{|a|\le A}
|\partial_a^l(P_\epsilon-P_{\epsilon,N})(a)|
\le2\mathcal C_{\epsilon,l}\mathcal J_{\epsilon,B}(N),
\tag{OZG46}
\]
where
\[
\begin{aligned}
\mathcal J_{\epsilon,B}(N)
=e^{B/2+\epsilon/2}\bigg\{&
4\epsilon e^{-(\log N-c_B)^2/(8\epsilon)}\\
&+c_B\sqrt{2\pi\epsilon}\,
\operatorname{erfc}\frac{\log N-c_B}{\sqrt{8\epsilon}}\bigg\}.
\end{aligned}
\tag{OZG47}
\]
To prove this, use \(0\le\Lambda(n)\le\log n\). The real-variable majorant
\((\log x)x^{-1/2}e^{-(\log x-B)^2/(8\epsilon)}\)
is decreasing on \(x\ge N\), because its logarithmic derivative with respect to \(u=\log x\) is
\(1/u-1/2-(u-B)/(4\epsilon)\le0\).
Thus the omitted integer sum is bounded by its integral from \(N\) to infinity. Substitution \(u=\log x\) gives
\(\int_{\log N}^{\infty}u e^{u/2-(u-B)^2/(8\epsilon)}du\).
Completing the square gives exactly (OZG47), including both terms and the factor 2 for the two translated legs. Every omitted prime power is included.

The finite convolution source \(k_{r,J}\) omits a probability factor of radius \(d2^{-J}\). The mean value theorem gives
\[
\sup_a|h_\epsilon^{(l)}(a)-h_{\epsilon,J}^{(l)}(a)|
\le\eta_l:=d2^{-J}\mathcal C_{\epsilon,l+1}.
\tag{OZG48}
\]
For the whole Gamma expression, (OZG41), \(1-e^{-x}\ge x/2\) on \(0<x\le1\), and the central second-difference bound give error
\(3\eta_l/2+\eta_{l+2}/8\) on that interval. On \(x\ge1\) the uniform error is at most
\(\eta_l(e^{-1}+4e^{-1/4})/(1-e^{-1})\).
The constant term adds \(|\gamma_{\rm E}+\log\pi|\eta_l\). Writing
\[
\mathcal A=
|\gamma_{\rm E}+\log\pi|+\tfrac32+
\frac{e^{-1}+4e^{-1/4}}{1-e^{-1}},
\quad W_N=\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n},
\]
the complete source-and-prime error is
\[
2\mathcal C_{\epsilon,l}\mathcal J_{\epsilon,B}(N)
+(\mathcal A+2W_N)\eta_l+\tfrac18\eta_{l+2}.
\tag{OZG49}
\]
This proves PWG14–22 with their full original arithmetic terms.

At \(\epsilon=1/8\), direct substitution into (OZG42) gives the corrected values
\[
\mathcal B_2=16/\mathrm e+4,\qquad
\mathcal B_4=1024/\mathrm e^2+384/\mathrm e+48.
\tag{OZG50}
\]
Using \(\mathrm e>2,\pi>2\) gives \(\mathcal C_{1/8,0}<503\), since
\(\mathcal B_4<496\), \(\mathcal B_2<12\), and
\((4\pi\epsilon)^{-1/2}<1\). The source's weaker bound \(507\) is therefore also valid.

For \(A=0,N=65536\), one has \(B=1/32\), \(c_B=9/32\), and
\(x=16\log2-9/32>997/96>10\). The bound
\(\operatorname{erfc}x\le e^{-x^2}/(\sqrt\pi x)\), obtained by comparing \(u/x\ge1\) in the Gaussian tail integral, gives
\[
\mathcal J_{1/8,1/32}(65536)
<\frac{329}{590}e^{-994009/9216}.
\tag{OZG51}
\]
Here \(e^{5/64}<64/59\), by termwise comparison with the geometric series. Also \(\log2>2/3\) follows from its positive atanh series, and \(\log10<7/3\) follows from the sixth exponential partial sum at \(7/3\), which is \(1071641/104976>10\). Since \(994009/9216>46(7/3)\), the last exponential is less than \(10^{-46}\). Equations (OZG46), (OZG50), and (OZG51) therefore prove
\[
|P_{1/8}(0)-P_{1/8,65536}(0)|<6\cdot10^{-44}.
\tag{OZG52}
\]
This certifies the prime tail only, not the value or sign of the full first matrix entry.

## 8. Full lattice coordinates and the corrected interpretation

For the original finite bounded distributive lattice \(L\), the actual carrier is
\[
G_L(V)=\{(v,1_L):v\in V\}
\cup\{z_\lambda=(0,\lambda):\lambda\ne1_L\},\qquad
e=(0,1_L),\quad\tau=z_{0_L}.
\tag{OZG53}
\]
Linear source maps send \((v,1_L)\) to \((Av,1_L)\) and fix each lower zero label. Nonzero carrier amplitudes occur only at top support. Independent function values at lower carrier points belong to the attached function space and are retained separately. Pairings use meet labels.

At every fixed cutoff, the original signed spectral and completion-divisor coordinates are
\[
\boldsymbol R_{\epsilon,N}
=(K_\epsilon+U_N)\mathbf e_{1_L},\qquad
\boldsymbol E_{\epsilon,N}=-U_N\mathbf e_{1_L}.
\tag{OZG54}
\]
The original endpoint values are zero because the unchanged factor \(F(0)=F(1)=0\) remains in every smoothed test. The supported identity is exactly
\[
\boldsymbol B_L=0,\quad
\boldsymbol D_L=-K_\epsilon\mathbf e_{1_L},\qquad
\boldsymbol B_L-\boldsymbol R_{\epsilon,N}
=\boldsymbol D_L+\boldsymbol E_{\epsilon,N}.
\tag{OZG55}
\]
Every lower coordinate has its evaluated zero amplitude and retained coordinate space. The Gamma boundary itself has top coefficient \(A_\infty+U_N\), as in (OZG24), and is recorded with its cutoff transition.

The complete object consists of the indexed nontrivial-zero sequence, the indexed trivial-zero sequence, the pole entry with its evaluated zero, the Gamma data, and these full lattice coordinates. The compensated map first adds the original signed and opposite completion-divisor entry at each identical fixed index, then applies the proved summation map. At such a zero amplitude, the top label remains \(e\); it does not become \(\tau\). The augmented comparison (OZG27), or entrywise \((R,E)\mapsto(R+E,E)\), retains an explicit inverse. Discarding the second coordinate would lose the obstruction class (OZG18).

Thus positive Gaussian translation time produces an entire compensated test receiver and an exact coefficient tower, while the full raw scalar divisor sum has no real translation domain. The finite-cutoff original-zeta equations and their common Gamma increments are the required replacement for an asserted nonexistent full scalar sum. The negative-index theorem applies to their compensated receiver and leaves the global sign inequality unresolved.

## Source identity and actual use

The incoming archive has SHA256
70810361fd8fd66f9cc7154ed919bc5c0c15d003e3ec72504b173bbb24aeed15.
Its member Shift_Synchronization_Arithmetic_20260923/PRIME_TRANSLATION_EXTENSION.tex has SHA256
21cacaaac17e356d5c4feb29213b30a9765a786bd80b1aca009d85f775268d14,
26746 bytes. PWG1–28, including its nonsequential PWG24 and PWG28, was read in full.

OZC1–18 and their complete preceding proofs were read directly for the original-zeta contour, reflection, Gamma boundary, and raw adjoint defect. The fixed primitive UP/PW definitions and proofs were already read in the preceding original-zeta audits; their displayed formulas are rederived above where used. No source-space mass-completion calculation from another task is claimed or duplicated here.

Human provenance remains Juan Arias de Reyna, [An infinitely differentiable function with compact support: Definition and properties, arXiv:1702.05442v1](https://arxiv.org/abs/1702.05442v1), Theorem 1, for the classical bump, and Alain Connes, [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, arXiv:math/9811068v1](https://arxiv.org/abs/math/9811068), Appendix II, Theorem 6, through the source-defined full theta and explicit-formula comparison. This derivation does not claim a fresh full reading of those human papers. Its new original-zeta content is the all-translation trivial-zero divergence, its exact growth and obstruction space, the retained finite-cutoff Gamma comparison, and the raw coefficient correction accompanying the entire compensated tower.


![Exact enclosure for the retained trivial-zero terms at the displayed original parameters. The lower and upper edges are the full logarithm of OZG11 with the proved bounds 1 and exp(r R) for G, respectively. OZG13–17 proves divergence and the failure to interchange the positive-time and infinite-cutoff limits. The density is the classical Arias de Reyna function, with the source and exact coordinate comparison stated in OZG3.](gaussian_trivial_zero_growth.png)


Pinned public predecessor proofs: [Original theta and its exact return](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a8e35be8f238913ae5bcbd8ad55a07d539b350f3/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/FAITHFUL_THETA_COMPLETION_RETURN.md#L149), TF17; [Original meromorphic heat family](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a8e35be8f238913ae5bcbd8ad55a07d539b350f3/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/FAITHFUL_UNCOMPLETED_ZETA_HEAT.md#L20), UZ1; [Full original-zeta contour and compact form](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a8e35be8f238913ae5bcbd8ad55a07d539b350f3/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md#L15), OZC1; [Original heat/contact traces](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a8e35be8f238913ae5bcbd8ad55a07d539b350f3/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION.md#L17), OZH1; [Original Cauchy correction and raw skew defect](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a8e35be8f238913ae5bcbd8ad55a07d539b350f3/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md#L184), OZK17. Their complete sources are also retained in this edition. The new full incoming programme TeX is included above, with its original references and its corrected receiving maps.


## Original endpoint sectors and the actual prime-boundary return

The complete new receiving proofs are [SER1–27](SECTORIAL_ENDPOINT_ZERO_TRACE_RETURN.md), [SFT1–48](SECTORIAL_FILTER_TRACE_DERIVATION.md), and [GAB](GAUSSIAN_ARITHMETIC_BOUNDARY_RETURN.md). They distinguish the actual original parameters: SER/SFT uses the original spectral heat time t; GAB uses the integer Gaussian coefficient d=1/(4 pi T), whose zero limit is original T tending to infinity. Both full incoming programme TeX sources are retained in supporting_proofs with their human references.

For the original unfiltered theta continuation, SER8 retains the full Gamma multiplier and both exponential endpoint sectors. Its common-part return has all right time derivatives but zero time-Taylor radius, with exact remainder SER14. The full differential inverse is SFT12–22, including one initial datum in the actual even domain. The zero divisors change by the explicitly evaluated quotient SFT23–30, not by an assumption based on kernel dimension. SER25 computes every finite-contour first trace change, with all multiplicities. SFT39–48 proves a global cubic-decay rational trace, every Gamma contribution, both endpoints and test/divisor collisions; it also evaluates a quadratic-growth counterexample to dropping the infinity term. Thus the original preceding filtered heat, compact-test and Cauchy calculations retain their stated domains and do not silently become raw-sectorial trace claims.

For the actual two-moment prime receiver, GAB10–16 evaluates the full Mellin–Barnes formula, the singular Gamma sector and each positive-odd logarithmic collision. GAB18–22 retains the inverse pair and every additional pole. GAB32–44 puts back the full Mellin multiplier, marked integer-zero source, actual supported-zero action and fixed prime label. The first moment vanishes throughout the critical strip, while its retained residual has exact order d^(3/2) precisely on the original nontrivial zero divisor. The coefficient there is nonzero, proved using original zeta at rho−2. This is an actual all-zero detector, not a sign assigned to the full Weil pairing. No new seminorm or scalar base is substituted.


## Endpoint-resonant detector and its original-time boundary

The complete [ERD1–50 proof](ENDPOINT_RESONANT_ZERO_DETECTION.md) proves that the actual endpoint-resonant cosine transform at t=1/32 is nonzero throughout the closed critical strip, uniformly in height. It retains the full original zeta product at both shifted arguments, every exceptional germ and an explicit phase bound. The same source has a zero complete right-time Taylor jet at time zero: ERD40–50 retains the exact exponential factor, constructs its nonzero nonnilpotent flat germ, evaluates the dual-number jet map, and supplies the positive-time inverse with its analytic coordinate. Vanishing of these time jets does not discard the positive-time detector.

The full [EPM1–47 proof](ENDPOINT_PAIR_TRANSPORT_AND_WEIL_MATRIX.md) calculates the cosine/sine pair's coupled original-time transport, its inverse, both endpoint argument maps and their common-zero set. The sine source is odd; EPM19–21 constructs a split extension of the even prime quotient rather than inserting that source into the old domain. EPM28–31 retains every finite original trivial-zero entry and the Gamma boundary. EPM43–47 puts the companion's certified50<K(0)<64 for the actual cosine test into the exact global translated criterion RH iff |K(a)|<=K(0) for every a>=0. Its positive diagonal does not prove the global inequality. The complete arithmetic certificate source, executable and independent tail proof are included unchanged.
