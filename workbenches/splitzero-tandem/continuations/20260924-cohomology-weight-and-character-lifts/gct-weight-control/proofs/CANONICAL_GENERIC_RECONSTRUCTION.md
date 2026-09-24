# The unique common support and canonical reconstruction of the original zeta function

24 September 2026. Proof labels CG1–CG8. This calculation receives the user's uniqueness argument: the complete counting structure, its global arithmetic unit, the parityless common support, and recovery of the original zeta must be considered together. The proposed consequence about a common spectral weight is retained as the next part of that argument; it is not substituted into the hypotheses of this proof.

The exact statement proved here is this: **the full generic datum in the specified Connes–Consani diagram canonically determines an integer ring, its complete normed prime spectrum, and the original Riemann zeta function. Both ordered-chart constructions factor uniquely through the same generic group completion. The supporting point of that common overlap is unique.** The identity operation is the arithmetic unit; the supporting point is not that operation.

The user notation is \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Here the absence of \(Z_2\) means the proved absence of an exchange-equivariant even/odd point-label. The quotient stack still has a \(C_2\) stabilizer at its generic point. No addition, subtraction, numerical distance, midpoint, vector or coordinate is assigned to \(\tau\). All algebra below is on the explicitly stated monoids, groups, endomorphisms or functions.

## Source and complete proof dependencies

The original author source is Alain Connes and Caterina Consani, [The Absolute Twistor Line and the Geometry of the compactified Spec Z, arXiv:2609.00299v1](https://arxiv.org/html/2609.00299v1), local `CC.tex`, SHA-256 `57a10dcef5cd758e6b2f1c54b1c0a11b0fb093638f74fb1be515ec3bc7080ba4`. Original passages actually read: lines 499–505 (topology), 526–540 (ordered charts and common group), 576–600 (imaginary generator and twisted restrictions), 773–847 (involution and chart compatibility), 881–898 (invariants and isotropy). We use the unfolded generic stalk throughout; passing to invariant sections would be a different operation.

The source curve and its full periods are read in Connes–Consani [arXiv:2606.06604v1](https://arxiv.org/html/2606.06604v1), author `FF.tex` lines 1550–1633, SHA-256 `14c17a95040be7bfc57bb5f87e58907a05cacd0bcb1b6967b2892cf3d9bc1229`.

The companion `TIMED_PRIME_PERIOD_DERIVATION.md`, TP0–TP14, contains full proofs of the clock recurrence, prime factorization, convolution coefficients and all analytic convergence assertions used below. It is appended without alteration in `CANONICAL_GENERIC_RECONSTRUCTION_FULL.md`. Thus the combined proof does not replace these arguments by a reference to a result name. The earlier winding calculation W1–W4 is restated with complete maps in CG1–CG6.

## CG0. Begin with the complete winding history and derive its one-step generator

The complete positive chart supplied by CC is \(M_+\) in CG2, including all four finite-order units \(H_+=\langle J_+\rangle\). Retain it and form the quotient monoid \(P_+=M_+/H_+\). From the original source relations, every element of \(P_+\) is a nonnegative power of \(u=q_+(T)\), with distinct powers. This statement concerns the whole source chart: identifying a finite observed prefix with part of it does not certify that every future event will obey its law.

Here is the requested contradiction argument **on the same complete history**. Let \(v\) be another positive one-step generator of \(P_+\): requiring that it is a generator means that its successive iterates account for the whole monoid without an additional missing class. Since \(u\) and \(v\) both generate that same whole monoid, there are positive iteration counts \(a,b\) with
\[
v=u^a,\qquad u=v^b.
\]
Neither count is zero, since a generator is not the identity. Substitution gives
\[
u=u^{ab}.
\]
Distinct powers in the source chart imply \(ab=1\). Positive iteration counts therefore give \(a=b=1\), whence \(u=v\). Two different complete one-step generators are impossible. The numerical names \(a,b\) count compositions in this proof; no observed prime has been prelabelled two or three to manufacture the unit.

The same generator is characterized without a chosen spelling: it is the unique element of \(P_+\) different from the identity that is not the product of two elements different from the identity. The generator has this property because positive exponents cannot add to one, while every larger exponent splits into one and its predecessor. Thus the whole monoid determines its primitive step.

The negative chart gives its own forward generator \(q_-(T^{-1})\). The exact embeddings into the group quotient are
\[
j_\pm:P_\pm\hookrightarrow L,\qquad
j_\pm(q_\pm(m))=q(\rho_\pm(m)).
\]
They are well defined since chart units map into \(H\). They are injective since equality after \(q\) means equal winding exponent, and the remaining difference is precisely a chart unit. Under these maps the images of the two forward generators are inverses in \(L\), so a numerical orientation has not been made intrinsic. The intrinsic arithmetic one is instead \(\operatorname{id}_L\), as CG4 proves. To connect these two meanings exactly, define
\[
\mathrm{ev}_u:R_+\longrightarrow P_+,\qquad
f\longmapsto j_+^{-1}\bigl(f(j_+(u))\bigr).
\]
The classification in CG4 proves that \(f(j_+(u))\) belongs to the image of \(j_+\), so the displayed inverse is applied on its domain. It also proves this evaluation is a bijection and satisfies \(\mathrm{ev}_u(f\oplus g)=\mathrm{ev}_u(f)\mathrm{ev}_u(g)\), and \(\mathrm{ev}_u(\mathbf1_R)=u\). For \(u_-=q_-(T^{-1})\), the exact negative-chart formula is \(f\mapsto j_-^{-1}(f(j_-(u_-)))\), justified by the same classification. The same arithmetic identity thus supplies either oriented step, with the actual inversion comparison retained.

This establishes uniqueness from the *complete specified counting structure*. Completeness by itself, with no event-composition law, does not assert that a primitive generator exists. Here existence comes from the actual full CC chart, and uniqueness is derived by the contradiction above. No additional existence assumption has been substituted for that source calculation.

## CG1. Unique support of the common unordered localization

The actual unfolded space is
\[
X=\{+,-,\eta\},\qquad
\Omega_+=\{+,\eta\},\quad
\Omega_-=\{-,\eta\},\quad
\Omega=\Omega_+\cap\Omega_-=\{\eta\}.
\]
Its opens are the empty set, these three sets, and \(X\). The involution \(\alpha\) interchanges \(+\) and \(-\). A homeomorphism fixes \(\eta\): the singleton \(\{\eta\}\) is the unique dense singleton, since the other two points are closed. Therefore
\[
\operatorname{Fix}(\alpha)=\{\eta\}.
\tag{CG1.1}
\]

There is a direct contradiction proof of the requested common-support uniqueness. If \(x\ne y\) were two points belonging to both ordered charts, then
\[
x,y\in\Omega_+\cap\Omega_-=\{\eta\}
\]
would imply \(x=\eta=y\), contradicting \(x\ne y\). This proves uniqueness of the specified supporting role. It uses the whole chart diagram, not a numerical coordinate or a midpoint construction.

Let \(Q_2=\{\mathrm{even},\mathrm{odd}\}\), with exchange \(\iota\). An equivariant point-label on an invariant subset satisfies \(P(\alpha x)=\iota(P(x))\). At \(\eta\), this would imply \(P(\eta)=\iota(P(\eta))\), impossible because \(\iota\) fixes neither label. On the other two points the rule is possible, by assigning either label at \(+\) and the other at \(-\). Thus the supporting \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\) is identified with \(\eta\) in this role by a proved obstruction. This does not mean its stalk is empty or that its isotropy is trivial.

## CG2. The complete signed data and both localization maps

At the nonabsorbing monomial level retain
\[
G=\langle T,J,\epsilon:\ TJ=JT,\ T\epsilon=\epsilon T,
J\epsilon=\epsilon J,\ J^2=\epsilon,\ \epsilon^2=1\rangle.
\tag{CG2.1}
\]
The separate source absorbing element is retained outside this group. The two charts have monomials
\[
M_+=\{T^mJ_+^k:m\ge0,\ k\bmod4\},\qquad
M_-=\{T^mJ_-^k:m\le0,\ k\bmod4\},
\]
with the same fourth-order unit relations. Their actual restrictions are
\[
\rho_+(T^mJ_+^k)=T^mJ^k,\qquad
\rho_-(T^mJ_-^k)=T^m(\epsilon J)^k.
\tag{CG2.2}
\]

The map \(T\mapsto(1,\bar0), J\mapsto(0,\bar1),\epsilon\mapsto(0,\bar2)\) gives \(G\cong\mathbb Z\times C_4\). Its inverse is \((m,\bar k)\mapsto T^mJ^k\): it is well defined because \(J^4=1\), respects the operations, and the two composites fix the generators. These integer coordinates prove the classification of the already specified source; they are not inferred from two prelabelled observed event times.

In these coordinates \(\rho_+\) preserves \((m,k)\), while \(\rho_-\) sends \((m,k)\) to \((m,3k)\). Since multiplication by three permutes \(C_4\), both maps are injective. Their image intersection is exactly the four units \(H=\langle J\rangle\).

The whole \(G\) is the group completion of either chart, with its stated restriction. For \(M_+\), a homomorphism \(f:M_+\to K\) into an abelian group extends necessarily and sufficiently by
\[
\widetilde f(T^mJ^k)=f(T)^m f(J_+)^k,
\qquad m\in\mathbb Z,\ k\bmod4.
\tag{CG2.3}
\]
The formula is well defined since \(f(J_+)^4=1\); it is a group homomorphism and agrees with \(f\). Uniqueness follows because \(T,J\) generate \(G\).

For \(M_-\), let \(U=T^{-1}\). The unique extension obeys
\[
\widetilde f(T)=f(U)^{-1},\qquad
\widetilde f(J)=f(J_-)^3.
\tag{CG2.4}
\]
Indeed \(\rho_-(J_-)=J^3\) and \((J^3)^3=J\), so this formula makes \(\widetilde f(\rho_-(J_-))=f(J_-)^9=f(J_-)\). The remaining generator and relation checks follow immediately by multiplication and the fourth-order relation. This proves existence and uniqueness on the negative chart with its source twist retained.

The universal completion is itself unique **with its chart map**: if \((G',\rho'_+)\) also realizes this property, there are unique extensions \(u:G\to G'\) and \(v:G'\to G\) preserving the chart maps. Both \(vu\) and the identity of \(G\) extend \(\rho_+\), hence are equal by the proved uniqueness. Likewise \(uv=\operatorname{id}_{G'}\). Thus the comparison is an isomorphism and is unique subject to its chart map. This is the precise mathematical meaning of reconstructing the same complete chart data in another presentation.

## CG3. Parity follows from the signed involution; all winding remains

The original action is
\[
A(T)=\epsilon T^{-1},\qquad A(J)=\epsilon J=J^{-1},\qquad A(\epsilon)=\epsilon.
\]
For every \(g=T^mJ^k\),
\[
A(g)=\epsilon^mT^{-m}J^{-k}=T^{-m}J^{2m-k},
\qquad
gA(g)=T^mJ^k\epsilon^mT^{-m}J^{-k}=\epsilon^m.
\tag{CG3.1}
\]
Applying the coordinate action twice gives \((m,k)\mapsto(-m,2m-k)\mapsto(m,k)\), so it is an involution.

The finite-order subgroup of \(G\) is exactly \(H=\langle J\rangle\). A nonzero exponent of \(T\) cannot become zero upon taking a nonzero power; all four \(J\)-states have finite order. Retain the full exact sequence
\[
1\longrightarrow H\longrightarrow G\xrightarrow{q}L:=G/H\longrightarrow1.
\tag{CG3.2}
\]
The quotient is infinite cyclic. The mirror induces inversion on it. Because \(hA(h)=1\) for every \(h\in H\), (CG3.1) descends to the surjection
\[
\delta:L\longrightarrow\{1,\epsilon\},\qquad
\delta(q(g))=gA(g),\qquad
\delta(q(T^mJ^k))=\epsilon^m.
\tag{CG3.3}
\]
It is a homomorphism since \(G\) is abelian. Its kernel is the subgroup of squares of \(L\). Equivalently, the kernel before passage through \(q\) is \(\langle T^2,J\rangle\). This derives the even/odd observation from the full involution. The retained object is the exact sequence and its map, not only its two-state image.

The user's winding history corresponds to the unbounded exponent in \(L\). It is different from the finite-order subgroup \(H\). Neither the identity of \(L\) nor any of its elements is identified with the supporting point.

## CG4. The global arithmetic unit, without choosing observed prime labels

**Receiver scope, clarified after the full timing derivation:** this section computes endomorphisms of the explicitly retained quotient L=G/H. It does not identify that ring with endomorphisms of the full signed sheaf preserving J, epsilon and its parity observation. On L, [n] sends the parity of a winding to n times that parity modulo two. Consequently only odd [n] preserve the parity observation identically; these are closed under composition but not addition. The full G, H, quotient map and parity observation remain in CG3. In addition, cyclicity of L comes from the displayed source chart, not from a proof that uncalibrated timing must yield that chart. GLOBAL_TIMING_QUOTIENT_INDEPENDENT.md GTQ1–GTQ8 and FIXED_SUPPORT_AND_ODD_REFINEMENT.md OR1–OR8 give the complete calculation of that earlier step and its obstruction.

Construct \(R=\operatorname{End}_{\mathrm{Ab}}(L)\), with
\[
(f\oplus g)(x)=f(x)g(x),\qquad (f\odot g)(x)=f(g(x)).
\tag{CG4.1}
\]
The pointwise product is a homomorphism because \(L\) is abelian. Its additive zero is \(x\mapsto1_L\), and its additive inverse sends \(x\) to \(f(x)^{-1}\). Associativity and commutativity of addition follow pointwise. Composition is associative. The homomorphism law proves left distributivity; evaluating a pointwise product at \(g(x)\) proves right distributivity. Thus this is a unital ring with
\[
\mathbf1_R=\operatorname{id}_L.
\tag{CG4.2}
\]

Here is the exact unit contradiction, using no prime names. If \(e,e'\in R\) were two distinct two-sided multiplicative identities, then
\[
e\odot e'=e'\quad\text{because }e\text{ is an identity},\qquad
e\odot e'=e\quad\text{because }e'\text{ is an identity}.
\]
Hence \(e=e'\), a contradiction. These are operations on endomorphisms; they assert no operation on \(\tau\).

Choose a generator \(t\) of \(L\) temporarily to classify this ring. Any endomorphism has \(f(t)=t^n\) for a unique \(n\in\mathbb Z\); then \(f(t^m)=t^{nm}\). Conversely every power map \([n]:x\mapsto x^n\) is a homomorphism. Consequently
\[
\iota:\mathbb Z\xrightarrow{\sim}R,\quad n\mapsto[n],\quad
[a]\oplus[b]=[a+b],\quad[a]\odot[b]=[ab].
\tag{CG4.3}
\]
The classification is independent of choosing \(t\) or \(t^{-1}\): the exponent of \(f(t^{-1})\) relative to \(t^{-1}\) is still \(n\). Thus the entire ring and its identity are orientation-independent.

Let \(R_+\) be the additive submonoid generated by \(\mathbf1_R\), including its zero. Its elements are distinct and correspond exactly to nonnegative integers under (CG4.3). Among its nonzero elements, \(\mathbf1_R\) is the unique universal divisor: it divides every element by composition, while an element dividing every nonzero element must divide \(\mathbf1_R\). Its positive degree \(a\) then has a positive degree partner \(b\) with \(ab=1\), forcing \(a=b=1\). This proves the user's “global quotient one” property in its precise divisibility sense on the constructed arithmetic.

The argument starts with the complete \(L\). It does not certify from a finite event record that the source has already been identified correctly. In the user's unrestricted late-event observation problem, a finite record can have incompatible full lattice extensions, as proved in GO3. That observational result and this construction from the specified complete source have different inputs.

## CG5. The full prime spectrum and its norms are canonical

For completeness, the prime ideals of \(\mathbb Z\) are \((0)\) and \((p)\) for positive prime integers \(p\). A nonzero ideal contains a least positive integer \(d\); division with remainder proves it is \(d\mathbb Z\). A composite \(d=ab\), with \(1<a,b<d\), makes that ideal nonprime. For prime \(p\), Euclid's lemma proves primality; TP6 supplies its full proof by the terminating Euclidean algorithm and Bezout identity. The zero ideal is prime because a product of two nonzero integers is nonzero.

The isomorphism (CG4.3) transports all these ideals and products exactly. It induces
\[
\operatorname{Spec}R\xrightarrow{\sim}\operatorname{Spec}\mathbb Z,
\quad\mathfrak p\mapsto\iota^{-1}(\mathfrak p).
\tag{CG5.1}
\]
The inverse is the image of an ideal under \(\iota\). Membership in \(D([n])\) corresponds to membership in \(D(n)\), proving that both directions are continuous. The maps of basic-open section rings are
\[
\mathbb Z[1/n]\xrightarrow{\sim}R[1/[n]],\qquad
a/n^k\longmapsto[a]/[n]^k.
\tag{CG5.2}
\]
Cross multiplication proves that the formula respects representatives; applying \(\iota^{-1}\) gives its inverse. They commute with every localization restriction. Thus the comparison includes the structure sheaf, not merely the list of primes.

For \(\mathfrak p_p=([p])\), the residue field and its exact norm are
\[
R/\mathfrak p_p\cong\mathbb F_p,\qquad
N(\mathfrak p_p)=p=|L/[p]L|.
\tag{CG5.3}
\]
The latter quotient has representatives \(1_L,t,\ldots,t^{p-1}\), by division of the exponent. They are distinct because two exponents in this range cannot differ by a nonzero multiple of \(p\). Every prime is retained, including two.

The generic point \((0)\in\operatorname{Spec}R\) is the unique generic point of this derived spectrum. It is a prime ideal of \(R\). The point \(\eta\in X\) is the supporting point in the source geometry. Their roles are connected by the construction (CG3.2)–(CG5.1); they are not silently identified as objects of the same space.

## CG6. Uniqueness of the complete arithmetic reconstruction

Let \(u:G\to G'\) be an isomorphism comparing two presentations of the full source, as in CG2. Every finite-order element is sent to a finite-order element, and applying \(u^{-1}\) proves equality of these subgroups. Thus \(u\) induces an isomorphism \(\bar u:L\to L'\). The induced map of rings is exactly
\[
R\xrightarrow{\sim}R',\qquad f\mapsto\bar u\circ f\circ\bar u^{-1}.
\tag{CG6.1}
\]
It preserves pointwise addition by the homomorphism law, composition by cancellation of \(\bar u^{-1}\bar u\), and the identity by direct substitution. It preserves every power map because \(\bar u(x^n)=\bar u(x)^n\). Therefore it preserves every element of \(R_+\), every prime ideal and every residue norm in CG5. It also preserves all quotient clocks: \(x\bmod[p]L\mapsto\bar u(x)\bmod[p]L'\) is a well-defined bijection.

In particular, the two ordered charts in CG2 yield exactly the same normed spectrum through their common localization. Every homomorphism from either chart into an abelian group factors uniquely through its indicated map to \(G\); killing the finite-order subgroup then factors uniquely through \(L\). The second statement applies to torsion-free targets: any image of \(H\) there is trivial, since it has finite order. This proves the claimed universal factorization with all its domains stated.

There are three levels of uniqueness, all retained here: the common point in the specified topological diagram is unique; group completion is unique with its chart map, up to unique isomorphism; the arithmetic identity and every power map are canonical under that isomorphism. The bare identity equation alone does not prove the first two levels. For example both actual ordered charts already have the same identity section, and both localization maps preserve it, despite their being distinct charts. The stronger common-support and completion requirements are the parts of the user's argument that select the one diagrammatic role proved in CG1–CG2.

## CG7. The original zeta function follows from the whole normed spectrum

For each recovered prime norm \(p\), the source curve is \(E_p=\mathbb C^\times/p^{\mathbb Z}\). Its flow \([z]\mapsto[e^t z]\) returns exactly when \(t\in(\log p)\mathbb Z\), because \(e^t z=p^kz\) is equivalent to \(t=k\log p\). The original differential has both periods \(\log p\) and \(2\pi i\), as proved in TP7. These are coordinates on the curves and their flow; no distance from \(\tau\) is defined.

Retain all positive returns and the complete count measure:
\[
\mathcal R=\sum_p\sum_{k\ge1}\frac1k\delta_{k\log p},\qquad
\mathcal D=\delta_0+\sum_{n\ge2}\delta_{\log n},\qquad
\mathcal W=\sum_p\sum_{k\ge1}(\log p)\delta_{k\log p}.
\tag{CG7.1}
\]
TP9 proves local finiteness; TP10 proves, including every convolution coefficient,
\[
\mathcal D=\exp_*\mathcal R,
\qquad\mathcal W=t\mathcal R.
\tag{CG7.2}
\]
The empty convolution has the atom \(\delta_0\), corresponding to arithmetic one. This atom is retained in all comparisons.

Since CG6 preserves every prime norm, it preserves each term of (CG7.1) with its repetition number and coefficient. Hence the measures are uniquely determined by the full source and independent of its ordered presentation. The exact Laplace transforms, with the absolute and locally uniform convergence proved in TP12–TP13, are
\[
\boxed{\int_{[0,\infty)}e^{-st}\,d\mathcal D(t)
=1+\sum_{n\ge2}n^{-s}=\zeta(s),\qquad\Re s>1,}
\tag{CG7.3}
\]
\[
\exp\left(\int e^{-st}\,d\mathcal R(t)\right)=\zeta(s),\qquad
\int e^{-st}\,d\mathcal W(t)=-\frac{\zeta'(s)}{\zeta(s)}.
\tag{CG7.4}
\]
The function here is the original zeta. No completion multiplier or rescaling replaces it. The measures include prime two and every positive repetition. Negative-time returns exist in the whole flow but are not positive integers in the original Dirichlet series; this domain comparison is proved in TP13.

This also gives a contradiction proof of uniqueness of the resulting analytic function: two functions reconstructed from the same normed spectrum have the same absolutely convergent series (CG7.3) at every point of \(\Re s>1\), so cannot differ there. If they have meromorphic continuations to the same connected domain, those continuations coincide. To verify the latter uniqueness, their difference is meromorphic and vanishes on an open set. Away from its discrete poles the analytic identity theorem makes it zero on the connected punctured domain; every apparent pole is then removable with zero extension. Existence of the original zeta continuation is not asserted to follow solely from abstract meromorphic uniqueness.

## CG8. Exact content of the composed claim

The constructed chain is
\[
(\eta,\mathcal O_\eta,A;\rho_+,\rho_-)
\longmapsto(G,H,L,\delta)
\longmapsto(R,\mathbf1_R,R_+)
\longmapsto(\operatorname{Spec}R,N)
\longmapsto(\mathcal R,\mathcal D,\mathcal W)
\longmapsto\zeta(s)\quad(\Re s>1).
\tag{CG8.1}
\]
Every arrow has been constructed above or in the complete appended TP proof. The full supporting datum is retained; \(G\to L\) is an explicit quotient within the exact sequence, not permission to erase \(H\) or its signed action.

The “only” established here is the unique common supporting point and the universal factorization of both chart reconstructions through its complete generic localization. It is not a classification of every possible arithmetic geometry by the existence of one unit. The full cyclic stalk, both chart maps and the signed involution are mathematical input supplied by the actual CC construction. The unit does not by itself recover those inputs.

The user's further argument concerns whether this complete, uniquely specified reconstruction forces a common arithmetic spectral weight and therefore the required purity. This proof supplies its actual original-zeta receiving map. It proves no modulus statement for the zeros by replacing that question with the uniqueness just established. That weight calculation remains part of the ongoing programme.
