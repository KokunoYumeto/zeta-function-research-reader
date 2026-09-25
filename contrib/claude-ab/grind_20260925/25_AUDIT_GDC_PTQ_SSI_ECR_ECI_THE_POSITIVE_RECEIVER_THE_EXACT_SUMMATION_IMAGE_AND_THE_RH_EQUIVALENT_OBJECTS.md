# The positive receiver, the exact summation image and the extension-class maps: an audit of GDC, PTQ, SSI, ECR and ECI

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 11:27 UTC. Board task 8 (the owner's priority from about 11:03 UTC), part 2.

**Read in full.** All five blocks are in the zeta-function-research-reader repository at commit 064f33b, folder `workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/`.
- GDC0–GDC14: `geometric-positive-quotient/GYSIN_DEFECT_CLOSURE_AND_POSITIVE_RECEIVER.md`.
- PTQ0–PTQ11: `geometric-positive-quotient/POSITIVE_TRANSFER_UNIVERSAL_QUOTIENT.md`.
- SSI0–SSI10: `gct-weight-control/proofs/EXACT_SCHWARTZ_SUMMATION_IMAGE.md`. For SSI10, I checked its Fourier and valuation formulas but not the adelic comparison CS2/CS2A that it rests on.
- ECR0–ECR7: `geometric-positive-quotient/EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md`.
- ECI0–ECI13: `geometric-positive-quotient/EXTENSION_CLASS_INVOLUTION_INDEPENDENT.md`.

**Cited by these blocks, not re-read here.** SDT0–SDT9 (strong-dual topology), RGR, RTT, GTR, GTAH, FOD, NEA, GIQ and CS2/CS2A. S3, the division estimate that SSI uses, was read with S1–S7 for `04_`.

**Checks.** `checks/gdc_ptq_ssi_ecr_eci_audit_checks.py` has 10 items, and all pass; the output is in `checks/gdc_ptq_ssi_ecr_eci_audit_checks_OUTPUT.txt`. Some items of `checks/gsl_gms_ast_audit_checks.py` (for `24_`) also apply here.

## 0. Summary

1. **SSI is correct, and it is the most substantial analytic theorem in this group.**
   - The map f ↦ ℳ₀Σf, from even Schwartz functions with f(0) = 0 and ∫f = 0, is a topological isomorphism onto the closed ideal I of rapidly decaying entire functions that vanish to full order at every nontrivial zero. Here ℳ₀Σf(s) = 2ζ(s)∫_0^∞f(v)v^{s−1}dv.
   - The inverse is explicit: the inverse Mellin transform of F/(2ζ), or the Möbius sum ½Σμ(n)b(nx).
   - The Taylor coefficients of the source at 0 are the values of F at the trivial zeros, divided by 2ζ′(−2r).
   - Lemma 25.1 restates the theorem.
2. **PTQ is correct.**
   - Among bounded representations in which the pullback and the transfer are adjoint, the universal one kills exactly the off-line coordinates.
   - The bounded positive forms with that adjointness are exactly the diagonal forms on the line zeros.
   - Lemma 25.2 restates this, with a shorter proof of the off-diagonal step.
3. **GDC is correct.**
   - The ACD defect image has preannihilator N_O and strong closure N_O^⊥, and the image does not depend on r > 1.
   - Restricting to A_O kills the defect and keeps the residue on the line zeros.
   - Its functional-analytic steps rest on SDT, which I have not re-read. GDC7's openness argument for restriction is standard duality theory for Fréchet–Montel spaces, and I checked it line by line.
4. **ECR and ECI are correct.**
   - The cyclic extension-class module M/𝔞 maps injectively into the source quotient by Gaussian multipliers, and canonically into the residue receiver.
   - The involutions keep their degree factors a, a² and a³ in their separate domains.
   - The extension generator e₀ detects the positive-adjoint defect exactly.
   - The two-line separator fixes the original component and its defect (ECR6, ECI9). This is consistent with `24_` §0 item 6, seen from the programme's side.
5. **Negative result (§5).**
   - AST, GDC, PTQ and ECR contain eight constructions that vanish, or fill their whole ambient space, if and only if RH holds. §5 lists them.
   - They reduce to three conditions: N_O = Q; H_off = 0; and the vanishing of a strictly positive sum over the off-line zeros Z_O.
   - Each equivalence holds by construction: the object is defined from the set of zeros with the off-line part isolated.
   - The two numerical detectors (PTQ8.3, ECR5.5) are not holomorphic functions of the zero ρ, so Weil's explicit formula does not compute them from the primes. The programme says so itself (PTQ8, ECR5).
   - These are exact reformulations. None of them is a mechanism that forces the off-line part to vanish.

## 1. SSI: the exact summation image

### 1.1 Audit, step by step

1. **Continuity, the inclusion and injectivity (SSI2).**
   - The Poisson identity Σf̂(u) = u^{−1}Σf(u^{−1}) + u^{−1}f(0) − ∫f handles u → 0 (`24_` check 5).
   - ℳ₀Σf = 2ζ·ℳf on Re s > 1 is Müntz's formula (Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., §2.11).
   - ℳ₀Σf is entire and rapidly decreasing on strips, because Σf ∈ A (the Poisson step). On Re s > −2 it equals 2ζℳf, where ℳf is holomorphic and zero at s = 1. So it vanishes to full order on Z (SSI2.3).
   - Injectivity follows from the Euler product on Re s > 1.
2. **The division (SSI2.4–2.6).** For F ∈ I, H = F/(2ζ) is holomorphic except for simple poles at −2r, with residue F(−2r)/(2ζ′(−2r)).
   - H(0) = −F(0), because ζ(0) = −½.
   - H(1) = 0 and H′(1) = F(1)/2, because the residue of ζ at 1 is 1.
3. **The edge estimates (SSI3).**
   - The formula |χ(−2N−1+it)|² = π^{−4N−3}·y coth(πy)·Π_{k=1}^N(k²+y²)·Π_{j=0}^N((j+½)²+y²), with y = t/2, follows from the reflection and recurrence of Γ (check 1, N = 0, …, 3, relative error below 10⁻⁴⁰).
   - Together with |1/ζ(b+it)| ≤ ζ(b), this bounds 1/ζ polynomially on both edges of the strip −2N−1 ≤ Re s ≤ b.
4. **The maximum principle (SSI4).**
   - The subquadratic bound |F/F_*| ≤ C exp(C(|t|+2)^{3/2}log(|t|+2)) is S3, read for `04_`. It is killed on the horizontal edges by e^{εs²}, whose modulus is e^{ε(σ²−T²)}.
   - The final bound (SSI4.7) is linear in a seminorm of F and does not involve the growth constant. So the inverse is continuous.
5. **The inverse (SSI5–SSI6).**
   - Shifting the contour to Re s = −2N−1 picks up exactly the residues c_r(F)x^{2r}.
   - The remainder is O(x^{2N+1−j}) after j derivatives. So f_F extends to an even Schwartz function with f_F(0) = 0.
   - ∫f_F = 2H(1) = 0.
6. **The Möbius form of the inverse (SSI7.1).** ½Σμ(n)Σf(nx) = f(x) by absolute convergence and Σ_{d|k}μ(d) = [k = 1] (check 2, for f = f₀ at three points).
7. **An independent test of SSI5.6.**
   - For the programme's source vector f₀(v) = (π/2)v²(2πv²−3)e^{−πv²}, ℳ₀Σf₀ = 2F₀ (`24_` check 4). So SSI5.6 predicts the Taylor coefficients of f₀ at 0 to be 2F₀(−2r)/(2ζ′(−2r)) = r(2r+1)(−1)^rπ^r/(2·r!).
   - The Taylor expansion of f₀ gives −3π/2 at v² and 5π²/2 at v⁴. Both agree with the formula, and so do the coefficients through v⁸ (check 3).
   - The endpoint identities (SSI6.3) also hold for f₀: ∫f₀ dx/x = −1/4 = −2F₀(0), and ∫f₀ log x dx = 1/8 = 2F₀(1)/2 (check 4).

**Verdict.** SSI1–SSI9 are correct. SSI10's local formulas are also correct: the Fourier transform of 1_{dẐ} is d^{−1}1_{d^{−1}Ẑ}, and ℓ_p(F̂) = −Cℓ_p(F). The adelic comparison that SSI10 rests on (CS2, CS2A) was not read.

### 1.2 Lemma 25.1 (the exact summation image)

**Setting.** Let S = {f ∈ 𝒮(ℝ): f even, f(0) = 0, ∫f = 0}. Put Σf(u) = 2Σ_{n≥1}f(nu) and ℳ₀b(s) = ∫_0^∞b(u)u^{s−1}du. Let I ⊂ B be the ideal of entire functions, rapidly decreasing on vertical strips, that vanish to full order at every nontrivial zero of ζ.

**Statement.** ℳ₀Σ: S → I is a topological isomorphism. The inverse is F ↦ f_F, where:
- f_F(x) = (2π)^{−1}∫H(2+it)x^{−2−it}dt, with H = F/(2ζ);
- equivalently, f_F(x) = ½Σ_{n≥1}μ(n)(ℳ₀^{−1}F)(nx) for x > 0;
- f_F^{(2r)}(0)/(2r)! = F(−2r)/(2ζ′(−2r)) for r ≥ 1;
- ∫_0^∞f_F dx/x = −F(0) and ∫_0^∞f_F log x dx = F(1)/2.

In particular the image ΣS is closed. There is no gap between the image and its closure.

*Proof.* This is SSI1–SSI7, audited in §1.1. The one analytic input from outside SSI is the division estimate S3. ∎

**Relation to earlier items.**
- The Taylor-coefficient formula is the Mellin fact recorded in the register (goal 4, item 11): ℳf has simple poles at −2r with residue f^{(2r)}(0)/(2r)!. Multiplying by ζ, which has simple zeros at −2r, turns each residue into the value F(−2r).
- In the owner's terms, the jet of the source at the point 0, where the nonzero numbers stop, is carried by the trivial zeros.
- **Attribution, as the programme itself records it (OMS0–OMS4, read for `26_`).** R. Meyer's arXiv:math/0412277 contains a closed-image theorem and a Fourier–Laplace range theorem. The range theorem requires two rapid-division conditions: F/ζ Schwartz on the lines σ ≥ ½, and F(σ+it)/ζ(1−σ−it) Schwartz on σ ≤ ½. OMS proves both conditions from full zero-jet vanishing (OMS2–OMS4); its division estimate (OMS2.8) is proved by the Hadamard product and a minimum-modulus argument, which I checked.
  - On that account, Lemma 25.1 is Meyer's range theorem made explicit for this space, with the division estimate supplied.
  - The eighth referee pass fetched Meyer's arXiv v3 through a tool summary, not a full reading. It reports Theorem 3.3 (closed range) and Theorem 4.1 (h/ζ Schwartz on σ ≥ ½, and h(σ+it)/ζ(1−σ−it) Schwartz on σ ≤ ½), which matches OMS0's description.
  - I have not read Meyer's paper. The comparison with it therefore remains open in the register under Verification, now narrowed to checking OMS0's description of Meyer's two theorems.

## 2. PTQ: the universal positive receiver

### 2.1 Audit

1. **The kernel of the defect (PTQ1.2).** The defect multiplier e^{−iγ log n}(n^σ − n^{1−σ}) vanishes if and only if σ = ½, for any n > 1. So ker D_n = H_line and the closure of the range is H_off.
2. **The projection as a limit (PTQ1.3).** P_line = s-lim exp(−rD_n^*D_n), by dominated convergence coordinate by coordinate.
3. **Adjointness on the line (PTQ2.2).** On H_line, n^{ρ̄} = n^{1−ρ}. So (T_n^{pos})^* = U_n^{pos} and T^*T = n.
4. **The universal property (PTQ3).** Let v = Xε_ρ. Then n‖v‖² = ‖A_nv‖² = n^{2σ}‖v‖². So v = 0 whenever σ ≠ ½ (check 10). I re-derived this.
5. **The classification of forms (PTQ4).** Correct. Lemma 25.2 gives a shorter proof of the off-diagonal step.
6. **The Weil form does not descend (PTQ5).** W = ⟨P_Lx, P_Ly⟩ + ⟨P_Ox, JP_Oy⟩. On an off-line pair, W(ε_ρ ± ε_{ρ^#}) = ±2m_ρ, with signature (1, 1) (check 10). So W descends through q_pos if and only if H_off = 0.
7. **The explicit formula (PTQ9).** It is written with the "history" weights log L_n − log L_{n−1}, where L_n = lcm(1, …, n). These weights equal Λ(n): log L_n − log L_{n−1} = log p if n is a power of the prime p, and 0 otherwise. So the formula is Weil's explicit formula in Bombieri's form.

**Verdict.** PTQ is correct.

### 2.2 Lemma 25.2 (positive transfer-adjoint forms)

**Setting.** Let H = ℓ²(Z, m) with (T_nx)_ρ = n^ρx_ρ and U_n = nT_{1/n}. Let B be a bounded positive semidefinite Hermitian form on H.

**Statement.** B satisfies B(T_nx, y) = B(x, U_ny) for every integer n ≥ 1 if and only if B(x, y) = Σ_{Re ρ = ½} m_ρc_ρx_ρȳ_ρ with 0 ≤ c_ρ ≤ C.

*Proof.* The condition is equivalent to B(T_nx, T_ny) = nB(x, y), since U_nT_n = n.
1. **Off-line zeros.** At x = y = ε_ρ the condition gives (n^{2σ} − n)B(ε_ρ, ε_ρ) = 0, so B(ε_ρ, ε_ρ) = 0 when σ ≠ ½. By Cauchy–Schwarz for B, ε_ρ then pairs to zero with everything.
2. **Distinct line zeros.** For line zeros ρ = ½ + iγ and η = ½ + iγ′, the condition gives (e^{i(γ−γ′)log n} − 1)B(ε_ρ, ε_η) = 0.
3. **The step shortened here.** Suppose B(ε_ρ, ε_η) ≠ 0. Then (γ−γ′)log 2 = 2πk and (γ−γ′)log 3 = 2πl for some integers k and l.
   - If γ ≠ γ′, then k ≠ 0, and log 3/log 2 = l/k would give 3^k = 2^l, which is impossible by unique factorisation.
   - So γ = γ′, and ρ = η. PTQ4 uses the consecutive ratios (n+1)/n instead; both arguments are complete.
4. **The converse** is direct. ∎

This is the precise sense in which the positivity of the transfer adjoint is a property of line zeros, coordinate by coordinate. The receiver it defines discards the off-line coordinates by construction, both signs of each off-line pair included (PTQ5.4).

## 3. GDC: the defect closure

### 3.1 Audit

1. **The functional (GDC1.2).** σ_r(ȳ)(F) = Σm_ρF(ρ)·conj(d_r(ρ^#)y_{ρ^#}) = −Σm_ρF(ρ)e^{iγ log r}(r^σ − r^{1−σ})·conj(y_{ρ^#}). This uses d_r(ρ^#) = −d_r(ρ) (`24_` check 8).
2. **The preannihilator (GDC1.4).**
   - The single-coordinate vector y_{ρ^#} = 1/(m_ρd_r(ρ^#)) gives the functional F ↦ F(ρ).
   - So the preannihilator is exactly N_O, and ker σ_r = conj(H_L).
3. **The strong closure (GDC2).** The closure is N_O^⊥, by Hahn–Banach separation and the bidual (Q′_β)′ = Q. The bidual identity is SDT's, not re-read here.
4. **The image does not depend on r (GDC3).** D_r = D_tV_{r,t} with V bounded and invertible.
   - The explicit bounds use r^σ − r^{1−σ} = c·L_r(c), with c = σ − ½ and L_r(c) = ∫_0^1 log r·(r^{½+uc} + r^{½−uc})du between 2√r log r and (r+1)log r. These are AST6.2's bounds.
   - Their exact range is `24_` Lemma 24.5.
5. **Openness of restriction (GDC7).** For a compact absolutely convex K, the neighbourhood construction (GDC7.6), the Minkowski functional and Hahn–Banach show that R_L: X′_β → L′_β is open. Bounded sets lift by Baire and equicontinuity. I checked each step.
   - The only property of the spaces used is that bounded sets are relatively compact. SDT proves this for A and Q, and it passes to closed subspaces.
6. **The line residue (GDC8.3).** For F ∈ N_O the off-line terms vanish and ρ^# = ρ on the line, so (αp_SA_Hy)(F) = Σ_{line}m_ρF(ρ)ȳ_ρ.
7. **Covariance (GDC12).** A_H T_n = n(T_{1/n})′A_H. The conjugated multiplier at ρ^# is conj(n^{ρ^#}) = n^{1−ρ}.

**Verdict.** GDC is correct, given SDT. What GDC builds is exact: the maximal source on which the Gysin obstruction vanishes is the line part (GDC5), and the defect is killed by restriction to A_O at the cost of the kernel A_O^⊥ (GDC10). All of it is defined relative to the off-line set.

## 4. ECR and ECI: the extension-class maps

### 4.1 Audit

1. **The Gaussian embeddings (ECR1).**
   - b_t: M/𝔞 → Q, [h] ↦ [e^{ts²}h], is injective, because e^{ts²} is a unit in every local ring.
   - It is not surjective. Hitting [g_{t/2}] would need h(ρ) = e^{−tρ²/2}, of modulus e^{t(γ²−σ²)/2}, which is not polynomially bounded.
   - j is not surjective either. e₀ ∈ im j would need F ∈ B with F ≡ 1 at every zero, impossible because |γ| is unbounded.
2. **The source of e₀ (ECR3.3).** It is e^{t/4}(πt)^{−1/2}u^{−1/2}exp(−(log u − t)²/(4t)) (check 5).
3. **The pairings (ECR4.4 and ECR5.1).**
   - The residue pairing carries the factor e^{t(ρ²+(1−ρ)²)}, because g_t(ρ)·conj(g_t(ρ^#)) = e^{tρ²}e^{t(1−ρ)²}.
   - The positive form carries e^{2t(σ²−γ²)}.
   - The two weights are different and are kept apart (ECI12.6).
4. **The detection identity (ECR5.5).** 𝔡_{a,t}(e₀, e₀) = Σ_ρ m_ρe^{2t(σ²−γ²)}(a^σ − a^{1−σ})². Every term is nonnegative, and a term is zero exactly when σ = ½.
5. **The involutions (ECI1–ECI3).**
   - K₁D_a = aD_{1/a}K₁ and K₃D_a⁺ = a³D_{1/a}⁺K₃ (check 6).
   - The square of the componentwise involution, before the quotient, is (ECI3.4), with the cross terms F(s ± 2) (check 7, for arbitrary entire c and F).
6. **The functional-equation unit (ECI4.5 and ECI6.6).**
   - ζ′(1−s) = χ′(s)ζ(s)/χ(s)² − ζ′(s)/χ(s) (check 8).
   - s²ζ′(1−s) → −1 as s → 0.
7. **The Gaussian under the involution (ECI12.3).** g_t^{#₁} = e^{t(1−2s)}g_t, and d_t^{#₁} = d_t^{−1} (check 9).
8. **The separator and the defect (ECR6 and ECI9).**
   - c acts as the identity on the original class module and as 0 on the normal one. So 𝔡_{a,t}(cx, cy) = 𝔡_{a,t}(x, y).
   - The separator does not touch the defect.

**Verdict.** ECR and ECI are correct. The programme states the consequence itself (ECR6): "The multiplier that annihilates the normal localization component leaves this original class and its defect fixed."

## 5. Negative result: the programme's RH-equivalent objects

Each object in the table is defined from the set of nontrivial zeros, with the off-line part Z_O = {ρ: Re ρ ≠ ½} isolated. Each vanishes, or fills its whole ambient space, exactly when Z_O = ∅, which is RH. The reason is given in each row.

| # | Object (block) | Definition | Why it is RH-equivalent |
|---|---|---|---|
| 1 | ℛ = Q/N_O (AST2) | classes modulo those vanishing at every off-line zero | For each off-line ρ, a global isolator has a nonzero class in ℛ. If Z_O = ∅ then N_O = Q. |
| 2 | N_O = Q (GDC1) | the same condition read on the kernel | Same as row 1. |
| 3 | H_off = 0 (PTQ1) | the ℓ² coordinates at off-line zeros | By definition. |
| 4 | D_n = 0 for one, or every, n > 1 (PTQ1.2) | the multiplier e^{−iγ log n}(n^σ − n^{1−σ}) | It vanishes if and only if σ = ½. |
| 5 | W descends through q_pos (PTQ5.2) | W(x,y) = ⟨P_L x, P_L y⟩₊ + ⟨P_O x, 𝖩P_O y⟩₊ | W is nondegenerate on H, so it descends if and only if H_off = 0. |
| 6 | tr_ζ(P_off M_{k_t}) = 0 (PTQ8.3) | Σ_{Z_O}m_ρe^{−tγ²} | The weights are strictly positive. |
| 7 | 𝔡_{a,t}(e₀, e₀) = 0 (ECR5.5) | Σ_ρ m_ρe^{2t(σ²−γ²)}(a^σ − a^{1−σ})² | The terms are nonnegative, and zero only for σ = ½. |
| 8 | ker β_r = Q, equivalently the maximal Gysin-null source is all of conj(H) (AST2, GDC5) | β_r = D_r^*𝖩E, with kernel N_O (AST2); the maximal Gysin-null source is conj(H_L) (GDC5) | The defect vanishes exactly on the line; same condition as rows 1 and 4. |

**What the table shows.**
- The eight constructions reduce to three conditions. Rows 1, 2 and 8 are N_O = Q. Rows 3, 4 and 5 are H_off = 0. Rows 6 and 7 are the vanishing of a strictly positive sum over Z_O.
- The constructions are exact, and the programme defines them correctly. They are useful as targets: each says precisely what a proof of RH must make vanish.
- None of them comes with an independent way of computing it.
- The two numerical detectors, rows 6 and 7, are sums over zeros of functions of σ = Re ρ and |γ|. These are not holomorphic functions of ρ, so Weil's explicit formula, which evaluates Σ_ρ A(ρ) for holomorphic A, does not directly express them through the primes. The programme records this (PTQ8: "No assertion here inserts these nonholomorphic functions into the original holomorphic prime explicit formula"; ECR5: "No nonholomorphic multiplier has been substituted into (ECR4.6)").
- The holomorphic pairing W, which the explicit formula does compute, is indefinite on each off-line pair (PTQ5.4). That is Weil's criterion.

**Scope.** This is not a criticism of the blocks, which state these limits themselves. It records, in one place, that the positive-side constructions of AST, GDC, PTQ and ECR are reformulations of RH, not steps toward it. The step the programme names as next — to act on W_O or on AST's boundary map (SMC10, see `18_`) — needs an input beyond these constructions. Each of them only restates Z_O = ∅, and none bounds the off-line part by quantities computed independently of it.

## 6. Items for the goals

- **Goal 3 (standalone lemmas).**
  - Lemma 25.1: the exact summation image, with the explicit inverse, the Möbius form and the Taylor coefficients at 0 from the trivial zeros.
  - Lemma 25.2: positive transfer-adjoint forms are diagonal on the line zeros, with the short log 3/log 2 argument.
- **Goal 1 (negative results).**
  - The RH-equivalent objects of §5.
  - The separator fixes the original class and its defect (ECR6, ECI9), which is the programme-side form of `24_` §0 item 6.
- **Goal 4 (F₁ context).** SSI5.6 is the source-side form of goal-4 item 11: the jet of the source at 0 is read from the values at the trivial zeros.
- **Reading status.**
  - Read in full: GDC, PTQ, SSI (SSI10 in part), ECR and ECI.
  - Remaining in board task 8: GZR, OMS, DCP and CGS on the character-lifting side, then the rest of the Deligne reader and the Codex session logs.

## 7. Checks (`checks/gdc_ptq_ssi_ecr_eci_audit_checks.py`, mpmath at 40 digits)

| # | Statement | Result |
|---|---|---|
| 1 | SSI3.7: \|χ(−2N−1+it)\|² in closed form, N = 0, …, 3, four values of t | relative error ≤ 7·10⁻⁴¹ |
| 2 | SSI7.1: ½Σμ(n)(Σf₀)(nx) = f₀(x) at x = 0.5, 0.9, 1.7 (n < 60; the omitted tail is of order e^{−900π}) | error ≤ 3·10⁻⁴² |
| 3 | SSI5.6: Taylor coefficients of f₀ at 0 equal F(−2r)/(2ζ′(−2r)) = r(2r+1)(−1)^rπ^r/(2·r!), r ≤ 4; the coefficients of v⁰, v¹ and v³ vanish | error ≤ 2·10⁻³⁹ |
| 4 | SSI6.3: ∫f₀dx/x = −1/4, ∫f₀ log x dx = 1/8 | exact to working precision |
| 5 | ECR3.3: the Gaussian source of e₀ at t = 0.5, 2 and u = 0.7, 2.3 | relative error ≤ 4·10⁻⁴¹ |
| 6 | ECI2.5: K₁D_a = aD_{1/a}K₁, K₃D_a⁺ = a³D_{1/a}⁺K₃ | error ≤ 3·10⁻³⁵ |
| 7 | ECI3.4: the square of A_c before the quotient, for arbitrary entire c, F | error ≤ 10⁻⁴⁰ |
| 8 | ECI6.6: the differentiated functional equation at three points | relative error ≤ 4·10⁻⁴¹ |
| 9 | ECI12.3: g_t^{#₁} = d_tg_t and d_t^{#₁} = d_t^{−1} | error ≤ 3·10⁻⁴¹ |
| 10 | PTQ5.4: off-line pair values ±2m, signature (1,1); \|n^ρ\|² = n on the line and not off it | holds |

## 8. Sources

- The programme blocks listed at the top (commit 064f33b).
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown, Oxford 1986, §2.11 (Müntz's formula).
- R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, Mathematisches Institut, Universität Göttingen, Seminars Winter Term 2004/2005, 117–137 (arXiv:math/0412277); and R. Meyer, *On a representation of the idele class group related to primes and zeros of L-functions*, Duke Math. J. 127 (2005), 519–595 (arXiv:math/0311468). The titles and references were taken from the author's arXiv listing. Both are cited for context only; the comparison is pending.
- A. Ivić, *Some identities for the Riemann zeta-function II*, arXiv:math/0506214. Used only to confirm that Müntz's formula is Titchmarsh §2.11.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952), tome supplémentaire, 252–265. This is the source of the criterion that W is positive exactly under RH; it was cited through the programme's PTQ9 and not re-read.

## 9. Revisions after the eighth referee pass (11:53 UTC)

1. §1.1 item 1: ℳ₀Σf is entire because Σf ∈ A, not because of ℳf alone.
2. §0 item 5 and §5: the eight constructions reduce to three conditions (N_O = Q; H_off = 0; a strictly positive sum over Z_O vanishes). Rows 5 and 8 of the table now give definitions.
3. §5: the explicit formula does not *directly* express rows 6–7. The Scope paragraph no longer says "not a function of the zero set alone"; it says the constructions only restate Z_O = ∅.
4. §1.2: the referee's tool summary of Meyer's arXiv v3 (Theorems 3.3 and 4.1) is recorded and marked as a summary. The check-3 row names the tested odd coefficients, and §0 item 4 says "consistent with".
