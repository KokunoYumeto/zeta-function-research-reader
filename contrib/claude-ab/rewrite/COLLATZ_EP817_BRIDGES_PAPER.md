# The Collatz and Erdős Problem 817 workbenches, and the bridges between the author's workbenches: an audited record

*Claude (Anthropic, model `claude-opus-5-5`), 27 September 2026. Published at the author's request ahead of the author's review; the author may revise or withdraw it. This record replaces the Collatz, Problem 817 and intersections sections of the reader of four workbenches and notes 44_, 45_ and 47_, which were withdrawn on 27 September 2026.*

## Abstract

The author's research programme includes a Collatz workbench, a workbench on Erdős Problem 817, and workbenches on the Erdős–Straus equation, Yang–Mills theory, Navier–Stokes, the S⁶ construction and the Riemann zeta function, with many explicit maps between them. For the Collatz problem we prove a sharp threshold for the full history law of consecutive starts (the word law of N starts is close to the geometric model below (1/2)log₂N halving counts and far from it above), explicit infinite families of merging pairs, a descent criterion that is necessary and sufficient, a contraction in the fair-coin model, and cycle bounds: every nontrivial positive cycle has at least 1636 odd steps from the workbench's own verification range, at least 190,537 from a verification to 2³³ made for this record, and at least 72,057,431,991 from Barina's published range by Eliahou's method. We also state an exact, invertible encoding of probability vectors on exponent words into the motion of a zero of the Riemann zeta function under the Hurwitz flow. For Problem 817 we give the proof, due to an anonymous contributor and reconstructed by the Clankers, that the least size g₄(n) of a set whose subset sums avoid 4-term progressions satisfies lim g₄(n)^{1/n} = 19^{1/3}, together with a variance refinement, a lifting principle, the characterization of every rate Λ_k as an infimum over modular certificates, the strict decrease Λ₃ = 3 > Λ₄ = 19^{1/3} > 97^{1/6} ≥ Λ₅, certificates for k = 5, 6, and the exact values g₄(1), …, g₄(6) = 1, 3, 5, 14, 40, 79. Finally we describe the bridges between the workbenches as typed maps, with what each carries and what it suggests.

## 0. Introduction

### 0.1 Why this record

The workbenches were developed with AI systems over 2026, each with its own notes, formal checks and continuations, and they are connected by explicit maps: the same period system appears in the S⁶, Erdős–Straus and Yang–Mills workbenches, the Hurwitz flow of the zeta programme appears in the Collatz workbench, and identities recur across several of them. This record states what the Collatz and Problem 817 workbenches prove, with proofs, and describes the bridges between all the workbenches, so that a reader can see both the results and the structure that connects them.

### 0.2 Main results

**Collatz** (§1).
- **Theorem 1.2** (*proved here*). The total variation between the empirical law of the first m exponents over N consecutive odd starts and the geometric model has an explicit two-sided bound for every m; it tends to Φ(2c) at m = L/2 + c√L (L = log₂N), to 0 at a polynomial rate below (1/2 − δ)L, and to 1 above (1/2 + δ)L, uniformly in the offset.
- **Theorem 1.4.** Explicit arithmetic progressions of pairs m < n whose trajectories meet, with prescribed exponent words.
- **Proposition 1.5** (*generalized here*). A cylinder of exponent words descends if and only if its least member does.
- **Theorem 1.8 and Corollary 1.9.** Every nontrivial positive cycle has at least 1636 odd steps and more than 678 steps with exponent 1 from the workbench's verification range; at least 190,537 odd steps from a verification to 2³³ made here; and at least 72,057,431,991 odd steps from Barina's published range.
- **Theorem 1.10.** An exact encoding of weights on exponent words into the zero motion of the Hurwitz flow of ζ.

**Erdős Problem 817** (§2).
- **Theorem 2.1.** (19^{n/3} − 1)/(2n) ≤ g₄(n) ≤ 8·19^{⌈n/3⌉−1}, so lim g₄(n)^{1/n} = 19^{1/3}.
- **Proposition 2.5 and Theorem 2.7** (*generalized here*). A lifting principle, and the rates Λ_k as infima over modular certificates, with Λ₃ = 3 > Λ₄ = 19^{1/3} > 97^{1/6} ≥ Λ₅.
- **Theorem 2.6.** A variance refinement of the lower bound.
- **Proposition 2.10** (*computed for this audit*). g₄(1), …, g₄(6) = 1, 3, 5, 14, 40, 79 and 176 ≤ g₄(7) ≤ 246.

**Bridges** (§4). Twenty-eight typed edges between the workbenches, eight of them substantive; they are stated with what crosses each and what it suggests.

### 0.3 What the results mean

For the Collatz problem, the history threshold makes precise how far the classical cylinder structure of Terras and Everett reaches: below half the logarithm of the sample size the full word law of consecutive starts is geometric, above it the word law is far from geometric, and the transition is Gaussian. The cycle bounds show how the verified range of the conjecture turns into lower bounds on the length of any nontrivial cycle through Eliahou's argument, and they locate the workbench's own bound within the published ones. The Hurwitz encoding shows that the zero dynamics of the Hurwitz flow can store a probability vector exactly, which is a new use of that flow.

For Problem 817, the k = 4 case of the exponential rate is settled, the general rates reduce to a certificate problem, and the first steps of the sequence Λ_k are strict. The bridges show how much of the programme is shared structure: several constructions of one workbench are theorems or tools in another.

### 0.4 How this record was made

This is an audit, carried out by an AI system, of research that was itself carried out with AI systems. The workbenches credit the literature they build on (Terras, Everett and Tao for the cylinder mechanism; Eliahou for the cycle argument; Erdős and Sárközy, Korsky and Costa for Problem 817), and the Problem 817 workbench records that its k = 4 proof is due to a contributor on the subreddit r/LLMmathematics whose account was later deleted, reconstructed, checked and partly formalized in Lean by the Clankers, with the finite upper bound formalized by sneed-and-feed. The workbench makes no priority claim for that theorem.

The audit read the proofs, re-derived them, recomputed every finite statement with independent programs, and added the results marked *proved here*, *generalized here* or *computed for this audit*. Statements carry one of four statuses, as in the companion papers: *verified* (proved here or re-computed by a program listed in §6), *not verified here*, *my assessment* (a view with its reasons, in the first person), and *proved negative* (with the counterexample or derivation in the text).

### 0.5 Organization

Part A contains the Collatz results (§1) and the Problem 817 results (§2). Part B (§3) contains the proved limits of specific methods. Part C (§4) describes the bridges between the workbenches. §5 lists questions and §6 the verification.

---

# Part A. Verified results

## 1. The Collatz workbench

*Notation.* X is the set of positive odd integers and T(n) = (3n + 1)/2^{ν₂(3n+1)} on X. The exponent word of n of length m is (a₁, …, a_m) with a_i = ν₂(3x_{i−1} + 1), x₀ = n, x_i = T(x_{i−1}); A = a₁ + … + a_m.

### 1.1 History laws

**Proposition 1.1 (cylinders).** For every exponent word w of length m and sum A there is a residue h_w modulo 2^A such that an odd n = 2k + 1 has exponent word w exactly when k ≡ h_w (mod 2^A). Among the N consecutive odd starts 2k + 1, b ≤ k ≤ b + N − 1, the number with word w is ⌊N/2^A⌋ or ⌈N/2^A⌉, so the empirical frequency P(w) satisfies |P(w) − 2^{−A}| < 1/N.

This is classical (Terras [Te], Everett [Ev]); the workbench credits the mechanism to Tao's Proposition 1.9 [Ta] and claims no priority.

**Theorem 1.2 (the full-history threshold; proved here).** Let P be the empirical law of the first m exponents over the N starts of Proposition 1.1, G_m(w) = 2^{−A(w)} the model of independent exponents with Pr(a = j) = 2^{−j}, L = log₂N, Δ = TV(P, G_m), and Φ the standard normal distribution function.
1. For every H ≥ 0, max{0, Q_m(H) − N2^{−H−1}} ≤ Δ ≤ min{1, Q_m(H) + C(H, m)/N}, where Q_m(H) = Pr(Bin(H, 1/2) ≤ m − 1) and C(H, m) is the binomial coefficient.
2. If m = ⌊L/2 + c√L⌋, then sup_b |Δ − Φ(2c)| → 0 as N → ∞.
3. If 0 < δ < 1/2 and 1 ≤ m ≤ (1/2 − δ)L, then Δ ≤ N^{−δ} + N^{−δ²/(2 ln 2)}. If m ≥ (1/2 + δ)L and δL > 1, then with H = ⌈(1 + δ)L⌉, 1 − Δ ≤ (1/2)N^{−δ} + exp(−2(δL/2 − 1/2)²/H).

All statements are uniform in b.

*Proof.* Under G_m the sum A is the waiting time for the m-th success in fair coin flips, so G_m(A > H) = Q_m(H), and the words with A ≤ H number C(H, m). *Upper bound:* Δ = 1 − Σ_w min(P(w), G(w)), and by Proposition 1.1 the words with A ≤ H contribute at least 1 − Q_m(H) − C(H, m)/N. *Lower bound:* P is carried by at most N words, each word with A > H has G-mass at most 2^{−H−1}, so Σ_{A>H} min(P, G) ≤ N2^{−H−1}, while Σ_{A≤H} min(P, G) ≤ 1 − Q_m(H). (2) Take H₊ = L + L^{1/4} in the lower bound and H₋ = L − L^{1/4} in the upper bound; the error terms tend to 0, and by the central limit theorem, uniform with error O(H^{−1/2}), Q_m(H_±) → Φ(2c). (3) Hoeffding's inequality for Bin(H, 1/2) in (1), with H = ⌊(1 − δ)L⌋ in the first case and H = ⌈(1 + δ)L⌉ in the second. ∎

The workbench's history-law note states the uniformity in b and gives (3) as explicit estimates. Checks: 2,952 sandwich checks; the exact Δ for N = 2¹⁰, 2¹², 2¹⁴ at three offsets against (1) for every 0 ≤ H ≤ 2L + 2 and against (3); at N = 2²⁰ the values 0.004, 0.044, 0.342, 0.668, 0.895 for c = −1, −1/2, 0, 1/2, 1 against Φ(2c) = 0.023, 0.159, 0.5, 0.841, 0.977, a slow convergence, as the note says. I have not searched the literature for this threshold.

### 1.2 Merging families

**Lemma 1.3.** For even e ≥ 2, h_e = (2^e + 2)/3 is an integer with h_e ≡ 2 (mod 4) and ν₃(h_e) = ν₃(e − 1).

*Proof.* 2^e ≡ 1 (mod 3) gives integrality and 2^e + 2 ≡ 2 (mod 4). With k = e − 1 odd, 2^e + 2 = 2(2^k + 1), and the lifting-the-exponent lemma gives ν₃(2^k + 1) = 1 + ν₃(k). ∎

**Theorem 1.4 (explicit merging families; the workbench's all-even join extension, Theorem 2).** Fix an even e ≥ 2, b ≥ 1 and σ ∈ {0, 1}. Let a be the least a ≥ 1 with 2^{a+e+2b−σ} < 3^{a+b}, and put J = 2^{e+2b−σ}, Q = 3^{a+b}, K = 2^aJ, and (d, r) = (4, 3) if σ = 0, (32, 27) if σ = 1. Let n₀ ∈ (0, dQ) solve n₀ ≡ r (mod d) and Jn₀ + h_e3^b ≡ 0 (mod Q), and m₀ = (Kn₀ + 2^ah_e3^b)/Q − 1. For every v ≥ 0, n = n₀ + dQv and m = m₀ + dKv are odd, 0 < m < n, ν₃(n) = b + ν₃(e − 1), the exponent words of n and m begin with (1) and (1^a, e, 2^{b−1}, 3) if σ = 0, and with (1, 2, 1) and (1^a, e, 2^{b−1}, 1, 1, 3) if σ = 1, and the trajectories meet at the same odd number.

*Proof.* *Range of a.* At a = b + 2e − 2σ, K/Q = (8/9)^{b+e−σ} < 1, and K < Q forces a ≥ e > ν₃(e − 1). *The 3-adic part.* J is a unit mod 3, so ν₃(n) = b + ν₃(e − 1); with z = n/3^b and W = (Jz + h_e)/3^a one has ν₂(W) = 1 and m = 2^aW − 1. *The right path.* The first a steps from m have exponent 1 and end at x_a = Jz + h_e − 1, odd; by 3h_e − 2 = 2^e the next exponent is exactly e, the next b − 1 have exponent 2, and the path ends at 4n + 1 (σ = 0) or 2n + 1 (σ = 1). *The meeting point.* If σ = 0, 3(4n + 1) + 1 = 4(3n + 1) gives the same value as T(n) = (3n + 1)/2. If σ = 1, n ≡ 27 (mod 32) gives n → (3n + 1)/2 → (9n + 5)/8 → (27n + 23)/16 with exponents 1, 2, 1, and 2n + 1 → 3n + 2 → (9n + 7)/2 → (27n + 23)/16 with exponents 1, 1, 3. *Height.* m = (K/Q)n + h_e(2/3)^a − 1 with K < Q and h_e(2/3)^a < 1. ∎

For example (e = 8, b = 2, σ = 0, a = 16), n = 20,241,207 + 1,549,681,956v and m = 14,024,703 + 2³⁰v reach 30,361,811 + 2,324,522,934v for every v ≥ 0. The workbench also proves its converse (the endpoint equality forces this progression) and a finite search that decides whether an odd n > 1 is the larger member of such a pair; only 367 of the odd n < 400,000 admit a template.

### 1.3 Descent, and a contraction in the fair-coin model

**Proposition 1.5 (generalized here).** Let F_m(x) = (3^mx + C_m)/2^{A_m} be the affine map of the first m odd steps of an exponent word, and n₀ the least odd n ≥ 3 whose word begins with it. Then every odd n ≥ 3 whose word begins with it satisfies T^m(n) < n if and only if F_m(n₀) < n₀; this holds in particular if F_m(3) < 3. More precisely, a member descends if and only if D = 2^{A_m} − 3^m > 0 and n > C_m/D.

*Proof.* F_m(x) − x = (C − Dx)/2^{A_m} with C = C_m > 0, and T^m(n) = F_m(n) for every member. ∎

The workbench's Chapter 2, Theorem 2.1, assumes F_j(3) ≥ 3 for j < m and F_m(3) < 3; the criterion needs only F_m(n₀) < n₀, which is also necessary. For example, the word (1, 1, 1, 1, 4) has F₅(3) = 235/64 > 3, but n₀ = 95 and every member descends.

**Proposition 1.6 (generalized here).** For x ≥ 2, (1/2)(√((x − 2)/2) + √((3x − 1)/2)) ≤ (√15/4)√(x − 1), with equality exactly at x = 7.

*Proof.* With u = (x − 2)/2 and v = (3x − 1)/2, Cauchy–Schwarz gives √u + √v ≤ √(2u + v)·√(3/2), and 2u + v = (5/2)(x − 1); equality needs 4u = v. ∎

In the fair-coin model, where x moves to x/2 or (3x + 1)/2 with probability 1/2 each, this says E√(X_next − 1) ≤ (√15/4)√(x − 1). Started at X₀ = 3 with the first step odd, the first time τ below 3 satisfies Pr(τ > h) ≤ (3/2)(31/32)^h, and the completed stopping word has tail t_H ≤ (31/20)(31/32)^H (the workbench's (7.9)–(7.16)). These are statements about the model, as the workbench says.

### 1.4 Cycles

**Proposition 1.7.** No nontrivial positive cycle of T has at most one step with exponent 1.

*Proof.* Let n > 1 be the least element. A step with exponent ≥ 2 from x > 1 decreases, so the step from n has exponent 1 and every later step decreases; an exponent ≥ 3 later would give a value below n. So the word is (1, 2, …, 2), and closing the cycle gives nD = 2·4^{m−1} − 3^{m−1} with D = 2·4^{m−1} − 3^m odd and prime to 3, so D = ±1; but D = −1 for m = 1, 2 (the negative cycles −1 and −5) and D_{m+1} = 4D_m + 3^m ≥ 5 for m ≥ 2. ∎

**Theorem 1.8.** Every nontrivial positive cycle of T has at least 1636 odd steps, at least 2593 halvings, and more than 678 steps with exponent 1.

*Proof.* The workbench verifies that every odd n ≤ 330,749 reaches 1 (recomputed here). Let the cycle have m odd steps, k of them with exponent 1, total exponent A and least element s ≥ 330,751. Multiplying T(x_i)/x_i = (3 + 1/x_i)/2^{a_i} around the cycle gives 2^A ∈ (3^m, (3 + 1/s)^m], and A ≥ 2m − k gives (4s)^m ≤ 2^k(3s + 1)^m. The least m for which a power of 2 lies in that interval is m = 1636 (exact integer arithmetic), so A > 1636 log₂3 = 2592.998…, and at m = 1636 the inequality needs k ≥ 679. ∎

This is Eliahou's argument [El]; the count k differs from the number of local minima used in the published bounds of Simons–de Weger [SdW] and Hercher [He]. Run with a larger verification range it gives more. A verification made for this record shows that every odd n with 3 ≤ n < 2³³ falls below itself (38 seconds on two cores, 128-bit arithmetic, largest value met 9.07·10¹⁸; repeated by two independently written programs), so every n < 2³³ reaches 1, and the same argument gives m ≥ 190,537, A ≥ 301,994 and k ≥ 79,080.

**Corollary 1.9 (from Barina's range).** Every n < 2.17·10²⁰ reaches 1: Barina verified every n < 2⁶⁸ (2020, published 2021 [Ba1]) and every n < 2⁷¹ [Ba2]. Hence every nontrivial positive cycle has at least 72,057,431,991 odd steps, at least 114,208,327,604 halvings, and at least 29,906,536,378 steps with exponent 1.

*Proof.* The least element s exceeds s_lo = 1/(2^{10439860591/6586818670} − 3) = 2.1689015534·10²⁰. So A/m ∈ (log₂3, log₂(3 + 1/s_lo)), an interval that excludes 10439860591/6586818670, and every fraction in (log₂3, 10439860591/6586818670) has denominator at least 72,057,431,991, the denominator of the next best upper approximation of log₂3. The bounds on A and k follow as in Theorem 1.8. ∎

The fraction 114208327604/72057431991 was found by the continued-fraction algorithm for the simplest fraction in an interval (80-digit arithmetic) and confirmed by a Stern–Brocot descent (120-digit arithmetic); the same computation returns Eliahou's published A = 17,087,915 at s = 2⁴⁰. The published bound is stronger: Hercher [He, Corollary 29] proves that if every n ≤ 3·2⁶⁹ reaches 1, every nontrivial cycle contains more than 1.375·10¹¹ odd numbers, and Barina's verification passed that range in 2023 [Ba2]. Hercher's proof is not verified here.

### 1.5 Restatements, and the Tao-clock deduction

The workbench states two exact restatements of the conjecture: the vanishing of ker(H¹(K_ε) → H¹(K)) for the orbit-graph complex K and its first-jet thickening, a group isomorphic to the sum of ℤ/m_C over the nontrivial cycles and of ℤ over the components without a cycle (Chapter 9; not verified here beyond its statement), and the vanishing of H₀ of a relative orbit-graph homology (Chapter 3; verified). Its Tao-clock preprint deduces from Tao's Proposition 1.11 [Ta] that the laws of the first entry of an orbit into [1, x], started from the logarithmic law on [t_{j+1}, t_{j+1}^α] with t_j = b^{α^j}, α = 1001/1000, converge in ℓ¹ as j → ∞ at the rate L_c(log t_j)^{−c}, coherently in x, with joint laws for several thresholds converging with the same error. The deduction (nested first passage, ℓ¹ contraction, a geometric sum of Tao's adjacent-scale errors, completeness) is verified; the preprint's repairs to Tao's §§5–6 are not verified here.

### 1.6 The Hurwitz zero-cluster encoding

Fix (m, A). The K odd-return words, the exponent words w = (a₁, …, a_m) with all a_i ≥ 1 and sum A, have pairwise distinct residues r_w modulo 2^{A+1}. For a probability vector λ on these words put Z_λ(s, t) = Σ_w λ_w ζ(s, 1 + tr_w) for |t|(2^{A+1} − 1) < 1.

**Theorem 1.10 (proved here for simple zeros; verified in general).** Let ρ be a nontrivial zero of ζ. The t-jet of order J of the zeros of Z_λ(·, t) near ρ (of their monic cluster polynomial if ρ is multiple) determines the moments M_i = Σ_w λ_w r_w^i, i ≤ J, and conversely. Hence the jet of order K − 1 determines λ, and for K ≥ 2 the jet of order K − 2 determines λ at no interior point of the simplex.

*Proof for a simple zero.* ζ(s, 1 + u) = Σ_j b_j(s)u^j with b_j(s) = (−1)^j(s)_jζ(s + j)/j! [DLMF, 25.11.10], so Z_λ = Σ_j b_j(s)M_jt^j with M₀ = 1, and b_j(ρ) ≠ 0 for j ≥ 1. Writing the zero as ρ(t) = ρ + c₁t + c₂t² + …, the coefficient of t^J in Z_λ(ρ(t), t) = 0 is ζ′(ρ)c_J + b_J(ρ)M_J plus a polynomial in the lower c_i and M_i, so the c's and M's determine each other triangularly. The K distinct nodes r_w make M₀, …, M_{K−1} determine λ (Vandermonde), and with h_w = 1/∏_{v≠w}(r_w − r_v), Σ_w h_w r_w^i = 0 for i ≤ K − 2, so λ + εh has the same moments to order K − 2. ∎

The encoding is an exact, invertible embedding of weights on residue classes into the motion of a zeta zero under the Hurwitz flow t ↦ ζ(s, 1 + t). It works at every nontrivial zero, so it is a storage device for the weights rather than a constraint on where the zeros lie; the note says so. The same note gives three witnesses of what coarser encodings lose: two parity words of length 5 whose affine constant terms 1/2 + q/32 and 1/8 + q/16 + q²/32 differ by (q − 3)(q + 4)/32 and agree at q = 3; the eigenvalues of the affine matrix forget bit order; and (K − 2)-jets do not separate weights.

## 2. The Erdős Problem 817 workbench

For a finite set A of distinct positive integers let H(A) = {Σ_{a∈A} ε_a a : ε_a ∈ {0, 1}} and S(A) = Σ_{a∈A} a. A is *k-admissible* if H(A) contains no k-term arithmetic progression with nonzero step, and g_k(n) is the least N such that some n-element A ⊆ {1, …, N} is k-admissible. Erdős Problem 817, a problem of Erdős and Sárközy, asks for estimates of g_k(n), in particular whether g₃(n) ≫ 3ⁿ; they proved g₃(n) ≫ 3ⁿ/n^{O(1)} [ES]. The workbench reports that Costa's preprint [Co] proves lim inf g₃(n)/3ⁿ = 0, a negative answer to that question; this is not verified here, and the workbench's own results concern k ≥ 4. Admissibility is hereditary, so g_k is strictly increasing.

### 2.1 The rate 19^{1/3} for four-term progressions

**Theorem 2.1.** For every n ≥ 1, (19^{n/3} − 1)/(2n) ≤ g₄(n) ≤ 8·19^{⌈n/3⌉−1}. Hence lim_n g₄(n)^{1/n} = 19^{1/3} ≈ 2.6684.

The workbench's paper is complete and correct as written, and the proof below follows it. The workbench reports the upper half as Lean-checked; the Lean files were read, not built. Let A = {a₁, …, a_n} be 4-admissible. A *relation* is c ∈ {−2, …, 2}ⁿ, c ≠ 0, with Σc_ia_i = 0.

**Lemma 2.2 (relation splitting).** If c is a relation, then with P_j = Σ_{c_i=j} a_i and N_j = Σ_{c_i=−j} a_i one has P₁ = N₁ and P₂ = N₂.

*Proof.* X₀ = P₁ + N₂, X₁ = P₁ + P₂, X₂ = N₁ + N₂, X₃ = N₁ + P₂ are subset sums. With d = P₂ − N₂, the relation gives N₁ − P₁ = 2d, and then X₁ − X₀ = X₂ − X₁ = X₃ − X₂ = d. Admissibility forces d = 0. ∎

**Lemma 2.3 (blocks).** Call a ±1-relation minimal if its support is inclusion-minimal. Two minimal relations have disjoint supports or are equal up to sign, and every relation is Σ_j t_jr^{(j)} with t_j ∈ {−2, …, 2}, where the blocks r^{(j)} are the minimal relations, with pairwise disjoint supports of size at least 3.

*Proof.* For minimal r, s, the ±2 layers of r ± s are r·1_{E±} with E_± = {i : r_i = ±s_i ≠ 0}; by Lemma 2.2 each is a relation or zero, and minimality gives the dichotomy. Every ±1-relation is a sum of blocks with disjoint supports, by induction on the support; for a relation c, the ±1 part and half the ±2 part are ±1-relations with disjoint supports (Lemma 2.2). ∎

**Lemma 2.4 (the ternary count).** Let T(A) = {Σx_ia_i : x ∈ {0, 1, 2}ⁿ}, let the blocks have sizes m₁, …, m_h, and let t = n − Σm_j. Then |T(A)| = 3^t ∏_j(3^{m_j} − 2^{m_j}).

*Proof.* Two vectors have the same value iff their difference is Σt_jr^{(j)}; on a block, reflecting x_i ↦ 2 − x_i where r_i = −1 turns the equivalence into translation by (1, …, 1), and each class has exactly one representative with minimum 0; these number 3^m − 2^m. ∎

*Proof of Theorem 2.1.* Lower bound: f_m = 3^m − 2^m has f₃ = 19 and f_{m+1} = 3f_m + 2^m > 3f_m, so f_m ≥ 19^{m/3} for m ≥ 3, and 3 ≥ 19^{1/3}; so |T(A)| ≥ 19^{n/3}, and T(A) ⊆ [0, 2S(A)] ⊆ [0, 2nN]. Upper bound: D = H({1, 7, 8}) = {0, 1, 7, 8, 9, 15, 16} contains no nonconstant 4-term progression modulo 19 (all 19·18 checked). For A_m = {19^jw : j < m, w ∈ {1, 7, 8}}, H(A_m) is the set of integers whose base-19 digits lie in D, without carries. If x + id (0 ≤ i ≤ 3) lie in H(A_m) with d = 19^re, 19 ∤ e, the r-th digits form a nonconstant progression in D modulo 19. So A_m is 4-admissible with 3m elements and maximum 8·19^{m−1}. ∎

**Proposition 2.5 (lifting; generalized here).** Let each W_j be {1, 7, 8} or {2, 3, 5}. For every 4-admissible B and q ≥ 0, {19^jw : j < q, w ∈ W_j} ∪ 19^q·B is 4-admissible. Hence g₄(n + 3q) ≤ 19^q g₄(n); g₄(n) ≤ c·19^{⌈n/3⌉−1} with c = 1, 3, 5 for n ≡ 1, 2, 0 (mod 3); g₄(3q) ≤ 79·19^{q−2} and g₄(3q + 1) ≤ 246·19^{q−2} for q ≥ 2, and g₄(3q + 2) ≤ 40·19^{q−1} for q ≥ 1, that is at most 0.219, 0.256 and 0.296 times 19^{n/3}; and for every certificate (q, B) of Theorem 2.7, g_k(m|B| + n) ≤ q^m g_k(n). The sets {1, 7, 8} and {2, 3, 5} are the only 3-element B with S(B) < 19 and H(B) free of nonconstant 4-term progressions modulo 19.

*Proof.* H of the lifted set is H(A) + 19^q·H(B) without carries. A progression with 19^q | d reduces to one in H(B); otherwise the r-th digits give a nonconstant progression modulo 19 in H(W_r), and H({2, 3, 5}) = 3·D mod 19. The last statement is a finite search. ∎

**Theorem 2.6 (the variance refinement).** Write n = 3q + r (0 ≤ r ≤ 2) and M_n = 19^q3^r. Every 4-admissible A has |T(A)| ≥ M_n and 19(|T(A)|² − 1) ≤ 192Σa_i². Hence g₄(n) ≥ ⌈√(19(M_n² − 1)/(192n))⌉, about c_r19^{n/3}/√n with c_r = 0.315, 0.354, 0.398, and g₄(n) ≥ ⌈(M_n + n(n − 1) − 1)/(2n)⌉.

*Proof.* f_m ≥ 19^{⌊m/3⌋}3^{m mod 3}, and since 3³ > 19 the least value of the product in Lemma 2.4 is M_n. The uniform law on T(A) is the law of a sum of independent components; a block with coefficients b_i, Σb_i = 0, has variance κ_mQ with κ_m = (8·3^m − 3·2^m)/(12(3^m − 2^m)) ≤ 16/19 for m ≥ 3, and a free coordinate has variance (2/3)a_i². So the variance is at most (16/19)Σa_i², while M distinct integers have uniform variance at least (M² − 1)/12. ∎

### 2.2 General k

**Theorem 2.7.** For every k ≥ 3, Λ_k = lim_n g_k(n)^{1/n} exists and equals inf q^{1/|B|} over the pairs (q, B) with S(B) < q and H(B) modulo q free of k-term progressions with nonzero step. Moreover Λ₃ = 3 > Λ₄ = 19^{1/3} > 97^{1/6} ≥ Λ₅ (proved here).

*Proof.* If A and B are k-admissible and R = 2S(A) + 1, then C = A ∪ R·B is k-admissible and 2S(C) + 1 = (2S(A) + 1)(2S(B) + 1), since a progression in H(C) = H(A) + R·H(B) has second differences Δ²α + RΔ²β = 0 with |Δ²α| < R. So F_k(n) = min(2S(A) + 1) is submultiplicative, and Fekete's lemma with 2g_k(n) + 1 ≤ F_k(n) ≤ 2ng_k(n) + 1 gives the limit. A certificate (q, B) gives k-admissible sets {q^jb} as in Theorem 2.1, and every k-admissible B gives the certificate (2S(B) + 1, B). For k = 3: the certificate (3, {1}) gives Λ₃ ≤ 3; conversely a 3-admissible set has no relation with coefficients in [−2, 2] (X₀, X₁, X₂ would be a 3-term progression), so the 3ⁿ ternary sums are distinct and 3ⁿ ≤ 2nN + 1. ∎

The workbench also proves Λ_k ≥ (k − 1)/(k − 2), the monotonicity Λ_{k+1} ≤ Λ_k, and that avoidance of k-term progressions by base-q numbers with digits from a finite set is decided by a finite carry graph.

**Theorem 2.8 (certificates for k = 5, 6).**
1. B* = {1, 4, 5, 17, 21, 22} has S(B*) = 70, |H(B*)| = 38, and H(B*) is free of nonzero-step 5-term progressions modulo 97 and of 6-term progressions modulo 93. Hence Λ₅ ≤ 97^{1/6} ≈ 2.1435 and Λ₆ ≤ 93^{1/6} ≈ 2.1285.
2. A♯ = {3, 4, 7, 34, 37, 41, 216, 250, 253, 257}, the ten pairwise distances of the marks 0, 4, 7, 41, 257, has S(A♯) = 1102 < 1651 = 13·127, |H(A♯)| = 291, and H(A♯) is free of nonzero-step 6-term progressions modulo 1651. Hence g₆(n) ≤ 257·1651^{⌈n/10⌉−1} and Λ₆ ≤ 1651^{1/10} ≈ 2.0979.

Each modular condition was recomputed twice. Korsky's preprint [Ko] proves, for fixed k ≥ 4, g_k(n) ≫_k ((k − 1)/(k − 2))ⁿn^{−log₂((k−1)/(k−2))} and upper rates min_p p^{2/(min{p,k}−1)} over primes p ≥ 3: 5^{2/3} ≈ 2.924 for k = 4, √5 ≈ 2.236 for k = 5 and 7^{2/5} ≈ 2.178 for k = 6. Theorem 2.1 determines the k = 4 rate between Korsky's 3/2 and 5^{2/3}, and Theorem 2.8 lowers the upper rates for k = 5 and 6.

**Proposition 2.9 (distance rulers; generalized here).** If A contains r pairwise disjoint subsets each summing to L, then H(A) contains 0, L, …, rL. In particular, for marks 0 = t₀ < … < t_{m−1} = L whose 2m − 3 distances L, t_i, L − t_i are pairwise distinct, the subset sums of any set containing these distances contain 0, L, …, (m − 1)L. For A♯ this gives 0, 257, 514, 771, 1028, so A♯ is 6-admissible and not 5-admissible.

### 2.3 Exact small values

**Proposition 2.10 (computed for this audit).** g₄(1), …, g₄(6) = 1, 3, 5, 14, 40, 79, and 176 ≤ g₄(7) ≤ 246.

The values for n ≤ 6 were computed by four independent exhaustive searches, which agree, including the numbers of optimal sets 1, 2, 2, 2, 7, 1. The unique optimal 6-set is {2, 29, 45, 74, 77, 79}: two blocks (29 + 45 = 74, 2 + 77 = 79), and |T| = 361 = M₆, the least value Theorem 2.6 allows. g₄(7) ≤ 246 by {1, 3, 39, 180, 219, 243, 246}; the lower bound 176 is conditional on the search program, which excluded maxima in [132, 175] by pruning from Lemma 2.4 and Theorem 2.6. I have not found these values in the sources read; OEIS could not be consulted.

### 2.4 The continuation notes

The workbench's 29 continuation notes are ordinary proofs with exact finite certificates. Beyond the results above: a finite-period approximation of the best lower-limit growth rate of q-ary images (verified in part; the radix-ten example has minima a₁ = 13, a_{3r} = 893^r, a_{3r+1} = 93²·893^{r−1}, a_{3r+2} = 93·893^r, verified for m ≤ 16 by an independently built automaton); a correction the workbench published (the independence test Y_P = P ∪ (L − P) with P ⊆ [0, Q] needs L > 3Q, not L > 2Q); and a recurrence control: if a_j > S_{j−1} + S_{j−r} for all j, the subset sums contain no (2^r + 1)-term progression, which for r = 2 covers the Pell numbers. The other continuation notes are not verified here.

---

# Part B. Proved limits of specific methods

## 3. What specific methods cannot do

**Collatz.**
- *The full-history threshold* (Theorem 1.2(3)): above (1/2 + δ)log₂N halving counts, the full word law of N consecutive starts is far from the geometric model. The statement concerns the full word law; coarser observables and individual orbits are outside it.
- *Coarser encodings* (§1.6): the (K − 2)-jets of the Hurwitz encoding do not separate weights, while the (K − 1)-jets do.
- *The formal inverse* (I − tP)⁻¹ of Chapter 3 is not a finite integral chain on cycles or divergent rays, and the signed primitive of the unit cochain is unbounded below on an acyclic component. These identify inputs that a global argument along those lines would need.
- *The finite template search* of Chapter 20 decides the template property at each n; it does not by itself show that a template applies at every retained source.

**Problem 817.**
1. The count of 19 classes per 3-block needs admissibility: {1, 2, 3} has |T| = 13 < 19.
2. Admissible classes are strictly nested: {1, 2} is 5-admissible but not 4-admissible.
3. Modular certificates are sufficient, not necessary, for all-length admissibility (B = {2, 7}, q = 11, k = 3); Theorem 2.7 is unaffected.
4. For B*, every base 71–96 fails at k = 5 and every base 71–92 at k = 6.
5. Every distinct-distance ruler with m marks has an m-term progression (Proposition 2.9), and the ruler (0, 1, 5, 22) has no 6-admissible extension by one further mark with distinct distances.
6. For A♯ no canonical schedule with radix in [1103, 1650] is admissible.
7. Image counts do not determine admissibility.

Each concerns the named block or construction; the unrestricted rates Λ_k for k ≥ 5 are open.

---

# Part C. Bridges between the workbenches

## 4. The bridges, what crosses them, and what they suggest

The workbenches were built as a connected programme, and many of their constructions cross from one workbench to another. This section states each crossing as a typed map: what it carries, what is established, and what it suggests. The types are P (a proved map or lemma used on both sides), I (the same identity or object on both sides), D (one side imports the other's theorem), R (a regression test), and A (an analogy or proposal).

### 4.1 The graph

The nodes are the zeta programme (zeta), Erdős–Straus (ES), Collatz (CZ), Erdős 817 (EP), Yang–Mills (YM), Navier–Stokes (NS), S⁶, and the Jacobian map F.

| # | Edge | What crosses | Type | Status |
|---|---|---|---|---|
| 1 | zeta → CZ | the Hurwitz zero-cluster reconstruction, re-proved in the part used (§1.6) | P | verified |
| 1a | zeta → CZ | the split-zero support modules and killed-representative quotient, on the Collatz operator | P/D | not verified here |
| 2 | NS → ES | the torus endomorphism J = [[3, 1], [1, 5]] of the NS manuscript, as an operator | P | verified |
| 3 | S⁶ → ES | the monodromies A₁, A₂, A_∞ of the (3,4,∞) period system | P | verified at every level (ES record, Theorem 10.1) |
| 4 | S⁶ → YM | the imaginary period block of the period matrix, through one positive number | P | verified |
| 5 | F → NS kinematics → YM | incompressible flows, the escaping curve, the material tensor, trial states | P | verified; conditional on fixed-box limits |
| 6 | F → zeta | an inverse-fibre chart, fibre heat, a material generator, endpoint jets | P | not verified here |
| 7 | ES ↔ zeta | a four-dimensional Keller map P with det DP = −2 and its conductor | P | det DP verified; the rest not verified here |
| 8 | zeta → YM | the Gram sandwich from a relative column error, δ ≤ 1 | P | verified |
| 9–10 | zeta → YM | an inverse-power observability pattern; a composed minimum-lift identity | P | verified in part |
| 11 | NS → YM | velocity ↦ reducible SU(2) connection, −2Σtr F_ij² = λ²|curl u|² | P; D | verified; conditional on the NS rates |
| 12 | NS → zeta | the NS field as arithmetic input (Mellin transports) | D; P | not verified here |
| 13 | S⁶, F → NS | fluid coordinates; S⁶ gauge-scalar equations → NS on 𝕋³ | P | not verified here |
| 14–15 | zeta ↔ ES | zeta results as dependencies of ES items; the ES reader as a source dependency | D | not verified here |
| 16 | EP → zeta | finite word sources in the supported quotient; a cocycle identity | P | one of ten notes verified |
| 17 | ES ↔ CZ | 3(4n + 1) + 1 = 4(3n + 1) | I | verified |
| 18 | CZ ↔ ES ↔ zeta | the homogenization (x, h) ↦ (ax + bh, h) | I | verified in part |
| 19 | CZ → YM | X_v − X_u = (q − 3)(q + 4)/32 | R | verified |
| 20 | ES ↔ zeta | the semiring G(R) = R ⊔ {τ} | I | verified |
| 21 | ES ↔ zeta | a finite Weyl basis of End ℂ[A] | I | verified in part |
| 22 | ES ↔ S⁶ | the Niemeier lattice with root system A₅⁴D₄, glue index 72 | I | verified on the ES side |
| 23–28 | various | shared vocabulary, routing proposals, packages | A, P/D | not verified here |

### 4.2 The substantive bridges

**zeta → Collatz: zero motion as storage (edge 1).** The map from probability vectors λ to the order-J jet of the zero cluster of Σ_w λ_w ζ(s, 1 + tr_w) near a nontrivial zero ρ factors as a moment map λ ↦ (M₁, …, M_J), depending only on the residues, followed by a triangular polynomial bijection whose diagonal coefficients are ζ′(ρ) and b_J(ρ) (Theorem 1.10). The zeta programme studies the same flow t ↦ ζ(s, 1 + t) at t = 0 through its jets; here the motion of one zero, taken at several shifts and averaged with weights, stores the weights exactly. The Collatz workbench is the only one besides the zeta programme that uses this flow. My assessment: the bridge shows that the Hurwitz flow is a faithful carrier of finite probability data, which suggests using zero dynamics as a coordinate system for other finite laws, and conversely using known laws to probe the dynamics of zeros.

**NS → ES: an operator from fluid dynamics in shell arithmetic (edge 2).** The torus endomorphism J of the NS manuscript (determinant 14, eigenvalues 4 ± √2) enters 21 Erdős–Straus statements. Their content is the identity {(u, v) ∈ G² : u³v = 1 = uv⁵} = {(u, u^{−3}) : u¹⁴ = 1} in a finite abelian group G (in the application the unit group modulo R_a), which gives exact aliasing on finite character groups, and the sharp constant inf_{k≠0}|v·k|‖k‖ = 1/√(4 + 2√2) for the eigen-directions v_r = (1, 1 − √2) and v_t = (√2 − 1, 1), approached along Pell vectors. The bridge carries the operator and its Diophantine approximation properties; the NS existence theorem is not used.

**S⁶ → ES and S⁶ → YM: two uses of one period system (edges 3, 4).** Erdős–Straus uses the integral monodromies of the (3,4,∞) period system to build covers whose sections are the solutions (ES record, §10); Yang–Mills uses the imaginary period block as a magnetic background, through one positive number D. Both use the displayed period matrices, and the S⁶ monodromy record determines the group that governs the first use.

**The name Fable: three objects (edges 5–7).** In the repositories the name refers to the three-dimensional Keller map F of the Jacobian counterexample, to the S⁶ construction in older files, and to the four-dimensional Keller map P of the Erdős–Straus crosswalk. F enters Yang–Mills through incompressible flows and trial states that track the free two-gluon threshold (YM record, §5); P has det DP = −2, and its fibres, monodromy and conductor are not verified here.

**zeta → YM: linear algebra shared across programmes (edges 8–10).** What crosses is the Gram sandwich (1 − δ)²Φ*Φ ⪯ Φ_J*Φ_J ⪯ (1 + δ)²Φ*Φ when ‖(Φ_J − Φ)x‖ ≤ δ‖Φx‖ and δ ≤ 1 (the zeta instance takes δ from a dilation factor, the Yang–Mills instance from a heat semigroup), an observability pattern, and Schur-complement identities. The transfers state that they assert no map between arithmetic zeta objects and gauge fields.

**NS → YM (edge 11).** A divergence-free velocity u becomes the reducible connection A_i = λu_iT with curvature density λ²|curl u|². The resulting curvature rates are derived, conditionally on four statements of OpenAI's manuscript, in the NS record (Theorem 3.1); the zero-quotient diagonal exists with coupling tending to 0.

**Erdős 817 → zeta (edge 16).** Ten interface notes restate 817's finite constructions in the zeta programme's supported-quotient vocabulary. The one verified is a correct restatement: free vector spaces on coefficient words, the evaluation quotient, the cut map e_{(x,y)} ↦ e_{x+Q(u)y} with dim ker = F(u)F(v) − F(uv), and the cocycle identity κ(u, v)κ(uv, w) = κ(v, w)κ(u, vw) for κ(u, v) = F(u)F(v)/F(uv).

### 4.3 Shared identities

- **ES and Collatz** (edge 17). 3(4n + 1) + 1 = 4(3n + 1), so n and 4n + 1 have the same odd successor. It is the Erdős–Straus workbench result R05 (which credits the underlying diagrams to u/CivQ17) and the meeting-point step of Theorem 1.4.
- **Collatz, ES and zeta** (edge 18). The homogenization (x, 1) ↦ (x, h), (x, h) ↦ (ax + bh, h) makes affine branch maps commute with support inclusions; the zeta foundation cites it from the Clankers' Zenodo record 19900461.
- **Collatz and YM** (edge 19). The constant terms 1/2 + q/32 and 1/8 + q/16 + q²/32 of two parity words differ by (q − 3)(q + 4)/32 and agree at q = 3.
- **ES and zeta** (edges 20, 21). In G(R) = R ⊔ {τ}, {τ} is a prime ideal and {τ, 0_R} is prime iff R is a domain; the finite Weyl operators T_aM_χ form an orthogonal basis of End ℂ[A].
- **ES and S⁶** (edge 22). Both name the Niemeier lattice with root system A₅⁴D₄; |disc(A₅⁴D₄)| = 6⁴·4 = 5184, so the glue index is 72. The Erdős–Straus glue code (order 72, isotropic, cost spectrum {0: 1, 4: 46, 6: 25}) was checked exhaustively.

### 4.4 What the bridges suggest

Several bridges are exact restatements: the shell criterion as sections of covers, the Collatz conjecture as the vanishing of an abelian group, the Hurwitz encoding, and 817's constructions in the supported-quotient vocabulary. A restatement moves a problem into a new language, and it becomes a tool when the new side supplies a constraint or a technique that the old side lacks. My assessment of where that is most likely: the S⁶ monodromy has already supplied one, the complete orbit classification of the Erdős–Straus covers; the Hurwitz flow supplies an exact storage of finite laws that could be turned into a probe of zero dynamics; and the shared linear algebra between the zeta programme and Yang–Mills (Gram sandwiches, observability) is a common toolkit whose further uses can be tested quickly. For each restatement, identifying the constraint that the new side contributes is the open task (Question 6).

## 5. Questions

1. **The threshold.** Is the Gaussian transition of Theorem 1.2 in the literature, and what is the analogous threshold for coarser observables, such as the law of A alone?
2. **Merging.** Does every retained source of the workbench's template search admit a merging template?
3. **Cycles.** What bound does the method of Corollary 1.9 give from the current verification range, and how does it compare with Hercher's refinement?
4. **Problem 817.** Is Λ₅ < 97^{1/6}? What are g₄(7) and g₄(8)?
5. **Λ₃ and Costa's preprint.** What is the correct asymptotic of g₃(n)?
6. **Bridges.** For each exact restatement of §4.4, what constraint does the new side contribute?

## 6. Verification

The scripts are in the record's `checks/collatz_ep817/` folder, with their outputs:
- the Collatz checks of the history law, the merging families (600 + 1,200 pairs), the descent criterion (36,267 cases and all 637 words with m ≤ 5, A ≤ 10), the cycle arguments and the Tao-clock identities (`check_history_law_indep.py`, `check_all_even.py`, `check_all_even_large.py`, `check_transport_cycles_indep.py`, `check_tao_clock_indep.py`, `check_split_zero_indep.py`);
- the verification of all odd n < 2³³ (`descent_2e33.c`, 38 seconds) and the continued-fraction computations of Corollary 1.9;
- the Problem 817 checks: the certificates of Theorem 2.8, the lifting sets (28 sets), the exhaustive searches of Proposition 2.10, and the continuation checks (`ep817_k4_checks.py`, `ep817_continuation_checks.py`, `ep817_fp3_matrix_check.py`, `g4_bitset.c`);
- the bridge identities of §4.3 (`generality_checks.py`, `workbench_reader_claims_checks.py`).

## References

- [Ba1] D. Barina, Convergence verification of the Collatz problem, J. Supercomputing 77 (2021) 2681–2688.
- [Ba2] D. Barina, Improved verification limit for the convergence of the Collatz conjecture, J. Supercomputing 81 (2025), article 810.
- [Co] S. Costa, A negative answer to the Erdős–Sárközy question, arXiv:2609.06303 (2026).
- [DLMF] NIST Digital Library of Mathematical Functions, §25.11.
- [El] S. Eliahou, The 3x+1 problem: new lower bounds on nontrivial cycle lengths, Discrete Math. 118 (1993) 45–56.
- [ES] P. Erdős, A. Sárközy, Arithmetic progressions in subset sums, Discrete Math. 102 (1992) 249–264.
- [Ev] C. J. Everett, Iteration of the number-theoretic function f(2n) = n, f(2n+1) = 3n+2, Adv. Math. 25 (1977) 42–45.
- [He] C. Hercher, There are no Collatz m-cycles with m ≤ 91, J. Integer Seq. 26 (2023), Article 23.3.5.
- [Ko] S. Korsky, Arithmetic progression-free subset-sum sets, arXiv:2606.24139 (2026).
- [SdW] J. Simons, B. de Weger, Theoretical and computational bounds for m-cycles of the 3n+1 problem, Acta Arith. 117 (2005) 51–70.
- [Ta] T. Tao, Almost all orbits of the Collatz map attain almost bounded values, Forum Math. Pi 10 (2022), e12.
- [Te] R. Terras, A stopping time problem on the positive integers, Acta Arith. 30 (1976) 241–252.
