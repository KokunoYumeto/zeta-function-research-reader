# Full original packet recovery from iterated observation

19 September 2026. This continues AKS/AKJ on the original simple-quartet five-orbit period domain. It concerns K=ker Lambda itself. It does not replace K by the arithmetic residue image im L. The full period, branch, and arithmetic unit are in the matrix H throughout.

## 1. Every original column has a concrete coefficient test

Put q=(k+1)^2 and r=8k-16. Let B denote the complex-linear coefficient matrix of the original ordered output polynomials (Hermitian adjoints occur only in Gram matrices). In the original root-value coordinates Lambda has matrix F_0 B, where

\[
\Theta_k f=f(H(ZW,Z,W,1)^T),\qquad f\in S_k^G,
\]

and the coefficient of Z^a W^b in this literal substitution is the (output word,(a,b)) entry of B. Equivalently, B^T is its complex-linear dual coefficient map; a stored adjoint convention is conjugated before this identification. The complete inherited word Gram obeys G_0>=5^k I, with the unscaled word multiplicities counted once. For the root idempotent e_{ab},

\[
\Lambda e_{ab}\ne0
\quad\Longleftrightarrow\quad
[Z^aW^b]\Theta_k f\ne0\text{ for some }f\in S_k^G.
\tag{O1}
\]

Since the original arithmetic A is diagonal in these root idempotents, its permanently invisible submodule is exactly

\[
K_\infty=\bigcap_{j=0}^{q-1}\ker(\Lambda A^j)
=\operatorname{span}\{e_{ab}:Be_{ab}=0\}.
\tag{O2}
\]

The equality follows either from the original Vandermonde in the q distinct roots or from its explicit Lagrange polynomials. No invariant-subspace assumption is made about the one-step kernel K.

## 2. The conductor detects every column except a fixed corner set

Retain the actual conductor biform A(Z,W), of bidegree (8,8), and the original inclusion

\[
A T_{k-8,k-8}\subset\Theta_k(S_k^G).
\tag{O3}
\]

The lift in (O3) is explicit. Choose a homogeneous lift h of a biform of degree (k-8,k-8), multiply by the actual product Acal=Q_1Q_2Q_3Q_4, and take sum_{j=0}^4 g^j(Acal h). Its restriction to Q=0 is exactly A times the chosen biform: all the other four terms contain Q.

Use the actual full-edge-support locus: A(0,W), the coefficient of Z^8, A(Z,0), and the coefficient of W^8 are all nonzero polynomials. RPK supplies explicit nonzero gates and a finite sufficient fixed-period radius for this locus.

For 8<=b<=k-8 and any a, choose a nonzero coefficient a_{0,s} when a<=k-8, and a_{8,s} when a>k-8. The monomial Z^{a-r}W^{b-s} has both exponents between zero and k-8. Its product with A has (a,b) coefficient exactly a_{r,s}, so that column in (O1) is nonzero. Interchanging the axes treats every a in [8,k-8] and any b.

Consequently, on this exact locus and k>=16,

\[
\boxed{\dim K_\infty\le256.}
\tag{O4}
\]

All possibly invisible columns lie in the four 8-by-8 corners. This bound uses actual edge coefficients, not only the overall observation rank.

## 3. Original primitive period columns with two active coordinates detect all corner jets

At a corner, use its original affine Segre coordinates (Z,W) centered at that corner. Then p=H e_alpha is the corresponding original primitive period column, including its unit. Choose an active coordinate i, and an active j_0 different from i. Let z_j=x_j/x_i.

The following three invariant projective functions form local coordinates in the ambient projective chart:

\[
T_0=z_{j_0}^5,
\qquad
T_j=z_jz_{j_0}^{d_j}\quad(j\ne i,j_0),
\]

where 0<=d_j<=4 and (j-i)+d_j(j_0-i)=0 mod5. Their Jacobian in the three z coordinates is triangular with nonzero diagonal 5z_{j_0}^4 and z_{j_0}^{d_j}. The original Segre chart is an immersion, so two of these functions, say T_1,T_2, have a nonzero two-by-two derivative minor on it. Their formal restrictions are therefore invertible local coordinates.

For r=-ki mod5 choose 0<=c<=4 with c(j_0-i)=r and L_r=z_{j_0}^c. The jets

\[
L_r[T_1-T_1(0)]^a[T_2-T_2(0)]^b,
\qquad a+b\le14,
\tag{O5}
\]

span the full degree-less-than-15 jet algebra at this point. This follows by composing the invertible formal coordinate change and multiplying by the unit L_r. Each polynomial has degree at most 74. After homogenization by x_i to degree k, it is an original invariant polynomial. Multiplication by the unit x_i(Z,W)^k preserves the whole jet algebra.

Every corner coefficient with both distances at most seven has total order at most fourteen. Thus (O5), with k>=74, supplies a test polynomial for each such coefficient. With (O4),

\[
\boxed{K_\infty=0\quad(k\ge74)}
\tag{O6}
\]

on the full-edge-support locus with two active entries in every primitive period column.

## 4. This locus contains an explicit original large-period domain

Write the original PCL factorization as

\[
H(u)=e^{\mathfrak a/u}G_u R(u^{-1})V^{-1}U.
\]

The scalar and G_u are invertible. At z=0, the third and fourth coordinates of R(0)V^{-1}Ue_alpha are

\[
U_\alpha\,w_\alpha/h_c'(w_\alpha),\qquad
U_\alpha/h_c'(w_\alpha).
\]

Both are nonzero for every original root, since the roots are simple, w_alpha is nonzero, and the complete unit is invertible. Let C_R=sum_{n>=1}||R_n||_1, which is finite by PCL. Define

\[
sigma_* =\min_{\alpha,\,j=3,4}
\frac{|(R(0)V^{-1}Ue_\alpha)_j|}{||V^{-1}Ue_\alpha||_1}>0.
\]

For

\[
R_{det}=\max\{R_{\operatorname{rank}},1,2C_R/sigma_*\},
\tag{O7}
\]

both selected coordinates remain nonzero at every original fixed period |u|>=R_det. R_rank is the original explicit full-edge-support radius from RPK. No period is varied while k grows.

More generally multiply the original RPK edge gates by all eight selected third/fourth-coordinate functions. This is a nonzero entire function of z=1/u, nonzero at zero. Its zero set on |z|<=R_*^{-1} is finite. Outside that explicitly specified finite exceptional superset in the original period domain, (O6) holds. At a gate zero its actual support and column coordinates must still be checked; the gate does not assert failure.

## 5. Finite exceptional corner tests are eventually periodic

On a full-edge-support period with a one-active-coordinate corner, choose the active i and work in the finite algebra

\[
A_{8,8}=C[Z,W]/(Z^8,W^8).
\]

Its maximal ideal has fifteenth power zero. Reduce charge-r ratio monomials using residues 0,...,4 and the three nilpotents z_j^5-z_j(0)^5, retaining total nilpotent degree at most fourteen. Every resulting ratio polynomial has degree at most 82. For k>=82 its homogeneous invariant lifts are therefore present.

Write x_i(Z,W)=x_i(0)(1+h) with h nilpotent. Multiplication by the common factor x_i^k has matrix

\[
x_i(0)^k\sum_{j=0}^{14}\binom{k}{j}M_h^j.
\tag{O8}
\]

For a fixed k residue modulo five, the remaining fixed charge-jet matrix has no k dependence. Applying a selected corner coefficient functional to (O8) times that matrix gives a vector of polynomials in k of degree at most fourteen, times the nonzero scalar x_i(0)^k.

A corner column is permanently absent on that residue sequence exactly when every polynomial coefficient in that vector is zero. Otherwise its possible zeros lie among the finitely many roots of any selected nonzero entry polynomial. The explicit bound 1+max_{j<d}|c_j/c_d| bounds those roots. Thus dim K_infty is eventually periodic modulo five on each full-support period, with all remaining strata specified by fixed finite original-period matrices. On the locus (O6) its value is exactly zero.

## 6. Only r+1 observation iterates are needed for injectivity

Set K_j=intersection_{h=0}^j ker(Lambda A^h). These form a decreasing chain starting with dim K_0=r. If K_j=K_{j+1}, then A K_j is contained in K_j, because each of the first j+1 observations of Ax is zero. Such a plateau is an invariant submodule of the one-step kernel. On (O6) there is no nonzero such submodule. Every nonzero step therefore drops dimension, and

\[
\boxed{\bigcap_{j=0}^{r}\ker(\Lambda A^j)=0,
\qquad r+1=8k-15.}
\tag{O9}
\]

In particular K itself is not A-invariant. This proves that the original one-step observation quotient does not inherit that arithmetic action; it is a statement about the original K, not the distinct low residue image.

## 7. An explicit full-packet left inverse and its cost

Let b_lambda=Lambda e_lambda, nonzero on (O6), in the actual inherited output metric. Define the complex-linear functional

\[
\vartheta_\lambda(y)=\langle b_\lambda,y\rangle/||b_\lambda||^2.
\]

Write the original Lagrange idempotent as e_lambda(S)=sum_{j=0}^{q-1}e_{lambda,j}S^j. The full q-iterate observation has the explicit left inverse

\[
\boxed{(y_0,...,y_{q-1})\longmapsto
\sum_\lambda e_\lambda\sum_{j=0}^{q-1}e_{\lambda,j}\vartheta_\lambda(y_j).}
\tag{O10}
\]

For original data y_j=Lambda A^j x, its lambda value is vartheta_lambda(Lambda e_lambda(A)x)=x_lambda. This proves the map on all classes, including the formerly one-step invisible K.

A degree-uniform norm bound also follows from the explicit tests above. The conductor lift in (O3) has coefficient norm bounded by a fixed constant times h_-^{k-8}, because it uses the original degree-k Segre lift and a five-term character sum. Its selected nonzero conductor coefficient is a fixed scalar. The corner construction uses only five fixed inverse jet matrices at each of four corners. The inverse jet of x_i^k has coefficients bounded by C(1+k)^14 max(1,|x_i(0)|^{-1})^k. Thus there are finite fixed-period constants C_0,C_1 such that every column has

\[
||b_\lambda||\ge
\frac{5^{k/2}}{C_0(1+k)^{14}C_1^k}.
\tag{O11}
\]

The original word Gram lower bound gives the factor 5^{k/2}; no multinomial is counted twice. All constants refer to the fixed actual period and its nonzero coordinate/jet determinants. They are not asserted uniform as that period approaches an exceptional stratum.

Let d_*=2min(delta,gamma) and R_h=k sqrt(delta^2+gamma^2), eta=pi/4. The preceding original Lagrange source bound is

\[
B_{h,k}=2q(2q-2)!(\eta d_*)^{-2q+2}e^{\eta R_h}M_h(\eta)^k.
\]

The coefficient l1 norm of e_lambda is bounded by [(1+C_hk)/d_*]^{q-1}. Consequently the norm of (O10) into the original arithmetic minimum metric, uniformly for N>=q-1, is at most

\[
\sqrt{qB_{h,k}}
\left(\frac{1+C_hk}{d_*}\right)^{q-1}
\max_\lambda ||b_\lambda||^{-1}
=\exp[O_{h,u}(q\log(q+2))].
\tag{O12}
\]

The q-iterate inverse (O10)--(O12) and the shorter r+1-iterate injectivity (O9) are different statements; no unproved identical inverse norm is assigned to the shorter stack. The recovery cost is large. It does not provide a small action allowance, the absolute single-step kernel determinant, or a geometric Frobenius comparison.
