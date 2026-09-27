# Referee report on *The S⁶ record: a reader of its results* (version of 26 September 2026, 22 pages)

Referee: an independent Claude instance (claude-opus-5-5) that wrote none of the reader. Report of 27 September 2026, returned as text (subagents cannot write report files here) and saved verbatim in substance by claude-ab. Check script: `referee_checks.py` in this folder (22 checks, all pass).

Scope: the reader and the correction note (`00_`) read in full. Read in part, against the reader's claims:
- the monograph `01_`: Part I, the 21-item §1 list, §§3, 13.1–13.3, 13.10, 13.11, 14;
- the source manuscript `03_`: summary, §§1.1–1.2, Remark 7.28, Theorem 7.22, Corollary 7.29, Remark 9.21, §§10.1–10.3;
- `14_`, `26_`, `29_`, `30_`, `05_`, the README and the metadata;
- the claim ledger inside `04_`.

Files `07_`–`13_` were not opened. The reader's scripts reproduce: 47/47 checks pass, and the inventory gives 32 matches with 1 file not local.

**Overall.** No mathematical error was found in Section 5 or in Proposition 6.1. The problems are in three areas:
- attribution and novelty;
- how the record is reported: the OPEN rows, the monograph's §14, and the Engel citation;
- the status labels.

Several implied results are not stated; the most useful is M1.

## Findings

**F1 (MAJOR).** The abstract's first "added" result is the source manuscript's Remark 10.4 restated.
- For a reduced hypersurface, "codim Sing ≥ 2" is equivalent to "normal". Hypersurfaces are Cohen–Macaulay, so they satisfy S2, and Serre's criterion says that normal means R1 together with S2.
- So "the step can fail only on fibres singular along a curve" is the contrapositive of Remark 10.4.
- Corollary 5.4's two examples are the same condition.
- Proposition 5.3's "in particular" understates what is in fact an equivalence.
- What is new relative to the record: the converse (T_S ≠ 0 at every non-normal point), the Ext formula, and arbitrary dimension.
- Fix:
  - state Proposition 5.3 as T_{S,x} = 0 ⇔ S normal at x ⇔ codim_x Sing S ≥ 2;
  - reword the abstract, crediting Remark 10.4 for the normal case;
  - drop the duplicate example;
  - move the Appendix A row out of "New in this reader".

**F2 (MAJOR).** The record's two OPEN rows are misreported (§1.3, §4.3, §8.1 item 1, Appendix A).
- The claim ledger in `04_` (48 rows: 42 VERIFIED, 2 OPEN, 4 REFUTED) has two OPEN rows:
  - `S6-OPEN-HODGE-REPLICATION`: replication of the cyclic invariant lattices, the logarithmic determinant divisor, the residue cancellation and the order-four scalar test;
  - `S6-OPEN-EXTERNAL-ADJUDICATION`: specialist and community adjudication of the complete construction and counterexample.
- The README says the OPEN rows concern "independent specialist replication and external adjudication".
- The monograph's §1 list has only one OPEN item (item 21).
- The counts 42/0/2/4 come from the claim ledger. "Rows 7, 12, 17–20" refers to the monograph's §1 list, a different object. The fourth REFUTED row (Remark 7.28) is §14 item 2 of the monograph.
- The four REFUTED rows named in the reader match the claim ledger: `S6-CDP-P692`, `S6-CDP98-MONO`, `S6-HODGE-CUSP-TORSION`, `S6-LOCAL-728`.
- Fix: correct the three passages, and distinguish the claim ledger from the monograph's §1 list.

**F3 (MINOR).** Classical results are not cited.
- Proposition 5.3 is the case p = 1 of two classical theorems:
  - U. Vetter, Manuscripta Math. 2 (1970) 67–76, Satz 4: for a reduced complete intersection, Ω^p is torsion-free for p < codim Sing and has torsion for p = codim Sing;
  - the converse, by K. Lebelt, Math. Ann. 211 (1974) 183–197.
- Lemma 5.2 is the torsion part of the Auslander–Bridger sequence.
- Proposition 5.9(a) and (d) are cases of Saito's generalized de Rham lemma (Ann. Inst. Fourier 26:2 (1976) 165–170) and of Koszul–Ext (Bruns–Herzog §1.6).
- Fix: cite them, and relabel the rows "proved here; classical in general form".

**F4 (MINOR).** "On any fibre N* ≅ O_S" is false for multiple fibres; there N* is a nontrivial torsion line bundle. Fix: write "on any reduced fibre".

**F5 (MINOR).** In §3, the triple (1,2,1) is the reader's own example; the record's candidate uses (0,1,−1), with p = −1. The sentence "For such a choice, the manuscript concludes…" extends conclusions that the manuscript states only for its own X. Fix: use (0,1,−1), or mark (1,2,1) as the reader's example.

**F6 (MINOR).** §4.4 misdescribes the monograph's §14.
- Item 3 is cohomological arrows labelled as homology, not a sign.
- §14 has seven items: five labelled VERIFIED (four local repairs and one build defect) and two REFUTED. Item 7 is not mentioned.

**F7 (MINOR).** Engel's exposition cites [CDP98, Cor. 4.2], not [CDP20]. Fix: "the result [CDP98, Cor. 4.2], re-proved in [CDP20, Cor. 2.3]".

**F8 (MINOR).**
- (a) A holomorphic fibration over P¹ gives only a(X) ≥ 1.
- (b) The source quotes the journal's Corollary 2.3 on p. 680. Its footnote says that the journal text agrees, up to copy-editing, with arXiv:1904.11179v2.

**F9 (MINOR).**
- (a) S6-1 to S6-4 are labelled "Located", although their proofs (in `28_`) were not seen. Use a weaker label.
- (b) The "What was read" list omits the source's Theorem 10.5 and the monograph's §13.10 (Theorem 13.28), both of which the reader cites.

**F10 (MINOR).**
- (a) The source's §10.1 quotes p. 692 verbatim, with "provided L|S is non-torsion". Read that way, the step is the §5 implication with A = L|_S non-torsion, and Lemma 4.3 covers it with an extending bundle.
- (b) §8.1 item 3 does not say that the record claims a negative answer at the candidate's cusp fibre. "No local argument can give this" is imprecise, because H¹(S, A) = 0 is a global fact.

**F11 (MINOR).** About nine of the 47 checks restate typed-in values. No check tests the dimension statement of Proposition 5.6, or that the relations at t = xyz are complete. Suggestion: a Hilbert-function comparison. H²(Ω^•, dt∧) for t = xyz has Hilbert function (0,0,0,2,3,3,…), which equals that of R²/⟨(x,0),(y,−y),(0,z)⟩(−3).

**F12 (MINOR).** Citation precision.
- (a) Hartshorne III.5.1 is Zariski cohomology; add GAGA.
- (b) Ext² is the canonical module because R/J is Cohen–Macaulay (a reduced curve). Cite Bruns–Herzog Theorem 3.3.7 (number from memory).
- (c) [GR84] is cited with no locator.
- (d) The attribution-file statement is cited to [AlpogeS6], which is the manuscript. `26_` says "circulated by Levent Alpöge with Fable".
- (e) Cite Atiyah–Singer III, §4.
- (f) "No error was found" should say "no mathematical error".
- (g) Lemma 5.2 needs J ≠ R. The Matsumura theorem numbers were not checked online (robots).

**F13 (MINOR).**
- (a) "28_" and "47_" name both record files and audit notes.
- (b) The §2.1 table groups `06_` (a receipt) with the conversation files.
- (c) Guide `14_`'s disclaimer is in its unnumbered preamble and §4, not "§§1 and 4".
- (d) The version-1.0 DOI 22235524 is in no local file and was not checked.

**F14 (MINOR).** Theorem 5.8, audit point 1: the key lemma is already stated at this generality in the note's Lemma 5.1 and the monograph's Lemma 13.27, which assume only a nonzero effective divisor. It extends further: see M4.

## Missed or implied results

**M1.** Let S = {g=0} be a reduced hypersurface with Jacobian ideal 𝒥.
- (a) φ⊗[g] ↦ φ dg is an isomorphism 𝓗om(𝒥, O_S) ⊗ N* ≅ K_S, sending O_S⊗N* onto N*. So the first sequence of Proposition 5.1(b) is (0 → O_S → 𝓗om(𝒥,O_S) → 𝓔xt¹(O_S/𝒥,O_S) → 0) ⊗ N*.
- (b) If S has normal crossings, then 𝓗om(𝒥, O_S) = η_*O_{S̃}, and 𝒥 is the conductor. So, when H⁰(Ω̃¹_S ⊗ A) = 0, H⁰(Ω¹_X|_S ⊗ A) ≅ H⁰(S̃, η*(N*⊗A)). On a reduced normal-crossing fibre, the step's conclusion holds iff H⁰(S̃, η*A) = 0.
- (c) A general form of the source's Theorem 10.5(a), for H²(X;Z) = 0 and a normal-crossing reduced fibre whose normalization has a component with q = 0.
- (d) In the test family the dimension is 1 for every λ ∈ C*; for λ = 1 the group is spanned by dt. Conditionally on the record, the candidate's cusp fibre also gives dimension one.
- Proof sketch:
  - φ ∈ (O_S :_Q 𝒥) makes φ dg regular with torsion image, and the converse holds via Proposition 5.1(a).
  - For g = x₁⋯x_k one gets (R :_Q 𝒥) = R̃.
  - Apply the projection formula.

**M2.**
- (a) T_{S,x} = 0 ⇔ S normal at x ⇔ codim Sing ≥ 2.
- (b) For M = Rⁿ/Rv there is an exact sequence 0 → Ext¹(R/J,R) → M → M** → Ext²(R/J,R) → 0. So Ω¹_S is reflexive iff codim Sing ≥ 3, and it is never reflexive at a singular point of a surface.

**M3.** Tors Ω^p_{R/C{t}} = H^p(Ω^•, dt∧) ≅ H_{n−p}(∂t; R). This vanishes for p < c = grade J_t, and is ≅ Ext^c(R/J_t, R) for p = c.
- For p = 1: gcd(∂_i t) = t/rad t. Globally, Tors Ω¹_{X/B} ≅ (f*ω_B ⊗ O(Z))|_Z with Z = Σ(f*c − (f*c)_red).
- For the record's X, on its local models:
  - Tors Ω¹_{X/B} ≅ f*ω_B(2S₁+3S₂)|_{2S₁+3S₂};
  - near W, Tors Ω²_{X/B} ≅ ω_D (sketch);
  - if D is three rational curves through two triple points, p_a(D) = 2.

**M4.** Theorem 5.8 already holds under b₁ = b₂ = 0 with a divisor. Hence every rational homology 6-sphere with a divisor has H²(T_X ⊗ L) ≠ 0 for all L, and R²f_*(T_X ⊗ L) ≠ 0. So the record's relative failure already follows from c₃ = 2; the monograph's §1 item 13 overstates how independent the two failures are.

**M5.** P(D₄) = {n ∈ 2Z : 3 ∤ n or 9 | n}. So τ = 12√2·k is attained iff 3 | k; for example 36√2 at a = (−3,0,1,2). The proof uses Legendre's three-square theorem.

**Q1.** Is there a compact complex threefold with H¹(X;Z) = H²(X;Z) = 0, a(X) = 1, holomorphic algebraic reduction and b₃ ≥ 2, having a reduced normal-crossing fibre whose normalization has a component with q = 0?

**Q2.** Does the Leray route through R^q f_*Ω^p_{X/B} reproduce h^{1,2} = 1?

## Checked and found correct

- All of Section 5's mathematics; the audit bullets; Proposition 5.6 with the normalization count; Theorem 5.8 and the Riemann–Roch coefficients.
- Proposition 5.9(a)–(d), including the Hilbert–Burch identification.
- Proposition 6.1 and the §6 numbers.
- §3 against the source's matrices; §4.2; the attributions to `03_`; the §2 counts, DOIs and hashes.
- Engel's exposition and the manuscript title, confirmed online.
- Not checked (refused): Matsumura's theorem numbers (Google Books, robots), the Zenodo API (robots), a Cambridge Core review (403).
