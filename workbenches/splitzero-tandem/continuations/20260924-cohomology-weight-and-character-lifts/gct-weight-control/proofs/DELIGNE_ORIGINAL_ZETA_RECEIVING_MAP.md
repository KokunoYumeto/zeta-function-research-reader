# The complete arithmetic return measure in Deligne's weight argument

24 September 2026. Exact maps DR0–DR7. The input stage is the complete arithmetic recovered from the source, not a preselected pair of prime labels. The maps preserve separate branch counters, the unit and every repeated return. No numerical operation is assigned to \(\tau\langle Z_1;\text{no }Z_2\rangle\).

## DR0. Source and input stage

The user requires the full infinite structure before its arithmetic labels are used. The current comparison begins **after** the complete source's winding quotient and endomorphism ring have been constructed in CG0–CG6 and BCC1–BCC4. Write \(L\) for that quotient and \(A=\operatorname{End}_{\mathrm{Ab}}(L)\). Those proofs construct the unital ring isomorphism \(A\simeq\mathbb Z\) from the full cyclic source; they do not prove cyclicity from a lone supporting point. GTQ records the exact duration-group criterion for that earlier step. This input boundary remains explicit.

Within this recovered ring, let \(A_{>0}\) be the positive nonzero endomorphisms. For \(a\in A_{>0}\), define
\[
N(a)=|L/aL|.
\tag{DR0.1}
\]
The source's identity endomorphism has \(N(1_A)=1\), and the quotient-clock proof gives \(N(ab)=N(a)N(b)\). The positive prime elements are exactly those with nonzero simple cokernel. Their norm labels become the usual primes under the established ring isomorphism. Numerical notation below refers to this output. No individual prime found in advance is used to construct the input ring.

Human source: Pierre Deligne, *La conjecture de Weil. II*, §2.1.9, printed p191, together with §§2.1.1–2.1.8. Root read the complete current French transcription, pp137–252. Its identity and limitations are in DP0 and the reading ledger. Deligne explicitly specializes the positive logarithmic-derivative measure to the original Riemann zeta function in2.1.9; the following calculation gives the full invertible map from the programme measure to his measure.

## DR1. All counts and all repeated prime returns

Use the nonnegative real time half-line only as the receiving space of logarithmic norms. It is not a coordinate or metric on the supporting point. Define locally finite measures
\[
\mathcal D=\sum_{a\in A_{>0}}\delta_{\log N(a)}
=\delta_0+\sum_{n\ge2}\delta_{\log n},
\tag{DR1.1}
\]
\[
\mathcal R=\sum_{\mathfrak p}\sum_{m\ge1}
\frac1m\delta_{m\log N(\mathfrak p)},
\qquad
\mathcal W=\sum_{\mathfrak p}\sum_{m\ge1}
\log N(\mathfrak p)\,\delta_{m\log N(\mathfrak p)}.
\tag{DR1.2}
\]
Here the first sum is over the recovered closed prime points of \(\operatorname{Spec}A\), with \(N(\mathfrak p)=|A/\mathfrak p|\). For every finite \(T\), an atom in \([0,T]\) has \(N(\mathfrak p)^m\le e^T\); only finitely many norms and repetitions occur. This proves local finiteness with every multiplicity retained.

For locally finite measures with support bounded away from zero, define convolution by addition of receiving times. On \([0,T]\), a convolution power of order greater than \(T/\log2\) of \(\mathcal R\), or of \(\mathcal D-\delta_0\), is zero. Therefore the formal convolution exponential and logarithm below are finite sums on each compact interval:
\[
\exp_*(\mathcal R)=\sum_{k\ge0}\frac{\mathcal R^{*k}}{k!},
\qquad
\log_*(\mathcal D)=\sum_{k\ge1}\frac{(-1)^{k+1}}k
(\mathcal D-\delta_0)^{*k}.
\tag{DR1.3}
\]
The zero-fold term is \(\delta_0\). No unit contribution is lost.

For a single prime point, put \(u=\delta_{\log N(\mathfrak p)}\). The formal identity
\[
\exp_*\left(\sum_{m\ge1}\frac{u^{*m}}m\right)
=\sum_{r\ge0}u^{*r}
\tag{DR1.4}
\]
follows by differentiating the corresponding one-variable series: both sides have constant1 and solve \((1-z)f'(z)=f(z)\), whose coefficient recursion forces every coefficient to be1. The exponential of a sum is a convolution product of exponentials, since convolution is commutative and the binomial formula applies coefficientwise. Thus
\[
\exp_*(\mathcal R)
=\mathop{*}_{\mathfrak p}\left(\sum_{r\ge0}
\delta_{r\log N(\mathfrak p)}\right)
=\mathcal D.
\tag{DR1.5}
\]
The second equality is exactly unique factorization in the reconstructed ring: each positive endomorphism has one finite prime factorization, including the empty factorization of the identity. On any compact interval all displayed products reduce to finite ones. The formal logarithm is inverse to the exponential because this identity holds in each truncated polynomial algebra, where the positive-support ideal is nilpotent. Therefore
\[
\boxed{\mathcal R=\log_*\mathcal D,\qquad
\mathcal D=\exp_*\mathcal R,\qquad
\mathcal W=t\,\mathcal R.}
\tag{DR1.6}
\]
The last identity follows atom by atom from \((m\log N(\mathfrak p))/m=\log N(\mathfrak p)\).

## DR2. The map to Deligne's positive measure, and its inverse

For a real number \(\sigma>1\), set
\[
\mu_\sigma=e^{-\sigma t}\mathcal W
=\sum_{\mathfrak p,m\ge1}
\log N(\mathfrak p)\,N(\mathfrak p)^{-m\sigma}
\delta_{m\log N(\mathfrak p)}.
\tag{DR2.1}
\]
This is the complete measure in Deligne2.1.9 for \(\Gamma=\mathbb R\), with the additive Frobenius class \(\log N(\mathfrak p)\). Its mass is finite: summing repetitions and enlarging the prime sum gives
\[
\|\mu_\sigma\|
\le\frac1{1-2^{-\sigma}}
\sum_{n\ge2}(\log n)n^{-\sigma}<\infty.
\tag{DR2.2}
\]
The final series converges by comparison with \(n^{-(\sigma+1)/2}\) beyond a finite threshold. The same argument is uniform for \(\sigma\ge1+\epsilon\) on every fixed \(\epsilon>0\), so termwise transforms and derivatives below are justified.

The map is invertible on this class of complete measures:
\[
\boxed{\mathcal R=\frac{e^{\sigma t}}t\mu_\sigma
\quad(t>0),\qquad
\mathcal D=\exp_*\left(\frac{e^{\sigma t}}t\mu_\sigma\right).}
\tag{DR2.3}
\]
Every positive-time atom stays away from zero, so the division by \(t\) is well defined and locally finite. The exponential reinstates \(\delta_0\) as its zeroth term. Conversely multiplication by \(te^{-\sigma t}\) recovers \(\mu_\sigma\) from that logarithm. This verifies both compositions. The only mass not directly seen by multiplying with \(t\) is the unit at0, which is independently retained in(DR1.1) and fixed by the original arithmetic.

For two branches related by BCC's actual full-record isomorphism, conjugation of endomorphisms induces isomorphic finite cokernels. It preserves every \(N(a)\), every prime ideal, and every \(N(\mathfrak p)\). Consequently it identifies the measures(DR1.1–2) and(DR2.1) term by term **after each branch uses its own recovered counter**. This is a comparison of two equal receiving measures. Adding the two measures instead would double the logarithm and produce a squared function; that operation is absent from this comparison.

## DR3. The original zeta and its complete logarithmic derivative

For \(s=\sigma+iu\) with \(\sigma>1\), absolute convergence gives
\[
\mathcal L\mathcal D(s)
=\int_{[0,\infty)}e^{-st}\,d\mathcal D(t)
=\sum_{n\ge1}n^{-s}=\zeta(s).
\tag{DR3.1}
\]
The unit coefficient is exactly1. Finite convolution products and then dominated convergence give
\[
\zeta(s)=\prod_{\mathfrak p}(1-N(\mathfrak p)^{-s})^{-1},
\qquad
\mathcal L\mathcal R(s)=\sum_{\mathfrak p,m\ge1}
\frac{N(\mathfrak p)^{-ms}}m=\log\zeta(s).
\tag{DR3.2}
\]
The logarithm is the analytic branch tending to0 as real \(s\to+\infty\); it has been constructed by the convergent series, not chosen after continuation. Differentiate using(DR2.2):
\[
\boxed{\widehat\mu_\sigma(u)
:=\int e^{-iut}\,d\mu_\sigma(t)
=-\frac{\zeta'(\sigma+iu)}{\zeta(\sigma+iu)}.}
\tag{DR3.3}
\]
In particular the Fourier transform convention fixes the sign. Conversely the logarithmic derivative determines the original function with its unit through
\[
\log\zeta(s)=\int_0^\infty
\left(-\frac{\zeta'(s+v)}{\zeta(s+v)}\right)\,dv,
\qquad \Re s>1.
\tag{DR3.4}
\]
To check it, integrate each term of(DR3.3): \(\int_0^\infty N(\mathfrak p)^{-mv}\log N(\mathfrak p)\,dv=1/m\). The absolute integral is the convergent series(DR3.2). Exponentiation yields(DR3.1), with limiting value1 at real infinity.

This proves an exact receiving map and inverse for the original function on its Euler half-plane. No completed zeta has replaced it.

## DR4. What the same positive measure proves at the boundary

Write \(A(s)=-\zeta'(s)/\zeta(s)\). Because \(\mu_\sigma\) is positive, the square identity
\[
3+4\cos v+2\cos(2v)=(1+2\cos v)^2\ge0
\tag{DR4.1}
\]
gives the exact all-return inequality
\[
3A(\sigma)+4\Re A(\sigma+iu)+2\Re A(\sigma+2iu)
=\sum_{\mathfrak p,m\ge1}
\log N(\mathfrak p)N(\mathfrak p)^{-m\sigma}
\bigl(1+2\cos(um\log N(\mathfrak p))\bigr)^2\ge0.
\tag{DR4.2}
\]
Assume \(u\ne0\) and let \(m_1,m_2\ge0\) be the respective zero multiplicities at \(1+iu\) and \(1+2iu\), taking zero multiplicity when no zero occurs. The established meromorphic continuation of the **same** original zeta has its unique pole, simple, at1. Its local logarithmic derivatives therefore satisfy
\[
\lim_{\sigma\downarrow1}(\sigma-1)A(\sigma)=1,
\quad
\lim_{\sigma\downarrow1}(\sigma-1)\Re A(\sigma+iju)=-m_j
\quad(j=1,2).
\tag{DR4.3}
\]
This follows by factoring each function locally as \((s-s_0)^{m_j}g(s)\) with \(g(s_0)\ne0\), and retaining the simple-pole factor at1. Multiply(DR4.2) by \(\sigma-1>0\) and take the limit. It gives \(3-4m_1-2m_2\ge0\). If \(m_1\ge1\), its left side is at most−1, a contradiction. Hence the original zeta has no zero on \(\Re s=1\).

This is the source's boundary mechanism, carried out on the programme's exact complete return measure. DB reconstructs its compact-group extension, including the exceptional quadratic-character argument. DW shows precisely where that **strict** boundary result enters the weight improvement for sheaf cohomology. The steps beyond(DR4.2) in that geometric argument are not replaced by the existence of the positive measure.

## DR5. Completion and exceptional points remain explicit

Where the source comparison or reflection uses the completed function, retain its full multiplier:
\[
C(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
\xi(s)=C(s)\zeta(s).
\tag{DR5.1}
\]
The expression(DR3.3) is still the original logarithmic derivative. At regular points its exact comparison is
\[
-\frac{\zeta'(s)}{\zeta(s)}
=\frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)-\frac{\xi'(s)}{\xi(s)},
\tag{DR5.2}
\]
where \(\psi=\Gamma'/\Gamma\). This is obtained by differentiating every factor of(DR5.1). As an identity of meromorphic functions it retains all exceptional-point cancellations:

- At0, \(\Gamma(s/2)=2/s-\gamma+O(s)\), so \(C(0)=-1\); the \(1/s\) term cancels the digamma pole and \(\zeta(0)=-1/2\) is nonzero.
- At1, \(C(s)=\tfrac12(s-1)+O((s-1)^2)\) and the pole of \(\zeta\) cancels its zero in \(\xi\). The original logarithmic derivative still has residue+1 there, as used in(DR4.3).
- At each \(s=-2n\), \(n\ge1\), \(C\) has a simple pole. The corresponding original trivial zero is retained in(DR5.2) as a pole of \(-\zeta'/\zeta\) of residue−1. The zero and pole cancel in \(\xi\), not in the original function.
- At a nontrivial zero \(\rho\), \(C(\rho)\ne0,\infty\). Its full multiplicity is unchanged, and the residue of the original negative logarithmic derivative is its negative multiplicity.

The exact reflection multiplier is also retained:
\[
\zeta(s)=\frac{C(1-s)}{C(s)}\zeta(1-s).
\tag{DR5.3}
\]
OZR1–OZR8 prove its exceptional values, all differentiated terms and its action on every local jet. Nothing in the branch comparison removes these contributions.

## DR6. The exact finite-field/time dictionary

In the finite-field part of Deligne's proof a single variable \(t\) records degrees, so a local factor contains \(t^{d_x}\). Writing \(t=q^{-s}\) is the explicit analytic map
\[
t^{d_x}=q^{-sd_x}=N(x)^{-s},\qquad
-\frac{d}{ds}\log L(q^{-s})
=(\log q)\,t\frac{L'(t)}{L(t)}.
\tag{DR6.1}
\]
Every degree factor and \(\log q\) remains. With a coefficient sheaf, the local repetitions are weighted by \(\operatorname{Tr}(F_x^m)\); DP4 raises those real traces to even powers. For the original Riemann zeta in(DR3), the norm times are the full \(\log N(\mathfrak p)\), and Deligne2.1.9 uses \(\Gamma=\mathbb R\). They are not all identified with multiples of one fixed \(\log q\).

To verify the last assertion, two distinct recovered prime norms p and r on such a common degree grid would satisfy p=q^a and r=q^b for positive integers a,b. Then p^b=r^a, contradicting unique factorization in the recovered ring. This argument is downstream of the complete arithmetic reconstruction.

This does not challenge the recovered integer counter: additive counting on \(L\), endomorphism degree \(N(a)\), and the logarithmic norm used in the Euler transform are connected by the explicit maps above. They are different receiving quantities with derived relations. No subtraction, common radius, or numeric origin is assigned to \(\tau\) by any of them.

## DR7. The actual composition supplied by the reading

The complete composition now established is
\[
\begin{gathered}
\text{complete reconstructed }A=\operatorname{End}(L),\ \operatorname{Spec}A,\ N
\ \longmapsto\ \mathcal D\text{ including }\delta_0,\\
\mathcal D\ \xleftrightarrow[\exp_*]{\log_*}\ \mathcal R
\ \xleftrightarrow[e^{\sigma t}/t]{te^{-\sigma t}}\ \mu_\sigma,\\
\widehat\mu_\sigma(u)=-\zeta'(\sigma+iu)/\zeta(\sigma+iu),\\
\text{positive square on all repeated returns}
\ \longmapsto\ \text{boundary nonvanishing of the original }\zeta.
\end{gathered}
\tag{DR7.1}
\]
It commutes with the separate-counter branch isomorphisms. It does not pool their measures, install a metric, or identify the supporting point with arithmetic zero. DP, DLM, DB and DW then spell out the additional **actual source operations**—tensor powers, local monodromy, boundary cycles, a pencil and duality—that give Deligne's exact cohomological weights. The adjacent base-comparison note constructs the available functors over the recovered arithmetic and the fixed support, with their retained Frobenius and duality data. These are proved maps on the specified objects; a bare renaming of a point has not been presented as a weight theorem.
