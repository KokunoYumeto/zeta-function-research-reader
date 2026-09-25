# The Deligne reader, part 2 (DB, DBC, DW0–DW4): Weil II §§2.1–2.2 and 3.1–3.2 are reconstructed correctly, nine of the reader's "transcription" corrections are misprints of the printed paper, and the ζ specialization is the classical one

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 17:59 UTC. Board task 8: the Deligne reader outside the parts read earlier. The first pass was an audit by one subagent (64 checks); §0 says what I verified myself. Not yet refereed.

## 0. Source, method and checks

- **Source.** `DELIGNE_WEIGHT_CONTROL_FULL.md`, the programme's Deligne reader: 4688 lines, SHA-256 `6478584d…26ffa595`, published in the reader repository at `workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/` (commit 36a82ec).
  - **Audited here:**
    - DB0–DB8 and DB10 (lines 1478–1918): Weil II §2.1, the method of Hadamard and de la Vallée-Poussin.
    - DBC1–DBC11 (lines 1919–2338): §2.2, the compact form and the strict bound.
    - DW0–DW4 (lines 2339–2652): §§3.1–3.2, the pencil, vanishing cycles and reality.
  - **Read before:** DB9, DR, DC, DW5–DW11 and MDB9–MDB11 (`07_`, `08_`), and DP, DMG and DLM (`36_`).
- **Label note.** "DW" here means the reader's sections. `35_` uses the prefix for another file.
- **Method.** One subagent made the first pass: an item-by-item verdict and 64 checks on explicit models (17 of them controls that must reject a wrong variant), all passing. My re-run at 17:58 UTC reproduces the output exactly. I verified the following myself:
  - the printed displays behind the nine discrepancies, on page images of the numdam scan: pp. 187, 191, 195, 199 (the display line only), 200, 202 (with its context) and 203, and earlier pp. 160 and 170;
  - Deligne's definition of the real part ℛ(τ) on p. 187, which decides the sign of the weight in 2.2.8(i);
  - the counterexample to the printed choice ε₁ + ε₂ < ε in the proof of 2.1.7, by hand (§2);
  - Lemmas 37.1–37.3 and the negative results, by the derivations given below.
- **Checks.** `checks/deligne_reader_part2_checks.py`: the subagent's script, 64 items (A1–L5), unchanged apart from the header.

**Verdict.**
- **The reconstruction is correct as far as checked.** No step fails. In three places it is more careful than the printed text:
  - it repairs the concentration lemma's proof (DB5);
  - it proves the simple pole of the curve zeta function at s = 1 from point counts alone (DBC7);
  - it supplies the order bookkeeping that Deligne leaves to the reader (DBC9).
- **Nine discrepancies are misprints of the printed paper.** The reader attributes all nine to its French transcription and says explicitly that it does not attribute them to the printed original (DB0, line 1488; DBC2, line 1974; DBC3, line 2010; DW0, line 2367). The page images show all nine in print. One of them is a slip in a printed proof rather than a typographical error (§2).
- **The "exact original-zeta specialization" is classical.** It proves the Euler product, positivity of the prime-power measure, and ζ(1 + it) ≠ 0 (Hadamard, de la Vallée-Poussin, 1896). The reader says so itself (lines 1496, 1913).
- **No bridge.** The audited range builds no map from a programme object into Deligne's objects. Its disclaimers (lines 1913, 2345, 2442, 2589) are accurate.

## 1. What the three parts prove

- **DB (§2.1).**
  - **Setting.** G is a locally compact extension of Γ ≅ ℤ or ℝ by a compact group, with conjugacy classes x_v (the Frobenius classes) and quasi-characters ω_s(g) = q^{−s·deg g}.
  - **Hypotheses.** Absolute convergence of the L-functions L(τ, s) for Re(τω_s) > 1, and meromorphy with controlled poles on the boundary line.
  - **Conclusion (Théorème 2.1.4).** L(τ, s) has no zero on Re(τω_s) = 1, except possibly one quadratic character with a simple zero.
  - **The steps.**
    - DB2: the positivity of the measure behind −L′/L.
    - DB3: the residues ν(τ).
    - DB4: reduction to a compact group.
    - DB5: the concentration lemma 2.1.7 (Lemma 37.1).
    - DB6: the bound Σ_τ d_τ(−ν(τ)) ≤ 1 (Lemma 37.2).
    - DB7–DB8: pole cancellation and equidistribution (2.1.11–2.1.13).
- **DBC (§2.2).** For a pure lisse sheaf on a curve over F_q:
  - the compact form of the monodromy (DBC3–DBC5);
  - the L-function identity (DBC6);
  - the simple pole of the curve zeta function (DBC7; Lemma 37.3);
  - condition (C), where a double cover removes the quadratic exception (DBC8);
  - the strict bound w < β + 2 on H¹_c (DBC9, = 2.2.10).
- **DW0–DW4 (§§3.1–3.2).**
  - the Lefschetz pencil and its blow-up (DW2);
  - the vanishing cycles at a node, a tangency and a crossing (DW3). The first pass checks the formulas by point counts on explicit pencils over F₇, F₁₁ and F₁₃.
  - the reality of the characteristic polynomials (3.2.1–3.2.2), which uses the strict bound of 2.2.10 (DW4).

## 2. The nine discrepancies, on the printed pages

The reader flags each of these as a defect of its transcription. The printed pages show every one in print. "Verified" means that I read the display on the page image.

| # | Place | Printed | Correct | Status |
|---|---|---|---|---|
| 1 | (2.1.1), p. 187 | the period is ω_s = ω_{s+2πi log q} | ω_s(g) = q^{−s·deg g} has period 2πi/log q in s | misprint; verified |
| 2 | proof of 2.1.7, p. 191 | "ε₁ + ε₂ < ε", followed by a chain that ignores the part of the integral outside V | ε₁ + 2ε₂ < ε (the lemma is true; see below) | slip in a printed proof; verified |
| 3 | 2.2.8(i), p. 195 | the sheaf is pointwise ι-pure of weight 2ℛ(τ) | −2ℛ(τ) (see below) | sign misprint, harmless in 2.2.10, where the weight is twisted to 0; verified |
| 4 | 1.3.10(iv), p. 160 | the centre maps onto a finite subgroup of ℤ | a subgroup of finite index | misprint; verified (`35_` §5) |
| 5 | proof of 3.2.1, p. 200 | H⁰ on a projective curve is dual to H²_c(X, F^∨(−1)) | F^∨(1): Poincaré duality pairs H⁰(X, F) with H²(X, F^∨(1)) into H²(X, Q_ℓ(1)) ≅ Q_ℓ | misprint, harmless for reality; verified |
| 6 | (3.2.7.1), p. 202 | (R¹f_!π*H₀)_x̄ = H¹(Y, π*H) | H¹_c: Y is a fibre of f: U₀ × U₀ → A₀*, an open curve in general, and proper base change for f_! gives compact support (the text then applies 3.2.2, a statement about H_c) | misprint; verified with its context |
| 7 | proof of 3.2.12, p. 203 | the bound w_{N(x)}(α) ≤ β + i, inside a proof at weight 0 | w ≤ i | a free β; harmless; verified |
| 8 | (1.6.14.3), p. 170 | the twist P_{−j}((i+j)/2) | P_{−j}(−(i+j)/2) | misprint; verified (`35_`, `36_`) |
| 9 | (3.1.3.3), p. 199, a remark "not used" | the Kummer cover of uv^{−1} gives a canonical generator | on uv = t, [u] + [v] = 0, so [uv^{−1}] = 2[u], not a generator when ℓ = 2 | display line verified; the reading of the next lines is the first pass's |

**Item 2 in detail.**
- **The printed chain** (p. 191) bounds ∫|ρ₀(g)|²τ(g)dg below by (1 − ε)τ(e)∫|ρ₀|². The hypotheses give two things:
  - on the neighbourhood V, Re τ ≥ (1 − ε₁)τ(e);
  - off V, the mass ∫_{K∖V}|ρ₀|² is at most ε₂ of the total.
- **The outside term.** Off V, Re τ can be as low as −τ(e). The correct lower bound is therefore ((1 − ε₁)(1 − ε₂) − ε₂)·τ(e)·∫|ρ₀|².
- **A counterexample** to the choice ε₁ + ε₂ < ε:
  - Take K = ℤ/2 = {e, g}, τ = sgn, V = {e}, and ρ₀ = 23·1 + 9·sgn. So ρ₀(e) = 32 and ρ₀(g) = 14, and ρ = ρ₀ since both coefficients are positive.
  - With Haar measure ½ on each point, ∫|ρ₀|² = (32² + 14²)/2 = 610. The outside mass is 98/610 < 0.18.
  - So ε₁ = 0.01, ε₂ = 0.18 and ε = 0.2 satisfy ε₁ + ε₂ < ε.
  - But [ρρ̄ : sgn] = 2·23·9 = 414 < 0.8·610 = 488 (check B3).
- **The repair.** With ε₁ + 2ε₂ < ε, the correct bound (1 − ε₁)(1 − ε₂) − ε₂ ≥ 1 − ε₁ − 2ε₂ > 1 − ε gives the lemma (Lemma 37.1; check B4). The reader's DB0 and DB5 make exactly this repair.

**Item 3 in detail.**
- On p. 187 Deligne defines ℛ(τ) = σ by |τ(g)| = ω_σ(g) = q^{−σ·deg g} for central g.
- So the eigenvalues of τ at a Frobenius class x_v of degree d have modulus q^{−σd} = Nv^{−σ}. For the geometric Frobenius classes of §2.2, that is weight −2σ.
- The same sign follows from convergence. L(τ, s) converges for Re s > 1 − σ, and the L-function of a sheaf of weight w converges for Re s > 1 + w/2. These agree only if w = −2σ (check E1; E2 rejects +2σ).

**Provenance.**
- The reader's reading log records a comparison with the printed pages for §1 (see `36_` §2). Its §2–§3 sections still say "not claims that Deligne printed these errors".
- Their mathematics stands. Their provenance sentences should say that the defects are in print.
- I claim no novelty for the list: `36_` §2 reports a quick errata search that found none.

## 3. The first pass's further findings, with my assessment

- **Notation clash (line 1496).** "No arithmetic on τ is introduced" uses τ for the programme's supporting datum, while everywhere else in DB and DBC τ is an irreducible representation. Harmless, but one of the two should be renamed. Agreed.
- **An unused step (DB5, lines 1666–1668).** The shift that makes the approximant strictly positive is never used; only reality, invariance under inversion and the mass ratio are. Redundant, not wrong. Agreed.
- **DB1 (line 1538).** Its remark that DB2–DB6 do not use the central-degree condition is right for the proofs. The statement of 2.1.4 at non-unitary points does use ℛ(τ), which is defined through a central element (p. 187). Agreed.
- **DBC7 preamble (line 2154).** The reader contrasts its proof with invoking equidistribution, "whose hypotheses already include that pole". Deligne's sketch (p. 195) invokes the arguments of 2.1.12, not the theorem, so the circularity concern may not apply. This is the first pass's reading of p. 195, which I did not read. The reader's own proof is complete either way.
- **Gaps.** None in what the reader claims to prove. Several standard facts are quoted: the Cartan decomposition for complex reductive groups (DBC3), 1.3.12 and 1.3.14 (DBC5, DBC8), and the tame local structure (3.1.2) (DW3). The first pass gives a direct proof of the weight formula (DBC.5.1): det V_a has finite order on G⁰, and evaluating at F_v and at the central element gives |ιλ_a| = q^{mβ_a/2}.

## 4. Standalone lemmas

**Lemma 37.1 (concentration, with the outside term; the corrected 2.1.7).**
- **Setting.**
  - K is a compact group with normalized Haar measure, and τ an irreducible character of degree d_τ.
  - V ⊂ K is a set on which Re χ_τ ≥ (1 − e₁)d_τ.
  - ρ₀ is a finite integer combination of irreducible characters, real and invariant under g ↦ g^{−1}, with ∫_{K∖V}|ρ₀|² ≤ e₂∫|ρ₀|². Write ρ₀ = ρ⁺ − ρ⁻ with ρ^± genuine and without common constituents, and ρ = ρ⁺ + ρ⁻.
- **Statement.** [ρρ̄ : 1] = ∫|ρ₀|² and [ρρ̄ : τ] ≥ ((1 − e₁)(1 − e₂) − e₂)·d_τ·[ρρ̄ : 1].
- **Proof.**
  - ρρ̄ = ρ₀ρ̄₀ + 2(ρ⁺ρ̄⁻ + ρ⁻ρ̄⁺), and the second term is a genuine representation.
  - [ρ⁺ρ̄⁻ : 1] = ⟨ρ⁺, ρ⁻⟩ = 0.
  - The multiplicity [ρ₀ρ̄₀ : τ] = ∫|ρ₀|² χ̄_τ is real, so it equals ∫|ρ₀|² Re χ_τ. Split that integral into the part over V, which is ≥ (1 − e₁)(1 − e₂)d_τ∫|ρ₀|², and the part off V, which is ≥ −e₂d_τ∫|ρ₀|². ∎
- **Sharpness.** The constant is sharp in e₂: on ℤ/2 with V = {e}, the ratio is exactly 1 − 2e₂ for suitable ρ₀. By Peter–Weyl, such ρ₀ exist for every e₁, e₂ > 0 (DB5; checks B1–B4 on U(1) and SU(2)).

**Lemma 37.2 (the integer positivity bound; 2.1.5–2.1.6).**
- **Setting.** Let K be compact and ν: K̂ → ℤ a function, extended additively to virtual representations, with:
  - ν(1) = 1;
  - ν(τ̄) = ν(τ);
  - ν(τ) ≤ 0 for τ ≠ 1;
  - ν(ρρ̄) ≥ 0 for every genuine ρ.
- **Statement.** Σ_{τ≠1} d_τ(−ν(τ)) ≤ 1. So at most one τ ≠ 1 has ν(τ) < 0, and it is a real character of degree 1 with ν(τ) = −1, that is, a quadratic character.
- **Proof.**
  - Take a finite T ⊂ K̂ ∖ {1}, let e > 0, and take ρ from Lemma 37.1 for all τ ∈ T at once, with M = [ρρ̄ : 1].
  - Since ν ≤ 0 off 1, 0 ≤ ν(ρρ̄) ≤ M + Σ_{τ∈T}(1 − e)d_τMν(τ).
  - Divide by M and let e → 0.
  - A τ with ν(τ) < 0 contributes d_τ|ν(τ)| ≥ 1, so d_τ = 1 and ν(τ) = −1. Then τ̄, which has the same ν, must equal τ. ∎
- **Sharpness.** On ℤ/2, ν(sgn) = −1 satisfies every hypothesis: ν((a + b·sgn)(a + b·sgn)) = (a − b)² ≥ 0 (check C1). So positivity alone cannot exclude the quadratic exception, and Deligne needs the double cover (DBC8).

**Lemma 37.3 (nonnegative power sums; the core of DBC7).**
- **Setting.** Let a₁, …, a_r ∈ ℂ^× and δ ∈ ℝ, with N_n = δ − Σ_j a_jⁿ real and ≥ 0 for every n ≥ 1.
- **Statement.** Then max_j|a_j| ≤ 1.
- **Proof.**
  - Suppose R = max|a_j| > 1, and let J be the set of indices with |a_j| = R.
  - By Dirichlet's simultaneous approximation, infinitely many n have |(a_j/R)ⁿ − 1| < ½ for all j ∈ J. For those n, Re Σ_{j∈J} a_jⁿ ≥ |J|Rⁿ/2, while the other terms are O(R′ⁿ) with R′ < R.
  - So N_n = δ − Re Σ_j a_jⁿ → −∞ along those n, a contradiction. ∎
- **Corollary (the simple pole of the curve zeta function at s = 1, without the Riemann hypothesis for curves).**
  - Let X₀ be a smooth projective geometrically connected curve over F_q, and suppose an eigenvalue of Frobenius on H¹ equals q.
  - Then #X₀(F_{qⁿ}) = 1 − Σ_{j≥2}α_jⁿ ≥ 0 for all n. By the lemma, |α_j| ≤ 1 for j ≥ 2, so the counts are bounded.
  - They are not bounded: X₀ has infinitely many closed points, and for n a common multiple of the degrees of C + 1 of them, #X₀(F_{qⁿ}) ≥ C + 1.
  - Hence P₁(q^{−1}) ≠ 0 (DBC7; checks F1–F4).
  - I claim no novelty for this argument.

## 5. Negative results (goal 1)

- **37.N1. Positivity alone cannot exclude the quadratic exception** (Lemma 37.2, sharpness). An extra input, the double cover of DBC8, is necessary.
- **37.N2. The method of §2.1 speaks only about the edge of absolute convergence.**
  - For ζ it gives ζ(1 + it) ≠ 0 and the classical positivity of the prime-power measure, and nothing about 0 < Re s < 1.
  - The reader's specialization DB9 is exactly Deligne's example 2.1.9 with G = ℝ, K = {0} and x_p = log p. As the reader says (line 1913), everything beyond it would need "an actual receiving construction".
- **37.N3. For ζ this route has no analogue of the rest of the argument.** The data G = ℝ, K = {0} have no compact form, no curve and no trace formula. So there is no analogue of DBC3–DBC5, of the cohomological proof of condition (C) (DBC6–DBC8), of the strict bound (DBC9), or of §3.
- **37.N4. The printed choice ε₁ + ε₂ < ε in the proof of 2.1.7 does not give the displayed inequality** (§2, item 2); ε₁ + 2ε₂ < ε does.
- **37.N5. The tensor Euler products of the off-line quartet cannot detect zeros of ζ.**
  - ℒ_k(s) = ∏ζ(s − σ(ω))^{m^{2k}} (`35_` §2) is defined from the exponent data {ρ, ρ̄, 1 − ρ, 1 − ρ̄} alone.
  - Its genuine pole at 1 + 2k·max(Re ρ, 1 − Re ρ) exists for every complex ρ. The other factors are evaluated at real part ≥ 1, where ζ has no zero, and the argument never uses ζ(ρ) = 0.
  - The first pass checks this at ρ = 0.7 + 10i, where |ζ(ρ)| ≈ 1.48 (check L2).
  - This sharpens `29_` 29.N4: the object never sees whether ρ is a zero.

## 6. Bridges (goal 2)

**Deligne's four inputs, against the programme's quartet.** Deligne's use of tensor powers (1.5.1, DW4) needs four things, labelled (R), (D), (S) and (P). The programme's representation of the off-line quartet (ω_{−ρ} ⊕ ω_{−ρ̄} ⊕ ω_{ρ−1} ⊕ ω_{ρ̄−1} on G = ℝ, with x_p = log p) meets two of them:

| Input | What it requires | Status for the quartet |
|---|---|---|
| (R) | real local polynomials | holds: the quartet is closed under conjugation |
| (D) | a known determinant weight | holds: the determinant weight is exactly 1 (`35_` 35.N1) |
| (S) | a monodromy group whose determinant controls its constituents (§1.3) | fails: G = ℝ is abelian, and the representation is a sum of characters whose real parts the determinant does not control |
| (P) | a bound on the poles of every even tensor power's L-function at the determinant-weight location, supplied on a curve by H²_c | fails: the pole sits at 1 + 2k·max(Re ρ, 1 − Re ρ) for every ρ (37.N5) |

- **What this means.** This is the precise form of the missing input named in `29_` 29.N4, `35_` 35.N1 and `36_` §6. A bridge would need an object that meets (S) and (P) and whose Frobenius data equal the quartet only when ζ(ρ) = 0. Nothing in the audited range provides one.
- **The ramification relation.** On a finite-dimensional space, NP = bPN with b not a root of unity forces N to be nilpotent: N is similar to bN, so its finite spectrum is stable under multiplication by b. The relation also makes N shift eigenvalues by the factor b^{−1}. It says nothing about their absolute values (check L3). Together with `36_` 36.N4 (no eigenvectors on Ẽ), the relation is all that transfers.

## 7. Not checked

- The first pass's reading of p. 195 around the DBC7 comparison, and of the lines after (3.1.3.3) on p. 199.
- The English transcription: it was not supplied, so the reader's English-witness rows cannot be checked. The printed French agrees with every formula the reader adopts in those rows (first pass).
- The external theorems: Peter–Weyl, maximal compact subgroups of complex reductive groups, the trace formula, Lefschetz pencils and the Picard–Lefschetz formula, and SGA 7.
- The reader's MDB0–MDB8. They are the last block of the reader.
