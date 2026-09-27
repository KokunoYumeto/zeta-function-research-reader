# Referee report on note 51_ (Navier–Stokes workbench; NS → YM rates; Rindler shear radius)

Independent referee (Claude, `claude-opus-5-5`), 27 September 2026. The note was refereed in both directions: overstatements and errors, and understatements and missed results. Line numbers "L…" refer to `51_NAVIER_STOKES_…_Q_STAR_SQUARED.md` as of 13:51 UTC (corrected by the coordinator from "15:51", which was the container's local time). All scripts and outputs are in this folder. Environment: python-flint 0.9.0 (Arb), mpmath 1.3.0 (including `mpmath.iv`), sympy 1.14.0. Quotations are under 15 words.

## Verdict

**No MAJOR findings.**
- Theorems 51.1 and 51.2 are correct. The proof of 51.2 was re-run: it is CERTIFIED in 134 s, and the output is identical apart from timing.
- The proof of 51.2 was also re-verified independently:
  - every one of the 42,650 Krawczyk conditions, with a different interval library, a different number of terms and a different tail bound;
  - coverage, neighbour search and consistency, in exact integer arithmetic;
  - the fold patch, with twice the discretization.
- Lemma 51.3 is correct, and its hypotheses (H1)–(H4) reflect the transcription faithfully. Two citation refinements are needed.
- The exponents of Proposition 51.4 are correct. Its comparison paragraph overstates in three places, and two of its comparisons hold automatically for any singular solution.
- Understatements:
  - Theorem 51.2 implies the exact asymptotics of the coefficients.
  - It also implies convergence on the circle of convergence itself, which makes the wording "converges exactly for |q²| < q*²" literally false.
  - Further unused consequences: uniqueness of the collision, part of the partner branch, and the result's unconditional status.
  - There are connections to the literature that the note should state (items 21–27).

## Scripts run by the referee (this folder)

| Script | What it does | Result |
|---|---|---|
| `certify_hydro_radius_rerun_dump.py` | verbatim copy of the certificate plus an exact dump of all cells (`cells_dump.pkl`, balls as mantissa/exponent pairs) | CERTIFIED, 134 s; identical to the shipped output (`certify_hydro_radius_rerun_OUTPUT.txt`) |
| `ref_G_independent.py` | tests `GGa`/`tails` (extracted verbatim with `ast`) against mpmath Bessel functions, Arb ₀F₁, and 400-term series | 8/8 PASS |
| `ref_cells_audit.py` | exact dyadic audit: ideal squares, coverage by recursive descent, all intersecting pairs, realness, origin, (Fd), α-domain | 9/9 PASS |
| `ivG.py` + `ref_krawczyk_independent.py` | Krawczyk re-verification of **all 42,650 cells** with `mpmath.iv`, 36 terms, and a tail bound derived independently | 0 failures; K′ ∩ K ≠ ∅ for every cell |
| `ref_fold_patch_independent.py` | (F0)–(Fc) re-verified with `mpmath.iv`, 512 segments per boundary (the certificate uses 256); zero of Δ located numerically | 4/4 PASS; Δ(x) = 0 at x* (difference 1e-32) |
| `ref_series_darboux.py` | a_k for k ≤ 320 by power-series Newton in Arb; checks against the exact rationals; Darboux constant; Abel sum at the radius | 5/5 PASS |
| `ref_physics_and_continuation.py` | monodromy around circles; Unruh/Matsubara; the CMST unit conversion; telegraph model; Matsubara limits | see items 13, 25–26 |
| `ref_prop514_margins.py` | exponent margins of Proposition 51.4 against Leray's bounds | see items 17, 27 |
| `rerun_small_scripts_OUTPUT.txt`, `first_pass_rerun/` | `certify_collision.py`, `ns51_rate_lemmas.py`, `track_partner.py`, and the 9 first-pass checkers re-run | identical apart from timing |

To reproduce: run `python3 certify_hydro_radius_rerun_dump.py` first, since it writes `cells_dump.pkl`. Then run the `ref_*.py` scripts from this folder. The Krawczyk check runs in two halves: `ref_krawczyk_independent.py 0 2` and `ref_krawczyk_independent.py 1 2`, about 7 min each.

---

## Findings

### A. The computer-assisted proof (Theorem 51.2, §4.2 L155–194)

**1. OK-CHECKED: the evaluator and the tail bounds** (L134–140, L165–168; certificate L15–18, L65–95).
- (51.1) matches mpmath's I_α at 60 random points with |α| ≤ 0.95 and |x| ≤ 0.2. Agreement is to 1e-60.
- G_α matches numerical α-differentiation of the Bessel expression.
- The balls of `GGa` contain the independent values at points and in 40 random boxes.
- The ratio bounds hold for m ≥ 30, |α| ≤ 0.95, |x| ≤ 0.2:
  - the ratio b_{m+1}/b_m carries the factor (a+2m+2)/(a+2m) ≤ 2;
  - the ratio d_{m+1}/d_m carries the factor (1+(a+2m+2)H_{m+1})/(1+(a+2m)H_m), which is < 2.14;
  - so both ratios are ≤ 2.2·10⁻⁴ ≪ 1/2. This was also checked in exact rationals for 30 ≤ m ≤ 2000.
- At the worst corner the true tails are 4.4·10⁻⁸² and 1.1·10⁻⁸⁰. The bounds are 2b_M = 9.2·10⁻⁸² and 2d_M = 2.2·10⁻⁸⁰.
- The tails are added to the real and imaginary radii. This is valid, since |t| ≤ ε implies |Re t|, |Im t| ≤ ε.
- (`ref_G_independent_OUTPUT.txt`)

**2. MINOR (provenance): the claimed mpmath check of (51.1) is not in the shipped script** (L140).
- L140 says (51.1) was checked against mpmath "to 37 digits (`certify_hydro_radius.py` preamble; session check)".
- The shipped script contains no such check. It states (51.1) only in its docstring.
- *Fix:* cite `referee/ref_G_independent.py`, or add the check to the script.

**3. OK-CHECKED, with a MINOR presentational point: the Krawczyk argument** (L170–172).
- The logic is correct for complex analytic G and square (acb) boxes:
  - **existence:** N_x(α) = α − YG(α, x) maps the compact convex set A_i into K_i ⊂ A_i. Apply Brouwer; Y ≠ 0.
  - **uniqueness and simplicity:** two zeros in A_i, or a zero of G_α in A_i, put 0 in the convex hull of G_α(A_i, x) (mean-value integral along a segment in A_i). Then 1 ∈ 1 − YG_α(A_i, X_i), so K_i contains c − YG(c, x) + (A_i − c), a translate of A_i. A translate cannot lie in int(A_i).
  - **analyticity in x:** the implicit function theorem.
- The phrase at L171, "A translate of A_i cannot fit inside int(A_i)", compresses this chain. The existence step does not name Brouwer.
- *Fix:* write out the chain above in two lines.

**4. OK-CHECKED: consistency, neighbour search, float rounding and coverage** (L169, L173–175). Checked in exact integer arithmetic (`ref_cells_audit_OUTPUT.txt`):
- **Ideal squares.** Every cell centre lies within 3.5·10⁻¹⁷ of its ideal 3-adic lattice centre. Every certified X-box, with Arb's outward-rounded radius, contains its ideal square.
  - The enlargement 1 + 10⁻⁹ is at least 1.6·10⁻¹⁴ in absolute terms, a factor of about 500 above the rounding.
  - Arb's 30-bit radius rounding only enlarges boxes.
- **Coverage.** An exact recursive descent confirms that the certified ideal squares, plus the squares outside the closed disk |x| ≤ R_hi (exact dyadic upper bound for x*) and those inside the open hole, tile the grid. There are no gaps and no orphan cells.
- **Neighbour search.** Every X-box lies strictly inside the 3×3 block of its top-level square, so searching adjacent top-level cells is complete.
- **Intersecting pairs.** Brute force finds 168,301 pairs, the same number as the certificate. For every pair, K_i ⊆ A_j or K_j ⊆ A_i holds exactly; both inclusions hold for 164,268 pairs.
- **One inclusion suffices:** for x ∈ X_i ∩ X_j, the zero α_i(x) lies in A_j, where the zero is unique.
- **Remaining checks:**
  - 102 real-axis cells, all real-centred;
  - one origin cell, with 0 in its α-box;
  - 4,039 cells meeting X_F, all with K_i ⊆ A_F;
  - every α-box lies within |α| ≤ 0.533;
  - every K_i lies in int(A_i).
- **Remark.** The certificate's "(Cov)" line (L414 of the script) only tests ETA_IN < ETA. Coverage holds by construction of the subdivision loop and is now independently confirmed.
- *Suggestion:* ship the exact audit.

**5. OK-CHECKED: all 42,650 Krawczyk conditions, independently** (L170–172).
- Every condition K_i ⊂ int(A_i) was re-verified with `mpmath.iv` (not Arb), 36 terms instead of 30, and an independently derived tail bound (`ivG.py`).
- This used the certificate's own A_i, c_i and actual X_i boxes, read exactly. Y_i was recomputed.
- For 659 cells the rectangular interval arithmetic of `mpmath.iv` needed the hull of G_α over a 3×3 subdivision of A_i. Sub-box endpoints were shared exactly, so the sub-boxes cover A_i.
- Result: 0 failures. The independent enclosure K′_i meets K_i for every cell (`ref_krawczyk_independent_OUTPUT.txt`).

**6. OK-CHECKED: realness (R) and origin (C0)** (L174, L176).
- G has real coefficients. A real-centred, real-symmetric α-box with a unique zero therefore has a real zero for real x.
- The origin cell's box contains 0, and G(α, 0) = α.

**7. OK-CHECKED: the fold patch (F)** (L177–183).
- (Fa) G ≠ 0 on ∂A_F × X_F. With (Fb), this gives exactly two zeros in A_F for every x ∈ X_F. The argument needs G analytic near A_F, which holds since |α| ≤ 0.86 on A_F.
- p_k is analytic, so Δ = 2p₂ − p₁² is analytic on a neighbourhood of X_F.
- The winding computation is rigorous. Each segment enclosure excludes 0, so the change of argument along a segment is less than π and equals the principal argument of the endpoint ratio.
- (Fc) gives exactly one zero of Δ in X_F, and it is simple. It is x*, because the certified double zero lies in int(A_F × X_F).
- **Independent re-run** with `mpmath.iv`, 128 segments per edge:
  - windings 2 ± 3·10⁻⁴⁵ and 1 ± 2·10⁻⁴⁴;
  - numerically Δ(x) = 0 at x* (difference 1·10⁻³²), with p₁(x*)/2 = −0.569714080972362 = α*;
  - Δ′(x*) = −7.186436 = −4κ², where κ² = 4F_q/(q*F_αα) (`ref_fold_patch_independent_OUTPUT.txt`).

**8. OK-CHECKED, with MINOR gaps in wording: conclusions (a)–(d) and the radius** (L184–192).
- The deductions are correct:
  - two analytic branches on the convex set X_F ∩ {|x| < x*};
  - Δ > 0 on [X_c − 2⁻⁸, x*) by continuity from a certified real point;
  - non-analyticity at x*, because Δ would otherwise have a zero of even order;
  - Δ < 0 to the right of x*;
  - radius ≥ x* from (a), and ≤ x* from (b).
- *Gaps to close in the text:*
  - (i) State why (tiled region) ∩ X_F ∩ {|x| < x*} is connected: the hole lies in int(X_F), so the set is C-shaped.
  - (ii) "Purely damped" (L20, L161) needs α_h < 0 on (0, x*), not only realness. This follows from G(0, x) = Σ 2m x^m/(m!)² > 0 for x > 0, so α_h never returns to 0. Add one line.
- The monodromy test (N) corroborates the result independently. Adaptive continuation of α_h around |x| = r:
  - returns to itself for r ∈ {0.05, 0.12, 0.15, x*(1 − 10⁻⁴)}, with jump ≤ 4·10⁻²⁰;
  - switches to the partner for r ∈ {x*(1 + 10⁻⁴), 0.155}, with jump 0.57 (`ref_physics_and_continuation_OUTPUT.txt`).

**9. MINOR (a statement that is literally false): "converges exactly for |q²| < q*²"** (L52; also L53, "converges exactly for |k| < k*").
- By Theorem 51.2 and Darboux (item 21), a_k x*^k = O(k^{−3/2}).
- The series therefore converges absolutely on the closed disk |x| ≤ x*, circle included.
- *Fix:* "has radius of convergence exactly q*²; it converges absolutely for |q²| ≤ q*² and diverges for |q²| > q*²". Make the same fix for k*. Statement (c) at L160 is correct as worded.

### B. Theorem 51.1, the numerics and the physics remarks (§4.1, L142–215)

**10. OK-CHECKED: Theorem 51.1** (L142–153).
- The existence argument (min over α, interior minimiser) is correct.
- F_q = I″_α comes from the Bessel equation and is correct.
- The F_αα remainder bound (h²/12)·4!·M/(ρ − r_I − h)⁴ is a valid Cauchy estimate.
- The interpolation step in (iii) is correct.
- The re-run output is identical. The square-root "Consequence" (L153) has the correct signs.

**11. OK-CHECKED: the numerical corroboration** (L196–202).
- An independent Arb power-series Newton iteration to k = 320 contains all 60 stored exact rationals and a₁…a₇ as quoted.
- All a_k < 0 for k ≤ 320; the note claims this for 240.
- The corrected ratios quoted at k = 40, 100, 200 are reproduced. Their error times k² is 0.120, 0.1216, 0.1220 and 0.1222 at k = 40, 100, 200, 319, which confirms the O(1/k²) rate (`ref_series_darboux_OUTPUT.txt`).

**12. OK-CHECKED (conversion only): the k⁴ comparison with Compère–McFadden–Skenderis–Taylor** (L209–211).
- The unit conversion is verified symbolically. With t = √r_c τ and ν = √r_c, (28) is exactly the plane-wave relation of ∂_τv − r_c∂²v = −(3/2)r_c²∂⁴v. The k⁶ coefficient 29ν⁵/(6c⁴) is also verified.
- The referee accessed only bibliographic data for arXiv:1103.3022 (JHEP 07 (2011) 050, confirmed on INSPIRE), not its eq. (6.3). The quoted equation is therefore unverified here; RESEARCH.md (28) makes the same claim.
- *Fix:* either quote (6.3) with its page or section, or say "as quoted in RESEARCH.md §5".

**13. OK-CHECKED, with a MINOR wording point: partner branch, Matsubara and Unruh remarks** (L204–207).
- T = ħc/(2πk_Bρ_c) is correct: proper acceleration c²/ρ_c, and t is proper time at ρ_c. It gives ω_n = −2πinT.
- Numerically, the zeros of I′_α(q) near α = −n satisfy (α + n)/q^{2n} → (−1)^{n+1}n/((n!)²4ⁿ): 1/4, −1/32 and 1/768 for n = 1, 2, 3. This confirms "x ≈ 1 + α" for n = 1.
- *Wording (L206):* "At q = 0 exactly, the zeros of I′_α(q) as q → 0" mixes two statements. At q = 0 the boundary problem degenerates. The correct statement is a limit: (q/2)^{1−α}·2I′_α(q) → 1/Γ(α) locally uniformly, so by Hurwitz the zeros tend to α = 0, −1, −2, …

### C. Lemma 51.3 and the YM bridge (§5, L219–249)

**14. OK-CHECKED, with MINOR citation refinements: hypotheses (H1)–(H4)** (L223–229), checked against the transcription.
- **(H1)** Theorem 4.6(i) (src p.33) says E = √(2X)F > 0 for X > 0 and every η ∈ [−1, 1], with F smooth up to X = 0. This gives both the positivity and the O(√X) used.
- **(H2)** (5.42) (src p.60) holds uniformly on [X_lo, X_hi] × [−1, 1] for the summed background. The Stokes streamfunctions are "summed before differentiation", so the base summation cutoffs are included.
  - The source says "Fix radial endpoints" and "constants … may depend on the fixed radial endpoints". "For every 0 < X_lo" (L225) is therefore a reading, and a sound one.
  - *Fix:* say so.
- **(H3)** Step 5 of Prop. 9.9 (src p.116) literally asserts vanishing only at the chosen X_in: "All annular corrections vanish there."
  - The Lemma needs vanishing on the whole region, for |η| ≤ η_* and on an open set for ∂_t. The sentence after (10.21) on src p.124 states exactly this: "the annular corrections vanish in the fixed inner similarity region", and "The summation cutoffs remain in this estimate". The support statements say the same: Thm 4.6(ii),(iv), (8.4), Step 4.
  - *Fix:* cite p.124 and the support statements together with Step 5.
- **(H4)** Prop. 10.1 (src p.117): the fields "agree with u^loc, p^loc on a spatial neighborhood of the origin" for t near 1. Correct.

**15. OK-CHECKED: every elementary step of `ns_inner_profile_curvature_current_bridge.md` §§3–5** (the energy bound of §3 and the steps of §§4–5), re-derived by hand; `ns51_rate_lemmas.py` re-run with 27/27 identical.
- **Energy bound (§3):** ‖u‖ ≤ 𝓕 from d‖u‖/dt ≤ ‖f‖; (3.3) from d𝓕²/ds = 2‖f‖𝓕; (3.4)–(3.5).
- **Enstrophy bound:**
  - (4.3) with e_* = e₀/4;
  - Stokes (4.4) and Cauchy–Schwarz (4.5);
  - dz/dη (4.6);
  - (4.7): exponent D − 2A and C_Ω = 4πe_*²∫L(1−η²)^{2A−D−1}dη;
  - (4.8): the factor ν^{3/2}.
- **Time-derivative bound:**
  - (5.1): q_t = −1/L, η_t = Dη/(qL), X_t = X/(qL), with L = 1 − 2hη² from 1 − η² + 2Dη²;
  - (5.2)–(5.3), and the non-vanishing of 𝓗;
  - (5.5): volume element q τ^D L(1−η²)^{−D−1};
  - (5.6): C_{u̇} = (πh_*²/2)ΔX∫L(1−η²)^{2A−D}dη;
  - (5.7): the factor ν^{5/2}.
- *Optional simplification:* since E = √(2X)F with F(0, 0) > 0, 𝓗(X, 0) = (1+h)E(X, 0) + O(X^{3/2}) > 0 for small X > 0. This gives the non-vanishing directly, without the contradiction argument.

### D. Proposition 51.4 (§6, L253–277)

**16. OK-CHECKED: exponents** (L255–265).
- 1 + D − pA and p_h = (3 − 2h)/(1 + 2h) < 3 are correct.
- For p = 3, the η-factor L(1 − η²)^{−1+4h} and the rate τ^{−4h/3} are correct.
- The disk-mean vorticity √2(e₀/4)X_*^{−1/2}q^{−1−h} is correct.
- The Type II statement is correct: τ^{1/2}·τ^{−A} = τ^{−h}.

**17. MINOR: the comparison with classical criteria overstates** (L66, L267–277; `ref_prop514_margins_OUTPUT.txt`).
- **(i)** "with margins that are powers τ^{−h}" (L66) and "with room τ^{−h}" (L267) are inaccurate:
  - the Leray enstrophy margin is τ^{−3h};
  - the L²_tL^∞_x margin is τ^{−2h};
  - the L^p margin against Leray's ‖u(t)‖_p ≥ c(T−t)^{−(p−3)/(2p)} is τ^{−h(1+1/p)};
  - the L³ criterion is a divergence statement, not a rate.
- **(ii)** "avoids Type I by exactly the factor τ^{−h}" (L274): (3) is only a lower bound, and no upper bound ‖u‖_∞ ≲ τ^{−1/2−h} is established (the annular waves are not bounded here). Replace "exactly" with "at least".
- **(iii)** The reading at L275 ("h > 0 is the room …") is speculative. The source needs h > 0 for its own construction, and nothing shows that h = 0 is excluded. Drop it, or mark it as speculation.
- **(iv)** The divergences of L²_tL^∞_x and of ∫‖ω‖_∞ (L276) hold automatically for any singular solution: Leray's ‖u(t)‖_∞ ≥ c(T−t)^{−1/2}, and BKM itself. They add nothing beyond (3). The genuine cross-check in this paragraph is the integrability condition h < 1/6.

### E. Other parts of the note

**18. MINOR: §8, non-abelian row** (L300: "the axis growth is **C**").
- The addendum's (243) (`nonabelian_fluid_profile_addendum.tex` L163–176) is an *exact* axis identity, b(0,0,s) = C⁻¹τ^{−1−h}. It is attributed to the workbench's own "released source continuation" (`axis_continuation_body.tex`), not to OpenAI's manuscript.
- (5.42) holds only for X ≥ X_lo > 0 and does not reach the axis. An exact power law also ignores the O(q^{2h}) corrections.
- *Fix:* either name that source as the hypothesis, or state what (H1)–(H4) do give: the disk-mean bound sup|ω| ≥ cτ^{−1−h} of Proposition 51.4(2).

**19. OK-CHECKED: D1** (L283–287).
- The crop `D1_official_pdf_p124_eq10_20.png` shows √(2X_inτ) with the radical over 2X_inτ.
- `pp121-126.tex` L304–307 reads `\sqrt2X_{\mathrm{in}}\tau`, as stated. (3.6) on src p.16 and the p.124 text after (10.21) need q = τ.
- `ERRATA.jsonl` holds only a ledger-initialization record, so "empty" is accurate as far as errata are concerned.
- The browser hash could not be re-checked here.

**20. OK-CHECKED, with MINOR additions: citations** (§9 L313–321, §6 L268–277).
- Checked on INSPIRE: 1904.01018 (PRL 122, 251601); 1803.08058 (JHEP 06 (2018) 059); 2007.05524 (PRD 104, 066002); 2011.12301 (PRX 11, 031024); 0712.2456; 1006.1902; 1101.2451; 1103.3022; 1201.1233 (Marolf–Rangamani, "Causality and the AdS Dirichlet problem", JHEP 04 (2012) 035).
- Checked on arXiv and the web: Chen–Strain–Tsai–Yau I, IMRN 2008 (math/0701796); II, Comm. PDE 34:3 (2009), **203–232** (0709.4230); KNSS, Acta Math. 203 (2009) no. 1; RSS, JMP 53 (2012) 115618; Leray, ESS and CMZ, as in the source bibliography [16], [11], [6]–[8].
- *Add:* the pages for CSTY II.
- *Add:* G. Seregin, Comm. Math. Phys. (2012), DOI 10.1007/s00220-011-1391-x (arXiv:1104.3615). It proves lim ‖u(t)‖_{L³} = ∞ at any blowup time, the sharper classical statement for the L³ comparison at L269.
- *Add:* Grozdanov–Kovtun–Starinets–Tadić, "The complex life of hydrodynamic modes", JHEP 11 (2019) 097. Its abstract ties radii to "critical points of the associated complex spectral curves", and the paper covers a translation-breaking model and pole-skipping.
- *Soften (L214, L316):* the ADGS abstract characterises the collision by the absolute values of ω_eq and k_eq. The referee could not confirm from bibliographic data that their collisions are at real k and imaginary ω in general. Say "a collision with a non-hydrodynamic (IR) pole", or cite the figure if real k is meant.
- *Alternative for a collision on the imaginary axis at real k:* Davison–Goutéraux, JHEP 01 (2015) 039 (coherent/incoherent crossover).

### F. Understatements (what the note proves but does not state)

**21. UNDERSTATEMENT: Theorem 51.2 gives the exact asymptotics and the sum on the boundary** (§4.2, L196–202 presents these only as "(N)").
- The certificate proves more than needed:
  - α_h is analytic on a slit disk {|x| < x* + ε} ∖ [x*, x* + ε) for some ε > 0. The closed cells have IFT neighbourhoods, and Δ ≠ 0 on X_F ∖ {x*};
  - near x*, α_h = p₁/2 + ½√(x*−x)·√g(x) with g analytic and g(x*) = 4κ².
- So x* is the **only** singularity on the circle of convergence. The Darboux transfer then gives
  - a_k = −C x*^{−k} k^{−3/2}(1 + O(1/k)), with C = κ√x*/(2√π) = 0.1471754299685…, κ² = 4F_q/(q*F_αα) = 1.7966091…
- Consequences, each checked with the 320 coefficients:
  - a_k < 0 for all large k: a theorem, not only an observation for k ≤ 240;
  - the corrected-ratio law holds;
  - the series converges absolutely on |x| = x*, and Abel's theorem gives Σ_k a_k x*^k = α*. Numerically, S₃₂₀ plus the Darboux tail equals α* to 1.6·10⁻¹¹; Richardson extrapolation gives C to 12 digits.
- Physically, the hydrodynamic series summed at k = k* returns the collision frequency ω*.
- In the spirit of Withers 2018, the hydrodynamic coefficients alone determine x*, α* and κ, and hence the partner mode near the collision.
- *Proposed addition:* a Corollary 51.2′ with this statement (`ref_series_darboux_OUTPUT.txt`).

**22. UNDERSTATEMENT: uniqueness and nondegeneracy of the collision come for free.**
- (Fc) shows that Δ has exactly one zero in X_F, and that it is simple. So the collision is the **only** branch point of the two roots in A_F × X_F, and its nondegeneracy is re-proved independently of the F_q and F_αα enclosures of 51.1.
- α* = p₁(x*)/2 could be certified to far more than the stated ±1.5·10⁻¹⁰, for example by a 2×2 Krawczyk on (F, F_α). Numerically, p₁/2 = −0.569714080972362 at x*.

**23. UNDERSTATEMENT: part of the partner branch is already certified** (L358 lists the partner as "(N)").
- The fold patch proves that the partner is real, simple and distinct from α_h on [X_c − 2⁻⁸, x*), since Δ > 0 there.
- The same tiling method would certify the whole partner branch on (0, x*) if applied to a normalisation that is regular at α = −1, such as (1 + α)G or F itself.

**24. UNDERSTATEMENT: status of Theorem 51.2.**
- Theorem 51.2 is **unconditional**. It is a statement about the zeros in the order α of I′_α(2√x), and uses no NS-00 input and none of the continuation's unverified inputs (2.3) or (20)–(24). Its only physical input is the quantisation condition (16) (Dirichlet data at the cutoff, ingoing at the horizon).
- The note gives it no status class (L9–15).
- *Fix:* label it, for example "E✓ (computer-assisted, unconditional)". State it once as a theorem about Bessel functions. This separates it cleanly from the conditional NS results.

**25. UNDERSTATEMENT: the natural normalisation and a comparison with ADGS** (L204–207, L213–215).
- With the Unruh temperature T at the cutoff, (w, q) = (ω, ck)/(2πT). These are exactly the variables (𝔴, 𝔮) of Grozdanov–Kovtun–Starinets–Tadić.
- ρ_c = 2ν/c is the relation ν = ħc²/(4πk_BT), that is η/s = ħ/(4πk_B) for a fluid with ε = 0 and ε + p = sT (sympy check).
- So the result reads: the Rindler shear critical point is at real 𝔮*² = 0.606020 and imaginary 𝔴* = −0.569714i. This is directly comparable with the complex critical points of GKST.
- *Test of ADGS's relation D = ω_eq/k_eq²:* here |ω*|/(ν k*²) = |α*|/(q*²/2) = 1.8802. The relation fails by a factor 1.88, because the higher gradient terms are O(1) at the collision.

**26. UNDERSTATEMENT: the elementary mechanism behind the collision.**
- The telegraph model (Maxwell–Cattaneo, or Müller–Israel–Stewart type) calibrated with the exact k → 0 data (D = 1/2 and a relaxation rate of 1 in units of c/ρ_c) is w² + iw − q²/2 = 0, that is α² + α + 2x = 0.
- It has the same collision pattern, at 𝔮² = 1/2 (x = 1/8) and α = −1/2, and its hydrodynamic branch is −2x − 4x² − 16x³ − …
- The exact problem dresses this to (0.6060, −0.5697), with branch −2x − 3x² − (29/3)x³ − …
- This makes the "level crossing at real momentum" of L214 concrete and explains why it sits roughly halfway down to the first Matsubara mode.
- *Optional reading:* the q → 0 limits sit exactly at Matsubara frequencies, where zeros and poles of H = I_α/(qI′_α) meet; compare pole-skipping (Blake–Davison–Vegh, JHEP 01 (2020) 077).

**27. UNDERSTATEMENT: Proposition 51.4 can say more with no new input.**
- Against Leray's L^p lower bounds for every p > 3, the construction's L^p lower bound holds with margin τ^{−h(1+1/p)}. As p → ∞ this is statement (3).
- For p_h < p < 3 (p_h = 2.96 at h = 1/200), the construction's **subcritical** L^p norms blow up, although no criterion requires this. This is a distinctive feature worth stating.
- Proposition 51.4(2) bounds the disk mean, avoiding the axis, where (5.42) is not available. This is a strength over the addendum's axis identity (item 18) and should be said.

---

## Summary table

| # | Label | One line |
|---|---|---|
| 1 | OK-CHECKED | evaluator and tail bounds valid; matches Bessel, ₀F₁ and series |
| 2 | MINOR | the claimed mpmath check of (51.1) is not in the shipped script |
| 3 | OK-CHECKED (+MINOR) | Krawczyk logic correct; the "translate" step and Brouwer need spelling out |
| 4 | OK-CHECKED | exact audit: coverage, 168,301 pairs, one inclusion suffices, no rounding gaps |
| 5 | OK-CHECKED | all 42,650 Krawczyk conditions re-verified with an independent library |
| 6 | OK-CHECKED | realness and origin arguments |
| 7 | OK-CHECKED | fold patch independently re-verified; Δ′(x*) = −4κ² |
| 8 | OK-CHECKED (+MINOR) | conclusions (a)–(d) correct; add connectedness and α_h < 0 lines |
| 9 | MINOR | "converges exactly for \|q²\| < q*²" is false: the series also converges on the circle |
| 10 | OK-CHECKED | Theorem 51.1 |
| 11 | OK-CHECKED | coefficients and ratio numerics reproduced independently (to k = 320) |
| 12 | OK-CHECKED (conversion) | CMST k⁴ conversion correct; the text of eq. (6.3) itself not verified |
| 13 | OK-CHECKED (+MINOR) | Unruh/Matsubara correct; the "at q = 0 exactly … as q → 0" wording |
| 14 | OK-CHECKED (+MINOR) | (H1)–(H4) faithful; cite p.124 for (H3); (H2) is a reading of "Fix" |
| 15 | OK-CHECKED | every step of bridge §§3–5 |
| 16 | OK-CHECKED | Proposition 51.4 exponents |
| 17 | MINOR | margins not uniformly τ^{−h}; "exactly" should be "at least"; speculative reading; automatic criteria |
| 18 | MINOR | the non-abelian axis growth rests on a workbench source, not on (H1)–(H4) |
| 19 | OK-CHECKED | D1 |
| 20 | OK-CHECKED (+MINOR) | citations correct; add CSTY II pages, Seregin 2012, GKST JHEP 2019; soften ADGS |
| 21 | UNDERSTATEMENT | Darboux asymptotics, unique boundary singularity, Σa_k x*^k = α* |
| 22 | UNDERSTATEMENT | (Fc) gives uniqueness and nondegeneracy of the collision; α* can be sharpened |
| 23 | UNDERSTATEMENT | the partner is already certified real near x*; the method extends |
| 24 | UNDERSTATEMENT | Theorem 51.2 is unconditional; label its status |
| 25 | UNDERSTATEMENT | (w, q) = (𝔴, 𝔮) of GKST; η/s = 1/4π; ADGS ratio 1.88 |
| 26 | UNDERSTATEMENT | the telegraph (MIS-type) model gives the same collision at (1/2, −1/2) |
| 27 | UNDERSTATEMENT | L^p margins for all p > 3; blowup of subcritical L^p norms; advantage of the disk mean |
