# Canonical memory at zero and the exact energy-graph determinant

Independent derivation, 21 September 2026. Equations **ME1–ME34** belong to this proof. The received claims addressed here are (1)–(9) and (47)–(49). Every finite assertion below is proved in its stated metric. The final native estimates use the retained original-source theorems identified in Section 1; their analytic hypotheses and eventual scope remain in force. The source profile is not represented as a new result of this derivation.

## 1. Original objects and the precise source receiver

Fix the original simple quartet, with \(0<\delta<1/2\), \(\gamma>2\), \(k\ge9\), \(k\equiv1\pmod4\), and

\[
\begin{gathered}
q=(k+1)^2,\qquad S=k/2+iy,\\
Q_k(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta],\\
E_k=\mathbb C[y]/(Q_k),\qquad M_k[P]=[yP].
\end{gathered}
\tag{ME1}
\]

The measure is exactly \(d\mu_k=w_h^{*k}(y)\,dy\), with \(w_h(y)=|(2\xi/h)(1/2+iy)|^2/(2\pi)\). Its mass and the full divisor \(h\) are retained. For \(q-1\le N\le2q\), the original metric \(G_N\) is the attained minimum over the whole fibre of the remainder map from polynomials of degree at most \(N\). In particular its relation space contains every polynomial \(Q_kp\) allowed by that degree.

The onto original observation \(\Lambda:E_k\to B_k\), including all invariant columns, has

\[
Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},\qquad
L_{B,N}=G_N^{-1}\Lambda^*Q_{B,N},\qquad
P_{B,N}=L_{B,N}\Lambda,
\quad K=\ker\Lambda.
\tag{ME2}
\]

Multiplication verifies \(\Lambda L_{B,N}=I\), \(L_{B,N}^*G_NL_{B,N}=Q_{B,N}\), and \(P_{B,N}^2=P_{B,N}=P_{B,N}^{\dagger}\). Thus \(L_{B,N}\) is the exact isometry from the attained observed metric to \(K^{\perp_{G_N}}\), and \(\Lambda=L_{B,N}^{\dagger}\). These maps are the ones used throughout.

The original rank is

\[
m=\dim K=8k-16,\qquad n=\dim B_k=q-m=k^2-6k+17.
\tag{ME3}
\]

This is asserted on the proved five-orbit period locus, with the actual period, units and coefficient pivots retained. In the original frame, \(Z=[M_A,S_kZ_k]\), \(\ker\pi=\operatorname{im}Z\), and \(I_K=\mathsf V^{-1}\pi^T\); the transpose is the complex-linear dual, not a metric adjoint. These formulas and the rank computation are [MR1–8, original kernel source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/ORIGINAL_KERNEL_MIXED_DETERMINANT.tex#L30). The source's verified period domain \(|u|\ge R_*\), and its warning that the size-one orbit has a different rank, are [NG24, original Gaussian transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/NATIVE_GAUSSIAN_TRANSFER.tex#L482). The finite matrix theorems below hold for the actual rank at any other period; ME3 and its asymptotic uses are confined to their proved period domain.

The native action has the exact original-metric decomposition

\[
\begin{gathered}
M_k=C_N+r_N\ell_N,\qquad C_N^{\dagger}=C_N,\\
r_N=[p_{N+1}],\qquad \ell_N(v)=[y^N]L_Nv,\qquad \ell_Nr_N=0,\\
\|C_N\|\le C_0:=B_hq,\qquad
\epsilon_N=\|r_N\ell_N\|,\qquad R_N=\epsilon_N+C_0.
\end{gathered}
\tag{ME4}
\]

Here \(L_N:E_k\to\mathcal P_N\) is the full remainder minimum section, distinct from \(L_{B,N}\). The plus sign and parity statement are [SD1–3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/ORIGINAL_SPECTRAL_DETERMINANT.tex#L34). The actual full multiplication inequality is \(\|yP\|_{\mu_k}\le C_{\rm mult}(h)(2L+\lfloor k/3\rfloor)\|P\|_{\mu_k}\) for \(\deg P\le L\); see [NG2–3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/NATIVE_GAUSSIAN_TRANSFER.tex#L50). For example the original choice \(B_h=5\max(1,C_{\rm mult}(h))\) covers \(N\le2q\). Taking \(L=N\) in that inequality bounds the complete degree-raising multiplication before compression; the degree \(N+1\) column is included.

The retained H2/H5 theorem explicitly includes \(N=2q\) and states, uniformly in this cutoff window,

\[
\log\epsilon_N=q\psi(s_N)+O_h(k\log^2(q+2)),\qquad
s_N=(N+1-q)/q.
\tag{ME5}
\]

Its continuous decreasing profile has \(\psi(0)=\log(4/\pi)\) and \(\psi(1)>0\). The exact source identity and its inherited EIQ input are [H1–9, retained profile](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/RETAINED_PROFILE_PROOF.tex#L1). In particular \(s_{2q}=1+1/q\) is covered. This is an eventual analytic theorem, not an effective numerical threshold in \(k\).

All roots in ME1 are nonzero, since both odd integers \(2a-k,2b-k\) are nonzero. Thus \(M_k\) is invertible at every stated finite cutoff. Its determinant is metric independent and exactly

\[
|\det M_k|^2=|Q_k(0)|^2
=\prod_{a,b=0}^k[(2a-k)^2\delta^2+(2b-k)^2\gamma^2].
\tag{ME6}
\]

## 2. The full memory, including zero regularizer

For this section let \(E\) be any \(q\)-dimensional positive Hilbert space, \(K\subset E\), \(0<m=\dim K<q\), and let \(M:E\to E\) be invertible. Use the metric orthogonal splitting \(E=K\oplus K^\perp\) and its isometric inclusions. Write

\[
\begin{gathered}
M=\begin{pmatrix}M_K&D\\C&M_B\end{pmatrix},\qquad
H=M^\dagger M=\begin{pmatrix}A&B_H\\B_H^\dagger&D_H\end{pmatrix},\\
A=M_K^\dagger M_K+C^\dagger C,\qquad D_H=D^\dagger D+M_B^\dagger M_B.
\end{gathered}
\tag{ME7}
\]

In particular \(H,A,D_H\) are positive definite. Define, now for every \(z\ge0\),

\[
\begin{gathered}
F(z)=zI+D_H-B_H^\dagger(zI+A)^{-1}B_H,\\
g(z)=\log\det(zI+A)+\log\det(zI+D_H)-\log\det(zI+H).
\end{gathered}
\tag{ME8}
\]

Block Gaussian elimination, whose triangular factors have determinant one, proves
\(\det(zI+H)=\det(zI+A)\det F(z)\). Completing the positive quadratic form shows \(F(z)>0\), even at \(z=0\). Thus all logarithms in ME8 are defined there, and \(g\) is continuous at zero.

Put

\[
\mathcal Q(t)=\operatorname{Tr}e^{-tH}
-\operatorname{Tr}e^{-tA}-\operatorname{Tr}e^{-tD_H}.
\tag{ME9}
\]

For completeness, choose orthonormal eigenbases of \(A\) and \(D_H\) and concatenate them. If \(e\) belongs to this basis, scalar Jensen applied to the spectral decomposition of \(H\) gives
\(\langle e,e^{-tH}e\rangle\ge e^{-t\langle e,He\rangle}\), because the weights \(|\langle e,v_j\rangle|^2\) are nonnegative and sum to one, and \(x\mapsto e^{-tx}\) is convex. Summing proves \(\mathcal Q(t)\ge0\). The Taylor series gives \(\mathcal Q(t)=t^2\|B_H\|_{\rm HS}^2+O(t^3)\): the constant and linear terms cancel, and \(\operatorname{Tr}H^2-\operatorname{Tr}A^2-\operatorname{Tr}D_H^2=2\|B_H\|_{\rm HS}^2\). At infinity all three traces decay exponentially at each fixed finite matrix. Consequently

\[
\boxed{g(z)=\int_0^\infty e^{-zt}\mathcal Q(t)\,\frac{dt}{t},\quad z\ge0;\qquad
0\le g(z)\le g(0).}
\tag{ME10}
\]

To verify the integral identity without interchanging divergent pieces, pair the \(q\) eigenvalues of \(A\oplus D_H\) with the \(q\) eigenvalues of \(H\). Each paired scalar integral is
\(\int_0^\infty(e^{-at}-e^{-bt})dt/t=\log(b/a)\) for \(a,b>0\): differentiate with respect to \(b\), integrate \(e^{-bt}\), and use equality at \(a=b\). Sum finitely many pairs. The estimates just proved justify the combined integral at zero. They also justify every derivative, including its one-sided value at zero:
\((-1)^jg^{(j)}(z)=\int_0^\infty t^{j-1}e^{-zt}\mathcal Q(t)dt\ge0\) for \(j\ge1\). Thus the complete monotonicity extends to this finite zero endpoint. No lower spectral gap uniform in \(k\) has been assumed.

## 3. Sharp restriction determinants with one exceptional singular value

Assume the descending singular values of \(M\) obey

\[
s_1(M)\le R,\qquad s_j(M)\le C_0\ (j\ge2),\qquad R\ge C_0>0.
\tag{ME11}
\]

The native ME4 implies this: on \(\ker\ell_N\), a codimension-one space, \(M=C_N\) and hence \(\|M\|\le C_0\) there. The variational characterization of the second singular value gives \(s_2\le C_0\); triangle inequality gives \(s_1\le R_N\). The variational characterization follows directly by intersecting any subspace of the required dimension with the span of the ordered eigenvectors of \(M^\dagger M\).

For every isometry \(J:\mathbb C^d\to E\), \(1\le d\le q\), restriction and the same variational argument give \(\lambda_j(J^\dagger HJ)\le s_j(M)^2\). Therefore

\[
\boxed{\det(J^\dagger HJ)\le R^2C_0^{2(d-1)}.}
\tag{ME12}
\]

This is sharp, by restricting \(\operatorname{diag}(R^2,C_0^2,\ldots,C_0^2)\) to a subspace containing its first coordinate. In particular the received two separate bounds for \(\det A\) and \(\det D_H\) follow.

They can be sharpened jointly. Let \(v\) be a unit top eigenvector of \(H\), and put \(t=\|P_Kv\|^2\). Spectral decomposition gives
\(H\preceq C_0^2I+(R^2-C_0^2)vv^\dagger\). Compression, the rank-one determinant formula and positive determinant monotonicity imply

\[
\begin{aligned}
\det A\det D_H
&\le C_0^{2(q-2)}
[C_0^2+(R^2-C_0^2)t]
[C_0^2+(R^2-C_0^2)(1-t)]\\
&=C_0^{2(q-2)}[R^2C_0^2+(R^2-C_0^2)^2t(1-t)]\\
&\le C_0^{2(q-2)}\frac{(R^2+C_0^2)^2}{4}.
\end{aligned}
\tag{ME13}
\]

Positive determinant monotonicity used here follows by congruence: if \(0<X\preceq Y\), all eigenvalues of \(X^{-1/2}YX^{-1/2}\) are at least one. The last bound in ME13 is sharp for every nontrivial splitting: take \(H=C_0^2I+(R^2-C_0^2)vv^\dagger\), with \(\|P_Kv\|^2=1/2\). Its positive square root supplies an invertible \(M\) attaining equality. This proves optimality of this universal numerator bound, not merely of the two separate factors.

Combining ME10 and ME13 proves the uniformly valid improvement of the supplied (3):

\[
\boxed{0\le g(z)\le g(0)
\le 2\log\frac{R^2+C_0^2}{2}
 +2(q-2)\log C_0-2\log|\det M|,\quad z\ge0.}
\tag{ME14}
\]

Since \((R^2+C_0^2)/2\le R^2\), the received \(4\log R\) upper bound is valid. More precisely the same argument for \(zI+H\) gives the finite regularized estimate

\[
g(z)\le(q-2)\log(z+C_0^2)
 +2\log\left(z+\frac{R^2+C_0^2}{2}\right)
 -\log\det(zI+H).
\tag{ME15}
\]

The determinant denominator is the complete action determinant, not the determinant of its bounded compression. If one additionally knows \(\sigma_1(M^{-1})\le L\), \(\sigma_j(M^{-1})\le D_0\) for \(j\ge2\), one obtains the useful independent bound

\[
g(0)=\log\det A+\log\det((H^{-1})_{KK})
\le2\log(RL)+2(m-1)\log(C_0D_0).
\tag{ME16}
\]

Indeed Schur elimination against \(D_H\) proves \((H^{-1})_{KK}=(A-B_HD_H^{-1}B_H^\dagger)^{-1}\), giving the equality; apply ME12 to \(H\) and \(H^{-1}\). The minimum of ME14–16 and the local bound below may always be used.

## 4. Native coefficient and the uniform zero endpoint

Define

\[
I_\square=\log(\delta^2+\gamma^2)-3
 +\frac\delta\gamma\arctan\frac\gamma\delta
 +\frac\gamma\delta\arctan\frac\delta\gamma.
\tag{ME17}
\]

It is \(\int_0^1\int_0^1\log(\delta^2x^2+\gamma^2y^2)dxdy\). For example first integrate in \(x\), using the antiderivative \(x\log(\delta^2x^2+\gamma^2y^2)-2x+(2\gamma y/\delta)\arctan(\delta x/(\gamma y))\); a second integration gives exactly ME17, including the constant \(-3\).

Here is the finite lattice estimate with every root retained. Put \(n_*=k+1\), and use midpoint coordinates \(x_a=(2a-k)/n_*\) on \([-1,1]\). Then ME6 is \(\log|\det M_k|^2=2q\log n_*+\sum_{a,b}f(x_a,x_b)\), \(f(x,y)=\log(\delta^2x^2+\gamma^2y^2)\). The four central cells have centre-minus-cell-average difference \(\log(\delta^2+\gamma^2)-\log4-I_\square\). On shell \(j\ge1\), whose maximum centre-coordinate magnitude is \((2j+1)/n_*\), there are \(8j+4\le12j\) cells. Each point in them has radius at least \(2j/n_*\), and
\(\|\nabla f\|\le2\gamma^2/(\delta^2\sqrt{x^2+y^2})\). The distance from a cell centre is at most \(\sqrt2/n_*\). Each error is consequently at most \(\sqrt2\gamma^2/(\delta^2j)\). Summing at most \(n_*/2\) shells proves

\[
\begin{gathered}
\left|\log|\det M_k|^2-2q\log k-qI_\square\right|\le E_{\rm root}(k),\\
\begin{aligned}
E_{\rm root}(k):={}&2q\log\frac{k+1}{k}+\frac{6\sqrt2\gamma^2}{\delta^2}(k+1)\\
&+4\left|\log(\delta^2+\gamma^2)-\log4-I_\square\right|.
\end{aligned}
\end{gathered}
\tag{ME18}
\]

This reproduces [HAR33–35](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L357) and proves the claimed \(O_{\delta,\gamma}(k)\) error independently from the displayed cells. In particular no logarithmic cell error has been lost at the four innermost roots.

ME5 and continuity with \(\psi(1)>0\) imply that \(\epsilon_N/C_0\to\infty\) uniformly in the window. Indeed the profile has a fixed positive lower bound on \([0,1+1/q]\) for all sufficiently large \(q\), while \(k\log^2(q+2)=o(q)\). Thus
\(\log R_N=\log\epsilon_N+\log(1+C_0/\epsilon_N)=q\psi(s_N)+O_h(k\log^2(q+2))\). Substituting the weaker form of ME14 and ME18, and expanding \(2(q-2)\log(B_hq)\), gives

\[
\boxed{g_N(z)\le2q\log(q/k)
 +q[4\psi(s_N)+2\log B_h-I_\square]
 +O_h(k\log^2(q+2)+\log(q+2)),\quad z\ge0.}
\tag{ME19}
\]

The exact finite alternative, requiring no asymptotic threshold, is ME14 with \(R_N\), \(B_hq\), and the root product ME6, or with the explicitly bounded error ME18. The coefficient \(2q\log(q/k)\) in the received (4) is correct. In particular inserting an additional \(q\log q\) into \(\log\epsilon_N\), or replacing \(\log|\det M|\) by \(\log|\det M|^2\) in (3), would be an error. The retained source H5 concerns \(\log\epsilon_N^2=2q\psi+O_h(k\log^2 q)\).

Since \(q=(k+1)^2\), \(\log(q/k)=O(\log k)=o(k)\), ME19 proves

\[
\boxed{\sup_{q-1\le N\le2q}\ \sup_{z\ge0}g_N(z)
=O_h(q\log(q/k))=o_h(kq),\qquad
\int_0^\infty\mathcal Q_N(t)\frac{dt}{t}=g_N(0).}
\tag{ME20}
\]

This uniform assertion uses positivity and the exact zero determinant; it does not require a uniform decay rate for the heat integrand. For the original signs \(+,+,-,-\) at \(q-1,q,2q-1,2q\), the absolute value of the signed sum at any four nonnegative endpoint-dependent regularizers is bounded by four times the supremum in ME20. Its quotient by \(kq\) tends to zero. This proves the received (1), (5) and (6), including independent regularizers equal to zero.

## 5. Local leakage and its exact difference from memory

For \(z>0\) put

\[
\ell(z)=\log\det(zI+D_H)-\log\det(zI+M_B^\dagger M_B).
\tag{ME21}
\]

Since \(D_H=M_B^\dagger M_B+D^\dagger D\), \(\ell\ge0\). ME8 yields exactly

\[
\boxed{\log\det F(z)-\log\det(zI+M_B^\dagger M_B)=\ell(z)-g(z).}
\tag{ME22}
\]

In original observed coordinates \(M_B\) is precisely \(\Lambda ML_{B,N}\), with the \(Q_{B,N}\) adjoint. Thus ME22 is already the requested original receiving map, with both coupling blocks retained.

Let \(r_D=\operatorname{rank}D\), \(r_H=\operatorname{rank}B_H\), and define
\(\mathcal B_0(z)=0\),

\[
\mathcal B_r(z)=\log(1+R^2/z)+(r-1)\log(1+C_0^2/z),\qquad r\ge1.
\tag{ME23}
\]

Then the rank-sensitive strengthening of the supplied (8) is

\[
\boxed{0\le\ell(z)\le\mathcal B_{r_D}(z),\qquad
0\le g(z)\le\mathcal B_{r_H}(z),\qquad
|\ell(z)-g(z)|\le\mathcal B_{\max(r_D,r_H)}(z)\le\mathcal B_m(z).}
\tag{ME24}
\]

Here \(r_D,r_H\le\min(m,n)\). To prove the first bound, apply the determinant identity to \(zI+M_B^\dagger M_B\) and \(D^\dagger D\); the nonzero eigenvalues of the resulting relative matrix are bounded by \(z^{-1}s_j(D)^2\). Restricting and projecting \(M\) cannot increase its ordered singular values: \((PMJ)^\dagger PMJ\preceq J^\dagger HJ\), followed by the variational argument of ME12. Thus \(s_1(D)\le R\), \(s_j(D)\le C_0\) for \(j\ge2\), and only \(r_D\) factors occur.

For memory, eliminate the other diagonal block. Set \(T_z=B_H(zI+D_H)^{-1}B_H^\dagger\) and \(F_K=zI+A-T_z\). Positivity of \(H\) implies \(B_HD_H^{-1}B_H^\dagger\preceq A\), so \(0\preceq T_z\preceq A\), \(F_K\succeq zI\), and \(\operatorname{rank}T_z=r_H\). Now
\(g=\log\det(I+F_K^{-1/2}T_zF_K^{-1/2})\). Its nonzero eigenvalues are those of \(T_z^{1/2}F_K^{-1}T_z^{1/2}\), bounded by the ordered eigenvalues of \(T_z/z\), hence by those of \(A/z\). ME12 supplies ME24. The final difference bound uses that both numbers are nonnegative; it does not require adding their two upper bounds.

For native matrices, \(\log(1+R_N^2)=O_h(q)\), \(\log(1+C_0^2)=O_h(\log(q+2))\), and \(m=8k-16\). The elementary inequality \(\log(1+x/z)\le\log(1+x)+\log^+(1/z)\), \(x\ge0\), gives

\[
|\ell_N(z)-g_N(z)|\le O_h(q+k\log(q+2))+(8k-16)\log^+(1/z).
\tag{ME25}
\]

Therefore the supplied (9) is correct whenever \(z_k>0\) and \(\log^+(1/z_k)=o(q)\). A slightly stronger exact statement replaces \(8k-16\) in its variable-regularizer cost by \(\max(r_D,r_H)\). Nothing in ME20 permits dropping the positive-regularizer guard from the separately observed action.

Specifically, if \(p=\dim\ker M_B\), diagonalization of \(M_B^\dagger M_B\) gives

\[
\ell(z)=-p\log z+\log\det D_H
 -\log\operatorname{pdet}(M_B^\dagger M_B)+o(1),\quad z\downarrow0.
\tag{ME26}
\]

The empty positive spectral product is one. The numerator is continuous because \(D_H>0\). This proves exactly when leakage diverges. For the rational fixture \(M=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), \(K=\mathbb Ce_1\), one has \(H=I\), \(g\equiv0\), \(M_B=0\), and \(\ell(z)=\log(1+1/z)\). Thus bounded memory alone cannot bound the zero-regularizer comparison with the independently compressed action.

## 6. Finite lower kernel gap and the native guard

Let the smallest eigenvalue of \(H\) be simple, equal to \(h>0\), with unit eigenvector \(w\), and suppose all remaining eigenvalues are at least \(\gamma_*>h\). Put \(\theta=\|P_Bw\|^2\). For a unit \(x\in K\), \(|\langle w,x\rangle|^2\le\|P_Kw\|^2=1-\theta\). Spectral decomposition then gives

\[
\boxed{A\succeq[h(1-\theta)+\gamma_*\theta]I_K
\succeq\gamma_*\theta I_K.}
\tag{ME27}
\]

This proves the supplied lower bound from the actual observed fraction of the actual singular line. To evaluate it natively, retain the exact inverse identity

\[
\begin{gathered}
M_k^{-1}=B_N-\frac{u\varphi_N}{Q_k(0)},\qquad
B_N=J_N\mathscr D L_N,\qquad \mathscr Dp=(p-p(0))/y,\\
u=J_N\frac{Q_k-Q_k(0)}y=-Q_k(0)[y^{-1}],\qquad
\varphi_N(v)=(L_Nv)(0).
\end{gathered}
\tag{ME28}
\]

It follows by multiplying by \(y\) modulo the full polynomial. The finite original bound is
\(\|B_N\|\le d_N:=\sqrt{u_k/\ell_{k,N}}\sqrt{n_N(n_N+1)}(1+\sqrt{N+1})\), \(n_N=\lceil(N+2)/2\rceil\), with \(\log d_N=O_h(k+\log q)\); see [S11–16](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/NATIVE_SMALLEST_SINGULAR_PROOF.tex#L64). These are the exact full-mass NG2 comparison constants.

Put \(E_N=\|u\|\|\varphi_N\|/|Q_k(0)|\), \(\eta_N=d_N/(E_N-d_N)\), and \(\theta_u=\|P_Bu\|^2/\|u\|^2\), an exact quotient-Gram scalar. On the explicit finite guards
\(E_N>2d_N\) and \(\theta_u>\eta_N\), a usable lower bound is

\[
\boxed{\alpha_N=d_N^{-2}(\theta_u-\eta_N)>0,\qquad A\succeq\alpha_NI.}
\tag{ME29}
\]

Proof: on \(\ker\varphi_N\), \(M^{-1}=B_N\), so \(\sigma_2(M^{-1})\le d_N\); triangle inequality gives \(\sigma_1(M^{-1})\ge E_N-d_N>d_N\). The smallest singular value of \(M\) is therefore simple, and the rest of the eigenvalues of \(H\) are at least \(d_N^{-2}\). A unit left top singular vector \(w\) of \(M^{-1}\) obeys \(\|(I-P_u)w\|\le\eta_N\), by applying \(I-P_u\) to ME28. The difference \(P_w-P_u\) has eigenvalues \(+s,-s\), \(s\le\eta_N\); in an orthonormal pair this follows by expanding the two rank-one projections. For any orthogonal projection \(P_B\), its trace against this difference is between \(-s\) and \(s\), since the two diagonal projection entries lie in \([0,1]\). Thus \(\theta\ge\theta_u-\eta_N\), and ME27 proves ME29. This slightly improves the safe trace-norm error \(2\eta_N\).

The original conductor comparison for the inverse-power rank \(r=1\) proves \(\theta_u\ge\vartheta_{1,N}>0\) and \(\log(1/\vartheta_{1,N})=O_{h,A}(k\log(q+2))\). Its fully specified domain is [IVO24–26](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INDEPENDENT_FINITE_OBSERVATION.tex#L258): \(q_-=(k-7)^2\ge16\), \(k\sqrt{\delta^2+\gamma^2}\le2^{-14}q_-\), \(n_-+2\le2q_-\), and \(\mathcal L_*\mathcal R_*T_N^{\rm lb}\ge2\mathcal A\), for an actual nonzero conductor coefficient, with exactly the constants defined there. These finite source conditions are not inferred from the small fixture \(k=9\). IVO26 proves they hold eventually for fixed original data and \(r=1\). The received inverse-observation asymptotic is used only through this proved finite angle estimate.

The retained original smallest-singular theorem [S4–6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/NATIVE_SMALLEST_SINGULAR_PROOF.tex#L40) gives \(\log\|M_k^{-1}\|=q\log(q/k)+O_h(q)\) throughout this cutoff window. Because \(|E_N-\|M_k^{-1}\||\le d_N\), one has \(\eta_N=\exp[-q\log(q/k)+O_h(q)]\). It is eventually smaller than \(\vartheta_{1,N}/2\), uniformly in the four cutoffs. Thus the fully source-evaluated finite guard \(E_N>2d_N\), \(\eta_N<\vartheta_{1,N}/2\) implies
\(\alpha_N\ge\vartheta_{1,N}/(2d_N^2)\), and
\(\log^+(1/\alpha_N)=O_{h,A}(k\log(q+2))\). All eventual statements retain fixed \(h,\delta,\gamma\) and the original period; no arbitrary high-degree filter is substituted for \(M_k\).

## 7. Exact energy graph, its determinant cost, and coefficient coordinates

Return first to any invertible finite \(M\). Write \(B=B_H\), and suppose a finite \(\alpha>0\) with \(A\succeq\alpha I\) has been evaluated, for example by ME29. For each \(b\in K^\perp\), completion of the square gives

\[
\langle(k,b),H(k,b)\rangle
=\langle k+A^{-1}Bb,A(k+A^{-1}Bb)\rangle+\langle b,Sb\rangle,
\quad S=D_H-B^\dagger A^{-1}B>0.
\tag{ME30}
\]

Hence the exact energy minimum section is \(L_{\rm en}b=(-A^{-1}Bb,b)\). Its original norm Gram is \(Z=I+B^\dagger A^{-2}B\), its energy Gram is \(S\), and \(J_{\rm en}=L_{\rm en}Z^{-1/2}\) is an isometry. Direct multiplication gives \(J_{\rm en}^\dagger HJ_{\rm en}=Z^{-1/2}SZ^{-1/2}\).

Let \(J_K:K\to E\) denote the isometric inclusion, not the unadjusted coefficient frame \(I_K\). If that frame is used, \(J_K=I_K(I_K^*GI_K)^{-1/2}\). Since \(A=J_K^\dagger HJ_K\), define the explicitly specified isometry

\[
V=H^{1/2}J_KA^{-1/2}:K\longrightarrow E.
\]

Indeed \(V^\dagger V=I\). Squaring the complete block matrix gives \(J_K^\dagger H^2J_K=A^2+BB^\dagger\). The rectangular determinant identity \(\det(I+UV)=\det(I+VU)\), proved by eliminating either diagonal block in \(\left(\begin{smallmatrix}I&U\\-V&I\end{smallmatrix}\right)\), therefore yields

\[
\boxed{\det Z=\frac{\det(J_K^\dagger H^2J_K)}{(\det A)^2},\qquad
\det A\det Z=\det(V^\dagger HV).}
\tag{ME31}
\]

This identity keeps the exact map relating the energy-weighted kernel subspace \(H^{1/2}K\) to the original kernel. It is not a replacement of the physical metric. Applying ME12 both to \(J_K\) and \(V\), and using \(Z\succeq I\), gives, with \(D_*:=2\log R+2(m-1)\log C_0\),

\[
\boxed{m\log\alpha\le\log\det A\le D_*,\qquad
0\le\log\det Z\le D_* -\log\det A\le D_*-m\log\alpha.}
\tag{ME32}
\]

This proves (47) and improves (48). The useful combined estimate is
\(|\log\det A|+\log\det Z\le D_*+2m\log^+(1/\alpha)\): if \(a=\log\det A\ge0\), its left side is at most \(D_*\); if \(a<0\), it is at most \(D_*-2a\). This proof works for every \(m\ge1\), including \(m=1\), without a negative multiplicity \(m-2\).

For comparison, the received rank-two estimate is also valid for the native \(m\ge2\), but a complete finite form must account for the domain and codomain ranks. Namely \(H-C_N^2=Cr\ell+\ell^\dagger r^\dagger C+\|r\|^2\ell^\dagger\ell\) has range in \(\operatorname{span}(Cr,\ell^\dagger)\), so its rank is at most two. Consequently \(A^{-1}B\) differs by rank at most two from \(A^{-1}P_KC_N^2|_{K^\perp}\), whose norm is at most \(C_0^2/\alpha\). Restriction to the kernel of that difference proves that every singular value after the second is at most \(C_0^2/\alpha\). All are at most \(R^2/\alpha\). Writing \(r=\min(m,n)\), \(t=\min(2,r)\), one obtains
\(\log\det Z\le t\log(1+R^4/\alpha^2)+(r-t)\log(1+C_0^4/\alpha^2)\). For actual \(m=8k-16\), this implies the supplied (48) by increasing the count to \(m\). The received expression is thus a valid weaker bound on its native domain, with a multiplicity repair required only if it is claimed for arbitrary small dimensions.

Finally express the result in the original observed coefficient coordinates. Put \(G=G_N\), \(Q=Q_{B,N}\), and choose the square isometry \(U=[J_K,L_{B,N}Q^{-1/2}]\), so \(U^*GU=I\) and \(\Lambda U=[0,Q^{-1/2}]\). Let \(H_U=U^*M^*GMU\). Then
\((M^*GM)^{-1}=UH_U^{-1}U^*\), and the observed block of \(H_U^{-1}\) is \(S^{-1}\) by elimination. Therefore the exact energy quotient and its graph compression satisfy

\[
\boxed{\begin{gathered}
\mathcal E_B=[\Lambda(M^*GM)^{-1}\Lambda^*]^{-1}
=Q^{1/2}SQ^{1/2},\\
\det(Q^{-1/2}\mathcal E_BQ^{-1/2})
=\det S=\frac{|\det M|^2}{\det A},\\
\det(J_{\rm en}^\dagger HJ_{\rm en})
=\frac{|\det M|^2}{\det A\det Z}
=\frac{|\det M|^2}{\det(V^\dagger HV)}.
\end{gathered}}
\tag{ME33}
\]

In arbitrary observed coordinates the energy-minimizing lift is exactly
\(L_{B,N}-J_KA^{-1}B Q^{1/2}\); its projection under \(\Lambda\) is the identity, and its norm Gram is \(Q^{1/2}ZQ^{1/2}\). Thus the coefficient, energy, and isometric graph objects in ME33 are related by stated maps, with no unidentified determinant factor.

For the original canonical \(M_k\), ME4–5 give \(D_*=O_h(q+k\log(q+2))\), while ME29 gives \(\log^+(1/\alpha_N)=O_{h,A}(k\log(q+2))\) eventually on the stated finite guards. With the actual \(m=8k-16\), ME32 proves

\[
\boxed{|\log\det A_N|+\log\det Z_N
=O_{h,A}(q\log(q+2))=o_{h,A}(kq).}
\tag{ME34}
\]

The same estimate applies to \(|\log\det(V_N^\dagger H_NV_N)|\) by ME31. The numerator \(|\det M_k|^2\) in ME33 is exactly independent of \(N\); it cancels under the original four signs. Consequently both four-cutoff logarithmic determinant returns in ME33, divided by \(kq\), tend to zero. This proves (49) and the energy-graph consequence on the original canonical action. It makes no assertion that the same determinant cost holds for arbitrary rational filters or arbitrary high powers of \(M_k\).

## 8. Verification scope

The accompanying `check_memory_energy.py` passes **208 exact rational checks** and **684 numerical fixture checks**. It checks the attained coefficient-to-isometry map, the sharp common-top-direction determinant, the leakage divergence fixture, and noncommuting energy graphs. The numerical section checks the zero-endpoint heat integral and inequalities on declared finite synthetic matrices; its largest graph-identity discrepancy is less than \(6.16\times10^{-14}\). These are independent algebraic and numerical fixtures, not computed native xi moments, period evaluations, or a replacement for the proof. `MEMORY_ENERGY_CHECK_RESULTS.json` retains the individual checks. The complete source identity and reading coverage are recorded separately in `MEMORY_SOURCE_USE_PRIVATE.json`, with eight local source hashes matched to their retained full-byte public receipts.

An exact two-dimensional geometric fixture is \(G=I\), \(K=\mathbb Re_1\), \(M=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\), \(H=\left(\begin{smallmatrix}5&4\\4&5\end{smallmatrix}\right)\). It attains ME13: \(R=3\), \(C_0=1\), \(t=1/2\), \(\det A\det D_H=25\), \(g(0)=\log(25/9)\). Its actual energy section is \(b\mapsto(-4b/5,b)\), \(Z=41/25\), \(S=9/5\), and \(V(1)=(2,1)/\sqrt5\). Thus \(\det A\det Z=41/5=V^THV\), while the isometric energy-graph compression is \(45/41\). These coordinates show the two distinct subspaces and their exact maps in ME30–33.
