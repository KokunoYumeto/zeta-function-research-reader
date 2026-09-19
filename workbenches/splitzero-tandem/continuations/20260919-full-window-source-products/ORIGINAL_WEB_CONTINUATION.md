The calculation now extends from the two low cutoffs to the **complete original window**. It evaluates the weighted products of both source-response energies and the four-cutoff norm return of the retained terminal eigenclass.

Write

$$
H_\rho=\sqrt{\delta^2+\gamma^2},\qquad R=kH_\rho,
$$

and retain the original equilibrium constant

$$
L=\int\log x\,\rho_{2,\pi}(x)\,dx
=\frac{C_\Gamma}{2}+4\log2-2.
$$

With the original weights

$$
w_{q-1}=w_{2q-1}=1,\qquad
w_N=2\quad(q\le N\le2q-2),
$$

the new values are

$$
\boxed{
-\sum_{N=q-1}^{2q-1}w_N\log p_{2,N}
=
2q\log\frac{q}{kH_\rho}+qL
+O_h(k+\log q),
}
\tag{1}
$$

and

$$
\boxed{
-\sum_{N=q-1}^{2q-1}w_N\log p_{1,N}
=
J_k^{\mathrm{action}}
-2q\log(qkH_\rho)-qL
+O_h(k+\log q).
}
\tag{2}
$$

Here \(p_1,p_2\) are the actual three-column source energies, not the observation-kernel energy \(\theta\), native angular exponents, or rank fractions.

The retained class itself satisfies the further evaluated return

$$
\boxed{
\log
\frac{E_{q-1,\lambda}E_{q,\lambda}}
     {E_{2q-1,\lambda}E_{2q,\lambda}}
=
C_\partial q+O_h(k+\log q).
}
\tag{3}
$$

The error \(O_h(k+\log q)\) is \(o_h(q/\log q)\) at every fixed original multiplicity. Thus these formulas determine their order-\(q\) coefficients and permit the already evaluated inverse-logarithmic arithmetic correction to be propagated without losing its precision.

The decisive new step is a cancellation between consecutive Cauchy-transform coefficients. It reduces the complete \(p_2\)-product to one orthogonal-polynomial value. A comparison through **two rank-one quotient metrics**, rather than a comparison of two large determinants separately, then evaluates that value in the actual arithmetic source.

## 1. Exact identities at every cutoff

Retain

$$
e=1+k(m_0-1),\qquad q=e(k+1)^2,\qquad k\equiv1\pmod4,
$$

the complete polynomial

$$
\chi(S)=
\prod_{a,b=0}^{k}
\left[S-\frac{k}{2}-(2a-k)\delta-i(2b-k)\gamma\right]^e,
$$

and

$$
dm(y)=w_h^{*k}(y)\,dy,\qquad S=c+iy,\qquad c=k/2.
$$

Set

$$
\lambda=k\rho=c+d+it,\qquad d=k\delta,\quad t=k\gamma,
\qquad z=t-id.
$$

The terminal class remains

$$
v_\lambda=
\left[
b_\lambda\frac{\chi(S)}{S-\lambda}
\right],
\qquad
b_\lambda=\frac1{\chi_\lambda(\lambda)},
\qquad
\chi_\lambda(S)=\frac{\chi(S)}{(S-\lambda)^e}.
$$

This retains the complete-primary denominator when \(e>1\). The class and its full arithmetic unit are those used in the existing current calculation. 

Put

$$
Q(y)=i^{-q}\chi(c+iy),\qquad dW(y)=Q(y)^2\,dm(y).
$$

Let \(U_j\) be the real monic orthogonal polynomials for \(dW\), with squared norms \(\nu_j\), and define

$$
C_j(z)=\int_{\mathbb R}\frac{U_j(y)}{z-y}\,dW(y).
$$

For \(r\ge0\), define the **actual attained rational residual**

$$
H_r(z)=
\min_{\deg P<r}
\int_{\mathbb R}
\left|\frac1{z-y}-P(y)\right|^2dW(y).
\tag{4}
$$

At the original cutoff \(N=q-1+r\),

$$
E_{N,\lambda}=|b_\lambda|^2H_r(z).
$$

Indeed, multiplication by \(Q\) turns the residual in (4) into the original polynomial minimum representative, with its fixed factor \(-b_\lambda i^{q-1}\). No source or quotient has been substituted.

Write

$$
\Delta_j=\frac{\omega_{q+j}}{\nu_j},
$$

where \(\omega_n\) is the original arithmetic monic source norm. Orthogonal projection gives

$$
H_r-H_{r+1}=\frac{|C_r|^2}{\nu_r}.
$$

Consequently,

$$
\boxed{
p_{2,q-1+r}
=
\frac{H_r-H_{r+1}}{(1-\Delta_r)H_r},
}
\tag{5}
$$

and, for \(r\ge1\),

$$
\boxed{
p_{1,q-1+r}
=
\frac{\Delta_{r-1}}{1-\Delta_{r-1}}
\left(\frac{H_{r-1}}{H_r}-1\right).
}
\tag{6}
$$

These identities include all preceding relations. For example, the minimum representative of \(b_{N+1}\) at cutoff \(N\) is the difference between the source monic polynomial and the complete monic relation of the same degree; its norm is

$$
\nu_r-\omega_{q+r}=\nu_r(1-\Delta_r).
$$

That is the denominator in (5), not a trial-relation norm.

There is a useful finite Wronskian identity:

$$
\boxed{
H_r(z)=
\frac{\operatorname{Im}\!\left(C_r(z)\overline{C_{r-1}(z)}\right)}
     {d\,\nu_{r-1}},
\qquad r\ge1.
}
\tag{7}
$$

To prove it, the monic recurrence gives

$$
C_1=zC_0-\nu_0,\qquad
C_{j+1}=zC_j-\frac{\nu_j}{\nu_{j-1}}C_{j-1}.
$$

Since \(\operatorname{Im}C_0=dH_0\), the formula holds at \(r=1\). Taking imaginary parts of the recurrence proves

$$
\frac{\operatorname{Im}(C_{j+1}\overline C_j)}{d\nu_j}
=
\frac{\operatorname{Im}(C_j\overline C_{j-1})}{d\nu_{j-1}}
-\frac{|C_j|^2}{\nu_j},
$$

which is exactly the residual recursion. No infinite orthogonal expansion or completeness assertion is required.

The standard monic recurrence, real-zero and interlacing facts used here are the usual orthogonal-polynomial results; the new identities apply them to the retained relation measure and class. ([DLMF][1])

## 2. Control the whole window without discarding the central interval

The following comparison is used only as an auxiliary calculation, and its error is returned to the original source.

Choose a fixed sufficiently small \(\epsilon_*>0\), no larger than \(2^{-16}\), with \(\epsilon_*^2\) strictly below the original EIQ support. Put

$$
Y=\epsilon_*q,\qquad D=q+2.
$$

Use the original whole-polynomial comparison through degree \(2q+2\):

$$
\ell_k\|P\|_\sigma^2
\le \|P\|_m^2
\le u_k\|P\|_\sigma^2,
\qquad
\Lambda_k=\log(u_k/\ell_k)=O_h(k+\log q).
\tag{8}
$$

The original CAI estimate is stated for arbitrary finite degree, so this includes the two output degrees needed to calculate the last endpoint. 

A finite central-fraction bound, valid for every polynomial \(P\) of degree at most \(D\), is

$$
\int_{|y|\le Y}|P(y)|^2\,dW(y)
\le\eta_k\int_{\mathbb R}|P(y)|^2\,dW(y),
\tag{9}
$$

where one may take

$$
\boxed{
\eta_k=
\frac{u_k}{\ell_k}
\frac{\sqrt{2\pi}}{c_G}
\frac{(D+1)^2\sqrt{1+2q}}q\,
100^D e^{\pi q}
\left(\frac{Y^2+R^2}{q^2-R^2}\right)^q.
}
\tag{10}
$$

Here \(c_G\) is the original lower Gamma-envelope constant.

For (10), expand \(P\) in the full shifted Legendre basis on \([q,2q]\). Its central squared value is bounded by

$$
\frac{(D+1)^2 100^D}{q}\int_q^{2q}|P|^2.
$$

On the central interval, \(|Q|^2\le(Y^2+R^2)^q\); on \([q,2q]\), \(|Q|^2\ge(q^2-R^2)^q\). The original Gamma mass controls the numerator, and the original lower density on that entire interval controls the denominator. This is the same complete-form comparison used in LRC, with the literal degree and root radius retained. 

On the eventual guard \(R\le Y/4\),

$$
\eta_k\le
\exp[-q\log16+O_h(k+\log q)].
$$

Let

$$
dW^\circ=1_{\{|y|>Y\}}\,dW.
$$

Denote its monic polynomials and norms by \(U_j^\circ,\nu_j^\circ\), and its residual minima by \(H_r^\circ\).

The passage from polynomial to rational fibres also has a finite bound. If \(C_k\) is the original multiplication constant at the required output degree, set

$$
\xi_k=\eta_k\frac{(C_k+R)^2}{d^2}.
$$

For every candidate in (4), multiplication by \(Q\) gives a polynomial, and multiplication by \(z-y\) returns the numerator controlled in (9). Hence

$$
\boxed{
(1-\xi_k)H_r\le H_r^\circ\le H_r,
\qquad 0\le r\le q+2.
}
\tag{11}
$$

In particular, for the removal fractions

$$
T_r=1-H_{r+1}/H_r,
\qquad
T_r^\circ=1-H_{r+1}^\circ/H_r^\circ,
$$

$$
|T_r-T_r^\circ|\le\frac{\xi_k}{1-\xi_k}.
\tag{12}
$$

The omitted interval has therefore not been assigned zero contribution. Its effect on each actual affine minimum is explicitly bounded.

### Paired removal fractions

On the auxiliary measure, all nonzero orthogonal-polynomial zeros have modulus at least \(Y\). Define the finite inverse moments

$$
M_j^\circ
=
\int_{|y|>Y}\frac{U_j^\circ(y)^2}{y^2}\,dW(y).
$$

There is no inverse moment integrated through \(y=0\).

For a suitable explicit \(\widehat C_k=O_h(q)\), obtained from the original multiplication bound and \(1-\eta_k\),

$$
\frac1{\widehat C_k^2}
\le
\frac{M_j^\circ}{\nu_j^\circ}
\le\frac1{Y^2},
\qquad
\frac{\nu_j^\circ}{\nu_{j-1}^\circ}\le\widehat C_k^2.
\tag{13}
$$

The existing consecutive-zero argument has a stronger use here than phase control alone. It gives the following **amplitude** formulas:

$$
\boxed{
p_{2,q-1+r}
=
\begin{cases}
\displaystyle
R^2\frac{M_r^\circ}{\nu_r^\circ}(1+\epsilon_r),
&r\ \mathrm{even},\\[8pt]
\displaystyle
\frac{(\nu_{r-1}^\circ)^2}
{\nu_r^\circ M_{r-1}^\circ}(1+\epsilon_r),
&r\ \mathrm{odd},
\end{cases}
}
\tag{14}
$$

uniformly for \(0\le r\le q+1\), with

$$
\sup_r|\epsilon_r|
=
O_h(k^2/q^2)+e^{-cq+O_h(k+\log q)}.
\tag{15}
$$

Here is the coefficient calculation behind (14). Write

$$
U_{2h}^\circ(y)=P_h(y^2),\qquad
U_{2h+1}^\circ(y)=yT_h(y^2).
$$

Orthogonality gives exactly

$$
\int T_h(y^2)\,dW^\circ
=\frac{\nu_{2h}^\circ}{P_h(0)},
$$

$$
M_{2h+1}^\circ
=T_h(0)\frac{\nu_{2h}^\circ}{P_h(0)},
\qquad
\frac{P_{h+1}(0)}{P_h(0)}
=-\frac{\nu_{2h+1}^\circ}{\nu_{2h}^\circ}.
\tag{16}
$$

Also,

$$
U_j^\circ(z)C_j^\circ(z)
=
-zM_j^\circ(1+e_j),
\qquad
|e_j|\le\frac{R^2}{Y^2-R^2}.
$$

The positive squared zeros of consecutive polynomials interlace. Therefore their **ratio** of root products differs from its value at zero by logarithm at most

$$
-\log(1-R^2/Y^2),
$$

with no factor \(j\). Combining this fact with (16) gives

$$
\frac{C_r^\circ}{C_{r-1}^\circ}
=
\begin{cases}
\displaystyle
-z\,\frac{M_r^\circ}{\nu_{r-1}^\circ}(1+O_h(R^2/Y^2)),
&r\ \mathrm{even},\\[7pt]
\displaystyle
z^{-1}\frac{\nu_{r-1}^\circ}{M_{r-1}^\circ}(1+O_h(R^2/Y^2)),
&r\ \mathrm{odd}.
\end{cases}
$$

Insert these ratios into the exact Wronskian (7), then use (11)–(12) and the factor \(1-\Delta_r\) in (5). This proves (14). The underlying consecutive-root comparison is retained from the original EC proof. 

For finite use, put \(\rho_k=R^2/Y^2\). On

$$
\rho_k\le1/16,\qquad
32(1+R/d)\rho_k\le1/4,\qquad \xi_k<1/4,
$$

a common relative allowance can be taken as

$$
e_k=
4\left[
32(1+R/d)\rho_k
+\frac{\xi_k}{1-\xi_k}\frac{\widehat C_k^2}{R^2}
+\Delta_k^*
\right],
\tag{17}
$$

where \(\Delta_k^*\) is the maximum of the original LRC/GRA upper bounds for \(\omega_{q+r}/\nu_r\), through \(r=q+1\). Its evaluated size is

$$
\Delta_k^*
=\exp[-2qa_1+O_h(k+\log q)],
\qquad a_1=\psi(1)>0.
$$

After imposing \(e_k\le1/4\), it bounds every \(|\epsilon_r|\) in (14).

This proves, including both high cutoffs,

$$
\boxed{
p_{2,q-1+r}
=
\begin{cases}
\Theta_h(k^2/q^2),&r\ \mathrm{even},\\
\Theta_h(1),&r\ \mathrm{odd}.
\end{cases}
}
\tag{18}
$$

The odd estimate allows values approaching one; it does not assert a uniform gap below one.

The full-packet monic estimate additionally gives

$$
\boxed{
-\log p_{1,q-1+r}
=
2q\psi(r/q)+O_h(k+\log q),
\qquad 0\le r\le q+1.
}
\tag{19}
$$

Indeed, the exact canonical-radius formula and

$$
p_{1,N}p_{2,N}=\frac{|\mathfrak c_{N,\lambda}|^2}{\epsilon_N^2}
$$

reduce this to

$$
\log\nu_r-\log\omega_{q+r}
=2q\psi(r/q)+O_h(k+\log q).
$$

The paired-root proof of this estimate uses the complete degree, radius and parity; applying it to the repeated root list retains \(q=e(k+1)^2\). Its finite monic intervals are those of LRC/CRV, not a differentiated asymptotic remainder. 

## 3. The complete \(p_2\)-product eliminates the inverse moments

Define

$$
\mathscr A_{i,k}
=-\sum_{N=q-1}^{2q-1}w_N\log p_{i,N}.
$$

These are source-response products. They are not a renaming of \(S_K\) or \(S_R\).

Let \(\mathfrak b_r\) denote the leading expression in (14). Consecutive even–odd terms satisfy the exact cancellation

$$
\boxed{
\mathfrak b_{2h}\mathfrak b_{2h+1}
=
R^2\frac{\nu_{2h}^\circ}{\nu_{2h+1}^\circ}.
}
\tag{20}
$$

All inverse moments cancel within each pair.

The recurrence at zero gives

$$
|U_q^\circ(0)|
=
\prod_{h=0}^{q/2-1}
\frac{\nu_{2h+1}^\circ}{\nu_{2h}^\circ}.
$$

Using the original endpoint weights, rather than replacing them by equal weights,

$$
\sum_{r=0}^{q}w_{q-1+r}\log\mathfrak b_r
=
2q\log R-2\log|U_q^\circ(0)|
+\log
\frac{M_q^\circ/\nu_q^\circ}
     {M_0^\circ/\nu_0^\circ}.
\tag{21}
$$

The final logarithm is bounded by \(2\log(\widehat C_k/Y)=O_h(1)\).

Thus

$$
\boxed{
\mathscr A_{2,k}
=
2\log|U_q^\circ(0)|-2q\log R
+O_h(1+k^2/q).
}
\tag{22}
$$

A finite error bound is

$$
2\log(\widehat C_k/Y)+4qe_k.
$$

The original \(q+1\) changing inverse moments have been eliminated. What remains is a single specified orthogonal-polynomial value, which can be evaluated without solving an arithmetic moving-kernel limit.

## 4. Evaluate that polynomial value through two rank-one quotients

Push \(dW^\circ\) forward under the literal scaling

$$
x=(y/q)^2.
$$

Its full arithmetic mass is retained. Let \(h=q/2\), and let \(\widehat P_h\) be the monic polynomial for this pushed-forward measure. Then

$$
U_q^\circ(y)=q^q\widehat P_h((y/q)^2).
\tag{23}
$$

For the arithmetic and Gamma sources separately, define

$$
D_h^\mu(a)=
\det\left[\int x^{i+j+a}\,d\mu(x)\right]_{0\le i,j<h},
\qquad
f_\mu(a)=\log D_h^\mu(a).
$$

Here both measures contain the same complete \(Q\)-factor and the same gap \(x>\epsilon_*^2\).

The constant-term determinant formula gives

$$
|\widehat P_h(0)|
=\frac{D_h^m(1)}{D_h^m(0)}.
\tag{24}
$$

Moreover, \(f_\mu(a)\) is convex: its second derivative is the variance of \(\sum_i\log x_i\) in its full squared-Vandermonde integral. Consequently,

$$
\boxed{
\frac{f_m(0)-f_m(-2)}2
\le
\log|\widehat P_h(0)|
\le
\frac{f_m(2)-f_m(0)}2.
}
\tag{25}
$$

The arithmetic comparison in these two slopes is low rank.

For the positive slope, the two spaces are

$$
V=\mathcal P_{h-1},
\qquad
xV=x\mathcal P_{h-1}.
$$

Their common subspace is \(x\mathcal P_{h-2}\), of codimension one in each. The complete determinant factorization through that common subspace cancels its Gram. Only two rank-one attained quotient norms remain.

The gapped version of (8) has constants

$$
\ell_k^\circ=(1-\eta_k)\ell_k,\qquad
u_k^\circ=\frac{u_k}{1-\eta_k^\Gamma},
$$

so

$$
\boxed{
\left|
[f_m(2)-f_m(0)]-[f_\Gamma(2)-f_\Gamma(0)]
\right|
\le
\Lambda_k^\circ,
}
\tag{26}
$$

where

$$
\Lambda_k^\circ=\log(u_k^\circ/\ell_k^\circ)
=O_h(k+\log q).
$$

There is no factor \(h\) in (26).

For the negative slope, compare \(V\) and \(x^{-1}V\), whose common subspace is \(\mathcal P_{h-2}\). This calculation takes place only on the gapped measure. It introduces no divergent inverse moment at zero.

The original multiplication bound supplies \(B_m,B_\Gamma=O_h(q)\) such that

$$
\|yF\|_\mu\le B_\mu\|F\|_\mu
$$

on the required polynomial spaces. Jensen gives

$$
\left(\frac q{B_\mu}\right)^4\|F\|_\mu^2
\le\|F/x\|_\mu^2
\le\epsilon_*^{-4}\|F\|_\mu^2.
$$

Hence the rational comparison has logarithmic width

$$
\Lambda_k^{\mathrm{rat}}
=
\Lambda_k^\circ+
4\log\frac{B_mB_\Gamma}{\epsilon_*^2q^2}
=O_h(k+\log q).
$$

The same two rank-one quotient factorizations prove

$$
\boxed{
\left|
[f_m(0)-f_m(-2)]-[f_\Gamma(0)-f_\Gamma(-2)]
\right|
\le\Lambda_k^{\mathrm{rat}}.
}
\tag{27}
$$

This is the new comparison step. Bounding two \(h\)-dimensional determinants independently would cost \(h\Lambda_k\) and lose the desired coefficient.

### The Gamma slopes

The already established AG calculation supplies the required fixed-potential Gamma determinant. On its retained positive interval,

$$
V(x)=\pi\sqrt x-2\log x,
$$

and the three powers \(a=-2,0,2\) give analytic factors

$$
W_{a,k}(x)
=(a-\tfrac34)\log x-\tau_k/x,
\qquad
\tau_k=\frac{(\gamma^2-\delta^2)k(k+2)}{3q}.
$$

The full root remainder, Gamma-density error, and both complementary regions are retained in AG14–18. The parameter \(\tau_k\) is bounded at every fixed multiplicity.

The resulting analytic-factor formula is

$$
\log D_h^\Gamma[e^W]
=
\log D_h^\Gamma[1]
+h\int W\,d\rho_{2,\pi}+O_h(\log q).
$$

This is the existing application of the one-cut expansion and analytic linear-statistic formula of Borot and Guionnet (2013), on the fixed interval where the potential is analytic. It does not assert analyticity through \(x=0\). ([arXiv][2])

Therefore

$$
f_\Gamma(2)-f_\Gamma(0)=qL+O_h(\log q),
$$

$$
f_\Gamma(0)-f_\Gamma(-2)=qL+O_h(\log q).
$$

Combining these with (25)–(27) yields

$$
\boxed{
\log|\widehat P_h(0)|
=\frac q2L+O_h(k+\log q),
}
$$

and restoring the exact scaling in (23),

$$
\boxed{
\log|U_q^\circ(0)|
=q\log q+\frac q2L+O_h(k+\log q).
}
\tag{28}
$$

A finite enclosure, before replacing the Gamma slopes by their asymptotics, is

$$
\frac{f_\Gamma(0)-f_\Gamma(-2)-\Lambda_k^{\mathrm{rat}}}{2}
\le \log|\widehat P_h(0)|
\le
\frac{f_\Gamma(2)-f_\Gamma(0)+\Lambda_k^\circ}{2}.
\tag{29}
$$

All three reference determinants in this interval are specified Gamma integrals; no unknown arithmetic determinant remains in its endpoints.

Substituting (28) into (22) proves the claimed value (1). Equivalently,

$$
\boxed{
\left(
\prod_{N=q-1}^{2q-1}p_{2,N}^{\,w_N}
\right)^{1/(2q)}
=
\frac{kH_\rho}{q}\,e^{-L/2}
\left[1+O_h\!\left(\frac{k+\log q}{q}\right)\right].
}
\tag{30}
$$

## 5. The first product receives the complete arithmetic correction

The exact three-column identity is

$$
p_{1,N}p_{2,N}
=\frac{|\mathfrak c_{N,\lambda}|^2}{\epsilon_N^2}.
$$

The original current theorem gives

$$
\mathfrak c_{N,\lambda}
=d+i(-1)^{N+1-q}(t-\varepsilon_{N,\lambda}),
\qquad
0<\varepsilon_{N,\lambda}=O_h(k^3/q^2).
$$

Thus

$$
\log|\mathfrak c_{N,\lambda}|
=\log R+O_h(k^2/q^2)
$$

uniformly on the original action window. 

Using the exact action weights,

$$
J_k^{\mathrm{action}}
=2\sum_{N=q-1}^{2q-1}w_N\log\epsilon_N,
$$

gives

$$
\boxed{
\mathscr A_{1,k}+\mathscr A_{2,k}
=
J_k^{\mathrm{action}}-4q\log R
+O_h(k^2/q).
}
\tag{31}
$$

The original weighted action identity is unchanged. 

Equations (1) and (31) prove (2), or

$$
\boxed{
\left(
\prod_{N=q-1}^{2q-1}p_{1,N}^{\,w_N}
\right)^{1/(2q)}
=
qkH_\rho
\exp\!\left(\frac L2-\frac{J_k^{\mathrm{action}}}{2q}\right)
\left[1+O_h\!\left(\frac{k+\log q}{q}\right)\right].
}
\tag{32}
$$

This can now receive the full evaluated scalar. Define

$$
A_J=C_\sigma+8\log2-4-(4m_0-2)C_\Gamma,
\qquad
r_h=\frac23(\gamma^2-\delta^2)M_{-1}.
$$

The current absolute-action formula, valid at every fixed original multiplicity, is

$$
\begin{aligned}
J_k^{\mathrm{action}}
={}&C_Bq^2+4q\log q+A_Jq
+\frac{\log2}{\pi}I_hk^2-r_hk(k+2)\\
&+\frac{C_\Gamma q}{2(\log q+c_\zeta)}
+o_h(q/\log q).
\end{aligned}
$$

Its arithmetic estimate remains an imported written result; the new product calculation does not independently recertify that estimate.

Substitution gives the completed product expansion

$$
\boxed{
\begin{aligned}
\mathscr A_{1,k}
={}&C_Bq^2+2q\log(q/k)
+[A_J-L-2\log H_\rho]q\\
&+\frac{\log2}{\pi}I_hk^2-r_hk(k+2)\\
&+\frac{C_\Gamma q}{2(\log q+c_\zeta)}
+o_h(q/\log q),
\end{aligned}}
\tag{33}
$$

whereas

$$
\boxed{
\mathscr A_{2,k}
=
2q\log(q/k)+(L-2\log H_\rho)q
+O_h(k+\log q).
}
\tag{34}
$$

In particular, the second product has no \(q/\log q\) contribution. At that precision, the inverse-logarithmic term occurs in the first product.

There is an exact backward interpretation. Repeating the construction in the original Gamma metric gives

$$
\boxed{
\mathscr A_{2,k}^{\mathrm{ar}}
-\mathscr A_{2,k}^{\Gamma}
=O_h(k+\log q),
}
$$

$$
\boxed{
\mathscr A_{1,k}^{\mathrm{ar}}
-\mathscr A_{1,k}^{\Gamma}
=
\delta_{k,1}^{\mathrm{ar}}+O_h(k+\log q).
}
\tag{35}
$$

The monic-window comparison and the original penalties have that same smaller error. Therefore **the arithmetic correction is localized, at the requested precision, in the first source-correlation product**.

This is an allocation between the two specified source-correlation products. It does not assign the unrelated native kernel/residual allocation.

## 6. Evaluate the retained eigenclass’s complete norm loss

The same calculation evaluates a genuinely different original quantity: \(E_{N,\lambda}\) itself.

At the auxiliary zero argument, after the gap has been imposed,

$$
\boxed{
H_{2h}^\circ(0)=H_{2h+1}^\circ(0)
=
\frac{M_{2h}^\circ}{|U_{2h}^\circ(0)|^2}.
}
\tag{36}
$$

This follows from the same finite Wronskian and the identities in (16). It is an auxiliary evaluation in the gapped measure, not a substitution of a critical root into the arithmetic packet.

Returning from zero to the original \(z\), the individual root products contribute

$$
\left|
\log\frac{H_r^\circ(z)}{H_r^\circ(0)}
\right|
\le C_h(r+1)\frac{R^2}{Y^2}.
\tag{37}
$$

Here a factor \(r\) is allowed: this is an individual-product comparison. At \(r\le q+1\), its size is \(O_h(k^2/q)\). Equation (11) then returns the result to the original source.

Since

$$
\log(M_j^\circ/\nu_j^\circ)
=-2\log q+O_h(1),
$$

equations (28), (36) and (37) give

$$
\log\frac{E_{q-1,\lambda}}{E_{2q-1,\lambda}}
=
\log\nu_0-\log\nu_q+2\log|U_q^\circ(0)|
+O_h(1+k^2/q).
\tag{38}
$$

The original monic profile gives

$$
\log\nu_q-\log\nu_0
=
2q\log q+
[4\log2-2+2a_1-2a_0]q
+O_h(k+\log q).
$$

Consequently,

$$
\log\frac{E_{q-1,\lambda}}{E_{2q-1,\lambda}}
=
[L-4\log2+2-2a_1+2a_0]q
+O_h(k+\log q).
$$

The original equilibrium identities imply

$$
C_\Gamma=2C_B-4a_1,
\qquad
C_\partial=2C_B-8a_1+4a_0.
$$

Thus the bracket equals \(C_\partial/2\). These are the original EIQ/ECL conventions, not a coefficient chosen from the known native total. 

The even updates at \(r=0\) and \(r=q\) change the class norm by only \(O_h(k^2/q^2)\). Therefore

$$
\boxed{
\log\frac{E_{q-1,\lambda}}{E_{2q-1,\lambda}}
=
\log\frac{E_{q,\lambda}}{E_{2q,\lambda}}
=
\frac{C_\partial}{2}q+O_h(k+\log q),
}
\tag{39}
$$

which proves the four-cutoff result (3).

### The full degree-resolved loss also has an evaluated limit

For fixed \(0<s\le1\), repeat the rank-one determinant comparison with

$$
h=\left\lfloor\frac{\lfloor sq\rfloor}{2}\right\rfloor
$$

and the original equilibrium

$$
V_s(x)=\frac{\pi}{s}\sqrt x-\frac2s\log x.
$$

The rounding difference \(sq-2h\in[0,2)\) remains in the bounded analytic factor

$$
\frac{sq-2h}{s}\log x
-\frac{\pi(sq-2h)}{2s}\sqrt x.
$$

It is not dropped before taking the determinant.

The resulting value is

$$
\boxed{
-\log\frac{E_{q-1+\lfloor sq\rfloor,\lambda}}
           {E_{q-1,\lambda}}
=
q\,\mathcal J(s)+O_{h,s}(k+\log q),
}
\tag{40}
$$

where

$$
\boxed{
\mathcal J(s)
=
s\left[
\mathcal L(2/s,\pi/s)+\frac12\lambda(2/s,\pi/s)
\right]+2a_0-2
=
\int_0^s f(t)\,dt.
}
\tag{41}
$$

In particular, \(\mathcal J(1)=C_\partial/2\). The equality with the integrated original profile follows from the existing ECL derivative identities. 

This gives an evaluated nonlinear distribution of the actual class loss. Put

$$
g_r=\frac{H_{r+1}}{H_r}
=1-(1-\Delta_r)p_{2,q-1+r}.
$$

Then the positive measures

$$
\frac1q\sum_{\substack{0\le r<q\\r\ \mathrm{odd}}}
[-\log g_r]\,\delta_{r/q}
$$

converge weakly to

$$
\boxed{f(s)\,ds\quad\text{on }[0,1].}
\tag{42}
$$

The total even-index contribution is only

$$
O_h(k^2/q)=o(q).
$$

Thus the leading norm contraction is carried by the odd updates, with the explicit cumulative density (41).

Equation (42) is an integrated theorem. It does not infer individual odd-update limits by differentiating the error in (40).

## 7. The actual kernel response bound now holds throughout the window

The preceding source results hold at every fixed multiplicity. This subsection uses the original simple-quartet five-orbit conductor construction.

Retain

$$
q'=(k-7)^2,\qquad
\Delta_A=q-q'=16k-48,\qquad
v=\operatorname{ord}_0E_A\le80,
$$

and the actual inclusion

$$
K=\ker\Lambda_k\subset
V_A=\{P:\chi_{k-8}\mid\mathcal T_AP\}.
$$

The conductor also carries every original relation into the same lower-root ideal. Both facts are explicit in FEX/KRC.   

Let

$$
\pi_{1,K,N}
=
\frac{\|P_Kb_N\|_{G_N}^2}{F_{11}}.
$$

The leading coefficient of the normalized conductor \(\mathcal C_A\) is \((N)_v\). Applying its original forward bound \(M_N\) to an arbitrary minimum representative of an element of \(K\), and then minimizing over the complete lower-root fibre, gives

$$
\boxed{
\pi_{1,K,N}
\le
\min\left\{
1,\,
\frac{u_k}{\ell_k}
\frac{M_N^2\gamma_N}
{\eta_N(N)_v^2
 \nu^-_{\,N-v-q',1}}
\right\},
}
\tag{43}
$$

where

$$
\eta_{q-1}=1,\qquad
\eta_N=1-\Delta_{N-q}\quad(N\ge q).
$$

This bound applies to the whole actual kernel. It does not depend on which coefficient section was selected.

Combining the two complete monic estimates with (19), and writing \(r=N+1-q\), yields

$$
\log\frac{\pi_{1,K,N}}{p_{1,N}}
\le
2q\psi(r/q)
-2q'\psi((r+\Delta_A-v-1)/q')
+O_{h,\varpi}(k+\log q).
$$

The original period \(\varpi\) is fixed.

For \(F(n,r)=2n\psi(r/n)\), the exact identity

$$
F_n-F_r=f(r/n)
$$

integrates this difference:

$$
F(q,r)-F(q',r+\Delta_A)
=
\int_0^{\Delta_A}
f\!\left(\frac{r+s}{q-s}\right)ds.
$$

Using the retained small-argument bound

$$
f(t)=-\tfrac12\log t+O(1)
$$

and retaining the fixed \(v+1\) shift proves

$$
\boxed{
|U_N|
\le
\sqrt{\theta_N}\,
\exp\left[
\frac{\Delta_A}{4}
\log^+\frac{q}{r+\Delta_A}
+C_{h,\varpi}k
\right],
\quad q-1\le N\le2q.
}
\tag{44}
$$

The exact profile identity and logarithmic behavior are the existing CRV formulas. 

Equation (18) simultaneously gives

$$
\boxed{
|V_N|\le C_h\sqrt{\theta_N}
\begin{cases}
q/k,&r\ \mathrm{even},\\
1,&r\ \mathrm{odd}.
\end{cases}
}
\tag{45}
$$

For every fixed \(s_0>0\), the portion \(r\ge s_0q\) therefore has

$$
|U_N|\le\sqrt{\theta_N}\,e^{C_{h,\varpi,s_0}k}.
$$

The actual conductor removes the unrestricted ellipse’s \(e^{cq}\)-scale amplification throughout the macroscopic window, not only at the first two cutoffs.

These bounds enter the same receiver:

$$
P_K=\bar UV,\qquad
P_B=(1-\bar U)(1-V),\qquad
P_\times=\bar U+V-2\bar UV,
$$

$$
\frac{\Phi_X}{2E_N}
=
k[\delta\Re P_X-(-1)^r\gamma\Im P_X]
+(-1)^r\varepsilon_{N,\lambda}\Im P_X.
\tag{46}
$$

The error remains one shared scalar. Its signed sum cancels because \(\sum_XP_X=1\). Equations (44)–(45) improve the actual amplification bounds; they do not set the remaining \(\theta_N\) or complex response position.

## 8. Backward scope correction and resulting state

One statement from the preceding continuation needs a narrower scope. The current COI derivation shows that

$$
\operatorname{im}L_0=\mathcal P_{m-1}
$$

holds for the **consecutive comparison minor**. The original chosen minor \(I\) need not be that minor. Its exact map is

$$
L_I=F_CD_{0I}+L_0M_{0I},
$$

and its arithmetic metric retains the conductor term and both cross terms:

$$
\begin{aligned}
L_I^*G_NL_I={}&
M_{0I}^*G_{00,N}M_{0I}
+D_{0I}^*G_{CC,N}D_{0I}\\
&+M_{0I}^*G_{0C,N}D_{0I}
+D_{0I}^*G_{C0,N}M_{0I}.
\end{aligned}
$$

Accordingly, the earlier low-polynomial coefficient-image statements apply directly to \(L_0\); transporting them to the actual \(L_I\) requires these additional terms. The direct assertions about \(K\cap\mathcal P_D\), \(\Lambda S^v\), and observation survival do not require that section substitution.

The new results above avoid that issue: equations (1)–(42) use the full original class and source; equations (43)–(46) use the actual kernel directly.

The completed advances are therefore:

$$
\boxed{
\begin{gathered}
\text{the full-window }p_2\text{ product through order }q,\\
\text{the full-window }p_1\text{ product through }q/\log q,\\
\text{the terminal-class four-cutoff return }C_\partial q,\\
\text{the degree-resolved nonlinear class-loss measure }f(s)\,ds,\\
\text{the original-kernel response bound across the whole window}.
\end{gathered}
}
$$

The remaining period-dependent quantity is the actual observation projection, particularly \(\theta_N\) and the correlated position of \(U_N,V_N\). The native clipped sums and the independent proper-source return are still different receivers. The new source products do not assign their values by analogy.

These are written deductions from the retained GRA, LRC, EC and AG estimates, including the new paired-product and rank-one comparison arguments above. No new numerical xi-packet evaluation, period computation, formal verification, or repository write is claimed.

[1]: https://dlmf.nist.gov/18.2 "https://dlmf.nist.gov/18.2"
[2]: https://arxiv.org/abs/1107.1167 "https://arxiv.org/abs/1107.1167"
