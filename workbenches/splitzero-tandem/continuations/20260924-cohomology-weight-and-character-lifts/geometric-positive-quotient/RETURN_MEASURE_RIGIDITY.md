# Global inverse reconstruction of the original zeta return measures

24 September 2026. Independent derivation. Result locators RMR0–RMR10.

This note proves the converse to the programme's timed-prime reconstruction: the original Riemann zeta function determines the complete scalar count measure, its primitive periods, all repeated returns, their coefficients, and the time origin and scale. Every proof applies to the complete measure. No finite range of numerical tests enters an argument.

The supporting datum remains

\[
\tau\langle Z_1;\text{no intrinsic }Z_2\text{ parity}\rangle.
\]

The time-zero atom below records the arithmetic unit. It does not identify that atom, the real time coordinate zero, integer zero, or the supporting datum with one another. Addition and convolution below act on measures and counts; no addition on tau is introduced. In particular the retracted equation involving the sum of tau with itself is not used.

## RMR0. Sources, order of reconstruction, and the exact input

Read for this calculation:

- `work/tau_weight_cohomology_20260924/TIMED_PRIME_PERIOD_DERIVATION.md`: TP9–TP14 read in full for the measures and transforms; TP0–TP5 read for reconstruction order. The prior public proof is [TP0–TP14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/32acd0df89ae22c96d2bc30372e4426a31ce4506/workbenches/splitzero-tandem/temporary-arguments/20260924-fixed-generic-point-purity/timed-prime-reconstruction/README.md).
- `SEQUENTIAL_ARGUMENT_RECONSTRUCTION.md`, A18–A25: complete-history certification, joint reconstruction of the supporting viewpoint and unit, fixed-point and signed-norm arguments, and the proposed uniqueness-to-purity inference.

The inverse calculation starts with the full original analytic function on its original half-plane

\[
\zeta(s)=1+\sum_{n\ge2}n^{-s},\qquad \Re s>1.
\tag{RMR0.1}
\]

It does not obtain the unit by subtracting two previously named prime events. Once a measure has been recovered, its additive support determines its primitive elements intrinsically. The classical labels in the proof verify which recovered objects these are. The construction of the complete source before this analytic comparison is the subject of TP0 and the separate generic-reconstruction proof; this note does not derive that source from a bare supporting point.

No completed zeta function is substituted for (RMR0.1). Gamma factors, powers of pi and endpoint multipliers are absent because none is introduced. Later meromorphic continuation is that of this same original function.

## RMR1. The three complete measures and their transforms

On \([0,\infty)\), retain

\[
\begin{aligned}
\mathcal D&=\delta_0+\sum_{n\ge2}\delta_{\log n},\\
\mathcal R&=\sum_p\sum_{k\ge1}\frac1k\delta_{k\log p},\\
\mathcal W&=t\mathcal R
=\sum_p\sum_{k\ge1}\frac{k\log p}{k}\delta_{k\log p}
=\sum_p\sum_{k\ge1}(\log p)\delta_{k\log p}.
\end{aligned}
\tag{RMR1.1}
\]

The last two measures have mass zero at time zero. On any compact interval \([0,T]\), an atom of \(\mathcal D\) has \(n\le e^T\); an atom of \(\mathcal R\) or \(\mathcal W\) has \(p^k\le e^T\). Consequently all three measures are locally finite.

For \(\sigma\ge1+\delta>1\),

\[
\sum_p\sum_{k\ge1}\frac{p^{-k\sigma}}k
\le \frac{1}{1-2^{-1-\delta}}\sum_{n\ge2}n^{-1-\delta}<\infty,
\]

\[
\sum_p\sum_{k\ge1}(\log p)p^{-k\sigma}
\le \frac{1}{1-2^{-1-\delta}}
\sum_{n\ge2}(\log n)n^{-1-\delta}<\infty.
\tag{RMR1.2}
\]

The second last series converges by the integral test, or by comparing its tail with \(n^{-1-\delta/2}\). These majorants give absolute and locally uniform convergence. Define the branch

\[
L(s):=\sum_p\sum_{k\ge1}\frac{p^{-ks}}k.
\tag{RMR1.3}
\]

The power-series identity \(\exp(\sum_{k\ge1}z^k/k)=(1-z)^{-1}\), followed by unique factorization and the convergent Euler product, gives

\[
\mathcal L\mathcal D(s)=\zeta(s),\qquad
\mathcal L\mathcal R(s)=L(s),\qquad
e^{L(s)}=\zeta(s),\qquad
\mathcal L\mathcal W(s)=-\frac{\zeta'(s)}{\zeta(s)}.
\tag{RMR1.4}
\]

Here \(\mathcal L\mu(s)=\int e^{-st}\,d\mu(t)\), and all four identities hold on \(\Re s>1\). Differentiation in the last identity retains the factor \(k\log p\) multiplying the coefficient \(1/k\), as shown in (RMR1.1). The logarithm is specified by (RMR1.3), equivalently by its real values for real \(s>1\) and its limit zero as \(s\to+\infty\). It is not an unspecified branch.

For completeness, the needed Euler product can be checked globally without a numerical approximation. A product over the primes at most \(N\) expands into the Dirichlet terms whose prime factors are all at most \(N\). Unique factorization supplies coefficient one to each such term. Every omitted integer exceeds \(N\), so on \(\Re s\ge1+\delta\) the absolute remainder is at most \(\sum_{n>N}n^{-1-\delta}\), which tends to zero. This proves the equality for the entire infinite product. The bound is a convergence proof, not a finite verification of a global assertion.

## RMR2. Injectivity of the complete Laplace observation

Let \(\mathscr M_1^+\) be the set of positive Borel measures \(\mu\) on \([0,\infty)\) which are locally finite and satisfy

\[
\int_0^\infty e^{-ct}\,d\mu(t)<\infty
\quad\text{for every real }c>1.
\tag{RMR2.1}
\]

**Theorem.** The map \(\mu\mapsto\mathcal L\mu\) is injective on \(\mathscr M_1^+\). More strongly, for any one fixed \(c>1\), the values \(\mathcal L\mu(c+j)\), \(j=0,1,2,\ldots\), determine \(\mu\).

**Proof.** Define a finite positive measure on \([0,1]\) by

\[
\nu_{\mu,c}:=(t\mapsto e^{-t})_*\bigl(e^{-ct}\mu\bigr),
\qquad \nu_{\mu,c}(\{0\})=0.
\tag{RMR2.2}
\]

For every nonnegative integer \(j\),

\[
\int_{[0,1]}x^j\,d\nu_{\mu,c}(x)=\mathcal L\mu(c+j).
\tag{RMR2.3}
\]

Equal Laplace values therefore give equal integrals of every polynomial. These imply equal integrals of every continuous function. Here is the approximation argument explicitly. For \(f\in C([0,1])\), its Bernstein polynomial is

\[
B_Nf(x)=\sum_{k=0}^N f(k/N)\binom Nk x^k(1-x)^{N-k}.
\]

If \(K\) has binomial law with parameters \(N,x\), this is \(\mathbb E f(K/N)\), while
\(\mathbb E(K/N-x)^2=x(1-x)/N\le1/(4N)\). Given \(\varepsilon>0\), uniform continuity provides \(\eta>0\) such that \(|f(y)-f(x)|<\varepsilon\) when \(|y-x|<\eta\). Splitting the expectation at that event and using the second-moment bound gives uniformly in \(x\)

\[
|B_Nf(x)-f(x)|
\le\varepsilon+\frac{2\|f\|_\infty}{4N\eta^2}.
\]

Thus the polynomials converge uniformly. Finite measures with equal polynomial integrals have equal continuous-function integrals. To see the last measure-identification step directly, continuous ramps increasing pointwise to the indicator of any open interval give its measure by monotone convergence; intervals determine the Borel measure. Hence \(\nu_{\mu,c}=\nu_{\lambda,c}\).

The transformation (RMR2.2) has the exact inverse

\[
\mu(E)=\int_{\{e^{-t}:t\in E\}}x^{-c}\,d\nu_{\mu,c}(x)
\tag{RMR2.4}
\]

for every Borel \(E\subseteq[0,\infty)\). The integrand is bounded on the image of any bounded \(E\); the identity for unbounded sets follows by monotone convergence. Equality of the \(\nu\)'s therefore proves equality of the original measures. \(\square\)

This also gives an explicit inverse on continuous test functions, without selecting atom locations in advance:

\[
\begin{aligned}
\int f\,d\nu_{\mu,c}
=\lim_{N\to\infty}\sum_{k=0}^N f(k/N)\binom Nk
\sum_{j=0}^{N-k}(-1)^j\binom{N-k}{j}
\mathcal L\mu(c+k+j).
\end{aligned}
\tag{RMR2.5}
\]

Indeed, expanding each \((1-x)^{N-k}\) in \(B_Nf\) gives the finite sum, and uniform convergence gives its limit. Equations (RMR2.4)–(RMR2.5) reconstruct the full measure from the full observation.

## RMR3. The converse for the original zeta and its unit

**Theorem.** Among all measures in \(\mathscr M_1^+\), precisely one has Laplace transform the original \(\zeta(s)\) on \(\Re s>1\), namely

\[
\boxed{\mathcal D=\delta_0+\sum_{n\ge2}\delta_{\log n}.}
\tag{RMR3.1}
\]

**Proof.** RMR1 establishes existence and RMR2 establishes uniqueness. In fact equality only at \(c,c+1,c+2,\ldots\) already suffices. This is an infinite exact observation, not a finite event prefix. \(\square\)

The unit atom is itself recoverable. For any \(\mu\in\mathscr M_1^+\), fix \(c>1\). As real \(s\to+\infty\), the functions \(e^{-st}\), for \(s\ge c\), are dominated by the integrable \(e^{-ct}\) and tend pointwise to \(\mathbf1_{\{0\}}(t)\). Consequently

\[
\mu(\{0\})=\lim_{s\to+\infty}\mathcal L\mu(s).
\tag{RMR3.2}
\]

For the original zeta that limit is exactly one: its terms with \(n\ge2\) tend to zero and are dominated by the convergent series at any fixed real \(c>1\). Thus the complete analytic observation fixes both the unit's time and its multiplicity. This is a statement about \(\delta_0\); tau remains the separately retained supporting datum.

The conclusion is a reconstruction of the actual infinite measure. It does not certify that measure from finitely many observations. For example, for any \(T>0\) and any \(u>T\), the positive measure \(\mathcal D+\delta_u\) has exactly the same restriction to \([0,T]\) and has all the required exponential moments, but its transform is \(\zeta(s)+e^{-su}\). This is the exact map that retains the user's later-event possibility: a finite time restriction has a nontrivial fibre, whereas the complete Laplace observation does not.

## RMR4. Recovering repeated returns by a convolution logarithm

Convolution is taken under addition of nonnegative real times. Thus

\[
\delta_a*\delta_b=\delta_{a+b},\qquad \delta_0*\mu=\mu.
\tag{RMR4.1}
\]

For \(\mathcal M:=\mathcal D-\delta_0\), the support lies in \([h,\infty)\) with \(h=\log2>0\). Define

\[
\log_*\mathcal D
=\sum_{r\ge1}\frac{(-1)^{r+1}}r\mathcal M^{*r}.
\tag{RMR4.2}
\]

This signed sum is locally finite: \(\mathcal M^{*r}\) is supported in \([rh,\infty)\), so only finitely many \(r\) contribute on any fixed compact interval. Each of these convolution measures has finitely many atoms there. No convergence assertion or sign inference is hidden in the definition.

**Theorem.** The logarithm (RMR4.2) is positive and is exactly \(\mathcal R\) in (RMR1.1). Its inverse map is

\[
\exp_*\mathcal R
=\delta_0+\sum_{r\ge1}\frac{\mathcal R^{*r}}{r!}
=\mathcal D.
\tag{RMR4.3}
\]

**Proof.** On \([0,T]\), discard contributions supported strictly after \(T\). This is the quotient of the convolution algebra by the ideal of such contributions. Its positive-time part generated by measures with support at least \(h\) is nilpotent: a product of more than \(T/h\) factors is zero there. Therefore exponential and logarithm are finite polynomial operations in this quotient. The formal identities
\(\log(\exp X)=X\), \(\exp(\log(1+X))=1+X\), and
\(\exp(X+Y)=\exp X\exp Y\) hold in it. They follow by differentiation of the formal series, their constant terms, and the product rule; all coefficients have rational denominators and commute.

For a fixed prime the identity

\[
\exp_*\left(\sum_{k\ge1}\frac1k\delta_{k\log p}\right)
=\sum_{j\ge0}\delta_{j\log p}
\tag{RMR4.4}
\]

is obtained from \(\exp(\sum_{k\ge1}X^k/k)=(1-X)^{-1}\) by substituting \(X^k\mapsto\delta_{k\log p}\). Products over prime factors give exactly one atom at each \(\log n\), including the exponent-zero tuple giving \(\delta_0\). On \([0,T]\), only primes at most \(e^T\) enter. This is a finite product in the quotient just described. It proves (RMR4.3) on every compact interval, hence globally. Applying its polynomial inverse gives (RMR4.2) equal to \(\mathcal R\). Its coefficients \(1/k\) are positive, proving positivity rather than assuming it for a convolution logarithm. \(\square\)

In particular, the inverse formula yields the exact coefficient identity, for every integer \(n\ge2\),

\[
\sum_{r\ge1}\frac{(-1)^{r+1}}r
\#\{(d_1,\ldots,d_r):d_i\ge2,\ d_1\cdots d_r=n\}
=\begin{cases}1/k,&n=p^k,\\0,&n\text{ has at least two distinct prime factors.}\end{cases}
\tag{RMR4.5}
\]

The sum is finite because \(2^r\le n\). The proof above verifies this identity for every \(n\); no range of values is substituted for it.

## RMR5. Primitive periods, repetitions and arithmetic are recovered intrinsically

Let \(M=\operatorname{supp}\mathcal D\), with its addition inherited from time. This is the additive monoid \(\{\log n:n\ge1\}\), with neutral element zero. Define its positive irreducibles without using prime labels:

\[
P(M)=\{t\in M\setminus\{0\}:t\ne a+b\text{ for all }a,b\in M\setminus\{0\}\}.
\tag{RMR5.1}
\]

**Theorem.** The recovered set \(P(M)\) is precisely \(\{\log p:p\text{ prime}\}\). Every element of \(M\) has a unique expression as a finite sum of these primitive elements with nonnegative integral multiplicities.

**Proof.** If \(n=ab\) with \(a,b>1\), then \(\log n=\log a+\log b\), so \(\log n\) is reducible. Conversely an equality \(\log n=\log a+\log b\) exponentiates to \(n=ab\); if \(n\) is prime, one factor must be one and the corresponding summand zero.

Here is the arithmetic existence and uniqueness argument used throughout this note. Every integer greater than one has a least divisor greater than one, and that divisor is prime: a proper factor of the divisor would contradict its minimality. Induction on the integer gives a finite prime factorization by factoring a composite into two smaller positive integers. To prove uniqueness, Euclidean division gives the Euclidean algorithm; the successive nonzero remainders strictly decrease, and tracing its equations backwards expresses their last nonzero member, the greatest common divisor, as an integral linear combination of the two inputs. If a prime \(p\) does not divide \(a\), its greatest common divisor with \(a\) is one, so \(up+va=1\) for some integers \(u,v\). Multiplying this equation by \(b\) proves that \(p\mid ab\) implies \(p\mid b\). Applying this lemma repeatedly to a product shows that a prime in either factorization must equal a prime in the other; cancelling that equal factor and inducting proves uniqueness of every multiplicity. Taking real logarithms supplies exactly the asserted unique finite sum. This proves the intrinsic classification and its arithmetic comparison. \(\square\)

An entirely equivalent recovery uses \(\mathcal R\): its primitive positive atoms are the atoms not equal to an integer multiple \(k\ge2\) of another positive atom. Indeed, \(k\log p\) with \(k\ge2\) is visibly a repetition, while \(\log p=j\ell\log q\) would give \(p=q^{j\ell}\), impossible for \(j\ell\ge2\). Thus the time and repetition number are reconstructed before their conventional prime-power names are attached.

The exact monoid isomorphism is

\[
\bigoplus_{a\in P(M)}\mathbb N_0\longrightarrow M,
\qquad (k_a)_a\longmapsto\sum_a k_a a.
\tag{RMR5.2}
\]

Its inverse records the unique multiplicities. The empty tuple maps to time zero, retaining the unit. The exponential map \(t\mapsto e^t\) then identifies this with the positive-integer multiplicative monoid, including integer one. The order inherited from time orders its countable elements and identifies the complete sequence of counts. This comparison uses all of \(M\); it does not claim that a finite prefix certifies the whole source.

The measure \(\mathcal W\) has two exact reconstructions:

\[
\mathcal W=t\log_*\mathcal D,
\qquad
\mathcal W=(t\mathcal D)*\mathcal D^{-1},
\tag{RMR5.3}
\]

where

\[
\mathcal D^{-1}=\sum_{r\ge0}(-1)^r\mathcal M^{*r}
=\sum_{n\ge1}\mu_{\rm ar}(n)\delta_{\log n}.
\tag{RMR5.4}
\]

Here \(\mu_{\rm ar}\) is the integer Möbius function: coefficient zero when a prime is repeated and coefficient \((-1)^r\) for a product of \(r\) distinct primes; its value at one is one. To prove (RMR5.4), invert each prime factor \(\sum_{j\ge0}\delta_{j\log p}\) by \(\delta_0-\delta_{\log p}\); multiply, and use unique factorization on each compact interval. The alternating geometric sum gives the same inverse.

Finally, multiplication by time is a derivation of convolution:

\[
t(\mu*\nu)=(t\mu)*\nu+\mu*(t\nu),
\]

because the product time is the sum of its two input times. Apply this to the finite local exponential expansion to obtain
\(t\exp_*\mathcal R=(t\mathcal R)*\exp_*\mathcal R\). This proves the second formula in (RMR5.3). In coefficients it retains

\[
\sum_{d\mid n}(\log d)\mu_{\rm ar}(n/d)=\Lambda(n),
\quad
\Lambda(p^k)=\log p,\quad \Lambda(1)=0.
\tag{RMR5.5}
\]

## RMR6. Converse uniqueness for both repeated-return transforms

**Theorem.** The following three sets each contain exactly the displayed measure:

\[
\begin{aligned}
\{\nu\in\mathscr M_1^+:\mathcal L\nu=L\}&=\{\mathcal R\},\\
\{\nu\in\mathscr M_1^+:\exp(\mathcal L\nu)=\zeta\}&=\{\mathcal R\},\\
\{\nu\in\mathscr M_1^+:\mathcal L\nu=-\zeta'/\zeta\}&=\{\mathcal W\}.
\end{aligned}
\tag{RMR6.1}
\]

The transform identities in each set are on \(\Re s>1\).

**Proof.** Existence was proved in RMR1; the first and third uniqueness statements are RMR2. In the second statement, for every real \(s>1\), \(\mathcal L\nu(s)\) is a finite nonnegative real number. The real exponential is injective and \(L(s)\) is the real logarithm of \(\zeta(s)\). Therefore \(\mathcal L\nu(s)=L(s)\) on that real half-line. RMR2 applies again. In particular no atom at time zero can be added: it would multiply the real exponential by a positive constant different from one. \(\square\)

The precise inverse between the last two measures is multiplication by \(t\) and multiplication by \(1/t\) on \((0,\infty)\), together with their established zero masses at zero. These are genuine mutually inverse maps on the measures in question. They do not add a time-zero contribution to a logarithmic derivative whose coefficient there is zero. The arithmetic unit is recovered in passing back to \(\exp_*\mathcal R\).

## RMR7. Global rigidity of time origin and scale

For \(a>0\) and \(b\in\mathbb R\), push \(\mathcal D\) along the affine clock change \(A_{a,b}(t)=at+b\). Allow a target real half-line bounded below, so the proof does not silently exclude shifts of either sign. Its transform, on the common half-plane of convergence, is exactly

\[
\mathcal L\bigl((A_{a,b})_*\mathcal D\bigr)(s)
=e^{-bs}\zeta(as).
\tag{RMR7.1}
\]

**Theorem.** Equality of (RMR7.1) with the original \(\zeta(s)\) for all sufficiently large real \(s\) forces \(b=0\) and \(a=1\).

**Proof.** Both \(\zeta(as)\) and \(\zeta(s)\) tend to one as real \(s\to+\infty\). Therefore \(e^{-bs}=\zeta(s)/\zeta(as)\) tends to one, forcing \(b=0\). For real \(x>1\), the original Dirichlet series is strictly decreasing: if \(y>x\), every term \(n^{-y}\) is at most \(n^{-x}\), and the inequality is strict for every \(n\ge2\); the absolutely convergent positive sums preserve strictness. Hence \(\zeta(as)=\zeta(s)\), at any real \(s\) with \(s>1\) and \(as>1\), implies \(as=s\), so \(a=1\). \(\square\)

The same conclusion holds for every order-preserving additive bijection of real nonnegative time. Such a map \(h\) satisfies \(h(t)=ct\), \(c>0\). To prove this, additivity gives the formula on nonnegative rational arguments from \(h(1)=c\); rational sequences increasing and decreasing to any real \(t\), together with monotonicity, give the formula there. RMR7 then fixes \(c=1\).

For the intrinsic return-time monoid \(M\), any order-preserving monoid automorphism is already the identity: it must fix the least element, the next element, and, inductively, every element in the increasing sequence, since the increasing bijection of this sequence cannot skip a position. This induction proves a statement about the whole automorphism, rather than certifying an unknown whole history from a finite record.

## RMR8. What a scalar return observation retains about time between events

The preceding rigidity concerns the actual additive clock and every event time. To specify its precise strength, consider only an increasing homeomorphism of ambient time, without assuming it respects addition. There exist such maps preserving the entire count measure but changing the intervals between its atoms.

Here is one complete construction. For every \(n\ge1\), put \(a_n=\log n\), \(d_n=\log(n+1)-\log n\), and define on \([a_n,a_{n+1}]\)

\[
h(t)=a_n+d_n\psi\left(\frac{t-a_n}{d_n}\right),
\qquad
\psi(x)=x+\frac{1}{4\pi}\sin(2\pi x).
\tag{RMR8.1}
\]

The endpoints agree between adjacent intervals, \(\psi(0)=0\), \(\psi(1)=1\), and
\(\psi'(x)=1+\tfrac12\cos(2\pi x)\ge\tfrac12\). Hence \(h\) is an increasing homeomorphism of \([0,\infty)\), fixes every \(\log n\), and satisfies \(h_*\mathcal D=\mathcal D\). It is not the identity inside these intervals and cannot be additive by RMR7's classification. This preserves rather than changes every event time and coefficient.

Thus the scalar original zeta recovers the event measure exactly, and the additive structure fixes its clock scale. The ambient interpolation of time is additional structure. Formula (RMR8.1) identifies exactly the observation fibre exposed by omitting that structure; it says nothing against the source's already supplied additive flow.

## RMR9. The exact map that forgets phase and support labels

The scalar measure reconstructs scalar arithmetic. Here is the explicit comparison with retained labels.

Let \(S\) be a finite label set, and let

\[
\pi:[0,\infty)\times S\longrightarrow[0,\infty),\qquad
\pi(t,\ell)=t.
\tag{RMR9.1}
\]

For a positive labelled measure \(\widetilde{\mathcal D}\), the scalar observation is \(\pi_*\widetilde{\mathcal D}\). The positive fibre over \(\mathcal D\) consists exactly of

\[
\widetilde{\mathcal D}
=\sum_{n\ge1}\delta_{\log n}\otimes\nu_n,
\qquad
\nu_n\text{ a probability measure on }S.
\tag{RMR9.2}
\]

**Proof.** Positivity and the zero scalar mass outside the count times imply zero labelled mass there. Above each count time, the total labelled mass must be the scalar coefficient one. That is exactly a probability measure on the finite fibre. Conversely every such family pushes to \(\mathcal D\), and local finiteness follows from that of \(\mathcal D\). \(\square\)

For the retained quarter-phase group

\[
H=\{1,J,\epsilon,\epsilon J\},\qquad
J^2=\epsilon,\quad \epsilon^2=1,
\]

there are labelled lifts which retain multiplication and the complete convolution exponential as well. Choose any monoid homomorphism
\(\chi:(\mathbb N_{>0},\cdot)\to H\). Its value at one is the identity. Define

\[
\begin{aligned}
\mathcal D_\chi&=\sum_{n\ge1}\delta_{(\log n,\chi(n))},\\
\mathcal R_\chi&=\sum_p\sum_{k\ge1}\frac1k
\delta_{(k\log p,\chi(p)^k)}.
\end{aligned}
\tag{RMR9.3}
\]

Convolution on this labelled space uses
\((t,h)(u,j)=(t+u,hj)\). Unique factorization and the proof of RMR4, with this multiplication retained, give

\[
\mathcal D_\chi=\exp_*\mathcal R_\chi,
\qquad
\pi_*\mathcal D_\chi=\mathcal D,
\qquad
\pi_*\mathcal R_\chi=\mathcal R.
\tag{RMR9.4}
\]

For every primitive prime period, its assigned phase can be specified in \(H\) and then extended uniquely by multiplication. Assigning a nonidentity phase to one primitive period produces a measure different from the all-identity assignment, with the same scalar transform and the same unit atom. This establishes the precise information lost by scalarization. It does not assert that every such assignment meets every additional condition of the Connes–Consani geometry.

In coefficient notation, the projection is the augmentation

\[
\operatorname{aug}:\mathbb Z[H]\longrightarrow\mathbb Z,
\quad\sum_{h\in H}a_h[h]\longmapsto\sum_{h\in H}a_h,
\]

\[
\ker(\operatorname{aug})
=\bigoplus_{h\in H\setminus\{1\}}\mathbb Z\bigl([h]-[1]\bigr).
\tag{RMR9.5}
\]

The kernel formula follows by rewriting a sum with total coefficient zero as
\(\sum_{h\ne1}a_h([h]-[1])\); the three displayed generators are linearly independent by inspecting their nonidentity coefficients. The map respects multiplication because each basis group element maps to one. The same formula over rational coefficients accommodates the retained return coefficient \(1/k\).

If a support label is retained alongside the phase, use \([0,\infty)\times S\times H\) and the same projection to time. The resulting scalar formula does not identify distinct support labels with one another; it observes them through a map having the fibre (RMR9.2). A prescribed supporting point can be held fixed in every term, so the scalar reconstruction is fully compatible with retaining that point. Recovering the whole support-labelled programme requires its additional labelled observations or the source's proven reconstruction maps, not a silent replacement of those objects by their scalar image.

## RMR10. The proved consequence for the complete-history argument

The following is now an exact chain of mutually recovering arithmetic data:

\[
\begin{array}{ccccc}
\mathcal D&\xrightarrow{\log_*}&\mathcal R&\xrightarrow{\;t\cdot\;}&\mathcal W\\
\mathcal L\downarrow&&\mathcal L\downarrow&&\mathcal L\downarrow\\
\zeta&\xrightarrow{\text{the branch }L(+\infty)=0}&L
&\xrightarrow{-\partial_s}&-\zeta'/\zeta.
\end{array}
\tag{RMR10.1}
\]

Inverses are respectively convolution exponential, division by positive time with the zero atom prescribed as above, and the injective Laplace reconstruction RMR2. The left-hand unit atom has coefficient one. Additive irreducibles of its complete support recover every primitive period; RMR4 recovers every repetition coefficient. The original zeta also fixes every affine origin and scale by RMR7.

This proves a global uniqueness statement stronger than uniqueness of an identity inside a previously chosen algebra: no different positive scalar measure with the stated exponential moments has the same complete original-zeta observation. In particular a proposed later event outside that measure changes the original function, by RMR2, even when it leaves every earlier time restriction unchanged.

It also states the remaining comparison exactly. The scalar measure is an image of the full support- and phase-labelled history. Its inverse is unique in the scalar measure category; (RMR9.2)–(RMR9.5) describe the fibre of the labelled-to-scalar map. These formulas retain the supporting datum, the quarter phases, and their relationship to the unique scalar arithmetic observation, without asserting that equality of one scalar transform identifies arbitrary geometries.

Once the original zeta is recovered on \(\Re s>1\), its meromorphic continuation, wherever supplied, is unique: two meromorphic continuations on a connected common domain that agree on this open half-plane agree everywhere there by the identity theorem. Thus the continuation has the same original zeros, poles and multiplicities. No completion multiplier is introduced, and none of its exceptional loci is cancelled by this argument. The inverse theorem does not place those zeros on a line; its proved contribution is the complete global rigidity of the arithmetic return data that any subsequent purity argument must use.
