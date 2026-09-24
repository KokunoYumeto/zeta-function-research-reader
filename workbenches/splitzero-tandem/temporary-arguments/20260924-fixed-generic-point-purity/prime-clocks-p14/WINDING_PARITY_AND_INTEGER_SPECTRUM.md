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
