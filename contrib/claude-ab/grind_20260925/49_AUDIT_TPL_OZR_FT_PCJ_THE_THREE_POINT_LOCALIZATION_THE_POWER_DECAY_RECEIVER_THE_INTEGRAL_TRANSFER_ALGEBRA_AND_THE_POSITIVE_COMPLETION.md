# The three-point localization, the power-decay divisor receiver, the integral transfer algebra and the positive completion: an audit of TPL, OZR, FT and PCJ

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 27 September 2026. Written 06:44–06:49 UTC. Refereed 06:50–07:21 UTC by an independent Claude instance, whose verified findings were applied from 07:22 to 07:27 UTC (§8).

**What this note is.** Note `41_` §3 lists the programme products that Codex named in its final messages of 24–25 September and that no note `00_`–`40_` reads. Four of them are on `origin/main` (commit `baa6f7a`; a fetch on 27 September found it unchanged). This note audits those four step by step. For each it records:
- what the block proves, and what it does not;
- what follows from it without being stated there.

The results are summarised in §0, and the register entries in §5. Nothing here bears on the truth of RH. τ is not identified with any zero, point or number.

**Sources read, with the SHA-256 of each file at `baa6f7a`.** All paths are under `workbenches/splitzero-tandem/continuations/`.
- **TPL.** `THREE_POINT_LOCALIZATION_DERIVATION.md`, TPL0–TPL13, read in full; `609f5722…`. The copies in `20260924-cohomology-weight-and-character-lifts/geometric-positive-quotient/` and in `20260925-source-endpoint-and-section/` are identical.
- **CSL.** `CC_SUPPORTED_LOCALIZATION_AND_WEIGHT_MAPS.md`, CSL0–CSL10, read in full for TPL13; `63e373b0…`, in `20260924-…/gct-weight-control/proofs/`.
- **OZR.** `ORIGINAL_ZETA_DIVISOR_DEFECT_REVIEW.md`, OZR0–OZR10, read in full; `56c80e09…`, in `20260925-full-source-tensor-and-original-divisor/identity/`. The copy in `20260925-source-endpoint-and-section/` (`64539c82…`) has the same text, OZR10 included. It differs only in line endings, in plain rather than hyperlinked file names in OZR0, and in the absence of the closing links section. The reviewed file OZD (`ORIGINAL_ZETA_DIVISOR_DEFECT_RECEIVER.md`, identity version, `01f71965…`) was read for its definitions; `12_` had read OZD itself.
- **FT.** `INTEGRAL_FROBENIUS_TRANSFER_ALGEBRA.md`, FT1–FT10, read in full; `4735130b…`, in `20260924-…/gct-weight-control/proofs/`. Up to line endings it is identical to lines 26221–26724 of `RECONSTRUCTION_AND_WEIGHT_FULL.md`.
- **PCJ.** `POSITIVE_COMPLETION_AND_ZERO_JETS.md`, PCJ0–PCJ10, read in full; `44b4d44a…`, in the same folder.

**Checks.**
- `checks/audit49/audit49_checks.py` has 33 items, all pass, and runs in a few seconds. Exact arithmetic (sympy, fractions) is used for the algebraic identities; mpmath at 40 digits is used for the analytic identities at sample points.
- The referee's programs are in `checks/audit49/referee/`: 16 items, all pass. They include stronger versions of several of my items (§7).

## 0. Summary

| Block | Verdict | Added here |
|---|---|---|
| TPL0–TPL12 | correct | TPL9's family is every diagram of free rank-one J_m-modules, up to isomorphism (§1.4) |
| TPL13 | correct as a comparison | Its one open point, J = C, is settled. CSL10, added to the CSL file after TPL13 was written, states it, from SSI (audited in `25_`, Lemma 25.1) and from CSL6's claim that ℳ₀ : A → ℬ is a topological isomorphism (which cites S1, unaudited). That isomorphism is proved here (§1.3) |
| OZR0–OZR10 | correct | p > 1 in OZR8 is sharp among power weights. The exact threshold is logarithmic: (1 + \|y\|)^{−1}(log(2 + \|y\|))^{−2−ε}. p > 2 is sharp for absolute convergence of the completed comparison, which holds for every p > 1 as a cut-off limit (§2.2) |
| FT1–FT10 | correct | FT's integral ring is the quotient, by V_pF_p = p, of the ring 𝒲 of Frobenius–Verschiebung relations shared by the integral Bost–Connes system and the big Witt vectors (§3.3). V_pF_p = p fails on ℤ[ℚ/ℤ]. On W(A) it holds exactly when pA = 0, so no nonzero W(A) satisfies it at every prime: it is the characteristic-p relation imposed at all primes at once. FT10's circle is the same in every cohomological degree (§3.4). |
| PCJ0–PCJ10 | correct | The half-twist b_r ↦ √r·u_r identifies the positive completion with the group C*-algebra C*(ℚ^×_{>0}) ≅ C(∏_p S¹). So the geometric norm of a Dirichlet polynomial is its supremum on the critical line, and PCJ10's trace is one block of the Weil form (§4.2). |
| PCJ4, PCJ5, PCJ10, OZR8.5 | negative result | Each "positive exactly on the line" statement is RH, or RH with simple zeros, by construction (§5) |
| `41_` §3 | correction | BQC0–BQC6 are cited on `origin/main` but defined in no Markdown file there (§6) |

## 1. TPL: localization on the three-point space

### 1.1 The space and the audit

The space is X = {+, η, −}, with open sets ∅, {η}, U_+ = {+, η}, U_− = {−, η} and X (Connes–Consani, *The absolute twistor line and the geometry of the compactified Spec ℤ*, arXiv:2609.00299, as TPL0 cites it; CSL1.1 is the same space).
- It is a topology: U_+ ∪ U_− = X and U_+ ∩ U_− = {η}.
- η is the generic point, since every nonempty open set contains it.
- The closure of {+} is the complement of U_−, which is {+}. So + and − are closed.

Each step was re-derived.
1. **TPL0, the conventions.**
   - Cone(f)^n = D^n ⊕ C^{n+1}, with differential (y, x) ↦ (d_Dy + fx, −d_Cx).
   - For r : A[0] → B[0] this puts A in degree −1 and B in degree 0, with differential +r. Shifting by −1 negates the differential, so Cone(r)[−1] = [A →^{−r} B] in degrees 0 and 1, as stated.
2. **TPL1, sheaves as diagrams.**
   - Each point has a smallest open neighbourhood: U_+, U_− and {η}.
   - So a sheaf is the diagram A_+ → B ← A_−, where A_± = F(U_±) and B = F({η}).
   - Γ = A_+ ×_B A_− is the sheaf condition for the cover X = U_+ ∪ U_−.
3. **TPL2, the resolution.**
   - I_+(V), I_−(V) and I_η(V) are right adjoint to the three stalk functors, which are exact. So they carry injective vector spaces to injective sheaves.
   - The sequence (TPL2.2) is exact at each stalk. At +, it is 0 → A_+ → A_+ ⊕ B → B → 0, with a ↦ (a, r_+a) and (a, b) ↦ b − r_+a.
   - The map to the Čech complex is (v_+, v_−) ↦ v_− − v_+ in degree 1. It is a chain map and surjective, and its kernel [B →^{b↦(b,b)} diag B] is acyclic.
   - Hence H⁰ = A_+ ×_B A_−, H¹ = B/(r_+A_+ + r_−A_−), and H^q = 0 for q ≥ 2.
4. **TPL3–TPL4, the open–closed functors.**
   - The formulas for j_* and j_! (with j : {η} → X) and for i^* and i_* (with i : {+, −} → X) are read off from the smallest neighbourhoods, and i^!F = (ker r_+, ker r_−).
   - Applying i^! to the resolution gives K_± = [A_± →^{−r_±} B]. The sequence 0 → i_*Ri^!F → I^• → j_*B[0] → 0 is exact termwise.
5. **TPL5, the long exact sequence.**
   - Lifting b to (0, 0, b) and taking minus the differential, as fixed in TPL0, gives δ(b) = ([−b], [−b]).
   - The sequence (TPL5.3) is exact, with ker δ = r_+A_+ ∩ r_−A_− = im(res).
   - Exactness at q is TPL5's direct argument: if v_− − v_+ = r_+a_+ + r_−a_−, then b = v_+ + r_+a_+ = v_− − r_−a_− represents both classes.
   - The dimensions were checked on 40 random diagrams over ℚ (check A4).
6. **TPL6, the second triangle.**
   - 0 → j_!j^*F → F → i_*i^*F → 0 is exact at each stalk.
   - For the single-point sequence at +, the lift of a_− ∈ F(U_−) is (0, a_−, r_−a_−). Its differential is (r_−a_−, 0), so the boundary is a_− ↦ [−r_−a_−] ∈ B/r_+A_+.
7. **TPL7, operators and the exchange.**
   - A triple (S_+, S_−, S_η) with r_±S_± = S_ηr_± acts on everything.
   - For an exchange (s_+, s_−, s_η) with r_−s_+ = s_ηr_+ and r_+s_− = s_ηr_−: d(s_−a_−, s_+a_+) = −s_η d(a_+, a_−). So the Čech degree-one action is −s_η, and the costalk action is (b_+, b_−) ↦ (s_ηb_−, s_ηb_+).
8. **TPL8, full jets.**
   - Tensoring over a field with J_m = ℂ[t]/(t^m) is exact, so H^q(F⁰ ⊗ J_m) = H^q(F⁰) ⊗ J_m.
   - T_a = a^λ exp((log a)N) is a group homomorphism in a, and its inverse is a^{−λ}exp(−(log a)N).
9. **TPL9, restrictions given by powers of N.**
   - dim H⁰ = m + k, dim H¹ = k and dim im(res) = m − h, with k = min(a, b) and h = max(a, b). This was checked for every m ≤ 8 and 0 ≤ a, b ≤ m (check A1).
   - (y, u) ↦ (t^{b−a}y + u, y) is an isomorphism J_m ⊕ t^{m−a}J_m → H⁰ for a ≤ b (check A2, m ≤ 7).
10. **TPL10, the unipotent case.**
    - M − 1 = N·H(N) with H(N) = Σ N^j/(j+1)!, which is invertible (check A6).
    - In the total complex A → B ⊕ A → B, the composite of the two differentials is dN_A − N_Bd = 0.
    - The sequence 0 → coker(N|H⁰) → H¹_tot → ker(N|H¹) → 0 and H²_tot = coker(N|H¹) were re-derived. Their dimensions were checked on 12 random diagrams of free J_m-modules (check A5).
11. **TPL11–TPL12, the Fréchet case.**
    - H¹_alg is Hausdorff exactly when r_+A_+ + r_−A_− is closed. If both images and their sum are closed, (TPL5.3) is strict, by the open mapping theorem.
    - In the example N(x, y) = (Sy, 0) with Sx = (x_n/n): N² = 0, and the image S(ℓ²) ⊕ 0 is dense and proper, since (1/n) = S(1, 1, …) and (1, 1, …) ∉ ℓ².
    - With r_+ = S and r_− = 1 on ℓ²: H¹_alg = 0, δ(b) = ([−b], 0), and the class of (1/n) is nonzero, while the reduced boundary vanishes. So replacing images by their closures loses the lifting question.
12. **TPL13, comparison with CSL.**
    - The substitution A_± = S ⊕ ℂ², B = A, r_+(f, c) = Σf, r_−(h, d) = RΣh is CSL1.5.
    - CSL's positive costalk differentials and its difference map b_+ − b_− are related to TPL's by the chain isomorphism (1, −1), which carries CSL's boundary b ↦ ([b], [b]) to TPL5's.
    - The mirror (s_+, s_−, s_η) = (swap, swap, R) satisfies TPL7.3 because R² = 1. Its Čech action −R is CSL5.1.
    - Both restriction images equal J = Σ(S), because RΣh = Σĥ on S (CSL1.7). That identity is Poisson summation, Σĥ(u) = u^{−1}Σh(u^{−1}) + u^{−1}h(0) − ∫h, with both moment terms zero on S.

**Verdict.** TPL0–TPL13 are correct. The derivation is elementary homological algebra on a finite space, and every sign convention is stated and used consistently.

### 1.2 Lemma 49.1 (localization on the three-point space)

Let F be a sheaf of complex vector spaces on X, given by r_± : A_± → B. Then:
- H⁰(X, F) = A_+ ×_B A_−, H¹(X, F) = B/(r_+A_+ + r_−A_−), and H^q = 0 for q ≥ 2;
- the costalks are Ri^!F = ([A_+ →^{−r_+} B], [A_− →^{−r_−} B]);
- the sequence 0 → ker r_+ ⊕ ker r_− → H⁰ → B →^δ B/r_+A_+ ⊕ B/r_−A_− →^q H¹ → 0 is exact, with δ(b) = ([−b], [−b]), q([v_+], [v_−]) = [v_− − v_+], and ker δ = r_+A_+ ∩ r_−A_−.

In words: the obstruction to extending a generic section is the pair of its classes modulo the two restriction images, and Čech H¹ receives that pair through the difference map. *Proof:* TPL2–TPL5, audited in §1.1.

### 1.3 The open point of TPL13 is closed

TPL13 ends by saying that the algebraic receiver A/J and the Hausdorff receiver A/C (C = closure of J) "remain the distinct objects" until J = C is proved. TPL13 cites CSL0–CSL9. A later section of the same file, CSL10, states J = C. It rests on two things:
- the exact summation image SSI, which `25_` audited as Lemma 25.1: ℳ₀Σ : S → ℐ is a topological isomorphism onto the ideal ℐ ⊂ ℬ of functions vanishing to full order at every nontrivial zero. That lemma already records that the image is closed.
- CSL6.3's statement that ℳ₀ is a topological isomorphism A → ℬ, which cites S1, not audited.

That isomorphism is proved here in full, so the conclusion no longer depends on S1.

**Lemma 49.2.** The Mellin map ℳ₀a(s) = ∫₀^∞ a(u)u^{s−1}du is a topological isomorphism from the space A of CSL1.3 onto the space ℬ of FT5.2. Consequently J = Σ(S) = ℳ₀^{−1}(ℐ) is closed in A, so N = C/J = 0, H¹_alg = H¹_red, and A/J ≅ ℬ/ℐ = 𝒬 topologically.

*Proof.*
1. **Continuity.** Fix a ∈ A, A₀ > 0 and M ∈ ℕ, and write s = σ + iτ with |σ| ≤ A₀. Integrating by parts M times gives s^Mℳ₀a(s) = ∫₀^∞ ((−u∂_u)^M a)(u)u^{s−1}du. The boundary terms vanish, because (u∂_u)^j a is O(u^N) at 0 and O(u^{−N}) at ∞ for every N. Take an integer N > A₀, and put K = ∫₀^∞ u^{σ−1}(u^N + u^{−N})^{−1}du. Then K ≤ 1/(N + σ) + 1/(N − σ) ≤ 2/(N − A₀), uniformly in |σ| ≤ A₀, and

   |∫₀^∞ g(u)u^{s−1}du| ≤ K·sup_u (u^N + u^{−N})|g(u)|.

   Summing over j ≤ M bounds b_{A₀,M}(ℳ₀a) by finitely many seminorms of a.
2. **Injectivity and the inverse.** For F ∈ ℬ put a(u) = (1/2π)∫F(c + it)u^{−c−it}dt. This does not depend on c, because F decays rapidly on vertical strips, so the contour can be moved.
   - Then u^c(u∂_u)^j a(u) = (1/2π)∫(−(c + it))^j F(c + it)u^{−it}dt, so |u^c(u∂_u)^j a(u)| ≤ C_j·b_{|c|, j+2}(F).
   - Taking c = N and c = −N shows a ∈ A, with each seminorm of a bounded by finitely many seminorms of F.
   - ℳ₀a = F by Fourier inversion in the variable log u, and a = 0 if ℳ₀a = 0.
   - So ℳ₀ is bijective with a continuous inverse. This part was found by the referee pass (its M1).
3. **ℐ is closed.** By Cauchy's estimate on a circle of radius 1 around ρ, |F^{(j)}(ρ)| ≤ j!·b_{|Re ρ|+1, 0}(F). So each evaluation F ↦ F^{(j)}(ρ) is continuous on ℬ, and ℐ, their common kernel, is closed.
4. **J = ℳ₀^{−1}(ℐ).** The inclusion ⊆ holds because ℳ₀Σf ∈ ℐ. Conversely, if ℳ₀a ∈ ℐ, Lemma 25.1 gives f ∈ S with ℳ₀Σf = ℳ₀a, and injectivity gives a = Σf.
5. So J is the preimage of a closed set under a continuous map. ∎

So on the programme's actual sheaf the Hausdorff issue of TPL11–TPL12 does not arise: both restriction images are the closed subspace J. The boundary δ(b) = ([−b], [−b]) lands in (A/J)², and A/J ≅ ℬ/ℐ = 𝒬, the quotient that carries every zero with its multiplicity. The referee pass checked step 1's integration by parts exactly for a = e^{−u−1/u}, where ℳ₀a = 2K_s(2) (its R-F1).

### 1.4 Missed generality: TPL9 is the whole rank-one family

**Proposition 49.3.** Consider diagrams J_m → J_m ← J_m of free rank-one J_m-modules with J_m-linear restriction maps. Every such diagram is isomorphic to exactly one diagram of TPL9, (N^a, N^b) with 0 ≤ a, b ≤ m.

*Proof.*
1. A J_m-linear map J_m → J_m is multiplication by some g ∈ J_m.
2. If g ≠ 0, then g = t^a·u, where a < m is the t-adic order of g and u has nonzero constant term, so u is a unit. If g = 0, put a = m.
3. Precomposing with the automorphism u^{−1} of the source changes r_+ = t^a u into t^a without changing the diagram's isomorphism class. The same applies to r_−.
4. Uniqueness: dim ker(t^a·) = a (check A3), and kernel dimensions are isomorphism invariants. ∎

So TPL9's "proved family for arbitrary multiplicity" is the complete list, and its formulas (dim H⁰ = m + min(a, b), dim H¹ = min(a, b), dim im(res) = m − max(a, b)) compute every such diagram.

## 2. OZR: the review of the divisor receiver, and its power-decay extension

### 2.1 Audit

OZR reviews OZD, the identity (1/2π)∫ log|ζ| Δφ dA = Σ_ρ m_ρφ(ρ) + Σ_{k≥1}φ(−2k) − φ(1) and its receivers. Each step of OZR was re-derived.
1. **OZR1, the reflection.**
   - d_r(ρ^#) = −d_r(ρ), because ρ^# = 1 − ρ̄ has real part 1 − σ and the same imaginary part γ.
   - So (D_r^*JG_t)^*(D_r^*JG_t) = G_t^*D_r^*D_rG_t, with diagonal (r^σ − r^{1−σ})²e^{2t(σ²−γ²)}.
2. **OZR2, the divisor.**
   - Green's identity on a punctured disc gives Δlog|s − a| = 2πδ_a.
   - Hence Δlog|ζ| = 2π(Σ m_ρδ_ρ + Σ_{k≥1}δ_{−2k} − δ₁), with no term at 0, since ζ(0) = −½.
3. **OZR3, the logarithmic estimate.**
   - ζ(s) = s∫₁^∞⌊u⌋u^{−s−1}du and the Euler–Maclaurin expansion (OZR3.1). Checked at s = ½ + 3i with K₀ = 2 and 3, to 10⁻¹⁵ (check B9).
   - |ζ(2 + ij)| ≥ 1/ζ(2), because |1/ζ(2 + ij)| ≤ Σ n^{−2} (check B10, j ≤ 200).
   - The area sub-mean inequality for log|(s − 1)ζ(s)| on discs D(2 + ij, R_K) then gives ∫_{K×[j,j+1]} |log|ζ|| = O_K(log(|j| + 2)).
4. **OZR4, the test Laplacian.**
   - Δ(h(x)e^{2t(x²−y²)}) = e^{2t(x²−y²)}[h'' + 8txh' + 16t²(x² + y²)h]; the two ±4t terms cancel (check B1).
   - q_r' = 2 log r·(r^{2x} − r^{2−2x}) and q_r'' = 4(log r)²(r^{2x} + r^{2−2x}), with q_r(1) = (r − 1)² and q_r(½) = 0 (checks B2–B4).
5. **OZR5, the completed factor.**
   - The divisor of F₀ = s(s − 1)π^{−s/2}Γ(s/2)ζ(s)/8: at 0 the zero of s cancels the pole of Γ(s/2); at 1 the zero of s − 1 cancels the pole of ζ; at −2k the trivial zeros cancel the poles of Γ.
   - |F₀(2 + iy)|² = (4 + y²)(1 + y²)/(64π²) · (πy/2)/sinh(πy/2) · |ζ(2 + iy)|², using |Γ(1 + ib)|² = πb/sinh(πb). This was checked at five values of y (check B7).
6. **OZR6, the functional equation.**
   - ζ(s) = χ(s)ζ(1 − s) with χ(s) = π^{s−½}Γ((1 − s)/2)/Γ(s/2) (check B8).
   - The divisor of χ: zeros at 0, −2, −4, … and poles at 1, 3, 5, ….
   - The bookkeeping (OZR6.1) of the odd part was checked on random odd test profiles (check B11).
7. **OZR7, the multiplicity trace.** Multiplication by b(ρ + h) on ℂ[h]/(h^m) is triangular with diagonal b(ρ), so its trace is m·b(ρ).
8. **OZR8, the power-decay extension.** See §2.2.
9. **OZR10, the wording repair.** 𝖱(x, y) = (1 − x, y) has Jacobian diag(−1, 1), so it preserves area, and Δ(f∘𝖱) = (Δf)∘𝖱.

**Verdict.** OZR0–OZR10 are correct.

### 2.2 Lemma 49.4 (the power-decay divisor identity; OZR8) and its sharp exponents

**Statement (OZR8).** Let p > 1, K ⊂ ℝ compact, and φ ∈ C^∞(ℂ) supported in K × ℝ, with |∂_x^a∂_y^bφ| ≤ C(1 + |y|)^{−p} for a + b ≤ 2. Then

(1/2π)∫ log|ζ| Δφ dA = Σ_ρ m_ρφ(ρ) + Σ_{k≥1}φ(−2k) − φ(1),

and every integral and sum converges absolutely.

*Proof, as audited.*
1. The zeros with height in [T, T + 1] number O(log T), so Σ m_ρ(1 + |γ|)^{−p} < ∞ for p > 1.
2. §2.1 step 3 gives ∫|log|ζ|| |Δφ| ≤ C Σ_j (1 + |j|)^{−p}log(|j| + 2) < ∞.
3. Cut off with θ(y/R). The two derivative errors are O(R^{−p}log R) and O(R^{−p−1}log R), and dominated convergence handles the rest.

For the explicit weight w_p = (1 + y²)^{−p/2}:
- w_p'' = p((p + 1)y² − 1)(1 + y²)^{−p/2−2} (check B5);
- |w_p^{(k)}| ≤ C_k w_p for k ≤ 2, which gives (OZR8.1) (check B6, sampled).

**Sharpness (added here).**
1. **p = 1 fails for the general identity.** φ(x, y) = η(x)(1 + y²)^{−1/2}, with η as in OZD (η ∈ C_c^∞(ℝ), η = 1 near [0, 1]), satisfies the derivative bounds with p = 1. Yet Σ_ρ m_ρφ(ρ) = Σ_ρ m_ρ(1 + γ²)^{−1/2} diverges.
   - The Riemann–von Mangoldt formula gives N(T) = (T/2π)log(T/2πe) + O(log T) (Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Theorem 9.4).
   - By partial summation, Σ_{0<γ≤T} m_ρ/γ = N(T)/T + ∫^T N(t)t^{−2}dt, which is ≥ (1/2π)∫_{2πe²}^T (log(t/2πe)/t)dt − O(1). This grows like (log T)²/(4π).
   - So the class of tests in OZR8 cannot be extended to p = 1 with absolute convergence.
   - Among all weights, not only powers, the exact threshold is logarithmic (found by the referee pass, its M3). Suppose every derivative of order at most 2 is bounded by w(y) = C(1 + |y|)^{−1}(log(2 + |y|))^{−2−ε} with ε > 0.
     - The integral side converges: Σ_j log(|j| + 2)·w(j) < ∞.
     - The divisor side converges: ∫w dN < ∞, since dN ≍ (log t/2π)dt.
     - The cut-off errors are O(w(R)·log R) → 0.
     - At ε = 0 both fail, since ∫dt/(t log t) = ∞.
2. **p > 2 is exact for absolute convergence of the completed comparison.** By Stirling's formula, log|Γ(s/2)| = −(π/4)|y| + O(log|y|) on each vertical strip.
   - So on a unit-height rectangle K × [j, j + 1] the absolute integral of log|Γ(s/2)| is of order |j|. The same holds for log|F₀| = log|ζ| + log|Γ(s/2)| + log|s(s − 1)/8| − (x/2)log π, since the other terms contribute O(log|j|). This is OZR5's linear bound, and it is attained.
   - Hence ∫|log|F₀|| |Δφ| is finite for every test in the class (OZR8.1) exactly when p > 2.
   - For p = 2 it fails: take φ = η(x)(1 + y²)^{−1}. Then Δφ = η''(x)(1 + y²)^{−1} + η(x)·2(3y² − 1)(1 + y²)^{−3}. The second term is O((1 + |y|)^{−4}) and contributes a finite amount.
   - The first term is not identically zero, since η'' ≢ 0. On the x-set where η''(x) ≠ 0, |log|F₀|| ≥ (π/4)|y| − O(log|y|).
   - So ∫|log|F₀|| |Δφ| ≥ c∫|y|(1 + y²)^{−1}dy − O(1) = ∞.
   - This is OZR8's restriction to p > 2 for absolute convergence in OZD4's completed comparison. As a statement about absolute convergence it cannot be weakened.
3. **The completed identity itself holds for every p > 1, as a cut-off limit** (the referee's M2).
   - Claim: lim_{R→∞}(1/2π)∫log|F₀| θ(y/R)Δφ dA = Σ_ρ m_ρφ(ρ).
   - Proof: apply the compact-support identity to θ(y/R)φ. The absolute integral of log|F₀| over a unit rectangle is O(1 + |j|) (OZR5), so the two derivative errors are O(R^{−1}·R^{−p}·R²) = O(R^{1−p}) and O(R^{−2}·R^{−p}·R²) = O(R^{−p}). The zero sum converges by dominated convergence.
   - The referee pass checked this numerically for p = 2 (its R-B3): the cut-off integral tends to the predicted value, while the absolute integral grows.

**What OZR8.5 is.**
- E_r^{(p)} = Σ m_ρ q_r(σ)(1 + γ²)^{−p/2} vanishes exactly when q_r(σ) = 0 for every zero, that is, when every nontrivial zero has σ = ½.
- So "E_r^{(p)} = 0 ⟺ β_r = 0" is a new receiver of the same RH-equivalent quantity as OZD's Gaussian energy. It is not progress towards evaluating that quantity, and OZR says so (OZR9).

## 3. FT: the integral transfer algebra and its geometric receiver

### 3.1 Audit

Each step was re-derived.
1. **FT1, the ring.**
   - 𝒞 = ℤ[b_n, n·b_{1/n}] ⊂ ℚ[ℚ^×_{>0}] has ℤ-basis c_r = den(r)·b_r.
   - The product rule is c_rc_s = gcd(ac, bd)·c_{rs} for r = a/b and s = c/d reduced, because den(rs) = bd/gcd(ac, bd) (check C1, 2,000 pairs).
   - c_{a/b} = F_aV_b.
2. **FT2, the presentation.**
   - 𝒞 ≅ ℤ[X_p, Y_p]/(X_pY_p − p).
   - Normal monomials map to c_r (check C2), and the c_r are independent.
3. **FT3, the involution.**
   - b_r^⋆ = r·b_{1/r} satisfies c_r^⋆ = c_{1/r}, so it preserves 𝒞 and exchanges F_n and V_n.
   - F_mV_n = d·F_{m/d}V_{n/d} with d = gcd(m, n) (check C3).
4. **FT4, the denominator obstruction.**
   - b_{1/p} ∉ 𝒞, since its coefficient 1 is not divisible by den(1/p) = p.
   - 0 → 𝒞 → Λ → ⊕_r ℤ/den(r) → 0 is exact.
   - F_n is not integral over ℤ, because the powers b_{n^j} are independent.
5. **FT5, the zeta receiver.**
   - Ψ(F_n) = T_n and Ψ(V_n) = nT_{1/n} on 𝒬 = ℬ/ℐ. On each Jordan block this is (FT5.6)–(FT5.8), and their product is n.
   - The Weil-form identity (FT5.9) was re-derived from W(F, G) = Σ_ρ m_ρF(ρ)·conj(G(ρ^#)), the form of RTT audited in `27_`: m_ρ n^ρF(ρ)·conj(G(ρ^#)) = m_ρF(ρ)·conj(n·n^{−ρ^#}G(ρ^#)), because conj(n^{−ρ^#}) = n^{−1+ρ}.
6. **FT6, the tori.**
   - E_q = ℂ/(q log p·ℤ + 2πiℤ). The covering u_{n,q} : E_{nq} → E_q and the dual isogeny both have degree n.
   - The pullback matrices are 1, diag(n, 1), n and the transfer matrices n, diag(1, n), 1 in degrees 0, 1, 2. So S·P = P·S = n in each degree (check C4).
   - v^* agrees with the transfer only in degree one (check C5).
7. **FT7, the scale family.**
   - The relations F_mF_n = F_{mn}, V_mV_n = V_{mn}, F_mV_n = V_nF_m and F_nV_n = n hold, with mixed matrices n, diag(m, n), m (check C8).
   - The representation is faithful: c_{a/b} sends e₁ to b·e_{a/b}.
8. **FT8, the positive forms.**
   - The Gram matrices are qAB, diag(B/(qA), qA/B) and 1/(qAB) (check C7).
   - h_{nq}(Px, y) = h_q(x, Sy) and h_{nq}(Px, Px') = n·h_q(x, x') in every degree (check C6). So 𝔉_n^† = 𝔙_n and ‖𝔉_n‖ = √n.
9. **FT10, the spectrum.**
   - On the degree-zero completion with ‖e_q‖² = qAB, the normalised vectors f_q = e_q/‖e_q‖ satisfy 𝔉_nf_q = √n·f_{nq}. So 𝔉_n is √n times a bilateral shift on each orbit q·n^ℤ.
   - Its spectrum is the circle |λ| = √n and it has no eigenvalues, as for any bilateral shift.
   - FT10's explicit proof was checked, including ‖z_N‖² = (2N + 1)AB and ‖(𝔉_n − λ)z_N‖² = 2nAB (check C9).

**Verdict.** FT1–FT10 are correct.
- FT5's statements rest on RZ (audited in `27_`) and on IC8, which is not audited here. FT's own claims were checked from their definitions.
- FT9 is explicit that the two representations of 𝒞 are not intertwined, and that no positivity passes from the torus side to 𝒬.

### 3.2 Lemma 49.5 (the integral transfer algebra; FT1–FT3, FT7–FT8)

Statement:
1. The subring 𝒞 of ℚ[ℚ^×_{>0}] generated by F_n = b_n and V_n = n·b_{1/n} has ℤ-basis {den(r)·b_r : r ∈ ℚ^×_{>0}}.
2. 𝒞 ≅ ℤ[X_p, Y_p : p prime]/(X_pY_p − p).
3. 𝒞 is stable under b_r ↦ r·b_{1/r}, which exchanges F_n and V_n.
4. On the Hilbert direct sum of the cohomology of the tori E_q, it acts faithfully by pullbacks and transfers along the coverings E_{nq} → E_q, with 𝔉_n^† = 𝔙_n and 𝔉_n𝔙_n = 𝔙_n𝔉_n = n.

*Proof:* FT1–FT3 and FT6–FT8, audited above.

### 3.3 Proposition 49.6 (FT's ring against the integral Bost–Connes system and the big Witt vectors)

This is a typed comparison for goal 4 (the 𝔽₁ context).

**The relation ring.** Let 𝒲 be the associative ring generated over ℤ by symbols F_n, V_n (n ≥ 1), with relations

F₁ = V₁ = 1, F_mF_n = F_{mn}, V_mV_n = V_{mn}, F_cV_b = (b, c)·V_{b/(b,c)}F_{c/(b,c)}.

Products are compositions, so F_cV_b means "V_b first, then F_c".

**Statement.**
1. **Both classical systems represent 𝒲.**
   - On ℤ[ℚ/ℤ], F_n ↦ σ_n and V_n ↦ ρ̃_n, where σ_n(e(γ)) = e(nγ) and ρ̃_n(e(γ)) = Σ_{nγ'=γ}e(γ'). This is the integral Bost–Connes system of Connes, Consani and Marcolli.
   - On the big Witt vectors W(A), F_n and V_n are the Frobenius and Verschiebung.
2. **FT's ring is a quotient.** 𝒞 ≅ 𝒲/(V_pF_p − p : p prime). The quotient is commutative, while 𝒲 is not.
3. **Where the extra relation holds.**
   - On ℤ[ℚ/ℤ], ρ̃_pσ_p is multiplication by π_p = Σ_{pt=0}e(t), and π_p ≠ p. So V_pF_p = p fails.
   - On W(A), V_pF_p is multiplication by V_p(1), and V_p(1) = p exactly when pA = 0. So the relation holds on W(A) precisely in characteristic p, where it is the classical VF = p (Hesselholt, *loc. cit.*, the lemma on 𝔽_p-algebras). No nonzero W(A) satisfies it at every prime simultaneously, since pA = qA = 0 for two primes forces A = 0.
   - So 𝒞 is 𝒲 with the characteristic-p relation imposed at all primes at once.

*Proof.*
1. **ℤ[ℚ/ℤ].**
   - The relation σ_cρ̃_b = (b, c)ρ̃_{b'}σ_{c'} is Connes–Consani–Marcolli, *Fun with 𝔽₁*, J. Number Theory 129 (2009), Proposition 4.4, equations (46)–(48) (read through a tool summary of arXiv:0806.2401). It was also checked here in 300 random cases (check E1).
   - σ_mσ_n = σ_{mn} is immediate. ρ̃_mρ̃_n = ρ̃_{mn} holds because the m-th roots of the n-th roots of γ are the mn-th roots.
2. **W(A).** Hesselholt, *Lecture notes on Witt vectors* (2005), Lemma 5 in the text fetched from the author's page, lists:
   - (ii) F_nV_n(a) = na;
   - (iii) a·V_n(a') = V_n(F_n(a)a');
   - (iv) F_mV_n = V_nF_m when (m, n) = 1.

   Multiplicativity in n is standard. For d = (b, c), write c = c'd and b = b'd. Then

   F_cV_b = F_{c'}F_dV_dV_{b'} = d·F_{c'}V_{b'} = d·V_{b'}F_{c'},

   by (ii), the additivity of F_{c'}, and (iv).
3. **The quotient.**
   - 𝒞 satisfies the relations of 𝒲 (FT3.4–FT3.6) together with V_pF_p = p. So there is a surjection 𝒲/(V_pF_p − p) → 𝒞.
   - In the quotient every pair of prime generators commutes: F_pF_q = F_{pq} = F_qF_p, likewise for V; F_pV_q = V_qF_p for p ≠ q by the coprime case; and F_pV_p = p = V_pF_p.
   - So the quotient is a commutative ring generated by F_p and V_p with F_pV_p = p, that is, a quotient of ℤ[X_p, Y_p]/(X_pY_p − p) ≅ 𝒞 (FT2). The two maps are mutually inverse on generators.
   - 𝒲 is not commutative, since its representation on ℤ[ℚ/ℤ] has σ_pρ̃_p = p ≠ ρ̃_pσ_p.
4. **V_pF_p ≠ p in the classical systems.**
   - ρ̃_pσ_p(e(γ)) = Σ_{pt=0}e(γ + t) = π_p·e(γ) (check E2). π_p ≠ p because π_p·e(0) = Σ_{pt=0}e(t) ≠ p·e(0).
   - By (iii) with a' = 1, V_pF_p(a) = V_p(1)·a.
   - In the power-series model W(A) = 1 + tA[[t]], the unit is (1 − t)^{−1}, so p·1 is (1 − t)^{−p}. Also V_p(1) = (1 − t^p)^{−1}, since V_p substitutes t^p for t.
   - These are equal exactly when (1 − t)^p = 1 − t^p in A[[t]]. That holds exactly when pA = 0: the coefficient of t is −p, and p divides the binomial coefficients C(p, k) for 0 < k < p.
   - For A = ℤ: the ghost components of V_p(1) are p at indices divisible by p and 0 elsewhere, while those of p are all p. The referee pass checked the characteristic criterion in W(ℤ/N) for N ≤ 30 and p ≤ 7 (its R-E1). ∎

**Degree and deck sum.** In each system, one composite of F_n and V_n is a degree (a fibre count), and the other is a sum over the kernel of the degree-n map, the deck translations. Which one is which depends on the dictionary.
- **On FT's tori,** 𝔉 is pull-back and 𝔙 is transfer.
  - 𝔙_n𝔉_n = u_!u^* = n, the degree formula, which holds for every covering of degree n.
  - 𝔉_n𝔙_n = u^*u_! = Σ_{g∈ker} τ_g^*, the deck sum of the Galois covering. Each translation of a connected torus is homotopic to the identity, so τ_g^* = 1 on cohomology and the sum is n.
  - So in FT's own dictionary the extra relation V_nF_n = n is the degree formula. The collapse of the deck sum is what gives the relation F_nV_n = n of 𝒲, which the tori need to represent 𝒲 at all.
- **On ℤ[ℚ/ℤ],** σ_n is push-forward along multiplication by n and ρ̃_n is pull-back.
  - σ_nρ̃_n = n is the fibre count; that is 𝒲's relation.
  - ρ̃_nσ_n = Σ_{nt=0}(translation by t) = π_n is the deck sum; that would be the extra relation, and the translations act nontrivially.
- **The dictionaries match** under F ↦ 𝔙, V ↦ 𝔉. This is also a representation of 𝒲, because FT3's involution ⋆ is an automorphism of the commutative ring 𝒞. In that dictionary the extra relation is the deck sum in both systems: it collapses on the connected tori and not on ℤ[ℚ/ℤ].
- The referee pass found that the first version of this paragraph attributed the extra relation to the deck collapse in FT's own dictionary, which is the wrong way round.

**The structure of 𝒲** (found by the referee pass, its M7; the proof is its own, re-read here).
- 𝒲 is a free ℤ-module with basis {V_bF_c : b, c ≥ 1}.
- The product rule is (V_{b1}F_{c1})(V_{b2}F_{c2}) = d·V_{b1b2/d}F_{c1c2/d}, with d = (c1, b2).
- Both classical representations are faithful.
- The quotient map to 𝒞 sends V_bF_c to (b, c)·c_{c/b}.
- Spanning is by normal ordering: each use of F_cV_b = (b, c)V_{b'}F_{c'} lowers the number of F-before-V pairs.
- Independence on ℤ[ℚ/ℤ] follows by grouping the terms by the reduced ratio c/b, writing ρ̃_{b₀t}σ_{c₀t} = ρ̃_{b₀}(π_t·σ_{c₀}(−)), and evaluating at e(1/ℓ) for a large prime ℓ. Independence on W(ℚ) follows from ghost coordinates.
- The referee's checks R-G1 to R-G3 cover b, c ≤ 6 and the associativity of the product rule.

*Interpretation, not a theorem.* V_pF_p = p replaces the p-element deck orbit (π_p on ℤ[ℚ/ℤ], V_p(1) in W(A)) by its cardinality p. On W(A) this identification is exactly characteristic p. In this sense FT's ring is the Frobenius–Verschiebung pattern of a "characteristic p at every prime" object, realised geometrically by connected coverings, where the deck orbits act trivially. The same relations appear in two places in the 𝔽₁ literature:
- Connes–Consani–Marcolli's treatment of the extensions 𝔽_{1^n} through ℤ[ℚ/ℤ];
- the big Witt vectors that underlie Borger's λ-ring approach to 𝔽₁.

### 3.4 What FT10 says about weights

On the degree-zero geometric receiver the spectrum of 𝔉_n is the circle |λ| = n^{1/2}.
- **The same circle in every degree** (the referee's M4). In degrees 1 and 2 as well, FT8.3 shows that 𝔉_n maps each orthonormalised basis vector at scale q to √n times the corresponding one at scale nq (its R-C3). After the half-twist, the whole of H* carries four copies of the regular representation of ℚ^×_{>0}: one in degree 0, two in degree 1, one in degree 2. So the spectrum is |λ| = √n with no eigenvalues in every degree.
- **So this is not a Weil weight.** The circle does not depend on the degree, unlike Frobenius on H^i of a curve over a finite field. It is fixed by the similitude factor of FT8's forms, h(𝔉x, 𝔉x') = n·h(x, x').
- In the translation |α| = p^{w/2} of the register (S31) it reads as "weight one" in every degree.
- On 𝒬 the operator T_n has, on the block of ρ, the eigenvalue n^ρ, of modulus n^{Re ρ}. The two moduli agree exactly on the critical line.
- FT constructs no map between the two receivers. PCJ (§4) computes what continuity in the geometric norm would force.

## 4. PCJ: the positive completion and the zero jets

### 4.1 Audit

Each step was re-derived.
1. **PCJ1.** 𝕋 = ∏_p S¹ with Haar measure is the dual group of ℚ^×_{>0} ≅ ⊕_pℤ. The characters z^{v(r)} form an orthonormal basis, so Ue_r = √(ABr)·z^{v(r)} is unitary.
2. **PCJ2.**
   - US_rU^{−1} is multiplication by √r·z^{v(r)}. In particular 𝔉_p ↦ √p·z_p and 𝔙_p ↦ p·(1/√p)·z_p^{−1} = √p·z_p^{−1}.
   - C_{a/b} ↦ b√(a/b)·z^{v(a/b)} = √(ab)·z^{v(a/b)}, and C_r^* = C_{1/r} goes to complex conjugation (check D1).
   - The norm of a multiplication operator by a continuous function, for a measure of full support, is the supremum of the function.
3. **PCJ3.** The closure is C(𝕋), and its characters are the point evaluations.
4. **PCJ4.** χ_ρ(b_r) = r^ρ extends exactly when p^{ρ−½} lies on the unit circle, that is, Re ρ = ½. The witnesses p^{−k/2}F_p^k and p^{−k/2}V_p^k have norm one.
5. **PCJ5.** The jet representation is π(b_r) = r^ρ exp((log r)N).
   - N is recovered from π(F_p) by the truncated logarithm (check D2, m ≤ 6).
   - On the line, ‖π(A_k)1‖ ≥ (k log p)^{m−1}/(m − 1)! (check D3, for p = 2).
6. **PCJ6.** The ideals of J_m are the (t^j), because an element of order j is t^j times a unit.
7. **PCJ7.** The closed ideal generated by the jet kernel is determined by its zero set.
   - Off the line, the function √p·z_p − p^ρ has no zero on 𝕋, since its two terms have different moduli.
   - On the line the zero set is {z_ρ}, and closed ideals of C(𝕋) are the ideals of functions vanishing on a closed set.
8. **PCJ10.**
   - The trace of π(a) on J_m is m·h_a(ρ).
   - The residue of h_aζ'/ζ at a zero of multiplicity m is m·h_a(ρ). This was checked at the first zero to 10⁻⁴⁰ (check D5).
   - Off the line, T(a^*a) = m(p^{1−σ} − √p)(p^σ − √p) < 0 (check D4, 500 random cases).
   - The trace pairing on a critical-line jet has radical (t).

**Verdict.** PCJ0–PCJ10 are correct.

### 4.2 Proposition 49.7 (the positive completion is the group C*-algebra of ℚ^×_{>0})

Let 𝒜 = ℂ[ℚ^×_{>0}] with the involution b_r^* = r·b_{1/r} (complex coefficients conjugated), and let ℂ[ℚ^×_{>0}]_std be the group algebra with u_r^* = u_{1/r}.
1. Φ(b_r) = √r·u_r defines a *-isomorphism 𝒜 → ℂ[ℚ^×_{>0}]_std.
2. Under Φ and the unitary U of PCJ1, Ψ_geom becomes the regular representation, written in Fourier coordinates. So the operator-norm completion of Ψ_geom(𝒜) is C*(ℚ^×_{>0}) ≅ C(∏_p S¹).
3. A character χ of the group ℚ^×_{>0}, given by the numbers w_p = χ(b_p) ∈ ℂ^×, extends continuously to the completion exactly when |w_p| = √p for every prime p. This is PCJ3's classification of the characters, restated in terms of w_p.
4. A finite-dimensional representation π of 𝒜 extends boundedly exactly when π∘Φ^{−1} is a uniformly bounded representation of the group. In particular the jet representation of PCJ5 extends exactly when Re ρ = ½ and m = 1.
5. On the line, the points z_ρ = (p^{iγ})_p of distinct γ are distinct, and the set {(p^{iγ})_p : γ ∈ ℝ} is dense in ∏_p S¹.
6. (The referee's M5.) For D = Σ c_rb_r, ‖Ψ_geom(D)‖ = sup_{γ∈ℝ}|Σ_r c_r r^{1/2+iγ}|: the geometric norm of a Dirichlet polynomial with rational frequencies is its supremum on the critical line.
7. (The referee's M6.) T_{ρ,m}(a^*a) = m·h_a(ρ)·conj(h_a(ρ^#)), which is the ρ-summand of the Weil form W(h_a, h_a) of RTT (audited in `27_`).

*Proof.*
1. Φ(b_rb_s) = √(rs)·u_{rs} = Φ(b_r)Φ(b_s). Also Φ(b_r^*) = Φ(r·b_{1/r}) = r·(1/√r)·u_{1/r} = √r·u_{1/r} = Φ(b_r)^*.
2. PCJ2.1 is exactly Φ followed by the Fourier transform of the regular representation of ℚ^×_{>0} on ℓ²(ℚ^×_{>0}). The group C*-algebra of a discrete abelian group is C(Ĝ) by Gelfand duality, and here Ĝ = ∏_p S¹.
3. χ∘Φ^{−1}(u_p) = w_p/√p. So χ extends exactly when this is a unitary character, i.e. |w_p| = √p for all p. The zeta characters are the case w_p = p^ρ, which gives PCJ4.
4. A bounded representation of C*(G) restricts to a uniformly bounded representation of the group. Conversely, a uniformly bounded representation of a discrete abelian group on a finite-dimensional space is similar to a unitary one, and so extends. The jet representation gives u_p ↦ p^{ρ−½}exp((log p)N), which is uniformly bounded in the powers of p exactly when |p^{ρ−½}| = 1 and N = 0.
5. If p^{iγ} = p^{iγ'} for p = 2 and 3, then (γ − γ')log 2 and (γ − γ')log 3 both lie in 2πℤ. If γ ≠ γ', this makes log 3/log 2 rational, which it is not.

   Density: the numbers log p are linearly independent over ℚ, by unique factorisation. So Kronecker's theorem makes {(p^{iγ})_{p≤P} : γ ∈ ℝ} dense in ∏_{p≤P}S¹ for every P. The torus (p^{−it})_p is the one Bohr used for the values of ζ on vertical lines (Titchmarsh, op. cit., Chapter XI).
6. The Fourier image of D is f_D(z) = Σ c_r√r·z^{v(r)} (PCJ2.1). At z_γ = (p^{iγ})_p, z_γ^{v(r)} = r^{iγ}, so f_D(z_γ) = Σ c_r r^{1/2+iγ}. Since f_D is continuous and the z_γ are dense (item 5), sup_𝕋|f_D| = sup_γ|f_D(z_γ)|, and PCJ2.5 gives the norm.
7. Write a = Σ c_rb_r and a^* = Σ c̄_r r·b_{1/r}. Then χ_ρ(a^*) = Σ c̄_r r^{1−ρ} = conj(Σ c_r r^{1−ρ̄}) = conj(h_a(ρ^#)). So T_{ρ,m}(a^*a) = m·χ_ρ(a^*)χ_ρ(a) = m·h_a(ρ)·conj(h_a(ρ^#)), with W(F, G) = Σ_ρ m_ρF(ρ)·conj(G(ρ^#)). The referee pass checked this for m ≤ 4 (its R-D1). ∎

**What this adds.** PCJ3–PCJ7 and PCJ10 follow from two facts:
- after the half-twist, F_p is √p times a unitary, which is what the positive transfer adjoint 𝔉_p^†𝔉_p = p means once the geometric norm is fixed;
- the representation is the regular one (PCJ1's U is its Fourier transform).

The second fact is needed. The one-dimensional representation b_r ↦ √r also makes F_p equal to √p times a unitary, but its completion is ℂ, and χ_{1/2+iγ} does not extend to it for γ ≠ 0. (The first version of this paragraph named only the first fact; the referee pass supplied the example.)

Item 6 makes the "RH by construction" results of §5 explicit: the positive norm is the sup norm on the critical line. So χ_ρ is continuous exactly when |Σ c_r r^ρ| ≤ C·sup_γ|Σ c_r r^{1/2+iγ}| for every Dirichlet polynomial, and that holds exactly on the line.

Item 7 identifies PCJ10.7's negative square with the off-line hyperbolic block of the Weil form (`25_`, check 10).

## 5. Register entries

**Standalone results** (register, goal 3):
- Lemma 49.1: localization on the three-point space. Proved in the programme (TPL); audited.
- Lemma 49.2: ℳ₀ : A → ℬ is a topological isomorphism, so the summation image J is closed in A and J = C.
  - CSL6.3 and CSL10.3 state this; CSL6 cites the unaudited S1.
  - The proof here is self-contained. The surjectivity half was found by the referee pass.
- Proposition 49.3: TPL9 is the complete rank-one family. Proved here.
- Lemma 49.4: the power-decay divisor identity (OZR8), audited. Proved here:
  - p > 1 is sharp among power weights;
  - the exact threshold is (1 + |y|)^{−1}(log(2 + |y|))^{−2−ε};
  - p > 2 is sharp for absolute convergence of the completed comparison, which holds for every p > 1 as a cut-off limit.
- Lemma 49.5: the integral transfer algebra 𝒞 and its positive geometric receiver (FT). Audited. Its spectrum is the circle |λ| = √n in every cohomological degree (§3.4).
- Proposition 49.7: the half-twist.
  - 𝒞 ⊗ ℂ completes to C*(ℚ^×_{>0}) ≅ C(∏_p S¹).
  - The geometric norm of a Dirichlet polynomial is its supremum on the critical line.
  - PCJ10's trace is the ρ-block of the Weil form.
  - This is the structure behind PCJ3–PCJ7 and PCJ10.

**Negative results** (register, goal 1): the following conditions are RH, or RH with simple zeros, by construction.
1. "Every zero character χ_ρ is continuous in the positive geometric norm" (PCJ4) is RH.
2. "Every full jet representation extends boundedly" (PCJ5) is RH together with the simplicity of all zeros.
3. "The multiplicity trace is positive at every zero" (PCJ10.5–10.7) is RH.
4. "E_r^{(p)} = 0" (OZR8.5) is RH, for any single r > 1 and p > 1.

In items 1–3 the positive norm is the sup norm on the critical line (Proposition 49.7(6)). So continuity at ρ means that values at ρ are dominated by values on the line, which is the statement that ρ lies on the line. The programme's texts say that none of these conditions has been proved (PCJ9, OZR9).

**Bridges** (register, goal 4, the 𝔽₁ context): Proposition 49.6 and the structure of 𝒲.
- FT's integral ring 𝒞 = 𝒲/(V_pF_p − p : p prime).
- 𝒲 is the Frobenius–Verschiebung relation ring shared by the integral Bost–Connes system (Connes–Consani–Marcolli) and the big Witt vectors. It is a free ℤ-module on {V_bF_c}, and both classical representations are faithful.
- On W(A) the extra relation holds exactly when pA = 0: it is the characteristic-p relation VF = p, imposed in 𝒞 at every prime at once. It fails on ℤ[ℚ/ℤ], where V_pF_p is multiplication by π_p.
- On FT's tori, the extra relation is the degree formula. The collapse of the deck sum on connected tori gives 𝒲's own relation F_pV_p = p.

## 6. What was not checked, and a correction to `41_`

**Not checked.**
- The sources that FT and PCJ cite: IC1–IC9 (`INTEGRAL_COUNTING_AND_WEIGHT_COMPARISON.md`), IAR0–IAR9, AT5, JTR0–JTR8, and TATE_H1 T5–T8. The statements of FT and PCJ were checked from their own definitions.
- S1 (the Mellin estimates of `GLOBAL_MELLIN_SYNTHESIS.md`). Lemma 49.2 replaces the part of it used here.
- RZ was audited in `27_`, and SSI in `25_`.
- The Codex review and receipt files that accompany these blocks, and the checks named in OZR0.
- The Connes–Consani–Marcolli relation (Proposition 4.4, (46)–(48)) and Hesselholt's lemmas were read through tool summaries of the papers, not in full. The Bost–Connes relation and the Witt-vector criterion are also checked computationally (check E1; the referee's R-E1, R-E2).
- The journal metadata of Connes–Consani–Marcolli, and the year of Hesselholt's notes, were not confirmed from the documents themselves.
- The two other blocks in the same compilation as FT, CB1–CB10 (the boundary quotient) and GI1–GI4 (the geometric-to-zeta intertwiners, including a nonclosability statement), are not audited here. They are the natural next audit.

**Correction to `41_` §3.** The first list there includes "the programme sections BQC0–BQC6, FT10 and PCJ10 (on `origin/main`)".
- FT10 and PCJ10 are on `origin/main`, and are audited here.
- BQC0–BQC6 are only cited there, and cited more often than first stated here:
  - `RECONSTRUCTION_AND_WEIGHT_FULL.md` line 7116, and line 11 of each of the three copies of `CC_GYSIN_TO_GLOBAL_SHIFTED_ZETA.md`;
  - `RECONSTRUCTION_AND_WEIGHT_FULL.tex` line 11403, and line 23 of two copies of `CC_GYSIN_TO_GLOBAL_SHIFTED_ZETA_BODY.tex`.
- No Markdown or TeX file at `baa6f7a` defines them. The other byte matches (PDF, ZIP, image and `.json.gz.partNN` files) are chance sequences. The extracted text of every matching PDF, and every text or PDF member of the matching ZIPs, contains no "BQC" (the referee's `scan_bqc.py`).

## 7. Checks

`checks/audit49/audit49_checks.py`, output in `audit49_checks_OUTPUT.txt`: 33 items, all pass, in a few seconds. The items, by part:
- **A (TPL):**
  - A1: the dimensions of TPL9 for m ≤ 8;
  - A2: the isomorphism (TPL9.5);
  - A3: kernel dimension equals t-adic order;
  - A4: dimension bookkeeping only (an identity in the ranks; exactness is the referee's R-A1);
  - A5: H⁰_tot and H¹_tot of TPL10.4–10.5 on 12 random J_m-diagrams;
  - A6: M − 1 = N·H(N).
- **B (OZR):**
  - B1–B4: the test Laplacian, the derivatives of q_r, and q_r(1), q_r(½);
  - B5–B6: w_p'' and the derivative bounds;
  - B7: |F₀(2 + iy)|²;
  - B8: the functional equation;
  - B9: Euler–Maclaurin;
  - B10: |ζ(2 + ij)|·ζ(2) ≥ 1;
  - B11: the odd-part bookkeeping.
- **C (FT):**
  - C1: the product rule;
  - C2: normal monomials;
  - C3: FT3.6, multiplied out in the group algebra;
  - C4–C5: the typed matrices of FT6 (derived from the lattice maps in the referee's R-C1);
  - C6–C7: FT8;
  - C8: FT7.5;
  - C9: FT10, with the operator applied to z_N in exact arithmetic.
- **D (PCJ):**
  - D1: the Fourier coefficients (an algebraic identity);
  - D2: the logarithm formula;
  - D3: jet growth (an illustration);
  - D4: the negative square;
  - D5: the residue trace for m = 1 and m = 2.
- **E (Bost–Connes):**
  - E1: Connes–Consani–Marcolli's relation on 300 random cases;
  - E2: σ_nρ̃_n = n and ρ̃_nσ_n = π_n·, with π_n ≠ n.

**The referee's checks**, in `checks/audit49/referee/referee49_checks.py`: 16 items, all pass.
- R-A1: exactness with the maps built.
- R-B1 to R-B3: N(T), Stirling, and the cut-off limit at p = 2.
- R-C1 to R-C3: FT6 from the lattices, FT10 applied, and the circle in every degree.
- R-D1, R-D2: the Weil block, and multiplicity 2.
- R-E1, R-E2: Witt vectors in characteristic N.
- R-F1: Lemma 49.2, step 1.
- R-G1 to R-G3: the structure of 𝒲.

## 8. Revision after the referee pass

An independent Claude instance refereed this note from 06:50 to 07:21 UTC. It reported 2 major findings, 8 minor ones, and 7 missed or implied results. Its report is `checks/audit49/referee/REFEREE_REPORT_49.md`. I verified each finding before applying it.

**Major.**
1. **The Witt-vector claim was false in characteristic p.** V_p(1) = p exactly when pA = 0. I verified this in the power-series model (§3.3, proof step 4). Items affected: §0, Proposition 49.6(3) and §5.
2. **The deck-group explanation was reversed.** I re-derived both composites in both dictionaries (§3.3, "Degree and deck sum"). Items affected: §3.3 and §5.

**Minor.**
- Checks: the weak items are rewritten or relabelled (§7).
- The completed comparison holds as a cut-off limit, and the logarithmic threshold is added (§2.2).
- Lemma 49.2: attribution corrected to CSL6.3, CSL10.3 and Lemma 25.1; surjectivity added; the integer N and the uniform bound on K fixed (§1.3).
- Proposition 49.7: the credit to PCJ3 and the second fact are added (§4.2).
- The OZR copy is described correctly (Sources).
- The BQC matches are listed in full (§6).
- The header times are corrected.
- The weight caveat is added (§3.4).

**Missed results added.**
- M1: the Mellin isomorphism (§1.3).
- M2, M3: the cut-off limit and the logarithmic threshold (§2.2).
- M4: the circle in every degree (§3.4).
- M5, M6: the norm as the supremum on the critical line, and the Weil block (§4.2).
- M7: the structure of 𝒲 (§3.3).
