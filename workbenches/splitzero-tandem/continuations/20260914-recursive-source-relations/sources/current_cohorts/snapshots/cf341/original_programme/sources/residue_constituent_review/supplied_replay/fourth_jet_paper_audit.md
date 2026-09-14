# Read-only paper audit of the residue-curvature fourth jet and false controls

Date: 2026-09-13. This is a source-level mathematical audit. No Python checker,
predecessor checker, or Lean command was executed for this audit. The delivered
packet was not modified. Execution and manifest verification belong to the
parent task.


## 1. The exact identities RC18–RC27

Write \(e_0=1_E\), \(\ell=e_{q-1}^{T}\), and \(R=e_0\ell\). Retain
\(P(t)=\Pi(t)\iota\), \(H_F=P^*P\), and
\(Q=P H_F^{-1}P^*\). The assumptions used in this calculation are the
specified \(u\ne0\), the given holomorphic invertible period matrix with
\(\Pi'=-\Pi(A+tR)/u\), and the actual nonzero proper invariant constituent
\(A\iota=\iota A_F\). These are exactly the objects and hypotheses already
specified by RC4–RC5 and RC13–RC17.

Multiplication of the differential equation by \(\iota\) gives, with the order
of the matrix factors unchanged,

\[
P'=-P A_F/u-(t/u)\Pi e_0\ell_F,
\qquad \ell_F=\ell\iota.
\]

Since \(QP=P\), this proves RC18–RC19:

\[
N=(I_q-Q)P'=-(t/u)n\ell_F,
\qquad n=(I_q-Q)\Pi e_0.
\]

The vector \(n\) cannot vanish: otherwise \(\Pi e_0\) would belong to
\(\operatorname{im}(\Pi\iota)\), and invertibility of \(\Pi\) would put
\(e_0\) in the proper invariant subspace \(F\). Its entire cyclic orbit
\(e_0,Ae_0,\ldots,A^{q-1}e_0\) would then lie in \(F\), contradicting
\(\dim F<q\). Also \(\ell_F\ne0\): if \(\ell(F)=0\), invariance gives
\(\ell(A^j f)=0\) for every \(f\in F\) and \(0\le j<q\). The perfect
residue pairing \(\beta(v,w)=\ell(vw)\), whose matrix determinant is
\((-1)^{q(q-1)/2}\), then forces \(f=0\), contradicting \(F\ne0\).
Thus the normal map has rank one for every \(t\ne0\), and has kernel
\(\ker\ell_F\). It vanishes at zero.

Differentiating the period equation exactly gives

\[
\Pi''=\Pi(A+tR)^2/u^2-\Pi R/u.
\]

At zero, \(A^2\iota=\iota A_F^2\), so

\[
(I_q-Q(0))P''(0)=-n(0)\ell_F/u.
\]

This proves RC20, including its nonzero rank-one statement.

For \(\psi=\log\det H_F\), holomorphy gives
\(\partial_t H_F=P^*P'\),
\(\partial_{\bar t}H_F=P'^*P\), and
\(\partial_t\partial_{\bar t}H_F=P'^*P'\). Differentiation of the inverse
and cyclic invariance of trace therefore give

\[
\begin{aligned}
\partial_t\partial_{\bar t}\psi
&=\operatorname{Tr}\bigl(
 H_F^{-1}P'^*P'
 -H_F^{-1}P'^*P H_F^{-1}P^*P'\bigr)\\
&=\operatorname{Tr}\bigl(H_F^{-1}P'^*(I_q-Q)P'\bigr)
 =\operatorname{Tr}(H_F^{-1}N^*N).
\end{aligned}
\]

The last equality uses \(Q^*=Q\) and \(Q^2=Q\); it does not replace a
rectangular determinant by a square one. Substitution of the normal map gives

\[
N^*N=\frac{|t|^2}{|u|^2}\|n\|^2\ell_F^*\ell_F,
\qquad
\operatorname{Tr}(H_F^{-1}\ell_F^*\ell_F)
=\ell_F H_F^{-1}\ell_F^*.
\]

Because \(H=\Pi^*\Pi\), minimization over the actual coset yields

\[
\min_f(e_0-\iota f)^*H(e_0-\iota f)
=\min_f\|\Pi e_0-Pf\|^2
=\|(I_q-Q)\Pi e_0\|^2=\|n\|^2.
\]

This proves RC23–RC25 exactly:

\[
\partial_t\partial_{\bar t}\psi
=\frac{t\bar t}{|u|^2}\mathfrak c_F(H(t)).
\]

Both factors of \(\mathfrak c_F\) are positive by the established
nonvanishing of the quotient vector and restricted functional. For the dual
determinant line, the curvature convention
\(c_1(L,h)=-(i/2\pi)\partial\bar\partial\log h\) gives precisely the
positive sign in RC26.

The functions involved are real analytic near zero: \(\Pi\) is holomorphic,
\(H_F\) is positive definite, and the inverse and real logarithm are real
analytic there. Applying \(\partial_t\partial_{\bar t}\) once more gives

\[
\partial_t\partial_{\bar t}(t\bar t\,c(t,\bar t))
=c+t\partial_t c+\bar t\partial_{\bar t}c
+t\bar t\partial_t\partial_{\bar t}c.
\]

Evaluation at zero proves

\[
\left.\partial_t^2\partial_{\bar t}^2\psi\right|_0
=\mathfrak c_F(H(0))/|u|^2.
\]

If \(C_{22}\) is the coefficient of \(t^2\bar t^2\) in the real-analytic
Taylor expansion of \(\psi\), then

\[
\left.\partial_t^2\partial_{\bar t}^2
(C_{22}t^2\bar t^2)\right|_0
=(2!)(2!)C_{22}=4C_{22}.
\]

Thus RC27’s derivative and its following Taylor-coefficient statement agree:
\(C_{22}=\mathfrak c_F(H(0))/(4|u|^2)\).

## 2. Exact fourth-jet fixture in test 07

For \(\chi=S^2\), \(d=S\), and the ordered coefficient basis \((1,S)\),

\[
A=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
R=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
\iota=\binom01,\quad \pi=\begin{pmatrix}1&0\end{pmatrix}.
\]

The exact model matrix in the delivered checker is

\[
B=\begin{pmatrix}1&b\\0&1\end{pmatrix},\qquad
b=(1+i)/3,\qquad u=2.
\]

Let \(B_j\) denote the coefficient of \(t^j\) in the solution initialized
by \(\Pi(0)=B\). Equating coefficients in the period equation gives

\[
B_0=B,\qquad B_1=-BA/2,\qquad
B_2=-(B_1A+B_0R)/4=-BR/4,
\]

because \(A^2=0\). In particular the code’s `jets` are Taylor coefficients,
and `jets[2]` already contains the factor \(1/2!\). Their actual constituent
columns are

\[
p_0=B_0\iota=\binom b1,\qquad
p_1=B_1\iota=\binom00,\qquad
p_2=B_2\iota=\binom{-1/4}{0}.
\]

With independent formal variables \(x=t\) and \(y=\bar t\), the Gram
through bidegree \((2,2)\) is exactly

\[
h(x,y)=\sum_{i,j=0}^{2}p_i^*p_j\,y^ix^j
=\frac{11}{9}-\frac{1-i}{12}x^2-
\frac{1+i}{12}y^2+\frac1{16}x^2y^2.
\]

Indeed \(|b|^2=2/9\), so \(h_0=1+|b|^2=11/9\). Hence

\[
Z=h/h_0-1=\alpha x^2+\gamma y^2+\delta x^2y^2,
\quad
\alpha=-\frac{3(1-i)}{44},\quad
\gamma=-\frac{3(1+i)}{44},\quad
\delta=\frac9{176}.
\]

For this particular fixture, powers \(Z^n\) with \(n\ge3\) have total
degree at least six and cannot contribute to \(x^2y^2\). Therefore

\[
\begin{aligned}
[x^2y^2]\log h
&=[x^2y^2](Z-Z^2/2)\\
&=\delta-\alpha\gamma
=\frac9{176}-\frac9{968}
=\frac{81}{1936}.
\end{aligned}
\]

The checker’s generic loop through \(n=4\) is also sufficient even for a
nonzero linear term: \(Z\) has zero constant term, so \(Z^n\) has total
degree at least \(n\). Terms of degree greater than four cannot contribute
to \(x^2y^2\). Its truncation is reduction in
\(\mathbb Q(i)[x,y]/(x^3,y^3)\); discarding a term with either exponent
greater than two cannot remove a later contribution to the target monomial,
because multiplication never decreases either exponent. Higher period jets
also have either \(x\)-degree or \(y\)-degree at least three in the Gram,
so the same reduction proves they cannot change the target coefficient.

The exact fourth derivative computed by line 152 is consequently

\[
4\cdot\frac{81}{1936}=\frac{81}{484}.
\]

Independently, the fixed coefficient metric and restricted Gram are

\[
M=B^*B=\begin{pmatrix}1&b\\\bar b&11/9\end{pmatrix},
\qquad M_F=(11/9).
\]

The quotient norm and residue dual norm in the delivered `pairing_cost` are

\[
q_{M,F}([1])=1-\frac{|b|^2}{11/9}=\frac9{11},\qquad
\ell_F M_F^{-1}\ell_F^*=\frac9{11}.
\]

Thus

\[
\mathfrak c_F(M)=\frac{81}{121},\qquad
\frac{\mathfrak c_F(M)}{u^2}=\frac{81}{484},
\]

exactly the checker’s equality. The factorial is present once at each
necessary place: \(1/2!\) in the holomorphic second Taylor coefficient,
and \(2!2!\) in converting the bivariate scalar coefficient to the mixed
fourth derivative. There is no lost or duplicated factor.

## 3. The preceding normal-acceleration fixture in test 07

The first part of that method instead retains \(\chi=S^3+S\), \(d=S\),
the basis \((1,S,S^2)\), and \(u=2\). Thus

\[
A=\begin{pmatrix}0&0&0\\1&0&-1\\0&1&0\end{pmatrix},\quad
R=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix},\quad
\iota=\begin{pmatrix}0&0\\1&0\\0&1\end{pmatrix},\quad
\ell_F=\begin{pmatrix}0&1\end{pmatrix}.
\]

The original model is

\[
B=\begin{pmatrix}
1&(1+i)/3&1/4+i/3\\
0&1&1/2+i/3\\
0&0&1
\end{pmatrix}.
\]

Writing its upper entries as \(b,c,d\), the two columns of \(P=B\iota\)
are \((b,1,0)^T\) and \((c,d,1)^T\), and their Gram is

\[
H_F=\begin{pmatrix}
11/9&(25+13i)/36\\
(25-13i)/36&221/144
\end{pmatrix},\qquad
\det H_F=\frac{1637}{1296}.
\]

The vector

\[
z=\begin{pmatrix}1\\-(1-i)/3\\(-7+2i)/36\end{pmatrix}
\]

satisfies \(P^*z=0\), because its last coordinate is
\(\overline{db-c}\) and \(db-c=(-7-2i)/36\). Its squared norm is

\[
z^*z=1+2/9+53/1296=1637/1296.
\]

The exact normal projection of \(Be_0=e_0\) is therefore
\(n=(1296/1637)z\), with \(\|n\|^2=1296/1637\).
The second derivative used in the checker is
\(P''=B(A^2/4-R/2)\iota\). The invariant \(A^2\) term projects to zero,
leaving

\[
N=-\frac12 n\begin{pmatrix}0&1\end{pmatrix}.
\]

This has rank one. The exact dual norm is

\[
\ell_FH_F^{-1}\ell_F^*
=\frac{11/9}{1637/1296}=\frac{1584}{1637}.
\]

Consequently both sides of the checker’s normal-acceleration cost equality
are

\[
\operatorname{Tr}(H_F^{-1}N^*N)
=\frac14\frac{1296}{1637}\frac{1584}{1637}
=\frac{513216}{2679769}
=\frac{\mathfrak c_F(B^*B)}{u^2}.
\]

## 4. The three deliberately false controls

All three branches use \(\chi=S^2\), \(d=S\), the same \(A,R,\iota,\pi\)
as in section 2, but now retain \(B=I_2\), \(u=1\), and the outer
assignment \(t=2\). Therefore

\[
P=\binom01,\quad H_F=(1),\quad
Q=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
I_2-Q=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

### Rank branch

\[
R\iota=\binom10,\qquad
\pi R\iota=(1),\qquad \operatorname{rank}(\pi R\iota)=1.
\]

The branch explicitly requires this last rank to be zero. It therefore
rejects the actual false transverse-rank formula, with no preparatory
mathematical failure.

### Laplacian branch

This branch uses the jet at zero and \(k=1\); its outer \(t=2\) assignment
is unused. Since \(A^2=0\), its two derivative matrices are

\[
B_1=-A=\begin{pmatrix}0&0\\-1&0\end{pmatrix},\qquad
B_2=-R=\begin{pmatrix}0&-1\\0&0\end{pmatrix}.
\]

The false equality has the exact sides

\[
u^2B_2+B_1=\begin{pmatrix}0&-1\\-1&0\end{pmatrix},\qquad
B(A^2-A)=\begin{pmatrix}0&0\\-1&0\end{pmatrix}.
\]

Its residual is \(-R\ne0\). Restoring the omitted forcing \(uBR=R\)
annuls the residual exactly, as RC39 requires.

### Curvature branch

At the branch’s retained \(t=2\),

\[
A+tR=\begin{pmatrix}0&2\\1&0\end{pmatrix},\qquad
P'=-B(A+tR)\iota/u=\binom{-2}{0}.
\]

Thus

\[
\operatorname{Tr}(H_F^{-1}P'^*(I_2-Q)P')=4.
\]

For \(M=I_2\), the quotient norm of \([1]\) is one and the squared dual
norm of \(\ell_F=(1)\) is one. Hence the intentionally false right side
\(\mathfrak c_F(M)/u^2\) equals one, and the residual is \(4-1=3\ne0\).
Restoring \(|t|^2=4\) gives precisely the value four in RC25.

### Source-level failure mechanism

`require` uses an ordinary `if not bool(value)` followed by an explicit
`raise AssertionError(message)`. `eq` calls `require(zero(x-y), message)`.
No branch relies on a Python `assert` statement. Each negative option is an
admitted argparse choice and directly invokes `negative_control` before
the following `return 0`. The exceptions are not caught in that path.
Consequently, with dependencies successfully imported, each branch reaches
and rejects its substantive formula in both ordinary and optimized Python.
The source contains no deliberate startup guard that substitutes for these
formula failures. Actual tracebacks and exit statuses must be supplied by
the parent’s executions; this audit does not assert they were observed here.

## 5. RC28 derivative convention

RC28 is correct for the ordinary derivative on the real \(t\)-axis. More
explicitly, write \(s\in\mathbb R\) for that axis and evaluate the given
period family at \(t=s\). For the specified real \(u>0\), RC18 yields
\(P'(0)=-P(0)A_F/u\), so

\[
\left.\frac{dH_F(s)}{ds}\right|_0
=-(A_F^*H_F(0)+H_F(0)A_F)/u.
\]

Therefore

\[
\left.\frac{d}{ds}\log\det H_F(s)\right|_0
=-\frac{\overline{\operatorname{Tr}A_F}+\operatorname{Tr}A_F}{u}
=-\frac{2\operatorname{Re}\operatorname{Tr}A_F}{u}.
\]

The original \(\det G_{N,F}\) is independent of \(s\), so multiplying
by \(-u\) and subtracting \(kp\) gives exactly RC28. A Wirtinger
\(\partial_t\) derivative would instead give
\(-\operatorname{Tr}A_F/u\). The note uses `d/dt` in RC28 and has just
distinguished real-axis differentiation from mixed differentiation after
RC27, so this is a notation clarification, not a detected false formula.
Writing `d/ds at s=0, t=s real` when reusing RC28 would make the convention
fully explicit.

## Audit result

No arithmetic, matrix-order, sign, or factorial discrepancy was found in the
audited formulas or fixtures. The fourth-jet coefficient is \(81/1936\),
the mixed fourth derivative is \(81/484\), and the three substantive false
controls have respectively actual rank one, residual \(-R\), and residual
three. The only clarification identified is the real-axis derivative
convention in RC28. All assigned source-level calculations are complete.
