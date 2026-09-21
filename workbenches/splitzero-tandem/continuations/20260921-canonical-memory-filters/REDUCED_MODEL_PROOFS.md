# The full observed polynomial action: reduced resolvents, heat, and exact pole masses

This derivation proves the finite statements (33)–(46) in the received memory/filter continuation and extends the pole and energy-graph statements to every eigenvalue below the kernel block, with multiplicities retained. All adjoints, norms, projections and minima use the original metric. The source-family and canonical memory estimates are proved in the accompanying derivations.

## 1. Original spaces and the exact finite model

Fix an original cutoff. Let \((E,G)\) have dimension \(q\), let \(\Lambda:E\to B\) be the original onto observation, and put
\[
Q_B=(\Lambda G^{-1}\Lambda^*)^{-1},\qquad
L_B=G^{-1}\Lambda^*Q_B.
\tag{RM1}
\]
Then \(\Lambda L_B=I_B\), \(L_B^\dagger=\Lambda\), and \(L_B\) is an isometry. Indeed \(L_B^*GL_B=Q_B\); completing the quadratic minimum proves that this is the entire observed quotient metric. The projection onto \(K^\perp\), where \(K=\ker\Lambda\), is \(P_B=L_B\Lambda\).

For an admitted monic filter \(p\) of degree \(d\), retain
\[
X=p(M)^{-1}=B_p+U_pT_p,\quad
U_pa=[a/p],\quad T_p=\operatorname{rem}_pL_N,
\tag{RM2}
\]
where \(L_N\) is the original source-minimum section. The polynomial quotient identity proves RM2: if \(L_Nx=p\mathfrak Q_pL_Nx+\operatorname{rem}_pL_Nx\), then applying the original remainder map gives \(x=p(M)B_px+T_px\), and division by \(p(M)\) gives the result. Thus no independent compressed action is substituted.

Set
\[
H_p=U_p^*GU_p,\quad V=U_pH_p^{-1/2},\quad
F=U_pT_p,\quad
\mathsf K=H_p^{1/2}T_pG^{-1}T_p^*H_p^{1/2},
\tag{RM3}
\]
\[
Y=\Lambda V,\qquad \Theta=Y^\dagger Y
=H_p^{-1/2}U_p^*\Lambda^*Q_B\Lambda U_pH_p^{-1/2}.
\tag{RM4}
\]
These are exact operators on the coefficient space, equipped here with its stated Euclidean metric. The source and target changes in RM3–4 are isometries with their original metrics; no physical coordinate or source mass is changed. Direct multiplication proves
\[
V^\dagger V=I_d,\qquad FF^\dagger=V\mathsf KV^\dagger,
\qquad 0\preceq\Theta\preceq I_d.
\tag{RM5}
\]
The admitted rational-source estimate proves that \(T_p\) is onto and \(\Lambda U_p\) is injective on its displayed finite guards. Thus \(\mathsf K>0\) and \(\Theta>0\) there. Outside those guards all formulas containing their inverses have that explicit restriction; the covariance identities themselves do not require it.

Let
\[
\beta\ge\|B_p\|,\qquad \kappa_-=\lambda_{\min}\mathsf K,
\quad\kappa_+=\|\mathsf K\|,\qquad
\varepsilon_R=2\beta\sqrt{\kappa_+}+\beta^2.
\tag{RM6}
\]
Since \(\|F\|=\sqrt{\kappa_+}\), expansion of \(XX^\dagger\) proves
\[
\|XX^\dagger-FF^\dagger\|\le\varepsilon_R,
\qquad
\|XX^\dagger-FF^\dagger\|_{\rm HS}
\le2\beta\sqrt{\operatorname{Tr}\mathsf K}+\sqrt q\,\beta^2.
\tag{RM7}
\]
For the second bound use \(\|B_pF^\dagger\|_{\rm HS}\le\beta\|F\|_{\rm HS}\), its adjoint, and \(\|B_pB_p^\dagger\|_{\rm HS}\le\sqrt q\beta^2\). These steps retain both cross terms. The additional guard \(\kappa_->4\beta^2\) gives a separated cluster by singular-value min–max: the first \(d\) singular values of \(X\) are at least \(\sqrt{\kappa_-}-\beta>\beta\), and every remaining one is at most \(\beta\).

## 2. Complete resolvent and heat bounds

Put \(H=p(M)^\dagger p(M)>0\), so \(H^{-1}=XX^\dagger\). For positive semidefinite \(A,B\) and \(z\ge0\), multiplication of both sides gives the exact identity
\[
A(I+zA)^{-1}-B(I+zB)^{-1}
=(I+zA)^{-1}(A-B)(I+zB)^{-1}.
\tag{RM8}
\]
The two outside factors are contractions, even if \(A\) and \(B\) do not commute. Use \(A=XX^\dagger\), \(B=FF^\dagger\), and RM5. The function \(x/(1+zx)\) vanishes at zero, so functional calculus on \(\operatorname{im}V\) and its orthogonal complement gives
\[
\left\|\Lambda(zI+H)^{-1}L_B
-Y(\mathsf K^{-1}+zI_d)^{-1}Y^\dagger\right\|
\le\varepsilon_R\qquad(z\ge0).
\tag{RM9}
\]
The estimate at \(z=0\) is included. It is an absolute estimate with the displayed size, not an assertion that this size tends to zero without its late-scale comparison.

For \(\tau>0\) define \(f_\tau(0)=0\), \(f_\tau(x)=e^{-\tau/x}\) for \(x>0\). Its derivative is \(\tau x^{-2}e^{-\tau/x}\). With \(u=\tau/x\), maximizing \(u^2e^{-u}/\tau\) at \(u=2\) proves
\[
\sup_{x\ge0}|f_\tau'(x)|=\frac4{e^2\tau}.
\tag{RM10}
\]
Take orthonormal eigenbases \(u_i,v_j\) of \(A,B\). The \((i,j)\) matrix entries in these bases satisfy
\[
\langle u_i,(f_\tau(A)-f_\tau(B))v_j\rangle
=[f_\tau(a_i)-f_\tau(b_j)]\langle u_i,v_j\rangle,
\]
while the corresponding entry of \(A-B\) is \((a_i-b_j)\langle u_i,v_j\rangle\). Squaring, summing and applying RM10 proves the Hilbert–Schmidt estimate. Trace norm on \(E\) is at most \(\sqrt q\) times that norm. Compression by \(\Lambda=L_B^\dagger\) and \(L_B\) does not increase trace norm. Thus
\[
\begin{split}
\|\Lambda e^{-\tau H}L_B-Ye^{-\tau\mathsf K^{-1}}Y^\dagger\|_1
\le \varepsilon_H(\tau)
:={4\over e^2\tau}
\left[2\sqrt q\,\beta\sqrt{\operatorname{Tr}\mathsf K}+q\beta^2\right].
\end{split}\tag{RM11}
\]
Taking traces proves, in the exact given order,
\[
\left|\operatorname{Tr}(\Lambda e^{-\tau H}L_B)
-\operatorname{Tr}(\Theta e^{-\tau\mathsf K^{-1}})\right|
\le\varepsilon_H(\tau).
\tag{RM12}
\]
There is no commutation premise on \(\Theta,\mathsf K\). This proves the received model through all modes, including the entire complement of its \(d\)-dimensional range.

## 3. The actual reduced memory pencil and its mass matrix

Let \(a=\lambda_{\min}\Theta>0\), and \(V_B=Y\Theta^{-1/2}\), an original-target isometry. Write
\[
R_{\rm red}(z)=V_B^\dagger\Lambda(zI+H)^{-1}L_BV_B,
\quad
R_0(z)=\Theta^{1/2}(\mathsf K^{-1}+zI)^{-1}\Theta^{1/2}.
\tag{RM13}
\]
The two inversions in this construction first eliminate the original kernel and then the remaining observed complement; associativity of the full quadratic minimum gives precisely this restriction of the full inverse. RM9 implies \(\|R_{\rm red}-R_0\|\le\varepsilon_R\), while
\[
R_0(z)\succeq {a\over\kappa_-^{-1}+z}I_d.
\]
Consequently, when the explicit finite quantity
\[
\delta_R(z)={\varepsilon_R(\kappa_-^{-1}+z)\over a}<1,
\tag{RM14}
\]
the comparison and its inverse are
\[
(1-\delta_R)R_0\preceq R_{\rm red}\preceq(1+\delta_R)R_0,
\]
\[
{\widehat{\mathcal F}_{\rm red}(z)\over1+\delta_R}
\preceq\mathcal F_{\rm red}(z)
\preceq{\widehat{\mathcal F}_{\rm red}(z)\over1-\delta_R},
\quad
\widehat{\mathcal F}_{\rm red}(z)
=\Theta^{-1/2}(\mathsf K^{-1}+zI)\Theta^{-1/2}.
\tag{RM15}
\]
This proves the exact relationship between the static reduced matrix and the spectral pencil. Its coefficient of \(z\) is \(\Theta^{-1}\); the original observed mass is retained.

An immediate determinant estimate useful for the programme is
\[
-d\log(1+\delta_R)\le
\log{\det\mathcal F_{\rm red}\over\det\widehat{\mathcal F}_{\rm red}}
\le-d\log(1-\delta_R).
\tag{RM16}
\]
It follows by conjugating RM15 by the positive model square root and multiplying eigenvalues. At all four cutoffs, the absolute signed error is at most the sum of these four finite bounds. The constant \(d\) is retained; it is not lost on passage from operators to determinants.

In the proved rational-source family, put \(T=T_{k,N}\). Its explicit bounds give \(\log T=q\log(q/k)+O_h(q)\), \(\log\beta=o(q)\), \(\log\kappa_\pm=2\log T+o(q)\), and \(-\log a=o(q)\). Substitution in RM11 and RM14 shows
\[
\begin{gathered}
\varepsilon_H(\tau)=\exp[-q\log(q/k)+O_h(q)]
\quad\text{if }\log\tau=2q\log(q/k)+O_h(q),\\
\delta_R(x/T^2)=\exp[-q\log(q/k)+O_{h,A,\mathscr P}(q)]
\quad(0\le x\le x_0<\infty).
\end{gathered}\tag{RM17}
\]
These displays are upper bounds; a vanishing error is allowed. Their meaning is \(\varepsilon_H,\delta_R\le\exp[-q\log(q/k)+Cq]\) eventually, with the prescribed fixed data. The explicit finite formulas RM11 and RM14 control the threshold. Since \(\log d=O(\log q)\), RM16 remains exponentially small on this scale. Every error is smaller than the retained observation floor \(e^{-o(q)}\). No effective threshold for a separate reference zero law is introduced.

## 4. Exact pole reconstruction in the original metric

The general Feshbach–Schur construction and reconstruction map are established in Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, *The Feshbach–Schur map and perturbation theory* (2021), [original arXiv source, version 1](https://arxiv.org/src/2105.02058v1), Section 1, theorem `thm:isospF`, equations `Fesh`, `QP`, and proposition `prop:U-prop-SA`; the original file was read at lines 398–490. The following finite proofs establish the constants and original-metric identities used here. They do not require the paper’s separate small-perturbation theorem.

Decompose \(E=K\oplus K^\perp\), identifying \(K^\perp\) with the original \(B\) via RM1, and retain
\[
H=\begin{pmatrix}A&B_H\\B_H^\dagger&D_H\end{pmatrix}>0,
\qquad
\mathcal F(z)=zI+D_H-B_H^\dagger(A+zI)^{-1}B_H.
\tag{RM18}
\]
If \(A+zI\) is invertible, solve the first block equation in \((H+zI)(x,b)=(0,c)\). It gives \(x=-(A+zI)^{-1}B_Hb\) and then \(\mathcal F(z)b=c\). Thus \(\mathcal F(z)^{-1}=\Lambda(H+zI)^{-1}L_B\) whenever both inverses exist. The same elimination gives a congruence between \(H+zI\) and \(\operatorname{diag}(A+zI,\mathcal F(z))\) for real \(z\); it preserves the full inertia because the elimination matrix is invertible.

Let \(h\) be a simple least eigenvalue, with unit eigenvector \(w\), and let the remaining eigenvalues be at least \(g>h\). Put \(\theta=\|\Lambda w\|_{Q_B}^2>0\). For unit \(x\in K\), \(|\langle w,x\rangle|^2\le1-\theta\). The spectral theorem gives
\[
A\succeq[h(1-\theta)+g\theta]I>hI.
\tag{RM19}
\]
In particular the expressions at \(z=-h\) below are defined. Put \(b=\Lambda w/\sqrt\theta\). The block eigenvector equations and its unit norm give
\[
\mathcal F(-h)b=0,\qquad
w=\sqrt\theta\binom{-(A-hI)^{-1}B_Hb}{b},
\qquad b^\dagger\mathcal F'(-h)b=\theta^{-1}.
\tag{RM20}
\]
The derivative is \(I+B_H^\dagger(A-hI)^{-2}B_H\), so the last identity is exactly the norm of the displayed reconstructed vector. The spectral resolution of the full resolvent proves
\[
\operatorname*{Res}_{z=-h}\mathcal F(z)^{-1}=\theta bb^\dagger.
\tag{RM21}
\]
For the static Schur matrix \(S=\mathcal F(0)\), the same resolution gives \(S^{-1}=(\theta/h)bb^\dagger+R\), \(0\preceq R\preceq g^{-1}I\). Therefore
\[
{h\over\theta+h/g}\le\lambda_{\min}S\le {h\over\theta},
\qquad\lambda_2(S)\ge g\quad(\dim B\ge2).
\tag{RM22}
\]
The last bound follows by the max–min principle on the complement of \(b\), where the rank-one term vanishes. RM20–22 give the exact relation among the full pole, the static eigenvalue and the observation residue.

## 5. Multiplicities and the entire slow cluster

Let \(W:\mathbb C^d\to E\) be an isometry onto a slow spectral subspace, with all eigenvalues in \([h_-,h_+]\), and suppose the orthogonal complement has spectrum at least \(g>h_+\). Put \(\Theta_W=W^\dagger P_BW\), \(a_W=\lambda_{\min}\Theta_W>0\). Since
\(\|P_KW\|^2=\|I-\Theta_W\|=1-a_W\), every unit \(x\in K\) satisfies \(\|W^\dagger x\|^2\le1-a_W\). Hence
\[
A\succeq[h_-(1-a_W)+ga_W]I\succeq ga_W I.
\tag{RM23}
\]
This is a bound for the entire actual cluster. RF57–58 supplies an explicit value in the rational family: put \(\epsilon_N=\beta_N/(f_-T-\beta_N)\), \(\ell_N=e^{-2E_{k,d,N}}\), and
\[
a_W\ge\ell_{\mathrm{sharp},N}
=\left(\sqrt{\ell_N}\sqrt{1-\epsilon_N^2}
-\sqrt{1-\ell_N}\epsilon_N\right)^2
\quad\text{when }\epsilon_N\le\sqrt{\ell_N}/4.
\]
RF50 gives \(g\ge\beta_N^{-2}\). Thus the computable choice
\(\alpha=\beta_N^{-2}\ell_{\mathrm{sharp},N}\) is valid in RM28. The additional finite comparison
\((f_-T-\beta_N)^{-2}<\alpha\) puts the entire slow cluster below the kernel block. All these inequalities hold eventually on the growing-degree family by RF36–58. The bounds give \(a_W\ge e^{-o(q)}\) and \(g\ge e^{-o(q)}\), with the full observed Gram retained.

For an eigenvalue \(h<\lambda_{\min}A\) of multiplicity \(s\), choose an orthonormal eigenframe \(W_h\), put \(C_h=\Lambda W_h\), and \(\Theta_h=C_h^\dagger C_h\). The matrix \(C_h\) is injective: a full eigenvector in \(K\) would have energy at least \(\lambda_{\min}A>h\). Thus \(\Theta_h>0\). Block reconstruction, column by column, proves
\[
\begin{gathered}
\mathcal F(-h)C_h=0,\qquad
C_h^\dagger\mathcal F'(-h)C_h=I_s,\\
\operatorname*{Res}_{z=-h}\mathcal F(z)^{-1}=C_hC_h^\dagger.
\end{gathered}\tag{RM24}
\]
In the isometric observed frame \(Y_h=C_h\Theta_h^{-1/2}\), these become
\[
Y_h^\dagger\mathcal F'(-h)Y_h=\Theta_h^{-1},
\qquad\operatorname*{Res}_{z=-h}\mathcal F(z)^{-1}
=Y_h\Theta_hY_h^\dagger.
\tag{RM25}
\]
The matrix mass remains through every collision. For distinct eigenvalues \(h_i,h_j<\lambda_{\min}A\), their observed eigenvectors \(c_i,c_j\) satisfy the exact joint orthogonality identity
\[
c_i^\dagger\left[I+B_H^\dagger(A-h_iI)^{-1}(A-h_jI)^{-1}B_H\right]c_j
=\delta_{ij}.
\tag{RM26}
\]
For equal eigenvalues this is RM24. For distinct ones it follows either by taking inner products of the reconstructed full eigenvectors or by the resolvent identity for the divided difference of \(\mathcal F\). This establishes the full relation among poles and their observed vectors without an assumption that their observed Gram is diagonal.

## 6. Every slow eigenvalue in the energy graph

Keep the entire energy-minimizing section and its two Grams:
\[
L_{\rm en}b=\binom{-A^{-1}B_Hb}{b},\quad
Z=L_{\rm en}^\dagger L_{\rm en}=I+B_H^\dagger A^{-2}B_H,
\quad S=L_{\rm en}^\dagger HL_{\rm en}.
\]
Its actual isometry is \(J_{\rm en}=L_{\rm en}Z^{-1/2}\), and its energy operator is
\[
J_{\rm en}^\dagger HJ_{\rm en}=Z^{-1/2}SZ^{-1/2}.
\tag{RM27}
\]
Let \(h_j\) denote the eigenvalues of \(H\) in increasing order, including multiplicities, and \(\nu_j\) those of RM27 in the same convention. Fix a computable \(\alpha\le\lambda_{\min}A\). For every \(j\) with \(h_j<\alpha\),
\[
h_j\le\nu_j\le {h_j\over1-h_j/\alpha}.
\tag{RM28}
\]
There are at most \(\dim B\) such eigenvalues, by the block inertia at a real number below \(\alpha\). The lower bound is the minimum principle on the isometric subspace \(\operatorname{im}J_{\rm en}\). For the upper bound expand the exact resolvent in RM18:
\[
\mathcal F(-h)=S-hZ-h^2B_H^\dagger A^{-2}(A-hI)^{-1}B_H.
\]
For \(0<h<\alpha\), the final positive matrix is at most
\(h^2(Z-I)/(\alpha-h)\preceq h^2Z/(\alpha-h)\). Hence
\[
S-{h\over1-h/\alpha}Z\preceq\mathcal F(-h).
\tag{RM29}
\]
At \(h=h_j\), block inertia says \(\mathcal F(-h)\) has at least \(j\) nonpositive eigenvalues. The same is true of the left side of RM29. Conjugating by \(Z^{-1/2}\) gives the upper bound. This proof includes every multiplicity and does not use differentiation of an individually labelled eigenvalue at a crossing.

In the proved native late cluster, \(h_j=\exp[-2q\log(q/k)+O_h(q)]\) and \(\alpha\ge e^{-o(q)}\). Thus RM28 gives a relative error of size at most
\[
0\le {\nu_j\over h_j}-1
\le {h_j\over\alpha-h_j}
=\exp[-2q\log(q/k)+O_{h,A,\mathscr P}(q)],
\tag{RM30}
\]
with the same upper-bound interpretation as RM17, uniform over the admitted cluster. The original graph metric \(Z\) is retained. Its determinant cost is calculated for the canonical multiplication operator in the accompanying memory/energy proof; RM28 alone does not assign that determinant cost for an arbitrary growing-degree filter.

Multiplying the proved bounds over all \(d\) slow directions also gives the entire cluster determinant, including all collisions:
\[
0\le\sum_{j=1}^d\log\nu_j-\sum_{j=1}^d\log h_j
\le-\sum_{j=1}^d\log(1-h_j/\alpha)
\le\frac{d h_+}{\alpha-h_+}.
\tag{RM31}
\]
The last inequality follows by integrating \((1-t)^{-1}\) from zero to \(h_j/\alpha\). RF51 and RM23 make the final error exponentially small in the native family. Consequently RF54's full slow-energy return
\(-C_\partial dq+o(dq)\) is also the return of the first \(d\) eigenvalues of the actual energy-graph operator \(Z^{-1/2}SZ^{-1/2}\). The four-cutoff error is bounded by the sum of the four displayed finite errors. This is an evaluated receiving result for the entire cluster; the full graph determinant still includes its remaining eigenvalues.

## Proof sources and exact scope

The complete source-family memory and rational-filter identities are in the [pinned 014 reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/f1ad8be11f329a12d562420edfa58fa464948ee2/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/UNIFORM_SOURCE_FAMILY_COMPLETE_READER.tex), specifically UH1–32 and IFE24–31. The harmonic and inverse decomposition used for the canonical native receiver are proved in [HAR1–49](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md) and [ACT1–48](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/ACTION_PROOFS.md). The root source polynomial, source mass, period and four-cutoff signs are unchanged.

Original-author TeX for Dusson–Sigal–Stamm was obtained intact from arXiv version 1 and read at the stated locators. The original Gamma and Meixner–Pollaczek sources remain attributed to their human authors in the rational-source proof. The estimates here are finite derivations, not an invocation of a source theorem without checking its hypotheses. Exact small-matrix checks and numerical norm checks have their separate fixtures and reported scope; they do not establish an asymptotic theorem.
