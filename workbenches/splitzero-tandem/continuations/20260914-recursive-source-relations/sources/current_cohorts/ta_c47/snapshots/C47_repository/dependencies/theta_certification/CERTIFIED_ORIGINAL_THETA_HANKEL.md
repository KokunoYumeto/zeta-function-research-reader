# Certified original-theta Hankel calculation

This calculation certifies strict positive definiteness of both original
matrices
\[
 \mathsf H_{15}=(b_{r+s})_{0\le r,s\le15},
 \qquad
 \mathsf H_{15}^{(1)}=(b_{r+s+1})_{0\le r,s\le15}.
\tag{CH.1}
\]
Their coefficients are computed from the original \(g=2\xi\) theta source.
Every one of their 32 leading principal minors is certified positive.
The coordinates, original mass, theta terms and logarithmic coefficient
recurrence are retained. No zero ordinate is supplied to the calculation.

## 1. Original integral and coefficients

Use the original functions
\[
 \phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\quad
 f_0(x)=2\sum_{n\ge1}\phi_*(nx),\quad
 \psi(y)=e^{y/2}f_0(e^y).
\tag{CH.2}
\]
For completeness, write
\(\vartheta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x^2}\) and
\(D=-x\partial_x\). Termwise differentiation on compact positive
\(x\)-intervals gives \(f_0=(D^2-D)\vartheta\). The original Gaussian
Poisson identity is \(\vartheta(x)=x^{-1}\vartheta(1/x)\).
For the exact reflection operator
\((\mathcal Rv)(x)=x^{-1}v(1/x)\), differentiation gives
\(D\mathcal R=\mathcal R(1-D)\), and hence
\((D^2-D)\mathcal R=\mathcal R(D^2-D)\).
Applying this identity to \(\vartheta\) proves
\(f_0(x)=x^{-1}f_0(1/x)\) and therefore
\(\psi(-y)=\psi(y)\). All powers of \(x\) are retained in this map.
Consequently, for every even nonnegative integer \(J\),
\[
\begin{split}
 M_J&=\int_{\mathbb R}y^J\psi(y)\,dy\\
 &=\int_0^\infty y^J
 \sum_{n\ge1}
 \left(16\pi^2n^4e^{9y/2}-24\pi n^2e^{5y/2}\right)
 e^{-\pi n^2e^{2y}}\,dy .
\end{split}
\tag{CH.3}
\]
Both factors two, from theta summation and reflection, are present.
Every summand in (CH.3) is nonnegative for \(y\ge0\), and is strictly
positive for \(y>0\): its non-polynomial coefficient factors as
\[
 8\pi n^2e^{5y/2}
 (2\pi n^2e^{2y}-3)e^{-\pi n^2e^{2y}}>0.
\tag{CH.4}
\]
For \(J=0\), positivity holds at \(y=0\) as well.

The Mellin substitution \(x=e^y\), including \(dx=e^y\,dy\), gives
\[
 g(1/2+iz)=\int_{\mathbb R}\psi(y)e^{izy}\,dy,\qquad
 a_j=\frac{(-1)^jM_{2j}}{(2j)!},\qquad
 F(w)=\sum_{j\ge0}a_jw^j .
\tag{CH.5}
\]
The bounds proved below supply absolute integrability after multiplication
by every power of \(y\), and by \(e^{A|y|}\) for each fixed \(A\):
replace \(9/2\) by \(9/2+A\) in (CH.11) and choose a sufficiently
large positive \(L\), so its decay constant is positive. Reflection
gives the same estimate on the other half-line. Thus
dominated differentiation on compact \(z\)-sets is valid and proves
\(F(z^2)=g(1/2+iz)\) with the displayed coefficients. In particular the
original \(a_0=M_0=g(1/2)\) is strictly positive. Multiplication of the
convergent power series
\(-F'(w)/F(w)=\sum_{n\ge0}b_nw^n\) by \(F(w)\) gives
\[
 a_0b_n+\sum_{j=1}^n a_jb_{n-j}=-(n+1)a_{n+1},
 \qquad
 b_n=\frac{-(n+1)a_{n+1}-\sum_{j=1}^na_jb_{n-j}}{a_0}.
\tag{CH.6}
\]
This is the exact coefficient map used by the program. The denominator is
the computed interval for the original \(a_0\). It is never replaced by one.

## 2. Explicit positive omitted regions

Fix \(N=20\) and \(L=4\). The finite integral retains precisely
\(1\le n\le19\) and \(0\le y\le4\). Its complement is the disjoint union of
the omitted terms \(n\ge20\) on \(0\le y\le4\) and every \(n\ge1\) on
\(y>4\). Endpoints have measure zero.

For \(n=N+\ell\), \(\ell\ge0\), the elementary inequality
\(\log(1+t)\le t\) for \(t\ge0\), proved by differentiating
\(t-\log(1+t)\), implies
\[
 (N+\ell)^4\le N^4e^{4\ell/N},\qquad
 (N+\ell)^2\ge N^2+2N\ell .
\tag{CH.7}
\]
Hence, for \(y\ge0\),
\[
 \sum_{n\ge N}n^4e^{-\pi n^2e^{2y}}
 \le
 N^4e^{-\pi N^2}
 \sum_{\ell\ge0}e^{(4/N-2\pi N)\ell}
 =
 \frac{N^4e^{-\pi N^2}}{1-e^{4/N-2\pi N}} .
\tag{CH.8}
\]
The exponent \(4/N-2\pi N\) is negative for every integer \(N\ge1\).
Using (CH.4), and bounding the positive difference in (CH.3) by its
first positive term, the first omitted region lies in \([0,T_{J,n}]\), where
\[
 T_{J,n}=
 \frac{16\pi^2L^{J+1}e^{9L/2}N^4e^{-\pi N^2}}
 {1-e^{4/N-2\pi N}} .
\tag{CH.9}
\]
Indeed \(y^J\le L^J\) and \(e^{9y/2}\le e^{9L/2}\) on the finite interval,
whose length contributes the displayed factor \(L\). The deliberately
larger bound \(L^{J+1}\) is retained.

For the second omitted region the same argument, with \(N=1\) but
retaining the \(y\)-dependent first exponential, gives
\[
 \sum_{n\ge1}n^4e^{-\pi n^2e^{2y}}
 \le
 \frac{e^{-\pi e^{2y}}}{1-e^{4-2\pi}},
 \qquad y\ge0 .
\tag{CH.10}
\]
Set \(h_J(y)=y^Je^{9y/2-\pi e^{2y}}\) on \(y\ge L>0\). Its logarithmic
derivative is
\[
 \frac{h_J'(y)}{h_J(y)}
 =\frac Jy+\frac92-2\pi e^{2y}
 \le-\alpha_J,\qquad
 \alpha_J=2\pi e^{2L}-\frac92-\frac JL .
\tag{CH.11}
\]
For \(0\le J\le64\), \(N=20\), \(L=4\), all \(\alpha_J\) are strictly
positive. For example, \(\pi>3\) and
\(e^8>1+8+8^2/2=41\) give
\(\alpha_J>246-9/2-16>0\).
Integration of (CH.11) gives
\(h_J(y)\le h_J(L)e^{-\alpha_J(y-L)}\), and then
\[
 T_{J,y}=
 \frac{16\pi^2 L^J e^{9L/2-\pi e^{2L}}}
 {(1-e^{4-2\pi})(2\pi e^{2L}-9/2-J/L)}
\tag{CH.12}
\]
bounds the second omitted region. Therefore the complete exact moment
satisfies
\[
 M_J\in I_{J,\mathrm{finite}}+[0,T_{J,n}+T_{J,y}].
\tag{CH.13}
\]
The constants and signs of both original terms survive (CH.3) and the
finite integration. The positive upper majorant is used only for the
two explicitly omitted regions.

## 3. Validated finite integration and its exact export

The program uses python-flint 0.9.0, linked to FLINT 3.6.0, with
1024-bit arithmetic. For each even \(J=0,2,\ldots,64\), it evaluates
\[
 z^J e^{z/2}\sum_{n=1}^{19}
 \bigl(16(\pi n^2e^{2z})^2-24\pi n^2e^{2z}\bigr)
 e^{-\pi n^2e^{2z}}.
\tag{CH.14}
\]
This is algebraically identical to the finite integrand in (CH.3).
It is an entire complex function: all powers are nonnegative integer
powers, and every remaining operation is addition, multiplication or
the entire exponential. It has no branch cut, pole, absolute value,
conjugation or piecewise real continuation.

The acb.integral callback receives a Boolean analytic. The official
contract requires the callback to establish analyticity on the input
complex ball when this flag is true. Formula (CH.14) is entire, so the
same formula is valid for both values of the flag on every ball. This
is the reason that the implementation may ignore the flag. It is not
assuming that analyticity along the real segment alone suffices.

The finite interval is divided at the exact rationals
\(0,1/2,1,\ldots,7/2,4\). Each of its eight integrals is evaluated with
relative and absolute tolerance goals \(2^{-850}\), evaluation limit
200000 and depth limit 50. These controls affect effort and enclosure
width; the final proof uses the returned enclosures themselves.
Every returned value must be finite and its imaginary part must contain
zero. Its real interval therefore encloses the real integral. The eight
real intervals are added with outward rounding.

The two tail formulas are evaluated with Arb arithmetic, after verifying
strict positivity of each denominator interval. If their sum has upper
endpoint \(U_J\), the program forms the interval
\(\operatorname{hull}(0,U_J)\), and adds it to the real finite interval.
This proves (CH.13) with the actually stored enclosure.

For every reported Arb ball, lower() and upper() produce exact
dyadic endpoints rounded respectively downward and upward.
man_exp() writes each as \(m2^e\), with integers \(m,e\).
The export writes that same rational as numerator \(m2^e\) and denominator
one if \(e\ge0\), and numerator \(m\), denominator \(2^{-e}\) otherwise.
No decimal conversion intervenes. Every decimal display field is for
reading only. The lower and upper integer fractions are the
authoritative certificate. The program raises the Python integer-string
limit to accommodate the large dyadic denominator of
(CH.12); this changes only serialization capacity.

## 4. Interval coefficient and LDL proof

Arb interval operations enclose every real operation on represented
inputs. Induction in (CH.6), beginning with \(a_0>0\), therefore proves
that each stored \(a_j\) encloses the exact coefficient in (CH.5) and
each stored \(b_n\) encloses the exact logarithmic coefficient in (CH.6).
The 33 moments determine \(a_0,\ldots,a_{32}\) and
\(b_0,\ldots,b_{31}\), exactly the data required by (CH.1).

For each shift \(\epsilon=0,1\), put \(A_{ij}=b_{i+j+\epsilon}\).
In the original ordered monomial basis, define the unit lower triangular
matrix \(L\) and diagonal \(D=\operatorname{diag}(d_0,\ldots,d_{15})\)
recursively by
\[
 d_j=A_{jj}-\sum_{k<j}L_{jk}^{\,2}d_k,\qquad
 L_{ij}=\frac{A_{ij}-\sum_{k<j}L_{ik}L_{jk}d_k}{d_j}\quad(i>j).
\tag{CH.15}
\]
The implementation checks that the entire computed interval for \(d_j\)
is strictly positive before every division. Induction on \(j\) proves
that the stored interval values contain the exact values of (CH.15).
The equations for the diagonal and lower triangular entries are exactly
the equations of \(A=LDL^T\); symmetry supplies the upper triangular
entries. Since \(L\) is invertible with determinant one,
\[
 c^TAc=\sum_{j=0}^{15}d_j(L^Tc)_j^2>0
 \quad\text{for every }c\in\mathbb R^{16}\setminus\{0\}.
\tag{CH.16}
\]
For each leading size \(r\), restriction to the first \(r\) coordinates
and triangularity give
\[
 \det A_{[0,r-1]}=\prod_{j=0}^{r-1}d_j>0.
\tag{CH.17}
\]
The exact interval computation certifies all 32 pivots as positive.
No pivoting, coordinate rescaling, diagonal congruence or replacement
of the source mass occurs.

## 5. Recorded values and finite conclusion

The authoritative file certificate_dimension16_1024.json stores
all 264 finite integral pieces, their real and imaginary intervals,
all 66 tail bounds, all 33 complete moments, all coefficients, and both
complete lower triangular factor intervals. The run took about
16.14 seconds on the recorded host. This duration measures one
reproducible computation, rather than a mathematical assumption.

For orientation the original mass and first coefficients begin
\[
\begin{split}
 a_0&=0.99424155637662821982554747937079544\ldots,\\
 b_0&=0.023104993115418970788933810430339014\ldots,\\
 b_1&=3.7172599285269686164866262471740578\ldots\times10^{-5},\\
 b_2&=1.4417393140097327969538155609482091\ldots\times10^{-7}.
\end{split}
\tag{CH.18}
\]
The last pivots and full determinants are enclosed within the following
simple rational intervals:
\[
\begin{array}{c|c|c}
 \epsilon&
 d_{15}&\det \mathsf H_{15}^{(\epsilon)}\\ \hline
 0&(6\cdot10^{-107},\,7\cdot10^{-107})
   &(9\cdot10^{-822},\,10\cdot10^{-822})\\
 1&(7\cdot10^{-111},\,8\cdot10^{-111})
   &(6\cdot10^{-878},\,7\cdot10^{-878})
\end{array}
\tag{CH.19}
\]
The exact stored rational endpoints are much narrower; the respective
last pivots retain 656 and 648 relative accuracy bits.

Thus this calculation establishes strict positivity of the two
specified dimension-16 matrices and every leading truncation.
Its quantified conclusion concerns these finite matrices. It supplies
certified original-theta inputs in place of the Workbench's unvalidated
quadrature values at these dimensions.

## Reproduction

Run certify_theta_hankel.py with arguments --dimension 16 --precision 1024
--target-bits 850 --output certificate_dimension16_1024.json
using python-flint 0.9.0. The defaults retain \(N=20,L=4\).
The file certificate_dimension2_256.json records a separate smaller run
with dimension two, precision 256 and tolerance exponent 200.

The official integration and real-endpoint API contracts are documented at:

- [python-flint complex integration](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral)
- [python-flint real ball endpoints](https://python-flint.readthedocs.io/en/latest/arb.html)

The local API_CONTRACT.txt records the installed method docstrings used
when implementing the computation.
