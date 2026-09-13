# Finite Gamma coefficients, certified Hermitian envelopes, and quotient-volume bounds

Independent derivation, 2026-09-13. This note supplements the exact nested-source update being developed in `gamma_finite_metric_transfer`. It concerns finite polynomial observations and their original quotient maps. No density is divided by its mass, no packet is supplied by the seed, and no global positive lower bound for an arithmetic density enters the calculation.

## 1. Exact coefficient map, with its original mass

Fix a positive real parameter \(\lambda\), put \(\alpha=2\lambda\), and let \(k\geq1\) be an integer. Write
\[
d\sigma_\lambda(t)=r_\lambda(t)\,dt,
\qquad r_\lambda(t)=\frac{|\Gamma(\lambda+it/2)|^2}{2\pi},
\qquad c_\lambda=2^{1-2\lambda}\Gamma(2\lambda),
\qquad C=c_\lambda^k,\qquad \beta=k\alpha.
\]
Let \(B\in L^2(\sigma_\lambda)\) be real and nonnegative almost everywhere, with positive integral. Its arithmetic measure is \(w(t)\,dt=B(t)d\sigma_\lambda(t)\). The polynomial moments of every order exist: for every integer \(j\geq0\), Cauchy--Schwarz bounds \(\int |t|^jB\,d\sigma_\lambda\) by \(\|B\|_{L^2(\sigma_\lambda)}(\int |t|^{2j}d\sigma_\lambda)^{1/2}\), and the Gamma reference has those moments. This domain includes the bounded arithmetic multipliers in the delivered Gamma construction, and also permits the explicitly labeled algebraic calibration multiplier used by the parent calculation.

The monic one-factor polynomials have norms \(c_\lambda j!(\alpha)_j\). Define their actual coefficients and a finite-coefficient formal series by
\[
c_{B,j}=\frac{\int b_j^{(\lambda)}(t)w(t)\,dt}{c_\lambda j!(\alpha)_j},
\qquad A(z)=\sum_{j\geq0}a_jz^j,
\qquad a_j=(\alpha)_jc_{B,j},
\qquad d_n=[z^n]A(z)^k.
\tag{FE.1}
\]
Here \(c_{B,j}\) is the exact typed alias of the delivered coefficient \(c_{h,j}\) when \(B=B_{h,\lambda}\). The reference mass remains \(c_\lambda\). The additional \(B\) index prevents a collision between reference mass \(c_1\) at \(\lambda=1\) and the degree-one expansion coefficient. No coefficient value, mass, or map changes with this alias.
The delivered finite addition formula, paired with \(B^{\otimes k}\), gives
\[
\int b_n^{(k\lambda)}(u)w^{*k}(u)\,du=C\,n!\,d_n.
\tag{FE.2}
\]
For completeness, the addition formula is
\[
b_n^{(k\lambda)}(t_1+\cdots+t_k)
=\sum_{n_1+\cdots+n_k=n}\frac{n!}{n_1!\cdots n_k!}
\prod_{i=1}^k b_{n_i}^{(\lambda)}(t_i).
\]
Pairing a summand against the product measure gives
\(\frac{n!}{\prod n_i!}\prod(c_\lambda n_i!(\alpha)_{n_i}c_{B,n_i})
=C n!\prod a_{n_i}\). Summing the finitely many compositions proves (FE.2). Absolute integrability of each summand follows from the moment estimate above, so this argument uses only finite sums and Fubini on integrable functions. In particular, the factor \(n!\) in (FE.2) remains present.

Let \(p_1,\ldots,p_s\in\mathbb C[u]\), with degrees at most \(N\). These polynomials can be the original source columns \((k/2+iu)^j\), the original relation columns, or specified linear combinations. For each ordered pair expand the complete polynomial product in the monic Gamma basis:
\[
\overline{p_i(u)}p_j(u)=\sum_{n=0}^{2N}L_{ij,n}b_n^{(k\lambda)}(u),\qquad u\in\mathbb R.
\tag{FE.3}
\]
The conjugation acts on every coefficient of \(p_i\); it does not change the real variable \(u\). The exact Hermitian Gram is
\[
M_{ij}=\int\overline{p_i(u)}p_j(u)w^{*k}(u)\,du
=\sum_{n=0}^{2N} L_{ij,n}v_n,
\qquad v_n=C n!d_n.
\tag{FE.4}
\]
This specifies a typed map from the real tuple \((c_{B,0},\ldots,c_{B,2N})\), together with its reference parameter and mass, to \(\operatorname{Herm}(\mathbb C^s)\). It is polynomial in the coefficients \(c_{B,j}\), homogeneous of degree \(k\), and is multiplied by the original factor \(C\). It is not a linear map in the one-factor coefficients when \(k>1\).

Every \(L_{ij,n}\) can be computed by finite triangular elimination. Start with
\[
b_0=1,\quad b_1=u,\quad
b_{n+1}=u b_n-n(n+\beta-1)b_{n-1}.
\tag{FE.5}
\]
Subtract the leading coefficient of the current remainder times its monic \(b_n\), descending from degree \(2N\) to zero. Each subtraction strictly lowers the degree, so the process terminates and gives the unique expansion (FE.3). Its inverse is the displayed sum in (FE.3), an equality of the original polynomials. Because every \(b_n\) has real coefficients, \(L_{ji,n}=\overline{L_{ij,n}}\). All \(v_n\) are real, hence (FE.4) is Hermitian. For rational \(\alpha\) and polynomial coefficients in \(\mathbb Q(i)\), the \(L_{ij,n}\) belong to \(\mathbb Q(i)\).

The relation-degree restriction is literal: (FE.4) uses coefficients through \(2N\) only when the full relation polynomials \(\chi(k/2+iu)P(k/2+iu)\) have degree at most \(N\). Degree \(N\) of \(P\) alone would be insufficient.

## 2. Finite interval errors for every tensor degree

Suppose exact coefficient enclosures have been recorded as
\(a_j=\widehat a_j+\varepsilon_j\), \(|\varepsilon_j|\leq r_j\), for \(0\leq j\leq L\). These are enclosures of the actual integrals in (FE.1), not freely chosen replacement coefficients. Put
\[
\widehat A(z)=\sum_{j=0}^L\widehat a_jz^j,\quad
P(z)=\sum_{j=0}^L|\widehat a_j|z^j,\quad
R(z)=\sum_{j=0}^Lr_jz^j,
\]
\[
\widehat d_n=[z^n]\widehat A(z)^k,\qquad
E_n=[z^n]\big((P(z)+R(z))^k-P(z)^k\big),\qquad n\leq L.
\tag{FE.6}
\]
Then
\[
|d_n-\widehat d_n|\leq E_n.
\tag{FE.7}
\]
Indeed, write \(A=\widehat A+\varepsilon\) up to degree \(L\), expand its \(k\)-th power, and remove the term containing no \(\varepsilon\). Apply the triangle inequality coefficientwise to every remaining finite product. Replacing each \(|\varepsilon_j|\) by \(r_j\) gives exactly the right side of (FE.6). Coefficients above degree \(L\) cannot enter a coefficient of degree at most \(L\), so truncating at \(L\) introduces no further error. This bound keeps all mixed terms and repeated-index terms. In particular, a missing tensor cross term is not absorbed into a supposed first-order error term.

If \(c_{B,j}\) have centers \(\widehat c_{B,j}\) and radii \(\rho_j\), the exact positive factor \((\alpha)_j\) gives \(\widehat a_j=(\alpha)_j\widehat c_{B,j}\), \(r_j=(\alpha)_j\rho_j\). If this factor itself is supplied by an interval, ordinary finite interval multiplication is applied before (FE.6). For rational positive \(\alpha\), all rising factorials are exact positive rationals.

The mass is retained even when an implementation uses a rational enclosure for it. If
\[
0<C_-\leq C\leq C_+,\qquad |C-\widehat C|\leq r_C,
\]
define \(\widehat v_n=\widehat C n!\widehat d_n\). The exact identity
\(C d_n-\widehat C\widehat d_n=C(d_n-\widehat d_n)+(C-\widehat C)\widehat d_n\) proves
\[
|v_n-\widehat v_n|
\leq e_n:=n!\big(C_+E_n+r_C|\widehat d_n|\big).
\tag{FE.8}
\]
With exact polynomial tests, (FE.4) therefore has center and radii
\[
\widehat M_{ij}=\sum_n L_{ij,n}\widehat v_n,
\qquad |M_{ij}-\widehat M_{ij}|
\leq e_{ij}:=\sum_n|L_{ij,n}|e_n.
\tag{FE.9}
\]
One may use any certified rational upper bound for a complex modulus; for example \(|x+iy|\leq |x|+|y|\) requires no irrational square root. Choose symmetric radii \(e_{ji}=e_{ij}\). The center remains Hermitian by the exact conjugation rule from (FE.3).

If the original test coefficients also have enclosures, first propagate them through the finite polynomial map (FE.3). Write \(|L_{ij,n}-\widehat L_{ij,n}|\leq \ell_{ij,n}\). Then
\[
|M_{ij}-\sum_n\widehat L_{ij,n}\widehat v_n|
\leq\sum_n\big(|\widehat L_{ij,n}|e_n+
\ell_{ij,n}(|\widehat v_n|+e_n)\big).
\tag{FE.10}
\]
This follows from \(Lv-\widehat L\widehat v=\widehat L(v-\widehat v)+(L-\widehat L)v\). Thus a coefficient enclosure for an actual packet polynomial can enter with every original complex coefficient and conjugation retained; no numerical packet data are supplied by this note.

## 3. Exact rational positive-definiteness certificates

Let \(E=M-\widehat M\), where (FE.9) or (FE.10) supplies symmetric nonnegative rational bounds \(|E_{ij}|\leq e_{ij}\). Choose any positive rational vector \(w=(w_1,\ldots,w_s)\). Define the diagonal matrix
\[
\Delta=\operatorname{diag}(\delta_1,\ldots,\delta_s),\qquad
\delta_i=\sum_{j=1}^s e_{ij}\frac{w_j}{w_i}.
\tag{FE.11}
\]
Then the exact Hermitian inequalities are
\[
-\Delta\preceq E\preceq\Delta,
\qquad M_-:=\widehat M-\Delta\preceq M\preceq
M_+:=\widehat M+\Delta.
\tag{FE.12}
\]
For any \(x\in\mathbb C^s\),
\[
|x^*Ex|\leq\sum_i e_{ii}|x_i|^2+
2\sum_{i<j}e_{ij}|x_i||x_j|.
\]
For each pair, nonnegativity of
\((\sqrt{w_j/w_i}|x_i|-\sqrt{w_i/w_j}|x_j|)^2\)
gives
\(2|x_i||x_j|\leq(w_j/w_i)|x_i|^2+(w_i/w_j)|x_j|^2\).
Substitution gives \(|x^*Ex|\leq x^*\Delta x\), proving (FE.12). Square roots occur only in this proof of the inequality; the certificate (FE.11) uses rational operations exclusively.

For a rational Hermitian matrix \(A\), the following recurrence produces a complete certificate of strict positivity when it succeeds. Set a lower triangular matrix \(L\) with diagonal entries one, and define in increasing order
\[
d_j=A_{jj}-\sum_{r<j}L_{jr}d_r\overline{L_{jr}},
\qquad
L_{ij}=\frac{A_{ij}-\sum_{r<j}L_{ir}d_r\overline{L_{jr}}}{d_j}\quad(i>j).
\tag{FE.13}
\]
At each step verify \(d_j>0\) as an exact rational comparison. Entrywise multiplication verifies \(A=L\operatorname{diag}(d_j)L^*\): the recurrence gives diagonal entries and entries below the diagonal, and Hermitian conjugation gives the remainder. For nonzero \(x\), \(L^*x\ne0\), so
\(x^*Ax=\sum_j d_j|(L^*x)_j|^2>0\).
Thus successful evaluation of (FE.13) for \(M_-\) proves \(M_-\succ0\), \(M\succ0\), and \(M_+\succ0\). A nonpositive pivot causes this certificate to fail; it does not certify nonpositivity of the actual arithmetic Gram. This is a checkable finite decision about the recorded enclosures, with no unproved lower bound on the density.

There is also a relative version with the same exact coefficients. Factor \(\widehat M=L D L^*\succ0\) by (FE.13). Put
\[
S_{ab}=\sum_{i,j}|(L^{-1})_{ai}|e_{ij}|(L^{-1})_{bj}|,
\quad
\eta=\max_a\frac{\sum_b S_{ab}w_b}{D_{aa}w_a}.
\tag{FE.14}
\]
Rational modulus majorants may again replace the displayed moduli. Entrywise multiplication shows that \(L^{-1}E L^{-*}\) has entries bounded by \(S_{ab}\). Applying the proof of (FE.12) gives
\(-\eta D\preceq L^{-1}E L^{-*}\preceq\eta D\).
Congruence by \(L\) proves
\[
(1-\eta)\widehat M\preceq M\preceq(1+\eta)\widehat M.
\tag{FE.15}
\]
The map here is the explicit invertible coordinate map \(x\mapsto L^*x\), with inverse \(y\mapsto L^{-*}y\). Its determinant contribution is \(|\det L|^2=1\), because its diagonal entries are one. Neither the measure nor its mass has changed. Formula (FE.15) is useful only after the exact certificate verifies \(\eta<1\).

## 4. Quotient envelopes in the original quotient dimension

Fix the original surjection \(\mathcal O:\mathbb C^s\to\mathbb C^q\), an injective relation matrix \(B:\mathbb C^m\to\mathbb C^s\) with \(\operatorname{im}B=\ker\mathcal O\), and a right inverse \(J:\mathbb C^q\to\mathbb C^s\) satisfying \(\mathcal OJ=I_q\). Thus \(m+q=s\). These are algebraic source and quotient maps; they are not selected from a density approximation. For every \(A\succ0\), set
\[
H_A=B^*AB,
\qquad R_A=J-BH_A^{-1}B^*AJ,
\]
\[
G_A=J^*AJ-J^*ABH_A^{-1}B^*AJ.
\tag{FE.16}
\]
The matrix \(H_A\) is positive definite because \(B\) is injective. Also \(\mathcal OR_A=I_q\) and \(B^*AR_A=0\). Every lift of \(u\) is uniquely \(R_Au+Bv\), and the orthogonality gives
\[
\|R_Au+Bv\|_A^2=u^*G_Au+v^*H_Av.
\tag{FE.17}
\]
Thus \(R_A\) is the unique least lift, \(G_A=R_A^*AR_A\succ0\), and
\(u^*G_Au=\min_{\mathcal Ox=u}x^*Ax\).

Apply this variational equality to (FE.12). For every \(u\), minimizing each of the three pointwise quadratic inequalities over exactly the same fibre gives
\[
G_{M_-}\preceq G_M\preceq G_{M_+}.
\tag{FE.18}
\]
All matrices on the outside are obtained by rational matrix arithmetic when the maps and the envelopes are rational. They enclose the full actual quotient metric before any determinant is taken. Consequently
\[
\det G_{M_-}\leq V:=\det G_M\leq\det G_{M_+}.
\tag{FE.19}
\]
To prove determinant monotonicity, for positive \(A\preceq D\), the Hermitian matrix \(A^{-1/2}DA^{-1/2}\) has every eigenvalue at least one by its quadratic form. Its determinant is therefore at least one, and \(\det D\geq\det A\). These auxiliary square roots prove the inequality and are not part of the rational certificate.

The determinant in (FE.19) has dimension \(q\). In the relative certificate (FE.15), minimization preserves the scalar factors and yields
\[
(1-\eta)G_{\widehat M}\preceq G_M\preceq(1+\eta)G_{\widehat M},
\quad
(1-\eta)^q\det G_{\widehat M}\leq V\leq
(1+\eta)^q\det G_{\widehat M}.
\tag{FE.20}
\]
The exponent is the dimension of the specified quotient, even if the polynomial source and its relation space are much larger. One can use (FE.18) directly when its separate matrix envelopes are sharper than the common factor \(\eta\).

Every determinant factor in the source-to-quotient change of coordinates is explicit. The matrix \(T=[J\ B]\) is invertible: a relation \(Ju+Bv=0\) gives \(u=0\) on applying \(\mathcal O\), and then \(v=0\) by injectivity. Its block Gram has Schur complement \(G_A\), so block triangular elimination proves
\[
\det G_A=\frac{|\det T|^2\det A}{\det(B^*AB)}.
\tag{FE.21}
\]
For a monic polynomial division presentation, the supplied coordinate map may have \(|\det T|^2=1\); (FE.21) records the general factor instead of presuming it. If a reference Gamma Gram \(M^\Gamma\) uses the same \(\mathcal O,B,J\), then
\[
\frac{V}{V^\Gamma}=\frac{\det G_M}{\det G_{M^\Gamma}}
\in\left[\frac{\det G_{M_-}}{\det G_{M^\Gamma}},
\frac{\det G_{M_+}}{\det G_{M^\Gamma}}\right].
\tag{FE.22}
\]
This is the exact arithmetic correction \(T_N\) in the delivered notation, with the original reference denominator retained.

For two consecutive admitted source degrees carrying the same quotient, independently computed bounds \(v_-^{\mathrm{lo}},v_-^{\mathrm{hi}}\) and \(v_+^{\mathrm{lo}},v_+^{\mathrm{hi}}\) imply
\[
\frac{v_-^{\mathrm{lo}}}{v_+^{\mathrm{hi}}}
\leq\frac{V_-}{V_+}\leq
\frac{v_-^{\mathrm{hi}}}{v_+^{\mathrm{lo}}}.
\tag{FE.23}
\]
Both denominators are positive by the preceding certificates. This is finite certified control of a consecutive quotient-volume ratio. It proves no bound uniform in an uncomputed degree. The parent's exact nested-source Schur identity retains the correlation between the two degrees and can improve these separate-envelope bounds.

When \(m=0\), all boundary terms in (FE.16) are absent and \(G_A=J^*AJ\). When \(q=0\), the quotient matrix is the unique \(0\)-by-\(0\) matrix and its determinant is one. Formulas (FE.19)--(FE.22) then give exactly one. A nonzero analytic seed does not change that zero-dimensional quotient.

## 5. Why finite positivity needs no global positive density floor

The exact scalar density \(w^{*k}\) is nonnegative and has mass \((\int w)^k>0\). Its positivity set has positive Lebesgue measure. A nonzero one-variable polynomial has finitely many real roots: repeated division by a linear factor lowers its finite degree, so it cannot have more distinct roots than its degree. Therefore \(|P(u)|^2w^{*k}(u)\) is positive on a set of positive measure for every nonzero \(P\), and its integral is strictly positive. This proves positive definiteness of every finite source Gram with linearly independent polynomial columns. It also proves positive definiteness of every injective relation Gram.

This argument permits the density to approach zero arbitrarily closely and permits real zeros. It supplies the exact logical reason a finite matrix can be positive definite while no pointwise uniform positive lower bound is available. The interval certificate obtains an actual finite quantitative margin from the moment entries themselves. In any sequence of coefficient enclosures whose radii tend to zero and whose centers tend to the actual coefficients, (FE.6)--(FE.12) give entry errors tending to zero at fixed \(k,N\). Since a finite positive definite Gram has a positive least eigenvalue, its lower envelope is positive definite for every sufficiently accurate member of that sequence. This last statement concerns fixed dimension and the indicated limit; it supplies no rate uniform in \(k,N\), and does not claim that uncomputed coefficient enclosures have been produced.

## 6. Actual theta seed: a certified all-k degree-one source

This section uses the existing proved infinite-tail enclosures, not the new delivery's floating-point estimates. The exact local input is `work/toda_theta_input_tail_result_normal_20260912.json`, accompanied by `work/toda_theta_input_tail_20260912.tex`, equations (TI.19), (TI.23), (TI.27)--(TI.31). The receipt records checker SHA-256 `db01839848cb6b67d24f5702789f6b9eb27d523a80c40cc58b25b9634ce101c5`, 256-bit Arb arithmetic, integer cutoff eight, and the proved infinite tail. The accompanying new checker pins the input receipt hash before using its exact rational endpoints.

Write \(\mu=\int w_1(t)dt=M_1(0)\), \(\nu=\int t^2w_1(t)dt=M_1''(0)\). The recorded rational decimal enclosures are
\[
1.2790072478464851404795335922671932744916
<\mu<
1.2790072478464851404795335922671932744919,
\]
\[
13.0555493025705584353926846581231936824343
<\nu<
13.0555493025705584353926846581231936824346.
\tag{FE.24}
\]
The exact dyadic endpoints in that same receipt are stronger and are used by the new checker. The seed is even, so its first moment is exactly zero. Expanding \((t_1+\cdots+t_k)^2\), every cross term integrates to zero and every diagonal term gives \(\nu\mu^{k-1}\). Thus in the actual original sum-variable basis \((1,u)\),
\[
M_{1,k}^{\mathrm{sum}}=
\begin{pmatrix}\mu^k&0\\0&k\mu^{k-1}\nu\end{pmatrix}.
\tag{FE.25}
\]
The coordinate map to the original spectral basis \((1,S)\), \(S=k/2+iu\), has columns
\[
T_k=\begin{pmatrix}1&k/2\\0&i\end{pmatrix},\qquad
M_{1,k}^{S}=T_k^*M_{1,k}^{\mathrm{sum}}T_k
=\begin{pmatrix}
\mu^k&(k/2)\mu^k\\
(k/2)\mu^k&(k^2/4)\mu^k+k\mu^{k-1}\nu
\end{pmatrix}.
\tag{FE.26}
\]
The inverse coordinate matrix is \(T_k^{-1}=\begin{pmatrix}1&ik/2\\0&-i\end{pmatrix}\). Multiplying either way gives the identity, and \(|\det T_k|^2=1\), so the exact determinant is \(k\mu^{2k-1}\nu\) in both bases. This proves the typed source-coordinate correspondence including the phase \(i\), the shift \(k/2\), and the complete mass.

Denote the lower and upper endpoints in (FE.24) by \(\mu_-,\mu_+,\nu_-,\nu_+\). Since all four are positive, for every integer \(k\geq1\),
\[
\operatorname{diag}(\mu_-^k,k\mu_-^{k-1}\nu_-)
\preceq M_{1,k}^{\mathrm{sum}}
\preceq\operatorname{diag}(\mu_+^k,k\mu_+^{k-1}\nu_+).
\tag{FE.27}
\]
These are exact rational SPD certificates at every specified integer \(k\); their positivity follows directly from the displayed factors. Congruence by the exact \(T_k\) gives the certificates in the original spectral coordinates. This all-\(k\), fixed-degree statement follows from the algebraic formula, not from testing finitely many values of \(k\).

At \(\lambda=13/4\), \(\alpha=13/2\), the reference mass is exactly
\[
c_{13/4}=2^{-11/2}\Gamma(13/2)
=\frac{10395}{2048}\sqrt{\frac\pi2}.
\tag{FE.28}
\]
Indeed \(\Gamma(13/2)=(11\cdot9\cdot7\cdot5\cdot3\cdot1)2^{-6}\Gamma(1/2)\), \(\Gamma(1/2)=\sqrt\pi\), and \(2^{-11/2}=1/(32\sqrt2)\). Since \(b_2^{(13/4)}(t)=t^2-13/2\), the exact first two nonzero coefficient formulas are
\[
c_{B,0}=\frac\mu{c_{13/4}},\qquad
c_{B,2}=\frac{\nu-(13/2)\mu}{c_{13/4}\,2!(13/2)(15/2)}.
\tag{FE.29}
\]
The associated first source-determinant correction is exactly
\[
Q_0=\frac{X_2X_0}{X_1^2}=\frac\nu{(13/2)\mu},
\qquad X_0=1,\quad X_1=(\mu/c_{13/4})^k,
\quad X_2=(\mu/c_{13/4})^{2k}\frac\nu{(13/2)\mu}.
\tag{FE.30}
\]
To verify this, the Gamma source determinants in dimensions one and two are respectively \(c_{13/4}^k\) and \(c_{13/4}^{2k}k(13/2)\), whereas (FE.25) gives the arithmetic determinants \(\mu^k\) and \(k\mu^{2k-1}\nu\). Dividing exactly yields (FE.30), retaining every mass factor. Therefore \(a_1^{(k)}=k(13/2)Q_0=k\nu/\mu\). The coefficient checker certifies (FE.29)--(FE.30) from the pinned actual seed intervals and a fresh Arb enclosure of the exact constant (FE.28).

The newly executed certificate gives the following strict decimal enclosures. Every endpoint is an exact decimal rational and each interval has width \(3\cdot10^{-40}\).

| Actual quantity | Lower endpoint | Upper endpoint |
|:--|:--|:--|
| \(c_{13/4}\) | 6.3614260045872192926298535487331092297380 | 6.3614260045872192926298535487331092297383 |
| \(c_{B,0}\) | 0.2010566886927858658099161632202187798614 | 0.2010566886927858658099161632202187798617 |
| \(c_{B,2}\) | 0.0076454429994864011881338514807939967436 | 0.0076454429994864011881338514807939967439 |
| \(Q_0\), every \(k\geq1\) | 1.5703945774593417982870401926519315653839 | 1.5703945774593417982870401926519315653842 |

The checker ran successfully in normal and optimized Python. Their complete output records are identical except for the recorded optimization flag. Both negative-control executions exit with code one on the deliberate false assertion \(Q_0<1\), and neither creates a successful result file. Validation uses explicit exceptions, so optimized Python retains the checks. These runs perform no new quadrature: they transfer the previously proved infinite-tail intervals through the exact formulas above. The Gamma constant uses a fresh outward Arb evaluation of (FE.28).

The checker is `work/gamma_seed_coefficient_certificate_20260913.py`, SHA-256 `f1f5adc54e750545856c47bef10fbdb0519ff50454d9685d970b412047553c6e`; normal result `work/gamma_seed_coefficient_result_normal_20260913.json`, SHA-256 `c3ebae40e6596b97783e89f8b476e66979af66c2b5bee8c69d1a5469e6f575bf`; optimized result `work/gamma_seed_coefficient_result_optimized_20260913.json`, SHA-256 `e545ebebad669e619ceb2eb5c2df11af200bf7c499fbf4d54194c14ede3c8f38`; validation receipt `work/gamma_seed_coefficient_validation_20260913.json`, SHA-256 `e3ce0072222f4801b07dab743c888a2546fa98e24109a3189a52d3e38b82619d`. The preserved input receipt hash is `2d5ebb1a40f1f33cff8d227ae57d68fb3ae0a18d084b74973d08fcf2c1cc32cc`.

For this seed \(h=1\), the finite packet quotient has dimension zero. Equations (FE.25)--(FE.30) certify source observations and Gamma correction data; their quotient determinant remains one as proved above. No value of an actual nonempty packet polynomial or of an uncomputed higher-degree arithmetic determinant is supplied here.

## 7. Review outcome and propagation points

The delivered finite-coefficient claim is correct with the full relation-degree restriction. The coefficient map is the finite homogeneous map (FE.1)--(FE.4), followed by the original quotient minimization (FE.16); the composition keeps the original measure, packet columns, and quotient coordinates. Equations (FE.6)--(FE.14) give a completely explicit finite certificate from actual coefficient enclosures to positive definite rational Hermitian envelopes. Equations (FE.18)--(FE.23) transfer those envelopes to quotient metrics and consecutive volume ratios with quotient dimension \(q\), without substituting a global density floor for missing information. Equations (FE.25)--(FE.30) provide an actual all-tensor-degree, degree-one source instance from the previously certified theta seed. The remaining higher-degree numerical inputs are neither assumed nor declared computed by this review.
