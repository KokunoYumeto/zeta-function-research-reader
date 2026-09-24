# Deligne's fundamental weight argument: the surface, its singular fibres, and the exact weight conclusion

Status: independent derivation of the argument in *La conjecture de Weil II*, §§3.1–3.3, with the coefficient weight retained throughout. This is a reconstruction of the finite-field theorem. It does not assert a transfer of that theorem to the programme's supporting point. The upstream purity criterion, local monodromy theorem and boundary nonvanishing theorem are identified below by their full mathematical conclusions and source locators. Their proofs belong to the adjoining source reconstructions; the present file does not claim to have independently reproved the SGA results used by Deligne.

## DW0. Source identity, actual reading, and discrepancies

Author: Pierre Deligne. Work: *La conjecture de Weil. II*, Publications Mathématiques de l'IHÉS **52** (1980), 137–252. The receiving argument is §§3.1–3.3, article pages 197–207. The primary publication is indexed at <https://www.numdam.org/item/PMIHES_1980__52__137_0/>.

The text read here is the local current French page-record export:

`output/Deligne_Weil_II_S20_LaTeX/typed_latex/S20_FR_record_export.tex`

SHA256: `d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351`.

This file is a modern transcription, not Deligne-authored TeX. Its page-record verification verifies reversible export and coverage; it is not a mathematical verification of every formula. The original printed PDF was not used in this derivation. The older English TeX companion was read for comparison, not treated as authority.

Actual reading coverage for this derivation:

- Current French §§3.1–3.3, in full, lines 1933–2311, including every displayed relation and each geometric reduction.
- Current French conventions (0.1)–(0.11), lines 192–251; definitions and operations (1.2.1)–(1.2.8), lines 480–530.
- Current French (1.4.1)–(1.5.3), lines 749–872; (1.6.4)–(1.6.14), lines 885–1063; (1.7.1)–(1.7.12), lines 1067–1207; (1.8.1)–(1.8.8), lines 1210–1276.
- Current French final proof of (2.2.9) and all of (2.2.10), lines 1883–1927. The complete proofs of §§2.1–2.2 are handled in the adjoining reconstruction, not certified by these last paragraphs alone.
- Historical English §§3.1–3.3, lines 1832–2072, and displayed (1.6.14.3), for edition comparison.

The following discrepancies are material. They are discrepancies in the available witnesses, not claims that Deligne printed these errors.

| Locator | Available witness | Formula used in this derivation and its justification |
|---|---|---|
| (3.2.4), (3.2.11), (3.2.13) | Historical English repeatedly changes the French non-strict inequalities into strict inequalities. | The inductive conclusion is `≤`; the independent strict input is specifically (2.2.10). |
| (3.2.7) | Historical English calls the external tensor product itself real. | The real sheaf is a direct-sum companion. At weight zero it is `G ⊕ G∨`; the full-weight companion is constructed in DW4. |
| (3.2.9.1) | Historical English omits the final generic stalk of `R²f_!`. | The complete sequence has both special and generic `R²f_!` stalks, displayed in DW5. |
| (3.2.12) | Historical English changes `≤2` into `<2`. | The correct bound at source weight zero is `≤2`; DW7 retains the full coefficient weight and obtains `≤2β+2`. |
| (3.3.9) | Historical English uses `det(1−Ft)` while retaining the absolute value of eigenvalues. | `det(t·1−F)` has roots of modulus `q^{i/2}`; `det(1−Ft)` has reciprocal roots of modulus `q^{−i/2}`. |
| (3.2.1) | Current French writes the duality partner `F∨(−1)`. | The partner is `F∨(1)`: the trace pairing has target `Q̄ℓ(−1)`, and the added `(1)` makes its target `Q̄ℓ`. The corrected identity is proved in DW4. |
| (3.2.7.1) | Current French prints ordinary `H¹` of a generally open fibre. | Proper-support base change gives `H_c¹` for `R¹f_!`. No properness of that open fibre is assumed. |
| (3.2.12) | Current French retains a free `β` inside a proof already restricted to weight zero. | DW7 proves the statement with the actual weight `2β` of the external product, removing the free-symbol ambiguity by an explicit calculation. |
| (1.6.14.3) | Both witnesses display a positive twist `(i+j)/2`. | From `N:V(1)→V`, the primitive contribution is `P_{−j}(−(i+j)/2)`. Applying `N^{(i+j)/2}` proves that sign. DW1 records the resulting weight theorem; the adjoining local reconstruction proves it. |
| (3.1.3.3), optional description | Current French calls the Kummer class of `u/v` a generator modulo `ℓ^n`. | For the local equation `uv=t`, over a geometric generic fibre `[v]=−[u]`, so `[u/v]=2[u]`. The needed branch-sign line is constructed from `[u]` and `[v]`, retaining their opposite signs. The optional factor-two assertion is not used. |

No source file has been overwritten. The derivation below states its own formulas and proves the corrections from the applicable maps.

## DW1. Objects, Frobenius, weights, and the exact upstream results

Fix primes `p≠ℓ`, a power `q=p^a`, an algebraic closure `F̄_q`, and a field isomorphism

\[
\iota:\overline{\mathbb Q}_{\ell}\longrightarrow\mathbb C.
\]

Objects carrying subscript `0` are defined over `F_q`. Removing the subscript means extension of scalars to `F̄_q`. Every sheaf is a constructible `Q̄_ℓ`-sheaf, or a Weil sheaf as specified, on a separated finite-type scheme with `ℓ` invertible. Frobenius is geometric Frobenius. For a nonzero eigenvalue `α`,

\[
w_q(\alpha)=2\log_q|\iota(\alpha)|.
\tag{DW1.1}
\]

At a closed point `x` of degree `d`, the appropriate base is `N(x)=q^d`. A lisse sheaf is pointwise `ι`-pure of weight `β` when each of its local eigenvalues has absolute value `N(x)^{β/2}`. A mixed sheaf has a finite filtration with pointwise pure successive quotients. Without an `ι` qualifier, purity additionally asserts algebraicity and the same modulus for every complex conjugate, and its weights are integers.

The Tate line `Q̄_ℓ(1)` carries geometric Frobenius `q^{-1}`. Thus

\[
w_q(\alpha q^{-r})=w_q(\alpha)-2r,
\quad
w_q(\alpha\gamma)=w_q(\alpha)+w_q(\gamma),
\quad
w_q(\alpha^{-1})=-w_q(\alpha).
\tag{DW1.2}
\]

All following occurrences of Tate twists use this convention. In particular `(-1)` raises weight by two; it is not a deleted factor.

The proof uses the following results, which are established earlier in Deligne's paper or are explicitly cited cohomological theorems.

**Input D1: degree zero and degree two on a curve, (1.4.1)–(1.4.4).** For a geometrically connected smooth curve `C`, a lisse sheaf with geometric fibre representation `V`, and `π=π_1(C)`,

\[
H^0(C,\mathcal F)=V^{\pi},\qquad
H_c^0(C,\mathcal F)=
\begin{cases}V^{\pi},&C\text{ proper},\\0,&C\text{ not proper},\end{cases}
\qquad H_c^2(C,\mathcal F)=V_{\pi}(-1).
\tag{DW1.3}
\]

For a pointwise pure coefficient of weight `β`, eigenvalues on `H^0` or `H_c^0` have weight `β`, and on `H_c^2` have weight `β+2`. For a coefficient whose pointwise weights are bounded above by `b`, the corresponding upper bounds are `b` and `b+2`. For a general constructible coefficient, restrict to a dense lisse open for degree two; degree zero consists of global sections, with any finite-support contributions included. These assertions retain the Tate `(-1)` in (DW1.3).

**Input D2: Grothendieck's trace formula, (1.4.5.1).** With `d(x)=[k(x):F_q]`,

\[
\prod_{x\in|C_0|}
\det(1-F_xt^{d(x)},\mathcal F_{\bar x})^{-1}
=
\frac{\det(1-Ft,H_c^1(C,\mathcal F))}
{\det(1-Ft,H_c^0(C,\mathcal F))
 \det(1-Ft,H_c^2(C,\mathcal F))}.
\tag{DW1.4}
\]

Both denominator factors remain present. A zero cohomology group contributes the determinant one by an actual vanishing theorem, not a convention discarding a contribution. For a pure weight-`β` sheaf, the Euler product converges and is nonzero for `|t|<q^{-(β+2)/2}` on a curve; this follows from (1.4.6), counting degree-`d` closed points by `O(q^d)` and using the geometric series with terms `q^{d(1+β/2)}|t|^d`.

**Input D3: constituents of real sheaves, (1.5.1).** A lisse sheaf on a smooth geometrically connected curve whose local characteristic polynomials become real under `ι` has pointwise `ι`-pure simple constituents. Therefore each direct summand of such a sheaf has a finite filtration by lisse pointwise `ι`-pure quotients. This is the exact input used for the pencil's first direct image. It is not an assertion that a point or a reflection alone forces weights.

**Input D4: local monodromy purity, (1.8.4).** If a lisse sheaf of weight `β` is restricted to the geometric generic point of a henselian trait at a boundary point `s`, its local monodromy filtration `M` satisfies

\[
\operatorname{Gr}_i^M V\text{ is pure of weight }\beta+i
\quad\text{relative to }N(s).
\tag{DW1.5}
\]

Here the nilpotent logarithm is a Frobenius-compatible map `N:V(1)→V`. Inertia acts unipotently after a finite covering; on the monodromy graded pieces it acts trivially in the unipotent case. At a general boundary point,

\[
(j_*\mathcal F)_{\bar s}=V^I
\subseteq\ker N\subseteq M_0V,
\tag{DW1.6}
\]

where the first containment includes taking invariants under the residual finite inertia quotient. The induced graded pieces have weights `β+i`, `i≤0`. Formation in a tame family along a smooth relative divisor is compatible with taking fibres, as constructed in (1.7.8), (1.8.6)–(1.8.8).

**Input D5: strict curve estimate, (2.2.10).** Every eigenvalue on `H_c^1(C, F)` for a lisse pure weight-`β` coefficient satisfies

\[
w_q(\alpha)<\beta+2.
\tag{DW1.7}
\]

The strict sign comes from the Hadamard–de la Vallée-Poussin argument in §2, through the nonvanishing of its representation-theoretic `L`-functions on the boundary. The weaker `≤β+2` follows already from (1.8.2), or directly from (DW1.4) and the convergence disk. In DW6 it is precisely the strict sign, together with a discrete weight congruence, that produces a full one-unit gain.

**Input D6: cohomological geometry.** Proper-support base change; finite-dimensionality; the Künneth isomorphism; the compact-support Leray spectral sequence; Poincaré duality; the existence of sufficiently general Lefschetz pencils; the local Picard–Lefschetz calculation for an ordinary node; and quasi-unipotence followed by a finite cover are the geometric theorems used by Deligne. This reconstruction proves their applications and all resulting weight inferences. It does not claim fresh proofs of these foundational SGA theorems.

## DW2. The surface and the pencil, with its exceptional divisor retained

Let `S` be a smooth projective surface over an algebraically closed field, `D` a normal-crossings divisor, `V=S\D`, and `j:V→S`. Let `F` be lisse on `V`, tame along `D`. Choose an embedding in projective space and a pencil of hyperplanes with axis `A`; its parameter space `A*` is a projective line. Set

\[
\widetilde S=\{(x,t)\in S\times A^*:x\in H_t\},
\quad\pi:\widetilde S\to S,
\quad f:\widetilde S\to A^*,
\quad\widetilde V=\pi^{-1}(V).
\tag{DW2.1}
\]

The hypotheses of (3.1.1) are all used:

1. The axis is transverse to `S` and misses `D`; therefore `π` blows up the finite set `A∩V`.
2. Critical points of `f` on `S̃` are ordinary quadratic singularities and miss `D`.
3. Critical points of the map on the normalization `D′` are ordinary quadratic singularities and lie over smooth points of `D`.
4. Each exceptional fibre has exactly one exceptional point.

The three exceptional types are consequently: an interior node; a tangency of the fibre to a smooth boundary branch; or a fibre meeting a crossing of two boundary branches.

Since the blowup centres lie in `V`, the exceptional lines contribute to compact-support cohomology in degree two. The full blowup formula is

\[
H_c^m(\widetilde V,\pi^*\mathcal F)
\simeq H_c^m(V,\mathcal F)
\oplus
\begin{cases}H^0(A\cap V,\mathcal F)(-1),&m=2,\\0,&m\ne2.\end{cases}
\tag{DW2.2}
\]

In particular `π*` is injective. Its retraction is the map obtained by taking the Poincaré-dual transpose of pullback in ordinary cohomology. The added term is not identified with zero or removed from the construction.

Properness of `A*` yields the Frobenius-compatible Leray spectral sequence

\[
E_2^{p,r}=H^p(A^*,R^rf_!\pi^*\mathcal F)
\Longrightarrow H_c^{p+r}(\widetilde V,\pi^*\mathcal F).
\tag{DW2.3}
\]

Here `f_!` on the open surface means `f_*j_!` for the proper surface map. That is why the open fibres contribute compact-support cohomology. All differentials commute with Frobenius. Hence every eigenvalue of the abutment occurs on a subquotient of one of the displayed `E₂` groups, with algebraic multiplicity controlled by those subquotients.

## DW3. All three local vanishing-cycle calculations

At an exceptional value `t`, work on the strict henselization of `A*` at `t`, with geometric generic point `η̄`. Write `Φ_x^r` for the vanishing cycles of `j_!π*F`, supported at its one exceptional point `x`. Assume additionally that local boundary monodromy is unipotent. Then near a boundary point the lisse coefficient has a finite filtration whose graded pieces extend constantly over the strict localization, as in (3.1.2).

For a two-element branch set `B`, define the sign line

\[
\epsilon(B)=\mathbb Z^B/\mathbb Z(1,1),
\qquad \epsilon_\ell(B)=\epsilon(B)\otimes\overline{\mathbb Q}_\ell.
\tag{DW3.1}
\]

The two choices of branch give opposite generators. A Frobenius permutation of the branches therefore acts by `+1` or `−1`, so this line is pure of weight zero. This conclusion keeps the sign representation; it does not identify it with a canonically trivial representation.

**Interior node.** The coefficient is lisse at `x`. The relative-dimension-one Picard–Lefschetz calculation gives

\[
\Phi_x^r(j_!\pi^*\mathcal F)=0\quad(r\ne1),
\qquad
\Phi_x^1(j_!\pi^*\mathcal F)
=\mathcal F_x(-1)\otimes\epsilon_\ell(B).
\tag{DW3.2}
\]

In a node chart `uv=t`, choosing `u` identifies the geometric generic local cohomology with the Kummer class of `u`; choosing `v` negates this class because `t` has compatible roots over the geometric generic field. Thus the branch ambiguity is precisely the sign line. The cohomological factor is `(-1)`, with Frobenius multiplier `N(x)`, and is retained.

**Tangency to the boundary.** First use the constant coefficient and the exact sequence

\[
0\to j_!\overline{\mathbb Q}_\ell
\to\overline{\mathbb Q}_\ell
\to\overline{\mathbb Q}_{\ell,D}\to0.
\tag{DW3.3}
\]

The ambient surface morphism is smooth at `x`, so its constant sheaf has no vanishing cycles there. The long exact sequence gives

\[
\Phi_x^r(j_!\overline{\mathbb Q}_\ell)
\simeq\Phi_x^{r-1}(D,\overline{\mathbb Q}_\ell).
\tag{DW3.4}
\]

The generic fibre of the local double cover on `D` has two points `B`; its reduced degree-zero cohomology is `Q̄_ℓ^B/Q̄_ℓ=ε_ℓ(B)`. Therefore only `r=1` is nonzero and its value is `ε_ℓ(B)`, without a Tate twist. Apply the same exact-sequence calculation to each constant graded coefficient in the local filtration. Since all other cohomological degrees vanish, the resulting filtration has

\[
\operatorname{Gr}_F^i\Phi_x^1(j_!\pi^*\mathcal F)
=\operatorname{Gr}_F^i(\mathcal F)_x\otimes\epsilon_\ell(B).
\tag{DW3.5}
\]

**Crossing of two boundary branches.** Let `i:D′→S` be the normalization near the crossing. The constant-coefficient exact sequence is

\[
0\to j_!\overline{\mathbb Q}_\ell
\to\overline{\mathbb Q}_\ell
\to i_*\overline{\mathbb Q}_\ell
\to\overline{\mathbb Q}_{\ell,x}\otimes\epsilon_\ell(B)
\to0.
\tag{DW3.6}
\]

Both `f` and `f∘i` are smooth at the relevant points. Applying vanishing cycles to the two short exact sequences obtained from (DW3.6) shifts the point-supported term by two:

\[
\Phi_x^r(j_!\overline{\mathbb Q}_\ell)
\simeq\Phi_x^{r-2}
(\overline{\mathbb Q}_{\ell,x}\otimes\epsilon_\ell(B)).
\tag{DW3.7}
\]

The point-supported term has no nearby generic fibre. With the convention of (3.1), its only vanishing-cycle group is in degree `−1`, equal to its stalk. Thus (DW3.7) is nonzero only for `r=1`, where it equals `ε_ℓ(B)`. Devissage in the coefficient filtration gives exactly (DW3.5), again with no Tate twist.

Consequently every one of the three types has vanishing cycles concentrated in degree one. For a coefficient whose local graded weights lie in `b+Z`, all these cycle weights also lie in `b+Z`: the sign line adds zero, and the nodal Tate factor adds two. This congruence, rather than an invented metric or a point's position, is what the next stage extracts from the local geometry.

## DW4. Real characteristic polynomials and the correct real companion

Let `C₀` be a smooth curve and `E₀` a lisse, pointwise pure weight-`b`, `ι`-real sheaf. We prove the full statement (3.2.1) for `i=0,1,2`.

First suppose `C₀` geometrically connected. Applying `ι` to (DW1.4), the Euler product is a real rational function since all its local characteristic polynomials are real. By D1, the zeros of the `H_c²` determinant have absolute value `q^{-(b+2)/2}`. By D5, the zeros of the `H_c¹` determinant have strictly larger absolute value. The `H_c⁰` determinant, if nontrivial, has zeros of absolute value `q^{-b/2}`, also strictly larger. Thus there is no cancellation at the radius `q^{-(b+2)/2}`: the poles on that circle, counted with their multiplicities, are exactly the zeros of the `H_c²` determinant. The real rational function has a conjugation-stable pole multiset there. The determinant's constant term is one, so its polynomial is real.

If the curve is not proper, `H_c⁰=0`. If it is proper, Poincaré duality gives a perfect equivariant pairing

\[
H^0(C,\mathcal E)\otimes H^2(C,\mathcal E^\vee(1))
\longrightarrow\overline{\mathbb Q}_\ell.
\tag{DW4.1}
\]

The coefficient `E∨(1)` is pure of weight `−b−2` and real: inverse roots of a real polynomial remain conjugation-stable, and the Tate multiplier is real. Its `H²` determinant is real by the preceding argument. Reciprocal eigenvalues preserve conjugation-stability, proving that the `H⁰` determinant is real. Now both denominator factors in (DW1.4) are real, so its numerator, the `H_c¹` determinant, is real too.

For a curve which becomes disconnected over `F̄_q`, pass to its finite constant-field extensions componentwise. Frobenius permutes the components in cycles. A cycle of length `d` contributes `det(1-F^dt^d,V)`; the same argument over `F_{q^d}` makes this real. Multiplying these real factors proves the general assertion (3.2.2).

Now let `F₀` be any lisse pure weight-`β` sheaf on a smooth curve `U₀`; it need not be real. On `V₀=U₀×U₀`, set

\[
\mathcal G_0=\operatorname{pr}_1^*\mathcal F_0
\otimes\operatorname{pr}_2^*\mathcal F_0.
\tag{DW4.2}
\]

This external product has weight `2β`. Choose `a∈Q̄_ℓ^×` with `ι(a)=q^{2β}`, and let `L_a` be the constant rank-one **Weil** sheaf over `F_q` with Frobenius `a`. Define

\[
\mathcal H_0=
\mathcal G_0\oplus(\mathcal G_0^\vee\otimes L_a).
\tag{DW4.3}
\]

The line has weight `4β`, so both summands have weight `2β`. If `λ` is a local eigenvalue of `G₀` at a degree-`d` point, then `|ιλ|=q^{dβ}` and

\[
\iota(a^d\lambda^{-1})
=\frac{q^{2d\beta}}{\iota\lambda}
=\overline{\iota\lambda}.
\tag{DW4.4}
\]

Hence `H₀` is `ι`-real. This constructs the real companion while keeping `G₀`, its original eigenvalues, the weight `β`, and the extra line explicit. It is a direct-sum receiving construction, not a replacement of `F₀` by a normalized coefficient.

Write `W₀⊂A₀*` for the nonexceptional parameter locus. Proper-support base change gives, for a closed parameter `x` and geometric fibre `Y`,

\[
(R^1f_!\pi^*\mathcal H_0)_{\bar x}
=H_c^1(Y,\pi^*\mathcal H).
\tag{DW4.5}
\]

The just-proved reality proposition applies to that smooth, possibly disconnected open curve over `k(x)`. It follows that `w*R¹f_!π*H₀` is real. The sheaf

\[
\mathcal R_0=w^*R^1f_!\pi^*\mathcal G_0
\tag{DW4.6}
\]

is a direct summand, because `Rf_!` respects the finite direct sum in (DW4.3). Input D3 supplies a finite filtration of `R₀` by lisse pointwise pure quotients. At `β=0`, choose `a=1`; (DW4.3) is exactly Deligne's `G₀⊕G₀∨` construction in (3.2.7).

## DW5. The boundary forces the weight congruence of every nonconstant piece

Maintain all pencil hypotheses of DW2–DW3. Let

\[
\mathcal R=R^1f_!\pi^*\mathcal G,
\qquad
\mathcal S=R^2f_!\pi^*\mathcal G.
\]

At an exceptional parameter `t`, the concentration of vanishing cycles in degree one gives the complete exact sequence

\[
0\longrightarrow\mathcal R_{\bar t}
\longrightarrow\mathcal R_{\bar\eta}
\longrightarrow\Phi_x^1
\longrightarrow\mathcal S_{\bar t}
\longrightarrow\mathcal S_{\bar\eta}
\longrightarrow0.
\tag{DW5.1}
\]

The initial injection proves that `R` has no section supported at `t`: any such section vanishes at the generic stalk, and therefore at the special stalk. Applying this at every exceptional point gives `R↪w_*w*R`.

Let `G^i(w*R₀)` be the finite pure-quotient filtration from DW4. Extend it by intersection,

\[
G^i\mathcal R_0
=\mathcal R_0\cap w_*G^i(w^*\mathcal R_0)
\quad\text{inside }w_*w^*\mathcal R_0.
\tag{DW5.2}
\]

This is a finite filtration and restricts to the original filtration on `W₀`. Its special-stalk filtration is induced by intersection with the generic one. Passing to the associated graded of the inclusion in (DW5.1), with the induced quotient filtration, gives

\[
0\to(\operatorname{Gr}_G^i\mathcal R_0)_{\bar t}
\to(\operatorname{Gr}_G^i\mathcal R_0)_{\bar\eta}
\to A_t^i\to0,
\tag{DW5.3}
\]

where `A_t^i` is a subquotient of `Φ_x¹`. All maps respect the local Weil action.

We compute the possible weights of `Φ_x¹`. At a boundary point of either curve factor, D4 gives coefficient weights `β+j`, `j∈Z`. At an interior point the weight is `β`. Tensoring the two factors gives local graded weights

\[
2\beta+j_1+j_2\in2\beta+\mathbb Z.
\tag{DW5.4}
\]

Tame unipotence makes those graded pieces constant on the relevant strict local open. The three calculations of DW3 add either zero or two to these weights and retain a weight-zero branch sign. Therefore every `Φ_x¹` and every `A_t^i` has all its weights in `2β+Z`.

Let the pure lisse restriction `w*Gr_G^i R₀` have weight `γ`. D4, now applied at the parameter boundary `t`, says all weights of its local generic representation lie in `γ+Z`. If `A_t^i≠0`, some eigenvalue occurs in this nonzero subquotient. Its weight belongs to both `γ+Z` and `2β+Z`. Thus

\[
\gamma-2\beta\in\mathbb Z.
\tag{DW5.5}
\]

If `A_t^i=0` for every exceptional `t`, the special-to-generic map is an isomorphism everywhere. Inertia therefore acts trivially, and the graded sheaf extends lisse across all of `A*`. The geometric projective line has trivial étale fundamental group, so this graded sheaf is geometrically constant. Its arithmetic Frobenius need not be the identity; nevertheless its geometric `H¹` is zero, since

\[
H^1(\mathbb P^1_{\overline{\mathbb F}_q},\overline{\mathbb Q}_\ell)=0.
\tag{DW5.6}
\]

We have therefore proved the exact alternative needed by (3.2.9): a nonconstant piece has weight congruent to `2β` modulo the integers, while every piece not constrained by this boundary test contributes zero to the subsequent `H¹`.

## DW6. The strict inequality and discreteness supply the decisive gain

Every pure constituent of `w*R¹f_!π*G₀` has some real weight `γ`. Evaluate it at any closed nonexceptional parameter `x`. Its fibre eigenvalues occur among those of the compact-support `H¹` of a smooth curve with coefficient of weight `2β`. Input D5 gives

\[
\gamma<2\beta+2.
\tag{DW6.1}
\]

For a nonconstant graded piece, (DW5.5) gives an integer `m=γ−2β`. Since `m<2`,

\[
\gamma\le2\beta+1.
\tag{DW6.2}
\]

This implication uses both inputs. The strict inequality alone permits weights arbitrarily close to `2β+2`; the congruence alone permits arbitrarily large integers. Their conjunction supplies the exact one-unit gain used in the product argument.

## DW7. The inductive argument, retaining the full coefficient weight

For each integer `k≥0`, consider the actual assertion

\[
\mathsf B_k:\qquad
w_q(\alpha)\le\beta+1+2^{-k}
\quad\text{on }H_c^1(U,\mathcal F),
\tag{DW7.1}
\]

for every smooth curve `U₀` and every lisse pointwise pure coefficient `F₀` of arbitrary real weight `β`. We prove all these assertions. This is the full-weight version of Deligne's (3.2.4), whose displayed proof restricts to `β=0`.

**Base case.** The Euler product in (DW1.4) is nonzero on `|t|<q^{-(β+2)/2}`. The `H_c⁰` and `H_c²` determinants have no roots in this open disk by D1. Thus the `H_c¹` determinant has no root there either, proving `w_q(α)≤β+2`. This is `B₀`.

**Extension from lisse opens.** Let `u:O₀→C₀` be a dense smooth open of a curve and `E₀` a constructible coefficient whose restriction to `O₀` is lisse pure of weight `γ`. The quotient in

\[
0\to u_!u^*\mathcal E_0\to\mathcal E_0
\to\mathcal E_0/u_!u^*\mathcal E_0\to0
\tag{DW7.2}
\]

has finite support, and hence has zero compact-support `H¹`. The long exact sequence yields a surjection

\[
H_c^1(O,u^*\mathcal E)\twoheadrightarrow H_c^1(C,\mathcal E).
\tag{DW7.3}
\]

Therefore `B_k` implies the bound `γ+1+2^{-k}` on the latter group. No claim that boundary stalks vanish is used; only their degree-one cohomology vanishes.

**Inductive step under the pencil hypotheses.** Form the full external product of DW4. The total-degree-two terms of (DW2.3) are

\[
E_2^{1,1}=H^1(A^*,\mathcal R),\qquad
E_2^{0,2}=H^0(A^*,\mathcal S),\qquad
E_2^{2,0}=H^2(A^*,R^0f_!\pi^*\mathcal G).
\tag{DW7.4}
\]

For `E₂^{1,1}`, filter `R` by (DW5.2). A geometrically constant quotient has zero `H¹` by (DW5.6). Every other quotient has generic pure weight at most `2β+1`, by DW6. Apply (DW7.3) and `B_k` to each such quotient. Long exact sequences through this finite filtration show

\[
w_q(\alpha)\le2\beta+2+2^{-k}
\quad\text{on }E_2^{1,1}.
\tag{DW7.5}
\]

For `E₂^{0,2}`, proper-support base change identifies each stalk of `R²f_!π*G₀` with a fibre's compact-support `H²`. On a dense smooth open of every fibre component the coefficient has weight `2β`, so D1 places these degree-two weights at `2β+2`; components of dimension zero contribute no `H²`. If a nonzero global eigenvector with eigenvalue `α` is evaluated at a degree-`d` closed point where it is nonzero, `α^d` is a local Frobenius eigenvalue. Such a point exists because a nonzero constructible section is nonzero on a nonempty constructible locus containing a closed point. Thus `w_q(α)=w_{q^d}(α^d)≤2β+2`. For `E₂^{2,0}`, the coefficient `R⁰f_!π*G₀` has pointwise weights at most `2β`; D1 on the base curve adds the Tate shift two. Thus

\[
w_q(\alpha)\le2\beta+2
\quad\text{on }E_2^{0,2}\text{ and }E_2^{2,0}.
\tag{DW7.6}
\]

Every total-degree-two abutment eigenvalue is an eigenvalue of a subquotient of these terms. Equations (DW7.5)–(DW7.6) therefore give

\[
w_q(\lambda)\le2\beta+2+2^{-k}
\quad\text{on }H_c^2(\widetilde V,\pi^*\mathcal G).
\tag{DW7.7}
\]

The full Künneth decomposition in degree two contains all three terms

\[
H_c^2(V,\mathcal G)
\simeq
(H_c^0(U,\mathcal F)\otimes H_c^2(U,\mathcal F))
\oplus
(H_c^1(U,\mathcal F)\otimes H_c^1(U,\mathcal F))
\oplus
(H_c^2(U,\mathcal F)\otimes H_c^0(U,\mathcal F)).
\tag{DW7.8}
\]

Combined with the blowup injection (DW2.2), its middle summand injects into the space controlled by (DW7.7). If `α` is a Frobenius eigenvalue on `H_c¹(U,F)`, choose a nonzero eigenvector over `Q̄_ℓ`; its tensor square is nonzero and has eigenvalue `α²`. Consequently

\[
2w_q(\alpha)=w_q(\alpha^2)
\le2\beta+2+2^{-k},
\quad\text{hence}\quad
w_q(\alpha)\le\beta+1+2^{-(k+1)}.
\tag{DW7.9}
\]

This is `B_{k+1}`. All product terms, the exceptional blowup term, and all Tate factors remain part of the construction; the proof uses an injection rather than declaring the other summands absent.

**Removing the auxiliary geometric hypotheses.** A finite extension `F_q⊂F_{q^d}` replaces eigenvalue `α` by `α^d` and retains its weight exactly:

\[
w_{q^d}(\alpha^d)
=2\frac{\log|\iota\alpha^d|}{\log q^d}
=w_q(\alpha).
\tag{DW7.10}
\]

Over the algebraic closure, sufficiently general embeddings and pencils with the four conditions of DW2 exist. Their finite coefficient data descend to some finite extension. A further finite extension makes every exceptional point rational. Equation (DW7.10) returns the resulting estimates to the original field without changing them.

Quasi-unipotence gives a finite surjective cover `g:U′₀→U₀`, with `U′₀` smooth, on which the pullback sheaf has tame unipotent boundary monodromy. Pullback on compact-support cohomology is injective. One way to see the injection is to use the trace (or the Poincaré-dual trace for a finite generically étale cover): trace composed with pullback is multiplication by the nonzero degree. The coefficient field has characteristic zero, so this degree is invertible. A purely inseparable factor is a universal homeomorphism and induces an equivalence on the étale cohomology involved. Thus the original cohomology is a direct summand of the cover's cohomology for the purpose of the eigenvalue bound. The pulled-back coefficient still has weight `β`, because local Frobenius eigenvalues and residue-field norms are raised to the same extension degrees. This proves `B_{k+1}` without the temporary hypotheses.

The induction is complete for every `k`. For any fixed eigenvalue `α`, if `w_q(α)>β+1`, choose `k` with `2^{-k}<w_q(α)−β−1`; this contradicts `B_k`. Therefore

\[
\boxed{w_q(\alpha)\le\beta+1\text{ on }H_c^1(U,\mathcal F).}
\tag{DW7.11}
\]

This is an exact universal conclusion from the geometrically repeatable argument, not a computation at a finite set of heights or primes.

## DW8. Curve purity by the exact duality, including the Tate factor

Let `j:U₀→X₀` be a dense open in a smooth projective curve and `F₀` lisse pointwise pure of weight `β`. The exact sequence (DW7.2), now with `E=j_*F`, gives a surjection from `H_c¹(U,F)` to `H¹(X,j_*F)`. By DW7,

\[
w_q(\alpha)\le\beta+1
\quad\text{on }H^1(X,j_*\mathcal F).
\tag{DW8.1}
\]

The curve's middle-extension duality, cited by Deligne from SGA 4½ [dualité] (1.3), (2.1), gives a perfect pairing

\[
H^1(X,j_*\mathcal F)
\otimes
H^1(X,j_*\mathcal F^\vee(1))
\longrightarrow\overline{\mathbb Q}_\ell.
\tag{DW8.2}
\]

The second coefficient has weight `−β−2`. Apply (DW8.1) to it: the inverse eigenvalue `α^{-1}` has weight at most `−β−1`. Using (DW1.2),

\[
-w_q(\alpha)\le-\beta-1,
\quad\text{so}\quad w_q(\alpha)\ge\beta+1.
\tag{DW8.3}
\]

Together with (DW8.1) this proves exact weight `β+1`. For degrees zero and two, D1 gives weights `β` and `β+2` directly. Thus the complete result (3.2.3) is

\[
\boxed{w_q(\alpha)=\beta+i
\quad\text{on }H^i(X,j_*\mathcal F).}
\tag{DW8.4}
\]

For `i=1`, this group is also the image of `H_c¹(U,F)→H¹(U,F)`. The statement is not purity of all of `H_c¹(U,F)` when boundary contributions occur; those may have lower weights. Their presence is exactly why both maps and their image are specified.

## DW9. From curves to the full direct-image theorem

We reconstruct (3.3.1): for a finite-type morphism `f:X→Y` of Deligne's separated schemes and a mixed coefficient of weights `≤n`, each `R^if_!F` is mixed of weights `≤n+i`.

The reductions are mathematically necessary and preserve the indicated degree shifts.

**Coefficient exact sequences.** From `0→F′→F→F″→0`, the segment

\[
R^{i-1}f_!\mathcal F''\to R^if_!\mathcal F'
\to R^if_!\mathcal F\to R^if_!\mathcal F''
\tag{DW9.1}
\]

shows that the required upper bound for `F′` and `F″` gives it for `F`, and the bounds for `F` and `F″` give it for `F′`. In the latter inference, the preceding term has upper weight `n+i−1≤n+i`. Direct summands inherit the bound. Mixedness and the weight bound survive subquotients and extensions because the eigenvalue multisets of filtered finite-dimensional stalks are the union of those of their graded pieces.

**Open and closed parts of the source.** For `j:U→X`, `i:S→X` its complement,

\[
0\to j_!j^*\mathcal F\to\mathcal F\to i_*i^*\mathcal F\to0
\tag{DW9.2}
\]

reduces the assertion to the two strata, by (DW9.1).

**Open and closed parts of the target.** Proper-support base change identifies the restrictions of `R^if_!F` with the corresponding direct images after each base change. A finite stratification on which those restrictions have the desired filtrations yields a finite global mixed filtration by successive extension by zero. Thus Noetherian induction on target strata is permitted.

**Composition.** If `f=g∘h`, the spectral sequence

\[
R^pg_!R^qh_!\mathcal F\Longrightarrow R^{p+q}f_!\mathcal F
\tag{DW9.3}
\]

propagates upper weight `n+p+q` to the indicated abutment degree. Every differential and subquotient is kept in that inference.

**Universal homeomorphisms.** Nilpotent reduction and purely inseparable changes induce the corresponding equivalences on étale sites; the coefficient and compact-support cohomology statements are unchanged. This is a cited property of étale cohomology, not an assertion about arbitrary topological maps.

**Relative dimension zero.** A geometric fibre is finite, so its compact-support cohomology is concentrated in degree zero. A point of residue degree `d` over a closed target point contributes an induced Frobenius block whose `d`th power has the source eigenvalues. If the latter have modulus `(N(y)^d)^{n/2}`, the block eigenvalues have modulus `N(y)^{n/2}`. Thus `f_!` preserves the coefficient's pure weight, and higher `R^if_!` vanish. Apply coefficient devissage for mixed coefficients.

Stratification and Noether normalization allow a finite-type morphism to be factored on strata into relative-dimension-zero maps and successive relative-dimension-one projections. Repeated use of (DW9.2)–(DW9.3) therefore reduces the theorem to relative dimension one. Further coefficient and source stratification make the coefficient lisse and pointwise pure of weight `n`.

On a generic fibre, after a finite purely inseparable extension if necessary, remove finitely many points to obtain a smooth curve. A finite cover makes the boundary ramification tame, and its compactification is a smooth projective curve with finite étale boundary after shrinking the base. Trace splits the coefficient as a direct summand of the finite cover's pushforward. These constructions spread from the generic fibre to an open neighbourhood by finite presentation. Target Noetherian induction, universal-homeomorphism invariance, the relative-dimension-zero case, and the direct-summand reduction therefore yield the actual remaining geometric situation:

\[
X\xrightarrow{j}\overline X\xleftarrow{i}D,
\qquad\overline f:\overline X\to Y
\tag{DW9.4}
\]

with `f= f̄∘j`, `f̄` smooth projective of pure relative dimension one, `D→Y` finite étale, and `F` lisse of weight `n` on `X`, tame at `D`. These geometric reductions are the ones in Deligne's (3.3.1), article p.205; their finite-cover and compactification existence is part of the upstream algebraic-geometric apparatus.

Now retain the full boundary sequence

\[
0\to j_!\mathcal F\to j_*\mathcal F
\to i_*i^*j_*\mathcal F\to0.
\tag{DW9.5}
\]

The formation of `j_*F`, its boundary monodromy filtration, and the corresponding proper direct images is compatible with the fibres in this tame smooth-relative-curve situation. Applying DW8 to each closed fibre shows that

\[
R^r\overline f_*j_*\mathcal F
\text{ is pointwise pure of weight }n+r.
\tag{DW9.6}
\]

By D4, the induced monodromy filtration on `i*j_*F` has graded pieces of weights `n+k`, zero for `k>0`. Its finite direct image along `f̄i` is therefore mixed of weights at most `n`, and has no higher direct images. Apply `R f̄_*` to (DW9.5). For degree zero, `R⁰f_!F` is a subsheaf of the weight-`n` term in (DW9.6). For degree one, the only extra contribution is a quotient of the weight-`≤n` boundary pushforward followed by a subobject of the pure weight-`n+1` term. In degrees at least two, the boundary has no degree `r−1` or `r` direct image, so the desired comparison is an isomorphism. In every degree the result is mixed of weights `≤n+r`. All reductions then prove (3.3.1).

The identical argument with the retained real coefficient weight `β` proves the `ι`-mixed version (3.3.10). Its weights are at most `β+i` and congruent modulo `Z` to one of the original coefficient weights. This congruence persists through each local monodromy shift, the product calculation, duality, and the integral cohomological degree shifts.

## DW10. Lower weights, integrality, and smooth/proper purity

The upper direct-image theorem specializes at `Y=Spec(F_q)` to

\[
H_c^i(X,\mathcal F)\text{ mixed of weights }\le n+i
\tag{DW10.1}
\]

for a coefficient mixed of weights `≤n`.

There are two distinct ways lower information enters Deligne's §3.3; neither is silently substituted for the other.

**Algebraic-integrality lower bound, (3.3.2)–(3.3.4).** If a nonzero algebraic integer `α` is pure of integral weight `w` relative to `q`, and has degree `d`, the absolute value of its norm is

\[
|N_{\mathbb Q(\alpha)/\mathbb Q}(\alpha)|
=\prod_{\sigma}|\sigma(\alpha)|=q^{wd/2}.
\tag{DW10.2}
\]

Its norm is a nonzero integer, hence has absolute value at least one; since `q>1`, `w≥0`. SGA 7 XXI (5.2.2), as explicitly cited by Deligne, gives integrality of `R^if_!F` and, above the maximal fibre dimension `d_X`, of `R^if_!F(i−d_X)`. The second conclusion retains the geometric Frobenius multiplier `N(y)^{-(i−d_X)}` and forces

\[
w\ge 2(i-d_X)\quad(i>d_X).
\tag{DW10.3}
\]

Together with DW9 these give all intervals in (3.3.3)–(3.3.4). This arithmetic integrality is not merely the statement that the weight label belongs to `Z`; it is the stronger assertion that eigenvalues are algebraic integers, used through their norm.

**Poincaré-duality lower bound, (3.3.5).** Suppose `X₀` is smooth of pure dimension `N` and `F₀` is lisse mixed of weights `≥n`. Its dual has weights `≤−n`. Apply (DW10.1) in degree `2N−i` and retain the Tate twist:

\[
H_c^{2N-i}(X,\mathcal F^\vee)(N)
\text{ has weights }\le
-n+(2N-i)-2N=-n-i.
\tag{DW10.4}
\]

Poincaré duality identifies `H^i(X,F)` with the dual of that vector space. Inverting eigenvalues negates their weights, proving

\[
H^i(X,\mathcal F)\text{ mixed of weights }\ge n+i.
\tag{DW10.5}
\]

When `F₀` is pure of weight `n`, the image of `H_c^i→H^i` is a quotient of a space of weights `≤n+i` and a subspace of one of weights `≥n+i`. Its every eigenvalue has exactly weight `n+i`, proving (3.3.6).

If `X₀` is also proper, compact and ordinary cohomology coincide. Thus for every eigenvalue, with no discarded boundary contribution,

\[
\boxed{|\iota\alpha|=q^{(n+i)/2}.}
\tag{DW10.6}
\]

For the constant coefficient `Q̄_ℓ`, `n=0`, hence `H^i` has weight `i`. We now give the additional descent of characteristic polynomials, corresponding to Deligne's citation of the Weil I argument (1.7)⇒(1.6). Run the purity proof for every isomorphism `ι:Q̄_ℓ→C`. Every eigenvalue is algebraic: a transcendental element could be sent by such field isomorphisms to transcendental numbers of different absolute values, contradicting its fixed required modulus. All its algebraic conjugates have that same weight. Set `P_i(t)=det(1−Ft,H^i(X,Q̄_ℓ))`; their coefficients are therefore algebraic. Their reciprocal roots have mutually distinct moduli `q^{i/2}` as `i` varies, so no two `P_i` have a common root.

The full trace formula gives

\[
Z(X_0,t)=\prod_{x\in|X_0|}(1-t^{d(x)})^{-1}
=\prod_i P_i(t)^{(-1)^{i+1}}.
\tag{DW10.6a}
\]

The left side has integer Taylor coefficients and constant term one. The right side is rational over an algebraic number field. Its expression as a ratio of coprime polynomials with constant terms one is unique; applying any automorphism of `Q̄/Q` leaves the Taylor coefficients fixed, and hence leaves that rational function and its coprime numerator and denominator fixed. Both polynomials therefore lie in `Q[t]`. Each `P_i` is recovered from this coprime rational function by collecting the root multiset of modulus `q^{-i/2}`, with its numerator or denominator sign already given by `(-1)^{i+1}`. Since every conjugate of such a root retains that modulus, this multiset is Galois-stable and `P_i∈Q[t]`. The integrality theorem cited above applies to the integral constant coefficient and says the Frobenius eigenvalues are algebraic integers. Their elementary symmetric polynomials are then algebraic integers; being rational, they belong to `Z`. Hence `P_i∈Z[t]`. Finally (DW10.6a), including its closed-point factors, is independent of `ℓ`, and its unique decomposition by the distinct root moduli gives the same `P_i` for every `ℓ≠p`.

The exact polynomial convention in (3.3.9) is

\[
\det(t\,1-F^*,H^i(X,\overline{\mathbb Q}_\ell))\in\mathbb Z[t],
\tag{DW10.7}
\]

with roots of modulus `q^{i/2}`. The inverse-root polynomial `det(1-F*t)` retains the opposite root radius.

For completeness, the slope description in (3.3.7)–(3.3.8) retains the normalization explicitly: for every `p`-adic valuation satisfying `v(q)=1`, put

\[
(r,s)=\bigl(v(\alpha),v(q^w\alpha^{-1})\bigr),
\qquad r+s=w.
\tag{DW10.8}
\]

When the coefficient is constant and `dim X≤d`, integrality of the eigenvalue and its paired complex-conjugate algebraic number gives `r,s≥0`. For compact-support degree `i`, (DW10.3) applied to the twist gives `r,s≥max(0,i−d)`, while `r+s≤i`. For smooth ordinary degree `i`, duality sends a compact-support pair `(r′,s′)` in degree `2d−i` to `(d−r′,d−s′)`. Consequently `r,s≤min(i,d)` and `r+s≥i`. These are the lower and upper triangles of Deligne's diagram. The stronger assertion mentioned after the diagram that ordinary cohomology lies in the union square is not needed here and is not claimed as newly proved by this argument.

In (3.3.11), smoothness can be replaced in the duality step by the exact rational-homology-manifold identity

\[
Ra^!\overline{\mathbb Q}_\ell
\simeq\overline{\mathbb Q}_\ell(N)[2N]
\tag{DW10.9}
\]

for `a:X₀→Spec(F_q)`. It is this identity, with its `N` and `2N`, that supplies the same pairing and therefore the same lower-weight computation. No mere resemblance of a supporting point supplies this dualizing-complex identity.

## DW11. The mechanism and the exact roles of its data

The established chain of maps and estimates is

\[
\begin{gathered}
\mathcal F_0
\longmapsto\mathcal F_0\boxtimes\mathcal F_0
\longmapsto R^1f_!\pi^*(\mathcal F_0\boxtimes\mathcal F_0),\\
\text{real companion}\longmapsto\text{pure constituents},\\
\text{local monodromy and three vanishing-cycle computations}
\longmapsto\gamma\in2\beta+\mathbb Z\text{ for every nonconstant piece},\\
\gamma<2\beta+2\longmapsto\gamma\le2\beta+1,\\
H_c^1\otimes H_c^1\hookrightarrow H_c^2(\widetilde V)
\longmapsto
2w_q(\alpha)\le2\beta+2+2^{-k},\\
\forall k\longmapsto w_q(\alpha)\le\beta+1,\\
\text{duality with }\mathcal F_0^\vee(1)
\longmapsto w_q(\alpha)\ge\beta+1.
\end{gathered}
\tag{DW11.1}
\]

The final circle is an eigenvalue-modulus conclusion. Its radius is determined by the coefficient weight, cohomological degree and residue-field norm. In this proof, weight zero of a coefficient is a quantitative statement about Frobenius eigenvalues; the zero sheaf is a different object; a geometric generic point is a supporting point; and a centre of a complex circle is a feature of the complex absolute-value realization. Their occurrences are given by the maps above, and no replacement between those roles has been asserted.

The detailed source proof therefore provides concrete operations for a subsequent programme comparison: external tensor product with all original coefficients; compact-support direct image over a projective-line pencil; the three boundary cycle maps with their signs and Tate factors; a filtration with proven local weight congruences; the strict boundary nonvanishing input; and the exact duality pairing. This file establishes the finite-field composition, with its full input hypotheses. Any further programme calculation must state and prove its maps to these particular objects rather than naming the final modulus relation as an additional assumption.
