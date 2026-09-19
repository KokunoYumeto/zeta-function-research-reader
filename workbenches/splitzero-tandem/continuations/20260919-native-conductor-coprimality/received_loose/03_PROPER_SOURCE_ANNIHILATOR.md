# The original proper-source kernel is annihilated on the coordinate divisor

19 September 2026. Algebraic continuation on the original simple-quartet five-orbit domain. This retains the original PRD source kernel E=ker(B F), the four degree-four multipliers, and all conductor factor multiplicities. It does not evaluate a native Hermitian determinant from a rank calculation.

## 1. The actual invariant image and its conductor

Let S=C[x_1,x_2,x_3,x_4], g f(x)=f(D^{-1}x), D=diag(zeta,zeta^2,zeta^3,zeta^4), zeta^5=1. Retain Q=Q_0(H^{-1}x), Q_0(t)=t_1t_4-t_2t_3, Q_j=g^jQ, and

\[
A=\prod_{j=1}^{4}Q_j,\qquad P=\prod_{j=0}^{4}Q_j,
\qquad R_Q=S/(Q),\qquad B=\operatorname{im}(S^{\langle g\rangle}\to R_Q).
\]

The five quadrics are the actual nonassociate prime quadrics on the admitted five-orbit domain. No restriction of Q_j modulo Q is assumed irreducible.

The conductor of B in R_Q is exactly

\[
\boxed{\{c\in R_Q:cR_Q\subset B\}=A R_Q.}
\tag{E1}
\]

First, A h is the restriction of the invariant polynomial sum_{j=0}^4 g^j(Ah): every nonzero j term contains Q. There is no factor 1/5 in this identity. Thus A R_Q lies in B and is an ideal in R_Q.

For the reverse inclusion work on x_i nonzero. The cyclic action is free, since every nonidentity element has no eigenvalue one in these four coordinates. More explicitly, after localizing at X_i=x_i^5, S is free over its invariant ring with basis 1,x_i,...,x_i^4; every character component is its indicated power of the invertible x_i times the invariant component. The extension is given by T^5-X_i, whose derivative is a unit. The character Vandermonde gives the direct-sum orbit decomposition after this finite etale base change.

The invariant ring B identifies with (S/(P))^G, since S^G intersect (Q) equals P S^G by the original five-prime argument. After the displayed free base change, B subset R_Q becomes

\[
S/(P)\longrightarrow\bigoplus_{j=0}^4S/(Q_j).
\]

A tuple supported only on component j is in this image precisely when its nonzero component is represented by a polynomial divisible by all other Q_i. The original polynomial ring is factorial and these primes are distinct, so the intersection of their principal ideals is their full product. Every ideal of the direct sum decomposes componentwise. Its conductor is therefore the product of the other four quadrics on each component. Descent through the displayed faithful free module gives c in A R_Q on each x_i chart.

To restore the vertex, use the original Segre isomorphism (R_Q)_d = T_{d,d} on P^1 times P^1. For a homogeneous c of degree d, the ratio c/A is a regular section of O(d-8,d-8) on the four x_i charts, which cover that surface because H is invertible. Expanding on the four standard Segre charts identifies this section with a biform in T_{d-8,d-8}, or with zero when either degree is negative. Hence c is globally divisible by A in R_Q. This proves (E1), with no additional vertex-supported term.

## 2. Apply the conductor to the actual four multiplier kernel

Put C_d=(S/(Q,A))_d, J_d=im(S_d^G -> C_d). The original proper source is J_{v,k}, the first-v-jet-vanishing invariant subspace. Its original cofactor kernel consists of those classes f for which all four x_i^4f lie in J_{k+4}. The low jets remain part of the source; the following argument is valid before imposing that further restriction.

An invariant lift f belongs to B. The condition x_i^4f in J_{k+4} means x_i^4f is in B modulo A R_Q. Since A R_Q is already contained in B by (E1), it means x_i^4f belongs to B itself.

Let p=x_1x_2x_3x_4, of character weight zero. For a monomial m of nonzero character weight w, choose the unique i with 4i=w mod5. Then

\[
p^4m/x_i^4
\]

is an actual invariant polynomial: its exponents are nonnegative and its character is zero. Thus

\[
p^4mf=(p^4m/x_i^4)(x_i^4f)\in B.
\]

For a weight-zero monomial the same conclusion follows from f in B. Monomials span R_Q, so p^4f R_Q is contained in B. Equation (E1) proves

\[
\boxed{p^4 E_k=0\quad\text{in }C_{k+16}.}
\tag{E2}
\]

This is a degree-changing annihilator for the exact original PRD kernel. It does not identify the original arithmetic dilation with this multiplication.

## 3. Complete factor multiplicities and an explicit dimension bound

Under the original Segre substitution write ell_i=x_i|_{Q=0}, a biform of bidegree (1,1), and retain the biform A of bidegree (8,8). Set

\[
G=\gcd\left(A,(ell_1ell_2ell_3ell_4)^4\right),
\qquad \operatorname{bideg} G=(g_z,g_w).
\]

This is the actual gcd, including all multiplicities and scalar compensation; no generic factor configuration is chosen. Unique factorization gives the entire kernel of multiplication by p^4:

\[
\boxed{
\ker M_{p^4}
=(A/G)T_{k-8+g_z,k-8+g_w}/A T_{k-8,k-8}.
}
\tag{E3}
\]

Indeed A divides p^4f exactly when A/G divides f. The numerator degree and denominator are the original biform degrees. For k>=9,

\[
\boxed{0\le \dim E_k\le(g_z+g_w)(k-7)+g_zg_w.}
\tag{E4}
\]

When the actual gcd is one, (E4) is zero: E_k=0. On that factor stratum, the original source metric is exactly Q_N^p=Z_R^*J_0^*D_{k,N-v}^{(s_0)}J_0Z_R, with the E-Schur terms absent. The target still minimizes over the full original J, so this does not remove its denominator or assign the proper-source scalar.

Combining with the fixed-jet calculation, on its two-active-coordinate stratum j_{0,k}=8k-32-v. Hence the original r_I satisfies

\[
8k-32-v-(g_z+g_w)(k-7)-g_zg_w
\le r_I\le8k-32-v,
\]

with the lower endpoint also intersected with zero. This is an explicit support/rank restriction on the original map, not a replacement of its full attained metrics by the rank.

## 4. Exact metric boundary retained

The proper return remains

\[
\mathcal M^p=\mathcal R\log\det[(Q_N^p)^{-1/2}H_N^p(Q_N^p)^{-1/2}],
\]

with Q_N^p at the original degree-k displaced cutoffs and H_N^p the original target-J minimum on the same Z_R values. Equation (E2) identifies the support of the source kernel. It does not evaluate this determinant, the native angular clipped sums, or the arithmetic responses U,V.
