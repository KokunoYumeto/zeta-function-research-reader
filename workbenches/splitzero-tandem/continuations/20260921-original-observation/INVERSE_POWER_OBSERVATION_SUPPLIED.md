## The original observation preserves an entire inverse-power determinant at the \(kq\) scale

Retain the simple-quartet domain

$$
0<\delta<\frac12,\qquad \gamma>2,\qquad k\equiv1\pmod4,
\qquad q=(k+1)^2,
$$

the complete polynomial

$$
Q_k(y)=
\prod_{a,b=0}^{k}
\bigl[y-(2b-k)\gamma+i(2a-k)\delta\bigr],
$$

and multiplication \(M_k[P]=[yP]\) on \(E_k=\mathbb C[y]/(Q_k)\).

At each original cutoff \(q-1\le N\le2q\), let \(G_N\) be the attained metric of the original source \(w_h^{*k}\). Let

$$
\Lambda_k:E_k\longrightarrow B_k,\qquad
Q_{B,N}=(\Lambda_kG_N^{-1}\Lambda_k^*)^{-1},
$$

be the unchanged observation and its full minimum metric, and put

$$
P_{B,N}=G_N^{-1}\Lambda_k^*Q_{B,N}\Lambda_k.
$$

For \(1\le r\le q\), define the literal inverse-power frame

$$
U_r d=\sum_{j=1}^{r}d_j[y^{-j}],
$$

and its two Grams

$$
H^E_{r,N}=U_r^*G_NU_r,\qquad
H^B_{r,N}=U_r^*\Lambda_k^*Q_{B,N}\Lambda_kU_r.
\tag{1}
$$

These are the powers of the original \(M_k^{-1}\), subsequently observed. They are not inverse powers of an independently compressed observed operator.

The current conductor theorem proves finite injectivity on these spaces, but its displayed metric lower bound can involve the full root-value metric condition number. The following calculation replaces that factor on the specified inverse-power space. The exact conductor and kernel inclusion used here are IK1–IK12 at the inspected commit `fe22dc1dd51c633e82f93b731cbb6ec96b11ed64`.

**Theorem.** Fix the original period and its nonzero conductor coefficients. Let \(J\) be their number. Suppose

$$
r=r(k)\ge1,\qquad r\log(q+2)=o(q).
$$

Then, uniformly over the original cutoff window,

$$
\boxed{
e^{-C_{h,A}(k+Jr)\log(q+Jr+2)}H^E_{r,N}
\preceq H^B_{r,N}\preceq H^E_{r,N}.
}
\tag{2}
$$

In particular,

$$
\boxed{
0\le
\log\det H^E_{r,N}-\log\det H^B_{r,N}
\le
C_{h,A}\,r(k+Jr)\log(q+Jr+2).
}
\tag{3}
$$

A finite, explicitly specified lower factor replacing the exponential in (2) is derived below. The finite estimate uses the original polynomial-norm comparison, but **does not use the monic-profile asymptotic or the equilibrium zero law**.

For the evaluated determinant limit, retain those two additional inputs, exactly as in the supplied smallest-singular-value proof. Then, with

$$
\mathcal R F_N=F_{q-1}+F_q-F_{2q-1}-F_{2q},
$$

one obtains

$$
\boxed{
\lim_{k\to\infty}\frac{1}{rq}\mathcal R\log\det H^B_{r,N}
=
\lim_{k\to\infty}\frac{1}{rq}\mathcal R\log\det H^E_{r,N}
=
\mathfrak C,
}
\tag{4}
$$

where

$$
\boxed{
\mathfrak C
=
4\left[\psi(0)-\psi(1)-J(1)-1\right].
}
\tag{5}
$$

Here \(\psi\) and \(J\) retain the definitions in the preceding proof:

$$
\psi(0)=\log(4/\pi),\qquad
J(s)=(1+s)[\log(1+s)-1]
-\frac{s}{2}\int\log x\,\rho_s(x)\,dx.
$$

The supplied interval certificate therefore gives

$$
\boxed{
\frac{1353893}{10^6}<\mathfrak C<
\frac{1354751}{10^6}.
}
\tag{6}
$$

This enclosure is inherited from that certificate, not a new numerical run.  

Taking \(r=k\) in particular evaluates the requested growing-rank scale:

$$
\boxed{
\mathcal R\log\det
\bigl(U_k^*\Lambda_k^*Q_{B,N}\Lambda_kU_k\bigr)
=
\mathfrak C\,kq+o_h(kq).
}
\tag{7}
$$

The full original kernel has not been replaced. Its additional constraints enter through the actual \(P_{B,N}\); the estimate below holds for every vector in this fixed inverse-power space.

---

## 1. The conductor comparison is between the actual value maps

Write

$$
k_-=k-8,\qquad q_-=(k-7)^2,\qquad
\Delta=q-q_-=16k-48,
$$

and let \(Q_-=Q_{k-8}\), in its own centred \(y\)-coordinate.

For the nonzero original coefficients \(a_j\), retain

$$
b_j=4+(2r_j-8)\delta+i(2s_j-8)\gamma,
\qquad
\zeta_j=i(b_j-4).
$$

Thus

$$
|\zeta_j|\le8\sqrt{\delta^2+\gamma^2},
\qquad
|\zeta_i-\zeta_j|\ge2\delta\quad(i\ne j).
$$

The two physical centres are

$$
c=k/2,\qquad c'=c-4.
$$

For \(\Psi_cf(S)=f((S-c)/i)\), direct substitution gives

$$
\boxed{
\Psi_{c'}^{-1}\mathcal T_A\Psi_cf(y)
=
\sum_j a_jf(y-\zeta_j).
}
\tag{8}
$$

In particular, the \(i^n\) in the original \(S\)-coordinate inverse powers cancels through the displayed coordinate map, not by deleting a phase.

Let \(v=\operatorname{ord}_0E_A\). The centred symbol is

$$
e^{-4z/i}E_A(z/i),
$$

so its first nonzero derivative is \(i^{-v}\mu_v\). The operator in (8) lowers degree by exactly \(v\), with leading coefficient

$$
i^{-v}\mu_v\binom nv
$$

on a monic degree-\(n\) polynomial.

Denote its induced quotient map by \(C_A\). The exact source identities are

$$
J_-\mathcal T_A=C_AJ_N,
\qquad
K_k:=\ker\Lambda_k\subseteq\ker C_A.
\tag{9}
$$

Equivalently, there is a well-defined map

$$
\widehat C_A:B_k\longrightarrow \mathbb C[y]/(Q_-),
\qquad
\widehat C_A(\Lambda_k[p])=[\mathcal T_Ap]_{Q_-}.
$$

These are the original conductor identities; no equality between the full observation kernel and the conductor kernel is assumed.

For any quotient class \(f\), write

$$
\|f\|_{\sigma,Q,L}
=
\min_{\substack{p\in\mathcal P_L\\p=f\pmod Q}}\|p\|_\sigma.
$$

When \(f\) is rational with denominator coprime to \(Q\), this denotes its polynomial quotient class. **No rational function is integrated across its poles.**

The original native comparison is

$$
\ell_{k,N}\|p\|_\sigma^2
\le\|p\|_{\mu_k}^2
\le u_k\|p\|_\sigma^2,
\qquad
\log(u_k/\ell_{k,N})=O_h(k+\log(N+1)).
\tag{10}
$$

Its full-mass constants are the retained NG2 constants.

A useful explicit forward bound for (8) is

$$
\boxed{
\|\mathcal T_A\|_{\sigma,\mathcal P_N\to\mathcal P_{N-v}}
\le
\mathcal F_N
:=
A_1e^{1+2\pi\gamma}(N+1)(2N+1)^{4\delta+1/2},
\qquad A_1=\sum_j|a_j|.
}
\tag{11}
$$

It follows from the unchanged Gamma generating function

$$
\sum_{n\ge0}\frac{p_n(y)}{n!}t^n
=(1+t^2)^{-1/4}e^{y\arctan t}.
$$

Translation multiplies it by \(e^{-\zeta_j\arctan t}\). On \(|t|=N/(N+1)\),

$$
|\Re\arctan t|<\pi/4,\qquad
|\Im\arctan t|\le\tfrac12\log(2N+1).
$$

Cauchy’s coefficient bound costs at most \(e\), and the original orthonormal coefficient ratio is at most \(\sqrt{2N+1}\). Summing the \(N+1\) diagonals and all \(a_j\) proves (11). The generating-function convention is DLMF 18.23.7. ([DLMF][1])

Now minimize over the **same original observed fibre**. Every admissible native representative \(p\) has

$$
C_A[p]=C_Af.
$$

Consequently,

$$
\boxed{
\|P_{B,N}f\|_{G_N}
\ge
\frac{\sqrt{\ell_{k,N}}}{\mathcal F_N}
\|C_Af\|_{\sigma,Q_-,N-v},
}
\tag{12}
$$

whereas

$$
\boxed{
\|f\|_{G_N}
\le\sqrt{u_k}\|f\|_{\sigma,Q_k,N}.
}
\tag{13}
$$

The rest of the proof compares the two polynomial minima in (12)–(13) **before estimating their common exponentially large factor**.

## 2. Finite control of the reference relation kernels

For a polynomial \(Q\), let

$$
\mathsf K_{Q,n}(z,w)
=
\sum_{j=0}^{n}\phi_j^{(Q)}(z)
\overline{\phi_j^{(Q)}(w)}
$$

be the reproducing kernel for degree at most \(n\) in

$$
|Q(y)|^2d\sigma(y).
$$

The measure is not divided by its mass.

Set

$$
b_L=\sqrt{2L+1}\sum_{j=1}^{L}\frac1j,\qquad b_0=0.
$$

The Gamma derivative formula gives

$$
\|\partial_y\|_{\mathcal P_L,\sigma}\le b_L.
$$

Pairing

$$
[\partial_y,y-z]p=p
$$

with \(p\), and retaining the adjoint multiplication by \(y-\bar z\), yields

$$
\boxed{
\frac{\|p\|_\sigma}{2b_{L+1}}
\le\|(y-z)p\|_\sigma
\le[2(L+1)+|z|]\|p\|_\sigma.
}
\tag{14}
$$

These are the full-polynomial bounds CG9–CG11 in the current source.

For anchored division

$$
\mathscr Dp=\frac{p-p(0)}y,
$$

the original evaluation kernel at zero gives

$$
\boxed{
\|\mathscr D\|_{\mathcal P_L,\sigma}
\le
\mathfrak d_L:=2b_L(1+\sqrt{L+1}).
}
\tag{15}
$$

### A hard gap allowing twice the relation degree

Let \(Q\) be monic of degree \(d\ge16\), with all roots in

$$
|z|\le2^{-13}d.
$$

Then, for every polynomial \(p\) of degree at most \(2d\),

$$
\boxed{
\int y^2|Qp|^2\,d\sigma
\ge\beta_d\int|Qp|^2\,d\sigma,
\qquad
\beta_d=2^{-27}d^2.
}
\tag{16}
$$

Here is a finite proof. Put \(c_*=2^{-13}\) and

$$
c_\sigma=\frac{\Gamma(1/4)^2}{2\pi}.
$$

Euler’s product gives

$$
\frac{c_\sigma e^{-\pi|y|/2}}{1+4y^2}
\le\sigma(y)\le c_\sigma.
\tag{17}
$$

The product and its convention are those of DLMF §5.8. ([DLMF][2])

On \(|y|\le c_*d\),

$$
|Q(y)|\le(2c_*d)^d;
$$

on \([d,2d]\),

$$
|Q(y)|\ge(d/2)^d.
$$

The Legendre evaluation estimate on \([1,2]\) gives, for \(\deg p\le2d\),

$$
\sup_{|y|\le c_*d}|p(y)|^2
\le
\frac{(2d+1)^2\,10^{4d}}{d}
\int_d^{2d}|p(u)|^2\,du.
$$

Therefore the ratio of the inner mass to the mass on \([d,2d]\) is at most

$$
2c_*(1+16d^2)(2d+1)^2
\left(16c_*^2\,10^4e^\pi\right)^d.
$$

Using \(\pi<4\) and \(e<3\), the factor in parentheses is below \(1/4\). Thus the ratio is bounded by

$$
\frac{(1+16d^2)(2d+1)^2}{4096\,4^d}\le1.
$$

At least half the full mass lies outside \(|y|\le c_*d\), proving (16).

### Kernel consequences

Assume now that \(|Q|^2d\sigma\) is even. Within the degree range just established,

$$
\boxed{
\mathsf K_{Q,n}(z,z)
\le
e^{nR^2/\beta_d}
\left(1+\frac{R^2}{\beta_d}\right)
\mathsf K_{Q,n}(0,0),
\qquad |z|\le R.
}
\tag{18}
$$

Indeed every nonzero squared zero of the relevant even or odd orthogonal polynomial is at least \(\beta_d\). For even degrees, factor the polynomial into its paired zeros and use \(1+x\le e^x\). For odd degrees, write the polynomial as \(y\) times an orthogonal polynomial for the \(x\)-weighted pushforward measure. Equation (16) compares that whole weighted Gram with \(\beta_d\) times the unweighted one. Summing the even and odd evaluations gives (18). The reproducing-kernel and parity identities used here have the standard conventions of DLMF §18.2. ([DLMF][3])

For even \(n\), define the exact minimum polynomial

$$
H_{Q,n}(y)=
\frac{\mathsf K_{Q,n}(y,0)}{\mathsf K_{Q,n}(0,0)}.
$$

It satisfies

$$
H_{Q,n}(0)=1,\qquad
\|QH_{Q,n}\|_\sigma^2=\mathsf K_{Q,n}(0,0)^{-1},
$$

and, when \(R^2\le\beta_d/2\),

$$
\boxed{
|H_{Q,n}(z)|\ge e^{-nR^2/\beta_d},
\qquad |z|\le R.
}
\tag{19}
$$

To see the zero structure exactly, \(yH_{Q,n}\) is a scalar multiple of the original odd monic polynomial of degree \(n+1\). Its nonzero zeros obey (16).

One also needs to compare nearby kernel degrees. If all roots of \(Q\) have imaginary part of modulus at least \(\delta\), then

$$
\|p'\|_{|Q|^2\sigma}
\le
\left(b_{d+n+1}+\frac d\delta\right)
\|p\|_{|Q|^2\sigma}.
$$

The first term differentiates \(Qp\); the second uses

$$
|Q'(y)/Q(y)|\le d/\delta
$$

on the real line.

Put

$$
V=b_{d+n+1}+d/\delta,\qquad U=2(d+n+2).
$$

The monic recurrence coefficients obey \(a_j\ge j/V\) and \(a_j\le U\). Therefore, for even \(n_0\le n\), with \(h=\lfloor n/2\rfloor-n_0/2\),

$$
\boxed{
\mathsf K_{Q,n}(0,0)
\le
\mathcal D_{d;n_0,n}\,\mathsf K_{Q,n_0}(0,0),
}
\tag{20}
$$

where the entirely finite factor is

$$
\boxed{
\mathcal D_{d;n_0,n}
=
\prod_{t=1}^{h}
\left[
1+\left(\frac{UV}{n_0+2t}\right)^2
\right].
}
\tag{21}
$$

This follows from the exact even evaluation recurrence

$$
\phi_{j+2}(0)
=-\frac{a_{j+1}}{a_{j+2}}\phi_j(0).
$$

## 3. A uniform norm comparison for every inverse-power coefficient vector

Put

$$
n_0=2\left\lfloor\frac{N+1-q}{2}\right\rfloor,
\qquad
T_N=
\frac1{|Q_k(0)|\sqrt{\mathsf K_{Q_k,n_0}(0,0)}}.
\tag{22}
$$

This is the common large factor.

### The source upper bound

Let

$$
A_d(y)=\sum_{j=1}^{r}d_jy^{r-j},
\qquad
H=H_{Q_k,n_0}.
$$

In the formal Taylor ring at zero, define

$$
h(y)=
-H(y)\operatorname{rem}_{y^r}
\frac{A_d(y)}{Q_k(y)H(y)}.
$$

Then

$$
p(y)=\frac{A_d(y)+Q_k(y)h(y)}{y^r}
$$

is a polynomial of degree at most \(N\), and

$$
[p]_{Q_k}=U_rd.
$$

This is a representative in the original polynomial source.

Take \(\rho=\delta/2\), and choose one root from each pair \(\{\omega,-\omega\}\) of \(Q_k\). Define

$$
\mathcal Q_\rho
=
\prod_{\omega/\pm}
\left(1-\frac{\rho^2}{|\omega|^2}\right)^{-1}.
$$

On \(|y|=\rho\),

$$
|Q_k(0)/Q_k(y)|\le\mathcal Q_\rho.
$$

Moreover,

$$
\log\mathcal Q_\rho
\le
\frac{4\rho^2}{\delta^2}
\sum_{\substack{1\le j\le k\\j\ {\rm odd}}}\frac1j
=O(\log k).
\tag{23}
$$

Cauchy’s coefficient estimate, (19), repeated multiplication by \(y\), and (15) now give

$$
\boxed{
\|U_rd\|_{\sigma,Q_k,N}
\le \mathcal U_{r,N}T_N\|d\|_2,
}
\tag{24}
$$

with

$$
\boxed{
\mathcal U_{r,N}
=
\mathfrak d_{N+r}^{\,r}
\frac{\mathcal Q_\rho e^{n_0\rho^2/\beta_q}}
{\sqrt{1-\rho^2}}
\sum_{j=0}^{r-1}
\left(\frac{2(N+r+1)}{\rho}\right)^j.
}
\tag{25}
$$

The cancellation at zero is exact:

$$
p=\mathscr D^r(Q_kh).
$$

Thus (24) never integrates \(y^{-r}\).

### The conductor lower bound retains every pole

In the centred lower coordinate,

$$
C_AU_rd
=
\left[
R_d(y)
\right]_{Q_-},
\qquad
R_d(y)=
\sum_{j=1}^{J}\sum_{n=1}^{r}
\frac{a_jd_n}{(y-\zeta_j)^n}.
\tag{26}
$$

Put

$$
B(y)=\prod_{j=1}^{J}(y-\zeta_j)^r,
\qquad
A_d^-(y)=B(y)R_d(y).
$$

If \(p\) is any degree-\((N-v)\) representative of this lower quotient class, then

$$
Bp-A_d^-=Q_-h,
\qquad
\deg h\le n_-:=N-v+Jr-q_-.
\tag{27}
$$

Fix one actual nonzero coefficient \(a_*\), at its actual pole \(\zeta_*\), and let

$$
B_*(y)=\prod_{j\ne *}(y-\zeta_j)^r.
$$

The full divided jet of (27) at that pole is

$$
\boxed{
\operatorname{jet}_{\zeta_*,<r}
\left(\frac{Q_-h}{B_*}\right)
=
-a_*\,(d_r,d_{r-1},\ldots,d_1).
}
\tag{28}
$$

All other rational summands are analytic at \(\zeta_*\) and become divisible by \((y-\zeta_*)^r\). This is why their interference cannot erase the coefficient vector in (28).

Here are finite constants for the resulting estimate. For \(m_0=r(J-1)\), define

$$
t_j^{(m_0)}=
\begin{cases}
\displaystyle
\binom{m_0+j-1}{j}(2\delta)^{-m_0-j},&m_0>0,\\
1,&m_0=0,\ j=0,\\
0,&m_0=0,\ j>0,
\end{cases}
$$

and

$$
\mathcal P
=
\sum_{j=0}^{r-1}\sum_{\ell=0}^{j}
\binom{q_-}{\ell}\delta^{-\ell}
t_{j-\ell}^{(m_0)}.
\tag{29}
$$

This bounds the full triangular multiplication on the jet in (28), after retaining \(|Q_-(\zeta_*)|\).

Equation (18) and Cauchy’s formula give

$$
\mathcal E
=
\sqrt r\,\rho^{1-r}
e^{n_-(|\zeta_*|+\rho)^2/(2\beta_{q_-})}
\sqrt{1+\frac{(|\zeta_*|+\rho)^2}{\beta_{q_-}}},
\qquad
\mathcal L=\frac{|a_*|}{\mathcal P\mathcal E}.
\tag{30}
$$

Therefore

$$
\|Q_-h\|_\sigma
\ge
\frac{\mathcal L\|d\|_2}
{|Q_-(\zeta_*)|
 \sqrt{\mathsf K_{Q_-,n_-}(0,0)}}.
\tag{31}
$$

Let \(Z=\max_j|\zeta_j|\), and put

$$
\mathcal B=2(N-v+Jr+1)+Z,
$$

$$
\mathcal A
=
\sqrt{\mathfrak m_\sigma}\,A_1\sqrt r
[2(Jr+1)+Z]^{Jr-1},
\qquad \mathfrak m_\sigma=\sqrt{2\pi}.
$$

The complete numerator satisfies

$$
\|A_d^-\|_\sigma\le\mathcal A\|d\|_2,
\qquad
\|Bp\|_\sigma\le\mathcal B^{Jr}\|p\|_\sigma.
$$

Thus (27)–(31) give a lower bound on the complete polynomial minimum, not on one selected representative.

### Compare the two relation kernels before bounding their size

The central lower grid is an exact subset of the upper grid:

$$
Q_k=Q_-D_{\partial},\qquad \deg D_\partial=\Delta.
$$

Set

$$
\mathcal W=2(q+n_0+1)+k\sqrt{\delta^2+\gamma^2},
$$

and

$$
\boxed{
\mathcal R_*=
\frac{|Q_k(0)|}
{|Q_-(\zeta_*)|\,
 \mathcal W^\Delta
 \sqrt{\mathcal D_{q_-;n_0,n_-}}}.
}
\tag{32}
$$

Repeated application of the full multiplication bound (14), followed by (20), proves

$$
\frac1{|Q_-(\zeta_*)|
\sqrt{\mathsf K_{Q_-,n_-}(0,0)}}
\ge \mathcal R_*T_N.
\tag{33}
$$

Every removed root remains in (32). For the size estimate, the removed grid consists of the four outer odd shells, so

$$
|D_\partial(0)|\ge[\delta(k-6)]^\Delta.
$$

Also, pairing the lower roots gives

$$
\left|\frac{Q_-(\zeta_*)}{Q_-(0)}\right|
\le
\exp\left[
\frac{2|\zeta_*|^2}{\delta^2}
\sum_{\substack{1\le j\le k-8\\j\ {\rm odd}}}\frac1j
\right].
$$

Together with (21),

$$
\log^+(1/\mathcal R_*)
=
O_A((k+Jr)\log(q+Jr+2)).
\tag{34}
$$

The large factor \(T_N\) has a fully explicit lower bound. Put

$$
R_k=k\sqrt{\delta^2+\gamma^2}.
$$

Evaluation on \([q,2q]\), with all Gamma and polynomial factors retained, yields

$$
\boxed{
T_N\ge T_N^{\rm lb}:=
\frac{
\sqrt{c_\sigma q/(1+16q^2)}\,
(q-R_k)^q e^{-\pi q/2}
}{
|Q_k(0)|(n_0+1)10^{n_0}
}.
}
\tag{35}
$$

A sufficient finite domain is

$$
q_-\ge16,\qquad
R_k\le2^{-14}q_-,
\qquad
n_-+2\le2q_-,
$$

together with

$$
\boxed{\mathcal L\mathcal R_*T_N^{\rm lb}\ge2\mathcal A.}
\tag{36}
$$

All quantities in these guards are specified above or are the original conductor coefficients.

On that domain, (27)–(36) prove

$$
\boxed{
\|C_AU_rd\|_{\sigma,Q_-,N-v}
\ge
\frac{\mathcal L\mathcal R_*}
{2\mathcal B^{Jr}}T_N\|d\|_2.
}
\tag{37}
$$

Combining (12), (13), (24), and (37) gives the promised finite observation factor:

$$
\boxed{
\frac{\|P_{B,N}U_rd\|_{G_N}^2}
{\|U_rd\|_{G_N}^2}
\ge
\frac{\ell_{k,N}}{u_k}
\left[
\frac{\mathcal L\mathcal R_*}
{2\mathcal F_N\mathcal B^{Jr}\mathcal U_{r,N}}
\right]^2.
}
\tag{38}
$$

For \(r\log(q+2)=o(q)\), every logarithmic factor on the right costs

$$
O_{h,A}((k+Jr)\log(q+Jr+2)).
$$

Meanwhile

$$
\log T_N^{\rm lb}
\ge q\log(q/k)-O_h(q).
$$

Consequently the finite guard (36) eventually holds, and (38) proves (2)–(3).

The pole argument itself permits repeated roots. For another packet, however, the full-jet conductor factorization, nested polynomial comparison, and actual kernel inclusion must be retained for that packet; they are not inferred from its reduced root set.

## 4. Evaluation of the determinant coefficient

The preceding bounds give, for both \(H^E_{r,N}\) and \(H^B_{r,N}\),

$$
\log\det H_{r,N}
=
r\log u_k
-2r\log|Q_k(0)|
-r\log\mathsf K_{Q_k,n_0}(0,0)
+
O_{h,A}\!\left(r(k+Jr)\log(q+Jr+2)\right).
\tag{39}
$$

At the four original cutoffs, \(n_0\) is exactly

$$
0,\ 0,\ q,\ q.
$$

The common source factor \(u_k\) and the full root product \(Q_k(0)\) therefore cancel under the prescribed signs:

$$
\boxed{
\mathcal R\log\det H_{r,N}
=
2r\log
\frac{\mathsf K_{Q_k,q}(0,0)}
     {\mathsf K_{Q_k,0}(0,0)}
+o_{h,A}(rq).
}
\tag{40}
$$

It remains to evaluate one reference-kernel ratio.

Let \(U_n^\Gamma\) be the monic polynomials for \(Q_k^2d\sigma\), with squared norms \(\nu_n^\Gamma\). Christoffel–Darboux at zero gives

$$
\mathsf K_{Q_k,q}(0,0)
=
\frac{U_{q+1}^{\Gamma\,\prime}(0)U_q^\Gamma(0)}
{\nu_q^\Gamma}.
$$

The ratio

$$
\Xi_q=
\frac{U_{q+1}^{\Gamma\,\prime}(0)}{U_q^\Gamma(0)}
$$

satisfies

$$
1\le\Xi_q\le
\frac{4(2q+1)^2}{\beta_q}.
\tag{41}
$$

Indeed, after \(x=y^2\), the numerator and denominator are the values at zero of monic polynomials for \(x\,d\lambda\) and \(d\lambda\). Their zeros interlace in the positive interval supplied by (16). The product of their zero ratios is bounded by the largest zero divided by the smallest. Thus \(\log\Xi_q=O(1)\).

Since

$$
\mathsf K_{Q_k,0}(0,0)=1/\nu_0^\Gamma,
$$

we have the exact identity

$$
\boxed{
\log\frac{\mathsf K_{Q_k,q}(0,0)}
{\mathsf K_{Q_k,0}(0,0)}
=
2\log|U_q^\Gamma(0)|
+\log\nu_0^\Gamma-\log\nu_q^\Gamma+\log\Xi_q.
}
\tag{42}
$$

The original native/Gamma comparison passes to both complete monic affine minima. Hence the supplied H4 profile implies the same ratio estimate in the Gamma reference:

$$
\log\frac{\nu_j^\Gamma}{\omega_{q+j}^\Gamma}
=
2q\psi(j/q)+O_h(k\log^2(q+2)).
\tag{43}
$$

This is the precise use of the imported monic-profile input. 

The full reference zero law, now applicable to the logarithm because of (16), gives

$$
\log|U_q^\Gamma(0)|
=
q\log q+\frac q2\int\log x\,\rho_1(x)\,dx+o_h(q).
$$

This is the same reference logarithmic limit used in the supplied proof. 

Finally,

$$
\omega_n^\Gamma=\sqrt{2\pi}\,n!(1/2)_n
$$

gives

$$
\log\omega_{2q}^\Gamma-\log\omega_q^\Gamma
=
2q\log q+4q\log2-2q+O(\log q).
$$

Substitute into (42):

$$
\boxed{
\frac1q\log
\frac{\mathsf K_{Q_k,q}(0,0)}
{\mathsf K_{Q_k,0}(0,0)}
\longrightarrow
2[\psi(0)-\psi(1)-J(1)-1].
}
\tag{44}
$$

Equations (40) and (44) prove (4)–(7).

The estimate is on every vector in the inverse-power frame. The determinant conclusion is not inferred from a full-space volume comparison.

## 5. The actual observed late-heat return has an eventual positive sign

The current source identifies the late-heat line as

$$
u=-Q_k(0)[y^{-1}],
$$

and proves

$$
M_k^{-1}=B_N-\frac{u\varphi_N}{Q_k(0)},
\qquad
\|B_N\|\le D_N,
\qquad
E_N=\frac{\|u\|\|\varphi_N\|}{|Q_k(0)|}.
$$

If \(E_N>2D_N\), its smallest-singular projection \(P_{\min,N}\) satisfies

$$
\|P_{\min,N}-P_{u,N}\|_1
\le2\eta_N,\qquad
\eta_N=\frac{D_N}{E_N-D_N}.
$$

This is the inherited LS1–LS5 line estimate.

Our \(r=1\) bound gives the actual observed fraction

$$
\theta_N=
\frac{\|P_{B,N}u\|_{G_N}^2}{\|u\|_{G_N}^2}
$$

the new quantitative lower bound

$$
\boxed{
e^{-C_{h,A}k\log(q+2)}
\le\theta_N\le1.
}
\tag{45}
$$

In particular,

$$
\boxed{\frac1q\log\theta_N\longrightarrow0.}
\tag{46}
$$

This does not assert that \(\theta_N\) tends to a nonzero constant.

Define the measured full heat

$$
\Theta_N(\tau)
=
\operatorname{Tr}_{B_k}
\left[
\Lambda_k e^{-\tau M_k^{\dagger_{G_N}}M_k}
L_{B,N}
\right],
\qquad
L_{B,N}=G_N^{-1}\Lambda_k^*Q_{B,N}.
\tag{47}
$$

Equivalently,

$$
\Theta_N(\tau)
=
\operatorname{Tr}_{E_k}
\left[P_{B,N}e^{-\tau M_k^\dagger M_k}\right].
$$

This is the original observation of the full heat operator. It is not the heat trace of \(\Lambda_kM_kL_{B,N}\).

Let \(s_{\min,N}\) be the actual smallest singular value. The finite relative error is

$$
\boxed{
\left|
\frac{\Theta_N(\tau)}
{\theta_N e^{-\tau s_{\min,N}^2}}-1
\right|
\le
\frac{2\eta_N}{\theta_N}
+
\frac{q-1}{\theta_N}
e^{-\tau(D_N^{-2}-s_{\min,N}^2)}.
}
\tag{48}
$$

At the late times

$$
\tau_k(b)=\exp\{2q[\log(q/k)+b]\},
$$

both terms tend to zero. The reason is quantitative: the supplied smallest-singular theorem gives

$$
\eta_N=\exp[-q\log(q/k)+O_h(q)],
$$

whereas (45) loses only \(\exp[-O_{h,A}(k\log q)]\). Therefore

$$
\boxed{
\Theta_N(\tau_k(b))
=
\theta_N e^{-\tau_k(b)s_{\min,N}^2}(1+o_h(1)).
}
\tag{49}
$$

The observed line is also determined in relative trace norm. If

$$
\Pi_{\Lambda u,N}
=
\frac{(\Lambda u)(\Lambda u)^*Q_{B,N}}
{(\Lambda u)^*Q_{B,N}(\Lambda u)},
$$

then the measured heat, divided by its own trace, approaches this actual projector. No limiting observation angle is inserted.

For the same physical time used in the supplied four-cutoff theorem,

$$
\boxed{
\tau_k^*
=
\exp\left\{
2q\left[
\log(q/k)-1-\frac{I(\delta,\gamma)}2
\right]
\right\},
}
\tag{50}
$$

the lower two full heat weights tend to one, while the upper two are doubly exponentially small. The source’s endpoint inequalities are

$$
\psi(1)+J(1)<-1<\psi(0)+J(0).
$$

They are retained without modification. 

Since the observed lower weights are bounded below by (45),

$$
\boxed{
\mathcal R\Theta_N(\tau_k^*)>0
\quad\text{for all sufficiently large }k,
}
\tag{51}
$$

and more precisely

$$
\boxed{
\frac1q\log\bigl(\mathcal R\Theta_N(\tau_k^*)\bigr)
\longrightarrow0.
}
\tag{52}
$$

The limit of the unscaled signed trace is not assigned the value \(2\): its retained fractions \(\theta_N\) may still decay. What is established is its eventual sign and its complete leading exponential rate.

## 6. The same logarithmic rate holds for every conductor-detected eigenclass

There is a second application that does not require summing over projections.

For an upper root \(\lambda\), let

$$
e_\lambda(y)=
\frac{Q_k(y)}{(y-\lambda)Q_k'(\lambda)}
$$

be the actual cardinal eigenclass. Put

$$
\mathcal J_\lambda=
\{j:\mu_j:=\lambda+\zeta_j
\text{ is a lower root}\}.
$$

Then

$$
C_Ae_\lambda(\mu_j)=a_j,
$$

and the other lower values vanish. Thus

$$
C_Ae_\lambda\ne0
\iff\mathcal J_\lambda\ne\varnothing.
\tag{53}
$$

The different \(j\)'s give different lower roots, so these values do not cancel.

Define

$$
B_\lambda(y)=\prod_{j\in\mathcal J_\lambda}(y-\mu_j),
\qquad
Q_\lambda=\frac{Q_k}{y-\lambda},
\qquad
Q_{\mathrm{rest}}=\frac{Q_-}{B_\lambda},
$$

$$
n_a=N+1-q,\qquad
n_\lambda=N-v-q_-+|\mathcal J_\lambda|.
$$

The complete source minimum is

$$
\|e_\lambda\|_{\sigma,Q_k,N}^2
=
\frac1{|Q_k'(\lambda)|^2
\mathsf K_{Q_\lambda,n_a}(\lambda,\lambda)}.
$$

At any chosen \(j_*\in\mathcal J_\lambda\), the conductor image satisfies the finite lower bound obtained by retaining its exact value at \(\mu=\mu_{j_*}\). Therefore

$$
\boxed{
\begin{aligned}
\frac{\|P_{B,N}e_\lambda\|_{G_N}^2}
{\|e_\lambda\|_{G_N}^2}
\ge{}&
\frac{\ell_{k,N}}{u_k\mathcal F_N^2}\\
&\times
\frac{
|a_{j_*}|^2|B_\lambda'(\mu)|^2
|Q_k'(\lambda)|^2
\mathsf K_{Q_\lambda,n_a}(\lambda,\lambda)
}{
|Q_-'(\mu)|^2
\mathsf K_{Q_{\mathrm{rest}},n_\lambda}(\mu,\mu)
}.
\end{aligned}
}
\tag{54}
$$

Every kernel in (54) is a finite Gamma-polynomial kernel with its specified full factor. No native midpoint Gram is used.

To estimate the ratio, use

$$
Q_k(y)=Q_-(y+\zeta_{j_*})D_{j_*}(y),
\qquad
\frac{|Q_k'(\lambda)|}{|Q_-'(\mu)|}
=|D_{j_*}(\lambda)|
\ge(2\delta)^\Delta,
$$

and

$$
|B_\lambda'(\mu)|\ge(2\delta)^{|\mathcal J_\lambda|-1}.
$$

Multiplication bounds compare \(Q_\lambda\) and \(Q_{\mathrm{rest}}\) with the complete even polynomials; (18)–(21) compare their evaluation kernels. Since \(|\lambda|,|\mu|\le R_k=O_h(k)\) and \(\beta_q\asymp q^2\), the complex-point kernel factors cost only bounded or polynomial factors. This proves

$$
\boxed{
\frac{\|P_{B,N}e_\lambda\|_{G_N}^2}
{\|e_\lambda\|_{G_N}^2}
\ge e^{-C_{h,A}k\log(q+2)}
}
\tag{55}
$$

uniformly over all \(\lambda\) satisfying (53).

For any one nonzero conductor coefficient, its translated lower grid already contains \(q_-\) upper roots. Thus (55) applies to at least \(q_-\) of the \(q\) original eigenlines. It is an individual-line statement; it does not assert the same bound for arbitrary combinations of all those eigenvectors.

Finally, the cofactor minimum and the same kernel estimates give

$$
\log\|e_\lambda\|_{G_N}^2
=
\log u_k-2\log|Q_k'(\lambda)|
-\log\mathsf K_{Q_k,n_0}(0,0)
+O_h(k+\log q),
$$

uniformly over the full upper grid. The derivative factor is independent of \(N\). Consequently every conductor-detected eigenclass has the evaluated observed return

$$
\boxed{
\frac1q\mathcal R
\log\|P_{B,N}e_\lambda\|_{G_N}^2
\longrightarrow\mathfrak C.
}
\tag{56}
$$

Any original nonzero physical scalar attached to that eigenline cancels under the same four signs. For a terminal corner, the sufficient conductor condition is its actual corresponding corner coefficient being nonzero; a zero coefficient is not replaced by a generic one.

---

The matrices evaluated here are the original observed inverse-power Grams (1) and the original observed eigenclass norms. Their \(kq\)- and \(q\)-scale coefficients are now explicit. They are not reidentifications of the different invariant-kernel matrix \(I_K^*G_NI_K\), nor of the independently minimized proper-source target.

The finite estimates are the displayed polynomial, kernel, and pole inequalities. The limiting coefficient and late-time consequences additionally use the named source profile and reference zero law. No new numerical native-moment evaluation or machine-check execution is asserted.

### References

National Institute of Standards and Technology. (n.d.). *Digital Library of Mathematical Functions*. §§5.8, 18.2, and 18.23. The Gamma product, reproducing-kernel conventions, parity transformation, and Meixner–Pollaczek generating function are used as identified above. ([DLMF][2])

*Original-metric heat transitions and complete mixed-family control*. (2026, September 20). [User-supplied research manuscript]. H4–H5 supply the retained monic-norm profile and its stated scope. 

Split-Zero research programme. (2026a, September 21). *The original conductor detects a full inverse-power space* [Research manuscript, IK1–IK12; SZ-20260921-007]. *Zeta-function research reader*, inspected at commit `fe22dc1dd51c633e82f93b731cbb6ec96b11ed64`.

Split-Zero research programme. (2026b, September 21). *Original conductor roots, native singular directions, and complete observation receivers* [Research manuscript, CG9–CG11 and LS1–LS7]. Same repository and inspected commit.

*The unique small singular direction of the native arithmetic quotient*. (2026, September 21). [Supplied predecessor proof, S1–S45]. Its endpoint integral enclosure and late-time theorem are retained as separately identified inputs. 

[1]: https://dlmf.nist.gov/18.23 "https://dlmf.nist.gov/18.23"
[2]: https://dlmf.nist.gov/5.8 "https://dlmf.nist.gov/5.8"
[3]: https://dlmf.nist.gov/18.2 "https://dlmf.nist.gov/18.2"
