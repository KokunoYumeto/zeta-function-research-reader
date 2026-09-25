# The proof of Theorem 14.2 of the Yang–Mills workbench: the low-mode sequence is the free two-gluon threshold of a shrinking-coupling box

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 15:36 UTC. Board task 8, item carried over from `28_`: the statement of Theorem 14.2 was read there, but its proof was not checked. The first pass was an audit by one subagent (15:05–15:31 UTC); §0 says what I verified myself. Not yet refereed.

## 0. Source, method and checks

- **Source.** `FABEL_LOW_MODE_TRANSFER.md` from the Yang–Mills workbench (the file read for `28_`), SHA-256 `04a0415f…5c768c79`, read in full by the subagent.
- **Related files.** These were read as needed:
  - `FABEL_TENSOR_TRANSFER.md`, `FABEL_CURVATURE_TO_PHYSICAL_STATE.md`, `FABEL_AFFINE_ELECTRIC_SPECTRAL_MAP.md`;
  - `FABEL_CORRECTIONS_20260908.md`, `FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md`;
  - `magnetic_translation_true_vacuum.md`.
- **Checks.** `checks/ym_theorem_14_2_audit_checks.py`, 14 items (Y1–Y14), written by the subagent and copied here unchanged apart from the header. My re-run at 15:34–15:36 UTC gives 14/14 PASS. No item computes the interacting spectrum on the boxes with L ≥ 2; that is not feasible.
- **Verified by me.**
  - The scale identities of §3: Δ_j, j·Δ_j → 100√2π, the box side, Q_j·ℓ_j → 2√2π.
  - The identification of Δ_j as twice the lowest transverse free mode of the open box.

**Verdict.**
- **The algebra is correct.** Every displayed identity and asymptotic that the subagent re-derived holds.
- **The proof is a valid diagonal argument, conditional on the fixed-box weak-coupling limits** (g → 0 at fixed L and a). The file only sketches these and credits their proofs to sources that were not available here. Those limits are harmonic-approximation results of a standard type (B. Simon, Ann. Inst. H. Poincaré A 38 (1983) 295, for nondegenerate minima). The sketch omits one detail, in §2 item 1.
- **The theorem is the expected free-field behaviour.** The quotient it produces is the lowest free two-gluon colour-singlet energy of an open box whose side grows like j/50, at couplings g_j < 1/j. It gives no evidence against a mass gap.

## 1. The statement and its objects

- **Lattice.** Vertices form the open box {−L, …, L}³, with spacing a and gauge group SU(2).
- **Hamiltonian.** The Kogut–Susskind Hamiltonian H = κΣ_eE_e + bΣ_p(2 − W_p), with κ = 2g²/a, b = 1/(2g²a) and W_p = tr U_p.
  - The constant is chosen so that the potential is ≥ 0.
  - The physical space is the gauge-invariant subspace of L²(SU(2)^E).
  - The vacuum ψ is the true positive ground state, with energy ℰ.
- **The vectors.** w_j = 1_{(Δ_j/2, 11Δ_j/10)}(H_{g_j} − ℰ_{g_j})Ξ_{f_{S_j}}. Here Ξ_f is the vacuum-centred image of a "Fabel tensor" source D_f, and the spectral projection is taken on the physical space.
- **The regulators.** L_j = j², a_j = 1/(100j), N_j = 2j² + 1, σ_j = 2√2 sin(π/(2N_j)) and Δ_j = 2σ_j/a_j.
- **The claim.** There are dyadic couplings g_j < 1/j such that each w_j is physical, smooth and orthogonal to ψ. The energy quotient Q_j = ⟨w_j, (H − ℰ)w_j⟩/‖w_j‖² satisfies j·Q_j → 100√2π. The norms satisfy j^{−18}‖w_j‖² → 𝒞_* ≈ 44705.92.

## 2. The proof, step by step (subagent's audit)

The following steps check out:
- the tree gauge and its Haar measure;
- the matrices T, G, C, R and O of the linearization (Y1);
- the comparison oscillator, with quanta σ_ν/a and the one-plaquette normalisation (Y12);
- the moment bounds (Y11);
- the electric and magnetic coefficients (113) and (115), checked symbolically (Y9);
- the colour-contraction norms (116);
- the transverse spectrum (117). The three lowest modes sit at σ² = 2s² and the next at 3s² (Y2, Y3).
- Theorem 14.1, including the endpoint sums, the Dirichlet-kernel steps, the block (119), its explicit inverse and (120) (Y4–Y8).
- Band isolation: the lowest singlet level is 2σ/a with multiplicity 6, the next is 1.11237 times that, and three quanta are at least 1.5 times it (Y10).
- The diagonal choice of the n_j, orthogonality to ψ (since 0 is outside the window), physicality, the window |Q_j/Δ_j − 1| < 1/(10j), and the constants 109321/2048, 531/512 and 𝒞_* (Y13–Y14).

**Gaps and scope points.**
1. **Everything rests on the fixed-box weak-coupling limits,** which are only sketched in the file. In the fixed chart, W = ¼|Cy|² + O(|y|³) because of commutator terms. So the quadratic comparison holds only up to a factor 1 ± O(ρ): the lower bound needs g → 0 first and then ρ → 0. The file's stated error O_{L,ρ}(g²) covers only the localisation error.
2. **The couplings are specified but not effective.** n_j is the least integer satisfying inequalities about the unknown interacting spectrum. There is no rate, and g_j < 1/j is only an upper bound.
3. **The quotient does not depend on the Fabel tensor.** Any nonzero vector in the range of 1_I(H − ℰ) has its quotient in the window Δ_j(1 ± 1/(10j)).
   - The tensor S_j affects only the norm ‖w_j‖² and the fact that the projection of Ξ is nonzero.
   - The proof shows that the finite-regulator physical gap itself lies in that window.
4. **Precision.** The left end Δ/2 of the window is the one-gluon colour-adjoint level. The projection argument is valid because the projection is taken on the colour-singlet (physical) space, as the file defines it.
5. **A correction to `28_`.** `28_` §2 called j/100 the box length. That is L_j·a_j, the half-side. The full side is ℓ_j = 2L_j·a_j = j/50.

## 3. What the theorem is: the free two-gluon threshold (my verification)

- **The quotient.** Δ_j = 2σ_j/a_j = 400√2·j·sin(π/(4j² + 2)).
  - Since sin x ≤ x, jΔ_j ≤ 400√2·j²·π/(4j² + 2) < 100√2π.
  - jΔ_j → 100√2π, with relative deficit about 1/(2j²).
  - Q_j lies in Δ_j(1 ± 1/(10j)). For example Q₂ ∈ (186.64, 206.28) and Q₁₀ ∈ (43.77, 44.65) (Y14).
- **The mode.** σ_j/a_j is the lowest transverse eigenfrequency of the lattice Laplacian on the open box with N_j points per side.
  - Its momentum is (π/N_j)(1, 1, 0)·a_j^{−1}, and 4sin²(π/(2N)) + 4sin²(π/(2N)) = σ².
  - So Δ_j = 2σ_j/a_j is the lowest free two-gluon colour-singlet energy.
- **The scale.** The full side is ℓ_j = 2L_ja_j = j/50. Hence

  Q_j·ℓ_j → (100√2π/j)·(j/50) = 2√2π ≈ 8.886, and Q_j/(2π/ℓ_j) → √2.

  A product Q·ℓ that tends to a constant is the scaling of a massless free field in a box of side ℓ. With a mass gap m > 0, Q·ℓ would grow without bound as ℓ grows.
- **The regime.** The regulators combine g_j → 0 with a growing box. In a fixed box, as g → 0, the theory approaches three free Maxwell fields restricted to colour singlets (gap 1 above). Such fields have no gap in infinite volume, so the sequence reproduces free-field behaviour.
  - For comparison, on a periodic torus the weak-coupling levels scale differently, of order g^{2/3}/ℓ, because of the constant modes (M. Lüscher, Nucl. Phys. B219 (1983) 233). The open box has no such flat directions.

## 4. Negative result and bridge (goals 1 and 2)

- **34.N1. The Jacobian → Yang–Mills chain produces the free two-gluon threshold, not a statement about the mass gap.**
  - Theorem 14.2's vectors have energy quotients equal, up to a factor 1 ± 1/(10j), to the free two-gluon singlet threshold of an open box of side j/50, at couplings below 1/j.
  - This is the expected small-coupling, finite-volume behaviour. The file's own disclaimer, that there is no continuum identification, is accurate.
  - This completes `28_`'s scope limit for the YM transfer (register negative result 49) with the proof now checked.
- **Bridge.** The only arithmetic input of the construction, the Fabel/Jacobian tensor S_j, affects the norm of w_j and not its energy (§2 item 3). So nothing of the Jacobian map is visible in the energy quotient. This parallels `21_` scope limit 21.4 (coupling → 0 with a growing box).

## 5. Not checked

- The three source files to which the file credits the fixed-box limits. They were not available, and a search of the NS workbench found none of them.
- The interacting spectrum on the boxes with L ≥ 2. The checks test the weak-coupling mechanism only in the one-plaquette case.
