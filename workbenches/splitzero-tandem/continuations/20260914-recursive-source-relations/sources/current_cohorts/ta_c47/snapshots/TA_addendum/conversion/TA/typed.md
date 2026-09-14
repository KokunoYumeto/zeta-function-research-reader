# Which analytic pole classes belong to the original theta source?

13 September 2026. This is the next calculation after AP1--26. It keeps the
original one-factor arithmetic source, its Mellin measure and mass, and computes
both its Hilbert admission and its strong-Schwartz admission. The resulting
complexes, their residue images, their exact source maps and their theta-boundary
defects are displayed. No freely chosen metric or hypothetical zero replaces
the arithmetic input.

## 1. Original source, fixed parameters, and the exact norm

Retain the full actual packet $h$ of degree $d>0$, $g=2\xi$, the entire function
$v_h=g/h$, and the original $F_h$ in the strong Schwartz source $B$ with Mellin
transform $v_h$. Retain the complete Taylor-unit polynomial $\nu$ representing
$\upsilon_h=j_h(g/h)$; $\gcd(h,\nu)=1$. Let $P_\nu$ be its distinct roots. At every
$p\in P_\nu$ put $m_p=\operatorname{ord}_p v_h$, a finite nonnegative integer. Since $h(p)\ne0$,
this is exactly $\operatorname{ord}_p g$, not a multiplicity of $\nu$ or a presumed simple zero.

Use $s$ for the Mellin coordinate and $y$ for its critical-line imaginary part.
The independent geometric parameters are $u\in\mathbb C^*$ and $t\in\mathbb C$. Distinguish

$$
D_x=-x\frac{d}{dx},\qquad D_{\mathrm{exp}}=u\frac{d}{ds}+h(s)-t,\qquad L=u\frac{d}{dt}-s.\tag{TA1}
$$

On rational coefficients $R\in\mathbb C[s,\nu^{-1}]$, the stipulated original Hilbert norm is

$$
\|V_{h,\mathrm{rat}}R\|^2=\frac{1}{2\pi}\int_{\mathbb R}|v_h(1/2+iy)R(1/2+iy)|^2\,dy.\tag{TA2}
$$

When finite, inverse Mellin on this line defines $V_{h,\mathrm{rat}}R$ in $L^2(\mathbb R_+,dx)$.
Indeed logarithmic coordinates $x=e^z$ turn $F(x)$ into $e^{z/2}F(e^z)$, whose
Fourier Plancherel identity is precisely TA2. No total mass is divided out.
For polynomial $R$ this is exactly $R(D_x)F_h$, the original source map.

## 2. Complete Hilbert admission, including zeros on the observation line

Partition $P_\nu$ into $O=\{p:\operatorname{Re}p\ne1/2\}$ and $C=\{p:\operatorname{Re}p=1/2\}$. Let $\mathrm{PP}_p^{\le n}$
be the span of $(s-p)^{-1},\ldots,(s-p)^{-n}$, and $\mathrm{PP}_p$ the union over $n$.
The zero bound $n=0$ means the zero space, not a discarded supported point.

The rational coefficients of finite TA2 norm are exactly

$$
A^1=\mathbb C[s]+\bigoplus_{p\in O}\mathrm{PP}_p+\bigoplus_{p\in C}\mathrm{PP}_p^{\le m_p}.\tag{TA3}
$$

To prove necessity at $p=1/2+iy_p$, write $v_h(s)=(s-p)^{m_p}a(s)$,
where $a(p)\ne0$, and $R(s)=(s-p)^{-n}c(s)$, where $c(p)\ne0$. Along the line,
the squared modulus is bounded above and below by positive constants times
$|y-y_p|^{2(m_p-n)}$ near $p$. Its integral is finite exactly when
$2(m_p-n)>-1$, or, because the orders are integers, $n\le m_p$. The leading
coefficient cannot be cancelled by principal parts at another point.

There are no local line singularities from $O$. Outside a fixed compact interval,
any rational $R$ has at most polynomial growth. The actual Mellin transform $v_h$
is rapidly decreasing on every vertical strip, as follows from $F_h$ in $B$;
equivalently its gamma decay gives more than the required line decay.
Thus every coefficient described in TA3 has finite norm, proving sufficiency.

The exact domain making $D_{\mathrm{exp}}$ an admitted differential is

$$
\begin{aligned}A^0&=D_{\mathrm{exp}}^{-1}(A^1)\\&=\mathbb C[s]+\bigoplus_{p\in O}\mathrm{PP}_p+\bigoplus_{p\in C}\mathrm{PP}_p^{\le\max(m_p-1,0)}.\end{aligned}\tag{TA4}
$$

For a pole of order $n\ge1$, $D_{\mathrm{exp}}R$ has the uncancellable leading pole
$-un c(p)(s-p)^{-n-1}$. Hence at a line point its image is admitted exactly
when $n+1\le m_p$. A polynomial has polynomial image and is always admitted.
This proves TA4 and also $A^0\subset A^1$ without any extra domain assumption.

The two-term complex $[A^0\xrightarrow{D_{\mathrm{exp}}}A^1\,ds]$ is consequently the original
norm-admitted subcomplex of AP's analytic localization at fixed $u\ne0$.
This is a graph-domain calculation, not an assertion that all finite-norm
coefficients form a differential-invariant space in both degrees.

## 3. Its entire cohomology and exact inclusion into the analytic family

Put $S=O\cup\{p\in C:m_p\ge1\}$ and $Z=\{p\in C:m_p=0\}$.
Use the actual weight $w=\exp((\Phi(s)-ts)/u)$, with $\Phi'=h$ and its original
constant. AP's exact residue map restricts to give

$$
\begin{gathered}0\longrightarrow H_{\mathrm{pol}}\longrightarrow H^1(A)\xrightarrow{\operatorname{Res}_w}\mathbb C^S\longrightarrow0,\qquad\text{(TA5)}\\0\longrightarrow H^1(A)\longrightarrow H_{\mathrm{loc}}\xrightarrow{\operatorname{Res}_w|_Z}\mathbb C^Z\longrightarrow0.\qquad\text{(TA6)}\end{gathered}
$$

Here $H^0(A)=0$, and a basis of $H^1(A)$ is the original polynomial basis
$1,s,\ldots,s^{d-1}$, followed by $1/(s-p)$ for $p\in S$.

For full proof, the highest-pole argument makes $D_{\mathrm{exp}}$ injective on rational
functions, followed by its leading-degree argument on polynomials. If an
admitted $F$ equals $D_{\mathrm{exp}}Q$ in the larger localized complex, TA4 forces $Q$ to
belong to $A^0$. Thus the induced map on $H^1$ has no kernel. Subtract from an
admitted $F$ its weighted residues using $(\operatorname{Res}_wF)_p/(w(p)(s-p))$ for $p\in S$.
At a point with bound $m_p$, AP's log-free local primitive then has pole order
at most $m_p-1$. Its sum of principal parts belongs to $A^0$. Subtracting its
$D_{\mathrm{exp}}$ image leaves a polynomial and proves the kernel assertion in TA5.
Those simple-pole lifts prove surjectivity. Independence follows by residues
and then polynomial cohomology. Finally AP's full residue decomposition shows
that precisely the classes with zero $Z$-residues have such representatives,
proving TA6.

All original $m_p$ occur in the two chain spaces and in their local primitive
maps. One coordinate per admitted point is the computed cohomology, not a
replacement of the original zero orders by one.

Because $L$ does not increase finite pole order and commutes with $D_{\mathrm{exp}}$, it
preserves $A^0$ and $A^1$. Its connection on TA5 is exactly the submatrix of AP:

$$
L=u\frac{d}{dt}-\begin{bmatrix}A(t)&B_S\\0&\operatorname{diag}(p)_{p\in S}\end{bmatrix},\tag{TA7}
$$

where each column of $B_S$ is the original constant-polynomial column. Its
weighted-residue factors $w(p)$, its entire upper-right scaling integral and
its oriented $2\pi i$ loop periods are the corresponding AP formulas restricted
to $S$. No new connection or residue scaling is chosen.

## 4. Strong-Schwartz admission is an actual full-zero packet construction

The original source is

$$
B=\left\{F\text{ smooth on }\mathbb R_+:\ \begin{gathered}\sup_{x>0}x^b|D_x^jF(x)|<\infty\\\text{for every integer }b\text{ and }j\ge0\end{gathered}\right\}.\tag{TA8}
$$

Its Mellin transforms are entire: for $s\text{ in a compact set}$ the bounds at zero
and infinity dominate the integral and all its logarithmic derivatives.
Therefore $V_{h,\mathrm{rat}}R$ can belong to $B$ only when every finite pole of $v_hR$
is removable, at all $p\in P_\nu$, not just on the observation line. Agreement
of its entire Mellin transform with $v_hR$ on a nonsingular segment of the
critical line extends to the connected punctured plane by the identity theorem,
which proves the necessity of the removable-pole assertion.

Define the actual polynomials

$$
\begin{aligned}S_B&=\{p\in P_\nu:m_p>0\},\\\kappa(s)&=\prod_{p\in S_B}(s-p)^{m_p},\\\kappa_0(s)&=\prod_{p\in S_B}(s-p)^{m_p-1},\\b(s)&=\kappa/\kappa_0=\prod_{p\in S_B}(s-p),\\c(s)&=\sum_{p\in S_B}(m_p-1)b(s)/(s-p),\\H(s)&=h(s)\kappa(s).\end{aligned}\tag{TA9}
$$

Empty products equal one and the empty sum is zero. These are products of
the specified monic factors, not renormalizations of an arbitrary leading
coefficient. Since $\gcd(h,\nu)=1$, the roots of $h$ and $\kappa$ are disjoint.
$H$ therefore selects only actual zeros of $g$, retaining their complete orders.

All entire-admitted rational coefficients are exactly $\kappa^{-1}\mathbb C[s]$.
This follows either from partial fractions with the full order bounds, or
by multiplying by $\kappa$: the resulting rational function has no finite poles
and is polynomial. Conversely $P/\kappa$ has at most the prescribed orders.

Sufficiency for the original $B$ follows through its existing Euler inverses,
without a new space-identification assumption. Apply the original $S_\rho$
inverses successively to $\Theta\phi_*$ through every full factor of $H$. At each
step the remaining Mellin zero supplies the required kernel condition. Their
already proved source map gives $F_H\in B$ with Mellin transform $g/H$. Therefore

$$
\begin{aligned}V_{h,\mathrm{rat}}(P/\kappa)&=P(D_x)F_H,\\M(P(D_x)F_H)&=gP/H=v_hP/\kappa.\end{aligned}\tag{TA10}
$$

Every term on the right is an original strong-Schwartz theta-source vector.
This proves the converse and the exact source realization, not merely finite
norm. The differential graph domain of this strong-source degree-one space is
$\kappa_0^{-1}\mathbb C[s]$, by the same highest-pole calculation as TA4 at every $p$.

Thus the strong-source complex is the explicit subcomplex

$$
[\,\kappa_0^{-1}\mathbb C[s]\xrightarrow{D_{\mathrm{exp}}}\kappa^{-1}\mathbb C[s]\,ds\,].\tag{TA11}
$$

It injects into the Hilbert-admitted and full analytic cohomologies with no
extra kernel, by the same $D_{\mathrm{exp}}$-preimage proof. Its residue image is exactly
$\mathbb C^{S_B}$. In particular a $\nu$-root off the critical line with $m_p=0$ is admitted
by the Hilbert norm but not by $B$; its exact omitted coordinate is its AP residue.

## 5. Polynomial coordinates, source maps and every retained boundary defect

Use the literal maps $Q\longmapsto Q/\kappa_0$ in degree zero and $P\longmapsto P/\kappa$ in
degree one. They carry TA11 to a polynomial complex with differential

$$
\begin{aligned}E(Q)&=\kappa D_{\mathrm{exp}}(Q/\kappa_0)\\&=ubQ'+[b(h-t)-uc]Q.\end{aligned}\tag{TA12}
$$

The quotient $\kappa_0'/\kappa_0=\sum_p(m_p-1)/(s-p)$ proves this identity with
all orders and the negative derivative term retained. Since $b$ and $h$ are the
specified monic polynomials, the leading term of $E(Q)$ has degree
$\deg Q+d+|S_B|$ and unchanged leading coefficient. Every other term has lower
degree. Thus $E$ is injective and its cokernel has the unique polynomial basis
of degrees less than $d+|S_B|$, by terminating leading-term reduction.

The original polynomial exponential complex maps into it by the exact square

$$
\begin{gathered}\begin{array}{ccc}\mathbb C[s]&\xrightarrow{D_{\mathrm{exp}}}&\mathbb C[s]\\{\scriptstyle\text{multiplication }\kappa_0}\downarrow&&\downarrow{\scriptstyle\text{multiplication }\kappa}\\\mathbb C[s]&\xrightarrow{E}&\mathbb C[s]\end{array},\\E(\kappa_0Q)=\kappa D_{\mathrm{exp}}Q.\end{gathered}\tag{TA13}
$$

Leibniz differentiation proves this directly, or use the denominator maps.
The original arithmetic source is carried identically, since
$V_{h,\mathrm{rat}}((\kappa P)/\kappa)=P(D_x)F_h$. No map here sends supported zero to $\tau$
or changes the base point; lift each displayed linear map on its original mask.

There is also an exact arithmetic-quotient map, with its boundary value fully
retained. Write $E_H=\mathbb C[s]/(H)$, $\upsilon_H=j_H(g/H)$, and use the existing full
packet section $\sigma_H:E_H\longrightarrow Q=B/\Theta V$. For the original full jet $J_H$,

$$
\begin{aligned}J_HV_{h,\mathrm{rat}}(P/\kappa)&=\upsilon_H[P]_H,\\qV_{h,\mathrm{rat}}(P/\kappa)&=\sigma_H(\upsilon_H[P]_H).\end{aligned}\tag{TA14}
$$

To justify the second equation, $H(D_x)P(D_x)F_H=\Theta(P(D_x)\phi_*)$
by Mellin identity and injectivity, so its $Q$-class lies in $Q[H(D_x)]$. On that
actual submodule the original full-jet map and $\sigma_H$ are inverse. Thus the
displayed equation follows from the first one, which is the literal product
of Taylor series. Restriction to the original $h$-block gives

$$
j_h(\kappa\upsilon_HP)=\upsilon_h[P]_h.\tag{TA15}
$$

At each added $\kappa$-block, $\kappa P$ vanishes through its full order. The old
source inclusion therefore retains its actual full-unit $h$-component and has
zero added components, not a hidden mixture of old and new source classes.

For a geometric degree-zero numerator $Q$ the observed boundary is exactly

$$
qV_{h,\mathrm{rat}}(E(Q)/\kappa)=\sigma_H(\upsilon_H[E(Q)]_H).\tag{TA16}
$$

It need not be zero. TA16 is the calculated defect preventing an unproved
descent from geometric de Rham cohomology to the original theta quotient.
The cochain source map, its full-unit jet value and its entire residual
boundary have all been supplied; no false cohomology intertwiner replaces them.

At the fixed-domain specialization $u=t=0$, $E=bh$. The quotient of the original
arithmetic $E_H$ by its ideal $(bh)/(H)$, transported by the unit $\upsilon_H$,
is exactly the geometric polynomial quotient $\mathbb C[s]/(bh)$. At an added root $p$
this ideal is $(s-p)/(s-p)^{m_p}$; at an original $h$-root its component is zero.
This computes the complete endpoint kernel, including every removed higher
jet, instead of identifying the two quotients outright. For $m_p=1$ that
component is zero. Its rank count is $d+|S_B|$, with no deletion from the
larger original $E_H$ before the specified quotient map.

The fixed pair TA11 was derived for $u\ne0$. At $u=0$, recomputing the maximal
graph domain allows all coefficients in $\kappa^{-1}\mathbb C[s]$, since $h-t$ has no pole;
that is a different degree-zero domain. At $u=t=0$ its localized cohomology
has rank $d$. The fixed-domain specialization just calculated has rank $d+|S_B|$.
Both domains and the exact endpoint quotient are explicit; no flatness of
the recomputed graph domain is asserted.

## 6. The actual theta Gram and finite source cost

For the literal denominator frame TA10, TA2 becomes the exact identity

$$
\begin{gathered}\|V_{h,\mathrm{rat}}(P/\kappa)\|^2=\int_{\mathbb R}|P(1/2+iy)|^2w_H(y)\,dy,\\w_H(y)=|(g/H)(1/2+iy)|^2/(2\pi),\qquad\int w_H=\mu_H.\end{gathered}\tag{TA17}
$$

All removable values on the line are filled by the original entire $g/H$.
This is the already specified arithmetic convolution seed for the actual
extended packet $H$, with its own full mass $\mu_H$, not a unit-mass replacement.
For any finite numerator degree $N$, the exact Gram is

$$
(M_{H,N})_{ij}=\int_{\mathbb R}\overline{(1/2+iy)^i}(1/2+iy)^jw_H(y)\,dy,\qquad0\le i,j\le N.\tag{TA18}
$$

It is positive definite: a nonzero polynomial is nonzero outside a finite set,
and the nonzero entire $g/H$ is nonzero almost everywhere on the line.
All moments converge by the original rapid vertical decay. In an arbitrary
specified finite rational basis $R_j$, the unchanged norm instead has matrix
$\int\overline{R_i}R_jw_h$; TA17--18 are its exact denominator-coordinate
pullback, not a change of norm.

Let $E_N$ be the coefficient matrix of TA12 from degrees $\le N$ to degrees
$\le N+d+|S_B|$. The full source cost of the actual geometric boundary is

$$
\|V_{h,\mathrm{rat}}(E(Q)/\kappa)\|^2=Q^*E_N^*M_{H,N+d+|S_B|}E_NQ.\tag{TA19}
$$

This includes $u$, $t$, every $m_p$ through $c$, and all cross terms. Its arithmetic
class is TA16. If $G_H$ is an existing canonical quotient Gram at an admitted
cutoff and $T_N$ is the literal matrix $Q\longmapsto\upsilon_H[E(Q)]_H$, the quotient
cost is exactly $Q^*T_N^*G_HT_NQ$. No new quotient metric is selected.
No uniform bound on these actual matrices is inferred from their positivity.

Completed result: all analytic pole classes have their exact original-Hilbert
admission test; those with genuine strong-Schwartz source representatives are
realized by an actual enlarged full-zero packet. Their complex, residues,
source Gram and arithmetic boundary defect are explicitly calculated.

## 7. The connection in the same arithmetic numerator frame

Write $r=|S_B|$ and $q=d+r$. In the degree-one numerator frame
$f_j=s^j/\kappa$, $0\le j<q$, the actual connection is

$$
\begin{aligned}L&=u\frac{d}{dt}-A_{\mathrm{adm}}(u,t),\\A_{\mathrm{adm}}&=\operatorname{Companion}(\chi_{\mathrm{adm}}),\\\chi_{\mathrm{adm}}(u,t;s)&=b(s)(h(s)-t)-uc(s).\end{aligned}\tag{TA20}
$$

Here Companion means the column-convention matrix taking $e_j\text{ to }e_{j+1}$
for $j<q-1$ and taking $e_{q-1}$ to minus the coefficient column of the
lower-degree part of the displayed monic polynomial. This specifies every
matrix entry without a basis convention left implicit.

Indeed $[L,E]=0$ on parameter-dependent polynomial numerators: the term
$[u\,d/dt,E]=-ub$ cancels $[-s,ub\,d/ds]=ub$, and all remaining commutators
vanish. Thus $L$ descends through the parameter-dependent cokernel. Its value
on $f_j$ is $-s^{j+1}/\kappa$. Only the last basis vector requires reduction,
and the exact reduction relation is $E(1)=\chi_{\mathrm{adm}}$. This proves TA20.
It does not assert that multiplication by $s$ alone descends on the fixed
quotient by the image of the differential operator $E$. Nor is $\chi_{\mathrm{adm}}$ being
declared an annihilator made of new actual zeros of $g$. It is the calculated
connection matrix in the already admitted arithmetic frame.

Here is its exact relation to AP's polynomial-plus-simple-pole frame.
Use that frame restricted to $S_B$, and denote its connection matrix by
$T_B=\begin{bmatrix}A(t)&B_{S_B}\\0&\operatorname{diag}(p)\end{bmatrix}$. Let $G(u,t)$ be the matrix whose jth column
is the AP coordinates of $[s^j/\kappa]$. Its residue-block entries are

$$
\begin{aligned}G_{(p,j)}&=\operatorname{Res}_p\bigl(w(s)s^j/\kappa(s)\,ds\bigr)/w(p)\\&=\frac{\left.\left(\dfrac{d}{ds}\right)^{m_p-1}\left[w(s)s^j/\kappa_p(s)\right]\right|_{s=p}}{(m_p-1)!w(p)},\\\kappa_p(s)&=\kappa(s)/(s-p)^{m_p}.\end{aligned}\tag{TA21}
$$

All $m_p$ derivatives, the original exponential weight, and its value $w(p)$
are retained. To compute the polynomial-block entries, subtract the simple
poles with these coefficients from $f_j$. The result has zero weighted
residue at every admitted point. Take AP's log-free local primitives,
keep their finite principal parts, and subtract their $D_{\mathrm{exp}}$ images. This
leaves a polynomial. Reduce it to $\text{degree less than }d$ with the original
leading-term reduction for $D_{\mathrm{exp}}$. These coefficients are exactly the
remaining entries of $G$. This is a finite formula for each column, not a
choice of an unspecified comparison map.

Both sets are proved bases of the same admitted cohomology, so $G$ is
invertible. The primitive calculations only divide by nonzero $u$, $w(p)$,
nonzero leading coefficients, and fixed nonzero differences of distinct
points. Their finite coefficients are therefore holomorphic for $u\ne0$ and
all $t$. Applying $L$ to each column, with its parameter dependence included,
gives the exact identity and finite scaling transport

$$
\begin{aligned}uG_t&=T_BG-GA_{\mathrm{adm}},\\A_{\mathrm{adm}}&=G^{-1}T_BG-uG^{-1}G_t,\\C_{\mathrm{adm}}(a;t)&=G(t)^{-1}C_B(a;t)G(t+ua).\end{aligned}\tag{TA22}
$$

The fixed $u$ is suppressed only in the last line's arguments. For proof of
that line, differentiate its right side with $\text{respect to }a$, use
$C_B'(a;t)=-C_B(a;t)T_B(t+ua)$, and then the first identity of TA22.
The derivative is $-C_{\mathrm{adm}}(a;t)A_{\mathrm{adm}}(t+ua)$ and the value at $a=0$ is $I$.
The uniqueness of this finite linear differential equation proves the
transport formula. Both endpoint frames and the derivative gauge term
are present; a pointwise similarity would omit an actual term.

These same numerator vectors are the actual source vectors $D_x^jF_H$
by TA10, so their original norm is the explicitly calculated $M_{H,q-1}$.
The cohomological frame change $G$, however, also used $D_{\mathrm{exp}}$ primitives.
Those primitive differences have exactly the source cost TA19 and the
full arithmetic image TA16. A norm isometry between arbitrary reduced
representatives is not silently inferred from a cohomology change of basis.
Thus TA20--22 supply the concrete arithmetic-frame connection, its exact
comparison with AP, and the already computed source-level discrepancy.

## 8. Exact recovery of the old canonical quotient metric

The comparison reaches the original quotient metric as well as individual
source vectors. Put $K=\deg\kappa$ and $D=\deg H=d+K$. Use the literal injection

$$
i_\kappa:\mathbb C[s]/h\longrightarrow\mathbb C[s]/H,\qquad[P]_h\longmapsto[\kappa P]_H.
$$

It is well-defined because $H=h\kappa$ and injective because the polynomial
ring has no zero divisors. Its image is the ideal $(\kappa)/(H)$. At the
old $h$-block it multiplies by the actual nonzero Taylor unit $j_h(\kappa)$;
at every new block it is zero through that block's full order. Composing
with $\upsilon_H$ yields precisely the original arithmetic unit $\upsilon_h$
by TA15, not a newly chosen identification of the $h$-component.

Let $R_{H,N}^{\mathrm{coef}}$ be the existing unique least-source-norm representative for
coefficient classes in $\mathbb C[s]/H$ among polynomials of degree at most $N$;
let $G_{H,N}^{\mathrm{coef}}$ be its Gram. Define $R_{h,N-K}^{\mathrm{coef}}$ and $G_{h,N-K}^{\mathrm{coef}}$ in precisely the
same way using the original weight $w_h$. Take $N\ge D-1$ so both quotient
maps are onto and both metrics are defined. Then, as maps and forms,

$$
\begin{aligned}R_{H,N}^{\mathrm{coef}}i_\kappa&=M_\kappa R_{h,N-K}^{\mathrm{coef}},\\i_\kappa^*G_{H,N}^{\mathrm{coef}}i_\kappa&=G_{h,N-K}^{\mathrm{coef}}.\end{aligned}\tag{TA23}
$$

where $M_\kappa$ is literal polynomial multiplication. These are the
original least-norm constructions, not newly selected quotient metrics.

For proof, a degree-at-most-$N$ representative $Q$ of $i_\kappa[P]_h$ has
$Q-\kappa P=HT$ for some polynomial $T$. Thus $Q=\kappa R$ with $[R]_h=[P]_h$
and $\deg R\le N-K$. Conversely every such $R$ gives an allowed $Q$. This is a
bijection between the two complete affine spaces of representatives,
including all their relation directions. Their norms agree exactly:

$$
\begin{gathered}\int|\kappa(s)R(s)|^2w_H(y)\,dy=\int|R(s)|^2w_h(y)\,dy,\qquad s=1/2+iy,\\w_h(y)=|\kappa(1/2+iy)|^2w_H(y).\end{gathered}\tag{TA24}
$$

The last identity is $g/h=\kappa g/H$, with the removable line values
filled by those entire functions. It retains both unnormalized masses;
neither mass is asserted equal to the other. Finite-dimensional positive
definiteness gives a unique minimizer in each affine space. The norm
bijection therefore proves the first identity of TA23, and polarization
proves its full Hermitian Gram identity, including cross terms.

Under the actual source maps the two minimizing polynomials give the
identical strong-Schwartz function:

$$
(R_{H,N}^{\mathrm{coef}}i_\kappa[P])(D_x)F_H=(R_{h,N-K}^{\mathrm{coef}}[P])(D_x)F_h,
$$

because $\kappa(D_x)F_H=F_h$ follows from the original Mellin transforms.
Thus TA23 is a calculated isometric inclusion of the original arithmetic
quotient observation into the extended-packet observation with the exact
degree shift $K$. It is stronger than a bound inferred from positivity.
For precision about full-unit coordinates, write $G_{H,N}^{\mathrm{jet}}$ for the
same canonical observation expressed in physical jet coordinates
$J_H=\upsilon_H\pi_H$. Then

$$
\begin{aligned}G_{H,N}^{\mathrm{coef}}&=M_{\upsilon_H}^*G_{H,N}^{\mathrm{jet}}M_{\upsilon_H},\\j&=M_{\upsilon_H}i_\kappa M_{\upsilon_h}^{-1},\\j^*G_{H,N}^{\mathrm{jet}}j&=G_{h,N-K}^{\mathrm{jet}}.\end{aligned}
$$

Here $M_\upsilon$ denotes multiplication by the indicated complete Taylor
unit, not its leading coefficient. TA15 proves that $j$ is exactly the
identity on the original $h$-block and zero on each added full $\kappa$-block.
These equations specify the equivalent metric statement in the physical
jet convention used for the arithmetic cost in TA19. No unit-coordinate
change is left implicit or omitted from a Gram pullback.

TA23 does not identify the extra quotient directions or their mixed Gram
entries with old directions. Those remain in the actual extended metric; the
geometric-boundary image TA16 and its source cost TA19 remain unchanged.

## Sources and verification scope

Root reread A1--A5 of the current `tex/arithmetic_input.tex`, including the
definition of $B$, $g=2\xi$, $\Theta\phi_*$, and the original Euler inverse. The full
A1--A19 source and its full-order section were read previously. AP1--26 is the
accepted analytic input, SHA256
357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652.
The independent collaborator derived and checked TA3--TA7, the global graph
domain and TA12--TA16 while root wrote their complete proofs and source-cost
formulas here. This note claims written mathematics, not new Lean execution,
numerical zero certification, a uniform estimate, or remote publication.
