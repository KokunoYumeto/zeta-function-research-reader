# The 25 September continuations, part 3: the vertical weight receivers and the growth of tensor powers

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 06:43 UTC. Refereed in the fourth pass (on `14_`–`16_` and digest draft 2); its findings were applied at 07:39–07:43 UTC (`PLAN.md`).

This is a content map of two further proof blocks from the continuation `20260925-full-source-tensor-and-original-divisor/counterfactual/`, both read in full:

- VWR0–VWR11 (`FULL_VERTICAL_WEIGHT_RETURN.md`): Connes' weighted-L² construction on every vertical line;
- ATG0–ATG10 (`ALL_TENSOR_DERIVED_RETURN_AND_ACTUAL_GROWTH.md`): all tensor powers and their growth estimates.

Notation as in `12_`: Q = A/J is the zeta quotient, T_a is the dilation b(u) ↦ b(u/a), and K_off is the classes of Q vanishing on all critical-line jets.

## 1. VWR: one Hilbert receiver for every vertical line

For 0 < σ < 1 and δ > 0 put

  𝓗_{σ,δ} = L²((0,∞), u^{2σ−1}(1 + log²u)^δ du),  Q_{σ,δ} = 𝓗_{σ,δ}/closure(J).

WHR (`12_` §1.6) is the case σ = ½. VWR proves the following.

1. **Jets.** The jet functional F ↦ F^{(j)}(ρ) is continuous on 𝓗_{σ,δ} iff Re ρ = σ and j < δ − ½, and then its norm is as in WHR2.4 (VWR4.1–4.2). The closure of J is the common kernel of the jet functionals at the zeros ρ of ζ on Re s = σ, with j < min(m_ρ, δ − ½) (VWR4.3). It has the same one-function generator b₀ = Σh₀ as in WHR.
2. **Purity of each receiver.** ‖T_a‖ = a^σ Λ₊(log a)^{δ/2} on 𝓗_{σ,δ}, and Spec(T_p | Q_{σ,δ}) ⊆ {|z| = p^σ} (VWR3.2–3.4). Translated into Deligne's normalization |α| = p^{w/2}, the receiver Q_{σ,δ} would be "pure of weight 2σ". This is an analogy only: the weights here are real numbers, not integers, and the discreteness of weights is exactly the missing mechanism (digest §1.2(a)).
3. **Joint faithfulness.** The family α_all : Q → ∏_{0<σ<1} ∏_{N≥1} Q_{σ,N} is continuous, equivariant and injective (VWR5.2). The critical family alone has common kernel K_off (VWR5.4).
4. **Duality.**
   - The mirror R b(u) = u^{−1}b(u^{−1}) is an isometry 𝓗_{σ,δ} → 𝓗_{1−σ,δ}. It carries J to J and satisfies RT_a = aT_{1/a}R (VWR7.1–7.2).
   - So the weights come in pairs 2σ and 2 − 2σ, and the residue pairing has target character a, of weight 2. Each individual input weight is 2σ, not necessarily 1.
5. **Nondegeneracy on the defect.** The residue form B_ζ restricted to K_off × K_off is nondegenerate on both sides (VWR8.9). A quotient that kills part of K_off therefore cannot carry B_ζ.
6. **The scalar defect, and a test.**
   - Θ_off(b) = F(0) + F(1) + A_∞(b) − P_ζ(b) − Σ_{Re ρ=½} m_ρ F(ρ) = Σ_{Re ρ≠½} m_ρ F(ρ) is a continuous functional on Q. It vanishes iff there are no off-line zeros (VWR10.5–10.6).
   - It is never a *nonzero* multiple of the generic-point evaluation b ↦ b(1): Θ_off = c·ev₁ forces c = 0 and Θ_off = 0. The evaluation b ↦ b(1) is the term that, as cited in VWR10, Connes–Consani's semilocal trace formula attributes to the generic point (arXiv:2602.15941, §8; not read by me).
   - The proof uses an explicit b_* ∈ J with b_*(1) = 2 and Θ_off(b_*) = 0 (VWR10.8–10.9). I checked b_*(1) = 2 by hand: only n = 1 meets the support of h_*.

**Reading.** The facts above are proved in VWR; the interpretation is mine.

- The family {Q_{σ,N}} is a faithful decomposition of Q into pieces that are "pure" in the analogical sense of item 2, indexed by the vertical lines that carry zeros. It is faithful, but not a direct sum.
- The mirror is a Poincaré-type duality, weight w ↔ 2 − w.
- RH is the statement that every piece with σ ≠ ½ is zero, which is "purity of weight 1" in the same analogical sense. Equivalently, the σ = ½ family alone is faithful.
- VWR9 states explicitly that this exclusion has not been proved and remains the active lifting target.

## 2. ATG: tensor powers and their growth

1. **Cohomology of the k-fold product (ATG1.3).** H^j(D_k) is the sum over subsets I ⊂ {1, …, k} with |I| = j of ⊗_ν C_{ν,I}, where C_{ν,I} = Q for ν ∈ I and H otherwise. The diagonal return (ATG2–ATG4) and its trace are computed in every degree, with signs.
2. **The faithful norm is bounded by t^k (t ≥ 1).**
   - The quotient ν of the seminorm p_{1,0} is a separating norm on Q (ATG6.3), and ν^{⊗k}(T_t^{⊗k}X) ≤ t^k ν^{⊗k}(X) (ATG6.4).
   - The exponent 1 per factor is sharp for the source seminorms on A (ATG6.1). Sharpness for ν on Q is not proved.
3. **An isometric seminorm sees no zero (ATG6.5).** The quotient ν₀ of the sup norm is invariant under T_t and T_t^{−1}, and it vanishes on every primary block with 0 < Re ρ < 1. For an eigenvector, ν₀(x) = ν₀(T_px) = p^{Re ρ}ν₀(x) forces ν₀(x) = 0; induction up the Jordan chain does the rest.
   - The same argument with the half-density action U_p = p^{−1/2}T_p gives a general statement (my derivation): any seminorm invariant under U_p and U_p^{−1} vanishes on every off-line block. Invariance forces ν(x) = p^{Re ρ − ½}ν(x).
4. **The critical Hilbert components grow like t^{k/2}, but have a kernel (ATG6A).** On the σ = ½ components the tensor bound has exponent k/2. Their common kernel is Σ_ν Q^{⊗(ν−1)} ⊗ K_off ⊗ Q^{⊗(k−ν)} (ATG6A.4). So the better exponent is paid for by exactly the off-line classes.
5. **The exact error is linear in k (ATG8).**
   - Let S be any finite set of zeros that is stable under ρ ↦ 1 − ρ̄ (as ATG8.5 assumes; this gives B ≥ ½). Then Tr((T_p^{⊗k})^ℓ | V_S^{⊗k}) = (Σ_{ρ∈S} m_ρ p^{ℓρ})^k, and its exponential rate is k·max_{ρ∈S} Re ρ (ATG8.3–8.4).
   - Against the target k/2 the error is k(B − ½), with B = max Re ρ (ATG8.5).
   - A Deligne-type bound k/2 + c, with c independent of k, would force B = ½. The proved estimates (ATG6.4, 7.3, 9.2) have exponent k, not k/2 + c. They are of the additive-exponent kind, which Deligne avoids with D6.8 (a doubled-input bound with a single copy of the error) followed by the halving step D6.11.
   - This is the programme's own exact version of register negative result 27 (`08_` §3(e)).
6. **No ordinary trace on Q^{⊗k} for k ≥ 2 (ATG9).**
   - Take infinitely many reflected pairs (ρ, 1−ρ). They give linearly independent eigenvectors with the same eigenvalue p^{1+ρ₃+⋯+ρ_k}, so the eigenspace is infinite-dimensional.
   - Tests that see only the sum of the parameters meet this infinite multiplicity. ATG9.1 obtains a valid whole-spectrum trace by testing each factor separately; ATG9 does not prove that every valid trace must do so. The bound for this trace again has exponent k (ATG9.2).

**Checks.** The algebra of ATG8.3 is the multinomial expansion of a trace of a tensor power of a triangular operator. The rate ATG8.4 is the pole location of Σ_λ d_λ/(1 − λz) with positive multiplicities d_λ. The eigenvalue count in ATG9 uses only ρ + (1−ρ) = 1. The Hilbert-tensor operator bound ATG6A.3 is the product of the one-factor norms VWR3.2, whose constant Λ₊ is checked in `checks/c925_part2_checks.py` (WHR8.2). I read the remaining homological steps (ATG1–ATG4, ATG10) for correctness without re-deriving them.

## 3. Items for the goals

- **Lemma (goal 3).**
  - For every σ ∈ (0,1), Connes' construction in L²(u^{2σ−1}(1 + log²u)^δ du) realizes exactly the zeros on the line Re s = σ, with the multiplicity cutoff j < min(m_ρ, δ − ½). The prime dilations there have spectrum on |z| = p^σ. The family over all σ and N is jointly faithful on Meyer's quotient.
  - Status: proved in the programme (VWR); the jet norms and Λ₊ are checked.
  - Novelty: Connes' paper treats σ = ½. I have not checked whether the other lines appear there or elsewhere.
- **Negative results (goal 1).**
  - *Isometry sees nothing off the unitary axis.* This is ATG6.5 together with my half-density form.
  - *Tensor growth.* The faithful norm is bounded with exponent k (t ≥ 1), and the critical components have exponent k/2 only with the off-line kernel. The error k(B − ½) is linear in k (ATG6.4, ATG6A.4, ATG8.5).
  - *The off-line defect cannot be absorbed into the generic-point term (VWR10.9).*
- **Bridge (goal 2).** The VWR family plays the part of Deligne's weight decomposition:
  - each receiver is "pure of weight 2σ" in the translation |α| = p^{w/2} (real weights, so an analogy);
  - the mirror is duality w ↔ 2 − w, with a weight-2 target;
  - RH is purity of weight 1.

  This is an analogy of structure, and the programme itself states that the weight-1 exclusion is not proved (VWR9).
- **Remark.** VWR10.9 proves that the off-line defect functional is never a *nonzero* multiple of the generic-point evaluation b ↦ b(1). This is one precise form of the remark that a hidden off-line zero could not hide inside the "pure state". It is recorded as a pointer, not as a result about τ.
