# Global contact variation on the fixed primitive test

<!-- original-zeta-reconstruction-start -->
**Original-zeta receiving calculation.** The working meromorphic function is the original Riemann zeta, with its full Gamma/endpoints multiplier and its full trivial-zero and pole divisor retained. [TF1–42](FAITHFUL_THETA_COMPLETION_RETURN.md) proves the original labelled theta inverse and the actual heat-image defect. [UZ1–53](FAITHFUL_UNCOMPLETED_ZETA_HEAT.md) proves every exceptional-point fibre, jet, original-zeta heat term and reflection orientation. [OZC1–48](ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md) rederives the compact contour and interval operator directly from zeta, including the left-cutoff Gamma boundary, and specifies exactly which compensated pairing the bounds concern. [OZH1–49](ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION.md) rederives the actual meromorphic heat, rational signed trace, compact-test domain, contact drift and full causal arithmetic variation. The raw full divisor and the compensated Weil receiver are linked by their displayed correction, not identified. In particular the fixed-test trivial-zero sum converges exactly at translations at least 1/32 and equals the earlier R term; at zero translation it requires the proved cutoff compensation. [OZK1–38](ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md) reconstructs the original signed Cauchy trace, its full Gamma correction, resonant finite parts, every finite matrix and its index, and the complete local heat jets. Its invertible map retains the raw trace and correction separately. These complete receiving proofs govern the interpretation of the retained auxiliary calculations below.
<!-- original-zeta-reconstruction-end -->


This proof evaluates the complete contact contribution on the single fixed primitive test, proves its global convergence, and computes its exact meromorphic Laplace receiver. It then combines that contribution with the regularized variation of the genuine heat family. The surviving terms retain every analytic unit and every interaction between distinct zeros. Adding this scalar contact contribution is not asserted to construct a new global heat family.

The sources used are [AG17–AG24](ACTUAL_HEAT_ZERO_DISTRIBUTION_VARIATION.md), [UP1–UP35](UNIVERSAL_PRIMITIVE_TRANSLATION_CRITERION.md), and the complete companion proof [BT1–BT22](CONTACT_DEFECT_TRACE_VARIATION.tex). The last source is retained at its original programme path in the source-use record. The arithmetic coordinate and the factor \(1/4\) below are exactly those of AG1 and BT13–BT18.

## 1. Original objects and the fixed family of tests

Let
\[
g_t(s)=16H_t(-2i(s-\tfrac12)),\qquad g_0=2\xi_R,\qquad
\partial_tg_t=\tfrac14\partial_s^2g_t.
\tag{GC1}
\]
Let \(\mathcal Z\) be the set of distinct zeros of \(g_0\), with multiplicities \(m_\rho\), and retain the local factorization
\[
g_0(s)=(s-\rho)^{m_\rho}u_\rho(s),\qquad
u_\rho(\rho)\ne0,\qquad
b_\rho=\frac{u_\rho'(\rho)}{u_\rho(\rho)},\qquad
c_\rho=\rho-\tfrac12.
\tag{GC2}
\]
The symbols \(b_\rho\) are the complete local-unit logarithmic derivatives, not free parameters. In particular, their expression in terms of the other zeros will be retained below.

Use the fixed density \(b_r\) of UP1–UP11, with \(r=1/64\), and put
\[
\begin{gathered}
f_r=(\partial_v^2-\tfrac14)b_r,\qquad
F(s)=M_{f_r}(s)=s(s-1)G_r(s-\tfrac12),\\
H(s)=F(s)^2,\qquad A_a(s)=e^{a(s-1/2)}H(s)
\quad(a\in\mathbb R).
\end{gathered}
\tag{GC3}
\]
Here \(H(s)\) denotes the square of the fixed Mellin test, and is distinct from the original heat function \(H_t(Z)\). The product theorem UP11 gives \(F(\rho)\ne0\) at every actual off-critical zero. We do not assert this nonvanishing at every critical zero.

Every derivative \(F^{(j)}\) decreases faster than any inverse power of height on each fixed closed vertical strip. Indeed,
\[
F^{(j)}(s)=\int_{\mathbb R}(-v)^jf_r(v)e^{-(s-1/2)v}\,dv,
\]
and \((-v)^jf_r(v)\) is compactly supported and smooth. Repeated integration by parts in its Fourier factor proves the claim, uniformly in the real part on the strip. Products and derivatives therefore give the same assertion for \(H\).

For every fixed pair of nonnegative integers \(k,N\), there is a finite constant \(C_{k,N}\) such that, for \(a\ge0\),
\[
\max_{0\le j\le2}\sup_{0\le\Re s\le1}
(1+|\Im s|)^N
\left|\partial_s^j\partial_a^k A_a(s)\right|
\le C_{k,N}(1+a^2)e^{a/2}.
\tag{GC4}
\]
To prove this, \(\partial_a^kA_a=(s-1/2)^ke^{a(s-1/2)}H(s)\). Taking at most two spatial derivatives introduces at most \(a^2\), fixed powers of \(s-1/2\), and derivatives of \(H\) of order at most two. The preceding rapid decrease absorbs those powers; the exponential has modulus at most \(e^{a/2}\) on the strip. For \(a\) in a bounded interval of the whole real line, the same proof gives a uniform bound, with \(e^{|a|/2}\) in place of \(e^{a/2}\).

## 2. The global contact sum and all real derivatives

BT15 assigns the contribution \(m_\rho(m_\rho-1)A''(\rho)/4\) at an actual centre. Define the full scalar receiver
\[
\mathcal C(a)=\frac14\sum_{\rho\in\mathcal Z}
m_\rho(m_\rho-1)A_a''(\rho).
\tag{GC5}
\]
The sum converges absolutely, uniformly for \(a\) in every compact real interval, and remains so after every number of real \(a\)-derivatives.

For a detailed bound, AG4 gives a constant with total multiplicity at modulus at most \(R\) bounded by \(C R\log(R+2)\). On a dyadic annulus of radius \(R\), therefore,
\[
\sum_{\rho\ {\rm in\ annulus}}m_\rho(m_\rho-1)
\le\left(\sum_{\rho\ {\rm in\ annulus}}m_\rho\right)^2
=O(R^2\log^2(R+2)).
\tag{GC6}
\]
On the strip, modulus and height are comparable outside a fixed disc. Equations (GC4) and (GC6), with any sufficiently large \(N\), bound the sum of absolute values on this annulus by
\(C_{k,N}(1+a^2)e^{a/2}R^{2-N}\log^2(R+2)\).
Summing the dyadic annuli proves both the stated normal convergence and
\[
\mathcal C\in C^\infty(\mathbb R),\qquad
\mathcal C^{(k)}(a)=
\frac14\sum_\rho m_\rho(m_\rho-1)
\partial_s^2\!\left((s-\tfrac12)^k A_a(s)\right)_{s=\rho},
\quad
|\mathcal C^{(k)}(a)|\le C_k(1+a^2)e^{a/2}
\quad(a\ge0).
\tag{GC7}
\]
Termwise differentiation follows from uniform convergence on real compact intervals at each order. Thus (GC5) is a defined contribution on the full actual zero multiset; no omitted tail or bound on individual multiplicities is assumed.

The exact summand is
\[
A_a''(\rho)=e^{ac_\rho}
\left(a^2F(\rho)^2+4aF(\rho)F'(\rho)
+2F'(\rho)^2+2F(\rho)F''(\rho)\right).
\tag{GC8}
\]
This follows from \(H'=2FF'\) and \(H''=2(F')^2+2FF''\). All derivatives are taken in the original coordinate \(s\). The function \(\mathcal C\) is real and even on the real axis: conjugation of the zero set gives reality, while reflection \(\rho\mapsto1-\rho\), with its unchanged multiplicity, gives \(A_a''(1-\rho)=A_{-a}''(\rho)\). These changes of summation variable are justified by the absolute convergence just proved.

## 3. Exact contact Laplace poles

For \(\Re w>1/2\), define
\[
\Psi_w(s)=\frac{H(s)}{w-(s-1/2)}.
\tag{GC9}
\]
The original strip is free of the test pole at \(s=w+1/2\). Fubini's theorem, justified by (GC6)–(GC7) and the exponential margin \(\Re w-1/2>0\), gives
\[
\widehat{\mathcal C}(w)
:=\int_0^\infty e^{-wa}\mathcal C(a)\,da
=\frac14\sum_\rho m_\rho(m_\rho-1)\Psi_w''(\rho).
\tag{GC10}
\]
For example, integrating the absolute majorant in (GC4) multiplies the convergent annular bound by
\(\int_0^\infty(1+a^2)e^{-(\Re w-1/2)a}da<\infty\).
Writing \(p_\rho=w-c_\rho\), direct differentiation in \(s\) gives
\[
\widehat{\mathcal C}(w)=
\sum_\rho\frac{m_\rho(m_\rho-1)}4
\left(
\frac{2H(\rho)}{p_\rho^3}
+\frac{2H'(\rho)}{p_\rho^2}
+\frac{H''(\rho)}{p_\rho}
\right).
\tag{GC11}
\]
The sign of every denominator derivative is positive because
\(\partial_s(w-(s-1/2))=-1\).

The series in (GC11) extends meromorphically to the whole \(w\)-plane. On a compact set avoiding the discrete points \(c_\rho\), its finitely many bounded-height terms have separated denominators, and all sufficiently high terms have \(|p_\rho|\ge|\Im\rho|/2\). The rapid decrease of \(H,H',H''\) and (GC6) make the tail uniformly absolutely summable. The same argument applies in a small disc around one \(c_\rho\) after that one term is removed. Its complete principal part is consequently
\[
\boxed{
\operatorname{PP}_{c_\rho}\widehat{\mathcal C}
=
\frac{m_\rho(m_\rho-1)F(\rho)^2}{2(w-c_\rho)^3}
+\frac{m_\rho(m_\rho-1)F(\rho)F'(\rho)}{(w-c_\rho)^2}
+\frac{m_\rho(m_\rho-1)
\bigl(F'(\rho)^2+F(\rho)F''(\rho)\bigr)}
{2(w-c_\rho)}.}
\tag{GC12}
\]
Thus each off-critical multiple zero has a nonzero triple pole in this receiver, because \(m_\rho(m_\rho-1)>0\) and \(F(\rho)\ne0\). Each simple zero is absent from this contact receiver. At a critical zero, (GC12) states every possible cancellation through the actual values \(F,F',F''\); none of these values is discarded.

## 4. The genuine heat variation and the exact residual term

Set \(b=g_0'(0)/g_0(0)\), and for distinct zeros define, as in AG19,
\[
T_A(\rho,\eta)=
\frac{A'(\rho)-A'(\eta)}{\rho-\eta}
+\frac{A'(\rho)}{\eta}+\frac{A'(\eta)}{\rho}.
\tag{GC13}
\]
The regularized genuine-heat variation is precisely AG20 and AG22:
\[
\begin{aligned}
\mathcal V(a):=\mathcal V(A_a)
=-\frac14\Bigg[&
\sum_\rho m_\rho(m_\rho-1)A_a''(\rho)
+2b\sum_\rho m_\rho A_a'(\rho)\\
&+2\sum_\rho\frac{m_\rho^2 A_a'(\rho)}{\rho}
+2\sum_{\{\rho,\eta\}}m_\rho m_\eta T_{A_a}(\rho,\eta)
\Bigg].
\end{aligned}
\tag{GC14}
\]
The last sum is over unordered pairs of distinct supports. Define the residual scalar after adding the contact contribution:
\[
\boxed{
\begin{aligned}
\mathcal R(a):=\mathcal V(a)+\mathcal C(a)
=-\frac12\Bigg[
b\sum_\rho m_\rho A_a'(\rho)
+\sum_\rho\frac{m_\rho^2 A_a'(\rho)}{\rho}
+\sum_{\{\rho,\eta\}}m_\rho m_\eta T_{A_a}(\rho,\eta)
\Bigg].
\end{aligned}}
\tag{GC15}
\]
This cancels exactly the second-derivative summand, with its factor \(1/4\), and no other term. Formula (GC15), including its grouped pair term, is the global definition of the residual. It does not assume that the ungrouped series \(\sum m_\rho b_\rho A_a'(\rho)\) is absolutely convergent.

Here are bounds that justify the complete real-parameter statement. The absolute-convergence proof of AG19–AG21 is uniform on any bounded set of the rapid-decay seminorms in AG18. Explicitly, for comparable large \(|\rho|\le|\eta|<2|\rho|\), either their separation is at least \(|\rho|/2\), so endpoint values bound the divided difference, or the segment joining them stays at modulus at least \(|\rho|/2\); integration of \(A''\) along that segment then bounds it. Both cases give \(C_N(1+|\rho|)^{-N}\) times the seminorm of \(A\). The multiplicity sum on a comparable dyadic pair annulus is \(O(R^2\log^2(R+2))\).

For \(|\eta|\ge2|\rho|\), retain the cancellation
\[
T_A(\rho,\eta)=
\frac{\rho A'(\rho)}{\eta(\rho-\eta)}
+\frac{\eta A'(\eta)}{\rho(\eta-\rho)}.
\tag{GC16}
\]
Its absolute value is at most
\(2|\rho||A'(\rho)|/|\eta|^2+2|A'(\eta)|/|\rho|\).
AG's zero count gives
\(\sum_{|\eta|\ge R}m_\eta/|\eta|^2=O(\log(R+2)/(R+1))\)
and
\(\sum_{|\rho|\le R}m_\rho/|\rho|=O(\log^2(R+2))\).
These bounds prove summability of the two disparate-pair terms, uniformly in the same seminorms. The finitely many small zeros have nonzero denominators, since \(g_0(0)\ne0\).

Applying these explicit estimates to (GC4) proves absolute convergence of every single and grouped pair sum in (GC14)–(GC15), locally uniformly in real \(a\), together with every real derivative. It also proves
\[
\mathcal V,\mathcal R\in C^\infty(\mathbb R),\qquad
|\mathcal V^{(k)}(a)|+|\mathcal R^{(k)}(a)|
\le C_k(1+a^2)e^{a/2}\quad(a\ge0).
\tag{GC17}
\]
The derivatives are obtained by replacing \(A_a\) by \((s-1/2)^kA_a\) in the formulas. This is a global statement about the exactly specified AG regularized variation. It does not replace that regularization by an unproved derivative of a global moving-zero sum for arbitrary entire tests.

## 5. Meromorphic receiver of the retained unit and pair interactions

For \(\Re w>1/2\), the estimates just proved permit taking Laplace transforms through every **grouped** sum in (GC14)–(GC15). Indeed their integrable majorant is a constant times \((1+a^2)e^{-(\Re w-1/2)a}\). Thus
\[
\begin{aligned}
\widehat{\mathcal V}(w)&=\mathcal V(\Psi_w),\\
\widehat{\mathcal R}(w)&=
-\frac12\left[
b\sum_\rho m_\rho\Psi_w'(\rho)
+\sum_\rho\frac{m_\rho^2\Psi_w'(\rho)}{\rho}
+\sum_{\{\rho,\eta\}}m_\rho m_\eta T_{\Psi_w}(\rho,\eta)
\right],\\
\widehat{\mathcal V}(w)+\widehat{\mathcal C}(w)
&=\widehat{\mathcal R}(w).
\end{aligned}
\tag{GC18}
\]
On this half-plane \(\Psi_w\) is holomorphic on the entire zero strip and satisfies the rapid-decrease estimates used in AG. The notation \(\mathcal V(\Psi_w)\) in (GC18) means the explicit grouped expression (GC14) evaluated on this test; that expression is well defined by those strip estimates, although \(\Psi_w\) has its stated pole outside the strip.

The displayed expressions extend meromorphically to every \(w\in\mathbb C\), with possible poles only at \(c_\rho\). This assertion retains the grouped pair series. To prove it, fix a compact \(w\)-set with \(|w|\le M\) avoiding those points. For sufficiently high spatial points in the original strip, \(|w-(s-1/2)|\ge |s|/2\). The functions \(\Psi_w'\) and \(\Psi_w''\) therefore have rapid-decay bounds there uniformly in \(w\).

For pairs at comparable high moduli, the proof preceding (GC16) applies uniformly: if a connecting segment is needed, it remains at large modulus and hence avoids the moving test pole \(s=w+1/2\). For well-separated comparable pairs, only endpoint values are used. For disparate pairs use the exact formula (GC16); finitely many bounded-height values and the high-height estimates supply its required bounds. Pairs with both heights bounded form a finite set and are meromorphic in \(w\), with no pole on the chosen compact set. The resulting absolute normal convergence proves the extension away from the discrete points.

To compute its principal part at \(c_\rho\), isolate every pair containing that one zero. The coefficient of \(\Psi_w'(\rho)\) in the bracket in (GC18) is
\[
m_\rho\left[
b+\frac{m_\rho}{\rho}
+\sum_{\eta\ne\rho}m_\eta
\left(\frac1{\rho-\eta}+\frac1\eta\right)
\right]=m_\rho b_\rho.
\tag{GC19}
\]
This is exactly AG23. The inner series is absolutely convergent for this fixed \(\rho\), by its genus-one cancellation: its high-height summand is \(O_\rho(m_\eta/|\eta|^2)\). The other terms of those pairs multiply \(\Psi_w'(\eta)\) and are holomorphic near \(c_\rho\); their normal convergence there follows from the rapid decrease at \(\eta\). The pairs not containing \(\rho\) also converge normally there by the preceding argument. Consequently
\[
\boxed{
\operatorname{PP}_{c_\rho}\widehat{\mathcal R}
=-\frac{m_\rho b_\rho}{2}
\left[
\frac{H(\rho)}{(w-c_\rho)^2}
+\frac{H'(\rho)}{w-c_\rho}
\right].}
\tag{GC20}
\]
In the original fixed-test values, \(H=F^2\) and \(H'=2FF'\). Thus the complete genuine-heat receiver has principal part
\[
\boxed{
\operatorname{PP}_{c_\rho}\widehat{\mathcal V}
=-\operatorname{PP}_{c_\rho}\widehat{\mathcal C}
-\frac{m_\rho b_\rho}{2}
\left[
\frac{F(\rho)^2}{(w-c_\rho)^2}
+\frac{2F(\rho)F'(\rho)}{w-c_\rho}
\right].}
\tag{GC21}
\]
These identities compute the exact cancellation and the entire remaining local principal part. They do not suppress the inter-zero interactions: (GC19) is the map carrying them into the actual local unit \(b_\rho\).

At an off-critical multiple zero, the genuine variation has a nonzero triple pole with the negative of the coefficient in (GC12). The added contact term removes that triple pole. The residual still has a double pole precisely when \(b_\rho\ne0\), since \(F(\rho)\ne0\). At an off-critical simple zero, \(\widehat{\mathcal C}\) is holomorphic and (GC20) is the whole first variation. It has a nonzero double pole exactly when \(b_\rho\ne0\); if \(b_\rho=0\), both its displayed coefficients vanish. This computation does not assert that the actual simple-zero unit derivatives are all nonzero.

## 6. Exact map from the full translation resolvent to its heat variation

The original time-zero kernel and its Laplace transform are UP20 and UP23:
\[
K_r(a)=\sum_\rho m_\rho H(\rho)e^{ac_\rho},\qquad
\mathscr K_r(w)=\sum_\rho\frac{m_\rho H(\rho)}{w-c_\rho}.
\tag{GC22}
\]
Their residue at \(c_\rho\) is \(m_\rho F(\rho)^2\). In particular it is nonzero at every actual off-critical zero, including a simple zero with \(b_\rho=0\). The absence of such a zero from the **first variation** is not its absence from this original resolvent.

We specify exactly the derivative map in (GC18). Take the separated rectangular contours \(\Gamma_j\) of AG22, with real edges \(-1,2\). For each fixed \(j\), the actual function \(L_t=g_t'/g_t\) is holomorphic on the contour for a sufficiently small complex time disc. For \(\Re w>3/2\), the point \(w+1/2\) lies to the right of the contour. Define
\[
\mathscr K_{r,j}(t,w)
=\frac1{2\pi i}\int_{\Gamma_j}\Psi_w(s)L_t(s)\,ds.
\tag{GC23}
\]
This is the sum of the actual zero-cluster residues inside that contour, including all multiplicities, and is holomorphic in time on the stated local disc. At time zero its limit as \(j\to\infty\) is \(\mathscr K_r(w)\), by absolute convergence of (GC22). The residue proof of AG22 extends to this test with its pole outside the contours, as justified immediately below, and gives
\[
\widehat{\mathcal V}(w)
=\lim_{j\to\infty}
\left.\partial_t\mathscr K_{r,j}(t,w)\right|_{t=0}
\qquad(\Re w>3/2).
\tag{GC24}
\]
The test \(\Psi_w\) is holomorphic on and inside these contours, and its rapid strip bounds used in AG's proof hold on the slightly wider strip as well; they follow from the fixed compact support of \(f_r\). The residue derivation and cross-boundary estimates AG23–AG24 therefore apply without a test-pole correction in this specified half-plane.

For a test pole \(p=w+1/2\) strictly inside a particular contour and not a zero or a point on the contour, the precise finite correction is also explicit:
\[
\sum_{\rho_t\ {\rm inside}\ \Gamma_j}
m_{\rho_t}\Psi_w(\rho_t)
=\frac1{2\pi i}\int_{\Gamma_j}\Psi_w L_t\,ds
+H(p)L_t(p).
\tag{GC25}
\]
The added term follows because \(\operatorname{Res}_{s=p}\Psi_w(s)=-H(p)\). On a time disc where \(p\) stays a nonzero point and the contour stays zero-free, this equality may be differentiated, with the correction differentiated too. Equation (GC24), first proved where the pole is outside, and the unique meromorphic continuation in (GC18) specify the complete regularized derivative receiver. No test pole is silently moved through a contour.

Equations (GC18), (GC22), and (GC24) are the promised map to the full original \(K_r\) Laplace transform: apply the actual heat derivative at each fixed zero-isolating exhaustion, then take the proven regularized limit. They do not claim interchange of the infinite zero limit and the time derivative on the entire moving-zero family. Nor do they claim that \(\mathcal R\), obtained by adding the contact term, is the derivative of a globally constructed persistent-contact family.

## 7. A stationary first derivative does not imply a stationary simple zero

There is a further exact local statement about the genuine heat family. No fixed complex spatial point \(s\) is a zero of \(g_t(s)\) for every time. Indeed the original integral gives, for \(T>0\),
\[
g_{-T}(s)=16\int_0^\infty
e^{-Tu^2}\Phi(u)\cosh(2(s-\tfrac12)u)\,du.
\tag{GC26}
\]
The kernel \(\Phi\) is continuous and bounded on \([0,\infty)\), by its defining series and its superexponential bound in AG2, and \(\Phi(0)>0\), since every term there is positive. Substitute \(x=\sqrt T\,u\). For \(T\ge1\) the resulting integrand is bounded in modulus by
\[
\|\Phi\|_\infty e^{-x^2}e^{2|\Re(s-1/2)|x},
\]
an integrable function. Dominated convergence proves the exact limit
\[
\lim_{T\to\infty}\sqrt T\,g_{-T}(s)
=16\Phi(0)\int_0^\infty e^{-x^2}dx
=8\sqrt\pi\,\Phi(0)>0.
\tag{GC27}
\]

For an actual simple zero \(\rho\), joint holomorphy and \(g_0'(\rho)\ne0\) give one analytic zero branch \(\rho(t)\) near zero time and its complete nonvanishing unit. Since \(t\mapsto g_t(\rho)\) is entire and is not identically zero by (GC27), define its finite first nonvanishing order by
\[
n_\rho=\min\{n\ge1:g_0^{(2n)}(\rho)\ne0\}<\infty.
\tag{GC28}
\]
The equality of its derivatives with \(4^{-n}g_0^{(2n)}(\rho)\) follows by repeated differentiation of (GC1). Analytic local division gives
\(g_t(s)=(s-\rho(t))U(t,s)\), with \(U(0,\rho)=g_0'(\rho)\).
Evaluating this identity at the fixed point \(\rho\) gives
\[
\rho(t)=\rho-
\frac{g_0^{(2n_\rho)}(\rho)}
{4^{n_\rho}n_\rho!\,g_0'(\rho)}\,t^{n_\rho}
+O(t^{n_\rho+1}).
\tag{GC29}
\]
This retains the original heat time; no reparameterization is used.

For the local weighted resolvent \(\Psi_w(\rho(t))\), all time derivatives of order \(1,\ldots,n_\rho-1\) vanish. Its derivative at the first nonzero motion order \(n_\rho\) is
\[
\left.\partial_t^{n_\rho}\Psi_w(\rho(t))\right|_0
=-\frac{g_0^{(2n_\rho)}(\rho)}
{4^{n_\rho}g_0'(\rho)}
\left[
\frac{H(\rho)}{(w-c_\rho)^2}
+\frac{H'(\rho)}{w-c_\rho}
\right].
\tag{GC30}
\]
This follows by Taylor substitution in (GC29); the factor \(n_\rho!\) cancels exactly. At an off-critical simple zero its double-pole coefficient is nonzero, since \(H(\rho)=F(\rho)^2\ne0\). For \(n_\rho=1\), the identity \(g_0''(\rho)=2g_0'(\rho)b_\rho\) makes (GC30) precisely (GC20) with \(m_\rho=1\). If the first-order unit drift vanishes, a finite higher-order local receiver still detects the motion.

Equation (GC30) is proved for the actual finite zero cluster. It does not assert convergence of the sum of these higher-order derivatives over every zero. The global first-order receiver is (GC14)–(GC24); the higher-order statement has the explicitly smaller local domain.

## 8. Supported endpoints and interpretation of the cancellation

The fixed tests satisfy \(F(0)=F(1)=0\), hence \(A_a(0)=A_a(1)=0\) for every \(a\). All endpoint and lower fixed-support coordinates in the original full explicit formula therefore have their evaluated zero amplitudes. At the top spectral coordinate, the three scalar receivers are
\[
\boldsymbol{\mathcal V}(a)=\mathcal V(a)\mathbf e_{1_{\mathscr L}},
\qquad
\boldsymbol{\mathcal C}(a)=\mathcal C(a)\mathbf e_{1_{\mathscr L}},
\qquad
\boldsymbol{\mathcal R}(a)=\boldsymbol{\mathcal V}(a)
+\boldsymbol{\mathcal C}(a).
\tag{GC31}
\]
The endpoint weights themselves have zero derivative for these fixed tests. In the full identity \(\boldsymbol B-\boldsymbol Z=\boldsymbol D\), the induced regularized arithmetic coordinate, with the derivative-first order fixed in (GC24), is therefore
\[
\dot{\boldsymbol D}_{\rm reg}(a)
=-\mathcal V(a)\mathbf e_{1_{\mathscr L}},\qquad
\dot{\boldsymbol D}_{\rm reg,contact}(a)
-\dot{\boldsymbol D}_{\rm reg}(a)
=-\mathcal C(a)\mathbf e_{1_{\mathscr L}}.
\tag{GC31a}
\]
All lower-coordinate amplitudes are zero. Thus the contact comparison changes the spectral coordinate by \(+\mathcal C(a)\) and its corresponding arithmetic coordinate by \(-\mathcal C(a)\). These are the induced coordinates of the specified regularized identity. They are not an independent differentiation of a prime expression at nonzero heat time, nor a claim of a global moving-zero derivative for this entire test. The definition of the original heat equation remains (GC1).

On the original synchronized supported carriers, each linear contour or residue map retains its input label, as in BT22 and UP34–UP35. Thus a zero scalar amplitude in (GC31) with top support remains the supported zero \(e\), and not the unsupported element \(\tau\). The contact classes are the full local BT6 classes, including their original analytic units; their map to (GC5) is BT8–BT15 with the original arithmetic coordinate. Their addition removes the multiple-zero splitting term exactly, while (GC19)–(GC21) retains the unit and inter-zero terms. None of these identities assigns positivity to the complete original Weil form or implies RH.

## Source-use record

AG17–AG24 and their complete proofs were reread at the beginning of this calculation. UP1–UP35 was verified at its previously reviewed source version. BT1–BT22 and all proofs were read in full from:

[Complete companion source, BT1–22](CONTACT_DEFECT_TRACE_VARIATION.tex)

The original human heat source remains Brad Rodgers and Terence Tao, The de Bruijn–Newman constant is non-negative, arXiv:1801.05914v5, with exact author-source coordinates retained in AG and BT. This calculation does not claim a fresh read of that author paper. The convergence, meromorphic continuation, fixed-point asymptotic, and local higher-order formulas needed here are proved above.

## Actual positive-real-time continuation

The complete [real-time proof](REAL_TIME_HEAT_TRACE_DERIVATION.md), RT1–30, strengthens the compact-test variation in this edition: the whole zero trace is smooth for the original real heat time t at least zero, with actual right derivatives at zero. RT16 identifies its first derivative with the full causal arithmetic distribution, and RT20–27 constructs every higher meromorphic derivative receiver. The contact comparison retains the unit and inter-zero terms. These results do not assert a common zero strip for negative or complex time and do not prove the remaining RH inequality. All original supported carriers remain present.
