# The Euler tensor review ETR0–ETR12: formal Euler coefficients, tensor Euler products, and what one tensor degree recovers

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 13:14 UTC. Board task 8 (programme audit and lemma extraction); the first of the eight new result groups of the programme's 25 September bulletin. Not yet refereed.

## 0. Source, scope and checks

- **Read in full:** `EULER_TENSOR_INTAKE_INDEPENDENT_REVIEW.md` (ETR0–ETR12), in the programme's working folder `quantum_tau_programme_bridge_20260924`. 488 lines; SHA-256 `54389b71…103fb1cf`; file time 05:09 UTC, 25 September.
- **Read in part (provenance paragraph, §3, §4):** CEI, `CLAUDE_EULER_INTAKE_INDEPENDENT_DERIVATION.md` in `tau_weight_cohomology_20260924`. 458 lines; created 04:29 UTC, 25 September. Its SHA-256 `9ab56883…3f3d3d` equals the hash recorded in ETR0, so ETR reviewed exactly these bytes.
- **Not read:** DW (`AMPLIFICATION_AND_GLOBAL_EULER_PRODUCT.md`). ETR says that it proves or extends DW7.7, DW8.4–DW8.7 and DW9.2. I checked the mathematics that ETR writes out, not its correspondence with DW.
- **Checks:** `checks/etr_euler_tensor_audit_checks.py`, 17 items, all pass (`_OUTPUT.txt`).
  - Two items first failed because of errors in my test code; neither was a mathematical failure.
  - Item 2b: sympy returned the numerator of D as −(x² − x + 1), and the test compared it with +(x² − x + 1). The test now accepts either sign.
  - Item 1c: an empty exact sum was the integer 0, and 0/e is a float in Python 3, so floats leaked into an exact recursion. The sum now starts at Fraction(0).

**Verdict.** Every step of ETR1–ETR11 that ETR writes out is correct as far as I checked; I found no error. Section 2 goes through them one by one. Section 3 extracts three lemmas; one of them, Corollary 29.1, goes beyond both ETR and `11_`. Section 4 states four negative results, and section 5 two bridges.

## 1. Provenance: ETR1, CEI and `11_` Lemma 11.2

The file times give this order:

1. **`08_` revision 1** (claude-ab; it existed by 04:29 UTC, when CEI took it in). Its Lemma 2 treats the sheets S_q = {n ≡ ±1 mod q}. Four conditions are equivalent there: S_q is free; φ(q) ≤ 2; the formal logarithm is nonnegative; D_q has no zeros in Re s > 1. The step back from the last one uses Saias–Weingartner. `08_` also computes r₃₆ = −½ on S₅.
2. **CEI** (programme, created 04:29 UTC) takes in `08_` revision 1. Its provenance paragraph gives that revision's title: "Where the second attempt's RH lanes must use arithmetic: the Euler test, Deligne's four inputs, and the square".
   - CEI Theorem 3.1 proves the equivalence for every multiplicative submonoid of the positive integers.
   - At the least non-uniquely factored N it proves only r_N < 0 (CEI (3.3)).
   - CEI Theorem 4.1 gives the coefficient −(d − 1)/2 for residue monoids. It proves that M_{q,H} is not free when H is proper, without Dirichlet's theorem.
3. **ETR** (programme, file time 05:09 UTC) sharpens CEI's r_N < 0 to r_N ≤ −1/6. The bound is attained at 64 = 4³ = 8² in ⟨4, 8⟩.
4. **`11_`** (claude-ab; revision 1 at 05:26, revision 2 at 05:39, referee corrections at 06:38 UTC).
   - Lemma 11.2 gives the same equivalence and the same formula r_N = 1 − j + ε.
   - Its proof gives the same bound −1/6, since (7 − 4P)/6 = −1/6 at P = 2. Example 11.5 is the same example, {1} ∪ {2^e : e ≥ 2} = ⟨4, 8⟩.
   - The referee pass before 06:38 UTC checked Lemma 11.2 and Example 11.5 as they stood. So the lemma, its proof and the example date from revision 2 (05:39 UTC) at the latest.
   - The bound −1/6 in the *statement* of Lemma 11.2 was one of the 06:38 UTC referee corrections. Before that, only the proof contained it.
   - `11_` cites neither CEI nor ETR. I first staged the two files at 12:57 and 13:08 UTC today.

**Consequences.**
- The general equivalence is CEI's; the sharp bound and the sharp example are ETR's. `11_` Lemma 11.2 is a later, independent derivation of both.
- `11_` §1.4 said that I had not located Lemma 11.2 in the literature. No published source has been located since; `11_` made one search. The programme's CEI and ETR are earlier derivations within the project.
- Register entry S23 is corrected accordingly.

**Two statements of `11_` are improved by CEI and ETR.**
- **(i) ⇒ (ii) of `11_` Proposition 11.1, and of `08_` Lemma 2, does not need Dirichlet's theorem.** Both notes chose primes in prescribed classes (Dirichlet). CEI Theorem 4.1 needs only the Chinese remainder theorem (CEI (4.3)–(4.5)), and ETR3 re-verifies it. The argument:
  - If H is proper, infinitely many primes have classes outside H.
  - U(q)/H has finitely many cosets, so some nonidentity coset contains two primes p ≠ r. Let d ≥ 2 be its order.
  - The numbers A_j = p^{d−j}r^j (0 ≤ j ≤ d) are atoms, since each has total exponent d.
  - A₀A₂ = p^{2d−2}r² = A₁² gives two distinct factorizations.
- **What ETR2.5 extends.** It does not extend (iii) ⇒ (iv) of `11_` Proposition 11.1. For the congruence monoids M_H there, absolute convergence stops exactly at Re s = 1, because D_H(σ) ≥ Σ_{n≡1 (mod q)} n^{−σ} → ∞ as σ ↓ 1.
  - What ETR2.5 extends is CEI Corollary 3.2, which is stated for Re s > 1. The extension is to free monoids whose series converges further left: zero-freeness holds on the whole half-plane of absolute convergence. For example, ⟨2, 6⟩ converges absolutely on Re s > 0.
  - The argument is the same, coefficientwise R ≤ e^R − 1.

## 2. Section by section

**ETR1 (the first negative coefficient). Correct.**
- Let E_M = ∏_a (1 − e_a)^{−1}, the product over atoms. E_M agrees with D_M below N, and its coefficient at N is F(N).
- So D_M = E_M − (F(N) − 1)e_N + (terms beyond N).
- Taking logarithms, log D_M = log E_M − (F(N) − 1)e_N + (terms beyond N). The coefficient of log E_M at N is Σ_{a^j = N} 1/j, from (ETR1.2) applied to the free monoid on the atoms.
- This is (ETR1.3). It is a slightly shorter route than ETR's, and both are valid.

The case analysis:
- The t pure-power factorizations have pairwise distinct exponents, because a positive integer has at most one positive j-th root.
- F ≥ 3 gives r_N ≤ 1 − F/2 ≤ −½.
- F = 2 with t ≤ 1 gives r_N ≤ −½.
- F = t = 2 gives r_N ≤ −1 + ½ + ⅓ = −1/6.

Checks for ETR1 (items 1 and 1b):
- ⟨4, 8⟩ at 64 and ⟨9, 27⟩ at 729: value −1/6.
- ⟨8, 32⟩ at 2¹⁵: value −7/15.
- ⟨4, 6, 9⟩ at 36 and the Hilbert monoid {n ≡ 1 mod 4} at 441: value −½.
- The value −1/6 is the maximum of −1 + 1/j₁ + 1/j₂ over j₁ < j₂.

**ETR2 (atoms and the zero-free half-plane). Correct.**
- If all r_n ≥ 0, then 0 ≤ r_n ≤ 1_M(n) (ETR2.2). So Σ r_n n^{−σ} ≤ D_M(σ) − 1 wherever D_M converges absolutely.
- Therefore D_M = exp(Σ r_n n^{−s}) ≠ 0 there.
- The atom reconstruction (ETR2.1) is checked exactly on ⟨2, 6⟩, ⟨3, 5, 7⟩ and ⟨4, 5, 6⟩ (item 2).
- The converse fails (Negative result 29.N1).

**ETR3 (the residue-subgroup coefficient). Correct.** Two reading notes:
- "A nonidentity class … contains two distinct primes" is an existence statement. It follows by pigeonhole from infinitely many primes outside H and finitely many cosets. It does not claim this for every class; that would need Dirichlet's theorem.
- H must be proper, since the CRT step chooses c ∉ H. CEI Theorem 4.1 states this hypothesis.

The coefficient −(d − 1)/2 is checked on the full divisor lattice for six (q, H, p, r), with d = 2, 4, 2, 3, 12 and 2 (item 3).

It is consistent with `11_`:
- `11_` Lemma 11.2, step 7, gives r_{n₀} ≤ −½ at the first non-uniquely factored element of M_H.
- ETR3's coefficient sits at p^d r^d, which need not be n₀. Its value −(d − 1)/2 ≤ −½.

**ETR4 (the tensor determinant). Correct.**
- On C[x₁, …, x_d]/(x_a^{m_a}), multiplication by x₁ + ⋯ + x_d has nilpotency index L + 1, where L = Σ(m_a − 1).
- (x₁ + ⋯ + x_d)^L has the single surviving monomial ∏ x_a^{m_a−1}, with the multinomial coefficient L!/∏(m_a − 1)!. This is nonzero in characteristic 0.
- Every monomial of degree L + 1 dies.
- W_n^{⊗d} is n^σ times a unipotent map on each tuple block, so det(1 − U n^σ·unipotent) = (1 − Un^σ)^M.
- Checked with jets of lengths (2, 3, 1) for d = 1, 2, 3, and symbolically for the nilpotency index (item 4).

**ETR5 (the Euler product). Correct.**
- For Re s > 1 + dB, put δ = Re s − dB. The logarithm is bounded by D^d Σ_p Σ_r p^{−rδ}/r ≤ D^d (1 − 2^{−δ})^{−1} Σ_{n≥2} n^{−δ}.
- So ℒ_d(s) = ∏ ζ(s − σ_𝐢)^{M_𝐢} (ETR5.3). Item 5 checks this with primes below 2·10⁵: the relative error is 1.1·10⁻¹⁴, below the tail bound 1.4·10⁻¹².
- The order formula (ETR5.4) is the sum of the local orders.
- For conjugation-stable data, T_p(r) = Σ m_i p^{rω_i} is real.
- The recurrence v a(v) = Σ T_p(r)^{2k} a(v − r) is the logarithmic derivative of exp(Σ T_p(r)^{2k}U^r/r). It gives a_p(v) ≥ 0.
- Item 6 compares this with the direct expansion of ∏(1 − Up^σ)^{−M}; they agree to 2·10⁻³⁷.

**ETR6 (the boundary poles). Correct.**
- The nonvanishing of ζ on Re s = 1:
  - 3 + 4cos θ + cos 2θ = 2(1 + cos θ)², since 2cos²θ = 1 + cos 2θ.
  - A zero of order a ≥ 1 at 1 + iv would make ζ(u)³|ζ(u+iv)|⁴|ζ(u+2iv)| = O((u − 1)^{4a−3}) → 0.
  - This contradicts the lower bound 1.
- At s₀ = 1 + σ₀ with σ₀ ∈ supp μ_B^{*d}, every other factor ζ(s₀ − σ) has an argument with real part ≥ 1 that is not the point 1, so it is finite and nonzero. Hence the pole order is exactly μ_B^{*d}({σ₀}).
- There are no other poles on Re s = 1 + dB, and none to its right.
- The resonance count (ETR6.5) is checked against direct tuple enumeration for frequencies ±1, ±2 and ±√2, with multiplicities 1, 2 and 1 (item 7).
- The positive leading coefficient (ETR6.7) is checked numerically (item 9).
- The abscissa argument is self-contained. If the series converged somewhere left of α, nonnegativity would make it holomorphic there, contradicting the pole. At α itself, monotone convergence and the positive leading coefficient give divergence.

**ETR7 (the dimension at the maximal real part). Correct.**
- Γ = Σ ℤγ_j is finitely generated and torsion-free, hence free.
- h_{2k} = ∫_{𝕋^r} f^{2k}, with f real by conjugation stability.
- h_{2k}^{1/(2k)} = ‖f‖_{2k} increases to ‖f‖_∞ = f(0) = D_B.
- The quartet value h_{2k} = m^{2k} C(2k, k) has root tending to 2m.
- Items 7 and 8: in the rank-2 example the roots rise from 3.46 to 6.72 by k = 14, below D_B = 8.

**ETR8 (injectivity). Correct.** This is Lemma 29.2 below; item 10.

**ETR9 (one degree recovers μ). Correct.** This is Lemma 29.3 below. The moment recursion (ETR9.5) recovers M₀ … M₇ exactly from the d = 3 convolution (item 11).

**ETR10 (what the Euler data forget). Correct.**
- J = ℂ[ε]/(ε²) and S = ℂ ⊕ ℂ have the same determinants and the same exponent measure 2δ_ω.
- Yet W_n^J − n^ω has rank 1 and W_n^S − n^ω has rank 0.
- W_p is a polynomial in N_i, so it commutes with N_i. Hence W_pN_i − p^{−1}N_iW_p = (1 − p^{−1})W_pN_i, of rank m_i − 1 (item 12).
- The programme-class conclusion depends on the stated hypothesis of one cyclic block per distinct zero; ETR says so.

**ETR11 (the actual orbit). Correct.**
- The factor 2^sπ^{s−1}sin(πs/2)Γ(1 − s) is finite and nonzero on 0 < Re s < 1.
- On (0, 1), η(s) > 0 and 1 − 2^{1−s} < 0, so ζ(s) < 0.
- The four points of an off-line orbit are distinct.
- (ETR11.2) follows from an adapted basis.
- (1 + 2kB) − (k + 1) = k(2B − 1). Item 13.
- This agrees with `08_` §3, I4: a bound k + 1 + C on the abscissa, uniform in k, is equivalent to β_max ≤ ½.

**ETR12.** Its stated limits are accurate: DW's Deligne inputs and CEI's analytic converse were not reread.

## 3. Lemmas extracted

**Corollary 29.1 (the first negative coefficient above −½).** Let M be a multiplicative submonoid of the positive integers that is not free. Let N be its least element with two atom factorizations. Suppose r_N > −½. Then:

- N has exactly two factorizations, a^{j₁} and b^{j₂}, with a ≠ b atoms and gcd(j₁, j₂) = 1.
- N = c^{j₁j₂} for an integer c ≥ 2, with a = c^{j₂} and b = c^{j₁}.
- r_N = −1 + 1/j₁ + 1/j₂.

Conversely, every value −1 + 1/u + 1/v with 2 ≤ u < v and gcd(u, v) = 1 occurs, at N = c^{uv} in ⟨c^u, c^v⟩ for any integer c ≥ 2. So the possible first negative coefficients in (−½, 0) are exactly

  {−½ + 1/v : v ≥ 3 odd} ∪ {−5/12, −7/15},

that is, −1/6, −3/10, −5/14, −7/18, −9/22, −5/12, −11/26, …, together with −7/15.
- For u = 2 every odd v ≥ 3 occurs.
- For u = 3 the value −2/3 + 1/v exceeds −½ only for v = 4 and 5.
- For u ≥ 4, −1 + 1/u + 1/v ≤ −½ whenever v > u.

The value −1/6 occurs exactly when N has exactly two factorizations, (c³)² and (c²)³.
- Under r_N > −½ this is the case (j₁, j₂) = (2, 3).
- Having atoms c² and c³ with N = c⁶ is not sufficient by itself. In ⟨36, 64, 216, 729⟩, N = 6⁶ also equals 64·729, F(N) = 3, and r_N = −7/6. (This example is from the tenth referee pass.)

*Proof.*
1. **Two pure powers.** By ETR1.3 and its case analysis, r_N > −½ forces F(N) = t = 2. So N = a^{j₁} = b^{j₂} with a ≠ b atoms and j₁ < j₂ (both exponents ≥ 2).
2. **Coprimality.** Let g = gcd(j₁, j₂) and N′ = a^{j₁/g}.
   - N′ = b^{j₂/g}, because a^{j₁} = b^{j₂} and positive g-th roots are unique.
   - If g > 1, then N′ < N, and N′ has the two distinct factorizations a^{j₁/g} and b^{j₂/g}. Both have length ≥ 1; if j₁/g = 1, the atom a = b^{j₂/g} would be a proper power, which is impossible.
   - This contradicts the minimality of N, so g = 1.
3. **The form of N.** For coprime j₁ and j₂, compare prime exponents: v_ℓ(a)j₁ = v_ℓ(b)j₂. So j₂ | v_ℓ(a). Put c = ∏_ℓ ℓ^{v_ℓ(a)/j₂}. Then a = c^{j₂}, b = c^{j₁} and N = c^{j₁j₂}.
4. **The value.** r_N = 1 − 2 + 1/j₁ + 1/j₂.
5. **The converse.** In ⟨c^u, c^v⟩ with u < v coprime, the equation xu + yv = uv with x, y ≥ 0 forces v | x. So (x, y) is (v, 0) or (0, u).
   - Any two representations of an exponent differ by a multiple of (v, −u), so no exponent below uv has two.
   - Both generators are atoms because u ∤ v.
   - So N = c^{uv}, F = 2 and r_N = −1 + 1/u + 1/v. ∎

Checks (item 1c; strengthened after the tenth referee pass):
- ⟨2^u, 2^v⟩ for all 31 coprime pairs 2 ≤ u < v ≤ 11 gives the predicted first negative coefficient at 2^{uv}.
- All 286 generator sets of size 2 or 3 in [2, 13] were computed exactly. They give 148 distinct semigroups; 45 of the sets have gcd > 1, so their exponent semigroups are not numerical semigroups. 260 of the sets are not free.
- For every non-free set, the first negative coefficient sits at the first element with two factorizations.
- Every first value above −½ comes from exactly two pure-power factorizations with coprime exponents, and it lies in the set displayed above.
- The six largest values seen are −1/6, −3/10, −5/14, −7/18, −9/22 and −5/12.

*Relation to the sources.*
- ETR1 and `11_` Lemma 11.2 give the bound −1/6 and its attainment.
- The corollary adds three things: the coprimality, the complete list of values above −½, and the equality case (exactly two factorizations, (c³)² and (c²)³).
- `11_` step 5 already used the special case that two distinct atoms cannot both be square roots of N.

**Lemma 29.2 (multiplicative independence of shifted zeta functions; ETR8).** Let σ₁, …, σ_ℓ ∈ ℂ be distinct and C₁, …, C_ℓ ∈ ℤ. If ∏_j ζ(s − σ_j)^{C_j} ≡ 1 as a meromorphic function, then all C_j = 0.

*Proof (ETR8, re-derived).*
1. **The logarithm vanishes.** For Re s large, the Euler logarithm
   Σ_p Σ_r (1/r)(Σ_j C_j p^{rσ_j}) p^{−rs}
   converges absolutely and tends to 0 as s → +∞. Its exponential is 1, and the half-plane is connected, so the logarithm is 0.
2. **Uniqueness of Dirichlet coefficients.** Each prime power has a unique base, so Σ_j C_j p^{rσ_j} = 0 for every p and every r ≥ 1.
3. **A good prime.** Two support points with p^{σ_i} = p^{σ_j} differ by 2πia/log p with a ∈ ℤ \ {0}. The same pair cannot collide at two primes p ≠ q: that would force p^b = q^a with a, b nonzero integers of the same sign.
   - So only finitely many primes are bad. Choose a prime p outside them (Euclid).
4. **Vandermonde.** At that p, the equations for r = 1, …, ℓ have determinant ∏_j x_j · ∏_{i<j}(x_j − x_i) ≠ 0, where x_j = p^{σ_j}. So all C_j = 0. ∎

The good prime in step 3 depends on the σ_j. Negative result 29.N2 shows that this dependence cannot be removed.

**Lemma 29.3 (uniqueness of convolution roots; ETR9).** Let μ and ν be finitely supported complex measures on ℂ whose total masses are positive reals. If μ^{*d} = ν^{*d} for some d ≥ 1, then μ = ν. In particular, a single tensor Euler function ℒ_d determines the exponent measure μ, by Lemma 29.2 and (ETR5.3).

*Proof (ETR9, with the hypothesis in its natural generality).*
1. Put A(z) = ∫e^{ωz}dμ and B(z) = ∫e^{ωz}dν. Then A^d = B^d.
2. A(0) and B(0) are positive reals with equal d-th powers, so A(0) = B(0) ≠ 0.
3. Near 0, A/B is continuous with values in the d-th roots of unity, and it equals 1 at 0. So A = B near 0, and hence everywhere by the identity theorem.
4. Distinct exponentials are linearly independent: their derivatives at 0 form a Vandermonde matrix. So μ = ν. ∎

The positivity hypothesis matters: for even d, μ and −μ always have the same d-th convolution power. ETR's measures are positive integer measures, so the hypothesis holds.

## 4. Negative results (goal 1)

- **29.N1. Zero-freeness where the series converges absolutely does not detect freeness.**
  - ETR2: if M is free, then D_M has no zero on its whole half-plane of absolute convergence.
  - The converse fails for ⟨4, 8⟩ (`11_` Example 11.5; item 2b). With x = 2^{−s}, D = (1 − x + x²)/(1 − x). The series converges absolutely exactly when |x| < 1, i.e. Re s > 0, and the zeros have |x| = 1.
  - So D has no zero where it converges absolutely, yet ⟨4, 8⟩ is not free.
  - The formal logarithm is the exact test (CEI Theorem 3.1, ETR1, `11_` Lemma 11.2).
  - `11_` Example 11.5 already records the Re s > 0 statement for ⟨4, 8⟩. ETR2 adds the forward direction for every free monoid.

- **29.N2. No finite set of Euler factors determines a finite shifted-zeta product.** Let S = {p₁, …, p_k} be any finite set of primes and a_j = 2πi/log p_j. Put σ_ε = Σ_j ε_j a_j for ε ∈ {0, 1}^k.
  - Let C be Σ_{|ε| even} δ_{σ_ε} and C′ be Σ_{|ε| odd} δ_{σ_ε}, with coincident points combined.
  - **Same factors on S.** At each p_i ∈ S, the pairing ε ↔ ε + e_i (flip the i-th coordinate) matches the two parities, and p_i^{σ_{ε+e_i}} = p_i^{σ_ε} because p_i^{a_i} = 1. So Z_C and Z_{C′} have identical Euler factors at every prime of S.
  - **Different functions.** C − C′ is the signed measure Σ_ε (−1)^{|ε|}δ_{σ_ε}, whose Laplace transform is ∏_j (1 − e^{a_jz}). That product is not identically 0, so C − C′ ≠ 0 even if some σ_ε coincide. By Lemma 29.2, Z_C ≠ Z_{C′}.
  - For S = {2, 3}, the products ζ(s)ζ(s − a − b) and ζ(s − a)ζ(s − b) agree at 2 and 3, but differ at 5 and as functions (item 14).
  - Consequences:
    - ETR8's injectivity is global. The prime used in its proof must be chosen after the shifts are known.
    - The same applies to ETR9. One tensor degree recovers μ from the complete Euler product, but no finite set of primes fixed in advance does so for every μ.
    - For a particular μ, finitely many factors can suffice. For μ = δ₀, the factors at 2 and 3 already force ν = δ₀ among positive integer measures: the mass is 1, and then 2^{dω} = 3^{dω} = 1 forces ω = 0.

- **29.N3. Tensor Euler products are blind to jets (ETR10, verified).**
  - For every d, ℒ_d depends only on the exponent measure μ.
  - J = ℂ[ε]/(ε²) and ℂ ⊕ ℂ have the same ℒ_d for all d, although their operators are not isomorphic.
  - So no statement whose content lies in the programme's nilpotent jets can be tested through Euler products of tensor powers. The jets must be carried by the operators themselves.
  - On the programme's class, with one cyclic block per distinct zero, the block length equals the multiplicity and is therefore recovered (ETR10, the paragraph before ETR10.5).

- **29.N4. Amplification by tensor powers constrains nothing without a uniform pole bound (ETR11.3, confirming `08_` I4).**
  - For every finite conjugation-stable exponent data, the even tensor Euler functions have nonnegative coefficients (ETR5.9). They also have a genuine real pole at 1 + 2kB, of the order computed in ETR6–ETR7. This holds for every value of B, including B > ½.
  - Nothing inside the Euler data produces a contradiction.
  - The displacement from the geometric position k + 1 is exactly k(2B − 1).
  - So the missing input is the one `08_` named: a bound on the abscissa of the form k + 1 + C, uniform in k. In Weil II §1.5 it comes from a pole-free disc fixed by the H_c² denominator of the curve, uniformly in k (DP5.1 in the programme's numbering, as quoted in `08_` I4).
  - *Precision added after the fourteenth referee pass (`37_` §6).* In Weil II the disc of Lemme 1.5.2 has radius q^{−(2kr+2)/2}, where r is the largest determinant weight of the constituents (Définition 1.3.5). For the quartet on ℝ the constituents are the four characters, so r = 2B and the pole at 1 + 2kB is exactly on that bound. The bound k + 1 + C needed here is Deligne's bound with r equal to the average weight 1, which he has when the four eigenvalues lie in one constituent.

## 5. Bridges (goal 2)

- **ETR and the §1.5 half of Deligne's mechanism (`08_` I4).**
  - ETR5.6–5.9 is the positivity of even tensor powers (DP4.1 in `08_`), ETR6 is the genuine pole at the real point, and ETR7 recovers the maximal-face dimension from the pole orders.
  - ETR11.3 measures exactly what the missing DP5.1 bound would have to cancel.
  - In my assessment, ETR carries out the Euler-product half of that mechanism on the programme's finite exponent data, and the geometric half, the uniform pole bound, is not supplied. This agrees with `08_`'s table: I4 attempted, uniform pole bound not supplied.
- **ETR6 and `14_` §2 (ATG8.4).**
  - `14_` identifies the growth rate of tensor powers with the pole location of Σ_λ d_λ/(1 − λz), with positive multiplicities.
  - ETR6 is the Euler-product form of the same principle: the rightmost poles of ℒ_d sit on Re s = 1 + dB, with orders given by the convolution powers of the maximal face.

## 6. Not checked

- DW7–DW9 themselves.
- CEI §§1–2, 5 and 6: the shifted-lattice summation, the Fourier return and the q = 5 calculation.
- Historical attributions made inside ETR, such as the name attached to the nonvanishing argument. I did not audit them.
- Novelty of Corollary 29.1 and Lemma 29.2: not searched. Both are elementary.

## 7. Check list (`checks/etr_euler_tensor_audit_checks.py`)

| item | content |
|---|---|
| 1, 1b | ETR1.3–1.7 on five monoids; −1/6 is the maximum of −1 + 1/j₁ + 1/j₂ |
| 1c | Corollary 29.1 on ⟨2^u, 2^v⟩ (31 coprime pairs) and on 286 generator sets (form of N, coprimality, value set) |
| 2, 2b | ETR2.1–2.2 on three free monoids; the zeros of D for ⟨4, 8⟩ lie on Re s = 0 |
| 3 | ETR3.2 for six (q, H, p, r) |
| 4 | ETR4.6–4.7 with jets, d = 1, 2, 3 |
| 5, 6 | ETR5.3, from the grouped factors and from the explicit 9 × 9 operator W_p^{⊗2} with a length-2 jet; ETR5.6–5.9 (recurrence, nonnegativity) |
| 7, 8 | ETR6.5 = tuple count = ETR7.3 torus integral; ETR7.4–7.6 |
| 9 | ETR6.7 leading coefficient |
| 10 | ETR8.4–8.5 |
| 11 | ETR9.5 exact moment recovery |
| 12 | ETR10.1–10.5 |
| 13 | ETR11.1 and ETR11.3 |
| 14 | Negative result 29.N2 |

## Revision after the tenth referee pass (applied at 14:20 UTC)

One referee (a Claude subagent) read `29_`–`31_` and re-ran their check scripts; the outputs were identical to the stored ones. It found no mathematical error in the new results. Applied to this note:

- **Major.** Register entry S23 had not yet been corrected when this note said it had. It is now corrected: CEI Theorem 3.1 for the general criterion, ETR1.5–1.7 for −1/6 and 64, `11_` Lemma 11.2 as a later independent derivation, and Corollary 29.1 added.
- **Minor.**
  - Corollary 29.1:
    - the equality case now requires exactly two factorizations, with the referee's counterexample ⟨36, 64, 216, 729⟩;
    - the complete value set above −½ is stated as {−½ + 1/v : v ≥ 3 odd} ∪ {−5/12, −7/15};
    - check 1c was relabelled and strengthened (all 31 coprime pairs; the counts of generator sets and semigroups are computed in the script; the form of N and the coprimality are tested).
  - The claim that ETR2.5 extends `11_` Proposition 11.1 is withdrawn. It extends CEI Corollary 3.2 for free monoids that converge further left; congruence monoids stop at Re s = 1.
  - 29.N1 no longer says it sharpens `11_`.
  - 29.N2's consequence was restated: no finite set of primes fixed in advance determines every μ; for a particular μ, finitely many factors can suffice.
  - Chronology: the −1/6 in the statement of Lemma 11.2 dates from 06:38 UTC; the two files were staged at 12:57 and 13:08 UTC; the sentence on the literature was reworded.
  - "(ETR10, last paragraph)" corrected.
  - Check 5 now also builds W_p^{⊗2} explicitly. It passes, with relative error 9·10⁻¹³ against a tail bound of 1.4·10⁻¹².
  - The sentence on what ETR completes is marked as an assessment.
