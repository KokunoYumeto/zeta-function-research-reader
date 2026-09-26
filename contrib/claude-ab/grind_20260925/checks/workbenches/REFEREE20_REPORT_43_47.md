# Referee report on notes 43–47 (the workbench readers and their intersections)

Referee: Claude (Opus 5.5), independent of the author (claude-ab) and of the first-pass auditors. 26 September 2026.
Read-only on all sources. Every file I created is in `scratchpad/referee20/`. No web access was used. Quotations are under 15 words.

**Scope.** Notes `43_` (Erdős–Straus), `44_` (Collatz), `45_` (Erdős 817), `46_` (Yang–Mills, NS, S⁶, Jacobian map) and `47_` (intersections). I checked them against the first-pass reports `43a`–`46a`, the inventory `47a`, the notes `21_`, `28_` and `34_`, the zeta reader (`reader/*.tex`), and the source repositories at the pinned commits: ES `d20b32e`, Collatz `caf04ff`, 817 `dbd0a93`, YM `fa79faf`, zeta `origin/main` `baa6f7a5`. I read them with `git show`, `git grep` and `git ls-tree`.

**Overall verdict.**
- The mathematics written out in the notes is sound. I re-derived every proof stated as complete: Theorem 43.1, Propositions 43.2 and 43.3, Lemma 44.3, Theorem 44.4, Propositions 44.6–44.8, Theorem 44.9, Theorem 44.12, Lemmas 45.2–45.4, Theorems 45.1, 45.6 and 45.7, Proposition 45.9, Lemmas 46.2 and 46.3, and Propositions 46.4–46.6. I found no gap, and no sign or constant error, in the proofs as written. All the numbers I recomputed agree, with one exception (93^{1/6}).
- The problems are in the surrounding statements:
  - one missing hypothesis (odd D, ES-09);
  - one false summary line (what E_a, M_a count);
  - several status labels stronger than the evidence;
  - a few false factual claims about the sources ("the one place", "attained", "the workbench itself says");
  - credit gaps;
  - omitted intersections.

**Counts.** 14 MAJOR, 56 MINOR:

| Note | MAJOR | MINOR |
|---|---|---|
| `43_` | 2 | 15 |
| `44_` | 2 | 11 |
| `45_` | 1 | 11 |
| `46_` | 1 | 8 |
| `47_` | 8 | 11 |

Two of the MAJOR findings are the same issue in two notes (43-M1 = 47-M1; 44-M2 = 47-M8).

**The author's script.** I copied `workbench_reader_claims_checks.py` and re-ran it. It prints 46 PASS lines and "ALL PASS" (5.7 s). The output is identical to `workbench_reader_claims_checks_OUTPUT.txt` apart from the four timing lines. One caveat: the κ_m check tests 45 blocks, not 60 (see 45-m6).

---

## Note 43 (Erdős–Straus)

### MAJOR

**43-M1. §3 (and the §0 row "ES-09") omit the hypothesis that D is odd.**
- *Text at issue:* "The action on (ℤ/D)³ is transitive when 3 ∤ D"; the genus formulas follow without a parity condition.
- *What is wrong:* the source proves the orbit and genus classification only for odd D. For even D the statements are false.
- *Evidence (source):*
  - `research/continuation-2026-09-12/received/es_s6_counterfactual/src/core.tex` L17: "For a positive odd integer D".
  - Same file L97: the theorem is titled "Complete odd-level classification".
  - Same file L113 uses "units modulo the odd integer D".
  - The package README L7: classification "for every odd D".
- *Evidence (my check, `referee_checks_es.py`):* all three relations hold for every D, but the action and the formulas fail for even D.

  | D | orbit sizes | genera | formula gives |
  |---|---|---|---|
  | 2 | 2, 6 | 0, 0 | g = −3/4 |
  | 4 | 16, 48 | 1, 3 | g = 7/2 |
  | 6 | 6, 18, 48, 144 | 1, 1, 5, 19 | g₀ = 7/4, g₁ = 23 |
  | 8 | 128, 384 | 17, 53 | g = 70 |

  - D = 2, 4 and 8 have 3 ∤ D, yet the action is not transitive.
  - D = 6 has four orbits, not two.
  - D = 10 and 12 fail in the same way.
  - All odd D ≤ 15 match the formulas.
- *Suggested correction:* "For odd D, the action … is transitive when 3 ∤ D …; genera … (odd D)." Add one line: in the ES application D divides R_a, which is odd, so the ES-09 equivalence is unaffected.

**43-M2. The §0 row "ES-01/02" misstates what E_a and M_a count.**
- *Text at issue:* "the solutions with a given least denominator a are counted exactly by".
- *What is wrong:* 2|E_a| + |M_a| counts all ordered pairs (y, z) with 1/a + 1/y + 1/z = 4/p. That includes solutions whose least denominator is smaller than a. Theorem 43.1(b) itself is stated correctly; only the summary is wrong.
- *Evidence (my check):*
  - p = 37, a = 22 (R = 51): the pair (y, z) = (16, 6512) is counted in shell 22, but its least denominator is 16.
  - p = 61, a = 42: the pair (24, 10248), likewise.
- *Suggested correction:* "the ordered pairs (y, z) completing a first denominator a number exactly 2|E_a| + |M_a|, and every solution has its least denominator in [3h+1, 9h]."

### MINOR

**43-m1. §2, dates of the structural items.**
- *Text:* "28 structural items (September 18–22)".
- *Problem:* the dates are wrong.
  - Item 1 is `es-turn01-joint-failure-20260917` (README L51).
  - Items 27 and 28 are dated 20260923 (README L269, L283).
  - README L44 itself says "17–21 September".
- *Fix:* "17–23 September".

**43-m2. §2 item 14, the equality case.**
- *Text:* "with equality exactly in one prime family".
- *Source:* `es-turn07-capacity-completion-20260920/core.tex`.
  - L172: equality holds exactly when w = n = 1 and t = 4ℓ + 2, an arithmetic family.
  - `thm:sharp` (L279–284): equality is realised at infinitely many primes p ≡ 1 (mod 840) for t = 6 + 420z.
- *Fix:* restate as the source does.

**43-m3. §2 item 7, the scope of the bound.**
- *Text:* "a middle solution has least denominator a ≤ 3(p+3)/11".
- *Source:* (M7) bounds every middle state (a, u) on a first-half shell p/4 < a < p/2 at a hard prime (`pointwise_localization.md` L39–41, L202–205). Here a is the shell's first denominator, not necessarily the least one.
- *My check:* no counterexample on 12 hard primes below 4,600 (`referee_item7.py`). The paraphrase is unproved beyond the source hypothesis, not shown false.
- *Fix:* "every middle state on a shell p/4 < a < p/2 has 11a ≤ 3(p+3)".

**43-m4. §0 and §6, the count of located items.**
- *Text:* "The other 16 items".
- *Problem:*
  - §2 handles 11 items (2, 3, 4, 6, 7, 8, 14, 21, 22, 23, 26), so 17 remain.
  - §2 says items 11–13 are located, but §6's list omits item 11.
- *Fix:* make the three places agree. Item 11 is partly checked in `21_`.

**43-m5. §2, last bullet, a wrong cross-reference.**
- *Text:* "§6 of `47_` places them among the intersections".
- *Problem:* `47_` §6 is "Checks".
- *Fix:* the relevant places are `47_` §0 (edges 7 and 14) and §1.4.

**43-m6. §4, rows that are not in the table.**
- *Text:* "All rows except item 24 and items 16, 18, 27, 28 were checked".
- *Problem:* those rows are not in this note's table. The sentence was copied from 43a §5.
- *Fix:* add the rows (item 24; items 16/18/27/28; the item-26 fixed-tail-sum row; X5), or delete the sentence.

**43-m7. §0 row "Item 4", the size of the enumeration.**
- *Text:* "an enumeration of about 5.9·10⁶ profiles".
- *Problem:* the enumeration covers 1,381,117,764 rooted profiles, of which 5,922,259 are range-compatible (43a §2.4 and this note's own §2). The summary understates it. The same wording is in `47_` §2.4.

**43-m8. §3, credit for the S⁶ manuscript.**
- *Text:* "from Alpöge's S⁶ manuscript".
- *Sources:*
  - The ES package calls it "the manuscript circulated by Levent Alpöge" (`es_s6_counterfactual/README.md` L5).
  - YM `ATTRIBUTION.md` L31: "circulated by Levent Alpöge and produced with Claude".
  - 47a §0.4: the PDF has no author line.
- *Fix:* use the workbench's wording.

**43-m9. The paragraph before §0, the scope of the disclaimer.**
- *Text:* "with no Lean build and no independent human review".
- *Problem:* DAILY_RESULTS_20260922 L679–687 is about that release's Python packages. The repository does contain Lean and verification material for the earlier 488-page reader (README L445; `02_ERDOS_STRAUSS_Verification_and_Lean.zip`).
- *Fix:* restrict the sentence to the 17–23 September items.

**43-m10. Credit omitted.**
- *Problem:* the note gives no credit line for the workbench. The sources give:
  - the collective byline "The Clankers" (README L469);
  - u/CommonCareful3149 for the mod-107 observation (R04) and u/UmbrellaCorp_HR (README L469);
  - the owner KokunoYumeto / u/lepthymo (`CONTRIBUTIONS.md`);
  - u/CivQ17 for R05's residue/affine diagrams (`results/records.json`, R05).
- *Fix:* add a credit paragraph, as `45_` does.

**43-m11. §1.1, wording that reads as a novelty claim.**
- *Text:* "What the workbench adds is the exact bookkeeping".
- *Problem:* no literature search was made (§6), so "adds" reads as a novelty claim.
- *Fix:* "What the workbench's texts supply beyond the classical parametrisation is …".

**43-m12. §3, "cocycle" for "class".**
- *Text:* "a cocycle of infinite order".
- *Problem:* the source says the cocycle *class* [b] has infinite order (core.tex L41–43).
- *Fix:* say "cocycle class".

**43-m13. §2 item 22, the certificates simplified too far.**
- *Text:* "two finite polynomial positivity certificates (all 221 and 192".
- *Problem:* per 43a §2.22 the exterior side has three 221-coefficient polynomials (P_E and two derivative combinations). The improvement at p ≡ 1 (mod 24) uses a further certificate: 191 positive coefficients and a zero constant term.
- *Fix:* one clause fixes it.

**43-m14. §1.2, "occupied" is used but never defined.**
- *Text:* "The shell is occupied if and only if".
- *Fix:* define it ("E_a ∪ M_a ≠ ∅, i.e. some solution has a as a denominator"). Note that for a = 3h+1 and a = 3h+2 this coincides with "least denominator a".

**43-m15. §0, the status labels.**
- *Text:* "(used in all five notes and in the reader)".
- *Problem:* the five notes also use other labels: "audited in part", "audited as a statement", "audited (arithmetic)", "audited for the least example", "audited as restatements", "verified", "not audited", "implied by YM-01", and in `47_` edge 26 "claude-ab".
- *Fix:* extend the definitions or map these onto the four defined labels.

*Confirmed correct in `43_`:*
- the proofs of 43.1, 43.2 and 43.3, including integrality of 3P₁(P₂ − 1)/4;
- the counts 27 primes / 4,398 shells, 19,564 and 4,472 primes, and 989 primes with both shells empty (first 1129, 1201, 2521; all ≡ 1 mod 24);
- the unit squares mod 840 and the 24 classes ≡ 1 (mod 24);
- the item examples: R = 47 at p = 944329; the item-26 residuals 27 and 31 and 7·29·83; 289³ ≡ 169 (mod 840); the equality primes of item 8 (t = 7, 31, 39, 47, 71);
- the item-6 claims at p = 87481: all 21,870 first-half shells have L_a ≤ 0, and 34 are occupied;
- the item-2 witness at 2521.

The 22-digit prime of item 3 has an explicit solution already in the first shell a = (p+3)/4 (`referee_item3.py`). The workbench's claim that it is solvable therefore holds independently of its verifier.

---

## Note 44 (Collatz)

### MAJOR

**44-M1. §0 row 44.10: the status label is not supported.**
- *Text:* "44.10 Collatz ⟺ an explicit abelian group vanishes (Ch. 9) | audited; a restatement".
- *What is wrong:* by the notes' own definition, "audited" means the proof was read in full, every step was checked, and independent checks were run. None of that happened for Ch. 9:
  - 44a audited Ch. 9 only "as summarized in the overview" (44a §2.6 heading).
  - 44a's reading list gives the other chapters "opening paragraph and theorem headings only" (44a §0).
  - The chapter itself (`intrinsic_zero_firstjet_20260915/note.md`, 421 lines, Theorems 1–2, §§5–8) was not read.
  - No script checks it.
- *Suggested label:* "re-derived from the overview statement (44a §2.6); chapter proof located, not read". Alternatively, audit the chapter.

**44-M2. §7: the "one place" claim is false.**
- *Text:* "This is the one place where the Collatz workbench uses".
- *Evidence:*
  - Ch. 1 (`history_law_cutoff_20260914/RESEARCH_NOTE.md` §5, L259–262) defines Z_p(s,t) = p_∂ζ(s,1) + Σ_w p_w ζ(s, 1 + t r_w). It applies the cluster reconstruction to the history law with an overflow node.
  - Ch. 2 §10 (`stopped_affine_transport_20260914/note.md` L1040ff., (10.7)–(10.10)) uses Hurwitz values ζ(−k, λ_i) for a separate finite moment reconstruction.
- *Suggested correction:* "the split-zero note, and its application in Ch. 1 §5, are the places where the Collatz workbench uses ζ(s, 1 + t); Ch. 2 §10 uses Hurwitz special values."

### MINOR

**44-m1. §4, credit for the rational-cycle criterion.**
- *Text:* "credited to the Böhm–Sontacchi and Lagarias line".
- *Problem:* Ch. 3 credits Lagarias (Acta Arith. 56 (1990) 33–53) and Mori (`cycle_relative_cohomology_20260914/note.md` L15, L867). It does not cite Böhm–Sontacchi.
- *Fix:* "credited by the chapter to Lagarias (1990); the criterion goes back to Böhm–Sontacchi".

**44-m2. §0 row 44.9: the status is understated.**
- *Text:* "conditional on the workbench's finite verification".
- *Problem:* the hypothesis is that every odd n ≤ 330,749 reaches 1. I recomputed it in under a second by stopping-time induction (`referee_checks_cz.py`). It also lies far inside published verification ranges.
- *Fix:* the result can be labelled audited, with the finite hypothesis recomputed.

**44-m3. §9, the source of the homogenisation.**
- *Text:* "from the Clankers' Zenodo record 19900461".
- *Problem:* the Collatz split-zero note cites a "local technical note, April 2026" (`note.tex` L39, L433–437). Neither "19900461" nor "Clankers" occurs anywhere in the Collatz repository. It is the zeta v11 foundation that cites the Zenodo record (47a OV-19).
- *Fix:* credit each side by its own locator.

**44-m4. §9, an incomplete list of zeta → Collatz overlaps.**
- *Text at issue:* the zeta ↔ Collatz bullet, which lists only the Hurwitz use.
- *Problem:* the Split-Zero support-module imports are missing:
  - Ch. 7 `completion_defect_20260914/note.md` L7 takes zeta `formal/splitzero/DERIVED_MATHEMATICS.md` §§1–4;
  - Chs. 8 and 9 build on the same Split-Zero support;
  - the source records of Chs. 6 and 15 read zeta.
  - 44a §5 row 3 records this edge.
- *Fix:* add it. See 47-M4.

**44-m5. §7, Theorem 44.12, credit.**
- *Problem:* the cluster-jet ↔ moments theorem and the reconstruction of the measure are the zeta programme's historical Hurwitz reconstruction:
  - zeta `…/20260913-toda/tex/historical_hurwitz_jets.tex`, (H10)–(H13), L299: the cluster germ "determines the entire compact probability input";
  - the Collatz note says so itself (`note.tex` L39–41).
- The theorem block credits only DLMF and the zeta reader's jet theorem, which supplies the Taylor coefficients; §9 mentions H10–H13.
- *Fix:* put the credit in the theorem. Also say that the multiple-zero case rests on the source proof and on H10–H13, read by 44a, and not on the sketch given here.

**44-m6. §0, a quotation that is not in the source.**
- *Text:* '"written proofs with exact finite checks"'.
- *Problem:* the phrase does not occur in the repository (grep). It is 44a's paraphrase.
- *Fix:* drop the quotation marks or quote an actual line.

**44-m7. §3, superfluous notation.**
- *Text:* "the affine map of its first j odd steps (k_j odd steps".
- *Problem:* in the source F_j(x) = (3^j x + C_j)/2^{A_j}, so k_j = j (`stopped_affine_transport` note.md L39–48).
- *Fix:* drop k_j.

**44-m8. Theorem 44.5, an undefined symbol.**
- *Text:* "a ≤ a′ ≤ ν₃(J(n/3^b) + h_e)".
- *Problem:* a′ (the number of leading exponent-1 steps) is never defined.
- *My check:* whether a′ is restricted to the least a or allowed to vary, I get exactly 367 larger members below 400,000, all with e ≤ 4. This confirms the note's count.

**44-m9. Theorem 44.11, undefined constants.**
- *Text:* "where L_c = B′/(1 − α^{−c})".
- *Problem:* c and B′ are not defined. They come from Tao's Proposition 1.11.
- *Fix:* define them.

**44-m10. §11, what was re-run.**
- *Text:* "the workbench's own checkers' outputs; re-run 26 September".
- *Problem:* `rerun_20260926/collatz/` contains only the six independent scripts. The workbench's own checkers ran once, in 44a.
- *Fix:* say so.

**44-m11. Credit omitted.**
- *Problem:* the Collatz README (L36) gives the collaboration name Kokuno Yumeto, developed with ChatGPT 5.6 Sol (Ultra mode, in Codex) and GPT-6 Astra. The note gives no credit line.

*Confirmed correct in `44_`:*
- **Proofs:** all written-out proofs.
- **Theorem 44.2:** the squeeze and the CLT step. The TV values at N = 2²⁰ (0.004, 0.044, 0.342, 0.668, 0.895) reproduce exactly.
- **Theorem 44.4:** 1,200 new pairs pass (e ≤ 40, b ≤ 10, both σ, v up to 10²⁰+1), including the range of a and 0 < m < n.
- **Proposition 44.8:** the algebra.
- **Theorem 44.9:** m* = 1636 and k ≥ 679 (exact); (C37) holds.
- **Cylinder classes:** all C(11, m) words with A ≤ 11 are realised, each in exactly one class.
- **Theorem 44.12:** the residues 19, 1, 29 for (m, A) = (2, 4); M₁ = 92/5, M₂ = 433, λ = 1/5.
- **The fixture:** (q − 3)(q + 4)/32 = 19/32 at q = 3.
- **The 3x−1 clock identity:** 6.0633.
- **Literature:** the citations are plausible (Terras, Everett, Tao FMP 10 (2022) e12, Simons–de Weger Acta Arith. 117 (2005) 51–70, Hercher arXiv:2201.00406, Barina J. Supercomput. 81 (2025) 810).

---

## Note 45 (Erdős 817)

### MAJOR

**45-M1. §7, an unsupported generalisation.**
- *Text:* "They are correct as restatements and elementary".
- *What is wrong:* the sentence covers all ten SplitZero interface notes, but only one was read, and only in part: 45a §0 lists `ep817-finite-period/notes/splitzero-receiving-map.md` L1–125.
- The other nine were not read. They total about 100 KB:
  - `all-block-image`, `arity-boundary`, `canonical-isolation`, `defect-closure`, `local-flow`, `recurrence-control`, `seven-observable` and `supported-defects` (each `…/splitzero-receiving-map.md`);
  - `graphical-obstructions/notes/splitzero-return.md`.
- *Suggested correction:* "The finite-period receiving map (L1–125) was read; it is a correct elementary restatement. The other nine are located." See 47-M3.

### MINOR

**45-m1. Theorem 45.8, a wrong decimal.**
- *Text:* "Λ₆ ≤ 93^{1/6} ≈ 2.1277".
- *Problem:* 93^{1/6} = 2.12853 (2.1277⁶ = 92.78). The workbench states only 93^{1/6}; the decimal comes from 45a.
- *Fix:* ≈ 2.1285.

**45-m2. §0, the state of the k = 3 question.**
- *Text:* "in particular whether g₃(n) ≫ 3^n".
- *Problem:* the note omits that, according to the workbench, Costa (arXiv:2609.06303v1) answered this question negatively, with liminf g₃(n)/3^n = 0 (paper `ep817_k4_rate.tex` L96–97; `problem/statement.md`; `STATUS.md`).
- The "status open" (erdosproblems.com) could not be checked here.
- *Fix:* add the Costa sentence as reported by the workbench, marked unchecked.

**45-m3. §3, Korsky's preprint.**
- *Text:* "g_k(n) ≫_k ((k − 1)/(k − 2))^n" and "22 June 2026".
- *Problems:*
  - The workbench records Korsky's lower base "for fixed k ≥ 4" (paper L91–93).
  - The workbench cites the preprint as 23 June 2026 (`notes/general-k-capacity.md` L570).
- *Fix:* add the k ≥ 4 restriction, and harmonise the date or say which one is the v1 date.

**45-m4. §3, the novelty statement.**
- *Text:* "and the workbench claims no novelty".
- *Problem:* the general-k note disclaims literature priority (L22). It also says its k = 5, 6 bounds "improve the corresponding upper rates in Korsky's inspected v1" (L69), and its title says "improved k=5,6 constructions".
- *Fix:* state both.

**45-m5. §1 and the attribution paragraph.**
- *Text:* "The upper half is Lean-checked".
- *Problems:*
  - This is the workbench's report. The audit did not rebuild the Lean code (§8).
  - The attribution paragraph credits only sneed-and-feed's upper-bound formalisation. The README (L50–52) says The Clankers formalised the central algebraic and base-19 components in Lean (`Core.lean`).
- *Fix:* "the workbench reports … (not rebuilt here)", and add the Core credit.

**45-m6. §2, "My check", the number of blocks.**
- *Text:* "on 60 random blocks".
- *Problem:* the script skips blocks that contain a zero entry. With its seed only 45 blocks are tested and 15 are skipped (instrumented re-run, `instrumented_checks.py`).
- *Fix:* say 45.

**45-m7. Theorem 45.6, the constant.**
- *Text:* "about 0.315·19^{n/3}/√n".
- *Problem:* this is exact only for n ≡ 0 (mod 3). For n ≡ 1 and 2 (mod 3) the constant is 0.354 and 0.398, since M_n = 19^{n/3}(3/19^{1/3})^r.
- *Fix:* "at least about 0.315·19^{n/3}/√n".

**45-m8. Theorem 45.6 status line, an incomplete dependency.**
- *Text:* "short-kernel lemma (Lemma 45.3)".
- *Problem:* EP-03 depends on `lem:short-kernel` and on `eq:ternary-count`, i.e. Lemmas 45.3 and 45.4 (`notes/ternary-variance-lower-bound.md` L9–11).

**45-m9. §6 item 7, a missing status.**
- *Text:* "the coefficient 2 in m·log Ξ_m/log m cannot be improved".
- *Problem:* 45a marks (6.1)–(6.4) only "Read, plausible" (45a §3.3). The item is listed without that status. This matters for `47_` §2.2 (47-M7).

**45-m10. §9, the re-run claim.**
- *Text:* "three g₄ searches; re-run 26 September with identical results".
- *Problem:* `rerun_20260926/ep817/` contains only the five Python scripts. Its one g₄ script, `g4_small_confirm.py`, covers n ≤ 5. None of the C searches (`g4_bruteforce`, `g4_decreasing`, `g4_upper7`, the n = 7 run) is there.
- I re-ran `g4_bruteforce.c` and the author's `g4_bitset.c` for n ≤ 6: the output is identical to the recorded output. The values stand; the process statement is wrong.

**45-m11. §4, heading and an unnamed source.**
- *Text:* "(new data from this audit)" and "a public repository recording g₃(1..6)".
- *Problems:* "new" can be read as a novelty claim. The g₃ source is unnamed, so it cannot be checked.
- *Fix:* rename the heading "(computed in this audit; not in the workbench)", and give the locator of the g₃ source or drop it.

*Confirmed correct in `45_`:*
- **Proofs:** 45.1–45.9 as written.
- **The g₄ values:** reproduced for n ≤ 6 (1, 3, 5, 14, 40, 79, with optimal-set counts 1, 2, 2, 2, 7, 1) by two programs. The 7-set with maximum 246 and the unique optimal 6-set (|T| = 361) are admissible.
- **Certificates:** B* (S = 70, |H| = 38; mod 97, mod 93) and A♯ (distances, S = 1102, |H| = 291, mod 1651, the 5-AP 0…1028).
- **Negative results 3, 4, 5:**
  - {2, 7} has a modular 3-AP mod 11, but its base-11 languages of lengths 1–4 are 3-AP-free;
  - every base 71–96 (k = 5) and 71–92 (k = 6) gives an integer AP in the 2-digit language, while 97 and 93 give none up to 3 digits;
  - no mark z ≤ 3000 extends (0, 1, 5, 22) to a 6-admissible distinct-distance ruler.
- **Proposition 45.9:** holds on 200 random rulers.
- **Theorem 45.6 constants:** the κ_m identities and the refined table 1, 3, 5, 11, 27, 49.
- **Korsky-type rates:** 5^{2/3} = 2.924, √5 = 2.236, 7^{2/5} = 2.178.
- **Credits:** the anonymous Reddit contributor for the k = 4 proof, The Clankers, and sneed-and-feed are credited as in the README (L38–64) and in `STATUS.md`.

---

## Note 46 (Yang–Mills, NS, S⁶, the Jacobian map)

### MAJOR

**46-M1. §6, credit for the S⁶ construction is incomplete.**
- *Text:* '"produced with Claude" in `ATTRIBUTION.md`'.
- *What is wrong:* the workbench's designated wording is "circulated by Levent Alpöge and produced with Claude" (`ATTRIBUTION.md` L31; also `s6/README.md` and the YM README L31). The note quotes only the second half and names Alpöge nowhere in §6; only the URL alpo.ge appears. A reader following the note could credit the construction to Claude alone.
- *Suggested correction:* "The construction was circulated by Levent Alpöge and produced with Claude (ATTRIBUTION.md, the designated clarification); older files say 'with Fable'."

### MINOR

**46-m1. §1.5, wording that reads as a novelty claim.**
- *Text:* "What the workbench adds is an explicit, box-uniform bound".
- *Problem:* no novelty search was made.
- *Fix:* "What the workbench proves is …".

**46-m2. §7, "holds" for "is proved".**
- *Text:* "it holds only at strong bare coupling".
- *Problem:* nothing is shown for g² < 3.68.
- *Fix:* "it is proved only for g² ≥ 3.68…".

**46-m3. §1.4, the sensitivity claim.**
- *Text:* "is robust to such errors".
- *Problem:* the sensitivity run covers only (m₅, t₅). Errors in (m₃, t₃) and (m₄, t₄), which were not re-derived, were not assessed. My recomputation of the ×2 case agrees: α = 0.017905, g² = 3.7366, d₅(1/64) = 1.8946.
- *Fix:* add the scope.

**46-m4. §1.1, an ambiguous locator.**
- *Text:* "(F8: g_C = 2^{3/4}g)".
- *Problem:* `FIFTH_REFERENCE.md` numbers both its section headings (F1–F8) and its equations ((F1)–(F42)). Equation (F8) defines Γ and B (L82). The convention change is in the section "F8. Sources and evidence" (L435–441).
- *Fix:* write "§F8". Likewise, Lemma 46.2's "F7" is the equation (F7), which sits in section F2.

**46-m5. §1.3, a spectrum statement stronger than intended.**
- *Text:* "The spectrum of H₀ is {0} ∪ [3/4, ∞)".
- *Problem:* the spectrum is the discrete set {Σ j_e(j_e+1)}.
- *Fix:* "is contained in"; the proof only uses that.

**46-m6. Status labels outside the defined four.**
- *Problem:* the note uses "audited in part", "audited as a statement", "audited (arithmetic)", "verified", "implied by YM-01" and "not audited" (see 43-m15).

**46-m7. Credit omitted.**
- *Problem:* the YM README (L61) calls the workbench AI-assisted, including work with ChatGPT 5.6 Sol and GPT-6 Astra. The note gives no workbench credit line.

**46-m8. §10, what was re-run.**
- *Text:* "Re-run 26 September: identical."
- *Problem:* only 46a's three scripts were re-run (`rerun_20260926/ym/`). The producer and auditor logs come from 46a's single run.
- *Fix:* say so.

*Confirmed correct in `46_`:*
- **Lemma 46.2:** the proof, including disjointness and the at-most-twice count on the bipartite cubic graph. It matches (F7).
- **Lemma 46.3 and Proposition 46.4:** the algebra, including d₅ = 3(1 − χ) and the small root w_*. Both agree with F33–F37.
- **Proposition 46.5:** the §27 radii, 1/1280 at L = 2 and ~1/(128j⁶).
- **Proposition 46.6:** the mod-9 argument and the gcd 2 on D₄.
- **Inputs and numbers:**
  - the F26 rationals match the author's inputs exactly;
  - α₅ = 0.01842495357611761668188 and the threshold 3.683551983985727304439;
  - d₅ = 1.620721 at g² = 37/10, 1.699349 at 15/4 and 1.906830 at 4 (matching F38);
  - d₅(α₅) = 1.54531 and d₅(1/55) = 1.63763 > 13/8.
- **YM-05:** d₅ ≥ d_[4] on [0, α_[4]], so YM-05 is implied by YM-01.
- **The Keller map:** det DF = −2 and the curve γ: F(γ(τ)) = (2τ − 1/4, 0, 0) and DF(γ)γ′ = (2, 0, 0).
- **Credit for F:** the note matches `ATTRIBUTION.md` L9 (Alpöge's announcement, crediting Akhil and Fable).
- **NS-00:** "OpenAI's manuscript" matches `SOURCE_READING_20260920.json`.
- **Quotations and source constants:** the WORKBENCH.md L21 quotation, the YM-02/YM-03 constants (67896/169, 1/55, 3/256, 45/4096), and README L117 on the producer not being re-run at publication.

---

## Note 47 (intersections)

### MAJOR

**47-M1. §1.3 (and edge 3): the odd-D hypothesis is missing.**
- *Text:* "transitive on (ℤ/D)³ when 3 ∤ D".
- *Problem:* the same as 43-M1.
- *Fix:* add "for odd D".

**47-M2. §1.1 and edge 1: what crosses is misstated, and the credit is misplaced.**
- *Text:* "From zeta: the jet formula" … "From Collatz: only the residues r_w".
- *What is wrong:* the Collatz note imports the zeta programme's historical Hurwitz reconstruction (`historical_hurwitz_jets.tex`, H1–H13, especially H10–H13). That is the theorem that the zero-cluster jet at any nontrivial zero determines all moments and reconstructs the measure (the §§ at L23 and L231; L299).
  - The Collatz note says so (`note.tex` L39–41; bibitem L438–442).
  - The zeta reader's Theorem "the first Hurwitz jet" (proved by claude-ab in `17_`) is not what the Collatz note cites. It cites DLMF 25.11.10 and H1–H13.
- *Suggested correction:* "From zeta: the reconstruction theorem of the historical Hurwitz file (H10–H13), with the Taylor coefficients b_j (DLMF 25.11.10; zeta reader, first Hurwitz jet (a)). From Collatz: the node set r_w."

**47-M3. Edge 16 and §3: an unsupported status.**
- *Text:* "audited as restatements (`45_` §7)".
- *Problem:* only one of the ten notes was read, partly (see 45-M1).
- *Fix:* "one of ten read (finite-period, L1–125); the rest located".

**47-M4. The completeness claim in the header is false: intersections are missing.**
- *Text:* "This note collects every intersection found".
- *Missing edges:*
  - **zeta → Collatz, the Split-Zero support modules and killed-representative quotient.** Collatz Ch. 7 `completion_defect_20260914/note.md` L7 cites zeta `formal/splitzero/DERIVED_MATHEMATICS.md` §§1–4 at `91ed3b7c`, "instantiated on the Collatz operator". Chs. 8 and 9 build on the same Split-Zero support. The source records of Chs. 6 and 15 read zeta. 44a §5 row 3 records this edge. It is in neither the table nor §1.
  - **47a OV-26** (YM's summary of the zeta routes, type A) is dropped. It survives only as D1.
- *Fix:* add both.

**47-M5. §2.1: an assessment attributed to the workbench that it does not make.**
- *Text:* "In each instance the workbench itself says the restatement is not progress".
- *What is wrong:* this is not so for ES-09.
  - The ES package presents `thm:failure` as a "Complete failure object". It identifies the obstruction with a cohomology class of exact order D (`es_s6_counterfactual/README.md` L3–7; `src/arithmetic.tex` L109–125).
  - It does not say the criterion is ES-02 restated. That is 43a's assessment (43a §4).
- *Suggested correction:* attribute the assessment instance by instance: "the workbench records this limit for ES-02, Ch. 9, the Hurwitz note, NS-04(a) and 817 → zeta; for ES-09 it is the audit's assessment".

**47-M6. §1.2: "attained" is false, and a normalisation is missing.**
- *Text:* "attained along Pell vectors".
- *What is wrong:* the infimum is never attained.
  - `21_` Lemma 21.3 proves |v·k|‖k‖₂ > 1/√(4+2√2) strictly for every nonzero k. The Pell vectors only approach the bound, with an excess of order (1+√2)^{−4j}.
  - My search over |k|∞ ≤ 400 gives a minimum of 0.38268343238645 at (−70, −169). That is above 1/√(4+2√2) = 0.38268343236509, by 2.1·10⁻¹¹.
- *Also missing:* the constant holds for the normalisations v_r = (1, 1−√2) and v_t = (√2−1, 1). For unit eigenvectors the infimum is 1/√8.
- *Fix:* "approached, never attained, along Pell vectors, for v_r = (1, 1−√2), v_t = (√2−1, 1)".

**47-M7. §2 and §2.2: an instance presented as proved that is not.**
- *Text:* "each of which is proved in the note cited".
- *What is wrong:*
  - §2.2 lists "817 negative results 3, 4, 6, 7". Item 7 (the complete-graph leading law) is only "Read, plausible" in 45a §3.3 and is not proved in `45_`.
  - The §2.1 instance "Ch. 3: Collatz ⟺ H₀ = 0" is mentioned in `44_` §5 but not proved there.
- *Suggested correction:* drop item 7 or mark it located, and cite 44a's table for Ch. 3.

**47-M8. §1.1: the "one place" claim is false.**
- *Text:* "It is the one place where a workbench other than zeta uses".
- *Problem:* Collatz Ch. 1 §5 uses the same ζ(s, 1 + t r_w) family (see 44-M2).
- *Fix:* correct as there.

### MINOR

**47-m1. Edge 18, §1.8 and §5, the locator for the Collatz side.**
- *Text:* "CZ side (Zenodo 19900461) external".
- *Problem:* the Collatz side is the split-zero note §2.1, which is in the cloned repository and was read by 44a. That note cites a local April 2026 note (`note.tex` L433–437). Only zeta cites the Zenodo record.
- *Also:* the §3 corrections to the zeta reader's table should fix the same row. The reader's §8.4 says the Collatz side is the Zenodo record.

**47-m2. §0, one file counted as used by two workbenches.**
- *Text:* "Two zeta files are each used by two workbenches".
- *Problem:* `FABLE_TO_ORIGINAL_CONDUCTOR.tex` is used twice by ES (edges 7 and 14), not by two workbenches.

**47-m3. §2.2, a quotation not in the source.**
- *Text:* '"within the exact scope of what did not work"'.
- *Problem:* the phrase is not in the zeta reader. Its §7 is titled "Routes that do not decide the location of the zeros, with their exact scope" (`reader/sec7_negative.tex` L1).
- *Fix:* drop the quotation marks or quote correctly.

**47-m4. §1.1, the zeta reader's theorems described inaccurately.**
- *Text:* "study how the zero set of ζ(s, 1 + t) moves with t".
- *Problem:* the mirror theorem concerns the sets Z, Z − 1 and A(Z), with no motion in t. The reader stresses that the Hurwitz flow does not translate the zero set (`sec4_twolines.tex` L4).
- *Fix:* rephrase, e.g. "the jet theorem computes the first-order motion; the mirror theorem identifies the nodal set of the first jet".

**47-m5. §2.3, the 817 result misclassified.**
- *Text:* "817: exact rates for k = 4 and upper bounds for k = 5, 6".
- *Problem:* the k = 4 theorem answers the k = 4 exponential-rate question itself. Listing it under "limits taken in the wrong order" understates it.
- *Fix:* move it, or keep only the k ≥ 5 part.

**47-m6. §2.2, instances that do not fit the stated pattern.**
- *Pattern as defined:* "an explicit instance where P holds but the certificate fails".
- *Problem:* Collatz 44.2(c) and 817 items 4, 6 and 7 do not fit this definition. Items 4 and 6 are failures of a construction; 44.2(c) is a distributional statement.
- *Fix:* adjust the definition or the list.

**47-m7. The status column.**
- *Text:* "audited / audited in part / located, as in `43_`".
- *Problems:*
  - `43_` defines audited, audited (certificate), conditional and located; "audited in part" is not among them.
  - Edge 10's "audited on random rational matrices" is a numerical check of standard Schur-complement algebra, not an audited proof.
  - Edge 26's "claude-ab" is not a status.
- *Fix:* map these onto the defined labels.

**47-m8. §2.4, the size of the ES item-4 enumeration.**
- *Text:* "5.9·10⁶ profiles".
- *Problem:* the domain has 1,381,117,764 rooted profiles, of which 5,922,259 are range-compatible (as 43-m7).

**47-m9. §2.4, the Collatz Theorem 44.9 row.**
- *Text:* "the database not re-run".
- *Problem:* the finite hypothesis takes under a second to recompute, and I recomputed it (see 44-m2).
- *Fix:* the row can say so.

**47-m10. §3, corrections to the zeta reader's table missed.**
- *Problem:* §3 omits two corrections to the zeta reader's overlaps table:
  - the Collatz side of the homogenisation row (47-m1);
  - the missing zeta → Collatz Split-Zero imports (47-M4).

**47-m11. Edge 17 and §1.8, credit for R05.**
- *Problem:* ES R05's record credits u/CivQ17 (residue/affine diagrams), KokunoYumeto/u/lepthymo and The Clankers (`results/records.json`, R05). The note gives none of these.
- *Fix:* add the credits.

*Confirmed consistent with 47a, `21_`, `28_`, `34_` and the sources:*
- **Edges:** the types and statuses of edges 2, 4–9, 11–15, 17, 19–25, 27 and 28.
- **The group identity:** {(u, v) : u³v = 1 = uv⁵} = {(u, u⁻³) : u¹⁴ = 1}; J has determinant 14 and eigenvalues 4 ± √2.
- **Lemmas:** the Gram sandwich (δ ≤ 1 is needed) and Lemma 28.2's D = det B.
- **Theorem 14.2's description:** matches `34_`.
- **The zeta quotation:** "did not itself produce" (zeta `ATTEMPTS.md` L19).
- **D1:** the zeta value is 2.0984855607004·10⁻¹¹ (zeta `satellites/29f_actual_theta_weil.tex` L294). The YM files give it as 10⁻¹⁹ at `ATTEMPTS.md` L274 and `research-attempts.json` L918; L915 of the latter has the correct 10⁻¹¹.
- **D3:** ES `RESEARCH_DIRECTIONS.md` L61.
- **D4:** zeta satellites 23/26/27 cite Tao, Speyer and Poplett for F.
- **The zeta reader's DOI:** 10.5281/zenodo.22970703, as recorded in `00_RESULTS_REGISTER.md`.

---

## Cross-cutting points (for the reader as a whole)

1. **Status labels.** Either widen the four-label vocabulary of `43_` §0 or map every label onto it. Several items carry labels stronger than their evidence: 44.10, 817 → zeta, and 47 edges 10 and 16.
2. **Statements about re-runs** in `44_` §11, `45_` §9 and `46_` §10 overstate what `rerun_20260926/` contains. In each case only the independent Python scripts were re-run.
3. **Credit lines.** Give one per workbench, as `45_` does: ES (The Clankers; named Reddit contributors), Collatz (Kokuno Yumeto; ChatGPT 5.6 Sol, GPT-6 Astra), YM (AI-assisted; ChatGPT 5.6 Sol, GPT-6 Astra; S⁶ "circulated by Levent Alpöge and produced with Claude").
4. **"What the workbench adds …"** (43 §1.1, 46 §1.5) reads as a novelty assessment. None was made.
5. **The remaining statements are accurately scoped.** None of the five notes claims a bearing on RH, the Collatz conjecture, the Erdős–Straus conjecture or the Yang–Mills mass gap beyond what is proved, and every negative result is given its scope.

---

## Checks I ran (all in `scratchpad/referee20/`; each took under 5 minutes)

| # | Check | Result |
|---|---|---|
| 1 | The author's `workbench_reader_claims_checks.py`, copied and re-run (`rerun_OUTPUT.txt`) | 46 PASS lines, ALL PASS; identical to the recorded output apart from timings |
| 2 | `instrumented_checks.py` (the same script, counting κ-blocks) | 45 blocks tested, 15 skipped (45-m6) |
| 3 | `referee_checks_es.py` | Findings: ES-09 fails for even D (43-M1); shell counts include pairs with a smaller least denominator (43-M2). Confirmed: the ES-09 relations; odd D ≤ 15 match the formulas; the §1 counts; the item arithmetic; P₂ ≡ 1 (mod 4) for all a ≡ 1 (mod 3) below 2·10⁵ |
| 4 | `referee_item6.py` | p = 87481: all 21,870 first-half shells have L_a ≤ 0 (maximum 0); 34 occupied |
| 5 | `referee_item3.py` | The 22-digit prime (≡ 121 mod 840, BPSW prime) has an explicit solution in the shell a = (p+3)/4 |
| 6 | `referee_item7.py` | 12 hard primes below 4,600: no middle solution with least denominator > p/2 |
| 7 | `referee_checks_cz.py` | All odd n ≤ 330,749 reach 1; m* = 1636 and k = 679; (C37) holds; all C(11, m) words realised, one class each; Theorem 44.4 on 1,200 pairs, no failure; Proposition 44.8 algebra; the (2, 4) residues and moments; the fixture; the TV values at N = 2²⁰ reproduce |
| 8 | `referee_checks_extra.py` and the `least a` variant | 367 template members below 400,000, all with e ≤ 4; the {2, 7}, q = 11 example |
| 9 | `referee_checks_extra2.py` | B*: every base 71–96 (k = 5) and 71–92 (k = 6) gives an integer AP in the 2-digit language; bases 97 and 93 give none up to 3 digits |
| 10 | `referee_checks_ep.py` | 93^{1/6} = 2.12853, not 2.1277 (45-m1). Confirmed: the other decimals and the Korsky-type rates; the κ_m identities; the refined table; certificates B* and A♯; Proposition 45.9 on 200 random rulers; (0, 1, 5, 22) not extendable up to z = 3000; the witnesses admissible |
| 11 | `g4_bitset.c` and 45a's `g4_bruteforce.c`, recompiled and re-run | Identical to the recorded outputs for n ≤ 6 (30 s and 7 s) |
| 12 | `referee_checks_ym.py` | α₅, the thresholds and the d₅ values; χ ∈ [0, ½); d₅ ≥ d_[4] on [0, α_[4]]; the ×2 sensitivity; d₅ = 3(1 − χ); the w_* root; the §27 radii; det DF = −2 and the curve γ; S6-5; the NS→ES infimum not attained (47-M6) |
| 13 | `referee_clock3xm1.py` | The 3x−1 clock identity equals 6.0633 on both sides |
| 14 | Source spot-checks | ES: RESEARCH_STATE L33, DAILY_RESULTS_20260922 L679–687, the Elsholtz–Tao attributions, the item 6, 7, 14, 22 and 23 statements, ES-09 core.tex and README, README credits and dates. Collatz: README L36, QUARANTINED.md, Ch. 6 Theorems 8–9 (L404–446), Ch. 3 credits, the split-zero bibliography, Ch. 1 §5, Ch. 2 §10, Ch. 7 §1, the Ch. 9 length, the disclaimers per note. 817: README, STATUS, statement.md, paper L91–97, general-k L22/L69/L570, the EP-05 and EP-03 status lines, the interface-note list. YM: F26 and F28–F38, F7, §F8, fifth-reference README, ATTRIBUTION, s6 README and TeX, NS SOURCE_READING, HEAT constants, 20260921 README, WORKBENCH L21. Zeta: historical Hurwitz file, ATTEMPTS L19, satellite 29f L294, satellites 23/26/27, reader sec4 and sec7. At least 5 per note; all results as reported above |

One run was killed at the 295-second limit: the B* part of `referee_checks_extra.py`, which used an O(n²) search on 3-digit languages. Its results were obtained instead by the bitset version in check 9.
