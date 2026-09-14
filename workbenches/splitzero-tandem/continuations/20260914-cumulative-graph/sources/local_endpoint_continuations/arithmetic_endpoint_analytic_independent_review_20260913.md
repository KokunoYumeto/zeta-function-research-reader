# Independent analytic review of the arithmetic endpoint bounds

Date: 2026-09-13. Reviewer lane: analytic propagation, the actual convolution
density, and the two monic norm endpoints. No numerical checker, Lean process,
compiler, source mutation, or publication operation was run in this review.

## 1. Sources, scope, and finding

I read the complete `NOTE.tex` and `RESEARCH_NOTE.md` in
`sources/web_arithmetic_endpoint_delivery/Tau_Arithmetic_Endpoint_Bounds` and
the complete pinned `endpoint_criterion_pr23_c720f405_20260913.md`. Their
SHA-256 values, respectively, are:

- `f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8`;
- `8fa97624a55c2f1baad54e465e4637c584329f24f6c198bb5d168a443811a280`;
- `61dd03044ad56b2baf3671fa217497b0f4749c1259f841cdc8491846abbd2e46`.

The written analytic argument in source equations (14)--(37) is valid. In
particular, it proves the claimed bound with the **literal constant in (36)**
for every pair of integers $n\ge k\ge3$. The exponent 42, the removable
centres of $g/h$, the compact mass raised to $k-3$, the source coordinate
$S=k/2+iu$, and the factor two from the two Laplace moments all survive the
calculation below. No change to the measure is required.

One local type restriction should be inserted in the integrated treatment of
the paragraph after (13): the graded isomorphism induced by multiplication by
the degree-$q$ polynomial $\chi$ has domain $n\ge q$. The displayed exact
sequence (13) itself remains valid at $n=q-1$. Section 9 below proves the
precise maps, including that edge case. This correction has no effect on the
analytic bound or on its window, where $n\ge q$.

The finite boundary and confluent-jet claims in source Sections 8--9 were read
for context; their independent matrix audit belongs to the parent integration
lane. I do not represent this report as a replay of upstream theta, cyclic,
exterior, Deligne-transcription, or Lean proofs. Section 10 below checks the
elementary endpoint composition using the stated original local control law.

## 2. Exact ellipse, holomorphy, and strip growth

Put $J(w)=(w+w^{-1})/2$. For $w=8e^{i\phi}$,

\[
J(w)=\frac{65}{16}\cos\phi+i\frac{63}{16}\sin\phi.
\]

Thus the closed ellipse has semiaxes $a=65/16$, $b_E=63/16$.
For $z=x+iy$ in that ellipse and

\[
s=\frac12+iT+iz=\frac12-y+i(T+x),
\]

we have the literal bounds

\[
-\frac{55}{16}\le\Re s\le\frac{71}{16},\qquad
|\Im s-T|\le\frac{65}{16}.
\]

When $|T|\ge10$, $|\Im s|\ge95/16$. In particular $s=1$ is absent
from the entire image, and $f_T(z)=\zeta(1/2+iT+iz)$ is holomorphic on a
neighbourhood of the closed ellipse.

For $\sigma=\Re s>1$, absolute convergence permits

\[
\zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx
=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\]

The last integral is absolutely convergent and holomorphic for $\sigma>0$:
on every compact subset of that half-plane its derivatives are dominated by
$x^{-1-\sigma_0}(\log x)^j$, with $\sigma_0>0$. Analytic continuation
therefore proves the same identity for $\sigma>0,s\ne1$. Its modulus is
bounded by

\[
1+\frac1{|s-1|}+\frac{|s|}{\sigma}.
\]

On the portion of the displayed strip with $\sigma\ge1/4$,
$|s-1|\ge95/16$, $|s|\le |T|+17/2$, and this gives a uniform bound
$C(1+|T|)$.

For $-55/16\le\sigma\le1/4$, the functional equation is

\[
\zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s).
\]

This is the formula in [DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2). The
vertical gamma estimate, uniform when its real argument remains in a bounded
interval, is [DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9):

\[
|\Gamma(a+iy)|\sim\sqrt{2\pi}|y|^{a-1/2}e^{-\pi|y|/2}.
\]

Here $a=1-\sigma\in[3/4,71/16]$, and
$|\sin(\pi s/2)|\le e^{\pi|\Im s|/2}$. The exponential factors cancel
in this upper bound, while the integral formula already proved gives
$|\zeta(1-s)|\le C(1+|T|)$. The remaining gamma power is
$(1+|T|)^{1/2-\sigma}$, up to a fixed constant. Hence

\[
|\zeta(s)|\le C'(1+|T|)^{3/2-\sigma},\qquad
\frac32-\sigma\le\frac{79}{16}<5.
\]

Uniformity of the gamma asymptotic and compactness of the remaining bounded
part of this strip justify one common constant. It follows that some fixed
$C_0\ge1$ gives $M_T=C_0(1+|T|)^6$ on the closed ellipse, as asserted.

For completeness the radius-one discs used in the derivative step really are
contained in the ellipse. Every such disc about a point of $[-1,1]$ lies in
$\{|x|\le2,|y|\le1\}$. For this rectangle,

\[
\frac{x^2}{a^2}+\frac{y^2}{b_E^2}
\le\frac{1024}{4225}+\frac{256}{3969}<1.
\]

The maximum principle bounds $f_T$ by $M_T$ throughout the ellipse.
Cauchy's formula on the radius-one circle around each real $x\in[-1,1]$
then gives $|f_T'(x)|\le M_T$, with the same constant and no radius loss.

## 3. Nonzero off-line value to exact local critical-line mass

Set $r_*=(3+\sqrt{13})/2$. Its defining equation is
$r_*^2-3r_*-1=0$, so $r_*-r_*^{-1}=3$, and therefore

\[
J(-ir_*)=-\frac{i}{2}(r_*-r_*^{-1})=-\frac{3i}{2}.
\]

The original affine map takes this point to $2+iT$. The absolutely
convergent Euler product, or its Möbius Dirichlet inverse obtained by
absolutely convergent multiplication, gives

\[
\frac1{\zeta(2+iT)}=\sum_{m\ge1}\frac{\mu(m)}{m^{2+iT}},\qquad
\left|\frac1{\zeta(2+iT)}\right|\le\sum_{m\ge1}m^{-2}=\zeta(2).
\]

Here the elementary coefficient identity is
$\sum_{d\mid m}\mu(d)=1$ at $m=1$, and zero for $m>1$; it follows by
expanding $(1-1)^r$ over the distinct prime divisors. Thus the product of
the two absolutely convergent series is exactly one, which also proves the
required nonvanishing at $2+iT$. Put $c_*=\zeta(2)^{-1}\in(0,1)$.

The function $F_T(w)=f_T(J(w))$ is holomorphic on a neighbourhood of
$1\le|w|\le8$. Its inner boundary is mapped onto $[-1,1]$; its outer
boundary is mapped onto the ellipse. Write
$m_T=\max_{[-1,1]}|f_T|$. This number is positive, because identically
zero on that interval would force $f_T$ to vanish identically and would
contradict its value at $-3i/2$.

Subtract from the subharmonic function $\log|F_T|$ the harmonic function

\[
H(w)=\left(1-\frac{\log|w|}{\log8}\right)\log m_T
      +\frac{\log|w|}{\log8}\log M_T.
\]

The difference is at most zero on both boundary circles. Its value at zeros
is minus infinity, so the subharmonic maximum principle applies without
dividing by $F_T$. Evaluating at $-ir_*$ proves

\[
c_*\le m_T^\vartheta M_T^{1-\vartheta},\qquad
\vartheta=1-\frac{\log r_*}{\log8}.
\]

Since $r_*<4$, $\vartheta>1/3$. Consequently

\[
m_T\ge c_*^{1/\vartheta}M_T^{-(1-\vartheta)/\vartheta}
\ge c_*^3M_T^{-2}.
\]

The second inequality uses both $0<c_*<1$ and $M_T\ge1$, with the
directions shown explicitly: $1/\vartheta<3$ and
$(1-\vartheta)/\vartheta<2$.

Let $x_0\in[-1,1]$ attain $m_T$. At least one of the two directions from
$x_0$ stays in the interval for length at least one. Choose that direction
and retain the segment of length $\ell=m_T/(2M_T)\le1/2$. Along it,

\[
|f_T(x)-f_T(x_0)|\le M_T|x-x_0|\le m_T/2,
\qquad |f_T(x)|\ge m_T/2.
\]

The change of variable $t=T+x$ has Jacobian one. It yields

\[
\begin{aligned}
\int_{T-1}^{T+1}|\zeta(1/2+it)|^2\,dt
&\ge\ell(m_T/2)^2=\frac{m_T^3}{8M_T}\\
&\ge\frac{c_*^9}{8M_T^7}
=\frac{c_*^9}{8C_0^7}(1+|T|)^{-42}.
\end{aligned}
\]

This checks the seventh power of $M_T$, and hence the literal exponent 42.

Define $I(T)=\int_{-1}^1|\zeta(1/2+i(T+x))|^2\,dx$. On
$[-10,10]\times[-1,1]$ the integrand is continuous and bounded, so $I$
is continuous. If $I(T)=0$, continuity and nonnegativity force its
integrand to vanish on the whole interval. The identity theorem would then
make $\zeta$ identically zero on its connected holomorphic domain away
from its pole, contradicting $\zeta(2)>0$. Thus
$m_{\mathrm{comp}}=\min_{|T|\le10}I(T)>0$. One permitted explicit
definition of the constant in (23) is

\[
c_\zeta=\min\left\{m_{\mathrm{comp}},\frac{c_*^9}{8C_0^7}\right\}>0.
\]

Since $(1+|T|)^{-42}\le1$, it works on the compact interval as well as
outside it. This is a definition of a positive mathematical constant; no
numerical interval enclosure is claimed.

## 4. The original entire quotient, its tails, and all selected centres

Let the monic packet polynomial be

\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\quad d=\sum_\rho m_\rho,
\qquad g(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Each selected multiplicity is its actual full multiplicity in $g$. Near a
selected centre $\rho$, write
$g(s)=(s-\rho)^{m_\rho}a_\rho(s)$ and
$h(s)=(s-\rho)^{m_\rho}h_\rho(s)$, where both residual factors are
holomorphic and nonzero at $\rho$. Therefore
$v_h=a_\rho/h_\rho$ there. It is holomorphic with the definite nonzero
value $a_\rho(\rho)/h_\rho(\rho)$. These local expressions glue with
$g/h$ away from the centres, proving the entire identity $g=hv_h$.

Put $\alpha_0=\pi/2$. The vertical gamma formula gives

\[
|\Gamma(1/4+it/2)|^2\sim2\pi\sqrt2\,|t|^{-1/2}e^{-\alpha_0|t|}.
\]

Gamma is holomorphic on the half-plane of positive real part. At
$z=1/4+it/2$, the two factors in the reflection formula are finite and

\[
\Gamma(z)\Gamma(1-z)=\frac{\pi}{\sin(\pi z)}\ne0.
\]

Indeed the real part of $z$ is $1/4$, so $z$ is not an integer and the sine
denominator is nonzero. The reflection identity is
[DLMF 5.5.3](https://dlmf.nist.gov/5.5.E3). Thus gamma has no zero and no
pole along the line used here. The continuous positive function

\[
R_\Gamma(t)=|\Gamma(1/4+it/2)|^2(1+|t|)^{1/2}e^{\alpha_0|t|}
\]

tends to $2\pi\sqrt2>0$ at both ends of the real line. Its infimum
$c_\Gamma>0$ therefore gives the all-real lower estimate (24). The same
argument gives a finite upper constant for the identical weight. No zero
of zeta enters this gamma assertion.

For $s=1/2+it$, every packet factor obeys

\[
|s-\rho|\le |t|+|\rho-1/2|
\le(1+|t|)(1+|\rho-1/2|).
\]

Thus $H_h=\prod_\rho(1+|\rho-1/2|)^{m_\rho}$ gives
$|h(s)|\le H_h(1+|t|)^d$. The entire identity, without division by a
possibly zero $h(s)$, proves

\[
|v_h(s)|^2\ge\frac{|g(s)|^2}{H_h^2(1+|t|)^{2d}}.
\]

This remains true at every selected critical-line centre. At such a point
the right-hand side vanishes and the already defined left-hand side remains
the entire quotient value.

All constants in $g$ give exactly

\[
\frac{|g(1/2+it)|^2}{2\pi}
=\frac{(t^2+1/4)^2}{2\pi^{3/2}}
 |\Gamma(1/4+it/2)|^2|\zeta(1/2+it)|^2.
\]

For $x=|t|\ge0$,
$(1+x)^2\le2(1+x^2)\le8(x^2+1/4)$, and hence

\[
(t^2+1/4)^2(1+|t|)^{-1/2}
\ge\frac1{64}(1+|t|)^{7/2}\ge\frac1{64}.
\]

In particular the following literal choice is valid in (25):

\[
c_h^{(0)}=\frac{c_\Gamma}{128\pi^{3/2}H_h^2}>0.
\]

It proves

\[
w_h(t)\ge c_h^{(0)}e^{-\alpha_0|t|}(1+|t|)^{-2d}
                |\zeta(1/2+it)|^2.
\]

The stronger factor $(1+|t|)^{7/2-2d}$ is present in the preceding
calculation; taking its displayed lower bound changes only the inequality.

The integrability claims also follow with the actual $h$ retained. Define
$R_h=\max(\{1\}\cup\{2|\rho-1/2|+1:\rho\in Z\})$, which also specifies
the threshold for the empty packet. If $|t|\ge R_h$, then
$|1/2+it-\rho|\ge|t|/2$. Consequently
$|h(1/2+it)|\ge(|t|/2)^d$. The integral formula of Section 2 gives
$|\zeta(1/2+it)|\le C(1+|t|)$, and the upper gamma bound gives a constant
$C_h^{\mathrm{tail}}$ such that, outside that compact interval,

\[
w_h(t)\le C_h^{\mathrm{tail}}
e^{-\alpha_0|t|}(1+|t|)^{11/2-2d}.
\]

Inside it the entire quotient is continuous, including the removable
centres. Thus $w_h\in C(\mathbb R)\cap L^1(\mathbb R)\cap
L^\infty(\mathbb R)$, every polynomial moment is finite, and for each
$0<b<\alpha_0$ both $M_h(b)$ and $M_h(-b)$ are finite. The empty
product $h=1$ satisfies the same reasoning with $d=0,H_h=1$.

Finally $v_h$ is a nonzero entire function. Its zeros on the line are
discrete: any finite accumulation point would contradict the identity
theorem. Therefore $w_h$ is positive outside a discrete set and
$\mu_h=\int w_h>0$.

For $|t-T|\le1$,

\[
e^{-\alpha_0|t|}\ge e^{-\alpha_0}e^{-\alpha_0|T|},\qquad
(1+|t|)^{-2d}\ge2^{-2d}(1+|T|)^{-2d}.
\]

Combining these inequalities with Section 3 proves (26) with the choices

\[
B_h=42+2d,\qquad
c_h^{(1)}=c_h^{(0)}e^{-\alpha_0}2^{-2d}c_\zeta>0.
\]

## 5. Three convolution factors and the complete tensor mass

For each real $u$,

\[
m_{h,2}(u)=\int_\mathbb R w_h(t)w_h(u-t)\,dt
\]

is finite, since it is at most $\|w_h\|_\infty\|w_h\|_1$. Its integrand
is positive except on the union of two discrete sets. Therefore the integral
is strictly positive. Also

\[
|m_{h,2}(u+a)-m_{h,2}(u)|
\le\|w_h\|_\infty\|w_h(\cdot+a)-w_h\|_1\longrightarrow0.
\]

Translation continuity in $L^1$ proves continuity, uniformly in $u$.
Thus the source constants

\[
b_h=\min_{|v|\le1}m_{h,2}(v)>0,\qquad
\vartheta_h=\int_{-1}^1w_h(v)\,dv>0
\]

exist with their actual mass. Nonnegative Fubini proves convolution
associativity and $\int m_{h,k}=\mu_h^k$, without any probability
normalization.

At three factors, retaining the part with $v\in[-1,1]$ gives

\[
\begin{aligned}
m_{h,3}(u)
&=\int_\mathbb R m_{h,2}(v)w_h(u-v)\,dv\\
&\ge b_h\int_{-1}^1w_h(u-v)\,dv\\
&=b_h\int_{u-1}^{u+1}w_h(t)\,dt\\
&\ge c_h e^{-\alpha_0|u|}(1+|u|)^{-B_h},\qquad
c_h=b_hc_h^{(1)}.
\end{aligned}
\]

For $k\ge4$, the full convolution expression is

\[
m_{h,k}(u)=\int_{\mathbb R^{k-3}}
m_{h,3}(u-v_1-\cdots-v_{k-3})\prod_{a=1}^{k-3}w_h(v_a)\,dv_a.
\]

Restrict to the cube $[-1,1]^{k-3}$. There
$|u-\sum v_a|\le|u|+k-3$; since the exponential and negative polynomial
power in the lower envelope decrease with their nonnegative argument,

\[
m_{h,k}(u)\ge
c_h e^{-\alpha_0(|u|+k-3)}(1+|u|+k-3)^{-B_h}
\prod_{a=1}^{k-3}\int_{-1}^1w_h(v_a)\,dv_a.
\]

This is exactly (29), with $\vartheta_h^{k-3}$. For $k=3$ the
calculation just made is used directly and the product over zero variables is
one. No negative tensor power or missing compact mass has been used.

## 6. Typed monic minimization and the exact Legendre constant

Use the original source form

\[
\|P\|_{h,k}^2=\int_\mathbb R|P(k/2+iu)|^2m_{h,k}(u)\,du
\]

on $\mathbb C[S]_{\le j}$. The substitution map and its inverse are

\[
\Psi_k:\mathbb C[S]_{\le j}\longrightarrow\mathbb C[u]_{\le j},
\quad\Psi_kP(u)=P(k/2+iu),\qquad
\Psi_k^{-1}Q(S)=Q((S-k/2)/i).
\]

They are mutually inverse linear isomorphisms. On leading coefficients
$\operatorname{lc}_u(\Psi_kP)=i^j\operatorname{lc}_S(P)$.
In particular a monic original polynomial has leading coefficient $i^j$
after evaluation; its modulus is one and its phase is explicit.

Let

\[
P_j(x)=\frac1{2^jj!}\frac{d^j}{dx^j}(x^2-1)^j,
\qquad a_j=\frac{(2j)!}{2^j(j!)^2}.
\]

This agrees with the Rodrigues formula in
[DLMF Table 18.5.1](https://dlmf.nist.gov/18.5.T1). Differentiating the
leading term $x^{2j}$ proves that $a_j$ is its leading coefficient.
Integrating by parts $j$ times proves orthogonality to every polynomial of
degree less than $j$; all endpoint terms vanish since $(x^2-1)^j$
has order $j$ at both endpoints. The same operation on $P_j$ itself
gives

\[
\int_{-1}^1P_j(x)^2\,dx
=\frac{a_j}{2^j}\int_{-1}^1(1-x^2)^j\,dx.
\]

The substitution $x=2y-1$, followed by integration by parts for the beta
integral, yields

\[
\int_{-1}^1(1-x^2)^j\,dx
=2^{2j+1}\int_0^1y^j(1-y)^j\,dy
=\frac{2^{2j+1}(j!)^2}{(2j+1)!}.
\]

Thus $\int_{-1}^1P_j^2=2/(2j+1)$, with every factorial retained.

The monic polynomial in $u$ is
$R_{j,L}(u)=L^jP_j(u/L)/a_j$. The required original polynomial is

\[
Q_{j,L}(S)=i^jR_{j,L}((S-k/2)/i).
\]

It has leading coefficient one in $S$, and
$Q_{j,L}(k/2+iu)=i^jR_{j,L}(u)$. Every competing monic original polynomial
differs after evaluation by a complex polynomial of degree below $j$.
The real orthogonality just proved extends to all complex coefficients, so
Pythagoras gives the exact minimum

\[
\inf_{\operatorname{lc}_S Q=1}\int_{-L}^L|Q(k/2+iu)|^2\,du
=\frac{L^{2j+1}}{a_j^2}\frac2{2j+1}
=\frac{2L^{2j+1}}{2j+1}
 \left(\frac{2^j(j!)^2}{(2j)!}\right)^2=\mathfrak l_j(L).
\]

The formula also holds at $j=0$, where both sides are $2L$.

For the restriction step the isometric map is

\[
L^2(m_{h,k}(u)du)\longrightarrow
L^2(m_{h,k}(u)du|_{[-L,L]})\oplus
L^2(m_{h,k}(u)du|_{\mathbb R\setminus[-L,L]}),
\quad f\longmapsto(f|_{[-L,L]},f|_{\mathbb R\setminus[-L,L]}).
\]

Its inverse extends both components by zero and adds them. Norms add in
squares. On the first component (29) gives a contraction to the same function
in $L^2(\rho_{h,k,L}\,du)$, where

\[
\rho_{h,k,L}=c_h\vartheta_h^{k-3}
e^{-\alpha_0(L+k-3)}(1+L+k-3)^{-B_h}.
\]

This follows from $m_{h,k}(u)\ge\rho_{h,k,L}$ there. Taking infima over
the original monic affine space, and using the exact Legendre minimum,
proves (34) with this literal coefficient.

## 7. Upper endpoint and verification of the constant 64

For every $0<b<\alpha_0$, nonnegative Fubini gives the exact identities

\[
\int e^{bu}m_{h,k}(u)\,du=M_h(b)^k,\qquad
\int e^{-bu}m_{h,k}(u)\,du=M_h(-b)^k.
\]

Using $e^{b|u|}\le e^{bu}+e^{-bu}$ proves (31). The term of degree $2j$
in the exponential series gives
$|u|^{2j}\le(2j)!b^{-2j}e^{b|u|}$. The original monic trial polynomial
$(S-k/2)^j$ evaluates to $i^ju^j$, which yields

\[
\omega_{h,k,j}\le(2j)!b^{-2j}\bigl(M_h(b)^k+M_h(-b)^k\bigr).
\]

Combining this at $j=2n$ with the exact lower bound at $j=n,L=n$
proves (35). Both lower norm and the upper moments are finite and strictly
positive, so the division and positive $2n$-th root are permitted.

To check (36) without suppressing any prefactor, put

\[
M_* =\max\{1,M_h(b),M_h(-b)\},\quad
C_* =\max\{1,c_h^{-1}\},\quad
\Theta_* =\max\{1,\vartheta_h^{-1}\}.
\]

The binomial identity in the exact lower norm gives

\[
\mathfrak l_n(n)=\frac{2n^{2n+1}}{2n+1}
\left(\frac{2^n}{\binom{2n}{n}}\right)^2
\ge\frac{2n^{2n+1}}{(2n+1)4^n}.
\]

Use $(4n)!\le(4n)^{4n}$ and the literal two-moment estimate
$M_h(b)^k+M_h(-b)^k\le2M_*^k$. The factorial, Legendre, and this factor
two together have $2n$-th root at most

\[
\begin{aligned}
\left[\frac{(4n)^{4n}\,2(2n+1)4^n}{2n^{2n+1}}\right]^{1/(2n)}
&=32n\left(2+\frac1n\right)^{1/(2n)}\\
&\le64n.
\end{aligned}
\]

The last inequality holds already for $n\ge1$, since
$2+1/n\le3\le4^n$. Thus the leading constant 64 in the source safely
includes the factor two from the Laplace sum. This allocation makes explicit
the harmless suppressed intermediate factor in the source paragraph.

For $n\ge k\ge3$, the remaining mass factors obey

\[
M_*^{k/(2n)}\le\sqrt{M_*},\qquad
c_h^{-1/(2n)}\le\sqrt{C_*},\qquad
\vartheta_h^{-(k-3)/(2n)}\le\sqrt{\Theta_*}.
\]

These cover both possibilities that a retained mass is below or above one;
no mass is assigned a different value. The exponential part is bounded by

\[
e^{\alpha_0(n+k-3)/(2n)}\le e^{\alpha_0},
\]

and, since $1+n+k-3=n+k-2\le2n$, the polynomial part is bounded by

\[
(1+n+k-3)^{B_h/(2n)}
\le(2n)^{B_h/(2n)}
=2^{B_h/(2n)}\exp\left(\frac{B_h\log n}{2n}\right)
\le2^{B_h/2}\exp\left(\frac{B_h}{2e}\right).
\]

The final step follows from the maximum of $\log x/x$ on $x>0$, whose
derivative is $(1-\log x)/x^2$ and whose maximum is $1/e$ at $x=e$.
Finally $b^{-4n}$ contributes exactly $b^{-2}$. Multiplication proves

\[
\left(\frac{\omega_{h,k,2n}}{\omega_{h,k,n}}\right)^{1/(2n)}
\le64b^{-2}e^{\alpha_0}2^{B_h/2}e^{B_h/(2e)}
\sqrt{M_*C_*\Theta_*}\,n.
\]

This is precisely the source constant (36). Fixing $b$, for example
$b=\pi/4$, makes every quantity on its right depend only on the fixed
packet $h$ and on universal constants. The proof does not enclose that
constant numerically.

## 8. General source window with all parameters retained

For integers $k\ge3,n\ge0,r\ge1$ and any real $L>0$, use the
upper estimate at degree $n+r$ and the lower estimate at degree $n$.
The exact result is

\[
\left(\frac{\omega_{h,k,n+r}}{\omega_{h,k,n}}\right)^{1/(2r)}
\le
\left[
\frac{(2(n+r))!b^{-2(n+r)}(M_h(b)^k+M_h(-b)^k)
 e^{\alpha_0(L+k-3)}(1+L+k-3)^{B_h}}
 {c_h\vartheta_h^{k-3}\mathfrak l_n(L)}
\right]^{1/(2r)}.
\]

These explicit parameter conditions should accompany (37) in an integrated
standalone presentation. The uniform $C_hn$ estimate then specializes to
$r=n,L=n,n\ge k\ge3$, so there is no use of $L=0$ or $r=0$.

## 9. The exact graded edge correction

Set $\mathcal P_a=\mathbb C[S]_{\le a}$ for $a\ge0$, and
$\mathcal P_a=0$ for $a<0$. For a monic $\chi$ of degree $q\ge1$,
polynomial division proves, for every $n\ge q-1$,

\[
0\longrightarrow\mathcal P_{n-q}\xrightarrow{\times\chi}
\mathcal P_n\xrightarrow{\pi_\chi}\mathbb C[S]/(\chi)
\longrightarrow0.
\]

Indeed multiplication by a nonzero polynomial is injective; its image is
exactly the polynomials in $\mathcal P_n$ divisible by $\chi$; every
residue has its unique representative of degree below $q$, which belongs
to $\mathcal P_n$. At $n=q-1$ the relation space is zero and this last
map is an isomorphism from $\mathcal P_{q-1}$ to the residue space.

For $n\ge q$, multiplication also descends to

\[
\overline m_\chi:
\mathcal P_{n-q}/\mathcal P_{n-q-1}
\longrightarrow\mathcal P_n/\mathcal P_{n-1},\qquad
[A]\longmapsto[\chi A].
\]

It is well-defined by degree, and
$\operatorname{lc}_n(\chi A)=\operatorname{lc}_{n-q}(A)$ because
$\chi$ is monic. The two leading-coefficient isomorphisms to
$\mathbb C$ therefore identify this map with the identity; it is an
isomorphism preserving the original leading coefficient exactly. At
$n=q-1$ its prospective domain is $0/0=0$, whereas its prospective
target is one-dimensional. Thus that edge is excluded specifically from
the graded-isomorphism sentence, while retained in the exact sequence.

Under $\pi_\chi$, every actual $\chi A$ maps to the zero residue.
This identifies the exact correspondence between the leading-coefficient
line of a relation and its vanishing arithmetic residue. Their original
source norm remains the norm of the same polynomial under $\mathcal V$.

## 10. Endpoint composition and the forced four-volume threshold

The pinned endpoint source uses the existing local control law

\[
0\le\epsilon_N\le
\sqrt{\omega_{N+1}/\omega_N}\,
\sinh\left(\frac12\log(V_{N-1}/V_{N+1})\right),\qquad N\ge q,
\]

with $V_N>0$ nonincreasing. Retain $n\ge q,r\ge1$ and set

\[
x_j=\frac12\log\frac{V_{n+j-1}}{V_{n+j+1}}\ge0,
\quad a_j=\sqrt{\frac{\omega_{n+j+1}}{\omega_{n+j}}}>0,
\quad E=\min_{0\le j<r}\epsilon_{n+j}.
\]

If any $x_j=0$, that local allowance is zero and the required upper bound
holds. Otherwise $(\log\sinh x)''=-1/\sinh^2x<0$ on $(0,\infty)$.
Finite Jensen and multiplication give

\[
E^r\le\prod_j\epsilon_{n+j}
\le\prod_ja_j\prod_j\sinh x_j
\le\left(\frac{\omega_{n+r}}{\omega_n}\right)^{1/2}
\sinh\left(\frac1r\sum_jx_j\right)^r.
\]

The norm product telescopes in the displayed expression. The volume product
is exactly

\[
2\sum_jx_j=
\log\frac{V_{n-1}V_n}{V_{n+r-1}V_{n+r}},
\]

including $r=1$, where the common $V_n$ occurs on both sides of the
ratio. Taking the nonnegative $r$-th root reproduces source (38).
For $n\ge\max(q,k),k\ge3,r=n$, Section 7 bounds its norm factor by
$C_hn$. This proves (39) on the original admissible degree window.

For the fixed nonreal off-line quartet of the upstream exterior result,
$m\ge1,\delta>0$, and

\[
q_k=[1+k(m-1)](k+1)^2,\qquad
L_{h,k}=2\delta[1+k(m-1)](k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
\]

The original finite exterior lower bound applies to every degree selected
in the window. The elementary constants obey $q_k\ge(k+1)^2\ge k$, and

\[
\frac{L_{h,k}}{q_k}
=\frac{2\delta}{k+1}\left\lfloor\frac{(k+1)^2}{4}\right\rfloor
\ge\frac{\delta k}{2}.
\]

For odd $k$, four times the floor is $(k+1)^2\ge k(k+1)$; for even
$k$, it is $k(k+2)\ge k(k+1)$. This proves the displayed inequality
for both parities. Hence on $n=r=q_k$,

\[
\frac{\delta k}{2C_h}\le
\sinh\left(\frac{\mathcal B_{h,k}}{2q_k}\right),\qquad
\mathcal B_{h,k}=\log\frac{V_{q_k-1}V_{q_k}}{V_{2q_k-1}V_{2q_k}}\ge0.
\]

Since $\sinh$ is increasing, this implies the exact lower bound

\[
\mathcal B_{h,k}\ge2q_k\operatorname{arsinh}
\left(\frac{\delta k}{2C_h}\right).
\]

For fixed $a=\delta/(2C_h)>0$,

\[
\operatorname{arsinh}(ak)=
\log k+\log\left(a+\sqrt{a^2+k^{-2}}\right).
\]

The second term converges to the finite real number $\log(2a)$. Division
by $\log k$ and passage to the lower limit gives

\[
\liminf_{k\to\infty}\frac{\mathcal B_{h,k}}{q_k\log k}\ge2.
\]

This is the proved composition with the earlier exterior control. The new
analytic calculation supplies the $C_hq_k$ norm factor; it supplies no
upper estimate for these four quotient volumes. The exact determinant and
boundary maps in the source specify that further arithmetic quantity, and
their estimates remain the continuation lane.

## 11. Integration notes and verification boundary

The five particularly terse steps in the raw argument now have full written
calculations above: the discs inside the ellipse; the power-seven propagation
constant; the entire $g=hv_h$ inequality at selected centres; the typed
Legendre minimizer; and the factor-two allocation inside 64. None requires a
change to the claimed analytic theorem or to its stated constant. An integrated
proof can use this expanded derivation and impose $n\ge q$ only on the
graded isomorphism after source (13).

No numeric estimate of $c_\zeta,c_\Gamma,b_h,\vartheta_h,M_h(\pm b)$, or
$C_h$ was performed here. Positivity, finiteness, and dependence only on the
fixed packet and the fixed $b$ have been proved mathematically. The separate
checker review must describe its own executed tests; this report makes no
test-execution claim. All raw source bytes remained unchanged.
