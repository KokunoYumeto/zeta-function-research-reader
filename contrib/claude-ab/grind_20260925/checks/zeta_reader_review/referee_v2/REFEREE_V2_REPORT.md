# Referee report on version 2 of *The split-zero programme around the Riemann zeta function: a reader of its results, with proofs*

**Referee.** An independent Claude instance (claude-opus-5-5), 26 September 2026. I did not write the reader, the notes, the addendum `48_`, the review or the verification of the minor items.

**What I read.**
- All of version 2: `reader_v2/*.tex`, and `reader.pdf` (57 pages) through `pdftotext` and page renderings.
- Every diff hunk between version 1 and version 2.
- The addendum `48_`, the review report and its outputs, the verification report, and the author's checks `zeta_reader_addendum_checks.py`.
- Every note locator cited in a changed status line: `11_`, `16_`, `24_`, `26_`, `29_`, `31_`, `33_`, `42_`, and the register `00_` S23 and S73–S79.

**Conventions.**
- Statement numbers are those of version 2, taken from `reader_v2/reader.aux`.
- The new Proposition 2.8 moves version 1's Lemmas 2.8–2.9 to 2.9–2.10. Nothing else is renumbered.
- `file:line` refers to `reader_v2/`.
- Scripts and outputs are in this folder (table at the end). None imports the review's or the author's scripts.

---

## Summary

- **Version 2 applies the addendum faithfully.**
  - I re-derived every new or changed proof.
  - I found no false theorem, and no theorem with a missing hypothesis.
  - Apart from one intermediate bound in a proof (m1), every number I recomputed agrees with the reader, among them: the Carleman ratios 1.0597/1.0196/1.0061, t* = 0.121196, the Jensen threshold 0.38075, the k = 3 poles, 8.79194 and 21.19445, the constant 1.0342, the signature (n_on + n_pairs, n_pairs), the on-line determinant p^m, and 1.236·10¹³.
  - Nothing true in version 1 was lost or weakened.
- **Three major findings.**
  - **M1 (understatement).** Carleman's formula in the angle |arg w| < π/4 halves the new density threshold for {2^a3^b}, to (log 2)(log 3)/(4π) = 0.06060.
    - The proof uses only the reader's own growth bound.
    - Open question 5 is therefore open only for 0 < t ≤ 0.0606, not for 0 < t ≤ 0.1212.
  - **M2 (credit).** The version-2 generalisations were stated and proved in the independent reviewer's report.
    - The front matter still says that two Claude instances contributed results.
    - Most status lines and catalogue rows credit only "version 2", and the register credits claude-ab.
  - **M3 (overstated verification record).** Appendix B says that the author re-derived every finding, and that the minor ones were also checked by a second instance.
    - The addendum and Appendix C say that the author verified only O1–O4 and F1–F5.
- **Thirteen minor findings:**
  - a numerical slip in the proof of Lemma 3.6;
  - an overstated clause about Theorem 4.1(d) (it holds at a = ½);
  - Proposition 2.8's left side holds for every q with φ(q) > 2, not only for prime q ≥ 5 (an understatement);
  - inconsistent labels and missing "not re-read" caveats;
  - stale summaries, a stale locator, and wording and typography.

---

## Major findings

### M1. Proposition 3.11 and open question 5: the Carleman threshold for {2^a3^b} can be halved *(direction: understatement / missed generalisation)*

**Location.**
- §3.4, Proposition 3.11: the statement at `sec3_quotient.tex:201–207` ("exactly when" at :206), proof step 3 at :215, step 6 at :221.
- §9, open question 5 (`sec9_open.tex:10`).
- §8, the Nyman–Beurling bullet (`sec8_bridges.tex:11`).
- Appendix A, row S75 (`appA_catalogue.tex:93`).
- Appendix B.4, "Stronger statements" (`appB_corrections.tex:39`).

**Problem.**
- The reader proves that the family is dense for t > (log 2)(log 3)/(2π) = 0.12120.
- It says the question remains open for 0 < t ≤ 0.12120, "where Carleman's formula is inconclusive".
- That is true only of Carleman's formula in the half-plane. The same formula applied to L(z^{1/2}), which is Nevanlinna's formula for the angle |arg w| < π/4, gives density for every t > (log 2)(log 3)/(4π) = 0.060598.
- The argument uses only the reader's step 2 bound, log|L(u+iv)| ≤ v²/(4t) + (1+A)|u| + M log(2+|v|) + C′.

**Derivation.**
- *Setting.* Let F(z) = L(z^{1/2}), with the principal branch, on the half-annulus ρ₀² ≤ |z| ≤ R, Re z ≥ 0; put X = R^{1/2}.
  - F is analytic there, since L is entire.
  - The zeros of F include (log n)² for n ∈ S, on the positive axis.
- *Carleman's formula for F.* It reads Σ_j(1/|z_j| − |z_j|/R²)cos(arg z_j) = arc + axis + O(1). This is the reader's step 3 with L replaced by F.
- *Arc.* For z = Re^{iψ} we have w = R^{1/2}e^{iψ/2} and v² = R sin²(ψ/2).
  - So log|F| ≤ R sin²(ψ/2)/(4t) + O(R^{1/2}).
  - Hence arc ≤ (1/(4πt)) ∫_{−π/2}^{π/2} sin²(ψ/2) cos ψ dψ + o(1) = (1 − π/4)/(4πt) + o(1) = O(1).
- *Imaginary axis.* F(±iy) = L(y^{1/2}e^{±iπ/4}), so v² = y/2.
  - So log|F(iy)F(−iy)| ≤ y/(4t) + O(y^{1/2}).
  - Hence axis ≤ (1/2π)∫_{ρ₀²}^{R}(y^{−2} − R^{−2})(y/(4t))dy + O(1) = (log R)/(8πt) + O(1) = (log X)/(4πt) + O(1).
- *Zero side.* It is at least Σ_{n∈S, log n<X}((log n)^{−2} − (log n)²X^{−4}); every other zero adds a nonnegative term.
- *Criterion.* So L ≢ 0 forces Σ_{log n<X}((log n)^{−2} − (log n)²X^{−4}) ≤ (log X)/(4πt) + O(1).
- *The lattice.* Partial summation, with the boundary term 0 at x = X, gives Σ = ∫ν(x)(2x^{−3} + 2xX^{−4})dx = 2κ log X + O(1), with κ = 1/(2 log 2 log 3).
  - The contradiction therefore holds for every t > 1/(8πκ) = (log 2)(log 3)/(4π).
  - Steps 4–6 of the reader's proof then apply unchanged, giving density in ℬ, in I_ζ, and for larger t.
- *Optimality within the family.* For the angle |arg w| < π/(2k), 0 < k ≤ 2, the same computation gives the threshold t > 1/(4πκk).
  - It rests on the identity (4 − k²)∫_{−α}^{α}sin²φ cos kφ dφ + 2k sin²α = 4/k, with α = π/(2k).
  - The threshold decreases in k, and k = 1 is the reader's half-plane.
  - For k > 2 the zero sum Σ x_n^{−k} converges for quadratic counting, so no contradiction arises.
  - Hence π/4 is the best angle.
- *The phrase "exactly when".* In Proposition 3.11 ("…for S = {2^a3^b} exactly when t > 0.12120…"), this refers to the displayed half-plane condition. It is correct for that condition, but a reader can take it as the threshold of density, which is not proved.

**Evidence.**
- `r01_carleman_lattice.py`:
  - the identity above holds for k from 0.5 to 2 (error 4·10⁻³¹);
  - C₂(X) − 2κ log X = 3.1657, 3.1892, 3.1951, 3.1961 at X = 50, 200, 800, 1600 (bounded);
  - the thresholds are 0.12120 (k = 1), 0.08080 (k = 1.5), 0.06379 (k = 1.9) and 0.060598 (k = 2).
- `r02_angle_formula_check.py` checks the π/4-angle form of the formula, including the factor 1/π on the ray term, on a test function whose zeros lie on the positive axis:
  - the test function is f(w) = sin(π(w² − ½))e^w(w + 2), which has Gaussian growth in the imaginary direction;
  - the remainder is −4.504353, −4.504271, −4.504257, −4.504253, −4.504252 at R² = 16, 36, 64, 100, 144, so it converges;
  - over the same range the zero side grows by 2.2.
- `r02b_ray_growth.py` computes an explicit L(w) = Λ(K_w) for the functional Λ(F) = Σ_{|k|≤400}F(ik)/(1+k²):
  - on the ray arg w = π/4, log|L| − r²/(8t) − r cos(π/4) stays negative for r ≤ 60;
  - so the constant 1/(8t) on the rays is the one the argument uses.

**Proposed fix.**
- *Proposition 3.11, statement.* Replace the sentence "This holds for every t if … larger t." with:
  > "The same conclusion holds if limsup_{X→∞}(1/log X)Σ_{n∈S, log n<X}((log n)^{−2} − (log n)²/X⁴) > 1/(4πt). Both conditions hold for every t when ν_S(R)/R² is unbounded, as for S = {2,3,…} or for the d-th powers. For S = {2^a3^b : a+b ≥ 1} the first condition holds exactly when t > (log 2)(log 3)/(2π) = 0.12120…, and the second exactly when t > (log 2)(log 3)/(4π) = 0.06060…, so this family is dense for every t > 0.06060. Density for one t implies density for every larger t."
- *Proof, after step 3.* Add a step 3′ with the derivation above, in five lines.
- *§9, open question 5.* Replace the second and third sentences with:
  > "Version 1 left this open. Carleman's formula in the half-plane gives density for t > (log 2)(log 3)/(2π) = 0.12120…; applied to L(z^{1/2}), that is, in the angle |arg w| < π/4, it gives density for every t > (log 2)(log 3)/(4π) = 0.06060… (the Jensen argument needs t > 0.381). The question remains open for 0 < t ≤ 0.06060, where the angle formulas are inconclusive for every angle."
- *Other places.*
  - §8: replace "when t > 0.1212" with "when t > 0.0606".
  - S75: replace "t > (log 2)(log 3)/(2π)" with "t > (log 2)(log 3)/(4π)".
  - Appendix B.4: replace "which answers open question 5 for t > (log 2)(log 3)/(2π)" with "…for t > (log 2)(log 3)/(4π)".
- *Credit.* Record this step as the referee's (version 2 referee pass), to be checked like the other version-2 items.

### M2. Credit for the version-2 results *(direction: wrong or incomplete credit)*

**Location.**
- Front matter, "Who did what" (`sec0_front.tex:26–30`) and "Status labels" (:32–40).
- The status lines of:
  - Theorem 4.1 (`sec4_twolines.tex:18`);
  - Lemma 3.13 (`sec3_quotient.tex:249`);
  - Proposition 3.11 (:208);
  - Theorem 2.3 (`sec2_sheets.tex:65`) and Corollary 2.4 (:87);
  - Proposition 5.1 (`sec5_deligne.tex:14`).
- Appendix A, rows S73–S79 (`appA_catalogue.tex:91–97`).
- The register `00_`, rows S73–S79 (register lines 94–100).

**Problem.**
- *Who produced these results.* The review report states and proves each of the five major generalisations: for F1–F5 it gives a "Stronger statement" and a "Proof".
  - The addendum `48_` §0 describes the author's role as verification: claude-ab verified O1–O4 and F1–F5, "re-deriving each proof".
  - The left side of Proposition 2.8 is the review's F7. The verifier corrected its quantifiers.
- *How the reader credits them.*
  - The status lines say "version 2's (… after an independent review …)".
  - Only row S75 names "the reviewer's proof". Rows S73, S74, S76 and S77 say "proved; version 2".
  - The register credits S73–S77 to "claude-ab, after an independent review", and credits S78 to "the independent verifier".
- *The front matter.*
  - It still says that two Claude instances contributed results, claude-ab and the copy.
  - It says each result is labelled programme, copy or claude-ab. "Version 2" is none of these.

**Evidence.**
- Review report, sections F1–F5, the "Proof" bullet of each; F7, "Stronger statement".
- `48_` lines 9–11 and §2.1–2.5 ("Status: proved here").
- `sec0_front.tex:28–29`; `appA_catalogue.tex:91–97`; register lines 94–99.

**Proposed fix.**
- *"Who did what".* Add:
  > "Version 2 adds results found by two further Claude instances that wrote neither the reader nor the notes: the reviewer of version 1, whose report states and proves the stronger forms F1–F22, and a verifier of the minor items F6–F22, who corrected six of their wordings. claude-ab re-derived F1–F5 and O1–O4. A status line that calls a statement 'version 2's' credits the review, and the verification where stated."
- *"Status labels".* Add the label *review* (version 2).
- *Catalogue rows.*
  - S73: "the review's F1, re-derived by claude-ab". Likewise S74 (F2), S76 (F4) and S77 (F5).
  - S78: "the review's F7, with quantifiers corrected by the verifier; conditional on [40]".
  - S79: "the review's F17, corrected by the verifier".
- *Register.* Correct the credit column of `00_` in the same way.

### M3. Appendix B.4 overstates who verified the review's findings *(direction: overstated verification record)*

**Location.** Appendix B.4, first paragraph (`appB_corrections.tex:29`).

**Problem.**
- The paragraph says the review's findings were verified by the author of the reader, who "re-derived each proof", and that "the minor ones" were checked "also by a second independent instance".
- This implies that every finding, F6–F22 included, was re-derived twice.
- In fact:
  - the author verified O1–O4 and F1–F5 (checks Z1–Z6);
  - the seventeen minor findings were verified once, by the second instance.
- Mathematically this matters little. It is a claim about the verification record, and the appendix contradicts Appendix C of the same document.

**Evidence.** `48_` §0, items 2–3 (lines 10–11); `appC_verification.tex:42`, which states the division correctly.

**Proposed fix.** Replace the sentence with:
> "The author of this reader verified its four overclaims and five major findings against the sources, re-deriving each proof, with independent checks (Z1–Z6); a second independent instance verified the seventeen minor findings with checks of its own (`48_`; `checks/zeta_reader_review/verify_minors/`)."

---

## Minor findings

**m1. The proof of Lemma 3.6 contains a numerical slip.**
- *Location:* `sec3_quotient.tex:104`.
- *Problem:* the proof says (1+x)/(½+x) has "value at most 15.14/14.64 < 1.0342 at x ≥ γ₁". The function decreases in x, so its maximum on x ≥ γ₁ is (1+γ₁)/(½+γ₁) = 1.0341653. The stated value 15.14/14.64 = 1.0341530 is smaller than that maximum, so the stated bound is false for γ₁ ≤ x < 14.14. The final constant 1.0342 is right.
- *Evidence:* `r11_misc.py` (a).
- *Fix:* replace the clause with "…and for x ≥ γ₁ = 14.1347… it is at most (1+γ₁)/(½+γ₁) = 1.03417… < 1.0342."

**m2. The remark after Theorem 4.1 says that part (d) "does not extend to other sheets"; at a = ½ it does hold.** *(overstated)*
- *Location:* `sec4_twolines.tex:27`. The register S73 repeats the claim.
- *Problem:* the a = ½ example shows only that Theorem 4.2 fails there, since the zero set is not #-symmetric. Part (d) itself holds at a = ½.
  - The zeros of ζ(s, ½) = (2^s − 1)ζ(s) are 2πik/log 2 (k ∈ ℤ, including 0), −2k, and ρ.
  - Translated by −1, these give −1 + 2πik/log 2, −2k−1 and ρ − 1.
  - At all of these, (2^s − 1)ζ(s) ≠ 0. The reason is that ζ has no zeros on Re s = −1, at odd negative integers, or in −1 < Re s < 0, and |2^{ρ−1}| < 1.
- *Evidence:* the derivation above, and `r11_misc.py` (e). The minimum of |ζ(z−1, ½)| over the listed zeros z is 3.8·10⁻³, attained at z = −4.
- *Fix:* replace "Part (d) and Theorem 4.2 use … do not extend to other sheets:" with "Theorem 4.2 uses the functional equation of ζ and does not extend to other sheets:". Add after the example: "(Part (d) is proved from the functional equation and is not claimed for other sheets; at a = ½ it holds.)"

**m3. Proposition 2.8's left side holds for every q with φ(q) > 2, not only for prime q ≥ 5.** *(understatement)*
- *Location:* the statement (`sec2_sheets.tex:131`), the proof (:136–138), and S78.
- *Derivation.*
  - Group k by d = gcd(k, q). This gives Φ_{1/q}(s) = Σ_{d|q} d^{−s} Σ_{χ mod q/d} c_{d,χ}L(s, χ), with c_{d,χ} = (2/φ(e))τ(χ̄) for even χ (e = q/d) and 0 for odd χ.
  - Writing each χ through its primitive ψ gives Φ_{1/q} = Σ_ψ P_ψ(s)L(s, ψ) with Dirichlet polynomials P_ψ.
  - *The representation is unique.* Take the least integer d₀ in the supports. For large primes p, the coefficient at d₀p is Σ_ψ b_{ψ,d₀}ψ(p). Distinct primitive characters are linearly independent on the primes, by Dirichlet's theorem.
  - *The ζ-component is nonzero.* Its coefficient at q^{−s} is 2Σ_{e|q squarefree}1/φ(e) > 0.
  - *Some nontrivial component is nonzero.* Otherwise Φ = P₁ζ, and then 2cos(2πp/q) = 2cos(2π/q) for every large prime p. Every class coprime to q would then be ±1, so φ(q) ≤ 2.
  - Hence Φ_{1/q} is not of the form P·L(s, χ) whenever φ(q) > 2, and the rest of the proof is unchanged.
- *Evidence:*
  - `r12_phi_components.py`: the decomposition reproduces Φ_{1/q} to 6·10⁻¹¹. For every q ≤ 40, a nontrivial component exists exactly when φ(q) > 2, and the ζ-component is always nonzero.
  - `r15_z18_left_zeros.py` locates zeros of Z_{1/8} and Z_{1/12} in 0 < Re s < ½, for example 0.2527 − 7.8196i and 0.2285 − 6.5307i, reflected from zeros of Φ_{1/q}.
- *Fix:*
  - In the statement, replace "If q ≥ 5 is prime, the same holds" with "The same holds".
  - In the proof, replace the prime-q computation with the three bullets above.
  - In S78, replace "q ≥ 5 prime" with "φ(q) > 2".

**m4. The Saias–Weingartner theorem has three different statuses.**
- *Location:* Proposition 2.8's status (`sec2_sheets.tex:133`); Proposition 2.6, step (iv)⇒(ii) (:115) and its status (:109); Proposition 2.7; S78; the front matter labels (`sec0_front.tex:32–40`).
- *Problem:*
  - Proposition 2.8 is "Conditional on the theorem of Saias and Weingartner", which is not one of the defined status labels.
  - Propositions 2.6–2.7 use the same theorem, citing "their Theorem 4", and are labelled as proved.
  - The verification report notes that the theorem number is not visible in the abstract, the only text read.
- *Fix:* give all three one status, for example "Proved here, using Saias–Weingartner [40] as stated in its abstract (theorem number and printed statement not checked)", and drop "Theorem 4" or mark it unverified.

**m5. Several extensions omit the caveat that their standard inputs were not re-read.**
- *Location:*
  - Theorem 3.9's sentence on L(s, χ) (`sec3_quotient.tex:147`, status :149);
  - the paragraph on L(s, χ) after Corollary 4.7 (`sec4_twolines.tex:129`);
  - Proposition 3.11's status, for Carleman's formula (:208).
- *Problem:*
  - `48_` §5 says that the L(s, χ) inputs (Davenport, Ch. 16) for F13, F17 and F19, and Titchmarsh's statement of Carleman's formula, were not re-read.
  - Only the Dedekind paragraph says so.
  - The L(s, χ) carry-over of Theorem 3.9 is an outline ("with the evident changes") inside a statement labelled "Proved here".
- *Fix:*
  - Theorem 3.9 and the L(s, χ) paragraph: add "(an outline; the L-function inputs (D1), (D2) and good heights were not re-read, `48_` §5)".
  - Proposition 3.11: add "(Titchmarsh's statement was not re-read; the form of the formula was checked numerically, `48_` §5)". My `r02` also checks the angle form numerically.

**m6. The proof of Lemma 3.3 is garbled at one point.**
- *Location:* `sec3_quotient.tex:50`.
- *Problem:* "since x ranges over the image of (L−λ)^m" should say that (L−λ)^m is onto, so every y equals (L−λ)^m x for some x.
- *Fix:* "…has zero m-jet at λ; since (L−λ)^m is onto ℬ/I_D, every H(y) has zero m-jet at every such λ, so H(y) ∈ I_{D″}."

**m7. δ is undefined in the Corollary B bullet.**
- *Location:* `sec2_sheets.tex:33`.
- *Fix:* write "Δ ≥ (1+δ)√(2 log T₂)/log 2 for a fixed δ > 0". The same applies to O3 (`appB_corrections.tex:35`).

**m8. The addendum's locators use version-1 numbering.**
- *Location:* the status lines of Lemmas 2.9 and 2.10 (`sec2_sheets.tex:157`, :166), which cite "`48_` §3, F8".
- *Problem:* that row of `48_` names "Lemmas 2.8–2.9", which are version 1's numbers. In version 2, 2.8 is the new Proposition 2.8.
- *Fix:* in Appendix B.4, add "`48_` and the review use version 1's numbering; version 1's Lemmas 2.8–2.9 are Lemmas 2.9–2.10 here."

**m9. Theorem 2.3 omits the infinitude of divisor-minimal elements, and Appendix B's "applies all of them" is slightly too strong.** *(understatement)*
- *Location:* `sec2_sheets.tex:63`, :65; S76; `appB_corrections.tex:29`.
- *Problem:*
  - The register S76 and `48_` §2.4 state two things the theorem omits:
    - in every M_H with H ≠ G there are infinitely many elements satisfying (b);
    - n = pp′rr′ has r_n = −1 or −2, for example r = −2 at 3·7·11·19 in the Hilbert monoid.
  - The review's Jensen criterion (J) is not included either, so "applies all of them" is slightly too strong.
  - The −½ bound for M_H is proved only in the status line, not in the proof.
- *Evidence:* `r10_formal_log.py`:
  - r = −2 at 4389 = 3·7·11·19, with three factorizations;
  - the formula r_n = 1 − j + ε, and the bound ≤ −½ for j ≥ 2, hold at 1493, 1874, 1589 and 1141 divisor-minimal elements of four congruence monoids.
- *Fix:* add to Theorem 2.3 "In every M_H with H ≠ G infinitely many n satisfy (b): for primes p ≠ r in a class c ∉ H and p′ ≠ r′ in c^{−1}, n = pp′rr′ has r_n = −1, or −2 if c² ∈ H." Move the one-line proof of the −½ bound into the proof. Write "applies them" in place of "applies all of them".

**m10. Some summaries were not updated for version 2.**
- *Location:* N-Unif4 (`sec7_negative.tex:48`); S44 (`appA_catalogue.tex:60`); S6 (:22).
- *Problem:*
  - N-Unif4 and S44 still restrict the splitting to Dirichlet L-functions, though the Dedekind paragraph extends it.
  - S6 still says Theorem D is proved "assuming" simplicity on the line, though the §2.1 bullet now states that the hypothesis holds for n ≤ 1.2·10¹³.
- *Fix:* add "and (§4.6) every Dedekind zeta function" to N-Unif4 and S44. Add to S6 "(the hypothesis holds for n ≤ 1.2·10¹³)".

**m11. Lemma 5.6 can take a weaker hypothesis.** *(understatement)*
- *Location:* `sec5_deligne.tex:92`.
- *Problem:* the proof uses δ_n ≤ CD^n only through δ_n = o(R^n) for every R > D. So limsup_n max(δ_n, 0)^{1/n} ≤ D suffices; for example δ_n = n^A D^n is allowed.
- *Fix:* "…real δ_n with limsup_n max(δ_n,0)^{1/n} ≤ D (for example δ_n ≤ CD^n)…".

**m12. A parenthesis in Appendix C reads ambiguously.**
- *Location:* `appC_verification.tex:46`.
- *Problem:* "(47 of them with a recorded _OUTPUT.txt)" now follows the parenthesis about version 2, so it reads as a count of the version-2 scripts.
- *Evidence:* the counts themselves are right: 49 scripts and 48 outputs at the top level of `checks/`, with `z15_scan.py` the one without output.
- *Fix:* "48 scripts in checks/ for version 1 (47 of them with a recorded _OUTPUT.txt); version 2 adds …".

**m13. Typography.**
- *Location:* the title of §8.3 (`sec8_bridges.tex:41`), "The $\mathbb{F}_1$ context".
- *Problem:* the maths in the title produces the four hyperref "Token not allowed" warnings in the PDF bookmark. This was already so in version 1.
- *Fix:* use `\texorpdfstring{$\mathbb{F}_1$}{F1}`.
- *PDF check otherwise:* there are no undefined references, no "??", and no replacement or private-use glyphs. Overlines render correctly on the checked pages 10, 17, 19, 21, 50 and 52. The underfull boxes rose from 81 to 88, which is cosmetic.

**Notes on sources (not findings against the reader).**
- `48_` §2.2 describes check Z2 as run on a "#- and conjugation-stable configuration". The script omits the conjugates of ½ + 40i and ½ + (40 + 2π/log 2)i, so the configuration is only #-stable. The conclusion stands: `r09` uses a configuration that is both #- and conjugation-stable, and finds the 20 entries (ρ, ρ#) for n ∈ {2, 3} and 32 for n = 2.
- Anyone re-checking the a = ½ remark should know that mpmath's default `zeta(s)` is ill-conditioned exactly at s = 1 + 2πik/log 2: it divides by 1 − 2^{1−s}, and its value drifts by about 10⁻⁶ with the working precision. The Hurwitz evaluation, or `method='euler-maclaurin'`, gives the stable value 1.3465795 + 0.1098831i. The review's |ζ(1 − s̄₁, ½)| = 1.351 is correct.

---

## What I verified and found correct

Each item below was re-derived by hand, and checked by script where marked.

**§2**
- **Corollary 2.2** (normalised sheet). (½)^sζ(s, ½) = (1 − 2^{−s})ζ(s), the Euler product over the odd primes. The correction O2 is accurate. [r11 c]
- **Theorem 2.3 and Corollary 2.4** at elements whose proper M-divisors factor uniquely.
  - Each entry of a k-tuple (k ≥ 2) is a proper M-divisor, which is the only use of the hypothesis.
  - In the corollary, N′ = a^{j₁/g} = b^{j₂/g} is a proper M-divisor of N = N′^g.
  - The −½ bound for M_H, via u = w^{b′}, v = w^{a′} with w ∈ M_H, holds.
  - The converse is correct in ⟨c^u, c^v⟩. [r10]
- **Example 2.5** is zero-free on the whole half-plane Re s > 0. **Proposition 2.6**'s Dirichlet-free step (CRT plus pigeonhole, A₀A₂ = A₁²) is correct. [r11 h]
- **Proposition 2.8** (given Saias–Weingartner as read).
  - Hurwitz's formula summed over a and 1 − a gives Z_a(1 − s) = 2Γ(s)(2π)^{−s}cos(πs/2)Φ_a(s).
  - The character expansion for prime q holds (τ(χ₀) = −1, |τ| = √q).
  - At nonreal zeros with Re s₀ > 0, the Gamma–cosine factor is finite and nonzero.
  - The O(1) real zeros are absorbed into the counts. [r12, r15; see m3]
- **Lemma 2.9** (complex C_j, and L(s − σ_j, χ)) and **Lemma 2.10** (μ = ην with η^d = 1) are correct.

**§3**
- **Proposition 3.2 and Lemma 3.3** for D ≤ div Φ (Φ_λ, U, U_ρ) are correct.
- **Lemma 3.4** with the terms x^k e^{ρx} is correct: Fubini holds because |v|^k ≤ k!R^{−k}e^{R|v|}, and the jets are realised by G(s−ρ₀)^{−m}P.
- **Lemma 3.6** (|β| ≤ 3/2, factor ((1+|γ|)/(½+|γ|))^M) is correct, apart from m1.
- **Corollary 3.7** (J(Q) dense in Λ_m) and **Theorem 3.9(b′)** (the cycle (d)⇒(b′)⇒(b)) are correct.
- **Proposition 3.11**: all six steps are correct.
  - L is entire (the ℬ-valued power series), and step 2's bound holds with a Λ-independent 1/(4t).
  - The Carleman constants 2/3 and R/(6πt) are right; the "other terms" are in fact O(1).
  - (∂_w − 1)K_w = g_te^{(1−s)w}, and the Bochner integral is justified.
  - g_tℬ is dense, with |h_N| ≤ e^{2tσ²}; the ideal case follows by Hahn–Banach.
  - ∫ν(x)(x^{−2} + R^{−2})dx = (4/3)κR + O(log R); monotonicity in t holds.
  - [r01: ratios 1.05974, 1.01959, 1.00606 at R = 100, 400, 1600, identical to Z3; t* = 0.121196]
- **Proposition 3.12** (infinite codimension; I_D for F = ∅) is correct. [r11 g]
- **Lemma 3.13** is correct.
  - (n^{ρ+η̄−1} − 1)B_{ρη} = 0, and (2πi/log 2)ℤ ∩ (2πi/log 3)ℤ = {0}.
  - |b_ρ| ≤ ‖B‖ uses m_{ρ#} = m_ρ; the converse holds for all n > 0.
  - An off-line block has eigenvalues ±m|b|; the single-n aliasing and the "In particular" clause hold. [r09]
- **The residue-duality constant** is correct: ζ(2)(1/π + 8π/5) = 8.79194; the Re s = −1 bound 4π²ζ(2)(1+|t|)^{−3/2} holds (maximum ratio 0.444); and B(P(L)x, y) = B(x, P(1−L)y). [r11 b]

**§4**
- **Theorem 4.1** on every sheet is correct.
  - The factor (s)_m cancels the pole at 1 − m, where the product equals −(m−1)!.
  - sζ(s+1, a) = 1 at s = 0, and the divisors are as stated in the whole plane.
  - The simple zeros at 0, …, 2 − m follow from ζ(m − j, a) > 0.
  - The jet vanishes at s₀ − 1 for s₀ = 1.40778804065 + 23.3279877546i. [r11 d]
- **The a = ½ counterexample** to #-symmetry is correct (see m2 for the clause about (d)).
- **Proposition 4.3** (one dilation) and **Lemma 4.13** (the monotonicity has the sign of r − t) are correct.
- **Proposition 4.6(c)** is correct: the cross block vanishes identically, and the signatures (n_on + n_pairs, n_pairs) on V₊ and (n_pairs, n_on + n_pairs) on V₋ hold. Maximality under RH follows by subtracting the V₊ component, and #-closure is needed. [r07]
- **The L(s, χ) paragraph** rests on Λ(1 − s̄, χ) = W(χ)·conj(Λ(s, χ)), which follows from the two identities it cites.
- **Proposition 4.10** for every modulus is correct: the principal character cancels. [r14: q = 7, 9, 11, 16]
- **The Dedekind paragraph** is correct: Γ_ℝ(1−s)Γ_ℝ(1+s) = 1/cos(πs/2) and Γ_ℂ(1−s)Γ_ℂ(1+s) = s/(π sin πs), and the rate is e^{−nπ|t|/2}. [r06]

**§5**
- **Proposition 5.1** in every degree is correct: convergence at some σ₁ < 1 + kβ_max would contradict the pole at 1 + kρ, which has residue c_w > 0.
- **Its k = 3 example** is correct: poles at 3.1 ± 10i (residue 3) and 3.1 ± 30i (residue 1), and no real pole. [r03]
- **Proposition 5.2** is correct: an off-line zero gives rank 4m and determinant p^{2m}; an on-line zero gives rank 2m and determinant p^m. [r08]
- **Lemma 5.5** (real-valued ν; the ℤ/3 example, positive exactly when x ≤ ½) and **Lemma 5.6** (δ_n ≤ CD^n) are correct. [r04]

**§6**
- **Proposition 6.2** (every integer a ≥ 2) is correct.
- **Lemma 6.4** (real a > 1) is correct, including the a = 3/2, ρ = 0.55 + i example and the collision clause. [r05]
- **Lemma 6.6** (C¹ fields) is correct; it is checked exactly with a cubic non-affine V. [r13]

**§7–§9, the appendices and the front matter**
- N-W2 and N-Pos1 agree with Proposition 5.1 and Lemma 3.13. The question in §9 agrees with Proposition 3.11 as written (but see M1).
- In Appendix A, rows S73–S79 agree with the statements (but see M2 and m3).
- In Appendix B, O1–O4 are accurate, and the counts and lists match `48_` (but see M3).
- The counts in Appendix C are correct (but see m12).
- In the front matter, "more than twenty statements" is accurate: at least 27 numbered statements were strengthened. The date and version line are consistent.
- **Nothing lost.** Every version-1 statement that version 2 generalises is contained in the new form. No version-1 claim was dropped without replacement.
- **Locators.** Every note locator in a changed status line was found in the note it cites:
  - `11_` L. 11.2 and S23;
  - `29_` §1, ETR2 and 29.N1;
  - `26_` §2.1;
  - `24_` L. 24.5(b);
  - `42_` P. 42.2(c);
  - `16_` §1 item 3;
  - `31_` L. 31.1;
  - `33_` L. 33.4.

---

## Scripts

All scripts are in this folder, each with `<name>_OUTPUT.txt`. They use Python 3 with mpmath (25–40 digits), sympy, numpy and exact `Fraction` arithmetic, and all end with ALL CHECKS PASS.

| Script | Reader item | What it checks | Result |
|---|---|---|---|
| `r01_carleman_lattice.py` | Prop 3.11, §9 Q5, M1 | ν(x) = κx² + O(x) for {2^a3^b}; the Carleman sum is (4/3)κR + O(log R); t* = 0.121196; Jensen threshold 0.38075; step-3 constants; the angle identity (4−k²)I₁ + 2k sin²α = 4/k; the angle sums C_k and C₂ = 2κ log X + O(1); angle thresholds, down to 0.060598 | pass |
| `r02_angle_formula_check.py` | M1 | Carleman's formula in the angle \|arg w\| < π/4, with its weights and ray factor, on f(w) = sin(π(w²−½))e^w(w+2); the remainder converges to −4.50425 | pass |
| `r02b_ray_growth.py` | M1 | explicit L(w) = Λ(K_w): growth ≤ r²/(8t) + r cos(π/4) + O(log r) on the ray arg w = π/4; v²/(4t) on the imaginary axis | pass |
| `r03_abscissa_k3.py` | Prop 5.1 | the k = 3 grouping; rightmost poles 3.1 ± 10i and 3.1 ± 30i with residues 3 and 1; no real pole; the identity at s = 6; even k gives a real pole | pass |
| `r04_Z3_intpos.py` | Lemma 5.5 | ℤ/3 multiplicities; positive exactly when x ≤ ½ (violated at (1,1,1)); the ℤ/2 exception | pass |
| `r05_escape_pair.py` | Lemma 6.4 | the a = 3/2 returning pair (exact); no pair for a ≥ 2, and the band for 1 < a < 2; an irrational collision ratio; the critical-line clause | pass |
| `r06_dedekind_gamma.py` | Dedekind paragraph (§4.6) | the Γ_ℝ and Γ_ℂ identities to 10⁻³⁹; the rate e^{−nπ\|t\|/2} with factor \|t\|^{r₂}; the functional equation of ℚ(i) | pass |
| `r07_chiral_signature.py` | Prop 4.6 | hyperbolic Q_A; V₊ ⊥ V₋; Q_A = ±2Ω; the signatures on V₊ and V₋ (15 configurations); maximality; #-closure needed | pass |
| `r08_det_online.py` | Prop 5.2 | explicit Jordan-block W_p: rank 4m and p^{2m} off the line, rank 2m and p^m on it; average weight 1 | pass |
| `r09_transfer_forms.py` | Lemma 3.13 | a #- and conjugation-stable configuration with multiplicities: entries (ρ, ρ#) for {2,3}, {3,5}, {2,3,5,7}; aliasing for {2} and {2,4}; the converse for real n; the positivity criterion (2000 forms); block eigenvalues | pass |
| `r10_formal_log.py` | Thm 2.3, Cor 2.4 | r_n = ε or 1 − j + ε at every divisor-minimal element of {1 mod 4}, {±1 mod 5}, {1 mod 5}, {1 mod 7} and ⟨4,6,9⟩; ≤ −½ in M_H; r = −2 at 3·7·11·19; first negative coefficients −1/6, −5/12, −7/15, −3/10 in ⟨c^u, c^v⟩ | pass |
| `r11_misc.py` | Lemma 3.6, duality, Cor 2.2, Thm 4.1, Thm D, Props 3.12 and 2.6 | the Lemma 3.6 slip (m1); 8.79194 and 21.19445; the Euler product of the normalised sheet; Thm 4.1 on four sheets, the m = 3 jet and the jet at s₀ − 1; the a = ½ remark, with (d) holding at a = ½ (m2); the zero count 1.2363·10¹³; codimension J; the atoms A_j | pass |
| `r12_phi_components.py` | Prop 2.8 (m3) | the primitive decomposition of Φ_{1/q}; for q ≤ 40, a nontrivial component exactly when φ(q) > 2, and the ζ-component always nonzero; the reflection formula for composite q | pass |
| `r13_keller.py` | Lemma 6.6 | det DF = −2; the three preimages; div U = (div V)∘F and DF·U = V∘F identically for a cubic V; the escaping curve | pass |
| `r14_races.py` | Prop 4.10 | the character identity (principal character cancels); convergence of the correction for q = 7, 9, 11, 16 up to 10⁷ | pass |
| `r15_z18_left_zeros.py` | Prop 2.8 (m3) | zeros of Z_{1/8} and Z_{1/12} in 0 < Re s < ½, reflected from zeros of Φ_{1/q} | pass |

**Comparison with the other passes.**
- The Carleman ratios and t* agree with the author's Z3 and the reviewer's (c).
- The k = 3 poles agree with Z5.
- The signatures and the duality constants agree with the verifier's.
- The only new mathematical content here is M1's angle step and m3's extension to composite q. Both should be checked by the next pass like any other version-2 item.
