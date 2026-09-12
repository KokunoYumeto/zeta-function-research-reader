# Independent spectral-square parity audit

Date: 2026-09-12. This is a bounded algebraic audit of the original PR17
relation presentation and the new even/odd splitting. The complete source
read was `sources/web_pr17_spectral_sum/workbenches/tau-spectral-sum/RESEARCH_NOTE.md`,
especially its original coordinate morphisms and invariant-ideal proof in
Section 3. No main or TeX file was edited. No literature search or Lean run
was needed. The repeated-root examples below are exact polynomial models,
not assertions about the roots of xi.

## 1. The exact quotient presentations and signs

Let H be monic of degree D>=1, d=2D, and retain

\[
 h(s)=(-1)^D H(-(s-\tfrac12)^2),\quad
 S=s_1+s_2,\quad Z=S-1,\quad r=s_1-s_2,\quad
 \Delta=r^2,\quad x=-Z^2.
\]

The leading coefficient of h is exactly one: the two factors (-1)^D
from the displayed exterior sign and the substitution into monic H
multiply to one. The inverse original coordinates are

\[
 s_1=\tfrac12+\tfrac{Z+r}{2},\qquad
 s_2=\tfrac12+\tfrac{Z-r}{2}.
\]

Write the unique even/odd expansion in r as

\[
 h((S+r)/2)=H_0(S,\Delta)+rH_1(S,\Delta).
\]

Since h is even about 1/2, H_0 is even in Z and H_1 is odd in Z.
Thus there are unique polynomials A_0,A_1 in R=C[x,Delta] such that
H_0=A_0(-Z^2,Delta) and H_1=Z A_1(-Z^2,Delta). Put Q=Delta A_1.
PR17's swap-invariant quotient is precisely

\[
 B=\mathbb C[Z,\Delta]/(A_0(-Z^2,\Delta),ZQ(-Z^2,\Delta)).
\]

To verify the underlying ideal without discarding any odd term, write a
polynomial in r uniquely as a_even(S,r^2)+r a_odd(S,r^2). Averaging
H_0 a+rH_1 b under r -> -r gives H_0 a_even+Delta H_1 b_odd.
Conversely both displayed generators belong to the original ideal
(h(s_1),h(s_2)). Averaging over a group of order two is exact over C:
an invariant quotient class can be lifted and its lift averaged. This
proves the stated invariant quotient with the original coefficients.

As an R-module C[Z,Delta] is R direct-sum ZR. In the ideal above, the
even part of A_0(a_e+Za_o)+ZQ(b_e+Zb_o) is A_0a_e-xQb_o, and the odd
part is Z(A_0a_o+Qb_e). Consequently

\[
 B=B_e\oplus ZB_o,\qquad
 B_e=R/(A_0,xQ),\qquad B_o=R/(A_0,Q).
\]

The actual operator Z=S-1 on this direct sum is

\[
 (b,c)\longmapsto(-\alpha(c),\beta(b)),
 \qquad\alpha:B_o\to B_e,\ [p]\mapsto[xp],\qquad
 \beta:B_e\to B_o,\ [p]\mapsto[p].
\]

The minus sign is required by Z^2=-x. In particular alpha beta is
multiplication by x on B_e and beta alpha is multiplication by x on B_o.

## 2. Dimensions with all multiplicities retained

Put y_i=s_i-1/2. Since h is monic even of degree 2D, the classes
y_1^i y_2^j, 0<=i,j<2D, form a basis of the original tensor algebra.
Swap-invariant orbit sums, with the diagonal vector used once and each
off-diagonal pair summed with coefficient one, form a basis indexed by
0<=i<=j<2D. Reflection (y_1,y_2)->(-y_1,-y_2) acts on its (i,j) member
by (-1)^(i+j). There are D even and D odd exponents between 0 and 2D-1.
The even members therefore number

\[
 2\binom{D+1}{2}=D(D+1),
\]

and the odd members number D^2. This proves

\[
 \dim B_e=D(D+1),\qquad\dim B_o=D^2,
\]

without imposing reducedness or making any assumption that roots are
distinct. The same argument proves that both quotient algebras are finite.

## 3. Both exact sequences and their complete kernel map

At x=0, the even coefficient in the original h relation is

\[
 A_0(0,\Delta)=(-1)^D H(-\Delta/4)=:T(\Delta).
\]

The polynomial T is nonzero of degree D, with its original factor
(-1)^D and argument -Delta/4 retained. Hence x does not divide A_0.
Also A_0 and Q are coprime in R. Otherwise an irreducible common factor
would divide both generators of (A_0,xQ), and the finite-dimensional
algebra B_e would map onto R/(p) for a nonconstant irreducible p.
That latter quotient is infinite-dimensional: if p depends on x then
C[Delta] injects into it, while if p depends only on Delta then C[x]
injects into it. This contradiction proves the coprimality.

For alpha, suppose xf=A_0u+xQv. Then x(f-Qv)=A_0u. Since x is coprime
to A_0 in the polynomial UFD, x divides u. Dividing this equality by x
gives f in (A_0,Q). This proves alpha is injective; well-definedness
follows immediately by multiplying the two defining relations of B_o
by x. Its cokernel is obtained by setting x=0 in B_e, namely C[Delta]/(T).
The exact quotient map is [f(x,Delta)] -> [f(0,Delta)]. Thus

\[
 0\longrightarrow B_o\xrightarrow{\alpha}B_e
   \xrightarrow{f\mapsto f(0,\Delta)}\mathbb C[\Delta]/(T)
   \longrightarrow0.
\]

The quotient beta is onto. Its kernel is the image of the ideal (Q).
Consider the R-module map

\[
 \iota:\mathbb C[\Delta]/(T)\longrightarrow B_e,
 \qquad[q(\Delta)]\longmapsto[Q(x,\Delta)q(\Delta)].
\]

This map retains the **whole polynomial Q before taking its class in
B_e**. To prove well-definedness directly, write A_0=T+xL. Then
QT=QA_0-xQL belongs to (A_0,xQ). Also xQ=0 in B_e, so any polynomial
coefficient multiplying Q can be replaced by its x=0 value. For
injectivity, if Qf=A_0u+xQv then Q(f-xv)=A_0u. Coprimality of Q and A_0
implies Q divides u. Dividing gives f in (A_0,x). The converse inclusion
is immediate. Thus the annihilator of [Q] is exactly (A_0,x), proving
injectivity and identifying its domain precisely. Surjectivity onto
ker beta follows from the description of that kernel as the image of
(Q). Therefore

\[
 0\longrightarrow\mathbb C[\Delta]/(T)
   \xrightarrow{\iota}B_e\xrightarrow{\beta}B_o\longrightarrow0.
\]

Replacing a **coefficient multiplying Q** by its x=0 value is justified
by xQ=0. Replacing **Q itself** by Q(0,Delta) has no such justification:
its difference from Q is divisible by x, whereas x does not annihilate
all of B_e. The following explicit fibres show the resulting error.

## 4. Repeated-root calibrations H(X)=(X-eta)^2, eta=+1 or -1

Let a=1 for eta=-1 and a=i for eta=1, so a^2=-eta. The exact original
packet is h(s)=((s-1/2)^2+eta)^2, with both roots 1/2+a and 1/2-a
retained to order two. Direct expansion in the original half coordinates
gives

\[
 \begin{split}
 A_0(x,\Delta)&=\frac{(\Delta-x+4\eta)^2-4x\Delta}{16},\\
 A_1(x,\Delta)&=\frac{\Delta-x+4\eta}{4},\\
 Q(x,\Delta)&=\frac{\Delta(\Delta-x+4\eta)}4,\qquad
 T(\Delta)=\frac{(\Delta+4\eta)^2}{16}.
 \end{split}
\]

Here dim B_e=6, dim B_o=4, and both kernel and cokernel have dimension
two. The factors 1/16 and 1/4 are present in the source expressions and
the kernel map; they have not been replaced by unspecified units.

On a same-root pair choose y_1=a+u, y_2=a+v with u^2=v^2=0. Its
swap-invariant algebra is C[z]/(z^3), z=u+v, since z^2=2uv. It has

\[
 Z=2a+z,\quad x=4\eta-4az-z^2,\quad\Delta=-z^2.
\]

In this algebra the original relation gives Q=0, while

\[
 Q(0,\Delta)=-\eta z^2\ne0.
\]

Reflection exchanges the two same-root pair components. It follows
that this same C[z]/(z^3) component is present in both B_e and B_o,
and beta is the identity on it. Thus Q(0,Delta) is not even in ker beta.

On the mixed pair choose y_1=a+u, y_2=-a+v, still with u^2=v^2=0.
After reflecting and swapping back into this chosen component,
(u,v) maps to (-v,-u). Its even subalgebra is C[w]/(w^3), w=u-v,
with w^2=-2uv. The original coordinates are

\[
 Z=u+v,\quad x=w^2=-2uv,\quad
 \Delta=-4\eta+4aw+w^2.
\]

The odd part is the one-dimensional span of Z; on it x=0 and
Delta=-4eta. Hence beta on this mixed component is evaluation at w=0,
and alpha sends its scalar input to x=w^2. The complete kernel generator
and its prematurely specialized expression are respectively

\[
 \begin{split}
 Q&=-4a\eta w-4\eta w^2
      =-4a\eta(u-v)+8\eta uv,\\
 Q(0,\Delta)&=-4a\eta w-5\eta w^2
      =-4a\eta(u-v)+10\eta uv.
 \end{split}
\]

The second-order difference is eta w^2=-2eta uv for Q-Q(0,Delta).
It is nonzero. Moreover

\[
 Q(\Delta+4\eta)=16w^2=-32uv\ne0,\qquad
 Q(\Delta+4\eta)^2=0.
\]

Thus the exact map from C[Delta]/((Delta+4eta)^2) retains the full
length-two kernel, including the terminal nilpotent vector. This mixed
component changes the second-order coefficient if Q is specialized
prematurely; the same-root component above proves that the resulting
global map is no longer a kernel map at all.

For eta=-1, the especially simple formulas are

\[
 x=-2uv,\quad\Delta=4+4(u-v)-2uv,\quad
 Q=4(u-v)-8uv,\quad Q(0,\Delta)=4(u-v)-10uv.
\]

## 5. Explicit full-jet bases and the global witness

Exact bases are

\[
 (1,\Delta,\Delta^2,\Delta^3,\Delta^4,x)\quad\text{for }B_e,
 \qquad(1,\Delta,\Delta^2,x)\quad\text{for }B_o.
\]

They can be verified without discarding local derivatives. Evaluate the
first list on the same-root chart in the coefficient basis (1,z,z^2)
and on the mixed even chart in the basis (1,w,w^2). The resulting 6 by 6
matrix has determinant 2^20 for each eta. For eta=-1 it is

\[
 \begin{pmatrix}
 1&0&0&0&0&-4\\
 0&0&0&0&0&-4\\
 0&-1&0&0&0&-1\\
 1&4&16&64&256&0\\
 0&4&32&192&1024&0\\
 0&1&24&240&1792&1
 \end{pmatrix}.
\]

For eta=1 the last column in its first two rows is (4,-4i), the
mixed constant row is (1,-4,16,-64,256,0), the mixed linear row is
(0,4i,-32i,192i,-1024i,0), and the mixed quadratic row is
(0,1,-24,240,-1792,1); the third row remains unchanged. Its determinant
is again 2^20. For the odd list, use the same-root chart and the mixed
scalar chart (x,Delta)=(0,-4eta). The determinant is 64a, nonzero.
Together with the already proved dimensions these calculations prove
the basis statements.

In these odd coordinates the failure of the specialized generator is
particularly explicit:

\[
 \beta(Q(0,\Delta))=\tfrac14\Delta^2+\eta\Delta\ne0,
 \qquad\beta(Q)=0.
\]

Every coefficient displayed here is over Q when eta=-1; eta=1 merely
uses the exact root a=i for the local coordinate charts, while both
global quotient matrices remain rational.

## 6. A complete local-unit calibration

The original arithmetic unit is transported through these same maps.
Indeed g(1/2+y)=g(1/2-y) and h(1/2+y)=h(1/2-y), so the entire quotient
g/h and its full remainder unit upsilon_h are reflection-even. Uniqueness
of the degree-below-d remainder under the even monic h proves that its
polynomial representative is even as well. The tensor product of the
two full units is therefore an invertible element U of B_e. It acts on
B_o by beta(U), and on C[Delta]/(T) by U(0,Delta) modulo T. Both images
are units because these are unital quotient homomorphisms. Every map in
the two exact sequences is R-linear. In particular,

\[
 U\,\iota(q)=UQq=Q\,U(0,\Delta)q
       =\iota(U(0,\Delta)q),
\]

since U-U(0,Delta) is divisible by x and xQ=0. This identity is the
exact descent of the original full unit and all its retained jets;
the full Q is present on both sides. It does not replace the arithmetic
unit by a chosen scalar or by the following example.

To check that these maps also retain derivatives of a full unit, take
the explicit even calibration unit upsilon(y)=2+y^2 on the original
single-factor packet. It is invertible at both double roots, with value
c=2-eta, equal to 3 or 1. Its tensor product descends exactly as

\[
 U(x,\Delta)=4-x+\Delta+\frac{(x+\Delta)^2}{16}.
\]

In the mixed full-jet chart it is

\[
 U=c^2+2acw-2\eta w^2
   =c^2+2ac(u-v)+4\eta uv.
\]

Its inverse retains all three terms:

\[
 U^{-1}=c^{-2}-2ac^{-3}w-2\eta c^{-4}w^2.
\]

Multiplying these expressions modulo w^3 gives exactly one. For the
eta=-1 model the unit is 9+6(u-v)-4uv and its inverse is
1/9-2(u-v)/27-4uv/81. The checker verifies the full multiplication
matrices and the commutative diagrams through alpha, beta, iota and the
cokernel map. This is an explicit finite calibration of unit transport;
it is not a replacement for the actual arithmetic unit j_h(g/h).

## 7. Reproducible checks and scope

`checks/spectral_square_parity_independent.py` makes **86 exact checks**
in each ordinary mode. They cover both eta values, original coordinate
expansions, quotient dimensions, every map and composition, kernel and
cokernel actions, both full-jet chart determinants, the nonzero
second-order witnesses, and the complete unit diagrams. Normal and
optimized runs both pass 86/86.

Each negative run replaces Q by Q(0,Delta) only in the selected kernel
map test. Normal and optimized negative runs both exit 1 with exactly
the two corresponding kernel-map failures. The conditions do not use
Python assertions and remain active under `python -O`.

The four receipts are:

- `checks/spectral_square_parity_independent.json`
- `checks/spectral_square_parity_independent_optimized.json`
- `checks/spectral_square_parity_independent_negative.json`
- `checks/spectral_square_parity_independent_negative_optimized.json`

The general exact-sequence proofs are Sections 1–3 above. The finite
checks supplement those proofs and retain repeated-root nilpotents. No
analytic half-line norm result or actual xi-zero claim is made here.
