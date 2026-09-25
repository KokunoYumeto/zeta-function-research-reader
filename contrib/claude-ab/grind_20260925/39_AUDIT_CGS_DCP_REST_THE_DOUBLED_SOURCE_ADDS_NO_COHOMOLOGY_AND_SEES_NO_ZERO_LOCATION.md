# CGS4–CGS10 and DCP4–DCP12: the source-space gluing and the doubled Connes–Consani pullback are correct, the doubling adds no cohomology, and nothing depends on where the zeros are

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 19:42 UTC. Board task 8: the rest of CGS and DCP (`26_` read CGS0–CGS3 and DCP0–DCP3). The first pass was an audit by one subagent (83 checks); §0 says what I verified myself. Not yet refereed.

## 0. Source, method and checks

- **Sources.** In the reader repository, `workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/` (commit 36a82ec):
  - `SOURCE_COEFFICIENT_GLUE.md` (CGS), 441 lines. Audited here: CGS4–CGS10, lines 133–441.
  - `SOURCE_CC_DOUBLE_PULLBACK.md` (DCP), 522 lines. Audited here: DCP4–DCP12 and three dated appendices, lines 160–522.
- **External source.** A. Connes and C. Consani, *Schemes over 𝔽₁ and zeta functions*, arXiv:0903.2024v3, §5, which DCP cites as its human source. The first pass compared DCP with CC's text: the chart spaces and restriction maps (CC (83), (85)), the Čech differential (87) with its sign, Lemma 5.3, the idèle action (93), the Weyl involution (95)–(96), and Theorem 5.5. I spot-checked (87), Lemma 5.3, (93), (95)–(96) and the statement of Theorem 5.5 in the extracted text.
- **Method.** Everything in CGS and DCP is formal in its input data, so the first pass modelled it exactly on finite spaces:
  - the source X = Spec ℤ ∪ {𝔪} by a four-point space with the same specialization order;
  - the doubled source by a five-point space;
  - Connes–Consani's base by the three-point space {x₊, η, x₋};
  - their Mellin data by a finite algebra ℚ[s]/(Z·E) with the reflection s ↦ 1 − s.

  Cohomology is computed with the Roos complex, supported cohomology with its subcomplex, Ext with the bar complex; 83 checks, 10 of them controls that must reject a wrong sign or normalization, all pass. My re-run at 19:41 UTC reproduces the output exactly. The Mellin items run twice: once with zeros on Re s = ½ (Z = (s² − s + 5/4)², zeros ½ ± i) and once with zeros off it (Z = (s² − s + 4/25)², zeros 1/5 and 4/5).
- **Verified myself:** Lemma 39.3 (the doubling adds no cohomology), by the derivation below; the reading of the appendices (§3); the three negative results of §4.
- **Checks.** `checks/cgs_dcp_rest_checks.py`: the subagent's script, 83 items, unchanged apart from the header.

**Verdict.**
- **No errors.** Every numbered item of CGS4–CGS10 and DCP4–DCP12 is a standard construction carried out correctly, signs included: recollement on a space whose extra point has the whole space as its only neighbourhood, pullback to a three-point space, and Čech and supported cohomology of a two-chart cover.
- **Four minor points**, none affecting a result:
  - DCP11.3 calls s(q) = ½(q, −q) *the* equivariant section; it is one of an affine family, the unique one commuting with the reflection (check D24).
  - CGS's fibre convention makes its boundary map the negative of the snake-lemma boundary. It is used uniformly (check C10).
  - The chain map representing the derived restriction is left implicit (CGS5.3, CGS6.4).
  - Some vanishing ranges are not stated (§1).
- **DCP transcribes Connes–Consani accurately.** DCP's H¹ is their H¹(P¹_{𝔽₁}, Ω), the spectral realization of the zeros (their Theorem 5.5, after Connes 1999), in the trivial finite-unit sector for ℚ.
- **Nothing depends on the location of the zeros** (§4).

## 1. What CGS4–CGS10 prove

The setting: X = U ∪ {𝔪} with U = Spec ℤ and X the only open neighbourhood of 𝔪, and the ring sheaf ℛ with its idempotent ε. CGS1 (audited in `26_`) classifies ℛ-modules by gluing data (𝒢, A₊, A₋, r: A₊ → Γ(U, 𝒢)).
- **CGS4.** Each module ℳ is an extension 0 → j_!𝒢 → ℳ → i_*(A₊ ⊕ A₋) → 0, pulled back from 0 → j_!𝒢 → j_*𝒢 → i_*Γ(U, 𝒢) → 0 along r. Ext¹(i_*A, j_!𝒢) ≅ Hom(εA, Γ(U, 𝒢)), with Baer sum r₁ + r₂; the extension splits iff r = 0 (checks C1–C6).
- **CGS5–CGS6.** H^q(X, ℳ) = 0 for q ≥ 1. Supported cohomology at 𝔪: H⁰ = A₋ ⊕ ker r, H¹ = coker r, H^q = H^{q−1}(U, 𝒢) for q ≥ 2; for complexes, RΓ_𝔪 ≅ A₋^• ⊕ Fib(A₊^• → RΓ(U, 𝒢^•)) (checks C7–C17). The degree-n sequence of CGS6.7 need not split over ℤ (check C17, with 0 → ℤ → ℤ → ℤ/2 → 0).
  - *Unstated ranges.* For U = Spec ℤ, H^q_𝔪 = 0 for q ≥ 3, and for q ≥ 2 when 𝒢 is quasi-coherent; H²_𝔪 ≠ 0 can occur (check N2).
- **CGS7–CGS8.** The "selected residue" functor is ℳ ↦ A₋, exact. RHom(i_*A, j_!𝒢) ≅ RHom(εA, RΓ(U, 𝒢))[−1]; boundaries are equivariant for commuting actions (checks C18–C19).
- **CGS9.** For ℛ itself the gluing class of 0 → j_!𝒪 → ℛ → i_*ℤ² → 0 is the identity (non-split), and 0 → i_*ℤ → ℛ → j_*𝒪 → 0 splits (checks C20–C21, with partial fractions over ℤ).
- **CGS10.** The classification is Deligne's recollement as recalled in Weil II (3.4.8), p. 209. No RH or purity claim is made.

## 2. What DCP4–DCP12 prove, and Lemma 39.3

**Lemma 39.3 (the doubled source adds no cohomology).**
- **Setting.** X^dbl = U ∪ {𝔪₊, 𝔪₋}, with X± = U ∪ {𝔪±} the only open neighbourhood of 𝔪±. Connes–Consani's base Y = {x₊, η, x₋} has the opens ∅, {η}, U± = {x±, η} and Y. The map f sends 𝔪± to x± and U to η.
- **Statement.** For every sheaf of abelian groups Ω on Y:
  - f_*f^{−1}Ω = Ω and R^q f_* f^{−1}Ω = 0 for q > 0;
  - hence RΓ(X^dbl, f^{−1}Ω) ≅ RΓ(Y, Ω) and RΓ_{𝔪±}(X^dbl, f^{−1}Ω) ≅ RΓ_{x±}(Y, Ω).
- **Proof.**
  - The preimages of the opens of Y are ∅, U, X± and X^dbl. On U, f^{−1}Ω is the constant sheaf with value Ω_η; U is irreducible, so this sheaf is flabby, its sections over U are Ω_η = Ω({η}), and its higher cohomology vanishes. X± is the minimal open of 𝔪±, so sections over it are the stalk at 𝔪±, which is Ω_{x±} = Ω(U±).
  - So f_*f^{−1}Ω = Ω. The stalks of R^q f_* are H^q of these local pieces, which vanish for q > 0.
  - The Leray spectral sequence, and its supported version with Γ_{f^{−1}Z}(X^dbl, −) = Γ_Z(Y, f_* −), give the rest. ∎ (Checks D3–D5, E1 on random Ω.)
- **Consequence.** DCP's H* and supported H* are exactly Connes–Consani's. The faithful scalar extension of DCP8 only adds flabby summands supported at 𝔪±, which change H⁰ and nothing else (checks D15–D18).

**The rest of DCP.**
- **DCP4–DCP6.** The pullback 𝒩 = f^{−1}Ω_CC is computed on every open (the presheaf pullback is already a sheaf, check D3). The Čech complex [V₊ ⊕ V₋ → A] with d = r₊ − r₋ is CC's (87), with the same sign. H⁰ is the graph of the Fourier transform plus the endpoint lines (CC Lemma 5.3), and H¹ = Q, the zeta quotient, given the closed-range theorem imported from SSI (`25_`).
- **DCP7.** The supported complexes and their maps to the Čech complex, with the orientation sign (plus for the plus support, minus for the minus support; checks D8–D11 with controls). The boundary V₋ → H¹_{𝔪₊} vanishes because of the Fourier lift, that is, Poisson summation. This is Connes–Consani's own proof of their Theorem 5.5.
- **DCP10–DCP11.** The dilations and the idèle action (CC (93)), the mirror (CC (95)–(96)), and jets j_ρ at zeros ρ with j_ρT_a = a^ρ exp(log a·N) j_ρ (checks D19–D24, Z1–Z5, to 40 digits). The "endpoint weights" 0, 2, 2, 0 are labels fixed by the normalization of the dilations, not results.
- **DCP12.** A summary; no RH or purity claim.

## 3. The three appendices

The appendices summarize results in files that were not provided (GAP, GER, GEX, CTF, JTB, ASD, SCL, DPL). Their checkable cores are correct:
- **Appendix 1** ("global adelic lifting propagation") asserts that all Ext groups between the zeta quotient Q and the endpoint modules vanish. The algebraic core is: with L the dilation generator (multiplication by s on Q = ℬ/I), L − λ is invertible on Q for λ ∈ {0, 1}.
  - *Proof (first pass, Lemma 39.7; I checked it).* F_* = ξ/4 lies in I, with F_*(0) = F_*(1) = ξ(0)/4 = 1/8 ≠ 0. For G ∈ ℬ, G − (G(λ)/F_*(λ))F_* vanishes at λ and is divisible by s − λ in ℬ, so L − λ is onto Q. If (s − λ)F ∈ I then F ∈ I, because λ is not a zero, so L − λ is injective on Q. The Koszul resolution of ℂ_λ over ℂ[L] then gives Ext^i(Q, ℂ_λ) = Ext^i(ℂ_λ, Q) = 0.
  - This uses only ξ(0) ≠ 0 and ξ(1) ≠ 0, i.e. ζ(0) ≠ 0 and the pole of ζ at 1. Check N4 shows that it fails when the model polynomial vanishes at 0 and 1.
- **Appendix 2** ("supported duality and original-zeta trace"): the residue pairing with 1/ζ (GZR) is correct (`26_` Lemma 26.1). The passage to Weil's explicit-formula form (JTB) and the chain map ASD14 are asserted, not verifiable here. The statement that weak-* density is not algebraic surjectivity is correct.
- **Appendix 3** ("finite lifting and a nonzero remainder"):
  - The class c_ζ in the algebraic cokernel of Q → Q′ is nonzero. A lift F ∈ ℬ would satisfy F ≡ 1 to full order at every zero, but F decays on vertical strips while the zero heights are unbounded.
  - The invertibility of every nonzero polynomial in the cokernel generator (SCL, DPL) is asserted, not verified. Given it, the lifting of finite-dimensional invariant subspaces follows formally.

## 4. Negative results (goal 1)

- **39.N1. The doubling adds no cohomology** (Lemma 39.3). DCP's H¹ is exactly Connes–Consani's H¹(P¹_{𝔽₁}, Ω), the spectral realization of the zeros, and nothing more; the faithful extension adds only flabby summands.
- **39.N2. Nothing in CGS4–CGS10 or DCP4–DCP12 depends on where the zeros are.**
  - Every construction is functorial in the linear data (the chart spaces, the restriction maps, the reflection, the Fourier transform and the dilations). The zeros enter only through the imported identification Q = A/J ≅ ℬ/I and through the jets, which need only that J lies in the kernel of each jet.
  - In the two finite models, with zeros on Re s = ½ and with zeros off it, every cohomology group, supported group, rank, sign, section family and gluing-class rank is the same (checks N1, N5; D2–D24 in both).
- **39.N3. DCP's "lift" is not a weight argument.**
  - In Weil II §3.6 (the local invariant cycle theorem, pp. 213–214) a boundary into a supported group vanishes because weights separate: ≤ i on one side, ≥ i + 1 on the other.
  - In DCP7.2 the corresponding boundary vanishes by the Fourier lift, i.e. Poisson summation, and it does so in both finite models.
  - The analogue of Deligne's weight separation would be a statement about the weights 2Re ρ on H¹_{𝔪₊} = Q, which is RH-type information. No such statement is made or available, and on the Schwartz part the dilations have continuous spectrum, so a numerical weight separation cannot even be formulated there.
- **39.N4. The Ext-vanishing of Appendix 1 sees only ζ(0) ≠ 0 and the pole at 1** (§3). It says nothing about the nontrivial zeros.

## 5. Bridges (goal 2)

- **DCP = Connes–Consani §5** in the trivial finite-unit sector for ℚ (established, item by item; Lemma 39.3).
- **DCP ↔ SSI** (`25_`): H¹(X^dbl, 𝒩) = Q ≅ ℬ/I, with the dilations acting as multiplication by a^s.
- **DCP ↔ GZR** (`26_` Lemma 26.1): the residue pairing B_ζ is nondegenerate on H¹, scales by a under the dilations, and the mirror sends it to its transpose; no symmetry or positivity follows.
- **CGS = recollement** (Weil II (3.4.8)).
- **No bridge to Weil II §3.6** (39.N3), and **none from the source monoid to the zeros**: the only place where τ and 1 act differently is an extra flabby summand, which appears neither in H¹ nor in any boundary.

## 6. Not checked

- The files behind the appendices (GAP, GER, GEX, CTF, JTB, ASD, SCL, DPL).
- The closed-range theorem of SSI, which DCP6.3 imports (audited in `25_`).
- Connes–Consani's text beyond the spot checks listed in §0.
