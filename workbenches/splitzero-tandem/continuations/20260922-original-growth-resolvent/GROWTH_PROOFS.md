# Relative source growth and expanding conductor-pole cancellation

Independent derivation, 22 September 2026. This continuation proves the RH-labelled sections 1–3 of the two supplied arrivals in the original invariant-row problem. The label identifies that programme; no conclusion that the Riemann hypothesis is closed is made. The residual coefficient at order \(kq\) remains a determinant to evaluate. RG10 repairs a radius guard that cannot be inferred for every allowed \(L_k\).

The complete predecessor proofs are retained in this source collection and published: [AS1–64, original angle spectrum](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9b7b0bad40b33dc88bba7d8cb1548da1fadbb585/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/ANGLE_PROOFS.md), [RX1–20, full-root innovations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9b7b0bad40b33dc88bba7d8cb1548da1fadbb585/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/ROOT_INNOVATION_AND_EXTRACTION_PROOFS.md), and [FI1–13, finite invariant receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/FINITE_INVARIANT_PROOFS.md). The local complete-basis sampling proof CS1–24 is retained at relative_growth_arrival_20260922/sampling_derivation/SAMPLING_PROOFS.md. Precise versions, actual reading coverage and original human sources are recorded in SOURCE_USE_LEDGER.md. All new relative-growth, complementary-minimum, chronological, radius, spectral-law and common-circle sampling arguments are proved below.

## RG1. Original objects, coordinates and finite domain

Fix the original admitted simple quartet, nonzero conductor and period. Put
\[
k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad k'=k-8,
\quad q'=(k-7)^2,\quad0<\delta<1/2,\quad\gamma>2,
\quad R_h=\sqrt{\delta^2+\gamma^2},\quad q\ge2kR_h.
\tag{RG1}
\]
The original exponents and physical coordinates are
\[
c=k/2,\quad c'=k/2-4,\quad
\beta_{ab}=c+(2a-k)\delta+i(2b-k)\gamma,
\]
\[
\beta'_{ab}=c'+(2a-k')\delta+i(2b-k')\gamma,\quad
\omega'_{ab}=(\beta'_{ab}-c')/i
=(2b-k')\gamma-i(2a-k')\delta.
\]
Retain the complete original symbol
\[
E_A(w)=\sum_{a,b=0}^{8}a_{ab}e^{b_{ab}w},\quad
b_{ab}=4+(2a-8)\delta+i(2b-8)\gamma,
\]
\[
v=\operatorname{ord}_0E_A\le80,\quad\mu_v=E_A^{(v)}(0)\ne0,
\quad d_A=|\mu_v|/v!,\quad A_1=\sum|a_{ab}|,\quad
B_A=\max_{a_{ab}\ne0}|b_{ab}|.
\]
The bound on \(v\) follows from the invertible Vandermonde matrix of at most 81 distinct exponents. The complete original invariant rows, after all low-polynomial constraints, form \(V_k\), supported on the original conductor strip of size \(n_E=q-q'=16k-48\). Let \(Z\) be its fixed full row frame,
\[
R_Z=ZZ^*>0,\qquad r=8k-32-v+s_k,\quad
s_k=\dim(K_k\cap\mathcal P_{<v}),\quad0\le s_k\le v.
\]
In particular \(24\le r\le8k-32\). A physical row \(z\in V_k\) acts through
\[
F_z(w)=\sum_\alpha z_\alpha e^{\beta_\alpha w},\quad
A_z(w)=e^{-c'w}F_z(w)/E_A(w),\quad
\ell_z[y^n]=(-i)^n n![w^n]A_z(w).
\tag{RG2}
\]
The numerator's first \(v\) derivatives vanish, so \(A_z\) is removable at zero. The identity in (RG2) is exactly
\(\ell_z[f]=[f((\partial_w-c')/i)(F_z/E_A)]_{w=0}\), by differentiating \(e^{-c'w}\). Neither the center nor the phase is changed.

For every integer \(q-1\le N\le2q\), set \(D=N-v\), \(M=D-q'\). Retain
\[
Q_-(y)=i^{-q'}\chi'(c'+iy)=\prod_{a,b=0}^{k'}(y-\omega'_{ab}),
\quad I_N=Q_-\mathbb C[y]_{\le M},
\]
\[
d\sigma(y)=|\Gamma(1/4+iy/2)|^2\,dy/(2\pi),\quad
M_\sigma=\sqrt{2\pi},\quad
p_{n+1}=yp_n-n(n-1/2)p_{n-1},\quad h_n=M_\sigma n!(1/2)_n,
\]
with \(p_0=1,p_1=y\). The matrix \(E_D\) has every evaluation row \(p_n(\omega'_\alpha)/\sqrt{h_n}\). Its rank is \(q'\) by interpolation; its kernel is exactly \(I_N\), since all roots are distinct. Thus
\[
P_N=I-E_D^*(E_DE_D^*)^{-1}E_D,\quad
C_N=W_NP_NW_N^*,\quad B_N=W_NW_N^*,\quad
S_N=B_N^{-1/2}C_NB_N^{-1/2}.
\tag{RG3}
\]
Here \(W_N\) comprises the original functionals on \(p_n/\sqrt{h_n}\). The fixed coefficient congruence is
\(C_N^\circ=R_Z^{-1/2}C_NR_Z^{-1/2}\), \(B_N^\circ=R_Z^{-1/2}B_NR_Z^{-1/2}\). It compares the same rows and leaves the physical source unchanged. Its unitary relation with the physical angle matrix is induced by
\(B_N^{1/2}R_Z^{-1/2}(B_N^\circ)^{-1/2}\).
In the subsequent matrix arguments \(C_N,B_N\) abbreviate these congruent matrices. The inverse congruence recovers the physical frame.

## RG2. Explicit previously proved finite constants

These are the finite constants of AS6–31, with no unspecified remainder in a finite inequality. Let \(a_*\ne0\) be the actual lexicographic conductor pivot and \(C_{\rm path}=A_1/|a_*|\). Put
\[
\mathfrak M=\max\{1,e^{1+2\pi\gamma}A_1(8q+1)^{1/4}(2q+1)(4q+1)^{4\delta}\},
\]
\[
B_{\rm val}=qM_\sigma e^{8q}
\left({2q+kR_h\over2\delta k}\right)^{2(q-1)},\quad
B_E=n_EM_\sigma\left({2n_E+kR_h\over2\delta}\right)^{2(n_E-1)},
\]
\[
c_k=(\mathfrak M^2B_{\rm val}qC_{\rm path}^{20k})^{-1},\qquad
b_k^-=(\mathfrak M^2B_E)^{-1}.
\tag{RG4}
\]
AS6–11 prove \(C_N\succeq c_kI\) using the full upper-root product, the actual strip elimination and the complete lower-root minimum. AS26 proves \(B_N\succeq b_k^-I\) using the entire strip. The exact expansion is
\[
\log(1/c_k)=2(q-1)\log(q/k)+8q+
2(q-1)\log{2+kR_h/q\over2\delta}
+2\log\mathfrak M+\log(q^2M_\sigma)+20k\log C_{\rm path}.
\tag{RG5}
\]
No monic-profile asymptotic is used.

Define
\[
a_0={\log^+(A_1/d_A)\over\log2},\quad b_0={4B_A\over\log2},\quad
C_A={\max(A_1,d_A)^2\over d_A^3},\quad
M_k(R)=C_A\sqrt{n_E}e^{(2kR_h+8+4B_A)R},
\]
\[
\bar B_A=\max(1,B_A),\quad
\rho_A=\min\left\{1,{(v+1)!d_A\over2A_1\bar B_A^{v+1}e^{\bar B_A}}\right\},\quad
M_{0,k}=2\sqrt{n_E}\rho_A^{-v}d_A^{-1}e^{(4+kR_h)\rho_A}.
\]
Put \(M_{\max}=2q-v-q'\), \(c_\sigma=\Gamma(1/4)^2/(2\pi)\), and
\[
\mathfrak A=(M_{\max}+1)10^{M_{\max}}2^{q'}e^{\pi q/2}
\sqrt{{1+16q^2\over c_\sigma q}},
\]
\[
\mathfrak F=\mathfrak A C_A\sqrt{n_E}
e^{2R_hq+(8+4B_A)k}(R_h+2)^{q'},\quad
\mathfrak F_0=\mathfrak A M_{0,k}(kR_h/q+2/\rho_A)^{q'}(2/\rho_A)^{M_{\max}},
\]
\[
L_A=b_0+9,\quad j_A=\left\lceil\max\{2(a_0+1),a_0+1+4L_A\}\right\rceil,\quad
\mathfrak U_k=\max\{\mathfrak F^2(4L_A)^{2q'},\mathfrak F_0^2j_A^{2q'}\}.
\tag{RG6}
\]
AS12–25 prove, at every cutoff,
\[
\lambda_j^\downarrow(C_N)\le\mathfrak U_kj^{-2q'},\qquad1\le j\le r.
\tag{RG7}
\]
The exact index is justified by \(R_j=(j-1-a_0)/(2L_A)\): for \(j\ge j_A\),
\(2\le R_j\le k\), \(R_j\ge j/(4L_A)\), and the true pole-constraint codimension is \(<j\). The first \(j\) eigenspace therefore intersects that subspace. For \(j<j_A\), the fixed-radius bound supplies the second term of (RG6). This also covers \(j_A>r\).

For the angle constant set \(t_A=\tanh(\rho_A/2)\),
\[
b_k^+=\max\{1,M_{0,k}^2M_\sigma^{-1}(1-t_A^2)^{-1/2}(2q+1)^2t_A^{-4q}\},
\]
\[
\ell_k=\log(q/k),\qquad C_{\rm ang}=\max\left\{0,
-q^{-1}\log(c_k/b_k^+)-2\ell_k,\ 
q^{-1}\log(\mathfrak U_k/b_k^-)+2\ell_k-{2q'\over q}\log r\right\}.
\tag{RG8}
\]
AS29–31 give
\[
-C_{\rm ang}\le x_{j,N}:=q^{-1}\log s_{j,N}+2\ell_k
\le C_{\rm ang}+2\log(r/j).
\tag{RG9}
\]
For fixed data, (RG5) gives \(\log(1/c_k)=2(q-1)\ell_k+O(q)\), (RG6) gives \(\log\mathfrak U_k=O(q)\), and \(\log(1/b_k^-)=O(k\log q)\). Also \(\log b_k^+=O(q)\), and \(2\ell_k-2(q'/q)\log r=O(1)\), since \(r=8k+O(1)\). Hence \(C_{\rm ang}=O(1)\). None of these statements is asserted uniformly through degeneration of \(d_A\) or \(a_*\).

## RG3. Exact full-root chronological innovation

Append one original orthonormal source column: \(E_{D+1}=[E_D,e]\), \(W_{N+1}=[W_N,w]\). Let \(G=E_DE_D^*\). In the new source,
\[
t={1\over\sqrt\kappa}\binom{-E_D^*G^{-1}e}{1},\qquad
\kappa=1+e^*G^{-1}e
\]
has norm one, lies in the full evaluation kernel, and is perpendicular to the embedded old kernel. The new kernel has dimension exactly one more. Consequently
\[
C_{N+1}=C_N+\eta_N\eta_N^*,\quad
\eta_N={w-W_NE_D^*G^{-1}e\over\sqrt\kappa},\quad
B_{N+1}=B_N+ww^*.
\tag{RG10}
\]
This reproves RX1 with every complex cross term and every root retained. Congruence multiplies both new columns by \(R_Z^{-1/2}\).

## RG4. Relative-growth spectrum, tails and all exterior ranks

Take any integers \(q-1\le l\le u\le2q\), and define
\[
\Gamma=C_l^{-1/2}C_uC_l^{-1/2},\quad
\mu_1\ge\cdots\ge\mu_r\ge1,\quad
\Omega=\log(\mathfrak U_k/c_k),\quad\alpha=q'/q,\quad
B_{\rm inc}={\Omega-2q'\log r\over q}.
\tag{RG11}
\]
The eigenvalues of \(\Gamma\) equal those of \(C_u^{1/2}C_l^{-1}C_u^{1/2}\), because \(TT^*\) and \(T^*T\) have identical spectra for the invertible matrix \(T=C_l^{-1/2}C_u^{1/2}\). The latter matrix is at most \(c_k^{-1}C_u\). Min–max and (RG7) therefore give
\[
1\le\mu_j\le(\mathfrak U_k/c_k)j^{-2q'},\qquad
0\le q^{-1}\log\mu_j\le B_{\rm inc}+2\alpha\log(r/j).
\tag{RG12}
\]
The inequality \(c_k\le\lambda_r(C_l)\le\mathfrak U_kr^{-2q'}\) proves \(B_{\rm inc}\ge0\) exactly. From (RG5),
\(qB_{\rm inc}=2(q-1)\log(q/k)-2q'\log r+O(q)=O(q)\); hence \(B_{\rm inc}=O(1)\).

For \(T\ge B_{\rm inc}\), count the indices in (RG12) and integrate:
\[
{1\over r}\sum_j(q^{-1}\log\mu_j-T)_+
\le2\alpha e^{-(T-B_{\rm inc})/(2\alpha)}.
\tag{RG13}
\]
For \(0\le\theta<(2\alpha)^{-1}\), comparison of \(\sum j^{-2\alpha\theta}\) with its integral on \((0,r]\) gives
\(r^{-1}\sum_j\mu_j^{\theta/q}\le e^{\theta B_{\rm inc}}/(1-2\alpha\theta)\).

For every integer \(0\le h\le r\), define
\[
\mathfrak D_k(0)=0,\quad
\mathfrak D_k(h)=h\Omega-2q'\log(h!)
=qhB_{\rm inc}+2q'\log(r^h/h!).
\tag{RG14}
\]
Then
\[
\log\|\wedge^h\Gamma\|=\sum_{j=1}^h\log\mu_j
\le\mathfrak D_k(h)
\le qh[B_{\rm inc}+2\alpha(1+\log(r/h))].
\tag{RG15}
\]
The last inequality is \(\log(h!)\ge h\log h-h\), obtained by integrating \(\log t\). Also
\(\mathfrak D_k(h)-\mathfrak D_k(h-1)=\Omega-2q'\log h\ge0\).
Since \(t\log(1/t)\to0\), \(h=o(k)\) implies \(\mathfrak D_k(h)=o(kq)\). The bounds are uniform over the complete integer cutoff window.

## RG5. Restrictions and attained quotients: complete generalized interlacing

Let \(A\preceq D\) be positive definite forms on \(\mathbb C^r\), with relative eigenvalues \(\mu_j\) in decreasing order. For a fixed injection \(J:\mathbb C^m\to\mathbb C^r\), \(d=r-m\), the matrix
\[
V=A^{1/2}J(J^*AJ)^{-1/2}
\]
is an isometry, and the relative restriction matrix equals
\[
(J^*AJ)^{-1/2}J^*DJ(J^*AJ)^{-1/2}
=V^*(A^{-1/2}DA^{-1/2})V.
\]
Its ordered eigenvalues satisfy
\[
\mu_j\ge\theta_j^J\ge\mu_{j+d},\qquad1\le j\le m.
\tag{RG16}
\]
The upper inequality follows by restricting the maximizing \(j\)-dimensional trial spaces to \(\operatorname{im}V\). For the lower inequality, the top \((j+d)\)-dimensional eigenspace intersects this codimension-\(d\) image in dimension at least \(j\), where the quadratic form is at least \(\mu_{j+d}\). This proves the finite min–max statement without eigenvector alignment.

For any fixed surjection \(\pi:\mathbb C^r\to\mathbb C^m\), define
\[
Q_A=(\pi A^{-1}\pi^*)^{-1},\quad
\min_{\pi x=y}x^*Ax=y^*Q_Ay,\quad
x_{\min}=A^{-1}\pi^*Q_Ay.
\tag{RG17}
\]
The proposed point maps to \(y\); every other point differs by \(z\in\ker\pi\), and its cross term vanishes since \(Ax_{\min}=\pi^*Q_Ay\). Positivity proves existence and uniqueness of the attained minimum. Increasing the form increases its minimum on each fixed fibre; thus \(Q_A\preceq Q_D\).

The matrix \(V=A^{-1/2}\pi^*Q_A^{1/2}\) is an isometry and
\[
V^*(A^{-1/2}DA^{-1/2})^{-1}V
=Q_A^{1/2}Q_D^{-1}Q_A^{1/2}
=(Q_A^{-1/2}Q_DQ_A^{-1/2})^{-1}.
\]
Apply compression interlacing to the inverses and invert their ordered eigenvalues. The attained-quotient relative eigenvalues satisfy
\[
\mu_j\ge\theta_j^Q\ge\mu_{j+d},\qquad1\le j\le m.
\tag{RG18}
\]
This inversion step specifies the exact quotient map; compressing \(A\) itself would instead produce its restriction.

## RG6. Complete complementary Schur loss

Choose one fixed invertible coefficient frame \([J,K]\), with \(J\) the retained rank-\(r-h\) inclusion. In this frame write
\[
C_N=\begin{pmatrix}A_N&T_N\\T_N^*&D_N\end{pmatrix},\qquad
\Sigma_N=D_N-T_N^*A_N^{-1}T_N.
\]
Completion of the square proves
\[
\det C_N=\det A_N\det\Sigma_N,
\]
\[
u^*C_N^{-1}v=u_1^*A_N^{-1}v_1+
(u_2-T_N^*A_N^{-1}u_1)^*\Sigma_N^{-1}
(v_2-T_N^*A_N^{-1}v_1).
\tag{RG19}
\]
For a nonunitary frame its constant squared determinant is present at each cutoff and cancels between the same endpoints. The form \(\Sigma_N\) is exactly the attained quotient under projection onto the complementary \(h\) entries, and therefore increases with \(N\).

Write \(G(l,u)=\log(\det C_u/\det C_l)\), \(G_J(l,u)=\log(\det A_u/\det A_l)\). Equations (RG18)–(RG19) prove
\[
0\le G(l,u)-G_J(l,u)
=\log{\det\Sigma_u\over\det\Sigma_l}
\le\sum_{j=1}^h\log\mu_j\le\mathfrak D_k(h).
\tag{RG20}
\]
For a retained attained quotient of rank \(r-h\), the missing determinant is the restriction to its rank-\(h\) kernel. The same square completion and (RG16) prove the identical bound. Every complementary minimum is retained, and no inverse cross term in (RG19) has been set to zero.

## RG7. Selected actual chronological increments

Let \(\mathcal J\subset\{l,\ldots,u-1\}\) contain \(h\) selected original additions. Put
\(d_N=\log(\det C_{N+1}/\det C_N)=\log(1+\eta_N^*C_N^{-1}\eta_N)\ge0\).
The selected-only partial sums
\(C_N^{\mathcal J}=C_l+\sum_{j<N,j\in\mathcal J}\eta_j\eta_j^*\)
satisfy \(C_N^{\mathcal J}\preceq C_N\), hence
\((C_N^{\mathcal J})^{-1}\succeq C_N^{-1}\).
The determinant lemma at every selected step gives
\[
\sum_{N\in\mathcal J}d_N
\le\log{\det(C_l+\sum_{N\in\mathcal J}\eta_N\eta_N^*)\over\det C_l}.
\]
After whitening, the latter relative matrix lies between \(I\) and \(\Gamma\) and differs from \(I\) by rank at most \(\min(h,r)\). Min–max bounds its nonunit eigenvalues by the first \(\min(h,r)\) eigenvalues of \(\Gamma\). Therefore
\[
0\le\sum_{N\in\mathcal J}d_N\le\mathfrak D_k(\min(h,r)).
\tag{RG21}
\]
These are the actual increments in the full chronology. Their sum generally differs from the selected-only determinant gain; the proved inequality is the needed connecting map. On either original \(q\)-step window, \(o(k)\) selected additions contribute \(o(kq)\).

For any one fixed retained rank-\(s\) row inclusion, the updates are exactly \(J^*\eta_N\eta_N^*J\). The same proof on that row space, followed by (RG16), gives the sharper rank cap \(\mathfrak D_k(\min(h,s))\) for its selected actual increments. This statement uses the retained chronological covariance at each step, including all earlier additions to that row space.

## RG8. Actual pole jets and the finite holomorphic envelope

Set \(b(w)=E_A(w)/w^v\), so \(b\) is entire and \(|b(0)|=d_A\). Jensen's formula on radius \(4R\), obtained by factoring its finitely many interior zeros and applying the mean-value identity to the remaining logarithm, gives for \(R\ge1\)
\[
n_b(2R)\log2\le\log^+(A_1/d_A)+4B_AR.
\tag{RG22}
\]
The boundary estimate is \(|b(w)|\le A_1(4R)^{-v}e^{4B_AR}\le A_1e^{4B_AR}\); approach boundary-zero radii by admissible radii. Zeros in the open disk are counted with complete multiplicities.

Let \(\mathcal Z_R\subset V_k\) be the kernel of all original equations \(F_z^{(j)}(\zeta)=0\) for these zeros and \(0\le j<\operatorname{ord}_\zeta b\). Its actual codimension obeys
\[
h_R\le n_b(2R)\le a_0+b_0R.
\tag{RG23}
\]
These kernels are nested in \(R\), fixed across \(N\), and no independence of their equations is assumed.

Form the radius-\(2R\) finite Blaschke product
\[
\mathcal B_R(w)=\prod_\zeta
\left({2R(w-\zeta)\over(2R)^2-\bar\zeta w}\right)^{m_\zeta}.
\]
It has modulus one on the boundary and its poles are outside the closed disk. Both \(b/\mathcal B_R\) and \(e^{-c'w}F_z/(w^v\mathcal B_R)\) extend across every listed zero; the first has no zero in the open disk. Put \(M_b=\max(A_1,d_A)e^{2B_AR}\). The maximum principle gives \(|b/\mathcal B_R|\le M_b\), and its value at zero has modulus at least \(d_A\). The nonnegative harmonic function \(u=\log(M_b/|b/\mathcal B_R|)\) satisfies \(u(w)\le3u(0)\) on \(|w|\le R\): use the Poisson kernel on \(R<s<2R\), with ratio at most \((s+R)/(s-R)\), then let \(s\uparrow2R\). Therefore \(|b/\mathcal B_R|\ge d_A^3/M_b^2\). Boundary zeros are allowed in this argument.

On \(|w|=2R\), \(|\beta_\alpha-c'|\le4+kR_h\), and the \(n_E\) actual strip entries give
\[
|e^{-c'w}F_z/w^v|\le\sqrt{n_E}e^{2(4+kR_h)R}\|z\|.
\]
The numerator maximum principle and the preceding denominator bound prove
\[
\sup_{|w|\le R}|A_z(w)|\le M_k(R)\|z\|,\qquad z\in\mathcal Z_R.
\tag{RG24}
\]
The row coefficient norm is exactly the one induced by the fixed \(R_Z\) congruence.

## RG9. Every allowed growing radius and its complementary cost

Let \(L_k\to\infty\), \(L_k=o(k)\), and \(R_k=k/L_k\). For the complete metric-and-sampling result use the explicit finite guards
\[
1\le L_k\le k/4,\qquad R_k=k/L_k,\qquad a_0+b_0R_k\le r/2,
\tag{RG25}
\]
together with (RG1) and the original finite arithmetic-receiver guards when using that receiver. All radius guards hold eventually for fixed data. The actual codimension \(h=h_{R_k}\) is an integer, \(s=r-h\ge r/2>0\), and one coefficient-orthonormal inclusion \(J_R:\mathbb C^s\hookrightarrow\mathbb C^r\) is fixed at every cutoff.

For \(l_i=q-1+i,u_i=2q-1+i\), \(i=0,1\), put \(G_i=G(l_i,u_i)\), \(G_i^R=G_{J_R}(l_i,u_i)\). Then
\[
0\le(G_0+G_1)-(G_0^R+G_1^R)
\le2\mathfrak D_k(h)
=O\!\left(kq{1+\log L_k\over L_k}\right)=o(kq).
\tag{RG26}
\]
Indeed \(k/L_k\to\infty\) absorbs the fixed \(a_0\), so \(h/r=O(1/L_k)\), and (RG15) applies. The entire attained complementary determinant is included.

The first arrival's choice is also valid: \(d=\lfloor r/\log(q+e)\rfloor\), \(R=(d-a_0)/(b_0+1)\), with finite guards \(2\le R\le k\), \(R\ge\frac12\log(8q-1)\), \(d\le r/2\). Since \(a_0+b_0R=d-R\le d\), its true codimension is at most \(d\); all guards hold eventually. Its complementary cost is \(O(kq\log\log(q+e)/\log(q+e))\). For sampling at this radius add \(R\ge4\), also eventual.

## RG10. Finite-radius defect and repaired every-direction metric theorem

The conditions \(L_k\to\infty\), \(L_k=o(k)\) do **not** imply
\(R_k\ge\operatorname{arctanh}(1-1/(4q))=\frac12\log(8q-1)\).
For example \(L_k=k/\sqrt{\log(q+e)}\) satisfies both conditions but has \(R_k=\sqrt{\log(q+e)}\), smaller than this logarithmic threshold eventually. Thus the fixed \(t\)-circle of the first arrival cannot be used automatically for every later \(L_k\). The exact admissible circle space is
\[
\mathcal D_{k,R}=\{\rho:0<\rho\le1-1/(4q),\
\operatorname{arctanh}\rho\le R\}.
\]
Its largest member is
\[
\rho_{k,R}=\min\{1-1/(4q),\tanh R\}.
\tag{RG27}
\]
For \(|t|\le\rho_{k,R}\), the power series gives \(|-i\arctan t|\le\operatorname{arctanh}|t|\le R\). The original Gamma generating function yields
\[
H_z(t)=(1+t^2)^{-1/4}A_z(-i\arctan t),\qquad
W_{z,n}={\rho_n\over\sqrt{M_\sigma}}[t^n]H_z,\qquad
\rho_n^2={n!\over(1/2)_n}\le2n+1.
\]
The last inequality follows by induction. Cauchy's bound and
\(\sum_{n=0}^D(2n+1)=(D+1)^2\), applied to every retained row combination, give
\[
b_k^-I\preceq B_N^R:=J_R^*B_NJ_R\preceq b^+_{k,R}I,
\]
\[
b^+_{k,R}=\max\{1,M_k(R)^2M_\sigma^{-1}
(1-\rho_{k,R}^2)^{-1/2}(2q+1)^2\rho_{k,R}^{-4q}\}.
\tag{RG28}
\]
There is no additional row-rank factor. A completely finite logarithmic bound is
\[
\log b^+_{k,R}\le
\log^+(M_k(R)^2/M_\sigma)+2\log(2q+1)+\tfrac12\log(4q)
+\tfrac43+{8q e^{-2R}\over1-e^{-2R}}.
\tag{RG29}
\]
Indeed \(1-\rho_{k,R}^2\ge1/(4q)\),
\(-4q\log(1-1/(4q))\le4/3\), and
\[
-\log\tanh R=\log{1+e^{-2R}\over1-e^{-2R}}
\le{2e^{-2R}\over1-e^{-2R}}.
\]
The negative logarithm of the minimum is the maximum of the two negative logarithms, bounded by their sum. Taking a positive part in (RG28) proves (RG29).

Define the finite nonnegative width
\[
\epsilon_{k,R}^{\rm met}={1\over q}
\max\{\log^+(1/b_k^-),\log b^+_{k,R}\}.
\tag{RG30}
\]
At \(R=k/L_k\),
\[
\epsilon_{k,R}^{\rm met}
=O\!\left({1\over L_k}+e^{-2k/L_k}+{k\log(q+2)\over q}\right)=o(1).
\tag{RG31}
\]
This repairs the general \(L_k\) extension in every retained direction. When \(R\ge\frac12\log(8q-1)\), the original fixed circle is valid and the exponential term is unnecessary; this holds eventually for \(L_k=\sqrt{\log(q+e)}\) and the first arrival's radius.

## RG11. Uniform Wasserstein comparison with the original angles

Let \(y_{1,N}\ge\cdots\ge y_{s,N}\) be the centered log eigenvalues of
\((B_N^R)^{-1/2}C_N^R(B_N^R)^{-1/2}\), where \(C_N^R=J_R^*C_NJ_R\), and let
\(z_{j,N}=q^{-1}\log\lambda_j(C_N^R)+2\ell_k\).
The exact isometry
\[
\mathcal J_N=B_N^{1/2}J_R(J_R^*B_NJ_R)^{-1/2}
\]
compresses the full angle matrix to the retained one. Thus
\[
x_{j,N}\ge y_{j,N}\ge x_{j+h,N},\qquad
|z_{j,N}-y_{j,N}|\le\epsilon_{k,R}^{\rm met}.
\tag{RG32}
\]
The second statement is generalized min–max applied to (RG28).

Put \(\mu_N=r^{-1}\sum\delta_{x_{j,N}}\), \(\nu_N^R=s^{-1}\sum\delta_{z_{j,N}}\), \(\delta_R=h/r\). At \(h=0\) interpret \(\delta_R\log(1/\delta_R)=0\). Then
\[
\sup_N W_1(\mu_N,\nu_N^R)
\le\epsilon_{k,R}^{\rm met}
+\delta_R[4C_{\rm ang}+6+2\log(1/\delta_R)].
\tag{RG33}
\]
Here is the full proof with both empirical masses. Pad \(y_1,\ldots,y_s\) by \(h\) copies of \(-C_{\rm ang}\). The resulting decreasing list \(\widetilde y\) satisfies \(x_j\ge\widetilde y_j\), by (RG9),(RG32). Its ordered-coupling cost is therefore its mean difference, bounded by
\[
{1\over r}\left(2hC_{\rm ang}+2\sum_{j=1}^h\log(r/j)\right)
\le\delta_R[2C_{\rm ang}+2+2\log(1/\delta_R)].
\]
The padded law is
\((1-\delta_R)s^{-1}\sum\delta_{y_j}+\delta_R\delta_{-C_{\rm ang}}\).
Moving its additional atom to the restricted list costs at most
\[
\delta_R\left(s^{-1}\sum y_j+C_{\rm ang}\right)
\le\delta_R[2C_{\rm ang}+2+2\log(r/s)].
\]
Use \(y_j\le C_{\rm ang}+2\log(r/j)\) and
\(s^{-1}\sum_{j\le s}\log(s/j)\le1\). Since \(\delta_R\le1/2\),
\(2\log(r/s)\le2\log2<2\). The triangle inequality and (RG32) prove (RG33).
Ordered coupling is optimal on the line: uncrossing \(a\le b,c\le d\) uses
\(|a-c|+|b-d|\le|a-d|+|b-c|\).

The right side increases when \(\delta_R\) is replaced by any certified upper bound in \([\delta_R,1/2]\), because the derivative of its last term is
\(4C_{\rm ang}+4+2\log(1/\delta)>0\). At the general radius it is
\[
O\!\left({1+\log L_k\over L_k}+e^{-2k/L_k}
+{k\log(q+2)\over q}\right)=o(1).
\tag{RG34}
\]
Every 1-Lipschitz statistic, including the mean and clipped sums, differs by at most (RG33). Two endpoint differences have at most twice that error. Since \(C_N^R\) increases, each \(z_{j,N}\) increases: \(\nu_N^R\) is an exact stochastically increasing path approximating the full angular path uniformly. Its total \(W_1\) variation telescopes and is at most
\[
{G_J(q-1,2q)\over sq}\le{\mathfrak D_k(r)\over sq}
\le{r\over s}(B_{\rm inc}+2\alpha).
\tag{RG35}
\]
Uniform path distance alone is not used to infer total variation for the original path.

Set \(C_R=C_{\rm ang}+\epsilon_{k,R}^{\rm met}+2\log(r/s)\).
Then \(-C_R\le z_j\le C_R+2\log(s/j)\). Therefore
\(s^{-1}\sum(z_j-T)_+\le2e^{-(T-C_R)/2}\) for \(T\ge C_R\), and
\(s^{-1}\sum e^{\theta z_j}\le e^{\theta C_R}/(1-2\theta)\) for \(0\le\theta<1/2\).
The proof is the same index count and integral as RG4. Uniform first-moment control, including its tails, is retained.

## RG12. Both original Gamma source orders

Write \(k=4\ell+1\). Retain the full masses
\[
dm_s(y)={(2\pi)^{s/2}2^{s/2}\over4\pi\Gamma(s/2)}
|\Gamma(s/4+iy/2)|^2dy,\qquad s\in\{1,k\},
\]
\[
dm_k=\beta_k\prod_{j<\ell}[y^2+(2j+1/2)^2]d\sigma,\qquad
\beta_k={(2\pi)^{k/2}\over\sqrt2\Gamma(k/2)}.
\tag{RG36}
\]
The equality is the Gamma recurrence applied exactly \(\ell\) times.
The orthonormal polynomial recurrence implies
\(\|yp\|_\sigma\le2(D+1)\|p\|_\sigma\) for degree at most \(D\): the two off-diagonal weighted shifts each have norm at most \(D+1\). Apply this successively to multiplication by \(y+i(2j+1/2)\). With \(D_{\max}=2q-v\), set
\[
a=\beta_k\prod_{j<\ell}(2j+1/2)^2,\qquad
b=\beta_k\prod_{j<\ell}[2(D_{\max}+j+1)+2j+1/2]^2,\qquad
\Lambda_\Gamma=\log(b/a).
\tag{RG37}
\]
The complete source and every complete ideal satisfy
\(aH^{(1)}\preceq H^{(k)}\preceq bH^{(1)}\).
The exact dual supremum reverses these inequalities for \(C,B\), including their row restrictions. Hence every original angle logarithm changes by at most \(\Lambda_\Gamma\), and the centered laws differ by at most \(\Lambda_\Gamma/q=O(k\log q/q)=o(1)\).

The same-source relative-growth and sampling constants transport exactly as
\[
c^{(k)}=c_k/b,\quad b_-^{(k)}=b_k^-/b,\quad
\mathfrak U^{(k)}=\mathfrak U_k/a,\quad H_{k,R}^{(k)}=H_{k,R}/\sqrt a.
\tag{RG38}
\]
Thus \(\Omega^{(k)}=\Omega+\Lambda_\Gamma\); the additional rank-\(h\) exterior allowance is \(h\Lambda_\Gamma\). The sampling threshold increases by at most \(\Lambda_\Gamma/(2\log2)\), plus its integer ceiling. The full \(\beta_k\) is retained in all form comparisons. If projected-covariance laws themselves are compared between sources, the common mass shift must also be kept: corresponding log eigenvalues lie between shifts \(-q^{-1}\log b\) and \(-q^{-1}\log a\). The angle comparison cancels that common scale only after forming the ratio of both physical forms.

## RG13. Full-ideal estimate for arbitrary finite coefficient errors

This argument is restated to cover sampling errors that need not satisfy any pole-cancellation equations. The original Gamma product implies
\[
\sigma(y)\ge c_\sigma e^{-\pi|y|/2}/(1+4y^2).
\]
Indeed retain its first factor and bound the remaining sum of logarithms by
\(\int_0^\infty\log(1+t^2/x^2)\,dx=\pi|t|\), at \(t=y/2\).
On the original interval \([q,2q]\), all lower roots have modulus at most \(q/2\), so
\[
\|Q_-p\|_\sigma^2\ge {c_\sigma q e^{-\pi q}\over1+16q^2}
(q/2)^{2q'}\|p(q\,\cdot)\|_{L^2[1,2]}^2.
\]
The norm on the left is the full real-line norm. In the shifted orthonormal Legendre frame, the coefficient sum of the degree-\(j\) polynomial is
\(\sqrt{2j+1}P_j(5)\le\sqrt{2j+1}10^j\).
All its roots lie in \((1,2)\) by orthogonality and sign changes, so its coefficients alternate and evaluation at \(-1\) gives this sum. The bound on \(P_j(5)\) follows from
\[
P_j(x)=\pi^{-1}\int_0^\pi(x+\sqrt{x^2-1}\cos t)^jdt,
\]
whose summed generating series is \((1-2xz+z^2)^{-1/2}\).
Cauchy–Schwarz across degrees at most \(M\) yields
\[
\|\operatorname{coef}p(q\,\cdot)\|_1
\le(M+1)10^M\|p(q\,\cdot)\|_{L^2[1,2]}
\le\mathfrak A q^{-q'}\|Q_-p\|_\sigma.
\tag{RG39}
\]
Let an arbitrary finite error functional \(e\), through degree \(D\), satisfy
\(|e[y^n]|\le Hn!R^{-n}\).
Since \(n!\le D^n\), its coefficient pairing with \(Q_-p\) is bounded by the product of absolute coefficient sums at \(t=D/R\). All \(q'\) roots occur in
\(\sum|[y^j]Q_-|t^j\le(kR_h+t)^{q'}\), and
\(\sum|p_j|t^j\le\max(1,t/q)^M\sum|p_j|q^j\).
Therefore
\[
\|e|_{I_N}\|\le\mathfrak A H
(kR_h/q+D/(qR))^{q'}\max(1,D/(qR))^{D-q'}.
\tag{RG40}
\]
Only the finite envelope was used: no holomorphic continuation or cancellation property of the errors was assumed.

## RG14. Common-circle sampling in the original \(w\)-plane

For \(R\ge4\), write \(A_z(w)=\sum a_{z,n}w^n\), choose one integer \(T>D_{\max}\), and sample at \(w_j=(R/2)e^{2\pi ij/T}\). Define
\[
a_{z,n}^{[T]}={(R/2)^{-n}\over T}
\sum_{j=0}^{T-1}A_z(w_j)e^{-2\pi ijn/T},\qquad0\le n<T.
\]
The finite root-of-unity sum and absolute convergence give
\[
a_{z,n}^{[T]}-a_{z,n}
=\sum_{m\ge1}a_{z,n+mT}(R/2)^{mT},\qquad
|a_{z,n}^{[T]}-a_{z,n}|
\le M_k(R)R^{-n}{2^{-T}\over1-2^{-T}}\|z\|.
\tag{RG41}
\]
The bound holds on every combination of retained orthonormal rows. Keep the complete derivative phase and apply (RG40); \(D\le2q\), \(R\ge4\) make its last maximum one. The error on the whole lower ideal is
\[
\|\widehat{\mathcal R}_{I,N}-\mathcal R_{I,N}\|
\le H_{k,R}{2^{-T}\over1-2^{-T}},\qquad
H_{k,R}=\mathfrak A M_k(R)(kR_h/q+2/R)^{q'}.
\tag{RG42}
\]
These maps have source \(I_N\) in its full Gamma norm and target \(\mathbb C^s\) in the retained coefficient frame.

To compute the whole ideal, put
\[
\mathsf H_{I,N}[i,j]=\int_{\mathbb R}y^{i+j}|Q_-(y)|^2d\sigma(y),
\]
\[
F_N[z,j]=\sum_{t=0}^{q'}[y^t]Q_-\,(-i)^{t+j}(t+j)!a_{z,t+j},
\qquad 0\le i,j\le M.
\]
Then exactly
\[
C_N^R=F_N\mathsf H_{I,N}^{-1}F_N^*.
\tag{RG43}
\]
Indeed multiplication by \(Q_-\) has an injective coefficient matrix \(J_I\) whose image is the full evaluation kernel. In orthonormal source coordinates its orthogonal projector is \(J_I(J_I^*J_I)^{-1}J_I^*=P_N\). Expressing this identity in monomial coordinates gives (RG43). The mass \(M_\sigma\), all phases and the physical \(i^{q'}\) factor remain. A shared sampled coefficient prefix supplies all four cutoffs and every intermediate \(N\). Exact nested Gram restrictions preserve the source nesting for these approximated functionals.

## RG15. Relative perturbation, finite sample count and precision

Let \(L=\mathcal R_{I,N}\), so \(LL^*=C_N^R\succeq c_kI\). If
\(\|\widehat L-L\|\le\eta\sqrt{c_k}\), \(0<\eta<1/2\), then every target vector satisfies
\[
|\|\widehat L^*x\|-\|L^*x\||\le\eta\sqrt{c_k}\|x\|
\le\eta\|L^*x\|.
\]
Squaring proves
\[
(1-\eta)^2C_N^R\preceq\widehat C_N^R\preceq(1+\eta)^2C_N^R.
\tag{RG44}
\]
No second condition-number factor is needed.

Since \(s>0\), applying the true functional bound to a retained unit row gives \(H_{k,R}\ge\sqrt{c_k}\). A sufficient integer count is
\[
T=\max\left\{2q-v+1,\
\left\lceil\log_2{2H_{k,R}\over\eta\sqrt{c_k}}\right\rceil\right\}.
\tag{RG45}
\]
It gives \(2^{-T}\le\eta\sqrt{c_k}/(2H_{k,R})\le\eta/2<1/4\), so (RG42) is at most \(\eta\sqrt{c_k}\). The degree guard and ceiling remain explicit.

At \(R=k/L_k\),
\[
\log{H_{k,R}\over\sqrt{c_k}}=q'\log L_k+O(q),\qquad
T={q'\over\log2}\log L_k+O(q+\log(1/\eta)).
\tag{RG46}
\]
For the first equality, write
\(kR_h/q+2/R=(L_k/k)(2+k^2R_h/(qL_k))\); its final factor has a bounded positive logarithm on \(1\le L_k\le k/4\).
Combine with \(\frac12\log(1/c_k)=(q-1)\log(q/k)+O(q)\),
\(\log\mathfrak A=O(q)\), and \(\log M_k(R)=O(q/L_k+\log q)\).
The remaining \(\log k\) term is
\((q-1-q')\log k=(16k-49)\log k=O(q)\);
also \((q-1)\log(q/k^2)=O(k)\).
This proves the stated leading coefficient. Eventually \(\log L_k\to\infty\), so the degree guard contributes only \(O(q)\). In particular,
\[
L_k=\sqrt{\log(q+e)}
\quad\Longrightarrow\quad
T={q'\over2\log2}\log\log(q+e)+O(q+\log(1/\eta)).
\tag{RG47}
\]
This is \(T\) sample points per retained row, or \(T\) vector evaluations; it uses \(sT\) scalar values. It is distinct from CS1–24's total \(O(kq)\) complete-basis theorem, which uses different radii and retains every complementary row.

For \(\mathcal Rf=f_{q-1}+f_q-f_{2q-1}-f_{2q}\), the per-cutoff determinant errors in (RG44) lie between \(2s\log(1-\eta)\) and \(2s\log(1+\eta)\). Hence
\[
|\mathcal R\log\det\widehat C_N^R-\mathcal R\log\det C_N^R|
\le4s\log{1+\eta\over1-\eta}\le8s[-\log(1-\eta)].
\tag{RG48}
\]
For any \(\varepsilon>0\), use
\(\eta=\min\{1/4,1-e^{-\varepsilon/(8s)}\}\).
Then (RG48) is at most \(\varepsilon\), and the remainder in (RG47) is
\(O(q+\log^+(s/\varepsilon))\).

If each sampled row vector has Euclidean error at most \(\delta_{\rm eval}\), the coefficient envelope is \(\delta_{\rm eval}(R/2)^{-n}\) on every unit row combination. Equation (RG40) bounds the additional map error by
\[
\mathfrak A(kR_h/q+4/R)^{q'}\delta_{\rm eval}.
\tag{RG49}
\]
Add this to (RG42) before applying (RG44). Per-row scalar error \(\delta\) gives \(\delta_{\rm eval}\le\sqrt{s}\delta\).
If the full source Gram obeys
\((1-\tau)H\preceq\widehat H\preceq(1+\tau)H\), \(0\le\tau<1\),
its complete ideal has the same enclosure. Inversion changes the factors of (RG44) to
\((1-\eta)^2/(1+\tau)\) and \((1+\eta)^2/(1-\tau)\).
Errors in roots, periods, cancellation jets and row construction must enter these actual function, coefficient and Gram budgets, as specified in CS21–24. At canceled zeros, use the removable analytic quotient; a rounded \(0/0\) is not a valid sample.

## RG16. Full original arithmetic-kernel receiver

Keep \(g=q-q'-v\) and
\(\mathcal K_k=\mathcal R\log\det(I_K^*G_NI_K)\).
The exact finite scalar is
\[
\nu_{2j}=(2j)![t^{2j}](\cos t)^{-1/2},\quad\nu_{2j+1}=0,\quad
\Delta_n(a)=\det[\nu_{2a+i+j}]_{i,j=0}^n,\quad\Delta_{-1}=1,
\]
\[
\mathcal A_{k,v}=
{\Delta_{g-1}(q')\Delta_g(q')\Delta_{q-1}(q-v)\Delta_q(q-v)
\over\Delta_{q+g-1}(q')\Delta_{q+g}(q')\Delta_0(q-v)}.
\tag{RG50}
\]
The complete [published finite proof FI1–13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/FINITE_INVARIANT_PROOFS.md) proves on its original KF/CG finite guards
\[
|\mathcal K_k-\log\mathcal A_{k,v}+G_0+G_1|\le\mathcal E_k,
\tag{RG51}
\]
with its complete original error
\[
\mathcal E_k=B_{\rm KF49}^{\rm sharp}
+\sum_{N\in\{q-1,q,2q-1,2q\}}
[E_N^{\rm vol}+(M_N+1)E_{\chi'}+(L_N+1)E_{d,N}],
\]
\[
L_N=N-q,\quad M_N=L_N+g,\qquad
B_{\rm KF49}^{\rm sharp}=2m\Lambda_k+2s_k\log\kappa_k^*
+2B_k^{\rm ang}+2\sum_NE_N^*,\quad m=8k-16,
\]
\[
\Lambda_k=\log(u_k/\ell_{k,2q}),\quad
\ell_{k,2q}=a_k/[1+4(2q+25)^2]^{25},\quad u_k=A_k,
\]
\[
E_N^*=(N+1)\log M_{N-v}+J_{N-v},\quad
J_D=(D+1)\log^+(1/d_A),\quad
B_k^{\rm ang}=v\log\kappa_k^*+2v\log(1/\epsilon_k).
\tag{RG52}
\]
The constants \(a_k,A_k,M_D,\kappa_k^*,\epsilon_k\), CG24's \(E_N^{\rm vol}\), and CG18–20's exact \(E_{\chi'},E_{d,N}\) are the original quantities fully defined and proved in FI and its retained provider sources. They concern the arithmetic source, the complete polynomial factors and both original integration regions; they are not replaced by (RG4)'s coefficient-frame constants. FI gives
\(\Lambda_k=O(k+\log q)\), \(E_{\chi'}=O(1)\), \(E_{d,N}=O(\log q)\),
\(\mathcal E_k=O(q\log(q+2))\).
This continuation changes none of those original source factors or guards. Equation (RG51) is a proved finite determinant identity, not an assumed evaluation of a profile coefficient.

The physical coefficient map
\((c'+iy)^j=\sum_{a\le j}\binom ja(c')^{j-a}i^ay^a\)
has unit-modulus diagonal phases and is applied to the complete functional and Gram matrices. The full Gamma mass contributes the same dimension difference \(g\) at every cutoff; it cancels under the four signs only after those dimensions are retained. The conductor polynomial \(d_{\rm cond}(S')\) stays distinct from the scalar \(d_A\), with its complete leading coefficient and root factors present in FI's Gram identity.

Define
\(\mathcal K_{k,R}^{\rm ret}=\log\mathcal A_{k,v}-G_0^R-G_1^R\).
Equations (RG20),(RG51) prove the directed finite interval
\[
\mathcal K_{k,R}^{\rm ret}-\mathcal E_k-2\mathfrak D_k(h_R)
\le\mathcal K_k\le\mathcal K_{k,R}^{\rm ret}+\mathcal E_k.
\tag{RG53}
\]
If sampling has four-sign determinant error at most \(\varepsilon\), replace the retained receiver by its sampled value and enlarge each side's allowance by \(\varepsilon\).
The scalar \(g=16k-48-v\) remains unchanged; it is not the retained row rank \(s\).
At \(L_k=\sqrt{\log(q+e)}\), the full allowance is
\[
O\!\left(kq{1+\log\log(q+e)\over\sqrt{\log(q+e)}}+q\log(q+2)\right)=o(kq).
\tag{RG54}
\]
The original source-order comparison (RG36)–(RG38) adds its explicitly stated finite costs. The remaining projected covariance still contains every original lower-root constraint; its \(kq\)-coefficient has not been assigned a value.

## RG17. Verification scope

The companion check_growth.py checks noncommuting complex forms, restriction and attained-quotient interlacing, complete complementary Schur factors, inverse cross terms, all selected chronological subsets of its fixture, full-root innovations, unequal empirical masses, a radius-guard counterexample, coefficient aliasing and relative map perturbation. GROWTH_CHECKS.json and GROWTH_CHECKS_OPTIMIZED.json record test counts, exact witnesses and source hashes. These finite auxiliary fixtures supplement the proofs; they do not evaluate the period-dependent original row data. Existing AS and CS source bytes are preserved.

## Original human sources

R. A. Askey and R. Roy, DLMF Chapter 5, [original Gamma product, Eq. 5.8.3](https://dlmf.nist.gov/5.8.E3), supply the product used in RG13. T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, DLMF Chapter 18, supply [the Legendre generating function, Eq. 18.12.11](https://dlmf.nist.gov/18.12.E11), [the Meixner–Pollaczek recurrence, Eq. 18.22.8](https://dlmf.nist.gov/18.22.E8), and [its generating function, Eq. 18.23.7](https://dlmf.nist.gov/18.23.E7). The complete original formula TeX files, version 1.2.8 in the retained receipt, were read; their hashes and receiving calculations are listed in SOURCE_USE_LEDGER.json. The new relative-growth, attained-minimum, chronological, radius and Wasserstein results are the present derivation, not assertions attributed to those human sources.
