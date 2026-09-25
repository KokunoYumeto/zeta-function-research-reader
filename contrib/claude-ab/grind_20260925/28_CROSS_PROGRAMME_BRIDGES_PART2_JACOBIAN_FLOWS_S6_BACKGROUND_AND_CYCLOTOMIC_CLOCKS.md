# Cross-programme bridges, part 2: the Jacobian polynomial as an incompressible flow, the S⁶ period block as a magnetic field, and the cyclotomic clocks

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 12:36 UTC. Board task 2 part 2, folded into board task 8 (the owner's priority: the actual programmes first). Part 1 is `21_`.

**Sources read.**
- In the YM workbench (commit fa79faf), folder `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/`:
  - `FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md`, in full;
  - `FABEL_CORRECTIONS_20260908.md`, in full;
  - `FABEL_TENSOR_TRANSFER.md`, the transport conventions and the statements of Theorem 13.1 and of the scope.
- In the YM workbench, `yang-mills/sources/ym_gap_primary_20260908/magnetic_translation_true_vacuum.md`: §1 and §9.
- In the YM workbench, `navier-stokes/RESEARCH_STATE.md`, in full. I also searched the 840 KB NS workbench TeX for "Fabel", "Jacobi", "S6" and "heat flow".
- On the owner's computer, in `work/`:
  - `cyclotomic_clock_transfer_20260924/`: DERIVATION.md, LOGBOOK.md and CHECK_RESULTS.json, in full;
  - `quantum_tau_programme_bridge_20260924/`: the directory listing and `RESULTS_BULLETIN_2026-09-25.md`, in full.

**Checks.** `checks/cross_programme_bridges_part2_checks.py` has 12 items, all passing: J1–J7 with J5b (sympy), S1 (sympy) and C1–C3 (exact arithmetic). The output is in `checks/cross_programme_bridges_part2_checks_OUTPUT.txt`.

## 0. Summary

1. **The Jacobian polynomial gives an incompressible polynomial flow that escapes in finite time (Lemma 28.1).**
   - F is the Jacobian-conjecture counterexample recorded in the YM workbench: det DF = −2, and F is three-to-one on the fibre over (−1/4, 0, 0).
   - The field U = DF^{−1}(V∘F), with V constant (or affine with div V = 0), is polynomial and divergence-free. F carries its integral curves onto straight lines.
   - One integral curve, γ(τ) = (z^{−1}, −3z/2, 13z²/2) with z = √(1−8τ), escapes to infinity as τ ↑ 1/8, while F(γ(τ)) = (−1/4 + 2τ, 0, 0) stays bounded.
   - For a polynomial automorphism this cannot happen: every such integral curve is defined for all τ.
   - This is the exact content of the "retained Navier–Stokes orbit" that the YM workbench uses. It is kinematics: U is not shown to solve the Navier–Stokes equations. The nearest source statement is FABEL_CORRECTIONS item 6: the external NS manuscript must not be "confused with the stationary Fabel polynomial".
2. **The chain Jacobian → NS kinematics → YM is typed and verified at every algebraic step I could check.**
   - The Lagrangian deformation A_τ has det A_τ = 1.
   - The material covector grows like (9/4)(1−8τ)^{−3/2}.
   - The "diffusion tensor" K_τ degenerates to a rank-one leading term, z^6K_τ → vv^T with v = (1/4, 3/8, −9/4).
   - The three endpoint spectral coefficients 113569/36864, 100825/12288 and 531/512 of the YM tensor transfer are exact.
   - The YM side uses K_τ as spatial weights of a lattice local-energy operator, and asserts no fluid-to-Hamiltonian intertwiner.
   - Its later Section 14 (`FABEL_LOW_MODE_TRANSFER.md`, Theorem 14.2; statement read, proof not checked) claims a sequence of physical vectors orthogonal to the vacuum whose energy quotients decay like 100√2π/j. The sequence runs along changing regulators: box L_j = j², spacing a_j = 1/(100j) and couplings g_j < 1/j. So the physical box length j/100 grows while the coupling tends to 0.
   - By the source's own account, the continuum identification remains unresolved. The same limitation, a zero-quotient sequence only as the coupling tends to 0, was found for the NS-profile edge in `21_` (scope limit 21.4).
3. **S⁶ → YM uses one number from the S⁶ data (Lemma 28.2).** The magnetic background is, after an exact frame change, the constant field of strength 2π/D on a plane, where D = Lq + 6m² is the determinant of the imaginary period block. The workbench states that the identification with S⁶ is not an input.
4. **The NS workbench's own heat and S⁶ transfers are not certified by that workbench.** Its research state says their implications "are not certified by this reader". The "heat correction" in the NS construction is internal to the NS proof, not a transfer. There is no morphism to state.
5. **The two local folders.**
   - `quantum_tau_programme_bridge_20260924` is the programme's own working folder for the three-lane edition, not a cross-programme bridge. Its 25 September bulletin has 15 entries (SZ-20260925-001 to -013, -017 and -018). Eight result groups are new relative to `12_`, `14_`, `16_`, `18_` and `24_`–`27_`; §5.1 lists them for board task 8.
   - `cyclotomic_clock_transfer_20260924` is an internal zeta-programme bridge. It runs from the owner's finite signed clock group ⟨T, J, ε | [T, J] = 1, J² = ε, ε² = 1⟩ to the Bost–Connes group ring ℤ[ℚ/ℤ]. I checked its identities (C1–C3), and they are correct. It sharpens item 1 of goal 2 in the register (prime clocks and Bost–Connes).

## 1. The Jacobian polynomial as an incompressible flow

**The map.** F: ℂ³ → ℂ³ has components
- F₁ = (1+xy)³w + y²(1+xy)(4+3xy);
- F₂ = y + 3x(1+xy)²w + 3xy²(4+3xy);
- F₃ = 2x − 3x²y − x³w.

Its Jacobian is det DF = −2 identically (check J1). The YM workbench's `ATTRIBUTION.md` identifies F with the counterexample to the Jacobian conjecture announced by Levent Alpöge on 20 July 2026 (`21_` §4).

### Lemma 28.1 (Keller maps and incompressible flows)

**Setting.** Let F: ℝⁿ → ℝⁿ be polynomial with det DF ≡ c ≠ 0 constant, and let V: ℝⁿ → ℝⁿ be an affine vector field. Put U = DF^{−1}(V∘F).

**Statement.**
- (a) U is a polynomial vector field, and div U = (div V)∘F. In particular U is divergence-free when V is.
- (b) F maps integral curves of U to integral curves of V. For γ′ = U(γ), d/dτ F(γ(τ)) = V(F(γ(τ))).
- (c) If F is a polynomial automorphism with polynomial inverse G, then every maximal integral curve of U is defined for all τ ∈ ℝ, namely γ(τ) = G(Φ^V_τ(F(γ(0)))).
- (d) For the F above, take V(y) = (2, 0, 0) or V(y) = (2, 6y₃, 0), so that V∘F = (2, 0, 0) or (2, 6F₃, 0). Both have γ(τ) = (z^{−1}, −3z/2, 13z²/2), z = √(1−8τ), as an integral curve of U, with F(γ(τ)) = (−1/4 + 2τ, 0, 0). The curve γ is the one in `FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md` §2. This curve leaves every compact set as τ ↑ 1/8, while its image stays on a bounded segment.

*Proof.*
1. **(a), polynomiality.** DF^{−1} = adj(DF)/c, and adj(DF) is polynomial.
2. **(a), the divergence.** The Piola identity Σ_j ∂_j adj(DF)_{ji} = 0 (check J2) and the chain rule give
   c·div U = Σ_{i,j}[∂_j adj(DF)_{ji}]·V_i(F) + Σ_{i,j,k} adj(DF)_{ji}·(∂_kV_i)(F)·∂_jF_k.
   The first sum vanishes. In the second, Σ_j ∂_jF_k·adj(DF)_{ji} = (DF·adj DF)_{ki} = cδ_{ki}, so the second sum is c·(div V)(F).
3. **(b).** d/dτ F(γ) = DF(γ)γ′ = V(F(γ)).
4. **(c).** By (b), F(γ(τ)) = Φ^V_τ(F(γ(0))), and the flow of an affine field is defined for all τ. Apply G.
5. **(d).** Substitution gives xy = −3/2 and 1 + xy = −1/2. Then F₁(γ) = −13z²/16 + 9z²/16 = −z²/4 = −1/4 + 2τ, F₂(γ) = −3z/2 + 39z/8 − 27z/8 = 0 and F₃(γ) = (4 + 9 − 13)/(2z) = 0. So γ′ = DF(γ)^{−1}(2, 0, 0) = U(γ); the shear term 6F₃ vanishes on γ (check J4). ∎

**What it shows.**
- The finite-time escape of γ is the failure of F to be proper, seen through a flow: a curve leaves every compact set while its image stays bounded.
- By (c), no polynomial automorphism can produce such a curve.
- The field is incompressible and polynomial: U₀ = DF^{−1}(2, 0, 0) has degree 8, and U has degree 13 (check J3).
- Finite-time escape alone is easy to produce without F. For example, U = (x², 0, −2xz) is divergence-free and x′ = x² escapes. What F adds is that the escaping incompressible flow is straightened, globally, by a polynomial map with constant Jacobian.
- Novelty not searched.

### The Lagrangian deformation along γ (the programme's §3, verified)

- **The deformation.** Let J₀ = DF(1, −3/2, 13/2), J_γ = DF(γ(τ)) and B_τ = I + 6τE₂₃ (the derivative of the target flow of V(y) = (2, 6y₃, 0)). The Lagrangian deformation is A_τ = J_γ^{−1}B_τJ₀. This follows from DΦ_τ = DF(Φ_τ)^{−1}·DΦ^V_τ·DF, a consequence of (b).
- **Checks (J5).** det A_τ = 1 and A_0 = I. The covector ζ_τ = A_τ^{−T}e₃ has |ζ_τ|²z^6 → 81/16, that is, |ζ_τ| ~ (9/4)(1−8τ)^{−3/2}.
- **The tensor.** K_τ = C_τC_τ^T, with C_τ = A_τ^{−1}, satisfies z^6K_τ → vv^T with v = (1/4, 3/8, −9/4) and |v|² = 337/64.
  - Its eigenvalues behave like (64/121)z^6, then → 121/337, and like (337/64)z^{−6}. The product is 1.
  - These follow exactly from z^6·tr K_τ → 337/64, z^6·e₂(K_τ) → 121/64 and det K_τ = 1, where e₂ is the sum of the principal 2×2 minors (check J5b). A direct numerical diagonalisation at z = 10⁻³, not in the check script, agrees to 5 digits; the ninth referee pass reproduced the ratios 1.000000003, 0.999991 and 1.000009.
- **The programme's reading, which I share.** This is the loss of uniform ellipticity at the endpoint, "not a finite-time singularity of u, ∇u, or curvature" (`FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md` §3).

## 2. From the material tensor to Yang–Mills trial states

**The typed chain.**

F ↦ U (Lemma 28.1) ↦ γ, A_τ, C_τ, K_τ (§1) ↦ weights of the lattice local-energy operator D_f = κΣ_e f_eE_e + Σ_p f_p b(2 − W_p) ↦ trial states Ξ_{m^TSm} in the gauge-invariant Hilbert space.

**What the programme proves (FABEL_CORRECTIONS, FABEL_TENSOR_TRANSFER).** The positive spectral measure of S ↦ Ξ_{m^TSm} splits into three cubic-symmetry sectors,
ν_S = (tr S)²/9·ν₀ + ½Σ_i(S_ii − tr S/3)²·ν_d + Σ_{i<j}S_ij²·ν_o.
For S = K_τ, z^{12}ν_{K_τ} converges to (113569/36864)ν₀ + (100825/12288)ν_d + (531/512)ν_o.
- I recomputed the three coefficients exactly from K_τ (check J6).
- The remaining statements are lattice spectral calculations that I did not re-derive. These are the first-surviving coefficient 𝒟_{S_*} and the quotient 234κ/49 + O_L(κξ²) at small coupling on a fixed box.

**Scope, in the workbench's own words.**
- "No equality between fluid evolution and quantum Hamiltonian evolution is asserted" (`FABEL_TENSOR_TRANSFER.md`, opening).
- "The three unknown interacting seed-sector limits at changing regulators remain unevaluated. No counterexample or all-theory exclusion follows" (FABEL_CORRECTIONS).
- For the raw mass-gap question: "A complex Fabel tangent vector has no map into this real gauge-invariant Hilbert space until one specifies" an observable, its gauge action, the state and domain, and the continuum limit (FABEL_JACOBI_TO_YM_COORDINATE_AUDIT §4).

**The later Section 14 (statement read; proof not checked here).** FABEL_CORRECTIONS ("Subsequent continuation in Section 14") and `FABEL_LOW_MODE_TRANSFER.md` Theorem 14.2 claim "a proved finite-regulator sequence". The vectors are
w_j = 1_{(Δ_j/2, 11Δ_j/10)}(H_{g_j,L_j,a_j} − ℰ)Ξ_{f_{S_j}}, with S_j = K_{τ_j}.
They are orthogonal to the vacuum, with ‖w_j‖² ~ 𝒞_*j^{18} and energy quotient ~ 100√2π/j.
- **What varies.** The regulators vary with j: L_j = j², a_j = 1/(100j), g_j < 1/j. So the physical box length L_ja_j = j/100 tends to infinity and the coupling tends to 0.
- **What the source leaves open.** "The common interacting continuum state/observable identification remains unresolved" (FABEL_CORRECTIONS). "The construction does not identify their changing Hilbert spaces with an interacting four-dimensional continuum theory" (FABEL_LOW_MODE_TRANSFER, opening).
- **The typed conclusion.** The morphism F → YM reaches projected physical states at each finite regulator, as claimed by the source. It does not reach a fixed-coupling or continuum statement. This parallels `21_` scope limit 21.4, where the NS profile gave a zero-quotient sequence only as the coupling tends to 0.

**The gauge encoding is the one in `21_` §2:** 𝒜_i = λu_iT and ℱ_ij = λ(∂_iu_j − ∂_ju_i)T, with −2Σ_{i<j}tr ℱ_ij² = λ²|curl u|².
- The source is correct that the growth of |ζ_τ| does not give growth of curl u: ζ_τ is a material covector, not the velocity.
- It is also correct that pointwise vorticity growth does not give growth of ∫|curl u|² unless the concentrating volume is controlled (FABEL_CORRECTIONS item 5).

## 3. S⁶ → Yang–Mills: one number from the period data

### Lemma 28.2 (the S⁶ period block enters only through its determinant)

**Setting.** Let B = [[6m, L], [−q, m]] be the imaginary period block of the regular fibre, as used in `magnetic_translation_true_vacuum.md` (1.4). Put D = det B = Lq + 6m² > 0. Set (u₁, u₂) = B^{−1}(y₁, y₂) and A_orig = 2πH_c·u₁du₂.

**Statement.**
- du₁∧du₂ = D^{−1}dy₁∧dy₂.
- A_orig = (2π/D)H_c·y₁dy₂ + H_c·df, with f = (2π/D²)(mqy₁²/2 − Lqy₁y₂ − 3mLy₂²).

After the frame change exp(−H_cf), the background is the constant magnetic field of strength 𝔟 = 2π/D in the (y₁, y₂) plane. Its plaquette angle is θ = 𝔟a² = 2πa²/D.

*Proof.* Expand both components. The dy₁ coefficient of A_orig equals ∂f/∂y₁. The dy₂ coefficients differ by (2π/D²)(6m² + Lq)y₁ = (2π/D)y₁ (check S1). ∎

**What it shows.** On the non-wrapping patch used in this file, the YM calculation built on the S⁶ data (the magnetic translation T_h, the Gauss projection and the vacuum variance) depends on the S⁶ periods only through the single positive number D. The source already displays this identity and θ = 2πa²/D after (1.4); it is re-verified here.
- The workbench says the same from its side: "the claimed identification of a completed complex threefold with S6 is not an input to this calculation" (the file's opening paragraph).
- The companion cusp calculation keeps the wrap factors and the full period-matrix map. So the statement "only D enters" is limited to this patch.

## 4. The NS workbench's own transfers

`navier-stokes/RESEARCH_STATE.md` says: "The programme initially investigated transfers from algebraic, S6-related and heat-flow constructions into fluid equations. Those directions motivated the research; their proposed implications are not certified by this reader."
- The workbench's main content is the reconstruction of a released finite-time NS manuscript. Its "base field and heat correction" component (`proof_sources/base_heat/derivation.tex`) belongs to that reconstruction; it is not a transfer from another programme.
- A search of the 840 KB NS workbench TeX finds no occurrence of "Fabel". "Jacobi" appears only inside "Jacobian" (change-of-variables determinants), never for the Jacobian-conjecture map.
- The Jacobian material flow of §1 lives in the YM workbench's Fabel files, which call it "the retained Navier–Stokes orbit".

So there is no certified NS-side transfer to state as a morphism. The edge Jacobian → NS kinematics of §1 is the one that exists, and it is proved here (Lemma 28.1).

## 5. The two local folders on the owner's computer

### 5.1 `quantum_tau_programme_bridge_20260924`

This folder is the programme's working folder for the three-lane edition. It holds the same blocks that `24_`–`27_` audited from the repository (commit 064f33b), for example GYSIN_DEFECT_CLOSURE…, POSITIVE_TRANSFER_UNIVERSAL_QUOTIENT… and EXACT_SCHWARTZ_SUMMATION_IMAGE…, together with receipts, drawings and packaged continuations. It is not a bridge between programmes.

Its `RESULTS_BULLETIN_2026-09-25.md` has 15 entries: SZ-20260925-001 to -013, then -017 and -018. Numbers 014–016 do not appear.
- **Audited in `12_`, `14_`, `16_`, `18_`, `24_`–`27_`:** GDC, CFP/CPS, SPF/SMC, OZD, NHJ, NCI, NPE/NER (in part), RSS, and AST/ACD (in part).
- **New, not yet read by me:**
  - GDE (Gaussian defect energies and determinants) and ABH (the trace-class Hardy observation of the boundary);
  - NJS/SSR (the choice of residue section) and NHI/HSR/HBW (holomorphic specialization and boundary continuation);
  - BML/BMR (the winding-difference lift) and BRC/BRR (the ramified boundary comparison);
  - GJN/GJNR (algebraic jet ramification);
  - ETR, whose ETR1 claims "the sharp first-negative formal Euler-log bound −1/6, extending CEI's free-monoid criterion".
- ETR1 touches `11_` directly (the formal logarithm of a monoid of integers and freeness), so it is the next item of board task 8.

### 5.2 `cyclotomic_clock_transfer_20260924` (CCT-1 to CCT-8)

**What it proves.** The owner's finite signed clocks G_N = ⟨T, J, ε | [T, J] = 1, T^N = 1, J² = ε, ε² = 1⟩ ≅ C_N × C₄, with N even, are joined to the Bost–Connes group ring R = ℤ[ℚ/ℤ], with σ_n(e(r)) = e(nr) and the unnormalised transfer ρ_n(e(r)) = Σ_{ns=r}e(s). The main points are:
- **The integral relations (CCT-2, (14)).**
  - σ_mσ_n = σ_mn and ρ_mρ_n = ρ_mn.
  - σ_nρ_n = n and ρ_nσ_n = multiplication by E_n = Σ_{k<n}e(k/n).
  - E_n² = nE_n and ρ_n(a)ρ_n(b) = nρ_n(ab).
  - ρ_n(σ_n(a)b) = aρ_n(b) and σ_mρ_n = dρ_{n/d}σ_{m/d}, with d = gcd(m, n).
  - Check C1 tests all of them on random elements of ℤ[ℚ/ℤ] for n, m ∈ {2, 3, 4, 6}: 640 configurations, no failures.
- **The defect ideals (CCT-2a).**
  - ker σ_n = (e(1/n) − 1)R and im ρ_n = E_nR.
  - Each is the annihilator of the other, and their intersection is 0.
  - R/(ker σ_n + E_nR) ≅ R/nR.
  - At finite level, and this form is my addition rather than CCT's: for n | N, σ_n induces ℤ[C_N]/(I_n + E_nℤ[C_N]) ≅ (ℤ/n)[C_{N/n}]. The level drops to N/n, so the index is n^{N/n}. Check C2 confirms this by Smith normal form for six pairs (N, n); the ninth referee pass found the same for seven more.
- **The sign obstruction (CCT-1).** No character χ′ satisfies χ′ⁿ = χ with n even when χ(ε) = −1, since χ′(ε)ⁿ = 1. So even-degree Bost–Connes transfer is never a fibre map over a sign-faithful character of this group.
- **Scalar evaluation versus formal lifts (CCT-5 and CCT-5a).** On the sign-faithful characters, the kernel of scalar evaluation is exactly (J² + 1). The formal cyclotomic lifts separate the group ring when the prime set is unbounded.
- **Transfer stability of the prime seeds (CCT-6).**
  - The prime-only seeds are not stable under any transfer ρ_n with n > 1.
  - The smallest recipient closed under all degrees is all of ℤ[ℚ/ℤ].
  - For odd degrees, the smallest closed sets are U_c, the roots of unity whose order has 2-adic valuation at most c. Here c = 1, or c = 2 when the prime 2 is present; for monomial values c = 2.
- **The transfer comparison (CCT-7).** For odd n, pushing forward the source fibre agrees with the Bost–Connes transfer on the monomial T^aJ^b exactly when gcd(a, n) = 1. The defect lies in ker σ_n. (For even n the fibre over a sign-faithful point is empty.) Check C3 tests b = 0; the ninth referee pass tested 5,376 cases with b = 0, …, 3 and negative a, with no mismatch.

**Verdict.** The identities I tested are correct. The algebra is elementary, and CCT states no RH or cohomology claim.
- The integral relations are consistent with the integral model of the Bost–Connes system, on the evidence of the abstract only. Connes, Consani and Marcolli, *Fun with 𝔽₁* (arXiv:0806.2401), give "an explicit model over the integers" for the Bost–Connes endomotive.
- This refines item 1 of goal 2 in the register (prime clocks and the Bost–Connes / Laca–Raeburn crossed product, `01_`) in two ways. First, it records exactly where the owner's sign ε blocks even degrees. Second, it gives the integral quotient ℤ/n that the unnormalised transfer keeps.

## 6. Items for the goals

- **Goal 2 (bridges).**
  - The Jacobian polynomial → incompressible polynomial flow with finite-time escape (Lemma 28.1), → the YM tensor transfer. Every step is typed. The YM end stops at finite-regulator projected states (claimed by the source's Section 14; not checked), along regulators whose coupling tends to 0.
  - S⁶ → YM through the single number D = det B (Lemma 28.2).
  - The finite signed clocks → the integral Bost–Connes ring (CCT), with the sign obstruction and the quotient ℤ/n.
- **Goal 1 (negative results with scope).**
  - The Jacobian → YM chain yields no fixed-coupling or continuum mass-gap statement. The source's own zero-quotient sequence (Theorem 14.2) has g_j → 0 and growing physical box, and the continuum identification is unresolved by its own account. The endpoint of K_τ is a loss of ellipticity, not a singularity.
  - The S⁶ → YM edge uses no property of S⁶ beyond D > 0.
  - The NS workbench certifies none of its early transfers.
  - Prime-only clock seeds are not transfer-stable (CCT-6a).
- **Goal 3 (standalone lemmas).** Lemmas 28.1 and 28.2; the finite-level index n^{N/n} (CCT-2a, check C2).
- **Board task 8, next.** The eight new bulletin items of §5.1, starting with ETR1.

## 7. Checks (`checks/cross_programme_bridges_part2_checks.py`)

| # | Statement | Result |
|---|---|---|
| J1 | det DF = −2 | holds |
| J2 | Piola: Σ_j ∂_j adj(DF)_{ji} = 0 | holds |
| J3 | U₀ = DF^{−1}(2,0,0) (degree 8) and U = DF^{−1}(2, 6F₃, 0) (degree 13) are polynomial and divergence-free | holds |
| J4 | F(γ(τ)) = (−1/4 + 2τ, 0, 0); γ is an integral curve of U₀ and U | holds |
| J5 | det A_τ = 1, A_0 = I; \|ζ_τ\|²z^6 → 81/16; z^6K_τ → vv^T, \|v\|² = 337/64 | holds |
| J5b | z^6 e₂(K_τ) → 121/64 and z^6 tr K_τ → 337/64, with det K_τ = 1 (the three eigenvalue asymptotics) | exact |
| J6 | the endpoint coefficients 113569/36864, 100825/12288, 531/512 | exact |
| J7 | an example of Lemma 28.1(c): for G = (x, y + x², w + (y + x²)³) and V = (2, 0, 0), the integral curves are G^{−1}(lines), polynomial in τ and complete | holds |
| S1 | det B = Lq + 6m²; du₁∧du₂ = D^{−1}dy₁∧dy₂; A_orig = (2π/D)y₁dy₂ + df | holds |
| C1 | integral Bost–Connes relations, 640 configurations | no failures |
| C2 | [ℤ[C_N] : I_n + E_nℤ[C_N]] = n^{N/n}, six (N, n) | holds |
| C3 | pushforward equals transfer iff gcd(a, n) = 1; the defect lies in ker σ_n | holds |

## 8. Sources

- The YM workbench files listed at the top (commit fa79faf), and the owner's local folders `cyclotomic_clock_transfer_20260924` and `quantum_tau_programme_bridge_20260924`.
- A. Connes, C. Consani, M. Marcolli, *Fun with 𝔽₁*, arXiv:0806.2401. Its abstract describes an explicit model over the integers of the Bost–Connes endomotive; the relations were not compared line by line.
- J. Kogut and L. Susskind, Phys. Rev. D 11 (1975) 395–408, cited by the YM file for the Hamiltonian lattice formulation; not re-read.

## 9. Revisions after the ninth referee pass (12:56 UTC)

1. **Major.** §0 item 2, §2 and §6 said that the YM end stops at trial states and that the Fabel-to-state map is missing. The source's later Section 14 (FABEL_CORRECTIONS; `FABEL_LOW_MODE_TRANSFER.md`, Theorem 14.2) claims a proved finite-regulator sequence of physical vectors orthogonal to the vacuum, with energy quotients ~ 100√2π/j. The note now reports this claim, with its regulators L_j = j², a_j = 1/(100j) and g_j < 1/j. The physical box grows and the coupling tends to 0. The note also records that the continuum identification is unresolved by the source's own account, and relates the result to `21_` scope limit 21.4. The proof of Theorem 14.2 was not checked.
2. The bulletin has 15 entries, not 18. The folder holds the same blocks that `24_`–`27_` audited from the repository.
3. The presentation of G_N now includes [T, J] = 1 and N even. The finite-level index is stated for n | N, marked as my addition, and derived. The CCT-7 statement is limited to odd n.
4. Lemma 28.2's "any torus with the same D" is limited to the non-wrapping patch, and the source's own display is credited.
5. The NS TeX search result is corrected ("Jacobi" occurs only inside "Jacobian"). The "source says so" about U and NS now cites FABEL_CORRECTIONS item 6.
6. Notation: V(y) = (2, 6y₃, 0). Row J7 now describes the single example it tests, and the script comment is corrected. Register cross-references and the *Fun with 𝔽₁* wording are softened to what the abstract supports.
