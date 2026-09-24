---
title: "Fixed support, winding arithmetic, and global clock completion"
date: "24 September 2026"
geometry: "margin=24mm"
fontsize: "11pt"
colorlinks: true
---

Private cumulative source. The four complete derivations below are retained in their order of dependence. Source statements, derived comparisons, and unproved identifications remain distinguished in each note. The pivot has no assigned arithmetic, metric, or coordinate.



# The fixed generic point and the parity exchanged by the mirror

24 September 2026. Reading and derivation from the original author TeX of Alain Connes and Caterina Consani, *The Absolute Twistor Line and the Geometry of the compactification of Spec Z*, arXiv:2609.00299v1. This note uses the paper's actual topological space and sheaf action. It does not replace the user's tau by a midpoint, vector, complex coordinate or numerical distance. It does not assume a torsion construction or a purity conclusion.

## CC1. The source space and why its generic point is fixed

The source's Section 3, original CC.tex lines 499–541, specifies

\[
X=\{+, -,\eta\},\qquad
\mathcal T=\{\varnothing,\{\eta\},\{+,\eta\},\{-,\eta\},X\}.
\]

The two affine opens correspond to the two orderings of the integer group. Their intersection is the generic open and corresponds to the group without a selected ordering. The paper's Section 4 exchanges the closed points by its geometric automorphism alpha.

Here is a derivation of fixedness from this source topology, rather than an extra axiom attached to a candidate pivot. The closed subsets are the complements of the displayed opens:

\[
\varnothing,\quad\{+\},\quad\{-\},\quad\{+,-\},\quad X.
\]

The only closed set containing eta is X. Thus the closure of {eta} is X. The singleton {+} is closed, and so is {-}; neither is dense. Therefore eta is the unique point whose singleton is dense. A homeomorphism sends the closure of a set to the closure of its image: continuity gives inclusion in one direction, and continuity of the inverse gives the reverse inclusion. Hence every homeomorphism of X fixes eta. In particular the source automorphism alpha does. Since alpha exchanges + and -, they are not fixed. Consequently

\[
\operatorname{Fix}_X(\alpha)=\{\eta\},\qquad
\alpha(+)= -,\qquad\alpha(-)= +.
\]

This proves uniqueness and fixedness using the actual source, without affine coordinates. It agrees with the displayed formula in Definition def:alpha_symmetry, CC.tex lines 773–798.

## CC2. The exact parity statement follows, rather than being added

Keep the user's Z2 notation for the two orientation labels exchanged by the mirror. In this calculation their target is the two-element set

\[
Q_2=\{\mathrm{even},\mathrm{odd}\},\qquad
r(\mathrm{even})=\mathrm{odd},\quad
r(\mathrm{odd})=\mathrm{even}.
\]

The use of the names even and odd labels this two-state orientation observation. It does not identify the source chart inversion with addition of one to every integer, nor erase the full integer coefficients.

An assignment of these labels that respects the mirror has to satisfy

\[
p(\alpha x)=r(p(x))
\]

where the assignment is defined. This equation states that the label changes when the two mirror states are exchanged; it is not a numerical operation involving the user's tau.

On the exchanged pair {+,-}, there are exactly two such assignments: choose either label at +, and the equation forces the other label at -. Both satisfy the equation at both points.

Neither extends to eta. Indeed CC1 has proved alpha(eta)=eta. Extension would require

\[
p(\eta)=p(\alpha\eta)=r(p(\eta)).
\]

But neither of the two values of Q2 is fixed by r. This is a contradiction. Thus the point's lack of a mirror-exchanged Z2 label is a consequence of the topology and symmetry already in the paper. It has not been inserted as a new axiom.

This is specifically the orientation label exchanged by this mirror. A fixed point can still support nontrivial symmetry data; CC3 computes that data. An invariant label on a representation is a different observation from the free two-state label just specified.

## CC3. The point is fixed while its retained data transform

The full generic stalk in the enriched source is

\[
\mathcal O(\{\eta\})
=\mathbf F_{1^2}[T^{\mathbb Z},J]/(J^2=\epsilon),
\qquad \epsilon^2=1.
\]

The imaginary generator and the sign are retained. The source involution satisfies

\[
\alpha^*(T)=\epsilon T^{-1},\qquad
\alpha^*(J)=\epsilon J,\qquad
\alpha^*(\epsilon)=\epsilon.
\]

These are the source's equations, not operations assigned to the user's tau.

At the underlying pointed-monoid level, every nonabsorbing element has a unique multiplicative expression

\[
\epsilon^a T^m J^b,
\quad a,b\in\{0,1\},\quad m\in\mathbb Z.
\]

For completeness, uniqueness follows by using J^2=epsilon to identify the nonabsorbing group with Z times Z/4Z: the expression is sent to (m,2a+b mod 4). The inverse sends (m,k) to T^m J^k. Every k mod 4 has a unique form 2a+b with a,b in {0,1}. This is an exact description of the source multiplicative relations, retaining the full integer m, sign and imaginary branch; it is not a quotient discarding them. The absorbing zero is a separate monoid element.

Multiplicativity gives the complete action

\[
\alpha^*(\epsilon^a T^m J^b)
=\epsilon^a(\epsilon T^{-1})^m(\epsilon J)^b
=\epsilon^{a+m+b}T^{-m}J^b.
\]

Negative m are allowed because T and epsilon are units. Applying the same formula a second time gives epsilon exponent a+m+b-m+b=a+2b, integer exponent m, and branch exponent b. Since epsilon^2=1, the original element is recovered. No sign or exponent is suppressed from this check.

An element fixed by alpha must have m=-m, hence m=0. With m=0, equality of the sign coordinate requires b=0. The fixed nonabsorbing monoid elements are therefore exactly 1 and epsilon; together with the absorbing element they form {0,1,epsilon}. This computation is at the stated multiplicative level, before any additional additive realization.

In particular alpha acts nontrivially on the retained stalk even though eta is fixed as a point. For example J and epsilon J are distinct in this source and are exchanged. The quotient therefore retains isotropy: the two group elements identity and alpha both stabilize eta. The paper records this at CC.tex lines 891–899. Lack of a freely exchanged point-label must not erase that isotropy or the stalk action.

The spatial exponent changes m to -m. Consequently m modulo 2 is unchanged under this particular exponent inversion. This exact formula retains the distinction between the exchanged chart-orientation label in CC2 and ordinary integer residue; their full comparison cannot be replaced by using the word parity for both.

## CC4. The previously established connection with the user's Wick/Cartan work

The July source modular_cartan_realform_bridge_20260719.tex, lines 226–248, uses the parameter involution

\[
\rho(\zeta)=-\overline\zeta,
\qquad \rho(t+is)=-t+is.
\]

Here zeta is that source's complex modular parameter; it is neither the Riemann zeta function nor the user's tau. The real coordinate changes sign while the imaginary coordinate is retained. This is a formula about the supplied July operator construction, not a vector structure assigned to tau.

In the first Connes–Consani source, arXiv:2606.06604v1, Corollary luriearch, the exact cover is

\[
P=\mathbb C^\times/\mathbb R_{>0}
\longrightarrow
B=\mathbb C^\times/\mathbb R^\times,
\qquad [z]_+\longmapsto[z]_{\mathbb R}.
\]

The two rays over a line are exchanged by [z]_+ to [-z]_+. The July theorem, lines 722–768, constructs the associated real rank-two bundle with relation

\[
(p,t+is)\sim(rp,-t+is).
\]

Its map to the orientation line together with the retained imaginary coordinate is

\[
[p,t+is]\longmapsto([p,t],(\pi(p),is)).
\]

It is well-defined because replacing (p,t,s) by (rp,-t,s) preserves the class [p,t], the base pi(p), and is. Conversely a pair ([p,t],(pi(p),is)) maps to [p,t+is]. Choosing the other representative replaces (p,t) by (rp,-t), exactly the defining relation, so the inverse is well-defined. The composites are the identities by substitution; in every local covering chart the maps are continuous and real-linear. This proves the earlier typed comparison with all coordinates retained. The first summand is the orientation/Möbius line, and the second is a trivial imaginary line.

The later source's descended complex-point symmetry is

\[
\sigma(z)=-1/\overline z,
\qquad \sigma(0)=\infty,\quad\sigma(\infty)=0.
\]

Let I(z)=1/z, including I(0)=infinity and I(infinity)=0. Direct substitution gives

\[
I\circ\rho=\rho\circ I=\sigma.
\]

The original inversion, minus sign and conjugation all remain present. The two-copy orbit derivation is written in CARTAN_WICK_SPLINE_COMPARISON.md C2 and MIRROR_AND_PURITY.md M3 and is checked against the original CC.tex theorem at lines 989–1033.

The fixed generic topological point eta and the formula on complex-valued points belong to the actual source at their stated levels. The complex-valued-point involution has no fixed point: a finite nonzero fixed point would give z*conjugate(z)=-1, and the two endpoints are exchanged. This fact does not remove eta from the underlying three-point topological space. The paper uses both levels.

## CC5. Receiving statement for the user's construction

The user's latest statement is that the rotation is around their Z1/tau, and that its missing mirror parity is to be derived rather than stipulated. CC1–CC2 prove the fixed-base/no-exchanged-parity mechanism on the actual Connes–Consani source. Its unique generic point is the specific source object to compare with that proposed role for tau. It is not defined by averaging two numbers and is not the numbered endpoint zero.

This note has not declared a full identification of the source's enriched generic stalk with the user's latest Z0/no-torsion and Z1/torsion-without-parity proposal. That would have to retain the sign, imaginary generator, complete exponent data and involution in CC3; naming eta tau is not that construction. The existing Wick/Cartan comparison is retained in CC4 rather than discarded.

There is no additive-tau calculation here. The parity statement is a proved consequence about the specified mirror observation, not a new axiom. The user's proposed route to purity remains the research target; no numerical distance or RH conclusion is substituted for it.

## Sources and exact reading

- Alain Connes and Caterina Consani, [The Absolute Twistor Line and the Geometry of the compactification of Spec Z, v1](https://arxiv.org/html/2609.00299v1#S3), Sections 3–5. Original author TeX used: literature/lorscheid_sources_20260923/papers/06_new_user_intake/2609.00299/tex/CC.tex. This step read lines 350–407, 415–548, 557–685, 725–913, 970–1056, 1140–1225. No claim of reading the whole paper is made.
- Alain Connes and Caterina Consani, [On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve, v1](https://arxiv.org/html/2606.06604v1#S4.SS1.SSS1), Corollary luriearch. Original FF.tex lines 1521–1587 reread in this step.
- The supplied July modular-Cartan TeX, sections headed Canonical parity splitting of the modular plane and Typed descent of time and radial directions. Original lines 202–256 and 712–783 reread in this step.

Public arXiv pages were used to verify source identity. Mathematical reading used the original local TeX. The generic-point parity derivation and the multiplicative action were independently derived by a mathematical sub-agent; no independent agent was used for file discovery or recordkeeping.



# Winding data at the fixed point: parity, the integer ring, and its spectrum

24 September 2026. Private mathematical continuation. Proof labels W1–W10.

This note implements the user's requested passage from the fixed point to the arithmetic carried at it, using the actual Connes–Consani generic stalk. In the user's notation the proposed base role is \(\tau\langle Z_1;\text{no }Z_2\rangle\). The source point is denoted \(\eta\); a point, a section at that point, and a map of its sections retain their separate domains. No addition, subtraction, distance, vector, or numerical coordinate is assigned to \(\tau\). Here the user's word torsion means accumulated winding. The finite-order subgroup appearing below is separately called \(H\), to avoid identifying finite-order elements with that accumulated winding.

The newly proved result is an explicit recovery of integer parity and the ring \(\mathbb Z\), hence its spectrum, from the full signed rank-one stalk. The source itself already supplies the Laurent direction \(T^{\mathbb Z}\). This is therefore a recovery from that point together with its attached structure, not a derivation of the Laurent direction from uniqueness of a point alone. Purity is not assumed or asserted.

## W1. The actual fixed point and its full multiplicative data

The underlying source space has points \(+, -,\eta\), with open sets
\[
\varnothing,\quad\{\eta\},\quad\{+,\eta\},\quad\{-,\eta\},\quad\{+,-,\eta\}.
\]
Its only dense singleton is \(\{\eta\}\): its closure is the whole space, whereas each other singleton is closed. A homeomorphism preserves closure, by continuity in both directions. Consequently it must fix \(\eta\). The source involution exchanges \(+\) and \(-\), so \(\eta\) is its unique fixed point.

A two-state label exchanged by that involution cannot be assigned equivariantly to \(\eta\). Such a label would equal its exchanged value because the point is fixed; neither of the two labels equals its exchanged value. This proves the absence of that mirror-exchanged \(Z_2\) point-label. It does not discard the involution acting on the data attached to the point.

The generic spherical algebra is
\[
\mathcal O(\{\eta\})=\mathbf F_{1^2}[T^{\mathbb Z},J]/(J^2=\epsilon),\qquad \epsilon^2=1.
\]
At its underlying pointed-monoid level, keep the absorbing element and the entire group of nonabsorbing elements
\[
G=\langle T,J,\epsilon\mid TJ=JT,\ T\epsilon=\epsilon T,\ J\epsilon=\epsilon J,\ J^2=\epsilon,\ \epsilon^2=1\rangle.
\]
Here \(T\) is invertible, and \(J^{-1}=\epsilon J\). Every element has the unique form
\[
g=\epsilon^aT^mJ^b,\qquad a,b\in\{0,1\},\quad m\in\mathbb Z.
\]
For existence commute the factors, replace pairs of \(J\)'s by \(\epsilon\), and use \(\epsilon^2=1\). For uniqueness send \(T\) to \((1,\bar0)\), \(J\) to \((0,\bar1)\), and \(\epsilon\) to \((0,\bar2)\) in \(\mathbb Z\times(\mathbb Z/4\mathbb Z)\). These images satisfy every relation. The inverse sends \((m,\bar k)\) to \(T^mJ^k\), which is independent of the representative of \(\bar k\) because \(J^4=1\). Both composites are the identity on generators. Thus the coordinate descriptions are exactly equivalent, with all four imaginary/sign states retained. In the latter coordinates \(k=2a+b\pmod4\).

Write \(A=\alpha^*\) for the source action on sections. Its original formulas are
\[
A(T)=\epsilon T^{-1},\qquad A(J)=J^{-1}=\epsilon J,\qquad A(\epsilon)=\epsilon.
\]
They give the full action
\[
A(\epsilon^aT^mJ^b)=\epsilon^{a+m+b}T^{-m}J^b,
\qquad
A(T^mJ^k)=T^{-m}J^{2m-k}.
\]
Applying the first formula twice gives sign exponent \(a+2b\), integer exponent \(m\), and branch exponent \(b\), hence the original element. This proves \(A^2=1\), with its signs retained.

An element of \(G\) has finite order exactly when \(m=0\): a nonzero power of an element with \(m\ne0\) has nonzero integer exponent; every \(J^k\) has order dividing four. Therefore the intrinsic finite-order subgroup is
\[
H=\{1,J,\epsilon,\epsilon J\}=\langle J\rangle.
\]
Retain the whole exact sequence
\[
1\longrightarrow H\longrightarrow G\mathrel{\mathop{\longrightarrow}^{q}}L:=G/H\longrightarrow1.
\]
It is a connecting map, not a replacement of \(G\) by \(L\). The group \(L\) is infinite cyclic with generator \(t=q(T)\). Its elements \(t^m\) remain distinct for every integer \(m\). The induced action of \(A\) on \(L\) is \(t^m\mapsto t^{-m}\).

## W2. Derive the Z2 parity from the full signed mirror

For \(g\in G\), form the product of the source mirror image and the original section:
\[
N_A(g):=A(g)g.
\]
Direct calculation with every source factor gives
\[
N_A(\epsilon^aT^mJ^b)
=\epsilon^{2a+m+b}J^{2b}
=\epsilon^{2a+m+2b}
=\epsilon^m.
\]
For every \(h\in H\), \(A(h)h=1\). Since \(G\) is abelian,
\[
N_A(gh)=A(g)A(h)gh=N_A(g)N_A(h)=N_A(g).
\]
Thus it descends, independently of the imaginary branch, to the map
\[
\delta:L\longrightarrow\{1,\epsilon\},\qquad
\delta(q(g))=A(g)g,
\qquad
\boxed{\delta(t^m)=\epsilon^m.}
\]
It is a group homomorphism because \(N_A(g_1g_2)=N_A(g_1)N_A(g_2)\). It is onto since \(\delta(t)=\epsilon\). Its kernel is exactly \(\{t^{2r}:r\in\mathbb Z\}\): \(\epsilon\) has exact order two by W1, so \(\epsilon^m=1\) exactly when \(m\) is even. Consequently
\[
L/2L\ \xrightarrow{\ \sim\ }\ \{1,\epsilon\},
\qquad
[t^m]\longmapsto\epsilon^m,
\]
where \(2L\) denotes the subgroup of squares in the multiplicative notation for \(L\).

Encoding \(1\) as even and \(\epsilon\) as odd gives the user's \(Z_2\) quantum-number observation on the winding data. This encoding forgets information only when used alone; the working object retains \(g\), its full winding class \(q(g)\), and \(\delta(q(g))\) together. In particular \(T^2\ne T^4\), although their \(Z_2\) observations agree. Integer zero is the exponent-zero class in \(L\); neither it nor the identity section is identified with the topological point \(\eta\) or with \(\tau\).

The sign cannot be removed by changing the branch used to lift the winding. Any group section \(s:L\to G\) of \(q\) sends \(t\) to \(TJ^c\) for some \(c\pmod4\). Therefore
\[
s(t^m)=T^mJ^{cm},\qquad
A(s(t^m))=\epsilon^mT^{-m}J^{-cm}
=\delta(t^m)s(t^{-m}).
\]
The same factor \(\delta(t^m)\) appears for every \(c\). At \(m=1\) it is \(\epsilon\ne1\), so no such section intertwines \(A\) with inversion on \(L\). This is a precise, branch-independent parity defect in the retained signed extension.

## W3. Recover the integer ring without adding the base point to anything

Let
\[
R=\operatorname{End}_{\mathrm{Ab}}(L)
\]
be the set of group endomorphisms of the winding group. Its addition and multiplication are explicitly
\[
(f\mathbin\oplus h)(\ell)=f(\ell)h(\ell),\qquad
(f\mathbin\odot h)(\ell)=f(h(\ell)),\qquad \ell\in L.
\]
The first operation is a group endomorphism because \(L\) is abelian: its value on \(\ell_1\ell_2\) is the product of its values on \(\ell_1\) and \(\ell_2\). The additive identity is the map \(\ell\mapsto1_L\); the additive inverse sends \(\ell\) to \(f(\ell)^{-1}\). Associativity and commutativity of addition follow pointwise from the group law. Composition is associative and has identity \(\operatorname{id}_L\). For left distributivity use the homomorphism law of \(f\); for right distributivity evaluate the pointwise product at \(h(\ell)\). Thus these operations give an endomorphism ring. They are operations on maps of the retained data. They supply no addition involving \(\tau\).

For each integer \(n\), let \([n]:\ell\mapsto\ell^n\). Evaluation at the generator gives a full classification: every endomorphism sends \(t\) to a unique \(t^n\), and then sends \(t^m\) to \(t^{nm}\). Hence
\[
\iota:\mathbb Z\longrightarrow R,\qquad n\longmapsto[n]
\]
is bijective. Direct evaluation gives
\[
[n]\oplus[m]=[n+m],\qquad
[n]\odot[m]=[nm],\qquad \operatorname{id}_L=[1].
\]
This proves that \(\iota\) is a unital ring isomorphism. It does not depend on choosing \(t\) rather than \(t^{-1}\), since \([n](t^{-1})=t^{-n}=(t^{-1})^n\). More intrinsically \([n]\) is the power map, defined on every abelian group independently of a chosen generator. The generator is used only to prove that these are all the maps.

Conjugation by the source involution on \(L\) acts trivially on this ring: inversion composed with \([n]\) and then inversion again sends \(\ell\) to \(\ell^n\). Thus the recovered integer ring is independent of which ordering the mirror exchanges.

## W4. Recover all of Spec Z, with its local rings and residue norms

The ring isomorphism induces the explicit map
\[
\operatorname{Spec}R\longrightarrow\operatorname{Spec}\mathbb Z,
\qquad \mathfrak p\longmapsto\iota^{-1}(\mathfrak p).
\]
Its inverse sends an ideal to its image under \(\iota\). Primality is preserved in both directions because products and membership are preserved and \(\iota\) is bijective.

For completeness classify the ideals. A nonzero ideal of \(\mathbb Z\) contains a least positive integer \(d\). Division with remainder shows every element of the ideal is divisible by \(d\): otherwise its remainder would be a smaller positive member. Conversely the ideal contains every multiple of \(d\), so it equals \(d\mathbb Z\). The zero ideal is prime because a product of nonzero integers is nonzero. A nonzero proper ideal \(d\mathbb Z\) is prime precisely when \(d\) is prime. If \(d=ab\) with \(1<a,b<d\), then \(ab\) belongs to the ideal but neither factor does. If \(d=p\) is prime and \(p\nmid a\), Euclidean division yields Bezout integers \(u,v\) with \(ua+vp=1\); multiplying by \(b\) proves \(p\mid b\) whenever \(p\mid ab\). Therefore the prime points are exactly
\[
\mathfrak p_0=\{[0]\},\qquad
\mathfrak p_p=\{[pk]:k\in\mathbb Z\}\quad(p\text{ a positive rational prime}).
\]
The basic open \(D([n])\) maps to \(D(n)\), by the same membership test. These basic opens define both Zariski topologies, so the map is a homeomorphism, including the zero element: \(D([0])=\varnothing\). The zero ideal is the generic point since it lies in every nonempty basic open. Each \(\mathfrak p_p\) is closed: its quotient is the field with \(p\) elements, so no larger proper prime contains it.

The structure sheaf is retained as well. On each basic open, extend \(\iota\) to
\[
\mathbb Z[1/n]\longrightarrow R[1/[n]],\qquad
\frac{a}{n^k}\longmapsto\frac{[a]}{[n]^k}.
\]
Cross multiplication shows this is independent of the representative; applying \(\iota^{-1}\) to numerator and denominator gives its inverse. These maps commute with localization restriction maps because both send a fraction to the same fraction in the larger localization. Thus the affine schemes, not merely their point sets, are isomorphic. At \(\mathfrak p_p\) the local ring consists of fractions \([a]/[b]\) with \(p\nmid b\), and the residue field is \(\mathbb F_p\); at \(\mathfrak p_0\) the local ring is \(\mathbb Q\) through the corresponding fraction map.

The winding data also gives the residue norm directly. The quotient \(L/[p]L\) has exactly \(p\) elements, represented by \(1,t,\ldots,t^{p-1}\); division of the exponent gives existence, and distinctness follows since two exponents in that range cannot differ by a nonzero multiple of \(p\). Consequently
\[
N(\mathfrak p_p)=|R/\mathfrak p_p|=|L/[p]L|=p.
\]
This includes \(p=2\). Nothing in this construction removes that prime.

This affine scheme has been derived from the attached rank-one data. It is not the three-point archimedean space \(X\) itself. Connes–Consani's Section 7 separately supplies the finite arithmetic curve as an input to its amalgam; the endomorphism-ring derivation here specifies another exact route from the retained generic data to its integer spectrum.

## W5. Exactly which arithmetic degrees preserve the complete signed mirror

Classify group endomorphisms \(f:G\to G\) satisfying both
\[
f(\epsilon)=\epsilon,\qquad fA=Af.
\]
Because a homomorphism sends finite-order elements to finite-order elements, \(f(J)=J^b\). Preserving \(\epsilon=J^2\) forces \(2b=2\pmod4\), so \(b\) is either \(1\) or \(3\). The image of \(T\) has the form \(T^nJ^c\), with \(n\in\mathbb Z\) and \(c\pmod4\) arbitrary. These assignments respect all group relations and define a group homomorphism.

On the generator \(J\), the commuting relation holds automatically. On \(T\), compute both sides with all factors:
\[
f(A(T))=f(\epsilon T^{-1})=\epsilon T^{-n}J^{-c},
\]
\[
A(f(T))=A(T^nJ^c)=\epsilon^nT^{-n}J^{-c}.
\]
Equality holds exactly when \(\epsilon^n=\epsilon\), namely when \(n\) is odd. Since \(T,J\) generate \(G\), this condition is necessary and sufficient. Thus every such map, and no other one, is
\[
f_{n,c,b}(T)=T^nJ^c,\quad f_{n,c,b}(J)=J^b,
\qquad n\text{ odd},\quad c\in\mathbb Z/4,\quad b\in\{1,3\}.
\]
Composition, applying the second map first, is
\[
f_{n,c,b}\circ f_{n',c',b'}
=f_{nn',\,cn'+bc',\,bb'},
\]
with the last two indices read modulo four. This follows by applying the composite to \(T\) and \(J\). The induced map on \(L\) is \([n]\).

There is also an intrinsic parity proof of the same restriction. The equality \(fA=Af\) implies
\[
N_A(f(g))=f(N_A(g)).
\]
Taking \(g=T\), the right side is \(\epsilon\), whereas the left side is \(\epsilon^n\). Hence the degree must be odd. Conversely the classified maps realize every odd degree.

Therefore \([2]\) is a genuine endomorphism of the recovered winding group and \((2)\) is a genuine prime in its recovered spectrum, but \([2]\) has no lift preserving both this sign and this source involution. These are simultaneous proved statements. They explain precisely why retaining the full signed geometry changes the allowed arithmetic action without deleting the prime from the integer spectrum.

For an even degree the exact failed commuting factor is \(\epsilon\): the two computed images of \(T\) differ by multiplication by \(\epsilon\). Retaining this defect, instead of replacing \(\epsilon\) by \(1\), specifies the extension problem at degree two.

The source power maps are the distinguished choices
\[
F_n(g)=g^n=f_{n,0,\bar n}(g),\qquad n>0\text{ odd}.
\]
They retain the imaginary-branch action \(J\mapsto J^n\). On the source's complex-point quotient the complete formula is
\[
F_n(z)=
\begin{cases}
z^n,&n\equiv1\pmod4,\\
-1/z^n,&n\equiv3\pmod4.
\end{cases}
\]
Indeed the unquotiented map is \((z,j)\mapsto(z^n,j^n)\). In the first case \(j^n=j\). In the second \(j^n=-j\), and returning to the chosen sphere uses \((w,-j)\mapsto(-1/w,j)\). Both branches, the minus sign, and the endpoints \(0,\infty\) remain part of this formula.

## W6. Why the fixed-point data must remain equivariant

Solving \(A(T^mJ^k)=T^mJ^k\) gives \(m=-m\), hence \(m=0\), and then \(-k=k\pmod4\), hence \(k=0\) or \(2\). Thus
\[
G^A=\{1,\epsilon\}.
\]
Including the absorbing element gives the signed base \(\{0,1,\epsilon\}\). Taking only strictly fixed sections therefore retains no nonzero winding exponent. Keeping the object \((G,A)\) over the fixed point keeps all exponents and all four branch/sign states, with the involution as part of the data. This is the exact mathematical distinction behind the user's instruction that the fixed point must carry the amount of winding. No number of copies of \(\tau\) is introduced.

The fixed group and the equivariant group are connected by the explicit inclusion \(\{1,\epsilon\}\hookrightarrow G\), and the full exponent observation is \(q:G\to L\). The first inclusion followed by \(q\) has only the identity as image. This proves exactly which data the fixed-section passage retains and which data the winding passage uses.

## W7. What the same source action does to modulus

The source's generic complex-valued points have
\[
\chi(T)=z\in\mathbb C^\times,\qquad
\chi(J)=j\in\{i,-i\},\qquad
\chi(\epsilon)=-1.
\]
Every such pair gives the group character
\[
\chi_{z,j}(\epsilon^aT^mJ^b)=(-1)^a z^m j^b.
\]
The relations hold because \(j^2=-1\); conversely a character respecting \(\epsilon\mapsto-1\) has these values and is uniquely determined by them. The pointed absorbing element goes to zero. These are the actual evaluation maps used in the source, not a metric or coordinate assigned to \(\tau\).

Precomposition by \(A\) gives
\[
\chi_{z,j}\circ A=\chi_{-z^{-1},\,-j}.
\]
Ordinary complex conjugation sends \((z,j)\) to \((\bar z,-j)\). Returning to the original branch after applying it gives the source twistor involution
\[
\sigma(z)=-\frac1{\bar z},\qquad\sigma(0)=\infty,\quad\sigma(\infty)=0.
\]
For every finite nonzero \(z\),
\[
|\chi_{z,j}(\epsilon^aT^mJ^b)|=|z|^m,
\qquad |\sigma(z)|=|z|^{-1}.
\]
Consequently the radius product for the reflected pair is exactly one. The pair has equal radii exactly when \(|z|=|z|^{-1}\), which for a positive radius is equivalent to \(|z|=1\). The source accepts every \(z\in\mathbb C^\times\); in particular both \((1,i)\) and \((2,i)\) satisfy every defining relation and their full reflected partners are \((-1,-i)\) and \((-1/2,-i)\). Thus the actual source retains a radial parameter; its reciprocal symmetry does not by itself fix that parameter to one.

This calculation is about characters of the same retained stalk. These characters have not been identified with eigenvalues detecting the zeros of the original Riemann zeta function. It is therefore neither a counterexample to arithmetic purity nor a proof of it. It identifies the exact radial behavior of the structure just used to recover parity and the integer spectrum.

## W8. The proved chain and its present endpoint

The construction proved here is
\[
(\eta,\mathcal O_\eta,A)
\longrightarrow (G,H,A,q)
\longrightarrow (L,\delta)
\longrightarrow R=\operatorname{End}_{\mathrm{Ab}}(L)
\longrightarrow\operatorname{Spec}R\cong\operatorname{Spec}\mathbb Z.
\]
The arrows mean, in order: retain the multiplicative data of the original generic stalk; retain the finite-order subgroup and take its winding quotient with the full extension still present; form its endomorphism ring by the operations in W3; and take the affine spectrum with the explicit scheme isomorphism of W4. The \(Z_2\) observation is derived by \(A(g)g\), rather than imposed by attaching an arbitrary parity tag to a number.

This supplies the arithmetic-recovery part of the user's proposed chain at the actual source-stalk level. It also gives the exact signed restriction on arithmetic actions and the complete character-radius symmetry. It has not derived purity or an RH verdict. The recoverable integer arithmetic comes from the rank-one structure carried at the point, which the source explicitly supplies; its existence has not been deduced from topological uniqueness alone.

The \(Z_0/Z_1\) distinction in the user's latest articulation is not settled here by assigning different labels at the outset. No source addition involving \(\tau\), numerical distance from \(\tau\), or replacement zeta function has been introduced.

## Source provenance and reading coverage

Original authors: Alain Connes and Caterina Consani. Source: The Absolute Twistor Line and the Geometry of the compactification of Spec Z, arXiv:2609.00299v1. Canonical index ID: arXiv:2609.00299v1. Original author TeX: literature/lorscheid_sources_20260923/papers/06_new_user_intake/2609.00299/tex/CC.tex. This continuation directly read lines 489–608, 771–903, 966–1052, 1051–1149, and 1151–1194. The shared source index was read for routing and identity; its broader coverage note is not a claim that this continuation reread the entire paper.

Source Sections 3–4 supply the stalk, sign, branch and involution. Sections 5–6 supply complex evaluation and twistor conjugation. Section 7 supplies the odd power action and separately takes the finite arithmetic curve into the amalgam. W2–W6 are explicit derivations here from those objects; no claim of novelty is made. An independent mathematical agent rederived the parity defect, the endomorphism-ring reconstruction, and the complete commuting-map classification.

Public source: https://arxiv.org/html/2609.00299v1

The user articulation receiving this calculation is recorded verbatim as U144–U146 and attachment A11 in TAU_DEFINITIONS_AND_CORRECTIONS_VERBATIM.md. The earlier fixed-point and July Wick/Cartan comparison remains in CC_FIXED_GENERIC_POINT_AND_MIRROR_PARITY.md, CC1–CC5.


## W9. What remains the center while winding changes

The exact source object is the unique generic point \(\eta\), with its attached stalk and induced involution. The proposed comparison is to the user's \(\tau\langle Z_1;\text{no }Z_2\rangle\); this does not assert an identification of every further proposed structure.

W1 proves, using the complete three-point topology, that every homeomorphism fixes \(\eta\). The source involution exchanges both other points, so its fixed-point set is exactly \(\{\eta\}\). Its fixedness is a consequence of that topology. No midpoint, coordinate, numerical origin or distance was used.

Let \(M_\eta=G\sqcup\{0\}\) be the underlying pointed monoid of the source stalk. The natural stalk projection to its supporting point is \(\pi_\eta:M_\eta\to\{\eta\}\). For every integer \(r\), multiplication by the actual unit \(T^r\) defines a bijection of this fiber,
\[
\mu_r(g)=T^r g\quad(g\in G),\qquad \mu_r(0)=0.
\]
Its inverse is \(\mu_{-r}\), and \(\mu_r\mu_s=\mu_{r+s}\), by the group law of the source units. These are actions on stalk elements, not addition or multiplication of the base point. For \(r\ne0\), \(\mu_r\) is not a unital monoid homomorphism: it sends the identity to \(T^r\ne1\).

Both the winding action and the source mirror stay over the same point:
\[
\pi_\eta\mu_r=\pi_\eta,\qquad
\pi_\eta A=\alpha\pi_\eta=\pi_\eta.
\]
These equalities record the domains: winding changes data in the actual stalk; the underlying source involution fixes its supporting point by the preceding topological proof. In particular,
\[
\alpha(\eta)=\eta,\qquad A(T^m)=\epsilon^mT^{-m}.
\]
The point is unchanged even though the full signed winding datum is not. More generally, the exact interaction between winding and mirror is
\[
A\mu_r(g)=A(T^r)A(g)=\epsilon^rT^{-r}A(g).
\]
Thus reversing the winding retains the sign factor \(\epsilon^r\); it cannot silently be omitted.

A freely exchanged two-state point label cannot extend equivariantly to \(\eta\), since it would have to equal its exchanged label. This statement concerns that point observation. It does not assert that the stalk has no parity: W2 derives its winding parity \(A(g)g=\epsilon^m\). The point, the stored count, and its parity observation retain their distinct roles.

Finally, iterating the involution alone does not retain an integer count, since \(A^2=1\). The distinct source units \(T^m\) retain that count. Their presence in the source stalk is an input of the Connes–Consani construction, not a consequence of fixedness alone. The source therefore gives an exact answer to what remains fixed while the retained winding varies, without yet deriving that full stalk from a bare parityless point.


## W10. Fixed support, parity exchange and retained count in one source structure

This section receives the user's clarification that Z1 and Z2 are proposed as parts of one structure, rather than that Z1 alone generates all other data. All maps below use the source stalk of W1. The proposed identification with the user's Z0/Z1 terminology remains recorded as exploratory.

Retain G, its finite-order subgroup H=<J>, the quotient q:G->L and the involution A exactly as in W1–W2. Put t=q(T). The element t has infinite order by the proved description of G. The parity observation is the already derived homomorphism delta(t^m)=epsilon^m, with epsilon of exact order two.

Define the actual winding step on L by S(ell)=t ell. It is a bijection, with inverse ell->t^(-1)ell; it is not a group homomorphism since S(1)=t!=1. Its integer powers are S^n(ell)=t^n ell, for every n in Z, by induction in each direction. Thus its orbit of the identity consists of every element of L exactly once. These assertions use the infinite cyclic source direction; they do not deduce that direction from the uniqueness of a point.

The exact observation square is
\[
\begin{array}{ccc}
L&\xrightarrow{S}&L\\
\delta\downarrow&&\downarrow\delta\\
\{1,\epsilon\}&\xrightarrow{r}&\{1,\epsilon\},
\end{array}
\qquad r(v)=\epsilon v.
\]
Indeed delta(S ell)=delta(t)delta(ell)=epsilon delta(ell). The map r satisfies r^2=1 and has no fixed value. The map S has infinite order: S^n(1)=1 forces t^n=1, hence n=0. Therefore the retained counting operation is a lift of a parity involution. Its square restores parity while preserving the distinct winding state t^2. The same square on the full source units uses mu_1(g)=Tg and delta q; no branch data are discarded from G.

The supporting point remains fixed throughout: the stalk projection pi_eta of W9 satisfies pi_eta mu_n=pi_eta for every n. Independently, the source involution fixes eta by the topological argument W1. These two statements concern the actual common support, not a coordinate assigned to that point.

The original source mirror induces a(ell)=ell^(-1) on L. It preserves the integer parity observation, since
\[
\delta(a\ell)=\delta(\ell)^{-1}=\delta(\ell).
\]
It reverses the counting step:
\[
aS(\ell)=(t\ell)^{-1}=t^{-1}\ell^{-1}=S^{-1}a(\ell).
\]
Before passage to L, define c(g)=epsilon g and retain every source sign. Direct substitution gives
\[
A\mu_n(g)=A(T^n)A(g)=\epsilon^nT^{-n}A(g),
\qquad A\mu_n=c^n\mu_{-n}A.
\]
All of c, mu_n and A extend to the pointed stalk by fixing its absorbing zero. These are bijections of source states; mu_n and c are not asserted to be unital monoid homomorphisms. Applying q to the displayed identity gives aS^n=S^(-n)a because q(epsilon)=1, with the original signed identity still retained.

There is also an exact two-reflection realization of the counting step. On L set b=Sa. Then
\[
b(t^m)=t^{1-m},\qquad b^2=SaSa=SS^{-1}=1,\qquad ba=S.
\]
Thus two involutions compose to give the infinite-order winding step. On the full source units the corresponding map is B=mu_1 A. Its square retains a sign:
\[
B^2=\mu_1 A\mu_1 A=\mu_1c\mu_{-1}A^2=c,
\qquad B^4=c^2=1.
\]
The map c is not the identity because c(1)=epsilon!=1. Hence B has order four on the full source, even though its image b on L has order two. The factor is not suppressed or treated as irrelevant.

These formulas distinguish the actual operations without disconnecting them: source mirror A, winding step mu_1, quotient reflections a,b, and the parity exchange r have the exact commuting and composition relations displayed above. In particular, the source mirror A is not itself the count-advancing operation.

The claim that every involution must have a fixed center does not follow from the definition of an involution. The present source already exhibits the obstruction: r exchanges its two parity values and has no fixed value. Likewise b(t^m)=t^m would require 2m=1, which has no integer solution. Their action nevertheless is involutive and bijective by the computations above. The maps delta and q prove their relationship to the full source with fixed support; these are not unrelated substitute examples. The specific fixed point eta is guaranteed by the CC three-point topology and the placement of the sheaf data, not by involutivity or bijectivity alone.

Consequently, the rigorous coupled construction retains a fixed supporting point, full integer winding states, a two-state parity observation, and a lift of parity exchange. Parity alone is not the full count, because delta(t^m)=delta(t^(m+2)) while t^m!=t^(m+2). The source's full Laurent direction is the additional structure which keeps that distinction. No arithmetic operation or numerical distance involving tau is introduced.



# Deligne's exact common modulus and the retained winding characters

24 September 2026. Private continuation. Proof labels D1–D5. This note answers the user's request to retrieve Deligne from GitHub and make the proposed common-distance comparison exact. It retains all original powers of the residue cardinality. It introduces no distance or addition on the user's parityless \(\tau\langle Z_1;\text{no }Z_2\rangle\).

## D1. The retrieved source and the meaning of same

The GitHub file D032_FULL_EN.tex was retrieved at commit 492a44c2938cc6f5e3c41105567492a8fa528c8c of KokunoYumeto/zeta-function-research-reader. Its SHA-256 is 316cbc52349cd6bc2dedbd0a493a530696d367ca0e292fc64ee3c3973327567e. It is a historical English transcription, not Deligne's original author TeX. The current French S20 transcription was read beside it. No original author TeX is available in this indexed edition; the distinction is preserved rather than describing a transcription as an author file. The published article is Pierre Deligne, La conjecture de Weil. II, IHES 52 (1980), 137–252.

Definition 1.2.1 says that an algebraic number \(\alpha\) is pure of weight \(w\), relative to a prime power \(q\), when every complex embedding has
\[
|\iota(\alpha)|=q^{w/2}.
\]
For a sheaf, Definition 1.2.2 applies this statement to Frobenius eigenvalues at every closed point \(x\), with \(q\) replaced by its residue-field size \(N(x)\). Thus the original pointwise formula is
\[
|\iota(\alpha_x)|=N(x)^{w/2}.
\]
A common weight is the same exponent \(w\) throughout this statement. It does not make different residue cardinalities equal. For instance the weight-one radii at residue cardinalities two and three are \(2^{1/2}\) and \(3^{1/2}\). At a fixed finite field and fixed pure weight all the relevant eigenvalues and all their complex conjugates do have one common numerical radius. The radius is a complex absolute value of an eigenvalue; it is not a subtraction of the geometric base point from that eigenvalue.

Keep the symbols separate: \(m\) in the winding source \(T^m\) counts signed turns; \(w\) denotes Deligne's weight; \(i\) below is cohomological degree. None is identified with another merely because all are integer-valued in the relevant instances.

## D2. How the exact circle is obtained, retaining the Tate factor

Here are Deligne's hypotheses and the actual last step of the proof. Let \(X_0\) be smooth of finite type over \(\mathbb F_q\), pure of dimension \(d\). Let \(\ell\) differ from the field characteristic and let \(\mathcal F_0\) be a lisse pure \(\overline{\mathbb Q}_\ell\)-sheaf of weight \(n\). Put \(X=X_0\times_{\mathbb F_q}\overline{\mathbb F}_q\) and let \(\mathcal F\) be its pullback. These are the hypotheses of the cited theorem, not hypotheses asserted for the user's construction.

Deligne 3.3.4 gives weights at most \(n+i\) on
\[
V_c=H_c^i(X,\mathcal F).
\]
The dual sheaf has weight \(-n\). Applying 3.3.4 to it gives weights at most
\[
-n+(2d-i)
\]
on \(W=H_c^{2d-i}(X,\mathcal F^\vee)\). In the geometric Frobenius convention a Tate twist \((d)\) multiplies its eigenvalues by \(q^{-d}\). Poincare duality is the exact Frobenius-equivariant identification
\[
H^i(X,\mathcal F)\cong\bigl(H_c^{2d-i}(X,\mathcal F^\vee)(d)\bigr)^\vee.
\]
Therefore an eigenvalue \(\beta\) on \(W\) produces the eigenvalue
\[
\lambda=(q^{-d}\beta)^{-1}=q^d/\beta
\]
on the dual space. For every complex embedding, the cited upper estimate gives
\[
|\iota(\beta)|\le q^{(-n+2d-i)/2}.
\]
Retaining the whole Tate factor yields
\[
|\iota(\lambda)|
=\frac{q^d}{|\iota(\beta)|}
\ge \frac{q^d}{q^{(-n+2d-i)/2}}
=q^{(n+i)/2}.
\]
This proves the lower weight assertion 3.3.5 from the upper assertion and the stated duality theorem.

Now take the actual Frobenius-equivariant comparison map
\[
u:H_c^i(X,\mathcal F)\longrightarrow H^i(X,\mathcal F)
\]
and its image \(I\). This image is simultaneously a quotient of \(V_c\) and a subspace of \(H^i\). For an invariant subspace, a basis beginning with a basis of the subspace makes the matrix of Frobenius block triangular; hence its characteristic polynomial is the product of those on the subspace and quotient. It follows that eigenvalues of \(I\), with their algebraic conjugates, satisfy both the cited upper estimate and the derived lower estimate. Thus each satisfies
\[
q^{(n+i)/2}\le |\iota(\alpha)|\le q^{(n+i)/2},
\qquad
\boxed{|\iota(\alpha)|=q^{(n+i)/2}.}
\]
This is Corollary 3.3.6. If \(X_0\) is proper, compactly supported and ordinary cohomology coincide, so the image is the whole cohomology. For constant coefficients of weight zero and degree one, the radius is exactly \(q^{1/2}\). No division by \(q^{1/2}\) has replaced that eigenvalue.

The equality has therefore been derived on a specified image of a specified cohomological map. The construction of that map and the two controls are the mechanisms, rather than an assumption that every noncentral datum has a common distance.

## D3. The product mechanism behind the upper control

The preceding use of 3.3.4 is a use of Deligne's theorem, not a claim to have reproduced its entire proof here. The relevant part of his curve argument was also read directly in the current French text, 3.2.4–3.2.15. Here is its exact numerical mechanism and the source geometry it uses.

For a smooth curve and a lisse sheaf of pointwise weight zero, 3.2.4 proves, for every integer \(k\ge0\),
\[
w_q(\alpha)\le1+2^{-k},
\qquad
w_q(\alpha)=\frac{2\log|\iota(\alpha)|}{\log q}.
\]
He forms \(S_0=X_0\times X_0\), \(V_0=U_0\times U_0\), and the external tensor product \(\mathcal G_0=\mathcal F_0\boxtimes\mathcal F_0\). A Lefschetz pencil, its vanishing cycles, and the local monodromy filtration control the Leray terms. At the decisive induction step he has Frobenius-equivariant inclusions
\[
H_c^1(U,\mathcal F)\otimes H_c^1(U,\mathcal F)
\hookrightarrow H_c^2(V,\mathcal G)
\hookrightarrow H_c^2(\widetilde V,\pi^*\mathcal G).
\]
The target weight bound is \(2+2^{-k}\). If \(\alpha\) is a source eigenvalue, a nonzero eigenvector tensored with itself gives eigenvalue \(\alpha^2\) in the tensor square. Over a field its pure tensor is nonzero: choose a linear functional nonzero on the eigenvector and apply its tensor square. The injections preserve that eigenvalue. Therefore
\[
2w_q(\alpha)=w_q(\alpha^2)\le2+2^{-k},
\qquad
w_q(\alpha)\le1+2^{-(k+1)}.
\]
Holding for every \(k\), these inequalities imply \(w_q(\alpha)\le1\): any larger value differs from one by a positive amount, and some \(2^{-k}\) is smaller than that amount. For pointwise weight \(\beta\), the original bound is \(\beta+1\). Deligne applies it to \(\mathcal F_0^\vee(1)\), whose weight is \(-\beta-2\); the duality pairing then gives
\[
w_q(\alpha^{-1})\le(-\beta-2)+1,
\qquad w_q(\alpha)\ge\beta+1.
\]
Together the two results give weight exactly \(\beta+1\).

This is weight control driven by product geometry and duality. It is not a finite numerical scan. This note uses the source's geometric lemmas, rather than claiming to have reconstructed its monodromy and vanishing-cycle proofs in full.

## D4. The precise same-modulus receiver for the retained winding

Use the full signed generic group and action proved in W1–W2 of WINDING_PARITY_AND_INTEGER_SPECTRUM.md. Its actual signed complex-character space is
\[
\mathcal C=\{\chi_{z,j}:z\in\mathbb C^\times,\ j\in\{i,-i\}\},
\qquad
\chi_{z,j}(T^mJ^k)=z^m j^k.
\]
Here \(k\pmod4\) retains both the imaginary branch and the sign. Define the space of bounded-winding evaluations inside this actual character space by
\[
\mathcal U=\left\{\chi\in\mathcal C:\sup_{m\in\mathbb Z}|\chi(T^m)|<\infty\right\}.
\]
This is a space of evaluation maps, not a boundedness axiom placed on \(\tau\). Its definition is independent of changing the source lift from \(T\) to \(TJ^c\) or to its inverse, because \(|j^c|=1\) and both signs of \(m\) occur.

Write \(r=|z|>0\). Then \(|\chi(T^m)|=r^m\). If \(r>1\), positive powers are unbounded; if \(r<1\), negative powers are unbounded; if \(r=1\), every power has modulus one. This proves the exact classification
\[
\boxed{\mathcal U=\{\chi_{z,j}:|z|=1,\ j=\pm i\}.}
\]
For every \(g=\epsilon^aT^mJ^b\in G\) and every \(\chi\in\mathcal U\),
\[
|\chi(g)|=|(-1)^a z^m j^b|=1.
\]
The full pointed monoid has a faithful receiver in functions on \(\mathcal U\):
\[
E:G\sqcup\{0\}\longrightarrow\operatorname{Map}(\mathcal U,\mathbb C),
\qquad E(g)(\chi)=\chi(g),\quad E(0)=0.
\]
It preserves multiplication and the absorbing element by the character law. To prove injectivity, suppose \(E(T^mJ^k)=E(T^{m'}J^{k'})\). Evaluate first at \((z,j)=(1,i)\); this gives \(k=k'\pmod4\). Thus \(z^{m-m'}=1\) for every \(|z|=1\). If \(a=m-m'\ne0\), choose \(z=\exp(i\pi/a)\); then \(z^a=-1\), a contradiction. Hence \(m=m'\). Finally the zero function differs from each nonabsorbing image because those images have modulus one at every character. All integer winding data and all four branch/sign states therefore survive in this receiver despite its common modulus.

The source involution preserves \(\mathcal U\) by
\[
\alpha_{\mathcal C}(z,j)=(-z^{-1},-j).
\]
The receiver is exactly equivariant:
\[
E(A(g))(\chi)=\chi(A(g))=E(g)(\chi\circ A).
\]
Every sign-preserving commuting lift \(f_{n,c,b}\) from W5 also preserves \(\mathcal U\), because its character action is
\[
(z,j)\longmapsto(z^n j^c,j^b),
\]
whose spatial coordinate has modulus \(|z|^n=1\), while odd \(b\) retains \(j^b\in\{i,-i\}\). On the source's quotient sphere the odd Frobenius branches remain \(z^n\) and \(-1/z^n\), both preserving this circle. The full character space \(\mathcal C\), its inclusion \(\mathcal U\hookrightarrow\mathcal C\), and its unrestricted radii are retained; no rescaling turns an arbitrary source character into a unit character.

This proves a substantive part of the user's geometric picture: all full winding integers can be retained faithfully while their evaluated values have the same modulus. The property is realized by the precisely identified bounded-winding character space. The absence of a parity label at the fixed base point did not, by itself, establish that every arithmetic spectral receiver is this space.

## D5. Exact comparison with purity and limits of the result

The statement in D4 concerns values of all group elements under a family of multiplicative characters. Deligne's statement concerns eigenvalues of a particular Frobenius action on one cohomological degree, including every algebraic conjugate and the full residue-cardinality factor. The following exact formula connects repetition with his modulus law without discarding that factor. For an eigenvalue \(\alpha\) of pure weight \(w\) relative to \(q\), iteration \(r\) gives
\[
|\iota(\alpha^r)|=q^{rw/2}=(q^r)^{w/2}.
\]
Thus the weight remains \(w\) when the base finite field is extended to cardinality \(q^r\), while the original numerical radius changes. By comparison, winding evaluation has \(|\chi(T^m)|=|z|^m\). Both preserve the full exponent; a constant numerical radius for all windings corresponds to the special unit-character sector, not to dropping \(q^{w/2}\) from Deligne's formula.

The arithmetic reconstruction W1–W6 and the faithful common-modulus receiver D4 are now proved. No cohomological realization identifying this receiver with the eigenvalues detecting zeros of the original Riemann zeta function has been derived here. Consequently no RH conclusion is claimed. Neither the integer spectrum nor the common-modulus construction is discarded because this last identification is absent.

## Source comparison corrections retained in the reading record

The fetched GitHub historical English witness compresses several proof passages. In its lines 2064–2066 it writes the polynomial \(\det(1-Ft)\) and then assigns its roots the eigenvalue radius \(q^{i/2}\). The current French 3.3.9 instead uses \(\det(t\,1-F^*)\), whose roots are the eigenvalues and correctly have that radius. These two polynomials have reciprocal roots: \(\det(1-tF)=\prod_j(1-t\alpha_j)\), so its roots are \(\alpha_j^{-1}\), of modulus \(q^{-i/2}\). This follows directly by factoring the characteristic polynomial over an algebraic closure and preserves all multiplicities. The source file has not been silently rewritten; the corrected receiving formulas here use the current French statement.

The historical English 3.2.4 prints strict inequalities where the current French 3.2.4, 3.2.11–13 use non-strict inequalities. D3 retains the current French inequalities. The English compressed 3.2.7 calls the external tensor product itself real; the French proof first adjoins its dual by the direct sum \(\mathcal G_0\oplus\mathcal G_0^\vee\). D3 does not replace that source construction with the compressed assertion. The current French, not the historical English shortening, governs these comparisons.

Reading coverage: GitHub English lines 116–145, 572–622 and 1939–2110; current French S20 lines 477–541, 2088–2227 and 2221–2308. D2's Tate-factor calculation and D4's faithful character receiver were independently derived by a mathematical agent. This is a reading of the named passages, not a claim of rereading all Weil II.

Public original identity: https://www.numdam.org/item/PMIHES_1980__52__137_0/

Pinned GitHub transcription: https://github.com/KokunoYumeto/zeta-function-research-reader/blob/492a44c2938cc6f5e3c41105567492a8fa528c8c/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/prior_intakes/supporting_sources/D032_FULL_EN.tex



# Prime clocks, orchard visibility, and faithful prime observations

24 September 2026. Private continuation. Proofs P1–P14. This receives the user's proposal that prime spectral appearances should recover all other counts. The word torsion in that proposal means retained winding. Finite-order groups below are identified explicitly. No arithmetic operation, coordinate or distance is assigned to tau. No RH conclusion or identification of these character values with arithmetic Frobenius eigenvalues is asserted.

## P1. Integer winding from the actual oriented-ray covering

Connes–Consani, arXiv:2606.06604v1, Corollary luriearch, gives the actual covering
\[
P=\mathbb C^\times/\mathbb R_{>0}\longrightarrow B=\mathbb C^\times/\mathbb R^\times.
\]
Original FF.tex lines 1521–1580 were reread for this calculation. The source complex scalar origin is not identified with the user's tau, and the reference line chosen below is not the generic point eta of the other source paper.

Write a nonzero complex number as r exp(i theta), with r>0. The two quotient maps identify respectively angles differing by 2pi and by pi. Thus the maps
\[
\mathbb R\longrightarrow P,\quad\theta\longmapsto[e^{i\theta}]_+,
\qquad
\mathbb R\longrightarrow B,\quad\theta\longmapsto[e^{i\theta}]_{\mathbb R^\times}
\]
retain periods 2pi and pi respectively. These are coordinates on the source's ray and line spaces, not coordinates of tau. Intervals of length less than pi project injectively to B; their translates by integer multiples of pi give its covering charts.

Fix the reference line ell_0=[1]. A continuous loop in B based there has a unique continuous real angle lift starting at zero. To construct it, subdivide the compact parameter interval so each successive piece lies in one covering chart and choose the next branch to match the preceding endpoint; branch uniqueness follows because two lifts differ by an integer multiple of pi, locally constant and zero initially. The endpoint is m pi for a unique integer m. A based homotopy preserves m: lift the homotopy by the same overlapping-chart construction on a finite rectangular subdivision of its compact parameter square; the lifted terminal value is continuous and lies in the discrete set pi Z, so it is constant.

Every m is attained by the loop u->exp(i m pi u) modulo real scaling. Two lifted loops with the same endpoints are homotopic relative endpoints by linear interpolation of their real angle lifts; projecting gives a based homotopy. Concatenation adds endpoint angle displacements. Therefore
\[
\pi_1(B,\ell_0)\cong\mathbb Z,\qquad[\gamma]\longmapsto\frac{\widetilde\gamma(1)}{\pi}.
\]
The displayed division retains the original pi period. Lifting further to P shows that the ray returns to itself precisely for even m; for odd m it returns to the opposite ray. Thus the actual covering's monodromy is m->m mod 2. A full turn has angle 2pi and count two; it is not identified with zero count.

This derives integer winding from the source covering geometry rather than only naming a stalk T^Z. It still uses that covering geometry; its existence is not derived from a bare point alone. Reflection of source angles theta->-theta reverses m and preserves its parity.

In the other source, arXiv:2609.00299v1, keep the full generic group
\[
G=\langle T,J\mid TJ=JT,\ J^4=1\rangle,quad\epsilon=J^2,
\quad A(T)=\epsilon T^{-1},\quad A(J)=J^{-1}.
\]
Keep its finite-order subgroup H=<J> and the map q:G->L=G/H. Set t=q(T). The map from the just-computed fundamental group to L sends a loop of lifted angle m pi to t^m. It is a group isomorphism by the two explicit infinite cyclic descriptions. It sends ray-return parity to the source-derived observation delta(t^m)=epsilon^m. It also intertwines angle reflection with the induced action t^m->t^(-m). On G itself the sign epsilon^m remains in A(T^m); the isomorphism to L does not remove the full extension from the construction. Reversing the chosen winding orientation replaces both generators by their inverses.

## P2. The prime clocks and the exact meaning of irreducible

For each n>=1, form C_n=L/[n]L, where [n](ell)=ell^n and [n]L is the subgroup of n-th powers. These are finite winding-state groups at the same supporting point eta. Choosing t writes the n distinct states as the classes of 1,t,...,t^(n-1). The step S_n multiplies by the class of t. It visits all n states and has period n.

Every subgroup of L is <t^d> for a unique d>=0, where d=0 denotes the trivial subgroup. For a nontrivial subgroup, choose the least positive exponent d present. Division with remainder shows every exponent in the subgroup is divisible by d; conversely all multiples of d occur. Hence the subgroups of C_n are precisely
\[
\langle t^d\rangle/\langle t^n\rangle,\qquad d\mid n,
\]
with n/d elements, and quotient C_d. For n>=2 this proves
\[
 n\text{ prime}\ \Longleftrightarrow\ C_n\text{ is a nontrivial simple cyclic group}
 \ \Longleftrightarrow\ C_n\text{ has no quotient with size strictly between }1\text{ and }n.
\]
This is the precise irreducibility condition. Transitivity alone does not detect primes, since every C_n is transitive under S_n.

An equivariant clock map f:C_m->C_n satisfies f(S_m x)=S_n f(x). Consequently f(t^k)=t^k f(1). It is well defined exactly when t^m=1 in C_n, that is n divides m. When this holds every choice of f(1) gives one map; all are surjective, and exactly one preserves the initial state. Thus a pointed clock isomorphism C_m->C_n exists exactly when m=n. In particular the prime clocks yield pairwise non-isomorphic objects over the same eta, but composites also yield distinguishable objects. Simplicity, not distinguishability alone, separates primes.

The original sign and branch data remain in G. The full quotient map G->C_n has kernel
\[
K_n=\langle T^n,J\rangle,
\qquad 1\to K_n\to G\to C_n\to1.
\]
Both J and epsilon are retained in that exact sequence. Taking this clock observation does not replace the full source by its quotient.

## P3. Prime degree as indecomposable winding scale

The map [n]:L->L has image [n]L and index n. Every group endomorphism of L is one of the power maps [a], because its image on t determines its values on every element. The composition law is [a][b]=[ab]. Therefore a positive degree n>1 is prime precisely when [n] cannot factor as [a][b] with a,b>1.

On the character circle Hom(L,S^1), precomposition by [n] sends z=chi(t) to z^n. It is an n-sheeted cover: every point has n distinct roots and a sufficiently short target arc has n disjoint continuous root branches. Any factorization into connected finite covers of degrees a,b has n=ab by counting the inverse images of one point. Conversely n=ab supplies the explicit factorization z->z^b->z^(ab). This proves the same prime criterion for covering degree. Degree one is invertible and degree zero is a constant map, not a finite-sheeted cover.

Scaling [n] and unit winding S are different source maps: [n](t^m)=t^(nm), whereas S(t^m)=t^(m+1). Their relation to the count is explicit and neither is an operation on eta or tau.

## P4. Euclid's orchard and the exact clock observation

The orchard uses the arithmetic count lattice Z^2. Its lattice zero is not tau; its coordinates are counts already recovered in P1. A nonzero pair (a,b) is visible when no lattice point lies on the open segment from the lattice zero to (a,b).

Put d=gcd(|a|,|b|). If d>1 then (a/d,b/d) is an interior lattice point. If d=1, Bezout gives integers r,s with ra+sb=1. Any interior lattice point lambda(a,b), 0<lambda<1, would satisfy lambda=r(lambda a)+s(lambda b), hence lambda would be an integer, a contradiction. Thus visibility is equivalent to gcd(|a|,|b|)=1.

In C_n the state t^a has order n/gcd(a,n): writing a=da',n=dn' with coprime a',n', the return condition n divides ka is equivalent to n' divides k. Therefore, for 1<=a<n,
\[
(a,n)\text{ visible}\ \Longleftrightarrow\ t^a\text{ generates }C_n
\ \Longleftrightarrow\ \text{step }a\text{ visits all }n\text{ states}.
\]
The number of such a is phi(n). Every interior point of row n is visible exactly when n is prime: for a prime all 1<=a<n are coprime; for a composite n a divisor 1<d<n yields an invisible (d,n). A single visible vector need not represent a prime: (1,4) is visible. The complete-row property is the prime detector.

## P5. Reconstructing positive integers from prime divisors

Every integer n>1 has a prime divisor: its least divisor greater than one is prime, since any nontrivial factor of it would be a smaller divisor. Repeated division terminates because the positive quotient strictly decreases. Thus n is a finite product of primes. If a prime p divides ab and does not divide a, Bezout gives ua+vp=1 and multiplication by b proves p divides b. Applying this fact repeatedly to two prime factorizations matches a prime from one with a prime from the other, cancels them, and proves uniqueness by induction on the total number of factors.

Consequently the valuation map is an isomorphism of multiplicative monoids
\[
\mathbb Z_{>0}\longrightarrow\bigoplus_{p\text{ prime}}\mathbb Z_{\ge0},
\qquad n\longmapsto(v_p(n))_p,
\qquad n=\prod_p p^{v_p(n)},
\]
where multiplication on the left corresponds to componentwise addition on the right. The finite product retains every multiplicity. Integer one corresponds to the empty product. Integer zero is not represented by a finite prime product; negative integers require the additional sign. Nothing here identifies any of these with eta or tau.

Observing only the support {p:p divides n} loses multiplicities, as 2 and 4 demonstrate. Observing the full valuations does not. The full integer ring recovered as End(L) also retains addition. Prime factorization alone describes its positive multiplicative monoid and must not silently substitute for the ring structure.

Geometrically, Spec End(L) has one closed point for each positive prime and also the generic zero prime. Composite n is not a new prime point; its arithmetic is retained in the quotient End(L)/n End(L), whose prime-power factors and nilpotent elements are not discarded. This uses the ring and prime-ideal classification already proved in W3–W4, rather than declaring every distinct clock a new prime.

## P6. All prime-clock readings distinguish every winding count

There is a second, stronger meaning of prime observation than just divisor support. Define
\[
\mathcal R:L\longrightarrow\prod_{p\text{ prime}} C_p,
\qquad\mathcal R(\ell)=(\ell\bmod[p]L)_p.
\]
This homomorphism is injective. If two states t^m and t^n have equal images, every prime divides m-n. A nonzero integer has only finitely many positive divisors, whereas there are infinitely many primes: given any finite list, a prime divisor of their product plus one is absent from the list. Hence m-n=0.

For a finite set P of primes the corresponding kernel is [N]L with N=product over p in P of p. Indeed divisibility by the pairwise coprime primes is equivalent to divisibility by their product, by the Bezout argument above. Thus finite prime observations leave exactly the stated ambiguity; the all-prime map separates all integer states. The proof retains prime 2.

This map retains the full residue at each prime, not merely whether that residue is zero. It therefore can distinguish powers such as 2 and 4 even without separately reporting their valuations. No surjectivity onto the infinite product is asserted, and no completion is identified with L.

## P7. Prime character values fill the circle densely without exhausting it

The character group of C_p has the values
\[
\mu_p=\{\exp(2\pi i a/p):a=0,\ldots,p-1\}.
\]
Indeed a character is determined by its value on t, and that value must have p-th power one. Conversely every such value defines a character by t^m->exp(2pi i am/p). The full 2pi factor and the residues a are retained.

Let Gamma be the union of mu_p over all primes. It is countable, being a countable union of finite sets. It is dense in S^1: the p-th roots divide the angle into p arcs of length 2pi/p, and unbounded primes make that mesh smaller than the length of any specified open arc. It is proper: i has order four, which does not divide any prime, so i is absent. For distinct primes p,q the intersection mu_p intersect mu_q is {1}; an element in both has order dividing gcd(p,q)=1.

Thus each prime adds p-1 new character values. This is a circle of character values, not an assertion that a prime is itself a complex point or that every visible orchard ray is prime. One arbitrarily chosen point per prime would be a different construction: the choices exp(2pi i/p) accumulate only at one and do not give this dense family.

## P8. Preserve the full signed source under prime observation

Gamma alone is not invariant under all original source maps. In particular A sends the spatial character coordinate z to -z^(-1), which can have order 2p. Arbitrary sign-preserving commuting source lifts send (z,j) to (z^n j^c,j^b), with n odd, c modulo four, and b odd. The quartic branch cannot be dropped.

For every prime p retain the finite quotient
\[
G_p^{\rm full}=G/\langle T^{4p}\rangle,
\qquad |G_p^{\rm full}|=16p,
\]
with its original J, epsilon and A. The subgroup is invariant under A since A(T^(4p))=T^(-4p), and under every source lift f_(n,c,b) since f(T^(4p))=T^(4pn)J^(4pc)=T^(4pn). Prime 2 is retained, including this quotient's order-eight spatial factor. The exponent 4p is a uniform choice; no claim of minimality for p=2 is made.

Its signed characters are exactly (z,j) with z^(4p)=1 and j in {i,-i}, because epsilon must evaluate to -1 and J^2=epsilon. Define the full domain
\[
\mathcal D=\bigcup_{p\text{ prime}}\{(z,j):z^{4p}=1,\ j\in\{i,-i\}\}.
\]
For g=T^mJ^k retain the evaluation
\[
E_{\mathcal D}(g)(z,j)=z^m j^k,
\qquad E_{\mathcal D}(0)=0.
\]
It preserves multiplication and the absorbing element. Every nonabsorbing value has modulus one: both z and j are roots of unity. To prove injectivity suppose the functions for (m,k) and (m',k') agree. Taking z=1 and j=i gives k=k' modulo four. If d=m-m' is nonzero, choose a prime p not dividing d and set z=exp(2pi i/p), which belongs to mu_(4p). Then z^d is not one, a contradiction. Hence m=m', and the zero function is distinguished from each nonabsorbing function. All full source data are therefore retained.

The original source mirror acts on D by (z,j)->(-z^(-1),-j). It stays in the same p-level since (-z^(-1))^(4p)=1. Each original commuting signed lift acts by (z,j)->(z^n j^c,j^b); its spatial coordinate has 4p-th power one and its branch remains in {i,-i}. Exact equivariance is
\[
E_{\mathcal D}(f(g))(\chi)=\chi(f(g))=E_{\mathcal D}(g)(\chi\circ f).
\]
No sign, branch, or source factor was suppressed in this comparison.

The spatial values union_p mu_(4p) are still countable and dense, since they contain Gamma. They are not the full circle: a primitive ninth root has order nine, and 9 does not divide 4p for any prime p. Thus the full signed construction preserves the user's dense-but-not-exhaustive circle picture while retaining all source symmetries and still separating every integer count.

The common modulus is proved for characters of these actual finite quotients. Deligne purity concerns arithmetic Frobenius eigenvalues and retains the factor N(x)^(w/2), as derived in D1–D5 of DELIGNE_COMMON_MODULUS_AND_WINDING.md. No map identifying those eigenvalues with E_D is established here. The faithful prime-character construction is an exact result on the source data, not an RH conclusion.

## Provenance and scope

Human sources: Alain Connes and Caterina Consani, arXiv:2606.06604v1, original FF.tex Corollary luriearch, lines 1521–1580; and arXiv:2609.00299v1, original CC.tex Sections 3–4, with the exact generic group and sheaf action read in W1–W10. The prime-clock, divisor, orchard, residue and character arguments are completely derived above; no novelty claim is made. An independent mathematical agent derived P2–P4 and reviewed the all-prime separation and character construction. The first paper's original parameter tau=i log(p)/(2pi) is its modular parameter, not the user's tau; it is not used to identify a metric on the user's object.

The controlling user definitions and corrections are retained verbatim in ../TAU_DEFINITIONS_AND_CORRECTIONS_VERBATIM.md. These results do not show that existence of a point forces the source covering or Laurent direction. They derive the integers from the actual oriented-ray covering and then prove precisely which observations characterize primes and recover integer counts.


## P9. Sequential first appearances: the exact absorption sieve

This is the user's revised observation: a composite need not produce a new line. The observer records a channel at its first activation and sees later returns in that same channel. The earlier comparison of the divisor supports of 2 and 4 did not refute this proposed first-appearance observation; it concerned a different observation of an individual number.

Take the source winding progression from the chosen ordering, with one elementary step S(t^n)=t^(n+1). The state at zero winding is the initial identity in L, not eta or the absorbing monoid zero. Applying one step n times visits every state with count 0,1,...,n in order. A composite instruction S^r abbreviates those r successive steps; it does not delete their intermediate states. Each fixed finite prime is reached after finitely many steps, while there is no finite step at which all primes have been reached.

The periodic channel labelled d>=2 is the quotient clock C_d. At time n its state is t^n modulo <t^d>, and it returns to its initial state exactly when d divides n. Thus an earlier count covers a later count through this divisibility relation, not through earlier occurrence alone: 2 covers 4, but 3 does not cover 4.

Define the sequential sieve without presupposing the list of primes. Initially there are no active channels. At each integer time n>=2, let B_n be the set of previously activated d with d dividing n. If B_n is nonempty, create no new channel. If B_n is empty, activate channel n; it registers its initial return now and every subsequent multiple. This rule refers only to the retained progression and its quotient-clock return tests.

The activated counts are exactly the primes. Prove this by induction on n. At n=2 there is no earlier channel and 2 is prime. Suppose the activated counts below n are precisely the primes below n. If n is prime, it has no proper divisor d with 2<=d<n, so B_n is empty and it activates. If n is composite, its least divisor p>1 is prime and satisfies p<n; by the induction hypothesis its channel is already active, and p divides n, so n is covered and does not activate. This proves the assertion at every finite time.

Equivalently the exact first-arrival indicator is
\[
A(n)=\prod_{\substack{p<n\\p\ \mathrm{prime}}}
\left(1-\mathbf 1_{p\mid n}\right),\qquad n\ge2.
\]
The product is finite and retains all overlapping channels. It equals one precisely for a prime, and zero for a composite. The recurrence preceding the formula computes the same active set without requiring primes as prior input.

For example the successive events are: 2 activates; 3 activates; 4 is covered by 2; 5 activates; 6 is covered by both 2 and 3; 7 activates; 8 is covered by 2; 9 is covered by 3. Integer 1 is the multiplicative unit, with a one-state quotient clock and no nontrivial prime channel. It is not identified with the supporting point eta or tau.

This proves why first appearances detect exactly primes and why suppressing repeated appearances does not delete the underlying composite counts. Reconstructing composites retains the channel-composition operation and its multiplicities, as proved in P5; the activation list alone is not asserted to be a record of every state at every time. The proposition derives prime events from the source winding progression and periodic return maps. It does not yet derive that progression from an unstructured absence/presence datum, or identify this binary sieve with the analytic absorption spectrum in Connes's trace formula.

The companion interactive incidence diagram implements this recurrence for counts 1 through 48. Its equal-height channel marks mean that a channel is present; they assert no spectral weight, geometric radius from tau, or purity theorem. A finite display illustrates the proved all-n statement and is not evidence substituting for its induction proof.


## P10. Finite histories and the inductive whole

The user further proposes that ordered winding history is essential and that the whole collection of counts is obtained only through indefinite continuation. The exact construction retains the finite stages rather than positing a last infinite-time event.

In the actual source winding group take L_+={1,t,t^2,...}, selected by the chosen ordering and generated by one positive winding step. For each finite n let H_n={1,t,...,t^n}, with the order inherited from their exponents and inclusion H_n->H_(n+1). The distinctness of these states follows from P1's winding calculation, not from assigning new labels to the same parity value. Every finite history is a prefix of every later history of the same deterministic run.

The union H_infinity=union_(n>=0) H_n is exactly L_+. It has the following universal property. Given maps f_n:H_n->Y agreeing on successive overlaps, define f(t^k)=f_n(t^k) for any n>=k. Compatibility makes this independent of the chosen n, and this defines the unique map extending all f_n. Thus H_infinity is the direct limit of the finite histories. The already proved exponent correspondence identifies it with N including zero. Each individual count k belongs to H_k; no count first appears at an additional infinite-time stage. There is no largest finite H_n, since t^(n+1) is absent from H_n.

The winding step maps each history state to its successor. A composed instruction S^r represents r such steps; its mathematical prefixes remain S,S^2,...,S^r. Sequential generation does not require a storage device to retain a separate copy of every frame: the initial state, known transition rule and full count uniquely determine those prefixes. It does require retaining enough information to distinguish t^n from t^(n+2); parity alone cannot do that.

The sieve states of P9 are compatible under these same inclusions. At stage n every count from 2 through n has either activated a prime channel or returned through one already active. The union of all prime channels covers exactly the positive integers >=2: each has a least prime divisor, while the unit 1 has none. Every individual count is processed at a finite stage, and every individual prime activates at a finite stage. No finite stage contains all primes, by Euclid's proof in P6.

This gives a precise sense of internal sequential order. It does not identify the step parameter with physical time, posit a Hamiltonian, or establish that no other faithful representation of these histories exists. P6 and P8 explicitly construct other faithful encodings of the same count. The present theorem describes the generation by one winding step and its compatible finite observations.


## P11. The exact uniform infinite-observation statement

Use the full prime-clock readings, not only the binary sieve-event indicator. For a finite nonempty prime set P put M_P=product_(p in P)p. P6 proves that the fiber over the readings of an integer n is n+M_P Z. It is infinite. No finite set of those readings isolates n among all integers. Every infinite set of distinct primes does isolate it, since a nonzero difference has finitely many prime divisors. Thus the minimum cardinality of a family of prime residue observations isolating any given n is aleph_0, the same for all n.

The quantifiers are important: for every finite P there is some n_P different from n with the same readings, but there is no single n' different from n that has the same readings at every prime. This is an exact global-observation property. It does not prevent n from being specified in another representation, such as a finite successor history.

For the full signed source G and the character family D of P8, equality of observations at the finitely many p in P has kernel
\[
\{T^{4M_P r}:r\in\mathbb Z\}.
\]
Proof: equality with the identity at z=1,j=i forces k=0 modulo four. Equality for every z in mu_(4p) forces 4p to divide m for each p in P. The least common multiple of these 4p is 4M_P: every odd prime in P occurs once, and the power of two is four if 2 is absent and eight if 2 is present. Conversely divisibility by 4M_P makes all the stated evaluations one. Thus every fiber remains infinite at a finite observation stage, while the full family separates G by P8. This statement retains the source's four branch states and the extra two-adic factor in the chosen uniform family.

The equal aleph_0 value is an observation-complexity invariant relative to this family of finite clocks. It is not the definition of Deligne weight, an eigenvalue modulus, or a metric on tau. The following construction gives an actual common-modulus theorem from the global clock completion.

## P12. A compact global completion and its exact modulus theorem

For each finite nonempty prime set P retain the quotient
\[
G_P=G/\langle T^{4M_P}\rangle
\cong (\mathbb Z/(4M_P)\mathbb Z)\times(\mathbb Z/4\mathbb Z).
\]
The isomorphism sends T^mJ^k to (m modulo 4M_P,k modulo four), retaining both coordinates. For P contained in Q the transition G_Q->G_P reduces the first coordinate and leaves the second unchanged. All these finite groups have their discrete topologies. Define
\[
K=\varprojlim_P G_P
\]
as the space of compatible families, with the subspace topology from their product. The constraints of compatibility are closed, so K is a closed subspace of a product of finite compact spaces and is compact. Equivalently choose the cofinal sequence of sets of the first N primes; the diagonal subsequence argument proves compactness of the resulting countable product, and the compatibility equations retain a closed subset. Multiplication and inversion are coordinatewise and continuous.

The map i:G->K sends a source element to all its finite residue classes. It is injective by P11: all residues equal identity force k=0 modulo four and every 4M_P to divide m, hence m=0. It has dense image. A basic open condition specifies only finitely many quotient coordinates. Their union Q is a finite prime set; a compatible value in G_Q has a representative T^mJ^k in G, whose image satisfies all those conditions. Thus every nonempty basic open set meets i(G). This is a faithful embedding with retained finite observations, not an identification of G with its completion.

The cofinal sets P containing 2 give the more explicit full description
\[
K\cong(\mathbb Z/8\mathbb Z)\times
\prod_{p\ \mathrm{odd\ prime}}\mathbb Z/p\mathbb Z
\times(\mathbb Z/4\mathbb Z).
\]
To verify it, use 4M_P=8 times the product of the odd primes in P. The reduction map modulo these pairwise coprime factors is injective because an integer divisible by each is divisible by their product; it is surjective by Bezout's identity, constructing a representative for each finite list of residues. These finite isomorphisms commute with every transition, so taking compatible families gives the displayed isomorphism. The final factor remains the source J-branch. The first factor comes from the chosen uniform 4p observation family, including p=2; it is not declared a minimal completion.

All original source symmetries used above extend continuously. At a finite level, the source mirror is
\[
A_P(m,k)=(-m,2m-k),
\]
where the first coordinate is modulo 4M_P and the second modulo four. This is well defined because 4 divides 4M_P. It is a homomorphism of order two and it commutes with reductions. Hence it induces A_K on K. Each sign-preserving commuting lift has finite formula
\[
f_{n,c,b;P}(m,k)=(nm,cm+bk),
\qquad n,b\text{ odd},\quad c\pmod4,
\]
with the same respective moduli. This is well defined, continuous and compatible with transitions, so it extends to K as well. No source sign is removed by the extension.

Now let chi:K->C^times be a continuous group character. Its image is a compact subgroup of C^times because K is compact. The modulus image is therefore a compact subgroup of R_(>0). Such a subgroup is {1}: if it contains r>1 then the powers r^n are unbounded, contrary to compactness; if it contains 0<r<1 then it contains r^(-1)>1. Consequently
\[
\boxed{|\chi(x)|=1\quad\text{for every }x\in K.}
\]
This is the common-modulus theorem for the constructed global clock completion. It follows from compactness and the multiplicative character law. It neither measures a distance from eta nor assigns infinite modulus to source elements.

The continuous characters can also be classified without an extra hypothesis. Consider the open arc V={exp(i theta): |theta|<pi/3}. It contains no nontrivial subgroup of S^1. Indeed, if a nonidentity value already lies outside V it is excluded; if it is exp(i theta) with 0<|theta|<pi/3, the power with exponent ceil(pi/(3|theta|)) has an angle between pi/3 and 2pi/3 in absolute value and lies outside V. Continuity gives an identity neighborhood in K whose image lies in V. Some kernel N_P of K->G_P is contained in that neighborhood, since finite quotient conditions form a neighborhood basis. Its character image is a subgroup contained in V, hence trivial. Thus chi factors through G_P.

Conversely every character of a finite G_P pulls back to a continuous character of K. The source signed condition chi(epsilon)=-1 requires j=chi(J) in {i,-i}. Its restriction to G therefore has exactly the original formula
\[
\chi(T^mJ^k)=z^m j^k,
\qquad z^{4M_P}=1\text{ for some finite }P,
\qquad j\in\{i,-i\}.
\]
All original factors are retained. These signed characters separate K: at a finite quotient where two elements differ, their branch difference is detected with z=1,j=i when that difference is nonzero modulo four; otherwise a character z detecting the distinct first residues, with j=i, separates them. Thus the global completion and every original winding state are faithfully observable by this continuous signed character family.

This construction also identifies the exact continuity obstruction for original source characters not in this family. The original character chi_(2,i)(T^mJ^k)=2^m i^k is valid on the uncompleted G. Along a cofinal sequence P_N, the source elements T^(4M_(P_N)) converge to identity in K, because every fixed finite quotient eventually sends them to identity. Their chi_(2,i) values are 2^(4M_(P_N)), which do not converge to one. That character cannot extend continuously to K. The full original character space is retained in the record; the map of continuous characters of K into it is a proved inclusion, not a replacement obtained by rescaling values.

There are consequently two distinct proved statements: every original winding state requires infinitely many unrestricted prime-clock observations to isolate it in this observation topology; and every continuous character of the compact global clock completion has modulus one. The second follows through the explicit topology and group structure, not by renaming the first statement as purity. Deligne weight w is the arithmetic eigenvalue relation |iota alpha|=N(x)^(w/2), with its full residue-norm factor. No identification of these clock characters with the required arithmetic cohomology has been supplied by the completion theorem.


## P13. Retaining all stacked prime powers

The intermediate completion K in P12 is faithful on the original group G but is not the completion of all winding clocks. At an odd prime p its spatial factor is F_p. Multiplication by p, and multiplication by p^r for any r>=1, both have the same zero image on that factor and are invertible at every other prime factor. Their spatial image index is p in K, not p^r. Thus the intermediate observer does not preserve every covering-degree multiplicity after completion. This defect does not identify source integers, but it matters to the user's stacking operation.

Retain all finite clock quotients instead. For each positive integer N put
\[
\widetilde G_N=G/\langle T^{4N}\rangle
\cong\mathbb Z/(4N)\mathbb Z\times\mathbb Z/4\mathbb Z.
\]
For N dividing M use reduction modulo 4N in the first coordinate and retain the branch coordinate. Define
\[
\widehat G=\varprojlim_{N\mid M}\widetilde G_N.
\]
The moduli 4N are cofinal among all positive integer moduli: every modulus d divides 4d. A coherent family at moduli 4N therefore extends uniquely to all moduli by reduction, and restriction gives its inverse. Hence
\[
\boxed{\widehat G\cong\widehat{\mathbb Z}\times\mathbb Z/4\mathbb Z,
\qquad\widehat{\mathbb Z}=\varprojlim_N\mathbb Z/N\mathbb Z.}
\]
The space is compact by the same finite-product and closed-compatibility proof as P12. The source map T^mJ^k -> ((m mod N)_N,k) is injective: a nonzero integer m cannot be divisible by every positive N. Its image is dense because every basic finite compatible residue prescription reduces to one prescription modulo the least common multiple and has an integer representative. The absorbing zero is retained separately as an isolated absorbing point; it is neither the group identity nor the supporting eta.

Prime factorization and the same finite Bezout construction identify the spatial completion with product_p Z_p, where Z_p=lim_r Z/p^r Z. Every modulus involves finitely many prime powers; finite compatibility constructs its residue from those components. Conversely the residue family restricts to every prime-power chain. Thus all p^r information, including the entire prime-two chain, is retained.

The original source involution and all the classified commuting signed maps extend continuously:
\[
\widehat A(x,k)=(-x,\,2(x\bmod4)-k),
\qquad
\widehat f_{n,c,b}(x,k)=(nx,\,c(x\bmod4)+bk),
\]
with n,b odd and second coordinate modulo four. These formulas descend at every modulus 4N and commute with the transition maps, so are well defined. They restrict to the original source formulas. The earlier completion K is a quotient of this one: retain x modulo eight, x modulo each odd prime, and k modulo four. This projection records exactly which higher prime-power coordinates that intermediate observer omitted; it does not replace the full completion.

For any positive n, multiplication by n on Zhat is injective and has image equal to the kernel of reduction modulo n. Here is a direct proof without an exactness assumption about inverse limits. If nx=0, inspect its coordinate modulo nm for an arbitrary positive m. A representative a of x modulo nm satisfies nm divides na, hence m divides a. Its reduction x modulo m is zero; all coordinates are therefore zero. Conversely, if x modulo n is zero, choose a representative a of x modulo nm divisible by n, and define y modulo m to be a/n modulo m. This is independent of representative, since changing a by nm changes a/n by m. Compatibility of the x coordinates makes these y coordinates compatible. They define y in Zhat with ny=x. Thus
\[
\widehat{\mathbb Z}/n\widehat{\mathbb Z}\cong\mathbb Z/n\mathbb Z,
\qquad [\widehat{\mathbb Z}:n\widehat{\mathbb Z}]=n.
\]
In particular the degree p^r retains its exact index p^r. For a signed source lift with odd nonzero n and odd b, injectivity follows from injectivity of multiplication by n and invertibility of b modulo four. Its image has exactly the condition x in n Zhat; once the unique preimage of x is chosen, the branch equation can be solved uniquely for k. Thus its image index is |n|. The winding map at n=2 also exists and retains index two; this does not remove W5's obstruction to a sign-preserving equivariant lift of even degree on the full source.

Every continuous character of Ghat still has modulus one by compactness, with the complete proof in P12 applying unchanged. Every such character factors through some finite quotient, by the no-small-subgroup arc argument. The continuous signed characters restrict to the original G as
\[
\chi_{z,j}(T^mJ^k)=z^m j^k,
\qquad z\text{ any root of unity},\quad j\in\{i,-i\}.
\]
Every root of unity occurs since its finite order divides 4N for some N. Conversely the finite quotient relation forces that order condition. These signed characters separate Ghat by the finite-coordinate proof, and separate all original source elements. The character values are a dense proper subset of the unit circle, with all prime powers now retained.

This gives a compact global object carrying the entire sequence of finite clock observations, faithfully retaining original integers and preserving winding-cover degrees. Its character-modulus theorem is proved. It is not an identification of Ghat with Spec Z, nor a construction of the arithmetic cohomology whose eigenvalues enter Deligne purity.

## P14. The exact degree factor in the clock operators

### P14.1. Measure and change of variables

Write K_w=Zhat for the winding factor of the full group Ghat=Zhat x C_4 in P13. Every variable in the following integrals belongs to K_w, not to tau. Retain a finite nonzero translation-invariant Haar measure mu with arbitrary total mass h=mu(K_w)>0. Its measure on a residue class modulo M is h/M: the M classes partition K_w and translations permute them. These assignments are compatible with refinement, since each class modulo M is a disjoint union of M'/M classes modulo M' when M divides M'. They describe the measure directly on every finite clock. No choice h=1 or rescaling of operators is made.

For a positive integer n, P13 proves that multiplication phi_n(x)=nx is injective, with clopen image nK_w of index n. It is a homeomorphism from K_w onto nK_w, since a continuous bijection from a compact space to a Hausdorff space has continuous inverse. Division x/n is used only on nK_w. Each of its n cosets has measure h/n. The measures (phi_n)_*mu and n mu restricted to nK_w are translation invariant on that subgroup and both have mass h. Uniqueness of Haar measure at specified mass gives
\[
\int_{K_w}F(nx)\,d\mu(x)=n\int_{nK_w}F(y)\,d\mu(y).
\tag{P14.1}
\]
This identity holds for nonnegative measurable F and for integrable complex F. It can also be checked first on each residue-class cylinder using the class measures h/M, then extended to nonnegative measurable functions by the measure extension and monotone convergence theorems. It implies mu(nE)=mu(E)/n and mu(phi_n^{-1}(E))=n mu(E intersect nK_w). Thus both image and inverse image preserve null sets, including for the completed measure.

### P14.2. Unrescaled operators and adjoints

Let H=L^2(K_w,mu), with inner product linear in its first entry, and define
\[
(U_nf)(x)=f(nx),\qquad
(V_nf)(x)=\begin{cases}f(x/n),&x\in nK_w,\\0,&x\notin nK_w.\end{cases}
\tag{P14.2}
\]
The null-set statement proves these maps are well defined on almost-everywhere equivalence classes. Formula P14.1 gives
\[
\|U_nf\|^2=n\int_{nK_w}|f(y)|^2\,d\mu(y),\qquad
\|V_nf\|^2=\frac1n\int_{K_w}|f(y)|^2\,d\mu(y).
\tag{P14.3}
\]
In particular both operators are bounded. The second equality gives norm(V_n)=1/sqrt(n). The first gives norm(U_n)<=sqrt(n), and equality follows by taking f=1_(nK_w): its squared norm is h/n while U_nf=1_(K_w) has squared norm h. Thus every factor is retained:
\[
\|U_n\|=\sqrt n,\qquad\|V_n\|=\frac1{\sqrt n}.
\tag{P14.4}
\]
For f,g in H, change variables y=nx through P14.1 to obtain
\[
\begin{aligned}
\langle U_nf,g\rangle
&=\int_{K_w}f(nx)\overline{g(x)}\,d\mu(x)\\
&=n\int_{nK_w}f(y)\overline{g(y/n)}\,d\mu(y)
=\langle f,nV_ng\rangle.
\end{aligned}
\]
Cauchy--Schwarz and P14.3 justify these integrals. Hence U_n^*=nV_n and V_n^*=U_n/n. With P_n multiplication by the indicator of nK_w, direct evaluation yields U_nV_n=I and V_nU_n=P_n, and consequently
\[
\boxed{U_nU_n^*=nI,\quad U_n^*U_n=nP_n,\quad
V_n^*V_n=\frac1nI,\quad V_nV_n^*=\frac1nP_n.}
\tag{P14.5}
\]

### P14.3. These factors already occur in the finite clocks

For every positive M give H_M=C^(Z/MZ) the inner product
\[
\langle F,G\rangle_M=\frac hM\sum_{a\bmod M}F(a)\overline{G(a)}.
\tag{P14.6}
\]
The pullback J_M F=F composed with reduction rho_M embeds it isometrically into H, by the measured residue classes above. Define maps with their different domains retained:
\[
u_{n,M}:H_{nM}\to H_M,\quad (u_{n,M}F)(a)=F(na),
\]
\[
v_{n,M}:H_M\to H_{nM},\quad
(v_{n,M}G)(b)=\begin{cases}G(b/n),& n\mid b,\\0,&n\nmid b.\end{cases}
\tag{P14.7}
\]
The map a mod M -> na mod nM is injective with image the residues divisible by n; its inverse there is division by n modulo M. Therefore the displayed formulas are well defined. Their adjoint calculation is
\[
\begin{aligned}
\langle u_{n,M}F,G\rangle_M
&=\frac hM\sum_{a\bmod M}F(na)\overline{G(a)}\\
&=\frac h{nM}\sum_{b\bmod nM}F(b)
\overline{n\mathbf1_{n\mid b}G(b/n)}
=\langle F,nv_{n,M}G\rangle_{nM}.
\end{aligned}
\tag{P14.8}
\]
Thus u_(n,M)^*=n v_(n,M). Also uv=I and vu is multiplication by the divisibility indicator. The completed and finite maps intertwine exactly:
\[
U_nJ_{nM}=J_Mu_{n,M},\qquad V_nJ_M=J_{nM}v_{n,M}.
\tag{P14.9}
\]
The factor n is therefore already forced by finite quotient arithmetic and the two class measures h/M and h/(nM). The construction has not inserted it by choosing an eigenvalue or changing scale.

### P14.4. Composition retains multiplication and common divisors

For positive m,n, evaluating at x gives
\[
U_mU_n=U_{mn}=U_nU_m,\qquad
V_mV_n=V_{mn}=V_nV_m.
\tag{P14.10}
\]
The first equality is f(nmx). For the second the support conditions are x in mK_w and x/m in nK_w, equivalently x in mnK_w; on that set unique division gives (x/m)/n=x/(mn).

There is a more informative mixed relation. Let d=gcd(m,n), a=m/d, b=n/d. Injectivity of multiplication by d proves mx in nK_w iff ax in bK_w. Since a,b are coprime, choose integers r,s with ra+sb=1. If ax in bK_w then x=r(ax)+s(bx) is in bK_w; the converse is immediate. On this support x=by gives mx/n=ay. Therefore
\[
\boxed{U_mV_n=V_{n/d}U_{m/d},\qquad d=\gcd(m,n).}
\tag{P14.11}
\]
The coprime case is U_mV_n=V_nU_m; the common divisor has not been discarded.

### P14.5. Operator modulus and eigenvalue modulus

P14.5 gives the exact positive operator square root
\[
|U_n|=(U_n^*U_n)^{1/2}=\sqrt n\,P_n.
\tag{P14.12}
\]
The equality follows because P_n is a self-adjoint projection, so the nonnegative operator sqrt(n) P_n squares to nP_n. For n>1, P_n and I-P_n are nonzero: their supports have positive measures h/n and h-h/n. Thus U_n^*U_n=nP_n differs from U_nU_n^*=nI, and U_n is not normal.

The same operator has the exact eigenvector
\[
U_n\mathbf1_{K_w}=\mathbf1_{K_w},\qquad
\|\mathbf1_{K_w}\|^2=h.
\tag{P14.13}
\]
For n>1 its eigenvalue 1 has modulus different from sqrt(n). Hence P14.12 is an operator-modulus result; it does not make every eigenvalue have modulus sqrt(n). This statement concerns the constructed operator on its stated full function space. It makes no assertion that another arithmetic cohomological realization or a derived sector cannot have pure weight. No such realization is constructed here. Continuous characters have squared norm h, since their pointwise modulus is one by P13.

### P14.6. The full signed source is retained

Keep the entire Ghat=K_w x C_4, with its original A and sign epsilon, rather than replacing it by K_w. Define its translation-invariant measure by
\[
\int_{\widehat G}F(x,k)\,d\widetilde\mu(x,k)
=\frac14\sum_{k\bmod4}\int_{K_w}F(x,k)\,d\mu(x).
\tag{P14.14}
\]
Its total mass remains h and every branch has mass h/4. Pullback by the winding projection pi(x,k)=x is isometric because the four terms and the factor 1/4 cancel explicitly in the squared norm. This is a retained comparison map, not an identification of the two spaces.

For a positive odd n, c modulo four, and odd b, the original source map F=f_(n,c,b) from P13 is an injective homomorphism onto nK_w x C_4 of index n. Its inverse there is explicitly
\[
F^{-1}(y,l)=\left(y/n,\ b^{-1}\bigl(l-c((y/n)\bmod4)\bigr)\right),
\tag{P14.15}
\]
where b inverse is taken modulo four. Define U_F f=f composed with F and V_F f as f composed with F inverse on its image and zero elsewhere. The same Haar argument, now on the full signed group and its index-n image, gives U_F^*=n V_F and all four relations in P14.5 with the image projection P_F. Every branch and its measure remain present. Moreover pi composed with F=[n] composed with pi, so
\[
U_F\pi^*=\pi^*U_n,\qquad V_F\pi^*=\pi^*V_n.
\tag{P14.16}
\]
These identities follow by evaluating inside and outside the image. Winding degree two retains index two on K_w; this does not assert an even-degree sign-preserving map commuting with A on Ghat, whose obstruction was proved in W5.

### P14.7. What the global construction establishes

The exact chain now proved is: finite clock residues have infinite ambiguity on integer counts (P11); their compatible completion is compact and retains all prime powers and the original signed data (P12–P13); its continuous characters have modulus one (P12–P13); and its arithmetic degree-n maps have index n and the unrescaled adjoint factor n, with operator modulus sqrt(n) on the image sector (P14). These are maps and identities of the original source-derived winding data. Neither the shared countable observation requirement nor the operator modulus is being substituted for Deligne's arithmetic Frobenius eigenvalue relation. P14 was independently derived and its complete finite and infinite computations are recorded here.

