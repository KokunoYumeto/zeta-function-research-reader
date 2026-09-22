# Positive arithmetic probes and the increasing original determinant

Result SZ-20260922-022, probe derivation. The incoming arithmetic-probe manuscript supplies the finite polarization construction. This proof establishes its maps completely, strengthens its finite-error constant, evaluates the optimal positive regularizer for the resulting error bound, and derives a positive, telescoping determinant at every original observation depth. No native period-dependent value is assigned by a dimension count.

The exact predecessor is [BD1–31, original arithmetic observation and whole-source estimate](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/BOUNDED_DEGREE_PROOFS.md), [MR1–29, original matrix recovery](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/MATRIX_RECOVERY_PROOFS.md), and [SD1–54, scalar recovery](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/SCALAR_RECOVERY_PROOFS.md). The public files are pinned to the verified 021 proof commit.

## AP1. Original spaces and source

Retain the actual admitted period and hypothetical simple quartet of the preceding programme proofs. Thus \(q=(k+1)^2\), \(k\equiv1\pmod4\), \(k\ge17\), \(0<\delta<1/2\), and the actual quartet satisfies the finite-height guard in BD1. In the original physical coordinate,
\[
 Q_k(y)=\prod_{a,b=0}^k\bigl(y-(2b-k)\gamma+i(2a-k)\delta\bigr),
 \quad E=\mathbb C[y]/(Q_k),\quad M[p]=[yp].
\]
The physical arithmetic operator is \(kI/2+iM\). The original onto observation is \(\Lambda:E\to B\), its kernel is \(K\), and its fixed frame is \(I_K:\mathbb C^m\to K\), where \(m=8k-16\), \(n=q-m\). For each of the four cutoffs \(N=q-1,q,2q-1,2q\), use the attained source metric \(G_N>0\), including the complete original source measure and its mass. Put
\[
 Q_N=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
 L_N=G_N^{-1}\Lambda^*Q_N,\quad H_{K,N}=I_K^*G_NI_K.
 \tag{AP1}
\]
All stars refer to conjugate transpose in the indicated coefficient frames. Write
\[
 \mathcal R f=f_{q-1}+f_q-f_{2q-1}-f_{2q},\qquad
 \mathcal K_k=\mathcal R\log\det H_{K,N}.
\]
The complete source inequality needed below is the explicitly proved BD21:
\[
 e^{-E_k}G_{q-1}\preceq G_N\preceq G_{q-1},
 \quad E_k=2\log C_{\rm rem}+\log(u_k/\ell_k)=O_h(q).
 \tag{AP2}
\]
Here \(r=k\sqrt{\delta^2+\gamma^2}/q\), \(t=\max(1,r)\),
\[
 C_{\rm rem}=(2\pi)^{1/4}2^q
 \left(1+(q+1)[4t(1+r)]^q\right)
 \frac{(2q+1)11^{2q}e^{\pi q}}{\sqrt{C_Lq}},
 \qquad C_L=\frac{\pi}{\Gamma(3/4)^2}.
\]
The bounds \(\ell_k,u_k\) apply to every polynomial through degree \(2q\) in the original measure. The proof of AP2, including the Gamma mass and every root, is retained in full in the predecessor BD11. We use that independently derived constant instead of assuming the different unevaluated remainder constant in the new incoming text. Source nesting gives \(G_{N'}\preceq G_N\) whenever \(N'\ge N\).

BD1–3 prove, with the actual corner and period guards,
\[
 K_s=\bigcap_{j=0}^s\ker(\Lambda M^j),\quad
 t_s=\dim K_s,\quad t_0=m,\quad t_8\le128,\quad K_d=0,\ d\le80.
 \tag{AP3}
\]
No conductor kernel is substituted for the kernel of the complete observation.

## AP2. Every specified positive probe is an original operator

For a polynomial \(P\), define
\[
 V_N[P]=\Lambda P(M)G_N^{-1}P(M)^*\Lambda^*.
 \tag{AP4}
\]
All roots of \(Q_k\) have modulus at least \(\sqrt{\delta^2+\gamma^2}>2\), since \(k\) is odd. For \(0\le i<j\le s\), the polynomials
\[
 y^i,\qquad y^i+y^j,\qquad y^i+iy^j
 \tag{AP5}
\]
are nonzero at every original root. Indeed their possible additional zeros satisfy \(|y|=1\). Bezout division therefore gives a unique residue polynomial for \(P^{-1}\) modulo the full \(Q_k\). It defines \(T_P=P(M)^{-1}\) on the same \(E\), with no change of source degree, and
\[
 V_N[P]=\Lambda(T_P^*G_NT_P)^{-1}\Lambda^*.
 \tag{AP6}
\]
This follows by multiplying the proposed inverse \(P(M)G_N^{-1}P(M)^*\) on both sides by \(T_P^*G_NT_P\).

There is also an exact energy map. Suppressing \(N\), let \(P^\dagger=G^{-1}P(M)^*G\). Since \(GL=\Lambda^*Q\),
\[
 L^*G(P^\dagger)^\dagger P^\dagger L
 =L^*GP(M)G^{-1}P(M)^*GL
 =QV[P]Q. \tag{AP7}
\]
Both quotient factors remain. This proves the relation between the reciprocal-word inverse energy and the full adjoint-word energy before any compression.

## AP3. Exact polarization and selected source minimum

Set \(S_{ij}=\Lambda M^iG^{-1}(M^*)^j\Lambda^*\), and let \(D_i=V[y^i]\). Expansion of the two mixed probes gives
\[
 A_{ij}=V[y^i+y^j]-D_i-D_j=S_{ij}+S_{ji},
\]
\[
 B_{ij}=V[y^i+iy^j]-D_i-D_j=-iS_{ij}+iS_{ji}.
\]
Consequently
\[
 S_{ii}=D_i,\quad S_{ij}=\tfrac12(A_{ij}+iB_{ij}),\quad S_{ji}=S_{ij}^*.
 \tag{AP8}
\]
There are \((s+1)^2\) positive probes. This is the classical complex polarization identity applied to these exact arithmetic words; the identity itself is not claimed as new.

The whole matrix equals
\[
 \mathcal S_{s,N}=\mathcal O_sG_N^{-1}\mathcal O_s^*,
 \qquad\mathcal O_s=\operatorname{col}_{j=0}^s(\Lambda M^j). \tag{AP9}
\]
Start with every row of \(\Lambda\). At each successive depth, append independent scalar rows from \(\Lambda M^s\), preserving all earlier selected rows. Let \(r_s=m-t_s\). The selected map has full row rank \(n+r_s\). Its Gram is positive definite. The complete Schur complement of its initial \(Q_N^{-1}\) block is
\[
 C_{s,N}=J_s H_{K,N}^{-1}J_s^*, \tag{AP10}
\]
where \(J_s\) consists of the selected rows of \(\Lambda M^jI_K\), \(j\ge1\).

For a direct proof of the source identity used here, the square matrix \(U=[L,I_K]\) is invertible: applying \(\Lambda\) shows that its two summands intersect trivially and span \(E\). Its Gram is \(\operatorname{diag}(Q,H_K)\), because \(\Lambda L=I\), \(L^*GL=Q\), and \(L^*GI_K=0\). Inverting the Gram and transporting it back gives
\[
 G^{-1}=LQ^{-1}L^*+I_KH_K^{-1}I_K^*.
\]
Its first term is \(G^{-1}\Lambda^*Q\Lambda G^{-1}\). Applying the selected rows on both sides proves AP10, including every cross block.

Choose fixed \(P_1,P_0\) with \(J_sP_1=I\) and \(I_KP_0\) a basis of \(K_s\). In the basis \([P_1,P_0]\), AP10 is the upper principal block of the inverse of \(H_K\). Inversion by completing the square gives
\[
 \det H_K
 =\frac{\det(P_0^*H_KP_0)}{|\det[P_1,P_0]|^2\det C_s}.
\]
The fixed coefficient determinant cancels under the four original signs. Thus
\[
 X_s:=-\mathcal R\log\det C_{s,N},\quad
 Z_s:=\mathcal R\log\det(P_0^*H_{K,N}P_0),\quad
 \mathcal K_k=X_s+Z_s. \tag{AP11}
\]
For \(s=0\), the determinant of the empty \(C_0\) is one and \(X_0=0\). At \(s=d\), \(Z_d=0\) and \(J_d\) is square:
\[
 H_{K,N}^{-1}=J_d^{-1}C_{d,N}J_d^{-*}. \tag{AP12}
\]
If \(\mathcal B_d\mathcal O_d=I\), AP9 also gives \(G_N^{-1}=\mathcal B_d\mathcal S_{d,N}\mathcal B_d^*\).

Restricting AP2 and using source nesting at the paired cutoffs proves
\[
 0\le Z_s\le2t_sE_k.
 \tag{AP13}
\]
Each low-to-high determinant ratio lies between one and \(e^{t_sE_k}\). At depth eight there are 81 positive probes and \(0\le\mathcal K_k-X_8\le256E_k=O_h(q)\). At depth at most80, 6561 probes suffice for exact full recovery. The arithmetic values of these matrices are still required.

## AP4. New positive increments at every depth

Let \(b_s=t_{s-1}-t_s=r_s-r_{s-1}\). If \(b_s=0\), put \(D_{s,N}\) equal to the empty matrix. Otherwise take the complete Schur complement of \(C_{s-1,N}\) in the successively selected \(C_{s,N}\):
\[
 D_{s,N}=C_{s,N}^{\rm new,new}
 -C_{s,N}^{\rm new,old}C_{s-1,N}^{-1}C_{s,N}^{\rm old,new}.
 \tag{AP14}
\]
Every \(D_{s,N}\) is positive definite. Completing the square proves \(\det C_s=\det C_{s-1}\det D_s\). Therefore
\[
 X_s-X_{s-1}=-\mathcal R\log\det D_{s,N}. \tag{AP15}
\]
These are the actual original observation innovations; no chain block is declared invariant under \(M\).

Here is their source metric meaning. After all prior observation rows are fixed, their common nullspace is \(K_{s-1}\). Apply the same identity used in AP10 to that complete prior observation map. It shows that \(D_s\) is the covariance of the new rows restricted to \(K_{s-1}\), in the inverse of its original restricted metric. These new rows have nullspace \(K_s\). Consequently \(D_s^{-1}\) is exactly the attained quotient metric on \(K_{s-1}/K_s\), in the fixed new-row coordinate frame.

For explicit connecting maps, let \(I_{s-1}\) be a fixed frame of \(K_{s-1}\), \(F_s\) the new observation rows restricted to that frame, and \(H_{s-1,N}=I_{s-1}^*G_NI_{s-1}\). Then
\[
 D_{s,N}=F_sH_{s-1,N}^{-1}F_s^*,\qquad
 L_{s,N}=H_{s-1,N}^{-1}F_s^*D_{s,N}^{-1},\quad F_sL_{s,N}=I.
 \tag{AP16}
\]
The lift \(L_{s,N}\) is orthogonal to \(\ker F_s\), so its energy is \(D_{s,N}^{-1}\). This proves the exact quotient assertion.

Restrictions and minima preserve both inequalities in AP2 and preserve source nesting. Applying the same two paired determinant comparisons to this rank-\(b_s\) quotient gives
\[
 0\le X_s-X_{s-1}\le2b_sE_k. \tag{AP17}
\]
In particular,
\[
 0=X_0\le X_1\le\cdots\le X_d=\mathcal K_k,\qquad
 \mathcal K_k=\sum_{s=1}^d\bigl[-\mathcal R\log\det D_{s,N}\bigr].
 \tag{AP18}
\]
Summing only after depth \(s\) gives AP13 again because \(\sum_{j>s}b_j=t_s\). This proves a positive decomposition of the original signed return; it is stronger than an error estimate for one truncation. It does not determine the values of the positive increments.

The dimensions are intrinsic: BD6 gives \(b_s=\#\{a:\epsilon_a\ge s\}\) for the actual observation-chain lengths. AP16 supplies the metric on each such quotient and therefore the data omitted by the integer multiplicity alone. In particular \(b_1\ge k-18\) on the proved domain and \(\sum_{s>8}b_s\le128\).

## AP5. Data size and a stronger finite-error constant

Let \(r_i\) be the number of selected new rows from level \(i\). With the original \(Q_N^{-1}\) known, diagonal probes need at most \(n\sum r_i=nr_s\) complex entries; pairs with level zero need \(2nr_s\); other pairs need \(2\sum_{i<j}r_ir_j\). The required diagonal subtractions are already included, with the opposite blocks supplied by Hermitian symmetry. Thus
\[
 \text{additional complex entries}\le3nr_s+r_s^2=O(kq). \tag{AP19}
\]
The baseline's \(n^2\) real entries and the precision of every requested value remain part of the calculation.

Suppose each supplied covariance has operator error at most \(\eta\), measured in one fixed observed coefficient norm. Replace it by its Hermitian part, which does not increase this error. In AP8 the off-diagonal error can be collected as
\[
 \tfrac12\left(E_{ij}^{+}+iE_{ij}^{\,i}-(1+i)(E_i+E_j)\right).
\]
Its norm is at most \((1+\sqrt2)\eta\), improving the incoming \(3\eta\) bound. The diagonal error is at most \(\eta\). For block vectors use the scalar matrix with diagonal1 and off-diagonal \(1+\sqrt2\); its largest absolute eigenvalue is \(1+s(1+\sqrt2)\). The triangle inequality followed by its quadratic-form bound proves
\[
 \|\widehat{\mathcal S}_s-\mathcal S_s\|
 \le a_s\eta,\qquad a_s=1+s(1+\sqrt2). \tag{AP20}
\]
A scalar-row principal selection cannot enlarge the bound.

If the actual selected Gram has lower eigenvalue bound \(h_N> a_s\eta\), put \(\varepsilon_N=a_s\eta/h_N\). Then its full relative bounds are \(1-\varepsilon_N\) and \(1+\varepsilon_N\). Minimizing each bounding form over the same first-coordinate fibre transfers those bounds to \(C_{s,N}\). For \(\varepsilon_N\le\varepsilon<1\) at all cutoffs,
\[
 |\widehat X_s-X_s|\le
 e_s:=2r_s\log\frac{1+\varepsilon}{1-\varepsilon}. \tag{AP21}
\]
Combining with AP13 gives
\[
 \widehat X_s-e_s\le\mathcal K_k
 \le\widehat X_s+e_s+2t_sE_k. \tag{AP22}
\]
These intervals can be intersected over all computed depths. The certified lower endpoint can additionally be replaced by its maximum with zero. The upper endpoint can be replaced by the minimum of all the displayed upper endpoints. AP18 proves validity without assuming independent errors or adding the same source remainder repeatedly.

A directly computable eigenvalue floor is \(\lambda_{\min}(\widehat{\mathcal S}^{\rm sel}_s)-a_s\eta\), when positive, since the Rayleigh quotient changes by at most \(a_s\eta\). Another is \(\sigma_{\min}(\mathcal O_s^{\rm sel})^2/\lambda_{\max}(G_N)\). These are numerical margins of the actual matrices, never consequences of rank alone.

## AP6. New optimal positive regularizer for the certified error

For an invertible polynomial probe keep the original response
\[
 Y_P(z)=\Lambda z(zI+G^{-1}T_P^*GT_P)^{-1}L,\quad z>0.
\]
Multiplication by \(G\) and \(GL=\Lambda^*Q\) proves
\[
 \Sigma_P(z)=z^{-1}Y_P(z)Q^{-1}
 =\Lambda(T_P^*GT_P+zG)^{-1}\Lambda^*. \tag{AP23}
\]
Let \(a\ge\|P(M)\|_G^2\), \(b\ge\|V[P]\|\), both positive certified finite numbers. For \(x=P(M)y\), the norm inequality gives \(y^*Gy\ge a^{-1}x^*Gx\). Hence \(T_P^*GT_P\succeq a^{-1}G\). Adding \(zG\), inverting, and applying \(\Lambda\) proves
\[
 (1+za)^{-1}V[P]\preceq\Sigma_P(z)\preceq V[P].
\]
If the measured response has operator error at most \(\eta_P\) and the supplied \(Q^{-1}\) is exact, set \(c=\eta_P\|Q^{-1}\|\). After Hermitian projection, a full error bound is
\[
 \|\widehat\Sigma_P(z)-V[P]\|
 \le f(z):=\frac{baz}{1+az}+\frac c z. \tag{AP24}
\]
The first term is the exact consequence of the relative bias, stronger than \(baz\). The second retains the observed response amplification.

For \(c>0\) and \(ac<b\), let \(\tau=\sqrt{ac/b}\in(0,1)\). Differentiating AP24 gives
\[
 z_*=\frac{\tau}{a(1-\tau)},\qquad
 \min_{z>0}f(z)=b(2\tau-\tau^2)=2\sqrt{abc}-ac. \tag{AP25}
\]
Indeed \(f'(z)=ba/(1+az)^2-c/z^2\), which changes sign exactly once at \(z_*\). If \(ac\ge b\), this derivative is negative and the infimum is \(b\) as \(z\to\infty\). For \(c=0\), the infimum is zero as \(z\downarrow0\). Those limiting cases do not assert a finite regularizer achieving the infimum.

For a requested covariance error \(0<\eta<b\), the sufficient and exact threshold for this bound is
\[
 \eta_P\le
 \frac{b}{a\|Q^{-1}\|}
 \left(1-\sqrt{1-\eta/b}\right)^2. \tag{AP26}
\]
Use \(z_*\) with the actual \(c\), or any positive \(z\) whose AP24 value is below the target. This evaluates the best tradeoff in the specified certified bound. It makes no assertion that its constants are the actual worst-case errors of all native probes.

The inverse quotient error has an explicit place in this bound. If \(\|\widehat D-Q^{-1}\|\le\xi\), \(\|\widehat Y-Y\|\le\eta_P\), and \(\|Y\|\le y_0\), expansion of \(\widehat Y\widehat D-YQ^{-1}\) bounds its norm by
\[
 c=\eta_P\|Q^{-1}\|+(y_0+\eta_P)\xi. \tag{AP26a}
\]
AP24–25 hold with this \(c\). One uniform valid value is \(y_0=\sqrt{\|Q\|\|Q^{-1}\|}\): the response is a positive contraction in the \(Q\) metric, because \(Q^{1/2}YQ^{-1/2}\) is the compression of \(z(z+H)^{-1}\) by the original \(G\)-isometric section \(LQ^{-1/2}\). Its Euclidean norm is therefore at most the displayed similarity bound. This proves the complete amplification of both measured factors.

## AP7. Centered current with the actual quotient uncertainty

Put \(M_B=\Lambda ML=S_{10}Q\). The physical centered action is \(iM_B\). In the original output frame its real current is
\[
 \Phi(b)=i b^*(QM_B-M_B^*Q)b
 =b^*Q\,i(S_{10}-S_{01})Qb. \tag{AP27}
\]
The two positive covariances give
\[
 T_c=\tfrac12\bigl(V[1+iy]-V[1-iy]\bigr)
 =i(S_{10}-S_{01}). \tag{AP28}
\]
This is the same complete current as the polynomial-gauge formula BD29, since both equal the first expression in AP27. Thus the connecting map includes its derivative correction automatically. It does not substitute for other cross-pairings in BD31.

With exact \(Q,b\), two covariance errors of norm at most \(\eta\) imply
\[
 |\widehat\Phi-\Phi|\le\eta\|Qb\|^2.
\]
Now also allow a Hermitian quotient estimate with
\[
 \widehat Q=Q^{1/2}(I+E)Q^{1/2},\quad\|E\|\le\varepsilon,
 \qquad \|Q^{1/2}(\widehat T_c-T_c)Q^{1/2}\|\le\zeta.
\]
These are measured errors in the original quotient geometry. Put \(A=Q^{1/2}T_cQ^{1/2}\), \(y=Q^{1/2}b\). Then
\[
 \widehat\Phi=y^*(I+E)(A+\Delta A)(I+E)y,\quad \Phi=y^*Ay.
\]
Expanding every term and using the operator norm gives the complete bound
\[
 |\widehat\Phi-\Phi|
 \le\left[(2\varepsilon+\varepsilon^2)\|A\|
 +(1+\varepsilon)^2\zeta\right]\,b^*Qb. \tag{AP29}
\]
This keeps both quotient factors and their cross term. The vector \(b\) here is the fixed original observed class. It is not replaced by a newly minimized vector at each probe.

If its supplied value is also approximate, set \(\rho=\|Q^{1/2}(\widehat b-b)\|\), \(v=\sqrt{b^*Qb}\), and let \(e_A\) be the bracket in AP29. The same expansion gives
\[
 |\widehat\Phi(\widehat b)-\Phi(b)|
 \le e_Av^2+(2\rho v+\rho^2)(1+\varepsilon)^2(\|A\|+\zeta).
 \tag{AP30}
\]
Indeed the difference between the quadratic forms of the computed Hermitian matrix at \(y\) and \(y+\Delta y\) is at most its norm times \(2\|\Delta y\|\|y\|+\|\Delta y\|^2\). Thus the acquisition error of the original class is also retained.

## AP8. Exact verification and attribution

The checker constructs a four-dimensional companion action with roots \(2,3,4,5\), one original observation row, a nonidentity complex covariance and a positive rank-one source update at four cutoffs. The true native root grid is not identified with this example. It verifies every complex probe, the whole Schur complement, the nested determinant factorization, the quotient maps AP16, and the current before and after polarization. It also checks AP25–26 by exact algebra. A reversed imaginary phase and a raw lower-right block fail in explicit negative controls.

The incoming proof's finite-polarization and complete selected-covariance construction is retained as provenance. The new contributions here are AP17–18's increasing depth return, AP20's stronger error constant, AP25–26's evaluated regularizer and AP29's full quotient-error current bound. The original source estimate and observation-depth theorem are credited to SZ-20260922-021, BD1–3 and BD11–12, whose complete proofs accompany this continuation. Classical Schur elimination is proved above; its human-source context is Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, [The Feshbach–Schur map and perturbation theory, arXiv:2105.02058v1](https://arxiv.org/abs/2105.02058v1), Theorem1.2 and the equations labelled Fesh and QP, read in original author TeX as recorded in the predecessor.

The fixed original matrix values still determine the \(kq\) coefficient and separate current signs. The new positive filtration and finite acquisition budget specify and strengthen that calculation; they do not replace those values by ranks.
