# 51a_ The Navier–Stokes workbench: first-pass inventory, architecture, verification and bridges (subagent report)

*Status of this file.* First-pass report written by a subagent of the coordinating session (27 September 2026, 11:40–12:27 UTC) and kept as written, apart from three removals marked [removed]. The coordinator re-ran every script here (outputs identical apart from timing lines), read `certify_collision.py` line by line, re-derived the NS → YM rate bounds, settled D1 against the official PDF, and certified items 1–2 of §6; see `51_`. Script paths below refer to `checks/ns51/first_pass/`.

Claude (model `claude-opus-5-5`), 27 September 2026. First-pass audit for the coordinator's lane. Everything below was read or computed read-only; my scripts and their outputs are in this folder (`*_OUTPUT.txt`). Quotations are under 15 words.

**Subject.**
- `KokunoYumeto/yang-mills-interacting-workbench` at `fa79faff` (21 Sep 2026), folder `navier-stokes/`.
  - The local copy `/home/claude/work/ns/navier-stokes/` is byte-identical to that commit (7 files compared).
  - The bundle ZIP hash (`43b128e2…`) and the 208-page PDF hash (`242fe7f8…`) match `navier_stokes_checks.json`.
  - All 119 manifest-listed bundle members match `navier_stokes_primary_manifest.json` (`run_workbench_checkers_OUTPUT.txt`).
- The source-faithful transcription of OpenAI's 166-page manuscript, pinned at `5e162f34`. It is cited below as "src p.N" together with its `sections/ppXXX-YYY.tex` file and line.
- The 208-page reader `navier_stokes_workbench.tex`, cited as "reader L…".
- The zeta repository `zeta-function-research-reader` at `32acd0df`, for the NS satellites.

**Background.** OpenAI announced the manuscript on 8 September 2026 (the YM repository's `ns_inner_profile_curvature_current_bridge.md` §1 links the release, the PDF and the Lean repository). [removed: three further background items taken from search results and not verified.] I did not verify OpenAI's 166-page proof.

**Status classes.**
- **I**: imported from OpenAI's manuscript (NS-00 or its internal propositions).
- **E**: an exact identity or finite calculation that the workbench proves.
- **E✓**: re-derived by me (sympy) or re-run.
- **N**: numerical only.
- **C**: conditional on NS-00.
- **U**: unfinished, conjectural, or located only.
- **S**: a standard known result, re-proved.
- **M**: provenance or transcription only.
- **A**: an analogy or reading.
- **P**: an operator or map shared without a theorem (as in `47_`).

---

## 0. Summary

- **NS-00 is imported and unverified.** It is OpenAI's Theorem 1.1: for every ν > 0 there are a smooth compactly supported force and zero initial velocity giving a smooth solution on [0, 1) with bounded energy and lim sup‖u‖_∞ = ∞. On 𝕋³ this is Cor. 10.6.
  - The workbench is a reconstruction and verification reader. It lists four items as unfinished (research-state.json L232–236):
    - imported profile and admissible-stress existence;
    - all-stage realization and convergence;
    - the final force for the same assembled witness;
    - a formal endpoint and Comparator certificate.
  - Nothing here changes that.
- **Exact identities.** I re-derived 256 exact or finite claims with my own code (0 failures), plus 4 negative controls. They cover:
  - the leading-field calculus, including the full leading residual–stress identity R⁽⁰⁾ = −(∂_r + k/r)(q^{−A−1/2}T₀);
  - the order-n coefficient equations (5.2)–(5.6) for n = 0, 1, 2 from the full residual;
  - the actual-shear correction (AS7)–(AS40) and the ambient projection;
  - the principal exact identities of the vacuum-hydrodynamics continuation: TT lift, Lichnerowicz reduction, momentum constraint, Kasner bijection and inverse, Einstein check, Kretschmann limit, decoder;
  - the bridge identities (NS→YM abelian and non-abelian, NS→zeta Mellin, S⁶→NS Beltrami, Jacobian map);
  - the viscosity, parabolic and periodization maps.
- **The workbench's own checkers.** The nine replay programs (144 result groups, 12 probes) and `verify_recovered_formulas.py` pass on fresh copies. The regenerated receipts match the shipped receipts in content; they differ only in CRLF line endings.
- **New: the Rindler pole collision is now interval-certified** (`certify_collision.py`, python-flint/Arb). This is NS-04(c), which the continuation itself says is not certified. The certificate shows a nondegenerate double zero of I′_α(q) in the box
  - |q − 0.778472800990330076180356446189| < 10⁻²⁰;
  - |α − (−0.569714080972361784438457668663)| < 1.5·10⁻¹⁰;
  - with F_q ∈ 1.750358… > 0 and F_αα ∈ [4.98, 5.02].
  - That one colliding branch is the hydrodynamic branch is shown only numerically (`track_hydro_branch.py`).
- **Bridges.**
  - Every NS→YM, NS→zeta and S⁶→NS link is an exact but elementary map (velocity → connection; velocity → Mellin transform; oscillator → Beltrami flow).
  - Where a link uses the blowup at all, it uses NS-00's growth rates and is conditional (C).
  - No bridge carries a theorem into YM-01, the S⁶ question or any zeta-zero statement.
  - There is no NS→S⁶ edge. The only S⁶→NS map is a two-parameter family of global smooth Beltrami solutions.
  - New traceability: the NS→YM rate bounds (250) that `21_` §2 imported unchecked are derived in the YM repository's `ns_inner_profile_curvature_current_bridge.md` §§4–5 from the source's (5.42) and Prop. 9.9. I checked every elementary step. They are therefore conditional on NS-00 (C), no longer "unchecked".
- **Discrepancies found (none mathematical).**
  - D1: the transcription's (10.20) on p.124 reads √2·X_in·τ, inconsistent with (3.6).
  - D2: `ATTEMPTS.md` points to NS-05 payloads that the bundle does not contain.
  - D3: a status tension between the reader's "Leading-profile assembly theorem" and the unresolved list.
  - See §7.

---

## 1. Inventory

### 1a. Survey IDs (NS-00 … NS-06, from `47a` §3) and the 13 components (research-state.json L39–188)

| ID | What it states | Class | Locators | This audit |
|---|---|---|---|---|
| **NS-00** | OpenAI Thm 1.1; Cor. 10.6 on 𝕋³ (alternatives (C), (D) of Fefferman's statement, per the source) | **I** | src p.1, `pp001-006.tex` L42–66; Cor. 10.6 src p.125, `pp121-126.tex` L406; research-state.json L9–19 | not verified; architecture mapped in §2 |
| **NS-01** reconstruction | the source's stage sequence, written out in 13 component bodies | E / I mix, per component (rows below) | reader L76–14245; bundle `proof_sources/*` | algebra spot-verified (§3) |
| NS-profiles | coordinates (3.2); derivative maps ∂_t(q^b f), ∂_z(q^b f); Cartesian axis extension; continuity via A + D = 1; pressure balance Π_X = F²; transport identity; sources S_q, S_n; radial primitives; stress T₀; five moments; cone equivalence; heat exterior; analytic axis contraction (App. B); continuation and five-moment join | **E** for the algebra; **I** for the inputs: pressure datum Π₀ from App. A (reader L360) and the outer profile and wave cone (L82) | reader L76–956 (core L80–355, axis L358–602, continuation L606–956); bundle `profiles/profiles_body.tex`; src pp.24–45, 144–157 | **E✓**: 67 identities (`check_leading_field`), 13 axis margins (`check_axis_numerics`); bundle's 14 re-run |
| NS-base_heat | order-n coefficient equations (φ), (U), (Π), (Ω); analytic Volterra recursion; power-moment maps; weighted residual identities; outer schedule; cone margins; heat factor; exterior stress | **E** for the algebra; leading-profile existence kept as input (reader L1174, L2369–2375) | reader L957–2377; src pp.45–62, 126–144 | **E✓**: coefficient equations assembled for n = 0, 1, 2 (`check_order_n_equations`); conservative forms (`check_cylindrical_forms`); Volterra convergence read, not re-derived |
| NS-oscillations | auxiliary torus J = [[3,1],[1,5]]; phase; pulse equation; covariance; curl identity; cutoff residuals; admissible shear loop (App. C) | **E**; imports Prop. 5.5 background (reader L2503) and App. A/B inputs (L3088) | reader L2378–3296; src pp.62–87, 157–165 | **E✓**: 26 actual-shear and projection identities, torus J; bundle's 28 re-run |
| NS-mean_corrections | §8: radial range, inverse and projection; cylindrical mean equations; pressure; five-dimensional moment correction | **E**; imports as above | reader L3297–3975; src pp.87–100 | **E✓**: MC11 transport and vector Laplacian; bundle's 26 re-run |
| NS-stage9 | §9: finite correction state, four-step cycle, σ_{j+1} = σ_j + 1/10, common domain, single-stage realization | **E** for finite stages; **U** for all-stage convergence (research-state L234) | reader L3976–4693; src pp.100–116 | bundle's 15 + 7 re-run; not re-derived |
| NS-terminal_endpoint | §10: localization, force limits, Borel-type extension, energy, comparison, viscosity and periodization maps | **E** (standard arguments) given Thm 3.1 | reader L4694–5356 (viscosity maps L5203–5290); src pp.116–126 | **E✓**: (10.22), (E.24)–(E.30), Cor. 10.6 scalings; logic read |
| NS-profile_assembly | "Leading-profile assembly theorem": all of Thm 4.6 for a chosen h | **E** claimed in writing; the workbench's own ledger still lists profile existence as unresolved (D3) | reader L5357–5985 (theorem L5900–5985) | algebra only (PA.1 = A16) |
| NS-stage_inputs | initialization, pulse data, maps and covariance, radial five-equation block | **E**, plus exponent arithmetic | reader L7858–10944 | bundle's 7 + 19 + 18 re-run |
| NS-summation_realization | Lemma 5.4 and Prop. 9.9 shrinking-cutoff summation | **E** in its bounded scope; its receipt excludes the upstream increments and full Prop. 9.9 | reader L10945–11645; bundle `primary_continuation/summation_realization_audit_receipt.json` | not audited |
| NS-terminal_trace | the trace H ↦ (∂_σ^j H(·,0)) onto force jets is continuous and onto; it has no continuous linear section | **S** (Borel's lemma; ω has no continuous norm) | reader L11646–11862 | read |
| NS-radial_stress_reconstruction_audit | compact radial stress with moments and chart factors | **E** | reader L11863–12232 | **E✓**: stress-primitive identities (reader L1377–1383) |
| NS-stage_cycle_gain_audit | four-step gain and invariants | **E**, exponent arithmetic | reader L12233–12950 | not audited |
| NS-global_closure_body | interface disposition; (AS1)–(AS40); ambient projection | **E** | reader L12951–14245 (AS L13543–13777; projection L14207–14229) | **E✓** (`check_actual_shear`) |
| **NS-02** corrections | the actual shear: −g·T = −\|g₀\|T_N − (g − g₀)·T with positive-production bounds; the S_* factors in derivatives of b·n_{Φ,r}; the plane-coordinate inverse | **E**. It corrects the workbench's own 162-page edition. The source's p.81 sentence is literally about the frozen shear −g₀·T and is correct as such (`pp079-084.tex` near (7.22)) | reader L45–60, L13543–13777; bundle `lanes/web_bundle_audit/actual_shear_energy_morphism.md` | **E✓** all |
| **NS-03** transcription | 166 pages, 6,175 formula occurrences; transcription checks only | **M** (provenance) | `SOURCE_READING_20260920.json` L38–55 | one inconsistency (D1) |
| **NS-04(a)** | any V ∈ C^∞_{c,div=0}(ℝ³) → exact vacuum constraint data (h, K) = (φ²δ, φ⁻²Ā + (τ_*/4)φ²δ) on ℝ⁴ with Λ = −6/L², plus a Newton decoder with 𝒟∘ℰ = id on marked data | **E** (existence of φ by barriers: **S**) | continuation README L23–84; `manuscripts/IDENTITY_AND_COMPLETION.md` §§5–6 (L395–708) | **E✓**: TT, trace, divergence, norm, cross term; R(φ²δ) = −6φ⁻³Δφ by direct curvature computation; momentum constraint div_h(φ⁻²Ā) = φ⁻⁴ div Ā; κ_* = 12a_*²; the decoder (Fourier, and a numerical kernel check to 1.4·10⁻¹⁴) |
| **NS-04(b)** | strain ↔ block-Kasner bijection onto P_w ∈ [−1/2, 1/4), with inverse and volume factor χ; the explicit Einstein metric (4.2) | **E** | README L86–104; IDENTITY §4 L211–393 | **E✓**: tr P = tr P² = 1; inverse; surjectivity modulo the Kasner ideal; range; Ric(g_S) = −(4/L²)g_S from a direct 5D Ricci computation; the Kretschmann limit (4.13) exactly; (4.11); (4.14) |
| NS-04(b′) | conserved radial tensor 𝒥 and the identity p⁽¹⁾ = δT^TF/(ε + p) = −2νS/c² | **E**, given the radial ODE (2.3) from the interior continuation | IDENTITY §2 L45–133 | **E✓**: ∂_r𝒥 = 0, the regular 𝒥, both evaluations consistent. (2.3) itself not derived |
| **NS-04(c)** | Rindler shear sector: Bessel reduction, response H(w, q), hydrodynamic pole ω = −iνk² − i(3ν³/2c²)k⁴ − i(29ν⁵/6c⁴)k⁶, pole collision, finite pole-cluster limit | **E** (reductions) + **N** (collision); collision existence now certified here | `manuscripts/RESEARCH.md` §§3–7 (L81–453); README L126–156 | **E✓**: (5), (13), (14), (28); all five series coefficients numerically (error/q¹² bounded); q_c, α_c, F_q, F_αα, C to 30 digits by an independent formulation; argument-principle count 2; **interval certificate** |
| **NS-04(d)** | slab stress: global regularity of NS + κΛ²𝒩 with symbol ≥ c_*k³ | **S** (hyperdissipation; Lions 1969, Tao 2009); concerns a modified equation | `SLAB_COMPARATORS.md` §2 L70–139 | **E✓**: (S1), (S3), (S5) closed form, (S7) constant C_Y = (1/10)(9/5)⁹C_GN³⁰, (S8) layer composition; the H² → H^s bootstrap not re-derived |
| **NS-05** | audits of the 40-page `fluid_blowup_reconstruction.zip` (Boussinesq, CKN, IPM, moving centre, arithmetic heat map) | **U** / located | YM `ATTEMPTS.md` L47–75 | the payloads are not in the bundle (D2); apparently in zeta `sidebar/fluid/tex/*` |
| **NS-06** | coupled viscous Boussinesq stages and a finite pulse bridge; the third return is unproved | **U** | YM `ATTEMPTS.md` L77–107; zeta `sidebar/fluid/tex/{boussinesq_core,coupled_viscous_control}.tex` | located only |

### 1b. The four unfinished items (research-state.json L232–236; RESEARCH_STATE.md L47)

1. Imported profile and admissible-stress existence: Thm 4.6, App. A–C.
2. All-stage realization and convergence: Prop. 9.6 iterated and Prop. 9.9.
3. The final force for the same assembled witness: Lemmas 10.2–10.3 applied to the actual summed fields.
4. A formal endpoint and Comparator certificate.
   - The Lean run stopped (research-state L242).
   - A static comparison of 26/26 statements is recorded; it is not kernel checking (L25–31).

---

## 2. Architecture of OpenAI's construction (src = transcription; reader = 208-page reconstruction)

**0. Ansatz (src p.3, `pp001-006.tex` L142–159; p.7).**
- For any incompressible (u, p) the force is defined as the residual f := ℛ(u, p) = ∂_t u + (u·∇)u − Δu + ∇p. The equations then hold trivially.
- The task is a flow that blows up while the residual and all its derivatives extend smoothly through t = 1.
- The construction is done at ν = 1. Any ν > 0 follows from (u, p, f) ↦ (√ν u(x/√ν, t), νp(x/√ν, t), √ν f(x/√ν, t)), which leaves the singular time unchanged ((10.22), p.124; verified).

**1. Coordinates and leading profiles (§3.1 pp.7–8; §4 pp.24–45; App. B pp.144–157; reader L76–956).**
- Coordinates: τ = 1 − t = q(1 − η²), z = q^D η, X = r²/(2q), with A = 1/2 + h, D = 1/2 − h and 0 < h < 1/100.
- Fields: u_θ = q^{−A}E, u_z = q^{−A}U, ru_r = V₀ (from incompressibility), p = q^{−2A}Π.
- Scales: ℓ_r ≍ τ^{1/2}, ℓ_z ≍ τ^{1/2−h}, |u_θ|, |u_z| ≍ τ^{−1/2−h}. The core becomes a slender column.
- Theorem 4.6 (p.32, `pp031-036.tex` L111) fixes profiles such that:
  - the tangential residuals are exact radial divergences of a stress q^{−A−1/2}T₀;
  - T₀ = 0 for X ≤ X_a (inner, stress-free) and for X ≥ X_b;
  - T₀ lies strictly inside an admissible cone on the annulus X_a < X < X_b;
  - the exterior X ≥ X_b is the exact heat solution K = c_∞ s^{−A}𝓗(2τ/s). Here 𝓗 is a Tricomi function: 𝓗(Z) = Z^{−1−h}U(1+h, 2, 1/Z) (verified).
- App. B: the axis profile comes from a contraction in a weighted analytic coefficient space (Prop. B.2, p.146). It is then continued and joined, with the five radial moments M, I, J, S, C_p matched exactly (Prop. B.8, p.155).

**2. Background stress and the cone (§3.2 pp.9–10; §4.3 pp.30–31; App. A pp.126–144; App. C pp.157–165).**
- R_θ⁽⁰⁾ = −(∂_r + 2/r)T_{rθ} and R_z⁽⁰⁾ = −(∂_r + 1/r)T_{rz}, with the zero total moments ∫r²R_θ⁽⁰⁾ = ∫rR_z⁽⁰⁾ = 0.
- The cone condition (Lemma 4.5) is what allows T = c₁v₁ + c₂v₂ with c_i > 0 for two wave families.
- App. A builds the outer profile and pressure datum and replaces an exterior power by the heat flow (Lemma A.6, p.138).
- App. C inserts a radial oscillation with phase N log X and restores all five moments exactly (Prop. C.2–C.3).

**3. Heat/base correction (§5 pp.45–62; reader L957–2377).**
- The profiles are expanded in powers q^{2nh}, via the coefficient equations (5.2)–(5.6) (verified for n ≤ 2).
- The analytic Volterra system is solved near the axis. The total radial residual integrals are cancelled (Lemma 5.2), then a coefficient induction runs (Prop. 5.3).
- The coefficients are summed divergence-preservingly: Borel-type cutoffs χ(c_n q) on Stokes streamfunctions, with curls taken after (Lemma 5.4).
- Result (Prop. 5.5, p.60): ℛ(u_B, p_B) = −(∂_r + 2/r)𝒯_θ e_θ − (∂_r + 1/r)𝒯_z e_z + ℰ_B, with ℰ_B **flat**: every derivative is O(q^N).

**4. Auxiliary torus and oscillations (§6 pp.62–73; §7 pp.73–88; reader L2378–3296).**
- Dyadic charts Q = 2^{−ℓ}, ε = Q^h.
- Waves live on an extended variable Y ∈ 𝕋², evaluated at a phase map Y(r, t).
- The degree-14 toral endomorphism J (eigenvalues 4 ± √2, with Pell-type Diophantine bounds) separates the supports of overlapping pulses.
- A constrained pulse equation, with the pressure eliminated, makes each pulse grow by shear production and then decay by viscosity.
- The covariance of the two families equals εT₀ (Prop. 7.5, p.82). Velocities are exact curls.
- The energy exchange is (1/2)∂_v|t|² = −g·T − d|t|² ((7.22), p.81; the actual-shear remainder is NS-02).

**5. Mean corrections (§8 pp.88–100; reader L3297–3975).**
- Conservative momentum equations; compactly supported radial primitives with an obstruction projector; pressure reconstruction.
- Three compatibility defects are identified. The fast auxiliary-time derivative is inverted on zero-mean parts. A five-dimensional moment correction is applied.

**6. Correction cycle and summation (§9 pp.100–116; reader L3976–4693, L10945–11645).**
- Increment identity: ℛ(u + δu, p + δp) = ℛ(u, p) + ℒ_u(δu, δp) + ∇·(δu ⊗ δu).
- Each cycle performs four operations (Prop. 9.6, p.107):
  1. harmonic amplitude equations;
  2. signed amplitude increments;
  3. the temporal mean inverse;
  4. the five-equation correction.
- The residual exponent is σ_j = 1/5 + j/10 → ∞.
- Stages are summed with shrinking cutoffs on potentials (Prop. 9.9, p.114). This gives Theorem 3.1 (p.15):
  - local fields on Ω_* = {τ > 0, q < q_*} with u = curl 𝒜 + ℬe_θ;
  - a flat residual (3.4);
  - an exact heat exterior (3.5) with zero residual;
  - growth u_θ(√(2X_in τ), 0, 0, 1−τ) = τ^{−A}(e₀ + O(τ^{2h})) (3.6).

**7. Terminal endpoint and localization (§10 pp.116–126; reader L4694–5356).**
- Cutoffs c = χ_x χ_t multiply the potentials before the curl, preserving incompressibility (Prop. 10.1, p.117). Set f = ℛ(u, p) for t < 1.
- Lemma 10.2 (p.118): every ∂_x^α∂_t^j f converges uniformly as t ↑ 1, to ∂^αF_j with F_j ∈ C_c^∞(𝒦) and ∂^αF_j(0) = 0.
- Lemma 10.3 (p.120): f(x, 1+σ) = Σ_j χ₀(b_jσ)σ^j F_j(x)/j! with rapidly increasing b_j. This is a Borel construction and gives f ∈ C_c^∞(ℝ³ × (0, ∞)) supported in 𝒦 × [0, 2].
- Energy bound: Lemma 10.4. Uniqueness among bounded-energy smooth competitors: Lemma 10.5 (Riesz-transform pressure, localized energy).
- The growth path (10.20)–(10.21) gives the breakdown.

**8. Periodization (Cor. 10.6, p.125).**
- Rescale by λ into Q₀ = (−1/2, 1/2)³, with a time shift t₀ = 1 − λ^{−2} absorbed by the initial zero interval.
- Sum the integer translates. Their supports are disjoint, so the nonlinearity splits.
- Energy/Gronwall gives uniqueness on 𝕋³ (λ³ scaling and t₀ verified).

**What makes the force smooth through t = 1, as the manuscript explains it (src p.3; pp.16, 118–120).**
- **Near the singular point (0, 1):** the cutoffs equal one there, so f is the local residual. That residual is **flat**: |∂^α f| ≤ C_{α,j,N}(τ + |z|^{1/D})^N ((10.9), p.119). Flatness has three sources:
  1. the oscillatory pulses' averaged momentum flux cancels the singular stress divergence of the background;
  2. the infinite correction cycle drives the residual exponent σ_j → ∞;
  3. the shrinking-cutoff summation and the flat base remainder ℰ_B.
- **Away from the origin:** q stays positive, and all derivatives of the potentials and pressure are bounded up to τ = 0 (Thm 3.1(ii)). Where r > 0 and q → 0, the field is the exact heat exterior, smooth up to τ = 0 with zero uncut residual. The cutoff-derivative terms live only in these regions.
- **Extension past t = 1:** the uniform limits F_j are compatible jets. Lemma 10.3 realizes them for t > 1 by a Borel series.
- The **velocity** is not continued past t = 1; only the force is.

---

## 3. Verification results (all mine unless stated; 256 PASS, 0 FAIL)

| Script (output) | What is re-derived | Result |
|---|---|---|
| `check_leading_field.py` | See the item list below the table. | **67/67 PASS** |
| `check_order_n_equations.py` | Builds the full NS residual (with axial viscosity) for generic φ_n, M_n, Π_n, n = 0, 1, 2 (h = 1/100, q = w¹⁰⁰). Extracts each order and compares with (φ), (U), (Π), (Ω) (reader L1050–1065; src (5.2)–(5.6)). | **10/10 PASS** (my first run failed from an extraction bug, fixed) |
| `check_negative_controls.py` | Wrong variants: continuity with 2Aη M; R⁽⁰⁾ with the sign of a flipped; Z_b with q^{b−A}; Kasner inverse with 2P. | **4/4 rejected** |
| `check_actual_shear.py` | See the item list below the table. | **26/26 PASS** |
| `check_cylindrical_forms.py` | MC11 transport (conservative = standard + U_i·div U); cylindrical vector Laplacian; conservative residual identities r²ℛ_θ, rℛ_z (L1330–1334); stress primitives (L1382–1383); R^e(∂_R + e/R)h = ∂_R(R^e h). | **14/14 PASS** |
| `check_axis_numerics.py` | f₀ = J₁(2√t)/√t ≥ 305719/1152000 > 0.265 on t ≤ 2.05 (actual minimum 0.2711); f₀ + zf₀′ = J₀(2√t) ≤ −0.188 on [1.98, 2] (actual maximum −0.1908); −W_* ≥ 2.87; (H_*/d)′ > 0; 𝓗 = Tricomi U. | **14/14 PASS** |
| `check_vacuum_hydrodynamics.py` | See the item list below the table. | **81/81 PASS** |
| `check_bridges_and_scalings.py` | See §4. Also: viscosity map (10.22)/(E.24) on the full triple; parabolic map λ³ and t₀ (Cor. 10.6); 𝒯_ν = 𝒮_{√ν}∘𝒜_ν (E.28); energy factors ν^{5/2}, ν²; ‖f_ν‖₂ = ν^{5/4}‖f‖₂. | **39/39 PASS** |
| `certify_collision.py` | Arb interval certificate of the double zero (above). | **CERTIFIED** |
| `track_hydro_branch.py` | Numerical continuation of the hydrodynamic zero from q = 0.05 to q_c − 10⁻⁶. It arrives at α_c + 7.8·10⁻⁴; the second zero is at α_c − 8.4·10⁻⁴. | numerical |
| `run_workbench_checkers.sh` | The bundle's `replay_checks.py` (9 programs, 144 groups, 12 probes; sympy 1.14 against the pinned 1.13.1); `replay_additional_checks.py` (0 programs); 119/119 member hashes; receipts content-identical; `verify_recovered_formulas.py` passed (residual 5.9·10⁻⁶⁷). | **all pass** |

Items in `check_leading_field.py` (reader L86–355, L981–1175):
- q_t, η_t, X_t, q_z, η_z, X_z from the inverse Jacobian;
- commuting coordinate fields;
- ∂_t(q^b f) = q^{b−1}T_b f and ∂_z(q^b f) = q^{b−D}Z_b f;
- L − 2Dη² = d, A + D = 1, −2A − D = −A − 1;
- continuity (V₀)_X = −Z_{−A}U with V₀ = (2ηXU − 2DηM − dM_η)/L;
- the Cartesian axis formula;
- Π_X = F²;
- the transport identity with W and H_c;
- (∂_t + u·∇)(ru_θ) = −q^{−h−1}HS_q/L, and the axial analogue with S_n;
- (∂_r + k/r)(q^{−A−1/2}G);
- ∂_r u_θ − u_θ/r = −q^{−A−1/2}Fa;
- **R_θ⁽⁰⁾ = −(∂_r + 2/r)(q^{−A−1/2}T_{0,θ}) and R_z⁽⁰⁾ = −(∂_r + 1/r)(q^{−A−1/2}T_{0,z}) in full**;
- the zero-stress equations;
- both five-moment primitive formulas;
- the cone roots, the factorization and the stress coordinates;
- the heat ODE (symbolically, and by quadrature for h = 1/137);
- (∂_rr + r^{−1}∂_r − r^{−2})K;
- the viscous operator identities B1–B3 on rφ(X), U(X), V(X)/r;
- the ξ-forms, K_n, and V_n/X.

Items in `check_actual_shear.py`:
- t^T𝒦t = g·T (src p.81);
- t^TΔ𝒦t = Δg·T;
- (AS26) −g·T = −|g₀|T_N − Δg·T;
- the pressure (AS17) and (AS18);
- 𝒜 − 𝒜₀ = −Π_nΔ𝒦 (AS19);
- the force–pressure bijection (AS20)–(AS22);
- the energy identity (AS25);
- the derivative formula (AS7) up to order 4;
- the jet map and its inverse (AS11)–(AS13);
- (AS34) and (AS38);
- the ambient projection: B^ℓB = I₂ and BB^ℓ = I₃ − K_a n^T/|n_tan|;
- the thresholds (AS28) and (AS36), on 2000 random constant sets.

Items in `check_vacuum_hydrodynamics.py` (continuation):
- the TT lift: trace, divergence, norm (5.4), cross term, and why the mixed block is needed;
- R(φ²δ) = −6φ⁻³Δφ, computed from Christoffels;
- the momentum constraint in n = 4 for a generic tracefree Ā;
- tr_h K = τ_* and |K|²_h = φ⁻⁸q + τ²/4;
- the Hamiltonian → Lichnerowicz reduction (6.4), and κ_* = 12a_*²;
- (6.8), the barrier inequality, and (7.6);
- Kasner (1.2), (1.3), (4.9), surjectivity and range, (4.11);
- H_A (4.4);
- Ric = −4g/L² from a direct 5D computation, modulo Σp = Σp² = 1 (the quadratic constraint is genuinely used);
- the Kretschmann identity and the exact limit (4.13), with 9/2 at rest and 9/64;
- (4.6), (3.4) and (4.14);
- (7.1), (7.2), (6.3);
- (2.4)–(2.6) ⇒ (1.1);
- (7.7) and (7.3a);
- the decoder: the Fourier identity, and the kernel (6.13) numerically;
- slab (S1), (S3), (S5), (S7) and (S8) (two-layer direct solve);
- Rindler (5), (13), (14), the series (27), (28), the collision (29)–(33) by an independent formulation (qI_{α+1} + αI_α = 0), an argument-principle count, and two table rows.

**Not verified here:**
- NS-00 and its analytic estimates (Thm 4.6 existence; Props 5.3, 5.5, 7.2–7.6, 9.6, 9.9; Lemmas 10.2–10.5);
- the Volterra convergence and the contraction constants of App. B;
- the stage-cycle exponent tables beyond re-running the bundle;
- (2.3) of the continuation (the finite-cutoff tensor equation) and the physical evaluations (2.6);
- the Brown–York formulas (20)–(24), the pole-cluster Laurent data (A₋₂, A₋₁), the two-sided probe of IDENTITY §8, and the archived predecessor documents (`archive/*`);
- the H² → H^s bootstrap in the slab theorem;
- the Lichnerowicz existence beyond the barrier and comparison inequalities.

---

## 4. Bridges (every NS link found)

| Edge | Precise statement | Status |
|---|---|---|
| **NS → YM, abelian** (`released_profile_measures_addendum.tex` (250)–(266); `21_` §2) | A_i = λu_iT with T = −iσ₃/2 gives F_ij = λ(∂_iu_j − ∂_ju_i)T, so 𝒦_B = λ²‖curl u‖² and 𝒦_E = λ²c⁻²‖∂_s u‖² (253). The rate bounds (250) ‖curl u_ν(1−τ)‖² ≥ ν^{3/2}C_Ωτ^{−1/2−3h} and ‖∂_s u_ν‖² ≥ ν^{5/2}C_{u̇}τ^{−3/2−3h} are **derived** in `ym_gap_primary_20260908/ns_inner_profile_curvature_current_bridge.md` §4 ((4.2)–(4.8), L186–240) and §5 ((5.1)–(5.7), L≈250–315). The method is circulation on the disks r = √(2X_*q) (Stokes, then Cauchy–Schwarz), integrated over η; the inputs are the source's (5.42) (Prop. 5.5) and Prop. 9.9, Step 5. The zero-quotient diagonal needs g_j → 0; the source itself calls (265) a "weak-coupling counterexample candidate". | map **E✓**; exponent steps **E✓**; the divergence of the curvature masses is **C** (NS-00 via (5.42) and Prop. 9.9); no fixed-coupling or mass-gap content (`21_` 21.4) |
| **NS → YM, non-abelian** (`nonabelian_fluid_profile_addendum.tex` (227)–(246), L41–223) | 𝐀_i = λe_i × u gives B_i^a = λ(∂_a u_i − δ_{ia} div u) + λ²u_iu_a, \|𝐁\|² = λ²\|∇u\|² + λ³∂_a(\|u\|²u_a) + λ⁴\|u\|⁴, tr B = λ²\|u\|², \|𝐄\|² = 2λ²\|u_s\|²/c². The currents (236) and (237) are given in full. At the axis, \|𝐁\|² = 2λ²(a² + b²) + (−2λa + λ²w²)². | all identities **E✓** (generic divergence-free u = curl ψ). The axis growth b(0,0,s) = C⁻¹τ^{−1−h} is **C**. The current j ≠ 0, so this is a sourced field, not a YM solution (the source says so) |
| **NS → ES** (`21_` §1) | the source's torus operator J = [[3,1],[1,5]] (src §6.1): det 14, eigenvalues 4 ± √2, norm forms of ℤ[√2]; aliasing on character groups | operator only (**P**); no fluid theorem used; J identities **E✓** |
| **NS → zeta** (satellites 29g–29s; 29k (nam:cartesian) L134, (nam:pde) L157, (nam:mellin) L265, (nam:arithmetic) L331) | exact angular-momentum balance for L = x₁u₂ − x₂u₁; averaged equation ∂_tB + ∂_σP + ∂_zQ = ν(2σB_σσ + B_zz) + F; Mellin shift equation; Müntz-type trace 𝒜_h a(x) = Σ_n ψ_a(nx) with multiplier W_h(s) = ζ(s)(1 − 2^{s−1})(1 − 2^{h−s}), entire. The residue of B̂ at s = −1 is ∂_σB(0), i.e. the axis vorticity, which grows like τ^{−1−h}. | transforms **E✓** (classical Müntz formula); the growth is **C**; the zeta repository itself says there is no zeta-zero conclusion (zeta `ATTEMPTS.md` L27) |
| **NS ↔ zeta Mellin-abscissa reading** (`21_` Prop. 21.7; `47_` edge 26) | abscissa of 𝒦_B(1 − τ) lies in [1/2 + 3h, 1] | **A** (a reading), **C** on (250) |
| **S⁶ → NS** (zeta `sidebar/fluid/tex/s6_dynamics_bridge.tex` L1–14, (eq:s6dyn-ns-solution) L222) | the S⁶-workbench scalar oscillator (h, R, ω) gives u = ηe^{−νλ²t}(K(t)B₁ + B(t)B₂), with p = −η²d²KBc(x) and f = ησωd(−BB₁ + KB₂). This is an exact forced NS solution on 𝕋³ built from Beltrami modes (curl B_j = λB_j) and is global and smooth. | **E✓**; elementary; only two real numbers cross from the S⁶ side; no blowup |
| **NS → S⁶** | none. The continuation says no S⁶ edge was identified (README L170); `28_` §4 finds no certified NS-side transfer. | — |
| **Jacobian map F → NS kinematics → YM** (`28_` Lemma 28.1; `34_`) | U = DF⁻¹(V∘F) is a polynomial divergence-free field; an integral curve escapes at τ = 1/8 | det DF = −2 and div U = 0 **E✓**. Kinematic only: a steady field, whose "NS" status is just force = residual. Theorem 14.2 is the free two-gluon threshold (`34_`). |
| **NS → Einstein** (the vacuum-hydrodynamics continuation, NS-04) | snapshot encoding; Kasner map; Rindler response; slab comparator | **E✓** as listed. A snapshot map, not a dynamical correspondence: inserting NS time as Einstein time leaves the defect −2cNφ⁻²Ā ≠ 0 (7.7). |
| **"Heat Grams"** (`21_` §3) | a zeta → YM Gram-sandwich lemma | no NS content. The NS "base_heat" component is the source's own heat exterior, not a transfer (`28_` §4). |

**Assessment of "under-used".**
- The NS material that touches the other programmes consists of typed maps. Each map is exact, but none transfers an NS theorem, except through NS-00's growth rates, and then only conditionally.
- None enters YM-01, S⁶, or a zeta-zero statement.
- The genuinely arithmetic object inside the NS construction is the auxiliary torus J and its ℤ[√2] Diophantine bound (reader L2405–2431). The ES programme already uses it.

---

## 5. Closest established mathematics

- **Forced-singularity programme.** Córdoba–Martínez-Zoroa is the closest literature for the strategy of treating the force as the residual and making it regular while the solution blows up:
  - forced 3D Euler with C^{1,1/2−ε} ∩ L² force, arXiv:2309.08495;
  - C^∞(ℝ³∖{0}) ∩ C^{1,α} Euler singularities, arXiv:2308.12197 (Annals of PDE);
  - smooth-source IPM singularities, arXiv:2410.22920;
  - with Zheng, hypodissipative NS with L¹_tC^{1,ε}_x force, arXiv:2407.06776.
  - The source cites these (its refs [6]–[8]) and states the difference: a C_c^∞ force, the true Laplacian, amplification by oscillatory pulses rather than vortex layers.
  - [removed: two further items seen only in search results and not verified.]
- **Unforced blowup.**
  - Elgindi, Annals of Math. 194(3) (2021), arXiv:1904.04795 (C^{1,α} axisymmetric Euler, self-similar);
  - Chen–Hou, arXiv:2210.07191 and 2305.05660 (computer-assisted, Boussinesq and Euler with boundary).
  - These are related only in their anisotropic/self-similar core. The OpenAI flow is forced, and its core balance includes viscosity (Re_r = O(1)).
- **Tao's averaged NS**, JAMS 29 (2016). Blowup for a modified nonlinearity that keeps the energy identity. Contrast: the true nonlinearity, but with a force.
- **Oscillation machinery.** Convex integration and stress realization (Daneri–Székelyhidi, cited by the source); WKB short-wave stability (Lifschitz–Hameiri; Friedlander–Vishik); Craik–Criminale waves; centrifugal instability (Leibovich–Stewartson; Billant–Gallaire).
- **Borel-type extensions.**
  - The force extension (Lemma 10.3) is Borel's lemma with shrinking cutoffs.
  - The trace-quotient chapter's "no continuous linear section" follows because ω = ℝ^ℕ has no continuous norm, while C_c^∞(K) does.
- **Heat exterior.** A self-similar solution of the swirl heat equation, 𝓗(Z) = Z^{−1−h}U(1+h, 2, 1/Z) (Tricomi function; verified).
- **Vacuum hydrodynamics.**
  - Fluid/gravity: Bhattacharyya–Hubeny–Minwalla–Rangamani, JHEP 0802:045 (2008), arXiv:0712.2456.
  - Rindler fluid: Bredberg–Keeler–Lysov–Strominger, "From Navier–Stokes to Einstein", JHEP 07 (2012) 146, arXiv:1101.2451; Compère–McFadden–Skenderis–Taylor, arXiv:1103.3022; Marolf–Rangamani, arXiv:1201.1233.
  - Kasner (1921) and Bianchi I with Λ.
  - The Lichnerowicz–York conformal method in general dimension: Choquet-Bruhat–Isenberg–Pollack (2007).
  - Maximal development: Choquet-Bruhat–Geroch; Sbierski.
  - The decoder is the Biot–Savart/Newton inversion ΔV = 2 div S_V.
  - The continuation's constraint encoding differs from BKLS: it maps snapshots to constraint data and is not an ε-expansion evolution correspondence.
  - The collision and the finite pole-cluster limit are standard complex analysis: coalescing simple poles give a double pole.
- **Hyperdissipation.** J.-L. Lions (1969) proves global regularity for |k|^{2α} with α ≥ 5/4; Tao (2009) extends this log-supercritically. The slab theorem is the case 2α = 3.

---

## 6. Items a careful outside contributor could settle in a few hours

1. **Certify the hydrodynamic-branch identification** of the collision (RESEARCH.md §6; my `certify_collision.py` covers existence and nondegeneracy only).
   - Statement: the zero α(q) of I′_α(q), with α(q) ~ −q²/2 as q → 0, continues analytically and stays real on (0, q*) and reaches the certified double zero.
   - Method: interval Newton on q-cells. Arb is available as python-flint.
2. **Radius of convergence of the hydrodynamic series (27).**
   - Locate all complex branch points F = F_α = 0 with |q²| ≤ q_c² ≈ 0.606 and certify them. The manuscript explicitly leaves open whether a nearer complex singularity exists.
   - Also extend the series to q²⁰ symbolically; the recursion is the checker's.
3. **Derive (2.3), [r(r⁴ − r_h⁴)H′]′ = −3Lr_c√f_c r²** (IDENTITY_AND_COMPLETION.md L71–77), from the linearized Einstein equations of the black brane in the BHMR gauge ((4.16)–(4.20) of 0712.2456) with the finite-cutoff normalization (2.2). Then derive both evaluations (2.6): the ordered shape-operator endpoint and the Brown–York stress. Here only the algebra from (2.3) and (2.6) to (1.1) is verified.
4. **Brown–York response (20)–(24) of RESEARCH.md** from the metric reconstruction (11)–(12). Includes the contact terms and the hydrodynamic limit H = (1 + O(q²))/(−iw + q²/2 + O(q⁴)). The reductions (13)–(14) are verified here.
5. **Leading-profile numerical margins.**
   - Interval-certify every finite constant the profile construction uses. Examples: κ, c_ex = 0.2, the loop gaps, the (PA.3)–(PA.26) choices (reader L5531–5900), and the outer-schedule cone margins (reader L1759–2018; bundle checks "pulse_quadratic_1/2", 58081/80000).
   - The f₀ bounds are already rigorous (alternating series) and are re-checked here.
6. **Exponent bookkeeping of the correction cycle.** Re-derive by hand, from the class rules (reader L2478–2500, L4448–4480, (9.17)–(9.19)), that one cycle gains exactly 1/10 (σ_{j+1} = σ_j + 1/10). This covers the exponent margins that are currently checked only by Fraction arithmetic:
   - 7 named margins with κ = 10⁻⁵ and H = 99999/100000 in `stage_inputs_audit/exponent_checks.json`;
   - 15 exponent inequalities for α ≥ 9/10 in `mean_corrections/exact_checks.json`.
7. **Close the NS→YM rate bound (250) as a lemma conditional on stated source propositions.**
   - Write the exact dependency: (5.42) on a fixed inner rectangle; Prop. 9.9 Step 5; the cutoffs equal to one.
   - Check that the summation cutoffs χ(c_n q) do not spoil (4.2) uniformly in η on |η| ≤ η_*.
   - The elementary part is verified here.
8. **Official PDF comparison for D1.** Compare (10.20) on p.124 of the 166-page PDF (sha256 `0e779481…`) with the transcription. Record the result in the transcription's empty `evidence/errata/ERRATA.jsonl`.
9. **Lichnerowicz existence with explicit constants** (IDENTITY L589–628): Schauder bounds for the monotone iteration (6.9) on balls and the diagonal extraction. This is standard, but the writing is only sketched.

---

## 7. Errors and discrepancies found (no failed identity)

- **D1 (transcription).** `sections/pp121-126.tex` L304–307 and the formula inventory (`NS-F-P124-005`) read x_τ = (\sqrt2X_{in}τ, 0, 0), which renders as √2·X_in·τ.
  - On that path X = X_in²τ → 0, so u_θ grows only like τ^{−h}, and the asymptotic τ^{−A}(e₀ + O(τ^{2h})) of (10.21) would not hold.
  - The same transcription's (3.6) (p.16) and p.116, the reader (L5183, L14193) and zeta 29i all use √(2X_in τ), for which q = τ and X = X_in.
  - Either the transcription slipped or the source has a misprint. The errata ledger (`evidence/errata/ERRATA.jsonl`) is empty. Not checked against the official PDF.
- **D2 (locator).** YM `ATTEMPTS.md` L59 points to `navier_stokes_source_bundle.zip` for the Boussinesq, CKN, rational-cylinder, IPM and moving-centre payloads (NS-05).
  - No member of the 120-member bundle mentions them; the only hits are the source's reference list.
  - The accounts themselves say their public counterparts have not been verified (L51). The material appears to live in zeta `sidebar/fluid/tex/`.
- **D3 (status labelling).** The reader states a "Leading-profile assembly theorem" giving every property of Theorem 4.6 (L5900–5985), while research-state.json L233 lists profile existence as unresolved.
  - This is not a contradiction: the reader's claim is a written, not independently validated, derivation.
  - A reader of the note should treat Theorem 4.6 as **I** (with a workbench reconstruction), not as **E✓**.
- **Update to earlier audits (not an error).**
  - `21_` §2, the YM reader (`y6_side.tex`) and `46_` treat the rate bounds (250) as imported and unchecked. They are derived in the YM repository (see §4), and I verified the derivation's elementary steps.
  - Their status is now "conditional on NS-00 (5.42) and Prop. 9.9".
  - NS-04(c) moves from "not audited" to reductions **E✓**, series **E✓** (numerically), and collision existence certified.
- **Cosmetic.**
  - The shipped receipts are CRLF; regenerated receipts are content-identical.
  - `navier-stokes/README.md` repeats its "What was tried" link line (L23, L25).
- **Mine, corrected.** Early versions of five of my scripts produced false FAILs or crashes. The causes were coefficient extraction, one mistyped test expression, sqrt-of-squares, non-simplifying symbolic powers and Subs objects. Each was traced to my code and fixed; the sources were right in every case (see the outputs).
- **Housekeeping.** [removed: a note on a mistakenly created scratch file outside this folder, since deleted.] Nothing else outside this folder was written.

---

## 8. Files in this folder

- **Scripts and outputs:**
  - `check_leading_field.py`, `check_order_n_equations.py`, `check_negative_controls.py`;
  - `check_actual_shear.py`, `check_cylindrical_forms.py`, `check_axis_numerics.py`;
  - `check_vacuum_hydrodynamics.py`, `check_bridges_and_scalings.py`;
  - `certify_collision.py`, `track_hydro_branch.py`, `run_workbench_checkers.sh`;
  - each with its `*_OUTPUT.txt`.
- **Scratch:** `scratch/` holds my bundle extraction and replay copies (`bundle/`, `bundle_run/`) and a copy of `verify_recovered_formulas.py`.
- **Runtime:** every script runs in under 30 s (2 cores).
