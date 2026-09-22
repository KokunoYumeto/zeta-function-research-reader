# The prime 0 of G(ℤ) and Weil's positivity condition

- **Prepared:** 22 September 2026 by Claude (Anthropic; model id `claude-opus-5-5`), in a Cowork session, at the owner's request. The request was to take τ, determine what it does to the spectrum of primes, and then what that does to Weil's positivity condition.
- **Status of claims:** every statement is one of:
  - proved here;
  - quoted with a locator;
  - labelled **[inference]** (a structural reading, not a theorem) or **[open]**.
- **Checks:** nothing here is Lean-checked. Numerical statements refer to:
  - `prime_zero_checks.py`, output in `prime_zero_checks_OUTPUT.txt`;
  - `check_pro_A2.py`, output in `check_pro_A2_OUTPUT.txt`;
  - the earlier calibration `weil_localized_check.py`.
  All checks pass.
- **Refereeing:** an independent subagent referee read the whole note against its sources (22 September 2026). It found no error in the proofs of Theorems 1, C, D and E or of Propositions 2.2 and 2.3. Its corrections are incorporated: labels on identifications, historical attributions, one sign argument (§3.4(iv)) and one citation locator.
- **Relation to the earlier restart note:** `TAU_PRIME_SPECTRUM_AND_WEIL_POSITIVITY.md` tracked only the new generic point P_τ and the τ-fixed points. Its theorems stand, but it omitted the prime 0. **[inference]** Following the owner, I take the prime 0 to be the object through which τ acts on Weil's criterion; §§2–3 give the evidence. On that question this note supersedes the earlier note's §§2–3.

## 0. Sources and notation

**Paper one** is *A Note on the Globalization Semiring G(ℤ)*, Zenodo, DOI 10.5281/zenodo.18976982 (record of 12 March 2026; the owner uploaded the TeX). Theorem numbers follow its TeX:
- Theorem 2.2: ideals;
- Corollary 2.3: prime ideals;
- Corollary 2.4: dim S = 2;
- Proposition 3.1: units and irreducibles;
- **Theorem 3.2: the element 0 is prime but not irreducible;**
- Theorem 3.4: congruences;
- Corollary 3.5: ζ_S = ζ;
- Theorem 4.2: Frac S ≅ 𝔹;
- Corollary 4.3: stalks;
- Theorem 5.5: the contracted monoid algebra.

**P1** is *Split-Zero Projective Geometry and Leibniz Monads* (June 2026 draft). It is used for:
- `cor:two-zero-localizations`: G(R)[e⁻¹] ≅ 𝔹;
- `thm:generic-suspension`;
- the example "The shifted generic point of Spec ℤ";
- `thm:support-zeta-product`.

**P2** is *Split Support Geometry: Universal Zero Fibres, Arithmetic Curves, and Frobenius-Perfect Quantization* (June 2026 draft, version 11). It is used for `thm:trivial-place-neutrality` (l.5543).

**Weil's form** uses the repository convention, `satellites/22_rh_counterexample_routes.tex:348–398`, equation `eq:rh-full-weil-test`.

**Notation.**
- S = G(ℤ) = ℤ ⊔ {τ}.
- 0 ∈ ℤ is the supported zero, written e in P1. τ is the semiring zero.
- P_τ = {τ}, P_0 = {0, τ}, P_p = pℤ ∪ {τ}.
- **Weil's form** is W(f,g) = Σ_ρ m_ρ conj f̂(γ̄_ρ) ĝ(γ_ρ), with γ_ρ = (ρ − ½)/i and f̂(z) = ∫f(u)e^{−iuz}du. It is conjugate-linear in the first slot (`satellites/22_rh_counterexample_routes.tex:348–359`).
- Λ(s) = π^{−s/2}Γ(s/2)ζ(s) is the completed zeta function. The von Mangoldt function is always written Λ(n), with an integer argument.
- ϑ₊(x) = Σ_{n≥1} e^{−πn²x} is the theta tail.

---

## 1. The prime 0

**Theorem 1.**

- **(a)** Up to the units ±1, the prime elements of S are 0 and the rational primes p.
- **(b)** 0·0 = 0, and n | 0 for every n ∈ ℤ. The element 0 is not irreducible.
- **(c)** The principal ideal (0) = S·0 equals P_0.
  - It is prime, and P_0·P_0 = P_0.
  - P_0 = ⋂_p P_p.
  - Its height is 1.
  - Its closure V(0) = {P_0} ∪ {P_p} is homeomorphic to Spec ℤ, and D(0) = {P_τ}.
- **(d)** S[0⁻¹] ≅ 𝔹. The stalk at P_0 is G(ℚ), whose maximal ideal is 0·G(ℚ) = {0, τ}. The Bourne quotients are S/P_0 ≅ ℤ and G(ℚ)/(0) ≅ ℚ.
- **(e)** For a prime element π put v_π(x) := sup{k ≥ 0 : π^k | x}.
  - v_0 takes only the values 0 and ∞, and v_0 = ∞ exactly on P_0.
  - The absolute value c^{−v_0} (for any c > 1) is the trivial absolute value on ℤ.
  - The archimedean absolute value is not of the form c^{−v_π} for any prime element π.
- **(f)** S is Noetherian (ascending chain condition on ideals). P_p = S·p is a principal prime of height 2. Hence Krull's principal ideal theorem, which holds for Noetherian commutative rings (Matsumura, *Commutative Ring Theory*, Theorem 13.5), fails for S.

**Proof.**

*(a)* By Proposition 3.1 and Theorem 3.2 of paper one, 0 is prime and the irreducibles are ±p.

p is prime in S. Suppose p | ab, so ab = p·c.
- If c = τ, then ab = τ, so a = τ or b = τ; and p | τ, because τ = p·τ.
- If c ∈ ℤ, then a, b ∈ ℤ and p | ab in ℤ, so p divides a or b.

No other element is prime.
- τ is the semiring zero and ±1 are units.
- Suppose n ∈ ℤ∖{0} has at least two prime factors counted with multiplicity. Write n = ab with a, b ∈ ℤ, |a|, |b| > 1, so |a| < |n|. Then n | ab. But n | a would require a = n·c. That is impossible: c = τ gives τ ≠ a, and c ∈ ℤ gives |a| ≥ |n| because a ≠ 0, contradicting |a| < |n|. The same holds for b.

*(b)* In ℤ, 0·0 = 0 and 0 = n·0. Paper one, Theorem 3.2, gives 0 = 2·0 with neither factor a unit.

*(c)* S·0 = {0·n, 0·τ} = {0, τ}.
- Primality is paper one, Corollary 2.3.
- P_0·P_0 is generated by 0·0 = 0, 0·τ = τ and τ·τ = τ, so it equals {0, τ}.
- ⋂_p P_p = (⋂_p pℤ) ∪ {τ} = {0, τ}.
- The primes inside P_0 are P_τ and P_0 (Corollary 2.3), so the height is 1.
- The statements about V(0) and D(0) are P1, `thm:generic-suspension`.

*(d)* The first statement is P1, `cor:two-zero-localizations`, and the stalk is paper one, Corollary 4.3.

By Theorem 2.2 applied to the field ℚ (P1, `thm:prime-classification`), the ideals of G(ℚ) are {τ}, {0, τ} and G(ℚ). So {0, τ} = 0·G(ℚ) is the maximal ideal.

Bourne congruence: x ~ y iff x ⊕ i = y ⊕ j for some i, j ∈ P_0.
- τ ~ 0, because τ ⊕ 0 = 0 ⊕ τ.
- For an integer m, m ⊕ i = m for both i ∈ {0, τ}, so distinct integers remain distinct.

Hence S/P_0 ≅ ℤ. This is also paper one, Theorem 3.4, with n = 0. The same argument gives G(ℚ)/(0) ≅ ℚ.

*(e)* Since 0^k = 0 for k ≥ 1, we have 0^k | x iff 0 | x iff x ∈ {0·c : c ∈ S} = {0, τ}. So c^{−v_0} is 1 on ℤ∖{0} and 0 on P_0, which is the trivial absolute value.

Each c^{−v_π} is ultrametric. If π^k | x and π^k | y, write x = π^k a and y = π^k b; then x ⊕ y = π^k(a ⊕ b). The archimedean absolute value is not ultrametric, since |1+1|_∞ = 2 > 1.

*(f)* By Theorem 2.2 the ideals are {τ} and the nℤ ∪ {τ}. An ascending chain of these is an ascending chain of ideals of ℤ, so it stabilizes. P_p = S·p by Theorem 2.2, and P_τ ⊊ P_0 ⊊ P_p (Corollary 2.4). ∎

**Remark [inference].** Spec S is two-dimensional (paper one, Corollary 2.4). By (c) and (d), the arithmetic curve Spec ℤ is the zero locus V(0) of the single prime element 0, and the generic point of Spec S has residue 𝔹. τ turns the classical generic point (0) into a prime divisor.

---

## 2. The local factor of the prime 0: three computations, one answer

### 2.1 Norms

**Lemma 2.1.** Let N be a multiplicative function from the ideals of S to [0, ∞]. Then N(P_0) ∈ {0, 1, ∞}.

*Proof.* P_0² = P_0 gives N(P_0)² = N(P_0) in [0, ∞]. The solutions are 0, 1 and ∞. ∎

- **The Bourne norm** of paper one (Corollary 3.5) gives N(P_0) = |ℤ| = ∞. The Euler factor (1 − N(P_0)^{−s})⁻¹ is then 1 for Re s > 0.
  - This is why ζ_S = ζ: the Euler product cannot see the prime 0.
  - My earlier restart note stopped here.
- **The value 1** is the only finite nonzero one. Then (1 − 1^{−s})⁻¹ diverges.
  - Soulé's regularization is ζ_X(s) := lim_{q→1} Z(X, q^{−s})(q − 1)^{N(1)} (Connes–Consani, *Compositio Math.* 146 (2010) 1383–1415, §2, eq. (3), after Soulé, *Moscow Math. J.* 4 (2004) 217–244).
  - Applied to one point counted once (N(q) = 1, Z = (1 − T)⁻¹), it gives lim_{q→1} (q − 1)/(1 − q^{−s}) = 1/s. By l'Hôpital, the derivative of the numerator is 1 and that of the denominator is s·q^{−s−1} → s.
  - Check (2) confirms this numerically.
- **An analogy in P1 [inference].** P1's split projective line has Z_sp(ℙ¹/𝔽_q, T) = 1/((1 − T)³(1 − qT)) (`thm:support-zeta-product` and the following remark). Its two extra degree-zero factors (1 − T)⁻¹ belong to the τ-points 0_τ and ∞_τ, not to the supported zero e. The match with the prime 0 is only in the counting function N ≡ 1.

### 2.2 Dilation by 0 and Poisson summation

For φ: ℝ → ℂ put (U_a φ)(x) = φ(ax). For a = 0:
- U_0 φ = φ(0)·𝟙 has rank one;
- U_0² = U_0.

The **split theta** is Θ_S φ(x) := Σ_{a ∈ S∖{τ}} (U_a φ)(x) = φ(0) + Σ_{n≠0} φ(nx). The absent element τ contributes nothing.

The τ-base model's theta map, Θφ(x) = Σ_{n≠0} φ(nx) (`workbenches/tau-base-cohomology/TAU_BASE_MODEL.md:90–100`), is Θ_S with the prime 0 removed.

*Convention.* The model's dilation is U_aF(x) = F(x/a), defined for a > 0 (`TAU_BASE_MODEL.md:233`). This is the inverse of the U_a used here. So U_0 is not an operator of the model, and the model's "action a" on 𝓛₁ is action a⁻¹ in this note's convention.

**Proposition 2.2.**

(i) For Schwartz φ and x > 0, with φ̂(ξ) = ∫φ(y)e^{−2πiyξ}dy:

Θ_S φ(x) = x⁻¹ Θ_S φ̂(1/x) exactly.

Without the prime 0, the identity for Θ acquires the correction term φ̂(0)/x − φ(0).

(ii) Let θ(x) = Σ_{n∈ℤ} e^{−πn²x} = 1 + 2ϑ₊(x). Then for all s ≠ 0, 1:

Λ(s) = ∫_1^∞ ϑ₊(x)(x^{s/2} + x^{(1−s)/2}) dx/x + [1/(s − 1) − 1/s].

The integral is entire. The bracket comes entirely from the n = 0 term, the prime 0, and its Poisson dual.

*Proof.*

(i) Apply Poisson summation Σ_n g(n) = Σ_n ĝ(n) to g(y) = φ(xy), for which ĝ(ξ) = x⁻¹φ̂(ξ/x). The n = 0 terms are φ(0) on the left and φ̂(0)/x on the right. Removing them gives the corrected identity for Θ.

(ii) For Re s > 1, ∫_0^∞ ϑ₊(x)x^{s/2} dx/x = Σ_{n≥1}(πn²)^{−s/2}Γ(s/2) = Λ(s).

Part (i) with φ(y) = e^{−πy²} (so φ̂ = φ), after the substitution x ↦ √x, gives θ(1/x) = √x θ(x). Equivalently,

ϑ₊(1/x) = √x ϑ₊(x) + (√x − 1)/2.

The term (√x − 1)/2 is half the difference of the two n = 0 terms.

Substitute this into ∫_0^1 ϑ₊(x)x^{s/2} dx/x. The n = 0 part contributes

½∫_1^∞ (y^{(1−s)/2} − y^{−s/2}) dy/y = 1/(s − 1) − 1/s  (Re s > 1).

The resulting right-hand side is meromorphic on ℂ, which gives the continuation. (Riemann 1859; Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., §2.6.) Check (1) agrees to within 6·10⁻³² at s = 2.5, 0.3 + 4i and −1.7 + 0.9i. ∎

**Adelic form.** In Tate's thesis the same statement reads as follows. Consider Poisson summation Σ_{γ∈ℚ} f(γa) = |a|⁻¹ Σ_γ f̂(γ/a) (Tate 1950, in Cassels–Fröhlich 1967, Theorem 4.2.1, which Tate calls the Riemann–Roch theorem). Its γ = 0 term produces −f(0)/s and f̂(0)/(s − 1) in Main Theorem 4.4.1. No other γ produces a pole.

**The prime 0 in the τ-base model.** The model's moment map m(φ) = (φ(0), ∫φ), with lines 𝓛₀ and 𝓛₁ (`TAU_BASE_MODEL.md:252–258`), is exactly the pair of prime-0 functionals of the theta picture: U_0, and its Poisson dual φ ↦ φ̂(0) = ∫φ.

Within the even Schwartz functions, the model's test space V = {φ even, φ(0) = 0, φ̂(0) = 0} (`TAU_BASE_MODEL.md:90–92`) is their common kernel. On V the correction in (i) vanishes, so Θ already satisfies the exact Poisson identity Θφ(1/x) = xΘφ̂(x) there.

Consequently the Mellin transform Z(φ, s) = ∫_0^∞ Θφ(x)x^s dx/x, which equals 2ζ(s)·Mφ(s) for Re s > 1, is entire. Split the integral at x = 1 and substitute the exact identity on (0, 1):

Z(φ, s) = ∫_1^∞ Θφ(x)x^s dx/x + ∫_1^∞ Θφ̂(x)x^{1−s} dx/x.

Both integrals are entire, because Θφ and Θφ̂ decay faster than any power at ∞. So on V the prime-0 terms −φ(0)/s and φ̂(0)/(s − 1) are absent: V is the kernel of the prime 0.

### 2.3 The place of the prime 0

Let M(ℤ) be Berkovich's spectrum of (ℤ, |·|_∞): the multiplicative seminorms bounded by |·|_∞, with the weakest topology in which each x ↦ |n|_x is continuous. By Ostrowski (*Acta Math.* 41 (1916) 271–284), its points are:
- the trivial norm |·|_0;
- |·|_p^ε for 0 < ε < ∞;
- the seminorm |·|_{p,∞} with kernel pℤ;
- |·|_∞^ε for 0 < ε ≤ 1.

This description, with each p-adic branch homeomorphic to [0, ∞] and the archimedean branch to [0, 1], is in J. Poineau, *An introduction to the Berkovich line over ℤ*, §2 and Figure 1. The space M(ℤ) is Example 1.4.1 of Berkovich, *Spectral Theory and Analytic Geometry over Non-Archimedean Fields* (AMS, 1990), as cited in M. Baker's 2007 Arizona Winter School notes (footnote 10).

**Proposition 2.3.**

- (i) The trivial norm, which is the absolute value of the prime 0 by Theorem 1(e), lies in the closure of every branch.
- (ii) M(ℤ) is path-connected.
- (iii) M(ℤ) ∖ {|·|_0} is not connected. It is the disjoint union of the open sets B_p = {x : |p|_x < 1}, one for each prime p, and B_∞ = {x : |2|_x > 1}.

*Proof.*

(i) For n ≠ 0, |n|_v^ε → 1 = |n|_0 as ε → 0; and |0|_v^ε = 0 = |0|_0. So ε ↦ |·|_v^ε extends continuously to ε = 0 with value |·|_0.

(ii) Each branch together with |·|_0 is the image of a continuous path through |·|_0:
- for ∞, with ε ∈ [0, 1];
- for p, with ε ∈ [0, ∞]. At ε = ∞ the limit |n|_p^ε → 0 if p | n and → 1 otherwise, which is |n|_{p,∞}.

(iii) B_p and B_∞ are open, as preimages of open sets.
- A point |·|_q^ε or |·|_{q,∞} satisfies |p| < 1 iff q = p.
- A point |·|_∞^ε has |2| = 2^ε > 1 and |p| = p^ε > 1.
- All non-archimedean points have |2| ≤ 1.

So every nontrivial point lies in exactly one of these sets, none of them contains |·|_0, and at least two are nonempty. ∎

**The same point in Sédillot's framework.** The owner uploaded A. Sédillot, *Topological adelic curves*, arXiv:2503.20156v2. At TeX line 1379 it adjoins a point ∗ carrying the trivial absolute value to any topological adelic curve, with ν′(∗) = 1, and notes that the result is proper iff the original is. That is, the product formula does not see this point. P2 proves the same neutrality for adelic curves (`thm:trivial-place-neutrality`, l.5543).

So the prime 0 is the place that connects the space of places, and it is invisible to the product formula.

### 2.4 One factor

For Re s > 1, exactly:

Λ(s) = (1/s) · [2π^{−s/2}Γ(1 + s/2)] · ∏_p (1 − p^{−s})⁻¹,

because Γ(s/2) = (2/s)Γ(1 + s/2). Check (3) confirms this. In this identity the factor 1/s is the Gamma recurrence.

**[inference]** The factor 1/s is the regularized prime-0 factor of §2.1; the match depends on reading "a prime of norm 1" as a point with counting function N ≡ 1. The term −1/s is the s = 0 half of the prime-0 term of §2.2. The three computations describe one object. The prime 0 is an H⁰-type point of Spec S. The functional equation s ↦ 1 − s, which is Poisson duality, carries its term −1/s to the other half, 1/(s − 1).

---

## 3. What the prime 0 does to Weil's positivity condition

### 3.1 The decomposition

In the repository convention, with h = f∗f^⋆ and ĥ(z) = f̂(z)·conj f̂(z̄):

**W(f,f) = W_0(f) + A(f) − P(f),**

where:
- **W_0(f)** = ĥ(i/2) + ĥ(−i/2) = 2Re(a b̄), with a = f̂(i/2) = ∫f(u)e^{u/2}du and b = f̂(−i/2) = ∫f(u)e^{−u/2}du. These are the pole terms.
- **A(f)** = ∫ ĥ(t)G(t)dt, with G(t) = (Re ψ(¼ + it/2) − log π)/2π. This is the archimedean term.
- **P(f)** = Σ_{n≥2} Λ(n)n^{−1/2}{h(log n) + h(−log n)}. These are the rational primes.

**Proposition 3.1.**

- (i) W_0 is exactly the sum of the pole terms. In Riemann's theta splitting (Proposition 2.2(ii)) these poles come from the n = 0 term alone, and on that basis W_0 is *called* the prime-0 contribution. This is a definition, not a theorem. In the Euler factorization Λ = Γ_ℝ·ζ, the pole at s = 0 comes from Γ(s/2) (ζ(0) = −½ ≠ 0) and the pole at s = 1 from ζ.
- (ii) W_0 = ½(|a+b|² − |a−b|²). It is a hyperbolic plane of signature (1,1). On even f, a = b and W_0 = 2|a|² ≥ 0 has rank one.
- (iii) The coefficients Λ(n)n^{−1/2} of P are nonnegative, and P enters W with a minus sign. W_0 is the only term that comes neither from the archimedean place nor from a rational prime.

*Proof.*

(i) In the explicit formula (Weil 1952), the pole terms are the contributions of the poles of Λ at s = 0 and s = 1:
- a simple pole gives Λ′/Λ residue −1;
- the pole at s = 0 contributes ĥ at γ = (0 − ½)/i = i/2;
- the pole at s = 1 contributes ĥ at γ = −i/2.

By Proposition 2.2(ii), in the theta splitting these poles are produced by the n = 0 term alone.

(ii) The identity 2Re(ab̄) = ½(|a+b|² − |a−b|²) is algebra. If f is even, then f̂ is even and a = b. Check (5) gives W_0 = 0.948 for two bumps of the same sign and −0.550 for two bumps of opposite sign.

(iii) Λ(n) ≥ 0. ∎

**Calibration.** The test function is `weil_localized_check.py`'s f̂(z) = 2ξ(½ + iz)/(γ₁² − z²). The explicit formula was checked there to 1.3·10⁻³³. The values are:

| Term | Value |
|---|---|
| W_0 (prime 0) | 4.9979778719·10⁻⁵ |
| A (archimedean) | −4.8674531658·10⁻⁵ |
| P (rational primes) | 1.2861078883·10⁻⁶ |
| W | 1.9139173403·10⁻⁸ |

The prime 0 supplies the entire positive part. The archimedean place and the rational primes remove all of it except 3.8·10⁻⁴ of it.

### 3.2 Theorem C: the Castelnuovo–Severi form of Weil's criterion

Put I(f) := P(f) − A(f). This is the contribution of the rational primes and the archimedean place. Then W = W_0 − I.

**Theorem C.** The following are equivalent:
1. RH;
2. I(f) ≤ W_0(f) for every f ∈ C_c^∞(ℝ);
3. I(f) ≤ 0 for every f ∈ C_c^∞(ℝ) with a(f) = b(f) = 0.

Moreover, (3) holds for all complex f iff it holds for all real-valued f.

*Proof.*

*(1)⇒(2).* Under RH, W(f,f) = Σ_ρ m_ρ|f̂(γ_ρ)|² ≥ 0 (repository, *Finite negative-certificate test*).

*(2)⇒(3).* If a = b = 0, then W_0 = 0.

*(3)⇒(1).* Suppose RH fails, and let ρ₀ be a zero with Re ρ₀ < ½.

- **Choice of κ.** Take κ ∈ C_c^∞ with κ̂(γ_{ρ₀}) ≠ 0 and κ̂(γ̄_{ρ₀}) ≠ 0. Such κ exists: κ̂ is entire and not identically zero, so replacing κ by κ(·/λ) (with transform λκ̂(λz)) works for all but countably many λ.
- **Choice of φ.** Put φ := κ″ − κ/4. Then φ̂(z) = −(z² + ¼)κ̂(z).
  - This vanishes at z = ±i/2, so a(φ) = b(φ) = 0.
  - It does not vanish at γ_{ρ₀} or γ̄_{ρ₀}, because these are not ±i/2 (ρ₀ ∉ {0, 1}).
- **Unboundedness.** F(T) := W(φ, φ(· − T)) is unbounded on [0, ∞). This is the proof of Lemma U of `TAU_PRIME_SPECTRUM_AND_WEIL_POSITIVITY.md` §3 (Steps 1–3, a Laplace-transform argument). That proof works for any φ ∈ C_c^∞ with φ̂(γ_{ρ₀})·φ̂(γ̄_{ρ₀}) ≠ 0.
- **Construction.** Put f := φ + ωφ(· − T) with ω = −conj F(T)/|F(T)|.
  - This choice of phase uses the convention that W is conjugate-linear in the first slot. In the opposite convention the phase is −F(T)/|F(T)|.
  - Hermitian symmetry and translation invariance give W(f,f) = 2W(φ,φ) − 2|F(T)|. This is < 0 for suitable T.
  - Also a(f) = a(φ)(1 + ωe^{T/2}) = 0, and similarly b(f) = 0.
  - Hence I(f) = −W(f,f) > 0, contradicting (3).

*Real reduction.* For real u, v the zero set is closed under γ ↦ −γ̄, so W(u,v) is real and W(u + iv) = W(u) + W(v). Moreover a(u + iv) = a(u) + i·a(v) with a(u), a(v) real, and similarly for b. ∎

**Remarks.**
- (1)⟺(2) is Weil's criterion (Weil 1952; Bombieri, *Rend. Mat. Acc. Lincei* s.9 v.11 (2000) 183–233).
- (1)⟺(3) is its codimension-two form: positivity is needed only on the kernel of the prime 0.
- The only new content here is the identification of that codimension-two constraint with the prime 0 of G(ℤ).
- **What the prime 0 does not do.** On that kernel W_0 = 0, so (3) reads P(f) ≤ A(f): the archimedean term must dominate the rational primes. The prime 0 fixes the subspace on which positivity is needed, but contributes nothing to the inequality there. Everything that is hard about RH remains in P ≤ A on that subspace.

### 3.3 Hodge-index reading

The standard results are these. For a curve C over 𝔽_q, let f₁ = {pt} × C and f₂ = C × {pt}. The Castelnuovo–Severi inequality on C × C,

D² ≤ 2(D·f₁)(D·f₂),

implies RH for C. Weil (1948) proved RH for curves using correspondences on C × C and the Jacobian. Two later papers recast the argument:
- Mattuck–Tate (*Abh. Math. Sem. Hamburg* 22 (1958) 295–299) derive the inequality from Riemann–Roch on the surface.
- Grothendieck (*J. reine angew. Math.* 200 (1958) 208–215) derives it from the Hodge index theorem.

See Hartshorne, *Algebraic Geometry*, V, Theorem 1.9 and Exercises 1.9–1.10. Stepanov (1969) and Bombieri (Sém. Bourbaki, exp. 430, 1973) give a different proof, using Riemann–Roch on the curve alone.

**Dictionary [inference].**

| Weil form for ζ | Surface C × C |
|---|---|
| I(f) (sum of local terms at the places other than 0) | D² |
| W_0(f) = 2Re(ab̄) | 2(D·f₁)(D·f₂) |
| (a, b) | (D·f₁, D·f₂) |
| {a = b = 0} | primitive classes |

Under this dictionary, Theorem C says: RH is equivalent to the Hodge-index inequality for I, with the prime 0 as the fibre plane. The prime 0 supplies the fibres in Weil's argument. It does not supply the surface, or the Riemann–Roch theorem from which the Hodge index inequality follows in the Mattuck–Tate and Grothendieck form of Weil's proof.

### 3.4 The owner's "sub-τ" argument

**The argument.** Positivity is a property of the primes, because negativity with respect to the absolute base would require something below τ, and nothing lies below τ because τ is global.

**(i) What is true (proof).** Consider the natural preorder x ≼ y ⟺ ∃z: x ⊕ z = y.
- τ is its least element, because τ ⊕ y = y.
- Only τ lies below τ: x ⊕ z = τ forces x = z = τ.
- {τ} is prime (paper one, Corollary 2.3).

**(ii) Where the step fails as stated (proof).** The support order does not see signs.
- For all m, n ∈ ℤ (or ℝ), m ⊕ (n − m) = n. So m ≼ n and n ≼ m.
- χ(−1) = χ(1) = 1 (P1, definition of the support character).
- Hence a value W(f,f) = −c < 0 is a supported element of G(ℝ), not an element below τ.

So the algebra of G(ℤ) alone does not turn "negative" into "below τ".

**(iii) A form in which the argument works.** Positivity is automatic for a quantity that is a dimension or a cardinality, because such quantities take values in a semiring whose least element is the empty object. The Mattuck–Tate form of Weil's proof is of this kind: it obtains D² ≤ 2(D·f₁)(D·f₂) from h⁰ ≥ 0 together with Riemann–Roch on the surface.

**[inference]** The owner's mechanism would be realized if I, on the kernel of the prime 0, were expressed through dimensions of spaces of sections over the τ-base. That is a Riemann–Roch theorem on the square. **[open]**

**(iv) "Positivity is a property of the primes."**
- In W, the rational primes enter as −P. Only the coefficients Λ(n)n^{−1/2} are nonnegative; the terms Λ(n)n^{−1/2}·2Re h(log n) have no fixed sign. For example, f = g − g(· − log 2) with g a narrow bump gives h(log 2) = −‖g‖², so there the prime 2 *increases* W.
- In the form Theorem C(2), positivity says that the prime 0 bounds the other places: I ≤ W_0.
- In the form Theorem C(3), on the kernel of the prime 0, it says P ≤ A: the archimedean place bounds the rational primes, and the prime 0 plays no part in the inequality.
- In Deligne's Weil I (*Publ. Math. IHÉS* 43 (1974), §3, Théorème 3.2), the positivity used at closed points is Tr(F_x^{⊗2k}) = Tr(F_x)^{2k} ≥ 0. It bounds Frobenius eigenvalues on *stalks*.
- For ζ, the stalk eigenvalue at every p is 1, from the Euler factor (1 − p^{−s})⁻¹. The zeros are eigenvalues on no stalk.
- Deligne reaches H¹ of a curve as a stalk of R¹f_*ℚ_ℓ on the base of a Lefschetz pencil. The corresponding family for Spec ℤ has not been constructed. **[open]**

---

## 4. Theorem D: the prime 0 alone cannot force positivity

**Setup** (Part A of `CHATGPT_PRO_TASK_A_B.md`).
- δ₀ ∈ (0, ½) and γ₀ > 2 with γ₀ ≠ γ₁, γ₂, such that ρ₀ = ½ + δ₀ + iγ₀ is not a zero of ξ.
- γ₁ = 14.1347… and γ₂ = 21.0220… are the first two ordinates.
- Q_0(s) = ((s − ½)² − (δ₀ + iγ₀)²)((s − ½)² − (δ₀ − iγ₀)²).
- Q_1(s) = ((s − ½)² + γ₁²)((s − ½)² + γ₂²).

Both are monic quartics in s − ½ with real coefficients.

Put Λ̃ := Λ·Q_0/Q_1.

**Theorem D.**

(i) Λ̃ has the following properties:
- it is meromorphic of order 1, with simple poles exactly at s = 0 and s = 1;
- Λ̃(1 − s) = Λ̃(s), and Λ̃ is real on ℝ;
- its archimedean factor is Γ_ℝ(s) = π^{−s/2}Γ(s/2);
- its prime-0 term is exactly W_0. The residues of Λ̃ at 0 and 1 are c times those of Λ, with c = Q_0(0)/Q_1(0) > 0, but only the pole orders enter the logarithmic derivative.

(ii) Its Weil form W̃(f,f), the sum of conj f̂(γ̄) f̂(γ) over the zeros of Λ̃ with multiplicity, is negative for some f ∈ C_c^∞ with a(f) = b(f) = 0.

(iii) Λ̃ is not of the form Γ_ℝ(s)·D(s) with D a Dirichlet series convergent in some half-plane.

**Consequence.** Consider any argument whose only inputs are:
- the prime-0 term W_0;
- the functional equation s ↦ 1 − s;
- the archimedean factor Γ_ℝ;
- order-one growth.

No such argument can prove W ≥ 0 for ζ, because all four inputs hold for Λ̃ and W̃ ≥ 0 fails. The rational primes, that is, the Euler product, must enter. In Theorem C they enter through I(f). This says nothing against arguments that use the Euler product.

*Proof.*

(i) Q_0/Q_1 is rational. It is holomorphic and nonzero at 0 and 1:
- Q_1(0) = (¼ + γ₁²)(¼ + γ₂²) > 0;
- Q_0(0) = |¼ − (δ₀ + iγ₀)²|² > 0, because (δ₀ + iγ₀)² = ¼ would need γ₀ = 0.

The zeros of Q_1 are ½ ± iγ₁ and ½ ± iγ₂. These are simple zeros of Λ: the first 1.5·10⁹ zeros are simple and on the line (van de Lune, te Riele and Winter, *Math. Comp.* 46 (1986) 667–681). So Λ̃ has no other poles.

Q_0 and Q_1 are polynomials in (s − ½)² with real coefficients, which gives the symmetry and reality. A simple pole contributes residue −1 to Λ̃′/Λ̃, whatever its residue in Λ̃. Check (4): c = 1.13·10⁷ for (δ₀, γ₀) = (0.25, 1000), and c = 70.67 for (0.01, 50), with equal values at s = 0 and s = 1.

(ii) The zeros of Λ̃ in the strip are:
- those of ξ other than ½ ± iγ₁ and ½ ± iγ₂;
- together with ρ₀, 1 − ρ₀, ρ̄₀ and 1 − ρ̄₀.

Their counting function is O(T log T). Lemma U and the construction in Theorem C (3)⇒(1) use only four facts, all of which hold for Λ̃:
- the zero set is closed under ρ ↦ 1 − ρ̄ and ρ ↦ ρ̄;
- every zero satisfies 0 < Re ρ < 1, so |Im γ_ρ| ≤ ½;
- one zero is off the line;
- the count O(T log T).

(iii) Suppose Γ_ℝ(s)D(s) = Λ̃(s).
- Then D = ζ·R with R := Q_0/Q_1.
- D converges absolutely for σ greater than its abscissa of convergence plus 1. So D/ζ = D·Σμ(n)n^{−s} is a Dirichlet series, absolutely convergent for large σ. So R(σ) = Σc_n n^{−σ} → c₁, with R(σ) − c₁ = O(2^{−σ}).
- A rational function with this property is constant.
- R(∞) = 1, so R ≡ 1 and Q_0 = Q_1. This is impossible, because their zero sets differ.

ChatGPT Pro gave the same argument for A1, and I checked it (§7). ∎

---

## 5. The chain "0 is a prime → part of the spectrum → smooth spectrum → RH"

| Step | Status |
|---|---|
| 0 is a prime | **Proved.** Theorem 1(a); paper one, Theorem 3.2. |
| 0 is part of the spectrum | **Proved.** P_0 = (0) has height 1 (Theorem 1(c)). Its place is the trivial absolute value, which is the point that connects M(ℤ) (Proposition 2.3). |
| The spectrum is smooth | **Not yet defined in a form that holds.** See (1) and (2) below. **[open]:** a notion of smoothness for G(ℤ) that carries information beyond unique factorization. |
| Smooth ⇒ RH | **Not available.** See the paragraph after the table. **[open]** |

**Why smoothness is not yet defined.**
1. The stalk G(ℤ_(p)) has Krull dimension 2 (the chain {τ} ⊊ {0, τ} ⊊ (p)) and a principal maximal ideal (p) ∪ {τ}. So its dimension exceeds the number of generators of its maximal ideal, which cannot happen in a Noetherian local ring (Theorem 1(f)). The ring-theoretic regularity test "dimension = number of generators of the maximal ideal" therefore does not transfer.
2. The multiplicative skeleton is ℤ_0[M_S] ≅ ℤ × ℤ[M^×] (paper one, Theorem 5.5). Here ℤ[M^×] ≅ ℤ[ε]/(ε² − 1) ⊗ ℤ[x_p : p prime], because M^× ≅ {±1} × (the free commutative monoid on the primes), by unique factorization. So this is unique factorization restated, with the idempotent 0 splitting off one copy of Spec ℤ.

**Why smooth ⇒ RH is not available.** For curves over 𝔽_q, smoothness and properness give RH only through a proof that uses more structure:
- Weil's, via correspondences, recast through Riemann–Roch or Hodge index on C × C (§3.3);
- Stepanov–Bombieri's, via Riemann–Roch on the curve and the Frobenius;
- Deligne's (§3.4(iv)).
- The uploaded Sédillot paper contains no statement about zeta functions or RH; the string "zeta" does not occur in its TeX source. Its trivial-place adjunction (l.1379) is the neutrality of §2.3.
- I have not found an RH-type theorem in the adelic-curve literature.

---

## 6. What would complete the argument

**Theorem E (sufficient condition).** Suppose we are given:
- a real vector space N with a symmetric bilinear form ( , );
- classes e₁, e₂ ∈ N;
- a real-linear map c from real-valued f ∈ C_c^∞(ℝ) to N;

such that:
- **(E1)** (c(f), c(f)) = I(f);
- **(E2)** (e₁, e₁) = (e₂, e₂) = 0, (e₁, e₂) = 1, (c(f), e₁) = a(f) and (c(f), e₂) = b(f);
- **(E3)** (x, x) ≤ 0 for every x ∈ N with (x, e₁) = (x, e₂) = 0.

Then RH holds.

*Proof.* For real f with a(f) = b(f) = 0, c(f) is orthogonal to e₁ and e₂, so I(f) = (c(f), c(f)) ≤ 0. By the real reduction in Theorem C, this gives (3) for all f, and hence RH. ∎

**Remark (the converse is tautological).** Under RH, (E1)–(E3) can be met trivially.
- Take N = C_c^∞(ℝ, ℝ) ⊕ ℝe₁ ⊕ ℝe₂, with c the inclusion.
- Set (f, g) := W_0(f,g) − W(f,g), where W_0(f,g) = a(f)b(g) + b(f)a(g). Give e₁ and e₂ the pairings in (E2).
- Every x ∈ N orthogonal to e₁ and e₂ has the form x = c(f) − b(f)e₁ − a(f)e₂.
- For such x, (x, x) = I(f) − 2a(f)b(f) = −W(f,f) ≤ 0. So Theorem E is an equivalence, and it has content only when N comes from a construction in which (E3) follows from a Riemann–Roch theorem, as in Weil's case.

**What this means.**
- (E3) is the Hodge index inequality. In the Mattuck–Tate form of Weil's proof it follows from Riemann–Roch on C × C together with h⁰ ≥ 0.
- **[inference]** The owner's sub-τ mechanism (§3.4(iii)) is this route.
- **[inference, not proved]** The prime 0 should supply (E2).
  - In the Weil variables its functionals are a(f) = f̂(i/2) and b(f) = f̂(−i/2): the values at s = 0 and s = 1.
  - In the theta variables they are the moment functionals φ(0) and ∫φ, which give the residues −φ(0) and φ̂(0) of Z(φ, s) at s = 0 and s = 1 (§2.2).
  - These are two different spaces of test functions, and no map between them has been constructed that carries one pair of functionals to the other. For the theta image F = x^{1/2}Θφ one finds f̂(γ) = Z(φ, ½ − iγ), so a = Z(φ, 1) and b = Z(φ, 0). On V these values are finite but in general nonzero. So V is *not* the kernel {a = b = 0}.
  - Moreover f̂ vanishes at every zero of ζ on the theta image, because ζ(1 − ρ) = 0. So W ≡ 0 there. This is Connes' point that the zeros live in the cokernel B/ΘV, not on the image.

**[open]** Construct N, as a square over the τ-base with fibre classes e₁ and e₂ given by the prime 0, satisfying (E1)–(E2) and a Riemann–Roch theorem that implies (E3).

**A different route with reality by construction.** Connes–Consani–Moscovici, *Zeta spectral triples*, arXiv:2511.22755, construct self-adjoint rank-one perturbations D − |Dξ⟩⟨δ_N| of the scaling operator on [λ⁻¹, λ]. By their Theorem 1.1, the zeros of the corresponding ξ̂ are real by construction. RH would follow from convergence as N, λ → ∞, which is observed numerically but not proved. Their self-adjointness is with respect to the inner product QW_λ^N − ε_N, so reality by construction rests on a finite-dimensional Weil positivity. **[inference, not checked against their §§2–4]** Their rank-one vector δ_N approximates boundary evaluation, which is structurally parallel to the rank-one idempotent U_0 of the prime 0.

---

## 7. ChatGPT Pro audit, Part A (received 22 September 2026)

- **A1.** Done, including the elementary proof that g̃ is not a Dirichlet-series completion; it is reproduced in Theorem D(iii).
- **A2.** Done. The control density is

  w̃_h(t) = (t² + ¼)²|Γ(¼ + it/2)|²|ζ(½ + it)|² / (2π^{3/2}(t² − γ₁²)²(t² − γ₂²)²).

  It is independent of δ₀ and γ₀: the off-line quartet cancels out of the density, because h = Q_0. Proofs of the two main bounds:
  - **(25)** |Γ(¼ + iy)|² ≤ Γ(¼)²(1 + 4y²)^{−1/4}/cosh(πy).
    - By DLMF 5.8.3 and 4.36.2, |Γ(¼ + iy)|²cosh(πy)/Γ(¼)² = ∏_{k≥0}(1 + y²/(k + ½)²)/(1 + y²/(k + ¼)²).
    - Its logarithm is −Σ_k ∫_{k+¼}^{k+½} ψ_y, where ψ_y(t) = 2y²/(t(t² + y²)) is decreasing.
    - Hence ∫_{k+¼}^{k+½} ψ_y ≥ ¼ψ_y(k + ½) ≥ ¼∫_{k+½}^{k+3/2} ψ_y.
    - Summing over k gives at least ¼∫_{½}^{∞} ψ_y = ¼log(1 + 4y²).
    - With y = t/2 this is Pro's (25). The cruder form follows from 1/cosh x ≤ 2e^{−|x|}.
  - **(29)** |ζ(½ + it)|² ≤ 4(t² + ¼)/(√2 − 1)².
    - For σ > 0, (1 − 2^{1−s})ζ(s) = Σ_{k≥1}((2k−1)^{−s} − (2k)^{−s}).
    - Each term is at most |s|∫_{2k−1}^{2k} x^{−σ−1}dx, so the sum is at most |s|/σ.
    - At σ = ½, |1 − 2^{1−s}| ≥ √2 − 1.
  - `check_pro_A2.py` spot-checks (25), (29), the exact density and its value 2.5977399728·10⁻¹⁴ at t = γ₁. All checks pass.
  - Pro's further bounds (31)–(35) are recorded as Pro's claims; they are not re-derived here.
- **A3, A4 and B1–B3** were not done. Pro reported that it could not read the pinned repository files through its GitHub connection.

---

## 8. Next calculations [recommendations]

1. **The square.** Form the blueprint tensor product B_S ⊗_{𝔽_{1,τ}} B_S in Lorscheid's framework. Compute its prime spectrum and its height-one primes. Test whether 0⊗1 and 1⊗0 give two fibre divisors meeting in one point. This is the data (E2), and the first test of whether (E1)–(E3) can exist.
2. **The packet split.** Compute W_0, A and P on the programme's quartet packet {P·v_h : deg P ≤ 3} as 4×4 matrices in (δ, γ), separated into the prime 0 and the rest. This measures the packet's Castelnuovo–Severi margin.
3. **The complete τ-base complex.** Write the τ-base complex with the prime 0 included: Θ_S, with 𝓛₀ and 𝓛₁ as H⁰ and H² classes. Check whether its Euler characteristic reproduces W_0 as a trace.

## 9. Provenance and external theorems

- **Proved here:**
  - Theorem 1;
  - Lemma 2.1;
  - Propositions 2.2 (after Riemann and Tate) and 2.3;
  - Proposition 3.1(ii)–(iii); 3.1(i) is a definition, justified by Proposition 2.2;
  - Theorems C, D and E;
  - §3.4(i)–(ii);
  - the proofs of Pro's (25) and (29).
- **External results used:**
  - Ostrowski (1916);
  - Berkovich (1990), Example 1.4.1 (as cited in Baker's 2007 AWS notes), with Poineau's exposition;
  - Krull's principal ideal theorem (Matsumura, Theorem 13.5);
  - Poisson summation;
  - Riemann (1859) and Titchmarsh §2.6;
  - Tate (1950): Theorem 4.2.1 and Main Theorem 4.4.1;
  - Weil (1948) and Weil (1952);
  - Bombieri (2000);
  - Mattuck–Tate (1958) and Grothendieck (1958);
  - Stepanov (1969) and Bombieri (1973);
  - Hartshorne V.1.9 and Exercises 1.9–1.10;
  - Deligne (1974), §3;
  - Soulé (2004), via Connes–Consani (2010), eq. (3);
  - DLMF 5.8.3 and 4.36.2;
  - van de Lune–te Riele–Winter (1986);
  - Connes–Consani–Moscovici (2025), Theorem 1.1 as stated in their abstract and introduction.
- **Not claimed:** no proof of RH. Theorem C is a reformulation equivalent to RH. Theorem E is a sufficient condition whose hypotheses are not constructed.
