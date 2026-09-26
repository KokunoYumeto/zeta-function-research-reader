# The Collatz workbench: history laws, merging families, small cycle exclusions, the Tao-clock deduction and the Hurwitz encoding

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 26 September 2026, 05:34 UTC; revised 06:39 UTC after the twentieth referee pass (§12).

Second note of board task 10, part 2. Subject: `KokunoYumeto/collatz-workbench` at commit `caf04ff` (main; the 16 September cumulative collection and its later additions). The inventory (`47a` §7) had found no Collatz repository among the provided ones; the owner's public Collatz workbench was cloned read-only for this note.

**How this note was made.** As for `43_`: a first-pass audit by a Claude subagent (report reproduced as `44a_COLLATZ_FIRST_PASS_AUDIT_REPORT.md`, "44a"; scripts in `checks/workbenches/audit44_collatz/`), whose six independent scripts other than the 168-second Tao-clock one I re-ran on 26 September with identical results (`rerun_20260926/collatz/`; the workbench's own checkers were run by 44a and not re-run); an independent check of my own from the definitions (`workbench_reader_claims_checks.py`, section CZ; all pass); and my own re-derivation of the proofs given below. Status labels as in `43_`.

**Notation.** X is the set of positive odd integers; T(n) = (3n+1)/2^{ν₂(3n+1)} on X. The *exponent word* of n of length m is (a₁, …, a_m), a_i = ν₂(3x_{i−1} + 1), x₀ = n, x_i = T(x_{i−1}); A = a₁ + … + a_m.

The workbench states in every note that it does not claim the Collatz conjecture; its chapters describe themselves as written proofs with exact finite checks, not externally reviewed, and no chapter has a Lean file (44a §1(b)).

**Credit, as the workbench records it.** The public collaboration name is Kokuno Yumeto; the contributions were developed with ChatGPT 5.6 Sol (Ultra mode, in Codex) and GPT-6 Astra; source authors retain their attribution (README, "Collaboration and source history"). The early `research_program` tree is quarantined by the owner's directive; the quarantine withdraws those statements from use and does not show any of them false (44a §4).

## 0. Summary

| Result | Status |
|---|---|
| 44.1 Cylinder classes and exact counts in windows of odd starts (Ch. 1) | audited; classical mechanism (Terras, Everett; Tao Prop. 1.9) |
| 44.2 The full-history threshold: TV distance to the geometric model tends to Φ(2c) at m = L/2 + c√L (Ch. 1) | audited |
| 44.3 ν₃((2^e+2)/3) = ν₃(e−1) (Ch. 20, Lemma 1) | audited |
| 44.4 Two-template merging families for every even interior exponent (Ch. 20, Thm 2) | audited |
| 44.5 Finite template search at each odd n (Ch. 20, Thm 3) | audited |
| 44.6 Reference-3 stopping leaves force descent (Ch. 2, Thm 2.1) | audited |
| 44.7 √15/4 contraction in the fair-coin model (Ch. 2, Thm 7.1) | audited |
| 44.8 No nontrivial cycle with at most one exponent-1 step (Ch. 3) | audited |
| 44.9 No nontrivial cycle with at most 678 exponent-1 steps (Ch. 6, Thm 9) | audited (its hypothesis, that every odd n ≤ 330,749 reaches 1, was recomputed here) |
| 44.10 Collatz ⟺ an explicit abelian group vanishes (Ch. 9) | re-derived from the overview's statement; the chapter's proof located; a restatement |
| 44.11 Coherent first-entry limit laws from Tao's Prop. 1.11 (Tao-clock preprint) | conditional on Tao's Prop. 1.11 (cited) |
| 44.12 The Hurwitz zero-cluster encoding (split-zero note) | audited; an encoding with no dynamical content |
| Chapters 4, 5, 7, 8, 10–19; the research companion; the Siegel edition | located |

## 1. History laws (Ch. 1, `history_law_cutoff_20260914`)

**Proposition 44.1 (cylinders and exact counts).** For every exponent word w of length m and sum A there is a residue h_w modulo 2^A such that an odd n = 2k + 1 has exponent word w exactly when k ≡ h_w (mod 2^A). Consequently, among the N consecutive odd starts 2k + 1, b ≤ k ≤ b + N − 1, the number with word w is ⌊(b + N − 1 − h_w)/2^A⌋ − ⌊(b − 1 − h_w)/2^A⌋, and the empirical frequency P(w) satisfies |P(w) − 2^{−A}| ≤ 1/N.

This is the classical cylinder lemma (Terras 1976; Everett 1977), which the note credits through Tao's Proposition 1.9 mechanism; the note claims no priority. (My check: every word with A ≤ 11 of lengths 1–3 is realised by exactly one class of odd n modulo 2^{A+1} among n < 2¹⁵.)

**Theorem 44.2 (the full-history threshold).** Let G_m(w) = 2^{−A(w)} (independent exponents with P(a = j) = 2^{−j}), L = log₂N, and Δ = TV(P, G_m).
- (a) For every H ≥ m: max{0, Q_m(H) − N·2^{−H−1}} ≤ Δ ≤ min{1, Q_m(H) + C(H, m)/N}, where Q_m(H) = P(Bin(H, ½) ≤ m − 1) and C(H, m) = #{w : |w| = m, A(w) ≤ H} = binom(H, m).
- (b) If m = ⌊L/2 + c√L⌋, then sup_b |Δ − Φ(2c)| → 0 as N → ∞.
- (c) Δ → 0 uniformly in b if m ≤ (½ − δ)L, and Δ → 1 if m ≥ (½ + δ)L.

*Proof.* Under G_m, A is the waiting time for the m-th success in fair coin flips, so G_m(A > H) = Q_m(H).
- Upper bound: Δ = 1 − Σ_w min(P(w), G(w)), and by Proposition 44.1 the words with A ≤ H contribute at least Σ_{A≤H}(2^{−A} − 1/N) = 1 − Q_m(H) − C(H, m)/N.
- Lower bound: P is supported on at most N words, and a word with A > H has G-mass at most 2^{−H−1}; so Σ_{A>H} min(P, G) ≤ N·2^{−H−1}, while Σ_{A≤H} min(P, G) ≤ 1 − Q_m(H).
- (b) Take H₊ = L + L^{1/4} in the lower bound and H₋ = L − L^{1/4} in the upper bound. Then N·2^{−H₊−1} → 0 and C(H₋, m)/N ≤ 2^{H₋ − L} → 0. By the central limit theorem for Bin(H, ½) (uniform in the argument, with error O(H^{−1/2})), Q_m(H±) = Φ((2m − 2 − H±)/√H±) + o(1), and (2m − 2 − H±)/√H± → 2c.
- (c) Hoeffding's inequality in the same squeeze. ∎

*Checks.* 44a: the cylinder lemma on all odd n < 2²⁰ for m ∈ {1, 3, 6}; 2,952 sandwich checks. At N = 2²⁰ the numerical TV values are 0.004, 0.044, 0.342, 0.668, 0.895 for c = −1, −½, 0, ½, 1, against Φ(2c) = 0.023, 0.159, 0.5, 0.841, 0.977: the convergence is slow, as the note warns.

*Scope.* Theorem 44.2(c) is an obstruction: above (½ + δ)log₂N halving counts, the whole word law of N consecutive starts is far from the geometric model. It says nothing about coarser observables (descent, entrance locations) or about individual orbits. No literature search on this threshold was made.

## 2. Merging families (Ch. 20, `all_even_join_extension_20260916`)

**Lemma 44.3.** For even e ≥ 2, h_e = (2^e + 2)/3 is an integer, h_e ≡ 2 (mod 4), and ν₃(h_e) = ν₃(e − 1).

*Proof.* 2^e ≡ 1 (mod 3) gives integrality; 2^e + 2 ≡ 2 (mod 4) and 3 is odd give h_e ≡ 2 (mod 4). With k = e − 1 odd, 2^e + 2 = 2(2^k + 1), and the lifting-the-exponent lemma for the odd prime 3 (3 | 2 + 1, k odd) gives ν₃(2^k + 1) = ν₃(2 + 1) + ν₃(k) = 1 + ν₃(k). So ν₃(h_e) = ν₃(2^k + 1) − 1 = ν₃(e − 1). ∎ (My check: all even e ≤ 3000.)

**Theorem 44.4 (explicit merging families).** Fix an even e ≥ 2, an integer b ≥ 1 and σ ∈ {0, 1}. Let a be the least a ≥ 1 with 2^{a+e+2b−σ} < 3^{a+b}; put J = 2^{e+2b−σ}, Q = 3^{a+b}, K = 2^aJ, (d, r) = (4, 3) if σ = 0 and (32, 27) if σ = 1. Let n₀ ∈ (0, dQ) solve n₀ ≡ r (mod d) and Jn₀ + h_e3^b ≡ 0 (mod Q), and m₀ = (Kn₀ + 2^ah_e3^b)/Q − 1. For every v ≥ 0, n = n₀ + dQv and m = m₀ + dKv are odd, 0 < m < n, ν₃(n) = b + ν₃(e − 1), and the orbits meet: the exponent word of n begins with (1) (σ = 0) or (1, 2, 1) (σ = 1), that of m begins with (1^a, e, 2^{b−1}, 3) (σ = 0) or (1^a, e, 2^{b−1}, 1, 1, 3) (σ = 1), and both words end at the same odd number.

*Proof.*
1. *Range of a.* At a = b + 2e − 2σ one has K/Q = (8/9)^{b+e−σ} < 1, so a ≤ b + 2e − 2σ. If a ≤ e − 1 then (3/2)^a < 2^{e−1}, while K < Q needs (3/2)^a > 2^{e−σ}(4/3)^b; so a ≥ e > ν₃(e − 1).
2. *The 3-adic part.* J is a unit mod 3, so n ≡ −h_e3^bJ⁻¹ (mod 3^{a+b}); since ν₃(h_e3^b) = b + ν₃(e−1) < a + b, ν₃(n) = b + ν₃(e − 1). Put z = n/3^b and W = (Jz + h_e)/3^a, an integer. As 4 | J and h_e ≡ 2 (mod 4), ν₂(W) = 1; and m = 2^aW − 1.
3. *The right path.* Since m + 1 = 2^{a+1}(W/2) with W/2 odd, the first a steps from m have exponent exactly 1, through x_j = 3^j2^{a−j}W − 1, ending at x_a = 3^aW − 1 = Jz + h_e − 1, which is odd. Using 3h_e − 2 = 2^e, 3x_a + 1 = 2^e(3·2^{2b−σ}z + 1), and 2b − σ ≥ 1, so the next exponent is exactly e and x_{a+1} = 3·2^{2b−σ}z + 1. The next b − 1 steps have exponent 2 and end at 4n + 1 (σ = 0) or 2n + 1 (σ = 1).
4. *The meeting point.* σ = 0: n ≡ 3 (mod 4), so T(n) = (3n + 1)/2 with exponent 1, and 3(4n + 1) + 1 = 4(3n + 1) = 8·((3n+1)/2) gives exponent 3 and the same value. σ = 1: from n ≡ 27 (mod 32), the left path n → (3n+1)/2 → (9n+5)/8 → (27n+23)/16 has exponents 1, 2, 1, and the right tail 2n + 1 → 3n + 2 → (9n+7)/2 → (27n+23)/16 has exponents 1, 1, 3.
5. *Height.* m = (K/Q)n + h_e(2/3)^a − 1, with K < Q, and h_e(2/3)^a < h_e3^b/J = ((2 + 2^{2−e})/3)·2^{σ−1}(3/4)^b < 1. So 0 < m < n. ∎

*Converse (44a).* The endpoint equality forces exactly this progression; 44a scanned all odd m < 2²¹ for six families and found only the progression members.

*Example (§5 of the note).* e = 8, b = 2, σ = 0, a = 16: n = 20,241,207 + 1,549,681,956v and m = 14,024,703 + 2³⁰v reach 30,361,811 + 2,324,522,934v, with words (1) and (1¹⁶, 8, 2, 3). (My check: 500 values of v including 10³⁰ + 7.) The added claim that every source of the progression was a root of the previous reduction was checked only by re-running the workbench's own checker.

**Theorem 44.5 (finite search; statement).** For odd n > 1 let k(n) = ⌊log₂(n − 1)⌋ − 1. Any template of Theorem 44.4 with larger member n has e ≤ k(n) and b = ν₃(n) − ν₃(e − 1), and its admitted smaller members are m_{a′} = 2^{a′}(J(n/3^b) + h_e)/3^{a′} − 1 for a ≤ a′ ≤ A_max = ν₃(J(n/3^b) + h_e), a chain with T(m_{a′+1}) = m_{a′}; so whether n is the larger member of such a pair is decided by a finite search at n. The proof uses m_{a′} + 1 = 2^{a′}W ≥ 2^{a′+1} and m_{a′} + 1 ≤ n − 1. 44a compared the search with an unrestricted backward search on all odd n < 400,000 and on 3,144 large sources: identical. Only 367 of the 199,999 odd n < 400,000 admit a template, all with e ≤ 4.

*Scope.* These are exact families of orbit mergers and a proved finite test. The note itself says the search does not show that some template applies to every retained source; coverage is sparse (templates need 3 | n and n ≡ 3 (mod 4)); no convergence statement follows.

## 3. Descent and a model contraction (Ch. 2, `stopped_affine_transport_20260914`)

For a word p let F_j(x) = (3^jx + C_j)/2^{A_j} be the affine map of its first j odd steps (total exponent A_j, C_j ≥ 0).

**Proposition 44.6.** If F_j(3) ≥ 3 for j < m and F_m(3) < 3, then every odd n ≥ 3 whose exponent word begins with p satisfies T^m(n) < n.

*Proof.* Write D = 2^{A_m} − 3^m and C = C_m. F_m(3) < 3 means 3^{m+1} + C < 3·2^{A_m}, so C < 3D, and in particular D > 0. Then T^m(n) = F_m(n) < n ⟺ C < Dn, and Dn ≥ 3D > C. ∎

(44a checked all 1,601 reference-3 leaves with A ≤ 16 and 9,605 actual starts.)

**Proposition 44.7.** For x ≥ 2, (√((x − 2)/2) + √((3x − 1)/2))/2 ≤ (√15/4)√(x − 1), with equality exactly at x = 7.

*Proof.* With u = (x − 2)/2 and v = (3x − 1)/2, Cauchy–Schwarz with weights ½ and 1 gives √u + √v = √(2u)·√(½) + √v·1 ≤ √(2u + v)·√(3/2), and 2u + v = (5/2)(x − 1). So the left side is at most ½√(3/2)√(5/2)√(x − 1) = (√15/4)√(x − 1). Equality needs 2u/(½) = v, that is 4u = v, that is x = 7. ∎

*Scope.* In the fair-coin reference model, where x moves to x/2 or (3x + 1)/2 with probability ½ each, this says E√(X_{next} − 1) ≤ (√15/4)√(x − 1). It is a statement about the model, not about individual orbits; the note says so. The tail bounds built on it ((7.9)–(7.16) of the note) were checked by 44a.

## 4. Cycles

A *nontrivial cycle* is a cycle of T on X other than {1}.

**Proposition 44.8 (Ch. 3).** No nontrivial positive cycle has at most one exponent-1 step.

*Proof.* Let n be the least element of the cycle, n > 1. If a step from x has exponent ≥ 2, then T(x) ≤ (3x + 1)/4 < x.
- If no step has exponent 1, every step decreases, which is impossible in a cycle.
- If exactly one step has exponent 1, it must be the step from n (otherwise T(n) < n). Then x₁ = (3n + 1)/2, and every later step decreases. A later step with exponent ≥ 3 would give a value at most (3x₁ + 1)/8 = (9n + 5)/16 < n, contradicting minimality. So the word is (1, 2, …, 2) with m − 1 twos, and x_{j+1} − 1 = (3/4)(x_j − 1) along the twos. Closing the cycle gives n − 1 = (3/4)^{m−1}(3n − 1)/2, that is n·D = 2·4^{m−1} − 3^{m−1} with D = 2·4^{m−1} − 3^m, and then n − 1 = 2·3^{m−1}/D. D is odd and prime to 3, so D | 2·3^{m−1} forces D = ±1. But D = −1 for m = 1, 2 (giving the negative cycles n = −1 and n = −5) and D ≥ 5 for m ≥ 3 (D increases: D_{m+1} = 4D_m + 3^m). So no positive cycle arises. ∎

(My check: for the word (1, 2^{m−1}) with m < 200 the only integer values are n = −1 and n = −5.) This is weaker than the published cycle results and the note says it does not supersede them; for the rational-cycle criterion "positive integer cycle ⟺ D > 0 and D | C" of the same chapter, the chapter cites Lagarias (Acta Arith. 56 (1990) 33–53) and, for operator formulations, Mori (arXiv:2411.08084), and claims no priority.

**Theorem 44.9 (Ch. 6, Theorem 9).** Every nontrivial positive cycle has more than 678 exponent-1 steps in its primitive odd-return word.

*Proof.* Every odd n ≤ 330,749 reaches 1 (the workbench's Theorem 8, from its own database; recomputed here: every odd n in this range falls below itself under T, so all reach 1 by induction). Let the cycle have m odd steps, k of them with exponent 1, total exponent A, and least element s. Since no element of a nontrivial cycle reaches 1, s ≥ 330,751. Multiplying T(x_i)/x_i = (3 + 1/x_i)/2^{a_i} around the cycle gives 2^A = ∏(3 + 1/x_i), so 3^m < 2^A ≤ (3 + 1/s)^m, and A ≥ 2m − k gives (4s)^m ≤ 2^k(3s + 1)^m. The least m for which some power of 2 lies in (3^m, (3 + 1/s)^m] is m = 1636, and (4s/(3s + 1))^m increases with m; at m = 1636 the inequality (4s)^m ≤ 2^k(3s + 1)^m needs k ≥ 679. ∎

(My check: the hypothesis in 0.2 s; exact integer arithmetic gives m* = 1636 and k ≥ 679; 44a verified the note's inequalities (C36) and (C37).)

*Scope.* The workbench labels this an internal bound, not a claim to exceed published cycle bounds, and the label is accurate. The count k (exponent-1 positions) differs from the number of local minima used by Simons–de Weger (Acta Arith. 117 (2005) 51–70) and Hercher (arXiv:2201.00406: no m-cycles with m ≤ 91). The same argument run with a larger verification range s would give a stronger bound of the same kind; Barina (J. Supercomputing 81 (2025), article 810) reports verification of convergence for all n below 2⁷¹.

## 5. Restatements

**Proposition 44.10 (Ch. 9; statement).** Let K be the orbit-graph complex of T and K_ε its first-jet thickening. Then B := ker(H¹(K_ε) → H¹(K)) ≅ ⊕_{nontrivial cycles C} ℤ/m_C ⊕ ⊕_{components without a cycle} ℤ, where m_C is the length of C, and every positive integer reaches 1 if and only if B = 0.

*Why (44a §2.6, re-derived there).* In the functional graph, ker d is spanned by the directed cycles; the map P sends a cycle to the sum of its vertices, which is m_C times the component class; the loop at 1 contributes ℤ/1 = 0. A finite certificate (u = −E₁, v = the edges of a path to 1) shows that each ξ_n vanishes exactly when n has an explicit path to 1.

*Scope.* This is an exact algebraic restatement of the conjecture, and the workbench says that B = 0 is not established. The same holds for the cycle-relative cohomology of Ch. 3 (coker B_p ≅ ℤ/D with [1] ↦ [C]; Collatz ⟺ H₀ = 0), whose formal inverse (I − tP)⁻¹ the chapter shows is not a finite integral chain on cycles or divergent rays: that identifies an input a global proof would need, not an obstruction to the conjecture.

## 6. The Tao-clock preprint (`preprints/tao_clock_audit/`)

Fix a base b, α = 1001/1000 and t_j = b^{α^j}. Let μ_s be the logarithmically weighted law on the odd integers of [s, s^α], and K_x the push-forward by first entry into [1, x] (with a failure state †). The exponent c > 0 and the constant B′ below are those supplied by Tao's Proposition 1.11 for the error between adjacent scales.

**Theorem 44.11 (statement; conditional on Tao's Proposition 1.11).**
- For every x, λ_{x,j} = K_xμ_{t_{j+1}} converges in ℓ¹ to a law λ_x^∞, with ‖λ_{x,j} − λ_x^∞‖ ≤ L_c(log t_j)^{−c} for x ≤ t_j, where L_c = B′/(1 − α^{−c}).
- The limits are coherent: K_xλ_y^∞ = λ_x^∞ for x ≤ y.
- For thresholds x₁ ≤ … ≤ x_r the joint first-entry law converges with the same error, independent of r.

*Proof steps (44a §3, no gap found).* Nested first passage gives p_x∘p_y = p_x for x ≤ y; push-forward is an ℓ¹ contraction; Tao's Proposition 1.11 (Tao, Forum Math. Pi 10 (2022), e12) gives the error between adjacent scales; the errors sum geometrically, Σ_{i≥j}(α^i log b)^{−c} = (log t_j)^{−c}/(1 − α^{−c}); completeness of ℓ¹ gives the limit and continuity of K_x gives coherence; the joint law is the push-forward under a bijection onto compatible tuples whose inverse is the last projection, hence an ℓ¹ isometry.

*Scope.* The preprint reproduces Tao's orbit-minimum theorems with attribution and says it proves no stronger orbit-minimum bound; both statements are accurate. Its stated repairs to Tao's §§5–6 were not audited. The clock identity Σ_{n≤X, C_min(n)>K} 1/n = Σ_a 2^{−a}Σ_{m≤X/2^a odd, S_min(m)>K} 1/m holds trivially (both sides 0) for 3x + 1 on every verified range; 44a tested the same mechanism non-vacuously on the 3x − 1 map, where both sides agree exactly (6.0633 at X = 50,000, K = 4).

## 7. The Hurwitz zero-cluster encoding (`split_zero_history_20260913/note.tex`)

The Collatz workbench uses the Hurwitz zeta function in three places: this note; Ch. 1 §5, which applies the same reconstruction to the history law with an extra boundary term (Z_p(s, t) = p_∂ζ(s, 1) + Σ_wp_wζ(s, 1 + tr_w)); and Ch. 2 §10, which uses Hurwitz values at nonpositive integers through the Hurwitz–Bernoulli identity (DLMF 25.11.14). This note is the one that treats the motion of a zero under ζ(s, 1 + t) in full, and it is audited here.

*Setting.* For fixed (m, A), let W_{m,A} be the set of odd-return exponent words with m odd steps and total exponent A, K = |W_{m,A}|, and r_w the residue of the words, which are exact and pairwise distinct modulo 2^{A+1} (Lemma 3.1 of the note; 44a checked all 105 packets with A ≤ 14). For a probability vector λ on W_{m,A} put Z_λ(s, t) = Σ_w λ_w ζ(s, 1 + tr_w), for |t|(2^{A+1} − 1) < 1.

**Theorem 44.12.** (The reconstruction is the zeta programme's, `historical_hurwitz_jets.tex`, equations H10–H13, at commit 16fc4dbb817b of the zeta repository; the Collatz note cites it and re-proves the part it uses.) Let ρ be a nontrivial zero of ζ of multiplicity r. The t-jet of order J of the monic polynomial whose roots are the r zeros of Z_λ(·, t) near ρ determines the moments M_i = Σ_w λ_w r_w^i for i ≤ J, and conversely. Hence the jet of order K − 1 determines λ, and the jet of order K − 2 does not determine it in general.

*Proof (for a simple zero; the multiple case uses the same triangularity for the cluster polynomial).* By the Taylor expansion of the Hurwitz zeta function in its second argument (DLMF 25.11.10; the zeta reader's Theorem "the first Hurwitz jet", part (a)), ζ(s, 1 + u) = Σ_j b_j(s)u^j with b_j(s) = (−1)^j(s)_jζ(s + j)/j!, so Z_λ(s, t) = Σ_j b_j(s)M_jt^j with M₀ = 1. For j ≥ 1, b_j(ρ) ≠ 0: (ρ)_j ≠ 0 since ρ is not a nonpositive integer, and ζ(ρ + j) ≠ 0 since Re(ρ + j) ≥ 1. Writing the zero as ρ(t) = ρ + c₁t + c₂t² + …, the coefficient of t^J in Z_λ(ρ(t), t) = 0 is ζ′(ρ)c_J + b_J(ρ)M_J + (terms in c₁, …, c_{J−1} and M₁, …, M_{J−1}). So (c₁, …, c_J) and (M₁, …, M_J) determine each other by a triangular polynomial change of variables. The residues r_w are K distinct nodes, so M₀, …, M_{K−1} determine λ by Vandermonde (Lagrange) inversion. For order K − 2, take h_w = 1/∏_{v≠w}(r_w − r_v); then Σ_w h_w r_w^i = 0 for i ≤ K − 2 and = 1 for i = K − 1, so λ^± = 1/K ± εh have the same moments up to K − 2. ∎

*Checks.* 44a solved for the zero trajectory of Z_λ near ρ₁ = ½ + 14.1347…i numerically (mpmath, 40 digits, |t| ≤ 2·10⁻⁶) and recovered M₁ = 18.4, M₂ = 433 and λ_{(2,2)} = 0.2 for the weights (0.5, 0.2, 0.3) at (m, A) = (2, 4), as the note's formulas predict.

*Scope.* This is an exact, invertible encoding of a finite probability vector on words into the motion of a zeta zero. The Hurwitz family is built from the weights, any nontrivial zero works, and no information about Collatz orbits enters beyond the residues r_w. It bears neither on RH nor on Collatz dynamics, and the note says so. The same note gives three information-loss witnesses: specialisation q → 3 of the parity-word lift is not injective on the constant terms (two words of length 5 with X(q) = 1/2 + q/32 and 1/8 + q/16 + q²/32, which differ by (q − 3)(q + 4)/32 and agree at q = 3), the eigenvalues of the affine matrix forget bit order, and (K − 2)-jets do not separate weights.

## 8. Negative results, with exact scope

- **Full-history obstruction** (Theorem 44.2(c)): above (½ + δ)log₂N the whole first-m word law is far from the geometric model. It does not bound any coarser observable and says nothing about individual orbits.
- **Encoding losses** (§7): three explicit witnesses. They do not show that no faithful spectral encoding exists; the (K − 1)-jet encoding is faithful.
- **Ch. 3 formal inverses**: (I − tP)⁻¹ is not a finite integral chain on cycles or divergent rays; the signed primitive of the unit cochain is unbounded below on an acyclic component. These name inputs a global proof would need; they are not obstructions to the conjecture.
- **Ch. 20 coverage**: the finite template search does not show that some template applies at every retained source.
- **Quarantine**: a process decision (owner's directive USR-0004), not a refutation; the quarantined tree contains a registered conjecture (record-tail genericity) and a rejected Bost–Connes–Marcolli construction.
- **Source ledger**: the workbench's literature ledger records counterexamples to printed statements and corrections (CLM-COL-000006, 021, 025, 034, 038, 041, 042, 149, 157, 159, 162). These concern sources and earlier drafts, not Collatz orbits, and were not audited.

## 9. Overlaps (detailed in `47_`)

- zeta ↔ Collatz: §7 uses ζ(s, 1 + tr_w); the dependency is on the zeta workbench's historical Hurwitz-jet file (eqs. H10–H13), re-proved locally.
- ES ↔ Collatz: the identity 3(4n + 1) + 1 = 4(3n + 1) of step 4 of Theorem 44.4 is ES's R05 (θT = 4θ for T(n) = 4n + 1, θ(n) = 3n + 1). Same classical identity, no recorded dependency.
- Collatz ↔ ES ↔ zeta: the support-idempotent homogenisation (x, h) ↦ (ax + bh, h). The split-zero note cites it as a local technical note of April 2026, *Support-Idempotent Homogenization for a Split-Zero Collatz F-Series Frame*, the title of the Clankers' Zenodo record 19900461, which the zeta foundation cites; ES proves the diagram (X4).
- zeta → Collatz: the Split-Zero support modules and killed-representative quotient. Ch. 7 takes the zeta workbench's `formal/splitzero/DERIVED_MATHEMATICS.md` §§1–4 and instantiates it on the Collatz operator; Chs. 8, 9 and 15 build on it; Ch. 6 states that it builds no map from the whole zeta theta quotient (44a §5). Located.
- Collatz → YM: the fixture (q − 3)(q + 4)/32 of §7, used by YM's research control as a regression test only.

## 10. Not checked

Chapters 4, 5, 7, 8, 10–19 beyond headings (except Theorem 9 of Ch. 6), and the proof of Ch. 9 itself (only its overview statement was re-derived); Ch. 13's use of Matveev's bound; the 11,610-step ledgers; the predecessor-root claim of the e = 8 progression (only the workbench checker was re-run); the R₀ budget of Ch. 19; Tao's Proposition 1.11 and the preprint's repairs; the Siegel edition, the literature reader, the research companion (including the registered conjecture CLM-COL-000173) and the Lean file (not built); novelty.

## 11. Checks

- `checks/workbenches/audit44_collatz/` (first pass): seven independent scripts and the outputs of the workbench's own checkers as run by 44a; the six independent scripts other than the Tao-clock one were re-run on 26 September with identical results.
- `checks/workbenches/workbench_reader_claims_checks.py`, section CZ (mine): Lemma 44.3 for e ≤ 3000; the §2 example for 500 values of v; Theorem 44.4 implemented from its definitions (600 pairs, e ≤ 20, b ≤ 6, both σ); the one-step cycle values; the hypothesis of Theorem 44.9 (every odd n ≤ 330,749 falls below itself); m* = 1636 and k ≥ 679; Proposition 44.7; the cylinder classes.

## 12. Revision after the twentieth referee pass

A referee (a Claude instance that did not write this note) re-derived Lemma 44.3, Theorem 44.4, Propositions 44.6–44.8 and Theorems 44.9 and 44.12 and found no error; it re-ran Theorem 44.4 on 1,200 further parameter pairs. Its findings on this note, each verified against the source before being applied:
- **Major.** (1) The status "audited" for Proposition 44.10 was not supported: only the overview's statement of Ch. 9 was re-derived. Relabelled. (2) §7 called the split-zero note the one place where the workbench uses ζ(s, 1 + t); Ch. 1 §5 uses the same reconstruction and Ch. 2 §10 uses Hurwitz special values. Corrected.
- **Minor, applied.** The credit for the rational-cycle criterion (Lagarias; Mori); Theorem 44.9 made unconditional by recomputing its hypothesis; the source of the homogenisation on the Collatz side; the missing Split-Zero support-module overlap; the zeta programme credited for the reconstruction in Theorem 44.12; a paraphrase no longer shown as a quotation; the notation of §3; a′ defined; c and B′ explained; the re-run statements made exact; a credit line.
