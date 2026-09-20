# Constant-depth recovery and a linear-rank arithmetic leakage bound

Research continuation, 19 September 2026.

## Original domain and inputs

This calculation stays on the simple-quartet period locus of the original
O1–12 observability proof, with every original unit and period factor in
`H`. It uses that proof's full-edge conductor support and its nonzero
primitive-column tests. In particular this locus contains its stated fixed
large-period domain `|u| >= R_det`. The original degrees are
\(k\equiv1\pmod4\), \(k\ge74\), so the first integer on this sequence is 77.
The five-orbit rank formula gives \(\dim\ker\Lambda_k=8k-16\).
The new result below improves the prior `8k-15` observations to at most 81,
and propagates the explicit inverse through the actual NP action blocks.
It does not replace a one-step observation by an isometry of its kernel.

The source references are the local incoming proof
`Programme_Native_Continuation_20260919/proof/04_FULL_ORIGINAL_OBSERVABILITY.md`
and the pinned GitHub NP15–24 equations in
`20260919-native-precision-leakage/NATIVE_PRECISION_AND_LEAKAGE.tex`, commit
`1445091fd84d47b3908f56d4db1f8a28acd134da`.

## 1. Fixed conductor support and the missing corners

Let
\[
E_k=\mathbb C[S]/(\chi_k),\quad q=(k+1)^2,\qquad
\lambda_{ab}=k/2+(2a-k)\delta+i(2b-k)\gamma,
\]
where the full simple root polynomial and the original multiplication
\(A=M_S\) are unchanged. Its value-coordinate isomorphism is
\(\mathsf V_k:E_k\to\mathbb C^{\{0,\ldots,k\}^2}\); its inverse sends a
coordinate vector to the corresponding original Lagrange idempotent.

Retain the fixed original conductor biform
\[
\mathcal A(Z,W)=\sum_{\sigma\in\mathcal S}a_\sigma
Z^{\sigma_1}W^{\sigma_2},\quad
\mathcal S\subset\{0,\ldots,8\}^2,\quad a_\sigma\ne0,
\quad s=|\mathcal S|\le81.
\tag{DO1}
\]
The set \(\mathcal S\) is its actual support. No coefficient is declared
nonzero solely from a bidegree. Define
\[
F_k=\mathcal S+\{0,\ldots,k-8\}^2,\quad
C_k=\{0,\ldots,k\}^2\setminus F_k,\quad h=|C_k|.
\tag{DO2}
\]
On the retained full-edge-support locus,
\[
\boxed{h\le128.}\tag{DO3}
\]
For \(k\ge16\), the corner pattern, and hence \(h\), is independent of
\(k\) after indexing each corner by its distances from the two edges.

### Proof

For \(8\le b\le k-8\), the support contains a point \((0,b_0)\) and a point
\((8,b_1)\). The first reaches every \((a,b)\) with \(a\le k-8\); the second
reaches the remaining \(a\). Interchanging axes covers every \(8\le a\le k-8\).
Thus missing coordinates lie in four disjoint 8 by 8 corner blocks.

The single point \((0,b_0)\) already reaches \(8(8-b_0)\) cells in the lower
left corner and \(8b_0\) cells in the upper left corner. It therefore reaches
64 of their 128 cells, leaving at most 64. The point \((8,b_1)\) proves the
same count at the right corners. This proves DO3. The reachability tests
within a corner are inequalities between the support indices and distances
0 through 7, independent of \(k\). No generic full-support assumption is used.


There is a sharper count needed for joint corner recovery. Let \(h_i\) be
the missing sizes of the four corners. Then
\[
\boxed{\sum_i h_i-\max_i h_i\le64.}\tag{DO3a}
\]
Choose support points \((0,b_0),(8,b_1),(a_0,0),(a_1,8)\). The four missing
sizes are bounded respectively by
\(a_0b_0,a_1(8-b_0),(8-a_0)b_1,(8-a_1)(8-b_1)\).
Additional support only decreases them. The function sum minus maximum is
coordinatewise nondecreasing. Divide these four bounds by 64 and set
\(x=a_0/8,y=a_1/8,u=b_0/8,v=b_1/8\). Their sum is
\(1+(x-y)(u-v)\). For a nonpositive product the result is immediate.
For \(x\ge y,u\ge v\), the product is at most \(xu\); for
\(x\le y,u\le v\), it is at most \((1-x)v\). In every case subtracting
the largest of the four entries leaves at most one. This proves DO3a
without an enumeration assumption.

## 2. Recover every translated conductor coordinate with at most 81 iterates

For each \(\beta\in\{0,\ldots,k-8\}^2\), O3 constructs an original invariant
polynomial whose restriction to the original quadric is
\(\mathcal A Z^{\beta_1}W^{\beta_2}\). Explicitly, lift the biform monomial
to the original degree-\(k-8\) homogeneous polynomial, multiply it by the
four other orbit quadrics, and sum its five cyclic translates. The four
other translates contain the original quadric, so the restriction is
exactly the displayed biform, with no extra factor of five.

Let \(\ell_\beta\) be the corresponding complex-linear output functional.
The original coefficient-observation dictionary gives exactly
\[
\ell_\beta(\Lambda_k x)=
\sum_{\sigma\in\mathcal S}a_\sigma
(\mathsf V_kx)_{\beta+\sigma}.
\tag{DO4}
\]
For precision, in an original word frame \(F_0\) and invariant polynomial
coefficient row \(c_\beta^T\), this functional is the restriction of
\(c_\beta^T(F_0^*F_0)^{-1}F_0^*\) to \(\operatorname{im}\Lambda_k\).
The transpose in \(c_\beta^T\) is ordinary: this is a complex-linear
polynomial pairing. The full inherited Gram remains in the displayed
left inverse of \(F_0\).

For \(\sigma\in\mathcal S\), form the explicit degree-\(s-1\) polynomial
\[
\boxed{\displaystyle
p_{\beta,\sigma}(S)=
\prod_{\tau\in\mathcal S\setminus\{\sigma\}}
\frac{S-\lambda_{\beta+\tau}}
{\lambda_{\beta+\sigma}-\lambda_{\beta+\tau}}.}
\tag{DO5}
\]
Its denominators are precisely
\[
2\delta(\sigma_1-\tau_1)+2i\gamma(\sigma_2-\tau_2)\ne0.
\]
They are fixed original root differences, independent of \(k\) and \(\beta\).
For actual data \(y_n=\Lambda_k A^n x\), DO4 yields
\[
\boxed{\displaystyle
(\mathsf V_kx)_{\beta+\sigma}
=\frac1{a_\sigma}\sum_{n=0}^{s-1}
[S^n]p_{\beta,\sigma}(S)\,\ell_\beta(y_n).}
\tag{DO6}
\]
Indeed applying DO4 to \(p_{\beta,\sigma}(A)x\) kills every other translated
support coordinate. This is recovery of all values in \(F_k\), not merely
nonvanishing of their observation columns.
Choose one ordered representation \(\alpha=\beta+\sigma\) for each
\(\alpha\in F_k\). DO6 is then a specified linear recovery map.

## 3. The original observation is jointly injective on each corner

The O5 proof supplies more than separate nonzero columns. On each original
primitive corner it spans the entire jet algebra of total degree at most
14, using invariant polynomials of degree at most 74. Every coefficient
with the two corner distances at most 7 is among those jets. Consequently
the restriction of the original observation to **all** coordinate vectors
supported on any one corner is injective. This follows by pairing with the
full spanning jet family, not merely by counting nonzero columns.

For completeness, the local invariant coordinates used there are
\(z_{j_0}^5\) and \(z_jz_{j_0}^{d_j}\), with
\((j-i)+d_j(j_0-i)=0\pmod5\), where two original Fourier coordinates are
active. Their triangular ambient Jacobian is invertible; two restrictions
have independent differentials on the original Segre surface. A charge
unit times their centered monomials through total degree 14 spans all
those jets. Homogenization to degree \(k\) is an original invariant lift;
its nonzero local factor is an invertible jet multiplication. This is the
same O5 map at the same fixed period, now used on the whole corner at once.

Write \(B_i=(\Lambda_k e_\alpha)_{\alpha\in C_i}\) for the columns of a
nonempty missing corner. At a fixed original cutoff \(N\), retain
\(Q_N=(\Lambda_kG_N^{-1}\Lambda_k^*)^{-1}\). The just-proved injectivity gives
\[
J_i=(B_i^*Q_NB_i)^{-1}B_i^*Q_N,\qquad J_iB_i=I_{h_i}.
\tag{DO7}
\]
This inverts the entire corner Gram, of size at most 64, not the separate
norms of its columns.

Subtract the recovered values in \(F_k\) from all available observations:
\[
\widetilde y_n=y_n-\sum_{\alpha\in F_k}
\lambda_\alpha^n(\Lambda_k e_\alpha)(\mathsf V_kx)_\alpha.
\]
Order the remaining corners by decreasing size, with a fixed order for ties.
At the current stage let \(C'\) be the still unrecovered coordinates and
choose its largest corner \(C_i\). Define
\[
p_i(S)=\prod_{\beta\in C'\setminus C_i}(S-\lambda_\beta),\qquad
r_i=\deg p_i.
\]
Initially \(r_i=h-\max h_i\le64\), by DO3a. After that step all remaining
coordinates number at most 64, so every subsequent \(r_i\le64\) as well.
All values of \(p_i\) at \(C_i\) are nonzero. The exact recovery is
\[
\boxed{\displaystyle
((\mathsf V_kx)_\alpha)_{\alpha\in C_i}
=\operatorname{diag}(p_i(\lambda_\alpha))_{\alpha\in C_i}^{-1}
J_i\sum_{n=0}^{r_i}[S^n]p_i(S)\,\widetilde y_n.}
\tag{DO8}
\]
The polynomial first annihilates every other unrecovered corner. The
remaining vector is exactly \(B_i\operatorname{diag}(p_i(\lambda_\alpha))x_i\).
After DO8, subtract this corner's known contribution from each
\(\widetilde y_n\) and repeat. There are at most four steps. No period,
source, or original observation is changed.

Put \(d=\max\{s-1,h-\max_i h_i,1\}\), with the corner term zero when
\(h=0\). Then \(d\le80\). DO6 and DO8, followed by \(\mathsf V_k^{-1}\),
give an explicit left inverse \(\mathcal R_{d,N}\) of the **original** stack
\(\mathcal O_d=(\Lambda_k,\Lambda_k A,\ldots,\Lambda_k A^d)^T\). Thus
\[
\boxed{\displaystyle
\mathcal R_{d,N}\mathcal O_d=I_{E_k},\qquad
\bigcap_{n=0}^{80}\ker(\Lambda_k A^n)=0.}
\tag{DO9}
\]
At most 81 observations are needed, independent of tensor degree. This
does not assert \(\ker\Lambda_k=0\), whose actual dimension is \(8k-16\).

## 4. A finite bound in the original metrics

Use the actual \(Q_N\) norm on outputs and Euclidean norm on root values.
Let \(R_k=\max|\lambda_\alpha|\), \(M_k=\max(1,R_k)\),
\(\delta_0=2\min(\delta,\gamma)\), and
\[
C_F=\frac1{\min_{\sigma\in\mathcal S}|a_\sigma|}
\left(\frac{1+R_k}{\delta_0}\right)^{s-1}
\max_\beta\|\ell_\beta\|_{Q_N^*},\qquad
b_+=\max_\alpha\|\Lambda_k e_\alpha\|_{Q_N}.
\]
Every local Lagrange coefficient one-norm is bounded by the displayed
product of \(1+R_k\) over the retained nonzero root differences. Hence
\(\|x_F\|_2\le\sqrt q C_F\|y\|_{Q_N^{\oplus(d+1)}}\).
The first residual stack has norm at most
\[
R_0\|y\|,\qquad
R_0=1+\sqrt{d+1}\,q b_+M_k^d C_F.
\]
For each of the at most four ordered corners set
\[
c_i=\lambda_{\min}(B_i^*Q_NB_i)^{-1/2}
\left(\frac{1+R_k}{\delta_0}\right)^{r_i},\qquad
n_i=\sqrt{d+1}\,M_k^d\|B_i\|_{\ell^2\to Q_N}.
\]
The inverse diagonal in DO8 has norm at most \(\delta_0^{-r_i}\), and the
filter's coefficient one-norm at most \((1+R_k)^{r_i}\), proving
\(\|x_i\|\le c_i\|\widetilde y\|\). Subtracting its contribution gives
\(\|\widetilde y_{\rm next}\|\le(1+n_ic_i)\|\widetilde y\|\).
Consequently the full root-value inverse has the finite bound
\[
\boxed{\displaystyle
C_{\rm root,N}=\sqrt q C_F+
R_0\sum_i c_i\prod_{l<i}(1+n_lc_l).}
\tag{DO10}
\]
The sum is empty at \(h=0\). Return through the exact original
value-to-polynomial map:
\[
\|\mathcal R_{d,N}\|_{Q_N^{\oplus(d+1)}\to G_N}
\le C_{d,N}:=\|\mathsf V_k^{-1}\|_{\ell^2\to G_N}C_{\rm root,N}.
\tag{DO11}
\]
These are finite constants in the original metrics. No bound in the
inherited period-output metric has been substituted for a bound in
\(Q_N\), and no small asymptotic condition number is asserted. An exact,
potentially sharper constant is the operator norm of the explicit matrix
DO6–8 with these same domain and codomain metrics.

## 5. Constant-depth original kernel leakage

Retain all NP15–16 maps at this same original cutoff:
\[
I:\mathbb C^r\to K_k,\quad H_K=I^*G_NI,\quad
L=G_N^{-1}\Lambda_k^*Q_N,\quad J_K=H_K^{-1}I^*G_N,
\]
\[
T=J_KAI,\ C=J_KAL,\ B=\Lambda_k AI,\ D=\Lambda_k AL.
\tag{DO12}
\]
The frame \([I,L]\) is an isometry from \(\operatorname{diag}(H_K,Q_N)\)
to \(G_N\), and the action block matrix is exactly
\(\left(\begin{smallmatrix}T&C\\B&D\end{smallmatrix}\right)\).
Neither cross block is removed.

For \(x\in\mathbb C^r\), write \(y_j=\Lambda_k A^jIx\). The block recursion
eliminates the kernel coordinate to give
\[
y_{j+1}=BT^jx+Dy_j+
\sum_{l=0}^{j-1}BT^{j-1-l}Cy_l,\qquad y_0=0.
\tag{DO13}
\]
Let \(W_d\) be the d by d lower triangular block matrix mapping
\((BT^jx)_{j=0}^{d-1}\) to \((y_1,\ldots,y_d)\) by this recursion. Its diagonal
is the identity, and subtraction in DO13 is its exact inverse.
The new short-stack identity implies
\[
\boxed{\displaystyle
\sum_{j=0}^{d-1}(T^j)^*B^*Q_NBT^j
\succeq (C_{d,N}\|W_d\|_{Q_N^{\oplus d}})^{-2}H_K\succ0.}
\tag{DO14}
\]
Proof: apply \(\mathcal R_{d,N}\) to
\(\mathcal O_dIx=(0,W_d(BT^jx)_{j<d})\), then use DO11 and square the
actual metric norms. There is no characteristic-polynomial compression
or additional `C_T` factor as in the earlier NP24 argument.

For an elementary finite bound put \(M_N=\max(1,\|A\|_{G_N})\). Each of
\(T,C,B,D\), with the stated domain and codomain metrics, has norm at most
\(M_N\). The feedback coefficients at lag \(p\) are \(D\) at zero and
\(BT^{p-1}C\) at \(p\ge1\), with norms at most \(M_N^{p+1}\).
The recursion for the inverse-feedback coefficients gives inductively
\(\|W_{d,n}\|\le(2M_N)^n\). Summing the d diagonal-block norms proves
\[
\|W_d\|\le d(2M_N)^{d-1}.
\tag{DO15}
\]
This value can be inserted into DO14. The original rank-two source action
also gives the finite estimate
\(\|A\|_{G_N}\le k/2+C_{\rm mult}(h)(2N+\lfloor k/3\rfloor)+\kappa_N\),
with the existing full-source constants and the original boundary radius;
HG22 supplies its explicit upper bound on the original window.

Most importantly, DO14 evaluates a new algebraic property of the actual
one-step leakage. The d-block matrix \((B,BT,\ldots,BT^{d-1})^T\) has rank r,
but has rank at most \(d\,\operatorname{rank}B\). Therefore
\[
\boxed{\displaystyle
\operatorname{rank}(\Lambda_k AI)
\ge\left\lceil\frac{8k-16}{d}\right\rceil
\ge\left\lceil\frac{8k-16}{80}\right\rceil.}
\tag{DO16}
\]
Thus the actual action leakage has a rank growing at least linearly with
tensor degree on this original period locus. This strengthens the earlier
nonzero-leakage conclusion; it does not calculate its individual singular
values or the sign of its pairing with a specified eigenclass.


There is a further exact consequence for both mixed action directions.
The original attained-source identity RBE4 is
\[
\mathsf T_N A\mathsf T_N^{-1}
=kI/2+i\mathsf J_N+\widehat b_{N+1}\widehat b_N^*/\omega_N,
\]
with \(\mathsf J_N\) Hermitian in the original source norm. Hence the full
relative Hermitian weight has rank at most two. In the isometric block
frame of DO12, define
\[
\widetilde B=Q_N^{1/2}BH_K^{-1/2},\qquad
\widetilde C=H_K^{1/2}CQ_N^{-1/2}.
\]
Its mixed weight block is exactly
\[
\boxed{\widetilde C+\widetilde B^*=R_N,\qquad
\operatorname{rank}R_N\le2.}\tag{DO17}
\]
Therefore the same original return direction satisfies
\[
\operatorname{rank}C\ge\left\lceil\frac{8k-16}{80}\right\rceil-2.
\]
For the original metric projection \(P_{K,N}=IJ_K\), its action commutator
has block matrix \(\left(\begin{smallmatrix}0&-C\\B&0\end{smallmatrix}\right)\).
The two output summands are disjoint, so its rank is the sum of their ranks:
\[
\boxed{\displaystyle
\operatorname{rank}[A,P_{K,N}]
\ge2\left\lceil\frac{8k-16}{80}\right\rceil-2.}\tag{DO18}
\]
On \(\ker R_N\), a subspace of codimension at most two in the observation
block, the equality \(\widetilde C=-\widetilde B^*\) is exact. Thus the
rank-two Hermitian weight and the growing-rank two-way action leakage
are related by the displayed cancellation; neither cross direction
can be omitted on account of the full weight's rank.


### A sharper rank calculation from eight differentiated conductor rows

The original coefficient dual of \(A\) on degree-\((k,k)\) biforms is
\[
\eta_k+\mathcal D,\qquad
\eta_k=k(1/2-\delta-i\gamma),\qquad
\mathcal D=2\delta Z_1\partial_{Z_1}+2i\gamma W_1\partial_{W_1}.
\tag{DO19}
\]
Its value on \(Z_0^{k-a}Z_1^aW_0^{k-b}W_1^b\) is exactly
\(\lambda_{ab}\). The two spans of powers through any fixed order are
related by the inverse binomial transformations
\((\eta_k+\mathcal D)^j=\sum_{l\le j}\binom jl\eta_k^{j-l}\mathcal D^l\)
and
\(\mathcal D^j=\sum_{l\le j}\binom jl(-\eta_k)^{j-l}(\eta_k+\mathcal D)^l\).
Thus no different arithmetic action is substituted.

Homogenize the same conductor as a biform of degree \((8,8)\). Full edge
support excludes all four coordinate variables as factors. Each
irreducible factor \(F\) is bihomogeneous. If \(F\mid\mathcal DF\), equality
of its two degrees makes the quotient a scalar. But the \(\mathcal D\)
weights of distinct monomials of a fixed bidegree are distinct: their
real and imaginary parts distinguish both indices, since
\(\delta,\gamma>0\). Such an eigen-polynomial is a monomial. An irreducible
monomial is one coordinate variable, already excluded. Hence
\(F\nmid\mathcal DF\) for every factor of the actual conductor.

If \(F^e\) is its exact power in \(\mathcal A\), then \(e\le8\), because
at least one of the bidegrees of \(F\) is positive. Repeated product
differentiation gives, for \(j\le e\),
\[
\mathcal D^j\mathcal A
=(e)_{\underline j}F^{e-j}(\mathcal DF)^j(\mathcal A/F^e)
\pmod {F^{e-j+1}}.
\]
The displayed coefficient is nonzero modulo \(F\). In particular
\[
\gcd(\mathcal A,\mathcal D\mathcal A,\ldots,\mathcal D^8\mathcal A)=1.
\tag{DO20}
\]
This includes every repeated conductor factor; no squarefreeness is assumed.

A specified pair of coprime biforms can now be selected finitely. Put
\(B_t=\sum_{j=1}^8t^{j-1}\mathcal D^j\mathcal A\). For each irreducible
factor of \(\mathcal A\), its reduction is a nonzero polynomial in \(t\)
of degree at most seven, by DO20. There are at most sixteen distinct factors.
At most 112 complex numbers are therefore forbidden. Choose the first
integer \(t\in\{0,\ldots,112\}\) for which the actual gcd is one. Its
existence has just been proved, and the selection retains the fixed
original coefficients. Write the selected biform as \(B\).

Let \(\mathcal W_k\) be the original invariant coefficient image. It
contains \(\mathcal A T_{k-8,k-8}\). Product differentiation, and induction
on the derivative order, show that
\((\mathcal D^j\mathcal A)T_{k-8,k-8}\) is contained in
\(\sum_{n=0}^j\mathcal D^n\mathcal W_k\): isolate its last product-rule
term and use that \(\mathcal D\) preserves every biform degree.
Consequently the row space of the original stack through \(A^8\) contains
\[
\mathcal A T_{k-8,k-8}+B T_{k-8,k-8}.
\]
The full kernel of the map \((f,g)\mapsto\mathcal Af+Bg\) is
\((Bh,-\mathcal Ah)\). This follows by gcd cancellation in the polynomial
UFD and retains both bidegrees. For \(k\ge16\), its cokernel dimension is
therefore exactly
\[
(k+1)^2-2(k-7)^2+(k-15)^2=128.
\]
Hence the **actual original** eight-step invisible space satisfies
\[
\boxed{\displaystyle
\dim\bigcap_{j=0}^8\ker(\Lambda_k A^j)\le128.}
\tag{DO21}
\]
This uses the conductor ideal as a row-space inclusion; it does not assert
that the conductor rows exhaust the original observation.

Apply the exact feedback map DO13 through eight steps. On the original
kernel of dimension \(r=8k-16\), the rank of
\((B,BT,\ldots,BT^7)^T\) is at least \(r-128\), by DO21, and at most
\(8\operatorname{rank}B\). Thus the earlier rank bound improves to
\[
\boxed{\displaystyle
\operatorname{rank}(\Lambda_k AI)\ge k-18.}
\tag{DO22}
\]
It applies on the common original domain above, where \(k\ge77\).
Combining with the exact rank-two mixed-weight identity DO17 gives
\[
\boxed{\displaystyle
\operatorname{rank}(J_KAL)\ge k-20,\qquad
\operatorname{rank}[A,P_{K,N}]\ge2k-38.}
\tag{DO23}
\]
These are ranks of the original action and original metric projection,
not of a substituted coefficient section. The first eight leakage steps
leave at most 128 invisible directions; the explicit at-most-81-step
inverse DO9 removes all of them. The original metrics and their finite
comparison constants still occur in DO14.

## 6. Receiving boundary

The single-step kernel, its full metric, and the actual projected-current
numerators remain those of HG6–7. DO9 gives recovery only after applying the
displayed stack, and its exact inverse and metric cost are DO6–11. It must
not be inserted as \(\theta_N=0\) in a one-step response.

Likewise DO14 is an original arithmetic leakage estimate in \((H_K,Q_N)\).
It does not assert preservation of the different coefficient-cone spaces,
or identify the proper-source target minimum with this stack. The original
PRD source-kernel vanishing is the separate NC22 result, and its remaining
target subtraction in NP30–31 is unaffected.
