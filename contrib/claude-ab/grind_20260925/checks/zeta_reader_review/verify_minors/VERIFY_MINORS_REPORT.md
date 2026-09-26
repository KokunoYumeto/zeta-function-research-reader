# Verification of the MINOR findings F6–F22 of the understatement review of the zeta reader

**Verifier.** An independent Claude instance (claude-opus-5-5). Work done on 26 September 2026. I only read the reader, the notes, the register and the review report. The only files I wrote are the scripts and outputs in this folder.

**Objects.**
- Reader: `reader/sec*.tex` and `reader.pdf`. Numbering and pages were checked against `reader.aux` and against my own `pdftotext` extraction.
- Review: `…/scratchpad/review_zeta_under/UNDERSTATEMENT_REPORT_ZETA_READER.md`, findings F6–F22.
- Notes: `` (`02_`, `03_`, `08_`, `11_`, `15_`, `17_`, `23_`, `24_`, `26_`, `27_`, `28_`, `29_`, `31_`, `32_`, `33_`, `37_`, `40_`, `42_`) and the register `00_`.

**Method.**
- For each finding I read the reader passage and the note it relies on.
- I re-derived the stronger statement myself.
- Where a computation matters, I wrote my own script. I did not import or run the review's scripts.
- Two citation checks were made on the web, both explicitly flagged in the brief (arXiv; no refusals were met):
  - Saias–Weingartner, arXiv:0807.0783, abstract.
  - Platt–Trudgian, arXiv:2004.09765, abstract and PDF text as returned by the fetch tool.

**Result.** 17 findings: **11 CONFIRMED, 6 CONFIRMED WITH CORRECTION, 0 REJECTED.** One sub-item, the Prop 6.5 part of F22, is not an understatement; it is recorded under F22. No finding is mathematically wrong in its main claim. The corrections concern:
- constants and quantifiers (F7);
- what a cited verification actually states (F9);
- the word "verbatim" (F13);
- provenance and one missing hypothesis in the suggested wording (F17);
- one input the review glosses over (F19);
- a clause that does not survive the proposed generalisation (F22).

## Summary table

| # | Reader location | Verdict | One line |
|---|---|---|---|
| F6 | Thm 2.3(b), Prop 2.6, Ex. 2.5 (pp. 7–9) | CONFIRMED | All three refinements are true and in the notes (`11_` L. 11.2 step 7, register S23, `29_` §1, ETR2/29.N1). Checked on 44 congruence monoids: the first negative value is ≤ −½. Caveat: the "every divisor-minimal element" clause rests on F4. |
| F7 | Props 2.6–2.7, q = 5 paragraph, Fig. 2 (pp. 9–10) | CONFIRMED WITH CORRECTION | Saias–Weingartner applies to D_{M_H} (H ≠ G) and, for prime q ≥ 5, to Φ_{1/q}. So Z_{1/q} has ≍T zeros in every strip on both sides of the line. The counts are between c₁T and c₂T, with constants depending on q and the strip, for large T, and a separate η for the reflected strips; "about T" is imprecise. The left-side statement is new. |
| F8 | Lemmas 2.8–2.9 (p. 10) | CONFIRMED | Complex C_j and L(s − σ_j, χ) are fine. μ^{*d} = ν^{*d} ⟺ μ = ων with ω^d = 1. New, elementary. |
| F9 | §2.1 bullets (p. 6) | CONFIRMED WITH CORRECTION | Platt–Trudgian's Theorem 1 states only Re ρ = ½ (up to T = 3 000 175 332 800; lowest 12 363 153 437 138 zeros). Simplicity follows from their sign-change count matched by Turing's method (I(T) = 0). The Corollary B o(1) claim follows from `02_`'s bound only if its O-constants are absolute, and it needs T₁/Δ → ∞ (tied to O3). |
| F10 | Prop 3.2, Lemma 3.3 (pp. 11–12) | CONFIRMED | D ≤ div Φ, Φ ≢ 0 (equivalently I_D ≠ 0) suffices; equivariant maps land in I_{D″}/I_{D′}. New. |
| F11 | Lemma 3.4 (p. 12) | CONFIRMED | Holds for Σ c_{ρ,k}x^k e^{ρx}, k < m_ρ, with Σ\|c_{ρ,k}\|k!R^{−k} < ∞. New. |
| F12 | Lemma 3.6, Cor 3.7 (p. 13) | CONFIRMED | The bound holds for \|Re ρ\| ≤ 3/2, with factor ((1+\|γ\|)/(½+\|γ\|))^M ≤ 1.0342^M at the zeros. J(Q) is dense in Λ_m ⊊ ∏A_ρ. |
| F13 | Thm 3.9 (p. 14) | CONFIRMED WITH CORRECTION | (b′) rapid decay is equivalent. The L(s, χ) version holds, but "with the evident changes", not "verbatim": good heights separately for χ and χ̄, L in place of (s − 1)ζ, q-dependent constants. |
| F14 | Prop 3.12 (p. 16) | CONFIRMED | The closure has infinite codimension, in B and in I_ζ. New. |
| F15 | §3.5, residue duality (p. 17) | CONFIRMED | ζ(2)(1/π + 8π/5) = 8.7919 is valid (`26_` §2.1, register S49). The P(L) form is trivial. |
| F16 | Prop 4.3 (p. 19) | CONFIRMED | Commuting with one U_{a₀}, a₀ ≠ 1, suffices. New. |
| F17 | Prop 4.6, Thm 4.2 (pp. 18–20) | CONFIRMED WITH CORRECTION | V₊ ⊥ V₋ holds unconditionally; the signature is (n_on + n_pairs, n_pairs) on #-closed support; both results hold for primitive L(s, χ). `42_` has the orthogonality only inside its RH clause, and the suggested wording drops "#-closed". |
| F18 | Prop 4.10 (p. 22) | CONFIRMED | Every modulus, every pair (and r-tuple) of classes. Immediate from `42_` 42.4(a). |
| F19 | Prop 4.12 (p. 23) | CONFIRMED WITH CORRECTION | α = nπ/2 is right (checked for n = 2, 3, 4, with both Γ_ℝ and Γ_ℂ). The review omits polynomial growth of ζ_K on strips; the reader's partial-summation step does not supply it. |
| F20 | Lemma 4.13 (p. 23) | CONFIRMED | Increasing iff r > t (`24_` L. 24.5(b)). Omission. |
| F21 | Lemmas 5.5–5.6 (pp. 26–27) | CONFIRMED | Real-valued ν suffices for the bound (a ℤ/3 example shows the dichotomy needs integrality); δ_n ≤ CD^n gives max\|a_j\| ≤ D. |
| F22 | Prop 6.2, Lemma 6.4, Prop 6.5, Lemma 6.6 (pp. 28–31) | CONFIRMED WITH CORRECTION | 6.2 and 6.6: correct. 6.4: the collision clause fails as stated ("ℚ_{>0}") for real a, a′; it becomes "ℝ_{>0}". 6.5: not an understatement, since "if T ⊬ ¬RH then RH" is the contrapositive of the statement's first sentence. |

---

## F6. Three refinements of §2.2–2.3

**Reader.**
- Thm 2.3(b): "This number is at most −1/6".
- Prop 2.6 (i)⇒(ii) chooses primes in prescribed classes "(Dirichlet)".
- Ex. 2.5: zeros of D_{⟨4,8⟩} "lie on Re s=0", and "absence of zeros in Re s>1 does not imply freeness".

**Item 1 (congruence monoids: ≤ −½).**
- *Proof (re-derived).* Suppose u^a = v^b with u ≠ v atoms of M_H.
  - With g = gcd(a, b), u^{a′} = v^{b′}, where gcd(a′, b′) = 1.
  - Comparing prime exponents, b′ | v_ℓ(u). Put w = ∏ℓ^{v_ℓ(u)/b′}; then u = w^{b′} and v = w^{a′}.
  - w is coprime to q, and its class c has c^{a′}, c^{b′} ∈ H. So c = (c^{a′})^x(c^{b′})^y ∈ H with xa′ + yb′ = 1, and w ∈ M_H.
  - An atom is not a proper power of an element of M_H∖{1}, so a′ = b′ = 1 and u = v, a contradiction.
  - Hence every element has at most one pure-power factorization. Also u^k = u^l forces k = l.
- At the least element n₀ with j ≥ 2 factorizations, Thm 2.3(b) gives r = 1 − j + ε with ε ≤ ½, since the one possible pure power has exponent k ≥ 2. So r ≤ −½.
- The clause "r_n ≤ −½ at every divisor-minimal non-factorial element" uses F4's formula r_n = 1 − j + ε at such elements. F4 is a MAJOR finding verified separately; granted F4, the same bound follows.
- *Check* (`v_f6_monoids.py`, exact rationals, n ≤ 6000). In all 44 proper (q, H) with q ≤ 16 that have a negative coefficient below 6000, the first negative value is ≤ −½ and the largest is exactly −½. At all divisor-minimal non-factorial elements (for example 209 of them for q = 5, H = {±1}), r_n = 1 − j + ε holds exactly, r_n ≤ −½, and at most one factorization is a pure power.

**Item 2 (no Dirichlet in (i)⇒(ii)).**
- *Proof (re-derived).* Let c ∉ H and let p₁, …, p_k be primes already found outside H with p_i ∤ q.
  - By CRT choose n > 1 with n ≡ c (mod q) and n ≡ 1 (mod p_i).
  - The classes of the prime factors of n multiply to c ∉ H, so some prime factor lies outside H. It is not among the p_i and does not divide q. So infinitely many primes lie outside H.
  - Finitely many cosets, so some non-identity coset, of order d ≥ 2 in G/H, contains two primes p ≠ r.
  - Then A_j = p^{d−j}r^j (0 ≤ j ≤ d) lie in M_H. They are atoms: a proper M_H-divisor p^u r^v with 0 < u + v < d has class c^{u+v} ∉ H. And A₀A₂ = A₁².
- *Check.* Six (q, H) examples: all A_j are atoms, and A₀A₂ = A₁².
- *Caveat for the wording.* Dirichlet's theorem is still used in the half-factoriality part of Prop 2.6 (primes in the classes c, c^{−1}, or c, d, cd), and Saias–Weingartner in (iv)⇒(ii). "Replace '(Dirichlet)'" applies to the (i)⇒(ii) step only, which is where the reader writes it.

**Item 3.**
- If M is free, r_n ∈ {0, 1/k} and 0 ≤ r_n ≤ 1_M(n). So Σ r_n n^{−σ} ≤ D_M(σ) − 1 wherever D_M converges absolutely, and D_M = exp(Σ r_n n^{−s}) ≠ 0 on the whole half-plane of absolute convergence. This is the reader's own (iii)⇒(iv) argument.
- ⟨4,8⟩ has abscissa 0 and zeros on Re s = 0, so it is zero-free on that whole half-plane and not free.
- The reader's text already implies zero-freeness on Re s > 0. What it lacks is the positive statement for free monoids, which makes the counterexample sharp.

**In the notes?** Yes, all three: `11_` Lemma 11.2 (statement and step 7); register S23 ("at most −½ for congruence monoids"); `29_` §1 (CEI Thm 4.1, ETR3), ETR2 and 29.N1. These are omissions, except the divisor-minimal extension, which is new and depends on F4.

**Suggested wording.** Accurate, with the scope caveat of item 2. Proposed:
- Thm 2.3: "For a congruence monoid M_H with H ≠ G the value is at most −½, since two distinct atoms of M_H have no common power (`11_` Lemma 11.2)."
- Prop 2.6: "…(Dirichlet's theorem is not needed here: by CRT infinitely many primes lie outside H, so some non-identity coset of order d contains primes p ≠ r, and A_j = p^{d−j}r^j satisfy A₀A₂ = A₁²; `29_` §1)."
- Ex. 2.5: "…so D_M is zero-free on its whole half-plane of absolute convergence, Re s > 0, as the zeta function of every free monoid is (ETR2), and yet M is not free."

**Verdict. CONFIRMED.**

---

## F7. Saias–Weingartner on the even sheets

**Reader.**
- Prop 2.6 (iv)⇒(ii) cites Saias–Weingartner's "Theorem 4" for zeros in Re s > 1.
- The q = 5 paragraph ends "checked numerically".
- The Fig. 2 caption says Z_{1/5} "has zeros on both sides of the line".

**What the theorem needs.** Checked from the arXiv abstract of 0807.0783, fetched today:
- a periodic sequence a = (a_n) (complex);
- F_a(s) = Σ a_n n^{−s}, meromorphically continued, **not of the form P(s)L_χ(s)**, with P a Dirichlet polynomial and L_χ a Dirichlet L-function.
- **Conclusion:** there is η = η(a) > 0 such that for all ½ < σ₁ < σ₂ < 1 + η one has c₁T ≤ N_a(σ₁, σ₂, T) ≤ c₂T for sufficiently large T. Here N_a counts zeros with σ₁ < Re s < σ₂ and |Im s| ≤ T, and c₁, c₂ > 0 depend on a, σ₁ and σ₂.
- I read only the abstract. The theorem number "Theorem 4", used by the reader and by `08_`, is not confirmed by it.

**Application to D_{M_H}, H ≠ G.**
- The coefficients are periodic mod q.
- D_{M_H} = [G:H]^{−1}Σ_{χ|_H = 1}L(s, χ) has nonzero components along at least two distinct primitive characters: the trivial one and one inducing a nontrivial χ trivial on H.
- So it is not P·L_χ. A direct argument also works: at large primes a_p = b(1)χ(p) would force a_p ≠ 0, but a_p = 0 on classes outside H. (Uses Dirichlet.)
- Hence D_{M_H}, and Z_{1/q} = q^s D_{M_{±1}} when φ(q) > 2, has between c₁T and c₂T zeros in every strip ½ < σ₁ < Re s < σ₂ < 1 + η with |Im s| ≤ T, for T ≥ T₀.

**Application to Φ_{1/q}, prime q ≥ 5 (re-derived).**
- For gcd(k, q) = 1, e(k/q) = φ(q)^{−1}Σ_χ χ̄(k)τ(χ), so cos(2πk/q) = φ(q)^{−1}Σ_{χ even}τ(χ)χ̄(k). Hence

  Φ_{1/q}(s) = 2q^{−s}ζ(s) + (2/(q−1))Σ_{χ even}τ(χ)L(s, χ̄) = (2/(q−1))(q^{1−s} − 1)ζ(s) + (2/(q−1))Σ_{χ even, χ≠χ₀}τ(χ)L(s, χ̄),

  using τ(χ₀) = −1 and L(s, χ₀) = (1 − q^{−s})ζ.
- For prime q ≥ 5 there are (q − 1)/2 ≥ 2 even characters, all nontrivial ones primitive, with |τ(χ)| = √q ≠ 0.
- So Φ_{1/q} has nonzero components along ζ and along at least one nontrivial primitive character, and is not P·L_χ. A direct check: the prime-coefficient test a_p² = b(1)a_{p²} forces two different values of b(1) on two classes.
- q = 5 gives ½[(5^{1−s} − 1)ζ + √5 L(s, (·/5))]. q = 3 gives (3^{1−s} − 1)ζ, which is excluded, consistent with q = 3 being Eulerian.
- Hurwitz's formula gives Z_a(1 − s) = 2Γ(s)(2π)^{−s}cos(πs/2)Φ_a(s). At a nonreal zero s₀ of Φ with Re s₀ > 0 the prefactor is finite and nonzero, so 1 − s₀ is a zero of Z_a.
- Hence Z_{1/q} has between c₁′T − O(1) and c₂′T + O(1) zeros with 1 − σ₂ < Re s < 1 − σ₁ and |Im s| ≤ T, for ½ < σ₁ < σ₂ < 1 + η′, where η′ = η(Φ_{1/q}) is in general different from η. The O(1) accounts for real zeros.
- Taking σ₁ ≥ 1 gives infinitely many zeros in Re s < 0; taking σ₂ ≤ 1 gives zeros in 0 < Re s < ½.

**Does "c₁T zeros in each strip" follow?** Yes, in each strip inside (½, 1 + η), or its reflection, for T ≥ T₀. The constants depend on q and on the strip. The review's summary phrase "about T zeros" suggests an asymptotic ~T and should be "≍ T".

**Checks** (`v_f7_evensheets.py`, 40 digits).
- The Hurwitz formula holds to 10⁻⁴⁰.
- The character decomposition holds for q = 3, 5, 7, 11, 13 against Z(1 − s), to below 10⁻²⁵; |τ| = √q.
- The not-P·L test gives 2 to 6 distinct forced values of b(1).
- `figures/data/z15_zeros_150.csv`: 90 zeros; 24 with Re > ½, 40 with 0 < Re < ½, 26 with Re ≤ 0; minimum distance from the line 0.006806; max |Z_{1/5}| at the listed zeros 2·10⁻¹⁶.
- Φ_{1/5}(1 − z) vanishes (relative 1.5·10⁻¹⁶) at **all 66** listed zeros with Re z < ½. So Φ_{1/5} has zeros with Re w > 1, as the theorem predicts.

**In the notes?**
- The right-hand side is in `08_` §1 and Appendix A ("The existence of off-line zeros is the theorem of Saias–Weingartner"; zeros with Re s > 1 exist above height 150). That part is an omission.
- The reflection technique appears in `24_` Prop. 24.6, for the Davenport–Heilbronn function.
- The left-side statement for Z_{1/q} via Φ_{1/q} is **new**.

**Corrected wording.**
- Prop 2.7, add: "If φ(q) > 2, Saias–Weingartner give η > 0 such that for all ½ < σ₁ < σ₂ < 1 + η the number of zeros of Z_{1/q} with σ₁ < Re s < σ₂ and |Im s| ≤ T lies between c₁T and c₂T for all large T, with c₁, c₂ depending on q, σ₁ and σ₂. For prime q ≥ 5 the same holds, with another η, in the reflected strips 1 − σ₂ < Re s < 1 − σ₁. The reason is Hurwitz's formula Z_a(1 − s) = 2Γ(s)(2π)^{−s}cos(πs/2)Φ_a(s), where Φ_{1/q} = 2Σ_k cos(2πk/q)k^{−s} has nonzero components along ζ and along every nontrivial even character mod q."
- Caption: "…that Z_{1/5} has infinitely many zeros on each side of the line, and in Re s > 1 and Re s < 0, is a theorem [SW]; the positions shown are computed."

**Verdict. CONFIRMED WITH CORRECTION** (quantifiers and constants; separate η; "about T" → "≍T"; the left side is new).

**Confidence.** Saias–Weingartner read through the abstract only.

---

## F8. Lemma 2.8 with complex exponents and for L(s, χ); Lemma 2.9 without positivity

**Reader.**
- Lemma 2.8 takes "C₁,…,C_ℓ ∈ ℤ".
- Lemma 2.9 assumes the "total masses are positive reals".

**Proof, (i).**
- For Re s large, Σ_j C_j log L(s − σ_j, χ), with Euler-product branches, equals Σ_p Σ_r (1/r)χ(p)^r(Σ_j C_j p^{rσ_j})p^{−rs}.
- If it is constant, the constant is its limit 0 as s → +∞. The prime powers are distinct frequencies, so χ(p)^r Σ_j C_j p^{rσ_j} = 0 for all p, r.
- For p ∤ q, divide by χ(p)^r ≠ 0.
- A collision p^{σ_i} = p^{σ_j} happens at no more than one prime per pair. So some good prime has distinct x_j = p^{σ_j}, and the Vandermonde-type determinant ∏x_j∏(x_j − x_i) ≠ 0 gives C = 0.
- The ζ′/ζ form is the derivative. Integrality is used only to write ∏ζ^{C_j}.

**Proof, (ii).**
- A^d = B^d for the exponential polynomials A, B.
- If ν = 0 then A = 0.
- Otherwise A/B is holomorphic on the connected set {B ≠ 0}, and continuous with values in μ_d. So A/B is a constant ω, A = ωB everywhere, and μ = ων by independence of exponentials.
- The converse is clear. Positive total masses force ω > 0, hence ω = 1.

**Checks** (`v_f8_independence.py`).
- The determinant formula holds for random complex σ_j at p = 2, 3, 5, 7.
- A constructed collision at p = 2 only.
- The Euler-log coefficients for χ mod 5 match.
- sympy returns exactly the d solutions ν = ωμ, ω^d = 1, for d = 2, 3, 4, and the two solutions ±μ in a three-point case.

**In the notes?** No; `29_` has the integer version and the ±μ remark. New, elementary.

**Wording.** Accurate.

**Verdict. CONFIRMED.**

---

## F9. Theorem D in the verified range; Corollary B with growing Δ

**Reader.**
- The Theorem D bullet reads "assuming the zeros up to γ_n are simple and on the line".
- The Corollary B bullet: for fixed Δ the error is "of the same order T".
- p. 22 says Turing-method verifications establish I(T) = 0 and cites Platt–Trudgian for 3·10¹².

**(1) Theorem D.**
- *What Platt–Trudgian establish* (fetched arXiv abstract and PDF text):
  - Theorem 1: "RH is true up to height 3 000 175 332 800. That is, the lowest 12 363 153 437 138 non-trivial zeroes ρ have ℜρ = 1/2."
  - Their method counts sign changes of the completed zeta function on the half line and uses "a variation of Turing's method" to confirm that all expected zeros are accounted for.
  - They do **not** state simplicity.
- Logically, if the number of sign changes V(T) equals N(T) (which counts multiplicity), every zero up to T is on the line and simple. This is exactly I(T) = 0 in the reader's Prop 4.9.
- So the hypothesis of Theorem D holds for n ≤ 12 363 153 437 138 ≈ 1.24·10¹³. The proof of D uses nothing else (Z(0) = ζ(½) < 0, and sign changes at γ₁, …, γ_n).
- The review's claim "RH, with simplicity, is verified … up to height 3·10¹²" is right in substance. The simplicity is a consequence of the method, not a statement of PT's theorem, and the wording should say so.
- *Check* (`v_f9_counts.py`): θ(T)/π + 1 at PT's height is 12 363 153 437 137.1, within 1 of PT's count; θ(3·10¹²)/π + 1 = 1.23624·10¹³.
- *In the notes:* `03_` §3.1 ("this holds for n ≤ 10¹³ (Platt–Trudgian)"). An omission.

**(2) Corollary B at a = 1.**
- `02_` §4.2 gives the horizontal error ≤ (T₁ + T₂)d(Δ)/(2π) + K(Δ) + O(e^{−πT₁/2} + T₁e^{−T₁²/(8Δ²)}); the vertical law has the same error.
- d(Δ) is dominated by the n = 2 term ½·2^{−½}e^{−Δ²log²2/2}/log 2. So T₂d(Δ) ≤ C·T₂^{1−(1+δ)²} → 0 if Δ ≥ (1 + δ)√(2 log T₂)/log 2.
- K(Δ) → 0 as Δ → ∞.
- T₁e^{−T₁²/8Δ²} is decreasing for T₁ > 2Δ and is ≤ 4√(log Δ)/Δ once T₁ ≥ 4Δ√(log Δ).
- With T₁ = 10Δ only, it equals 10Δe^{−12.5}, which grows with Δ. So T₁/Δ → ∞ is needed, as the review says (and as O3 records against `02_`).
- *Check.*
  - d(1), d(2), d(3), d(5) = 0.7567, 0.2299, 0.06026, 0.001257, matching `02_`'s table.
  - With Δ = 1.1√(2 log T)/log 2, T·d(Δ) = 0.0737, 0.028, 0.0107, 0.00154 and 0.000223 at T = 10⁴, 10⁶, 10⁸, 10¹² and 10¹⁶, with the n = 2 term 100% of d.
  - The T₁ term at 10Δ is 37.3 at Δ = 10⁶, against 1.5·10⁻⁵ with T₁ = 4Δ√(log Δ).
- *Caveat.* This rests on `02_`'s displayed bound with absolute O-constants. `02_` does not say the constants are uniform in Δ, and the copy's report was not refereed separately. I did not re-derive Corollary B.
- *In the notes:* the Δ condition is in `02_` §4.2; the T₁ condition is new (O3).

**Corrected wording.**
- Theorem D: "…(this holds for every n ≤ 1.2·10¹³: Platt–Trudgian's verification to height 3.0·10¹² counts as many sign changes of Z as N(T), i.e. I(T) = 0 (Prop 4.9), so these zeros are on the line and simple; their theorem states the first property)."
- Corollary B: "…for fixed Δ the horizontal error is of order T. By the explicit error bound of `02_` §4.2, if Δ ≥ (1 + δ)√(2 log T₂)/log 2 and T₁ ≥ max(10Δ, 4Δ√(log Δ)), both errors tend to 0 at a = 1."

**Verdict. CONFIRMED WITH CORRECTION.**

**Confidence.** The PT paper was read through the fetch tool's rendering of its abstract and PDF. Corollary B was not re-derived.

---

## F10. Prop 3.2 and Lemma 3.3 under D ≤ div Φ

**Reader.**
- Prop 3.2: "Let Φ∈B have zero divisor exactly D".
- Lemma 3.3: "D the divisor of some F_D∈B".

**Proof (re-derived).**
- Let 0 ≢ Φ ∈ B with ord_λΦ ≥ D(λ) for all λ; equivalently I_D ≠ 0. Dividing Φ by (s − λ)^k at a zero of order ≥ k stays in B, by the maximum principle on |s − λ| ≤ 1 and |s − λ|^{−k} ≤ 1 outside.
- (a) For λ ∉ supp D, Φ_λ = Φ/(s − λ)^{ord_λΦ} ∈ I_D and Φ_λ(λ) ≠ 0. The reader's resolvent with Φ_λ in place of Φ works verbatim: it preserves I_D because D(λ) = 0.
- (b) With m′ = ord_ρΦ ≥ m = D(ρ), U = Φ/(s − ρ)^{m′−m+1} has order m − 1 at ρ and (s − ρ)U ∈ I_D.
- (c) U_ρ = Φ/(s − ρ)^{m′} has U_ρ(ρ) ≠ 0 and order ≥ D elsewhere. The rest of the proof does not use Φ.
- Lemma 3.3, general form. For λ ∈ supp D′∖supp D, (L − λ)^{D′(λ)} is onto B/I_D by (a). So every H(y) has zero D′(λ)-jet at λ, i.e. H takes values in I_{D″}/I_{D′} with D″ = D′·1_{ℂ∖supp D} (note I_{D′} ⊂ I_{D″}). The disjoint case gives H = 0.
- Example: D = the on-line or off-line part of Z, with Φ = F_*. A function in B with exactly that divisor is not known to exist, so the generalisation has content.

**Check.** By hand; there is nothing numerical to test.

**In the notes?** No (`24_` L. 24.2 and `27_` L. 27.1 assume the divisor is exact). New.

**Wording.** Accurate.

**Verdict. CONFIRMED.**

---

## F11. Lemma 3.4 for generalised exponentials

**Reader.** "If Σ_ρ c_ρ e^{ρx} = 0 for every real x, then c = 0".

**Proof (re-derived).**
- F^{(k)}(ρ) = ½∫a(e^v)v^k e^{ρv}dv, with a(e^v) decaying faster than every exponential (the half-Mellin representation NJS4.1 the reader uses).
- |v|^k ≤ k!R^{−k}e^{R|v|} gives Σ_{ρ,k}|c_{ρ,k}|∫|a||v|^k e^{A|v|} ≤ (Σ|c_{ρ,k}|k!R^{−k})∫|a|e^{(A+R)|v|} < ∞. So Fubini gives Σ c_{ρ,k}F^{(k)}(ρ) = 0 for all F ∈ B.
- F = G(s − ρ₀)^{−m}P(s − ρ₀) is in B (B is a module over polynomials). Its jet of order < m at ρ₀ is arbitrary and it vanishes to order m_ρ at the other ρ. So c_{ρ₀,·} = 0.

**Check.** By hand.

**In the notes?** No. New.

**Wording.** Accurate.

**Verdict. CONFIRMED.**

---

## F12. Lemma 3.6 and Corollary 3.7

**Reader.**
- Lemma 3.6 is stated for "a nontrivial zero ρ".
- Cor 3.7 says J(Q) "is a proper dense subspace of the product".

**Proof (re-derived).**
- (i) If |Re ρ| ≤ 3/2, the circle |z − ρ| = ½ lies in |Re z| ≤ 2, and 1 + |Im z| ≥ ½ + |γ|. So (1 + |γ|)^M|F^{(r)}(ρ)/r!| ≤ 2^r((1 + |γ|)/(½ + |γ|))^M b_{2,M}(F). The factor is ≤ 2 always and ≤ (1 + γ₁)/(½ + γ₁) = 1.034165 at the zeros.
- (ii) Lemma 3.6 with r < m_ρ ≤ C log(2 + |γ|) (D1) gives J(Q) ⊂ Λ_m continuously. This is the step "J is continuous into Λ_m" in `40_` Prop 40.5 and in the reader's proof of Thm 3.9.
- Finitely supported tuples lie in J(Q) (sections), and p_M(P − P_{≤T}) ≤ (1 + T)^{−1}p_{M+1}(P). So J(Q) is dense in Λ_m ⊊ ∏A_ρ.
- Whether J(Q) = Λ_m is exactly Thm 3.9(c)/(d), which is open. "Dense in Λ_m" is correct; "proper in Λ_m" would not be known.

**Checks** (`v_f12_f13_jets_L.py`).
- F = e^{s²/100}, zeros 1–20, r ≤ 3, M ≤ 4: max lhs/rhs = 0.838.
- Off-zero points with Re ∈ {−1.5, 0, 1.5}: 0.983 (≤ 1).
- The tail inequality holds on a random rapidly decreasing tuple.

**In the notes?** (i) is new (trivial). J(Q) ⊂ Λ_m is in `40_` (inside a proof); density in Λ_m is new (trivial).

**Wording.** Accurate. Λ_m is defined in the reader only before Thm 3.9, so the addendum must define it at Cor 3.7.

**Verdict. CONFIRMED.**

---

## F13. Theorem 3.9: rapid decay, and L(s, χ)

**(i) (b′) ⟺ (a)–(d).**
- (d) gives q(J^{−1}P) ≤ C·p_M(P).
- Π_ρx = J^{−1}(j_ρx·δ_ρ), and (1 + |γ|)^{M+N}‖j_ρx‖ ≤ p_{M+N}(Jx). So q(Π_ρx) ≤ C(1 + |γ|)^{−N}p_{M+N}(Jx).
- (b′) ⇒ (b), since Σ_ρ(1 + |γ|)^{−2} < ∞.

Correct.

**(ii) The L(s, χ) quotient: inputs, each checked against the proof of Thm 3.9.**

| Input | Where the ζ proof uses it | L(s, χ) analogue |
|---|---|---|
| a function in B with divisor exactly Z_χ | sections | Λ_χ ∈ B (Stirling; reader Prop 4.12) |
| (D1), (D2) | m_ρ ≤ C log, good heights | O(log q(\|t\|+2)); standard (Davenport ch. 16; not re-read) |
| good heights (Titchmarsh 9.7) | horizontal sides | same proof. For complex χ the zeros are not conjugation-symmetric, so heights for t < 0 come from χ̄ (L(σ − it, χ) = conj L(σ + it, χ̄)); the reader's "σ ± it" form needs this split |
| \|1/ζ(2 + it)\| ≤ ζ(2) | right side of R | \|1/L(2 + it, χ)\| ≤ ζ(2) |
| \|ζ(−1 + it)\| ≥ 3/π⁴ | left side of R | \|L(−1 + it, χ)\| = q^{3/2}(2π²)^{−1}\|1 − it\|√(π\|t\| th(π\|t\|/2)/2)\|L(2 − it, χ̄)\|, with th = coth (even χ) or tanh (odd χ); checked numerically for both parities (odd complex χ mod 5; even (·/5) and an even cubic χ mod 7), to 5·10⁻³¹. It is ≫_q (1 + \|t\|)^{3/2} for \|t\| ≥ 1, and vanishes at t = 0 for odd χ, a point outside the rectangles |
| polynomial growth of (s − 1)ζ(s) on strips | interpolants G_{ρ,k} | L(s, χ) itself (reader Prop 4.12, periodic partial summation); the factor (s − 1) and the bound \|ρ − 1\| ≥ 1 are simply dropped |
| N(T) ≪ T log T | summability | N(T, χ) ≪ T log qT |

**Checks** (χ mod 5, χ(2) = i).
- max |1/L(2 + it)| = 1.411 ≤ ζ(2).
- The closed form for |L(−1 + it)| agrees to 4·10⁻³¹.
- min |L(−1 + it)|/(1 + |t|)^{3/2} = 0.314 on 1 ≤ |t| ≤ 100.
- L(−1, χ) = 0.
- A zero at 0.5 + 6.18358i while L(conj ρ, χ) ≠ 0 (the asymmetry).

**In the notes?** No. New.

**Corrected wording.**
- "(b′) for every x ∈ Q and every continuous seminorm q, q(Π_ρx) = O((1 + |γ|)^{−N}) for every N."
- Remark: "The theorem and its proof carry over, with the evident changes, to B/I_χ for every primitive Dirichlet character χ. The principal parts of 1/L(s, χ) enter in (c). Λ_χ supplies the sections, L(s, χ) replaces (s − 1)ζ(s) in the interpolants, and (D1)–(D2) and the good heights hold with log q(|t| + 2). For complex χ, heights with t < 0 come from χ̄. Constants depend on q."
- "Verbatim" overstates this.

**Verdict. CONFIRMED WITH CORRECTION.**

**Confidence.** Davenport ch. 16 not re-read; the inputs are standard.

---

## F14. Prop 3.12: infinite codimension

**Proof (re-derived).**
- For any J, the (J + |F|)-tuples c with Σ_j c_j ev_{s_j}(g_t h_n) = 0 for n ∈ F (h_n = (n − n^{1−s})/s, s_j = 2πij/log a) form a space of dimension ≥ J.
- Each such combination kills every g_t h_{a^k}, because h_{a^k}(s_j) = 0.
- Distinct evaluations are independent on B. So the closure of N_S has codimension ≥ J.
- In I_ζ the same holds with the column factors ξ(s_j)g_t(s_j) ≠ 0 (Re s_j = 0). The restricted evaluations are independent on {g_tξP}, by interpolation.
- If F = ∅, every generator vanishes at every s_j, j ≠ 0 (negative j included), but not at 0, where h_n(0) = n log n.

**Check** (`v_f14_f15.py`, a = 3, F = {2, 5, 7, 10}).
- The condition matrix has full rank 4 (Hadamard ratio 0.143).
- The annihilating space has dimension exactly J for J = 2, 5, 8.
- The residuals on the n ∈ F generators and on all 3^k, k ≤ 30, are ≤ 1.7·10⁻³⁰.
- ξ(s_j) ≠ 0.

**In the notes?** No (`31_` L. 31.1 says "not dense"). New.

**Wording.** Accurate.

**Verdict. CONFIRMED.**

---

## F15. The residue-duality constant

**Reader.** "|B_ζ(F,G)| ≤ ζ(2)(1+4π²)π^{−1} b_{2,1}(F) b_{2,1}(G)". The expression equals 21.194; the review's phrase "the reader prints ≈ 21.19" is its own evaluation.

**Proof (re-derived).**
- On Re s = 2: |F(2 + it)G(−1 − it)/ζ| ≤ ζ(2)b b(1 + |t|)^{−2}, contributing (1/2π)·2·ζ(2) = ζ(2)/π.
- On Re s = −1: |χ(−1 + it)|² = π^{−3}y coth(πy)(¼ + y²) with y = t/2. With ¼ + y² ≥ (1 + |t|)²/8 and y coth πy ≥ (1 + |t|)/(2π), this gives |1/ζ(−1 + it)| ≤ 4π²ζ(2)(1 + |t|)^{−3/2}.
- The left contribution is therefore (1/2π)·4π²ζ(2)·∫(1 + |t|)^{−7/2}dt = 2πζ(2)·4/5 = 8πζ(2)/5.
- Total: ζ(2)(1/π + 8π/5) = **8.79194**. Dropping the factor (1 + |t|)^{−3/2} gives the reader's ζ(2)(1 + 4π²)/π = 21.19445.
- B(P(L)x, y) = B(x, P(1 − L)y) follows from B(Lx, y) = B(x, (1 − L)y) by iteration and linearity.

**Checks.**
- The constants; ∫(1 + |t|)^{−7/2} = 0.8.
- The edge bound ratio is ≤ 0.444 on [0, 400].
- For three test pairs the edge integrals of |FG(1 − s)/ζ| lie below the 8.79 bound (ratios 0.09, 6·10⁻⁵ and 0.12).

**In the notes?** Yes: `26_` §2.1 item 1 (from the eighth referee pass), register S49 ("8.79 in place of 21.19 is also valid"), `26_` Lemma 26.1(d). Omission.

**Wording.** Accurate.

**Verdict. CONFIRMED.**

---

## F16. Prop 4.3 with one dilation

**Proof (re-derived).**
- U_aU_b = U_{ab} and U_{a₀}^{−1} = U_{1/a₀}. So KU_{a₀} = U_{a₀}K implies KU_{a₀^k} = U_{a₀^k}K for all k ∈ ℤ.
- The reader's estimate ‖Kf‖ ≤ a^{σ′−σ}‖K‖‖f‖ holds for each such a.
- a₀^k → 0 and → ∞ along k → ±∞, whichever sign σ′ − σ has. So Kf = 0.

**In the notes?** No (`17_` 17.4(c) uses all a). New.

**Wording.** Accurate.

**Verdict. CONFIRMED.**

---

## F17. Prop 4.6 and Thm 4.2: orthogonality, index, L(s, χ)

**Reader.** Prop 4.6(c): "Under RH the T-even data form a maximal positive subspace".

**Proof (re-derived).**
- (i) Q_A is Hermitian, since A is an involution preserving m. Directly, Q_A(u, v) = Σ m_ρ[u(ρ)conj v(ρ^# − 1) + u(ρ − 1)conj v(ρ^#)] = Σ m_ρ u(ρ)[−conj v(ρ^#) + conj v(ρ^#)] = 0 for T-even u and T-odd v. So V₊ ⊥ V₋ with no hypothesis, and Q_A = 2Ω|_{V₊} ⊕ (−2Ω)|_{V₋}.
- (ii) On T-even data on a finite #-closed S, each on-line point gives a positive square, and each off-line pair gives 2m Re(x·conj y), with eigenvalues ±m. So the signature is (n_on + n_pairs, n_pairs). Without #-closedness, a lone off-line point gives a null direction.
- (iii) Under RH, Q_A is negative definite on V₋ and positive definite on V₊. A space strictly containing V₋ contains a nonzero x₊ ∈ V₊ with Q_A(x₊) > 0. So V₋ is maximal negative.
- (iv) Λ(s, χ) = WΛ(1 − s, χ̄) and conj Λ(s̄, χ̄) = Λ(s, χ) give Λ(1 − s̄, χ) = W·conj Λ(s, χ). So Z_χ is #-invariant with multiplicities, for complex χ as well.
  - Z_χ lies in 0 < Re s < 1, and G_χ(it) ≠ 0 (reader Prop 4.12 proof).
  - The proofs of Thm 4.2 and Prop 4.6(a)–(c) use only these facts.
  - Absolute convergence for data from B uses N(T, χ) ≪ T log qT. Cor 4.7 is ζ-specific and is not claimed.

**Checks** (`v_f17_chiral.py`).
- All 24 synthetic configurations (n_on, n_pairs ≤ 4, with multiplicities): cross block exactly 0; sig(Q_A|V₊) = (n_on + n_pairs, n_pairs); sig(Q_A|V₋) = (n_pairs, n_on + n_pairs).
- χ mod 5, χ(2) = i: |Λ(1 − s̄, χ)| = |Λ(s, χ)| at off-line points to 10⁻²⁵ (non-vacuous); W = 0.85065 + 0.52573i, |W| = 1; |L(1 − ρ, χ)| = 2.82 at a zero (s ↦ 1 − s is not a symmetry); A(ρ) + 1 is a zero; min_t |G_χ(it)|e^{π|t|/2} = 2.0 > 0.
- The review's own #-check, |L(1 − ρ̄, χ)| at on-line zeros, is vacuous, because 1 − ρ̄ = ρ there. The identity above replaces it.

**In the notes?**
- `42_` Prop 42.2(c) states the orthogonal decomposition and the definiteness on V₊ and V₋ **inside its "Under RH" clause**. It says "V₊ maximal positive" but not "V₋ maximal negative".
- So the unconditional orthogonality (i) is new in form, though immediate from 42.2's identity. (iii) is a one-step consequence of 42.2(c). (ii) and (iv) are new.
- The review's "(i) and (iii) are in `42_` Prop 42.2(c)" is only partly accurate.

**Corrected wording.**
- "(c) Unconditionally V₊ and V₋ are Q_A-orthogonal, and Q_A is 2Ω on V₊ and −2Ω on V₋. On T-even data supported on a finite #-closed set of zeros its signature is (n_on + n_pairs, n_pairs). Under RH V₊ is maximal positive and V₋ maximal negative; if RH fails, V₊ contains a negative direction."
- Remark: "Theorem 4.2 and Proposition 4.6 hold for every primitive Dirichlet L-function, complex χ included, with GRH for χ in place of RH."
- The review's wording omits "#-closed" and the RH-failure clause.

**Verdict. CONFIRMED WITH CORRECTION** (wording and provenance only).

---

## F18. Prop 4.10 for every modulus

**Proof (re-derived).**
- Σ_{p≤x}(1_{p≡a} − 1_{p≡b})log p/p = φ(q)^{−1}Σ_{χ≠χ₀}(χ̄(a) − χ̄(b))Σ_{p≤x}χ(p)log p/p. The principal character cancels because χ₀(a) = χ₀(b) = 1.
- Each inner sum converges by partial summation and the PNT for progressions (`42_` 42.4(a) proves this for every nonprincipal χ; imprimitive ones differ at finitely many p). The same holds with 1/p for the counting race.
- For r-way races the normalised term φ(q)Σ_{p≡a}1/p − Σ_p 1/p = Σ_{χ≠χ₀}χ̄(a)Σχ(p)/p − Σ_{p|q}1/p + o(1) also converges.
- After the √x (or √x/log x) normalisation the differences tend to 0. So the limiting distributions (Rubinstein–Sarnak, under GRH for the characters mod q) agree, and so do the densities δ(q; a, b), under GRH and linear independence, which make the distribution atomless.

**Check** (`v_f18_races.py`, primes up to 10⁷).
- q ∈ {3, 5, 7, 8, 12}, all pairs of classes.
- The spread over x ∈ {10⁵, 10⁶, 10⁷} is ≤ 0.0049 (θ-race) and ≤ 0.0004 (counting race).
- mod 5 (1,2): −0.5897, −0.5721, −0.5804, −0.5799, −0.5808, the review's numbers up to the sign of the (2,1) order.
- The normalised values at 10⁷ are ≤ 2.3·10⁻⁴ and 3.4·10⁻³.
- The r-way terms converge.

**In the notes?** No for general q, but immediate from `42_` 42.4(a). New.

**Wording.** Accurate.

**Verdict. CONFIRMED.**

---

## F19. Prop 4.12 for Dedekind zeta functions

**Proof (re-derived).**
- Λ_K = |d_K|^{s/2}Γ_ℝ^{r₁}Γ_ℂ^{r₂}ζ_K. The trivial zeros cancel the Gamma poles, and Λ_K has simple poles at 0 and 1. So ξ_K = s(s − 1)Λ_K is entire with zeros exactly the nontrivial zeros, in 0 < Re s < 1.
- G_K(s) = ξ_K(1 − s)ξ_K(1 + s) = |d_K|s²(s² − 1)[Γ_ℝ(1 − s)Γ_ℝ(1 + s)]^{r₁}[Γ_ℂ(1 − s)Γ_ℂ(1 + s)]^{r₂}ζ_K(1 − s)ζ_K(1 + s).
- Γ_ℝ(1 − s)Γ_ℝ(1 + s) = 1/cos(πs/2) and Γ_ℂ(1 − s)Γ_ℂ(1 + s) = s/(π sin πs). For |t| ≥ 1 these are ≍ e^{−π|t|/2} and ≍ |t|e^{−π|t|} on every vertical line. So the upper rate (a) and the Gamma part of the lower rate (b) match at α = (r₁ + 2r₂)π/2 = nπ/2.
- The corridor lower bound for ζ_K(1 + x ± it) follows from the 3-4-1 inequality (Euler product over prime ideals), ζ_K(1 + δ) ≤ C/δ, and polynomial bounds for ζ_K and ζ_K′ near σ = 1.
- For |t| ≤ 1, G_K(it) = |ξ_K(1 + it)|² > 0.
- **Input the review glosses over.** Polynomial growth of ζ_K (and ζ_K′) on vertical strips is needed for ξ_K ∈ B, for (a) and for the corridor. The reader's growth step, periodic partial summation for L(s, χ), does not apply to ζ_K. It is standard (finite order plus Phragmén–Lindelöf, i.e. the convexity bound), but it must be cited.
- Full list of inputs: Hecke's continuation and functional equation; polynomial growth on strips; the Euler product; ζ_K(1 + it) ≠ 0 made quantitative by 3-4-1; Stirling.

**Checks** (`v_f19_dedekind.py`). Fields ℚ(i) (0,1), ℚ(√5) (2,0), the cyclic cubic field of conductor 7 (3,0) and ℚ(ζ₅) (0,2):
- the Gamma identities hold to 10⁻³⁰;
- Λ_K(s) = Λ_K(1 − s) to 10⁻²⁹;
- with α = nπ/2 the local polynomial order of |G_K(x + it)|e^{αt} between t = 40 and t = 80 lies in [1.9, 9.7] on seven lines x ∈ [−1.5, 1.5], and log(|G_K(it)|e^{αt}) ≥ 4.08 on [2, 80];
- α − π/2 gives slopes between −89 and −81, and α + π/2 slopes between +92 and +100, so the rate is exactly nπ/2;
- the 3-4-1 products are ≥ 1.23 on the grid.

**In the notes?** No. New.

**Corrected wording.** "The same argument gives the splitting for every Dedekind zeta function, with α = nπ/2, n = [K:ℚ]. The inputs are Hecke's functional equation, polynomial growth of ζ_K on vertical strips (convexity), the 3-4-1 inequality and Stirling."

**Verdict. CONFIRMED WITH CORRECTION.**

**Confidence.** The standard ζ_K facts were not re-read in a textbook.

---

## F20. Lemma 4.13: direction of monotonicity

**Proof (re-derived).**
- d/dx log(sinh(ax)/sinh(bx)) = a coth(ax) − b coth(bx), with a = log r and b = log t.
- c ↦ c coth(cx) is strictly increasing for x > 0; its derivative is (½sinh 2cx − cx)/sinh²cx > 0.
- So the ratio is increasing in |x| iff r > t, and decreasing iff r < t. It is even in x.

**Check.** 20 ordered pairs from {1.1, 2, 5, 30, 100}, 2000 points each: exactly as stated. The endpoint values are confirmed.

**In the notes?** `24_` Lemma 24.5(b). Omission.

**Wording.** Accurate.

**Verdict. CONFIRMED.**

---

## F21. Lemmas 5.5 and 5.6

**(i) Lemma 5.5.**
- In the reader's chain 0 ≤ ν(ρρ̄) = M + Σ_{τ≠1}[ρρ̄ : τ]ν(τ) ≤ M + Σ_{τ∈T}(1 − e)d_τ Mν(τ), only ν ≤ 0 off 1 and real values are used.
- So Σ d_τ(−ν(τ)) ≤ 1 for real-valued ν. Integrality and ν(τ̄) = ν(τ) are used only in the dichotomy.
- *Check* on ℤ/3 with ν(τ) = ν(τ²) = −x: ν(ρρ̄) = a² + b² + c² − 2x(ab + bc + ca) ≥ 0 for all genuine ρ iff x ≤ ½ (exhaustive to 12; the violation is at (1,1,1)).
- So the real-valued bound is sharp, and at x = ½ two nontrivial characters are negative. The integer dichotomy genuinely needs integrality.

**(ii) Lemma 5.6.**
- In the Dirichlet-approximation step, δ_n − Re Σa_j^n ≤ CD^n − |J|R^n/2 + O(R′^n) → −∞ along infinitely many n if R > D. Any D > 0 works; "D ≥ 1" is harmless.
- For a curve, δ_n = 1 + q^n ≤ 2q^n gives |α_j| ≤ q, the trivial bound.
- *Check:*
  - a = (1.5e^{±0.3i}, −0.7), δ_n = 2D^n + 1: nonnegative for n ≤ 2000 at D = 1.6 and 1.5; fails at n = 18 for D = 1.45.
  - y² = x³ + x + 3 over F₇: a_p = 2, |α| = √7, and the point counts for n ≤ 20 are ≥ 0.

**In the notes?** No (`37_` Lemmas 37.2–37.3 use integer ν and a constant δ). New.

**Wording.** Accurate. For Lemma 5.6 state δ_n real, δ_n ≤ CD^n, D > 0.

**Verdict. CONFIRMED.**

---

## F22. Four auxiliary statements of §6

**Prop 6.2.**
- For an integer a ≥ 2 and every d, N = a^d − 1 is coprime to a. Also 1 < a^k < N for 1 ≤ k < d, so ord_N(a) = d.
- Hence n ↦ a^n extends to Ẑ → ∏_{ℓ∤a}ℤ_ℓ^×. It is injective, with kernel ∩_d dẐ = 0, and has compact image equal to the closure.
- *Check:* a ≤ 30, d ≤ 40. **Correct.**

**Lemma 6.4 (reader: "a≥2", with the collision clause "only if ρ/ρ′∈ℚ_{>0}").**
- For real a > 1 the escape clauses hold: finiteness of returns, no aS ⊂ S, and "only Re ρ < 1/a can return".
- The reflected-pair clause needs a ≥ 2. For 1 < a < 2 a pair with 1 − 1/a < Re ρ < 1/a *can* return, for suitable Z. Example: a = 1.5, ρ = 0.55 + i, and Z = {ρ, ρ^#, aρ, aρ^#, (aρ)^#, (aρ^#)^#}, which is #-closed and in the strip. The review's "returns" should read "can return".
- **The collision clause does not survive for real a, a′.** aρ = a′ρ′ gives ρ/ρ′ = a′/a, which is rational only for rational a, a′.
  - Example: a = 2√2, a′ = 2, ρ = 0.3 + 0.3i, ρ′ = √2ρ, both in the strip, ratio 1/√2.
  - The consequence for the critical line survives with "ℝ_{>0}": (½ + iγ)/(½ + iγ′) is real only if γ = γ′.
  - So the review's "Every clause except … holds for every real a > 1" is inaccurate for the collision clause as written.

**Prop 6.5.**
- The statement's first sentence, "If RH is false, T ⊢ ¬RH", is logically the same as "if T ⊬ ¬RH, then RH". `23_` Prop 23.1(b) states that form.
- So the reader's statement already contains the stronger form. "So if RH is independent of T, it is true" is only an added weaker gloss. The review's "the statement does not [say the stronger form]" is wrong, and the suggested parenthetical is a restatement, not an addition.
- Its side observations are correct:
  - Σ₁-soundness is needed only for RH ⇒ T ⊬ ¬RH. For example, T = ZFC + ¬RH, if consistent, proves all true Σ₁ sentences and refutes a true RH.
  - Recursive axiomatisability is needed only to arithmetise Con and for Gödel II.
- **This sub-item is not an understatement** (no change needed; the contrapositive may be made explicit).

**Lemma 6.6.**
- div U = (div V)∘F by the Piola identity and the chain rule, using only first derivatives of V. So it holds for C¹ V, and U is polynomial if V is.
- DF·U = V∘F gives the curve statement.
- For a polynomial automorphism with inverse G, Φ^U_τ = G∘Φ^V_τ∘F, so U is complete iff V is.
- *Check* (sympy, exact rationals): the reader's F with det DF = −2 and V = (x² + y, yw, x³ − w). At six random rational points div U = (div V)(F) exactly, the Piola sums are 0, and DF·U = V(F). **Correct.**

**In the notes?** No for 6.2, 6.4 and 6.6 (new). For 6.5 the form is in `23_` (b), and the reader keeps it as its first sentence.

**Corrected wording.**
- Prop 6.2: "…the closure of a^ℤ in ∏_{ℓ∤a}ℤ_ℓ^× is a copy of Ẑ for every integer a ≥ 2."
- Lemma 6.4: "Let a > 1 be real (a ≥ 2 for the reflected-pair clause) … Two points collide, aρ = a′ρ′ with ρ ≠ ρ′, only if ρ/ρ′ = a′/a > 0 (rational when a, a′ are integers), which is impossible for distinct points of the critical line."
- Prop 6.5: no change needed.
- Lemma 6.6: "V a C¹ vector field; U is polynomial if V is; if F is a polynomial automorphism, U is complete iff V is (for instance, V affine)."

**Verdict. CONFIRMED WITH CORRECTION** (the Lemma 6.4 collision clause and "can return"; the Prop 6.5 sub-item rejected as an understatement).

---

## Citation checks (web)

- **Saias–Weingartner**, arXiv:0807.0783 (Acta Arith. 140 (2009), DOI 10.4064/aa140-4-4). Abstract only:
  - hypothesis: a periodic, F_a not of the form P(s)L_χ(s);
  - conclusion: ∃η(a) > 0 with c₁T ≤ N_a(σ₁, σ₂, T) ≤ c₂T for all ½ < σ₁ < σ₂ < 1 + η and large T, where N_a counts σ₁ < Re s < σ₂, |Im s| ≤ T and c_i = c_i(a, σ₁, σ₂).
  - The theorem number (4) is not visible in the abstract.
- **Platt–Trudgian**, arXiv:2004.09765 (Bull. LMS 53 (2021)):
  - Theorem 1: RH to height 3 000 175 332 800, i.e. the lowest 12 363 153 437 138 zeros have real part ½.
  - Method: sign changes of the completed zeta function on the half line, plus a variation of Turing's method confirming that all expected zeros are accounted for.
  - Simplicity is not stated.
  - Read through the fetch tool's rendering, not page images.

## Scripts and results

All are in this folder and use mpmath 1.3, sympy 1.14, numpy 2.4 and exact `Fraction` arithmetic. Each ends with "ALL … CHECKS PASS", and its full output is in `<name>_OUTPUT.txt`. None imports the review's scripts.

| Script | Finding | Key results |
|---|---|---|
| `v_f6_monoids.py` | F6 | 44 proper (q,H), q ≤ 16, n ≤ 6000: first negative value ≤ −½, largest −½. At every divisor-minimal non-factorial element, r = 1 − j + ε ≤ −½ and ≤ 1 pure power. Pigeonhole atoms A₀A₂ = A₁² in 6 cases. ⟨4,8⟩ roots on \|x\| = 1. |
| `v_f7_evensheets.py` | F7 | Hurwitz formula to 10⁻⁴⁰. Φ_{1/q} decomposition for q = 3, 5, 7, 11, 13 to < 10⁻²⁵; \|τ\| = √q. Not P·L (≥ 2 forced b(1) values). CSV: 24 / 40 / 26, gap 0.006806. Φ_{1/5}(1 − z) = 0 at all 66 left zeros (1.5·10⁻¹⁶). |
| `v_f8_independence.py` | F8 | Vandermonde determinant formula for complex σ_j. Collision at p = 2 only. χ-twisted Euler-log coefficients. d-th convolution roots are exactly ωμ, ω^d = 1 (d = 2, 3, 4). |
| `v_f9_counts.py` | F9 | θ(T)/π + 1 = 12 363 153 437 137.1 at PT's height (PT: …138). d(Δ) reproduces `02_`'s table. T·d(Δ(T)) = 0.0737, 0.028, 0.0107, 0.00154, 0.000223. The T₁ = 10Δ term grows (37 at Δ = 10⁶); T₁ = 4Δ√(log Δ) makes it decay. |
| `v_f12_f13_jets_L.py` | F12, F13 | Sharper constant 1.034165; max ratio 0.838 at zeros, 0.983 off zeros. Λ_m tail inequality. χ mod 5: \|1/L(2+it)\| ≤ 1.411, closed form for \|L(−1+it)\| to 4·10⁻³¹ (also the even-parity form for (·/5) and a cubic χ mod 7, to 5·10⁻³¹), min ratio to (1+\|t\|)^{3/2} is 0.314, L(−1, χ) = 0, zero sets of χ and χ̄ differ. |
| `v_f14_f15.py` | F14, F15 | Codimension ≥ J for J = 2, 5, 8 (residuals ≤ 1.7·10⁻³⁰). Constants 21.19445 and 8.79194. ∫(1+\|t\|)^{−7/2} = 0.8. Edge-bound ratio 0.444. Three test pairs below the 8.79 bound. |
| `v_f17_chiral.py` | F17 | 24 configurations: V₊ ⊥ V₋ exactly; signatures (n_on + n_pairs, n_pairs) and (n_pairs, n_on + n_pairs). \|Λ(1 − s̄, χ)\| = \|Λ(s, χ)\| off the line; \|W\| = 1; the zero set is not 1 − s symmetric; G_χ(it) ≠ 0. |
| `v_f18_races.py` | F18 | q ∈ {3, 5, 7, 8, 12}, all pairs, x ≤ 10⁷: convergent differences (spread ≤ 0.0049 and 0.0004); normalised values → 0; r-way terms converge. |
| `v_f19_dedekind.py` | F19 | Four fields, n = 2, 3, 4. Gamma identities; functional equations to 10⁻²⁹. Matched rate α = nπ/2 (local order 1.9–9.7; α − π/2 gives slopes −89 to −81, α + π/2 gives +92 to +100). Lower bound on Re s = 0. 3-4-1 products ≥ 1.23. |
| `v_f20_f21.py` | F20, F21 | Monotonicity direction on 20 pairs. ℤ/3 real-valued ν: hypothesis ⟺ 2x ≤ 1, with a violation at (1,1,1) for x > ½. Lemma 5.6 with δ_n = 2D^n + 1: holds for D ≥ 1.5, fails at n = 18 for D = 1.45. Elliptic curve over F₇ with \|α\| = √7. |
| `v_f22_misc.py` | F22 | ord_{a^d−1}(a) = d for a ≤ 30, d ≤ 40. Reflected pair returning at a = 1.5. Irrational collision ratio 1/√2 for real a, a′. Keller map: det DF = −2; div U = (div V)∘F, Piola and DF·U = V∘F exactly at six rational points with a cubic, non-affine V. |

## Counts

- **CONFIRMED (11):** F6, F8, F10, F11, F12, F14, F15, F16, F18, F20, F21.
- **CONFIRMED WITH CORRECTION (6):** F7, F9, F13, F17, F19, F22.
- **REJECTED (0).** Within F22, the Prop 6.5 sub-item is rejected as an understatement.
- **Omissions of the notes vs new.**
  - Omissions: F6, F9 (both parts, with the T₁ condition new), F15, F20, and the right-side part of F7.
  - New: F7 (left side), F8, F10, F11, F12(i) and the density part, F13, F14, F16, F17 (mostly), F18, F19, F21, and F22 (except Prop 6.5).
