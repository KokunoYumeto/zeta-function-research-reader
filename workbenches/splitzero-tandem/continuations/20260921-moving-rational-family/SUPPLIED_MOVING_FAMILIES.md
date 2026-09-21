# Moving rational families: uniform source activation, collision-stable coordinates, and the complete filtered heat

The inverse-sector calculation now extends from the single pole at zero to **every monic denominator whose poles lie in a fixed compact part of the original arithmetic resolvent set**. Poles may repeat, move, or collide with one another. Translated poles of the conductor may also coincide.

The principal result is a uniform comparison on the original arithmetic values:

$$
\boxed{
e^{-E_{k,d}}\mathfrak h_N(\alpha)I_d
\preceq
H_{D,N}^{B}(\alpha)
\preceq
H_{D,N}^{E}(\alpha)
\preceq
e^{E_{k,d}}\mathfrak h_N(\alpha)I_d,
}
\tag{1}
$$

where

$$
\mathfrak h_N(\alpha)
=
\frac{\mathsf S_N}{1-\alpha+\alpha\mathsf S_N},
\qquad 0\le\alpha\le1,
$$

and

$$
\boxed{
E_{k,d}
=
O_{h,A,\mathscr P}
\!\left(
k\log^2(q+2)+(k+Jd)\log(q+Jd+2)
\right).
}
\tag{2}
$$

Here \(D\) is any monic polynomial of degree \(d\) with its entire root multiset in the fixed pole set \(\mathscr P\). The matrices in (1) are the **original source and observation metrics on the same numerator coefficients**. In particular,

$$
d\log(q+2)=o(q)
\quad\Longrightarrow\quad
E_{k,d}=o(q)
$$

on the original simple-quartet family.

This has three further consequences.

First, the previously evaluated critical-activation coefficient is unchanged throughout this moving, confluent rational family:

$$
\boxed{
\mathcal R\log\det H_{D,N}^{X}(\alpha_k(\zeta))
=
dq\,C_{\mathrm{inv}}(\zeta)+o(dq),
\qquad X=E,B.
}
\tag{3}
$$

Second, polynomial filters between the corresponding quotient spaces have a bound uniform over the **whole physical activation interval**. The complete original observation feedback remains a rank-at-most-\(\dim K\) correction.

Third, for a monic filter \(F\) of degree \(s\) in the same pole family, all sufficiently slow singular directions of \(F(M)\) are confined to, and quantitatively detected through, its original rational sector. In particular, at every fixed \(c>0\),

$$
\boxed{
\operatorname{Tr}\!\left(
P_{(K+V_D)^\perp}
e^{-e^{cq}F(M)^\dagger F(M)}
\right)
\le e^{-cq+o(q)}
}
\tag{4}
$$

uniformly in \(0\le\alpha\le1\), whenever \(F\mid D\) and the stated degree range is retained.

The adjoint and projection in (4) are those of the **actual activated metric**. The polynomial filter, the kernel, and the quotient values are unchanged.

The construction also gives a global polynomial frame for the rational sector at parameters where a pole reaches an arithmetic root. At those parameters the ordinary rational formula ceases to exist, but the continued sector, its complete multiplicities, and its numerator-map defect are all explicit. That boundary calculation is in §6.

The supplied critical-activation result is used as an input to (3), not counted again as new. The new work is the uniformity in the complete pole family, its collision-stable realization, and its return through the original filtered action and heat. The earlier conductor paper treated the pole at zero and supplied its original minimum-metric return; those maps remain the starting point here.

---

## 1. Original objects and the moving-pole domain

Retain the original simple-quartet data

$$
k\equiv1\pmod4,\qquad
q=(k+1)^2,\qquad
0<\delta<\tfrac12,\qquad \gamma>2.
$$

Use the original centred variable

$$
y=\frac{S-k/2}{i},
$$

and write

$$
Q_k(y)
=
\prod_{a,b=0}^{k}
\bigl[y-(2b-k)\gamma+i(2a-k)\delta\bigr].
\tag{5}
$$

The polynomial is real, even, monic, and has no real root.

Let

$$
E_k=\mathbb C[y]/(Q_k),\qquad M[P]=[yP].
$$

For the original convolution measure

$$
d\mu_k(y)=m_k(y)\,dy,\qquad m_k=w_h^{*k},
$$

retain the full polynomial source Gram \(H_N\), remainder map \(J_N\), quotient metric, and attained source section

$$
G_N=(J_NH_N^{-1}J_N^*)^{-1},
\qquad
L_N=H_N^{-1}J_N^*G_N.
\tag{6}
$$

Thus \(L_N^*H_NL_N=G_N\).

The complete original observation is

$$
\Lambda:E_k\longrightarrow B_k,
\qquad K_k=\ker\Lambda,
$$

with

$$
Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},
\qquad
\mathcal L_N=G_N^{-1}\Lambda^*Q_{B,N}.
\tag{7}
$$

The distinction between \(L_N\), which lifts a full polynomial class, and \(\mathcal L_N\), which lifts an observed value, is retained.

The original added source has its full covariance

$$
\Omega_N=(G_N^J)^{-1}-G_N^{-1}\succeq0.
$$

Define its physical activation by

$$
\boxed{
G_N(\alpha)^{-1}
=
(1-\alpha)G_N^{-1}+\alpha(G_N^J)^{-1},
\qquad 0\le\alpha\le1.
}
\tag{8}
$$

The corresponding \(Q_{B,N}(\alpha)\), \(\mathcal L_N(\alpha)\), and projections are obtained by the same full minima.

The infinite odd lattice containing every root in (5) is

$$
\mathscr L_{\delta,\gamma}
=
\{(2b+1)\gamma+i(2a+1)\delta:a,b\in\mathbb Z\}.
$$

Choose a fixed compact set

$$
\boxed{\mathscr P\Subset\mathbb C\setminus\mathscr L_{\delta,\gamma}.}
\tag{9}
$$

Choose also a bounded finite polygonal domain \(\mathcal O\) with

$$
\mathscr P\subset\mathcal O,\qquad
\overline{\mathcal O}\cap\mathscr L_{\delta,\gamma}=\varnothing.
$$

Its oriented boundary is denoted \(\Gamma\). It may have several components and holes. These allow poles on different sides of lattice points without placing any lattice point inside \(\mathcal O\).

Put

$$
R_P=\max_{z\in\mathscr P}|z|,
\quad
R_\Gamma=\max\left(1,\max_{z\in\Gamma}|z|\right),
$$

$$
a_\Gamma=\operatorname{dist}(\mathscr P,\Gamma)>0,
\qquad
a_*=\operatorname{dist}(\mathscr P,\mathscr L_{\delta,\gamma})>0.
\tag{10}
$$

For every monic \(D\) of degree \(d\) with all roots in \(\mathscr P\), define

$$
\boxed{
U_D:\mathcal P_{d-1}\longrightarrow E_k,
\qquad
U_Dp=[p/D].
}
\tag{11}
$$

This uses the inverse of the actual multiplication operator \(D(M)\).

Its two metrics are

$$
\boxed{
H_{D,N}^{E}(\alpha)=U_D^*G_N(\alpha)U_D,
}
$$

$$
\boxed{
H_{D,N}^{B}(\alpha)
=
(\Lambda U_D)^*Q_{B,N}(\alpha)(\Lambda U_D).
}
\tag{12}
$$

The coefficient basis is \(1,y,\ldots,y^{d-1}\) for the **numerator** \(p\). No separated-pole basis is used.

In particular, \(D\) may have real roots, including zero. The proof never integrates \(p(y)/D(y)\) against the physical measure. It constructs and integrates actual polynomial representatives of that quotient class.

---

## 2. A polynomial representative with a uniform moving-pole bound

Set

$$
n_0=2\left\lfloor\frac{N+1-q}{2}\right\rfloor,
\qquad q-1\le N\le2q.
$$

Let \(\mathcal K_{Q,n}\) be the Christoffel kernel in the full measure

$$
|Q_k(y)|^2\,d\sigma(y),
\qquad
d\sigma(y)
=
\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy.
$$

Its mass is not normalized to one:

$$
\int d\sigma=\sqrt{2\pi}=:M_\sigma.
$$

Retain the original polynomial

$$
H_{Q,n_0}(y)
=
\frac{\mathcal K_{Q,n_0}(y,0)}
{\mathcal K_{Q,n_0}(0,0)},
\qquad H_{Q,n_0}(0)=1,
$$

and put

$$
\boxed{
T_N=
\frac1{|Q_k(0)|\sqrt{\mathcal K_{Q,n_0}(0,0)}},
\qquad
\mathsf S_N=u_kT_N^2.
}
\tag{13}
$$

Here \(u_k\) is the original upper full-form comparison constant

$$
\|P\|_{\mu_k}^2\le u_k\|P\|_\sigma^2.
$$

The supplied hard-gap estimates, on their explicit eventual degree domain, are

$$
\beta_q=2^{-27}q^2,
$$

$$
|H_{Q,n_0}(z)|
\ge e^{-n_0|z|^2/\beta_q},
\qquad |z|^2\le\beta_q/2,
\tag{14}
$$

and

$$
\mathcal K_{Q,n}(z,z)
\le
e^{n|z|^2/\beta_q}
\left(1+\frac{|z|^2}{\beta_q}\right)
\mathcal K_{Q,n}(0,0).
\tag{15}
$$

These involve the complete preceding relation space.

### 2.1 Uniform control of the original root product on the pole contour

Pair every root \(\omega\) of \(Q_k\) with \(-\omega\). For roots with \(|\omega|>2R_\Gamma\),

$$
\left|1-\frac{z^2}{\omega^2}\right|^{-1}
\le
\exp\left(\frac{2R_\Gamma^2}{|\omega|^2}\right),
\qquad z\in\Gamma.
$$

The finitely many lattice pairs with \(|\omega|\le2R_\Gamma\) have a fixed nonzero distance from \(\Gamma\). Their product gives a fixed constant \(C_\Gamma\).

The shell count on the original odd rectangular lattice gives

$$
\sum_{\omega/\{\pm1\}}\frac1{|\omega|^2}
\le
\frac2{\delta^2}
\sum_{\substack{1\le j\le k\\j\text{ odd}}}\frac1j.
$$

Consequently

$$
\boxed{
\sup_{z\in\Gamma}
\left|\frac{Q_k(0)}{Q_k(z)}\right|
\le
C_\Gamma
\exp\left[
\frac{4R_\Gamma^2}{\delta^2}
\sum_{\substack{j\le k\\j\text{ odd}}}\frac1j
\right].
}
\tag{16}
$$

The logarithm of this bound is \(O_{\mathscr P,h}(\log(k+2))\).

### 2.2 Confluent interpolation without pole-separation denominators

For a function \(F\) holomorphic on \(\mathcal O\), its remainder modulo \(D\) is

$$
\boxed{
\operatorname{rem}_D F(y)
=
\frac1{2\pi i}
\int_\Gamma
F(z)\frac{D(z)-D(y)}{D(z)(z-y)}\,dz.
}
\tag{17}
$$

The right side is a polynomial of degree below \(d\). Differentiating at each root of \(D\) proves that it has the complete required jets, including repeated roots.

Let \(\|\cdot\|_1\) denote the sum of absolute polynomial coefficients. Since

$$
\|D\|_1\le(1+R_P)^d,\qquad
|D(z)|\ge a_\Gamma^d\quad(z\in\Gamma),
$$

equation (17) gives

$$
\boxed{
\|\operatorname{rem}_D F\|_1
\le
\frac{\operatorname{length}\Gamma}{2\pi}
d(1+R_P)^dR_\Gamma^{d-1}a_\Gamma^{-d}
\sup_\Gamma|F|.
}
\tag{18}
$$

There is no factor \((z_i-z_j)^{-1}\).

Take

$$
R_{D,p}
=
\operatorname{rem}_D
\left(\frac{p}{Q_kH_{Q,n_0}}\right).
$$

The denominator is nonzero on \(\overline{\mathcal O}\) on the stated hard-gap domain. Define

$$
\boxed{
P_{D,p}
=
\frac{p-Q_kH_{Q,n_0}R_{D,p}}{D}.
}
\tag{19}
$$

It is a polynomial, has degree at most \(q+n_0-1\le N\), and satisfies

$$
J_NP_{D,p}=U_Dp.
$$

Thus (19) is an actual original source representative.

### 2.3 Its full source norm

For \(|z|\le R_P\), the Gamma evaluation kernel has the explicit bound

$$
M_\sigma\mathcal K_{\sigma,L}(z,z)
\le
C_{R_P}(L+1)^{3+2R_P},
$$

where one valid constant is

$$
C_R=e^2\,2^{2+2R}e^{\pi R}.
\tag{20}
$$

This follows directly from the original Meixner–Pollaczek generating function by Cauchy’s coefficient estimate.

Let

$$
b_L=\sqrt{2L+1}\sum_{j=1}^{L}\frac1j,
$$

and define

$$
\mathfrak d_L(R)
=
\max\left\{
1,\,
2b_L\left[1+\sqrt{C_R}(L+1)^{(3+2R)/2}\right]
\right\}.
\tag{21}
$$

The exact divided difference

$$
\mathscr D_zP=\frac{P(y)-P(z)}{y-z}
$$

has Gamma norm at most \(\mathfrak d_L(R)\) on degree \(L\), uniformly for \(|z|\le R\). The proof applies the original lower multiplication estimate to \((y-z)\mathscr D_zP\), then uses (20) for \(P(z)\).

Successive divided differences give polynomial division by \(D\), even when its roots repeat. Therefore

$$
\|\operatorname{quo}_D P\|_\sigma
\le
\mathfrak d_L(R_P)^d\|P\|_\sigma.
\tag{22}
$$

Since \(\operatorname{quo}_D p=0\), equation (19) is

$$
P_{D,p}
=
-\operatorname{quo}_D(Q_kH_{Q,n_0}R_{D,p}).
$$

Combining (14), (16), (18), (22), and the original Gamma multiplication bound proves

$$
\boxed{
\|U_Dp\|_{G_N}
\le
\sqrt{u_k}\,\mathcal U_{k,d,N}\,T_N\|p\|_2,
}
\tag{23}
$$

where the following fully specified choice is valid:

$$
\begin{aligned}
\mathcal U_{k,d,N}
={}&
\mathfrak d_{N+d}(R_P)^d
[2(N+d+1)]^{d-1}\\
&\times
\frac{\operatorname{length}\Gamma}{2\pi}
d^{3/2}(1+R_P)^dR_\Gamma^{2d-2}a_\Gamma^{-d}\\
&\times
C_\Gamma
\exp\left[
\frac{4R_\Gamma^2}{\delta^2}
\sum_{\substack{j\le k\\j\text{ odd}}}\frac1j
+\frac{n_0R_\Gamma^2}{\beta_q}
\right].
\end{aligned}
\tag{24}
$$

In particular,

$$
\log^+\mathcal U_{k,d,N}
=
O_{h,\mathscr P}\bigl(d\log(q+d+2)+\log(k+2)\bigr).
$$

---

## 3. The complete original conductor gives a matching lower bound

Retain the original lower packet

$$
q'=(k-7)^2,\qquad
Q_-(y),
\qquad
\Delta=q-q'=16k-48.
$$

In the centred variables, the original conductor is

$$
\boxed{
\mathcal T_Af(y)=\sum_{j=1}^{J}a_jf(y-\zeta_j),
\qquad
\zeta_j=i(b_j-4).
}
\tag{25}
$$

The coordinate identity is

$$
\frac{\eta+b_j-k/2}{i}
=
\frac{\eta-(k/2-4)}i-\zeta_j.
$$

Thus the factor \(i\), the centre shift four, and every conductor coefficient remain.

Let

$$
A_\Sigma=\sum_j|a_j|,
\qquad Z=\max_j|\zeta_j|.
$$

The original symbol order is still \(v\). Its centred moments

$$
m_l=\sum_ja_j\zeta_j^l
$$

satisfy

$$
m_l=0\quad(l<v),\qquad m_v=i^v\mu_v\ne0.
\tag{26}
$$

### 3.1 A common denominator retains translated-pole collisions

For \(p\in\mathcal P_{d-1}\), put

$$
\mathcal B_D(y)=\prod_{j=1}^{J}D(y-\zeta_j),
\qquad L=Jd,
$$

$$
\boxed{
\mathcal N_Dp
=
\mathcal B_D
\sum_{j=1}^{J}a_j\frac{p(y-\zeta_j)}{D(y-\zeta_j)}.
}
\tag{27}
$$

This is a polynomial of degree at most \(L-v-1\).

The product \(\mathcal B_D\) retains repeated factors when translated poles coincide. Nothing is cancelled to create a changing-degree denominator.

The map \(p\mapsto\mathcal N_Dp\) is injective. Indeed, for a nonzero proper rational function

$$
f(y)=cy^{-n_0}+O(y^{-n_0-1}),
$$

equation (26) gives

$$
\boxed{
\mathcal T_Af(y)
=
\binom{n_0+v-1}{v}m_vc\,y^{-n_0-v}
+O(y^{-n_0-v-1}),
}
\tag{28}
$$

whose leading coefficient is nonzero.

### 3.2 An explicit coefficient inverse bound

Write

$$
\frac{p(y)}{D(y)}=\sum_{n\ge1}c_ny^{-n},
\qquad
\mathcal T_A(p/D)=\sum_{m\ge1}b_my^{-m}.
$$

Set

$$
e(z)=z^{-v}\sum_ja_je^{\zeta_jz},
\qquad e_0=\frac{m_v}{v!}.
$$

Choose the explicit radius

$$
r_A=
\min\left\{
1,\,
\frac{|e_0|(v+1)!}
{2A_\Sigma\max(1,Z)^{v+1}e^{\max(1,Z)}}
\right\}.
$$

Then \(|e(z)-e_0|\le|e_0|/2\) on \(|z|\le r_A\), and

$$
|[z^j]e(z)^{-1}|\le2|e_0|^{-1}r_A^{-j}.
$$

The exact inverse is

$$
\boxed{
c_n
=
(n-1)!
\sum_{l=1}^{n}
[z^{n-l}]e(z)^{-1}
\frac{b_{v+l}}{(v+l-1)!},
\qquad1\le n\le d,
}
\tag{29}
$$

followed by

$$
\boxed{
p(y)=\operatorname{pol}_{y=\infty}
\left[D(y)\sum_{n=1}^{d}c_ny^{-n}\right].
}
\tag{30}
$$

Put

$$
R_B=R_P+Z,\qquad
r_\infty=\frac1{2\max(1,R_B)}.
$$

The reciprocal of the common denominator has modulus at most \(2^L\) on \(|z|=r_\infty\). Cauchy’s coefficient estimate in (29)–(30) gives

$$
\boxed{
\|p\|_2\le\mathcal I_d\|\mathcal N_Dp\|_1,
}
\tag{31}
$$

with

$$
\boxed{
\mathcal I_d=
\frac{
2d^2(d-1)!(1+R_P)^d2^L
}{
|e_0|
}
r_A^{-(d-1)}r_\infty^{1-v-d}.
}
\tag{32}
$$

Its logarithm is \(O_A(Jd\log(d+2))\), uniformly over the pole family.

### 3.3 Carry the numerator through the full lower-source minimum

Let \(g\) be any original lower polynomial representative of the conductor value, of degree at most \(N-v\). Then

$$
\boxed{
\mathcal B_Dg-\mathcal N_Dp=Q_-h,
\qquad
\deg h\le n_-:=N-v+L-q'.
}
\tag{33}
$$

All functions in (33) are polynomials. No rational function with a real pole is integrated.

Assume the explicit finite degree guards

$$
L-v\le q',\qquad
n_-\le2q'-2,
\tag{34}
$$

together with the supplied hard-gap guards for \(Q_-\). They hold eventually throughout \(d\log(q+2)=o(q)\).

Because \(\deg\mathcal N_Dp<L\),

$$
\mathcal N_Dp=-\operatorname{rem}_{\mathcal B_D}(Q_-h).
$$

Use the circle of radius

$$
R_C=R_B+1.
$$

It stays at distance at least one from every root of \(\mathcal B_D\). The remainder formula (17) gives

$$
\|\mathcal N_Dp\|_1
\le
L R_C^{2L}\sup_{|z|=R_C}|Q_-(z)h(z)|.
\tag{35}
$$

The original full relation kernel gives

$$
\begin{aligned}
\sup_{|z|=R_C}|Q_-(z)h(z)|
\le{}&
|Q_-(0)|\,\mathcal P_-\mathcal E_-
\sqrt{\mathcal K_{Q_-,n_-}(0,0)}\,
\|Q_-h\|_\sigma,
\end{aligned}
\tag{36}
$$

where

$$
\mathcal P_-=
\exp\left[
R_C^2
\sum_{\omega\in\operatorname{roots}(Q_-)/\{\pm1\}}
|\omega|^{-2}
\right],
$$

$$
\mathcal E_-=
e^{n_-R_C^2/(2\beta_{q'})}
\sqrt{1+R_C^2/\beta_{q'}}.
$$

The complete near-degree kernel comparison from the original proof supplies

$$
\mathcal K_{Q_-,n_-}(0,0)
\le
\mathcal D_{\mathrm{near}}\,
\mathcal W^{2\Delta}
\mathcal K_{Q_k,n_0}(0,0),
$$

with

$$
\mathcal W=2(q+n_0+1)+k\sqrt{\delta^2+\gamma^2}.
$$

Here \(\mathcal D_{\mathrm{near}}\) is the retained finite product over the intervening even degrees. Its logarithm is

$$
O_h((k+L)\log(q+L+2)).
$$

Define the positive finite number

$$
\boxed{
C_0=
\frac{|Q_k(0)/Q_-(0)|}
{
\mathcal W^\Delta\sqrt{\mathcal D_{\mathrm{near}}}\,
\mathcal I_d\,L R_C^{2L}\mathcal P_-\mathcal E_-
}.
}
\tag{37}
$$

Equations (31), (35), and (36) prove

$$
\boxed{
\|Q_-h\|_\sigma\ge C_0T_N\|p\|_2.
}
\tag{38}
$$

The finite boundary product is not left as an unspecified asymptotic:

$$
|Q_k(0)/Q_-(0)|
=
\prod_{\omega\in\operatorname{roots}(Q_k/Q_-)}|\omega|
\ge[\delta(k-6)]^\Delta.
$$

For the other polynomial in (33), one valid bound is

$$
\|\mathcal N_Dp\|_\sigma\le\mathcal A_d\|p\|_2,
$$

$$
\mathcal A_d
=
\sqrt{M_\sigma}\,A_\Sigma\sqrt d\,
(1+Z)^{d-1}
\max(1,2(L+1)+R_B)^{L-1}.
\tag{39}
$$

Also,

$$
\|\mathcal B_Dg\|_\sigma
\le
\mathcal B_{N,d}^{\,L}\|g\|_\sigma,
\qquad
\mathcal B_{N,d}
=
\max(1,2(N-v+L+1)+R_B).
$$

Thus, on the finite guard

$$
C_0T_N\ge2\mathcal A_d,
$$

equation (33) yields

$$
\boxed{
\|g\|_\sigma
\ge
\frac{C_0}{2\mathcal B_{N,d}^{\,L}}
T_N\|p\|_2.
}
\tag{40}
$$

### 3.4 The guard has an explicit eventual certificate

The original Gamma lower envelope includes

$$
\sigma(y)\ge c_\sigma\frac{e^{-\pi|y|/2}}{1+4y^2}.
$$

On \([q,2q]\), \(|Q_k(y)|\ge(q/2)^q\) once the root radius is at most \(q/2\).

The Legendre evaluation bound at zero for polynomials on \([q,2q]\) gives

$$
\boxed{
T_N\ge
\underline T_N:=
\frac{
\sqrt{c_\sigma q}\,(q/2)^q e^{-\pi q/2}
}{
|Q_k(0)|\sqrt{1+16q^2}\,(n_0+1)6^{n_0}
}.
}
\tag{41}
$$

Since

$$
|Q_k(0)|\le
\bigl(k\sqrt{\delta^2+\gamma^2}\bigr)^q,
$$

$$
\log\underline T_N
\ge q\log(q/k)-O_h(q).
$$

By contrast,

$$
\log^+C_0^{-1}+\log^+\mathcal A_d
=
O_{h,A,\mathscr P}((k+Jd)\log(q+Jd+2)).
$$

Hence the directly checkable guard

$$
C_0\underline T_N\ge2\mathcal A_d
\tag{42}
$$

holds eventually in the stated degree range.

### 3.5 Return through the original observation

The original conductor annihilates the complete \(K_k\). Its Gamma operator norm on degree \(N\) is bounded, for example, by

$$
\mathcal F_N=A_\Sigma e^{Zb_N}.
$$

This follows from the exact finite translation

$$
f(y-\zeta)=e^{-\zeta\partial_y}f(y)
$$

and the original Gamma derivative norm.

Let

$$
\ell_{k,N}\|P\|_\sigma^2
\le\|P\|_{\mu_k}^2
\le u_k\|P\|_\sigma^2.
$$

Apply the conductor bound to every polynomial representative of an observed value, and then minimize over the complete original fibre. Equation (40) proves

$$
\boxed{
\|\Lambda U_Dp\|_{Q_{B,N}}
\ge
\frac{\sqrt{\ell_{k,N}}\,C_0}
{2\mathcal F_N\mathcal B_{N,d}^{\,L}}
T_N\|p\|_2.
}
\tag{43}
$$

Together with (23),

$$
\boxed{
a_{k,d,N}\mathsf S_NI
\preceq H_{D,N}^{B}(0)
\preceq H_{D,N}^{E}(0)
\preceq b_{k,d,N}\mathsf S_NI,
}
\tag{44}
$$

where

$$
a_{k,d,N}
=
\frac{\ell_{k,N}}{u_k}
\left(\frac{C_0}
{2\mathcal F_N\mathcal B_{N,d}^{\,L}}\right)^2,
\qquad
b_{k,d,N}=\mathcal U_{k,d,N}^2.
$$

The logarithmic cost is

$$
O_{h,A,\mathscr P}((k+Jd)\log(q+Jd+2)).
$$

This proves the moving-pole canonical estimate without using a pole-separation Vandermonde.

---

## 4. Extend the comparison uniformly to every physical activation

Retain the source’s complete tensor reference \(T_k\) and its actual bounds

$$
\mathbf L_k^{-1}T_k\preceq G_N^J\preceq\mathbf B_kT_k,
\qquad
\log\mathbf L_k+\log\mathbf B_k
=O_h(k\log^2(q+2)).
\tag{45}
$$

The reference is the original polynomial-value metric pulled back through the complete physical unit. That unit is not omitted from the physical injection.

In root-value coordinates, let its weights be \(W_\omega\), with

$$
W_\omega\ge a_{\min}^k,\qquad
\sum_\omega W_\omega=A_w^k.
$$

The full original cardinal lift

$$
P_\omega(y)
=
\frac{Q_k(y)H_{Q,n_0}(y)}
{(y-\omega)Q_k'(\omega)H_{Q,n_0}(\omega)}
$$

has degree at most \(N\) and the exact cardinal values.

The original rectangular product gives

$$
\frac{|Q_k(0)|}{|Q_k'(\omega)|}
\le
R_0e^{4kR_0/\delta},
\qquad R_0=\sqrt{\delta^2+\gamma^2}.
$$

One proof is to locate the minimum derivative product at the four central roots using consecutive product ratios, then sum

$$
\log\frac{|\omega|}{|\omega-\omega_*|}
\le\frac{R_0}{|\omega-\omega_*|}
$$

over the complete rectangular shells.

Using (14) for the cardinal lift gives

$$
\boxed{
G_N\preceq\Gamma_N\mathsf S_NT_k,
}
\tag{46}
$$

where

$$
\Gamma_N=
\frac{qR_0^2}{\delta^2a_{\min}^k}
\exp\left[
\frac{8kR_0}{\delta}
+\frac{2n_0k^2R_0^2}{\beta_q}
\right].
$$

Equations (45)–(46) imply the full-space harmonic lower bound

$$
\boxed{
G_N(\alpha)\succeq
\frac{G_N}
{1-\alpha+\alpha\mathbf L_k\Gamma_N\mathsf S_N}.
}
\tag{47}
$$

The identical inequality holds for the original observation quotient, because the same affine minimum is taken on both sides.

For the rational numerator space, (9) gives a fixed constant \(C_{\mathscr P}\) such that

$$
\left|\frac{p(\omega)}{D(\omega)}\right|
\le\sqrt d\,C_{\mathscr P}^{\,d}\|p\|_2
$$

at every original lattice point. Near the fixed pole region this is the retained distance \(a_*\); far from it, every denominator factor is at least \(|\omega|/2\).

Consequently

$$
U_D^*T_kU_D
\preceq dC_{\mathscr P}^{2d}A_w^kI.
\tag{48}
$$

Combining the canonical upper bound with

$$
G_N(\alpha)\preceq\alpha^{-1}G_N^J
$$

and using (47) gives (1), with the explicit choices

$$
\underline a_{k,d,N}
=
\frac{a_{k,d,N}}{\max(1,\mathbf L_k\Gamma_N)},
$$

$$
\overline b_{k,d,N}
=
b_{k,d,N}
+\mathbf B_kdC_{\mathscr P}^{2d}A_w^k,
$$

$$
\boxed{
E_{k,d}
=
\max_N
\left\{
\log^+\overline b_{k,d,N},
\log^+\underline a_{k,d,N}^{-1}
\right\}.
}
\tag{49}
$$

These formulas prove the uniformity in (2). In particular, no activation-dependent minimum eigenvalue is left inside the error constant.

---

## 5. Critical activation, all fixed rational subquotients, and the original kernel

At the four original cutoffs,

$$
n_0=0,0,q,q.
$$

Thus \(\mathsf S_N\) takes precisely two values, \(\mathsf S_L,\mathsf S_H\).

Equation (1) gives the finite determinant formula

$$
\boxed{
\begin{aligned}
\left|
\mathcal R\log\det H_{D,N}^{X}(\alpha)
-
2d\log
\frac{
\mathsf S_L(1-\alpha+\alpha\mathsf S_H)
}{
\mathsf S_H(1-\alpha+\alpha\mathsf S_L)
}
\right|
\le4dE_{k,d},
\end{aligned}
}
\tag{50}
$$

for \(X=E,B\), uniformly over the complete pole family.

The supplied critical-activation calculation gives

$$
\log\mathsf S_L
=
2q\log(q/k)+\beta_Lq+o(q),
$$

$$
\log\mathsf S_H
=
2q\log(q/k)+\beta_Hq+o(q),
\qquad
2(\beta_L-\beta_H)=\mathfrak C,
$$

with

$$
1.353893<\mathfrak C<1.354751.
$$

For

$$
\alpha_k(\zeta)
=
e^{-2q\log(q/k)-\zeta q},
$$

the scalar identity

$$
\log\frac{\mathsf S}{1-\alpha+\alpha\mathsf S}
=
\min(\log\mathsf S,-\log\alpha)+O(1)
$$

is uniform once \(\mathsf S\ge1\). Substitution into (50) proves (3), with

$$
\boxed{
C_{\mathrm{inv}}(\zeta)
=
2\bigl[\min(\beta_L,\zeta)-\min(\beta_H,\zeta)\bigr].
}
\tag{51}
$$

Thus the critical coefficient is the same for every denominator in this compact moving-pole family. The numerator frame and all its coefficients remain fixed in meaning.

Every fixed restriction or full quotient of the numerator space receives the same comparison by applying it to every representative of the same affine fibre. Its rank replaces \(d\) in the determinant error. No separate orientation assumption enters that passage.

### 5.1 Uniform kernel deflation

Let

$$
\Gamma_D=I_K^*G_N(\alpha)U_D,
\qquad
H_K=I_K^*G_N(\alpha)I_K.
$$

The full observed rational metric is

$$
H_D^B
=
H_D^E-\Gamma_D^*H_K^{-1}\Gamma_D.
$$

The metric induced on the original kernel after quotienting by \(V_D=\operatorname{im}U_D\) is

$$
\widehat H_K
=
H_K-\Gamma_D(H_D^E)^{-1}\Gamma_D^*.
$$

The same block determinant gives

$$
\boxed{
\delta_D
:=
\log\frac{\det H_D^E}{\det H_D^B}
=
\log\frac{\det H_K}{\det\widehat H_K},
}
\tag{52}
$$

and (1) gives

$$
\boxed{
0\le\delta_D\le2\min(\dim K,d)E_{k,d}.
}
\tag{53}
$$

For \(d=\lfloor q/\log^2(q+2)\rfloor\), the four-cutoff error is

$$
O_{h,A,\mathscr P}
\left(k^2\log^2q+\frac{Jkq}{\log q}\right)
=o(kq).
\tag{54}
$$

This is uniform in \(\alpha\) and in the full pole multiset.

It removes the same original kernel directions by an actual quotient. It does not set the remaining kernel determinant to zero.

---

## 6. A global polynomial frame continues the sector across arithmetic poles

The compact-resolvent estimates require \((D,Q_k)=1\). The **sector itself** has a canonical finite continuation when that resultant vanishes.

This calculation works for every monic \(Q\) of degree \(q\), including complete primary multiplicities.

For every monic \(D\) of degree \(d\le q\), define

$$
\boxed{
\pi_D[P]
=
\operatorname{quo}_D
\operatorname{rem}_Q(DP)
\in\mathcal P_{q-d-1}.
}
\tag{55}
$$

The ordinary inclusion

$$
\iota_D:\mathcal P_{q-d-1}\hookrightarrow E
$$

satisfies

$$
\pi_D\iota_D=I,
$$

because \(DP\) has degree below \(q\) on that subspace.

Hence

$$
\boxed{
V_D^{\mathrm{flat}}:=\ker\pi_D
}
$$

has dimension exactly \(d\) for **every** monic \(D\).

An explicit global polynomial frame is

$$
\boxed{
F_De_j
=
[y^{q-d+j}]
-\iota_D\pi_D[y^{q-d+j}],
\qquad0\le j<d.
}
\tag{56}
$$

Its high-degree coefficient block is the identity. Its entries are polynomial in the coefficients of \(D\).

On the resolvent locus,

$$
V_D^{\mathrm{flat}}=V_D.
$$

Define the numerator map

$$
B_De_j
=
\operatorname{rem}_D
\operatorname{rem}_Q(Dy^{q-d+j}).
$$

Then

$$
\boxed{
D(M)F_D=B_D,\qquad
U_D=F_DB_D^{-1},
}
\tag{57}
$$

and

$$
\boxed{
\det B_D
=
(-1)^{d(q-d)}\operatorname{Res}(Q,D).
}
\tag{58}
$$

For (58), use the domain basis \([F_D,\mathcal P_{q-d-1}]\), whose determinant is the displayed permutation sign, and the codomain basis

$$
[\mathcal P_{d-1},D\mathcal P_{q-d-1}],
$$

whose triangular coefficient determinant is one. The multiplication map has block diagonal \(\operatorname{diag}(B_D,I)\).

Let

$$
g=\gcd(Q,D),\qquad e=\deg g.
$$

At the boundary, the exact sequence is

$$
\boxed{
0\longrightarrow
(Q/g)\mathcal P_{e-1}
\longrightarrow
V_D^{\mathrm{flat}}
\xrightarrow{\,D(M)\,}
g\mathcal P_{d-e-1}
\longrightarrow0.
}
\tag{59}
$$

The left term is the full multiplication kernel. The right term is the intersection of the multiplication image \((g)\subset E\) with the retained numerator space.

Thus a rational-pole collision with the arithmetic spectrum is recorded by an actual multiplication defect, not by reducing the original primary algebra.

### 6.1 Exact metric factor at the resultant

For every original positive metric \(G\),

$$
\boxed{
U_D^*GU_D
=
B_D^{-*}(F_D^*GF_D)B_D^{-1}.
}
\tag{60}
$$

The observed metric has the identical congruence.

Therefore

$$
\log\det(U_D^*GU_D)
=
\log\det(F_D^*GF_D)
-2\log|\operatorname{Res}(Q,D)|.
\tag{61}
$$

The same resultant factor cancels in the source/observation determinant ratio and in every original four-cutoff return with the same \(D\).

On a parameter chart where \(\Lambda F_D\) retains full rank, the observed fraction and the determinant angle extend through the resultant divisor in the frame \(F_D\). Where that rank drops, the actual new kernel

$$
V_D^{\mathrm{flat}}\cap\ker\Lambda
$$

must be retained. Equation (59) does not assert its absence.

For example,

$$
Q=y^2+1,\qquad D=y-z
$$

gives

$$
F_D=y+z,\qquad B_D=-(1+z^2),
$$

$$
[y-z]^{-1}=-\frac{y+z}{1+z^2}.
$$

At \(z=i\), the continued vector \(y+i\) is a nonzero \(i\)-eigenvector of \(M\). The rational numerator map vanishes, but the continued sector has not disappeared.

---

## 7. Polynomial filters give an exact rational quotient system

Let \(D,F\) be monic, with degrees \(d,s\), and \(d+s\le q\). On the resolvent domain define

$$
\boxed{
\mathcal I_{D,F}:E/V_D\longrightarrow E/V_{DF},
\qquad
[x]\longmapsto[F(M)^{-1}x].
}
\tag{62}
$$

Under the explicit coordinates (55), this is simply polynomial quotient by \(F\):

$$
\boxed{
\pi_{DF}F(M)^{-1}
=
\operatorname{quo}_F\,\pi_D.
}
\tag{63}
$$

Its kernel is \(\mathcal P_{s-1}\), and multiplication by \(F\) supplies its right inverse.

The identity that remains valid even on the resultant boundary is

$$
\boxed{
\pi_{DF}
=
\operatorname{quo}_F\,\pi_DF(M).
}
\tag{64}
$$

It follows by dividing the actual polynomial
\(\operatorname{rem}_Q(DFP)\) first by \(D\), then by \(F\). Thus the coefficient map extends polynomially, while its interpretation as multiplication by \(F(M)^{-1}\) is confined to the domain where that inverse exists.

For a third factor \(G\),

$$
\boxed{
\mathcal I_{DF,G}\mathcal I_{D,F}
=
\mathcal I_{D,FG}.
}
\tag{65}
$$

### 7.1 Uniform bounds in every activated metric

The original scalar minimum section gives the exact finite-rank decomposition

$$
\boxed{
F(M)^{-1}
=
J_N\operatorname{quo}_F L_N
+
U_F\operatorname{rem}_F L_N.
}
\tag{66}
$$

The second term is in \(V_F\), which is killed in \(E/V_{DF}\).

Equation (22) and one complete arithmetic/Gamma comparison give the canonical quotient bound

$$
b_0=
\sqrt{u_k/\ell_{k,N}}\,
\mathfrak d_N(R_P)^s.
\tag{67}
$$

Only one full-form comparison is charged, not one for each linear factor.

At the joint endpoint, the original root-value reference gives

$$
b_1=
\sqrt{\mathbf B_k\mathbf L_k}\,a_*^{-s}.
\tag{68}
$$

Indeed, multiplication by \(F(M)^{-1}\) has reference norm

$$
\max_{\omega:Q_k(\omega)=0}|F(\omega)|^{-1}\le a_*^{-s}.
$$

For the same map \(T\) between the two quotient spaces, an endpoint norm bound is equivalent to

$$
T\,G_{\mathrm{domain}}^{-1}T^*
\preceq b^2G_{\mathrm{target}}^{-1}.
$$

Take the convex combination of this exact inequality at \(\alpha=0,1\). Since quotient covariances are linear images of the original covariance in (8), this proves

$$
\boxed{
\|\mathcal I_{D,F}\|_{\overline G_D(\alpha)\to\overline G_{DF}(\alpha)}
\le
B_{s,N}:=\max(b_0,b_1),
\qquad0\le\alpha\le1.
}
\tag{69}
$$

In the stated degree range,

$$
\boxed{
\log^+ B_{s,N}
=
O_{h,\mathscr P}(k\log^2(q+2)+s\log(q+s+2))
=o(q).
}
\tag{70}
$$

### 7.2 The original observation keeps its full feedback term

Let \(\bar\Lambda_D\) be the induced observation

$$
E/V_D\longrightarrow B/\Lambda V_D,
$$

and let \(\bar L_D\) be its actual minimum section. Define

$$
\mathcal B_{D,F}
=
\bar\Lambda_{DF}\mathcal I_{D,F}\bar L_D.
$$

Then

$$
\boxed{
\begin{aligned}
\mathcal B_{D,FG}
-\mathcal B_{DF,G}\mathcal B_{D,F}
={}&
\bar\Lambda_{DFG}\mathcal I_{DF,G}
P_{\ker\bar\Lambda_{DF}}
\mathcal I_{D,F}\bar L_D.
\end{aligned}}
\tag{71}
$$

Its rank is at most \(\dim K\), and its norm is at most
\(B_{\deg F,N}B_{\deg G,N}\).

The right side is the complete arithmetic feedback through the deflated original kernel. It has not been declared zero by the polynomial composition law (65).

---

## 8. The entire low filtered spectrum is controlled

Take the case \(D=1\) in (69). In the actual activated metric,

$$
\left\|
(I-P_{V_F})F(M)^{-1}
\right\|
\le B_{s,N}.
\tag{72}
$$

Write

$$
F(M)^{-1}
=
\underbrace{(I-P_{V_F})F(M)^{-1}}_{\text{norm }\le B_{s,N}}
+
\underbrace{P_{V_F}F(M)^{-1}}_{\text{rank }\le s}.
\tag{73}
$$

Consequently the \((s+1)\)-st singular value of \(F(M)^{-1}\) is at most \(B_{s,N}\). Equivalently, for

$$
H_F=F(M)^\dagger F(M),
$$

the spectral space below \(B_{s,N}^{-2}\) has dimension at most \(s\).

Let \(P_{\le\lambda}\) be its full spectral projection. For

$$
0<\lambda<B_{s,N}^{-2},
$$

equation (72) gives

$$
\boxed{
\|(I-P_{V_F})P_{\le\lambda}\|
\le B_{s,N}\sqrt\lambda,
\qquad
\operatorname{rank}P_{\le\lambda}\le s.
}
\tag{74}
$$

This identifies the whole low spectral space quantitatively. No simple-smallest-singular-value assumption is needed.

### 8.1 Its actual observation fraction

Let

$$
\ell_{F,N,\alpha}
=
\lambda_{\min}\left[
(H_F^E)^{-1/2}H_F^B(H_F^E)^{-1/2}
\right].
$$

Equation (1) proves

$$
\ell_{F,N,\alpha}\ge e^{-2E_{k,s}}.
$$

For a unit vector in \(\operatorname{ran}P_{\le\lambda}\), its distance to \(V_F\) is at most

$$
\varepsilon=B_{s,N}\sqrt\lambda.
$$

The exact two-subspace angle bound gives

$$
\boxed{
\|P_Bx\|^2
\ge
\left[
\sqrt{\ell_{F,N,\alpha}}\sqrt{1-\varepsilon^2}
-\sqrt{1-\ell_{F,N,\alpha}}\varepsilon
\right]_+^2.
}
\tag{75}
$$

The factor \(\sqrt{1-\ell}\) retains the actual complementary angle.

For every fixed \(c>0\), at \(\lambda=e^{-cq}\), equations (2) and (70) imply

$$
\varepsilon^2=e^{-cq+o(q)},
\qquad
\ell_{F,N,\alpha}\ge e^{-o(q)}.
$$

Thus every such low spectral vector is detected with fraction

$$
\boxed{
\ell_{F,N,\alpha}(1-o(1)),
}
\tag{76}
$$

uniformly over the activation and pole family.

### 8.2 Full filtered heat outside the rational sector

Let \(P_R\) be any original orthogonal projection annihilating \(V_F\). Let

$$
\sigma_1\ge\cdots\ge\sigma_q
$$

be the singular values of \(F(M)^{-1}\), and \(a_j\) its left singular vectors. Equation (72) gives

$$
\|P_Ra_j\|\le B_{s,N}/\sigma_j.
$$

For the first \(s\) vectors,

$$
e^{-\tau/\sigma_j^2}\|P_Ra_j\|^2
\le\frac{B_{s,N}^2}{e\tau}.
$$

For the rest, \(\sigma_j\le B_{s,N}\). Summing the entire spectrum proves

$$
\boxed{
0\le
\operatorname{Tr}(P_Re^{-\tau H_F})
\le
s\min\left(1,\frac{B_{s,N}^2}{e\tau}\right)
+(q-s)e^{-\tau/B_{s,N}^2}.
}
\tag{77}
$$

Take

$$
P_R=P_{(K+V_D)^\perp},
\qquad F\mid D.
$$

Then \(P_RV_F=0\), and (77) proves (4).

Moreover,

$$
E=K\oplus P_BV_D\oplus(K+V_D)^\perp
$$

is the actual orthogonal decomposition. Therefore

$$
\boxed{
\begin{aligned}
0\le{}&
\operatorname{Tr}_B
\left(\Lambda e^{-\tau H_F}\mathcal L_N\right)
-\operatorname{Tr}\left(P_{P_BV_D}e^{-\tau H_F}\right)\\
\le{}&
s\min\left(1,\frac{B_{s,N}^2}{e\tau}\right)
+(q-s)e^{-\tau/B_{s,N}^2}.
\end{aligned}}
\tag{78}
$$

At \(\tau=e^{cq}\), the right side is \(e^{-cq+o(q)}\). The original observed late heat is therefore carried by the explicitly specified observed rational sector, up to that absolute error.

For the original one-pole late-heat line, this agrees with the supplied identification

$$
u=-Q_k(0)[y^{-1}],
$$

but (74)–(78) do not require its rank-one singular-line argument. They apply to growing filters and complete slow subspaces. The original observation and its full heat receiver remain those in the repository.

The heat in (78) is still the compression of the **full** filtered heat. Its relation to the observed operator’s own heat retains the original memory and leakage terms; those are not removed by locating its slow sector.

---

## 9. Exact source-complex and proper-source returns

The comparison (1) proves

$$
K\cap V_D=0.
$$

Thus the original two-term complex has the quotient map

$$
[E\xrightarrow{\Lambda}B]
\longrightarrow
[E/V_D\xrightarrow{\bar\Lambda_D}B/\Lambda V_D].
$$

Its actual contracting homotopy is

$$
\boxed{
h_D
=
U_D(H_D^B)^{-1}(\Lambda U_D)^*Q_{B,N}(\alpha).
}
\tag{79}
$$

It satisfies

$$
h_D\Lambda U_D=U_D,
$$

and

$$
\Lambda h_D
$$

is the original-metric orthogonal projection onto \(\Lambda V_D\).

Using the full minimum sections of the two quotient maps gives chain maps \(p,j\) with

$$
\boxed{
I-jp=dh_D+h_Dd,
\qquad
\|h_D\|\le e^{E_{k,d}}.
}
\tag{80}
$$

The projection \(h_D\Lambda\) on \(E\) is generally oblique. Its role in (80) is not replaced by \(P_{V_D}\).

For the independent proper-source pair, retain its actual matrices on the original \(Z_R\) values,

$$
Q_N^p,\qquad
H_N^p=A_N-B_N^*C_N^{-1}B_N.
$$

The full target \(J\)-minimum remains in the second matrix.

Choose a rational reference sector of the same rank in the proved domain. On those specified coefficient coordinates,

$$
\boxed{
\begin{aligned}
\mathcal M^p
={}&
\mathcal R\left[
\log\frac{\det H_N^p}{\det H_{D,N}^{B}(\alpha)}
-
\log\frac{\det Q_N^p}{\det H_{D,N}^{E}(\alpha)}
\right]\\
&-\mathcal R\,\delta_D(\alpha).
\end{aligned}}
\tag{81}
$$

The last term is \(o(kq)\) in the range (54), uniformly in activation and moving poles.

Equation (81) does not assign values to the two remaining native comparisons. It shows that their common rational reference is now stable under pole motion, confluence, and every physical source activation. The scalar critical-activation contribution occurs on both sides and cancels through the displayed identity.

---

# Resulting control

The moving rational sector now has:

1. **A uniform original-metric comparison** over all pole multisets in a compact arithmetic resolvent region, including repeated and translated-colliding poles.
2. **The same evaluated critical-activation determinant coefficient** as the original inverse-power sector, with a complete finite error.
3. **A global polynomial sector frame at arithmetic pole collisions**, with the resultant, full multiplication kernel, and metric factor explicitly retained.
4. **An exact quotient system under polynomial filters**, including the complete original observation feedback.
5. **A uniform low-spectrum and late-heat theorem** for the full original filtered operator, with no assumed singular gap beyond the displayed spectral threshold.
6. **An \(o(kq)\)-accurate return through the original kernel and proper-source comparison**, without replacing their native metrics.

The bounds are uniform in pole position and collision inside the stated compact set. They are not uniform across a point of the arithmetic spectrum by suppressing the resultant; §6 gives the exact boundary calculation instead. Likewise, changing the original period can change the conductor’s first nonzero moment. The formulas retain that moment and the actual source constants; they are not replaced by a period-independent positive number without a proved parameter margin.

The original finer kernel coefficient, the two native comparisons in (81), and the signed projected-current value remain unevaluated here. What has been removed is a substantial source of uncontrolled variation around those values: **the reference family can now move, conflate, activate, and pass through the complete filtered action without losing its degree, multiplicity, quotient maps, or quantitative error control.**

No new numerical xi-packet evaluation or machine-verification receipt is claimed for this continuation. The results above are analytic derivations from the stated original finite-form inputs and the supplied harmonic-activation theorem.
