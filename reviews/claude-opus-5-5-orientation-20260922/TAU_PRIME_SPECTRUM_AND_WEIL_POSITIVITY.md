# τ, the prime spectrum, and Weil's positivity condition: a restart from the first papers

- **Prepared:** 22 September 2026, by Claude (Anthropic; model id `claude-opus-5-5`), in a Cowork session, at the owner's request ("restart from there").
- **Scope of claims:** every statement below is one of:
  - quoted from a named source with a line locator;
  - proved here;
  - labelled **[open]** or **[inference]**.
- **Checks:** nothing in this note has been Lean-checked. No numerical claim is made except where a script is named.

## 0. Sources used as the basis

The two first papers are the owner's manuscripts. They are cited here by theorem label and line number but are not reproduced.

**P1 = `split_zero_projective_monads_surcomplex.tex`** (23 June 2026):
- Definition of G(R) (l.254);
- prime classification, Theorem `thm:prime-classification` (l.976);
- generic-point suspension, `thm:generic-suspension` (l.1009);
- stalks, `cor:split-stalks` (l.1039);
- finite products and absolute halo, `thm:product-ring-reflection` (l.596).

**P2 = `split_support_geometry_arithmetic_curve_v11.tex`** (6 July 2026):
- G_L(R), `def:lattice-split` (l.1229);
- Boolean characters, `thm:lattice-boolean-characters` (l.1312);
- support localization, `thm:lattice-localization` (l.1457);
- ideal classification, `thm:lattice-ideal-classification` (l.1619);
- prime classification, `thm:lattice-prime-classification` (l.1662);
- **spectral ordinal sum**, `thm:spectral-ordinal-sum` (l.1710);
- Krull dimension, `cor:lattice-split-dimension` (l.1750);
- Connes–Consani package, `thm:cc-package` (l.4598);
- zero Abel–Jacobi fibre, `thm:abel-jacobi-resolution` (l.4695);
- global-field rigidity of balanced supports, `thm:global-field-balanced-supports` (l.5439) and `thm:q-balanced-supports` (l.5507);
- trivial-place neutrality, `thm:trivial-place-neutrality` (l.5543);
- three local states, `prop:three-metric-support-states` (l.5705).

**Weil's form** uses the repository's own convention, `satellites/22_rh_counterexample_routes.tex:348–398`:
- f̂(z) = ∫ f(u) e^{−iuz} du;
- f^⋆(u) = conj f(−u);
- W(f,g) = Σ_ρ m_ρ conj(f̂(γ̄_ρ)) ĝ(γ_ρ), with γ_ρ = (ρ−½)/i;
- the explicit formula `eq:rh-full-weil-test`: pole terms, plus the Gamma integral with weight G(t) = (Re ψ(¼+it/2) − log π)/2π, minus Σ_n Λ(n)n^{−1/2}{h(log n)+h(−log n)}, where h = f∗f^⋆.

"Positive type" means h = f∗f^⋆ with f ∈ C_c^∞(ℝ). Then h(0) = ‖f‖₂² and W(h) := W(f,f).

---

## 1. What τ does to the prime spectrum

### 1.1 The scalar case, L = 𝔹

This is quoted from P1, Theorems `thm:prime-classification` and `thm:generic-suspension`.

- Spec G(R) = {P_τ} ⊔ {P_𝔭 : 𝔭 ∈ Spec R}, with P_τ = {τ} and P_𝔭 = 𝔭 ∪ {τ}.
- P_τ is open, dense, and contained in every prime.
- V(e) ≅ Spec R, and D(e) = {P_τ}.
- The stalk at P_τ is 𝔹 (P1 `cor:split-stalks`).

For R = ℤ this gives the chain P_τ ⊊ P_0 ⊊ P_p. The classical generic point (0) becomes the non-minimal prime P_0 = {τ, e}.

### 1.2 The lattice case

This is quoted from P2, Theorem `thm:spectral-ordinal-sum`:

> Spec G_L(R) ≅ SpecLat(L) ▶ Spec R.

- **Topology.** Every lattice prime generizes every ring prime. D(e_L) = SpecLat(L) and V(e_L) = Spec R.
- **Dimension.** dim G_L(R) = dim SpecLat(L) + dim R + 1 (`cor:lattice-split-dimension`).

The following refinements are proved here from P2's classification.

**(a) Number of added points.** For finite L, the added points are the prime lattice ideals of L. These are in bijection with the join-irreducibles J(L), via 𝔭_j = {λ : j ≰ λ} (P2 `thm:birkhoff-support-coordinates`, l.1359).

*Proof.* The complement of a prime lattice ideal is a prime filter. In a finite distributive lattice a prime filter is principal, ↑j, with j join-prime, hence join-irreducible. ∎

So the scalar τ adds 1 point, L = 𝔹ⁿ adds n incomparable points, and the chain C_2 adds 2 points in a chain.

**(b) When {τ_L} is prime.** {τ_L} = Z_{{0_L}} is prime iff 0_L is meet-prime (λ∧μ = 0_L ⇒ λ = 0_L or μ = 0_L).

*Proof.* This is P2 `thm:lattice-prime-classification` applied to 𝔭 = {0_L}. ∎

- For L = 𝔹ⁿ with n ≥ 2 this fails, because z_{{i}}·z_{{j}} = τ for i ≠ j. This was also observed in a parallel session on 22 September.
- For every chain, including C_2, {τ} is prime.

**(c) Closed points and residue rings.** The closed points are the Q_p = I_{pℤ}. The Bourne quotient of G_L(ℤ) by Q_p is 𝔽_p.

*Proof.*
- For supported r, s: r + a = s + b with a, b ∈ Q_p forces r ≡ s (mod p), because adding a support-only element does not change a supported one.
- Every z_λ satisfies z_λ + e = e + e with e ∈ Q_p, so z_λ is identified with 0.

∎

The separated congruence (Note 1, Theorem 3.4 for L = 𝔹) keeps the support states apart and gives G_L(ℤ/pℤ). That ring has p + |L| − 1 elements.

**(d) The place-lattice version.** Take L to be the Boolean algebra 𝒫(Ω_ℚ) of all sets of places. This is the measure algebra of the counting measure, P2 `cor:adelic-lattice-support` (l.5348). Then SpecLat(L) is the Stone space βΩ_ℚ.

*Proof.* Prime ideals of a Boolean algebra are exactly the complements of ultrafilters, and P2's classification needs no finiteness of L. The basic opens D(z_A) = {U : A ∈ U} give the Stone topology. ∎

So place support adds to the spectrum:
- the principal ultrafilters, which are the places themselves;
- the non-principal ultrafilters, which are limits of primes. There are 2^{2^{ℵ₀}} of them.

### 1.3 Two facts that fix the role of the new points

- **Not places.** The new points are generic, not closed, and they index no completion.
  - The stalk at a support prime is a lattice semiring, ↓λ (P2 `thm:lattice-localization`).
  - Scalar Booleanization forgets the absolute value at every place (P2 `thm:absolute-value-boolean-no-go`, l.5685).
  - **[inference]** If such a point is nevertheless made into a place of an adelic curve, the natural choice is the trivial absolute value. P2 `thm:trivial-place-neutrality` proves that trivial places change neither heights nor the product formula.
- **The zero Abel–Jacobi fibre.** P2 `thm:abel-jacobi-resolution` sends P_τ to the Connes–Consani trivial point {0} and P_0 to ℤ. Both lie over the zero divisor class, and the split spectrum separates them.

---

## 2. Where primes enter Weil's criterion, and what τ changes

Primes enter Weil's criterion in four ways. The effect of τ on each is computed below.

### 2.1 Euler factors through ideal norms: unchanged

With Bourne norms:
- every amplitude ideal I_J has quotient ℤ/J, so it has norm n when J = nℤ;
- every pure-support ideal Z_𝔞 has infinite quotient, because the supported copy of ℤ survives. It therefore has no finite norm.

So Σ N(I)^{−s} over the ideals of finite norm is ζ(s). The Euler factors, and hence the explicit formula and W, are literally unchanged. For L = 𝔹 this is Note 1, Corollary 3.5. The same proof applies for all L, using P2 `thm:lattice-ideal-classification`. ∎

### 2.2 Separated norms: no Euler product and no Riemann functional equation

With N^sep(I_n) := |G_L(ℤ/n)| = n + |L| − 1, the series is

Σ_n N^sep(I_n)^{−s} = ζ(s, |L|) = ζ(s) − Σ_{k<|L|} k^{−s}.

For |L| ≥ 2 its first coefficient is 0, so its coefficients are not multiplicative and it has no Euler product.

It does not satisfy ζ's functional equation either. By Hamburger (Math. Z. 10 (1921) 240–254), any such Dirichlet series is a constant multiple of ζ. That is impossible here, since the coefficient at 1 is 0 and the coefficient at |L| is 1. ∎

For L = 𝔹 this is the separated sheet ζ − 1 of Note 2, Proposition 4.2 and Theorem 5.12. Weil's explicit formula, and with it Weil's criterion, does not exist on this sheet.

### 2.3 Local fixed points: extra terms

**Count.** Let u ∈ (ℤ/pⁿ)^× act by multiplication on G_L(ℤ/pⁿ). Then

#Fix(u) = p^{min(n, v_p(u−1))} + |L| − 1.

*Proof.* A supported x is fixed iff (u−1)x = 0. That has p^{min(n,v)} solutions, including x = e. Every support-only state z_λ with λ ≠ 1_L is fixed, since u·z_λ = z_{1∧λ} = z_λ. ∎

Two remarks on this count:
- The first term equals |1−u|_p^{−1} for n > v. This is the density whose integral is Weil's local term at p (Connes, Selecta Math. 5 (1999) 29–106).
- The number of added fixed states is |L| − 1, which is **not** the number of added generic primes |J(L)|. For 𝔹ⁿ the two numbers are 2ⁿ − 1 and n.

**Local trace.** On the split local space G_L(ℚ_p) = ℚ_p ⊔ {z_λ : λ ≠ 1}, the function space is 𝒮(ℚ_p) ⊕ ℂ^{L∖{1}}, and the finite summand carries the trivial action. So

Tr^L_p(h) = Tr_p(h) + (|L|−1) ∫_{ℚ_p^×} h(u) d^×u.

This is exact: the second term is a trace on a finite-dimensional space.

**Global.** Normalize so that the classical term at p carries the weight log p, as in Weil's formula. Then the τ-term at p contains the diagonal part (|L|−1)·log p·h(0) (the m = 0 shell |u|_p = 1). Since Σ_p log p = ∞, adjoining the states at every finite prime makes the τ-contribution diverge on every h with h(0) ≠ 0. That includes every nonzero positive-type h, since h(0) = ‖f‖² > 0.

For a finite set of primes S, the contribution is

E^L_S(h) = (|L|−1) Σ_{p∈S} log p [ h(0) + Σ_{m≠0} η_h(p^m) ],

where η_h is h written multiplicatively in the same normalization.

### 2.4 One global τ-point: a trivial-character term that vanishes on the τ-base test space

A single point fixed by the whole idele class group adds a one-dimensional summand with a character of |u|. Its trace is ∫ h(u)|u|^w d^×u. For weight w ∈ {0, 1} this is exactly the shape of a pole term, ĥ(±i/2).

In the τ-base model, the two characters of weight 0 and 1 are carried exactly by the moment map m(φ) = (φ(0), ∫φ), onto the lines 𝓛₀ and 𝓛₁ (`workbenches/tau-base-cohomology/TAU_BASE_MODEL.md:252–258`, with m U_a = diag(1,a) m).

Couple the τ-summand to the test space through the corresponding moment functional. On the model's own test space V = {φ even, φ(0) = 0, φ̂(0) = 0} (`TAU_BASE_MODEL.md:90–92`), both moment functionals vanish. So such a term contributes 0 on V. ∎ The coupling through the moment functional is the identification stated in this paragraph; it is not a further theorem.

### 2.5 Non-principal ultrafilter points: nothing beyond diagonal terms

Let supp h ⊂ [−A, A]. The classical local term at p vanishes once log p > A, because every m ≥ 1 then has m log p outside the support. A non-principal ultrafilter contains every cofinite set of primes, so every ultrafilter limit of the classical local terms is 0.

Of the τ-terms, only the diagonal m = 0 term survives for such primes. ∎

---

## 3. Two theorems on diagonal shifts of Weil's functional

Everything τ adds in §2.3–2.5 is either a pole-type term or a multiple of h(0), except the off-diagonal part of E^L_S. The following two theorems decide exactly what diagonal terms can do.

### Lemma U

If RH is false, there is a φ ∈ C_c^∞(ℝ) such that T ↦ F(T) := W(φ, φ(·−T)) is unbounded on [0, ∞).

**Proof.**

*Step 1: the series for F.* Choose an off-line zero ρ₀ with β₀ < ½; one exists by the symmetry ρ ↔ 1−ρ̄. Then Im γ_{ρ₀} = ½ − β₀ > 0. Choose φ ∈ C_c^∞, supported in [−A, A], with φ̂(γ_{ρ₀}) ≠ 0 and φ̂(γ̄_{ρ₀}) ≠ 0. Since φ(·−T)^ = e^{−iTz}φ̂,

F(T) = Σ_ρ m_ρ b_ρ e^{−iTγ_ρ}, with b_ρ = φ̂(γ_ρ) conj(φ̂(γ̄_ρ)).

We have |b_ρ| ≤ C_N (1+|Re γ_ρ|)^{−2N} e^{A}, because |Im γ_ρ| ≤ ½. Together with the zero count O(t log t), this makes the series absolutely convergent for every T, with |e^{−iTγ_ρ}| = e^{T Im γ_ρ} ≤ e^{T/2}.

*Step 2: the Laplace transform.* Suppose sup_{T≥0} |F| < ∞. Then L(s) = ∫₀^∞ F(T) e^{−sT} dT is analytic on Re s > 0. For Re s > ½, Fubini applies and gives L(s) = Σ_ρ m_ρ b_ρ/(s + iγ_ρ).

The series converges locally uniformly away from the points s_ρ = −iγ_ρ, so it is meromorphic on ℂ. Its residue at s_{ρ₀} is m_{ρ₀} b_{ρ₀} ≠ 0, and Re s_{ρ₀} = ½ − β₀ > 0.

*Step 3: the contradiction.* L and the series agree on Re s > ½. By the identity theorem the series would then be analytic at s_{ρ₀}, which is a contradiction. ∎

### Theorem B (positive diagonal shifts do not change the criterion)

For every c ≥ 0:

RH ⟺ W(h) + c·h(0) ≥ 0 for every positive-type h ∈ C_c^∞(ℝ).

**Proof.**

*⇒.* Under RH, W(h) = Σ_ρ m_ρ |f̂(γ_ρ)|² ≥ 0, and h(0) ≥ 0.

*⇐.* Suppose RH is false. Take φ from Lemma U. Choose T > 2A with

|F(T)| > W(φ,φ) + c‖φ‖².

Such a T exists: F is unbounded on [0, ∞) but bounded on [0, 2A]. Put f = φ + ζφ(·−T) with ζ = −conj F(T)/|F(T)|.

W is Hermitian and translation-invariant, since W(φ_T, φ_T) = W(φ, φ). Hence

W(f,f) = 2W(φ,φ) + 2Re(ζF(T)) = 2W(φ,φ) − 2|F(T)|,

and ‖f‖² = 2‖φ‖² because the supports are disjoint. So W(f,f) + c‖f‖² < 0, with h = f∗f^⋆ of positive type. ∎

### Theorem A (negative diagonal shifts destroy positivity unconditionally)

For every c > 0 there is a positive-type h ∈ C_c^∞ with W(h) − c·h(0) < 0.

**Proof.**

- *If RH is false:* use Theorem B with c = 0.
- *If RH is true:* take g ∈ C_c^∞ nonzero and g_λ(u) = g(u/λ), so ĝ_λ(z) = λ ĝ(λz). Then:
  - W(g_λ, g_λ) = λ² Σ_ρ m_ρ |ĝ(λγ_ρ)|² ≤ C_N λ^{2−2N} Σ_ρ m_ρ |γ_ρ|^{−2N};
  - ‖g_λ‖² = λ‖g‖².

  So the ratio W/h(0) is O(λ^{1−2N}), which tends to 0.

∎

### Consequences for τ (proved from §2 together with Theorems A and B)

**1. Fixed points.** Suppose the τ-states of §2.3 are counted among the fixed points in the Lefschetz balance, so that W = poles − fixed points. Then they subtract E^L_S.

- For S = all primes, the functional is −∞ on every nonzero positive-type h.
- For finite S, restrict to positive-type h with supp h ⊂ (−log 2, log 2). All prime terms and all m ≠ 0 τ-terms vanish there, so

  W^τ_S(h) = W_∞(h) − (|L|−1)·ϑ_S·h(0), with ϑ_S = Σ_{p∈S} log p.

  On this small-support class:
  - Yoshida's theorem gives W_∞ ≥ 0 on the subclass with ĥ(±i/2) = 0 (Yoshida 1992, quoted in the introduction of Connes–Consani, Selecta Math. 27 (2021), Art. 77).
  - So the τ-augmented functional stays positive exactly while (|L|−1)ϑ_S ≤ κ_∞, where κ_∞ := inf W_∞(h)/h(0) over that subclass. **[open]** κ_∞ is a computable archimedean constant; its value has not been computed.

**2. Other accountings.** If the τ-states are counted with the opposite sign, or as separate H⁰ classes (so that they cancel), then by Theorem B, or trivially, the criterion is unchanged and still equivalent to RH.

**3. Pole-type and ultrafilter terms.** The pole-type terms of §2.4 vanish on V. The ultrafilter terms of §2.5 are diagonal.

**Summary [proved for the constructions above].** Through these channels, τ either leaves Weil's criterion exactly equivalent to RH, or makes it fail regardless of RH. It cannot, through these channels, make Weil positivity easier to prove. **[open]** The off-diagonal part (|L|−1) Σ_{p∈S} log p Σ_{m≠0} η_h(p^m) is not covered by Theorems A and B. Its normalization depends on the weight given to τ-states, and it is the one remaining τ-channel of §2.

---

## 4. Where τ does meet Weil positivity: the support of the Weil pairing

Let each zero carry a two-channel mask μ(ρ) ∈ 𝔹² = 𝒫({+,−}):
- μ(ρ) = {+,−} if Re ρ = ½;
- μ(ρ) = {+} if Re ρ > ½;
- μ(ρ) = {−} if Re ρ < ½.

Weil's form pairs ρ with ρ* := 1−ρ̄ (this is γ ↦ γ̄), and μ(ρ*) is μ(ρ) with + and − swapped.

**Proposition.** Let Z be a finite set of zeros closed under ρ ↦ ρ*. Let B_Z(a) = Σ_{ρ∈Z} m_ρ conj(a_{ρ*}) a_ρ on ℂ^Z.

1. The pairing term of ρ lies over the mask product z_{μ(ρ)}·z_{μ(ρ*)} in G_{𝔹²}(ℂ). That product is e_L when ρ is on the line, and τ when ρ is off the line.
2. B_Z is positive semidefinite iff no zero in Z has pairing support τ. Each off-line pair contributes a hyperbolic block of signature (1,1).

**Proof.**

- *Item 1.* For an on-line zero, ρ* = ρ and the mask product is {+,−}∧{+,−} = {+,−}, which corresponds to e_L. For an off-line zero, ρ* ≠ ρ and the product is {+}∧{−} = ∅, which corresponds to τ.
- *Item 2.* The form splits into blocks:
  - an on-line zero gives m_ρ|a_ρ|² ≥ 0;
  - an off-line pair gives m(conj(a_{ρ*})a_ρ + conj(a_ρ)a_{ρ*}) = 2m Re(ā_ρ a_{ρ*}), whose matrix m·[[0,1],[1,0]] has eigenvalues ±m.

∎

Combined with Weil's criterion, this gives the reformulation (not a proof):

> RH ⟺ no zero's Weil pairing is τ-supported ⟺ the zero set admits the one-channel labelling (L = 𝔹), in which {τ} is prime.

The parallel-session finding that {τ} is not prime in G_{𝔹²} is exactly the algebraic fact behind the negative directions: an off-line pairing is a factorization τ = z_{+}·z_{−}.

This is also the structure of the programme's own finite packets.
- The τ-base trace contraction R_Z(f, J_g h) = Σ m_ρ conj(f(1−ρ̄)) h(ρ) (`TAU_BASE_MODEL.md:315–317`) is B_Z.
- Proposition 3 of this directory's `README.md` shows that on the test functions P·v_h this form equals Weil's form, computed by the explicit formula including the primes. That identity was checked to 1.3·10⁻³³ on the first zero pair.
- So the τ-supported blocks of the τ-base pairing are exactly where arithmetic (the primes) must supply positivity.

---

## 5. Next calculations [recommendations]

1. **Compute κ_∞.** κ_∞ = inf W_∞(h)/h(0) over positive-type h with supp ⊂ (−log 2, log 2) and ĥ(±i/2) = 0. Compute it with rigorous interval arithmetic. It is the threshold at which τ-fixed points at the primes in S break positivity (§3, consequence 1).
2. **Fix the τ accounting.** In Spec G(ℤ), P_τ is dense, not an isolated component. So adding it does not add an H⁰ class for the constant sheaf, and the Lefschetz balance has to absorb its fixed point elsewhere. Decide this in a stratified split adele class space whose strata are indexed by place supports A. Compare those strata with Connes' semilocal spaces X_S = 𝔸_S/O_S^×. P2's rigidity theorem, "only ∅ and Ω are balanced", suggests that the proper strata are exactly the non-Hausdorff ones.
3. **The off-diagonal τ-term.** Determine the correct weight of τ-states (half-twist or none). Then compute the off-diagonal τ-term's Hermitian form on V, and its interaction with W, as a finite matrix on the packet test space.
4. **The two-channel packet form.** Compute the arithmetic side of B_h on {P·v_h : deg P ≤ 3} (pole, Gamma and prime parts) as 4×4 matrices in (δ, γ), separating the e-supported diagonal blocks from the τ-supported cross blocks.

## 6. Provenance

- **Sources:** all quoted results are from the owner's papers P1 and P2, with the line locators above.
- **Proved here:** 1.2(a)–(d), 2.1–2.5, Lemma U, Theorems A and B, and the §4 Proposition.
- **External theorems used:**
  - Hamburger (1921);
  - Weil's explicit formula (Weil 1952), in the repository's convention;
  - Connes (1999) for the local trace density;
  - Yoshida (1992) as quoted by Connes–Consani (2021);
  - Stone duality for Boolean algebras.
