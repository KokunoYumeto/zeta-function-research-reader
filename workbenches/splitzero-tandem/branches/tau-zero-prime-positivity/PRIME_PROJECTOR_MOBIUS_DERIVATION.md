# The von Mangoldt operator, Fourier support defects, and the full Weil receiver

<!-- original-zeta-reconstruction-start -->
**Original-zeta receiving calculation.** The working meromorphic function is the original Riemann zeta, with its full Gamma/endpoints multiplier and its full trivial-zero and pole divisor retained. [TF1–42](FAITHFUL_THETA_COMPLETION_RETURN.md) proves the original labelled theta inverse and the actual heat-image defect. [UZ1–53](FAITHFUL_UNCOMPLETED_ZETA_HEAT.md) proves every exceptional-point fibre, jet, original-zeta heat term and reflection orientation. [OZC1–48](ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md) rederives the compact contour and interval operator directly from zeta, including the left-cutoff Gamma boundary, and specifies exactly which compensated pairing the bounds concern. [OZH1–49](ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION.md) rederives the actual meromorphic heat, rational signed trace, compact-test domain, contact drift and full causal arithmetic variation. The raw full divisor and the compensated Weil receiver are linked by their displayed correction, not identified. In particular the fixed-test trivial-zero sum converges exactly at translations at least 1/32 and equals the earlier R term; at zero translation it requires the proved cutoff compensation. [OZK1–38](ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md) reconstructs the original signed Cauchy trace, its full Gamma correction, resonant finite parts, every finite matrix and its index, and the complete local heat jets. Its invertible map retains the raw trace and correction separately. These complete receiving proofs govern the interpretation of the retained auxiliary calculations below.
<!-- original-zeta-reconstruction-end -->


This derivation uses the original basis and time scale of [HCR1–42, complete companion source](HURWITZ_CYCLOTOMIC_RECEIVER.tex). It constructs the exact divisibility-projector sum for the von Mangoldt operator, both of its different supported corrections, and its map into the complete Weil formula. The resulting translation form has both signs even after both endpoint values are forced to vanish. No sign of the entire Weil form is inferred from the positive diagonal operator.

## 1. Objects and the finite arithmetic identity

Let \(\mathbb N=\{1,2,\ldots\}\), \(\mathcal H=\ell^2(\mathbb N)\), and retain the orthonormal basis \(\xi_n\). Let \(N\xi_n=n\xi_n\) and \(P_d\xi_n=\mathbf1_{d\mid n}\xi_n\). Thus \(P_d=S_dS_d^*\) in HCR1–4, with no change to the index or the logarithmic generator \(H=\log N\). Write
\[
\mu(1)=1,\qquad
\mu(n)=\begin{cases}(-1)^r,&n\text{ is a product of }r\text{ distinct primes},\\0,&n\text{ has a squared prime factor},\end{cases}
\quad
\Lambda(n)=\begin{cases}\log p,&n=p^k,\ k\ge1,\\0,&\text{otherwise}.
\end{cases}
\tag{PM1}
\]
In particular \(\Lambda(1)=0\). For an integer \(D\ge1\), put
\[
I_D=\{d:2\le d\le D,\ \mu(d)\ne0\},\qquad
c_d=-\mu(d)\log d,\qquad
A_D=\sum_{d\in I_D}c_dP_d,
\quad a_D(n)=\sum_{\substack{d\in I_D\\d\mid n}}c_d.
\tag{PM2}
\]
Every coefficient in this displayed sum is nonzero. An empty sum is the zero operator. Each \(A_D\) is a bounded self-adjoint operator: it is a finite real linear combination of bounded orthogonal projections, all diagonal in the same basis.

For every \(n\ge1\),
\[
\boxed{\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d.}
\tag{PM3}
\]
Here and below \(\log1=0\). To prove (PM3), let \(p_1,\ldots,p_r\) be the distinct prime factors of \(n>1\). Only their squarefree products contribute. The coefficient of \(\log p_i\) in \(\sum_{d\mid n}\mu(d)\log d\) is
\[
\sum_{J\subset\{1,\ldots,r\}\setminus\{i\}}(-1)^{1+|J|}
=-(1-1)^{r-1}.
\]
For \(r=1\) this is \(-1\); for \(r>1\) it is zero. This is exactly (PM3). For \(n=1\) the sole divisor contributes zero. Consequently \(a_D(n)=\Lambda(n)\) as soon as \(D\ge n\). No infinite arithmetic sum is needed at a fixed entry.

## 2. The precise operator domains and modes of convergence

Define the multiplication operator
\[
\mathcal D_\Lambda=\left\{x\in\ell^2(\mathbb N):
\sum_n\Lambda(n)^2|x_n|^2<\infty\right\},\qquad
(Ax)_n=\Lambda(n)x_n.
\tag{PM4}
\]
It is positive and self-adjoint. Positivity follows by summing the nonnegative quantities \(\Lambda(n)|x_n|^2\); that series is finite on \(\mathcal D_\Lambda\) by Cauchy–Schwarz. To identify the adjoint, test against each basis vector. A vector \(y\) belongs to the adjoint domain exactly when the sequence \((\Lambda(n)y_n)_n\) is square summable, and the adjoint is multiplication by that sequence. This is precisely (PM4). For \(x\in\mathcal D_\Lambda\), its first \(K\) coordinates converge to \(x\) in both Hilbert norm and the norm of \(Ax\). Thus the finite vectors form a core. On this core, (PM3) proves the exact identity
\[
\boxed{\Lambda(N)=-\sum_{\substack{d\ge2\\\mu(d)\ne0}}
\mu(d)\log(d)P_d,}
\tag{PM5}
\]
where the right side stabilizes on each finite vector and its closure is the operator (PM4).

The convergence assertion cannot be strengthened to strong convergence of \(A_Dx\) for every \(x\in\mathcal D_\Lambda\). This has an explicit counterexample. Choose distinct odd primes \(q_j\) so large that \(\log q_j\ge j^2\), and define
\[
x_{2q_j}=1/j,\qquad x_n=0\text{ otherwise}.
\tag{PM6}
\]
Arbitrarily large primes exist: a prime divisor of one plus the product of any finite set of primes is outside that set. Thus this choice is available. The series \(\sum1/j^2\) converges, and \(\Lambda(2q_j)=0\), so \(x\in\mathcal D_\Lambda\) and \(Ax=0\). At cutoff \(D=q_j\), the divisors \(2,q_j\) contribute to its \(2q_j\) coordinate and \(2q_j\) does not. Hence
\[
a_{q_j}(2q_j)=\log(2q_j),\qquad
\|A_{q_j}x\|\ge\log(2q_j)/j\ge j.
\tag{PM7}
\]
The claimed stronger convergence therefore fails even on the kernel of \(A\).

A useful valid common domain is explicit. Set
\[
b(1)=0,\qquad
b(n)=\sum_{d\mid n}|\mu(d)|\log d
=2^{\omega(n)-1}\log\operatorname{rad}(n)\quad(n>1),
\quad
\mathcal D_b=\left\{x:\sum b(n)^2|x_n|^2<\infty\right\}.
\tag{PM8}
\]
Here \(\omega(n)\) counts its distinct prime factors and \(\operatorname{rad}(n)\) is their product. Each factor appears in exactly \(2^{\omega(n)-1}\) squarefree divisors, proving the formula for \(b\). The bounds \(|a_D(n)|\le b(n)\) and \(\Lambda(n)\le b(n)\), followed by dominated convergence of the series of squared coordinates, prove \(A_Dx\to Ax\) for every \(x\in\mathcal D_b\). This statement preserves the actual cutoff in (PM2).

## 3. The weighted trace and its exact factor

Fix \(s\in\mathbb C\) with \(\sigma=\Re s>1\), using the real logarithm for \(n^{-s}\). The diagonal operator \(P_dN^{-s}\) has trace norm
\[
\|P_dN^{-s}\|_1=\sum_{k\ge1}(dk)^{-\sigma}
=d^{-\sigma}\zeta(\sigma),\qquad
\operatorname{Tr}(P_dN^{-s})=d^{-s}\zeta(s).
\tag{PM9}
\]
These are HCR26–28 with \(q=a=d\), also proved directly by their displayed sums. Therefore
\[
\sum_{d\ge2,\,\mu(d)\ne0}|c_d|\,\|P_dN^{-s}\|_1
\le\zeta(\sigma)\sum_{d\ge2}(\log d)d^{-\sigma}<\infty.
\tag{PM10}
\]
The scalar majorant converges, for example by integrating \((\log x)x^{-\sigma}\) on \([2,\infty)\). Thus the weighted operator series converges in trace norm. Its diagonal entries stabilize to \(\Lambda(n)n^{-s}\), which identifies its limit as \(AN^{-s}\). In particular
\[
\begin{aligned}
\operatorname{Tr}(AN^{-s})
&=\sum_{n\ge2}\Lambda(n)n^{-s}
=\zeta(s)\sum_{d\ge2}(-\mu(d)\log d)d^{-s}
=-\frac{\zeta'(s)}{\zeta(s)},\\
\|A_DN^{-s}-AN^{-s}\|_1
&\le\zeta(\sigma)\sum_{d>D}|\mu(d)|(\log d)d^{-\sigma}.
\end{aligned}
\tag{PM11}
\]
For completeness the last analytic identity follows without differentiating a conditionally convergent series. The elementary divisor identity \(\sum_{d\mid n}\mu(d)=\mathbf1_{n=1}\), proved by \((1-1)^{\omega(n)}\), and absolute Dirichlet convolution give \(\zeta(s)\sum\mu(d)d^{-s}=1\) for \(\Re s>1\). The two series and their derivatives converge locally uniformly there, using the same logarithmic majorants as (PM10). Differentiate \(\sum\mu(d)d^{-s}=1/\zeta(s)\), obtaining \(\sum(-\mu(d)\log d)d^{-s}=-\zeta'(s)/\zeta(s)^2\), and multiply by \(\zeta(s)\). In particular all signs in (PM11) are fixed. This is the function \(-r(s)\) of HA10.

## 4. The original lattice and the two different cutoff corrections

Retain a nontrivial bounded distributive lattice \(L\), with bottom \(0_L\) and top \(1_L\), and exactly HCR7:
\[
\begin{gathered}
G_L(\mathbb C)=\{(a,\lambda):a\ne0\Longrightarrow\lambda=1_L\},\\
(a,\lambda)+(b,\eta)=(a+b,\lambda\vee\eta),\qquad
(a,\lambda)(b,\eta)=(ab,\lambda\wedge\eta),\\
\tau=(0,0_L),\qquad e=(0,1_L),\qquad\widehat c=(c,1_L).
\end{gathered}
\tag{PM12}
\]
All matrices below have off-diagonal entries \(\tau\), so they are in the row-and-column-finite matrix semiring of HCR7–9. Let
\[
(\widehat P_d)_{nn}=\begin{cases}1_S,&d\mid n,\\\tau,&d\nmid n,\end{cases}
\quad
(M_d)_{nn}=\begin{cases}\tau,&d\mid n,\\e,&d\nmid n,\end{cases}
\quad
R_d=\widehat{1/d}\sum_{j=0}^{d-1}\widehat E(j/d).
\tag{PM13}
\]
The root sum from HCR3, calculated with the actual labels, gives
\[
R_d=\widehat P_d+M_d,
\qquad (R_d)_{nn}=(\mathbf1_{d\mid n},1_L).
\tag{PM14}
\]
At a nonmultiple the roots cancel in amplitude, and their sum is \(e\), not \(\tau\).

For \(D\ge2\), define the sparse and raw sums using only the nonzero coefficients specified in (PM2):
\[
\mathcal A_D=\sum_{d\in I_D}\widehat c_d\widehat P_d,
\qquad \mathcal R_D=\sum_{d\in I_D}\widehat c_d R_d,
\quad
\chi_D(n)=\mathbf1_{\exists p\le D:\ p\text{ prime},\ p\mid n}.
\tag{PM15}
\]
Then the full entry formulas are
\[
(\mathcal A_D)_{nn}=\begin{cases}(a_D(n),1_L),&\chi_D(n)=1,\\\tau,&\chi_D(n)=0,\end{cases}
\qquad
(\mathcal R_D)_{nn}=(a_D(n),1_L).
\tag{PM16}
\]
Indeed an active squarefree divisor of \(n\) exists exactly when a prime divisor at most \(D\) exists. The sparse sum then joins at least one top label, including when its amplitudes subsequently cancel. Every raw summand has top diagonal label, and there is at least one such summand since \(2\in I_D\). This proves (PM16) at every entry. For \(D=1\) both sums are the zero matrix; it is a separate empty-sum case.

The least missing-support correction is
\[
(\mathcal M_D)_{nn}=\begin{cases}\tau,&\chi_D(n)=1,\\e,&\chi_D(n)=0,\end{cases}
\qquad
\boxed{\mathcal A_D+\mathcal M_D=\mathcal R_D.}
\tag{PM17}
\]
Every correction \(C\) satisfying \(\mathcal A_D+C=\mathcal R_D\) has zero amplitudes, off-diagonal entries \(\tau\), top diagonal label when \(\chi_D(n)=0\), and any original label when \(\chi_D(n)=1\). These conditions are necessary by amplitude equality and by the joins in (PM12); they are sufficient by the same calculation. Thus (PM17) is the unique least correction in the entrywise order on zero-amplitude labels, and the entire family of corrections has been specified.

The actual sum of the individual Fourier corrections is usually larger. Put
\[
\mathcal K_D=\sum_{d\in I_D}\widehat c_dM_d,
\qquad Q_D=\prod_{p\le D,\ p\text{ prime}}p.
\tag{PM18}
\]
Each nonzero \(c_d\) acts on \(e\) as \(e\). Therefore
\[
(\mathcal K_D)_{nn}=\begin{cases}\tau,&Q_D\mid n,\\e,&Q_D\nmid n,\end{cases}
\qquad
\boxed{\mathcal A_D+\mathcal K_D=\mathcal R_D.}
\tag{PM19}
\]
To prove the first formula, all the active \(d\) divide \(n\) exactly when all primes at most \(D\) divide \(n\): the forward implication uses that each of these primes is active, and the reverse uses that an active \(d\) is squarefree. The second formula follows by adding (PM14) with its stated coefficients, or directly from (PM16). In particular \(\mathcal M_D\le\mathcal K_D\), but equality need not hold. For \(D=3\), at \(n=2\) the least correction is \(\tau\) and the directly summed correction is \(e\). The additional \(e\) is absorbed by the already top-labelled entry of \(\mathcal A_D\); it has not been set equal to \(\tau\).

## 5. All limiting support, including the index one

Every limit in this paragraph is eventual equality at each matrix entry, so it requires no completeness assumption or infinite join in \(L\). The exact limits are
\[
\begin{aligned}
\mathcal A_{nn}&=\begin{cases}\tau,&n=1,\\(\Lambda(n),1_L),&n\ge2,\end{cases}
&\mathcal R_{nn}&=(\Lambda(n),1_L)\quad(n\ge1),\\
\mathcal M_{nn}&=\begin{cases}e,&n=1,\\\tau,&n\ge2,\end{cases}
&\mathcal K&=Z=\operatorname{diag}(e,e,\ldots).
\end{aligned}
\tag{PM20}
\]
For \(n\ge2\), some prime divisor appears by \(D\ge n\), and (PM3) fixes the amplitude. The index 1 has no active divisors. For the last limit choose a prime not dividing the fixed integer \(n\); once it is included, \(Q_D\nmid n\) forever. Existence follows from the elementary infinitude argument already supplied. Thus
\[
\boxed{\mathcal A+\mathcal M=\mathcal R=\mathcal A+Z.}
\tag{PM21}
\]
In particular every integer with at least two distinct prime factors has the entry \(e\) in both \(\mathcal A\) and \(\mathcal R\), since its zero value of \(\Lambda\) was produced by cancellation. Only the sparse index 1 has \(\tau\). The least limiting defect and the directly summed limiting defect are different matrices, even though both complete the same equation.

The stipulated index set is also essential to the full lift. In the complex identity one may insert the zero term \(-\mu(1)\log1\,P_1=0\). Lifting that newly inserted coefficient as \(\widehat0=e\) instead gives \(e\widehat P_1=Z\), since \(P_1=I\). Thus adding this zero term before lifting changes the sparse lift from \(\mathcal A\) to \(\mathcal A+Z=\mathcal R\). This is the exact connecting map for the two presentations, not permission to identify their support matrices. The original index set \(d\ge2,\mu(d)\ne0\) in (PM5) has been retained throughout.

For an arbitrary input with original coordinates \(v_n=(x_n,\lambda_n)\), where \(x\in\ell^2\) and \(x_n\ne0\Rightarrow\lambda_n=1_L\), the finite sums act by
\[
(\mathcal A_Dv)_n=
\begin{cases}(a_D(n)x_n,\lambda_n),&\chi_D(n)=1,\\\tau,&\chi_D(n)=0,\end{cases}
\quad
(\mathcal R_Dv)_n=(a_D(n)x_n,\lambda_n).
\tag{PM22}
\]
Their amplitude operators are bounded at each finite \(D\). The limiting amplitude operator has domain (PM4). On that domain the limiting labelled maps act as \((\Lambda(n)x_n,\lambda_n)\) at every \(n\ge2\), with \(\tau\) at 1 for the sparse map and \((0,\lambda_1)\) at 1 for the raw map. This is an entrywise definition with the domain of the amplitude stated; it does not assert the false Hilbert convergence excluded in (PM7).

The complete coefficient injection of HCR9 sends a matrix entry \((a,\lambda)\) to \((a,\iota_L(\lambda))\), where \(\iota_L:L\hookrightarrow K\otimes_{\mathbb B}L\) has its stated retraction. For diagonal masks write \(\chi_D^K\) and \((1-\chi_D)^K\) for the separate selected and complementary indicators; the notation is a description of masks, not subtraction in the lattice semiring. The exact images are
\[
\begin{array}{c|cc}
&\text{complex amplitude}&\text{full support matrix}\\\hline
\mathcal A_D&A_D&\chi_D^K\\
\mathcal R_D&A_D&I_K\\
\mathcal M_D&0&(1-\chi_D)^K\\
\mathcal K_D&0&\mathbf1_{Q_D\nmid n}^{K}
\end{array}
\tag{PM23}
\]
The same map takes the limits to the corresponding masks in (PM20). The retraction recovers every original label, including the \(\lambda_n\) in (PM22). The common-label completion \(C(D)=D+Z\) of HCR16 sends \(\mathcal A_D\) to \(\mathcal R_D\) and \(\mathcal A\) to \(\mathcal R\). Its kernel congruence is equality of amplitudes; the complete injection (PM23) has not taken that quotient.

There is also a supported weighted trace, with its domain expressly fixed. For \(\Re s>1\), multiply the diagonal entries by \((n^{-s},1_L)\), take finite basis traces, and then take the absolutely convergent amplitude limit while retaining the eventual label. For \(D\ge2\), sparse finite basis traces are \(\tau\) at cutoff 1 and top-labelled at every cutoff at least 2. Raw traces are top-labelled at every positive cutoff. Hence both limiting traces are
\[
\left(\operatorname{Tr}(A_DN^{-s}),1_L\right),
\quad\text{and, as }D\to\infty,\quad
\left(-\zeta'(s)/\zeta(s),1_L\right).
\tag{PM24}
\]
The correction traces are \(e\), because their zero-amplitude support contains index 1. Equality of the two scalar traces thus does not identify their different support matrices. This construction does not define a trace on arbitrary infinite labelled matrices.

## 6. The exact map into the complete Weil prime distribution

Use the original SZW19 convention
\[
\mathcal T=C_c^\infty(\mathbb R;\mathbb C),\quad
M_h(s)=\int_{\mathbb R}h(v)e^{-(s-1/2)v}\,dv,
\quad h^\#(v)=\overline{h(-v)}.
\tag{PM25}
\]
For \(h\in\mathcal T\), the diagonal operator
\[
B_h=N^{-1/2}\{h(\log N)+h(-\log N)\}
\tag{PM26}
\]
has finite rank: if \(\operatorname{supp}h\subset[-R,R]\), its entries vanish for \(n>e^R\). Its entry at 1 is \(2h(0)\). Since \(\Lambda(1)=0\), the exact trace receiver is
\[
\begin{aligned}
\operatorname{Tr}(AB_h)
&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\{h(\log n)+h(-\log n)\}\\
&=\sum_p\sum_{k\ge1}(\log p)p^{-k/2}
\{h(k\log p)+h(-k\log p)\}
=P_{\rm fin}(h).
\end{aligned}
\tag{PM27}
\]
The prime-power expansion uses (PM1), not an altered norm for supported zero. Every sum in (PM27) is finite for a fixed test. At cutoff \(D\ge\max(2,\lfloor e^R\rfloor)\), \(\operatorname{Tr}(A_DB_h)\) is already equal to (PM27).

To state a full supported test receiver rather than hiding its choices, take \(K\ge\max(2,\lfloor e^R\rfloor)\) and the specified finite-basis lift
\[
(\widehat B_{h,K})_{nn}=
\begin{cases}(n^{-1/2}\{h(\log n)+h(-\log n)\},1_L),&1\le n\le K,\\
\tau,&n>K.
\end{cases}
\tag{PM28}
\]
It keeps the zero values inside that chosen finite basis as \(e\). Multiplying by the matrices in (PM20), followed by the finite trace, gives
\[
\operatorname{tr}(\mathcal A\widehat B_{h,K})
=\operatorname{tr}(\mathcal R\widehat B_{h,K})
=(P_{\rm fin}(h),1_L),
\quad
\operatorname{tr}(\mathcal M\widehat B_{h,K})=e.
\tag{PM29}
\]
The first top label in the sparse trace is at index 2; the raw trace already has it at index 1. These assertions remain true if \(h=0\), because (PM28) deliberately specifies a top-labelled lift of its zero values. This lift therefore is not asserted to be an additive zero-preserving linear map from the complex test space into the ambient split semiring. The amplitude trace is the complex-linear distribution (PM27); the complete matrix injection (PM23) separately retains the support. If a support-adapted lift of \(B_h\) is chosen instead, its zero entries have different labels and (PM28)–(PM29) must not be silently reused.

The connection to the entire supported formula is now exact. With \(H=M_h\), let \(\mathbf e_\lambda\) denote the coordinate basis of \(\mathbb C[L]\) for the finite support lattice used in SZW. Its existing identity is
\[
\begin{aligned}
\boldsymbol B_L(h)&=(H(0)+H(1))\mathbf e_{1_L}
 +H(0)\sum_{\lambda\ne1_L}\mathbf e_\lambda,\\
\boldsymbol Z_L(h)&=Z(h)\mathbf e_{1_L},\\
\boldsymbol D_L(h)&=(\operatorname{Tr}(AB_h)-A_\infty(h))\mathbf e_{1_L}
 +H(0)\sum_{\lambda\ne1_L}\mathbf e_\lambda,\\
\boldsymbol B_L(h)-\boldsymbol Z_L(h)&=\boldsymbol D_L(h),
\end{aligned}
\tag{PM30}
\]
where
\[
Z(h)=\sum_\rho m_\rho M_h(\rho),\qquad
A_\infty(h)=\frac1{2\pi}\int_{\mathbb R}\widehat h(t)
\{\Re\psi(1/4+it/2)-\log\pi\}\,dt.
\tag{PM31}
\]
Here the sum ranges over all nontrivial zeta zeros with their multiplicities and \(\widehat h(t)=\int h(v)e^{-itv}dv\). Formula (PM30) follows by substituting the proved equality (PM27) into SZW24–25 and SZW33–34. Those original formulas retain the theta endpoint traces and prove their convergence. No lower coordinate is replaced by a proposed numerical prime weight. For the noncompact Cauchy convolution in HA7, the same receiver is an absolutely convergent trace: its two terms at \(\pm\log n\) give precisely \((n^{-w}+n^{-\bar z})/(w+\bar z-1)\), yielding the prime term of HA11 when \(\Re z,\Re w>1\). Thus (PM11), (PM27), and HA11 receive exactly the same arithmetic coefficients with their original constants.

## 7. Translation is the map relevant to positivity

For \(f,g\in\mathcal T\), direct substitution in convolution gives
\[
(f^\#*g)(v)=\int_{\mathbb R}\overline{f(x)}g(x+v)\,dx
=\langle f,U_vg\rangle_{L^2(\mathbb R)},\qquad
(U_vg)(x)=g(x+v),\quad U_v^*=U_{-v}.
\tag{PM32}
\]
If the difference of the two test supports is contained in \([-R,R]\), all terms outside that interval vanish, and
\[
P_{\rm fin}(f^\#*g)
=\left\langle f,
\sum_{2\le n\le e^R}\frac{\Lambda(n)}{\sqrt n}
\{U_{\log n}+U_{-\log n}\}g\right\rangle.
\tag{PM33}
\]
The finite operator on the right is bounded and self-adjoint; its norm is at most \(2\sum_{n\le e^R}\Lambda(n)/\sqrt n\). The expression stabilizes on each fixed test pair as \(R\) grows. An infinite bounded translation operator is not required or asserted. This is the exact receiver from the positive multiplication operator (PM4) to the prime sesquilinear form. The map from finite diagonal coefficients to the sum of translations in (PM33) is linear and respects adjoints, but is not a positive map.

Here is a complete sign test. Write \(a=\log2\), choose
\[
0<2\delta<\min\{\log2,\log(3/2)\},\qquad
0\ne\varphi\in C_c^\infty((-\delta,\delta)),\qquad
\varphi_a(x)=\varphi(x-a).
\tag{PM34}
\]
For any nonzero \(\eta\) with this support, put \(k=\eta^\#*\eta\) and \(g_\pm=\eta\pm\eta_a\). Then
\[
g_\pm^\#*g_\pm(v)=2k(v)\pm k(v-a)\pm k(v+a),
\quad k(0)=\|\eta\|_2^2,
\quad\operatorname{supp}k\subset[-2\delta,2\delta].
\tag{PM35}
\]
Indeed expand the four convolutions in (PM32); translating both arguments leaves \(k\) unchanged and translating one shifts it by \(\pm a\). At \(v=a\) or \(-a\), only one shifted term survives, giving \(\pm\|\eta\|_2^2\). At \(v=\pm\log n\) with \(n\ge3\), every term vanishes because \(a+2\delta<\log3\). Consequently
\[
\boxed{P_{\rm fin}(g_\pm^\#*g_\pm)
=\pm\frac{2\log2}{\sqrt2}\|\eta\|_2^2
=\pm\sqrt2\log2\,\|\eta\|_2^2.}
\tag{PM36}
\]
This also proves nonpositivity of the coefficient-to-translation map already on the positive single diagonal coefficient at index 2. Positive diagonal coefficients alone therefore do not imply a positive autocorrelation receiver.

## 8. The same exact signs survive endpoint annihilation

Keep the test operator and its original constant
\[
T=\partial_v^2-\tfrac14.
\tag{PM37}
\]
Integration by parts twice, with no boundary term for a compact smooth test, gives
\[
M_{Tf}(s)=\bigl((s-\tfrac12)^2-\tfrac14\bigr)M_f(s)
=s(s-1)M_f(s).
\tag{PM38}
\]
Thus both endpoint values vanish exactly; at every nontrivial zero the multiplying factor is nonzero. The coefficients are real and the order is even, so \((Tf)^\#=T(f^\#)\). Differentiation of compact convolution gives
\[
(Tf)^\#*(Tg)=T^2(f^\#*g),\qquad
M_{(Tf)^\#*(Tg)}(s)=[s(s-1)]^2
\overline{M_f(1-\bar s)}M_g(s).
\tag{PM39}
\]
All support and convergence requirements of (PM27) and (PM30) continue to hold.

For an explicit endpoint-zero version of (PM36), take \(\eta=T\varphi\) with \(\varphi\) from (PM34). This \(\eta\) is nonzero. Otherwise \(\varphi''=\varphi/4\) everywhere; solving this equation with its zero value and zero derivative outside the compact support gives the identically zero solution, a contradiction. Its support remains contained in \((-\delta,\delta)\), and \(T\) commutes with translation. Hence
\[
g_\pm=T(\varphi\pm\varphi_a),\quad
M_{g_\pm}(0)=M_{g_\pm}(1)=0,\quad
\boxed{P_{\rm fin}(g_\pm^\#*g_\pm)
=\pm\sqrt2\log2\,\|T\varphi\|_2^2.}
\tag{PM40}
\]
There is no approximation in these signs, and no zero-location assumption in their proof.

For these or any endpoint-zero tests, write \(h=g^\#*g\). Then \(M_h(0)=M_h(1)=0\) by the convolution formula, so (PM30) is exactly
\[
\boldsymbol B_L(h)=0,\quad
\boldsymbol D_L(h)=(P_{\rm fin}(h)-A_\infty(h))\mathbf e_{1_L},\quad
\boldsymbol Z_L(h)=(A_\infty(h)-P_{\rm fin}(h))\mathbf e_{1_L}.
\tag{PM41}
\]
The coordinate spaces and all support maps remain those of (PM30); the lower coefficients here are the calculated zero values of these tests. In particular (PM40) assigns no sign to (PM41) until the archimedean term is included. The exact remaining comparison is between the archimedean form and the translated prime form, with their already fixed constants. The positive operator \(\Lambda(N)\), the raw supported zeros, and the endpoint annihilator each have now been connected to that comparison by explicit maps rather than by a positivity assertion.

## Source identities and actual reading coverage

- **HCR:** `work/rh_counterfactual_20260913/tau_prime_weil_20260922/cc_totality_20260923/reader_fragments/HURWITZ_CYCLOTOMIC_RECEIVER.tex`, SHA256 `d8a4caa0b66e492e7ffe987ba2aa04beb201aed3cacc3b30a3b0d4b526e6df38`. Read the complete HCR1–42 and their proofs for this derivation. Operators and full lattice are HCR1–16; the weighted original trace is HCR26–31. Its human operator source is Alain Connes, Caterina Consani and Matilde Marcolli, [*Fun with F1*, arXiv:0806.2401v1](https://arxiv.org/abs/0806.2401v1), original `funBC.tex`, relations `pres`, `idem`, `endo`, `endosigma`, and (c1)–(c4), with exact line ranges recorded in HCR. This derivation has read the HCR proof, not newly reread that author archive; HCR's original-source reading claim is not represented as a new reading here. Equations (PM13)–(PM19) reprove every operator and label identity actually needed.
- **HA:** `HEAT_CAUCHY_ARITHMETIC_DERIVATION.md`, SHA256 `024d3f42723fabf2361cab9400d98d2fe64c57ec114112e6ada6f5430a88f909`. Read HA1–26 for this derivation. [HA10–14, pinned public proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/76f421965914beb133df797835f940849844dc4f/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/HEAT_CAUCHY_ARITHMETIC_DERIVATION.md) supply the exact logarithmic derivative, Cauchy trace and supported coefficients checked in (PM11), (PM30), and the paragraph after (PM31).
- **SZW:** `SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md`, SHA256 `ff7fbe6cc627720368a7c245052ef8263925ca2d912046dfe45e3be74d4455f4`. Read SZW19–26 and SZW33–38, with adjacent text, for this derivation. The complete explicit-formula proof is in [SZW24–26 and full support identity SZW33–34, pinned public source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5a89872598df0902b7c1393cf8e4692ca3010a95/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md). Its human explicit-formula source is Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068), Appendix II, Theorem 6. The present proof uses the complete programme derivation and does not assert a new reading of that author archive.

The Möbius identity (PM3) is the classical arithmetic inversion identity, proved here with its complete divisor calculation. The new programme calculation is its specified split lift, both distinct support corrections and their limits, its exact full Weil receiver, and the endpoint-zero sign test. No novelty claim about classical Möbius inversion, trace-class diagonal operators, or the classical explicit formula is made.
