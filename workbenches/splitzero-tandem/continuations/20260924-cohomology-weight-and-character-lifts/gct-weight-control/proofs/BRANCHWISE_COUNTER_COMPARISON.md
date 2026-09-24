# Separate branch counters, the original zeta, and the retained spectral action

Private independent derivation, 24 September 2026. Proof locators BCC0–BCC9.

## BCC0. The request, reading record, and exact input class

The new attachment was read in full:

Latest branch correction and admissible-deviation argument (private construction record; not included).

Its operative correction is that branches are compared **after each has been divided by its own recovered counter**. Their measures must not be pooled. Its subsequent question concerns deviations that retain sufficient arithmetic to recover the same original Riemann zeta function. The user's tentative implication from quotientability to RH is a question to calculate, not an established theorem.

The present input class consists of complete timing records whose generated duration groups are nonzero cyclic groups. This is the class for which the preceding full-history calculation actually constructs a primitive counter. The cyclicity criterion and its proof are in [GLOBAL_TIMING_QUOTIENT_INDEPENDENT.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/GLOBAL_TIMING_QUOTIENT_INDEPENDENT.md), GTQ1–GTQ4. No assertion is made that a parityless supporting point alone forces this input class.

Every numerical label below occurs after that complete-history construction. No selected prime is an initial datum. Integers used to state finite repeated concatenations in the proof belong to the metatheory; the branch's arithmetic labels are the output of BCC2–BCC4.

The supporting object retains the user's notation
\[
\tau\langle Z_1;\text{ no }Z_2\rangle.
\]
No addition, subtraction, metric, coordinate, midpoint, or vector is assigned to it. A duration belongs to a duration line, not to the supporting object.

The following programme sources were actually read for this calculation:

- GLOBAL_TIMING_QUOTIENT_INDEPENDENT.md, GTQ0–GTQ12: the complete timing group, primitive-counter criterion, and finite-prefix comparison.
- CANONICAL_GENERIC_RECONSTRUCTION.md, CG0, and TIMED_PRIME_PERIOD_DERIVATION.md, TP0–TP2 and the opening of TP3: the existing return-measure receiver.
- WINDING_REVERSAL_AND_FIXED_SUPPORT.md, WR5–WR7, including the full signed character and multiplicity formulas.
- ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md, RZ1 and RZ8, together with the immediately preceding projector formulas: the actual quotient, original-zeta multiplier, and arithmetic action.

The source-routing and source-use ledgers were consulted before this derivation. The branch maps below are derived directly. BCC7 and BCC8 apply them to the specified programme receivers; they do not replace those receivers with an arbitrary matrix example.

## BCC1. Classification of linear comparisons between complete cyclic histories

For each branch \(i\), let \(V_i\) be an oriented one-dimensional real vector space of durations. Let \(E_i\) be the set of **absorption events**, including any retained event identities, multiplicities, and channel labels, and let
\[
t_i:E_i\longrightarrow V_{i,>0}
\tag{BCC1.1}
\]
give their complete positive timing record. Events sharing a duration remain distinct elements of \(E_i\). Separately recorded non-absorption observations may be kept in a set \(N_i\) with a map \(u_i:N_i\to V_i\). They are not relabelled as absorption events.

The generated duration group is
\[
G_i=\left\{\sum_{e\in F}a_e t_i(e):
 F\subset E_i\text{ finite},\ a_e\in\mathbb Z\right\}\subset V_i.
\tag{BCC1.2}
\]
In the present input class \(G_i\) is nonzero and has a least positive element. The full-history calculation calls that element \(\delta_i\) and proves
\[
G_i=\delta_i\mathbb Z.
\tag{BCC1.3}
\]
For completeness, every \(g>0\) in \(G_i\) has an integer \(n\geq0\) with
\(n\delta_i\leq g<(n+1)\delta_i\), by the Archimedean property of the real duration line. The remainder \(g-n\delta_i\) belongs to \(G_i\) and lies in \([0,\delta_i)\); minimality of \(\delta_i\) makes it zero. Negative elements follow by negation. The positive generator is unique because it is the least positive element.

Let
\[
A:V_i\xrightarrow{\sim}V_j,\qquad A(G_i)=G_j
\tag{BCC1.4}
\]
be a real-linear isomorphism. Put \(\varepsilon_A=+1\) for orientation preservation and \(-1\) for reversal. Then
\[
\boxed{A\delta_i=\varepsilon_A\delta_j.}
\tag{BCC1.5}
\]
Indeed \(A\delta_i=k\delta_j\) for a nonzero integer \(k\). Surjectivity on the generated groups gives \(\delta_j=\ell A\delta_i\) for an integer \(\ell\), hence \(k\ell=1\). Thus \(k=\pm1\), and its sign is \(\varepsilon_A\). Conversely the two real-linear maps
\[
A_\varepsilon(x\delta_i)=\varepsilon x\delta_j,
\qquad x\in\mathbb R,\quad\varepsilon\in\{+1,-1\},
\tag{BCC1.6}
\]
are all the maps satisfying (BCC1.4). This is an exact classification of the stated linear duration comparisons.

A comparison of the **complete forward absorption records** includes, in addition, a bijection
\[
\phi:E_i\xrightarrow{\sim}E_j,\qquad t_j\phi=A t_i
\tag{BCC1.7}
\]
preserving the stipulated labels and multiplicities. When both records in (BCC1.1) are nonempty and positive in their given orientations, (BCC1.7) forces \(\varepsilon_A=+1\). A reversing map sends positive durations to negative ones. It compares signed histories, or forward histories after transporting the target orientation, rather than two positive records with both orientations unchanged.

Equation (BCC1.4) alone does not assert (BCC1.7). An isomorphism of the duration groups need not preserve the actual absorption pattern. The needed event correspondence is part of the complete-record comparison and is tested explicitly in BCC2.

## BCC2. Separate counter readings and all event fibres

For each completed branch define its counter reading and its inverse by
\[
\nu_i:G_i\xrightarrow{\sim}\mathbb Z,\qquad
\nu_i(n\delta_i)=n,\qquad
\iota_i:\mathbb Z\xrightarrow{\sim}G_i,\quad \iota_i(n)=n\delta_i.
\tag{BCC2.1}
\]
Uniqueness of the representation proves that these maps are well defined, inverse, and additive. The two branches have been read with their **own** primitive counter; their duration values have not been identified or added.

Equations (BCC1.5) and (BCC2.1) give the complete comparison:
\[
\boxed{\nu_j A=\varepsilon_A\nu_i,\qquad
A\iota_i=\iota_j[\varepsilon_A].}
\tag{BCC2.2}
\]
Here \([\varepsilon_A]\) denotes multiplication by the displayed sign on the integer target. The diagram is
\[
\begin{array}{ccc}
G_i&\xrightarrow{\ A\ }&G_j\\
\nu_i\downarrow&&\downarrow\nu_j\\
\mathbb Z&\xrightarrow{\ n\mapsto\varepsilon_A n\ }&\mathbb Z.
\end{array}
\tag{BCC2.3}
\]
For the orientation-preserving comparison, the bottom arrow is the identity.

This is the exact meaning of division by the recovered counter in the arithmetic reconstruction. The literal additive quotient
\[
G_i/(\delta_i\mathbb Z)=0
\tag{BCC2.4}
\]
has no retained count information. It is not (BCC2.1).

After the complete counter has been recovered, let
\[
E_{i,n}=\{e\in E_i:t_i(e)=n\delta_i\},\qquad n>0.
\tag{BCC2.5}
\]
For a forward-record comparison (BCC1.7), (BCC2.2) proves
\[
\phi:E_{i,n}\xrightarrow{\sim}E_{j,n}
\quad\text{for every }n>0.
\tag{BCC2.6}
\]
To verify both directions, \(e\in E_{i,n}\) implies
\(t_j(\phi e)=A(n\delta_i)=n\delta_j\); the same calculation with \(A^{-1}\) and \(\phi^{-1}\) gives surjectivity on the displayed fibre.

The reconstructed absorption indicator
\[
b_i(n)=
\begin{cases}
1,&E_{i,n}\neq\varnothing,\\
0,&E_{i,n}=\varnothing
\end{cases}
\tag{BCC2.7}
\]
therefore satisfies \(b_i(n)=b_j(n)\) at every count. As \(E_i\) is the complete absorption record, empty fibres record the absence of absorption at those ticks. All event multiplicities and channel labels are retained by (BCC2.6), not only this binary indicator. Conversely, label-preserving bijections of every fibre assemble to a bijection \(\phi\) satisfying (BCC1.7). This proves the exact criterion for preservation of the full absorption record.

Separately recorded non-absorption data are transported by a separately specified bijection
\(\psi:N_i\to N_j\) with \(u_j\psi=A u_i\). The same fibre proof applies where their durations belong to \(G_i\). Observations outside \(G_i\) are retained as their original durations; (BCC2.1) is not extended to them without a further group construction. Thus no extra clock reading is silently invented.

## BCC3. Endomorphism arithmetic, multiplication, and the orientation sign

Let
\[
R_i=\operatorname{End}_{\mathrm{Ab}}(G_i)
\tag{BCC3.1}
\]
with pointwise addition and composition as multiplication. Every \(f\in R_i\) is determined by \(f(\delta_i)=n\delta_i\), and additivity then gives
\[
f(m\delta_i)=mn\delta_i.
\tag{BCC3.2}
\]
Conversely this formula defines an endomorphism for every integer \(n\). Writing this endomorphism as \([n]_i\), we obtain
\[
[m]_i+[n]_i=[m+n]_i,\quad
[m]_i[n]_i=[mn]_i,\quad
1_{R_i}=[1]_i.
\tag{BCC3.3}
\]
Consequently the degree map
\[
d_i:R_i\xrightarrow{\sim}\mathbb Z,\qquad d_i([n]_i)=n
\tag{BCC3.4}
\]
is a unital ring isomorphism. It is derived from the completed duration group.

The branch comparison gives
\[
C_A:R_i\xrightarrow{\sim}R_j,\qquad C_A(f)=AfA^{-1}.
\tag{BCC3.5}
\]
For \(x\in G_j\), additivity of \(A\) proves
\(C_A(f+g)(x)=C_A(f)(x)+C_A(g)(x)\).
Inserting \(A^{-1}A\) proves
\(C_A(fg)=C_A(f)C_A(g)\).
Also \(C_A(1)=1\), and \(C_{A^{-1}}\) is its inverse. Thus (BCC3.5) is a unital ring isomorphism for either orientation.

For every integer degree,
\[
\boxed{C_A([n]_i)=[n]_j,\qquad d_jC_A=d_i.}
\tag{BCC3.6}
\]
Indeed \(A(nA^{-1}x)=nx\). In particular, reversal changes the signed count in (BCC2.2) while preserving each endomorphism degree, each power \([n]^r=[n^r]\), and every polynomial relation among these endomorphisms.

Evaluation on the respective positive units has its own sign:
\[
\operatorname{ev}_i:R_i\to G_i,\quad f\mapsto f(\delta_i),
\qquad
\boxed{\operatorname{ev}_j C_A
       =\varepsilon_A A\operatorname{ev}_i.}
\tag{BCC3.7}
\]
Proof: \(A^{-1}\delta_j=\varepsilon_A\delta_i\), so
\((AfA^{-1})(\delta_j)=\varepsilon_A A(f(\delta_i))\).

For reference, transport the ring multiplication to the duration group:
\[
(n\delta_i)\odot_i(m\delta_i)=nm\delta_i.
\tag{BCC3.8}
\]
Its unit is the actual duration \(\delta_i\). A positive \(A\) is a unital isomorphism between these duration rings. A reversing \(A\) instead satisfies
\[
A(g\odot_i h)=\varepsilon_A
              \bigl(A(g)\odot_j A(h)\bigr),\qquad
A\delta_i=-\delta_j.
\tag{BCC3.9}
\]
Both equations follow by putting \(g=n\delta_i\), \(h=m\delta_i\) and retaining the signs. Thus \(A\) with negative sign is not a unital ring isomorphism between duration rings with their **positive** units. The endomorphism isomorphism (BCC3.5) remains unital. Using \(-A\), or explicitly transporting the signed unit, gives the corresponding positive comparison.

For any abelian multiplicative group \(K^\times\), there is also the exact character comparison
\[
\Phi_A:\operatorname{Hom}(G_i,K^\times)
 \xrightarrow{\sim}\operatorname{Hom}(G_j,K^\times),
\qquad \Phi_A(\chi)=\chi\circ A^{-1}.
\tag{BCC3.10}
\]
Its inverse is \(\Phi_{A^{-1}}\), it preserves pointwise powers, and
\[
\Phi_A(\chi)(\delta_j)=\chi(\delta_i)^{\varepsilon_A}.
\tag{BCC3.11}
\]
This follows again from \(A^{-1}\delta_j=\varepsilon_A\delta_i\). Character-coordinate inversion and preservation of endomorphism degree are therefore simultaneous, calculated effects of the same reversing map.

## BCC4. Finite quotient clocks, prime ideals, and retained norms

For \(f\in R_i\), define the quotient comparison
\[
\overline A_f:G_i/fG_i\xrightarrow{\sim}
G_j/(C_A f)G_j,\qquad
g+fG_i\longmapsto Ag+(C_A f)G_j.
\tag{BCC4.1}
\]
Since \(A(fG_i)=(C_A f)G_j\), this is well defined; the analogous map induced by \(A^{-1}\) is its inverse. For \(f=[n]\), \(n\neq0\), division with remainder provides the distinct representatives
\[
0,\delta_i,\ldots,(|n|-1)\delta_i.
\tag{BCC4.2}
\]
Existence of representatives follows from division of the integer coordinate by \(|n|\); two displayed representatives have difference in \(nG_i\) only when their coordinate difference is a multiple of \(|n|\), hence only when they coincide. Therefore
\[
\#(G_i/[n]G_i)=|n|
             =\#(G_j/[n]G_j).
\tag{BCC4.3}
\]
For \(n=0\), the quotient is the infinite group \(G_i\); no finite norm is assigned by this formula. For \(n=1\), the quotient is the zero group with one element, so its cardinality is one.

Every ideal in \(R_i\) has the form \(dR_i\), for one nonnegative integer \(d\). To prove it, the zero ideal gives \(d=0\). A nonzero ideal contains a nonzero integer degree and hence a positive degree. Take its least positive degree \(d\). Division of any degree \(a\) in the ideal by \(d\) gives \(a=qd+r\), \(0\leq r<d\), with \(r\) still in the ideal. Minimality gives \(r=0\). Conversely the ideal contains all multiples of \(d\).

Its nonzero proper prime ideals are exactly \(pR_i\) with \(p\) a positive prime integer in the recovered ring. If \(d=ab\) with \(1<a,b<d\), then neither \(a\) nor \(b\) belongs to \(dR_i\), but their product does, so the ideal is not prime. For prime \(p\), division in the recovered integer ring gives the Euclidean algorithm. It terminates because its nonzero remainders strictly decrease; back substitution expresses the greatest common divisor as an integer combination. If \(p\) does not divide \(a\), their greatest common divisor is one, so \(ua+vp=1\). If \(p\mid ab\), multiplication by \(b\) gives \(p\mid b\). This proves primality of \(pR_i\). The zero ideal is also prime, because degrees multiply in an integral domain.

Equation (BCC3.6) gives
\[
C_A(dR_i)=dR_j,\qquad
R_i/dR_i\xrightarrow{\sim}R_j/dR_j.
\tag{BCC4.4}
\]
For \(d\neq0\) the quotient rings have \(|d|\) elements by the same representatives as above. In particular each closed prime point has the unchanged residue norm
\[
N_i(pR_i)=\#(R_i/pR_i)=p=N_j(pR_j).
\tag{BCC4.5}
\]
The generic prime \((0)\) is retained; its residue field is the fraction field of the recovered ring, and is not a finite residue field. It is not inserted as an extra finite-norm Euler factor. This paragraph does not identify the ring's generic point with the programme's supporting object without a specified supporting map.

The contravariant map
\[
\operatorname{Spec}R_j\longrightarrow\operatorname{Spec}R_i,\qquad
\mathfrak p\longmapsto C_A^{-1}(\mathfrak p)
\tag{BCC4.6}
\]
is a homeomorphism. Primality is preserved by the ring isomorphism; the inverse uses \(C_A\); and the inverse image of the basic open \(D(f)\) is \(D(C_A f)\), proving continuity in both directions. Equations (BCC4.4)–(BCC4.5) prove that this is a comparison of **normed** prime spectra, including every recovered prime, not only a selected finite collection.

## BCC5. Each reconstructed branch gives the same original zeta

Let \(R_{i,+}\) consist of the endomorphisms sending the positive generator to a nonnegative multiple of itself. For its nonzero elements put
\[
N_i([n]_i)=\#(G_i/[n]_iG_i)=n,\qquad n\geq1.
\tag{BCC5.1}
\]
The branch's full Dirichlet sum is
\[
Z_i(s)=\sum_{f\in R_{i,+}\setminus\{[0]_i\}}N_i(f)^{-s}
      =\sum_{n=1}^\infty n^{-s}
      =\zeta(s),\qquad \operatorname{Re}s>1.
\tag{BCC5.2}
\]
Here \(x^{-s}=\exp(-s\log x)\) uses the real logarithm of the positive finite quotient cardinality. If \(\sigma=\operatorname{Re}s>1\), the series is absolutely convergent because
\[
\sum_{n=1}^\infty n^{-\sigma}
\leq 1+\int_1^\infty x^{-\sigma}\,dx
=1+\frac1{\sigma-1}.
\tag{BCC5.3}
\]
Every term, including the unit term \(1^{-s}=1\), is present.

Conjugation \(C_A\) bijects the positive-degree endomorphisms and preserves (BCC5.1), even for a reversing duration comparison. Thus
\[
Z_j(s)=Z_i(s)
\tag{BCC5.4}
\]
term by term, after each branch's own reconstruction. This proof never takes a sum of the two branch records.

The Euler product is recovered from the whole ring. Here is the factorization argument needed to justify it. A positive integer greater than one has a smallest divisor greater than one; that divisor is prime, for a proper factor would be a smaller such divisor. Repeated division by such a prime terminates on each integer because the positive quotients decrease. This gives existence of a finite prime factorization. The prime divisor property proved in BCC4 shows that a prime in one factorization appears in any other factorization of the same integer. Cancel it and repeat, proving uniqueness including exponents.

For a finite set \(P\) of recovered primes, the absolutely convergent geometric products therefore give
\[
\prod_{p\in P}(1-p^{-s})^{-1}
=\sum_{\substack{n\geq1\\\text{all prime divisors of }n\text{ lie in }P}}
n^{-s}.
\tag{BCC5.5}
\]
As \(P\) exhausts the full prime set, every integer eventually occurs and the omitted terms are bounded in absolute value by the tail of (BCC5.3). Hence
\[
Z_i(s)=\prod_{p\ {\rm prime}}(1-p^{-s})^{-1}
      =Z_j(s)=\zeta(s),\qquad \operatorname{Re}s>1.
\tag{BCC5.6}
\]
This keeps every prime power and its exponent. No prime is chosen before the global counter and ring are reconstructed.

Since the original Riemann zeta function has its meromorphic continuation, the branch functions defined by (BCC5.2) have that same continuation by uniqueness of analytic continuation. More explicitly, the difference of two proposed meromorphic continuations vanishes on the connected right half-plane; away from isolated poles the identity theorem propagates that equality through the connected continuation domain, and identical Laurent expansions then identify poles as well. Accordingly, the comparison preserves the original pole, all trivial and nontrivial zeros, their orders, and all Laurent coefficients. It does not replace the original zeta by a completed function.

The conclusion in this section concerns the arithmetic reconstructed from \(R_i\). An arbitrary marked timing record is not thereby declared to be its prime return measure. The precise return-measure receiver is the next calculation.

## BCC6. Full return measures, all repetitions, and the unit term

From the recovered normed prime spectrum define, for each branch separately,
\[
\mu_i=\sum_{\mathfrak p\in(\operatorname{Spec}R_i)_{\rm closed}}
      \ \sum_{k=1}^\infty\frac1k\,
          \delta_{\,k\log N_i(\mathfrak p)}.
\tag{BCC6.1}
\]
The symbol \(\delta_x\) in this section denotes a unit point mass at a positive logarithmic duration \(x\); it is not the primitive tick \(\delta_i\).

The measure is locally finite. In a bounded interval \([0,B]\), an atom must satisfy \(p^k\leq e^B\). There are only finitely many integers \(p\leq e^B\), and for each such \(p>1\) there are only finitely many positive \(k\) satisfying this inequality. The coefficients \(1/k\), repetitions, and prime labels have not been suppressed.

The norm-preserving prime bijection in (BCC4.6) gives the exact transported identity
\[
\boxed{\mu_j=\mu_i.}
\tag{BCC6.2}
\]
This denotes equality after transporting the source labels through their bijection, or equality of the resulting scalar measures on logarithmic durations. It is not a pooling of measures.

For \(\operatorname{Re}s=\sigma>1\),
\[
\int e^{-su}\,d\mu_i(u)
=\sum_p\sum_{k=1}^\infty\frac{p^{-ks}}k.
\tag{BCC6.3}
\]
Absolute convergence follows, for example, from
\[
\sum_p\sum_{k\geq1}\frac{p^{-k\sigma}}k
\leq \frac1{1-2^{-\sigma}}\sum_{n=2}^\infty n^{-\sigma}<\infty.
\tag{BCC6.4}
\]
The appearance of the smallest recovered prime in this estimate is downstream of the complete reconstruction; it is not a selected input to it.

For \(|z|<1\), integrating the absolutely convergent geometric series along the segment from \(0\) to \(z\) gives
\(-\log(1-z)=\sum_{k\geq1}z^k/k\), with the logarithm taking value zero at \(z=0\). Exponentiation, finite products, and then absolute convergence yield
\[
\exp\!\left(\int e^{-su}\,d\mu_i(u)\right)
=\prod_p(1-p^{-s})^{-1}
=\zeta(s).
\tag{BCC6.5}
\]

The complete counting measure, including its unit atom, is the convolution exponential
\[
\operatorname{Exp}_*(\mu_i)
=\delta_0+\sum_{r=1}^\infty\frac1{r!}\mu_i^{*r}
=\sum_{n=1}^\infty\delta_{\log n}.
\tag{BCC6.6}
\]
To prove that this is an equality of locally finite measures rather than only a formal notation, every atom of \(\mu_i\) has duration at least \(\log2>0\), so only \(r\leq B/\log2\) can contribute on \([0,B]\). Within each convolution only finitely many atoms contribute there, as already proved. For a single prime, the coefficient-generating identity is
\[
\exp\!\left(\sum_{k\geq1}\frac{x^k}k\right)
=\frac1{1-x}=\sum_{a\geq0}x^a.
\tag{BCC6.7}
\]
One can check it as a formal power series: the left series has constant coefficient one and logarithmic derivative \(1/(1-x)\), so its coefficient recurrence is exactly that of the right series. Each exponent \(a\) therefore has coefficient one. Unique factorization from BCC5 then shows that every \(\log n=\sum_p a_p\log p\) has coefficient one in (BCC6.6), including \(\log1=0\) from the explicit \(\delta_0\).

The two sides of the branch comparison preserve (BCC6.6) term by term. In particular, taking its Laplace transform gives the same original \(\zeta(s)\) in each branch. The unit atom here is an atom in the logarithmic return measure; it is not an identification of \(\tau\) with numerical zero.

## BCC7. The actual signed winding reversal and its arithmetic character map

The programme's CC receiver has the actual group and involution
\[
\mathcal G=\mathbb Z\times C_4,\qquad
T=(1,0),\quad J=(0,1),\quad \epsilon=(0,2),
\]
\[
\alpha(m,k)=(-m,\,2m-k)\quad(k\text{ modulo }4).
\tag{BCC7.1}
\]
These are the full source coordinates recorded in WINDING_REVERSAL_AND_FIXED_SUPPORT.md, WR1 and WR5. Addition of pairs proves that \(\alpha\) is a homomorphism. Directly,
\[
\alpha^2(m,k)
=\alpha(-m,2m-k)
=(m,k-4m)=(m,k),
\tag{BCC7.2}
\]
so it is an automorphism.

Its finite-order subgroup is exactly \(\{0\}\times C_4\). An element with nonzero integer coordinate cannot have finite order, while one with zero integer coordinate has order dividing four. Thus the exact sequence
\[
0\longrightarrow C_4
\longrightarrow\mathcal G
\xrightarrow{\ q\ }\mathbb Z
\longrightarrow0,\qquad q(m,k)=m
\tag{BCC7.3}
\]
retains the finite phase data and gives
\[
q\alpha=-q.
\tag{BCC7.4}
\]
The induced winding comparison has the negative sign of BCC2, while conjugation on its cyclic endomorphism ring still fixes every \([n]\) by BCC3. The \(C_4\) factor is retained in (BCC7.1)–(BCC7.3), not erased from the source.

A character \(\chi:\mathcal G\to\mathbb C^\times\) is specified by
\[
\chi(T)=a\neq0,\qquad \chi(J)=\omega,\qquad
\omega^4=1,\qquad \chi(T^mJ^k)=a^m\omega^k.
\tag{BCC7.5}
\]
Every such pair defines a character, and the generators prove uniqueness. Pullback and its complex conjugate have generator values
\[
\chi\circ\alpha:
(a,\omega)\longmapsto(\omega^2 a^{-1},\omega^{-1}),
\]
\[
\overline{\chi\circ\alpha}:
(a,\omega)\longmapsto(\omega^2/\overline a,\omega).
\tag{BCC7.6}
\]
The first equation follows by applying \(\alpha\) to \(T,J\); the second uses \(|\omega|=1\), \(\overline{\omega^{-1}}=\omega\), and \(\overline{\omega^2}=\omega^2\).

For a recovered prime norm \(p\) and each retained phase sector \(\omega\), define the compensating character
\[
\mu_{p,\omega}(T)=p\omega^2,\qquad
\mu_{p,\omega}(J)=1,\qquad
\mu_{p,\omega}(\epsilon)=1.
\tag{BCC7.7}
\]
These assignments respect the group presentation. Multiplying it by the full reversed-conjugate character gives
\[
\mathfrak D_p\chi
=\mu_{p,\omega}\overline{\chi\circ\alpha},
\qquad
\mathfrak D_p(a,\omega)=(p/\overline a,\omega).
\tag{BCC7.8}
\]
Indeed the value at \(T\) is
\[
(p\omega^2)(\omega^2/\overline a)
=p\omega^4/\overline a=p/\overline a,
\tag{BCC7.9}
\]
and the value at \(J\) remains \(\omega\). The degree, finite phase, and conjugation factors are all displayed.

For the actual arithmetic character \(a=p^\rho=\exp(\rho\log p)\),
\[
\mathfrak D_p(p^\rho,\omega)
=(p^{1-\overline\rho},\omega).
\tag{BCC7.10}
\]
Its fixed-character equation is exactly
\[
a=p/\overline a
\ \Longleftrightarrow\ |a|^2=p
\ \Longleftrightarrow\ p^{2\operatorname{Re}\rho}=p
\ \Longleftrightarrow\ \operatorname{Re}\rho=\tfrac12.
\tag{BCC7.11}
\]
The last equivalence uses \(\log p>0\).

This compares the operations exactly: branch conjugation fixes the recovered endomorphism degree \([p]\), but degree-weighted conjugate duality changes the character value by (BCC7.8). Equation (BCC3.6) does not set that character value equal to its transformed value. There is no distance assigned to the support in this calculation.

## BCC8. The same original zeta retains the same actual zero blocks

Here the inputs are the specific proved quotient and operators in ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md, RZ1 and RZ8. Let \(\mathcal Z\) be the actual multiset of nontrivial zeros of the original \(\zeta(s)\), with multiplicity \(m_\rho\). Let \(\mathcal B\) be the entire functions rapidly decreasing on every closed vertical strip, with seminorms
\[
\|F\|_{A,M}
=\sup_{|\operatorname{Re}s|\leq A}
(1+|\operatorname{Im}s|)^M|F(s)|,
\qquad A>0,\quad M\geq0.
\tag{BCC8.1}
\]
Put
\[
\mathcal I
=\{F\in\mathcal B:F^{(j)}(\rho)=0
 \text{ for every }\rho\in\mathcal Z,\ 0\leq j<m_\rho\},
\qquad
\mathcal Q=\mathcal B/\mathcal I.
\tag{BCC8.2}
\]
This is the actual quotient with its quotient topology. It is not replaced by an unrestricted product of independently invented zero coordinates.

The full source multiplier in the programme remains
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{BCC8.3}
\]
In particular the endpoint and trivial-zero continuation values retained in RZ1 are
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2r)=
\frac{r(2r+1)(-1)^r\pi^r}{2r!}\zeta'(-2r),
\qquad r=1,2,\ldots .
\tag{BCC8.4}
\]
They are not discarded when using the quotient (BCC8.2). Formula (BCC8.4) follows directly at the negative even points by multiplying
\(\Gamma(s/2)=2(-1)^r/(r!(s+2r))+O(1)\)
with
\(\zeta(s)=\zeta'(-2r)(s+2r)+O((s+2r)^2)\)
and evaluating every remaining factor. At zero the leading factors
\(s(s-1)/8\), \(2/s\), and \(\zeta(0)=-1/2\) give \(1/8\); at one the zeta residue one and \(\pi^{-1/2}\Gamma(1/2)=1\) give \(1/8\). These are comparisons with the original zeta, not a replacement of the working zeta.

Since BCC5 identifies the entire original zeta functions, the branch zero data and ideals coincide. The branch map on the actual quotient is therefore
\[
I_A:\mathcal Q_i\xrightarrow{\sim}\mathcal Q_j,\qquad
[F]_i\longmapsto[F]_j.
\tag{BCC8.5}
\]
Equality of ideals makes this well defined, the identity on \(\mathcal B\) provides the inverse and continuity in both directions, and no spectral variable is changed.

For the actual operators
\[
L[F]=[sF(s)],\qquad T_a[F]=[a^sF(s)]\quad(a>0),
\tag{BCC8.6}
\]
one has
\[
I_A L_i=L_j I_A,\qquad I_A T_{a,i}=T_{a,j}I_A.
\tag{BCC8.7}
\]
Here \(a^s=\exp(s\log a)\) uses the real logarithm. Multiplication by \(s\) is continuous on (BCC8.1) because its extra growth is absorbed by raising \(M\) by one and a strip-dependent constant. Multiplication by \(a^s\) is bounded on that strip by \(\max(a^A,a^{-A})\). Both preserve the zero vanishing orders in (BCC8.2). These facts prove the operators and the identities on the quotient, including \(T_{1/n}\) for every recovered positive integer \(n\). Their exact source-space action at those integers remains the proved RZ formula
\[
\mathcal M^{-1}T_n\mathcal M\,k(u)=n^{1/2}k(u/n);
\tag{BCC8.8}
\]
its factor \(n^{1/2}\) is retained. Explicitly, the source space and transform appearing here are
\[
\mathcal A=\left\{k\in C^\infty(\mathbb R_{>0}):
 \sup_{u>0}(u^N+u^{-N})|(u\partial_u)^j k(u)|<\infty
 \quad(N,j\geq0)\right\},
\]
\[
\mathcal M k(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u}.
\tag{BCC8.8a}
\]
The existing synthesis proof identifies \(\mathcal M:\mathcal A\to\mathcal B\) topologically. The dilation identity itself can be checked directly: substituting \(u=nv\) gives
\[
\mathcal M\!\left(n^{1/2}k(u/n)\right)(s)
=\int_0^\infty n^{1/2}k(v)(nv)^{s-1/2}\frac{dv}{v}
=n^s\mathcal Mk(s).
\tag{BCC8.8b}
\]
Absolute convergence follows from the defining decay at both ends of \(\mathcal A\). For the specific retained multiplier (BCC8.3), the source element from RZ1 is
\[
k_0(u)=u^{1/2}\sum_{n\geq1}f_0(nu),\qquad
f_0(v)=\frac{\pi}{2}v^2(2\pi v^2-3)e^{-\pi v^2},
\qquad \mathcal M k_0=F_0.
\tag{BCC8.8c}
\]
These full source formulas are unchanged under the branch identity.

The multiplicity block at an actual zero \(\rho\) is the jet algebra
\[
\mathcal Q_\rho\simeq
\mathbb C[\epsilon_\rho]/(\epsilon_\rho^{m_\rho}),
\quad
L_\rho=\rho+\epsilon_\rho,
\quad
T_{n,\rho}
=n^\rho\sum_{r=0}^{m_\rho-1}
\frac{(\log n)^r}{r!}\epsilon_\rho^r
\tag{BCC8.9}
\]
from the RZ projector construction. The last identity is the Taylor expansion of \(n^s=n^\rho\exp((s-\rho)\log n)\) in the full multiplicity algebra. It keeps every nilpotent term. The branch comparison (BCC8.5) is the identity on this actual block.

The original-zeta reflection has
\[
\rho^\#=1-\overline\rho,\qquad m_{\rho^\#}=m_\rho,
\qquad
JF(s)=\overline{F(1-\overline s)}.
\tag{BCC8.10}
\]
The zero symmetry with multiplicities is the actual original-zeta input in RZ and WR7, with the full analytic multiplier (BCC8.3) retained. It is not an assumption that \(\rho^\#=\rho\). The map \(J\) preserves \(\mathcal B\), since reflection changes the strip bound \(A\) to at most \(A+1\), and it preserves the ideal by (BCC8.10). On the full zero block it is exactly
\[
J_\rho\!\left(\sum_{r=0}^{m_\rho-1}c_r\epsilon_\rho^r\right)
=\sum_{r=0}^{m_\rho-1}(-1)^r\overline{c_r}\,
\epsilon_{\rho^\#}^r.
\tag{BCC8.11}
\]
Indeed \(s-\rho\) is sent to \(-(s-\rho^\#)\). Applying (BCC8.11) twice is the identity, so no jet data are lost.

Direct multiplication, with all coefficients retained, proves
\[
J_\rho L_\rho=(1-L_{\rho^\#})J_\rho,
\qquad
J_\rho T_{n,\rho}
=n\,T_{1/n,\rho^\#}J_\rho.
\tag{BCC8.12}
\]
For the first equation both multipliers are
\(\overline\rho-\epsilon_{\rho^\#}\), since
\(1-\rho^\#=\overline\rho\).
For the second, both multipliers on the image of \(J_\rho\) are
\[
n^{\overline\rho}
\sum_{r=0}^{m_\rho-1}
\frac{(-\log n)^r}{r!}\epsilon_{\rho^\#}^r.
\tag{BCC8.13}
\]
The factor \(n\) on the right side of (BCC8.12) is essential.

The branch identity also commutes with \(J\):
\[
I_AJ_i=J_jI_A.
\tag{BCC8.14}
\]
It commutes with every actual zero projector \(P_\rho\) in RZ. Its full representative formula is
\[
A_\rho(s)=\frac{F_0(s)}{(s-\rho)^{m_\rho}},\qquad
\mathscr P_\rho F(s)=
A_\rho(s)\sum_{r=0}^{m_\rho-1}
\frac{(F/A_\rho)^{(r)}(\rho)}{r!}(s-\rho)^r,
\qquad
P_\rho[F]=[\mathscr P_\rho F].
\tag{BCC8.14a}
\]
The quotient \(F/A_\rho\) is holomorphic near \(\rho\), because \(A_\rho(\rho)\neq0\); its derivatives in this formula are local derivatives there. RZ6–RZ7 supply the global membership and projector proof on \(\mathcal B/\mathcal I\). In the branch comparison, every factor, derivative, original zero, and multiplicity in (BCC8.14a) is identical, proving the stated commutation without dropping the full multiplier.

Consequently the complete branch comparison retains each actual zero and each full reflected orbit
\[
\{\rho,\,1-\overline\rho\}.
\tag{BCC8.15}
\]
It does not identify the two members by discarding their parameter values. The exact scalar defect of individual fixedness is
\[
\Delta_\rho
=(\rho-\rho^\#)^2
=(2\operatorname{Re}\rho-1)^2.
\tag{BCC8.16}
\]
Under reflection, the difference changes sign, so its square is unchanged. Under the branch identity (BCC8.5), every original parameter is unchanged, so this defect is unchanged as well. Its vanishing is equivalent to \(\rho=\rho^\#\), or \(\operatorname{Re}\rho=1/2\). Formula (BCC8.16) does not assert that an off-critical zero exists; it computes exactly what this faithful comparison would retain at any actual zero.

Finally, retained supporting labels remain a disjoint family. For any specified label bijection \(\beta:\mathcal L_i\to\mathcal L_j\), define
\[
\widehat{\mathcal Q}_i
=\coprod_{\ell\in\mathcal L_i}\{\ell\}\times\mathcal Q_i,
\qquad
\widehat I_A(\ell,q)=(\beta(\ell),I_Aq).
\tag{BCC8.17}
\]
Its inverse is \((\ell',q')\mapsto(\beta^{-1}\ell',I_A^{-1}q')\). Thus distinct labelled zero sections \((\ell,0)\) remain distinct. No tensor product is used to claim that a zero coefficient retains a basis label.

## BCC9. What the calculated comparison establishes

The branch comparison derived here has the complete map chain
\[
\begin{array}{ccccc}
(E_i,t_i,G_i,\delta_i)&\longrightarrow&
(R_i,\operatorname{Spec}R_i,N_i)&\longrightarrow&
(\mu_i,\operatorname{Exp}_*\mu_i,\zeta_i)\\
\downarrow(\phi,A)&&\downarrow(C_A,\operatorname{Spec}(C_A^{-1}),N)&&
\downarrow\text{transport}\\
(E_j,t_j,G_j,\delta_j)&\longrightarrow&
(R_j,\operatorname{Spec}R_j,N_j)&\longrightarrow&
(\mu_j,\operatorname{Exp}_*\mu_j,\zeta_j).
\end{array}
\tag{BCC9.1}
\]
The left column requires the full event comparison and uses each branch's own globally recovered counter. BCC2 proves every count and event fibre. BCC3 proves the arithmetic ring comparison with the orientation sign retained. BCC4 proves the full normed spectrum comparison. BCC5–BCC6 prove the original-zeta equality, all repetitions, and the unit term, separately in each branch.

This class of complete cyclic histories is therefore quotientable in the user's separate-counter sense. The proof classifies all real-linear duration comparisons within this class; it does not assert that every conceivable zeta-preserving deformation is one of these maps.

The effect on the actual spectral receiver is also determined: it is (BCC8.5), which preserves every actual \(\rho\), every multiplicity, all jets, all labels, and the defect (BCC8.16). The degree-weighted reflected action is (BCC7.8) and (BCC8.12). Thus preservation of the same complete original zeta and individual fixedness under that reflected action are two explicit mathematical operations with a calculated comparison. The former map preserves the latter's defect; it does not make the defect vanish.

This is not a claim that the full intended construction has been refuted. It identifies the exact information retained by the stated branch quotient, including precisely the character and zero-jet data that cannot be removed while claiming that this quotient is faithful to the same original zeta.

Independent mathematical check: the cyclic comparison, all count and endomorphism formulas, quotient cardinalities, character inversion, and the evaluation sign were independently rederived. The checker specifically confirmed the positive-forward-time restriction, the distinction between the counter isomorphism and the zero group quotient, and the need for an event-fibre comparison in addition to an endomorphism-ring comparison. A subsequent independent audit checked BCC5–BCC8, including the convolution exponential, signed character compensation, full jet conjugation, and defect preservation. It identified two presentation defects, now corrected: the operator domain includes every positive real \(a\) so that \(T_{1/n}\) is defined, and the downward spectrum map in (BCC9.1) is \(\operatorname{Spec}(C_A^{-1})\), with the required contravariance retained.
