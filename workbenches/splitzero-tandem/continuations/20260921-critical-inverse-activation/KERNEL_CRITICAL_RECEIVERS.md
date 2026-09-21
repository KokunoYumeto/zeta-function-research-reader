# Critical activation carried into the original kernel and complementary quotient

These calculations use the full original source covariance, the unchanged observation and its complete kernel. They strengthen IQR1–6 and the covariance receiving equations without replacing the kernel by the inverse-power space. The all-activation comparison used below is proved in the accompanying harmonic derivation from the original finite IVO estimates; its analytic endpoint coefficient retains the exact earlier monic-profile and zero-law proof status.

## 1. Original objects and proved input

Keep
\[
q=(k+1)^2,\quad k\equiv1\pmod4,\quad 0<\delta<\tfrac12,\quad\gamma>2,
\quad Q(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta].
\]
Let \(E=\mathbb C[y]/(Q)\), \(M[p]=[yp]\), and retain \(S=k/2+iy\) and the original physical source \(w_h^{*k}(y)\,dy\). Let \(\Lambda:E\to B\) be the original onto observation. Its kernel \(K\), frame \(I_K\), every period constraint and the complete invariant-image columns remain fixed. On the previously proved period domain, \(m=\dim K=8k-16\).

The original scalar and complete joint source minima are \(G_N,G_N^J\). Their exact activation is
\[
G_N(\alpha)^{-1}=(1-\alpha)G_N^{-1}+\alpha(G_N^J)^{-1},
\qquad 0\le\alpha\le1. \tag{AK1}
\]
The joint source contains the scalar source isometrically with the same value map. Taking the infimum over that larger set proves \(G_N^J\preceq G_N\). Hence \(G_N^J\preceq G_N(\alpha)\preceq G_N\).

Set \(U_rd=\sum_{j=1}^rd_j[y^{-j}]\), \(V_r=\operatorname{im}U_r\). All finite rational detection guards are retained, and \(r\log(q+2)=o(q)\). The proved harmonic comparison is
\[
e^{-E_{r,N}}h_N(\alpha)I
 \preceq H^B_{r,N}(\alpha)\preceq H^E_{r,N}(\alpha)
 \preceq e^{E_{r,N}}h_N(\alpha)I,\qquad
h_N(\alpha)=\frac{\mathsf S_N}{1-\alpha+\alpha\mathsf S_N},
\tag{AK2}
\]
where \(H^E=U_r^*G_N(\alpha)U_r\),
\(H^B=U_r^*\Lambda^*Q_{B,N}(\alpha)\Lambda U_r\),
\(Q_{B,N}(\alpha)=(\Lambda G_N(\alpha)^{-1}\Lambda^*)^{-1}\),
\(\mathsf S_N=u_k/(|Q(0)|^2\mathsf K_{Q,n_0}(0,0))\), and
\[
E_{r,N}=O_{h,A}\bigl(k\log^2(q+2)+(k+Jr)\log(q+Jr+2)\bigr)=o(q).
\]
The constants in AK2 are independent of activation. In particular,
\(H^B\succeq e^{-2E_{r,N}}H^E\). No division of the original arithmetic metric has been made.

Write \(\mathcal R f_N=f_{q-1}+f_q-f_{2q-1}-f_{2q}\). With
\[
\alpha_k(\zeta)=e^{-2q\log(q/k)-\zeta q},\quad
\beta_{\rm H}=\beta_{\rm L}-C_\partial/2,
\quad
C_{\rm inv}(\zeta)=2[\min(\beta_{\rm L},\zeta)-\min(\beta_{\rm H},\zeta)],
\]
the harmonic calculation gives
\[
\mathcal R\log\det H^B_{r,N}(\alpha_k(\zeta))
 =rq\,C_{\rm inv}(\zeta)+o_{h,A}(rq). \tag{AK3}
\]
IQR2 identifies the exact coefficient in this formula with the earlier \(C_\partial\); this is an algebraic identity of the retained elliptic formulas, not a numerical identification.

## 2. The original kernel survives the inverse-sector quotient at every activation

Since AK2 makes \(\Lambda U_r\) injective, \(K\cap V_r=0\). The algebraic quotient
\(\pi_r:E\to E/V_r\) is fixed. Give it the metric
\(\overline G_{r,N}(\alpha)=(\pi_rG_N(\alpha)^{-1}\pi_r^*)^{-1}\) in any fixed quotient coordinates. Define
\[
H_{K,N}(\alpha)=I_K^*G_N(\alpha)I_K,\qquad
\widehat H_{K,r,N}(\alpha)
 =(\pi_r I_K)^*\overline G_{r,N}(\alpha)(\pi_r I_K).
\tag{AK4}
\]
The image frame has exactly \(m\) independent columns because of the intersection statement.

For the following finite calculation fix \(N,\alpha\), and write
\[
A=I_K^*GI_K,\quad D=U_r^*GU_r,\quad C=I_K^*GU_r.
\]
Minimizing over the full kernel gives
\(H^B=D-C^*A^{-1}C\). Minimizing over the full inverse sector gives
\(\widehat H_K=A-CD^{-1}C^*\). These formulas follow by expanding
\(\|I_Kx+U_ry\|_G^2\) and completing its quadratic square, so both original minima, rather than a chosen section, are retained.

Put \(X=A^{-1/2}CD^{-1/2}\). AK2 implies
\(I-X^*X\succeq e^{-2E_{r,N}}I\). The nonzero eigenvalues of
\(X^*X\) and \(XX^*\) coincide: if \(X^*Xv=\lambda v\) with \(\lambda>0\), then \(Xv\ne0\) and \(XX^*(Xv)=\lambda Xv\), and the inverse correspondence is \(X^*/\lambda\). Therefore
\[
\begin{split}
\delta_{r,N}(\alpha)
&:=\log\det H_{K,N}(\alpha)-\log\det\widehat H_{K,r,N}(\alpha)\\
&=\log\det H^E_{r,N}(\alpha)-\log\det H^B_{r,N}(\alpha)\\
&=-\log\det(I-XX^*)\\
&\in[0,\,2\rho_{r,N}(\alpha)E_{r,N}],
\qquad \rho_{r,N}(\alpha)=\operatorname{rank}C\le\min(m,r).
\end{split}\tag{AK5}
\]
This also proves the exact relation between the kernel quotient and observed inverse-power metric.

Let \(d_N=2\rho_{r,N}E_{r,N}\). Retaining all four signs yields
\[
\begin{split}
\left|\mathcal R\log\det H_{K,N}(\alpha)
-\mathcal R\log\det\widehat H_{K,r,N}(\alpha)\right|
&\le \max(d_{q-1}+d_q,d_{2q-1}+d_{2q})\\
&\le4\min(m,r)\max_N E_{r,N}.
\end{split}
\tag{AK6}
\]
For \(r=k\), the right side is \(O_{h,A}(k^2\log^2(q+2))=o(kq)\), uniformly for every activation, including both endpoints and the critical exponential window. The first inequality uses nonnegativity in AK5; it does not sum absolute errors with an unnecessary factor two. This extends the earlier canonical-source kernel quotient to the complete activated metric.

## 3. Exact source map after shifting the inverse sector

The quotient used in AK4 has a concrete original source presentation. Let
\(J_N^{\rm sc}:\mathcal X_N\to E\) and \(J_N^{\rm jt}:\mathcal J_N\to E\)
be the original scalar and joint value maps from their full physical source Hilbert spaces. Define
\[
T_{N,\alpha}(p,z)
 =\sqrt{1-\alpha}\,J_N^{\rm sc}p+
   \sqrt{\alpha}\,J_N^{\rm jt}z .
\tag{AK7}
\]
The direct sum uses the unchanged two physical source norms. Its covariance is exactly AK1, since multiplication by the two real square roots squares their coefficients in \(T_{N,\alpha}T_{N,\alpha}^*\). Its entire relation space is \(\ker T_{N,\alpha}\). Cross terms arise in the attained minimum and are not removed.

Multiplication by \(M^r\) induces the exact isomorphism
\[
\varphi_r:E/V_r\longrightarrow E/\mathcal P_{<r},
\qquad [x]_{V_r}\longmapsto[M^rx]_{\mathcal P_{<r}}. \tag{AK8}
\]
Indeed \(M\) is invertible because none of the original roots is zero, and \(M^rV_r=\mathcal P_{<r}\); its inverse is multiplication by \(M^{-r}\) modulo \(V_r\).

Give the target in AK8 the metric attained from the **same source** by
\(p_rM^rT_{N,\alpha}\), where \(p_r:E\to E/\mathcal P_{<r}\).
For any target \(z\),
\[
\begin{split}
\|z\|_{\rm target}^2
&=\inf_{p_rM^rT_{N,\alpha}s=z}\|s\|^2\\
&=\inf_{\varphi_r\pi_rT_{N,\alpha}s=z}\|s\|^2
=\|\varphi_r^{-1}z\|_{\overline G_{r,N}(\alpha)}^2 .
\end{split}\tag{AK9}
\]
Thus AK8 is an isometry for these explicitly specified attained metrics, and the target Gram of \(p_rM^rI_K\) is exactly \(\widehat H_{K,r,N}(\alpha)\). The cutoff remains \(N\). The map does not substitute the unrestricted scalar source at degree \(N+r\), whose metric requires the separate IQR5 comparison.

## 4. The known inverse-sector contribution passes through the determinant lines

Choose a fixed matrix \(W\) completing \([I_K,U_r]\) to a basis
\(\mathcal T=[I_K,U_r,W]\) of \(E\). It may depend on \(k\) and the original period but is independent of \(N,\alpha\). Write
\[
B_r=\operatorname{im}(\Lambda U_r),\qquad
B_{\rm rem}=B/B_r,
\]
and let \(H_{{\rm rem},r,N}(\alpha)\) be the metric on \(B_{\rm rem}\) attained from the original \(Q_{B,N}(\alpha)\), in the basis supplied by \(\Lambda W\) modulo \(B_r\).

Two complete Schur eliminations, first \(K\) and then \(B_r\), give
\[
\det(\mathcal T^*G_N(\alpha)\mathcal T)
=\det H_{K,N}(\alpha)\,
 \det H^B_{r,N}(\alpha)\,
 \det H_{{\rm rem},r,N}(\alpha).
\tag{AK10}
\]
Every factor uses its declared original restriction or attained quotient. In particular the final factor contains all corrections along both \(K\) and \(V_r\).

The frame factor \(|\det\mathcal T|^2\) cancels under \(\mathcal R\), whose four signs sum to zero. Inserting AK3 proves
\[
\begin{split}
\mathcal R\log\det G_N(\alpha_k(\zeta))
={}&\mathcal R\log\det H_{K,N}(\alpha_k(\zeta))\\
 &+\mathcal R\log\det H_{{\rm rem},r,N}(\alpha_k(\zeta))
 +rq\,C_{\rm inv}(\zeta)+o(rq).
\end{split}\tag{AK11}
\]
At \(r=k\) this subtracts an evaluated \(kq\) contribution from the original complementary return.

For any one of the three metric factors, write
\(\Delta_X(\alpha)=\log\det H_X(0)-\log\det H_X(\alpha)\).
For \(E\), this is the full source cost
\[
\Delta_E(\alpha)=\log\det(I+\alpha\mathsf K_N),\quad
\mathsf K_N=G_N^{1/2}[(G_N^J)^{-1}-G_N^{-1}]G_N^{1/2}\succeq0.
\]
Taking the ratio of AK10 at \(0\) and \(\alpha\) proves the exact identity
\(\Delta_E=\Delta_K+\Delta_{V_r}^B+\Delta_{\rm rem}\).
Consequently
\[
\mathcal R(\Delta_K+\Delta_{\rm rem})(\alpha_k(\zeta))
=\mathcal R\Delta_E(\alpha_k(\zeta))
-rq[C_\partial-C_{\rm inv}(\zeta)]+o(rq).
\tag{AK12}
\]
This is the backward receiver for the earlier full source-metric cost. It does not allocate the unevaluated sum between its two remaining factors.

## 5. Weak critical activation preserves every original subquotient

The lattice cardinal estimate proves, in the actual original root-value coordinates,
\[
\operatorname{Tr}(T_k^{-1}G_N)\le\Gamma_N\mathsf S_N,\qquad
(G_N^J)^{-1}\preceq\mathbf L_kT_k^{-1}.
\]
For any positive matrix \(G\), set \(A=G^{1/2}T_k^{-1}G^{1/2}\succeq0\). Every eigenvalue of \(A\) is at most \(\operatorname{Tr}A\), so conjugating this inequality gives
\(T_k^{-1}\preceq\operatorname{Tr}(T_k^{-1}G)G^{-1}\).
Define \(c_N=\max(1,\mathbf L_k\Gamma_N\mathsf S_N)\). Thus
\[
G_N^{-1}\preceq G_N(\alpha)^{-1}
 \preceq(1-\alpha+\alpha c_N)G_N^{-1},
\quad
\frac{G_N}{1-\alpha+\alpha c_N}
 \preceq G_N(\alpha)\preceq G_N.
\tag{AK13}
\]
This is a full-space inequality before any projection.

Both restriction and attained quotient preserve a two-sided metric comparison with the same constants: restriction follows by inserting the same vector, while the quotient follows by taking the infimum over exactly the same fibre. Iterating proves the assertion for every fixed original subquotient. For a resulting rank-\(t\) metric \(H_X\),
\[
0\le\log\frac{\det H_{X,N}(0)}{\det H_{X,N}(\alpha)}
\le t\log(1-\alpha+\alpha c_N).
\tag{AK14}
\]
The rank multiplier is retained.

Now
\(\log c_N=2q\log(q/k)+\beta_{\rm L/H}q+o(q)\);
the equality follows from the proved endpoint expansions and
\(\log(\mathbf L_k\Gamma_N)=o(q)\), with the lower endpoint eventually positive. For \(\alpha=\alpha_k(\zeta)\),
\[
0\le\Delta_{X,N}(\alpha_k(\zeta))
\le tq[\beta_{\rm L/H}-\zeta]_++t\,o(q).
\tag{AK15}
\]
The finite controlling quantity is always AK14. For any fixed \(\varepsilon>0\), if \(\zeta\ge\beta_{\rm L}+\varepsilon\), then for all sufficiently large \(k\)
\[
0\le\Delta_{X,N}(\alpha_k(\zeta))\le t e^{-\varepsilon q/2}
\quad\hbox{at each of the four cutoffs},\qquad
|\mathcal R\Delta_{X,N}|\le2t e^{-\varepsilon q/2}.
\tag{AK16}
\]
Indeed \(\alpha c_N\le e^{-\varepsilon q/2}\),
\(\log(1-\alpha+\alpha c_N)\le\alpha c_N\), and there are two positive and two negative losses, each nonnegative.

In particular this applies to the full original kernel, with \(t=m\), and every complementary attained quotient. Since
\(\beta_{\rm L}<2\log(4/(\pi\gamma))<0\), the original boundary activation
\(\alpha=e^{-2q\log(q/k)}\) has \(\zeta=0\) and satisfies AK16 with
\(\varepsilon=-\beta_{\rm L}\). Therefore the canonical kernel determinant at this activation agrees with its unactivated value up to an exponentially small finite metric error. This conclusion uses the full-space cardinal comparison; it does not insert a moving parameter into the earlier fixed-activation asymptotic.

Within \(\beta_{\rm H}<\zeta<\beta_{\rm L}\), AK14–15 instead give the actual kernel-loss enclosure
\[
-2mq(\beta_{\rm L}-\zeta)-o(mq)
\le
\mathcal R\log\det H_{K,N}(\alpha_k(\zeta))
-\mathcal R\log\det H_{K,N}(0)
\le o(mq).
\tag{AK17}
\]
The two high-cutoff losses are \(o(mq)\), the two low-cutoff losses are nonnegative and at most \(mq(\beta_{\rm L}-\zeta)+o(mq)\) each. This explains both signs in AK17. The exact initial canonical determinant and its individual complex-current coefficients remain separate calculations; AK5–17 give the proved maps and bounds connecting this critical-layer result to them.

## 6. An exact certificate for the concrete activation coefficient

For the received choice \(\zeta_\diamond=\beta_{\rm L}-a_0\), where \(a_0=\log(4/\pi)\), the coefficient is \(C_\partial-2a_0\). The exact rational calculation accompanying this proof certifies
\[
0.870764<C_\partial-2\log(4/\pi)<0.871623,
\qquad C_\partial>4\log(4/\pi)>0.
\tag{AK18}
\]
Here is its full elementary method. Let \(a=\arctan(1/5)\), \(b=\arctan(1/239)\). The double-angle formula gives \(\tan(2a)=5/12\), \(\tan(4a)=120/119\) and \(\tan(4a-b)=1\). Both \(4a-b\) and \(\pi/4\) lie in \((0,\pi/2)\), so \(\pi=16a-4b\). Integrating the finite geometric series for \(1/(1+x^2)\) bounds each arctangent between its alternating truncation and that truncation plus the next term. The certificate takes 14 terms at \(1/5\) and four at \(1/239\), giving exact rational endpoints \(p_-<\pi<p_+\).

Set \(t_-=(4-p_+)/(4+p_+)\) and \(t_+=(4-p_-)/(4+p_-)\). Integrating \(2/(1-t^2)\) gives \(\log((1+t)/(1-t))=2\sum_{j\ge0}t^{2j+1}/(2j+1)\). Its first 16 terms at \(t_-\) are a lower bound for \(a_0\). The first 16 terms at \(t_+\), plus \(2t_+^{33}/[33(1-t_+^2)]\), are an upper bound. All quantities in this finite calculation are rational. Combining them with the retained strict interval \(1.353893<C_\partial<1.354751\) proves AK18 by integer cross multiplication. The included script records the exact fractions. This numerical certificate does not strengthen the inherited analytic status of that \(C_\partial\) interval.

At the same concrete activation and with the original \(r=k\) frame, AK11--12 therefore give the two evaluated complementary receivers
\[
\begin{aligned}
\mathcal R(\log\det H_K+\log\det H_{{\rm rem},k})
 &=\mathcal R\log\det G-[C_\partial-2\log(4/\pi)]kq+o(kq),\\
\mathcal R(\Delta_K+\Delta_{{\rm rem},k})
 &=\mathcal R\Delta_E-2\log(4/\pi)kq+o(kq).
\end{aligned}\tag{AK19}
\]
All activated terms in AK19 are evaluated at \(\alpha_k(\zeta_\diamond)\), and every \(\Delta\) is relative to its own original unactivated metric. These formulas follow by substituting \(C_{\rm inv}(\zeta_\diamond)=C_\partial-2\log(4/\pi)\) into the exact determinant factors. No extra term is adjoined to the arithmetic action.

## 7. A larger controlled quotient for the original kernel calculation

The estimate AK6 has \(\min(m,r)\), not a mandatory factor \(r\). Thus every admitted \(r\log(q+2)=o(q)\) preserves the original kernel determinant through \(o(kq)\), because \(m=8k-16\) and \(E_{r,N}=o(q)\). A specific growing choice supplied by this bound is
\[
r_k=\left\lfloor\frac{q}{\log^2(q+2)}\right\rfloor,
\]
\[
\begin{gathered}
\sup_{0\le\alpha\le1}
\left|\mathcal R\log\det H_{K,N}(\alpha)
-\mathcal R\log\det\widehat H_{K,r_k,N}(\alpha)\right|\\
=O_{h,A}\!\left(k^2\log^2(q+2)+\frac{Jkq}{\log(q+2)}\right)=o(kq).
\end{gathered}
\tag{AK20}
\]
Indeed \(r_k\log(q+2)\le q/\log(q+2)=o(q)\), so the original finite guards eventually hold, and substitution into the proved \(E_{r,N}\) bound gives the displayed error. The exact shifted source in AK7--9 realizes this quotient for every activation. Its retained kernel dimension is still \(m\); all \(r_k\) inverse-power classes are removed by the actual quotient map. The four original cutoffs and source spaces are unchanged. The determinant of this remaining kernel is still the next value to evaluate; no numerical allocation follows merely from its unchanged dimension.

## Proof sources and human sources

- [IQR1–6 and IQR2's exact coefficient identification](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ab120cf974feb26a31d77b07458b6da52f912ea4/workbenches/splitzero-tandem/continuations/20260921-inverse-quotient/INVERSE_QUOTIENT_RECEIVERS.tex).
- [IFH1–10: original observation, its finite inverse-power metric and exact determinant receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INVERSE_FLAG_AND_RELATIVE_HEAT.tex).
- [J3 and the complete joint-source minimum](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/f1ad8be11f329a12d562420edfa58fa464948ee2/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/JOINT_MINIMUM_COMPLETE.tex#L634).
- [TC1–29: the actual adjacent two-column source and complete normal-source covariance](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/f1ad8be11f329a12d562420edfa58fa464948ee2/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/TWO_COLUMN_ACTUAL_UPDATE.md).
- Human analytic inputs carried by these original-source proofs: R. A. Askey and R. Roy, DLMF Chapter5, especially [5.8.E3](https://dlmf.nist.gov/5.8.E3); T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw, DLMF Chapter18, especially [18.22.E8](https://dlmf.nist.gov/18.22.E8) and [18.23.E7](https://dlmf.nist.gov/18.23.E7). Their original equation TeX is retained. The finite matrix identities AK4–17 are proved here; the human sources are credited for the Gamma and polynomial inputs rather than for these new receiving identities.
