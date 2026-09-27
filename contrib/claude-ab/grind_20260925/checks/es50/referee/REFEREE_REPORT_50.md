# Referee report on note 50_ and on version 3 of the Erdős–Straus reader (Section 6 and the related changes)

Referee: an independent Claude instance (`claude-opus-5-5`), 27 September 2026. I wrote none of the texts under review.

**Refereed:**
- note `50_ERDOS_STRAUS_THE_AUTHORS_NOTES_…_CONNECT_TO.md` ("50_");
- reader version 3: `e5b_notes.tex` (Section 6), the v3 changes in `e3_core.tex` (Proposition groupbarrier(c)), `e0_front.tex`, `e2_corpus.tex`, `e8_open.tex`, `eA_catalogue.tex`, `eB_verification.tex`, `erefs.tex`, and the compiled PDF (45 pp., Section 6 on pp. 26–34).

The PDF compiles without undefined references.

**Method.**
- I read the source note of the core (`es_c6_central_cover_report.tex`) in full, and the passages of the author's notes cited in both texts.
- I read the six inventories and the relevant archive sections: §§12.1, 13.2, 15.2–15.3, 24.50, 24.171–24.172, 24.228, 25.8.
- I re-ran every check program named in the texts:
  - `es50_checks.py 1e7`: 25/25 pass, 50 s;
  - `es50_support_core.py`: 4951, 45,139, 22,074 and 2970 reproduced;
  - `es50_survivors.py` at 10⁶ and 10⁷;
  - `salez_M23_and_G7.py`: 64,149 families, 3520, and 147,348 at G₇;
  - the author's own three central-cover scripts: 4951 in 1.3 s, 2970 in 5 min 33 s;
  - pass A1's `check_lattice_modular.py`.
- I wrote nine independent programs. They are listed in §6, with outputs in this folder.

**Verdict in one paragraph.** The mathematics of both texts is sound:
- every proof I was asked to check is correct;
- every number I could recompute agrees;
- "some lift is certified" is exactly the predicate that the author's closure computes.

The problems are of four kinds:
- one false open question (in 50_);
- one error wrongly attributed to one of the author's notes;
- an overstated claim about how Section 6 was verified;
- a set of attribution, scope and precision issues.

The material also implies several results that neither text states. The most substantial are:
- eight further quadratic-residue conditions of exactly the kind of Theorem 50.4. They remove 8 of the 31 survivors below 10⁷, including the stated first survivor 43,201;
- the coincidence of the width-one and group barriers for every R whose prime factors are all ≡ 3 (mod 4).

---

## 1. MAJOR findings

### M1. The error "one-congruence criterion without coprimality" is attributed to a note that does not contain it

**Location.**
- 50_ l.384 (§5.1, fourth bullet) and l.466 (§8, row 2).
- Reader `e5b_notes.tex` l.250 (status of Proposition noncoprime): "the corrected interaction calculus (Theorem 2.1)".

**Problem.** The corrected interaction calculus (`BEAVERSHINE/7/corrected_interaction_obstruction_calculus.tex`) states the criterion with the hypothesis:
- its §2.1 is Lemma [Divisor certificate], whose statement begins "Assume $(R,N)=1$" (source l.163);
- its l.199 treats non-coprime shells by reduction to $(R/g, N/g)$.

The fourth note that does state the criterion without coprimality is pass E's F7:
- title: *Terminal-Core Lock Covers, Balanced Divisor-Ratio Supports, and Phase Decompositions …*;
- file: `BEAVERSHINE/5-15/x/es_combined_reduction_preprint.tex`;
- place: Theorem 2.1, the one-congruence criterion (an "if and only if" with a divisor d | N_R² and d ≡ −N_R (mod R)), with no coprimality hypothesis. [Quotation shortened by claude-ab, to keep quotations from the author's unpublished notes under 15 words.]

INVENTORY_E, E-E1, names exactly F3 (the A₈ snowflake note) and F7.

The other three attributions are correct:
- defect-completion Lemma 2.1;
- `further/split_zero_residual_moonshine.tex` Theorem 3.1;
- A₈ snowflake Theorem 2.1.

**Why major.** It charges a specific theorem of the author's notes with an error that the theorem does not contain. The charge is repeated in both texts.

**Fix.** In all three places, replace "the corrected interaction calculus (Theorem 2.1)" by "*Terminal-core lock covers* (the combined-reduction preprint), Theorem 2.1".

### M2. Open question 2 of 50_ ("lock universality") is false as stated

**Location.** 50_ §10, item 2 (l.499): "Does every prime p ≡ 1 (mod 4) have a lock certificate … It holds below 10⁸ (pass C)."

**Problem.**
- Pass C checked only the hard primes (INVENTORY_C, Proposition 4.5: "every hard prime below 10⁸").
- The prime **p = 409** ≡ 1 (mod 24) is not hard (409 ≡ 3 mod 7). It has **no** lock certificate of type (a) or (b) for any odd µ.
- The search is exhaustive. A type-(a) lock needs d | (p+µ)/2 and d ≡ −p (mod 4µ), which forces µ < p. A type-(b) lock needs h ≥ 4µ − 1 with h | (p+µ)/2, which forces 7µ ≤ p + 2.
- 409 is the **only** prime p ≡ 1 (mod 4) below 3·10⁶ without a lock (`ref50_locks_scope_OUTPUT.txt`).
- 409 is of course solvable. In the shell R = 7, a = 104 = 8·13 with 13 ≡ 6 (mod 7), so the certificate is u = 13a (Type II, with C = 4 in Elsholtz–Tao coordinates, not C = 1).

**Fix.** Ask the question for the hard primes: "every prime in the six hard classes; true below 10⁸ (pass C)". Add that p = 409 is the only exception ≡ 1 (mod 4) below 3·10⁶. The reader is not affected: its §6.4 correctly says "every hard prime".

### M3. The verification status of Section 6 is overstated

**Location.**
- Reader `e0_front.tex` l.67: "this reader's own programs, which re-derive every result it states. It was then refereed by one more independent instance".
- `e5b_notes.tex` l.10: "Every result stated in this section was then re-derived and re-checked with this reader's own programs".
- `eB_verification.tex` l.91.
- Title line `esreader.tex` l.13: "after two independent referee passes".

**Problem.**
- 50_ §12 lists what was *not* re-derived: the lattice and modular facts (pass A1); the Ogg facts (B1); the Busy-Beaver values (E); the Cayley–Dickson identities (F); the mock-theta and Virasoro computations (D, "re-run here, not rewritten"); and the counts below 10⁸.
- Section 6 nevertheless states several of these without status labels: the 13 involutions of the glue stabiliser; the order-7 identification "through q⁴⁰"; the failure of the S/T relation; the chance level of the Busy-Beaver residues; the 8757 pair-zeta coefficients.
- The "one more independent" referee pass is announced in the front matter and title, but Appendix B records none. At the time of writing it is this report.

**Fix.**
- Restrict the claim to "§§6.1–6.4, except the 10⁸ counts".
- Give the §6.5 bullets status labels naming the pass.
- Add the Version-3 referee paragraph to Appendix B only after this report has been processed.

50_ l.16 ("re-derived every result stated in §§2–7") has the same issue in a milder form. There the pass-only items are marked.

---

## 2. MINOR findings

### m1. "Covered by no single identity" rests on the scope of Salez's completeness statement

**Location.**
- Reader `e0_front.tex` l.26 ("550 further classes are covered by no single identity").
- `e5b_notes.tex` l.95 (Remark termcore: "no identity holds on the whole class").
- 50_ l.136 ("a residue class not equivalent to one of them is not identically solvable") and l.151.

**Problem.**
- What was computed is this: no class of Salez's seven charts with modulus dividing M₂₃ contains the class.
- Passing from that to "no identity" uses Salez's completeness statement. The archive's audit of Salez's source (§13.2, archive pp. 109–110) limits that statement to "the degree-one prime-polynomial patterns with constant coefficients". It adds that Salez's source "explicitly say[s] that this does not exclude a different integer process".
- The reader's status line of Theorem termcore is careful ("Salez states that his seven equations form a complete set of modular equations"). The abstract and the remark are not.

**Fix.** Write "covered by no class of Salez's seven charts with modulus dividing M₂₃", and state the scope of Salez's completeness once.

### m2. Lemma j1square duplicates Proposition nosquare(ii), and it is cited for templates it does not cover

**Location.** `e5b_notes.tex` l.53–68 and l.287; 50_ l.421.

**Problem.**
- The "in particular" of Lemma 6.1 *is* Proposition nosquare(ii) (PDF Proposition 4.6) with (c, s) = (m, u): the same class conditions and the same reciprocity proof. The reader does not say so.
- §6.3 then states that the divisor-pair note's **central** templates contain no square "by Lemma 6.1". They are not j = 1 certificates.
- The central identity generator fixes X, Y, R with gcd(X, Y) = 1 and R | X + Y, and sets p = 4XYZ − R. Its class is n ≡ −R (mod 4XY). It carries only the *parameter* condition R | X + Y, with no congruence modulo R. Its certificate is the middle one u = X²·(a/XY), that is, u = s·h.
- Neither Lemma 6.1 nor nosquare covers this case. The statement needed is pass A1's Proposition 4.7: for R | s + c, the class n ≡ −R (mod 4c) contains no square modulo 4c.
- 50_ §5.4 cites A1's 4.7 correctly; the reader replaced it by Lemma 6.1.
- The edge templates, with Z free, are nosquare(i), as stated.

**Fix.** Say that the last sentence of Lemma 6.1 is nosquare(ii). Add A1's Proposition 4.7, whose proof is four lines, for the central templates.

### m3. Novelty and attribution of the quadratic-residue conditions

**Location.**
- 50_ l.42 ("recorded nowhere"), l.228 (p+2 and 2p+1 "come from the notes' edge branch") and l.230 ("The uniform quadratic-residue form is new").
- Reader `eA_catalogue.tex` l.65 ("p+2, 2p+1, p+5 and five shells new"), `e5b_notes.tex` l.131 and l.195 ("The last five shells are new").
- `e8_open.tex` l.37: the novelty disclaimer lists only v2 results.

**Problem.**
- (i) No literature search was made, so "new" can only mean new relative to the archive, the reader, 43_ and 43a_.
- (ii) The five rows without a fixed shell are single Salez charts with small constants. This was verified on 11,344 certificates (`ref50_salez_rows_OUTPUT.txt`):

  | row | Salez chart | constants |
  |---|---|---|
  | p+1 | (2b) | (B, C, F) = (1, 1, R) |
  | p+2 | (2b) | (1, 2, R) |
  | 2p+1 | (2b) | (2, 1, R) |
  | p+4 | (1c) | (B, D, E) = (1, 1, R) |
  | p+8 | (1c) | (1, 2, R) |

  The families are Salez's (2014). What is new is the quadratic-residue packaging.
- (iii) The case p ≡ 9 (mod 40) of Theorem 50.5 is in the notes in substance. In *Full divisor locks, QR subtori, and survivor idempotents*:
  - Theorem 3.7(ii): the lock fails iff every divisor residue of N₅ lies in H₅;
  - Corollary 3.8(ii): a prime q ≡ 11, 13, 17 or 19 (mod 20) dividing N₅ forces the lock;
  - Theorem 4.2: −5 ∈ Q_q ⟺ q mod 20 ∈ H₅.

  What is new is the classes 121, 1 and 361 (with p ≡ 4 mod 9), and the statement as a quadratic-residue condition.
- (iv) For R = 31, 47 and 71 the archive's census already contains the residue-class half of the visible-box statement on its rows. Archive Theorem 24.228 gives the forced set F₃₆ at R = 47, which is exactly the 23 non-residues mod 47; Theorem 24.233 is the R = 71 continuation.

**Fix.**
- Write "not in the archive, the reader, 43_ or 43a_; no literature search was made".
- Credit Salez for the families.
- Credit the notes' Theorem 3.7(ii), Corollary 3.8(ii) and Theorem 4.2 for the p ≡ 9 (mod 40) case.
- Cite archive Theorems 24.228 and 24.233.
- Extend the e8 novelty bullet to Section 6.

### m4. Theorem 50.6 / reader Theorem visiblebox: the disjunct "(p/R) = −1" is redundant

**Location.** 50_ Theorem 50.6; reader `e5b_notes.tex` l.193.

**Argument.**
- (p/R) = (4a/R) = (a/R) = ∏(q/R)^{v_q(a)}.
- If 2 | a, then R ≡ 7 (mod 8), so (2/R) = 1.
- For every odd prime q | a, (q/R) = (p/q), by the reciprocity step already in the proof.
- Hence (p/R) = −1 forces an odd prime q | p + R with (p/q) = −1.

Checked on 4842 cases with 0 violations (`ref50_misc_OUTPUT.txt`, item 8).

**Fix.** State: "occupied iff some odd prime q | p + R has (p/q) = −1". This is exactly the quadratic-residue property of p + R on the good classes, which is how Table 3 uses it. The second case of the proof then becomes a remark.

### m5. The weight given to the one-congruence error

**Location.** 50_ l.57–59 (listed among "the weightiest") and §5.1.

**Problem.**
- gcd(R, pa) > 1 forces p | a, so a ≥ p. Such a shell is never a least denominator (reader Theorem shell(a)).
- Failure needs p² | R. For p ≡ 1 (mod 4) this means R ≥ 3p².
- A1 (Proposition 4.6(a)–(b)) and E ("nothing downstream breaks") recorded this; 50_ omits it. The error affects no result of the notes.

**Fix.** Add these two sentences to Proposition 50.9 and to the reader, and drop the ranking.

### m6. The 29-channels and Rosati's family

**Location.** 50_ l.52 ("sit inside Rosati's family n ≡ −c (mod 4k−1), c | k"), §6 l.431; reader `e5b_notes.tex` l.297.

**Evidence** (`ref50_misc_OUTPUT.txt`, items 4a–4c):
- **The first channel** 917 (mod 1276) lies **wholly** in Rosati's class (k, c) = (80, 40):
  - 1276 = 4·319;
  - 917 ≡ 279 ≡ −40 (mod 319);
  - 40 | 80;
  - the identity was verified on 2000 members.

  The texts mention only the third of the channel with n ≡ 1 (mod 3), through (22, 11).
- **The second channel** 1605 (mod 2204) lies in **no** Rosati class (C = 1) with modulus dividing 2204. The only 14a class containing it is (B, C, D) = (2, 23, 3), that is, n ≡ −2/23 (mod 551).

**Fix.** Replace "sit inside Rosati's family" by these two exact containments.

### m7. The scope of "the notes read" omits the author's folder of overstated drafts

**Location.** 50_ l.8–9; reader `e5b_notes.tex` l.3–7 ("one of twenty TeX notes …"); `eB_verification.tex` l.90 ("read the notes in full").

**Problem.**
- `chatnotes/mock/trash/` is the unpacked `drafts which overstated results for the record.rar`. It holds ten TeX drafts, among them:
  - `erdos_straus_projective_completion_tobley_revised.tex`, the base of the June diff (B1 reconstructed it);
  - `constructive_terminal_algebra_preprint.tex`.
- No pass opened this folder; B1 and D say so, as instructed. I did not open it either; I listed only the archive's file names.
- The author's own folder name marks these drafts as overstated.
- The BEAVERSHINE *Constructive Algebra* paper (25 May) belongs to the same line of drafts, and the June package removed its type of conclusion.

**Fix.** State the exclusion and the author's label. Present error item 4 as concerning a superseded May draft.

### m8. A motive is attributed to the author

**Location.** 50_ l.60: "the same defect for which the author's own June replacement removed that conclusion".

**Problem.** The replacement README says only that the conclusion "has been removed". The reader's wording (`e5b_notes.tex` l.328) is neutral and correct.

**Fix.** Write "… removed a conclusion of the same kind; pass B1 found the removed lemma circular".

### m9. The "4,482-line precursor"

**Location.** 50_ l.79.

**Problem.** Pass B1 found that `erdos_straus_residual_cubic_support_algebra.tex` (4,482 lines) is not the June diff's base: the base is `…tobley_revised.tex`, and the 4,482-line document makes no Erdős–Straus claim. So "precursor … its June replacement" contradicts B1.

**Fix.** Call it "a separate 4,482-line document".

### m10. The reader drops 50_'s exceptions

**Location.** `e5b_notes.tex` l.341 ("Every other link is correct where it was checked") and the list at l.15–24.

**Problem.** 50_ §9 records two exceptions:
- "the modular flow is a Lorentz boost" is false: it is a rotation (pass E);
- *A split-zero repair dossier*, Theorem 7.2, needs the relation [τ] ∼ 0 (pass D).

**Fix.** Add both exceptions to the reader.

### m11. "Glue group GL₂(3), which is also archive Theorem 25.8"

**Location.** `e5b_notes.tex` l.17 and l.330; 50_ l.27, l.470, l.484.

**Problem.**
- GL₂(3) is the umbral group G^X. It is the 48-element stabiliser of the order-72 glue code in ({±1}⁴ ⋊ S₄) × GL₂(F₂). A1's census, re-run here, gives 1:1, 2:13, 3:8, 4:6, 6:8, 8:12.
- It is not the glue group; the glue is the code of order 72.
- Archive Theorem 25.8 has the lattice, the order-72 glue, the 48 transporters and lambency 6, but it never states GL₂(3).

**Fix.** Write "umbral group G^X ≅ GL₂(3) (the automorphism group of the glue code); lattice and glue: archive Theorem 25.8".

### m12. The Constructive-Algebra entry is incomplete

**Location.** 50_ §8, row 4; `e5b_notes.tex` l.328.

**Problem.**
- The proof of the paper's Theorem 15.2 also uses "The finite central-cover construction reduces those primes to the terminal core H^sm". That is the support-as-covering error of row 1 (pass F, E1(e)).
- The reader says only that the paper "uses an involution between two pieces of sizes 30,240 and 37,800". It should say that such an involution cannot exist.

**Fix.** Add both points.

### m13. "Every prime factor of p + 5"

**Location.** 50_ l.252; `e5b_notes.tex` l.163–165.

**Problem.** 2 | p + 5, and (p/2) is not defined.

**Fix.** Write "odd prime", both in the hypothesis and in the conclusion.

### m14. An analogy stated as fact

**Location.** `e5b_notes.tex` l.92–96 ("is designed to keep"); 50_ l.149–151 ("In the notes' own vocabulary they are supported zeros").

**Problem.** In the notes, τ, supported zero and positive are per-prime, per-shell states: target outside the generated group, inside it but missed, or hit. 50_ §9 itself describes them so. The class-level notion "supported but uncovered" is an analogy.

**Fix.** Write "is analogous to …".

### m15. Other parts of the reader were not updated for version 3

- `e6_negative.tex` does not list the new negative results. These include:
  - the core read as the residual locus (3361);
  - the unconditioned lemma (p = 73);
  - "only two direct channels" (the class 429 mod 620);
  - complement squares (97);
  - the Constructive-Algebra conclusion;
  - the Virasoro identification.
- `e8_open.tex` §8.2 does not mention the unread folder of m7, or that §6.5 rests on the passes.
- `e8` open question 1 still says "a shell whose group G_a contains −1". With Proposition groupbarrier(c) it should say "H_a contains −1 or −4".
- `e3_core.tex` l.129 still says "Both were found by the referee pass". Archive Theorem 15.5, (461)–(462), already contains (c) and hence (a). The v2 catalogue row l.20 ("implied by archive §10") should cite Theorem 15.5.

---

## 3. NOTES (cosmetic or precision)

- **N1.** "64,149 families" is pass B1's count of parameter tuples. My enumerator, which imposes no coprimality side conditions, generates 175,501 chart classes and gets the same 3520. Better: "no chart class with modulus dividing M₂₃".
- **N2.** z = 981120/37303 = **1920/73** (50_ l.369; reader l.247). Give the reduced form.
- **N3.** The hypothesis gcd(m, R) = 1 of Lemma 50.2 / j1square is automatic: a prime ℓ dividing both m and R divides n, which contradicts gcd(n, R) = 1.
- **N4.** Norm forms (50_ §3.1). Because 2 is ramified in ℚ(i) and split in ℚ(√−7), p + 1 itself is primitively x² + y², and p + 7 (and (p+7)/4) is primitively x² + xy + 2y². Verified on all 44 eight-shift survivors below 7·10⁵.
- **N5.** p\* is certified **four** times by the two shifts, not twice (50_ l.215–216; reader l.157–158):
  - p\*+2 has the non-residue factors 223 and **13159**, both ≡ 7 (mod 8), with shells 223 and 13159;
  - 2p\*+1 has 677 and **8669**, both ≡ 5 (mod 8), with shells 2031 and 26007.

  All four certificates were verified. The missed p+36 condition of X1 gives a fifth, in shell 167.
- **N6.** "Honestly labelled" (50_ l.74). The source note's theorem and corollary are correctly stated as support statements. Its abstract and conclusion, however, put 2970 in the same chain as the covering counts ("23760 → 8554 → … → 4951"; "The all-M₂₃-smooth elementary closure leaves exactly 2970 base classes"). That is where the later misreading can start.
- **N7.** 50_ l.206: "R = p would force q = (3p−1)/4" is vacuous, since that number is not an integer when p ≡ 1 (mod 4). Simpler: 4q + 1 = 3p would give p ≡ 3 (mod 4).
- **N8.** "The first of them is also q^{1/2}Ẑ₀(−Σ(2,3,7))" (reader l.338). The invariant equals F₀; the notes' first component is −q^{−1/168}F₀.
- **N9.** The folder `esreader_v2_backup_before_notes/` is not a v2 backup. It contains `e5b_notes.tex` and the v3 `e3_core.tex` and `erefs.tex`. The true v2 is `claude_grind_20260925/es_reader/`, which I used for the diff.
- **N10.** The docstring of `es50_survivors.py` is a copy of that of `es50_checks.py`. Its saved output has only the 10⁷ run; the re-run at 10⁶ reproduces 2370, 54, 29, 29, 7.
- **N11.** 50_ §0 says "Twelve are listed with counterexamples". Rows 11 (the Busy-Beaver bounds) and 12 (the Kneser citation) are not counterexamples. The value "index 643" (pass E) was not re-checked here.
- **N12.** The bibliography checks out:
  - **CFS**: arXiv:1912.07997 = *Three-manifold quantum invariants and mock theta functions*, Phil. Trans. R. Soc. A 378 (issue 2163), 20180439 ([arXiv](https://arxiv.org/abs/1912.07997), [journal](https://royalsocietypublishing.org/doi/abs/10.1098/rsta.2018.0439)).
  - **Lopez**: matches archive §12.1 (v3 of 15 April 2024).
  - **CCFGH**, **Kneser** (Math. Z. 61 (1955) 429–434), **Lagarias** (Monthly 92 (1985) 3–23) and **Zagier** (Astérisque 326 (2009) 143–164): consistent with standard data.

---

## 4. Results the material implies that neither text states

### X1. Eight further quadratic-residue conditions of the same kind as Theorem 50.4

**Mechanism.** Three certificate types have a shell R = q·r, where q | S(p) is prime and r is a product of the small primes 3, 9, 5, 7 whose divisibility of S the class forces:
- M_s: u = s, with S = p + 4s;
- E_t: u = a/t, with S = p + t;
- F_t: u = t·a, with S = tp + 1.

**Search.** I ran a complete search over the parameter sets that the class modulo 10080 can see: s | 2⁶3⁴5²7² and t | 2³3²·5·7, 363 parameters in all (`ref50_more_shifts.py`). Besides the five rows already in Theorem 50.4, it finds these quadratic-residue-good conditions:

| condition | certificate | classes |
|---|---|---|
| **p+16** | u = 4 | 169, 289, 529 |
| **p+36** | u = 9 | 169, 289, 529 |
| **p+12** | u = 3 | 121, 289 |
| **p+6** | u = a/6 | 169 |
| **6p+1** | u = 6a | 169 |
| **p+24** | u = 6 | 361 |
| **5p+1** | u = 5a | 8 lifts of 361 and 529 |
| **p+20** | u = 5 | 8 lifts of 1 and 169 |

Three further hits, E_3, F_3 and E_5, are implied by existing rows.

**Two proofs.**
- *p+16 on p ≡ 4 (mod 5).* A prime q | p+16 has (p/q) = (−1/q) = −1 exactly when q ≡ 3 (mod 4). Take R = q if q ≡ 7 (mod 8), and R = 5q if q ≡ 3 (mod 8); here 5 | p + 16. Then R ≡ 7 (mod 8), so a is even and 4 | a². Also 4(a+4) = p + R + 16 ≡ 0 (mod R).
- *p+24 on 361.* (p/q) = (−6/q) = −1 exactly when q ≡ 13, 17, 19, 23 (mod 24). The certificate needs R ≡ 23 (mod 24), so that 6 | a. Take R = 35q, 7q, 5q or q respectively. This works because 5·7 | p + 24 when p ≡ 1 (mod 5) and p ≡ 4 (mod 7).

**Checks.**
- All 46,441 certificates for hard primes below 10⁷ were built and verified; none failed.
- The conditions remove 8 of the 31 survivors of Table 3 below 10⁷, leaving 23.
- In particular 43,201, which both texts give as the first survivor, is solved by p+24:
  - 43,225 = 5²·7·13·19, with (43201/13) = −1;
  - R = 455, u = 6;
  - 4/43201 = 1/10914 + 1/1036824 + 1/1885982856.
- p\* is also certified by p+36 (non-residue factors 167 and 811).

**Consequence.** The list of "nine conditions" and Table 3 describe one stopping point, not the method's limit. Pass A1 already asked the open question behind this (its O2: which shifts αp + β have the quadratic-residue property on a class?). Neither text carries that question over.

### X2. When the width-one and group barriers coincide

**Claim.** They coincide whenever every prime factor of R is ≡ 3 (mod 4), not only for prime powers (50_ Proposition 50.8(3); reader groupbarrier(c)).

**Proof.**
- In that case the 2-Sylow subgroup P of (ℤ/R)^× is elementary abelian, and G = P × H with |H| odd.
- 4 is a square, so it lies in H.
- If −1 = 4^j k with k ∈ K, then projecting to P gives π_P(k) = −1.
- Since |H| is odd, k^{|H|} = π_P(k) = −1, so −1 ∈ K.

**Consequence.** The width-one barrier is strictly sharper than the group barrier only when R has a prime factor ≡ 1 (mod 4).

**Checks.**
- 87 values of R below 700 and 1398 subgroups, with no disagreement.
- All 124 separating shells of the count have such a factor: 91 = 7·13, 187 = 11·17, and so on. The smallest R that can separate is 35 = 5·7, with K = ⟨6⟩.
- A1's "needs two distinct prime factors" and C's Proposition 4.6 are special cases (`ref50_barrier_general_OUTPUT.txt`).

### X3. The rows as Salez charts

The five rows of m3(ii) are Salez charts. So are all of X1's conditions:
- M_s = (1c) with B²D = s, D squarefree;
- E_t = (2b)(1, t, R);
- F_t = (2b)(t, 1, R).

This gives one description of every condition in §3 and credits the families correctly.

### X4. Exact containments of the 29-channels

See m6: 917 (mod 1276) ⊂ Rosati (80, 40), and 1605 (mod 2204) ⊂ 14a(2, 23, 3).

### X5. A certificate proof of Theorem 50.1(a), "only if"

Every one of the 20,790 non-square base classes has an explicit witness (R, m, u) with R = 3^a5^b7^c11^d19^e23^f:
- exponents ≤ 3 suffice for all but 335 classes;
- exponents ≤ 11 for all but 2;
- the last two, 995,569 and 2,726,089, need R = 3¹³ with (m, u) = (23, 23).

All 20,790 lifts satisfy the class conditions and the formula of Lemma 50.2. Four hundred random lifts contain a prime whose solution was verified exactly (`ref50_core_OUTPUT.txt`). The status "finite computation" can therefore become an explicit certificate table.

### X6. Non-coprime shells never matter

See m5: p | a, and the error needs R ≥ 3p².

### X7. Theorem 50.6 in quadratic-residue form

See m4.

### X8. Lock universality

See M2: 409 is the only exception ≡ 1 (mod 4) below 3·10⁶, so the natural question is the one for the hard primes.

---

## 5. Checked and found correct

- **Lemma 50.2 / j1square.** Each step checks: (n/R) = −(u/R), the reciprocity step, the case ℓ = 2 and the "in particular". The formula also holds on all 20,790 witnesses.
- **Theorem 50.1 / termcore.**
  - (a): "if" proved; "only if" confirmed constructively (X5).
  - "Some lift of it modulo lcm(M₂₃, R) is certified" is exactly the author's predicate. The script tests −4u ≡ a (mod gcd(M, ρ)), with availability read from ρ mod 4ℓ (mod 8 for ℓ = 2); this is the source note's lifted-target-count lemma.
  - 4951, 45,139, 22,074 and 2970 reproduced three times: by my brute force, by es50_support_core and by the author's scripts.
  - (b)–(c): 3520 = 2970 + 550 by an independent enumerator (175,501 chart classes, 3483 identities verified). The non-square patterns are 176 (11 only), 91 (19 only), 212 (23 only) and 71 (mixed).
  - B1's enumerator re-run: 64,149, 3520, and 147,348 at G₇.
  - 3361, 18,481 and 2,840,041 are uncovered and non-square; 1201 is covered.
  - Densities 1/256, 1/216, 1/990.7 and 1/1024, together with 142,560 = 6·5·6·8·9·11 and 4788, check.
  - 9/12,236 checks.
- **Theorem 50.4 / eightshifts.** Every row checks: the characters, the divisibilities, u | a², the argument 3 | shift ⇒ R = 3q for q ≡ 5 (mod 8), the 3p+1 row (N₃ ≡ 1 mod 3, a = qm, 4qm − p = R) and coprimality.
  - 780,700 certificates (the sum of A1's per-shift counts); 247 survivors; 2521, 9601 and 33,961; the factorisations of p\*.
  - The archive locators check: 24.50, including its final sentence on (p+1)/2 and p+4; 24.171 with k = 3; (2028) with s = 2.
  - The norm-form corollary checks.
- **Theorem 50.5 / pplus5.** Both cases check: H = {1, 3, 7, 9}; N ≡ 7 or 3 (mod 20); the forced divisors 3, 7 (class 121) and 9 (p ≡ 4 mod 9); the counterexample 12601 (N = 3·11·191). The counts 41,419, 19,546 and 5688 check.
- **Theorem 50.6 / visiblebox.**
  - The proof checks.
  - The table 72/72/48/12/48/30/20/4/12/1 was recomputed by a different method, from exponents read off actual primes.
  - The counts 90,897 and 50,545 check, and so does the bound 315 ⇒ R ≤ 631.
  - The class descriptions for R = 11, 19 and 23 check.
- **Proposition 50.7 / mu17.**
  - The six classes modulo 42,840 are 2881, 7921, 11449, 16489, 18001 and 26569; the finite condition holds on each.
  - The count 433 checks.
  - For the example 2,458,369, p + 17 = 2·3²·7·109·179, and lock (b) with h = 6867 and R = 375 gives a verified solution.
- **Proposition 50.8 / groupbarrier(c).**
  - (1)–(3) are correct, including the prime-power equivalence (strengthened in X2).
  - (433, 91): K = ⟨40⟩ = {1, 27, 40, 53, 66, 79}, (131/91) = −1, and the shell is empty.
  - The count of 124 checks independently.
  - The example p = 73, R = 483 (C's Proposition 4.6) checks.
- **Proposition 50.9 / noncoprime.** Part (2) is proved correctly. For the p = 73 example: y = 60, z = 1920/73, and there is no solution with this a.
- **Proposition 50.10 / ramified.** Both parts check, with the counts 233 and 947.
- **Pair-count series / pairzeta.** The formula is proved correctly; 918 coefficients (R = 7, 11, 15) were checked independently with complex characters.
- **Rosati / rosati.** The identity checks, as do the parameters of chart 14a (c, 1, k/c), the case 76 (mod 87) with (22, 11), and the rows 15b (1, 29, 11) and (1, 29, 19).
- **Locks / locks.** The identities check. The Elsholtz–Tao faces check through archive (407) and (411): lock (a) is Type I with A = 1 and C = µ; lock (b) is Type II with C = 1 and (A, B, D) = (µ, 2e, t), which is Lopez Type B. The corrected numerator ps + p + µ checks.
- **The class 429 (mod 620)** and 33,289 in the square core check.
- **The three computations of §7.**
  - Every hard prime below 10⁷ has a lock.
  - Exhaustively, 1201 has no type-(a) lock (it has (b): µ = 17, h = 203), and 5569 has no type-(b) lock (it has (a): µ = 17, d = 7).
  - Every p ≡ 1 (mod 24) below 10⁷ has a Type II solution with R ≤ 107, and p\* alone needs 107.
  - Complement squares (Lopez Type C, independent search) fail first at 97; the first hard failure is 3361. The bound R ≤ (p+4)/3 is correct.
- **The Collatz remark.** It checks: the formula for Π_k, the recurrence, Π_k ≡ 5 (mod 8) for k ≥ 1, the certificate R = 3 with u = 2 for P ≡ 5 (mod 8), and 4/5 = 1/2 + 1/20 + 1/4.
- **Table 3.** The 10⁶ and 10⁷ columns were re-run.
- **§12 solutions.** All four solutions are exact, and their shells R = 3, 19, 7 and 3 are the least occupied ones.
- **Locators checked in the sources.**
  - The source note's statements and the TRC quote ("gives the terminal smooth core", l.123).
  - The June diagram (hard prime → H^sm) and the README.
  - Pre-Niemeier Theorem 3.1 (width-one).
  - Subtori Theorem 3.7.
  - Constructive Algebra: Lemma 13.4 and Theorems 15.1–15.3.
  - The three correctly attributed unconditioned lemmas.
  - Archive Theorems 15.5 and 15.7, 24.50, 24.171 and (2028), 24.228, 25.8, §12.1 (Lopez) and §13.2 (Salez).
- **The GL₂(3) census.** A1's script re-run gives 13 involutions, against 1 for the binary octahedral group.
- **Page counts.** The TRC PDF has 52 pages. The item counts 508, 390 and 744 appear in the D, E and F inventories.

---

## 6. Programs and outputs (all in this folder)

| program | checks | result |
|---|---|---|
| `ref50_core.py` | 4951 by brute force; explicit witnesses for all 20,790 non-square classes; Lemma 50.2 formula; 400 prime solutions; 45,139 and 22,074 | all as claimed; X5 |
| `ref50_salez_M23.py` | independent seven-chart enumerator from archive §13.2 | 840: the six squares; M₂₃: 3520 = 2970 + 550 |
| `ref50_more_shifts.py` | complete search for further quadratic-residue shift conditions; exact certificates; survivors | X1: 46,441 certificates; 31 → 23 |
| `ref50_misc.py` | 32 checks: solutions, p\*, 43,201, Rosati, locks, Type C, norm forms, the redundancy of Theorem 50.6, barriers, Propositions 50.9–50.10, pair zeta, Collatz, µ = 17 | all pass |
| `ref50_barrier_general.py` | X2 | 0 disagreements; all 124 separating shells have a factor ≡ 1 (mod 4) |
| `ref50_visiblebox.py` | the visible-box table from empirical exponents | identical |
| `ref50_locks_scope.py` | least shells of the §12 primes; lock universality for all p ≡ 1 (mod 4) | 409 is the only exception below 3·10⁶ |
| `ref50_salez_rows.py` | the rows as Salez charts (2b)/(1c) | 11,344 certificates, 0 mismatches |
| `ref50_examples.py` | 2,458,369 and p\* under the new conditions | as stated |
| `rerun_*_OUTPUT.txt` | outputs of the re-runs of es50_checks, es50_support_core, es50_survivors, the Salez script, the author's three scripts and A1's lattice check | all reproduce their stated values |
