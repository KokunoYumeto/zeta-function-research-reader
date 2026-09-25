# DW: the reconstruction of Deligne's amplification (Weil II §§1.5, 1.8), and which programme operator satisfies the monodromy relation

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 15:41 UTC. Board task 8: DW, the source on which ETR (`29_`) builds. Not yet refereed.

## 0. Source and scope

- **Read in full:** `AMPLIFICATION_AND_GLOBAL_EULER_PRODUCT.md` (DW, sections 1–10), in `quantum_tau_programme_bridge_20260924/next_edition_after_719`. 578 lines; SHA-256 `1bc4b572…afaaaa6f`, which equals the hash recorded in ETR0.
- **What DW is.** Sections 2–6 reconstruct Deligne's arguments in *La conjecture de Weil. II*, Publ. Math. IHÉS 52 (1980), §§1.5 and 1.8. DW works from a transcription of the printed text that is not among the staged files, and which I did not read. Sections 7–9 compute the programme's tensor Euler products, and section 10 summarizes what transfers.
- **What I checked.**
  - The logic of sections 2–6, step by step, as a mathematical argument.
  - I did not compare it with Deligne's printed text.
  - Sections 7–9 against ETR (`29_`), where the same statements were re-derived and checked.
- **Checks.** No new script. DW7.6 was checked at 40 digits on a synthetic off-line orbit (relative error 5·10⁻⁴⁰). DW8.3–8.6 are ETR4–ETR7, which `29_` checks.

**Verdict.** DW is correct as far as checked. Its reconstruction of Deligne's §1.5 and §1.8 arguments follows the standard mechanism, and every step I checked is valid.

## 1. Sections 2–6: the reconstruction

- **§1.5 (DW3), positivity and amplification.**
  - For an ι-real sheaf, tr((A^{⊗2k})^r) = (tr A^r)^{2k} ≥ 0, so every local reciprocal determinant of the even tensor power has nonnegative coefficients (DW3.1–3.3).
  - The global rational function has no pole in |T| < R_k = q^{−kr₀−1}. The reason: the only denominator is H_c², whose weights are at most 2kr₀ + 2 (DW2.3–2.4, DW3.4).
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
  - DW reports that both consulted copies print a positive twist in (1.6.14.3). A negative twist is forced by FNF^{−1} = Q^{−1}N together with the weights of the graded pieces, and DW's derivation of it is consistent.
    - I have not compared this with the printed original.
    - DW itself does not attribute the sign to Deligne.
- **§§1.8.5–1.8.13 (DW6).** The propagation statements are summarized correctly as consequences of DW5, the uniqueness of the relative monodromy filtration, and Deligne's reductions. DW does not claim to re-prove the reductions.

## 2. Sections 7–9: the programme's tensor objects

- **DW7.6.** tr(W_p^r | V_ρ) = 2m(p^{rβ} + p^{r(1−β)})cos(rγ log p) for an off-line quartet. It is real, so the even tensor powers have nonnegative coefficients (DW7.7).
- **DW8.4–8.6.** ℒ_k = ∏ζ(s − σ(ω))^{m^{2k}}, with a genuine pole at s_k = 1 + 2kB of order m^{2k}C(2k, k). These are ETR5–ETR7 for the quartet (`29_`).
- **DW8.11.** The displacement is s_k − (k + 1) = k(2B − 1) (`29_` 29.N4; `08_` I4).
- **DW8.12.** det(W_p | V_ρ) = p^{2m}, since ρ + ρ̄ + (1 − ρ) + (1 − ρ̄) = 2. So the average weight of the quartet is exactly 1.
  - The constituent characters have weights 2Re ω ∈ {2β, 2(1 − β)}.
  - So the determinant average does not detect an off-line quartet. This is a negative result (35.N1).
- **DW9 (= ETR10.5).** On a primary block, W_pNW_p^{−1} = N. So the defect against Deligne's relation FNF^{−1} = p^{−1}N is (1 − p^{−1})W_pN, of rank m − 1.
  - The regraded operator F_p^{geom} = p^ρS_p, with S_pε^j = p^{−j}ε^j, satisfies the relation and is multiplicative in p.
  - But its eigenvalues are p^{ρ−j}, not p^ρ. Satisfying the relation costs exactly a shift of weight by −2j on the j-th jet level.
  - I verified both identities: F N F^{−1}ε^j = p^{−1}ε^{j+1}, and F_aF_b = F_{ab}.

## 3. Bridge (goal 2): which programme operator satisfies the monodromy relation

- In Deligne's local picture, Frobenius F satisfies FNF^{−1} = Q^{−1}N (DW5.2, reconstructing Weil II §1.8.4).
- In the programme:
  - the counting operators W_p (ETR, DW7) and C_b (GJN5) commute with N (DW9.1, ETR10.5, GJN5.2);
  - the ramification operators satisfy NP_b = bP_bN (GJN4.4; `33_` Lemma 33.3), that is, P_bNP_b^{−1} = b^{−1}N on the image of P_b. This is the same form as Deligne's relation with Q = b.
- So, as an operator identity, the programme's analogue of Frobenius in the monodromy relation is ramification P_b, which moves the exponents λ ↦ bλ. It is not counting, which fixes them.
- The only way to make the counting jets satisfy the relation is DW9's regrading, which shifts the jet weights.
- This is a structural comparison of relations only. No geometric identification of P_b with a Frobenius is asserted. P_b does not preserve the space of exponents, so it is not a Frobenius acting on a fixed representation.

## 4. Negative result (goal 1)

- **35.N1. The determinant weight of an off-line quartet is exactly 1** (DW8.12). Determinant or average-weight data therefore cannot see an off-critical zero; only the constituent weights 2β and 2(1 − β) do. This matches `29_` 29.N4: the missing input is a pole bound uniform in the tensor degree, not any averaged weight.

## 5. Not checked

- Deligne's printed text (see §0).
- The transcription-defect claims about (1.3.10)(iv), (1.6.14.3) and (1.7.5).
- The external theorems DW cites: Grothendieck's trace formula, quasi-unipotence, and geometric monodromy.
