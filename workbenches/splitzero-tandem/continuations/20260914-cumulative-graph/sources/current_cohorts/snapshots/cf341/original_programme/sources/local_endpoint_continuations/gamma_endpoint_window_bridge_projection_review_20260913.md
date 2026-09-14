# Independent proof review: endpoint-window projection geometry

Date: 13 September 2026.

This review proves the proposed projection and finite-metric endpoint statements directly. It uses the immutable endpoint criterion at GitHub revision c720f40530eed2f5969dbabe94dfd3fddc0f507f and the parent task's endpoint-window definitions. It certifies the mathematics written below, rather than unseen later edits to the parent article. No Lean run, numerical experiment, or uncomputed arithmetic asymptotic estimate is used.

The constants in the proposed bounds are correct. One wording correction is necessary: at a zero of the nonnegative window logarithm, its square root need not be ordinarily differentiable. The integrated Lipschitz statement and the almost-everywhere derivative statement remain valid. Section 8 gives an exact positive-form counterexample to ordinary differentiability.

## 1. Original coordinates, quotient maps, and least lifts

Keep the original polynomial coordinate \(S=k/2+iu\), its original source mass, and the original fixed monic relation
\[
\chi(S)=S^q+\chi_{q-1}S^{q-1}+\cdots+\chi_0,\qquad q\geq1.
\tag{P.1}
\]
The coefficients may be complex. No assumption that the relation roots are real or simple is made. Write \(\mathcal P_a\) for the complex polynomials in the original \(S\), of degree at most \(a\). The ordered coefficient basis is \(1,S,\ldots,S^a\). Throughout the proof the Hermitian convention is conjugate-linear in the first argument:
\[
\langle x,y\rangle_{H_a}=x^*H_a y .
\tag{P.2}
\]
Fix an ambient degree \(m\), and let \(H_m\) be a positive-definite Hermitian matrix in that basis. Every \(H_a\), \(0\leq a\leq m\), is its leading principal submatrix. Thus inclusions of the original polynomial spaces preserve the actual inner product. The proof applies, in particular, when these are the Gram matrices of a positive original source measure. It also applies to any positive finite Hermitian form with these nested principal restrictions.

For \(a\geq q-1\), define
\[
\mathcal K_a=\chi\mathcal P_{a-q},
\qquad \mathcal P_{-1}=\{0\},
\qquad
J_a:\mathcal P_a\longrightarrow\mathbb C^q
\tag{P.3}
\]
where \(J_a\) gives the coefficients of the unique remainder of monic division by \(\chi\). In particular,
\[
\ker J_a=\mathcal K_a,\qquad
J_a I_a=I_{\mathbb C^q},\qquad
I_a x=\sum_{j=0}^{q-1}x_j S^j.
\tag{P.4}
\]
The quotient coordinates are unchanged for every \(a\). Let \(B_a\) be the coefficient matrix with columns \(\chi,S\chi,\ldots,S^{a-q}\chi\). Its columns are linearly independent because their highest degrees are distinct and their leading coefficients are one. Hence \(B_a^*H_aB_a\) is positive definite when there are columns. Set
\[
R_a=I_a-B_a(B_a^*H_aB_a)^{-1}B_a^*H_a I_a,
\quad
G_a=R_a^*H_aR_a,
\quad
V_a=\det G_a .
\tag{P.5}
\]
When \(a=q-1\), the subtracted term is the zero map. Equations (P.4) and (P.5) give
\[
J_aR_a=I,\qquad
B_a^*H_aR_a=0,\qquad
\mathcal L_a:=R_a\mathbb C^q
=\mathcal P_a\cap\mathcal K_a^\perp .
\tag{P.6}
\]
Indeed, the first two equations show that the range is contained in the displayed orthogonal complement, and both spaces have dimension \(q\). For a fixed quotient vector \(x\), any other representative is \(R_ax+w\), \(w\in\mathcal K_a\), so its squared norm is
\[
\|R_ax+w\|_{H_a}^2=x^*G_a x+\|w\|_{H_a}^2.
\tag{P.7}
\]
This proves the exact least-lift property and its uniqueness. It also proves \(G_a>0\) and \(V_a>0\).

All subsequent comparisons embed these original spaces in \(\mathcal P_m\). In particular, \(R_a\) in a common ambient formula means its coefficient inclusion into \(\mathcal P_m\), without changing its coefficients, quotient vector, or inner product.

## 2. Exact projection and the number of moving directions

Let \(q-1\leq a<b\leq m\). Let \(\Pi_b\) be the orthogonal projection in the original \(H_m\) inner product onto \(\mathcal L_b\). The identical remainder coordinates give
\[
R_ax-R_bx\in\mathcal K_b .
\]
The second vector belongs to \(\mathcal L_b\), which is orthogonal to \(\mathcal K_b\). Therefore
\[
\boxed{\Pi_bR_a=R_b.}
\tag{P.8}
\]
This is the typed morphism
\[
\Pi_b|_{\mathcal L_a}:\mathcal L_a\longrightarrow\mathcal L_b,
\qquad R_ax\longmapsto R_bx.
\]
It is bijective because both least-lift maps are injective and use the same quotient coordinates. By orthogonal decomposition,
\[
G_a-G_b=(R_a-R_b)^*H_m(R_a-R_b)\succeq0 .
\tag{P.9}
\]
The difference \(R_ax-R_bx\) is orthogonal to \(\mathcal K_a\), since each summand is, and belongs to \(\mathcal K_b\). Since \(\mathcal K_a\subset\mathcal K_b\), the space
\[
\mathcal K_b\cap\mathcal K_a^\perp
\]
has dimension
\[
\dim\mathcal K_b-\dim\mathcal K_a
=(b-q+1)-(a-q+1)=b-a.
\]
Consequently
\[
\operatorname{rank}(R_a-R_b)\leq s_{a,b}:=\min(q,b-a).
\tag{P.10}
\]
The map from \(\ker(R_a-R_b)\) to \(\mathcal L_a\cap\mathcal L_b\), sending \(x\) to \(R_ax\), is bijective. To prove surjectivity, if \(R_ax=R_by\), applying the same remainder map in degree \(b\) gives \(x=y\). Injectivity follows from \(J_aR_a=I\). Thus
\[
\dim(\mathcal L_a\cap\mathcal L_b)
=q-\operatorname{rank}(R_a-R_b)\geq q-(b-a).
\tag{P.11}
\]
This argument includes \(a=q-1\), when \(\mathcal K_a=\{0\}\); it never uses a negative-dimensional relation matrix.

## 3. Complete principal-angle blocks and the determinant loss

The maps
\[
U_a:\mathbb C^q\longrightarrow(\mathcal P_m,H_m),
\quad U_a=R_aG_a^{-1/2},
\qquad
U_b=R_bG_b^{-1/2}
\tag{P.12}
\]
are isometric coordinate maps onto the original \(\mathcal L_a,\mathcal L_b\). These are auxiliary maps; \(G_a,G_b,H_m\) and their literal masses are retained. The adjoint of a map into \((\mathcal P_m,H_m)\) uses \(H_m\). From (P.8),
\[
U_b^*\Pi_bU_a
=G_b^{1/2}G_a^{-1/2}.
\]
Hence the squared singular values of \(\Pi_b|_{\mathcal L_a}\) are exactly the eigenvalues of
\[
M_{a,b}=G_a^{-1/2}G_bG_a^{-1/2}.
\tag{P.13}
\]
They lie in \((0,1]\), since \(G_b>0\) and (P.9) holds. Denote them by \(\sigma_j^2\). The number \(t_{a,b}\) of values strictly less than one equals \(\operatorname{rank}(R_a-R_b)\): the kernels of \(I-M_{a,b}\) and \((R_a-R_b)G_a^{-1/2}\) agree by (P.9). Thus \(t_{a,b}\leq s_{a,b}\).

Here is the full two-dimensional block construction. Choose an orthonormal eigenbasis \(e_j\) of \(M_{a,b}\), and put
\[
v_j=U_ae_j,\qquad
w_j=\sigma_j^{-1}\Pi_bv_j.
\]
The \(v_j\) form an orthonormal basis of \(\mathcal L_a\). The \(w_j\) form an orthonormal basis of \(\mathcal L_b\), because
\[
\langle \Pi_bv_i,\Pi_bv_j\rangle
=\langle v_i,\Pi_bv_j\rangle
=\sigma_j^2\delta_{ij}.
\]
Moreover \(\langle v_i,w_j\rangle=\sigma_j\delta_{ij}\). If \(\sigma_j=1\), then \(\|v_j-w_j\|^2=0\), so \(v_j=w_j\). If \(\sigma_j<1\), put
\[
\tau_j=\sqrt{1-\sigma_j^2},
\qquad z_j=(w_j-\sigma_jv_j)/\tau_j.
\]
The inner-product identities just established give
\[
\langle v_i,z_j\rangle=0,\qquad
\langle z_i,z_j\rangle=\delta_{ij}.
\]
The planes \(\operatorname{span}(v_j,z_j)\) are pairwise orthogonal and orthogonal to the common vectors with \(\sigma_i=1\). In their ordered bases \((v_j,z_j)\),
\[
\Pi_a=
\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
\Pi_b=
\begin{pmatrix}\sigma_j^2&\sigma_j\tau_j\\
\sigma_j\tau_j&\tau_j^2\end{pmatrix},
\qquad
\Pi_a-\Pi_b=
\begin{pmatrix}\tau_j^2&-\sigma_j\tau_j\\
-\sigma_j\tau_j&-\tau_j^2\end{pmatrix}.
\tag{P.14}
\]
The square of the last matrix is \(\tau_j^2I_2\), and its trace is zero. Its two eigenvalues are \(+\tau_j,-\tau_j\). Both projections vanish on the orthogonal complement of these planes and their common subspace. This proves the exact trace-norm identity
\[
\boxed{\|\Pi_a-\Pi_b\|_1
=2\sum_{\sigma_j<1}\sqrt{1-\sigma_j^2}.}
\tag{P.15}
\]
The trace norm here is the trace norm in the original ambient Hilbert space. Transport by its isometry \(x\mapsto H_m^{1/2}x\) gives the same value in Euclidean coordinates.

Define the nonnegative determinant loss
\[
\delta_{a,b}=\log(V_a/V_b)
=-\log\det M_{a,b}
=\sum_j-\log\sigma_j^2.
\tag{P.16}
\]
For \(0<x\leq1\),
\[
-\log x-(1-x)=\int_x^1(1/t-1)\,dt\geq0.
\]
Finite Cauchy–Schwarz and (P.15) therefore give the two bounds
\[
\boxed{\|\Pi_a-\Pi_b\|_1
\leq2\sqrt{t_{a,b}\delta_{a,b}}
\leq2\sqrt{s_{a,b}\delta_{a,b}},\qquad
\|\Pi_a-\Pi_b\|_1\leq2s_{a,b}.}
\tag{P.17}
\]
When \(\delta_{a,b}=0\), every \(\sigma_j=1\); hence \(R_a=R_b\) and \(\Pi_a=\Pi_b\). There is no remaining direction on which the two projections can differ.

## 4. Metric derivatives in a fixed ambient source

Let \(H_m(t)>0\) be a continuously differentiable family on a compact real interval, with the same original coefficient coordinates and fixed \(\chi\). Let all lower-degree matrices remain its leading principal restrictions. Write
\[
E(t)=H_m'(t),\qquad
\Lambda(t)=H_m(t)^{-1/2}E(t)H_m(t)^{-1/2},
\qquad
\omega(t)=\lambda_{\max}(\Lambda(t))-\lambda_{\min}(\Lambda(t)).
\tag{P.18}
\]
Positive definiteness makes (P.5) continuously differentiable. Differentiating \(J_aR_a=I\), with the original remainder map fixed, gives \(J_aR_a'=0\), so every column of \(R_a'\) belongs to \(\mathcal K_a\). Orthogonality to \(R_a\) cancels both differentiated-lift terms:
\[
G_a'=R_a'^*H_mR_a+R_a^*ER_a+R_a^*H_mR_a'
=R_a^*ER_a.
\]
Here the common-ambient embeddings are fixed coefficient inclusions. Jacobi's determinant identity yields
\[
(\log V_a)'=\operatorname{Tr}(G_a^{-1}R_a^*ER_a)
=\operatorname{Tr}(\widehat\Pi_a\Lambda),
\quad
\widehat\Pi_a=H_m^{1/2}R_aG_a^{-1}R_a^*H_m^{1/2}.
\tag{P.19}
\]
The matrix \(\widehat\Pi_a\) is the Euclidean orthogonal projection onto the image of the original \(\mathcal L_a\) under \(H_m^{1/2}\); it has rank \(q\). Equation (P.19) differentiates the original determinant. No differentiated moving-frame term has been omitted: its cancellation was proved in the preceding displayed equation.

For the original monic orthogonal polynomial \(p_j(t)\) of degree \(j\), set
\[
\omega_j(t)=\|p_j(t)\|_{H_m(t)}^2>0,\qquad
\widehat Q_j=
\frac{H_m^{1/2}p_jp_j^*H_m^{1/2}}{\omega_j}.
\tag{P.20}
\]
Coefficient columns are used for \(p_j\) here. Its leading coefficient is the fixed number one, so \(p_j'\in\mathcal P_{j-1}\), while \(p_j\perp\mathcal P_{j-1}\). Differentiation therefore gives
\[
(\log\omega_j)'=\operatorname{Tr}(\widehat Q_j\Lambda).
\tag{P.21}
\]
The case \(j=0\) has \(p_0=1\) and the same formula. The projection \(\widehat Q_j\) has rank one. If \(n<m\), \(p_m\perp p_n\), so \(\widehat Q_m,\widehat Q_n\) are orthogonal projections onto orthogonal lines.

For any self-adjoint trace-zero matrix \(T\), let
\[
c(t)=\tfrac12\bigl(\lambda_{\max}(\Lambda(t))+
\lambda_{\min}(\Lambda(t))\bigr).
\]
Then \(\|\Lambda-cI\|_{\mathrm{op}}=\omega/2\) and
\[
|\operatorname{Tr}(T\Lambda)|
=|\operatorname{Tr}(T(\Lambda-cI))|
\leq\tfrac{\omega}{2}\|T\|_1.
\tag{P.22}
\]
For completeness, diagonalize \(T\) with real eigenvalues \(t_i\). The trace on the left is \(\sum_i t_i\langle e_i,(\Lambda-cI)e_i\rangle\); the absolute value of each expectation is at most \(\omega/2\), proving the inequality. This also verifies its use for noncommuting \(T,\Lambda\).

## 5. The two endpoint-window quantities

Fix integers \(n\geq q\), \(r\geq1\), and \(m=n+r\). Retain exactly the source quantities used by the endpoint criterion:
\[
U=\frac{\omega_m}{\omega_n}>0,\qquad
\mathcal R=\frac{V_{n-1}V_n}{V_{m-1}V_m}\geq1,
\qquad
L=\log\mathcal R\geq0,\qquad s=\min(q,r).
\tag{P.23}
\]
The first lower index is \(n-1\geq q-1\), so all least-lift matrices are defined by (P.5). The original endpoint expression is exactly
\[
\mathcal E_{n,r}=U^{1/(2r)}\sinh\!\left(\frac{L}{2r}\right)
=\frac{(U\mathcal R)^{1/(2r)}-(U/\mathcal R)^{1/(2r)}}2,
\tag{P.24}
\]
with positive real roots. This identity follows by substituting \(L=\log\mathcal R\) into the definition of the hyperbolic sine. It changes neither endpoint norm nor quotient volume.

Equations (P.21) and (P.22) imply
\[
(\log U)'=\operatorname{Tr}((\widehat Q_m-\widehat Q_n)\Lambda),
\qquad
\boxed{|(\log U)'|\leq\omega,}
\tag{P.25}
\]
because \(\widehat Q_m-\widehat Q_n\) has eigenvalues \(+1,-1\) and zeros, hence trace norm two.

Write
\[
\delta_1=\log(V_{n-1}/V_{m-1}),\qquad
\delta_2=\log(V_n/V_m),\qquad L=\delta_1+\delta_2.
\]
Both losses are nonnegative, and the degree difference in each pair is exactly \(r\). By (P.19),
\[
L'=\operatorname{Tr}(T\Lambda),\qquad
T=\widehat\Pi_{n-1}-\widehat\Pi_{m-1}
+\widehat\Pi_n-\widehat\Pi_m .
\tag{P.26}
\]
The trace of \(T\) is \(q-q+q-q=0\). Let \(t_1,t_2\) be the actual numbers of moving directions in these two pairs. Combining (P.17), the trace-norm triangle inequality, and (P.22) proves
\[
\begin{aligned}
|L'|
&\leq\omega\bigl(\sqrt{t_1\delta_1}+\sqrt{t_2\delta_2}\bigr)\\
&\leq\omega\sqrt{(t_1+t_2)L}
\leq\omega\sqrt{2sL},\\
|L'|&\leq(t_1+t_2)\omega\leq2s\omega.
\end{aligned}
\tag{P.27}
\]
The middle inequality is ordinary Cauchy–Schwarz on the two real vectors \((\sqrt{t_1},\sqrt{t_2})\) and \((\sqrt{\delta_1},\sqrt{\delta_2})\). Thus both proposed constants follow with their stated indices and the actual rank refinement.

At \(L=0\), \(\delta_1=\delta_2=0\), so both projection differences vanish by Section 3 and \(L'=0\). This pointwise statement about \(L\) is valid. It does not imply ordinary differentiability of \(\sqrt L\) at that point.

## 6. The square-root bound, including zeros

For \(\varepsilon>0\), the function \(\sqrt{L+\varepsilon}\) is continuously differentiable and (P.27) gives
\[
\left|\frac{d}{dt}\sqrt{L+\varepsilon}\right|
=\frac{|L'|}{2\sqrt{L+\varepsilon}}
\leq\sqrt{\frac s2}\,\omega
\frac{\sqrt L}{\sqrt{L+\varepsilon}}
\leq\sqrt{\frac s2}\,\omega .
\]
Integrate between any two parameter values \(t_0,t_1\) and then let \(\varepsilon\) decrease to zero. Continuity of the square root gives
\[
\boxed{
|\sqrt{L(t_1)}-\sqrt{L(t_0)}|
\leq\sqrt{\frac s2}\int_{t_0}^{t_1}\omega(t)\,dt
}
\tag{P.28}
\]
when \(t_1\geq t_0\). There is no division by zero in this proof. On a compact interval the continuous function \(\omega\) is bounded, so \(\sqrt L\) is Lipschitz. It is absolutely continuous and satisfies the corresponding derivative bound almost everywhere; wherever \(L>0\), ordinary differentiation gives it directly. Equation (P.28) is the form needed for endpoint comparison.

## 7. Exact positive-segment length and projective distance

Let \(H_0,H_1>0\) be two ambient source forms in the identical original basis, and follow their actual linear segment
\[
H(t)=(1-t)H_0+tH_1,\quad 0\leq t\leq1.
\]
It remains positive definite because for each nonzero \(x\), \(x^*H(t)x\) is a convex combination of two strictly positive numbers. Define
\[
M=H_0^{-1/2}H_1H_0^{-1/2}>0,\qquad
A(t)=I+t(M-I).
\]
Then \(H(t)=H_0^{1/2}A(t)H_0^{1/2}\). The explicit matrix
\[
W(t)=H(t)^{-1/2}H_0^{1/2}A(t)^{1/2}
\tag{P.29}
\]
is unitary, since \(W(t)W(t)^*=I\); being square and invertible, it also satisfies \(W(t)^*W(t)=I\). As \(A(t)\) is a polynomial in \(M\), the two commute. Direct multiplication now proves the exact unitary identity
\[
H(t)^{-1/2}(H_1-H_0)H(t)^{-1/2}
=W(t)\,A(t)^{-1/2}(M-I)A(t)^{-1/2}\,W(t)^*.
\tag{P.30}
\]
Thus, if the eigenvalues of \(M\) are \(\lambda_i>0\), those of the left side are
\[
f_t(\lambda_i)=\frac{\lambda_i-1}{1+t(\lambda_i-1)}.
\]
The derivative of \(f_t(\lambda)\) in \(\lambda\) is \(1/[1+t(\lambda-1)]^2>0\). Therefore its largest and smallest values come from \(\lambda_{\max}\) and \(\lambda_{\min}\). Integration gives the exact identity
\[
\boxed{
\int_0^1\omega(t)\,dt
=\log\lambda_{\max}-\log\lambda_{\min}
=:d_{\mathrm{proj}}(H_0,H_1).
}
\tag{P.31}
\]
The integral formula also covers eigenvalue one, whose integrand is zero.

This quantity is a metric on positive rays of forms. Here is a finite-dimensional proof of that assertion. The extreme eigenvalues are the extreme Rayleigh quotients \(x^*H_1x/(x^*H_0x)\), by substituting \(y=H_0^{1/2}x\) and diagonalizing \(M\). They are the optimal positive numbers \(\alpha,\beta\) for
\[
\alpha H_0\preceq H_1\preceq\beta H_0.
\]
Multiplying either form by a positive scalar multiplies both \(\alpha,\beta\) by the same positive factor, so \(\log(\beta/\alpha)\) is unchanged. Reversing the forms replaces the extrema by \(1/\beta,1/\alpha\), proving symmetry. The distance vanishes exactly when \(\alpha=\beta=c\), which forces \(H_1=cH_0\). Finally, inequalities for \((H_0,H_1)\) and \((H_1,H_2)\) compose to
\[
\alpha_{01}\alpha_{12}H_0\preceq H_2
\preceq\beta_{01}\beta_{12}H_0 .
\]
The optimal extreme ratio for \((H_0,H_2)\) is at most the ratio of these two displayed coefficients, proving the triangle inequality.

Equations (P.25), (P.28), and (P.31), applied on the positive segment with the same fixed relation, yield
\[
\boxed{
|\log U(H_1)-\log U(H_0)|\leq d_{\mathrm{proj}}(H_0,H_1),
\quad
|\sqrt{L(H_1)}-\sqrt{L(H_0)}|
\leq\sqrt{\frac s2}\,d_{\mathrm{proj}}(H_0,H_1).
}
\tag{P.32}
\]
These are finite-degree identities and estimates between the exact original source quantities. They neither assume nor establish a growing-window arithmetic estimate.

For a directly usable endpoint enclosure, put \(d=d_{\mathrm{proj}}(H_0,H_1)\), \(b=\sqrt{s/2}\,d\), and
\[
L_-=\max(0,\sqrt{L(H_0)}-b)^2,\qquad
L_+=(\sqrt{L(H_0)}+b)^2.
\]
The two quantities in (P.23) satisfy
\[
U(H_0)e^{-d}\leq U(H_1)\leq U(H_0)e^d,
\qquad L_-\leq L(H_1)\leq L_+.
\]
Since \(U^{1/(2r)}\sinh(L/(2r))\) is nondecreasing in both positive \(U\) and nonnegative \(L\),
\[
\boxed{
U(H_0)^{1/(2r)}e^{-d/(2r)}
\sinh\!\frac{L_-}{2r}
\leq\mathcal E_{n,r}(H_1)
\leq
U(H_0)^{1/(2r)}e^{d/(2r)}
\sinh\!\frac{L_+}{2r}.
}
\tag{P.33}
\]
If a finite certificate instead supplies explicit \(0<\alpha\leq\beta\) with
\(\alpha H_0\preceq H_1\preceq\beta H_0\), then the same enclosures hold with the explicit larger number \(d=\log(\beta/\alpha)\). This follows from the optimal Rayleigh bounds, and provides the exact connection to rational positive-matrix certificates.

## 8. Boundary tests and the differentiability correction

### The smallest positive quotient degree and a square-root cusp

Take the auxiliary finite positive form in the original coefficient basis \(1,S,S^2\),
\[
H_2(t)=
\begin{pmatrix}1&0&t\\0&1&0\\t&0&1\end{pmatrix},
\qquad -1<t<1,
\quad \chi(S)=S,\quad q=1,\quad n=1,\quad r=1.
\tag{P.34}
\]
Its eigenvalues are \(1,1+t,1-t\), so it is strictly positive throughout the indicated interval. The quotient is evaluation at \(S=0\). The exact least lifts are
\[
R_0=R_1=1,\qquad R_2=1-tS^2.
\]
Indeed, \(R_2\) has remainder one, and its inner products with \(S,S^2\) are zero. Thus
\[
V_0=V_1=1,\qquad V_2=1-t^2,\qquad
L=-\log(1-t^2).
\tag{P.35}
\]
For \(t\ne0\),
\[
\frac{\sqrt{-\log(1-t^2)}}{|t|}
=\sqrt{\frac{-\log(1-t^2)}{t^2}}\longrightarrow1,
\]
because \(-\log(1-y)/y=\int_0^1(1-sy)^{-1}ds\to1\) as \(y\to0\). The right derivative of \(\sqrt L\) at zero is one and the left derivative is minus one. Ordinary differentiability at that zero is false. The Lipschitz conclusion (P.28) remains valid.

This example belongs to the finite positive-form class covered by the proof. It is not presented as the moment matrix of the zeta source. Its role is to show why the general theorem must state the zero case using the integrated or almost-everywhere formulation. It uses the same coefficient, quotient, and least-lift maps as the theorem.

### A finite positive measure in the original vertical coordinate

One can also test the boundary \(q=n=r=1\) directly with a positive source measure on the original line \(S=c+iu\), where \(c=k/2\) is retained. Give \(u=-1,0,1\) masses \(1,1+t,1\), with \(t>-1\), and use \(\chi(S)=S-c\). The degree-two Gram form is positive definite: a polynomial of degree at most two that vanishes at all three distinct support points is zero, and every mass is positive. Direct evaluation gives
\[
R_0=R_1=1,\qquad
R_2=1+(S-c)^2,
\quad
V_0=V_1=t+3,\quad V_2=t+1.
\tag{P.36}
\]
The last least lift equals one at \(u=0\) and zero at \(u=\pm1\), so it is orthogonal to every multiple of \(\chi\). The original monic orthogonal polynomials and their norms are
\[
p_1=S-c,\quad\omega_1=2,\qquad
p_2=(S-c)^2+\frac2{t+3},\quad
\omega_2=\frac{2(t+1)}{t+3}.
\]
Consequently
\[
U=\frac{t+1}{t+3},\qquad
L=\log\frac{t+3}{t+1}.
\tag{P.37}
\]
The fixed evaluation map from \(\mathcal P_2\) to its three support values is invertible. It transports \(H_2(t)\) exactly to the diagonal mass matrix \(\operatorname{diag}(1,1+t,1)\). The generalized derivative eigenvalues are therefore \(0,1/(1+t),0\), and \(\omega=1/(1+t)\). Direct differentiation gives
\[
(\log U)'=\frac2{(t+1)(t+3)},\qquad
L'=-\frac2{(t+1)(t+3)}.
\]
Both satisfy (P.25) and (P.27), with the full source mass \(t+3\) still present in (P.36). This is an auxiliary finite measure, connected to the theorem by its explicitly stated evaluation map; it is not a numerical estimate for the arithmetic source.

### The zero quotient

For \(q=0\), set \(\chi=1\), \(\mathcal K_a=\mathcal P_a\), and \(\mathcal L_a=\{0\}\). The least-lift map has domain \(\mathbb C^0\); its Gram matrix is empty and its determinant is one. Thus every \(V_a=1\), \(L=0\), \(s=0\), and \(\mathcal E_{n,r}=0\). No inverse of an empty matrix or negative-index relation determinant is needed.

If the endpoint convention admits \(n=0\), define \(V_{-1}=1\) from \(\mathcal P_{-1}=\{0\}\). Then the same endpoint formula holds. If the source reserves endpoint windows for nonempty packets, the \(q=0\) statement is the exact zero-quotient extension, not an extra admitted packet. The monic source norms and \(U=\omega_{n+r}/\omega_n\) remain well defined for \(n\geq0\) independently of this zero quotient.

### Literal mass changes

For any positive scalar \(c\), replacing \(H_m\) by \(cH_m\) leaves \(R_a\) and the monic polynomial coefficients fixed, and sends
\[
G_a\longmapsto cG_a,\qquad
V_a\longmapsto c^qV_a,\qquad
\omega_j\longmapsto c\omega_j.
\tag{P.38}
\]
These equalities follow directly from (P.5) and the monic least-norm characterization. They imply exact cancellation in \(U\) and in the four-volume ratio \(\mathcal R\). They do not reset the source's mass. For a positive differentiable scalar \(c(t)\), the derivative matrix becomes
\[
\widetilde\Lambda=(c'/c)I+\Lambda,
\]
so its oscillation is unchanged. Both trace derivatives in (P.25) and (P.26) kill the added scalar term because their projection differences have trace zero. This is the exact morphism responsible for the projective invariance.

## 9. Review outcome and scope

The projection formula, rank bound, singular-value formula, principal-angle trace norm, determinant-loss comparison, log-norm-ratio derivative, both window-logarithm derivative bounds, exact linear-segment oscillation integral, and the projective Lipschitz bounds have complete proofs above. The indices \(n=q\), \(r=1\), \(a=q-1\), and the zero quotient are explicitly handled. Complex coefficient conjugations use the original \(x^*Hy\) orientation throughout.

The sole correction to the proposed wording is at zeros of \(L\): use (P.28), or the corresponding almost-everywhere derivative assertion, instead of asserting ordinary differentiability of \(\sqrt L\) at every point. The exact example (P.34)–(P.35) proves the need for that correction in the stated positive-form class.

The result provides finite-metric error control for the existing endpoint expression. It supplies no unstated upper estimate for its arithmetic growth as \(q,n,r,k\) vary.

## 10. Complete authored article review

The parent subsequently supplied the full article gamma_endpoint_window_bridge_20260913.tex, EW.1–51 with the additional EW.46a strictness proof. I read the entire article. The first full-file output truncated part of EW.28–35; separate bounded reads of that entire region repaired the omission. The source subsequently incorporated the three small corrections recorded below. A final byte pin remains pending the parent's additional coefficient-box calibration paragraph; the complete geometric proof and EW.1–48 have been reviewed.

### 10.1 The source, coefficients, and determinant prefixes

EW.1–4 retain \(w_h=|v_h|^2/(2\pi)\), \(\mu_h^k\), \(S=k/2+iu\), the complete local orders of the packet, and the monic relation. For the displayed injection, the exact role of complete local orders is that \(g/h\) has a nonzero constant term at each selected centre. The recursive inverse of its truncated local series and the Chinese remainder map make its tensor class a unit; consequently multiplying the sum class by that unit leaves the kernel equal to the original intersection ideal. The article uses this exact kernel to justify its injection. Its positivity statement follows from a positive almost-everywhere real-line density and the finite real zero set of a nonzero polynomial.

The analytic decay and theta construction in EW.1 are explicitly delegated to the accompanying complete GC proof, rather than claimed as new numerical verification in this article. This review checks their use in the finite maps: the required polynomial moments and the original nonzero positive source ensure that every finite integral, source Gram, and monic projection invoked below exists. This review has not replayed the analytic GC proof or its numerical certificates.

Differentiating EW.6 gives
\[
(1+z^2)\partial_z G=(t-\alpha z)G,
\]
and therefore \(b_{j+1}=tb_j-j(j+\alpha-1)b_{j-1}\). This checks the exact recurrence parameter and signs. The full reference mass in EW.5–7 is \(C_k=c_\lambda^k\), not \(c_{k\lambda}\). The equality
\[
r_\lambda^{*k}=(C_k/c_{k\lambda})r_{k\lambda}
\]
therefore gives the stated monic norms \(C_kj!(k\alpha)_j\). Every instance of the norm and endpoint ratio retains that mass.

The tensor coefficient computation EW.8–10 has its factorials in the correct positions. Namely the one-factor integral is \(c_\lambda j!(\alpha)_jc_{h,j}\), while the polynomial addition coefficient is \(l!/\prod j_i!\). Their product leaves exactly \(C_kl!\prod_i(\alpha)_{j_i}c_{h,j_i}\), as EW.9 states. A test polynomial of degree at most \(m\) and its conjugate have product degree at most \(2m\). Thus EW.10 really requires only \(c_{h,0},\ldots,c_{h,2m}\); it does not omit a derivative or higher-moment input in the zero-tilt endpoint problem. At the constant entry, the same formula gives \(C_kc_{h,0}^k=\mu_h^k\). Complex conjugation appears on the first polynomial factor, consistent with the article's \(x^*Hy\) convention.

For EW.11, direct multiplication gives
\[
J_NR_N=I,\qquad B_N^*H_NR_N=(J_NB_N)^*G_N=0,\qquad
R_N^*H_NR_N=G_NK_NG_N=G_N.
\]
The columns of \([E_N,B_N]\) have successive highest degrees and leading coefficients one, so its determinant is one in the original \(S\) basis. Replacing \(E_N\) by its least lifts subtracts combinations of the remaining columns. Its determinant stays one and its Gram becomes \(\operatorname{diag}(G_N,B_N^*H_NB_N)\). This proves EW.12 with the exact relation index and no extra determinant of a quotient-coordinate change.

The full Schur map in EW.14–16 has the correct orientation:
\[
\Psi^*H_m\Psi=\operatorname{diag}(H_{n-1},W),\qquad
J_m\Psi=[J_{n-1},F].
\]
The same identities restrict to every first \(j\) appended columns, since their top-right matrix is precisely the first \(j\) columns of \(C_D\). Thus
\[
K_{n+j-1}=K_{n-1}+F_jW_j^{-1}F_j^*
\]
and the determinant lemma gives EW.17 with \(Z_j=F_j^*G_{n-1}F_j\). All prefix sizes are \(j\), the old source has dimension \(n\), the final block has dimension \(r+1\), and the quotient dimension remains \(q\).

The first residual is the original monic orthogonal polynomial of degree \(n\), so \(w=\omega_n\). Orthogonally removing the first \(r\) residuals from the last one gives \(\omega_m=\det W_{r+1}/\det W_r\). The resulting \(U\) and the volume ratio in EW.18 use the correct indices. In particular
\[
\frac{\mathscr R_r\mathscr R_{r+1}}{\mathscr R_1}
=\frac{V_{n-1}V_n}{V_{m-1}V_m}.
\]
The local definitions inserted before EW.19 now state
\(\mathfrak D_j=\det H_{j-1}\), \(\mathfrak D_0=1\), and
\[
\mathfrak B_j=\det(B_{q+j-1}^*H_{q+j-1}B_{q+j-1}),\qquad
\mathfrak B_0=1.
\]
They also define \(Y_j=\mathfrak B_j/\mathfrak B_j^\Gamma\). Consequently \(T_N=V_N/V_N^\Gamma\) and the two exact correction formulas in EW.19 follow. The reference norm ratio is \((n+1)_r(n+\beta)_r\); both rising factorial starting points were checked.

### 10.2 Paired root arguments and the finite criterion

Substitution of the four prefix determinants from EW.17 into EW.18 gives, with the article's symbols,
\[
U=\frac{s}{pw},\quad
\mathscr R=\frac{Dw}{pse},\quad
U\mathscr R=\frac{D}{p^2e},\quad
U/\mathscr R=\frac{s^2e}{w^2D}.
\]
Thus both cancellations in EW.21 are exact. The repeated determinant symbols refer to the same matrices, which is necessary for these cancellations. The positive-root factorization in EW.22 follows from the integer identity \(P^{2r}-Q^{2r}=(P-Q)\sum P^{2r-1-j}Q^j\); its denominator stays strictly positive when \(\mathscr R=1\). EW.20 and EW.22 therefore agree at that boundary as well as at positive loss.

The coefficient cutoff in EW.23 is \(2(n+r)\), with all relation columns obtained from the same fixed monic division. The local-to-window argument in EW.24 correctly treats a zero local logarithm first. In the positive case the concavity of \(\log\sinh x\) and the two stated telescopes give exactly the \(r\)-th-root bound. The article explicitly locates the existing local arithmetic inequality and retained losses in the complete TVB source; it does not replace that earlier inequality by a new arbitrary allowance assumption.

### 10.3 Geometry and finite metric variation

EW.25–28 agree with the full independent proof in Sections 1–3 of this review, including the quotient identity map, the relative positive matrix \(G_a^{-1/2}G_bG_a^{-1/2}\), the maximum \(\min(q,b-a)\) moving directions, and the entire two-dimensional projection blocks. The ambient norm and original quotient norm are connected by the displayed isometries.

EW.30 correctly distinguishes the contravariant coefficient matrices from the ambient projections: the projection matrices are \(P_jH_m\) and \(Q_jH_m\). Their Euclidean isometric conjugates are \(H_m^{1/2}P_jH_m^{1/2}\) and \(H_m^{1/2}Q_jH_m^{1/2}\). Cyclic trace therefore takes EW.31–32 exactly to the centred trace expressions used in the proof of EW.33. No Hermitian adjoint is replaced by a transpose, and no derivative of a moving least lift survives its proved boundary orthogonality.

The article's EW.33–36 constants match (P.27)–(P.33) above. Its generalized-eigenvalue calculation on the linear positive segment is valid: the equation \(Ex=\lambda H(t)x\) transforms into the commuting matrices \(M-I\) and \(I+t(M-I)\), producing the eigenvalues \((\ell_i-1)/(1+t(\ell_i-1))\). Their spread integrates to \(\log\kappa\). Equation (P.29)–(P.30) in this review supplies an additional explicit unitary for that same identification.

The integration hypothesis has been corrected to continuously differentiable paths. The zero-loss example and the article's Lipschitz wording now agree: no ordinary derivative of \(\sqrt{\mathscr L}\) is claimed at the cusp. Scalar source changes retain the original source mass and cancel exactly from the two window quantities.

### 10.4 Interval maps with the actual relation

The coefficient error polynomial in EW.37 is correct: expand each \(k\)-fold product by the subset of factors that carry coefficient errors, exclude the empty subset, and bound each remaining central factor by its absolute value. Summing gives the coefficient of \((A_++E_+)^k-A_+^k\). EW.38 is then an entrywise bound for the exact same finite map EW.10.

The quotient-first congruence EW.39 resolves the nonrational relation issue exactly. For the actual matrix \(A_N=[E_N,B_N]\), the first component of \(A_N^{-1}\) is the actual remainder \(J_N\). Thus an enclosure of \(A_N^*H_NA_N\), computed using intervals for the actual relation coefficients, can be minimized over fibres with a fixed first-coordinate projection. It does not substitute the remainder map of a nearby rounded polynomial. This fixed affine fibre is the key reason the quotient Loewner bounds in EW.43 hold.

The symmetric entry radii in EW.40 imply the claimed Loewner enclosure: sum
\[
\varepsilon_{ab}|x_a||x_b|
\leq \tfrac12\varepsilon_{ab}
\left(\frac{v_b}{v_a}|x_a|^2+\frac{v_a}{v_b}|x_b|^2\right)
\]
over ordered pairs and use \(\varepsilon_{ab}=\varepsilon_{ba}\). Its right side is \(x^*\Delta x\), including diagonal terms with their original coefficient. The congruence EW.41 has its negative sign and \(bb^*/a\) orientation correct. Strictly positive rational pivots prove the positive lower matrix and hence the positive upper matrix. The convergence assertion is only at fixed degree with convergent valid input intervals; it follows from the actual matrix's strictly positive least eigenvalue and finite entrywise error. It introduces no growing-degree conditioning assertion.

Monic minimization over identical original affine fibres proves EW.42. Quotient minimization over identical first-coordinate fibres proves EW.43, including the empty boundary at \(N=q-1\). For positive forms \(G^-\preceq G\preceq G^+\), multiplication of the eigenvalues after congruence by the smaller form gives the determinant inequalities with the displayed orientation.

The lower and upper ratios EW.44 put each numerator and denominator enclosure on the correct side. The lower clamp at one is warranted by already-proved nested minimization, and the upper ratio is necessarily at least the actual ratio. All four positive-root arguments use the correct monotonic corners \((U_-,\mathscr R_-)\) and \((U_+,\mathscr R_+)\). The upper root endpoint minus the lower root endpoint, and the opposite subtraction for the lower bound, have the correct orientations in EW.45. In particular its upper bound cannot be negative: \(u_3\geq(U_+\mathscr R_+)^{1/(2r)}\geq(U_+/\mathscr R_+)^{1/(2r)}\geq l_4\). Every comparison can be certified by integer power inequalities as the article states.

### 10.5 Strictness, boundaries, and theta primitives

At \(r=1\), \(d=2\) and \(\mathscr R=\mathscr R_2\); the article's reduction to the two-column result is exact. At \(n=q\), the base degree is \(q-1\), its boundary has zero columns, and its quotient is its entire source space. The formula never requires a full \(q\)-dimensional quotient at degree \(q-2\).

The additional EW.46a strictness proof is valid for the actual positive polynomial measure. Multiplication by real \(u\) is self-adjoint and the degree calculation gives the original monic recurrence with \(a_j=\omega_j/\omega_{j-1}>0\). The explicit phase map
\[
p_j(S)=i^j\pi_j((S-c)/i)
\]
is monic in the original \(S\), is orthogonal to lower original powers, and retains its norm because \(|i^j|=1\). It gives
\[
Sp_j=p_{j+1}+(c+ib_j)p_j-a_jp_{j-1}.
\]
In particular the sign of the last term is negative. If \(\chi\) divided consecutive \(p_j,p_{j+1}\), the nonzero scalar \(a_j\) would force divisibility of \(p_{j-1}\), continuing to \(p_0=1\). This contradicts \(q\geq1\).

The two residuals over \(\mathcal P_{N-1}\) are \(p_N\) and \(p_{N+1}+zp_N\), with the now-displayed exact coefficient
\[
z=\langle p_N,S^{N+1}\rangle_H/\omega_N.
\]
If both residual quotient columns vanished, both consecutive monic polynomials would be divisible by \(\chi\), which the previous argument excludes. Hence \(F_2\ne0\), \(F_2^*G_{N-1}F_2\) is nonzero positive semidefinite, and its determinant increment is strictly greater than one. Multiplication over the overlapping window proves EW.46a and strict positivity of the actual endpoint expression. The article correctly keeps this actual-measure assertion separate from its general positive-form path theorem while giving the exact phase and quotient maps between the presentations.

For \(q=0\), the declared empty matrices, \(V_N=1\), and \(H_{-1}\) convention yield the zero quotient and zero endpoint expression; the original analytic source mass still exists. The \(n=0\) window takes \(W=H_r\), with its first entry equal to the original mass, and uses no inverse of a negative-degree matrix.

EW.46–48 prove an explicit representative difference rather than merely declaring the representatives inequivalent. The same original remainder makes the difference a unique multiple \(\chi\kappa_x\). Ordered monic division in the tensor variables supplies the \(Q_i\) identity. In the \((k-1)\)-cochain, each preceding \(F_h\) has degree one, giving the differential sign \((-1)^{i-1}\); it cancels the written sign. The equality \(h(D_i)F_h=\Theta\phi_0\) then gives the displayed boundary term by term. Its tensor arithmetic jet vanishes because \(\chi\) annihilates the sum, while both representatives retain the common original jet \(\eta x\). The support carrier sends this boundary to the fibre zero rather than to the external absence point.

### 10.6 Independent calibration of the three displayed windows

The fixture EW.49–50 retains \(B(t)=1+t^2/4\), \(c_1=1/2\), \(C_2=1/4\), and \(\chi(S)=S^2-2S-1\). The Gamma functional equation gives \(Br_1=r_2\) exactly. Its literal convolution is
\[
r_2*r_2=\frac{(3/4)^2}{315/8}r_4=\frac1{70}r_4,
\]
with source mass \(9/16\). This proves the all-degree monic norms \((9/16)j!(8)_j\) used in the independent check.

The new companion calibration script uses a different exact route from the parent's Schur checker. Put \(x=S-1\), so the original relation becomes \(x^2=2\). The quotient-coordinate map
\[
(a,b)_{\{1,x\}}\longmapsto(a-b,b)_{\{1,S\}}
\]
has determinant one, so it preserves the quotient determinant exactly. The original monic recurrence yields
\[
[p_{j+1}]_\chi=x[p_j]_\chi+j(j+7)[p_{j-1}]_\chi .
\]
For \(j=0,\ldots,5\), the remainder vectors in \((1,x)\) are
\[
(1,0),\ (0,1),\ (10,0),\ (0,28),\ (356,0),\ (0,1588).
\]
Since the original orthogonal polynomial coefficient matrix is monic triangular, diagonalizing its Gram gives the exact quotient kernel
\[
K_N=\sum_{j=0}^N
\frac{[p_j]_\chi[p_j]_\chi^*}{(9/16)j!(8)_j},
\qquad V_N=(\det K_N)^{-1}.
\]
This calculation makes no Schur block. It gives
\[
\begin{array}{c|c}
N&V_N\\\hline
1&81/32\\
2&729/488\\
3&98415/161528\\
4&16238475/37139524\\
5&2679348375/10549111519 .
\end{array}
\]
Taking the source norm ratios and the four corresponding volume ratios reproduces exactly all six displayed scalar values of EW.51:
\[
\begin{array}{c|c|c}
(n,r)&U&\mathscr R\\\hline
(2,1)&30&20191/4860\\
(2,2)&1320&3073295611/216513000\\
(3,2)&2640&295913127219469/36104825790000 .
\end{array}
\]
The script gamma_endpoint_window_bridge_projection_review_calibration_20260913.py completed with exit code zero and six exact Fraction comparisons passing. Its JSON records the full remainders, kernel matrices, volumes, coordinate map, literal masses, and its own script hash. This is one ordinary Python execution of six scalar checks. It is not a mutation-sensitivity test and is not counted as a second set of arithmetic input intervals.

### 10.7 Corrections resolved before the final pin

Three additional article-level findings were sent to the parent and verified after their corrections:

1. The source determinants \(\mathfrak D_j\), relation determinants \(\mathfrak B_j\), empty determinant conventions, and \(Y_j\) are now explicitly defined before EW.19.
2. The integrated sensitivity argument now uses continuously differentiable positive paths.
3. The original projection coefficient \(z\) in the strictness argument is explicitly displayed as \(\langle p_N,S^{N+1}\rangle_H/\omega_N\).

The cusp correction from the initial independent proof is also fully incorporated. No other mathematical error was found in the complete EW.1–51 and EW.46a article at this review stage. The parent's forthcoming explicit coefficient-box calibration and the final source hash remain to be read and recorded.

## 11. New exact strengthening from concavity of the angle loss

This continuation was derived in the independent projection-review lane after the complete EW.1–51 review. It uses the same original source spaces, quotient relation, and two lists of principal angles proved above. It introduces no additional arithmetic coefficient, measure hypothesis, or asymptotic estimate. The parent has accepted it for inclusion in the endpoint article as EW.35a–b.

Retain \(s=\min(q,r)\geq1\), \(L=\delta_1+\delta_2\), and \(\omega=\lambda_{\max}(\Lambda)-\lambda_{\min}(\Lambda)\). For each of the two projection pairs, put \(x_i=-\log\sigma_i^2\) for its moving singular directions. Every \(x_i\) is a positive finite real number. There are at most \(s\) such directions in each pair. Pad the combined two lists with zeros to exactly \(2s\) entries. Their sum is exactly \(L\), since all omitted singular values were one.

Define
\[
f:[0,\infty)\longrightarrow[0,1),\qquad
f(x)=\sqrt{1-e^{-x}}.
\]
It is continuous at zero and strictly increasing. For \(x>0\),
\[
f'(x)=\frac{e^{-x}}{2\sqrt{1-e^{-x}}},
\qquad
f''(x)=
-\frac{e^{-x}}{2\sqrt{1-e^{-x}}}
-\frac{e^{-2x}}{4(1-e^{-x})^{3/2}}<0 .
\tag{P.39}
\]
Thus \(f\) is concave on \((0,\infty)\). Its continuous extension is concave on \([0,\infty)\): apply the positive-domain concavity inequality with each argument increased by \(\varepsilon>0\), then let \(\varepsilon\) decrease to zero. Finite Jensen for the \(2s\) equally weighted entries gives
\[
\sum_{i=1}^{2s}f(x_i)
\leq2s\,f\!\left(\frac{L}{2s}\right).
\tag{P.40}
\]
The exact principal-angle trace norm and its triangle inequality, followed by the centred trace estimate (P.22), give
\[
\begin{aligned}
|L'|
&\leq\frac{\omega}{2}
\left(\|\widehat\Pi_{n-1}-\widehat\Pi_{m-1}\|_1+
\|\widehat\Pi_n-\widehat\Pi_m\|_1\right)\\
&=\omega\sum_{i=1}^{2s}f(x_i).
\end{aligned}
\]
Together with (P.40) this proves the strengthened pointwise estimate
\[
\boxed{|L'|\leq
2s\,\omega\sqrt{1-\exp(-L/(2s))}.}
\tag{P.41}
\]
It implies both earlier pointwise bounds: \(f(y)\leq1\), and
\[
1-e^{-y}=\int_0^y e^{-t}\,dt\leq y
\]
gives \(f(y)\leq\sqrt y\). Hence the right side of (P.41) is at most both \(2s\omega\) and \(\omega\sqrt{2sL}\), with no change to their constants.

The exact increasing coordinate map for this stronger differential bound is
\[
\Phi_s:[0,\infty)\longrightarrow[0,\infty),\qquad
\Phi_s(L)=2\operatorname{arcosh}\!\left(e^{L/(4s)}\right).
\tag{P.42}
\]
Here \(\operatorname{arcosh}\) is the nonnegative inverse of the strictly increasing restriction of \(\cosh\) to \([0,\infty)\). For \(L>0\), differentiating that inverse gives
\[
\Phi_s'(L)
=\frac{1}{2s\sqrt{1-\exp(-L/(2s))}}.
\tag{P.43}
\]
Equations (P.41) and (P.43) therefore show
\[
|(\Phi_s(L(t)))'|\leq\omega(t)
\]
where \(L(t)>0\). This derivative statement alone does not dispose of zeros; the following regularization does.

For a continuously differentiable positive-form path and \(\varepsilon>0\), the function \(t\mapsto\Phi_s(L(t)+\varepsilon)\) is continuously differentiable. Since \(f\) is increasing, (P.41) implies
\[
\left|\frac{d}{dt}\Phi_s(L+\varepsilon)\right|
\leq
\omega\,
\frac{f(L/(2s))}{f((L+\varepsilon)/(2s))}
\leq\omega .
\tag{P.44}
\]
This includes \(L=0\), where the numerator is zero and the denominator is positive. Integrating and taking the limit \(\varepsilon\downarrow0\) gives the exact path estimate
\[
|\Phi_s(L(t_1))-\Phi_s(L(t_0))|
\leq\int_{t_0}^{t_1}\omega(t)\,dt.
\]
For the actual linear segment joining two positive source forms, (P.31) makes its right side exactly their finite projective distance. Thus
\[
\boxed{
|\Phi_s(L(H_1))-\Phi_s(L(H_0))|
\leq d_{\mathrm{proj}}(H_0,H_1).
}
\tag{P.45}
\]
The same compact-interval argument proves Lipschitz continuity of the transformed quantity along the path; no ordinary derivative at a zero is asserted.

The map (P.42) is a bijection with the explicitly proved inverse
\[
\boxed{\Phi_s^{-1}(y)=4s\log\cosh(y/2),\qquad y\geq0.}
\tag{P.46}
\]
Indeed \(\cosh(\Phi_s(L)/2)=e^{L/(4s)}\) proves one composition, and the nonnegative inverse definition of \(\operatorname{arcosh}\) proves the other. This is an exact change of the recorded loss coordinate, not a change of the original volume or source mass.

Writing \(d=d_{\mathrm{proj}}(H_0,H_1)\), \(y_0=\Phi_s(L(H_0))\), set
\[
y_-=\max(0,y_0-d),\quad y_+=y_0+d,\qquad
\widetilde L_\pm=4s\log\cosh(y_\pm/2).
\]
Equations (P.45) and (P.46) give
\[
\widetilde L_-\leq L(H_1)\leq\widetilde L_+.
\tag{P.47}
\]
Equivalently the unchanged four-volume ratio satisfies
\[
\cosh(y_-/2)^{4s}
\leq\mathcal R(H_1)
\leq\cosh(y_+/2)^{4s}.
\]
Combining (P.47) with the already-proved norm-ratio bounds gives the explicit endpoint enclosure
\[
\boxed{
U(H_0)^{1/(2r)}e^{-d/(2r)}
\sinh\!\frac{\widetilde L_-}{2r}
\leq\mathcal E_{n,r}(H_1)
\leq
U(H_0)^{1/(2r)}e^{d/(2r)}
\sinh\!\frac{\widetilde L_+}{2r}.
}
\tag{P.48}
\]
All quantities use the same fixed \(n,r,q,\chi\) and original source coordinates. If \(\alpha H_0\preceq H_1\preceq\beta H_0\) with explicit positive scalars, then \(d=\log(\beta/\alpha)\) can again be used in these enclosing intervals by the optimal Rayleigh bounds.

For \(s=0\), the present endpoint domain has \(q=0\) because \(r\geq1\). Its quotient loss is exactly \(L=0\) for every source. Define \(\Phi_0(0)=0\) only on this one-point loss domain. The transformed loss and endpoint expression are then zero, and (P.45) has left side zero. No expression with \(1/s\) is used in that case.

## 12. Final source-bound review and completed numeric audit

The final complete reviewed TeX is gamma_endpoint_window_bridge_20260913.tex, SHA-256

e8d6152532c98532a062b5840834d934b28f29490ec926f47c2bce1af3493854.

This pin includes EW.1–59, EW.35a–c, and EW.46a. I read the complete earlier article, all final mathematical additions, and the final small changes to the injection domain, compact-real-part wording, ambient projection type, and coefficient-box realization statement. I separately read the entire supplementary written calculation gamma_endpoint_window_bridge_supplement_20260913.md. The normal unchanged supplementary receipt supplied the exact rational objects inspected below. No parent executable was imported, edited, or replayed by this final review.

### 12.1 Final strengthened certificate

EW.35a–b incorporate exactly the complete derivation in Section 11 above, with its attribution to this independent review. The singular-loss list has \(2s\) entries after zero padding, its sum is the actual \(L\), both terms of \(f''\) are negative, the derivative denominator of \(\Phi_s\) is \(2s\sqrt{1-e^{-L/(2s)}}\), and the regularized ratio is at most one. The one-point \(s=0\) convention avoids division by \(s\).

For the additional algebraic certificate EW.35c, the exact identity is
\[
z_0=
(\mathscr R^{(0)})^{1/(4s)}
+\sqrt{(\mathscr R^{(0)})^{1/(2s)}-1}
=\exp\!\left(\frac{\Phi_s(\log\mathscr R^{(0)})}{2}\right).
\]
The first equality with the exponential follows from the specified nonnegative branch of \(\operatorname{arcosh}\). If \(\rho\geq\kappa\), the proved difference of the two \(\Phi_s\) values is at most \(\log\rho\), so their exponentials divided by two differ by multiplicative factors at most \(\sqrt\rho\). Each exponential is at least one. Therefore
\[
\max(1,z_0/\sqrt\rho)\leq
\exp(\Phi_s(\log\mathscr R^{(1)})/2)\leq \sqrt\rho\,z_0.
\]
For \(z\geq1\), \((z+z^{-1})/2\) has derivative \((1-z^{-2})/2\geq0\). Raising it to the positive integer power \(4s\) and using the explicit inverse of \(\Phi_s\) proves the displayed volume enclosure. The concurrent norm-ratio enclosure follows from \(|\log(U^{(1)}/U^{(0)})|\leq\log\rho\). Thus the final algebraic certificate has the correct square-root factor \(\sqrt\rho\), both clamping and inverse powers, and the exact original exponent \(4s\).

Two final domain wording details were corrected and verified before this pin: EW.35c explicitly begins with \(s\geq1\), and its computational description permits nonnegative real roots. This includes the zero radical when \(\mathscr R^{(0)}=1\). Every denominator \(z_-\), \(z_+\) remains at least one.

The article's exact matrix-certificate connection is also valid. If \(aH^{(0)}\preceq H^{(1)}\preceq bH^{(0)}\), then every generalized Rayleigh quotient lies in \([a,b]\); hence \(\kappa\leq b/a\). Taking \(\rho=b/a\) in the algebraic formula closes the stated map from a rational matrix comparison to the original endpoint quantity. The source mass and the fixed relation remain unchanged throughout that map.

### 12.2 Final source and coordinate clarifications

The final EW.3 now gives the two kernels with their exact different domains. The unfactored map from \(\mathbb C[S]\) has kernel \((\chi)\); the induced map \(\eta\) from \(\mathbb C[S]/(\chi)\) has kernel zero. The complete local-unit proof applies to the unfactored map and then descends by that ideal. The final statement therefore proves the claimed injection with its literal domain.

The vertical decay is stated uniformly in each fixed compact interval of real parts. The projection \(\Pi_b\) is now explicitly an endomorphism of the common ambient polynomial Hilbert space, with range \(L_b\) included by its fixed polynomial inclusion. Thus projection differences and their trace norms are typed in the same space.

EW.55 says that every finite input vector in the indicated box is realized by the specified positive quadratic multiplier, rather than asserting that finitely many coefficients determine a unique multiplier as a function. This statement is proved by the exact map \(a=c_{B,0}-2c_{B,2}\), \(b=c_{B,2}\). Both are positive in the complete box. The finite endpoint depends only on the recorded coefficients through degree six, as the earlier map proves.

### 12.3 Independent kernel table and exact central inverse

EW.52–54 contain the complete recurrence-kernel computation from Section 10.6. The quotient change is \(A:(1,x)\to(1,S)\) with determinant one. In matrix terms,
\[
G_N^x=A^*G_N^SA,\qquad
(G_N^x)^{-1}=A^{-1}(G_N^S)^{-1}A^{-*}.
\]
Applying that inverse congruence to the orthogonal-polynomial expansion of \(J_NH_N^{-1}J_N^*\) gives precisely the displayed remainder vectors in the \((1,x)\) basis. The table retains all source norms \(9/16,9/2,81,2430,106920,6415200\). Its entries and the three selected windows have passed the six independent exact comparisons already recorded above.

The final numeric-audit script additionally multiplied the explicit EW.57 central matrix by the displayed EW.58 inverse and checked all sixteen entries against the identity matrix. Their product is exactly \(I_4\), and the inverse trace is exactly \(956/243<4\). The original centre is positive by its Gamma measure, so its inverse is positive. Its largest eigenvalue is bounded by its trace, proving \(\widehat H_3\succ I_4/4\) as stated.

The same audit recomputed all four \(\Delta_{jj}\) as exact Fractions at \(\varepsilon=10^{-12}\). Each equals the saved full row-sum polynomial, and each satisfies \(0<\Delta_{jj}<10^{-6}\). Therefore
\[
\widehat H_3-\Delta\succ(1/4-10^{-6})I_4\succ0.
\]
This verifies the article's short positive-matrix certificate before any perturbed inverse is used. The quadratic error terms are retained in every diagonal polynomial.

### 12.4 Independent final endpoint numbers

The final audit built the exact matrices \(\widehat H_3\pm\Delta\) directly from the article's integer matrix and its four diagonal polynomials, then compared them to the saved receipt. It used its own permutation determinant and Gauss–Jordan inverse implementations, without importing the parent checker, to recompute the two monic norms and all quotient volumes at degrees \(1,2,3\), using the unchanged original remainder matrices. It then recomputed the lower and upper \(U,\mathscr R\) corner values and verified exact equality with all four saved rational values. Their domain satisfies \(0<U_-\leq U_+\) and \(1<\mathscr R_-\leq\mathscr R_+\).

For the lower corner, the specified interior input, and the upper corner, the audit checked both positive square-root brackets by squaring their exact rational endpoints. It then reconstructed each endpoint interval by the required lower-first minus upper-second subtraction, and the reverse subtraction for the upper bound, including the factor one half. The final written dyadics in EW.59 agree exactly with those corner intervals:
\[
\frac{10247872526420120792621067}{2^{81}}
\leq\mathcal E_{2,1}\leq
\frac{10247872551311149445602506}{2^{81}}.
\]
The independently recorded narrow interior interval is strictly inside these endpoints. The upper numerator here is twice the numerator \(5123936275655574722801253\) in the supplement's denominator-\(2^{80}\) presentation, so the two forms agree by exact integer multiplication.

The final script ran once under ordinary Python and completed with exit code zero. It passed 67 explicitly labelled predicates: 63 mathematical checks plus four provenance and normal-job-selection checks. This count describes only the final displayed inverse, diagonal bounds, matrix corners, and root endpoints. It is separate from the parent's 329 mathematical supplement checks, the parent's base fixture, the earlier six-window-scalar review checks, and any changed-formula runs. No mutation-sensitivity claim is made for this read-only final numeric audit.

The final independent companions are:

- gamma_endpoint_window_bridge_projection_review_calibration_20260913.py — SHA-256 d2540cfc1ffb2eda9eb18966a8478090da5c564b0b7d78a11a0de130a0cce435.
- gamma_endpoint_window_bridge_projection_review_calibration_20260913.json — SHA-256 13a2ba51eefdde82c599a94ae2b98160b4d529d5cae1e8757ec89601017b94c6.
- gamma_endpoint_window_bridge_projection_review_final_numeric_20260913.py — SHA-256 b26951e4278552820a6bf7e5fb85c275540632d03fe2ccfc25c32702ce13e5b7.
- gamma_endpoint_window_bridge_projection_review_final_numeric_20260913.json — SHA-256 cf651a0f2e11203fa93eaec36fc7cdc76e1c84e962144dbfa60eeea15e532306.

The supplementary receipt inspected by the final audit has SHA-256 59b0c682b860e024070a1ac307f600a0bd55566aeba83808a9dee73a42250c6a. Its complete written report records the separate full coefficient-box propagation and the independent reviewers' larger saved-data checks. Those results are attributed to that report and are not described as additional executions by this review lane.

### 12.5 Final outcome

All requested sections and final additions have now been read and checked against the pinned TeX source. The corrected zero-loss wording, determinant definitions, differentiability hypothesis, original residual coefficient, injection domain, common projection codomain, and algebraic root domains are incorporated. The stronger angle-loss theorem is proved in full and integrated with the exact algebraic endpoint map. No unresolved mathematical error was found in the final article. This review does not certify PDF layout, unprovided arithmetic growing-degree input, or the separate Lean declarations.
