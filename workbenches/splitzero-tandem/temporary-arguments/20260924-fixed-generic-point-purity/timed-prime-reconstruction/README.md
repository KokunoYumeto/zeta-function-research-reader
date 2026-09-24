# First-appearance time, primitive periods, and the original zeta function

## Online proof edition

This is the complete TP0–TP14 derivation from the programme's **Split Zero to GCT bridge** task, not a new result attributed to its publication task. It constructs the arithmetic unit from the full signed stalk's winding quotient, identifies prime clocks, and proves that the complete prime-return measure reconstructs the original Riemann zeta function on its half-plane of absolute convergence. The unit term, prime two, every prime-power repetition, sign branches, and the source periods are retained.

**[Complete LaTeX source](README.tex).** The mathematical body below is preserved in full; three local source locators were converted into public citations. No new PDF build or Lean certification is claimed by this edition.

The supporting fixed-point proof is already public: **[CC1–CC5: the generic point and absence of an equivariant mirror-parity label](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6bc7202eceb05d1a482d495ad302803a80b5aeca/workbenches/splitzero-tandem/temporary-arguments/20260924-fixed-generic-point-purity/prime-clocks-p14/CC_FIXED_GENERIC_POINT_AND_MIRROR_PARITY.md)**. Its winding-parity calculation is **[W2](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6bc7202eceb05d1a482d495ad302803a80b5aeca/workbenches/splitzero-tandem/temporary-arguments/20260924-fixed-generic-point-purity/prime-clocks-p14/WINDING_PARITY_AND_INTEGER_SPECTRUM.md#L55-L85)**. Those are preceding results, not discoveries of this edition. The original human geometry is Connes–Consani's [absolute twistor construction](https://arxiv.org/html/2609.00299v1) and [absolute geometry of Spec Z](https://arxiv.org/html/2606.06604v1). The Euler product and logarithmic derivative recovered below are classical identities; the note proves their precise realization from the programme's retained clock data. It does not assert RH or infer arithmetic purity from these transform identities.

---

24 September 2026. Independent mathematical derivation for the current programme. Result identifiers TP0–TP14.

The user's clarification is that integer `1` supplies the counting step, while the appearance times of new prime channels distinguish those channels. The subsequent correction requires the whole unlabelled structure first: one, two, three, and prime labels must then be outputs of its arithmetic construction, not preassigned observations used to manufacture a unit. TP0 supplies that order of construction. The later sections prove the exact maps from the resulting timed record to the periodic curves in Connes–Consani and to the original Riemann zeta function on its domain of absolute convergence. They retain integer zero, the unit, prime two, every prime-power return, and every multiplicity.

The supporting datum is written

\[
\tau\langle Z_1;\text{no }Z_2\rangle.
\]

No addition, subtraction, coordinate, vector, metric, or distance is assigned to this datum. All counts, group operations, times, coordinates and measures below belong to the indicated winding group, clocks, source curves, or real half-line. In particular, the count `1` is not identified with this supporting datum. The earlier retracted expression \(\tau+\tau=\tau\) is not used.

## Sources and actual reading

1. Connes–Consani, [arXiv:2606.06604v1](https://arxiv.org/html/2606.06604v1), original author file `FF.tex (original author source, arXiv:2606.06604v1)`, lines 1550–1633 read for this derivation. The source supplies \(E_p=\mathbb C^\times/p^{\mathbb Z}\), the scaling generator \(z\mapsto pz\), its real structure, the product with the phase circle, and the full differential \(dz/z=d\lambda/\lambda+i\,d\theta\). The source parameter called `tau` in its modular-parameter formula is distinguished below as \(\tau_p^{\rm mod}\); it is not the user's supporting datum.
2. [Prime clocks, orchard visibility, and faithful prime observations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6bc7202eceb05d1a482d495ad302803a80b5aeca/workbenches/splitzero-tandem/temporary-arguments/20260924-fixed-generic-point-purity/prime-clocks-p14/PRIME_CLOCKS_ORCHARD_AND_SPECTRUM.md), P9–P14 read in full. P1–P3 were also read. The present note supplies complete proofs of the timed sieve, reconstruction, period maps and zeta identities it asserts; it does not infer a result from a search hit.
3. [Winding data at the fixed point: parity, the integer ring, and its spectrum](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6bc7202eceb05d1a482d495ad302803a80b5aeca/workbenches/splitzero-tandem/temporary-arguments/20260924-fixed-generic-point-purity/prime-clocks-p14/WINDING_PARITY_AND_INTEGER_SPECTRUM.md), W1–W3 read for the whole-source reconstruction. The original signed group and its quotient are reproduced below; the four branch states are retained in the exact sequence.

These calculations are not a novelty claim. They apply elementary arithmetic and the displayed source curves to the user's specified timed observation. They do not substitute a completed or rescaled zeta function for the original function.

## TP0. The whole source precedes numerical labels and the unit is intrinsic

Start from the entire source group of nonabsorbing generic sections, with its source relations retained:

\[
G=\langle T,J,\epsilon\mid TJ=JT,\ T\epsilon=\epsilon T,
\ J\epsilon=\epsilon J,\ J^2=\epsilon,\ \epsilon^2=1\rangle.
\]

The source also has a separate absorbing element, which is not a group element and is not identified here with the supporting point. Sending \(T\) to \((1,\bar0)\), \(J\) to \((0,\bar1)\), and \(\epsilon\) to \((0,\bar2)\) defines an isomorphism

\[
G\longrightarrow\mathbb Z\times\mathbb Z/4\mathbb Z.
\]

Indeed, the displayed images satisfy every relation. The inverse sends \((m,\bar k)\) to \(T^mJ^k\), is independent of the representative of \(\bar k\) because \(J^4=1\), and both compositions fix the generators. This comparison checks the source group's structure; it does not assert that the numerical labels have been observed by running the proposed clock.

The subgroup of finite-order elements is intrinsically

\[
H=\operatorname{Tor}(G)=\{1,J,\epsilon,\epsilon J\}.
\]

Proof: a finite positive power of \((m,\bar k)\) can be the identity only if \(m=0\), and all four elements with that property have finite order. Retain the exact sequence

\[
1\longrightarrow H\longrightarrow G\xrightarrow{q}L:=G/H\longrightarrow1.
\]

The quotient \(L\) is an infinite cyclic group. Regard it initially without a marked generator. The choice of source presentation can later exhibit a generator, but the following arithmetic ring and its identity do not depend on that choice.

Define

\[
E=\operatorname{End}_{\rm Ab}(L),
\qquad
(f\oplus g)(x)=f(x)g(x),
\qquad
(f\odot g)(x)=f(g(x)).
\]

Because \(L\) is abelian, the pointwise product of two homomorphisms is a homomorphism. Addition is associative and commutative; its zero is \(0_E:x\mapsto1_L\), and the additive inverse of \(f\) is \(x\mapsto f(x)^{-1}\). Composition is associative and has the distinguished identity

\[
\mathbf1_E=\operatorname{id}_L.
\]

For left distributivity, evaluate \(f(g(x)h(x))=f(g(x))f(h(x))\); right distributivity follows by evaluating a pointwise product at \(h(x)\). These prove that \(E\) is a unital ring. No numeral has been selected by inspecting early prime events: \(\mathbf1_E\) is already distinguished as the identity operation on the whole source. It differs from \(0_E\) because \(L\) is nontrivial.

For a proof of its arithmetic structure, choose either generator \(u\) of the infinite cyclic group temporarily. Any endomorphism has \(f(u)=u^n\) for a unique integer \(n\), and the homomorphism law then forces \(f(u^m)=u^{nm}\). Conversely every map \([n]:x\mapsto x^n\) is an endomorphism. Its exponent on the other generator \(u^{-1}\) is still \(n\), since \(f(u^{-1})=u^{-n}=(u^{-1})^n\). The resulting isomorphism

\[
\mathbb Z\xrightarrow{\sim}E,\qquad n\longmapsto[n],
\]

is therefore independent of which generator was used to prove it. Evaluation gives \([n]\oplus[m]=[n+m]\), \([n]\odot[m]=[nm]\), \([0]=0_E\), and \([1]=\mathbf1_E\). Thus the count labels describe an arithmetic object obtained from the entire source, rather than serving as a calibration assumption.

The nonnegative part \(E_+\) is the additive submonoid generated by \(\mathbf1_E\), including its empty sum \(0_E\). Its successive elements are distinct: equality of two different finite sums would give two unequal powers of a generator the same value. It follows from the preceding classification that \(E_+\) corresponds exactly to the nonnegative integers. In particular, \(\mathbf1_E\) is its unique nonzero element that cannot be expressed as a sum of two nonzero elements of \(E_+\): in the exponent description one is not a sum of two positive integers, whereas every integer \(n\ge2\) is \(1+(n-1)\).

For a nonzero \(f\in E_+\), define its winding clock intrinsically as the cokernel

\[
C_f=L/f(L).
\]

If \(f=[n]\), the representatives \(1_L,u,\ldots,u^{n-1}\), with division of exponents by \(n\), show that it has exactly \(n\) elements. This order does not depend on the chosen generator. The unit \(\mathbf1_E\) has trivial cokernel. A positive nonunit \(f\) has nonzero simple cokernel exactly when its resulting degree label \(n\) is prime, by the full subgroup argument in TP4. Thus the prime objects too are intrinsic to the reconstructed ring and its quotient clocks; their numerical names can be supplied after this construction.

There is also an intrinsic formulation of the statement that one divides everything. Define \(a\mid b\) in \(E_+\setminus\{0_E\}\) by the existence of \(c\in E_+\) with \(b=a\odot c\). The identity divides every \(b\). Conversely an element dividing every positive element divides \(\mathbf1_E\). Under the proved ring isomorphism, the equation \(ac=1\) with positive integer degrees forces both degrees to be one, so this element is exactly \(\mathbf1_E\). The full ring has two units, \(\mathbf1_E\) and \(-\mathbf1_E\); only the first lies in \(E_+\).

Parity can now be expressed without using a prime label to found the unit. Form the intrinsic doubling endomorphism \(\mathbf1_E\oplus\mathbf1_E\) and the quotient by its image. The quotient has two elements, as the cyclic-group calculation shows. Every \(f\in E\) induces either its zero map or its identity map; in the exponent coordinates those are respectively even and odd. In particular \(\mathbf1_E\) has the odd \(Z_2\) state. The source point is not a member of this ring of maps and is assigned no parity by this construction.

This proves a construction from the full signed source and its winding quotient. That source already supplies an infinite cyclic direction; this proof does not derive its existence from a datum consisting only of \(\tau\langle Z_1;\text{no }Z_2\rangle\). The whole structure used here and an observer's finite record of that structure are different stages. The finite record and its exact infinite limit are calculated in TP11. Neither the construction nor that limit proves that an observer must wait through infinitely many ticks before an identity operation exists. In particular, no subtraction of two already labelled prime times is used to establish \(\mathbf1_E\).

The user's further permitted possibility of future observations falling off a currently inferred integer grid is a question about extending a partial observation, not about evaluating a fixed endomorphism of the already specified complete cyclic group. TP0 does not certify the complete source group from any finite event prefix. Its input is the complete Connes–Consani group and the retained exact sequence. The identity map would still exist for a different source group; the proof that every endomorphism is an integral multiple of it specifically uses the cyclic structure. This is the interface with the separate calculation of source extensions and the global counting unit.

## TP1. The retained count and the parity observation have different periods

After TP0's construction, the oriented-ray covering gives the following geometric realization of its winding quotient:

\[
\mathbb C^\times/\mathbb R_{>0}\longrightarrow
\mathbb C^\times/\mathbb R^\times.
\]

An angle on the first space has period \(2\pi\); an angle on the second has period \(\pi\). Fix a reference line and a ray above it. A loop of lines has a real angle lift starting at zero, with endpoint \(n\pi\) for a unique integer \(n\). A homotopy of based loops preserves \(n\), since its lifted endpoint varies continuously in the discrete set \(\pi\mathbb Z\). Conversely two lifted paths with the same endpoints are homotopic by linear interpolation, whose projection is a based homotopy. Concatenation adds endpoint angles. This proves that the winding classes form an infinite cyclic group

\[
L=\langle t\rangle=\{t^n:n\in\mathbb Z\}.
\]

The lifted ray has returned to its initial orientation exactly when \(n\) is even. Thus its parity observation is

\[
\operatorname{par}(t^n)=n\bmod 2.
\]

The forward counting step is the map

\[
S(t^n)=t^{n+1}.
\]

It has infinite order, because \(t^n\ne t^{n+r}\) for \(r\ne0\). On parity it induces the two-state exchange. After two steps the parity returns, while the retained count has increased by two. Consequently the full operation carrying history is not an order-two map; its observation on the ray states is order two. The term “torsion” in the user's description refers here to retained winding, not to a finite-order element of \(L\).

The state \(t^0\) has count zero. It is the identity of this winding group, not \(\tau\langle Z_1;\text{no }Z_2\rangle\). The elementary increment `1` has \(Z_2\) state odd. None of this assigns parity to the supporting datum.

## TP2. Unit time and the return test

Choose the forward progression \(0,1,2,\ldots\) supplied by TP1. A time in this paragraph is an integer tick, not physical time. At a fixed positive integer \(d\), the quotient clock is

\[
C_d=L/\langle t^d\rangle.
\]

Its state at tick \(n\) is the class of \(t^n\). It is at its initial state exactly when \(t^n\in\langle t^d\rangle\), which is exactly the integer divisibility condition \(d\mid n\). Thus the test can be implemented by advancing a finite clock one state at every unit tick and checking for return. It does not require the list of primes as input.

The progression and the periodic-return rule are both data of this construction. A successor sequence with no specified return or divisibility test would not by itself select prime ticks. Here the specified test is the already constructed quotient-clock return, so the selection rule has an exact domain and meaning.

Repeated application of `1` distinguishes every consecutive tick. Multiplication of positive counts is the repeated-addition operation \(a b=b+\cdots+b\), with \(a\) summands. Division with remainder follows by taking the greatest \(q\) such that \(dq\le n\): the nonnegative remainder \(r=n-dq\) satisfies \(0\le r<d\), since otherwise \(d(q+1)\le n\). Uniqueness follows by subtracting two such descriptions and using that a nonzero multiple of \(d\) has absolute value at least \(d\). These are operations on counts, not on the supporting datum.

## TP3. The sequential first-appearance recurrence produces precisely the primes

Let \(A_1=\varnothing\). Suppose that ticks through \(n-1\) have been processed, for an integer \(n\ge2\). Define

\[
B_n=\{d\in A_{n-1}:d\mid n\},
\qquad
\epsilon_n=\begin{cases}1,&B_n=\varnothing,\\0,&B_n\ne\varnothing,\end{cases}
\]

and

\[
A_n=\begin{cases}A_{n-1}\cup\{n\},&\epsilon_n=1,\\A_{n-1},&\epsilon_n=0.\end{cases}
\]

When \(d\) is first activated at tick \(d\), its clock is in the initial state. After \(n-d\) subsequent unit steps it is again in that state exactly when \(d\mid n-d\), equivalently \(d\mid n\). Therefore this recurrence agrees with the physical description “advance every active clock; create a new line only if none returns now.” All overlapping returns are retained in \(B_n\).

**Claim.** For every \(n\ge1\), \(A_n\) consists exactly of the primes at most \(n\).

**Proof.** The assertion is true at \(n=1\), and tick two activates because the active set is empty. Assume it holds through \(n-1\). A prime \(n\) has no divisor strictly between one and itself, so no member of \(A_{n-1}\) divides it and it activates. If \(n\) is composite, let \(p>1\) be its least divisor greater than one. If \(p=ab\) with \(1<a<p\), then \(a\mid n\), contradicting its minimality. Hence \(p\) is prime; compositeness gives \(p<n\). By induction its clock is already active and returns at \(n\), so \(n\) does not activate. This proves the claim by induction. \(\square\)

For the first several ticks,

| Tick \(n\) | Returning earlier prime channels \(B_n\) | New line |
|---:|:---|:---|
| 1 | no prime channel is tested | none; this is the unit |
| 2 | none | 2 |
| 3 | none | 3 |
| 4 | 2 | none |
| 5 | none | 5 |
| 6 | 2 and 3 | none |
| 7 | none | 7 |
| 8 | 2 | none |
| 9 | 3 | none |
| 10 | 2 and 5 | none |
| 11 | none | 11 |

In particular, two conceals the newness of four but does not remove tick four. The unit increments still record its occurrence.

## TP4. Why one is not a prime channel and does not cover everything

The clock \(C_1=L/L\) has one state and is the trivial group. It returns at every tick. If it were inserted into \(A_1\), then \(1\mid n\) for every \(n\), so the recurrence would create no prime channels at all. The stated recurrence excludes this trivial clock by testing ticks \(n\ge2\) and admitting only nontrivial clocks.

This exclusion is dictated by the exact prime criterion, rather than by an exception to that criterion. Every subgroup of \(L\) is \(\langle t^d\rangle\) for a unique \(d\ge0\): choose the least positive exponent in a nontrivial subgroup and apply division with remainder. Subgroups of \(C_n\) are consequently the images of these subgroups for divisors \(d\mid n\). Thus

\[
n\text{ is prime}
\quad\Longleftrightarrow\quad
C_n\text{ is a nontrivial simple cyclic group}.
\]

Indeed, for prime \(n\), its only divisors are one and \(n\), so the quotient has only the whole group and the identity subgroup. If \(n=ab\) with \(a,b>1\), the subgroup generated by \(t^a\) in \(C_n\) has \(b\) elements and is proper and nontrivial. The case \(n=1\) is excluded by “nontrivial.”

Equivalently, the winding-scale map \([n]:t^m\mapsto t^{nm}\) has image index \(n\); composition obeys \([a][b]=[ab]\). The map \([1]\) is invertible, and a prime is a noninvertible positive-degree map that does not factor into two noninvertible positive-degree maps. The ideal \((1)\) is the entire integer ring, not a proper prime ideal. These equivalent unit distinctions explain why the counting increment can be indispensable while not being a prime event.

## TP5. The complete timed record is equivalent to the anchored waiting times

The prime set is infinite. To prove this, a finite purported complete list \(p_1,\ldots,p_r\) would give \(M=p_1\cdots p_r+1>1\). Its least divisor greater than one is a prime by TP3's argument and cannot equal any \(p_j\), since division of \(M\) by \(p_j\) leaves remainder one. This is a contradiction.

Let \(p_1<p_2<\cdots\) be the activation ticks proved in TP3; \(p_1=2\). Anchor elapsed time at the unit tick `1`. Then define

\[
e_j=p_j-1,\qquad
g_1=p_1-1=1,\qquad
g_j=p_j-p_{j-1}\quad(j\ge2).
\]

The exact inverse formulas are

\[
e_j=\sum_{r=1}^{j}g_r,
\qquad
p_j=1+\sum_{r=1}^{j}g_r,
\qquad
\epsilon_n=\mathbf1_{\{p_1,p_2,\ldots\}}(n).
\]

The first two formulas telescope; the final formula is TP3. Conversely the indicator's successive ticks where it is one give the \(p_j\), and adjacent subtraction gives the gaps. Hence the unit-anchored waiting sequence, the timed binary event record, and the increasing list of prime labels determine one another exactly.

For example, the first waiting times from tick one are

\[
1,1,2,2,4,2,4,2,4,6,\ldots,
\]

giving prime ticks \(2,3,5,7,11,13,17,19,23,29,\ldots\). If elapsed time is anchored instead at count zero, the first wait is two and all subsequent gaps are unchanged. The origin convention must be retained: gap lengths without the first absolute or anchored event locate events only up to an additive shift, and an unordered collection of gaps also loses their order. Neither loss occurs in the recorded sequential history.

Thus the statement “the information is in the time intervals” has a precise content: the ordered waiting times with their anchor retain every prime label. It is not necessary to assign different geometric radii to the channels to distinguish them.

## TP6. The timed prime record reconstructs every multiplicity

Every integer \(n>1\) is a product of primes. Proof by induction: a prime is already such a product; a composite \(n=ab\) with \(1<a,b<n\) is a product of the prime products supplied by induction for \(a,b\).

For uniqueness, first prove Euclid's lemma. If a prime \(p\) does not divide \(a\), the Euclidean algorithm gives integers \(u,v\) with \(up+va=1\). Here the Euclidean algorithm terminates because successive nonzero remainders strictly decrease; tracing the remainder identities backwards expresses the greatest common divisor as an integer combination. The gcd of \(p,a\) is one because it divides the prime \(p\) and is not \(p\). Multiplying by \(b\) shows that \(p\mid ab\) implies \(p\mid b\). Applying the lemma repeatedly to two prime decompositions shows that the first prime in one equals a prime in the other; cancelling that positive factor and inducting gives equality of all prime multiplicities.

Consequently, the labels reconstructed in TP5 give the unique data

\[
n=\prod_p p^{v_p(n)},\qquad
v_p(n)\in\mathbb N_0,
\]

with finitely many nonzero \(v_p(n)\). The unit one has every exponent zero. The integer zero is not represented by a finite product of positive primes, and negative integers require a separate sign. Neither is silently included in the positive-integer product below. This is exactly the domain required by the original zeta Dirichlet series.

An individual returning prime-clock state records divisibility, not the exponent \(v_p(n)\). The reconstruction retains multiplicities through successive division, or equivalently through the complete prime-power clocks \(C_{p^r}\): \(v_p(n)\) is the greatest \(r\ge0\) for which that clock returns at \(n\). No prime-power observation is deleted.

## TP7. The same prime label determines a primitive period in the source curve

For each recovered prime \(p\), retain the Connes–Consani source object

\[
E_p=\mathbb C^\times/p^{\mathbb Z}.
\]

Let \([z]\) denote the equivalence class of \(z\ne0\). Positive real scaling supplies the real-parameter flow

\[
\Phi_t([z])=[e^t z],\qquad t\in\mathbb R.
\]

It is well defined because replacing \(z\) by \(p^m z\) replaces its image by \(p^m e^t z\). The exponential law gives \(\Phi_{t+u}=\Phi_t\Phi_u\). For every \([z]\),

\[
\Phi_t([z])=[z]
\iff e^t z=p^kz\text{ for some }k\in\mathbb Z
\iff t=k\log p.
\]

The primitive positive period is therefore

\[
\lambda_p=\log p.
\]

The positive, zero and negative returns are all retained as the full subgroup \(\lambda_p\mathbb Z\). The connected positive real orbit is \(C_p=\mathbb R_{>0}/p^{\mathbb Z}\), and \(u\mapsto[e^u]\) identifies it with \(\mathbb R/(\lambda_p\mathbb Z)\).

In polar coordinates \(z=r e^{i\theta}\), the full source one-form is

\[
\frac{dz}{z}=\frac{dr}{r}+i\,d\theta.
\]

The scaling cycle has integral \(\int_1^p dr/r=\log p\); the positive phase cycle has integral \(\int_0^{2\pi}i\,d\theta=2\pi i\). Thus the logarithmic coordinate \(u\mapsto e^u\) has deck lattice

\[
\lambda_p\mathbb Z+2\pi i\mathbb Z.
\]

With the source's alternative exponential coordinate \(z=e^{2\pi i w}\), the same lattice is

\[
\mathbb Z+\mathbb Z\tau_p^{\rm mod},
\qquad \tau_p^{\rm mod}=i\frac{\log p}{2\pi}.
\]

The basis vector \(\tau_p^{\rm mod}\) exponentiates to \(1/p\), rather than \(p\); its negative exponentiates to \(p\). Both generate the same subgroup \(p^{\mathbb Z}\). This preserves the sign and the factor \(2\pi\) in the source convention.

These are coordinates and periods of \(E_p\), not coordinates or a numerical distance from \(\tau\langle Z_1;\text{no }Z_2\rangle\).

## TP8. Integer event time and logarithmic return time have an exact comparison

For the activation list recovered in TP5,

\[
p_j=1+\sum_{r=1}^{j}g_r,
\qquad
\lambda_{p_j}=\log\!\left(1+\sum_{r=1}^{j}g_r\right).
\]

The inverse is \(p_j=e^{\lambda_{p_j}}\). Therefore no prime label is lost in passing from the exact primitive-period list to the activation list. For \(j\ge2\),

\[
\lambda_{p_j}-\lambda_{p_{j-1}}
=\log\!\left(1+\frac{g_j}{p_{j-1}}\right).
\]

An additive prime gap \(g_j\) and a primitive orbit period \(\log p_j\) are thus different data with this proved comparison; they are not set equal.

The logarithmic length of a positive integer is

\[
\ell(n)=\log n=\sum_p v_p(n)\log p.
\]

This follows by applying the logarithm to TP6's finite product. The equality \(\ell(ab)=\ell(a)+\ell(b)\) follows from the positive-real exponential law. It is this multiplication-to-addition map that converts the \(k\)-fold prime repetition into return time

\[
k\lambda_p=k\log p=\log(p^k).
\]

At integer tick \(n\), a prime clock returns if \(p\mid n\); those times include \(p,2p,3p,\ldots\). A repetition of the scaling orbit has positive logarithmic time \(k\log p\) and corresponds to \(p^k\). Both structures are retained: the first is the divisibility-clock observation used to discover prime channels, while the second is repetition in the source's multiplicative scaling orbit.

Prime two is present throughout: it activates at tick two, has \(\lambda_2=\log2\), and returns at \(k\log2\) for every integer \(k\). This does not assert the existence of an even-degree lift through the separate signed source action discussed in P13–P14; the obstruction there does not remove the prime-two curve or any of these returns.

## TP9. Exact measures of primitive events, repetitions and all counts

Write \(\delta_a\) for the unit point measure at real time \(a\). Define the following positive measures on their stated time spaces:

\[
\begin{aligned}
\mathcal E&=\sum_p\delta_p &&\text{on integer event time},\\
\mathcal P&=\sum_p\delta_{\log p} &&\text{on positive logarithmic time},\\
\mathcal R&=\sum_p\sum_{k\ge1}\frac1k\,\delta_{k\log p}
&&\text{on positive logarithmic time},\\
\mathcal W&=\sum_p\sum_{k\ge1}(\log p)\,\delta_{k\log p}
&&\text{on positive logarithmic time},\\
\mathcal D&=\sum_{n\ge1}\delta_{\log n}
=\delta_0+\sum_{n\ge2}\delta_{\log n}
&&\text{on nonnegative logarithmic time}.
\end{aligned}
\]

Every one of these measures is locally finite. For a compact logarithmic interval \([0,T]\), a contributing prime satisfies \(p\le e^T\) and a contributing repetition satisfies \(k\le T/\log p\); there are finitely many such integers. A contributing general count satisfies \(n\le e^T\), again a finite set. The same argument on a bounded interval of integer event time proves local finiteness of \(\mathcal E\).

The primitive measure satisfies \(\mathcal P=(\log)_*\mathcal E\), by evaluating both sides on an arbitrary Borel set. Multiplication of a measure by its time coordinate gives the exact identity

\[
\mathcal W=t\,\mathcal R,
\]

since at the \(k\)-th return, \(t/k=(k\log p)/k=\log p\). No coefficient has been suppressed. If two positive returns have equal time, \(k\log p=l\log q\), then \(p^k=q^l\); uniqueness of factorization gives \(p=q\) and \(k=l\). Thus distinct prime-power labels do not collide in this time representation.

Define \(\Lambda(1)=0\), \(\Lambda(p^k)=\log p\) for \(k\ge1\), and \(\Lambda(n)=0\) for other positive integers. Then

\[
\mathcal W=\sum_{n\ge2}\Lambda(n)\delta_{\log n},
\qquad
\mathcal R=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}\delta_{\log n}.
\]

The coefficients \(1/k\) and \(\log p\) are derived from the full counting measure in TP10–TP12; they are not claimed to follow merely from the existence of a periodic orbit.

## TP10. Recovering the full count measure, including its unit atom

For each prime retain the locally finite measure

\[
\mathcal D_p=\sum_{k\ge0}\delta_{k\log p}.
\]

For a finite set of primes \(F\), its convolution product is

\[
\mathcal D_F=\underset{p\in F}{*}\mathcal D_p
=\sum_{(k_p)\in\mathbb N_0^F}
\delta_{\sum_{p\in F}k_p\log p}.
\]

Convolution of point measures obeys \(\delta_a*\delta_b=\delta_{a+b}\). Local finiteness follows from the finite range of exponents contributing to a bounded time interval. TP6 and TP8 give

\[
\mathcal D_F=
\sum_{\substack{n\ge1\\p\mid n\Rightarrow p\in F}}
\delta_{\log n}.
\]

Every coefficient is one because factorization is unique. The exponent tuple with every entry zero contributes exactly \(\delta_0\), the unit count one.

There is also an exact convolution-exponential identity

\[
\boxed{\mathcal D=\exp_*(\mathcal R)
:=\delta_0+\sum_{r\ge1}\frac{\mathcal R^{*r}}{r!}.}
\]

To prove it without an analytic limiting convention, first note that \(\mathcal R\) is supported in \([\log2,\infty)\). On \([0,T]\), only \(r\le T/\log2\) can contribute to the displayed exponential, and each convolution term has finitely many contributing point masses. Hence the expression is a well-defined locally finite measure.

For a fixed prime, use a formal variable \(X\). The formal power series \(f(X)=\sum_{k\ge1}X^k/k\) has derivative \(1/(1-X)\). If \(H(X)=\exp f(X)=\sum_{j\ge0}h_jX^j\), formal differentiation gives \((1-X)H'=H\), with \(h_0=1\). Its coefficient equation is \(h_1=h_0\), and, for \(j\ge1\), \((j+1)h_{j+1}-j h_j=h_j\). Thus \(h_{j+1}=h_j\), so every \(h_j=1\). Substituting \(X^k\mapsto\delta_{k\log p}\) respects multiplication as convolution on bounded time intervals. Therefore

\[
\exp_*\left(\sum_{k\ge1}\frac1k\delta_{k\log p}\right)=\mathcal D_p.
\]

For finitely many primes, the convolution binomial identity gives \(\exp_*(A+B)=\exp_*(A)*\exp_*(B)\): expand the \(r\)-fold convolution and count the \(\binom{r}{j}\) choices of the \(j\) factors from \(A\), whose coefficient becomes \(1/(j!(r-j)!)\). All sums relevant on a bounded interval are finite. Thus the convolution exponential of the finite-prime repetition measure is \(\mathcal D_F\).

On \([0,T]\), primes greater than \(e^T\) contribute no positive-time atom; their local counting factor contributes only \(\delta_0\). Taking \(F\) to contain the finitely many primes at most \(e^T\) makes both sides of the claimed boxed identity equal on that interval. Since \(T\) is arbitrary, the identity follows globally.

This proves the precise reconstruction: primitive prime labels, every repetition, the coefficients \(1/k\), and convolution produce all composite counts with exactly their required multiplicities. The unit atom cannot be omitted from the convolution exponential.

## TP11. The finite record and the whole record

Let \(F_N\) be the activated prime labels through tick \(N\). TP3 proves \(F_N=\{p:p\le N\}\). These sets increase, and their union is the set of all primes. For the corresponding measures retain

\[
\mathcal R_N=\sum_{p\le N}\sum_{k\ge1}\frac1k\delta_{k\log p},
\qquad
\mathcal W_N=\sum_{p\le N}\sum_{k\ge1}(\log p)\delta_{k\log p},
\qquad
\mathcal D_N=\underset{p\le N}{*}\mathcal D_p.
\]

For every \(T\ge0\), all three measures agree with their full counterparts on \([0,T]\) once \(N\ge e^T\). For \(\mathcal R\) and \(\mathcal W\), this follows from \(p^k\le e^T\Rightarrow p\le e^T\). For \(\mathcal D\), every \(n\le e^T\) has all prime divisors at most \(e^T\), so TP10 supplies precisely its mass. Thus the infinite measure is obtained as an exact compatible locally finite limit; each bounded time window is eventually determined exactly.

No finite \(N\) contains the whole record, by infinitude of primes. Conversely, the finite record already determines these exact restrictions. The reconstructed \(\mathcal D_N\) also contains counts larger than \(N\), such as arbitrarily high powers of two after tick two: this is the consequence of the retained multiplication rule, not a claim that those ticks have already occurred in the finite sequential history.

## TP12. The original zeta function is the transform of the full count measure

Let \(s\in\mathbb C\) with \(\sigma=\operatorname{Re}s>1\), and use real logarithms of positive integers. The original Riemann zeta function on this domain is

\[
\zeta(s)=\sum_{n\ge1}n^{-s}
=\int_{[0,\infty)}e^{-st}\,d\mathcal D(t)
=1+\sum_{n\ge2}e^{-s\log n}.
\]

The series is absolutely convergent: the positive decreasing function \(x^{-\sigma}\) gives \(\sum_{n\ge2}n^{-\sigma}\le\int_1^\infty x^{-\sigma}\,dx=1/(\sigma-1)\). On a half-plane \(\sigma\ge1+\delta\), with \(\delta>0\), the fixed summable majorant \(n^{-1-\delta}\) also gives uniform convergence.

For finite \(F_N\), the geometric series and TP10 yield

\[
Z_N(s):=\prod_{p\le N}(1-p^{-s})^{-1}
=\sum_{\substack{n\ge1\\p\mid n\Rightarrow p\le N}}n^{-s}
=\int e^{-st}\,d\mathcal D_N(t).
\]

Indeed, \(|p^{-s}|<1\); each local geometric series converges absolutely. The finite product of these absolutely convergent series may be expanded term by term, and uniqueness of factorization identifies each term exactly once. Every integer omitted from the finite product has a prime divisor exceeding \(N\), and therefore itself exceeds \(N\). Consequently, on \(\sigma\ge1+\delta\),

\[
|\zeta(s)-Z_N(s)|\le\sum_{n>N}n^{-1-\delta}\longrightarrow0.
\]

This proves the full Euler product on its stated original domain:

\[
\boxed{\zeta(s)=\prod_p(1-p^{-s})^{-1},\qquad\operatorname{Re}s>1.}
\]

The displayed finite products and their proof contain the prime-two factor \((1-2^{-s})^{-1}\), the exponent-zero term at every prime, and the global unit term one. No completion multiplier, Gamma factor, or boundary term is suppressed: none has been introduced in this calculation of the original Dirichlet series on its domain of absolute convergence.

## TP13. The repetition weights give the exact logarithm and logarithmic derivative

For \(\operatorname{Re}s>1\), define

\[
L(s)=\int e^{-st}\,d\mathcal R(t)
=\sum_p\sum_{k\ge1}\frac{p^{-ks}}k.
\]

Both this series and its once-differentiated series converge absolutely and locally uniformly. To check this explicitly on \(\sigma\ge1+\delta\),

\[
\sum_p\sum_{k\ge1}\frac{p^{-k\sigma}}k
\le\frac{1}{1-2^{-1-\delta}}\sum_{n\ge2}n^{-1-\delta}<\infty,
\]

and

\[
\sum_p\sum_{k\ge1}(\log p)p^{-k\sigma}
\le\frac{1}{1-2^{-1-\delta}}\sum_{n\ge2}(\log n)n^{-1-\delta}<\infty.
\]

The latter numerical series converges because, for sufficiently large \(x\), \(\log x\le x^{\delta/2}\): put \(y=\log x\) and use \(e^{(\delta/2)y}\ge((\delta/2)y)^2/2\), whose ratio to \(y\) tends to infinity. Its tail is therefore bounded by the convergent series \(\sum n^{-1-\delta/2}\). These bounds establish the stated uniform convergence and justify termwise differentiation on every compact subset of the half-plane.

For \(|z|<1\), the same coefficient calculation as TP10, now in absolutely convergent analytic series, gives

\[
\exp\left(\sum_{k\ge1}\frac{z^k}{k}\right)=(1-z)^{-1}.
\]

For a finite prime set this gives \(e^{L_N(s)}=Z_N(s)\). Passing to the locally uniform limits from TP12 and the preceding convergence yields

\[
\boxed{e^{L(s)}=\zeta(s),\qquad\operatorname{Re}s>1.}
\]

Thus \(L\) is the analytic logarithm of the original zeta function on this half-plane, selected by its convergent series and by \(L(x)\to0\) as real \(x\to+\infty\). That last limit follows by domination by the convergent series at \(x=2\), whose individual terms tend to zero. In particular \(\zeta\) has no zero on this half-plane, since an exponential is nonzero. Differentiating the exponential identity and retaining the full factor from each repeated return gives

\[
\begin{aligned}
-\frac{\zeta'(s)}{\zeta(s)}
&=-L'(s)\\
&=\sum_p\sum_{k\ge1}\frac{k\log p}{k}\,p^{-ks}\\
&=\sum_p\sum_{k\ge1}(\log p)p^{-ks}\\
&=\int e^{-st}\,d\mathcal W(t)\\
&=\sum_{n\ge2}\frac{\Lambda(n)}{n^s}.
\end{aligned}
\]

The second line displays where the repetition number \(k\) from differentiating the exponential and the original coefficient \(1/k\) enter. The subsequent equality computes their product; the original contributions remain visible. There is no coefficient one replacing \(\log p\), and the repeated return at \(p^k\) has coefficient \(\log p\), not \(k\log p\).

The original integer one contributes the atom \(\delta_0\) and the constant term one to \(\zeta\). Its derivative is zero, and the Dirichlet coefficient at one in \(-\zeta'/\zeta\) is \(\Lambda(1)=0\). The denominator of that quotient remains the full \(\zeta\), including its constant term; dropping the unit there would change the function. Integer one has not been identified with the supporting datum. Zero and negative logarithmic return times still exist in the full flow of TP7. The positive-time series here comes from the original expansion \((1-p^{-s})^{-1}=\sum_{k\ge0}p^{-ks}\) on \(\operatorname{Re}s>1\). Negative repetitions correspond to reciprocal powers outside this positive-integer Dirichlet series, while the zero exponent is its retained unit term. The logarithmic series has no constant term because the logarithm of that local unit constant is zero.

## TP14. What this contributes to the current weight calculation

The following maps and weights have now been proved, with no numerical scan or purity assumption:

\[
\begin{gathered}
\text{unit-anchored waits }(g_j)
\longleftrightarrow p_j=1+\sum_{r\le j}g_r
\longleftrightarrow \lambda_{p_j}=\log p_j,\\
\text{primitive curve }E_p
\longrightarrow \{k\log p:k\in\mathbb Z\},\\
\mathcal R=\sum_{p,k\ge1}\frac1k\delta_{k\log p},
\qquad
\mathcal D=\exp_*\mathcal R,
\qquad
\mathcal W=t\mathcal R,\\
\mathcal L\mathcal D=\zeta,
\qquad
\mathcal L\mathcal R=\log\zeta,
\qquad
\mathcal L\mathcal W=-\zeta'/\zeta
\quad(\operatorname{Re}s>1).
\end{gathered}
\]

Here \(\mathcal L\) is exactly the displayed Laplace integral, and \(\log\zeta\) is exactly the analytic branch constructed in TP13. The nonnegative coefficients of these measures are explicitly established. Positivity of these particular time measures is not silently substituted for a Weil quadratic-form inequality, and the displayed transform identities are not asserted outside the half-plane in which they were proved.

The numerical period \(\log p\) is now determined by the timed prime event, and its occurrence as the coefficient of every prime-power term in \(-\zeta'/\zeta\) is derived. That is the exact datum supplied to the separate arithmetic cohomology and weight calculation: the event-time record gives the source curve and all its repeated periods, rather than a common-radius assumption or an imposed distance from the supporting datum.
