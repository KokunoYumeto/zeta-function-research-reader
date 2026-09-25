# The owner's anomaly picture made exact: two lines, anti-numbers, chirality and the prime knots

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 10:57 UTC.

This note answers the owner's messages M17–M27 of 25 September (verbatim in the private provenance file). It builds the model first, with full precision, and tests it afterwards, as M18 asks. It follows the owner's standing corrections, as recorded in the transcript uploaded with M17:
- no additive operations on τ;
- the parityless support keeps the winding data it carries;
- consequences are derived, not inserted as definitions;
- an objection must address the actual construction.

Every statement marked **proved** has its proof here or in a cited note. Every statement marked **checked** is in `checks/anomaly_two_line_model_checks.py`, with output in `checks/anomaly_two_line_model_checks_OUTPUT.txt`. A **proposal** is a typed matching between the owner's terms and exact objects: the objects and the facts about them are proved; the matching itself is a proposal. A **reading** interprets proved statements.

## 0. The owner's argument, as one piece

1. **Parity is a quantum number of numbers.** The notation Z₁/Z₂ marks this symmetry: Z₁ is presence, or mere existence, and Z₂ is parity. The support τ is parityless but carries winding and torsion data.
2. **Parity is a global anomaly.** Every parity must be cancelled by a parity partner for the system to be globally consistent. The model is Witten's SU(2) anomaly: one doublet's partition function flips sign under the large gauge transformation (the "great rotation"), and cancellation needs a second doublet. A mirror image of the first does not do it.
3. **One critical line is anomalous; two lines cancel.** The lines Re s = ½ and Re s = −½ are present at once ("there is never not two"). The shift is only how one finds the second line; the content is that both exist simultaneously.
4. **Four directions.** The sign needs four directions, not two: a full rotation gives a sign in four dimensions and none in two. Connes–Consani's newest paper has four directions (the rays), and their knots–primes paper contains a sign.
5. **Mechanisms.** Chiral partners and anomaly inflow (Freed–Hopkins; Lurie/Teleman) are candidate mechanisms of the cancellation. The double helix is the picture of the pair.
6. **Particle, antiparticle and chirality are three different things (M21–M23).**
   - A number has an anti-number, "on the other side of τ". It is not −n: it annihilates the number, but not by subtraction.
   - The anti-number is "anti-present": its Z₁ element carries a minus sign. It is the number in negative time, in Feynman's sense, and the owner treats anti-time and anti-unitarity as interchangeable.
   - This is not ordinary time-reversal symmetry. It is anti-time in the sense of a CPT-symmetric universe.
   - A doublet consists of two particle–antiparticle pairs, and the pairs are chiral partners of each other.
7. **Two anomalies (M26).**
   - Z₁, the time direction, is also a global anomaly, cancelled by anti-time (unitarity and anti-unitarity), in the manner of a CPT-symmetric universe (Boyle–Finn–Turok).
   - Z₂, parity, is a different anomaly, cancelled by the chiral partner.
8. **The knots (M25).** Connes–Consani's *Knots, primes and class field theory* may be the right language for all of this.
9. **The payoff sought.**
   - With both lines in view, a forced rotation, a nontrivial holonomy in the sense of the knots paper, would show up as a distortion that one line alone hides.
   - So off-line zeros might become easier to detect, or the rigidity of the whole construction might forbid them.
10. **Method and aim (M18, M27).**
    - Build the model precisely, then test it.
    - Components that do not settle RH one at a time are still accurate descriptions. They are kept because a later combination may need them (§5).

## 1. The dictionary (proposal; every object on the right is exact)

| owner's term | exact object | status |
|---|---|---|
| a number n | the clock u = n on the multiplicative line ℝ_{>0}, running for time log n; a prime p is the periodic orbit C_p of length log p (Connes–Consani 2025, the scaling action on X_ℚ) | definition (CC) |
| its anti-number | the same clock run backwards, u ↦ 1/u (time −log n), taken with complex conjugation: g ↦ g*, g*(u) = conj g(1/u)/u | proposal; Prop. 22.5 |
| "annihilates, but not by subtraction" | n·(1/n) = 1; for test functions (g ∗ g*)(1) = ‖g‖² | proved, checked (11b) |
| anti-time versus time reversal | g* (inversion and conjugation) against plain conjugation s ↦ s̄, which is the reality of ζ | proposal |
| anti-unitarity, "Cartan involution" | θ(g) = (g*)⁻¹; on the characters u^{s−½} it is s ↦ 1 − s̄, and its fixed set is the unitary line Re s = ½ | proved, checked (11c) |
| chirality, chiral partner | the mirror A(s) = −s̄ through the pole at 0; it carries Re s = ½ to Re s = −½ | proved (`17_`) |
| the doublet (two particle–antiparticle pairs, chiral partners of each other) | the orbit {ρ, ρ^#, A(ρ), A(ρ^#)} of a zero ρ in the two-line system, with ρ^# = 1 − ρ̄ | proved (Prop. 22.6) |
| four directions, the half-turn sign | Connes–Consani's Bombelli generator J with J² = ε: the rays 1, J, ε, εJ; the half-turn J² is the sign | definition (CC) |
| the SU(2) doublet's sign | the lift σ(z₁, z₂) = (−z̄₂, z̄₁) of their twistor real structure z ↦ −1/z̄; σ² = −1 | proved, checked (Prop. 22.1) |
| the Z₂ anomaly and its cancellation | the two lines are the two sheets of one connected double cover, with deck transformation the central −1 of SU(2) | proved, checked (Prop. 22.2) |
| the double helix, chiral pair | the owner's Hopf fibre D and the shift circle Γ: fibres of the left and the right Hopf fibrations | proved, checked (Prop. 22.3) |
| the Z₁ anomaly and its cancellation | the root-number phase W(χ) picked up crossing τ; the anti-number sector cancels it: W(χ)W(χ̄) = 1 | proved, checked (Prop. 22.8) |
| the prime knot and its reverse | C_p with monodromy Frob_p; reversal inverts the monodromy, which conjugates the character | proved (Prop. 22.8) |
| anomaly inflow | the open strip between the two lines is the bulk; it holds exactly the off-line zeros | proved (Prop. 22.7) |
| CPT-symmetric universe | the functional equation makes Re s < ½ the image of Re s > ½ with conjugate characters; the critical line is the fixed set of θ | reading |

## 2. The model

**Proposition 22.1 (four directions and the quaternionic sign).**
- Connes–Consani's twistor real structure z ↦ −1/z̄ (arXiv:2609.00299, the theorem on the twistor space) lifts to ℂ² as σ(z₁, z₂) = (−z̄₂, z̄₁).
- With q = z₁ + z₂j, σ is left multiplication by the quaternion j.
- σ commutes with SU(2), σ² = −1, and σ has no fixed point on ℂP¹.
- On the unit circle |z| = 1 it is the half-turn z ↦ −z.
- On two copies, σ ⊗ σ squares to +1, a real structure.

*Proof.*
1. [−z̄₂ : z̄₁] = −1/z̄ for z = z₁/z₂.
2. j(z₁ + z₂j) = z̄₁j − z̄₂, since jz = z̄j and j² = −1. So σ = L_j and σ² = L_{j²} = −1.
3. For U = [[a, −b̄], [b, ā]] ∈ SU(2), σ(Uz) = Uσ(z) by direct expansion.
4. A fixed point would need −1/z̄ = z, that is |z|² = −1. On |z| = 1, −1/z̄ = −z.
5. (σ⊗σ)² = σ²⊗σ² = (−1)(−1) = 1. ∎

This is the quaternionic (pseudoreal) structure of the SU(2) doublet. A single doublet admits no invariant real structure, which is why its fermion measure is a Pfaffian with a sign ambiguity. Two doublets admit one (Witten, *An SU(2) anomaly*, Phys. Lett. B 117 (1982) 324; checks 4a–4d). The Bombelli generator gives the four rays 1, J, ε, εJ, and the half-turn J² = ε is the sign (check 5a).

**Proposition 22.2 (the two lines are the two sheets of one double cover).**
- For s on Re s = ½ put p(s) = (s, s − 1)/(√2|s|). For s on Re s = −½ put p(s) = (s, s + 1)/(√2|s|).
- Both land on the circle Γ(φ) = (e^{iφ}, −e^{−iφ})/√2 of the Clifford torus, at φ = arg s: the critical line fills φ ∈ (−π/2, π/2) and the line at −½ fills φ ∈ (π/2, 3π/2).
- The map w = z₁/z₂ sends Γ onto the unit circle E, and Γ(φ + π) = −Γ(φ) has the same image. So Γ → E is a connected double cover whose deck transformation is the central element −1 of SU(2).
- One full turn of w lifts to a path from the critical line to the line at −½. Two turns are needed to return.

*Proof.*
1. On Re s = ½, s − 1 = −s̄, so p(s) = (e^{iφ}, −e^{−iφ})/√2. On Re s = −½, s + 1 = −s̄, which gives the same formula.
2. w = −e^{2iφ} has degree 2 in φ, and Γ(φ + π) = −Γ(φ). ∎ (Checks 2a–2d.)

A small rotation stays on one line; only the full turn changes line. So the Z₂ is global, not visible infinitesimally, as in Witten's case, where the anomaly sits in π₄(SU(2)) = ℤ₂.

**Proposition 22.3 (the double helix is a chiral pair).**
- The owner's Hopf fibre from `6.tex`, the critical line with the pairing (s, 1 − s̄), is D(φ) = (e^{iφ}, e^{iφ})/√2, an orbit of left multiplication q ↦ e^{iα}q.
- Γ is an orbit of right multiplication q ↦ qe^{iα} = (e^{iα}z₁, e^{−iα}z₂).
- The reflection (z₁, z₂) ↦ (z₁, −z̄₂), of determinant −1 on ℝ⁴, carries Γ onto D.

So D and Γ are fibres of the left- and the right-handed Hopf fibrations, which correspond to the two factors of Spin(4) = SU(2)_L × SU(2)_R. In SO(4) = (SU(2)_L × SU(2)_R)/{±1} the central signs of the two chiralities cancel. (Checks 3a–3d; `17_` §4 for D, Γ and their intersection at t = ±∞.)

**Proposition 22.4 (the two-line product is real and positive on the line of the pole at 0).** For G(s) = F₀(s)F₀(s+1) = ξ(s)ξ(s+1)/16, the programme's separator function:
- G(−s̄) = conj G(s);
- G(it) = |ξ(1+it)|²/16 > 0 for every real t.

The 0-centred partner pairing Q_A(f) = Σ_{G(w)=0} f(w)·conj f(−w̄) is real, because A is an involution of the zeros of G. It is indefinite, even when every zero is on the line.

*Proof.*
1. ξ(1 − s) = ξ(s) and ξ(s̄) = conj ξ(s). Hence ξ(−s̄) = ξ(1 + s̄) = conj ξ(1 + s) and ξ(1 − s̄) = conj ξ(s), which gives the first identity.
2. At s = it, ξ(it) = ξ(1 − it) = conj ξ(1 + it), which gives G(it) = |ξ(1+it)|²/16. This is positive because ζ has no zeros on Re s = 1.
3. Substituting w ↦ −w̄ in Q_A gives its conjugate.
4. For indefiniteness, multiply f by e^{iαs}. Each on-line term f(ρ)conj f(ρ−1) is multiplied by e^{iα}e^{−2αγ}. Check 10 shows both signs for f_α(s) = e^{iαs}e^{iπs}e^{(s+1/4)²} over the first 30 zeros and their conjugates. ∎

`17_` found the 0-centred pairing not real for ζ alone. With both lines present it becomes real, because the pair is real where each factor alone is not: the zeta form of Pf·conj Pf = |Pf|². (Checks 1a–1c, 10.)

**Proposition 22.5 (anti-number and chirality are one operation in two normalisations).** Put g^A(u) = conj g(1/u), which is unitary for the Haar measure du/u, and g^#(u) = conj g(1/u)/u, which is unitary for du. With the Mellin transform ĝ(s) = ∫₀^∞ g(u)u^{s−1}du:
- (g^A)^(s) = conj ĝ(−s̄), the mirror A centred at 0;
- (g^#)^(s) = conj ĝ(1 − s̄), the reflection # through ½;
- g^# = g^A/u, so the two differ exactly by the factor u, the Tate twist of `17_` (B∘A = T₁);
- each annihilates g into a norm at the unit: (g ∗ g^A)(1) = ∫|g|²du/u and (g ∗ g^#)(1) = ∫|g|²du;
- on the characters u^{s−½}, θ(g) = (g*)⁻¹ acts by s ↦ 1 − s̄ and fixes exactly Re s = ½.

*Proof.* Substitute u ↦ 1/u in the Mellin integral. The convolution at 1 is ∫g(v)g*(1/v)dv/v. conj(u^{s−½})⁻¹ = u^{(1−s̄)−½}, and |u^{s−½}| = u^{Re s−½}. ∎ (Checks 11a–11c.)

So the owner's antiparticle and chiral partner are the same geometric act, running the clock backwards with conjugation, measured in two different densities. Only the ½-centred one gives Weil's positivity: RH holds if and only if the Weil functional is nonnegative on every annihilation g ∗ g^# (Weil's criterion; Bombieri, *The Riemann Hypothesis*, Clay problem description, §V; `17_` Prop. 17.5).

**Proposition 22.6 (the doublet and the holonomy).**
- On the two-line zero set Z ⊔ (Z − 1), four maps form a Klein four-group:
  - the identity;
  - the mirror A;
  - the internal reflection P, which is # on Z and s ↦ −1 − s̄ on Z − 1;
  - T = AP.
- T is s ↦ s − 1 on Z and s ↦ s + 1 on Z − 1.
- Orbits:
  - an on-line zero ρ has orbit {ρ, ρ − 1}; its particle–antiparticle pair collapses, because ρ^# = ρ;
  - an off-line zero has orbit {ρ, ρ^#, A(ρ), A(ρ^#)} = {ρ, ρ^#, ρ^# − 1, ρ − 1}: two particle–antiparticle pairs that are chiral partners of each other, the owner's doublet.
- The loop "across by A, back by T⁻¹" has holonomy T⁻¹A = # on Z. It is trivial exactly at on-line zeros.

*Proof.* A² = P² = 1 and AP = PA hold because A conjugates # into s ↦ −1 − s̄. A(1 − s̄) = s − 1, and A(s) + 1 = 1 − s̄. ∎ (Checks 6a–6c.)

So RH says: every zero is its own anti-number. Equivalently, for every zero, "the other side of τ" equals "the anti-time version": 1 − ρ = ρ̄, which is the owner's sentence in M21.

**Proposition 22.7 (inflow: the bulk between the lines).**
- The zeros of G in the open strip −½ < Re s < ½ are exactly the zeros of ζ with Re ρ < ½, together with their mirrors A(ρ).
- The on-line zeros sit on the two boundary lines.
- RH holds if and only if the bulk is empty.
- The argument principle on rectangles in the strip computes the bulk count from the values of G on the boundary.

*Proof.* A zero ρ − 1 of ζ(s + 1) lies in the strip if and only if Re ρ > ½, and then ρ − 1 = A(ρ^#). ∎ (Check 8.)

**Proposition 22.8 (knots, anti-numbers and the Z₁ phase).**
- (a) In Connes–Consani, arXiv:2501.06560, Theorem 3.12(iii), the monodromy of the periodic orbit C_p in the cover X_ℚ^L attached to a finite abelian extension L is Frob_p.
  - Reversing the orbit inverts the monodromy.
  - For a unitary character χ of Gal(L/ℚ), χ(g⁻¹) = χ̄(g). So the reversed knot carries the conjugate character: the anti-number of a prime knot, in the character, is χ̄.
- (b) For a primitive Dirichlet character χ mod q with χ(−1) = (−1)^a, Λ(s, χ) = (q/π)^{(s+a)/2}Γ((s+a)/2)L(s, χ) satisfies Λ(s, χ) = W(χ)Λ(1 − s, χ̄), with W(χ) = τ(χ)/(i^a√q) and |W(χ)| = 1 (Davenport, *Multiplicative Number Theory*, ch. 9). Crossing τ = ½ carries the particle sector χ into the antiparticle sector χ̄ and costs the phase W(χ).
- (c) W(χ)W(χ̄) = 1. Real characters, which are their own anti-characters, have W = 1.

*Proof of (c).*
1. τ(χ̄) = χ(−1)·conj τ(χ) and |τ(χ)|² = q, so τ(χ)τ(χ̄) = χ(−1)q.
2. Hence W(χ)W(χ̄) = χ(−1)q/(i^{2a}q) = χ(−1)(−1)^a = 1.
3. For real χ, W = 1 by Gauss's determination of the sign of the quadratic Gauss sum (Davenport, ch. 2). ∎

Check 12 verifies (b) and (c) for every character mod 5 and mod 7. For χ mod 5 with χ(2) = i, W(χ) = 0.85065 + 0.52573i, a phase of 31.72°.

*Reading.* This is the owner's Z₁ anomaly and its cancellation (M26). The time orientation of a sector is its character. Crossing τ reverses it (χ ↦ χ̄) at the cost of the phase W. The anti-number sector cancels the phase exactly. ζ and the real characters are their own antiparticles, with nothing to cancel.

## 3. Tests: what the simplest versions give, and what they need

**22.9 (parity sees only self-conjugate zeros).** Proved.
- The Z₂ anomaly of one line is the monodromy of √ξ around the part of the critical strip below height T. It equals (−1)^{N(T)}. When the on-line zeros up to T are simple it matches −sgn Z(T), Hardy's function: checked at eight heights up to T = 1000 (check 7a).
- Off-line zeros come in pairs at the same height, so they cancel mod 2.
- In the two-line system the count is 2N₀ + 4N_pairs. So the ℤ₂ and ℤ₄ (four-direction) anomalies vanish identically. The first level that sees off-line zeros is mod 8 (the parity of N_pairs), or the integer count itself, which is Turing's method (A. M. Turing, Proc. London Math. Soc. (3) 3 (1953) 99–117). (Check 7b.)
- *What this gives:* the torsion anomalies are exactly the part of the structure that every symmetric configuration satisfies. Any argument that uses them must add something that distinguishes ζ.
- *What it needs:* the integer count, or the holonomy of Prop. 22.6, whose triviality at each zero is Re ρ = ½.

**22.10 (the structure without the Euler product).** Proved and checked.
- The Davenport–Heilbronn function f has the whole structure of §2:
  - Λ_f(s) = (5/π)^{(s+1)/2}Γ((s+1)/2)f(s) = Λ_f(1 − s);
  - Λ_f is real on the real axis;
  - G_f(−s̄) = conj G_f(s) and G_f(it) ≥ 0;
  - its zero 0.808517182457 + 85.6993484854i is off the line, with a Klein-four orbit of size 4 (checks 9a–9c).
- So Props. 22.1–22.7 together do not force RH.
- *What they need:* an ingredient that ζ has and f lacks. That ingredient is the Euler product, which in Connes–Consani's language is the prime knots with their monodromy.

**22.11 (cancelling Z₁ by addition or by multiplication).** Proved and checked.
- f = cL(s, χ) + c̄L(s, χ̄) for χ mod 5 with χ(2) = i and c = (1 − iκ)/2 (check 13). It is a superposition of a particle sector and its antiparticle sector, with coefficients chosen so that the phase cancels and the root number of f is 1.
- The phase cancels, the Euler product is lost, and the zero above is off the line.
- The doublet L(s, χ)L(s, χ̄) cancels the same phase by multiplication: W(χ)W(χ̄) = 1. It keeps the Euler product, and its zeros are those of its two factors.
- *What this gives:* the anomaly picture separates cancellation by multiplication from cancellation by addition, and the Euler product is exactly what this separation tracks.
- *What it needs:* a proof that multiplicative cancellation forces the zeros onto the line. For the doublet that statement is GRH for L(s, χ), which is open.

## 4. What was learned

- **Every component of the owner's picture has an exact counterpart.**
  - Four directions and the quaternionic sign: Prop. 22.1.
  - Two lines as one double cover with the central sign: 22.2.
  - The chiral pair: 22.3.
  - The pair's positivity on the pole's line: 22.4.
  - Anti-number and chirality as one operation in two normalisations: 22.5.
  - The doublet and its holonomy: 22.6.
  - Inflow: 22.7.
  - The knots and the Z₁ phase: 22.8.
  - The dictionary of §1 is a complete matching between the pieces of the anomaly-cancellation machinery used here and exact structures of ζ and its L-functions. It is a result in its own right, independent of RH.
- **The two anomalies behave differently.**
  - Z₂ (parity) cancels automatically for every symmetric configuration, which is why it cannot see off-line zeros.
  - Z₁ (the phase) cancels only by pairing a sector with its anti-sector, and the way it is cancelled, by product or by sum, is where ζ differs from the Davenport–Heilbronn function.
- **RH, in the owner's words, has three exact forms here:**
  - every zero is its own anti-number (Prop. 22.6);
  - number–anti-number annihilation is positive (Weil, Prop. 22.5);
  - the bulk between the two lines is empty (Prop. 22.7).

## 5. Continuation: combinations the construction makes available

As M27 says, components that do not individually settle RH are kept, because combinations may. These are the next constructions, each stated precisely enough to be proved or refuted.

1. **The multiplicative doublet class.**
   - Consider products Λ = ∏Λ(s, χᵢ) over multisets closed under χ ↦ χ̄; for these the Z₁ phase cancels (Prop. 22.8(c)), and G_Λ(s) = Λ(s)Λ(s+1) is real and ≥ 0 on Re s = 0 (Prop. 22.4 applies verbatim).
   - *Question:* combine the positivity of G_Λ on the pole's line with the explicit formula for G_Λ, whose prime side carries the weights (1 + p^{−k}) of the second line. Does the combination bound the bulk count of Prop. 22.7 better than Turing's method does?
2. **Annihilation positivity with two lines.**
   - The two-line system carries two Hermitian forms: Weil's ½-centred form on each copy, positive exactly under RH, and the 0-centred cross form Q_A, which is indefinite (Prop. 22.4).
   - Together they make the two-line space an indefinite (Krein-type) inner-product space.
   - *Question:* is RH equivalent to a maximality or positivity statement for a subspace of this space, and does the chiral cross form add information that Weil's form alone does not?
3. **Detection at the knots: the prime squares.**
   - A knot traversed twice carries the monodromy χ(p)² = 1: two copies cancel the sign.
   - The prime squares contribute to Σ_{n≤x} χ(n)Λ(n) the term θ(√x) ~ √x, of exactly the size x^{1/2} that on-line zeros produce.
   - Under GRH and linear independence of the ordinates, this makes the primes 3 mod 4 lead in the famous proportion 0.9959 (Rubinstein–Sarnak, *Chebyshev's bias*, Experiment. Math. 3 (1994) 173–197). A zero of L(s, χ₋₄) with real part above ½ would produce oscillations larger than √x.
   - *Question:* formulate the owner's "distortion visible only with both lines" as the corresponding bias for the two-line system, and compute it.
4. **The holonomy as a function.** Prop. 22.6 gives the holonomy only at zeros. Extend it to a map on the whole strip, built from G and its two partner involutions, whose fixed points are the on-line zeros. The aim is an index or degree that counts off-line zeros from boundary data alone.

## 6. Items for the goals

- **Bridges (goal 2).** The §1 dictionary between the anomaly-cancellation machinery (Witten's SU(2) anomaly, chirality, CPT, inflow) and the symmetries of ζ, its L-functions and Connes–Consani's knots.
- **Negative results with scope (goal 1).**
  - 22.9: ℤ₂ and ℤ₄ anomalies cannot see off-line zeros.
  - 22.10: the full symmetry structure exists for a function with off-line zeros.
- **Lemmas that stand alone (goal 3).**
  - 22.4: G is real on Re s = 0 and equals |ξ(1+it)|²/16 there.
  - 22.5: the two normalisations of the anti-number differ by the Tate twist.
  - 22.8(c): W(χ)W(χ̄) = 1, a standard fact, read as anomaly cancellation.
  - All are elementary; no novelty search was made.
- **F1 context (goal 4).** The Bombelli generator J (J² = ε) of the absolute twistor line gives the four directions, and the twistor real structure is the quaternionic sign (Prop. 22.1).

## 7. Checks

`checks/anomaly_two_line_model_checks.py`, output `checks/anomaly_two_line_model_checks_OUTPUT.txt`:

| item | test | result |
|---|---|---|
| 1a–1c | G(−s̄) = conj G(s); G(it) = \|ξ(1+it)\|²/16 > 0 on t ∈ [0, 300] | rel. error 4·10⁻³⁰; minimum > 0 |
| 2a–2d | both lines land on Γ; base winding; Γ(φ+π) = −Γ(φ); the lift changes line | all hold |
| 3a–3d | D and Γ as left and right orbits; quaternion check; reflection of determinant −1 | all hold |
| 4a–4d | σ² = −1; σ = L_j; induced map −1/z̄; (σ⊗σ)² = 1; σ commutes with SU(2) | all hold |
| 5a–5b | J² = ε; odd Frobenius winding = χ₋₄(n)·n for n ≤ 15 | all hold |
| 6a–6c | Klein four-group on a synthetic two-line system; orbit sizes 2 and 4; holonomy = # | all hold |
| 7a–7b | sgn Z(T) = −(−1)^{N(T)} at eight heights up to T = 1000; the counting hierarchy | all hold |
| 8 | the bulk holds exactly the off-line zeros and their mirrors | holds |
| 9a–9c | Davenport–Heilbronn: completed functional equation, reality, G_f ≥ 0 on Re s = 0, orbit of size 4 | residuals ≤ 5·10⁻³⁰ |
| 10 | Q_A takes both signs on on-line zeros | holds |
| 11a–11c | Mellin shadows of the two normalisations; annihilation into norms; Cartan fixed set | exact to working precision |
| 12 | root numbers mod 5 and 7: \|W\| = 1, W(χ)W(χ̄) = 1, functional equations | all hold (residuals < 10⁻²⁹) |
| 13 | Davenport–Heilbronn as the superposition of χ and χ̄ with conjugate coefficients | holds; W(χ) phase 31.72° |

## 8. Sources

- A. Connes, C. Consani, *The Absolute Twistor Line and the Geometry of Spec ℤ* (compactified), arXiv:2609.00299v1 (read in full on 23 September; the Bombelli generator, the twistor real structure, the odd Frobenius).
- A. Connes, C. Consani, *Knots, primes and class field theory*, arXiv:2501.06560 (Theorem 3.12(iii), Remark 3.13; read through the arXiv PDF for these statements).
- E. Witten, *An SU(2) anomaly*, Phys. Lett. B 117 (1982) 324–328.
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer GTM 74, chs. 2 and 9.
- A. M. Turing, *Some calculations of the Riemann zeta-function*, Proc. London Math. Soc. (3) 3 (1953) 99–117.
- M. Rubinstein, P. Sarnak, *Chebyshev's bias*, Experiment. Math. 3 (1994) 173–197.
- R. P. Feynman, *The theory of positrons*, Phys. Rev. 76 (1949) 749–759 (the backwards-in-time antiparticle).
- L. Boyle, K. Finn, N. Turok, *CPT-symmetric universe*, Phys. Rev. Lett. 121 (2018) 251301.
- E. Bombieri, *The Riemann Hypothesis*, Clay Mathematics Institute problem description, §V (Weil's criterion).
- The owner's `6.tex` (the Hopf section) and the programme's separator G (ADM6, `18_`).
