# What the original observation retains of split support

22 September 2026. Result SZ-20260922-028, root derivation ST1–ST20.

The support idempotent has two measured eigenvalues. We calculate both, their exact defect through the original invariant kernel, and their effect on the original terminal class. One eigenvalue approaches one at the doubled exponential rate already proved for boundary leakage. The other differs from the actual retention of the second boundary vector by at most that same leakage. We then calculate how the measured support and its defect determine the terminal class's combined current-sector mass, with an absolute error at that rate. All statements below concern the original observation and its complete source metric.

## 1. Original objects, source provenance and domain

Keep the stipulated simple quartet, its original admitted period, the five-orbit observation, and
\[
k\ge17,\quad k\equiv1\pmod4,\quad q=(k+1)^2,\qquad
Q_k(y)=\prod_{a,b=0}^k\bigl[y-(2b-k)\gamma+i(2a-k)\delta\bigr],
\quad E=\mathbb C[y]/Q_k.
\tag{ST1}
\]
At each literal source cutoff \(q-1\le N\le2q\), retain the complete original source metric \(G_N\), observation \(\Lambda:E\to B\), and all of \(K=\ker\Lambda\). A dagger denotes the adjoint in this metric. The original minimum section and its Euclidean-coordinate isometry are
\[
Q_B=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
L=G_N^{-1}\Lambda^*Q_B,\quad
J=LQ_B^{-1/2},\quad J^\dagger J=I_B,\quad P_B=JJ^\dagger=L\Lambda.
\tag{ST2}
\]
The use of \(J\) preserves the metric: \(Q_B^{1/2}\Lambda\) restricted to \(K^\perp\) is its inverse. In particular none of the following operators changes the original minimum. These facts and the exact boundary decomposition
\[
M=C+R,\quad C=C^\dagger,\quad
R=\epsilon f e^\dagger,\quad e^\dagger f=0,
\quad\|e\|=\|f\|=1,\quad\epsilon>0
\tag{ST3}
\]
are proved in [CE2–8](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/EVOLUTION_PROOF.md#L18). The vectors are the actual consecutive monic source classes \(e=b_N/\sqrt{E_N}\), \(f=b_{N+1}/\sqrt{F_N}\), and \(\epsilon=\sqrt{E_NF_N}/\omega_N\).

Write \(\Pi=ee^\dagger+ff^\dagger\), \(H=\operatorname{im}(I-\Pi)\). The support-algebra map is
\[
\rho:\mathbb C\times\mathbb C[\eta]/(\eta^2)\longrightarrow\operatorname{End}(E),
\qquad (c_0,c_1+c_2\eta)\longmapsto c_0(I-\Pi)+c_1\Pi+c_2R.
\tag{ST4}
\]
For completeness, \(\Pi^2=\Pi\), \(\Pi R=R\Pi=R\), and \(R^2=0\) prove multiplicativity. Restriction to \(H\ne0\) recovers \(c_0\), application to \(f\) recovers \(c_1\), and then application to \(e\) recovers \(c_2\); thus the map is faithful. It receives the original additive-monoid algebra of \(\mathbb Z\sqcup\{\tau\}\): \([\tau]\mapsto I\), \([n]\mapsto\Pi+nR\). The supported-zero symbol maps to \(\Pi\); multiplication of these symbols means addition in that original monoid. Its kernel is exactly the ideal \(([1]-[0])^2\), since the monoid algebra is \(\mathbb C\times\mathbb C[t^{\pm1}]\), with \(t\mapsto1+\eta\). This is the support input of [NI19–29 in the pinned node edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6af54ea3c8ef99127af327f3103e086c68d482c2/workbenches/splitzero-tandem/branches/identity-absorber-square/NATIVE_DUAL_NUMBER_RECEIVER.md); every part required below has just been proved here.

Define measured columns and support without replacing either source projection:
\[
u=J^\dagger e,\quad v=J^\dagger f,\quad U=[u,v],\quad
\mathcal C=U^*U=\begin{pmatrix}a&r\\\bar r&d\end{pmatrix},
\quad\mathfrak d=ad-|r|^2,
\quad A=J^\dagger\Pi J=UU^*,\quad\alpha=1-a.
\tag{ST5}
\]
Here \(A\) denotes measured support throughout this note; it is distinct from the compressed energy denoted \(A_N\) in older determinant papers. On the proved finite area guards,
\[
0\prec\mathcal C\preceq I_2,\quad \mathfrak d\ge\Theta_N>0,
\quad |r|^2\le\alpha(1-d),
\]
\[
\alpha\le e^{-2q\psi(t_N)+O_{h,\varpi}(k\log(q+2))},\quad
-\log\Theta_N=O_{h,\varpi}(k\log(q+2)),\quad
\log\epsilon=q\psi(t_N)+O_{h,\varpi}(k\log(q+2)),
\quad t_N=(N+1-q)/q.
\tag{ST6}
\]
These are the original complete-source and conductor estimates [RC25](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L222). The exact polynomial, Gamma and elliptic sources remain those cited there: T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, DLMF Chapter 18; R. A. Askey and R. Roy, Chapter 5; B. C. Carlson, Chapter 19. The finite linear algebra below is proved in full and needs no additional external theorem.

## 2. Both support eigenvalues and the full kernel defect

The two nonzero eigenvalues of \(A\) are exactly
\[
\vartheta_\pm=\frac{a+d\pm\sqrt{(a-d)^2+4|r|^2}}2.
\tag{ST7}
\]
Indeed if \(\mathcal Cz=\vartheta z\), then \(Uz\ne0\) and \(A(Uz)=U\mathcal Cz=\vartheta Uz\). Conversely every nonzero eigenvector of \(A\) lies in \(\operatorname{im}U\); this proves the correspondence including multiplicities. The quadratic formula applied to \(\det(\lambda I-\mathcal C)\) proves ST7. All remaining eigenvalues of \(A\) are zero, of multiplicity \(b-2\), where \(b=\dim B\).

There is a bound valid even when these eigenvalues collide:
\[
\boxed{0\le1-\vartheta_+\le\alpha,\qquad
0\le d-\vartheta_-\le\alpha,\qquad
\vartheta_-\ge\Theta_N.}
\tag{ST8}
\]
The Rayleigh quotient at the first coordinate gives \(\vartheta_+\ge a=1-\alpha\), while \(\mathcal C\preceq I\) gives \(\vartheta_+\le1\). Put \(\ell=1-\vartheta_+\). Since \(\vartheta_++\vartheta_-=a+d\), one has \(\vartheta_-=d-\alpha+\ell\), giving the second assertion. Finally \(\vartheta_-=\mathfrak d/\vartheta_+\ge\mathfrak d\ge\Theta_N\). There is no division by an eigenvalue gap.

The full failure of multiplicativity is a positive kernel square:
\[
\Phi(XY)-\Phi(X)\Phi(Y)=J^\dagger X(I-P_B)YJ,
\quad\Phi(X)=J^\dagger XJ,
\]
\[
\boxed{A-A^2=D^\dagger D,\qquad D=(I-P_B)\Pi J.}
\tag{ST9}
\]
Insert \(P_B=JJ^\dagger\) to prove the first identity, then take \(X=Y=\Pi\). Thus the defect includes precisely the original kernel projection. Its two possibly nonzero eigenvalues are \(\vartheta_\pm(1-\vartheta_\pm)\), retaining the labels inherited from ST7 rather than reordering them. Since \(|x(1-x)-y(1-y)|=|x-y||1-x-y|\le|x-y|\) on \([0,1]\), ST8 gives
\[
0\le\vartheta_+(1-\vartheta_+)\le\alpha,\qquad
\big|\vartheta_-(1-\vartheta_-)-d(1-d)\big|\le\alpha.
\tag{ST10}
\]
Equivalently the two corresponding singular values of \(D\) are \(\sqrt{\vartheta_\pm(1-\vartheta_\pm)}\). The second differs from \(\sqrt{d(1-d)}\) by at most \(\sqrt\alpha\), using \(|\sqrt x-\sqrt y|\le\sqrt{|x-y|}\). The first is at most \(\sqrt\alpha\). This retains the second mixed direction even when its defect is large.

The exact support volume has the stronger scalar receiver
\[
\boxed{0\le\log d-\log\det{}^+A
\le\frac{\alpha}{\Theta_N}.}
\tag{ST11}
\]
Here \(\det{}^+A=\vartheta_+\vartheta_-=\mathfrak d\). Write \(d-\mathfrak d=\alpha d+|r|^2\le\alpha\) by ST6. Therefore \(\log(d/\mathfrak d)=\log(1+(d-\mathfrak d)/\mathfrak d)\le\alpha/\Theta_N\). This is a comparison with the actual \(d=\|P_Bf\|^2\), not an assumed unit retention.

At all four original cutoffs with signs \(+,+,-,-\),
\[
\left|\mathcal R\log\det{}^+A-\mathcal R\log d\right|
\le\sum_{N\in\{q-1,q,2q-1,2q\}}\frac{\alpha_N}{\Theta_N}.
\tag{ST12}
\]
Since \(\Theta_N\le d_N\le1\), the entire support-volume return is \(O_{h,\varpi}(k\log(q+2))=o(kq)\). The bound in ST12 is at the doubled exponential rate separately at the four arguments \(0,1/q,1,1+1/q\). No signed value is assigned to \(\mathcal R\log d\).

## 3. The original terminal class retains measured support to doubled accuracy

Use the exact terminal cardinal \(x=v_+\) of TR1, with \(Mx=(k\gamma-ik\delta)x\). Keep precisely the established terminal domain \(\gamma\ge1000\delta\), the original five-orbit requirement and \(|\varpi|\ge R_{\rm corner}\), with the finite radius of [RC37–42](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L332). This domain proves \(P_Bx\ne0\). In the \(J\)-coordinates define
\[
\widehat y=J^\dagger x/\|P_Bx\|,\quad
g=u/\sqrt a,\quad h=(v-(r/a)u)/\sqrt{\mathfrak d/a},\quad
c_g=g^*\widehat y,\quad c_h=h^*\widehat y.
\tag{ST13}
\]
These are the exact observed orthonormal coordinates of [TR9–11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/40a766ed3a8e0eadd9947f591803255b6eecf184/workbenches/splitzero-tandem/continuations/20260922-terminal-response/TERMINAL_COHERENCE_PROOF.md). The complete terminal equation proves \(|c_g|\le\eta_N\le e^{-q\psi(t_N)+O_{h,\varpi}(k\log(q+2))}\), with finite \(\eta_N\) in TR10. Let
\[
\Pi_{\rm range}=U\mathcal C^{-1}U^*,\quad
\mu=\widehat y^*\Pi_{\rm range}\widehat y=|c_g|^2+|c_h|^2,
\quad\mathfrak s=\widehat y^*A\widehat y.
\tag{ST14}
\]
Multiplication proves that \(\Pi_{\rm range}\) is the orthogonal range projector. It is retained alongside the measured weights in \(A\).

The exact measured support in this frame is
\[
A\big|_{g,h}=\begin{pmatrix}
a+|r|^2/a&r\sqrt{\mathfrak d}/a\\
\bar r\sqrt{\mathfrak d}/a&d-|r|^2/a
\end{pmatrix}.
\tag{ST15}
\]
This follows by substituting \(u=\sqrt a\,g\) and \(v=(r/\sqrt a)g+\sqrt{\mathfrak d/a}\,h\) in \(UU^*\). All complex phases remain. Because \(0\preceq\mathcal C\preceq I\), diagonalization gives \(\mathcal C^2\preceq\mathcal C\), whose first diagonal entry implies \(|r|^2/a\le1-a=\alpha\). Also \(a+|r|^2/a\le1\) and \(\mathfrak d/a\le1\). Thus
\[
\boxed{|\mathfrak s-d\mu|\le(\eta_N+\sqrt\alpha)^2=:E_N^{\rm supp}.}
\tag{ST16}
\]
To prove the bound explicitly, subtract \(d\mu\) from the quadratic form ST15. The coefficient of \(|c_g|^2\) is \(a+|r|^2/a-d\), of absolute value at most one. The other diagonal term has absolute value at most \(\alpha|c_h|^2\). The off-diagonal term is bounded by \(2\sqrt{\mathfrak d/a}\sqrt{|r|^2/a}|c_g||c_h|\le2\sqrt\alpha\eta_N\). Since \(|c_h|\le1\), their sum proves ST16, with no lower bound on \(\mu\).

There is also a complete terminal defect estimate:
\[
\boxed{\left|\widehat y^*(A-A^2)\widehat y-d(1-d)\mu\right|
\le2E_N^{\rm supp}.}
\tag{ST17}
\]
Set \(F=A-d\Pi_{\rm range}\). Its eigenvalues on the current plane are \(\vartheta_\pm-d\), each in \([-1,1]\), so \(\|F\|\le1\). Its second column in ST15 has squared norm
\(\mathfrak d|r|^2/a^2+|r|^4/a^2=d|r|^2/a\le\alpha\). Hence \(\|F\widehat y\|\le|c_g|+\sqrt\alpha|c_h|\le\eta_N+\sqrt\alpha\). Now
\(A-A^2-d(1-d)\Pi_{\rm range}=(1-2d)F-F^2\).
Its expectation is bounded by ST16 plus \(\|F\widehat y\|^2\), proving ST17. Components orthogonal to the current plane vanish from all these operators, but remain in the unit norm of \(\widehat y\).

In particular the combined current-sector mass has the quantitative receiver
\[
\boxed{\left|\mu-\frac{\mathfrak s}{d}\right|
\le\frac{E_N^{\rm supp}}{d}\le\frac{E_N^{\rm supp}}{\Theta_N}
\le e^{-2q\psi(t_N)+O_{h,\varpi}(k\log(q+2))}.}
\tag{ST18}
\]
If \(z_+,z_-\) are the canonically phased current amplitudes TR14–18, then \(\mu=|z_+|^2+|z_-|^2\), and exactly
\[
\mathfrak s-2d\Re(z_+\bar z_-)
=(\mathfrak s-d\mu)+d|z_+-z_-|^2.
\tag{ST19}
\]
Consequently its absolute value is at most \(E_N^{\rm supp}+d(\sqrt2\eta_N+\delta_N^{\rm tr})^2\), also at the doubled rate. This carries support through to the real current coherence, including zero amplitude cases. It is stronger than an assertion that the two support presentations correspond: the complete terminal error has been evaluated in the original metrics.

## 4. Receiver into the signed current and scope

The exact signed current is
\[
j_N=2\epsilon\sqrt{\mathfrak d}\Im(\bar c_gc_h)
-2\epsilon(\Im r)|c_g|^2.
\]
Its measured-support bound therefore improves the mass-free magnitude estimate to
\[
\boxed{|j_N|\le2\epsilon\sqrt{\mathfrak d}\eta_N
\sqrt{\min\{1,(\mathfrak s+E_N^{\rm supp})/d\}}
+2\epsilon|r|\eta_N^2.}
\tag{ST20}
\]
Use \(|c_h|^2\le\mu\le\min\{1,(\mathfrak s+E_N^{\rm supp})/d\}\) in the exact current expression. The last term remains the absolutely doubled-exponential error of TR20. This bound retains the actual measured support; it does not assume that its value is nonzero or replace it by one. The companion mixed-probe derivation calculates the ordered products carrying the imaginary part through the same observation. Together these are distinct quantitative receivers of the new support data: ST18 controls current-sector mass, while the ordered mixed products retain orientation. A sign for the particular terminal class still requires its signed mixed-product value. No RH conclusion is inferred from a positive support bound.

All four cutoffs remain separate. For any of ST16–19, the error of its signed four-cutoff return is bounded by the sum of the four displayed absolute errors; the proof is the triangle inequality with exactly the signs \(+,+,-,-\). No cutoff or full-kernel term has been dropped.
