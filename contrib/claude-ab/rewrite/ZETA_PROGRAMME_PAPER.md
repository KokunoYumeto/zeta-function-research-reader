# The split-zero programme around the Riemann zeta function: an audited record of its results, with proofs

*Claude (Anthropic, model `claude-opus-5-5`), 27 September 2026. Published at the author's request ahead of the author's review; the author may revise or withdraw it. This record replaces the zeta reader (Zenodo 10.5281/zenodo.22970703 and 10.5281/zenodo.22977243) and the audit notes 01\_–49\_, which were withdrawn on 27 September 2026.*

## Abstract

The split-zero programme of KokunoYumeto studies the nontrivial zeros of the Riemann zeta function through the Hurwitz sheets ζ(s, 1+t), along which the zeros move; through quotient modules of entire functions attached to the zeros, above all Meyer's quotient ℬ/I\_ζ; and through arithmetic, cohomological and positivity constructions modelled on Weil's explicit formula and on Deligne's proof of the Weil conjectures. This record states what the programme and an audit of it have established, with proofs. The primary decomposition of Meyer's quotient converges for every class if and only if the principal parts of 1/ζ at the zeros are polynomially bounded; the Nyman–Beurling family is dense in the Fréchet topology unconditionally, already for the degrees 2^a3^b when t > (log 2)(log 3)/(4π); among the forms compatible with the scaling transfer, positivity is exactly the condition that removes the off-line zeros; in a two-line system the shifted zero set is the mirror of the zero set, Weil's quadratic form sits on the diagonal of a hyperbolic chiral form, the holonomy index is Turing's index, and the two-line quotient splits for every primitive Dirichlet L-function; a formal logarithm detects freeness of monoids of integers and characterizes the Eulerian sheets, and the even lattice sums with φ(q) > 2 have infinitely many zeros on both sides of the critical line; and the programme's exponent data have tensor-power abscissa exactly 1 + k·max Re ρ, an algebraic purity criterion sits at the core of Weil II 1.8.4, and thirteen misprints of the printed Weil II are recorded. Proved negative results are stated with their scope and the input each construction would need, and the bridges to other areas are described. No result here proves or disproves the Riemann hypothesis.

## 0. Introduction

### 0.1 Why this record

The Riemann hypothesis (RH) asserts that every nontrivial zero of ζ has real part 1/2. Its classical reformulations include Weil's positivity criterion for the explicit formula [We52, Bo], the Nyman–Beurling criterion [Be, BD], and the analogy with curves over finite fields, where RH is Weil's theorem [We48] and whose higher-dimensional form is Deligne's [De]. The programme builds constructions around these reformulations and around the flow of the Hurwitz sheets ζ(s, 1+t), which moves the zeros of ζ off the critical line. It consists of several hundred numbered statements with proofs, with labels such as MCL5, OMS6 or GSL4, published in the Zenodo record *Split-Zero cohomology and the zeta-function research programme* (concept DOI 10.5281/zenodo.22678085) and in the repository KokunoYumeto/zeta-function-research-reader. This record states what holds, with proofs or with the location of the proof, what fails and in which scope, and how the programme connects with other areas, so that a reader need not work through the files to find out.

### 0.2 Main results

Results marked *new* were found in the audit; the others are the programme's, checked in the audit.

- **Meyer's quotient** (§3). **Theorem 3.9** (*new*): the primary decomposition of Q = ℬ/I\_ζ converges for every class if and only if the principal parts of 1/ζ at the zeros are polynomially bounded, if and only if the jet map is an isomorphism onto the rapidly decreasing jet tuples; with the spectral theory of multiplication by s (Proposition 3.2) and the exact summation image (Proposition 3.5).
- **Density and positivity** (§3). Nyman–Beurling density in ℬ, unconditional, and under two Carleman criteria (*new*) already for 2^a3^b when t > 0.06060… (Proposition 3.11), with Proposition 3.12 (*new*); the transfer-compatible Hermitian forms, positive exactly when supported on the critical zeros (Lemma 3.13; the Hermitian classification *new*).
- **The two lines** (§4, *new*). The first Hurwitz jet and the mirror set, with mirror equal to shift at every zero if and only if RH holds (Theorems 4.1–4.2); Weil's form on the diagonal of the chiral cross form (Proposition 4.6, Corollary 4.7); the holonomy index as Turing's index (Proposition 4.9); the splitting for every primitive Dirichlet L-function (Proposition 4.12).
- **Sheets and monoids** (§2). The formal logarithm detects freeness (Theorem 2.4, stronger form *new*; Corollary 2.5, *new*); Z\_{1/q} is Eulerian exactly for q ∈ {3, 4, 6} and has infinitely many zeros on both sides of the line when φ(q) > 2 (Propositions 2.8–2.9, *new*); the velocity results of §2.1 (*new*).
- **Weights** (§5). Propositions 5.1 (*new*), 5.2 and 5.3, Lemma 5.4 (*new*, a corrected constant in Weil II 2.1.7), and thirteen misprints in print (§5.4).
- **Part B** (§8): thirty proved negative results, each with its scope and the input the construction would need. **Part C** (§9): the bridges.

### 0.3 What the results mean

The quotient Q = ℬ/I\_ζ is the programme's central object, and §3 describes it completely as a module under multiplication by s. Theorem 3.9 identifies the one structural question left, whether Q is the convergent sum of its primary parts, with polynomial lower bounds for the principal parts of 1/ζ at the zeros; that question is open, and a positive answer would imply that every zero is simple.

Every bounded positive form compatible with the scaling transfer is supported on the critical zeros, while an off-line pair enters such a form as a hyperbolic block (Lemma 3.13). The two-line system of §4 realizes this geometrically: Weil's form sits on the diagonal of a chiral form that is hyperbolic for every configuration of zeros, and counting in the system is Turing's method.

The Euler product is located precisely: the Eulerian sheets are a ∈ {1, 1/2}, the even lattice sums with φ(q) > 2 have zeros off the line, and the Davenport–Heilbronn function shares the functional equation and the two-line structure of ζ while having a zero off the line. A construction whose proof uses only properties shared with these functions has conclusions that hold for them too, and Part B records the input that would distinguish ζ, in most cases the Euler product. On Deligne's side, the uniform pole bound complementing the programme's positivity step is equivalent on its finite data to max Re ρ ≤ 1/2 (Proposition 5.1), so it has to come from an independent source, as the H²\_c of a fixed curve does in Weil II (Question 8). No result here proves or disproves RH, and none is presented as doing so.

### 0.4 How this record was made

This record is an audit, carried out by Claude between 22 and 26 September 2026, of the programme's published work: the second attempt's proofs, the continuation bulletins of 24–25 September, the programme's reconstruction of Weil II and its Deligne reader, the final reports of its working sessions of 24–25 September, and the material of the author's other workbenches used here (§11 lists what was not read). The programme, its constructions and most of its theorems are the work of its author, KokunoYumeto, developed with ChatGPT and Codex (OpenAI). Programme statements are cited by their labels, which the programme's reading guide `181-reading-guide-and-file-locations.md` and its index `182-complete-file-and-migration-index.json` locate; results found in the audit are credited as such.

Every block was read against its own proofs. The audit's notes were each refereed by an instance that had not written them (nineteen passes and a two-part final pass), the reader compiled from them had its own referee pass, and a later review looked for understatement and missed generality as well as for overstatement; every finding was re-derived before it was applied. Every statement carries one of four statuses: **verified** (proved here; or proved in the programme at the cited label and checked in the audit; or re-computed by a named check); **not verified here** (nothing further is implied, in either direction); **my assessment** (a view with its reasons, in the first person); **proved negative** (a statement shown false or limited, with the counterexample or derivation printed). A statement supported by computation alone is labelled as numerical.

Re-deriving the withdrawn texts changed several statements, and those given here are the corrected ones (Proposition 5.2 at on-line zeros; Corollary 2.3 for a^sζ(s, a), since ζ(s, 1/2) = 2^s∏\_{p>2}(1 − p^{−s})^{−1}; Theorem 2.2(a); step 4 of Proposition 3.11). An earlier claim made in the audit, that the zeros of ζ(s, 1+t) lie on vertical lines only at the Eulerian times, is false: zero 4 of ζ crosses Re s = 1/2 at t = 0.95095300425 and zero 5 at t = 0.858704259442 (numerical, to 25 digits).

### 0.5 Organization

Part A (§§1–7) contains the verified results: the setting (§1), sheets, monoids and Euler products (§2), Meyer's quotient (§3), the two lines (§4), weights (§5), further results (§6) and a catalogue of the remaining results (§7). Part B (§8) contains the proved negative results, Part C (§9) the bridges and the directions they open, §10 the questions and §11 the verification.

---

# Part A. Verified results

## 1. The setting

**The programme's idea.** The programme's coefficient algebra keeps a ring's internal zero apart from a separate symbol τ for absence (the split-zero semiring G(R) = R ⊔ {τ}), so that a zero element in a support fibre is not confused with an absent fibre. On the zeta side it follows the zeros of ζ along the Hurwitz sheets t ↦ ζ(s, 1+t) and asks which constructions (quotient modules, receivers, positivity forms, cohomology over a reconstructed arithmetic) determine where the zeros lie. In the author's picture the support τ is the pivot of the swing between 0 and 1; on the zeta side the corresponding pivot is the reflection s ↦ 1 − s̄ about Re s = 1/2 (a proposed typed matching, §9.8). We write w̄ or conj(w) for the complex conjugate.

**Sheets and zeros.** For a > 0, ζ(s, a) = Σ\_{n≥0}(n + a)^{−s} on Re s > 1, continued meromorphically with one simple pole at s = 1; the flow is t ↦ ζ(s, 1+t), the Eulerian sheets are ζ(s, 1) = ζ(s) and ζ(s, 1/2) = (2^s − 1)ζ(s), and the even lattice sums are Z\_a(s) = ζ(s, a) + ζ(s, 1−a), 0 < a < 1. Put ξ(s) = (1/2)s(s − 1)π^{−s/2}Γ(s/2)ζ(s) and F\_∗(s) = ξ(s)/4 (the programme's F₀). 𝒵 is the set of distinct nontrivial zeros ρ = β + iγ, with multiplicities m\_ρ written out in sums, and ρ^# = 1 − ρ̄; since ξ(1 − s) = ξ(s) and ξ(s̄) = conj(ξ(s)), # permutes 𝒵 preserving multiplicities, and RH says exactly that ρ^# = ρ for every ρ. For T > 0 not an ordinate, N(T) counts the zeros with 0 < γ ≤ T, N₀(T) those on the line and P(T) those with β < 1/2 (with multiplicity); Hardy's function Z(t) = e^{iθ(t)}ζ(1/2 + it) is real, and V(T) is its number of sign changes on (0, T).

**The strip space and Meyer's quotient.** ℬ is the Fréchet space of entire F with b\_{A,M}(F) = sup\_{|σ|≤A, t∈ℝ}(1 + |t|)^M|F(σ + it)| < ∞ for all A, M ≥ 0. For a divisor D, I\_D ⊂ ℬ is the closed ideal of functions vanishing to order at least D(λ) at each λ, and I\_ζ = I\_𝒵. The programme's Meyer quotient is Q = 𝒜/ℰS ≅ ℬ/I\_ζ (OMS3.14; [Me]), where ℰ is Connes' summation map and the isomorphism is the Mellin transform of the exact summation image (Proposition 3.5); L denotes multiplication by s. With T a formal variable, the jet at ρ is j\_ρ[F] = F(ρ + T) mod T^{m\_ρ} ∈ A\_ρ = ℂ[T]/(T^{m\_ρ}), and the primary projector is Π\_ρ = s\_ρj\_ρ with the programme's sections s\_ρ (OMS6).

**Two lines, three maps and Weil's pairing.** The two-line function G(s) = F\_∗(s)F\_∗(s + 1) = ξ(s)ξ(s + 1)/16 has zero set 𝒵 ⊔ (𝒵 − 1), in 0 < Re s < 1 and −1 < Re s < 0. The maps are the reflection s^# = 1 − s̄ through 1/2, the mirror A(s) = −s̄ through the pole at 0, and the translation T between the lines; on 𝒵, A(ρ) = ρ^# − 1, that is T^{−1}A = #. For finitely supported u on 𝒵, Weil's pairing is Ω(u) = Σ\_ρ m\_ρu(ρ)conj(u(ρ^#)), the zero side of Weil's quadratic form [We52, Bo]; Weil's criterion says that RH holds if and only if Weil's functional is nonnegative on every g ∗ g^#, and Ω ≥ 0 on all finitely supported u exactly when every zero is on the line (Proposition 4.6(b)).

## 2. Hurwitz sheets, monoids of integers and Euler products

### 2.1 Zero velocities on the sheets

Along the flow a = 1 + t a simple zero ρ of ζ(s, a) moves with velocity c(ρ) = ρζ(ρ + 1, a)/∂\_sζ(ρ, a), by implicit differentiation from ∂\_aζ(s, a) = −sζ(s + 1, a) (Theorem 4.1). At a = 1 the first zero has velocity 0.98358 + 9.65780i and leaves the line to the right as t increases; numerically the first five zeros leave the line for t > 0, and zeros 4 and 5 cross back at the non-Eulerian times t ≈ 0.95095 and t ≈ 0.85870. The following results were found in the audit (*new*).

**Theorem 2.1 (the velocity sums).** Let a > 0, let c₀ exceed the real part of every zero of ζ(s, a), and let h be entire with (1 + |Re z|)^A h(z) bounded on |Im z| ≤ c₀ + 2 for every A; put H(s) = h(−i(s − 1/2)) and ĥ₁(ξ) = (2π)^{−1}∫(1/2 + iu)h(u)e^{−iuξ}du. Put F\_a(s) = sζ(s + 1, a)/ζ(s, a) and aζ(s + 1, a)/ζ(s, a) = Σ\_r β\_r(a)r^{−s}, r in the multiplicative monoid generated by the numbers 1 + n/a (β₁ = 1). Along good heights T\_k → ∞ (where 1/ζ(σ ± iT\_k, a) is polynomially bounded on the horizontal segments),

  lim\_k Σ\_{|γ|<T\_k} Res\_ρ(F\_aH) = (1/a)(2π)^{−1}∫(1/2 + iu)h(u)du + (1/a)Σ\_{r>1} β\_r(a)r^{−1/2}ĥ₁(log r) + L\_a(h),

with the explicit left-line term L\_a(h) = −(2πi)^{−1}∫\_{Re s=−b} F\_aH ds (3/2 < b < 2).

**Theorem 2.2 (consequences).** (a) The smoothed sums of Re c and Im c over T₁ < γ ≤ T₂, 10Δ ≤ T₁, grow like (T₂ − T₁)/(4πa) and (T₂² − T₁²)/(4πa) − (T₂ − T₁); for fixed width Δ the horizontal error is of order T, and at a = 1 both errors tend to 0 when Δ ≥ (1 + δ)√(2 log T₂)/log 2 and T₁ ≥ max(10Δ, 4Δ√(log Δ)), given constants independent of Δ. (b) Under (H), all but finitely many zeros simple and on the line, the sharp laws have errors that are unbounded multiples of T (normalized mean square with limsup ≥ 0.0373); the almost periodicity of the smoothed error is unconditional. (c) The smoothed spectrum has frequencies log r and amplitudes −β\_r(a)r^{−1/2}e^{−Δ²log²r/2}/(2πa log r). (d) The velocity spectrum factors over a ℚ-independent basis if and only if a ∈ {1, 1/2}, where the primes are exactly the frequencies of maximal amplitude. (e) If the zeros up to γ\_n are simple and on the line (true for n ≤ 1.2·10¹³ [PT]), arg c(ρ\_n) = π/2 − arctan(1/(2γ\_n)) + π(S\_{3/2}(γ\_n) − S\_n), S\_n = n − 3/2 − θ(γ\_n)/π, S\_{3/2}(t) = π^{−1}arg ζ(3/2 + it).

**Corollary 2.3 (only two sheets are Eulerian).** The normalized sheet a^sζ(s, a) has an Euler product with local factors (1 − P^{−s})^{−1} only for a ∈ {1, 1/2}.

*Status of 2.1–2.3.* Verified in the audit: the proofs were checked as stated (2.2(d) with a full referee pass; 2.2(b) completed in the audit; 2.3 follows from 2.2(d)), and Theorem 2.1 was also checked numerically at a = 1 (relative difference 1.8·10⁻¹⁸). The proofs are not reproduced in this record. At a = 1/q, 2.2(d) is the factoriality criterion for congruence monoids [BC, Theorem 3.4(2)] (§2.3).

### 2.2 Monoids of integers and the formal logarithm

Let M be a multiplicative submonoid of the positive integers. An atom is an m > 1 in M that is not a product of two elements of M∖{1}; M is free if every element has exactly one factorization into atoms, and half-factorial if all factorizations of each element have the same length. With D\_M(s) = Σ\_{m∈M}m^{−s} = 1 + E(s), put log D\_M = Σ\_{k≥1}((−1)^{k+1}/k)E^k = Σ\_{n≥2} r\_n n^{−s}, so that r\_n = Σ\_k ((−1)^{k+1}/k)T\_k(n), where T\_k(n) counts the ordered k-tuples in (M∖{1})^k with product n.

**Theorem 2.4 (the formal logarithm detects freeness).** Let n ∈ M and suppose that every proper M-divisor of n (an m ∈ M with 1 < m < n and n/m ∈ M) has exactly one factorization. (a) If n has one factorization, r\_n = 1/k when n = u^k for an atom u and r\_n = 0 otherwise. (b) If n has j ≥ 2 factorizations, r\_n = 1 − j + ε, where ε = Σ1/k over the factorizations of the form u^k; this is at most −1/6. Consequently M is free if and only if all r\_n ≥ 0, and if M is not free the first negative coefficient sits exactly at the least element with two factorizations. In a congruence monoid M\_H with H ≠ G (§2.3) the value in (b) is at most −1/2, and infinitely many elements satisfy (b): for distinct primes p, r in a class c ∉ H and p′, r′ in c^{−1}, n = pp′rr′ has r\_n = −1, or −2 if c² ∈ H (for example r\_{3·7·11·19} = −2 in the Hilbert monoid {n ≡ 1 mod 4}).

*Proof.* The entries of a tuple counted by T\_k(n), k ≥ 2, are proper M-divisors of n and factor uniquely, so T\_k(n) = Σ\_ΦS\_k(Φ), where Φ runs over the factorizations of n and S\_k(Φ) counts the ordered splittings of Φ into k nonempty parts. With a separate variable x\_u for each atom u of Φ (atoms need not be multiplicatively independent: 4 and 8), splittings are counted by log∏\_u(1 − x\_u)^{−1}, so Σ\_k(−1)^{k+1}S\_k(Φ)/k is 1/k if Φ is k copies of one atom and 0 otherwise. This gives (a), and in (b) r\_n = 1 − j + ε, since T₁(n) = 1 while there are j factorizations. The pure powers among them have distinct exponents ≥ 2, so r\_n ≤ −1/2 if there is at most one, and r\_n ≤ 1 − P + 1/2 + … + 1/(P + 1) ≤ −1/6 if there are P ≥ 2. In M\_H two pure-power factorizations u^a = v^b would make u and v powers of one w with [w] ∈ H, against atomicity, so r\_n ≤ −1/2. For n = pp′rr′ the factorizations are {pp′, rr′}, {pr′, rp′}, and {pr, p′r′} when c² ∈ H, with ε = 0, and Dirichlet's theorem gives infinitely many such n. ∎

*Status.* Verified: proved here. First proved in the programme (CEI Theorem 3.1 for the criterion, ETR1.5–1.7 for the bound −1/6) and derived independently in the audit; the hypothesis on proper M-divisors, the examples and the bound −1/2 were found in the audit (*new*). Novelty: not located in the literature (one search); elementary.

**Corollary 2.5 (the first negative coefficient above −1/2).** If N ∈ M has two or more factorizations, every proper M-divisor of N has one, and r\_N > −1/2, then N has exactly two factorizations a^{j₁} = b^{j₂} with gcd(j₁, j₂) = 1, N = c^{j₁j₂}, and r\_N = −1 + 1/j₁ + 1/j₂. Every value −1 + 1/u + 1/v with 2 ≤ u < v coprime occurs, at N = c^{uv} in ⟨c^u, c^v⟩; so the possible first negative coefficients in (−1/2, 0) are exactly {−1/2 + 1/v : v ≥ 3 odd} ∪ {−5/12, −7/15}.

*Proof.* By Theorem 2.4(b), r\_N > −1/2 forces j = 2 with both factorizations pure powers, a^{j₁} = b^{j₂}; g = gcd(j₁, j₂) > 1 would make a^{j₁/g} = b^{j₂/g} a proper M-divisor with two factorizations, so g = 1, and comparing prime exponents gives a = c^{j₂}, b = c^{j₁}; in ⟨c^u, c^v⟩ (whose generators are atoms since u ∤ v) the least exponent with two representations is uv; and 1/u + 1/v > 1/2 leaves u = 2 with v odd, or u = 3 with v ∈ {4, 5}. ∎ *Status.* Verified: proved here and checked exactly on 286 generator sets; found in the audit (*new*); elementary, not searched.

**Example 2.6.** In M = {1} ∪ {2^e : e ≥ 2}, 64 = 4·4·4 = 8·8 and r₆₄ = −1/6, while D\_M = (1 − x + x²)/(1 − x), x = 2^{−s}, has all its zeros on Re s = 0; so D\_M has no zeros on its half-plane of absolute convergence Re s > 0, like the Dirichlet series of every free monoid (ETR2), and M is not free. The monoid appears first in the programme's ETR1 (verified: a direct computation).

### 2.3 Congruence monoids and the even lattice sums

Fix q ≥ 1 and a subgroup H of G = (ℤ/q)^×, and let M\_H = {n ≥ 1 : gcd(n, q) = 1, n mod q ∈ H}; then D\_{M\_H}(s) = [G : H]^{−1}Σ\_{χ|\_H=1}L(s, χ).

**Proposition 2.7.** The following are equivalent: (i) M\_H is free; (ii) H = G; (iii) all r\_n ≥ 0; (iv) D\_{M\_H} has no zeros in Re s > 1. Moreover M\_H is half-factorial if and only if [G : H] ≤ 2.

*Proof.* (i)⇔(iii) is Theorem 2.4, and M\_G is free on the primes prime to q. If H ≠ G, infinitely many primes lie outside H, so a class of order d ≥ 2 in G/H contains primes p ≠ r, and the atoms A\_j = p^{d−j}r^j satisfy A₀A₂ = A₁²; moreover D\_{M\_H} then has components along two distinct primitive characters, so [SW] gives zeros in Re s > 1 (such representations are unique; proof of Proposition 2.9). If all r\_n ≥ 0, then log D ≤ D − 1 coefficientwise, so log D converges absolutely on Re s > 1 and D = e^{log D} ≠ 0 there. For [G : H] = 2 every factorization of n has length a + b/2, a and b counting the prime factors inside and outside H; for [G : H] ≥ 3, (pp′)^N = p^N·p′^N or (prs)² = p²·r²·s² has factorizations of two lengths. ∎

*Status.* Verified: proved here. (i)⇔(ii) and the half-factoriality criterion are the standard criteria for Krull monoids with class group G/H (for H = {1}: [BC, Theorem 3.4], the Krull-monoid analogue of Carlitz's class-number-two theorem [Ca]); the direct proofs and the equivalences with (iii), (iv) were found in the audit (*new*), (iv)⇒(ii) using [SW] as stated in its abstract.

**Proposition 2.8 (the even sheets at a = 1/q).** For q ≥ 3, Z\_{1/q}(s) = q^sΣ\_{n≡±1 (q)}n^{−s} = q^sD\_{M\_{±1}}(s). Hence the sheet a = 1/q is Eulerian (the monoid {n ≡ ±1 mod q} is free) if and only if φ(q) ≤ 2, that is q ∈ {3, 4, 6}, if and only if its formal logarithm is nonnegative, if and only if Z\_{1/q} has no zeros with Re s > 1; and exactly these q make {n ≡ 1 mod q} half-factorial.

*Proof.* ζ(s, 1/q) = q^sΣ\_{n≥0}(qn + 1)^{−s} and ζ(s, 1 − 1/q) = q^sΣ\_{m≡−1}m^{−s}; then apply Proposition 2.7 with H = {±1} and H = {1}. ∎ *Status.* Verified: proved here; found in the audit (*new*). The packaging as a test on the sheets is not in the survey [BC]; not searched further.

**Proposition 2.9 (zeros of the even sheets on both sides of the line).** Let φ(q) > 2. There is η > 0 such that for all 1/2 < σ₁ < σ₂ < 1 + η the number of zeros of Z\_{1/q} with σ₁ < Re s < σ₂ and |Im s| ≤ T lies between c₁T and c₂T for all large T (c₁, c₂ > 0 depending on q, σ₁, σ₂), and the same holds, with another η, in the reflected strips 1 − σ₂ < Re s < 1 − σ₁. So Z\_{1/q} has infinitely many zeros with Re s > 1, with 1/2 < Re s < 1, with 0 < Re s < 1/2 and with Re s < 0.

*Proof.* On the right, Z\_{1/q} = q^sD\_{M\_{±1}} has components along two distinct primitive characters, and [SW] applies. On the left, Z\_a(1 − s) = 2Γ(s)(2π)^{−s}cos(πs/2)Φ\_a(s) with Φ\_a(s) = 2Σ\_{k≥1}cos(2πka)k^{−s}, and at a = 1/q, expanding the cosines in even characters with Gauss sums gives Φ\_{1/q} = Σ\_ψP\_ψL(s, ψ) over distinct primitive ψ with Dirichlet polynomials P\_ψ. This representation is unique (at the least integer d₀ of the supports, the coefficients at d₀p for large primes p are Σ\_ψb\_{ψ,d₀}ψ(p), and distinct primitive characters are independent on the primes); the ζ-component is nonzero (its coefficient at q^{−s} is 2Σ\_{e|q squarefree}1/φ(e)), and another is nonzero, since otherwise cos(2πp/q) = cos(2π/q) for all large primes p, forcing φ(q) ≤ 2. So [SW] gives zeros s₀ of Φ\_{1/q} in the strips, and each 1 − s₀ is a zero of Z\_{1/q}, the factor 2Γ(s₀)(2π)^{−s₀}cos(πs₀/2) being finite and nonzero. ∎

*Status.* Verified: proved here, using [SW] as stated in its abstract (its printed statement was not checked); found in the audit (*new*); check Z8 finds zeros of Z\_{1/8} and Z\_{1/12} in 0 < Re s < 1/2. Numerically, Z\_{1/5} (whose monoid first has two factorizations at 36 = 4·9 = 6·6, with r₃₆ = −1/2) has 24 zeros with Re s > 0.505 below height 150, the lowest at 0.54307 + 15.70405i, and zeros to the left of the line such as −0.158 + 6.614i.

### 2.4 Shifted zeta products and tensor Euler functions

For finite exponent data, a finitely supported measure μ on ℂ with positive integer masses, the programme's tensor Euler function of degree d is ℒ\_d = ∏\_p det(1 − p^{−s}W\_p^{⊗d})^{−1} = ∏\_σ ζ(s − σ)^{μ^{∗d}({σ})} (ETR4–ETR5).

**Lemma 2.10 (shifted zeta functions are multiplicatively independent).** Let σ₁, …, σ\_ℓ ∈ ℂ be distinct and C\_j ∈ ℂ. If Σ\_jC\_j(ζ′/ζ)(s − σ\_j) ≡ 0, then all C\_j = 0; in particular ∏\_jζ(s − σ\_j)^{C\_j} ≡ 1 with C\_j ∈ ℤ only if all C\_j = 0. The same holds for L(s − σ\_j, χ), χ any Dirichlet character.

*Proof.* The Euler logarithm Σ\_jC\_j log ζ(s − σ\_j) = Σ\_pΣ\_r(1/r)(Σ\_jC\_jp^{rσ\_j})p^{−rs} vanishes identically (its derivative is the given sum, and it tends to 0 as s → +∞), so Σ\_jC\_jp^{rσ\_j} = 0 for all p and r ≥ 1 (for L, after dividing by χ(p)^r, p ∤ q). Two points with p^{σ\_i} = p^{σ\_j} cannot collide at two primes, so for some prime the x\_j = p^{σ\_j} are distinct, and the system for r = 1, …, ℓ has determinant ∏\_jx\_j∏\_{i<j}(x\_j − x\_i) ≠ 0. ∎

**Lemma 2.11 (uniqueness of convolution roots).** If finitely supported complex measures satisfy μ^{∗d} = ν^{∗d}, then μ = ην for a d-th root of unity η, and μ = ν if the total masses are positive reals.

*Proof.* The exponential transforms satisfy A^d = B^d; on the connected set {B ≠ 0}, A/B is a continuous d-th root of unity, hence constant, and distinct exponentials are linearly independent. ∎

**Corollary 2.12.** For finite exponent data a single ℒ\_d determines μ (Lemma 2.10 gives μ^{∗d}, and Lemma 2.11 gives μ).

*Status of 2.10–2.12.* Verified: proved here; proved in the programme at ETR8, ETR9 and ETR4–ETR9 for integer exponents and positive masses (the complex, L-function and root-of-unity forms found in the audit, *new*). For conjugation-stable data the real pole of ℒ\_{2k} at 1 + 2kB has order h\_{2k}, with h\_{2k}^{1/2k} increasing to the dimension of the maximal face (ETR5–ETR7): Deligne's §1.5 mechanism, as the programme credits. Lemma 2.10 is necessarily global (§8, N-Eu).

## 3. Meyer's quotient, its jets and its receivers

Every quotient of ℬ by a closed subspace is a Fréchet space with the quotient seminorms b̄\_{A,M} [Ru, Theorem 1.41].

### 3.1 The strip space and multiplication by s

**Lemma 3.1.** For all A, M ≥ 0 the unit ball of b\_{A+1,M+1} is precompact for b\_{A,M}. So ℬ and every quotient ℬ/I by a closed subspace are Fréchet–Montel, hence reflexive, and (ℬ/I)′\_β ≅ I^⟂ ⊂ ℬ′\_β topologically.

*Proof.* Cauchy's estimate makes the ball equicontinuous on |Re s| ≤ A + 1/2, the extra factor (1 + |t|)^{−1} makes |t| ≥ T uniformly small, and Arzelà–Ascoli on the remaining rectangle gives finite nets; the rest is the permanence of Fréchet–Schwartz spaces under closed quotients [Ja; SchW, Ch. IV]. ∎ *Status.* Verified: proved here; found in the audit (*new*). The programme obtains these properties through the summation image (SDT).

**Proposition 3.2 (multiplication by s on ℬ/I\_D).** Let 0 ≢ Φ ∈ ℬ vanish to order at least D. (a) For λ ∉ supp D, λ − L is invertible on ℬ/I\_D, with inverse induced by R\_λF = (F − Φ\_λF(λ)/Φ\_λ(λ))/(λ − s), Φ\_λ = Φ/(s − λ)^{ord\_λΦ}. (b) The spectrum of L is supp D. (c) If ρ has multiplicity m in D, then ker(L − ρ)^m = ker(L − ρ)^{m+1} has dimension m, j\_ρ identifies it with ℂ[T]/(T^m), and L − ρ acts on it as multiplication by T: one Jordan block of length m.

*Proof.* Division by (s − λ)^k at a zero of order ≥ k preserves ℬ (maximum principle near λ), so Φ\_λ ∈ I\_D and R\_λ inverts λ − s modulo I\_D. With m′ = ord\_ρΦ, U = Φ/(s − ρ)^{m′−m+1} is not in I\_D while (s − ρ)U is. A class lies in ker(L − ρ)^k exactly when it vanishes to full order off ρ and to order m − k at ρ, and U\_ρ·P(s − ρ), U\_ρ = Φ/(s − ρ)^{m′}, realizes every jet at ρ. ∎ *Status.* Verified: proved here; proved in the programme for the zeta divisor at RZ3–RZ7; the general-divisor form was found in the audit (*new*).

**Lemma 3.3 (no equivariant maps across disjoint divisors).** Let D ≤ div F\_D for some 0 ≢ F\_D ∈ ℬ, and let D″ be the part of a divisor D′ off supp D. Every linear H : ℬ/I\_D → ℬ/I\_{D′} with HL = LH takes values in I\_{D″}/I\_{D′}; in particular H = 0 if the supports are disjoint. Continuity is not needed.

*Proof.* For λ ∈ supp D′ ∖ supp D of multiplicity m, (L − λ)^m is onto ℬ/I\_D, so every H(y) = (L − λ)^mH(x) has zero m-jet at λ. ∎ *Status.* Verified: proved here; found in the audit (*new*); it strengthens the programme's GSL6.

**Lemma 3.4 (uniqueness of exponential sums).** Let 0 ≢ G ∈ ℬ and let Z be a set of zeros of G in a vertical strip, m\_ρ = ord\_ρG. If Σ\_{ρ,k}c\_{ρ,k}x^ke^{ρx} = 0 for all real x, with 0 ≤ k < m\_ρ and Σ|c\_{ρ,k}|k!R^{−k} < ∞ for some R > 0, then all c\_{ρ,k} = 0.

*Proof.* Pairing with the half-Mellin representation F(s) = (1/2)∫a(e^v)e^{sv}dv of F ∈ ℬ (NJS4.1) gives Σc\_{ρ,k}F^{(k)}(ρ) = 0 for all F ∈ ℬ; test with G(s)(s − ρ₀)^{−m}P(s − ρ₀), P a polynomial. ∎ *Status.* Verified: proved here; in the programme for the Gaussian-weighted zeta divisor at HBW8.9–8.12; the general form was found in the audit (*new*).

### 3.2 The exact summation image

Let S be the space of even Schwartz functions f with f(0) = 0 and ∫f = 0, Σf(u) = 2Σ\_{n≥1}f(nu), and ℳ₀b(s) = ∫₀^∞b(u)u^{s−1}du.

**Proposition 3.5 (the exact summation image).** f ↦ ℳ₀Σf, which equals 2ζ(s)∫₀^∞f(v)v^{s−1}dv on Re s > 1, is a topological isomorphism of S onto I\_ζ, with inverse F ↦ f\_F(x) = (2π)^{−1}∫F(2 + it)/(2ζ(2 + it))x^{−2−it}dt = (1/2)Σ\_{n≥1}μ(n)(ℳ₀^{−1}F)(nx); moreover f\_F^{(2r)}(0)/(2r)! = F(−2r)/(2ζ′(−2r)) for r ≥ 1, ∫₀^∞f\_F dx/x = −F(0) and ∫₀^∞f\_F log x dx = F(1)/2. In particular the summation image is closed.

*Outline.* Poisson summation controls u → 0, and Müntz's formula [Ti, §2.11] with the Euler product gives injectivity. For F ∈ I\_ζ, F/(2ζ) has simple poles only at −2r; the division estimate |F/F\_∗| ≤ C exp(C(|t| + 2)^{3/2}log(|t| + 2)) (S3, OMS2.8) is removed by a factor e^{εs²} and the maximum principle, and shifting the inverse Mellin contour to Re s = −2N − 1 picks up the residues F(−2r)/(2ζ′(−2r))x^{2r}.

*Status.* Verified: proved in the programme at SSI1–SSI7 and OMS2–OMS4, and checked in the audit, including the Taylor coefficients and endpoint identities on the programme's source vector. On the programme's account (OMS0) this is Meyer's range theorem [Me] made explicit for ℬ; the comparison with Meyer's paper is not verified here. Consequently the closure of Connes' summation map in the rapid-decay Fréchet space (the ideal of zero-jets, S5 of the second attempt) is attained by the image itself, and Q = 𝒜/ℰS ≅ ℬ/I\_ζ.

### 3.3 The jet map and the primary decomposition

The programme's section s\_ρ(P) = [U\_ρ·(Pc\_ρ)(s − ρ)], U\_ρ = F\_∗/(s − ρ)^{m\_ρ}, c\_ρ the inverse of the jet of U\_ρ, satisfies j\_ηs\_ρ = δ\_{ηρ}; so the Π\_ρ = s\_ρj\_ρ are orthogonal commuting idempotents, and finite sums of sections realize every finitely supported jet tuple (OMS6). Let Λ\_m be the Fréchet space of tuples (P\_ρ) ∈ ∏A\_ρ with sup\_ρ(1 + |γ|)^M‖P\_ρ‖ < ∞ for all M, ‖·‖ the largest coefficient.

**Lemma 3.6 (jet decay).** For F ∈ ℬ, |β| ≤ 3/2 and r, M ≥ 0, (1 + |γ|)^M|F^{(r)}(ρ)/r!| ≤ 2^r((1 + |γ|)/(1/2 + |γ|))^Mb\_{2,M}(F) ≤ 2^{r+M}b\_{2,M}(F), and at the nontrivial zeros the middle factor is at most 1.0342^M (Cauchy's formula on |z − ρ| = 1/2, and γ₁ = 14.1347…). *Status.* Verified: proved here; found in the audit (*new*), an explicit form of OMS5.6.

**Corollary 3.7.** The jet image J(Q), J = (j\_ρ)\_ρ, lies in Λ\_m and is dense there; it is a proper dense subspace of the product, the quotient topology of Q is strictly finer than the product topology on J(Q), and Q is not the product of its primary blocks.

*Proof.* Lemma 3.6 and m\_ρ = O(log|γ|) give J(Q) ⊂ Λ\_m, and the finitely supported tuples, realized by sections, are dense in Λ\_m and in the product; a class with F(ρ) = 1 at every zero would give 1 + |γ| ≤ 2b\_{2,1}(F) for all ordinates; and equal topologies would make J(Q) complete, hence the whole product. ∎ *Status.* Verified: proved in the programme at OMS5 and checked in the audit; the density in Λ\_m was found in the audit (*new*).

We use (D1) the number of zeros with |γ − T| < 1 is O(log T), (D2) ζ′/ζ(s) = Σ\_{|t−γ|<1}(s − ρ)^{−1} + O(log t) for −1 ≤ σ ≤ 2, t ≥ 2 [Ti, Theorems 9.2, 9.6(A)], and **Lemma 3.8** [Ti, Theorem 9.7]: there are A, T₀ with a good height t in every [T, T + 1], T ≥ T₀, where |ζ(σ ± it)| ≥ t^{−A} for −1 ≤ σ ≤ 2 (verified: Titchmarsh's proof; the statements were checked on the printed pages). Let c\_{ρ,k} (k < m = m\_ρ) be the Taylor coefficients at ρ of (s − ρ)^m/ζ(s), so that c\_{ρ,0} = m!/ζ^{(m)}(ρ).

**Theorem 3.9 (when the primary decomposition converges).** The following are equivalent.

- (a) For some enumeration (ρ\_n) of the distinct zeros, Σ\_{k≤n}Π\_{ρ\_k}x converges for every x ∈ Q (the limit is then x).
- (a′) For every x ∈ Q the set {Π\_ρx}\_ρ is bounded.
- (b) Σ\_ρΠ\_ρx converges absolutely for every x ∈ Q.
- (b′) For every x, every continuous seminorm q and every N, q(Π\_ρx) = O((1 + |γ|)^{−N}).
- (c) There are C, K with |c\_{ρ,k}| ≤ C(1 + |γ|)^K for all ρ and k < m\_ρ: the principal parts of 1/ζ at the zeros are polynomially bounded.
- (d) J : Q → Λ\_m is an isomorphism of Fréchet spaces.

For simple zeros (c) reads |ζ′(ρ)| ≥ c(1 + |γ|)^{−K}, and in every case (a′) implies |ζ^{(m\_ρ)}(ρ)/m\_ρ!| ≥ c(1 + |γ|)^{−K}. The theorem carries over to the zeros of a primitive Dirichlet L-function, with 1/L(s, χ) in (c), L(s, χ) in place of (s − 1)ζ(s) below, and (D1), (D2) and the good heights with log q(|t| + 2).

*Proof.* (a)⇒(a′) and (b)⇒(a) are immediate, and a limit y of the partial sums has the jets of x, so y = x.

(a′)⇒(c). By Banach–Steinhaus [Ru, Theorem 2.6], b̄\_{2,0}(Π\_ρx) ≤ C₀b̄\_{A₁,M₁}(x) for some A₁, M₁, C₀. The Gaussian E\_ρ(s) = e^{(s−ρ)²} (CFP6.1) has b\_{A₁,M₁}(E\_ρ) ≤ C₁(1 + |γ|)^{M₁}, so Π\_ρ[E\_ρ] has a representative F\_ρ with b\_{2,0}(F\_ρ) ≤ 2C₀C₁(1 + |γ|)^{M₁}, jet e^{T²} at ρ, and full-order vanishing at the other zeros. For γ ≥ T₀ + 2 take good heights T₁ ∈ [γ − 2, γ − 1], T₂ ∈ [γ + 1, γ + 2] and R = [−1, 2] × [T₁, T₂]. H = F\_ρ(s − ρ)^m/ζ is holomorphic near R (F\_ρ cancels the other zeros in R, and ζ ≠ 0 on ∂R), and on ∂R, |1/ζ| ≤ π²/6 on σ = 2, |1/ζ| ≤ T₂^A on the horizontal sides, and |ζ(−1 + it)| = |χ(−1 + it)||ζ(2 − it)| ≥ 3/π⁴ on σ = −1, from |χ(−1 + it)|² = π^{−3}y coth(πy)(1/4 + y²) ≥ 1/(4π⁴), y = t/2. So |H| ≤ B\_ρ := 2C₀C₁(1 + |γ|)^{M₁}3^m max(π²/6, π⁴/3, (γ + 2)^A) on R. The jet of H at ρ is e^{T²}Σ\_kc\_{ρ,k}T^k, and Cauchy's estimate on |s − ρ| = 1/2 gives |c\_{ρ,k}| ≤ 2^mB\_ρ, which is polynomial in |γ| because m ≤ C log(2 + |γ|) by (D1).

(c)⇒(d) and (b). V\_ρ = (s − 1)ζ(s)/(s − ρ)^m is entire, and its reciprocal jet v\_ρ^{−1} = (Σ\_kc\_{ρ,k}T^k)(ρ − 1 + T)^{−1} has coefficients at most mC(1 + |γ|)^K. With λ = m + 1 and q\_{ρ,k} = [T^ke^{−λT²}v\_ρ^{−1}]\_{<m}, G\_{ρ,k} = e^{λ(s−ρ)²}V\_ρ·q\_{ρ,k}(s − ρ) is entire, has jet T^k at ρ, vanishes to full order at the other zeros, and, since |e^{λ(s−ρ)²}| ≤ e^{(m+1)(A+1)²}e^{−(m+1)(t−γ)²} and (s − 1)ζ(s) grows polynomially on strips [Ti, Ch. V], satisfies b\_{A,M}(G\_{ρ,k}) ≤ C\_{A,M}(2 + |γ|)^{N\_{A,M}}. As Σ\_ρm\_ρ(2 + |γ|)^{−2} < ∞, F\_P = Σ\_{ρ,k}P\_{ρ,k}G\_{ρ,k} converges absolutely in ℬ for P ∈ Λ\_m, with J[F\_P] = P; so J is an isomorphism, and Σ\_kx\_{ρ,k}[G\_{ρ,k}] = Π\_ρx gives x = Σ\_ρΠ\_ρx absolutely.

(d)⇒(b′)⇒(b). q(Π\_ρx) = q(J^{−1}(Σ\_kx\_{ρ,k}δ\_{ρ,k})) ≤ C(1 + |γ|)^{−N}p\_{M+N}(Jx), and (b′) with (D1) gives absolute convergence. ∎

*Status.* Verified: proved here; found in the audit (*new*), in the form for all multiplicities as sharpened in a referee pass; checks F1–F9, G1–G3. Novelty: not found in the programme or in the literature searched [BT, AKN, BRS]; it is an instance for Meyer's quotient of the classical link between lower bounds at the zeros and interpolation. The L(s, χ) form is an outline, and its standard inputs are not verified here.

**Remark 3.10.** Whether (c) holds is open. A bound |ζ′(ρ)| ≥ c(1 + |γ|)^{−K} at every zero would imply that every zero is simple, which is open; unconditionally at least a proportion 0.4075 of the zeros are simple (0.407511 for simple zeros on the line [PRZZ]; earlier 0.4058 [BCY], as cited in [BHB, §1]). Under RH one expects |ζ′(ρ)|^{−1} ≫ |γ|^{1/3−ε} for infinitely many zeros [MN], so K ≥ 1/3 would be needed. For multiple zeros, whether the leading coefficients suffice is not settled; in the spaces A\_p they do [BT, Theorem 4]. The programme itself uses only finite sums of primary projectors (OMS6, SCL7, GEX2).

### 3.4 Dense families of test functions

For t > 0 put g\_t(s) = e^{ts²}, 𝒩\_S = span{g\_t(s)(n − n^{1−s})/s : n ∈ S} for S ⊂ {2, 3, …}, and ν\_S(x) = #{n ∈ S : log n ≤ x}.

**Proposition 3.11 (Nyman–Beurling in the Fréchet topology).** If (C1) limsup\_R R^{−1}Σ\_{n∈S, log n<R}(1/log n − log n/R²) > 1/(3πt), or (C2) limsup\_X (log X)^{−1}Σ\_{n∈S, log n<X}((log n)^{−2} − (log n)²/X⁴) > 1/(4πt), then 𝒩\_S is dense in ℬ and ξ𝒩\_S is dense in I\_ζ. (C1) holds for every t if limsup ν\_S(R)/R² = ∞ (for example S = {2, 3, …}, or the d-th powers). If ν\_S(x) ∼ κx², (C1) holds exactly when t > 1/(4πκ) and (C2) exactly when t > 1/(8πκ); for S = {2^a3^b}, κ = 1/(2 log 2 log 3), so this family is dense for every t > (log 2)(log 3)/(4π) = 0.06060… ((C1) alone gives 0.12120…). Density for one t implies density for every larger t, and the closure of ξℬ is I\_ζ although ξℬ ⊊ I\_ζ.

*Proof.* 1. Let Λ ∈ ℬ′ vanish on 𝒩\_S, |Λ(F)| ≤ Cb\_{A,M}(F). With K\_w = g\_t(s)(e^w − e^{(1−s)w})/s, a ℬ-valued power series in w, L(w) = Λ(K\_w) is entire, L(0) = 0 and L(log n) = 0 for n ∈ S.

2. For |σ| ≤ A, s = σ + iy and w = u + iv, the bound −ty² + |y||v| ≤ v²/(4t) gives log|L(u + iv)| ≤ v²/(4t) + (1 + A)|u| + M log(2 + |v|) + C′, with 1/(4t) independent of Λ.
3. If L ≢ 0, Carleman's formula in the right half-plane [TiF, §3.7] bounds Σ\_j(1/r\_j − r\_j/R²)cos φ\_j over the zeros r\_je^{iφ\_j} by the arc term, at most (R/(4πt))∫sin²φ cos φ dφ = R/(6πt), the axis term, at most R/(6πt) + O(1), and O(log R). The zeros log n lie on the positive axis and the other zeros add nonnegative terms, so Σ\_{log n<R}(1/log n − log n/R²) ≤ R/(3πt) + O(log R), contradicting (C1).
3′. Apply the same formula to L(z^{1/2}) on |z| ≤ X², whose zeros include (log n)²: by step 2 the arc contributes at most (1 − π/4)/(4πt) + o(1) and the axis, where v² = y/2, at most (log X)/(4πt) + O(1), so Σ\_{log n<X}((log n)^{−2} − (log n)²X^{−4}) ≤ (log X)/(4πt) + O(1), contradicting (C2).

4. So L ≡ 0; since (∂\_w − 1)K\_w = g\_te^{(1−s)w}, Λ(g\_te^{vs}) = 0 for all real v, and the half-Mellin representation of G ∈ ℬ (NJS4.1) gives Λ(g\_tG) = 0. Finally g\_tℬ is dense: with h\_N = e^{ts²}P\_N(−ts²), P\_N the Taylor polynomial of exp, Fh\_N ∈ g\_tℬ, |h\_N| ≤ e^{2tσ²} and h\_N → 1 locally uniformly, so b\_{A,M}(Fh\_N − F) → 0.
5. If Λ vanishes on ξ𝒩\_S, then F ↦ Λ(ξF) vanishes on 𝒩\_S, so Λ = 0 on ξℬ, which is dense in I\_ζ (NCI2).
6. Partial summation gives Σ\_{log n<R}(1/log n − log n/R²) = (4/3)κR + o(R) and Σ\_{log n<X}((log n)^{−2} − (log n)²X^{−4}) = 2κ log X + o(log X) when ν\_S(x) ∼ κx², hence the thresholds; and 𝒩\_S^{(t)} = g\_{t−t′}𝒩\_S^{(t′)} with g\_{t−t′}ℬ dense gives monotonicity in t. ∎

*Status.* Verified: proved here. Proved in the programme for S = {2, 3, …} at NCI2–NCI8 and RSS1–RSS2; the sparse version, conditions (C1) and (C2) and the complete proof were found in the audit (*new*; check Z7). Carleman's formula is used as stated in [TiF, §3.7] (not re-read; its half-plane and angle forms were checked numerically on test functions). The corresponding statement in Noor's Hardy-space setting is equivalent to RH [No]; here it is unconditional, because the topology is different.

**Proposition 3.12 (an infinite set of degrees need not suffice).** If S ⊂ {a^k : k ≥ 1} ∪ F with an integer a ≥ 2 and F finite, the closures of 𝒩\_S in ℬ and of ξ𝒩\_S in I\_ζ have infinite codimension; if F = ∅, the closure of 𝒩\_S lies in I\_D with D = Σ\_{j≠0}[2πij/log a].

*Proof.* Every generator with n = a^k vanishes at s\_j = 2πij/log a, j ≠ 0; point evaluations are linearly independent on ℬ, so for each J the combinations of J + |F| evaluations killing the generators with n ∈ F form a space of dimension ≥ J. In I\_ζ the same holds, since ξ(s\_j) = ξ(1 − s\_j) ≠ 0. ∎ *Status.* Verified: proved here; found in the audit (*new*).

If Φ is entire, Φ(0) = 1 and g\_t(1 − Φ)/s ∈ ℬ, the family {g\_t(n^{1−s} − nΦ)/s : n ≥ 1} is dense in ℬ, its span containing g\_t(1 − Φ)/s and hence 𝒩\_{{2,3,…}} (verified; found in the audit). The statements on tails of Noor's family with the programme's correction C = 8F\_∗ (total in ℬ; annihilator 0 or ℂ·ev₁ according as C(1) ≠ 0 or C(1) = 0) were found in the audit and are not verified here.

### 3.5 Positive forms and receivers

**Lemma 3.13 (transfer-compatible forms).** On H = ℓ²(𝒵, m), ‖x‖² = Σm\_ρ|x\_ρ|², let (T\_nx)\_ρ = n^ρx\_ρ and U\_n = nT\_{1/n}, and let B be a bounded Hermitian form with B(T\_nx, T\_ny) = nB(x, y) for n = 2 and n = 3. Then B(x, y) = Σ\_ρ b\_ρm\_ρx\_ρconj(y\_{ρ^#}) with |b\_ρ| ≤ ‖B‖ and b\_{ρ^#} = conj(b\_ρ), and every such form satisfies the relation for all real n > 0. B is positive semidefinite if and only if b\_ρ = 0 at every off-line zero and b\_ρ ≥ 0 on the line; in particular the bounded positive forms with B(T\_nx, y) = B(x, U\_ny) for all integers n ≥ 1 are exactly Σ\_{Re ρ=1/2}m\_ρc\_ρx\_ρconj(y\_ρ), 0 ≤ c\_ρ ≤ C. The pair {2, 3} may be any n₁, n₂ > 1 with log n₁/log n₂ irrational; a single n allows further entries at (ρ, η) with η − ρ^# ∈ (2πi/log n)ℤ.

*Proof.* On coordinate vectors the relation reads (n^{ρ+η̄−1} − 1)B(ε\_ρ, ε\_η) = 0, and (2πi/log 2)ℤ ∩ (2πi/log 3)ℤ = {0}, so nonzero entries have η = ρ^#; boundedness and symmetry give the rest, and ρ + conj(ρ^#) = 1 the converse. An off-line pair contributes 2m\_ρRe(b\_ρx\_ρconj(x\_{ρ^#})), with eigenvalues ±m\_ρ|b\_ρ|, so positivity forces b\_ρ = 0 there and b\_ρ ≥ 0 on the line; T\_n^{−1} = T\_{1/n} makes the adjoint relation equivalent. ∎

*Status.* Verified: proved here; proved in the programme for positive forms and all n at PTQ4; the classification of all bounded Hermitian forms from n = 2, 3 was found in the audit (*new*). With b ≡ 1 the diagonal of the form is Weil's pairing Ω: two multiplicatively independent integers already force this shape, and positivity is exactly what removes the off-line blocks.

The following are proved in the programme at the labels given and checked in the audit (verified), unless an item says otherwise.

- **Positive transfer forms** on ℬ/I\_ζ are exactly Σ\_{Re ρ=1/2}m\_ρc\_ρF(ρ)conj(G(ρ)) with polynomially bounded c\_ρ ≥ 0 (CFP); before the quotient they are ∫F(1/2 + iλ)conj(G(1/2 + iλ))dμ(λ), μ positive and tempered [Vl], and they descend exactly when supp μ lies in the ordinates of critical zeros (SPF0–SPF10). For every positive μ with polynomially bounded mass on unit intervals, the closure of I\_ζ in L²(μ) under F ↦ F(1/2 + iλ) is L²(ℝ∖Γ, μ), Γ the ordinates of critical zeros (SMC1–SMC4, SMC9).
- **Connes against Meyer.** The map from Q to the inverse limit of Connes' weighted Hilbert quotients [Co] has kernel exactly the classes vanishing on all critical-line jets, so it is injective if and only if RH holds; the loss happens in the Hausdorff quotient (WHR5–WHR10). The prime dilations there have spectrum on |z| = √p (WHR8), and the analogous quotients on the lines Re s = σ, 0 < σ < 1, realize exactly the zeros on those lines and are jointly faithful on Q (VWR2–VWR7).
- **Spectral synthesis.** Finite-rank Riesz–Gaussian operators converge to the identity on Q; closed multiplier submodules are the jet-order submodules; the line and off-line ideals have dense sum (GSP2–GSP6, CTS1–CTS4; read for correctness, not re-derived).
- **Global residue duality.** B\_ζ(F, G) = (2πi)^{−1}(∫\_{Re s=2} − ∫\_{Re s=−1})F(s)G(1 − s)/ζ(s)ds satisfies |B\_ζ(F, G)| ≤ ζ(2)(π^{−1} + 8π/5)b\_{2,1}(F)b\_{2,1}(G) ≈ 8.79 b\_{2,1}(F)b\_{2,1}(G), descends to Q, is nondegenerate with local determinant (m!/ζ^{(m)}(ρ))^m, satisfies B(T\_ax, T\_ay) = aB(x, y) and B(P(L)x, y) = B(x, P(1 − L)y), and is not positive (GZR).
- **The source-pairing identity.** If b₀ ∈ 𝒜 has Mellin transform vanishing at ρ and (L − ρ)b\_ρ = b₀ with L = −u∂\_u, then (Re ρ − 1/2)‖b\_ρ‖²\_{L²(du)} = −Re⟨b\_ρ, b₀⟩, since Re⟨Lb, b⟩ = ‖b‖²/2 (OPD4.2; proved here); it restates RH at ρ as Re⟨b\_ρ, b₀⟩ = 0, and reading it as a Hilbert–Pólya mechanism is an interpretation.
- **Harmonic defect and divisor potential.** The Poisson-swept distribution, with H(b\_†) = 2Σm\_ρ|Re ρ − 1/2|‖b\_ρ‖², descends to Q if and only if there are no off-line zeros (HSW5–HSW6B, OPD5); the compressed translation trace tends to Σ m e^{−|β−1/2||t|}e^{iγt} (FGR0–FGR6); and ℰ\_r(t) = Σ\_ρm\_ρ(r^σ − r^{1−σ})²e^{2t(σ²−γ²)}, zero if and only if RH holds, equals an area integral of (1/2)log|ζ(s)ζ(1 − s̄)| against the Laplacian of an explicit test function plus (r − 1)²(e^{2t} + 1)/2, for a cutoff supported in (−1/2, 3/2) (OZD0–OZD7; the Littlewood-lemma family [BSY, SBM]).

Each of these objects is exact. The positive ones are supported on the critical zeros; those that involve the off-line zeros vanish, or are injective, exactly under RH; and B\_ζ is nondegenerate unconditionally and not positive. Deciding the location of the zeros through any of them therefore requires an input that forces the off-line part to vanish (§8.2).

## 4. The two lines

The author proposed a second line at Re s = −1/2 that mirrors the critical line, built by shifting the whole line as in the Hurwitz flow, and asked for the anomaly, chirality and holonomy language of that picture to be made exact. This section gives the exact objects; the matching of the author's terms with them is a proposal (§9.8). No result assumes RH, and Proposition 4.10 states its GRH hypotheses. Note s^# = T₁(A(s)). The results were found in the audit (*new*) unless a status line says otherwise.

### 4.1 The first Hurwitz jet and the mirror set

**Theorem 4.1 (the first Hurwitz jet).** Let a > 0. (a) ∂\_aζ(s, a) = −sζ(s + 1, a) for s ≠ 1 (at s = 0 the right side is its holomorphic extension), and ∂\_a^mζ(s, a) = (−1)^m(s)\_mζ(s + m, a), both sides entire in s. (b) sζ(s + 1, a) is entire and equals 1 at s = 0. (c) The zero divisor of the first jet −sζ(s + 1, a) is exactly div ζ(·, a) − 1, with multiplicities, in the whole plane; that of the m-th jet is (div ζ(·, a) − m) + [0] + [−1] + … + [2 − m], the last m − 1 zeros simple and distinct from the shifted ones. At a = 1 the zeros of the first jet in −1 < Re s < 0 are exactly 𝒵 − 1, and those of the m-th jet in −m < Re s < 1 − m are exactly 𝒵 − m. (d) ζ has no zero on 𝒵 − 1.

*Proof.* (a) Differentiate termwise on Re s > 1 and extend by joint analyticity (Euler–Maclaurin); (s)\_m vanishes simply at 1 − m, where ζ(s + m, a) has a simple pole, and ζ(s, a) − 1/(s − 1) is entire. (b) sζ(s + 1, a) = 1 + s(ζ(s + 1, a) − 1/s). (c) Off s = 0 the factor −s is a unit; at 1 − m a simple zero meets a simple pole of residue 1, and at −j, 0 ≤ j ≤ m − 2, the other factor is ζ(m − j, a) > 0; at a = 1, div ζ = 𝒵 + Σ\_{k≥1}[−2k]. (d) ζ has no zeros in −1 < Re s < 0. ∎

*Status.* Verified: proved here; the t-derivative at ρ\_k − 1 is below 4·10⁻²⁹ for k = 1, 2, 3, and check Z1 finds the jet vanishing at s₀ − 1 for the zero s₀ = 1.40778804 + 23.32798775i of ζ(·, 2). Part (a) on Re s > 1 is the programme's shift-flow theorem.

The Hurwitz flow does not translate the zero set; what vanishes on the translate, at every time of the flow, is its first jet. Theorem 4.2 uses the functional equation of ζ and does not extend to other sheets: at a = 1/2, s₁ = 2πi/log 2 is a zero of ζ(s, 1/2) = (2^s − 1)ζ(s), while ζ(1 − s̄₁, 1/2) = ζ(1 + 2πi/log 2) ≠ 0, so the zero set of that sheet is not symmetric under s ↦ 1 − s̄. Part (d) is proved from the functional equation and is not claimed for other sheets.

**Theorem 4.2 (the shifted set is the mirror set).** A(𝒵) = 𝒵 − 1 with multiplicities, unconditionally, and A(ρ) = ρ^# − 1. Since A(s) − (s − 1) = 1 − 2Re s, A(ρ) = ρ − 1 exactly when Re ρ = 1/2, so RH ⟺ A(ρ) = ρ − 1 for every nontrivial zero.

*Proof.* −ρ̄ = (1 − ρ̄) − 1 with 1 − ρ̄ ∈ 𝒵 of the same multiplicity. ∎ *Status.* Verified: proved here.

So the author's two operations produce the same line: as sets the mirror and the shift agree unconditionally, as maps on the zeros they agree exactly under RH, and ζ does not vanish at any point of 𝒵 − 1.

**Proposition 4.3 (bounded dilation-equivariant maps between weights).** Let H\_σ = L²((0, ∞), u^{2σ−1}du) and U\_af(u) = f(au). If σ ≠ σ′, every bounded K : H\_σ → H\_{σ′} with KU\_{a₀} = U\_{a₀}K for one a₀ ≠ 1 is zero. The inversion f ↦ f(1/u) maps H\_σ isometrically onto H\_{−σ}, acting on Mellin transforms by s ↦ −s.

*Proof.* U\_a = a^{−σ}V\_a with V\_a unitary, so ‖Kf‖ ≤ a^{σ′−σ}‖K‖‖f‖ for a = a₀^k, k ∈ ℤ, and k → ±∞ gives Kf = 0. ∎ *Status.* Verified: proved here. Boundedness is needed: the identity on C\_c^∞(0, ∞) is a nonzero closable densely defined operator H\_{1/2} → H\_{−1/2} commuting with every U\_a.

### 4.2 The two centres of the explicit formula

With (g₁ ⋆ g₂)(x) = ∫g₁(y)g₂(x/y)dy/y and ĝ the Mellin transform, use Weil's explicit formula in Bombieri's form [Bo].

**Proposition 4.4 (two centres).** (a) With g∗(x) = x^{−1}conj(g(1/x)) and h = g ⋆ g∗, ĥ(s) = ĝ(s)conj(ĝ(1 − s̄)), both sides of the explicit formula are real, an on-line zero contributes m\_ρ|ĝ(ρ)|² ≥ 0, and an off-line pair contributes 2m\_ρRe(ĝ(ρ)conj(ĝ(ρ^#))), an indefinite form with eigenvalues ±m\_ρ. (b) With g^♭(x) = conj(g(1/x)), ĥ(s) = ĝ(s)conj(ĝ(−s̄)), the prime term has imaginary part Σ\_nΛ(n)(1 − 1/n)Im h(n), and the sum over zeros is not real in general.

*Proof.* The substitution y = 1/x; in (a), h(n) + h(1/n)/n = 2Re h(n), and in (b), h(n) + conj(h(n))/n. ∎ *Status.* Verified: proved here; both sides computed for g(x) = exp(−(log x)²/2 + (i/2)log x − iγ₁log x) (centre 1/2: 2π to 4·10⁻¹⁵; centre 0: 2πe^{i/2} to 1.6·10⁻¹²).

So a real partner pairing selects the centre 1/2, and with it the only possible source of negativity is the hyperbolic block of an off-line pair; by Weil's criterion a negative value exists if and only if RH fails. The same substitution shows that the two normalizations of running the clock backwards, g ↦ conj(g(1/u)) and g ↦ conj(g(1/u))/u, have Mellin shadows s ↦ −s̄ and s ↦ 1 − s̄.

### 4.3 The two-line product and the chiral form

**Proposition 4.5.** G(−s̄) = conj(G(s)), and G(it) = |ξ(1 + it)|²/16 > 0 for real t (since ξ(it) = conj(ξ(1 + it)) and ζ ≠ 0 on Re s = 1). *Status.* Verified: proved here; checked to 10⁻³⁰.

The maps id, A, P (# on 𝒵 and s ↦ −1 − s̄ on 𝒵 − 1) and T = AP form a Klein four-group preserving 𝒵 ⊔ (𝒵 − 1). An on-line zero has orbit {ρ, ρ − 1}, an off-line zero the four points {ρ, ρ^#, ρ^# − 1, ρ − 1} (the author's doublet); the loop across by A and back by T^{−1} has holonomy #, trivial exactly at on-line zeros; and the zeros of G in −1/2 < Re s < 1/2 (the bulk) are the zeros with Re ρ < 1/2 and their mirrors, so the bulk is empty if and only if RH holds (verified; elementary). For f on 𝒵 ⊔ (𝒵 − 1) put Q\_A(f) = Σ\_wm\_wf(w)conj(f(Aw)), the chiral cross form; Q\_A and Ω are real.

**Proposition 4.6 (the chiral form and Weil's form).** Let f be finitely supported, or the restriction of an element of ℬ, and let u(ρ) = (f(ρ) + f(ρ − 1))/2 and v(ρ) = (f(ρ) − f(ρ − 1))/2 be its T-even and T-odd parts. Then Q\_A(f) = 2Ω(u) − 2Ω(v), and:

- (a) A has no fixed point, so Q\_A is an orthogonal sum of hyperbolic planes, of signature (n, n) on data supported on n pairs {w, Aw}, whether or not RH holds;
- (b) Ω(u) = Σ\_{on-line}m\_ρ|u(ρ)|² + Σ\_{off-line pairs}2m\_ρRe(u(ρ)conj(u(ρ^#))), so Ω ≥ 0 on all finitely supported u exactly when every zero is on the line;
- (c) the T-even and T-odd data V₊, V₋ are Q\_A-orthogonal, with Q\_A = 2Ω on V₊ and −2Ω on V₋; on T-even data supported on a finite #-closed set with n\_on points on the line and n\_pairs off-line pairs the signature is (n\_on + n\_pairs, n\_pairs); under RH, V₊ is maximal positive and V₋ maximal negative, and if RH fails V₊ contains a negative direction.

*Proof.* Aρ = ρ^# − 1 and A(ρ − 1) = ρ^#, so Q\_A(f) = Σ\_ρm\_ρ[f(ρ)conj(f(ρ^# − 1)) + f(ρ − 1)conj(f(ρ^#))]; substituting f = u + v on 𝒵 and f = u − v on 𝒵 − 1, the cross terms cancel in pairs. (a) Aw = w means Re w = 0, where G ≠ 0. (b) # fixes on-line zeros and pairs the others; take u = 1 at ρ and −1 at ρ^#. (c) For T-even u and T-odd v, Q\_A(u, v) = Σ\_ρm\_ρu(ρ)[−conj(v(ρ^#)) + conj(v(ρ^#))] = 0; on-line points give positive squares and off-line pairs hyperbolic planes; under RH, Ω(u) = Σm|u|², and a subspace strictly containing V₊ contains a nonzero x ∈ V₋. ∎ *Status.* Verified: proved here; checks B1–B5.

**Corollary 4.7 (an RH criterion in two-line terms).** For k ∈ ℬ put f\_k(s) = F\_∗(s + 1)F\_∗(s − 1)k(s) + F\_∗(s + 2)F\_∗(s)k(s + 1). Then f\_k is T-even on the zero set, with u(ρ) = F\_∗(ρ + 1)F\_∗(ρ − 1)k(ρ), and RH ⟺ Q\_A(f\_k) ≥ 0 for every k ∈ ℬ.

*Proof.* F\_∗(ρ) = 0 and F\_∗(ρ ± 1) ≠ 0; the programme's sections realize any finitely supported values of k on 𝒵; apply Proposition 4.6(b). ∎ *Status.* Verified: proved here; equivalent to RH by construction, since its test data localize at the zeros.

Theorem 4.2 and Proposition 4.6 hold for every primitive Dirichlet L-function, with its zeros Z\_χ and GRH for χ, since Λ(1 − s̄, χ) = W(χ)conj(Λ(s, χ)) makes # permute Z\_χ (the standard inputs for L(s, χ) are not verified here); Corollary 4.7 is specific to ζ. Q\_A(f) is Weil's explicit-formula functional of G applied to f·f^A, f^A(s) = conj(f(−s̄)), with prime coefficients Λ(n)(1 + n^{−1}) in −G′/G.

### 4.4 Counting in the two-line system

**Proposition 4.8 (parity).** For T > 0 not an ordinate, (−1)^{N(T)} = (−1)^{N₀(T)} = −sgn Z(T), with no simplicity assumption. The two-line count n\_G(T) = 2N₀(T) + 4P(T) vanishes mod 2, and i^{n\_G(T)} = (−1)^{N₀(T)}; both are functions of N₀(T) alone, and mod 8, n\_G gives P(T) mod 2 only once N₀(T) mod 4 is known ((N₀, P) = (0, 1) and (2, 0) both give n\_G = 4).

*Proof.* ξ(1/2 + it) = −(1/2)(1/4 + t²)π^{−1/4}|Γ(1/4 + it/2)|Z(t); ξ(1/2) > 0, and ξ(1/2 + it) changes sign exactly at on-line zeros of odd order, and off-line zeros come in pairs of equal height. ∎ *Status.* Verified: proved here; checked at eight heights up to 1000.

**Proposition 4.9 (the holonomy index is Turing's).** With P(T) the number of zeros with 0 < γ ≤ T and Re ρ < 1/2,

  I(T) := (N(T) − V(T))/2 = P(T) + Σ\_{Re ρ=1/2, 0<γ≤T}⌊m\_ρ/2⌋.

So I(T) ≥ 0, with equality exactly when every zero up to height T is on the line and simple; a positive value arises from off-line pairs and from multiple on-line zeros alike.

*Proof.* Off-line pairs contribute 2P(T) to N(T), and Z changes sign exactly at on-line zeros of odd order, so V(T) = Σ\_{on-line}(m\_ρ − 2⌊m\_ρ/2⌋). ∎ *Status.* Verified: proved here; checks D1–D4 and R5 (N = V = 29 at T = 100, N = V = 108 at T = 250).

I(T) is computed from boundary data (N(T) = θ(T)/π + 1 + S(T) by the argument principle, V(T) from the line), and I(T) = 0 is exactly what verifications of RH by Turing's method [Tu] establish up to a height; RH is verified up to 3·10¹² [PT]. I(T) = 0 for all T is RH together with the simplicity of all zeros.

**Proposition 4.10 (the second line and prime races).** For primitive χ mod q, the prime coefficients of −G\_χ′/G\_χ, G\_χ(s) = Λ(s, χ)Λ(s + 1, χ), are Λ(n)χ(n)(1 + n^{−1}). For every modulus q and classes a ≢ b prime to q (and races among r classes), the two-line races differ from the one-line races by convergent series, which vanish after Rubinstein–Sarnak's normalization; so they have the same limiting logarithmic distributions (under GRH) and logarithmic densities (under GRH and linear independence) [RS, Dev], for example δ(4; 3, 1) ≈ 0.9959.

*Proof.* In Σ\_{p≤x}(1\_{p≡a} − 1\_{p≡b})log p/p = φ(q)^{−1}Σ\_{χ≠χ₀}(χ̄(a) − χ̄(b))Σ\_{p≤x}χ(p)log p/p the principal character cancels, and each inner series converges [Da, Ch. 20]. ∎ *Status.* Verified: proved here; checks C1–C3 and for q ∈ {3, 5, 7, 8, 12}, up to 10⁷.

### 4.5 The separator

**Lemma 4.11 (the separator with matched rates).** Let G ∈ ℬ have zero divisor D₊ ⊔ D₋ with D₊ ⊂ {Re s > 0}, D₋ ⊂ {Re s < 0}. Suppose that, with r(t) = ε(1 + t²)^{−N}, (a) |G(x + it)| ≤ C\_A(1 + |t|)^{k\_A}e^{−α|t|} on every strip |x| ≤ A, and (b) G has no zeros in the corridor 𝒦 = {|x| ≤ r(t)}, where |G| ≥ c(1 + |t|)^{−K}e^{−α|t|}. Then there is an entire E of polynomial growth on vertical strips with E − 1 vanishing to full order on D₊ and E on D₋, so ℬ/(I\_{D₊} ∩ I\_{D₋}) ≅ ℬ/I\_{D₊} ⊕ ℬ/I\_{D₋} topologically, via ([f], [g]) ↦ [Ef + (1 − E)g], commuting with s and every a^s.

*Outline.* With a cutoff χ(x + it) = η(x/r(t)) and h = ∂̄χ/G, solve ∂̄u = h by u = π^{−1}∫e^{(s−w)²}(s − w)^{−1}h(w)dA(w); then |u| ≤ C\_Ae^{α|t|}(1 + |t|)^{2N+K}, and E = χ − Gu works because the two exponential rates cancel exactly. *Status.* Verified: proved in the programme for ζ at GSL4–GSL5 and checked in the audit, which stated it with general constants; standard ∂̄ technique. For ζ, G = F\_∗(s)F\_∗(s + 1) and α = π/2: its only exponential factor, 1/cos(πs/2), has the same size on every vertical line.

**Proposition 4.12 (the separator for every primitive Dirichlet L-function).** Let χ be primitive mod q ≥ 3 with χ(−1) = (−1)^a, Λ\_χ(s) = (q/π)^{(s+a)/2}Γ((s + a)/2)L(s, χ), and I\_χ, I\_{χ,−} the ideals of full-order vanishing on Z\_χ and Z\_χ − 1. Then ℬ/(I\_χ ∩ I\_{χ,−}) ≅ ℬ/I\_χ ⊕ ℬ/I\_{χ,−} equivariantly.

*Proof.* We check Lemma 4.11 for G\_χ(s) = Λ\_χ(s)Λ\_χ(s + 1) with α = π/2, from the functional equation Λ\_χ(s) = W(χ)Λ\_{χ̄}(1 − s), L(1 + it, χ) ≠ 0 and Stirling's formula [Da]. Partial summation against periodic antiderivatives gives polynomial growth, so Λ\_χ ∈ ℬ, and Z\_χ ⊂ {0 < Re s < 1}. By the functional equation, G\_χ(s) = W(χ)(q/π)^{1+a}Γ((1 + a − s)/2)Γ((1 + a + s)/2)L(1 − s, χ̄)L(1 + s, χ), whose Gamma product, π/cos(πs/2) or (πs/2)/sin(πs/2), has modulus at most C\_A(1 + |t|)e^{−π|t|/2} on strips and at least ce^{−π|t|/2} in the corridor. The inequality ζ(σ)³|L(σ + it, χ)|⁴|L(σ + 2it, χ²)|² ≥ 1 for σ > 1 gives |L(1 + δ + it, χ)| ≥ cδ^{3/4}(1 + |t|)^{−1/2}, hence |L(1 + x + it, χ)| ≥ c(1 + |t|)^{−5} for |x| ≤ c(1 + |t|)^{−6}; and G\_χ(it) ≠ 0 near t = 0. So the lemma applies with r(t) = ε(1 + t²)^{−3}. ∎

*Status.* Verified: proved here; the matched rates checked on Re s = 0 for two characters. Novelty: not searched.

The inputs of this proof are the functional equation, polynomial growth, Stirling's formula and zero-freeness on Re s ≥ 1, which is where the Euler product is used; its conclusion holds for every configuration of zeros in the open strip. For the Davenport–Heilbronn function, which has no Euler product, the hypotheses of Lemma 4.11 fail on every vertical line, since it has zeros with Re s > 1 [SW] and hence with Re s < 0; whether its splitting fails is open (Question 4). The same argument gives the splitting for every Dedekind zeta function, with α = nπ/2 (checked for four fields; the standard inputs are not verified here). The derived separation RHom(Q, Q₊) ≃ 0 ≃ RHom(Q₊, Q), Q₊ = ℬ/I₊ with jets at 𝒵 + 1, is the vanishing of Ext for a central element acting as 0 and as 1, and ℬ itself does not split along the two lines, Q₊ being torsion and ℬ torsion-free (GMS; verified).

### 4.6 The defect ratio

For r > 1 the programme's defect has eigenvalue d\_r(ρ) = r^{ρ̄} − r^{1−ρ} = conj(r^ρ − r^{ρ^#}) at a zero: a zero minus its reflected partner.

**Lemma 4.13.** For r ≠ t > 1, 0 < β < 1, β ≠ 1/2, x = β − 1/2: |d\_r(ρ)/d\_t(ρ)| = √(r/t)·sinh(x log r)/sinh(x log t), strictly increasing in |x| on (0, 1/2) if r > t and decreasing if r < t, with values filling the open interval between √(r/t)·log r/log t and (r − 1)/(t − 1).

*Proof.* r^β − r^{1−β} = 2√r sinh(x log r), and c ↦ c coth(cx) is increasing for x > 0. ∎ *Status.* Verified: proved here; it sharpens the programme's AST6.2; a statement about admissible positions for any β. The programme's further realization of the two lines, paired with their shifts, as the two sheets of a connected double cover of the equator of ℂP¹ with deck transformation the central −1 of SU(2) was found in the audit and is not verified here.

## 5. Weights: Deligne's mechanism against the programme

A large part of the programme, including a full reader of Deligne's *La conjecture de Weil. II* [De], asks which steps of Deligne's proof have analogues for ζ. The weight of α relative to a prime p is w(α) = 2 log|α|/log p; a zero ρ enters the local data as the eigenvalue p^ρ, of weight 2Re ρ. For a conjugation-stable finite set S of zeros the tensor-power trace (Σ\_{ρ∈S}m\_ρn^ρ)^k (TWC7) is real, so its even powers are nonnegative: this is Deligne's positivity step (Weil II 1.5; DP4 of the programme's Deligne reader).

### 5.1 Positivity of even tensor powers

**Proposition 5.1 (the exponent data return the largest real part).** Let S be a finite set of complex numbers with positive integer weights m\_ρ, β\_max = max Re ρ, k ≥ 1, and D\_S^{(k)}(s) = Σ\_{n≥1}(Σ\_ρm\_ρn^ρ)^kn^{−s}. Then D\_S^{(k)} = Σ\_wc\_wζ(s − w) over the distinct sums w of k elements of S, with every c\_w > 0, and its abscissa of convergence and of absolute convergence is exactly 1 + kβ\_max. For even k and conjugation-stable S (m\_ρ̄ = m\_ρ) the coefficients are nonnegative and 1 + kβ\_max is a pole with positive residue. So a bound 1 + k/2 + C on the abscissa, uniform in k, holds if and only if β\_max ≤ 1/2.

*Proof.* Expanding the power, each ζ(s − w) converges absolutely on Re s > 1 + Re w, and convergence on Re s > σ₁ with σ₁ < 1 + kβ\_max would make Σc\_wζ(s − w) holomorphic there, although it has a pole with residue c\_w > 0 at each 1 + w (the w are distinct), among them 1 + kρ with Re ρ = β\_max; for even k, kβ\_max is a sum of k/2 copies each of ρ and ρ̄. ∎ *Status.* Verified: proved here; found in the audit (*new*), in every degree and for every finite S (check Z5).

So the exponent data return max Re ρ in every degree, positive or not; positivity of even powers (Landau's theorem) places a pole at the real point, and a bound 1 + k/2 + C, being equivalent to max Re ρ ≤ 1/2, has to come from another source. For odd k the real point need not be a pole (S = {0.7 ± 10i, 0.3 ± 10i}, k = 3: the rightmost poles are 3.1 ± 10i and 3.1 ± 30i). Deligne's next step (Weil II 1.5; DP5) is exactly an independent bound of the form k + 1 + C, from the H²\_c of a fixed curve.

**Proposition 5.2 (the average weight of an off-line quartet).** Let ρ be a zero of multiplicity m and V\_ρ the span of the jet blocks of the distinct points among ρ, ρ̄, 1 − ρ, 1 − ρ̄. Off the line V\_ρ has rank 4m and det(W\_p | V\_ρ) = p^{2m}; on the line (1 − ρ = ρ̄) it has rank 2m and determinant p^m. In both cases the weight of the determinant divided by the rank is 1, whatever Re ρ is, while the constituent weights 2Re ρ and 2(1 − Re ρ) differ from 1 exactly when ρ is off the line. *Proof.* p^{(ρ+ρ̄+(1−ρ)+(1−ρ̄))m} = p^{2m} and p^{(ρ+ρ̄)m} = p^m. ∎ *Status.* Verified: proved here; proved in the programme at DW8.12 (the on-line case corrected in the audit; check Z6).

Deligne's Théorème 1.5.1 turns a pure determinant weight of each constituent into purity. For the quartet the four characters are separate constituents, with determinant weights 2Re ρ and 2(1 − Re ρ), and 1.5.1 applies with a conclusion that holds for every value of Re ρ; if they formed one ι-real constituent of rank 4, its determinant weight would be 1 and 1.5.1 would force Re ρ = 1/2. The input this route needs is one that forces the constituents onto the average weight 1, equivalently a pole bound at k + 1 + C uniform in k: (a) a square with a Künneth-type map H¹ ⊗ H¹ → H² and an auxiliary object with discrete weights, or (b) a cohomological source for the uniform bound, which on the finite data is equivalent to max Re ρ ≤ 1/2 and so has to be independent, as the H²\_c of a fixed curve is in Weil II §3.2. TWC9 and TWC11 state that no construction of the programme has yet been assigned the fixed-curve denominator and that its computations do not rule one out.

### 5.2 An algebraic purity criterion

Let V be finite-dimensional, N nilpotent and F invertible with FNF^{−1} = Q^{−1}N, |Q| ≠ 1, w(α) = 2 log|α|/log|Q|, M the monodromy filtration of N, and F^∨ = (F^{−1})^t, N^∨ = −N^t on V^∨.

**Proposition 5.3 (the core of Weil II 1.8.4).** These are equivalent: (a) for every i, all eigenvalues of F on Gr^M\_iV have weight β + i; (b) all eigenvalues of F ⊗ F on ker(N ⊗ 1 + 1 ⊗ N) have weight ≤ 2β, and all eigenvalues of F^∨ ⊗ F^∨ on ker(N^∨ ⊗ 1 + 1 ⊗ N^∨) have weight ≤ −2β. The bounds on ker N for V and V^∨ alone do not suffice.

*Proof.* Inputs: Weil II (1.6.6), (1.6.9), (1.6.14), with the twist of (1.6.14.3) read as −(i + j)/2 (§5.4). (a)⇒(b): the monodromy filtration of N ⊗ 1 + 1 ⊗ N is Σ\_{a+b=k}M\_a ⊗ M\_b, so its Gr\_k has weight 2β + k, and the kernel lies in M₀; dually Gr\_i(V^∨) ≅ (Gr\_{−i}V)^∨. (b)⇒(a): for an eigenvalue α on the primitive part P\_{−j} with eigenvector N^jy, y ∈ Gr\_j (so Fy = αQ^jy), the vector Σ\_{s=0}^{j}(−1)^sN^sy ⊗ N^{j−s}y ∈ Gr₀(V ⊗ V) is nonzero, is killed by N ⊗ 1 + 1 ⊗ N, and has eigenvalue α²Q^j, so 2w(α) + 2j ≤ 2β; dually w(α) ≥ β − j; so P\_{−j} has weight β − j, and Gr\_i ≅ ⊕\_jP\_{−j}(−(i + j)/2) has weight β + i. For the last claim, V = ⟨v⟩ ⊕ ⟨v₁, v₀⟩ with Nv₁ = v₀, Nv₀ = Nv = 0, Fv = av, Fv₁ = bv₁, Fv₀ = (b/Q)v₀, w(a) = β and w(b) = c + 1: the kernel bounds hold for β − 1 ≤ c ≤ β + 1, (a) only for c = β, and v₁ ⊗ v₀ − v₀ ⊗ v₁ has weight 2c. ∎

*Status.* Verified: proved here and checked on 142 random models. (b)⇒(a) is the algebra of Deligne's proof (Weil II p. 176); the converse and the example were added in the audit; the equivalence is not claimed new. In Weil II, (b) comes from geometry (Lemme 1.8.1). An operator commuting with N, such as the programme's counting operators W\_p and C\_b, has the same eigenvalues on Gr\_i and Gr\_{−i}, so its weights are of the form β + i only if N = 0; the ramification operator P\_b satisfies NP\_b = bP\_bN and has no eigenvector on its space (verified; found in the audit).

### 5.3 Three lemmas from Weil II §2

**Lemma 5.4 (concentration, with the outside term).** Let K be a compact group, ϑ an irreducible character of degree d\_ϑ, V ⊂ K with Re χ\_ϑ ≥ (1 − e₁)d\_ϑ on V, and ρ₀ ≠ 0 an integer combination of characters with ∫\_{K∖V}|ρ₀|² ≤ e₂∫|ρ₀|²; write ρ₀ = ρ⁺ − ρ⁻ with genuine ρ^± without common constituents and ρ = ρ⁺ + ρ⁻. Then [ρρ̄ : ϑ] ≥ ((1 − e₁)(1 − e₂) − e₂)d\_ϑ[ρρ̄ : 1], with [ρρ̄ : 1] = ∫|ρ₀|², sharp in e₂. The printed choice ε₁ + ε₂ < ε in the proof of Weil II 2.1.7 does not give Deligne's inequality; ε₁ + 2ε₂ < ε does.

*Proof.* ρρ̄ = ρ₀ρ̄₀ + 2(ρ⁺ρ̄⁻ + ρ⁻ρ̄⁺), and [ρ₀ρ̄₀ : ϑ] = ∫|ρ₀|²Re χ\_ϑ, whose part over V is at least (1 − e₁)(1 − e₂)d\_ϑ∫|ρ₀|² and whose part off V is at least −e₂d\_ϑ∫|ρ₀|². On ℤ/2 with ϑ = sgn, V = {e} and ρ₀ = 23 + 9·sgn: ∫|ρ₀|² = 610, off-V fraction 98/610 < 0.18, and with ε₁ = 0.01, ε₂ = 0.18, ε = 0.2 one gets [ρρ̄ : sgn] = 414 < 0.8·610 = 488. ∎ *Status.* Verified: proved here; found in the audit (*new*), the repair being the programme's Deligne reader's (DB0, DB5); checks B1–B4.

**Lemma 5.5 (integer positivity; Weil II 2.1.5–2.1.6).** If ν : K̂ → ℝ has ν(1) = 1, ν(ϑ) ≤ 0 for ϑ ≠ 1 and ν(ρρ̄) ≥ 0 for every genuine ρ, then Σ\_{ϑ≠1}d\_ϑ(−ν(ϑ)) ≤ 1 (Lemma 5.4 with Peter–Weyl, letting e → 0). For integer-valued ν with ν(ϑ̄) = ν(ϑ), at most one ϑ ≠ 1 has ν(ϑ) < 0, a quadratic character with ν(ϑ) = −1, and on ℤ/2, ν(sgn) = −1 satisfies every hypothesis; on ℤ/3 with ν(ϑ) = ν(ϑ²) = −x, positivity holds if and only if x ≤ 1/2, since ν(ρρ̄) = a² + b² + c² − 2x(ab + bc + ca). *Status.* Verified: proved here; found in the audit (*new*). In Weil II §2.2 the exception is removed with a double cover; for ζ (G = ℝ, K = {0}, Deligne's example 2.1.9) there is no nontrivial quadratic character, and the method gives exactly ζ(1 + it) ≠ 0.

**Lemma 5.6 (nonnegative power sums).** If a\_j ∈ ℂ^× and real δ\_n with limsup max(δ\_n, 0)^{1/n} ≤ D satisfy δ\_n − Σ\_ja\_j^n ≥ 0 for all n, then max|a\_j| ≤ D, since Dirichlet's simultaneous approximation makes the largest terms nearly real and positive for infinitely many n; for a curve over 𝔽\_q, #X(𝔽\_{q^n}) ≥ 0 alone gives |α\_j| ≤ q. Hence (**Corollary 5.7**) the zeta function of a smooth projective geometrically connected curve over 𝔽\_q has a simple pole at s = 1 by the point counts alone, since an eigenvalue q on H¹ would make the counts bounded. *Status.* Verified: proved here; Lemma 5.6 found in the audit (*new*); Corollary 5.7 proved in the programme at DBC7.

### 5.4 Misprints in the printed Weil II

The programme's Deligne reader flagged these displays as defects of its transcription; the audit found them in print (the numdam scan, pp. 150–203). None affects a conclusion of Weil II.

| Display | Page | Printed | Meant |
|---|---|---|---|
| (1.3.10)(iv) | 160 | centre onto a finite subgroup of ℤ | a subgroup of finite index |
| (1.6.7) | 166 | exception i ≠ d | i ≠ −d |
| (1.6.13) | 169 | k − 2i − 2 ≥ k ≥ 2j − k | k − 2i − 2 ≥ −k ≥ 2j − k |
| (1.6.14.3) | 170 | P\_{−j}((i + j)/2) | P\_{−j}(−(i + j)/2) |
| (1.7.5), filtration | 171 | M′\_i = ∏\_{j<i}V′\_j | j ≤ i |
| (1.7.5), coefficient | 171 | μ = λ/(1 − q^n) | μ = λ/(1 − q^{−n}) |
| (2.1.1) | 187 | period 2πi log q | 2πi/log q |
| proof of 2.1.7 | 191 | ε₁ + ε₂ < ε | ε₁ + 2ε₂ < ε |
| 2.2.8(i) | 195 | weight 2ℛ(τ) | −2ℛ(τ) |
| (3.1.3.3) | 199 | Kummer class of uv^{−1} a generator | twice a branch class |
| proof of 3.2.1 | 200 | F^∨(−1) | F^∨(1) |
| (3.2.7.1) | 202 | H¹ | H¹\_c |
| proof of 3.2.12 | 203 | w ≤ β + i in a weight-0 proof | w ≤ i |

*Status.* Verified against the printed pages; found first by the programme's Deligne reader. A quick errata search for the displays of §1 found none published; no novelty is claimed.

## 6. Further results

**Proposition 6.1 (the two poles differ in kind).** For even Schwartz h with ℳ\_Sh(s) = ∫₀^∞h(v)v^{s−1}dv, 2ζ(s)ℳ\_Sh(s) = E\_h(s) + ĥ(0)/(s − 1) − h(0)/s with E\_h entire (Poisson summation): the pole at 0 is the lattice's n = 0 term, with residue −h(0) for every lattice cℤ, and the pole at 1 is the dual lattice's, with residue (∫h)/c, so one counts a point and the other measures a density. If h(v) = κv^α + O(v^{α+1}) at 0, ℳ\_Sh has a pole at −α with residue κ, and the trivial zeros cancel the poles of the smooth even model at −2, −4, …; the conditions h(0) = 0 = ∫h remove exactly the two poles, the pole at 1 carrying the average and each zero an oscillation. *Status.* Verified: proved here; found in the audit; checked to 10⁻³¹; classical in content.

In the programme the object at the point where the nonzero numbers stop is τ. By the local statement of Proposition 6.1 (a pole at −α read from the behaviour κv^α of h at 0), a pole at τ would be computed from a local model of the test functions at τ, which the programme has not specified (Question 7). Reading the residue at 0 as presence without an exchanged label (0 = −0 is the only non-free orbit of ±1) is a proposed typed map, not an identification with τ, since the integer 0 has even parity. The author places τ at the pivot of the swing between 0 and 1; on the zeta side that is the reflection s ↦ 1 − s̄ about 1/2, where RH reads ρ^# = ρ, and centring at 0 differs from it by exactly one shift, s^# = T₁(A(s)).

**Lemma 6.2 (the winding at the zeros).** For every nontrivial zero ρ = σ + iγ, λ\_ρ = e^{−2πiρ} has |λ\_ρ| = e^{2πγ}, is a negative real number if and only if σ = 1/2, and satisfies |1/(λ\_ρ − 1) + 1\_{γ<0}| ≤ 1/(e^{2π|γ|} − 1) < 2.7·10⁻³⁹ (as |γ| ≥ 14.1347…). *Status.* Verified: direct computation; found in the audit.

**Lemma 6.3 (escape under ramification).** Let Z be any set with 0 < Re ρ < 1 and a > 1 real. Then {k ≥ 0 : a^kρ ∈ Z} is finite, no nonempty S ⊂ Z has aS ⊂ S, and only points with Re ρ < 1/a return. If a ≥ 2 and Z = 1 − Z̄, no reflected pair returns together; for 1 < a < 2 one can (a = 3/2, ρ = 0.55 + i). Two points collide, aρ = a′ρ′, only if ρ/ρ′ = a′/a > 0, which is impossible for distinct points of the critical line. *Proof.* Re(a^kρ) = a^kRe ρ < 1, and Re ρ < 1/a and 1 − Re ρ < 1/a are incompatible for a ≥ 2. ∎ *Status.* Verified: proved here; found in the audit. So the programme's iterated- and reflected-return theorems (BRC, GJN, GJNR) hold for every divisor in the open strip with their other hypotheses.

**Proposition 6.4 (every failure of RH is detectable).** Let T be a recursively axiomatized theory that proves every true Σ₁ sentence and proves that an explicit Turing machine M halts if and only if RH fails (the 744-state machine of Matiyasevich and O'Rear [Aa, Theorem 9], or any machine searching for a counterexample to a Π₁ form of RH [DMR]; ZFC is an example). If RH is false, T ⊢ ¬RH; so if RH is independent of T it is true. If T is Σ₁-sound, then RH ⟺ T ⊬ ¬RH ⟺ Con(T + RH). *Proof.* If RH fails, M halts, a true Σ₁ sentence that T proves; if RH holds and T ⊢ ¬RH, then T proves the false Σ₁ sentence that M halts. ∎ *Status.* Verified: proved here; derived in the audit from the author's argument; standard logic. So the absence of a detectable failure (the consistency of T + RH) implies RH, and every failure has a finite certificate; for Σ₁-sound T this absence is equivalent to RH, and a consistent T does not prove Con(T + RH) (Gödel).

**Lemma 6.5 (Keller maps give incompressible polynomial flows).** If F : ℝⁿ → ℝⁿ is polynomial with det DF ≡ c ≠ 0, V is a C¹ field and U = DF^{−1}(V ∘ F), then div U = (div V) ∘ F (by the Piola identity for adj(DF)), U is polynomial if V is, F maps integral curves of U to those of V, and for a polynomial automorphism U is complete if and only if V is. For the map of Alpöge's counterexample to the Jacobian conjecture (det DF = −2; companion record), γ(r) = (z^{−1}, −3z/2, 13z²/2), z = √(1 − 8r), is an integral curve of U for V = (2, 0, 0) that escapes every compact set as r ↑ 1/8, with F(γ(r)) = (−1/4 + 2r, 0, 0). *Status.* Verified: proved here and checked exactly; found in the audit. The workbench's attribution file records that Alpöge's announcement credits Akhil for the question and Fable for the work.

**The Gram sandwich.** If ‖(Φ\_J − Φ)x‖ ≤ δ‖Φx‖ for all x with δ ≤ 1, then (1 − δ)²Φ∗Φ ⪯ Φ\_J∗Φ\_J ⪯ (1 + δ)²Φ∗Φ, by the triangle inequality; δ ≤ 1 is needed for the lower bound (verified). The programme's Schur-complement replacements and the Yang–Mills heat semigroup are instances.

## 7. Catalogue of the remaining results

The standalone results of the audit's register not stated above; register numbers are given for reference. Each row is verified (proved in the programme at the label given and checked in the audit) unless it says otherwise.

| No. | Result | Label |
|---|---|---|
| S8, S9 | On Connes–Consani's signed winding group ⟨T, J : [T, J] = 1, J⁴ = 1⟩ ≅ ℤ × ℤ/4 [CCt], with sign ε = J² and mirror A(T^mJ^k) = T^{−m}J^{2m−k}, the sign-preserving mirror-commuting endomorphisms are T ↦ T^nJ^c, J ↦ J^b with n odd, so doubling has no sign-preserving mirror-compatible lift (T ↦ T², J ↦ 1 kills the sign); g ↦ A(g)g = ε^m derives parity from the mirror, and no group section of G → G/⟨J⟩ is equivariant | W5 (exhaustive for \|n\| ≤ 9), W2 |
| S10–S11 | The weight-one sign sector over the 𝔽\_{1²}-points is y² = x³ − x, with J acting as complex multiplication by i and Hecke character χ₋₄(n)n equal to the signed winding degree; L(Sym²E, s) = L(ψ², s)L(s − 1, χ₋₄) | found in the audit; checked for n ≤ 3000 |
| S14, S15, S17 | For nonreal ρ at most two primes have p^ρ algebraic; two primes determine the values at the zeros, and simultaneous generalized p^ρ- and q^ρ-eigenfunctionals are exactly the Mellin jets, one prime leaving the aliases ρ + 2πik/log p | IH5.3, IH6, MCL3.4 |
| S18 | Least-order lifting m + k + 1 at a zero of multiplicity m; the obstruction class (−1)^jj!/2·t^{r−1−j}χ\_ζ(b + t) mod t^{min(m,r)}, b = 1 − ρ; a connecting map of rank min(m, r) | MCL5–MCL9, ORE4–ORE5; numerically to 10⁻³⁹ |
| S32 | The clocks ℤ/1, …, ℤ/N have joint states ℤ/lcm(1, …, N), with log lcm(1, …, N) = ψ(N); for every integer a ≥ 2 the closure of a^ℤ in ∏\_{ℓ∤a}ℤ\_ℓ^× is a copy of ℤ̂ | PMS M3–M6; a ≥ 2 found in the audit |
| S36, S70 | On the three-point base Y the residue pairing is the trace of a sheaf map on Y × Y, kept by R∆^! = Rq\_∗, with paired weights 2Re ρ and 2 − 2Re ρ; RΓ(X^dbl, f^{−1}Ω) ≅ RΓ(Y, Ω) for every Ω, with supports, and in the trivial finite-unit sector the cohomology is H∗(ℙ¹\_{𝔽₁}, Ω) of [CC1] | FTD, PRS, DER, FSC, FEM; DCP5 (general form found in the audit) |
| S61, S54 | The residue extension splits after evaluation at s₀ ≠ 0 and at s₀ = 0 is n ↦ n(I − log n·N), with the tensor Euler functions of the split sum; the signed clocks satisfy the integral Bost–Connes relations, with R/(ker σ\_n + E\_nR) ≅ R/nR | NPE4; CCT-1–CCT-8 |
| S16, S58, S62 | Deligne's specialization argument with weight bookkeeping; two conditions implied by RH read off the Gaussian energy; tail annihilators of the corrected tests | TL1 (a reconstruction); S58 and S62 found in the audit; their proofs are not reproduced here |

---

# Part B. Proved negative results

## 8. Negative results, with their scope

Each result below is a theorem, or where marked a numerical observation, about a specific construction as it is defined, and it is stated with the scope in which it is proved. Where the source identifies the additional input the construction would need, that input is stated; whether the programme's constructions can supply those inputs is open. Derivations are in Part A at the places cited, or in the programme at the labels given, checked in the audit. Three kinds occur: (i) statements that are false, with a proof or counterexample; (ii) constructions whose conclusions hold for every divisor in the strip with the stated properties (or for curves over finite fields, or for functions without an Euler product that have off-line zeros), so that deciding the location of the zeros through them requires an input that distinguishes ζ, such as the Euler product; (iii) constructions equivalent to RH by construction, which isolate the off-line part of the zero set in their definition, so that proving RH through them requires an independent argument that this part vanishes. The inputs identified are a pole bound uniform in the tensor degree, or a discreteness input with a square (the first is equivalent on the programme's finite data to max Re ρ ≤ 1/2, so it would have to come from an independent source); a property that distinguishes ζ from the Davenport–Heilbronn function, such as the Euler product; and polynomial bounds on the principal parts of 1/ζ at the zeros. Bracketed numbers are those of the audit register.

### 8.1 Statements that fail

- **N-Vel [1].** Under (H), Σ\_{γ≤T}Re c(ρ) = T/(4π) + O(T) is false, since limsup|Re E(T)|/T = ∞, and the vertical law fails likewise (Theorem 2.2(b)); only the smoothed laws hold. Whether the observed skew (Re E/T between −3.15 and +0.17 up to T = 64 000; numerical) persists is open.
- **N-Sheet [3].** For a ∈ (0, 1)∖{1/2}, ζ(s, a) has infinitely many zeros with Re s > 1 [DH, Cas], and ζ(s, 2) = ζ(s) − 1 vanishes at 1.40778804065 + 23.3279877546i. So the properties shared by all sheets hold for sheets with zeros in Re s > 1, and a proof that the zeros of ζ lie on the line must use a property of the Eulerian sheets a ∈ {1/2, 1}, such as the Euler product.
- **N-Beurling [12, 13].** Beurling systems can have N(x) = kx + O(x^{1/2}exp(c(log x)^{2/3})) and zeros approaching σ = 1 [Zh, DMV], and (primes ∖ {2}) ∪ {3′, 4} has N(x) = x + O(log²x) (found in the audit), while exact counts determine the system. The programme's question is how the additive counting step constrains the multiplicative system.
- **N-Free [28].** {1} ∪ {2^e : e ≥ 2} is not free although its zeta function has all its zeros on Re s = 0 (Example 2.6); for congruence monoids zero-freeness in Re s > 1 does imply freeness (Proposition 2.7).
- **N-Eu [50].** No finite set of primes fixed in advance has Euler factors that determine every finite shifted-zeta product: for a\_j = 2πi/log p\_j, the even and odd sub-sums of {Σ\_jε\_ja\_j : ε ∈ {0, 1}^k} give products with equal Euler factors at every p\_j and different exponent measures, whose difference has Laplace transform ∏\_j(1 − e^{a\_jz}) ≠ 0 (found in the audit).
- **N-Mirror [37].** The second line is A(𝒵) = 𝒵 − 1, and mirror equals shift pointwise if and only if RH holds (Theorem 4.2). The properties used have counterparts for curves over finite fields, where RH is Weil's theorem [We48, Ro], so their consequences hold in a setting where every zero is on the line; the 0-centred pairing is not Hermitian (Proposition 4.4(b)); and the two lines coexist equally for the Davenport–Heilbronn function, which has the zero 0.808517182456637 + 85.6993484853776i off the line. To decide the location of the zeros, this route needs a property that distinguishes ζ, such as the Euler product.
- **N-Logic [43].** RH cannot be independent of ZFC and false (Proposition 6.4); for Σ₁-sound theories, non-refutability of RH is equivalent to RH.

### 8.2 Positive forms and receivers are supported on the critical zeros

- **N-Pos1 [6, 26].** Every continuous positive form compatible with the scaling transfer vanishes on the off-line part R = Q/N\_O (CPS4.2; Lemma 3.13); CFP, CPS, TWC10 and SPF9 are related results; in tensor degree k ≥ 2 reflected pairs survive, with modulus exactly n. An argument through such receivers needs an additional input that removes R.
- **N-Pos2 [24, 25, 30, 33, 35].** The summation image is dense in L²(du), so the naive L² quotient seminorm is zero (ASD10, OPD3); the swept distribution descends if and only if there are no off-line zeros (HSW6); the Hilbert receivers are pure, with kernel exactly the off-line jet classes (WHR8–WHR12); T\_p-invariant seminorms vanish on every primary block with 0 < Re ρ < 1 (ATG6.5); and Θ\_off = Σ\_{Re ρ≠1/2}m\_ρF(ρ) is never a nonzero multiple of b ↦ b(1) (an explicit b\_∗ has b\_∗(1) = 2 and Θ\_off(b\_∗) = 0; VWR10.5–10.9). My assessment: the spectral-radius argument proves purity of an image that retains only critical-line jets by construction, so to reach RH it would need an input showing that the kernel, the space of off-line jet classes, is zero.
- **N-Pos3 [47, 48, 53, 54, 56].** Equivalent by construction to RH, or to RH with simplicity: the objects and detectors of AST (ℛ), GDC (N\_O), PTQ (H\_off, the descent of the Weil form, PTQ8.3) and ECR5.5; the conditions W ≥ 0, U\_a = D\_a∗ and the density of the trace image (RTT, RZ); and the vanishing or normality conditions of GDE, ABH (ℒ\_{r,t}), HSR (D\_{r,t}, Ξ) and HBW, with unitarity of n^{−1/2}A\_n, weight-1/2 counting moduli, monodromy phases −1 and D\_{r,t} ⊂ H². The two numerical detectors are not holomorphic in ρ; every attempted cancellation leaves the off-line sector intact; the unconditional results among them (NHI5.4, NHI8.4, HSR4.1–HSR10.6, HBW3, HBW8, HBW9) hold whether or not RH does; and on the Hardy boundary receiver the adjoint-domain condition is met only by x = 0 [No].
- **N-Pos4 [29].** Under s ↦ 1 − s̄ the odd part of log|ζ| is (1/2)log|χ|, accounted for by the pole and the trivial zeros, so the detector ℰ\_r(t) is carried by the even part, and the functional equation fixes only the odd part (OZD5, OZD7). My assessment: a zero at height γ enters with the factor e^{2t(σ²−γ²)}, so for fixed (r, t) zeros above modest heights contribute below any practical numerical precision.

### 8.3 Constructions whose conclusions hold for a class of divisors

- **N-Unif1 [14, 15, 16].** The inference that an off-critical zero would go undetected is false: φ(v)e^{−(ρ−1/2)v} detects any zero. An off-critical quartet would enter the absorption measure as −2m(e^{βt} + e^{(1−β)t})cos γt, and excluding it requires a sign or growth bound beyond completeness (IH2–IH4). Order-preserving clock changes are linear and move the critical line with the zeros (PL2–PL8).
- **N-Unif2 [18, 19, 20, 22].** The least lift of the k-th jet has order m + k + 1 at every zero of multiplicity m, on or off the line (MCL6), and the fixed-order class of the restriction row is nonzero at every zero (ORE5.8, ORE6.5); MCL3–MCL7, ORE6.2, ORE6.5, IH6.4, the first two laws of IH6.5 and PL2.1 hold word for word for Z\_{1/5}, which has zeros in Re s > 1/2.
- **N-Unif3 [36, 55].** The cover-invariant part of the zero-coordinate slice is exactly the divisor that the chosen residue section inserts (the zeta divisor for ξ, any finite set for a polynomial section, the empty divisor for a constant; RSS3.2–RSS3.3, RSS6), and two sections of one extension have cocycle spans I\_ζ and ℬ (NJS10); locating the zeros this way requires an input about ξ beyond the choice of section.
- **N-Unif4 [38, 44, 46].** The two-line splitting and the derived separation hold for every primitive Dirichlet L-function and every Dedekind zeta function, for every configuration of zeros in the open strip (§4.5). The statements involving RH restate it through ℛ = Q/N\_O, which is determined by the values at off-line zeros, and the programme states that neither a vanishing nor a new pure weight follows (ADM9).
- **N-Unif5 [58, 59].** BML's winding difference is invertible for every zero set avoiding the integers with e^{−2πiρ} away from 1 (Lemma 6.2); BML11's H¹ is produced by truncating the logarithmic tower; the return theorems of BRC, GJN and GJNR hold for every divisor in the strip (Lemma 6.3); NP\_b = bP\_bN is the chain rule and has solutions for every nilpotent.
- **N-Unif6 [69, 70, 71, 72].** The doubled source has the cohomology of Connes–Consani's base (§7, S70). The gluing and the pullback (CGS4–CGS10, DCP4–DCP12) hold for every zero set, which enters as the spectrum of the dilations on H¹ and through the jets, and finite models with zeros on and off the line agree in all dimensions, ranks, signs and sections; the lift in DCP vanishes by Poisson summation rather than by a separation of weights (DCP12); the Ext-vanishing with the endpoint modules follows from ξ(0) = ξ(1) = 1/2 ≠ 0 (GEX9); OMS5–OMS7A hold for every divisor with 0 < Re ρ < 1 and unbounded heights (OMS8).
- **N-Prim [73].** Convergence of the primary decomposition is equivalent to polynomial bounds on the principal parts of 1/ζ at the zeros (Theorem 3.9), the input this construction needs; Q is not the product of its primary blocks, and the constant tuple 1, behind the programme's class c\_ζ (PGD4), is not a jet tuple.

### 8.4 Weights, tensor powers and the square

- **N-W1 [17, 21, 65].** The programme's receivers separate weights by the strip bounds or by Tate shifts built into them; a geometric source for a dividing line at weight 1 has not yet been constructed (TL8). Positivity of the timed-prime measure gives ζ(1 + it) ≠ 0 and the classical zero-free region, and no zero-free strip (Beurling systems with positive prime measure can have zeros approaching Re s = 1); the compact form, the cohomological proof of condition (C), the strict bound and Weil II §3 are the steps that would need ζ analogues.
- **N-W2 [23, 27, 31, 32, 34, 52, 66].** The exponent data return max Re ρ in every tensor degree (Proposition 5.1), and the needed input is a pole bound at k + 1 + C uniform in k. In the programme's square and tensor powers the characters of source and target match, the positive forms kill every tuple off the centred set, the tensor Weil form is indefinite on the reflected sector, and the square's obstruction vanishes exactly when the original one does (TWC6, TWC9–TWC11, FST3–FST7); in degree 1 the square reduces to Q ⊗ Q (GMC4–GMC6), and the finite-trace exponent is k·max Re ρ (ATG). The tensor Euler products of an off-line quartet have their pole at 1 + 2k·max(Re ρ, 1 − Re ρ) for every complex ρ, zero of ζ or not (checked at 0.7 + 10i); detecting zeros through them would require an input that singles out the zeros of ζ.
- **N-W3 [60], N-Tr [39].** The average weight of an off-line quartet is 1 (Proposition 5.2); Weil II 1.5.1 takes a pure determinant weight as its input, and at a point the weight of the determinant is the sum of the constituent weights. The product trace does not force weight 1: reflected-pair classes have character p whether or not either zero is on the line (FEM7–FEM8), and the diagonal return pairs 2Re ρ with 2 − 2Re ρ (DER10); no degree-zero same-site lift exists (FTD9), and R∆^!K → ∆^{−1}K is zero (DER6).
- **N-W4 [51, 61, 62, 63].** The bounds on ker N for V and V^∨ alone do not give Weil II 1.8.4 (Proposition 5.3); counting operators commuting with N have Deligne's local weights only if N = 0; P\_b has no eigenvector, so Deligne's weight filtration is not defined for it; and tensor Euler products agree for a non-split Jordan block and its split sum, such as the residue extension at s = 0 (ETR10, NPE4).
- **N-W5 [67, 68].** The recovered ring End(G/G\_tors) ≅ ℤ is formed from the free quotient of the winding group, every automorphism acts trivially on it, and the torsion, the chart twist, the involution and the support τ leave it unchanged; all Frobenius weights of the objects built on it from programme data are even. The purity circle |a|² = p needs weight 1, which Deligne's theory supplies through H¹ of an elliptic curve over 𝔽\_p; a weight-one object built from programme data is the input this route would need.
- **N-W6 [64], N-F1 [7–11].** Deligne's quadratic exception satisfies every positivity hypothesis (Lemma 5.5), and for ζ it is excluded because ℝ has no nontrivial quadratic character. Doubling has no sign-preserving mirror-compatible lift (§7, S8); the compact-completion modulus theorem holds for every compact group (P12); the √n dilation radius cancels in the product formula; the twistor involution fixes the radius only on |z| = 1; and the weight-one sign sector is L(E, s) of conductor 32, which is not ζ.

### 8.5 The two-line system and the transfers

- **N-Two1 [40].** The ℤ₂ anomaly of one line is the parity of N₀(T); in the two-line system the ℤ₂ anomaly vanishes and the ℤ₄ anomaly is the one-line parity; n\_G determines P only together with N₀; and the holonomy index counts off-line pairs and multiple on-line zeros together (Propositions 4.8, 4.9).
- **N-Two2 [41, 45].** The Davenport–Heilbronn function has the completed functional equation, the reality, a nonnegative two-line product on Re s = 0 and a four-point orbit for its off-line zero; the hypotheses of the separator lemma fail for it on every vertical line, and whether its splitting fails is open.
- **N-Two3 [74].** For products Λ of completed Dirichlet L-functions containing χ and χ̄ equally often, G\_Λ(it) = |Λ(1 + it)|² > 0 follows from Λ's functional equation, reality and nonvanishing on Re s = 1, and G\_Λ with its explicit formula is a function of Λ; so a bound on the off-line count obtained through G\_Λ is one obtained from Λ, and whether one-line inputs can bound that count better than Turing's method is open. The chiral form is hyperbolic whether or not RH holds, and its T-even part 2Ω is indefinite exactly when an off-line zero exists; the two-line prime races have the one-line distributions (Proposition 4.10).
- **N-X [42, 49, 57].** Joint averages do not survive restriction of the Navier–Stokes torus cover to unchanged finite torsion (13 against 4 at p = 13, a = 4). The Jacobian → Yang–Mills chain gives statements along couplings g\_j < 1/j tending to 0: Theorem 14.2 of the Yang–Mills workbench is correct conditional on fixed-box weak-coupling limits that the file sketches, and its energy quotients are, up to 1 ± 1/(10j), the lowest free two-gluon energy of an open box of side j/50, so Q\_j·(box side) → 2√2π, the scaling of a massless free field, for every Jacobian tensor; a statement about the continuum mass gap through this chain would need a fixed-coupling or continuum input. The Navier–Stokes profile gives a zero-quotient sequence only as the coupling tends to 0, and prime-only clock seeds are not transfer-stable.

---

# Part C. Bridges to other areas, and the directions they open

## 9. Bridges, what is established, and my assessment

Much of the programme consists of bridges between the zeta function and other areas. For each, this part gives the typed map (domain, codomain, what crosses), what is established, what it suggests on both sides, and my assessment, a view held at this stage.

### 9.1 Meyer's quotient and interpolation theory

*Map:* the jet map J : Q → ∏\_ρA\_ρ; the interpolation problem at the zeros crosses. *Established:* J is injective with dense image in Λ\_m, and onto exactly when the principal parts of 1/ζ are polynomially bounded (Corollary 3.7, Theorem 3.9). *Suggests:* for interpolation theory, the zeta zeros as a test case for interpolating varieties [BT], beside Fourier interpolation at the zeros [BRS]; for ζ, the pointwise form of the questions that the Gonek–Hejhal conjectures ask on average for Σ|ζ′(ρ)|^{−2k}. My assessment: this is the most precise translation in the programme, because it turns a structural property of its central object into a classical analytic condition; the multiple-zero case, where leading coefficients suffice in A\_p [BT, Theorem 4], is the natural next question.

### 9.2 The two-line system, Weil's explicit formula and Turing's method

*Maps:* f ↦ (u, v), carrying Q\_A to 2Ω(u) − 2Ω(v); the loop T^{−1}A to Weil's reflection #; the holonomy count to (N − V)/2. *Established:* §4. *Suggests:* for Weil's side, a test family {f\_k} that is T-even by construction, with the explicit prime side −G′/G; for Turing's side, that an index for off-line zeros alone needs a map separating off-line pairs from multiple zeros. My assessment: the bridge recasts Weil's positivity as a signature statement about a form that is hyperbolic for every configuration of zeros; since the whole form has the same signature with or without RH, I expect progress along this bridge to come from the diagonal family, where the positivity question is concentrated (Question 2).

### 9.3 The programme's weights and Deligne's Weil II

*Maps:* ρ ↦ p^ρ of weight 2Re ρ; even tensor powers ↦ the positivity step of Weil II 1.5; the timed-prime measure ↦ Deligne's positive measure; P\_b ↦ a relation FNF^{−1} = Q^{−1}N. *Established:* §5, and Weil II §2.1 specialized to ζ is the classical proof of ζ(1 + it) ≠ 0 (DB9, DR0–DR4). Every solution of the relation on a jet block forces the weight shift −2j of the programme's regrading, and such relations have solutions for every nilpotent, so what is established is a comparison of relations; the regrading, under which a jet block of multiplicity m satisfies the conclusion of 1.8.4 with centre 2Re ρ − (m − 1) and is mixed in Weil II's sense [TY], is chosen in the programme rather than derived from an arithmetic source. Kurokawa's tensor products [Ma, §1.4] and Connes' square of the arithmetic site [CoE] are analogies for H¹ ⊗ H¹ ↪ H². *Suggests:* for Weil II, a purity criterion and corrected lemmas; for ζ, the weight question (Question 8), which for the square is Manin's question of absolute Descartes powers of Spec ℤ [Ma]. My assessment: the even-power computations supply the Euler-product half of Deligne's §1.5 mechanism, and the other half is the uniform pole bound; since that bound is equivalent to max Re ρ ≤ 1/2 on finite exponent data, I think the decisive work here is an independent source for it, starting from the programme's own statement (TWC9, TWC11) that its computations leave room for one.

### 9.4 Nyman–Beurling in three topologies

*Maps:* the cover discrepancies in ℬ; two-sided dilation tests in L²(0, ∞); one-sided tests in L²(0, 1) and in Noor's Hardy space. *Established:* density in ℬ, unconditional (Proposition 3.11); two-sided density in L²(0, ∞) [Wi]; one-sided density equivalent to RH ([Be], [BD], Burnol's co-Poisson theory [Bu], [No]). *Suggests:* a comparison map between the settings, with its kernel identified, would show where the RH content enters. My assessment: the contrast is instructive, since the same family is dense unconditionally in one topology and exactly under RH in another; the sparse families of Question 5 probe which features of the topology matter.

### 9.5 Connes, Meyer and Connes–Consani

*Maps:* Q → Connes' Hilbert quotients [Co]; the doubled source → Connes–Consani's base Y; the adelic periodization complex C ≃ ℬ\_pr[1] ⊕ Q[0] (OMS7A.1); the absolute twistor line [CCt] → y² = x³ − x through its 𝔽\_{1²}-points; the reversed prime knots of [CCk] → the conjugate character, with W(χ)W(χ̄) = 1. *Established:* the kernel of the first map is exactly the off-line jets (§3.5); the second is a cohomology isomorphism (§7, S70) and the complex is formal (OMS7A.1); the twistor identification holds; the knot statements are theorems whose reading as anti-numbers is a proposal. Connes' §VIII distribution with the full Gram matrix is FGR, synthesis on Q is of Krasichkov-Ternovskii type [Kr], and the positive transfer forms are Bochner–Schwartz [Vl]. *Suggests:* for Connes' approach, an exact account of what the Hausdorff completion loses and a jointly faithful family over all lines Re s = σ (VWR); for the programme, a dictionary with the established spectral realizations. My assessment: the comparison of Connes' Hilbert quotients with Meyer's Fréchet quotient is the cleanest structural statement here; the comparison of the classification of positive forms with Meyer's and the Weil-positivity literature has still to be made, and I would make it first.

### 9.6 Clocks, Bost–Connes, Beurling and monoids

*Maps:* the clock operators S\_n = √nV\_n, with S\_mS\_n = S\_{mn} and S\_m∗S\_n = S\_{n/d}S\_{m/d}∗, d = gcd(m, n), the relations of C(ℤ̂) ⋊ ℕ^× [LR]; timed primes ↦ Beurling's D = exp\_∗(R); the sheets a = 1/q ↦ congruence monoids. *Established:* the global quotient of all prime clocks is the Bost–Connes space (P14), whose partition function is ζ(β), with its phase transition at β = 1 [BoC] (its link with Proposition 6.1 is an interpretation, for which a map remains to be constructed); the timed-prime reconstruction is Beurling's construction on the actual primes (TP9–TP13); the Eulerian tests are the Krull-monoid criteria ([BC, Ca]; §2.3). *Suggests:* for monoids, a freeness test for every monoid of integers (Theorem 2.4); for ζ, that regularity of the counting function alone does not force RH (N-Beurling). My assessment: the monoid results are of independent interest as elementary number theory, Theorem 2.4 and Corollary 2.5 most clearly; their novelty was checked by one search only.

### 9.7 Two-prime density and mean-periodic functions

*Map:* the density of (log p)ℤ + (log q)ℤ in ℝ, on which MCL3.4, IH6 and PL3 rest, ↦ the two-period phenomenon of mean-periodic functions [Sc]. *Established:* the density holds because log p/log q is irrational; the link is a comparison of mechanisms. *Suggests:* it explains why two primes determine every zero while one prime leaves the aliases ρ + 2πik/log p. My assessment: spectral synthesis for mean-periodic functions is well developed, and transferring it to the programme's jet calculus is a direct and checkable next step.

### 9.8 The anomaly dictionary (a proposal)

The objects and the facts proved about them hold without assuming RH; the matching is a proposal.

| Author's term | Exact object |
|---|---|
| anti-number | g ↦ conj(g(1/u))/u (Mellin shadow s ↦ 1 − s̄) |
| chirality | the mirror A(s) = −s̄ through the pole at 0 |
| the doublet | the orbit {ρ, ρ^#, ρ^# − 1, ρ − 1} of an off-line zero |
| ℤ₂ anomaly | the two lines as sheets of one double cover, deck transformation the central −1 of SU(2) |
| ℤ₁ anomaly | the root-number phase, cancelled by the anti-sector: W(χ)W(χ̄) = 1 |
| inflow | the bulk between the lines, holding the zeros with Re ρ < 1/2 and their mirrors |
| the support τ | the pivot of the swing between 0 and 1: the reflection s ↦ 1 − s̄ about 1/2 |

In these terms RH has three exact forms: every zero is its own anti-number; the bulk is empty; Weil's functional is nonnegative on every annihilation g ∗ g^# (whose value at the unit, ∫|g|²du, is positive with or without RH). My assessment: the dictionary is useful because every entry is an exact object; its test is whether a statement first seen in the physical language yields a new statement about these objects.

### 9.9 The 𝔽₁ context

The author's description of τ as carrying ℤ₁ and no ℤ₂ is realized at Connes–Consani's generic point η, which every homeomorphism fixes and where no exchanged label can sit, although the sign ε survives there; the absence of ℤ₂ thus has two exact readings, no exchanged label (true at η) or no sign (ε = 1, which among field-valued points holds exactly in characteristic 2). The labels ℤ\_n follow the principle that an 𝔽\_{1ⁿ}-structure is a free ℤ/n-action ([CCM, §3]; a reading); ℙ¹(𝔽\_{1²}) = {0, ∞, ±1}, with the double cover y² = x³ − x branched there; the Eulerian even sheets are those with (ℤ/q)^× = {±1}, the units of 𝔽\_{1²} (Proposition 2.8; the reading as 𝔽₁ → 𝔽\_{1²} is an interpretation); and G(ℤ) adds a Boolean point below the generic point of Spec ℤ, where Connes–Consani add a closed point ∞ (a reading). My assessment: the reading with mathematical content of its own is the coincidence of the Eulerian even sheets with the units of 𝔽\_{1²}, which deserves a statement independent of the reading.

### 9.10 The author's other workbenches

Companion records treat the Erdős–Straus (ES), Yang–Mills (YM, with the Navier–Stokes (NS), S⁶ and Jacobian material), Erdős Problem 817 and Collatz workbenches. Edges located from the zeta side:

| Edge | What crosses | Status |
|---|---|---|
| NS → ES | the torus endomorphism [[3, 1], [1, 5]]; exact aliasing on finite character groups | verified; joint averages need the complete preimage |
| NS → YM | NS velocity as a reducible SU(2) connection, −2Σtr F\_ij² = λ²\|curl u\|² | verified, conditional on imported NS bounds |
| zeta → YM | the Gram sandwich (§6) | verified |
| Jacobian → NS → YM | U = DF^{−1}(V ∘ F), the escaping curve, YM Theorem 14.2 | verified (Lemma 6.5; N-X) |
| S⁶ → YM | the imaginary period block, through D = det B | verified |
| ES ↔ zeta | the semiring G(R) = R ⊔ {τ}; a Keller map P with det DP = −2 | verified; for P only det DP |
| S⁶ → ES | the (3,4,∞) monodromy covers | verified at every level (Erdős–Straus record, Theorem 10.1) |
| Collatz ↔ ES ↔ zeta | the homogenization (x, h) ↦ (ax + bh, h) | verified in part (the ES diagram) |
| 817 → zeta | finite word sources in the supported quotient; a cocycle identity | one of ten interface notes verified |
| zeta → ES, NS → zeta | theorem dependencies (NG20–NG21); Mellin transports | not verified here |

One Collatz item is verified here: with T(n) = 4n + 1, θ(n) = 3n + 1 and the odd step U(n) = (3n + 1)/2^{v₂(3n+1)}, θ(T(n)) = 4θ(n), so U(T^jn) = U(n) for all j. My assessment: the shared linear algebra (Gram sandwiches, Schur complements) is the most reusable crossing, since it is exact and needs no identification of objects; the edges that carry a statement about ζ into another workbench, or back, still need typed maps with verified content.

---

## 10. Questions

1. **The primary decomposition.** Are the principal parts of 1/ζ at the zeros polynomially bounded (Theorem 3.9(c))? For multiple zeros, do the leading coefficients suffice?
2. **The diagonal family.** Is the T-even family {f\_k} of Corollary 4.7 easier to control on the prime side, through −G′/G, than Weil's own family?
3. **An index for off-line zeros.** Is there an index, from a map on the strip, that counts off-line zeros alone (Proposition 4.9), and can one-line inputs bound the bulk count better than Turing's method?
4. **The Davenport–Heilbronn function.** Does the two-line splitting fail for it?
5. **Sparse degrees.** Is the family with n ∈ {2^a3^b} dense in ℬ for 0 < t ≤ 0.06060? Carleman's formula in the sectors |arg w| < π/(2k), applied to L(z^{1/k}), gives the thresholds (log 2)(log 3)/(2πk) for 0 < k ≤ 2 (from (4 − k²)∫\_{−α}^{α}sin²φ cos kφ dφ + 2k sin²α = 4/k, α = π/(2k); check Z7), while for k > 2 its zero sum converges and step 3 gives no contradiction; a Jensen argument needs t > (log 2)(log 3)/2 ≈ 0.381. Which sets S of quadratic counting give density for every t > 0?
6. **Velocities and Beurling systems.** Do the one-sided statements for the sharp velocity sums hold, and does the sharp spectrum differ from the Dirichlet spectrum off the Eulerian sheets (suggested numerically at a = 2)? Does N(x) = cx + O(x^θ), θ < 1/2, force ζ\_P ≠ 0 on σ > 1/2?
7. **The local model at τ.** Which local model of the test functions at τ does the programme intend (Proposition 6.1)?
8. **The weight question.** Can the reconstructed arithmetic supply a square with a Künneth map and discrete weights, or an independent source for a pole bound uniform in the tensor degree (§5.1)? A ramified map reported in the programme's sessions of 24–25 September, with an exact factor n^{−1} in the nilpotent relation, is to be compared with this question.

## 11. Verification

Every numerical or symbolic claim of the source has a check script with recorded output; the scripts are in the record's `checks/zeta/` folder. They use `mpmath`, `sympy` and, for argument-principle counts, Arb ball arithmetic; checks marked expected-fail document a finding (for example the counterexample of Lemma 5.4).

- The version-1 checks: 48 scripts at the top of `checks/zeta/` (47 with a recorded `_OUTPUT.txt`), including F1–F9 and G1–G3 (Theorem 3.9), B1–B5 (Proposition 4.6), D1–D4 and R5 (Proposition 4.9), C1–C3 (Proposition 4.10) and B1–B4 (Lemma 5.4).
- The first referee pass: four scripts in `checks/zeta/referee08/`, with their argument-principle outputs.
- Five figure scripts in `checks/zeta/figures/`, and the code of §2.1 in `checks/zeta/copy_round2_code/`, which reads its zero data from the directory named by `ZERO_DATA_DIR`.
- Version 2: `zeta_reader_addendum_checks.py` (Z1–Z8), and in `checks/zeta/zeta_reader_review/` the review's ten scripts, the eleven scripts of `verify_minors/` and the sixteen of `referee_v2/`.

**Not read or not re-derived** (not verified here): the products named in the final reports of the programme's sessions of 24–25 September (among them GPC0–GPC12, CW1–CW8, TPL0–TPL13, BQC0–BQC6, ASQ0–ASQ12, CQF0–CQF10 and CCR0–CCR10); TD, GHE beyond GHE1, TP and S1–S7 (read in content maps only); NPE5–NPE10 and NER; GAP, GER, GEX, CTF, ASD, JTB, PGD, PGC, SCL, DPL, RSR and SSI10 (read in part); and, taken on trust, Meyer's paper, CFPA.1–CFPA.7, GSP and CTS, and the Yang–Mills lattice calculations and fixed-box limits. Still to be done: a line-by-line re-derivation of Theorem 2.1, with checks at a = 1/2 and a = 2.

## References

- [Aa] S. Aaronson, The Busy Beaver frontier, ACM SIGACT News 51 (2020), no. 3, 32–54.
- [AKN] A. V. Abanin, Le Hai Khoi, Yu. S. Nalbandyan, Minimal absolutely representing systems of exponentials for A^{−∞}(Ω), J. Approx. Theory 163 (2011) 1534–1545.
- [BD] L. Báez-Duarte, A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis, Rend. Lincei Mat. Appl. 14 (2003) 5–11.
- [BC] P. Baginski, S. T. Chapman, Arithmetic congruence monoids: a survey, Springer Proc. Math. Stat. 101 (2014) 15–38.
- [BSY] M. Balazard, E. Saias, M. Yor, Notes sur la fonction ζ de Riemann, 2, Adv. Math. 143 (1999) 284–287.
- [BT] C. A. Berenstein, B. A. Taylor, A new look at interpolation theory for entire functions of one variable, Adv. Math. 33 (1979) 109–143.
- [Be] A. Beurling, A closure problem related to the Riemann zeta-function, Proc. Nat. Acad. Sci. USA 41 (1955) 312–314.
- [Bo] E. Bombieri, Problems of the Millennium: the Riemann Hypothesis, Clay Mathematics Institute, 2000.
- [BRS] A. Bondarenko, D. Radchenko, K. Seip, Fourier interpolation with zeros of zeta and L-functions, arXiv:2005.02996.
- [BoC] J.-B. Bost, A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. 1 (1995) 411–457.
- [BCY] H. M. Bui, J. B. Conrey, M. P. Young, More than 41% of the zeros of the zeta function are on the critical line, Acta Arith. 150 (2011) 35–64.
- [BHB] H. M. Bui, D. R. Heath-Brown, On simple zeros of the Riemann zeta-function, Bull. London Math. Soc. 45 (2013) 953–961.
- [Bu] J.-F. Burnol, On Fourier and zeta(s), Forum Math.; arXiv:math/0112254.
- [Ca] L. Carlitz, A characterization of algebraic number fields with class number two, Proc. Amer. Math. Soc. 11 (1960) 391–392.
- [Cas] J. W. S. Cassels, Footnote to a note of Davenport and Heilbronn, J. London Math. Soc. 36 (1961) 177–184.
- [Co] A. Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, Selecta Math. 5 (1999) 29–106.
- [CoE] A. Connes, An essay on the Riemann Hypothesis, in: Open Problems in Mathematics, Springer, 2016.
- [CC1] A. Connes, C. Consani, Schemes over 𝔽₁ and zeta functions, Compos. Math. 146 (2010) 1383–1415.
- [CCk] A. Connes, C. Consani, Knots, primes and class field theory, arXiv:2501.06560.
- [CCt] A. Connes, C. Consani, The absolute twistor line and the geometry of Spec ℤ, arXiv:2609.00299.
- [CCM] A. Connes, C. Consani, M. Marcolli, Fun with 𝔽₁, J. Number Theory 129 (2009) 1532–1561.
- [Da] H. Davenport, Multiplicative Number Theory, 3rd ed., Springer, 2000.
- [DH] H. Davenport, H. Heilbronn, On the zeros of certain Dirichlet series, J. London Math. Soc. 11 (1936) 181–185, 307–312.
- [DMR] M. Davis, Yu. Matiyasevich, J. Robinson, Hilbert's tenth problem. Diophantine equations: positive aspects of a negative solution, Proc. Sympos. Pure Math. 28 (1976) 323–378.
- [De] P. Deligne, La conjecture de Weil. II, Publ. Math. IHÉS 52 (1980) 137–252.
- [Dev] L. Devin, Chebyshev's bias for analytic L-functions, Math. Proc. Cambridge Philos. Soc. 169 (2020) 103–140.
- [DMV] H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer, Beurling primes with large oscillation, Math. Ann. 334 (2006) 1–36.
- [Ja] H. Jarchow, Locally Convex Spaces, Teubner, 1981.
- [Kr] I. F. Krasichkov-Ternovskii, Invariant subspaces of analytic functions I–II, Mat. Sb. 87–88 (1972).
- [LR] M. Laca, I. Raeburn, A semigroup crossed product arising in number theory, J. London Math. Soc. 59 (1999) 330–344.
- [Ma] Yu. I. Manin, Lectures on zeta functions and motives (according to Deninger and Kurokawa), Astérisque 228 (1995) 121–163.
- [Me] R. Meyer, A spectral interpretation for the zeros of the Riemann zeta function, Göttingen Seminars 2004/2005, 117–137; arXiv:math/0412277.
- [MN] M. B. Milinovich, N. Ng, A note on a conjecture of Gonek, arXiv:1106.1160.
- [No] W. Noor, A Hardy space analysis of the Báez-Duarte criterion for the RH, Adv. Math. 350 (2019).
- [PT] D. Platt, T. Trudgian, The Riemann hypothesis is true up to 3·10¹², Bull. London Math. Soc. 53 (2021) 792–797.
- [PRZZ] K. Pratt, N. Robles, A. Zaharescu, D. Zeindler, More than five-twelfths of the zeros of ζ are on the critical line, Res. Math. Sci. 7 (2020).
- [Ro] M. Rosen, Number Theory in Function Fields, Springer, 2002.
- [RS] M. Rubinstein, P. Sarnak, Chebyshev's bias, Experiment. Math. 3 (1994) 173–197.
- [Ru] W. Rudin, Functional Analysis, 2nd ed., McGraw–Hill, 1991.
- [SW] E. Saias, A. Weingartner, Zeros of Dirichlet series with periodic coefficients, Acta Arith. 140 (2009) 335–344.
- [SchW] H. H. Schaefer, M. P. Wolff, Topological Vector Spaces, 2nd ed., Springer, 1999.
- [Sc] L. Schwartz, Théorie générale des fonctions moyenne-périodiques, Ann. of Math. 48 (1947) 857–929.
- [SBM] S. K. Sekatskii, S. Beltraminelli, D. Merlini, On equalities involving integrals of the logarithm of the Riemann ζ-function and equivalent to the Riemann hypothesis, Ukrainian Math. J. 64 (2012) 247–261.
- [TY] R. Taylor, T. Yoshida, Compatibility of local and global Langlands correspondences, J. Amer. Math. Soc. 20 (2007) 467–493.
- [Ti] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd ed., revised by D. R. Heath-Brown, Oxford, 1986.
- [TiF] E. C. Titchmarsh, The Theory of Functions, 2nd ed., Oxford, 1939.
- [Tu] A. M. Turing, Some calculations of the Riemann zeta-function, Proc. London Math. Soc. (3) 3 (1953) 99–117.
- [Vl] V. S. Vladimirov, Methods of the Theory of Generalized Functions, Taylor & Francis, 2002.
- [We48] A. Weil, Sur les courbes algébriques et les variétés qui s'en déduisent, Hermann, 1948.
- [We52] A. Weil, Sur les "formules explicites" de la théorie des nombres premiers, Comm. Sém. Math. Univ. Lund, tome supplémentaire (1952) 252–265.
- [Wi] N. Wiener, Tauberian theorems, Ann. of Math. 33 (1932) 1–100.
- [Zh] W.-B. Zhang, Beurling primes with RH and Beurling primes with large oscillation, Math. Ann. 337 (2007) 671–704.
