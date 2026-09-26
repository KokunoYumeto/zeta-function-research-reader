# The four continuation directions of `22_` §5: the chiral cross form is Weil's form on the diagonal, the second line is invisible to prime races, and the holonomy index is Turing's

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 23:04 UTC. Board task 9: the continuation directions of `22_` §5, written after `22_`'s eighteenth referee pass. Refereed in the nineteenth pass (report written by about 00:02 UTC on 26 September) and revised at 00:25 UTC; §9 lists the changes.

The four directions are the owner's (M27: components that do not settle RH one at a time are kept, because a combination may). This note pushes each to a precise statement and proves it. Directions 1 and 3 have negative answers, and each says which observable fails to see an off-line zero and why. Direction 2 has both: the chiral form on all data is blind (42.2(a)), and on the diagonal it is Weil's form, positive exactly under RH (42.2, 42.3), so the owner's chiral pairing becomes Weil's pairing on the diagonal of the two lines. Direction 4 gives an index that sees off-line zeros at each finite height, together with multiple zeros on the line (42.5).

## 0. Setting

- **Zeros and maps.**
  - Z is the set of distinct nontrivial zeros of ζ, and m_ρ is the multiplicity of ρ. Sums over Z, Z − 1 and Z ⊔ (Z − 1) run over distinct points, with the weights m written out.
  - G(s) = ξ(s)ξ(s + 1)/16 has zero set Z ⊔ (Z − 1), with multiplicity m_ρ at ρ and at ρ − 1. The two parts are disjoint, since their real parts lie in (0, 1) and (−1, 0).
  - The maps are those of `22_` Prop. 22.6: the reflection # (s ↦ 1 − s̄) on Z; the mirror A (s ↦ −s̄) through the pole at 0; and the translation T between the lines, s ↦ s − 1 on Z and s ↦ s + 1 on Z − 1.
  - A carries Z onto Z − 1 by ρ ↦ ρ^# − 1, and T⁻¹A = # on Z (the holonomy).
- **Test space.** ℬ is the space of entire functions rapidly decreasing in vertical strips (`40_` §1). F_*(s) = s(s − 1)π^{−s/2}Γ(s/2)ζ(s)/8 lies in ℬ and vanishes exactly on Z, with multiplicities (OMS2.3–2.5).
- **The two pairings on value data.** Let f be a finitely supported function on Z ⊔ (Z − 1).
  - Weil's pairing, centred at ½: Ω(u) = Σ_{ρ∈Z} m_ρ u(ρ)·conj u(ρ^#), for u a function on Z.
  - The chiral cross form, centred at 0: Q_A(f) = Σ_{w∈Z⊔(Z−1)} m_w f(w)·conj f(Aw) (`22_` Prop. 22.4, with the hypotheses of its revised text).
  - Both are real, because # and A are involutions that preserve multiplicities.

## 1. Direction 1: the multiplicative doublet class

**Proposition 42.1.** Let Λ = ∏_i Λ(s, χ_i) over a finite multiset of primitive Dirichlet characters that is invariant under χ ↦ χ̄ (χ and χ̄ occur equally often), with ξ in place of the trivial character. Put G_Λ(s) = Λ(s)Λ(s + 1).
- (a) Λ(1 − s) = Λ(s) and Λ(s̄) = conj Λ(s). Hence G_Λ(it) = |Λ(1 + it)|² > 0 for every real t.
- (b) The zeros of G_Λ in the open strip −½ < Re s < ½ are the zeros of Λ with 0 < Re ρ < ½, together with the translates ρ − 1 of the zeros with ½ < Re ρ < 1. Their number up to height T, with multiplicity, is the number of off-line zeros of Λ up to T.
- (c) The explicit formula of G_Λ is that of Λ plus the terms of the second line. These are the prime series Σ_i Σ_n Λ(n)χ_i(n)n^{−1−s}, the Gamma terms of Λ(s + 1) and, for each trivial factor, the rational terms −1/s − 1/(s + 1) of −ξ′/ξ(s + 1). The prime series converges absolutely for Re s > 0, and all these terms are holomorphic there. For a trivial factor the prime series has a pole at s = 0, which −1/s cancels (§3).

*Proof.*
- (a) By `22_` 22.8(c), W(χ)W(χ̄) = 1, and W = 1 for real primitive χ. Since χ and χ̄ occur equally often, the product of the functional equations Λ(s, χ) = W(χ)Λ(1 − s, χ̄) has total root number 1 and returns the same multiset, so Λ(s) = Λ(1 − s). For a multiset closed under conjugation only as a set, such as {χ, χ, χ̄}, the functional equations return the multiset {χ̄, χ̄, χ}, and Λ(1 − s) = Λ(s) fails (check R2b: |Λ(1 − s)/Λ(s) − 1| = 2.66 at s = 0.31 + 7.3i). Conjugation invariance gives conj Λ(s̄) = ∏Λ(s, χ̄_i) = Λ(s). Then Λ(it) = Λ(1 − it) = conj Λ(1 + it), and L(1 + it, χ) ≠ 0 (ξ(1 + it) ≠ 0 for the trivial character).
- (b) Λ(s + 1) has no zero with Re s ≥ 0, and Λ has no zero with Re s ≤ 0 or Re s ≥ 1.
- (c) −G_Λ′/G_Λ = −Λ′/Λ(s) − Λ′/Λ(s + 1). ∎ (Checks A1–A2: the doublet χ, χ̄ mod 5.)

**Negative result 42.N1.** The positivity of G_Λ on the centre line Re s = 0 is a consequence of Λ's functional equation, its reality and L(1 + it, χ) ≠ 0 (a). G_Λ(s) = Λ(s)Λ(s + 1), and its explicit formula is the sum of Λ's explicit formula at s and at s + 1 (c). So the combination has no input beyond Λ's own functional equation, reality, explicit formula and nonvanishing on Re s = 1, and every bound on the bulk count (b) that it yields can be obtained from these. This is a statement that no new input enters; it does not decide whether one-line inputs can do better than Turing's method, which is the original question. For finite heights, Turing's method and the located sign changes give N(T) and the index (N(T) − V(T))/2 = P(T) + Σ⌊m_ρ/2⌋ of Proposition 42.5 (stated there for ζ). When the index is 0 the bulk count is 0. When it is positive, these data do not separate off-line pairs from multiple zeros on the line (check R5c). For ζ, RH has been verified up to height 3·10¹² (Platt–Trudgian, Bull. London Math. Soc. 53 (2021) 792–797), so the bulk count of G is 0 there. For the L-functions of primitive characters of modulus q ≤ 400 000, GRH has been verified up to height max(10⁸/q, 7.5·10⁷/q + 200) for even q and max(10⁸/q, 3.75·10⁷/q + 200) for odd q (Platt, Math. Comp. 85 (2016) 3009–3027).

## 2. Direction 2: annihilation positivity with two lines

**Proposition 42.2 (the chiral cross form is Weil's form on the diagonal).** Let f be finitely supported on Z ⊔ (Z − 1), or the restriction of an element of ℬ. In the second case every sum below converges absolutely, since |F(w)| ≤ b_{1,M}(F)(1 + |Im w|)^{−M} on the zero set for F ∈ ℬ and the number of zeros up to height T is O(T log T) (`22_` Prop. 22.4); the proof is unchanged, term by term. Write u(ρ) = ½(f(ρ) + f(ρ − 1)) and v(ρ) = ½(f(ρ) − f(ρ − 1)) for ρ ∈ Z. These are the T-even and T-odd parts: f = u + v on Z and f = u − v on Z − 1. Then

  Q_A(f) = 2Ω(u) − 2Ω(v).

- (a) A has no fixed point on Z ⊔ (Z − 1). So Q_A is an orthogonal sum of hyperbolic planes, one for each pair {w, Aw}, and on data supported on n such pairs its signature is (n, n), whether or not RH holds.
- (b) Ω(u) = Σ_{on-line ρ} m_ρ|u(ρ)|² + Σ_{off-line pairs {ρ, ρ^#}} 2m_ρ Re(u(ρ)·conj u(ρ^#)). So Ω ≥ 0 on all finitely supported u exactly when every zero is on the line. (The same holds on the data of ℬ, which contain the finitely supported data by OMS6.2; see the proof of Corollary 42.3.)
- (c) Under RH, the T-even data V₊ and the T-odd data V₋ form a Q_A-orthogonal decomposition with Q_A positive definite on V₊ and negative definite on V₋. So V₊ is a maximal positive subspace. If RH fails, V₊ contains a negative direction.

*Proof.*
- For ρ ∈ Z one has Aρ = ρ^# − 1 ∈ Z − 1 and A(ρ − 1) = ρ^# ∈ Z. Hence

  Q_A(f) = Σ_ρ m_ρ [f(ρ)·conj f(ρ^# − 1) + f(ρ − 1)·conj f(ρ^#)].

- Substituting f = u + v on Z and f = u − v on Z − 1 gives 2Σ m_ρ[u(ρ)conj u(ρ^#) − v(ρ)conj v(ρ^#)]. The cross terms cancel pairwise.
- (a) Aw = w means Re w = 0, and G has no zero there (G(it) > 0, `22_` 22.4). On a pair {w, Aw} the form is 2m_w Re(f(w)·conj f(Aw)), a hyperbolic plane.
- (b) # fixes the on-line zeros and pairs the off-line ones.
- (c) Under RH, Ω(u) = Σ m|u|² is positive definite. If W ⊋ V₊, then W contains some x = x₊ + x₋ with x₋ ≠ 0, hence x₋ itself, and Q_A(x₋) < 0. If RH fails, (b) gives u ∈ V₊ with Ω(u) < 0 (u = 1 at ρ, −1 at ρ^#). ∎ (Checks B1–B5, on a synthetic configuration with multiplicities and an off-line quadruple.)

**Corollary 42.3 (an RH criterion in the owner's two-line terms).** For k ∈ ℬ put

  f_k(s) = F_*(s + 1)F_*(s − 1)k(s) + F_*(s + 2)F_*(s)k(s + 1).

Then f_k ∈ ℬ, and f_k is T-even on the zero set, with u(ρ) = F_*(ρ + 1)F_*(ρ − 1)k(ρ). Moreover

  RH ⟺ Q_A(f_k) ≥ 0 for every k ∈ ℬ,

and Q_A(f_k) = 2Σ_ρ m_ρ U(ρ)·conj U(1 − ρ̄) with U = F_*(s + 1)F_*(s − 1)k.

*Proof.*
- **T-evenness.** F_*(ρ) = 0 gives f_k(ρ) = F_*(ρ + 1)F_*(ρ − 1)k(ρ) = f_k(ρ − 1).
- **⇐.** F_*(ρ ± 1) ≠ 0 for every nontrivial zero ρ: Re(ρ ± 1) lies in (1, 2) or (−1, 0), and F_* vanishes only on Z. Finite sums of the functions ℛ_ρ(P) ∈ ℬ of OMS6.2 (the test representatives of OMS6's sections) give k ∈ ℬ with prescribed values at finitely many zeros and full-order vanishing at all others. So u ranges over all finitely supported data, and Proposition 42.2(b) applies.
- **⇒.** Under RH, Ω(u) = Σ m|u|² ≥ 0. ∎ (Checks B′1–B′3 at the first zero: Q_A(f_k) = 2|f_k(ρ₁)|² for the T-even f_k, and −2|f_k(ρ₁)|² for the T-odd variant with a minus sign.)

**Reading and scope.**
- **The answer to the question of `22_` §5, item 2.** RH is equivalent to a positivity statement for a subspace of the two-line space: the chiral cross form is nonnegative on the diagonal of T-even data, and then that diagonal is a maximal positive subspace.
  - The chiral form adds no information beyond Weil's pairing: on the diagonal it is twice Weil's form, and on the anti-diagonal minus twice it.
  - As a form on all data it is blind to RH (a).
  - This is the functional form of the holonomy identity T⁻¹A = # of `22_` Prop. 22.6. The chiral mirror A through the pole at 0, followed by the translation back between the lines, is Weil's reflection through ½.
- **The criterion is equivalent to RH by construction.** Like the constructions of register negative result 47, its test data can be localized at the zeros.
  - It would gain leverage only through its prime side. Q_A(f) = Σ_{w} m_w(f·f^A)(w), with f^A(s) = conj f(−s̄), is Weil's explicit-formula functional of G applied to f·f^A. So it is computable from primes, Gamma factors and polar terms without the zeros, as Weil's own criterion is. Since G(−s) = G(s), for a > 1 and h = f·f^A,

    Q_A(f) = (1/2πi)∫_{(a)} [h(s) + h(−s)](G′/G)(s) ds,

    where on Re s = a

    G′/G(s) = 2/s + 1/(s − 1) + 1/(s + 1) − log π + ½ψ(s/2) + ½ψ((s + 1)/2) − Σ_n Λ(n)(1 + n^{−1})n^{−s}.

    The left side of the rectangle is carried to the right side by s ↦ −s, because G′/G is odd. The horizontal sides tend to 0 along the good heights of `40_` Lemma 40.2, where G′/G is polynomially bounded, because h decays faster than any power of |t| in vertical strips. (Check R3f: the two sides agree to 25 digits for f(s) = e^{0.02s²}(α + βs); check R3g: without the polar terms they differ by 1.7637.)
  - Whether the diagonal family {f_k} is easier to control on the prime side than Weil's family is open here.

## 3. Direction 3: the prime squares and the two-line race

**Proposition 42.4.** Let χ be a primitive character mod q, and let G_χ(s) = Λ(s, χ)Λ(s + 1, χ). The prime coefficients of −G_χ′/G_χ are Λ(n)χ(n)(1 + n^{−1}). Put θ_G(x, χ) = Σ_{p≤x} χ(p) log p·(1 + p^{−1}).
- (a) For nonprincipal χ, θ_G(x, χ) − θ(x, χ) = Σ_{p≤x} χ(p) log p/p = C_χ + o(1), a convergent series. For the trivial character the difference is log x + O(1) (Mertens).
- (b) Hence the two-line races mod 4 differ from the one-line races by convergent series.
  - For the θ-race: E_G(x) = (θ_G(x; 4, 3) − θ_G(x; 4, 1))/√x = E(x) + O(x^{−1/2}), where E(x) is the one-line quantity.
  - For the counting race with π_G(x; q, a) = Σ_{p≤x, p≡a} (1 + 1/p): the difference from the one-line race is −Σ_{p≤x} χ₋₄(p)/p, which converges. After Rubinstein–Sarnak's normalization log x/√x it tends to 0.
  - So each two-line race has a limiting logarithmic distribution whenever its one-line counterpart has one, and then the same one.
  - Under GRH, Rubinstein–Sarnak show that the counting race has a limiting logarithmic distribution (their Theorem 1.1). Under GRH and their Grand Simplicity Hypothesis (linear independence over ℚ of the nonnegative ordinates), this distribution is absolutely continuous, and the primes 3 mod 4 lead on a set of logarithmic density δ(4; 3, 1) ≈ 0.9959 (*Chebyshev's bias*, Experiment. Math. 3 (1994) 173–197; the value as quoted by Devin, arXiv:1706.06394v4, p. 1; the hypotheses of Theorem 1.1 as described in Devin's Remark 3(1)). The two-line counting race therefore has the same limiting distribution under GRH, and the same density under GRH and the Grand Simplicity Hypothesis. (Check R4g recomputes δ(4; 3, 1) = 0.99593 under these hypotheses from the zeros of L(s, χ₋₄) up to height 100.)
- (c) For real χ, the prime squares contribute θ(√x) + O(log q) ~ √x to both races. For complex χ the corresponding term is o(√x) (`22_` §5, item 3, as revised).

*Proof.*
- (a) Partial summation gives Σ_{p≤x} χ(p) log p/p = θ(x, χ)/x + ∫_2^x θ(t, χ)t^{−2}dt. For a fixed modulus q, θ(t, χ) = O(t·exp(−c√log t)) (the prime number theorem for progressions; Davenport, *Multiplicative Number Theory*, ch. 20). So the integral converges.
- (b) follows from (a), since θ(x; 4, 3) − θ(x; 4, 1) = −Σ_{p≤x} χ₋₄(p) log p. Likewise Σ_{p≤x} χ₋₄(p)/p converges, by partial summation from the same estimate.
  - Two quantities whose difference tends to 0 have the same limiting logarithmic distribution.
  - The logarithmic densities of the sets where they are positive agree when that distribution has no atom at 0.
- (c) For real χ, χ(p²) = 1 for p ∤ q. ∎ (Checks C1–C3 up to 10⁷.)
  - The partial sums of −Σχ₋₄(p) log p/p are 0.5271, 0.5321, 0.5414, 0.5455 and 0.5454 at x = 10³ … 10⁷.
  - E and E_G differ by at most 0.0018 at every prime x in [10⁵, 10⁷] (check R4c; the maximum is 0.00171).

**Negative result 42.N3.** At the √x scale of Chebyshev's bias the second line is invisible. The two-line system's prime race differs from the one-line race by a convergent series, which vanishes after the bias normalization. So whenever the one-line race has a limiting logarithmic distribution (under GRH), the two-line race has the same one, and the logarithmic densities agree when that distribution has no atom at 0 (under GRH and linear independence).
- In the owner's terms: a knot traversed twice cancels the sign for real χ on both lines at once. The "distortion visible only with both lines" does not appear in prime races.
- Among the observables examined here, the only one that uses both lines and sees off-line zeros is the pairing Q_A on its diagonal, and there it is twice Weil's form (Proposition 42.2).

## 4. Direction 4: the holonomy as an index

**Proposition 42.5 (the holonomy index).** For T > 0 not the ordinate of a zero:
- let N(T) be the number of zeros with 0 < γ ≤ T, with multiplicity;
- let V(T) be the number of sign changes of Hardy's function Z on (0, T);
- let P(T) be the number, with multiplicity, of zeros with 0 < γ ≤ T and Re ρ < ½. This is one member of each off-line #-pair, that is, the doublets of `22_` Prop. 22.6 with nontrivial holonomy.

Then

  I(T) := (N(T) − V(T))/2 = P(T) + Σ_{on-line ρ, 0<γ≤T} ⌊m_ρ/2⌋.

So I(T) ≥ 0, and I(T) = 0 exactly when every zero with 0 < γ ≤ T is on the line and simple.

*Proof.*
- The off-line zeros come in #-pairs of equal height and equal multiplicity, so they contribute 2P(T) to N(T).
- Z(t) = e^{iθ(t)}ζ(½ + it) is real-analytic and real-valued, and its zeros are the on-line zeros with the same orders. It changes sign exactly at the zeros of odd order. So V(T) = Σ_{on-line}(m_ρ − 2⌊m_ρ/2⌋).
- Subtract. ∎ (Checks D1–D4.)
  - For ζ: N = V = 29 at T = 100, and N = V = 108 at T = 250.
  - A symmetric polynomial model with a double on-line zero and one off-line pair gives N = 5, V = 1 and I = 2.
  - The counting identity holds on 200 random configurations (D4 computes V by the formula under test, so it checks only m − (m mod 2) = 2⌊m/2⌋; check R5b computes V exactly, from square-free parts and Sturm counts, on 25 random symmetric configurations).

**Reading.**
- **Boundary data.** N(T) is determined by the values of ζ on the boundary of a rectangle: N(T) = θ(T)/π + 1 + S(T) by the argument principle. V(T) is determined by the values on the critical line. Both lines of the two-line picture carry the same data, by translation. So I(T) is computed from boundary data. It is not the index asked for in `22_` §5, item 4, which should count off-line zeros alone and come from a map on the strip. I(T) also counts Σ⌊m_ρ/2⌋, and no such map is constructed here.
- **It counts the nontrivial holonomies P(T),** plus ⌊m_ρ/2⌋ for each on-line zero, the number of pairs in its multiplicity.
- **It is Turing's index.** Verifications of RH to a height T locate the sign changes of Z and confirm with Turing's method that none are missing, that is, that N(T) equals their number. This is I(T) = 0 (A. M. Turing, Proc. London Math. Soc. (3) 3 (1953) 99–117).
- **What is missing.** The statement I(T) = 0 for all T is RH together with the simplicity of all zeros. No finite computation gives it.

## 5. What was learned

- **The second line carries no zero data of its own.** Z ⊔ (Z − 1) is determined by Z. The second line's contribution to prime sums is a Dirichlet series holomorphic on Re s > 0 (42.1(c)). At s = 0, where the races live, it is Σ_{p≤x} χ(p) log p/p. This converges conditionally for nonprincipal χ, by the prime number theorem in progressions (42.4(a)), and grows like log x for the principal character (check R4e: the series with |χ(p)| grows by log 10 per decade). In either case it is o(√x), and it vanishes after the bias normalization (42.4).
- **Three observables are blind to off-line zeros:**
  - the positivity of the doublet class on the centre line (42.N1);
  - the chiral form as a whole (42.2(a));
  - the two-line prime race (42.N3).

  Each is blind for an exact reason: it is implied by one-line facts, it is hyperbolic whatever the zeros do, or the second line enters only at order x^{−1/2}, up to a factor log x, after the bias normalization.
- **One two-line observable sees them, and it is Weil's.** The chiral form on the diagonal of T-even data equals Weil's form, and it is positive exactly under RH (42.2, 42.3). This makes the owner's chirality exact at the level of pairings: the mirror through the pole at 0, composed with the passage between the lines, is Weil's reflection through ½.
- **The holonomy has an index, Turing's.** It is exact at every finite height, and it is certified whenever it vanishes, as in all verifications so far. A positive value could not always be certified by finite-precision computation: a double zero on the line and two nearby simple zeros have boundary values that agree to any given precision (42.5; check R5d).

## 6. Items for the goals

- **Negative results (goal 1).** 42.N1 (direction 1: positivity on the centre line adds no input to the bulk count); 42.2(a) (direction 2: the chiral form on all data is hyperbolic whether or not RH holds); 42.N3 (direction 3: the second line is invisible to prime races).
- **Standalone lemmas (goal 3).** Proposition 42.2 (Q_A = 2Ω ⊕ (−2Ω)); Proposition 42.5 (the index formula). Both are elementary; no novelty search was made.
- **Bridges (goal 2).**
  - The owner's chiral pairing becomes Weil's pairing on the two-line diagonal, via T⁻¹A = #.
  - The owner's holonomy becomes Turing's index.

## 7. Checks

`checks/two_line_directions_checks.py`, 17 items, all pass (runtime about 80 s; output in `…_OUTPUT.txt`). After the nineteenth referee pass: `checks/referee19_notes41_42_checks.py`, 29 items, all pass (runtime 73 s), adapted from the referee's own script; the items R1–R5 cited above are there.

| items | test |
|---|---|
| A1–A2 | the doublet χ, χ̄ mod 5: G_Λ(it) real, equal to \|Λ(1 + it)\|² > 0; Λ(s) = Λ(1 − s) and reality |
| B1–B5 | Q_A = 2Ω(u) − 2Ω(v) on 50 random data; Ω real; A without fixed points; Ω < 0 on an off-line pair; Ω = Σm\|u\|² on on-line zeros |
| B′1–B′3 | f_k at the first zero: T-even, vanishing at the other zeros, Q_A(f_k) = ±2\|f_k(ρ₁)\|² |
| C1–C3 | the convergent correction series up to 10⁷; E and E_G; the prime-square term θ(y)/y at y = 10³, √(10⁷), 10⁶ |
| D1–D4 | N(T) = V(T) for ζ at T = 100 and 250; the model with I = 2; the counting identity |

C3 first failed because its tolerance was set too tightly (2% at y = 3162, where θ(y)/y = 0.968). It now checks the ratio at three sizes; this was not a mathematical failure.

B2–B5 and D4 hold by construction of the synthetic data and cannot fail. B′3 follows from B′1. C2 tests the bound 0.03 at three points, and C3 checks θ(y)/y only. The script `checks/referee19_notes41_42_checks.py` tests these statements independently: R1a–R1e (an independent matrix implementation of Proposition 42.2 on 30 configurations with multiplicities and off-line quadruples), R4c (the bound on E_G − E at every prime), R4f (the prime-square term for a complex character) and R5b (the index formula with V computed exactly).

## 8. Sources

- `22_` (Props. 22.4, 22.6, 22.7, 22.8 and §5, as revised after the eighteenth referee pass); `40_` §1 and OMS2.3–2.5, OMS6 (the space ℬ, F_*, the sections).
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., GTM 74, ch. 20 (the prime number theorem for progressions).
- M. Rubinstein, P. Sarnak, *Chebyshev's bias*, Experiment. Math. 3 (1994) 173–197.
- A. M. Turing, *Some calculations of the Riemann zeta-function*, Proc. London Math. Soc. (3) 3 (1953) 99–117.
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10¹²*, Bull. London Math. Soc. 53 (2021) 792–797 (arXiv:2004.09765).
- D. Platt, *Numerical computations concerning the GRH*, Math. Comp. 85 (2016) 3009–3027 (arXiv:1305.3087).
- L. Devin, *Chebyshev's bias for analytic L-functions*, Math. Proc. Cambridge Philos. Soc. 169 (2020) 103–140 (arXiv:1706.06394).

## 9. Revision after the nineteenth referee pass

An independent referee pass (report written by about 00:02 UTC on 26 September) re-derived and checked Propositions 42.1–42.5, Corollary 42.3 and the explicit-formula claim of §2, and found them correct. It found two statements false as written and seven minor points. I checked each finding and accepted all of them; the revision was made at 00:25 UTC.
- **Major.**
  - M1 (42.N1): Turing's method does not give the bulk count exactly. With the located sign changes it gives the index P(T) + Σ⌊m_ρ/2⌋ of Proposition 42.5, which does not separate off-line pairs from multiple zeros on the line (check R5c). Platt–Trudgian's verification concerns ζ only; Platt's verification of GRH for Dirichlet L-functions is now cited.
  - M2 (§5): the second line's contribution to the prime races is not absolutely convergent. It converges conditionally for nonprincipal χ and grows like log x for the principal character. It is o(√x) in both cases, so 42.N3 stands (check R4e).
- **Minor.**
  - m1: Z is the set of distinct zeros, and the weights m are written out.
  - m2: Proposition 42.2 now covers data from ℬ (absolutely convergent sums), which Corollary 42.3 uses. OMS6's sections are classes; the functions in ℬ are their test representatives ℛ_ρ(P).
  - m3: Rubinstein–Sarnak's existence theorem needs GRH only; absolute continuity and the density need GRH and linear independence. Devin and Platt are added to §8.
  - m4: I(T) is not the index asked for in `22_` §5, item 4; ⌊m_ρ/2⌋ replaces "half the excess multiplicities"; "I(T) = 0 for all T" is RH with simplicity; a positive index cannot always be certified by finite-precision computation (check R5d).
  - m5: the invariance hypothesis of 42.1 (χ and χ̄ equally often; check R2b); the rational terms −1/s − 1/(s + 1) of a trivial factor (check R2c); the polar terms in the explicit formula for Q_A (checks R3f–R3g); the operative reason in 42.N1 is that G_Λ and its explicit formula are functions of Λ.
  - m6: the introduction and §§5–6 now agree on which directions are negative.
  - m7: the checks that cannot fail are named in §7, and the bound on E_G − E is the one verified at every prime (0.0018).
- **New checks.** `checks/referee19_notes41_42_checks.py`, 29 items, all pass, adapted from the referee's script. The referee's items that documented the findings are now checks of the corrected statements.
- **Downstream.** Register S72, negative result 74 and bridge 44; digest §2 item 30, §3 item 42, the header and §6.
