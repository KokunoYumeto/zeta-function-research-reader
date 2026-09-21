# Exact evaluation by positive cutoff increments

21 September 2026. This continuation supplies an executable form of the complete original invariant determinant. Every original row, the lower-root projection, the nonideal conductor relations, the source mass and all four cutoff signs remain. The computation below has two parts: an exact integer evaluation of the universal scalar reference, and a sequence of positive quantities for the actual invariant rows. The second part still requires those original rows as input; no hypothetical zero or period is selected by the algorithm.

## 1. Original source and complete observation

Keep the original packet and admitted period, with
\[
q=(k+1)^2,\quad q'=(k-7)^2,\quad c'=k/2-4,\quad
g=q-q'-v,\quad N=q+L,\quad M=g+L.
\tag{CI1}
\]
Here $v$ is the actual order at zero of the full conductor symbol $E_A$. The four original values of $L$ are $-1,0,q-1,q$. Let $\chi'$ be the complete lower-root polynomial in $S'$. For $i,j\ge0$ put
\[
H_{ij}=\int_{\mathbb R}\overline{\chi'(c'+iy)(c'+iy)^i}
\chi'(c'+iy)(c'+iy)^j\,d\sigma(y),\quad
d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy.
\tag{CI2}
\]
Its mass is $\mathfrak m_\sigma=\sqrt{2\pi}$. Write $H_M=(H_{ij})_{0\le i,j\le M}$. It is positive definite: a nonzero polynomial times $\chi'$ is nonzero outside a finite set and the density is positive on the real axis. This argument also covers repeated lower roots.

Let $\ell_1,\ldots,\ell_r$ be the complete original invariant functionals after the proved low-degree elimination. Retain
\[
b_j=(\ell_1(S'^j),\ldots,\ell_r(S'^j))^{\mathsf T},\qquad
B_M=[b_0\ \cdots\ b_M],\qquad A_R=B_{g-1}.
\tag{CI3}
\]
The original construction proves $\operatorname{rank}A_R=r$. Its rows annihilate every complete relation $u_j=\mathcal U_A(S^j)$. These facts, including the actual low-degree elimination, come from KF and CG, rather than from a choice of new observation rows.

Let $J_M$ map coefficients of $p(S')$ to the Gamma-orthonormal coefficients of $\chi'p$. Then $J_M^*J_M=H_M$. The orthogonal projector onto the full lower-root ideal is $J_MH_M^{-1}J_M^*$. If $W_N$ is the original invariant row matrix in that orthonormal source, its restriction satisfies $W_NJ_M=B_M$. Consequently
\[
C_M=B_MH_M^{-1}B_M^*
=W_NJ_MH_M^{-1}J_M^*W_N^*.
\tag{CI4}
\]
This proves the exact map from the full projected covariance to the coefficient expression used below. Its source is the entire lower-root ideal, with no missing pole rows. $C_M$ is positive definite for $M\ge g-1$, since $B_M$ already contains the full-row-rank matrix $A_R$.

## 2. One added source coefficient gives a positive covariance increment

For $M\ge g$ write the same moment matrix and the same observation in blocks:
\[
H_M=\begin{pmatrix}H_{M-1}&h_M\\h_M^*&\eta_M\end{pmatrix},
\quad B_M=[B_{M-1}\ b_M],\quad
\nu_M=\eta_M-h_M^*H_{M-1}^{-1}h_M>0.
\tag{CI5}
\]
Define the full observation of the new orthogonal polynomial by
\[
f_M=b_M-B_{M-1}H_{M-1}^{-1}h_M,\qquad
s_M=\frac{f_M^*C_{M-1}^{-1}f_M}{\nu_M}\ge0.
\tag{CI6}
\]
Completing the quadratic square in $H_M$, or multiplying its block inverse, gives
\[
C_M=C_{M-1}+\frac{f_Mf_M^*}{\nu_M},\qquad
\frac{\det C_M}{\det C_{M-1}}=1+s_M.
\tag{CI7}
\]
For completeness, the block inverse is the sum of $\operatorname{diag}(H_{M-1}^{-1},0)$ and
$\nu_M^{-1}(-H_{M-1}^{-1}h_M,1)^{\mathsf T}(-H_{M-1}^{-1}h_M,1)^*$. Multiplication by $B_M$ proves the first equality. For the second, conjugate by the positive square root of $C_{M-1}$; the rank-one matrix has its single nonzero eigenvalue $s_M$. This proof includes $f_M=0$.

Applying the four original signs now gives the exact formula
\[
\boxed{\mathcal R\log\det C_M
=-\log(1+s_g)-2\sum_{j=g+1}^{g+q-1}\log(1+s_j)
-\log(1+s_{g+q}).}
\tag{CI8}
\]
Indeed the difference between the first and third determinants sums increments from $g$ through $g+q-1$, while the difference between the second and fourth sums from $g+1$ through $g+q$. Their overlap accounts for the coefficient two. In particular every term in this covariance return is nonpositive. The formula treats the two adjacent endpoints separately.

All of CI4--8 survive any fixed invertible change of invariant row coordinates: $B\mapsto TB$, $C\mapsto TCT^*$, $f\mapsto Tf$ leaves $s_M$ unchanged. The source metric and physical coordinate are unchanged. Thus no row preconditioning can silently change this sequence.

## 3. The complete relation gives positive original-kernel losses

Write the original relation polynomial as
\[
u_L(S')=\mathcal U_A(S^L)(S'),\quad \deg u_L=g+L,
\quad a_L=[S'^{g+L}]u_L=\mu_v\binom{q+L}{v}\ne0.
\tag{CI9}
\]
For $L\ge0$ let $R_L$ be the full Gram of $u_0,\ldots,u_L$ in the weight $|\chi'|^2d\sigma$. Put $R_{-1}=1$ at the determinant level and
\[
\rho_L=\frac{\det R_L}{\det R_{L-1}}>0.
\tag{CI10}
\]
Equivalently $\rho_L$ is the squared norm of $u_L$ after subtracting its orthogonal projection onto all earlier $u_j$. Their distinct degrees and nonzero leading coefficients prove linear independence and strict positivity. This step retains the entire nonideal relation graph.

The ordered coefficient basis $1,S',\ldots,S'^{g-1},u_0,\ldots,u_L$ has determinant $\tau_L=\prod_{j=0}^La_j$. Schur-complementing the complete relation Gram therefore gives the original graph quotient metric $Q_L$ on the fixed low-coefficient space:
\[
\det Q_L=\frac{|\tau_L|^2\det H_{g+L}}{\det R_L},
\qquad
\frac{\det Q_L}{\det Q_{L-1}}
=\frac{|a_L|^2\nu_{g+L}}{\rho_L}.
\tag{CI11}
\]
For $L=-1$, $Q_{-1}=H_{g-1}$. Since $B_M$ annihilates every $u_j$, the attained observation covariance on this fixed quotient is exactly
\[
C_{g+L}=A_RQ_L^{-1}A_R^*.
\tag{CI12}
\]
One proof uses the same block basis: $B_M$ becomes $[A_R\ 0]$, so the upper block of the inverse Gram is $Q_L^{-1}$.

Choose once a full-rank coefficient matrix $K_0$ for $\ker A_R$. Its Gram is $K_L=K_0^*Q_LK_0$. There is a positive constant $c_{A_R,K_0}$, independent of $L$, with
\[
\det K_L=c_{A_R,K_0}\det Q_L\det C_{g+L}.
\tag{CI13}
\]
To prove this including every frame factor, choose a fixed right inverse $J$ of $A_R$. In the fixed square basis $T=[K_0\ J]$, Schur-complement the $K_0$ block of $T^*Q_LT$. The resulting quotient metric has inverse $A_RQ_L^{-1}A_R^*$ because $A_RT=[0\ I]$. Hence
$|\det T|^2\det Q_L=\det K_L/\det C_{g+L}$, and $c_{A_R,K_0}=|\det T|^2$. Empty kernels or observations use determinant one and the same identity.

Combining CI7, CI11 and CI13 yields the new positive loss ratio
\[
\boxed{d_L:=\frac{\det K_{L-1}}{\det K_L}
=\frac{\rho_L}{|a_L|^2\nu_{g+L}(1+s_{g+L})}\ge1.}
\tag{CI14}
\]
The inequality is a consequence of the original minimum, not an estimate inferred from rank. The allowed source space and relation span both increase as $L$ increases. Every representative allowed at $L-1$ is allowed at $L$ with the same physical norm, so $Q_L\preceq Q_{L-1}$. Restriction to the same $K_0$ gives $K_L\preceq K_{L-1}$ and proves the inequality. In particular the source data satisfy the stronger finite identity and inequality
\[
\rho_L\ge |a_L|^2\nu_{g+L}(1+s_{g+L}).
\tag{CI15}
\]
Thus the original relation's new squared distance controls both the new source direction and the entire observed covariance gain. Its factors cannot be allocated separately by their dimensions.

The exact four-cutoff graph-kernel return is now
\[
\boxed{\mathcal R\log\det K_L
=\log d_0+2\sum_{L=1}^{q-1}\log d_L+\log d_q.}
\tag{CI16}
\]
It is a sum of nonnegative quantities. The physical original kernel differs from this retained graph-kernel metric by the finite KF49 receiver. The sharpened same-source comparison proved in the accompanying finite-determinant continuation replaces its older form-width term; all low-degree and angle terms stay in that bound. Therefore CI16 evaluates the correct graph contribution without assigning a missing original coefficient.

CI14 also gives a directly usable error rule. If positive certified intervals are available for $\rho_L,\nu_{g+L},1+s_{g+L}$, and $|a_L|^2$, divide their endpoints with the denominator endpoints reversed. Intersect the result with $[1,\infty)$ using CI14. Monotonicity of $\log$ and the weights $1,2,\ldots,2,1$ gives a certified interval for CI16. This is a computation on the actual complete relation; a floating-point midpoint alone is not an interval.

## 4. The scalar reference is an exact integer computation

Define the retained mass-independent rational coefficients by
\[
\nu_{2j}=(2j)![t^{2j}](\cos t)^{-1/2},\quad \nu_{2j+1}=0,
\quad m_j=2^j\nu_{2j}.
\tag{CI17}
\]
The physical moments are $\int y^j d\sigma=\mathfrak m_\sigma\nu_j$. The common mass has not been changed. This generating function follows by integrating the monic Meixner--Pollaczek generating function in the physical $y$ coordinate. The original TeX equations [DLMF 18.23.7](https://dlmf.nist.gov/18.23.E7) and [18.22.8](https://dlmf.nist.gov/18.22.E8) were read; their authors are Tom H. Koornwinder, Roderick Wong, Roelof Koekoek and René F. Swarttouw, with William P. Reinhardt, in NIST DLMF Chapter 18.

Let $T_j=(d^{2j+1}/dt^{2j+1})\tan t|_{t=0}$. The differential equations $(\tan t)'=1+\tan^2t$ and $((\cos t)^{-1/2})'=\tfrac12\tan t(\cos t)^{-1/2}$ give
\[
T_0=1,\quad T_n=\sum_{j=0}^{n-1}\binom{2n}{2j+1}T_jT_{n-j-1},
\quad m_0=1,
\tag{CI18}
\]
\[
\boxed{m_n=\sum_{j=0}^{n-1}\binom{2n-1}{2j+1}2^jT_jm_{n-j-1}.}
\tag{CI19}
\]
Leibniz's rule gives the displayed binomial coefficients; odd derivatives of the even function vanish. Induction proves these numbers are positive integers. The first five are $1,1,7,139,5473$.

For integers $a,n\ge0$ set $D_0(a)=1$ and
\[
D_n(a)=\det[m_{a+i+j}]_{0\le i,j<n}.
\tag{CI20}
\]
Every determinant is positive. Indeed $m_j$ is the $j$th moment of the positive pushforward of $d\sigma/\mathfrak m_\sigma$ by $y\mapsto2y^2$. The weighted Gram with factor $x^a$ is strictly positive for any nonzero polynomial, because its support contains the positive half-line. The exact recurrence is
\[
\boxed{D_n(a)=\frac{D_{n-1}(a)D_{n-1}(a+2)-D_{n-1}(a+1)^2}{D_{n-2}(a+2)}\quad(n\ge2).}
\tag{CI21}
\]
This is the Desnanot--Jacobi identity, read in Christian Krattenthaler, [Advanced Determinant Calculus, arXiv:math/9902004v3](https://arxiv.org/abs/math/9902004v3), Section 2.3, source labels `sec:cond`, `prop:cond`, `eq:cond`. Here is a direct proof in the present positive case. Schur-complement the middle $(n-2)$ rows and columns of the Hankel matrix. Its remaining $2\times2$ determinant gives the numerator in CI21 divided by the square of the middle determinant. Multiplying by that middle determinant proves CI21. Positivity proved above ensures every denominator is nonzero. Each quotient is an integer since it equals CI20. The checker verifies zero remainder at every performed division.

For the original rational determinant
\[
\Delta_n(a)=\det[\nu_{2a+i+j}]_{0\le i,j\le n},\quad \Delta_{-1}(a)=1,
\tag{CI22}
\]
reorder both rows and columns by parity. Odd-even cross blocks are zero, and the two permutation signs multiply to one. With $r=\lceil(n+1)/2\rceil$ and $s=\lfloor(n+1)/2\rfloor$, factor the powers of two from the two diagonal blocks to obtain
\[
\boxed{\Delta_n(a)=2^{-(n+1)a-n(n+1)/2}D_r(a)D_s(a+1).}
\tag{CI23}
\]
The even block contributes exponent $ra+r(r-1)$; the odd block contributes $s(a+1)+s(s-1)$. Their sum is the exponent in CI23. This proves the full determinant formula, including parity and all powers of two.

Insert these exact integers into
\[
\mathcal A_{k,v}=\frac{\Delta_{g-1}(q')\Delta_g(q')\Delta_{q-1}(q-v)\Delta_q(q-v)}{\Delta_{q+g-1}(q')\Delta_{q+g}(q')\Delta_0(q-v)}.
\tag{CI24}
\]
It is a specified positive rational number. Moments only through order $4q-2v$ are required. The maximum order follows by inspecting each block in CI23; its last even-moment index is $a+n$, or $a+n-1$ if the last parity is absent. The script uses only the necessary indices and checks every positive division.

The incoming finite scalar receiver is
\[
\left|\mathcal K_k-\log\mathcal A_{k,v}-\mathcal R\log\det C_M\right|\le\mathcal E_k.
\tag{CI25}
\]
Its complete corrected source proof appears in the accompanying finite-determinant continuation. Substituting CI8 gives an explicit scalar reference minus the positive covariance gains; substituting CI16 instead keeps the nonideal relation and avoids the scalar comparison altogether. These are two exact ways to compute the same original graph allocation with their stated finite physical-transfer errors. Neither discards the small covariance eigenvalues.

## 5. Executed calculations and their scope

`exact_reference.py` executes CI18--24 using arbitrary-precision integers. It compares 31 small positive Hankel determinants and 32 full parity Grams with independent direct determinants, and checks the initial moments. The resulting 64 checks test factors, indexing and exact divisibility. Its saved numerator and denominator determine each scalar reference without a decimal approximation. Directed-rounding logarithms supply a separate outward decimal enclosure.

The runs $(k,v)=(9,0)$ and $(13,1)$ are evaluations of the universal scalar reference for those stated integer parameters. They do not assert that either conductor order has been supplied for an actual hypothetical zeta quartet. The invariant covariance is not inferred from these numbers.

| Scalar reference parameters | Certified enclosure for $\log\mathcal A_{k,v}/(kq)$ | Exact condensation divisions |
|---|---|---|
| $k=9,v=0,q=100$ | $5.05293645587376521324 < \cdot < 5.05293645587376521325$ | 9,996 |
| $k=13,v=1,q=196$ | $6.72260331029858135790 < \cdot < 6.72260331029858135791$ | 37,878 |

The full saved rational numerators and denominators have respective bit lengths $(276512,269951)$ and $(1314806,1290094)$. The displayed intervals are outward truncations of the retained 60-decimal certified bounds. These are finite reference values, not estimates of the original kernel coefficient or its limit.

`check_cutoff_innovations.py` executes a complete auxiliary complex-shift example. It uses
\[
\mathcal T_Af(S')=f(S'+4i)-f(S'),\quad
\chi'=S'(S'-1),\quad
\chi=S'(S'-1)(S'-2)(S'-3)(S'-4i)(S'-1-4i),
\tag{CI26}
\]
with $c'=0$, $q=6$, $q'=2$, $v=1$, $g=3$, and the two actual numerator rows $e^w-1$ and $e^{3w}-e^{2w}$. Both divide by the full symbol $e^{4iw}-1$ at the removable origin. All seven relation columns $u_0,\ldots,u_6$ are present. Each relation is polynomial because the numerator vanishes at both roots of $\chi'$. The code proves exact annihilation of every relation, then checks CI4, CI7 and CI11--16 at every cutoff from $L=-1$ to $L=6$. Its 111 exact checks also verify the stronger source/observation/kernel energy split and rank-one quotient decrease derived below, retaining both observation rows and the full physical $i$ phase.

The original graph-kernel return in this example is $6.0207468765747968457\ldots$, while the full projected covariance return is $-9.9322122445256196262\ldots$. Their exact positive rational exponentials and every $d_L,s_M$ are saved in `CUTOFF_INNOVATION_CHECKS.json`. These values establish the execution of the full algorithm on a finite example. They do not evaluate the outstanding original-period covariance or its asymptotic coefficient.

## Programme proof sources

The complete original source and invariant maps used in CI1--16 are [KF1--55, ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex) and [CG1--32, COMPLETE_CONDUCTOR_GRAPH_METRIC.tex](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/COMPLETE_CONDUCTOR_GRAPH_METRIC.tex), especially CG29--32. Their finite source hypotheses remain. The new projected-covariance and integer calculations above are complete derivations from those objects. The publication source ledger retains the exact read versions, source hashes and theorem locators.


# The exact cutoff loss in the original conductor relation

Independent derivation, 21 September 2026. This note proves CI5–16 of the accompanying CUTOFF_INNOVATION_PROOFS.md directly from the original KF/CG source and supplies a stronger positive rank-one formula. It does not modify the frozen collision proof or duplicate its checks.

## 1. One fixed polynomial observation at every cutoff

Keep the original polynomial variables \(S,S'\), centres \(c=k/2,c'=k/2-4\), original upper and lower polynomials \(\chi,\chi'\), full conductor \(\mathcal T_A\), first nonzero moment \(\mu_v\), and
\[
q=(k+1)^2,\quad q'=(k-7)^2,\quad
g=q-q'-v,\quad M=g+L,\quad N=q+L.
\]
The exact complete relation is
\[
u_L(S')=\mathcal U_A(S^L)(S'),\qquad
\chi'u_L=\mathcal T_A(\chi S^L),\qquad
a_L=[S'^{g+L}]u_L=\mu_v\binom{q+L}{v}\ne0.
\tag{CL1}
\]
The same \(\mathcal U_A\) acts at every degree; its subscript in KF41 means its restriction to the indicated source degree, not a change of operator.

Here is the explicit fixed observation extending CG29–30 beyond its low coefficient domain. Let \(\mathcal R\) be KF8's unique polynomial right inverse of \(\mathcal T_A\) whose coefficients below degree \(v\) vanish. Its nilpotent derivative expression is compatible under inclusion of polynomial spaces: the coefficient of any fixed polynomial is determined by a finite derivative series, and extending the ambient degree inserts only zero additional terms. Therefore
\[
\mathcal T_A\mathcal R=I,\qquad
\mathcal R\mathcal T_Ap=p-\operatorname{low}_{<v}p
\tag{CL2}
\]
on the entire polynomial space. The second identity follows from the first: its difference lies in \(\ker\mathcal T_A=\mathcal P_{<v}\), and the prescribed low coefficients determine that difference exactly.

Retain the full additional invariant columns \(J_R=S_kZ_k\). Write \(\operatorname{ev}_\beta\) for evaluation at all original upper roots, extending the coefficient matrix \(V\) to polynomials of any degree. Set
\(B_{\mathcal L}=J_R^{\mathsf T}\operatorname{ev}_\beta|_{\mathcal P_{<v}}\).
Choose the fixed row-combination matrix \(E\) from CG29's row basis of
\(\Pi B_\eta\). Thus
\[
EB_{\mathcal L}=0,\qquad
A_R\eta=EJ_R^{\mathsf T}\operatorname{ev}_\beta\mathcal R(\chi'\eta),
\quad \deg\eta<g.
\]
Define on every polynomial \(f(S')\)
\[
\ell(f)=EJ_R^{\mathsf T}\operatorname{ev}_\beta\mathcal R(\chi'f).
\tag{CL3}
\]
All maps are the original complex-linear ones; no metric adjoint is inserted in \(J_R^{\mathsf T}\). Every coefficient and every eliminated low constraint remains in \(E\). Since \(\chi\) vanishes at all upper roots, CL1–3 prove
\[
\ell(u_L)
=EJ_R^{\mathsf T}\operatorname{ev}_\beta
\bigl(\chi S^L-\operatorname{low}_{<v}(\chi S^L)\bigr)=0.
\tag{CL4}
\]
This holds for every \(L\ge0\). On \(\mathcal P'_{<g}\), \(\ell=A_R\) exactly.

Distinct degrees and \(a_L\ne0\) imply the direct sum
\[
\mathcal P'_{\le g+L}
=\mathcal P'_{<g}\oplus\operatorname{span}(u_0,\ldots,u_L).
\]
Let \(\pi_L\) be projection to the first summand. The new vector \(u_L\) is the sole basis vector with degree \(g+L\), so
\[
\pi_L|_{\mathcal P'_{\le g+L-1}}=\pi_{L-1},\qquad
\ell|_{\mathcal P'_{\le g+L}}=A_R\pi_L.
\tag{CL5}
\]
Consequently \(B_M=[\ell(1),\ldots,\ell(S'^M)]\) is the prefix of one fixed observation matrix. It is not independently recomputed or changed at each cutoff.

The source norm also remains fixed:
\[
\|f\|_H^2=\int_{\mathbb R}
|\chi'(c'+iy)f(c'+iy)|^2\,d\sigma(y),\qquad
d\sigma(y)=|\Gamma(1/4+iy/2)|^2dy/(2\pi).
\tag{CL6}
\]
The spaces, metrics and relations are literal inclusions. Thus a previously permitted representative of a fixed low vector remains permitted with precisely the same norm. This proves \(Q_L\preceq Q_{L-1}\) for the attained graph quotient metric, without any assumed compatibility of an independently chosen moving frame.

## 2. Source innovation and the exact complete-relation innovation

At \(L\ge0\), put \(M=g+L\). Let
\[
H_M=\begin{pmatrix}H_{M-1}&h_M\\h_M^*&\eta_M\end{pmatrix},\quad
a^{\rm proj}=H_{M-1}^{-1}h_M,
\]
and let
\[
p_M(S')=S'^M-\sum_{j<M}a^{\rm proj}_jS'^j,\quad
\nu_M=\|p_M\|_H^2=\eta_M-h_M^*H_{M-1}^{-1}h_M>0.
\tag{CL7}
\]
This is the original monic polynomial in the complete weighted source, with no source mass divided out.

Write \(u_L=a_LS'^M+c_L\), \(\deg c_L<M\), and define the old-degree polynomial and its fixed quotient coordinate
\[
w_L^{\rm old}=c_L+a_L\sum_{j<M}a_j^{\rm proj}S'^j,\qquad
r_L=\pi_{L-1}w_L^{\rm old}\in\mathbb C^g.
\tag{CL8}
\]
Thus \(u_L=a_Lp_M+w_L^{\rm old}\). Let \(\mathcal L_{L-1}\) be the minimum section of the old quotient \(Q_{L-1}\), and put
\(w_L=\mathcal L_{L-1}r_L\).
Orthogonal projection of \(u_L\) away from every old relation gives exactly
\[
v_L=(I-P_{\operatorname{span}(u_0,\ldots,u_{L-1})})u_L
=a_Lp_M+w_L.
\]
The two terms are orthogonal, since \(p_M\) is orthogonal to the entire previous polynomial space. Therefore the original relation innovation satisfies
\[
\boxed{\rho_L=\|v_L\|_H^2
=|a_L|^2\nu_M+r_L^*Q_{L-1}r_L.}
\tag{CL9}
\]
It equals \(\det R_L/\det R_{L-1}\) by the Schur determinant formula for the complete relation Gram. At \(L=0\), the previous relation space is zero and the same formulas apply.

A low quotient vector \(x\in\mathbb C^g\), after the old relation minimum, has lift \(\mathcal L_{L-1}x\). Its new minimum additionally varies along \(v_L\), so it minimizes
\[
\|\mathcal L_{L-1}x+t w_L\|_H^2+|ta_L|^2\nu_M
\]
over \(t\in\mathbb C\). Expanding and completing the scalar square proves
\[
\boxed{
Q_L=Q_{L-1}
-\frac{Q_{L-1}r_Lr_L^*Q_{L-1}}{\rho_L},\qquad
Q_L^{-1}=Q_{L-1}^{-1}
+\frac{r_Lr_L^*}{|a_L|^2\nu_M}.}
\tag{CL10}
\]
The first formula is a positive rank-at-most-one decrease of the actual graph metric. The second follows by multiplying the two displayed matrices and using CL9. It also proves positive definiteness directly.

The exact observation of \(p_M\) is
\[
f_M=\ell(p_M)=b_M-B_{M-1}H_{M-1}^{-1}h_M
=-A_Rr_L/a_L.
\tag{CL11}
\]
Indeed CL4 applied to \(u_L=a_Lp_M+w_L^{\rm old}\), followed by CL5, gives the last equality, retaining its sign and complex phase. Consequently
\[
C_M=A_RQ_L^{-1}A_R^*
=C_{M-1}+f_Mf_M^*/\nu_M,\qquad
s_M=f_M^*C_{M-1}^{-1}f_M/\nu_M\ge0,
\tag{CL12}
\]
and \(\det C_M/\det C_{M-1}=1+s_M\). This is CI5–7 on exactly the original functional extension.

## 3. The positive kernel loss and its exact allocation

Let \(\mathcal K=\ker A_R\) in the fixed low coefficient space, and let \(E_K\) be its fixed full-rank frame. Its dimension is
\[
h=g-r=m-s_k,\qquad s_k=\dim(K\cap\mathcal P_{<v}),
\]
rather than the full original \(m\) when the low intersection is nonzero. Use the old metric \(Q=Q_{L-1}\), and let \(P_{\mathcal K}^{Q}\) be its orthogonal projection. The attained observation formula gives
\[
\|r_L\|_Q^2
=\|P_{\mathcal K}^{Q}r_L\|_Q^2+
(A_Rr_L)^*(A_RQ^{-1}A_R^*)^{-1}(A_Rr_L).
\]
By CL11–12 the last term is \(|a_L|^2\nu_Ms_M\). Insert this in CL9:
\[
\boxed{\rho_L=|a_L|^2\nu_M(1+s_M)
+\|P_{\mathcal K}^{Q}r_L\|_Q^2.}
\tag{CL13}
\]
This proves the stronger source-level allocation and its inequality before taking any determinants.

Restrict CL10 to \(E_K\). The rank-one determinant identity gives
\[
\frac{\det(E_K^*Q_LE_K)}{\det(E_K^*QE_K)}
=1-\frac{\|P_{\mathcal K}^{Q}r_L\|_Q^2}{\rho_L}.
\]
Use CL13 to obtain the exact loss
\[
\boxed{
\begin{aligned}
d_L&=\frac{\det(E_K^*Q_{L-1}E_K)}{\det(E_K^*Q_LE_K)}
=\frac{\rho_L}{|a_L|^2\nu_{g+L}(1+s_{g+L})}
\\&=1+\frac{\|P_{\mathcal K}^{Q_{L-1}}r_L\|_{Q_{L-1}}^2}
{|a_L|^2\nu_{g+L}(1+s_{g+L})}\ge1.
\end{aligned}}
\tag{CL14}
\]
Equality holds precisely when the new old-degree relation component \(r_L\) has no component in the actual residual kernel. The observation covariance may grow even when \(d_L=1\); the exact decomposition CL13 records both effects. All formulas include empty kernels or observations with determinant one and the zero projection.

For comparison with CI11–13, the full polynomial basis
\([1,\ldots,S'^{g-1},u_0,\ldots,u_L]\)
has determinant \(\prod_{j=0}^La_j\). Its full Gram determinant followed by the relation Schur complement gives
\[
\det Q_L=\frac{\prod_{j=0}^L|a_j|^2\det H_{g+L}}{\det R_L}.
\]
Choose any fixed right inverse \(J\) of \(A_R\), and set \(T=[E_K,J]\). The second Schur determinant gives
\[
\det(E_K^*Q_LE_K)=|\det T|^2\det Q_L\,\det(A_RQ_L^{-1}A_R^*).
\tag{CL15}
\]
Taking adjacent ratios reproduces CL14. The fixed frame factor is explicitly present and cancels. Thus both independent derivations give exactly the signs and denominator in CI14.

## 4. All four cutoffs and the precise original-kernel receiver

Let \(K_L=E_K^*Q_LE_K\), \(Q_{-1}=H_{g-1}\).
The four original values of \(L\) are \(-1,0,q-1,q\).
Telescoping each low/high pair separately proves
\[
\boxed{
\mathcal R\log\det K_L
=\log d_0+2\sum_{L=1}^{q-1}\log d_L+\log d_q.}
\tag{CL16}
\]
All terms are nonnegative by CL14. The coefficient two is the overlap of the two exact intervals; it is not a multiplicity convention. The same argument applied to CL12 gives
\[
\mathcal R\log\det C_M
=-\log(1+s_g)-2\sum_{j=g+1}^{g+q-1}\log(1+s_j)
-\log(1+s_{g+q}).
\tag{CL17}
\]
The source prefix property proved in CL3–5 is what makes both telescoping identities and covariance monotonicity valid.

Finally, the exact map to the original physical kernel is KF44:
\[
\Psi_N:V_A/\mathcal P_{<v}\longrightarrow
Y_N=\mathcal P'_{\le g+L}/\mathcal U_A\mathcal P_{\le L},
\qquad[p]\longmapsto[\mathcal T_Ap/\chi'].
\]
For the unique degree-below-\(q\) representative of any original class, this target has degree below \(g\). Thus its coefficient vector is independent of \(N\), as proved in KF7 and44–45. Its actual image of \(K/(K\cap\mathcal P_{<v})\) is exactly \(\ker A_R\) by CG29–30. The metric of this image is precisely \(K_L\), the full Schur minimum KF51.

Therefore [KF49](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex) gives, with all its actual finite guards,
\[
\left|\mathcal R\log\det H_{K,N}^{\rm ar}
-\left(\log d_0+2\sum_{L=1}^{q-1}\log d_L+\log d_q\right)\right|
\le\mathcal E_{\rm KF49},
\]
\[
\mathcal E_{\rm KF49}
=2mL_k^{\rm form}+2s_k\log\kappa_k^*
+2B_k^{\rm ang}+2\sum_{N=q-1,q,2q-1,2q}E_N^*.
\tag{CL18}
\]
The original source mass, the \(v\)-dimensional low space, its intersection and angle, and the full conductor exterior transport all remain. The accompanying finite-determinant proof applies the sharper NG2 comparison to this same source. Thus its explicit width \(\Lambda_k=\log(u_k/\ell_{k,2q})\) replaces \(L_k^{\rm form}\) here; every other displayed term remains.

Thus CI5–16 contains no mathematical defect in the loss ratio or cutoff embedding. The precise scope is the actual residual graph-kernel metric, of rank \(m-s_k\); equality with an individual original physical cutoff loss is not asserted. CL18 is the proved four-cutoff transfer to that original kernel.

## Source reading and scope

The complete accompanying CUTOFF_INNOVATION_PROOFS.md was read. The original TeX [CG1–32](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/COMPLETE_CONDUCTOR_GRAPH_METRIC.tex) was read, with CG28–32 reread directly. KF1–17 and KF33–55 were read, with KF3–10 and41–49 the decisive maps. No additional external theorem or human-source result is imported by this finite derivation; its weighted source is the unchanged one in those original proofs. No duplicate checker was run and no frozen IC file was changed.

