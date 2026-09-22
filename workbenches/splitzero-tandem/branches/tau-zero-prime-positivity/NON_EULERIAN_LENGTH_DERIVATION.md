# The logarithmic arithmetic distribution of the separated-support zeta sheet

This calculation uses the actual interpolation in the programme's *Secondary Note on Split-Zero Globalization*, canonical source PUBUNIT-B1A260A5E731EA568C353AA4, equations under `def:hurwitz-specialization`, `thm:universal-taylor-deformation`, `thm:arithmetic-kernels-riemann`, and `cor:first-log-jet-explicit`. It also uses *Split-Zero Support Repair*, `some considerrations.tex`, sections “Conservative ideal and zeta side” and “Shifted zeta deformation”. These are prior programme results. The supported-zero prime is also a prior result of Paper 1, attributed by the user to Gemini Pro 2.5. The calculation below derives the signed arithmetic distribution that replaces the prime-power distribution for this particular separated sheet. It does not assign an arbitrary finite norm to the supported-zero prime.

## NL1. The original scalar maps and the actual analytic family

Let \(R=\mathbb Z\), and let \(G(R)=R\sqcup\{\tau\}\). Addition and multiplication on supported elements are their ring operations; \(\tau+x=x\) and \(\tau x=\tau\). Write \(e=0_R\), so \(e\ne\tau\), \(e^2=e\), and \(er=e\) for every supported \(r\). The two maps
\[
p:G(R)\to R,\quad p(r)=r,\ p(\tau)=0,
\qquad
\chi:G(R)\to\mathbb B,\quad \chi(r)=1,\ \chi(\tau)=0
\tag{NL1}
\]
preserve both operations and units, directly by these laws. The prime ideal \((e)=\{\tau,e\}\) is \(p^{-1}(0)\); its complement consists of nonzero integers and is multiplicatively closed. This proves its primality without identifying its generator with the semiring zero.

The separated residue map \(G(\mathbb Z)\to G(\mathbb Z/n\mathbb Z)\), obtained by reducing the supported amplitude and keeping \(\tau\), has target cardinality \(n+1\). This holds also for \(n=1\): the zero ring has a supported zero and the distinct \(\tau\). Composing with amplitude gives \(\mathbb Z/n\mathbb Z\), of cardinality \(n\). Thus the two defined sums are
\[
F_0(s)=\sum_{n\ge1}n^{-s}=\zeta(s),\qquad
F_1(s)=\sum_{n\ge1}(n+1)^{-s}=\zeta(s)-1.
\tag{NL2}
\]
Their interpolation is
\[
F_t(s)=\sum_{n\ge1}(n+t)^{-s}=\zeta(s,1+t),\qquad t\ge0,\quad\Re s>1.
\tag{NL3}
\]
Here \(t\) is a real shift parameter, not the semiring element \(\tau\). The equality with Hurwitz zeta is the defining series with its index translated; compare the original TeX formulas at [DLMF 25.11.1](https://dlmf.nist.gov/25.11.E1) and [25.11.3](https://dlmf.nist.gov/25.11.E3).

The prime \((e)\) cannot be inserted into the old ideal Euler product with a positive finite multiplicative norm extending the integer ideal norm. Indeed \((e)I_{(n)}=(e)\); a multiplicative norm \(h\) would satisfy \(h((e))=n h((e))\), so \(h((e))=0\) for \(n=2\). This equality specifies the obstruction. The separated residue sum (NL3) is a different, already defined analytic receiver of support. Its logarithmic distribution is now calculated in full.

## NL2. A convergent expansion with every multiplicative interaction retained

Put
\[
b=1+t,\qquad r_n=\frac{n+t}{1+t}\quad(n\ge2),\qquad
H_t(s)=\sum_{n\ge2}r_n^{-s}.
\tag{NL4}
\]
Every \(r_n>1\), and
\[
F_t(s)=b^{-s}(1+H_t(s)).
\tag{NL5}
\]
There exists \(\sigma_0>1\) with \(H_t(\sigma_0)<1\). To prove this, fix any \(\sigma_1>1\). The terms \(r_n^{-\sigma}\) tend to zero as \(\sigma\to\infty\), and for \(\sigma\ge\sigma_1\) they are dominated by the summable sequence \(r_n^{-\sigma_1}\). Dominated convergence gives \(H_t(\sigma)\to0\).

On every closed half-plane \(\Re s\ge\sigma_0\) with \(H_t(\sigma_0)<1\), the series
\[
\log F_t(s)=-s\log b+
\sum_{k\ge1}\frac{(-1)^{k+1}}{k}
\sum_{n_1,\ldots,n_k\ge2}
(r_{n_1}\cdots r_{n_k})^{-s}
\tag{NL6}
\]
uses the holomorphic logarithm of \(1+H_t\) defined by its power series. Its absolute sum is at most \(\sum_{k\ge1}H_t(\sigma_0)^k/k<\infty\). Differentiation is locally uniformly justified: for a slightly smaller abscissa still exceeding 1 and with \(H_t<1\),
\[
J_t(\sigma)=\sum_{n\ge2}(\log r_n)r_n^{-\sigma}<\infty,
\]
and the absolute sum of the differentiated length terms of length \(k\), after the factor \(1/k\), is \(J_t(\sigma)H_t(\sigma)^{k-1}\). Summing this geometric bound proves
\[
-\frac{F_t'(s)}{F_t(s)}
=\log b+
\sum_{k\ge1}\frac{(-1)^{k+1}}{k}
\sum_{n_1,\ldots,n_k\ge2}
\log(r_{n_1}\cdots r_{n_k})
(r_{n_1}\cdots r_{n_k})^{-s}.
\tag{NL7}
\]
No factor indexed by an ordinary prime has been assumed.

Define the signed measure on \([0,\infty)\)
\[
\nu_t=(\log b)\delta_0+
\sum_{k\ge1}\frac{(-1)^{k+1}}k
\sum_{n_1,\ldots,n_k\ge2}
\ell(n_1,\ldots,n_k)\delta_{\ell(n_1,\ldots,n_k)},
\quad
\ell(n_1,\ldots,n_k)=\sum_i\log r_{n_i}.
\tag{NL8}
\]
It is locally finite: if \(\ell\le M\), then \(k\le M/\log r_2\), and every \(r_{n_i}\le e^M\), leaving finitely many tuples. Equal lengths are added with their exact signed multiplicities. The same bound proving (NL7) gives \(\int e^{-\sigma\ell}|d\nu_t|<\infty\) in the stated right half-plane. Its Laplace transform is exactly \(-F_t'/F_t\).

## NL3. An explicit negative arithmetic atom at the separated endpoint

At \(t=1\), \(b=2\), \(r_n=(n+1)/2\), and
\[
H_1(4)=\sum_{m\ge3}(2/m)^4
\le\frac{16}{81}+\int_3^\infty16x^{-4}\,dx
=\frac{32}{81}<1.
\tag{NL9}
\]
Thus (NL7) holds, in particular, for \(\Re s\ge4\), with the convergence estimate just proved. There is a positive atom
\[
\nu_1(\{\log(3/2)\})=\log(3/2).
\tag{NL10}
\]
Only the one-term tuple \(n_1=2\) has that length: a tuple of at least two terms has product at least \((3/2)^2\).

There is also the exact negative atom
\[
\boxed{\nu_1(\{\log(9/4)\})=-\log(3/2).}
\tag{NL11}
\]
For a one-term tuple, \((n+1)/2=9/4\) would give \(n=7/2\), impossible. A tuple of at least three terms has product at least \(27/8>9/4\). For two terms both factors are at least \(3/2\), so equality forces both to be \(3/2\), that is, the single ordered tuple \((2,2)\). Its coefficient in (NL8) is \(-\tfrac12\log(9/4)=-\log(3/2)\). This proves (NL11) with no truncation.

Consequently the logarithmic arithmetic distribution for the actual separated sheet is signed. The original von Mangoldt distribution, \(\sum_{n\ge2}\Lambda(n)\delta_{\log n}\), cannot be reused for this sheet. The negative atom alone is not a negative value of the full Weil form: the gamma, divisor, reflection-defect, and boundary terms of a complete contour identity must also be retained. It is an exact arithmetic coefficient that such an identity must contain.

## NL4. The first infinitesimal is nonzero and contains mixed prime data

For \(|t|<1\), the binomial series gives, locally uniformly for \(\Re s>1\),
\[
F_t(s)=\zeta(s)-t\,s\zeta(s+1)+O(t^2).
\tag{NL12}
\]
For completeness, fix a compact set of \(s\) and a radius \(r<1\). The Taylor remainder in \((1+t/n)^{-s}\) is bounded by a constant times \(|t|^2/n^2\), uniformly on that compact set; after multiplication by \(n^{-s}\) it is summable. This proves the asserted termwise expansion and its holomorphic derivatives.

The Euler product of \(\zeta\), used only at \(t=0\), gives
\[
Q(s)=\frac{\zeta(s+1)}{\zeta(s)}
=\sum_{n\ge1}\alpha(n)n^{-s},\qquad
\alpha(1)=1,\quad
\alpha(n)=(-1)^{\omega(n)}\frac{\prod_{p\mid n}(p-1)}{n}.
\tag{NL13}
\]
Indeed the local series is
\[
\frac{1-p^{-s}}{1-p^{-s-1}}
=1-\sum_{j\ge1}\frac{p-1}{p^j}p^{-js}.
\]
Its absolute product converges for \(\Re s>1\); multiplying the series proves (NL13). Thus
\[
\left.\partial_t\log F_t(s)\right|_{t=0}=-sQ(s),
\qquad
\left.\partial_t\left(-\frac{F_t'}{F_t}\right)\right|_{t=0}
=Q(s)+sQ'(s)
=\sum_{n\ge1}\alpha(n)(1-s\log n)n^{-s}.
\tag{NL14}
\]
The derivative series is absolutely convergent on compact subsets of \(\Re s>1\), since \(|\alpha(n)|\le1\) and \(\sum(1+\log n)n^{-\sigma}<\infty\). For real \(s>1\), \(sQ(s)>0\), so the first deformation of \(\log F_t\) does not vanish. This infinitesimal is not the first-order-trivial node deformation from the observed collision.

Equation (NL14) is equivalently the Laplace transform of the locally finite distribution
\[
\dot\nu_0=
\sum_{n\ge1}\alpha(n)
\bigl(\delta_{\log n}-(\log n)\delta'_{\log n}\bigr).
\tag{NL15}
\]
Here \(\langle\delta'_\ell,f\rangle=-f'(\ell)\), so its Laplace transform is \(s e^{-s\ell}\). This fixes the derivative sign in (NL15).

The dot also denotes the actual distributional derivative of (NL8), not only a matching transform. On a fixed compact length interval and for \(0\le t\le1\), the inequalities \(r_2(t)\ge3/2\) and \(r_n(t)\ge(n+1)/2\) give a uniform finite bound on the tuples which can enter. Differentiating their smooth moving atoms therefore defines the derivative on every compactly supported smooth test. For weighted Laplace tests, \(|\partial_t\log r_n|\le1\). A tuple of length \(k\) has length derivative bounded by \(k\); differentiating its coefficient and its exponential introduces at most one further factor \(k\), together with its original length. On a sufficiently far right half-plane, uniformly in a neighborhood of zero, the sums are bounded by geometric series of the forms \(\sum k B^k\) and \(\sum k D B^{k-1}\), with \(B<1\) and \(D<\infty\) as above. Thus Laplace transformation commutes with differentiation. At zero all tuple lengths are logs of positive integers. The resulting distribution has the form \(\sum_n(a_n\delta_{\log n}+b_n\delta'_{\log n})\). These coefficients are uniquely determined by its Laplace transform: multiply the difference of two such transforms by the exponential of its least remaining length and let the real argument tend to infinity; the leading polynomial of degree at most one must be zero, and induction removes every length. The exponentially weighted convergence just proved bounds the remaining tail in each step. Comparing with (NL14) proves exactly \(a_n=\alpha(n)\), \(b_n=-(\log n)\alpha(n)\), as in (NL15).

For distinct primes \(p,q\),
\[
\alpha(pq)=\frac{(p-1)(q-1)}{pq}\ne0.
\tag{NL16}
\]
These are supported at products of distinct primes, whereas the original von Mangoldt coefficients vanish there. The deformation therefore has explicitly nonzero mixed-prime terms already at first order; they cannot be removed by keeping only a modified weight at each prime power.

## NL5. Full finite support and exact specialization

For a finite bounded distributive support lattice \(L\), the actual set is
\[
G_L(R)=\{(0,\lambda):\lambda\in L\}\cup\{(r,1_L):r\in R\}.
\tag{NL17}
\]
Let \(c=|L|-1\). Its separated residue over \(\mathbb Z/n\mathbb Z\) has \(n+c\) elements: \(n\) supported top elements and \(|L|-1\) lower support elements. Hence its scalar cardinality receiver is
\[
F_c(s)=\sum_{n\ge1}(n+c)^{-s}
=\zeta(s)-\sum_{n=1}^{c}n^{-s}.
\tag{NL18}
\]
This proves exactly how (NL3) receives the full support count. It does not identify different support labels with one another in \(G_L\). The cardinality map forgets that distinction; the full meet-algebra coefficients and their primitive idempotents remain separate in the programme's full-support reconstruction. Formula (NL8) applies with \(t=c\) to the count receiver. All logarithmic product tuples, including their collisions in the length variable, are retained.

## NL6. Consequence for the positivity calculation

There are three exact facts to carry forward. First, the supported-zero prime remains a nontrivial prime of \(G(\mathbb Z)\); no positive finite multiplicative ideal norm extending the old norm can give it an ordinary new Euler factor. Second, the programme already supplies a different analytic receiver, the separated quotient-size interpolation (NL3), whose logarithmic derivative is (NL7), with the explicit signed atom (NL11). Third, its infinitesimal variation is (NL14), not zero. A corrected explicit formula for this receiver must use these arithmetic terms and its own completed divisor. The exact escaping-fibre trace and observed-operator current are calculated in the accompanying derivations; equality with a Weil form requires the actual map, not an identification of their names.

The two primitive-defect source files in folders 3 and 4 are byte-identical (SHA256 `2f3289f6a04105d3f15fe5f7c36dde286515e61f465caf1582f9808e19f3d2f7`). Their negative augmentation retains the kernel of a scalar cancellation. That same instruction is followed here: the full signed length distribution (NL8) and mixed-prime distribution (NL15) are retained rather than discarded when an ordinary Euler presentation fails.


![All nonzero positive-length atoms through ratio 3, and the exact first arithmetic coefficients; the zero-length mass is stated separately. Proof: NL7–NL16.](figures/24_non_eulerian_lengths.png)
