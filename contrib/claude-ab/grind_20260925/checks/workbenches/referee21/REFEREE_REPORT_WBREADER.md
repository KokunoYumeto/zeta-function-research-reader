# Referee report: "Four workbenches and where they meet" (wbreader.pdf, 26 pages)

Referee: Claude (Opus 5.5). I did not write the document, the notes 43_–47_, or the first-pass reports. 26 September 2026.

I worked read-only on `workbench_reader/`, ``, `reader/` and the five source clones. I read the clones with `git show <commit>:<path>` at ES `d20b32e`, Collatz `caf04ff`, 817 `dbd0a93`, YM `fa79faf` and zeta `baa6f7a5`. I used no web access.

All my files are in `scratchpad/referee21/`:
- `wb/`: my scripts and their `*_OUTPUT.txt` files;
- `pg-01.png` … `pg-26.png`: page renders;
- `wbreader.txt`: the extracted text.

The folder already held files from an earlier session (`ref21_*.py`, `tex/`, `zeta_*.tex`, `ym_*`). I left them untouched.

Page numbers are PDF pages. Theorem numbers follow the PDF.

---

## Overall verdict

**The mathematics is sound.** I checked every written-out proof step by step, including constants and signs. All of them are correct:
- Theorem 1.1, Propositions 1.2 and 1.3, and the §1.3 families;
- Proposition 2.1 (statement), Theorem 2.2, Lemma 2.3, Theorem 2.4, Propositions 2.5–2.7, and Theorems 2.8 and 2.9;
- Lemmas 3.2–3.4, Theorem 3.1, Corollary 3.5, Theorems 3.6 and 3.7, and Proposition 3.9;
- Lemmas 4.2 and 4.3, Propositions 4.4–4.6, and the NS-04(b) proof.

Three proofs compress a step, and those points are minor (m24, m31, m32). Every number I recomputed agrees with the document. The list of checks is at the end.

The document never claims to prove or disprove the Erdős–Straus or Collatz conjectures, or a continuum Yang–Mills mass gap. Quotations are all short.

**The problems are in the surrounding claims:**
- an unverified external claim (a complex structure on S⁶) stated as fact;
- one status label stronger than the evidence (NS-04(a));
- two dropped scope conditions in the intersections table;
- one overstatement in the patterns section;
- an incomplete Erdős–Straus credit line;
- several process claims about the audit that the record contradicts, including a dangling sentence promising a description of this referee pass.

**Counts: 8 MAJOR, 52 MINOR.**

---

## MAJOR findings

### M1. An unverified external claim, a complex threefold diffeomorphic to S⁶, is stated as fact
- **Where:** Abstract (p. 1), "on a complex threefold diffeomorphic to $S^6$"; §4.6 (p. 19), "fibred by tori over the projective line and diffeomorphic to $S^6$".
- **What is wrong:**
  - A compact complex threefold diffeomorphic to S⁶ is a complex structure on S⁶. That is the manuscript's claim, and Engel's exposition makes it too. The audit did not check it: S6-1 to S6-4 are "located", and only the arithmetic part of S6-5 was proved.
  - The workbench itself does not certify it. §4.6 says so two sentences later, which makes the unattributed statement contradictory.
- **Evidence:**
  - YM `s6/README.md` L11: the package "does not independently certify a global complex structure on S6".
  - YM `ATTRIBUTION.md` L39: the hypotheses of the uses "do not require an independent proof here" of the identification with the six-sphere.
  - `47a` L56: the manuscript's abstract claims X is "diffeomorphic to S6".
  - `47a` L448: Engel's exposition states a proof, and that is "outside the repository".
  - `46_` §6: S6-1 to S6-4 are located.
- **Correction:**
  - Abstract: "…and on a manuscript that constructs a compact complex threefold which it states is diffeomorphic to S⁶ (not checked here)…".
  - §4.6: "…a compact complex threefold fibred by tori over the projective line, which the manuscript states is diffeomorphic to S⁶; this was not checked here, and the workbench does not certify it."

### M2. NS-04(a) is labelled "audited", but its existence proof was not re-checked
- **Where:** §4.5 (p. 19), "*Exact constraint data* (NS-04(a); audited)".
- **What is wrong:**
  - The front matter defines Audited as "read in full, every step was checked" (p. 2). That did not happen here.
  - The first pass checked the TT lift, the conformal exponents, the decoder and the barrier inequalities.
  - The existence of the positive Lichnerowicz solution was not re-checked. It rests on monotone Dirichlet solves on expanding balls, interior compactness and comparison.
  - §6 does not list it among the unchecked items either.
- **Evidence:**
  - `46a` L248: "The existence proof itself was not re-checked beyond the barrier inequalities."
  - `46a` L313 lists it under "Not checked in this pass".
  - The source proof is at YM `navier-stokes/continuations/20260919-vacuum-hydrodynamics/README.md` L50–57.
  - `46_` L114 carried the same "audited" label into the reader.
- **Correction:**
  - "(NS-04(a); audited in part: the encoding, the decoder and the barrier inequalities checked symbolically; the existence of the Lichnerowicz solution by the standard barrier method read, not re-checked)".
  - Add "the existence step of NS-04(a)" to §6 (YM).

### M3. The process claims about re-runs and inventory are contradicted by the record
- **Where:** "How the audit was done" (p. 1); Appendix A, "First-pass audits" and "Re-runs" (p. 25).
- **(a) "re-ran every first-pass script (identical outputs apart from timing lines)".** False as written.
  - The author did not re-run 45a's three C programs: `g4_bruteforce.c`, `g4_decreasing.c` (including the n = 7 run on which g₄(7) ≥ 176 rests) and `g4_upper7.c`. Nor did the author re-run the 168-second Tao-clock script.
  - `rerun_20260926/ep817/` holds only the five Python outputs, and `rerun_20260926/collatz/` only six (my listing: `wb/wb_rerun_audit_OUTPUT.txt`).
  - Note 45 L7 says "45a's C searches were not re-run by me"; note 44 L7 names the Tao-clock exception.
  - The appendix admits only the Tao-clock exception; the front matter admits none.
  - The notes had been corrected on exactly this point (REFEREE20 45-m10 and cross-cutting point 2, L327–330 and L545). The reader reintroduces it.
  - Where re-runs did happen, I confirmed that the outputs differ only in timing and exit lines.
- **(b) "re-ran the workbench's own checkers where they were fast"** (Appendix: "where … they ran in a few minutes they were re-run as well"). This holds only for Collatz (44a) and YM (46a).
  - The 817 first pass ran none of them: "The workbench's own verifiers … were not run; I wrote independent checks instead" (`45a` L464).
  - The ES first pass ran none either. Its four scripts are its own, and its method section (`43a` §0) lists no workbench checker.
- **(c) "an inventory of all four repositories (made before the audits)".** 47a surveyed ES, YM (with NS and S⁶), 817 and zeta. It records that no Collatz repository was provided and that the Collatz workbench "was not surveyed" (`47a` L5, L59, L725; note 44 L5).
- **Correction:**
  - "re-ran every Python script of the first passes except the 168-second Tao-clock script (identical outputs apart from timing lines). The C searches of 45a were not re-run; a separate search of the author's (`g4_bitset.c`) replaces them for n ≤ 6."
  - "the Collatz and Yang–Mills first passes also re-ran the workbenches' own checkers; the Erdős–Straus and 817 first passes wrote independent checks instead."
  - "an inventory of the ES, YM, 817 and zeta repositories (the Collatz repository was cloned later, for the audit)".

### M4. The sentence promising a description of this referee pass has nothing after it
- **Where:** Appendix A, "Referee passes" (p. 25), "This reader then had a referee pass of its own, described below."
- **What is wrong:** Nothing follows except "Where everything is" and the references. In a document to be published, the sentence claims a review whose description, findings and disposition are absent.
- **Correction:** Add a paragraph naming this pass: who made it, what it re-derived and recomputed, how many major and minor findings, and what was applied. Or delete the sentence.

### M5. Edge 11 (NS → YM) drops half of its condition
- **Where:** §5.1 table, edge 11 (p. 20), "audited; conditional on NS rate bounds". §5.2.6 (p. 22) also states that the zero-quotient bound "holds for every admissible curvature weight" without the condition.
- **What is wrong:** The audit of this edge (`21_` §2) also rests on YM material it did not read:
  - the free norm formula behind (259)–(260);
  - the energy estimate (261);
  - the positive-coupling convergence theorem.

  The free zero-quotient bound, which is the part holding for every weight, depends on exactly these.
- **Evidence:**
  - `21_` L86: "Imported from YM sections I did not read."
  - The zeta reader's own table row (`reader/sec8_bridges.tex` L62): "audited; correct conditional on imported NS bounds and on YM sections not read".
- **Correction:** "audited; conditional on the imported NS rate bounds and on YM sections not read (the free norm formula, the energy estimate and the convergence theorem)". Add "given those YM inputs" in §5.2.6.

### M6. Edge 4 (S⁶ → YM): the "non-wrapping patch" scope of det B has been dropped
- **Where:**
  - §5.1 table, edge 4 (p. 20): "only through $\det B$".
  - §5.2.3 (p. 22): "and only $\det B$ enters".
- **What is wrong:** Lemma 28.2 proves that the YM calculation sees the S⁶ periods only through D = det B on the non-wrapping patch used by the source. A referee had already restricted it to that patch. The reader states it without the restriction.
- **Evidence:**
  - `28_` L127: "On the non-wrapping patch used in this file …".
  - `28_` L224: the correction "limited to the non-wrapping patch".
  - `47_` L75: "only D = det B enters on the non-wrapping patch".
- **Correction:** Add "(on the non-wrapping patch used by the workbench)" in both places.

### M7. §5.4 says a conditional theorem "proves the property", and conflates two different properties
- **Where:** §5.4, "Method obstructions" (p. 23), "where Theorem 4.1 proves the property by other means".
- **What is wrong:**
  - Theorem 4.1 is labelled Conditional on the computed order-3 to order-5 coefficient bounds (p. 16), so "proves" overstates it.
  - The property that Proposition 4.5's Neumann route fails to certify is the isolated rank-one ground-state projection, analytic in complex ξ, on the **full** space L²(SU(2)^E) with no gauge projection.
  - Theorem 4.1 is a gap bound on the **physical** space for real 0 < ξ ≤ α₅. It does not establish that property.
  - So Prop. 4.5 is not an instance of "the property holds and the method fails" as claimed.
- **Evidence:**
  - p. 18: Prop. 4.5 is "on the full space (no gauge projection)".
  - p. 16: the Theorem 4.1 status is Conditional.
  - `46a` §3 (FC8): the certified object is the Riesz projection on |z| = 3/8.
  - `47_` L129 says only that YM-01 "proves a box-uniform statement".
- **Correction:** "the global Neumann radius of Proposition 4.5, which shrinks with the box, whereas Theorem 4.1 obtains (conditionally, on the physical space and for real ξ) a box-uniform gap by local norms."

### M8. The Erdős–Straus credit line is incomplete and compresses the owner's recorded role
- **Where:** §1, opening paragraph (p. 4), "the owner (KokunoYumeto, u/lepthymo) supplied motivations and directions". Only the README and `records.json` are cited.
- **What is wrong:** The workbench's own contribution record, `CONTRIBUTIONS.md`, headed "Who contributed what", credits more people and a broader role:
  - u/Far-Lifeguard519 for "the initiating computational investigation" that prompted the project (L13);
  - u/TextBackground496 for the supersignum proposal later reused in ES (L23);
  - u/JGPTech as an upstream source (L87);
  - the owner for proposing directions and examples, directing and developing the investigations with AI, and specifying proof requirements (L101). It states that this contribution "is not reduced to an organiser label" (L95).

  The reader's line omits the initiator and narrows the owner's role.
- **Correction:** Keep the README credit and add: "The workbench's fuller record (`CONTRIBUTIONS.md`) also credits u/Far-Lifeguard519 for the initiating computational investigation, u/TextBackground496 and u/JGPTech for source ideas, and the owner for proposing the research directions and directing and developing the investigations with AI."

---

## MINOR findings

### Front matter, abstract and status vocabulary

- **m1. The abstract overstates coverage (p. 1).**
  - *Text:* "every other one is given with its status and the location of its proof".
  - *Problem:* the 17 located ES items, Collatz Chapters 4–19, most 817 continuation notes and YM-04/06/13 are not each given a status and location. They are only listed in §6 or pointed to 43a.
  - *Fix:* "the others are listed with their status, or by a pointer to the first-pass reports".
- **m2. The negative-results lists are a selection, not complete (p. 1).**
  - *Text:* "Each section ends with the workbench's negative results".
  - *Problem:* the ES table omits the checked rows "item 7 §9" and "`21_` Neg. 21.2" (note 43 §4 L149, L153). The 817 list omits `45_` §6 item 7 and `45a` §5 items 5, 11 and 12.
  - *Fix:* "…with the negative results that were checked, each within…".
- **m3. The front matter's summary of the notes' referee pass is incomplete (p. 1).**
  - *Text:* "14 major findings about status labels, credit, one missing hypothesis".
  - *Problem:* several of the 14 were false factual statements: a false summary line, "one place" (twice), "attained", a self-assessment attributed to ES, and the edge-1 misattribution (REFEREE20 L10–16). Appendix A's list is fuller.
  - *Fix:* align it with the appendix.
- **m4. The Collatz commit has no date (p. 1).** `caf04ff` has none, while the other three commits are dated. It is dated 17 Sept 2026 01:52 +0200 (16 Sept UTC).
- **m5. The branch link needs confirming before publication (pp. 1, 25).**
  - The branch `claude/claude-ab-grind-20260925` exists in the local clone (commit `366c3c9`, which contains the notes and checks).
  - The clone's remote-tracking refs do not show it on origin.
  - Confirm it is pushed, or the link will not resolve.
- **m6. Several status labels fall outside the seven defined on p. 2.**
  - §1: "audited for the least example" (item 26) and "audited for their certificates only" (items 2, 3, 8, 23). Item 23's deduction was read only in part (`43a` L397, L400), so it is "Audited in part".
  - §4.3: "implied by Theorem 4.1" (YM-05).
  - §2.5: the Tao-clock paragraph has no label (see m19).
  - §5 status column: "arithmetic checked", "checked", "ES diagram read", "ES side checked", "ES code checked", "a reading" and "—".
  - Proposition 3.10 is stated as a Proposition while its evidence is computational. The p. 2 label "Checked numerically" says "never presented as proved".
  - *Fix:* map each onto the defined labels. Alternatively, add a label such as "Computed (exhaustive search, n programs)" and say that an exhaustive search is a computer proof.

### Section 1 (Erdős–Straus)

- **m7. A disclaimer is attached to the wrong object (p. 4, Thm 1.1 status).**
  - *Text:* "and do not advertise them as new".
  - *Problem:* the source's "not advertised as new results" (`RESEARCH_STATE.md` L33) refers to the scope identities of §1.3 (the three families), not to the shell coordinates (`43a` §1.1 and §1.5; note 43 L73).
  - *Fix:* "attribute these coordinates to Elsholtz and Tao, §2"; move the "not advertised as new" remark to §1.3.
- **m8. The count in Prop. 1.2 is of unordered solutions (p. 5).**
  - *Text:* "there are then exactly $3P_1(P_2-1)/4$ of them".
  - *Problem:* this counts unordered (sorted) solutions; the ordered pairs number twice as many. Note 43 says "(unordered)".
  - *Fix:* "…exactly 3P₁(P₂−1)/4 unordered solutions".
- **m9. The count of located items reads wrongly (p. 6).**
  - *Text:* "the other 17 items are located".
  - *Problem:* after naming items 11–13, 15 and 20, this reads as 17 further items (11 + 5 + 17 = 33, not 28). The 17 located items are 1, 5, 9–13, 15–20, 24, 25, 27 and 28, which include those five (§6, p. 24).
  - *Fix:* "the remaining 17 items, including these five, are located".
- **m10. Item 4: say "two implementations" (p. 6).**
  - *Text:* "run twice by the workbench".
  - *Fix:* "run by two independent implementations of the workbench" (`43a` L268).
- **m11. The genus formula needs its 3 ∤ D hypothesis (p. 6, §1.5).**
  - *Text:* "the covers have genus $(5D^3-12D^2-17D+24)/24$".
  - *Problem:* the source states g(D) for 3 ∤ D, where the cover is connected (`es_s6_counterfactual/src/core.tex` L106–108). For 3 | D the cover has two components. The formula then equals g₀ + g₁ − 1, which I computed for D = 3, 9 and 15 (`wb/wb_es09_orbits.py`).
  - *Fix:* add "(3 ∤ D)".
- **m12. The ES-09 status reads as if only D ≤ 15 was checked (p. 7).**
  - *Text:* "the genera for $D=1,3,\dots,15$ from cycle counts".
  - *Problem:* 43a read the general proof (core.tex in full) and also recomputed D ≤ 15.
  - *Fix:* "Audited: the proof read; the relations, orbits and genera also recomputed from cycle counts for D = 1, 3, …, 15."
  - *Credit:* the even-D failure ("at D = 2 the orbits have sizes 2 and 6", p. 6–7) was found by the twentieth-pass referee (note 43 L131). The reader does not say so.
- **m13. Table row "item 21": name the population (p. 7).**
  - *Text:* "3,041 of 3,654 sources below 2600".
  - *Fix:* "3,041 of the 3,654 other-word (u ∤ 36) sources at primes below 2600". There are 4,233 proper trace sources in all (`43a` L351–353).

### Section 2 (Collatz)

- **m15. Two symbols in Theorem 2.2 are undefined (p. 8).** Φ (the standard normal distribution function) and P (the empirical law of the first m exponents over the N starts of Prop. 2.1) are not defined in the statement.
- **m16. Say which referee (p. 9, Thm 2.4 status).**
  - *Text:* "by the referee on 1,200 further pairs".
  - *Fix:* "by the referee of the notes (twentieth pass)".
- **m17. Prop. 2.6 widens the source's hypothesis without saying so (p. 9).**
  - *Text:* "For $x\ge2$" (attributed to Chapter 2, Theorem 7.1).
  - *Problem:* the source states it "For every real x ≥ 3" (`stopped_affine_transport_20260914/note.md` L694–698). The inequality holds for x ≥ 2 (my check), so the reader's version is a valid extension, but that is not said.
  - *Fix:* "(stated there for x ≥ 3; the proof gives x ≥ 2)".
- **m18. Chapter 9: "proves" and "re-derived here" overstate (p. 10, §2.5).**
  - *Text:* "The workbench proves (Chapter 9; re-derived here from the overview's statement".
  - *Problem:* the re-derivation is in 44a §2.6, not in this reader. The chapter's proof is only located.
  - *Fix:* "The workbench states, with a proof in Chapter 9 (located; the statement re-derived from the overview in 44a §2.6), that …".
- **m19. The Tao-clock paragraph has no status (p. 10).**
  - *Fix:* add "Conditional on Tao's Proposition 1.11: the deduction audited; the preprint's repairs to Tao's §§5–6 not audited" (note 44 L132).
- **m20. "Odd-return words" is used but never defined (p. 11, §2.6).**
- **m21. The Collatz note re-proves only part of the reconstruction (p. 11, Thm 2.9 status).**
  - *Text:* "which the Collatz note cites and re-proves".
  - *Fix:* "…and re-proves the part it uses" (note 44 L140; `note.tex` L298).
- **m22. The coefficients of the triangular map are misdescribed (pp. 11, 21).**
  - *Text (§5.2.1):* "whose coefficients are the Hurwitz jets $b_j(\rho)$ and the derivatives of $\zeta$".
  - *Problem:* the triangular relations also involve the derivatives b_j^{(k)}(ρ). At J = 2: ζ′(ρ)c₂ + ½ζ″(ρ)c₁² + b₁′(ρ)M₁c₁ + b₂(ρ)M₂ = 0, with b₁′(ρ) = −ζ(ρ+1) − ρζ′(ρ+1). I recovered M₁ = 18.4, M₂ = 433 and the weights (0.5, 0.2, 0.3) from these relations numerically (`wb/wb_cz_hurwitz.py`).
  - *Fix:* "…whose coefficients are built from the derivatives at ρ of ζ and of the jet coefficients b_j".

### Section 3 (Erdős 817)

- **m23. The Lean statement is too coarse (p. 12, Thm 3.1 status).**
  - *Text:* "The lower half is not in Lean."
  - *Problem:* the relation-splitting algebra of Lemma 3.2 is in `Core.lean` (`relation_splitting`). The block decomposition, the ternary count and the lower bound itself are not (`45a` §2.3 L222 and L233–234).
  - *Fix:* "The lower bound is not in Lean; only the algebra of Lemma 3.2 is."
- **m24. One step of Lemma 3.3's proof is compressed (p. 12).**
  - *Text:* "peel off a minimal sub-relation; the remainder vanishes on it".
  - *Missing step:* a support-minimal restriction u·1_S that is a relation is a globally minimal relation (apply Lemma 3.2 to u·1_S ± s for any relation s with supp s ⊆ S). 45a records this (L109).
  - *Fix:* add that sentence.
- **m25. Missing status lines (p. 13).** Corollary 3.5 has none; note 45 L42 marks it Audited. Lemmas 3.2–3.4 have none either; say that Theorem 3.1's status covers them.
- **m27. The g₄(7) lower bound omits one ingredient (p. 14, Prop. 3.10 status).**
  - *Problem:* maxima below 132 are excluded not by the search but by the refined form of Theorem 3.6, which uses Σa_i² ≤ Σ_{j<7}(N−j)² (`45a` L209). I get N ≥ 132 from the refined bound and N ≥ 129 from the plain bound (`wb/wb_ep_misc.py`).
  - *Fix:* add "(maxima below 132 are excluded by the refined bound of Theorem 3.6)".
- **m28. EP-08 bullet: an undefined symbol and a formula that fails at r = 0 (p. 15).**
  - U_m is undefined.
  - "a_{3r+1} = 93²·893^{r−1}" is not an integer at r = 0. The source gives a₁ = 13 separately (note 45 L94; `45a` L357).
  - *Fix:* "a₁ = 13, and a_{3r+1} = 93²·893^{r−1} for r ≥ 1", and define U_m.
- **m29. Negative result 4 does not say in what sense the bases fail (p. 15).**
  - *Text:* "every base 71–96 fails at k = 5".
  - *Fix:* add "(all-length admissibility fails: the full carry graph accepts)" (`45a` L302). I confirmed that for every such base the two-digit language already contains an integer 5-term (respectively 6-term) progression, and that bases 97 and 93 give none (`wb/wb_ep_misc.py`).

### Section 4 (Yang–Mills, NS, S⁶)

- **m30. The coupled-cluster credit reads as origination (p. 17).**
  - *Text:* "the coupled-cluster method, credited to Schütte, Zheng and Hamer".
  - *Problem:* this reads as if Schütte, Zheng and Hamer originated the coupled-cluster method. The workbench credits them for the exponential-vacuum and character/Casimir framework in Hamiltonian lattice field theory (fifth-reference README L121).
  - *Fix:* "…which the workbench credits, for Hamiltonian lattice field theory, to Schütte, Zheng and Hamer".
- **m31. Lemma 4.2's proof stops early (p. 16).** It ends at c_j ≥ 6j_e. The stated consequences Σ_e j_e ≤ (2/3)c_j and "c_j ≥ 3 on the nonconstant physical space" are not derived. Add the last line of note 46 L56.
- **m32. Prop. 4.5: an undefined symbol and an unargued direction (p. 18).**
  - E_e (the link Casimir) is undefined.
  - The proof shows only that the series converges below the radius. For "only for", add: ‖ξW_L‖ = 2|ξ|M_L exactly, and the resolvent bound 8/3 is attained at z = ±3/8, so the norm-product criterion fails beyond the radius.
- **m33. YM-05 has no status label (p. 18).** Add "(implied by Theorem 4.1, hence conditional on the same computed inputs)".
- **m34. "Proved" for a conditional theorem (p. 20, §4.7).**
  - *Text:* "Theorem 4.1 is proved only at strong bare coupling".
  - *Fix:* Theorem 4.1 is labelled Conditional; write "…holds, conditionally, only at strong bare coupling".
- **m35. The Osterwalder–Seiler statement was not re-checked (p. 17).** It is stated as a fact with citation, but `46a` L136 says it was "cited from memory and not re-checked". Add the physics literature to §6 "Everywhere" (note 46 §9 lists it).

### Section 5 (intersections)

- **m37. The §5.2.4 heading contradicts its text (pp. 3, 22).**
  - *Text:* "The Jacobian map: one map, three constructions".
  - *Problem:* the text describes one name for three different objects: F, the S⁶ construction and the four-dimensional map P.
  - *Fix:* "The name 'Fable': one name, three objects".
  - Also say that "Fable" is the agent credited in Alpöge's announcement for producing F (§4.4) and in older S⁶ files. YM `ATTRIBUTION.md` L40 warns about this.
- **m38. Edge 6 loses its qualifier (p. 20).** The type "P / A" drops the note's "P within zeta; A relative to YM" (`47_` L23).
- **m39. Edge rows lose detail (p. 21).**
  - Edges 27 and 28 are merged with status "located", but edge 27 (A, a routing proposal) has status "—" in `47_` L45.
  - Edge 14 omits "and family C" (`47_` L31).
- **m40. §5.2.2: G is undefined (p. 22).** Say "a finite abelian group G (the unit group U(R))".
- **m41. Proof steps are named, not numbered (p. 23, §5.3).**
  - *Text:* "step 4 of Theorem 2.4".
  - *Fix:* "the meeting-point step of the proof of Theorem 2.4".
- **m42. An evaluative claim is stated for every instance (p. 23, §5.4).**
  - *Text:* "each moves the difficulty without reducing it".
  - *Problem:* this is asserted for every instance. `47_` L115 states it conditionally ("does not reduce it unless the new side has a constraint that the old side lacked"). For the Hurwitz encoding and 817's restatements there is no "difficulty" being moved.
  - *Fix:* restore the conditional.
- **m43. The Tao-clock sentence drops "in logarithmic density" (p. 23).**
  - *Text:* "the Tao-clock laws, for almost all orbits along one scale sequence".
  - *Problem:* the source note keeps "in logarithmic density" (`47_` L140). Without it, the sentence reads as a pointwise almost-every-orbit claim. The results are limit laws for first entry under the logarithmic measure.
  - *Fix:* "the Tao-clock laws, statements about first-entry laws in logarithmic density, along one scale sequence".
- **m44. The certificate table in §5.4 has no caption or lead-in (p. 23).** Add one, as in `47_` §2.4: "What 'certificate verified' means in each workbench".

### Section 6 (not checked) and Appendix A

- **m46. The Collatz not-checked list is incomplete (p. 24).**
  - *Text:* "Chapters 4, 5, 7, 8 and 10–19 … (except Theorem 9 of Chapter 6)".
  - *Problem:* Chapter 6 is not in the list, so the exception dangles and Chapter 6 beyond Theorems 8–9 is not recorded as unchecked. Also unlisted: Chapter 2 §§4–6 and 8–10 (`44a` L263), and Chapter 3 beyond §§1, 3–5 and Theorem 6.1 (`44a` L27).
  - *Fix:* "Chapters 4–8 and 10–19 beyond their theorem headings (except Theorems 8–9 of Chapter 6); Chapter 2 §§4–6 and 8–10; Chapter 3 beyond §§1, 3–5 and Theorem 6.1; …".
- **m47. The YM not-checked list is incomplete (p. 24).** Add:
  - NS-04(a)'s existence step (M2);
  - YM-13 beyond its first lines;
  - the YM-05 write-up beyond R24–R31 (note 46 L143).
- **m48. §6 has no "Intersections" paragraph (p. 24).** Per `47_` §5 L175, the following were not checked:
  - edges 1a, 6, 12–15, 26a and 28 beyond location;
  - nine of the ten 817 interface notes;
  - the zeta side of edge 21 and the S⁶ side of edge 22;
  - the external record on the Collatz side of edge 18;
  - the A and M edges beyond their statements.
- **m49. The Collatz literature was cited, not read (p. 24).**
  - *Text:* "the reading of … the published Collatz cycle and verification bounds".
  - *Problem:* no note records reading Simons–de Weger, Hercher or Barina. 44a used no web access, and the 2⁷¹ figure comes from the workbench's literature reader (`44a` L306).
  - *Fix:* "…and the citation of the published Collatz cycle and verification bounds (from the workbench's literature reader; not re-read)".
- **m50. The item count is wrong (p. 25).**
  - *Text:* "48 items".
  - *Problem:* `workbench_reader_claims_checks_OUTPUT.txt` has 47 PASS lines and no FAIL line (my count). The time, 6.5 s, is right.

### Bibliography (pp. 25–26)

- **m52. Hercher [8] has no year or venue.** Add the year (arXiv 2022). If the journal version is meant: J. Integer Seq. 26 (2023), Art. 23.3.5 (from memory; I could not verify this without web access).
- **m53. OpenAI [13] has no locator.** 47a L58 records a cdn.openai.com URL.
- **m54. DLMF is cited but not listed.** DLMF 25.11.10 is cited in §2.6 (p. 11) with no bibliography entry.
- **Other entries.** The rest are internally consistent and plausible:
  - Costa (arXiv:2609.06303, dated 5 Sept 2026) and Korsky (arXiv:2606.24139, dated 23 June 2026) match the 817 workbench's citations (`notes/general-k-capacity.md` L570–572).
  - The zeta reader entry matches its title and DOI.
  - Terras, Everett, Tao (Forum Math. Pi 10, e12; Anal. PDE 2), Elsholtz–Tao, Erdős–Sárközy, Eymard, Kogut–Susskind, Osterwalder–Seiler, Schütte–Zheng–Hamer, Simons–de Weger, Mordell, Lions and Barina carry standard data.

### Typography (checked on renders at 80 dpi and on zoomed crops at 170–200 dpi)

- **m55. Narrow justified table columns (pp. 7, 20–21, 23).** They produce large gaps and odd hyphenation: "the principal-only bound" (p. 7), "the zeta programme's Hur-/witz" (p. 20), "a re-/statement" (p. 21), "byte-/identical" (p. 23). Use `>{\raggedright\arraybackslash}p{…}`.
- **m56. Monospace identifiers break at their own hyphens (pp. 1, 25).** Examples: "yang-mills-/interacting-workbench", "claude/claude-/ab-grind-20260925" and "contrib/claude-/ab/…". This makes the names ambiguous. Use `\path`/`\url` with breaks only at "/".
- **m57. Other layout points.**
  - p. 4 (Thm 1.1 status): "p ≡ 1 / (mod 12)" is split across lines; tie it.
  - p. 7: extra vertical space after the longtable.
  - p. 1: a gap after "What was read".
  - The references are not in the table of contents.
  - The status of Prop. 3.9 (p. 14) follows its proof, while every other status precedes its proof.
- There are no overfull boxes and no missing glyphs in `wbreader.log`, only underfull table cells and microtype protrusion notices. The formulas are legible and the symbols correct: ⊔, ⪯, ↔, ℓ¹, 𝔑, Δ², A♯, B*.

(Numbers m14, m26, m36, m45 and m51 are unused: those points were merged into other findings.)

---

## Status labels, credit and scope: what I confirmed correct

Apart from the findings above, every status label and scope statement I checked matches the notes and the first-pass reports:
- ES items 4, 6, 7, 14, 21, 22 and 26, and the reduction to p ≡ 1 (mod 24) and to the six classes modulo 840 (Mordell);
- Collatz 44.1–44.12 as relabelled after the twentieth pass, including 44.10 as re-derived and located, and 44.12 audited for multiple zeros (`44a` L204: "No gap found");
- 817 EP-01 to EP-09 and the small values;
- YM-01 (Conditional on orders 3–5), YM-02 (in part), YM-03 (located), Prop. 4.5, Theorem 14.2 (conditional on fixed-box limits), NS-00 (not audited), NS-04(b) and (d), and S6-5;
- the edges of §5 other than M5, M6, m38 and m39.

The corrections to the zeta reader's overlaps table (§5.5) are accurate against `reader/sec8_bridges.tex` L53–75: the Collatz workbench "was not cloned"; the Collatz side of the homogenisation row is the Zenodo record; S⁶ → ES was "located (new edge; not audited)"; 817 → zeta was "located".

---

## Proofs checked (PDF numbering)

| Result | p. | Verdict and my independent check |
|---|---|---|
| Thm 1.1 (a)–(c) | 4 | Correct: the unit argument, the factorisation, the three layers, and the swap without fixed point. Brute force on all 1,710 shells for p < 400, plus a direct search for the least denominator (`wb_es_count.py`). |
| Prop 1.2 | 5 | Correct, including P₂ ≡ 1 (mod 4). All 19,564 primes p ≡ 1 (mod 12) below 10⁶ (`wb_es_shells.py`). |
| Prop 1.3 | 5 | Correct: the discrete logs, the sufficiency table, and both cases of necessity. Same 19,564 primes. There are 989 two-shell survivors, all ≡ 1 (mod 24); the first are 1129, 1201, 2521. |
| §1.3 families; mod 840 | 5–6 | Correct. There are 6 unit squares, 24 classes ≡ 1 (mod 24), and 18 non-squares among them. |
| §1.5 ES-09 | 6–7 | Relations verified. The orbits and genera from cycle counts match for odd D ≤ 15. At D = 2, 4 and 6 the orbits fail as stated (D = 2: sizes 2 and 6) (`wb_es09_orbits.py`). |
| Thm 2.2 | 8 | Both bounds and the CLT/Hoeffding squeeze are correct. TV at N = 2²⁰: 0.004, 0.044, 0.342, 0.668, 0.895, all reproduced (`wb_cz_tv.py`). |
| Lemma 2.3 | 8 | Correct (lifting the exponent). Checked for all even e ≤ 5000. |
| Thm 2.4 | 8–9 | Every step re-derived: the range of a, the 3-adic part, the right path, the σ = 1 valuations (1,2,1) and (1,1,3), and height < 1. The example is reproduced, including v ≈ 1.2·10¹⁹ (`wb_cz_misc.py`). |
| Prop 2.5 | 9 | Correct. The hypothesis F_j(3) ≥ 3 for j < m is not used. |
| Prop 2.6 | 9 | Correct (Cauchy–Schwarz, equality at x = 7), valid for x ≥ 2 (see m17). |
| Prop 2.7 | 10 | Correct. D₁ = D₂ = −1, D₃ = 5, and the recursion D_{m+1} = 4D_m + 3^m holds. |
| Thm 2.8 | 10 | Correct. m* = 1636 (A = 2593) and k ≥ 679 exactly; the real value is 678.9990. (C37) also holds. |
| Thm 2.9 (simple zero) | 11 | Correct: the Taylor coefficients, b_j(ρ) ≠ 0, triangularity, Vandermonde, and the (K−2) pair. The residues are 19, 1, 29, and the weights (0.5, 0.2, 0.3) are recovered from the zero motion at ρ₁ (`wb_cz_hurwitz.py`). |
| Lemmas 3.2–3.4 | 12–13 | Correct (the step noted in m24 is compressed). |
| Thm 3.1, Cor 3.5 | 12–13 | Correct. D has no 4-AP mod 19; the lift is correct. |
| Thm 3.6 | 13 | Correct. The identity for 16/19 − κ_m holds for all m < 40, κ₃ = 16/19, and c_r = 0.315, 0.354, 0.398. |
| Thm 3.7 | 13–14 | Correct: composition, Fekete, lifting, and the converse via 2S(B)+1. |
| Thm 3.8, Prop 3.9 | 14 | Certificates recomputed. S = 70 and 1102, \|H\| = 38 and 291, and the 5-AP 0 … 1028. |
| Prop 3.10 | 14 | g₄(1..6) = 1, 3, 5, 14, 40, 79 and counts 1, 2, 2, 2, 7, 1 reproduced by a fourth, separately written C program in 59 s (`wb_g4.c`). The unique optimal 6-set and the 7-set with maximum 246 are admissible; the 6-set has \|T\| = 361. |
| Lemma 4.2 | 16 | Correct: disjointness, bipartiteness, the at-most-twice count, and j(j+1) ≥ (3/2)j. |
| Lemma 4.3, Prop 4.4 | 17 | Correct. The identity 3(1−χ) = d₅ is checked numerically at 1/64; the case λ/κ ≥ 3 needs d₅ ≤ 3, which holds (d₅(0) = 3 and d₅ decreases on (0, α₅]). |
| Thm 4.1 numbers | 16–17 | α₅ = 0.01842495357611761668188, g² ≥ 3.683551983985727304439. d₅(1/64) = 1.90683015670, d₅(4/225) = 1.699349, d₅(α₅) = 1.545306. d₅ is decreasing. The ×2 sensitivity gives α = 0.017905, g² = 3.7366, d₅(1/64) = 1.8946 (`wb_ym_numbers.py`). |
| Prop 4.5 | 18 | Correct. 1/1280, 1/4032, 1/9216 for L = 2, 3, 4. |
| §4.4 map F | 18 | det DF = −2. The fibre over (−1/4,0,0) is **exactly** the three points (lex Gröbner basis x(x−1)(x+1), y = −3x/2, w = (27x²−1)/4). F(γ(τ)) = (2τ − 1/4, 0, 0) and DF(γ)γ′ = (2,0,0) (`wb_fibre.py`, `wb_ym_misc.py`). |
| NS-04(b) | 19 | Both Kasner identities, the inverse, and surjectivity (round trip on 200 random Kasner data). The Kasner set forces P_w ≥ −1/2. |
| Prop 4.6 | 19 | Correct: Re(q³), gcd 2 on D₄, P ≠ ±6 (3 \| P ⇒ 9 \| P), det 6⁴·4 = 5184, minimum 12. |
| §5 identities | 21–23 | Verified: det J = 14, eigenvalues 4 ± √2, the eigenvectors; the group identity for all U(R), R ≤ 200; the constant 1/√(4+2√2) approached but not attained (minimum over \|k\| ≤ 300 is 0.3826834323865 at (−70, −169)); the curvature identity; (q−3)(q+4)/32; the Gram sandwich (triangle inequality, δ ≤ 1). |

---

## Source spot checks (at least four per section; all agree unless noted)

**Section 1 (ES `d20b32e`)**
- README L467–469: credit to The Clankers, u/CommonCareful3149 and u/UmbrellaCorp_HR.
- `results/records.json`: R06 credits u/CommonCareful3149 for the mod-107 observation; R05 credits u/CivQ17's diagrams.
- `CONTRIBUTIONS.md` L13, 23, 87, 93–101: see M8.
- `RESEARCH_STATE.md` L28–33: see m7.
- `DAILY_RESULTS_20260922.md`, "Verification boundary": no Lean build, no independent human review.
- `es_s6_counterfactual/src/core.tex` L1–30 (matrices; "For a positive odd integer D") and L97–109 (odd-level classification; g(D) for 3 ∤ D).
- `ARGUMENTS.md` L101–107: 289³ ≡ 169 (mod 840).
- Item 22 constants: README L207, RESEARCH_STATE L105.
- Item 26: p = 67369. Shells 16843–16849 are unoccupied, 16850 is occupied with E = {674, 84250}, and p is prime, ≡ 169 (mod 840) (my check).

**Section 2 (Collatz `caf04ff`)**
- README L36: credit line.
- `stopped_affine_transport…/note.md` L694–702: Theorem 7.1 for x ≥ 3 (m17).
- `clocked_support…/note.md` L404–450: Theorems 8 and 9, (C36) m ≤ 1635, (C37).
- `all_even_join_extension…/note.md`: 16 Sept, Lemma 1, Theorems 2 and 3.
- `split_zero_history…/note.tex` L298 and L440–442: H10–H13 at `16fc4dbb817b`.
- `tao_clock_audit/sections/consequences.tex` L3 and L12: α = 1001/1000, Tao Prop. 1.11.
- `completion_defect…/note.md` L7: edge 1a, zeta `DERIVED_MATHEMATICS.md` §§1–4.
- The Hurwitz function occurs only in the three places named in §2.6 (git grep; Ch. 6 L15 only refers back).

**Section 3 (817 `dbd0a93`)**
- README L36–66: credits and scope.
- `problem/statement.md` L18–20 and paper L89–98: Costa's k = 3 answer.
- `notes/general-k-capacity.md` L22, L69 (improvement on Korsky's v1 rates) and L570–572 (citations).
- `interfaces/zeta/workbenches/`: 11 folders and 10 interface notes.

**Section 4 (YM `fa79faf`)**
- `ATTRIBUTION.md` L1–40: Alpöge's announcement of 20 July; Akhil and Fable; S⁶ "circulated by Levent Alpöge and produced with Claude"; the warning about the shared label "Fable".
- `FIFTH_REFERENCE.md` (F26) L251–272: the values match the author's script.
- Fifth-reference README L117: producer and auditor not rerun at publication; no Lean or external certification.
- README L121: the SZH credit (m30).
- `WORKBENCH.md` L21: the continuum question "remains unresolved in this collection".
- `s6/README.md`: the five-page reader, Zenodo 22678442, "does not independently certify".
- `navier-stokes/README.md` L31: validation unfinished.
- Vacuum-hydrodynamics README L5, L50–57, L84, L93–104: Λ = −6/L², the existence argument, marked-data injectivity, the Kasner bijection.
- D1 confirmed: `ATTEMPTS.md` L274 and `research-attempts.json` L918 say 10⁻¹⁹, while L915 says 10⁻¹¹.

**Section 5**
- YM `research-control/check.py` L238–243: edge 19 fixture.
- Collatz Ch. 7 L7: edge 1a.
- 817 interfaces: edge 16.
- The zeta reader: `sec4_twolines.tex` Theorem "the first Hurwitz jet" (a) gives all jets and (c) the nodal set Z − 1; `sec6_other.tex` L98–112 has the Keller-map lemma and the Gram sandwich with δ ≤ 1; `sec8_bridges.tex` L53–75 has the overlaps table.
- `47a` G-ES-7: the pinned-file drift of up to 7 lines (§6).

---

## Checks I ran

All are in `scratchpad/referee21/wb/`, each with an `_OUTPUT.txt`. They use exact integer, Fraction or sympy arithmetic unless marked. Each took under 60 s.

1. `wb_es09_orbits.py`: ES-09 relations; orbits and Riemann–Hurwitz genera for D = 1, 3, …, 15 and D = 2, 4, 6.
2. `wb_es_shells.py`: the R3 and R7 sieves on all 19,564 primes p ≡ 1 (mod 12) below 10⁶; the 989 survivors; the mod-840 classes.
3. `wb_es_count.py`: Theorem 1.1(a) and (b) by brute force for p < 400 (1,710 shells).
4. `wb_es_items_OUTPUT.txt` (inline script): p = 67369 shells; the examples at p = 37 and 373; the witnesses at 37 and 2521; primality of 67369, 7840561 and 87481.
5. `wb_cz_tv.py`: the TV values of Theorem 2.2 at N = 2²⁰.
6. `wb_cz_misc.py`: m* and k (exact); (C37); D_m; the Thm 2.4 example at v = 0 and v ≈ 1.2·10¹⁹; Lemma 2.3 for e ≤ 5000; Prop. 2.6 on a grid of [2, 10⁴] (floating point).
7. `wb_cz_hurwitz.py`: Theorem 2.9 numerically (mpmath, 40 digits). M₁ and M₂ are recovered from the zero motion at ρ₁, and the weights by Vandermonde.
8. `wb_ep_misc.py`:
   - admissibility of the optimal 6-set and the 7-set, and their |T|;
   - the refined n = 7 bound (132) and the table n ≤ 7;
   - the constants c_r and the Korsky-type rates;
   - negative results 1–4 (including {2,7} base 11, lengths 1–4, and B* at bases 71–96 and 71–92);
   - the Pell numbers, A♯, the digit set mod 19, and the f_m and κ_m identities.
9. `wb_g4.c`: an independent exhaustive search for g₄(n), n ≤ 6, with optimal-set counts.
10. `wb_ym_numbers.py` (mpmath, 40 digits): α₅, the threshold, d₅ at 1/64, 4/225 and α₅; monotonicity; χ ∈ [0, ½); the ×2 sensitivity; the Neumann radii; the coefficient signs.
11. `wb_ym_misc.py`: the map F and its curve; Kasner identities and inverse (floating point, 200 random B), surjectivity round trip (200 random data); S6-5 arithmetic and the D₄ determinant.
12. `wb_fibre.py`: a lex Gröbner basis of the fibre F⁻¹(−1/4, 0, 0).
13. `wb_ns_es.py`: J and its eigen-directions; the sharp constant over |k| ≤ 300 (50 digits); the group identity for R ≤ 200; the curvature identity.
14. `wb_rerun_audit_OUTPUT.txt`: the contents of `rerun_20260926/`, the diffs against the first-pass outputs (only timing and exit lines differ), and the PASS-line count (47).
15. The LaTeX log scanned for overfull boxes and missing glyphs. All 26 pages rendered at 80 dpi and inspected; zoomed crops of pp. 6, 10 and 21.
16. Source spot checks with `git show` / `git grep` at the pinned commits, as listed above.
