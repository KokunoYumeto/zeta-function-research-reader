# GDE and ABH: the Gaussian energy of the boundary, its determinants, and the boundary in Noor's Hardy space

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 13:23 UTC. Board task 8 (programme audit and lemma extraction), the second and third of the eight new result groups of the 25 September bulletin. Not yet refereed.

## 0. Sources, scope and checks

All four files are in the programme's working folder `quantum_tau_programme_bridge_20260924` and were read in full:

- GDE0–GDE13, `GAUSSIAN_DEFECT_ENERGY_AND_DETERMINANTS.md`: 637 lines, SHA-256 `2aee949f…149dae6d`.
- GDR0–GDR5, `GAUSSIAN_DEFECT_ROOT_REVIEW.md`: 87 lines. The GDE hash it records equals the one above.
- ABH0–ABH8, `ACTUAL_BOUNDARY_HARDY_RECEIVER.md`: 338 lines, SHA-256 `9774d207…d101ff7b`.
- AHR0–AHR9, `ACTUAL_BOUNDARY_HARDY_RECEIVER_REVIEW.md`: 323 lines. The ABH hash it records equals the one above.

**Later copies.** The copies of these four files in the continuation folder `next_edition_after_647` (file times 01:11 UTC) were compared line by line after removing carriage returns:
- ABH, AHR and GDR are identical;
- GDE differs only in the verification paragraph under GDE7.6, where inline formulas are set as displays.

So this audit covers the current text.

**Not read.**
- GAP, ADM and GTAH, on which GDE builds.
- NHD, NHR, CTS, FST, QTI and ACC, which ABH lists.
- Noor's paper. ABH7 and AHR8 use Noor's unconditional theorem 𝒩^⊥ ∩ 𝒟_{δ₁} = {0} (arXiv:1809.09577v4). I take that theorem as cited; I did not read the source.

**Checks.** `checks/gde_abh_audit_checks.py`, 12 items, all pass (`_OUTPUT.txt`). Three items failed on the first run because of my test settings; none of the three was a mathematical failure:
- item 2 substituted floats into a symbolic identity and then demanded 10⁻²⁵ accuracy;
- item 4 demanded 10⁻⁹ agreement at the end δ → 0, which the grid approaches only to O(δ²) ≈ 10⁻⁷;
- item 7 used a relative tolerance of 10⁻¹², below the double-precision rounding of differences of nearly equal powers, which is about 4·10⁻¹².

After the tolerances were corrected (exact rationals in item 2), all three pass.

**Verdict.** Every displayed identity and estimate of GDE and ABH that I checked is correct, and GDR and AHR are accurate reviews. I found no error. There is one notational point (§1.4) and one bound that can be sharpened (§1.5).

## 1. GDE: what it computes, and the checks

**Setting.**
- H = ℓ²(𝒵, m) over the distinct nontrivial zeros, with weights m_ρ.
- 𝖩 is the reflection x_ρ ↦ x_{ρ#}, where ρ# = 1 − ρ̄.
- D_r is diagonal with d_r(ρ) = e^{−iγ log r}(r^σ − r^{1−σ}), and G_t is diagonal with e^{tρ²}.
- The operator studied is B_{r,t} = D_r^*𝖩G_t.

In the orthonormal basis e_ρ/√m_ρ, B is block off-diagonal: it has one 2×2 block on each off-line pair {ρ, ρ#} and is zero on the line. Everything in GDE follows from this block structure. I verified the following.

**1.1 The products (GDE2, GDE5, GDE6; item 1).**
- B*B = diag(a) with a(ρ) = Δ_r(σ)²e^{2t(σ²−γ²)}, and BB* = 𝖩(B*B)𝖩.
- B² = −M_c with c = Δ_r²e^{t(σ²+(1−σ)²−2γ²)}e^{2iγ(log r + t)}.
- B*𝖩B = −G*P_r𝖩G, where P_r = D_r^*D_r.
- det(I + zB) = ∏_{pairs}(1 + z²c), and Tr B = Tr_ζ B = 0.
- All of these are checked on a synthetic finite divisor with four off-line pairs and three line points, with multiplicities. Every identity is algebraic in the coordinates, so the synthetic set tests them exactly.

**1.2 Degree covariance (GDE7; item 2).**
- BT_n = U_n^*B and BU_n = T_n^*B.
- P_r = T_rT_r^* + U_r^*U_r − 2r.
- The reflected-trace identity GDE7.2a holds.
- The closed form GDE7.6 holds exactly: on an off-line pair, 2m nΔ²e^{−2tγ²+t/2+2tδ²}[cosh(2δ(t + log n)) − cosh(2tδ)].

**1.3 Estimates and limits (GDE9–GDE11; item 5).**
- |e^{tρ²} − 1| ≤ te(1 + γ²) and |e^{2t(σ²−γ²)} − 1| ≤ 2te²(1 + γ²), for 0 < t ≤ 1 and 0 < σ < 1.
- The commutator limit is (BB* − B*B)/t → M_{2Δ²(1−2σ)}.
- Δ_r(σ)²/(r(log r)²) → 4δ² as r ↓ 1.
- The trace limit (GDE10.2) follows by monotone convergence: e^{−2t}a increases as t ↓ 0. I checked this by hand.

**1.4 A notational point in GDE8.3 (and ABH0.2).**
- The formula F₀(−2k) = k(2k+1)(−1)^kπ^k ζ′(−2k)/(2k!) must be read with 2k! = 2·(k!), not (2k)!.
- Item 3 checks k = 1, …, 5 against F₀ = ξ/4 to 10⁻³¹; the reading (2k)! fails at k = 2 by 83%.
- `25_` (check 3) already used the reading 2·r!.

**1.5 A sharper form of GDE11.2.** Write δ = σ − ½. The comparison quotient is exactly

  κ_{r,q}(σ) = √(r/q)·sinh(δ log r)/sinh(δ log q).

- Its exact range over 0 ≤ σ ≤ 1 lies between √(r/q)·log r/log q (at δ → 0) and (r − 1)/(q − 1) (at |δ| = ½). This is `24_` Lemma 24.5.
- GDE11.2's bounds 2√r log r/((q+1)log q) ≤ κ ≤ (r+1)log r/(2√q log q) hold. They follow from the Cauchy mean-value theorem, and they are strictly weaker than the exact range.
- Item 4 checks the formula, both bounds and the exact range for four pairs (r, q).

## 2. ABH: what it computes, and the checks

**Setting.** This is Noor's Hardy-space setting (arXiv:1809.09577v4, as cited by ABH):
- g_s(z) = Σ_j \overline{φ_j(s)} z^j, with φ₀ = −1/s and φ_j = (j^{1−s} − (j+1)^{1−s})/s;
- the cover W_nf(z) = (1 + ⋯ + z^{n−1})f(z^n);
- 𝒩 = span{h_k : k ≥ 2}.

ABH attaches the programme's boundary β_r to this Hardy space.

**2.1 The Hardy facts (ABH1; items 6–8).**
- ‖g_s‖² ≤ 1/(2Re s − 1). Item 6 computes the sum to 2·10⁶ terms and adds a tail bound, for four values of s. The coefficient identity behind Noor's isometry, (j+1)q(j) − jq(j+1) = a_s(j) with q(j) = j^{1−s̄}/s̄, is checked symbolically.
- W_n^*g_s = n^{1−s̄}g_s, including the first block.
- ⟨h_k, g_s⟩ = (1 − k^{1−s})ζ(s)/s. Item 8 checks this to relative error below 10⁻¹⁰, for k = 2, 3 and s = 0.7 + 3i, 0.8 + 21i.
- So g_λ ∈ 𝒩^⊥ at every zero λ with ½ < Re λ < 1.

**2.2 The uniqueness lemma (ABH2; item 9).** This is the heart of ABH. Put ψ_j = φ_j + 8F₀/s; it is entire, because 8F₀(0) = 1. Every continuous functional on the strip space ℬ that kills all g_tψ_j is zero. The proof has five steps:

1. **Telescoping.** Σ_{j<n} ψ_j = (8nF₀(s) − n^{1−s})/s.
2. **An entire function of order 2.** L(w) = Λ[g_t(e^{(1−s)w} − 8e^wF₀)/s] is entire of order ≤ 2 and vanishes at w = log n for every n ≥ 1.
3. **Jensen's formula.** It gives L ≡ 0: there are e^{R/2} zeros log n with n ≤ e^{R/2}, against O(R²) allowed.
4. **Removing the correction.** (∂_w − 1)L = −Λ(g_te^{(1−s)w}). So Λ kills every g_te^{vs}.
5. **Density.** The half-Mellin representation extends this to Λ(e^{us²}F) = 0 for u > t. Holomorphy in u, then u ↓ 0, gives Λ = 0.

I checked each step; item 9 checks steps 1 and 4 and the absence of a pole at 0.

**2.3 The receiver (ABH3–ABH6; items 10–12).**
- The receiver is 𝓛_{r,t}x = −Σ_{λ∈𝒵₊} m_λ d_r(λ) \overline{g_t(λ)} x_{λ#} g_λ.
- The bound Δ_r(σ)²‖g_λ‖² ≤ (r+1)²(log r)²/4 is uniform up to the critical line (item 10). Together with Σ_λ √m_λ e^{−t(Im λ)²} < ∞ (ABH3.6), it makes 𝓛 trace class.
- 𝓛 is injective and maps into 𝒩^⊥.
- 𝓛 factors as C₊B*_{r,t}.
  - ‖B*x‖² = ⟨BB*x, x⟩ is GDE's target energy, not the source energy ⟨Ax, x⟩ (AHR5 stresses this).
  - The Hardy norm carries the off-diagonal Gram terms K(λ, μ).
- The cover covariance is W_n^*𝓛 = 𝓛T_n. It gives nK − T_n^*KT_n = n𝓛*(I − P_n)𝓛, with the diagonal value (n − n^{2(1−σ)})·(…) > 0 (item 12).
- Iterating gives the all-scale identity ABH6.2 and the vector reconstruction ABH6.3.
- ABH6.3 is the elementary orthogonal decomposition attached to the isometry n^{−1/2}W_n. Item 11 checks it exactly on a window of length 3⁶. ABH says it makes no novelty claim for this decomposition.
- AHR7 strengthens both limits to trace norm. I checked the trace formula AHR7.2 and the domination argument.

**2.4 Noor's adjoint domain (ABH7, AHR8).** Every nonzero element of 𝒩^⊥ lies outside 𝒟_{δ₁} (Noor, unconditional; cited, not read by me). 𝓛 is injective with image in 𝒩^⊥. So 𝓛x ∈ 𝒟_{δ₁} forces x = 0.

## 3. Lemmas extracted

**Lemma 30.1 (two conditions implied by RH and read off the zero-time energy; GDE9.6 and GDE10.2).** Let r > 1 and P_r = D_r^*D_r, which is diagonal on H with coefficient Δ_r(σ)² at ρ = σ + iγ. Then:

- (a) P_r is compact iff the off-line zeros approach the critical line, that is, β − ½ → 0 along every sequence of distinct off-line zeros. This holds trivially if there are finitely many.
- (b) P_r is trace class for the divisor trace, Σ_ρ m_ρΔ_r(σ)² < ∞, iff Σ_ρ m_ρ(β − ½)² < ∞. For the ordinary trace, drop m_ρ.
- Neither condition depends on r.
- (b) implies (a): if Σ m_ρ(β − ½)² < ∞, then β − ½ → 0 along the off-line zeros.
- Both hold under RH, where P_r = 0.

*Proof.* With L = log r and δ = σ − ½, Δ_r(σ)² = 4r sinh²(δL). For |δ| ≤ ½, sinh(x)/x ∈ [1, sinh(L/2)/(L/2)] for |x| ≤ L/2. Hence

  4rL²δ² ≤ Δ_r(σ)² ≤ 4rL²δ²(sinh(L/2)/(L/2))².

- (a) A diagonal operator is compact iff its coefficients tend to 0 outside finite sets. The zero count is finite at bounded height, so "outside finite sets" means along |γ| → ∞.
- (b) The two-sided bound compares the two sums term by term. ∎

GDE9.6 states (a) with Δ_r², and GDE10.2 computes the limit trace in (b). The two-sided bound converts both into conditions on the zeros alone. I do not know of a proof of either condition without RH, and I make no claim about their status in the literature.

**Corollary 30.2 (the corrected tests are dense for every correction term; ABH2 follows from RSS1.2).** Let ℬ be the strip space and t > 0. Let Φ be an entire function with Φ(0) = 1 such that κ := g_t(1 − Φ)/s lies in ℬ; this holds, for example, when g_tΦ ∈ ℬ. Then

  closure span{g_t(s)(n^{1−s} − nΦ(s))/s : n ≥ 1} = ℬ.

- For Φ ≡ 1 this is RSS1.2 (audited in `16_`).
- For Φ = 8F₀ = 2ξ it is ABH2, because the partial sums of ABH's tests g_tψ_j are exactly these members (ABH2.3).

*Proof (the tenth referee pass pointed out this one-line route).* Put η_n = g_t(n − n^{1−s})/s. Then the n-th member is nκ − η_n, and η₁ = 0, so the first member is κ. Hence the span of the members is span{κ, η_n : n ≥ 2}, which contains span{η_n : n ≥ 2}. That span is dense by RSS1.2. ∎

*Remark.* ABH2's own Jensen proof also works for general Φ. There the Φ-term enters through the split L(w) = e^wΛ[g_t(e^{−sw} − 1)/s] + e^wΛ(κ). Note that g_tΦ/s alone is not in ℬ, since it has a pole at 0.

*Scope.* For the corrected tests, the correction term never affects density in ℬ. For the cover discrepancies it does: δ_n = 8F₀η_n has closed span I, while η_n has closed span ℬ (NJS10; `31_`, 31.N1). This matches `16_`: cover invariance recovers exactly the divisor that the section inserts.

## 4. Negative results (goal 1)

- **30.N1. Further quantities that vanish iff RH holds, each by construction.**
  - (i) The ordinary trace Tr_H A_{r,t} = 0 (GDE3.4). The divisor trace Tr_ζ A_{r,t} is not new: it is the same quantity as row 7 of the table in `25_` §5 (ECR5.5).
  - (ii) B_{r,t} is normal, for one or every t > 0 (GDE11.5). The two squares BB* and B*B have coefficients a(ρ#) and a(ρ), which agree iff σ = ½.
  - (iii) 𝓛_{r,t} = 0 (ABH3.5).
  - (iv) The degree-adjusted trace GDE7.6 vanishes.
  - Each condition says only that there are no off-line zeros, because each operator is built on the off-line coordinates. They join the eight rows of `25_` §5 and do not reduce RH to anything new.

- **30.N2. The cancellations attempted in GDE and ABH all leave the off-line sector intact.**
  - Cyclicity cancels only the antisymmetric part a(ρ) − a(ρ#) (GDE5.3).
  - The degree relation leaves the positive pair term GDE7.6.
  - The cover relation leaves n𝓛*(I − P_n)𝓛, which by ABH6.2 recovers the whole Hardy norm.
  - GDE12 and AHR9 draw the same conclusion themselves. I confirm it computationally.

- **30.N3. The adjoint-domain route is circular on this receiver (ABH7.1, with Noor's theorem as cited).** 𝓛_{r,t}x ∈ 𝒟_{δ₁} holds iff x = 0. So proving the regularity of the Hardy image is the same problem as proving that the off-line sector vanishes.

## 5. Bridges and context (goal 2)

- **GDE ↔ `24_`.** The comparison quotient κ_{r,q} of GDE11 is the AST defect ratio, whose exact range is `24_` Lemma 24.5 (§1.5 above).
- **GDE ↔ `25_` §5.** GDE3.4 is row 7 of that table; GDE11.5 adds normality (30.N1).
- **ABH ↔ `16_` (RSS, NCI, NHJ).** By Corollary 30.2, ABH2 is a consequence of RSS1.2.
  - The Jensen step used in RSS1, NCI3 and ABH2 is the same.
  - What `16_` transplanted from NCI8 into RSS1 is NCI8's sparse-family version (register S33).
  - The Hardy receiver of ABH is the NCI/NHJ receiver restricted to the reflected off-line boundary.

## 6. Not checked

- GAP, ADM, GTAH, NHD, NHR and Noor's paper (see §0).
- ABH's statement that its uniqueness proof was "developed jointly with an independent derivation". I have no way to check its provenance.
- The four source-endpoint factors (1, eᵗ, eᵗ, 1) of GDE8, which GDE takes from GAP7.

## 7. Check list (`checks/gde_abh_audit_checks.py`)

| item | content |
|---|---|
| 1 | GDE2.1–2.3, 5.5, 6.1–6.4 (products, square, determinant, traces) |
| 2 | GDE7.2–7.3, 7.2a, 7.6 |
| 3 | GDE8.3 special values of F₀; the reading 2·k! |
| 4 | GDE11.1–11.2 against the exact range (`24_` Lemma 24.5) |
| 5 | GDE9.2–9.3, 11.5, 11.6 |
| 6 | ABH1.2 norm bound; the coefficient identity behind Noor's isometry, symbolically and via the coefficients of T g_s |
| 7 | ABH1.4 cover eigen-relation |
| 8 | ABH0.3 Noor pairing (tolerance 10⁻⁹; errors about 6·10⁻¹¹) |
| 9 | ABH2.1–2.5 |
| 10 | ABH3.3 uniform near-line bound |
| 11 | ABH6.3 / AHR7.5 with W_n built as an explicit matrix |
| 12 | ABH5.3 sign; AHR7.2 decay factor (elementary) |

## Revision after the tenth referee pass (applied at 14:20 UTC)

- **Major.** §5 misattributed the Jensen step to `16_`. RSS1.2's own proof already uses Jensen's formula; what `16_` transplanted was NCI8's sparse version (register S33). Corrected.
- **Minor.**
  - Lemma 30.2 is now Corollary 30.2, with the one-line proof from RSS1.2 and the corrected hypothesis κ ∈ ℬ. The earlier proof sketch wrongly treated g_tΦ/s as an element of ℬ.
  - Its "Consequence" is restricted to the corrected tests. For the discrepancy families the section does change density (NJS10).
  - 30.N1(i): only the ordinary trace is new; the divisor trace is `25_` §5, row 7.
  - §2.3: ‖B*x‖² is the target energy, and the trace-class conclusion needs ABH3.6.
  - Lemma 30.1: added that (b) implies (a).
  - Checks: item 6 now tests the step from T to g_s numerically; item 8's tolerance was tightened to 10⁻⁹; item 11 builds W_n as an explicit matrix; item 12 is labelled elementary. All 12 pass.
