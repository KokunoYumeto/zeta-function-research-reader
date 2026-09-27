# Rotations, boosts and the Apollonian group: the modular flow of the Erdős–Straus paper and a thin group

*Claude (Anthropic, model `claude-opus-5-5`), 27 September 2026. A companion note to the Erdős–Straus paper (version 4): it answers the question that paper raises about the rotations and boosts of its Proposition 8.3. In the condensed version of that paper the same statements are Proposition 8.3, §12.4 and Question 11. Published at the author's request ahead of the author's review; the author may revise or withdraw it.*

## Abstract

Proposition 8.3 of the Erdős–Straus paper shows how the modular flow of a faithful state on M₂(ℂ) relates to the Lorentz boost used in the author's notes. The flow is the compact real form, and the boost the non-compact real form, of one complex one-parameter subgroup z ↦ H\_r^z of SL₂(ℂ), acting on 2×2 Hermitian matrices, a model of Minkowski space. The Apollonian group A acts on the same Minkowski space through the Descartes form, and it is the standard example of a thin group. That paper asks which rotations and boosts meet A, and how.

This note answers the question.

- **Rotations.** The compact real form never meets A. The group A meets every compact subgroup of SO\_F(ℝ) only in the identity: its orientation-preserving part A ∩ SO\_F(ℝ) is torsion-free, while its four generating reflections have determinant −1 and lie outside SO\_F(ℝ). In particular, under any identification of the Descartes space with Hermitian matrices, no element of A is a modular automorphism of a faithful state.
- **Boosts in circle stabilizers.** The non-compact real form meets A in two ways. First, the stabilizer of each circle of a packing is a congruence group; in the strip packing it is the image of Γ⁰(4) in PSL₂(ℤ). Every nontrivial element of a circle stabilizer is a boost or parabolic. Sarnak's binary quadratic forms are attached to these circles, and both the positive-density theorem and the disproof of the local–global conjecture run through them.
- **Boosts attached to no circle.** Second, there are boosts that fix no circle of the packing. An example is S₁S₂S₁S₃S₄S₃, with trace −18 and rapidity 2 arccosh 9. A criterion on words identifies all of them.
- **Screws.** Every other loxodromic element is a screw motion, a boost combined with a rotation about the same axis. Its rotation angle is an irrational multiple of 2π. It follows that a boost one-parameter group meets A exactly when it contains a boost of A.
- **Lattices.** The complex one-parameter group through each primitive element meets A in a lattice of the complex plane. The lattice is spanned by the rotation period and the complex length of the element, and these two are orthogonal exactly for boosts.

A census of the 51,050 primitive conjugacy classes of word length at most 12 gives the proportions. All statements are proved in the text or checked by the included program. Results cited from the literature carry their references.

## 0. Introduction

### 0.1 Why this note

The author's notes on the Erdős–Straus problem contain a section titled *Finite-dimensional modular flow as a Lorentz boost*. Proposition 8.3 of the Erdős–Straus paper made that section's relation precise. Take the density H\_r = diag(e^r, e^{−r}) and act on Hermitian matrices X by X ↦ H\_r^z X H\_r^{z̄}. At imaginary z = it this is the modular automorphism group of the state with density proportional to H\_r, a rotation of Minkowski space. At real z = s it is the boost of the author's section. The two are the two real forms of the complex one-parameter group z ↦ H\_r^z.

The same Minkowski space carries the Descartes form F(x) = 2Σxᵢ² − (Σxᵢ)², the quadratic form of Descartes' circle theorem. The Apollonian group A, which generates Apollonian circle packings, is a subgroup of the integral orthogonal group O\_F(ℤ). It has infinite index in O\_F(ℤ) and is Zariski dense in O\_F [Sa, SaL], which is what makes it a thin group.

That paper asked how the rotations and boosts of its Proposition 8.3 sit relative to this thin group. The question has a complete answer, and the answer separates the two real forms sharply. The answer also shows where the known arithmetic of Apollonian packings sits in this picture.

### 0.2 Main results

The results are stated for the Apollonian group A = ⟨S₁, S₂, S₃, S₄⟩ acting on ℝ⁴ with the form F, and for its orientation-preserving subgroup A⁺. Section 1 gives an explicit model in SL₂(ℤ[i]) for the strip packing, in which A⁺ acts on the Riemann sphere by Möbius transformations. In that model the classes of elements are named as follows:

- **boost:** real trace t with |t| > 2;
- **parabolic:** t = ±2;
- **screw motion:** t not real;
- **rotation:** real t with |t| < 2.

1. **Structure** (Theorem 2.2). A is the free product of four groups of order 2. The stabilizer of the i-th circle vector is A\_i = ⟨S\_j : j ≠ i⟩. A⁺ is torsion-free. An element of A⁺ fixes a circle of the packing if and only if its cyclically reduced word omits one of the four letters (Corollary 2.4).
2. **Rotations** (Theorem 3.1, Corollary 3.2). A meets every compact subgroup of SO\_F(ℝ) only in the identity. In particular, no nontrivial element of A is a modular automorphism of a faithful state of M₂(ℂ). This holds under any identification of (ℝ⁴, F) with the Hermitian matrices and their determinant.
3. **Boosts in circle stabilizers** (Theorem 4.1). In the strip packing, the orientation-preserving stabilizer of the line Im z = 1 acts on the upper half-plane as the image of Γ⁰(4) = {(a b; c d) ∈ SL₂(ℤ) : b ≡ 0 mod 4} in PSL₂(ℤ). This group is conjugate to Γ(2).
   - All its nontrivial elements are boosts or parabolic.
   - The boosts have traces ±(4k + 2), k ≥ 1; every such trace occurs, and the rapidity is 2 arccosh(2k + 1).
   - Every circle stabilizer is conjugate to this group.
4. **Boosts attached to no circle** (Theorem 4.2, Proposition 4.3). The element S₁S₂S₁S₃S₄S₃ is a boost with trace −18 and rapidity 2 arccosh 9. It is the product of the reflections in two disjoint dual circles.
   - It fixes no circle of the packing. Equivalently, no circle of the packing passes through both of its fixed points.
   - It belongs to an infinite family of such boosts, (S₁S₂)ᵏS₁S₃S₄S₃ with trace (−1)ᵏ(12k + 6), k ≥ 1.
   - Not every boost is a product of two reflections: S₁S₂S₁S₂S₃S₁S₂S₃ (trace −34) is not.
5. **Screws and lattices** (Theorems 5.1 and 5.2, Corollary 5.3).
   - The rotation angle of every screw motion in A⁺ is an irrational multiple of 2π; so no power of a screw is a boost.
   - For each pair of points p ≠ q, the complex one-parameter group fixing p and q is a conjugate of z ↦ H\_r^z, and A⁺ meets it trivially or in an infinite cyclic group.
   - In the second case, writing the group as z ↦ gH\_r^zg⁻¹, the parameters z with gH\_r^zg⁻¹ ∈ A⁺ form a lattice ℤz₀ ⊕ ℤ(πi/r) in ℂ, with modulus τ = (−θ + iℓ)/2π, where ℓ + iθ is the complex length of the generator.
   - The rotation direction of this lattice contains only the trivial parameters. The boost direction contains nontrivial parameters exactly when the generator is a boost, in which case τ is purely imaginary. For screw motions, Re τ is irrational.
6. **Orbits on integral packings** (Proposition 5.4). Along the orbit of a boost, the curvatures are αe^{nℓ} + α′e^{−nℓ} + β. Along the orbit of a screw motion the constant β is replaced by a bounded oscillation βcos nθ + β′sin nθ with θ/2π irrational, which, when nonzero, is never periodic.
7. **Census** (Section 6). Among the 51,050 primitive conjugacy classes of A⁺ of word length at most 12:
   - 6 are parabolic;
   - 1,904 are boosts in circle stabilizers;
   - 2,274 are boosts attached to no circle;
   - 46,866 are screw motions;
   - none is a rotation.

### 0.3 What the results mean

The modular flow of Proposition 8.3 is the rotation part, and the note's boost the translation part, of one complex one-parameter group. Every loxodromic element of the Apollonian group lies in exactly one such group, the one fixing its two fixed points. There it is the value at a complex parameter z₀, unique modulo the kernel. The imaginary part of 2rz₀ is the rotation angle θ, the holonomy, and the real part is the rapidity ℓ. The results say how these two parts are distributed over a thin group.

- **Rotation part.** A pure rotation never occurs. The rotation part is nonetheless present in every screw motion, as an irrational holonomy, and by the next item the screw motions are all but a density-zero set of the primitive elements. In integral packings it is visible as a bounded oscillation of curvatures that never repeats.
- **Holonomy equidistributes.** By a theorem of Margulis, Mohammadi and Oh [MMO], the holonomies of closed geodesics equidistribute for Zariski-dense geometrically finite groups such as A⁺. So the pure boosts, the elements with holonomy zero, have density zero when the primitive elements are ordered by length (Section 8.1).
- **Where the arithmetic lives.** The known arithmetic of Apollonian packings lives on the density-zero boost slice. Sarnak's binary quadratic forms, the positive-density theorem of Bourgain and Fuchs, and the reciprocity obstructions of Haag, Kertzer, Rickards and Stange all run through the circles of the packing and the forms attached to them [SaL, Sa, BF, HKRS]. The symmetry groups of these circles are the circle stabilizers, which Theorem 4.1 identifies as congruence groups made entirely of boosts and parabolic elements.
- **An open question.** The boost slice also contains elements attached to no circle, and in the census they are as numerous as the circle-stabilizer boosts. Whether they carry arithmetic of their own is Question 1.

### 0.4 How this note was made

Every statement has one of four statuses:

- **verified:** proved in the text, or checked by the program `checks/apollonian/apollonian_real_forms.py` (95 checks, all passing; Section 10);
- **cited:** proved in the literature at the reference given;
- **my assessment:** a view with its reasons, in the first person;
- **proved negative:** a statement shown false, with the counterexample.

The group theory in Section 2 is elementary and is proved in full. The identification of circle stabilizers as arithmetic groups is due to Sarnak [Sa]; Theorem 4.1 makes it explicit for the strip packing. The facts from the geometry of Kleinian groups used in Section 5 (Cartan subgroups, complex length, the torus quotient) are standard and are proved where they are used.

### 0.5 Organization

- Part A (Sections 1–6) contains the results with proofs.
- Part B (Section 7) collects the negative results.
- Part C (Section 8) discusses the bridges to the literature and the directions they suggest, with my assessments labelled.
- Section 9 lists open questions, Section 10 the verification, and Section 11 the references.

## Part A. Results

## 1. The setting and an explicit spin model

### 1.1 The Descartes form and the Apollonian group

Let Q = 2I − J, where J is the 4×4 matrix of ones, and let B(x, y) = xᵀQy, so that F(x) = B(x, x) = 2Σxᵢ² − (Σxᵢ)². Q has the eigenvalue −2 on (1,1,1,1) and the eigenvalue 2 on its Euclidean orthogonal complement, so F has signature (3,1). Let e₁, …, e₄ be the standard basis. Then B(eᵢ, eᵢ) = 1 and B(eᵢ, eⱼ) = −1 for i ≠ j.

The Apollonian generators are the reflections

  Sᵢx = x − 2B(x, eᵢ)eᵢ, that is, (Sᵢx)ᵢ = 2Σ\_{j≠i} xⱼ − xᵢ, and the other coordinates are unchanged.

They preserve F, are involutions and have determinant −1 (check §1). The Apollonian group is A = ⟨S₁, S₂, S₃, S₄⟩ ⊂ O\_F(ℤ). Since each eᵢ is spacelike, each Sᵢ preserves the two sheets of {F < 0}, so A lies in the time-orientation-preserving group O⁺\_F(ℝ). The subgroup A⁺ = A ∩ SO\_F(ℝ) consists of the products of an even number of generators.

The *circle vectors* are cᵢ = Q⁻¹eᵢ = eᵢ/2 − (1,1,1,1)/4. They form the dual basis to the eᵢ: B(eⱼ, cᵢ) = δᵢⱼ, and so B(x, cᵢ) = xᵢ for every x. Moreover F(cᵢ) = 1/4, and Sⱼcᵢ = cᵢ for j ≠ i (check §3). The name is justified by Proposition 1.1(b).

### 1.2 The strip packing

Take the four mutually tangent circles

- C₁: Im z = 1;
- C₂: Im z = −1;
- C₃: |z| = 1;
- C₄: |z − 2| = 1.

Their curvatures are (0, 0, 1, 1). Write each oriented circle as a Hermitian matrix H with zero set (z̄, 1)H(z, 1)ᵀ = 0, normalized by det H = −1 and oriented so that the four interiors are disjoint:

  H₁ = (0 −i; i 2), H₂ = (0 i; −i 2), H₃ = (1 0; 0 −1), H₄ = (1 −2; −2 3).

The dual circle Dᵢ passes through the three tangency points of the circles Cⱼ, j ≠ i:

- D₁: |z − (1 − i)| = 1;
- D₂: |z − (1 + i)| = 1;
- D₃: Re z = 2;
- D₄: Re z = 0.

Let gᵢ be the reflection (inversion) in Dᵢ. It is the anti-Möbius map gᵢ(z) = Mᵢ·z̄ with

  M₁ = (1+i −i; i 1−i), M₂ = (−1+i −i; i −1−i), M₃ = (−i 4i; 0 i), M₄ = (−i 0; 0 i),

all in SL₂(ℤ[i]). An anti-Möbius map g(z) = M·z̄ sends the circle H to the circle Λ\_g(H) = (M⁻¹)∗ H̄ M⁻¹, and Λ\_{g∘h} = Λ\_g Λ\_h. The *strip packing* P is the set of all circles g(Cᵢ) for g in G = ⟨g₁, g₂, g₃, g₄⟩.

**Proposition 1.1 (the spin model).** Let Ψ(x) = Σₖ (Qx)ₖ Hₖ.

- (a) Ψ is a linear isomorphism of ℝ⁴ onto the 2×2 Hermitian matrices, with det Ψ(x) = −4F(x).
- (b) Ψ(cᵢ) = Hᵢ.
- (c) Λ\_{gᵢ} ∘ Ψ = Ψ ∘ Sᵢ for each i.

Consequently Sᵢ ↦ gᵢ extends to an isomorphism A → G with Λ\_{g} = ΨS\_gΨ⁻¹. The circles of the packing are the images Ψ(h cᵢ), h ∈ A. The orientation-preserving subgroup A⁺ corresponds to the Möbius transformations z ↦ N\_w·z with

  N\_w = M\_{a₁} M̄\_{a₂} M\_{a₃} M̄\_{a₄} ⋯ M̄\_{a₂ₖ} ∈ SL₂(ℤ[i])

for the even word w = S\_{a₁}S\_{a₂}⋯S\_{a₂ₖ}.

*Status: verified; the finite identities are checked exactly in §4 of the program.*

*Proof.* Part (b) holds because Qcᵢ = eᵢ. The polarized determinant ⟨X, Y⟩ = ½(det(X+Y) − det X − det Y) takes the values ⟨Hⱼ, Hₖ⟩ = −Qⱼₖ on the four matrices, an exact computation. Since Q² = 4I, this gives ⟨Ψ(x), Ψ(y)⟩ = −(Qx)ᵀQ(Qy) = −4xᵀQy. So Ψ is an isomorphism, the Gram matrix −Q being nondegenerate, and det Ψ(x) = −4F(x); this is (a).

For (c), an exact computation with the matrices above gives Λ\_{gᵢ}(Hⱼ) = Hⱼ for j ≠ i and Λ\_{gᵢ}(Hᵢ) = 2Σ\_{j≠i}Hⱼ − Hᵢ. That is, Λ\_{gᵢ}(Hⱼ) = Σₖ(Sᵢ)ⱼₖHₖ, and therefore

  Λ\_{gᵢ}Ψ(x) = Σⱼ(Qx)ⱼ Σₖ(Sᵢ)ⱼₖHₖ = Σₖ(SᵢᵀQx)ₖHₖ = Σₖ(QSᵢx)ₖHₖ = Ψ(Sᵢx).

Here SᵢᵀQ = QSᵢ follows from SᵢᵀQSᵢ = Q and Sᵢ² = I.

Since Λ is faithful, Λ\_g = id only for g = id, and the word map is an isomorphism. The composition rule (M·z̄)∘(M′·z̄) = (MM̄′)·z gives the matrices N\_w. ∎

**Lemma 1.2 (traces).** Let N ∈ SL₂(ℂ) be diagonalizable with eigenvalues μ^{±1}. Then the real-linear map X ↦ NXN∗ of the Hermitian matrices has the eigenvalues |μ|², |μ|⁻², μ/μ̄ and μ̄/μ.

- Its trace is |tr N|².
- Its characteristic polynomial is (x² − px + 1)(x² − qx + 1), with p = 2cosh ℓ, q = 2cos θ, e^ℓ = |μ|² and θ = 2 arg μ.
- In terms of t = tr N = x + iy, its trace is a = x² + y² and its second coefficient is b = 2(x² − y²) − 2.
- For parabolic N all four eigenvalues are 1.

*Status: verified.*

*Proof.* The complexification of the space of Hermitian matrices is M₂(ℂ), and the complexified map is X ↦ NXN∗, whose eigenvalues are the products λ\_aλ̄\_b of eigenvalues of N and N̄. Hence tr = tr N · tr N̄ = |t|². The products give p = |μ|² + |μ|⁻² and q = μ/μ̄ + μ̄/μ = 2cos(2 arg μ). The second coefficient is b = 2 + pq. With μ = e^{(ℓ+iθ)/2}, 2Re(t²) = 2Re(μ² + μ⁻²) + 4 = pq + 4, so b = 2Re(t²) − 2 = 2(x² − y²) − 2. ∎

By Proposition 1.1 and Lemma 1.2, a nontrivial γ ∈ A⁺ with SL₂-trace t is:

- a *rotation* (elliptic) if t is real with |t| < 2;
- *parabolic* if t = ±2;
- a *boost* (pure hyperbolic) if t is real with |t| > 2;
- a *screw motion* (loxodromic, not a boost) if t is not real.

The rapidity ℓ and the rotation angle, or *holonomy*, θ are those of Lemma 1.2. On the 4×4 side the classes read as follows: γ is a boost or parabolic exactly when b = 2a − 2, since then q = 2. In the notation of Proposition 8.3 of the Erdős–Straus paper, H\_r^z with 2rz = ℓ + iθ has rapidity ℓ and rotation angle θ.

## 2. Structure of the Apollonian group

**Lemma 2.1 (height).** Let a₁, a₂, … be indices in {1, 2, 3, 4} with a\_k ≠ a\_{k+1}. Put y⁽⁰⁾ = (1,1,1,1) and y⁽ᵏ⁾ = S\_{a\_k}y⁽ᵏ⁻¹⁾. Then for every k ≥ 1:

- all entries of y⁽ᵏ⁾ are positive integers;
- the new entry y⁽ᵏ⁾\_{a\_k} exceeds max y⁽ᵏ⁻¹⁾;
- it is the strict maximum of y⁽ᵏ⁾.

*Status: verified (proof; check §2 tests all words of length at most 10).*

*Proof.* For k = 1 the new entry is 2·3 − 1 = 5. For k ≥ 2, the new entry is 2Σ\_{j≠a\_k}y⁽ᵏ⁻¹⁾ⱼ − y⁽ᵏ⁻¹⁾\_{a\_k}. Because a\_{k−1} ≠ a\_k, the sum contains M = y⁽ᵏ⁻¹⁾\_{a\_{k−1}}, which is the maximum of y⁽ᵏ⁻¹⁾ by induction, and two further entries that are at least 1. So the new entry is at least 2(M + 2) − M = M + 4 > M. ∎

**Theorem 2.2 (structure).**

- (a) A is the free product of the four groups ⟨Sᵢ⟩ of order 2: a nonempty reduced word in the Sᵢ is never the identity.
- (b) The stabilizer of cᵢ in A is Aᵢ = ⟨Sⱼ : j ≠ i⟩.
- (c) Every element of finite order other than 1 is conjugate to some Sᵢ. A⁺ is torsion-free and is generated by S₁S₄, S₂S₄ and S₃S₄.

*Status: verified (proof below).*

(a) is the standard fact that A is the Coxeter group with no relations besides Sᵢ² = 1, the reflection group of four pairwise tangent planes [Vi]. The proof here is elementary. Sarnak observes that the Aᵢ are arithmetic in their Zariski closures [Sa]; Theorem 4.1 makes this explicit.

*Proof.* (a) A nonempty reduced word maps (1,1,1,1) to a vector whose entries sum to more than 4, by Lemma 2.1, so it is not the identity.

(b) Suppose gc₁ = c₁. Then (gx)₁ = B(gx, c₁) = B(gx, gc₁) = B(x, c₁) = x₁ for all x. Apply this to x = (1,1,1,1) and the reduced word of g, read from right to left.

- If S₁ occurs, then at its first occurrence the first entry becomes larger than the maximum so far, which is at least 1.
- Afterwards the first entry changes only at later occurrences of S₁, and each time it becomes larger than the current maximum, hence larger than its previous value (Lemma 2.1).

So the first entry ends above 1, a contradiction. Hence S₁ does not occur and g ∈ A₁. Conversely, A₁ fixes c₁ by §1.1.

(c) By Lemma 2.3(i) every element is conjugate to a cyclically reduced word w. If |w| ≥ 2, the powers wⁿ are reduced words of length n|w|, since the last letter of w differs from the first; so w has infinite order. Hence the elements of finite order other than 1 are the conjugates of the Sᵢ, which have determinant −1 and do not lie in A⁺. Finally, A⁺ is generated by the products S\_aS\_b = (S\_aS₄)(S\_bS₄)⁻¹. ∎

**Lemma 2.3 (conjugacy).**

- (i) Every element of A is conjugate to one whose reduced word is cyclically reduced: of length at most 1, or with first letter different from last letter.
- (ii) Let u be cyclically reduced with |u| ≥ 2 and let g ∈ A. Then the reduced word of gug⁻¹ is xvx⁻¹, reduced as written, where v is a cyclic permutation of u.
- (iii) Two cyclically reduced words of length at least 2 are conjugate in A if and only if they are cyclic permutations of each other.

*Status: verified (proof).*

*Proof.* (i) If the first and last letters agree, conjugating by that letter shortens the word by 2.

(ii) Induct on the length of g. Suppose the claim holds for g, and multiply by a letter s on both sides, obtaining s·xvx⁻¹·s. Each letter is its own inverse, so x⁻¹ is x reversed.

1. x is nonempty and begins with s: the product is x′vx′⁻¹ with x = sx′.
2. x is nonempty and does not begin with s: sxvx⁻¹s is reduced as written.
3. x is empty. Then v, being cyclically reduced, cannot begin and end with s.
   - If v begins with s, then svs = v′s with v = sv′, a cyclic permutation of v.
   - If v ends with s, the case is symmetric.
   - Otherwise svs is reduced with x = s.

(iii) Suppose v′ = gug⁻¹ with v′ cyclically reduced. By (ii), v′ = xvx⁻¹ as reduced words. If x were nonempty, v′ would begin and end with the first letter of x; so x is empty and v′ = v. ∎

**Corollary 2.4 (which elements fix a circle).** Let γ ∈ A⁺, γ ≠ 1, and let w be a cyclically reduced word conjugate to γ. Then γ fixes an oriented circle of the packing if and only if w omits one of the four letters. Fixing an oriented circle means fixing its Hermitian matrix.

For a boost, fixing a circle as a set is the same thing. It is also equivalent to the circle passing through both fixed points of γ: a boost z ↦ λz with λ > 1 preserves exactly the lines through 0, with their orientations.

*Status: verified (proof).*

*Proof.* By Proposition 1.1, γ fixes the circle Ψ(hcᵢ) exactly when S\_γhcᵢ = hcᵢ, that is, when h⁻¹γh ∈ Stab(cᵢ) = Aᵢ (Theorem 2.2(b)).

- If w omits Sᵢ, then w ∈ Aᵢ. Writing γ = hwh⁻¹, γ fixes hcᵢ, that is, the circle Ψ(hcᵢ).
- Conversely, suppose h⁻¹γh = a ∈ Aᵢ. Cyclically reduce a inside Aᵢ, which keeps it in Aᵢ, to a word a′ of length at least 2; the length is at least 2 because a′ is even and nontrivial. By Lemma 2.3(iii), w is a cyclic permutation of a′, so w omits Sᵢ. ∎

## 3. The compact real form: no rotations

**Theorem 3.1.** For every compact subgroup K of SO\_F(ℝ), K ∩ A = {1}. In particular, A meets every compact one-parameter subgroup, a group of rotations about a timelike axis, only in the identity.

*Status: verified (proof).*

*Proof.* A ⊂ GL₄(ℤ) is discrete, so K ∩ A is finite. Its elements have finite order and lie in A ∩ SO\_F = A⁺, which is torsion-free by Theorem 2.2(c). ∎

**Corollary 3.2 (modular flows).** Let φ(X) = tr(ρX) be a faithful state on M₂(ℂ). Its modular automorphism group is σ\_t(X) = ρ^{it}Xρ^{−it}; for ρ ∝ H\_r this is Proposition 8.3(a) of the Erdős–Straus paper. Let ι be any linear isomorphism of ℝ⁴ onto the Hermitian matrices with det∘ι = −cF, c > 0; Ψ is one example. Then ι⁻¹σ\_tι ∉ A whenever σ\_t ≠ id.

*Status: verified (proof).*

*Proof.* ρ^{it} is unitary, so σ\_t acts on the Hermitian matrices through the compact group {X ↦ uXu∗ : u ∈ U(2)}, which preserves det. Transported by ι, this is a compact subgroup of SO\_F(ℝ), and Theorem 3.1 applies. ∎

The same holds for every conjugate of the rotation form of Proposition 8.3 by SL₂(ℂ), since such conjugates are again compact.

## 4. The non-compact real form: boosts

### 4.1 Circle stabilizers are congruence groups

**Theorem 4.1.** Let G₁⁺ be the orientation-preserving stabilizer of C₁ in the strip model, the image of A₁⁺ = A₁ ∩ A⁺. In the coordinate u = z − i, which moves C₁ to the real axis and its interior to the upper half-plane, G₁⁺ is the image in PSL₂(ℤ) of

  Γ⁰(4) = {(a b; c d) ∈ SL₂(ℤ) : b ≡ 0 mod 4},

and Γ⁰(4) = diag(2,1) Γ(2) diag(2,1)⁻¹.

- (a) Every nontrivial element of G₁⁺ is a boost or parabolic.
- (b) The traces of its boosts are exactly the integers t with |t| ≡ 2 (mod 4) and |t| ≥ 6.
- (c) The rapidity of a boost is ℓ = 2 arccosh(|t|/2) = 2 arccosh(2k + 1), with k ≥ 1.

The stabilizer of any circle of the packing is conjugate, in the full isometry group of hyperbolic space, to G₁⁺.

*Status: verified (proof; checks §5).*

*Proof.* A₁⁺ is generated by S₂S₄ and S₄S₃, since S₂S₃ = (S₂S₄)(S₄S₃). In the spin model:

- g₄g₃ has matrix M₄M̄₃ = (1 −4; 0 1), the translation z ↦ z − 4;
- g₂g₄ has matrix M₂M̄₄ = (−1−i −1; −1 −1+i), which in the coordinate u is −(1 0; 1 1), the map u ↦ u/(u+1).

So G₁⁺ is the image of ⟨T⁴, U⟩, where T = (1 1; 0 1) and U = (1 0; 1 1).

Next, ⟨T⁴, U, −I⟩ = Γ⁰(4). The inclusion ⊆ is clear. For ⊇, let X ∈ Γ⁰(4) have first row (a, 4b′). Right multiplication by Uᵏ changes a to a + 4kb′, and by T⁴ᵏ changes b′ to b′ + ka. Here a is odd, because ad − 4b′c = 1, so |a| ≠ 2|b′| unless b′ = 0.

- If |a| > 2|b′|, choose k with |a + 4kb′| ≤ 2|b′|.
- Otherwise choose k with |b′ + ka| ≤ |a|/2.

Either way max(|a|, 2|b′|) strictly decreases, so the process ends at b′ = 0, where X = ±Uᶜ. Check §5 runs this reduction on all 5,906 elements of Γ⁰(4) with entries of absolute value at most 60.

The conjugation diag(2,1)(a b; c d)diag(2,1)⁻¹ = (a 2b; c/2 d) maps Γ(2) onto Γ⁰(4). For an element of Γ⁰(4), ad ≡ 1 (mod 4) forces a ≡ d (mod 4), so a + d ≡ 2a ≡ 2 (mod 4). Hence |t| ∉ {0, 1, 3}: there are no rotations, |t| = 2 gives parabolic elements, and |t| ≥ 6 gives boosts; this proves (a). The matrix (1 4; k 4k+1) has trace 4k + 2, so every trace in (b) occurs. The rapidity in (c) follows from Lemma 1.2: for real t = 2cosh(ℓ/2), p = 2cosh ℓ.

Finally, the permutation matrices P\_σ lie in O\_F(ℤ) and satisfy P\_σSᵢP\_σ⁻¹ = S\_{σ(i)}, so they conjugate A₁ to each Aᵢ. The stabilizer of the circle Ψ(hcᵢ) is hAᵢh⁻¹ (Corollary 2.4). ∎

In the upper half-plane of u, the full stabilizer ⟨g₂, g₃, g₄⟩ is the reflection group of the ideal triangle with vertices 0, 2 and ∞, whose sides are Re u = 0, Re u = 2 and |u − 1| = 1. Scaling by ½ gives the triangle (0, 1, ∞) and the classical Γ(2).

### 4.2 Boosts attached to no circle

**Theorem 4.2.** The element γ = S₁S₂S₁S₃S₄S₃ ∈ A⁺ has the following properties.

- **It is a boost.** Its SL₂-trace is −18, and on the 4×4 side a = 324 = 18² and b = 646 = 2a − 2. Its rapidity is ℓ = 2 arccosh 9 = 2 log(9 + 4√5), so e^ℓ = 161 + 72√5.
- **It is a product of two reflections.** γ = R\_uR\_v, with u = S₁e₂ = (2, 1, 0, 0) and v = S₃e₄ = (0, 0, 2, 1). Here B(u,u) = B(v,v) = 1 and B(u,v) = −9. Geometrically these are the reflections in the dual circles g₁(D₂) and g₃(D₄), which are disjoint, and γ translates along their common perpendicular by twice their distance, arccosh 9.
- **It fixes no circle of the packing.** Equivalently, no circle of the packing passes through both of its fixed points.

*Status: verified (proof; check §12).*

*Proof.* R\_uR\_v = S₁S₂S₁·S₃S₄S₃, because S₁S₂S₁ is the reflection in S₁e₂, and similarly for the second factor. Two reflections in spacelike unit vectors with |B(u,v)| = cosh d > 1 compose to a boost of rapidity 2d that fixes span(u,v)^⊥ pointwise. The 4×4 invariants agree with this: a = 2 + 2cosh(2d) = 2 + 2·161 = 324. By Proposition 1.1, Ψ(eᵢ)/2 is the Hermitian matrix of Dᵢ: it has determinant −1 and is orthogonal to Hⱼ for j ≠ i. So u and v correspond to g₁(D₂) and g₃(D₄).

The cyclically reduced word 121343 uses all four letters, so by Corollary 2.4 γ fixes no oriented circle. For a boost, a circle is invariant as a set exactly when it passes through both fixed points, and then its orientation is preserved. As a check, §12 confirms that γ moves every circle vector hcᵢ with |h| ≤ 8. ∎

The same holds for the whole family (S₁S₂)ᵏS₁S₃S₄S₃, k ≥ 1, which consists of boosts of trace (−1)ᵏ(12k + 6) attached to no circle (Section 6). In the census (Section 6) there are 2,274 primitive classes of boosts attached to no circle with word length at most 12, and 1,904 primitive classes of boosts in circle stabilizers.

**Proposition 4.3 (products of two reflections).**

- (a) A product of two reflections of A is the identity, a boost or a parabolic element.
- (b) γ ∈ A⁺ is a product of two reflections of A if and only if some cyclic permutation of its cyclically reduced word is PQ, with P and Q palindromes of odd length.
- (c) The converse of (a) fails: the boost S₁S₂S₁S₂S₃S₁S₂S₃, with trace −34, lies in the circle stabilizer A₄ but is not a product of two reflections of A.

*Status: verified (proof; checks §6).*

*Proof.* The reflections of A are the conjugates of the Sᵢ, by Theorem 2.2(c).

(a) R\_uR\_v fixes span(u,v)^⊥ pointwise, so 1 is an eigenvalue of multiplicity at least 2, q = 2, and γ is not a screw motion. It is not a rotation, by Theorem 2.2(c).

(b) If γ = (aSᵢa⁻¹)(bSⱼb⁻¹), then γ is conjugate to SᵢcSⱼc⁻¹ with c = a⁻¹b. We may assume c does not end in Sⱼ, since otherwise the last letter cancels. Then P = cSⱼc⁻¹ is reduced as written and is an odd palindrome.

- If P does not begin with Sᵢ, then SᵢP is cyclically reduced, and it is the product of the odd palindromes Sᵢ and P.
- If P = SᵢmSᵢ, then SᵢP = mSᵢ, where m is an odd palindrome not beginning or ending with Sᵢ.

In both cases Lemma 2.3(iii) gives the claim. Conversely, an odd palindrome pS\_ap⁻¹ is a reflection.

(c) The word 12123123 has trace −34 and uses three letters. Check §6 confirms that none of its 8 cyclic permutations splits into two odd palindromes. The census finds 2,102 such boosts, not products of two reflections, among the classes of length at most 12. ∎

## 5. Complex one-parameter groups, lattices and holonomy

For points p ≠ q of the Riemann sphere, the group of Möbius transformations fixing p and q is

  T\_{p,q} = {gH\_r^zg⁻¹ : z ∈ ℂ},

for any g with g(0) = p and g(∞) = q. The map z ↦ gH\_r^zg⁻¹ is a homomorphism of ℂ onto T\_{p,q} with kernel (πi/r)ℤ in PSL₂(ℂ). Its compact real form (z ∈ iℝ) consists of the rotations about the geodesic pq; these are the conjugates of the modular flow of Proposition 8.3. Its non-compact real form (z ∈ ℝ) consists of the boosts along pq, the conjugates of the note's boost.

**Theorem 5.1 (irrational holonomy).** For every screw motion γ ∈ A⁺, θ(γ)/2π is irrational. Equivalently, no power of a screw motion is a boost.

*Status: verified (proof; the congruence in step (iii) is a finite computation, check §7; check §8 confirms the conclusion for all 46,866 screw classes of length at most 12).*

*Proof.* (i) *Crystallographic restriction.* By Lemma 1.2 the characteristic polynomial x⁴ − ax³ + bx² − ax + 1 of γ, which has integer coefficients, factors as (x² − px + 1)(x² − qx + 1). Here p = 2cosh ℓ > 2 and q = 2cos θ ∈ [−2, 2], and p and q are the two roots of Y² − aY + (b − 2) ∈ ℤ[Y].

- Suppose θ ∈ 2πℚ. Then q = ζ + ζ⁻¹ for a root of unity ζ, so every Galois conjugate of q lies in [−2, 2].
- If q were irrational, its Galois conjugate would be the other root p > 2, a contradiction. So q is rational, and being a root of a monic integer polynomial, it is an integer in [−2, 2].
- q = 2 means θ = 0, which is not a screw motion. So q ∈ {−2, −1, 0, 1}.

(ii) *The four cases.* By Lemma 1.2, a = x² + y² and b − 2 = 2(x² − y²) − 4, where t = x + iy. Substituting q into q² − aq + (b − 2) = 0 gives:

| q | condition on t = x + iy |
|---|---|
| −2 | x = 0 |
| −1 | 3x² − y² = 3 |
| 0 | x² − y² = 2 |
| 1 | x² − 3y² = 3 |

(iii) *A congruence.* The images of the matrices of S₁S₄, S₂S₄ and S₃S₄ generate a subgroup of SL₂(ℤ[i]/4ℤ[i]) with 8 elements, and every one of them has trace ≡ 2 (check §7, closure under multiplication). Every element of A⁺ is a product of these generators and their inverses, so the corresponding product of matrices, a lift of it to SL₂(ℤ[i]), has trace t ≡ 2 (mod 4ℤ[i]). The other lift has trace −t, and −2 ≡ 2, so the sign of the lift does not matter. Hence x ≡ 2 (mod 4) and y ≡ 0 (mod 4), so x² ≡ 4 and y² ≡ 0 (mod 16).

This rules out each case. The first contradicts x ≡ 2. Modulo 16, the other three would require 12 ≡ 3, 4 ≡ 2 and 4 ≡ 3 respectively. ∎

**Theorem 5.2 (lattices).** Let T = T\_{p,q}.

- A⁺ ∩ T is trivial or infinite cyclic.
- If it is nontrivial, it is generated by a primitive loxodromic element γ₀ with fixed points p and q, and the set Λ = {z ∈ ℂ : gH\_r^zg⁻¹ ∈ A⁺} is the lattice ℤz₀ ⊕ ℤ(πi/r), where 2rz₀ = ℓ₀ + iθ₀ is the complex length of γ₀.

Then:

- (a) Λ ∩ iℝ = (πi/r)ℤ. The rotation real form meets A⁺ only in the identity.
- (b) Λ ∩ ℝ ≠ {0} if and only if γ₀ is a boost, and then A⁺ ∩ T lies in the boost real form.
- (c) The quotient of the sphere minus {p, q} by ⟨γ₀⟩ is the torus ℂ/(ℤ(ℓ₀ + iθ₀) + ℤ2πi). In the basis formed by the complex length and the rotation period 2πi, its modulus is τ = (−θ₀ + iℓ₀)/2π in the upper half-plane, with θ₀ ∈ (−π, π]. τ is purely imaginary, that is, the complex length is orthogonal to the rotation period, exactly for boosts; for screw motions Re τ = −θ₀/2π is irrational.

*Status: verified (proof; examples in check §13).*

*Proof.* A⁺ ∩ T is discrete and torsion-free. The preimage of a discrete subgroup D of T ≅ ℂ/(πi/r)ℤ in ℂ is a discrete subgroup containing (πi/r)ℤ, hence of rank at most 2. So D ≅ ℤ × (finite), and since D is torsion-free, D is trivial or ℤ.

Suppose γ₀ = δᵏ with δ ∈ A⁺. Then δ commutes with γ₀, so it permutes {p, q}. It cannot swap them: then δ² would fix p, q and the fixed points of δ, hence would be the identity, and δ ≠ 1 would have order 2, which Theorem 2.2(c) excludes. So δ ∈ T ∩ A⁺ = ⟨γ₀⟩, and γ₀ is primitive.

(a) If mz₀ + nπi/r is purely imaginary with m ≠ 0, then Re z₀ = 0 and ℓ₀ = 0, which is impossible for a loxodromic element.

(b) mz₀ + nπi/r is real exactly when mθ₀ + 2πn = 0. For m ≠ 0 this forces θ₀ ∈ 2πℚ, hence θ₀ = 0 by Theorem 5.1.

(c) The multiplication z ↦ e^{ℓ₀+iθ₀}z on ℂ∗ is covered by the translation by ℓ₀ + iθ₀ on ℂ, which has period 2πi. The irrationality for screw motions is Theorem 5.1. ∎

**Corollary 5.3 (answer to the question of the Erdős–Straus paper).** Let {exp(sY)} be a one-parameter subgroup of SO⁺\_F(ℝ) ≅ PSL₂(ℂ).

1. **Compact** (rotations about a timelike axis, including every transported modular flow): it meets A only in the identity.
2. **Non-compact, fixing two points p ≠ q** (boosts or screw motions along the axis pq): write it as s ↦ gH\_r^{sw}g⁻¹. It meets A nontrivially if and only if A⁺ ∩ T\_{p,q} = ⟨γ₀⟩ is nontrivial and w is a real multiple of mz₀ + kπi/r for coprime integers m ≥ 1 and k, where γ₀ = gH\_r^{z₀}g⁻¹. The intersection is then ⟨γ₀^m⟩.
   - A boost group (w real) therefore meets A nontrivially exactly when its axis carries a boost γ₀ of A⁺, and the intersection is then ⟨γ₀⟩. Such axes occur inside every circle stabilizer, with rapidities 2 arccosh(2k + 1), and outside all of them (Theorem 4.2).
   - If γ₀ is a screw motion, every group in (2) that meets A is a screw group.
3. **Unipotent** (null rotations): it meets A nontrivially exactly when it contains a parabolic element of A⁺; the six classes SᵢSⱼ are examples.

*Status: verified (proof below, from Theorems 3.1, 5.1 and 5.2).*

*Proof.* (1) is Theorem 3.1. For (2), note first that a non-compact one-parameter group fixing p and q lies in T\_{p,q}. By Theorem 5.2 its elements in A⁺ are the gH\_r^{sw}g⁻¹ with sw ∈ ℤz₀ ⊕ ℤ(πi/r). Write w = mz₀ + kπi/r. Since z₀ has nonzero real part ℓ₀/2r, the numbers z₀ and πi/r are linearly independent over ℝ, so sw lies in the lattice exactly when sm ∈ ℤ and sk ∈ ℤ, that is, when s ∈ ℤ, as m and k are coprime. The intersection is therefore generated by gH\_r^{mz₀ + kπi/r}g⁻¹ = γ₀^m in PSL₂(ℂ). If w is not a real multiple of such an mz₀ + kπi/r, only s = 0 qualifies. A real w arises in this way only if mθ₀ + 2πk = 0, which by Theorem 5.1 forces θ₀ = 0, k = 0 and m = 1. Part (3) is a restatement. ∎

**Proposition 5.4 (orbits on integral packings).** Let γ ∈ A⁺ and let v be an integral Descartes quadruple. The curvature sequences n ↦ (γⁿv)ᵢ satisfy the integer linear recurrence given by the characteristic polynomial of γ.

- If γ is a boost, then (γⁿv)ᵢ = αe^{nℓ} + α′e^{−nℓ} + β.
- If γ is a screw motion, then (γⁿv)ᵢ = αe^{nℓ} + α′e^{−nℓ} + βcos(nθ) + β′sin(nθ), with θ/2π irrational. So the bounded part, the trace of the rotation, is quasi-periodic and, when nonzero, never periodic.

Two examples on the packing (−1, 2, 2, 3):

- The boost S₁S₂S₁S₃ ∈ A₄ has characteristic polynomial (x − 1)²(x² − 34x + 1) and growth factor e^ℓ = 17 + 12√2. Its orbit keeps the fourth circle, of curvature 3, fixed: (−1,2,2,3) → (119,62,6,3) → (4271,2138,362,3) → ⋯.
- The screw motion S₁S₂S₃S₄, with trace −2 − 8i, has e^ℓ ≈ 69.7628 and cos θ = 17 − 8√5, so θ ≈ 2.66496. The rotation part of its orbit is nonzero; check §10 shows its first coordinates −1.84, 1.59, −0.98, 0.15, 0.71, …

*Status: verified (proof; checks §§10–11).*

*Proof.* The recurrence is the Cayley–Hamilton theorem. Boosts are diagonalizable with eigenvalues e^{±ℓ} and 1 (twice). Screw motions have four distinct eigenvalues e^{±ℓ} and e^{±iθ}. Irrationality is Theorem 5.1. ∎

## 6. Census

Check §6 classifies every primitive conjugacy class of A⁺ whose cyclically reduced word has length at most 12, one class per cyclic word, 51,050 in all:

| word length | parabolic | boosts in circle stabilizers (3 letters) | boosts attached to no circle (4 letters) | screw motions |
|---|---|---|---|---|
| 2 | 6 | 0 | 0 | 0 |
| 4 | 0 | 12 | 0 | 6 |
| 6 | 0 | 36 | 12 | 68 |
| 8 | 0 | 120 | 90 | 600 |
| 10 | 0 | 396 | 396 | 5,088 |
| 12 | 0 | 1,340 | 1,776 | 41,104 |
| total | 6 | 1,904 | 2,274 | 46,866 |

No class is a rotation, and no class using at most three letters is a screw motion, as Theorems 2.2 and 4.1 require. The first class in each column follows a visible pattern:

- boosts in circle stabilizers: (12)ᵏ13, with t = (−1)ᵏ(4k + 2);
- boosts attached to no circle: (12)ᵏ1343, with t = (−1)ᵏ(12k + 6);
- screw motions: (12)ᵏ34, with t = (−1)ᵏ(2 + 8ki).

These formulas hold for every k ≥ 1. The lift of S₁S₂ is −(I + N) with N² = 0, so for every word u the trace tr((S₁S₂)ᵏu) = (−1)ᵏ(tr u + k·tr(Nu)) is (−1)ᵏ times an affine function of k. Two computed values then fix each formula, and check §14 confirms them for k ≤ 30. In particular (S₁S₂)ᵏS₁S₃S₄S₃, k ≥ 1, is an infinite family of pairwise non-conjugate boosts attached to no circle, and (S₁S₂)ᵏS₃S₄ an infinite family of screw motions.

Sample moduli τ = (−θ + iℓ)/2π:

| class | trace | ℓ | θ | τ |
|---|---|---|---|---|
| 1213 | −6 | 3.525494 | 0 | 0.561100 i |
| 121343 | −18 | 5.774542 | 0 | 0.919047 i |
| 1234 | −2 − 8i | 4.245100 | 2.664958 | −0.424141 + 0.675629 i |
| 121234 | 2 + 16i | 5.568099 | 2.894755 | −0.460715 + 0.886190 i |

The proportion of boosts among the classes of length 12 is (1,340 + 1,776)/44,220 ≈ 7%. Section 8.1 explains why this proportion is expected to tend to zero, when the classes are ordered by length ℓ.

## Part B. Proved negative results

## 7. Proved negative results

1. **No rotations.** No nontrivial element of A is a rotation, and no nontrivial element is a transported modular automorphism of a faithful state of M₂(ℂ) (Theorem 3.1, Corollary 3.2).
2. **Not every boost fixes a circle.** S₁S₂S₁S₃S₄S₃ is a boost that fixes no circle of the packing (Theorem 4.2).
3. **Not every boost is a product of two reflections of A.** S₁S₂S₁S₂S₃S₁S₂S₃ is a boost of trace −34 that is not such a product (Proposition 4.3(c)).
4. **No power of a screw motion is a boost.** A screw motion never has rational holonomy (Theorem 5.1).

## Part C. Bridges and directions

## 8. Bridges and directions

### 8.1 The rotation part is generic

Margulis, Mohammadi and Oh prove the following for a Zariski-dense, geometrically finite subgroup Γ of a rank-one group [MMO, Theorem 1.1]: for every continuous class function φ on the holonomy group M,

  Σ φ(h\_C) ∼ (e^{δT}/δT) ∫\_M φ dm,

where the sum runs over the closed geodesics C of length at most T counted in [MMO], and h\_C is the holonomy of C. For PSL₂(ℂ) this says that the arguments of the multipliers equidistribute [MMO, Theorem 1.3].

A⁺ satisfies these hypotheses.

- **Zariski density.** A⁺ is Zariski dense, since A is Zariski dense [Sa] and A⁺ has index 2 in it.
- **Geometric finiteness.** The polyhedron bounded by the four hemispheres over the dual disks has face normals e₁, …, e₄. Their Gram matrix is 2I − J, so the faces are pairwise tangent at infinity, with dihedral angles 0. By Vinberg's theory of reflection groups [Vi], A is discrete with this four-sided polyhedron as a fundamental domain, and A⁺ has the union of two copies as one. A finite-sided fundamental polyhedron is the classical definition of geometric finiteness in dimension 3 [Bo].

Approximating the indicator of the identity by continuous functions, the boosts, whose holonomy is trivial, therefore form a subset of density zero among the primitive closed geodesics ordered by length. The census in Section 6 is ordered by word length rather than ℓ, so it is only consistent with this, not a test of it.

My assessment: in the terms of Proposition 8.3, this says that the rotation direction of the complex one-parameter group is the generic behaviour in the thin group, and the boost direction the exceptional one. Yet the boost direction is where the known arithmetic is (Section 8.2). I think this is the most useful reading of the section title *Finite-dimensional modular flow as a Lorentz boost* in the author's notes, because it says where each real form sits in the group.

### 8.2 The arithmetic of A sits in the boost slice

Sarnak observed that the curvatures of the circles tangent to a fixed circle are properly represented by a shifted binary quadratic form attached to that circle [SaL, Sa].

- Bourgain and Fuchs prove that the curvatures of an integral packing have positive density [BF]. Fuchs's survey describes their strategy: it considers the curvatures two tangencies away from a fixed circle, that is, the values of the corresponding family of shifted binary forms [Fu].
- Haag, Kertzer, Rickards and Stange attach a quadratic form f\_C to each circle C. Using quadratic and quartic reciprocity for the values of these forms, they construct the obstructions that disprove the local–global conjecture for Apollonian packings [HKRS, §§3.2 and 4].

Theorem 4.1 identifies the group behind these forms. It is a congruence group, conjugate to Γ(2), in which every element is a boost or parabolic. The known arithmetic of the thin group is thus carried by the non-compact real form, inside circle stabilizers.

My assessment: I think the natural next question is whether the boosts attached to no circle (Theorem 4.2), which are as numerous as the circle-stabilizer boosts in the census, carry arithmetic of a comparable kind. A boost fixes the pencil of circles through its two fixed points. For a circle-stabilizer boost one circle of that pencil belongs to the packing, and the binary form lives on it. For the other boosts no circle of the pencil belongs to the packing, and I do not know what replaces the form (Question 1).

### 8.3 Modular theory

In finite dimensions the modular flow of a faithful state is a unitary conjugation, hence a rotation (Corollary 3.2), and the boost appears as the real-parameter form of the same complex group. In algebraic quantum field theory the situation is reversed. Bisognano and Wichmann showed that the modular group of the vacuum state restricted to the algebra of a Rindler wedge acts by the Lorentz boosts that preserve the wedge [BW].

My assessment: the one-parameter groups that meet A through boosts (Corollary 5.3(2)) are of the type that occurs as a modular group in the Bisognano–Wichmann setting, boosts preserving a wedge, and not of the type that occurs in M₂(ℂ). This is a structural observation, not a construction. I have not found a family of wedge-type algebras on which A acts so that its boosts become modular flows, and I do not know whether one exists.

### 8.4 Bearing on the Erdős–Straus notes

The map from shell data to Descartes quadruples in the author's notes is not verified here (Erdős–Straus paper, §8.4). If such a map exists, the results above say which one-parameter subgroups could carry shell data into the Apollonian group: boosts and screw motions through elements of A, never a rotation or a modular flow by itself (Corollary 5.3). This is a statement about the Apollonian side only. I have no view yet on whether a typed map from shell occupancy to A exists.

## 9. Questions

1. **Arithmetic of boosts attached to no circle.** Is there a binary quadratic form, or another arithmetic object, attached to the pencil of circles through the fixed points of a boost that fixes no circle of the packing, as Sarnak's form is attached to a circle?
2. **Parabolic elements.** Is every parabolic element of A⁺ conjugate to a power of some SᵢSⱼ? The census finds no other primitive parabolic class up to word length 12.
3. **The congruence of Theorem 5.1.** The image of A⁺ in SL₂(ℤ[i]/4) has only 8 elements. Is A⁺, in this model, contained in a conjugate of a principal congruence subgroup of level 2 of PSL₂(ℤ[i])? What is the smallest congruence subgroup of the Picard group containing it?
4. **Counting by word length.** What is the asymptotic proportion of boosts, and of boosts attached to no circle, among primitive classes ordered by word length? Section 8.1 settles the analogous question for ordering by ℓ.

## 10. Verification

`checks/apollonian/apollonian_real_forms.py` runs in about 35 seconds with Python 3, sympy and numpy, and prints 95 checks, all passing (`apollonian_real_forms_OUTPUT.txt`). All group computations use exact integer or Gaussian-integer arithmetic. Only the decomposition in §10 and the complex lengths in §13 use floating point. The sections of the program are:

- §1: the generators;
- §2: the height lemma on all reduced words of length at most 10;
- §3: the circle vectors;
- §4: the spin model. The intertwining Λ\_{gᵢ}Ψ = ΨSᵢ is checked exactly, and the identities tr S\_w = |tr N\_w|² and b = 2Re(t²) − 2 on all 88,572 even words of length at most 10;
- §5: the circle stabilizer and Γ⁰(4);
- §6: the census and the two-palindrome test;
- §7: the image of A⁺ modulo 4;
- §8: irrational holonomy of all screw classes;
- §9: rational holonomy of powers up to 12;
- §§10–11: orbits;
- §12: the boost S₁S₂S₁S₃S₄S₃;
- §13: complex lengths and moduli;
- §14: the three infinite families along the parabolic S₁S₂.

## 11. References

- [BF] J. Bourgain, E. Fuchs, A proof of the positive density conjecture for integer Apollonian circle packings, J. Amer. Math. Soc. 24 (2011) 945–967.
- [Bo] B. H. Bowditch, Geometrical finiteness for hyperbolic groups, J. Funct. Anal. 113 (1993).
- [BW] J. J. Bisognano, E. H. Wichmann, On the duality condition for a Hermitian scalar field, J. Math. Phys. 16 (1975) 985.
- [Fu] E. Fuchs, Apollonian packings: the rise and fall of the local to global conjecture, survey, available at the author's web page (math.ucdavis.edu/~efuchs/LocGlobConjACP.pdf).
- [HKRS] S. Haag, C. Kertzer, J. Rickards, K. E. Stange, The local-global conjecture for Apollonian circle packings is false, Ann. of Math. 200 (2024) 749–770; arXiv:2307.02749.
- [MMO] G. Margulis, A. Mohammadi, H. Oh, Closed geodesics and holonomies for Kleinian manifolds, Geom. Funct. Anal. 24 (2014) 1608–1636.
- [Sa] P. Sarnak, Integral Apollonian packings, Amer. Math. Monthly 118 (2011) 291–306.
- [SaL] P. Sarnak, Letter to J. Lagarias about integral Apollonian packings, June 2007.
- [Vi] È. B. Vinberg, Discrete groups generated by reflections in Lobachevskii spaces, Math. USSR-Sb. 1 (1967) 429–444.
- Claude (Anthropic), *The Erdős–Straus equation through residual shells*, version 4, 2026, `contrib/claude-ab/rewrite/papers/erdos_straus/`: Proposition 8.3, §8.4 and Question 12; in its condensed version, `contrib/claude-ab/rewrite/condensed/ERDOS_STRAUS_PAPER.md`, these are Proposition 8.3, §12.4 and Question 11.
