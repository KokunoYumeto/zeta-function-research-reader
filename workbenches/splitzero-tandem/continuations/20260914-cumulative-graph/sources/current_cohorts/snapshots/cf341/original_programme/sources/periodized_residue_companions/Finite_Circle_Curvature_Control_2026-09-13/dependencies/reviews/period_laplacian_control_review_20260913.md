# Complete independent review of the period–Laplacian control bridge

Reviewed on 13 September 2026. The complete LC1–LC16 source was read, together with the actual Toda source TVB.22–TVB.34 and its first-degree and empty-quotient calculations, and the complete accepted SC1–SC37 source. No numerical tests, mathematical checker, Lean, or PDF build was run for this review. Every claim below is proved directly in the original coordinates and positive metric.

The reviewed sources are:

| Source | SHA-256 |
|---|---|
| `work/period_laplacian_control_bridge_20260913.tex`, complete LC1–LC16 and LC12a edition | `84d884eeceae8ab339b78c29404d86798fcd04b6d40dde1abcff1cc7ed631231` |
| The preceding LC source, retained as `work/period_laplacian_control_before_local_typing_20260913.tex` | `0799f1fbc266b25e11fec456c1d66618bdae365fe17060c9f69393a9b11c900c` |
| `output/split_zero_rh_tandem_2026-09-12/tex/toda_cv_exact_bridge.tex` | `c9629b11d4b4a173dd52bdf75fafb437883a85aba05e598c637f390386d45512` |
| `work/sga_constituent_period_curvature_20260913.tex` | `f7cbbb2da3a97722c9f9128602b4de64ad1ab9cfccdbb03e8ee9363321f7de63` |

Verdict: LC1–LC16 are correct. The original twelve formulae, constants, signs and orientations required no changes. After notifying the coordinating author, the reviewer added the explicit parameter range, integer admission range, full source-column kernel definition, empty kernel convention and omitted-column kernel. These additions make the boundary determinant calculation self-contained; the preceding source bytes are retained. The new additional radius is an exact norm. The sum with the original radius is a proved upper bound, with equality not asserted. Its numerical-range consequence applies with the actual supplied finite control, without a missing smallness premise. The coordinating author's subsequent exact constituent comparison was appended as LC13–LC16 with its complete proof; Sections 10–14 below check every factor and its domain.

## 1. Original spaces, adjoints and companion action

Let the original monic relation be

\[
\chi(S)=S^q+\sum_{a=0}^{q-1}c_aS^a,
\qquad q\ge1,
\]

and retain the ordered coefficient frame \(1,S,\ldots,S^{q-1}\) of
\(E=\mathbb C[S]/(\chi)\). Its dimension is \(q\), including the full degree of every repeated factor. The functional

\[
\ell:E\longrightarrow\mathbb C,
\qquad [P]\longmapsto[S^{q-1}]\operatorname{rem}_{\chi}P
\]

is well-defined because monic remainder is unique. It is nonzero: its value at \([S^{q-1}]\) is one. The column \(e_0=[1]\) is nonzero because \(q\ge1\). Thus

\[
R=e_0\ell:E\longrightarrow E
\]

has image exactly \(\mathbb C e_0\), kernel exactly \(\ker\ell\), and rank one. In the original increasing-power frame, multiplication by \(S\) has last column \((-c_0,\ldots,-c_{q-1})^T\). Adding \(tR\), with \(t\in\mathbb C\), changes only its first entry to \(-c_0+t\). Consequently \(A_t=A+tR\) is exactly multiplication by \(S\) on the coefficient frame of \(\mathbb C[S]/(\chi-t)\), as in SC1–SC4. This identifies the actual companion deformation and its parameter sign.

Fix the original admitted integer degree \(N\ge q-1\), its positive quotient Gram \(G=G_N\), and real \(k\). The metric is conjugate-linear in the first argument:

\[
\langle v,w\rangle_G=v^*Gw.
\]

For any endomorphism \(T\) of this fixed coefficient space, its metric adjoint is \(T^{\dagger_G}=G^{-1}T^*G\), since
\(\langle Tv,w\rangle_G=v^*T^*Gw=\langle v,T^{\dagger_G}w\rangle_G\).
The displayed control and Laplacian are therefore

\[
W_t=A_t^*G+GA_t-kG=W_t^*,\qquad
X_t=G^{-1}W_t=A_t^{\dagger_G}+A_t-kI,
\]
\[
L_t=A_t^2-kA_t,
\qquad B_t=A_t-\frac{k}{2}I.
\]

The identity \(X_t^*G=GX_t\) proves its self-adjointness for this actual metric. Since the space is finite and the metric is positive, its operator norm exists and equals its largest absolute eigenvalue. Thus \(\epsilon_N=\|X_0\|_G\) is an actual finite scalar and

\[
-\epsilon_NG\preceq W_0\preceq\epsilon_NG.
\]

This definition makes sense for every declared \(k\) and companion. The more specific reflection-stable arithmetic calculation in the next section evaluates the same scalar for its stated original source. No reflection premise is needed for the later elementary deformation and numerical-range identities when \(\epsilon_N\) is taken from its definition.

## 2. LC3 and the complete Toda determinant calculation

For the reflection-stable original source, let \(p_j\) denote its monic orthogonal polynomials, \(\omega_j>0\) their full squared norms, and \(b_j=[p_j]_\chi\) their original remainder columns. Retain

\[
K_j=\sum_{r=0}^{j}\frac{b_rb_r^*}{\omega_r},\qquad j\ge-1,
\qquad K_{-1}=0,
\qquad D_j=\det K_j.
\]

The first \(q\) columns form a triangular matrix with diagonal one, so \(K_N>0\) at the admitted degree and \(G=K_N^{-1}\). Put

\[
x=b_N,\quad y=b_{N+1},\quad \omega=\omega_N,
\quad \nu=\omega_{N+1},
\quad a=x^*Gx,\quad d_+=y^*Gy,\quad z=x^*Gy.
\]

The source recurrence and telescoping in TVB.22–TVB.27 give exactly

\[
W_0=\frac{G(yx^*+xy^*)G}{\omega},
\qquad
X_0=\frac{(yx^*+xy^*)G}{\omega}.
\]

Reflection preserves the annihilator ideal and yields the real monic polynomial \(i^{-q}\chi(k/2+iu)\). The complete coefficient transport in TVB.25–TVB.26 retains the phase

\[
z=b_N^*Gb_{N+1}=i\omega_N\psi_N,
\qquad \psi_N\in\mathbb R.
\]

In particular \(\operatorname{Tr}X_0=(z+\bar z)/\omega=0\). The rank is at most two. Directly composing the two rank-one factors and taking their traces gives

\[
\operatorname{Tr}(X_0^2)
=\frac{z^2+\bar z^2+2ad_+}{\omega^2}
=\frac{2(ad_+-|z|^2)}{\omega^2}.
\]

Self-adjointness and trace zero make its possible nonzero eigenvalues a pair \(\epsilon_N,-\epsilon_N\). If fewer than two are nonzero, they are all zero. Thus

\[
\epsilon_N^2=\frac{ad_+-|z|^2}{\omega_N^2}.
\]

Its radicand is nonnegative by Cauchy–Schwarz for the same \(G\). At \(q=1\), the single eigenvalue has zero trace and the same formula gives zero, since \(ad_+=|z|^2\) in a one-dimensional metric space.

Define the actual omitted-column matrix

\[
\widetilde K_N
=K_{N-1}+\frac{yy^*}{\nu}
=K_N-\frac{xx^*}{\omega}+\frac{yy^*}{\nu},
\qquad \widetilde D_N=\det\widetilde K_N.
\]

No inverse of \(K_{N-1}\) or \(\widetilde K_N\) is used. To prove the required determinant identity, block elimination of

\[
\begin{pmatrix}K&U\\-V^*&I\end{pmatrix}
\]

using its two diagonal blocks gives
\(\det(K+UV^*)=\det K\det(I+V^*K^{-1}U)\). Apply this only to the invertible \(K=K_N\), with \(U=[x,y]\) and rows \(V^*=(-x^*/\omega,y^*/\nu)^T\). The two-dimensional matrix is

\[
\begin{pmatrix}
1-a/\omega&-z/\omega\\
\bar z/\nu&1+d_+/\nu
\end{pmatrix}.
\]

Hence

\[
\frac{\widetilde D_N}{D_N}
=\left(1-\frac a\omega\right)
 \left(1+\frac{d_+}\nu\right)+\frac{|z|^2}{\omega\nu}.
\]

The individual rank-one determinant formula likewise gives

\[
\frac{D_{N-1}}{D_N}=1-\frac a\omega,
\qquad
\frac{D_{N+1}}{D_N}=1+\frac{d_+}\nu.
\]

Subtract the four terms in their original order:

\[
\begin{aligned}
\frac{\Delta_N}{D_N}
&=\frac{D_{N+1}+D_{N-1}-D_N-\widetilde D_N}{D_N}\\
&=\frac{ad_+-|z|^2}{\omega\nu}.
\end{aligned}
\]

Multiplication by \(\alpha_{N+1}=\nu/\omega\) proves exactly

\[
\epsilon_N^2=\alpha_{N+1}\frac{\Delta_N}{D_N}.
\]

This identity includes \(N=q-1\): the first \(q-1\) columns have rank \(q-1\), so \(D_{q-2}=0\). At \(q=1,N=0\), this is the declared \(1\times1\) zero matrix \(K_{-1}\), whose determinant is zero. The denominator \(D_{q-1}>0\) remains valid. Neither a quotient volume \(V_{q-2}\) nor a singular inverse is introduced.

The source-minor identity also keeps its full interpretation. Cauchy–Binet on each of the four column sets cancels exactly the selections containing neither or only one of \(N,N+1\). For \(q\ge2\) the remainder is

\[
\Delta_N=
\sum_{\substack{I\subseteq\{0,\ldots,N-1\}\\ |I|=q-2}}
\frac{|\det[b_j]_{j\in I\cup\{N,N+1\}\text{ increasing}}|^2}
{\omega_N\omega_{N+1}\prod_{i\in I}\omega_i}.
\]

At \(q=1\), every selection has one column and cancels, so \(\Delta_N=0\). This is the exact positive source-minor sum in TVB.30, with all original norms and column orientations retained.

## 3. LC4–LC6: the exact additional radius

The coordinate adjoint is \(R^*=\ell^*e_0^*\), and therefore

\[
R^{\dagger_G}=G^{-1}\ell^*e_0^*G.
\]

Substitution into the control gives

\[
X_t-X_0=tR+\bar tR^{\dagger_G}.
\]

For \(q>1\), the coefficient of \(S^{q-1}\) in the constant polynomial is zero, so \(\ell e_0=0\) and \(R^2=e_0(\ell e_0)\ell=0\). Put

\[
f=G^{-1}\ell^*,\qquad a_0=e_0^*Ge_0>0,
\qquad b_0=\ell G^{-1}\ell^*>0.
\]

Both strict signs follow from positive definiteness and the nonzero column and functional. Moreover

\[
\langle e_0,f\rangle_G=e_0^*\ell^*=\overline{\ell e_0}=0,
\quad \langle f,f\rangle_G=b_0,
\quad \langle f,v\rangle_G=\ell v.
\]

The two original unscaled columns are independent and have Gram \(\operatorname{diag}(a_0,b_0)\). Their images are

\[
Re_0=0,\quad Rf=b_0e_0,
\qquad R^{\dagger_G}e_0=a_0f,\quad R^{\dagger_G}f=0.
\]

Thus the added self-adjoint map, restricted to their span and expressed in that same ordered frame, is

\[
\begin{pmatrix}0&t b_0\\\bar t a_0&0\end{pmatrix}.
\]

The matrix is self-adjoint for \(\operatorname{diag}(a_0,b_0)\): multiplying it on the left by that Gram gives mutually conjugate off-diagonal entries. A vector in the \(G\)-orthogonal complement of both \(e_0\) and \(f\) is killed by \(R\) and by its metric adjoint, using their displayed rank-one formulas. The characteristic polynomial on the two-dimensional span is \(x^2-|t|^2a_0b_0\), so the eigenvalues there are exactly

\[
|t|\sqrt{a_0b_0},\qquad -|t|\sqrt{a_0b_0}.
\]

All \(q-2\) remaining eigenvalues are zero. At \(t=0\), all eigenvalues are zero as well. The operator norm of this self-adjoint map in the original metric is consequently exactly

\[
\|X_t-X_0\|_G=|t|\sigma_N,
\qquad \sigma_N=\sqrt{(e_0^*Ge_0)(\ell G^{-1}\ell^*)}.
\]

No unit-vector choice, source-mass rescaling or replacement of the Gram was used.

For \(q=1\), \(\ell e_0=1\) and \(R=I_E\). It follows directly that

\[
X_t-X_0=2\operatorname{Re}(t)I_E,
\qquad \|X_t-X_0\|_G=2|\operatorname{Re}t|.
\]

In particular a purely imaginary scalar deformation contributes zero to this relative self-adjoint control, exactly as the written scalar case states. The nilpotent calculation from \(q>1\) is not used in this case.

## 4. LC7–LC8: supplied control and the full Laplacian change

The operator triangle inequality in the same norm gives

\[
\|X_t\|_G\le E_N(t):=
\epsilon_N+
\begin{cases}
|t|\sigma_N,&q>1,\\
2|\operatorname{Re}t|,&q=1.
\end{cases}
\]

For every vector, Cauchy–Schwarz therefore gives
\(|v^*W_tv|\le E_N(t)v^*Gv\), equivalent to
\(-E_N(t)G\preceq W_t\preceq E_N(t)G\). Every scalar in this bound has been explicitly defined from the original finite matrices and parameter. Equality in the triangle inequality is unnecessary and is not asserted.

Direct expansion in the fixed coefficient space gives

\[
(A+tR)^2-k(A+tR)-(A^2-kA)
=t(AR+RA-kR)+t^2R^2.
\]

Thus the quadratic term is zero for \(q>1\), and is exactly \(t^2I_E\) for \(q=1\). The two linear products remain separately in their original order; no commutation assumption was inserted.

## 5. LC9: the adjoint defect and the quadratic identity

For real \(k\), expansion gives

\[
\begin{aligned}
A_t^*W_t-W_tA_t
&=(A_t^*)^2G-kA_t^*G-GA_t^2+kGA_t\\
&=L_t^*G-GL_t.
\end{aligned}
\]

The two copies of \(A_t^*GA_t\) cancel with their original opposite signs. Also

\[
W_t=B_t^*G+GB_t,
\qquad L_t=B_t^2-\frac{k^2}{4}I,
\]

so

\[
W_tB_t-B_t^*GB_t-\frac{k^2}{4}G
=GB_t^2-\frac{k^2}{4}G=GL_t.
\]

These identities hold for the actual complex parameter and arbitrary original positive Gram. They require neither normality of \(A_t\) nor commutation of \(W_t\) and \(A_t\).

## 6. LC10–LC11: the complete numerical-range parabola

For every unchanged nonzero \(v\in E\), define

\[
z=\frac{v^*GL_tv}{v^*Gv},\qquad
r=\frac{\|B_tv\|_G}{\|v\|_G},\qquad
a+ib=\frac{\langle v,X_tB_tv\rangle_G}{\|v\|_G^2},
\quad a,b\in\mathbb R.
\]

These are homogeneous observations of the original vector; the proof does not replace that vector by a different representative. Put \(e=E_N(t)\ge0\). Then

\[
|\langle v,X_tB_tv\rangle_G|
\le\|v\|_G\,\|X_tB_tv\|_G
\le e\|v\|_G\,\|B_tv\|_G,
\]

and hence \(a^2+b^2\le e^2r^2\). The second identity in Section 5 gives

\[
\operatorname{Re}z=a-r^2-\frac{k^2}{4},
\qquad \operatorname{Im}z=b.
\]

Since \(a\le er\), completing the real square gives

\[
\operatorname{Re}z
\le er-r^2-\frac{k^2}{4}
=\frac{e^2-k^2}{4}-(r-e/2)^2
\le\frac{e^2-k^2}{4}.
\]

For the second inequality, retain all terms and expand exactly:

\[
\begin{aligned}
e^2\left(\frac{e^2-k^2}{4}-\operatorname{Re}z\right)
-(\operatorname{Im}z)^2
&=\frac{e^4}{4}-e^2a+e^2r^2-b^2\\
&=(a-e^2/2)^2+(e^2r^2-a^2-b^2)\ge0.
\end{aligned}
\]

This proves both original inequalities in LC11, with the factor \(1/4\) and the sign of \(-k^2\) preserved. If \(e=0\), the initial bound forces \(a=b=0\), so \(z=-r^2-k^2/4\) is real and satisfies the same two statements. No division by \(e\) occurs.

If \(\lambda\) is an eigenvalue of \(L_t\), its nonzero eigenvector satisfies \(z=\lambda\) in this metric quotient, since \(GL_tv=\lambda Gv\). Every eigenvalue is therefore included. This argument retains possible nondiagonalizable generalized blocks; it does not require an eigenbasis or alter algebraic multiplicities.

The excluded \(q=0\) case is already excluded explicitly by LC1. On the actual empty quotient, every endomorphism is the unique zero map and its numerical range, defined by nonzero vectors, is empty. The coefficient functional selecting \(S^{q-1}\) is not invoked there. Thus no positivity assertion about \(a_0,b_0\), no two-dimensional frame, and no nonzero eigenvector claim is silently transferred to the empty quotient.

## 7. LC12 and the complete period metric transport

SC1–SC6 retain \(u\in\mathbb C^*\), one fixed argument of \(u\), the potential \(\Phi_t\), the original rays and their signed differences. The actual matrix has rows

\[
\Pi_{jb}(u,t)=\int_{\Gamma_j}e^{\Phi_t(S)/u}S^b\,dS,
\qquad 1\le j\le q,\quad0\le b<q.
\]

The accepted full determinant identity is

\[
\det\Pi(u,t)=\det\Pi_{\rm mon}(u)
\exp\left(\frac{\operatorname{Tr}\Phi_t(A_t)}u\right),
\qquad |\det\Pi_{\rm mon}(u)|^2=(2\pi|u|)^q>0.
\]

Its nonzero exponential proves invertibility for every complex \(t\), including collisions. The explicit contour phases in SC6 are preserved. Thus the coefficient-to-period map \(\Pi:(E,G)\to(\mathbb C^q,\widetilde G)\), where

\[
\widetilde G=\Pi^{-*}G\Pi^{-1},
\]

is an onto isometry. Indeed \((\Pi v)^*\widetilde G(\Pi w)=v^*Gw\), and the inverse is the actual \(\Pi^{-1}\). This is the transported theta metric from SC23–SC25. It is not replaced by the different coordinate metric \(I_q\) used for the separate constituent curvature; their exact connection remains the SC metric congruence.

With the literal transformations

\[
\widetilde A_t=\Pi A_t\Pi^{-1},\quad
\widetilde L_t=\Pi L_t\Pi^{-1},\quad
\widetilde W_t=\Pi^{-*}W_t\Pi^{-1},
\]

matrix multiplication gives

\[
\widetilde A_t^*\widetilde G+\widetilde G\widetilde A_t-k\widetilde G
=\Pi^{-*}(A_t^*G+GA_t-kG)\Pi^{-1}
=\widetilde W_t,
\]
\[
\widetilde L_t=\widetilde A_t^2-k\widetilde A_t,
\qquad
\widetilde G^{-1}\widetilde W_t=\Pi X_t\Pi^{-1}.
\]

The last operator has exactly the same metric norm, by the stated onto isometry. For \(x=\Pi v\), the norm, Laplacian quotient, control quotient and the \(B_t\) norm quotient are each identical to those in Sections 1 and 6. The adjoint-defect identity also carries through in full:

\[
\widetilde L_t^*\widetilde G-\widetilde G\widetilde L_t
=\Pi^{-*}(L_t^*G-GL_t)\Pi^{-1}
=\widetilde A_t^*\widetilde W_t-\widetilde W_t\widetilde A_t.
\]

Thus LC11 applies literally unchanged in this period realization. The action transported from the fixed original algebra is \(\Pi A\Pi^{-1}\). The action transported from the deformed companion differs by exactly \(t\Pi R\Pi^{-1}\). The norm and control of this difference have already been calculated in Section 3; neither deformation is substituted silently for the other.

## 8. The original arithmetic source and its primitive

SC7–SC8 specify the original coefficient quotient map \(j_E\) on the admitted source domain and the least source lift

\[
r_N=\mathcal V O_N^{-1}B_N^*G_N:E\longrightarrow\mathscr B_k,
\qquad j_Er_N=I_E.
\]

Here \(\mathscr B_k\) denotes that stated original tensor-source domain; its original Euler action satisfies \(j_ED^{(k)}=Aj_E\). Its exact primitive is

\[
D^{(k)}r_N-r_NA=dK_N^{\rm prim},
\]

where the primitive has the original degree-one-lower tensor-complex target. Define on the same admitted source domain

\[
D_t^{(k)}=D^{(k)}+t r_NRj_E.
\]

The added arrow has types \(\mathscr B_k\xrightarrow{j_E}E\xrightarrow R E\xrightarrow{r_N}\mathscr B_k\). Its image is the actual finite lift space and its restriction to \(\ker j_E\) is zero. Substitution of \(j_Er_N=I_E\) gives

\[
j_ED_t^{(k)}=(A+tR)j_E=A_tj_E,
\]
\[
D_t^{(k)}r_N-r_NA_t
=D^{(k)}r_N+t r_NR-r_NA-t r_NR
=dK_N^{\rm prim}.
\]

This proves the exact cancellation and preserves the original primitive, every kernel class and the receiving quotient. Iterating the intertwining on its stable source domain gives the explicit Laplacian observation

\[
j_E\bigl((D_t^{(k)})^2-kD_t^{(k)}\bigr)=L_tj_E.
\]

For completeness the lift defect of this quadratic operator is already determined without any new estimate:

\[
\bigl((D_t^{(k)})^2-kD_t^{(k)}\bigr)r_N-r_NL_t
=D_t^{(k)}dK_N^{\rm prim}+dK_N^{\rm prim}A_t-kdK_N^{\rm prim}.
\]

Indeed expand the square using \(D_t^{(k)}r_N=r_NA_t+dK_N^{\rm prim}\). The right side has zero \(j_E\) observation by the intertwining, as required. Moreover \(j_EdK_N^{\rm prim}=0\), so the added finite-rank term acts as zero on this original boundary and \(D_t^{(k)}dK_N^{\rm prim}=D^{(k)}dK_N^{\rm prim}\). The original Euler action commutes with the tensor differential; writing its action in the primitive's degree as \(D^{(k)}_{\rm prim}\), the entire difference is the boundary

\[
d\left(D^{(k)}_{\rm prim}K_N^{\rm prim}
      +K_N^{\rm prim}A_t-kK_N^{\rm prim}\right).
\]

All operators here retain their declared degrees and the same original differential. This spells out the source-to-coefficient polynomial map underlying the final paragraph of LC12.

Each linear arrow also has the original supported lift from SC14: a represented vector \(v^\bullet\) maps to \(f(v)^\bullet\), and external absence \(\tau\) maps to \(\tau\). Its kernel therefore maps to the supported zero at the original receiving label. The period isomorphism and these source identities introduce no new support adjunction.

## 9. Scope of the completed review

The additional rank-one control has been fully evaluated, with its exact metric lengths and both scalar and nilpotent cases. The original control is supplied by its norm definition and, in the reflection-stable arithmetic case, by the complete Toda determinant and positive-minor formulas. The numerical-range enclosure follows for that actual finite control at every complex deformation parameter and every allowed period parameter. The proof supplies no estimate uniform in packet size for \(\epsilon_N\) or \(\sigma_N\), and uses none. No arithmetic asymptotic, zero-location result, or independence of the period metric from its parameters is inferred.

The detailed Toda dependency review is retained separately as `work/period_laplacian_toda_dependency_review_20260913.md`. The primary LC changes made during this review concern local typing only; all twelve displayed results and their constants are unchanged.

## 10. LC13: the original constituent and both positive projection factors

Let \(I:F\hookrightarrow E\) be an actual injection with \(AI=IA_F\) and \(0<p=\dim F<q\). This implies \(q>1\), exactly the range in which LC5 defines the nilpotent companion radius. Retain

\[
G_F=I^*GI,\quad P_F=I G_F^{-1}I^*G,\quad L=\ell I,
\quad f=G^{-1}\ell^*.
\]

The injectivity of \(I\) and positivity of \(G\) imply \(G_F>0\). Multiplication gives \(P_F^2=P_F\), \(P_FI=I\), and \(P_F^*G=GP_F\). Thus \(P_F\) is exactly the orthogonal projection onto \(I(F)\) in the original metric. In particular

\[
e_0^*G(1-P_F)e_0=\|(1-P_F)e_0\|_G^2=:a_\perp.
\]

Using \(I^*Gf=I^*\ell^*\), the projection of \(f\) is
\(P_Ff=I G_F^{-1}I^*\ell^*\). Its squared norm is

\[
\begin{aligned}
\|P_Ff\|_G^2
&=\ell I G_F^{-1}(I^*GI)G_F^{-1}I^*\ell^*\\
&=\ell I G_F^{-1}I^*\ell^*
=L G_F^{-1}L^*=:b_F.
\end{aligned}
\]

The positivity assertions use the actual cyclic structure. Invariance under \(A\) gives invariance under every polynomial in \(A\); this is invariance under multiplication by every element of \(E\). Hence \(I(F)\) is an ideal. Its inverse image in \(\mathbb C[S]\) is generated by a unique monic \(g\mid\chi\). With \(\chi=gh\), the map \([a]_h\mapsto[ga]_\chi\) is surjective onto that ideal, and \(gh\mid ga\) implies \(h\mid a\), proving injectivity. Thus \(\deg h=p\), and the literal monic basis

\[
[g],[Sg],\ldots,[S^{p-1}g]
\]

has a last vector of degree \(q-1\) and top coefficient one. This proves \(L\ne0\), and therefore \(b_F>0\). If \(e_0\) belonged to the ideal, multiplication by arbitrary elements would make the ideal all of \(E\), contrary to properness. Therefore \(a_\perp>0\). Every repeated factor is preserved by this ideal correspondence; no reduced-spectrum replacement enters the argument.

## 11. LC14: actual metric comparison eigenvalues and the residual minimum

Set \(Q(t)=\Pi(t)^*\Pi(t)>0\), and \(B(t)=G^{-1}Q(t)\). This operator is \(G\)-self-adjoint because \(B^*G=GB=Q\). Its quadratic form is strictly positive on every nonzero vector. Its smallest and largest eigenvalues \(m(t),M(t)\) are therefore actual finite numbers satisfying \(0<m(t)\le M(t)\). The spectral theorem in the original metric gives

\[
m(t)G\preceq Q(t)\preceq M(t)G.
\]

These eigenvalues are defined from the complete period matrix and original Gram. Their existence is not a postulated estimate. No independence of \(t,u,N\), the original coefficients or packet size is claimed.

Put \(Y=\Pi I\), \(H_F=Y^*Y\), and
\(z=(1-YH_F^{-1}Y^*)\Pi e_0\). Full rank of \(Y\) follows from the two injections. The standard-coordinate period projection is therefore well-defined, and orthogonal Pythagoras proves

\[
\|z\|_{I_q}^2=\min_{x\in F}(e_0-Ix)^*Q(t)(e_0-Ix).
\]

The same minimization with \(G\) has the unique minimizer
\(x_G=G_F^{-1}I^*Ge_0\) and value \(a_\perp\). Indeed \(Ix_G=P_Fe_0\), so its residual is orthogonal to the image of \(I\). For every \(x\), the first displayed matrix bound gives

\[
(e_0-Ix)^*Q(t)(e_0-Ix)
\ge m(t)\|e_0-Ix\|_G^2\ge m(t)a_\perp.
\]

Taking the minimum proves the lower residual bound. Evaluating at the actual \(x_G\) and using the upper matrix bound proves the upper one. Thus

\[
m(t)a_\perp\le\|z(t)\|_{I_q}^2\le M(t)a_\perp.
\]

Compression of the matrix inequality by \(I\) gives
\(m(t)G_F\preceq H_F\preceq M(t)G_F\). To verify the inverse direction without a commutation assumption, for every positive \(T\) and column \(w\), completion of the square gives

\[
2\operatorname{Re}(w^*x)-x^*Tx
=w^*T^{-1}w-(x-T^{-1}w)^*T(x-T^{-1}w).
\]

Its maximum is \(w^*T^{-1}w\). Ordering the three original quadratic forms orders these maxima in the opposite direction. Hence

\[
M(t)^{-1}G_F^{-1}\preceq H_F^{-1}
\preceq m(t)^{-1}G_F^{-1}.
\]

Using the same original row \(L\) yields precisely

\[
\frac{b_F}{M(t)}\le L H_F^{-1}L^*\le\frac{b_F}{m(t)}.
\]

This proves both pairs in LC14, including the exact positions of \(m(t)\) and \(M(t)\).

## 12. LC15: the actual curvature coefficient and its two-sided comparison

With the fixed invariant constituent, the accepted period equation gives

\[
Y'=-\frac1u YA_F-\frac t u\Pi e_0L.
\]

Let \(N_{\rm per}=1-YH_F^{-1}Y^*\). Then \(N_{\rm per}Y=0\), \(N_{\rm per}^*=N_{\rm per}^2=N_{\rm per}\), and
\(N_{\rm per}Y'=-tzL/u\). Holomorphy of \(Y\) gives

\[
\partial_t H_F=Y^*Y',\quad
\partial_{\bar t}H_F=Y'^*Y,\quad
\partial_{\bar t}\partial_tH_F=Y'^*Y'.
\]

Differentiating the inverse identity and then the determinant logarithm gives

\[
\begin{aligned}
\partial_{\bar t}\partial_t\log\det H_F
&=\operatorname{Tr}\bigl(H_F^{-1}Y'^*Y'
-H_F^{-1}Y'^*YH_F^{-1}Y^*Y'\bigr)\\
&=\operatorname{Tr}(H_F^{-1}Y'^*N_{\rm per}Y')\\
&=\frac{|t|^2}{|u|^2}\|z(t)\|_{I_q}^2 L H_F^{-1}L^*.
\end{aligned}
\]

The final trace uses the full rank-one outer product \(L^*L\); its trace is exactly \(LH_F^{-1}L^*\). Thus the coefficient \(c_F(t)\) is positive and has the literal definition from SC16. Multiplying the positive lower factors from Section 11, and then the positive upper factors, gives

\[
\frac{m(t)}{M(t)}\frac{a_\perp b_F}{|u|^2}
\le c_F(t)\le
\frac{M(t)}{m(t)}\frac{a_\perp b_F}{|u|^2}.
\]

The curvature itself is \(|t|^2c_F(t)\). Consequently it vanishes at \(t=0\) even though this coefficient is strictly positive there. The parameter's complex modulus and the period factor \(|u|^2\) remain unchanged.

## 13. LC16: the complete nonnegative loss against the companion radius

In the notation of Sections 3 and 10,

\[
a_0=\|e_0\|_G^2=\|P_Fe_0\|_G^2+a_\perp,
\quad
b_0=\|f\|_G^2=b_F+\|(1-P_F)f\|_G^2,
\quad\sigma_N^2=a_0b_0.
\]

These are orthogonal Pythagoras identities for the original projection and vectors. Direct multiplication, with neither component discarded, gives

\[
\begin{aligned}
\sigma_N^2-a_\perp b_F
&=(a_0-a_\perp)b_0+a_\perp(b_0-b_F)\\
&=\|P_Fe_0\|_G^2b_0
+a_\perp\|(1-P_F)G^{-1}\ell^*\|_G^2\ge0.
\end{aligned}
\]

Every factor in the two products is retained. In particular the first product contains the full \(b_0\), not just its projected component \(b_F\); replacing it would lose the mixed term. Since \(b_0,a_\perp>0\), equality holds exactly when \(P_Fe_0=0\) and \((1-P_F)f=0\). The displayed identity is valid regardless of whether equality occurs. The column \(f\) is exactly that already defined in LC5; no new meaning is assigned to the original programme's theta-source notation.

Combining it with Section 12 proves

\[
c_F(t)\le\frac{M(t)}{m(t)}\frac{\sigma_N^2}{|u|^2}.
\]

On a proper nonzero constituent \(q>1\), so the already proved exact companion formula \(\|X_t-X_0\|_G^2=|t|^2\sigma_N^2\) applies. Multiplying by the retained \(|t|^2\) therefore proves the actual derivative comparison

\[
\partial_{\bar t}\partial_t\log\det H_F(t)
\le\frac{M(t)}{m(t)}\frac{\|X_t-X_0\|_G^2}{|u|^2}.
\]

The result has the original constituent projections, the complete period comparison eigenvalues and the exact metric radius on both sides. It assumes no uniform bound on these quantities.

## 14. Final scope of LC1–LC16

The added comparison is restricted to \(0<\dim F<q\), which supplies \(q>1\), \(a_\perp>0\) and \(b_F>0\). There is no nonzero proper constituent when \(q=1\); its separately proved LC7 control remains valid. For the zero or full constituent, the original SC normal map and its curvature are zero directly, using the empty or full projection. None of the strict positivity statements for a proper constituent is invoked for those cases.

The exact comparison joins the original companion's relative self-adjoint change to the period constituent curvature through the original theta projections and the actual finite period metric. It does not identify the period-coordinate metric with the transported theta metric, and their full congruence and eigenvalue comparison were proved above. The independent extension check is retained as `work/period_laplacian_constituent_comparison_review_20260913.md`. All final claims remain finite identities or inequalities for the stated original objects; no arithmetic asymptotic is used or asserted.

The coordinating author also requested that the explicit quadratic source primitive proved in Section 8 be promoted into the primary article. It is now LC12a. Its \(D_0\) is the original Euler source action of cochain degree zero on the primitive term \(\mathcal C_{\rm prim}\); it is the operator denoted \(D^{(k)}_{\rm prim}\) in Section 8. The primary proof first establishes \(D_t^{(k)}d=dD_0\) from the original chain identity and \(j_Ed=0\), then expands both terms of \((D_t^{(k)})^2r_N\). The primitive is exactly \(D_0K_N^{\rm prim}+K_N^{\rm prim}A_t-kK_N^{\rm prim}\), including the full \(tK_N^{\rm prim}R\) term. This final addition and the \(f\) notation reuse were read in full at the final source hash listed above. All resulting arrows have the domains and codomains specified in Section 8; no further source estimate or test is needed.

The final local type wording also calls \(W_t\) the control form, and \(X_t,L_t,B_t\) the respective endomorphisms, rather than calling all four objects endomorphisms. Its exact displayed map is \(v^*W_tw=\langle v,X_tw\rangle_G\), with \(X_t=G^{-1}W_t\), precisely the identification proved in Section 1. This changes no matrix formula or constant and agrees with the congruence transport in LC12.
