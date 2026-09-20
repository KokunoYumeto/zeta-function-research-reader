# Independent proof of the polynomial and tensor coercivity estimates

Date: 2026-09-20. Scope: equations P1–P11 and J1–J11 in the supplied
`COMPLETE_PROOFS(2).md`, Sections 1–2. This file gives the complete independent
derivation within that scope. Sections 3–5 have not been audited here.

## Acceptance and precise scope

All numerical constants in P1–P11 are valid. J1–J11 are valid for the original
nested sources, a nonempty fixed divisor, positive fixed jet weights, and a
single section fixed at the four cutoffs. The formulas using the inverse of
the scalar minimum metric require its attained domain, namely N >= q-1.
The joint minimum itself exists for every N >= 0 because the section is onto.

One sentence requires a scope correction. The last paragraph of Section 2
extends all results to intermediate sources inside the same polynomial box.
The common metric bounds extend to every such source containing the section.
The nonnegative lower bound in J11 additionally requires that these sources
increase with N. Without this nesting, the enclosure gives the valid bound
`|R log det| <= 2 r_X W_k`, but it does not prove a nonnegative return.
The actual sources `X_N + Y_{k,eta}` are nested, so their stated J11 is valid.

For general multiplicities the exact tolerance cost is retained below.
Nothing here removes `log(1/eta)` from that cost when eta is allowed to shrink
arbitrarily. For simple factors, the metric has no higher jets and the cost
does not depend on eta.

The displayed maxima over roots and the degree `n_0=2d-1` in the supplied
formulas presuppose a nonempty divisor. This is the domain used below. No
convention for an empty root set is silently inserted.

## 1. Original spaces, coordinates, and physical unit

Let Z be a finite nonempty set of distinct nontrivial zeros of zeta, and let
each m_rho be its complete order in 2 xi. Put
\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\quad
d=\sum_\rho m_\rho,\quad d_\rho=m_\rho-1,\quad
d_{\max}=\max_\rho d_\rho.
\]
Fix a_rho > 0. The physical line is s=1/2+iy. In all norm integrals,
\[
\|P\|_{w_h}^2=\int_{\mathbb R}|P(1/2+iy)|^2
 \frac{|(2\xi/h)(1/2+iy)|^2}{2\pi}\,dy,
\]
\[
\|P\|_\sigma^2=\int_{\mathbb R}|P(1/2+iy)|^2
 \frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy.
\]
When a polynomial is displayed as a function of y, it means the exact
substitution Q(y)=P(1/2+iy). No density is divided by its mass.

The coefficient quotient is A_h=C[s]/(h), represented by polynomials of
degree below d. The divided-jet map is
\[
\mathsf H_h:A_h\longrightarrow
 \bigoplus_{\rho\in Z}\mathbb C[t_\rho]/(t_\rho^{m_\rho}),\qquad
[P]\longmapsto\left(\sum_{j=0}^{d_\rho}
 \frac{P^{(j)}(\rho)}{j!}t_\rho^j\right)_\rho.
\]
This is an isomorphism: its kernel consists precisely of multiples of h,
and its source and target both have dimension d. In these jets define
\[
\mathsf D_{h,\eta}[P]=\sum_{\rho,j}
a_\rho(j!)^2\binom{d_\rho}{j}\eta^{2j}
\left|\frac{P^{(j)}(\rho)}{j!}\right|^2,
\quad 0<\eta\le1,
\qquad T_\eta=\mathsf H_h^*\mathsf D_{h,\eta}\mathsf H_h.
\]
Here and below a positive matrix also denotes its quadratic form when the
argument is written in brackets.

Put f_h=2xi/h. It is entire and f_h(rho) is nonzero at every selected root,
because the complete order was removed. Multiplication by its truncated
Taylor series defines the invertible jet map U_h. Every coefficient is
retained:
\[
(U_h u)_{\rho,j}=\sum_{r=0}^j
 \frac{f_h^{(r)}(\rho)}{r!}\,u_{\rho,j-r}.
\]
With the physical metric D_phys=(U_h^{-1})^*D_{h,1}U_h^{-1},
\[
\|U_hu\|_{D_{\rm phys}}^2=u^*D_{h,1}u.
\]
The tensor identity is obtained by taking tensor powers of this exact
identity. Thus the later value constraint beta v and the physical constraint
\(U_h^{\otimes k}\beta v\) have equal specified norms; the physical unit and
its derivatives have not been discarded.

## 2. Gamma polynomial basis, mass, and multiplication bound

The Meixner–Pollaczek formulas used are DLMF 18.23.7, 18.19.8, and
18.19.9. Substitute lambda=1/4, phi=pi/2, x=y/2, and define
\[
p_m(y)=m!P_m^{(1/4)}(y/2;\pi/2).
\]
Then
\[
\sum_{m\ge0}\frac{p_m(y)}{m!}z^m
 =(1+z^2)^{-1/4}\exp(y\arctan z),\qquad |z|<1.
\tag{C1}
\]
The leading coefficient in y is one, as is also immediate by selecting the
highest y power in C1. The exact change dy=2dx in DLMF's orthogonality gives
\[
\langle p_m,p_l\rangle_\sigma=\delta_{ml}\gamma_m,
\qquad
\gamma_m=\sqrt{2\pi}\,m!(1/2)_m.
\tag{C2}
\]
Indeed the DLMF norm of P_m is
`2 pi Gamma(m+1/2)/(sqrt(2) m!)`; multiplying by `(m!)^2/pi`
gives C2. In particular M_sigma=gamma_0=sqrt(2 pi), exactly as in P10.

Differentiate C1 in z. Its right side satisfies
\[
(1+z^2)\partial_z C1=(y-z/2)C1.
\]
Comparison of coefficients gives, with p_{-1}=0,
\[
yp_m=p_{m+1}+m(m-1/2)p_{m-1}.
\tag{C3}
\]
Thus in the orthonormal basis e_m=p_m/sqrt(gamma_m), the off-diagonal
coefficient is alpha_m=sqrt(m(m-1/2)). If deg Q <= n, the two shifted
coefficient vectors in yQ have norms at most alpha_{n+1}||Q|| and
alpha_n||Q||. The triangle inequality yields
\[
\|yQ\|_\sigma\le(\alpha_{n+1}+\alpha_n)\|Q\|_\sigma
 \le2(n+1)\|Q\|_\sigma.
\tag{C4}
\]
For R=8(n+1), integration of `1_{|y|>R} <= y^2/R^2` now gives
\[
\int_{|y|>R}|Q(y)|^2\sigma(y)\,dy\le\frac1{16}\|Q\|_\sigma^2.
\tag{C5}
\]
This verifies P5, including its degree and constant.

## 3. Legendre localization and the excluded mass

DLMF 5.7.6 gives, for a>0 and t>=0,
\[
\operatorname{Im}\psi(a+it)=\frac{t}{a^2+t^2}
 +\sum_{j\ge1}\frac{t}{(j+a)^2+t^2}.
\]
The first summand is at most 1/(2a). The remaining summand is decreasing
as a function of j>=0, so its sum for j>=1 is at most
\[
\int_0^\infty\frac{t}{(x+a)^2+t^2}\,dx\le\pi/2.
\]
At a=1/4 this proves `|Im psi(a+it)| <= 2+pi/2 <4`.
Differentiating the actual density, with its factor y/2, gives
\[
\frac d{dy}\log\sigma(y)=-\operatorname{Im}\psi(1/4+iy/2).
\]
Complex conjugation handles negative y. Therefore, for |u-y|<=1,
\[
\sigma(y)\le e^4\sigma(u).
\tag{C6}
\]

Let L_m be the Legendre polynomial on [-1,1], with
`integral L_m^2=2/(2m+1)`. Its value at zero is 0 for odd m; for m=2j
it is `(-1)^j binom(2j,j)/4^j`, of modulus at most 1.
Expand the complete complex polynomial Q(y+t) in the orthonormal functions
`sqrt((2m+1)/2)L_m(t)`. Cauchy–Schwarz at t=0 gives
\[
|Q(y)|^2\le
 \left(\sum_{m=0}^n\frac{2m+1}{2}|L_m(0)|^2\right)
 \int_{y-1}^{y+1}|Q(u)|^2\,du
\le\frac{(n+1)^2}{2}\int_{y-1}^{y+1}|Q(u)|^2\,du.
\]
Multiply by sigma(y), use C6 inside the integral, and extend that integral
to the whole line. This proves P4 with exactly
\[
B_n=e^4(n+1)^2/2.
\tag{C7}
\]
Consequently every measurable excluded set E of length at most 1/(32B_n)
has `integral_E |Q|^2 sigma <= ||Q||_sigma^2/32`.

## 4. The zeta bound and all disk constants

Set g(s)=(s-1)zeta(s), which is entire. Taking n=1 in DLMF 25.2.10
and integrating its periodic B_3 remainder using B_4'=4B_3 gives
\[
\zeta(s)=\frac1{s-1}+\frac12+\frac{s}{12}
 -\frac{s(s+1)(s+2)}{720}
 -\frac{(s)_4}{24}\int_1^\infty\widetilde B_4(x)x^{-s-4}\,dx.
\tag{C8}
\]
Initially this integration is valid on the common convergence domain;
the resulting absolutely convergent integral extends the identity to
Re s > -3. The sign and coefficient of its boundary term follow from
`B_4(1)=-1/30` and `[-B_4(1)/4]=1/120` in the integration of B_3.
Since `B_4(t)=t^2(1-t)^2-1/30` on [0,1], its range lies in
`[-1/30,7/240]`; hence `sup |B_4|=1/30`.

If Re s >= -2, the absolute value of the integral in C8 is at most 1/30.
Put t=|s|, T=t+4>=4. Multiplication by s-1 yields the explicit estimate
\[
|g(s)|\le1+\frac{t+1}{2}+\frac{t(t+1)}{12}
 +\frac{t(t+1)^2(t+2)}{720}
 +\frac{t(t+1)^2(t+2)(t+3)}{720}
\le1+T/2+T^2/12+T^4/720+T^5/720<T^5.
\tag{C9}
\]
For the last inequality, division by T^5 bounds the right side by
`1/1024+1/512+1/768+1/2880+1/720 <1`.
At the removable point s=1 the same inequality follows by continuity.
This verifies P6.

The Euler product in Re s>1 gives
\[
|\zeta(2+ij)^{-1}|\le\prod_p(1+p^{-2})
 \le\prod_p(1-p^{-2})^{-1}=\zeta(2)<2.
\]
The last strict inequality also follows directly from the sum and the
integral comparison `sum_{m>=2}m^{-2}<integral_1^infty x^{-2}dx=1`.
Since |1+ij|>=1, `|g(2+ij)|>1/2`.

Fix an integer j with |j|<=R, and put f_j(z)=g(2+ij+z). On |z|<=4,
Re(2+ij+z)>=-2 and `|2+ij+z|+4 <= R+10`. Therefore C9 gives
\[
|f_j(z)|\le(R+10)^5\le M_n:=4(R+14)^5.
\tag{C10}
\]
Let L_n=log(2M_n), and let N_j be the number of zeros a of f_j in
|a|<3, counted with multiplicity. Jensen's formula at radii tending to
4 from below gives
\[
N_j\log(4/3)\le\log M_n-\log|f_j(0)|<L_n.
\]
No zero occurs at zero. Thus
\[
N_j\le K_n=\left\lceil L_n/\log(4/3)\right\rceil.
\tag{C11}
\]
This reasoning allows zeros on the circle of radius 4 by taking the
limit through radii avoiding their moduli.

Form the finite product
\[
B_j(z)=\prod_{|a|<3}\frac{3(z-a)}{9-\bar a z},
\qquad F_j(z)=f_j(z)/B_j(z),
\]
with multiplicities. All apparent poles of F_j at the listed zeros are
removable, and there are no zeros of F_j in |z|<3. On |z|=3 every
factor has modulus one, so the maximum principle gives `|F_j|<=M_n`
on the disk. Also `|B_j(0)|<=1`, hence `|F_j(0)|>1/2`.

The nonnegative harmonic function H=log(M_n/|F_j|) has H(0)<L_n.
To apply Harnack without any boundary regularity assumption, use every
radius r with 2<r<3 and then let r increase to 3. At |z|<=2,
\[
H(z)\le\lim_{r\uparrow3}\frac{r+2}{r-2}H(0)
 \le5L_n.
\]
Thus
\[
|F_j(z)|\ge M_ne^{-5L_n}=\frac1{32M_n^4},\qquad |z|\le2.
\tag{C12}
\]
For each removed zero, `|9-bar(a)z|<=15` on |z|<=2. Hence
\[
\left|\frac{3(z-a)}{9-\bar a z}\right|\ge|z-a|/5.
\tag{C13}
\]

The critical-line cell `j-1/2 <= y <= j+1/2` has relative coordinate
`z=-3/2+i(y-j)`, whose modulus is at most sqrt(5/2)<2.
Let
\[
m_n=2R+1,\qquad
\epsilon_n=(64B_nm_nK_n)^{-1},\qquad
c_n=(\epsilon_n/5)^{K_n}/(32M_n^4).
\]
The number epsilon_n/5 is below one. Outside the epsilon_n disks about
the listed zeros, C11–C13 imply `|g(1/2+iy)|>=c_n`.
Each disk cuts an interval of length at most 2epsilon_n from the real
y line. Across all m_n cells the total excluded length is at most
\[
2m_nK_n\epsilon_n=1/(32B_n).
\tag{C14}
\]
Counting a disk or an overlapping interval more than once can only
increase this upper bound. By C5 and C7, the retained part of [-R,R]
carries Gamma polynomial mass at least
`1-1/16-1/32=29/32` of the full mass, and therefore at least one half.
This establishes P7 with precisely the stated constants.

## 5. Lower and upper arithmetic comparisons

The defining identity
`2xi(s)=s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)` gives on the physical line
\[
\frac{w_h(y)}{\sigma(y)}=
 \frac{|s|^2}{\sqrt\pi}\left|\frac{g(s)}{h(s)}\right|^2,
 \qquad s=1/2+iy.
\tag{C15}
\]
This formula uses the entire removable value of g/h at selected roots.
Away from h=0 it is exactly P8 in its displayed fraction form.

Let `R_h=2+max_rho|rho-1/2|`. On |y|<=R,
\[
|h(1/2+iy)|\le(R+R_h)^d,\qquad |s|^2\ge1/4.
\]
The retained set contains no zero of g. In particular h is nonzero there,
so division is legitimate. C15 and the retained half-mass yield
\[
\|P\|_{w_h}^2\ge
\frac{c_n^2}{8\sqrt\pi(R+R_h)^{2d}}\|P\|_\sigma^2
=a_{h,n}\|P\|_\sigma^2.
\tag{C16}
\]

For the upper comparison, g/h is entire because h divides the actual
nontrivial-zero divisor of g. Consider the rectangle
`-1<=Re s<=2`, `|Im s|<=2R_h`. On its vertical sides, every
`|s-rho|>=1`, since `0<Re rho<1`. On its horizontal sides,
\[
|s-\rho|\ge2R_h-|\operatorname{Im}\rho|
 \ge2R_h-(R_h-2)=R_h+2>1.
\]
Thus |h|>=1 on the entire boundary. Also `|s|+4<=2R_h+6` there.
C9 and the maximum principle applied to the entire g/h prove
\[
|g/h|\le(2R_h+6)^5
\]
throughout the rectangle, including all removable values. On its critical
line segment, C15 consequently gives
\[
w_h/\sigma\le[(2R_h)^2+1](2R_h+6)^{10}.
\tag{C17}
\]

For |y|>=2R_h>=4, triangle inequalities give
\[
|s-\rho|\ge|y|-|\rho-1/2|\ge|y|/2,\quad
|h(s)|\ge(|y|/2)^d\ge1,
\]
and `|s|<=2|y|`, `|s|+4<=3|y|`. Hence C9 and C15 give
\[
w_h/\sigma\le(4\cdot3^{10}/\sqrt\pi)|y|^{12}
 \le2^{24}(1+y^2)^6.
\tag{C18}
\]
Combining C17 and C18 proves P9 with exactly
\[
C_h=\max\{2^{24},[(2R_h)^2+1](2R_h+6)^{10}\}.
\]
For every polynomial of degree at most m, C4 implies
`||(y+i)Q||_sigma <=(2m+3)||Q||_sigma`. Iteration at
`m=n,n+1,...,n+5` gives
\[
\|(y+i)^6Q\|_\sigma^2\le
 \prod_{r=0}^5(2n+2r+3)^2\|Q\|_\sigma^2
 \le(2n+15)^{12}\|Q\|_\sigma^2.
\]
Because `|(y+i)^6|^2=(1+y^2)^6`, P9 proves the upper half of P2
with the unchanged `b_{h,n}=C_h(2n+15)^{12}`.

Now `K_n=O(log(n+2))`, `log M_n=O(log(n+2))`, and
\[
-\log\epsilon_n=
\log64+\log B_n+\log m_n+\log K_n=O(\log(n+2)).
\]
The explicit logarithm of a_{h,n} is
\[
-\log a_{h,n}=
2K_n\log(5/\epsilon_n)+2\log32+8\log M_n
+\log(8\sqrt\pi)+2d\log(R+R_h).
\tag{C19}
\]
It is `O_h(log^2(n+2))`. Also
`log b_{h,n}=log C_h+12 log(2n+15)=O_h(log(n+2))`.
This proves P3 with no change to the constants.

## 6. The complete divided-jet bound

Let `r=n/(n+1)` and `u_n=(1/2)log(2n+1)`. On |z|=r the power series
for arctan gives
\[
|\arctan z|\le\sum_{l\ge0}\frac{r^{2l+1}}{2l+1}
=\operatorname{arctanh}r=u_n.
\]
Further,
\[
|1+z^2|^{-1/4}\le(1-r^2)^{-1/4}\le(n+1)^{1/4},
\qquad r^{-m}\le(1+1/n)^n\le e\quad(m\le n).
\]
Write `Z_h=max_rho|rho-1/2|` and `y_rho=(rho-1/2)/i`, so
`|y_rho|<=Z_h`. Cauchy's coefficient estimate applied to the j-th
divided y derivative of C1 gives
\[
\left|\frac{p_m^{(j)}(y_\rho)}{j!}\right|
\le m!\,e(n+1)^{1/4}(2n+1)^{Z_h/2}\frac{u_n^j}{j!}.
\tag{C20}
\]
The s derivative of `p_m((s-1/2)/i)` contributes the exact phase
`i^{-j}`, of modulus one. The inequality `m!/(1/2)_m<=2m+1`
holds by induction: its ratio at the next step is `(m+1)/(m+1/2)`,
and `(2m+1)(m+1)/(m+1/2)=2m+2<=2m+3`.

Expand Q in the orthonormal basis e_0,...,e_n and apply Cauchy–Schwarz
to its j-th divided derivative at y_rho. C2 and C20 give
\[
\left|\frac{P^{(j)}(\rho)}{j!}\right|^2
\le\|P\|_\sigma^2\frac{e^2}{M_\sigma}(n+1)^{1/2}
(2n+1)^{Z_h}\frac{u_n^{2j}}{(j!)^2}
 \sum_{m=0}^n(2m+1).
\]
The sum is `(n+1)^2 <=(n+1)(2n+1)`. Thus
\[
\left|\frac{P^{(j)}(\rho)}{j!}\right|^2
\le\|P\|_\sigma^2\frac{e^2}{M_\sigma}(n+1)^{3/2}
(2n+1)^{Z_h+1}\frac{u_n^{2j}}{(j!)^2}.
\tag{C21}
\]
Multiply by the original weights
`a_rho (j!)^2 binom(d_rho,j)` and sum over all roots and all jet orders.
The factorials cancel exactly; the remaining sum over j is
`(1+u_n^2)^{d_rho}`. Therefore
\[
\|J_hP\|_{\mathsf D_{h,1}}^2\le J_{h,n}\|P\|_\sigma^2,
\quad
J_{h,n}=\frac{e^2}{M_\sigma}(n+1)^{3/2}(2n+1)^{Z_h+1}
 \sum_\rho a_\rho(1+u_n^2)^{d_\rho}.
\tag{C22}
\]
Combining C22 and C16 gives P11 with
`Lambda_{h,n}=max{1,J_{h,n}/a_{h,n}}`. The fixed finite root set and
fixed weights give `log^+ J_{h,n}=O_h(log(n+2))`; C19 therefore proves
`log Lambda_{h,n}=O_h(log^2(n+2))`.

## 7. Tensor forms and exact collision coefficients

Let V_n be the full polynomial space of degree at most n with its
w_h inner product, and let J:V_n->A_h be the remainder map. C22 and C16
say that the finite operator
\[
J:(V_n,\|\cdot\|_{w_h})\longrightarrow(A_h,T_1)
\]
has squared operator norm at most Lambda_{h,n}. Tensoring its singular
value decomposition shows that the squared norm of \(J^{\otimes k}\) is at
most Lambda_{h,n}^k. This acts on the full Hilbert tensor product \(V_n^{\otimes k}\),
which is precisely the space of polynomials of separate degree at most n.
Its norm is the original product-measure norm. This proves J1 for every
coefficient vector, including all cross terms.

For clarity the cyclic source and its complete collision coefficients can
be obtained directly. For an ordered tuple
`boldrho=(rho_1,...,rho_k)`, put
\[
\kappa(\boldsymbol\rho)=\sum_i\rho_i,\quad
D(\boldsymbol\rho)=\sum_i d_{\rho_i},\quad
A(\boldsymbol\rho)=\prod_i a_{\rho_i}.
\]
Let K be the set of distinct attained kappa, and set
\[
e_\kappa=1+\max_{\kappa(\boldsymbol\rho)=\kappa}D(\boldsymbol\rho),
\quad \chi(S)=\prod_{\kappa\in K}(S-\kappa)^{e_\kappa},
\quad E=\mathbb C[S]/(\chi),\quad q=\deg\chi.
\]
The map
\[
\beta:E\longrightarrow A_h^{\otimes k},\qquad
[P(S)]\longmapsto[P(s_1+\cdots+s_k)]
\tag{C23}
\]
is well-defined and injective. In the primary factor for a tuple,
\(s_i=\rho_i+t_i\) and \(t_i^{d_{\rho_i}+1}=0\). The element
`t_1+...+t_k` has nilpotence order D+1: its D-th power is the nonzero
multiple \(\displaystyle\frac{D!}{\prod_i d_{\rho_i}!}\prod_i t_i^{d_{\rho_i}}\), and every
monomial of degree D+1 vanishes. For each center the largest such D
therefore imposes exactly the exponent e_kappa. Taking all tuple factors
shows that the kernel of the substitution from C[S] is exactly (chi).

Write `v_{kappa,j}=P^{(j)}(kappa)/j!`. In the tuple component of beta v,
the coefficient of `prod_i t_i^{j_i}`, with sum j_i=j, is
\[
\frac{j!}{\prod_i j_i!}v_{\kappa,j}.
\]
Its squared coefficient times its exact product metric weight is
\[
(j!)^2 |v_{\kappa,j}|^2 A(\boldsymbol\rho)
 \prod_i\binom{d_{\rho_i}}{j_i}.
\]
The sum over the j_i is the coefficient of x^j in
`prod_i(1+x)^{d_{rho_i}}=(1+x)^D`. Thus, with zero binomial
coefficients when j>D,
\[
S_{\kappa,j}=\sum_{\kappa(\boldsymbol\rho)=\kappa}
A(\boldsymbol\rho)\binom{D(\boldsymbol\rho)}j,
\quad
G_{k,1}(v)=\sum_{\kappa,j}(j!)^2S_{\kappa,j}|v_{\kappa,j}|^2.
\tag{C24}
\]
Each S_{kappa,j} is positive on the stated j range, since a tuple of
maximum D contributes positively. Every ordered tuple, including tuples
with unequal lengths at a common center, is included. With D_{h,eta}
in every factor, the product contributes eta^{2sum j_i}=eta^{2j}; hence
\[
G_{k,\eta}(v)=\sum_{\kappa,j}\eta^{2j}(j!)^2S_{\kappa,j}|v_{\kappa,j}|^2
\preceq G_{k,1}(v).
\tag{C25}
\]
For every full polynomial F with `J^{tensor k}F=beta v`, J1 and C24
give the exact J2 lower bound `||F||^2>=Lambda_{h,n}^{-k}G_{k,1}(v)`.

## 8. The section and the complete minimum

Set n_0=2d-1, and use the original coefficient frame on V_{n_0}.
Its source Gram H is positive definite: w_h is positive except at a
discrete set, so the squared norm of a nonzero polynomial is positive.
The remainder matrix J has rank d. Its kernel consists of `hQ` with
deg Q <= d-1, so it has dimension d. Define
\[
G_0=(JH^{-1}J^*)^{-1},\quad R_0=H^{-1}J^*G_0.
\]
Then `JR_0=I` and `R_0^*HR_0=G_0`. Choose W with d columns spanning
ker J and `W^*HW=I_d`. Direct multiplication gives
`R_0^*HW=G_0JW=0`.

Let `L_h=1+||T_1^{-1/2}G_0T_1^{-1/2}||` and
`tau_eta=L_h eta^{-2d_max}`. The exact jet weights imply
\[
\eta^{2d_{\max}}T_1\preceq T_\eta\preceq T_1,
\qquad \tau_\eta T_\eta\succeq L_hT_1\succ G_0.
\]
The positive square root in the original coefficient frame is consequently
well-defined. With `D=(tau_eta T_eta-G_0)^{1/2}`, put
\[
R_\eta=R_0+WD.
\]
The exact equalities are
\[
JR_\eta=I,\qquad R_\eta^*HR_\eta
=G_0+D^*D=\tau_\eta T_\eta.
\tag{C26}
\]
No square root has been transported through a nonunitary congruence.

Tensor C26 and compose with beta. After the original physical source
isometry A_h, the section `mathcal R=(A_h R_eta)^{tensor k} beta`
has value beta v and squared norm
\[
\mathcal R^*\mathcal R=\tau_\eta^kG_{k,\eta}.
\tag{C27}
\]
Let X_N be exactly the scalar-polynomial physical source from P(S),
deg P<=N, with S=s_1+...+s_k, and set Y=im mathcal R. Both sources
lie in the box of separate degree at most `n=max(N,n_0)`.
The section shows that their sum maps onto E. Its minimum exists and
is unique modulo zero-value directions by finite-dimensional orthogonal
projection. Its metric is positive definite. J2 applied before taking
this minimum gives its lower bound; C27 is an admitted vector for each
value and gives its upper bound. Thus
\[
\Lambda_{h,n}^{-k}G_{k,1}\preceq G_N^J
\preceq\tau_\eta^kG_{k,\eta}\preceq\tau_\eta^kG_{k,1}.
\tag{C28}
\]
For N>=q-1 the scalar source is onto E, with positive minimum metric
G_N; source inclusion then gives `G_N^J<=G_N`.

For the full box, let H_n be the one-factor polynomial Gram and J_n its
remainder matrix. Its covariance is `C_n=J_n H_n^{-1} J_n^*`, and its
minimum metric is `G_{h,n}=C_n^{-1}`. The box covariance is exactly
\[
(J_n^{\otimes k})(H_n^{-1})^{\otimes k}(J_n^*)^{\otimes k}
=C_n^{\otimes k}.
\]
Its value metric is therefore `G_{h,n}^{tensor k}`. Restriction to the
exact value beta v yields
\[
G_{k,n}^{\rm box}=\beta^*(G_{h,n}^{\otimes k})\beta\preceq G_N^J,
\tag{C29}
\]
because every joint candidate is a box candidate. This proves J4 with
the whole box kernel present. The same proof factor by factor gives the
heterogeneous constants `prod_i Lambda_{h_i,n_i}` and
`prod_i tau_{i,eta}`, with `n_i=max(N,2d_i-1)`.

## 9. The original cross Gram and its positive-range inverse

For N>=q-1 let B_X be the scalar coefficient map into the actual source,
`H_X=B_X^*B_X`, and let J_N be its map onto E. Its orthogonal projector
is `P_X=B_X H_X^{-1}B_X^*`. Put
\[
C_X=B_X^*\mathcal R,\quad
R_Z=(I-P_X)\mathcal R,\quad
H_Z=R_Z^*R_Z=\Gamma-C_X^*H_X^{-1}C_X,
\]
\[
F_Z=I-J_NH_X^{-1}C_X.
\tag{C30}
\]
The actual value map sends R_Z to beta F_Z. R_Z lies in the same
polynomial box, so J1 applied to R_Z v for every v gives
\[
F_Z^*G_{k,1}F_Z\preceq\Lambda_{h,n}^kH_Z.
\tag{C31}
\]
In particular `ker H_Z subset ker F_Z`, since G_{k,1} is positive.

The sum source is the orthogonal sum `X_N + im R_Z`. Take a unitary
spectral decomposition of H_Z. On each positive eigenvalue lambda its
source coordinate becomes orthonormal after multiplication by
lambda^{-1/2}; coordinates in ker H_Z represent the zero vector and
are killed by F_Z. Hence the covariance of this normal source is exactly
`F_Z H_Z^+ F_Z^*`. The scalar covariance is
`J_N H_X^{-1} J_N^*=G_N^{-1}`. Covariances of orthogonal source summands
add, which proves
\[
\Omega_N=F_ZH_Z^+F_Z^*,\qquad
G_N^J=(G_N^{-1}+\Omega_N)^{-1}.
\tag{C32}
\]
The inverse exists because the scalar covariance is positive definite.
Factoring it out gives
\[
\frac{\det G_N}{\det G_N^J}
=\det(I+G_N^{1/2}\Omega_NG_N^{1/2}),
\tag{C33}
\]
which proves J7–J8 on the original coefficient space.

The section is injective by its right-inverse property. Therefore
\[
\dim\ker R_Z=\dim(Y\cap X_N),\quad
\operatorname{rank}H_Z=q-\dim(Y\cap X_N).
\]
If a vector belongs to the intersection, its polynomial is both
P(s_1+...+s_k) and of separate degree at most n_0. Equality of physical
vectors implies equality of these polynomials, because the product density
is positive almost everywhere and a polynomial vanishing there is zero.
If deg P=M, its highest pure s_1 monomial has nonzero coefficient and
degree M, so M<=n_0. Consequently
\[
\dim(Y\cap X_N)\le\min(N,n_0)+1\le2d,
\qquad \operatorname{rank}H_Z\ge q-2d.
\tag{C34}
\]
This is J9. It makes no claim that the value correction Omega_N has the
same rank as H_Z.

## 10. Fixed restrictions, complete quotients, and the four cutoffs

Assume `2q>=n_0` and use the single constant
`Lambda=Lambda_{h,2q}` throughout `q-1<=N<=2q`. Every relevant source
lies in that same box. With `G_ref=G_{k,1}`, C28 gives
\[
\alpha G_{\rm ref}\preceq G_N^J\preceq bG_{\rm ref},
\quad \alpha=\Lambda^{-k},\quad b=\tau_\eta^k,
\quad \log(b/\alpha)=W_k=k\log(\tau_\eta\Lambda).
\tag{C35}
\]
For any fixed injective inclusion I, congruence gives the same bounds on
`I^*G_N^J I`. For any fixed onto quotient L onto its actual image,
minimizing the scalar quadratic inequality over the exact affine fibre
`Lv=w` gives the same bounds on its quotient metric. That minimum is
\[
Q_N=(L(G_N^J)^{-1}L^*)^{-1},
\]
as follows by the minimizing vector
`v=(G_N^J)^{-1}L^*Q_N w`, whose difference from any other lift is
orthogonal to ker L. Repeated fixed inclusions and quotients preserve
these same constants, proving the assertion for every fixed subquotient.

Because Y is fixed and X_N increases, G_N^J decreases with N. Restriction
and affine minimization preserve this order. If the resulting rank is
r_X and `f(N)=log det G_{X,N}^J`, positive congruence and eigenvalue
comparison imply
\[
f(N_1)\ge f(N_2)\quad(N_1\le N_2),\qquad
\sup_Nf(N)-\inf_Nf(N)\le r_XW_k.
\]
Pair the actual four signs as
\[
\mathcal Rf=[f(q-1)-f(2q-1)]+[f(q)-f(2q)].
\]
Both differences lie between zero and r_X W_k. This proves J11 exactly:
\[
0\le\mathcal R\log\det G_{X,N}^J\le2r_XW_k.
\tag{C36}
\]
Rank one includes the restriction to a specified nonzero class, with its
original vector fixed across all cutoffs.

The complete finite tolerance expression is
\[
W_k=k\log L_h+k\log\Lambda+2kd_{\max}\log(1/\eta).
\tag{C37}
\]
For the general choice `eta=min(1,t_*/(D+1))`, where D is the largest
total tuple degree and `D<=k d_max`,
\[
\log(1/\eta)=\log^+((D+1)/t_*)
 \le\log(D+1)+\log^+(1/t_*).
\]
C19 and C22 therefore give the precise J10 order
\[
W_k=O_h\bigl(k\log^2(q+2)+k\log(k+2)
 +k\log^+(1/t_*)\bigr).
\tag{C38}
\]
For a common-multiplicity quartet with
`e=1+k(m_0-1)` and `eta=delta/e` when m_0>1, one instead reads
`log(1/eta)=log e+log(1/delta)=O_h(log(k+2))` directly. For simple
roots d_max=0, so C37 is independent of eta and gives
`W_k=O_h(k log^2(q+2))`; on the simple quartet `q=(k+1)^2`.

For every fixed one-factor root set with z=|Z|, there is also the explicit
polynomial growth bound
\[
q\le(kd_{\max}+1)\binom{k+z-1}{z-1}.
\tag{C39}
\]
Indeed an unordered root-count vector is a z-tuple of nonnegative integers
summing to k, so there are exactly the displayed binomial number of such
vectors. Every ordered tuple has one such vector and therefore one of at
most that many centers. Each center has e_kappa<=k d_max+1. Summing these
inequalities proves C39, including all possible collisions. This is the
polynomial growth assertion needed in J10. On the stated quartet the exact
formula q=(1+k(m_0-1))(k+1)^2 follows because the independent real and
imaginary sign counts each run from 0 through k and every pair of counts
is attainable; all tuples have the same D=k(m_0-1).

If a family of intermediate sources contains Y and stays inside the same
box, C35 and its fixed restrictions and quotients still hold. Nesting is
needed for the first inequality in C36. In the absence of nesting each
of the two paired differences lies in `[-r_XW_k,r_XW_k]`, yielding the
valid conclusion `|R f|<=2r_X W_k`. Common enclosing constants alone
cannot fix the sign: in rank one, choosing both early metric values at
alpha and both late values at b gives `R f=-2log(b/alpha)`. This shows
exactly why the claimed intermediate-source extension needs its stated
scope repair. The original joint source satisfies the nesting requirement.

## 11. Reading and use record

The mathematical input actually read for this derivation was:

- `COMPLETE_PROOFS(2).md`, complete Sections 1–2,
  equations P1–P11 and J1–J11. The initial tool output also exposed later
  sections; no independent verification of those later sections is asserted.
- `.../family_cost_intake_20260920/extracted/ES_RH_Family_Integration_20260920_C/proofs/01_METRIC_RETURN.md`,
  complete file read; only Section 1.1's explicit common-multiplicity
  tolerance choice was used here. Its separate imported spectral theorem
  was not used in the present proof.
- The same package's `proofs/02_JOINT_SOURCE.md`, bounded search excerpts
  around the cross-Gram and physical-source discussion. The cross-Gram
  identities in this file were independently proved in C30–C33; no claim
  of complete reading of that package is made.
- NIST DLMF, version 1.2.8, release 2026-09-15: exact formulas
  [5.7.6](https://dlmf.nist.gov/5.7.E6),
  [18.23.7](https://dlmf.nist.gov/18.23.E7),
  [18.19.8–9](https://dlmf.nist.gov/18.19.E8), and
  [25.2.10–11](https://dlmf.nist.gov/25.2.E10).
  These formulas were read in the rendered primary source and fetched
  from its original `.tex` endpoints. They supply only the classical
  identities identified in C1–C3, C6, and C8; all quantitative constants
  and all finite tensor and minimum arguments are derived above.
  The six unchanged TeX responses are retained in `coercivity_sources/`
  under their DLMF equation IDs, including `18.19.E9a.tex` for the norm.

No paper absent from this list, no original arXiv source, and no entire
literature corpus is represented as having been read. No PDF was used.
No remote publication or graphical rendering was performed in this
independent derivation subtask.
