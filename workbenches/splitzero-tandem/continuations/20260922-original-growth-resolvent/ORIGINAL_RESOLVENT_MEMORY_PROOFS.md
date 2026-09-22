# The exact kernel memory of the original measured resolvent

22 September 2026. Result SZ-20260922-020, root derivation RM1–RM23.

The received PR1–PR44 calculation evaluates a determinant of the full observed resolvent. This continuation identifies the entire matrix correction produced by the observation kernel, constructs the smallest kernel space that carries that correction, and proves its exact reconstruction from the observed family. Every original metric, observation, word and complex cross term remains in the formulas. The construction applies directly to the programme's word \(T_k=D_k(M)\) and its canonical metrics at the four original cutoffs. It does not assign the unresolved native determinant coefficient.

The elimination used here is the finite positive-metric Feshbach–Schur map. Its human source is Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, [*The Feshbach–Schur map and perturbation theory*](https://arxiv.org/abs/2105.02058v1), original author TeX `AriFestFSM_arxiv.tex`, theorem `thm:isospF`, equations `Fesh`, `QP`, `Hlam-deco`, `Ulam-def`, source lines 398–489. The exact substitution is their operator \(H-\lambda\) with our \(T^{\dagger_G}T+zI\), their projection with the original minimum-section projection \(L\Lambda\), and \(\lambda=-z\). The finite proofs below also supply the complete elimination and reconstruction explicitly. This is a use of that established construction, not a claim of inventing it.

## RM1. Original value and kernel coordinates

Let \(E=\mathbb C^q\) carry the positive Hermitian metric \(G\), let \(\Lambda:E\to B=\mathbb C^n\) be onto, and let \(K=\ker\Lambda\), \(m=q-n\). Let \(I_K:\mathbb C^m\to E\) be a fixed full frame of the actual kernel, and retain a linear word \(T:E\to E\). Put

\[
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad
 L=G^{-1}\Lambda^*Q,\quad H_K=I_K^*GI_K,\quad H=T^{\dagger_G}T=G^{-1}T^*GT.
 \tag{RM1}
\]

Then \(\Lambda L=I_n\), \(L^*GL=Q\), and \(I_K^*GL=0\). In particular the map

\[
 U_0:B\oplus\mathbb C^m\longrightarrow E,\qquad U_0(b,a)=Lb+I_Ka
 \tag{RM2}
\]

is an isomorphism with source metric \(\operatorname{diag}(Q,H_K)\). Indeed applying \(\Lambda\) to a zero image gives \(b=0\), then injectivity of \(I_K\) gives \(a=0\); dimensions finish the proof. The orthogonality follows by direct substitution in RM1. This proves the coordinate map without replacing the value metric or kernel metric by a different source.

Define the three energy blocks

\[
 E_{BB}=L^*T^*GTL,\qquad X=I_K^*T^*GTL,\qquad E_{KK}=I_K^*T^*GTI_K.
 \tag{RM3}
\]

Thus \(U_0^*T^*GTU_0=\begin{psmallmatrix}E_{BB}&X^*\\X&E_{KK}\end{psmallmatrix}\succeq0\). Notice that \(E_{KK}\) is the energy of the full rectangular map \(T I_K\). No compressed arithmetic endomorphism has been substituted.

## RM2. The complete attained minimum at every positive parameter

For \(z>0\), set

\[
 D(z)=X^*(zH_K+E_{KK})^{-1}X,\quad
 F(z)=zQ+E_{BB}-D(z).
 \tag{RM4}
\]

The matrix \(F(z)\) is positive definite. More precisely, for every \(b\in B\),

\[
 b^*F(z)b=z\,b^*Qb+
 \min_{a\in\mathbb C^m}\left\{\|T(Lb+I_Ka)\|_G^2+z\,a^*H_Ka\right\}.
 \tag{RM5}
\]

The unique minimizer is

\[
 a_z(b)=-(zH_K+E_{KK})^{-1}Xb.
 \tag{RM6}
\]

To prove both statements, expand the braces using RM3, then complete the square with its strictly positive \(a\)-block. The remaining quadratic form is \(E_{BB}-D(z)\succeq0\). Adding \(zQ>0\) proves strict positivity. This also specifies the map lifting each observed vector back to its exact minimizing full vector \(Lb+I_Ka_z(b)\).

## RM3. Matrix recovery of the full measured resolvent

Retain the actual observed family

\[
 \mathscr Y(z)=\Lambda z(zI+H)^{-1}L.
\]

Solving the two block equations of \(U_0^*G(zI+H)U_0\), whose right-hand side for an observed input \(b\) is \(z(Qb,0)^T\), gives

\[
 \boxed{\mathscr Y(z)=zF(z)^{-1}Q.}
 \tag{RM7}
\]

Consequently the entire memory matrix is recoverable from the original observed family:

\[
 \boxed{D(z)=E_{BB}-zQ\bigl(\mathscr Y(z)^{-1}-I\bigr).}
 \tag{RM8}
\]

The multiplication order in RM7–RM8 is essential. For example \(\mathscr Y(z)\) need not be Hermitian in the original coefficient frame; \(Q\mathscr Y(z)\) is Hermitian. The high-parameter coefficient also recovers \(E_{BB}\):

\[
 E_{BB}=\lim_{z\to\infty}zQ\bigl(\mathscr Y(z)^{-1}-I\bigr),
 \tag{RM9}
\]

because \(D(z)=O(z^{-1})\). All these statements are finite exact identities in the displayed maps.

## RM4. The positive memory measure and its complete kernel space

For the sole purpose of expressing the same metric in an orthonormal frame, define

\[
 A=H_K^{-1/2}E_{KK}H_K^{-1/2},\quad
 C=H_K^{-1/2}XQ^{-1/2},\quad B=Q^{-1/2}E_{BB}Q^{-1/2}.
 \tag{RM10}
\]

The inverse coordinate maps are specified by \(I_KH_K^{-1/2}\) and \(LQ^{-1/2}\); thus no original mass or norm is removed. Write \(A=\sum_{\lambda\ge0}\lambda P_\lambda\), with its complete spectral projections, including multiplicities. Positivity of RM3 implies \(P_0C=0\). One proof is that a vector \(a\in\ker A\) gives zero energy to \(TI_KH_K^{-1/2}a\), hence this vector is zero and its energy pairing with \(TLQ^{-1/2}b\) vanishes for every \(b\).

Therefore

\[
 \widehat D(z):=Q^{-1/2}D(z)Q^{-1/2}
 =\sum_{\lambda>0}\frac{M_\lambda}{z+\lambda},\qquad
 M_\lambda=C^*P_\lambda C\succeq0.
 \tag{RM11}
\]

This is a finite matrix Stieltjes transform: the definition here is exactly a sum of positive matrix masses divided by \(z+\lambda\) for positive real \(\lambda\). Repeated kernel energies use one full residue \(M_\lambda\); no arbitrary eigenvector choice enters it. At a zero energy, the residue vanishes by the proved relation \(P_0C=0\), rather than by deletion.

Define the actual observable kernel subspace

\[
 \mathcal H_{\rm mem}=\operatorname{span}\{A^jCb:b\in\mathbb C^n,\ 0\le j<m\}\subseteq\mathbb C^m.
 \tag{RM12}
\]

Cayley–Hamilton shows that this space is \(A\)-invariant. Since \(A=A^*\), its orthogonal complement is invariant too. Spectral interpolation by polynomials in \(A\) then proves

\[
 \mathcal H_{\rm mem}=\bigoplus_{\lambda>0}\operatorname{ran}(P_\lambda C),\qquad
 \dim\mathcal H_{\rm mem}=\sum_{\lambda>0}\operatorname{rank}M_\lambda.
 \tag{RM13}
\]

For the rank statement use \(M_\lambda=(P_\lambda C)^*(P_\lambda C)\), so both matrices have the same null space. The inclusion \(I_KH_K^{-1/2}:\mathcal H_{\rm mem}\hookrightarrow K\subset E\) is the exact connecting isometry to the programme. The orthogonal complement is retained as a reducing kernel space with zero coupling to the observation.

## RM5. Minimality and uniqueness, with a finite moment certificate

Any representation of RM11 in the form \(C_1^*(zI+A_1)^{-1}C_1\), with \(A_1\succeq0\) and no zero residue, has a residue \(C_1^*P_{1,\lambda}C_1=M_\lambda\) at each actual pole. The dimension of its \(\lambda\)-eigenspace is at least \(\operatorname{rank}M_\lambda\). Summing gives the lower bound in RM13. Restriction to \(\mathcal H_{\rm mem}\) attains it, so this is a smallest realization of the original memory.

It is unique up to an isometry that also intertwines \(A\) and \(C\). Here is a direct proof. Equality of the rational functions gives equality of their expansions at infinity, hence

\[
 C^*A^jC=C_1^*A_1^jC_1\quad(j\ge0).
\]

Send each vector \(\sum_j A^jCb_j\) to \(\sum_j A_1^jC_1b_j\). The squared norm and every cross inner product are the same, by the moment identities with exponent \(i+j\). The map is well-defined, isometric, onto the generated spaces, and intertwines \(A\) and \(A_1\). It also maps \(C\) to \(C_1\). This proves the assertion.

There is an exact finite rank certificate. The block matrix

\[
 \mathcal M_m=[C^*A^{i+j}C]_{i,j=0}^{m-1}
\]

is the Gram matrix of \([C,AC,\ldots,A^{m-1}C]\). Thus

\[
 \boxed{\operatorname{rank}\mathcal M_m=\dim\mathcal H_{\rm mem}.}
 \tag{RM14}
\]

It uses the original phase-bearing moments, not their scalar traces.

## RM6. The exact correction to compressing before taking the resolvent

In the orthonormal value frame the compression of the positive energy \(H\) is \(B\). Put

\[
 F_0=zI+B,\qquad R(z)=F_0^{-1/2}\widehat D(z)F_0^{-1/2}.
\]

RM5 gives \(0\preceq R(z)\prec I\). Comparing the correct family with \(Y_{\rm energy}(z)=z(zI+B)^{-1}\) gives

\[
 \widehat{\mathscr Y}(z)\succeq Y_{\rm energy}(z),\qquad
 \log\frac{\det\mathscr Y(z)}{\det Y_{\rm energy}(z)}
 =-\log\det(I-R(z))\ge0.
 \tag{RM15}
\]

Both statements follow by inversion and the factorization of \(F_0-\widehat D\). The rank of \(R(z)\) equals \(\operatorname{rank}C\), and the exact correction is the sum \(-\sum_{j=1}^{\operatorname{rank}C}\log(1-r_j(z))\). In particular it vanishes at one positive \(z\) if and only if \(C=0\), which is equivalent to \(K\) reducing the positive energy \(H\). This proves precisely when the omission is allowed.

For comparison with the arithmetic operator compressed first, write the full word itself in the same orthogonal splitting:

\[
 \widetilde T=\begin{pmatrix}T_{BB}&T_{BK}\\T_{KB}&T_{KK}\end{pmatrix}.
\]

Then

\[
 B=T_{BB}^*T_{BB}+T_{KB}^*T_{KB},\quad
 C=T_{BK}^*T_{BB}+T_{KK}^*T_{KB},\quad
 A=T_{BK}^*T_{BK}+T_{KK}^*T_{KK}.
 \tag{RM16}
\]

Substitution in RM7 proves the complete relation to the resolvent of \(T_{BB}^*T_{BB}\): its missing effective term is \(T_{KB}^*T_{KB}-C^*(zI+A)^{-1}C\). Its sign is not fixed. Indeed with scalar blocks, \(T=\begin{psmallmatrix}0&0\\1&0\end{psmallmatrix}\) gives positive term \(1\), while \(T=\begin{psmallmatrix}1&1\\0&0\end{psmallmatrix}\) gives negative term \(-1/(z+1)\). These exact words have positive full energies. Thus the defect defines the specified memory family; it is not a reason to end the calculation.

## RM7. Every zero direction and every determinant factor

The full energy in this frame is \(\begin{psmallmatrix}B&C^*\\C&A\end{psmallmatrix}\). Let \(\mathcal H_{\rm inv}=\mathcal H_{\rm mem}^{\perp}\subset K\). It is reducing and has no coupling to \(B\). Hence

\[
 \det(zI+H)=\det(zI+A|_{\mathcal H_{\rm inv}})
 \det\begin{pmatrix}zI+B&C_{\rm mem}^*\\C_{\rm mem}&zI+A_{\rm mem}\end{pmatrix}.
\]

The same factor occurs in \(\det(zI+A)\) in the numerator of PR7 and cancels exactly. It includes every zero direction of \(K\cap\ker T\), since those are in \(\mathcal H_{\rm inv}\). The invariant space and its energy are retained explicitly; they have zero residue in RM11. The cancellation therefore has a proved map and a precise mathematical reason.

The remaining determinant identity is

\[
 \det\mathscr Y(z)=
 z^n\frac{\det(zI+A_{\rm mem})}
 {\det\begin{pmatrix}zI+B&C_{\rm mem}^*\\C_{\rm mem}&zI+A_{\rm mem}\end{pmatrix}}.
 \tag{RM17}
\]

It is the PR determinant formula with all unobserved reducing factors canceled by exact equality, not by an asymptotic allocation.

## RM8. Application to the original mixed arithmetic family

For each original \(N\in\{q-1,q,2q-1,2q\}\), use \(T=T_k=D_k(M)\), the unchanged \(G_N,\Lambda,I_K\), and \(m=8k-16\). Then RM4 is the explicit original-metric matrix

\[
 D_N(z)=L_N^*T_k^*G_NT_kI_K
 (zH_{K,N}+H_{TK,N})^{-1}
 I_K^*T_k^*G_NT_kL_N.
 \tag{RM18}
\]

The received PR19 gives \(H_{TK,N}=J^*\mathfrak G_NJ\) with the fixed exact map \(J=V_O^{-1}\pi_\partial I_K\); this is also the image map proved in the full-word calculation. Substituting that image Gram in RM18 leaves the complete original \(H_{K,N}\) and both complex cross blocks. The positive word spectrum alone does not determine RM18, whereas the full measured family determines it by RM8–RM9.

The finite sign and deep-regularizer results PR25–PR31 are preserved at their stated analytic input status. RM18 neither replaces their native kernel coefficient nor derives a sign of a different complex current. It supplies the exact matrix object that carries the mixed kernel/observation coupling, and RM12–RM14 give a concrete finite construction and rank test for all of its contributing directions. These are the next matrices to evaluate with the complete-row sampling bounds; a determinant bound on them does not erase the off-diagonal terms.


## RM9. Coherent error in the original full source metric

Keep exactly the same linear maps \(T,\Lambda,I_K\). Let \(G\) and \(\widetilde G\) be two positive Hermitian forms on that same original space, and let positive numbers \(\alpha\le\beta\) satisfy
\[
 \alpha G\preceq\widetilde G\preceq\beta G,\qquad \kappa=\beta/\alpha.
\]
Every object bearing a tilde is recomputed from that full form by RM1–7; in particular its minimum section is recomputed, rather than held fixed when its defining metric changes. Write \(\Delta=\operatorname{rank}T\), \(p=\operatorname{rank}(T I_K)\), and let \(\lambda_1,\ldots,\lambda_\Delta>0\) be the positive eigenvalues of \(G^{-1}T^*GT\), in decreasing order. Let \(a_1,\ldots,a_p>0\) be the positive generalized eigenvalues of \((I_K^*T^*GTI_K,I_K^*GI_K)\). The remaining eigenvalues in both lists are exactly zero and their multiplicities depend only on the fixed maps.

For every vector \(x\ne0\), the two Rayleigh quotients of the full positive energy satisfy
\[
 \kappa^{-1}\frac{\|Tx\|_G^2}{\|x\|_G^2}
 \le\frac{\|Tx\|_{\widetilde G}^2}{\|x\|_{\widetilde G}^2}
 \le\kappa\frac{\|Tx\|_G^2}{\|x\|_G^2}.
\]
The identical proof for \(x=I_Kb\) applies on the complete kernel. The min–max formula now gives, in the same ordering,
\[
 \kappa^{-1}\lambda_j\le\widetilde\lambda_j\le\kappa\lambda_j,
 \qquad \kappa^{-1}a_j\le\widetilde a_j\le\kappa a_j.
 \tag{RM19}
\]
For clarity, this use of min–max is finite: choose an orthonormal eigenbasis for either Hermitian representative, express a vector's quotient as its eigenvalue-weighted squared coordinates, and maximize the minimum over subspaces of prescribed dimension. Intersection with the span of the smaller eigenvectors proves the upper bound, while the span of the larger eigenvectors attains equality. This argument permits repeated eigenvalues. Applying the pointwise quotient comparison on every such subspace proves RM19.

The original block determinant in RM7, before any reducing-factor cancellation, is
\[
 \det\mathscr Y_G(z)=z^{\Delta-p}
 \frac{\prod_{j=1}^{p}(z+a_j)}{\prod_{j=1}^{\Delta}(z+\lambda_j)}.
\]
Indeed its numerator is \(z^n\det(zI_m+A)\), its denominator is \(\det(zI_q+H)\), and \(n=q-m\); the zero multiplicities therefore give \(z^{n+m-p-(q-\Delta)}=z^{\Delta-p}\). The identical power occurs for \(\widetilde G\). By RM19, each remaining positive factor changes by a ratio in \([\kappa^{-1},\kappa]\) for every \(z>0\). Thus
\[
 \boxed{\left|\log\det\mathscr Y_{\widetilde G}(z)
       -\log\det\mathscr Y_G(z)\right|
 \le(\Delta+p)\log\kappa.}
 \tag{RM20}
\]
This bound is uniform in the regularizer, including values smaller than every positive energy. It counts the actual nonzero energies and keeps all exact zero factors before canceling them. It also includes the metric-induced change of the original section, since both determinants were derived with their own RM1 section.

For the programme word, \(\Delta=16k-48\), \(p=m=8k-16\), by its proved trivial intersection \(K\cap\ker T_k=0\). Apply RM20 separately to its four original full forms, using their own positive enclosures \(\alpha_N,\beta_N\), at any chosen positive parameters \(z_N\). The exact four-sign difference is bounded by
\[
 \boxed{\left|\mathcal R\log\det\mathscr Y_{\widetilde G_N}(z_N)
       -\mathcal R\log\det\mathscr Y_{G_N}(z_N)\right|
 \le(24k-64)\sum_{N\in\{q-1,q,2q-1,2q\}}
                 \log(\beta_N/\alpha_N).}
 \tag{RM21}
\]
The sum is over four cutoffs, with the return signs \(+,+,-,-\) unchanged in the left side. A fixed enclosure ratio costs \(O(k)=o(kq)\). More generally the bound is \(o(kq)\) whenever the displayed sum divided by \(q\) tends to zero. This is an error theorem for the complete form and its actual maps; the CS20–23 enclosure of a particular row covariance must still be transported by its exact defining maps before it can serve as a full-form enclosure. In both constructions the common operation is congruence followed by a full minimum and inverse. RM19–21 prove this operation for the measured resolvent itself, including its moving section. No native coefficient is inferred from an enclosure width.

## RM10. An exact illustration of the phase-bearing correction

Take the finite auxiliary example
\[
 G=I_3,\quad T=\operatorname{diag}(0,2,3i),\quad
 \Lambda=\begin{pmatrix}-1&1&0\\-i&0&1\end{pmatrix},\quad
 I_K=(1,1,i)^{\mathsf T}.
\]
Direct substitution in RM1–4 gives
\[
 Q=\frac13\begin{pmatrix}2&i\\-i&2\end{pmatrix},\quad
 L=\frac13\begin{pmatrix}-1&i\\2&i\\-i&2\end{pmatrix},\quad
 H_K=3,\quad E_{KK}=13,\quad X=\frac13(-1,-14i),
\]
\[
 E_{BB}=\frac19\begin{pmatrix}25&26i\\-26i&40\end{pmatrix},\quad
 D(z)=\frac1{9(3z+13)}\begin{pmatrix}1&14i\\-14i&196\end{pmatrix}.
\]
Thus the memory has one positive pole energy \(13/3\), its contributing kernel dimension is exactly one, and its complex off-diagonal entry is nonzero. The actual measured determinant and the two possible early compressions are
\[
 \det\mathscr Y(z)=\frac{z(3z+13)}{3(z+4)(z+9)},\quad
 \det Y_{\rm energy}(z)=\frac{3z^2}{3z^2+26z+36},\quad
 \det Y_{\rm arithmetic}(z)=\frac{9z^2}{9z^2+52z+36}.
\]
Here the second uses the positive energy compression \(Q^{-1}E_{BB}\), while the third uses the square of the actual compressed word \(T_{BB}=\Lambda TL\) in its original metric \(Q\). The first difference is nonnegative by RM15. For the last comparison, exact subtraction gives
\[
 \boxed{\det\mathscr Y(z)-\det Y_{\rm arithmetic}(z)
 =\frac{-2z(39z^2+94z-234)}{3(z+4)(z+9)(9z^2+52z+36)}.}
 \tag{RM22}
\]
All denominator factors are positive for \(z>0\). The difference is positive below \((\sqrt{11335}-47)/39\), zero there, and negative above it. Thus its sign change is calculated on the same original maps. RM4 and RM16 provide the exact connecting correction in both cases. This example illustrates those identities; it is not a sampled native period or a claim about its current sign.

## RM11. A complete complex-response error in the original value frame

The same coherent source comparison also controls every complex matrix entry of the measured action. Take \((1-\varepsilon)G\preceq\widetilde G\preceq(1+\varepsilon)G\), \(0\le\varepsilon<1\), with the same original maps. Define the two complete compressed inverse forms
\[
 \Sigma_z=\Lambda(zG+T^*GT)^{-1}\Lambda^*,\qquad
 \Sigma_0=\Lambda G^{-1}\Lambda^*=Q^{-1},
\]
and define their tilded versions by the same expressions. The exact original-frame identity is \(\mathscr Y=z\Sigma_z\Sigma_0^{-1}\). It follows directly from \((zI+G^{-1}T^*GT)^{-1}G^{-1}=(zG+T^*GT)^{-1}\), so this expression retains the changed minimum section automatically.

Congruence by \(T\), addition of \(zG\), inverse order and congruence by \(\Lambda\) prove
\[
 \frac{\Sigma_j}{1+\varepsilon}\preceq\widetilde\Sigma_j
 \preceq\frac{\Sigma_j}{1-\varepsilon},\qquad j\in\{0,z\}.
\]
Put \(Y=Q^{1/2}\mathscr YQ^{-1/2}\), \(A=zQ^{1/2}\widetilde\Sigma_zQ^{1/2}\), and \(S=Q^{1/2}\widetilde\Sigma_0Q^{1/2}\). Then \(0\prec Y\preceq I\), \(\|A-Y\|\le\varepsilon\|Y\|/(1-\varepsilon)\), \(\|S^{-1}\|\le1+\varepsilon\), and \(\|S^{-1}-I\|\le\varepsilon\). These follow from the displayed form inequalities and their inverse; no separately chosen square-root coordinate frame is compared. The actual tilded action expressed in this same original value frame is \(Q^{1/2}\widetilde{\mathscr Y}Q^{-1/2}=AS^{-1}\). Therefore
\[
 \boxed{\left\|Q^{1/2}(\widetilde{\mathscr Y}(z)-\mathscr Y(z))Q^{-1/2}\right\|
 \le\frac{2\varepsilon}{1-\varepsilon}\,
       \left\|Q^{1/2}\mathscr Y(z)Q^{-1/2}\right\|
 \le\frac{2\varepsilon}{1-\varepsilon}.}
 \tag{RM23}
\]
Indeed subtract \(Y\) from \(AS^{-1}\) as \((A-Y)S^{-1}+Y(S^{-1}-I)\), take operator norms and add the two exact bounds. For any original observed vectors \(u,v\), Cauchy–Schwarz now gives
\[
 |u^*Q(\widetilde{\mathscr Y}-\mathscr Y)v|
 \le\frac{2\varepsilon}{1-\varepsilon}\|Y\|\,\|u\|_Q\|v\|_Q.
\]
This is an absolute complex-response error, with real and imaginary parts both retained. It is uniform over all positive regularizers. It does not determine the sign of a response whose actual value has not been evaluated; it gives the exact original-metric error to be paid when that value is computed. RM20 separately gives the stronger nonzero-rank determinant bound, so the phase estimate is not used to charge a full ambient rank to the determinant.

## Proof and source coverage

The received `COMPLETE_PROOFS (5).md`, SHA-256 `1e042cf77ef8df20bcb3167d38d5a98e9f653b6a2a1694a16e6c2728b7de96ab`, PR1–44 was read completely. The matching resolvent paste was read completely. The derivation above proves RM1–23 in full finite dimension independently of the incoming numerical receipt. Its checker tests the complete original coordinates, nonidentity complex metrics, nonnormal words, kernel intersections, both signs of the arithmetic-compression defect, and the minimal memory moment rank. Native asymptotic coefficients are not outputs of these auxiliary checks.

The exact programme specialization is [FW1–10 and FW39–49](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9b7b0bad40b33dc88bba7d8cb1548da1fadbb585/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/WORD_PROOFS.md), retaining its full original root polynomial, source metric and complete observation. The finite source receiver is [FI1–17, FR1–4](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/FINITE_INVARIANT_PROOFS.md). Their entire proofs accompany this edition.
