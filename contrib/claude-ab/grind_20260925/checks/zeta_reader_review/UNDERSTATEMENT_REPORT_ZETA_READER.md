# Understatement and missed-generality review of the zeta reader

**Document reviewed.** *The split-zero programme around the Riemann zeta function: a reader of its results, with proofs* (Zenodo, DOI 10.5281/zenodo.22970703). Source: `reader/*.tex`; PDF: `reader.pdf`, 51 pages. Page numbers below are the printed ones, which equal the PDF page numbers.

**Reviewer.** An independent Claude instance (claude-opus-5-5) that did not write the reader or the notes. The review was read-only, done on 26 September 2026. I read the whole reader, then the register `00_` and the notes behind Sections 2–6 (`02_`, `03_`, `08_`, `11_`, `16_`, `17_`, `20_`, `22_`–`27_`, `29_`, `31_`–`33_`, `37_`, `40_`, `42_`).

**Brief.** Look for understatement and missed generality, and record any overclaim seen along the way. Every stronger statement below is either proved here or is a proved statement of the notes that the reader leaves out. Each one has a computational check where a check means anything. Nothing here bears on the truth of RH, and τ is not identified with any zero.

## Summary

There are 22 findings: 5 MAJOR and 17 MINOR. Separately, 4 overclaims or gaps are recorded, 3 in the reader and 1 in a source note. All 10 check scripts pass.

| # | Location | Class | In one line |
|---|---|---|---|
| F1 | Thm 4.1, p. 18 | MAJOR | The first-jet theorem holds on every sheet a > 0 and globally. Only (d) and Thm 4.2 are specific to ζ. |
| F2 | Lemma 3.13, p. 16 | MAJOR | Every bounded Hermitian transfer form is a weighted Weil pairing. n ∈ {2, 3} suffices. Positivity forces support on the line. |
| F3 | Prop 3.11, p. 16; §9 item 5, p. 41 | MAJOR | Quadratic counting with an explicit constant suffices. {2^a3^b} gives a dense family for every t > log2·log3/(2π) ≈ 0.121. |
| F4 | Thm 2.3, Cor 2.4, pp. 7–8 | MAJOR | The formula r_n = 1 − j + ε holds at every element whose proper M-divisors factor uniquely. This locates infinitely many negative coefficients, not just the first. |
| F5 | Prop 5.1, p. 24 | MAJOR | The abscissa is 1 + k·β_max for every power k and every finite S. Positivity is needed only to put the pole at the real point. |
| F6 | Thm 2.3, Prop 2.6, Ex 2.5, pp. 7–9 | MINOR | Three proved refinements from `11_` and `29_` are dropped: the bound −½ for congruence monoids, a proof without Dirichlet's theorem, and the zero-free half-plane of absolute convergence. |
| F7 | Props 2.6–2.7, §2.3, Fig. 2, pp. 9–10 | MINOR | Saias–Weingartner gives about T zeros in every strip. For prime q ≥ 5 this holds on both sides of the line, so "checked numerically" can become a theorem for the qualitative claim. |
| F8 | Lemmas 2.8–2.9, p. 10 | MINOR | Lemma 2.8 holds with complex exponents and for L(s, χ). Lemma 2.9 without normalisation gives μ = ων with ω^d = 1. |
| F9 | §2.1 bullets, p. 6 | MINOR | Theorem D is unconditional for n ≤ 1.2·10¹³. Corollary B has error o(1) when Δ grows like √(2 log T). |
| F10 | Prop 3.2, Lemma 3.3, pp. 11–12 | MINOR | D ≤ div Φ suffices. An equivariant map lands in the ideal of jets vanishing off supp D. |
| F11 | Lemma 3.4, p. 12 | MINOR | The lemma extends to generalised exponentials x^k e^{ρx} with k < m_ρ. |
| F12 | Lemma 3.6, Cor 3.7, p. 13 | MINOR | The decay bound holds at every point with \|Re ρ\| ≤ 3/2, with a better constant. J(Q) is a dense subspace of Λ_m, which is sharper than "proper". |
| F13 | Thm 3.9, p. 14 | MINOR | Rapid decay of Π_ρx can be added to the equivalences. The theorem holds verbatim for every primitive L(s, χ). |
| F14 | Prop 3.12, p. 16 | MINOR | The closure has infinite codimension, not just codimension ≥ 1. |
| F15 | §3.5, residue duality, p. 17 | MINOR | The sharper constant 8.79 from `26_` can replace 21.19. |
| F16 | Prop 4.3, p. 19 | MINOR | Commuting with one dilation a ≠ 1 is enough. |
| F17 | Prop 4.6, Thm 4.2, pp. 18–20 | MINOR | The splitting Q_A = 2Ω ⊕ (−2Ω) is unconditional, and the negative index counts the off-line pairs. Both results hold for every primitive L(s, χ). |
| F18 | Prop 4.10, p. 22 | MINOR | The conclusion holds for every modulus and every pair of classes, not only mod 4. |
| F19 | Prop 4.12, p. 23 | MINOR | The same proof works for Dedekind zeta functions, with α = nπ/2. |
| F20 | Lemma 4.13, p. 23 | MINOR | The direction of monotonicity is dropped; `24_` states it. |
| F21 | Lemmas 5.5–5.6, pp. 26–27 | MINOR | Lemma 5.5's inequality holds for real-valued ν. Lemma 5.6 holds with δ_n = O(D^n), which gives \|α\| ≤ q for curves. |
| F22 | Prop 6.2, Lemma 6.4, Prop 6.5, Lemma 6.6, pp. 28–31 | MINOR | Hypotheses in four auxiliary statements are stronger than their proofs use. |

---

## MAJOR findings

### F1. Theorem 4.1 (the first Hurwitz jet) holds on every sheet and globally

- **Location.** §4.1, Theorem 4.1 (c), p. 18. The introduction to §4 (p. 18) says "what vanishes on the shifted set is its first jet". The source `17_` §6 says "Theorem 17.1 is specific to ζ", and `17_` §1 says "Parts (b)–(d) use ζ's pole and zero-free regions".
- **Understated.** "In −1<Re s<0 the zeros of the first jet are exactly Z−1." The statement is made only at a = 1 and only in the strip.
- **Stronger statement.** For every sheet a > 0, that is at every time t = a − 1 of the flow, and every m ≥ 1:
  - (a′) ∂_a^m ζ(s, a) = (−1)^m (s)_m ζ(s + m, a). The right side is entire, because the zero of (s)_m at 1 − m cancels the pole, and its value there is −(m − 1)!.
  - (b′) sζ(s + 1, a) is entire with value 1 at s = 0. So the first jet equals −1 at s = 0 on every sheet.
  - (c′) The zero divisor of the first a-jet −sζ(s + 1, a) is exactly the zero divisor of ζ(·, a) translated by −1, with multiplicities and without any strip restriction. For the m-th jet it is (div ζ(·, a) − m) + [0] + [−1] + … + [2 − m]; the last m − 1 are simple zeros.
  - At a = 1 this reads div = (Z − 1) + Σ_{k≥1}[−2k − 1]. The reader's (c) is the part of this divisor in −1 < Re s < 0.
  - **Scope.** (d) and Theorem 4.2 do not extend. At a = ½, the point s₁ = 2πi/log 2 is a zero of ζ(·, ½) = (2^s − 1)ζ(s), but |ζ(1 − s̄₁, ½)| = 1.351. So the zero set of that sheet is not #-symmetric, and A(Z_{1/2}) ≠ Z_{1/2} − 1.
- **Proof.**
  - (a′) The reader's own proof is already written for every a: the identity holds termwise on Re s > 1, and joint analyticity in (s, a) extends it.
  - (b′) ζ(s, a) = a^{1−s}/(s − 1) + (entire), so its pole at s = 1 has residue 1 for every a.
  - (c′) For s ≠ 0 the factor −s is a nonzero constant factor locally, so it changes neither the zeros nor their orders. At s = 0 the value is −1.
  - For the m-th jet, (s)_m vanishes at 0, …, 1 − m. At −j with 0 ≤ j ≤ m − 2, the value ζ(m − j, a) = Σ(n + a)^{−(m−j)} > 0, so these zeros are simple and cannot coincide with shifted zeros of ζ(·, a).
- **Check.** `check_hurwitz_jet_all_sheets.py` (all pass).
  - The identity holds at a ∈ {0.3, ½, 1, 2, 3.7} at points with Re s < 1.
  - The value −1 + ψ(a)s is matched to 10⁻²⁰ for six values of a.
  - Shifted zeros are jet zeros at a = 2 (the zero 1.40779 + 23.32799i of ζ(s) − 1), at a = ½ (2πik/log 2 and 0), at a = 0.3 (four off-line zeros) and at a = 1 (ρ₁, −2, −4); the directly computed a-derivative there is ≤ 1.5·10⁻²⁸.
  - Conversely, jet zeros found by findroot, shifted by +1, are zeros of ζ(·, a).
  - At a = 0.3, m = 3, the jet vanishes at 0 and −1 and equals −2 at 1 − m.
  - The a = ½ counterexample to #-symmetry is computed.
- **Suggested wording.** "Theorem 4.1 (the first Hurwitz jet, on every sheet). For every a > 0, ∂_aζ(s, a) = −sζ(s + 1, a) is entire, equals −1 at s = 0, and its zero divisor is exactly div ζ(·, a) − 1. At a = 1 this is (Z − 1) + Σ_k[−2k − 1], and the zeros in −1 < Re s < 0 are exactly Z − 1. [(d) unchanged.] Parts (a)–(c) hold at every time of the flow; (d) and Theorem 4.2 use the functional equation of ζ and fail, for example, at a = ½."
- **Class.** MAJOR. A statement made for a = 1 is proved, by the same proof, on every sheet and without the strip restriction. The source note said the opposite.

### F2. Lemma 3.13: every bounded Hermitian transfer form is a weighted Weil pairing

- **Location.** §3.5, Lemma 3.13, p. 16. The same objects appear in N-Pos1 (p. 33), in PTQ5 (Weil's W, `25_` §2.1) and in Prop 4.6(b).
- **Understated.**
  - The hypotheses: "B(T_n x, y) = B(x, U_n y) for all integers n ≥ 1".
  - The scope: positive semidefinite forms only.
- **Stronger statement.** Let B be a bounded Hermitian form on ℓ²(Z, m) with B(T_nx, T_ny) = nB(x, y) for n = 2 and n = 3 only.
  - Then B(x, y) = Σ_ρ b_ρ m_ρ x_ρ·conj(y_{ρ#}), where ρ# = 1 − ρ̄, (b_ρ) is bounded and b_{ρ#} = conj(b_ρ).
  - Conversely, every such form satisfies the relation for every real n > 0.
  - B ≥ 0 if and only if b_ρ = 0 at every off-line ρ and b_ρ ≥ 0 on the line.
  - Weil's pairing Ω is the case b ≡ 1. So Lemma 3.13, Weil's form W of PTQ5 and Prop 4.6(b) are three faces of one classification.
  - {2, 3} can be replaced by any n₁, n₂ > 1 with log n₁/log n₂ ∉ ℚ.
  - One value of n is not enough. If two points of Z differ by 2πi/log 2, n = 2 allows further forms, which are not of Weil type.
- **Proof.**
  - The relation on coordinate vectors reads (n^{ρ+η̄−1} − 1)B(ε_ρ, ε_η) = 0. If the entry is nonzero, then ρ + η̄ − 1 lies in (2πi/log 2)ℤ ∩ (2πi/log 3)ℤ = {0}; this is the reader's step 3^k ≠ 2^l. So η = ρ#.
  - Boundedness gives B(x, y) = Σ_ρ B(ε_ρ, ε_{ρ#}) x_ρ conj(y_{ρ#}). Put b_ρ = B(ε_ρ, ε_{ρ#})/m_ρ; then |b_ρ| ≤ ‖B‖, and B Hermitian gives b_{ρ#} = conj b_ρ.
  - For the converse, ρ + conj(ρ#) = 1 identically.
  - Positivity: on the line ρ# = ρ, and the block is m b_ρ|x_ρ|². An off-line pair gives 2m Re(b_ρ x_ρ conj x_{ρ#}), a hyperbolic plane with eigenvalues ±m|b_ρ|, which is ≥ 0 only if b_ρ = 0.
  - The reader's proof uses positivity only through Cauchy–Schwarz. The classification shows why: positivity is exactly what kills the hyperbolic off-line blocks.
- **Check.** `check_transfer_forms.py` (all pass). It uses a synthetic #- and conjugation-stable configuration: three ζ ordinates with synthetic multiplicities, a hypothetical off-line quartet, and a line pair 2π/log 2 apart.
  - The entries left free by n ∈ {2, 3} are exactly the 14 entries (ρ, ρ#). Using n ∈ {2, …, 59} gives the same 14.
  - n = 2 alone leaves 4 extra entries, at the 2π/log 2 pair.
  - Weil-type forms satisfy the relation at 200 random real n.
  - The positivity criterion agrees with eigenvalue computations on 4000 random forms.
  - An off-line block has eigenvalues ±m|b|.
- **Suggested wording.** "Lemma 3.13 (transfer-compatible forms). A bounded Hermitian form B on ℓ²(Z, m) satisfies B(T_nx, T_ny) = nB(x, y) for n = 2 and n = 3 if and only if B(x, y) = Σ_ρ b_ρ m_ρ x_ρ conj(y_{ρ#}) with bounded b and b_{ρ#} = conj b_ρ. The relation then holds for every n > 0. Such a B is positive if and only if b vanishes off the line and is ≥ 0 on it. Weil's pairing is b ≡ 1."
- **Class.** MAJOR. Both a hypothesis and a scope are weakened, and the statement becomes one classification that contains Weil's form.

### F3. Prop 3.11: quadratic counting with an explicit constant suffices, which answers open question 5 for t > log2·log3/(2π)

- **Location.** §3.4, Prop 3.11, p. 16, and its outline. §9 item 5, p. 41. The source `16_` §1 item 3 says the quadratic case is "not covered, because the constant in the Jensen bound depends on Λ".
- **Understated.**
  - The hypothesis: "If limsup_{R→∞} #{n∈S: log n ≤ R}/R² = ∞".
  - The open question: "quadratic counting, where the Jensen argument is inconclusive".
- **Stronger statement.** Fix t > 0, let S ⊂ {2, 3, …}, and put ν_S(x) = #{n ∈ S : log n ≤ x}.
  - N_S is dense in B, and ξN_S is dense in I_ζ, as soon as either condition holds:
    - (C) limsup_{R→∞} R^{−1} Σ_{n∈S, log n<R}(1/log n − log n/R²) > 1/(3πt), or
    - (J) limsup_{R→∞} R^{−2} ∫₁^R ν_S(x) dx/x > 1/(8t).
  - For S = {2^a3^b : a + b ≥ 1}, ν_S(x) = x²/(2 log 2 log 3) + O(x). Condition (C) then gives density for every t > (log 2)(log 3)/(2π) ≈ 0.1212; condition (J) gives it for t > (log 2)(log 3)/2 ≈ 0.381.
  - Density is monotone in t. If N_S^{(t′)} is dense, then N_S^{(t)} = g_{t−t′}N_S^{(t′)} is dense for every t > t′, because g_{t−t′}B is dense in B (step 4 of the proof).
  - So open question 5 is answered, affirmatively, for every t > 0.1212. It remains open for 0 < t ≤ 0.1212.
  - The reader's condition, limsup ν_S/R² = ∞, implies (J) for every t.
- **Proof.**
  1. Let Λ ∈ B′ annihilate N_S, with |Λ(F)| ≤ C b_{A,M}(F). Put L(w) = Λ(K_w), where K_w = g_t(e^w − e^{(1−s)w})/s. By the identity (e^w − e^{(1−s)w})/s = w e^w ∫₀¹ e^{−θsw}dθ, w ↦ K_w is a B-valued power series, so L is entire. L(0) = 0, and L(log n) = 0 for n ∈ S.
  2. **Growth.** sup_τ(1 + |τ|)^M e^{−tτ² + τv} ≤ C_M(1 + |v|)^M e^{v²/(4t)}. With a maximum-principle bound near s = 0, this gives

     log|L(u + iv)| ≤ v²/(4t) + α(|u| + |v|) + M log(2 + |w|) + C.

     Only α, M and C depend on Λ. The quadratic coefficient 1/(4t) does not, and this is exactly the point that `16_` §1 item 3 gets wrong.
  3. **Carleman's formula.** Apply it to f = L/w^k on the half-annulus ρ ≤ |w| ≤ R, Re w ≥ 0 (Titchmarsh, *Theory of Functions*, §3.7). The boundary term is O(1); move the boundary line slightly if f has zeros on it. The arc integral contributes (1/πR)∫(R² sin²θ/4t) cos θ dθ = R/(6πt) + O(1), and the imaginary-axis integral contributes (1/4πt)∫_ρ^R(1 − y²/R²)dy = R/(6πt) + O(1). So Σ(1/r_j − r_j/R²)cos θ_j ≤ R/(3πt) + O(log R). The zeros log n are real and positive, and the other zeros only add nonnegative terms, so (C) forces L ≡ 0. Jensen's formula at 0 gives ∫₀^R n(x)/x dx ≤ R²/(8t) + O(R), which yields (J).
  4. **L ≡ 0 implies Λ = 0.** (∂_w − 1)K_w = g_t e^{(1−s)w}, so Λ(g_t e^{vs}) = 0 for every real v.
     - The half-Mellin representation G = ½∫a_G(e^v)e^{sv}dv of G ∈ B gives Λ(g_tG) = 0, as an absolutely convergent Bochner integral in B.
     - g_tB is dense in B. Put h_N = e^{ts²}P_N(−ts²), where P_N is the N-th Taylor polynomial of exp. Then |h_N| ≤ e^{2tσ²} on strips, h_N → 1 locally uniformly, and Fh_N = g_t·(F·P_N(−ts²)) ∈ g_tB. So Fh_N → F in B.
     - This makes explicit the "regularisation removal" that the outline skips (see O4).
  5. **The ideal.** The same argument with 8F₀ inserted gives Λ = 0 on F₀g_tB. This set is dense in closure(F₀B) = I_ζ (NCI2.8).
  6. **The count.** For S = {2^a3^b}, ∫_ρ^R (1/x − x/R²)dν = ∫ν(x)(x^{−2} + R^{−2})dx = (4/3)κR + O(log R), with κ = 1/(2 log 2 log 3). (C) holds if and only if (4/3)κ > 1/(3πt).
- **Check.** `check_nb_carleman.py` (all pass).
  - **Carleman's formula.** On f = sin(πz)e^{0.37z²}(z + 3), the remainder is −1.58598, −1.58529, −1.58510 and −1.58505 at R = 10.5, 20.5, 40.5 and 80.5, so it is bounded. The Gaussian factor's contributions to the two integrals cancel, as the structure predicts.
  - **Growth.** For the spread functional Λ(F) = Σ_{|k|≤200}F(ik)/(1 + k²) at t = 0.2, log|L(iv)| − v²/(4t) is −8.3, −10.4, −11.6 and −12.4 at v = 10, 20, 30 and 40, so the constant 1/(4t) is attained. On the real axis log|L(u)| is linear in u.
  - **Lattice count.** ν(800)/κ·800² = 1.0022, and the Carleman sum over (4/3)κR is 1.060, 1.020 and 1.006 at R = 100, 400 and 1600.
  - **g_tB dense.** sup(1 + |τ|)²|Fh_N − F| = 6.9, 0.15 and 1.3·10⁻⁶ for N = 10, 40 and 120, and |h_N|e^{−2tσ²} ≤ 1.
- **Suggested wording.**
  - Prop 3.11: "Fix t > 0. If limsup_R R^{−1}Σ_{n∈S, log n<R}(1/log n − log n/R²) > 1/(3πt), for example if limsup #{n ∈ S : log n ≤ R}/R² = ∞, then 𝒩_S is dense in ℬ and ξ𝒩_S is dense in I_ζ. In particular n ∈ {2^a3^b} gives a dense family for every t > (log 2)(log 3)/(2π)."
  - §9 item 5: "…dense in ℬ for t ≤ (log 2)(log 3)/(2π)? (For larger t it is, by Carleman's formula; F3 of the understatement review.)"
- **Class.** MAJOR. The hypothesis is much weaker than stated, and one of the reader's open questions is answered for an explicit range of t.

### F4. Theorem 2.3 and Corollary 2.4 hold at every "divisor-minimal" element, so negative coefficients are located everywhere, not only the first

- **Location.** §2.2, Theorem 2.3 (a)–(b) and its consequence, p. 7; Corollary 2.4, p. 8.
- **Understated.**
  - The hypothesis of (b): "every smaller element of M has exactly one".
  - The consequence: "the first negative coefficient sits exactly at the least element with two factorizations."
- **Stronger statement.** Let n ∈ M, and suppose every *proper M-divisor* of n factors uniquely. A proper M-divisor is an m ∈ M with 1 < m < n and n/m ∈ M. Let j be the number of factorizations of n, and ε = Σ 1/k over those of the form u^k.
  - Then r_n = 1 − j + ε. If j = 1 this is part (a); if j ≥ 2 it is ≤ −1/6.
  - Corollary 2.4 (coprime exponents, N = c^{j₁j₂}, the value set above −½) holds for every such n.
  - So every divisor-minimal non-factorial element carries a negative coefficient with an explicit value.
  - In a congruence monoid with H ≠ G there are infinitely many such elements, by Dirichlet's theorem. For example, with p ≠ r in a class c ∉ H and p′ ≠ r′ in c^{−1}, n = pp′rr′ has r_n = −1 if c² ∉ H and r_n = −2 if c² ∈ H.
  - The programme's ETR3 coefficient −(d − 1)/2 at p^dr^d (`29_` §2) is another instance.
- **Proof.**
  - In the reader's proof the hypothesis is used once: "each entry [of a k-tuple, k ≥ 2] has exactly one factorization". Every entry of such a tuple is a proper M-divisor of n. Nothing else uses smaller elements.
  - In Corollary 2.4, minimality is used only for N′ = a^{j₁/g} = b^{j₂/g}. Since N = N′^g, N′ is a proper M-divisor of N.
- **Check.** `check_formal_log.py` and `check_formal_log_extra.py`, exact rationals (all pass).
  - The formula r_n = 1 − j + ε holds at all 134, 723, 362 and 535 divisor-minimal elements of {n ≡ 1 mod 4} (up to 20 000), {±1 mod 5} (20 000), {1 mod 5} (30 000) and {±1 mod 7} (20 000), and in ⟨4,8⟩, ⟨8,32⟩, ⟨4,6,9⟩ and ⟨9,27⟩.
  - r_n = ε_n (part (a) in the same form) holds at all elements whose M-divisors all factor uniquely.
  - In the Hilbert monoid the 134 negative coefficients below 20 000 are exactly the divisor-minimal elements.
  - r = −2 at 3·7·11·19, 3·7·11·23 and 7·11·19·23.
- **Suggested wording.** "(b) If n has j ≥ 2 factorizations and every proper M-divisor of n (m ∈ M, 1 < m < n, n/m ∈ M) has exactly one, then r_n = 1 − j + ε ≤ −1/6. … Consequently every element that is not uniquely factored but whose proper M-divisors are carries a negative coefficient; the first negative coefficient sits at the least such element." Cor 2.4: replace "least element with two factorizations" by "an element with two factorizations whose proper M-divisors factor uniquely".
- **Class.** MAJOR. The same proof gives a strictly stronger statement, which locates infinitely many negative coefficients with their values.

### F5. Prop 5.1: the abscissa is 1 + k·β_max for every power k and every finite S. Positivity only places the pole at the real point.

- **Location.** §5.1, Proposition 5.1 ("positivity returns the largest real part"), p. 24. The same point recurs in N-W2 (p. 35): "Positivity of even tensor powers returns max Re ρ".
- **Understated.** "its abscissa of convergence is exactly 1+2kβ_max, where it has a pole". This is stated only for even powers, conjugation-stable S, and attributed to positivity.
- **Stronger statement.** Let S ⊂ ℂ be any finite multiset with positive integer weights, and k ≥ 1 any integer.
  - D_S^{(k)}(s) = Σ_n(Σ m_ρ n^ρ)^k n^{−s} = Σ_w c_w ζ(s − w), with every c_w > 0.
  - The continuation has poles exactly at the points 1 + w, and the rightmost lie on Re s = 1 + kβ_max.
  - Hence σ_c = σ_a = 1 + kβ_max, for every k, whether or not S is conjugation-stable and whether or not the coefficients are nonnegative.
  - Positivity is needed only for Landau's conclusion that the real point 1 + kβ_max is a pole. For odd k that can fail: for the quartet 0.7 ± 10i, 0.3 ± 10i and k = 3 the top poles are 3.1 ± 10i and 3.1 ± 30i, and 3.1 itself is not a pole. The abscissa is still 3.1.
  - So on finite exponent data it is the data, not positivity, that return max Re ρ. N-W2 holds for every tensor degree, positive or not.
- **Proof.**
  - Expanding the power gives the grouped sum Σ_w c_w ζ(s − w), with c_w a sum of products of multiplicities; the reader's own first step, which uses no positivity.
  - For σ > 1 + kβ_max the series converges absolutely.
  - If it converged at some σ₁ < 1 + kβ_max, it would define a holomorphic function on Re s > σ₁. That function would be the continuation, which has a pole of residue c_w > 0 at 1 + w with Re w = kβ_max. This is a contradiction.
- **Check.** `check_abscissa.py` (all pass).
  - Exact grouping for three configurations, including a non-conjugation-stable one. All c_w > 0. The real point is a pole only for even k with conjugation-stable S.
  - The identity series = Σ c_w ζ(s − w) holds to 10⁻¹⁵.
  - For k = 3, the range of the partial sums over dyadic windows [N₀, 2N₀] grows (13.8, 19.3, 29.2, 35.9) at σ = 2.8 < 3.1 and shrinks (0.115 down to 0.037) at σ = 3.4.
- **Suggested wording.** "Proposition 5.1 (the exponent data return the largest real part). For every finite S and every k ≥ 1, D_S^{(k)} is a finite sum of shifted zeta functions with positive coefficients, and its abscissa of convergence is exactly 1 + kβ_max. For even k and conjugation-stable S the coefficients are nonnegative, and 1 + kβ_max is itself a pole with positive residue. …"
- **Class.** MAJOR. The statement is correct in a clearly more general form, and the generality changes what the proposition says positivity contributes.

---

## MINOR findings

### F6. Three proved refinements of §2.2–2.3 from `11_` and `29_` are left out

- **Location.** Theorem 2.3(b), p. 7 ("This number is at most −1/6"); Prop 2.6, proof of (i)⇒(ii), p. 9 ("choose primes p ≠ r in the class c … (Dirichlet)"); Example 2.5, p. 9 ("the absence of zeros in Re s > 1 does not imply freeness").
- **Stronger statements.**
  1. **Congruence monoids.** For M_H with H ≠ G, the first negative coefficient is ≤ −½. With F4, r_n ≤ −½ at every divisor-minimal non-factorial element of M_H.
     - Proof (`11_` Lemma 11.2, step 7): if u^a = v^b with u ≠ v atoms of M_H, then u = w^{b′} and v = w^{a′} with w ∈ M_H, which contradicts atomicity. So at most one factorization of any element is a pure power, ε ≤ ½ and j ≥ 2.
     - The register S23 states this; the reader does not.
  2. **(i)⇒(ii) of Prop 2.6 needs no Dirichlet theorem** (`29_` §1; the programme's CEI Thm 4.1).
     - If H is proper, the Chinese remainder theorem gives infinitely many primes outside H. By pigeonhole some nonidentity coset, of order d ≥ 2, contains two primes p ≠ r.
     - Then A_j = p^{d−j}r^j (0 ≤ j ≤ d) are atoms, and A₀A₂ = A₁².
  3. **Free implies zero-free on the whole half-plane of absolute convergence** (ETR2; `29_` 29.N1).
     - ⟨4,8⟩ is zero-free on its entire half-plane of absolute convergence, Re s > 0, yet it is not free. This is sharper than "Re s > 1".
- **Check.** `check_formal_log.py` F2: in all 46 proper (q, H) with q ≤ 16 that have a negative coefficient below 25 000, the largest first negative value is exactly −½. Items 2 and 3 are proofs from the notes, re-read here.
- **Suggested wording.** Add to Thm 2.3: "For the congruence monoids M_H (H ≠ G) the value is at most −½." Replace "(Dirichlet)" by the pigeonhole argument or add "(Dirichlet's theorem can be avoided: `29_` §1)". In Ex 2.5: "…zero-free on its whole half-plane of absolute convergence Re s > 0, whereas every free monoid is (ETR2)."
- **Class.** MINOR. These are proved results in the notes that the reader omits.

### F7. Props 2.6–2.7 and §2.3: Saias–Weingartner gives about T zeros in every strip, and for prime q ≥ 5 on both sides of the line

- **Location.** Prop 2.6(iv), Prop 2.7 and the "At q = 5" paragraph, p. 9. The caption of Fig. 2, p. 10: "Z_{1/5} has zeros on both sides of the line". The paragraph says "Numerically, Z_{1/5} has 24 zeros with Re s > 0.505" and the status is "checked numerically".
- **Stronger statement.**
  - If H ≠ G, then D_{M_H} has at least c₁T and at most c₂T zeros with σ₁ < Re s < σ₂, |Im s| ≤ T, for all ½ < σ₁ < σ₂ < 1 + η. This is Saias–Weingartner's theorem as quoted in `08_` §1 and `24_` Prop 24.6.
  - For prime q ≥ 5, Z_{1/q} also has at least c₁T zeros with 1 − σ₂ < Re s < 1 − σ₁.
  - So the qualitative claims, infinitely many zeros on each side of the critical line and in Re s < 0, are theorems. Only the specific counts and positions are numerical.
- **Proof.**
  - Hurwitz's formula gives Z_a(1 − s) = 2Γ(s)(2π)^{−s}cos(πs/2)Φ_a(s), with Φ_a = 2Σ_k cos(2πka)k^{−s}.
  - For prime q, Φ_{1/q} has a nonzero ζ-component, (2/(q − 1))(q^{1−s} − 1), and nonzero components τ(χ)-multiples along every nontrivial even primitive χ (Gauss sums are nonzero). For q ≥ 5 there are at least two primitive characters, so Φ_{1/q} is not of the form P·L(s, ψ). For q = 5, Φ_{1/5} = ½[(5^{1−s} − 1)ζ + √5 L(s, (·/5))] (`08_` §2).
  - Saias–Weingartner applies to Φ_{1/q}. Zeros s₀ of Φ with ½ < Re s₀ < 1 + η, Im s₀ ≠ 0, are zeros 1 − s₀ of Z_{1/q}, since the Gamma–cosine factor is finite and nonzero there.
- **Check.** `check_misc.py` item 4 (all pass).
  - The functional equation holds at two points to 10⁻²⁰.
  - The two-character decomposition of Φ_{1/5} holds.
  - Of the 90 zeros in `figures/data/z15_zeros_150.csv`, 24 lie right of the line, 40 in 0 < Re < ½ and 26 in Re ≤ 0. For the six lowest in 0 < Re < ½, Φ_{1/5}(1 − z) vanishes (relative 6·10⁻¹⁸).
  - The saved zeros also confirm the reader's 24/66 split and the gap 0.00681.
  - The Saias–Weingartner theorem itself was not re-read here; it is quoted from its abstract in `24_`.
- **Suggested wording.** In Prop 2.7: "…iff Z_{1/q} has no zeros in Re s > 1; otherwise it has about T zeros up to height T in every strip ½ < σ₁ < Re s < σ₂ < 1 + η [SW], and for prime q ≥ 5 also in the reflected strips to the left of the line." In the caption: "(existence on both sides is a theorem; the positions are computed)".
- **Class.** MINOR. The status "checked numerically" is weaker than what the cited theorem gives.

### F8. Lemma 2.8 holds with complex exponents and for L(s, χ). Lemma 2.9 without normalisation gives μ = ων.

- **Location.** Lemma 2.8, p. 10 ("C₁, …, C_ℓ ∈ ℤ"); Lemma 2.9, p. 10 ("whose total masses are positive reals").
- **Stronger statements.**
  - (i) For distinct σ_j and C_j ∈ ℂ: if Σ_j C_j log ζ(s − σ_j) is constant, equivalently Σ_j C_j ζ′/ζ(s − σ_j) ≡ 0, then all C_j = 0. The same holds with L(s − σ_j, χ) for any Dirichlet character χ.
  - (ii) For finitely supported complex measures, μ^{*d} = ν^{*d} if and only if μ = ων with ω^d = 1. The positivity hypothesis only picks ω = 1.
- **Proof.**
  - (i) The reader's proof uses integrality only to pass from the product to the logarithm. From Σ C_j p^{rσ_j} = 0 onwards it is linear algebra. For χ, divide the p^r-coefficient by χ(p)^r at a good prime p ∤ q.
  - (ii) If ν ≠ 0, then (A/B)^d = 1 on the connected set {B ≠ 0}, which has only isolated points removed. So A/B is a constant d-th root of unity.
- **Check.** `check_misc.py` items 5–6.
  - The coefficient matrix (p^{rσ_j}) has full column rank for random complex σ_j, and also with χ(p)^r (χ mod 5).
  - sympy finds exactly the three solutions ν = ωμ, ω³ = 1, for a two-point μ.
- **Suggested wording.** Lemma 2.8: "C_j ∈ ℂ (the ζ′/ζ(s − σ_j) are linearly independent); the same for L(s − σ_j, χ)." Lemma 2.9: "…then μ = ων with ω^d = 1; if the total masses are positive reals, μ = ν."
- **Class.** MINOR.

### F9. §2.1 summary bullets: Theorem D is unconditional in the verified range, and Corollary B has o(1) error

- **Location.** §2.1 bullets, p. 6.
  - Theorem D: "assuming the zeros up to γ_n are simple and on the line".
  - Corollaries B: "for fixed smoothing width Δ the error … is of the same order T". N-Vel (p. 32) repeats the negative half only.
- **Stronger statements.**
  1. **Theorem D.** The hypothesis holds for every n ≤ N(3·10¹²) ≈ 1.24·10¹³. RH, with simplicity, is verified by Turing's method up to height 3·10¹². By the reader's own Prop 4.9 discussion, that verification is I(T) = 0. So Theorem D is an unconditional theorem for the first 1.2·10¹³ zeros; the copy states this in `03_` §3.1 ("this holds for n ≤ 10¹³").
  2. **Corollary B at a = 1.** The error is O(T₂d(Δ) + K(Δ)) + O(T₁e^{−T₁²/(8Δ²)}). It tends to 0 when Δ ≥ (1 + δ)√(2 log T₂)/log 2 and T₁ ≥ max(10Δ, 4Δ√log Δ). So the smoothed laws, including the −T term of the vertical law, hold with o(1) error for smoothing that grows like √(log T). `02_` §4.2 states the first condition but not the T₁ condition; see O3.
- **Check.** `check_misc.py` items 2–3.
  - The Riemann–von Mangoldt main term gives N(3·10¹²) = 1.236·10¹³.
  - With Δ = 1.1√(2 log T)/log 2, T·d(Δ) = 0.074, 0.028, 0.011 and 0.0015 at T = 10⁴, 10⁶, 10⁸ and 10¹². The n = 2 term dominates, as the proof uses.
- **Suggested wording.** Theorem D: "…(the hypothesis holds unconditionally for n ≤ 10¹³, by the verification of RH to height 3·10¹²)". Corollary B: "…for fixed Δ the horizontal error is of order T, while for Δ ≥ (1+δ)√(2 log T₂)/log 2 (and T₁ ≥ 4Δ√log Δ) both errors tend to 0 at a = 1."
- **Class.** MINOR. The status is understated in summary bullets.

### F10. Prop 3.2 and Lemma 3.3 need only D ≤ div Φ, and Lemma 3.3 has a general form

- **Location.** Prop 3.2, p. 11 ("Let Φ∈B have zero divisor exactly D"). Lemma 3.3, p. 12 ("D the divisor of some F_D ∈ B", "D ∩ D′ = ∅").
- **Stronger statement.**
  - (i) Prop 3.2 (a)–(c) hold whenever D ≤ div Φ for some 0 ≢ Φ ∈ B. For example, D can be the critical-line part or the off-line part of Z, with Φ = ξ; these are the line and off-line ideals of §3.5. No function with divisor exactly D is needed.
  - (ii) For such D and any divisor D′, every linear H: B/I_D → B/I_{D′} with HL = LH takes values in I_{D″}/I_{D′}, where D″ is D′ restricted to the complement of supp D. The disjoint case is H = 0.
- **Proof.**
  - (a) For λ ∉ supp D, use Φ_λ = Φ/(s − λ)^{ord_λΦ} ∈ I_D, which has Φ_λ(λ) ≠ 0.
  - (b)–(c) With m′ = ord_ρΦ ≥ m = D(ρ), use Φ/(s − ρ)^{m′−m+1} and U_ρ = Φ/(s − ρ)^{m′}. Dividing by (s − ρ)^k keeps a function in B.
  - (ii) The reader's argument, applied only at λ ∈ supp D′ ∖ supp D.
- **Check.** By hand: every step of the reader's proof holds with the substituted functions. No numerical content.
- **Suggested wording.** Prop 3.2: "Let 0 ≢ Φ ∈ ℬ vanish to order at least D." Lemma 3.3: "…every L-equivariant linear map takes values in the classes whose jets vanish at every point of D′ outside supp D; in particular it is 0 if D ∩ D′ = ∅."
- **Class.** MINOR.

### F11. Lemma 3.4 extends to generalised exponentials

- **Location.** Lemma 3.4, p. 12 ("If Σ_ρ c_ρ e^{ρx} = 0 for every real x, then c = 0").
- **Stronger statement.** Let m_ρ = ord_ρG. Take coefficients c_{ρ,k}, for ρ ∈ Z and 0 ≤ k < m_ρ, with Σ|c_{ρ,k}|k!R^{−k} < ∞ for some R > 0. If Σ_{ρ,k} c_{ρ,k}x^k e^{ρx} = 0 for every real x, then all c_{ρ,k} = 0. This is the natural statement for the Jordan blocks of §3.2.
- **Proof.**
  - F^{(k)}(ρ) = ½∫a_F(e^v)v^k e^{ρv}dv. The bound |v|^k ≤ k!R^{−k}e^{R|v|} and the super-exponential decay of a_F justify Fubini.
  - So Σ c_{ρ,k}F^{(k)}(ρ) = 0 for all F ∈ B.
  - Take F = G(s − ρ₀)^{−m}P(s − ρ₀). The polynomial P prescribes any jet of order < m at ρ₀, and F vanishes to order m_ρ at every other ρ, as in Prop 3.2(c). This gives c_{ρ₀,·} = 0.
- **Check.** By hand. The input identity for F^{(k)} follows from the half-Mellin representation NJS4.1, which the reader uses.
- **Suggested wording.** Add "(more generally, Σ c_{ρ,k}x^k e^{ρx} ≡ 0 with k < m_ρ and Σ|c_{ρ,k}|k!R^{−k} < ∞ forces c = 0)".
- **Class.** MINOR.

### F12. Lemma 3.6 and Corollary 3.7

- **Location.** Lemma 3.6, p. 13 ("a nontrivial zero ρ = β + iγ"). Cor 3.7, p. 13 ("is a proper dense subspace of the product").
- **Stronger statements.**
  - (i) The bound holds at every point ρ with |Re ρ| ≤ 3/2. The factor 2^M can be replaced by ((1 + |γ|)/(½ + |γ|))^M, which is at most 1.0342^M at the zeros.
  - (ii) J(Q) lies in Λ_m, the rapidly decreasing jet tuples, and is dense there. This is much sharper than "proper": J(Q) misses every tuple that is not rapidly decreasing. Theorem 3.9(d) says J(Q) = Λ_m exactly under (c). The reader proves J(Q) ⊂ Λ_m only inside the proof of Theorem 3.9.
- **Proof.**
  - (i) 1 + |Im z| ≥ ½ + |γ| on the circle, and the circle lies in |Re z| ≤ 2.
  - (ii) Lemma 3.6 with m_ρ ≪ log|γ| (D1). Finitely supported tuples are dense in Λ_m, since p_M(P − P_{≤T}) ≤ (1 + T)^{−1}p_{M+1}(P).
- **Check.** `check_more.py` (g): the sharper bound holds for the first 20 zeros with F = e^{s²/100}, r ≤ 2, M ≤ 3 (maximum ratio 0.786).
- **Suggested wording.** Cor 3.7: "J(Q) is a dense subspace of the space Λ_m of rapidly decreasing jet tuples (in particular a proper subspace of the product)…".
- **Class.** MINOR.

### F13. Theorem 3.9: add rapid decay to the equivalences, and note that it holds for every primitive L(s, χ)

- **Location.** Theorem 3.9, p. 14 ("(b) Σ_ρ Π_ρ x converges absolutely for every x ∈ Q").
- **Stronger statements.**
  - (i) (a)–(d) are also equivalent to (b′): for every x, every continuous seminorm q and every N, q(Π_ρx) = O((1 + |γ|)^{−N}).
  - (ii) The theorem and its proof hold verbatim for B/I_χ, the zero-jet quotient of L(s, χ) for primitive χ, with the principal parts of 1/L(s, χ) in (c).
- **Proof.**
  - (i) (d) gives q(J^{−1}P) ≤ Cp_M(P). Since Π_ρx = J^{−1}(x̂_ρδ_ρ), q(Π_ρx) ≤ C(1 + |γ|)^{−N}p_{M+N}(Jx). And (b′) ⇒ (b) ⇒ (a).
  - (ii) The proof uses (D1), (D2), good heights (Titchmarsh 9.7), |1/ζ| ≤ ζ(2) on σ = 2, a lower bound on σ = −1 from the functional equation, polynomial growth on strips, and N(T) ≪ T log T. Each has the standard L(s, χ) analogue: Davenport ch. 16 for (D1) and (D2), with the same Titchmarsh argument for good heights; |1/L(2 + it)| ≤ ζ(2); |L(−1 + it, χ)| ≫ (1 + |t|)^{3/2} for |t| ≥ 2 from Λ(s, χ) = WΛ(1 − s, χ̄); and the growth step of Prop 4.12. Λ_χ ∈ B supplies the sections.
- **Check.** `check_more.py` (d) for χ mod 5 with χ(2) = i: max |1/L(2 + it)| = 1.41 ≤ ζ(2), and min |L(−1 + it)|/(1 + |t|)^{3/2} = 0.38 for 2 ≤ |t| ≤ 100. At t = 0, L(−1, χ) = 0, a trivial zero, which the proof's rectangles avoid.
- **Suggested wording.** Add "(b′) Π_ρx → 0 faster than every power of 1 + |γ|, for every x" and a remark: "The theorem holds verbatim for the quotient of every primitive Dirichlet L-function."
- **Class.** MINOR.

### F14. Prop 3.12: the closure has infinite codimension

- **Location.** Prop 3.12, p. 16 ("then 𝒩_S is not dense in ℬ").
- **Stronger statement.**
  - The closures of 𝒩_S in B and of ξ𝒩_S in I_ζ have infinite codimension.
  - If F = ∅, closure(𝒩_S) is contained in the ideal of functions vanishing at every 2πij/log a, j ≠ 0.
- **Proof.** For any J, the combinations of the evaluations at s₁, …, s_{J+|F|} that satisfy the |F| conditions form a space of dimension at least J. Distinct evaluations are linearly independent on B, and also on I_ζ, by the reader's g_tξP argument.
- **Check.** `check_misc.py` item 7, a = 2, F = {3, 5, 7}: for J = 3 and 6 there are exactly J independent combinations, and they kill every generator 2^k (k < 25) and n ∈ F to 10⁻¹⁰.
- **Suggested wording.** "…then the closures of 𝒩_S in ℬ and of ξ𝒩_S in I_ζ have infinite codimension."
- **Class.** MINOR.

### F15. Global residue duality: the sharper constant from `26_`

- **Location.** §3.5, "Global residue duality" bullet, p. 17 ("|B_ζ(F,G)| ≤ ζ(2)(1+4π²)π^{−1} b_{2,1}(F) b_{2,1}(G)").
- **Stronger statement.**
  - The constant ζ(2)(1/π + 8π/5) ≈ 8.792 is valid; the reader prints ≈ 21.19. `26_` §2.1 records this constant from the eighth referee pass.
  - B(P(L)x, y) = B(x, P(1 − L)y) for every polynomial P (`26_` Lemma 26.1(d)).
- **Proof.** Keep the factor (1 + |t|)^{−3/2} in |1/ζ(−1 + it)| ≤ 4π²ζ(2)(1 + |t|)^{−3/2}. Then ∫(1 + |t|)^{−7/2}dt = 4/5 in place of ∫(1 + |t|)^{−2}dt = 2.
- **Check.** `check_misc.py` item 1.
  - The bound on |1/ζ(−1 + it)| holds on [0, 400], with maximum ratio 0.444.
  - The constant is recomputed.
  - `check_duality_nontrivial.py`: for F = e^{(s−ρ₁)²} and G = e^{(s−1+ρ₁)²}, the two-contour value of B_ζ is 1.24510 − 0.19822i. It equals the residue sum Σ F(ρ)G(1−ρ)/ζ′(ρ) to 15 digits and lies below both bounds (5.4·10⁸ and 1.3·10⁹). The bound is far from tight for such tests, so the constant itself is checked by the integral computation.
- **Suggested wording.** "…≤ ζ(2)(1/π + 8π/5) b_{2,1}(F)b_{2,1}(G) ≈ 8.79 b_{2,1}(F)b_{2,1}(G)…; B(P(L)x, y) = B(x, P(1 − L)y) for every polynomial P".
- **Class.** MINOR. A constant from the notes is understated.

### F16. Prop 4.3 (the blind lemma): one dilation suffices

- **Location.** Prop 4.3, p. 19 ("with KU_a = U_aK for all a>0 is zero").
- **Stronger statement.** If σ ≠ σ′ and K is bounded with KU_{a₀} = U_{a₀}K for a single a₀ ≠ 1, then K = 0.
- **Proof.** Commuting with U_{a₀} implies commuting with U_{a₀}^k = U_{a₀^k} for all k ∈ ℤ, since U_{a₀} is invertible. The reader's estimate ‖Kf‖ ≤ a^{σ′−σ}‖K‖‖f‖ with a = a₀^k and k → ±∞ gives Kf = 0.
- **Check.** By hand.
- **Suggested wording.** "…every bounded K with KU_a = U_aK for one a ≠ 1 is zero."
- **Class.** MINOR.

### F17. Prop 4.6 and Thm 4.2: an unconditional orthogonal splitting, the negative index, and every primitive L(s, χ)

- **Location.** Prop 4.6(c), p. 20 ("Under RH the T-even data form a maximal positive subspace for Q_A"). Thm 4.2 and Prop 4.6 are stated for ζ.
- **Stronger statements.**
  - (i) V₊ (T-even) and V₋ (T-odd) are Q_A-orthogonal unconditionally. So Q_A = 2Ω|_{V₊} ⊕ (−2Ω)|_{V₋}.
  - (ii) On T-even data supported on a finite #-closed set, the negative index of Q_A equals the number of off-line pairs in the support, and the signature is (n_on + n_pairs, n_pairs).
  - (iii) Under RH, V₋ is maximal negative.
  - (iv) Thm 4.2 and Prop 4.6 hold for every primitive L(s, χ), complex χ included. Z_χ is #-invariant: Λ(s, χ) = WΛ(1 − s, χ̄) together with conj L(s̄, χ̄) = L(s, χ) gives 1 − ρ̄ ∈ Z_χ. G_χ has no zeros on Re s = 0.
  - (i) and (iii) are in `42_` Prop 42.2(c); the reader drops them.
- **Proof.**
  - (i) Q_A(u + v) = 2Ω(u) − 2Ω(v) for all T-even u and T-odd v, including iv, so the polarisation vanishes.
  - (ii) Each on-line zero gives a positive square; each off-line pair gives a hyperbolic plane.
  - (iv) The reader's proofs use only the #-invariance and the zero-freeness of Re s = 0.
- **Check.** `check_more.py` (b) and (c).
  - The signature (n_on + n_pairs, n_pairs) holds for all n_on, n_pairs ≤ 4.
  - For χ mod 5 with χ(2) = i, five zeros from 0.5 + 6.18358i up satisfy |L(1 − ρ̄, χ)| ≤ 4·10⁻²⁵, while |L(1 − ρ, χ)| = 2.8.
- **Suggested wording.** "(c) Unconditionally V₊ ⊥_{Q_A} V₋ and Q_A = 2Ω ⊕ (−2Ω); on T-even data the negative index is the number of off-line pairs in the support; under RH V₊ is maximal positive and V₋ maximal negative." Remark: "Theorem 4.2 and Proposition 4.6 hold for every primitive Dirichlet L-function."
- **Class.** MINOR.

### F18. Prop 4.10: every modulus and every pair of classes

- **Location.** Prop 4.10, p. 22 ("hence the two-line races mod 4 differ from the one-line races").
- **Stronger statement.** For every q and all classes a ≢ b coprime to q, the two-line θ-race and counting race differ from the one-line races by convergent series. The same holds for r-way races. So the limiting logarithmic distribution (under GRH) and the densities δ(q; a, b) (under GRH and linear independence) are unchanged.
- **Proof.** The difference is φ(q)^{−1}Σ_{χ≠χ₀}(χ̄(a) − χ̄(b))Σ_{p≤x}χ(p)log p/p. The principal character cancels, and each inner series converges by the note's own (a).
- **Check.** `check_races_all_moduli.py`, primes up to 10⁷, q ∈ {3, 5, 8, 12}, nine pairs.
  - The corrections converge. For example, mod 5 (2, 1): 0.5897, 0.5721, 0.5804, 0.5799, 0.5808 at x = 10³ … 10⁷.
  - Divided by √x they are ≤ 2.3·10⁻⁴ at 10⁷.
- **Suggested wording.** "…hence for every modulus q and every pair of classes the two-line races differ from the one-line races by convergent series… (for q = 4, δ(4; 3, 1) ≈ 0.9959)".
- **Class.** MINOR.

### F19. Prop 4.12: the same proof gives the separator for Dedekind zeta functions

- **Location.** Prop 4.12, p. 23 ("the separator for every primitive Dirichlet L-function"), and N-Unif4, p. 34.
- **Stronger statement.** For every number field K of degree n, with ξ_K = s(s − 1)Λ_K ∈ B, there is a separator E_K. So B/(I_K ∩ I_{K,−}) ≅ B/I_K ⊕ B/I_{K,−} equivariantly, with α = nπ/2 in Lemma 4.11.
- **Proof.** The same three inputs are available: Hecke's Λ_K(s) = Λ_K(1 − s), ζ_K(1 + it) ≠ 0, and Stirling.
  - Γ_ℝ(1 − s)Γ_ℝ(1 + s) = 1/cos(πs/2) and Γ_ℂ(1 − s)Γ_ℂ(1 + s) = s/(π sin πs). These have the same exponential size, e^{−π|t|/2} and |t|e^{−π|t|}, on every vertical line, so the rates match at α = (r₁ + 2r₂)π/2.
  - The lower rate comes from the 3-4-1 inequality ζ_K(σ)³|ζ_K(σ + it)|⁴|ζ_K(σ + 2it)| ≥ 1 and polynomial bounds, exactly as in steps 3–5 of the reader's proof.
- **Check.** `check_more.py` (e), K = ℚ(i).
  - ξ_K(s) = ξ_K(1 − s) to 10⁻¹⁸.
  - log(|G_K(x + it)|e^{π t}) has local polynomial order between 5.5 and 8.5 on the lines x = −1.5, 0, 0.7 and 2 for t between 40 and 80, and is bounded below on Re s = 0. So the rates match at α = π.
- **Suggested wording.** Add to the proof or to N-Unif4: "The same argument gives the splitting for every Dedekind zeta function (α = nπ/2)."
- **Class.** MINOR.

### F20. Lemma 4.13: the direction of monotonicity

- **Location.** Lemma 4.13, p. 23 ("it is strictly monotone in |x| on (0, ½)").
- **Stronger statement.** The ratio is increasing in |x| if r > t and decreasing if r < t (`24_` Lemma 24.5(b)).
- **Proof.** a coth(ax) − b coth(bx) has the sign of a − b, by the reader's own monotonicity of c ↦ c coth(cx).
- **Check.** `check_more.py` (f): on 12 pairs (r, t), the ratio is increasing exactly when r > t.
- **Suggested wording.** "…strictly increasing in |x| if r > t (decreasing if r < t)…".
- **Class.** MINOR.

### F21. Lemmas 5.5 and 5.6

- **Location.** Lemma 5.5, p. 26 ("ν: K̂ → ℤ"). Lemma 5.6, p. 27 ("δ ∈ ℝ with δ − Σ_j a_j^n real and ≥ 0").
- **Stronger statements.**
  - (i) Lemma 5.5's inequality Σ_{τ≠1}d_τ(−ν(τ)) ≤ 1 holds for real-valued ν. Integrality and ν(τ̄) = ν(τ) are used only for the final dichotomy: one quadratic τ with ν = −1.
  - (ii) Lemma 5.6 holds with real δ_n ≤ C·D^n (D ≥ 1) in place of a constant δ; the conclusion is max|a_j| ≤ D. Corollary: for a curve over F_q, #X(F_{q^n}) = 1 + q^n − Σα_j^n ≥ 0 alone gives |α_j| ≤ q. This is the trivial bound, obtained from positivity by the same lemma.
- **Proof.**
  - (i) The reader's chain 0 ≤ ν(ρρ̄) ≤ M + Σ_T(1 − e)d_τMν(τ) never uses integrality.
  - (ii) In the Dirichlet-approximation step, δ_n − Re Σa_j^n ≤ CD^n − |J|R^n/2 + O(R′^n), which tends to −∞ if R > D.
- **Check.** `check_more.py` (a).
  - With a = (1.5e^{±0.3i}, −0.7) and δ_n = 2D^n + 1, nonnegativity holds for n ≤ 399 at D = 1.6 and 1.5 and fails at D = 1.4.
  - For an elliptic curve with q = 7, the point counts are ≥ 0 and |α| = √7 ≤ 7.
- **Suggested wording.** Lemma 5.5: "ν: K̂ → ℝ … then Σ_{τ≠1}d_τ(−ν(τ)) ≤ 1; if ν is integer-valued, at most one τ ≠ 1…". Lemma 5.6: "…with δ_n − Σa_j^n real and ≥ 0 and δ_n ≤ CD^n; then max|a_j| ≤ D."
- **Class.** MINOR.

### F22. Four auxiliary statements of §6 assume more than they use

- **Location and stronger statements.**
  - **Prop 6.2**, p. 28 ("The closure of p^ℤ in ∏_{q≠p}ℤ_q^× is a copy of Ẑ"). The same holds for every integer a ≥ 2 in ∏_{ℓ∤a}ℤ_ℓ^×, since a has exact order d mod a^d − 1. Checked: `check_misc.py` item 9, a ∈ {6, 10, 12}, d < 25.
  - **Lemma 6.4**, p. 30 ("a ≥ 2"). Every clause except "no reflected pair returns together" holds for every real a > 1. That clause needs a ≥ 2: for 1 < a < 2 a pair with 1 − 1/a < Re ρ < 1/a returns.
  - **Prop 6.5**, p. 30 ("so if RH is independent of T, it is true"). The proof gives "if T ⊬ ¬RH then RH". Σ₁-soundness is not needed for Con(T + RH) ⇒ RH (`23_` (b), referee n2). Recursive axiomatisability is used only to arithmetise Con and for Gödel II. The paragraph after the proposition says the stronger form; the statement does not.
  - **Lemma 6.6**, p. 31 ("V an affine vector field"). div U = (div V)∘F and "F maps U-curves to V-curves" hold for every C¹ field V; U is polynomial if V is. "Affine" is used only for completeness, and for a polynomial automorphism U is complete exactly when V is. Checked: `check_misc.py` item 8. For the reader's F and the non-affine V = (x² + y, yz, x³ − z), det DF = −2 and |div U − (div V)∘F| ≤ 1.4·10⁻³⁹ at random points.
- **Proof.** Each is the reader's proof with the hypothesis dropped where it is not used. The Piola computation in Lemma 6.6 never differentiates V twice.
- **Suggested wording.** Replace p by an integer a ≥ 2 in Prop 6.2. Write "a > 1 (a ≥ 2 for the reflected-pair clause)" in Lemma 6.4. Add "(indeed, if T does not refute RH, RH holds)" in Prop 6.5. Write "V a C¹ vector field (affine, for completeness)" in Lemma 6.6.
- **Class.** MINOR.

---

## Overclaims and gaps noticed (listed separately)

- **O1. Prop 5.2, p. 25.**
  - The text says "det(W_p|V_ρ) = p^{2m}, … divided by the rank 4m is 1, whatever Re ρ is", for V_ρ the span of the blocks of ρ, ρ̄, 1 − ρ, 1 − ρ̄.
  - For an on-line zero the four points are only two, since 1 − ρ̄ = ρ. Then V_ρ has rank 2m and det(W_p|V_ρ) = p^m. The conclusion, average weight 1, still holds.
  - Suggested fix: "Let ρ be an off-line zero …", or treat the on-line case separately.
- **O2. Corollary 2.2, p. 6.**
  - "ζ(s,1+t) has an Euler product" is literally true only after the normalisation a^sζ(s, a). At t = −½, ζ(s, ½) = 2^s∏_{p>2}(1 − p^{−s})^{−1}.
  - Suggested fix: "a^sζ(s, a), a = 1 + t, has an Euler product …".
- **O3. Source note `02_` §4.2, not the reader.**
  - "If Δ ≥ (1+δ)√(2 log T₂)/log 2, both errors tend to 0" omits the term O(T₁e^{−T₁²/(8Δ²)}) of the same corollary, which tends to 0 only if T₁/Δ → ∞ (for example T₁ ≥ 4Δ√log Δ). See F9.
- **O4. Prop 3.11 outline, p. 16: a gap.**
  - "the half-Mellin representation extends this to Λ = 0" gives, as written, only Λ = 0 on g_tℬ. The missing step, density of g_tℬ in ℬ, is the programme's NHJ4 regularisation removal, which `16_` read only through its displayed result.
  - F3, step 4, supplies a two-line proof via h_N = e^{ts²}P_N(−ts²). The status "audited (`16_`)" is therefore thinner than it reads for this step.

No other overclaim was found in Sections 2–6.
- I re-checked the numbers the reader quotes: the velocity 0.98358 + 9.65780i (reproduced as 0.98358249 + 9.657804i), r₃₆ = −½, and the 24/66 split and 0.0068 for Z_{1/5} (from `figures/data/z15_zeros_150.csv`). The bound 2.7·10⁻³⁹ in Lemma 6.3 I re-checked by hand.
- Statements examined without an understatement worth reporting: Lemma 3.1, Prop 3.5, Lemma 3.8, Props 4.4, 4.5, 4.8 and 4.9, Lemma 4.11, Prop 5.3, Lemma 5.4, Cor 5.7, Prop 6.1 and Lemma 6.3. Some of these hold in wider generality (for example Props 4.8–4.9 for L-functions), but trivially.

---

## Checks run

All scripts and their outputs are in `checks/zeta_reader_review/`. They use mpmath (25–60 digits), sympy, numpy and exact `Fraction` arithmetic. Every script ends with "ALL CHECKS PASS". Runtimes are 1–15 s each.

| Script (output file) | Findings | What it verifies |
|---|---|---|
| `check_formal_log.py` (`_OUTPUT.txt`), plus `check_formal_log_extra.py` | F4, F6 | r_n = 1 − j + ε at every divisor-minimal element of 9 monoids, and r_n = ε_n when all M-divisors factor uniquely. The first negative value is ≤ −½ in all 46 proper congruence monoids with q ≤ 16. r = −2 at products of four primes ≡ 3 mod 4. |
| `check_hurwitz_jet_all_sheets.py` | F1 | ∂_aζ = −sζ(s + 1, a) on 5 sheets; the value −1 at s = 0; jet zeros equal shifted zeros on 4 sheets, both directions; the m = 3 jet; the a = ½ counterexample to #-symmetry. |
| `check_transfer_forms.py` | F2 | The free entries for n ∈ {2, 3} are exactly (ρ, ρ#); n = 2 alone admits extra forms; the transfer identity for real n; the positivity criterion on 4000 random forms. |
| `check_nb_carleman.py` | F3 | The Carleman remainder is bounded; the growth v²/(4t) is attained and the real-axis growth is linear; the lattice constant; the thresholds 0.12120 and 0.38075; h_N → 1 with \|h_N\| ≤ e^{2tσ²}. |
| `check_abscissa.py` | F5 | Grouping into Σc_wζ(s − w) with c_w > 0; no real pole for odd k; the identity to 10⁻¹⁵; divergence and convergence on either side of the abscissa. |
| `check_races_all_moduli.py` | F18 | Convergent race corrections for q = 3, 5, 8, 12, primes up to 10⁷. |
| `check_misc.py` | F6–F9, F14, F15, F22, and reader numbers | Residue-duality constants and bound; N(3·10¹²); T·d(Δ(T)) → 0; the Hurwitz functional equation and the left zeros of Z_{1/5}; Lemma 2.8 rank; Lemma 2.9 roots of unity; infinite codimension; Lemma 6.6 with non-affine V; composite bases in Prop 6.2; the velocity ρ₁ζ(ρ₁+1)/ζ′(ρ₁). |
| `check_duality_nontrivial.py` | F15 | A nontrivial value of B_ζ; contour equals residue sum; the bound with 8.79. |
| `check_more.py` | F12, F13, F17, F19–F21 | Lemma 5.6 with δ_n = CD^n; the signature of Weil's pairing; #-symmetry of Z_χ (χ mod 5 complex); L-function inputs for Thm 3.9; matched rates for ζ_{ℚ(i)}; the direction in Lemma 4.13; the sharper Lemma 3.6 constant. |

**Not checked here.**
- The printed statement of Saias–Weingartner's Theorem 4; it is quoted from the abstract in `24_`.
- The page references in Davenport ch. 16 for the L-function versions of (D1)–(D2) in F13; these are standard, but I did not re-read them.
- Titchmarsh's statement of Carleman's formula; I verified its form numerically and did not re-read it.
- No web access was used.
