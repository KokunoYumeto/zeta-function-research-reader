# The programme's separator, its derived separation and its off-line source: an audit of GSL, GMS and AST

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 11:20 UTC.

This note belongs to board task 8. From about 11:03 UTC the owner gave that task priority: audit the programme and extract lemmas first, then continue the work from there.

**Read in full.** All three blocks are in the zeta-function-research-reader repository at commit 064f33b, folder `workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/`.
- GSL0–GSL11: `gct-weight-control/proofs/GLOBAL_SHIFTED_ZETA_LIFT.md`.
- GMS0–GMS11: `gct-weight-control/proofs/CC_GLOBAL_MULTIPLIER_SEPARATION.md`.
- AST0–AST9: `geometric-positive-quotient/ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md`.

**Cited by these blocks, not re-read here.** S5 (the summation image, mapped in `04_`), RZ1–RZ12, CW1–CW8, CLP1–CLP13, ACD0–ACD8, SDT1–SDT4, and GDC0–GDC14 (next in board task 8).

**Checks.** `checks/gsl_gms_ast_audit_checks.py` has 13 items, and all pass; the output is in `checks/gsl_gms_ast_audit_checks_OUTPUT.txt`. The item numbers below are the numbers in that script.

## 0. Summary

1. **GSL is correct.**
   - It constructs an entire function E that has polynomial growth on every vertical strip. E is 1 to full order at every nontrivial zero ρ and 0 to full order at every ρ − 1.
   - With E, the quotient by the union of the two divisors splits continuously and equivariantly into the two quotients, and the splitting is unique.
   - The Euler product enters only through the zero-freeness of the closed half-plane Re s ≥ 1. For Re s > 1 it gives this directly, and with the functional equation it makes the line Re s = 0 separate Z from Z − 1. Near Re s = 1 it is made quantitative by the 3-4-2 inequality, which gives a thin zero-free corridor around Re s = 0 with an explicit lower bound.
   - I re-derived every estimate.
2. **GMS is correct.**
   - Let M be the ring of entire functions of polynomial growth on strips. Over M, the separator makes the two quotients Q (jets at Z) and Q₊ (jets at Z + 1) derived-orthogonal in both directions.
   - The normal row 0 → I₊ → B → Q₊ → 0 does not split, and the separator is not an idempotent of M.
3. **AST is correct.**
   - The defect of ACD vanishes exactly at the zeros on the line. So its kernel N_O, and the source ℛ = Q/N_O, do not depend on the parameter r.
   - ℛ holds one value coordinate for each off-line zero and nothing else, so ℛ = 0 if and only if RH holds. AST itself says that nothing in it decides which case holds (AST9).
4. **Lemmas extracted.**
   - 24.1: the separator lemma, stated without ζ. It needs matched exponential rates: an upper bound on strips and a lower bound in a corridor.
   - 24.2: no equivariant maps between the quotients of two disjoint divisors.
   - 24.3: the two-line product in closed form, on the line Re s = 0, which passes through the pole at 0.
   - 24.5: the exact range of the defect ratio, which sharpens AST6.2.
5. **Continued.**
   - 24.4: the separator, and with it the two-line splitting, exists for every primitive Dirichlet L-function.
   - 24.6: this proof does not reach the Davenport–Heilbronn function, because no vertical line separates its two divisors.
6. **Consequence.** The two-line splitting uses the Euler product only through the zero-freeness of Re s ≥ 1. It holds for every primitive Dirichlet L-function, and its proof never uses where the zeros lie inside the open strip. So the splitting cannot serve as a criterion for RH (or GRH).

## 1. GSL: the separator

### 1.1 What GSL proves

- **The spaces.**
  - B is the Fréchet space of entire F with b_{A,M}(F) = sup_{|Re s|≤A}(1+|Im s|)^M|F(s)| < ∞ for all A, M.
  - I, I₋ and J = I ∩ I₋ are the closed ideals of functions vanishing to full order on Z, on Z − 1, and on both.
  - F₀(s) = s(s−1)/8 · π^{−s/2}Γ(s/2)ζ(s) = ξ(s)/4, F₁(s) = F₀(s+1) and G = F₀F₁.
- **The main result (GSL0.1, GSL5).**
  - The map B/J → B/I ⊕ B/I₋ is a topological isomorphism, with inverse ([f], [g]) ↦ [Ef + (1−E)g].
  - It commutes with multiplication by s and by every a^s.
  - The equivariant section is unique (GSL6).
- **The high-weight version (GSL6.5–6.11).** With E₊(s) = 1 − E(s − 1), the same statements hold for Z and Z + 1. The weights are (0, 2) on Z, (−2, 0) on Z − 1 and (2, 4) on Z + 1.

### 1.2 Audit, step by step

1. **Exceptional values (GSL1.4–1.5).** F₀(0) = F₀(1) = 1/8, and F₀(−2r) = r(2r+1)(−1)^rπ^r ζ′(−2r)/(2·r!) = F₀(1+2r) ≠ 0. The first form comes from the residue (−1)^r/r! of Γ at −r against the simple zero of ζ at −2r (check 3, r = 1, …, 4).
2. **Growth on strips (GSL2).**
   - The Euler–Maclaurin continuation (GSL2.4) is ζ(s) = 1/(s−1) + ½ + Σ_{j=2}^{K}(s)_{j−1}P_j(1) − (s)_K∫_1^∞P_K(x)x^{−s−K}dx.
   - I re-derived its first two integrations by parts from ζ(s) = s/(s−1) − s∫_1^∞{x}x^{−s−1}dx, including the signs.
   - The remainder is at most ‖P_K‖_∞/(K−1−A) on |Re s| ≤ A. This gives |ζ| ≤ C_A(1+|t|)^K there, for |t| ≥ 1.
3. **The corridor (GSL3.1–3.4).**
   - Since (1+2cos θ)² = 3 + 4cos θ + 2cos 2θ, the Euler product gives ζ(1+δ)³|ζ(1+δ+it)|⁴|ζ(1+δ+2it)|² ≥ 1 (check 6; on the grid tested the minimum is 5.26).
   - With ζ(1+δ) ≤ 2/δ and |ζ(1+δ+2it)| ≤ CT, where T = 1 + |t|, this gives |ζ(1+δ+it)| ≥ c₀δ^{3/4}T^{−1/2}.
   - Take δ = cT^{−6}. The main term is then c₀c^{3/4}T^{−9/2}·T^{−1/2} = c₀c^{3/4}T^{−5}. The derivative correction is 2C₁Tδ = 2C₁cT^{−5}.
   - Hence |ζ(1+x+it)| ≥ (c₀c^{3/4}/2)T^{−5} for |x| ≤ cT^{−6} once 2C₁c ≤ (c₀/2)c^{3/4}. The exponents agree with GSL3.3–3.4.
4. **The closed form (GSL3.5–3.7).**
   - The functional equation gives F₀(s) = F₀(1−s), and Γ((1−s)/2)Γ((1+s)/2) = π/cos(πs/2).
   - Together they give G(s) = s²(s²−1)ζ(1−s)ζ(1+s)/(64 cos(πs/2)) (check 1, relative error 3·10⁻⁴⁰).
5. **Matched rates (GSL3.8–3.12).**
   - |cos(π(x+it)/2)|² = cos²(πx/2) + sinh²(πt/2), so 1/|cos| lies between constant multiples of e^{−π|t|/2} for |t| ≥ 1.
   - Hence |G| ≥ c₂T^{−6}e^{−π|t|/2} in the corridor, and |G| ≤ C_A(1+|t|)^{k_A}e^{−π|t|/2} on every strip.
   - Check 7 confirms both numerically: the lower bound on Re s = 0, and the upper bound on Re s = −2, ½ and 2, for 1 ≤ t ≤ 200.
6. **The ∂̄ construction (GSL4).** Put χ = η(x/r(t)), h = ∂̄χ/G on the corridor (0 off it), u = (1/π)∫e^{(s−w)²}(s−w)^{−1}h(w)dA(w), and E = χ − Gu. I checked:
   - ∂̄(1/(πs)) = δ₀ for ∂̄ = ½(∂_x + i∂_t), and e^{s²} is holomorphic with value 1 at 0, so ∂̄u = h;
   - the u-integral of 1/|s−w| over |Re w| ≤ ε is at most 2 arcsinh(ε/|y|) ≤ C(1 + log₊(1/|y|)), where y = t − Im w;
   - the Gaussian e^{−(t−v)²} dominates e^{π|t−v|/2}(1+|t−v|)^{12}.

   Hence |u| ≤ C_A e^{π|t|/2}(1+|t|)^{12}, and |Gu| grows at most polynomially: the two exponentials cancel exactly.
7. **The splitting (GSL5).**
   - The inclusions EB ⊂ I₋, (1−E)B ⊂ I, EI ⊂ J and (1−E)I₋ ⊂ J follow from the jets of E and the Leibniz rule.
   - Hence ΦΨ = 1 and ΨΦ = 1, and the quotient-seminorm estimate (GSL5.7) holds.
8. **Equivariance and uniqueness (GSL6).**
   - Substitution gives T_{a,−}Ū = a^{−1}ŪT_a and L₋Ū = Ū(L − 1).
   - The uniqueness argument is re-derived as Lemma 24.2 below.
9. **The union resolvent (GSL7.4).** (λ − s)R^∪_λF = F − G·F(λ)/G(λ), which is ≡ F mod J because G ∈ J.
10. **Mellin transport and units (GSL8–GSL9).**
    - ℳ(uk)(s) = ℳk(s+1).
    - ζ is a unit on −1 < Re s < 0, by ζ(s) = C(1−s)ζ(1−s)/C(s), because Re(1−s) > 1 there.

**Verdict.** GSL is correct, and I found no gap. The corridor width T^{−6} is much cruder than the classical zero-free region of width c/log T (Davenport, *Multiplicative Number Theory*, ch. 13). Any polynomial width suffices for the construction.

### 1.3 Lemma 24.1 (the separator lemma, stated without ζ)

**Hypotheses.** Let G ∈ B have zero divisor D₊ ⊔ D₋, with D₊ ⊂ {Re s > 0} and D₋ ⊂ {Re s < 0}. Suppose there are α ≥ 0, ε > 0 and integers N, K ≥ 0 such that, with r(t) = ε(1+t²)^{−N}:
- (a) **upper rate on strips:** for every A there are C_A and k_A with |G(x+it)| ≤ C_A(1+|t|)^{k_A}e^{−α|t|} for |x| ≤ A;
- (b) **lower rate in the corridor:** G has no zeros in 𝒦 = {|x| ≤ r(t)}, and |G(x+it)| ≥ c(1+|t|)^{−K}e^{−α|t|} on 𝒦.

**Conclusion.** There is an entire E with |E| + |1 − E| ≤ C′_A(1+|t|)^{d_A} on |x| ≤ A, such that E − 1 vanishes to full order on D₊ and E vanishes to full order on D₋. Consequently I_{D₊} + I_{D₋} = B, and B/(I_{D₊} ∩ I_{D₋}) → B/I_{D₊} ⊕ B/I_{D₋} is a topological isomorphism with inverse ([f],[g]) ↦ [Ef + (1−E)g].

*Proof.* This is GSL4–GSL5 with the constants left general.
1. **The cutoff.** Put χ(x+it) = η(x/r(t)). Then ∂̄χ = ½η′(x/r)(1/r − ixr′/r²). On 𝒦 we have |xr′/r²| ≤ |r′/r| = 2N|t|/(1+t²) ≤ N, so |∂̄χ| ≤ C(1+|t|)^{2N}.
2. **The ∂̄ solution.** By (b), h = ∂̄χ/G satisfies |h| ≤ C(1+|t|)^{2N+K}e^{α|t|}, with support in 𝒦 ⊂ {|x| ≤ ε}. Step 6 of §1.2 gives |u(x+it)| ≤ C_A(1+|t|)^{2N+K}e^{α|t|}.
3. **The bound on E.** By (a), |Gu| ≤ C(1+|t|)^{k_A+2N+K}, and |χ| ≤ 1.
4. **The jets.** Since 𝒦 has no zeros and contains the line x = 0, the divisor D₊ lies to the right of 𝒦, where χ = 1, and D₋ lies to the left, where χ = 0. Near either divisor h = 0, so u is holomorphic there. So E − 1 = −Gu near D₊ and E = −Gu near D₋, and G vanishes there to full order.
5. **The splitting.** This is GSL5 verbatim. ∎

**The matching of the two rates is what the method uses.** Suppose the lower bound in (b) had rate e^{−α₂|t|} with α₂ > α. Then the same estimates give only |Gu| ≤ C(1+|t|)^{k}e^{(α₂−α)|t|}, and E would not be shown to lie in M. For G = F₀F₁ the two rates coincide at α = π/2. The reason is the closed form of Lemma 24.3: its only exponential factor, 1/cos(πs/2), has the same size on every vertical line.

### 1.4 Lemma 24.2 (no equivariant maps across disjoint divisors)

**Statement.** Let D ⊂ ℂ be the zero divisor of some F_D ∈ B, and let D′ be a divisor with D ∩ D′ = ∅. Put Q = B/I_D and Q′ = B/I_{D′}, and let L and L′ be multiplication by s on each. Then every linear H: Q → Q′ with HL = L′H is zero. Continuity is not needed.

*Proof.*
1. **λ − L is invertible on Q for λ ∉ D.** Put R_λF = (F − F_D·F(λ)/F_D(λ))/(λ − s). The numerator vanishes at s = λ, so R_λF is entire. It lies in B: away from λ, divide by |λ − s| ≥ 1; on |s − λ| ≤ 1, use the maximum principle. R_λ preserves I_D. Moreover (λ − s)R_λF ≡ F mod I_D and R_λ((λ − s)F) = F. So R_λ inverts λ − L on Q. (This is the formula of RZ3 and GSL7.4, verified here directly.)
2. **The jets of H(x) vanish on D′.** Let λ ∈ D′ have multiplicity m. For x ∈ Q, (L′ − λ)^m H(x) has zero m-jet at λ. It equals H((L − λ)^m x), and (L − λ)^m is onto Q by step 1. So every H(y) has zero m-jet at every λ ∈ D′. That is, H(y) ∈ I_{D′}, so H = 0. ∎

This is the uniqueness argument of GSL6, with D = Z and D′ = Z ∓ 1. It needs only commutation with L, not with all of M, and no continuity. So it is stronger than the degree-0 case of GMS4.4.

### 1.5 Lemma 24.3 (the two-line product on the line Re s = 0)

- G(s) = F₀(s)F₀(s+1) = s²(s²−1)ζ(1−s)ζ(1+s)/(64 cos(πs/2)).
- G(0) = 1/64 = F₀(0)F₀(1).
- G(it) = |F₀(1+it)|² > 0 for real t.

*Proof.*
1. The closed form is (GSL3.5–3.7) (check 1).
2. G(0) = F₀(0)F₀(1) = (1/8)(1/8) = 1/64.
3. For real t, F₀(it) = F₀(1−it), which is the complex conjugate of F₀(1+it), because F₀ is real on the real axis. F₀(1+it) ≠ 0 because ζ does not vanish on Re s = 1 (check 2). ∎

The separator switches from 0 to 1 across the line Re s = 0. That line passes through s = 0, where the pole at 0 of the register (goal 4, item 11) sits. On that line, G is built only from values of ζ on Re s = 1, where the Euler product's boundary nonvanishing holds. The positivity G(it) > 0 is also `22_` Prop. 22.4 (S37); `22_` was refereed in the eighteenth pass.

## 2. GMS: the derived separation

### 2.1 What GMS proves

- **The ring and the separator.** Let M be the ring of entire functions of polynomial growth on every vertical strip. B, I, I₊, Q = B/I and Q₊ = B/I₊ are M-modules. The separator is c(λ) = 1 − E(λ − 1) ∈ M. It is 1 to full order on Z and 0 to full order on Z + 1.
- **Derived separation (GMS4.4).** RHom_M(Q, Q₊) ≃ 0 and RHom_M(Q₊, Q) ≃ 0.
- **The normal ideal and the normal row.**
  - RHom_M(Q, I₊) → RHom_M(Q, B) is a quasi-isomorphism, with explicit inverse β_*, where β = multiplication by c (GMS5.4).
  - The normal row does not split, and its class dies under pushout along c (GMS6).
- **Strict extensions.** Every strict Fréchet M-extension of Q by Q₊ splits uniquely and continuously (GMS7).
- **The simultaneous complexes.** The M-action extends to them (GMS9).

### 2.2 Audit

1. **The source vector (GMS2.5).**
   - ∫_0^∞ f₀(v)v^{s−1}dv = (1/4)π^{−s/2}[2Γ(s/2+2) − 3Γ(s/2+1)].
   - Since 2Γ(s/2+2) − 3Γ(s/2+1) = Γ(s/2)(s/2)(2(s/2+1) − 3) = Γ(s/2)(s/2)(s−1), this equals s(s−1)/8 · π^{−s/2}Γ(s/2).
   - f₀ is even and f₀(0) = 0. ∫f₀ = 0 because the Mellin transform vanishes at s = 1 (check 4).
2. **The translated factor (GMS2.11).** F₊(0) = F₀(−1) = π/24 (check 3).
3. **The separator is not an idempotent (GMS3).** An entire c with c² = c is constant, because c(c − 1) = 0 on a connected domain. The separator takes both values 0 and 1, so it is not constant.
4. **The homotopy (GMS4.1–4.3).** For f of degree n, D(Hf) + H(Df) = [(−1)^n d_N f h + f h d_P] + [(−1)^{n+1} d_N f h + f d_P h] = f(hd_P + d_Ph) = f a_P = a_N f. I re-derived this identity.
5. **Degree 0 of GMS5.5.** Hom_M(Q, B) = 0 because 1 − c kills Q, and multiplication by the nonzero entire function 1 − c is injective on B.
6. **The Poisson identity (GMS9.1).** Σĝ(u) = u^{−1}Σg(u^{−1}) + u^{−1}g(0) − ∫g, where Σf(u) = 2Σ_{n≥1}f(nu) (check 5, for two Gaussians).
7. **The reflection.** R: b(u) ↦ u^{−1}b(u^{−1}) becomes F(s) ↦ F(1−s) under Θ.
8. **The degree statements (GMS10).**
   - The antipodal map −1/z̄ has degree −1 on S² and restricts to z ↦ −z, of degree +1, on the equator.
   - The map −1/z has degree +1 on S² and restricts to z ↦ −z̄, of degree −1, on the equator.

**Verdict.** GMS is correct.

### 2.3 Lemma (coprime annihilators; the content of GMS4)

**Statement.** Let a be a central element of a ring that acts as 0 on a module X and as the identity on a module N. Then RHom(X, N) ≃ 0.

*Proof.* Take a projective resolution P → X. Lift the action of a on P to a null-homotopy h with d_Ph + hd_P = a_P; this is possible because a_X = 0. Then item 4 of §2.2 gives D(Hf) + H(Df) = a_N f = f. So the Hom complex is contractible. ∎

- This is standard homological algebra. GMS proves it directly, with an explicit choice-free bar-resolution homotopy (GMS4.5–4.9).
- In the programme it gives the derived separation of Q and Q₊ with a = 1 − c, and of Q₊ and Q with a = c. That separation holds for any two coprime closed ideals that a multiplier separates; it has no zeta-specific content (as recorded in `18_`).

### 2.4 Negative result: B itself does not split along the two lines

Two facts are proved.

1. **The normal row 0 → I₊ → B → Q₊ → 0 has no M-linear section (GMS6.3).** GMS6.3 uses one torsion element, (λ − ρ − 1)[v_ρ] = 0. The variant below uses that all of Q₊ is torsion.
   - Every class in Q₊ is killed by F₊ = F₀(· − 1) ∈ B ⊂ M, because F₊ vanishes to full order on Z + 1. So Q₊ is a torsion M-module.
   - B is torsion-free: a nonzero entire function times a nonzero entire function is nonzero.
   - Hence Hom_M(Q₊, B) = 0. Since Q₊ ≠ 0, the row cannot split. (Q₊ ≠ 0 because Z ≠ ∅ and e^{s²} ∈ B does not vanish at ρ₁ + 1. Check 10, F₀′(ρ₁) ≠ 0, is the fact GMS's element v_ρ needs.)
2. **The separator is not an idempotent of M** (§2.2 item 3).

So the two lines are separated only after passing to the quotients Q and Q₊. The coefficient space B does not split along them, and no idempotent of M does the separating.

## 3. AST: the off-line source

### 3.1 What AST proves

- **The defect.**
  - Let H = ℓ²(Z, m) with ⟨x, y⟩₊ = Σm_ρx_ρȳ_ρ, and (EF)_ρ = F(ρ).
  - Let (𝖩y)_ρ = y_{ρ^#} with ρ^# = 1 − ρ̄, and let T_t act by t^ρ on the coordinate ρ.
  - For r > 1, the defect of ACD is D_r = T_r^* − rT_{1/r}, with eigenvalue d_r(ρ) = e^{−i Im ρ log r}(r^{Re ρ} − r^{1−Re ρ}).
  - Put β_r = D_r^*𝖩E, so that (β_rF)_ρ = conj(d_r(ρ))·F(ρ^#).
- **Its kernel (AST2).**
  - ker β_r = N_O := {F: F(ρ) = 0 for every off-line ρ}, the same for every r > 1.
  - ℛ = Q/N_O ≅ A/A_O.
  - On a block ℂ[z]/z^m, ℛ keeps exactly one value coordinate at an off-line zero and nothing at an on-line zero.
- **Its dual (AST3–AST8).**
  - ℛ is Montel Fréchet, and its strong dual is N_O^⊥ with strict exact rows.
  - β̄_r: ℛ → H_O is injective with dense image. The positive-sign boundary is +β̄_r and the cone boundary is −β̄_r (AST5.2a–b).
  - Changing the parameter is a bounded invertible diagonal map (AST6).
- **Scope (AST9).** If an off-line zero exists, its value class in ℛ is nonzero; if none exists, ℛ = 0. AST does not decide which case holds.

### 3.2 Audit

1. **The eigenvalue.** On H, (T_r^*y)_ρ = r^{ρ̄}y_ρ and (rT_{1/r}y)_ρ = r^{1−ρ}y_ρ. So d_r(ρ) = r^{ρ̄} − r^{1−ρ} = e^{−iγ log r}(r^β − r^{1−β}), where ρ = β + iγ (check 8).
2. **The kernel.** d_r(ρ) = 0 if and only if r^β = r^{1−β}, that is, β = ½, since r > 1. The involution # preserves the off-line set. So ker β_r = N_O, independent of r.
3. **The reindexing in AST4.4.** d_r(ρ^#) = −d_r(ρ), since ρ^# = (1−β) + iγ, and m_{ρ^#} = m_ρ (check 8).
4. **The bounds of AST6.2.** They hold. Lemma 24.5 below gives the exact range, and check 9 tests both on a grid: no violations, over the 12 pairs r ≠ t with r, t ∈ {1.1, 2, 5, 30} and 998 values of β.
5. **The sign bookkeeping.** In AST5.2a–b, the short-exact-sequence boundary is +b_ra. In the cone convention the cocycle (a, −b_ra) projects to −b_ra. I re-derived both.
6. **This confirms `18_` as corrected in the sixth referee pass.** ℛ holds only off-line values, and ℛ = 0 if and only if RH holds.

**Verdict.** AST is correct as far as I checked it. The functional-analytic parts (Montel property, strong duals, strict rows) rest on SDT and GDC7, which I have not re-read; they are next.

### 3.3 An exact identity: the defect is a zero minus its reflected partner

- d_r(ρ) = conj(r^ρ − r^{ρ^#}), where ρ^# = 1 − ρ̄.
- In particular |d_r(ρ)| = |r^ρ − r^{ρ^#}|.

*Proof.* conj(r^ρ − r^{1−ρ̄}) = r^{ρ̄} − r^{1−ρ} (check 8). ∎

So the ACD/AST defect at scale r is the difference between the scaling eigenvalue of a zero and that of its partner under s ↦ 1 − s̄. It vanishes exactly when the zero is its own partner. In the dictionary of `22_` this partner is the owner's anti-number. That note was refereed in the eighteenth pass; this correspondence is not followed up here (`42_` treats the continuation directions of `22_` §5).

### 3.4 Lemma 24.5 (the exact range of the defect ratio)

**Statement.** Let r, t > 1 with r ≠ t, and let ρ = β + iγ with 0 < β < 1 and β ≠ ½. Put x = β − ½ and a = log r, b = log t. Then:
- (a) |d_r(ρ)/d_t(ρ)| = √(r/t) · sinh(ax)/sinh(bx);
- (b) this is a strictly monotone function of |x| on (0, ½): increasing if r > t, decreasing if r < t;
- (c) its values lie strictly between √(r/t)·log r/log t (the limit as x → 0) and (r−1)/(t−1) (the value at |x| = ½);
- (d) both ends are approached, so this is the exact range as β runs over (0, ½) ∪ (½, 1). It is a statement about admissible positions, not about actual zeros;
- (e) AST6.2's bounds 2√r log r/((t+1)log t) ≤ |v_{r,t}| ≤ (r+1)log r/(2√t log t) follow from (c).

*Proof.*
1. **(a).** r^β − r^{1−β} = √r(r^x − r^{−x}) = 2√r sinh(ax), and likewise for t.
2. **(b).** The derivative of log(sinh(ax)/sinh(bx)) is a coth(ax) − b coth(bx). For fixed x > 0, the function c ↦ c coth(cx) is strictly increasing, because its derivative is (½sinh(2cx) − cx)/sinh²(cx) > 0.
3. **(c).** As x → 0, sinh(ax)/sinh(bx) → a/b, so the ratio tends to √(r/t)·a/b. At |x| = ½, sinh(a/2) = (r−1)/(2√r), so the value there is √(r/t)·[(r−1)/(2√r)]/[(t−1)/(2√t)] = (r−1)/(t−1).
4. **(e).**
   - For y > 1 write y = e^{2w}. Then (y−1)/√y = 2 sinh w > 2w = log y, and 2(y−1)/(y+1) = 2 tanh w < 2w = log y. So 2(y−1)/(y+1) < log y < (y−1)/√y.
   - The lower bound: 2√r log r/((t+1)log t) is at most √(r/t)·log r/log t, because 2√t ≤ t + 1. It is also below (r−1)/(t−1), by the two log inequalities.
   - The upper bound follows symmetrically. ∎

**How much sharper.** For r = 2, t = 30 the exact range is (0.0345, 0.0526); AST6.2 gives [0.0186, 0.0558]. The improvement is modest. What the lemma adds is that the range is exact and that it is reached at the two ends: near the line, and at the edge of the strip.

## 4. Continuing from GSL: which L-functions have a separator

### 4.1 Proposition 24.4 (the separator for every primitive Dirichlet L-function)

**Setting.** Let χ be a primitive Dirichlet character modulo q ≥ 3, with χ(−1) = (−1)^a and a ∈ {0, 1}. Put Λ_χ(s) = (q/π)^{(s+a)/2}Γ((s+a)/2)L(s,χ) and G_χ(s) = Λ_χ(s)Λ_χ(s+1). Let Z_χ be the zero divisor of Λ_χ, and let I_χ and I_{χ,−} be the closed ideals of B of full-order vanishing on Z_χ and on Z_χ − 1.

**Statement.** There is E_χ ∈ M that is 1 to full order on Z_χ and 0 to full order on Z_χ − 1. Consequently B/(I_χ ∩ I_{χ,−}) → B/I_χ ⊕ B/I_{χ,−} is a topological isomorphism, and it commutes with s and with every a^s. For q = 1, that is ζ with the factor s(s−1)/8, this is GSL.

*Proof.* I verify the hypotheses of Lemma 24.1 with α = π/2. The standard facts used are:
- (F1) Λ_χ is entire and Λ_χ(s) = W(χ)Λ_χ̄(1−s) with |W(χ)| = 1 (Davenport, ch. 9);
- (F2) L(1+it, χ) ≠ 0 for all real t (Davenport, chs. 4 and 6 for t = 0, and ch. 14);
- (F3) Stirling's formula: |Γ(σ+it)| lies between constant multiples of |t|^{σ−½}e^{−π|t|/2} for σ in a compact set and |t| ≥ 1 (Davenport, ch. 10).

The steps are:
1. **Polynomial growth on strips.** S(x) = Σ_{n≤x}χ(n) is bounded and q-periodic, so it is the constant m_S plus a q-periodic function S₀ of mean zero. Partial summation gives L(s,χ) = s∫_1^∞S(x)x^{−s−1}dx for Re s > 0. Repeated integration by parts against the periodic antiderivatives of S₀ of mean zero continues L to every half-plane, with |L(s,χ)| + |L′(s,χ)| ≤ C_{A,q}(1+|t|)^{K} on |Re s| ≤ A. This is GSL2's argument with P₁ replaced by S₀. By (F3), Λ_χ ∈ B. Near Re s = 1 a linear bound is also needed. For 3/4 ≤ σ ≤ 2 and |t| ≥ 1, differentiating L(s,χ) = s∫_1^∞S(x)x^{−s−1}dx gives |L′(s,χ)| ≤ ‖S‖_∞(1/σ + |s|/σ²) ≤ ‖S‖_∞(4/3 + 16|s|/9) ≤ C₁T, with T = 1 + |t|. This is the analogue of (GSL2.2).
2. **The divisors are separated by Re s = 0.** By the Euler product and (F2), L(s,χ) ≠ 0 for Re s ≥ 1, and the Gamma factor has no zeros. By (F1), Λ_χ ≠ 0 for Re s ≤ 0. So Z_χ ⊂ {0 < Re s < 1} and Z_χ − 1 ⊂ {−1 < Re s < 0}.
3. **The upper rate (a).**
   - By (F1), G_χ(s) = W(χ)(q/π)^{1+a}·Γ((1+a−s)/2)Γ((1+a+s)/2)·L(1−s,χ̄)L(1+s,χ).
   - The Gamma product is π/cos(πs/2) when a = 0, and (πs/2)/sin(πs/2) when a = 1 (check 11). For |t| ≥ 1 and |Re s| ≤ A its modulus is at most C_A(1+|t|)e^{−π|t|/2}.
   - With step 1, |G_χ(x+it)| ≤ C_A(1+|t|)^{k_A}e^{−π|t|/2} on |x| ≤ A. For |t| ≤ 1 the bound follows by compactness.
4. **The lower rate (b), for |t| ≥ 1.**
   - For σ = 1 + δ > 1, the logarithm of ζ(σ)³|L(σ+it,χ)|⁴|L(σ+2it,χ²)|² equals Σ_pΣ_k p^{−kσ}k^{−1}·[3 + 4Re(χ(p)^kp^{−ikt}) + 2Re(χ(p)^{2k}p^{−2ikt})]. Here L(s,χ²) = Σχ(n)²n^{−s}, possibly imprimitive.
   - Each bracket is (1 + 2cos θ)² ≥ 0 when p ∤ q, and 3 when p | q. So the product is at least 1.
   - For |t| ≥ 1, L(σ+2it,χ²) is at most CT for 3/4 ≤ σ ≤ 2. This is step 1 applied to the primitive character inducing χ², times a finite Euler product; if χ² is principal, the argument of GSL2 for ζ gives the bound, since |2t| ≥ 2 keeps away from the pole.
   - Hence |L(1+δ+it,χ)| ≥ cδ^{3/4}T^{−1/2}. With the linear derivative bound of step 1, the computation of §1.2 item 3 gives |L(1+x+it,χ)| ≥ cT^{−5} for |x| ≤ cT^{−6}.
   - The same bound holds for L(1−x−it, χ̄), which is the complex conjugate of L(1−x+it, χ).
   - The Gamma product has modulus at least ce^{−π|t|/2} in the corridor. So |G_χ| ≥ cT^{−10}e^{−π|t|/2} there.
5. **The lower rate (b), for |t| ≤ 1.** G_χ(it) = Λ_χ(it)Λ_χ(1+it). Here Λ_χ(1+it) ≠ 0 by (F2), and Λ_χ(it) = W(χ)Λ_χ̄(1−it) ≠ 0 by (F1) and (F2). (At t = 0 with a = 0, the pole of Γ(s/2) is cancelled by the trivial zero of L(s,χ) at s = 0.) Compactness gives a zero-free neighbourhood of the segment, with a positive lower bound.
6. **Conclusion.** Lemma 24.1 applies with r(t) = ε(1+t²)^{−3} for small ε. ∎

Check 12 confirms the matched rates on the line Re s = 0 for 0.5 ≤ t ≤ 60, for χ mod 5 with χ(2) = i (odd) and for the even real primitive character (2/n) mod 8. There, |G_χ(it)|e^{πt/2} lies between 4.48 and 1.27(1+t)⁴.

### 4.2 Proposition 24.6 (the Davenport–Heilbronn function is out of reach of this proof)

**Setting.** Let f = ½(1 − iκ)L(s,χ) + ½(1 + iκ)L(s,χ̄), with χ mod 5, χ(2) = i and κ = (√(10−2√5) − 2)/(√5 − 1). This is the function of `22_` 22.10. Let Λ_f(s) = (5/π)^{(s+1)/2}Γ((s+1)/2)f(s), and let Z_f be the zero divisor of Λ_f.

**Statement.**
- (i) Λ_f satisfies Λ_f(s) = Λ_f(1−s) and conj Λ_f(s̄) = Λ_f(s) (`22_` checks 9a–9c). Hence G_f(s) = Λ_f(s)Λ_f(s+1) satisfies the upper rate (a) of Lemma 24.1 with α = π/2, by §4.1 step 3.
- (ii) f has zeros with Re s > 1.
- (iii) Z_f contains points with Re s < 0, and Z_f − 1 contains points with Re s > 0. So no vertical line separates Z_f from Z_f − 1, the hypotheses of Lemma 24.1 fail for every vertical line, and GSL's construction does not apply to f.

Whether the CRT splitting itself fails for f is not decided here.

*Proof.*
1. **(ii), the input.** Saias and Weingartner (Acta Arith. 140 (2009) 335–344; arXiv:0807.0783) prove the following for a Dirichlet series F_a with periodic coefficients that is not of the form P(s)L(s,ψ), with P a Dirichlet polynomial. Their abstract states that there is η = η(a) > 0 such that, for all ½ < σ₁ < σ₂ < 1 + η, the number of zeros with σ₁ < Re s < σ₂ and |Im s| ≤ T lies between c₁T and c₂T for all sufficiently large T. Taking σ₁ = 1 gives infinitely many zeros with 1 < Re s < σ₂.
2. **(ii), f is not of that form.** f has 5-periodic coefficients a_n = cχ(n) + c̄χ̄(n), where c = (1 − iκ)/2. Suppose f = P(s)L(s,ψ), and let P have coefficients b(n) supported on n ≤ N.
   - Take a prime p > N that is coprime to 5 and to the modulus of ψ. Comparing the coefficients of p and p² gives A_p := cx + c̄x̄ = b(1)ψ(p) and B_p := cx² + c̄x̄² = b(1)ψ(p)², where x = χ(p). Hence A_p² = b(1)B_p.
   - For p ≡ 1 (mod 5), x = 1 and A = B = 2Re c = 1, so b(1) = 1.
   - For p ≡ 2 (mod 5), x = i, A = −2Im c = κ and B = −2Re c = −1, so b(1) = −κ² ≠ 1.
   - b(1) = 0 is impossible, since A_p = 1 for p ≡ 1 (mod 5). Both residue classes contain infinitely many primes (Dirichlet). This is a contradiction (check 13).
3. **(iii).** Let ρ be a nonreal zero with Re ρ > 1. Such zeros exist: step 1 gives at least c₁T zeros with 1 < Re s < σ₂ and |Im s| ≤ T, while f has only finitely many real zeros in [1, σ₂]. Then ρ − 1 ∈ Z_f − 1 has positive real part. By (i), Λ_f(1 − ρ̄) = conj Λ_f(ρ) = 0. The Gamma factor is finite and nonzero at nonreal points, so 1 − ρ̄ ∈ Z_f, and its real part is negative. A vertical line Re s = c separating the divisors would need c < Re(1 − ρ̄) < 0 and c > Re(ρ − 1) > 0 at once. ∎

**What this locates.** Prop. 24.4 and Prop. 24.6 together locate the input that *this proof* uses: the zero-freeness of the closed half-plane Re s ≥ 1.
- For Re s > 1 it comes from the Euler product.
- On Re s = 1 it is made quantitative by the 3-4-2 inequality.
- With the functional equation it confines the divisor to 0 < Re s < 1 and yields the corridor.

The Gamma factor is the same for f and for L(s,χ), so it does not distinguish them. Whether a functional equation of the right shape suffices for the splitting itself is not decided here.

## 5. Items for the goals

- **Goal 3 (standalone lemmas).**
  - Lemma 24.1: the separator lemma with matched rates.
  - Prop. 24.4: the two-line splitting for every primitive Dirichlet L-function.
  - Lemma 24.2: no equivariant maps across disjoint divisors, needing only commutation with s.
  - Lemma 24.5: the exact range of the defect ratio.
  - Lemma 24.3: the closed form of the two-line product.
- **Goal 1 (negative results with scope).**
  - The two-line splitting of GSL/GMS holds for every primitive Dirichlet L-function, and its proof never uses where the zeros lie inside the open strip. Its only arithmetic input is the zero-freeness of Re s ≥ 1, made quantitative near Re s = 1. So it cannot serve as a criterion for RH or GRH (§0 item 6, Prop. 24.4).
  - B does not split along the two lines: the normal row has no M-linear section, and the separator is not an idempotent (§2.4).
  - This proof of the splitting does not reach the Davenport–Heilbronn function, whose divisors Z and Z − 1 are not separated by any vertical line (Prop. 24.6).
  - AST's ℛ vanishes if and only if RH holds, and AST does not decide which (AST9; `18_` confirmed).
- **Goal 2 (bridges).** The ACD/AST defect is d_r(ρ) = conj(r^ρ − r^{ρ^#}) (§3.3). It is the same involution ρ ↦ 1 − ρ̄ that `13_` and `17_` use for the pivot at ½. The correspondence with `22_`'s anti-numbers is not followed up here; `42_` treats the continuation directions of `22_` §5.
- **Reading status.** GSL, GMS and AST have now been read in full. The remaining unread blocks of board task 8 are GDC, PTQ, SSI, ECI and ECR, and on the character-lifting side GZR, OMS, DCP and CGS.

## 6. Checks (`checks/gsl_gms_ast_audit_checks.py`, mpmath at 40 digits)

| # | Statement | Result |
|---|---|---|
| 1 | G(s) = s²(s²−1)ζ(1−s)ζ(1+s)/(64 cos(πs/2)) at five points | relative error ≤ 3.4·10⁻⁴⁰ |
| 2 | G(0) = 1/64; G(it) = \|F₀(1+it)\|² > 0 at t = 1, 10, 50, 120 | errors ≤ 2.1·10⁻⁴¹ |
| 3 | F₀(−1) = F₀(2) = π/24; F₀(−2r) = r(2r+1)(−1)^rπ^rζ′(−2r)/(2·r!) = F₀(1+2r), r ≤ 4 | error ≤ 2·10⁻⁴¹ |
| 4 | Mellin transform of f₀ equals s(s−1)/8·π^{−s/2}Γ(s/2) at four points; ∫f₀ = 0 | error ≤ 10⁻³⁵ |
| 5 | Poisson identity of GMS9.1 for two Gaussians at u = 0.7, 1.3 | error ≤ 10⁻⁴¹ |
| 6 | (1+2cos θ)² = 3 + 4cos θ + 2cos 2θ; the 3-4-2 product ≥ 1 on 597 grid points | minimum 5.26 |
| 7 | \|G(it)\|e^{πt/2} ≥ 0.0717 on [1, 200]; \|G(x+it)\|e^{πt/2} ≤ 2.11·10⁻⁵(1+t)^{12} on three lines | holds |
| 8 | d_r(ρ) = r^{ρ̄} − r^{1−ρ}; \|d_r(ρ)\| = \|r^ρ − r^{ρ^#}\|; d_r(ρ^#) = −d_r(ρ) | error ≤ 7.1·10⁻³⁹ |
| 9 | AST6.2 bounds, the exact range and monotonicity of Lemma 24.5 | no violations over 12 pairs r ≠ t in {1.1, 2, 5, 30} (plus 4 trivial diagonal pairs) × 998 values of β |
| 10 | F₀′(ρ₁) ≠ 0 at the first zero | \|F₀′(ρ₁)\| = 3.46·10⁻⁴ |
| 11 | Gamma reflection products for both parities | relative error ≤ 1.4·10⁻⁴⁰ |
| 12 | Matched rates for G_χ on Re s = 0 (χ mod 5 odd; the even real primitive character (2/n) mod 8) | between 4.48 and 1.27(1+t)⁴ |
| 13 | The Davenport–Heilbronn function is not P(s)L(s,ψ): b(1) = 1 against b(1) = −κ² = −0.0807 | contradiction confirmed |

## 7. Sources

- The programme blocks listed at the top (commit 064f33b).
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer GTM 74 (2000). The chapter titles were checked against the table of contents in the Deutsche Nationalbibliothek record: ch. 4 (primes in arithmetic progression, general modulus), ch. 6 (the class number formula), ch. 9 (the functional equation of the L-functions), ch. 10 (properties of the Γ function), ch. 13 (a zero-free region for ζ(s)) and ch. 14 (zero-free regions for L(s,χ)).
- E. Saias and A. Weingartner, *Zeros of Dirichlet series with periodic coefficients*, Acta Arith. 140 (2009), no. 4, 335–344 (arXiv:0807.0783). Read through its abstract only.
- A. R. Booker and F. Thorne, *Zeros of L-functions outside the critical strip*, Algebra & Number Theory 8 (2014), no. 9, 2027–2042, with a published correction. Read through its abstract only, which says that the proof adapts and extends Saias–Weingartner's degree-1 result. It is cited here for context, not used.
- M. Righetti, *Zeros of combinations of Euler products for σ > 1*, arXiv:1412.6331. Read through its abstract and introduction only. It reports that Booker and Thorne cover polynomial, not only linear, combinations with at least two distinct nonzero terms; for automorphic L-functions of GL_r with r ≥ 2 their result is conditional on the generalized Ramanujan conjecture.
- The AMS copy of E. P. Balanzario and J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample* (Math. Comp. 76 (2007)), returned HTTP 403 and was not read.

## 8. Revisions after the eighth referee pass (11:53 UTC)

One subagent refereed `24_`–`26_` and re-ran the three check scripts; their outputs were byte-identical to the stored ones. It made one major finding and eight minor ones in all three notes, and nothing broke a lemma or proposition. Applied here:
1. **Major.** §4.2 "What this locates" overstated what Props. 24.4 and 24.6 show. It now locates the input of *this proof* (zero-freeness of Re s ≥ 1). It notes that the Gamma factor does not distinguish f from L(s,χ), and it leaves open whether a functional equation of the right shape suffices for the splitting itself.
2. §0 items 1 and 6 and §5: the Euler product enters through the zero-freeness of Re s ≥ 1, not only near Re s = 1. The splitting "cannot serve as an RH criterion", replacing "cannot distinguish".
3. Prop. 24.4: the linear bound |L′(s,χ)| ≤ C₁T near Re s = 1 is now proved in step 1, and step 4 cites it. C_A replaces C in step 3.
4. Prop. 24.6: Z_f is defined, the zero ρ is chosen nonreal (with the reason such zeros exist), and "(and for its translates)" is removed. The Saias–Weingartner statement now says |Im s| ≤ T, T large, η = η(a).
5. Numbers in §6 are rounded in the safe direction, check 9 counts 12 off-diagonal pairs, and the character mod 8 is named as (2/n).
6. §2.4 credits GMS6.3 as a torsion argument, and gives the correct reason that Q₊ ≠ 0.
7. Lemma 24.2 needs no continuity (it now says "every linear H"), and step 1 uses the maximum principle. The wording of Lemma 24.5(c)–(d) is corrected, and "the line of the pole at 0" is replaced by "the line Re s = 0, which passes through the pole at 0".
8. Sources: the Booker–Thorne correction, and Righetti's description of the polynomial and conditional scope of Booker–Thorne.
