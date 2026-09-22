# Finite matrix recovery and the original zero-frequency angle spectrum

This proof starts with the complete original observation and metric. The incoming anchored construction is proved in MR1–8. MR9–13 identify its recovered zero-frequency matrix directly with every primary angle, including intersections, zero directions and unit directions. MR14–17 give finite error and original determinant receivers. Finite recoverability does not assign the unevaluated original period values.

The predecessor is [RM1–23, exact kernel memory](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/ORIGINAL_RESOLVENT_MEMORY_PROOFS.md). Its Schur construction is related to the Feshbach–Schur map of Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, [arXiv:2105.02058v1](https://arxiv.org/abs/2105.02058v1), Theorem1.2. The data factorization below is the Loewner realization method of A. J. Mayo and A. C. Antoulas, [2007, DOI10.1016/j.laa.2007.03.008](https://doi.org/10.1016/j.laa.2007.03.008), in the factorized form proved by Qiang Zhang, Ion Victor Gosea and Athanasios C. Antoulas, [arXiv:2103.09674v1, Lemma2.1](https://arxiv.org/abs/2103.09674v1). The latter original TeX, lines169–328, was read. Mayo–Antoulas is historical attribution; no original-TeX reading of that article is asserted. The finite original-metric proof is complete below.

## MR1. Original spaces, sections and energy

Let \(E=\mathbb C^q\), \(G=G^*>0\), and let the fixed observation \(\Lambda:E\to B=\mathbb C^n\) be onto. Set \(K=\ker\Lambda\), \(m=q-n\), and retain its full column frame \(I_K:\mathbb C^m\to E\). Define
\[
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad
 L=G^{-1}\Lambda^*Q,\quad H_K=I_K^*GI_K,\quad
 J_K=I_KH_K^{-1/2}.
\tag{MR1}
\]
Then \(\Lambda L=I\), \(L^*GL=Q\), \(L^*GJ_K=0\), and \(J_K^*GJ_K=I_m\), by multiplication. Thus
\(U=[L,J_K]\) is an invertible map from \(B\oplus\mathbb C^m\), carrying the metric \(\operatorname{diag}(Q,I)\) exactly to \(G\). These formulas preserve both original metrics rather than assigning Euclidean lengths to \(B\).

For the fixed word \(T:E\to E\), let \(H=G^{-1}T^*GT\), \(V=\ker T\), \(d=\dim V\), and \(\Delta=q-d\). Initially suppose \(K\cap V=0\); MR11 includes intersections. Choose a physical energy scale \(R\ge\|H\|_G>0\), and put
\[
 A=R^{-1}J_K^*T^*GTJ_K,\quad
 C=R^{-1}J_K^*T^*GTL,\quad
 B_0=R^{-1}L^*T^*GTL.
\tag{MR2}
\]
The matrix \(A\) is positive definite: its quadratic form is \(R^{-1}\|TJ_Kx\|_G^2\), and its kernel is the stated intersection. The whole energy form in \(U\) is
\(\left(\begin{smallmatrix}B_0&C^*\\ C&A\end{smallmatrix}\right)\).
Write
\(\mathscr Y(z)=\Lambda z(zI+H)^{-1}L\).

## MR2. The anchored original measured response

Block elimination in \(U\), keeping the metric in MR1, gives for \(x>0\)
\[
 \mathscr Y(Rx)=x[xQ+B_0-C^*(xI+A)^{-1}C]^{-1}Q.
\tag{MR3}
\]
Indeed the top-left block of \((xU^*GU+U^*GHU/R)^{-1}\) is the displayed Schur inverse; multiplication by \(xQ\) on the right produces MR3. Define, in the original observation coordinates,
\[
 Z(x)=xQ(\mathscr Y(Rx)^{-1}-I)
     =B_0-C^*(xI+A)^{-1}C.
\tag{MR4}
\]
Subtract at \(x=1\), using the resolvent identity, and set
\[
 C_1=(I+A)^{-1/2}C,\qquad
 F(x)=\frac{Z(x)-Z(1)}{x-1}
     =C_1^*(xI+A)^{-1}C_1 .
\tag{MR5}
\]
The formula at1 is its derivative value, but the sampling scheme never asks for it.

Let \(\mathcal M=\operatorname{span}\{A^jCb:0\le j<m,b\in B\}\), \(s=\dim\mathcal M\).
By Cayley–Hamilton this space is \(A\)-invariant, hence reducing because \(A=A^*\). Functional calculus and invertibility of \((I+A)^{1/2}\) on each eigenspace prove that \(C_1\) generates exactly the same space.

## MR3. Complete finite rank, including repeated poles

When \(m>0\), use \(m\) nodes \(x_i=2+(i-1)/m\), and \(m\) nodes \(y_j=4+(j-1)/m\), together with the anchor1. Let
\[
 \mathcal L_{ij}=\frac{F(x_i)-F(y_j)}{y_j-x_i},\qquad
 \mathcal S_{ij}=\frac{y_jF(y_j)-x_iF(x_i)}{y_j-x_i}.
\tag{MR6}
\]
With \(X=[(A+x_iI)^{-1}C_1]_i\) and \(Y=[(A+y_jI)^{-1}C_1]_j\), direct subtraction gives
\(\mathcal L=X^*Y\), \(\mathcal S=X^*AY\).

Both \(X\) and \(Y\) have range \(\mathcal M\). For proof, put \(p(t)=\prod_i(t+x_i)\). The polynomials \(p(t)/(t+x_i)\) form a basis of polynomials of degree at most \(m-1\): evaluation at \(-x_j\) proves independence. Multiplication by \(p(A)^{-1}\), invertible on the whole kernel, carries their span applied to \(C_1\) onto \(\mathcal M\). This is exactly the range of \(X\). The proof for \(Y\) is identical. It never requires distinct eigenvalues of \(A\).

Since \(X^*:\mathcal M\to B^m\) is injective and \(Y:B^m\to\mathcal M\) is onto, \(\operatorname{rank}\mathcal L=s\). This proves the actual memory rank from the finite data.

## MR4. Recovery through an actual nonzero minor

Choose row and column indices \(I,J\) giving an invertible \(s\)-square minor \(\mathcal L_0\), and take the same minor \(\mathcal S_0\). Let \(X_0,Y_0:\mathbb C^s\to\mathcal M\) be the selected columns of \(X,Y\). They are invertible onto \(\mathcal M\), since \(X_0^*Y_0=\mathcal L_0\). Set
\[
 B_L=[F(x_i)]_{\text{selected rows}},\qquad
 B_R=[F(y_j)]_{\text{selected columns}}.
\]
Then \(B_L=X_0^*C_1\), \(B_R=C_1^*Y_0\), and
\[
 F(z)=B_R(\mathcal S_0+z\mathcal L_0)^{-1}B_L,\quad
 \mathcal L_0^{-1}\mathcal S_0=Y_0^{-1}A_{\mathcal M}Y_0 .
\tag{MR7}
\]
Cancel the invertible factors \(X_0^*,Y_0\) to verify both equalities. The metric of the latter representation is \(Y_0^*Y_0\), which is retained; the matrix is not assigned Euclidean selfadjointness. For \(s=0\), \(C=0\), \(F=0\), and all subsequent empty determinants are1. The case \(m=0\) requires only \(Z(1)\).

Thus \(2m+1\) original matrix values suffice. This is a count of matrices, with exact entries; neither a bit-complexity estimate nor a value of the native period is implied.

## MR5. Two recovered zero coefficients

Differentiate MR7 algebraically:
\[
 F_0=B_R\mathcal S_0^{-1}B_L,\qquad
 F'_0=-B_R\mathcal S_0^{-1}\mathcal L_0\mathcal S_0^{-1}B_L.
\]
The recovered forms are
\[
 E_0=Z(1)-F_0=B_0-C^*A^{-1}C,\qquad
 W_0=F_0-F'_0=C^*A^{-2}C.
\tag{MR8}
\]
To check the second equality on an eigenvalue \(a>0\), use
\((a^{-1}+a^{-2})/(1+a)=a^{-2}\).
For the first, use \(1/(1+a)+1/(a(1+a))=1/a\).
The form \(E_0\) is the complete Schur minimum of the original energy and is positive semidefinite. The form \(W_0\) is the mass of the actual kernel graph; it has rank at most \(s\).

## MR6. Original zero space and its metric

The zero space in \(U\) consists exactly of
\[
 U\binom{b}{-A^{-1}Cb},\qquad b\in\ker E_0.
\tag{MR9}
\]
This follows by completing the whole energy square:
\[
 b^*E_0b+(a+A^{-1}Cb)^*A(a+A^{-1}Cb).
\]
If \(Z_0\) is any full frame for \(\ker E_0\), the actual Gram of this graph is
\[
 H_V=Z_0^*(Q+W_0)Z_0 .
\tag{MR10}
\]
In particular \(\dim\ker E_0=d\). No coordinate volume in \(Z_0\) has been discarded.

## MR7. The zero-frequency matrix itself is recovered

The spectral theorem in the \(G\) metric gives
\[
 Y_*=\lim_{z\downarrow0}\mathscr Y(z)=\Lambda P_V^G L .
\tag{MR11}
\]
Projection onto the graph MR9, using MR10, gives the explicit finite reconstruction
\[
 \boxed{Y_*=Z_0[Z_0^*(Q+W_0)Z_0]^{-1}Z_0^*Q.}
\tag{MR12}
\]
Indeed the graph frame is \(V_0=U[Z_0;-A^{-1}CZ_0]\); its observation is \(Z_0\), its adjoint against \(GL\) is \(Z_0^*Q\), and
\(P_V^G=V_0(V_0^*GV_0)^{-1}V_0^*G\).
If \(d=0\), the frame is empty and \(Y_*=0\). All matrices in MR12 are constructed from MR4–8 and the original \(Q\).

## MR8. Invisible memory and full original volume

For \(w\in\mathcal M^\perp\), \(C^*w=0\), and \(A\) preserves \(\mathcal M^\perp\). Hence the subspace \(J_K\mathcal M^\perp\) is reducing for \(H\). It is positive and perpendicular to \(V\). Its primary-angle matrix is the identity. Its original kernel-coordinate Gram need not be the identity: \(J_K=I_KH_K^{-1/2}\) is the specified metric isometry, not a change to the fixed volume frame. Thus invisible memory cancels only unit angle factors; MR17 below retains \(H_K\).

## MR9. Full spectral morphism at zero frequency

This argument no longer requires \(K\cap V=0\). Define the primary matrix
\[
 \Gamma_K=J_K^*GP_{V^{\perp_G}}^GJ_K,\qquad
 J_B=LQ^{-1/2},\qquad
 \overline Y_*=Q^{1/2}Y_*Q^{-1/2}=J_B^*GP_V^GJ_B .
\tag{MR13}
\]
Both \(J_B,J_K\) are isometries, and their images are orthogonal complements in \(E\). Let \(J_V\) be a \(G\)-isometry from \(\mathbb C^d\) onto \(V\), and write
\(A_V=J_K^*GJ_V\), \(B_V=J_B^*GJ_V\).
Orthogonal resolution gives \(A_V^*A_V+B_V^*B_V=I_d\), while
\(\Gamma_K=I_m-A_VA_V^*\) and \(\overline Y_*=B_VB_V^*\).
Sylvester's determinant identity, itself obtained by eliminating the two blocks of \(\left(\begin{smallmatrix}I&X\\Y&I\end{smallmatrix}\right)\), yields the polynomial identity
\[
 \boxed{(1-u)^m\det(I_n-u\overline Y_*)
       =(1-u)^d\det(I_m-u\Gamma_K).}
\tag{MR14}
\]
For \(u\ne1\), replace \(B_V^*B_V\) by \(I_d-A_V^*A_V\) and apply that identity; multiplying clears every negative exponent. Polynomial equality then holds also at1. All eigenvalues in \((0,1)\) agree with complete multiplicities.

Here is the exact eigenvector map. For \(\Gamma_Kx=\gamma x\), \(0<\gamma<1\), put \(a=J_Kx\) and
\[
 b=P_{K^{\perp_G}}^G P_V^G a,\qquad
 \Psi_\gamma x=\frac{J_B^*Gb}{\sqrt{\gamma(1-\gamma)}}.
\tag{MR15}
\]
Since \(P_KP_Va=(1-\gamma)a\) and \(P_V^2=P_V\), one has
\(P_BP_Vb=\gamma b\) and \(\|b\|_G^2=\gamma(1-\gamma)\|x\|^2\).
Therefore \(\Psi_\gamma\) is an isometry onto the \(\gamma\) eigenspace of \(\overline Y_*\); the reverse construction or the equal multiplicity in MR14 proves surjectivity. This supplies the actual map, including complex phases.

## MR10. Zero, unit and positive determinants

Put \(t=\dim(K\cap V)\), \(a=\dim(K\cap V^{\perp_G})\), and \(b=\dim(K^{\perp_G}\cap V)\). Directly from the quadratic projection forms:
\[
 \operatorname{null}\Gamma_K=t,\quad
 \operatorname{mult}_1\Gamma_K=a,\quad
 \operatorname{rank}Y_*=d-t,\quad
 \operatorname{mult}_1Y_*=b.
\tag{MR16}
\]
The rank statement follows because \(P_B|_V\) has kernel \(K\cap V\); the compression is its product with its adjoint. The common count of eigenvalues strictly between0 and1 is
\(h=m-t-a=d-t-b\), so \(b-a=d-m\). Consequently
\[
 \boxed{\det\nolimits_+\Gamma_K=\det\nolimits_+Y_* .}
\tag{MR17}
\]
The positive determinant is the product of positive eigenvalues; its empty value is1. Zero-angle multiplicity is not hidden in this convention: it is exactly \(t\) and must be reported with it. In the original transverse programme \(t=0\), so the left side is the ordinary primary determinant.

## MR11. Intersections in finite recovery

Let \(K_0=K\cap V\). In the metric coordinates MR1, \(A\) is positive semidefinite and its zero space corresponds exactly to \(K_0\). Positivity of the whole energy forces \(C^*|_{\ker A}=0\): the quadratic polynomial in a scalar multiple of a zero vector has nonnegative values for every complex scalar only if its linear cross coefficient vanishes. Thus the memory is entirely in \((\ker A)^\perp\). Restrict there, with \(p=m-t\), and replace \(A^{-1}\) by the positive-range inverse \(A^+\).

MR2–8 remain valid with at most \(2p+1\) samples if \(p\) is known; the \(2m+1\) scheme still works without reducing the count. The recovered graph is \(V\ominus_G K_0\); the missing zero space \(K_0\) is perpendicular to \(L(B)\), hence contributes zero to \(Y_*\). MR12 therefore still recovers exactly the same \(Y_*\), and MR16–17 include all original zero angles.

## MR12. Quantitative spectral approach to the recovered endpoint

Retain any proved positive spectral interval
\(\ell P_{V^\perp}\preceq_G H\preceq_G uP_{V^\perp}\).
For \(z>0\), put \(\tau_a=z/(z+a)\). Spectral calculus, followed by the actual isometry \(J_B\), proves
\[
 \boxed{\overline Y_*+\tau_u(I-\overline Y_*)
 \preceq Q^{1/2}\mathscr Y(z)Q^{-1/2}
 \preceq\overline Y_*+\tau_\ell(I-\overline Y_*).}
\tag{MR18}
\]
Let \(\beta_i(z)\) and \(y_i\) denote the decreasing ordered eigenvalues of the middle matrix and \(\overline Y_*\). Min–max gives the explicit enclosure
\[
 \max\left(0,\frac{\beta_i(z)-\tau_\ell}{1-\tau_\ell}\right)
 \le y_i\le
 \min\left(1,\frac{\beta_i(z)-\tau_u}{1-\tau_u}\right).
\tag{MR19}
\]
There is no assertion that coarse moderate-frequency data resolve arbitrarily small \(y_i\). Formula MR19 measures exactly how the gap and the actual response enter that question.

## MR13. A finite positive-determinant certificate

Suppose a Hermitian approximation \(\widehat Y_*\) to \(\overline Y_*\) has operator error at most \(e\). Its known positive rank is \(r=d-t\). If the \(r\)-th decreasing eigenvalue \(\widehat y_r>e\), min–max gives
\[
 -\sum_{i=1}^r\log\min(1,\widehat y_i+e)
 \le-\log\det\nolimits_+\Gamma_K
 \le-\sum_{i=1}^r\log(\widehat y_i-e).
\tag{MR20}
\]
Only the known positive indices enter. Every logarithm has a strictly positive argument under the displayed guard. This certificate is for independent endpoint error; complete-source bounds in MR16 have a different, stronger error structure.

## MR14. Independent rounding in the anchored reconstruction

Use one fixed \(Q\)-isometry for error measurement. In those coordinates \(Q=I\) as a proved congruence, and \(x/(x+1)I\preceq\mathscr Y(Rx)\preceq I\). Suppose every original sample has error \(\eta\le1/4\), and all nonlinear operations below use the stated error intervals. Since \(\|Y^{-1}\|\le2\), the resolvent inverse identity gives error at most \(8\eta\) in each inverse. Therefore \(\|\delta Z(1)\|\le8\eta\), and on \(2\le x\le5\),
\[
 \|\delta F(x)\|\le 8\eta(x+1)/(x-1)\le24\eta.
\]
Every chosen scalar \(s\)-square minor consequently has
\[
 e_L=48s\eta,\quad e_S=192s\eta,\quad
 e_{B_L}=e_{B_R}=24\sqrt s\,\eta.
\tag{MR21}
\]
The separation \(y_j-x_i>1\) proves the first two bounds by entrywise estimates followed by Frobenius norm. The last two follow by stacking selected rows or columns.

Take actual upper bounds \(v\ge\|\mathcal S_0^{-1}\|\), \(l\ge\|\mathcal L_0\|\), \(b_L\ge\|B_L\|\), \(b_R\ge\|B_R\|\). Under \(ve_S<1\), set \(v'=v/(1-ve_S)\) and
\[
 e_0=(b_R+e_{B_R})v'(b_L+e_{B_L})-b_Rvb_L,
\]
\[
 e_1=(b_R+e_{B_R})(v')^2(l+e_L)(b_L+e_{B_L})
       -b_Rv^2lb_L.
\tag{MR22}
\]
Expanding the product differences and using
\(\|\delta(\mathcal S_0^{-1})\|\le v'-v\)
proves \(\|\delta F_0\|\le e_0\), \(\|\delta F'_0\|\le e_1\). Hence
\(e_E=8\eta+e_0\), \(e_W=e_0+e_1\) bound MR8. Taking Hermitian parts does not increase these errors.

## MR15. The energy gap gives the required kernel projector guard

In \(Q\)-isometric coordinates, the Schur form \(E_0\) is bounded by
\[
 (\ell/R)P_{(K+V)^\perp}\preceq E_0
 \preceq (u/R)P_{(K+V)^\perp}.
\tag{MR23}
\]
Here the projector is expressed in \(K^\perp\) via \(J_B\). To prove this, the Schur form of a vector \(b\) is the minimum of \(\langle H(b+a),b+a\rangle_G/R\) over \(a\in K\). Replace \(H\) by its lower or upper multiple of \(P_{V^\perp}\). The remaining minimum is \(\operatorname{dist}_G(b,K+V)^2\), proving MR23. Thus every positive eigenvalue of \(E_0\) is at least \(g_0=\ell/R\), without an extra angle factor.

Hermitian \(\widehat E_0\) with \(e_E<g_0/2\) has exactly the known number of zero-cluster eigenvalues in \([-e_E,e_E]\); the others are at least \(g_0-e_E\). Let \(\widehat P_0\) be the projector onto this cluster and \(P_0=\operatorname{proj}\ker E_0\). Then
\(\|\widehat P_0-P_0\|\le2e_E/g_0\).
For completeness, the off-diagonal block between \(\ker E_0\) and the complementary \(\widehat E_0\)-space solves a Sylvester equation whose spectra are separated by \(g_0-e_E\). Its inverse has norm at most \(1/(g_0-e_E)\), by the integral \(\int_0^\infty e^{-t\widehat E_{\rm high}}(\cdot)\,dt\). Multiplication by the perturbation gives the bound \(e_E/(g_0-e_E)\le2e_E/g_0\). Equal ranks identify this norm with the projector difference.

If \(M_W\ge\|W_0\|\), then
\[
 e_{\rm ang}=e_W+4M_We_E/g_0
\tag{MR24}
\]
bounds the difference between \(I+P_0W_0P_0\) and its hatted counterpart. The true determinant is \((\det_+\Gamma_K)^{-1}\): restrict to \(\ker E_0\) in MR10–12, or use Sylvester's identity. The true matrix is at least \(I\). Before taking Hermitian parts the reconstructed \(W_0\) has rank at most \(s\), afterward at most \(2s\); the difference of the two projected products has rank at most \(3s\). Thus, under \(e_{\rm ang}<1\),
\[
 |\widehat{\mathcal J}-(-\log\det\nolimits_+\Gamma_K)|
 \le-\min(n,3s)\log(1-e_{\rm ang}).
\tag{MR25}
\]
Indeed relative congruence by the true inverse square root puts every eigenvalue in \([1-e_{\rm ang},1+e_{\rm ang}]\), with at most \(\min(n,3s)\) eigenvalues different from1. Summing their logarithms proves the claim.

## MR16. Complete-source error has a rank cost

For fixed \(T,\Lambda,I_K\) and \(\alpha G\preceq\widetilde G\preceq\beta G\), let \(\kappa=\beta/\alpha\). The numerator form of every primary angle is
\(\inf_{v\in V}\|I_Kx-v\|_G^2\); its denominator is \(\|I_Kx\|_G^2\). Both have the same complete-source enclosure. On the fixed quotient by \(K\cap V\), min–max gives
\[
 \kappa^{-1}\gamma_j(G)\le\gamma_j(\widetilde G)\le\kappa\gamma_j(G).
\tag{MR26}
\]
Consequently the positive determinant logarithms differ by at most \((m-t)\log\kappa\). Both minimum sections and both projections are recomputed from their actual metrics. This estimate is not a statement about independent sample perturbations.

## MR17. Return to the original four determinants

On the transverse programme stratum \(T=D_k(M)\), the original primary quotient \(\pi_\partial\) has kernel \(V\). Its attained metric and restriction are
\[
 G_N^\partial=(\pi_\partial G_N^{-1}\pi_\partial^*)^{-1},\qquad
 B_{K,N}=(\pi_\partial I_K)^*G_N^\partial(\pi_\partial I_K).
\]
By the quotient minimum, \(B_{K,N}=I_K^*G_NP_{V^{\perp_{G_N}}}I_K\). Therefore MR17 proves the absolute identity
\[
 \boxed{\log\det H_{K,N}
 =\log\det B_{K,N}-\log\det\nolimits_+Y_{*,N}.}
\tag{MR27}
\]
All constant coordinate determinants stay in both sides. Write
\(\mathcal R f_N=f_{q-1}+f_q-f_{2q-1}-f_{2q}\)
and \(\mathcal J_N=-\log\det_+Y_{*,N}\).
The retained boundary-width result [AS, original angle proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9b7b0bad40b33dc88bba7d8cb1548da1fadbb585/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/ANGLE_PROOFS.md) supplies
\(a_kI\preceq G_N^\partial\preceq b_kI\), \(\omega_k=\log(b_k/a_k)=O(k\log q)\), with decreasing cutoff metrics. Hence
\[
 \boxed{0\le\mathcal K_k-\mathcal R\mathcal J_N
 \le2m\omega_k=o(kq).}
\tag{MR28}
\]
Proof: congruence by the same \(\pi_\partial I_K\) preserves the finite width; decreasing metrics make each low-minus-high log determinant nonnegative, and each is at most \(m\omega_k\). There are two such pairs.

Combining MR28 with the exact [RG50–54 finite invariant receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/GROWTH_PROOFS.md), whose finite bound is
\(|\mathcal K_k-\log\mathcal A_k+G_0+G_1|\le\mathcal E_k\),
gives
\[
 -\mathcal E_k\le
 \log\mathcal A_k-G_0-G_1-\mathcal R\mathcal J_N
 \le\mathcal E_k+2m\omega_k.
\tag{MR29}
\]
Thus the scalar invariant-row return and the full matrix endpoint are joined by a proved directed bound, without identifying their differently ranked angle matrices.

## MR18. Exact complex replay

Take \(G=I_4\), \(\Lambda=(I_2,0)\),
\[
 T=\begin{pmatrix}1&i&1&0\\0&1/\sqrt2&0&\sqrt2\\0&0&0&0\\0&0&0&0\end{pmatrix}.
\]
Its positive energies are2 and7/2; \(R=4\) is allowed. Put
\(C_*=\left(\begin{smallmatrix}1&i\\0&1\end{smallmatrix}\right)\).
The three original samples at \(x=1,2,4\) give
\[
 F(2)=C_*^*\operatorname{diag}(1/45,1/60)C_*,
 \quad F(4)=C_*^*\operatorname{diag}(1/85,1/108)C_*.
\]
Here one block minor already has full memory rank2, so three samples suffice. They yield
\[
 \mathcal L_0=C_*^*\operatorname{diag}(4/765,1/270)C_*,
 \quad\mathcal S_0=C_*^*\operatorname{diag}(1/765,1/540)C_*,
\]
\[
 E_0=0,\quad W_0=C_*^*\operatorname{diag}(1,1/4)C_*,
 \quad Y_*=(I+W_0)^{-1}
 =\begin{pmatrix}9/14&-2i/7\\2i/7&4/7\end{pmatrix}.
\]
Direct projection gives
\(\Gamma_K=\left(\begin{smallmatrix}5/14&-i/7\\i/7&6/7\end{smallmatrix}\right)\).
They are different coordinate matrices, related by MR15; both have determinant \(2/7\) and eigenvalues \((17\pm\sqrt{65})/28\). This tests the full complex reconstruction and spectral morphism. It is an auxiliary exact example, not evaluated original xi data.

## MR19. Precision is an actual mathematical datum

For fixed \(T=\operatorname{diag}(0,1)\), \(\Lambda=(-1,1)\), and
\(G_\varepsilon=\operatorname{diag}((1-\varepsilon)/\varepsilon,1)\),
direct inversion gives \(Q=1-\varepsilon\),
\(\mathscr Y_\varepsilon(z)=(z+\varepsilon)/(z+1)\),
\(Y_*=\Gamma_K=\varepsilon\), and \(H_K=1/\varepsilon\).
If \(\varepsilon=2^{-L}\) and \(\varepsilon'=2^{-L-q}\), then on \([1,5]\) the response difference is at most \(2^{-L-1}\), whereas the primary determinant logarithms differ by \(q\log2\). Direct sums multiply this logarithmic difference by the kernel rank. The exact endpoint and finite recovery formulas retain that information, but recovering it from independently rounded samples requires corresponding precision. None of MR1–29 replaces it by a rank count.
