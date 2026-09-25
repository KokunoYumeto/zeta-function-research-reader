# The split-zero programme around ζ(s, 1+t): a results digest (Claude's edition, draft 1)

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026; draft 1 at 05:05 UTC, corrected at 05:24 UTC after an independent referee pass; §2 items 4 and 6, §4 item 7 and §5 item 3 updated at 05:41 UTC from `11_`. This is a draft for the owner's review, not yet for publication.

This digest collects what an audit-and-extension lane established about the owner's programme between 22 and 25 September 2026. It covers the programme's own proofs, results of two Claude instances, and independent checks. Each item gives a statement, its status, and where the proof lives: the numbered notes `01_`–`11_` of this folder, and the programme's proof labels such as MCL5 or HSW6. The full index is `00_RESULTS_REGISTER.md`. Nothing here proves or disproves the Riemann hypothesis. The items are judged by what they establish.

## 1. The overall picture

1. **Where RH can enter.**
   - The Connes–Consani summation map, applied to the shifted lattice ℤ + a, gives the even shadow Z_a = ζ(s,a) + ζ(s,1−a) of the owner's flow. On the sheets a = 1/q, Z_a is q^s times the zeta function of the monoid {n ≡ ±1 mod q}.
   - This monoid factors uniquely exactly when q ∈ {1, 2, 3, 4, 6}. At q = 5, for example, 36 = 4·9 = 6·6.
   - Exactly for those q the formal logarithm is nonnegative and there are no zeros with Re s > 1. Otherwise there are zeros off the line. At q = 5 there are 24 zeros with Re s > 0.505 below height 150; of the 90 zeros below that height, none lies within 0.0068 of the line (Figure 1, `figures/fig_z15_zeros.png`).
   - How the programme's results behave on such a sheet:
     - The finite-block lifting algebra holds there word for word (MCL3–MCL7, ORE6.2, ORE6.5).
     - MCL9 and ORE4 hold there in substance.
     - The reflection laws change: they pair Z_a with a different function.
     - The closed-image, projector and residue-pairing inputs were not checked on other sheets.
   - My assessment: a step that separates the critical line has to use at least one of unique factorization, the positive prime measure, the prime clocks, or the self-dual functional equation. (`08_` §§1–2)
2. **What Deligne's weight argument needs, and what is available.**
   - Available:
     - positivity, which gives ζ(1+it) ≠ 0 and, with growth bounds, the classical zero-free region;
     - duality, the functional equation.

     In the programme's separations these are used to produce the strip 0 < Re ρ < 1.
   - Missing, in the constructions examined, is one of two things:
     - (a) a discreteness mechanism for weights on an auxiliary object, together with a square with a Künneth map;
     - (b) a pole bound for positive even tensor powers that is uniform in the power.
   - Positivity of even tensor powers on its own gives back the largest real part and cannot bound it. The positive series Σ_n (Σ_{ρ∈S} m_ρ n^ρ)^{2k} n^{−s} has abscissa exactly 1 + 2k·max Re ρ. (`08_` §3)
3. **Positivity sees only the critical zeros.** Four related results:
   - CFP: the positive transfer-compatible forms on the zeta quotient are sums over the critical zeros.
   - CPS: the specialization quotient carries only the zero form.
   - SPF9: before the quotient, a positive form descends if and only if its spectral measure sits on the critical zeros.
   - TWC10: the positive tensor receivers kill the off-line same-eigenvalue powers. For k ≥ 2 they keep the reflected pairs, which have modulus exactly n.

   Such forms vanish on the off-line data they could detect, so by themselves they cannot decide where the zeros lie. (`04_`, `08_`, `09_`)
4. **The Hilbert–Pólya obstruction, located.**
   - At each zero, the canonical representative b_ρ of the eigenvector satisfies (Re ρ − ½)‖b_ρ‖² = −Re⟨b_ρ, b_0⟩ in L²(du).
   - Since ‖b_ρ‖ > 0, this restates RH at each zero as Re⟨b_ρ, b_0⟩ = 0.
   - The L² form cannot supply a skew-adjoint structure on the quotient: the summation image is dense in L², so the quotient seminorm is zero (the easy direction of Wiener's theorem).
   - The Poisson-swept defect equals 2Σ m|Re ρ − ½|‖b_ρ‖². (`09_`)
5. **The F1 question.**
   - The square is Manin's question (1995) of an "absolute Descartes power" of Spec ℤ. In additive form, Kurokawa's tensor product plays the part of Deligne's squaring, and Connes proposes the square of the arithmetic site as the analogue of C̄ × C̄.
   - The weight mechanism that must accompany the square is specific to Deligne's argument. It is not a question from the 𝔽₁ literature.
   - The programme's own construction of a square has been computed, and it does not yet give the weight gain. (`08_` §4)

## 2. Results that stand without the programme's vocabulary

1. **Zero velocities of ζ(s, a).**
   - For c₁ = dρ/da there is an exact explicit formula for smoothed sums, on every sheet (copy, Theorems A and A_a). I checked it independently at a = 1 on one window, with relative difference 1.8·10⁻¹⁸.
   - Sharp sums deviate at order T, with Bohr coefficients −b(n)/(2π√n log n) (Theorem C). The coefficients are proved after smoothing. The sharp form assumes RH, all but finitely many zeros simple, and the existence of Bohr means (`03_` §4).
   - The spectrum of the velocity sums is multiplicative exactly on the sheets a ∈ {1, ½}, and there the primes are the frequencies of maximal amplitude (Theorem E, refereed as correct).
   - The direction of motion of the n-th zero is its Gram offset (Theorem D). This assumes the zeros up to γ_n are simple and on the line. (`02_`, `03_`, `06_`)
2. **Two primes suffice.** Generalized eigenfunctionals common to dilation by two distinct primes are exactly the Mellin jets. This is the distributional form of the fact that two incommensurable periods force polynomial behaviour. (MCL3.4; `07_`)
3. **Least-order lifting.**
   - At a zero of multiplicity m, the k-th source Mellin jet lifts through the summation transpose with least generalized-character order m + k + 1.
   - The obstruction class to lifting at fixed order is the germ of the functional-equation multiplier: (−1)^j j!/2 · t^{r−1−j} χ_ζ(b+t) mod t^{min(m,r)}. It was checked for m = 1 and m = 2, with maximal deviation 1.1·10⁻³⁹. (MCL5–MCL9, ORE5; `07_`)
4. **Even lattice sheets.** The equivalence in §1.1 is proved; the step (iv) ⇒ (ii) cites Saias–Weingartner. It holds for every congruence monoid {n : n mod q ∈ H}: freeness holds iff H = (ℤ/q)^×. The even monoid {n ≡ ±1 mod q} is free exactly when the one-sided monoid {n ≡ 1 mod q} is half-factorial. (`08_` Lemma 2; `11_` Proposition 11.1, Corollary 11.4)
5. **Source pairing and harmonic defect.** These are the identities of §1.4, together with two-sided bounds that compare the defect with Σ m|Re ρ − ½|/(1+γ²). (OPD4, HSW6A–6B; `09_`)
6. **The formal logarithm detects freeness.**
   - For every multiplicative monoid M of positive integers, M is free if and only if log Σ_{m∈M} m^{−s} has nonnegative coefficients.
   - The first negative coefficient sits at the smallest element with two factorizations, and its value is 1 − j + ε ≤ −1/6.
   - Absence of zeros does not detect freeness in general: {1} ∪ {2^e : e ≥ 2} is not free, and its zeta function has zeros only on Re s = 0. (`11_` Lemma 11.2, Example 11.5)

## 3. Negative results, with their exact scope

1. **Detection, clock changes and loops.**
   - "Off-critical, therefore undetected" is false: every zero is detected by an explicit test.
   - Clock changes that preserve order and composition are linear, and move the critical line together with the zeros.
   - Seeing the parityless support again identifies no state. (IH, PL; `05_`)
2. **No finite-rank integral model of the prime dilations.** For each nonreal ρ, p^ρ is algebraic for at most two primes, by the six exponentials theorem. (IH5.3)
3. **No character-level lifting at any zero.**
   - The nilpotent enlargement is forced by the multiplicity, whether or not the zero is on the line.
   - In the restriction row, the kernel and the target carry the same character, so no weight truncation can separate them. That separation is the one Deligne's argument uses. (MCL6, ORE6)
4. **The sharp velocity laws fail at order T.** This assumes RH, all but finitely many zeros simple, and the Bohr-mean hypothesis. The smoothed laws hold unconditionally. (Theorem C; `03_` §4)
5. **What descends to the zeta quotient.**
   - Poisson-sweeping the zeros onto the line descends if and only if there are no off-critical zeros (HSW6).
   - The L² norm never descends, even under RH (OPD3).
6. **Generalized primes.**
   - Regularity of the integer count does not force RH for generalized primes (Diamond–Montgomery–Vorhauer, Math. Ann. 334, 2006; Zhang, Math. Ann. 337, 2007).
   - Near-exact counts do not determine the prime system (copy, T2).

## 4. Bridges between programmes and fields

1. **Deligne, Weil II §2.1.9 = Hadamard–de la Vallée Poussin = the programme's timed primes.** The programme's measure maps invertibly onto Deligne's positive measure. (DB9, DR)
2. **The Nyman–Beurling functions are values of the summation map on one-sided step tests.**
   - For a_k > 1 with Σc_k/a_k = 0, Σc_k{1/(a_k x)} = −½Σh(x), where h = Σc_k 1_{[−1/a_k, 1/a_k]}. This h is not in the programme's Schwartz class.
   - The programme's moment condition is the cancellation of the pole at 1.
   - There are three settings:
     - Fréchet: the discrepancies generate the zero-jet ideal, unconditionally (the programme's NCI).
     - L²(0,∞): the two-sided image is dense, unconditionally (Wiener).
     - One-sided L²(0,1): density is equivalent to RH (Nyman, Beurling, Báez-Duarte; Burnol; Noor in H² of the disk).
   - The three differ in topology, support and test class. (`09_` §4(c))
3. **Deligne's squaring, Kurokawa's tensor product, and Manin's absolute square.** Deligne's squaring step, in additive form, corresponds to Kurokawa's tensor product. Both point to the absolute square Manin asked for. Weil's proof uses C̄ × C̄, and Connes proposes the square of the arithmetic site. These are analogies, not identities. (`08_` §4)
4. **Connes–Consani's twistor line meets an elliptic curve with complex multiplication.** Through the 𝔽_{1²}-points {0, ∞, ±1}, the line relates to y² = x³ − x. The Hecke character equals the signed winding degree. (copy R5; S10–S11)
5. **Prime clocks = the Bost–Connes / Laca–Raeburn crossed product. Timed primes = Beurling generalized numbers.** (`01_`)
6. **Zero velocities = Gram offsets. Connes' §VIII harmonic distribution, realized rationally.** (`03_`, `09_`)
7. **Theorem E at a = 1/q = the factoriality criterion for arithmetic congruence monoids.** The criterion is Baginski–Chapman, Theorem 3.4; the Hilbert monoid 441 = 9·49 = 21·21 is the example there. The even-sheet test is the same criterion after dividing the class group by ±1, and it coincides with Carlitz's class-number-two criterion for half-factoriality. (`11_`)

## 5. The 𝔽₁ context

1. **The support.** The owner's τ〈Z₁; no Z₂〉 is realized at the generic point of Connes–Consani's 𝔽_{1²}-line. "No Z₂" has two exact readings: no exchanged label, which holds at the generic point; and no sign, which holds exactly in characteristic 2. (`01_` for the realization; `00_`, goal 4, item 1 for the two readings)
2. **The question asked without meaning to.** The weight lane of the second attempt asks for Manin's square (1995), with a Künneth map, together with a weight mechanism specific to Deligne's argument. (`08_` §4)
3. **The sign and the Euler product.** The Eulerian even sheets a = 1/q are exactly those whose units mod q are the 𝔽_{1²}-signs ±1. Equivalently (proved), they are the sheets on which the one-sided monoid is half-factorial: quotienting by the sign turns half-factoriality into factoriality. Reading this as the passage from 𝔽₁ to 𝔽_{1²} is interpretation. (`08_` §1; `11_` §3; Figure 2, `figures/fig_monoid_sheets.png`)

## 6. Corrections recorded

- **FLIP_FABLE Addendum 4.** The claim that zeros of ζ(s, 1+t) lie on vertical lines only at Eulerian times was false. Zeros 4 and 5 of ζ cross the line at t ≈ 0.95095 and t ≈ 0.85870. (`ERRATUM_FLIP_FABLE_ADDENDUM_4.md`; Figure 3, `figures/fig_shifted_flow_crossings.png`)
- **`08_`, revision 2.** A referee pass and the Codex reading found:
  - a zero count of 13 that should have been 24;
  - three citation fixes;
  - several overstatements.

  All are corrected. A second referee pass corrected overstatements in `09_` and in draft 1 of this digest.
- **The N3 table** (T = 2515) has been corrected.

## Provenance

- **Checks.** Every numerical claim has a script with its output, in `checks/` or, for the copy's results, in `copy_round2/code/`.
- **Branch.** The public mirror is the GitHub branch `claude/claude-ab-grind-20260925` of KokunoYumeto/zeta-function-research-reader.
- **Instances.** Results marked "copy" come from a second Claude instance of the same model. Items marked with programme labels are the ChatGPT/Codex lanes' proofs, which claude-ab has read and checked where stated.
