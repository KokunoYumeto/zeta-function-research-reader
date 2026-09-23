# One fixed primitive test and the full translation criterion

<!-- original-zeta-reconstruction-start -->
**Original-zeta receiving calculation.** The working meromorphic function is the original Riemann zeta, with its full Gamma/endpoints multiplier and its full trivial-zero and pole divisor retained. [TF1–42](FAITHFUL_THETA_COMPLETION_RETURN.md) proves the original labelled theta inverse and the actual heat-image defect. [UZ1–53](FAITHFUL_UNCOMPLETED_ZETA_HEAT.md) proves every exceptional-point fibre, jet, original-zeta heat term and reflection orientation. [OZC1–48](ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md) rederives the compact contour and interval operator directly from zeta, including the left-cutoff Gamma boundary, and specifies exactly which compensated pairing the bounds concern. [OZH1–49](ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION.md) rederives the actual meromorphic heat, rational signed trace, compact-test domain, contact drift and full causal arithmetic variation. The raw full divisor and the compensated Weil receiver are linked by their displayed correction, not identified. In particular the fixed-test trivial-zero sum converges exactly at translations at least 1/32 and equals the earlier R term; at zero translation it requires the proved cutoff compensation. [OZK1–38](ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md) reconstructs the original signed Cauchy trace, its full Gamma correction, resonant finite parts, every finite matrix and its index, and the complete local heat jets. Its invertible map retains the raw trace and correction separately. These complete receiving proofs govern the interpretation of the retained auxiliary calculations below.
<!-- original-zeta-reconstruction-end -->


This proof constructs one specified compactly supported smooth test, chosen independently of every zeta zero. Its Mellin transform is nonzero at every possible off-critical zero. The full reflected Weil pairing of that test with its translates is bounded on the positive half-line exactly when RH holds. The proof does not establish that boundedness.

The original minus-exponent Mellin convention, actual zero multiset, boundary filter, and global Laplace argument are those of [BPZ1–BPZ23](BOUNDARY_PRIMITIVE_ALL_ZERO_RECEIVER.tex). That entire TeX source was read for this derivation. The explicit construction here makes its detecting test independent of a selected or hypothetical zero. The method is an application of the classical Weil-positivity mechanism, with no assertion of historical priority for a bounded-translation criterion.

## 1. A fixed infinite convolution

The compact density and its dyadic product are classical. In Juan Arias de Reyna, [*An infinitely differentiable function with compact support: Definition and properties*, arXiv:1702.05442v1](https://arxiv.org/abs/1702.05442v1), Theorem 1 and equations (1)–(9), the author's convention is \(\widehat\varphi(\zeta)=\int\varphi(t)e^{-2\pi i t\zeta}\,dt\). The exact relation to the construction below is
\[
b_r(v)=r^{-1}\varphi(v/r),\qquad
G_r(z)=\widehat\varphi\!\left(\frac{rz}{2\pi i}\right).
\tag{UP0}
\]
Indeed substitution in the integral proves the second equality from the first; the author's product (4), with index \(h=j-1\), becomes exactly (UP3). Fourier uniqueness then proves the first equality for the density constructed below. The author's equation (9) gives the same zero multiplicities as (UP11). The source is the author's 2017 English translation of the 1982 paper. Its introduction credits Jessen and Wintner (1935) for the Fourier-product construction; that earlier paper has not been independently read here. The complete proof below is retained to specify the exact test used in the programme; the bump, product and product-zero multiplicities are not claimed as new.

Throughout the construction retain
\[
r=\frac1{64},\qquad a_j=r2^{-j}\quad(j\ge1),\qquad
\sum_{j\ge1}a_j=r,\quad \sum_{j\ge1}a_j^2=\frac{r^2}{3}.
\tag{UP1}
\]
Let \(u_j(v)=(2a_j)^{-1}\mathbf1_{[-a_j,a_j]}(v)\), and let
\(b_{r,N}=u_1*\cdots*u_N\) be its finite convolution density. This is a nonnegative probability density, is real and even, and is supported in
\([-r_N,r_N]\), where \(r_N=r(1-2^{-N})\). These assertions follow successively from the integral formula for convolution: its integral is the product of the integrals, convolution adds support intervals, and reflection preserves the convolution of even functions.

Use the Fourier convention \(\widehat b(y)=\int_{\mathbb R}b(v)e^{-iyv}\,dv\). Direct integration on each interval gives
\[
\widehat b_{r,N}(y)=\prod_{j=1}^N\frac{\sin(a_jy)}{a_jy},\qquad
G_{r,N}(z)=\int_{\mathbb R}b_{r,N}(v)e^{-zv}\,dv
=\prod_{j=1}^N\frac{\sinh(a_jz)}{a_jz},
\tag{UP2}
\]
with each quotient assigned its removable value 1 at zero. In particular \(\widehat b_{r,N}(y)=G_{r,N}(iy)\).

The entire functions in (UP2) converge uniformly on compact subsets of \(\mathbb C\) to an entire function
\[
G_r(z)=\prod_{j=1}^\infty\frac{\sinh(a_jz)}{a_jz},
\qquad G_r(0)=1.
\tag{UP3}
\]
Here is the required product estimate. The power series for \(\sinh w/w\) gives
\[
\left|\frac{\sinh w}{w}-1\right|
\le\frac{|w|^2e^{|w|}}6.
\tag{UP4}
\]
For the coefficient comparison, \((2k+1)!\ge6(2k-2)!\) for \(k\ge1\), so the tail is bounded by \(|w|^2/6\) times a subseries of \(e^{|w|}\). On \(|z|\le R\), (UP4) and (UP1) bound the sum of the deviations of the factors from 1 by
\(R^2e^{rR/2}r^2/18\). The tail of this convergent sum is uniform on that disc. The estimate
\(\prod(1+|d_j|)\le\exp(\sum|d_j|)\) then shows that the product partial sums are uniformly Cauchy. Their locally uniform limit is entire, proving (UP3).

For real \(y\), each factor in \(\widehat b_{r,N}\) has modulus at most 1. For every fixed integer \(M\ge1\), every \(N\ge M\), and \(|y|\ge1\), keeping its first \(M\) factors gives the explicit bound
\[
|\widehat b_{r,N}(y)|
\le r^{-M}2^{M(M+1)/2}|y|^{-M}.
\tag{UP5}
\]
For \(|y|\le1\) the bound 1 holds. The same two bounds hold for \(G_r(iy)\) by taking the limit. Thus the limiting Fourier function is rapidly decreasing, and every polynomial multiple of it is integrable.

Define
\[
b_r(v)=\frac1{2\pi}\int_{\mathbb R}G_r(iy)e^{iyv}\,dy.
\tag{UP6}
\]
For every integer \(k\ge0\), (UP5), with \(M>k+1\), permits differentiating (UP6) under the integral \(k\) times and gives
\[
b_r^{(k)}(v)=\frac1{2\pi}\int_{\mathbb R}(iy)^kG_r(iy)e^{iyv}\,dy.
\tag{UP7}
\]
These derivatives are continuous by dominated convergence. Moreover, for \(N\) sufficiently large, Fourier inversion applies to the integrable Fourier transform of the actual convolution density \(b_{r,N}\). It gives its continuous representative and the corresponding derivative formula through any fixed order \(k\). The uniform domination (UP5) and pointwise convergence imply
\[
\sup_{v\in\mathbb R}|b_{r,N}^{(k)}(v)-b_r^{(k)}(v)|
\le\frac1{2\pi}\int_{\mathbb R}|y|^k
|G_{r,N}(iy)-G_r(iy)|\,dy\longrightarrow0.
\tag{UP8}
\]
For \(k=0\), every approximating representative is nonnegative and zero outside \([-r,r]\); its continuous representative has these properties everywhere since it has them almost everywhere. The uniform limit therefore has the same properties. Uniform convergence on \([-r,r]\) gives \(\int b_r=\lim_N\int b_{r,N}=1\). Reflection and real-valuedness also pass to the limit. We have proved, with its density and limiting sense specified,
\[
b_r\in C_c^\infty(\mathbb R,\mathbb R),\quad b_r\ge0,\quad
b_r(-v)=b_r(v),\quad \int b_r(v)\,dv=1,\quad
\operatorname{supp}b_r\subset[-r,r].
\tag{UP9}
\]
This is the fixed infinite convolution meant in (UP1). No random choice of a bump or dependence on a zero is involved.

Uniform convergence of the densities on their common compact support permits taking the limit in the integral in (UP2), uniformly for \(z\) in compact subsets. Consequently
\[
G_r(z)=\int_{\mathbb R}b_r(v)e^{-zv}\,dv,
\qquad |G_r(z)|\le e^{r|\Re z|}.
\tag{UP10}
\]
The function is real on the real axis, has real Taylor coefficients, and satisfies \(G_r(-z)=G_r(z)\).

## 2. The exact zero set of the product

There are no zeros of (UP3) apart from the zeros of its individual factors. For proof, at a point where none of the factors vanishes, choose a small disc on which a finite initial product has no zeros and the tail deviations from 1 have modulus at most \(1/2\). Their sum converges uniformly by (UP4). The analytic logarithms of the tail factors, given by the power series for \(\log(1+w)\), then have a uniformly absolutely convergent sum on a smaller disc, since \(|\log(1+w)|\le2|w|\). The tail product equals the exponential of that sum, and is nonzero. At a point where factors vanish, the same reasoning applies after removing the finitely many vanishing factors. Only finitely many can vanish there because \(a_jz\to0\).

The zeros of a single factor are the simple zeros \(z=i\pi n/a_j\), with \(n\in\mathbb Z\setminus\{0\}\). Their union and the order at each point are therefore
\[
\begin{aligned}
\{z:G_r(z)=0\}
&=\left\{\frac{2\pi i k}{r}:k\in\mathbb Z\setminus\{0\}\right\}
=\{128\pi i k:k\in\mathbb Z\setminus\{0\}\},\\
\operatorname{ord}_{2\pi i k/r}G_r&=1+\nu_2(|k|).
\end{aligned}
\tag{UP11}
\]
Indeed the \(j\)-th factor vanishes at \(2\pi i k/r\) precisely when \(2^{j-1}\) divides \(k\), giving the displayed number of factors, each with order one. In particular, every zero of \(G_r\) is on the imaginary axis. The construction does not claim that a critical-line zeta zero cannot lie on that explicitly stated lattice.

## 3. The original primitive boundary filter

Retain the BPZ operators and coordinate conventions:
\[
T=\frac{d^2}{dv^2}-\frac14,\quad f_r=T b_r,\quad
M_f(s)=\int_{\mathbb R}f(v)e^{-(s-1/2)v}\,dv,\quad
f^\#(v)=\overline{f(-v)}.
\tag{UP12}
\]
The test \(f_r\) is real and even and belongs to \(C_c^\infty\), with support contained in \([-r,r]\). Integration by parts twice has no boundary terms and proves
\[
M_{f_r}(s)
=\bigl((s-\tfrac12)^2-\tfrac14\bigr)G_r(s-\tfrac12)
=s(s-1)G_r(s-\tfrac12).
\tag{UP13}
\]
Thus its two endpoint moments vanish, and it is nonzero:
\[
M_{f_r}(0)=M_{f_r}(1)=0,
\qquad M_{f_r}(\tfrac12)=\int f_r=-\tfrac14.
\tag{UP14}
\]
The factor \(T\) and the original coordinate \(s-\tfrac12\) have not been rescaled.

Let \(\rho\) be any actual nontrivial zero of \(\xi_R\). BPZ4–BPZ5 gives \(0\le\Re\rho\le1\) and \(\rho\notin\{0,1\}\); its argument does not need a zero-free assertion on the two vertical boundary lines. Equations (UP11)–(UP13) give the exact detecting statement
\[
\Re\rho\ne\tfrac12\quad\Longrightarrow\quad M_{f_r}(\rho)\ne0.
\tag{UP15}
\]
The implication follows because then \(\rho-1/2\) is not purely imaginary and the factor \(\rho(\rho-1)\) is nonzero. Formula (UP15) applies simultaneously to all actual off-critical zeros, without selecting one during the construction of \(b_r\).

## 4. The actual infinite translation pairing

Let \(\rho\) range over the distinct zeros of \(\xi_R\), with their original multiplicities \(m_\rho\). For compact smooth tests use exactly the pairing
\[
B(f,g)=\sum_\rho m_\rho\overline{M_f(1-\bar\rho)}M_g(\rho),
\quad Q(f)=B(f,f),\quad f_a(v)=f(v-a).
\tag{UP16}
\]
The polynomial zero count and compact-test decay proved in BPZ5–BPZ6 ensure absolute convergence. Here is the estimate specialized to the present test. For every integer \(M\ge0\), integration by parts in the Fourier factor of the Mellin integral gives
\[
\sup_{0\le\sigma\le1}|M_{f_r}(\sigma+i\gamma)|
\le C_M(1+|\gamma|)^{-M}.
\tag{UP17}
\]
All derivatives of \(f_r(v)e^{-(\sigma-1/2)v}\) have uniformly bounded integrals for \(0\le\sigma\le1\), because of (UP9) and its fixed compact support. These bounds prove (UP17) for \(|\gamma|\ge1\); the original integral covers the bounded interval. Combining this with BPZ5, by dyadic height intervals, proves for every integer \(k\ge0\)
\[
\sum_\rho m_\rho|M_{f_r}(\rho)|^2(1+|\Im\rho|)^k<\infty.
\tag{UP18}
\]

Since \(f_r\) is real and even, its transform has the exact identities
\[
M_{f_r}(1-s)=M_{f_r}(s),\qquad
M_{f_r}(\bar s)=\overline{M_{f_r}(s)},\qquad
\overline{M_{f_r}(1-\bar\rho)}=M_{f_r}(\rho).
\tag{UP19}
\]
Translation in the original variable gives
\(M_{(f_r)_a}(s)=e^{-(s-1/2)a}M_{f_r}(s)\) for every real \(a\). Therefore, with \(c_\rho=\rho-1/2\),
\[
K_r(a):=B((f_r)_a,f_r)
=\sum_\rho m_\rho M_{f_r}(\rho)^2e^{c_\rho a},
\qquad q_r=K_r(0)=Q(f_r).
\tag{UP20}
\]
The weight off the critical line is the displayed complex square, not an absolute square. Every off-critical weight is nonzero by (UP15). The multiplicity is retained in the coefficient at each distinct exponent.

Since \(|\Re c_\rho|\le1/2\), equations (UP18) and (UP20) justify all real derivatives locally uniformly:
\[
K_r^{(k)}(a)=\sum_\rho m_\rho M_{f_r}(\rho)^2c_\rho^k e^{c_\rho a},
\quad K_r\in C^\infty(\mathbb R),\quad
|K_r(a)|\le C e^{|a|/2}.
\tag{UP21}
\]
Changing \(\rho\) to \(1-\rho\), respectively \(\bar\rho\), is legitimate in these absolutely convergent sums and proves
\[
K_r(-a)=K_r(a),\qquad K_r(a)\in\mathbb R
\quad(a\in\mathbb R).
\tag{UP22}
\]
No holomorphic extension of this real-time series in the variable \(a\) is asserted. Its proof of smoothness and the growth bound are the real-variable statements in (UP21).

## 5. The global Laplace transform and every possible pole

For \(\Re w>1/2\), (UP18), the strip bound, and absolute integrability permit interchanging the integral and full zero sum. They give
\[
\mathscr K_r(w):=\int_0^\infty e^{-wa}K_r(a)\,da
=\sum_\rho\frac{m_\rho M_{f_r}(\rho)^2}{w-c_\rho}.
\tag{UP23}
\]
For example, the integral of the absolute values of all summands is bounded by
\((\Re w-1/2)^{-1}\sum_\rho m_\rho|M_{f_r}(\rho)|^2\), which is finite. The series on the right is a meromorphic function on the entire \(w\)-plane. On a compact set \(|w|\le R\) avoiding its listed exponent points, only finitely many zeros have bounded height; their nonzero denominators have a positive minimum. For all sufficiently large \(|\Im\rho|\), the denominator has modulus at least \(|\Im\rho|/2\), so (UP18) gives uniform absolute convergence of the remaining tail. The same argument applies on a disc after removing any one listed term.

It follows that its residue at every possible exponent point is exactly
\[
\operatorname{Res}_{w=c_\rho}\mathscr K_r(w)
=m_\rho M_{f_r}(\rho)^2.
\tag{UP24}
\]
The right side is nonzero at every off-critical zero. Distinct actual zeros have distinct \(c_\rho\), so no sum of other zeros can cancel that residue. A point with zero weight is a removable singularity, as specified by (UP24).

Suppose \(K_r\) is bounded on \([0,\infty)\). Its Laplace integral in (UP23) then defines a holomorphic function on \(\Re w>0\), because on every compact subset of that half-plane each derivative in \(w\) is bounded by an integrable multiple of \(a^ke^{-\delta a}\), for some \(\delta>0\). It equals the meromorphic series for \(\Re w>1/2\). The half-plane with the discrete exponent points removed is connected: a segment joining any two points has a compact neighborhood meeting only finitely many such points, and small arcs detour around them. The identity theorem consequently extends their equality throughout that punctured half-plane.

If an actual zero lies off the critical line, reflection provides one with \(\Re\rho>1/2\). Its exponent \(c_\rho\) lies in that half-plane and has the nonzero residue (UP24). A holomorphic Laplace integral there cannot agree on a punctured disc with a meromorphic function having that residue. This contradiction proves
\[
K_r\text{ bounded on }[0,\infty)
\quad\Longrightarrow\quad\mathrm{RH}.
\tag{UP25}
\]
This proof uses the whole infinite zero sum and its normally convergent meromorphic continuation. It does not truncate the actual spectrum.

Conversely, under RH each \(c_\rho=i\gamma_\rho\) is purely imaginary, and (UP19) gives \(M_{f_r}(\rho)\in\mathbb R\). Equations (UP18) and (UP20) then give
\[
q_r=\sum_\rho m_\rho M_{f_r}(\rho)^2\ge0,
\qquad |K_r(a)|\le q_r\quad(a\in\mathbb R).
\tag{UP26}
\]
This is the exact triangle inequality for that absolutely convergent sum, with its actual weights. In particular, no independent sign assumption on \(q_r\) was used to prove (UP25).

## 6. A single fixed test gives the complete criterion

Combining (UP25) and (UP26) proves
\[
\boxed{
\begin{aligned}
\mathrm{RH}
&\Longleftrightarrow K_r\text{ is bounded on }[0,\infty)\\
&\Longleftrightarrow |K_r(a)|\le q_r\text{ for every }a\ge0,
\qquad r=\frac1{64}.
\end{aligned}}
\tag{UP27}
\]
All quantities here arise from the one test fixed in (UP1)–(UP14). The last displayed inequality implies boundedness directly: at \(a=0\) it also forces \(q_r\ge0\), and thereafter supplies the finite constant \(q_r\).

The criterion has an exact two-translate formulation. BPZ13–BPZ14, or direct cancellation of the exponentials in (UP16), gives
\[
Q((f_r)_a)=q_r,
\qquad
Q((f_r)_a+f_r)=2q_r+2K_r(a),
\qquad
Q((f_r)_a-f_r)=2q_r-2K_r(a).
\tag{UP28}
\]
Here Hermitian symmetry of \(B\), the reality (UP22), and its conjugate linearity in the first slot give the cross terms exactly. All three tests retain both zero endpoint moments because translation multiplies those moments by exponentials. Consequently (UP27) is also exactly
\[
\mathrm{RH}\quad\Longleftrightarrow\quad
Q((f_r)_a+f_r)\ge0\text{ and }Q((f_r)_a-f_r)\ge0
\text{ for every }a\ge0.
\tag{UP29}
\]
If an off-critical zero exists, the proof of (UP25) makes \(K_r\) unbounded. One can then choose \(a\ge0\) with \(|K_r(a)|>|q_r|\). The minus sign when \(K_r(a)>0\), and the plus sign when \(K_r(a)<0\), gives the actual compact primitive test with value
\(2q_r-2|K_r(a)|<0\). This witness requires only a translate and a sign of the same fixed test; it does not alter the bump in response to the zero.

Continuity also proves an exact countable version: the inequality in (UP27), or both inequalities in (UP29), can be required for every rational \(a\ge0\), because every real \(a\ge0\) is a limit of such rationals. No corresponding criterion on one fixed, equally spaced translation lattice is asserted here. Sampling on a fixed lattice identifies distinct imaginary frequencies modulo its period; (UP24), which separates their continuous Laplace poles, does not justify discarding that distinction.

## 7. The convolution test and the full supported receiver

Define the actual convolution
\[
h_r=f_r^\#*f_r=f_r*f_r,
\quad h_r\in C_c^\infty(\mathbb R,\mathbb R),
\quad h_r(-v)=h_r(v),\quad
\operatorname{supp}h_r\subset[-2r,2r].
\tag{UP30}
\]
Fubini's theorem on compact supports gives \(M_{h_r}=M_{f_r}^2\). The convolution in the cross pairing of (UP20) is exactly
\[
((f_r)_a)^\#*f_r(v)=h_r(v+a),\qquad
M_{h_r(\,\cdot+a)}(s)=e^{(s-1/2)a}M_{f_r}(s)^2.
\tag{UP31}
\]
For proof, \(((f_r)_a)^\#(v)=f_r(v+a)\) because \(f_r\) is real and even, and a change of variable in the convolution yields the first identity. Both endpoint values of the transform in (UP31) are zero by (UP14). Thus the original full explicit formula on this test reads
\[
K_r(a)=A_\infty(h_r(\,\cdot+a))
-P_{\rm fin}(h_r(\,\cdot+a)),
\tag{UP32}
\]
with the original archimedean and finite-prime terms of BPZ19 and SZW; no endpoint contribution is omitted. The same statement applies to each of the two primitive tests in (UP28), using its own full convolution.

For the finite support semilattice \(\mathscr L\), write \(\mathbf e_\lambda\) for the retained coordinate basis of the supported explicit formula. For the test (UP31), its exact vector values are
\[
\begin{aligned}
\boldsymbol B_{\mathscr L}&=0,\\
\boldsymbol Z_{\mathscr L}&=K_r(a)\mathbf e_{1_{\mathscr L}},\\
\boldsymbol D_{\mathscr L}
&=\bigl(P_{\rm fin}-A_\infty\bigr)(h_r(\,\cdot+a))
\mathbf e_{1_{\mathscr L}},\\
\boldsymbol B_{\mathscr L}-\boldsymbol Z_{\mathscr L}
&=\boldsymbol D_{\mathscr L}.
\end{aligned}
\tag{UP33}
\]
Indeed, both top endpoint coefficients and every lower endpoint coefficient are zero by the evaluated moments in (UP14) and (UP31). These zeros are values of the existing coordinate functionals. They do not identify the supported zero element with external absence.

That distinction is retained directly by the synchronized carriers from BPZ20–BPZ22. For this carrier construction retain the original nontrivial bounded distributive support lattice \(\mathscr L\), with bottom \(0_{\mathscr L}\), top \(1_{\mathscr L}\), and \(0_{\mathscr L}\ne1_{\mathscr L}\). For a complex vector space \(V\), set
\[
G_{\mathscr L}(V)
=\{(0,\lambda):\lambda\in\mathscr L\}
\cup(V\times\{1_{\mathscr L}\}),
\quad A^\uparrow(v,\lambda)=(Av,\lambda)
\tag{UP34}
\]
for each complex linear map \(A\). With the original join addition and meet scalar action, this lift is additive and scalar compatible by direct substitution. Translation, \(T\), and the endpoint map \(E(f)=(M_f(0),M_f(1))\) are all such linear maps. Every nonzero primitive test with label \(1_{\mathscr L}\) maps under \(E^\uparrow\) to \((0,1_{\mathscr L})\), the supported zero in the endpoint carrier. The unsupported input \((0,0_{\mathscr L})\) retains its distinct label. Their entire lower-label families are preserved by (UP34).

Likewise the lifted pairing is exactly
\[
B^{\mathscr L}((u,\lambda),(v,\mu))
=(B(u,v),\lambda\wedge\mu).
\tag{UP35}
\]
It lies in the synchronized carrier: a nonzero amplitude requires both input amplitudes nonzero, hence both input labels top. Its additivity and conjugate scalar compatibility follow from those of \(B\) and distributivity of meet over join. Thus (UP20) and (UP28) retain top support even when their amplitudes vanish. The negative amplitude obtained after (UP29) has this same support label; an endpoint value equal to supported zero does not change its sign. These formulas keep all the original label maps while applying the single fixed primitive test.

## Reading and scope

The complete source read was `BOUNDARY_PRIMITIVE_ALL_ZERO_RECEIVER.tex`, equations BPZ1–BPZ23 and all intervening proofs, at the path linked above. Its original human input is Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5, with source equations `phidef`, `htdef`, `hoz`, and `sas`, and the original Weil explicit-formula convention is retained through the cited programme sources. This note does not represent a fresh read of those author papers. The new self-contained steps are the fixed infinite convolution, its complete product zero set, the nonvanishing at every possible off-critical zero, and the resulting application of the full BPZ Laplace argument. No arithmetic bound on \(K_r(a)\) for all translations has been supplied by this proof.

## Actual positive-real-time continuation

The complete [real-time proof](REAL_TIME_HEAT_TRACE_DERIVATION.md), RT1–30, strengthens the compact-test variation in this edition: the whole zero trace is smooth for the original real heat time t at least zero, with actual right derivatives at zero. RT16 identifies its first derivative with the full causal arithmetic distribution, and RT20–27 constructs every higher meromorphic derivative receiver. The contact comparison retains the unit and inter-zero terms. These results do not assert a common zero strip for negative or complex time and do not prove the remaining RH inequality. All original supported carriers remain present.


## Proved compact-interval and finite-translation bounds

The complete [compact-interval proof](FIRST_PRIME_FULL_WEIL_COERCIVITY.md), FC1–43, proves full Weil coercivity with constant 11509/600000 through support diameter 19/25, including prime 2 and both original endpoint moments. [FW1–21](FIRST_PRIME_WINDOW_BOUND.md) proves the every-rank matrix bound for centre diameter 583/800 and a strict two-test margin through the next prime gap. The same unchanged test now satisfies its required strict correlation bound for every positive translation through log 256, by [FP1–25](FINITE_PRIME_WINDOW_EXTENSION.md) and the complete [rational prime-power certificate, FPC1–14](FINITE_PRIME_WINDOW_COEFFICIENT_CERTIFICATE.md). [PT1–40](PRIME_TWO_HEAT_TAIL_DERIVATION.md) calculates the surviving mixed channel and proves a strictly negative full actual right heat derivative on the stated short interval after the prime-2 atom ends. These are exact portions of the original bound, retaining supported zero and every original arithmetic coefficient. The uniform inequality beyond log 256 remains unproved.


## Original-zeta Gaussian and affine receiving maps

The complete extension OZG1–55 proves that Gaussian convolution of the test at every positive time makes the original trivial-zero scalar sum diverge for every real translation. Its admissible replacement retains each cutoff trace and the Gamma boundary with the identical finite sum U_N; OZG20–27 gives both maps and the inverse. The full coefficient tower, its raw non-Hermitian correction and exact compensated negative index are OZG28–39. No compact-support prime window is assumed after smoothing; all prime powers and Gamma terms, with explicit error bounds, are OZG40–52. This extension acts on the tests while fixing the original zeta zeros.

The different affine change of the actual original heat family is OZR1–36. Its multiplier is exp(chi) C(phi)/C, with the full inverse, exceptional units and local jets. The original generator contains every q derivative term. The signed divisor comparison is OZR19–24; its Cauchy logarithmic kernel has an additional growth contribution 2a. OZR33 proves the exact full negative index after that contribution is retained. The full support carrier and every lower coordinate are OZG53–55 and OZR34–36. These are the receiving maps for these specified extensions; the original preceding test, time and domains remain those stated in its proof.
