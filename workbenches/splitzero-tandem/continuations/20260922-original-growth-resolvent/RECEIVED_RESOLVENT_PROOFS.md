# The original primary-word measured resolvent

## Complete additive proofs and original-source extraction

21 September 2026. Equations PR1–PR44, including lettered extensions.

The finite identities below are new derivations on the specified maps. Arithmetic asymptotics consume the two retained uploads and the pinned DCR source with their stated domains and analytic-input status. All roots, source masses, the original observation, full minima, and zero directions remain. The original kernel coefficient is not assigned. See `README.md`, `state/READING_LEDGER.json`, and `state/VERIFICATION.json`.

# PR1–PR16. The full measured primary-word resolvent

21 September 2026. New finite derivation. These identities use the specified
positive metric, linear word, and onto observation. They do not use a monic-profile
asymptotic. Their arithmetic specialization uses the two retained input files.
Adjoints are metric adjoints; ordinary stars are conjugate transposes in the
coefficient frames that are explicitly displayed.

## PR1. Original maps and unchanged values

Let E have dimension q and positive metric G. Retain the actual onto observation
Lambda:E->B, of rank n, its kernel K of dimension m=q-n, and the fixed kernel frame
I_K. Define

\[
Q_B=(\Lambda G^{-1}\Lambda^*)^{-1},\quad
L=G^{-1}\Lambda^*Q_B,\quad
H_K=I_K^*GI_K.
\tag{PR1}
\]

Then Lambda L=I, L*GL=Q_B, and L Lambda is the G-orthogonal projection onto K^perp.
The isometries from Euclidean coefficient spaces are

\[
J_B=LQ_B^{-1/2},\qquad J_K=I_KH_K^{-1/2}.
\]

For the retained linear word T, put H=T^dagger T, V=ker T, d=dim V, delta=q-d.
The observed endomorphism to be calculated is

\[
\mathscr Y(z)=\Lambda z(zI+H)^{-1}L,\qquad z>0.
\tag{PR2}
\]

It is positive and at most I in Q_B. Its Euclidean representation is
Q_B^(1/2) mathscrY Q_B^(-1/2)=J_B^dagger z(zI+H)^(-1)J_B.
The determinant is unchanged by that similarity. Moreover

\[
\mathscr Y(z)=\int_0^\infty z e^{-z\tau}
\Lambda e^{-\tau H}L\,d\tau.
\tag{PR3}
\]

The integral is the scalar identity on the complete positive spectral resolution
of H, including its d zero eigenvalues. No projection is moved through H.

## PR2. The exact overlap and all zero factors

Choose any isometry J_Vperp onto V^perp, and define

\[
B_+=J_{V^\perp}^\dagger HJ_{V^\perp}>0,\quad
C=J_K^\dagger J_{V^\perp},\quad
A_K=J_K^\dagger HJ_K=CB_+C^*,\quad \Gamma=CC^*.
\tag{PR4}
\]

Write R=J_B^dagger J_Vperp. Because J_BJ_B^dagger+J_KJ_K^dagger=I,
R*R=I-C*C. Direct substitution in PR2 gives the complete original observed matrix

\[
\widehat{\mathscr Y}(z)
=I-RB_+(zI+B_+)^{-1}R^*.
\tag{PR5}
\]

The factors C and B_+ need not commute. Sylvester's determinant identity, proved
by the determinant of the block matrix [[I,U],[-V,I]], gives

\[
\boxed{
\det_B\mathscr Y(z)
=z^{\delta-m}\frac{\det(zI_m+A_K)}{\det(zI_\delta+B_+)}.
}
\tag{PR6}
\]

Indeed its delta-dimensional numerator is
zI+B_+^(1/2)C*C B_+^(1/2), whose nonzero Gram spectrum equals that of CB_+C*.
In the original fixed coefficient frame the identical formula is

\[
\boxed{
\det_B\mathscr Y(z)
=z^{q-m}\frac{\det(zH_K+I_K^*T^*GTI_K)}
{\det H_K\,\det(zI_q+G^{-1}T^*GT)}.
}
\tag{PR7}
\]

PR7 uses only matrices invertible for z>0 and has no positive-range convention.

Let h=dim(K intersect V), p=m-h. Then rank A_K=p, and PR6 is equivalently

\[
\det_B\mathscr Y(z)
=z^{\delta-p}
\frac{\prod_{j=1}^{p}(z+\alpha_j)}
{\prod_{j=1}^{\delta}(z+\lambda_j)},
\tag{PR8}
\]

where alpha_j are all positive eigenvalues of A_K and lambda_j all positive
eigenvalues of H. The forced power is delta-m+h, not delta-m with h dropped.
Rank(T|K)=m-h<=delta proves that this exponent is nonnegative.

When parameters change rank, PR7 remains the single exact formula. A newly zero
numerator eigenvalue contributes a factor z; a newly zero denominator eigenvalue
also contributes its own z. No disappearing direction is assigned value one.

### Exact complementary factor at zero regularizer

On the original transverse domain h=0 let U=C*Gamma^(-1/2); it is an isometry
onto ran(C*). Choose an isometry Z onto ker C, of dimension rho=delta-m. Full
block inversion in [U,Z] gives

\[
\boxed{
\frac{\det A_K}{\det B_+}
=\det\Gamma\,\det\Xi,\qquad
\Xi=Z^*B_+^{-1}Z.
}
\tag{PR8a}
\]

In fact det A_K=det Gamma det(U*B_+U), and the lower inverse block is the inverse
of the COMPLETE Schur complement of U*B_+U. This proves the ratio without
replacing the off-diagonal blocks by zero. For an arbitrary full frame Z0 of
ker C, the identical last determinant is det(Z0*B_+^-1 Z0)/det(Z0*Z0).
Every inverse and every Gram in this comparison is specified.

## PR3. Positive spectral shift and every regularizer derivative

Because ||C||<=1, singular-value min–max gives alpha_j<=lambda_j when both
positive lists are decreasing and j<=p. Thus

\[
\xi(s)=\#\{j:\lambda_j>s\}-\#\{j:\alpha_j>s\}
\]

satisfies 0<=xi(s)<=delta. Scalar integration in PR8 yields

\[
\boxed{
-\log\det_B\mathscr Y(z)
=\int_0^\infty\frac{\xi(s)}{z+s}\,ds.
}
\tag{PR9}
\]

This identity has every original eigenvalue, including multiplicity. It proves,
for every integer j>=1,

\[
0\le(-1)^j\frac{d^j}{dz^j}[-\log\det\mathscr Y(z)]
\le\frac{\delta(j-1)!}{z^j}.
\tag{PR10}
\]

In particular 0<=z(d/dz)logdet mathscrY<=delta. These are uniform in the positive
metric and in the nonzero spectral gaps. With a=min lambda_j and b=max lambda_j,
xi(s)>=delta-p on 0<s<a, so

\[
-\delta\log(1+b/z)\le\log\det\mathscr Y(z)
\le-(\delta-p)\log(1+a/z).
\tag{PR11}
\]

The exact large-z expansion retains the differences of full moments:

\[
-\log\det\mathscr Y(z)
=\sum_{j=1}^{N}\frac{(-1)^{j+1}}{jz^j}
[\operatorname{Tr}B_+^j-\operatorname{Tr}A_K^j]+\mathcal E_N(z).
\]

The remainder has the sign (-1)^N and obeys

\[
|\mathcal E_N(z)|\le
\frac{\operatorname{Tr}B_+^{N+1}-\operatorname{Tr}A_K^{N+1}}
{(N+1)z^{N+1}}.
\tag{PR12}
\]

This follows by finite division of 1/(z+s), then integration against xi(s); it
is valid even when its numerical bound is large. In the first moment the exact
difference is Tr(P_B H). At higher powers Tr(A_K^j) is not replaced by Tr(P_K H^j).

### The matrix-valued regularizer derivatives retain every mixed block

Let P_lambda be the full positive spectral projections of H and put
B_lambda=J_B^dagger P_lambda J_B>=0. In the exact observed orthonormal frame,

\[
\widehat{\mathscr Y}(z)=Y_0+
\sum_{\lambda>0}\frac z{z+\lambda}B_\lambda,\qquad
\sum_{\lambda>0}B_\lambda=I-Y_0.
\tag{PR12a}
\]

The matrices B_lambda need not commute. All derivatives, with these matrices
unchanged, satisfy

\[
0\preceq z^j(-1)^{j-1}\widehat{\mathscr Y}^{(j)}(z)
\preceq j!\frac{j^j}{(j+1)^{j+1}}(I-Y_0),\quad j\ge1.
\tag{PR12b}
\]

This is the maximum of x/(1+x)^(j+1), at x=1/j. For Im z>0,

\[
\operatorname{Im}\widehat{\mathscr Y}(z)
=(\operatorname{Im}z)\sum_{\lambda>0}
\frac{\lambda}{|z+\lambda|^2}B_\lambda\succeq0.
\tag{PR12c}
\]

It is invertible there: a kernel vector would annihilate every B_lambda by the
imaginary quadratic form; then Y0 acts as the identity on it, a contradiction.
Thus this is a complete holomorphic matrix family, with the displayed mixed
coefficients, on the upper half-plane.

## PR4. Scalar spectral enclosure with the complete overlap retained

Retain any finite c and E>=0 for which

\[
e^{c-E}I\preceq B_+\preceq e^{c+E}I.
\]

This is a concrete finite input in the original application. Let
Y0=J_B^dagger P_V J_B. Then

\[
Y_0+\frac z{z+e^{c+E}}(I-Y_0)
\preceq\widehat{\mathscr Y}(z)
\preceq
Y_0+\frac z{z+e^{c-E}}(I-Y_0).
\tag{PR13}
\]

The central model is barY=Y0+z/(z+exp(c))(I-Y0). PR13 also yields the relative
form comparison exp(-E)barY<=widehat(mathscrY)<=exp(E)barY. Every fixed restriction
and every full attained quotient of these two positive forms inherits that same
comparison by minimizing on the identical affine fibres. Its rank-p determinant
error is at most pE. No new quotient minimum is assigned a diagonal metric.

The common unit subspace ker(I-Y0) is fixed pointwise by all three operators.
Its complementary dimension is at most delta. For 0<=mu<=1,

f_a(mu)=(z+a mu)/(z+a)

has |d log f_a/d log a|<=1. Therefore the logarithm of each nonunit eigenvalue
of mathscrY differs by at most E from the same ordered eigenvalue of
Y0+z/(z+exp(c))(I-Y0). The determinant error is at most delta E, not qE.

Let gamma_1,...,gamma_p be all positive eigenvalues of Gamma. Its h zero
eigenvalues stay separate. The exact flat-spectrum determinant is

\[
\det[Y_0+\eta(I-Y_0)]
=\eta^{\delta-p}\prod_{j=1}^{p}[\eta+(1-\eta)\gamma_j],
\quad 0<\eta\le1.
\tag{PR14}
\]

It follows directly from PR5 with the scalar B_+=aI. It remains valid when
some gamma_j equal one, or when d<m. No negative unit multiplicity need be used.

Fix a positive scale Q and put z=exp(c-Qt), kappa_j=-(log gamma_j)/Q>=0.
The elementary inequality 0<=log(1+exp x)-max(x,0)<=log2 gives

\[
\boxed{
\left|\log\det\mathscr Y(z)
+Q\left[(\delta-p)t_++\sum_{j=1}^{p}\min(t_+,\kappa_j)\right]\right|
\le\delta(E+\log2).
}
\tag{PR15}
\]

The bound is uniform for all real t, including moving parameters and thresholds.
It contains no inverse power of min gamma_j. Each nonunit eigenvalue and each
inverse exterior product has the corresponding error E+log2 per contributing
direction. For d>=m and h=0, the model exponent list is d-m zeros, delta-m copies
of t_+, and min(t_+,kappa_j), 1<=j<=m. Sort that list to obtain the individual and
exterior statements. The unit factors from gamma_j=1 remain zero exponents.

## PR5. Coordinate transport, mass, and intersecting kernels

For a fixed coefficient isomorphism S, use
T'=STS^-1, G'=S^-*GS^-1, Lambda'=Lambda S^-1. Then L'=SL, H'=SHS^-1,
and mathscrY'(z)=mathscrY(z) exactly. The original S=k/2+iy coefficient change
and the full-unit isometries must be applied by this paired transport.

Under a common source-mass change G->aG, Q_B->aQ_B and H_K->aH_K, whereas L,H,
A_K and mathscrY are unchanged. The two determinants involving H_K in PR7 acquire
the same factor a^m. This verifies the balancing; no actual source mass is changed.

For an additional original onto observation Xi:B->C define
Q_C=(Xi Q_B^-1 Xi*)^-1 and L_Xi=Q_B^-1 Xi* Q_C. Direct multiplication proves

\[
L_{\Xi\Lambda}=L_\Lambda L_\Xi,\qquad
\mathscr Y_{\Xi\Lambda}(z)=\Xi\mathscr Y_\Lambda(z)L_\Xi.
\tag{PR15a}
\]

Thus the exact minimum and the full measured resolvent pass through nested
observations using the actual maps. Applying PR7 on the composite keeps its full
kernel, including any newly formed intersection with ker T. No equality between
powers of compressed arithmetic operators is implied by this identity.

At h>0 the positive determinant of A_K refers to the full attained metric on
K/(K intersect V). In a fixed frame [I_Z,I_U] of K, its domain Gram is
H_UU-H_UZ H_ZZ^-1 H_ZU and its image Gram is (TI_U)*G(TI_U). Their determinant
ratio is det^+ A_K. The original full determinant of K additionally contains
its inherited determinant on Z. This is the precise remaining factor at an
observation/word-kernel intersection.

## PR6. Exact complex illustration

In Euclidean E=C^3 use

\[
T=\operatorname{diag}(0,2,3i),\quad
\Lambda=\begin{pmatrix}-1&1&0\\-i&0&1\end{pmatrix},\quad
K=\mathbb C(1,1,i)^T.
\]

Then

\[
Q_B=\tfrac13\begin{pmatrix}2&i\\-i&2\end{pmatrix},\quad
\mathscr Y(z)=
\begin{pmatrix}
(3z+4)/(3(z+4))&-4i/(3(z+4))\\
3i/(z+9)&(z+3)/(z+9)
\end{pmatrix},
\]

\[
\boxed{\det\mathscr Y(z)=\frac{z(3z+13)}{3(z+4)(z+9)}.}
\tag{PR16}
\]

Here Gamma=2/3 and A_K=13/3. The off-diagonal entries are nonzero. In the same
Q_B metric the separately compressed arithmetic action T_B=Lambda T L instead
has resolvent determinant 9z^2/(9z^2+52z+36). The two exact rational functions
disagree, exhibiting the omitted terms in that substitution on specified maps.


---

# PR17–PR31. A signed kq-scale determinant in the original observation

This is an additive derivation from LONG_WORD_SOURCE.md, equations (4)–(10),
(37) and (44), and the pinned DCR26–27 receiver. The source's all-direction
outer-minimum estimate and its finite guards retain their supplied written-proof
status. No independent proof of the imported equilibrium theorem is claimed.
All four source cutoffs and the original full physical unit are unchanged.

## PR17. Retained arithmetic data and finite inputs

Keep k=1 mod 4 on the source's proved simple-quartet period domain, and put

\[
q=(k+1)^2,\quad d=(k-7)^2,\quad\Delta=q-d=16k-48,\quad m=8k-16,
\]

\[
Q_k(y)=D_k(y)O_k(y),\quad T_k=D_k(M),\quad M[p]=[yp],\quad S=k/2+iy.
\]

D_k contains the complete pivot-translated interior box and O_k its entire
complement. The same original nonzero conductor pivot proves K intersect ker T_k=0.
In the interior/boundary root ordering the conductor is [A_I,A_partial] with
A_I invertible, and every vector of K has the exact form (Fb,b),
F=-A_I^-1 A_partial. No condition mu_0!=0 is added.

Let pi_partial be the original boundary-value map and let

\[
Q_N^\partial=(\pi_\partial G_N^{-1}\pi_\partial^*)^{-1},\quad
H_{K,N}=I_K^*G_NI_K,
\]

\[
\Gamma_N=H_{K,N}^{-1/2}
(\pi_\partial I_K)^*Q_N^\partial(\pi_\partial I_K)H_{K,N}^{-1/2}.
\tag{PR17}
\]

Every Gamma_N is positive and at most I. Let V_O evaluate degree-below-Delta
polynomials at the boundary roots, and define the single fixed injective matrix

\[
J=V_O^{-1}\pi_\partial I_K.
\]

The uploaded original source minimum is the coefficient Gram mathfrakG_N of
min integral |D_k|^2 |p+O_kh|^2 dmu_k, at degrees Delta-1, Delta, q+Delta-1,
q+Delta. Its supplied all-direction estimate is

\[
e^{c_N-\epsilon_k}I\preceq\mathfrak G_N\preceq e^{c_N+\epsilon_k}I,
\quad\epsilon_k=o(q),
\]

\[
c_L=2q\log q+\eta_Lq,\quad c_H=2q\log q+\eta_Hq,
\quad\eta_L=2\log(4/\pi)-2,\quad\eta_L-\eta_H=C_\partial/2.
\tag{PR18}
\]

The low type is N=q-1,q; the high type is N=2q-1,2q. The original image Gram is
exactly

\[
H_{TK,N}=I_K^*T_k^*G_NT_kI_K=J^*\mathfrak G_NJ.
\tag{PR19}
\]

In particular the fixed coefficient factor det(J*J) cancels only after the
four original signs are applied.

The boundary comparison from LONG_WORD_SOURCE (9) is

\[
a_k I\preceq Q_N^\partial\preceq b_kI,\qquad
\omega_k=\log(b_k/a_k)=o(q),
\tag{PR20}
\]

where, retaining the original arithmetic/Gamma factors ell_k,u_k,

\[
a_k=\ell_k/A^\partial_{2q},\quad b_k=u_k B_k^\partial,
\]

\[
A^\partial_{2q}=\frac{\Delta e^2}{M_\sigma}
(2q+1)^{3/2}(4q+1)^{R_k+1},\quad
B_k^\partial=\Delta M_\sigma
\left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)},
\quad R_k=k\sqrt{\delta^2+\gamma^2},\quad M_\sigma=\sqrt{2\pi}.
\]

For explicit spectral constants set

\[
V_+=\Delta\max(1,R_k)^{\Delta-1},\quad
V_-=\Delta\left(\frac{1+R_k}{2\delta}\right)^{\Delta-1},
\]

\[
E_k=\epsilon_k+
\max\{\log^+(b_kV_+^2),\log^+(V_-^2/a_k)\}=o(q).
\tag{PR21}
\]

The boundary Vandermonde matrix and its full Lagrange inverse satisfy
||V_O||<=V_+, ||V_O^-1||<=V_-. The exact positive word matrix is
(Q_N^partial)^(-1/2) V_O^-* mathfrakG_N V_O^-1 (Q_N^partial)^(-1/2).
Consequently every positive word eigenvalue obeys

\[
e^{c_N-E_k}\le\lambda_{j,N}\le e^{c_N+E_k},\quad1\le j\le\Delta.
\tag{PR22}
\]

PR19 also has relative form bounds exp(c_N+-E_k)J*J. Every zero word mode,
exactly d in number, remains outside this positive list.

## PR18. Complete observed resolvent spectrum with no angle margin in the error

Let

\[
\mathscr Y_N(z)=\Lambda z(zI+T_k^{\dagger_{G_N}}T_k)^{-1}L_N,
\quad L_N=G_N^{-1}\Lambda^*Q_{B,N}.
\]

Its determinant is in the original observed value space; the Q_B isometry of
PR1 merely gives an orthonormal representation.

Order the actual positive Gamma_N eigenvalues gamma_{j,N}, and put
kappa_{j,N}=-q^-1 log gamma_{j,N}>=0. Define one common regularizer at all cutoffs,

\[
z_k(b)=q^{2q}e^{bq},\qquad t_N(b)=\eta_{L/H}-b.
\tag{PR23}
\]

PR15 gives the complete finite scalar formula

\[
\boxed{
\left|\log\det\mathscr Y_N(z_k(b))
+q\left[(\Delta-m)(t_N)_+
+\sum_{j=1}^m\min((t_N)_+,\kappa_{j,N})\right]\right|
\le B_k,\quad B_k=\Delta(E_k+\log2).
}
\tag{PR24}
\]

It is uniform for all real b and includes equality at either edge. The operator
comparison PR13 also determines each logarithmic eigenvalue with error E_k+log2,
and every inverse exterior product with error at most min(p,Delta)(E_k+log2).
No nonzero angle is replaced by a mean. No inverse power of gamma_min occurs.

For d>=m, an exact model exponent list consists of d-m zeros, Delta-m copies of
(t_N)_+, and min((t_N)_+,kappa_{j,N}), j=1,...,m. Sort it to apply the individual
and exterior bounds. At the finitely smaller dimensions PR14, rather than a
negative unit multiplicity, supplies the same determinant statement.

## PR19. A negative kq-scale determinant throughout the original strict interval

Let eta_H<b<eta_L be fixed and tau=eta_L-b>0. At both low endpoints t_N=tau,
and at both high endpoints (t_N)_+=0. Formula PR24 and 0<=min(tau,kappa)<=tau prove

\[
\boxed{
-2\Delta q\tau-4B_k
\le\mathcal R\log\det\mathscr Y_N(z_k(b))
\le-2(\Delta-m)q\tau+4B_k.
}
\tag{PR25}
\]

In particular the original observation's resolvent determinant has an eventually
negative return with an order-kq margin. At b_mid=(eta_L+eta_H)/2 the normalized
bounds are

\[
-8C_\partial\le
\liminf\frac{\mathcal R\log\det\mathscr Y_N(z_k(b_{mid}))}{kq}
\le\limsup\frac{\mathcal R\log\det\mathscr Y_N(z_k(b_{mid}))}{kq}
\le-4C_\partial.
\tag{PR26}
\]

This is a sign and a quantitative interval; it is not an asserted equality
between the two endpoints. It uses the full observed resolvent, not the resolvent
of (Lambda T L)^dagger(Lambda T L).

## PR20. Extend the sign below the high threshold with the original metric order

At l_i=q-1+i, u_i=2q-1+i the canonical source inclusions imply
H_K,u_i<=H_K,l_i. Set B_N=(pi_partial I_K)*Q_N^partial(pi_partial I_K).
PR20 implies B_u_i>=exp(-omega_k)B_l_i. Generalized Rayleigh min–max therefore gives

\[
\gamma_{j,u_i}\ge e^{-\omega_k}\gamma_{j,l_i},\qquad
\kappa_{j,u_i}\le\kappa_{j,l_i}+\omega_k/q,
\tag{PR27}
\]

with corresponding sorted indices. This compares both members of the same
metric pair, not an assumed monotonicity of angle matrices in fixed Euclidean
coordinates.

Define the evaluated nonnegative function

\[
f(b)=(\eta_L-b)_+-(\eta_H-b)_+
=\min\{(\eta_L-b)_+,C_\partial/2\}.
\]

The scalar clipping is increasing and 1-Lipschitz in kappa. PR27 and t_l>=t_u
show that the sum of the clipped low angles exceeds the sum of clipped high
angles by at least -2m omega_k/q. Substitution in PR24 proves

\[
\boxed{
\mathcal R\log\det\mathscr Y_N(z_k(b))
\le-2(\Delta-m)q f(b)+2m\omega_k+4B_k.
}
\tag{PR28}
\]

The exact finite negative region is

\[
f(b)>\epsilon_k^{edge}:=
\frac{m\omega_k+2\Delta(E_k+\log2)}{(\Delta-m)q}.
\tag{PR28a}
\]

Every constant in this guard is supplied in PR18–PR21, and epsilon_k^edge=o(1).
It therefore controls moving regularizers without asserting a step value inside
an uncomputed boundary layer.

The finite bound holds for every real b. For each fixed b<eta_L its leading term
is strictly negative; for b<=eta_H it saturates at -(Delta-m)C_partial q.
For each fixed b>eta_L, PR11 gives absolute convergence of the return to zero.
At b=eta_L, PR24 proves only the normalized statement o(kq), without assigning a
raw transition value.

## PR21. Deep regularization recovers the full original kernel with its exact offset

A completely explicit, sharper angle margin is obtained from the original
lattice and graph (Fb,b). For an upper root omega_alpha put
r_alpha,beta=max(|a_alpha-a_beta|,|b_alpha-b_beta|). Every distance is at least
2delta r_alpha,beta and at most 8j grid points occur at shell j. Thus

\[
\sum_{\beta\ne\alpha}\log(k/r_{\alpha\beta})
\le\sum_{j=1}^k8j(k/j-1)=4k(k-1)\le4q.
\]

The complete Lagrange denominator is at least (2delta k)^(q-1) exp(-4q).
Successive Gamma multiplication bounds retain every numerator root and give
norm at most sqrt(M_sigma)(2q+R_k)^(q-1). Summing the squared norms of all q
Lagrange columns proves

\[
G_N^{val}\preceq u_k B_{lat,k}I,\qquad
\boxed{
B_{lat,k}=qM_\sigma e^{8q}
\left(\frac{2q+R_k}{2\delta k}\right)^{2(q-1)}.
}
\tag{PR29a}
\]

Every lifting polynomial has degree q-1, so it is admitted at all four original
cutoffs. This strengthens the first note's cruder B_full by retaining the complete
lattice-distance product rather than charging the smallest distance q-1 times.

The exact strip map N_k=[R,I] satisfies N_k M_A=0. In the dual root order its
transpose identifies the actual graph F=R^T; hence ||F||<=sqrt(q)C_path^(10k), where
C_path=A_1/|a_*| is the retained nonzero pivot ratio. The boundary norm of a
kernel vector (Fb,b) is at least a_k||b||^2, whereas its full norm is at most
u_k B_lat,k(1+q C_path^(20k))||b||^2. Therefore

\[
\boxed{
\Gamma_N\succeq\vartheta_k I,\qquad
\vartheta_k=\min\left\{1,
\frac{a_k}{u_kB_{lat,k}(1+qC_{path}^{20k})}\right\}>0.
}
\tag{PR29}
\]

All fixed-period and original source constants remain. Since their logarithms
here are o(q), the explicit bound has

\[
-\log\vartheta_k
=2q\log(q/k)+(8-2\log\delta)q+o(q).
\tag{PR29b}
\]

This is the asymptotic of the specified conservative lower bound, not a value
assigned to any actual angle. Combining it with PR22 evaluates a lower rate
for EVERY original-kernel word-energy direction:

\[
\boxed{
\liminf_{k\to\infty}\min_N
\left\{\frac{\log\lambda_{min}(A_{K,N})-2q\log k}{q}
-\eta_{L/H}\right\}\ge-8+2\log\delta.
}
\tag{PR29c}
\]

The exact finite version is A_K,N>=vartheta_k exp(c_N-E_k)I. This is the full
rectangular energy of T_k on the original K, not the square of a compressed
arithmetic endomorphism. Its word degree is d=q-O(k); all its primary zero modes
outside this transverse K remain in H.

Choose the same positive regularizer at all four cutoffs,

\[
z_k^{deep}=\vartheta_k e^{c_H-E_k-q}.
\]

The positive compression A_K,N satisfies A_K,N>=vartheta_k exp(c_H-E_k)I.
Expand the exact PR6 determinant at this regularizer. The two finite errors obey

0<=logdet(I+z A_K,N^-1)<=m exp(-q),
0<=logdet(I+z B_+,N^-1)<=Delta exp(-q).

Since A_K,N=H_K,N^-1/2 H_TK,N H_K,N^-1/2 and PR19 retains the same J at all
endpoints, the four-return is

\[
\boxed{
\left|\mathcal R\log\det\mathscr Y_N(z_k^{deep})
+(\Delta-m)C_\partial q+\mathcal K_k\right|
\le E_k^{deep},
}
\tag{PR30}
\]

\[
\mathcal K_k=\mathcal R\log\det H_{K,N},\qquad
E_k^{deep}=\min\{4(m+\Delta)E_k,\ 2m\omega_k+4(\Delta-m)E_k\}+2(m+\Delta)e^{-q}=o(kq).
\]

For the sharper second term in this error, use the exact PR8a factor with
rho=Delta-m. PR22 gives exp(-c_N-E_k)I<=Xi_N<=exp(-c_N+E_k)I. Hence

\[
\log\det\Xi_N=-\rho c_N+e_N,\qquad |e_N|\le\rho E_k.
\]

Also logdet Gamma_N=logdet B_N-logdet H_K,N, where
B_N=(pi_partial I_K)*Q_N^partial(pi_partial I_K). The full source minima make
B_N decrease with cutoff, and PR20 gives

\[
0\le\mathcal R\log\det B_N\le2m\omega_k.
\]

Thus PR8a and the same thermal remainder prove the directed bound

\[
-4\rho E_k-\varepsilon_{reg}
\le\mathcal R\log\det\mathscr Y_N(z_k^{deep})+\rho C_\partial q+\mathcal K_k
\le2m\omega_k+4\rho E_k+\varepsilon_{reg},
\quad\varepsilon_{reg}=2(m+\Delta)e^{-q}.
\tag{PR30a}
\]

The complementary space and its full Schur minimum may vary with N; its form
bound is valid on every one of those actual spaces, so no common eigenvectors
or generic orientation is needed.

There is now a fixed-exponent common regularizer as well. For any fixed

\[
b<\eta_H-8+2\log\delta,\qquad z_k=k^{2q}e^{bq},
\tag{PR30b}
\]

PR29c makes z_k/min_N lambda_min(A_K,N) exponentially small. The positive full
word modes are still larger, by PR22. Therefore the same leading identity PR30
holds at PR30b with an explicitly exponentially decreasing regularization error.
This regularizer is at the k^(2q) arithmetic-root scale, rather than specified
using an unknown original Gram eigenvalue.

The coefficient is Delta-m=8k-32, not Delta or m. It arises from the retained
zero-word modes in PR6 and cancels neither the original kernel volume nor the
positive word determinant.

The pinned DCR27 receiver states, with its full explicit error E_k^K=o(kq),

0<=mathcalK_k<=g_k C_partial q+E_k^K,  g_k=Delta-v.

Consequently

\[
\boxed{
-(24k-80-v)C_\partial q-E_k^K-E_k^{deep}
\le\mathcal R\log\det\mathscr Y_N(z_k^{deep})
\le-(8k-32)C_\partial q+E_k^{deep}.
}
\tag{PR31}
\]

The unknown kernel allocation remains in the exact equality PR30. The new
observable has a sign without assigning that unknown value.


---

# PR32–PR44. Activation, all-direction source extraction, and exact sharpness

## PR32. The same measured resolvent at the actual source activations

Retain the exact source covariance family

\[
G_N(\alpha)^{-1}=(1-\alpha)G_N^{-1}+\alpha(G_N^J)^{-1},\quad0\le\alpha\le1.
\]

The original T_k, Lambda, I_K, interior polynomial D_k and boundary polynomial
O_k are unchanged. Define the observed resolvent through the actual Q_B(alpha)
and its minimum section at each alpha. Every finite identity PR1–PR16 holds on
this family, at both endpoints and with the full normal-source cross Gram.

For alpha>0 the covariance order gives

\[
G_N^J\preceq G_N(\alpha)\preceq\alpha^{-1}G_N^J.
\tag{PR32}
\]

The supplied complete joint-source comparison is
L_k^-1 T_val<=G_N^J<=B_k T_val, with log(L_k B_k)=o(q).
In that stated reference T_k is diagonal with values D_k(omega) at the original
boundary roots and zero at the interior roots. Thus

\[
\|T_k\|_{G_N(\alpha)}^2
\le\alpha^{-1}L_kB_k(2kR_h)^{2d}=:M_k(\alpha).
\tag{PR33}
\]

This uses the entire original scalar/tensor minimum: alpha is its stated penalty,
not a rescaling of the original physical measure. Compression in the actual
observation and rank(T_k)=Delta now give

\[
\boxed{
0\le-\log\det\mathscr Y_{N,\alpha}(z)
\le\Delta\log\left(1+\frac{M_k(\alpha)}z\right),
}
\tag{PR34}
\]

\[
\|I-\mathscr Y_{N,\alpha}(z)\|_1
\le\Delta\frac{M_k(\alpha)}{z+M_k(\alpha)}.
\]

The trace norm is in the actual observed metric. The rank factor is Delta, not
q-m. At z=z_k(b) from PR23, for b in a fixed bounded interval,

\[
\log\frac{M_k(\alpha)}{z_k(b)}
\le-\log\alpha-2q\log(q/k)+O_h(q).
\tag{PR35}
\]

Consequently, at every fixed 0<=beta<1 and alpha_k=exp[-2beta q log(q/k)], the
observed determinant and its four-return tend to zero absolutely. More generally
PR35 is the finite criterion on any moving activation; it does not assign an
unproved law on the critical scale beta=1. In particular the canonical negative
return of PR25 or PR28 and this activated vanishing concern exactly the same
arithmetic word and observation. Their change of metric remains in PR32 and in
the complete source determinant identities; it is not a zero-cost substitution.

### Uniform control over every joint-source regularizer

For any two positive metrics aG0<=G1<=bG0 on the SAME E, the positive squared
singular values of T and of T restricted to the fixed K each change by factors
between a/b and b/a. This follows from the two actual numerator/denominator
Rayleigh norms; their kernels are unchanged. Since log(1+lambda/z) is 1-Lipschitz
in log lambda, PR8 gives the finite comparison

\[
\boxed{
|\log\det\mathscr Y_{G_1}(z)-\log\det\mathscr Y_{G_0}(z)|
\le(\delta+p)\log(b/a),\qquad z>0,
}
\tag{PR35a}
\]

where p=rank(T|K), with intersections retained exactly as in PR8.
For the original joint-source family p=m, delta=Delta and the common reference
T_val is the same at all four cutoffs. Therefore

\[
\boxed{
\sup_{z>0}\left|\mathcal R\log\det\mathscr Y_{N,J}(z)\right|
\le4(\Delta+m)\log(L_kB_k)=o(kq).
}
\tag{PR35b}
\]

The powers of log z cancel under the four signs, so the finite zero-regularizer
limit of the return has the same bound. This is a uniform all-regularizer result
for the original joint source, including the scale PR30b. It does not compare
the canonical source to the joint source at zero cost.

## PR33. Full-root innovations from the second supplied note

Use the original lower-root evaluation matrix E_N, the actual invariant rows W_N,
and the Gamma source cutoff D=N-v. Define

\[
C_N=W_N[I-E_N^*(E_NE_N^*)^{-1}E_N]W_N^*.
\]

For the original appended columns e_N,w_N, set

\[
\kappa_N=1+e_N^*(E_NE_N^*)^{-1}e_N,\qquad
v_N=w_N-W_NE_N^*(E_NE_N^*)^{-1}e_N.
\]

The unit new kernel direction is
(-E_N*(E_NE_N*)^-1 e_N,1)^T/sqrt(kappa_N). It is orthogonal to the entire old
lower-root ideal, so the exact update is

\[
C_{N+1}=C_N+v_Nv_N^*/\kappa_N.
\tag{PR36}
\]

This repeats the second note's formula as the input map to the new estimates.
It is not an omitted lower-root projection. Its complex cross term is explicit.

For i=0,1, collect all q updates from l_i=q-1+i through u_i=2q-1+i. Let
V_i^{all} be their innovation column matrix and X_i=C_l_i^-1/2 V_i^{all}.
Then

\[
G_i=\log\det(I+X_iX_i^*)\ge0,\qquad
\mathcal R\log\det C_N=-G_0-G_1.
\tag{PR37}
\]

A_i=[I_r,X_i] is a physical orthonormal-column source map in the explicitly
normalized target coordinates. Its first r source columns are the isometry
R_l_i^dagger C_l_i^-1/2 in the old ideal; the appended columns are the actual
orthogonal innovations. The old zero-value source summand remains separate.

## PR34. Selected original columns control every spectral direction

Choose r actual columns of A_i as a nonsingular matrix V_i. After the exact
column permutation write

\[
A_iP_i=V_i[I_r,T_i],\qquad |(T_i)_{ab}|\le2.
\tag{PR38}
\]

There are q unselected columns. The exact source covariance is

\[
A_iA_i^*=V_i(I+T_iT_i^*)V_i^*.
\]

Because Tr(T_iT_i*)<=4rq,

\[
\boxed{
V_iV_i^*\preceq A_iA_i^*\preceq(1+4rq)V_iV_i^*.
}
\tag{PR39}
\]

Thus all corresponding ordered eigenvalues obey

\[
0\le\log\lambda_j(A_iA_i^*)-2\log s_j(V_i)
\le\log(1+4rq),\qquad1\le j\le r.
\tag{PR40}
\]

Every p-dimensional exterior volume has error at most p log(1+4rq). Every fixed
restriction or full attained quotient of the inverse metric has the same
relative form bound and rank-p logarithmic error. This is a full spectral
statement, not just the determinant estimate of the supplied note.

The sharper full determinant bound remains

\[
G_i=\log|\det V_i|^2+\rho_i,\quad
0\le\rho_i=\log\det(I+T_iT_i^*)\le r\log(1+4q).
\tag{PR41}
\]

Its inverse, including all phase data, is exactly

\[
(A_iA_i^*)^{-1}=V_i^{-*}(I+T_iT_i^*)^{-1}V_i^{-1}.
\]

The residual has eigenvalues between 1/(1+4rq) and 1. Only after the displayed
coordinate map V_i^-1 has been applied is that a bounded-coefficient remainder.
An original action and marked class must also transform to V_i^-1 A V_i and
V_i^-1 x. The residual cannot be dropped in a complex-current calculation.

## PR35. The number of swaps improves to O(kq)

Retain the scalar Gamma/Hankel expression A_{k,v} and full finite error E_k^src
from INNOVATION_AND_ES_SOURCE, equations (8)–(9). They state

\[
|\mathcal K_k-\log\mathcal A_{k,v}+G_0+G_1|\le E_k^{src}.
\tag{PR42}
\]

For reference its unchanged scalar is

\[
\mathcal A_{k,v}=
\frac{\Delta_{g-1}(q')\Delta_g(q')\Delta_{q-1}(q-v)\Delta_q(q-v)}
{\Delta_{q+g-1}(q')\Delta_{q+g}(q')\Delta_0(q-v)},
\]

\[
\Delta_j(a)=\det[\nu_{2a+i+l}]_{i,l=0}^j,\quad
\nu_{2b}=(2b)![t^{2b}](\cos t)^{-1/2},\quad\nu_{2b+1}=0.
\]

The original Gamma mass cancels because numerator and denominator contain equal
total matrix dimensions. E_k^src is the exact supplied full-source error,
O(q log(q+2)) on its retained finite guards.

Monotonicity of the original kernel metric gives mathcalK_k>=0, so PR42 proves

\[
G_0+G_1\le\log\mathcal A_{k,v}+E_k^{src}.
\]

The DCR26 receiver and CGS17 unprojected determinant bound imply, by subtracting
the two equations for the SAME mathcalK_k,

\[
\left|\log\mathcal A_{k,v}-gC_\partial q\right|
\le E_k^{src}+B_{DCR,k}+\sum_N K_N=o(kq).
\]

No value for mathcalK_k was needed to obtain this scalar estimate. Starting with
the identity columns, each accepted swap whose certified modulus exceeds 3/2
raises selected squared volume by more than (3/2)^2. The total selected volume
is bounded above by exp(G_0+G_1). Hence the total number of swaps in BOTH searches
is at most

\[
\boxed{
\frac{\max(0,\log\mathcal A_{k,v}+E_k^{src})}{2\log(3/2)}=O(kq).
}
\tag{PR43}
\]

This improves the older O(kq log q) endpoint bound. It bounds swaps, not the bit
cost of obtaining reliable values of the original period-dependent entries.
The supplied overlapping acceptance tests <=2 and >3/2 remain valid.

Let Z_k^piv=log A_{k,v}-log|det V_0 det V_1|^2. PR42 and PR41 give the supplied
kernel interval with every residual retained. Together with PR30 the NEW measured
resolvent interval is

\[
\boxed{
\begin{split}
-(\Delta-m)C_\partial q-Z_k^{piv}-E_k^{src}-E_k^{deep}
&\le\mathcal R\log\det\mathscr Y_N(z_k^{deep})\\
&\le-(\Delta-m)C_\partial q-Z_k^{piv}
+E_k^{src}+2r\log(1+4q)+E_k^{deep}.
\end{split}}
\tag{PR44}
\]

Both selected determinants consist of actual original source columns. The exact
values of those columns have not been numerically supplied or evaluated here.

## Exact sharpness with the same finite word and observation

This is a declared auxiliary source family, not an arithmetic xi packet.
It checks that the word spectrum and boundary quotient alone do not fix the
kernel allocation. On C^Delta direct-sum C^Delta retain

T=diag(0,I_Delta),
K=span{(e_j,e_j):1<=j<=m},

and the same onto observation with exactly that kernel. For a>=1 use either

\[
G_\pm(a)=\begin{pmatrix}aI&\pm(a-1)I\\\pm(a-1)I&aI\end{pmatrix}.
\]

Their common boundary quotient is ((2a-1)/a)I. Their complete positive word
spectrum is Delta copies of a^2/(2a-1). Every V-zero mode is retained. The two
kernel Grams and compressed kernel energies are instead

\[
H_{K,+}=(4a-2)I_m,\quad A_{K,+}=a/(4a-2)I_m,
\]

\[
H_{K,-}=2I_m,\quad A_{K,-}=a/2\,I_m.
\]

Therefore their exact measured determinants are

\[
\det\mathscr Y_\pm(z)
=\frac{z^{\Delta-m}(z+A_{K,\pm}^{scalar})^m}
{(z+a^2/(2a-1))^\Delta}.
\]

Both metrics increase with a in positive-form order, so setting a_low=R^2,
a_high=R gives nested positive quotient metrics. They have an actual finite
source realization: take a square-root covariance source at the low endpoint
and add a square root of the positive covariance difference at the high one.
At z=R^(3/2), with two copies of each endpoint,

\[
\mathcal R\log\det\mathscr Y_+=-\Delta\log R+O(1),\qquad
\mathcal R\log\det\mathscr Y_-=-(\Delta-m)\log R+O(1).
\]

Meanwhile their kernel returns are 2m log R+O(1/R) and zero. These exact maps
attain both rank bounds in the strict-interval argument. They demonstrate why
the actual invariant rows still have to be evaluated for an equality value.
The source and metric choices of the original programme are not replaced by
these illustrations.

## Sources and verification scope

LONG_WORD_SOURCE.md is the first upload, preserved byte for byte. Its equation
(8) supplies the all-direction image form; (9) the boundary quotient; (10) the
positive word spectrum; (37) the original kernel angle; (44) its finite margin.

INNOVATION_AND_ES_SOURCE.md is the second upload, preserved byte for byte. This
continuation uses its RH original-root formulas (1)–(10). Its later ES receiving
bounds stay in their stated label/receiving metrics. No new ES-to-RH map or
counterexample claim is introduced here.

DCR1–27 was inspected at GitHub commit bee43be41d2f6f872869d5e258fa5f752335a5ad,
path workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/
009/CONDUCTOR_DIVISOR_COVARIANCE_RETURN.tex, blob
256bfb0f4eb295bf3094c81f6c166cafdb96c316. Its EIQ/OOQ provider remains an inherited
input at the source's written-proof status, not a theorem newly reproved here.

The bounded interpolation-factor context is classical: M. Gu and S. C. Eisenstat,
Efficient Algorithms for Computing a Strong Rank-Revealing QR Factorization,
SIAM Journal on Scientific Computing 17 (1996), 848–869, doi:10.1137/0917055.
PR39–43 were derived directly for the specified source columns. The Gamma
convention is NIST DLMF 18.23.7, with its source note crediting Ismail (2009).

The checker uses exact Gaussian-rational auxiliary matrices. It tests the full
resolvent determinant, the retained intersection zeros, noncommuting metric
blocks, all principal-minor form bounds in the fixtures, full-root innovations,
selected-column residuals and the exact sharpness examples. These checks do not
validate an unspecified native period, xi packet, or the imported analytic
asymptotics.
