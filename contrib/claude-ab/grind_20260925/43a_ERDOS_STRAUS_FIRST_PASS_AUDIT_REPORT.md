# Erdős–Straus workbench: first-pass mathematical audit

Prepared by Claude (`claude-opus-5-5`), 26 September 2026, for the public reader of the Erdős–Straus (ES) workbench. Read-only: nothing in any repository was changed. Every script and output named below is in this folder.

Conventions:
- "WB" means the workbench's own label.
- "Verdict" is my finding.
- Quotations are under 15 words; everything else is paraphrase.
- A "witness" is a triple of positive integers (x, y, z) with 4/p = 1/x + 1/y + 1/z.

---

## §0 Sources, commit, method

**Repository.** `KokunoYumeto/erdos-straus-foundation`, `origin/main` = `d20b32e` ("Pin ES proof locators and publication receipts", 23 Sep 2026). This is the same commit used by the inventory and by `21_`. Files were read with `git show origin/main:<path>`.

**Read in full:**
- `RESEARCH_STATE.md`, lines 1–160;
- `README.md`, lines 1–420;
- `research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex`, lines 1–220;
- `first_two_shell_sieve.tex`;
- `counterexample_sieve/all_shell_no_hit.tex`;
- for item 4, `es-turn04-square-expansion-20260918/full/core.tex` (through the finite-enumeration section);
- for item 6, `es-turn06-full-shell-20260919/core.tex`;
- for item 7, `es-turn06b-pointwise-localization-20260919/pointwise_localization.md`;
- for item 14, `es-turn07-capacity-completion-20260920/core.tex` (to the obstruction theorem) and `CORRECTION.md`;
- for item 21, `es-turn07-divisor-descent-20260921/core.tex` (through the optimality proof);
- for item 22, `es-turn07-global-receiver-determinant-20260921/core.tex`;
- for item 23, `es-turn07-sharp-receiver-growth-20260921/core.tex`, lines 1–330;
- for item 26, `es-turn07-square-zero-pell-20260922/core.tex`, lines 33–130, 344–440 and 940–1072;
- `results/PROOF_NOTES.md` (R01–R10);
- `results/integration-2026-09-10/ARGUMENTS.md` (X1–X7);
- `research/continuation-2026-09-12/received/es_s6_counterfactual/src/core.tex` and `src/arithmetic.tex`, lines 1–150;
- `research/continuation-2026-09-12/README.md` and `CORRECTIONS.md` (head).

**Read at README level only** (statement and scope): items 1, 2, 3, 5, 8–13, 15–20, 24, 25, 27, 28.

**Reused.** The inventory `workbench_survey/WORKBENCH_SURVEY.md` §§0–1 and 8–10. The earlier audit `21_…FABLE.md` §1 (NS operator bridge, R07), §4 (the ES quartic and det DP) and §6 (G(R)). I do not redo those; I cite them.

**Method.**
1. For each audited statement I restate it with all hypotheses.
2. I follow the written proof step by step.
3. I write my own check. Exact integer or `sympy` arithmetic is used throughout. Floating point appears only in the explicitly marked singular-value and Fourier checks: `mpmath` at 60 digits, and `numpy` for X6.

**Scripts** (each has a `*_OUTPUT.txt`):

| Script | What it checks | Runtime |
|---|---|---|
| `check_core_reduction.py` | ES-01, ES-02, ES-03 and the elementary reductions | 59 s |
| `check_items_arith.py` | items 4, 6, 7, 14, 21, 26 | 65 s |
| `check_receiver_certificates.py` | items 22 and 23: symbolic certificates and a witness census | 156 s |
| `check_extras.py` | items 2, 3, 8; R02–R10; X5, X6; ES-08, ES-09; the mod-840 reduction | 2 s |

---

## §1 The core reduction (ES-01, ES-02, ES-03)

### 1.0 Definitions, exactly as the source gives them

- Fix h ≥ 1 with p = 12h + 1 prime.
- The shell range is A_p = {3h+1, …, 9h}.
- For a ∈ A_p, put R_a = 4a − p and S_a = pa.
- Then 3 ≤ R_a ≤ 2p − 3, R_a ≡ 3 (mod 4), and 0 < a < p (`bounded_transport.tex` L38–45).
- All divisors are positive.

The channels:

- **Exterior:** E_a = {u : u | a², R_a | 4u + 1}.
- **Middle:** M_a = {u : u | a², R_a | u + a} (L118–121).
- **Shell count:** q_a = |E_a| + ½|M_a|.
- **Total:** Q_p = Σ_{a∈A_p} q_a (L152–156).

In `all_shell_no_hit.tex`:

- **Exponent box.** B_a = ∏_{ℓ|a} {0, …, 2v_ℓ(a)}, with the bijection e ↦ U_a(e) = ∏ ℓ^{e_ℓ} onto Div(a²).
- **Packet.** F_{a,R_a} = ∏_{ℓ|a} (Σ_{e=0}^{2v_ℓ} [ℓ]^e) ∈ ℕ[U(R_a)], with coefficients c_{a,R_a}(g) = #{e ∈ B_a : U_a(e) ≡ g (mod R_a)}.
- **Chart.** For u in a channel: g = gcd(a, u), A = a/g, B = u/g, D = g²/u, and C = (A + p^{1−ε}B)/R_a. Here ε = 0 for E and ε = 1 for M.

### 1.1 ES-01: shell bijection (`lem:units`, L49–100)

**Statement.**
1. gcd(R_a, S_a) = 1.
2. The set 𝒲_a = {(m, n) ∈ ℤ²_{>0} : m | S_a, n | S_a, gcd(m, n) = 1, R_a | m + n} is in bijection with the ordered positive solutions (y, z) of 1/a + 1/y + 1/z = 4/p.
3. The map is (m, n) ↦ (a, (S_a/n)k, (S_a/m)k), with k = (m + n)/R_a.
4. The inverse takes the reduced fraction m/n = y/z = (R_a y − S_a)/S_a.

**Proof steps and my verdict on each.**
1. *Units.* Since 0 < a < p, gcd(a, 4a − p) = gcd(a, p) = 1, and gcd(p, 4a − p) = gcd(p, 4a) = 1. Correct.
2. *Forward map.* 1/y + 1/z = (m + n)/(S_a k) = R_a/S_a = 4/p − 1/a. Correct.
3. *Converse, first part.* From R_a yz = S_a(y + z) one gets d = R_a y − S_a = S_a y/z > 0 and (R_a y − S_a)(R_a z − S_a) = S_a². I re-derived the product identity by expansion. Correct.
4. *Converse, second part.* The reduced ratio d/S_a has exponents max(c_ℓ − b_ℓ, 0) and max(b_ℓ − c_ℓ, 0), where c_ℓ = v_ℓ(d) and b_ℓ = v_ℓ(S_a). Both are at most b_ℓ, so m | S_a, n | S_a and gcd(m, n) = 1. Also d ≡ −S_a (mod R_a); multiplying by the unit n/S_a gives m + n ≡ 0. Correct.
5. *Mutual inverses.* These follow from uniqueness of reduced fractions. The forward image has y/z = m/n, and a given ratio together with a given value of 1/y + 1/z fixes (y, z). Correct.

**Verdict: correct and complete.** It is the classical divisor parametrisation of 1/y + 1/z = R/S. The later packages attribute these coordinates to Elsholtz–Tao (§2, Propositions 2.2 and 2.6), and a reader should present it that way. RESEARCH_STATE L33 says the scope identities are "not advertised as new results".

### 1.2 ES-02: E/M count, biconditional, shellwise and global criteria

**Statement A (L123–133).**
- The ordered solution count with first denominator a is 2|E_a| + |M_a|.
- The unordered count is exactly |E_a| + ½|M_a|; in particular |M_a| is even.

**Proof, checked.**
- Write each residual divisor d | p²a² uniquely as d = p^i v with i ∈ {0, 1, 2} and v | a².
- *i = 2.* The gate d ≡ −pa (mod R_a) becomes R_a | pv + a. Multiplying by 4p⁻¹ (a unit, since R_a is odd) and using 4a ≡ p gives R_a | 4v + 1, that is, v ∈ E_a.
- *i = 0.* This is the complement d ↦ S_a²/d of the i = 2 case.
- *i = 1.* The gate becomes R_a | v + a, that is, v ∈ M_a.
- *Fixed points.* The complement swaps y and z. Its only possible fixed point is v = a in the middle case, which would give R_a | 2a, impossible.

Correct.

**Statement B (L150–174): ES(p) ⇔ Q_p > 0.**
- Necessity: choose the witness order with minimal first denominator a. Then 1/a < 4/p ≤ 3/a, so p/4 < a ≤ 3p/4. For p = 12h + 1 the integers in this range are exactly 3h+1, …, 9h. Lemma `lem:units` then gives a positive summand.
- Sufficiency: reconstruct the witness.

Correct.

**Statement C (`thm:shellwise-no-hit`, L79–233).**
1. A shell has no witness if and only if c_{a,R_a}(−4⁻¹) = 0 and c_{a,R_a}(−a) = 0.
2. The tagged domain 𝒯 = {(0, u, σ) : u ∈ E_a, σ ∈ {0, 1}} ⊔ {(1, u, 0) : u ∈ M_a} maps bijectively onto the ordered witnesses by (a, p^ε ACD, pBCD), with an optional swap.
3. The explicit inverse (10a) reads off i = v_p(R_a y − S_a).

I re-derived each of the following. All are correct:
- the chart exponents v − min(v, e), e − min(v, e) and 2min(v, e) − e;
- the gate equivalence A(4u + p^ε) ≡ p^ε(A + p^{1−ε}B);
- the identity 4ABCD = A + p^{1−ε}B + pC;
- the residuals (10b), R_a y₀ − S_a = p^ε a²/u and R_a z₀ − S_a = p^{2−ε} u;
- all three inverse branches.

**Statement D (`thm:global-no-hit`, L295–327).** The following are equivalent:
- the product 𝒪_p of indicators equals 1;
- E_a = M_a = ∅ for every shell a;
- Q_p = 0;
- no witness exists.

Hence a counterexample prime would satisfy a finite, computable condition (13). Correct; this is immediate from A–C.

**Verdict: correct and complete.** It is an exact finite criterion at each prime, not a positivity theorem. RESEARCH_STATE L66–68 states the same limit.

### 1.3 ES-03: residual-3 and residual-7 sieves (`first_two_shell_sieve.tex`)

**R3 (`thm:r3-factor-sieve`).**
- *Setting.* a = 3h + 1, so R = 3 and a ≡ 1 (mod 3).
- *Claim 1.* E_a = M_a = {u | a² : u ≡ 2 (mod 3)}, which is the set of exponent vectors whose exponent sum over the primes ≡ 2 (mod 3) is odd.
- *Claim 2.* |E_a| = |M_a| = P₁(P₂ − 1)/2, where P_i = ∏_{ℓ ≡ i (mod 3)} (2v_ℓ + 1).
- *Claim 3.* The shell has a witness if and only if a has a prime factor ℓ ≡ 2 (mod 3).
- *Claim 4.* For such ℓ the witnesses are (a, C₀D, pℓC₀D) and (a, pC₁D, pℓC₁D), with D = a/ℓ, C₀ = (1 + pℓ)/3 and C₁ = (1 + ℓ)/3.

Proof, checked:
- the parity count uses the alternating sum ∏(Σ_{e=0}^{2v} (−1)^e) = 1;
- evenness of |M_a| comes from the complement, whose fixed point u = a has residue 1 and so is absent.

Consistency, my arithmetic: a ≡ 1 (mod 3) forces Σ_{ℓ≡2} v_ℓ to be even, so P₂ ≡ 1 (mod 4) and the weighted count 3P₁(P₂ − 1)/4 is an integer. Correct.

**R7 (`thm:r7-factor-sieve`).**
- *Setting.* a = 3h + 2, so R = 7, and 7 ∤ a (otherwise 7 | p).
- *Discrete log.* In base 3 mod 7, λ(1, 2, 3, 4, 5, 6) = (0, 2, 1, 4, 5, 3).
- *Targets.* Exterior: residue 5 = 3⁵. Middle: u/a ≡ −1 = 3³, that is, Σλe ≡ b + 3 (mod 6).
- *Claim 1.* The channels are nonempty if and only if one of three predicates holds:
  - a has a prime factor ≡ 5 or 6 (mod 7);
  - n₃ ≥ 3;
  - n₃ ≥ 1 and n₂₄ ≥ 1.

  Here n₃ is the total exponent of primes ≡ 3 (mod 7) in a, and n₂₄ is the total exponent of primes ≡ 2 or 4 (mod 7).
- *Claim 2.* The counts are coefficients of F_a(T) = ∏_ℓ Σ_{e=0}^{2v_ℓ} T^{λ_ℓ e} in ℤ[T]/(T⁶ − 1).

Proof, checked:
- the sufficiency table (u = ℓ, aℓ, ad, aℓt, aℓ/t) has the stated residues;
- necessity splits into two cases. If n₃ = 0, all residues lie in the subgroup {1, 2, 4}, which contains neither 5 nor −1. If 1 ≤ n₃ ≤ 2 and n₂₄ = 0, the exponent ranges 0 ≤ e ≤ 4 and |e − n₃| ≤ 2 miss both targets.

Correct.

**Two-shell corollary.** Both shells fail exactly when both rejection conditions hold. The general chart (a, y, z) = (ABD, p^ε ACD, pBCD) with C = (A + p^{1−ε}B)/R_a is proved. Correct.

**Verdict: correct and complete.** These are elementary, and of the same kind as the classical identities. The worked examples (p = 13, a = 4; p = 373, a = 95; p = 37, a = 12) all reproduce.

### 1.4 Checks (`check_core_reduction_OUTPUT.txt`)

| Check | Range | Result |
|---|---|---|
| lem:units map vs brute force over y; 2\|E\|+\|M\| = ordered count; no y = z; \|M\| even; Φ and (10a) both directions | all 8,124 shells of all primes p ≡ 1 (mod 12), 13 ≤ p < 1000 | all pass |
| minimal denominator of every sorted solution lies in A_p (naive search, x ≤ 2p) | p ∈ {13, 37, 61, 73, 97, 109} | all pass |
| Q_p > 0 | all 300 primes p ≡ 1 (mod 12), p < 10⁴ | Q_p > 0 for all; the first occupied shell is always within 6 of the bottom (worst case p = 1201) |
| R3 formula and witnesses; R7 predicates, group-ring counts and table witnesses | all 19,564 primes p ≡ 1 (mod 12) below 10⁶ | all pass |
| two-shell survivors | same range | 989 primes; all ≡ 1 (mod 24); the first are 1129, 1201, 2521, … |

### 1.5 Which primes the frontier concerns

**What the workbench proves** (RESEARCH_STATE L11–36, checked in `check_core_reduction` §0 for all primes < 2·10⁵):
- p ≡ 2 (mod 3) is covered by (p, (p+1)/3, p(p+1)/3);
- p ≡ 3 (mod 4) is covered by ((p+1)/4, p(p+1)/2, p(p+1)/2);
- p ≡ 13 (mod 24) is covered by (a, pa/2, pa) with a = (p+3)/4, which is even.

So the workbench's own reduction leaves the primes p ≡ 1 (mod 24). Its shell maps are stated on the larger domain p = 12h + 1.

**What the workbench uses without proof in the texts I read.** Many later packages restrict to "hard primes", p mod 840 ∈ {1, 121, 169, 289, 361, 529}; for example DAILY_RESULTS_20260919 L230 and items 4, 21 and 26.
- These six classes are exactly the unit squares mod 840. My arithmetic: the unit squares form a group of order 1·1·2·3 = 6.
- The classical reduction to these classes is usually attributed to Mordell. It is not proved in the core texts I read. The workbench names it only indirectly, through its "Mordell-hard" citation titles in `es_pointwise_tranche/tranche.tex`.

**My check** (`check_extras`, "[840]").
- There are 24 unit classes c (mod 840) with c ≡ 1 (mod 24).
- The 18 non-square classes are each covered by an explicit polynomial family whose modulus divides 840. The families are of two kinds:
  - middle: 4/p = 1/(ABD) + 1/(pACD) + 1/(pBCD), with p = 4ABD − R and R·C = A + B;
  - exterior: 4/p = 1/(ABD) + 1/(ACD) + 1/(pBCD), with R·C = A + pB.
- The six square classes are not covered by any family in the search. I claim no impossibility beyond the families searched.
- The family identities were checked on sample primes.

**Reader wording:** "the classical identities reduce ES to primes p ≡ 1, 121, 169, 289, 361 or 529 (mod 840); the workbench proves the weaker reduction to p ≡ 1 (mod 24) itself."

---

## §2 The 28 structural items

**Common WB status** (DAILY_RESULTS_20260922 L679–686):
- the items are written proofs with Python replays;
- there is no Lean build and no independent human review;
- no item claims a proof or counterexample to ES.

The table uses these depth codes:
- **D**: read the proof and wrote an independent check;
- **Dc**: certificate or examples verified, proof read in part;
- **L**: README-level reading, with the proof file located (the `.tex` size in the folder is given).

| # | Statement (paraphrase) | WB label | Depth | Verdict |
|---|---|---|---|---|
| 1 | On first-half shells at p ≡ 1 (mod 4): exact three-target collision law, factor-cut inequalities, and every simultaneous E/M failure normal form of effective quotient order ≤ 8 (index-six normal form at a prime residual) | proved | L (39 KB tex) | Proof present; not checked. No recorded repairs. |
| 2 | All-edge transition and closure theorems for the shifted-factor graph. At p = 2521 the 7-cycle 11→211→683→89→17→643→113→11 is a sink with both local gates empty. | method counterexample ("not Erdős–Straus", README L57–58) | Dc | Sink **verified**: each canonical source has a unique nonresidue prime factor, the next vertex, and E = M = ∅ at all seven shells. p = 2521 has witnesses elsewhere, e.g. (636, 5611746, 70588). Closure theorems not checked. |
| 3 | At p = 7510085481569082811681 (≡ 121 mod 840), the canonical triangle 31→223→307→31 has E = M = ∅ at every vertex. A square-source escape holds for all-3-mod-4 triangles. | method counterexample plus proofs | Dc | Triangle **verified**: BPSW primality (not a certificate), unique simple successors, 1,215 divisor vectors all failing, and the multiplier-9 sources exit the triangle. The escape theorem was not read. |
| 4 | At every hard prime, every set of ≤ 5 nonresidue prime vertices has a valid source (p + σ_q q t²)/4, t ∈ {1, 3, 5, 7, 9}, with a nonresidue prime factor outside the set. Hence ≥ 6 vertices are reached within 25 factorisations. Height bound p < (4H)^m for closed sets of size m. | proved (computer-assisted) | D | See 2.4. Reduction proofs correct; exceptional cycles verified; my direct test finds no counterexample at hard p < 40,000. **The 5.9-million-profile enumeration was not re-run.** |
| 5 | For 4 \| a, u ↦ a/(4u) is an involution exchanging E and M gates on Div(a/4). The pair source 𝒫_R(N) has 2τ(h)-point fibres. Möbius return. The transported factor character is annihilated by \|1 + χ(p)\|². | proved | L (53 KB) | Proof present; not checked. |
| 6 | For p ≡ 1 (mod 4), p ≥ 2²⁰, Σ_{a∈I_p} L_a ≤ −(1/24) p log p (principal-only lower bound). Sublinear-mode versions. Integer collision bound; five of 23 even modes give T_a ≥ 60 at p = 944329, R = 47. | proved | D | See 2.6. **Correct**; all finite claims reproduce. |
| 7 | At p ≡ 1 (mod 8): least-nonresidue bounds on every middle and exterior state, e.g. 11a ≤ 3(p + 3) and 22(p + 1) ≤ 23(p − 2a + 1)² at hard p. Endpoint alternative. D-bound. Free Klein-four action. | proved; "does not prove that it is occupied" | D | See 2.7. **Correct**, including the three presentation repairs the WB records. |
| 8 | Middle identity p = RQ − (Q+1)²/(4A). With t = min(R, Q): 4p ≥ 3t² + 6t − 25, and at hard p 4p ≥ 3t² + 14t − 81. Complete direct/cofactor atlas. No fixed list of grades covers all hard primes. | proved; branch reduction | Dc | Identity and both bounds **verified** on 1,613 oriented middle states (p ≡ 1 mod 8 < 4000). Equality occurs at 41, and also at 761, 1193, 1721 and 3881; the WB cites 41 only and claims no uniqueness. Atlas not checked. |
| 9 | Exterior complement–norm atlas; strict cubic cutoff for min(residual, cofactor, complementary divisor); a sharp family | proved | L (44 KB) | Not checked. |
| 10 | Every diagonal E state (R = D) has an M state at the same p. At hard p, E shapes of radius ≤ 7 are one singular family, and radius 8 forces a u = 9 middle state. The cubic involution fails to preserve p. | proved; branch reductions | L (74 KB; has `PROOF_AUDIT.md`) | Not checked. |
| 11 | Each witness at p ≡ 1 (mod 12) gives the normalised quartic −S⁻¹∏(T − ℓ_i) with roots p, x, y, z. p = −5u₄/u₃. Coefficient hypersurface 625u₀u₄³ − 125u₃u₄² + 25u₂u₃²u₄ − 4u₃⁴ = 0. Eight-point signed fibre; conductor transport; odd-receiver pullback. | proved; "structural bridge, not an occupancy or zeta-zero theorem" | L, plus `21_` | Quartic identities and det DP = −2 **checked in `21_`** (Prop. 21.6, C1–C4). Fibre, cover and conductor not checked. Imports the C123 preprint, which is not in the repository (inventory G-ES-3). |
| 12 | Prime-local fibres: E has ℚ_p³ × K_ram², M has ℚ_p³ × K_unr², integral orders differ by index p. Negative-four-square transfer. Fixed-cofactor bijection {U \| ((h+1)/4)², h \| p + 4U} → middle states with Q = h. | proved after repairs (missing exterior divisibility gate restored) | L | Not checked. The WB's own audit records the repaired gate. |
| 13 | Fixed-input cover: at fixed p, ranks 2 + 6, monodromy order 48, deck group C₂ × C₂; finite flat rank-8 completion; odd-moment frame with det ±A⁻² | proved | L | Not checked. `21_` §4 left monodromy and conductor unchecked. |
| 14 | For h = 4j − 1 > t, the divisors W \| j² with W ≡ t (mod h) are canonical, companion, or finite templates. The finite ones satisfy the sharp bound h ≤ t² − 3t + 1. Prime families attain equality. For every t ≥ 4, infinitely many hard primes have an E state whose same-grade M box is empty. | proved; "not an ES counterexample" | D | See 2.14. **Correct**. |
| 15 | Unique rank-3 crossing on the positive-real ray p(1, t/(4t−402), t/202, t/200). Trace pairing = residue pairing ∘ ×2η³. Residue-to-native-Gram multiplier with retained defect. | proved; RH-facing parts are "interfaces, not ES occupancy claims" | L | Not checked. Uses zeta sources (inventory OV-12). |
| 16 | Integral signed completion: E index p², M index p⁹; Smith factors, conductors, kernels; Type-I boundary has p lifts mod p² and none mod p³ | proved; control family "not an ES counterexample" | L (102 KB) | Not checked. |
| 17 | Defining-prime chart is an exact quadratic twist; rank-(2+6) fibre product; 2·length + a(W) = 6Σ v_p(t_i − t_j) | proved | L | Not checked. |
| 18 | Three Legendre-symbol conditions force odd-frame nonsingularity on 3,456 classes mod 521,220. (13; 4, 18, 468) over 𝔽₆₁: 0 rational, 8 quadratic-extension points. | proved; conditions "sufficient, not necessary" | L | Not checked. Superseded in substance by item 22, which holds for all witnesses. |
| 19 | For n ≥ 3 rational denominators with reciprocal sum 4/p, integral first n − 1 power sums ⇔ all denominators integral; for ES two traces suffice. Raw-source fibres. | proved | L (38 KB) | Not checked. Plausible (monic-polynomial argument). |
| 20 | Mixed-source minimum G_J = G^{1/2}(I + T)⁻¹G^{1/2}; ES-labelled tensor action; collision exponents | finite results proved; **metric asymptotics conditional on zeta NG20–NG21** | L | Not checked. **Conditional import** (inventory OV-12, type D). |
| 21 | For a proper rational trace source (p, a, R, u, c), the complete set of same-word residual-divisor returns is {k \| R : d \| k, k ≡ 1 (mod 4K(u))}. Uniform strict return exists exactly for the nine words u \| 36. Every other word has infinitely many hard primes with proper M sources and no return. | proved; "method obstructions, not Erdős–Straus counterexamples" | D | See 2.21. **Correct**. |
| 22 | For every witness at p ≡ 1 (mod 12), the degree-8 symmetric 𝔑(p, x, y, z) < −(125873811/262144) p⁸ (≈ −480.17 p⁸), and < −6960.19 p⁸ at p ≡ 1 (mod 24). \|det O\| > 4cp⁸/S³. | proved (polynomial certificates) | D | See 2.22. **Correct**. Both certificates independently recomputed. |
| 23 | ‖O⁻¹‖ < 360p√w/𝔠, ‖∧²O⁻¹‖ < 180/𝔠, ‖∧³O⁻¹‖ < 41/(4𝔠p²) with 𝔠 = 80/6279⁴. s₃(O) > √(𝔠/180). Exponents sharp. | proved | Dc | See 2.23. The three new certificates are **verified**. The norm deduction was read in part; sharpness families not checked. |
| 24 | At p ≡ 1 (mod 24), a = cq with c \| 6 and q > 3 prime, p/4 < a < p/2: every rational tail pair with integral sum returns an integral middle witness. Nine automatic rays; infinite obstructing progressions for the others. | proved; obstruction is a method obstruction | L (3 audit files; tip differs from the pin in 2 lines) | Not checked. |
| 25 | Complete mixed-return fibres (size 2\|𝓘_E\| + 2Σ\|𝓘_{M,ν}\|); fixed-(R, u) spectra with powers 9, 4, 3/2, −3/2; two progressions in 1 mod 840 show inverse powers sharp | proved | L | Not checked. |
| 26 | Square-zero trace defect; prime-square trace classification; terminality; factor-sum map with Pell specialisation; fixed-tail-sum obstruction. p = 67369 is the least p ≡ 1 (mod 24) whose first trace shell precedes its first full shell. | proved; counterexample to a method, "not Erdős–Straus" | D (least example, prime-square theorem); L (Pell, tail-sum) | See 2.26. Least example **reproduced exactly**. |
| 27 | On the common-trace locus, c_E = c_M − (p−1)/K in ℤ/D. The two-channel operator (I + T_ω) is injective with an alternating inverse. Quotient-support criterion supp(Q) ∪ (supp(Q) + δ) = ℤ/g. Upward return across p = 67369. | proved | L (tip differs from the pin) | Not checked. |
| 28 | 𝒯_{p,a}(σ) = 2Σ_{E_a} W_σ(h_u) + (p^σ + p^{−σ})Σ_{M_a} W_σ(h_u), positive ⇔ occupancy. Cross-shell identity. \|𝒯_N\| = 2\|E_a\| + \|M_a\| + \|U_N\|. N = 3 is the unique closing odd quotient. Residual-27 empty locus at p ≡ 73 or 145 (mod 216). | proved | L | Not checked. The first identity is a weighted form of ES-02 (positivity ⇔ occupancy). |

### 2.4 Item 4 in depth

**Proof chain, read and checked.**

1. *Hard classes.* At a hard prime, 2, 3, 5 and 7 are quadratic residues, so every nonresidue vertex is ≥ 11 and p ≥ 1009. My arithmetic: p ≡ 1 (mod 8), 1 (mod 3), ±1 (mod 5) and {1, 2, 4} (mod 7) give exactly the six classes, and the least hard prime is 1009.
2. *Sources.* A source A_t = (p + σ_q q t²)/4 with t odd and R = σ_q q t² < 3p satisfies (A_t/p) = −1. It therefore has a nonresidue prime factor r ≠ q.
3. *gcd identity (7).* gcd(F_q(i), F_q(j)) = gcd(F_q(i), (j−i)(i+j+1)). For i, j ≤ 4, the right side has prime factors ≤ 7. So five valid ports give five distinct successors, and a closed set of size ≤ 5 forces 81σ_q q ≥ 3p at every vertex. Correct.
4. *Cycle equations.* p + σ_i q_i = 4c_i q_{i+1} gives p | D − S and p < (4H)^l. Cofactor bounds (19). Correct as read.
5. *Finite enumeration (21).* Recorded as 1,381,117,764 rooted profiles, 5,922,259 range-compatible, 1,915 integer models, and three surviving five-cycles, at p = 4201, 12601 and 26209.

**Checks.**
- The three cycles, their canonical edges and their multiplier-9 exits (43 | 1462, 23 | 5911, 5507 | 11014) are **verified**.
- Independent direct test: for all 108 hard primes 1009 ≤ p < 40,000, the graph with ports t ∈ {1, 3, 5, 7, 9} has no closed set of ≤ 5 vertices. For each vertex, the reachable set has size ≥ 6.

**Verdict.** Proved, conditional on the computer enumeration of the finite domain (21). That enumeration was run by two WB implementations but not by me. My check covers p < 40,000 directly. The reduction guarantees that the enumeration domain is complete for all p. What it gives is factor supply ("not selector occupancy", README of the package).

### 2.6 Item 6 in depth

**Theorem `thm:negative`.**
- *Notation.* L_a = 8τ(a)²/φ(R_a) − ℰ_a, where ℰ_a = Σ_g c_a(g)² is the residue-collision energy of the 2τ(a) divisors of pa mod R_a, and I_p = (p/4, p/2).
- *Constants re-derived.* I re-derived 𝒫 < (224/15)p^{2/3}(log p + 4) from τ(n) < 4n^{1/3} and Σ_{r≡3(4), r≤x} 1/φ(r) < (7/5)(1 + ¼ log x).
- *Diagonal bound.* 𝒟 ≥ 2Στ(a) > p(½ log p − log 2) − 2√p.
- *Final comparison.* 7/16 − 728/1875 = 1477/30000 > 1/24. Arithmetic checked.

Correct. The sublinear versions (18b)–(18d) were read: C₄ = 9 and 972² = 944784 are consistent. Not re-derived in detail.

**Finite claims, all reproduced** (`check_items_arith`):

| Claim | Reproduced value |
|---|---|
| p = 944329 ≡ 169 (mod 840); a = 236094 = 2·3·19²·109, R = 47 | T_a = 60; ℰ_a = 132; principal² = 2304 |
| Norm polynomial coefficients | Q₀ = 192, and (Q₁, …, Q₁₁) as printed |
| Character values | Q(ζ) = 1009.5515…, Q(ζ²) = 24.5211… |
| Three-mode and five-mode bounds | 55.96 and 58.09, so T_a ≥ 60 (T_a is a multiple of 4) |
| Principal-only bound at R = 47 | −732/23 |
| a = 236098, R = 63 | T_a = 8, ℰ_a = 16, coset masses (8, 8, 0) |
| p = 87481 | 21,870 first-half shells; L_a ≤ 0 on all; 34 occupied shells; T_a ≡ 0 (mod 4) on all (Klein-four lemma) |
| Hard primes ≤ 2·10⁶ | 4,519 primes; 311 residuals with φ(R) < 960 (largest 1995); principal-only misses exactly 87481, 196561, 944329, 1915201 |

**Verdict: correct.** The main theorem is a negative result about one lower-bound method (§5).

### 2.7 Item 7 in depth

**Proofs checked by hand:**
- ν_p (the least nonresidue) is an odd prime, ν_p² ≤ p, and m_p ≤ p − 2ν_p;
- the middle identities Q s = pλ + r and QR = p + 4hr², with Q a nonresidue below p, via Jacobi reciprocity. The proof needs gcd(r, Q) = 1; that holds because a common prime would divide s, and the WB does not spell this out;
- (M3)–(M5) with the √a case split;
- the exterior identities (E1)–(E2), (E3) h ≥ ν_p, and the monotonicity leading to (E6);
- the endpoint alternative (E8), including the mod-8 contradiction for equality;
- the D-bound (D1)–(D3);
- the free Klein-four action and the fundamental domain.

**Checks.**
- ν_p prime, ν_p² ≤ p and m_p ≤ p − 2ν_p for all primes p ≡ 1 (mod 8) below 2·10⁵.
- All 2,685 ordered middle states and 4,966 exterior states at primes p ≡ 1 (mod 8) below 6000 satisfy:
  - (M1), and that Q is a nonresidue below p;
  - (M5) with J = J_p;
  - (E1) and (E2) exactly;
  - h ≥ ν_p, (E6), (E8) where applicable, and (D2);
  - the hard specialisations.
- No violation. Equality cases: 118 for (M5) and 3 for (E6).
- The p = 2521 lanes reproduce: ν = m = 11; p² + 44 = 3²·5·141233; no divisor ≡ 31 (mod 44).

**Verdict: correct.** The WB's own three presentation repairs (radicals, the complement-fixed case, the image-lattice typing) are needed and sufficient.

### 2.14 Item 14 in depth

**Theorem `thm:capacity`.** I re-derived every step:
- 16tV = 1 + kh with k = 4ℓ + 1;
- j = ℓ + 4nV and t = (4ℓ + 1)n + ℓ²/V;
- the converse identity j²/V = t + n(4j − 1).

**Theorem `thm:bound`.** h + 1 ≤ 4ℓ + 16ℓ²(t − 1)/(4ℓ + 1) ≤ t² − 3t + 2. Equality holds if and only if w = n = 1 and t = 4ℓ + 2.

**Obstruction theorem, read.**
- t | j² ⇔ K(t) | j ⇔ h ≡ −1 (mod 4K(t)).
- The Jacobi-class lemma gives a class A ≢ −1 exactly when t ≥ 4.
- The CRT and Dirichlet construction then gives p ≡ 1 (mod 840) with a = hr, u = hr², shape α = −4t and 𝒜_t(j) = ∅.

Correct.

**Checks.**
- Brute force over t ≤ 80, j ≤ 4000, h > t: 159 finite words and 19 equality cases. Zero violations of the classification, the inverse (9), the bound (11) or the count (12).
- The t = 289 coexistence example reproduces.
- Example (17) at p = 825241 and example (19) at p = 7840561 are valid E states with the claimed shapes; 𝒜₄(11) = ∅.
- The CORRECTION case p = 5209 (a = 1900, R = 2391, u = 1520) gives (4u + 1) mod R = 1299, confirming that the predecessor's prose domain was missing the gate.

**Verdict: correct.**

### 2.21 Item 21 in depth

- *Trace lemma.* The tail trace is integral ⇔ R | G_c², and the reduced denominator d = R/gcd(R, G_c) satisfies d² | R. Checked by reading.
- *`thm:all`.* The return set is {k | R : d | k, k ≡ 1 (mod m)} with m = 4K(u). This is correct: the key step multiplies p + R/k ≡ 0 by the unit k and uses p ≡ −R.
- *Nine-word theorem.* H_m = {1} ⇔ m | 24 ⇔ u | 36. Checked.
- *Optimality construction for u ∤ 36.* Take a unit b with b² ≠ 1; primes δ ≡ −b² and t ≡ b⁻¹; R = δt². Then the only candidates k ∈ {t, t², δt, δt²} are ≡ b⁻¹, b⁻², −b, −1 (mod m), and none is ≡ 1. Checked.

**Checks.**
- On all 4,233 proper trace sources at primes p ≡ 1 (mod 4) below 2600, the formula equals the brute-force set of returns (built from the definition).
- No u | 36 source lacks a return.
- 3,041 of 3,654 other-word sources have none.
- The examples at p = 1009, 1108801 and 51361 give K = {25}, {21, 441} and {81}, as stated.

**Verdict: correct.**

### 2.22 Item 22 in depth

**Reduction steps, checked by reading.** Every witness has four distinct literal roots and a unique smallest denominator in (p/4, p/2):
- no denominator equals p, because (3y − p)(3z − p) = p² with both factors ≡ 2 (mod 3);
- the Type I and Type II case analysis.

**Recomputed symbolically** (`check_receiver_certificates`):
- S⁶F = 𝔑 under A = −1/S, B = −e₂/S, C = e₃/S, D = −e₄/S;
- the reduction matrix of (1, H′, AH′² + 2TH′, 7T²H′ − 13H′²) mod H equals the printed M_H;
- det M_H = 4F/A.

**Exterior certificate.** The E-root substitution divided by 64u² is an integer polynomial P_E of bidegree (12, 16). P_E(1+X, 1+Y) and both derivative combinations have 221 coefficients each, all positive (minimum 83,886,080). Φ(u) = (2u − 1)²V(u)/(4096u⁶), Φ(2) = c₁₂ exactly, and Φ(5) > c₂₄.

**Middle certificate.** H_M has 192 positive coefficients. 47045881·H_M − 327448292668·L_M⁶ has zero constant term and 191 positive coefficients.

**Census.** All 1,317 witnesses at primes p ≡ 1 (mod 12) below 1300:
- the smallest denominator lies in (p/4, p/2) and is unique;
- no violation of 𝔑 < −c p⁸;
- the tightest case has ratio 160.9 at p = 13, witness (4, 26, 52).

The constants are therefore conservative on small witnesses.

**Verdict: correct and proved.** The certificates are finite polynomial identities, now reproduced by independent code. Scope, as the WB says: it is a statement about existing witnesses, and says nothing about occupancy.

### 2.23 Item 23 in depth

**Certificates verified:**
- J_E = S/p·16wu;
- 449⁶P_E − 1310720·4w⁴J_E⁶ has 221 positive translated coefficients;
- J_M = (1 + b + c)L + bc;
- 483⁶H_M − 81920J_M⁶ has 192 positive coefficients;
- 4·52⁴·483⁴(b+c)²H_M − 81920L_M⁴(Y+1)²J_M⁴ has 237 positive coefficients;
- 𝔠 = 80/6279⁴ = 81920/(4·52⁴·483⁴).

**Numeric check** on all 101 witnesses at p < 200 (complex receiver O at 60 digits):
- |det O| = 4|𝔑|/S³;
- all four bounds hold, with large margins: max ‖O⁻¹‖/(p√w) = 0.30, max ‖∧²O⁻¹‖ = 1.03, min s₃ = 2.93.

**Not checked:**
- the cofactor and entry-table deduction (§§3–4 of the source), read only in part;
- the two sharpness families.

**Verdict:** the certificates are correct. The norm theorem is plausible and consistent with the numerics. Sharpness is unverified here.

### 2.26 Item 26 in depth

**Theorem `thm:least`, reproduced exactly:**
- 817 primes p ≡ 1 (mod 24) up to 67369;
- the first with a trace shell below the first full shell is p = 67369, with a = 16849 = 7·29·83 (R = 27) against a = 16850 (R = 31);
- the E trace words {29, 83, 488621, 1398467} and M words {1421, 4067, 69803, 199781} match;
- the full E words {674, 84250} match.

The deduction ("no universal trace-to-witness map with a′ ≤ a") is valid: every witness's minimal denominator is a full first-half shell, and the first one is 16850.

**Theorem `thm:square`** (prime-square traces at p ≡ 1 (mod 24)): read, and correct as read. The identity 16(4q³ + 1) − (4q + 1)(16q² − 4q + 1) = 15 checked by expansion.

**Terminality:** read, and correct as read.

**Not checked:** the factor-sum/Pell and fixed-tail-sum sections.

**Verdict:** the least example is correct; see §5 for its scope.

### 2.x Fable- and zeta-facing items (11–13, 15, 20)

**What they prove.** Algebraic structures attached to an existing witness:
- the quartic with roots (p, x, y, z) and its coefficient hypersurface (`21_` C1–C3);
- an eight-point signed cover;
- local fibre algebras;
- trace and residue pairings.

**What they import:**
- the 4-D map P with det DP = −2 (`21_` C4). It is presented as the "ES–Fable inverse correspondence" and uses the C123 preprint, which is not in the repository;
- for items 15 and 20, zeta-programme files. Item 20's metric asymptotics consume NG20–NG21 as a theorem dependency (README L189–192).

**Scope, per the WB:** none of these gives occupancy, a zeta-zero statement or an RH conclusion.

---

## §3 Results bench R01–R10 and X1–X7

WB status (RESULTS.md L31–33): no prover, no independent review, no novelty search. Most sources are private (CN-*).

| ID | Statement (paraphrase) | Check | Verdict |
|---|---|---|---|
| R01 | S = R ⊔ {τ} is a commutative semiring. {τ} is prime; {τ, 0_R} is prime ⇔ R is a domain. | proof read; zeta counterpart checked by hand in `21_` §6 | correct |
| R02 | In ℂ[C₆], δ_k = e₃ + 2e_{3−k} has all six Fourier values nonzero (\|1 + 2ζ^{−km}\| ≥ 1) | computed: minimum modulus 1.000 | correct |
| R03 | 15 primes split by residue mod 5 into fibres 1 + 4 + 4 + 3 + 3; opposite residues give 1 + 7 + 7; pullback is injective | by hand: fibres {5}, {11,31,41,71}, {2,7,17,47}, {3,13,23}, {19,29,59} | correct (finite set facts only) |
| R04 | Congruences mod 107 at p = 8,803,369 | all nine residues reproduce; p is prime; 4 \| p + 107 | correct (arithmetic only; the "Busy Beaver" meaning is interpretation) |
| R05 | θT = 4θ for T(n) = 4n + 1, θ(n) = 3n + 1; U(T^j n) = U(n) for the odd Collatz step U | identity; U-invariance for odd n < 4000, j < 8 | correct (classical-style observation; no convergence claim) |
| R06 | In C₅₃: A = {35r + 11s + 33t}, complement D = {23 + 42j}, \|A\| = 43, \|D − D\| = 19, 6 ∉ D − D, (A+29) ∪ (A+23) = C₅₃ | exhaustive | correct |
| R07 | inf_{k≠0} \|v·k\|‖k‖ = 1/√(4+2√2) for the √2 directions | `21_` Lemma 21.3 (A7) | correct (`21_`) |
| R08 | For Λ³ with cyclic shift P: fixed lattice has Gram 3G; zero-sum lattice has Gram [[2G, −G], [−G, 2G]]; index 3^d; minima m and 2m; Eisenstein action | Gram matrices and index for Λ = A₂ and ℤ³ | correct (general proof read) |
| R09 | Star–Kneser obstruction: a miss forces Σ(K) ≤ 0 at K = Stab(B) | proof read; imports Kneser (DeVos, arXiv:1303.3539) | correct given Kneser |
| R10 | H ⊂ (ℤ/6)⁴ × 𝔽₂² of order 72 (duad code plus tetracode); q(H) = 0; cost 0 once, 4 × 46, 6 × 25 | exhaustive: \|H\| = 72, closed, q ≡ 0, costs {0:1, 4:46, 6:25} | correct (finite) |
| X1 | Coefficient-frame matrices A, B generate M₅(𝔽₁₀₇) (25 × 25 determinant 32) | **not recomputed** | — |
| X2 | det A_l = (1+l)³(1−3l); no rational similarity between A₁ and A₂ (16/135 is not a square) | by hand: −16, −135; odd 3- and 5-adic valuations | correct |
| X3 | G(R) universal maps (= R01) | `21_` §6 | correct |
| X4 | Support-aware homogenisation (x, h) ↦ (ax + bh, h); finite-word matrix product | proof read | correct as read |
| X5 | Abstract C₆ Fourier identities; 289³ ≡ 169, not −1, mod 840 | powers of 289 mod 840: 1, 289, 361, 169, 121, 529 | correct (a source-passage error, recorded by the WB) |
| X6 | Weyl operators T_a M_χ form an orthogonal basis of End(ℂ[A]) | C₂ × C₃: rank 36, Gram 6I | correct |
| X7 | Diagonal model (n + q/3)²/ρ² has kernel \|0,0⟩ and gap 1/(9ρ²); quadratic-form identity | by hand | correct (WB: "not an interacting Yang–Mills theorem") |

---

## §4 ES-08 and ES-09

### ES-08: JT Boolean/cyclotomic (12 Sep continuation)

**Statement.** At p = 1201, a = 310, R = 39, the negative Jacobi cell has mass 18 and energy 30, while avoiding every target would need energy ≥ 32. This forces a solution in that shell. The unpartitioned test does not.

**Checked:** only the stated witness, (310, 1489240, 9608), which is valid.

**Not checked:**
- the energy minimum and cell computation;
- the hexagonal/quartic-norm statements;
- the common-modulus affine return.

**Verdict:** the witness is correct; the forcing inequality was not audited.

### ES-09: ES → S⁶ counterfactual (`received/es_s6_counterfactual/src/core.tex`)

**What is imported.** Only three integer matrices A₁, A₂, A_∞, cited as inverse-transpose monodromies from `alpo.ge/s6.pdf` §2, Lemmas 2.4–2.7. The source says no global S⁶ assertion is used.

**What is proved:**
- `thm:class`: the affine part b of the representation is a cocycle whose class has infinite order. Its reduction mod D has exact order D, detected by the third coordinate at the cusp. It is locally trivial on ⟨g₁⟩ and ⟨g₂⟩. The level-D cover has a section ⇔ D = 1.
- `lem:shears`: the two shears and their central commutator (x, y, z − 12).
- `thm:orbits`:
  - the action on (ℤ/D)³ is transitive if 3 ∤ D;
  - there are two orbits (sizes D³/9 and 8D³/9) if 3 | D;
  - the genera are g(D) = (5D³ − 12D² − 17D + 24)/24, g₀(D) = (5D³ − 12D² − 81D + 216)/216 and g₁(D) = (5D³ − 12D² − 9D + 27)/27.
- `prop:crt`: modulus maps. The compactification part is corrected in `CORRECTIONS.md`: the finite-branch cycle lengths divide 3 and 4, not the moduli.

**Checks** (`check_extras`):
- A₁³ = A₂⁴ = A₁A₂A_∞ = I;
- the induced permutations satisfy the relation pointwise;
- orbit decomposition and Riemann–Hurwitz genera computed from cycle counts for D = 1, 3, 5, 7, 9, 11, 13, 15, all matching the formulas. For example g(5) = 11, (g₀, g₁)(3) = (0, 1), (g₀, g₁)(9) = (10, 97) and (g₀, g₁)(15) = (61, 521).

**ES application (`arithmetic.tex`).**
- The rational candidate's tail denominator D = R/gcd(R, 4u + 1) (E) or R/gcd(R, u + a) (M) is 1 exactly at integral candidates. This is ES-02 again.
- `thm:failure`: ES fails at p ⇔ the denominator-labelled cover (a disjoint union of level-D_α covers) has no section.

**Verdict.**
- The group theory, orbit classification and genus formulas are correct.
- The ES equivalence is correct but is a re-encoding of ES-02: the section criterion "D = 1" is exactly integrality. As written it adds no new arithmetic constraint.
- It depends on the S⁶ source only for the three matrices, whose relations I verified.

---

## §5 Negative results with exact scope

| Source | What proposed implication fails | Certificate (checked here unless noted) | What it does NOT show |
|---|---|---|---|
| `bounded_transport.tex` L196–217 | "Each occupied shell has a witness with unary layer A ≤ 2" | p = 37, a = 12: only u = 8, (A, B, s) = (3, 2, 2); witness (12, 42, 1036) | Not a failure of the global cutoff: a = 10 at the same prime works, with (10, 2405, 130). |
| `first_two_shell_sieve.tex` L291–320 | Occupancy of the R = 7 shell implies a first-two-layer (A ≤ 2) hit | p = 373, a = 95: E = {5, 19}, M = ∅, every hit has A ∈ {19, 5} | Nothing about other shells. |
| Item 2 | Every canonical closed component contains a local hit | p = 2521: 7-cycle sink, E = M = ∅ at all seven shells | p = 2521 has witnesses, e.g. (636, 5611746, 70588). Not an ES counterexample. |
| Item 3 | Strict canonical (primitive-cycle) descent terminates at a hit | p = 7510085481569082811681: triangle 31→223→307 with 1,215 divisor vectors, all failing | The prime has an ES solution (WB verifier); only the canonical component is closed. |
| Item 6, `thm:negative` | The principal-only (adverse-sign) lower bound, summed over shells, is positive for large p | proof checked: Σ L_a ≤ −(1/24)p log p for p ≥ 2²⁰ | Says nothing about the true count T_a. The true signed sum cancels the lost diagonal. |
| Item 6, p = 87481 | Some nonnegative reweighting of the principal-only bounds certifies occupancy | all 21,870 shells have L_a ≤ 0; 34 shells are occupied | Only this certificate family fails; the prime is solvable. |
| Item 7, §9 | Two-colour (prime-free) positivity at odd squares n | proof read; n = 25, a = 7: restricted source {1, 7, 25, 175} misses divisor 5; 4/25 = 1/7 + 1/350 + 1/70 | Not a composite ES counterexample. |
| Item 14, `thm:obstruct` | Same-grade (cofactor-h) middle repair always exists from an exterior state with α = −4t, t ≥ 4 | construction read; t = 4 instance p = 7840561 checked (𝒜₄(11) = ∅) | Those primes have the exterior solution. Not an ES counterexample. |
| Item 21, `thm:optimal` | A same-word residual-divisor return exists for every proper trace source, for words u ∤ 36 | construction read; brute force: 3,041 of 3,654 non-nine-word sources at p < 2600 lack returns | Endpoint solutions exist at those primes. Only the transformation system fails. |
| Item 24 | The universal ray-preserving rule on nonautomatic rays | not checked | WB: a separately constructed middle witness exists. |
| Item 26, `thm:least` | Some universal map from every rational trace to a witness never increases a | p = 67369: first trace at a = 16849, first witness shell a = 16850 | p = 67369 is solvable (a = 16850, E words 674, 84250). A repair must sometimes increase a. |
| Item 26, fixed tail sum | Keeping the numerical tail sum Y + Z and moving to a proper divisor residual | p = 67369, M trace u = 1421 (not recomputed beyond the trace words) | Only that fibre. |
| Items 16, 18, 27, 28 | Various: listed gates are not an integral-source certificate; failed character tests do not certify singularity; two labels do not close a quotient; odd quotients N > 3 leave uncovered orbits | not checked | All labelled method limits by the WB. |
| ES-07 (`21_` Neg. 21.2) | Joint averages transfer on unchanged finite torsion | p = 13, a = 4: 13 against 4 (`21_` A5) | The repaired cover (T17) restores the counts. |
| X5 | Arithmetic −1 ≡ 289³ (mod 840) | 289³ ≡ 169 | Only that source passage. |

---

## §6 Overlaps with other programmes

Type codes follow the inventory §8: P = proved map, I = shared identity, D = imported dependency, A = analogy, M = methodology.

| Object | ES locator | Other side | Type | Status here |
|---|---|---|---|---|
| NS auxiliary torus J = [[3,1],[1,5]], eigenvalues 4 ± √2; Pell constant (R07) | `ns_operator_bridge/*.tex` (ES-07) | NS manuscript §6.1 (via YM transcription) | P (operator only, no fluid theorem) | checked in `21_` §1 |
| (3,4,∞) monodromy A₁, A₂, A_∞ | ES-09 `src/core.tex` L1–20 | `alpo.ge/s6.pdf` §2 | P/D (matrices imported; relations verified) | matrices, orbits and genera verified here |
| Order-72 glue for A₅⁴D₄ | R10; `RESEARCH_DIRECTIONS.md` §2 | S⁶ key-advances §4 ([N:R] = 72) | I at the level of the named object | R10 verified; the two codes were not compared (inventory OV-09) |
| Split-zero semiring G(R) | R01, X3 | zeta satellite 14 `prop:gcue-coordinate-support` | I | `21_` §6 |
| Finite Weyl basis | X6 | zeta `prop:finite-weyl-coordinate-isomorphism` | I (per ES) | X6 verified on C₂ × C₃; the zeta side was not read |
| NG20–NG21 and native Gram/moment files | items 15, 18, 20 (`SOURCE_LEDGER.md`) | zeta `NATIVE_GAUSSIAN_TRANSFER.tex` etc. | D (item 20 conditional) | not checked |
| 4-D map P (det −2) and conductor | item 11 `upstream/FABLE_TO_ORIGINAL_CONDUCTOR.tex` | zeta file, byte-identical (inventory OV-13) | P | det DP in `21_`; rest not checked |
| ES reader v69 vendored into zeta | root PDF / `01_…zip` | zeta `source_dependencies/ES_READER_V69.tex` | D (zeta imports ES) | not checked |
| Jacobian counterexample F (Alpöge announcement; "Fable") | owner's C123 preprint (not in the repository) | YM, zeta | P within each side | `21_` §4 |
| SplitZero 13–16 Sep packages | table F folders | zeta `formal/splitzero/…`, AMT1–10 | P/D | not read |
| Collatz: θT = 4θ and odd-step invariance (R05); homogenisation (x, h) ↦ (ax + bh, h) (X4) | `PROOF_NOTES` R05; ARGUMENTS X4 | Clankers Zenodo 19900461; zeta v11 foundation; external collatz-workbench | I (same formulas); R05 is internal | R05 verified; X4 read |
| "Gap" wording | X7 | YM mass gap | A (WB: not the YM theorem) | — |
| ES PR6 top-socle to success projector | `es-split-boundary-20260914` | YM research-control | A ("candidate-not-imported") | — |
| Erdős 817 | — | — | M only (PolyClank methodology); no mathematical edge found (inventory) | — |

---

## §7 What I did not check

1. Item 4's finite enumeration of domain (21), about 5.9 million profiles. My direct graph test covers hard p < 40,000 only.
2. Items 1, 5, 9, 10, 12, 13, 15–20, 24, 25, 27 and 28 beyond README statements. For items 2, 3 and 8 I checked only the certificates and bounds noted.
3. Item 6: the sublinear theorem constants (18b)–(18d), beyond consistency; the complement-aware refinement.
4. Item 23: the cofactor and entry-table deduction to the norm bounds, and the sharpness families. Items 22 and 23: the p-adic valuation histogram.
5. Item 26: the factor-sum/Pell map, the fixed-tail-sum classifier, and the unit-direction saturation theorem.
6. ES-04, ES-05, ES-06 (bounded transport CRT, Connes–Consani interfaces, boundary swap). The locator-only files of ES-07.
7. ES-08's energy argument. X1's M₅(𝔽₁₀₇) computation.
8. The 14 earlier incoming packages (inventory table F). The 488- and 619-page archives. Any ZIP or PDF content.
9. Primality of the 22-digit p in item 3 is by BPSW (sympy), not a certificate. The WB supplies an 80-node certificate, which I did not replay.
10. Literature novelty. I relied on the WB's own attributions (Elsholtz–Tao Type I/II, Mordell-type identities, Kneser via DeVos) and did no search.

---

## §8 Results that stand without the workbench's vocabulary

These are candidates for the reader, each in one plain line. Status: ✓ = proved and checked here; (c) = classical in substance; ✓* = proved given a computer enumeration that I did not re-run.

1. (c) ✓ For a prime p = 12h + 1, every solution of 4/p = 1/x + 1/y + 1/z has smallest denominator a in [3h+1, 9h]. The solutions with that a correspond exactly to divisors u of a² with (4a − p) | 4u + 1 or (4a − p) | u + a. The number of unordered pairs is |E_a| + |M_a|/2.
2. (c) ✓ Hence ES at p is equivalent to a finite, explicitly computable divisor test over those shells (ES-02).
3. ✓ At a = (p+3)/4, a solution with smallest denominator a exists if and only if a has a prime factor ≡ 2 (mod 3). The number of such unordered solutions is 3P₁(P₂ − 1)/4.
4. ✓ At a = (p+7)/4, a three-predicate criterion on the prime factors of a mod 7 decides the same question.
5. ✓ (Item 7) For p ≡ 1 (mod 8), explicit bounds in terms of the least quadratic nonresidue constrain where solutions can lie. At primes where 2, 3, 5 and 7 are residues:
   - any "middle" solution has smallest denominator a ≤ 3(p+3)/11;
   - any "exterior" one has 22(p+1) ≤ 23(p − 2a + 1)².
6. ✓ (Item 14) For h = 4j − 1 > t, the divisors of j² congruent to t mod h are t itself, 4tj, or members of an explicit finite list. That list is empty unless h ≤ t² − 3t + 1, and this bound is sharp.
7. ✓ (Item 21) An explicit complete rule for when a rational solution with integral y + z can be turned into an integral one by dividing the residual. It works uniformly for exactly the nine words u dividing 36.
8. ✓ (Item 22) For every solution at a prime p ≡ 1 (mod 12), an explicit degree-8 symmetric polynomial 𝔑(p, x, y, z) is below −480 p⁸ (below −6960 p⁸ if p ≡ 1 mod 24). This is proved by two finite positive-coefficient certificates.
9. ✓ (Item 6) The "principal character only" lower bound for the pair count, summed over shells, is at most −(1/24) p log p for all p ≥ 2²⁰. That method cannot prove ES.
10. ✓ (Item 26) p = 67369 is the least prime ≡ 1 (mod 24) at which a rational solution with integral y + z occurs below the smallest integral solution's first denominator.
11. ✓* (Item 4) At every hard prime, starting from any quadratic-nonresidue prime and factoring at most 25 numbers of the form (p + σqt²)/4 (t = 1, 3, 5, 7, 9) yields at least six distinct nonresidue primes.
12. ✓ (ES-09) The (3,4,∞) monodromy matrices give (ℤ/D)³-covers of genus (5D³ − 12D² − 17D + 24)/24 for 3 ∤ D, with an extra orbit split for 3 | D. They have a section only at D = 1.
13. ✓ (R07, via `21_`) inf_{k≠0} |v·k|·‖k‖ = 1/√(4 + 2√2) for the eigen-directions of [[3,1],[1,5]], attained along Pell vectors.
14. ✓ Small finite facts that stand alone: R06, R10 (an order-72 isotropic glue code with its cost spectrum), X2 (Descartes and Kocik forms are not rationally similar), and X5 (289³ ≡ 169 mod 840).
