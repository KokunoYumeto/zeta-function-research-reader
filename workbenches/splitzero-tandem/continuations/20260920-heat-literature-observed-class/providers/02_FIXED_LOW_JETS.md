# Original observation: cofinal low-degree kernel ranks

19 September 2026. New algebraic calculation on the original simple-quartet five-orbit domain. The actual fixed period, branch, full unit, conductor order, and observation are retained. This does not evaluate the kernel's growing minimum Gram.

## 1. Original jet pairing

Let H be the original invertible one-factor matrix in AKS7, with the full period and unit. Put b_*=1/2-delta-i gamma and

\[
x(z)=H(e^{2(\delta+i \gamma)z},e^{2\delta z},e^{2i \gamma z},1)^T.
\]

For an invariant homogeneous polynomial f of degree k, its exact numerator is

\[
N_{k,f}(z)=e^{kb_*z}f(x(z)).
\]

Its pairing with P(S) is P(partial_z)N_{k,f}(0). Hence, for v=ord_0 E_A,

\[
t_0(k,u)=\dim(K_k\cap P_{v-1})
=v-\operatorname{rank}\{\text{first }v\text{ jets of all invariant }N_{k,f}\}.
\tag{J1}
\]

This is the full invariant image, not its already jet-vanishing subspace. Raw derivatives and divided Taylor coefficients are related by the invertible diagonal matrix diag(0!,..., (v-1)!). When v=0 the jet space is zero and t_0=0.

## 2. Five fixed finite matrices replace the growing-degree rank test

Choose the first i with x_i(0) nonzero and set z_j=x_j/x_i for j different from i. Multiplication on C[z]/(z^v) by

\[
e^{kb_*z}x_i(z)^k
\]

is an invertible linear map, with reciprocal multiplier as its explicit inverse. It is not asserted to be a ring automorphism. A homogeneous invariant monomial becomes this common multiplier times a monomial in the three ratios with charge

\[
r=-ki\pmod5,\qquad charge(z_j)=j-i\pmod5.
\]

For each r in Z/5Z form J_{r,v}(u): its rows are Taylor coefficients 0 through v-1, and its columns are

\[
z^\alpha\prod_{j\ne i}(z_j^5-z_j(0)^5)^{b_j},
\quad 0\le \alpha_j\le4,
\quad\sum_{j\ne i}(j-i)\alpha_j=r\pmod5,
\quad |b|\le v-1.
\tag{J2}
\]

There are 25 choices of alpha and at most binom(v+2,3) choices of b. Every column has polynomial ratio degree at most 5v+7.

Every ratio monomial has exponents alpha+5c. Expand each (z_j^5)^c around z_j(0)^5. Products of v vanishing factors have zero v-jet, so its jet is in the span of (J2). Conversely, every term of a column in (J2) can be homogenized by x_i to total degree k when k>=5v+7. Its charge is ki+r=0. Thus the spaces of jets agree in both directions, and

\[
\boxed{t_0(k,u)=v-\operatorname{rank} J_{-ki\bmod5,v}(u),\qquad k\ge5v+7.}
\tag{J3}
\]

The matrices in (J2) are independent of k. Their entries require only the first v coefficients of four specified exponential sums and the inverse of x_i(0). Explicitly, x_j^{(n)}(0) is the sum of H_{j,alpha} times the nth power of the four original exponents. A reciprocal Taylor series is computed recursively by b_0=1/a_0, b_n=-a_0^{-1}sum_{h=1}^n a_h b_{n-h}. Products in (J2) then use finite convolution. No new period is assigned.

The exact value is consequently periodic with period five in k once this finite threshold is reached, and with period twenty along k=1 mod4. Each exceptional stratum is specified by the actual minors of these five fixed matrices. This removes a growing-rank problem; it does not claim that those finite exceptional matrices have been numerically evaluated.

## 3. The two-active-coordinate stratum has t_0=0

Suppose the actual x(0) has at least two nonzero coordinates, and retain an active j_0 different from i. Its ratio z_{j_0}(0) is nonzero. The projective derivative of x is nonzero: otherwise invertibility of H would make (2delta+2i gamma,2delta,2i gamma,0) proportional to (1,1,1,1). Thus some z_j'(0) is nonzero.

If this z_j is a unit at zero, use T=z_j^5. Otherwise choose d in {0,...,4} with (j-i)+d(j_0-i)=0 mod5, and use T=z_j z_{j_0}^d. In either case T is an invariant ratio polynomial of degree at most five and T'(0) is nonzero. For the required charge r choose c in {0,...,4} with c(j_0-i)=r and put L_r=z_{j_0}^c.

The v columns

\[
L_r[T-T(0)]^h,\qquad 0\le h<v,
\]

have lower-triangular jets with determinant

\[
L_r(0)^v T'(0)^{v(v-1)/2}\ne0.
\]

Their degrees are at most 5v-1. Homogenization proves

\[
\boxed{t_0(k,u)=0\quad\text{on this actual stratum for } k\ge5v-1.}
\tag{J4}
\]

### The one-active-coordinate stratum has a smaller exact matrix and an explicit kernel class

At a one-active-coordinate point all three ratios z_j(0) vanish. A ratio monomial of total degree at least v therefore has zero v-jet. In (J3) the fixed matrix can be replaced by the columns
\[
z^\nu,\quad |\nu|<v,\quad
\sum_{j\ne i}(j-i)\nu_j=r\pmod5.
\tag{J3a}
\]
The equality t_0=v-rank of this smaller matrix holds already for k>=v-1. It has at most binom(v+2,3) columns, and retains the actual ratio derivatives.

There is also a concrete nonzero low polynomial in the kernel. Every original orbit quadric vanishes at this projective fixed point, so the four factors of the nonzero conductor each have positive order: v>=4. For r nonzero all charge-r monomials vanish at zero. Hence
\[
1\in K_k\quad(5\nmid k).
\]
For r=0, the invariant ratio polynomials have no linear monomial. Their numerator jets therefore satisfy N'(0)=k[b_*+x_i'(0)/x_i(0)]N(0), and
\[
S-k[b_*+x_i'(0)/x_i(0)]\in K_k\quad(5\mid k).
\tag{J3b}
\]
These polynomials have degree at most one, so they belong to the indicated low subspace since v>=4. In particular t_0>=1 on this actual exceptional stratum. This is why the two-active-coordinate value zero must not be extended to every period.

## 4. The actual PCL family has only finitely many one-coordinate exceptions

This is checked using the original PCL coefficients rather than an arbitrary invertible matrix. Write the even interpolation polynomial for U1 as p_0+p_2w^2. Its two coefficients are real, not both zero. The exact matrix factorization gives

\[
H(u)1=e^{\mathfrak a/u}G_u R(u^{-1})(p_0,0,p_2,0)^T.
\]

The scalar and diagonal factors are nonzero, and do not change coordinate support. Retain beta=2(gamma^2-delta^2)>0 and eta=(delta^2+gamma^2)^2. At z=0 the first and third coordinates of the last factor are

\[
p_0-\beta p_2/3,\qquad p_2.
\]

The fourth coordinate has the exact first coefficient

\[
[(\beta/3)p_0+(\eta-2\beta^2/9)p_2]z+O(z^3).
\tag{J5}
\]

This follows by inserting (row,column,n)=(4,0,1),(4,2,1) in the original PCL2 series: the coefficients are beta/3 and eta-2beta^2/9, respectively. When p_2=0, the first coordinate and the linear fourth coefficient are nonzero. When p_0-beta p_2/3=0 and p_2 is nonzero, the third coordinate and the linear fourth coefficient are nonzero, since eta-beta^2/9>0. Otherwise the first and third constant coefficients already suffice.

For each fixed original packet, a selected product of two coordinate functions is therefore a nonzero entire function of z. Its zeros in |z|<=R_*^{-1} are finite; z=0 itself is excluded when returning to u. All one-coordinate periods on the original |u|>=R_* domain belong to this explicitly specified finite set. At each exceptional period (J3) remains valid, and no generic rank is substituted.

## 5. Consequence for the actual kernel's polynomial degrees

AKJ15--17 gives the original containing space V_A: it has low degrees 0,...,v-1 and high degrees q'+v,...,q-1, with q'=(k-7)^2. On the stratum (J4),

\[
K_k\cap P_{q'+v-1}=0.
\]

With r=dim K_k=8k-16 and its actual increasing degree jumps d_0,...,d_{r-1},

\[
\boxed{q'+v+j\le d_j\le q-r+j,\qquad0\le j<r,}
\]

\[
r(q'+v)+r(r-1)/2\le\sum_jd_j\le r(q-r)+r(r-1)/2.
\tag{J6}
\]

These refer to the original observation kernel, not im L_k. The degree bounds are not a value for det(I^*G_NI); the actual metric orientation remains in that determinant.
