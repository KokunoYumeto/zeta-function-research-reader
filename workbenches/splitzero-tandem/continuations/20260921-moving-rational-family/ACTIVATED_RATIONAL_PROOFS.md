# Uniform activation, complete rational quotients, and filtered heat

21 September 2026. Independent proof of the new activation, quotient-filter and spectral claims in the received moving-family continuation, sections 1–5 and 7–8. Its original attachment has SHA-256 E9ABFCCC8CC9F7D81A9B77486987FBD7EBD3CADB890EABCFECFB5C6FD8A9B66A. The global polynomial continuation at a vanishing resultant and the source-complex homotopy are treated by the accompanying derivation.

The canonical collision-uniform rational norm was already proved in RF1–67. The inverse-power harmonic comparison and its critical coefficient were already proved in HAR1–49. The new statements here are the harmonic comparison for every retained rational denominator, the uniform activated quotient-filter system with its complete observation feedback, and its complete low-spectrum and heat bounds. Two further consequences are proved: all of the least \(s\) filter singular values have the same harmonic scalar up to \(e^{o(q)}\), uniformly over every physical activation; and the full observed heat operator is approximated in trace norm by its compression to the observed rational sector.

## 1. Exact source, physical coordinates, and finite inputs

Keep the original simple-quartet and period domain:
\[
k\ge9,\quad k\equiv1\pmod4,\quad q=(k+1)^2,\quad
0<\delta<\tfrac12,\quad\gamma>2,\quad S=k/2+iy,
\]
\[
Q_k(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta],
\quad E=\mathbb C[y]/(Q_k),\quad M[f]=[yf].
\tag{MF1}
\]
The convolution source remains \(d\mu_k=w_h^{*k}(y)\,dy\). Its degree-\(N\) Gram is \(H_N\), its remainder map \(J_N\), its attained metric \(G_0=G_N\), and its minimum section \(L_N=H_N^{-1}J_N^*G_N\), for \(q-1\le N\le2q\). The original observation \(\Lambda:E\to B\) is onto, with full kernel \(K\). No conductor kernel replaces \(K\).

Here are the hypotheses behind the added-source bound, retained from [J1–J7 of the complete joint-source proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/f1ad8be11f329a12d562420edfa58fa464948ee2/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/JOINT_MINIMUM_COMPLETE.tex#L607). The fixed one-factor divisor \(h\) retains the complete orders of its selected original zeros. Its divided-jet unit \(U_h=j_h(2\xi/h)\) is invertible, and its physical injection is the complete \(U_h^{\otimes k}\beta\). The original positive source Gram and the whole one-factor relation space give a section \(R_\eta\) with
\(JR_\eta=I\), \(R_\eta^*HR_\eta=\tau_\eta T_\eta\), through degree
\(n_{\rm sec}=2\deg h-1\).
The added source is exactly
\(Y_{k,\eta}=\operatorname{im}(\mathcal A_hR_\eta)^{\otimes k}\beta\);
the same section is fixed at every cutoff. The joint source is the sum \(X_N+Y_{k,\eta}\), with its original cross Gram and the constraint on the complete tensor value. It is not an orthogonal sum of independent source minima.

Use the original simple-quartet choice \(\eta=1\). Put
\(n_*=\max(2q,n_{\rm sec})\),
\[
\mathbf L_k=\Lambda_{h,n_*}^{\,k},\qquad
\mathbf B_k=\tau_1^{\,k},\qquad
T_k=G_{k,1}.
\]
The original one-factor constants satisfy \(\Lambda_{h,n_*}\ge1\), \(\tau_1>1\). Tensoring its positive full-form inequality before minimizing, and using the actual section for the upper side, proves
\[
\mathbf L_k^{-1}T_k\preceq G_1:=G_N^J\preceq\mathbf B_kT_k,\qquad
G_1\preceq G_0,\qquad
\log\mathbf L_k+\log\mathbf B_k=O_h(k\log^2(q+2)).
\tag{MF2}
\]
In particular both individual logarithms have this bound, because both are nonnegative. The separate degree \(n_*\), the fixed divisor and section, and the complete value constraint are part of this assertion. An arbitrary positive added source is not assigned MF2 without these hypotheses.

In the complete root-value coordinates,
\[
T_k=\operatorname{diag}(W_\omega),\quad
W_\omega\ge a_{\min}^k>0,\quad \sum_\omega W_\omega=A_w^k.
\]
These are the original ordered-tuple weights. This value-coordinate expression is transported through the same physical unit as above; it is not a replacement coefficient metric.

Write the exact covariance
\[
C_\alpha=G_\alpha^{-1}=(1-\alpha)G_0^{-1}+\alpha G_1^{-1}
=G_0^{-1}+\alpha\Omega_N,\qquad0\le\alpha\le1,
\]
\[
\Omega_N=F_ZH_Z^+F_Z^*\succeq0,\quad
Q_\alpha=(\Lambda C_\alpha\Lambda^*)^{-1},\quad
\mathcal L_\alpha=C_\alpha\Lambda^*Q_\alpha,\quad
P_{B,\alpha}=\mathcal L_\alpha\Lambda .
\tag{MF3}
\]
Here \(H_Z=\Gamma-C_X^*H_X^{-1}C_X\) and
\(F_Z=I-J_NH_X^{-1}C_X\) are the complete original normal-source matrices. The positive-range inverse retains every null direction. The maps in MF3 are the full attained minima; \(\Lambda=\mathcal L_\alpha^\dagger\) and \(\mathcal L_\alpha\) is an isometry for \(Q_\alpha,G_\alpha\).

Fix \(\mathscr P\Subset\mathbb C\setminus\mathscr L\), where
\(\mathscr L=\{(2a+1)\gamma-i(2b+1)\delta:a,b\in\mathbb Z\}\).
Let \(D\) be monic of degree \(d\), with all roots in \(\mathscr P\), including all repetitions, and put
\(U_Da=[a/D]\), \(\deg a<d\), \(V_D=\operatorname{ran}U_D\).
The canonical result used is [RF16–41 in sealed016](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d44d94aa43d0a1934455ddac008368583f43a2c1/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/RATIONAL_FILTER_PROOFS.md):
\[
a_{d,N}\mathsf S_N I_d
\preceq H^B_{D,N}(0)\preceq H^E_{D,N}(0)
\preceq b_{d,N}\mathsf S_N I_d,
\]
\[
\mathsf S_N=u_kT_N^2,\quad
T_N=\frac1{|Q_k(0)|\sqrt{K_{Q_k,n_0}(0,0)}},\quad
n_0=2\left\lfloor\frac{N+1-q}{2}\right\rfloor,
\]
\[
a_{d,N}=\frac{\ell_{k,N}}{u_k}
\left(\frac{\mathcal L_N^{\rm RF}}
 {2\mathcal F_N^{\rm RF}(\mathcal B_N^{\rm RF})^{Jd}}\right)^2,\qquad
b_{d,N}=(\mathcal U_{d,N}^{\rm RF})^2 .
\tag{MF4}
\]
The superscript identifies exactly RF19, RF32–34 and RF39; it avoids confusing those scalar constants with the observed section \(\mathcal L_\alpha\).
All depend on the fixed compact pole set and degree, not on distances between individual poles.

For clarity, the complete finite domain carried forward is RF37:
\[
q_-=(k-7)^2\ge16,\quad R_k=k\sqrt{\delta^2+\gamma^2}\le2^{-14}q_-,
\quad a_\Gamma^2\le\beta_q/2,\quad\beta_q=2^{-27}q^2,
\]
\[
Jd-v\le q_-,\quad n_-+2\le2q_-,\quad
n_-=N-v+Jd-q_-,\quad
\mathcal L_N^{\rm RF}T_N^{\rm lb}\ge2\mathcal A_d^{\rm RF}.
\tag{MF5}
\]
Here \(a_\Gamma\) is the radius of RF6's fixed punctured contour and
\[
T_N^{\rm lb}=
\frac{\sqrt{c_\sigma q/(1+16q^2)}(q-R_k)^q e^{-\pi q/2}}
 {|Q_k(0)|(n_0+1)10^{n_0}},
\quad c_\sigma=\Gamma(1/4)^2/(2\pi).
\]
RF32 explicitly retains the entire boundary product and every nearby-degree kernel factor in \(\mathcal L_N^{\rm RF}\). The inequality
\(n_--n_0=\Delta+Jd-v+(N-q-n_0)\ge\Delta>0\)
shows that MF5 covers both complex kernel degrees. IVO10 imposes no additional radius restriction on its complex evaluation, whereas the separate reciprocal-\(H\) guard is explicitly present in MF5. These finite guards hold eventually when \(d\log(q+2)=o(q)\), with the original fixed packet, period and nonzero conductor symbol. Uniformity over moving periods is not inferred if the first nonzero moment or source constants lose their stated bounds.

## 2. Uniform harmonic enclosure for the entire rational family

Put \(R_P=\max_{\lambda\in\mathscr P}|\lambda|\),
\(a_*=\operatorname{dist}(\mathscr P,\mathscr L)>0\),
\(A=2\max(1,R_P)\), and
\[
C_{\mathscr P}=\max(2,A/a_*).
\]
For \(|\omega|\le A\),
\(|a(\omega)|\le\sqrt d A^{d-1}\|a\|_2\) and
\(|D(\omega)|\ge a_*^d\).
For \(|\omega|>A\), each denominator factor is at least \(|\omega|/2\), whereas the numerator is at most \(\sqrt d|\omega|^{d-1}\|a\|_2\).
Therefore, with every original root and weight retained,
\[
|a(\omega)/D(\omega)|\le\sqrt d C_{\mathscr P}^{\,d}\|a\|_2,\qquad
U_D^*T_kU_D\preceq d C_{\mathscr P}^{2d}A_w^k I_d.
\tag{MF6}
\]

The full cardinal-lift estimate [HAR13–22](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L134) gives
\[
\operatorname{Tr}(T_k^{-1}G_0)\le\Gamma_N\mathsf S_N,\qquad
\Gamma_N=\max\left(1,\frac{qR_0^2}{\delta^2a_{\min}^k}
e^{8kR_0/\delta+2n_0R_k^2/\beta_q}\right),\quad R_0=\sqrt{\delta^2+\gamma^2}.
\tag{MF7}
\]
Its guards follow from MF5: \(R_k^2\le\beta_q/2\) and \(n_0\le q\le2q-2\).
For completeness its source lift is
\(Q_kH_{Q_k,n_0}/[(y-\omega)Q_k'(\omega)H_{Q_k,n_0}(\omega)]\).
The root product proves
\(|Q_k(0)/Q_k'(\omega)|\le R_0e^{4kR_0/\delta}\);
\(|y-\omega|\ge\delta\) on the real line and the full Gamma comparison give the corresponding diagonal source norm. Summing these norms divided by \(W_\omega\) gives exactly the trace in MF7. The operator inequality
\(T_k^{-1}\preceq\operatorname{Tr}(T_k^{-1}G_0)G_0^{-1}\)
follows by congruence from a positive operator being at most its trace times the identity. It uses the entire covariance.

Invert the lower half of MF2, then apply MF7. Thus
\[
G_1^{-1}\preceq \mathbf L_k\Gamma_N\mathsf S_N G_0^{-1},
\quad
G_\alpha\succeq\frac{G_0}
 {1-\alpha+\alpha\mathbf L_k\Gamma_N\mathsf S_N}.
\tag{MF8}
\]
The same lower inequality holds for \(Q_\alpha\), by applying the fixed \(\Lambda,\Lambda^*\) to the covariance inequality and then inverting, or by taking the same affine minimum on the metric side.

Put
\[
h_N(\alpha)=\frac{\mathsf S_N}{1-\alpha+\alpha\mathsf S_N},\quad
\underline a_{d,N}=\frac{a_{d,N}}{\max(1,\mathbf L_k\Gamma_N)},\quad
\overline b_{d,N}=b_{d,N}+\mathbf B_kdC_{\mathscr P}^{2d}A_w^k.
\]
MF4 and MF8 give the lower bound. For the upper bound use both
\(G_\alpha\preceq G_0/(1-\alpha)\) and \(G_\alpha\preceq G_1/\alpha\),
omitting a bound with zero denominator. The elementary identity
\[
\min\left(\frac{bs}{1-\alpha},\frac t\alpha\right)
\le(b+t)\frac{s}{1-\alpha+\alpha s}
\]
is verified by considering which fraction is smaller; it extends to both endpoints. Consequently
\[
\boxed{
\underline a_{d,N}h_N(\alpha)I_d
\preceq H^B_{D,N}(\alpha)\preceq H^E_{D,N}(\alpha)
\preceq\overline b_{d,N}h_N(\alpha)I_d.}
\tag{MF9}
\]
Take
\[
E_{d,N}=\max(0,-\log\underline a_{d,N},\log\overline b_{d,N}),\quad
E_{k,d}=\max_NE_{d,N}.
\]
MF2, MF4, MF6 and MF7 prove
\[
E_{k,d}=O_{h,A,\mathscr P}
\left(k\log^2(q+2)+(k+Jd)\log(q+Jd+2)\right).
\tag{MF10}
\]
In particular it is \(o(q)\) in the stated degree regime and independent of \(\alpha\). This is the received harmonic theorem, now for the exact joint source specified in MF2–3.

## 3. Critical activation, subquotients, and the complete kernel

The scalar endpoints were already evaluated in [HAR41–49](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L459):
\[
\log\mathsf S_T=2q\ell_k+\beta_Tq+e_{T,k},\quad
\ell_k=\log(q/k),\quad \epsilon_k^{\rm end}=\max_T|e_{T,k}|=o(q),
\]
\[
T=L,H,\quad
\beta_L=2\log(4/\pi)-2-I(\delta,\gamma),\quad
\beta_H=\beta_L-\mathfrak C/2,\quad
1.353893<\mathfrak C<1.354751.
\tag{MF11}
\]
The original high-endpoint profile and zero-law theorem keeps the exact source status stated there. It is not proved again by the present finite matrix bounds.

For \(\alpha_k(\zeta)=e^{-2q\ell_k-\zeta q}\), the exact physical domain is
\(\zeta\ge-2\ell_k\), with \(\alpha=0\) represented by \(\zeta=+\infty\).
For \(s\ge1\),
\[
\max(1,\alpha s)\le1-\alpha+\alpha s\le2\max(1,\alpha s).
\]
Thus, once both scalar endpoints are at least one, every Gram eigenvalue obeys
\[
\left|\log\lambda_j(H^X_{D,N}(\alpha_k(\zeta)))
-2q\ell_k-q\min(\beta_{L/H},\zeta)\right|
\le E_{d,N}+\epsilon_k^{\rm end}+\log2,\quad X=E,B.
\tag{MF12}
\]
This is uniform on the entire moving physical domain, not only on bounded \(\zeta\)-intervals. It yields
\[
\mathcal R\log\det H^X_{D,N}(\alpha_k(\zeta))
=dq C_{\rm inv}(\zeta)+O\!\left(d\sum_NE_{d,N}
 +4d\epsilon_k^{\rm end}+4d\log2\right),
\]
\[
C_{\rm inv}(\zeta)=2[\min(\beta_L,\zeta)-\min(\beta_H,\zeta)].
\tag{MF13}
\]
The finite all-activation version replaces the scalar term by
\(2d\log(h_L(\alpha)/h_H(\alpha))\) and has error \(d\sum_NE_{d,N}\).

For any fixed full-column coefficient map \(W:\mathbb C^r\to\mathbb C^d\) and onto map \(A:\mathbb C^r\to\mathbb C^t\), restrict MF9 and take the full affine minimum. Their exact coefficient metric
\[
Q_{\rm coef}=(A(W^*W)^{-1}A^*)^{-1}
\]
remains in
\[
e^{-E_{d,N}}h_NQ_{\rm coef}\preceq
\left[A(W^*H^X_{D,N}W)^{-1}A^*\right]^{-1}
\preceq e^{E_{d,N}}h_NQ_{\rm coef}.
\tag{MF14}
\]
Each inverse reverses order, proving the claim with the same fibre. Determinants have rank \(t\) in the error. The coefficient determinant cancels at the four cutoffs when the coefficient maps are identical there; it is not discarded if those maps change.

MF9 proves \(K\cap V_D=0\). With any fixed kernel frame \(I_K\), form the full cross Gram
\(C=I_K^*G_\alpha U_D\).
The two Schur complements of the Gram of \([I_K,U_D]\) prove
\[
\delta_{D,N}(\alpha)=
\log\frac{\det H^E_{D,N}(\alpha)}{\det H^B_{D,N}(\alpha)}
=\log\frac{\det(I_K^*G_\alpha I_K)}
{\det[I_K^*G_\alpha I_K-C(H^E_{D,N}(\alpha))^{-1}C^*]}.
\tag{MF15}
\]
After orthonormalizing the two frames, only \(\min(\dim K,d)\) cross singular values are nonzero. The relative eigenvalues in MF9 are at least \(e^{-2E_{d,N}}\). Hence
\[
0\le\delta_{D,N}(\alpha)\le2\min(\dim K,d)E_{d,N}.
\tag{MF16}
\]
For \(\dim K=8k-16\), all four angle losses are \(o(kq)\). At
\(d=\lfloor q/\log^2(q+2)\rfloor\) the displayed bound is
\(O(k^2\log^2q+Jkq/\log q)=o(kq)\), uniformly over all activations and pole multisets. The quotient retains the kernel metric; it does not evaluate its unknown determinant.

## 4. Exact filter quotients and their activated norm

For a monic \(D\) of degree \(d\le q\), define the fixed coefficient quotient
\[
\pi_D[x]=\operatorname{quo}_D\operatorname{rem}_{Q_k}(Dx)
\in\mathcal P_{<q-d}.
\tag{MF17}
\]
On the resolvent domain, its kernel is \(V_D\), and the low-polynomial inclusion is a right inverse: if \(\deg x<q-d\), then \(\deg Dx<q\) and the quotient is exactly \(x\). Its metric is
\[
\overline G_D(\alpha)=(\pi_DC_\alpha\pi_D^*)^{-1}.
\]
The case \(D=1,d=0\) has \(\pi_D=I\) and \(V_D=0\).

Let \(F\) be monic of degree \(s\), all roots in \(\mathscr P\), with \(d+s\le q\). Define
\[
\mathcal I_{D,F}[x]=[F(M)^{-1}x]\in E/V_{DF}.
\]
It is well defined because \(F(M)^{-1}V_D\subset V_{DF}\).
The complete coefficient identity is
\[
\boxed{\pi_{DF}F(M)^{-1}=\operatorname{quo}_F\pi_D.}
\tag{MF18}
\]
Indeed the left side divides \(\operatorname{rem}_{Q_k}(Dx)\) by \(DF\); dividing first by \(D\), then by \(F\), produces the same quotient because the remaining polynomial has degree below \(d+s\). Its kernel in \(\pi_D\)-coordinates is \(\mathcal P_{<s}\), and multiplication by \(F\) is a right inverse. It follows in particular that
\[
\mathcal I_{DF,G}\mathcal I_{D,F}=\mathcal I_{D,FG}
\tag{MF19}
\]
whenever all degrees fit. The polynomial identity
\(\pi_{DF}=\operatorname{quo}_F\pi_DF(M)\) remains valid without inverses; its boundary interpretation is handled by the separate global-frame proof.

For the canonical endpoint, divide the actual minimum representative:
\[
F(M)^{-1}=\mathbf B_0+U_FT_{F,0},\quad
\mathbf B_0=J_N\operatorname{quo}_F L_N,\quad
T_{F,0}=\operatorname{rem}_F L_N,
\]
\[
\|\mathbf B_0\|_{G_0}\le
b_0:=\sqrt{u_k/\ell_{k,N}}\,\mathcal D(N,R_P)^s.
\tag{MF20}
\]
Here \(\mathcal D\) is RF14's complete polynomial divided-difference bound, or the valid larger constant (21) in the received manuscript. Only one full source comparison is used. The remainder lies in \(V_F\subset V_{DF}\), so it is killed by the target quotient. Taking the minimum source lift in \(E/V_D\) proves
\(\|\mathcal I_{D,F}\|_{\alpha=0}\le b_0\).

In the complete value metric \(T_k\), \(F(M)^{-1}\) is diagonal with entries \(F(\omega)^{-1}\), whose modulus is at most \(a_*^{-s}\). MF2 gives
\[
\|F(M)^{-1}\|_{G_1}\le
b_1:=\sqrt{\mathbf L_k\mathbf B_k}\,a_*^{-s}.
\tag{MF21}
\]
Taking the full quotient minima proves the same bound on \(\mathcal I_{D,F}\) at \(\alpha=1\).

If \(A\) denotes its fixed matrix \(\operatorname{quo}_F\), a norm bound between two positive metrics is equivalent to
\[
A\,\overline G_D^{-1}A^*\preceq b^2\overline G_{DF}^{-1}.
\]
This follows by conjugation to Euclidean coordinates and the equality of the operator norms of a matrix and its adjoint. Both quotient covariances are linear images of \(C_\alpha\). Taking the convex combination of the two endpoint inequalities therefore proves
\[
\boxed{\|\mathcal I_{D,F}\|_\alpha\le
B_{s,N}:=\max(b_0,b_1),\qquad0\le\alpha\le1,}
\]
\[
\log^+B_{s,N}
=O_{h,\mathscr P}(k\log^2(q+2)+s\log(q+s+2)).
\tag{MF22}
\]
This proof works even when the numerator metrics are poorly conditioned. If the target has dimension zero, the map and norm are zero; the same bound holds.

Let \(\bar\Lambda_D:E/V_D\to B/\Lambda V_D\) and \(\bar{\mathcal L}_D\) be the actual quotient observation and its minimum section, in the induced metrics. They are respectively a contraction and an isometry. For
\(\mathcal B_{D,F}=\bar\Lambda_{DF}\mathcal I_{D,F}\bar{\mathcal L}_D\),
insert
\(\bar{\mathcal L}_{DF}\bar\Lambda_{DF}=I-P_{\ker\bar\Lambda_{DF}}\)
into MF19. This gives exactly
\[
\mathcal B_{D,FG}-\mathcal B_{DF,G}\mathcal B_{D,F}
=\bar\Lambda_{DFG}\mathcal I_{DF,G}
P_{\ker\bar\Lambda_{DF}}\mathcal I_{D,F}\bar{\mathcal L}_D.
\tag{MF23}
\]
The kernel equals the image of \(K\) in \(E/V_{DF}\), so its dimension is at most \(\dim K\), with equality on the observed rational domain. Thus the feedback rank is at most \(\dim K\), and its norm is at most \(B_{\deg F,N}B_{\deg G,N}\). Its complete projection, all metrics, and all original kernel directions remain.

## 5. A full activated inverse decomposition

The preceding quotient argument has an exact operator realization extending [ACT7–9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/ACTION_PROOFS.md#L112).
Define
\[
\mathcal J_\alpha(x_0,x_1)=\sqrt{1-\alpha}\,x_0+\sqrt\alpha\,x_1:
E_{G_0}\oplus E_{G_1}\to E_{G_\alpha}.
\]
Its actual adjoint is
\[
\mathcal J_\alpha^\dagger x=
(\sqrt{1-\alpha}\,G_0^{-1}G_\alpha x,\,
 \sqrt\alpha\,G_1^{-1}G_\alpha x).
\]
MF3 proves \(\mathcal J_\alpha\mathcal J_\alpha^\dagger=I\).
Consequently every fixed coefficient operator \(A\) satisfies
\[
A=\mathcal J_\alpha\operatorname{diag}(A,A)\mathcal J_\alpha^\dagger,\qquad
\|A\|_{G_\alpha}\le\max(\|A\|_{G_0},\|A\|_{G_1}).
\tag{MF24}
\]
The identity retains the factor order \(AC_\alpha G_\alpha=A\).

Put \(X=F(M)^{-1}\) and use the complete canonical decomposition MF20. Then
\[
\boxed{
X=\mathbf B_\alpha+(1-\alpha)U_FT_{F,0}G_0^{-1}G_\alpha,}
\]
\[
\mathbf B_\alpha=(1-\alpha)\mathbf B_0G_0^{-1}G_\alpha
+\alpha XG_1^{-1}G_\alpha,\qquad
\|\mathbf B_\alpha\|_{G_\alpha}\le B_{s,N}.
\tag{MF25}
\]
The bound follows by inserting \(\operatorname{diag}(\mathbf B_0,X)\) into the same coisometry. The remainder has image in \(V_F\) and rank at most \(s\). It vanishes at \(\alpha=1\). Thus no claim of an activation-uniform separated rank-\(s\) cluster follows merely from its rank.

Applying \(I-P_{V_F,\alpha}\) proves
\[
\|(I-P_{V_F,\alpha})X\|\le B_{s,N},\qquad
\sigma_{s+1}(X)\le B_{s,N}\quad(s<q).
\tag{MF26}
\]
The second statement follows from the singular-value minimum principle on the kernel of the rank-\(s\) remainder. It requires no norm bound for that remainder.

## 6. The entire low spectrum and the full observed heat

Let \(H_F=X^{-\dagger}X^{-1}=F(M)^\dagger F(M)\), and let \(P_{\le\lambda}\) be its full spectral projection. All adjoints and projections in this section use the actual \(G_\alpha\). For \(x\) in that range,
\(\|X^{-1}x\|^2=\langle H_Fx,x\rangle\le\lambda\|x\|^2\).
MF26 therefore proves
\[
\boxed{
\|(I-P_{V_F,\alpha})P_{\le\lambda}\|\le B_{s,N}\sqrt\lambda,\qquad
\operatorname{rank}P_{\le\lambda}\le s
\quad(0<\lambda<B_{s,N}^{-2}).}
\tag{MF27}
\]
The strict spectral threshold is essential for the rank statement with a closed spectral projection.

Write
\[
\ell_{F,N,\alpha}=\lambda_{\min}
[(H^E_{F,N})^{-1/2}H^B_{F,N}(H^E_{F,N})^{-1/2}]
\ge e^{-2E_{k,s}}.
\]
For \(\varepsilon=B_{s,N}\sqrt\lambda<1\), the exact two-subspace estimate gives every unit \(x\in\operatorname{ran}P_{\le\lambda}\)
\[
\|P_{B,\alpha}x\|^2\ge
\left(\sqrt\ell\sqrt{1-\varepsilon^2}
-\sqrt{1-\ell}\varepsilon\right)_+^2 .
\tag{MF28}
\]
To prove it, decompose \(x\) into its \(V_F\) and orthogonal components. For unit \(z\in K\),
\(|\langle z,x\rangle|\le
a\sqrt{1-t^2}+\sqrt{1-a^2}t\),
where \(a=\|P_{V_F}z\|\le\sqrt{1-\ell}\), \(t\le\varepsilon\).
For \(\varepsilon<\sqrt\ell\), the expression increases on both intervals; substituting their endpoints and subtracting its square from one gives MF28. For larger \(\varepsilon\) the positive-part bound is zero.
Thus, at \(\lambda=e^{-cq}\), \(c>0\), the observed fraction is at least
\(\ell(1-o(1))\), uniformly in activation and pole family. The explicit ratio
\(\varepsilon/\sqrt\ell\le B_{s,N}e^{-cq/2+E_{k,s}}\to0\)
proves this uniformity. The low space may be zero.

Let \(P_R\) be any original orthogonal projection annihilating \(V_F\).
For left singular vectors \(a_j\) of \(X\),
\(\|P_Ra_j\|\le\min(1,B_{s,N}/\sigma_j)\).
Since \(a_j\) are precisely the heat eigenvectors,
\[
\operatorname{Tr}(P_Re^{-\tau H_F})
=\sum_j e^{-\tau/\sigma_j^2}\|P_Ra_j\|^2.
\]
For the first \(s\) terms use \(\sup_{x\ge0}xe^{-x}=1/e\).
For the rest use \(\sigma_j\le B_{s,N}\). Therefore
\[
\boxed{
0\le\operatorname{Tr}(P_Re^{-\tau H_F})
\le\varepsilon_{s,N}(\tau):=
s\min(1,B_{s,N}^2/(e\tau))
+(q-s)e^{-\tau/B_{s,N}^2}.}
\tag{MF29}
\]
The last term is absent if \(s=q\); at \(\tau=0\) use the limiting bound \(q\).
For \(\tau=e^{cq}\), this is at most \(e^{-cq+o(q)}\), because
\(\log q=o(q)\) and \(\log^+B_{s,N}=o(q)\).

If \(F\mid D\), then \(V_F\subset V_D\): multiply its numerator by \(D/F\), whose degree is \(d-s\). Set
\(P_R=P_{(K+V_D)^\perp}\).
The actual orthogonal decomposition is
\[
E=K\oplus P_{B,\alpha}V_D\oplus(K+V_D)^\perp.
\]
This follows because \(K+P_{B,\alpha}V_D=K+V_D\), the first two summands are orthogonal, and \(K\cap V_D=0\).
The complete observed heat is
\(\mathcal H_B(\tau)=\Lambda e^{-\tau H_F}\mathcal L_\alpha\).
Let \(\Pi_D\) be the \(Q_\alpha\)-orthogonal projection onto \(\Lambda V_D\).
Isometry of \(\mathcal L_\alpha\) identifies it with \(P_{P_{B,\alpha}V_D}\). Thus
\[
0\le \operatorname{Tr}_B\mathcal H_B
-\operatorname{Tr}_B(\Pi_D\mathcal H_B\Pi_D)
=\operatorname{Tr}_E(P_Re^{-\tau H_F})
\le\varepsilon_{s,N}(\tau).
\tag{MF30}
\]
This proves the received complete trace localization, without replacing the full filtered heat by the heat of a compressed action.

There is also a full operator estimate. Since \(0\preceq\mathcal H_B\preceq I_B\), its blocks under \(\Pi_D\oplus(I-\Pi_D)\) satisfy
\(\operatorname{Tr}D\le\varepsilon_{s,N}\) and
\(\operatorname{Tr}A\le d\).
Factoring the positive operator as a square and applying
\(\|UV^*\|_1\le\|U\|_{\rm HS}\|V\|_{\rm HS}\) gives
\(\|C\|_1\le\sqrt{\operatorname{Tr}A\,\operatorname{Tr}D}\).
Hence
\[
\boxed{
\|\mathcal H_B-\Pi_D\mathcal H_B\Pi_D\|_1
\le\varepsilon_{s,N}(\tau)+2\sqrt{d\,\varepsilon_{s,N}(\tau)}.}
\tag{MF31}
\]
At \(\tau=e^{cq}\), its right side is \(e^{-cq/2+o(q)}\).
This retains the off-diagonal observed coupling, not only the scalar trace.

## 7. Every least filter singular value has the harmonic scale

The preceding results only need a small-rank bounded decomposition. The rational norm additionally determines the complete least-\(s\) scale, uniformly at all activations.

Fix \(F\) of degree \(1\le s\le q\), and retain its canonical coefficient constants from RF8,13,40,44,47:
\[
P_s=\sqrt{M_\sigma}
\left(\sum_{j=0}^{s-1}[2(s+1)]^{2j}\right)^{1/2},\qquad
\rho_{s,N}=\frac{C_sE_\sigma(N,a_\Gamma)}{\sqrt{\ell_{k,N}}},
\]
so that \(\|[a]\|_{G_0}\le\sqrt{u_k}P_s\|a\|_2\) and
\(\|T_{F,0}\|\le\rho_{s,N}\).
Both apply to every original numerator, including repeated poles.
MF4 and MF20 give
\[
\|X\|_{G_0}\le b_0+\sqrt{b_{s,N}\mathsf S_N}\,\rho_{s,N}.
\]
Define the positive finite constants
\[
c_{s,N}=
\max\left[
\left(b_0/\sqrt{\mathsf S_N}+\sqrt{b_{s,N}}\rho_{s,N}\right)^2,
\,b_1^2/\mathsf S_N
\right],\qquad
C_{s,N}^{X}=c_{s,N}+b_1^2.
\tag{MF32}
\]
By MF24, \(\|X\|_{G_\alpha}^2\le c_{s,N}\mathsf S_N\).
For \(\alpha>0\), the separate joint comparison gives
\[
\|Xx\|_{G_\alpha}^2
\le\alpha^{-1}\|Xx\|_{G_1}^2
\le\alpha^{-1}b_1^2\|x\|_{G_1}^2
\le\alpha^{-1}b_1^2\|x\|_{G_\alpha}^2 .
\]
Applying the same scalar harmonic inequality as in MF9 proves
\[
\boxed{\|F(M)^{-1}\|_{G_\alpha}^2
\le C_{s,N}^{X}h_N(\alpha).}
\tag{MF33}
\]

Conversely \(F(M)U_Fa=[a]\) exactly. Since \(G_\alpha\preceq G_0\), the actual restriction to \(V_F\) obeys
\[
\frac{\|F(M)U_Fa\|_{G_\alpha}^2}{\|U_Fa\|_{G_\alpha}^2}
\le\frac{u_kP_s^2e^{E_{s,N}}}{h_N(\alpha)} .
\]
The singular-value minimum principle on this \(s\)-dimensional subspace, together with MF33, proves simultaneously for every \(1\le j\le s\)
\[
\boxed{
\frac1{C_{s,N}^{X}h_N(\alpha)}
\le s_{q-s+j,N}(F(M);G_\alpha)^2
\le\frac{u_kP_s^2e^{E_{s,N}}}{h_N(\alpha)}.}
\tag{MF34}
\]
This finite statement needs MF5 for the rational enclosure but does not require the canonical rank/dominance guards RF49.

Put
\[
J_{s,N}=\max\{0,\log C_{s,N}^{X},\log(u_kP_s^2)+E_{s,N}\}.
\]
The unchanged \(u_k\) has \(|\log u_k|=O_h(k+\log q)\), as proved from the full constant-polynomial source comparison and its ratio in HAR40. Thus \(|\log\ell_{k,N}|=O_h(k+\log q)\) as well. Since \(\mathsf S_N\ge1\) eventually, every displayed factor in MF32 has logarithmic cost
\[
J_{s,N}=O_{h,A,\mathscr P}
\left(k\log^2(q+2)+(k+Js)\log(q+Js+2)\right)=o(q).
\tag{MF35}
\]
The finite formula MF32 is valid before \(\mathsf S_N\ge1\); that eventual fact is used only for its asymptotic logarithmic cost. MF34 now gives the uniform least-singular law
\[
\left|\log s_{q-s+j,N}(F(M);G_\alpha)^2+\log h_N(\alpha)\right|
\le J_{s,N}.
\tag{MF36}
\]
At \(\alpha=1\), \(h_N(1)=1\). These directions then have only \(e^{o(q)}\) variation, and no separated exponentially slow cluster is asserted. Whenever \(\log h_N(\alpha)\ge cq\) for a fixed \(c>0\), MF26 and MF36 prove a separated cluster of exactly \(s\) eigenvalues, because all the others are at least \(B_{s,N}^{-2}=e^{-o(q)}\).

Combining MF12's scalar denominator bound with MF36 yields, uniformly over every physical \(\zeta\),
\[
\left|
\log s_{q-s+j,N}(F(M);G_{\alpha_k(\zeta)})^2
+2q\ell_k+q\min(\beta_{L/H},\zeta)
\right|
\le J_{s,N}+\epsilon_k^{\rm end}+\log2 .
\tag{MF37}
\]
Consequently
\[
\mathcal R\sum_{j=q-s+1}^{q}
\log s_{j,N}(F(M);G_{\alpha_k(\zeta)})^2
=-sq C_{\rm inv}(\zeta)+o(sq)
\tag{MF38}
\]
uniformly on the whole physical activation range. Its explicit error is
\(s\sum_NJ_{s,N}+4s\epsilon_k^{\rm end}+4s\log2\).

For the same filter at all four cutoffs,
\(\det(F(M)^\dagger F(M))=|\det F(M)|^2\) is independent of metric and cutoff. Thus the remaining \(q-s\) squared singular values have the opposite four-cutoff logarithmic return
\(+sq C_{\rm inv}(\zeta)+o(sq)\). This exact compensation uses the original determinant, not separately adjusted errors.

## 8. Critical late heat of the complete polynomial family

Take a common time
\[
\tau_k(b)=\exp(2q\ell_k+bq),
\]
where \(b\) is fixed, or varies in a bounded set with every stated strict gap bounded below.
For fixed physical \(\zeta\), or uniformly over moving \(\zeta\) with those gaps, MF37 gives
\[
\tau_k(b)\,s_{q-s+j,N}(F(M);G_{\alpha_k(\zeta)})^2
=\exp\{q[b-\min(\beta_{L/H},\zeta)]+o(q)\}.
\]
The other \(q-s\) heat terms are bounded by
\((q-s)e^{-\tau_k(b)/B_{s,N}^2}\).
Therefore, away from the exact threshold equalities,
\[
\frac1s\mathcal R\operatorname{Tr}
e^{-\tau_k(b)F(M)^\dagger F(M)}
\longrightarrow
2\left[\mathbf1_{\{b<\min(\beta_L,\zeta)\}}
-\mathbf1_{\{b<\min(\beta_H,\zeta)\}}\right].
\tag{MF39}
\]
This is the full activated heat, not the heat of a compressed observation.

For the retained native time \(\tau_k^*=\tau_k(b_*)\), where
\[
b_*=-2-I(\delta,\gamma),
\]
the exact endpoint relations give
\(\beta_H<b_*<\beta_L\).
Indeed \(\beta_L-b_*=2\psi(0)>0\), and the retained strict bounds
\(\psi(1)<1/8\), \(J(1)<-1.163427\) give
\(b_*-\beta_H=-2[1+\psi(1)+J(1)]>0\).
Thus
\[
\frac1s\mathcal R\operatorname{Tr}
e^{-\tau_k^*F(M)^\dagger F(M)}
\longrightarrow
\begin{cases}
2,&\zeta>b_*,\\
0,&\zeta<b_*.
\end{cases}
\tag{MF40}
\]
The equality \(\zeta=b_*\) is not assigned a value without finer original asymptotics. The convergence is uniform when the indicated threshold gaps are bounded below. It is not asserted uniformly through that threshold.

When \(\zeta>b_*\) with a fixed positive margin, choose an exponentially small spectral threshold that includes every low-cutoff slow eigenvalue. MF27–28 gives each such vector an observed fraction at least \(e^{-o(q)}\). The high-cutoff heat is at most \(q e^{-\exp(cq)}\) for some \(c>0\). Therefore the original measured return is eventually positive, and
\[
\frac1q\log\left[
\frac1s\mathcal R\operatorname{Tr}_B
\bigl(\Lambda e^{-\tau_k^*F(M)^\dagger F(M)}\mathcal L_\alpha\bigr)
\right]\longrightarrow0.
\tag{MF41}
\]
For \(\zeta<b_*\), the absolute measured return tends to zero at the same double-exponential bound furnished by the full heat; no sign is imposed. At every activation, independently of these critical heat limits, MF30–31 retain their uniform finite localization bounds.

## 9. Constants in the received canonical reconstruction

The received sections 2–3 reproduce the canonical result already proved in RF1–41. Their alternative displayed constants are compatible with that result, with the following precise domains.

The contour formula requires the integrand to be holomorphic on a neighbourhood of the closed contour domain, not merely in its interior if boundary values are undefined. The actual \(a/(Q_kH_{Q_k,n_0})\) meets this requirement under MF5. The fixed punctured contour in RF6 is sufficient; a polygonal perturbation smaller than its positive separations also works.

The stated larger Gamma estimate (20) follows from RF13:
\[
M_\sigma K_{\sigma,L}(z,z)
\le e^{2+\pi R/2}(L+1)^2(2L+1)^{R+1/2}
\le e^2 2^{2+2R}e^{\pi R}(L+1)^{3+2R}.
\tag{MF42}
\]
The complete common-denominator remainder bound (35) follows from the coefficient one-norm version of the contour formula, with \(R_C=1+R_B\): its contour length contributes \(R_C\), each divided-polynomial coefficient is bounded using \((1+R_B)^L=R_C^L\), and summing its \(L\) coefficient rows gives \(L R_C^{2L}\). The numerator recovery constant (32) follows by applying Cauchy's estimate to the reversed denominator
\(\prod_{\nu=1}^{L}(1-\xi_\nu z)^{-1}\), not to the unreversed polynomial \(1/\mathcal B_D(z)\). This reversed expression is the precise meaning required by that sentence. On \(|z|=1/[2\max(1,R_B)]\), its modulus is at most \(2^L\). The full factorial Laurent convolution and polynomial-part recovery then give the displayed factor. Its implicit constant depends on \(\mathscr P\) as well as the fixed conductor.

The smaller base \(6^{n_0}\) in received (41) is valid for evaluation at zero. On the interval \([q,2q]\), the orthonormal Legendre basis has values
\(\sqrt{(2j+1)/q}\,P_j(-3)\) at zero.
Rodrigues' finite expansion makes \(P_j(3)>0\); its recurrence gives
\(P_{j+1}(3)\le6P_j(3)\), hence \(|P_j(-3)|\le6^j\).
Thus
\[
|H(0)|^2\le\frac{(n_0+1)^2\,6^{2n_0}}q
\int_q^{2q}|H(y)|^2\,dy.
\]
Together with \(|Q_k|\ge(q/2)^q\) on this interval when \(R_k\le q/2\), the original Gamma lower envelope proves the stated \(\underline T_N\).
This refinement is unnecessary for MF5's already proved \(T_N^{\rm lb}\), but it is not an error.

Finally the received conductor bound \(A_\Sigma e^{Zb_N}\) is valid by the finite translation exponential and the original derivative norm. On \(N\le2q\), its logarithm is \(O_A(\sqrt q\log q)=O_A(k\log q)\), which fits the claimed error. The sharper polynomial-in-\(N\) bound of IVO4/RF39 remains valid as well. None of these constants authorizes a uniform bound as the original nonzero conductor moment approaches zero.

## 10. Exact finite verification and scope

The companion checker uses exact rational matrices for a complete polynomial source, an actual added section with its cross Gram, harmonic covariance interpolation, polynomial quotients, and complex observations. It also checks the full heat localization, harmonic least-singular bounds and trace-norm strengthening on finite numerical fixtures with their original metrics. Its executed receipt ACTIVATED_RATIONAL_CHECKS.json records 159 exact checks and 338 floating-point spectral tests. Neither type is a native xi-moment computation or a new asymptotic certificate. ACTIVATED_RATIONAL_SOURCE_USE_LEDGER.md records the exact source versions, actual reading, human citations and inherited profile-theorem status.

The new proof preserves the original added-source construction and its fixed-packet hypotheses. It establishes all-activation norm and localization bounds without assuming that the critical slow cluster survives at full activation. The strengthened harmonic singular law describes that change explicitly. The global frame at the resultant and the corrected source-complex homotopy remain with the accompanying independent derivation.
