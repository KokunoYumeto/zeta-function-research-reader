# Complete timing, the common quotient, and retrospective integer meaning

Independent mathematical derivation, 24 September 2026. Result labels GTQ0–GTQ12. Private working note; no publication is asserted.

## GTQ0. Source, order, and exact scope

The governing user passages are WU050–WU053 in `USER_INPUT_SOURCE_RECORDS.json`. I read `READ_FIRST_USER_CONSTRUCTION.md` and `USER_ARGUMENT_RECONSTRUCTION.md` before this calculation. The essential order is:

> “And after you've timed every single absorption line, can you find the quotient that is common to all of them? And that's when you know what one is.” — WU051.

> “you count by counting how many times the quotient has been, you know, either, like how many times the quotient has corresponded to either an absorption or not an absorption. That's how you get the integers.” — WU050.

This note does not start with observed events named one, two, or three. It studies the mathematical content of a complete, uncalibrated timing record and calculates its primitive common tick, the coordinate system it determines, and the obstruction to such a tick. It then proves an impossibility of recovering those final coordinates from an arbitrary finite prefix. That impossibility concerns the construction map itself, not merely an observer's ignorance of a number system already assigned to the source.

The timing receiver used below is explicitly an analysis object: an ordered real line of durations with no chosen positive unit, a set of events, and their durations from a marked start. This is not attributed to the user as a definition of the parityless source. No vector, distance, coordinate, addition, subtraction, or count is assigned to

\[
\tau\langle Z_1;\text{no }Z_2\rangle.
\]

In particular, the marked start of a time record is not identified with this supporting datum. Addition at tau remains retracted. A receiver with durations adds timed information; this note does not claim that the property of having no parity by itself constructs that information.

The metatheory can discuss finite lists, words, repetition, and integers when proving a representation theorem. These proof indices are not the number meanings purportedly recovered inside the source. Every time an arithmetic coordinate is assigned to an event below, the positive unit used for that coordinate is derived first. The duration itself remains in every comparison; it is not rescaled away.

### Reading ledger for this derivation

The existing `CANONICAL_SOURCE_ROUTING_PRIVATE.json` and `INTEGRALITY_SOURCE_READING_PRIVATE.json` were read first. They route the CC papers and record the existing author-source coverage. I then read `CANONICAL_GENERIC_RECONSTRUCTION.md`, CG0, and `TIMED_PRIME_PERIOD_DERIVATION.md`, TP0–TP2 and the opening of TP3. These are programme derivations, not original-author literature. Their complete cyclic source is explicitly an input in those notes. No new theorem from an unread paper is imported here. The timing and group assertions below have their proofs in this file. GTQ11 proves its displayed period comparison directly rather than appealing to the source-reading receipt as a proof.

## GTQ1. The uncalibrated record and its universal duration group

Let V be an oriented one-dimensional real vector space. Its orientation supplies a positive ray \(V_{>0}\); no vector in that ray is selected as a unit. Let E be the complete set of **absorption-event identities**, and

\[
t:E\longrightarrow V_{>0}
\]

their durations from a distinguished start of the record. Several absorption-event identities may have the same duration. Thus absorption multiplicities and channel labels are retained rather than replaced by their support. Throughout the note, “event” in E means an absorption, not a general recorded clock observation. A discrete, sequential record will additionally have finitely many absorption events below every positive duration and unbounded event times, but GTQ1–GTQ5 do not need those additional properties.

Any separately recorded non-absorption observations are retained as a different set N with a duration map u:N→\(V_{>0}\), their own labels, and u(N) disjoint from t(E). They are never inserted into E and declared absorptions merely because they were recorded. The primary common-quotient calculation below uses all absorption timings t(E), as WU051 requests. GTQ3 also gives the exact comparison with additional recorded non-absorptions.

Let F(E) be the free abelian group on symbols [e], e in E. Its elements are finite signed words modulo reordering and cancellation of opposite copies. Form the homomorphism

\[
T:F(E)\longrightarrow V,\qquad
T\!\left(\sum_{e\in E}n_e[e]\right)=\sum_{e\in E}n_e t(e),
\]

where only finitely many proof coefficients \(n_e\) are nonzero. Define

\[
K_t=\ker T,
\qquad
D_t=F(E)/K_t,
\qquad
G_t=T(F(E))\subset V.
\]

The exact comparison is

\[
\overline T:D_t\xrightarrow{\sim}G_t,
\qquad [a]\longmapsto T(a).
\tag{GTQ1.1}
\]

It is well defined because equal quotient classes differ by an element of \(K_t\). It is injective because T(a)=0 means a is in \(K_t\), and surjective by the definition of \(G_t\). No infinite sum of durations has been performed: the complete record supplies all generators and all actual relations among finite signed combinations.

This is also a universal construction with its precise domain. Given an abelian group H and an assignment u:E→H for which every timing relation in \(K_t\) is respected, the homomorphism F(E)→H supplied by finite signed addition kills \(K_t\) and factors uniquely through \(D_t\). Conversely, a homomorphism \(D_t\)→H necessarily respects those relations. Uniqueness follows because the event classes generate \(D_t\).

Thus the complete timed record determines a group, not yet a primitive unit. Retaining \(K_t\) records which concatenated durations are actually equal. A list of event names or their order alone does not supply these duration relations.

## GTQ2. Calculate all common ticks and the primitive one

A positive duration d is called an admissible common tick for this receiver when every event time is a finite positive repetition of d:

\[
\mathcal C_t=
\left\{d\in V_{>0}: t(e)\in d\mathbb Z_{>0}\text{ for every }e\in E\right\}.
\tag{GTQ2.1}
\]

Here \(d\mathbb Z\) means the subgroup of V generated by the duration d. This definition tests a candidate duration; it does not designate any event as the integer one. Throughout this section E is nonempty.

**Classification.** The following statements are equivalent:

1. At least one admissible common tick exists.
2. \(G_t\) is a nonzero discrete subgroup of V.
3. \(G_t\) has a least positive element δ.
4. \(G_t\) is generated by a unique positive element δ.

When they hold, the entire set of admissible ticks is

\[
\boxed{\mathcal C_t=\{\delta/k:k\in\mathbb Z_{>0}\}.}
\tag{GTQ2.2}
\]

Consequently the primitive, greatest admissible tick is unique and equals δ. Merely requiring a common divisor of the timings does not make it unique: the proper refinements δ/k are also common divisors.

**Proof.** Suppose d is admissible. Then every event belongs to \(d\mathbb Z\), so \(G_t⊂d\mathbb Z\). Under the injective map n↦nd, a nonzero subgroup of this cyclic group corresponds to a nonzero subgroup A of the metatheoretic integers. Choose its least positive integer k. For n in A, write n=qk+r with 0≤r<k by integer division. Then r is in A; minimality forces r=0. Therefore \(A=k\mathbb Z\) and \(G_t=(kd)\mathbb Z\). This has least positive element kd and is discrete.

Conversely, suppose \(G_t\) is nonzero and discrete. Choose temporarily any positive vector v to express the order topology. This temporary coordinate does not calibrate the final tick. Discreteness at the zero duration gives a positive lower bound on positive members of \(G_t\). Let a>0 be the infimum of their real coordinates. Choose a positive member g with coordinate in [a,3a/2). Any other positive member h with coordinate in [a,3a/2) must equal g: otherwise |g−h| is a positive member of \(G_t\) with coordinate less than a. If g had coordinate greater than a, the definition of the infimum would supply such an h with smaller coordinate. Thus g has coordinate a and is least positive. Call its coordinate-independent duration δ.

For arbitrary g in \(G_t\), choose the unique integer q for which 0≤g−qδ<δ. The remainder is in \(G_t\). Minimality of δ makes it zero. Hence \(G_t=δ\mathbb Z\). Because all event times are positive members, δ is admissible. A positive generator must be the least positive element, so it is unique.

Finally, if d is admissible, \(G_t⊂d\mathbb Z\), so δ=kd for a positive integer k. Thus d=δ/k. Conversely every δ/k divides every t(e)=n_eδ, because t(e)=(\(kn_e\))(δ/k). This proves the full formula. ∎

The empty record is genuinely different. Its generated group is zero, every positive d vacuously divides all its event times, and there is no greatest common tick. The theorem does not manufacture a unit from absence.

## GTQ3. Exact retrospective counts, including non-absorption

In the cyclic case, first obtain δ by GTQ2. Only then define

\[
\nu_\delta:G_t\xrightarrow{\sim}\mathbb Z,
\qquad
\nu_\delta(g)=\text{the unique }n\text{ for which }g=n\delta.
\tag{GTQ3.1}
\]

Existence and uniqueness are GTQ2. Its inverse is n↦nδ. It preserves addition because

\[
n\delta+m\delta=(n+m)\delta,
\]

and preserves the order because δ is positive. The event-count assignment is the composite

\[
E\xrightarrow{t}G_t\xrightarrow{\nu_\delta}\mathbb Z_{>0}.
\tag{GTQ3.2}
\]

This assigns integer meaning after the group and its generator have been obtained from the whole record. It uses no pair of events carrying preassigned prime names.

Retain each event fibre

\[
E_n=\{e\in E:t(e)=n\delta\},
\qquad n\in\mathbb Z_{\ge0}.
\tag{GTQ3.3}
\]

The complete clock has every position nδ; absorption occurs at exactly the positions with \(E_n\) nonempty, because E is the complete absorption-event set. Set b(n)=1 for a nonempty fibre and b(n)=0 for an empty fibre. The positions with b(n)=0 are not deleted. If the record carries multiplicities or channel labels, these remain in \(E_n\) and must not be replaced by b(n) alone.

For separately recorded non-absorptions, retain \(N_n\)={a in N:u(a)=nδ}, with the original labels. Every nonempty \(N_n\) lies at a position with b(n)=0, by disjointness of u(N) and t(E). Observations u(a) outside \(δ\mathbb Z\) are also retained; they certify that the primitive quotient of absorption timings alone is not a clock tick for all those additional observations. In that situation the exact group for the joint timing record is \(\widetilde G=\langle t(E),u(N)\rangle_{\mathbb Z}\). Applying GTQ2 to this explicitly enlarged set calculates its common tick or proves that it has none. One still uses E alone to define absorption fibres, and N to record non-absorption fibres. No observed non-absorption datum is discarded or silently reclassified.

For any derived count N≥0, the number of positive clock positions through Nδ is N. Its decomposition is

\[
N=\sum_{n=1}^{N}b(n)+\sum_{n=1}^{N}(1-b(n)).
\tag{GTQ3.4}
\]

Each term corresponds to one clock position, with exactly one of absorption and non-absorption. This proves the latest WU050 distinction within this receiver: counting only newly appearing absorption fibres would retain the first sum and lose the second. The order number of an absorption event is not generally its elapsed tick count.

The inverse reconstruction retains the scale and the event identities. From (δ,{\(E_n\)}) reconstruct E as the disjoint union of the \(E_n\) and map (n,e) to nδ. The map from the original E to this disjoint union sends e to (ν_δ(t(e)),e). Its inverse forgets the first coordinate, whose value is already fixed by t(e). Thus no event, repetition at the same time, or duration factor is lost.

When N is supplied, the output additionally retains its fibres \(N_n\) and the off-grid part \(N_*\)={a in N:u(a) not in \(δ\mathbb Z\)}, with the complete map \(u|_{N_*}\) and labels unchanged. Reconstruct N as the disjoint union of the \(N_n\) and \(N_*\), assigning nδ to a member of \(N_n\) and its retained duration u(a) to a member of \(N_*\). The same fibre-membership maps are inverse. Thus the timing comparison also preserves every supplied non-absorption observation, including any one that invalidates the proposed absorption-grid clock.

This creates the lattice of possible clock positions. It does not prove that an unspecified geometric half-turn physically occurs at each such position. That further assertion is a statement about the source dynamics, not an extra conclusion smuggled into GTQ3.1.

## GTQ4. The recovered arithmetic and its one

Retain the whole group \(G_t=δ\mathbb Z\). Form

\[
R_t=\operatorname{End}_{\rm Ab}(G_t),
\]

with pointwise addition and multiplication by composition. Addition and composition are associative; addition is commutative because \(G_t\) is abelian. For homomorphisms f,g,h and x in \(G_t\),

\[
f((g+h)(x))=f(g(x))+f(h(x)),
\qquad
((f+g)\circ h)(x)=f(h(x))+g(h(x)).
\]

These prove both distributive laws. The zero map is the additive identity, −f the additive inverse, and \(id_{G_t}\) the multiplicative identity. These are operations on endomorphisms of the duration group, not on tau.

Every endomorphism is determined by its value at δ. For a unique integer n, f(δ)=nδ, and then f(mδ)=mnδ for every integer m. Conversely this formula defines an endomorphism for every n. Thus

\[
\mathbb Z\xrightarrow{\sim}R_t,\qquad
n\longmapsto[n],\quad[n](g)=ng
\tag{GTQ4.1}
\]

is a ring isomorphism. Its coordinate check gives [n]+[m]=[n+m], [n]∘[m]=[nm], and [1]=\(id_{G_t}\). Replacing δ by −δ leaves the integer n attached to an endomorphism unchanged. The identity endomorphism is therefore independent even of the chosen orientation, although the positive duration δ uses the direction of the timing record.

Evaluation at δ is an additive isomorphism

\[
\operatorname{ev}_\delta:R_t\xrightarrow{\sim}G_t,\qquad f\longmapsto f(\delta),
\tag{GTQ4.2}
\]

and sends the recovered arithmetic one to the recovered tick δ. It transfers multiplication to \(G_t\) by

\[
(n\delta)\mathbin{\odot_\delta}(m\delta)=(nm)\delta.
\tag{GTQ4.3}
\]

The duration δ is retained; it is not identified with tau or silently erased by a scale change.

Let \(R_{t,+}\) be the endomorphisms taking nonnegative durations to nonnegative durations. By GTQ4.1 these are precisely [n] with n≥0. Define a|b in its nonzero part when b=a∘c for a nonnegative endomorphism c. The identity divides every member. If a divides every nonzero member, it divides the identity: a∘c=id. Writing a=[n] and c=[m] gives nm=1 with n,m positive, so n=m=1. Hence \(id_{G_t}\) is the unique positive universal divisor of this recovered arithmetic.

There are therefore two proved comparisons, not an ambiguous use of one word:

* The primitive common timing divisor is δ, the greatest member of the set GTQ2.2.
* The universal divisor of the positive endomorphism arithmetic is \(id_{G_t}\), whose evaluation at δ is δ.

The first is a statement about durations. The second is a statement about composition of operations. Equation GTQ4.2 relates them exactly.

## GTQ5. What the whole determines that a prefix cannot determine

Let F be a nonempty finite set of observed events, and let B be a duration through which the record has been completely observed. Suppose the prefix's duration group is

\[
G_F=\delta_F\mathbb Z,
\qquad \delta_F>0.
\]

The existence of this prefix tick is checked on the prefix itself by GTQ2. It is not named the final unit. Choose an integer M large enough that \(Mδ_F\)>B. For any proof integer k>1 define two full continuations, retaining the same old events and their identities:

\[
S^{(0)}=t(F)\ \cup\ \{(M+j)\delta_F:j\in\mathbb Z_{\ge0}\},
\tag{GTQ5.1}
\]

\[
S^{(k)}=t(F)\ \cup\ \{(M+j+1/k)\delta_F:j\in\mathbb Z_{\ge0}\}.
\tag{GTQ5.2}
\]

If an existing event has multiplicity or labels, retain them; the newly added times can be assigned new event identities. Each continuation is unbounded and locally finite, and the observations through B coincide exactly.

The group of \(S^{(0)}\) is \(δ_F\mathbb Z\): the old events already generate that group and every new event belongs to it. The group of \(S^{(k)}\) is \((δ_F/k)\mathbb Z\). Indeed, it contains \(δ_F\) because the old events generate it, and it contains

\[
(M+1/k)\delta_F-M\delta_F=\delta_F/k.
\]

Every old and new event is an integer multiple of δ_F/k, proving the reverse inclusion. By GTQ2 the final primitive ticks are respectively \(δ_F\) and δ_F/k.

For every old event e whose prefix coordinate is t(e)=n_eδ_F, the two final retrospective counts are respectively

\[
\nu^{(0)}(t(e))=n_e,
\qquad
\nu^{(k)}(t(e))=kn_e.
\tag{GTQ5.3}
\]

They differ, and the finer reconstruction has additional non-absorption clock positions before B. Thus identical finite observed timings can correspond to different final numerical meanings in the two whole constructions.

**Construction-level conclusion.** On the class of unbounded, locally finite timed event records having a primitive tick, no rule depending only on an arbitrary finite observed prefix can always return the final primitive tick or even the final count of every old event. If it did, apply it to the two identical prefixes just constructed. Its output would be identical, whereas GTQ5.3 makes the correct outputs different. Contradiction.

Equivalently, the whole-record reconstruction in GTQ3 does not factor through the prefix restriction map on this class. This is a precise global dependency of the construction. The proof is not founded on assigning prime values to the first two events, and it is not merely a claim that a person happens not to know those values.

The class used here is stated in full. No conclusion is drawn that these arbitrary continuations are permitted by the actual CC source relations, or by an additional arithmetic return law. The calculation establishes exactly what timing plus order alone can and cannot force.

## GTQ6. A finite algebraic witness and a global certification are different facts

Now take a complete record for which \(G_t=δ\mathbb Z\). By definition \(G_t\) is generated by finite signed combinations of events. Since δ belongs to \(G_t\), there are finitely many events \(e_1\),…,\(e_r\) and signed proof integers \(a_1\),…,\(a_r\) such that

\[
\delta=\sum_{i=1}^{r}a_i t(e_i).
\tag{GTQ6.1}
\]

Let \(F_0\) be this finite set. Because \(F_0\)⊂E, its group lies in \(δ\mathbb Z\). Because GTQ6.1 puts δ in its group, that group is all \(δ\mathbb Z\). Thus the final primitive tick has a finite algebraic witness inside the full record.

For a sequential, locally finite record with an initial interval containing \(F_0\), that interval's primitive tick equals δ. Every later prefix of the actual complete record has the same primitive tick: it contains \(F_0\) and lies in \(δ\mathbb Z\).

This does not contradict GTQ5. The finite expression GTQ6.1 proves that δ is generated by those events. It does not prove that every event outside \(F_0\) is an integer multiple of δ. The latter is the universal assertion about the complete record used to certify the same primitive tick globally.

Accordingly, the universal statement “the unit can have no finite algebraic witness” is false for the cyclic duration reconstruction; GTQ6.1 explicitly constructs such a witness. The stronger whole-first requirement in the user's account can instead be represented by the failure of finite-prefix factorization in GTQ5. It cannot be proved by confusing these two assertions. No claim is made that the user's source has already been fully formalized by this receiver.

## GTQ7. Completeness alone does not force a primitive tick

Here is the exact calculation for a complete sequential record whose timings remain commensurable but admit no common positive tick. It is a receiving-space example, not a counterexample asserted to satisfy the user's still-to-be-derived geometric source.

Choose a positive duration v solely to describe this example. Include an event at v, followed by the events

\[
t_n=(n+3^{-n})v,\qquad n\in\mathbb Z_{>0}.
\tag{GTQ7.1}
\]

The labels n are metatheoretic positions in an example list, not prelabelled prime observations. The event times increase strictly because

\[
t_{n+1}-t_n=(1-2\cdot3^{-n-1})v>0.
\]

They are unbounded since \(t_n\)≥nv and locally finite for the same reason. Their entire list is specified, with no unknown future event. Every pair of durations has rational ratio.

The generated group contains v because that event is present. It then contains \(t_n\)−nv=3^{-n}v for every n. Conversely each event is a rational multiple of v whose denominator is a power of three. Therefore the exact generated group is

\[
\boxed{G_t=\mathbb Z[1/3]v.}
\tag{GTQ7.2}
\]

It has positive elements 3^{-n}v tending to the zero duration, so it is not discrete and has no least positive element. By GTQ2, its common-tick set is empty. Hence knowing the complete history and knowing all pairs of event durations to be commensurable do not by themselves force a primitive common tick. The odd-denominator refinement is chosen to allow comparison with the root's separate signed-support calculation; that support calculation is not assumed or duplicated here.

The full obstruction is not discarded. GTQ8 gives the group that records each refinement and identifies exactly when they terminate in a single primitive unit.

## GTQ8. The quotient recording every late refinement

Fix any nonempty observed prefix F with cyclic group \(δ_F\mathbb Z\) and retain the whole event group \(G_t\). Because \(δ_F\) belongs to \(G_t\), form the exact sequence

\[
0\longrightarrow\delta_F\mathbb Z
\longrightarrow G_t
\longrightarrow\mathcal D_F:=G_t/(\delta_F\mathbb Z)
\longrightarrow0.
\tag{GTQ8.1}
\]

This quotient records how complete timing differs from the prefix's grid. An event e remains on that grid exactly when its class \(t(e)+δ_F\mathbb Z\) is zero. Thus the entire history remains on it exactly when \(\mathcal D_F=0\), because event classes generate the quotient.

For any duration g in \(G_t\), its class in \(\mathcal D_F\) has finite order precisely when some positive repetition kg lies in \(δ_F\mathbb Z\). In a temporary coordinate this is equivalent to g/δ_F being rational. This equivalence follows directly from kg=\(mδ_F\) in one direction and clearing the denominator of a rational ratio in the other.

The following classification is exact:

* \(\mathcal D_F\) finite of cardinality k means \(G_t=(δ_F/k)\mathbb Z\). Its final tick is δ_F/k, and \(\mathcal D_F\) is cyclic of order k.
* \(\mathcal D_F\) infinite torsion means every event duration is rationally commensurable with \(δ_F\) but their denominators have no common bound. There is no common tick.
* \(\mathcal D_F\) containing an element of infinite order means at least one duration is incommensurable with \(δ_F\). There is no common tick.

**Proof of the finite case.** The quotient of a cyclic timing group \(δ\mathbb Z\) containing \(δ_F\mathbb Z\) has \(δ_F\)=kδ for a positive integer k, so it is cyclic with k classes, and the assertion follows in this direction. Conversely suppose \(\mathcal D_F\) has k elements. Addition by any class permutes this finite set; alternatively partition into the cosets of its cyclic subgroup. The order of every class divides k. Hence kg belongs to \(δ_F\mathbb Z\) for all g in \(G_t\), giving \(G_t⊂(δ_F/k)\mathbb Z\). By the subgroup argument of GTQ2, \(G_t\) is cyclic, say \(δ\mathbb Z\). The first direction now shows that its quotient has δ_F/δ classes; equality with k gives δ=δ_F/k.

**Proof of the infinite cases.** If a common tick existed, GTQ2 would make \(G_t\) cyclic, and the finite-case calculation would make \(\mathcal D_F\) finite. Thus either infinite case rules out such a tick. The statement about rational commensurability follows from the preceding order calculation. In the torsion case, a common denominator M, meaning that every reduced denominator divides M, would give \(G_t⊂(δ_F/M)\mathbb Z\) and a finite quotient. A numerical bound M on reduced denominators also supplies a common denominator, namely M!. Conversely a finite quotient supplies the common denominator k. Thus infinite torsion is exactly unbounded refinement among commensurable durations. ∎

For the pair of complete continuations in GTQ5, the quotients are respectively zero and a cyclic group of order k. For the record in GTQ7, quotienting its full group by \(v\mathbb Z\) gives \(\mathbb Z[1/3]/\mathbb Z\). Every class is killed by some power of three; classes of arbitrarily high power-of-three order occur. This explicitly records why there is no final positive tick, without replacing the defect by a slogan.

For completeness, a nonzero additive subgroup of V with no least positive element is dense. Indeed, if its positive infimum were positive, the argument in GTQ2 would attain the infimum and produce a least element. Therefore it has a positive member h shorter than any specified positive interval length. For a real interval (a,b), choose h<b−a and an integer k with a<kh≤a+h; then kh lies in (a,b). This proves density. The infinite cases of GTQ8 are thus genuinely nondiscrete timing groups, not merely missing a chosen name for an otherwise present smallest unit.

### GTQ8.2. The whole group is the exact directed limit of finite records

Order the finite subsets F of E by inclusion. Their timing groups have the actual inclusion maps \(G_F\)→\(G_{F'}\) whenever F⊂F'. Then

\[
G_t=\bigcup_{F\subset E,\ F\text{ finite}}G_F
\cong\varinjlim_FG_F.
\tag{GTQ8.2}
\]

The union equality follows because each element of \(G_t\) is a finite signed combination of event durations. For the universal property, a compatible family of group maps \(f_F\):\(G_F\)→H defines f(g)=\(f_F\)(g) for any F with g in \(G_F\). Two such choices lie in the common larger finite set F∪F', so compatibility makes this independent of the choice. The same common-finite-set argument proves additivity and uniqueness.

When \(G_F=δ_F\mathbb Z\) and \(G_{F'}=δ_{F'}\mathbb Z\) are nonzero cyclic, their inclusion has an exact positive index k with

\[
\delta_F=k\delta_{F'},\qquad
\nu_{\delta_{F'}}(g)=k\nu_{\delta_F}(g)\quad(g\in G_F).
\tag{GTQ8.3}
\]

The first equation holds because \(δ_F\) is a positive member of \(G_{F'}\). Substituting g=\(nδ_F\) proves the second. This is the exact transition map for old numerical labels under a later refinement; they need not be held fixed while the primitive tick changes. If the complete group is cyclic, GTQ6 supplies a finite record after which these indices are all one in the actual directed system. If it is not cyclic, no finite cyclic stage equals the whole group. The full group in GTQ8.2 is a mathematical object retaining all events and relations; no assertion that an infinitely long physical procedure has ended is used to construct the limit.

## GTQ9. A timing start is distinct from the supporting point

If the data give event positions in an oriented affine time line A rather than durations from a marked start, the coordinate-free timing data are differences t(e)−t(f) in its translation line V. Define

\[
G_{\rm diff}=\langle t(e)-t(f):e,f\in E\rangle_{\mathbb Z}.
\]

The preceding common-tick classification applies to this group. In its nonzero cyclic case it supplies a unique positive δ. The difference group by itself does not select which point of the affine record is to be numbered zero.

The event positions lie in the affine lattice

\[
\mathcal A=t(e_0)+G_{\rm diff}
\]

for any event \(e_0\), and changing \(e_0\) does not change that set. The group acts freely and transitively by translations on \(\mathcal A\). Choosing \(e_0\) assigns the coordinate c(e) by t(e)−t(\(e_0\))=c(e)δ. If another event \(e_1\) has coordinate r, the coordinates based at \(e_1\) are c(e)−r. Thus the lattice of possible positions is a torsor for the integer group.

The full event record may distinguish a point even when no separate initial marker was supplied. For example, a unique earliest event in an oriented record selects an event-based zero. General affine event records need not do this: for the whole affine lattice with identical event labels at every lattice point, translation by δ preserves the full data and fixes no point. An isomorphism-invariant selection of one point is therefore impossible for that example. Even when an earliest event selects an origin, it does not establish that the event was the user's initial no-turn state, or identify it with tau.

This is precisely why a parityless supporting point must not silently be used as a numerical start or a zero duration. A marked initial record position and the support of the construction are different input roles. No metric between them is used or derived here.

## GTQ10. Functoriality and preserved scale

An isomorphism of marked timing records consists of an event bijection φ:E→E' preserving any specified event labels and an orientation-preserving real-linear isomorphism A:V→V' such that t'∘φ=A∘t. It induces a group isomorphism \(G_t\)→\(G_{t'}\) by restriction of A. The group generators and all timing relations are carried to the corresponding generators and relations, so GTQ1.1 commutes with this map.

When the groups are cyclic, A sends their least positive elements to each other: if 0<g'<Aδ, its inverse would be a positive member of \(G_t\) less than δ. Consequently

\[
A(\delta)=\delta',
\qquad
\nu_{\delta'}(A(g))=\nu_\delta(g).
\tag{GTQ10.1}
\]

For endomorphisms the exact map is

\[
R_t\longrightarrow R_{t'},\qquad
f\longmapsto A\circ f\circ A^{-1}.
\tag{GTQ10.2}
\]

It preserves addition, composition, and the identity by evaluation; its inverse is conjugation by \(A^{-1}\). Evaluation at the actual durations δ and δ' commutes with these maps. The absorption fibres satisfy φ(\(E_n\))=E'_n for every derived count n, retaining every multiplicity and label.

Thus the arithmetic counts are invariant under a change of external time units, while the unit duration transforms as δ↦Aδ. This is a faithful comparison retaining the duration scale, not permission to replace the original duration by the scalar one everywhere.

## GTQ11. Counting-time quotients and logarithmic return periods

The programme's existing TP note also uses return-flow periods log(p) on the curves \(\mathbb C^×/p^{\mathbb Z}\). Those periods must not silently be identified with the tick δ of GTQ2. The following comparison is made only after the arithmetic in GTQ4 has been recovered. Prime symbols in this section therefore belong to the resulting arithmetic; none is a starting event label.

Write a=[n] for a positive endomorphism. For n≥1, define

\[
L(a)=\log n.
\]

Using a temporary generator only to compute the intrinsic integer n gives the same value after reversing that generator, by GTQ4.1. Then

\[
L(a\circ b)=L(a)+L(b),
\qquad L(\mathbf1_{R_t})=0.
\tag{GTQ11.1}
\]

It is the multiplication of recovered positive arithmetic that becomes addition of logarithmic flow time. The map from positive count durations is

\[
n\delta\longmapsto\log n,
\tag{GTQ11.2}
\]

which sends \(\odot_δ\) to addition. It does not send ordinary addition of count durations to addition: the required identity would be log(n+m)=log n+log m for all positive n,m, which fails already when n=m=1 because log(1+1)>0 and log 1+log 1=0. Here those integer values have been constructed before the test is made.

For a recovered prime p, the flow [z]↦[e^u z] on \(\mathbb C^×/p^{\mathbb Z}\) returns to [z] exactly when e^u z=p^jz for an integer j. Since z is nonzero and u is real, this is equivalent to u=j log p. Thus the period group is \((log p)\mathbb Z\) and all return repetitions are retained.

The additive subgroup generated by the complete prime return periods is

\[
\Gamma_{\rm ret}=\bigoplus_{p\ \mathrm{prime}}\mathbb Z\log p\subset\mathbb R.
\tag{GTQ11.3}
\]

Here is a complete proof of the independence assertion used in this formula. Positive integer division supplies the Euclidean algorithm: successive nonnegative remainders strictly decrease until zero, and back substitution expresses the greatest common divisor as an integral combination. If p is irreducible and p does not divide a, their greatest common divisor is one; write up+va=1. If p divides ab, multiplying the last equation by b proves p divides b. Hence irreducibles satisfy the prime divisor property. Every integer greater than one has an irreducible divisor: take its least divisor greater than one, whose factorization into two proper factors would contradict minimality. Repeated division terminates because positive quotients strictly decrease. For two factorizations, the prime divisor property matches and cancels a factor, and induction gives uniqueness of the multiset. Finally, a finite relation ∑_p \(a_p\) log p=0 exponentiates to equality between the products with positive and negative exponents on opposite sides. Uniqueness of factorization forces every \(a_p\)=0. This proves GTQ11.3.

There are at least two different primes: irreducible divisors exist by the preceding argument, and a divisor of p+1 cannot equal p because p cannot divide the difference (p+1)−p=1. If log p and log q for distinct primes were integer multiples of one common positive flow tick, their ratio would be rational, so p^a=q^b for positive integers a,b after exponentiating. Unique factorization forbids this. Therefore Γ_ret is not cyclic and, by GTQ2 and the density argument in GTQ8, has no common positive additive flow tick and is dense in the real flow line.

This does not refute the user's counting-time proposal. It proves the exact place where its potential common quotient and the CC logarithmic flow differ. The complete diagrams must retain both the count operation and the logarithmic receiving map. A common arithmetic divisor of the recovered integer norms does not become a common additive divisor of their logarithms.

## GTQ12. What has been derived for the actual argument

The complete timed record produces \(D_t\) and \(G_t\) with all finite duration relations retained. Its primitive global tick, when present, is the least positive element of \(G_t\) and is unique. Every event and every non-absorption clock position then receives its arithmetic count by GTQ3, and the unit and multiplication are recovered as operations on the whole cyclic group by GTQ4. No prime values are imported to establish that unit.

GTQ5 proves a construction-level necessity of the whole: on the stated class, the resulting counts do not factor through an arbitrary finite prefix. The finite prefix may acquire different retrospective labels under different full extensions. GTQ6 simultaneously proves that a globally valid unit has a finite algebraic witness. Those results give different answers to different questions and must both be retained.

GTQ7–GTQ8 calculate the missing-tick object exactly: the generated group can remain nondiscrete even with a complete locally finite history, and the quotient \(\mathcal D_F\) records finite, indefinitely refining, or incommensurable departures from a provisional grid. Thus the words “complete history” alone do not prove that a primitive common quotient exists. The user's actual source may impose more structure; this note does not invent that structure or treat a receiving-space example as an analysis of the entire \(Z_1\) construction.

The existing CG0/TP0 source is stronger than an uncalibrated event list: it supplies an entire signed group with a cyclic quotient. Its proved cyclicity can license the arithmetic reconstruction, but calling that input “the stalk” does not derive its origin from the user's timing process. Conversely, a successful comparison from the complete source to the group \(G_t\) above must preserve its full event relations and demonstrate cyclicity in this receiver, rather than assigning known prime labels in advance.

The equality of common timing divisibility, a universal arithmetic unit, and the supporting point's uniqueness has not been assumed. GTQ4 proves the precise relationship between the first two. GTQ9 prevents a hidden identification of the timing start with the support. GTQ11 prevents identifying the count tick with the logarithmic return-flow periods. These are explicit receiving maps and exact obstructions, supplied for the whole construction's next derivation.

No purity or RH assertion is made in this timing note. This is a completed calculation of the common-quotient mechanism and its reconstruction map, with its entire scope stated, rather than a requested final conclusion inserted as a hypothesis.

### Independent check

An independent mathematical reader checked GTQ1–GTQ10. Two scope corrections were applied: an earliest event can canonically select a record origin, although it does not identify the support or initial no-turn state; and a bound on reduced denominators gives a common denominator such as their factorial, rather than automatically the bound itself. The directed-limit calculation GTQ8.2 was added after that review and is proved in full above.
