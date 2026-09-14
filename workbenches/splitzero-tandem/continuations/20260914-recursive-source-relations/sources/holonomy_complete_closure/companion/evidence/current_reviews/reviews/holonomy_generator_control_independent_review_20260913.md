# Independent full proof review of the holonomy–generator bridge

Date: 2026-09-13. Reviewer: the cumulative integration review task. This is the complete mathematical review of HG1–25 plus HG11a in `holonomy_generator_control_bridge_20260913.tex`, at SHA-256 `39c67cb2953de52c109831893c347a6ff97639a151f24445d98b357edd7d3282`. The earliest candidate ended at HG24; a successor added HG25, and the final source proves the spectral-diameter sharpening HG11a and propagates it through HG11, HG22's finite-tail term and the finite allowance after HG22. The whole source was read at the preceding candidate and its final exact rho-plus-epsilon patch was read directly; the complete supplied holonomy `NOTE.md`, the complete coordinating task's `EXACT_ORIGINAL_RESIDUE_COMMUTATOR.md`, and its complete `ACTUAL_METRIC_COMMUTATOR_TRANSFER.md` were also read. Their exact source pins are recorded in the accompanying JSON receipt. The pre-sharpening review draft is preserved separately under its content hash.

The parent requested an independent check of all proofs, particularly the original-metric quadratic generator transfer, the exact rank-two norm with singular Grams, the explicit period/strip/phase/frequency choices, the finite discrepancy constant, and every action boundary. This review supplies the calculations below. No mathematical source was edited. No Lean process, inherited test suite, numerical theta integral, or numerical interval evaluation was run or claimed. The fixed 765-page reader had already been accepted and promoted; HG belongs to a later increment.

The final disposition is acceptance of HG1–25 and HG11a for the stated original finite source. All constants below retain their actual source-integral definitions. This proves the displayed finite-source comparisons and control transfers. It does not assign a uniform numerical bound to those source integrals or to the actual finite control radius.

## 1. Objects, source hypotheses, and exact types

Keep the original integer tensor degree (k\ge1), nonempty full-order packet, its monic cyclic polynomial (\chi=\chi_{h,k}\) of degree (q\ge1), and

\[
 E=\mathbb C[S]/(\chi),\qquad A[P]=[SP],\qquad
 e_0=[1],\qquad \ell[P]=[S^{q-1}]\operatorname{rem}_\chi P,
 \qquad R=e_0\ell.
 \tag{RHG1}
\]

For (N\ge q-1), write (d=N+1), (r_0^{\mathrm{rel}}=N+1-q\ge0), and

\[
 J:\mathcal P_N\longrightarrow E,\quad P\longmapsto[P],
 \qquad
 B_{\mathrm{rel}}:\mathbb C^{r_0^{\mathrm{rel}}}\longrightarrow\mathcal P_N,
 \quad Q\longmapsto\chi Q.
 \tag{RHG2}
\]

Monic polynomial division proves that (J) is onto, that (B_{\mathrm{rel}}) is injective, and that its image is precisely (\ker J). For (N=q-1), this domain is the zero vector space and (J) is an isomorphism. In particular, the apparent inverses on the relation space later in the proof have an explicit zero-dimensional case.

The original source is (\mathcal V P=P(D_1+\cdots+D_k)F_h^{\otimes k}), with (\mathcal M F_h=g/h), (g=2\xi), and the unchanged full-jet inclusion (\eta[P]=\upsilon_h^{\otimes k}P(A_k)1). These are the source inputs H5–H8 of the supplied holonomy note; they are not newly postulated substitute representatives. The source identity under (J^{(k)}\) and the original tensor theta primitive are inherited complete constructions. The new proof uses the literal polynomial relation (\chi Q) and its same primitive. It never asserts that a source relation has zero Hilbert norm merely because its cohomology class is zero.

The finite source maps into (L^2(\mathbb R,dr;\mathcal K)), with (\mathcal K=L^2(\mathbb R^{k-1},dz)). The weighted source norms and weighted derivative norms appearing in HG3 and HG18 are the actual finite quantities supplied by the source construction, as specified in H11, H39 and H50 of the supplied note. There is no new freedom to choose their values. Positivity of the unweighted source Gram also follows directly from its stated spectral norm: a nonzero polynomial has only finitely many zeros on the vertical spectral line, while (m_{h,k}=w_h^{*k}) is positive almost everywhere and not zero. For (k=1), (g/h) is a nonzero entire function and its line zeros are isolated; for (k\ge2), convolution makes the density positive at every real point. Thus no nonzero polynomial source vector has zero norm. Multiplication by the everywhere-positive weights (e^{\pm ar}) likewise makes each finite weighted Gram positive, with finite largest generalized eigenvalues.

All Gram matrices in the reviewed proof act in the original coefficient frames. A star denotes the coefficient dual/conjugate transpose; the adjoint between specified metric spaces includes those metric matrices. We use the stated convention (\langle v,w\rangle_G=v^*Gw), conjugate-linear in the first slot.

## 2. HG1–3: half-density, Fourier reconstruction, and source-relative phase error

The coordinate map is

\[
 x_i=e^{r+z_i}\ (i<k),\qquad x_k=e^r.
 \tag{RHG3}
\]

The Jacobian of the logarithmic linear map from ((z_1,\ldots,z_{k-1},r)) to ((\log x_1,\ldots,\log x_k)) has determinant one. Hence the actual product measure is

\[
 d^kx=e^{kr+\sum_{i<k}z_i}\,dr\,dz.
 \tag{RHG4}
\]

The squared half-density factor in HG1 is exactly this factor. It follows by substitution that the integral of (|\mathcal U_kF|^2\) against (dr\,dz) equals the original integral of (|F|^2\) against (d^kx). No relative variable or source mass is removed. Differentiating at fixed (z) gives (\partial_rF(x)=\sum_i x_i\partial_{x_i}F(x)). Differentiating the half-density as well then gives

\[
 (-\partial_r+k/2)\mathcal U_kF=\mathcal U_kD^{(k)}F.
 \tag{RHG5}
\]

Use the representative (0\le\theta<2\pi) of the phase circle, the measure (d\theta/(2\pi)), and (0\le r<L). For almost every (r), the sequence ((\psi(r+aL))_{a\in\mathbb Z}) lies in (\ell^2(\mathbb Z;\mathcal K)), since its integrated squared sequence norm is (\|\psi\|^2). Its Fourier series is precisely

\[
 \sum_a e^{ia\theta}\psi(r+aL).
 \tag{RHG6}
\]

Parseval on this sequence, followed by the (r)-integral, proves the isometry in HG2. Its coefficient at (a) is the integral against (e^{-ia\theta}), proving the stated inverse in the (L^2) sense and for almost every fixed (r). The actual finite source has the stronger weighted regularity required for its pointwise/derivative manipulations. Polarization of the norm identity yields the whole matrix identity (\int M_\theta\,d\mu=M), including every cross coefficient.

For the correlation estimate put (f(r)=\Psi_N(r)v). When (s\ge0), the ordered scalar integrand can be written with its exact factor as

\[
 \langle f(r),f(r+s)\rangle
 =e^{-as}\langle e^{-ar}f(r),e^{a(r+s)}f(r+s)\rangle.
 \tag{RHG7}
\]

Cauchy–Schwarz and the change of variable (u=r+s) imply

\[
 |v^*\mathcal C(s)v|
 \le e^{-as}\sqrt{(v^*M_{a,-}v)(v^*M_{a,+}v)}.
 \tag{RHG8}
\]

Changing variables proves (\mathcal C(-s)=\mathcal C(s)^*), so the same scalar bound holds at negative (s). The uniform summability supplied by this exponential bound justifies unfolding the actual periodization Gram. With (b=c-a) for its two translation indices, the phase multiplier is (e^{ib\theta}), and the unfolded integral is (\mathcal C(bL)). Thus its sign is exactly the one in HG3.

The two nonzero correlation tails together satisfy

\[
 \begin{aligned}
 |v^*(M_\theta-M)v|
 &\le 2\sqrt{(v^*M_{a,-}v)(v^*M_{a,+}v)}
                  \sum_{b=1}^\infty e^{-abL}\\
 &\le \frac{v^*(M_{a,-}+M_{a,+})v}{e^{aL}-1}
 \le\delta\,v^*Mv.
 \end{aligned}
 \tag{RHG9}
\]

Since (M_\theta-M) is Hermitian, this is exactly the claimed two-sided Loewner inequality. In particular, the subsequently proved (\delta<1) gives (M_\theta\succeq(1-\delta)M\succ0) for every phase. This argument also covers individually vanishing sample masses: positivity comes from the full finite-source inequality and does not require each individual sample to be positive.

## 3. HG4–7: canonical sections and the quadratic relation norm

For any positive source Gram (M_0), the matrix (JM_0^{-1}J^*) is positive: (J^*v\ne0) for (v\ne0), because (J) is onto. Its inverse (G_0) exists. The section (C_0=M_0^{-1}J^*G_0) has

\[
 JC_0=I_E,\qquad B_{\mathrm{rel}}^*M_0C_0
 =B_{\mathrm{rel}}^*J^*G_0=0,\qquad C_0^*M_0C_0=G_0.
 \tag{RHG10}
\]

Every representative of (vin E) is uniquely (C_0v+B_{\mathrm{rel}}w). Expanding its squared (M_0)-norm gives

\[
 v^*G_0v+w^*(B_{\mathrm{rel}}^*M_0B_{\mathrm{rel}})w,
 \tag{RHG11}
\]

because both ordered cross terms vanish. The relation Gram is positive on its nonzero domain. Thus the minimum is unique at (w=0). Applying this to (M) and (M_\theta) proves every assertion about (C,G,C_\theta,G_\theta) in HG4.

Since (J(C-C_\theta)=0), exactness of RHG2 gives a unique (X_\theta:E\to\mathbb C^{r_0^{\mathrm{rel}}}) with (C-C_\theta=B_{\mathrm{rel}}X_\theta). Multiplying by (B_{\mathrm{rel}}^*M_\theta) gives the formula in HG5, with its positive sign. For each phase,

\[
 C^*M_\theta C
 =G_\theta+(C-C_\theta)^*M_\theta(C-C_\theta).
 \tag{RHG12}
\]

Averaging the left side gives (C^*MC=G). This proves (G=\overline G+\mathscr D), with the actual positive relation form (\mathscr D). For the empty relation domain both sections equal (J^{-1}), and (\mathscr D=0). In particular, the equality is not obtained by declaring the norm of a theta relation to vanish.

For the lower bound on (\overline G), the scalar identity in HG6 expands to

\[
 \frac{x(2-x)-(1-\delta^2)}{x(1-\delta^2)}
 =\frac{\delta^2-(x-1)^2}{x(1-\delta^2)}\ge0.
 \tag{RHG13}
\]

The positive (M)-self-adjoint endomorphism (X=M^{-1}M_\theta) has spectrum in ([1-\delta,1+\delta]). Applying RHG13 in its finite spectral decomposition gives (f(X)\succeq_M0). Composing with the actual dual map (M^{-1}) produces an ordinary positive form: for a dual column (z),

\[
 z^*f(X)M^{-1}z
 =\langle M^{-1}z,f(X)M^{-1}z\rangle_M\ge0.
 \tag{RHG14}
\]

Expanding (f(X)M^{-1}) gives precisely

\[
 M_\theta^{-1}\preceq
 \frac{2M^{-1}-M^{-1}M_\theta M^{-1}}{1-\delta^2}.
 \tag{RHG15}
\]

After averaging and applying (J,J^*), this gives

\[
 \overline K:=\int G_\theta^{-1}d\mu
 \preceq\frac{G^{-1}}{1-\delta^2}.
 \tag{RHG16}
\]

The block form in HG6 is positive because its value is exactly

\[
 (x+G_\theta y)^*G_\theta^{-1}(x+G_\theta y).
 \tag{RHG17}
\]

Averaging gives a block form with diagonal blocks (\overline K,\overline G). Its Schur complement is (\overline G-\overline K^{-1}\succeq0). Inversion reverses RHG16, and hence

\[
 (1-\delta^2)G\preceq\overline K^{-1}
 \preceq\overline G\preceq G.
 \tag{RHG18}
\]

It follows that (0\preceq\mathscr D\preceq\delta^2G). The endomorphism (\mathsf D=G^{-1}\mathscr D) satisfies (\mathsf D^*G=\mathscr D=G\mathsf D); therefore it is (G)-self-adjoint and (0\preceq_G\mathsf D\preceq_G\delta^2I). This proves all of HG7 in the original metric, including its exact relation to (G^{-1}\overline G).

## 4. HG8–11: exact isometry, Sylvester integral, and full generator transfer

Keep (T_t=A+tR-kI/2) for the original complex (t). For an actual positive (H), set (C_H=G^{-1}H=I+B). Then (B^*G=H-G=GB). The lower bound (C_H\succeq_G\alpha I), with (\alpha>0), gives the unique positive (G)-self-adjoint square root (\mathsf S=C_H^{1/2}). This has the exact metric identity

\[
 \mathsf S^*G\mathsf S=G\mathsf S^2=GC_H=H.
 \tag{RHG19}
\]

Thus (\mathsf S:(E,H)\to(E,G)) is an isometry with inverse (\mathsf S^{-1}). It does not identify (H) and (G) as forms on the same untransformed vector. The ordered adjoint identity is

\[
 T_t^{\dagger_H}=C_H^{-1}T_t^{\dagger_G}C_H
 =\mathsf S^{-2}T_t^{\dagger_G}\mathsf S^2.
 \tag{RHG20}
\]

Consequently

\[
 \begin{aligned}
 \mathsf S X_H\mathsf S^{-1}-X_G
 &=\mathsf S^{-1}T_t^{\dagger_G}\mathsf S-T_t^{\dagger_G}
   +\mathsf S T_t\mathsf S^{-1}-T_t\\
 &=Z^{\dagger_G}+Z,\qquad
 Z=[\mathsf S,T_t]\mathsf S^{-1}.
 \end{aligned}
 \tag{RHG21}
\]

This verifies both the factor order and the adjoint in HG9. The Hermitian sum is retained before any norm estimate.

Let (Y=[\mathsf S,T_t]). Direct expansion gives

\[
 \mathsf S Y+Y\mathsf S=[\mathsf S^2,T_t]=[B,T_t].
 \tag{RHG22}
\]

For (K=[B,T_t]), define (Y_0=\int_0^\infty e^{-r\mathsf S}K e^{-r\mathsf S}\,dr). Its integrand has norm at most (e^{-2r\sqrt\alpha}\|K\|_G), so the integral converges absolutely in the finite operator norm. Differentiation and integration give

\[
 \mathsf S Y_0+Y_0\mathsf S
 =-\int_0^\infty\frac d{dr}(e^{-r\mathsf S}Ke^{-r\mathsf S})\,dr
 =K-0.
 \tag{RHG23}
\]

The endpoint (K) at zero is retained. If (Y_1) solves the homogeneous equation, decompose by the spectral projectors (P_i) of (\mathsf S). Each block satisfies ((s_i+s_j)P_iY_1P_j=0), and every (s_i+s_j>0). Hence (Y_1=0), also with repeated eigenvalues. Thus (Y=Y_0) and

\[
 \|[\mathsf S,T_t]\|_G\le\frac{\|[B,T_t]\|_G}{2\sqrt\alpha},
 \qquad \|\mathsf S^{-1}\|_G\le\alpha^{-1/2}.
 \tag{RHG24}
\]

Isometric transport preserves the control norm: (\|\mathsf S X_H\mathsf S^{-1}\|_G=\epsilon_H(t)). The reverse triangle inequality and RHG21–24 therefore prove

\[
 |\epsilon_H(t)-\epsilon_G(t)|
 \le\|Z+Z^{\dagger_G}\|_G
 \le\alpha^{-1}\|[B,T_t]\|_G
 =\alpha^{-1}\|[B,A]+t[B,R]\|_G.
 \tag{RHG25}
\]

The scalar (kI/2) commutes with (B); this exact reason removes it from the commutator, while it remains in (T_t) and its rough norm bound. The coefficient of ([B,R]) here is (t), not (\overline t); conjugation enters the adjoint term in RHG21 and is already retained there.

For the holonomy mean, (B=-\mathsf D), (\alpha=1-\delta^2), and the whole commutator changes only by a minus sign. Its norm is unchanged by that scalar. Since (\|\mathsf D\|_G\le\delta^2),

\[
 \|[\mathsf D,T_t]\|_G
 \le\|\mathsf D T_t\|_G+\|T_t\mathsf D\|_G
 \le2\delta^2\|T_t\|_G.
 \tag{RHG26}
\]

RHG26 is a valid preliminary bound. The final source sharpens its coefficient by proving HG11a as follows. For any (G)-self-adjoint (B), retain all its distinct eigenvalues (b_1<\cdots<b_r), full eigenspaces, and original spectral projections (P_j=\mathbf1_{(b_j,\infty)}(B)). On an eigenvector at (b_l), the endomorphism

\[
 b_1I+\sum_{j=1}^{r-1}(b_{j+1}-b_j)P_j
 \tag{RHG26a}
\]

has eigenvalue (b_1+\sum_{j<l}(b_{j+1}-b_j)=b_l). Thus RHG26a equals (B) on every spectral subspace. In the actual (G)-orthogonal decomposition (E=\operatorname{im}P_j\oplus\ker P_j), write the four blocks of (T) as (T_{ab}). Direct multiplication gives

\[
 [P_j,T]=\begin{pmatrix}0&T_{12}\\-T_{21}&0\end{pmatrix},
 \qquad
 \|[P_j,T](u,w)\|_G^2
 =\|T_{12}w\|_G^2+\|T_{21}u\|_G^2.
 \tag{RHG26b}
\]

The exact operator norm is therefore the maximum of the two off-diagonal block norms, including a zero block when a summand is zero. Each block is a compression of (T) between orthogonal subspaces, so its norm is at most (\|T\|_G). Commuting RHG26a with (T), taking the triangle inequality and summing its nonnegative original gaps gives

\[
 \|[B,T]\|_G
 \le\sum_{j=1}^{r-1}(b_{j+1}-b_j)\|[P_j,T]\|_G
 \le(b_r-b_1)\|T\|_G.
 \tag{RHG26c}
\]

For (r=1), the sum is empty and the commutator is zero. This proves HG11a while retaining every eigenvalue and spectral subspace. In particular, the actual spectrum of (\mathsf D) lies in ([0,\delta^2]), so its diameter is at most (\delta^2). The final holonomy allowance is exactly

\[
 \frac{\|[\mathsf D,T_t]\|_G}{1-\delta^2}
 \le\frac{\delta^2}{1-\delta^2}\|T_t\|_G.
 \tag{RHG26d}
\]

This proves the final improved coefficient in HG11, after retaining its full ordered commutator. If that commutator is zero, the Sylvester integral is zero, so (Z=0) and the transported control operators agree exactly. At (N=q-1), (\mathsf D=0) already, so this applies for every (t). More generally, a scalar comparison also commutes with every generator; this explains the zero-error case without claiming that the vector norms of its two metrics are identical.

## 5. HG12–15: full rank-two residue norm, including every singular case

Set (x=e_0), (y=G^{-1}\ell^*). The equality (y^*G=\ell) proves (\ell(v)=\langle y,v\rangle_G). Therefore (R=xy^{\dagger_G}). For (G)-self-adjoint (B), introduce auxiliary maps

\[
 U=[Bx,x]:\mathbb C^2\to E,\qquad
 V=[y,-By]:\mathbb C^2\to E.
 \tag{RHG27}
\]

The coefficient inner product on this auxiliary two-dimensional space is its displayed ordinary one; the source metric on (E) remains (G). On an arbitrary vector (v),

\[
 UV^{\dagger_G}v
 =Bx\langle y,v\rangle_G-x\langle By,v\rangle_G
 =Bx\ell(v)-x\ell(Bv)=[B,R]v.
 \tag{RHG28}
\]

The last equality uses self-adjointness in its exact form (\langle By,v\rangle_G=\langle y,Bv\rangle_G). It retains the minus sign before the second rank-one term.

The six moments in HG12 have (p_0,r_0\in\mathbb R): for example (\overline{\langle x,Bx\rangle_G}=\langle Bx,x\rangle_G=\langle x,Bx\rangle_G). Hence direct multiplication gives

\[
 P=U^{\dagger_G}U=\begin{pmatrix}a_0&p_0\\p_0&c_0\end{pmatrix},
 \qquad Q=V^{\dagger_G}V=\begin{pmatrix}d_0&-r_0\\-r_0&f_0\end{pmatrix}.
 \tag{RHG29}
\]

Both matrices are positive semidefinite, including when their column maps have a kernel. Their product has

\[
 \operatorname{tr}(PQ)=a_0d_0+c_0f_0-2p_0r_0=T_{\mathrm{res}},
 \qquad \det(PQ)=(a_0c_0-p_0^2)(d_0f_0-r_0^2)=\Delta_{\mathrm{res}}.
 \tag{RHG30}
\]

The two negative cross entries contribute the full (-2p_0r_0). Relative phases in (x,y,B) have not been erased; their actual values determine these moments and column Grams.

For completeness, if (A_0:\mathbb C^n\to\mathbb C^m) and (B_0:\mathbb C^m\to\mathbb C^n), eliminate either diagonal identity block in

\[
 \begin{pmatrix}I_m&-zA_0\\B_0&I_n\end{pmatrix}.
 \tag{RHG31}
\]

This gives the same determinant as both (I_m+zA_0B_0) and (I_n+zB_0A_0). The polynomial identity in (z) proves equality of all nonzero eigenvalues with algebraic multiplicities. It makes no full-rank assumption. For (K=[B,R]=UV^{\dagger_G}),

\[
 K^{\dagger_G}K=VPV^{\dagger_G}.
 \tag{RHG32}
\]

Apply RHG31 to (A_0=V), (B_0=PV^{\dagger_G}) to identify its nonzero eigenvalues with those of (PQ). In dimension two apply RHG31 to (A_0=P^{1/2}), (B_0=P^{1/2}Q). Its products are (PQ) and (P^{1/2}QP^{1/2}), respectively, so these two matrices have the same entire characteristic polynomial. The latter is positive semidefinite. Thus both roots of the characteristic polynomial of (PQ) are nonnegative real numbers, even when (P) is singular.

Their sum and product are RHG30, and therefore their values are

\[
 \lambda_\pm=\frac{T_{\mathrm{res}}\pm
 \sqrt{T_{\mathrm{res}}^2-4\Delta_{\mathrm{res}}}}2.
 \tag{RHG33}
\]

The positive metric adjoint makes (K^{\dagger_G}K) positive; its largest eigenvalue is its squared operator norm. The nonzero spectral correspondence above and its extra zero eigenvalues give precisely HG14. The case (q=1) is also included, since the two-dimensional determinant identity then forces enough zero eigenvalues in (PQ).

There is no inverse of (P,Q), no inverse of either Gram determinant, and no division by (\|x\|) or (\|y\|) anywhere in this proof. If (T_{\mathrm{res}}=0), positivity forces both eigenvalues to be zero and then (K=0). If (\Delta_{\mathrm{res}}=0<T_{\mathrm{res}}), one singular-value square is positive and one is zero, so the rank is one and the norm is (\sqrt{T_{\mathrm{res}}}). If (\Delta_{\mathrm{res}}>0), both are positive and the rank is two. A vanishing discriminant in this last case gives the two equal positive singular-value squares (T_{\mathrm{res}}/2), both retained.

In dimension one, (B=bI) with real (b); substitution gives

\[
 a_0=b^2c_0,\quad p_0=bc_0,\quad f_0=b^2d_0,\quad r_0=bd_0,
 \qquad T_{\mathrm{res}}=\Delta_{\mathrm{res}}=0.
 \tag{RHG34}
\]

This is the correct zero commutator with arbitrary original masses and complex functional. Nothing diagonalizes (A), divides by a root difference of (\chi), or suppresses its primary nilpotents, so repeated roots of the source polynomial have no effect on validity.

For (B=-\mathsf D), ([B,R]=-[\mathsf D,R]) has the same norm. The triangle inequality applied only after retaining ([\mathsf D,A]+t[\mathsf D,R]) gives HG15. This final separation can lose cancellation, while HG14 remains an exact evaluation of the residue commutator itself. The attribution to the coordinating Zeta task agrees with its complete proof, which was read independently.

## 6. HG16–17: complex strip and finite phase quadrature

For two distinct vectors (u,v), the same weighting as RHG7 gives, when (s\ge0),

\[
 |u^*\mathcal C(s)v|
 \le e^{-as}\sqrt{u^*M_{a,-}u}\sqrt{v^*M_{a,+}v}
 \le b_a e^{-as}\|u\|_M\|v\|_M.
 \tag{RHG35}
\]

At negative (s), adjunction interchanges the two weighted bounds and leaves their product (b_a=\sqrt{\kappa_+\kappa_-}) unchanged. Taking the dual supremum proves the operator norm bound (\|M^{-1}\mathcal C(nL)\|_M\le b_ae^{-a|n|L}).

The correlation series consequently converges absolutely and locally uniformly for (|\operatorname{Im}z|<aL), as do its entrywise derivatives on smaller closed strips. It defines a holomorphic matrix (\widetilde M(z)). On (|\operatorname{Im}z|\le s<aL),

\[
 \|M^{-1}(\widetilde M(z)-M)\|_M
 \le2b_a\sum_{n=1}^\infty e^{-(aL-s)n}
 =d_s.
 \tag{RHG36}
\]

Here (\widetilde M(z)) is the holomorphic extension of real phase-Gram entries. No star acts on (z). This matters because it is not generally Hermitian off the real axis.

To check every factor in the Schur estimate, equip the actual relation coefficient space with (K_{\mathrm{rel}}=B_{\mathrm{rel}}^*MB_{\mathrm{rel}}). The maps (C:(E,G)\to(\mathcal P_N,M)) and (B_{\mathrm{rel}}:(\mathbb C^{r_0^{\mathrm{rel}}},K_{\mathrm{rel}})\to(\mathcal P_N,M)) are isometries onto their complementary (M)-orthogonal images. These are their actual induced metrics. Write (F_z=M^{-1}(\widetilde M(z)-M)); its norm is at most (d_s). In these exact map types, the quotient block has perturbation norm at most (d_s), each ordered cross block has norm at most (d_s), and the relation block is (I+B_{\mathrm{rel}}^{\dagger}F_zB_{\mathrm{rel}}). The Neumann series makes its inverse exist with norm at most ((1-d_s)^{-1}) when (d_s<1). Therefore HG17 is holomorphic on the stated strip and

\[
 \|G^{-1}\widetilde G(z)\|_G
 \le1+d_s+d_s^2/(1-d_s)=1/(1-d_s).
 \tag{RHG37}
\]

For zero relation dimension its subtraction term is absent and the same upper bound holds. On the real axis, minimization by the canonical (M_\theta)-section is the Schur-complement calculation RHG11, so this extension agrees with the actual (G_\theta).

Let (F_n=(2\pi)^{-1}\int_0^{2\pi}G^{-1}\widetilde G(\theta)e^{-in\theta}d\theta). Shift to (operatorname{Im}z=-s\operatorname{sign}(n)). The two vertical integrals cancel by (2\pi)-periodicity and integer (n). The modulus of (e^{-inz}) on that shifted line is (e^{-s|n|}); hence

\[
 \|F_n\|_G\le(1-d_s)^{-1}e^{-s|n|}.
 \tag{RHG38}
\]

The series is absolutely convergent. Averaging it at (	heta_j=2\pi j/m) retains exactly frequencies divisible by (m), because the finite geometric character sum is one for these integers and zero for the others. The mean integral retains only (n=0). Thus

\[
 \|G^{-1}(H_m-\overline G)\|_G
 \le\frac2{1-d_s}\sum_{a=1}^\infty e^{-sma}
 =\frac2{(1-d_s)(e^{sm}-1)}=\varepsilon.
 \tag{RHG39}
\]

The real matrices are Hermitian, so this also means (-\varepsilon G\preceq H_m-\overline G\preceq\varepsilon G). Together with RHG18 this gives ((1-\delta^2-\varepsilon)G\preceq H_m\preceq(1+\varepsilon)G), with every phase-sampling constant retained.

## 7. HG18–20: finite Fourier tail and explicit positive budgets

The phase convention from HG2 gives boundary multiplier (e^{-i\theta}), hence basis (L^{-1/2}e^{-i(2\pi n+\theta)r/L}). Substituting (y=r+aL) in its coefficient integral cancels the phase as

\[
 e^{ia\theta}e^{-ia(2\pi n+\theta)}=1.
 \tag{RHG40}
\]

Thus the coefficient is exactly (L^{-1/2}\widehat\psi((2\pi n+\theta)/L)), with the Fourier convention of the source. The prefactor is not (1/L) at the coefficient level; its squared value (1/L) enters the Gram tail.

For (f=\Psi_Nv), integration by parts (p) times gives (widehat{f^{(p)}}(u)=(-iu)^p\widehat f(u)); the weighted regularity removes all endpoint terms. For (u\ne0), vector-valued Cauchy–Schwarz and (int_{\mathbb R}(1+r^2)^{-1}dr=\pi) yield

\[
 \|\widehat f(u)\|_{\mathcal K}^2
 \le\pi|u|^{-2p}\int(1+r^2)\|f^{(p)}(r)\|_{\mathcal K}^2dr
 =\pi|u|^{-2p}v^*H_{p,N}v.
 \tag{RHG41}
\]

For (0\le\theta<2\pi) and omitted (|n|>J\ge2), every omitted frequency is nonzero, and

\[
 |n+\theta/(2\pi)|\ge|n|-1,\qquad
 \sum_{|n|>J}(|n|-1)^{-2p}
 =2\sum_{a=J}^\infty a^{-2p}
 \le\frac{2(J-1)^{1-2p}}{2p-1}.
 \tag{RHG42}
\]

The last inequality integrates the decreasing positive function over ([J-1,\infty)). Multiplying its two tails by the exact factor ((\pi/L)(L/(2\pi))^{2p}) gives

\[
 \frac1{2p-1}\left(\frac{L}{2\pi(J-1)}\right)^{2p-1}.
 \tag{RHG43}
\]

This verifies the coefficient in HG18, including both tails and every (2\pi). Since (H_{p,N}\preceq h_pM), its tail is at most (\epsilon_JM\preceq\xi_JM_\theta), where (\xi_J=\epsilon_J/(1-\delta)). Therefore

\[
 (1-\xi_J)M_\theta\preceq M_{\theta,J}\preceq M_\theta.
 \tag{RHG44}
\]

When (\xi_J<1), this makes the retained finite Gram positive. Taking the minimum on the same affine fibre (J^{-1}(v)) in the lower and upper inequalities gives exactly ((1-\xi_J)G_\theta\preceq G_{\theta,J}\preceq G_\theta). The central coefficient (n=0,\theta=0) remains in the retained sum; no bound at (u=0) was used or needed. Averaging RHG44 at the chosen phases and using RHG39 proves HG19 with

\[
 \alpha=(1-\xi_J)(1-\delta^2-\varepsilon),\qquad\beta=1+\varepsilon.
 \tag{RHG45}
\]

It remains to verify that the choices in HG20 actually supply all preceding positivity requirements. Let (0<\delta_0<1), (0<\varepsilon_0<1-\delta_0^2), (0<\xi_0<1). Positivity of the two weighted Grams gives (b_a>0), and positivity of their sum gives (\kappa>0). With the exact chosen (L),

\[
 e^{aL}-1=\kappa/\delta_0+4b_a,\qquad
 \delta=\frac{\kappa}{\kappa/\delta_0+4b_a}<\delta_0.
 \tag{RHG46}
\]

The chosen (s=aL-\log(1+4b_a)) is strictly positive because (1+\kappa/\delta_0+4b_a>1+4b_a), and is strictly less than (aL) because (\log(1+4b_a)>0). Moreover

\[
 e^{aL-s}-1=4b_a,\qquad d_s=1/2.
 \tag{RHG47}
\]

The integer (m\ge\lceil s^{-1}\log(1+4/\varepsilon_0)\rceil) satisfies (e^{sm}-1\ge4/\varepsilon_0). Substituting (d_s=1/2) gives (\varepsilon=4/(e^{sm}-1)\le\varepsilon_0).

For the frequency integer put

\[
 X=\frac L{2\pi}
 \left(\frac{h_p}{(2p-1)\xi_0(1-\delta)}\right)^{1/(2p-1)}\ge0.
 \tag{RHG48}
\]

Then (J=2+\lceil X\rceil) has (J-1=1+\lceil X\rceil\ge X), as well as (J\ge2). If (h_p>0), substituting this inequality into HG18 yields (\epsilon_J\le\xi_0(1-\delta)); if (h_p=0), the tail bound is zero directly. Hence (\xi_J\le\xi_0<1) in all cases. Finally,

\[
 1-\delta^2-\varepsilon
 >1-\delta_0^2-\varepsilon_0>0.
 \tag{RHG49}
\]

Thus (\alpha>0) has been proved by explicit actual-source choices. These are finite mathematical values; the result does not assert that their defining integrals have been numerically enclosed. The constants may depend on the original packet, cutoff and tensor degree.

## 8. HG21–22: exact finite discrepancy and its commutator

The identity (G=\overline G+\mathscr D) gives

\[
 B_{m,J}=G^{-1}(H_{m,J}-G)
 =-\mathsf D+\mathsf E_{m,J},\qquad
 \mathsf E_{m,J}=G^{-1}(H_{m,J}-\overline G).
 \tag{RHG50}
\]

All three endomorphisms are (G)-self-adjoint. The upper inequality (H_{m,J}\preceq H_m\preceq\overline G+\varepsilon G) implies (H_{m,J}-\overline G\preceq\varepsilon G). The lower inequality is

\[
 \begin{aligned}
 H_{m,J}-\overline G
 &\succeq(1-\xi_J)(\overline G-\varepsilon G)-\overline G\\
 &=-\xi_J\overline G-(1-\xi_J)\varepsilon G\\
 &\succeq-[\xi_J+(1-\xi_J)\varepsilon]G=-\rho G.
 \end{aligned}
 \tag{RHG51}
\]

The final line uses (\overline G\preceq G) and (\xi_J\ge0) with the correct sign. As (\varepsilon<1),

\[
 \rho-\varepsilon=\xi_J(1-\varepsilon)\ge0.
 \tag{RHG52}
\]

Therefore (\|\mathsf E_{m,J}\|_G\le\rho). This proves the exact requested constant; replacing the factor (1-\xi_J) by one would give a larger bound but would lose the estimate actually proved here.

Apply RHG25 to the actual (H_{m,J}) with the actual positive lower bound RHG45. Since (B_{m,J}=-\mathsf D+\mathsf E_{m,J}), its full commutator is

\[
 [B_{m,J},T_t]=-[\mathsf D,A]-t[\mathsf D,R]
             +[\mathsf E_{m,J},A]+t[\mathsf E_{m,J},R].
 \tag{RHG53}
\]

This is the first inequality of HG22 with every sign and order retained. A preliminary separation after this equality gives

\[
 \|[B_{m,J},T_t]\|_G
 \le\|[\mathsf D,T_t]\|_G+2\rho\|T_t\|_G.
 \tag{RHG54}
\]

The final source uses the strictly more informative actual spectral interval already proved in RHG51–52: (\operatorname{spec}_G(\mathsf E_{m,J})\subseteq[-\rho,\varepsilon]). Applying the full spectral-projection proof RHG26c to this same endomorphism yields

\[
 \|[\mathsf E_{m,J},T_t]\|_G\le(\rho+\varepsilon)\|T_t\|_G,
 \qquad
 \|[B_{m,J},T_t]\|_G
 \le\|[\mathsf D,T_t]\|_G+(\rho+\varepsilon)\|T_t\|_G.
 \tag{RHG54a}
\]

This is the final second inequality of HG22. Since (\varepsilon\le\rho), it improves the valid preliminary coefficient (2\rho) without modifying the full commutator RHG53. The independent finite-bound reviewer derived the same interval refinement and the parent propagated it into the final source.

Independently, (I+B_{m,J}) has spectrum in ([\alpha,\beta]). The exact difference between its possible lower and upper deviations is

\[
 1-\alpha-\varepsilon
 =\xi_J(1-\varepsilon)+(1-\xi_J)\delta^2\ge0.
 \tag{RHG55}
\]

Thus (\|B_{m,J}\|_G\le1-\alpha) is independently valid. The final source uses the stronger spectral-diameter estimate RHG26c directly on the same actual spectral interval ([\alpha-1,\beta-1]). Its diameter is at most (\beta-\alpha), giving the propagated allowance

\[
 \alpha^{-1}\|[B_{m,J},T_t]\|_G
 \le\frac{\beta-\alpha}{\alpha}\|T_t\|_G.
 \tag{RHG55a}
\]

This is no larger than the earlier rough (2(1-\alpha)\|T_t\|_G/\alpha), because RHG55 proves (\beta-1=\varepsilon\le1-\alpha). RHG54a divided by (\alpha), and RHG55a, both bound the same transfer quantity, so their minimum is also valid. Their validity does not turn either into the exact full commutator norm. The rank-two formula RHG33 applies to the whole actual (B_{m,J}), including the finite discrepancy, since its only metric hypothesis is (G)-self-adjointness.

## 9. HG23: finite source action and both boundary terms

The multiplication (S:\mathcal P_N\to\mathcal P_{N+1}) raises the cutoff, and the review keeps that codomain. The canonical retained section has (JC_{\theta,J}=I_E). Hence

\[
 J_{N+1}(SC_{\theta,J}-C_{\theta,J}A)
 =AJC_{\theta,J}-JC_{\theta,J}A=0.
 \tag{RHG56}
\]

Monic division in (\mathcal P_{N+1}) therefore gives the unique literal coefficient map (Q_{\theta,J}) with

\[
 SC_{\theta,J}-C_{\theta,J}A=\chi Q_{\theta,J}.
 \tag{RHG57}
\]

There is no assertion that (S) is an endomorphism of the cutoff space. Its theta primitive is the same original tensor primitive for this exact polynomial relation.

Let (P_{\theta,J}) be the orthogonal projection onto the span of the retained twisted Fourier modes, with their (mathcal K)-valued coefficients. In full types the two observed maps are

\[
 \mathscr R_j=P_{\theta_j,J}\mathcal Z_{L,\theta_j}\mathcal U_k
                      \mathcal V C_{\theta_j,J}:E\to\mathcal H_{\theta_j,J},
 \tag{RHG58}
\]

\[
 \mathscr B_j=P_{\theta_j,J}\mathcal Z_{L,\theta_j}\mathcal U_k
                      \mathcal V(\chi Q_{\theta_j,J}):E\to\mathcal H_{\theta_j,J}.
 \tag{RHG59}
\]

Here (mathcal V) on the second line uses the larger polynomial domain. The source action intertwines (S) with (D^{(k)}); RHG5 intertwines it with (-\partial_r+k/2). Twisted periodization commutes with differentiation on these source columns, and the Fourier projection commutes with this same operator because each retained mode is an eigenfunction. Applying those maps to RHG57 proves

\[
 D_{L,\theta_j}\mathscr R_j-\mathscr R_jA=\mathscr B_j.
 \tag{RHG60}
\]

The retained maps have finite Fourier expansions, so their columns belong to the relevant quasi-periodic first-derivative domain. If (f,g) are two such columns, then

\[
 \langle f(L),g(L)\rangle_{\mathcal K}
 =\langle e^{-i\theta_j}f(0),e^{-i\theta_j}g(0)\rangle_{\mathcal K}
 =\langle f(0),g(0)\rangle_{\mathcal K}.
 \tag{RHG61}
\]

Thus integration by parts has zero endpoint difference and gives (D^*+D=kI) on this domain. Also (\mathscr R_j^*\mathscr R_j=C_{\theta_j,J}^*M_{\theta_j,J}C_{\theta_j,J}=G_{\theta_j,J}). Expanding (\mathscr R_j^*D\mathscr R_j+(D\mathscr R_j)^*\mathscr R_j=kG_{\theta_j,J}) with RHG60 yields

\[
 A^*G_{\theta_j,J}+G_{\theta_j,J}A-kG_{\theta_j,J}
 =-\mathscr R_j^*\mathscr B_j-\mathscr B_j^*\mathscr R_j.
 \tag{RHG62}
\]

Averaging gives HG23. Both ordered terms remain, with minus signs. The vanishing circle endpoint difference does not make the theta-relation boundary orthogonal to its representative. For the actual complex parameter (t),

\[
 H_{m,J}X_{H_{m,J}}
 =A^*H_{m,J}+H_{m,J}A-kH_{m,J}
   +\overline tR^*H_{m,J}+tH_{m,J}R.
 \tag{RHG63}
\]

This supplies exactly the complete finite control form used in HG22, with both residue terms and both theta-relation terms.

## 10. HG24: nonzero residue coefficient and its metric comparison

The unit (e_0) is cyclic under (A): its first (q) iterates are the coefficient basis. Therefore a proper (A)-invariant (F) cannot contain (e_0). The residue pairing (\ell(PQ)) is perfect without a simple-root hypothesis. Indeed, if (P) has degree (j<q) with nonzero leading coefficient, choose (Q=S^{q-1-j}). Then (PQ) has degree exactly (q-1), no reduction occurs, and (\ell(PQ)) is that nonzero coefficient. Equivalently its coefficient matrix is anti-triangular with anti-diagonal entries one and determinant ((-1)^{q(q-1)/2}).

If (\ell|_F=0), invariance gives (\ell(A^jf)=0) for every (j\ge0) and (f\in F). The powers of (A) represent all residue-pairing test polynomials. Perfection forces (f=0), contradicting (F\ne0). Thus (\ell I\ne0). For a positive form (T), both factors in HG24 are consequently strictly positive: a finite-dimensional proper subspace is closed, so the distance of (e_0) to it is positive; and (I^*TI\succ0), so its inverse is strictly positive on the nonzero dual row (\ell I).

If (\alpha G\preceq T\preceq\beta G), evaluate these inequalities on the vector (e_0-Ix) and then minimize over exactly the same (x\in F). This gives

\[
 \alpha d_G\le d_T\le\beta d_G,
 \qquad d_T=\min_x\|e_0-Ix\|_T^2.
 \tag{RHG64}
\]

Restriction to (F) and inverse order give

\[
 \beta^{-1}(I^*GI)^{-1}\preceq(I^*TI)^{-1}
 \preceq\alpha^{-1}(I^*GI)^{-1}.
 \tag{RHG65}
\]

Applying the same fixed row (\ell I) and multiplying the two positive bounds proves HG24. There is no averaging of the nonlinear coefficient. The two applications use ((\alpha,\beta)=(1-\delta^2,1)) and RHG45, respectively.

The source's final period-curvature sentence refers to its separately established period system. Its compatibility can also be checked directly: if (\Pi'=-\Pi(A+tR)/u), (H=\Pi^*\Pi), and (F) is (A)-invariant, then with (V=\Pi I) and the ordinary orthogonal projector (P_V=V(V^*V)^{-1}V^*), the log-determinant identity is

\[
 \partial_t\partial_{\bar t}\log\det(V^*V)
 =\operatorname{tr}((V^*V)^{-1}V'^*(I-P_V)V').
 \tag{RHG66}
\]

It follows by differentiating (V^*V) twice and the formula for the inverse; (V) is holomorphic. The (A I) term in (V') lies in the range of (V), so the projection removes precisely that term. The remainder is (-t\,(I-P_V)\Pi e_0\,\ell I/u). Substitution into RHG66 gives (|t|^2\mathfrak c_F(H)/|u|^2), since the squared norm of ((I-P_V)\Pi e_0) is the minimum quotient norm of the original (e_0). This confirms the exact curvature coefficient and its parameter factors. The period/source metric comparison remains the separately retained comparison of those actual source maps; no bound for it is invented in this bridge.

## 11. HG25: full original-metric Laplacian numerical range

For either actual observation (H\), set (e=\epsilon_H(t)+\|Z+Z^{\dagger_G}\|_G\ge0). RHG25 proves (e\ge\epsilon_G(t)). Replacing the second term by any of its proved larger allowances preserves this conclusion. Retain the full polynomial

\[
 \mathcal L_t=(A+tR)^2-k(A+tR)=T_t^2-k^2I/4.
 \tag{RHG67}
\]

Since (X_G=T_t^{\dagger_G}+T_t), multiply in the displayed order to obtain

\[
 G\mathcal L_t=GX_GT_t-T_t^*GT_t-k^2G/4.
 \tag{RHG68}
\]

For any nonzero original vector (v), keep its actual squared mass (m_v=v^*Gv>0) and put

\[
 z=\frac{v^*G\mathcal L_tv}{m_v},\quad
 r=\frac{\|T_tv\|_G}{\|v\|_G},\quad
 a_1+ib_1=\frac{\langle v,X_GT_tv\rangle_G}{m_v}.
 \tag{RHG69}
\]

These are quotients expressing the numerical-range observable, not a replacement of (v) by a rescaled source vector. Cauchy–Schwarz and (\|X_G\|_G\le e) give

\[
 a_1^2+b_1^2\le e^2r^2.
 \tag{RHG70}
\]

The exact real and imaginary parts of RHG68 are (\operatorname{Re}z=a_1-r^2-k^2/4) and (\operatorname{Im}z=b_1). Since (a_1\le er),

\[
 \operatorname{Re}z
 \le er-r^2-k^2/4
 =\frac{e^2-k^2}{4}-(r-e/2)^2
 \le\frac{e^2-k^2}{4}.
 \tag{RHG71}
\]

The full second identity expands without a missing (k^2) term:

\[
 \begin{aligned}
 e^2\left(\frac{e^2-k^2}{4}-\operatorname{Re}z\right)-b_1^2
 &=e^4/4-e^2a_1+e^2r^2-b_1^2\\
 &=(a_1-e^2/2)^2+e^2r^2-a_1^2-b_1^2\ge0.
 \end{aligned}
 \tag{RHG72}
\]

Together these prove both inequalities of HG25 for every nonzero original vector. If (e=0), then RHG70 gives (a_1=b_1=0) and (\operatorname{Re}z=-r^2-k^2/4); all formulas still hold without division by (e). For any eigenvector (v), the Rayleigh quotient equals its eigenvalue, so every eigenvalue lies in the same region. This argument assumes no normality and does not delete any Jordan block or generalized eigenspace from (E). It establishes no independent small value of (\epsilon_H(t)) simply from writing its finite matrix.

## 12. Coordinate and split-support covariance

For old coordinates (v=Wv') with arbitrary invertible complex (W), the same forms and operators have

\[
 G'=W^*GW,\quad H'=W^*HW,\quad
 B'=W^{-1}BW,\quad T_t'=W^{-1}T_tW,
 \quad x'=W^{-1}x,\quad\ell'=\ell W.
 \tag{RHG73}
\]

Direct inversion gives (y'=(G')^{-1}(\ell')^*=W^{-1}y). The endomorphism (W^{-1}\mathsf SW) squares to (G'^{-1}H'), is (G')-self-adjoint and positive, and hence is its unique positive square root. All commutators, Sylvester solutions, (Z), and control operators therefore transform by this same similarity. The source quotient sections transform by (C'=CW), the quotient map by (J'=W^{-1}J), and their actual relation norms by congruence. These are exact coordinate maps of the existing objects.

The auxiliary maps become (U'=W^{-1}U), (V'=W^{-1}V). Consequently (U'^{\dagger_{G'}}U'=U^{\dagger_G}U) and the analogous equality for (V); all six moments, both Gram determinants, both singular-value squares and their norm are unchanged. For an original vector (v=Wv'), its squared metric mass and Laplacian Rayleigh quotient likewise have exactly the same values. This proves the closing coordinate claim even for nonunitary (W), with no replacement source metric.

Finally, on any retained common support label (\lambda), lift a coefficient map (f) to ((\lambda,v)\mapsto(\lambda,fv)), and send external (\tau) to external (\tau). Composition of these lifts agrees with the lift of composition, the support observation stays (\lambda), and the arithmetic observation is the original coefficient-linear map. If (fv=0), its image is ((\lambda,0)), the receiving supported zero. Inverses and isometries obey the same rule. Thus every coefficient identity and comparison above has the stated exact split-supported map; none substitutes external absence for a represented zero.

## Acceptance and integration scope

Accept all HG1–25 and HG11a at the final source pin stated at the start. Every new displayed estimate has the complete derivation above. The exact source map, full-order packet, analytic weighted source regularity, tensor theta primitive and period system retain their original source dependencies; their roles are explicitly stated rather than supplied by new adjustable assumptions. The two coordinating-task proofs are accurately incorporated and attributed. The mean quotient discrepancy is quadratic, the exact spectral-diameter proof gives its final coefficient one and finite allowance ((\beta-\alpha)/\alpha), the residue norm formula is exact also for singular auxiliary Grams, the finite choices satisfy their inverse domains, the constant (\rho=\xi_J+(1-\xi_J)\varepsilon) is proved, and the finite action retains both relation boundary terms and both complex residue terms. HG25 gives the actual original-metric numerical range with its zero-radius case.

No correction to the mathematical source is requested. The accompanying receipt will bind the whole final source, the complete independent finite-bound review, and this complete proof text. The later cumulative builder must retain these whole bodies and source dependencies; the already promoted 765-page cut remains unchanged.
