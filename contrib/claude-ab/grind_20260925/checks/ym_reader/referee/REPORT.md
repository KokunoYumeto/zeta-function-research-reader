# Referee report on *The Yang–Mills workbench: a reader of its results, with proofs* (version of 26 September 2026, 25 pages)

Referee: an independent Claude instance (claude-opus-5-5) that wrote none of the reader. Report of 27 September 2026 (finished 04:47 UTC), returned as text (subagents cannot write report files here) and saved in substance by claude-ab. Check programs and their outputs are in `checks2/` in this folder; `checks/` holds the programs of an earlier referee attempt that was cut off before it wrote a report.

Sources used:
- the record, Zenodo 10.5281/zenodo.22883643 (43 files), and the repository at commit fa79faf;
- both proof manuscripts in full (FIFTH_REFERENCE.md, F1–F42; HEAT_AND_COMPLEMENT.md, H1–H34), ROUTE_ASSESSMENT.md, and every record passage the reader cites;
- the reader's two scripts, rerun: outputs byte-identical.

Page numbers refer to ymreader.pdf; `file.tex:N` is the source line.

**Summary.** As far as checked line by line, the mathematics of Sections 3–4, Proposition 5.1 and Proposition 7.1 is correct. No error invalidates a stated result. The main problems run in the other direction:
- the audited threshold is understated: the reader's own audited order-2 data give g² ≥ 3.9781, not 4.0187 (Finding 1);
- the heat prefactor 67896/169 of Theorem 4.1 can be replaced by 2829/13, by an inequality the reader itself states (Finding 2);
- an independent, numerical computation of the order-3 coefficient norms lowers the threshold to g² ≥ 3.7154 with no computed workbench input beyond order 1 (Result A);
- several results follow in a few lines from the reader's material but are not stated: a gap at complex coupling with an analyticity radius uniform in the box (B), a matching upper bound on the gap (C), and the gap on the full space (E).

## Findings

**1 (MAJOR). The audited threshold is understated.**
- Location: abstract p. 1 (y0_front.tex:13); Theorem 3.1 status p. 8 (y3_gap.tex:22); Corollary 3.5(b) and status pp. 10–11 (y3_gap.tex:68, 72); p. 11 (y3_gap.tex:77); §9.1 item 3 (y9_open.tex:8); Appendix A (yA_catalogue.tex:12).
- The status of Theorem 3.1 reports the exact values m(v₂) = 134.07… and t(v₂) = 19.80… recomputed by the first-pass audit, but Corollary 3.5(b) uses the workbench's larger pair (5834/39, 137/6) = (149.59, 22.83).
- Evidence: v₂ = B(v₁, v₁) recomputed with explicit SU(2) tensors (`r2_su2_blocks.py`, `r2_order2_exact.py`). Of the 42 adjacent pairs whose label contains the anchor link, 28 have block norms (16, 48) and 14 have (8, 24√3). The squared singular values are 1, 9, 4, 12 with multiplicities 16, 16, 4, 12 (`r2_order2_singular_values.py`). Exactly:
  - m(v₂) = 6 + 11200/117 + 112/9 + 448√3/39 = 134.0673186784…;
  - t(v₂) = 3/2 + 80/9 + 256/39 + 64√3/39 = 19.7953312398…;
  - identical at x-, y-, z-anchors; ‖v₂‖_loc = 212.33…; agrees with audit 46a_.
- With m₂ ≤ 1340674/10⁴, t₂ ≤ 197954/10⁴ (√3 < 1.7321), Corollary 3.5 with N = 2 gives α₂ = 0.0157977…, i.e. g² ≥ 3.97807…, d₂(α₂) = 1.52055, d₂(1/64) = 1.64707 (`r2_order2_threshold.py`). The benchmark g² = 4 is covered by audited inputs.
- Fix: state g² ≥ 3.9781 with Δ_L ≥ 1.5205κ, and 1.647κ at g² = 4, with the closed forms; keep 4.0187 as the value from the workbench's pair; in the abstract, "checked in the first-pass audit" (46a_) instead of "checked independently here".

**2 (MAJOR). Proposition 4.2(c) and Theorem 4.1: the prefactor is (1+255χ)/(1−χ) = 2829/13.**
- Location: step (i) p. 12 (y4_heat.tex:31); Prop 4.2(c)–(d) and proof p. 13 (y4_heat.tex:49–50, 57–62); Theorem 4.1 p. 12 (y4_heat.tex:24); "Other radii" p. 14 (y4_heat.tex:69); Prop 4.4; catalogue.
- Step (i) states |py| + ‖Ty‖_X ≤ χ‖y‖_X but then bounds |(μ − P_H)F| by ‖p‖‖S‖‖Q_H F‖ ≤ χ‖Q_H F‖/(1−χ), discarding the additive structure.
- Proof: for y ∈ X₀ and z = Sy, z = y + Tz, so |pz| ≤ χ‖z‖ − ‖Tz‖ ≤ χ(‖y‖ + ‖Tz‖) − ‖Tz‖ = χ‖y‖ − (1−χ)‖Tz‖ ≤ χ‖y‖. Hence |(μ − P_H)F| ≤ χ‖Q_H F‖_X, and ‖μ‖ ≤ 1 for every χ < 1. With ‖Q_HΓ‖_X = ‖Γ‖_X − |P_HΓ|: |μΓ(h_τ, G_z)| ≤ (1−χ)|P_HΓ| + χ‖Γ‖_X ≤ ((1−χ)/8 + 32χ)‖Kh_τ‖_X, giving (1+255χ)/(1−χ)·e^{−3(1−χ)τ}.
- With χ < 11/24: 2829/13 = 217.62 against 67896/169 = 401.75 (ratio exactly 13/24). With χ(1/55) = 0.454125: 213.97 against 391.98. Randomised test of the lemma on ℓ¹(n): max ‖pS‖/χ = 0.685 (`r2_heat_sharpening.py`).
- Carried through H14–H30 (with Findings 3–4), C_J = 782.29, and the table of Proposition 4.4 improves (`r2_improved_table.py`): g² ≥ 10: fraction 0.9778 → 0.99458, η_E 1.057·10⁻² → 5.712·10⁻³, η_G 1.122·10⁻² → 6.052·10⁻³; g² ≥ 13: 0.99904 → 0.99977, 4.36·10⁻⁴ → 2.362·10⁻⁴, 4.50·10⁻⁴ → 2.439·10⁻⁴; g² ≥ 16: 0.99991 → 0.999981, 3.56·10⁻⁵ → 1.933·10⁻⁵, 3.64·10⁻⁵ → 1.974·10⁻⁵.
- Fix: add the lemma; state 4.2(c) with (1+255χ)/(1−χ) and 2829/13 (the old constant remains valid); C(R) = (1+255χ_R)/(1−χ_R) in "Other radii"; recompute Prop 4.4. (The earlier unfinished attempt had (1+256χ)/(1−χ) = 2840/13.)

**3 (MINOR). Proposition 4.3(a): observed fraction ≥ 1 − β/(9l₂).**
- ‖(I − P_R)Φc‖² ≤ ‖Φc − Rc/3‖² = c*Jc/9 ≤ β|c|²/9 and ‖Φc‖² ≥ l₂|c|².
- Values at g² ≥ 10, 12, 25/2, 13, 16: reader 0.9778, 0.9975, 0.9984, 0.99904, 0.99991; new 0.98996, 0.99889, 0.99932, 0.99958, 0.999965.
- Fix: state (a) as the maximum of the two bounds.

**4 (MINOR). The kinetic-row constants 30 and 48.**
- Γ(W_p, W_p) = 3 − χ₁(U_p) (F17) and ‖χ₁(U_p)‖_X = 27 (F12, d = 3): 30 is exact.
- Adjacent p ≠ q: Γ(W_p, W_q) = (3/4)P₀ − (1/4)P₁ (Casimirs 9/2, 13/2); norm 24 for 8 of 12 neighbours, 6 + 6√3 ≈ 16.39 for 4; never 48.
- Row sum exactly 30 + 192 + 24 + 24√3 = 287.57 against 606; with Finding 2 the row is at most 3 + (11/24)(27 + 216 + 24√3) = 133.43.
- Fix: derive 30 and 48 in the text, and remove them from the unchecked inputs (y4_heat.tex:121; y9_open.tex:15).

**5 (MINOR). §9.1 (y9_open.tex:7) attributes "cannot move the source domain past α₅" to the workbench.** ROUTE_ASSESSMENT.md re-centres only the single-norm order-1 certificate (‖v₁‖_loc ≤ 32, ‖B‖ ≤ 2/3) and returns R₀ = 3/256 = α₁. Fix: say so; the α₅ question is open (J).

**6 (MINOR). Status labels.** Theorem 4.1 "Audited" although the semigroup construction and continuation were "read and standard" and the result depends on unchecked order 3–5 inputs: "Conditional; audited in part". The catalogue uses undefined labels ("Implied", "Gap implied", "Checked symbolically", "Not audited", "Superseded; located", …). Fix: map to defined labels.

**7 (MINOR). "The factor 255 is derived here" (y4_heat.tex:53).** The 21 September heat reader already derives 32 (U28), the 1/8 rule and ‖Ĉ‖_row ≤ ((1+255χ)/(1−χ)²)e^{−3(1−χ)τ} (U29a, p. 36); H11 restates it. Fix: credit U28–U29a.

**8 (MINOR). "Superseded" omits U29b** (heat reader p. 37: radius 45/4096, prefactor 6184/25, rate 15/8). As ξ → 0 the ratio of Theorem 4.1's right side to U29b's is (67896/169)/(6184/25)·(55·45/4096)⁶·e^{τ/4} = 0.0790·e^{τ/4}, so U29b is sharper for τ > 10.15; only the "Other radii" family supersedes it (at R = 45/4096: rate 2.2588, prefactor 112.9, or 85.0 with Finding 2).

**9 (MINOR). Proposition 3.4 omits ‖Kh′‖_X < ∞** (y3_gap.tex:55): eigenvectors are smooth, so Σ_j c_j‖A_j(h)‖₁ < ∞ on the finite product (F36). Add one sentence.

**10 (MINOR). Lemma 3.3 is stated for real v but used at complex coupling** (y3_gap.tex:39; y4_heat.tex:15, 38–42). The proof is algebraic; only positivity needs v real. State it for complex v.

**11 (MINOR). "The other twenty are only on Zenodo" (y2_corpus.tex:24).** Five of the twenty are byte-identical to members of archives committed at fa79faf (AI_READING_INDEX.md, READER_PROVENANCE.json, SOURCE_MANIFEST.json in yang_mills_current_sources_2026-09-09.zip; ALPOGE_ATTRIBUTION_20260921.md, YM_READING_GUIDE_20260921.md in yang_mills_heat_volume_reader_sources_20260921.zip); none occurs as a blob in the 44 commits (`r2_zip_scan.py`).

**12 (MINOR). The order-5 replay** (y3_gap.tex:22; yB_verification.tex:12). INTAKE_REVIEW.md reports 30 supplied runs whose hashes were matched but which were not repeated at intake. Write "a replay which the publication intake did not repeat".

**13 (MINOR). The attribution file's "not a hypothesis" statement** (y0_front.tex:33; y6_side.tex:3) is about the 21 September heat and volume proofs. That F1–F42 and H1–H34 do not use the Jacobian map or S⁶ follows from reading them. Reword.

**14 (MINOR). Missing credits: Yarotsky and Baez** (y0_front.tex:32; y1_problem.tex:22–28; y5_earlier.tex:30, 52–58). The quantum line's first volume-uniform gap (its (77)) uses Yarotsky's creation method and Baez's spin networks (quantum_coarse_graining.pdf p. 19); the README credits both.

**15 (MINOR). The reader's script is described as doing more than it does.** In `ymr_heat_constants.py` the constants 8, 32, 1/8, 30, 48 are checked as arithmetic of the manuscript's formulas (lines 30–35, 79); the "path scope" check is `check(…, True)` (line 115); at g² = 13 the agreement is to ten decimals, not eleven. Fix the descriptions (y0_front.tex:49; yB_verification.tex:34; Prop 4.4 status) and remove the vacuous check.

**16 (MINOR). Notation.** "δ = e^{−Ta₀}" in the §8 table (y8_overlaps.tex:13): a₀ is undefined and clashes with the lattice spacing of Prop 3.6 (the reader's quantity is ε = e^{−κd_ph T}); "H7" is both an equation and a section. Rename.

## Missed and implied results (proved or computed by the referee; claude-ab to verify)

**A. Order 3 computed independently (numerical).** v₃ = 2B(v₁, v₂) computed directly by summing over splits with B(f,h) = Σ_{b′}(c_f + c_h − c_{b′})/(2c_{b′})P_{b′}(fh) (F17), by Clebsch–Gordan contraction and SVD. The 612 anchored labels (4 self, 84 repeated, 460 path, 40 common-edge, 24 corner) fall into 22 classes under 12 orientation-preserving point maps. m(v₃) = 1203.1424168…, t(v₃) = 127.2886523…, ‖v₃‖_loc = 1965.1583644…. Checks: label counts equal C22/Q12; reconstruction error ≤ 3·10⁻¹⁵; invariance under the 12 maps; fast path equals the general split sum on three classes; the record's e₄ = 5M/216 − 2J/1053 reproduced exactly; t = Σ m_type/n_type; self cluster 40/27. With (m₁,t₁) = (64/3,16/3), (m₂,t₂) = (1340674,197954)/10⁴, (m₃,t₃) = (12031425,1272887)/10⁴, Corollary 3.5 with N = 3 gives α₃ = 0.018111…, g² ≥ 3.71533, d₃ ≥ 1.53319 there, d₃(1/64) = 1.90235, d₃(4/225) = 1.65712. Consequences: F26's (1611.59, 180.35) and C23's 944984/351 are valid upper bounds; L17's 3.8260 rests on checked inputs (3.7651 with the exact order-2 values); with F26's orders 4–5, N = 5 gives 3.6626 and 1.919κ at g² = 4. Record erratum: the web continuation (p. 153) justifies C21's self bound by an arithmetic line whose left side equals 12/5, not 40/27; the value 40/27 = 8/27 + 32/27 is correct.

**B. A spectral gap at complex coupling; analyticity radius uniform in L.** For |ζ| ≤ α_N: H_L(ζ)e^{v(ζ)} = E₀(ζ)e^{v(ζ)} with E₀ analytic; every other eigenvalue has Re(λ − E₀) ≥ κd_N(|ζ|); E₀ is algebraically simple. Proof as in Prop 3.4 using |c_j − λ/κ| ≥ c_j − Re λ/κ; simplicity by applying Q_H then P_H to the generalized-eigenvector equation. Kato type (A) gives an analytic Riesz projection in |ζ| < α_N for every L (compare 3/(4M_L) ≤ 1/320 from Prop 7.1).

**C. A matching upper bound.** Δ_L ≤ κ(3 − ⟨χ₁(U_p)⟩_ρ)/(1 + ⟨χ₁(U_p)⟩_ρ − ⟨W_p⟩_ρ²) (trial vector r_p, F3, W_p² = 1 + χ₁). With the widths of §4.3, Δ_L/κ ≤ (3 + w_K)/(1 − w₀): at g² ≥ 10, 13, 16 the gap lies in [2.8383, 3.0125], [2.9047, 3.00053], [2.9372, 3.000045]. The first-order coefficient of Δ_L vanishes at each L (∫W_pW_qW_r = 0). Open C′: Δ_L ≥ κ(3 − cξ²) uniformly?

**D. The sharper heat constants for every 0 < R ≤ α₅**, with prefactor (1+255χ_R)/(1−χ_R): 213.97 at 1/55, 241.99 at α₅, 85.00 at 45/4096.

**E. The gap on the full space:** Δ_L^full ≥ κd_N(ξ)/4, sharp at ξ = 0 (3κ/4). The record states N = 1 (G27, web continuation p. 66).

**F. The sharp per-link constant in Lemma 3.2:** γ_e = min(g_e, 1 + (ℓ_u + ℓ_w)/2), attained; LP-checked on ten graphs (`r2_girth.py`).

**G. Proposition 3.6 quantified:** at most 1 + ⌊(2√α₅ − g₀⁻²)/(β log 2)⌋ path points in the domain; with the one-loop β = 11/(3π²) (identification g_W² = 4g², conditional), at most two.

**H. Small facts:** C₀(τ) = e^{−3τ}I; coefficient bounds ‖[ξ^{2n}]Ĉ(τ)‖_row ≤ (2829/13)55^{2n}e^{−13τ/8}.

**I. (Conditional) exponential clustering** if H34's locality holds.

**J. (Open) re-centring beyond α₅.**

**K. (Open) exact certification of order 3; order 4 needs a spin-network implementation (8,621 anchored multisets).**

## Checked and found correct

Both scripts (byte-identical reruns; inventory 23 + 19 + 1; page counts of 14 PDFs; 43 files); Theorem 3.1's numbers (threshold 3.683551983985727; d₅ values); Lemma 3.2 (proof, count 1,012 on Q₃, LP optima on eight graphs); Lemma 3.3 and Proposition 3.4 (subject to Finding 9); F7, F9, F10, F28, F31; Corollary 3.5's constants; Proposition 3.6; Theorem 4.1 and Proposition 4.2 (steps (i)–(iv), 32, 1/8, 255, 67896/169, evenness on 240 faces, Lumer–Phillips); Propositions 4.3–4.4 and §4.4; Proposition 5.1 (ξ ≤ 1/49152 ⇔ g₀⁴ ≥ 12288); Proposition 7.1 (§27 of the spatial line); §6 (det DF = −2, three preimages, flow, tr T² = −1/2); the descriptions of the record; §8 (ATTEMPTS.md line 274; research-attempts.json lines 915, 918; the Collatz fixture; δ ≤ 1).

## Not checked

The order-4 and order-5 inputs (F14–F25); the inherited heat data C₂, C₄ and the row bounds; H25, H31–H32, H34 (read only); H6 accepted as standard; the 8–9 September and 14–19 September editions beyond the cited passages; per-version file lists (no network); the four-workbench reader, the global S⁶ statement, the imported NS theorem and the literature.
