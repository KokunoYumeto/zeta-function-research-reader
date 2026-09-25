# The split-zero programme around ζ(s, 1+t): a results digest (Claude's edition, draft 1)

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 05:05 UTC. This is a draft for the owner's review, not yet for publication.

This digest collects what an audit-and-extension lane established about the owner's programme between 22 and 25 September 2026. It covers the programme's own proofs, results of two Claude instances, and independent checks. Each item gives a statement, its status, and where the proof lives: the numbered notes `01_`–`09_` of this folder, and the programme's proof labels such as MCL5 or HSW6. The full index is `00_RESULTS_REGISTER.md`. Nothing here proves or disproves the Riemann hypothesis. The items are judged by what they establish.

## 1. The overall picture

1. **Where RH can enter.**
   - The Connes–Consani summation map, applied to the shifted lattices ℤ + a, defines one sheet of the owner's flow for each a. On the sheets a = 1/q the "integers" are the monoid {n ≡ ±1 mod q}.
   - This monoid factors uniquely exactly when q ∈ {1, 2, 3, 4, 6}. At q = 5, for example, 36 = 4·9 = 6·6.
   - On those same sheets the formal logarithm is nonnegative, and there are no zeros with Re s > 1. Otherwise zeros leave the line. At q = 5 there are 24 zeros with Re s > 0.505 below height 150.
   - The programme's lifting algebra holds word for word on such a sheet. What changes there is exactly the arithmetic: unique factorization, the positive prime measure, the prime clocks, and the self-dual functional equation.
   - An RH-relevant step must use one of these. (`08_` §§1–2)
2. **What Deligne's weight argument needs, and what is available.**
   - Available: positivity, which gives ζ(1+it) ≠ 0, and duality, the functional equation. Together these give the strip 0 < Re ρ < 1 and nothing sharper.
   - Missing, in the constructions examined: a discreteness mechanism for weights on an auxiliary object, and a square with a Künneth map. Equivalently, a pole bound for positive even tensor powers that is uniform in the power.
   - Positivity of even tensor powers on its own gives back the largest real part and cannot bound it. The positive series Σ_n (Σ_{ρ∈S} m_ρ n^ρ)^{2k} n^{−s} has abscissa exactly 1 + 2k·max Re ρ. (`08_` §3)
3. **Positivity sees only the critical zeros.** Three independent constructions show that every positive, transfer-compatible form on the zeta quotient is supported on the critical zeros:
   - on the specialization quotient (CPS);
   - on every tensor power (TWC10);
   - before the quotient, through spectral measures (SPF9).

   An argument through such forms has assumed the location of the zeros; it has not derived it. (`04_`, `08_`, `09_`)
4. **The Hilbert–Pólya obstruction, located.**
   - At each zero, the canonical representative b_ρ of the eigenvector satisfies (Re ρ − ½)‖b_ρ‖² = −Re⟨b_ρ, b_0⟩ in L²(du).
   - The pairing would vanish if the L² inner product passed to the quotient. It does not pass: the summation image is dense in L² (Wiener's theorem).
   - The whole off-critical content is the sum 2Σ m|Re ρ − ½|‖b_ρ‖², which is exactly the Poisson-swept defect. (`09_`)
5. **The F1 question.**
   - The square is Manin's "absolute Descartes power" of Spec ℤ (1995). Its additive shadow is Kurokawa's tensor product, and Connes' square of the arithmetic site is the analogue of C̄ × C̄.
   - The programme's own construction of a square has been computed, and it does not yet give the weight gain. (`08_` §4)

## 2. Results that stand without the programme's vocabulary

1. **Zero velocities of ζ(s, a).**
   - For c₁ = dρ/da there is an exact explicit formula for smoothed sums, on every sheet (copy, Theorems A and A_a). It was independently checked to 1.8·10⁻¹⁸.
   - Sharp sums deviate at order T. The deviation is almost periodic, with Bohr coefficients −b(n)/(2π√n log n) (Theorem C; sharp form conditional on RH and simple zeros).
   - The spectrum of the velocity sums is multiplicative exactly on the sheets a ∈ {1, ½}, and there the primes are the frequencies of maximal amplitude (Theorem E, refereed as correct).
   - The direction of motion of the n-th zero is its Gram offset (Theorem D). (`02_`, `03_`, `06_`)
2. **Two primes suffice.** Generalized eigenfunctionals common to dilation by two distinct primes are exactly the Mellin jets. This is the distributional form of the fact that two incommensurable periods force polynomial behaviour. (MCL3.4; `07_`)
3. **Least-order lifting.**
   - At a zero of multiplicity m, the k-th source Mellin jet lifts through the summation transpose with least generalized-character order m + k + 1.
   - The obstruction class to lifting at fixed order is the germ of the functional-equation multiplier: (−1)^j j!/2 · t^{r−1−j} χ_ζ(b+t) mod t^{min(m,r)}. It was checked to 10⁻³⁹ for m = 1 and m = 2. (MCL5–MCL9, ORE5; `07_`)
4. **Even lattice sheets.** The equivalence in §1.1 is proved; the step (iv) ⇒ (ii) cites Saias–Weingartner. (`08_` Lemma 2)
5. **Source pairing and harmonic defect.** These are the identities of §1.4, together with two-sided bounds that compare the defect with Σ m|Re ρ − ½|/(1+γ²). (OPD4, HSW6A–6B; `09_`)

## 3. Negative results, with their exact scope

1. **Detection, clock changes and loops.**
   - "Off-critical, therefore undetected" is false: every zero is detected by an explicit test.
   - Clock changes that preserve order and composition are linear, and move the critical line together with the zeros.
   - Seeing the parityless support again identifies no state. (IH, PL; `05_`)
2. **No finite-rank integral model of the prime dilations.** For each nonreal ρ, p^ρ is algebraic for at most two primes, by the six exponentials theorem. (IH5.3)
3. **No character-level lifting at any zero.**
   - The nilpotent enlargement is forced by the multiplicity, whether or not the zero is on the line.
   - In the restriction row, the kernel and the target carry the same character, so no weight truncation can separate them. That separation is the one Deligne's argument uses. (MCL6, ORE6)
4. **The sharp velocity laws fail at order T.** Only the smoothed laws hold. (Theorem C)
5. **Two sweepings that do not descend without RH.**
   - Poisson-sweeping the zeros onto the line descends to the zeta quotient if and only if there are no off-critical zeros.
   - The L² norm does not descend at all. (HSW6, OPD3)
6. **Generalized primes.**
   - Regularity of the integer count does not force RH for generalized primes (Diamond–Montgomery–Vorhauer, Math. Ann. 334, 2006; Zhang, Math. Ann. 337, 2007).
   - Near-exact counts do not determine the prime system (copy, T2).

## 4. Bridges between programmes and fields

1. **Deligne, Weil II §2.1.9 = Hadamard–de la Vallée Poussin = the programme's timed primes.** The programme's measure maps invertibly onto Deligne's positive measure. (DB9, DR)
2. **Nyman–Beurling = the summation map with one-sided support.**
   - For a_k > 1 with Σc_k/a_k = 0, Σc_k{1/(a_k x)} = −½Σh(x), where h = Σc_k 1_{[−1/a_k, 1/a_k]}.
   - The programme's moment condition is the cancellation of the pole at 1.
   - There are three settings. In the Fréchet setting, with the programme's NCI, the closure is the zero-jet ideal, unconditionally. In L²(0,∞), with Wiener, the image is dense, unconditionally. In H²(Re s > ½), density is equivalent to RH (Beurling, Báez-Duarte, Burnol, Noor).
   - The three differ only in topology and support. (`09_` §4(c))
3. **Deligne's squaring = Kurokawa's tensor product = Manin's absolute square.** Weil's proof uses C̄ × C̄, and Connes proposes the square of the arithmetic site. (`08_` §4)
4. **Connes–Consani's twistor line meets an elliptic curve with complex multiplication.** Through the 𝔽_{1²}-points {0, ∞, ±1}, the line relates to y² = x³ − x. The Hecke character equals the signed winding degree. (copy R5; S10–S11)
5. **Prime clocks = the Bost–Connes / Laca–Raeburn crossed product. Timed primes = Beurling generalized numbers.** (`01_`)
6. **Zero velocities = Gram offsets. Connes' §VIII harmonic distribution, realized rationally.** (`03_`, `09_`)

## 5. The 𝔽₁ context

1. **The support.** The owner's τ〈Z₁; no Z₂〉 is realized at the generic point of Connes–Consani's 𝔽_{1²}-line. "No Z₂" has two exact readings: no exchanged label, which holds at the generic point; and no sign, which holds exactly in characteristic 2. (`01_`)
2. **The question asked without meaning to.** The weight lane of the second attempt asks for Manin's square, with a Künneth map and a weight mechanism: the object 𝔽₁-geometry has sought since 1995. (`08_` §4)
3. **An observation.** The Eulerian even sheets a = 1/q are exactly those whose units mod q are the 𝔽_{1²}-signs ±1. (`08_` §1)

## 6. Corrections recorded

- **FLIP_FABLE Addendum 4.** The claim that zeros of ζ(s, 1+t) lie on vertical lines only at Eulerian times was false. Zeros 4 and 5 of ζ cross the line at t ≈ 0.95095 and t ≈ 0.85870. (`ERRATUM_FLIP_FABLE_ADDENDUM_4.md`)
- **`08_`, revision 2.** A referee pass found a zero count of 13 that should have been 24, a misplaced citation, and several overstatements. All are corrected.
- **The N3 table** (T = 2515) has been corrected.

## Provenance

- **Checks.** Every numerical claim has a script in `checks/` with its output.
- **Branch.** The public mirror is the GitHub branch `claude/claude-ab-grind-20260925` of KokunoYumeto/zeta-function-research-reader.
- **Instances.** Results marked "copy" come from a second Claude instance of the same model. Items marked with programme labels are the ChatGPT/Codex lanes' proofs, which claude-ab has read and checked where stated.
