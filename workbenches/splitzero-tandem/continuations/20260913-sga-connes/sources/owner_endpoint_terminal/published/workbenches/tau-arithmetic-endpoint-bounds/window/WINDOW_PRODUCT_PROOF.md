# Exact consecutive-window control and endpoint determinants

This note proves the consecutive product, its sharper four-endpoint consequence, and its two-transfer reduction for the original canonical quotient metrics. Composed with the independently reviewed arithmetic norm bound on a balanced window, it gives a necessary four-volume growth threshold of **4**, improving the older threshold of 2. It proves no opposing arithmetic upper estimate and no Riemann-hypothesis conclusion. It belongs to the next integration cut, not the frozen Toda–Gamma edition.

## 1. Original identity and exact window product

Fix a nonempty reflection-stable packet, tensor degree, cyclic dimension \(q\ge1\), and one admissible observation. Write \(V_N=\det G_N>0\), retain the original monic squared norms \(\omega_N>0\), and set \(\delta_N=V_N/V_{N-1}\in(0,1]\). The original Toda source, TVB.13, TVB.15 and TVB.22–27, supplies

\[
\epsilon_N^2+\phi_N^2
=\frac{\omega_{N+1}}{\omega_N}(1-\delta_N)(\delta_{N+1}^{-1}-1),
\qquad \phi_N=\sigma-\partial_\theta\log V_N,\qquad N\ge q. \tag{WP1}
\]

The real phase is not set to zero. At a general tilt all norms, volumes and derivatives in WP1 are evaluated at that same tilt. The arithmetic norm and asymptotic composition below use the original observation \(\theta=0\).

For integers \(n\ge q\), \(r\ge1\), put \(d_j=\delta_{n+j}\) for \(0\le j\le r\), \(\Omega=\omega_{n+r}/\omega_n\), and \(E=\min_{0\le j<r}\epsilon_{n+j}\). Multiplying WP1 first, the norm ratios telescope, every interior \(1-d_j\) occurs twice, and \(\prod_{j=1}^r d_j=V_{n+r}/V_n\). Therefore

\[
\boxed{\prod_{j=0}^{r-1}(\epsilon_{n+j}^2+\phi_{n+j}^2)
=\frac{\omega_{n+r}V_n}{\omega_nV_{n+r}}
(1-d_0)(1-d_r)\prod_{j=1}^{r-1}(1-d_j)^2.} \tag{WP2}
\]

Since \(E^{2r}\le\prod_j\epsilon_{n+j}^2\le\prod_j(\epsilon_{n+j}^2+\phi_{n+j}^2)\), dropping only the displayed nonnegative factors, each at most one, gives

\[
\boxed{E\le\left(\frac{\omega_{n+r}V_n}{\omega_nV_{n+r}}\right)^{1/(2r)}.} \tag{WP3}
\]

No inverse at degree \(q-2\), reassigned Gram, or recurrence supremum occurs. The empty quotient \(q=0\) is outside this positive-dimensional theorem; its determinant and control are separately the empty determinant and zero.

## 2. Sharper four-endpoint bound and comparison

For \(r\ge2\), define

\[
\alpha=V_n/V_{n-1},\quad \beta=V_{n+r}/V_{n+r-1},\quad
t=V_{n+r-1}/V_n,\quad A=\Omega^{1/(2r)}.
\]

These are positive and at most one, and the \(r-1\) interior contractions have product \(t\). For \(s=r-1\),

\[
\prod_{j=1}^s(1-d_j)\le(1-t^{1/s})^s. \tag{WP4}
\]

If any interior \(d_j=1\), the left side is zero. Otherwise set \(v_j=-\log d_j>0\). The second derivative of \(f(v)=\log(1-e^{-v})\) is \(-e^{-v}/(1-e^{-v})^2<0\), so finite concavity proves WP4. This is ordinary Jensen concavity, obtainable from the integral form by a step function; see [DLMF §1.7(iv)](https://dlmf.nist.gov/1.7.iv). Inserting WP4 into WP2 gives

\[
\boxed{E\le U:=A
\left(\frac{(1-\alpha)(1-\beta)}{\beta t}\right)^{1/(2r)}
\left(1-t^{1/(r-1)}\right)^{(r-1)/r}.} \tag{WP5}
\]

For \(r=1\) use the separate expression

\[
E=\epsilon_n\le\sqrt{\frac{\omega_{n+1}}{\omega_n}
(1-\alpha)(\beta^{-1}-1)}. \tag{WP6}
\]

No \(1/(r-1)\) is evaluated in WP6. For any \(r\), a unit contraction \(d_j=1\) makes an adjacent local radius sum zero; hence the corresponding allowance and phase both vanish and \(E=0\). At an interior unit contraction both neighboring local sums vanish. If \(t=1\), all interior contractions are one and WP5 is zero.

The corrected PR23 endpoint note proves the older bound

\[
E\le A\sinh\!\left(\frac{\mathcal B}{2r}\right),\qquad
\mathcal B=\log\frac{V_{n-1}V_n}{V_{n+r-1}V_{n+r}}
=-\log\alpha-\log\beta-2\log t.
\]

In fact \(U\le A\sinh(\mathcal B/(2r))\). To prove it without assuming an arithmetic extremizer, replace just the interior scalar contractions by their common geometric mean. This maximizes the exact product by WP4 while leaving the four endpoints fixed. For that scalar sequence put \(v_j=-\log d_j\). The original local completion of the square is

\[
(1-d_j)(d_{j+1}^{-1}-1)
=\sinh^2\frac{v_j+v_{j+1}}2
-\left(e^{(v_{j+1}-v_j)/2}-\cosh\frac{v_j+v_{j+1}}2\right)^2.
\]

Drop this square and apply concavity of \(\log\sinh x\), whose second derivative is \(-1/\sinh^2x\), to the \(r\) nonnegative half-sums. Their sum is \(\mathcal B/2\), proving the comparison. A zero half-sum is handled before logarithms. WP5 also dominates the simpler WP3 because all factors it retains are at most one; WP3 alone need not dominate the older bound for small contractions.

For constant \(d=e^{-v}<1\), WP5 becomes \(2A\sinh(v/2)\), whereas the older expression is \(A\sinh v\); their ratio is \(\cosh(v/2)\).

The sharpness claim is only for the relaxed scalar data, not the arithmetic moment family. In its strictly positive case require **all three** \(\alpha<1,\beta<1,t<1\). Set the interior ratios equal, put \(f_j=(1-d_j)(d_{j+1}^{-1}-1)>0\), choose successive norm ratios \(U^2/f_j\), phases zero and all allowances \(U\). The norm-ratio product is exactly \(\Omega\), so the prescribed endpoints and equality hold. Zero-product cases give a zero bound directly. Strict contraction of only the two outside ratios would not justify claiming \(f_j>0\) when \(t=1\).

## 3. Retained phase and interior loss

When every interior contraction is strictly below one, define

\[
J=(r-1)\log(1-t^{1/(r-1)})-\sum_{j=1}^{r-1}\log(1-d_j)\ge0.
\]

WP2 is precisely

\[
\prod_j(\epsilon_{n+j}^2+\phi_{n+j}^2)=U^{2r}e^{-2J},\qquad
\prod_j(E^2+\phi_{n+j}^2)\le U^{2r}e^{-2J}. \tag{WP7}
\]

The polynomial \(P(x)=\prod_j(x+\phi_{n+j}^2)\) is strictly increasing for \(x\ge0\). For consistent input, the right side \(R\) is at least \(P(0)\), so \(P(x)=R\) has a unique nonnegative solution \(x_*\) and \(E\le\sqrt{x_*}\). If proposed data instead have \(R<P(0)\), they are inconsistent with the original radius identities; a nonnegative threshold cannot then be asserted. Unit-contraction cases are handled directly, without using an infinite or undefined \(J\).

## 4. Literal determinant and full-jet transfer cancellation

To distinguish this scalar from the existing exterior map named \(\Lambda_N\), write \(\Lambda_N^{\rm sc}=\omega_N/V_N\). With the unchanged source and relation determinants, TVB.13 and TVB.15 give

\[
\omega_N=\mathfrak D_{N+1}/\mathfrak D_N,\qquad
V_N=\mathfrak D_{N+1}/\mathfrak B_{N-q+1},\qquad
\boxed{\Lambda_N^{\rm sc}=\mathfrak B_{N-q+1}/\mathfrak D_N.} \tag{WP8}
\]

The ordinary monic recurrence and moment-determinant background is [DLMF §18.2(iv)](https://dlmf.nist.gov/18.2.iv) and [§18.2(ix)](https://dlmf.nist.gov/18.2.ix); the specific arithmetic relation determinant is the supplied construction, not a conclusion attributed to DLMF. Thus WP3 equals

\[
E\le\left(\frac{\Lambda_{n+r}^{\rm sc}}{\Lambda_n^{\rm sc}}\right)^{1/(2r)}
=\left(\frac{\mathfrak B_{n+r-q+1}\mathfrak D_n}
{\mathfrak D_{n+r}\mathfrak B_{n-q+1}}\right)^{1/(2r)}. \tag{WP9}
\]

PR24's complete transfer note, equations (4)–(5), defines \(F_a\) using raw derivatives of the real monic source polynomials at every doubled root multiplicity, with fixed row order. It proves

\[
V_N=\left(\prod_{j=a}^{N}\omega_j\right)\frac{\det\mathsf V}{\det F_a},
\qquad a=N-q+1.
\]

Consequently, setting now \(a=n-q+1\),

\[
\boxed{E\le\left[
\frac{\det F_{a+r}}{\det F_a}
\prod_{j=0}^{q-2}\frac{\omega_{a+j}}{\omega_{a+r+j}}
\right]^{1/(2r)}.} \tag{WP10}
\]

This uses two transfer determinants; at \(q=1\) the norm product is empty. The common raw confluent Vandermonde, including every derivative factorial and its coordinate phase, cancels through the displayed ratio. No absolute value is inserted: positivity follows from equality with the positive scalar ratio in WP9. The relation map still contains the unit \(i^q\), and \(F_0\) need not equal \(\mathsf V\), although their determinants agree.

Literal mass bookkeeping confirms the cancellation: rescaling the fixed measure by \(c>0\) would give \(\omega_N\mapsto c\omega_N\), \(V_N\mapsto c^qV_N\), \(\Lambda_N^{\rm sc}\mapsto c^{1-q}\Lambda_N^{\rm sc}\). Only the endpoint ratio is invariant. No such rescaling is performed here.

## 5. Immediate arithmetic consequence: threshold four

The complete Arithmetic Endpoint Bounds note proves its original lower convolution envelope and exact general norm-window bound, equations (29), (33), (34), (37). Its independently checked balanced extension yields

\[
A_{h,k,n,r}\le C_h^{\rm bal}n,\qquad n\ge k\ge3,\quad n/2\le r\le n,
\]

where, with \(b\in(0,\pi/2)\), \(B_h=42+2\deg h\), \(X_h=\max(1,M_h(b),M_h(-b))\), \(K_h=\max(1,\vartheta_h^{-1})\),

\[
C_h^{\rm bal}=256e^\pi\max(1,3/c_h)X_hK_h\max(1,b^{-3})6^{B_h/3}.
\tag{WP11}
\]

The constant is finite and depends only on the fixed packet and chosen \(b\); it is not a numerically enclosed constant. A direct check of the extension uses
\(\mathfrak l_n(n)\ge2n^{2n+1}/((2n+1)4^n)\), \((2(n+r))!\le(4n)^{2(n+r)}\), and the two moment masses before taking roots. The factorial/Legendre contribution becomes
\(4n\,8^{n/r}((2n+1)/(c_hn))^{1/(2r)}\le256n\max(1,3/c_h)\).
The remaining factors are bounded by \(X_hK_h\max(1,b^{-3})e^\pi6^{B_h/3}\), using \(2r\ge n\) and decreasing \(\log(2n)/n\) for \(n\ge3\).

For a packet consisting exactly of a hypothetical full off-line quartet of common multiplicity \(m\), the original exterior lower allowance satisfies

\[
q=q_k=[1+k(m-1)](k+1)^2,\qquad L_{h,k}\ge\delta kq/2>0,
\qquad L_{h,k}\le\epsilon_N.
\]

Choose \(n=q,r=q-1\). Here \(q\ge k\ge3\), the allowance indices are precisely \(q,\ldots,2q-2\), and the last norm/volume endpoint is \(2q-1\). WP3 and WP11 imply

\[
C_k:=\log\frac{V_q}{V_{2q-1}}
\ge2(q-1)\log\frac{\delta k}{2C_h^{\rm bal}}. \tag{WP12}
\]

The old four-volume budget obeys the exact decomposition

\[
\mathcal B_{h,k}=\log\frac{V_{q-1}V_q}{V_{2q-1}V_{2q}}
=2C_k+\log\frac{V_{q-1}}{V_q}+\log\frac{V_{2q-1}}{V_{2q}}\ge2C_k.
\]

Therefore

\[
\boxed{\mathcal B_{h,k}\ge4(q_k-1)\log\frac{\delta k}{2C_h^{\rm bal}},
\qquad \liminf_{k\to\infty}\frac{\mathcal B_{h,k}}{q_k\log k}\ge4.} \tag{WP13}
\]

The diagonal window also gives \(\liminf\log(V_q/V_{2q})/(q_k\log k)\ge2\). These lower bounds follow from the actual arithmetic norm estimate and original radius identities, not from scalar-fixture sampling. The old threshold 2 remains a valid weaker result. A separately proved \(\limsup\mathcal B_{h,k}/(q_k\log k)<4\) would now contradict the hypothetical quartet; **no such upper bound is established**. Equivalently, WP9 identifies the sufficient target \((2r)^{-1}\log(\Lambda_{n+r}^{\rm sc}/\Lambda_n^{\rm sc})-\log(kq_k)\to-\infty\), but does not prove that target for the arithmetic family.

## 6. Exact fixture and verification scope

The independently recomputed fixture is \(d\mu=7e^{-u^2/2}du/\sqrt{2\pi}\), \(\chi=u^2+1\), \(Q_{j+1}=uQ_j-jQ_{j-1}\), \(\omega_j=7j!\), and \(G_N=(\sum_{j\le N}[Q_j][Q_j]^T/\omega_j)^{-1}\). It gives exactly

\[
G_2=\operatorname{diag}(7/3,7),\quad G_3=\operatorname{diag}(7/3,21/11),\quad
G_4=\operatorname{diag}(42/43,21/11),
\]
\[
(\epsilon_2^2,\epsilon_3^2,\epsilon_4^2)=(16/3,400/99,4225/946),
\quad(V_1,\ldots,V_5)=(49,49/3,49/11,882/473,980/1333).
\]

For \(n=2,r=3\), \(\Omega=60\), \(\alpha=1/3\), \(\beta=110/279\), \(t=54/473\). The minimum, geometric mean, sharper bound and older bound are respectively approximately 2.0100756305184, 2.1407199197265, 2.1666731523012 and 2.5178436563897. Their exact underlying quantities, not these decimal strings, enter the identity checks.

A separate original exponential tilt \(\theta=1/2\) retains mass \(7e^{1/8}\). At degree 2 it gives \(\phi_2=7/129\ne0\) and \(\epsilon_2^2=18769/4128\); further nonzero phases, the independent derivative \(\sigma-\partial_\theta\log V_N\), and the whole window product are checked. The polynomial \(u^2-3\) supplies an actual interior unit contraction. A one-dimensional quotient tests zero control with potentially nonzero phase and the empty norm band in WP10. Raw derivatives at doubled nonreal nodes independently verify WP8–WP10, while the literal moment matrices verify the source/relation determinants.

The receipt separates exact symbolic/rational/data checks from four approximate decimal-display comparisons. Symbolic product factorizations were checked for \(r=1,\ldots,8\); rational phases and degeneracies, exact powered endpoint comparisons, mass scaling, full raw-jet transfers and balanced-window index/algebra checks are retained. These finite checks do not replace the written general proofs, are not arithmetic zero packets, and are not interval or Lean certificates. No Wolfram session was run or its reported execution adopted as independent evidence.

The complete submitted calculation, original TVB source sections used above, corrected PR23 endpoint note, complete PR24 transfer note, complete Arithmetic Endpoint Bounds note, balanced-window proof, and parent four-volume synthesis were read. Their immutable hashes are in `EXACT_VERIFICATION_RECEIPT.json`; no private attachment path occurs in the public derivative or receipt. Source attachments remain unchanged. The parent's `FOUR_VOLUME_THRESHOLD.md` was independently approved at SHA-256 `9ff55c84d74db85306e7a68c70fe7b08d8e642e8ac1a3e6137649f68e102fc3a`.

Selecting the finite minimizing degree keeps the existing representative \(R_N\), \(J^{(k)}R_N=\eta_{h,k}\), and \(q^{(k)}R_N=\sigma_h^{\otimes k}\eta_{h,k}\), with the same arithmetic unit, jets, cohomology classes and supported-zero/absence distinction. Endpoint data certify existence, not identification of the minimizing degree. No owner scalar-budget optimization, canonical source, frozen edition, or remote publication was changed by this review.
