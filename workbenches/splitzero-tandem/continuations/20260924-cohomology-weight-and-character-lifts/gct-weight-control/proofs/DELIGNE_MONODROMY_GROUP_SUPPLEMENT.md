# Deligne's monodromy groups: dominant pullback, the radical, and extension to étale sheaves

Independent derivation, 24 September 2026. Labels DMG0–DMG7. This supplement supplies the remaining group-theoretic arguments in Weil II §1.3 requested after review of DP0–DP9. It does not modify the DP reconstruction or construct coefficient objects on `τ〈Z1; no Z2〉`.

## DMG0. Source and exact dependencies

The source is Pierre Deligne, *La conjecture de Weil. II*, IHÉS 52 (1980), 137–252. Read for this supplement: the entire current French §1.3, printed pages 156–162, including the general rank-one variant on page 158, propositions (1.3.8), (1.3.13), (1.3.14), and lemma (1.3.15). The actual witness is

`S20_FR_record_export.tex`,

SHA256 `d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351`. This is the current page-record transcription, not author TeX. No PDF was consulted. Source lines 560–746 contain the relevant discussion, with the final paragraph of (1.3.15) at the start of printed page 162. The available transcription says “finite subgroup of Z” in (1.3.10)(iv); the proof, corollary (1.3.11), and the direct derivation below give **finite index** instead. The witness is retained unchanged.

Foundational inputs are stated explicitly: global function-field class field theory and the Picard variety for rank one on curves; the curve-joining and Frobenius-density facts used in the source's Katz variant for general normal schemes; elementary theory of algebraic groups in characteristic zero, including their radicals and central isogenies; normality and the generic-point description of finite étale covers; and local analytic exponential/logarithm for linear algebraic groups over a finite extension of `Q_ℓ`. The deductions required here are proved below.

Fix `q=p^f`, `p≠ℓ`. A connected normal finite-type `F_q` scheme is integral. Its field of global constants can be larger than `F_q`; write it as `F_{q^{d_X}}`. Geometric Frobenius over that field has degree `d_X` relative to `q`. We retain these constant-field degrees when comparing two schemes.

For a Weil representation `V` on a geometrically connected base with finite constant field of cardinality `Q`, its algebraic monodromy extension is

\[
1\longrightarrow G^0\longrightarrow G\xrightarrow{\deg_Q}\mathbf Z\longrightarrow0.
\tag{DMG0.1}
\]

Here `G^0` is the Zariski closure of geometric monodromy. A chosen degree-one lift `w` gives `G=G^0⋊w^Z`; the action is conjugation by its actual representation matrix. The identity component of `G^0` is denoted `G^{00}`. The superscript `0` in this source notation does not by itself mean connected. The map `G→GL(V)` is faithful on `G^0`, but need not be faithful on all of `G`.

The determinant weight of an irreducible rank-`r` module is `β=(1/r)w_Q(c)`, where the determinant character is `c^{deg_Q}ε`, `ε` finite order, and

\[
w_Q(c)=2\log_Q|\iota c|.
\]

## DMG1. The rank-one input on a general normal base

**Source:** the variant following (1.3.4), printed page 158; the curve proof is (1.3.1)–(1.3.4), printed pages 156–158.

For a smooth geometrically connected curve, class field theory identifies the geometric part of the abelianized Weil group with the degree-zero idèle-class group allowing ramification at the finite boundary. Its quotient by the local boundary-unit groups is the rational point group of `Pic^0` over the finite constant field and is finite. Each boundary-unit group has finite residue quotient and pro-`p` principal units. Therefore this geometric abelian group has an open pro-`p` subgroup.

The image of a rank-one `ℓ`-adic character lies in `E^×` for some finite extension `E/Q_ℓ` and is compact on the geometric fundamental group. Its valuation image is a finite subgroup of `Z`, hence zero, so it lies in `O_E^×`, which has an open pro-`ℓ` subgroup. The intersection of the two open descriptions is both pro-`p` and pro-`ℓ`, hence trivial. The geometric image is finite.

Here is the general-base reduction used by the source. Let `X_0` be normal and connected, and let `χ` be a rank-one Weil character with values in `E^×`. Let `M` be the finite group of roots of unity in `E`. For closed points `x,y`, the curve-joining fact used by Deligne and Katz gives a curve comparison on which the preceding result applies. It yields

\[
\chi(F_x)^{\deg(y)}\chi(F_y)^{-\deg(x)}\in M,
\tag{DMG1.1}
\]

or equivalently equality of `χ(F_x)^{1/deg x}` and `χ(F_y)^{1/deg y}` in `E^×⊗_Z Q`, written multiplicatively. Degrees here are relative to the same finite constant field, so all ratios have been retained.

For a degree-zero closed-point cycle `∑_x n_x x`, equation (DMG1.1) implies

\[
\chi\left(\prod_xF_x^{n_x}\right)\in M,
\qquad \sum_x n_x\deg(x)=0.
\tag{DMG1.2}
\]

The product is used only after applying the abelian character; no noncommuting Frobenius representatives are identified. The Frobenius-density statement used in the source says that these degree-zero products are dense in the geometric abelian image. By continuity and finiteness of `M`, the entire geometric image of `χ` lies in `M`.

Choose `h≥1` killing that image. Then

\[
\chi(g)^h=b^{\deg_Q g},\qquad c^h=b,\qquad
\chi(g)=c^{\deg_Qg}\varepsilon(g),\quad\varepsilon^h=1.
\tag{DMG1.3}
\]

This is the rank-one input for arbitrary normal bases used in the group arguments below. The general curve-joining and Frobenius-density inputs are part of this deduction's scope; the curve case requires neither additional input.

## DMG2. Semisimple input, connected reductivity, and the finite-degree central element

**Source:** (1.3.9)–(1.3.12), printed pages 159–161. This also records the repaired disconnected-group step needed in DP2.

Suppose the Weil representation `V` is semisimple. The unipotent radical `U` of `G^{00}` is characteristic in `G^{00}`, hence normal in `G`. In an irreducible `G`-constituent, the `U`-invariant subspace is nonzero because a unipotent group has a nonzero fixed vector. Normality makes that invariant subspace `G`-stable, so it is the entire constituent. Thus `U` acts trivially on `V`. Faithfulness on `G^0` gives `U=1`, proving that `G^{00}` is reductive.

Let `T_1` be its connected central torus. The finitely many characters by which `T_1` acts on `V` generate its character group, because the action is faithful. Conjugation by `G` permutes these characters. A finite-index subgroup consequently acts trivially on `T_1`. The outer automorphisms of a connected reductive group that act trivially on the connected centre form a finite group: after fixing a pinning, the remaining action is through the finite root datum. A further finite-index restriction makes the degree action on `G^{00}` inner. Remove the finite geometric component group and correct the degree lift by an element of `G^{00}`. This yields a finite-index subgroup `G^{00}×Z`.

The corresponding finite étale cover and finite extension of the constant field have geometric monodromy Zariski dense in `G^{00}`. Let `T` be the maximal torus quotient of `G^{00}`, which is isogenous to `T_1`. A character of `T`, extended trivially over the degree factor, gives a rank-one Weil character. Its geometric image is finite by DMG1 and Zariski dense in the character image of `T`. A positive-dimensional torus cannot have a finite dense subset. Thus `T=1`, so `G^{00}` is semisimple and `Z(G^{00})` is finite.

Now derive a central element in the **original** `G`, rather than merely in the finite-index subgroup. Write `H=G^{00}` and choose an original positive-degree lift `w`. Take a power `w^m` whose action on `H` is inner and whose induced action on the finite group `G^0/H` is trivial. Choose `h_0∈H` with `Int(w^m)|_H=Int(h_0)|_H`, and set

\[
y=h_0^{-1}w^m.
\tag{DMG2.1}
\]

Then `y` centralizes `H` and acts trivially on `G^0/H`. If `a` is a representative of a component of `G^0`,

\[
[y,a]\in H
\quad\text{and}\quad
\operatorname{Int}([y,a])|_H=1,
\]

so `[y,a]∈Z(H)`. Also `[y,w]∈H`: this follows directly from `y=h_0^{-1}w^m`. The same conjugation calculation gives `[y,w]∈Z(H)`. The element `y` centralizes these commutators. Let `e≥1` be an exponent of the finite group `Z(H)`. Then

\[
[y^e,a]=[y,a]^e=1,
\qquad [y^e,w]=[y,w]^e=1.
\]

Together with its centralization of `H`, this proves

\[
z=y^e\in Z(G),\qquad \deg_Q z=em>0.
\tag{DMG2.2}
\]

The finite group here is `G^0/G^{00}`, not the infinite group `G/G^{00}`. The kernel of `deg_Q:Z(G)→Z` is finite: its intersection with `H` is contained in finite `Z(H)`, and its image in `G^0/H` is finite. Its cokernel is finite by (DMG2.2).

For completeness, a rank-one relation such as (DMG1.3) extends from the Weil group to all of `G`. Its restriction `χ^h=1` on geometric monodromy extends to `G^0` by Zariski density. For `g=g_0w^d`, this gives `χ(g)^h=b^d`. Therefore `ε(g)=χ(g)c^{-d}` is defined on `G` and satisfies `ε^h=1`, even when `g` is not the image of an actual Weil element.

On an irreducible rank-`r` module, let `z` act by scalar `u`, and put `m_z=deg_Q z`. Applying that extended determinant relation gives

\[
u^r=c^{m_z}\varepsilon(z),\qquad
|\iota u|=Q^{m_z\beta/2}.
\tag{DMG2.3}
\]

The same criterion holds constituent by constituent for a general finite-dimensional `G`-module. It is the precise scalar test used below, including its degree and rank factors.

## DMG3. The full nonsplit radical theorem

**Source:** theorem (1.3.8) and its proof on printed page 160.

Let `V` now be any finite-dimensional Weil representation, with no semisimplicity assumption. Choose a composition filtration

\[
0=V_0\subset V_1\subset\cdots\subset V_s=V,
\]

stable under the Weil group. The stabilizer `P⊂GL(V)` of this filtration has the homomorphism

\[
\pi:P\longrightarrow\prod_{a=1}^sGL(V_a/V_{a-1}),
\tag{DMG3.1}
\]

whose kernel `U_P` consists of matrices acting as the identity on every graded quotient. In a basis adapted to the filtration, these are block upper triangular with identity diagonal blocks; `U_P` is unipotent.

The original geometric closure `G^0` lies in `P`. Let `G_1^0` be the geometric closure on `Gr V`. Then

\[
\pi(G^0)=G_1^0,
\qquad
\ker(\pi|_{G^0})=G^0\cap U_P.
\tag{DMG3.2}
\]

For the equality of images, the algebraic group image is closed and contains the dense geometric image defining `G_1^0`; conversely it is the image of the closure of that same geometric monodromy. The kernel is unipotent because it is an algebraic subgroup of `U_P`.

The associated graded representation is semisimple, so DMG2 gives that `(G_1^0)^{00}` is semisimple. The map of identity components

\[
G^{00}\twoheadrightarrow (G_1^0)^{00}
\tag{DMG3.3}
\]

is surjective. One way to verify this is that the image is a connected normal closed subgroup, and the quotient of the target by it is an image of the finite component group of `G^0`; a connected finite algebraic group in characteristic zero is trivial.

Let `R=Rad(G^{00})`, the connected maximal solvable normal subgroup. Its image under (DMG3.3) is connected, solvable, and normal in a semisimple group, hence trivial. Consequently

\[
R\subseteq G^0\cap U_P.
\tag{DMG3.4}
\]

Every element of the latter group is unipotent, so `R` is unipotent. This proves the entire assertion (1.3.8): the radical of the connected geometric monodromy group is unipotent, including for nonsplit extensions. The proof keeps the original filtration and its unipotent kernel; it does not replace the original representation by its semisimplification and then transfer an unproved conclusion back.

## DMG4. Dominant pullback gives a finite-index monodromy comparison

**Source:** the geometric group input for (1.3.13)(i), printed page 161.

Let `f:Y_0→X_0` be a dominant morphism between normal connected finite-type schemes over `F_q`. Let `K=k(X_0)` and `L=k(Y_0)`. The algebraic closure of `K` inside the finitely generated extension `L` is finite over `K`; its separable part `K_s` is also finite. After compatible geometric generic points are chosen, restriction of absolute Galois groups has image

\[
\operatorname{im}\bigl(\operatorname{Gal}(L^{sep}/L)\to
\operatorname{Gal}(K^{sep}/K)\bigr)
=\operatorname{Gal}(K^{sep}/K_s).
\tag{DMG4.1}
\]

The image is closed by compactness. Its fixed field inside `K^{sep}` is exactly `K^{sep}∩L=K_s`; Galois correspondence then proves the displayed equality. Its index is `[K_s:K]`, retaining the finite extension rather than declaring a surjection without qualification.

For a normal connected scheme, its generic-point Galois group surjects onto the étale fundamental group: a connected finite étale cover is normal and integral, and thus has connected generic fiber. The commutative diagram of generic and scheme fundamental groups therefore implies that

\[
H=\operatorname{im}(\pi_1(Y_0)\to\pi_1(X_0))
\]

is an open subgroup, of index at most `[K_s:K]`. This is the needed finite-index assertion; injectivity is neither stated nor used.

Let the exact constant fields be `F_{q^{d_X}}` and `F_{q^{d_Y}}`. Dominance embeds the first in the second, so `d_X` divides `d_Y`. Write `W_q` for the inverse image of `Z⊂\widehat Z` using degree relative to `F_q`; its degree image for `X_0` is `d_XZ`, and for `Y_0` it is `d_YZ`. The induced map preserves that absolute degree. Thus

\[
\operatorname{im}(W_q(Y_0)\to W_q(X_0))=H\cap W_q(X_0).
\tag{DMG4.2}
\]

Indeed a lift in `π_1(Y_0)` of an element whose degree is an integer already belongs to `W_q(Y_0)`. Conversely all Weil elements have integer degree. The index is finite. Intersecting once more with degree zero shows that the image of geometric `π_1(Y)` has finite index in geometric `π_1(X)`.

For a representation `V` of `W_q(X_0)`, take the Zariski closures of these geometric images on the **same** vector space. The closure for `Y_0` is an algebraic subgroup of finite index in the closure for `X_0`, so their identity components agree. The monodromy extensions with retained absolute degree give an injective comparison

\[
G_Y\hookrightarrow G_X
\tag{DMG4.3}
\]

onto a finite-index subgroup: injectivity follows because the map is the identity inclusion on the geometric closure and preserves degree, and finite index follows from the finite component quotient together with `[d_XZ:d_YZ]=d_Y/d_X`. Choosing Weil lifts gives an explicit semidirect-product description, but the subgroup and the morphism do not depend on the chosen lifts.

## DMG5. Determinant weights are preserved and detected by dominant pullback

**Source:** proposition (1.3.13)(i), printed page 161.

The assertion is:

\[
V\text{ is purely of determinant weight }\beta
\quad\Longleftrightarrow\quad
f^*V\text{ is purely of determinant weight }\beta.
\tag{DMG5.1}
\]

For clarity, “purely of determinant weight β” means that **each nonzero irreducible constituent** has determinant weight β. It is not yet the assertion that every local eigenvalue has that weight.

First take `V` semisimple. Its restriction to a finite-index subgroup is semisimple. To verify this, pass to a finite-index normal core `H_0`. The sum of simple `H_0`-submodules of an irreducible `W`-module is nonzero and `W`-stable, hence the whole module. Thus restriction to `H_0` is semisimple. For an intermediate finite-index subgroup `H`, average an `H_0`-equivariant projection over the finite group `H/H_0`; characteristic zero permits division by its order. This supplies invariant complements and proves semisimplicity for `H` too.

Choose a central `z∈G_X` of positive degree by DMG2. Some positive power `z^a` belongs to the finite-index subgroup `G_Y`. Let the absolute degree of `z` relative to `q` be `m`. Then its degrees relative to the two exact constant fields are

\[
\deg_{q^{d_X}}z=\frac{m}{d_X},\qquad
\deg_{q^{d_Y}}z^a=\frac{am}{d_Y}.
\tag{DMG5.2}
\]

Both displayed numbers are integers where used. On an irreducible constituent of `V`, the element `z` acts by a scalar `u`. If that constituent has determinant weight β, (DMG2.3) gives

\[
|\iota u|=(q^{d_X})^{(m/d_X)\beta/2}=q^{m\beta/2}.
\tag{DMG5.3}
\]

Every irreducible constituent of its restriction to `G_Y` inherits the scalar `u^a` from `z^a`. Applying the same criterion over its exact constant field gives

\[
|\iota u^a|=q^{am\beta/2}
=(q^{d_Y})^{(am/d_Y)\beta/2}.
\tag{DMG5.4}
\]

Its determinant weight is therefore precisely β. Conversely, if all restricted constituents have determinant weight β, choose a nonzero restricted constituent inside each original irreducible constituent. Equation (DMG5.4) then forces (DMG5.3), because `a>0`; the original constituent has determinant weight β.

For nonsplit `V`, its composition filtration pulls back to an exact filtration. The multiset of constituents of `f^*V` is the union of the multisets obtained from its irreducible original quotients. Replace those quotients, only for this constituent calculation, by their direct sum; the semisimple argument just proved applies. It proves (DMG5.1) for the original `V` without an assertion that its extensions split.

The zero representation satisfies both sides vacuously for every β. No maximum of an empty weight set is taken.

## DMG6. A compact Zariski-dense subgroup has compact normalizer in a semisimple local group

**Source:** lemma (1.3.15), printed pages 161–162. The proof here, as in the source, treats characteristic zero.

Let `E/Q_ℓ` be finite, let `H` be a connected semisimple linear algebraic group over `E`, and let `K⊂H(E)` be compact and Zariski dense. Then

\[
N_{H(E)}(K)=\{g\in H(E):gKg^{-1}=K\}
\]

is compact.

Choose a sufficiently small analytic neighborhood of the identity on which exponential and logarithm are inverse. There is an open normal subgroup `K_0⊂K` contained in it: take the normal core in `K` of a sufficiently small open subgroup. The finite group `K/K_0` has an exponent `n≥1`. For every `x∈K`, define

\[
\log_K(x)=\frac1n\log(x^n)\in\operatorname{Lie}H(E).
\tag{DMG6.1}
\]

This is independent of the sufficiently divisible exponent chosen. On an analytic logarithm neighborhood, `log(y^r)=r log y`; applying that identity after two chosen exponents have been replaced by a common multiple proves independence. It is continuous on `K`, and commutes with conjugation wherever the conjugate also lies in a compact subgroup. In particular its compact image is invariant under the normalizer of `K`.

Let

\[
\mathfrak l=\operatorname{span}_E\log_K(K)\subseteq\operatorname{Lie}H.
\tag{DMG6.2}
\]

It is invariant under `Ad K`; the condition that a linear subspace be preserved is Zariski closed, so density makes it `Ad H`-invariant. Hence it is an ideal of the semisimple Lie algebra. Such an ideal is the Lie algebra of a connected normal algebraic subgroup `H'⊂H`: after extending to an algebraic closure it is the sum of a set of simple ideals, hence of the corresponding simple factors up to central isogeny; Galois stability gives descent to `E`.

For the quotient map `π:H→H/H'`, logarithms satisfy `log(π(x))=dπ(log(x))` near the identity. The right side is zero for `x∈K` in a sufficiently small neighborhood. The logarithm is injective there, so `π` kills an open subgroup of `K`. Thus `π(K)` is finite. It is also Zariski dense in the connected group `H/H'`. A finite closed subset cannot be dense in a positive-dimensional connected algebraic group. Therefore `H/H'=1` and

\[
\operatorname{span}_E\log_K(K)=\operatorname{Lie}H.
\tag{DMG6.3}
\]

Let `Λ` be the `O_E`-span of this compact logarithm set. It is bounded: choose an `E`-basis of `Lie H`; compactness bounds every coordinate of `log_K(K)` by one finite power of a uniformizer. Thus `Λ` lies in a fixed scalar multiple of the standard lattice. Since `O_E` is noetherian, it is finitely generated; (DMG6.3) gives full rank. Therefore `Λ` is an `O_E`-lattice. Every element normalizing `K` preserves `Λ` in both directions, so

\[
\operatorname{Ad}(N_{H(E)}(K))\subseteq GL_{O_E}(\Lambda).
\tag{DMG6.4}
\]

The group on the right is compact. The adjoint map has finite kernel and factors as the finite central isogeny `H→H_ad` followed by a closed embedding in `GL(Lie H)`. Its inverse image of a compact subset is compact. Here is a coordinate verification of that last assertion. On affine coordinate rings, every chosen coordinate generator `x_j` of `E[H]` is integral over `E[H_ad]`, hence satisfies

\[
x_j^{r_j}+a_{j,r_j-1}x_j^{r_j-1}+\cdots+a_{j,0}=0,
\tag{DMG6.5}
\]

where each `a_{j,i}` is a regular function on `H_ad`. On a compact set `C⊂H_ad(E)`, put

\[
M_j=\max\left(1,\ \max_{0\le i<r_j}\sup_{c\in C}|a_{j,i}(c)|_E\right).
\tag{DMG6.6}
\]

If `|x_j|_E>M_j`, the leading term in (DMG6.5) strictly dominates every other term in the nonarchimedean absolute value, which is impossible. Thus every coordinate of every inverse-image point is bounded by the displayed finite constant. The inverse image is closed and lies in a product of compact balls in the local field; it is compact.

Take `C=H_ad(E)∩GL_{O_E}(Λ)`, a closed subset of a compact group. Equation (DMG6.4) puts the normalizer in its compact inverse image. Finally the normalizer is closed: if `g_a→g` with each `g_aKg_a^{-1}=K`, then for each `k∈K`, closedness of `K` gives `gkg^{-1}∈K`; applying the same argument to inverses gives equality. A closed subset of the compact inverse image is compact. This proves the lemma.

## DMG7. The determinant criterion for an irreducible Weil sheaf to be étale

**Source:** proposition (1.3.14), printed page 161, using (1.3.15).

Let `V` be an irreducible lisse Weil sheaf of rank `r` on a normal connected finite-field scheme. Then

\[
V\text{ extends to an étale sheaf}
\quad\Longleftrightarrow\quad
\det V\text{ extends to an étale sheaf}.
\tag{DMG7.1}
\]

Necessity follows because exterior power is a continuous polynomial operation on a continuous representation of the profinite fundamental group. We prove sufficiency, retaining the scalar and degree.

Use the exact constant field of cardinality `Q=q^{d_X}` and its degree. Let `G` be the monodromy extension, choose `z∈Z(G)` of positive degree `m`, and let its action on `V` be scalar `u`. Enlarge a finite coefficient field `E/Q_ℓ` so that the representation, the needed group equations, and `z,u` are all defined over `E`. Suppose `det V` is étale. Write its character using (DMG1.3) as `χ=c^{deg_Q}ε`, with `ε^h=1`. An étale character has compact image on the profinite group, so `c` is an `ℓ`-adic unit. The exact determinant equation at `z` is

\[
u^r=c^m\varepsilon(z).
\tag{DMG7.2}
\]

Applying the discrete valuation, for which roots of unity have valuation zero, gives

\[
r\,v_E(u)=m\,v_E(c)=0.
\tag{DMG7.3}
\]

Hence `u` is a unit.

The subgroup

\[
G_1=G^{00}\,z^{\mathbf Z}\cong G^{00}\times z^{\mathbf Z}
\tag{DMG7.4}
\]

has finite index in `G`. The product is direct: `z` is central, and a power of nonzero-degree `z` lies in `G^{00}` only when that power is zero. Let `W_1` be its inverse image in the Weil group, and let `W_1^0` be the inverse image of `G^{00}`. Projection in (DMG7.4) defines

\[
\rho:W_1\longrightarrow G^{00}(E).
\tag{DMG7.5}
\]

The subgroup `K=ρ(W_1^0)` is compact, because `W_1^0` is a finite-index closed subgroup of geometric `π_1`, and it is Zariski dense in `G^{00}` by the definition of the monodromy closure and its identity component. Since `W_1^0` is normal in `W_1`, its image `K` is normalized by `ρ(W_1)`. DMG6 makes this normalizer compact. Thus `ρ(W_1)` is bounded.

For `w∈W_1`, the full original representation is

\[
R(w)=\rho(w)\,u^{\deg_Q(w)/m}.
\tag{DMG7.6}
\]

The exponent is an integer. Since `u` is a unit, its positive and negative powers lie in the compact group `O_E^×`. Both factors in (DMG7.6) are bounded, so the image of `W_1` is bounded. The entire Weil group is a finite union of its cosets, so its image is bounded as well.

Choose any lattice `L_0⊂V_E`. Boundedness gives an integer `b≥0` such that `R(w)L_0⊂π_E^{-b}L_0` for all `w`. Then

\[
L=\sum_w R(w)L_0
\tag{DMG7.7}
\]

is a full-rank `O_E`-submodule between `L_0` and `π_E^{-b}L_0`. It is finitely generated and hence a lattice; the group action permutes its defining summands, so it is stable. Thus the representation lands in the profinite group `GL(L)`.

To see the extension explicitly, select a geometric Frobenius lift `F` over the exact constant field. In the profinite arithmetic fundamental group, the map from `Z` taking `1` to `F` extends to a continuous map from `\widehat Z`, since the closure of the cyclic group generated by one element in a profinite group is procyclic. Composing with degree is the identity on `\widehat Z`, so this is a section. Hence

\[
\pi_1(X_0)=\pi_1(X)\rtimes\widehat{\mathbf Z},
\qquad W(X_0)=\pi_1(X)\rtimes\mathbf Z.
\tag{DMG7.8}
\]

Similarly the powers of `R(F)∈GL(L)` extend continuously from `Z` to `\widehat Z`. The compatibility of the conjugation action with the already continuous geometric representation holds for integer powers; density and continuity extend it to `\widehat Z`. Therefore

\[
R(\gamma F^a)=R(\gamma)R(F)^a,
\qquad \gamma\in\pi_1(X),\ a\in\widehat{\mathbf Z},
\tag{DMG7.9}
\]

defines the required continuous extension. Density makes it unique. This proves sufficiency in (DMG7.1).

Finally every irreducible Weil sheaf is a retained constant twist of an étale sheaf. Let `Q=p^g` be the exact constant field and let `c` be its determinant scalar in (DMG1.3). Choose

\[
b\in\overline{\mathbf Q}_\ell^\times,
\qquad b^{rg}=c^{-1}.
\tag{DMG7.10}
\]

Use the constant Weil line over `F_p` on which its geometric Frobenius acts by `b`. At a point of degree `d` over `F_Q`, this line acts by `b^{gd}`. Twisting `V` by it changes the determinant scalar from `c` to `cb^{rg}=1`, so the determinant character becomes exactly the finite-order character `ε`. By (DMG7.1), the twisted sheaf `V_b` is étale. The original object is recovered by the exact inverse twist

\[
V=V_b\otimes\mathcal L_{b^{-1}}.
\tag{DMG7.11}
\]

The determinant factor at a closed point is `b^{rgd}`, not `b^{rd/g}`. No factor, scalar, degree, or extension class has been suppressed. Equations (DMG7.10)–(DMG7.11) are a comparison with the original sheaf, not a replacement of it in the weight calculation.
