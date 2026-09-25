# DW: the reconstruction of Deligne's amplification (Weil II §§1.5, 1.8), and which programme operator satisfies the monodromy relation

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 15:41 UTC. Board task 8: DW, the source on which ETR (`29_`) builds. Refereed in the twelfth pass (16:43 UTC) and revised at 16:52 UTC; §6 lists the changes.

## 0. Source and scope

- **Read in full:** `AMPLIFICATION_AND_GLOBAL_EULER_PRODUCT.md` (DW, sections 1–10), in `quantum_tau_programme_bridge_20260924/next_edition_after_719`. 578 lines; SHA-256 `1bc4b572…39faaa6f`. ETR0 records this hash with one extra `a` (a 65-character string ending `…39faaaa6f`). Deleting that character gives DW's hash exactly (check B1), so ETR very probably reviewed these bytes, but the recorded string is not an exact match.
- **What DW is.** Sections 2–6 reconstruct Deligne's arguments in P. Deligne, *La conjecture de Weil. II*, Publ. Math. IHÉS 52 (1980), 137–252, §§1.5 and 1.8, with inputs from §§1.3–1.4. DW works from two transcriptions of the printed text, one French and one English; neither is among the staged files. Sections 7–8 compute the programme's tensor Euler products, section 9 the monodromy-comparison defect, and section 10 summarizes what transfers.
- **Label warning.** "DW" here means the equation labels DW2.1–DW9.2 of `AMPLIFICATION_AND_GLOBAL_EULER_PRODUCT.md`. The Deligne reader `DELIGNE_WEIGHT_CONTROL_FULL.md`, cited in `07_`–`08_`, uses the same prefix for its own sections DW0–DW11 (for example `08_`'s DW8.4).
- **What I checked.**
  - The logic of sections 2–6, step by step, as a mathematical argument.
  - Its agreement with Deligne's printed text: the referee of the twelfth pass compared sections 3–6 with the printed pages (numdam scan), and I checked the pages that carry the displays in question (pp. 160, 169–171 and 176); see §1.
  - Sections 7–9 against ETR, which re-derives them (ETR4–ETR7, ETR10.5, ETR11). `29_` checked ETR's derivations but not their correspondence with DW, which it did not read (`29_` §0); that correspondence is checked here.
- **Checks.** `checks/referee12_notes34_35_checks.py`, items B1–B13 (19/19 PASS for the whole script). For example DW7.6 holds on an explicit off-line quartet (β = 0.73, γ = 17.9, m = 3; p = 2, 3, 7; r ≤ 5) with relative error 1.9·10⁻⁴⁴ (B2). The label map is: DW8.3 is ETR4.7, DW8.4 is ETR5.3, DW8.5–8.6 are ETR6.6 with the quartet value ETR7.6, DW8.11 is ETR11.3, and DW9.2 is ETR10.5; `29_` checks these (its items 4–8, 12 and 13).

**Verdict.** DW is correct as far as checked. Its reconstruction follows Deligne's printed proofs step by step: Lemme 1.5.2 and (1.5.3) for DW3, Lemme 1.8.1 and Remarque 1.8.2 for DW4, and the proof of Théorème 1.8.4 for DW5, with β kept where Deligne twists to β = 0 (Weil II pp. 164–165 and 175–176; the comparison of pp. 164–165 and 175 is the referee's, and p. 176 I read myself). Every step I checked is valid.

## 1. Sections 2–6: the reconstruction

- **§1.5 (DW3), positivity and amplification.**
  - For an ι-real sheaf, tr((A^{⊗2k})^r) = (tr A^r)^{2k} ≥ 0, so every local reciprocal determinant of the even tensor power has nonnegative coefficients (DW3.1–3.3).
  - The global rational function has no pole in |T| < R_k = q^{−kr₀−1}. The reason: on an affine curve (H_c⁰ = 0; DW2.3; Deligne removes a point of X₀ to arrange this), the only denominator is H_c², whose weights are at most 2kr₀ + 2 (DW2.4, DW3.4).
  - Coefficientwise domination (DW3.5) transfers this to each local factor. I checked it: both factors have constant term 1 and nonnegative coefficients.
  - The local poles |ια|^{−2k/d_x} must therefore lie outside the disc. This gives w(α) ≤ r₀ + 1/k for every k, hence w(α) ≤ r₀ (DW3.7–3.8).
  - Purity of every constituent follows from exterior powers and the determinant equalities (DW3.9–3.13). The step is correct: the differences β − w(α_i) are nonnegative and sum to zero.
- **§1.8.1 (DW4), boundary weights.**
  - The trace formula and the weight β + 2 of H_c² give boundary weights ≤ β + 2.
  - The injection (V^I)^{⊗k} ↪ (V^{⊗k})^I carries α^k. So w ≤ β + 2/k, hence w ≤ β. Correct.
- **§1.8.4 (DW5), local monodromy.**
  - Geometric Frobenius and the logarithm of inertia satisfy FNF^{−1} = Q^{−1}N (DW5.2).
  - The primitive parts have |ια| = Q^{(β−j)/2}. The upper bound comes from the tensor summand P_{−j} ⊗ P_{−j}(−j) ⊂ P₀(V ⊗ V); the lower bound from the dual.
  - Gr_i^M V ≅ ⊕_{j≥|i|, j≡i (2)} P_{−j}(V)(−(i+j)/2) has weight β + i (DW5.12–5.13).
  - The Jordan-string vector Ω = Σ(−1)^r v_r ⊗ v_{j−r} is killed by N ⊗ 1 + 1 ⊗ N, as the telescoping shows. Its class is nonzero.
  - DW reports that both consulted copies print a positive twist in (1.6.14.3). The printed original has the same sign (Publ. Math. IHÉS 52, p. 170: Gr_i^M V ≅ ⊕_{j≥|i|, j≡i (2)} P_{−j}((i+j)/2)), so it is a misprint in the original.
    - Deligne's own mnemonic on the same page (give Gr_i and P_i the weight i and the one-dimensional Lie algebra 𝔑 the weight −2; then the two sides of each formula have equal weight; here Y(k) = Y ⊗ 𝔑^{⊗k}, p. 169) forces P_{−j}(−(i+j)/2): the printed right side has weight −i − 2j, not i (check B12). (1.6.14.1), (1.6.14.4) and (1.6.14.5) obey the rule.
    - The proof of Théorème 1.8.4 (p. 176) proves |ια| = q^{−j/2} on P_{−j} and then concludes from (1.6.14.3); that conclusion needs the negative twist.
    - In DW the sign comes from the equivariance of N^r: Gr_i(r) → Gr_{i−2r} (DW5.11); the weights of the graded pieces are then a consequence, not an input.
- **§§1.8.5–1.8.13 (DW6).** The propagation statements are summarized as consequences of DW5, the uniqueness (1.6.13) of the relative monodromy filtration, and Deligne's reductions. I checked the logic, not the wording against the printed text; the referee's spot check of Corollaire 1.8.5 against p. 176 agrees. DW does not claim to re-prove the reductions.

## 2. Sections 7–9: the programme's tensor objects

- **DW7.6.** tr(W_p^r | V_ρ) = 2m(p^{rβ} + p^{r(1−β)})cos(rγ log p) for an off-line quartet. It is real, so the even tensor powers have nonnegative coefficients (DW7.7).
- **DW8.4–8.6.** ℒ_k = ∏ζ(s − σ(ω))^{m^{2k}}, with a genuine pole at s_k = 1 + 2kB of order m^{2k}C(2k, k). These are ETR5.3, ETR6.6 and ETR7.6 for the quartet (`29_`).
- **DW8.11.** The displacement is s_k − (k + 1) = k(2B − 1) (`29_` 29.N4; `08_` I4).
- **DW8.12.** det(W_p | V_ρ) = p^{2m}, since ρ + ρ̄ + (1 − ρ) + (1 − ρ̄) = 2. So the average weight of the quartet is exactly 1.
  - The constituent characters have weights 2Re ω ∈ {2β, 2(1 − β)}.
  - So the determinant average does not detect an off-line quartet. This is a negative result (35.N1).
- **DW9 (= ETR10.5).** On a primary block, W_pNW_p^{−1} = N. So the defect against Deligne's relation FNF^{−1} = p^{−1}N is (1 − p^{−1})W_pN, of rank m − 1.
  - The regraded operator F_p^{geom} = p^ρS_p, with S_pε^j = p^{−j}ε^j, satisfies the relation and is multiplicative in p.
  - But its eigenvalues are p^{ρ−j}, not p^ρ. Satisfying the relation costs exactly a shift of weight by −2j on the j-th jet level.
  - I verified both identities: F N F^{−1}ε^j = p^{−1}ε^{j+1}, and F_aF_b = F_{ab}.

## 3. Bridge (goal 2): which programme operator satisfies the monodromy relation

- In Deligne's local picture, geometric Frobenius F satisfies FNF^{−1} = Q^{−1}N (DW5.2). In Weil II this is the Weil-group equivariance of N: V(1) → V, (1.7.2)–(1.7.3), pp. 170–171 (N commutes with the action of the Weil group), with geometric Frobenius acting on ℤ_ℓ(1) by Q^{−1} (check B10); it is used in the proof of Théorème 1.8.4.
- In the programme:
  - the counting operators W_p (ETR, DW7) and C_b (GJN5) commute with N (DW9.1, ETR10.5, GJN5.2);
  - the ramification operators satisfy NP_b = bP_bN (GJN4.4; `33_` Lemma 33.3), that is, P_bNP_b^{−1} = b^{−1}N on the image of P_b. This is the same form as Deligne's relation with Q = b.
- So, as an operator identity, the programme's analogue of Frobenius in the monodromy relation is ramification P_b, which moves the exponents λ ↦ bλ. It is not counting, which fixes them.
  - By `33_` 33.N5, a relation of the form NT = qTN has invertible solutions for every nilpotent N (they form Γ·Z(N)), so the comparison carries no arithmetic content by itself. The ramification operators realize it by the chain rule for the Kummer cover u ↦ u^b (`33_` Lemma 33.3).
- Counting can be made to satisfy the relation only by changing the jet weights, and the change is forced. Every operator F on a jet block J_ρ with FNF^{−1} = p^{−1}N has the form F = S_p·u(N), with u(N) an invertible polynomial in N: S_p^{−1}F commutes with N, and the commutant of a single Jordan block is ℂ[N]. Its eigenvalues are u(0)p^{−j}, 0 ≤ j < m (check B8). So if F induces W_p's scalar p^ρ on J_ρ/NJ_ρ, its eigenvalues are p^{ρ−j}: the shift of weight by −2j on the j-th jet level holds for every solution. DW9's F_p^{geom} = p^ρS_p is the solution with u = p^ρ.
- This is a structural comparison of relations only. No geometric identification of P_b with a Frobenius is asserted. P_b maps the block at λ to the block at bλ; on Ẽ it is injective but not surjective (GJN2.4: the block at a zero of smallest |Im ρ| is not in its image for b ≥ 2). So, unlike Deligne's F, it is not an automorphism of a fixed representation.

## 4. Negative result (goal 1)

- **35.N1. The determinant weight of an off-line quartet is exactly 1** (DW8.12). Determinant or average-weight data therefore cannot see an off-critical zero; only the constituent weights 2β and 2(1 − β) do. This matches `29_` 29.N4: the missing input is a pole bound uniform in the tensor degree, not any averaged weight.

## 5. Not checked

- Deligne's printed text outside the pages compared (pp. 160, 164–165, 169–171 and 175–176; see §0).
- The external theorems DW cites: Grothendieck's trace formula, quasi-unipotence, and geometric monodromy.

The three transcription defects that DW reports, in (1.3.10)(iv), (1.6.14.3) and (1.7.5), were in this list before the twelfth pass. They are now checked: all three are misprints in the printed original.
- (1.6.14.3), p. 170: see §1.
- (1.3.10)(iv), p. 160, states that the centre of G maps onto a finite subgroup of ℤ. A subgroup of finite index is meant. For G = 𝔾_m × ℤ, condition (i) holds (the projection to 𝔾_m is faithful on G⁰), while the centre, all of G, maps onto ℤ, which is not finite.
- (1.7.5), p. 171, prints M′_i = ∏_{j<i} V′_j in the proof. That gives Gr_i = V′_{i−1}, of weight i − 1, while the proposition asserts weight i; so j ≤ i is meant (check B13).

## 6. Revision after the twelfth referee pass (16:52 UTC)

The referee (a subagent) re-read DW, GJN and ETR, ran 32 checks, and compared DW §§3–6 with the printed Weil II (numdam scan). One of its three major findings concerns this note, and I applied it after checking it:
- **§0, the hash.** DW's SHA-256 ends `…39faaa6f`, not `…afaaaa6f`, and ETR0's recorded string has 65 hex digits, so "equals the hash recorded in ETR0" was false. Deleting one `a` from ETR0's string gives DW's hash (check B1). The mathematics is unaffected.

Minor findings applied, each checked against the source:
- the citation (pages 137–252), the two transcriptions, the sections of DW (§0), and a label warning: "DW" also names sections of the Deligne reader in `07_`–`08_`;
- what `29_` checked, and the exact DW↔ETR label map (§0, §2);
- a check script replacing an unrecorded 40-digit check (`checks/referee12_notes34_35_checks.py`, items B1–B13);
- the verdict now cites the printed proofs instead of "the standard mechanism" (§0);
- the affine hypothesis (§1);
- the three reported defects: I read pp. 160, 169–171 and 176 of the printed text, and all three are misprints in the original (§1, §5);
- the source of the monodromy relation in Weil II, (1.7.2)–(1.7.3) (§3);
- "the only way … is DW9's regrading" was literally false. The true statement is stronger: every solution of the relation on a jet block is S_p·u(N), so the weight shift is forced (§3; check B8);
- the relation NT = qTN has solutions for every nilpotent (`33_` 33.N5), so the comparison carries no arithmetic content by itself (§3);
- P_b is injective but not surjective on Ẽ (§3).

The time in the digest header is now consistent with this note.
