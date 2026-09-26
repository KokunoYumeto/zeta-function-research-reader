# Collatz workbench: first-pass mathematical audit

Audit date 26 September 2026. Subject: `KokunoYumeto/collatz-workbench`, commit `caf04ff` (main). This is a first-pass audit by one reviewer (an AI model) with limited time. It is not peer review. Nothing below says or implies that the Collatz conjecture is settled. The workbench does not say so either, and it repeats this in every note.

---

## §0 Sources read and method

**Clone.** A shallow partial clone of the repository at `caf04ff`. The working tree was empty. I read it with `git show HEAD:<path>`. To run scripts I exported copies with `git archive` into a scratch folder (read-only use). I left out `bilateral_root_bounds_20260916/evidence/sources11610.jsonl.gz` (30 MB). I did not modify, commit or push anything, and I did not use web access.

**Read in full:**
- `README.md`
- `editions/cumulative_20260916/{README.md, RESULTS_INDEX.md, PUBLICATION_NOTES.md}`
- `collatz_reconstruction/research_program/QUARANTINED.md`
- `docs/collatz_overview_20260916.md`
- `RESEARCH_MAP.json`
- `collatz_reconstruction/state/claims.jsonl` (all 200 records tabulated; selected records read in full)
- `research_program/all_even_join_extension_20260916/{note.md, README.md, all_even.py, replay.py}`
- `research_program/history_law_cutoff_20260914/RESEARCH_NOTE.md`
- `research_program/split_zero_history_20260913/{note.tex, README.md}`
- `preprints/tao_clock_audit/{README.md, sections/consequences.tex}`
- `research_program/README.md`, `research_program/chapters/00_status_and_scope.tex`, and the claim environments of chapters 03–04 in that quarantined tree
- `formal/README.md` and the theorem list of the Lean file

**Read in part:**
- `stopped_affine_transport_20260914/note.md`: §§1–3 and §7 in full, headings for the rest.
- `cycle_relative_cohomology_20260914/note.md`: §§1, 3, 4, 5 and Theorem 6.1.
- `clocked_support_20260914/note.md`: §7 and Theorems 8–9.
- For every other chapter: its opening paragraph and theorem headings only.

**Method.** For each audited item I:
- restated the result;
- re-derived the proof steps by hand;
- wrote an independent Python check that imports nothing from the workbench and tests the statement on actual Collatz data;
- re-ran the workbench's own checker when it finished within about 2 minutes.

All scripts and their `*_OUTPUT.txt` files are in this folder.

| Script (independent) | What it tests | Result, time |
|---|---|---|
| `check_all_even.py` | Ch. 20: Lemma 1; Theorems 2–3; §5 families; R₀ bound; identities (1), (18) | PASS, 22 s |
| `check_all_even_large.py` | Ch. 20: Theorem 3 on 3,144 large sources, e ≤ 12 | PASS, 2 s |
| `check_history_law_indep.py` | Ch. 1: Lemma 2.1; (2.1)–(3.5); (6.1); Gaussian window (numerical look) | PASS, 17 s |
| `check_split_zero_indep.py` | Split-zero note: exact parts, plus the zero-cluster inversion tested numerically with mpmath | PASS, 3 s |
| `check_transport_cycles_indep.py` | Ch. 2 Theorem 2.1 and §7; Ch. 3 Theorems 1.1 and 3.1 and the family exclusion; Ch. 6 Theorem 9 inequalities | PASS, 5 s |
| `check_tao_clock_indep.py` | Tao preprint: nested passage, the map J, ℓ¹ contraction | PASS, 168 s (see note in §3) |
| `check_tao_clock_identity_3xm1.py` | The clock identity, tested non-vacuously on the 3x−1 map | PASS |

| Workbench checker re-run | Result |
|---|---|
| `all_even_join_extension_20260916/replay.py --predecessor` | PASS in 19.5 s. Predecessor first-jet: 39,211 checks. New suite: 87,989 checks per run, ordinary and optimized runs identical. Affine auditor: 512 families, 24,180 equations. (`ALLEVEN_OWN_REPLAY_OUTPUT.txt`) |
| `split_zero_history_20260913/check_history.py` | pass in 4.7 s (`SPLITZERO_OWN_CHECK_OUTPUT.txt`) |
| `history_law_cutoff_20260914/check_history_law.py` | pass in 3.2 s (`HISTORYLAW_OWN_CHECK_OUTPUT.txt`) |
| `stopped_affine_transport_20260914/verify.py` | PASS: 175,269 checks in 1.3 s. Output JSON identical to the recorded `verification.json`. |
| `cycle_relative_cohomology_20260914/verify.py` | PASS: 42,507 checks in 1.9 s. Output identical to the recorded file. |
| `preprints/tao_clock_audit/certificates/check_finite.py` | pass in 19.2 s (`TAOCLOCK_OWN_CHECK_OUTPUT.txt`) |

---

## §1 Inventory

### 1(a) Editions and reconstructions of published literature (not the workbench's own theorems)

| Item | Location | What it is |
|---|---|---|
| Siegel, Hydra maps, numens, (p,q)-adic analysis | `siegel_edition/…`, PDF `maxwell_siegel_research/output/pdf/…` | Critical-expository edition under Siegel's name. The ledger records source-level issues, e.g. CLM-COL-000038 "not certified as printed", 000041 "not certified", 000042 "correction required" (Fourier inversion). Not audited here. |
| Tao v7, almost-all orbits | `tex/chapters/01g–01j`; claims CLM-COL-000111…122; QA `qa/TAO-*` | Reconstruction of Prop. 1.9, Prop. 1.11, Thm 3.1, Thm 1.6 and Thm 1.3 at "repaired" scopes, with local repairs recorded. The theorem is Tao's. |
| Terras, Everett, Allouche, Korec | `tex/chapters/01_literature_spine.tex`, `01f_everett_1977.tex`; CLM-COL-000073, 082–084, 127–136 | Density-of-descent lineage, crosswalks, and repairs of printed details. |
| Crandall 1978, Steuding, Pillai/Thue/Pólya chain, Herschfeld | `tex/chapters/01a, 01e`; CLM-COL-000061–110 | Cycle and continued-fraction lineage. CLM-COL-000103 is conditional on Crandall's Conjecture 2.1. |
| Krasikov–Lagarias 2003; Lagarias 1985/1990; de Bruijn graphs (Laarhoven–de Weger); Bernstein; Matthews; Kohl; Conway; Urata; computational verification (Barina, Oliveira e Silva, Roosendaal) | `tex/chapters/01c, 01d, 01k`; `qa/*.md`; `certificates/*_checks.py` | Source audits and crosswalks. |
| Lean | `formal/GeneralizedResidueItinerary.lean` (333 lines, no `sorry`) | Formalizes the finite one-digit lifting kernel for generalized residue itineraries only. Not built in this audit. |

### 1(b) The workbench's own statements

Status labels are the workbench's own. Every note describes itself as holding written proofs with exact finite checks, not external review. The claims ledger has records (CLM-COL-000187/188) only for the Tao-preprint deductions and the research companion. **It has no records for the twenty chapters or the split-zero note.** For those, the labels come from each note's status line. "Checker" means a `verify.py`/`replay.py` in the note's folder; several also have a `.github/workflows` file. No chapter has a Lean file.

| # | Item (location under `collatz_reconstruction/research_program/`) | Main statement (paraphrase) | Own label | Checker / Lean | This audit |
|---|---|---|---|---|---|
| SZ | Split-zero history, `split_zero_history_20260913/note.tex` | Faithful polynomial lift of parity words, with its inverse and realizing residue. On the odd-return words with fixed (m, A), the (K−1)-jet of a zeta-zero cluster of an explicit Hurwitz family recovers every weight and joint predicate; K−2 is not enough. | Proved (finite parts checked; analytic lemma "not Lean-certified") | `check_history.py` / no | **§2.2: correct**; encoding only |
| 1 | History laws, `history_law_cutoff_20260914/RESEARCH_NOTE.md` | Exact counts of exponent-word cylinders in any window of N odd numbers. Finite TV sandwich. Gaussian window: TV(P, G) → Φ(2c) at m = L/2 + c√L. | Written continuation with exact finite checks | yes / no | **§2.3: correct** |
| 2 | Stopped affine transport, `stopped_affine_transport_20260914/note.md` | Exact cylinders and restart charts on progressions. Reference-3 stopping leaves force actual descent. √-potential contraction √15/4 in the fair-bit reference model. Stopped law with explicit tail. | Proofs + exact replay | yes / no | **§2.4: audited parts correct** |
| 3 | Cycle-relative cohomology, `cycle_relative_cohomology_20260914/note.md` | coker B_p ≅ ℤ/D with [1] ↦ [C]. Positive integer cycle ⟺ D > 0 and D ∣ C. No nontrivial cycle with ≤ 1 exponent-1 step. Relative orbit-graph homology. Collatz ⟺ H₀ = 0. Descent retraction fixing every cycle chain. | Proofs + exact replay | yes / no | **§2.5: correct** (mostly reformulations) |
| 4 | Residual splice, `residual_splice_20260914/note.md` | Exact first-descent fibres; exponent-tail descent; period-driven cycle exclusion (403-rise sector retained). | Proved + checks | yes / no | Headings only |
| 5 | Integral blocks, `…/integral_blocks.md` | Block compression of the cycle complex, retaining the forcing vector. | Proved | yes / no | Headings only |
| 6 | Clocked support, `clocked_support_20260914/note.md` | Two-clock complex. Thm 8: all odd n ≤ 330,749 reach 1 (finite database). **Thm 9: no nontrivial positive cycle with ≤ 678 exponent-1 positions in its primitive odd-return word.** | Proved via finite certificate | yes / no | **Thm 9 re-derived; inequalities checked** |
| 7 | Completion defect, `completion_defect_20260914/note.md` | Classes carried to supported zero realized as infinite primitives modulo finite ones. | Proved | yes / no | Not audited |
| 8 | Supported structure, `supported_structure_20260915/note.md` | Laurent-module classification; a "structural restatement" of Collatz. | Proved | yes / no | Not audited |
| 9 | Intrinsic first-jet, `intrinsic_zero_firstjet_20260915/note.md` | B = ker(H¹(K_ε) → H¹(K)) ≅ ⊕_C ℤ/m_C ⊕ ⊕_A ℤ. Collatz ⟺ B = 0. Finite certificate for ξ_n = 0 ⟺ explicit path to 1. | Proved | yes / no | **§2.6: re-derived, correct** |
| 10 | Anchored defect, `anchored_defect_20260914/note.md` | Thm P (cycle inequality via exponent-1 positions). Thm Q: no nontrivial cycle with ≤ 403 exponent-1 positions. | Proved + certificate | yes / no | Superseded by Ch. 6 Thm 9; not audited |
| 11 | Turns and unit excess, `…/turns_and_unit_excess.md` | Thm T (ordered turns); Thm U: ≤ 404 exponent-1 positions excluded. | Proved + certificate | yes / no | Not audited |
| 12 | Defect-rank descent, `defect_rank_descent_20260915/note.md` | Repetition rank; all-length descent cone; finite certificate for all primitive lengths. | Proved + certificate | yes / no | Not audited |
| 13 | Logarithmic run exclusion, `…/logarithmic_run_exclusion.md` | All-length minimum-run exclusion (Thm F). | Proved; **imports Matveev's bound** as printed in Languasco–Luca–Moree–Togbé 2025, Thm 2.1 | yes / no | Not audited (external dependency) |
| 14 | Negative shadow descent, `negative_shadow_descent_20260916/note.md` | All-length gap inequalities; repeated-shadow descent at the coefficient crossing. | Proved | yes / no | Not audited |
| 15 | Mixed switch control, `mixed_switch_control_20260916/note.md` | Descent for every ordering of two packet types with a contracting tail. | Proved | yes / no | Not audited |
| 16 | Global cylinder control, `global_cylinder_control_20260916/note.md` | All-word separation; at most one original source remains per contracting cylinder. | Proved | yes / no | Not audited |
| 17 | Height window reduction, `height_window_reduction_20260916/note.md` | Sharp crossing envelope; finite-window reduction; integral retraction. | Proved | yes / no | Not audited |
| 18 | Ternary join reduction, `ternary_join_reduction_20260916/note.md` | Complete lower-source joins on every ternary layer; polynomial support control. | Proved | yes / no | Not audited (predecessor of Ch. 20) |
| 19 | Bilateral root bounds, `bilateral_root_bounds_20260916/note.md` | Bilateral joins; maximal lift; nested retractions; support bound R₀(n) ≤ 64 n^{log₃4} + 21. | Proved + large ledgers | yes / no | R₀ inherited, **not re-proved** |
| 20 | **All-even join extension**, `all_even_join_extension_20260916/note.md` | Common-future pair families for every even interior exponent e. Finite template search at each n. Budget-preserving and unrestricted retractions with support bounds. | Proved + checker + affine auditor | yes / no | **§2.1: correct** |
| TC | Tao clock preprint, `preprints/tao_clock_audit/` | Coherent first-entry limit laws for all thresholds; joint laws with r-independent error; clock identities; tightness equivalence (CLM-COL-000187/188). | Proved; Tao Prop. 1.11 cited | `check_finite.py` / no | **§3: correct deduction** |
| RC | Research companion, `research_companion/chapters/01–05` | Arctangent/Gaussian relation lattices (CLM 169–172); a registered **conjecture** (CLM 173, Collatz–Machin rigidity); groupoid/toric period maps (177–180); affine packets, parity necklaces, signed necklace count (182–192, 200); packet fixed-point series and poles (197–199). | Proved / conjecture registered | certificates / no | Not audited |
| Q | Early programme, `research_program/main.tex`, `chapters/00–04` | Residue cylinders, dyadic uniformity, a recursive sieve semigroup with a finite k ≤ 34 certificate, a record-tail conjecture, and a Bost–Connes–Marcolli/adelic route. | **Quarantined** | scripts / no | §4 |

---

## §2 In-depth audits

### 2.1 All-even join extension (Ch. 20, 16 September 2026)

**Definitions.** X is the set of positive odd integers and T(n) = (3n+1)/2^{ν₂(3n+1)}.

For even e ≥ 2:
- h_e = (2^e+2)/3 and t_e = ν₃(h_e).

For b ≥ 1 and σ ∈ {0,1}:
- a = min{a ≥ 1 : 2^{a+e+2b−σ} < 3^{a+b}};
- J = 2^{e+2b−σ}, Q = 3^{a+b}, K = 2^a J;
- (d_σ, r_σ) = (4, 3) or (32, 27);
- n₀ is the CRT solution in (0, d_σ Q) of n ≡ r_σ (mod d_σ) and Jn + h_e 3^b ≡ 0 (mod Q);
- m₀ = (K n₀ + 2^a h_e 3^b)/Q − 1.

The words are:
- left word l₀ = (1) and l₁ = (1,2,1);
- right word w₀ = (1^a, e, 2^{b−1}, 3) and w₁ = (1^a, e, 2^{b−1}, 1, 1, 3).

**Statements and proof steps, with verdicts.**

1. **Lemma 1: ν₃(h_e) = ν₃(e−1).** Put k = e−1, which is odd. Then 2^e + 2 = 2(1 + 2^k), and lifting-the-exponent gives ν₃(2^k + 1) = 1 + ν₃(k). The note proves this by the cubing step x³−1 = (x−1)(x²+x+1), which is correct. **Correct.** Checked for all even e ≤ 4000, with h_e ≡ 2 (mod 4).

2. **Bound on a: e ≤ a ≤ b + 2e − 2σ, and a > t_e.**
   - At a = b + 2e − 2σ, K/Q = (8/9)^{b+e−σ} < 1.
   - If a ≤ e−1, then (3/2)^a < 2^{e−1}, but contraction needs (3/2)^a > 2^{e−σ}(4/3)^b.
   - **Correct.**

3. **Theorem 2.** For every v ≥ 0, n(v) = n₀ + d_σ Q v and m(v) = m₀ + d_σ K v satisfy:
   - n →(l_σ) y ←(w_σ) m, with exact valuations;
   - 0 < m < n;
   - ν₃(n) = b + t_e.

   The converse also holds: the endpoint equality gives exactly this progression.

   Steps:
   - 3^b ∣ n. Writing z = n/3^b gives ν₃(z) = t_e.
   - W = (Jz + h_e)/3^a has ν₂(W) = 1.
   - m = 2^a W − 1. The first a values are x_j = 3^j 2^{a−j} W − 1, each with exponent exactly 1.
   - Using 3h_e − 2 = 2^e, the next exponent is exactly e (since 2b − σ ≥ 1).
   - The (b−1) exponents equal to 2 follow, then the tail.
   - σ = 0: 3(4n+1) + 1 = 4(3n+1), giving exponent 3.
   - σ = 1: the valuations follow from n ≡ 27 (mod 32).
   - Height: m = (K/Q)n + h_e(2/3)^a − 1, and h_e(2/3)^a < ((2 + 2^{2−e})/3)(3/4)^b < 1.

   I re-derived every step. **Correct and complete.** Checks:
   - 260 families (b ≤ 10, e ≤ 26, both σ), 8,060 pairs including v up to 10³⁰. PASS.
   - Converse: all odd m < 2²¹ scanned for 6 families; the found pairs are exactly the progression members. PASS.

4. **Theorem 3 (finite membership).** For odd n > 1, put k(n) = ⌊log₂(n−1)⌋ − 1. Any admitted template has:
   - e ≤ k(n);
   - b = ν₃(n) − ν₃(e−1);
   - a ≤ a′ ≤ A_max = ν₃(J(n/3^b) + h_e).

   The proof is sound: m + 1 = 2^{a′}W ≥ 2^{a′+1} and m + 1 ≤ n − 1, and adjacent sources satisfy T(m_{a′+1}) = m_{a′}. **Correct.** I compared this search with a brute-force backward search that allows any even e ≤ 60 and unbounded b and a′:
   - identical on all odd n < 400,000 (only 367 of these sources admit any template; max e = 4);
   - identical on 3,144 large sources with e up to 12. PASS.

5. **§5 progression.** n = 20,241,207 + 1,549,681,956v and m = 14,024,703 + 2³⁰v reach the common value 30,361,811 + 2,324,522,934v, with words (1) and (1¹⁶, 8, 2, 3).
   - At v = 0 the peak is 9,211,998,293 = (4096/9)n + 85.
   - The clock is 1 − 19 = −18, and ν₃(n) = 2.
   - The R₀ budget holds.

   All verified for v < 3000 and 200 random v < 10⁹. The e = 4 family (45,243 + 69,984v, etc.) is also verified. **Correct.**

   The added claim that every source in the progression was a root of the previous reduction depends on the predecessor's finite mask (period 5,668,704) and on a periodicity-in-v argument (period 8). **I verified it only by re-running the workbench checker (PASS), not independently.**

6. **§6: retraction identities (18) and (21), and Theorem 4.**
   - Identities: d_εH = I − Q, Q² = Q, HQ = 0, d_εF = Qd_ε, F² = F, FH = 0. These follow by induction from H(V_n) = B_n + q^j H(V_m), Q(V_n) = q^j Q(V_m) and F = I − Hd_ε. I re-derived them; they hold for any terminating strictly decreasing move rule. I also tested them over ℤ[ε]/(ε²) on a toy retraction for all odd n ≤ 60,001 (180,000 identity checks). PASS.
   - Theorem 4 (support at most R₀(n) in the budget-preserving mode) holds by construction, given the predecessor's R₀ property for old moves. **That property is inherited from Ch. 19 and was not re-proved here.**
   - R₀(n) ≤ 64 n^{log₃4} + 21 for n ≥ 27: my check passed for odd n ≤ 200,001, and the algebra is sound.
   - The unrestricted bound R_*(n) and the edge count K_*(n) follow from a′ ≤ k(n) and b ≤ ⌊log₃ n⌋, as written. **Correct.**

**Verdict: correct at its stated scope.** What the note establishes:
- explicit, complete two-template families of Collatz orbit mergers for every even interior exponent;
- a proved finite search at each source;
- chain-level bookkeeping that keeps a support bound.

What it does not establish:
- The note itself says that the finite search does not show a template applies to every retained source.
- Coverage is sparse: templates need 3 ∣ n and n ≡ 3 (mod 4), and only 367 of 199,999 odd n < 400,000 admit one.
- No convergence statement follows.

### 2.2 Split-zero histories and Hurwitz zero clusters (`split_zero_history_20260913/note.tex`)

**Statements.**
1. **Proposition (lift).** The composition of T_d^{(q)}(x) = (q^d x + d)/2, for d ∈ {0,1}, equals (q^m x + P_w(q))/2^N, where P_w = Σ d_j 2^j q^{m−1−s_j}. The map w ↦ (N, P_w) is injective, and n realizes w ⟺ 3^m n + P_w(3) ≡ 0 (mod 2^N). The reversal identity is X_{w^rev} = 2^{−N}P_w.
2. **Loss computations.**
   - X_v − X_u = (q−3)(q+4)/32, with both equal to 19/32 at q = 3.
   - The eigenvalues of the affine matrix do not see bit order: (0,1) and (1,0) have the same spectrum.
3. **Odd-return lemma.** Residues r_w mod 2^{A+1} are exact and pairwise distinct within W_{m,A}. Rotation: 3B_w + D = 2^{a₁}B_{σw}.
4. **Cluster lemma.** Take Z_λ(s,t) = Σ_w λ_w ζ(s, 1 + t r_w), with |t|(2^{A+1}−1) < 1, and a nontrivial zero ρ of multiplicity r. The t-jet of the monic cluster polynomial up to order J determines (M₁, …, M_J), and conversely. The recursions are explicit (Rouché, contour power sums, Newton identities, factorization Z = UQ).
5. **Theorem.** Jets of order K−1 determine λ (Lagrange interpolation on distinct nodes). Order K−2 is not enough (explicit pair λ^± = 1/K ± εh_w).
6. **Example (m, A) = (2, 4).** λ₍₂,₂₎ = (M₂ − 48M₁ + 551)/504, together with the simple-zero formulas for M₁ and M₂.

**Proof check.**
- Items 1–3 and 5 are elementary and correct. The realization and cylinder lemmas are classical (Terras-type), and the note does not claim them as new.
- Item 4: the Taylor expansion (DLMF 25.11.10) and the non-vanishing of b_j(ρ) = (−1)^j (ρ)_j ζ(ρ+j)/j! for j ≥ 1 are correct. The triangular inversion is correct. Holomorphy of the quotient U is argued adequately. No gap found.

**Checks.**
- All words of length ≤ 10: lift formula, injectivity and reversal identity.
- Realization and the words ↔ residues bijection for N ≤ 12.
- All 105 packets with A ≤ 14: exact and distinct residues, and the rotation identity.
- Sharpness identities for 36 packets.
- **Numerical test of the analytic claim.** At ρ₁ = ½ + 14.1347…i (mpmath, 40 digits), I solved for the zero trajectory of Z_λ(·, t) with |t| ≤ 2·10⁻⁶. I estimated c₁ and c₂ by finite differences, then applied the note's M₁ and M₂ formulas:
  - uniform weights: recovered M₁ = 16.3333…, M₂ = 401.000…, λ₍₂,₂₎ = 0.33333…;
  - weights (0.5, 0.2, 0.3): recovered M₁ = 18.4 and M₂ = 433 exactly to displayed precision, and λ₍₂,₂₎ = 0.2.
  - The workbench's own checker does no numerical zeta computation.

**Verdict: correct.** The scope matches the note's own framing. This is an exact, invertible encoding of a finite probability vector on words into zeta-zero displacements. The Hurwitz family is built from the weights, so it gives no information about orbits, and any nontrivial zero works. It has no bearing on RH or on Collatz dynamics, and the note says so.

### 2.3 History laws and the Gaussian threshold (Ch. 1)

**Statements.** Take N consecutive odd starts, beginning at 2b+1. Let P be the law of the first m exponents (a₁, …, a_m) and G_m(w) = 2^{−A(w)}.
- **(2.1)** Exact count C = ⌊(b+N−1−h_w)/2^A⌋ − ⌊(b−1−h_w)/2^A⌋. Hence |P(w) − 2^{−A}| ≤ 1/N.
- **(3.2)** For every H: max{0, Q_m(H) − N·2^{−H−1}} ≤ Δ ≤ min{1, Q_m(H) + C(H,m)/N}, where Q_m(H) = P(Bin(H, ½) ≤ m−1).
- **Refinements.** (3.3) rounding version; (3.4) support-size bound; (3.5) exact dyadic identity when N = 2^L.
- **Theorem 4.1.** For m_N = ⌊L/2 + c√L⌋ with L = log₂N, sup_b |Δ − Φ(2c)| → 0.
- **Off-critical bounds (4.3)–(4.4).** Δ → 0 when m ≤ (½−δ)L and Δ → 1 when m ≥ (½+δ)L, both uniformly in b.
- **(6.1)** A first-descent counter with exact overflow.

**Proof check.**
- The cylinder lemma is classical, and the note credits Tao's Prop. 1.9 mechanism.
- Upper bound: Δ = 1 − Σ min(P, G). Lower bound: supp P has at most N words, each with G-mass ≤ 2^{−H−1} when A > H.
- Theorem 4.1 is a squeeze with H± = L ± L^{1/4} and the binomial central limit theorem. The threshold (2m−2−H)/√H tends to 2c.
- The Hoeffding constants in (4.3)–(4.4) are right.
- **All correct.**

**Checks.**
- Lemma 2.1 on all odd n < 2²⁰ for m ∈ {1, 3, 6}: 1.57M cases.
- Counts over 72 (N, b, m) cases, including b = 10³⁰+3.
- 2,952 sandwich and refinement checks over H ≤ 40; (3.4) in all cases; (3.5) exact in 36 dyadic cases.
- Descent fixture: 3,929 accounted, 167 overflow, bounds 3,320..3,487, direct count 3,487. This matches the note exactly.
- Gaussian window (display only): at N = 2²⁰, TV = 0.004, 0.044, 0.342, 0.668 and 0.895 for c = −1, −½, 0, ½, 1, against Φ(2c) = 0.023, 0.159, 0.5, 0.841 and 0.977. Convergence is slow, as the note warns; much of the gap at c = 0 is the −2/√L term.

**Verdict: correct.** The note makes no priority claim. I did not search whether this threshold statement is already in the literature.

### 2.4 Stopped affine transport (Ch. 2), audited parts

Audited statements:
- **Prop. 1.2 (exact cylinder).** Classical.
- **Theorem 2.1.** Let a word p have F_j(3) ≥ 3 for j < m and F_m(3) < 3. Then 3D_m > C_m > 0, and every actual n ≥ 3 in the cylinder satisfies T^m(n) < n. The proof: D_m n ≥ 3D_m > C_m.
- **Theorem 3.1.** Restart chart on progressions a + 2dt, with gcd mask g ∣ c.
- **Theorem 7.1.** (√((x−2)/2) + √((3x−1)/2))/2 ≤ (√15/4)√(x−1) for x ≥ 3, with equality at x = 7. This is Cauchy–Schwarz with weights (½, 1).
- **Tail bounds** (7.9)–(7.16): S_h ≤ √2(√15/4)^{h−1} ≤ (3/2)(31/32)^h, the recurrence t_H = (t_{H−1} + S_H)/2, t_H ≤ (31/20)(31/32)^H, and the leaf count.

All steps check.

**Checks.**
- All 1,601 reference-3 leaves with A ≤ 16.
- 9,605 actual starts descend as claimed.
- Survival to h = 22 checked exactly.
- (7.14) and (7.16) match a direct leaf enumeration.

**Verdict: correct for the audited parts.**
- §7 is a statement about the fair-bit **reference model** only. The note says this explicitly, and it is not a statement about individual orbits.
- §§4–6 and 8–10 (image cohomology, stopped law, Hurwitz bridge) were not audited. The workbench checker reproduces its recorded JSON exactly.

### 2.5 Cycle-relative cohomology (Ch. 3)

Audited statements and their standing:

| Statement | Content | Standing |
|---|---|---|
| Thm 1.1 | F_p B_p = D e₁ᵗ; det B_p = (−1)^{m−1}D; coker B_p ≅ ℤ/D with [1] ↦ [C]; rational cycle x_i = C(p_i)/D | Correct |
| Thm 3.1 | Positive integer cycle ⟺ D > 0 and D ∣ C | Correct; the classical rational-cycle criterion (Böhm–Sontacchi/Lagarias lineage, credited to Lagarias) |
| §3 exclusion | No nontrivial positive cycle with 0 or 1 exponent-1 positions | Correct. My check of the minimality step: any later value x ≤ (3n+1)/2 with exponent ≥ 3 maps to at most (9n+5)/16 < n. Then D_m = 2·4^{m−1} − 3^m, and gcd(D, 6) = 1 forces \|D\| = 1. |
| Thm 4.1 | Relative H₀ and H₁ of the orbit graph | Correct (functional-graph facts) |
| (5.1) | Collatz ⟺ H₀ = 0 ⟺ … ⟺ a nonnegative primitive h with δh = 1 exists | Correct (h is the stopping count) |
| Thm 6.1 | Retraction identities; ∂c = 0 ⇒ Fc = c | Correct |

**Checks.** On all 16,383 words with A ≤ 14:
- F_p B_p = D e₁ᵗ and gcd(D, 6) = 1;
- det B_p (for m ≤ 7);
- the only D > 0, D ∣ C cases are repetitions of (2), and each has the stated actual word.

**Verdict: correct.** Much of this reformulates classical facts. The note is appropriately modest; it states that its small exclusion does not supersede the published cycle results.

### 2.6 Intrinsic first-jet group (Ch. 9), as summarized in the overview

**Statement.** B := ker(H¹(K_ε) → H¹(K)) ≅ C¹/(dC⁰ + P ker d) ≅ ⊕_{nontrivial cycles} ℤ/m_C ⊕ ⊕_{nonperiodic components} ℤ, and every positive integer reaches 1 ⟺ B = 0.

**Re-derivation.**
- In the functional graph, ker d is spanned by the actual directed cycles.
- P of a cycle equals the sum of its vertices, which is m times the component class.
- The loop at 1 contributes ℤ/1 = 0, and B = 0 ⟺ every component contains 1. An undirected path to 1 forces the forward orbits to merge.
- The certificate u = −E₁, v = Σ(path edges) satisfies du = 0 and dv − Pu = V_n.

**Verdict: correct.** This is an exact algebraic restatement of the conjecture, not progress on it. The workbench says the global assertion B = 0 is not established.

### 2.7 Cycle-sector exclusions (Ch. 6 Thm 9; Ch. 10–11 earlier versions)

**Statement.** No nontrivial positive cycle has at most 678 exponent-1 positions in its primitive odd-return word.

**Proof.** It uses minimum s = 330,751 (Thm 8: all odd n ≤ 330,749 reach 1, by the workbench's own database).
- (C35): with k exponent-1 positions, (4s)^m ≤ 2^k(3s+1)^m.
- (C36): no power of 2 lies in (3^m, (3+1/s)^m] for m ≤ 1635.
- (C37): (4s)^{1634} > 2^{678}(3s+1)^{1634}.

I re-derived the logic and verified (C36) and (C37) exactly. **Correct.** The workbench labels it an internal bound, not a claim to exceed published cycle bounds. That label is accurate: "k" counts exponent-1 positions, not Hercher's m-cycles. The literature reader records published verification ranges: Barina 2021, n < 2^68; Barina 2025, n < 2^71 (`tex/chapters/01k_computational_verification.tex`, table lines 380–382). Using those as s in the same argument would give far stronger bounds.

---

## §3 The Tao clock preprint (`preprints/tao_clock_audit/`)

**What it adds beyond Tao v7**, based on `sections/consequences.tex` and claims CLM-COL-000187/188.

**Setup.** Fix a base b and put t_j = b^{α^j} with α = 1001/1000. Let μ_s be the log-weighted law on the odd integers in [s, s^α]. Let K_x be the push-forward by first entry p_x into [1, x], with a failure state †.

- **Coherent first-entry limits (Cor. "cor:limit").** For every x, λ_{x,j} = K_x μ_{t_{j+1}} converges in ℓ¹ to λ_x^{∞}.
  - Rate: ‖λ_{x,j} − λ_x^∞‖ ≤ L_c(log t_j)^{−c} for x ≤ t_j, where L_c = B′/(1 − α^{−c}).
  - Exact compatibility: K_x λ_y^∞ = λ_x^∞ for x ≤ y.
  - Failure mass: at most B x^{−c/α} + L_c α^c (log x)^{−c} for x ≥ b.
- **Joint first-entry laws (Cor. "cor:joint-entry").** For thresholds x₁ ≤ … ≤ x_r, the joint law converges with the same error, with no factor depending on r. The map J(z) = (p_{x₁}(z), …, p_{x_r}(z)) is a bijection onto compatible tuples; its inverse is the last projection, so the push-forward is an ℓ¹ isometry.
- **Weighted tightness equivalence (Prop.) and exact C/T/S clock identities.** The fixed-threshold and diverging-threshold orbit-minimum theorems are reproduced and attributed to Tao. The preprint says it proves no stronger orbit-minimum bound, and that independence from an arbitrary different base is not established. Both statements are accurate.

**Proof check.**
1. Nested passage gives p_x∘p_y = p_x = p_y∘p_x.
2. Push-forward is an ℓ¹ contraction.
3. Tao's Prop. 1.11 gives the adjacent-scale error. The "unmerge" inequality keeps † separate at the cost of 2|Δ(†)|.
4. The errors sum as a geometric series: Σ_{i≥j} (α^i log b)^{−c} = (log t_j)^{−c}/(1 − α^{−c}).
5. Completeness of ℓ¹(E_x) gives the limit.
6. Continuity of K_x gives compatibility.
7. For the failure mass, choose r = t_k ≤ x < r^α and use p_r(†) = †.

I found no gap. **Verdict: a correct but modest deduction from Tao's Prop. 1.11.** Tao's proposition itself is cited, not re-proved. I did not audit `sections/repairs.tex`, the stated local repairs to Tao's §§5–6.

**Checks.**
- Nested passage on all odd n < 10⁶ for 7 thresholds (14M checks).
- J bijection on E_{100000}.
- ℓ¹ contraction on random signed measures.
- The clock identity Σ_{n≤X, C_min(n)>K} 1/n = Σ_a 2^{−a} Σ_{m≤X/2^a odd, S_min(m)>K} 1/m. **For 3x+1 both sides are 0 on every verified range, so the test is vacuous there.** I therefore tested the same mechanism on the 3x−1 map, which has nontrivial cycles. There it holds exactly with nonzero values (e.g. 6.0633 at X = 50,000, K = 4).
- The preprint's own `check_finite.py` passes.

---

## §4 Negative results and quarantined attempts

**Quarantine.** Source: `research_program/QUARANTINED.md` and `research_program/README.md`.
- **What is quarantined:** the early `research_program/main.tex` tree. Its chapters cover:
  - residue cylinders;
  - dyadic uniformity;
  - a recursive sieve semigroup, with a finite certificate for k ≤ 34 tied to the published sieve code;
  - a record-tail observable, with a "record-gap and record-tail genericity" **conjecture** (tail averages → 1/6, W(r)/g_r → 1/18);
  - a proposed Bost–Connes–Marcolli/"adelic" construction, which is **rejected in full**.
- **Scope.** The quarantine is a **process decision** (directive USR-0004). It does not show any of these statements false. It withdraws them from use until they are independently re-derived. Only a bibliography entry of the BCM construction survives in the repo (`chapters/99_references.tex`). The notice does not cover the dated 13–16 September notes.

**Proved negative or obstruction results inside the audited notes, with exact scope:**

- **Ch. 1: full-history obstruction.** For uniform samples of N consecutive odd starts, the whole first-m-exponent word law is at TV distance → 1 from the geometric model once m ≥ (½+δ)log₂N.
  - What fails: approximation of the full word law.
  - What it does NOT show: it says nothing about coarser observables (entrance locations, descent), and nothing about individual orbits.
- **Split-zero: three information losses, each shown by an explicit witness.**
  - The specialization q → 3 is not injective on histories (the (q−3)(q+4)/32 pair).
  - Eigenvalues of the affine matrix lose bit order.
  - (K−2)-jets cannot separate all weight vectors.
  - What it does NOT show: that no faithful spectral encoding exists. The (K−1) encoding is faithful.
- **Ch. 3.**
  - The formal inverse (I − tP)^{−1} is not a finite integral chain on cycles or divergent rays.
  - The signed primitive of the unit cochain is unbounded below on an acyclic component.
  - These identify what extra input a global proof would need. They are not obstructions to the conjecture.
- **Ch. 20.** The finite template search does not prove that some template applies at every retained root, and the residual root set remains open.
- **Ledger items against printed literature** (not audited; listed with the workbench's labels):
  - CLM-COL-000006, 021, 025: counterexamples to printed statements;
  - 034: contradicted as stated, then repaired;
  - 038, 041: not certified as printed;
  - 042: correction required;
  - 149: raw weighted-path algebra type failure;
  - 157: raw transducer counterexample;
  - 159: obstruction to a raw tropical algebra map;
  - 162: no branch map on a formal point.

  These concern defects in sources or in earlier drafts. They are not results about Collatz orbits.

---

## §5 Overlaps with other programmes

| Link | Collatz locator | Other side | Type |
|---|---|---|---|
| Hurwitz zero-cluster reconstruction | `split_zero_history_20260913/note.tex`, Lemma 4.1 / Thm 4.2 | `zeta-function-research-reader` @ `16fc4dbb817b`, `workbenches/splitzero-tandem/continuations/20260913-toda/tex/historical_hurwitz_jets.tex`, eqs. H10–H13 (from `RESEARCH_MAP.json`) | **Imported dependency, re-proved locally.** The note re-proves the part it uses; I confirmed it numerically (§2.2). |
| Support-idempotent homogenisation (x,h) ↦ (ax+bh, h) | `split_zero…/note.tex` §2.1: branch matrices M₀ = [[½, e],[τ, 1]], M₁ = [[q/2, ½],[τ, 1]] acting on (x,h); `AUDIT.md` item 3 | Local note, "Support-Idempotent Homogenization for a Split-Zero Collatz F-Series Frame" (April 2026; private path) | **Same identity / imported definitions.** The affine branch is written as a homogeneous 2×2 matrix. Only the finite branch matrices and prefix formula are used. |
| Split-Zero support modules and killed-representative quotient | Ch. 7 `completion_defect…/note.md` §1; Ch. 8 `supported_structure…/note.md` ref. [SZ]; Ch. 15 `SOURCE_INTAKE.json` | `zeta-function-research-reader` @ `91ed3b7c`, `formal/splitzero/DERIVED_MATHEMATICS.md` §§1–4; read-only pin `1efd5333` | **Imported construction**, instantiated on the Collatz operator. Ch. 6 states it builds no map from the whole zeta theta quotient. |
| Erdős–Straus R05 (T(n) = 4n+1, θ(n) = 3n+1, θT = 4θ, U(Tʲn) = U(n)) | `all_even…/note.md` §3, proof of Thm 2: the σ = 0 right path ends at 4n+1, and exponent 3 sends it to (3n+1)/2, because 3(4n+1)+1 = 4(3n+1) | Erdős–Straus workbench R05 (not accessible here) | **Same classical identity** (n and 4n+1 have the same odd successor). No recorded dependency either way. The only "Erdos Strauss" strings in the repo are a local folder name in provenance paths (`certificates/affine_packet_source_and_cycle_checks.py` lines 41, 59; `qa/KOHL-F003…md`). |
| Yang–Mills regression fixture (q−3)(q+4)/32 | `split_zero…/note.tex` §2.1 (X_v − X_u); checked in `check_history.py`, numerator [−12, 1, 1] | Yang–Mills workbench (not accessible here) | **Shared fixture, same identity.** No mention of Yang–Mills anywhere in the Collatz repo. It is a polynomial identity with no mathematical dependency. |

---

## §6 What I did not check

- **Chapters not audited:** 4–8 and 10–19 beyond their opening paragraphs and theorem headings, except the Theorem 9 inequalities in Ch. 6.
- **Specific dependencies not checked:**
  - Ch. 13's use of Matveev's bound.
  - The 11,610-step crossing horizon and the large ledgers (`sources11610.jsonl.gz` was not exported).
  - The predecessor-root claim for the e = 8 progression; I only re-ran the workbench checker.
  - The R₀ budget proof in Ch. 19.
- **Tao material not checked:** Tao's Prop. 1.11 itself; the preprint's `repairs.tex`, `transport.tex` and `versions.tex`; the literature-reader reconstructions of Tao v7.
- **Other parts of the workbench not audited:** the Siegel edition; the literature reader and QA audits; the research companion (CLM 169–200, including conjecture CLM 173); the Lean project (not built).
- **Novelty:** I did no literature search. I make no statement about whether any workbench result is new.
- **Other repositories:** the zeta, Erdős–Straus and Yang–Mills repositories were not accessible. Their sides of §5 are described only from the Collatz-side references.

---

## §7 Results that stand without the workbench's vocabulary (candidates for a reader)

1. In any N consecutive odd numbers, the count of starts with a given pattern of halvings after each 3n+1 step is an exact floor formula, and it is within 1 of N/2^A.
2. The first m halving counts of N consecutive odd starts look like independent fair geometric variables when m < (½−δ)log₂N, and not at all when m > (½+δ)log₂N. At the boundary, the TV distance tends to Φ(2c). All finite bounds are explicit.
3. For example, 14,024,703 + 2³⁰v and 20,241,207 + 1,549,681,956v reach the same odd number, 30,361,811 + 2,324,522,934v, for every v ≥ 0. More generally there are explicit merging families for every even exponent e, with ν₃((2^e+2)/3) = ν₃(e−1).
4. Whether a given odd n is the larger member of such a family is decided by a short finite search at n.
5. If a halving pattern sends 3 below 3, then every start ≥ 3 with that pattern falls below itself at the end of the pattern.
6. No nontrivial Collatz cycle has at most one "3n+1 followed by a single halving" step. With verification to 330,749, none has at most 678 such steps. This is weaker than published cycle bounds and uses a different count.
7. Every positive integer reaches 1 if and only if an explicitly presented abelian group vanishes. That group is a sum of ℤ/(cycle length) for each nontrivial cycle and ℤ for each divergent component. This is a restatement, not progress.
8. Tao's theorem yields one consistent family of limiting distributions for where the odd orbit first enters [1, x], for all x at once, along one scale sequence. Joint laws converge with error independent of the number of thresholds. Tao's bound itself is not strengthened.
9. In the fair-coin model of halving and tripling, E√(X−1) shrinks by at least √15/4 per step, with equality only at x = 7. This is a model statement, not one about individual orbits.
10. A probability vector on the K odd-step words with fixed (m, A) can be read back exactly from how a zeta zero moves under an explicit Hurwitz-zeta deformation to order K−1, and order K−2 is not enough. This is an encoding and carries no dynamical information.
