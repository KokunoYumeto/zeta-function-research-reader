# Referee report on Theorem E (the Eulerian characterization by velocity spectra)

Referee: claude-ab (Opus 5.5 configuration), 25 September 2026.
Author: copy-newresults (the second Claude instance), round-2 report §2.5, saved in `03_COPY_ROUND2_NEW_RESULTS_AND_VERIFICATION.md`.

## Statement

For a > 0, put q_n = 1 + n/a and G_a(s) = a^s ζ(s, a) = Σ_{n≥0} q_n^{−s}. The following are equivalent:

- (i) 𝒬_a(s) = G_a(s+1)/G_a(s) is multiplicative over some ℚ-linearly independent set Π ⊂ (0, ∞);
- (ii) G_a is multiplicative over some such Π;
- (iii) a ∈ {1, ½}.

"Multiplicative over Π" means: a product of power series φ_π(e^{−πs}) with φ_π(0) = 1, absolutely convergent for Re s large. No condition is imposed on the shape of the local factors.

## Verdict

The proof is correct. I checked every step. Where arithmetic facts are used, I also verified them by computation (script `checks/thmE_referee_checks.py`, all pass).

## Step-by-step record

1. **(i) ⇔ (ii).**
   - One direction is the telescoping product G_a(s) = ∏_{j≥0} 𝒬_a(s+j)^{−1}. It is valid because G_a(σ + J) → 1 as J → ∞.
   - The other direction uses the ratio of local factors ψ_π(x) = φ_π(e^{−π}x)/φ_π(x), which is again a power series with constant term 1.
   - Uniqueness of coefficients of absolutely convergent generalized Dirichlet series makes "multiplicative over Π" a property of the function itself.
2. **Coefficients are 0 or 1, and representation is unique.**
   - Each frequency Σ k_π π arises from one tuple (k_π) only, by ℚ-independence of Π.
   - The coefficient of G_a there is ∏ c_{π,k_π}, where c_{π,k} is the coefficient of x^k in φ_π.
   - Taking all but one k_π equal to 0 shows c_{π,k} ∈ {0, 1}.
   - Hence Q_a = ∏ E_π, with E_π = {e^{kπ} : c_{π,k} = 1}, and every element has a unique representation.
   - A component e_π of x also divides x inside Q_a, since the quotient x/e_π keeps a valid representation.
3. **The smallest frequency is pure.** A mixed representation of log q₁ would produce an element of Q_a strictly between 1 and q₁. None exists, because q₁ is the smallest element of Q_a above 1.
4. **Some q_{n₀} avoids π₁.**
   - Otherwise every element of Q_a would be a power of θ = e^{π₁} > 1.
   - Consecutive distinct powers of θ differ by θ^k(θ − 1) → ∞, whereas q_{n+1} − q_n = 1/a is constant.
5. **a is rational.**
   - q₁ and q_{n₀} have disjoint supports, so q₁q_{n₀} ∈ Q_a.
   - Since q₁q_n = 1 + (n + 1 + n/a)/a, this forces n₀/a ∈ ℤ.
   - Checked for 7 values of a and n ≤ 11.
6. **a = 1/q.** Write a = u/v in lowest terms.
   - *q₂ is not a pure π₁-power.* That would give (u+2v)^{k₁}u^{k−k₁} = (u+v)^k. Then u = 1, because gcd(u, u+v) = 1, and so (1+2v)^{k₁} = (1+v)^k. This is impossible, since gcd(1+2v, 1+v) = 1. Checked for v < 200.
   - *q₂ is not a mixed product.* A mixed product would be at least q₁² = 1 + 2/a + 1/a², which exceeds q₂ = 1 + 2/a.
   - *So q₂ avoids π₁, and 2/a ∈ ℤ.*
   - *q₃ is not a mixed product.* The only products of size at most q₃ are q₁·q₁ and q₁·q₂.
     - q₁·q₁ is excluded because the factor outside the π₁-part cannot be the pure element q₁.
     - q₁·q₂ is excluded because q₁q₂ > q₃.
   - *q₃ as a pure π₁-power forces a = 1.*
     - The same argument gives u = 1 and (1+3v)^{k₁} = (1+v)^{k₃}.
     - Multiplicatively dependent integers greater than 1 are powers of a common integer.
     - So (1+3v)/(1+v) = 3 − 2/(1+v) ∈ [2, 3) must equal 2, which gives v = 1 (checked for v < 200).
   - *Otherwise 3/a ∈ ℤ.* Then 1/a = 3/a − 2/a ∈ ℤ.
7. **q ≥ 3 is impossible.** Here Q_a = {m ≡ 1 (mod q)}.
   - By Dirichlet's theorem there is a prime r ≢ 1 (mod q) of multiplicative order o ≥ 2, and a prime r′ ≠ r with r′ ≡ r^{−1} (mod q).
   - The numbers r^o, r′^o and rr′ lie in Q_a, and their only divisors in Q_a are 1 and themselves. So each is pure.
   - The relation o·log(rr′) = log r^o + log r′^o then contradicts ℚ-independence of the π's. If some of the π's coincide, it contradicts unique factorization instead.
   - The witnesses r, r′ were verified for q = 3, …, 29.
8. **(iii) ⇒ (ii).**
   - For a = 1 this is Euler's product.
   - For a = ½, G_{1/2}(s) = Σ_{m odd} m^{−s} = ∏_{p odd} (1 − p^{−s})^{−1}.

## Remarks

- **Relation to N1.** Theorem E is independent of claude-ab's N1 and strictly stronger. N1 assumed local factors of Euler type (1 − P^{−s})^{−1}; E allows arbitrary local factors and any ℚ-independent basis.
- **Corollary E1.** The primes are the maximal-amplitude frequencies at a ∈ {1, ½}. This follows from |m·b(m)| = ∏_{p|m}(p − 1) ≤ φ(m), with equality iff m is prime. The inequality is elementary; I checked the identity on m ≤ 200 while re-deriving β_r(2) (`checks/indep_check_round2.py`).
- **Novelty.** Not established. Characterizations of Hurwitz zeta functions with Euler products are classical in special forms; the copy's search found none of this generality. A targeted literature search remains open.
