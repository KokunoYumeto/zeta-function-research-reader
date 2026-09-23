# Every time derivative of the actual heat logarithmic derivative

The original family is \(g_t(s)=16H_t(-2i(s-1/2))\), with \(\partial_tg_t=\tfrac14\partial_s^2g_t\). Its coordinate, analytic convergence, and complete supported arithmetic receiver are proved in [HA1–HA26](HEAT_CAUCHY_ARITHMETIC_DERIVATION.md). This note computes its time derivatives without replacing any Gamma or endpoint coefficient by a constant.

## 1. The exact differential-polynomial recurrence

Let \(\mathscr P=\mathbb Q[X_0,X_1,\ldots]\) be the polynomial ring in countably many variables; each polynomial uses only finitely many of them. Define commuting spatial and evolutionary derivations by
\[
D X_j=X_{j+1},\qquad
V X_j=D^j\!\left(\frac{X_2+2X_0X_1}{4}\right).
\tag{HM1}
\]
Both extend uniquely by the Leibniz rule and linearity. Their commutator is a derivation and is zero on every generator, because \(DVX_j=VDX_j\); therefore \(DV=VD\). Put
\[
B_0=X_0,\qquad B_{k+1}=VB_k
=\sum_{j\ge0}\frac{\partial B_k}{\partial X_j}
D^j\!\left(\frac{X_2+2X_0X_1}{4}\right).
\tag{HM2}
\]
The sum is finite for each \(k\). Where \(g_t\ne0\), set \(L_t=g_t'/g_t\). HA3 and the chain rule prove by induction the exact identity
\[
\partial_t^kL_t(s)=B_k(L_t(s),L_t'(s),L_t''(s),\ldots).
\tag{HM3}
\]
These are derivatives, not coefficients of a Taylor series; the Taylor coefficient is \(B_k/k!\). Each formula is valid as a meromorphic identity in \(s\) and locally holomorphically in \(t\) away from its zeros.

Give every \(X_j\) polynomial degree one. The derivation \(D\) preserves this degree. Split \(V=V_1+V_2\), where
\[
V_1X_j=\tfrac14X_{j+2},\qquad
V_2X_j=\tfrac12D^j(X_0X_1).
\tag{HM4}
\]
Thus \(V_1\) preserves homogeneous degree and \(V_2\) increases it by one. In particular \(\deg B_k\le k+1\). Its homogeneous component of degree \(k+1\) is exactly
\[
\boxed{B_k^{[k+1]}=\frac1{2^k(k+1)}D^k(X_0^{k+1}).}
\tag{HM5}
\]
Here is the full induction. At \(k=0\) the formula gives \(X_0\). As with \(V\), the derivation \(V_2\) commutes with \(D\). The only term capable of producing degree \(k+2\) in \(B_{k+1}\) is \(V_2B_k^{[k+1]}\). Applying the induction hypothesis gives
\[
\begin{split}
V_2B_k^{[k+1]}
&=\frac1{2^k(k+1)}D^k\!\left((k+1)X_0^k\frac{X_0X_1}{2}\right)\\
&=\frac1{2^{k+1}(k+2)}D^{k+1}(X_0^{k+2}),
\end{split}\tag{HM6}
\]
as required. This polynomial is nonzero; its monomial \(X_0^kX_k\) has a positive coefficient. Hence \(\deg B_k=k+1\), not only the upper bound.

For clarity the first two nonconstant polynomials are
\[
\begin{split}
B_1&=\frac14(X_2+2X_0X_1),\\
B_2&=\frac1{16}\left(X_4+8X_1X_2+4X_0X_3
+8X_0X_1^2+4X_0^2X_2\right).
\end{split}\tag{HM7}
\]
They follow by one and two direct applications of (HM2). In particular the coefficient of \(X_1X_2\) is eight; no factor is absorbed into a change of heat time.

## 2. The specified arithmetic expansion

On \(\Re s>1\), retain the exact split
\[
\begin{split}
L_0(s)&=a(s)+r(s),\\
a(s)&=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2),\\
r(s)&=-\sum_{n\ge2}\Lambda(n)n^{-s}.
\end{split}\tag{HM8}
\]
The coefficient functions \(a,a',\ldots\) are retained. The expansion meant here has an explicit rule: in \(B_k\) substitute \(X_j=a^{(j)}+r^{(j)}\), expand each monomial, and multiply the absolutely convergent Dirichlet series in the \(r^{(j)}\) factors by ordered Dirichlet convolution. A term with no \(r\) factor remains its original coefficient function. This is a specified representation; no uniqueness claim is made for expansions with arbitrary \(s\)-dependent coefficients.

Every factor \(r^{(j)}\) has series
\[
r^{(j)}(s)=-\sum_{n\ge2}\Lambda(n)(-\log n)^j n^{-s}.
\tag{HM9}
\]
Each derivative converges absolutely and locally uniformly on the half-plane. Finite products do too, because their absolute multiple sums are bounded by the product of the convergent single sums. Thus the expansion rule and every spatial derivative used below are justified there.

Since each nonzero coefficient of one factor is supported on prime powers, a product of \(j\) such factors is supported on integers with at most \(j\) distinct prime factors. By (HM4)–(HM5), the arithmetic coefficient at an integer with more than \(k+1\) distinct prime factors is zero in this specified expansion of \(\partial_t^kL_t|_0\).

For an integer with exactly \(k+1\) distinct prime factors, write
\[
n=\prod_{i=1}^{k+1}p_i^{\alpha_i},\qquad
p_i\ne p_j\ (i\ne j),\quad\alpha_i\ge1.
\tag{HM10}
\]
Only the homogeneous component of degree \(k+1\), with every factor chosen from \(r\), can contribute. Any \(a\) factor would reduce the number of available prime-power factors. Therefore its coefficient is the coefficient in
\[
\frac1{2^k(k+1)}\partial_s^k(r(s)^{k+1}).
\tag{HM11}
\]
To compute it, each of the \(k+1\) ordered factors must receive one of the distinct prime powers in (HM10). There are exactly \((k+1)!\) such assignments. No exponent can split between two factors, because that would leave a different prime without a factor. Hence the coefficient of \(r^{k+1}\) at \(n\) is
\((-1)^{k+1}(k+1)!\prod_i\log p_i\). Applying \(\partial_s^k\) multiplies it by \((-\log n)^k\). The two signs combine to minus, proving
\[
\boxed{[n^{-s}]\left.\partial_t^kL_t(s)\right|_0
=-\frac{k!}{2^k}(\log n)^k\prod_{i=1}^{k+1}\log p_i.}
\tag{HM12}
\]
The bracket refers exactly to the expansion rule after (HM8). The displayed coefficient has no remaining \(a(s)\) dependence. At lower distinct-prime counts all coefficient functions prescribed by that rule remain present.

For \(k=0\), (HM12) is the original coefficient \(-\log p\) at \(p^\alpha\). For \(k=1\) it is \(-\tfrac12\log p\log q\log(p^\alpha q^\beta)\), agreeing with HA19. For \(k=2\) it is \(-\tfrac12(\log n)^2\log p\log q\log r\) at three distinct prime factors. Formula (HM12) concerns a time derivative; dividing by \(k!\) gives the coefficient in the actual Taylor series in time.

## 3. The global supported receiver

For the original Cauchy tests at \(z,w\) in \(\Re s>1\), the exact global family of [HA5–HA20](HEAT_CAUCHY_ARITHMETIC_DERIVATION.md) gives, for every \(k\),
\[
\left.\partial_t^kK_t(z,w)\right|_0
=\frac{B_k(L_0,L_0',\ldots)(w)
+\overline{B_k(L_0,L_0',\ldots)(z)}}{w+\bar z-1}.
\tag{HM13}
\]
Indeed the finite-pole formula is holomorphic on a time disc for this finite test set, so it may be differentiated any finite number of times; (HM3) supplies the derivatives. All coefficients of \(B_k\) are real. The fixed supported boundary and every lower coordinate have zero time derivative for \(k\ge1\). The corresponding geometric-divisor response is the negative of (HM13) in the top coordinate, with no suppressed lower distribution, by HA20.

This constructs actual arithmetic mixed-prime data at every infinitesimal order. The negative coefficient in (HM12) is not the value of a quadratic form: the matrix denominator, conjugate counterpart, remaining coefficients, Gamma factors and endpoints in (HM13) are still present. The complete sign question is the [Cauchy–Weil matrix criterion](CAUCHY_WEIL_POSITIVITY_CRITERION.md).

## Verification and sources

The accompanying `check_heat_mixed_prime_recurrence.py` computes the entire recurrence through order six in the differential polynomial ring, checks its exact degree, and compares every highest-degree component with (HM5). Its monomial counts are 1, 2, 5, 11, 23, 44 and 82. These finite checks supplement the all-order proof (HM4)–(HM6).

The human heat source remains Brad Rodgers and Terence Tao, [arXiv:1801.05914v5, original author TeX](https://arxiv.org/src/1801.05914v5), equations `hoz`, `htdef` and the subsequent heat equation. The full supported explicit formula is [SZW19–SZW38](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3c022a0adde0a6aa3d8fc8e43ef42795d88e44b0/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md), with its original human sources retained. The logarithmic-derivative equation is the classical Burgers transformation of the heat equation; its exact normalization and every recurrence used here have been proved above. No novelty claim for that transformation is made.
