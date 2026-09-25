# Where the second attempt's RH lanes use arithmetic: the Euler test, Deligne's inputs, and the square

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, revision 3 (revision 2 at 04:40 UTC; revision 3 at 04:56 UTC adds item (e) of §3).

Revision 2 corrects the first version after two readings:

- an independent referee pass by a Claude subagent, listed in the appendix;
- a first reading by the Codex lane, which the owner relayed.

The corrections are listed at the end.

This note looks at the second attempt from outside its own conception, as the owner asked. It applies two external tests to the proofs mapped in `01_`, `04_`, `05_` and `07_`:

- **The Euler test** (§2) asks which proved statements remain true, word for word, for a zeta function whose "integers" do not factor uniquely and which has zeros off the critical line.
- **Deligne's inputs** (§3) asks which inputs of Deligne's weight argument the programme's constructions supply, in the files I have read.

Section 4 places the question in the F1 literature. Each claim carries its proof or a citation, and sentences that are my assessment say so.

## 1. A test sheet from the owner's own family

The Connes–Consani summation map acts on even test functions. On the shifted lattice ℤ + a it gives

  Σ_a h(u) = Σ_{n∈ℤ} h((n+a)u),  M(Σ_a h)(z) = Z_a(z) · M_S h(z),  Z_a(s) = ζ(s,a) + ζ(s,1−a),  0 < a < 1.

This is the even (parity-symmetrized) shadow of the owner's flow ζ(s, 1+t), with a = 1 + t. At a = 1 the lattice is ℤ, and the term n = 0 vanishes because h(0) = 0. The result is the programme's own Σ, with Mellin factor 2ζ.

**Lemma 1 (the test sheet is admissible).** For every a ∈ (0,1) and every h ∈ S, the function Σ_a h lies in the programme's space A (MCL1.1).

*Proof.*
1. **Large u.** As u → ∞, every term and every (u∂_u)-derivative decays faster than any power. This holds because h is Schwartz and |n + a| ≥ min(a, 1−a) > 0.
2. **Small u.** As u → 0, Poisson summation gives Σ_{n∈ℤ} h((n+a)u) = u^{−1} Σ_{k∈ℤ} ĥ(k/u) e^{2πika}. The k = 0 term is u^{−1}∫h = 0, and the remaining terms decay faster than any power of u.
3. **Mellin side.**
   - Z_a has a simple pole at 1. It is cancelled by M_S h(1) = ½∫h = 0.
   - Z_a(−2k) = −(B_{2k+1}(a) + B_{2k+1}(1−a))/(2k+1) = 0 for k ≥ 1, because B_n(1−x) = (−1)^n B_n(x). These zeros cancel the poles of M_S h at −2k.
   - The same identity at k = 0 gives Z_a(0) = 0 on every sheet. ∎

Two cautions.

- M_{S,z} is defined for Re z > −2 (MCL1.3). Some sheets have nontrivial zeros further left; for example, Z_{0.24} has a real zero at −2.95007 (found by the referee). Everything below concerns zeros with Re z > −2.
- Eulerian sheets also have zeros off the critical line: Z_a(0) = 0 always, and finite Euler factors vanish on Re s = 0 (for instance, Z_{1/3} = (3^s − 1)ζ(s)). The test is therefore about zeros in Re s > ½.

**Lemma 2 (the sheet a = 1/q, and when it is Eulerian).** Put S_q = {n ≥ 1 : n ≡ ±1 mod q}. Then

  Z_{1/q}(s) = q^s D_q(s),  D_q(s) = Σ_{n∈S_q} n^{−s} = (2/φ(q)) Σ_{χ even mod q} L(s, χ)  (q ≥ 3).

For q = 2 the two Hurwitz terms coincide, and Z_{1/2} = 2 · 2^s D_2. S_q is closed under multiplication, because (±1)(±1) = ±1. The following are equivalent:

- (i) the monoid S_q is free (unique factorization into irreducibles);
- (ii) φ(q) ≤ 2, that is, q ∈ {1, 2, 3, 4, 6};
- (iii) the formal logarithm log D_q = Σ_{n≥2} r_n n^{−s} has all r_n ≥ 0;
- (iv) D_q has no zeros in Re s > 1.

*Proof.*
- **(ii) ⇒ (i).** When φ(q) ≤ 2, the units mod q are ±1. So S_q is the set of integers coprime to q, which is free on the primes not dividing q.
- **(i) ⇒ (iii).** A free monoid gives an Euler product, whose logarithm has coefficient 1/k at π^k for each generator π and 0 elsewhere.
- **(iii) ⇒ (iv).**
  - The exponential of a series with nonnegative coefficients has coefficients at least as large as those of the series. So Σ r_n n^{−σ} ≤ D_q(σ) < ∞ for σ > 1.
  - Hence log D_q converges absolutely on Re s > 1, and D_q = exp(log D_q) does not vanish there.
- **(iv) ⇒ (ii).**
  - If φ(q) > 2, there are φ(q)/2 ≥ 2 even characters. So D_q has nonzero components along at least two distinct primitive characters, the trivial one and another.
  - Saias–Weingartner decompose the periodic Dirichlet series into a direct sum of subspaces E_{q,ψ}, one for each primitive ψ ([Acta Arith. 140 (2009) 335–344](https://arxiv.org/abs/0807.0783), Theorem 1). D_q therefore lies in no single E_{q,ψ}.
  - Their Theorem 4 then gives η > 0 such that the number of zeros with 1/2 < σ₁ < Re s < σ₂ ≤ 1 + η and |Im s| ≤ T grows like T.
  - Taking σ₁ > 1 gives zeros in Re s > 1.
- **(i) ⇒ (ii), directly.**
  - Suppose φ(q) > 2. Choose a unit c ≢ ±1 mod q. By Dirichlet's theorem, choose primes p ≠ r ≡ c and p′ ≠ r′ ≡ c^{−1}.
  - Then pp′, rr′, pr′ and rp′ are irreducible in S_q, because p, p′, r, r′ ∉ S_q.
  - Yet (pp′)(rr′) = (pr′)(rp′). ∎

**Computed example, q = 5.**

- **Logarithm.** Computed in exact rational arithmetic (`checks/monoid_log.py`, confirmed by the referee with an independent recursion).
  - The irreducibles of S_5 begin 4, 6, 9, 11, 14, 19, 21, 26, …, and 36 = 4·9 = 6·6.
  - The formal logarithm has r_36 = −1/2, its first negative coefficient. Among n ≤ 3000, 105 have r_n < 0.
- **Zeros.** Off-line zeros of Z_{1/5} appear from height 15.70 on.
  - The lowest has s = 0.54306884072582709337 + 15.704048267909062575i.
  - The referee counted zeros by the argument principle in python-flint/Arb, with an adaptive step that cannot skip a phase jump. Below height 150 there are exactly 24 zeros with Re s > 0.505. Of these, 21 have Re s > 0.52, 14 have Re s > 0.55 and 8 have Re s > 0.6.
  - The largest real part is 0.70907, at height 29.95, and none has Re s > 1.
  - My first search found only 13 of the 24. The referee located the others, and I re-verified four of them at 30 digits: 0.52473+32.98577i, 0.51038+58.51251i, 0.55954+105.89142i and 0.56607+139.45659i.
  - Zeros with Re s > 1 exist by Saias–Weingartner, but lie above height 150.

*Remark (an observation, not a claim of significance).* The Eulerian sheets a = 1/q are those with (ℤ/q)^× = {±1}. These are the q for which the sign units ±1 exhaust the units mod q; ±1 are the units of Connes–Consani's 𝔽_{1²} = 𝔽_1[μ_2].

## 2. The Euler test applied to the proved statements

On the sheet a = 1/5, factorization is not unique and there are zeros in Re s > ½ (Lemma 2). A statement that holds there word for word cannot, by itself, distinguish the critical line. A statement that fails there has used a property special to the Eulerian sheets.

**Transfers word for word.** Replace 2ζ by Z_a; nothing else changes.

- MCL3 and MCL3.4: the classification of generalized characters of A′, and the two-prime lemma. These do not involve ζ.
- MCL4–MCL7: independence of the source jets, the least-order lift, the finite block MCL6.3, and the dilation defect.
- ORE6.2 and ORE6.5: the single Jordan chain, and the truncation statement.
- IH6.4 and the first two laws of IH6.5: faithfulness and prime intertwining of the two-prime receiver. They need a bounded real part of the zeros, the zero count, and the density of (log 2)ℤ + (log 3)ℤ.
- PL2.1: linearity of clock changes.

**Transfers in substance, not word for word.**

- MCL9.1 and ORE1.3 build Q′ with the closed-image theorem. ORE4.7, ORE4.9 and ORE6.1 use the global projector ORE3.2.
- Taking Q′ := J^⊥ instead, the finite-block content of MCL9.2–MCL9.6 and ORE4.8 goes through, as the referee checked. This covers the connecting representative, its nonzero top coefficient, and the least-order statements.
- I did not check whether the closed image (OMS/SSI), the global projectors (ORE3.2), or the residue pairing with 1/Z_a (GZR, RPC, ORE5) extend to other sheets.

**Changes on other sheets.**

- **The reflection laws**: MCL8.6, ORE5, the third law of IH6.5, PL2.5–PL2.7 (which place the critical line through s ↦ 1/c − s), and PL6.8.
  - Poisson summation gives RΣ_a = Σ^{cos}_a 𝓕, with M(Σ^{cos}_a h) = Φ_a · M_S h and Φ_a(s) = 2Σ_{k≥1} cos(2πka) k^{−s}. The reflection therefore pairs the zeros of Z_a with those of Φ_a.
  - For a = 1/3 the two agree up to finite factors: Φ_{1/3} = (3^{1−s} − 1)ζ.
  - For a = 1/5, Φ_{1/5} = ½[(5^{1−s} − 1)ζ(s) + √5 L(s, χ_5)], whereas 2D_5 = (1 − 5^{−s})ζ(s) + L(s, χ_5). Φ_{1/5} does not vanish at the lowest zero of D_5 (`checks/z15_zero_check.py`).
- **The positive return measure** (TP0–TP14, DR1–DR4).
  - The programme's timed primes give D = exp_*(R) with R ≥ 0. DR1.5 says this is exactly unique factorization.
  - On the sheet 1/5 the logarithm has negative atoms, at log 36, log 84, log 126, … So the Hadamard–de la Vallée Poussin argument (DB9, DR4) is unavailable there.
  - Positivity would in fact give nonvanishing on all of Re s > 1 (Lemma 2, (iii) ⇒ (iv)), and that is false on this sheet.
- **Theorem E and N1/S7** (`06_`, register S5 and S7). The velocity spectrum is multiplicative exactly on the Eulerian sheets of the one-sided flow.
- **The prime clocks and the Bost–Connes relations** (P1–P14, `01_`). They are built from End(L) ≅ ℤ, whose positive part is a free monoid.

**Assessment.** The lifting algebra of the character-lifting lane does not see the sheet. Four inputs do:

- unique factorization;
- the positive timed-prime measure;
- the prime clocks;
- the self-dual form of the functional equation.

A step that is to separate the critical line from the rest of Re s > ½ therefore has to use at least one of these. Section 3 compares them with what Deligne's argument uses.

## 3. Deligne's inputs, and what the programme's constructions supply

I name the inputs I1–I4 to avoid a clash with the Input D1–D6 labels of the lane's DW1. The lane's reconstruction of Weil II §§3.2–3.3 (DW11.1, read in full; mapped in `07_`, item 13) proves that a lisse sheaf F, pure of weight β on a curve, has middle-extension H¹(X, j_*F) pure of weight β + 1 (DW8.4). Purity concerns this middle extension. Boundary contributions to H_c¹ can have lower weights (DW8, last paragraph); the Codex lane also stressed this point.

| Input | Role in Weil II | What the programme's constructions supply (files read) |
|---|---|---|
| **I1. Strict boundary estimate** (DW1 Input D5, Weil II 2.2.10) | Every eigenvalue on H_c¹ has w < β + 2 (DW1.7). The strict sign comes from the Hadamard–de la Vallée Poussin argument of §2. | **Supplied.** R ≥ 0 gives ζ(1+it) ≠ 0 (DB9, DR4). With the functional equation this gives 0 < Re ρ < 1, which is the separation every TL receiver uses (`05_` §3). The same positivity, with standard growth bounds, also gives the classical zero-free region σ > 1 − c/log\|t\|. Sheet-sensitive (§2). |
| **I2. Duality with the Tate twist** | Pairing with F^∨(1) turns the upper bound into a lower bound on the middle extension (DW8.2–DW8.3). | **Supplied in character form.** Reflection ρ ↔ 1 − ρ (MCL8, ORE5). Degree-two duality a ↦ p/ā, whose fixed circle is \|a\|² = p (MDB9.9–9.10). Conjugation duality c_p^*(K̄_{ρ,p}) ⊗ K_{ρ#,p} ≅ K_{1,p}, where the pullback c_p^* is essential on the angular period (PL6.8). |
| **I3. Discrete weight congruence** (DW1 Input D4, local monodromy purity, Weil II 1.8.4) | Nonconstant pieces of the pencil's fibre cohomology have weight γ ∈ 2β + ℤ (DW5). With I1 this gives γ ≤ 2β + 1 (DW6), the one-unit gain. | **Not supplied in the files read.** In Weil II the congruence is proved for an auxiliary object, the pencil's fibre cohomology, and not for the H¹ being studied. For that H¹ the congruence would already be the conclusion: for ζ, 2Re ρ ∈ ℤ together with 0 < Re ρ < 1 says Re ρ = ½. No auxiliary object with discretely spaced weights has been constructed. IH5.3 excludes only one route: the p^ρ at three primes cannot be eigenvalues of a single finite integer matrix. IH5 itself says it does not exclude other comparisons with Deligne's framework. |
| **I4. Squares and tensor powers** | **Weil II §3.2.** H_c¹(U,F) ⊗ H_c¹(U,F) injects into H_c² of the blow-up Ṽ of U × U (DW7.8, DW2.2). H_c² is bounded through the pencil using I1, I3 and induction, and squaring halves the error: w(α) ≤ β + 1 + 2^{−k} for all k (DW7.9). **Weil II §1.5** (DP4–DP5), a separate use of tensor powers: the even powers F^{⊗2k} of a real sheaf have nonnegative L-coefficients (DP4.1). Their L-function has no pole in \|t\| < R_k = q^{−(2kr+2)/2}, a disc fixed by the curve's H_c² denominator uniformly in k (DP5.1). This bounds the local weights, w ≤ r + 1/k (DP5.3). | **Attempted, with computed outcomes.** TWC (all tensor powers of the specialization source) and FST (a square on one sphere) were published 24–25 September. I read FST in full and TWC6, TWC10 and TWC11. The outcomes are points (a)–(e) below. |

Points (a)–(e) of the I4 row:

- **(a)** A same-eigenvalue tensor power of an off-line λ carries the eigenvalue n^{kλ} on both source and target. So a tensor power alone produces no disjoint weights (TWC6.2, TWC11).
- **(b)** The positive forms compatible with the product transfer have common radical ker P_{𝒞_k}, where 𝒞_k = {Re σ(ρ) = k/2} and σ(ρ) = Σρ_j^# (TWC10.5, TWC2.1).
  - This radical kills every tuple off 𝒞_k, in particular the same-eigenvalue powers of an off-line zero.
  - For k = 1 it is the zero positive receiver of CPS (`04_`).
  - For k = 2 the reflected pairs (ρ, ρ^#) survive, with positive norm 2m²\|δ\|⁴ (TWC10.12) and modulus exactly n (TWC6.4). The original tensor Weil form is indefinite on them: +2m² on u + v and −2m² on u − v (TWC10.11).
- **(c)** In FST the square's invariant-cycle source V/ker d_0 is zero exactly when the original map b_r is zero (FST3).
  - Its top tensor detector is already a boundary (FST4.2). On the completed source only b₂(ℛ₂) ⊂ closure of im d₁ is proved (FST4.4).
  - FST obtains the fixed geometric +2 on one sphere. FST7 states that this does not allow Deligne's pole argument to be applied to the vanished top detector.
- **(d)** TWC11 records that neither the external product (degree increment 2k) nor the same-base complex has been assigned the fixed-curve cohomological denominator. TWC9 adds that its computation does not rule out such a construction.
- **(e)** The Codex lane reported a calculation in which the even tensor powers keep the spectral data and have nonnegative coefficients. I located it in revision 3: it is TWC7.
  - For a finite conjugation-stable set S of zeros, Tr(T_n^{⊗k} | J_S^{⊗k}) = (Σ_{ρ∈S} m_ρ n^ρ)^k. This is real, so its even powers are nonnegative, which is the DP4 step.
  - TWC7 states that this does not make the infinite trace converge and gives no global determinant.
  - What positivity then yields can be computed exactly. Put D_S^{(2k)}(s) = Σ_n (Σ_{ρ∈S} m_ρ n^ρ)^{2k} n^{−s}. Expanding, D_S^{(2k)}(s) is the sum, over 2k-tuples of zeros in S, of the products of their multiplicities times ζ(s − Σ_j ρ_j).
  - This series converges absolutely for Re s > 1 + 2kβ_max, where β_max = max_{ρ∈S} Re ρ. It has a pole with positive residue at the real point s = 1 + 2kβ_max, coming from the tuples (ρ, ρ̄, …, ρ, ρ̄) with Re ρ = β_max. Tuples with the same exponent sum cannot cancel there, because each residue is a positive product of multiplicities.
  - So the abscissa of convergence is exactly 1 + 2kβ_max. Positivity of the even powers therefore returns max Re ρ; it cannot bound it.
  - The DP5 half would be an independent bound on this abscissa of the form k + 1 + C, with C independent of k and S. Letting k → ∞, such a bound is equivalent to β_max ≤ ½. In Deligne's proof that bound comes from the H_c² of a fixed curve (DP5.1).
  - Codex says it is checking this against its newer boundary construction. It reports a ramified map with the exact factor n^{−1} in the nilpotent relation, which the ordinary counting map lacks.

**What I1 and I2 are used for.** In the programme's proved separations (TL, TL7, ORE6), I1 and I2 are used to produce the strip 0 < Re ρ < 1. In Deligne's scheme, the step from the boundary to the middle uses I3 and I4 together: a discreteness gain on an auxiliary object, transported through the square. Alternatively, in §1.5 form, it uses positivity of even tensor powers together with a pole bound uniform in k. In the files I have read, the programme supplies I1, I2 and positivity of tensor powers. It has not yet supplied I3 or the uniform pole bound. Whether its constructions can supply them is open; IH5 and TWC9 both say so.

## 4. The F1 framing of the question

Stated without the programme's vocabulary, the weight lane has arrived at this question:

> Over the reconstructed arithmetic, construct a square with a Künneth-type map from H¹ ⊗ H¹ into its H², together with either (a) an auxiliary object whose weights are discrete, or (b) a pole bound for the positive even tensor powers that is uniform in the power.

**The literature on its first ingredient, the square:**

- **Manin 1995.** Yu. I. Manin, *Lectures on zeta functions and motives (according to Deninger and Kurokawa)*, Astérisque 228 (1995) 121–163 ([numdam](https://www.numdam.org/item/AST_1995__228__121_0/)).
  - Manin asks in his introduction (§0) for a category containing "absolute Descartes powers" Spec ℤ × … × Spec ℤ.
  - In §1.4 he presents Kurokawa's tensor product of zeta functions. In the additive case it is (H₁ ⊗ H₂, Φ₁ ⊗ id + id ⊗ Φ₂) (eq. 1.22), whose spectral parameters are the sums ρ + ρ′. This is the additive form of the step α ↦ α² in I4.
  - Manin cites Kurokawa's source as a 1990 preprint. Its published version is N. Kurokawa, *Multiple zeta functions: an example*, in *Zeta Functions in Geometry*, Adv. Stud. Pure Math. 21 (1992) ([doi:10.2969/aspm/02110219](https://doi.org/10.2969/aspm/02110219)). The DOI's suffix indicates p. 219; the page itself was blocked for both of us.
  - Deninger's regularized-determinant formula for the completed zeta, an alternating product over the H^i, is Manin's eq. (1.5) in §1.1.
- **Connes 2016.** Weil's proof for curves uses Riemann–Roch on C̄ × C̄ (A. Connes, *An essay on the Riemann Hypothesis*, [arXiv:1509.05576](https://arxiv.org/abs/1509.05576), §2.3). Connes introduces the square of the arithmetic site in §4.3.1. Table 1 in §4.3.2 pairs X = C̄ × C̄ with Â × Â, where Â is the scaling site.

The second ingredient, either (a) or (b), is specific to Deligne's argument. It is not a question from the F1 literature.

**Assessment.** The second attempt reaches this question from the owner's side: the τ-supported source, its winding ring, the timed primes, and the lifting through the Connes–Consani summation map. What its proved results provide:

- a positivity-and-duality package that reaches Re s = 1 and the functional equation; on the sheets a = 1/q, positivity holds exactly when the monoid S_q is free (Lemma 2);
- a lifting calculus that locates the obstruction class, the functional-equation germ (`07_`, item 7), without separating it by weight;
- its own construction of a square and of all tensor powers (TWC, FST), with computed outcomes (a)–(d). This sits beside Connes–Consani's square of the arithmetic site, a different construction.

The part left open is the one named in the question above.

## Appendix A: checks

- **`checks/monoid_log.py`.** Exact formal logarithms of D_5 and ζ up to n = 3000. The referee reproduced it with an independent recursion.
- **`checks/z15_scan.py`.** The first search: local minima of |F| on σ = 0.6, …, 1.1, refined by mpmath's `findroot` (secant method by default). It found 13 of the 24 zeros.
- **`checks/z15_zero_check.py`.**
  - It re-verifies the 13 listed zeros at 30 digits and the identity Z_{1/5} = 5^s F/2.
  - It also tests Φ_{1/5} at the lowest zero.
  - Its final line refers only to the listed points.
- **The count of 24.** This is the referee's python-flint/Arb argument-principle count. I re-verified four of the additional zeros with mpmath.
- **Status of the numerics.** They are illustration. The existence of off-line zeros is the theorem of Saias–Weingartner.

## Appendix B: corrections in revision 2

1. **Zero count.** Below height 150 there are 24 zeros with Re s > 0.505, not 13 (§1).
2. **Section 2 lists.**
   - MCL9, ORE2 and ORE4.7/4.9/6.1 use the closed image or the global projector. They transfer in substance, via Q′ := J^⊥, not word for word.
   - Only PL2.1 transfers.
   - The replacement is "2ζ by Z_a".
3. **Scope.** The test is about Re s > ½. Eulerian sheets also have zeros on Re s = 0.
4. **Table of inputs.**
   - The inputs are relabelled I1–I4.
   - Purity is stated for the middle extension.
   - I4 now uses H_c¹ ⊗ H_c¹ ↪ H_c²(Ṽ), and states the DP5.1 pole-free disc exactly.
   - PL6.8 is quoted with c_p^*.
   - The IH5.3 sentence is narrowed to what IH5 proves.
5. **Points (b) and (d).**
   - (b) now says "every tuple off 𝒞_k" and states what survives.
   - (d) now reports FST's +2 and TWC9's scope.
   - The claim that "positivity cannot see R" extends to every tensor power is withdrawn.
6. **Overstatements removed.**
   - "D1 and D2 prove nothing more".
   - "cannot supply D3 or D4". Codex also objected to this one.
   - "sharp".
   - "a first construction of the square".
   - "posed since Manin" for the whole question.
7. **Citations.**
   - Manin's "absolute Descartes powers" is in §0, not §1.6.
   - Deninger's formula is eq. (1.5) in §1.1.
   - Connes' square of the arithmetic site is introduced in §4.3.1.
8. **New item.** Codex's even-tensor-power positivity calculation is added as (e).
9. **Revision 3** (04:56 UTC). Item (e) is located as TWC7, with the exact abscissa 1 + 2kβ_max of the positive even-power series and the consequence stated there.
