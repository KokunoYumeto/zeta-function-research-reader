# Independent exact review of LC13–LC16

Review date: 13 September 2026. This independently delegated review derives and checks the full constituent comparison appended to the original Laplacian-control chapter. The complete current LC source was read, including LC13–LC16. The actual constituent source SC1–SC16 and the period equation PC18 with its preceding contour calculation were read to verify the comparison's inputs. The previously reviewed Toda dependency concerns LC1–LC3 and has its own complete review.

No primary TeX was edited. No mathematical checker, numerical test, Lean process, or PDF build was run. The arguments below establish the finite identities directly, without an estimate uniform in the arithmetic parameters.

## Exact editions

| Source | SHA-256 |
|---|---|
| work/period_laplacian_control_bridge_20260913.tex | 84d884eeceae8ab339b78c29404d86798fcd04b6d40dde1abcff1cc7ed631231 |
| work/sga_constituent_period_curvature_20260913.tex | f7cbbb2da3a97722c9f9128602b4de64ad1ab9cfccdbb03e8ee9363321f7de63 |
| work/period_critical_kernel_bridge_20260913.tex | 93a9d828e86608699b83cf331f77f77ae5062505293f6f7e30e69db77af4c5f9 |

Verdict: LC13–LC16 and their final curvature comparison are correct at the pinned edition. The strict hypothesis \(0<\dim F<q\), the original metric, the actual period-coordinate metric, both extremal eigenvalues, the parameter factors \(|t|^2\) and \(|u|^{-2}\), and the complete two-term loss are all retained. No mathematical correction is required.

The first extension edition read had SHA-256 11acd1f4437984c94ef21c961973d83445ad4fcc81f9935398e25e4cff111fa2. The subsequent edition dd3cb1ea68950ee77c0b140e30771d4be5875d5ede58ac6ae31f098961ba5b7d added the complete source primitive LC12a and named the coefficient vector \(f=G^{-1}\ell^*\), consistently with LC5. Those additions were read and checked. The final pinned edition additionally identifies \(W_t\) as the control form and explicitly proves its correspondence \(v^*W_tw=\langle v,X_tw\rangle_G\) with the endomorphism \(X_t=G^{-1}W_t\). The exact final wording was inspected; the constituent formulas are unchanged. Section 10 below gives the independent LC12a derivation.

## 1. Original constituent and the exact ideal map

Keep

\[
E=\mathbb C[S]/(\chi),\qquad q=\deg\chi,\qquad
A=M_S,\qquad e_0=[1],\qquad
\ell[P]=[S^{q-1}]\operatorname{rem}_\chi P.
\]

The polynomial \(\chi\) is the original monic one, including every repeated factor. At the fixed admitted source degree, keep \(G=G_N>0\). The map

\[
I:F\hookrightarrow E,\qquad AI=IA_F,\qquad
0<p:=\dim F<q
\]

is the actual injective constituent map. The inequalities imply \(q>1\). They exclude the zero constituent and the full quotient, both of which would invalidate the asserted strict positivity of one of the subsequent factors.

Let \(W=I(F)\). Invariance under \(A\) implies invariance under every polynomial in \(A\). Since every element of \(E\) is a polynomial in \(S\), this says that \(W\) is an ideal in \(E\). Its inverse image under the quotient map \(\mathbb C[S]\to E\) is a nonzero ideal containing \((\chi)\). To see directly why it has the claimed principal generator, choose a nonzero polynomial of minimal degree in that ideal and divide it by its leading coefficient to obtain a monic polynomial \(g\). Divide any other ideal element by \(g\); the remainder is again in the ideal and has smaller degree, so it is zero. Thus the ideal is \((g)\). Since \(\chi\) belongs to it, write \(\chi=gh\) with monic complementary factor \(h\).

The complete constituent is described by the exact map

\[
\mathbb C[S]/(h)\longrightarrow W,\qquad
[a]_h\longmapsto[ga]_\chi.
\]

It is well defined because a multiple of \(h\) maps to a multiple of \(\chi=gh\). It is onto by the definition of the ideal \((g)\). It is injective because \(ga\) divisible by \(gh\) implies \(a\) divisible by \(h\), using cancellation by the nonzero polynomial \(g\) in \(\mathbb C[S]\). Therefore \(\deg h=p\), \(\deg g=q-p\), and

\[
[g],[Sg],\ldots,[S^{p-1}g]
\]

is an ordered basis of \(W\). The last polynomial is monic of degree \(q-1\), so its class has \(\ell\)-value one. Consequently

\[
L:=\ell I:F\longrightarrow\mathbb C
\]

is nonzero and onto. The actual row in the original constituent coordinates remains \(\ell I\); no change of its entries is made by describing this ideal basis. If \(e_0\) belonged to the proper ideal \(W\), multiplication by any element of \(E\) would put every element in \(W\), a contradiction. Thus \(e_0\notin W\).

This derivation uses no square-free replacement, no diagonalization of \(A_F\), and no coprimality assumption on \(g,h\). It covers every repeated-root constituent in the stated range.

## 2. LC13: projection and the two positive observations

Define on the unchanged coefficient spaces

\[
G_F=I^*GI,\qquad
P_F=IG_F^{-1}I^*G,\qquad
f=G^{-1}\ell^*,
\]

\[
a_0=e_0^*Ge_0,\qquad
b_0=\ell G^{-1}\ell^*,\qquad
a_\perp=e_0^*G(1-P_F)e_0,\qquad
b_F=LG_F^{-1}L^*.
\]

For every nonzero \(x\in F\), injectivity gives \(Ix\ne0\), hence \(x^*G_Fx=(Ix)^*G(Ix)>0\). Thus \(G_F\) is positive definite. Multiplication gives

\[
P_F^2=IG_F^{-1}(I^*GI)G_F^{-1}I^*G=P_F,
\qquad
P_F^*G=GP_F.
\]

Its image is contained in \(W\), and \(P_FI=I\), so its image equals \(W\). These identities prove that it is the \(G\)-orthogonal projection onto the original constituent.

For any \(v\in E\), the two vectors \(P_Fv\) and \((1-P_F)v\) are \(G\)-orthogonal, since

\[
(P_Fv)^*G(1-P_F)v=v^*GP_F(1-P_F)v=0.
\]

In particular,

\[
a_\perp=\|(1-P_F)e_0\|_G^2.
\]

The vector is nonzero because \(e_0\notin W\); therefore \(a_\perp>0\).

Furthermore \(Gf=\ell^*\), so

\[
I^*Gf=I^*\ell^*=L^*,
\qquad
P_Ff=IG_F^{-1}L^*.
\]

Taking its original squared norm gives

\[
\|P_Ff\|_G^2
=LG_F^{-1}(I^*GI)G_F^{-1}L^*
=LG_F^{-1}L^*=b_F.
\]

Because \(L\ne0\) and \(G_F^{-1}>0\), this number is strictly positive. The unrestricted vector satisfies \(\|f\|_G^2=b_0>0\). Thus all positivity assertions in LC13 follow from the actual ideal and the original metric.

## 3. The actual period map and the comparison eigenvalues

Fix the original nonzero parameter \(u\in\mathbb C^*\), its chosen argument, and the original contour orientations. The constituent source uses

\[
\Phi_t(S)=\frac{S^{q+1}}{q+1}
+\sum_{a=0}^{q-1}\frac{c_aS^{a+1}}{a+1}-tS,
\qquad
\chi(S)=S^q+\sum_{a=0}^{q-1}c_aS^a,
\]

\[
\Pi_{jb}(t)=\int_{\Gamma_j}e^{\Phi_t(S)/u}S^b\,dS,
\qquad
\Gamma_j=-\ell_0^{\rm ray}+\ell_j^{\rm ray},
\qquad 1\le j\le q,\quad 0\le b<q.
\]

The previously proved full period determinant is nonzero at every parameter, including collisions, and the locally dominating ray estimate permits differentiation in \(t\). The exact constant-polynomial relation is \([\chi-t]=0\) in the period reduction. Differentiating a column inserts \(-S/u\), and reduction of its last power therefore gives the exact equation

\[
\Pi'=-\Pi(A+tR)/u,\qquad R=e_0\ell.
\]

These are the period-map inputs from SC1–SC6 and PC18. The present comparison neither changes the periods' phases nor changes the target Hermitian metric: its target is the declared period-coordinate metric \(I_q\).

Write

\[
Q(t)=\Pi(t)^*\Pi(t),\qquad B(t)=G^{-1}Q(t).
\]

Invertibility of \(\Pi\) gives \(Q>0\). The operator \(B\) is \(G\)-self-adjoint:

\[
B^{\dagger_G}=G^{-1}B^*G
=G^{-1}QG^{-1}G=B.
\]

It is positive because \(v^*GBv=\|\Pi v\|_{I_q}^2>0\) for every \(v\ne0\). Equivalently, its transported matrix

\[
G^{1/2}BG^{-1/2}=G^{-1/2}QG^{-1/2}
\]

is Hermitian positive definite. Thus \(B\) has actual positive eigenvalues. Define \(m(t)\) and \(M(t)\) as their minimum and maximum. The spectral theorem gives, on the original space,

\[
0<m(t)\le M(t)<\infty,\qquad
m(t)G\preceq Q(t)\preceq M(t)G.
\]

These are finite quantities computed from the original matrices at the specified parameter. They are not assumed to admit a uniform arithmetic bound.

## 4. LC14: exact comparison of the residuals

Let

\[
Y(t)=\Pi(t)I,\qquad
H_F(t)=Y(t)^*Y(t),\qquad
P^{\rm per}(t)=Y(t)H_F(t)^{-1}Y(t)^*,
\]

\[
z(t)=(1-P^{\rm per}(t))\Pi(t)e_0.
\]

The map \(Y\) is injective, so \(H_F>0\). Direct multiplication shows that \(P^{\rm per}\) is the orthogonal projection onto \(Y(F)\) in the declared target metric \(I_q\). Hence

\[
\|z(t)\|_{I_q}^2
=\min_{x\in F}\|\Pi(t)(e_0-Ix)\|_{I_q}^2.
\]

The same minimization in the original metric is explicit. Put \(x_G=G_F^{-1}I^*Ge_0\). Then \(Ix_G=P_Fe_0\), and for every \(x\),

\[
\|e_0-Ix\|_G^2
=a_\perp+(x-x_G)^*G_F(x-x_G).
\]

Thus its minimum is \(a_\perp\), attained at \(x_G\).

For every \(x\), the lower quadratic-form comparison gives

\[
\|\Pi(e_0-Ix)\|_{I_q}^2
\ge m(t)\|e_0-Ix\|_G^2
\ge m(t)a_\perp.
\]

Taking its minimum proves the lower residual bound. For the upper bound, evaluate the period distance at the specific original minimizer \(x_G\):

\[
\|z\|_{I_q}^2
\le\|\Pi(e_0-Ix_G)\|_{I_q}^2
\le M(t)\|e_0-Ix_G\|_G^2
=M(t)a_\perp.
\]

Consequently

\[
m(t)a_\perp\le\|z(t)\|_{I_q}^2\le M(t)a_\perp.
\]

Both bounds are strictly positive on their left side. They in particular show \(z(t)\ne0\), consistently with invertibility of \(\Pi(t)\) and \(e_0\notin W\).

## 5. LC14: inverse compression and the row functional

Compression of \(mG\preceq Q\preceq MG\) by the unchanged map \(I\) gives

\[
m(t)G_F\preceq H_F(t)\preceq M(t)G_F.
\]

For clarity, the precise inverse-order identity does not require any pair of these matrices to commute. For a positive matrix \(T\) and column \(w\), completion of the square gives

\[
2\operatorname{Re}(w^*x)-x^*Tx
=w^*T^{-1}w
-(x-T^{-1}w)^*T(x-T^{-1}w).
\]

Therefore its maximum over all \(x\) is \(w^*T^{-1}w\). If \(T_1\preceq T_2\), the expression being maximized for \(T_1\) is pointwise greater than or equal to the expression for \(T_2\), proving \(T_1^{-1}\succeq T_2^{-1}\). Applying this to the three compressed matrices gives

\[
\frac1{M(t)}G_F^{-1}\preceq H_F(t)^{-1}
\preceq\frac1{m(t)}G_F^{-1}.
\]

Congruence by the actual row \(L\) yields exactly

\[
\frac{b_F}{M(t)}
\le LH_F(t)^{-1}L^*
\le\frac{b_F}{m(t)}.
\]

The reciprocal factors are \(1/M\) and \(1/m\), without an extra square or an omitted compression matrix. Since \(b_F>0\), the middle factor is strictly positive.

## 6. LC15: the full curvature coefficient and its bounds

Keep the original constituent fixed in the original algebra. It satisfies \(AI=IA_F\); no invariance under \(A+tR\) is needed. Its period derivative is computed using the actual period equation:

\[
Y'=\Pi'I=-\Pi AI/u-t\Pi RI/u
=-YA_F/u-t\Pi e_0L/u.
\]

Because \((1-P^{\rm per})Y=0\), the complete normal derivative is

\[
(1-P^{\rm per})Y'=-tzL/u.
\]

This proves the exact rank-one map from the constituent to the normal period direction, including its parameter factor and complex denominator.

Use the Wirtinger derivatives \(\partial_t=\tfrac12(\partial_x-i\partial_y)\) and \(\partial_{\bar t}=\tfrac12(\partial_x+i\partial_y)\), as in SC15. Holomorphy of \(Y\) gives

\[
\partial_tH_F=Y^*Y',\qquad
\partial_{\bar t}H_F=Y'^*Y,\qquad
\partial_{\bar t}\partial_tH_F=Y'^*Y'.
\]

The positive real determinant \(\det H_F\) has a unique real logarithm. Differentiation of \(H_F^{-1}H_F=I\) yields

\[
\partial_{\bar t}H_F^{-1}
=-H_F^{-1}Y'^*YH_F^{-1}.
\]

Thus determinant differentiation and cyclic invariance of trace give

\[
\begin{aligned}
\partial_{\bar t}\partial_t\log\det H_F
&=\operatorname{Tr}\left(
H_F^{-1}Y'^*Y'
-H_F^{-1}Y'^*YH_F^{-1}Y^*Y'\right)\\
&=\operatorname{Tr}\left(
H_F^{-1}Y'^*(1-P^{\rm per})Y'\right).
\end{aligned}
\]

The period complement is an orthogonal projection, so substituting its complete normal derivative proves

\[
Y'^*(1-P^{\rm per})Y'
=\frac{|t|^2}{|u|^2}\,L^*z^*zL.
\]

Since \(z^*z\) is scalar and
\(\operatorname{Tr}(H_F^{-1}L^*L)=LH_F^{-1}L^*\), this is exactly

\[
\partial_{\bar t}\partial_t\log\det H_F(t)=|t|^2c_F(t),
\qquad
c_F(t)=\frac{\|z(t)\|_{I_q}^2}{|u|^2}\,
LH_F(t)^{-1}L^*>0.
\]

The complex factors yield \(|u|^{-2}\) and \(|t|^2\). There is no real-Laplacian factor of four in this formula because the displayed differential operator is precisely \(\partial_{\bar t}\partial_t\), with the stated Wirtinger conventions.

Multiplication of the positive lower bounds from Sections 4 and 5, and then multiplication of the positive upper bounds, proves

\[
\boxed{
\frac{m(t)}{M(t)}\frac{a_\perp b_F}{|u|^2}
\le c_F(t)\le
\frac{M(t)}{m(t)}\frac{a_\perp b_F}{|u|^2}.}
\]

This is LC15. It is valid at \(t=0\) as a bound on the strictly positive coefficient \(c_F(0)\). The actual curvature is zero there because the exact equality retains \(|t|^2\). For \(t\ne0\), the curvature is strictly positive.

## 7. LC16: the complete projection loss

The original projection decompositions give

\[
a_0=\|P_Fe_0\|_G^2+a_\perp,\qquad
b_0=b_F+\|(1-P_F)f\|_G^2.
\]

Write \(a_\parallel=\|P_Fe_0\|_G^2\) and
\(b_\perp=\|(1-P_F)f\|_G^2\) only for the following expansion. The complete product is

\[
a_0b_0=(a_\parallel+a_\perp)(b_F+b_\perp)
=a_\perp b_F+a_\parallel b_0+a_\perp b_\perp.
\]

With the original \(\sigma_N^2=a_0b_0\), this proves

\[
\boxed{
\sigma_N^2-a_\perp b_F
=\|P_Fe_0\|_G^2\,b_0
+a_\perp\|(1-P_F)G^{-1}\ell^*\|_G^2\ge0.}
\]

Both contributions are retained. Since \(b_0>0\) and \(a_\perp>0\), their sum vanishes exactly when \(P_Fe_0=0\) and \((1-P_F)f=0\). This identifies the equality geometry of the displayed loss without making a claim about equality in the independent period-metric comparisons.

In particular \(a_\perp b_F\le\sigma_N^2\), so Section 6 gives

\[
c_F(t)\le\frac{M(t)}{m(t)}\frac{\sigma_N^2}{|u|^2}.
\]

## 8. The exact additional control radius in the same metric

Because \(q>1\), the highest-remainder coefficient of the constant is zero: \(\ell e_0=0\). Consequently \(e_0\) and \(f=G^{-1}\ell^*\) are \(G\)-orthogonal:

\[
e_0^*Gf=e_0^*\ell^*=\overline{\ell e_0}=0.
\]

Their squared lengths are the retained positive numbers \(a_0,b_0\). For \(R=e_0\ell\),

\[
R^{\dagger_G}=G^{-1}\ell^*e_0^*G=fe_0^*G.
\]

The exact relative-control change is

\[
X_t-X_0=tR+\bar tR^{\dagger_G}.
\]

On the original, unscaled ordered pair \(e_0,f\), its matrix is

\[
\begin{pmatrix}0&t b_0\\\bar t a_0&0\end{pmatrix},
\]

because \(Rf=b_0e_0\), \(Re_0=0\),
\(R^{\dagger_G}e_0=a_0f\), and
\(R^{\dagger_G}f=0\). On the \(G\)-orthogonal complement of their span, both terms vanish. Its nonzero-pair characteristic polynomial is
\(\lambda^2-|t|^2a_0b_0\). Self-adjointness in the same metric therefore gives

\[
\|X_t-X_0\|_G^2=|t|^2a_0b_0=|t|^2\sigma_N^2.
\]

This includes \(t=0\), when the whole change is zero. The special \(q=1\) formula from LC7 is not used here because a nonzero proper constituent already forces \(q>1\).

Combining this exact norm identity with Sections 6 and 7 proves the final displayed comparison:

\[
\boxed{
\partial_{\bar t}\partial_t\log\det H_F(t)
\le\frac{M(t)}{m(t)}
\frac{\|X_t-X_0\|_G^2}{|u|^2}.}
\]

Every factor is evaluated on the same original constituent, source metric, deformation, and period map. The proof does not substitute a period-coordinate norm for the original norm in its right side.

## 9. Scope and final determination

The proof supplies the exact maps relating the original constituent projection, its normal period derivative, and the companion control. Its two positivity inputs follow from the actual invariant ideal. Its metric comparison uses the two actual extremal eigenvalues, and its projection comparison retains the full nonnegative loss.

The source explicitly assumes \(0<p<q\); thus the strict-positivity claims do not inadvertently include the zero or full constituent. It holds \(G_N\) fixed while differentiating the periods at fixed \(u\ne0\). It retains the full parameter factor at \(t=0\), and uses no diagonalizability of the companion or constituent actions.

The current LC13–LC16 require no mathematical correction. This review verifies their finite conclusions at the pinned source edition, including their exact relation to SC12–SC16 and the original norm from LC4–LC6. It supplies no estimate uniform in \(q\), the packet, \(N\), \(u\), or \(t\), and the source correctly asserts none.

## 10. LC12a: the complete quadratic primitive on the original source

The later source addition promotes the finite Laplacian calculation to the original source comparison. Retain the original source term and primitive term of the tensor complex, denoting them here by \(\mathcal C_{\rm src}\) and \(\mathcal C_{\rm prim}\). The original maps have types

\[
d:\mathcal C_{\rm prim}\longrightarrow\mathcal C_{\rm src},
\qquad
j_E:\mathcal C_{\rm src}\longrightarrow E,
\qquad
r_N:E\longrightarrow\mathcal C_{\rm src},
\qquad
K_N^{\rm prim}:E\longrightarrow\mathcal C_{\rm prim}.
\]

The original Euler action is a chain action. On the source it is \(D^{(k)}\); on the primitive term write its degree-zero action as \(D_0:\mathcal C_{\rm prim}\to\mathcal C_{\rm prim}\). Its original identities are

\[
D^{(k)}d=dD_0,\qquad j_Ed=0,\qquad j_Er_N=I_E,
\qquad D^{(k)}r_N-r_NA=dK_N^{\rm prim}.
\]

These are the source and boundary identities retained in SC7–SC8, with the primitive-term component of the original Euler action named explicitly. All compositions act on the original admitted source and primitive domains.

At fixed \(t\), define the actual source action from SC8,

\[
D_t^{(k)}=D^{(k)}+t\,r_NRj_E.
\]

Its action on the original boundaries is unchanged, by an exact multiplication:

\[
D_t^{(k)}d
=D^{(k)}d+t\,r_NR(j_Ed)
=dD_0.
\]

Its action on the source lift is

\[
\begin{aligned}
D_t^{(k)}r_N
&=D^{(k)}r_N+t\,r_NR(j_Er_N)\\
&=r_NA+dK_N^{\rm prim}+t\,r_NR\\
&=r_NA_t+dK_N^{\rm prim}.
\end{aligned}
\]

Put \(K=K_N^{\rm prim}\) solely to display the square. The operator \(D_t^{(k)}\) acts on the original source variables; it is not the period derivative \(\partial_t\). The parameter \(t\) is fixed in this composition, and \(A_t:E\to E\) is a coefficient endomorphism. Therefore

\[
\begin{aligned}
(D_t^{(k)})^2r_N
&=D_t^{(k)}(r_NA_t+dK)\\
&=(D_t^{(k)}r_N)A_t+(D_t^{(k)}d)K\\
&=(r_NA_t+dK)A_t+dD_0K\\
&=r_NA_t^2+d(KA_t+D_0K).
\end{aligned}
\]

Every map inside the last parentheses has domain \(E\) and target \(\mathcal C_{\rm prim}\). Subtract the whole linear term

\[
kD_t^{(k)}r_N=kr_NA_t+kdK.
\]

Since \(L_t=A_t^2-kA_t\), the exact quadratic source comparison is

\[
\boxed{
\big((D_t^{(k)})^2-kD_t^{(k)}\big)r_N-r_NL_t
=d\big(D_0K_N^{\rm prim}+K_N^{\rm prim}A_t-kK_N^{\rm prim}\big).}
\]

This is LC12a with its original order and sign. In particular

\[
K_N^{\rm prim}A_t
=K_N^{\rm prim}A+tK_N^{\rm prim}R
\]

retains the full deformation contribution. There is no commutation assumption between \(A_t\) and the primitive map. The source equality is established before passing to the quotient. Applying \(j_E\) then kills its displayed boundary through \(j_Ed=0\), recovering the corresponding coefficient Laplacian relation. LC12a therefore provides the complete typed primitive for the same deformed action used in LC13–LC16.
