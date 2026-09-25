# The proof of Theorem 14.2 of the Yang–Mills workbench: the low-mode sequence is the free two-gluon threshold of a shrinking-coupling box

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 15:36 UTC. Board task 8, item carried over from `28_`: the statement of Theorem 14.2 was read there, but its proof was not checked. The first pass was an audit by one subagent (15:05–15:31 UTC); §0 says what I verified myself. Refereed in the twelfth pass (16:43 UTC) and revised at 16:51 UTC; §6 lists the changes.

## 0. Source, method and checks

- **Source.** `FABEL_LOW_MODE_TRANSFER.md` from the Yang–Mills workbench, SHA-256 `04a0415f…5c768c79`, read in full by the subagent. (`28_` §2 read only the statement of its Theorem 14.2.)
- **Related files.** These were read as needed:
  - `FABEL_TENSOR_TRANSFER.md`, `FABEL_CURVATURE_TO_PHYSICAL_STATE.md`, `FABEL_AFFINE_ELECTRIC_SPECTRAL_MAP.md`;
  - `FABEL_CORRECTIONS_20260908.md`, `FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md`;
  - `magnetic_translation_true_vacuum.md`.
- **Checks.** `checks/ym_theorem_14_2_audit_checks.py`, 14 items (Y1–Y14), written by the subagent and copied here unchanged apart from the header. My re-run at 15:34–15:36 UTC gives 14/14 PASS, and the referee's re-run reproduced the stored output byte for byte. The corrections of the twelfth pass are checked in `checks/referee12_notes34_35_checks.py`, items A1–A6 (19/19 PASS for the whole script). No item computes the interacting spectrum on the boxes with L ≥ 2; that is not feasible.
- **Verified by me.**
  - The scale identities of §3: Δ_j, j·Δ_j → 100√2π, the box side, Q_j·ℓ_j → 2√2π.
  - The identification of Δ_j as twice the lowest transverse free mode of the open box.

**Verdict.**
- **The algebra is correct.** Every displayed identity and asymptotic that the subagent re-derived holds.
- **The proof is a valid diagonal argument, conditional on the fixed-box weak-coupling limits** (g → 0 at fixed L and a). The file only sketches these and credits their proofs to sources that were not available here.
  - The eigenvalue limits are harmonic-approximation results of a standard type: B. Simon, "Semiclassical analysis of low lying eigenvalues. I. Non-degenerate minima: asymptotic expansions", Ann. Inst. H. Poincaré Sect. A 38 (1983) 295–308. Its Theorem 1.1 treats −Δ + λ²h + λg under hypotheses (A1)–(A4) (p. 296), and its §6 treats Laplace–Beltrami operators on Riemannian manifolds.
  - Here H = κ(−Σ_eΔ_e + λ²Σ_p(2 − W_p)) with κ = 2g²/a and λ = 1/(2g²), since b/κ = 1/(4g⁴) (the workbench's (1.1)). One step is needed before the citation applies: in the tree gauge, where the minimum is isolated, the kinetic term must be written as a Laplace–Beltrami operator plus a bounded potential.
  - The vector limits (113) and (115) are not of that type; the file derives them from its moment bounds.
  - The sketch also omits one detail, in §2 item 1.
- **The theorem reproduces free-field values.** Up to a factor 1 ± 1/(10j), its quotient Q_j equals 2σ_j/a_j, the lowest free two-gluon colour-singlet energy of the open box of side j/50, at couplings g_j < 1/j. It does not bear on the mass gap in either direction: its conclusion follows from the fixed-box limits and the choice of g_j, whether or not the continuum theory has a gap (§3).

## 1. The statement and its objects

- **Lattice.** Vertices form the open box {−L, …, L}³, with spacing a and gauge group SU(2).
- **Hamiltonian.** The Kogut–Susskind Hamiltonian H = κΣ_eE_e + bΣ_p(2 − W_p), with κ = 2g²/a, b = 1/(2g²a) and W_p = tr U_p.
  - The constant is chosen so that the potential is ≥ 0.
  - The physical space is the gauge-invariant subspace of L²(SU(2)^E).
  - The vacuum ψ is the true positive ground state, with energy ℰ.
- **The vectors.** w_j = 1_{(Δ_j/2, 11Δ_j/10)}(H_{g_j} − ℰ_{g_j})Ξ_{f_{S_j}}. Here Ξ_f = (D_f − ⟨ψ, D_fψ⟩)ψ is the vacuum-centred image of the weighted local-energy operator D_f = κΣ_e f_eE_e + Σ_p f_p b(2 − W_p), with f_p the average of f_e over the four edges of p (`FABEL_TENSOR_TRANSFER.md` (97)). The weight is f = f_S, f_S(e) = m(e)ᵀSm(e), where m(e) is the midpoint of e and S = S_j is the "Fabel tensor". The spectral projection is taken on the physical space.
- **The regulators.** L_j = j², a_j = 1/(100j), N_j = 2j² + 1, σ_j = 2√2 sin(π/(2N_j)) and Δ_j = 2σ_j/a_j.
- **The claim.** There are dyadic couplings g_j < 1/j such that each w_j is physical, smooth and orthogonal to ψ. The energy quotient Q_j = ⟨w_j, (H − ℰ)w_j⟩/‖w_j‖² satisfies j·Q_j → 100√2π. The norms satisfy j^{−18}‖w_j‖² → 𝒞_* ≈ 44705.92.

## 2. The proof, step by step (subagent's audit)

The following steps check out:
- the tree gauge and its Haar measure;
- the matrices T, G, C, R and O of the linearization (Y1);
- the comparison oscillator, with quanta σ_ν/a and the one-plaquette normalisation (Y12);
- the ingredients of the moment bounds (Y11: the derivative identity and Σ|XW|² ≤ 16W), and the moment inequality in the one-plaquette case (Y12);
- the electric and magnetic coefficients (113) and (115), checked symbolically (Y9);
- the colour-contraction norms (116);
- the transverse spectrum (117). The three lowest modes sit at σ² = 2s² and the next at 3s² (Y2, Y3).
- Theorem 14.1, including the endpoint sums, the Dirichlet-kernel steps, the block (119), its explicit inverse and (120) (Y4–Y8).
- Band isolation: the lowest singlet level is 2σ/a with multiplicity 6, the next is 1.11237 times that, and three quanta are at least 1.5 times it (Y10).
- The diagonal choice of the n_j, orthogonality to ψ (since 0 is outside the window), physicality, the window |Q_j/Δ_j − 1| < 1/(10j), and the constants 109321/2048, 531/512 and 𝒞_* (Y13–Y14).

**Gaps and scope points.**
1. **Everything rests on the fixed-box weak-coupling limits,** which are only sketched in the file. In a fixed chart of radius ρ, W = ¼|Cy|² + O(|y|³) because of commutator terms (on plaquettes with three or four chord edges; check A6), and the kinetic metric and the Haar density differ from flat ones by O(|y|²). So the quadratic comparison holds only up to a factor 1 ± O(ρ). With a fixed chart the lower bound needs g → 0 first and then ρ → 0; a chart shrinking with g, as in Simon's proof, avoids the second limit. The file's stated error O_{L,ρ}(g²) covers only the localisation error.
2. **The couplings are specified but not effective.** n_j is the least integer satisfying inequalities about the unknown interacting spectrum. There is no rate, and g_j < 1/j is only an upper bound.
3. **The window, and hence the limit of j·Q_j, do not depend on the Fabel tensor.** Any nonzero vector in the range of 1_I(H − ℰ) has its quotient in the window Δ_j(1 ± 1/(10j)).
   - The projection has rank six (the file's proof of Theorem 14.2), and at finite g its six eigenvalues need not coincide. Q_j is their average weighted by the components of w_j, so the tensor S_j decides where Q_j lies inside the window.
   - The tensor also fixes the norm ‖w_j‖², hence the energy ⟨w_j, (H − ℰ)w_j⟩ = Q_j‖w_j‖²: the constant 𝒞_* in (128)–(129) is computed from the tensor limit S_*.
   - The proof shows that the finite-regulator physical gap itself lies in the window.
4. **Precision.** The left end Δ/2 of the window is the one-gluon colour-adjoint level. The projection argument is valid because the projection is taken on the colour-singlet (physical) space, as the file defines it.
5. **A correction to `28_`.** `28_` §0 item 2 and §2 called j/100 the box length. That is L_j·a_j, the half-side. The full side is ℓ_j = 2L_j·a_j = j/50.

## 3. What the theorem is: the free two-gluon threshold (my verification)

- **The quotient.** Δ_j = 2σ_j/a_j = 400√2·j·sin(π/(4j² + 2)).
  - Since sin x ≤ x, jΔ_j ≤ 400√2·j²·π/(4j² + 2) < 100√2π.
  - jΔ_j → 100√2π, with relative deficit about 1/(2j²).
  - Q_j lies in Δ_j(1 ± 1/(10j)). For example Q₂ ∈ (186.637, 206.284) and Q₁₀ ∈ (43.765, 44.650), rounded outward (Y14; check A4).
- **The mode.** σ_j/a_j is the lowest transverse eigenfrequency of the lattice Laplacian on the open box with N_j points per side.
  - Its momentum is (π/N_j)(1, 1, 0)·a_j^{−1}, and 4sin²(π/(2N)) + 4sin²(π/(2N)) = σ².
  - So Δ_j = 2σ_j/a_j is the lowest free two-gluon colour-singlet energy.
- **The scale.** The full side is ℓ_j = 2L_ja_j = j/50. Hence

  Q_j·ℓ_j = (j·Q_j)·(ℓ_j/j) → 100√2π·(1/50) = 2√2π ≈ 8.886, and Q_j/(2π/ℓ_j) → √2 (check A5).

  A product Q·ℓ that tends to a constant is the scaling of a massless free field in a box of side ℓ. This says nothing about a mass gap of the continuum theory. Along this sequence the coupling tends to 0 as the box grows, and g_j is chosen at each j small enough for the fixed-box harmonic approximation to hold to relative accuracy 1/(10j). So Q_j·ℓ_j → 2√2π follows from the free spectrum alone, and it would hold whether or not the continuum theory has a gap. (For a single fixed theory with a gap m > 0, one expects the lowest excitation in a large box to stay near m, so that Q·ℓ would grow like mℓ. That is a heuristic, not a theorem, and it does not apply to a sequence whose coupling tends to 0.)
- **The regime.** The regulators combine g_j → 0 with a growing box. In a fixed box, as g → 0, the low-lying spectrum approaches that of three free lattice Maxwell fields restricted to colour singlets (conditional on the fixed-box limits, §2 item 1). Because g_j is chosen at each j inside this regime, the sequence reproduces the free values. (The free Maxwell field is gapless in infinite volume.)
  - For comparison, on a periodic torus the lowest weak-coupling levels scale differently: they are of order g^{2/3}/ℓ, with an expansion in powers of g^{2/3} (g the renormalized coupling), because the constant modes have a quartic classical potential (M. Lüscher, "Some analytic results concerning the mass spectrum of Yang-Mills gauge theories on a torus", Nucl. Phys. B219 (1983) 233–261; for the zero-mode mechanism see P. van Baal, arXiv:hep-th/9705112, introduction). The open box has no such flat directions: W has a unique zero, with nondegenerate Hessian (all σ_ν > 0; Y1, Y2).

## 4. Negative result and bridge (goals 1 and 2)

- **34.N1. The Jacobian → Yang–Mills chain produces the free two-gluon threshold, not a statement about the mass gap.**
  - Theorem 14.2's vectors have energy quotients equal, up to a factor 1 ± 1/(10j), to the free two-gluon singlet threshold of an open box of side j/50, at couplings below 1/j.
  - This is what the harmonic approximation gives at small coupling in a finite box. The file's own disclaimer, that there is no continuum identification, is accurate.
  - This completes `28_`'s scope limit for the YM transfer (register negative result 49): the proof is now checked, except for the fixed-box weak-coupling limits, which the file only sketches (§2 item 1).
- **Scope remark (with 34.N1; register bridge 38).** The only input from the Jacobian map, the Fabel tensor S_j, fixes ‖w_j‖² and hence the energy ⟨w_j, (H − ℰ)w_j⟩ = Q_j‖w_j‖²; the constant 𝒞_* in (128)–(129) is computed from S_*. It moves Q_j only inside the tensor-independent window Δ_j(1 ± 1/(10j)) (§2 item 3). So nothing of the Jacobian map is visible in the limit j·Q_j → 100√2π. This parallels `21_` scope limit 21.4, where the quotient bound likewise does not depend on the NS profile (coupling → 0 with a growing box). The tensor is algebraic data of the Jacobian-conjecture map (`28_` §1), not arithmetic data.

## 5. Not checked

- The three source files to which the file credits the fixed-box limits. They were not available: a search of the staged YM files, of the NS workbench TeX and of the staged programme folders finds the three titles only in the file's own line 11.
- The interacting spectrum on the boxes with L ≥ 2. The checks test the weak-coupling mechanism only in the one-plaquette case.

## 6. Revision after the twelfth referee pass (16:51 UTC)

One referee (a subagent) re-read the source, re-ran the check script (byte-identical output), recomputed every number and read Simon's paper (numdam) and the abstract of Lüscher's (ScienceDirect). Its 3 major findings on `34_`–`35_` include 2 on this note; I verified both against the source (the rank-six projection and (128)–(129) in the proof of Theorem 14.2) and applied them:
- **§3, the scale.** The sentence "With a mass gap m > 0, Q·ℓ would grow without bound as ℓ grows" stated a heuristic as a fact, and it does not apply to this sequence, whose coupling tends to 0 while g_j is chosen inside the weak-coupling regime. Replaced; the verdict now says that the theorem does not bear on the mass gap in either direction.
- **§2 item 3 and §4.** "The quotient does not depend on the Fabel tensor" and "affects … not its energy" were false as written. The window and the limit of j·Q_j are tensor-independent; the position of Q_j inside the window and the energy are not. The same correction is made in `28_` and in register entry 57.

Minor findings applied: the Simon citation made exact, with the step needed before it applies (verdict); the description of Ξ_f (§1); the check labels Y11/Y12 (§2); the omitted detail now includes the metric and Haar-density corrections (§2 item 1); the correction to `28_` extended to its §0 (§2 item 5); the sample windows rounded outward (§3; check A4); the limit written without j on the right (§3); "gap 1 above" and the reason for the free values (§3); the Lüscher citation made exact (§3); "expected" and "now checked" qualified (§4); the search statement (§5); the source-line note on `28_` (§0); the item in §4 renamed a scope remark and registered as bridge 38. New check script: `checks/referee12_notes34_35_checks.py` (items A1–A6 for this note).
