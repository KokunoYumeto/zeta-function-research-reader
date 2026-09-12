# Historical pre-Boolean branches and KMS continuation — 12 September 2026

This bounded source-first continuation reads the next mathematical responses in the distinct SSD edition `corpus:SSD-downloads\ChatGPT-Globalization Semiring Analysis (5).md`. It does not repeat the earlier ghost or Hurwitz work. The source has1087073bytes and26958lines, SHA256 `8d1780a24df3bb31db981b5e437558de31e6d94bf21bb54103a0a336d6a73091`.

## 1. Complete response coverage and the actual comparison

The following complete mathematical answer bodies were read, with their boundaries extended past the initially suggested endpoint26090 where needed:

| Original inclusive lines | Response as exported | Complete mathematical body |
|---|---|---|
|23137–23956|7/6/2026,12:23:35PM; response heading23104|Pre-Boolean support, prime filters, split characters, principal support intervals, Haar/Dirac states.|
|24426–25052|7/6/2026,7:57:51PM; heading24423|The intervening proposed proper-class reset, universal-class argument and localization comparison.|
|25162–25715|7/6/2026,7:58:41PM; heading25058|Lattice branch maps, nonunital halo embedding, split arithmetic quotient, transitive barycenter proof.|
|25754–26221|7/6/2026,10:01:27PM; heading25721|Final pointfree-frame version, complete-prime branches, claimed arithmetic branch theorem, finite-lattice argument.|
|26524–26958|7/6/2026,10:47:59PM; heading26521|Final KMS abstract/BC/CM/BCM response, read and independently audited in the delegated KMS lane.|

The mathematical answer bodies, rather than their preceding drafting text, define this coverage. The precise original-byte excerpts and hashes are in `output/split_zero_rh_tandem_2026-09-12/sources/historical/next_responses/PROVENANCE.json`. This covers the specified bodies in one distinct edition, not all25 distinct editions from the previous family inventory.

The core comparison was read directly from `corpus:Chatnotes\split_zero_projective_monads_surcomplex\split_support_geometry_arithmetic_curve_v11.tex`, SHA256 `5fa6a55aa9d1a2e57599e206087d3d2466b25dd99fa1a90d5f86367aafab1b4d`:

- Lines1772–2054 already contain the prime-filter bijection, the support-branch semiring quotient, its arithmetic spectrum map, and the Haar/Dirac stabilizer theorem with proofs. These are **not newly discovered absent theorems**.
- Core lines2001–2018 explicitly require arbitrary-join preservation for locale points. This is more precise than the first transcript response's assertion at23530–23550 that arbitrary ordinary lattice characters of a sober space are its points.
- The later transcript's Theorem6.1, lines25982–26020, incorrectly identifies every ordinary semiring map `G_L(R)→G(R)` fixing amplitudes with a frame point. Semiring maps preserve finite sums; they do not automatically preserve arbitrary joins in the zero fibre. Its Corollary6.2 consequently rules out too many algebraic branch maps. The original frame carrier and its lack of frame points can be retained through the exact comparison proved below.
- Core lines5006–5096 and5346–5378 already construct adelic measure-algebra support and its product-formula defect. The detailed proof calls the measure algebra a Boolean **sigma-algebra**; treating it as a complete frame additionally requires the relevant completeness/localizability hypotheses. The concrete probability-measure example below proves completeness directly and imposes no unstated hypothesis on all adelic curves.
- The intermediate proper-class response proves the familiar absence of a bijection from a set onto the universal class in NBG/MK, but supplies no arithmetic morphism establishing its further asserted 'shadow' relationship to the terminal semiring. It is a historical competing interpretation, not an input to the present arithmetic comparison. We preserve its source separately and import no unsupported equivalence between the proposed interpretations.

## 2. Exact ordinary and continuous Split-Zero branches

The results below are stated in classical set theory. The ultrafilter construction explicitly uses Zorn's lemma. No claim about existence or nonexistence of points in a constructive foundation is inferred from that use of choice; such an internal comparison would also have to specify its truth-value object and its available joins.

Let `R` be a nonzero commutative ring and let `L` be a nontrivial bounded distributive lattice. Retain the source carrier and all its exceptional coordinates:

\[
G_L(R)=\{(0,\lambda):\lambda\in L\}\cup\{(r,1_L):r\in R\}\subseteq R\times L,
\]

\[
(r,\lambda)+(s,\mu)=(r+s,\lambda\vee\mu),\qquad
(r,\lambda)(s,\mu)=(rs,\lambda\wedge\mu),
\]

\[
\tau_L=(0,0_L),\qquad e_L=(0,1_L),\qquad1=(1_R,1_L).
\]

Write `G(R)={τ} disjointunion R^bullet`, with supported zero `e=0_R^bullet` distinct from global zero `τ`. No product `R×L` outside this exact subset is silently admitted.

**Theorem B1 — all ordinary amplitude-fixed branches.** There is a natural bijection

\[
\operatorname{Hom}_{\mathrm{DLat}_{0,1}}(L,\mathbb B)
\xrightarrow{\sim}
\{\beta:G_L(R)\to G(R)\text{ unital semiring map}:\beta(r,1_L)=r^\bullet\}.
\tag{B1}
\]

It sends `ε` to

\[
\beta_\epsilon(r,1_L)=r^\bullet,\qquad
\beta_\epsilon(0,\lambda)=
\begin{cases}\tau&\epsilon(\lambda)=0,\\ e&\epsilon(\lambda)=1.\end{cases}
\tag{B2}
\]

The map is surjective as a semiring map; its exact kernel congruence is equality of amplitudes together with equality of selected support values:

\[
(r,\lambda)\sim_\epsilon(s,\mu)
\iff r=s\ \text{and}\ \epsilon(\lambda)=\epsilon(\mu).
\tag{B3}
\]

**Proof.** The source formulas agree at `(0,1_L)` since `ε(1_L)=1`. They preserve zero and unit. On the zero fibre, preservation of addition and multiplication is precisely preservation of join and meet. If one argument has nonzero amplitude, its lattice coordinate is `1_L`; adding a zero-fibre argument leaves it unchanged and multiplying by that argument gives `(0,λ)`, matching respectively addition by `τ` or `e`, and multiplication by `τ` or `e` in `G(R)`. With both arguments at full support, even if their sum or product cancels to amplitude zero, both outputs are supported and ring identities prove preservation. This verifies all exceptional products and cancellations.

Conversely, `(0,λ)` is additively idempotent. The only additive idempotents of `G(R)` are `τ` and `e`: a supported `r^bullet+r^bullet=r^bullet` implies `2r=r` in the ring, hence `r=0`. Therefore every amplitude-fixed `β` sends the zero fibre into `{τ,e}`. Identifying this two-element subsemiring with `B` gives a map `ε` preserving bottom, top, meet and join. Formula(B2) reconstructs `β`; both constructions are inverse. Every amplitude and `τ` occurs in the image, and inspecting(B2) gives exactly(B3). ∎

Now let `L` be a frame: all joins exist and finite meets distribute over arbitrary joins. Its zero fibre has specified infinitary joins

\[
\bigvee_{i\in I}^{\rm fib}(0,\lambda_i)=(0,\bigvee_{i\in I}\lambda_i).
\]

**Theorem B2 — exactly the continuous branches.** Under(B1), the subset of branches preserving all these zero-fibre joins is exactly

\[
\operatorname{Hom}_{\mathrm{Frm}}(L,\mathbb B).
\tag{B4}
\]

Indeed the corresponding equality for(B2) says exactly `ε(∨λ_i)=∨ε(λ_i)`, and finite meets are already preserved. This is the precise additional structure required by the transcript's final frame formulation. Its ordinary algebraic maps retain a larger, explicitly identified category.

The classification extends to every map between original lattice-split carriers. For commutative unital rings `R,A` and nontrivial bounded distributive lattices `L,M`,

\[
\operatorname{Hom}_{\mathrm{Semi}}(G_L(R),G_M(A))
\cong\operatorname{Hom}_{\mathrm{Ring}}(R,A)
\times\operatorname{Hom}_{\mathrm{DLat}_{0,1}}(L,M).
\tag{B5}
\]

The pair `(h,f)` gives `(r,λ)↦(h(r),f(λ))`. Conversely an arbitrary semiring map sends each additively idempotent `z_λ` to amplitude zero, say `z_(f(λ))`; this preserves finite joins, meets and bottom. The identity `e_L=(1_R,1_L)+(−1_R,1_L)` makes its image have top support, because one summand is the target unit; additive idempotence makes its amplitude zero. Thus `e_L↦e_M` and `f` preserves top. Now `(r,1_L)+e_L=(r,1_L)` forces its image to have top support. Write that image `(h(r),1_M)`. The supported operations give a unital ring map `h`, and the formulas recover every source element, consistently at `e_L`. Coordinate composition proves naturality and both inverse constructions. In particular the entire two-factor datum is recoverable from the semiring map; scalar amplitude and support are not freely interchanged.

## 3. The exact frame comparison retaining all ordinary branches

For the underlying bounded distributive lattice of a frame `L`, let `Idl(L)` be the set of lattice ideals. An ideal is a nonempty lower set closed under finite joins. Its bottom is `{0_L}`, its top is `L`, its finite meet is intersection, and the join of a family of ideals is

\[
\bigvee_\alpha I_\alpha=
\{x\in L:x\le y_1\vee\cdots\vee y_n
\text{ for some finite }n\ge0,\ y_j\in\bigcup_\alpha I_\alpha\}.
\tag{I1}
\]

The empty finite join is `0_L`; this retains the bottom ideal in every formula.

**Theorem I1 — frame quotient and principal-ideal section.** The maps

\[
q:\operatorname{Idl}(L)\to L,\quad I\mapsto\bigvee I,
\qquad\eta:L\to\operatorname{Idl}(L),\quad\lambda\mapsto\downarrow\lambda
\tag{I2}
\]

have the following exact properties:

1. `Idl(L)` is a frame and `q` is a surjective frame homomorphism.
2. `η` is an injective bounded-lattice homomorphism, `qη=id_L`, and
   `q(I)≤λ iff I⊆η(λ)`.
3. The kernel congruence of `q` is exactly `I~J iff ∨I=∨J`. No claim that `η` preserves arbitrary joins is made.

**Proof.** Formula(I1) is an ideal and is the least ideal containing every `I_α`; intersections give infima. To prove frame distributivity, let `x∈I∩∨_αJ_α`. Choose `x≤y_1∨...∨y_n` with `y_j∈J_{α_j}`. In the distributive lattice,

\[
x=x\wedge(y_1\vee\cdots\vee y_n)
=(x\wedge y_1)\vee\cdots\vee(x\wedge y_n).
\]

Each `x∧y_j` belongs to `I∩J_{α_j}`, proving `I∩∨J_α⊆∨(I∩J_α)`; the reverse inclusion follows from containment. Thus `Idl(L)` is a frame.

The supremum of the right side of(I1) equals `∨_α∨I_α`, proving arbitrary-join preservation by `q`, including the empty family. Since `L` is a frame,

\[
(\bigvee I)\wedge(\bigvee J)
=\bigvee_{i\in I,j\in J}(i\wedge j)
=\bigvee(I\cap J).
\]

The last equality holds because each `i∧j` is in the intersection, and each `x∈I∩J` is the term `x∧x`. Hence `q` preserves finite meets and the top. Principal ideals satisfy `↓λ∩↓μ=↓(λ∧μ)` and `↓λ∨↓μ=↓(λ∨μ)`; they also preserve bottom/top. Their suprema are the original elements, proving `qη=id`, injectivity and surjectivity. The adjunction equivalence and the kernel description follow immediately from the definition of supremum. ∎

**Theorem I2 — all algebraic branches become frame points before the quotient.** There are mutually inverse bijections

\[
\operatorname{Hom}_{\mathrm{DLat}_{0,1}}(L,\mathbb B)
\cong\operatorname{Hom}_{\mathrm{Frm}}(\operatorname{Idl}(L),\mathbb B),
\tag{I3}
\]

given by

\[
\widehat\epsilon(I)=\bigvee_{\lambda\in I}\epsilon(\lambda)
\quad\text{and}\quad\epsilon=\widehat\epsilon\eta.
\tag{I4}
\]

A frame point `εhat` in(I3) factors through `q` if and only if its original `ε` is a frame point of `L`. Thus the exact inclusion of point sets is

\[
q^*:\operatorname{Pt}(L)\hookrightarrow\operatorname{Pt}(\operatorname{Idl}(L)),
\quad\epsilon\mapsto\epsilon q,
\tag{I5}
\]

and its image is the points constant on the kernel congruence in TheoremI1.

**Proof.** In(I4), the value is1 precisely when the ideal meets the prime filter `ε^(-1)(1)`. For a join of ideals, a value1 is witnessed by an element below a finite join of source elements; finite primeness then gives an element of value1 in one of those source ideals. The reverse implication follows by containment, proving arbitrary-join preservation. For intersections, if `I` and `J` each have a value1 element `i,j`, their meet `i∧j∈I∩J` has value1; the reverse implication is immediate. Top and bottom follow from `ε(1)=1`, `ε(0)=0`. Therefore `εhat` is a frame homomorphism.

Every ideal is the join in `Idl(L)` of its principal ideals, so an arbitrary frame point is completely determined by its restriction along `η`, giving both inverse identities. If `ε` preserves arbitrary joins, `εhat(I)=ε(∨I)=εq(I)`. Conversely if `εhat=χq` for a frame map `χ`, then `ε=εhat η=χqη=χ`, so `ε` is a frame map. A set map constant on the fibres of surjective `q` factors uniquely; if that map is a frame map, the induced factor preserves arbitrary joins and finite meets by lifting families through `q`. This proves the final image claim. ∎

**Theorem I3 — original Split-Zero comparison and exact congruence.** Every bounded-lattice map `f:L→M` induces

\[
G_f(R):G_L(R)\to G_M(R),\quad (r,\lambda)\mapsto(r,f(\lambda)).
\tag{I6}
\]

For the nontrivial frames in TheoremI1 this gives a split pair of unital semiring maps

\[
G_L(R)\xrightarrow{G_\eta(R)}G_{\operatorname{Idl}(L)}(R)
\xrightarrow{G_q(R)}G_L(R),\qquad G_qG_\eta=\mathrm{id}.
\tag{I7}
\]

They preserve `τ` and supported `e` as distinct elements. The exact kernel of `G_q(R)` consists of equal amplitudes and equal suprema of zero-fibre ideals:

\[
(r,I)\sim(s,J)\iff r=s\text{ and }\bigvee I=\bigvee J.
\tag{I8}
\]

**Proof.** A nonzero amplitude in `G_L(R)` has full support and maps to full support because `f(1_L)=1_M`; hence(I6) lands in the exact target carrier. Finite join and meet preservation establish the semiring identities coordinate by coordinate, including zero-amplitude cancellation. Formula(I7) follows from `qη=id`, and(I8) is equality of the two coordinates of the image. The bottom and top of the nontrivial source and target lattices differ; their images under these bounded maps are again bottom and top, proving the exact zero statements. ∎

Thus an ordinary branch which fails zero-fibre join continuity is a fully explicit frame point **upstairs**, and the arithmetic map fails to descend through a proved frame quotient **downstairs**. The original support object and all its algebraic branches remain related by the maps(I2)–(I8).

The two available lifts have an exact comparison, which prevents a split algebra map from being mistaken for a split frame map. Given an ordinary `ε:L→𝔹`, both

\[
\epsilon q:\operatorname{Idl}(L)\to\mathbb B,
\qquad\widehat\epsilon:\operatorname{Idl}(L)\to\mathbb B
\tag{I9}
\]

are bounded-lattice maps and agree on every principal ideal. The first descends through `q` by definition; the second preserves arbitrary joins by TheoremI2. They coincide on all ideals exactly when `ε` preserves arbitrary joins. The forward implication follows because `εq=εhat` and surjectivity of the frame map `q` force its factor `ε` to preserve joins; the converse is(I4). This also yields two amplitude-fixed Split-Zero branch maps out of `G_Idl(L)(R)`, with exactly the same criterion for equality.

There is a further exact localic structure. The map `j=ηq` is a nucleus on `Idl(L)`: it is monotone, `I⊆j(I)` because each `i∈I` lies below `∨I`, it satisfies `j²=j` because `qη=id`, and it preserves finite meets because both `q` and `η` do. Its fixed ideals are exactly the principal ideals. Their inherited meet and nucleus-applied join

\[
\bigvee^{\mathrm{fix}}_\alpha\downarrow\lambda_\alpha
=j\left(\bigvee^{\operatorname{Idl}(L)}_\alpha\downarrow\lambda_\alpha\right)
=\downarrow\left(\bigvee^L_\alpha\lambda_\alpha\right)
\tag{I10}
\]

identify the fixed-point frame exactly with the original `L`. This proves the quotient/sub-locale correspondence at the level of operations, while retaining the precise failure of `η` to preserve the ambient ideal-frame joins.

## 4. A fully explicit nontrivial frame with algebraic branches and no frame points

Let `L` be the Lebesgue probability measure algebra of `[0,1]`: measurable subsets modulo null symmetric difference. Write `[A]` for the class of `A`, keep the original measure `μ(A)`, and use union, intersection and complement for finite Boolean operations.

**Lemma M1 — completeness and atomlessness.** This `L` is a complete Boolean algebra, hence a frame, and has no atoms.

**Proof.** For an arbitrary family `([A_i])_(i∈I)`, let

\[
b=\sup\{\mu(A_{i_1}\cup\cdots\cup A_{i_n}):n\ge0\}.
\]

Choose finite unions `F_n` with measures tending to `b`, and put `B=∪_nF_n`. Replacing `F_n` by the union of the first `n` such finite unions makes them increasing without changing their defining kind, so `μ(B)=b`. For each original `A_i`, the finite-union supremum bounds `μ(F_n∪A_i)≤b`, and continuity from below gives `μ(B∪A_i)≤b=μ(B)`. Thus `A_i\B` is null. If `[C]` is another upper bound, every one of the countably many constituent sets in `B` is contained in `C` modulo a null set; hence `B\C` is null. This proves that `[B]` is the supremum. Infima follow by complements.

In a complete Boolean algebra finite meets distribute over arbitrary joins: if `v=∨_i(a∧b_i)`, then every `b_i≤¬a∨v`; taking joins and intersecting with `a` gives `a∧∨b_i≤v`. The reverse inequality is immediate. Thus `L` is a frame.

For a nonzero `[A]`, the function `F(t)=μ(A∩[0,t])` is continuous because `|F(t)−F(u)|≤|t−u|`. It takes the values0 andμ(A)>0 at the endpoints. There is therefore `t` with `F(t)=μ(A)/2`. The class of `A∩[0,t]` is strictly between0 and[A], so no nonzero class is an atom. ∎

**Theorem M2 — exact frame points of a complete Boolean algebra.** If `B` is any complete Boolean algebra, its frame points correspond bijectively to its atoms:

\[
\operatorname{Hom}_{\mathrm{Frm}}(B,\mathbb B)
\cong\operatorname{At}(B),\qquad
a\longmapsto\epsilon_a(b)=\mathbf1_{\{a\le b\}}.
\tag{M1}
\]

**Proof.** An atom below `∨b_i` lies below some `b_i`: otherwise every `a∧b_i=0`, while frame distributivity gives `a=a∧∨b_i=∨(a∧b_i)=0`, a contradiction. Thus `ε_a` preserves arbitrary joins. It preserves finite meets, top and bottom directly.

Conversely, a frame map `ε:B→𝔹` into the two-element Boolean algebra preserves complements, since complements are characterized by their finite meet0 and join1. By De Morgan it therefore also preserves arbitrary meets. Put `a=∧{b:ε(b)=1}`. Its image is1, so `a≠0`. If `0<c≤a` and `ε(c)=0`, then `ε(¬c)=1`, forcing `a≤¬c` and hence `c=0`, a contradiction. Consequently `ε(c)=1`, which by definition of `a` implies `a≤c`. Thus `a` is an atom. Every element of the filter contains `a`; conversely if `a≤b`, then `ε(b)=1`. This proves the inverse formulas and their uniqueness. ∎

In the last proof the symbol for the codomain is the two-element Boolean algebra `mathbb B`; the domain is the specified complete Boolean algebra. In particular the measure algebra of LemmaM1 has **no frame points**.

It nevertheless has ordinary lattice characters. Here is an explicit witnessed failure of the required continuity. Let `D_n=[0,2^{-n}]` as original measurable subsets of `[0,1]`; their classes are nonzero and any finite intersection is the smallest selected `D_n`. The filter generated by these classes is proper. Order proper filters containing it by inclusion; the union of every chain is proper, so Zorn's lemma gives a maximal proper filter `F`. In a Boolean algebra, maximal proper filters contain exactly one of `b,¬b`: if neither lay in `F`, adjoining `b` would produce0, so some `f∈F` satisfies `f∧b=0` and hence `f≤¬b`, which already puts `¬b∈F`. Its characteristic function is therefore a bounded-lattice homomorphism `ε_F:L→mathbb B`.

Every `ε_F([D_n])=1`, while every `ε_F([D_n^c])=0`. But

\[
\bigvee_{n\ge1}[D_n^c]=[[0,1]\setminus\{0\}]=1_L,
\quad\epsilon_F(1_L)=1\ne\bigvee_{n\ge1}0=0.
\tag{M2}
\]

Thus(B2) gives an actual surjective semiring branch `β_(ε_F):G_L(R)→G(R)` preserving amplitudes, even though the frame has no point. Formula(M2) gives its exact failed zero-fibre join equation. The point `εhat_F` of `Idl(L)` does not descend through `q`. More explicitly, set

\[
J=\bigvee_{n\ge1}^{\operatorname{Idl}(L)}\downarrow[D_n^c].
\]

Then `q(J)=1_L=q(L)`, but `εhat_F(J)=0` and `εhat_F(L)=1`. This is an explicit pair in the kernel congruence of `q` distinguished by the upstairs point; it proves the obstruction to descent at an exact source/target pair.

In fact **every** ordinary branch on this measure algebra fails already countable-join preservation. For its ultrafilter `F`, start at `a_0=1`. Split a representative of `a_n` into two equal-measure pieces by the continuous cumulative-measure construction in LemmaM1. Exactly one of their classes belongs to `F`; call it `a_(n+1)`. The resulting decreasing sequence satisfies `a_n∈F` and `μ(a_n)=2^(−n)`. Its infimum is0 by continuity of measure. Consequently `b_n=¬a_n` increases to1 and each `ε_F(b_n)=0`, again contradicting countable-join preservation. The ideal `I=union_n↓b_n` then satisfies `q(I)=q(L)=1`, `εhat_F(I)=0`, and `εhat_F(L)=1`. This gives a kernel-congruence witness for each individual algebraic branch, not merely for the displayed dyadic choice.

## 5. Atomic observation and the exact support data it removes

For a complete Boolean algebra `B`, put

\[
b_{\mathrm{at}}=\bigvee_{a\in\operatorname{At}(B)}a,\qquad
b_{\mathrm{na}}=\neg b_{\mathrm{at}}.
\]

The frame-point evaluation map is

\[
\operatorname{ev}:B\to\mathcal P(\operatorname{At}(B)),\qquad
x\mapsto\{a:a\le x\}.
\tag{A1}
\]

**Theorem A1 — exact atomic quotient.** This is a surjective complete Boolean-algebra homomorphism. Its kernel congruence is

\[
\operatorname{ev}(x)=\operatorname{ev}(y)
\iff x\wedge b_{\mathrm{at}}=y\wedge b_{\mathrm{at}},
\tag{A2}
\]

and its inverse image of the empty set is the full principal ideal `↓b_na`. The complete decomposition retaining that ideal is

\[
B\xrightarrow{\sim}(\downarrow b_{\mathrm{at}})\times(\downarrow b_{\mathrm{na}}),
\quad x\mapsto(x\wedge b_{\mathrm{at}},x\wedge b_{\mathrm{na}}),
\tag{A3}
\]

with inverse `(u,v)↦u∨v` and respective local units `b_at,b_na`.

**Proof.** Each coordinate of(A1) is the frame point in(M1), so it preserves arbitrary joins and finite meets. Complements are preserved because an atom lies below exactly one of `x,¬x`. For any subset `S` of atoms, the element `∨_(a∈S)a` maps exactly to `S`, by pairwise disjointness of distinct atoms and the arbitrary-join argument in(M1). Thus evaluation is surjective. Distributivity gives `x∧b_at=∨_(a atom)(x∧a)=∨_(a≤x)a`, which proves(A2) and the empty-fibre claim. The two complementary components in(A3) reconstruct `x` by distributivity, and disjointness of `b_at,b_na` proves both inverse identities and preservation of complete Boolean operations. ∎

The complement on either local Boolean factor `↓b` in(A3) is explicitly `u↦b∧¬u`; its local top is `b`, not the global top of `B` unless `b=1`.

This supplies an exact relation to the source's adelic measure-algebra support. In a finite measure-algebra realization, frame-point evaluation detects precisely its measure atoms;(A3) retains the entire nonatomic component rather than treating lack of points as lack of support. For a discrete countable measure with positive measure at each singleton, the singleton classes are the atoms and `b_at=1`; evaluation is an isomorphism to the power set of the original places. For the Lebesgue example, `b_at=0`, `b_na=1`, and every frame-point evaluation is absent while the entire nontrivial Boolean carrier persists.

When applying `G_(ev)(R)`, retain the exceptional case: if there are no atoms, `P(Atoms(B))` is the one-element lattice, so the exact carrier `G_(P(empty))(R)` is isomorphic to `R`, and this quotient identifies `τ_B` and `e_B` with ordinary zero. It is the explicit ring-reflection map on this observation, not evidence that `τ_B=e_B` in the original carrier. The split comparison(I7) has nontrivial lattices on both sides and preserves them as distinct; it remains available when the point-observation quotient collapses them.

Concretely, `Ψ:G_(1-lattice)(R)→R`, `(r,*)↦r`, is bijective and preserves both operations because the unique support coordinate is fixed. In the atomless case its composition is the exact identity

\[
\Psi\circ G_{\mathrm{ev}}(R)=p_B:G_B(R)\to R,
\quad p_B(r,\lambda)=r.
\tag{A4}
\]

## 5a. The exact operator-algebraic branch map

The core manuscript's `L^infty` realization permits an additional precise bridge to state spaces. Work with the same finite probability measure space, complete measure algebra `B`, and the complex algebra `M=L^infty(Ω,μ;C)` equipped with essential-supremum norm and complex conjugation. The original measure and every atomic mass are retained.

**Theorem O1 — all Boolean branches extend exactly to multiplicative states.** There is a natural bijection

\[
\operatorname{Hom}_{\mathrm{DLat}_{0,1}}(B,\mathbb B)
\cong\{\chi:M\to\mathbb C:\chi\text{ is a unital complex-linear }*\text{-homomorphism}\}.
\tag{O1}
\]

The correspondence is specified on every projection by

\[
\chi_\epsilon(\mathbf1_A)=\epsilon([A]),
\tag{O2}
\]

and on arbitrary `f∈M` by the uniform extension of this finite formula:

\[
\chi_\epsilon\left(\sum_{j=1}^n c_j\mathbf1_{A_j}\right)
=\sum_{j=1}^n c_j\epsilon([A_j]),
\tag{O3}
\]

where the `A_j` form the specified measurable partition of `Ω` modulo null sets. Every such `χ` is positive and has norm1.

**Proof.** Exactly one member of a finite partition has `ε`-value1: finite-join preservation gives at least one, and pairwise disjointness with meet preservation gives at most one. Thus(O3) selects one of the original values `c_j`. Refining two partitions by all intersections shows the formula is independent of the simple-function presentation. The unique selected intersection gives additivity and multiplicativity for two simple functions, while conjugating their values gives star preservation. The selected value has modulus at most the essential supremum of the simple function, so the map is contractive.

Every bounded measurable complex function has simple functions tending to it in essential-supremum norm: partition a square containing its essential range into finitely many squares of diameter at most `2^(−n)` and use one original value in each nonempty square. The resulting evaluations are Cauchy by contractivity. Their limit defines a unique continuous extension independent of the approximating sequence. Addition, multiplication and conjugation commute with these uniform limits, proving the required homomorphism identities. Positivity follows from `f=g* g` with `g=√f` for every nonnegative measurable `f`; hence `χ(f)=|χ(g)|²≥0`. Contractivity and `χ(1)=1` prove norm1.

Conversely a unital star homomorphism sends projections to real idempotents0 or1. Since `1_(A∩B)=1_A1_B` and `1_(A∪B)=1_A+1_B−1_(A∩B)`, its projection values form the required Boolean lattice map. It is contractive because `||f||_infty²1−f*f` is the square of a bounded measurable function, so positivity gives `|χ(f)|²≤||f||_infty²`. It agrees with(O3) on simple functions, and continuity forces equality on all of `M`. This proves both inverse constructions. ∎

**Theorem O2 — normal branches, exact atomic masses, and failure of normality.** For the correspondence(O1), the following are equivalent:

1. `χ` preserves suprema of bounded increasing nets of nonnegative elements of `M` (normality).
2. `ε` is a frame point of the complete measure algebra.
3. There is a measure atom `a` such that
   \[
   \chi(f)=\frac{1}{\mu(a)}\int_a f\,d\mu\qquad(f\in M).
   \tag{O4}
   \]

In particular the atomless Lebesgue example has multiplicative states for all of its ordinary branches, and none is normal; its exact countable failure is exhibited by(M2).

All bounded increasing nets used here have a supremum in the specified `M`. An explicit proof for nonnegative nets retains the finite measure: put `b=sup_i integral f_i`. Choose indices with integrals tending to `b`, and use directedness to replace them by an increasing dominating sequence. Choose representatives outside one common null set for the countably many sequence comparisons, so this selected sequence is pointwise increasing there. Its pointwise supremum `g` has integral `b`. For every fixed original index `i`, each finite maximum with a sequence member lies below a net member, so `integral max(g,f_i)≤b=integral g` by monotone convergence. Thus `f_i≤g` almost everywhere. Every upper bound of the original net bounds the selected sequence and hence `g`, proving that `g` is the required least upper bound.

**Proof.** The supremum in `M` of the finite-union projections from an arbitrary family `([A_i])` is the projection `1_(∨[A_i])`: LemmaM1's countable essential union is an upper bound, and its increasing finite selected unions show it is the least upper bound also among arbitrary measurable nonnegative functions. Normality applied to this increasing net therefore gives preservation of its full projection join. Together with(O2), this is precisely frame continuity of `ε`, proving1⇒2. By TheoremM2, a frame point corresponds to a unique atom `a`.

Every bounded measurable `f` is essentially constant on `a`. To see this, use the finite measurable partitions of its essential range from the proof of TheoremO1. Each partition has exactly one cell whose intersection with `a` is nonzero, and by atomhood that intersection equals `a` modulo null sets. Its diameter tends to0, so the simple approximants restrict to constants `c_n` on `a`, with `|c_n−c_m|` bounded by their uniform difference. Their limit `c` is the almost-everywhere value of `f` on `a`. Formula(O3) selects exactly these constants and gives `χ(f)=c`; integration over the original atom gives precisely(O4), with the factor `1/μ(a)` retained. Thus2⇒3.

Finally let a bounded increasing net `f_i≥0` have supremum `f` in `M`, and let `c_i` be its respective constants on `a`. These constants increase; put `c=sup_i c_i`. Every `f_i` is bounded above by the function equal to `c` on `a` and to `f` off `a`; hence the least-upper-bound property of `f` forces its constant on `a` to be at most `c`. Conversely each `f_i≤f` forces `c_i≤f|_a`, and taking their supremum gives the reverse inequality. Thus `χ(f)=sup_iχ(f_i)`. This proves3⇒1, including every original coefficient and atomic mass. ∎

Equations(B1),(O1),(O2) form the promised typed connection between algebraic Split-Zero branches and operator-algebraic states. They identify exactly which branches can be normal observations of the measured support. This construction does not identify a selected character of `L^infty` with a KMS state of a separate dynamical system; the KMS action and its state-space morphism must be the explicit ones in the following source lane.

## 6. KMS lane and actionable routing

The completed independent KMS response audit is `work/historical_kms_branch_audit_20260912.md`, with the companion full abstract proof report `work/historical_kms_abstract_logic_20260912.md`. It compares the actual original BC/CM/BCM source with the final transcript, and computes the exact affine barycenter maps rather than inferring invariance of an arbitrary representing measure. That older inference is false: a fixed barycenter need not make every measure in its barycenter fibre invariant. Haar averaging the measure supplies the correct map to an invariant representative. The theorem of unique fixed barycenter for a transitive compact orbit is nevertheless true.

The principal explicit coefficient recovered and proved there is, for the original BC monomial, reduced `a/q` and real `β>1`,

\[
\overline\varphi_\beta\bigl(\mu_m e(a/q)\mu_n^*\bigr)
=\delta_{mn}\frac{m^{-\beta}}{\varphi(q)}
\sum_{d\mid q}\mu(q/d)d^{1-\beta}.
\tag{K1}
\]

The full Ramanujan-sum proof and its `G(C)`-linear lift are in that report. It also preserves the exact BCM level index `d_K=[K_0:K]` in the ordinary trace `Z_y=d_K ζ_(D,L)(β)`, the full GNS exponent `−β/2`, and the CM corner-state factor `N(J)^β`. The source's actual BC→GL₂ bridge is a correspondence through a Morita bimodule; it is not automatically a map to `M(A_2)`. The report retains the corresponding source/target and its exact limits, rather than invoking an unproved KMS classification as an RH argument. Its150 exact finite calibration checks pass both normal and optimized Python; their stated scope excludes classification, infinite trace convergence, class field theory and RH.

This is relevant to the existing Zeta/CUE/scaling/BC task, and root has been sent the exact source locations and the intended route. No new user task, publication, or remote merge is created by this lane.

The existing owner task identified in this session is **Zeta Function Literature & Local Corpus Foundation**. Root receives these exact proof paths for tandem integration and can route the BC/CUE-specific consequences to the appropriate existing owner; this source lane has not inferred or created an additional user-owned task.

## 7. Scope of the new mathematics

The branch and lattice constructions(B1)–(B4) are complete versions of surviving historical claims. The ideal-completion quotient(I1)–(I8), explicit measure-algebra counterexample(M1)–(M2), and atomic observation kernel(A1)–(A3) give the exact morphisms missing from the final historical pointfree claim. They preserve the original carrier, local units, amplitude, infinities of joins, and the special zero fibres. They make no RH conclusion and introduce no assumed positivity endpoint. Their immediate use is to prevent an algebraic support branch from being mistaken for a topologically continuous observation when the arithmetic program passes from support semirings to analytic/localic realizations.

An independent full proof audit is recorded in `work/frame_branch_independent_audit_20260912.md`; it covers the branch, ideal-completion, atomic and `L^infty` results above, including the final normality proof. Its clarifications were incorporated: the section is bounded-lattice/semiring, generally not frame; the two lifts remain distinct; local complements use their local tops; the one-element support isomorphism is explicit; and representatives of the selected monotone sequence are chosen outside one common null set. No finite numerical experiment is offered as proof of these infinite-join or normality results. The full written proofs are the mathematical evidence.
