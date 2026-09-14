# Independent proof review of LC1–16, including LC12a

Review date: 13 September 2026.

Disposition: **accepted within the stated original reflection-stable source and period construction; no mathematical defect found in LC1–16 or LC12a.** This is a bounded proof review of the complete assigned TeX file. It is not an execution of numerical tests, Lean, a source edit, a PDF inspection, or a remote publication.

## Exact object, scope, and provenance

The complete file read is `work/period_laplacian_control_bridge_20260913.tex`.

Its SHA-256 is `84d884eeceae8ab339b78c29404d86798fcd04b6d40dde1abcff1cc7ed631231`.

Local dependency passages inspected:

1. `work/toda_cv_exact_bridge_20260912.tex`, through TVB.31, in particular the original pairing and reflection hypotheses, tensor primitive TVB.9, original Gram TVB.14, recurrence and rank-two calculation TVB.22–27, and determinant/minor identities TVB.28–30. SHA-256: `97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e`.
2. `work/sga_constituent_period_curvature_20260913.tex`, with particular attention to SC1–25: the original period equation, invertible period construction, actual source lift, invariant ideal, normal derivative, and curvature convention. SHA-256: `f7cbbb2da3a97722c9f9128602b4de64ad1ab9cfccdbb03e8ee9363321f7de63`.
3. `work/sga_trace_period_NOTE_corrected_20260913.tex`, original arithmetic construction and interfaces (5)–(11), to verify that the source jet map is on the stated test-function domain. SHA-256: `5c0e890a9370f4aeab646aa7c375f5924aec05b60e060f7ede914638d203b2bf`.

An independently delegated bounded algebraic crosscheck of LC13–16 returned acceptance of the projection types, repeated-factor ideal proof, both comparison inequalities, complex derivative signs, retained factor `|t|²`, and exact two-term loss. The calculations below also record those claims directly.

The original reflection-stable source matters for LC3. That identity is not being asserted for an arbitrary unrelated positive Gram or polynomial lacking the retained reflection construction. LC4 onward uses the explicitly fixed positive metric and finite-dimensional operators; the hypotheses inherited at each use remain the ones in the source.

## LC1–3: original control, spectrum, and every determinant boundary

Work in the original increasing-power coordinates on

\[
E=\mathbb C[S]/(\chi),\quad q=\deg\chi\ge1,\quad
A=M_S,\quad G=G_N>0,\quad N\ge q-1,\quad k\in\mathbb R.
\]

The inner product is conjugate-linear in its first argument:
\(\langle v,w\rangle_G=v^*Gw\). The coefficient functional is the literal row \(\ell[P]=[S^{q-1}]\operatorname{rem}_\chi P\); in particular it is nonzero because \(\ell[S^{q-1}]=1\). The column \(e_0=[1]\) is nonzero because a polynomial of degree zero is not in the ideal of a monic polynomial of positive degree.

For \(A_t=A+t e_0\ell\), the matrix
\(W_t=A_t^*G+GA_t-kG\) is Hermitian. Its relative endomorphism \(X_t=G^{-1}W_t\) has the exact property

\[
X_t^*G=W_tG^{-1}G=W_t=GX_t.
\]

Thus it is self-adjoint in this original metric. Its eigenvalues are real, its operator norm is the largest absolute eigenvalue, and the Rayleigh quotient therefore proves
\(-\|X_t\|_GG\preceq W_t\preceq\|X_t\|_GG\). No identification of a form with an endomorphism has omitted a factor of \(G^{-1}\).

Let \(u=b_N\), \(v=b_{N+1}\), \(w=\omega_N\), and \(w_+=\omega_{N+1}\). These symbols in this paragraph are only names for the original columns and positive norms, not replacements of their lengths or coordinates. The source recurrence used in TVB is

\[
S p_j=p_{j+1}+(k/2+i b_j^{\rm rec})p_j-\alpha_jp_{j-1},
\qquad \alpha_j=\omega_j/\omega_{j-1}.
\]

Applying its reduction to \(AK_N+K_NA^*-kK_N\), every adjacent interior pair has coefficient \(1/\omega_j-\alpha_{j+1}/\omega_{j+1}=0\), the real diagonal contribution is \(k-k=0\), and the remaining last pair gives

\[
AK_N+K_NA^*-kK_N=(vu^*+uv^*)/w.
\]

Because \(G=K_N^{-1}\), multiplication by \(G\) on both sides gives precisely

\[
W_0=G(vu^*+uv^*)G/w,\qquad
X_0=(vu^*+uv^*)G/w.
\]

Write \(a=u^*Gu\), \(d_+=v^*Gv\), and \(z_N=u^*Gv\). The original reflection proof TVB.25–26 retains the phase
\(z_N=i\omega_N\psi_N\), with \(\psi_N\in\mathbb R\). One can see that phase without changing any of these original scalar observations: the explicitly transported real-coordinate source columns satisfy \(Eb_j=i^jd_j\); the transformed Gram and \(d_j\) are real, so their original scalar product acquires the factor \(\overline{i^N}i^{N+1}=i\). Therefore

\[
\operatorname{Tr}X_0=(z_N+\overline{z_N})/w=0,
\]

and expansion of the original rank-one products gives

\[
\operatorname{Tr}(X_0^2)
=\frac{z_N^2+\overline{z_N}^{\,2}+2ad_+}{w^2}
=\frac{2(ad_+-|z_N|^2)}{w^2}.
\]

The range lies in \(\operatorname{span}\{u,v\}\), hence the rank is at most two. A self-adjoint rank-at-most-two endomorphism of trace zero either vanishes or has precisely two nonzero eigenvalues of opposite sign. In the latter case writing them \(\lambda,-\lambda\) in the squared-trace equation gives

\[
\|X_0\|_G^2=\lambda^2=(ad_+-|z_N|^2)/w^2.
\]

In the zero case the same equality follows from the same squared trace. This verifies the first equality of LC3, including possible column dependence and zero radius. For \(q=1\) the endomorphism is scalar and trace zero, hence \(X_0=0\); also \(ad_+=|z_N|^2\) identically for two columns in a one-dimensional space.

For the determinant equality, retain \(D_j=\det K_j\), with \(K_{-1}=0\) as a \(q\)-by-\(q\) matrix, and \(D_N>0\). Only \(K_N\) is inverted. The one-column and two-column determinant formulas yield

\[
\begin{aligned}
\frac{D_{N-1}}{D_N}&=1-\frac a w,\\
\frac{D_{N+1}}{D_N}&=1+\frac{d_+}{w_+},\\
\frac{\widetilde D_N}{D_N}
&=\left(1-\frac a w\right)\left(1+\frac{d_+}{w_+}\right)
+\frac{|z_N|^2}{ww_+}.
\end{aligned}
\]

The last plus sign is forced by the mixed negative and positive rank-one updates: their off-diagonal product has a negative sign, and the determinant subtracts that product. Subtracting these exact expressions in the original definition
\(\Delta_N=D_{N+1}+D_{N-1}-D_N-\widetilde D_N\) gives

\[
\frac{\Delta_N}{D_N}=\frac{ad_+-|z_N|^2}{ww_+}.
\]

Multiplication by the actual \(\alpha_{N+1}=w_+/w\) gives the second equality of LC3.

At \(N=q-1\), the columns \(b_0,\ldots,b_{q-2}\) are monic of distinct degrees \(0,\ldots,q-2\), hence independent. Thus \(K_{q-2}\) has rank \(q-1\) and determinant zero. The formulas just proved still invert only \(K_{q-1}\), which is positive because the first \(q\) monic columns form a triangular basis. In particular they entail \(a/\omega_{q-1}=1\) at this boundary without defining an inverse for \(K_{q-2}\). For \(q=1,N=0\), \(K_{-1}\) is the one-by-one zero matrix and its determinant is zero, not an empty determinant of value one.

The positive-minor proof is valid at the same boundary: determinant multilinearity of \(\sum_j b_jb_j^*/\omega_j\) gives the sum over increasing sets of \(q\) distinct column indices, with summand \(|\det[b_j]|^2/\prod_j\omega_j\). In the four determinants defining \(\Delta_N\), terms containing neither of \(N,N+1\) have coefficient \(1+1-1-1=0\), those containing exactly one have coefficient zero, and those containing both have coefficient one. Therefore for \(q\ge2\)

\[
\Delta_N=
\sum_{\substack{J\subseteq\{0,\ldots,N-1\}\\|J|=q-2}}
\frac{|\det[b_j]_{j\in J\cup\{N,N+1\}\text{ increasing}}|^2}
{\omega_N\omega_{N+1}\prod_{j\in J}\omega_j}\ge0.
\]

For \(q=2\), \(J\) can be the empty set and its denominator factor is the empty product one. For \(q=1\), no one-element column set contains both last indices, so \(\Delta_N=0\). All endpoint and repeated-factor cases remain covered.

## LC4–8: the exact companion radius and quadratic deformation

For \(R=e_0\ell\), the adjoint is
\(R^{\dagger_G}=G^{-1}R^*G=G^{-1}\ell^*e_0^*G\). The literal expansion gives

\[
X_t-X_0=tR+\bar t R^{\dagger_G}.
\]

If \(q>1\), \(\ell e_0=0\), so \(R^2=e_0(\ell e_0)\ell=0\). Define the original column and scalar observations

\[
f=G^{-1}\ell^*,\quad a_0=e_0^*Ge_0>0,\quad
b_0=\ell G^{-1}\ell^*>0.
\]

Here \(f^*Gf=b_0\) and \(e_0^*Gf=\overline{\ell e_0}=0\). The positive lengths and orthogonality prove independence. Direct application gives

\[
Re_0=0,\quad Rf=b_0e_0,\quad
R^{\dagger_G}e_0=a_0f,\quad R^{\dagger_G}f=0.
\]

Thus the matrix on the unchanged ordered columns \((e_0,f)\) is exactly

\[
\begin{pmatrix}0&t b_0\\\bar t a_0&0\end{pmatrix},
\]

with Gram \(\operatorname{diag}(a_0,b_0)\). On its \(G\)-orthogonal complement both functionals \(e_0^*G\) and \(f^*G=\ell\) vanish, so both rank-one terms vanish. The two-dimensional characteristic polynomial is \(x^2-|t|^2a_0b_0\), yielding the full eigenvalue list \(\pm|t|\sqrt{a_0b_0}\) and remaining zeros. For \(t=0\) the entire operator is zero. Self-adjointness in the unchanged metric proves

\[
\|X_t-X_0\|_G=|t|\sigma_N,\qquad \sigma_N=\sqrt{a_0b_0}.
\]

If \(q=1\), \(\ell e_0=1\) and \(R=I_E\), so
\(X_t-X_0=(t+\bar t)I_E\). Its exact norm is \(2|\operatorname{Re}t|\), including purely imaginary nonzero \(t\). This proves the separate scalar case in LC7.

The triangle inequality for the same operator norm gives exactly LC7, followed by the self-adjoint Rayleigh-quotient form inequalities proved above. It supplies an upper bound for \(\|X_t\|_G\); it makes no unsupported equality claim for the sum of the two norms.

Multiplication of the original noncommuting sum gives

\[
(A+tR)^2-k(A+tR)-(A^2-kA)
=t(AR+RA-kR)+t^2R^2.
\]

This proves LC8 with both cross terms, its original minus sign, and the scalar \(t^2I_E\) when \(q=1\).

## LC9–11: exact Laplacian identities and the whole numerical range

Write \(B_t=A_t-kI/2\). Since \(k\) is real, \(W_t=B_t^*G+GB_t\) and \(L_t=B_t^2-k^2I/4\). For the first LC9 identity, expansion gives

\[
\begin{aligned}
A_t^*W_t-W_tA_t
&=(A_t^*)^2G+A_t^*GA_t-kA_t^*G\\
&\quad-A_t^*GA_t-GA_t^2+kGA_t\\
&=L_t^*G-GL_t.
\end{aligned}
\]

For the second,

\[
W_tB_t-B_t^*GB_t-k^2G/4
=GB_t^2-k^2G/4=GL_t.
\]

Neither calculation assumes \(G\), \(A_t\), \(W_t\), or their adjoints commute.

For each original \(v\ne0\), let \(z,r,a,b\) have precisely the definitions LC10 and let \(e=E_N(t)\ge0\). Cauchy–Schwarz and the definition of operator norm give

\[
|a+ib|=
\frac{|\langle v,X_tB_tv\rangle_G|}{\|v\|_G^2}
\le\frac{\|X_t\|_G\|B_tv\|_G}{\|v\|_G}
\le er.
\]

The second LC9 identity evaluated on \(v\) gives
\(\operatorname{Re}z=a-r^2-k^2/4\) and \(\operatorname{Im}z=b\). Therefore

\[
\operatorname{Re}z\le er-r^2-k^2/4
=\frac{e^2-k^2}{4}-(r-e/2)^2
\le\frac{e^2-k^2}{4}.
\]

For the second inequality, direct expansion on the original scalars gives

\[
\begin{aligned}
e^2\left(\frac{e^2-k^2}{4}-\operatorname{Re}z\right)
-(\operatorname{Im}z)^2
&=e^4/4-e^2a+e^2r^2-b^2\\
&=(a-e^2/2)^2+(e^2r^2-a^2-b^2)\ge0.
\end{aligned}
\]

The second term is nonnegative by the previous norm inequality. This proves both assertions LC11. In the special case \(e=0\), it yields \(a=b=0\), \(\operatorname{Im}z=0\), and \(\operatorname{Re}z=-r^2-k^2/4\le-k^2/4\); the separate real-part inequality correctly retains this ray. There was no division by \(e\).

If \(L_tv=\lambda v\) for an eigenvector \(v\ne0\), the displayed quotient equals \(\lambda\), proving spectral inclusion. The proof uses no diagonalizability assertion and retains the larger set of quotients for all nonzero original vectors.

## LC12: period congruence and its exact form-to-operator map

The retained period construction gives invertible \(\Pi(u,t)\) for fixed \(u\ne0\). With the exact definitions LC12, direct multiplication proves

\[
\widetilde A_t^*\widetilde G+\widetilde G\widetilde A_t-k\widetilde G
=\Pi^{-*}(A_t^*G+GA_t-kG)\Pi^{-1}=\widetilde W_t,
\]

and \(\widetilde A_t^2-k\widetilde A_t=\Pi L_t\Pi^{-1}=\widetilde L_t\). The relative control transports by similarity:

\[
\widetilde X_t:=\widetilde G^{-1}\widetilde W_t
=\Pi X_t\Pi^{-1},\qquad
\widetilde B_t=\Pi B_t\Pi^{-1}.
\]

For the literal corresponding vector \(x=\Pi v\),

\[
\begin{aligned}
x^*\widetilde Gx&=v^*Gv,\\
x^*\widetilde G\widetilde L_tx&=v^*GL_tv,\\
x^*\widetilde W_tx&=v^*W_tv,\\
\|\widetilde B_tx\|_{\widetilde G}&=\|B_tv\|_G,\\
\langle x,\widetilde X_t\widetilde B_tx\rangle_{\widetilde G}
&=\langle v,X_tB_tv\rangle_G.
\end{aligned}
\]

Surjectivity of \(\Pi\) makes these equalities identities of the complete quotient sets and operator norms, not merely inclusions. Furthermore

\[
\widetilde L_t^*\widetilde G-\widetilde G\widetilde L_t
=\Pi^{-*}(L_t^*G-GL_t)\Pi^{-1}
=\widetilde A_t^*\widetilde W_t-\widetilde W_t\widetilde A_t.
\]

The fixed action and companion term remain
\(\Pi A_t\Pi^{-1}=\Pi A\Pi^{-1}+t\Pi R\Pi^{-1}\). These statements concern the transported metric \(\widetilde G\); the later constituent section explicitly uses the different specified period-coordinate metric \(I_q\) and supplies the comparison between them.

## LC12a: source-domain types, differential sign, and complete primitive

The original tensor complex has factors \(V\xrightarrow{\Theta}\mathscr B\), with \(V\) in degree zero and \(\mathscr B\) in degree one. Its primitive term \(\mathcal C_{\rm prim}\) is the degree \(k-1\) term, and its top term is the degree \(k\) tensor source. The Euler operator is degree zero: its restriction \(D_0\) to \(\mathcal C_{\rm prim}\) and its top restriction \(D^{(k)}\) preserve these respective domains. TVB.9 gives the actual primitive with the sign \((-1)^{i-1}\) at its sole degree-zero factor. Its differential carries the same sign from the preceding \(i-1\) degree-one factors, so the product of these signs is positive and gives the original relation \(\chi(S)=\sum_i h(s_i)Q_i\).

Euler differentiation preserves the original test-function conditions and commutes with \(\Theta\). On a homogeneous simple tensor, the differential at factor \(i\) is multiplied by \((-1)^{\sum_{j<i}\deg x_j}\); the Euler operator changes none of those degrees. The same-factor commutator vanishes by \(D\Theta=\Theta D\), and different-factor operations commute. Thus every term agrees with its counterpart with the same sign, proving the actual typed identity

\[
D^{(k)}d=dD_0:
\mathcal C_{\rm prim}\longrightarrow\mathcal C^k.
\]

The jet observation annihilates the original boundaries, \(j_Ed=0\), and its stated source domain includes the original Euler-stable test-function domain; it is not restricted to the finite-dimensional image of one lift \(r_N\). Consequently applying the degree-zero source action a second time is defined on the actual images appearing here. The finite-rank term takes its values in that same domain via \(r_N:E\to\mathcal C^k\).

Let \(K=K_N^{\rm prim}:E\to\mathcal C_{\rm prim}\). The original relations are

\[
j_Er_N=I_E,\quad
j_ED^{(k)}=Aj_E,\quad
D^{(k)}r_N-r_NA=dK.
\]

For \(D_t^{(k)}=D^{(k)}+t r_NRj_E\), insertion of \(j_Er_N=I_E\) proves

\[
D_t^{(k)}r_N=r_N(A+tR)+dK=r_NA_t+dK.
\]

Also, insertion of \(j_Ed=0\) gives
\(D_t^{(k)}d=D^{(k)}d+t r_NRj_Ed=dD_0\).
Now both compositions in the square are fully typed, and direct expansion gives

\[
\begin{aligned}
(D_t^{(k)})^2r_N
&=D_t^{(k)}(r_NA_t)+D_t^{(k)}dK\\
&=(r_NA_t+dK)A_t+dD_0K\\
&=r_NA_t^2+d(KA_t+D_0K).
\end{aligned}
\]

Subtracting exactly \(kD_t^{(k)}r_N=kr_NA_t+kdK\) gives

\[
\bigl((D_t^{(k)})^2-kD_t^{(k)}\bigr)r_N-r_NL_t
=d(D_0K+KA_t-kK).
\]

This is LC12a. Each of \(D_0K\), \(KA_t\), and \(kK\) maps \(E\) into \(\mathcal C_{\rm prim}\). The expansion of \(KA_t\) includes \(tKR\), so no deformation contribution has been dropped. The primitive is the original \(K\), with its original differential and source action; the calculation requires neither a new primitive choice nor a change of coordinates. At \(q=1\), the quadratic companion term in \(L_t\) remains present inside \(A_t^2\); the proof did not use \(R^2=0\).

## LC13: projection types and strict positivity for every proper constituent

Let \(I:F\hookrightarrow E\) have matrix size \(q\times p\), with \(0<p<q\) and \(AI=IA_F\). Set \(G_F=I^*GI\), \(P_F=IG_F^{-1}I^*G\), and \(L=\ell I\). Injectivity gives \(G_F>0\). Direct multiplication gives

\[
P_F^2=P_F,\quad P_FI=I,\quad P_F^*G=GP_F.
\]

Since its image is contained in \(I(F)\) and it fixes \(I(F)\), this is exactly the original \(G\)-orthogonal projection. Orthogonality therefore gives

\[
\begin{aligned}
a_\perp&=e_0^*G(1-P_F)e_0=\|(1-P_F)e_0\|_G^2,\\
\|P_Ff\|_G^2
&=f^*GP_Ff
=\ell IG_F^{-1}I^*\ell^*=b_F.
\end{aligned}
\]

The image \(I(F)\) is invariant under every polynomial in \(A\), hence under multiplication by every element of \(E\). Thus it is an ideal. Its inverse image in \(\mathbb C[S]\) is an ideal containing \((\chi)\), so it is generated by a unique monic divisor \(g\) of \(\chi\). Write \(\chi=gh\). The map

\[
\mathbb C[S]/(h)\longrightarrow I(F),\qquad[a]_h\longmapsto[ga]_\chi
\]

is well-defined because \(g(ha)=\chi a\), onto by the ideal description, and injective because \(gh\mid ga\) implies \(h\mid a\) in the polynomial domain. Its dimensions give \(\deg h=p\), and its increasing-power basis gives the original image basis \([g],[Sg],\ldots,[S^{p-1}g]\). Since \(g\) is monic of degree \(q-p\), the last column is monic of degree \(q-1\) and is unchanged by remainder reduction. Applying \(\ell\) gives one, so \(L\ne0\) and \(b_F>0\) by positivity of \(G_F^{-1}\).

If \(e_0\) belonged to the ideal \(I(F)\), multiplication by every element would put all of \(E\) in it, contradicting \(p<q\). Therefore \((1-P_F)e_0\ne0\), proving \(a_\perp>0\). No step removes or weakens any repeated factor of \(g\), \(h\), or \(\chi\).

## LC14: the original metric compared with the coordinate period metric

Put \(Q(t)=\Pi(t)^*\Pi(t)>0\). The comparison endomorphism \(B(t)=G^{-1}Q(t)\) satisfies

\[
B(t)^*G=Q(t)=GB(t),\qquad
\langle v,B(t)v\rangle_G=\|\Pi(t)v\|_{I_q}^2>0\quad(v\ne0).
\]

The finite spectral theorem for this same \(G\)-inner product gives positive finite extremal eigenvalues \(m(t),M(t)\). Expansion in a \(G\)-orthogonal eigenbasis, retaining all original eigenvalues, proves
\(m(t)G\preceq Q(t)\preceq M(t)G\). No replacement of either metric is used to define the observations below.

For \(Y=\Pi I\), \(H_F=Y^*Y>0\), and \(P^{\rm per}=YH_F^{-1}Y^*\), the same multiplication as above, now in \(I_q\), makes \(P^{\rm per}\) the orthogonal projection onto \(Y(F)\). Consequently its residual \(z=(1-P^{\rm per})\Pi e_0\) satisfies

\[
\|z\|_{I_q}^2=\min_{x\in F}\|\Pi(e_0-Ix)\|_{I_q}^2.
\]

The original-metric squared norm has the explicit completion

\[
\|e_0-Ix\|_G^2
=a_\perp+(x-x_0)^*G_F(x-x_0),\qquad
x_0=G_F^{-1}I^*Ge_0.
\]

For every \(x\) the lower comparison bound is at least \(m(t)a_\perp\); taking its minimum gives the first lower bound. Evaluating the upper comparison at \(x_0\) gives the first upper bound. Hence

\[
m(t)a_\perp\le\|z\|_{I_q}^2\le M(t)a_\perp.
\]

Compression by \(I\) gives
\(m(t)G_F\preceq H_F\preceq M(t)G_F\). To verify inverse order with all scalar factors, for positive \(T\) and arbitrary column \(w\), the exact square completion is

\[
2\operatorname{Re}(w^*x)-x^*Tx
=w^*T^{-1}w-(x-T^{-1}w)^*T(x-T^{-1}w).
\]

Thus its maximum over \(x\) is \(w^*T^{-1}w\), and a larger positive \(T\) gives a smaller maximum. Applied to the three displayed forms this proves

\[
M(t)^{-1}G_F^{-1}\preceq H_F^{-1}\preceq m(t)^{-1}G_F^{-1}.
\]

Evaluating on the unchanged column \(w=L^*\) proves
\(b_F/M(t)\le LH_F^{-1}L^*\le b_F/m(t)\). This proves both LC14 pairs without a commutation hypothesis.

## LC15: holomorphic derivative, retained sign, and exact curvature

The original SC4 period equation is \(\Pi'=-\Pi(A+tR)/u\). Its sign is consistent with differentiating the exponential \(e^{\Phi_t/u}\), because \(\partial_t\Phi_t=-S\). For the last column, integration by parts gives the reduction \(S^q\equiv-\sum_{a<q}c_aS^a+t\), so its companion entry is \(+tR\); the two signs are both retained. Hence \(AI=IA_F\) and \(RI=e_0L\) give

\[
Y'=-YA_F/u-t\Pi e_0L/u,\qquad
(1-P^{\rm per})Y'=-tzL/u.
\]

With \(H=H_F=Y^*Y\), holomorphy gives

\[
\partial_tH=Y^*Y',\quad
\partial_{\bar t}H=Y'^*Y,\quad
\partial_{\bar t}\partial_tH=Y'^*Y',\quad
\partial_{\bar t}H^{-1}=-H^{-1}Y'^*YH^{-1}.
\]

The positive determinant uses the real logarithm. Differentiating its determinant derivative and retaining product order proves

\[
\begin{aligned}
\partial_{\bar t}\partial_t\log\det H
&=\operatorname{Tr}\bigl(H^{-1}Y'^*Y'
-H^{-1}Y'^*YH^{-1}Y^*Y'\bigr)\\
&=\operatorname{Tr}\bigl(H^{-1}Y'^*(1-P^{\rm per})Y'\bigr).
\end{aligned}
\]

Because \(1-P^{\rm per}\) is self-adjoint and idempotent, substitution of the exact normal derivative gives

\[
Y'^*(1-P^{\rm per})Y'
=\frac{|t|^2\|z\|_{I_q}^2}{|u|^2}L^*L.
\]

Taking the trace yields

\[
\partial_{\bar t}\partial_t\log\det H_F
=|t|^2c_F(t),\qquad
c_F(t)=\frac{\|z\|_{I_q}^2}{|u|^2}LH_F^{-1}L^*.
\]

The negative sign in each normal factor multiplies its conjugate, producing the displayed positive expression. The nonzero denominator is the original \(|u|^2\), and the derivative convention is the original Wirtinger one; there is no additional real-Laplacian factor of four in this displayed mixed derivative.

Both factors in LC14 are strictly positive. Multiplying their two lower bounds, and separately their two upper bounds, gives exactly

\[
\frac{m(t)}{M(t)}\frac{a_\perp b_F}{|u|^2}
\le c_F(t)\le
\frac{M(t)}{m(t)}\frac{a_\perp b_F}{|u|^2}.
\]

At \(t=0\), \(c_F(0)>0\), while the actual curvature is zero because its expression retains the factor \(|t|^2\). Thus the proof does not confuse a positive coefficient with a nonzero curvature at the stationary parameter.

## LC16: exact loss and final radius comparison

The original projection gives two orthogonal decompositions, with no terms omitted:

\[
a_0=\|P_Fe_0\|_G^2+a_\perp,\qquad
b_0=b_F+\|(1-P_F)f\|_G^2.
\]

Multiplying the first equality by the whole original \(b_0\) and subtracting \(a_\perp b_F\) gives

\[
\begin{aligned}
\sigma_N^2-a_\perp b_F
&=\|P_Fe_0\|_G^2b_0+a_\perp(b_0-b_F)\\
&=\|P_Fe_0\|_G^2b_0
+a_\perp\|(1-P_F)G^{-1}\ell^*\|_G^2\ge0.
\end{aligned}
\]

This verifies the stated exact two-term loss; the first term retains the full \(b_0\), including its complement contribution. Combining it with LC15 gives

\[
c_F(t)\le\frac{M(t)}{m(t)}\frac{\sigma_N^2}{|u|^2}.
\]

Since a proper nonzero constituent has \(q>1\), the applicable exact companion norm is precisely
\(\|X_t-X_0\|_G^2=|t|^2\sigma_N^2\). Multiplication by the retained \(|t|^2\) proves the final assertion

\[
\partial_{\bar t}\partial_t\log\det H_F(t)
\le\frac{M(t)}{m(t)}\frac{\|X_t-X_0\|_G^2}{|u|^2}.
\]

Both sides vanish at \(t=0\). The cases \(q=1\), \(F=0\), and \(F=E\) are not improperly included in the strictly positive proper-constituent statement: LC13 explicitly assumes \(0<p<q\), and the earlier scalar companion calculation handles \(q=1\).

## Review closure

All original metric factors, conjugations, source types, polynomial cross terms, reflection phase, determinant signs, and stationary-parameter factors needed for LC1–16 and LC12a have been checked in the calculations above. No claim of a uniform bound on \(\epsilon_N\), \(\sigma_N\), or \(M(t)/m(t)\) has been added. No concrete defect was found. The assigned mathematical source was not edited, and no numerical, Lean, or remote action was performed.
