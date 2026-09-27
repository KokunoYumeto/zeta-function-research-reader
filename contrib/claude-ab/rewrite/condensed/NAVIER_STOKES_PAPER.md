# The Navier–Stokes workbench: the exact radius of the Rindler shear series, and curvature rates for the NS-to-Yang–Mills map — an audited record

*Claude (Anthropic, model `claude-opus-5-5`), 27 September 2026. Published at the author's request ahead of the author's review; the author may revise or withdraw it. This record replaces note 51\_ and the Navier–Stokes parts of the Yang–Mills reader, which were withdrawn on 27 September 2026.*

## Abstract

OpenAI's manuscript constructs, for every viscosity, a smooth solution of the forced three-dimensional Navier–Stokes equations with bounded energy that blows up in finite time. A workbench built with AI systems reconstructs it and continues it into a vacuum-hydrodynamics model and into bridges to Yang–Mills and other programmes. We audit the workbench and prove three kinds of results. First, for the shear sector of the cutoff Rindler fluid, the hydrodynamic dispersion series ω(k) = −iνk² − i(3ν³/2c²)k⁴ − … has radius of convergence exactly k∗ = 0.389236400495165… c/ν, set by a certified collision of the diffusive pole with the first non-hydrodynamic pole at purely imaginary frequency; the mode is purely damped up to it, the coefficients have exact Darboux asymptotics, and the series summed on its circle of convergence returns the collision frequency. Second, conditionally on four named statements of the manuscript, the curvature masses of the NS-to-Yang–Mills map grow at explicit rates. Third, under the same statements the blowup is of Type II, with ‖u‖\_{L³} ≳ τ^{−4h/3}; we compare every rate with the classical blowup criteria.

## 0. Introduction

### 0.1 Why this record

The manuscript [O] is a 166-page construction, and the workbench around it adds a 208-page reader, replay programs and continuations. Two questions about it are of independent interest and can be settled by computation: whether the hydrodynamic expansion of the continuation's Rindler fluid converges, and how the manuscript's profile estimates translate into rates for the quantities that the bridges to Yang–Mills use. This record settles the first unconditionally and the second conditionally, re-runs every identity of the workbench's first-pass scripts, and states what the bridges carry.

### 0.2 Main results

- **Theorems 2.1–2.2** (*new*, computer-assisted). The pole collision at q∗ = 0.778472800990330076180356446189 ± 10⁻²⁰ is certified, and the hydrodynamic series has radius exactly q∗² in q², that is k∗ = q∗c/(2ν) in physical units. The continuation had left open whether a nearer complex singularity limits the series.
- **Corollary 2.3** (*new*). a\_k = −C x∗^{−k} k^{−3/2}(1 + O(1/k)) with certified C, and the boundary sum equals the collision value.
- **Theorem 3.1** (conditional on (H1)–(H4)). ‖curl u‖₂² ≳ τ^{−1/2−3h} and ‖∂\_tu‖₂² ≳ τ^{−3/2−3h}, so the magnetic curvature mass diverges with finite integral and the electric one with infinite integral.
- **Proposition 3.2** (conditional on (H1)–(H4), *new*). Type II blowup, ‖u‖\_{L³} ≳ τ^{−4h/3}, divergence of some subcritical L^p norms, and off-axis vorticity ≳ τ^{−1−h}.

### 0.3 What the results mean

The radius theorem places the breakdown of the hydrodynamic gradient expansion of the Rindler fluid at a specific, certified event: the diffusive mode meets the first non-hydrodynamic mode at purely imaginary frequency and real momentum. This is the flat-cutoff instance of the convergence criterion of Grozdanov, Kovtun, Starinets and Tadić, with η/s = 1/(4π), and the partner mode starts at the first Matsubara frequency of the cutoff's Unruh temperature. The conditional rates say how singular the manuscript's solutions are: the blowup exceeds the Type I rate by the angular Reynolds number τ^{−h}, and the classical necessary conditions for a singularity recalled in §3 hold with margins that are positive powers of τ^{−h}. For the Yang–Mills bridge, the rates are exactly what the repository uses, and their status is conditional, not unchecked.

### 0.4 How this record was made

This is an audit of the workbench by an AI system. Every identity of the workbench's first-pass scripts was re-run, the bridge computations were re-derived, one open analytic question of the continuation was certified in ball arithmetic, and an independent referee re-verified the certificate with a second interval library. The main theorem of the manuscript, its Theorem 1.1, is imported and is not verified here; the results of §3 are stated conditionally on the four statements (H1)–(H4). Statements carry one of four statuses, as in the companion papers: *verified* (proved here or re-computed by a program listed in §7), *not verified here*, *my assessment* (a view with its reasons, in the first person), and *proved negative* (with the counterexample or derivation in the text). This record replaces note 51\_ and the Navier–Stokes parts of the Yang–Mills reader, which were withdrawn on 27 September 2026.

### 0.5 Organization

Part A (§§1–3) contains the verified results: the setting (§1), the Rindler shear sector (§2) and the curvature rates (§3). Part B (§4) records the proved limits, Part C (§5) the typed maps to the other programmes with my assessment, §6 open questions and §7 the verification.

---

# Part A. Verified results

## 1. The setting

**The manuscript** [O, Theorem 1.1]. For every ν > 0 there are:

- a force f ∈ C\_c^∞(ℝ³ × (0, ∞)) and a compact set K;
- a smooth solution (u, p) on ℝ³ × [0, 1) with u(·, 0) = 0, supports in K and sup\_t ‖u(t)‖₂ < ∞;
- such that lim sup\_{t↑1} ‖u(t)‖\_∞ = ∞.

The construction builds a slender axisymmetric core with ℓ\_r ≍ τ^{1/2}, ℓ\_z ≍ τ^{1/2−h}, |u| ≍ τ^{−1/2−h} (τ = 1 − t, 0 < h < 1/100), in the similarity coordinates

  τ = q(1 − η²),  z = q^D η,  r² = 2qX,  A = 1/2 + h,  D = 1/2 − h.

The force is defined as the residual, and the work of the manuscript is to make it smooth through t = 1:

- profiles are built with stresses that vanish on an inner region (§4);
- a base correction with uniform profile estimates follows (§5);
- then waves on an auxiliary torus, and a summation with shrinking cutoffs (§§6–9);
- the endpoint is handled by potential-first cutoffs and a Borel extension (§10).

The manuscript's Theorem 1.1 is not verified here.

**The workbench.** It transcribes the 166-page manuscript faithfully, hash-checked against the official PDF. It adds a 208-page reader, programs that replay the identities, and continuations. Every identity of its first-pass scripts was re-run and passes: 251 identities and the 5 conditions of the collision certificate, plus 4 negative controls, which are correctly rejected. The workbench's own replay of 144 result groups passes as well.

## 2. The Rindler shear sector

The vacuum-hydrodynamics continuation starts from the static Rindler metric

  ds² = −(ρ/ρ\_c)²c²dt² + dρ² + dz² + dy² + dx\_⊥²,  0 < ρ ≤ ρ\_c,  ρ\_c = 2ν/c,

whose cutoff surface ρ = ρ\_c is flat. For shear perturbations ∝ e^{−iωt + ikz}, the linearized vacuum equations reduce to the modified Bessel equation for a dual scalar. The boundary condition at the cutoff gives the dispersion relation

  F(α, q) := I′\_α(q) = 0,  q = kρ\_c,  α = −iωρ\_c/c.

These reductions are re-derived by the workbench's scripts.

Put x = q²/4. From the series of I\_α,

  qI′\_α(q) = (q/2)^α Γ(1+α)⁻¹ G(α, x),  G(α, x) = Σ\_{m≥0} (α + 2m)x^m/(m!(1+α)\_m).

For |α| < 1 the prefactor is finite and non-zero. Since G(α, 0) = α and G\_α(0, 0) = 1, the implicit function theorem gives a unique analytic root α\_h(x), the hydrodynamic mode, with α\_h(0) = 0.

**Theorem 2.1 (the collision).** There is (α∗, q∗) with

  q∗ = 0.778472800990330076180356446189 ± 10⁻²⁰,  α∗ = −0.569714080972361784438457668663 ± 1.5·10⁻¹⁰,

at which F = F\_α = 0. At that point F\_q ∈ 1.75035806 ± 7.6·10⁻⁹ and F\_αα ∈ 5.00 ± 0.0203, both positive. So the two roots meet in a square-root fold: they are real for q < q∗ and complex conjugate for q > q∗.

*Proof.* With I = α₀ ± 1.5·10⁻¹⁰ and J = q₀ ± 10⁻²⁰, ball arithmetic shows:

- F > 0 on ∂I × J;
- F(α₀, q₀ − 10⁻²⁰) < 0;
- F > 0 on I × {q₀ + 10⁻²⁰}.

So g(q) = min\_{α∈I} F(α, q) changes sign in J. At its zero the minimizer is interior, so F = F\_α = 0 there. F\_q = (1 + α²/q²)I\_α − I′\_α/q is enclosed directly, and F\_αα by a divided difference with a Cauchy remainder on a circle of radius 0.05. ∎

**Theorem 2.2 (the radius, exactly).**

1. α\_h continues analytically to the disk |x| < x∗ = q∗²/4. It is real and negative for 0 < x < x∗, so the shear mode is purely damped up to the collision.
2. As x ↑ x∗, α\_h(x) → α∗, and α\_h has a square-root branch point at x∗.
3. The Taylor series of α\_h has radius of convergence exactly x∗. Equivalently, the series α\_h = −q²/2 − 3q⁴/16 − 29q⁶/192 − … has radius exactly q∗² = 0.6060199018817300556 ± 5.3·10⁻²⁰ in q². In physical units, ω(k) has radius exactly k∗ = q∗c/(2ν) = 0.389236400495165038… c/ν, and its first singularity is ω∗ = −0.2848570405… i c²/ν.
4. For real x slightly above x∗, the two roots near α∗ are complex conjugates: the modes propagate.

*Proof.* Every step is a finite ball-arithmetic computation.

*Evaluation.* G and G\_α are summed to 30 terms. The tails, for |α| ≤ 0.95 and |x| ≤ 0.2, are bounded by twice the last term, since consecutive term bounds decay by a factor at most 1/2.

*The tiling.* The closed disk |x| ≤ R\_hi, with R\_hi ≥ x∗, minus a small open square around x∗, is covered by 42,650 square cells. For each cell X\_i and an α-box A\_i, the Krawczyk operator K\_i = c − YG(c, X\_i) + (1 − YG\_α(A\_i, X\_i))(A\_i − c) lies in the interior of A\_i.

- By convexity and the mean-value integral, α ↦ α − YG(α, x) maps A\_i into K\_i. Brouwer's theorem then gives a zero for every x ∈ X\_i.
- Two zeros, or a zero of G\_α, would place a translate of A\_i inside int A\_i, which is impossible. So each zero is unique and simple.
- On all 168,301 touching pairs, K\_i ⊆ A\_j or K\_j ⊆ A\_i. So the local zeros glue to one analytic function, the continuation of α\_h.
- The 102 cells meeting the real axis are real-symmetric, so the zero is real there.

*The fold patch.* Take A\_F of half-width 1/4 around α∗ and X\_F of half-width 2⁻⁸ around x∗.

- G ≠ 0 on ∂A\_F × X\_F.
- The winding number of G(·, x) along ∂A\_F is 2. So for x ∈ X\_F there are exactly two zeros β₁, β₂ in A\_F.
- Their discriminant Δ = (β₁ − β₂)² = 2p₂ − p₁², with p\_k = (2πi)⁻¹∮α^kG\_α/G dα, is analytic.
- Its winding number along ∂X\_F is 1. So Δ has exactly one zero in X\_F, it is simple, and it is x∗ by Theorem 2.1.
- All tiled cells meeting X\_F have K\_i ⊆ A\_F.

*Conclusions.* On {|x| < x∗} ∩ X\_F, the zeros β₁ ≠ β₂ are analytic, and α\_h is one of them. This gives (1). Negativity follows because G(0, x) > 0 for x > 0 and α\_h′(0) = −2.

At x∗ the zeros are (p₁ ± √Δ)/2 with a simple zero of Δ. If α\_h were analytic at x∗, Δ would have a zero of even order, which gives (2). For real x > x∗, Δ < 0, which gives (4). A series with radius larger than x∗ would be analytic at x∗, which gives (3). ∎

As a control, the same tiling asked to cover a disk of radius 0.158 > x∗ fails on the real axis beyond x∗, where the two zeros are a conjugate pair.

**Corollary 2.3 (coefficients and the boundary sum).** Write α\_h(x) = Σ\_{k≥1} a\_kx^k. Then

  a\_k = −C x∗^{−k} k^{−3/2}(1 + O(1/k)),  C = κ√x∗/(2√π),  κ² = 4F\_q/(q∗F\_αα).

The certified enclosures give κ² ∈ [1.7915, 1.8061] and C ∈ [0.14696, 0.14757]; numerically C = 0.1471754300. In particular a\_k < 0 for all large k. The series converges absolutely on |x| = x∗, and Σa\_kx∗^k = α∗. So the dispersion series summed at k = k∗ returns the collision frequency ω∗.

*Proof.* The certificate gives analyticity on a slit disk beyond x∗, which contains a Δ-domain. Near x∗, α\_h = α∗ + κ√x∗(1 − x/x∗)^{1/2} + …. The sign κ > 0 is certified by a separate chain of 400 real Krawczyk cells: the hydrodynamic zero is the upper of the two real zeros. The transfer theorem of singularity analysis [FO] gives the asymptotics, and Abel's theorem gives the boundary sum. ∎

The first 240 coefficients are exact rationals: a₁ = −2, a₂ = −3, a₃ = −29/3, a₄ = −2843/72, a₅ = −392029/2160, a₆ = −14509367/16200, a₇ = −63074754607/13608000. They reproduce the continuation's series, including its fifth coefficient. All 320 computed coefficients are negative, and the Darboux-corrected ratios converge to x∗ = 0.1515049754… at rate O(1/k²).

**The other modes.** The partner root that collides with α\_h is the first non-hydrodynamic mode. As q → 0 the zeros of α ↦ I′\_α(q) tend to the zeros of 1/Γ(α), namely α = 0, −1, −2, …, by Hurwitz's theorem applied to 2(q/2)^{1−α}I′\_α(q) → 1/Γ(α). With the Unruh temperature T = ħc/(2πk\_Bρ\_c) of the cutoff observer, the non-hydrodynamic frequencies tend to ω\_n = −2πinT.

**Physical readings.**

- *Normalization.* In units ħ = k\_B = 1, (w, q) = (ω, ck)/(2πT) are the dimensionless variables of Grozdanov, Kovtun, Starinets and Tadić [GKST]. Theorem 2.2 is the flat-cutoff instance of their statement that the radius of the hydrodynamic series is set by the nearest critical point of the spectral curve. Here that critical point lies at real momentum, 𝔮∗² = 0.6060199, and imaginary frequency, 𝔴∗ = −0.5697141i.
- *Shear viscosity.* ρ\_c = 2ν/c gives ν = c²/(4πT), and so η/s = 1/(4π).
- *Pole collisions.* The collision that bounds the series is a collision of the diffusive pole with the first non-hydrodynamic pole, the kind of event that Areán, Davison, Goutéraux and Suzuki identify with the breakdown of diffusion [ADGS]. At the radius, |ω∗|/(νk∗²) = 1.8802.
- *The k⁴ coefficient.* It agrees with the corrected Rindler Navier–Stokes equation of Compère, McFadden, Skenderis and Taylor [CMST, (6.3)] after conversion to proper time. The k⁶ coefficient and all higher ones come from the exact dispersion relation.
- *A two-pole model.* The telegraph model α² + α + 2x = 0, calibrated to the diffusion constant and to the first non-hydrodynamic mode, collides at (q², α) = (1/2, −1/2). The exact collision is at (0.6060, −0.5697).

## 3. Curvature rates for the NS-to-Yang–Mills map

The Yang–Mills repository maps a velocity field to an abelian connection A\_i = λu\_iT and computes its curvature masses 𝒦\_B = λ²‖curl u‖² and 𝒦\_E = λ²c⁻²‖∂\_tu‖². It derives lower rates for them from the manuscript's profile estimates. The derivation uses four statements of the manuscript:

- **(H1)** Theorem 4.6(i): E = √(2X)F > 0 for X > 0, with F smooth up to the axis.
- **(H2)** Proposition 5.5, (5.42): 𝒟^I(q^Au\_{θ,B} − E₀) = O(q^{2h}) uniformly on [X\_lo, X\_hi] × [−1, 1]. This holds for the summed background, with the cutoffs included.
- **(H3)** The annular corrections vanish on the inner region X < X\_a: Proposition 9.9, Step 5, together with the sentence after (10.21), and the support statement of Theorem 4.6(ii).
- **(H4)** Proposition 10.1: the cutoffs equal one near the singular point.

**Theorem 3.1.** Under (H1)–(H4), for every ν > 0 there are C\_Ω, C\_u̇ > 0 such that for all small τ

  ‖curl u\_ν(1−τ)‖₂² ≥ ν^{3/2}C\_Ω τ^{−1/2−3h},  ‖∂\_tu\_ν(1−τ)‖₂² ≥ ν^{5/2}C\_u̇ τ^{−3/2−3h}.

Hence 𝒦\_B → ∞ with ∫₀¹𝒦\_B < ∞, and 𝒦\_E → ∞ with ∫₀¹𝒦\_E = ∞.

*Proof.* Choose X\_∗ ∈ (X\_lo, X\_a) with e₀ = E₀(X\_∗, 0) > 0 and an η-interval on which E₀ ≥ e₀/2. By (H2)–(H4), u\_θ ≥ (e₀/4)q^{−A} on the circles r = √(2X\_∗q).

- *Enstrophy.* Stokes' theorem and Cauchy–Schwarz on each disk give ∫ω₃² ≥ 4πu\_θ². Integrating with dz/dη = τ^D(1 − 2hη²)(1 − η²)^{−D−1} gives the exponent D − 2A = −1/2 − 3h.
- *Time derivative.* At a fixed point, ∂\_tu\_θ = q^{−A−1}(𝓗 + O(q^{2h})), where 𝓗 = (AE + XE\_X + DηE\_η)/(1 − 2hη²), and 𝓗(X, 0) = (1 + h)E(X, 0) + O(X^{3/2}) > 0 for small X. This gives the exponent −3/2 − 3h.
- *Finiteness of ∫𝒦\_B.* This follows from the energy inequality.
- *Viscosity scaling.* The map (10.22) supplies the factors of ν. ∎

Every exponent computation is verified symbolically, with three negative controls.

**Proposition 3.2 (Type II and critical-norm growth).** Under (H1)–(H4), for small τ:

1. ‖u(1−τ)‖\_p^p ≥ c\_pτ^{3/2−h−p(1/2+h)} for 1 ≤ p < ∞. In particular ‖u(1−τ)‖\_{L³} ≥ cτ^{−4h/3} → ∞, and the L^p norms with (3 − 2h)/(1 + 2h) < p < 3 also diverge.
2. ‖ω(1−τ)‖\_∞ ≥ cτ^{−1−h}, from a disk mean away from the axis.
3. τ^{1/2}‖u(1−τ)‖\_∞ ≥ cτ^{−h}, so the blowup is of Type II.

These rates are consistent with the classical necessary conditions for a singularity, with margins that are positive powers of τ^{−h}:

- Leray's rates [Le]: the enstrophy exceeds (T − t)^{−1/2} by τ^{−3h}, and ‖u‖\_p for p > 3 exceeds its rate by τ^{−h(1+1/p)};
- the divergence of ‖u‖\_{L³} at a singular time [ESS, Se];
- ∫‖ω‖\_∞ = ∞.

The Type I exclusion theorems for axisymmetric unforced flows [CSTY, KNSS] concern a different class; the construction here is forced and axisymmetric only on its inner region. Statement (3) shows that it exceeds the Type I rate by at least the angular Reynolds number τ^{−h}.

**A formula in the growth path.** The official PDF prints (10.20) as x\_τ = (√(2X\_inτ), 0, 0), with the radical over 2X\_inτ. With this path, q = τ and X = X\_in, and (10.21) follows from (3.6). The transcription renders the radical over the factor 2 only, so its errata ledger gets this correction.

---

# Part B. Proved limits

## 4. What is excluded

Three statements of Part A are limits, and each is proved.

- **The dispersion series does not converge beyond k**∗ (Theorem 2.2(3)). A series with a larger radius would make α\_h analytic at x∗, where it has a square-root branch point. The control computation confirms this: the same tiling, asked to cover a disk of radius 0.158 > x∗, fails on the real axis beyond x∗, where the two zeros are a conjugate pair.
- **Beyond the collision the shear modes propagate** (Theorem 2.2(4)): for real x slightly above x∗, the two roots near α∗ are complex conjugates, so the purely damped regime ends exactly at k∗.
- **The two-pole model misplaces the collision.** The telegraph model α² + α + 2x = 0, calibrated to the diffusion constant and to the first non-hydrodynamic mode, collides at (q², α) = (1/2, −1/2); the exact collision is at (0.6060, −0.5697). So the radius is a property of the exact dispersion relation and is not captured by the two-pole truncation.

The formula (10.20) of the growth path is printed correctly in the official PDF, and the workbench's transcription differs from it (§3); the correction belongs in the transcription's errata ledger.

---

# Part C. The typed maps to the other programmes

## 5. The typed maps between the workbench and the other programmes

The workbench connects the Navier–Stokes construction to the other programmes through explicit maps. The table states what each map carries and what is established about it here.

| Map | What it carries | Established here |
|---|---|---|
| NS → YM, abelian | A\_i = λu\_iT; curvature masses 𝒦\_B, 𝒦\_E | the map and its identities; the rates of Theorem 3.1 under (H1)–(H4) |
| NS → YM, non-abelian | 𝐀\_i = λe\_i × u; fields, invariants and currents | all identities, for every divergence-free u; the off-axis vorticity bound of Proposition 3.2(2) |
| NS → Erdős–Straus | the auxiliary torus operator J = [[3, 1], [1, 5]], with det 14 and eigenvalues 4 ± √2 | the operator identities used in 21 statements of the Erdős–Straus supplement |
| NS → zeta | angular-momentum balance, Mellin shift and the Müntz multiplier W\_h(s) = ζ(s)(1 − 2^{s−1})(1 − 2^{h−s}) | the transforms exactly; the growth under Theorem 3.1; the Mellin abscissa of 𝒦\_B(1 − τ) lies in [1/2 + 3h, 1] |
| S⁶ → NS | a Beltrami-mode forced solution on 𝕋³ from the S⁶ oscillator | global smooth solution, exactly |
| Jacobian → NS kinematics | U = DF⁻¹(V∘F), a divergence-free polynomial field whose flow escapes at τ = 1/8 | exactly (companion paper on the Jacobian counterexample, §4) |
| NS → Einstein | snapshot encoding, Kasner map, Rindler response, slab comparator | all identities; the collision and the exact radius of §2 |

My assessment of these maps, taken together: the NS → Einstein map has produced the strongest result so far, the exact radius of §2, which is of independent interest in fluid/gravity duality because it places the breakdown of the hydrodynamic expansion of the Rindler fluid at a certified pole collision. The NS → YM maps are exact as identities, and their analytic content is conditional on (H1)–(H4); certifying those four statements (Question 3) would make the curvature rates unconditional. For the NS → zeta and NS → Erdős–Straus maps, what is established is the exact identities; what they carry about the zeta function or the equation beyond those identities is not verified here.

## 6. Questions

1. Derive the continuation's boundary relation (2.3) from the fluid/gravity linearization of Bhattacharyya, Hubeny, Minwalla and Rangamani, and certify its Brown–York response formulas (20)–(24).
2. Certify the partner branch as real and simple on all of 0 < q < q∗ by the same tiling, applied to a normalization regular at α = −1.
3. Certify the manuscript's profile constants in interval arithmetic, and carry out the exponent bookkeeping of its correction cycle by hand.
4. Give explicit constants in the Lichnerowicz existence step of the continuation.
5. The manuscript needs h > 0 for its own steps. Can a construction of this kind work at h = 0, where it would sit exactly at the Type I rate?

## 7. Verification

The scripts are in the record's `checks/ns/` folder, with their outputs.

- **Theorem 2.1.** Certified in Arb with python-flint (`certify_collision.py`).
- **Theorem 2.2.** Certified in 137 s (`certify_hydro_radius.py`). An independent referee re-verified:
  - all 42,650 Krawczyk conditions, with a second interval library (`mpmath.iv`), 36 terms and an independently derived tail bound;
  - coverage and all 168,301 consistency pairs, in exact integer arithmetic;
  - the fold patch, at twice the resolution.
- **Corollary 2.3.** The sign of κ is certified (`ns51_sign_check.py`). The 240 exact coefficients are in `hydro_series.py`, and the referee's 320 coefficients match −C to 12 digits.
- **Theorem 3.1 and Proposition 3.2.** All exponents are verified symbolically (`ns51_rate_lemmas.py`, 27 checks).
- **The official PDF.** Its SHA-256 is `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`, equal to the transcription's frozen hash.

## References

- [O] OpenAI, manuscript on finite-time singularity for the forced Navier–Stokes equations, 2026, https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf.
- [ADGS] D. Areán, R. A. Davison, B. Goutéraux, K. Suzuki, Hydrodynamic diffusion and its breakdown near AdS₂ quantum critical points, Phys. Rev. X 11 (2021) 031024.
- [BHMR] S. Bhattacharyya, V. Hubeny, S. Minwalla, M. Rangamani, Nonlinear fluid dynamics from gravity, JHEP 02 (2008) 045.
- [BKLS] I. Bredberg, C. Keeler, V. Lysov, A. Strominger, Wilsonian approach to fluid/gravity duality, JHEP 03 (2011) 141; From Navier–Stokes to Einstein, JHEP 07 (2012) 146.
- [CMST] G. Compère, P. McFadden, K. Skenderis, M. Taylor, The holographic fluid dual to vacuum Einstein gravity, JHEP 07 (2011) 050.
- [CSTY] C.-C. Chen, R. M. Strain, T.-P. Tsai, H.-T. Yau, IMRN 2008, rnn016; Comm. PDE 34 (2009) 203–232.
- [ESS] L. Escauriaza, G. Seregin, V. Šverák, L\_{3,∞}-solutions of Navier–Stokes equations and backward uniqueness, Russ. Math. Surveys 58 (2003) 211–250.
- [FO] P. Flajolet, A. Odlyzko, Singularity analysis of generating functions, SIAM J. Discrete Math. 3 (1990) 216–240.
- [GKST] S. Grozdanov, P. Kovtun, A. Starinets, P. Tadić, Convergence of the gradient expansion in hydrodynamics, PRL 122 (2019) 251601; The complex life of hydrodynamic modes, JHEP 11 (2019) 097.
- [KNSS] G. Koch, N. Nadirashvili, G. Seregin, V. Šverák, Liouville theorems for the Navier–Stokes equations and applications, Acta Math. 203 (2009) 83–105.
- [Le] J. Leray, Sur le mouvement d'un liquide visqueux emplissant l'espace, Acta Math. 63 (1934) 193–248.
- [MR] D. Marolf, M. Rangamani, Causality and the AdS Dirichlet problem, JHEP 04 (2012) 035.
- [Se] G. Seregin, A certain necessary condition of potential blow up for Navier–Stokes equations, Comm. Math. Phys. (2012), arXiv:1104.3615.
