# Referee 23: "Four workbenches and where they meet" after the understatement pass

Referee 23 (Claude, Opus 5.5), 26 September 2026. I wrote none of the reader, the notes, the first-pass reports or the earlier referee reports. I worked read-only; every file I made is in `scratchpad/referee23/`.

**What was read.**
- The whole reader: `wbreader/*.tex` and the 33-page PDF. Page numbers below are those of `wbreader.pdf`; they agree with the `.aux` labels.
- The notes `43_`–`47_`, especially their 09:05 UTC "Second generalisation pass" sections, and the first-pass reports `43a_`–`46a_` where needed.
- The referee-22 report.
- Workbench sources at the pinned commits:
  - Collatz: history-law note, Ch. 2 §7, Ch. 6 Thms 8–9, Tao-clock `consequences.tex`.
  - Erdős 817: variance note, general-k chapters, chs. 08, 22, 24.
  - Yang–Mills: `CUMULATIVE_RESEARCH.md` (F26–F38; G, R and L series), the 16 September continuation, YM-07 §27.
- Three public literature pages:
  - Hercher's arXiv abstract page.
  - Crossref metadata for both Barina papers.
  - Barina's 2025 paper, which is CC-BY. I took it from the publisher's text-mining PDF link listed by Crossref. The article landing pages answered with a JavaScript challenge, which I did not get round.

**Re-runs of the author's checks** (from my folder, output only there):
- `generality_checks.py`: output identical to the recorded one (timing lines excluded).
- `workbench_reader_claims_checks.py`: 47/47 pass.

## Summary

| # | Where (page, label) | Class | Finding |
|---|---|---|---|
| M1 | §1.2, paragraph after Prop. 1.3 (p. 6); App. A (p. 31) | MAJOR (false statement) | The "Generalised here" claim that Prop. 1.2 holds for every prime p ≡ 1 (mod 4) is false for p ≡ 5 (mod 12). There E_a ≠ M_a and the counts differ; the paragraph contradicts itself. The check G17 does not test it. |
| M2 | Cor. 2.9 and status (p. 12); front matter (p. 2); §5 table (p. 29); §6 (p. 30) | MAJOR (substantial understatement, misleading sentence) | The two papers the reader cites (Hercher 2023, Barina 2025 §6) already give a nontrivial cycle length ≥ 355,504,839,929, i.e. m ≥ 137,528,045,312. That is about 1.9 times Cor. 2.9. The status line's "improves them only beyond 2^71.88" holds only for the plain Eliahou argument. |
| M3 | Cor. 4.5 and status (pp. 21–22); Thm 4.1 status (p. 19); front matter (p. 2) | MAJOR (wrong status, misattribution) | Cor. 4.5(a) is the workbench's own YM-06 theorem (G22, G26–G29) word for word. The workbench also has order-2 gap theorems: R10 at g² ≥ 4.1156, and L17 at 3.826 with extra computed input. "Generalised here" and the front matter's credit to the audit for "the gap theorem at truncation order 2" misattribute. |
| M4 | Thm 2.2 status (p. 9) | MAJOR (wrong status, misattribution) | The workbench's history-law note does state explicit polynomial rates, (4.3)–(4.4). It also says that all its statements are uniform in b. The reader's second rate is weaker than the workbench's (4.4), yet is labelled "Generalised here". |
| M5 | Thm 3.7 status (p. 16) | MAJOR (wrong status; small impact) | The (M_n−1)/(2n) bound is labelled "Generalised here". The workbench's EP-03 note (§6) already states the stronger 2nN ≥ M_n + n(n−1) − 1. |
| m1 | Thm 1.1(c) (p. 4) | minor | The range p/4 < a < p/2 works for every odd prime, not only for p ≡ 1 (mod 4). |
| m2 | Thm 2.2(a) (p. 9) | minor | The sandwich holds for every H ≥ 0, not only H ≥ m. The workbench's (3.2) says so, and the case split in the proof of (c) becomes unnecessary. |
| m3 | Thm 3.8 status, Λ₃ = 3 (p. 17) | minor | The phrase "given the cited Erdős–Sárközy bound" is unnecessary: g₃(n) ≥ (3ⁿ−1)/(2n) has a three-line proof from Lemma 3.2's argument. The workbench's own located chs. 22 and 24 state the injectivity and "ρ = 3 = λ₃". |
| m4 | Prop. 3.5 status (p. 16) | minor | (c) does not rest on the exhaustive searches: three explicit admissible sets suffice. |
| m5 | §5 certificate table (p. 29) | minor | The table says "three independent programs"; Prop. 3.11's status says three plus a fourth. |
| m6 | Front matter "Who did what" (p. 2) | minor | Lists "the range x < p/2" as the audit's own, but the workbench's item 22 already has the least denominator in (p/4, p/2) at p ≡ 1 (mod 12). Thm 1.1's status says so; the front matter does not. |
| m7 | Prop. 3.10 status (pp. 17–18) | minor | EP-05 Thm 3.1 is more general (signed disjoint lifts) than the proposition's first sentence. Only the ruler corollary is generalised. |
| m8 | 2^33 paragraph (p. 12) | minor | "Computed" requires independently run programs, but only one is named. Two independent re-runs exist, including this pass's. |
| m9 | Prop. 2.5 (p. 11) | minor (optional) | The per-member criterion is exact: a member descends iff D > 0 and n > C/D. |

Findings M1–M5 also apply, word for word, to the corresponding sections of the notes:
- M1: `43_` §§0, 10.
- M2: `44_` §§0, 13–14 and `47_` §2.4.
- M3: `46_` §§0, 13 and `47_` §8.
- M4: `44_` §§0, 14.
- M5: `45_` §12.

The reader and the notes are consistent with each other; the errors are shared.

---

## MAJOR findings

### M1. Proposition 1.2 does not hold at primes p ≡ 5 (mod 12)

**Location.**
- §1.2, the paragraph after Proposition 1.3 (p. 6), labelled *Generalised here*.
- Appendix A, "Independent checks" (p. 31): "Propositions 1.2–1.3 for every prime p ≡ 1 (mod 4) below 3·10⁴".
- Note `43_` §0 (ES-03 row) and §10.

**What the text says.** "Both propositions hold for every prime p ≡ 1 (mod 4)", checked "on all 1,611 such primes below 3·10⁴". Two sentences later it says that for p ≡ 5 (mod 12) the choice a = (p+3)/4 "puts u=1 in M_a".

**What is wrong.**
- Proposition 1.2 asserts three things:
  - E_a = M_a = {u | a² : u ≡ 2 (mod 3)};
  - |E_a| = |M_a| = P₁(P₂−1)/2;
  - there are exactly 3P₁(P₂−1)/4 unordered solutions with least denominator a.
- Its proof uses a ≡ 1 (mod 3), in "u + a ≡ u + 1". For p ≡ 5 (mod 12), a = (p+3)/4 ≡ 2 (mod 3), so u + a ≡ u − 1 and M_a = {u | a² : u ≡ 1 (mod 3)} ≠ E_a.
- The paragraph contradicts itself: it puts u = 1 in M_a, but 1 ≢ 2 (mod 3).
- Counterexamples:
  - p = 5, a = 2: E_a = {2}, M_a = {1, 4}. Prop. 1.2 predicts E_a = M_a = {2}.
  - p = 17, a = 5: E_a = {5}, M_a = {1, 25}.
- The stated form fails at **all 819** primes p ≡ 5 (mod 12) below 3·10⁴.
- The author's check G17 only tests, at those primes, `if 1 not in M3: bad += 1` (`generality_checks.py` l. 366). So the claimed check does not test the claim.

**Corrected statement.** Let p ≡ 1 (mod 4) be prime and a = (p+3)/4, so R_a = 3. Then:
- E_a = {u | a² : u ≡ 2 (mod 3)} and M_a = {u | a² : u ≡ −a (mod 3)}.
- For p ≡ 1 (mod 12), Proposition 1.2 holds as stated.
- For p ≡ 5 (mod 12):
  - M_a = {u | a² : u ≡ 1 (mod 3)};
  - |E_a| = P₁(P₂−1)/2 and |M_a| = P₁(P₂+1)/2;
  - there are exactly P₁(3P₂−1)/4 unordered solutions with least denominator a;
  - the shell is always occupied (1 ∈ M_a).
- The occupancy criterion "a solution with least denominator a exists iff a has a prime factor ≡ 2 (mod 3)" holds for every p ≡ 1 (mod 4). At p ≡ 5 (mod 12) both sides are true, since a ≡ 2 (mod 3) forces such a factor.
- Proposition 1.3 does hold for every prime p ≡ 1 (mod 4) as claimed (checked below). Proposition 1.4 then holds verbatim for every prime p ≡ 1 (mod 4), trivially at p ≡ 5 (mod 12).

**Proof.**
1. With p = 12h′+5 we have a = 3h′+2 ≡ 2 (mod 3), and 3 ∤ a.
2. Modulo 3, 4u+1 ≡ u+1 and u+a ≡ u−1. So E_a = {u ≡ 2} and M_a = {u ≡ 1}.
3. As in the proof of Prop. 1.2, a divisor u of a² satisfies u ≡ (−1)^{Σe_ℓ}, with the sum over the primes ℓ ≡ 2 (mod 3).
4. The number of exponent vectors with even sum minus the number with odd sum is ∏(Σ_{e=0}^{2v}(−1)^e) = 1. So #odd = P₁(P₂−1)/2 = |E_a| and #even = P₁(P₂+1)/2 = |M_a|.
5. R_a = 3 ≠ 1, so by Thm 1.1(b) the unordered pairs number |E_a| + |M_a|/2 = P₁(3P₂−1)/4. Each has least denominator a, since a = (p+3)/4 is the least possible.
6. Integrality: a ≡ 2 (mod 3) makes the total exponent of the primes ≡ 2 (mod 3) odd. Then P₂ ≡ 3 (mod 4) and 4 | 3P₂−1. ∎

**Check** (`r23_es.py`).
- At all 819 primes p ≡ 5 (mod 12) below 3·10⁴, the stated form fails and the corrected form holds.
- At all 792 primes p ≡ 1 (mod 12) below 3·10⁴, Prop. 1.2 holds as stated.
- Direct enumeration of all solutions at the primes p ≡ 5 (mod 12) below 700 gives P₁(3P₂−1)/4 solutions with least denominator (p+3)/4, never 3P₁(P₂−1)/4.
- Prop. 1.3's criterion holds at all 1,611 primes p ≡ 1 (mod 4) below 3·10⁴.

### M2. Corollary 2.9 is weaker than the published bound in the two papers it cites

**Location.**
- Corollary 2.9 and its status (p. 12).
- Front matter "Who did what" (p. 2): "the Eliahou-type cycle bounds … from Barina's published range".
- §5 certificate table (p. 29).
- §6 "Everywhere" (p. 30), which records "a check of the abstracts or publisher pages" of Barina (2021, 2025), Hercher and Eliahou.

**What the text says.**
- Cor. 2.9 gives m ≥ 72,057,431,991, A ≥ 114,208,327,604, A+m ≥ 186,265,759,595 and k ≥ 29,906,536,378.
- The status adds that any verified range between 2^67.56 and 2^71.88 gives the same bounds, and "a larger one improves them only beyond 2^{71.88}".

**What is wrong or understated.**
- Hercher, *J. Integer Seq.* 26 (2023) 23.3.5 (the reader's [Hercher]). The arXiv abstract, which I read on arxiv.org/abs/2201.00406, says two things:
  - its last part raises the number of odd members of a nontrivial cycle "to at least K ≥ 1.375·10^11";
  - for that it suffices that every integer up to "1536·2^60 = 3·2^69" reaches the trivial cycle.
- 3·2^69 ≈ 2^70.585 is below Barina's 2^71.
- Barina, *J. Supercomput.* 81 (2025) 810 (the reader's [Barina]), §6 "Results", says that at 2^71 "the length of a non-trivial cycle rises to 355 504 839 929". Its reference [12] is Hercher 2023.
- 355,504,839,929 = 217,976,794,617 + 137,528,045,312, where 217976794617/137528045312 is the next upper best approximation of log₂3 after the reader's fraction (my continued-fraction run, `r23_collatz.py`).
- So the literature the reader cites, and says it checked, gives bounds about 1.909 times the reader's.
- The status sentence is true only for the plain Eliahou argument. Hercher's refinement moves the needed range from s_hi = 2^71.884 down to 2^70.585.

**Stronger statement (Conditional on Hercher's theorem and Barina's 2025 computation).** Every nontrivial positive cycle of T has:
- at least 137,528,045,312 odd steps;
- at least 217,976,794,617 halvings, so at least 355,504,839,929 steps of n ↦ n/2, n ↦ 3n+1, as Barina 2025 §6 states;
- at least 57,079,296,007 steps with exponent 1 (derived here).

Corollary 2.9 remains correct as the statement of what Eliahou's method alone gives from 2^68.

**Proof.**
1. Barina verified every n < 2^71, and 3·2^69 < 2^71. Hercher's theorem therefore gives m ≥ K = 137,528,045,312.
2. A > m·log₂3 ≥ 137,528,045,312·log₂3 = 217,976,794,616.9999999999987…, so A ≥ 217,976,794,617.
3. The least element s satisfies s ≥ 2^71+1. As in the reader's proof, k ≥ 2m−A ≥ m(2 − log₂(3+1/s)) ≥ 137,528,045,312·(2 − log₂(3+2⁻⁷¹)) = 57,079,296,006.99999999997…. ∎

**Check.**
- `r23_hercher.py` (80 digits) computes the three bounds and the ranges 2^70.585 and 2^71.884.
- `hercher_abs.html` is the saved arXiv page. `barina2025.txt` lines 65–68, 118–119, 559–561 and 579–582 hold §1, §2, Table 10 and §6.
- All of the reader's own Cor. 2.9 numbers are correct (see "Verified" below).

**Suggested wording.**
- Keep Cor. 2.9 as "what Eliahou's argument gives from Barina's 2021 range".
- Add the published bound above, with its attribution and a *Conditional* label naming Hercher (2023) and Barina (2025).
- Delete or qualify "improves them only beyond 2^71.88".
- Correct §6's description of the literature check.

### M3. Corollary 4.5(a) is the workbench's own theorem, and the workbench already has order-2 versions

**Location.**
- Corollary 4.5 and its status "Generalised here" (pp. 21–22).
- Theorem 4.1 status (p. 19).
- Front matter "Who did what" (p. 2): "the gap theorem at truncation order 2 with audited inputs only".
- §5 "Method obstructions" (p. 29) and Appendix A (p. 32).

**What the text says.**
- Cor. 4.5 is "Generalised here".
- Its status says that (a) and (b) are "audited statements with no unverified input", and that the qualitative content of Thm 4.1 holds unconditionally for g² ≥ 4.0187.
- The front matter credits the audit with the order-2 gap theorem.

**What is wrong.** The workbench states these results itself in YM-06 (14–16 September). Sources:
- `yang-mills/consolidation/20260916/reader/yang_mills_web_continuation.md`;
- the same text inside the fifth-reference package's `CUMULATIVE_RESEARCH.md`, lines 4262–4333, 4473–4507 and 7270–7320. That is the package whose F1–F42 the audit read.

The statements are:
- **Order 1.**
  - (G22) "0<ξ≤3/256, g²≥8/√3".
  - (G26) Δ_L ≥ d_phys(ξ)κ with d_phys = (3/2)(1+√(1−256ξ/3)).
  - (G28) Δ_L > 2.07445κ at g² ≥ 5.
  - (G29) Δ_L ≥ (3g²/a)(1+√(1−64/(3g⁴))).
  - This is Corollary 4.5(a) word for word, since (3/2)κ = 3g²/a.
- **Order 2, single norm** (R7–R10). With a₁ = 32, a₂ = 236 and P₂(ξ) = 1 − (256/3)ξ + (10720/9)ξ², the bound is Δ_L ≥ (3κ/2)(1+√P₂(ξ)) for g² ≥ √((32+√354)/3) ≈ 4.1156, "no dependence on L". The first pass reproduced a₂ = ‖v₂‖_loc = 236 exactly (`audit46_ym/check_ym01_second_order_OUTPUT.txt`).
- **Order 2 with a computed linear response** (L17–L20). The threshold is 3.825973… ("the new sufficient coupling threshold"), with the two-norm budget t(v) ≤ (16/3)x + (137/6)x² + w_*/6.

The first pass lists YM-06 as not checked (`46a` l. 312), and so does the reader's §6. The label "Generalised here" is defined as "under weaker hypotheses than the workbench states". For (a) that is false: the workbench states it with the same hypotheses. The front matter's credit to the audit for "the gap theorem at truncation order 2" is also a misattribution: the workbench has order-2 gap theorems, one of them (R10) with an input the first pass reproduced exactly.

**Corrected statement and status.**
- (a) is the workbench's YM-06 G26/G29, re-derived here from the audited fifth-reference core; its input is order 1, by hand.
- (b) sharpens YM-06's R10: the threshold falls from 4.1156 to 4.0187, and the endpoint constant rises from 3/2 to 1.52094. It does this by using F26's two-norm pair (m₂, t₂) = (5834/39, 137/6) instead of the single norm a₂ = 236. Its inputs are audited. *Generalised here* relative to R10.
- (c) is as stated.
- The front matter should read, for example: "the gap theorem at truncation orders 1–2 (the workbench's YM-06) re-derived from the audited core, with the order-2 threshold lowered to 4.0187".
- §4.3 should list YM-06's gap theorems among the workbench's results (located).

**Check** (`r23_ym.py`).
- 𝒟₁ = 1 − 256ξ/3 identically and (3/2)m₁ − 6t₁ = 0, so d₁ is exactly G26's d_phys.
- d₁ = 2.0744563 at g² = 5, matching G28's "> 2.07445".
- R10's α = 3/(4(32+√354)) = 0.0147595 gives threshold 4.115616.
- The source locators are quoted above.

### M4. Theorem 2.2(c): the rates and the uniformity are the workbench's (4.3)–(4.4), not a generalisation

**Location.** Theorem 2.2's status (p. 9); note `44_` §0 (row 44.2) and §14.

**What the text says.** The workbench's note "states (c) as the two limits, the second without the uniformity; the rates and the uniformity are Generalised here".

**What is wrong.**
- The history-law note (`editions/cumulative_20260916/latex/chapters/01_history_law_cutoff_20260914_RESEARCH_NOTE.tex`) says in §1, line 44: "All statements below are uniform in its location b".
- Its §4 gives "Explicit off-critical estimates":
  - (4.3): Δ ≤ N^{−ε} + N^{−ε²/(2 log 2)} for 1 ≤ m ≤ (½−ε)L_N and 0 < ε < ½, stated "for sufficiently large N";
  - (4.4): 1 − Δ ≤ ½N^{−ε} + exp(−2(εL_N/2 − ½)²/H), with H = ⌈(1+ε)L_N⌉, for m ≥ (½+ε)L_N and εL_N > 1.
- The first pass recorded both: `44a` l. 225, "Off-critical bounds (4.3)–(4.4) … both uniformly in b", and l. 232.
- The reader's first rate is a corollary of (4.3), because N^{−δ} ≤ N^{−δ²/(2 ln 2)}. Its explicit hypothesis δL ≥ 1, in place of the source's "for sufficiently large N", is the one part of (c) that goes beyond the source. Even that is small: the source's proof of (4.3) needs no largeness of N.
- The reader's second rate, 1−Δ ≤ 2N^{−δ²/(16 ln 2)}, is **weaker** than (4.4):
  - its exponent is δ²/(16 ln 2), against about δ²/(2(1+δ) ln 2) for (4.4); at δ = ½ that is 0.0225 against 0.120;
  - it needs 0 < δ ≤ ½ and δL ≥ 2, whereas (4.4) needs only δL > 1.

**Corrected status.** "(c) is the workbench's (4.3)–(4.4), audited, uniform in b as the note states. The forms here are simplified corollaries, and the second is weaker than (4.4)." Better, state (4.4) itself. The reader's proof of (c) remains correct.

**Check** (`r23_collatz.py`).
- On 764 (N, b, m, δ) cases, the reader's bounds and the workbench's (4.3)–(4.4) all hold against the exact Δ.
- The exponent comparison is printed for δ = 0.1, 0.25 and 0.5.
- The locator lines are in `src_cz_ch01.tex` (extracted source) at l. 44 and ll. 252–275.

### M5. Theorem 3.7: the M_n-form of the linear lower bound is already the workbench's, and stronger

**Location.** Theorem 3.7's status (p. 16); note `45_` §12 ("The M_n lower bound").

**What the text says.** "The last bound (Generalised here) improves the lower bound of Theorem 3.1, and Corollary 3.6 likewise".

**What is wrong.**
- The workbench's EP-03 note (`notes/ternary-variance-lower-bound.md` §6, "Distinctness-aware, integer-only finite bound"; also chapter 01 of the cumulative edition, ll. 218–219) states that every admissible N satisfies 2nN ≥ M_n + n(n−1) − 1.
- That is g₄(n) ≥ ⌈(M_n + n(n−1) − 1)/(2n)⌉, which is exactly the "Corollary 3.6 likewise" improvement.
- It is stronger than the reader's (M_n−1)/(2n).
- The reader audited this note ("the workbench's note, audited"), so the label *Generalised here* is wrong.
- The mathematical impact is small: a factor ≤ 1.264 in a bound that the variance bound beats for n ≥ 3.

**Corrected status.** "The workbench's note (§6) also gives g₄(n) ≥ ⌈(M_n + n(n−1) − 1)/(2n)⌉ (audited). This improves Theorem 3.1 and Corollary 3.6 by the factor (3/19^{1/3})^{n mod 3} ≤ 1.264, and the variance bound is stronger for every n ≥ 3."

**Proof of the workbench's bound.**
1. Theorem 3.7 gives |T(A)| ≥ M_n.
2. T(A) ⊆ [0, 2S(A)], and distinct elements give S(A) ≤ nN − n(n−1)/2.
3. So M_n ≤ 2nN − n(n−1) + 1. ∎

**Check.** `r23_ep817.py` confirms that "the variance bound exceeds (M_n−1)/(2n) exactly for n ≥ 3" (n ≤ 60). The workbench's own table in the same §6 (1, 3, 5, 11, 27, 49 for n ≤ 6) is the one `45_` §2 already quotes.

---

## MINOR findings

**m1. Thm 1.1(c) (p. 4): the halved range works for every odd prime.**
- The text restricts "p/4 < a < p/2" to p ≡ 1 (mod 4).
- For p ≡ 3 (mod 4), the shell a = (p+1)/4 lies in (p/4, p/2), has R = 1 and is occupied (u = a ∈ M_a).
- Combined with (a), the equation is solvable at an odd prime p iff some shell with p/4 < a < p/2 is occupied.
- Check (`r23_es.py`): all 429 odd primes below 3000, and all primes p ≡ 3 (mod 4) below 20,000.

**m2. Thm 2.2(a) (p. 9): the sandwich holds for every H ≥ 0.**
- For H < m we have Q_m(H) = 1 and binom(H, m) = 0. The lower bound 1 − N2^{−H−1} ≤ Δ holds because every word has G-mass ≤ 2^{−m} ≤ 2^{−H−1}.
- The workbench's (3.2) is stated "for all N, b, m, H" and adds "This also handles H<m".
- With this, the proof of (c) can take H = ⌈(1+δ)L⌉ directly, without the max{m, ·}.
- Check: 3,000 (N, b, m, H) cases with H from 0 to 39 against the exact Δ (`r23_collatz.py`).

**m3. Thm 3.8 status (p. 17): Λ₃ = 3 needs no citation, and the workbench states it.**
- Lemma 3.2's argument with three terms shows that a 3-admissible set has no relation with coefficients in [−2, 2]:
  - X₀ = P₁+N₂, X₁ = P₁+P₂, X₂ = N₁+N₂ is a 3-term progression with step P₂−N₂, so P₂ = N₂ and P₁ = N₁;
  - a nonzero ±1 layer then gives the progression 0, P₁, 2P₁.
- So all 3ⁿ ternary sums are distinct, T(A) ⊆ [0, 2nN], and g₃(n) ≥ (3ⁿ−1)/(2n). By the variance argument, g₃(n) ≥ √((9ⁿ−1)/(8n)). Hence Λ₃ ≥ 3, proved here with no external input.
- The workbench's own located chapters say the same:
  - ch. 22, l. 681: "Three-admissibility makes H_3(A) injective on its 3^n words";
  - ch. 24, l. 631: "ρ = 3 = λ_3".
- Suggested status: "Proved here (the workbench's located chs. 22 and 24 state it)".
- Check (`r23_ep817.py`): |T(A)| = 3ⁿ on all 1,822 3-admissible sets searched. g₃(1..5) = 1, 3, 8, 22, 60 by search, against lower bounds 1, 2, 5, 10, 25 and 1, 3, 6, 15, 39.

**m4. Prop. 3.5 status (p. 16): (c) does not rest on the exhaustive searches.**
- "(c) rests also on the computed values of Proposition 3.11" is over-cautious.
- (c) uses only the upper bounds g₄(5) ≤ 40, g₄(6) ≤ 79 and g₄(7) ≤ 246. These follow from explicit admissible sets, for example {1,13,35,39,40}, {2,29,45,74,77,79} and {1,3,39,180,219,243,246}. Their admissibility is a finite check (`r23_ep817.py`).

**m5. §5 certificate table (p. 29): number of searches.**
- The table has "three independent programs (n ≤ 6)".
- Prop. 3.11's status (p. 18) and Appendix A count a fourth search, the referee's.

**m6. Front matter "Who did what" (p. 2): credit for the range x < p/2.**
- It lists "the range x < p/2 of the Erdős–Straus shell criterion" among the audit's contributions.
- The workbench's item 22 already has every witness's least denominator in (p/4, p/2) at p ≡ 1 (mod 12) (`43a` §2.22, l. 360).
- Thm 1.1's status acknowledges this; the front matter should say "extended to every odd prime".

**m7. Prop. 3.10 status (pp. 17–18): EP-05 Thm 3.1 is more general than the first sentence (old passage).**
- The status reads "Generalised here (the workbench's EP-05 Theorem 3.1 and its corollary …)".
- EP-05 Theorem 3.1 (cumulative ch. 08, l. 127) allows vectors c^h ∈ {−1,0,1}^E with pairwise disjoint supports and a common nonzero observed boundary.
- The proposition's first sentence (disjoint subsets with equal sums) is its special case c^h ∈ {0,1}^E. Only the ruler corollary (2m−3 distinct distances instead of binom(m,2)) is generalised.

**m8. 2^33 verification (p. 12): the "Computed" label.**
- The label requires programs "run independently of each other", but only `descent_2e33.c` is named.
- Two independent programs confirm the verification:
  - referee 22's `r5_descent.c`;
  - this pass's `r23_descent.c` (odd-to-odd map, 24 s on two cores).
- Mine also reproduces the published path record: n = 8,528,817,511 reaches 18,144,594,937,356,598,024 under 3x+1. Its half, 9,072,297,468,678,299,012, is exactly the reader's "largest value met 9.07·10^18".
- Naming a second program would make the label match its definition.

**m9. Prop. 2.5 (p. 11), optional: an exact per-member statement.**
- Since T^m(n) = (3^m n + C)/2^A with C ≥ 1, a member n satisfies T^m(n) < n iff D > 0 and n > C/D (D = 2^A − 3^m ≠ 0).
- So the descending members are exactly those above C/D. The proposition's "all members iff F_m(n₀) < n₀" is the case n = n₀.

---

## New or changed passages verified and found correct

Each passage below was checked against its proof, step by step, and against my own recomputation. Where a finding above concerns only the status or the attribution, the mathematics was still checked and is correct.

**§1 Erdős–Straus**
- **Thm 1.1** (p. 4): statement, range x < p/2 with its exception, (b) for every a > p/4 with p ∤ a, and the proof of (a). Each step was re-derived: y < p; p | z; 4z′−1 = pk; (4kx−N)(4ky−N) = N²; 4kx−N ≥ N+2(k−1). The (b) swap argument gives y = z iff R = 1.
  - Checks: 11,803 solutions at all odd primes < 1500 (2,259 below 400, as stated); 4,726 and 4,303 (p, a) pairs; 29 fixed points; 4,398 shells; the solution enumerator cross-checked against a plain y-loop for p < 120.
  - The largest x/p over non-exceptional solutions is 0.4877 (p = 1013, x = 494). So the constant ½ cannot be lowered.
- **Paragraph after Prop. 1.3:** correct for Prop. 1.3 and for the occupancy half of Prop. 1.2 (M1 concerns the rest).
- **Prop. 1.4:**
  - Proof: re-derived.
  - Checks: the characterisation at all primes p ≡ 1 (mod 12) below 2·10⁵; 989 survivors below 10⁶, the first 1129, 1201, 2521; classes {1, 25, 121} (mod 168).
- **Prop. 1.5:** the identity and integrality were re-derived. The leftover classes are exactly the six unit squares mod 840; the families hold at all 2,437 covered primes below 3·10⁵.
- **Item 26 status:** matches `43a` §2.26. The identity 16(4q³+1) − (4q+1)(16q²−4q+1) = 15 holds; 67369 is prime and ≡ 1 (mod 24); 16849 = 7·29·83 (R = 27); the first occupied shell is 16850 (R = 31), with E = {674, 84250}.
- **Item 3's Pocklington chain:** re-proved with my own implementation.
  - Every factorisation is exact, and the leaves are prime by trial division.
  - Least witnesses (largest 11):
    - q₂: {2:3, 3:2, 17:2, 5051:2, 169307:2};
    - q₁: {2:3, 3:2, 5:3, 351707:2, q₂:2};
    - p: {2:11, 3:3, 5:2, q₁:2}.

**§2 Collatz**
- **Prop. 2.1:** the count formula, floor/ceil, and |P(w) − 2^{−A}| ≤ (1−2^{−A})/N. The cylinder property holds for all words with A ≤ 11.
- **Thm 2.2(c):** statement and proof correct. Every Hoeffding step was checked: u ≥ δL/2; binom(H,m)/N ≤ Pr(X ≤ m); H ≤ 2L; the final inequality. M4 concerns only the status.
- **Prop. 2.5:** proof and converse correct. The example (1,1,1,1,4) gives F₅(3) = 235/64, n₀ = 95 and F₅(95) = 91; the count of 637 words is Σ_{m≤5} binom(10, m).
- **Tail-bound paragraph:** matches the source's (7.9)–(7.15), including t_H = (t_{H−1}+S_H)/2 and K(2ρ−1) = C₀ρ. Checked √2(√15/4)^{h−1} ≤ (3/2)(31/32)^h for h < 2000.
- **Thm 2.8:** exact integer arithmetic gives the least m = 1636, A = 2593 and k ≥ 679. The workbench's (C36)–(C38) contain the same m and A.
- **2^33 paragraph:** independently verified (m8); the least-denominator fraction for s = 2^33+1 is 301994/190537, with k ≥ 79,079.99999 → 79,080.
- **Cor. 2.9 (numbers and proof):**
  - The previous best upper approximation is 10439860591/6586818670.
  - s_lo = 2.1689015534053·10²⁰ (2^67.555526) and s_hi = 4.3584872·10²¹ (2^71.884317).
  - 72057431991·log₂3 = 114208327603.999999999992.
  - 72057431991·(2 − 10439860591/6586818670) lies strictly between 29906536377 and 29906536378, so k ≥ 29,906,536,378.
  - At 2^40 the fraction is 17087915/10781274 (Eliahou).
- **Cor. 2.9 (citations):**
  - Barina 2021 (Crossref): *J. Supercomput.* 77(3), 2681–2688, doi:10.1007/s11227-020-03368-x, online 1 July 2020.
  - Barina 2025: 81(7), article 810.
  - The 2025 paper's §1 says "all starting values up to 2^68 were computer-checked [4]", with [4] = Barina 2021. Its Table 10 dates 2^68 to 2020-05-07.
- **Thm 2.10**, "at no interior point": correct. The Lagrange-interpolation identity Σh_w r_w^i = 0 for i ≤ K−2 holds; for K ≥ 3 vertices are determined, so "interior" is the right scope.
- **Tao-clock sentence:** matches the source (`consequences.tex`, Cor. "Coherent first-entry limits": rate L_c(log t_j)^{−c} for 1 ≤ x ≤ t_j, with L_c = B′/(1−α^{−c})).

**§3 Erdős 817**
- **Prop. 3.5 (a)–(d):** proof correct and new (no base-19 lifting in the workbench).
  - The digit sets {1,7,8} and {2,3,5} are the only ones.
  - 396 lifted sets with random admissible tops are 4-admissible, and a non-admissible top fails.
  - The constants 0.2188, 0.2554 and 0.2957 are rounded up, as "at most" requires; the reader's 0.421, 3.00 and 1.12 are correct.
  - (b) was checked for n ≤ 12.
  - (d): A♯ ∪ 1651·B is 6-admissible for random B, and A♯∖{257} (max 253 < 257) shows that (d) is strictly sharper when 10 ∤ n.
  - The certificates (97, B*), (93, B*) and (1651, A♯) exclude progressions for every nonzero step, including the two steps of order 3 modulo 93 that give repeated terms.
- **Thm 3.7:** the (M_n−1)/(2n) bound and "the variance bound is stronger for every n ≥ 3" are correct (M5 concerns the label).
- **Λ₃ = 3 sentence:** correct (m3 concerns the status).

**§4 Yang–Mills** (from the F26 rationals transcribed from the source)
- **Thm 4.1 added statements:** α₅ = 0.01842495357611761668188… (the reader's digits are a correct truncation); threshold 3.6835519839857273; d₅(1/64) = 1.9068301567; d₅(α₅) = 1.5453056; d₅(0) = 3; d₅(4/225) = 1.6993492. The "Equivalently" Poincaré form is the variational characterisation.
- **Lemma 4.2:** girth form and circulation proof re-derived step by step:
  - Gale's feasibility (a column set of size ≥ 2 is served by all rows);
  - dart circulation conservation;
  - decomposition into closed walks with cyclically distinct consecutive links;
  - a closed walk without immediate repetition contains a cycle, via the farthest-vertex argument in a tree;
  - piece lengths ≥ g−1, hence |C| ≥ g·n_e(C).
  - LP check with real weights: the minimum over links equals the girth on 14 graphs, among them Q₄, Petersen, Heawood, the box, a multigraph (girth 2) and six random graphs.
- **Cor. 4.5 (mathematics):**
  - The residual identity and the argument that ℓ_N < 1 are correct.
  - The identity w_*′√𝒟 = δ′ + ℓ′w_* holds symbolically for N = 1…5, and d_N is decreasing on a 401-point grid.
  - All stated values reproduce:
    - N = 1: 2.0745, 2.8304 and the threshold 8/√3;
    - N = 2: α₂ = 0.0154800849822, 4.0186791538833, 1.52094, 1.7665, 2.3033;
    - N = 4: α₄, 3.7159603625, 1.898118, 1.658436.
  - All linear coefficients (3/2)m_i − 6t_i are ≥ 0, so d_N ≥ 3/2 for every N, as the source's F35 says.
- **YM-05 and YM-02 bullets:** correct. 4/225 < α₄; ξ = 4/225 ⟺ g² = 15/4; 1/25000 is in the workbench README. The parity step was checked: an all-(−1) plaquette cochain is a coboundary on the box.
- **Prop. 4.6 and the paragraph after it:** correct and consistent with the source's (FC1)–(FC8).
  - M_L = 12L²(2L+1) by enumeration for L = 2…5.
  - The radii are 1/1280 and 1/320, and 1/α₅ = 54.27.
  - The contour-optimality argument (winding numbers; max(1/x, 1/(c−x)) ≥ 2/c) is correct.

**§5, §6, Appendix A and front matter.** Consistent with the notes and with each other, except for M1–M3 and m5–m6. The re-run claims in Appendix A reproduce: 47/47 pass, and G1–G26 are identical in about 18 s.

---

## Scripts and results (all in `scratchpad/referee23/`)

| File | What it checks | Result |
|---|---|---|
| `r23_es.py` → `r23_es_OUTPUT.txt` | Theorem 1.1 (a)–(c) by independent enumeration; Prop. 1.2 at p ≡ 1 and p ≡ 5 (mod 12); corrected form; Props 1.3–1.5; item 26 data; Pocklington chain (own implementation) | All pass except the intended failure: Prop. 1.2 fails at 819/819 primes p ≡ 5 (mod 12) (M1). 13 s. |
| `r23_collatz.py` → `r23_collatz_OUTPUT.txt` | Continued fraction and upper best approximations of log₂3 (120 digits); Thm 2.8 exactly; 2^33 consequence; Cor. 2.9 constants; Prop. 2.1; Thm 2.2(a) for all H; reader's and workbench's (c) bounds on exact Δ; Prop. 2.5 example; tail constants | All pass. 3 s. |
| `r23_descent.c` → `r23_descent_OUTPUT.txt` | Every odd 3 ≤ n < 2^33 falls below itself (odd-to-odd map, 128-bit); peak value | Pass; peak 18,144,594,937,356,598,024 at n = 8,528,817,511 (published path record); 24 s on two cores. |
| `r23_hercher.py` → `r23_hercher_OUTPUT.txt` | Bounds from Hercher (2023) + Barina (2025); needed verification ranges | m ≥ 137,528,045,312; A ≥ 217,976,794,617; A+m ≥ 355,504,839,929; k ≥ 57,079,296,007; ranges 2^70.585 and 2^71.884 (M2). |
| `r23_ep817.py` → `r23_ep817_OUTPUT.txt` | Digit sets mod 19; lifting with random tops; (b), (c) constants and explicit sets; certificates with small-order steps; (d); Λ₃ via distinct ternary sums; variance vs linear bound | All pass. 66 s. |
| `r23_ym.py` → `r23_ym_OUTPUT.txt` | α_N, thresholds, d_N (N = 1…5) from the F26 rationals; closed form N = 1; monotonicity (symbolic and grid); sensitivity; M_L; Neumann radii; girth lemma by LP on 14 graphs | All pass (after fixing my own over-strict string test on α₅'s last digit). 36 s. |
| `r23_item26.py` → `r23_item26_OUTPUT.txt` | First occupied shell at p = 67369 | a = 16850, R = 31, E = {674, 84250}. |
| `rerun_generality_checks.txt`, `rerun_claims_checks.txt` | Author's scripts re-run from this folder | Identical output; 47/47 pass. |
| Evidence files | `hercher_abs.html` (arXiv page); `crossref_*.json`; `barina2025.pdf/.txt` (CC-BY); `src_cz_ch01.tex`, `src_cz_ch02.tex`, `src_ym_cumulative.md`, `src_ym_web_continuation_0916.md` (extracted workbench sources) | Locators quoted above. |
