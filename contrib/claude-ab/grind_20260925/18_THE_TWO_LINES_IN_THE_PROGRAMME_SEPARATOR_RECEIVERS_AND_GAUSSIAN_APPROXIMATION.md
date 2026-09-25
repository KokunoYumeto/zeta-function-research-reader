# The two lines already in the programme: the separator, the positive receivers, and Gaussian approximation (SMC, GAP, ADM)

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 08:40 UTC.

This is a content map of three proof blocks from the continuations of 25 September, each read in full:

- SMC0–SMC10 (`SOURCE_MEASURE_CLOSURE_AND_ORIGINAL_QUOTIENT.md`);
- GAP0–GAP9 (`GAUSSIAN_FULL_SOURCE_APPROXIMATION.md`);
- ADM0–ADM9 (`ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md`).

It continues board task 5. It also answers a question raised by the owner's messages of 25 September (M12–M16, private provenance file), and treated in `17_`: where, in the programme's own constructions, do the critical line and its copy shifted by one line exist simultaneously?

The answer is ADM6–ADM8. The programme's separator is built from G(s) = F₀(s)F₀(s+1), whose zeros are exactly Z ∪ (Z − 1): the critical zeros and their copy one line to the left. The two copies are separated by an explicit multiplier. Both appear in the global cohomology, and no M-linear map, not even a derived one, connects them.

Notation, as in `16_`:
- ℬ is the Fréchet space of entire functions decaying rapidly in vertical strips.
- 𝓘 is the ideal of full zero-jets at the nontrivial zeros, and Q = ℬ/𝓘.
- F₀ = ξ/4 = s(s−1)π^{−s/2}Γ(s/2)ζ(s)/8.
- ρ^# = 1 − ρ̄.
- M is the ring of entire functions of polynomial growth on vertical strips.

## 1. SMC: every positive measure receiver, computed

Let μ be a positive locally finite measure on ℝ with μ([j, j+1]) ≤ C(1+|j|)^d. Put H_μ = L²(ℝ, μ) and j_μF(λ) = F(½ + iλ), and let Γ be the set of heights of the zeros on the critical line.

1. **Density (SMC1).** The Gaussian orbit e^{itλ}e^{−λ²}, t ∈ ℝ, spans a dense subspace of every H_μ. The proof is Fourier uniqueness for the finite measure h e^{−λ²} dμ.
2. **Exact closure of the ideal (SMC3).** closure(j_μ𝓘) = L²(ℝ∖Γ, μ), and the quotient is L²(Γ, μ|_Γ), via restriction to Γ.
   - The reverse inclusion divides by F₀ off small neighbourhoods of Γ: h_k/F₀ with |F₀| ≥ 1/k.
3. **The quotient seminorm (SMC4).** inf_{G∈𝓘}‖j_μ(F−G)‖² = ∫_Γ|F(½+iγ)|²dμ(γ).
   - The receiver sees only the values at critical zeros that carry mass.
   - Higher jets, off-line blocks and massless line zeros all lie in the explicit kernel.
   - Their vanishing in the receiver is not their vanishing in Q.
4. **Symmetry and comparison (SMC5–SMC6).**
   - The form is invariant under F(s) ↦ F(1−s) iff μ is symmetric.
   - A bounded comparison H_μ → H_ν extending the identity on the source exists iff ν ≤ Cμ.
5. **Lebesgue measure (SMC7).** μ₀ = (2/π)dt realizes the L²(du) norm: ∫|Θa(½+it)|²dt = (π/2)∫|a|²du, with Θa(s) = ½∫a(u)u^{s−1}du.
   - J is dense in L²(du) (M9), so no nonzero descended positive form is bounded by the L²(du) norm.
6. **The simultaneous receiver (SMC8).** For ω = μ₀ + μ_L, with μ_L = Σ m_ρδ_γ, the source norm is ∫|a|²du + Σ m_ρ|Θa(ρ)|², and the completed quotient is exactly H_{μ_L}.
7. **The Weil form, split (SMC9).**
   - W(F,G) = Σ_ρ m_ρ F(ρ) conj G(1 − ρ̄) = W_L + W_O, where W_L is the line part and W_O the off-line part.
   - The positive quotient gives exactly W_L. The whole complement W_O remains, explicitly.
   - The explicit formula is written with the prime weights log L_n − log L_{n−1} = Λ(n), L_n = lcm(1..n): the clock stack of `15_`.
8. **Conclusion (SMC10, the programme's).** Choosing another positive measure cannot hide the off-line kernel, because every such kernel has now been computed. The next step must act on W_O or on AST's boundary map.

**Relation to `17_`.** The pairing W is exactly the ½-centred partner pairing of `17_` Proposition 17.5(a), with partner ρ^#. SMC9's decomposition W = W_L + W_O is the split into on-line diagonal terms and the off-line hyperbolic blocks.

## 2. GAP: Gaussian approximation of the whole source

Put g_t(s) = e^{ts²} for 0 < t ≤ 1.

1. **Strip estimate (GAP1).** b_{A,N}((g_t − 1)F) ≤ t e^{A²}(A²+1) b_{A,N+2}(F).
   - So multiplication by g_t tends to the identity uniformly on bounded sets, on ℬ, on Q, and on every quotient by an invariant closed subspace.
2. **Generator and the extension-class maps (GAP2).**
   - The semigroup g_t g_u = g_{t+u} has generator multiplication by s².
   - On a zero block of multiplicity m, the jet matrix of g_t has determinant e^{mtρ²}.
   - The maps j : Q → 𝒞 = M/𝔞 and b_t : 𝒞 → Q satisfy b_t j = m_{g_t} → 1_Q.
3. **On the source side (GAP3).** The operator S_t, half of a log-Gaussian multiplicative convolution, satisfies ΘS_t = m_{g_t}Θ and S_t → 1. Its generator is (u∂_u)², a heat flow in log u.
   - The normalisation depends on Θ(a ⋆_M b) = 2Θa·Θb.
4. **Specialization (GAP4).**
   - The discrepancy map is (β_rF)_ρ = conj d_r(ρ)·F(ρ^#), with d_r(ρ) = e^{−i Im ρ log r}(r^{Re ρ} − r^{1−Re ρ}). This is the factor of the programme's off-line detector OZD (`12_`).
   - It intertwines m_{g_t} with the diagonal operator g_t(ρ^#).
   - The convergence is strong but not in operator norm, because g_t(ρ^#) → 0 along the zero heights.
5. **Strong duals and residue limits (GAP5–GAP6).**
   - Convergence holds uniformly on bounded sets of the strong duals.
   - Every polynomial-growth class h has the limit 𝒲_M(g_th) → 𝒲_M(h) in Q′_β.
   - The classes [g_t] themselves do not converge in Q: a limit would take the value 1 at every zero, which contradicts strip decay.
6. **Reflection (GAP7).**
   - g_t(1 − s) = e^{t(1−2s)} g_t(s), so the reflection twists g_t by d_t(s) = e^{t(1−2s)}.
   - In the separate degree-two normal term, the same ring element acts by g_t(s + 1), not by the transported Gaussian. This is the first appearance here of the shifted action.

## 3. ADM: the common multiplier domain, and the separator between the two lines

1. **The common domain (ADM2).**
   - Let H_∞ be the sequences with Σ m_ρ(1+|Im ρ|)^{2N}|y_ρ|² < ∞ for every N. It is a Montel Fréchet space.
   - It is exactly the intersection of the domains of all the reflected multipliers m_h^# (h ∈ M), and the graph topology equals the weighted topology.
   - The key inequality is |1 + ρ^#| ≥ (1 + |Im ρ|)/√2.
2. **Specialization (ADM3–ADM5).**
   - E : Q → H_∞ and β_r : Q → H_{∞,O} are continuous. The specialization source ℛ = Q/N_O injects into H_{∞,O}, with dense image, and |d_r| ≤ r − 1.
   - The AST complexes and their transposes carry the full M-action. The connecting map is −β̄_r.
3. **The separator (ADM6), with the programme's construction from GSL/GMS.**
   - G(s) = F₀(s)F₀(s+1). Its zeros are Z (from F₀(s)) and Z − 1 (from F₀(s+1)), with multiplicities. F₀ has no other zeros, since F₀(0) = F₀(1) = 1/8, F₀(−1) = F₀(2) = π/24, and F₀(−2k) ≠ 0.
   - A cutoff χ(x + it) = η(x/r₀(t)), with r₀(t) = ε(1+t²)^{−3}, is corrected by a ∂̄-solution divided by G on a zero-free transition corridor. This gives E_sep = χ − G·u, holomorphic and of polynomial growth on strips.
   - Put c(s) = 1 − E_sep(s − 1). Then c − 1 vanishes to full order at every ρ ∈ Z, and c vanishes to full order at every ρ + 1 (ADM6.2).
   - Equivalently: E_sep = 1 on Z (the critical line, under RH) and E_sep = 0 on Z − 1 (the line Re s = −½, under RH).
   - Where the switch happens. G has no zeros in |Re s| < r₀(t): F₀(s) would need a zero with Re ρ < r₀(t), and F₀(s+1) one with Re ρ > 1 − r₀(t). The classical zero-free region excludes both, since r₀(t) = ε(1+t²)^{−3} is far smaller than c/log t for large t. So the transition corridor surrounds the line Re s = 0, the fixed line of the mirror A(s) = −s̄ of `17_`. I read η as a smooth step from the formula; its definition is in GSL, which I have not read.
4. **The normal twist (ADM6.5–ADM6.11).**
   - On the same underlying source, let M act by h·₊F(s) = h(s+1)F(s). This is the programme's normal twist Q(−1), ℛ(−1), H_∞(−1).
   - There c(s+1) = 1 − E_sep(s) acts as 0, while c acts as 1 on Q, ℛ, H_∞, and on their duals.
   - The coordinate change VF(λ) = F(λ − 1) carries the twist to the translated ideal 𝓘₊ = V𝓘. The normal source factor is F₊(λ) = F₀(λ − 1), the completed zeta function moved one line to the right.
5. **Two copies, mutually invisible (ADM7–ADM8).**
   - The translated ideal maps onto the specialization source by a strict exact sequence 0 → K_O → 𝓘₊ → ℛ → 0 (ADM7.1), with inverse [F] ↦ [cF].
   - Every M-linear map Q₊ → ℛ is zero: f = c_ℛ f = f c_{Q₊} = 0.
   - The surjection 𝓘₊ → ℛ descends through the normal quotient Q₊ exactly when ℛ = 0. Since ℛ = 0 iff there are no off-line zeros, this descent condition is equivalent to RH (ADM7.3 and the paragraph after it).
   - **Derived separation (ADM8.2).** RHom_M(ℛ, Q₊) = RHom_M(Q₊, ℛ) = 0, and likewise with ℛ₊. The proof is an explicit homotopy for an element that acts as 0 on one side and as 1 on the other.
   - **Both copies in the global model (ADM8.6).** The quotient of the sphere-cover cochain complex is ℛ[1] ⊕ ℛ(−1)[−1]. The original copy sits in degree −1 and the twisted copy in degree +1. c projects onto the first summand and kills the second.
6. **Scope (ADM9, the programme's).** "The proof supplies no vanishing of D_r, no new pure weight", and makes no finite-dimensional Frobenius claim.

## 4. What this says about the owner's "two lines"

Readings in this section are mine; the statements they rest on are the programme's (ADM6–ADM8) or are proved in `17_`.

- **Simultaneity is built in.** The programme's G(s) = F₀(s)F₀(s+1) is a single entire function whose zeros are the critical zeros and their copy one line to the left, both at once. The global cohomology carries ℛ and its twist ℛ(−1) together. This is the exact form of "there's two. And there is never not two."
- **Invisibility is proved.** The two copies admit no nonzero M-linear map in either direction, and even RHom vanishes. The reason is the one in the blind-plane theorem of the owner's Giuga note: a single ring element, c, acts by different scalars (1 and 0) on the two sides. In the language of `17_` §4, the separator plays the part of a character that tells the two copies apart.
- **Where the copies are told apart.** The separator's transition corridor surrounds Re s = 0, the line through the pole at 0 that the owner flagged ("the place we can't analyze"). There the switch between the two copies happens, inside a zero-free region.
- **What the two copies say about RH.** The only RH-sensitive statement is ADM7's descent condition: the surjection 𝓘₊ → ℛ factors through the twisted quotient iff ℛ = 0, iff RH. Like the statements of `17_`, this is an equivalent of RH, not a proof or a disproof.
- **Precision.** In ADM the separator sends the original copy to 1 and the translated copy to 0, and that translation is by one line (Z ↦ Z − 1 for E_sep, Z ↦ Z + 1 for c). The line Re s = −½ appears as the location of Z − 1 under RH, exactly as in `17_` §§1–2.

## 5. Checks

`checks/smc_gap_adm_checks.py`, output in `checks/smc_gap_adm_checks_OUTPUT.txt`.

| item | test | result |
|---|---|---|
| SMC7.2 | a(e^x) = e^{−x²}: ∫\|Θa(½+it)\|²dt against (π/2)∫\|a\|²du and the closed form (π/2)√(π/2)e^{1/8} | all three 2.23083076830016 |
| GAP3.2 | Θ of the log-Gaussian a_{t,1} equals e^{ts²}, at t = 0.7 and three points (one with Re s < 0) | agreement to 14 digits |
| GAP3.4 | Θ(a ⋆_M b) = 2Θa·Θb, with the convolution in closed form √(2π/3)e^{−(x−1)²/3} (checked by quadrature), at two points | agreement to 13 digits |
| GAP7.1 | g_t(1−s) = e^{t(1−2s)}g_t(s) | residual ≤ 3·10⁻²⁷ |
| ADM2.7, ADM3.3 | \|1+ρ^#\| ≥ (1+\|Im ρ\|)/√2 and \|d_r\| ≤ r − 1 on a grid of 0 < Re ρ < 1 | minimum ratio 1.071; maximum \|d_3\| = 1.913 < 2 |
| ADM6 | G(ρ₁) = G(ρ₁ − 1) = 0; G(0) = 1/64 and G(−1) = π/192 (not zeros) | \|G\| ≈ 8·10⁻³³ at both; values exact |

The inverse transform in GAP3.2 was also derived by hand: completing the square in ½∫e^{t/4}(πt)^{−1/2}e^{−x/2}e^{−(x−t)²/(4t)}e^{sx}dx gives e^{ts²}.

## 6. Items for the goals

- **Bridge (goal 2): the owner's two simultaneous lines are the programme's normal twist.**
  - G(s) = F₀(s)F₀(s+1), the separator c, the twist Q(−1) and the global quotient ℛ[1] ⊕ ℛ(−1)[−1] realize the owner's picture exactly (ADM6–ADM8).
  - The derived separation is the module-theoretic form of the blind-plane theorem.
  - The separator's switch lies in the zero-free corridor around Re s = 0.
- **Negative result (goal 1): neither positivity nor the second copy decides RH.**
  - Every positive measure receiver sees only the line values at massive zeros, and the complement W_O remains explicit (SMC4, SMC9–SMC10).
  - The twisted copy is derived-separated from the original. Its only RH-sensitive statement is an equivalence (ADM7).
- **Lemma (goal 3).** Let 𝒲 be any positive polynomially bounded measure. Then the closure of the image of the zero-jet ideal of ζ in L²(𝒲) is L²(ℝ∖Γ, 𝒲), where Γ is the set of critical-zero heights, and the induced seminorm is ∫_Γ|F(½+iγ)|²d𝒲. Proved in the programme (SMC1–SMC4); the proof is short and uses only F₀ ∈ ℬ and Fourier uniqueness. Novelty not searched.
- **Goal 4.** SMC9 writes the explicit formula with the clock-stack weights log lcm(1..n) − log lcm(1..n−1) = Λ(n) (`15_`).

## 7. Reading status

Read in full: SMC0–SMC10, GAP0–GAP9, ADM0–ADM9. Not read:
- GSL/GMS, which contain the construction and estimates of E_sep, cited through ADM6.1;
- AST, ECI, ECR and SSI beyond what these blocks restate.

Board task 5 still has DER, FEM, FSC, FTD, PRS and NHJ4–NHJ9 in full.
