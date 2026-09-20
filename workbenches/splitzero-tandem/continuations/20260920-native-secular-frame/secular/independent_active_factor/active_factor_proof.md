# Reduced active factor and exact multiplicities

## AF-1. Objects and conventions

Let chi be a monic polynomial of degree n >= 1 over the complex numbers. On V = C[z]/(chi), use the ordered basis 1,z,...,z^(n-1), and let M be multiplication by z. Let r be an n-by-1 column, ell a 1-by-n complex-linear row, and A = M + r ell. Suppose G is a positive-definite Hermitian matrix and A*G = GA. Set

\[
f(z)=\ell(zI-M)^{-1}r=\frac{P(z)}{D(z)},
\qquad \gcd(P,D)=1,
\]

where D is monic and deg P < deg D. If f is zero, take P=0 and D=1. Set Q=D-P and H=chi/D. A pole order is zero when f is holomorphic at the point in question.

The polynomial chi is both the characteristic and minimal polynomial of M. Indeed 1,M1,...,M^(n-1)1 is the chosen basis, chi(M)=0, and no nonzero polynomial of degree below n annihilates 1. Thus the minimal polynomial has degree n and equals chi; the characteristic polynomial is monic of degree n and is divisible by the minimal polynomial, so it also equals chi.

## AF-2. The two determinant and resolvent identities

The adjugate formula gives f=N/chi for a polynomial N of degree at most n-1. From P chi = ND and coprimality, D divides chi. Hence H is a monic polynomial. The rank-one determinant identity gives, initially off the spectrum of M,

\[
d(z):=\det(zI-A)
=\det(zI-M)\bigl(1-\ell(zI-M)^{-1}r\bigr)
=\chi(z)(1-f(z))=H(z)Q(z).
\tag{AF.1}
\]

These identities extend as polynomial or rational identities, as appropriate. On the common resolvent set, write R_M=(zI-M)^(-1). Solving (zI-M-r ell)R_A=I gives the rank-one inverse identity

\[
R_A=R_M+\frac{R_Mr\ell R_M}{1-f}.
\]

For completeness, direct multiplication on the left by zI-M-r ell gives I because the coefficient of r ell R_M is -1+(1-f)/(1-f)=0. Therefore

\[
f_A(z):=\ell(zI-A)^{-1}r
=f+\frac{f^2}{1-f}
=\frac{f}{1-f}
=\frac{P}{Q}.
\tag{AF.2}
\]

The denominator Q is monic of degree deg D. Moreover gcd(P,Q)=gcd(P,D-P)=gcd(P,D)=1. Thus (AF.2) is already reduced. In the zero-transfer case Q=1 and all these identities remain valid.

## AF-3. The active factor has simple real roots

Let S=G^(1/2), the positive-definite Hermitian square root. The matrix B=SAS^(-1) is Hermitian: from A*G=GA one gets B*=S^(-1)A*S=SAS^(-1). By the finite-dimensional Hermitian spectral decomposition,

\[
B=\sum_{\lambda\in\sigma(B)}\lambda E_\lambda,
\qquad
(zI-A)^{-1}=\sum_{\lambda\in\sigma(B)}
\frac{\Pi_\lambda}{z-\lambda},
\qquad
\Pi_\lambda=S^{-1}E_\lambda S,
\tag{AF.3}
\]

where the distinct numbers lambda are real and the E_lambda are mutually orthogonal projections whose sum is I. It follows that

\[
f_A(z)=\sum_{\lambda\in\sigma(A)}
\frac{\ell\Pi_\lambda r}{z-\lambda}.
\tag{AF.4}
\]

Every pole of this scalar function is real and simple. Because P/Q is reduced, every zero of Q is a pole of f_A, with order equal to its multiplicity in Q. Therefore every zero of Q is real and simple. This includes Q=1, whose zero set is empty.

Consequently Q is a monic real polynomial. Since A is diagonalizable with real spectrum, d has only real roots. Its monic factor H=d/Q therefore also has real coefficients and only real roots, but H need not be square-free. The scalars ell Pi_lambda r need not be positive, or even real; no positivity of these residues was assumed or used.

## AF-4. Exact multiplicity formula at every old root

Let alpha be a root of chi of multiplicity e_alpha, and put p_alpha=ord_alpha D. Then 0 <= p_alpha <= e_alpha, and p_alpha is exactly the pole order of f at alpha when positive. Let m_alpha be the algebraic multiplicity of alpha as an eigenvalue of A, allowing m_alpha=0 when alpha is absent.

If p_alpha>0, coprimality gives P(alpha) != 0, so Q(alpha)=-P(alpha) != 0. Hence (AF.1) gives

\[
m_\alpha=e_\alpha-p_\alpha
\qquad(p_\alpha>0).
\tag{AF.5}
\]

If p_alpha=0, D(alpha) != 0 and Q(alpha)=D(alpha)(1-f(alpha)). By AF-3, a zero of Q has multiplicity exactly one. Hence

\[
m_\alpha=e_\alpha+\delta_\alpha,
\qquad
\delta_\alpha=
\begin{cases}
1,&f(\alpha)=1,\\
0,&f(\alpha)\ne1,
\end{cases}
\qquad(p_\alpha=0).
\tag{AF.6}
\]

In the case delta_alpha=1 the zero is simple, so f'(alpha) != 0: differentiating Q=D(1-f) at alpha gives Q'(alpha)=-D(alpha)f'(alpha) != 0. For any beta not among the roots of chi, its multiplicity as an eigenvalue of A is one if Q(beta)=0, and zero otherwise.

If alpha is nonreal, it cannot be an eigenvalue of A. Also Q(alpha) != 0 because Q has only real roots. Thus (AF.1) forces e_alpha-p_alpha=0, namely

\[
p_\alpha=e_\alpha
\quad\text{for every nonreal old root }\alpha.
\tag{AF.7}
\]

Every such root is completely removed from the new characteristic polynomial. In particular, no nonreal old root is invisible to f.

## AF-5. The full characteristic polynomial has no root of multiplicity above two

For any linear maps X and R, the map from ker(X+R) to im R sending v to Rv has kernel ker(X+R) intersect ker R, a subspace of ker X. Consequently

\[
\dim\ker(X+R)\le\dim\ker X+\operatorname{rank}R.
\tag{AF.8}
\]

For the present cyclic M, dim ker(M-lambda I) is one at an old root lambda and zero otherwise. This can be checked directly in the quotient: if chi=(z-lambda)^e h with h(lambda) != 0, the condition chi divides (z-lambda)q is equivalent to chi/(z-lambda) dividing q; among representatives q of degree below n this is a one-dimensional space. If chi(lambda) != 0, Bezout's identity makes multiplication by z-lambda invertible.

Apply (AF.8) with X=M-lambda I and R=r ell. Since rank R <= 1,

\[
\dim\ker(A-\lambda I)\le
\begin{cases}2,&\chi(\lambda)=0,\\1,&\chi(\lambda)\ne0.\end{cases}
\tag{AF.9}
\]

By (AF.3), A is diagonalizable, so geometric and algebraic multiplicities agree. Every root of d has multiplicity at most two, and every doubled eigenvalue is an old real root.

Combining this with AF-4 gives every possible multiplicity case:

| Old root | Scalar pole data | Exact new multiplicity and restriction |
|---|---|---|
| Nonreal alpha, any e | p=e | m=0 |
| Real alpha, p>0 | 1 <= p <= e | m=e-p in {0,1,2}; thus p >= e-2 |
| Real alpha, p=0, e=1 | f(alpha) != 1 | m=1 |
| Real alpha, p=0, e=1 | f(alpha)=1 | m=2 |
| Real alpha, p=0, e=2 | necessarily f(alpha) != 1 | m=2 |
| Real alpha, e>=3 | p=0 is impossible | p is one of e,e-1,e-2 |

Equivalently, at every real old root of multiplicity e>=2, p is one of e,e-1,e-2 and m=e-p. The case p=0 in this assertion can occur only for e=2 and entails f(alpha) != 1. At a simple real old root, p=1 removes the root, whereas p=0 retains it with multiplicity one or two according as f(alpha) differs from or equals one.

An overlap between H and Q occurs exactly at a simple real old root with p=0 and f(alpha)=1, and then the full characteristic polynomial has a double root there. A doubled eigenvalue not lying in Q comes either from e=2,p=0, or from e=p+2 with p>0. There are no further cases.

## AF-6. Exact examples showing both sources of double roots

### An active and invisible overlap

In the basis 1,z of C[z]/((z-1)(z-2)), take

\[
M=\begin{pmatrix}0&-2\\1&3\end{pmatrix},
\quad r=\binom{1}{-1},
\quad \ell=\begin{pmatrix}1&2\end{pmatrix},
\quad G=I_2.
\]

Then r ell=[[1,2],[-1,-2]], so A=I_2 and A*G=GA. The determinant identity gives

\[
f(z)=1-\frac{(z-1)^2}{(z-1)(z-2)}
=-\frac1{z-2},
\quad D=z-2,\quad P=-1,\quad H=Q=z-1.
\]

Thus Q has a simple root at 1 while d=(z-1)^2 has a double root there. The rank bound is sharp. At the old root 1, e=1,p=0 and f(1)=1.

### A double invisible root despite a nonzero old-root pole

In the basis 1,z,z^2 of C[z]/(z^3), take

\[
M=\begin{pmatrix}0&0&0\\1&0&0\\0&1&0\end{pmatrix},
\quad r=\begin{pmatrix}0\\1\\0\end{pmatrix},
\quad \ell=\begin{pmatrix}-1&1&0\end{pmatrix}.
\]

Then

\[
A=\begin{pmatrix}0&0&0\\0&1&0\\0&1&0\end{pmatrix},
\qquad
G=\begin{pmatrix}1&0&0\\0&2&-1\\0&-1&1\end{pmatrix}.
\]

For x=(x_1,x_2,x_3), x*Gx=|x_1|^2+|x_2|^2+|x_2-x_3|^2>0 for x!=0. Direct multiplication gives GA=A*G=diag(0,1,0). Also

\[
(zI-M)^{-1}r=z^{-1}r+z^{-2}(0,0,1)^T,
\quad f(z)=z^{-1}.
\]

Hence D=z, P=1, Q=z-1, H=z^2 and d=z^2(z-1). At alpha=0, e=3,p=1 and m=2. The double eigenvalue is not an active root.

### Zero transfer need not make the full spectrum simple

In the basis 1,z of C[z]/(z^2), take M=[[0,0],[1,0]], r=(0,-1)^T and ell=(1,0). Then A=0 is selfadjoint for G=I_2. Since (zI-M)^(-1)r=(0,-1/z)^T, f=0, D=Q=1 and H=d=z^2. Thus the zero-transfer case must not be excluded or replaced by an assertion that the full characteristic polynomial is square-free.

## AF-7. Exact meaning of active and invisible

Equation (AF.4) identifies the active roots exactly:

\[
Q(\lambda)=0
\quad\Longleftrightarrow\quad
\ell\Pi_\lambda r\ne0.
\]

At every active root lambda, the residue is P(lambda)/Q'(lambda), which is nonzero. The factor H records determinant multiplicity not contributed by this scalar pole. Therefore an active root can also have one invisible copy; the first example realizes that possibility. The second and third examples realize double roots with no active scalar pole. This is the exact relation between the reduced scalar resolvent and the full characteristic polynomial, not a claim that either determines eigenvalue multiplicity by itself.
