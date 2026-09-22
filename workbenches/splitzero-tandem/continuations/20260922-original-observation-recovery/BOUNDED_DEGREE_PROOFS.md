# Finite observation chains with the original source and current

Independent derivation, 22 September 2026. The received sources are `03_received.md` and `06_received.md`; both were read completely. Statements BD1–BD18 below prove the bounded-degree receiver and add an intrinsic degree theorem, an explicit whole-source metric estimate, and recovery of every original spectral-pole residue. The original native kernel coefficient and the separate complex-current signs remain unevaluated. No conclusion here supplies the inherited EIQ value.

## BD1. Original objects and the admitted period domain

Fix the original simple hypothetical offcritical quartet, with \(0<\delta<1/2\), \(\gamma>2\), and the actual original unit and period. Retain the size-five orbit domain and the stronger period bound OC71–73, \( |\varpi|\ge R_{\rm corner}^{\rm explicit}\), which proves all four corner coefficients nonzero. Its proof uses \(\gamma\ge1000\delta\); for an actual zeta quartet this follows from the retained Platt–Trudgian finite-height theorem. These are existing proved programme domains, not new assumptions substituted for an unfinished calculation. The exact definitions and proof coverage are recorded in `SOURCE_USE_LEDGER.md`.

Let \(k\equiv1\pmod4\), \(k\ge17\), and put
\[
q=(k+1)^2,\quad m=8k-16,\quad n=q-m,\quad
\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,
\]
\[
Q_k(y)=\prod_{a,b=0}^k(y-\omega_{ab}),\qquad
E=\mathbb C[y]/(Q_k),\quad M[p]=[yp],\quad
\mathscr A=kI/2+iM.
\]
All roots are distinct, since their real and imaginary parts recover \(b,a\). All roots are nonzero, since \(k\) is odd. The given observation \(\Lambda:E\to B\) is onto, \(\dim B=n\), and \(K=\ker\Lambda\) has dimension \(m\). For every original cutoff \(q-1\le N\le2q\), \(G_N>0\) is the actual attained metric obtained by minimizing the original polynomial-source norm on its entire affine fibre. No Euclidean metric replaces \(G_N\).

The original conductor biform has coefficients \(a_{uv}\), \(0\le u,v\le8\), including every original scalar and phase, and
\[
\sigma_{uv}=(2v-8)\gamma-i(2u-8)\delta,
\quad C_A[p]=\left[\sum_{u,v=0}^8a_{uv}p(y+\sigma_{uv})\right]
\in E_-:=\mathbb C[y]/Q_{k-8}.
\]
Original CP8–9 prove well-definedness and a unique onto map \(\widehat C_A:B\to E_-\) with \(C_A=\widehat C_A\Lambda\). Indeed \(S=k/2+iy\), \(S_-=(k-8)/2+iy_-\) transforms CP8's physical shift \(4+(2u-8)\delta+i(2v-8)\gamma\) into exactly the displayed \(\sigma_{uv}\). This is a coordinate identity, including the centering and \(i\), and does not move the physical integration axis.

The precise public proofs are [OC71–73, complete original corner bound](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RETAINED_COMPLETE_PROOF_SOURCES.tex#L128308) and [OC61, the finite-height domain](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RETAINED_COMPLETE_PROOF_SOURCES.tex#L279817). Dave Platt and Tim Trudgian's [original paper, arXiv:2004.09765](https://arxiv.org/abs/2004.09765), Theorem 1 (source label bank), proves height \(3\,000\,175\,332\,800\); the weaker \(3\cdot10^{12}\) suffices here. Its retained original author TeX was read through the theorem and the complete “Theory and computation” section. This task does not rerun that finite-height computation.

The conductor maps and their proof are retained in [CP8–9, original conductor and arithmetic defect](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RETAINED_COMPLETE_PROOF_SOURCES.tex#L281873). The matching source lines were inspected; an unrelated occurrence of the prefix IVO is not used as evidence for this map.

## BD2. Literal restriction maps and the 80-power bound

Use the root-value isomorphisms solely as coordinates. For \(s=(u,v)\), define
\[
(R_sx)_{ab}=x_{a+u,b+v}\quad(0\le a,b\le k-8).
\]
Then \(C_A=\sum_s a_sR_s\) and \(R_sM-M_-R_s=\sigma_sR_s\). The latter follows entry by entry from \(\omega_{a+u,b+v}^{(k)}-\omega_{ab}^{(k-8)}=\sigma_{uv}\). Induction gives
\[
C_j:=\sum_s a_s\sigma_s^jR_s
=\sum_{h=0}^j(-1)^{j-h}\binom jh M_-^{j-h}C_AM^h. \tag{BD2}
\]
Let \(\mathcal S=\{s:a_s\ne0\}\), \(J=|\mathcal S|\le81\). The shifts on this support are distinct. Write
\[
L_s(z)=\prod_{t\in\mathcal S\setminus\{s\}}\frac{z-\sigma_t}{\sigma_s-\sigma_t}
=\sum_{j=0}^{J-1}\ell_{sj}z^j.
\]
The identity \(\sum_j\ell_{sj}C_j=a_sR_s\) is exact. Thus the observations \(\Lambda M^h\), \(0\le h\le J-1\), recover every supported restriction \(R_s\), with the actual nonzero \(a_s\) divided only where allowed. Each corner box is a product of intervals \( [0,k-8]\) or \([8,k]\). Their union covers \([0,k]^2\), since \(k\ge17\). Every upper coordinate is therefore recovered. Consequently
\[
\bigcap_{h=0}^{J-1}\ker(\Lambda M^h)=0,\qquad d\le J-1\le80. \tag{BD3}
\]
Without the corner domain, this argument recovers precisely the union of supported boxes for the conductor stack. It does not identify \(\Lambda\) with \(C_A\), nor prove a failure of the original observation from a failure of that smaller stack.

## BD3. Eight derivatives leave at most 128 directions

Homogenize the actual conductor as a biform \(\mathcal A\) of bidegree \((8,8)\) in \((X_0,X_1;Y_0,Y_1)\), and put
\[
\mathcal D=-2i\delta X_1\partial_{X_1}+2\gamma Y_1\partial_{Y_1}.
\]
Its monomial weights are \(-2i\delta u+2\gamma v\), pairwise distinct within any bidegree. The constant difference between these weights and \(\sigma_{uv}\) means the spans of the first \(r+1\) derivative biforms and moment biforms coincide, by an invertible triangular binomial matrix.

No coordinate variable divides \(\mathcal A\), because its four corners are nonzero. If a nonconstant bihomogeneous irreducible \(f\mid\mathcal A\) satisfied \(f\mid\mathcal Df\), equal bidegrees would give \(\mathcal Df=cf\). Distinct weights force \(f\) to be one monomial. An irreducible monomial is a coordinate variable, a contradiction. Thus \(f\nmid\mathcal Df\).

If \(f\) has multiplicity \(e\) in \(\mathcal A\), then \(e\le8\): at least one positive coordinate of the bidegree of \(f\) uses at least \(e\) of the corresponding total degree eight. Leibniz's formula gives
\[
\mathcal D^e(f^eg)\equiv e!(\mathcal Df)^eg\pmod f,\qquad f\nmid g,
\]
because every other distribution of the \(e\) derivatives leaves an undifferentiated factor \(f\). Hence \(\gcd(\mathcal A,\mathcal D\mathcal A,\ldots,\mathcal D^8\mathcal A)=1\), with multiplicities treated explicitly.

There are at most sixteen distinct irreducible factors: their positive total bidegrees sum to sixteen counting multiplicity. For each factor \(f\), the polynomial 
\(\sum_{j=1}^8t^{j-1}\mathcal D^j\mathcal A\) modulo \(f\) is nonzero and has degree at most seven in \(t\). The quotient by the prime \(f\) is an integral domain, so it has at most seven scalar zeros. Among \(t=0,\ldots,112\), at least one therefore gives a biform \(\mathcal B\) coprime to \(\mathcal A\).

In the biform ring, multiplication by \(\mathcal A\) and \(\mathcal B\) on bidegree \((k-8,k-8)\) is injective. Their images intersect in \(\mathcal A\mathcal B\mathcal P_{k-16,k-16}\): unique factorization implies \(\mathcal A u=\mathcal Bv\) only when \(u=\mathcal Bw\), \(v=\mathcal Aw\). Thus the sum has codimension
\[
(k+1)^2-2(k-7)^2+(k-15)^2=128. \tag{BD4}
\]
The ordinary transposes of these multiplication matrices are precisely the root-coordinate convolution maps. Ordinary transpose determines their rank; no Hermitian source metric is inserted into this algebraic identification. Since \(C_A=\widehat C_A\Lambda\), (BD2) shows that
\[
K_j:=\bigcap_{h=0}^j\ker(\Lambda M^h),\qquad \dim K_8\le128. \tag{BD5}
\]
This proves the claimed constant for the original observation even though the conductor generally has a larger kernel. It uses no squarefreeness assertion.

## BD4. Partial chains, their construction, and their intrinsic lengths

Put \(R=k\sqrt{\delta^2+\gamma^2}\), \(\nu=2R\), and \(A=M/\nu\). This changes only the receiver parameter; the original operator remains \(M=\nu A\) and the source measure is unchanged. Let \(d\) be least with \(K_d=0\). Multiplication gives injective maps
\[
A:K_j/K_{j+1}\longrightarrow K_{j-1}/K_j.
\]
Indeed \(Ax\in K_{j-1}\) for \(x\in K_j\), and \(Ax\in K_j\) implies \(x\in K_{j+1}\). Define \(b_j=\dim K_{j-1}-\dim K_j\), \(1\le j\le d\), \(b_{d+1}=0\). These injections prove \(b_{j+1}\le b_j\).

For each \(j\), descending from \(d\) to one, choose a complement of \(K_j+AK_j\) in \(K_{j-1}\). Its dimension is \(b_j-b_{j+1}\): the image of \(AK_j\) in \(K_{j-1}/K_j\) has dimension \(b_{j+1}\). For each chosen vector \(x\), take \(x,Ax,\ldots,A^jx\). Inductively, at quotient level \(K_{r-1}/K_r\), the descendants of longer selected chains span the injected copy of \(K_r/K_{r+1}\), and the vectors newly selected at level \(r\) complete its basis. Descending induction proves all nonterminal vectors form a basis of \(K\). At level \(E/K\), the terminal vectors of positive-length chains are independent: a relation modulo \(K\) among their terminals would, after taking their immediate predecessors, contradict the injectivity \(K/K_1\to E/K\). Add terminal-only chains to complete \(E/K\).

We obtain a basis \(F\) with chains
\[
e_{a,0},\ldots,e_{a,\varepsilon_a},\quad
Ae_{a,j}=e_{a,j+1}\ (j<\varepsilon_a),\quad a=1,\ldots,n.
\]
The nonterminal vectors span \(K\). Terminal actions are unrestricted; they remain in \(\widehat A=F^{-1}AF\). With coordinate inclusions \(E_K,E_B\) for nonterminal and terminal vectors, respectively, \(\Lambda F=R_B E_B^*\) for an invertible \(R_B\). Precisely,
\[
\dim K_j=\sum_a(\varepsilon_a-j)_+,\quad
\#\{a:\varepsilon_a\ge j\}=b_j,\quad
\sum_a\varepsilon_a=m,\quad \max_a\varepsilon_a=d\le80,
\]
\[
\sum_a(\varepsilon_a-8)_+\le128,\quad
b_1\ge(m-128)/8=k-18,\quad
\sum_a\varepsilon_a^2\le8m+80\cdot128. \tag{BD6}
\]
For the last bound, \(\varepsilon^2\le8\varepsilon+80(\varepsilon-8)_+\) when \(0\le\varepsilon\le80\). A negative lower bound for \(b_1\) is simply weaker than \(b_1\ge0\). These are partial observation chains, not invariant cyclic summands.

## BD5. The polynomial quotient and its complete finite spectral data

Define the \(n\times q\) matrix \(P(z)\) by a separate row on each chain,
\[
P_a(z)=(z^{\varepsilon_a},z^{\varepsilon_a-1},\ldots,z,1).
\]
Its supports are disjoint. Directly on each nonterminal column,
\[
P(z)(I-z\widehat A)E_K=0,\quad P(z)E_B=I,\quad
D(z):=P(z)(I-z\widehat A)E_B,
\]
\[
P(z)(I-z\widehat A)=D(z)E_B^*,\qquad D(0)=I. \tag{BD7}
\]
The matrix \(U(z)=[(I-z\widehat A)E_K,E_B]\) is polynomial and unimodular. In each chain its columns are \(e_j-ze_{j+1}\) followed by the terminal \(e_\varepsilon\); their determinant is one in chain order. Reordering all hidden columns before all terminals contributes only a fixed sign. Its bottom inverse rows are \(P(z)\), since they annihilate the first columns and equal the identity on terminal columns. Consequently
\[
U(z)^{-1}(I-z\widehat A)[E_K,E_B]
=\begin{pmatrix}I&X(z)\\0&D(z)\end{pmatrix}.
\]
An upper block column operation removes \(X\). All transformations are unimodular; evaluating at zero fixes the scalar determinant. Therefore
\[
\det D(z)=\det(I-zM/\nu),\qquad
\operatorname{coker}_{\mathbb C[z]}D\simeq
\operatorname{coker}_{\mathbb C[z]}(I-zM/\nu). \tag{BD8}
\]
The forward map is \(PF^{-1}\); the inverse is terminal inclusion in the displayed transformed quotient. This proves equality of every finite elementary divisor, including its algebraic multiplicity, not only equality of determinants. The original \(M\) has no zero eigenvalue. For an unrelated operator with a zero eigenvalue, affine cokernels would not record that eigenvalue at infinity; (BD8) makes no such assertion.

## BD6. New intrinsic degree and minimality theorem

Every polynomial row \(T(z)\) satisfying \(T(z)(I-z\widehat A)E_K=0\) obeys \(Te_{a,j}=zTe_{a,j+1}\), one column at a time. It follows exactly that
\[
T(z)=u(z)P(z),\qquad u(z)=T(z)E_B. \tag{BD9}
\]
Thus the annihilator is a free polynomial module with basis the rows of \(P\). Since the supports of those rows are disjoint, no highest-degree cancellation between distinct chains is possible, and
\[
\deg(uP)=\max_{a:u_a\ne0}(\deg u_a+\varepsilon_a).
\]
The dimension of its rows of degree at most \(h\) is therefore
\[
H(h)=\sum_a\max(h-\varepsilon_a+1,0). \tag{BD10}
\]
The second finite differences of \(H\) give the number of chains of each length. Hence the multiset \(\{\varepsilon_a\}\) is intrinsic to the observation pair, and \(d\) is its necessary maximum polynomial basis degree. Any other polynomial module basis is \(VP\) with \(V\) unimodular; its row degrees cannot all be less than \(d\), because then those rows could not generate a chain coordinate with length \(d\). This proves degree minimality without assuming any cyclic invariance.

The number 80 is sharp for the conductor-support argument alone. For any distinct \(J\) shifts set \(a_s=1/\prod_{t\ne s}(\sigma_s-\sigma_t)\). Lagrange interpolation of \(z^j\) gives \(\sum_s a_s\sigma_s^j=0\) for \(0\le j<J-1\), and one for \(j=J-1\). All coefficients are nonzero. The constant upper value vector then vanishes under every conductor observation through power \(J-2\), by the binomial formula, but not at \(J-1\). Taking the full original \(9\times9\) shift rectangle gives \(J-1=80\). This is a sharpness example for arbitrary conductor coefficients with the stated support; it does not identify those coefficients with the actual period product or claim the actual full observation requires 80 powers.

## BD7. The projective quotient retains all endpoints

Homogenize the row on chain \(a\) to
\((z^{\varepsilon_a},z^{\varepsilon_a-1}w,\ldots,w^{\varepsilon_a})\). Its kernel is spanned by \(we_j-ze_{j+1}\). At every projective point these vectors are independent: if \(w\ne0\), solve sequentially from the first coordinate; if \(w=0\), they are nonzero multiples of distinct \(e_{j+1}\). Their number is the kernel dimension. Thus the complete exact sequence is
\[
0\longrightarrow\mathcal O(-1)^m\longrightarrow\mathcal O^q
\longrightarrow\bigoplus_a\mathcal O(\varepsilon_a)\longrightarrow0. \tag{BD11}
\]
At \(z=0\) the terminal coordinates survive; at \(w=0\) the first chain coordinates survive. Truncating each degree to eight gives the inclusion with diagonal entries \(w^{(\varepsilon_a-8)_+}\). Its cokernel is supported at \(w=0\), with exact length \(\sum_a(\varepsilon_a-8)_+=\dim K_8\le128\). Locally its summands are \(\mathbb C[t]/(t^{(\varepsilon_a-8)_+})\); this identifies the obstruction as a concrete torsion object and proves its connecting map.

For each \(r\), the \(r\)-th exterior bundle splits as \(\bigoplus_{|I|=r}\mathcal O(\sum_{a\in I}\varepsilon_a)\). Each \(\varepsilon_a\) occurs in \(\binom{n-1}{r-1}\) summands, so its total degree is \(\binom{n-1}{r-1}m\).

## BD8. Inverse-energy polynomialization and the unchanged physical source

Fix one actual \(G=G_N\), set \(\mathcal G=F^{-1}G^{-1}F^{-*}>0\), and define
\[
\mathcal C(z,\bar z)=P(z)\mathcal G P(z)^*.
\]
Since \(PE_B=I\), this is positive definite at every finite \(z\). For \(W_\eta=I-\eta M\), the actual inverse-energy receiver is
\[
\mathcal F_N(\eta,\bar\eta)
=\Lambda(W_\eta^*GW_\eta)^{-1}\Lambda^*.
\]
Where \(D(z)\) is invertible, (BD7) gives the exact gauge identity
\[
\mathcal C(z,\bar z)
=D(z)R_B^{-1}\mathcal F_N(z/\nu,\bar z/\nu)R_B^{-*}D(z)^*. \tag{BD12}
\]
At a zero of \(D\), the left side defines the polynomial continuation; the original inverse on the right is undefined there. No cancellation has removed the original spectral information from \(D\).

Let \(\mathcal P_{\le N}\) carry the original Gram matrix \(H_{\rm src,N}\), and let \(J_N:\mathcal P_{\le N}\to E\) be the literal residue map. The minimum-norm lift of \(x\) is
\(H_{\rm src,N}^{-1}J_N^*(J_NH_{\rm src,N}^{-1}J_N^*)^{-1}x\); it maps to \(x\), and it is orthogonal to \(\ker J_N\), proving both minimality and uniqueness. Thus
\[
G_N^{-1}=J_NH_{\rm src,N}^{-1}J_N^*,\quad
\mathcal C=(PF^{-1}J_N)H_{\rm src,N}^{-1}(PF^{-1}J_N)^*. \tag{BD13}
\]
The map \(PF^{-1}J_N\) annihilates the entire original ideal fibre \(Q_k\mathcal P_{\le N-q}\), because \(J_N\) does. Its domain is exactly \(\mathcal P_{\le N}\), not a higher-degree source. The variable \(z\) is a receiver parameter and does not multiply the physical polynomial \(p(y)\). Source masses, cutoffs, and all discarded-degree relations are therefore preserved by a proved commuting map.

If an activation family is defined by an affine sum of complete source covariances, the same fixed linear maps in (BD13) show every coefficient and every cross block of \(\mathcal C\) varies affinely. Positive definiteness follows from the actual family metric, with no independent selection of its blocks.

## BD9. Complete coefficient recovery and the missing metric

Write \(P(z)=\sum_{j=0}^dP_jz^j\). In row \(a\), \(P_j\) selects exactly \(e_{a,\varepsilon_a-j}\) if \(j\le\varepsilon_a\), and is zero otherwise. Hence
\[
\mathcal C_{ij}=P_i\mathcal G P_j^*.
\]
Stack the coefficient rows and remove only these specified zero rows. Every coordinate of the chain basis appears exactly once, so the resulting full coefficient Gram is precisely \(\mathcal G\) up to a fixed permutation. This is an explicit inverse map, not a rank argument alone.

In hidden/terminal order write
\[
\mathcal G=\begin{pmatrix}U&V\\V^*&W\end{pmatrix},\qquad
Q_c=W^{-1}=R_B^*QR_B,\quad Q=(\Lambda G^{-1}\Lambda^*)^{-1}.
\]
Gaussian block elimination proves
\[
R_K:=U-VW^{-1}V^*=(E_K^*F^*GF E_K)^{-1}. \tag{BD14}
\]
The coefficients at levels \(1,\ldots,8\) retain all hidden coordinates except the first \((\varepsilon_a-8)_+\) coordinates of each chain. These omitted coordinates span exactly \(K_8\). Order retained coordinates first and omitted coordinates second in the original restricted metric \(H=E_K^*F^*GF E_K\). The retained principal block of \(H^{-1}\) is the inverse of the Schur complement over the omitted block \(H_{00}\). Taking determinants yields the exact identity
\[
\log\det H=-\log\det(R_K)_{\rm retained}+\log\det H_{00}. \tag{BD15}
\]
The omitted term is the actual metric restricted to \(K_8\), including its source mass. It is not set to one.

## BD10. Direct local jets and the relation to chains

At \(\eta=0\) expand the actual inverse-energy receiver:
\[
\mathcal F_N(\eta,\bar\eta)=\sum_{i,j\ge0}\eta^i\bar\eta^jS_{ij},\quad
S_{ij}=\Lambda M^iG^{-1}(M^*)^j\Lambda^*.
\]
These are coefficients; derivatives are \(i!j!S_{ij}\). If \(I_K\) is any fixed frame of \(K\), completing the square in the source metric gives
\[
G^{-1}-G^{-1}\Lambda^*Q\Lambda G^{-1}
=I_K(I_K^*GI_K)^{-1}I_K^*.
\]
Multiplication on both sides proves
\[
S_{ij}-S_{i0}QS_{0j}
=(\Lambda M^iI_K)(I_K^*GI_K)^{-1}(\Lambda M^jI_K)^*. \tag{BD16}
\]
The stack for \(1\le i,j\le d\) has rank \(m\), because its nullspace is \(K_d=0\). Selecting \(m\) independent rows gives an invertible known matrix \(J\), and \(H_K^{-1}=J^{-1}C_{\rm sel}J^{-*}\). Through level eight its rank is \(m-\dim K_8\), and (BD15) is the exact complementary metric. Thus local jets give a finite observation inverse; they do not imply that \(K\) is invariant or that its partial chains are cyclic invariant subspaces.

For the full source, the stack \(\mathcal O_d=(\Lambda,\Lambda M,\ldots,\Lambda M^d)^{\mathsf T}\) is injective. A left inverse \(T\) gives \(G^{-1}=T(S_{ij})_{0\le i,j\le d}T^*\). This proves exact full-metric recovery from the bounded matrix jet, with the known operators and coordinate maps retained.

## BD11. A new explicit estimate on the entire original source

Here is a direct proof of the needed \(O_h(q)\) logarithmic width which does not invoke the received \(Z_{k,1}\) formula. Keep
\[
d\sigma(y)=|\Gamma(1/4+iy/2)|^2\frac{dy}{2\pi},\quad
M_\sigma=\sqrt{2\pi},\quad C_L=\frac{\pi}{\Gamma(3/4)^2}.
\]
The Gamma duplication and reflection formulas give
\(|\Gamma(1/4+iy/2)|^2|\Gamma(3/4+iy/2)|^2=2\pi^2/\cosh(\pi y)\).
Euler's integral gives \(|\Gamma(3/4+iy/2)|\le\Gamma(3/4)\). Hence \(d\sigma/dy\ge C_Le^{-\pi|y|}\). The Meixner–Pollaczek recurrence with this exact measure gives
\[
\|yp\|_\sigma\le2(L+1)\|p\|_\sigma\quad(\deg p\le L). \tag{BD17}
\]
For completeness, in its orthonormal basis the two shift coefficients are \(\sqrt{(j+1)(j+1/2)}\) and \(\sqrt{j(j-1/2)}\). Each truncated shift has norm at most \(L+1\), so their sum has the stated norm. The unchanged constant vector has squared norm \(M_\sigma\). These exact classical formulas and their original equation sources are recorded in the source ledger.

The original human-source equations are R. A. Askey and R. Roy's [duplication formula, DLMF5.5.E5 TeX](https://dlmf.nist.gov/5.5.E5.tex), [reflection formula, DLMF5.5.E3 TeX](https://dlmf.nist.gov/5.5.E3.tex), and [Euler integral, DLMF5.2.E1 TeX](https://dlmf.nist.gov/5.2.E1.tex), together with T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw's [Meixner–Pollaczek generating function, DLMF18.23.E7 TeX](https://dlmf.nist.gov/18.23.E7.tex) and [recurrence, DLMF18.22.E8 TeX](https://dlmf.nist.gov/18.22.E8.tex). The source files are retained without rewriting them.

Here are the exact mass and norm factors needed to specialize those equations. Euler's two Gamma integrals, under \(x+y=s\), \(x/(x+y)=v\), give the beta identity. Substituting \(v=e^r/(1+e^r)\) into that identity gives
\[
\int_{\mathbb R}e^{itr}\frac{e^{ar}}{(1+e^r)^{2a}}\,dr
=\frac{\Gamma(a+it)\Gamma(a-it)}{\Gamma(2a)}.
\]
Fourier inversion at zero, and then at real shifts, gives
\[
\int_{\mathbb R}|\Gamma(a+it)|^2e^{ist}\frac{dt}{2\pi}
=\frac{\Gamma(2a)}{(2\cosh(s/2))^{2a}}.
\]
The beta integrand is integrable on every horizontal line strictly inside its analytic strip \(|\Im r|<\pi\), with the vertical sides of a finite rectangle tending to zero exponentially. Shifting to such a line in the direction of the sign of \(t\) bounds its Fourier transform by \(C_\theta e^{-\theta|t|}\) for each \(0<\theta<\pi\). This proves the required absolute convergence and Fourier inversion. At \(a=1/4\), \(y=2t\), the identity gives the mass \(M_\sigma=\sqrt{2\pi}\) and, by analytic continuation inside \(|\Re u|<\pi/2\), the moment generating function \(M_\sigma(\cos u)^{-1/2}\). Specializing the cited generating function gives
\[
g_t(y)=(1+t^2)^{-1/4}e^{y\arctan t}=\sum_{j\ge0}c_j(y)t^j.
\]
For small real \(s,t\), integration of \(g_sg_t\), using
\(\cos(\arctan s+\arctan t)=(1-st)/\sqrt{(1+s^2)(1+t^2)}\), yields \(M_\sigma(1-st)^{-1/2}\). Comparing convergent Taylor coefficients proves
\(\langle c_j,c_\ell\rangle_\sigma=\delta_{j\ell}M_\sigma(1/2)_j/j!\).
The leading coefficient of \(c_j\) is \(1/j!\). Substitution into the cited recurrence gives exactly the two orthonormal shift coefficients above. This proves the factors used in (BD17), without changing the source mass.

Let \(p\) have degree at most \(2q\), and set \(f(z)=p(qz)\) only to estimate its coefficients. The physical interval is still \([q,2q]\), and
\[
\|p\|_\sigma^2\ge C_Lqe^{-2\pi q}\int_1^2|f(x)|^2dx.
\]
Let \(L_j\) be the usual Legendre polynomial with \(L_j(1)=1\). Its recurrence and \(\|2z-3\|_{\rm coeff,1}=5\) imply \(\|L_j(2z-3)\|_{\rm coeff,1}\le11^j\): the initial values have norms one and five, and the recurrence bounds the next norm by ten times its predecessor plus the preceding norm. The polynomials \(\sqrt{2j+1}L_j(2x-3)\) are orthonormal on \([1,2]\); this also follows directly by integrating their Rodrigues formula by parts, so no source metric is being identified with that auxiliary interval metric. Expanding \(f\) in this basis and applying Cauchy–Schwarz gives
\[
\|f\|_{\rm coeff,1}
\le(2q+1)11^{2q}\|f\|_{L^2[1,2]}
\le K_q\|p\|_\sigma,
\quad K_q=\frac{(2q+1)11^{2q}e^{\pi q}}{\sqrt{C_Lq}}. \tag{BD18}
\]
Indeed the sum of \(2j+1\) for \(j=0,\ldots,2q\) is \((2q+1)^2\), and all powers \(11^j\) are at most \(11^{2q}\).

The exact Legendre source is [DLMF18.12.E11, original generating-function TeX](https://dlmf.nist.gov/18.12.E11.tex), by the same Chapter 18 authors. Its equation is \((1-2xt+t^2)^{-1/2}=\sum_{j\ge0}L_j(x)t^j\). Differentiation in \(t\) and coefficient comparison give
\((j+1)L_{j+1}=(2j+1)xL_j-jL_{j-1}\), precisely the recurrence used above. The binomial theorem also gives
\[
L_j(x)=2^{-j}\sum_{a=0}^{\lfloor j/2\rfloor}
\frac{(-1)^a(2j-2a)!}{a!(j-a)!(j-2a)!}x^{j-2a}
=\frac1{2^jj!}\frac{d^j}{dx^j}(x^2-1)^j.
\]
The second equality follows by differentiating the binomial expansion of \((x^2-1)^j\). Integration by parts \(j\) times proves orthogonality to every degree less than \(j\); all boundary terms vanish. The leading coefficient is \((2j)!/(2^j(j!)^2)\), so its squared norm equals that coefficient times
\[
\int_{-1}^1x^jL_j(x)\,dx
=2^{-j}\int_{-1}^1(1-x^2)^jdx
=\frac{2^{j+1}(j!)^2}{(2j+1)!}.
\]
The last integral follows from \(I_0=2\), \(I_j=2jI_{j-1}/(2j+1)\), obtained by one integration by parts. Thus the squared norm is \(2/(2j+1)\), and the change \(x=2y-3\) gives exactly \(1/(2j+1)\) on \([1,2]\), as used in (BD18). A separate original TeX endpoint for the DLMF norm table was unavailable; no table value is assumed, since the norm has just been derived.

Put \(r=R/q\), \(t=\max(1,r)\), and \(\widehat Q(z)=q^{-q}Q_k(qz)\). Its coefficient norm is at most \((1+r)^q\). In division of \(z^{q+s}\), \(0\le s\le q\), by \(\widehat Q\), the quotient coefficients are the complete homogeneous polynomials \(h_0,\ldots,h_s\) of its \(q\) roots. This follows by expanding
\(\prod_\omega(1-(\omega/q)u)^{-1}=\sum_{\ell\ge0}h_\ell u^\ell\)
and matching powers from the leading term down. Each satisfies
\[
|h_\ell|\le\binom{q+\ell-1}{\ell}r^\ell\le4^qt^q
\quad(0\le\ell\le q).
\]
The first bound counts its monomials; the second uses \(\binom{2q}{q}\le4^q\). Therefore the literal Euclidean remainder map, on all degrees through \(2q\), has coefficient norm at most
\[
D_q=1+(q+1)[4t(1+r)]^q. \tag{BD19}
\]
This bound also covers degrees below \(q\), where the map is the identity. Division commutes exactly with the substitution \(y=qz\); there is no change to the original fibre.

Repeated use of (BD17) gives
\(\|(y/q)^j\|_\sigma\le\sqrt{M_\sigma}2^jj!/q^j\le\sqrt{M_\sigma}2^q\)
for \(0\le j<q\). Combining this with (BD18)–(BD19) proves the all-direction inequality
\[
\|\operatorname{rem}_{Q_k}p\|_\sigma
\le C_{\rm rem}\|p\|_\sigma,\qquad
C_{\rm rem}=\sqrt{M_\sigma}\,2^qD_qK_q. \tag{BD20}
\]
Every original root is retained in the division; no root pairing or real translation is used.

The established complete-source comparison is
\(\ell_k\|p\|_\sigma^2\le\|p\|_{\mu_k}^2\le u_k\|p\|_\sigma^2\)
for all degrees through \(2q\), with \(\log(u_k/\ell_k)=O_h(k+\log q)\). The unique representative below degree \(q\) is \(\operatorname{rem}_{Q_k}p\), while the higher cutoff minimizes over all its original lifts. Apply (BD20) to an attained higher lift. Since enlarging the permitted degree can only decrease its minimum, this proves
\[
e^{-E_k}G_{q-1}\preceq G_N\preceq G_{q-1},\qquad
E_k=2\log C_{\rm rem}+\log(u_k/\ell_k),\quad q-1\le N\le2q. \tag{BD21}
\]
This is finite and explicit for every \(k\) in BD1, without an extra eventual inequality \(R\le q\). For the fixed original quartet, \(r=k\sqrt{\delta^2+\gamma^2}/(k+1)^2\) is bounded; every term in \(\log C_{\rm rem}\) is \(O_h(q)\). Thus \(E_k=O_h(q)\), with the original measure mass present.

The source constants and their unchanged mass are proved in [HAR40, complete native source comparison](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RETAINED_COMPLETE_PROOF_SOURCES.tex#L296138). The original comparison applies on the whole degree-\(2q\) source, which is essential to applying it to the literal remainder and an arbitrary attained lift.

## BD12. The exact determinant remainder and activated families

Use the original four-cutoff return
\(\mathcal Rf=f_{q-1}+f_q-f_{2q-1}-f_{2q}\).
For any fixed injective \(t\)-column frame \(J\), monotonicity of the source cutoffs and (BD21) give
\[
0\le\mathcal R\log\det(J^*G_NJ)\le2tE_k.
\]
To see both inequalities separately, pair \(q-1\) with \(2q-1\) and \(q\) with \(2q\); each pair is nonnegative by inclusion of the exact source spaces. Each pair has generalized eigenvalues at most \(e^{E_k}\), proving the upper bound. Apply this to the actual frame of \(K_8\) in (BD15):
\[
0\le\mathcal R\log\det H_N+
\mathcal R\log\det(R_{K,N})_{\rm retained}
\le256E_k=O_h(q). \tag{BD22}
\]
Fixed changes of hidden frame contribute a cutoff-independent determinant and cancel in \(\mathcal R\). At depth \(d\le80\) there is no remainder. The identities determine an exact positive determinant receiver; they do not evaluate its native value or the EIQ coefficient.

For the retained joint source the established complete-form bounds are
\(\mathbf L_k^{-1}T_k\preceq G_N^J\preceq\mathbf B_kT_k\), with the same fixed diagonal \(T_k\), and source inclusion still gives \(G_N^J\preceq G_{q-1}^J\). Hence
\(G_N^J\succeq(\mathbf L_k\mathbf B_k)^{-1}G_{q-1}^J\).
For the supplied activation whose inverse metric is the affine combination
\(G_N(\alpha)^{-1}=(1-\alpha)G_N(0)^{-1}+\alpha(G_N^J)^{-1}\), \(0\le\alpha\le1\), invert the two endpoint inequalities, add them with these weights, and invert again. This proves (BD21) with
\[
E_k^*=\max\{E_k,\log(\mathbf L_k\mathbf B_k)\}.
\]
The same proof yields (BD22) with \(E_k^*\). No family cross block is discarded.

## BD13. Exact finite samples, their error constants, and optimal scalar count

Let \(L=2d+1\), \(t_\ell=(\ell+1)/(d+2)\), \(r_\ell=\sqrt{t_\ell}\), and
\(z_{\ell s}=r_\ell e^{2\pi is/L}\), \(0\le\ell\le d\), \(0\le s<L\). The eigenvalues of \(M/\nu\) have modulus at most \(1/2\), so all these samples, which have modulus below one, avoid every original pole. For \(0\le h\le d\), the discrete Fourier identity gives
\[
\frac{r_\ell^{-h}}L\sum_{s=0}^{L-1}e^{-2\pi ihs/L}\mathcal C(z_{\ell s},\bar z_{\ell s})
=\sum_{j=0}^{d-h}\mathcal C_{j+h,j}t_\ell^j. \tag{BD23}
\]
Indeed all exponent differences lie between \(-d\) and \(d\); their congruence to \(h\) modulo \(2d+1\) is therefore equality. Interpolate the first \(d-h+1\) distinct rational \(t_\ell\) and use \(\mathcal C_{ij}=\mathcal C_{ji}^*\) for negative differences. Thus at most
\((d+1)(2d+1)\le13041\)
matrix values recover the exact full coefficient Gram.

If each sampled Hermitian matrix has operator error at most \(\delta_s\), coefficient errors are at most
\[
A_d\delta_s,\qquad
A_d=\max_{0\le h\le d}\frac{(d+2)^{h/2}[4(d+2)]^{d-h}}{(d-h)!}.
\]
To prove this, the Fourier row has norm sum at most \(r_\ell^{-h}\le(d+2)^{h/2}\). For interpolation of degree \(v=d-h\), each Lagrange numerator has coefficient norm at most \(2^v\), and its denominator has modulus \((d+2)^{-v}\ell!(v-\ell)!\). Summing over \(\ell\) gives \([4(d+2)]^v/v!\). The recovered coefficient Gram error is at most \((d+1)A_d\delta_s\), by the row-sum bound for its block operator norm; deleting known zero rows cannot enlarge the norm.

If \(g_*\) is the actual smallest eigenvalue of the exact full coefficient Gram and \((d+1)A_d\delta_s<g_*\), the additive estimate gives the corresponding positive relative enclosure. The constant \(g_*\) is not assigned a numerical value. More generally, a coherent enclosure \(a\mathcal G\preceq\widehat{\mathcal G}\preceq b\mathcal G\) passes to every principal restriction and Schur complement: use their minimum-energy characterization. Each rank-\(r\) log determinant then has error between \(r\log a\) and \(r\log b\), and its four-cutoff return error has modulus at most \(2r\log(b/a)\). Positivity of the pointwise polynomial alone is insufficient; \(1-|z|^2+|z|^4>0\) has an indefinite coefficient Gram.

Let \(a=\#\{\varepsilon_a>0\}\le m\). The \(n-a\) terminal-only outputs have a constant covariance subblock already supplied by the baseline. A full additional Hermitian sample contains \(2an-a^2=O(kq)\) real entries. There is a sharper exact statement about scalar linear data. With the baseline terminal covariance fixed, the real affine space of Hermitian source covariances has dimension
\[
q^2-n^2=m(2q-m). \tag{BD24}
\]
Its positive definite part is open in that affine space. The map to all the sampled real and imaginary matrix entries in (BD23) is injective, by exact coefficient recovery. Gaussian elimination therefore selects exactly \(q^2-n^2\) linearly independent real sample functionals and gives an explicit square inverse on the unknown affine coordinates. No smaller number of real linear scalar measurements can be injective on an open subset: its nonzero linear kernel would give two nearby positive covariances with the same data. Thus the bound is attained in this scalar linear data model. Conditioning is the actual selected square matrix's inverse norm; no uniform free accuracy follows from dimension counting.

## BD14. New exact recovery of every original spectral pole

Let \(\lambda=\omega_{ab}/\nu\), \(z_\lambda=1/\lambda\), and \(\chi(z)=\det D(z)=\prod_\mu(1-z\mu)\). All these roots are simple and nonzero. Since the polynomial equivalence in BD5 preserves the simple elementary divisor, \(D(z_\lambda)\) has corank one and \(\operatorname{adj}D(z_\lambda)\) has rank one. Moreover,
\[
\chi'(z_\lambda)=-\lambda\prod_{\mu\ne\lambda}(1-\mu/\lambda)\ne0.
\]
Using \(D^{-1}=\operatorname{adj}D/\chi\) in (BD12), with the actual complex phases retained, gives
\[
\lim_{z\to z_\lambda}|z-z_\lambda|^2\mathcal F_N(z/\nu,\bar z/\nu)
=\frac{R_B\operatorname{adj}D(z_\lambda)\mathcal C(z_\lambda,\bar z_\lambda)
\operatorname{adj}D(z_\lambda)^*R_B^*}{|\chi'(z_\lambda)|^2}. \tag{BD25}
\]
The right side is nonzero positive of rank one, because \(\mathcal C(z_\lambda)>0\). Independently, the spectral projector \(\Pi_\lambda=\prod_{\mu\ne\lambda}(A-\mu I)/(\lambda-\mu)\) gives
\[
\text{right side of (BD25)}
=\frac1{|\lambda|^2}\Lambda\Pi_\lambda G^{-1}\Pi_\lambda^*\Lambda^*.
\]
Indeed \((I-zA)^{-1}=\sum_\mu\Pi_\mu/(1-z\mu)\), and only the matching pole-pole term survives after multiplication by \(|z-z_\lambda|^2\). Its nonvanishing also follows from observability: if \(\Lambda\Pi_\lambda=0\), every observation power annihilates its nonzero eigenline, contradicting BD2. Thus none of the original positive inverse-energy poles cancels. Polynomialization regularizes the covariance while \(D\) and the exact formula (BD25) retain every pole, its multiplicity, its output line and all residue phases visible to the Hermitian matrix. An arbitrary complex scalar phase on an eigenvector cancels in its projector and is not physical data lost by this statement.

## BD15. Curvature, exact degree, and all-direction estimates

Define a reference covariance in the fixed chain coordinates, diagonal with entries \(\binom{\varepsilon_a}{j}\) on \(e_{a,j}\). Denote it by \(\mathcal G_{\rm ref}\). This is an auxiliary comparison form, not the physical metric. The binomial theorem gives
\[
\mathcal C_{\rm ref}(z,\bar z)=\operatorname{diag}((1+|z|^2)^{\varepsilon_a}).
\]
Let \(a_N,b_N>0\) be the exact least and greatest generalized eigenvalues of \((\mathcal G,\mathcal G_{\rm ref})\). Then
\(a_N\mathcal C_{\rm ref}\preceq\mathcal C\preceq b_N\mathcal C_{\rm ref}\).
If \(g_-I\preceq G\preceq g_+I\) is an actual known enclosure, explicit alternatives are
\[
a_N=\frac1{2^dg_+\|F\|^2},\qquad b_N=\frac{\|F^{-1}\|^2}{g_-}.
\]
Indeed \(I\preceq\mathcal G_{\rm ref}\preceq2^dI\) and the singular-value inequalities for \(F^{-1}G^{-1}F^{-*}\) give these comparisons. Exterior products preserve them, with constants \(a_N^r,b_N^r\). In particular the largest \(r\)-volume eigenvalue is bounded by these constants times \((1+|z|^2)^{\varepsilon_{(1)}+\cdots+\varepsilon_{(r)}}\), where the degrees are ordered decreasingly; each corresponding ordered exterior eigenvalue has its own sum of degrees.

Put
\[
T=P'\mathcal G P'^*-P'\mathcal G P^*\mathcal C^{-1}P\mathcal G P'^*,
\qquad \kappa=\operatorname{tr}(\mathcal C^{-1}T).
\]
For every output column \(u\), \(u^*Tu\) is the minimum over columns \(v\) of
\((P'^*u-P^*v)^*\mathcal G(P'^*u-P^*v)\); expanding and minimizing proves this assertion exactly. Thus \(a_NT_{\rm ref}\preceq T\preceq b_NT_{\rm ref}\). Direct differentiation gives
\[
T_{\rm ref}=\operatorname{diag}\bigl(\varepsilon_a(1+|z|^2)^{\varepsilon_a-2}\bigr).
\]
Comparison of Rayleigh quotients for \((T,\mathcal C)\), followed by the finite-dimensional min-max principle (obtained by diagonalizing \(\mathcal C^{-1/2}T\mathcal C^{-1/2}\)), proves its nonzero ordered eigenvalues lie between
\[
\frac{a_N}{b_N}\frac{\varepsilon_{(j)}}{(1+|z|^2)^2}
\quad\hbox{and}\quad
\frac{b_N}{a_N}\frac{\varepsilon_{(j)}}{(1+|z|^2)^2}.
\]
Its rank is exactly the number of positive chain lengths. Matrix differentiation gives \(\kappa=\partial_z\partial_{\bar z}\log\det\mathcal C\). Near infinity factor \(z^{\varepsilon_a}\) from each row of \(P\); the remaining rows tend to distinct first-chain coordinate rows, so their Gram determinant has a strictly positive limit and a convergent expansion in \(z^{-1},\bar z^{-1}\). Hence
\(\log\det\mathcal C=2m\log|z|+O(|z|^{-1})+c\), with a differentiated remainder \(O(|z|^{-2})\). Green's formula, \(\Delta=4\partial_z\partial_{\bar z}\), now gives
\[
\frac1\pi\int_{\mathbb C}\kappa(z)\,d^2z=m. \tag{BD26}
\]
The integral converges by the displayed eigenvalue comparison. This integer is a bundle degree, not the native determinant-return coefficient.

## BD16. Gauge-corrected current with its original sign

In hidden/terminal order write \(\widehat A=(A_{KK},A_{KB};A_{BK},A_{BB})\), and retain \(U,V,W,Q_c\) from BD9. The coefficient relations are
\[
D_1=-A_{BB},\qquad \mathcal C_{10}=A_{BK}V. \tag{BD27}
\]
The first follows by differentiating (BD7) at zero; \(P_1E_B=0\). For the second, \(A_{BK}\) selects exactly the immediate predecessor of each positive-length chain, which is the hidden part of \(P_1\). Define the original attained section
\(L=G^{-1}\Lambda^*Q\). In chain coordinates its value on \(R_Bb\) is \((VQ_cb,b)\). Consequently the exact observed arithmetic operator is
\[
M_B^c:=R_B^{-1}\Lambda ML R_B
=\nu(A_{BB}+A_{BK}VQ_c)
=\nu(\mathcal C_{10}Q_c-D_1). \tag{BD28}
\]
For the actual observed value \(b=R_B^{-1}\Lambda v\), the centered physical current is therefore
\[
\Phi_B=i\nu b^*\left[
Q_c(\mathcal C_{10}-\mathcal C_{01})Q_c-Q_cD_1+D_1^*Q_c
\right]b. \tag{BD29}
\]
This uses \(\mathscr A-kI/2=iM\), so \(\mathscr A+\mathscr A^{\dagger_G}-kI=i(M-M^{\dagger_G})\). The terms from \(D_1\) are the full connection correction for the polynomial output frame; deleting them changes the actual current. The \(5\times5\) exact fixture below changes \(-7/18\) to \(+5/18\) if those terms are deleted.

Let \(\mathsf E_\eta=L^*W_\eta^*GW_\eta L\), keeping this same original section for both measurements. Expanding both quadratic energies proves, for real \(r>0\),
\[
\Phi_B=(\Lambda v)^*\frac{\mathsf E_{-ir}-\mathsf E_{ir}}{2r}(\Lambda v). \tag{BD30}
\]
The section is not re-minimized separately for the two words. For \(\mathsf H_\eta=W_\eta^{\dagger_G}W_\eta\), direct expansion also gives
\[
M=\frac{\mathsf H_{-r}-\mathsf H_r}{4r}
+\frac{\mathsf H_{-ir}-\mathsf H_{ir}}{4ir}.
\]
Choose \(r<1/R\) to make all four energies positive definite. This recovers \(M\) and its adjoint as exact linear combinations. Products of at most \(2d\le160\) factors recover \(M^i(M^{\dagger_G})^j\), \(0\le i,j\le d\), in their stated order. No commutation is used. The observed ordered moments are \(S_{ij}Q\), since
\(\Lambda M^i(M^{\dagger_G})^jL=\Lambda M^iG^{-1}(M^*)^j\Lambda^*Q\).
Their Gram matrix has rank \(q\), by BD10. Every positive Hilbert-space realization of the same complete ordered data must have dimension at least its Gram rank \(q\); the original \(E\) realizes it, proving equality.

The relation to the original consecutive monic polynomial boundary is also exact. [CP4 and its following proof, original full outgoing correction](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RETAINED_COMPLETE_PROOF_SOURCES.tex#L281793) give
\[
\mathscr A-kI/2=i\mathcal J_N+\frac{b_{N+1}b_N^*G}{\omega_N},\qquad
\mathcal J_N^{\dagger_G}=\mathcal J_N.
\]
Adding its adjoint and compressing by the same \(L\) yields
\[
i(S_{10}-S_{01})=
\frac{(\Lambda b_{N+1})(\Lambda b_N)^*+(\Lambda b_N)(\Lambda b_{N+1})^*}{\omega_N}.
\]
Here \(\omega_N\) is the original squared monic norm, not a chosen scalar. Thus the current is the original boundary receiver in its actual metric and monic phases. Its rank-two origin does not restrict the leakage rank \(b_1\), which is at least \(k-18\).

## BD17. Both complex cross-pairings and the moving attained lift

The separate complex quantities can be retained without assigning their signs. Let \(v\) be the actual original vector, write its chain coordinates as \((v_K,b)\), and set
\[
X=VQ_c,\quad a=v_K-Xb,\quad H_K^c=E_K^*F^*GF E_K,
\]
\[
Z=A_{KB}+A_{KK}X-XA_{BB}-XA_{BK}X.
\]
The observed attained lift is \(w=F(Xb,b)\), and the hidden component is \(x=F(a,0)\). In these coordinates the metric factors exactly as
\[
F^*GF=
\begin{pmatrix}H_K^c&-H_K^cX\\-X^*H_K^c&Q_c+X^*H_K^cX\end{pmatrix}.
\]
This follows either by inversion of the covariance blocks or from orthogonality of \((Xb,b)\) to every hidden vector, together with their respective metric restrictions. Multiplying the full operator blocks, without dropping terminal actions, now gives
\[
z_M:=x^*GMw=\nu a^*H_K^c Zb,\qquad
w_M:=w^*GMx=\nu b^*Q_cA_{BK}a. \tag{BD31}
\]
For the physical centered operator \(iM\), both cross-pairings multiply by \(i\), so \(\overline{z_{iM}}w_{iM}=\overline{z_M}w_M\). Neither complex pairing, nor its real or imaginary sign, is determined merely by the rank, singular values, curvature integral, or determinant asymptotic. Equations (BD28)–(BD31) are their exact connecting maps to the polynomial receiver and original physical current.

## BD18. Exact fixtures and verification scope

The executable checker uses rational and Gaussian-rational arithmetic for the matrix identities, and separately labels any floating-point inequality check. Its main nontrivial current fixture is
\[
M=\begin{pmatrix}0&0&1&0&0\\1&0&0&0&1\\0&1&1&0&0\\0&0&0&0&1\\0&0&1&1&i\end{pmatrix},\quad
\Lambda=\begin{pmatrix}0&0&1&0&0\\0&0&0&0&1\end{pmatrix},
\]
\[
u=(1,i,1,1,2)^{\mathsf T},\quad G^{-1}=I+uu^*,\quad G=I-uu^*/9,
\]
with chain lengths \((2,1)\). It checks the complete polynomial matrices
\[
P=\begin{pmatrix}z^2&z&1&0&0\\0&0&0&z&1\end{pmatrix},\quad
D=\begin{pmatrix}1-z-z^3&-z^2\\-z&1-iz-z^2\end{pmatrix}.
\]
It checks the exact covariance, all coefficient blocks, the whole source Gram, the full hidden inverse and an omitted one-dimensional metric, the correct gauge current and the incorrect value when its \(D_1\) terms are deleted. These fixtures test identities; they are not replacements for the actual period coefficients or native xi moments.

The repeated-factor rectangular fixture \((1+X)^2(1+Y)^2\) on the upper \(6\times6\) grid checks successive kernel dimensions \(20,13,6,2,0\). This tests multiplicities in BD3. An original-shape \(9\times9\) shift fixture checks the support interpolation independently. A Jordan fixture tests determinant multiplicity in BD5. A simple-spectrum fixture tests every residue in BD14. A literal polynomial residue-source fixture includes a nonzero relation column and verifies (BD13). These tests complement the proofs; the proofs, rather than finite numerical samples, establish the original \(k\)-uniform claims.

The native coefficient, the EIQ evaluation and separate current signs are retained as unresolved original numerical/analytic quantities. The completed results here are exact finite recovery maps, the bounded complementary determinant estimate, intrinsic polynomial degree, preserved source fibres, and gauge-corrected current identities.
