# 51_ Navier–Stokes: the workbench checked, the NS → YM rates are conditional (not unchecked), and the Rindler shear series has radius exactly q*²

Claude (model `claude-opus-5-5`, Opus 5.5 at maximum effort), 27 September 2026. The first-pass inventory was written by a subagent between 11:40 and 12:27 UTC (`51a_`). I re-ran and extended it from 12:59 UTC and wrote this note from 13:50 UTC. From 14:45 UTC I verified the independent referee's findings and applied them (§13).

Checks are in `checks/ns51/`:
- `first_pass/` holds the subagent's scripts and outputs;
- the other files are mine.

Status classes follow `51a_`:
- **I**: imported from OpenAI's manuscript;
- **E✓**: an exact identity re-derived by code;
- **N**: numerical only;
- **C**: conditional on named propositions of the manuscript;
- **A**: a reading;
- **P**: a shared operator without a transferred theorem;
- **E✓(CA)**: an unconditional statement proved with computer assistance (Arb ball arithmetic).
  - Theorems 51.1, 51.2 and Corollary 51.2′ are of this kind. They are statements about the zeros of I′_α(q) in the order α and use no NS-00 input.
  - Reading those zeros as the Rindler shear frequencies uses the continuation's reduction (10)–(12), (15)–(16). The first pass re-derived (13)–(14). (16) follows from (12) at ρ = ρ_c: zero boundary source A_{0c} = A_{zc} = 0 gives φ′(ρ_c) = 0, i.e. kI′_α(kρ_c) = 0.

**What is new in this note.**
1. A computer-assisted proof (Arb ball arithmetic) that the hydrodynamic shear series of the workbench's vacuum-hydrodynamics continuation has radius of convergence exactly q*² in q² (Theorem 51.2).
   - q* is the pole-collision momentum. The continuation leaves open whether a nearer complex singularity limits the series.
   - The same certificate shows that the hydrodynamic mode stays purely damped up to the collision.
   - It also gives the exact coefficient asymptotics a_k ~ −C x*^{−k}k^{−3/2} and the sum of the series on its circle of convergence (Corollary 51.2′).
2. The NS → YM rate bounds (250) change status. `21_` and the YM reader imported them unchecked. They are in fact derived in the YM repository from named propositions of the manuscript. I checked every step (Lemma 51.3), so their status is **conditional**.
3. Conditional corollaries: a Type II classification and L^p lower bounds, including divergence of the critical L³ norm at rate at least τ^{−4h/3}. Each is compared with the classical necessary conditions for blowup (Proposition 51.4).
4. The transcription discrepancy D1 is settled against the official PDF (§7).

**Sources.**
- The YM repository `KokunoYumeto/yang-mills-interacting-workbench` at `fa79faf`, folder `navier-stokes/`, including:
  - the source-faithful transcription of OpenAI's 166-page manuscript (cited "src p.N");
  - the 208-page workbench reader;
  - the continuation `continuations/20260919-vacuum-hydrodynamics/` (cited "RESEARCH.md", "IDENTITY_AND_COMPLETION.md").
- The official PDF: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf. I computed its SHA-256 in the browser today: `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`, 2,959,204 bytes. This equals the hash frozen by the transcription.
- Quotations are under 15 words.

---

## 0. Summary

**NS-00** is OpenAI's Theorem 1.1 (src p.1): for every ν > 0 there are f ∈ C_c^∞(ℝ³ × (0, ∞)), a compact K and smooth (u, p) on ℝ³ × [0, 1) with u(·, 0) = 0, supports in K, sup_t‖u(t)‖₂ < ∞ and lim sup_{t↑1}‖u(t)‖_∞ = ∞. Cor. 10.6 (src p.125) is the periodic version.
- It is **imported (I)** and is not verified here.
- The workbench is a reconstruction and verification reader. Its own ledger lists four items as unfinished (`51a_` §1b).

**Re-verification.**
- All ten first-pass scripts were re-run here. Their outputs agree with the shipped ones line for line, apart from timing lines.
- They comprise 251 identity checks and the 5 conditions of the collision certificate, all passing, plus 4 negative controls, all correctly rejected.
- The workbench's own replay (9 programs, 144 result groups) passes.
- I read `certify_collision.py` line by line; its existence argument is correct (§4.1).

**New theorems (computer-assisted).**
- **Theorem 51.1** (certified collision). I′_α(q) has a nondegenerate double zero in α at (α*, q*):
  - q* = 0.778472800990330076180356446189 ± 10⁻²⁰;
  - α* = −0.569714080972361784438457668663 ± 1.5·10⁻¹⁰.
- **Theorem 51.2** (the radius, exactly). The hydrodynamic root α_h is real, negative (purely damped) and analytic on 0 < q < q*, and analytic for complex |q²| < q*². It has a square-root branch point at q² = q*².
  - Hence the series (27), α_h = −q²/2 − 3q⁴/16 − 29q⁶/192 − …, has radius of convergence exactly q*² = 0.6060199018817300556 ± 5.3·10⁻²⁰ in q². It diverges for |q²| > q*², and by Corollary 51.2′ it converges absolutely on the closed disk |q²| ≤ q*².
  - In physical units, ω(k) = −iνk² − i(3ν³/2c²)k⁴ − i(29ν⁵/6c⁴)k⁶ − … has radius of convergence exactly k* = q*c/(2ν) = 0.389236400495165038… c/ν in k.
  - Its first singularity is the collision, at ω* = −0.2848570405… i c²/ν.
- **Corollary 51.2′** (coefficients and boundary sum). In x = q²/4, α_h = Σa_kx^k with a_k = −C x*^{−k}k^{−3/2}(1 + O(1/k)).
  - C = κ√x*/(2√π), where κ² = 4F_q/(q*F_αα) ∈ [1.7915, 1.8061] is certified; numerically C = 0.14717543 (N).
  - Hence a_k < 0 for all large k, and Σa_kx*^k = α*: the hydrodynamic series summed at k = k* returns the collision frequency ω*.

**Conditional results (C).**
- **Lemma 51.3.** For every ν > 0 and all small τ = 1 − t:
  - ‖curl u_ν(1−τ)‖₂² ≥ ν^{3/2}C_Ωτ^{−1/2−3h};
  - ‖∂_tu_ν(1−τ)‖₂² ≥ ν^{5/2}C_{u̇}τ^{−3/2−3h}.
  - These hold under the manuscript's (5.42), Theorem 4.6, Proposition 9.9 Step 5 and Proposition 10.1.
  - Hence the NS → YM curvature masses satisfy 𝒦_B → ∞ with ∫𝒦_B < ∞, and 𝒦_E → ∞ with ∫𝒦_E = ∞.
- **Proposition 51.4.** Under the same hypotheses:
  - ‖u(1−τ)‖_p^p ≥ c_pτ^{3/2−h−p(1/2+h)} for every p ≥ 1, so ‖u(1−τ)‖_{L³} ≥ cτ^{−4h/3};
  - ‖ω(1−τ)‖_∞ ≥ cτ^{−1−h};
  - τ^{1/2}‖u(1−τ)‖_∞ ≥ cτ^{−h}, so the blowup is of Type II.
  - All of these are consistent with the classical necessary conditions for a singularity, with margins that are positive powers of τ^{−h} (τ^{−3h} for the enstrophy, τ^{−h(1+1/p)} for L^p with p > 3, τ^{−h} for L^∞).
  - For p_h < p < 3 the lower bound also diverges, although these norms are subcritical.

**D1 settled.** The official PDF prints x_τ = (√(2X_inτ), 0, 0) in (10.20). The transcription's `\sqrt2X_{\mathrm{in}}\tau` is a transcription slip; the source is correct.

**Bridges.** §8 gives the updated table. No bridge carries a theorem into YM-01, the S⁶ question or a zeta-zero statement. The NS → YM curvature divergence is now **C**.

**Connections to established fields** (§9, with citations):
- convergence of the hydrodynamic gradient expansion (Grozdanov–Kovtun–Starinets–Tadić);
- pole collisions that end diffusion (Areán–Davison–Goutéraux–Suzuki);
- fluid/gravity and the Rindler fluid (Bhattacharyya–Hubeny–Minwalla–Rangamani; Bredberg–Keeler–Lysov–Strominger; Compère–McFadden–Skenderis–Taylor; Marolf–Rangamani);
- forced singularities (Córdoba–Martínez-Zoroa);
- the classical blowup criteria (Leray; Escauriaza–Seregin–Šverák; Seregin; Chen–Strain–Tsai–Yau; Koch–Nadirashvili–Seregin–Šverák);
- singularity analysis of power series (Flajolet–Odlyzko), for Corollary 51.2′.

---

## 1. What was read and run

| Item | What | Result |
|---|---|---|
| First-pass inventory (`51a_`) | NS-00…NS-06 and the 13 reconstruction components, classified; architecture; bridges; 9 contributable items | read in full; claims re-checked as below |
| `first_pass/*.py` (10 scripts) | leading-field calculus (67), order-n equations (10), actual shear (26), cylindrical forms (14), axis numerics (14), vacuum hydrodynamics (81), bridges and scalings (39), collision certificate (5 conditions), branch tracking (numerical), workbench replay | re-run here (python-flint 0.9.0, sympy 1.14.0, mpmath 1.3.0); outputs identical apart from timing lines |
| YM bridge file `ns_inner_profile_curvature_current_bridge.md` §§1–6 | derivation of the rate bounds (250) | every step re-derived (§5; `ns51_rate_lemmas.py`, 27/27 including 3 negative controls) |
| transcription, src pp.1–6, 55–61, 115–126, 165–166 | Theorem 1.1, (5.41)–(5.43), Prop. 9.9 Step 5, (10.20)–(10.21), Cor. 10.6, bibliography | read |
| official PDF p.124 | (10.20) | viewed in the owner's browser at 250%; hash verified (§7) |
| continuation `RESEARCH.md` §§1–7 | Rindler shear sector: exact Bessel reduction, response, series (27), collision (29)–(33), cluster limit | read; (16), (26), (27) re-derived; (27) extended to 240 exact coefficients; collision and radius certified (§4) |
| literature (§9) | bibliographic data | checked on INSPIRE-HEP, the publishers' pages or arXiv today |

---

## 2. NS-00 and the architecture (for orientation; details in `51a_` §2)

- **Force as residual** (src p.3). For any incompressible (u, p), f := ∂_tu + (u·∇)u − νΔu + ∇p. The work is to make f smooth through t = 1 while ‖u‖_∞ → ∞.
- **Slender core** (src p.4). ℓ_r ≍ τ^{1/2}, ℓ_z ≍ τ^{1/2−h} and |u_θ|, |u_z| ≍ τ^{−1/2−h}, with 0 < h < 1/100. The core energy is ≍ τ^{1/2−3h} and Re_θ ≍ τ^{−h}.
  - Coordinates (src (3.2)): τ = q(1 − η²), z = q^Dη, r² = 2qX, with A = 1/2 + h and D = 1/2 − h.
- **Profiles** (Theorem 4.6, src p.32). The tangential residuals are exact radial divergences of a stress q^{−A−1/2}T₀. T₀ = 0 on the inner region X ≤ X_a, and it is admissible on the annulus. The exterior is an exact heat solution.
- **Base correction** (Prop. 5.5, src p.60). ℛ(u_B, p_B) equals stress divergences plus a flat ℰ_B. The profile estimates (5.42) hold uniformly on [X_lo, X_hi] × [−1, 1] for the summed background, with the Stokes streamfunctions summed before differentiation (src p.60).
- **Waves and corrections** (§§6–9). An auxiliary torus J = [[3, 1], [1, 5]] is used. Pulses realize the stress through their covariance (Prop. 7.5). A four-step cycle raises the residual exponent σ_j = 1/5 + j/10 → ∞. Shrinking-cutoff summation (Prop. 9.9) gives Theorem 3.1.
- **Endpoint** (§10). Potential-first cutoffs (Prop. 10.1) are used. Lemma 10.2 shows the force jets converge; Lemma 10.3 extends them by a Borel series past t = 1. Energy (Lemma 10.4) and uniqueness (Lemma 10.5) follow. The growth path is (10.20)–(10.21), and the viscosity map is (10.22). Periodization is Cor. 10.6.

---

## 3. What the re-run verifies, and what it does not

**Verified identities** (E✓; the list is in `51a_` §3):
- the leading-field calculus, including R⁽⁰⁾ = −(∂_r + k/r)(q^{−A−1/2}T₀) in full;
- the order-n coefficient equations for n ≤ 2, from the full residual;
- the actual-shear correction (AS7)–(AS40) and the ambient projection;
- the vacuum-hydrodynamics identities: TT lift, Lichnerowicz reduction, momentum constraint, Kasner bijection, the Einstein check Ric = −4g/L², and the Kretschmann limit;
- all bridge identities (§8);
- the viscosity, parabolic and periodization maps.

**Not verified** (as in `51a_` §3):
- NS-00 and its analytic estimates: Theorem 4.6 existence; Props 5.3, 5.5, 7.2–7.6, 9.6, 9.9; Lemmas 10.2–10.5;
- the Volterra convergence and the contraction constants of App. B;
- the stage-cycle exponent tables beyond re-running the bundle;
- the continuation's (2.3) and its Brown–York formulas (20)–(24).

---

## 4. The Rindler shear sector: the collision and the exact radius

**Setting** (RESEARCH.md §§2–5, verified in `first_pass/check_vacuum_hydrodynamics.py`).
- The seed is the static Rindler metric ds² = −(ρ/ρ_c)²c²dt² + dρ² + dz² + dy² + dx_⊥² on 0 < ρ ≤ ρ_c, with ρ_c = 2ν/c. The cutoff metric is Minkowski.
- For a shear perturbation ∝ e^{−iωt+ikz}, the linearized vacuum equations reduce to the modified Bessel equation for a dual scalar.
- With q = kρ_c, w = ωρ_c/c and α = −iw, the shear frequencies are the zeros of

  F(α, q) := I′_α(q)   (prime = derivative in the argument).   (16)

**Normalization used below.** Put x = q²/4 and let (1+α)_m be the rising factorial. The series I_α(q) = Σ_m (q/2)^{2m+α}/(m!Γ(m+α+1)) gives

  q I′_α(q) = (q/2)^α Γ(1+α)^{−1} G(α, x),   G(α, x) = Σ_{m≥0} (α + 2m) x^m / (m!(1+α)_m).   (51.1)

- For |α| < 1 the prefactor is finite and nonzero. So G = 0 ⟺ F = 0, and G = G_α = 0 ⟺ F = F_α = 0.
- G(α, 0) = α and G_α(0, 0) = 1. By the implicit function theorem, the hydrodynamic root α_h(x) is the unique analytic root with α_h(0) = 0.
- (51.1) was checked against mpmath's Bessel functions: by me at one point to 37 digits (a session check, not shipped), and by the referee at 60 random points with |α| ≤ 0.95, |x| ≤ 0.2, agreeing to 10⁻⁶⁰ (`referee/ref_G_independent.py`).

### 4.1 Theorem 51.1 (certified collision; `first_pass/certify_collision.py`; status E✓(CA))

**Statement.** There is (α*, q*) with |q* − 0.778472800990330076180356446189| < 10⁻²⁰ and |α* − (−0.569714080972361784438457668663)| < 1.5·10⁻¹⁰ such that F = F_α = 0. At that point F_q ∈ 1.75035806 ± 7.6·10⁻⁹ and F_αα ∈ 5.00 ± 0.0203, both positive.

**Proof (read and re-run by me).** Let I = a₀ ± 1.5·10⁻¹⁰ and J = q₀ ± 10⁻²⁰.
- **(i)** F > 0 on {a₀ ± 1.5·10⁻¹⁰} × J.
- **(ii)** F(a₀, q₀ − 10⁻²⁰) < 0.
- **(iii)** F > 0 on I × {q₀ + 10⁻²⁰}.
- **Existence.** g(q) = min_{α∈I} F(α, q) is continuous, with g(q₀ − 10⁻²⁰) < 0 < g(q₀ + 10⁻²⁰). At a zero q* of g the minimizer α* is interior by (i). Hence F = F_α = 0 there.
- **Derivatives.** F_q = I″_α = (1 + α²/q²)I_α − I′_α/q, by the Bessel equation, and is enclosed directly. F_αα is enclosed by a divided difference plus a Cauchy remainder; the maximum modulus is taken on a circle of radius 0.05.
- **Arithmetic.** All evaluations are Arb balls (python-flint `arb.bessel_i`). ∎
- **Consequence.** Since F_q ≠ 0 and F_αα ≠ 0, the two roots split as a square root in q − q*: they are real for q < q* and form a conjugate pair for q > q* (RESEARCH.md (33)).

### 4.2 Theorem 51.2 (the radius of convergence of the hydrodynamic series, exactly; status E✓(CA))

**Statement** (a theorem about Bessel functions: α_h(q) denotes the zero of α ↦ I′_α(q) that tends to 0 as q → 0).
- **(a)** The hydrodynamic root α_h continues analytically to the open disk |x| < x* = q*²/4. It is real and negative for 0 < x < x*, so the mode is purely damped there.
- **(b)** At x*, α_h(x) → α* as x ↑ x* along the reals. There α_h has a square-root branch point, and it is not analytic at x*.
- **(c)** Consequently the Taylor series of α_h in x, equivalently (27) in q², has radius of convergence exactly x*, equivalently q*² = 0.6060199018817300556 ± 5.3·10⁻²⁰.
- **(d)** For real x slightly above x*, the two roots near α* are complex conjugates: the modes propagate.

**Proof** (`certify_hydro_radius.py`, CERTIFIED in 137 s; output `certify_hydro_radius_OUTPUT.txt`). Every step is a finite ball-arithmetic computation.

- **Rigorous evaluation.** G and G_α are summed to M = 30 terms in Arb. The tails m ≥ 30 are bounded for |α| ≤ 0.95 and |x| ≤ 0.2:
  - |t_m| ≤ b_m := (a + 2m)X^m/(m!∏_{k≤m}(k − a)), and |∂_αt_m| ≤ d_m := X^m/(m!∏(k − a))·(1 + (a + 2m)Σ_{k≤m}1/(k − a));
  - b_{m+1}/b_m ≤ 2X/((m+1)(m+1−a)) ≤ 1/2 and d_{m+1}/d_m ≤ 5X/((m+1)(m+1−a)) ≤ 1/2;
  - so the tails are at most 2b_M and 2d_M. These are added as ball radii.
- **(T) Krawczyk tiling.** The closed disk |x| ≤ R_hi, with R_hi ≥ x* the upper end of the certified box, minus the open square of half-width 3·2⁻¹⁰ about X_c = x* + O(3·10⁻⁸), is covered by 42,650 square cells, adaptively subdivided 3 × 3.
  - For each cell X_i and a square α-box A_i, the Krawczyk operator K_i = c − YG(c, X_i) + (1 − YG_α(A_i, X_i))(A_i − c) lies in int(A_i).
  - **Existence.** A_i is convex and G is analytic in α. By the mean-value integral G(α, x) − G(c, x) = ∫₀¹G_α(c + t(α − c), x)dt·(α − c), whose integral lies in the convex enclosure of G_α(A_i, X_i), the map N_x(α) = α − YG(α, x) sends A_i into K_i ⊂ A_i for every x ∈ X_i. Brouwer's theorem gives a fixed point, which is a zero, since Y ≠ 0.
  - **Uniqueness and simplicity.** Two zeros in A_i, or a zero of G_α in A_i, would put 0 in the convex hull of G_α(A_i, x). Then 1 ∈ 1 − YG_α(A_i, X_i), so K_i would contain c − YG(c, x) + (A_i − c), a translate of A_i; a translate of A_i cannot lie in int(A_i).
  - Hence for every x ∈ X_i there is exactly one zero in A_i. It is simple, lies in K_i and is analytic in x.
  - Cells are enlarged by the factor 1 + 10⁻⁹, so the float rounding of cell centres cannot leave gaps.
  - Coverage holds by construction of the subdivision loop: every wanted cell is certified or subdivided, and there are 0 failures.
  - The referee re-checked coverage, completeness of the neighbour search and all 168,301 pairs in exact integer arithmetic (`referee/ref_cells_audit.py`).
  - The referee also re-verified all 42,650 Krawczyk conditions with a second interval library (`mpmath.iv`, 36 terms, an independently derived tail bound; `referee/ref_krawczyk_independent.py`).
- **(C) Consistency.** On all 168,301 touching pairs, K_i ⊆ A_j or K_j ⊆ A_i. So the two unique zeros agree on the overlaps. The cells containing x = 0 contain α = 0.
  - The zeros therefore form one analytic function on the tiled region: the continuation of α_h.
- **(R) Realness.** The 102 cells meeting the real axis have real centres and real-symmetric α-boxes. Uniqueness then forces the zero to be real for real x.
- **(F) Fold patch.** A_F is the square of half-width 1/4 about a dyadic α₀ ≈ α*. X_F is the square of half-width 2⁻⁸ about X_c. All corners and boundary points are exact binary numbers.
  - (Fa) G ≠ 0 on ∂A_F × X_F, with min |G| ≥ 0.0774.
  - (Fb) The winding number of G(·, X_c) along ∂A_F is 2 (enclosure 2.00000 ± 3·10⁻¹⁰). So for every x ∈ X_F, G(·, x) has exactly two zeros β₁, β₂ in A_F, counted with multiplicity.
  - Their discriminant Δ = (β₁ − β₂)² = 2p₂ − p₁² is analytic on X_F. Here p_k = (2πi)⁻¹∮_{∂A_F} α^k G_α/G dα.
  - (Fc) On the 256 boundary segments of X_F the two zeros lie in disjoint Krawczyk boxes inside A_F. The winding number of Δ along ∂X_F is 1 (enclosure 1.00000 ± 3·10⁻¹¹). So Δ has exactly one zero in X_F, and it is simple.
  - That zero is x*, because Theorem 51.1 places the double zero (α*, x*) inside A_F × X_F.
  - (Fd) All 4,039 tiled cells meeting X_F have K_i ⊆ A_F. So there α_h is one of β₁, β₂.
- **Conclusion (a).**
  - On X_F ∩ {|x| < x*}, a convex set with x* on its boundary, Δ ≠ 0. So β₁ and β₂ are distinct and each is analytic there.
  - The tiled function equals one of them on the connected set (tiled region) ∩ X_F ∩ {|x| < x*}. This set is connected because it contains the part of the square annulus between half-widths 3·2⁻¹⁰ and 2⁻⁸ that lies inside the disk; the hole is interior to X_F, and the circle |x| = x* passes through the centre region, leaving a C-shaped set. So α_h is analytic on {|x| < x*}.
  - Realness on [X_c − 2⁻⁸, x*): at a tiled real point in X_F, α_h is real, so its partner is real too. Δ is real on the real segment, nonzero on [·, x*), and positive at the tiled end. Hence Δ > 0 and both zeros are real up to x*.
  - Negativity: G(0, x) = Σ_m 2m x^m/(m!)² > 0 for x > 0, so α = 0 is never a zero for x > 0. Since α_h is real, continuous and has α_h′(0) = −2, it stays negative on (0, x*). The frequency w = iα_h is then negative imaginary: the mode is purely damped.
  - By-products:
    - (Fc) shows that Δ has exactly one zero in X_F and that it is simple. So the collision is the only branch point of the two roots in A_F × X_F, and it is nondegenerate independently of the F_q, F_αα enclosures of Theorem 51.1.
    - The partner β₂ is certified real, simple and distinct from α_h on [X_c − 2⁻⁸, x*).
- **Conclusion (b), (d).**
  - Near x* the two zeros are (p₁ ± √Δ)/2 with Δ(x*) = 0 simple. As x ↑ x*, α_h → p₁(x*)/2 = α*.
  - If α_h were analytic at x*, then √Δ = ±(2α_h − p₁) would be analytic there. Then Δ would have a zero of even order, a contradiction.
  - For real x > x* near x*, Δ < 0 because the zero is simple and Δ > 0 to its left. So the two zeros are a conjugate pair.
- **Conclusion (c).** A power series at 0 with radius R > x* would agree with α_h on {|x| < x*} and be analytic at x*, contradicting (b). The radius is ≥ x* by (a). ∎

**Negative control** (`certify_hydro_radius_negative_control_OUTPUT.txt`). Asking the same tiling to cover |x| ≤ 0.158 > x* fails on the real axis beyond x* (from x = 0.15451), as it must: there the two zeros are a conjugate pair, which no real-symmetric box can isolate.

### 4.3 Corollary 51.2′ (coefficient asymptotics and the sum on the circle; status E✓(CA), constant C numerical)

**Statement.** Write α_h(x) = Σ_{k≥1} a_k x^k. Then:
- a_k = −C x*^{−k} k^{−3/2}(1 + O(1/k)), with C = κ√x*/(2√π) and κ² = 4F_q/(q*F_αα).
  - From the certified enclosures of Theorem 51.1, κ² ∈ [1.7915, 1.8061] and C ∈ [0.14696, 0.14757].
  - Numerically, with F_αα to 30 digits (RESEARCH.md (32)), κ = 1.3403764770 and C = 0.1471754300.
- In particular a_k < 0 for all sufficiently large k.
- The series converges absolutely on |x| = x*, and Σ_k a_k x*^k = α*.
- Physically, the hydrodynamic dispersion series summed at k = k* equals the collision frequency ω*.

**Proof.**
- **Δ-domain.** The certificate gives more than the open disk.
  - Every closed tiled cell carries a simple zero. By the implicit function theorem and compactness, α_h extends to an open neighbourhood of the tiled region.
  - The fold square X_F is a full neighbourhood of x*, and on it the two zeros are (p₁ ± √Δ)/2 with Δ ≠ 0 off x*.
  - Hence α_h is analytic and single-valued on a slit disk {|x| < x* + ε} ∖ [x*, x* + ε) for some ε > 0. On X_F with the slit removed, the continuations from above and below the slit agree with the tiled function on the respective sides.
  - This slit disk contains a Δ-domain at x*.
- **Local expansion.** Near x*, α_h = (p₁ + √Δ)/2 with p₁ and Δ analytic and Δ(x*) = 0 simple. The quadratic model of F at the fold gives Δ = 4κ²(x* − x)(1 + O(x* − x)).
  - Hence α_h = α* + κ√x*(1 − x/x*)^{1/2} + c₁(x* − x) + c₂(x* − x)^{3/2} + ….
  - κ > 0, because the hydrodynamic zero is the upper of the two real zeros on [X_c − 2⁻⁸, x*). This is certified in `ns51_sign_check.py`:
    - a chain of 400 real Krawczyk cells continues α_h from α = 0 at x = 0 to x₀ = X_c − 2⁻⁸, where it lies in [−0.526, −0.474];
    - the two fold zeros at x₀ are enclosed in −0.484383876487 ± 1.2·10⁻¹³ and −0.651760880396 ± 4·10⁻¹³;
    - the chain's enclosure meets only the upper one;
    - the two zeros stay distinct up to x*.
- **Transfer.** By the transfer theorem of singularity analysis (Flajolet–Odlyzko, SIAM J. Discrete Math. 3 (1990) 216–240), [z^k](1 − z)^{1/2} = −k^{−3/2}/(2√π)·(1 + O(1/k)).
  - The analytic term c₁(x* − x) contributes nothing for k ≥ 2, and (x* − x)^{3/2} contributes O(k^{−5/2}).
  - This gives the asymptotics. Absolute convergence on |x| = x* follows from a_k x*^k = O(k^{−3/2}).
- **Boundary sum.** Abel's theorem and α_h(x) → α* as x ↑ x* give Σa_kx*^k = α*. ∎

**Checks (N).** From the referee's 320 coefficients (`referee/ref_series_darboux.py`):
- a_k x*^k k^{3/2} → −0.147175429969 by Richardson extrapolation, which equals −C to 12 digits;
- S₃₂₀ plus the Darboux tail equals α* to 1.6·10⁻¹¹;
- the fold-patch discriminant has Δ′(x*) = −7.186436 = −4κ² (`referee/ref_fold_patch_independent.py`).

**Numerical corroboration (N)** (`hydro_series.py`, `hydro_series_OUTPUT.txt`).
- The 240 Taylor coefficients a_k of α_h(x) = Σa_kx^k were computed exactly as rationals, and G(α_h(x), x) = O(x²⁴¹) was checked exactly. They are:
  - a₁ = −2, a₂ = −3, a₃ = −29/3, a₄ = −2843/72, a₅ = −392029/2160;
  - these reproduce (27) in q² = 4x, including the fifth coefficient, which the continuation "retained from the same symbolic recursion";
  - a₆ = −14509367/16200 and a₇ = −63074754607/13608000.
- All 240 are negative; the referee extended this to 320.
- The Darboux-corrected ratios (a_k/a_{k+1})/(1 + 3/(2k)) approach x* = 0.1515049754…: 0.15158 at k = 40, 0.151517 at k = 100 and 0.1515080 at k = 200, with O(1/k²) convergence. This is as the square-root singularity of Theorem 51.2 predicts.

**Partner branch (N)** (`track_partner.py`). The root that collides with α_h, followed backwards in α from α* (q is a smooth function of α near the fold because F_q ≠ 0), reaches q → 0 as α → −1 with x ≈ 1 + α.
- So it is the first non-hydrodynamic mode. At k = 0 it sits at w = −i, i.e. ω = −ic/ρ_c.
- As q → 0, the zeros of α ↦ I′_α(q) tend to the zeros of 1/Γ(α), namely α = 0, −1, −2, …
  - The reason: 2(q/2)^{1−α}I′_α(q) = Σ_m (2m + α)(q/2)^{2m}/(m!Γ(m + α + 1)) → α/Γ(α + 1) = 1/Γ(α), locally uniformly in α, and Hurwitz's theorem applies.
  - At q = 0 itself the boundary problem degenerates, so the statement is a limit.
  - So the non-hydrodynamic frequencies tend to ω_n = −inc/ρ_c as k → 0.
  - The referee found numerically (α + n)/q^{2n} → (−1)^{n+1}n/((n!)²4ⁿ) for n = 1, 2, 3 (`referee/ref_physics_and_continuation.py`).
- The cutoff observer's Unruh temperature is T = ħc/(2πk_Bρ_c). This follows from the proper acceleration c²/ρ_c and the redshift factor 1 at ρ = ρ_c. So ω_n = −2πinT (units ħ = k_B = 1).

**The k⁴ coefficient against the literature.** Compère–McFadden–Skenderis–Taylor (JHEP 07 (2011) 050, arXiv:1103.3022, eq. (6.3)) write the corrected Rindler Navier–Stokes equation. I read (6.3) through a text extraction of the arXiv PDF and use only its linear terms; RESEARCH.md §5 makes the same identification, and the referee could check only the unit conversion. Its linear part is ∂_τv − r_c∂²v = −(3r_c²/2)∂⁴v in their time τ, with induced metric −r_c dτ² + dx².
- In proper time t = √r_c τ and velocity v/√r_c this becomes ∂_tv − √r_c∂²v = −(3/2)r_c^{3/2}∂⁴v. So ν = √r_c and ω = −iνk² − i(3/2)ν³k⁴ (c = 1).
- This equals the second coefficient of (28). The k⁶ coefficient 29ν⁵/(6c⁴) and all higher ones come only from the exact condition (16).

**Reading (A) and comparisons.**
- **Normalization.** Let T be the Unruh temperature of the cutoff observer, so 2πT = c/ρ_c (units ħ = k_B = 1).
  - Then (w, q) = (ω, ck)/(2πT): exactly the dimensionless (𝔴, 𝔮) used by Grozdanov–Kovtun–Starinets–Tadić.
  - The collision is a critical point of the spectral curve F(α, q) = 0 at real 𝔮*² = 0.6060199 and imaginary 𝔴* = −0.5697141i.
  - Theorem 51.2 is the flat-cutoff instance of their statement that the radius is set by the nearest critical point on the hydrodynamic sheet. Here that critical point lies at real momentum.
- **The shear viscosity ratio.** ρ_c = 2ν/c gives ν = c²/(4πT). With η = ν(ε + p)/c² and ε + p = Ts at zero chemical potential, η/s = νT/c² = 1/(4π) in units ħ = k_B = 1.
- **Pole collisions.** Areán–Davison–Goutéraux–Suzuki characterize the breakdown of diffusion near AdS₂ critical points by a collision of the diffusive pole with a pole associated to the AdS₂ region (their abstract). The same kind of event bounds the series here. I did not check whether their collisions occur at real momentum.
  - At the collision here, |ω*|/(νk*²) = |α*|/(q*²/2) = 1.8802: at the radius, the leading diffusive law is off by a factor 1.88.
- **Two-pole model.** A telegraph-equation model calibrated to the exact k → 0 data is w² + iw − q²/2 = 0, i.e. α² + α + 2x = 0.
  - Its calibration is the diffusion constant (α ≈ −q²/2) and the first non-hydrodynamic mode (α → −1).
  - It collides at x = 1/8 (q² = 1/2) and α = −1/2, with hydrodynamic branch −2x − 4x² − 16x³ − ….
  - The exact problem moves the collision to (q*², α*) = (0.6060, −0.5697), with branch −2x − 3x² − (29/3)x³ − …. This is a computation, not a derivation of the exact result.
- **Prior statements.** I did not find the Rindler radius stated in any of:
  - Bredberg–Keeler–Lysov–Strominger 2011;
  - Compère–McFadden–Skenderis–Taylor 2011;
  - Marolf–Rangamani 2012, who give the vector master equation (2.14), matching RESEARCH.md (13);
  - Grozdanov–Kovtun–Starinets–Tadić 2019 (both papers);
  - Withers 2018;
  - Heller–Serantes–Spaliński–Svensson–Withers 2021.
  - That check was made through their abstracts and text excerpts; the search was not exhaustive.

---

## 5. Lemma 51.3: the NS → YM rate bounds are conditional, not unchecked

`21_` §2 imported the bounds (250) of `released_profile_measures_addendum.tex` without checking them, and the YM reader followed it (`y6_side.tex`, `y7_negative.tex`, `y8_overlaps.tex`: "imported rate bounds … which were not checked"). They are derived in the YM repository's `yang-mills/sources/ym_gap_primary_20260908/ns_inner_profile_curvature_current_bridge.md` §§4–5. I re-derived each step.

**Hypotheses** (all from the manuscript; status I):
- **(H1)** Theorem 4.6(i) (src p.33). E = √(2X)F > 0 for X > 0 and every η ∈ [−1, 1], with F = φ/𝖢 smooth on [0, R] × [−1, 1]. In particular E₀ > 0 on the inner region, and E₀(X, η) = O(√X) at the axis.
- **(H2)** Proposition 5.5, (5.42) (src p.60). For every composition 𝒟^I of q∂_q, ∂_X, ∂_η, 𝒟^I(q^Au_{θ,B} − E₀) = O(q^{2h}) uniformly on [X_lo, X_hi] × [−1, 1].
  - The source fixes radial endpoints 0 < X_lo < X_a < X_b < X_hi and lets the constants depend on them. I read this as holding for each such choice; the bridge file reads it the same way.
  - This holds for the summed background, with the Stokes streamfunctions summed before differentiation.
  - So the summation cutoffs are already included. This settles item 7 of `51a_` §6.
- **(H3)** All annular corrections vanish on the fixed inner similarity region X ∈ (0, X_a), for every η.
  - Step 5 of Proposition 9.9 (src p.116) says this only at the chosen point X_in.
  - The region-wide statement is the sentence after (10.21) on src p.124, where the corrections vanish in the fixed inner region and the summation cutoffs remain in the estimate.
  - It is also carried by the support statements: the stress is zero for X ≤ X_a in Theorem 4.6(ii).
- **(H4)** Proposition 10.1. The cutoffs equal one on a neighbourhood of the singular point.

**Statement.** Under (H1)–(H4), for every ν > 0 there are C_Ω, C_{u̇} > 0 such that for all small τ:
- ‖curl u_ν(1−τ)‖₂² ≥ ν^{3/2}C_Ωτ^{−1/2−3h};
- ‖∂_tu_ν(1−τ)‖₂² ≥ ν^{5/2}C_{u̇}τ^{−3/2−3h}.

Hence, for the abelian image A_i = λu_{ν,i}T:
- 𝒦_B(1−τ) = λ²‖curl u_ν‖² → ∞, while ∫₀¹𝒦_B ≤ λ²𝓕_ν(1)²/(2ν) < ∞;
- 𝒦_E(1−τ) = λ²c^{−2}‖∂_tu_ν‖² → ∞, and ∫₀¹𝒦_E = ∞.

**Proof (checked; `ns51_rate_lemmas.py`).**
- Let X_* ∈ (X_lo, X_a) with e₀ = E₀(X_*, 0) > 0, and choose η_* with E₀(X_*, η) ≥ e₀/2 for |η| ≤ η_*. By (H2)–(H4), u_θ ≥ (e₀/4)q^{−A} on the circles r = √(2X_*q), |η| ≤ η_*, for small τ.
- Stokes gives ∫_{D_z}ω₃ = 2πr u_θ. Cauchy–Schwarz on the disk gives ∫_{D_z}ω₃² ≥ (2πru_θ)²/(πr²) = 4πu_θ².
- At fixed τ, dz/dη = τ^D(1 − 2hη²)(1 − η²)^{−D−1}. Integrating over |η| ≤ η_* gives the enstrophy bound with exponent D − 2A = −1/2 − 3h.
- For ∂_t: at a fixed point, q_t = −1/L, η_t = Dη/(qL) and X_t = X/(qL) with L = 1 − 2hη². So ∂_tu_θ = q^{−A−1}(𝓗 + O(q^{2h})) with 𝓗 = (AE + XE_X + DηE_η)/L.
  - 𝓗(·, 0) ≢ 0 on (0, X_a). Otherwise X^AE(X, 0) would be constant, E = CX^{−A}, and (H1) would force C = 0.
  - More directly, E = √(2X)F gives 𝓗(X, 0) = (1 + h)E(X, 0) + O(X^{3/2}) > 0 for small X > 0 (referee's simplification).
  - Integrate over a rectangle where |𝓗| ≥ h_* > 0, using the volume element dx = qτ^DL(1 − η²)^{−D−1}dX dθ dη. This gives exponent D − 2A − 1 = −3/2 − 3h.
- The energy inequality ‖u‖² + 2ν∫‖∇u‖² ≤ 𝓕_ν(t)² and ‖curl u‖ = ‖∇u‖ for divergence-free, compactly supported fields give ∫𝒦_B < ∞.
- The viscosity map (10.22) gives the factors ν^{3/2} and ν^{5/2}. ∎

**Status change.** `21_` §2 and the YM reader (y6–y8) treat (250) as imported and unchecked. The correct status is **C**: conditional on (H1)–(H4), with the elementary derivation checked. Nothing in the YM-01 status changes: the map is a sourced, reducible SU(2) connection along couplings that must tend to 0 (`21_` 21.4).

---

## 6. Proposition 51.4: Type II blowup, L^p and critical-norm growth (conditional)

**Statement.** Under (H1)–(H4), for small τ:
1. ‖u(1−τ)‖_p^p ≥ c_pτ^{3/2−h−p(1/2+h)} for every 1 ≤ p < ∞. The exponent is negative exactly for p > p_h = (3 − 2h)/(1 + 2h), and p_h < 3.
   - In particular ‖u(1−τ)‖_{L³} ≥ cτ^{−4h/3} → ∞, and for p = 2 the core contribution decays like τ^{1/2−3h} (src p.4).
2. ‖ω(1−τ)‖_∞ ≥ cτ^{−1−h}.
3. τ^{1/2}‖u(1−τ)‖_∞ ≥ cτ^{−h} → ∞: the blowup is not of Type I (|u| ≤ C(T − t)^{−1/2}), so it is of Type II.
4. For p_h < p < 3 the lower bound in (1) diverges, although these L^p norms are subcritical. For p = 2 the norm stays bounded by the energy inequality.

Statement (2) bounds a disk mean at radius √(2X_*q), away from the axis, where (5.42) is not available. It therefore needs no axis information.

**Proof.**
- (1) Integrate |u_θ|^p ≥ (e/4)^pq^{−pA} over a rectangle as in §5. The τ-exponent is 1 + D − pA. For p = 3 the η-factor is L(1 − η²)^{−1+4h}, which is integrable on compact η-sets.
- (2) The mean of ω₃ on the disk D_z is 2u_θ/r ≥ √2(e₀/4)X_*^{−1/2}q^{−1−h}, and the maximum dominates the mean.
- (3) Use (10.21) with q = τ.
- All exponent algebra is checked in `ns51_rate_lemmas.py`. ∎

**Comparison with the classical necessary conditions.** Each is satisfied. The margins are the stated powers; they are lower bounds only, since no matching upper bounds are established here.
- **Leray** (Acta Math. 63 (1934) 193–248; src ref. [16]). A singular time forces ‖∇u(t)‖₂² ≳ (T − t)^{−1/2}, and ‖u(t)‖_p ≳ (T − t)^{−(p−3)/(2p)} for p > 3. Robinson–Sadowski–Silva (J. Math. Phys. 53 (2012) 115618) discuss these lower bounds.
  - The enstrophy exponent here is 1/2 + 3h, a margin of τ^{−3h}; ∫τ^{−1/2−3h} < ∞ ⟺ h < 1/6, as the finite dissipation requires.
  - For p > 3 the margin is τ^{−h(1+1/p)}; as p → ∞ this becomes statement (3).
- **L³ criterion.**
  - Escauriaza–Seregin–Šverák (Russ. Math. Surveys 58 (2003) 211–250; src ref. [11]) prove regularity under bounded L_t^∞L_x³ for the unforced Cauchy problem.
  - Seregin (Comm. Math. Phys. (2012), DOI 10.1007/s00220-011-1391-x; arXiv:1104.3615) shows that ‖u(t)‖_{L³} → ∞ at a potential blowup time.
  - Here ‖u‖₃ ≳ τ^{−4h/3} diverges. These criteria require divergence, not a rate.
  - I did not check whether they extend verbatim to smooth compactly supported forcing, so this is a consistency statement, not an implication.
- **Axisymmetric Type I exclusion.**
  - Chen–Strain–Tsai–Yau (IMRN 2008, rnn016; Comm. PDE 34 (2009) 203–232) and Koch–Nadirashvili–Seregin–Šverák (Acta Math. 203 (2009) 83–105) exclude Type I blowup for axisymmetric unforced solutions.
  - The OpenAI core is axisymmetric only on the inner region (H3), and the equation is forced. So those theorems do not apply as stated.
  - (3) shows that the construction escapes Type I by at least the factor τ^{−h}, which is the angular Reynolds number Re_θ of src p.4.
  - Whether a construction of this kind could work with h = 0 is not addressed here; the source needs h > 0 for its own steps.
- **L²_tL^∞_x and ∫‖ω‖_∞.** ∫‖u‖_∞² ≳ ∫τ^{−1−2h} = ∞ and ∫‖ω‖_∞ ≳ ∫τ^{−1−h} = ∞, with margins τ^{−2h} and τ^{−h} against the scaling rates.
  - These two divergences hold for every singular solution (Leray's ‖u(t)‖_∞ ≳ (T − t)^{−1/2}; Beale–Kato–Majda-type criteria), so they add nothing beyond (3). Only the exponent arithmetic is claimed.

---

## 7. Discrepancies

- **D1 (resolved: transcription slip, not a source misprint).**
  - The transcription (`sections/pp121-126.tex` L304–307, inventory `NS-F-P124-005`) reads `x_\tau=(\sqrt2X_{\mathrm{in}}\tau,0,0)`, which renders as √2·X_inτ.
  - The official PDF was hash-checked in the browser (SHA-256 `0e779481…ae228f`, 2,959,204 bytes) and viewed at 250% on p.124. It prints x_τ = (√(2X_inτ), 0, 0), with the radical over 2X_inτ (image `checks/ns51/D1_official_pdf_p124_eq10_20.png`, a one-line crop).
  - On the transcribed path X = X_in²τ → 0 and u_θ would grow only like τ^{−h}. On the printed path q = τ and X = X_in, and (10.21) follows from (3.6).
  - The transcription's errata ledger (`evidence/errata/ERRATA.jsonl`) is empty. This is the first erratum for it.
- **D2 (locator).** YM `ATTEMPTS.md` L59 points to the source bundle for the NS-05 payloads (Boussinesq, CKN, IPM, moving centre). No bundle member contains them; the material appears to be in zeta `sidebar/fluid/tex/`. Unchanged.
- **D3 (status labelling).**
  - The reader's "Leading-profile assembly theorem" (L5900–5985) states all of Theorem 4.6, while `research-state.json` L233 lists profile existence as unresolved.
  - The reader's derivation is written but not independently validated. So Theorem 4.6 is **I** here. Unchanged.

---

## 8. Bridges (status after this note)

| Edge | Statement | Status |
|---|---|---|
| NS → YM, abelian (`released_profile_measures_addendum.tex` (250)–(266); `21_` §2) | A_i = λu_iT; 𝒦_B = λ²‖curl u‖², 𝒦_E = λ²c⁻²‖∂_su‖²; curvature masses diverge as in Lemma 51.3 | map **E✓**; divergence **C** (was "imported, unchecked"); the zero-quotient diagonal needs g_j → 0; no fixed-coupling or mass-gap content |
| NS → YM, non-abelian (`nonabelian_fluid_profile_addendum.tex` (227)–(246)) | 𝐀_i = λe_i × u; B_i^a, \|𝐁\|², tr B, \|𝐄\|², currents (236)–(237) | identities **E✓** for generic divergence-free u. The exact axis identity b(0,0,s) = C⁻¹τ^{−1−h} of (243) is taken from the workbench's own axis continuation (`axis_continuation_body.tex`), not from (H1)–(H4), since (5.42) does not reach the axis; (H1)–(H4) give the off-axis disk-mean bound sup\|ω\| ≥ cτ^{−1−h} of Proposition 51.4(2). The current is nonzero, so this is a sourced field, not a YM solution |
| NS → ES | the torus operator J = [[3, 1], [1, 5]], det 14, eigenvalues 4 ± √2 | **P** (`21_` §1) |
| NS → zeta (satellites 29g–29s) | angular-momentum balance; Mellin shift; Müntz multiplier W_h(s) = ζ(s)(1 − 2^{s−1})(1 − 2^{h−s}) | transforms **E✓**; growth **C**; no zeta-zero conclusion |
| NS ↔ zeta, Mellin-abscissa reading (`21_` Prop. 21.7) | the abscissa of 𝒦_B(1 − τ) lies in [1/2 + 3h, 1] | **A**, now **C** on Lemma 51.3 rather than unchecked |
| S⁶ → NS (zeta `sidebar/fluid/tex/s6_dynamics_bridge.tex`) | a Beltrami-mode forced solution on 𝕋³ from the S⁶ oscillator | **E✓**; global and smooth; no blowup |
| NS → S⁶ | none | — |
| Jacobian F → NS kinematics → YM (`28_`, `34_`) | U = DF⁻¹(V∘F), a polynomial divergence-free field; escape at τ = 1/8 | det DF = −2 and div U = 0 **E✓**; kinematic only |
| NS → Einstein (NS-04) | snapshot encoding; Kasner map; Rindler response; slab comparator | **E✓** as listed in `51a_`; the collision is now certified (Thm 51.1), and the hydrodynamic series has its exact radius (Thm 51.2) |

---

## 9. Connections to established mathematics and physics

| Field | Connection | Reference (checked today) |
|---|---|---|
| Convergence of the hydrodynamic gradient expansion | Theorem 51.2 is the flat-cutoff instance of "the radius is set by a critical point of the spectral curve"; in their variables the critical point is (𝔮*², 𝔴*) = (0.6060199, −0.5697141i) | Grozdanov, Kovtun, Starinets, Tadić, *Convergence of the gradient expansion in hydrodynamics*, PRL 122 (2019) 251601, arXiv:1904.01018, and *The complex life of hydrodynamic modes*, JHEP 11 (2019) 097, arXiv:1904.12862; Withers, *Short-lived modes from hydrodynamic dispersion relations*, JHEP 06 (2018) 059, arXiv:1803.08058; Heller, Serantes, Spaliński, Svensson, Withers, *Hydrodynamic gradient expansion in linear response theory*, PRD 104 (2021) 066002, arXiv:2007.05524 |
| Breakdown of diffusion by pole collision | the breakdown is characterized by a collision of the diffusive pole with a non-hydrodynamic pole; here that collision is on the imaginary frequency axis at real momentum | Areán, Davison, Goutéraux, Suzuki, *Hydrodynamic diffusion and its breakdown near AdS₂ quantum critical points*, PRX 11 (2021) 031024, arXiv:2011.12301 |
| Fluid/gravity | the continuation's cutoff Rindler fluid | Bhattacharyya, Hubeny, Minwalla, Rangamani, JHEP 02 (2008) 045, arXiv:0712.2456; Bredberg, Keeler, Lysov, Strominger, JHEP 03 (2011) 141, arXiv:1006.1902, and JHEP 07 (2012) 146, arXiv:1101.2451; Compère, McFadden, Skenderis, Taylor, JHEP 07 (2011) 050, arXiv:1103.3022 (the k⁴ coefficient, §4); Marolf, Rangamani, JHEP 04 (2012) 035, arXiv:1201.1233 (vector master equation (2.14)) |
| Forced singularities | the manuscript's strategy of force as residual with controlled regularity | Córdoba, Martínez-Zoroa, arXiv:2309.08495 and arXiv:2410.22920; Córdoba, Martínez-Zoroa, Zheng, ARMA 250 (2026) 38 (src refs [6]–[8]) |
| Blowup criteria | Proposition 51.4: Type II, L³ and L^p growth, Leray rates | Leray 1934; Escauriaza, Seregin, Šverák 2003; Seregin, CMP 2012 (arXiv:1104.3615); Chen, Strain, Tsai, Yau, IMRN 2008 and Comm. PDE 34 (2009) 203–232; Koch, Nadirashvili, Seregin, Šverák, Acta Math. 203 (2009) 83–105; Robinson, Sadowski, Silva, J. Math. Phys. 53 (2012) 115618 |
| Singularity analysis | Corollary 51.2′: the square-root branch point at x* gives a_k ~ −Cx*^{−k}k^{−3/2} | Flajolet, Odlyzko, *Singularity analysis of generating functions*, SIAM J. Discrete Math. 3 (1990) 216–240 |
| Borel extension | Lemma 10.3 is Borel's lemma with shrinking cutoffs; the trace onto force jets has no continuous linear section, because ℝ^ℕ has no continuous norm | standard (`51a_` §5) |
| Heat exterior | 𝓗(Z) = Z^{−1−h}U(1+h, 2, 1/Z), a Tricomi function | verified (`first_pass/check_axis_numerics.py`) |

---

## 10. The contributable items of `51a_` §6

| # | Item | Status |
|---|---|---|
| 1 | certify the hydrodynamic-branch identification | **done**: Theorem 51.2(a)–(b); the tiling and fold patch identify α_h with the colliding real root |
| 2 | radius of convergence of (27) | **done**: exactly q*² (Theorem 51.2(c)); coefficient asymptotics and boundary sum (Corollary 51.2′); 240 exact coefficients |
| 3 | derive (2.3) of IDENTITY_AND_COMPLETION.md from the BHMR linearization | open |
| 4 | Brown–York response (20)–(24) | open |
| 5 | interval-certify the profile constants | open |
| 6 | exponent bookkeeping of the correction cycle by hand | open |
| 7 | NS → YM rate bound as a conditional lemma | **done**: Lemma 51.3; (5.42) already includes the summation cutoffs |
| 8 | D1 against the official PDF | **done** (§7) |
| 9 | Lichnerowicz existence with explicit constants | open |

---

## 11. Register rows (added to `00_RESULTS_REGISTER.md`)

- **S90.** The hydrodynamic shear series of the flat (Rindler) cutoff has radius exactly q*² in q², and its coefficients satisfy a_k ~ −Cx*^{−k}k^{−3/2} with boundary sum α* (Theorem 51.2, Corollary 51.2′; unconditional, computer-assisted).
- **S91.** The collision certificate (Theorem 51.1).
- **S92.** The NS rates and Type II classification are conditional on (H1)–(H4) (Lemma 51.3, Proposition 51.4).
- **Negative 79.** The NS → YM curvature divergence is conditional on four named source propositions, not unchecked, and still yields no fixed-coupling statement.
- **Status update.** On the rate bounds, `21_` §2 and the YM reader's y6–y8 wording are superseded by Lemma 51.3; the reader's next version should say "conditional on (H1)–(H4)". Register entry 42 (scope: couplings → 0) is unchanged.

---

## 12. Not checked

- The manuscript's analytic proof (NS-00). This includes whether the hypotheses (H1)–(H4) hold as stated.
- The continuation's physics inputs:
  - (2.3), the Brown–York formulas (20)–(24), the Laurent data (38)–(41) and the two-sided probe;
  - the slab theorem's H² → H^s bootstrap;
  - Lichnerowicz existence beyond the barrier inequalities.
- Whether the partner branch stays real and simple on all of 0 < q < q* is numerical (N), except on [X_c − 2⁻⁸, x*), where it is certified (§4.2). The same tiling, applied to a normalization regular at α = −1 such as (1 + α)G or F itself, would certify the rest.
- The text of Compère–McFadden–Skenderis–Taylor (6.3) beyond its linear terms.
- The literature search for prior statements of Theorem 51.2 was not exhaustive.

## 13. Referee pass

An independent referee (a subagent, 13:52–14:43 UTC) examined the note in both directions; report and scripts in `checks/ns51/referee/`.
- **Verdict.** No MAJOR findings.
- **Independent re-verification of the certificate:**
  - all 42,650 Krawczyk conditions, with a second interval library (`mpmath.iv`), 36 terms and an independently derived tail bound;
  - coverage, neighbour completeness and all 168,301 consistency pairs, in exact integer arithmetic;
  - the fold patch, with twice the discretization;
  - 320 coefficients by Arb power-series Newton.
- **Applied (each verified by me before editing).**
  - MINOR:
    - the provenance of the (51.1) check (item 2);
    - the Krawczyk chain written out (item 3);
    - connectedness and negativity added to Theorem 51.2 (item 8);
    - "converges exactly for |q²| < q*²" replaced by "radius exactly q*²", with convergence on the circle (item 9);
    - the CMST provenance (item 12);
    - the q → 0 limit wording (item 13);
    - (H1)–(H3) citations: Theorem 4.6(i) p.33, and p.124 for the region-wide vanishing (item 14);
    - the Proposition 51.4 margins, "at least", the automatic divergences, and the speculative h > 0 reading replaced by a neutral sentence (item 17);
    - the non-abelian axis identity attributed to its actual source (item 18);
    - citations added: CSTY II pages, Seregin 2012, GKST JHEP 2019, Flajolet–Odlyzko; the ADGS wording softened (item 20).
  - UNDERSTATEMENT:
    - Corollary 51.2′, with Δ-domain analyticity, Darboux asymptotics and the boundary sum (item 21). The sign κ > 0 is certified separately in `ns51_sign_check.py`.
    - Uniqueness and nondegeneracy of the collision from (Fc) (item 22).
    - The partner certified real near x* (item 23).
    - The status label E✓(CA) (item 24).
    - The GKST normalization and η/s = 1/4π (item 25).
    - The two-pole model (item 26).
    - The L^p margins for p > 3, subcritical L^p divergence and the off-axis disk mean (item 27).
- **Not applied.**
  - Item 25's comparison with a specific ADGS relation D = ω_eq/k_eq² (not verified from their text). Only the neutral number |ω*|/(νk*²) = 1.8802 is kept.
  - Item 20's suggested Davison–Goutéraux 2015 example (not checked).
  - Item 22's sharpening of α* (not needed).
- **Size.** The referee's 14 MB cell dump is not shipped; `certify_hydro_radius_rerun_dump.py` regenerates it.
