# The Erdős Problem 817 workbench: the rate 19^{1/3} for four-term progressions, the general-k capacity, certificates for k = 5, 6, and exact small values

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 26 September 2026, 05:37 UTC; revised 06:39 UTC after the twentieth referee pass (§10).

Third note of board task 10, part 2. Subject: `KokunoYumeto/erdos-problem-817-workbench` at commit `dbd0a93f2cf935103e88e5c2b2b71fe85ae7537b` (16 September 2026).

**How this note was made.** A first-pass audit by a Claude subagent (report reproduced as `45a_ERDOS_817_FIRST_PASS_AUDIT_REPORT.md`, "45a"; scripts in `checks/workbenches/audit45_ep817/`), whose Python scripts I re-ran on 26 September with identical results (`rerun_20260926/ep817/`; 45a's C searches were not re-run by me, and my own C search below replaces them for n ≤ 6); an independent check of my own (`workbench_reader_claims_checks.py`, section EP) and a third, independent exhaustive search for the small values (`checks/workbenches/g4_bitset.c`, output `g4_bitset_OUTPUT.txt`); my own re-derivation of the proofs below. Status labels as in `43_`.

**Attribution, as the workbench records it.** The k = 4 proof is due to an anonymous contributor on the subreddit r/LLMmathematics, whose account was later deleted; the reconstruction, exposition and checks are by "The Clankers", who also formalised the central algebraic and base-19 components in Lean (`Core.lean`); the Lean formalisation of the finite upper bound is by sneed-and-feed (pull request #1, `Extended.lean`). The workbench makes no novelty or priority claim for the k = 4 theorem and says the work concerns the k = 4 exponential-rate subproblem, not every part of Problem 817 (README; 45a §2; `47a` §6); for its k = 5, 6 bounds it says they improve on Korsky's v1 rates (general-k note).

## 0. The problem

For a finite set A of distinct positive integers let H(A) = {Σ_{a∈A} ε_a a : ε_a ∈ {0, 1}} (the empty sum included), S(A) = Σ_{a∈A} a. A is *k-admissible* if H(A) contains no k-term arithmetic progression x, x + d, …, x + (k − 1)d with d ≠ 0. g_k(n) is the least N such that some n-element A ⊆ {1, …, N} is k-admissible. Erdős Problem 817 (a problem of Erdős and Sárközy; listed as open on erdosproblems.com/817 when read on 26 September 2026) asks for estimates of g_k(n), in particular whether g₃(n) ≫ 3^n; Erdős and Sárközy proved g₃(n) ≫ 3^n/n^{O(1)} (Discrete Math. 102 (1992) 249–264). The workbench reports that Costa's preprint (arXiv:2609.06303) proves lim inf g₃(n)/3^n = 0, a negative answer to that question; this note did not check the preprint, and the workbench's own results concern k ≥ 4.

Admissibility is hereditary (H(B) ⊆ H(A) for B ⊆ A), so g_k is strictly increasing in n (delete the maximum).

## 1. The main theorem (EP-01)

**Theorem 45.1.** For every n ≥ 1, (19^{n/3} − 1)/(2n) ≤ g₄(n) ≤ 8·19^{⌈n/3⌉−1}. Hence lim g₄(n)^{1/n} = 19^{1/3} ≈ 2.6684.

Status: **audited**; the written proof (paper `ep817_k4_rate.tex`) is complete and correct as written (45a §2, every lemma re-derived; my re-derivation below). The workbench reports the upper half as Lean-checked (`Extended.lean`, `erdos_problem_817_upper_bound`; the Lean files were read but not built for this note); the lower half is not in Lean.

Let A = {a₁, …, a_n} be 4-admissible. A *relation* is c ∈ {−2, …, 2}^n, c ≠ 0, with Σc_ia_i = 0; a ±1-relation has c ∈ {−1, 0, 1}^n.

**Lemma 45.2 (relation splitting).** If c is a relation, its ±1 part and its ±2 part are each relations or zero: with P_j = Σ_{c_i=j}a_i and N_j = Σ_{c_i=−j}a_i, one has P₁ = N₁ and P₂ = N₂.

*Proof.* X₀ = P₁ + N₂, X₁ = P₁ + P₂, X₂ = N₁ + N₂, X₃ = N₁ + P₂ are subset sums (the four index classes are disjoint). With d = P₂ − N₂, the relation P₁ + 2P₂ = N₁ + 2N₂ gives N₁ − P₁ = 2d, and then X₁ − X₀ = X₂ − X₁ = X₃ − X₂ = d. Admissibility forces d = 0, and then P₁ = N₁. ∎

**Lemma 45.3 (blocks).** Call a ±1-relation *minimal* if its support is inclusion-minimal. Two minimal relations r, s have disjoint supports or s = ±r. Every ±1-relation is uniquely a sum of minimal relations with disjoint supports, and every relation is Σ_j t_jr^{(j)} with t_j ∈ {−2, …, 2} over the minimal blocks r^{(j)}. Each block has at least 3 elements.

*Proof.* r + s and r − s are relations with values in {−2, …, 2}; their ±2 layers are r·1_{E₊} and r·1_{E₋}, where E_± = {i : r_i = ±s_i ≠ 0}. By Lemma 45.2 these are relations or zero. If the supports meet, one of E_± is nonempty, and minimality of r gives E_± = supp r; so supp r ⊆ supp s and s = ±r there, and minimality of s gives equality. Existence of the decomposition: peel off a minimal sub-relation (the remainder vanishes on it and has smaller support); uniqueness is coordinatewise. For a general relation, the ±1 part u and half the ±2 part v are ±1-relations with disjoint supports (Lemma 45.2), each a sum of whole blocks; so c = u + 2v = Σ(α_j + 2β_j)r^{(j)} with α_jβ_j = 0. A block of size 1 would be a zero element and one of size 2 two equal elements. ∎

**Lemma 45.4 (the ternary count).** Let T(A) = {Σx_ia_i : x ∈ {0, 1, 2}^n}, let the blocks have sizes m₁, …, m_h and let t = n − Σm_j be the number of coordinates in no block. Then |T(A)| = 3^t∏_j(3^{m_j} − 2^{m_j}).

*Proof.* Φ(x) = Φ(y) iff x − y is a relation, iff x − y = Σt_jr^{(j)} (Lemma 45.3), so the fibres of Φ are products over the blocks and the free coordinates are fixed. On a block, the reflection x_i ↦ 2 − x_i at the coordinates where r_i = −1 turns the equivalence into translation by (1, …, 1). Each translation class in {0, 1, 2}^m has exactly one representative with minimum 0, and those number 3^m − 2^m. ∎

*Proof of Theorem 45.1.*
- *Lower bound.* f_m = 3^m − 2^m satisfies f₃ = 19 and f_{m+1} = 3f_m + 2^m > 3f_m ≥ 19^{1/3}f_m, so f_m ≥ 19^{m/3} for m ≥ 3, and 3 ≥ 19^{1/3}. By Lemma 45.4, |T(A)| ≥ 19^{n/3}. Since T(A) ⊆ [0, 2S(A)] ⊆ [0, 2nN], 19^{n/3} ≤ 2nN + 1.
- *Upper bound.* D = H({1, 7, 8}) = {0, 1, 7, 8, 9, 15, 16} contains no nonconstant 4-term progression modulo 19 (checked over all 19·18 progressions). For A_m = {19^jw : j < m, w ∈ {1, 7, 8}}, H(A_m) is the set of numbers whose base-19 digits all lie in D (no carries, since 16 < 19). If x, x + d, x + 2d, x + 3d lie in H(A_m) with d = 19^re, 19 ∤ e, then r < m (all terms are below 19^m), the lowest r digits agree, and the r-th digits δ₀, …, δ₃ ∈ D satisfy δ_i ≡ δ₀ + ie (mod 19): a nonconstant progression in D modulo 19, which is impossible. So A_m is 4-admissible with 3m elements and maximum 8·19^{m−1}; for general n take m = ⌈n/3⌉ and delete elements.
- *Rate.* The n-th roots of both bounds tend to 19^{1/3}. ∎

**Corollary 45.5 (The Clankers).** Since distinct elements give S(A) ≤ nN − n(n − 1)/2, g₄(n) ≥ ⌈(19^{n/3} + n(n − 1) − 1)/(2n)⌉. (Audited.)

## 2. The variance refinement (EP-03)

**Theorem 45.6.** Write n = 3q + r (0 ≤ r ≤ 2) and M_n = 19^q3^r. Every 4-admissible A has |T(A)| ≥ M_n and 19(|T(A)|² − 1) ≤ 192·Σa_i². Hence g₄(n) ≥ ⌈√(19(M_n² − 1)/(192n))⌉, about c_r·19^{n/3}/√n with c_r = 0.315, 0.354, 0.398 for n ≡ 0, 1, 2 (mod 3).

Status: **audited**; the workbench labels it "Not Lean-checked". It depends on the anonymous contributor's short-kernel lemma and ternary count (Lemmas 45.3 and 45.4).

*Proof (my derivation of the variance, which agrees with the note's).*
1. *|T| ≥ M_n.* f₃ = 19 ≥ 19, f₄ = 65 ≥ 57, f₅ = 211 ≥ 171 and f_{m+3} − 19f_m = 8·3^m + 11·2^m > 0, so f_m ≥ 19^{⌊m/3⌋}3^{m mod 3}. The product 3^t∏f_{m_j} is then at least 19^a3^b with 3a + b = n, and since 3³ > 19 the least such value is 19^q3^r.
2. *Product structure.* By Lemma 45.4 the uniform law on T(A) is the law of a sum of independent components: each free coordinate i contributes uniformly from {0, a_i, 2a_i} (variance (2/3)a_i²), and each block B contributes uniformly from its class values.
3. *Block variance.* After the reflection of Lemma 45.4, a block with coefficient vector b (b_i = ±a_i, Σb_i = 0) has class values ⟨b, y⟩ over y ∈ R = {y ∈ {0,1,2}^m : min y = 0}. The map y ↦ 2 − y permutes classes and negates values (Σb_i = 0), so the mean is 0. Since {0,1,2}^m = R ⊔ (1 + {0,1}^m) and values are translation invariant,
   Σ_{y∈R}⟨b, y⟩² = 3^m·E(Σb_iY_i)² − 2^m·E(Σb_iZ_i)² = 3^m(2/3)Q − 2^m(Q/4),
   with Y_i uniform on {0, 1, 2}, Z_i uniform on {0, 1} and Q = Σb_i² = Σ_{i∈B}a_i². Dividing by |R| = 3^m − 2^m gives the variance κ_mQ with κ_m = (8·3^m − 3·2^m)/(12(3^m − 2^m)).
4. *The constant.* 16/19 − κ_m = 5(8·3^m − 27·2^m)/(228(3^m − 2^m)) ≥ 0 exactly when (3/2)^m ≥ 27/8, i.e. m ≥ 3, with κ₃ = 16/19; and 2/3 < 16/19. So the variance of the uniform law on T(A) is at most (16/19)Σa_i² ≤ (16/19)nN².
5. *Packing.* M distinct integers have uniform variance at least (M² − 1)/12. Combining, (M_n² − 1)/12 ≤ (16/19)nN². ∎

(My check: mean 0 and variance κ_mQ on 60 random blocks; κ_m ≤ 16/19 for 3 ≤ m ≤ 40. The note's table of the refined bound, which uses Σa_i² ≤ Σ_{j<n}(N − j)² for distinct elements, is 1, 3, 5, 11, 27, 49 for n ≤ 6 and was recomputed by 45a.)

## 3. General k (EP-04, EP-05)

**Theorem 45.7 (EP-04, Theorem 1).** For every k ≥ 3, Λ_k = lim g_k(n)^{1/n} exists, and Λ_k = inf q^{1/|B|} over pairs (q, B) with S(B) < q and H(B) modulo q free of k-term progressions with nonzero step (composite q allowed).

*Proof.*
- *Composition.* If A and B are k-admissible and R = 2S(A) + 1, then C = A ∪ R·B is k-admissible and 2S(C) + 1 = (2S(A) + 1)(2S(B) + 1): H(C) = H(A) + R·H(B) bijectively, and a progression x_i = α_i + Rβ_i in H(C) has second differences Δ²α + RΔ²β = 0 with |Δ²α| ≤ 2S(A) < R, so α and β are progressions and one of them is nonconstant.
- *Limit.* F_k(n) = min(2S(A) + 1) over k-admissible n-sets is submultiplicative, so lim F_k(n)^{1/n} = inf F_k(n)^{1/n} (Fekete); and 2g_k(n) + 1 ≤ F_k(n) ≤ 2n·g_k(n) + 1.
- *Certificates.* Lifting: if (q, B) is a certificate, the sets {q^jb : b ∈ B, j < m} are k-admissible (the argument of the upper bound in Theorem 45.1, with q in place of 19; q ∤ e suffices, so q need not be prime); so Λ_k ≤ q^{1/|B|}. Conversely every k-admissible B gives the certificate (2S(B) + 1, B): elements of [0, S(B)] whose consecutive differences agree modulo 2S(B) + 1 have equal integer differences. So the infimum over certificates is at most inf_n F_k(n)^{1/n} = Λ_k. ∎

Status: **audited**. The note also proves Λ_k ≥ (k − 1)/(k − 2), Λ_{k+1} ≤ Λ_k, and (Theorem 2) that whether base-q numbers with digits from a given finite set avoid k-term progressions at every length is decided by a finite carry graph with at most 2·k! states (digits in [0, q − 1]); all audited in 45a §3.2.

**Theorem 45.8 (certificates).**
- (EP-04, Theorem 3) B* = {1, 4, 5, 17, 21, 22} has S(B*) = 70 and |H(B*)| = 38; H(B*) is free of nonzero-step 5-term progressions modulo 97 and of 6-term progressions modulo 93. Hence Λ₅ ≤ 97^{1/6} ≈ 2.1435 and Λ₆ ≤ 93^{1/6} ≈ 2.1285.
- (EP-05) A♯ = {3, 4, 7, 34, 37, 41, 216, 250, 253, 257}, the ten pairwise distances of the marks 0, 4, 7, 41, 257, has S(A♯) = 1102 < 1651 = 13·127, |H(A♯)| = 291, and H(A♯) is free of nonzero-step 6-term progressions modulo 1651. Hence g₆(n) ≤ 257·1651^{⌈n/10⌉−1} and Λ₆ ≤ 1651^{1/10} ≈ 2.0979. The workbench labels EP-05 "independent mathematical review pending".

Status: **audited (certificate)**; each modular condition was checked by 45a and again by my script (which also finds a 5-term progression of H(B*) modulo 96).

**Proposition 45.9 (distance rulers; EP-05 Theorem 3.1 and its corollary).** If the C(m, 2) pairwise distances of m marks 0 = t₀ < … < t_{m−1} = L are distinct, their subset sums contain the m-term progression 0, L, 2L, …, (m − 1)L.

*Proof.* The m − 1 sets {L} and {t_i, L − t_i} (1 ≤ i ≤ m − 2) of distances are pairwise disjoint (distinct pairs have distinct distances) and each sums to L. ∎ For A♯ this gives 0, 257, 514, 771, 1028 (checked), so A♯ is 6-admissible but not 5-admissible.

**Comparison with the literature (as far as read).** Korsky's preprint (arXiv:2606.24139, v1, June 2026; read in its arXiv HTML rendering for this note, Theorems 1.2–1.3 and (1.8)) proves, for fixed k ≥ 4, g_k(n) ≫_k ((k − 1)/(k − 2))^n n^{−log₂((k−1)/(k−2))}, and g_k(n) < 2p^{ρ_{p,k}(n)−1} for primes p ≥ 3, with q_{p,k} = min{p, k} − 1 and ρ_{p,k}(n) = max{q_{p,k} − 1, ⌈2n/q_{p,k}⌉}. The resulting upper exponential rate min_p p^{2/(min{p,k}−1)} is 5^{2/3} ≈ 2.924 for k = 4, √5 ≈ 2.236 for k = 5 and 7^{2/5} ≈ 2.178 for k = 6 (my arithmetic). Against these, Theorem 45.1 determines the k = 4 rate (19^{1/3} ≈ 2.668, between Korsky's lower rate 3/2 and upper rate 5^{2/3}), and Theorem 45.8 lowers the upper rates for k = 5 and 6. No wider literature search was made. The workbench disclaims priority for the k = 4 theorem and presents the k = 5, 6 bounds as improvements on Korsky's v1 rates.

## 4. Exact small values (computed for this audit)

**Proposition 45.10.** g₄(1), …, g₄(6) = 1, 3, 5, 14, 40, 79, and 176 ≤ g₄(7) ≤ 246.
- The values for n ≤ 6 were found by three independent exhaustive searches: two by 45a (an increasing branch-and-bound, and a decreasing search run with and without the lemma-based pruning) and a third by me (increasing, bitset subset sums, heredity pruning only, no lemma of the paper used). All agree, including the numbers of optimal sets (1, 2, 2, 2, 7, 1). The unique optimal 6-set is {2, 29, 45, 74, 77, 79}; it consists of two 3-blocks (29 + 45 = 74 and 2 + 77 = 79) and has |T| = 361 = M₆, the least value Theorem 45.6 allows.
- g₄(7) ≤ 246 by the explicit admissible set {1, 3, 39, 180, 219, 243, 246}. The lower bound 176 is **conditional** on 45a's search program, which excluded maxima in [132, 175] using pruning derived from the proved Lemmas 45.4 and Theorem 45.6 (and N < 132 by Theorem 45.6's refined bound).

These values are not in the workbench. The sources read for this note (erdosproblems.com/817; Korsky's HTML text; the public repository `firesh/erdos817-subset-sum-progressions-audit`, which records g₃(1..6) = 1, 3, 8, 22, 60, 168) do not list them; OEIS could not be consulted (its search is disallowed to the fetch tool). No claim of novelty is made.

## 5. The finite-period and other continuation notes

- **EP-08 (audited in part).** For a finite dictionary D of levels (radix b, block A with S(A) < b) and the q-ary image H_q(A) = {Σc_aa : 0 ≤ c_a < q}, the best lower-limit image growth δ_q(D) satisfies 0 ≤ log U_m − log δ_q(D) ≤ log(q − 1)/(m·n_min) (FP1). This is an image-count rate, not the maximum-generator cost. The radix-ten example (A = (10, {1, 3}), B = (10, {2, 4}), q = 5) has minima a₁ = 13, a_{3r} = 893^r, a_{3r+1} = 93²·893^{r−1}, a_{3r+2} = 93·893^r (verified for m ≤ 16 by an independently built 7-state automaton); the note says the rate 893^{1/6} ≈ 3.103 is not a record.
- **The published correction (audited).** In the seven-observable note the independence test Y_P = P ∪ (L − P) with P ⊆ [0, Q] needs L > 3Q (so that no pattern of width ≤ Q crosses the gap L − 2Q), not the older L > 2Q; the reader edition carries L > 3Q.
- **EP-09 recurrence control R1 (audited), R2 (verified for r ≤ 3, n ≤ 10).** If a_j > S_{j−1} + S_{j−r} for all j, the subset sums contain no (2^r + 1)-term progression; for r = 2 this covers the Pell numbers 1, 2, 5, 12, 29, ….
- EP-06 (outer control), EP-07 (cone dual; only C5 verified: image counts do not decide admissibility), the rest of EP-09, and the all-block image Theorem A (reverse direction) are **located**.

## 6. Negative results, with exact scope

1. The "19 classes per 3-block" count needs the ambient admissibility hypothesis: {1, 2, 3} has |T| = 13 < 19.
2. Admissible classes are strictly nested: {1, 2} is 5-admissible but not 4-admissible.
3. Modular certificates are sufficient, not necessary, for all-length admissibility (B = {2, 7}, q = 11, k = 3); the rate identity of Theorem 45.7 is unaffected.
4. For B*, every base 71–96 fails at k = 5 and every base 71–92 at k = 6 (full carry graph). A statement about this block only.
5. Distance rulers: every distinct-distance ruler with m marks has an m-term progression (Proposition 45.9); the ruler (0, 1, 5, 22) cannot be extended to a 6-admissible five-mark ruler (the family c = 5b − 3a always gives a 6-term progression of step c − b).
6. For A♯, no canonical schedule with radix in [1103, 1650] is admissible (548 explicit progressions); radices ≤ S(A♯) and other blocks are outside this statement.
7. Within the complete-graph family the coefficient 2 in m·log Ξ_m/log m cannot be improved; the note says this is not a lower bound for the unrestricted Λ_{m+1}. (Read and found plausible in 45a §3.3; not checked in detail.)
8. Image counts do not determine admissibility (cone dual C5).

None of these bears on the unrestricted Λ_k for k ≥ 5, which the workbench leaves open.

## 7. Overlaps (detailed in `47_`)

- 817 → zeta: ten SplitZero interface notes restate the finite constructions in the zeta programme's supported-quotient vocabulary. The finite-period receiving map (lines 1–125) was read: free vector spaces on coefficient words, the evaluation quotient, the cut map e_{(x,y)} ↦ e_{x+Q(u)y}, dim ker π = F(u)F(v) − F(uv), and a "cocycle" identity κ(u, v)κ(uv, w) = κ(v, w)κ(u, vw), which holds because both sides equal F(u)F(v)F(w)/F(uvw); it is a correct, elementary restatement. The other nine interface notes are located. Nothing flows back into the 817 proofs, and nothing is claimed about ζ.
- 817 ↔ ES: no mathematical link; the README says the work is not an Erdős–Straus artifact. The only shared items are methodological (the PolyClank record conventions; a validator design used by YM).

## 8. Not checked

Lean builds and the 44 axiom reports (no toolchain); the workbench's own verifiers (independent checks were written instead); the release ZIP and PDFs; the 951-line general-k v2 note; EP-06 optimality (47,259-block audit); EP-07 C1–C4; EP-09 beyond R1, R2 and the L > 3Q step; the all-block image Theorem A (reverse direction), B, C; the seven-observable Theorems 1–4; the general case of the cut inequality in the graphical note (m ≤ 5 checked); Costa's k = 3 preprint (arXiv:2609.06303), which the workbench cites for scope only; the exact value of g₄(7).

## 9. Checks

- `checks/workbenches/audit45_ep817/` (first pass): the k = 4 lemmas on exhaustive domains, the continuation certificates, the finite-period automaton, the light checks and three g₄ searches; the Python scripts were re-run on 26 September with identical results (the referee of the twentieth pass also recompiled and re-ran `g4_bruteforce.c`: identical for n ≤ 6).
- `checks/workbenches/g4_bitset.c` and `g4_bitset_OUTPUT.txt` (mine): the third search for n ≤ 6 (n = 6 in 30 s).
- `checks/workbenches/workbench_reader_claims_checks.py`, section EP (mine): the digit set and its modular progressions, the lift for m ≤ 3, κ_m, the B* and A♯ certificates, the composition identity.

## 10. Revision after the twentieth referee pass

A referee (a Claude instance that did not write this note) re-derived Lemmas 45.2–45.4, Theorems 45.1, 45.6, 45.7 and Proposition 45.9 and found no error; it reproduced the small values, the certificates and the negative results 3–5. Its findings, each verified before being applied:
- **Major.** §7 generalised from the one interface note that was read (the finite-period receiving map) to all ten. Corrected: the other nine are located.
- **Minor, applied.** 93^{1/6} ≈ 2.1285 (not 2.1277); the k = 3 question and Costa's reported answer; Korsky's lower bound is for fixed k ≥ 4; the workbench's own novelty statements; the Lean claims marked as the workbench's (not rebuilt here) and The Clankers' `Core.lean` credited; the constant c_r by residue class; the dependency on Lemma 45.4; the status of negative result 7; the re-run statements; the heading of §4 and the name of the g₃ source; my check script now tests 60 blocks with nonzero entries (it had tested 45).
