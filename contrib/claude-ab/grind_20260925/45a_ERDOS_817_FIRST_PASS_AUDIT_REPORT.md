# First-pass mathematical audit: Erdős Problem 817 workbench

Prepared by Claude (Opus 5.5), 26 September 2026. This is a read-only audit for a public reader. Nothing in the repository was modified, committed or pushed. Quotations are at most 15 words; everything else is paraphrase. "My check" means a computation written for this audit, not a workbench script.

Verdict vocabulary used below:

- **Verified**: I read the whole proof, found every step correct, and ran independent checks where possible.
- **Verified (finite)**: the stated finite certificate was recomputed independently and agrees.
- **Read, plausible**: I read the statement and the proof outline. I found no error, but I did not check every step.
- **Statement only**: only the statement was read.

---

## 0. Sources and method

**Repository.** KokunoYumeto/erdos-problem-817-workbench, `origin/main` = `dbd0a93` (16 Sep 2026), a shallow, sparse, partial clone. Files were read with `git show origin/main:<path>`. Line numbers ("L") refer to that commit.

**Read in full:**

- `README.md`, `STATUS.md`, `problem/statement.md`, `corpus/claims.ndjson` (11 records);
- `paper/ep817_k4_rate.tex` (579 lines; every line read);
- `formal/lean/ErdosProblem817/Core.lean` (214 lines) and `Extended.lean` (544 lines), plus `Main.lean` and `Audit.lean`;
- `notes/ternary-variance-lower-bound.md` (EP-03);
- `notes/general-k-capacity.md` (EP-04, 580 lines);
- `research/graphical_obstructions/notes/graphical-obstructions.md` (EP-05, 531 lines);
- `research/finite_period/notes/finite-period-control.md` (EP-08, 454 lines);
- `editions/cumulative_20260916/NOTE_INDEX.md` and `PUBLICATION_NOTES.md`;
- the finite-period receiving map `interfaces/zeta/workbenches/ep817-finite-period/notes/splitzero-receiving-map.md` (L1–125).

**Read in part** (statements, READMEs, selected sections):

- the READMEs of `splitzero_outer`, `cone_dual`, `seven_observable`, `all_block_image` and `recurrence_control`;
- the theorem headings of the recurrence, canonical-isolation, cone-dual and local-flow notes;
- `seven-observable-capacity.md` §4.1 (the L > 3Q step);
- `recurrence-control.md` §§2–3 (Theorems R1, R2);
- `all-block-image-capacity.md` §1 (Theorems A–C).

**Inventory used:** `WORKBENCH_SURVEY.md` §6 (EP-01…EP-10) and §8 (OV-18, OV-22, OV-23).

**Method.** I re-derived every step of the k = 4 proof by hand. I then wrote independent programs, using exact integer or `Fraction` arithmetic; floats appear only in display lines.

| Script (in `audit45/`) | Output | What it does |
|---|---|---|
| `g4_bruteforce.c` | `g4_bruteforce_OUTPUT.txt` | Exact g₄(n), n ≤ 6: branch-and-bound over increasing sets, pruning by heredity |
| `g4_decreasing.c` | `g4_decreasing_OUTPUT.txt`, `g4_decreasing_noprune_OUTPUT.txt`, `g4_n7_OUTPUT.txt` | Second implementation: fix the maximum N, search downward. Run with and without the lemma-based pruning. The n = 7 run is capped at 240 s. |
| `g4_upper7.c` | `g4_upper7_OUTPUT.txt` | Capped 150 s search for an explicit admissible 7-set |
| `g4_small_confirm.py` | `g4_small_confirm_OUTPUT.txt` | Pure-Python confirmation of g₄(1..5) and of the witness sets |
| `ep817_k4_checks.py` | `ep817_k4_checks_OUTPUT.txt` | Mod-19 kernel, digit rigidity, lift, and all structure lemmas on exhaustive domains; EP-03 polynomial and variance identities; bounds table |
| `ep817_continuation_checks.py` | `ep817_continuation_checks_OUTPUT.txt` | EP-04, EP-05 and EP-08 certificates |
| `ep817_fp3_matrix_check.py` | `ep817_fp3_matrix_check_OUTPUT.txt` | EP-08: an independently built 7-state automaton, rank-one product, crossing scalars |
| `ep817_light_checks.py` | `ep817_light_checks_OUTPUT.txt` | EP-07 C5 and EP-09 R1/R2 spot checks |

**Limits.**

- No Lean toolchain is installed (no `lean`, `lake` or `elan`), so the Lean files were read but not built.
- No web access was used, so novelty and the external papers (Korsky, Costa, Erdős–Sárközy) were not checked.
- PDFs and release ZIPs were not opened.

---

## 1. The problem as the workbench states it

Source: `problem/statement.md` L3–20; paper L78–87.

- For a finite set A of **distinct positive integers**, H(A) = {Σ_{a∈A} ε_a a : ε_a ∈ {0,1}}. The empty sum 0 is included, and each value is counted once (H is a set).
- **g_k(n)** is the least N such that some n-element A ⊆ {1,…,N} has H(A) free of nonconstant k-term APs (x, x+d, …, x+(k−1)d) with d ≠ 0. Equivalently, g_k(n) is the least possible max A over such A.
- The workbench studies the rate lim g₄(n)^{1/n}. It says it does not redefine the broader problem, which asks for estimates of g_k for all k ≥ 3.
- It attributes the historical k = 3 question to Costa (arXiv:2609.06303v1), who is reported to prove liminf g₃(n)/3ⁿ = 0. I did not check this.
- The general-k notes use the same definition (`general-k-capacity.md` L10–20) and call such A **k-admissible**.

Two consequences used below:

- **Heredity.** If A is admissible, so is every subset, because H(B) ⊆ H(A).
- **Monotonicity.** g_k is strictly increasing in n (delete the maximum).

---

## 2. EP-01, the main theorem

**Statement** (paper `thm:main` L100–111; corpus MC-ERDOS-817-THM-001). For every n ≥ 1,

  (19^{n/3} − 1)/(2n) ≤ g₄(n) ≤ 8·19^{⌈n/3⌉−1},  and hence lim g₄(n)^{1/n} = 19^{1/3} ≈ 2.6684.

**Attribution** (paper L60–74; README L38–64):

- construction and proof route: an anonymous r/LLMmathematics contributor whose account was later deleted;
- reconstruction, exposition and checks: "The Clankers";
- the Lean finite upper bound: sneed-and-feed (PR #1).

**Overall verdict: Verified.** The written proof is complete and correct as written. I found no gap. The five "corrections to the source rendering" (STATUS L68–79; paper L515–524) are accurate descriptions of what the paper supplies.

### 2.1 Lemma by lemma

**LEM-RELATION-SPLIT** (`lem:split`, L121–162). **Verified.**

- Let c ∈ {−2,…,2}ⁿ with Σ cᵢaᵢ = 0. Let P_j and N_j be the sums of the aᵢ with cᵢ = j and cᵢ = −j.
- The four sums X₀ = P₁+N₂, X₁ = P₁+P₂, X₂ = N₁+N₂, X₃ = N₁+P₂ are subset sums, because the four coefficient classes are disjoint.
- Put d = P₂ − N₂. The relation gives N₁ − P₁ = 2d, and the consecutive differences are d, d, d. I recomputed all three.
- 4-AP-freeness forces d = 0, hence P₂ = N₂ and P₁ = N₁.

**Minimal blocks are disjoint** (`lem:disjoint`, L174–202; corpus LEM-BLOCKS). **Verified.**

- Apply the splitting lemma to r + s and to r − s. Their magnitude-2 layers are r·1_{E₊} and r·1_{E₋}, so both restrictions are relations.
- Minimality of r forces the nonempty one of E₊, E₋ to be all of supp r. So s = ±r on supp r.
- If s is also minimal, the supports are equal and s = ±r.

**Every signed relation is a block sum** (`lem:signed-decomp`, L211–229; LEM-BLOCKS). **Verified.**

- Existence: peel off an inclusion-minimal sub-relation, which is globally minimal. The remainder is zero on that block and has strictly smaller support. A used block cannot recur, since the remainder vanishes on it.
- Uniqueness holds coordinatewise.

**SHORT-KERNEL** (`lem:short-kernel`, L231–267). **Verified.**

- The two layers u (the ±1 part) and v (half the ±2 part) have disjoint supports, and each is a relation by the splitting lemma.
- Each decomposes over whole blocks, so α_jβ_j = 0 and t_j = α_j + 2β_j ∈ {−2,…,2}.
- The converse direction also holds.

**Blocks have size ≥ 3** (L269–272). **Verified.** Sizes 1 and 2 would force a zero element or two equal elements.

**EQ-TERNARY-COUNT** (L274–318). **Verified.**

- Φ(x) = Φ(y) on {0,1,2}ⁿ iff x − y = Σ t_j r^{(j)}. The equivalence relation is a product over blocks, and free coordinates are fixed.
- The reflection F_j (xᵢ ↦ 2 − xᵢ where r_i = −1) turns the block relation into diagonal translation.
- Classes are counted by representatives with minimum 0: 3^m − 2^m of them. So |T(A)| = 3^t ∏(3^{m_j} − 2^{m_j}).

**Lower bound** (L320–343). **Verified.**

- f₃ = 19 and f_{m+1} = 3f_m + 2^m > 3f_m, while 3 > 19^{1/3}. So f_m ≥ 19^{m/3} and 3^t ≥ 19^{t/3}, giving |T(A)| ≥ 19^{n/3}.
- T(A) ⊆ [0, 2Σaᵢ] ⊆ [0, 2nN]. So 19^{n/3} ≤ 2nN + 1.

**COR-FINITE-LOWER** (`rem:finite-lower`, L345–356; credited to The Clankers). **Verified.** Distinct elements give Σaᵢ ≤ nN − n(n−1)/2, hence g₄(n) ≥ ⌈(19^{n/3} + n(n−1) − 1)/(2n)⌉.

**MOD19-KERNEL** (`lem:mod-kernel`, L374–397). **Verified.**

- With p = u + w and q = v + w: |p + 7q| ≤ 32, so p + 7q ∈ {0, ±19}.
- p + 7q = 19 forces (p,q) = (−2,3), which is impossible, since v + w = 3 forces w ≥ 1 and then u + w ≥ −1.
- p + 7q = 0 forces p = q = 0, so (u,v,w) = t(1,1,−1).

**DIGIT-RIGIDITY** (`prop:digit`, L399–433). **Verified.**

- D = {0,1,7,8,9,15,16}; the value 8 arises twice, as 8 and as 1+7.
- Second differences of binary representatives are kernel vectors, hence multiples of (1,1,−1).
- Project with π(a,b,c) = (a+c, b+c). The projections form an integer 4-AP in {0,1,2}², so its step is 0 and all values are equal.

**THM-LIFT** (`prop:lift`, L435–479). **Verified.**

- H(A_m) is the carry-free base-19 language with digits in D (all digits ≤ 16 < 19).
- A nonconstant AP has step 19^r·e with 19 ∤ e and r < m. The bound r < m holds because the language lies in [0, (8/9)(19^m − 1)] ⊂ [0, 19^m).
- Strip the common lowest r digits and divide by 19^r. Reducing mod 19 gives a nonconstant AP in D, a contradiction.

**THM-FINITE-UPPER** (L481–496). **Verified.**

- The 3m generators 19^j·{1,7,8} are distinct (by 19-adic valuation) and have maximum 8·19^{m−1}.
- For general n, take m = ⌈n/3⌉ and delete generators (heredity).

**Squeeze** (L498–513). **Verified.**

### 2.2 Independent checks (`ep817_k4_checks_OUTPUT.txt` and the `g4_*` outputs)

**The kernel, digits, lift and deletion:**

- All 125 coefficient triples satisfy the kernel statement.
- None of the 342 nonzero-step 4-APs mod 19 lies in D. Of the 7⁴ digit quadruples, exactly the 7 constant ones have both second differences ≡ 0.
- For m = 1..4, H(A_m) equals the digit language, has exactly 7^m elements, and is 4-AP-free. For m = 4 there are 12 generators and 2,401 sums, up to 115,840.
- All 64 subsets of A₂ and all 512 subsets of A₃ are admissible.

**Structure lemmas, exhaustively.** For every admissible n-subset of [1,N] I checked every relation in [−2,2]ⁿ, the zero vector included:

- relation splitting;
- disjointness of minimal blocks;
- the unique block decomposition;
- the short kernel;
- block sizes ≥ 3;
- the exact ternary-count formula (against direct enumeration of T(A));
- |T(A)| ≥ M_n ≥ 19^{n/3}.

The domains:

| (n, N) | Admissible sets | Block patterns found | Relations checked |
|---|---:|---|---:|
| (3, 40) | 7,829 | size 3 | 9,257 |
| (4, 40) | 20,176 | sizes 3, 4 | 58,940 |
| (5, 48) | 3,072 | sizes 3, 4, 5 | 15,360 |

All pass, together with the n ≤ 7 extras (the optimal sets and A₂ ∪ {361}).

**Negative controls.** Without the 4-AP-free hypothesis the count bound fails: {1,2,3} gives |T| = 13 < 19. This illustrates the paper's remark (L521–524) that the "19 classes" statement needs the ambient hypothesis.

**Exact values of g₄(n)** (my computation, not in the workbench):

| n | Paper lower | Remark lower | EP-03 combined lower | **Exact g₄(n)** | Upper 8·19^{⌈n/3⌉−1} | Optimal sets |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | **1** | 8 | {1} |
| 2 | 2 | 3 | 3 | **3** | 8 | {1,3}, {2,3} |
| 3 | 3 | 4 | 5 | **5** | 8 | {1,4,5}, {2,3,5} |
| 4 | 7 | 8 | 11 | **14** | 152 | {1,9,13,14}, {3,11,13,14} |
| 5 | 14 | 16 | 27 | **40** | 152 | 7 sets, e.g. {1,13,35,39,40} |
| 6 | 30 | 33 | 49 | **79** | 152 | unique: {2,29,45,74,77,79} |
| 7 | 69 | 72 | 132 | **176 ≤ g₄(7) ≤ 246** | 2888 | witness {1,3,39,180,219,243,246} |

How the exact values were obtained:

- The values for n ≤ 6 agree across three independent searches: the increasing branch-and-bound; the decreasing search with the lemma-based pruning; and the decreasing search without it.
- Pure-Python exhaustive enumeration confirms n ≤ 5. It lists the optimal sets, and their numbers (1, 2, 2, 2, 7) match the C searches' counts.
- The unique optimal 6-set consists of two 3-blocks (29+45 = 74 and 2+77 = 79). It has |T| = 361 = M₆, the minimum allowed by the class count.

Scope of the n = 7 bounds:

- **Lower bound 176.** The capped search found no admissible 7-set with maximum in [132, 175]. N < 132 is excluded by the EP-03 bound (verified in §3.1). The search used pruning that follows from the proved counting lemmas (heredity, a_j ≥ g₄(j), |T| ≤ 2S+1, and the EP-03 variance bound).
- **Upper bound 246.** An explicit witness set, independently confirmed admissible by the Python check.

All values respect the theorem's bounds, and the n-th roots approach 19^{1/3} slowly (n = 300: lower root 2.612, upper root 2.661).

### 2.3 Lean coverage (read, not built)

**`Core.lean`** proves, with `decide` or symbolically:

1. `bounded_kernel_mod19`: for u, v, w ∈ {−2,…,2}, 19 | u+7v+8w ⇔ (u = v and w = −u). This is exactly MOD19-KERNEL.
2. `digit_second_difference_rigidity`: four digits of D with both second differences divisible by 19 are equal. This is DIGIT-RIGIDITY in second-difference form, which is equivalent.
3. `language_four_ap_constant`: for every m, every 4-AP in the length-m base-19 language with digits D is constant. The proof peels the least significant digit by induction, not by the paper's least-differing-digit route. Both routes are valid.
4. `blockValue_is_digit`, `evaluateBlocks_mem_language` and `evaluated_blocks_four_ap_constant`: binary block choices map into the language.
5. `relation_splitting`: if S is 4-AP-free, P₁+2P₂ = N₁+2N₂, and the four sums lie in S, then P₂ = N₂ and P₁ = N₁. This is the algebraic core of LEM-RELATION-SPLIT. The step "the four sums are subset sums because the coefficient classes are disjoint" is a hypothesis, not proved in Lean. STATUS L22 accurately calls this "relation-splitting algebra"; the broader corpus wording is fine mathematically, but that combinatorial step is not formalised.

**`Extended.lean`** (sneed-and-feed):

- `generators_fourAPFree`: for every m, the subset sums of {19^j·w : j < m, w ∈ {1,7,8}} are 4-AP-free. This is THM-LIFT.
- `erdos_problem_817_upper_bound`: for every n > 0 there is B : Finset ℤ with |B| = n, 1 ≤ b ≤ 8·19^{(n+2)/3 − 1} (natural-number division), and FourAPFree(subsetSums B). The empty sum is included, and `(n+2)/3` is ⌈n/3⌉. This is THM-FINITE-UPPER exactly as the corpus states it.
- Also proved: helper lemmas (cardinality 3m, positivity, the bound, injectivity, heredity, translation invariance).

**Not formalised** (as the workbench says, STATUS L24, paper L550–553):

- g₄ itself is never defined in Lean, so the Lean theorem is the existence statement behind the upper bound;
- the minimal-block decomposition, the short kernel and the ternary count;
- the lower bound and the n-th-root limit.

The 44 axiom reports (STATUS L56–63) could not be re-run here.

---

## 3. EP-03, EP-04, EP-05, EP-08

### 3.1 EP-03: ternary-variance refinement

`notes/ternary-variance-lower-bound.md`. Status in the note: ordinary derivation; "Not Lean-checked" (L5–6). Credited as a workbench contribution; it depends on the Reddit contributor's short-kernel lemma.

**Statement** (L30–56). Write n = 3q + r and M_n = 19^q 3^r. Then:

- |T(A)| ≥ M_n;
- 19(|T(A)|² − 1) ≤ 192·Σaᵢ² ≤ 192nN²;
- hence g₄(n) ≥ ⌈√(19(M_n² − 1)/(192n))⌉ ≈ 0.315·19^{n/3}/√n.

**Verdict: Verified.** Each step was checked by hand:

- **Polynomial factorisation (L77–110).** The excluded vectors have generating function z^{S_B/2}∏(1+z^{aᵢ}). The global map from local representatives to T(A) is a bijection by the short kernel. Each factor has 0/1 coefficients.
- **Variance.** The mean is S by the symmetry x ↦ 2 − x. The per-block variance is κ_m Q_B with κ_m = (8·3^m − 3·2^m)/(12(3^m − 2^m)).
- **κ bound.** 16/19 − κ_m = 5(8·3^m − 27·2^m)/(228(3^m − 2^m)) ≥ 0 for m ≥ 3, with κ₃ = 16/19.
- **Packing.** Var ≥ (M² − 1)/12 for M distinct integers.
- **Class-count bound.** 3^m − 2^m ≥ 19·3^{m−3}, and h ≤ ⌊n/3⌋ blocks.
- **Quadratic threshold.** The completing-the-square in §6 is correct.

Computational checks:

- The polynomial identity (as a full coefficient map), the exact mean and variance, and 19(M² − 1) ≤ 192Q pass on every admissible set in the §2.2 domains.
- The §6 table is recomputed exactly: 1, 3, 5, 11, 27, 49; 724 (n = 9); 11,841 (n = 12); 352,128,817,514 (n = 30).
- The claimed "order-√n gain" holds: the ratio of the two bounds is 2√(19/192)·√n (3.45 at n = 30).
- The note claims exactness only for n ≤ 3, and my exact values confirm those. For n = 4, 5, 6 the bound (11, 27, 49) is strictly below the truth (14, 40, 79), consistent with the note's "no claim of exactness".

### 3.2 EP-04: general k

`notes/general-k-capacity.md`, 14 Sep. Status in the note: "ordinary mathematical proofs"; no new Lean (L6).

**Theorem 1: existence of Λ_k.** **Verified.**

- §3 composition. C = A ∪ R·B with R = 2S(A)+1 gives H(C) = H(A) + R·H(B) bijectively. Second differences split because |Δ²x| ≤ 2S(A) < R. So C is k-admissible, and 2S(C)+1 = (2S(A)+1)(2S(B)+1).
- §4 limit. F_k(n) = min(2S+1) is submultiplicative. The Fekete argument is written out, and 2g_k + 1 ≤ F_k ≤ 2n·g_k + 1. So Λ_k = lim g_k(n)^{1/n} = inf_n F_k(n)^{1/n} exists.
- §4 also re-derives Λ_k ≥ (k−1)/(k−2) (the one-shift chain argument; checked) and Λ_{k+1} ≤ Λ_k.

**Theorem 1: the certificate characterisation.** **Verified.**

- Λ_k is the infimum of q^{1/|B|} over pairs (q, B) with S(B) < q and H(B) mod q free of nonzero-step k-APs. Composite q and repeated residues are allowed.
- Lemma 5.1 (lifting for any q, not only primes) and Lemma 5.2 (every admissible B gives the certificate (2S(B)+1, B)) together prove the identity.

**Theorem 2: decision by a finite carry graph.** **Verified** (§6).

- The carry box [−L, L+i] with L = ⌈W/(q−1)⌉ is invariant.
- Path-to-AP and AP-to-path maps telescope. Reachability decides "k-AP-free at every length".
- For digits in [0, q−1], at most 2·k! states are needed.
- The C_k/M_k equality in §7 was read and is sound.

**Theorem 3: Λ₅ ≤ 97^{1/6} and Λ₆ ≤ 93^{1/6}**, via B* = {1,4,5,17,21,22} with g₅(n) ≤ w_s·97^j and g₆(n) ≤ w_s·93^j. **Verified (finite).** My checks (`ep817_continuation_checks_OUTPUT.txt`):

- H(B*) is the listed 38-element set.
- It is modular-5-AP-free mod 97 and modular-6-AP-free mod 93, and the chain histograms match the table exactly.
- The two-level languages (1,444 values) are integer-AP-free.
- The generator ordering gives exactly w_s·q^j.
- The smaller blocks (19,{1,7,8},4), (23,{1,3,4,7},5) and (47,{1,2,6,7,14},6) also pass.
- The comparisons 97 < 5³, 93⁵ < 7¹² and 97² < 23³ hold.
- The comparison with Korsky's v1 rates √5 and 7^{2/5} depends on the preprint, which I did not read. The integer inequalities themselves are correct.

**§6.4 example.** **Verified (finite).** For B = {2,7}, q = 11, k = 3, the reachable set is exactly the three states listed, with 14 edges. Acceptance is unreachable although modular 3-APs exist, so the modular test is sufficient but not necessary.

**§8.2 nearby bases.** **Verified (finite).** Every q in 71..96 fails at k = 5 and every q in 71..92 fails at k = 6 (full carry graph). The two displayed witness rows are genuine APs in the two-level language.

**§8.1 and §9** (vector model; column-mass bound m ≤ ⌊r(τ+1)/2⌋). **Verified** (short and elementary).

### 3.3 EP-05: g₆(n) ≤ 257·1651^{⌈n/10⌉−1}

`research/graphical_obstructions/notes/graphical-obstructions.md`. Status in the note: "independent mathematical review pending" (L3).

**The certificate (1.2)–(1.4).** **Verified (finite).**

- A♯ = {3,4,7,34,37,41,216,250,253,257} is the set of pairwise distances of (0,4,7,41,257). S = 1102 < 1651 = 13·127.
- |H(A♯)| = 291, with fibre-size histogram 120, 60, 60, 30, 20, 1 (sizes 1, 2, 4, 8, 14, 24), as stated.
- No nonzero-step 6-AP mod 1651 (all steps, composite modulus included).
- The two-level language (84,681 values) is integer 6-AP-free.
- The generator bookkeeping gives a_s·1651^j ≤ 257·1651^{⌈n/10⌉−1}.
- 1651³ = 4,500,297,451 < 93⁵ = 6,956,883,693.
- The lift is the EP-04 Lemma 5.1, so the bound on g₆(n), and hence Λ₆ ≤ 1651^{1/10} ≈ 2.0979, follows.

**Theorem 3.1 and the K_m corollary.** **Verified.** r disjoint signed lifts of one boundary force an (r+1)-AP. Hence every distinct-distance K_m ruler has an m-term AP; for A♯, 0, 257, 514, 771, 1028 is checked.

**Fixed-block optimality (9.3): γ₆(A♯) = 1651^{1/10} over canonical schedules.** **Verified (finite).**

- Return sections r(c) exist for all 81 carries c ∈ {−1,0,1}⁴.
- For every radix q = 1103..1650 (all 548), I found an explicit nonconstant integer 6-AP in D + qD.
- The scope stated in the note is correct: radices ≤ S(A♯), other blocks and the global λ₆ are excluded (L469).

**§7 hyperplane family** (0, a, b, c = 5b − 3a, z) with z > 2c: always a 6-AP of step c − b. **Verified**, algebraically and on 2,730 parameter choices. So the old ruler (0,1,5,22) cannot be extended.

**§8 tail classification** for the prefix (0,4,7,41) and z = 42..356. **Verified (finite).**

- The note's classification reproduces exactly: 270 values with a 6-AP, 6 with repeated weights, 39 free; z = 257 is free.
- The affine-packet argument for z > 356 was read. My spot checks at z = 357, 400, 1000 and 2500 are free.

**Theorems 5.2/5.3 (collision rigidity via tournament scores).** **Read, plausible;** I checked m ≤ 5 exhaustively.

- |Σ_m| = 2, 7, 38, 291, 2932 for m = 2..6.
- For m = 2..5, the packet of Theorem 5.2 exists for all 2 + 18 + 200 + 3080 nonzero score differences, for every argmax/argmin choice.
- The flow/cut proof of Lemma 5.1 is the classical Landau-type criterion; the note cites Kolesnik–Sanchez and does not claim it as new. The four-case cut bound (5.4) was followed but not re-derived in every case.

**(6.1)–(6.4)** (the leading law within the complete-graph family). **Read, plausible.** The lower bound follows from Theorem 5.3. The upper construction T = (0,1,p,…,p^{m−2}), q = p^{m−1}, is standard base-p digit reasoning. The note itself says it is "not a lower bound for the unrestricted" λ (L337).

### 3.4 EP-08: finite-period approximation

`research/finite_period/notes/finite-period-control.md`, 16 Sep. Status: ordinary proofs; no new Lean.

**Setting.** A "level" is (b, A) with S(A) < b. The q-ary image is H_q(A) = {Σ c_a a : 0 ≤ c_a < q}. δ_q(D) is the best lower-limit growth rate per generator over infinite words in a finite dictionary D. This is an **image-count** rate, not the max-generator cost, as the note says at L43.

**Cut bound (2.2).** **Verified.** Under concatenation, fibres of (x, y) ↦ x + Q(u)y have at most C = q − 1 points, because x ∈ [0, (q−1)(Q−1)] and the points in a fibre are congruent mod Q. The constant C is sharp for {1} at radix 2 (checked by hand).

**FP1** (L118–151): 0 ≤ log U_m − log δ_q(D) ≤ log(q−1)/(m·n_min). **Verified.** It needs only block splitting, supermultiplicativity of F/C, and Fekete for periodic words.

**§3.1** (periodic approximation, δ = inf_w η(w)^{1/N(w)}) and **FP2** (controllers with closing-path cost (s−1)·log T). **Verified** (short arguments).

**§5** (pressure enclosure). **Read, plausible.**

**FP3** (radix-ten dictionary A = (10,{1,3}), B = (10,{2,4}), q = 5): a₁ = 13, a_{3r} = 893^r, a_{3r+1} = 93²·893^{r−1}, a_{3r+2} = 93·893^r. **Verified (finite for m ≤ 16) and proof read.** My checks:

- I built an independent 7-state carry automaton. Its states are the nonempty sets of possible carries; carries are at most 2. It matches direct enumeration of H₅(A_w) for all words of length ≤ 5.
- The exhaustive minimum over all 2^m words equals the formula for every m ≤ 16. The generating function (1 + 13z + 93z² − 2960z⁴)/(1 − 893z³) matches.
- The attainers are confirmed: BA → 93, BAA → 893, BABA → 93², and (AAB)^r → 2301·893^{r−1}.
- The lower-bound mechanism for all m reproduces in my basis. The letter product M_B·M_A has rank 1, and the spectral radius of every cyclic A^aB^b (a, b ≤ 4) equals θ(a,b) = (8·10^{a+b} + 4·10^b − 3)/9 and is ≤ the count.
- The partition step holds: t_L − 93·t_{L−2} > 0 for L ≥ 4, and 93³ > 893².

The note states the rate 893^{1/6} ≈ 3.103 is not a new record (L440), and I agree: it is far above 97^{1/6}.

---

## 4. The remaining continuation notes (lighter reading)

All of these are labelled ordinary proofs plus finite certificates, submitted for independent review, with no new Lean. Verdicts here are **Statement only** unless stated otherwise.

- **EP-06, outer control** (`research/splitzero_outer`).
  - Claim: for each fixed k and per-level block size n, the optimum over all blocks and all canonical mixed-radix schedules is attained and computable.
  - The table gives fixed-block optima for n ≤ 5. For k = 5 and k = 6 alike: 8^{1/2}, 5^{1/2}, 13^{1/3}, 23^{1/4}. At n = 5: 65^{1/5} (k = 5) and 47^{1/5} (k = 6).
  - The certificate side for (23,{1,3,4,7}) and (47,{1,2,6,7,14}) is verified in §3.2. **Optimality is not checked**; it rests on the 47,259-block audit.
  - The README says the unrestricted infimum over block sizes is not evaluated.
- **EP-07, cone dual** (`research/cone_dual`).
  - C1: the feasible cone of the seven image observations has 9 facets and 10 extremal rays.
  - C2: integral lifts.
  - C3: finite rational certificates below the global rate.
  - C4: switching growth √285 per level for ({3,13},23) and ({1,4},23).
  - C5: the observation does not decide admissibility. **C5 verified (finite)**: (31,{1,3,4,7}) is modular-5-free, while {1,2,4,8} has H = [0,15], which contains 0..4. C1–C4 are not checked.
- **EP-09, several notes** (NOTE_INDEX L9–37).
  - **Recurrence control:**
    - R1: the gap condition a_j > S_{j−1} + S_{j−r} excludes (2^r+1)-APs. **Verified** (pigeonhole on 2^r intervals of width S_{h−r} against a crossing gap > S_{h−r}).
    - R2: the minimal sequence p_j = 2p_{j−1} + p_{j−r} gives longest AP exactly min(2^r, 2^n), with rate the root ρ_r > 2 of ρ^r − 2ρ^{r−1} − 1 = 0. **Verified (finite)** for r = 1, 2, 3 and n ≤ 10.
    - For r = 2 these are the Pell numbers 1, 2, 5, 12, 29, …, whose subset sums have no 5-AP.
    - R3–R5, R5u and the seven-term motif R6 are not checked.
  - **Canonical isolation CI1–CI4** (complete-graph score sources and canonical arithmetic factors). **Statement only.**
  - **Arity boundary, supported defects, defect closure, variable blocks and local flow.** **Statement only** (titles and READMEs).
  - **All-block image, Theorem A.**
    - Claim: for every k ≥ 3 and every q ≥ 5, λ_k = inf over k-admissible A of |H_q(A)|^{1/|A|}. In particular λ_k = inf |H₅(A)|^{1/|A|}.
    - The inequality inf ≤ λ_k is immediate from |H₅(A)| ≤ 4S(A)+1.
    - The reverse direction (prime selection plus amplification) is **not checked**. EP-08 and the seven-observable Theorem 4 use this bridge to interpret image rates as upper constructions.
    - Theorems B (a two-state ternary transfer) and C (collision horizon) are **Statement only**.
  - **Seven-observable Theorems 1–4.** **Statement only**, except the corrected step below.
- **The published correction** (`PUBLICATION_NOTES.md` L7; `seven-observable-capacity.md` §4.1, around L213–218). **The correction is right.**
  - The independence test uses Y_P = P ∪ (L − P) with P ⊆ [0, Q]. The gap between the two components is at least L − 2Q.
  - No pattern of width ≤ Q may cross the gap, which needs L − 2Q > Q, i.e. L > 3Q.
  - The older L > 2Q only gives a positive gap and would not suffice.
  - The reader edition uses the current L > 3Q text (NOTE_INDEX L5; PUBLICATION_NOTES L7).

---

## 5. Negative results, with their exact scope

**Proved obstructions** (verified or verified-finite as marked above):

1. **Hypothesis needed** (paper L521–524). The "19 classes per 3-block" statement needs the ambient 4-AP-free hypothesis. My controls show the count bound fails without it.
2. **Admissible classes are strictly nested.** The inclusion {4-admissible} ⊂ {k-admissible} is strict: {1,2} is 5-admissible but not 4-admissible (general-k §2).
3. **Modular certificates are sufficient, not necessary** (general-k §6.4). Example: B = {2,7}, q = 11, k = 3. This concerns the certificate test, not the rate identity, which holds for both classes (§7).
4. **Bases below 97 and 93 fail for B*.** Every base 71..96 fails at k = 5 and every base 71..92 at k = 6 (general-k §8.2). This is a statement about this block only.
5. **Rectangular-digit route** (general-k §9). m ≤ ⌊r(τ+1)/2⌋ bounds only that representation class.
6. **Distance rulers** (graphical §3). Every distinct-distance K_m ruler has an m-term AP. Also, |E| ≤ (k−2)(|V| − c(G)) for k-admissible distance graphs, but only for graphical sources (L126).
7. **The (0,1,5,22) ruler cannot be extended** (graphical §7). No appended mark with distinct distances gives a 6-admissible K₅ ruler; the whole family c = 5b − 3a fails.
8. **Fixed-block optimum for A♯** (graphical §9). No canonical schedule with a radix in [1103,1650] is admissible. Radices ≤ S and other blocks are out of scope.
9. **Leading law only within the complete-graph family** (graphical §6). The coefficient 2 in m·log Ξ_m/log m cannot be improved inside that family. The note says this is not a lower bound for the unrestricted λ_{m+1}.
10. **Image counts do not determine admissibility** (cone dual C5). The seven-coordinate count matrix plus reward does not determine binary admissibility.
11. **Infimum not attained** (all-block image §8, not checked). The capacity infimum is not attained at k = 3.
12. **Longer-delay recurrences** (recurrence R6, not checked). A six-generator motif gives a seven-term AP, which rules out proposed longer-delay recurrences for k = 5..7.

**"Does not decide" and "not proved" statements, as the workbench makes them:**

- **k = 4 scope.** The theorem does not address all of Problem 817 or every finite value (STATUS L29–32; README L53–54). It makes no novelty or priority claim (README L139–141; STATUS L27; corpus NONCLAIM-001).
- **k = 3.** It is separate and attributed to Costa.
- **Unrestricted Λ_k.** It is open for every k ≥ 5, both its value and any all-rank lower certificate (general-k L71 and §10; `splitzero_outer` README L19; finite-period §8; cone-dual README L5, L26).
- **Large-k target.** The uniform bound log q/|B| ≥ c·log k/k over all certificates is a "research target", not a premise (general-k L527–534).
- **EP-08 limits.** No claim that an optimum is attained by a finite period, no cutoff on block rank, and zero-reward edges are excluded (finite-period L5, L170, L240, L438).
- **Lean.** No new Lean for any continuation; the k = 4 lower bound is not in Lean (§2.3).

---

## 6. Overlaps

**EP-10: the SplitZero receiving maps** (`interfaces/zeta/workbenches/ep817-*`). There are 11 folders and 10 interface notes. Nine are chapters 10, 13, 15, 17, 19, 21, 25, 27 and 29 of the collection. Each folder also mirrors the arithmetic notes.

What the receiving maps are. From the finite-period example (L12–125):

- free ℚ-vector spaces on finite sets (coefficient words Ω_u; distinct values X_u);
- the evaluation quotient q_u, and the cut map π_{u,v}: e_{(x,y)} ↦ e_{x+Q(u)y};
- an exact sequence of kernels (R2), and dim ker π = F(u)F(v) − F(uv) (R3);
- a "cocycle" identity κ(u,v)κ(uv,w) = κ(v,w)κ(u,vw) (R4). It is immediate: both sides equal F(u)F(v)F(w)/F(uvw);
- least-norm weighted sections and a Gram matrix diag(1/μ).

These are typed linear-algebra restatements of the 817 finite constructions in the zeta programme's supported-quotient vocabulary. They are correct as restatements and elementary.

**Direction of flow.**

- Nothing flows back into the 817 proofs: none of the 817 theorems audited above uses a zeta result.
- Nothing is claimed about zeta. PUBLICATION_NOTES L27 disclaims any new zeta-function result, and several receiving notes say they prove no Riemann-hypothesis conclusion or zeta-zero statement.
- Per the survey (OV-18), the zeta side receives these as typed maps and enters no zeta statement. I did not re-read the zeta repository.

**Erdős–Straus and other workbenches.**

- There is no mathematical link. README L54 says the work is not an Erdős–Straus artifact.
- The only cross-references are methodological: PolyClank research-record conventions (general-k L947–948; survey OV-23) and a validator design (OV-22).
- An `integration/.../AUDIT.md` command line contains a private-style Windows path whose folder name mentions Erdős–Straus (survey D9). That is a hygiene matter, not mathematics.

---

## 7. Not checked

- Lean builds and the 44 axiom reports (no toolchain). The workbench's own verifiers (`certificates/*.py`, `research/*/certificates/*`) were not run; I wrote independent checks instead.
- The release ZIP, the PDFs, the corrected collection LaTeX, and the Chapter 3 "general-k v2" note (951 lines).
- The EP-06 optimality claims (the 47,259-block audit) and the EP-07 cone (C1–C4).
- In EP-09: recurrence R3–R6, canonical isolation, arity boundary, supported defects, defect closure, variable blocks, and local flow.
- All-block image Theorem A (the reverse direction), B and C, and seven-observable Theorems 1–4 (beyond the L > 3Q step).
- Graphical Theorem 5.2: every case of the cut inequality for general m; I checked m ≤ 5 by computer.
- The literature: Korsky's v1 values, Costa's theorem, and the novelty of any statement. There was no web access, and OEIS was not consulted for g₄.
- The exact value of g₄(7) (only 176 ≤ g₄(7) ≤ 246) and of g₄(n) for n ≥ 8.

---

## 8. Results that stand without the workbench's vocabulary (reader candidates)

1. **Main theorem.** (19^{n/3} − 1)/(2n) ≤ g₄(n) ≤ 8·19^{⌈n/3⌉−1} for all n ≥ 1, so g₄(n)^{1/n} → 19^{1/3} ≈ 2.668. Proof by the anonymous Reddit contributor; verified. The upper half is Lean-checked (sneed-and-feed).
2. **The construction.** The 3m numbers 19^j·1, 19^j·7, 19^j·8 (j < m) have subset sums with no nonconstant 4-term AP.
3. **Digit fact.** The seven residues {0,1,7,8,9,15,16} mod 19 contain no nonconstant 4-term AP.
4. **Relation splitting.** If H(A) has no 4-AP and Σ cᵢaᵢ = 0 with cᵢ ∈ {−2,…,2}, then the ±1 part and the ±2 part of the relation vanish separately.
5. **Exact ternary count.** If H(A) has no 4-AP, the number of distinct sums Σ xᵢaᵢ (xᵢ ∈ {0,1,2}) is 3^t ∏(3^{m_j} − 2^{m_j}), where m_j are the sizes of the disjoint minimal ±1-relations.
6. **Sharper finite lower bound** (The Clankers). g₄(n) ≥ ⌈(19^{n/3} + n(n−1) − 1)/(2n)⌉.
7. **Variance lower bound** (EP-03). g₄(n) ≥ ⌈√(19(M_n² − 1)/(192n))⌉ with M_n = 19^{⌊n/3⌋}·3^{n mod 3}, about 0.315·19^{n/3}/√n.
8. **The limit exists for every k** (EP-04). For every k ≥ 3, Λ_k = lim g_k(n)^{1/n} exists, because g_k is essentially submultiplicative via A ∪ (2ΣA + 1)·B.
9. **Λ_k from finite certificates** (EP-04). Λ_k is the infimum of q^{1/|B|} over finite B with ΣB < q whose subset sums, taken mod q, contain no k-term progression with nonzero step.
10. **A decision procedure** (EP-04). Whether base-q numbers with digits from a given finite set avoid k-term APs at every length is decidable by a finite carry graph.
11. **Better k = 5, 6 rates** (EP-04). Λ₅ ≤ 97^{1/6} ≈ 2.1435 and Λ₆ ≤ 93^{1/6} ≈ 2.1277, from the block {1,4,5,17,21,22}. Certificates verified.
12. **Better k = 6 rate** (EP-05, review pending in the workbench). g₆(n) ≤ 257·1651^{⌈n/10⌉−1}, so Λ₆ ≤ 1651^{1/10} ≈ 2.0979, from the block {3,4,7,34,37,41,216,250,253,257}. Certificate verified.
13. **Distance rulers** (EP-05). The subset sums of the ten pairwise distances of any 5 distinct integers, when those distances are distinct, contain a 5-term AP. In general, m marks give an m-term AP.
14. **Gap sequences** (EP-09 R1). If a_j > S_{j−1} + S_{j−r} for all j, the subset sums contain no (2^r + 1)-term AP. For r = 2 this covers the Pell numbers 1, 2, 5, 12, 29, ….
15. **Exact small values** (this audit, not in the workbench, no literature search). g₄(1..6) = 1, 3, 5, 14, 40, 79, and 176 ≤ g₄(7) ≤ 246.
