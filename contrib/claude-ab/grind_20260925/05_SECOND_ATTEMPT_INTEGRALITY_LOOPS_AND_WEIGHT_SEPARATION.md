# The second attempt, part 3: integrality, loops and weight separation

A content map of three notes in the character-lifting lane of the three-lane edition (zeta-function-research-reader, commit 064f33b):

- `original-character-lifting/integrality_purity_20260924/INTEGRAL_HISTORY_AND_PURITY.md` (IH1–IH8);
- `…/PRIME_CLOCK_LOOPS_AND_Z1.md` (PL1–PL8);
- `…/tau_lifting_weights_20260924/TAU_LIFTING_AND_WEIGHT_SEPARATION.md` (TL0–TL8, with its propagation notes).

All three were read in full.

**Not yet read:** the character-lifting core (MCL, ORE, RPC, SCT and their checks); the adelic-complex notes (AC, GAP, GEX, CTF); the distribution-realization notes (DR).

Claude (Opus 5.5 configuration), 25 September 2026.

These three notes test the owner's proposed routes from the complete arithmetic reconstruction to RH, one mechanism at a time:

- completeness and integrality;
- loops, returns and clock changes;
- Deligne-type weight separation.

## 1. Completeness and integrality (IH)

**The owner's proposed step (WU037).** Everything is quotiented by the single global unit and the whole spectrum has been detected. An off-critical zero would then be an undetected contribution, which is a contradiction.

**What the note establishes.**

1. **The identification is carried forward.**
   - The reconstructed ring is End(W) ≅ ℤ, where W is the winding group.
   - The reconstructed measures are R, D = exp_*R and 𝒲 = tR.
   - Their transforms are ζ and −ζ′/ζ on Re s > 1.
   - The mirror transports [n] to [n], so the identified function is unchanged (IH1).
2. **An off-critical zero would be detected, not undetected** (IH2.6).
   - Take any actual zero ρ, on or off the line, and any nonnegative nonzero φ ∈ C_c^∞(ℝ). The test function k_ρ(e^v) = φ(v)e^{−(ρ−1/2)v} has F_{k_ρ}(ρ) = ∫φ > 0.
   - So k_ρ gives a nonzero class of the actual quotient.
   - The step "off-critical, therefore undetected" is therefore false.
3. **The signature of an off-critical zero** (IH4).
   - On t > 0, the absorption measure (the von Mangoldt measure in logarithmic time) satisfies 𝒲 = e^t dt − Σ_ω m_ω e^{ωt} dt − Σ_{r≥1} e^{−2rt} dt, as distributions. This is the differentiated explicit formula for ψ.
   - An off-critical quartet contributes −2m(e^{βt} + e^{(1−β)t}) cos(γt): an oscillation with two unequal growth rates.
   - A critical pair contributes −2m e^{t/2} cos(γt).
   - Completeness places such an orbit inside the tested spectrum. It supplies no sign or growth bound that excludes it.
4. **Six exponentials** (IH5.3). For every nonreal ρ, at most two primes p have p^ρ algebraic.
   - This follows from the six exponentials theorem (Lang, Ramachandra) applied to (1, ρ) and (log p, log q, log r).
   - Consequence: the dilation eigenvalues p^ρ cannot all be eigenvalues of finite-rank integral endomorphisms, since those are algebraic. This holds for zeros on the critical line too.
   - So Deligne's algebraic integrality of Frobenius eigenvalues cannot be transferred to these operators by a finite-rank integral model.
5. **A faithful receiver built from two primes** (IH6).
   - The grid {a log 2 + b log 3 : a, b ∈ ℤ} is dense in ℝ, because log 2/log 3 is irrational.
   - Hence the sequence 𝒯(q)_{a,b} = Σ_ω m_ω F_q(ω) e^{−ω(a log 2 + b log 3)} determines every zero value F_q(ω).
   - Recovery is by the residues of the Laplace transform of the continuous extension.
   - Shifting a or b by one realizes the action of 2 or 3, and the reflection law has weight one.
6. **No bounded intertwiner to a shift chain** (IH7). A bounded intertwiner from the diagonal dilation on ℓ²(zeros) to a shift with S*S = nI must be zero. The shift has no eigenvectors, so the earlier positive Hodge-chain norm cannot be the norm of the zeta quotient.

**Outcome as the note states it.** No contradiction is produced. What off-criticality would change is the detected weight and the sign of the reflected value form; neither is excluded.

## 2. Loops, returns and clock changes (PL)

**The owner's proposed mechanism.** A deformation invisible to the complete counting system should be a change of clock, or a loop whose return exposes the parityless support.

**What the note establishes.**

1. **Clock changes are linear** (PL2).
   - A bijection of logarithmic time that preserves order and composition of durations is h(t) = ct.
   - Rescaling moves the pole to 1/c, the zeros to ρ/c and the critical line to real part 1/(2c), all together.
   - Hence 2 Re(ρ/c) − 1/c = (2 Re ρ − 1)/c: a change of clock can neither hide nor manufacture off-criticality.
2. **Two prime clocks never return together** (PL3).
   - The joint real clock t ↦ ([e^t]₂, [e^t]₃) on E₂ × E₃ never returns at a nonzero time, since log 2/log 3 is irrational.
   - There is nevertheless a common angular period: Λ₂ ∩ Λ₃ = 2πiℤ, where Λ_p = 2πiℤ + (log p)ℤ.
3. **Seeing the support again does not mean the state has returned** (PL4).
   - Every winding state T^mJ^k lies over η.
   - Identifying windings after N steps loses exactly the endomorphisms of degree divisible by N.
   - On the signed data the identification is compatible with the mirror only for even N.
4. **Folding the absorption record onto a circle is detectable** (PL5).
   - Every open arc receives infinite mass.
   - With damping e^{−σt}, the circle's Fourier coefficients are ζ(σ + 2πij/L) and −ζ′/ζ(σ + 2πij/L).
5. **What a zero contributes to a loop** (PL6).
   - Its return multiplier is e^{ρL}.
   - On Connes–Consani's E_p the multipliers are p^ρ along the real period and e^{2πiρ} along the angular period.
   - The test that distinguishes the critical line is \|p^ρ\|² − p = p^{2β} − p.
   - The angular multiplier cannot distinguish β = ½ from other values.
   - Conjugation duality: c_p*K̄_ρ ⊗ K_{1−ρ̄} ≅ K_1 (connection coefficient ρ̄ + (1 − ρ̄) = 1). This holds for off-critical pairs as well.

**Outcome as the note states it.** Every invisible clock change the note specifies is excluded. The note does not force a zeta zero to be such a change. Reappearance of the support gives no contradiction.

## 3. Weight separation, Deligne's mechanism (TL)

**What the note establishes.**

1. **Deligne's lifting theorem, reconstructed exactly** (TL1, Weil II §3.6.1–3.6.3).
   - The target C^i of specialization has weights ≤ i.
   - The obstruction group O^i = H^{i+1}_{X_s}(X) ≅ H^{2N−i−1}(X_s)^∨(−N) has weights ≥ i + 1, obtained from duality and the Tate twist.
   - So the weight-≤ i part of E^i maps onto C^i and has zero obstruction, which makes specialization surjective.
   - The separation is supplied by geometry (purity of the special and generic fibres), not by the existence of a spectrum.
2. **A receiving analogue** (TL2–TL4).
   - On B_ρ = ℂ[x, y]/(x, y)^{m_ρ} with quotient y ↦ 0, the kernel blocks have weights 2 Re ρ − 2j (j ≥ 1), strictly below the lifted block's 2 Re ρ.
   - Every section's obstruction cocycle is a coboundary, with an explicit inverse of U_p − I, and the equivariant lift is unique.
   - Across different zeros, Re ρ − Re σ − j < 0 because both lie in the open strip.
   - No use of Re ρ = ½ is made.
3. **Endpoint separation** (TL7, TL7.10).
   - The adelic endpoint module has weights exactly 0 and 2.
   - Zero blocks have weights strictly between them, since 1 < \|p^ρ\| < p.
   - Hence every Ext group between a zero block and the endpoints vanishes: the annihilators (z − p^ρ)^m and (z − 1)(z − p) are coprime.
4. **Honest scope** (TL8). None of these receivers has been identified with the actual geometric specialization complex of the original source.

**My reading, labelled as an assessment.**
- Every separation used in the receivers is the unconditional strip information 0 < Re ρ < 1 (weights strictly between 0 and 2), or a Tate shift built into the receiver.
- A Deligne-type argument for RH would need a geometric input that forces the obstruction group's weights to be ≥ i + 1 while the lifted classes have weights ≤ i, with the dividing line at weight 1, that is, at Re ρ = ½.
- In Deligne's proof that input is purity of the special fibre. No analogue has been constructed here.
- IH5.3 shows that such an analogue cannot be a finite-rank integral lattice. This agrees with the standard expectation that the relevant H¹ for ζ is infinite-dimensional (Deninger's programme; Connes' adèle-class-space realization). The literature comparison is not done.

## 4. Items for the four goals

- **Negative results (goal 1), stated plainly:**
  1. The completeness/integrality step "off-critical, therefore undetected" is false: an off-critical zero would be a detected class, with the explicit signature in §1.3.
  2. Invisible clock changes are linear and preserve off-criticality relative to the critical line. Reappearance of the parityless support identifies no state.
  3. The p^ρ cannot all be algebraic, so no finite-rank integral model of the dilations exists.
  4. All separations proved in the receivers use only 0 < Re ρ < 1. The weight-1 dividing line that Deligne's method would need has no geometric source in the present construction.
- **Standalone lemmas (goal 3):**
  - the six-exponentials consequence (IH5.3);
  - the two-prime faithful receiver (IH6);
  - the linearity of clock changes (PL2).

  All are elementary consequences of known theorems.
- **Bridges (goal 2):** Deligne's lifting mechanism, with its exact weight bookkeeping, is placed next to the Connes–Consani curves E_p = ℂ^×/p^ℤ and the explicit formula (TL7, PL6).

## Checks (claude-ab)

- **IH3.5, the defect recursion.** With D_n = n^{2β} − n, (D_a + a)(D_b + b) = (ab)^{2β} = D_{ab} + ab. Checked by expansion.
- **PL2.7 and PL6.8.** Both are one-line identities, checked.
- **TL4.2 and TL7.10.** These use only 0 < Re ρ < 1 and 1 < \|p^ρ\| = p^{Re ρ} < p; both are checked.
- **Not checked by me:** the six exponentials theorem, which is cited (Lang, Ramachandra; the programme cites Dasgupta, arXiv:2303.02037, Theorem 4.2); and TL7a–TL7b's adelic and distribution computations.
