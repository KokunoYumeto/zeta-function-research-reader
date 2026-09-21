# The original kernel gap, arithmetic powers, and complete late memory

Independent derivation, 21 September 2026. Equations **KG1–KG42** are the locators in this proof. The complete received source, equations (1)–(36), is retained as `SUPPLIED_KERNEL_GAP.md`. This proof verifies its finite claims, strengthens several bounds, and specifies the scope of its critical limits. No metric, source mass, coordinate, period coefficient, or relation is replaced.

## 1. Original objects, finite source constants, and exact domain

Retain the simple quartet

\[
q=(k+1)^2,\quad k\ge9,\quad k\equiv1\pmod4,\quad
0<\delta<1/2,\quad\gamma>2,\quad R_0=\sqrt{\delta^2+\gamma^2},
\]
\[
S=k/2+iy,\quad Q(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta],
\quad E=\mathbb C[y]/(Q),\quad M[p]=[yp].
\tag{KG1}
\]

The source is the original \(d\mu_k=w_h^{*k}(y)\,dy\), with \(w_h=|(2\xi/h)(1/2+iy)|^2/(2\pi)\). The whole divisor, source mass and polynomial relation space are retained. At \(q-1\le N\le2q\), write \(G_0=G_N\) for the full canonical minimum and \(G_1=G_N^J\) for the complete joint-source minimum. Their exact activation is

\[
G_\alpha^{-1}=(1-\alpha)G_0^{-1}+\alpha G_1^{-1},\qquad0\le\alpha\le1.
\tag{KG2}
\]

Let \(\Lambda:E\to B\) be the unchanged onto observation, \(K=\ker\Lambda\), and

\[
Q_B=(\Lambda G_\alpha^{-1}\Lambda^*)^{-1},\quad
L=G_\alpha^{-1}\Lambda^*Q_B,\quad P_B=L\Lambda.
\tag{KG3}
\]

Multiplication gives \(\Lambda L=I\), \(L^*G_\alpha L=Q_B\), \(P_B^2=P_B=P_B^\dagger\), and \(L^\dagger=\Lambda\). Thus \(L\) is the exact minimum-lift isometry to \(K^{\perp_{G_\alpha}}\). The fixed original coefficient frame is denoted \(I_K:\mathbb C^m\to E\), its inherited Gram is \(K_0=I_K^*G_\alpha I_K\), and its isometric version is \(J_K=I_KK_0^{-1/2}\). In an intrinsic statement on \(K\), the inclusion is an isometry with its inherited metric; in the coefficient frame, the identical gap statement is a comparison with \(K_0\), not with an unrelated identity matrix.

On the original proved five-orbit period locus,
\(m=8k-16\), \(n=q-m=k^2-6k+17\). The complete frame is \(I_K=\mathsf V^{-1}\pi^T\), with \(\ker\pi=\operatorname{im}[M_A,S_kZ_k]\); the transpose is complex-linear duality. These are [MR1–8](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/ORIGINAL_KERNEL_MIXED_DETERMINANT.tex#L30). Its verified period domain, including \(|u|\ge R_*\), is recorded in [NG24](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/NATIVE_GAUSSIAN_TRANSFER.tex#L482). All asymptotic rank uses below retain that domain; none assigns the five-orbit rank on a size-one orbit.

Here are the precise source bounds used. Put \(U_sd=\sum_{j=1}^sd_j[y^{-j}]\), \(V_s=\operatorname{im}U_s\). The proved all-activation comparison [HAR7–12, HAR26–31](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L78) gives

\[
U_s^*\Lambda^*Q_B\Lambda U_s\succeq\ell_{s,N}U_s^*G_\alpha U_s,
\quad \ell_{s,N}=e^{-2E_{s,N}}\in(0,1],
\]
\[
E_{s,N}=O_{h,\varpi}\bigl(k\log^2(q+2)+(k+Js)\log(q+Js+2)\bigr).
\tag{KG4}
\]

Here \(J\) is the number of actual nonzero conductor coefficients; \(\varpi\) denotes the fixed original period data, not a freely selected replacement. For a finite value use exactly
\(E_{s,N}=\max(0,-\log L_{s,N},\log U_{s,N})\),
\(L_{s,N}=a_{s,N}/\max(1,\mathbf L_k\Gamma_N)\),
\(U_{s,N}=b_{s,N}+\mathbf B_kA_w^k/(R_0^2-1)\),
with \(a_{s,N},b_{s,N}\) the original finite IVO constants, \(\Gamma_N\) the explicit HAR20 cardinal constant, and \(A_w^k\) the actual total tensor weight. HAR10 and HAR19–26 define all these finite quantities; no limiting constant is used to stand in for them.

The finite guards, [HAR11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L112), are

\[
\begin{gathered}
1\le s\le q,\quad q_-=(k-7)^2\ge16,\quad kR_0\le2^{-14}q_-,\\
n_-+2\le2q_-,\quad\mathcal L_*\mathcal R_*T_N^{\rm lb}\ge2\mathcal A,
\quad n_-=N-v+Js-q_-.
\end{gathered}
\tag{KG5}
\]

The last inequality uses an actual nonzero selected conductor coefficient and its complete pole numerator, exactly as in IVO24; all original invariant constraints remain. IVO24–26 proves these guards eventually for fixed original data and \(s\log(q+2)=o(q)\). Small algebraic fixtures below do not assert these eventual guards.

The full-polynomial canonical comparison is
\(\ell_{k,N}\|p\|_\sigma^2\le\|p\|_{\mu_k}^2\le u_k\|p\|_\sigma^2\), with the original Gamma mass \(\sqrt{2\pi}\). Anchored division on polynomials through degree \(N\) has Gamma norm at most
\(\mathfrak d_N=2\sqrt{2N+1}(\sum_{j=1}^N1/j)(1+\sqrt{N+1})\). The joint metric satisfies
\(\mathbf L_k^{-1}T_k\preceq G_1\preceq\mathbf B_kT_k\), with \(T_k\) diagonal in the exact original root-value coordinates. These statements and their proofs are [ACT3–9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/ACTION_PROOFS.md#L81) and [HAR5–6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L60). Their logarithmic losses are \(O_{h,\varpi}(k\log^2(q+2))\). The Gamma recurrence and source comparison retain the human-source attribution in those proofs; no new analytic-source asymptotic is claimed here.

## 2. Exact inverse transport and a sharp kernel gap

Let \(\widehat R_N:E\to\mathcal P_N\) be the complete canonical minimum section, \(J_N\) the remainder map, \(\mathscr Dp=(p-p(0))/y\), and \(u=[y^{-1}]\). All roots of \(Q\) have modulus at least \(R_0>2\), so \(M\) and this class are defined. Multiplication modulo the full \(Q\) proves

\[
M^{-1}=B_{1,0}+u\lambda_{1,0},\quad
B_{1,0}=J_N\mathscr D\widehat R_N,
\quad\lambda_{1,0}(x)=(\widehat R_Nx)(0).
\tag{KG6}
\]

In particular \(\lambda_{1,0}\) evaluates the specified lift, not a purported quotient evaluation at zero. For general \(1\le s\le q\), writing a polynomial as its first \(s\) Taylor coefficients plus \(y^s\mathscr D^sp\) proves

\[
M^{-s}=B_{s,0}+U_sR_{s,0},\quad
B_{s,0}=J_N\mathscr D^s\widehat R_N,\quad
(R_{s,0}x)_j=[y^{s-j}]\widehat R_Nx,\quad1\le j\le s.
\tag{KG7}
\]

Every division is applied to a polynomial at the original cutoff; no degree-increased source is introduced.

Define the actual coisometry
\(\mathcal C_\alpha(x_0,x_1)=\sqrt{1-\alpha}\,x_0+\sqrt\alpha\,x_1\) from \(E_{G_0}\oplus E_{G_1}\) to \(E_{G_\alpha}\). Its adjoint is
\((\sqrt{1-\alpha}G_0^{-1}G_\alpha x,\sqrt\alpha G_1^{-1}G_\alpha x)\), and KG2 gives \(\mathcal C_\alpha\mathcal C_\alpha^\dagger=I\). For any fixed coefficient operator \(T\),
\(T=\mathcal C_\alpha\operatorname{diag}(T,T)\mathcal C_\alpha^\dagger\), so \(\|T\|_{G_\alpha}\le\max(\|T\|_{G_0},\|T\|_{G_1})\). Applying this identity to KG7 yields exactly

\[
\begin{split}
M^{-s}&=B_{s,\alpha}+U_sR_{s,\alpha},\\
B_{s,\alpha}&=(1-\alpha)B_{s,0}G_0^{-1}G_\alpha
 +\alpha M^{-s}G_1^{-1}G_\alpha,\\
R_{s,\alpha}&=(1-\alpha)R_{s,0}G_0^{-1}G_\alpha,
\end{split}
\]
\[
\|B_{s,\alpha}\|\le D_s:=
\max\left\{1,\mathfrak d_N^s\sqrt{u_k/\ell_{k,N}},
\sqrt{\mathbf L_k\mathbf B_k}\,R_0^{-s}\right\}.
\tag{KG8}
\]

The first bound follows because \(J_N\) is a contraction and \(\widehat R_N\) is an isometry, applying source comparison before and after \(s\) polynomial divisions. In \(T_k\), the operator \(M^{-s}\) is diagonal, of norm \(R_0^{-s}\). The joint sandwich gives the second bound. The norm of the coisometry and its adjoint is one. Thus KG8 includes both endpoints \(\alpha=0,1\), with the exact factor order and rank at most \(s\).

Here is the underlying subspace statement. If \(V\subset E\) satisfies \(\|P_Bv\|^2\ge\ell\|v\|^2\) for all \(v\in V\), then \(\|P_K|_V\|\le\sqrt{1-\ell}\). Its adjoint is \(P_V|_K\), so the same bound holds there. Orthogonal decomposition gives

\[
\|(I-P_V)x\|\ge\sqrt\ell\|x\|\quad(x\in K).
\tag{KG9}
\]

Apply this to \(V_s\) using KG4. Since \((I-P_{V_s})U_s=0\), applying KG8 to \(M^sx\) gives
\((I-P_{V_s})x=(I-P_{V_s})B_{s,\alpha}M^sx\). Hence

\[
\boxed{\|M^sx\|\ge e^{-E_{s,N}}D_s^{-1}\|x\|\quad(x\in K).}
\tag{KG10}
\]

For \(s=1\), put \(D_-=D_1\), \(\ell_N=\ell_{1,N}\), \(a_N=\ell_N/D_-^2\). In the original metric,

\[
\boxed{J_K^\dagger M^\dagger MJ_K\succeq a_NI_m,
\qquad I_K^*M^*G_\alpha MI_K\succeq a_NK_0,
\quad -\log a_N=O_{h,\varpi}(k\log^2(q+2)).}
\tag{KG11}
\]

The full action is used. In its original orthogonal blocks the left side is \(M_K^\dagger M_K+C_0^\dagger C_0\), including the leakage \(C_0:K\to B\). No inequality for \(M_K\) alone follows. For instance the invertible swap matrix, with \(K=\mathbb Ce_1\), has \(M_K=0\) but \(M^\dagger M=I\).

The constant \(\ell/D_-^2\) is sharp with only the given angle and residual data. In a declared Euclidean fixture, let \(u=e_1\), \(K=\mathbb R(4/5,3/5)\),
\(M^{-1}=\left(\begin{smallmatrix}2&4/3\\0&1\end{smallmatrix}\right)=\operatorname{diag}(0,1)+u(2,4/3)\). Here \(D_-=1\), the observed fraction of \(u\) is \(\ell=9/25\), and \(M(4/5,3/5)=(0,3/5)\); equality holds in KG11. This fixture also shows why no separation guard is necessary for the proof.

KG11 strengthens the canonical singular-line guard in [ME27–29](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d44d94aa43d0a1934455ddac008368583f43a2c1/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/MEMORY_ENERGY_PROOFS.md) and extends its gap to every activation. Its finite requirements are exactly the original harmonic guards KG5, not a new assumed gap. The full quotient's scale \(\exp[-2q\log(q/k)+O(q)]\) is a canonical or fixed/bounded critical-parameter assertion. It is not uniform over \(0\le\alpha\le1\): at \(\alpha=1\), \(\|M^{-1}\|\le\sqrt{\mathbf L_k\mathbf B_k}/R_0=e^{o(q)}\). The kernel gap itself remains uniform there.

## 3. Complete word volumes in the original coefficient frame

The original outgoing decomposition is \(M=C_N+r_N\ell_N^{\rm top}\), with \(\|C_N\|\le C_{\rm pol}(N)\), \(\|r_N\ell_N^{\rm top}\|=\varepsilon_N\); it is selfadjoint only in \(G_0\). Transporting its bounded and rank-one parts by the coisometry proves

\[
s_1(M;G_\alpha)\le L_+,\qquad s_j(M;G_\alpha)\le D_+\quad(j\ge2),
\]
\[
D_+=\max\{1,C_{\rm pol}(N),\sqrt{\mathbf L_k\mathbf B_k}\,kR_0\},
\quad L_+=\max\{D_+,C_{\rm pol}(N)+\varepsilon_N\}.
\tag{KG12}
\]

Indeed the transported bounded part has norm at most \(D_+\) and the remaining term still has rank at most one. On its row kernel, singular min–max gives \(s_2\le D_+\). For \(s_1\), apply the coisometry to the complete \(M\); its canonical norm is at most \(C_{\rm pol}+\varepsilon_N\), and its joint norm is at most \(\sqrt{\mathbf L_k\mathbf B_k}kR_0\). Thus the stated maximum, rather than an unproved sum estimate, is valid. The original profile H5 and source constants give
\(\log L_+=O_{h,\varpi}(q)\), \(\log D_+=O_{h,\varpi}(k\log^2(q+2))\). No selfadjointness of the transported bounded part is asserted.

Let \(H=M^\dagger M\),
\(K_s^M=(M^sI_K)^*G_\alpha(M^sI_K)\), and
\(K_j^H=(H^jI_K)^*G_\alpha(H^jI_K)\). Put
\(D_*:=2\log L_++2(m-1)\log D_+\). Then

\[
\boxed{-2m(E_{s,N}+\log D_s)
\le\log\frac{\det K_s^M}{\det K_0}\le sD_*.}
\tag{KG13}
\]

The lower bound follows from KG10 by positive congruence. For the upper bound, in orthonormal singular frames \(\|\wedge^mM\|=\prod_{i=1}^ms_i(M)\le L_+D_+^{m-1}\). The identity \(\wedge^m(M^s)=(\wedge^m M)^s\) and submultiplicativity give the upper bound. The squared norm of \(\wedge^m(M^sJ_K)\) is exactly \(\det K_s^M/\det K_0\), so the fixed coefficient frame has not been changed.

For a unit \(x\in K\), write its spectral weights for \(H\) as \(p_i\). Convexity of \(t\mapsto t^{2j}\) on \([0,\infty)\), and KG11, imply
\(\langle x,H^{2j}x\rangle=\sum p_i\lambda_i^{2j}\ge(\sum p_i\lambda_i)^{2j}\ge a_N^{2j}\). For the upper bound the singular values of \(H^j\) are \(s_i(M)^{2j}\). Thus

\[
\boxed{2mj\log a_N\le\log\frac{\det K_j^H}{\det K_0}\le2jD_*.}
\tag{KG14}
\]

Equations (8) and (9) of the arrival are KG13 at \(s=1\) and KG14 at \(j=1\). Their \(K_1\) is \(K_1^M\) and their \(K_2\) is \(K_1^H\); this distinction prevents confusing \(H\) with \(M^2\).

More generally, for any positive integer bound \(r_k\) such that

\[
\frac{r_k\log^2(q+2)}{k}\longrightarrow0,
\tag{KG15}
\]

KG13–14 are \(o(kq)\), uniformly for \(1\le s,j\le r_k\), in \(N\) and \(\alpha\). To verify each term, \(m=O(k)\), \(q\asymp k^2\), \(D_*=O(q+k^2\log^2q)\), \(\log\mathfrak d_N=O(\log q)\), and
\(\log D_s=O(k\log^2q+s\log q)\). Since KG15 implies \(s=o(k)\), KG4 gives \(E_{s,N}=O(k\log^2q)\). The lower side of KG13 is \(O(k^2\log^2q+ks\log q)=o(kq)\); its upper side and both sides of KG14 are \(O(r_k(q+k^2\log^2q))=o(kq)\). Also \(r_k\log q=o(q)\), so every finite source guard is eventually satisfied. The received choice \(\max(1,\lfloor k/\log^3(q+2)\rfloor)\) satisfies KG15.

Taking the four original signs therefore proves that the returns of \(K_s^M\) and \(K_j^H\) differ from the return of \(K_0\) by \(o(kq)\). The estimate is uniform even if the four activations are chosen independently. It concerns precisely these two families of words; no bound for every possible noncommuting word is inferred.

There is an exact quotient action. For any invertible original coefficient operator \(T\), use \(\Lambda T^{-1}\) as coordinates on \(E/TK\). Then \(\overline T:E/K\to E/TK\) has coordinate matrix identity, with source metric \(Q_B\) and target metric
\(Q_T=(\Lambda T^{-1}G_\alpha^{-1}T^{-*}\Lambda^*)^{-1}\). Two full Gram eliminations, or completion of the energy square on the original kernel, give

\[
\boxed{\log\det(\overline T^\dagger\overline T)
=\log\frac{\det Q_T}{\det Q_B}
=2\log|\det T|-\log\frac{\det(I_K^*T^*G_\alpha TI_K)}{\det K_0}.}
\tag{KG16}
\]

For detail, choose any complement frame \(F\) with \(\Lambda F=I\). The determinant of \([I_K,F]^*G[I_K,F]\) is \(\det K_0\det Q_B\). Replacing \(G\) by \(T^*GT\) changes its determinant by \(|\det T|^2\), its kernel factor to the one in KG16, and its quotient factor to \(Q_T\). Cancel the same frame determinant. For \(T=M^s\), the first term is \(2s\log|Q(0)|\), independent of cutoff, and cancels under the four signs. For \(T=H^j\) it is \(4j\log|Q(0)|\), again independent of cutoff although the adjoint in \(H\) depends on the metric. Both induced quotient actions have zero leading \(kq\) return in KG15. The map is not \((\Lambda ML)^s\), whose intermediate projections are absent from this exact quotient construction.

## 4. Complete energy and the derivative mass

Use \(K\oplus LB\), with its inherited metrics, and write

\[
H=\begin{pmatrix}A&B_H\\B_H^\dagger&D_H\end{pmatrix}>0,
\quad A\succeq a_NI,
\quad F(z)=zI+D_H-B_H^\dagger(A+zI)^{-1}B_H.
\tag{KG17}
\]

Here \(A=M_K^\dagger M_K+C_0^\dagger C_0\),
\(B_H=M_K^\dagger D_0+C_0^\dagger M_B\),
\(D_H=D_0^\dagger D_0+M_B^\dagger M_B\). Every coupling block is retained. Block elimination gives \(F(z)^{-1}=\Lambda(H+zI)^{-1}L\) whenever the inverses exist.

The general Schur construction and reconstruction map are presented by Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, *The Feshbach–Schur map and perturbation theory* (2021), [original author TeX, arXiv:2105.02058v1](https://arxiv.org/src/2105.02058v1), theorem `thm:isospF`, reconstruction equation `QP`, and proposition `prop:U-prop-SA`. Its intact original source was retained for RM18–26 in the preceding edition; its complete source lines 398–507 were reread for the present proof. The identities and activated finite estimates KG17–38 are proved here; the human source is credited for the general construction, not asserted to supply these new constants or their original arithmetic receivers.

Put

\[
S=F(0)=D_H-B_H^\dagger A^{-1}B_H>0,
\qquad W=F'(0)=I+B_H^\dagger A^{-2}B_H\succeq I.
\tag{KG18}
\]

With \(\mathcal E=L-J_KA^{-1}B_H\), where \(B_H\) is the map from the original observed Hilbert space to the isometric kernel, direct multiplication and completion of the quadratic square prove
\(\Lambda\mathcal E=I\), \(\mathcal E^\dagger\mathcal E=W\), \(\mathcal E^\dagger H\mathcal E=S\). Thus

\[
\mathcal J=\mathcal EW^{-1/2},\quad
\mathcal J^\dagger\mathcal J=I,\quad H_{\rm eff}=\mathcal J^\dagger H\mathcal J=W^{-1/2}SW^{-1/2}.
\tag{KG19}
\]

These are identities between the original observed metric and the original full metric. In arbitrary observed coefficient coordinates, the intrinsic endomorphisms \(S,W\) have coefficient Grams \(Q_BS,Q_BW\), and their adjoints use \(Q_B\). Under the exact isometry \(b\mapsto Q_B^{1/2}b\), their Euclidean Hermitian matrices are \(S_o=Q_B^{1/2}SQ_B^{-1/2}\), \(W_o=Q_B^{1/2}WQ_B^{-1/2}\). The same coefficient Grams are consequently \(Q_B^{1/2}S_oQ_B^{1/2}\) and \(Q_B^{1/2}W_oQ_B^{1/2}\). The intrinsic positive square root of \(W\) is transported from that of \(W_o\). These formulas record every coordinate factor in the incoming inclusion notation.

Let \(K_1=K_1^M\), \(K_2=K_1^H\). Since the kernel block of \(H^2\) is \(A^2+B_HB_H^\dagger\), the rectangular determinant identity gives

\[
\boxed{\det W=\frac{\det K_2\det K_0}{(\det K_1)^2},\quad
\det S=|Q(0)|^2\frac{\det K_0}{\det K_1},\quad
\det H_{\rm eff}=|Q(0)|^2\frac{\det K_1}{\det K_2}.}
\tag{KG20}
\]

Indeed \(\det A=\det K_1/\det K_0\), \(\det(J_K^\dagger H^2J_K)=\det K_2/\det K_0\), and
\(\det W=\det(A^2+B_HB_H^\dagger)/(\det A)^2\). The identity \(\det(I+UV)=\det(I+VU)\) follows by eliminating either diagonal block of \(\left(\begin{smallmatrix}I&U\\-V&I\end{smallmatrix}\right)\). Full elimination gives \(\det H=\det A\det S=|\det M|^2=|Q(0)|^2\). These prove every factor in KG20, agreeing with [ME30–33](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d44d94aa43d0a1934455ddac008368583f43a2c1/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/MEMORY_ENERGY_PROOFS.md) and [BR1–6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d44d94aa43d0a1934455ddac008368583f43a2c1/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/PROGRAMME_RECEIVERS.md).

A stronger bound than incoming (16) follows from the exact isometry \(V=H^{1/2}J_KA^{-1/2}\). Multiplication gives \(V^\dagger V=I\) and
\(\det(V^\dagger HV)=\det A\det W\). For any \(m\)-dimensional isometry \(J\), singular min–max and KG12 give \(\det(J^\dagger HJ)\le L_+^2D_+^{2(m-1)}\). Hence

\[
\boxed{0\le\log\det W\le D_* -\log\det A\le D_*+m\log(1/a_N)
=O_{h,\varpi}(q+k^2\log^2(q+2))=o(kq).}
\tag{KG21}
\]

For completeness, incoming (16) is valid: \(H\) equals a rank-one top-eigenvalue term plus a positive remainder of norm at most \(D_+^2\); so its cross block has a rank-one part and remainder of norm at most \(D_+^2\). Left multiplication by \(A^{-1}\) bounds its second and later singular values by \(D_+^2/a_N\), and its first by \(L_+^2/a_N\). Only \(\rho=\operatorname{rank}B_H\) values are nonzero, giving exactly that expression with \(\rho=0\) interpreted as zero. Positivity also yields the sharper norm bound

\[
\boxed{\|W\|\le1+L_+^2/a_N.}
\tag{KG22}
\]

To prove it, \(B_H^\dagger A^{-1}B_H\preceq D_H\), while \(A^{-2}\preceq a_N^{-1}A^{-1}\). Therefore \(W-I\preceq a_N^{-1}D_H\preceq (L_+^2/a_N)I\). The received larger bound \(1+L_+^4/a_N^2\) remains valid.

Every restriction and attained quotient of the mass metric has cost between zero and \(\log\det W\), relative to the corresponding restriction or quotient of its original base metric. For a restriction, pass by its exact base-metric isometry to \(J^\dagger WJ\). Its eigenvalues are at least one and bounded by the corresponding leading eigenvalues of \(W\); their logarithmic sum is at most \(\log\det W\). For an attained quotient, use the same kernel-complement Gram elimination as in KG16: the full cost is the sum of the nonnegative kernel restriction cost and quotient cost. Iteration covers a restriction followed by a quotient. This proves the statement with the required base metrics and fixed coefficient maps, not an absolute determinant bound for arbitrarily rescaled frames.

KG13–14 and KG20–21 give \(\mathcal R\log\det S=o(kq)\), \(\mathcal R\log\det W=o(kq)\), and \(\mathcal R\log\det H_{\rm eff}=o(kq)\), uniformly in activation. The kernel's initial \(kq\) coefficient is not assigned by these distortion identities.

## 5. All-activation memory down to zero

Define the full memory logarithm
\(g(z)=\log\det(zI+A)+\log\det(zI+D_H)-\log\det(zI+H)\). Since \(H>0\), all three matrices remain positive at zero. With
\(\mathcal Q(t)=\operatorname{Tr}e^{-tH}-\operatorname{Tr}e^{-tA}-\operatorname{Tr}e^{-tD_H}\), scalar Jensen in concatenated eigenbases of \(A,D_H\) gives \(\mathcal Q(t)\ge0\). Taylor expansion gives \(\mathcal Q(t)=t^2\|B_H\|_{\rm HS}^2+O(t^3)\), while the finite positive matrices give exponential decay at infinity. Pairing their scalar eigenvalue integrals proves
\(g(z)=\int_0^\infty e^{-zt}\mathcal Q(t)dt/t\), including zero, and \(0\le g(z)\le g(0)\).

Let \(L_-\ge\|M^{-1}\|\), \(L_-\ge D_-\), with every remaining singular value of \(M^{-1}\) at most \(D_-\), as KG8 at \(s=1\) proves. Eliminating \(D_H\) gives
\(g(0)=\log\det A+\log\det((H^{-1})_{KK})\). Restriction min–max for \(H\) and \(H^{-1}\) therefore proves

\[
\boxed{0\le g(z)\le g(0)
\le2\log(L_+L_-)+2(m-1)\log(D_+D_-),\quad z\ge0.}
\tag{KG23}
\]

One finite all-activation choice is \(L_-=\max(D_-,\|M^{-1}\|_{G_0},\|M^{-1}\|_{G_1})\); the coisometry proves its validity. ACT10–14 and the retained scalar endpoints give \(\log L_-\le q\log(q/k)+O_{h,\varpi}(q)\), uniformly in \(N\). Consequently

\[
\boxed{\sup_{N,\alpha\in[0,1],z\ge0}g_{N,\alpha}(z)
=O_{h,\varpi}(q\log(q/k)+k^2\log^2(q+2))=o(kq).}
\tag{KG24}
\]

This is an additional all-activation extension of the canonical bound ME20. It uses both actual inverse and outgoing decompositions; it does not estimate \(q\) bounded singular directions by \(D_+\). It keeps the entire heat-memory integral at zero. It does not delete the separate leakage term of ME21–26 or turn the independently compressed \(M_B\) into the complete Schur action.

## 6. Relative low-frequency comparison and every memory moment

The scalar resolvent identity on the positive kernel block, followed by the full \(B_H\)-congruence, gives exactly

\[
F(z)=S+zW-z^2B_H^\dagger A^{-2}(A+zI)^{-1}B_H.
\tag{KG25}
\]

For real \(z\ge0\), write it instead as
\(F(z)=S+zI+zB_H^\dagger A^{-2}[A(A+zI)^{-1}]B_H\). The bracket lies between \((1+z/a_N)^{-1}I\) and \(I\), so

\[
\boxed{S+zI+\frac{z}{1+z/a_N}(W-I)
\preceq F(z)\preceq S+zW.}
\tag{KG26}
\]

The left side is at least \((S+zW)/(1+z/a_N)\), proving incoming (20) with a stronger intermediate lower bound. The nonnegative difference \(S+zW-F(z)\) has rank at most \(\rho\). Congruence by \((S+zW)^{-1/2}\) shows that at most \(\rho\) eigenvalues differ from one and that each lies in \([(1+z/a_N)^{-1},1]\). Thus

\[
\boxed{0\le\log\det(S+zW)-\log\det F(z)
\le\rho\log(1+z/a_N).}
\tag{KG27}
\]

Inverting KG26 and conjugating by \(W^{1/2}\) proves exactly

\[
\boxed{(zI+H_{\rm eff})^{-1}
\preceq W^{1/2}\Lambda(zI+H)^{-1}LW^{1/2}
\preceq(1+z/a_N)(zI+H_{\rm eff})^{-1}.}
\tag{KG28}
\]

All these finite estimates include \(z=0\). The heat measurements derived below use this actual mass rather than treating the pencil as \(zI+S\).

For every integer \(p\ge1\) and complex \(|z|<a_N\), the finite geometric identity gives

\[
F(z)=S+zW+\sum_{j=2}^p(-1)^{j+1}z^jB_H^\dagger A^{-(j+1)}B_H+R_p(z),
\]
\[
R_p(z)=(-1)^pz^{p+1}B_H^\dagger A^{-(p+1)}(A+zI)^{-1}B_H,
\quad
\boxed{\|W^{-1/2}R_p(z)W^{-1/2}\|
\le\frac{|z|^{p+1}}{a_N^p(1-|z|/a_N)}.}
\tag{KG29}
\]

For the norm bound, move one factor \(A^{-1}\) to each side of the middle kernel operator. Its norm is at most \(a_N^{-(p-1)}/(a_N-|z|)\), while
\(W^{-1/2}B_H^\dagger A^{-2}B_HW^{-1/2}=I-W^{-1}\preceq I\). This proves the full complex remainder without commuting \(B_H\) with \(A\).

Diagonalizing only \(A\) proves for the exact memory \(\mathcal M(t)=B_H^\dagger e^{-tA}B_H\) and every integer \(j\ge0\),

\[
\boxed{\int_0^\infty t^j\mathcal M(t)dt=j!B_H^\dagger A^{-(j+1)}B_H,\qquad
\int_T^\infty\mathcal M(t)dt\preceq e^{-a_NT}B_H^\dagger A^{-1}B_H.}
\tag{KG30}
\]

The scalar integral follows by repeated integration by parts. Thus \(W-I\) is the first time moment. The pencil's kernel poles are at negatives of eigenvalues of \(A\), all of magnitude at least \(a_N\); the much smaller full-system pole, when present, arises from the zero of the complete Schur pencil, not an omitted kernel eigenvalue.

## 7. Exact soft-mode mass, energy and heat

The rank-one inverse decomposition implies \(\lambda_2(H)\ge D_-^{-2}\). Let \(\lambda=\lambda_1(H)\) and retain the explicit guard

\[
\lambda<a_N=\ell_N/D_-^2\le D_-^{-2}.
\tag{KG31}
\]

This makes the smallest eigenvalue simple. Write its unit eigenvector as \(\psi=(x,b)\in K\oplus LB\), and \(\theta=\|b\|_{Q_B}^2\). Necessarily \(b\ne0\), since \(A\succeq a_NI\). The first block equation gives
\(-A^{-1}B_Hb=(I-\lambda A^{-1})x\). Hence

\[
\boxed{w_b:=b^\dagger Wb
=1-2\lambda\langle x,A^{-1}x\rangle+\lambda^2\langle x,A^{-2}x\rangle,
\quad(1-\lambda/a_N)^2\le w_b\le1.}
\tag{KG32}
\]

Both inequalities follow from the spectrum of \(I-\lambda A^{-1}\) lying in \([1-\lambda/a_N,1]\) and \(\|x\|^2+\|b\|^2=1\). Thus on the unit observed vector \(b/\sqrt\theta\), the mass is exactly \(w_b/\theta\), between \((1-\lambda/a_N)^2/\theta\) and \(1/\theta\). This proves incoming (25)–(26) with explicit relative constants.

The full spectral resolution, compressed by \(\Lambda,L\), gives
\(S^{-1}=\lambda^{-1}bb^\dagger+R\), \(0\preceq R\preceq D_-^2I\). Taking its maximum eigenvalue and inverting proves

\[
\boxed{\frac{\lambda}{\theta+\lambda D_-^2}
\le\lambda_{\min}S\le\frac\lambda\theta.}
\tag{KG33}
\]

The graph isometry gives \(\nu_i:=\lambda_i(H_{\rm eff})\ge\lambda_i(H)\), by the minimum principle. At the actual pole, \(F(-\lambda)b=0\) and
\(S=F(-\lambda)+\lambda[I+B_H^\dagger A^{-1}(A-\lambda I)^{-1}B_H]\). The bracket lies between \(W\) and \((1-\lambda/a_N)^{-1}W\). Insert \(b\) into the corresponding generalized Rayleigh quotient to obtain

\[
\boxed{\lambda\le\nu_1\le\frac{\lambda}{1-\lambda/a_N},\qquad
\nu_2\ge D_-^{-2}\quad(n\ge2).}
\tag{KG34}
\]

This agrees with the stronger all-index and multiplicity theorem [RM24–31](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d44d94aa43d0a1934455ddac008368583f43a2c1/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/REDUCED_MODEL_PROOFS.md). The present advance is the explicit all-activation kernel gap, not a new claim that the prior all-index eigenvalue theorem was unavailable.

Let \(Y(\tau)=\Lambda e^{-\tau H}L\), \(\tau\ge0\). Its spectral expansion and KG32 show

\[
\boxed{\left|\operatorname{Tr}(WY(\tau))-e^{-\tau\lambda}\right|
\le(1-w_b)e^{-\tau\lambda}
 +(\operatorname{Tr}W-w_b)e^{-\tau/D_-^2}.}
\tag{KG35}
\]

Indeed the sum of all fast observed weighted coefficients is exactly \(\operatorname{Tr}W-w_b\): the compressed full resolution of the identity is \(I_B\). Moreover \(1-w_b\le2\lambda/a_N-(\lambda/a_N)^2\le2\lambda/a_N\), and \(\operatorname{Tr}W-w_b\le(q-1)\|W\|\), yielding incoming (29). This proves the stronger finite tail with every mode counted. The raw observed soft coefficient remains \(\theta\), while the mass-weighted coefficient is \(w_b\); neither is assigned value one at finite size.

For effective heat, min–max gives \(\operatorname{Tr}e^{-\tau H}\ge\operatorname{Tr}e^{-\tau H_{\rm eff}}\). Pairing the first eigenvalues and discarding negative fast differences gives

\[
\boxed{0\le\operatorname{Tr}e^{-\tau H}-\operatorname{Tr}e^{-\tau H_{\rm eff}}
\le\frac{\lambda/a_N}{e(1-\lambda/a_N)}+(q-1)e^{-\tau/D_-^2}.}
\tag{KG36}
\]

For the first term, \(e^{-\tau\lambda}-e^{-\tau\nu_1}\le\tau(\nu_1-\lambda)e^{-\tau\lambda}\), followed by KG34 and \(\sup_{t\ge0}te^{-t}=1/e\). If desired, its exact optimized bound is \(r(1-r)^{(1-r)/r}\), \(r=\lambda/a_N\in(0,1)\): maximize \(e^{-t}-e^{-t/(1-r)}\) at \(t=-(1-r)\log(1-r)/r\). This is at most the displayed bound and keeps its uniformity in \(\tau\).

## 8. The complete observed critical determinant and heat

Block elimination at \(z\) and at zero gives the exact same-cutoff ratio

\[
\boxed{\log\frac{\det F(z)}{\det F(0)}
=\log\det(I+zH^{-1})-\log\det(I+zA^{-1}),\qquad z\ge0.}
\tag{KG37}
\]

There is only one inverse energy eigenvalue above \(D_-^2\); all \(m\) kernel inverse eigenvalues are at most \(a_N^{-1}\). Consequently

\[
\boxed{-m\log(1+z/a_N)\le
\log\frac{\det F(z)}{\det F(0)}-\log(1+z/\lambda)
\le(q-1)\log(1+zD_-^2).}
\tag{KG38}
\]

No \(\lambda<a_N\) guard is needed for KG37–38. Also
\(\det(S+zW)/\det S=\det(I+zH_{\rm eff}^{-1})\), so KG27 compares this effective determinant with KG37 with error at most \(\rho\log(1+z/a_N)\). This is a cancellation in a same-cutoff ratio, with the mass determinant KG20–21 retained separately.

For the critical limit, let \(\ell_k=\log(q/k)\), and use fixed real \(\zeta,b\), or bounded parameter sets with strict heat gaps bounded away from zero. Put
\(\alpha_k(\zeta)=e^{-2q\ell_k-\zeta q}\),
\(z_k(b)=e^{-2q\ell_k-bq}\), \(\tau_k(b)=z_k(b)^{-1}\). These activations lie in \([0,1]\) eventually; their exact physical domain is \(\zeta\ge-2\ell_k\). The finite harmonic theorem is uniform on the larger domain, but the following ultrasmall-scale and heat assertions have the fixed/bounded parameter scope just stated.

The retained analytic endpoint theorem, [HAR41–47](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L461), and the independently proved original inverse norm [ACT10–19](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/ACTION_PROOFS.md#L152), give

\[
-\log\lambda_{N,L/H}=2q\ell_k+\kappa_{L/H}(\zeta)q+o(q),\quad
\kappa_T(\zeta)=\min(\beta_T,\zeta),
\]
\[
\beta_L=-2-I_\square+2a_0,\quad a_0=\log(4/\pi),\quad
\beta_H=\beta_L-C_\partial/2,
\]
\[
I_\square=\log(\delta^2+\gamma^2)-3
 +(\delta/\gamma)\arctan(\gamma/\delta)+(\gamma/\delta)\arctan(\delta/\gamma).
\tag{KG39}
\]

The high-endpoint monic-profile/zero-law theorem has its retained analytic status. No new native moment evaluation is asserted. At this scale, \(z_k/a_N\) and \(z_kD_-^2\) are bounded above by \(\exp[-2q\ell_k+O_{h,\varpi,b}(q)]\), as are the two errors in KG38 after their polynomial dimension factors. They may vanish; these are upper bounds, not asymptotic equalities to a nonzero error.

The inequality \(0\le\log(1+e^x)-[x]_+\le\log2\), and the 1-Lipschitz property of \([x]_+\), prove, including equality at thresholds,

\[
\boxed{\frac1q\mathcal R\log\frac{\det F_N(z_k(b))}{\det F_N(0)}
\longrightarrow2[(\kappa_L(\zeta)-b)_+-(\kappa_H(\zeta)-b)_+].}
\tag{KG40}
\]

The identical limit holds for \(q^{-1}\mathcal R\log\det(I+z_k(b)H_{{\rm eff},N}^{-1})\), by KG27. Here \(\mathcal R\) has the unchanged signs \(+,+,-,-\) at \(q-1,q,2q-1,2q\); the two endpoints of each type have the same leading exponent, not necessarily equal finite matrices.

For heat, \(\lambda/a_N=\exp[-2q\ell_k+O(q)]\to0\), proving KG31 eventually. Also \(\log\|W\|=O(q)\) by KG22, while \(\tau_k/D_-^2=\exp[2q\ell_k+bq-o(q)]\). Thus every fast term in KG35–36 tends to zero, including its mass factor. The soft factor is
\(e^{-\tau_k\lambda}=\exp[-\exp(q(b-\kappa_T)+o(q))]\). Therefore

\[
\boxed{\mathcal R\operatorname{Tr}(W_NY_N(\tau_k(b)))\to2,
\qquad\mathcal R\operatorname{Tr}e^{-\tau_k(b)H_{{\rm eff},N}}\to2
\quad\text{if }\kappa_H<b<\kappa_L.}
\tag{KG41}
\]

Both limits are zero on \(b<\kappa_H\) and on \(b>\kappa_L\): in the first region all four soft factors tend to one and the four signs cancel, and in the second all tend to zero. If \(\kappa_L=\kappa_H\), the middle region is empty. At equality to an endpoint, \(o(q)\) in the exponent does not fix a step value; no such value is assigned. These are the mass-weighted full observed heat and the isometric graph heat, respectively. They do not give a limit two for the raw observed heat or for \(e^{-\tau M_B^\dagger M_B}\).

Finally choose \(\zeta_\diamond=\beta_L-a_0\), \(b_*=-2-I_\square=\beta_L-2a_0\). The exact source certificate [AK18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/KERNEL_CRITICAL_RECEIVERS.tex) proves \(C_\partial>4a_0>0\). Thus \(\beta_H<b_*<\zeta_\diamond<\beta_L\), and KG40 gives

\[
\boxed{\mathcal R\log\frac{\det F_N(z_k(b_*))}{\det F_N(0)}
=2a_0q+o(q)\quad\text{at }\alpha_k(\zeta_\diamond).}
\tag{KG42}
\]

At the canonical endpoint \(\alpha=0\), the same source formula has \(\kappa_T=\beta_T\), so the value is \(4a_0q+o(q)\). Their difference is \(-2a_0q+o(q)\), with the same regularizer at all cutoffs and both activations. KG41 holds at \(b_*\) in both cases. This verifies the incoming coefficients and signs. The gap has supplied the missing complete observed receiver; it has not supplied an initial kernel-volume coefficient or an individual complex-current phase.

## 9. Verification and affected results

The complete finite arguments above verify received (1), (4)–(29), (31)–(32), and (36) on their stated guards; (30) follows from KG36; the critical conclusions (2)–(3), (33)–(35) follow from KG39–42 with the precise limiting scope. The only needed corrections are the scope of the full ultrasmall scale over activation, the distinction between an inherited-metric inclusion and the coefficient frame, and the relative-base-metric meaning of subquotient mass costs. No coefficient error is present in the concrete \(2a_0\), \(4a_0\), or \(-2a_0\) claims.

KG11 improves the guarded canonical gap ME29 and the gap receivers RM19/RM23 by using the original inverse residual directly. KG13–16 extends BR1–5 to all activations and the two growing word families. KG20–22 extends ME31–34 and BR6 to every activation; KG24 extends ME20's memory bound. KG25–38 gives low-frequency and heat receivers for the original complete pencil, while the exact all-index pole reconstruction of RM24–31 remains valid. BR7–8's independent compressed-action leakage is not removed or reinterpreted by these identities.

The accompanying checker distinguishes exact rational polynomial-source and geometric fixtures from numerical matrix comparisons. No fixture is called an arithmetic zero-packet or period evaluation. Source-use identities and coverage are recorded in the source-use section of `SOURCE_LEDGER.json`; every imported programme result above points to its actual pinned proof file.
