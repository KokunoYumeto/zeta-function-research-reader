# The split-zero programme around ζ(s, 1+t): a results digest (Claude's edition, draft 2, revised)

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026.

- Draft 1 was written at 05:05 UTC and corrected at 05:24 UTC after an independent referee pass. §2 items 4 and 6, §4 item 7 and §5 item 3 were updated at 05:41 UTC from `11_`.
- Draft 2 (06:51 UTC) adds the results of `12_`–`16_`: §1 items 6–7; §2 items 7–12; §3 items 7–12; §4 items 8–13; §5 items 4–6; Figure 4.
- Draft 2 had its own referee pass (the fourth overall; 23 findings on `14_`–`16_` and this digest, two of them errors of statement). All were applied at 07:42 UTC. The same update adds the results of `17_`: §3 item 13, §4 item 14, §5 item 7 and Figure 5.
- `17_` had its own referee pass (the fifth; 16 findings, all applied by 08:25 UTC), and §3 item 13 was extended then. `18_` and `19_` added §4 item 15 and §3 item 14 (08:41–08:46 UTC), and `20_` updated §3 item 4 (08:53 UTC).
- A sixth referee pass, on `18_`–`20_` and this digest, found one major error, in the first version of §4 item 15, and several overstatements and gaps. All were applied at 09:38 UTC; §6 lists them.
- At 10:59 UTC `21_`–`23_` were added: the cross-programme bridges (part 1, refereed), the owner's anomaly picture made exact, and the detectability argument. The additions are §2 item 13, §3 items 15–17, §4 items 16–18 and §5 item 8. `22_` and `23_` await their referee pass.
- At 11:54 UTC `24_`–`26_` were added, for board task 8, which the owner gave priority from about 11:03 UTC. They audit GSL, GMS, AST, GDC, PTQ, SSI, ECR, ECI, GZR and OMS, and were refereed in the eighth pass. The additions are §2 items 14–17, §3 items 18–20, §4 item 19 and §5 item 9.
- This is a draft for the owner's review, not yet for publication.

This digest collects what an audit-and-extension lane established about the owner's programme between 22 and 25 September 2026. It covers the programme's own proofs, results of two Claude instances, and independent checks. Each item gives a statement and where the proof lives: the numbered notes `01_`–`26_` of this folder, and the programme's proof labels such as MCL5 or HSW6. The full index is `00_RESULTS_REGISTER.md`. Unless an item says otherwise, its statement is proved in the source cited in parentheses, and contributions of claude-ab are marked as such. Nothing here proves or disproves the Riemann hypothesis. The items are judged by what they establish.

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
6. **Weights, receivers and the growth of tensor powers.**
   - Connes' weighted-L² construction works on every vertical line Re s = σ. Each receiver sees exactly the zeros on its line, with the primes acting there with modulus p^σ. In Deligne's normalization |α| = p^{w/2} this reads "pure of weight 2σ", an analogy only, since the weights are real. The mirror pairs σ with 1 − σ, and the whole family is faithful on the zeta quotient. RH is the statement that only σ = ½ survives ("purity of weight 1" in the same analogy). (VWR; `14_`)
   - The natural map from Meyer's quotient to the inverse limit of Connes' Hilbert quotients (σ = ½) has kernel exactly the off-line classes. So it is injective iff RH holds. (WHR9.3; `12_`)
   - On tensor powers the faithful norm is bounded by t^k for t ≥ 1, exponent 1 per factor (ATG6.4). For a finite set of zeros stable under ρ ↦ 1 − ρ̄, the error against the target k/2 is k(max Re ρ − ½), linear in k. A bound of Deligne's uniform shape k/2 + c would force max Re ρ = ½; the proved estimates (ATG6.4, 7.3, 9.2) have exponent k. (ATG8; `14_`)
7. **The two poles.**
   - The pole at 1 is the average: the density of the integers, and through −ζ′/ζ the main term of ψ. The zeros give only the oscillation around it.
   - The pole at 0 depends on the local model of the test functions at the origin. It is the contribution of the single lattice point 0, while the pole at 1 is the contribution of the dual lattice's zero, which measures a density. Fourier duality exchanges the two (δ₀ ↔ 1). (`13_`)
   - In the programme's clock picture, the joint clock of periods 1, …, N has lcm(1, …, N) = e^{ψ(N)} states, so its growth is the pole's average N plus the zeros' oscillation (Figure 4). (PMS; `15_`)

## 2. Results that stand without the programme's vocabulary

1. **Zero velocities of ζ(s, a).**
   - For c₁ = dρ/da there is an exact explicit formula for smoothed sums, on every sheet (copy, Theorems A and A_a). I checked it independently at a = 1 on one window, with relative difference 1.8·10⁻¹⁸.
   - Under (H), all but finitely many zeros simple and on the line, sharp sums deviate from the drift at order T (Theorem C). After Gaussian smoothing, the deviation divided by T is, unconditionally and up to O(1/T), almost periodic with Bohr coefficients −b(n)e^{−Δ² log²n/2}/(2π√n log n). The sharp coefficients −b(n)/(2π√n log n) need (H) and the existence of Bohr means (`03_` §4).
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
7. **A divisor-potential form of RH.**
   - For r > 1 and t > 0 put 𝓔_r(t) = Σ_ρ m_ρ(r^σ − r^{1−σ})²e^{2t(σ²−γ²)}. It is ≥ 0, and it vanishes iff RH holds. (At r = 1 it vanishes identically.)
   - For a symmetric cutoff equal to 1 near [0, 1] and supported in (−½, 3/2), 𝓔_r(t) = (1/2π)∫ ½log|ζ(s)ζ(1−s̄)| Δφ₊ dA + (r−1)²(e^{2t}+1)/2.
   - The functional equation removes exactly the odd part of log|ζ|. (OZD5; `12_`)
8. **The swept trace.** For finitely many exponents, the translation trace on the full jet-constraint space over [−T, T] tends to Σ m e^{−|β−½||t|}e^{iγt}. Each off-line exponent is swept to the line by its Poisson kernel.
   - Same-side unit vectors are not asymptotically orthogonal. Connes' 1998 sketch says they are (verified by the referee of the third referee pass, on `11_`–`13_`, in the author TeX of arXiv:math/9811068v1, §VIII, proof of Lemma 3), and the conclusion survives with the full Gram inverse.
   - Checked numerically. (FGR; `12_`, `checks/fgr_trace_check.py`)
9. **Exact dilation norm.** On L²((0,∞), u^{2σ−1}(1+log²u)^δ du), ‖T_a‖ = a^σ Λ₊(log a)^{δ/2}, with Λ₊(t) = (t²+2+|t|√(t²+4))/2. (WHR8, VWR3; `12_`, `14_`)
10. **Nyman–Beurling in the Fréchet topology.** For fixed t > 0, the functions e^{ts²}(n − n^{1−s})/s span a dense subspace of the strip space ℬ. Multiplied by ξ, they span a dense subspace of the zero-jet ideal, which is the closure of ξℬ but strictly larger than ξℬ. Any set S of n ≥ 2 with limsup_{R→∞} #{n ∈ S : log n ≤ R}/R² = ∞ suffices, for example the squares. Proved in the programme (NCI2.8, NCI5.2, NCI8.2, RSS1.2); the sparse version in ℬ is claude-ab's transplant of the NCI8 Jensen step into RSS1. (NCI, RSS; `16_`)
11. **The completed prime clock and Chebyshev's ψ.**
    - The closure of p^ℤ in ∏_{q≠p}ℤ_q^× is a copy of Ẑ.
    - The joint state set of the clocks ℤ/1, …, ℤ/N has lcm(1..N) = e^{ψ(N)} elements.
    - Both are proved (PMS M3.3, M4.2, M6.2). Their ingredients were checked in finite ranges: the order lemma for p ≤ 50 and d ≤ 30, the state count for N ≤ 12, and the increments for N ≤ 20000. (PMS; `15_`)
12. **The two poles differ in kind.** For the lattice cℤ, the residue at 0 is −h(0) whatever c is, while the residue at 1 is (∫h)/c. The position of the pole at 0 is set by the local behaviour h ~ κv^α. (`13_`)
13. **The two-line product and the two ways to run the clock backwards.**
    - G(s) = F₀(s)F₀(s+1) satisfies G(−s̄) = conj G(s), and G(it) = |ξ(1+it)|²/16 > 0. So the pair is real and positive on the line of the pole at 0, where neither factor is real.
    - Running the clock u ↦ 1/u with conjugation has Mellin shadow s ↦ −s̄ in the Haar normalisation and s ↦ 1 − s̄ in the Lebesgue normalisation. The two differ by the factor u, and only the second gives Weil's positivity. (claude-ab; `22_` Props. 22.4–22.5)

14. **The separator, for ζ and for every Dirichlet L-function.**
    - An entire function E of polynomial growth on vertical strips can be 1 at every zero ρ and 0 at every ρ − 1, to full order. Then B/(I ∩ I₋) splits continuously into B/I ⊕ B/I₋.
    - The construction (∂̄ with a Gaussian Cauchy kernel) works whenever the two-line product has the same exponential rate above, on every strip, and below, in a zero-free corridor.
    - For ζ this product is s²(s²−1)ζ(1−s)ζ(1+s)/(64 cos(πs/2)), with rate e^{−π|t|/2}. The same holds for every primitive Dirichlet L-function.
    - (GSL, audited; claude-ab `24_` Lemma 24.1, Prop. 24.4)
15. **The exact summation image.**
    - Connes' summation map is a topological isomorphism from even Schwartz functions with f(0) = 0 = ∫f onto the entire functions, rapidly decreasing on strips, that vanish to full order at every nontrivial zero.
    - The inverse is explicit, and so is a Möbius formula for it. The source's Taylor coefficients at 0 are the values at the trivial zeros divided by 2ζ′(−2r).
    - On the programme's reading this is Meyer's range theorem, made explicit with a division estimate. (SSI, OMS; `25_` Lemma 25.1)
16. **Positive adjointness sees the line zeros one coordinate at a time.** A bounded positive form for which pullback and transfer are adjoint is diagonal on the line zeros and zero elsewhere. (PTQ4; `25_` Lemma 25.2)
17. **The global residue duality.** The contour pairing (2πi)^{−1}(∫_{Re 2} − ∫_{Re −1})F(s)G(1−s)/ζ(s)ds is continuous with an explicit constant and nondegenerate on the zeta quotient. It pairs the jets at ρ with those at 1 − ρ, with local determinant (m!/ζ^{(m)}(ρ))^m. (GZR; `26_` Lemma 26.1)

## 3. Negative results, with their exact scope

1. **Detection, clock changes and loops.**
   - "Off-critical, therefore undetected" is false: every zero is detected by an explicit test.
   - Clock changes that preserve order and composition are linear, and move the critical line together with the zeros.
   - Seeing the parityless support again identifies no state. (IH, PL; `05_`)
2. **No finite-rank integral model of the prime dilations.** For each nonreal ρ, p^ρ is algebraic for at most two primes, by the six exponentials theorem. (IH5.3)
3. **No character-level lifting at any zero.**
   - The nilpotent enlargement is forced by the multiplicity, whether or not the zero is on the line.
   - In the restriction row, the kernel and the target carry the same character, so no weight truncation can separate them. That separation is the one Deligne's argument uses. (MCL6, ORE6)
4. **The sharp velocity laws fail at order T.** Parts (i)–(ii) assume (H): all but finitely many zeros simple and on the line. The sharp Bohr coefficients also assume the Bohr-mean hypothesis. The smoothed laws hold unconditionally with the explicit error of Corollary B, O(T·d(Δ) + K(Δ)), where d(Δ) and K(Δ) are explicit and tend to 0 as Δ → ∞. For fixed Δ this error is of order T, the size of the oscillating term −(T/2π)𝒟_Δ(T) (part (iii)), and it tends to 0 when Δ ≥ (1+δ)√(2 log T)/log 2. The quantity summed is the zero velocity ρζ(ρ+1)/ζ′(ρ) of the Hurwitz shift (`17_` §1). (copy, Theorem C and Corollary B; `03_` §4; the proof of parts (i)–(iii) completed by claude-ab along the copy's route, relative to Theorem A, in `20_`)
5. **What descends to the zeta quotient.**
   - Poisson-sweeping the zeros onto the line descends if and only if there are no off-critical zeros (HSW6).
   - The L² norm never descends, even under RH (OPD3).
6. **Generalized primes.**
   - Regularity of the integer count does not force RH for generalized primes (Diamond–Montgomery–Vorhauer, Math. Ann. 334, 2006; Zhang, Math. Ann. 337, 2007).
   - Near-exact counts do not determine the prime system (copy, T2).
7. **The functional equation removes only what it can see.** Its whole odd contribution to the off-line detector is the pole and trivial-zero terms. The detector lives in the even part, where the functional equation says nothing further. (OZD5; `12_`)
8. **Connes' Hilbert receivers are automatically pure.** The prime spectra lie on |z| = √p unconditionally, so a spectral-radius argument there proves purity only of what remains after the off-line classes are lost (my assessment in `12_`). The RH content is exactly the injectivity of the comparison map. (WHR8–WHR12; `12_`)
9. **Tensor powers, as computed, give no uniform bound.** In degree 1 the square adds nothing beyond Q ⊗ Q. The error k(B − ½) is linear in k. For k ≥ 2 the reflected pairs (ρ, 1−ρ) give eigenvalues p·p^{ρ₃+⋯+ρ_k} of infinite multiplicity, so Q^{⊗k} has no ordinary trace. (GMC, ATG; `12_`, `14_`)
10. **Cover invariance cannot locate zeros.** For the transposed cover action on the dual of ℬ + ℂh_{P,t} (the slice α_P = 0), covariance recovers exactly the divisor that the chosen residue section inserts. With the ξ section that is the zeta divisor; with a polynomial section P, P(0) = 1, it is any prescribed finite set of nonzero points. A Hardy-receiver form exists for the ξ section (NCI6.3, NCI7.3). (RSS3.2; `16_`)
11. **An off-line defect cannot hide in the generic-point term.** The functional Σ_{Re ρ≠½} m_ρF(ρ) is never a nonzero multiple of the evaluation b ↦ b(1), which Connes–Consani's semilocal trace formula attributes to the generic point (arXiv:2602.15941, §8, as cited in VWR10; not read by me). (VWR10.9; `14_`)
12. **Isometry sees nothing off the unitary axis.** With the raw action, an invariant seminorm vanishes on every block (ATG6.5, stated for ν₀). A seminorm invariant under the half-density prime action vanishes on every off-line block (claude-ab's half-density form, confirmed by the referee). (`14_`)
13. **The mirror line at Re s = −½ does not disprove RH, and the explicit-formula pairing centred at the pole 0 is not real.** The mirror of the zeros through the pole at 0 is the whole zero set shifted by one: A(Z) = Z − 1 with A(s) = −s̄, unconditionally. It is exactly the nodal set of the first Hurwitz jet −sζ(s+1) in −1 < Re s < 0. Mirror = shift on every zero is equivalent to RH. Each property used has a counterpart for zeta functions of curves over finite fields, where RH is Weil's theorem. The explicit-formula pairing centred at 0 is not real: 2πe^{i/2} for an explicit Gaussian, against the real value 2π for Weil's pairing centred at ½. So, as it stands, the 0-centred pairing is not a positivity criterion. The simultaneous existence of ζ(s) and −sζ(s+1), the first two Taylor coefficients of ζ(s, 1+t) in t, does not decide RH either. "All zeros of ζ(s) on Re s = ½" and "all zeros of ζ(s+1) in the strip on Re s = −½" are one proposition. The Davenport–Heilbronn function, which has a functional equation but no Euler product, coexists with its translate and has a zero off the line. (claude-ab; `17_` §§5–6, 10, Figure 5)
14. **The product-trace machinery does not force weight 1.** The residue pairing lives on the product of the Connes–Consani base, whose dualizing complex is j_!k[1]. Its diagonal return by the right adjoint keeps the trace exactly. On Spec ℤ ∪ {m₊, m₋} the return is a correspondence, since no continuous single-valued lift of the diagonal map fixes the arithmetic diagonal. The reflected-pair classes have weight 2 whether or not RH holds, and the global complex kills them. In the programme's words, the return "does not prove either individual weight to be one". (FTD, PRS, DER, FSC, FEM; `19_`)
15. **Anomaly cancellation of the symmetric kind cannot see or forbid off-line zeros.**
    - Off-line zeros come in pairs at equal height, so the parity (ℤ₂) anomaly counts only on-line zeros.
    - With both lines present the count doubles (2N₀ + 4N_pairs), and the ℤ₄ (four-direction) anomaly also vanishes identically. Only the integer count, which is Turing's method, sees off-line zeros.
    - The Davenport–Heilbronn function carries the whole structure, including an off-line zero. It cancels the root-number phase by adding a character sector to its conjugate; ζ-type products cancel it by multiplication and keep the Euler product. (claude-ab; `22_` 22.9–22.11)
16. **Cross-programme transfers, with scope.** Joint averages do not survive restriction of the Navier–Stokes torus cover to unchanged finite torsion (13 against 4 at p = 13, a = 4); the complete preimage repairs them. The Navier–Stokes profile gives Yang–Mills a zero-quotient sequence only as the coupling tends to 0. (`21_`)
17. **RH cannot be independent of ZFC and false.** RH is equivalent to the non-halting of an explicit 744-state machine, so a false RH is refutable. Independence would imply truth, but proving non-refutability is as hard as RH. (the owner's M28; `23_`)

18. **The two-line splitting is not an RH criterion, and B does not split along the two lines.**
    - The splitting holds for every primitive Dirichlet L-function. Its proof never uses where the zeros lie inside the strip.
    - The separator fixes the original class and its defect.
    - Only the quotients split: the separator is not an idempotent, and the normal row has no section. (GSL, GMS, ECR6; `24_`)
19. **The separator proof does not reach the Davenport–Heilbronn function.** That function has zeros with Re s > 1 (Saias–Weingartner), so no vertical line separates its two divisors. Whether the splitting itself fails there is open. (`24_` Prop. 24.6)
20. **The positive-side constructions restate RH.**
    - The off-line source, the off-line coordinates, the descent of the Weil form, and two numerical detectors are eight constructions reducing to three conditions. Each vanishes exactly when there are no off-line zeros, by construction.
    - The detectors are not holomorphic in ρ, so the explicit formula does not directly compute them.
    - The global duality is nondegenerate but not positive. (AST, GDC, PTQ, ECR, GZR; `25_` §5, `26_`)

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
7. **Theorem E at a = 1/q = the factoriality criterion for arithmetic congruence monoids.** The criterion is Baginski–Chapman, Theorem 3.4; the Hilbert monoid 441 = 9·49 = 21·21 is the example there. The even-sheet test is the same criterion after dividing the class group by ±1. It coincides with the half-factoriality criterion, the Krull-monoid analogue of Carlitz's class-number-two theorem. (`11_`)
8. **The off-line detector and Littlewood-lemma criteria.** OZD's identity is a relative of the RH-equivalent integral identities for log|ζ|: Balazard–Saias–Yor, Adv. Math. 143 (1999), and Sekatskii–Beltraminelli–Merlini, Ukr. Math. J. 64 (2012). (`12_`)
9. **Connes 1999 and Meyer 2005 in one comparison map**, with Connes' exponent δ_CC = 2δ. (WHR; `12_`)
10. **Spectral synthesis.** Closed multiplier submodules of the zeta quotient are the jet-order submodules: a local description in Krasichkov-Ternovskii's sense. (GSP; `12_`)
11. **Bochner–Schwartz.** The positive transfer forms before the quotient are the Bochner–Schwartz theorem transported by the Mellin transform. (SPF; `12_`)
12. **Weight decomposition (an analogy of structure).** The vertical receivers are "pure of weight 2σ" in the translation |α| = p^{w/2} with real weights, the mirror is duality w ↔ 2 − w with a weight-2 target, and RH is purity of weight 1. (VWR; `14_`)
13. **The owner's clocks and Chebyshev's ψ.** The clocks follow Connes–Consani, *Knots, primes and class field theory*. Their joint state count is e^{ψ(N)}, so through the explicit formula they carry the zeta zeros. (PMS; `15_`)
14. **The Hurwitz shift, the mirror through 0, and two Hopf circles.** The first jet of the programme's shift flow ζ(s, 1+t) vanishes exactly on A(Z) = Z − 1 in −1 < Re s < 0, where A(s) = −s̄ is the reflection through the pole at 0. On the critical line the translation T₋₁ coincides with A. The zero velocities ρζ(ρ+1)/ζ′(ρ) are the initial tangents of the tracks in Figure 3. With the one-line shift pairing, the critical line and the line at −½ are the two halves of one (1,−1) circle on the Clifford torus. The owner's Hopf fibre (critical line with the pairing (s, 1 − s̄)) is a (1,1) circle, and the two circles meet only at t = ±∞. (claude-ab; `17_`)
15. **The two lines inside the programme.** The separator of GSL/GMS is built from G(s) = F₀(s)F₀(s+1), whose zeros are, unconditionally, the critical zeros Z and their copy Z − 1 one line to the left. The function E_sep equals 1 on Z and 0 on Z − 1 and switches in the zero-free corridor around Re s = 0; the separator proper, c(s) = 1 − E_sep(s − 1), equals 1 on Z and 0 on Z + 1. At the level of modules the unconditional pair is the zeta quotient Q and its normal twist Q₊ (jets at Z + 1). They are derived-separated by the general vanishing of Ext for coprime annihilators, which has no zeta-specific content. The global model's pair ℛ[1] ⊕ ℛ(−1)[−1] holds only off-line data and vanishes iff RH, and the descent condition of ADM7 holds iff ℛ = 0; both restate RH through the definition of ℛ. (ADM6–ADM8; `18_`)
16. **Where the programmes reuse each other's results (part 1).**
    - An integer torus matrix from the Navier–Stokes blowup construction enters Erdős–Straus divisor counting.
    - The Navier–Stokes velocity enters Yang–Mills as a reducible SU(2) connection.
    - A Gram-sandwich lemma of the zeta programme enters Yang–Mills heat estimates.
    - One Jacobian polynomial appears in Erdős–Straus, Yang–Mills and zeta work.
    - None of these makes a deep theorem of one programme a hypothesis of another, except the Navier–Stokes blowup rate used in Yang–Mills. (`21_`)
17. **The owner's anomaly picture, made exact.**
    - The anti-number is the clock run backwards with conjugation.
    - Chirality is the mirror through the pole at 0.
    - The owner's doublet is the zero quadruple.
    - Parity (Z₂) is the double cover formed by the two lines, whose deck transformation is the central sign of SU(2).
    - The time direction (Z₁) is the root-number phase.
    - Inflow is the bulk between the two lines.
    - In these terms RH says that every zero is its own anti-number. (claude-ab, from the owner's M12–M27; `22_`)
18. **Prime knots and anti-numbers.** In Connes–Consani's knots paper, reversing the orbit of p conjugates the character. The functional equation puts the conjugate character on the other side of τ at the phase W(χ), and W(χ)W(χ̄) = 1. (`22_` Prop. 22.8)

19. **The programme's defect is a zero minus its reflected partner.** d_r(ρ) = conj(r^ρ − r^{1−ρ̄}). It vanishes exactly when ρ is its own partner under s ↦ 1 − s̄, the involution used for the pivot at ½. (claude-ab; `24_` §3.3)

## 5. The 𝔽₁ context

1. **The support.** The owner's τ〈Z₁; no Z₂〉 is realized at the generic point of Connes–Consani's 𝔽_{1²}-line. "No Z₂" has two exact readings: no exchanged label, which holds at the generic point; and no sign, which holds exactly in characteristic 2. (`01_` for the realization; `00_`, goal 4, item 1 for the two readings)
2. **The question asked without meaning to.** The weight lane of the second attempt asks for Manin's square (1995), with a Künneth map, together with a weight mechanism specific to Deligne's argument. (`08_` §4)
3. **The sign and the Euler product.** The Eulerian even sheets a = 1/q are exactly those whose units mod q are the 𝔽_{1²}-signs ±1. Equivalently (proved), they are the sheets on which the one-sided monoid is half-factorial: quotienting by the sign turns half-factoriality into factoriality. Reading this as the passage from 𝔽₁ to 𝔽_{1²} is interpretation. (`08_` §1; `11_` §3; Figure 2, `figures/fig_monoid_sheets.png`)

4. **The pole at 1 and Bost–Connes (interpretation).** The pole at 1 is the average, and in the Bost–Connes system the partition function is ζ(β), with its phase transition at the same pole (Selecta Math. 1, 1995). No map between the two is constructed. (Register, goal 4, item 10)
5. **The pole at 0 and τ (proposal).** The classical pole at 0 merges three roles at one place: the lattice origin, the additive origin with its local germ, and the fixed point of the sign. The ledger separates them. The owner places τ at the pivot of the swing between 0 and 1. In the zeta picture that is the pivot of the pole exchange s ↦ 1 − s: ½ on the spectral side and u = 1 on the clock side. There RH reads ρ^# = ρ for every zero. (`13_` §4; register, goal 4, item 11)
6. **"Has not moved" is not "absent".** In the programme's generic monoid the winding-zero fibre {τ, J, ε, J³} is present, and absence is the absorbing 0. (PMS M1; `15_`)
7. **The two centres of reflection differ by one shift.** With A(s) = −s̄ (centre 0) and B(s) = 1 − s̄ (centre ½, the owner's proposed τ), B∘A is the shift s ↦ s + 1. (Reading: this shift is the Tate twist, the character of the pole at 1.) Under the Hurwitz generator sζ(s+1), the residue of ζ at 1 becomes the value 1 at s = 0. Of the two centres, only the ½-centred one makes the explicit-formula pairing real, as in Weil's criterion. (claude-ab; `17_`)
8. **Four directions from the Bombelli generator.** In the absolute twistor line, J² = ε gives the four rays 1, J, ε, εJ, and the half-turn is the sign. The twistor real structure lifts to the quaternionic structure of the SU(2) doublet (σ² = −1), and two copies make it real. (claude-ab; `22_` Prop. 22.1)

9. **The jet at 0 comes from the trivial zeros.** For a source in the exact image, f^{(2r)}(0)/(2r)! = F(−2r)/(2ζ′(−2r)). The Mellin poles of the local model at −2r (register, goal 4, item 11) are seen here from the source side. (SSI5.6; `25_` §1.2)

## 6. Corrections recorded

- **FLIP_FABLE Addendum 4.** The claim that zeros of ζ(s, 1+t) lie on vertical lines only at Eulerian times was false. Zeros 4 and 5 of ζ cross the line at t ≈ 0.95095 and t ≈ 0.85870. (`ERRATUM_FLIP_FABLE_ADDENDUM_4.md`; Figure 3, `figures/fig_shifted_flow_crossings.png`)
- **`08_`, revision 2.** A referee pass and the Codex reading found:
  - a zero count of 13 that should have been 24;
  - three citation fixes;
  - several overstatements.

  All are corrected. A second referee pass corrected overstatements in `09_` and in draft 1 of this digest.
- **The N3 table** (T = 2515) has been corrected.
- **`11_`–`13_`.** A third referee pass reported 25 wording, label and hypothesis findings and no mathematical error in the main lemmas. All were applied, and each note lists them.
- **`14_`–`16_` and draft 2 of this digest.** A fourth referee pass found two errors of statement, both corrected: "never a multiple" should read "never a *nonzero* multiple" (`14_`); the density hypothesis of the Fréchet Nyman–Beurling theorem is limsup #/R² = ∞ (register S33). It also found 21 overstatements, missing hypotheses, labels and ranges; all were applied.
- **`17_`.** A fifth referee pass made 16 findings, mostly wording. The main ones: the Hurwitz flow was written as if it translated Z (only its first jet vanishes on Z − 1); a false bound on rung lengths; missing hypotheses on the neighbouring lines; an overclaim in a corollary of the owner's `6.tex`; a misattribution of the circle Γ; and the missing boundedness hypothesis of the blind lemma. All were applied (`17_` §11).
- **`18_`–`20_` and this digest.** A sixth referee pass found one major error. The first versions of `18_` and of §4 item 15 described the global model's pair ℛ[1] ⊕ ℛ(−1)[−1] as the original and shifted copies of the zero set, but ℛ holds only off-line data; the unconditional pair is Q and Q₊. It also found overstatements (the scope of FSC2, "cannot force", "coincide", "independently re-proved") and three gaps in `20_`: the conjugate zeros, the integration by parts under a mean-square hypothesis, and the range of Lemma 20.2(b). All were applied (`18_` §8, `19_` header, `20_` §9).
- **Timestamps.** Several log times written ahead of the clock were corrected to `date -u` readings (`PLAN.md`).

## Provenance

- **Checks.** Every numerical claim has a script with its output, in `checks/`, in `figures/`, or, for the copy's results, in `copy_round2/code/`.
- **Figures.** 1 = `fig_z15_zeros`, 2 = `fig_monoid_sheets`, 3 = `fig_shifted_flow_crossings`, 4 = `fig_clock_stack_psi`, 5 = `fig_mirror_line_double_helix`.
- **Branch.** The public mirror is the GitHub branch `claude/claude-ab-grind-20260925` of KokunoYumeto/zeta-function-research-reader.
- **Instances.** Results marked "copy" come from a second Claude instance of the same model. Items marked with programme labels are the ChatGPT/Codex lanes' proofs, which claude-ab has read and checked where stated.
