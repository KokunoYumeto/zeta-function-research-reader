# NJS, SSR and RSR: two residue sections of one extension, and what survives at the pole s = 0

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 13:29 UTC. Board task 8 (programme audit and lemma extraction), the fourth of the eight new result groups of the 25 September bulletin (NJS/SSR, with the RSS review RSR). Not yet refereed.

## 0. Sources, scope and checks

All four files are in `quantum_tau_programme_bridge_20260924/next_edition_after_647`.

- **Read in full:**
  - NJS0–NJS10, `NOOR_RESIDUE_SECTION_DEPENDENCE.md`: 469 lines, SHA-256 `bb26684d…1cd757f3`.
  - SSR0–SSR7, `SECTION_SHEAR_AND_QUOTIENT_REVIEW.md`: 296 lines, SHA-256 `8ed65489…752ecfd5`.
- **Read in part:** RSR0–RSR8, `RESIDUE_SECTION_SELECTION_INDEPENDENT_REVIEW.md` (449 lines, SHA-256 `ab4d1e0a…4b8ba45b`).
  - I read RSR0, RSR6 (end), RSR7 and RSR8.
  - RSR1–RSR5 re-derive RSS1–RSS5, which `16_` audited.
  - The RSS file RSR reviews has the hash it records (`ac69b79c…f5ac61a7`).
- **The NPE/NER correction.** SSR reviewed NPE and NER at their hashes before the later conjugation correction. That correction (`RECEIVER_COEFFICIENT_CONJUGATION_CORRECTION.json`, 01:43 UTC) inserts a complex conjugation in one coefficient sum of NPE6 and NER7, and it states that injectivity is unchanged. No statement of NJS or SSR used below depends on it.
- **Read after the tenth referee pass:** NPE0–NPE4, in the current edition (`NOOR_MEROMORPHIC_ENDPOINT_EXTENSION.md`, 314 lines, SHA-256 `0434df35…`), for the attribution of Lemma 31.2(b).
- **Not read:** NPE5–NPE10, NER, and the current editions of NCI and NHJ.
  - `16_` audited NCI and RSS in full, and NHJ0–NHJ3 in full; NHJ4–NHJ9 only through their displayed results.
  - No earlier note of this branch audited NPE or NER. The phrase "NPE/NER (in part)" in `28_` §5.1 was wrong; `28_` is corrected in its revision section.
- **Checks:** `checks/njs_ssr_audit_checks.py`, 8 items, all pass.
  - Items 3 and 6 first failed because of my test design: absolute thresholds were swamped by the Gaussian factor e^{tρ²} ≈ e^{−60} at ρ₁. The tests now divide by that factor.

**Verdict.** NJS and SSR are correct as far as I checked, and so is the part of RSR that I read. I found no error.

## 1. What NJS proves

**The setting.**
- E = ℬ + ℂh_t is the meromorphic extension of the strip space ℬ, with h_t = 8g_tF₀/s and g_t = e^{ts²}. It carries the cover U_nf = n^{1−s}f.
- NJS compares the programme's residue section h_t with the uncorrected one, j_t = g_t/s.

**The comparison.**
1. **Shear.** The two sections differ by k_t = g_t(1 − 8F₀)/s ∈ ℬ, so E = ℬ ⊕ ℂh_t = ℬ ⊕ ℂj_t.
   - The coordinate change is an explicit shear, F_j = F_h − ck_t, and on the dual β = α + Λ(k_t) (NJS1).
   - k_t(0) = −8F₀′(0) = −(½log 4π − 1 − γ/2) ≈ 0.023096 (item 1).
2. **Discrepancies.** The two cover discrepancies are δ_n = nh_t − U_nh_t = 8g_tF₀(n − n^{1−s})/s ∈ I and η_n = nj_t − U_nj_t = g_t(n − n^{1−s})/s ∈ ℬ.
   - They satisfy δ_n = 8F₀η_n and η_n − δ_n = (n − U_n)k_t.
   - Both obey the cocycle law η_{mn} = mη_n + U_nη_m, and both have the value n log n at s = 0 (item 2).
3. **Neither section is equivariant in E.** A correction F ∈ ℬ would need (U_n − n)F = η_n. The left side vanishes at 0 and the right side has value n log n there (NJS2, SSR3). I verified this argument by hand.
4. **Density.** The closed span of the η_n is all of ℬ (NJS3–NJS4).
   - This is RSS1.2, audited in `16_`, and it is the case Φ ≡ 1 of `30_` Lemma 30.2. The proof is the same Jensen argument.
   - The closed span of the δ_n is the full zero-jet ideal I (NJS4.4, by NCI2). The squares n = k² already suffice (NJS4.5), a special case of register S33.
5. **In the quotient.** E/I ≅ Q ⊕ ℂ equivariantly, through the class [h_t] (NJS5, SSR3).
   - This equivariant section is unique, because n^{1−s} − n is a unit at every nontrivial zero (0 < Re ρ < 1).
   - [j_t] is not equivariant, since η_n(ρ) = g_t(ρ)(n − n^{1−ρ})/ρ ≠ 0 (item 3).
6. **Existence of a nontrivial zero.** NJS proves one exists by a short argument that I checked:
   - If F₀ = ξ/4 had no zero, Hadamard's factorization would give F₀ = e^{a+bs}.
   - The symmetry F₀(s) = F₀(1 − s) then forces b = 0, so F₀ would be constant.
   - But F₀(0) = 1/8 and F₀(2) = π/24 differ, since π ≠ 3 (item 4).
7. **Receivers (NJS6–NJS9).**
   - The corrected Hardy observations differ by the pole ℋ^j = ℋ^h + \overline{Λ(k_t)}/(1 − z).
   - The full meromorphic receiver 𝓜_t is unchanged by the shear.
   - The block sums telescope to η_n (item 5).
   - The largest cover-invariant subspace of the new zero-coordinate slice is {0}, while in the old coordinates it is σ_h(I^⊥).
   - The two Hardy domains agree exactly on the kernel of evaluation at k_t.

**SSR** re-derives items 1, 2, 3 and 5, and the receiver identities of item 7 (SSR5–SSR6).
- It does not treat the density statements of item 4.
- It does not treat the invariant-slice and Hardy-domain statements of item 7 (NJS7–NJS8.2).
- SSR7 adds that the shear formulas hold for any two residue sections differing by a fixed k ∈ ℬ.

**RSR7** proves an exact criterion for a polynomial P with P(0) = 1: I ⊂ Pℬ iff every root of P is an actual nontrivial zero, taken with order at most its multiplicity. I checked the proof: I ⊂ Pℬ forces P | F₀, and the converse is division by P. Item 8 checks an instance at ρ₁.

## 2. Lemmas extracted

**Lemma 31.1 (an infinite set of degrees need not suffice; the companion to register S33).** Fix t > 0 and an integer a ≥ 2. Let S ⊂ {a^k : k ≥ 1} ∪ F with F finite. Then span{η_{n,t} : n ∈ S} is not dense in ℬ. The same holds after multiplying by ξ: that span is not dense in I.

*Proof.*
1. Put s_j = 2πij/log a for j ≥ 1. For n = a^k, n^{−s_j} = e^{−2πijk} = 1. So η_{n,t}(s_j) = g_t(s_j)·n(1 − n^{−s_j})/s_j = 0.
2. Take |F| + 1 of these points. Some nonzero combination Λ of the evaluations there kills η_n for every n ∈ F: that is |F| linear conditions on |F| + 1 coefficients.
3. Λ kills every η_{a^k} by step 1.
4. Λ is a nonzero continuous functional on ℬ, because distinct point evaluations are linearly independent on ℬ.
5. **In I.** For the family δ_n = 8F₀η_n, choose instead a nonzero combination Λ′ of the same evaluations that kills δ_n for n ∈ F. Again this is |F| linear conditions on |F| + 1 coefficients.
   - Λ′ kills every δ_{a^k} by step 1.
   - Λ′ is nonzero on I. I contains g_tF₀P for every polynomial P, and Λ′(g_tF₀P) = Σ c′_j g_t(s_j)F₀(s_j)P(s_j). By interpolation this is nonzero for a suitable P, because g_t(s_j) ≠ 0 and F₀(s_j) = ξ(s_j)/4 ≠ 0.
   - For the last point: ξ(s_j) = ξ(1 − s_j) with Re(1 − s_j) = 1, where ζ has no zeros and the Gamma factor none either. ∎

*Scope.*
- Register S33 (`16_`) proves density when #{n ∈ S : log n ≤ R}/R² is unbounded; the squares are an example.
- The lemma shows that being infinite is not enough. S = {a^k} ∪ F has only about R/log a elements with log n ≤ R.
- It does not show that density depends on the counting function alone.
- For S = {2^a3^b}, which has about R²/(2 log 2 log 3) elements with log n ≤ R (quadratic growth), the Jensen argument is inconclusive.
- For S = {2^a3^b}, no finite combination of point evaluations and their derivatives annihilates the family. Here is why:
  - For such a Λ, Λ(η_n)/n is an exponential polynomial in (a, b) ∈ ℕ², with exponentials (2^{−s_i})^a(3^{−s_i})^b.
  - These pairs are distinct for distinct s_i, and equal (1, 1) only at s_i = 0.
  - Uniqueness of exponential-polynomial representations on a translate of ℕ² forces every polynomial coefficient to vanish, and then every c_{i,r} = 0.
  - At s_i = 0 this uses the fact that η_n^{(r)}(0) is n times a polynomial in log n of degree exactly r + 1.
  - I leave general functionals open.
- Item 6 checks the lemma for a = 2, 3 and 10. The same evaluation does not kill η_{a+1}.

**Lemma 31.2 (the residue extension survives evaluation only at the pole s = 0, where it becomes the Jordan block of ETR10).** Part (b) is NPE4.2 (see *Attribution* below). Consider the cover-equivariant extension 0 → ℬ → E → ℂ_χ → 0, where the cover acts on the residue line by χ(n) = n. For s₀ ∈ ℂ, push it out along evaluation ev_{s₀} : ℬ → ℂ, on which the cover acts by n^{1−s₀}.

- (a) If s₀ ≠ 0, the pushout splits.
- (b) If s₀ = 0, the pushout is the two-dimensional representation n ↦ n(I − log n·N) with N² = 0 and N ≠ 0. This is non-split, and its class in Ext¹(ℂ_χ, ℂ_χ) = Hom((ℕ_{≥1}, ×), (ℂ, +)) is −log.
- (c) The pushout is intrinsic to E. It does not depend on the residue section (h_t or j_t) or on t.
- (d) By ETR10 (`29_`, Negative result 29.N3), its tensor Euler functions are those of the split sum ℂ_χ ⊕ ℂ_χ, namely ℒ_d = ζ(s − d)^{2^d} for every d. So no Euler product of tensor powers detects it.

*Proof.*
1. **(a) At s₀ ≠ 0.** Every element of E is regular at s₀, since h_t has its only pole at 0. So ev_{s₀} extends to all of E, and the extension is cover-equivariant: ev_{s₀}(U_nf) = n^{1−s₀}f(s₀) for every f ∈ E. An equivariant extension of the pushout map splits the pushout.
   - Concretely, the cocycle value δ_n(s₀) = (n − n^{1−s₀})h_t(s₀) is the coboundary of the constant h_t(s₀) (item 7).
2. **(b) At s₀ = 0.** The kernel of ev₀ is cover-invariant, since (U_nF)(0) = nF(0). So the pushout is E/ker ev₀. It has the basis e = [F] with F(0) = 1, and [h_t].
   - U_ne = ne.
   - U_n[h_t] = n[h_t] − [δ_n] = n[h_t] − δ_n(0)e = n[h_t] − n log n·e.
   - So the matrix of U_n is n(I − log n·N) with N[h_t] = e.
   - It is multiplicative because log(mn) = log m + log n (item 7).
   - An equivariant splitting would be a value v for [h_t] with nv − n log n = nv for all n. This is impossible, since log 2 ≠ 0.
3. **The Ext group.** For a commutative monoid acting through characters χ and ψ, an extension of ℂ_χ by ℂ_ψ has a cocycle c with c(mn) = ψ(m)c(n) + c(m)χ(n).
   - If χ(n₀) ≠ ψ(n₀) for some n₀, commutativity gives c(m) = b(χ(m) − ψ(m)) with b = c(n₀)/(χ(n₀) − ψ(n₀)). So c is a coboundary.
   - If χ = ψ, then c/χ is additive and the coboundaries vanish.
   - Hence Ext¹(ℂ_χ, ℂ_χ) = Hom((ℕ_{≥1}, ×), ℂ), and the class in (b) is −log.
4. **(c)** The value of either discrepancy at 0 is n log n (NJS2), and the pushout is a quotient of E itself.
5. **(d)** is ETR10.4 with ω = 1. ∎

*Reading.*
- Among all evaluations of the programme's residue extension, the extension survives exactly at the pole s = 0 of h_t. There it is the logarithm n ↦ log n.
- At every other point, including every nontrivial zero ρ, it splits.
- Everywhere it is invisible to scalar Euler data.
- This places ETR10's abstract Jordan extension, which scalar Euler data do not detect, at a definite point of the programme's source: the pole at 0 of h_t = 8g_tF₀/s.

*Attribution.*
- Part (b) is NPE4. NPE4.1–4.2 define j(f) = (a₀, res₀f) from the Laurent expansion at 0 and prove j(U_nf) = n(I − (log n)N)j(f) with N² = 0.
- NPE4 also observes that the trace 2n and the determinant n² do not detect the nilpotent part.
- The same formula appears as the counting action n^{1−s}exp(−(log n)N) on logarithmic jet classes in HBW4.5 and HBW5.1 (`32_`).
- What this lemma adds:
  - (a), splitting at every s₀ ≠ 0;
  - the identification Ext¹(ℂ_χ, ℂ_χ) = Hom((ℕ_{≥1}, ×), ℂ), with class −log;
  - (c);
  - (d), the link to ETR10.

## 3. Negative results (goal 1)

- **31.N1. The section, not the covers, supplies the divisor (NJS10, confirming `16_`).** The two residue sections define the same non-split extension; their cocycles differ by an explicit coboundary. Yet the closed spans of the cocycle values are
  - I for h_t, the programme's ξ-section,
  - ℬ for j_t, the uncorrected section.
  - So "the closed span of the cover discrepancies", and the largest invariant subspace of a zero-coordinate slice, are not invariants of the extension.
  - The zeta divisor enters only through the factor 8F₀ in the chosen section. The residue character and the covers alone do not produce it.
  - This sharpens `16_`'s negative result 'cover invariance cannot locate zeros': even the ideal I is recovered only through the section.

- **31.N2. The only non-split residue data after evaluation is the logarithm at s = 0, and Euler products cannot see it (Lemma 31.2 with ETR10).**
  - A proposal that tries to detect the programme's residue extension through Euler products of tensor powers fails for every d.
  - A proposal that tries to detect it through evaluation at zeros fails because the extension splits there.

## 4. Bridges (goal 2)

- **`29_` (ETR10) ↔ NPE/NJS.** Lemma 31.2 identifies the abstract Jordan extension J = ℂ[ε]/(ε²), with exponent ω = 1, as the pushout of the programme's residue extension at the pole s = 0.
- **`30_` Lemma 30.2 ↔ NJS3.** They are one density statement; the correction term Φ is 1 for j_t and 8F₀ for ABH's ψ_j.
- **`16_` (RSS, NCI; register S33) ↔ NJS4.5 and Lemma 31.1.**
  - The squares suffice, as NJS4.5 shows and as a special case of S33.
  - Single-base powers never suffice, even with finitely many other degrees added (Lemma 31.1).
  - Superquadratic counting suffices (S33). For quadratic growth, as with {2^a3^b}, the question is open here.

## 5. Not checked

- NPE, NER, NCI and NHJ in their current editions (see §0).
- RSR1–RSR5 in the current edition; `16_` audited RSS itself.
- The Hardy-domain statements NJS8.2–8.3. I read their proofs, which use the non-square-summability of the constant sequence and the bounded cover; I did not test them numerically.

## 6. Check list (`checks/njs_ssr_audit_checks.py`)

| item | content |
|---|---|
| 1 | NJS1.2: k_t(0) = −8F₀′(0) |
| 2 | NJS2.1–2.3: values at 0, the coboundary, the cocycle law |
| 3 | NJS5.5 / SSR3.5 at ρ₁ and ρ₂ |
| 4 | NJS5: F₀(0) ≠ F₀(2) (elementary) |
| 5 | NJS6.3 and NJS6.5b |
| 6 | Lemma 31.1 |
| 7 | Lemma 31.2 / NPE4.2: Laurent data of U_nf by contour integrals; splitting at s₀ ≠ 0 (an identity) |
| 8 | RSR7: an instance at ρ₁ (elementary) |

## Revision after the tenth referee pass (applied at 14:20 UTC)

- **Major.**
  - Lemma 31.2(b) is NPE4.2. The referee located this from the bulletin entry on NPE's "evaluation pushout", and I confirmed it by reading NPE0–NPE4. The lemma now credits NPE4 and states what it adds.
  - §0 wrongly said that NPE/NER had been audited in part and NHJ in full in `16_`. Corrected; the same error in `28_` §5.1 is corrected there.
  - §1 overstated what SSR re-derives. Corrected.
- **Minor.**
  - Lemma 31.1:
    - retitled ("an infinite set of degrees need not suffice");
    - extended to {a^k} ∪ F;
    - proof completed for the ideal (ξ(s_j) ≠ 0 on Re s = 0);
    - scope restated: {2^a3^b} grows quadratically, and density is not shown to depend on growth alone.
  - The reference to the owner and the quotation marks around a phrase not in ETR10 were removed.
  - Check 7 now computes the Laurent data of U_nf by contour integrals, a real test of NPE4.2. Checks 4 and 8 are labelled elementary. All 8 pass.
