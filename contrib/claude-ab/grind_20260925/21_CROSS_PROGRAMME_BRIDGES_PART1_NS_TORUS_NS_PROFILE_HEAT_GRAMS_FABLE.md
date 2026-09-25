# Cross-programme bridges, part 1: where the programmes reuse each other's results

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 09:55 UTC. Revised 10:51 UTC after the seventh referee pass (§11).

This begins board task 2 (goal 2 of the owner's four). The owner reported that the ChatGPT/Codex lanes reuse results across Navier–Stokes (NS), Yang–Mills (YM), "Elpo G's S¹ work", zeta and Erdős–Straus (ES). The task is to find the concrete places where one programme's lemma is used in another, and to state each reuse as a typed morphism: its domain, its codomain, the map, the hypotheses, and what is and is not transferred.

**Sources inspected** (public repositories, read in the cloud workspace; nothing was changed in them):
- `erdos-straus-foundation`, commit `d20b32e1547aee2f08b440d56cceb47ab16dc4b7`;
- `yang-mills-interacting-workbench`, commit `fa79faff2cd697e16cfa3a7953f36810c22c8922` (it also holds the NS and S6 folders);
- `zeta-function-research-reader`, commits `42d00e359b16d52ca71568ce5e3db5341949d929` and `128aa308dd2a70ba6e073816a957d1ee6414ba2c`, the revisions that the ES and YM files cite.

The NS manuscript itself (*Finite Time Blowup for Navier–Stokes*; per the ES attribution record its title page names OpenAI as author) was not read. Edges 1, 3 and 4 below use no theorem of it. Edge 2 imports, through the programme's reconstruction of the NS construction, the blowup-rate lower bounds (250) and a dissipation bound; §2 says exactly where they enter.

**Checks.** Every algebraic or numerical claim that I call checked is in `checks/cross_programme_bridges_part1_checks.py`, with output in `checks/cross_programme_bridges_part1_checks_OUTPUT.txt`. The code is my own.

## 0. The reuse edges found

| # | Edge | What crosses | Status here |
|---|---|---|---|
| 1 | NS → ES | the integer matrix J = [[3,1],[1,5]] of the NS auxiliary torus, its eigen-directions and directional operators | read in full; the algebra and both examples checked (§1) |
| 2 | NS → YM | the NS velocity field, embedded as a reducible SU(2) connection; its enstrophy becomes magnetic curvature mass | read in full; the curvature identity and the free-state constants checked (§2) |
| 3 | zeta → YM | the split-zero "heat comparison" lemma (a Gram sandwich from a relative column error), instantiated with the YM heat semigroup | the zeta lemma HM10–HM14 read; the lemma and its YM instance checked on random matrices (§3) |
| 4 | the Jacobian polynomial F → zeta, YM and the owner's ES/Fable preprint; a four-dimensional analogue P in the ES crosswalk | F: det DF = −2, not injective; P: det DP = −2, eight-point generic fibres over a quartic | F's determinant, collision and symmetry checked; det DP and the ES quartic identities checked (§4) |
| 5 | S⁶ → YM, and S⁶/heat → NS | the S⁶ period matrix Π(z), used to build a YM connection | located only (§5) |
| 6 | ES ↔ zeta | the split-zero semiring G(R) and a finite Weyl basis; different Connes–Consani papers cited on the two sides | the zeta side of G(R) read and its proof checked by hand (§6) |

The owner's remark in M6, that the NS blowup happens "at zero", has an exact form in the terminal variable τ and its Mellin transform. It is in §7.

## 1. NS → ES: the auxiliary torus and exact arithmetic aliasing

**Source.** ES, `research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/torus_cover_lemma.tex` (labels `thm:ns-directional-intertwining`, `thm:ns-torus-fibres`, `thm:ns-torus-average`, `prop:ns-torus-powers`, `lem:ns-finite-dual`, `thm:ns-es-packet`, `cor:ns-es-cover-repair`), and `reverse_smooth_inverse.tex` (`thm:ns-sharp-denominator`). They cite the NS manuscript, §6.1, equation (6.2) on p. 63, and Lemma 6.2, equation (6.19) on p. 67. In the source's own words, the proofs "do not use a Navier–Stokes existence or blowup theorem".

**What crosses.** Only an operator:
- J = [[3,1],[1,5]], with det J = 14;
- the eigen-directions v_r = (1, 1−√2) and v_t = (√2−1, 1), with J v_r = (4−√2)v_r and J v_t = (4+√2)v_t;
- the torus map Φ(x, y) = (3x+y, x+5y) on 𝕋² = ℝ²/ℤ², and the directional derivatives D_v = v·∂.

**The typed morphisms** (all proved in the source; checks A1–A6):

1. *Pullback and intertwining.* P_m f(Y) = f(J^mY) on trigonometric polynomials satisfies D_vP_m = λ^m P_mD_v, with λ = 4 ∓ √2. On a Fourier mode this is the identity v·((J^m)^T n) = (J^m v)·n = λ^m (v·n) (check A2).
2. *Restriction to N-torsion.* J_N on (ℤ/N)² has kernel of size g = gcd(N, 14) and image {(a, b) : g | 5a − b}, of size N²/g (check A3, all N ≤ 60, by brute force).
3. *The finite character group.* For a finite abelian group G, the map J_G(χ, ψ) = (χ³ψ, χψ⁵) on Ĝ² is the restriction of the block torus map Φ^{⊕s} under an explicit coordinate embedding E: Ĝ → 𝕋^s.
4. *The arithmetic packet.* On an original ES shell (p = 12h + 1 prime, h ≥ 1, 3h + 1 ≤ a ≤ 9h, R = 4a − p) put G = U(R). Primality gives gcd(a, R) = 1, so every prime factor of a is a unit mod R (source lines 363–373; for p = 25, a = 10 one would get R = 15 with gcd 5). The coefficient c_a(g) counts the divisors of a² in the class g mod R. It is the mean of the packet function F_{a,g}(χ) = χ(g⁻¹)∏_{ℓ|a}Σ_{e≤2v_ℓ(a)}χ(ℓ)^e over Ĝ.

**Proposition 21.1 (exact aliasing; ES `thm:ns-es-packet`, (T12) and (T15)).**
- For every function f on Ĝ², the mean of f∘J_G equals Σ_{u∈G, u¹⁴=1} f̂(u, u⁻³), where f̂(u, v) = |G|⁻²Σ_{α,β∈Ĝ} f(α, β)·conj(α(u)β(v)).
- For two packets on the same group, where every prime factor of b is also a unit mod R, the joint mean of F_{a,g}(χ³ψ)F_{b,h}(χψ⁵) over Ĝ² is Σ_{u¹⁴=1} c_a(gu)c_b(hu⁻³).

The whole content is one group identity: {(u, v) ∈ G² : u³v = 1 = uv⁵} = {(u, u⁻³) : u¹⁴ = 1}. Substituting v = u⁻³ into the second equation gives u⁻¹⁴ = 1. Check A4 confirms the identity for all U(R) with R ≤ 300. Check A6 evaluates the joint mean with explicit characters on the non-cyclic group U(15) = ⟨2⟩ × ⟨14⟩ and matches the aliasing sum to 2·10⁻¹⁶.

**Negative result 21.2 (joint averages do not transfer on unchanged finite torsion; ES `cor:ns-es-cover-repair`).** Take the shell p = 13, a = 4, R = 3.
- The divisors 1, 2, 4, 8, 16 of a² = 16 have residues 1, 2, 1, 2, 1 mod 3, so c(1) = 3 and c(2) = 2.
- Both original targets, −4⁻¹ and −a, equal 2 in U(3).
- The joint mean (T15) is 2·2 + 3·3 = 13, whereas the independent count is 2·2 = 4.
- At the second power, J² = [[10,8],[8,26]] has first-row gcd 2, and (T16) gives c(2) + c(1) = 5 against the original 2.

Check A5 recomputes all of these with the two characters of U(3). The repair (T17) averages over the complete preimage H_m ⊂ 𝕋^{2s} of the embedded character group D = E₂(Ĝ²) under (J^m)^{⊕s}, which has 14^{ms}|G|² points. There every target occurs exactly 14^{ms} times, and the original counts 2 and 4 come back at every cover level. Fibre counting proves it.

**Lemma 21.3 (a sharp Diophantine constant; ES `thm:ns-sharp-denominator`, results entry R07).** For v = v_r or v_t and every nonzero k ∈ ℤ²,

  |v·k|·‖k‖₂ > 1/√(4+2√2), and inf_{k≠0} |v·k|·‖k‖₂ = 1/√(4+2√2) = 0.3826834….

*Proof (the source's, checked).*
1. With w_r = (1, 1+√2) and w_t = (−1−√2, 1), and k = (m, n): (v_r·k)(w_r·k) = (m+n)² − 2n² and (v_t·k)(w_t·k) = (n−m)² − 2m². These are norm forms of ℤ[√2], nonzero integers for k ≠ 0, so |v·k|·|w·k| ≥ 1.
2. Cauchy–Schwarz gives |w·k| < √(4+2√2)·‖k‖, strictly, because w has irrational slope.
3. With p_j + q_j√2 = (1+√2)^j, the Pell vectors k_{r,j} = (p_j − q_j, q_j) for v_r and k_{t,j} = (q_j, q_j − p_j) for v_t give |v·k|²‖k‖² = 1/(4+2√2) + (1+√2)^{−4j}/(4−2√2), which tends to the bound.

Checks A7: the factorizations (S2) symbolically; the Pell values; and a search over |k|_∞ ≤ 1500. Double precision cannot order the best candidates, whose excesses over 1/c are of order 10⁻¹³ to 10⁻¹⁴, so the 12 candidates within 10⁻⁶ were recomputed at 60 digits. The exact minimiser in the box is ±(408, 985) for v_r and ±(985, −408) for v_t (Pell index 9), with excess 1.85·10⁻¹⁴; every candidate lies strictly above 1/c. Strictness in general rests on the proof, not on the search.

*Reading.* The NS auxiliary operator is an expanding toral endomorphism of degree 14 whose eigenvalues 4 ± √2 lie in ℚ(√2). Its inverse directional derivatives have small divisors governed by the unit group of ℤ[√2]: Pell's equation. This is where the fluid construction touches arithmetic. The ES bridge uses exactly this, and no fluid theorem.

## 2. NS → YM: the NS profile as a curvature source

**Source.** YM, `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/released_profile_measures_addendum.tex`, §§1–4, equations (250)–(266).

**The map.**
- *The connection.* A divergence-free velocity field u_ν(s, x) from the NS construction goes to the reducible SU(2) connection A₀ = 0, A_i = λu_{ν,i}T, with T = −iσ₃/2 and −2 tr T² = 1.
- *The curvature.* All components share one Lie generator, so [A_i, A_j] = 0 and F_{ij} = λ(∂_iu_j − ∂_ju_i)T. The gauge-invariant magnetic density is h^B = −2Σ_{i<j}tr F_{ij}² = λ²|curl u_ν|², and the electric density is h^E = λ²c⁻²|∂_su_ν|².
- *The lattice.* The densities are sampled at edge midpoints, I_{L,a}h, and fed into the programme's operators D_{L,a,g}[h] and centred vectors Ξ = (D − ⟨ψ_g, Dψ_g⟩)ψ_g.

Check B1 verifies the curvature identity symbolically for arbitrary u.

**Hypotheses.**
- *The NS input.* The lower bounds (250), ‖curl u_ν(1−τ)‖₂² ≥ ν^{3/2}C_Ωτ^{−1/2−3h} and ‖∂_su_ν(1−τ)‖₂² ≥ ν^{5/2}C_{u̇}τ^{−3/2−3h} for 0 < h < 1/100 and small τ = 1 − s. These are blowup-rate bounds of the NS construction, imported from the programme's "source reader and its endpoint continuation" (addendum lines 8–16). The finiteness ∫₀¹𝒦_B < ∞ uses the positive-viscosity dissipation bound (line 55). I have not checked either. The NS workbench records its own analytical validation as unfinished, including "imported profile … existence" (NS `RESEARCH_STATE.md`, line 47).
- *Where they enter.* Item 1 below and the application in §7 depend on (250). Items 2 and 3 do not: they hold for any admissible weight.
- *Imported from YM sections I did not read.* The free norm formula behind (259)–(260), the energy estimate (261) and the positive-coupling convergence theorem.
- *The YM side.* The YM equation that results is sourced: D^μF_{μν} = g²j_ν with an explicit current j ≠ 0, given in (256)–(257). It is not a source-free YM solution, and the source says so.

**What is proved in the source.**
1. *Divergence of curvature mass.* The magnetic and electric curvature masses diverge as τ ↓ 0, with ∫₀¹𝒦_B ds < ∞ and ∫₀¹𝒦_E ds = ∞ (254)–(255). Check B4 is a consistency check of the exponents: −1/2 − 3h > −1 exactly when h < 1/6, and −3/2 − 3h < −1 always. The finiteness itself comes from the dissipation bound.
2. *A free zero-quotient bound.* For every nonzero, nonnegative, compactly supported curvature weight, the free energy-to-norm quotient is at most 72/(π⁴t⁹C_{R,t}), which is asymptotic to 32/t (260)–(262).
   - Exactly, C_{R,t} = 9P(7, t/(2R))/(4π⁴t⁸), with P the regularized lower incomplete gamma function. So the bound (262) equals 32/(t·P(7, t/(2R))) ≥ 32/t.
   - Check B2: for R = 1, C_{R,t}·4π⁴t⁸/9 = 1.00000000 and the quotient times t/32 = 1.00000000 at t = 100, 1000 and 10⁴.
   - At t = 10 the asymptotic regime has not started: the ratios are 0.238 = P(7, 5) and 4.205 = 1/P(7, 5).
   - Check B3: the support bound |ĥ(k)| ≥ H/2 for |k| ≤ 1/(2R) holds on an explicit bump, with minimum ratio 0.986.
3. *The diagonal transfer.* A diagonal sequence along the programme's weak-coupling path (L_j = j², a_j = (100j)⁻¹, g_j → 0) has energy-to-norm quotient at most 32/n + o(1/n) (263)–(265).

**What is not transferred (the source's own §§3–4).** The couplings g_{j_n} tend to 0. At a fixed coupling g₀ the dictionary gives ξ₀M_{L_j} → ∞ (addendum line 210), so the small-interaction regime used by the diagonal is unavailable. In the source's words, (265) is "a rigorous weak-coupling counterexample candidate, not a completed Millennium disproof".

**Scope limit 21.4.** The free quotient bound (260)–(262) holds for every nonzero, nonnegative, compactly supported weight. The diagonal (263)–(265) works verbatim with one fixed such weight. So the NS profile is one admissible weight; what it adds is the divergence of the curvature mass H_s along s ↑ 1, while the quotient bound does not depend on H_s (addendum line 164). The zero-quotient sequence exists only on the weak-coupling path g → 0. At fixed coupling, the source's exact calculation "neither proves nor rules out a different non-Abelian state with a vanishing physical quotient" (line 210). Whether such a state exists is open. (The map (251)–(258) itself is exact.)

**Notation.** The letter τ in this source is the NS terminal variable 1 − s. It is not the owner's τ, the pivot of the swing.

## 3. zeta → YM: the split-zero heat comparison

**Source.** YM, `yang-mills/consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260921-heat-response-transfer/RH_HEAT_TRANSFER.md`, §§T1–T3. It states that it read HM6–HM14 and HM19–HM24 of the zeta programme's `HEAT_TO_ORIGINAL_QUOTIENT_METRICS.tex` (zeta revision 128aa30, 19 September), and HG6–HG10 of `ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.tex`. I read HM10–HM14 in that revision.

**What crosses.** Not a map between zeta objects and gauge fields: the transfer says that "a source-specific map between arithmetic zeta packets and physical gauge fields is not asserted". What crosses is one Hilbert-space lemma.

**Lemma 21.5 (the shared interface).**
- (a) If a column map is perturbed with relative error δ ∈ [0, 1], that is ‖(Φ_J − Φ)x‖ ≤ δ‖Φx‖ for every x, then (1−δ)²Φ*Φ ⪯ Φ_J*Φ_J ⪯ (1+δ)²Φ*Φ. The source assumes δ < 1. For δ > 1 the lower bound fails: Φ_J = 0 satisfies the hypothesis with δ = 2, but (1−2)²Φ*Φ ⪯ 0 is false (check E1'). This is the triangle inequality. The same bounds pass to quotient minima, by completing the square over the same coefficient fibres.
- (b) In the zeta source, the relative error is δ_{N,J} = 2^{−(J+1)/2}c_N: a Schur constant times the dilation factor s^{−1/2}, with s = 2^{J+1} (HM11, HM13). For a positive definite Gram G = [[G₁₁, G₁₂], [G₁₂*, G₂₂]] with H = G₁₁ − G₁₂G₂₂⁻¹G₁₂* > 0, the largest eigenvalue of G^{−1/2}diag(0, G₂₂)G^{−1/2} is c² = 1 + ‖H^{−1/2}G₁₂G₂₂^{−1/2}‖² (HM10). (The source names the blocks A, C, S; they are renamed here because A denotes the YM operator in (c).)
- (c) In the YM instance, the relative error comes from the heat semigroup. For A ≥ a₀ > 0, C_T = I − e^{−TA}, Φ_T = C_TΦ and ε = e^{−Ta₀}: (1−ε)²Φ*Φ ⪯ Φ_T*Φ_T ⪯ Φ*Φ, and (1−ε)²Φ*AΦ ⪯ Φ_T*AΦ_T ⪯ Φ*AΦ. In YM, a₀ = 27κ/10 on the programme's fixed box (T2)–(T7).

Checks: E0 confirms (b) on 200 random Grams (relative error 1.4·10⁻¹³), E1 confirms (a) for δ ≤ 0.6 and E1' the failure for δ = 2, and E2 confirms (c), all on random matrices. In (c), (1−ε)² is sharp, because the spectrum of C_T lies in [1−ε, 1).

*Reading.* The zeta programme's heat replacement and the YM heat semigroup are two instances of one Gram-sandwich lemma. The arithmetic dilation there and the physical semigroup here each supply a relative error of their own. No arithmetic constant is assigned to a YM bound, as the transfer states.

**A small source typo.** In HM10 (line 179 of that revision) the block matrix is typed `\begin{pmatrix}A&C\ C^*&S\end{pmatrix}`, with `\ ` where `\\` is meant. It renders as one row; the repository's own PDF shows the single row. The proof uses the intended 2 × 2 block form. The referee found a second typo, in HM19 (line 305): `preceq` without its backslash, which prints as the word.

## 4. The Jacobian polynomial as a hub: zeta, YM and ES

**The object.** The YM workbench's `ATTRIBUTION.md` (line 9) identifies the polynomial historically called "Fabel/Jacobi" with the Jacobian-conjecture counterexample announced by Levent Alpöge on 20 July 2026. It records that the announcement "credits Akhil for the question and Fable for the work producing the example", and it names Tao's exposition (21 July 2026) as a separate source (line 19). The map is:
- F₁ = (1+xy)³w + y²(1+xy)(4+3xy);
- F₂ = y + 3x(1+xy)²w + 3xy²(4+3xy);
- F₃ = 2x − 3x²y − x³w.

Check F: det DF = −2, and the three points (0, 0, −1/4), (1, −3/2, 13/2) and (−1, 3/2, 13/2) all map to (−1/4, 0, 0). I verified these facts on 23 September in the FLIP_FABLE note, which I wrote for the owner; it also shows two further things. F is 3-to-1 off a discriminant surface. The real symmetry F(λx, y/λ, w/λ²) = (F₁/λ², F₂/λ, λF₃) carries the fibre over (−1/4, 0, 0) to the fibre over every (c, 0, 0) with c < 0 (check F repeats the symmetry). So the collision is generic, not special to −1/4.

**Where it is used.**
- *zeta side.* My FLIP_FABLE note for the owner (23 September; orientation branch, `FLIP_FABLE_FIBRE_AND_POSITIVITY.md`).
- *YM.* The material-tensor transfer (`FABEL_TENSOR_TRANSFER.md`, before equation (102)) and its addenda. Located, not read.
- *ES.* F itself is used in the owner's ES/Fable C123 preprint (`es_fable_c123_preprint.tex`, whose lines 2300–2430 treat the complete fibre over (−1/4, 0, 0); FLIP_FABLE §1, which read that range).
- *ES, a separate map.* The ES–Fable–zeta crosswalk (`research/incoming/es-fable-zeta-bridge-20260920/ES_FABLE_ZETA_CROSSWALK.tex`) uses a different, four-dimensional map P: ℂ⁴ → ℂ⁴ (EZ4, crosswalk lines 121–133).
  - P also has constant Jacobian determinant −2 (check C4).
  - Its generic fibre has eight points: two signs over each simple root of the normalized quartic h_u (crosswalk lines 458–500). F's generic fibre consists of the three simple roots of a binary cubic (Tao's marked-factor description; FLIP_FABLE §2).
  - The crosswalk cites The Clankers' "ES–Fable inverse correspondence" for P (line 2036), and the C123 preprint for the constant-Jacobian chart (lines 1997–1998). It does not name Alpöge.

**Proposition 21.6 (the ES quartic; the source's "Exact coefficients and intrinsic prime" and "Coefficient hypersurface").** For a solution of 4/p = 1/x + 1/y + 1/z, put S = p + x + y + z and H_ES(U,V) = −S⁻¹(U − pV)(U − xV)(U − yV)(U − zV). Then:
- u₀ = −1/S, u₁ = 1, u₂ = −(p(x+y+z) + xy + xz + yz)/S, u₃ = 5xyz/S and u₄ = −pxyz/S;
- p = −5u₄/u₃;
- 625u₀u₄³ − 125u₃u₄² + 25u₂u₃²u₄ − 4u₃⁴ = 0.

The factor 5 comes from p(xy + xz + yz) = 4xyz, the ES equation times pxyz, so that e₃ = 5xyz. The reciprocal transform H_rec = u₄⁻¹V(U − V)⁻¹H_ES(pV, U) equals −V(pV − xU)(pV − yU)(pV − zU)/(xyz), with roots U/V = p/x, p/y, p/z and ∞. Checks C1–C3 verify all of this symbolically on the ES variety, and verify the witness (13; 4, 18, 468).

**Scope.** I checked the quartic identities only. The eight-sheet cover, its monodromy of order 48, and the conductor bridge are the source's claims. The source itself states that these bridges "neither prove universal Erdős–Straus existence nor identify arithmetic roots with zeros of the Riemann zeta function". The same ATTRIBUTION.md separates this polynomial from the S⁶ construction of §5, which was also labelled "Fable" in older files.

## 5. S⁶ → YM, and the transfers into NS

**Identification (my reading of the name).** The owner's "Elpo G's S¹ work" is, on the evidence of the YM workbench's `s6/README.md` and `ATTRIBUTION.md`, most likely the S⁶ programme: the complex-threefold construction circulated by Levent Alpöge and produced with Claude (`alpo.ge/s6.pdf`). "Elpo G" would be Alpöge, and "S¹" would be S⁶. This is my inference from the files, not confirmed by the owner.

**Located edges.**
- *S⁶ → YM.* The imaginary-period block of the regular-fibre period matrix Π(z) = [[6μ, τ, 1, 0], [β, μ, 0, 1]] (ATTRIBUTION.md line 39) is used to build a connection, its frame changes and magnetic link transports (`ym_gap_primary_20260908/magnetic_translation_true_vacuum.md`, §1, equations (1.2)–(1.4); `retained_cusp_nonlinear_bridge.md`, §1). Here τ(z) is a period, not the owner's τ.
- *S⁶ and heat → NS.* The NS workbench's research state says that the programme "initially investigated transfers from algebraic, S6-related and heat-flow constructions into fluid equations" and that "their proposed implications are not certified by this reader".

Neither edge is examined further in this part.

## 6. ES ↔ zeta: shared structures and shared sources

**Shared structures.** The ES comparison note (`results/integration-2026-09-10/CROSS_WORKBENCH_COMPARISON.md`) finds two exact counterparts in the zeta workbench.
- *X3.* ES's support-sensitive semiring is the zeta programme's split-zero semiring G(R) = R ⊔ {τ}. I read the zeta side, `satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex` lines 13–88 at 42d00e3, `prop:gcue-coordinate-support`, and checked its proof by hand.
  - In G(R), τ is the semiring zero and e = 0_R is a second, supported element over the arithmetic zero; τ ≠ e.
  - Θ_R(τ) = (0, 0) and Θ_R(r) = (r, 1) give an isomorphism onto D_R ⊂ R × 𝔹.
  - The support character χ_RΘ_R is the only unital homomorphism to the Boolean semiring. The proof: f(e) = f(1) + f(−1) = 1 in 𝔹, and re = e forces f(r) = 1.
  - ES's results entry R01 ("two different zero layers in a precise semiring") is the ES statement of the same separation of absence from a supported zero.
- *X6.* A finite Weyl phase-space basis, per the comparison note fully covered by the zeta source `prop:finite-weyl-coordinate-isomorphism`. Not read by me.

**Common authors, different papers.**
- ES cites Connes–Consani, *Hochschild homology, trace map and zeta-cycles* (Prop. 3.1, eq. (3.2)), and *Cyclic theory and the pericyclic category* (§7.4, Lemma 7.7, Prop. 7.8) (ES `LITERATURE.md`, lines 15–16).
- The owner's second-attempt programme (`01_`) uses Connes–Consani's twistor line (arXiv:2609.00299). The public zeta literature chapter (`satellites/10_literature_foundations.tex` at 42d00e3) cites neither of the two ES papers (checked by search).

These are papers by the same authors, not a transfer of one programme's lemma into the other.

## 7. The owner's "zero is where you can escape" (M6), in exact form

The owner recalled that in the NS result "things blow up at zero … At time one". Per the ES attribution record, the NS manuscript's Theorem 1.1 has zero initial velocity, a smooth compactly supported force, and lim sup_{t↑1}‖u(t)‖_∞ = ∞. Reading: in the terminal variable τ = 1 − s used by the YM transfer (§2), time one is τ = 0, so both of the owner's phrases can be read literally. (The owner's "zero" might also refer to the zero initial velocity u(·, 0) = 0 of that theorem.)

**Proposition 21.7 (Mellin abscissa of a terminal singularity).** Let f ≥ 0 be measurable on (0, τ₀], with f(τ) ≥ Cτ^{−α} on (0, τ₁] for some C > 0, α > 0 and 0 < τ₁ ≤ min(τ₀, 1). Put 𝓜f(σ) = ∫₀^{τ₀} f(τ)τ^{σ−1}dτ.
- (i) 𝓜f(σ) = ∞ for every σ ≤ α.
- (ii) If ∫₀^{τ₀} f dτ < ∞, then 𝓜f(σ) < ∞ for every σ ≥ 1.
- (iii) If both hold (which forces α < 1), the abscissa of convergence σ_c lies in [α, 1]. Without (ii) there is no upper bound: f = τ^{−0.53}e^{1/τ} satisfies the lower bound and has σ_c = +∞.

*Proof.*
- (i) On (0, τ₁], f(τ)τ^{σ−1} ≥ Cτ^{σ−α−1} ≥ Cτ^{−1}, since σ − α ≤ 0 and τ ≤ 1. The integral of τ⁻¹ diverges at 0.
- (ii) For σ ≥ 1, τ^{σ−1} ≤ max(1, τ₀^{σ−1}) on (0, τ₀]. ∎

Check D illustrates both regimes on the model f = τ^{−0.53} + τ^{−0.2}.

**Application (conditional on the programme's (250) and (255)).** For the magnetic curvature mass f(τ) = 𝒦_B(1 − τ), (250) gives α = 1/2 + 3h, and (255) gives ∫₀¹𝒦_B < ∞. So σ_c ∈ [1/2 + 3h, 1]. For the electric mass, α = 3/2 + 3h > 1 and ∫₀¹𝒦_E = ∞. So 𝓜𝒦_E(σ) = ∞ for σ ≤ 3/2 + 3h, and in particular at σ = 1.

**Reading (labelled as such).**
- In the ledger of `13_` §2(b), a local germ h(v) = κv^α at the origin v = 0 puts a pole of the Mellin transform at s = −α. That is the slot Z3/Z4: the pole position is minus the local exponent at the origin.
- The NS terminal singularity occupies the same pair of slots with a negative exponent. The singular data sit at the origin τ = 0 of the integration variable (Z3), and they bound the abscissa in the Mellin variable (Z4): 𝓜𝒦_B diverges for every σ ≤ 1/2 + 3h.
- A lower bound on f gives only a lower bound on the abscissa; the true σ_c could be larger (f = τ^{−0.53} + τ^{−0.9} has σ_c = 0.9). Neither gives a pole.
- In this sense, the owner's "zero is where the weird shit happens" (M6, verbatim) holds in both settings: the singular data sit at the origin of the integration variable.
- This is a statement about Mellin transforms. It does not say that the NS singularity is a zeta pole.

## 8. Items for the goals

- **Bridges (goal 2).**
  - Edges 1–3 are genuine reuses with exact interfaces. Edge 1 moves an integer operator from NS into ES counting. Edge 2 moves a fluid field into YM as a curvature source. Edge 3 moves a Gram-sandwich lemma from zeta into YM.
  - Edge 4: one polynomial map F appears in the owner's ES/Fable preprint, in the YM material-tensor transfer, and in the zeta-side FLIP_FABLE note; the ES crosswalk adds a four-dimensional analogue P with the same constant Jacobian −2.
  - In edges 1, 3 and 4, and in items 2–3 of edge 2, no deep theorem of one programme is a hypothesis of another: what crosses is an operator, a field or a Hilbert-space lemma. Item 1 of edge 2 imports the NS blowup-rate bound (250).
- **Negative results (goal 1).**
  - 21.2: joint averages do not survive restriction of the NS torus cover to unchanged finite torsion (13 against 4); the complete preimage repairs them.
  - 21.4 (a scope limit): the zero-quotient sequence exists only as g → 0 and uses the NS profile only as one admissible weight; a fixed-coupling state is open.
- **Lemmas that stand alone (goal 3).**
  - 21.1: the aliasing identity for (χ, ψ) ↦ (χ³ψ, χψ⁵).
  - 21.3: the sharp constant 1/√(4+2√2) for the √2 directions.
  - 21.5: the Gram sandwich from a relative column error, with its Schur-complement and heat-semigroup instances.
  - 21.7: the Mellin abscissa of a terminal singularity.
  - All are elementary; no novelty search was made.
- **F1 context (goal 4).** None in this part.

## 9. Checks

`checks/cross_programme_bridges_part1_checks.py`, output in `checks/cross_programme_bridges_part1_checks_OUTPUT.txt`:

| item | test | result |
|---|---|---|
| A1–A2 | eigen-relations of J; v·((J^m)^T n) = λ^m v·n, m ≤ 4 | exact |
| A3 | kernel, image and image size of J mod N, N ≤ 60 | all agree with (T2) |
| A4 | {(u,v): u³v = uv⁵ = 1} = {(u, u⁻³): u¹⁴ = 1} in U(R), R ≤ 300 | all 299 groups |
| A5 | shell p = 13, a = 4, R = 3 with explicit characters | c = (3, 2); (T14) = 2; (T15) = 13 against 4; (T16) = 5 |
| A6 | (T15) on U(15) = ⟨2⟩ × ⟨14⟩, 12 target pairs | max error 1.9·10⁻¹⁶ |
| A7 | (S2) symbolic; Pell values; search over \|k\|_∞ ≤ 1500 with the 12 best candidates recomputed at 60 digits | exact minimiser ±(408, 985) (v_r), ±(985, −408) (v_t), excess 1.85·10⁻¹⁴ above 1/√(4+2√2); none below |
| B1 | −2Σtr F_{ij}² = λ²\|curl u\|² for A_i = λu_iT | exact (sympy) |
| B2 | C_{R,t} ~ 9/(4π⁴t⁸) and the quotient ~ 32/t, R = 1 | ratios 1.00000000 for t ≥ 100 |
| B3 | \|ĥ(k)\| ≥ H/2 on a bump, \|k\| ≤ 1/2 | minimum ratio 0.986 |
| B4 | integrability exponents in (254)–(255) | h < 1/6; never |
| C1–C4 | ES quartic coefficients, intrinsic p, coefficient hypersurface, H_rec; det DP for the crosswalk's map P | exact on the ES variety; det DP = −2 |
| D | Mellin abscissa model | diverges at σ ≤ 0.53, converges at σ ≥ 0.6 |
| E0–E2 | Schur constant (HM10/HM13); Gram sandwich (and its failure for δ = 2); heat-semigroup instance | 1.4·10⁻¹³; all eigenvalue margins ≥ 0; counterexample confirmed |
| F | det DF = −2 and the three colliding points | exact |

## 10. Reading status

- **Read in full:** ES `torus_cover_lemma.tex`, `reverse_smooth_inverse.tex` (the theorem used), `ATTRIBUTION.md`, `CROSS_WORKBENCH_COMPARISON.md`, `LITERATURE.md`; YM `released_profile_measures_addendum.tex`, `ATTRIBUTION.md`, the NS `RESEARCH_STATE.md`, `s6/README.md`; `RH_HEAT_TRANSFER.md` §§T1–T3; zeta HM10–HM14 and chapter 14 lines 13–88.
- **Read in part:** the introduction and first sections of `ES_FABLE_ZETA_CROSSWALK.tex`; the owner's ES/Fable C123 preprint (three ranges, on 23 September, for FLIP_FABLE).
- **Located, not read:** `sieve_character_cover.tex` and `reverse_proof_transport.tex` (ES); `FABEL_TENSOR_TRANSFER.md`, `magnetic_translation_true_vacuum.md`, `retained_cusp_nonlinear_bridge.md` and the NS workbench bodies (YM repository); the S⁶ manuscript; the NS manuscript.
- **Next parts of task 2:**
  - the YM uses of the Jacobian polynomial and of Π(z);
  - the NS workbench's own heat and S⁶ transfers;
  - the local folders `quantum_tau_programme_bridge_20260924` and `cyclotomic_clock_transfer_20260924` on the owner's computer.

## 11. Revision after the seventh referee pass (10:51 UTC)

An independent referee checked every item against its source and with its own scripts. It confirmed the core algebra: Propositions 21.1 and 21.6, the constant of Lemma 21.3, the curvature identity, the C_{R,t} constants, the Schur constant and the heat sandwich. It also confirmed that all extracted source copies are byte-identical to the cited revisions. Its findings, all applied:

1. **Lemma 21.5(a)** was false as stated without δ ≤ 1. The hypothesis is added, with the counterexample.
2. **§4** cited the wrong map for the ES edge. The crosswalk's P is a separate four-dimensional map (det DP = −2, eight-point fibres); F itself is used in the owner's ES/Fable C123 preprint. The attribution lines are added.
3. **Edge 2** does import the NS blowup-rate bound (250) and the dissipation bound. The introduction, §2 and §8 now say where.
4. **21.4** was an overstatement. It is now a scope limit: the NS profile is one admissible weight, and a fixed-coupling state is open.
5. **§7:** the Mellin reading had the direction inverted and conflated the slots Z3 and Z4. Corrected; the owner's M6 phrase is now quoted verbatim, and the reading is labelled.
6. **Check A7:** double precision cannot order the candidates. The candidates are now recomputed at 60 digits, and the exact minimiser is named.
7. **Lemma 21.3:** the proof for v_t (w_t and k_{t,j}) is added.
8. **Proposition 21.7:** the interval [α, 1] needs ∫f < ∞; a counterexample without it is added.
9. **Lemma 21.5(b):** the relative error is 2^{−(J+1)/2}c_N; positive definiteness is stated; the block names no longer clash.
10. **§1:** "p prime, h ≥ 1", the unit condition on the factors of b, and the normalisation of f̂ are added.
11. **Attribution:** the announcement's credits and Tao's exposition are recorded. FLIP_FABLE is my note for the owner, not the owner's material.
12. **§6:** "shared sources" became "common authors, different papers", with locators.
13. **§7:** "weird stuff" is replaced by the owner's words; "both descriptions hold" is labelled as a reading, with the alternative (zero initial velocity).
14. **Minor:**
    - the ξ₀M → ∞ locator (line 210);
    - B4 described as a consistency check;
    - the preimage in 𝕋^{2s} of D = E₂(Ĝ²);
    - the imaginary-period block of Π(z);
    - the imported, unread YM sections;
    - the exact form C_{R,t} = 9P(7, t/2R)/(4π⁴t⁸);
    - the second typo at HM19.
