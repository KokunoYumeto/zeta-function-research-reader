# The original inverse and observed arithmetic action at critical activation

Independent mathematical derivation, 21 September 2026. This file proves the action conclusions in supplied equations (27)–(48). It supplies the exact covariance coisometry and the missing quantitative shear calculation. The original metric, polynomial minimum section, physical coordinate, observation, conductor coefficients, and period stratum are retained.

## 1. Sources and precise shared input

The supplied critical-activation text is retained as **SUPPLIED_CRITICAL_ACTIVATION.md** in this directory. Its equation (17), together with the logarithmic costs in (18), is proved independently as **HAR28–31** in the companion **HARMONIC_PROOFS.md**. That proof's **HAR41–48** evaluates the scalar endpoints and their clipped law. These precise provider sections were read for the present derivation. The present proof uses the harmonic enclosure for the inverse norm, observation fraction, action-source injectivity, common-subspace determinant cancellation, and action shear estimate. No action or singular-value conclusion is included in this input.

The finite inequalities retain every activation \(0\le\alpha\le1\). The critical limits in Sections 4 and 7–9 take \(\zeta,b\) fixed, or uniformly in bounded parameter ranges; the heat conclusions additionally require the displayed strict gaps to be bounded away from zero. They do not claim these critical limits uniformly over arbitrary moving physical activation parameters. For example \(\zeta_k=-2\log(q/k)\) gives \(\alpha_k=1\) and \(h_N(1)=1\); neither a superexponentially small singular value nor a vanishing shear follows there from the critical argument. The finite estimates still apply there.

Earlier source files inspected at the following exact proof locators:

- The original coordinate conductor, full-fibre minimum, source comparison and anchored division, **IVO1–6**, in the [pinned independent finite observation proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INDEPENDENT_FINITE_OBSERVATION.tex#L7). Its finite guards and inverse-power comparison are **IVO24–26**, [in the same verified file](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INDEPENDENT_FINITE_OBSERVATION.tex#L258). Local TeX SHA-256: `d9889e4493c966dcd712e9a10840004794d4d41a79a91c8c9393ce15d7ac2e1e`, equal to the retained full-byte publication receipt.
- The original inverse decomposition and Gamma evaluation/anchored-division estimates, **S11–16**, in the [pinned smallest-singular proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/NATIVE_SMALLEST_SINGULAR_PROOF.tex#L64). Local TeX SHA-256: `c7dd360325dc475b82cabbc65f2dc01d5c67711b85951a1837cd3e7f52415bbb`, equal to that receipt.
- The original observed isometry **IFH1**, full flag minima **IFH2–7**, and relative measured-heat argument **IFH11–13**, in the [pinned original inverse-flag proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INVERSE_FLAG_AND_RELATIVE_HEAT.tex#L17). Local TeX SHA-256: `468c92ee4224a3659be44f122efb9fbfc0c2a469624ff5da6d16280aa069a6ca`.
- The retained activation source **A23–25** contains the earlier covariance coisometry for the outgoing action; **A38** retains the same full spectral-polynomial receiver. Those sections were read, and the construction is proved again for the inverse below.
- The received dual spectral-pencil proof **D1–2** contains the determinant formula. Its whole determinant calculation is reproduced in Section 8 below.

The source-reading ledger was used before these files were opened. The continuation's claimed inverse-observation byte identity differs from our retained accepted supplied proof: the latter has 29,503 bytes and SHA-256 `78b06adf8aa4065dacd76f901515d8fe88c736672107f4d6859892f3ce5fcd19`. We use the actual accepted IFH/IVO providers, not an unseen claimed-identical file. No PDF was read.

The human sources retained by IVO include DLMF Chapter 18 by T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw, with W. P. Reinhardt, especially Meixner–Pollaczek generating function 18.23.E7 and recurrence 18.22.E8. The finite consequences needed here are proved in IVO5–6. The original Gamma source mass remains \(\sqrt{2\pi}\).

Keep
\[
q=(k+1)^2,\quad k\equiv1\pmod4,\quad 0<\delta<1/2,\quad\gamma>2,\quad
R_0=(\delta^2+\gamma^2)^{1/2},
\]
\[
Q_k(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta],\quad
E_k=\mathbb C[y]/(Q_k),\quad M[p]=[yp].
\]
The original coordinate is \(S=k/2+iy\). Since \(Q_k(0)\ne0\), \(M\) is invertible; every root has modulus at least \(R_0\).

Fix a cutoff \(N\). Put \(G_0=G_N\), \(G_1=G_N^J\), and
\[
G_\alpha^{-1}=(1-\alpha)G_0^{-1}+\alpha G_1^{-1},\quad0\le\alpha\le1.
\tag{ACT1}
\]
The joint source contains the canonical source, so \(G_1\preceq G_0\).
Consequently \(G_1\preceq G_\alpha\preceq G_0\); for \(\alpha>0\),
\(G_\alpha\preceq\alpha^{-1}G_1\).

Retain
\[
Q_\alpha=(\Lambda G_\alpha^{-1}\Lambda^*)^{-1},\quad
L_\alpha=G_\alpha^{-1}\Lambda^*Q_\alpha,\quad P_{B,\alpha}=L_\alpha\Lambda.
\]
Direct multiplication gives \(\Lambda L_\alpha=I\), \(L_\alpha^*G_\alpha L_\alpha=Q_\alpha\), and \(\Lambda=L_\alpha^\dagger\); \(P_{B,\alpha}\) is the original orthogonal observed projection.

For \(U_dz=\sum_{j=1}^dz_j[y^{-j}]\), write
\(H^E_{d,\alpha}=U_d^*G_\alpha U_d\) and
\(H^B_{d,\alpha}=U_d^*\Lambda^*Q_\alpha\Lambda U_d\).
The shared harmonic lemma states
\[
e^{-E_{d,N}}h_N(\alpha)I_d\preceq H^B_{d,\alpha}\preceq H^E_{d,\alpha}
 \preceq e^{E_{d,N}}h_N(\alpha)I_d,\qquad
h_N(\alpha)=\frac{\mathsf S_N}{1-\alpha+\alpha\mathsf S_N},
\tag{ACT2}
\]
where \(E_{d,N}=o(q)\) for \(d\log(q+2)=o(q)\). It follows from the explicit \(L_{d,N},U_{d,N}\) in supplied (17); no metric is rescaled.

Every use retains the IVO guards at the enclosing rank \(d\): \(d\le q\),
\(q_-\ge16\), \(R_k\le2^{-14}q_-\), \(n_-+2\le2q_-\), and the complete absorption guard IVO24 with \(n_-=N-v+Jd-q_-\), together with the shared harmonic lemma's guards. Sections 5–7 also retain \(J(r-1)+1\le q_-\), \(r+v\le q\), and \(v\le N\). These are actual finite domain restrictions and hold eventually in the stated growth regime.

## 2. Original polynomial inverse and covariance transport

Let \(\widehat R_N:E_k\to\mathcal P_N\) be the actual canonical scalar minimum section and \(J_N:\mathcal P_N\to E_k\) its remainder map. The hat distinguishes this section from the coefficient left inverse also called \(R_N\) in supplied (14). Define
\[
\mathscr Dp=(p-p(0))/y,\quad B_N=J_N\mathscr D\widehat R_N,\quad
\ell_Nx=(\widehat R_Nx)(0),\quad u=[y^{-1}].
\]
The functional evaluates the specified polynomial representative, not the quotient algebra at zero. Multiplication gives \(MB_Nx=x-\ell_N(x)[1]\) and \(Mu=[1]\), hence
\[
\boxed{T:=M^{-1}=B_N+u\ell_N.}\tag{ACT3}
\]
The S11 vector \([(Q_k-Q_k(0))/y]\) equals \(-Q_k(0)u\), so the original factor and matched row agree exactly.

IVO3 and IVO6 give
\[
\|B_N\|_{G_0}\le
D_N:=\mathfrak d_N\sqrt{u_k/\ell_{k,N}},\quad
\mathfrak d_N=2\sqrt{2N+1}\left(\sum_{j=1}^N\frac1j\right)(1+\sqrt{N+1}).
\tag{ACT4}
\]
Indeed \(J_N\) is a contraction to the attained metric and \(\widehat R_N\) is an isometry; the two source comparisons apply to the actual polynomials before and after division. S14/IVO6 also gives
\[
\|\ell_N\|_{G_0^{-1}}\le
F_N:=\sqrt{\frac{N+1}{\ell_{k,N}\sqrt{2\pi}}}.
\tag{ACT5}
\]
Here \(K_{\sigma,N}(0,0)\le(N+1)/\sqrt{2\pi}\), with original mass retained.

In \(T_k=\operatorname{diag}(W_\omega)\), \(T\) is diagonal with entries \(1/\omega\); \(\|T\|_{T_k}=R_0^{-1}\). Therefore
\[
\|T\|_{G_1}\le J_N^{\rm inv}:=\frac{\sqrt{\mathbf L_k\mathbf B_k}}{R_0}.
\tag{ACT6}
\]
The superscript distinguishes this scalar bound from the remainder map.

Define
\[
\mathcal J_\alpha:E_{G_0}\oplus E_{G_1}\to E_{G_\alpha},\qquad
\mathcal J_\alpha(x_0,x_1)=\sqrt{1-\alpha}\,x_0+\sqrt\alpha\,x_1.
\]
Its actual adjoint is
\[
\mathcal J_\alpha^\dagger z=
(\sqrt{1-\alpha}\,G_0^{-1}G_\alpha z,\sqrt\alpha\,G_1^{-1}G_\alpha z).
\]
Equation (ACT1) proves \(\mathcal J_\alpha\mathcal J_\alpha^\dagger=I\).
Thus it is a coisometry and its adjoint is an isometry. For every fixed coefficient operator \(A\),
\[
A=\mathcal J_\alpha\operatorname{diag}(A,A)\mathcal J_\alpha^\dagger,\qquad
\|A\|_{G_\alpha}\le\max(\|A\|_{G_0},\|A\|_{G_1}).
\tag{ACT7}
\]
The equality retains factor order
\(A[(1-\alpha)G_0^{-1}+\alpha G_1^{-1}]G_\alpha=A\).

Apply the same map to \(\operatorname{diag}(B_N,T)\) and retain the canonical rank-one term separately:
\[
\boxed{T=B_{\alpha,N}+(1-\alpha)u\ell_NG_0^{-1}G_\alpha,}\tag{ACT8}
\]
\[
B_{\alpha,N}=(1-\alpha)B_NG_0^{-1}G_\alpha+\alpha TG_1^{-1}G_\alpha,\qquad
\|B_{\alpha,N}\|_{G_\alpha}\le\overline D_N:=\max(D_N,J_N^{\rm inv}).
\tag{ACT9}
\]
The moving dual row is exact. Neither selfadjointness nor nilpotence of these terms is asserted. The inherited finite source costs imply
\(\log^+\overline D_N=O_h(k\log^2(q+2))=o(q)\).

## 3. Inverse norm and every remaining singular direction

Here are explicit constants for supplied (28). Put
\[
s=\mathsf S_N,\quad b=b_{1,N},\quad m_k=M_h(0)^k,\quad
c_0=(D_N/\sqrt s+\sqrt b\,F_N)^2,\quad
C_0=\max(c_0,(J_N^{\rm inv})^2/s).
\]
The canonical \(r=1\) bound gives \(\|u\|_{G_0}^2\le bs\), so (ACT3) implies \(\|T\|_{G_0}^2\le c_0s\), and (ACT7) gives \(\|T\|_{G_\alpha}^2\le C_0s\).
For \(\alpha>0\),
\[
\|Tx\|_{G_\alpha}^2\le\alpha^{-1}\|Tx\|_{G_1}^2
\le\alpha^{-1}(J_N^{\rm inv})^2\|x\|_{G_1}^2
\le\alpha^{-1}(J_N^{\rm inv})^2\|x\|_{G_\alpha}^2.
\]
Thus
\[
\|T\|_{G_\alpha}^2
\le\min(C_0s,(J_N^{\rm inv})^2/\alpha)
\le[C_0+(J_N^{\rm inv})^2]h_N(\alpha).
\tag{ACT10}
\]
For the last step, the minimum \(z\) satisfies \(z\le C_0s\) and
\(\alpha sz\le(J_N^{\rm inv})^2s\). Adding and using
\(1-\alpha+\alpha s\le1+\alpha s\) proves it. The endpoint \(\alpha=0\) follows directly.

For the lower bound \(T[1]=u\), and the unchanged polynomial \(1\) gives
\(\|[1]\|_{G_\alpha}^2\le m_k\). The \(r=1\) harmonic bound yields
\[
\|T\|_{G_\alpha}^2\ge\|u\|_{G_\alpha}^2/m_k
\ge L_{1,N}h_N(\alpha)/m_k.
\tag{ACT11}
\]
Consequently
\[
\boxed{c_{-,N}=L_{1,N}/m_k,\quad c_{+,N}=C_0+(J_N^{\rm inv})^2,\quad
c_{-,N}h_N(\alpha)\le\|T\|_{G_\alpha}^2\le c_{+,N}h_N(\alpha).}
\tag{ACT12}
\]
On the eventual original domain \(s\ge1\),
\(|\log c_{\pm,N}|=O_{h,A}(k\log^2(q+2))\).
For \(c_+\), use the bounds on \(D_N,F_N,b,J_N^{\rm inv}\) and the fixed lower bound \(J_N^{\rm inv}\ge R_0^{-1}\); the latter follows because the joint sandwich requires \(\mathbf L_k\mathbf B_k\ge1\).
For \(c_-\), use \(|\log L_{1,N}|\le E_{1,N}\) and
\(|\log m_k|=O_h(k)\). The finite inequality holds before the eventual guard as well.

Order \(\sigma_1(T)\ge\cdots\ge\sigma_q(T)>0\).
On the codimension-at-most-one kernel of the rank-one row in (ACT8), \(T\) equals \(B_{\alpha,N}\). Singular min–max therefore proves
\[
\sigma_j(T;G_\alpha)\le\overline D_N\quad(2\le j\le q).
\tag{ACT13}
\]
For the original \(M\), order singular values increasingly. Then
\[
s_1(M)^2=\|T\|^{-2},\quad s_j(M)\ge\overline D_N^{-1}\ (j\ge2),\qquad
-\log s_1(M)^2=\log h_N(\alpha)+O_{h,A}(k\log^2(q+2)).
\tag{ACT14}
\]
All remaining \(q-1\) directions are retained.

If \(L=\|T\|>\overline D_N\), the top singular value is simple by (ACT13).
For unit vectors \(Tv=Lw\), projecting (ACT8) away from \(\mathbb Cu\) gives
\(\|(I-P_u)w\|\le\overline D_N/L\).
The trace norm of the difference of two rank-one orthogonal projections is twice the sine of their angle. Hence
\[
\|P_{\min,N}-P_u\|_1\le2\overline D_N/L=2\overline D_Ns_1(M).
\tag{ACT15}
\]
The top left singular line of \(T\) is exactly the minimum right singular line of \(M\), with the original \(G_\alpha\)-orthogonal projections.

## 4. Full observed heat and its actual observation fraction

The \(r=1\) harmonic enclosure gives
\[
\theta_N(\alpha)=\frac{\|\Lambda u\|_{Q_\alpha}^2}{\|u\|_{G_\alpha}^2}
\ge L_{1,N}/U_{1,N}>0,\qquad -\log\theta_N(\alpha)\le2E_{1,N}.
\tag{ACT16}
\]
On the finite guard \(\|T\|_{G_\alpha}>\overline D_N\) from (ACT15), the full positive heat \(Z(\tau)=e^{-\tau M^\dagger M}\) satisfies, by (ACT13) and (ACT15),
\[
\|Z(\tau)-e^{-\tau s_1^2}P_u\|_1
\le2\overline D_Ns_1e^{-\tau s_1^2}+(q-1)e^{-\tau/\overline D_N^2}.
\tag{ACT17}
\]
The complete observed trace is
\[
\Theta_N(\tau;\alpha)=\operatorname{Tr}_B(\Lambda Z(\tau)L_\alpha)
=\operatorname{Tr}_E(P_{B,\alpha}Z(\tau)).
\]
Since \(P_{B,\alpha}\) is an orthogonal projection,
\(|\operatorname{Tr}(P_{B,\alpha}X)|\le\|X\|_1\), and
\(\operatorname{Tr}(P_{B,\alpha}P_u)=\theta_N\). Therefore
\[
\left|\frac{\Theta_N(\tau;\alpha)}{\theta_Ne^{-\tau s_1^2}}-1\right|
\le\frac{2\overline D_Ns_1}{\theta_N}
+\frac{q-1}{\theta_N}e^{-\tau(\overline D_N^{-2}-s_1^2)}.
\tag{ACT18}
\]
This is supplied (33), extending the original [IFH11 relative estimate](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INVERSE_FLAG_AND_RELATIVE_HEAT.tex#L200) through the actual activation. The same finite guard is retained in (ACT18); (ACT12) and the following fixed-parameter critical scale prove it eventually.

Put \(\ell_k=\log(q/k)\). The independently proved endpoints **HAR41–44** and harmonic clipping **HAR45–47** in **HARMONIC_PROOFS.md** give, in particular for fixed \(\zeta\), uniformly on bounded \(\zeta\)-ranges,
\[
\log h_N(\alpha_k(\zeta))=2q\ell_k+q\kappa_{L/H}(\zeta)+o(q),\qquad
\kappa_{L/H}(\zeta)=\min(\beta_{L/H},\zeta).
\tag{ACT19}
\]
This is the only additional limiting input used here. The scalar enclosure itself is uniform on the larger physical domain \(\zeta\ge-2\ell_k\), as HAR47 proves; the singular separation and heat argument that follows uses the fixed or bounded parameter scope stated above. At
\(\tau_k(b)=e^{2q\ell_k+bq}\), the right side of (ACT18) tends to zero:
\(s_1=e^{-q\ell_k+O(q)}\), \(\overline D_N=e^{o(q)}\), and
\(\theta_N\ge e^{-o(q)}\). Moreover
\[
\tau_k(b)s_1^2=\exp\{q[b-\kappa_{L/H}(\zeta)]+o(q)\}.
\]
When \(\kappa_H(\zeta)<b<\kappa_L(\zeta)\), both low heat factors tend to one; both high factors are at most \(e^{-e^{cq}}\) for some \(c>0\). The two low observation weights are at least \(e^{-o(q)}\). Under the original signs \(+,+,-,-\), they dominate the high terms, proving
\[
\mathcal R\Theta_N(\tau_k(b);\alpha_k(\zeta))>0\text{ eventually},\qquad
q^{-1}\log\mathcal R\Theta_N(\tau_k(b);\alpha_k(\zeta))\to0.
\tag{ACT20}
\]
No unweighted limit is assigned to this measured full heat.

For \(\alpha=e^{-2\theta q}\), \(\theta>0\), the original scalar scales give
\(\alpha\mathsf S_N\to\infty\), so the exact harmonic formula gives
\(\log h_N=2\theta q+o(1)\). Thus \(s_1=e^{-\theta q+o(q)}\) while every \(s_j\), \(j\ge2\), is at least \(e^{-o(q)}\).
The **full unobserved trace** at time \(e^{2\sigma q}\) tends to one for
\(0<\sigma<\theta\) and to zero for \(\sigma>\theta\); the other \(q-1\) heat terms are bounded by
\(q\exp[-\exp(2\sigma q-o(q))]\to0\).

## 5. The fixed observed arithmetic map and its full target minimum

Keep the actual nonzero conductor coefficients \(a_j\), shifts
\[
b_j=4+(2r_j-8)\delta+i(2s_j-8)\gamma,\quad \zeta_j=i(b_j-4),
\]
and \(E_A(z)=\sum_ja_je^{b_jz}\). Let
\(v=\operatorname{ord}_0E_A\), so \(\mu_v\ne0\) and \(v\le J-1\le80\).
IVO1 gives \(C_Af(y)=\sum_ja_jf(y-\zeta_j)\). Its symbol is
\(e^{-4z/i}E_A(z/i)\), whose first nonzero derivative is \(i^{-v}\mu_v\).
Expansion of the monomial therefore proves exactly
\[
C_A[y^v]=i^{-v}\mu_v.
\tag{ACT21}
\]
This needs no assumption \(\Lambda[1]\ne0\).

Define
\[
W_r^{(v)}d=d_1[y^{-1}]+\sum_{j=2}^rd_j[y^{-(v+j)}].
\]
It is the literal coordinate subspace with index set
\(J_v=\{1,v+2,\ldots,v+r\}\) inside \(U_{r+v}\); (ACT2) makes
\(\Lambda W_r^{(v)}\) injective. Original multiplication gives
\[
M^{v+1}W_r^{(v)}d=d_1[y^v]+\sum_{j=2}^rd_j[y^{-(j-1)}].
\tag{ACT22}
\]

We prove the distance of the first target column from the others through every original observed-fibre correction. Put
\[
\begin{gathered}
L=J(r-1),\quad B(y)=\prod_j(y-\zeta_j)^{r-1},\\
t_*=\max(1,(R_-+Z)/(2\delta)),\quad R_-=(k-8)R_0,\quad Z=\max_j|\zeta_j|.
\end{gathered}
\]
For every \(d\in\mathbb C^{r-1}\),
\[
f(y)=C_A(y^v+U_{r-1}d)=i^{-v}\mu_v+
 \sum_{j,n}\frac{a_jd_n}{(y-\zeta_j)^n}.
\]
The polynomial \(Bf\) has degree \(L\) and leading coefficient
\(i^{-v}\mu_v\); each proper rational term has numerator degree at most \(L-1\).

Choose \(L+1\) distinct original lower roots \(\eta_0,\ldots,\eta_L\).
The guard \(L+1\le q_-\) permits this. Distances are at least \(2\delta\), moduli at most \(R_-\), and none is a pole. Lagrange's exact leading-coefficient formula gives
\[
i^{-v}\mu_v=\sum_{s=0}^L
 \frac{B(\eta_s)f(\eta_s)}{\prod_{t\ne s}(\eta_s-\eta_t)}.
\]
The coefficients have moduli at most \(t_*^L\). Cauchy–Schwarz proves
\[
\|C_A(y^v+U_{r-1}d)\|_2^2
\ge\frac{|\mu_v|^2}{(L+1)t_*^{2L}}.
\tag{ACT23}
\]
The full lower-root norm is at least its selected-node norm.

Each shifted lower grid is a subset of the upper grid, so each restriction has Euclidean norm at most one. Thus
\[
\|C_Aw\|_2\le A_1\|w\|_2\le A_1a_{\min}^{-k/2}\|w\|_{T_k},
\qquad A_1=\sum_j|a_j|.
\]
IVO2 gives \(\ker\Lambda\subseteq\ker C_A\). Every lift \(w\) of the observed class \(\Lambda(y^v+U_{r-1}d)\) therefore has the same conductor image.
Since \(G_\alpha\succeq\mathbf L_k^{-1}T_k\),
\[
\|w\|_{G_\alpha}^2\ge
\frac{a_{\min}^k}{\mathbf L_kA_1^2}\|C_A(y^v+U_{r-1}d)\|_2^2.
\]
Minimizing first over the entire original observed fibre and then over \(d\) gives
\[
d_-\le\rho:=
\operatorname{dist}_{Q_\alpha}(\Lambda[y^v],\Lambda U_{r-1})^2\le d_+,
\tag{ACT24}
\]
\[
d_-=\frac{a_{\min}^k|\mu_v|^2}
 {\mathbf L_kA_1^2(L+1)t_*^{2L}},\qquad
d_+=u_k\int_\mathbb R y^{2v}\,d\sigma(y).
\]
The upper bound uses \(d=0\), the allowed polynomial \(y^v\),
\(G_\alpha\preceq G_0\), and the original source comparison. In fact it also proves
\[
a:=\|\Lambda[y^v]\|_{Q_\alpha}^2\le d_+.
\tag{ACT25}
\]
This bound on the **whole first-column norm**, not only \(\rho\), controls the shear below.

The original Gamma moment is finite and positive. With fixed original nonzero \(\mu_v\), the inherited source costs give
\[
\max(|\log d_-|,|\log d_+|)
=O_{h,A}(k\log^2(q+2)+Jr\log(q+2))=o(q).
\tag{ACT26}
\]
This concerns the fixed admitted period stratum and its actual first nonzero moment; it does not assert a uniform constant while that moment tends arbitrarily fast to zero.

Equation (ACT24) proves independence of \(\Lambda[y^v],\Lambda U_{r-1}\). Therefore the map between the exact original observed subspaces
\[
\mathscr A_r^{(v)}(\Lambda W_r^{(v)}d)
=\Lambda M^{v+1}W_r^{(v)}d
\tag{ACT27}
\]
is well defined and bijective onto its target. Both metrics are restrictions of \(Q_\alpha\). This is not \((\Lambda ML_\alpha)^{v+1}\).

## 6. Exact common-subspace cancellation in the determinant

Let \(I=\{1,\ldots,r-1\}\), \(J=J_v\), \(C=I\cap J\), and denote the corresponding original observed inverse-power Grams by \(H_I,H_J,H_C\).
They come from the same \(H^B_{r+v,\alpha}\). Schur factorization gives
\[
\det H_I=\det H_C\det S_I,\qquad
\det H_J=\det H_C\det S_J,
\]
with empty determinant one. These are complete attained coefficient metrics after minimizing over the same common coordinate subspace.

Put \(h=h_N(\alpha)\), \(E=E_{r+v,N}\), \(l=e^{-E}\), \(u_*=e^E\).
The harmonic enclosure gives
\[
lhI\preceq S_I,S_J\preceq u_*hI.
\tag{ACT28}
\]
For the lower inequality, every extension of a specified remaining coefficient vector has at least its Euclidean norm; for the upper inequality, set eliminated coordinates to zero. These two facts and (ACT2), followed by the actual minima, prove the claim without interchanging restriction and inversion.

Write \(i=|I\setminus C|\), \(j=|J\setminus C|\). Then \(j=i+1\) and \(i+j\le2v+1\): for \(r\ge v+3\), \(i=v,j=v+1\); for \(2\le r\le v+2\), \(C=\{1\}\) and \(i+j=2r-3\); for \(r=1\), \(i=0,j=1\).

The target determinant is \(\rho\det H_I\), while the source determinant is \(\det H_J\). Hence exactly
\[
\mathscr J_{r,N}^{(v)}(\alpha)=\rho\,\det S_I/\det S_J.
\]
Therefore
\[
\boxed{|\log\mathscr J_{r,N}^{(v)}(\alpha)+\log h_N(\alpha)|
\le(2v+1)E_{r+v,N}+\max(|\log d_-|,|\log d_+|).}
\tag{ACT29}
\]
The common determinant cancels before estimation. There is no factor \(r\) multiplying its error.

The right side is \(o(q)\). From (ACT19), with original four-cutoff signs,
\[
\mathcal R\log\mathscr J_{r,N}^{(v)}(\alpha_k(\zeta))
=-2q[\kappa_L(\zeta)-\kappa_H(\zeta)]+o(q)
=-\mathfrak C_{\rm inv}(\zeta)q+o(q).
\tag{ACT30}
\]
At the canonical source the result is \(-\mathfrak Cq+o(q)\). This proves supplied (39)–(40) and (3).

## 7. Every action singular value, with the complete shear

The determinant does not by itself determine all singular scales. The extra estimate is (ACT25).

In the literal source coefficient basis, its Gram is \(S=H_J\); write the target Gram
\[
V=\begin{pmatrix}a&b^*\\b&K\end{pmatrix},\qquad K=H^B_{r-1,\alpha}.
\]
For \(r=1\), interpret \(K,b\) as empty. Put
\[
c=K^{-1}b,\quad \rho=a-b^*K^{-1}b,\quad
\mathcal T_c=\begin{pmatrix}1&0\\c&I\end{pmatrix}.
\]
The complete square is the exact congruence
\[
V=\mathcal T_c^*\begin{pmatrix}\rho&0\\0&K\end{pmatrix}\mathcal T_c.
\tag{ACT31}
\]
All cross terms remain. From \(K\succeq lhI\) and \(a\le d_+\),
\[
\|c\|^2=b^*K^{-2}b\le\frac{b^*K^{-1}b}{lh}\le\frac{d_+}{lh}.
\tag{ACT32}
\]
The nontrivial singular values of \(\mathcal T_c\) are
\[
\chi(c)=\frac{\sqrt{4+\|c\|^2}+\|c\|}{2},\qquad\chi(c)^{-1}.
\]
Its restriction to the span of the first coordinate and \((0,c)\) has squared-singular determinant one and trace \(2+\|c\|^2\); on the orthogonal complement it is the identity. This proves the formula and
\(\|\mathcal T_c\|=\|\mathcal T_c^{-1}\|=\chi(c)\).

Let \(\delta_1\le\cdots\le\delta_r\) be the eigenvalues of
\(\operatorname{diag}(\rho,K)\), and \(s_1\le\cdots\le s_r\) all the singular values of (ACT27) in its original metrics. Their squares are the generalized eigenvalues of \((V,S)\). Congruence (ACT31), min–max, and \(lhI\preceq S\preceq u_*hI\) give
\[
\boxed{\frac{\delta_j}{u_*h\chi(c)^2}\le s_j^2
\le\frac{\chi(c)^2\delta_j}{lh},\qquad1\le j\le r.}
\tag{ACT33}
\]
For the congruence estimate, substitute \(z=\mathcal T_cx\) in the Rayleigh quotient and use
\(\chi^{-2}\|z\|^2\le\|x\|^2\le\chi^2\|z\|^2\).
The invertible substitution preserves dimensions and sends all subspaces bijectively to subspaces in the min–max formula. The source comparison is a second Rayleigh estimate on those same coefficient subspaces.

Equation (ACT33) holds at every activation on the finite domain, recording all shear amplification. On the explicit finite guard \(lh\ge d_+\), the smallest diagonal eigenvalue is \(\rho\), and the other \(r-1\) are the eigenvalues of \(K\). Thus
\[
\boxed{\frac{d_-}{u_*h\chi^2}\le s_1^2\le\frac{d_+\chi^2}{lh},\qquad
\frac{l}{u_*\chi^2}\le s_j^2\le\frac{u_*\chi^2}{l}\quad(2\le j\le r).}
\tag{ACT34}
\]
The upper bound on \(s_1^2\) improves to \(d_+/(lh)\) by testing
\((1,-c)\), whose target squared norm is \(\rho\).

At critical activation, (ACT19), \(E=o(q)\), and (ACT26) imply
\[
\log(lh/d_+)=2q\ell_k+O(q)\to+\infty.
\]
Hence the finite guard holds eventually, and
\(\|c\|\le e^{-q\ell_k+O(q)}\to0\), so \(\chi(c)\to1\). Every singular direction therefore satisfies
\[
-\log s_1^2=\log h_N(\alpha_k(\zeta))+o(q),\qquad
|\log s_j^2|=o(q)\quad(2\le j\le r),
\tag{ACT35}
\]
uniformly in \(j\). The smallest value is eventually simple by its strict separation from the lower bound for \(s_2\).

The complete unweighted domain heat obeys
\[
e^{-\tau s_1^2}\le
\operatorname{Tr}_{\Lambda W_r^{(v)}}e^{-\tau(\mathscr A_r^{(v)})^\dagger
 \mathscr A_r^{(v)}}
\le e^{-\tau s_1^2}+(r-1)e^{-\tau l/(u_*\chi^2)}.
\tag{ACT36}
\]
At \(\tau_k(b)=e^{2q\ell_k+bq}\), its second term tends to zero:
\(r\le q\), \(l/(u_*\chi^2)=e^{-o(q)}\).
The first term tends to one at both low cutoffs and zero at both high cutoffs whenever
\(\kappa_H(\zeta)<b<\kappa_L(\zeta)\). Therefore
\[
\boxed{\mathcal R\operatorname{Tr}
e^{-\tau_k(b)(\mathscr A_r^{(v)})^\dagger\mathscr A_r^{(v)}}\to2.}
\tag{ACT37}
\]
This proves the unweighted action heat through every singular value.

The need for control of \(a\) has an exact two-dimensional example. Take \(h>1\), source \(S=hI_2\), and target
\[
V_h=\begin{pmatrix}1+h^3&h^2\\h^2&h\end{pmatrix}.
\]
Here \(K=h,\rho=1,\det V_h/\det S=1/h\), but the shear is \(c=h\).
The squared singular values have product \(1/h\) and sum \(h^2+1+1/h\); one grows like \(h^2\), the other decays like \(h^{-3}\). A controlled inverse block and Schur remainder alone would not prove (ACT35). The original bound \(a\le d_+\) excludes precisely this uncontrolled amplification.

## 8. The original small-regularizer edge and full source cost

Use the fixed original \(G_0\)-isometric frame
\[
M_0=G_0^{1/2}MG_0^{-1/2},\quad
C_\alpha=G_0^{1/2}G_\alpha^{-1}G_0^{1/2}=I+\alpha\mathsf K_N.
\]
The metric there is \(C_\alpha^{-1}\) and
\(M_0^\dagger=C_\alpha M_0^*C_\alpha^{-1}\).
The identity \(\det(aI+XY)=\det(aI+YX)\) gives
\[
\det(aI+M^\dagger M)
=\frac{\det(aC_\alpha+M_0C_\alpha M_0^*)}{\det C_\alpha}
=:\frac{\mathscr P_N(a,\alpha)}{\det(I+\alpha\mathsf K_N)}.
\tag{ACT38}
\]
This rederives dual pencil D2 at the exact original activation.
At zero,
\[
\mathscr P_N(0,\alpha)=|\det M|^2\det C_\alpha,\qquad
\Delta_N(\alpha)=\log\det G_0-\log\det G_\alpha=\log\det C_\alpha.
\tag{ACT39}
\]

For \(T=M^{-1}\), \((M^\dagger M)^{-1}=TT^\dagger\), and \(T^\dagger T\) has the same eigenvalues. Factoring \(M^\dagger M\) and applying the determinant identity proves
\[
\boxed{\mathscr P_N(a,\alpha)/\mathscr P_N(0,\alpha)=\det(I+aT^\dagger T).}
\tag{ACT40}
\]
Adjoints use \(G_\alpha\). This is a determinant equality, not an operator equality.

All \(q\) singular directions are in
\[
\log\det(I+aT^\dagger T)=\log(1+a\|T\|^2)
 +\sum_{j=2}^q\log(1+a\sigma_j(T)^2).
\]
By (ACT13) and \(0\le\log(1+x)\le x\),
\[
0\le\log\det(I+aT^\dagger T)-\log(1+a\|T\|^2)
\le(q-1)a\overline D_N^2.
\tag{ACT41}
\]
At \(a_k(b)=e^{-2q\ell_k-bq}\), this upper remainder tends to zero.
Equations (ACT12) and (ACT19) yield
\(\log(a_k(b)\|T\|^2)=q[\kappa_{L/H}(\zeta)-b]+o(q)\).
Since \(0\le\log(1+e^x)-x_+\le\log2\),
\[
\boxed{\frac1q\log
\frac{\mathscr P_N(a_k(b),\alpha_k(\zeta))}
{\mathscr P_N(0,\alpha_k(\zeta))}
\longrightarrow[\kappa_{L/H}(\zeta)-b]_+.}
\tag{ACT42}
\]
Threshold equality is included.

The exact two-metric receiver retains the full source cost:
\[
\log\frac{\mathscr P_N(a,\alpha)}{\mathscr P_N(a,0)}-\Delta_N(\alpha)
=\log\det(I+aT^{\dagger_{G_\alpha}}T)
 -\log\det(I+aT^{\dagger_{G_0}}T).
\tag{ACT43}
\]
Indeed division of (ACT40) at \(\alpha\) by its value at zero leaves
\(\mathscr P_N(0,\alpha)/\mathscr P_N(0,0)=\det C_\alpha\), with logarithm exactly \(\Delta_N\).

For general critical \(\zeta,b\), the four-cutoff return in (ACT43), divided by \(q\), therefore tends to
\[
2\bigl\{[\min(\beta_L,\zeta)-b]_+
-[\min(\beta_H,\zeta)-b]_+
-[\beta_L-b]_++[\beta_H-b]_+\bigr\}.
\tag{ACT44}
\]
This gives the complete clipped small-regularizer receiver, including thresholds.

## 9. Concrete simultaneous activation, action volume, and heat

Put
\[
a_0=\log(4/\pi)>0,\quad \beta_*=-2-I_\square,\quad
\beta_L=\beta_*+2a_0,\quad
\beta_H=\beta_*+2a_0-\mathfrak C/2,\quad
\zeta_\diamond=\beta_*+a_0.
\]
The inherited certified interval
\(1353893/10^6<\mathfrak C<1354751/10^6\)
is [S9 in the pinned source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/NATIVE_SMALLEST_SINGULAR_PROOF.tex#L55), with \(\mathfrak C=-\mathfrak c_{\min}\).
It implies \(\mathfrak C>4a_0\): \(\pi>3\) and
\(\log(4/3)<1/3\) give \(4a_0<4/3<1353893/10^6\). Consequently
\[
\beta_H<\beta_*<\zeta_\diamond<\beta_L.
\tag{ACT45}
\]
Take the original explicit values
\[
\alpha_k^\diamond=e^{-2q\ell_k-\zeta_\diamond q},\qquad
\tau_k^*=e^{2q\ell_k+\beta_*q}.
\]
The latter is exactly the [earlier original late time IFH13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INVERSE_FLAG_AND_RELATIVE_HEAT.tex#L261).

Since \(\kappa_L(\zeta_\diamond)=\zeta_\diamond\) and
\(\kappa_H(\zeta_\diamond)=\beta_H\),
\(2(\kappa_L-\kappa_H)=\mathfrak C-2a_0\).
For \(r=k\), the shared harmonic determinant calculation and the action proof give
\[
\mathcal R\log\det H^B_{k,N}(\alpha_k^\diamond)
=(\mathfrak C-2a_0)kq+o_{h,A}(kq),
\tag{ACT46}
\]
\[
\mathcal R\log\mathscr J_{k,N}^{(v)}(\alpha_k^\diamond)
=-(\mathfrak C-2a_0)q+o_{h,A}(q),\qquad
\mathcal R\operatorname{Tr}e^{-\tau_k^*(\mathscr A_k^{(v)})^\dagger
\mathscr A_k^{(v)}}\to2.
\tag{ACT47}
\]
Equation (ACT46) uses the shared harmonic determinant conclusion; both conclusions in (ACT47) are derived here from the fixed original arithmetic map.

Finally set \(a_k=1/\tau_k^*\), hence \(b=\beta_*\) in (ACT44).
The low positive parts are \(a_0\) after activation and \(2a_0\) canonically; both high positive parts vanish by (ACT45). Therefore
\[
\boxed{\mathcal R\left[
\log\frac{\mathscr P_N(a_k,\alpha_k^\diamond)}{\mathscr P_N(a_k,0)}
-\Delta_N(\alpha_k^\diamond)\right]
=-2\log(4/\pi)\,q+o_{h,A}(q).}
\tag{ACT48}
\]
This is supplied (48), with the complete original source cost and all inverse singular directions.

## 10. Verification scope

**check_action.py** supplies exact rational fixtures for the polynomial-section inverse, covariance coisometry and moving dual row, conductor phase and actual action columns, observed metrics with nonzero kernel corrections, common-subspace determinant cancellation, shear congruence, and spectral-polynomial edge identity. It also tests the exact two-dimensional amplification example and finite-precision enclosures. Small finite grids are algebraic fixtures, not claims that their asymptotics meet the large-\(k\) guards. The executed receipt is **ACTION_CHECK_RESULTS.json**.
