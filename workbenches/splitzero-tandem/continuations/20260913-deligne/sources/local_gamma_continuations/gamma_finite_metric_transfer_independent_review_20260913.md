# Independent full-source review of finite Gamma metric transfer

Review date: 2026-09-13. The reviewed mathematical source is `work/gamma_finite_metric_transfer_20260913.tex`, every paragraph from the declaration of the original packet through the verification scope, including all formulas GMT.1–GMT.42 and GMT.29a–GMT.29b. The accompanying source `work/gamma_finite_metric_transfer_check_20260913.py` was also read in full, including its five deliberate formula changes and the later bounded-cap and representative-coefficient comparisons. This review records derivations and exact independent evaluations; it does not infer an all-degree theorem from a finite calibration.

The final source and checker pins are recorded in the receipt accompanying this review. No author-owned source file was edited by this reviewer. The author repaired the endpoint criterion after GMT.19, the strict-envelope argument preceding GMT.42, the cosine-bound sentence, and the coefficient/reference-mass notation collision in response to the review. Those corrections are audited below.

## 1. Original packet, source, and relation maps: GMT.1–GMT.4

The original entire function is \(g=2\xi\), with the stated factors \(s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\). If a selected zero \(\rho\) has its complete order \(m\) in \(h\), write locally \(g(s)=(s-\rho)^m a(s)\), with \(a(\rho)\ne0\), and \(h(s)=(s-\rho)^m b(s)\), with \(b(\rho)\ne0\). Then \(v_h=a/b\) is analytic and nonzero there. This proves the local unit property at each selected component, including its full jet. The coefficient recursion written in the source is obtained from the coefficient of \(t^n\) in \((\sum a_jt^j)(\sum b_jt^j)=1\) modulo \(t^m\). Coprime powers of distinct linear factors have Bezout coefficients, so the Chinese remainder map is an exact algebra isomorphism and its inverse reconstructs the unit in \(\mathbb C[s]/(h)\).

The sum variable is literally \(u=t_1+\cdots+t_k\), and the spectral coordinate is \(S=k/2+iu\). The map \((t_1,\ldots,t_k)\mapsto(t_1,\ldots,t_{k-1},u)\) has triangular derivative with final diagonal entry one. Consequently the scalar pairing is exactly the integral in GMT.2 with \(m_{h,k}=w_h^{*k}\). Its total mass is \(\mu_h^k\); no Jacobian or factor \(k\) is missing. The complex amplitude \(\prod_i v_h(1/2+it_i)/\sqrt{2\pi}\) is explicitly retained before taking this quadratic observation.

For the tensor algebra \(A=\mathbb C[s_1,\ldots,s_k]/I\), multiplication by \(S\) is an endomorphism of a finite-dimensional complex vector space and hence has a nonzero annihilating polynomial. Thus \(I\cap\mathbb C[S]\) contains a nonzero polynomial. Its least-degree monic member \(\chi\) divides every other member: divide by \(\chi\), and the remainder still belongs to the ideal intersection; a nonzero remainder would contradict minimal degree. This proves the exact kernel in GMT.3. For \(N\geq q-1\), every quotient class has its degree-less-than-\(q\) representative, proving surjectivity of \(J_N\). Its kernel consists of \(\chi\mathcal P_{N-q}\), because ordinary degree adds under multiplication by a nonzero monic polynomial.

The tensor unit \([v_h]_h^{\otimes k}\) is invertible in \(A\). Therefore the kernel of \(\eta[P]=[v_h]_h^{\otimes k}[P(S)]_I\) is exactly the kernel already proved, and the induced map from \(\mathbb C[S]/(\chi)\) is injective. The coefficient matrix \([E_N,B_N]\) has diagonal entries one and no entries below its diagonal in the written degree order: the leading degree of its column numbered \(q+j\) is \(q+j\), with coefficient one. Its determinant is one. Moving the \(q\)-column quotient block past the \(N-q+1\)-column relation block contributes the exact sign \((-1)^{q(N-q+1)}\).

For GMT.4, monic division in each tensor variable expresses \(\chi(S)\) as \(\sum_i h(s_i)Q_i(\mathbf s)\) because its remainder modulo all the \(h(s_i)\) is zero. In the stated tensor differential, the component in position \(i\) has sign \((-1)^{i-1}\). The same sign is placed in front of the corresponding primitive, so their product is \(+1\). Using \(h(D)F_h=\Theta\phi_0\) then produces \(\chi(\sum D_i)P(\sum D_i)F_h^{\otimes k}\), the original relation source. This verifies both the boundary map and its orientation.

The zero-division operator also has the stated sign. With \(A(x)=\int_x^\infty F(y)y^{\rho-1}dy\), differentiation gives \(-x\partial_x(x^{-\rho}A)=\rho x^{-\rho}A+F(x)\), hence \((D-\rho)S_\rho F=F\). If the Mellin value at \(\rho\) vanishes, \(A(x)=-\int_0^x F(y)y^{\rho-1}dy\), giving the lower integral with the displayed minus sign. The two expressions provide the corresponding endpoint decay bounds, and successive division removes the complete selected multiplicities. The Mellin integral of the declared \(\phi_0\) is \(\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\) on \(\Re s>-2\): substitution \(y=\pi x^2\) produces the two Gamma terms and the recurrence combines them without changing the original coefficients \(4\pi^2,-6\pi\). The small-\(x\) behavior is order \(x^2\), explaining the domain \(\Re s>-2\). The theta sum first converges in the declared right half-plane and supplies the factor \(2\zeta(s)\).

The empty packet remains \(\chi=1\), quotient dimension zero, and determinant one. The analytic seed and the supported zero/absence labels remain present in their stated maps. Every later matrix formula has a unique empty-matrix interpretation; it creates no new packet.

## 2. Gamma scale, convolution, and coefficient evaluation: GMT.5–GMT.13

The factor two in the beta integral is essential and correct. Starting from the beta integral on \((0,\infty)\) and making the logarithmic substitution \(v=e^{2y}\) gives
\[
\frac{|\Gamma(\lambda+it/2)|^2}{\Gamma(2\lambda)}
=2\int_{\mathbb R}e^{ity}(2\cosh y)^{-2\lambda}dy.
\]
Division by \(2\pi\), followed by Fourier inversion, therefore yields
\(\int e^{iyt}r_\lambda(t)dt=2^{1-2\lambda}\Gamma(2\lambda)(\cosh y)^{-2\lambda}\), including the complete \(c_\lambda\). The integrand in \(y\) and each of its derivatives decays exponentially, so repeated integration by parts gives integrable polynomial decay of its Fourier transform. Gamma-contour rotation gives the additional exponential estimate needed for the Laplace transform: for \(t\geq0\), rotate by \(0<\varphi<\pi/2\), obtaining
\[
|\Gamma(\lambda+it/2)|
\leq e^{-\varphi t/2}\Gamma(\lambda)(\cos\varphi)^{-\lambda}.
\]
For \(t<0\), rotate in the opposite direction. Squaring proves the source's \(e^{-\varphi|t|}\) bound. For \(|a|<\pi/2\), choose \(|a|<\varphi<\pi/2\); this provides an integrable dominating function for the complex Laplace integral on any smaller strip. Analytic continuation from the Fourier axis gives \(c_\lambda(\cos a)^{-2\lambda}\). Taking the product transform proves the mass \(C_k=c_\lambda^k\), exponent \(\beta=2k\lambda\), and the exact convolution scalar \(C_k/c_{k\lambda}\) in GMT.6.

For real sufficiently small \(z\), the logarithms of \(1\pm iz\) are \(\tfrac12\log(1+z^2)\pm i\arctan z\). Substituting them proves the equality between the two generating expressions in GMT.7 with the sign \(+t\arctan z\). Differentiation gives \((1+z^2)\partial_zG=(t-2\lambda z)G\). Comparing coefficient \(z^j/j!\) gives the exact recurrence \(b_{j+1}=tb_j-j(j+2\lambda-1)b_{j-1}\). Its leading coefficient remains one.

The external classical-name attribution was independently checked against [DLMF 18.23.7](https://dlmf.nist.gov/18.23.E7). Substituting its variables \(x=t/2\), \(\varphi=\pi/2\), gives precisely the two factors in GMT.7; multiplying the classical coefficient by \(j!\) gives the displayed monic coefficient. The proof of the scale and norm in the source itself does not depend on this attribution.

To verify GMT.8, multiply the two real generating functions with parameters \(z,w\) and integrate. The Laplace transform has argument \(\arctan z+\arctan w\). The cosine addition formula cancels the two factors \((1+z^2)^{-\lambda}\) and \((1+w^2)^{-\lambda}\), leaving exactly \(c_\lambda(1-zw)^{-2\lambda}\). Local exponential domination permits coefficient differentiation. Its coefficient \(z^iw^j\) is zero for \(i\ne j\), and for \(i=j\) it is \(c_\lambda(2\lambda)_j/j!\). The generating denominators contribute \((j!)^2\), yielding the squared monic norm \(c_\lambda j!(2\lambda)_j\). Applying the exact convolution scalar gives \(C_k j!(\beta)_j\), with no extra factor \(k\) or \(2^j\).

The arithmetic multiplier identity \(w_h=B r_\lambda\) follows directly from its complex amplitude and the original \(2\pi\). Beyond twice the root radius, each factor of \(h(1/2+it)\) has modulus at least \(|t|/2\). Combining the exact two polynomial factors in \(g\) with the displayed zeta estimate bounds \(B\) by a constant times \(|t|^{6-2\deg h}\) at \(\lambda=1/4\). Increasing \(\lambda\) by an integer \(L\) divides this by the squared product \(\prod_{j<L}|j+1/4+it/2|^2\), contributing \(|t|^{-2L}\) at large \(|t|\). Thus the stated \(L\geq\max(0,3-\deg h)\) is sufficient. The exact entire quotient is bounded on each compact real interval. This gives the claimed \(L^2(r_\lambda)\) domain. For the more general nonnegative nonzero \(B\in L^2(r_\lambda)\), Cauchy--Schwarz against the reference moments gives every polynomial moment needed below.

GMT.9 is the adjoint conditional integral associated with the literal sum. Fubini proves \(\|U_\Sigma f\|^2=\|f\|^2\). Pairing an arbitrary tensor function against \(U_\Sigma f\) yields exactly the displayed integral for \(C_\Sigma\), including its positive denominator \(r_{\lambda,k}(u)\). Hence \(C_\Sigma U_\Sigma=I\), \(U_\Sigma C_\Sigma\) is an orthogonal projection, and \(F\mapsto(C_\Sigma F,(I-U_\Sigma C_\Sigma)F)\) has the stated inverse and direct-sum norm. The normal component is retained as an actual vector.

The finite addition formula obtained by multiplying generating functions has coefficient \(n!/\prod n_i!\). Pairing a term with \(B^{\otimes k}\) supplies \(\prod c_\lambda n_i!(\alpha)_{n_i}c_{B,n_i}\). Cancellation of precisely the \(n_i!\) leaves \(C_k n!\prod(\alpha)_{n_i}c_{B,n_i}\). Summing finite compositions gives GMT.11. This establishes the factorial and all tensor cross terms in GMT.12 independently of an infinite-series interchange.

The author now uses the exact typed alias \(c_{B,j}=c_{h,j}\) for the arithmetic multiplier, reserving \(c_\lambda\) for the reference mass. This removes the collision at \(\lambda=1\), where reference mass \(c_1\) and degree-one coefficient are different objects. The alias changes no value, coordinate, or formula. In the larger input domain, the explicit measures are \(w_B=B r_\lambda\) and \(m_{B,k}=w_B^{*k}\); for the specified arithmetic input they are exactly \(w_h,m_{h,k}\). The auxiliary calibration therefore uses a declared input of the same coefficient map, without reassigning the original arithmetic density. The finite map is homogeneous of degree \(k\) in the original coefficient tuple; its codomain is the Hermitian form in the declared source basis. The full complex-conjugate test \(\overline{p_a(c+iu)}p_b(c+iu)\) is retained, and relation degree includes all of \(\chi\).

Finally \(p_j^\Gamma(S)=i^j b_j((S-c)/i)\) has leading coefficient one in \(S\). On the observed line it equals \(i^jb_j(u)\), so its diagonal reference pairing has phase \((-i)^ji^j=1\). Therefore the monic triangular congruence in GMT.13 gives precisely \(C_kj!(\beta)_j\). Its inverse and the transformed reduction \(J_NU_N\) are correctly stated.

## 3. Finite errors and the full polynomial tests: GMT.14–GMT.17

For coefficient errors \(\delta_j\), expand \((\widehat A+\delta A)^k-\widehat A^k\). Every term contains at least one error factor. Replacing each central coefficient by its absolute value and every error coefficient by its given radius bounds that coefficient by \([z^n]((A_++E_+)^k-A_+^k)\). Only indices through \(n\) enter, so finite truncation introduces no additional term at \(n\leq2N\). Multiplying by the retained \(C_kn!L_{ab,n}\) and summing absolute values proves GMT.15. The instructions to propagate any mass enclosure and any enclosure of an original \(\chi\) coefficient before matrix certification are mathematically necessary and correctly included.

Let \(B_L\) be the orthogonal polynomial projection. Then \(\|B_L\|\leq\|B\|\). The exact tensor difference expands into \(k\) terms with one \(B-B_L\) factor and \(k-1\) factors each of norm at most \(\|B\|\), proving the displayed \(L^2\) bound after contraction by \(C_\Sigma\). A coefficient of total degree at most \(L\) uses only one-factor indices at most \(L\), so its moment pairing with the error is exactly zero. The nonzero part of the specified polynomial test is therefore \(\sum_{n>L}L_{ab,n}b_n\). Its squared reference norm is exactly \(C_k\sum_{n>L}n!(\beta)_n|L_{ab,n}|^2\). Cauchy--Schwarz gives GMT.16, including a literal zero when the sum is empty. This is stronger than pairing against the entire test norm and requires no pointwise positivity of a truncated multiplier.

For GMT.17, expand \(P(c+iu)=\sum a_jb_j(u)\). Weighted Cauchy--Schwarz gives
\[
|P(c+iu)|^2\leq
\left(\sum_j|a_j|^2C_kj!(\beta)_j\right)
\left(\sum_j\frac{b_j(u)^2}{C_kj!(\beta)_j}\right).
\]
The first factor is exactly \(\|P\|_\Gamma^2\), and the second is the written kernel. Multiplying by \(|E_k|r_{\lambda,k}\), integrating, and applying Cauchy--Schwarz proves GMT.17. The kernel squared has degree \(4N\) and finite reference integral. Every denominator and the original mass appear in the correct places.

## 4. Least lifts and the signed resolvent derivatives: GMT.18–GMT.21

Since \(J_N\) is surjective, \(J_N^*x\ne0\) for nonzero \(x\); thus \(x^*J_NH^{-1}J_N^*x>0\). The inverses in GMT.18 exist. Multiplying \(J_NR=I\) and \(B_N^*HR=B_N^*J_N^*G=0\) proves the right-inverse and boundary-orthogonality conditions. Every other lift is \(Rx+B_Ny\); expanding its squared norm gives the exact orthogonal sum with the boundary Gram. This proves uniqueness of the minimum lift and its quotient metric without an external choice of representative.

Along \(H_t=H_0+tE\), the boundary Gram is \(A_t=A_0+tF\succ0\). Since \(B_N^*H_tR_0=tC\), subtracting \(tB_NA_t^{-1}C\) gives the unique boundary-orthogonal right inverse. Expanding its norm produces two copies of \(-t^2C^*A_t^{-1}C\) and one compensating positive copy, leaving the negative quadratic remainder in GMT.19. The sign is correct. The full remainder vanishes at \(t=0\) for every \(C\); for \(t>0\), positivity of \(A_t^{-1}\) makes it zero exactly when \(C=0\). The author has repaired the initial endpoint omission and explicitly stated both cases. Empty boundary blocks give the zero form throughout.

Differentiating \(J_NR_t=I\) puts \(R_t'\) in \(\ker J_N=\operatorname{im}B_N\). Differentiate \(B_N^*H_tR_t=0\), substitute \(R_t'=B_NY_t\), and solve \(A_tY_t=-B_N^*ER_t\), obtaining the first formula of GMT.20. In the derivative of \(R_t^*H_tR_t\), both terms involving \(R_t'\) vanish by boundary orthogonality, leaving \(G_t'=R_t^*ER_t\). Its derivative is
\[
G_t''=R_t'^*ER_t+R_t^*ER_t'
=-2(B_N^*ER_t)^*A_t^{-1}(B_N^*ER_t),
\]
because \(E\) is Hermitian and \(A_t^{-1}\) is Hermitian. This proves the negative semidefinite second derivative with its factor two. The independent checker described below verifies all three derivative identities symbolically in the full rational parameter \(t\), separately from the author's five finite segment points.

The lift difference has coefficients \(-tA_t^{-1}Cx\) in the actual relation basis; substituting this polynomial into GMT.4 gives its original theta primitive. The injection \(\eta\) is unchanged because the difference lies in the already identified kernel. The exact comparison map is therefore supplied at both the polynomial and original source levels.

For GMT.21, \(R-E_N\) is a boundary matrix, so \([R,B_N]=[E_N,B_N]\begin{psmallmatrix}I&0\\D&I\end{psmallmatrix}\) for a specified coefficient matrix \(D\). Both triangular changes have determinant one. The Gram in the new columns is \(\operatorname{diag}(G,B_N^*HB_N)\). Taking its determinant proves exactly \(V_N=\det H/\det(B_N^*HB_N)\). The source/relation determinant quotient is justified by this literal orientation and not by dropping a coordinate factor.

## 5. The two-degree denominator and Toda substitution: GMT.22–GMT.27

Write the explicit change of source coefficients as \(T=\begin{psmallmatrix}I&-H_-^{-1}C_D\\0&I_2\end{psmallmatrix}\). Direct multiplication gives \(T^*H_+T=\operatorname{diag}(H_-,W)\), while the quotient map becomes \(J_+T=[J_-,F_D]\). Inverting the diagonal source Gram and applying this reduction gives \(K_+=K_-+F_DW^{-1}F_D^*\), with no loss of the two added columns. Positivity of \(H_+\) implies \(W\succ0\); surjectivity at degree \(N-1\) follows from \(N\geq q\), so \(G_-\) exists.

Since \(V_- /V_+=\det K_+/\det K_-\), the matrix determinant identity changes the determinant to dimension two:
\[
\frac{V_-}{V_+}=\det(I_2+W^{-1}F_D^*G_-F_D)
=\frac{\det(W+Z_D)}{\det W}.
\]
The identity \(\det(I_2+A)=1+\operatorname{Tr}A+\det A\) proves the last expression in GMT.24. The product \(W^{-1}Z_D\) need not be Hermitian in the original coordinates, but it is similar to the positive semidefinite Hermitian matrix \(W^{-1/2}Z_DW^{-1/2}\), so the nonnegative-eigenvalue argument is valid. This proves the actual ratio is at least one.

The first new monic residual has squared norm \(W_{11}\). Orthogonalizing the second residual against the first subtracts \(W_{12}/W_{11}\) times the first and gives squared norm \(W_{22}-|W_{12}|^2/W_{11}=\det W/W_{11}\). Their norm ratio is therefore \(\det W/W_{11}^2\). This proves both powers in the denominator of GMT.25. The source-coordinate change between \(u\) monomials and \(S=c+iu\) monomials has diagonal entries \(1,i,\ldots,i^{d-1}\) in dimension \(d\), so determinant \(i^{d(d-1)/2}\) and Gram multiplier one. Each corresponding monic residual also has a unit-modulus leading phase. Thus these are the original monic source norms entering the Hankel--Toda recurrence.

The arithmetic/reference correction satisfies \(T_-/T_+=(V_-/V_+)/(V_-^\Gamma/V_+^\Gamma)\), yielding GMT.26 with both denominators present. A degree-\(N+1\) Gram requires coefficients through \(2N+2\), and the stated finite coefficient calculation provides exactly these entries before taking the indicated positive inverses. GMT.27 replaces the two scalar inputs in the inherited Toda upper expression by the independently proved exact formulas. It claims only that substitution, retaining the inherited omitted nonnegative squares in the referenced sharper identity. It introduces neither an equality case nor an unproved arithmetic degree bound.

## 6. Rational envelopes and the quotient exponent: GMT.28–GMT.31

With symmetric radii \(\varepsilon_{ij}\), the inequality
\(2|x_i||x_j|\leq(v_j/v_i)|x_i|^2+(v_i/v_j)|x_j|^2\)
gives \(|x^*(H-\widehat H)x|\leq\sum_i\delta_i|x_i|^2\). Thus GMT.28 is an actual Hermitian enclosure. The pivot congruence displayed in the source is correct: for \(A=\begin{psmallmatrix}a&b^*\\b&C\end{psmallmatrix}\), substitute \((x-a^{-1}b^*y,y)\), cancel both mixed terms, and retain \(a|x|^2+y^*(C-bb^*/a)y\). Positive exact pivots therefore prove positivity by induction.

The actual finite source form is positive definite: \(w_h\) is a nonzero nonnegative density with positive mass, as is its convolution. A nonzero polynomial has only finitely many real roots, while the density is positive on a set of positive Lebesgue measure. Its squared norm is therefore strictly positive. A finite independent polynomial basis gives the positive definite matrix. This proof permits the scalar density to have zeros or arbitrarily small values and does not posit a global pointwise lower bound. At fixed matrix dimension, convergence of all valid entry enclosures forces the diagonal envelope errors to zero. The actual positive least quadratic value on the unit sphere then proves eventual positivity of the lower matrices. The source correctly restricts this statement to refined actual inputs at fixed finite degree.

Substituting \(E_N-B_N(B_N^*HB_N)^{-1}B_N^*HE_N\) gives the Schur expression GMT.29 and its same least lift. For a fixed quotient vector, minimization of the lower, actual, and upper source quadratic forms over their identical affine fibre gives the two quotient inequalities. Determinant monotonicity follows by congruence with an inverse positive square root and multiplication of the resulting eigenvalues. This proves GMT.30 in dimension \(q\). Taking the corresponding principal submatrix of the original common source enclosure supplies the lower-degree envelopes, and dividing their positive determinants yields GMT.31.

The new original-coordinate representative bounds in GMT.29a–GMT.29b are also valid. Since \(\widehat H\succeq H^{\rm lo}\succ0\), its least lift \(\widehat R\) exists. Write \(A=B_N^*HB_N\), \(A^{\rm lo}=B_N^*H^{\rm lo}B_N\), and \(S_E=B_N^*(H-\widehat H)\widehat R\). The exact resolvent formula gives
\[
R(H)-\widehat R=-B_NA^{-1}S_E.
\]
The entrywise bounds on \(H-\widehat H\) give \(|(S_E)_{ai}|\leq s_{ai}\) with precisely the complete sums printed in the source. Inversion reverses the positive order \(A\succeq A^{\rm lo}\succ0\), so \(A^{-1}\preceq(A^{\rm lo})^{-1}\). For a positive matrix, its two-coordinate principal minor implies \(|A^{-1}_{ab}|^2\leq A^{-1}_{aa}A^{-1}_{bb}\). Its diagonal bounds and the arithmetic-geometric mean inequality then give
\[
|A^{-1}_{ab}|\leq\tfrac12\big((A^{\rm lo})^{-1}_{aa}+(A^{\rm lo})^{-1}_{bb}\big)=k_{ab}.
\]
Multiplying the three entrywise majorants yields exactly \(|(R(H)-\widehat R)_{ri}|\leq\sum_{a,b}|(B_N)_{ra}|k_{ab}s_{bi}\). All original source rows, relation columns, and quotient coordinates are retained.

The difference \(\widehat R-R(H)\) is a boundary and hence is \(H\)-orthogonal to \(R(H)\). Expanding its norm proves
\[
\widehat R^*H\widehat R-G(H)
=(R(H)-\widehat R)^*H(R(H)-\widehat R)
=S_E^*A^{-1}S_E.
\]
Positive inverse order bounds the latter by \(S_E^*(A^{\rm lo})^{-1}S_E\). On a vector \(x\), absolute values bound this by \(\sum_{i,j}\tau_{ij}|x_i||x_j|\), with \(\tau_{ij}\) exactly the source's sum of \(s_{ai}|(A^{\rm lo})^{-1}_{ab}|s_{bj}\). This matrix of nonnegative majorants is symmetric. The same weighted pair inequality used in GMT.28 therefore bounds that quadratic expression by \(x^*\Delta_Qx\), proving the complete q-dimensional upper form in GMT.29b. Empty boundary blocks give zero matrices throughout. The arithmetic primitive is obtained from the already established boundary coefficient map in GMT.4.

I independently verified the seven new representative checks using the rational calibration, including the full coefficient difference, its zero original quotient, the inverse entry bounds, both exact loss identities, and the positive upper form. The original new test checked nonnegative leading minors, which alone would not be a sufficient general positive-semidefinite test when its first pivot vanishes. For this fixture the first leading minor and determinant are both strictly positive; the author changed the test to strict positivity, making it a valid Sylvester positive-definite certificate. The theorem and its proof were already correct; this repair strengthens the executable verification.

The common relative factor has exponent \(q\), because scaling a source form by \(a>0\) scales every squared representative norm and its minimum by \(a\), while the minimizer stays the same. Hence \(G(aH)=aG(H)\), \(R(aH)=R(H)\), and its determinant scales by \(a^q\). Applying this twice gives the stated ratio multipliers. This argument retains the declared comparison scaling and never replaces the original arithmetic mass by one.

## 7. Every calibration value: GMT.32–GMT.39

The calibration uses \(\lambda=1\), \(k=2\), reference masses \(1/2\) and \(1/4\), and \(B(t)=1+t^2/4\). Because \(b_2^{(1)}=t^2-2\), its expansion is \(B=3/2+b_2^{(1)}/4\). Thus the coefficient series is \(A(z)=3/2+(2)_2z^2/4=3/2+3z^2/2\), and its square has coefficients \((9/4,9/2,9/4)\) at degrees zero, two, four. The degree-four term is the tensor cross term and cannot be omitted. For \(\beta=4\), the recurrence gives \(b_2=u^2-4\), \(b_3=u^3-14u\), \(b_4=u^4-32u^2+72\). Substitution into \(\sum d_nb_n/(4)_n\) gives exactly the polynomial in GMT.33.

I generated the one-factor reference moments independently from the derivatives of \(\tfrac12\sec^2 z\), rather than the author's Jacobi walk. Its even moments through degree ten are \(1/2,1,8,136,3968,176896\). Inserting the literal factor \(1+t^2/4\) gives the arithmetic even moments through degree eight \(3/4,3,42,1128,48192\). Their two-factor binomial expansion gives exactly \(9/16,9/2,117,5472,385272\) at degrees zero, two, four, six, eight; every odd moment is zero. Independently, the reference sum moments are derivatives of \(\tfrac14\sec^4 z\). These calculations verify the masses and every number in GMT.34.

Expanding \((1-iu)^a(1+iu)^b\) with those moments reproduces every entry of both matrices in GMT.35. The reduction and relation matrices in GMT.36 are obtained from \(\chi=S^2-2S-1\). Polynomial reduction gives \(S^2=2S+1\), \(S^3=5S+2\), hence the displayed \(J_3\), and literal multiplication by \(\chi\) gives the displayed \(B_3\). Their product is zero and \(\det[E_3,B_3]=1\).

Using the independent boundary-Schur formula \(R=E-B(B^*HB)^{-1}B^*HE\), rather than the author's inverse-source formula, reproduces every entry of \(R_3\), \(G_3\), and \(G_3^\Gamma\) in GMT.37. I also verified \(J_3R_3=I\) and \(B_3^*H_3R_3=0\) directly. The two-degree source Schur and residual quotient map reproduce exactly
\[
W=\begin{pmatrix}81&243\\243&3159\end{pmatrix},\quad
F_D=\begin{pmatrix}10&2\\0&28\end{pmatrix},\quad
Z_D=\frac14\begin{pmatrix}225&675\\675&16137\end{pmatrix}.
\]
Their determinant expressions give the actual ratio \(20191/4860\), reference ratio \(2071/450\), correction ratio \(100955/111834\), and \(a_3=30\). All are exact rationals. The denominators in GMT.25 and GMT.39 are reproduced independently. The actual ratio exceeds one while its correction relative to the Gamma ratio is less than one.

## 8. Bounded cap and strict rational endpoints: GMT.40–GMT.42

The cap is applied at exactly \(|t|=200\), since \(1+200^2/4=10001\). The difference is nonnegative and bounded by \(\tfrac14t^2r_1(t)\) on \(|t|>200\). For \(x\geq0\), the term of order \(r\) in the exponential series gives \(x^r\leq r!2^re^{x/2}\). On \(x>200\), multiplying its right side by \(e^{(x-200)/2}>1\) yields \(x^r\leq r!2^re^{-100}e^x\). Then
\[
\int_{|t|>200}|t|^r r_1(t)dt
\leq r!2^re^{-100}\int_{\mathbb R}e^{|t|}r_1(t)dt
\leq2c_1r!2^re^{-100}\sec^2(1).
\]
The final inequality uses \(e^{|t|}\leq e^t+e^{-t}\) and both Laplace transforms. Here \(2c_1=1\). The elementary identity \(1-\cos1=\int_0^1\sin x\,dx\leq\int_0^1x\,dx=1/2\) gives \(\sec^2(1)\leq4\). The author repaired the original indirect wording to this direct integral argument. Since \(e>2\), the inequality \(e^{-100}<2^{-100}\) is strict. For \(r=j+2\leq8\), multiplication by the original cap factor \(1/4\) gives the uniform strict moment bound \(8!/2^{92}\) in GMT.40.

The auxiliary one-factor moment \(\mu_6=1128\) was independently verified. For \(j\leq6\), \(|t|^j\leq1+|t|^6\) proves the common bound \(A_*=4515/4\). The tensor difference identity in the source is exact and has both positive terms. Expanding the absolute sum power gives the difference bound \(2^{n+1}A_*\epsilon_*\) for degree \(n\), hence \(128A_*\epsilon_*\) through degree six. The sum of absolute coefficients of the full spectral test is at most \(2^{a+b}\leq64\). Thus every source entry differs by at most \(8192A_*\epsilon_*\), which is strictly less than \(1/40000\) by exact integer comparison. The independent checker verifies this last rational comparison.

Four strictly bounded row entries give an operator error strictly smaller than \(10^{-4}I\). Thus GMT.41 is a strict positive-definite enclosure, not merely non-strict. The four listed lower leading minors were independently computed as
\[
703/1250,\quad253068751/10^8,\quad
102481960035937/(5\cdot10^{11}),\quad
4980299350501627807501/10^{16}.
\]
All are positive. Their successive quotients give the positive elimination pivots; the first pivot is the first minor. This proves positivity of the lower envelope in full rational arithmetic.

Strict source inequalities do imply strict quotient inequalities here. For a nonzero quotient vector \(u\), let \(R_Hu\) be the actual minimum lift. It is nonzero because its reduction is \(u\). Therefore
\[
u^*G_{\rm lo}u\leq(R_Hu)^*H_{\rm lo}(R_Hu)
<(R_Hu)^*H(R_Hu)=u^*G_Hu.
\]
For the upper comparison, evaluate the actual form at the upper minimum lift and use the same nonzero-vector argument. This is the strict-minimization reasoning now included by the author. It is the required justification for the two strict inequalities involving the unknown capped volume in GMT.42; rational cross multiplication alone would only compare the explicitly known endpoints.

I evaluated both rational quotient-Schur envelopes independently and obtained the exact lower and upper fractions printed in GMT.42. Their comparison with \(2071/450\) is a positive-denominator rational comparison. The lower fraction also exceeds one. Combining strict minimization with these exact endpoints proves \(V_1^{[200]}>V_3^{[200]}\) and \(T_1^{[200]}<T_3^{[200]}\) for the completely specified multiplier \(1\leq B^{[200]}\leq10001\). No numerical integration of the capped weight is required by that proof; its actual finite form is enclosed by the proved analytic tail and exact rational matrices.

This is a valid counterexample to deducing monotonic decrease of the relative Gamma correction solely from positivity and boundedness of a multiplier. The quotient polynomial is explicitly auxiliary. The exact relation to the arithmetic construction is through the same typed coefficient, source, relation, minimum-lift, and volume maps; it supplies no claim that an actual zeta packet has these coefficients or this behavior.

## 9. Executable scope and review result

The author checker was read in full. It uses exact SymPy polynomial/rational operations. Its moment inputs come from the Jacobi recurrence, and its second moment route uses the literal binomial tensor expansion. It verifies reference orthogonality, every source Gram entry through the coefficient map, the original conjugation, least-lift identities, the signed remainder, five points of the positive segment, both two-degree formulas, the quotient determinant orientation, rational envelopes, the bounded cap entry radius, the relative correction, and the endpoint comparison with the Gamma ratio. Its five fault switches remove the reference mass, remove the degree-four tensor cross term, reverse the quadratic sign, remove the first-factor conjugation, and remove one factor of \(W_{11}\). Each switch changes a specific equality test; the checks are explicit recorded Booleans, retained under optimized Python. The author reports two positive runs and ten mutant runs on the final checker; their pinned result records are separately verified in the attached review receipt.

The independent script `work/gamma_finite_metric_transfer_independent_check_20260913.py` uses a different moment construction from derivatives of \(\sec^2 z/2\) and \(\sec^4 z/4\), and a different quotient construction by boundary Schur elimination. It passed 37 explicit exact checks, including all printed calibration matrices and scalar values, every rational strict endpoint and positivity minor, the three resolvent derivative formulas as symbolic identities in the full parameter, and seven representative error/loss identities or bounds. It explicitly verifies that the full quadratic remainder vanishes at \(t=0\) with nonzero coupling, exposing the endpoint issue that has now been repaired. This independent run performs neither capped-weight quadrature nor Lean. Its successful result records the precise finite algebraic scope.

The complete reviewed argument is mathematically valid after the recorded repairs. The exact Gamma scale, source-coordinate factors, boundary-resolvent signs, second-derivative factor two, two-degree Schur denominator square, and strict bounded-counterexample enclosure have all been independently derived and checked. The proof preserves the original arithmetic objects and provides the explicit morphisms whenever it compares their source or quotient observations. It establishes finite transfer, an exact nonlinear metric correction, and a concrete obstruction to a proposed general relative-monotonicity route; it does not assert uncomputed nonempty-packet interval values or a uniform RH estimate.
