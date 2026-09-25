# CGS4–CGS10 and DCP4–DCP12: the source-space gluing and the doubled Connes–Consani pullback are correct, the doubling adds no cohomology, and nothing constrains where the zeros are

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 19:42 UTC. Board task 8: the rest of CGS and DCP (`26_` read CGS0–CGS3 and DCP0–DCP3). The first pass was an audit by one subagent (83 checks); §0 says what I verified myself. Refereed in the sixteenth pass (report completed at 20:26 UTC) and revised at 20:36 UTC; §7 lists the changes.

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

  Cohomology is computed with the Roos complex, supported cohomology with its subcomplex, Ext with the bar complex; 83 checks, 10 of them controls (nine reject a wrong sign or normalization, and one, N4, a failed hypothesis), all pass. My re-run at 19:41 UTC reproduces the output exactly. The Mellin items run twice: once with zeros on Re s = ½ (Z = (s² − s + 5/4)², zeros ½ ± i) and once with zeros off it (Z = (s² − s + 4/25)², real zeros 1/5 and 4/5; the sixteenth referee found that a model with the non-real off-line quadruple 3/10 ± i, 7/10 ± i gives the same dimensions and ranks).
- **Verified myself:** Lemma 39.3 (DCP5.1–5.3 for every Ω and with supports), by the derivation below; the reading of the appendices (§3), with GEX's own statement of its limitation; the four negative results of §4.
- **Checks.** `checks/cgs_dcp_rest_checks.py`: the subagent's script, 83 items, unchanged apart from the header.

**Verdict.**
- **No errors.** Every numbered item of CGS4–CGS10 and DCP4–DCP12 is a standard construction carried out correctly, signs included: recollement on a space whose extra point has the whole space as its only neighbourhood, pullback along a map to a three-point space, and Čech and supported cohomology of a two-chart cover.
- **Four minor points**, none affecting a result:
  - DCP11.3 calls s(q) = ½(q, −q) *the* equivariant section; it is one of an affine family, the unique one commuting with the reflection (check D24).
  - CGS's fibre convention makes its boundary map the negative of the snake-lemma boundary. It is used uniformly (check C10).
  - The chain map representing the derived restriction is left implicit (CGS5.3, CGS6.4).
  - Some vanishing ranges are not stated (§1).
- **DCP transcribes Connes–Consani accurately.** DCP's H¹ is their H¹(P¹_{𝔽₁}, Ω), the spectral realization of the zeros, in the trivial finite-unit sector for ℚ. (Their Theorem 5.5; Connes–Consani identify it with the realization of Meyer, Duke Math. J. 127 (2005), and of Connes–Consani–Marcolli and Connes–Marcolli, "initiated in" Connes, Selecta Math. 5 (1999). Like Meyer's, it contains every nontrivial zero with its multiplicity, whereas Connes (1999) realizes the critical zeros as an absorption spectrum.)
- **Nothing constrains the location of the zeros** (§4): every construction is uniform in the zero set, which enters only as the spectrum of the dilations on H¹.

## 1. What CGS4–CGS10 prove

The setting: X = U ∪ {𝔪} with U = Spec ℤ and X the only open neighbourhood of 𝔪, and the ring sheaf ℛ with its idempotent ε. CGS1 (audited in `26_`) classifies ℛ-modules by gluing data (𝒢, A₊, A₋, r: A₊ → Γ(U, 𝒢)).
- **CGS4.** Each module ℳ is an extension 0 → j_!𝒢 → ℳ → i_*(A₊ ⊕ A₋) → 0, pulled back from 0 → j_!𝒢 → j_*𝒢 → i_*Γ(U, 𝒢) → 0 along r. Ext¹(i_*A, j_!𝒢) ≅ Hom(εA, Γ(U, 𝒢)), with Baer sum r₁ + r₂; the extension splits iff r = 0 (checks C1–C6).
- **CGS5–CGS6.** H^q(X, ℳ) = 0 for q ≥ 1. Supported cohomology at 𝔪: H⁰ = A₋ ⊕ ker r, H¹ = coker r, H^q = H^{q−1}(U, 𝒢) for q ≥ 2; for complexes, RΓ_𝔪 ≅ A₋^• ⊕ Fib(A₊^• → RΓ(U, 𝒢^•)) (checks C7–C17). The degree-n sequence of CGS6.7 need not split over ℤ (check C17, with 0 → ℤ → ℤ → ℤ/2 → 0).
  - *Unstated ranges.* For a single sheaf ℳ and U = Spec ℤ, H^q_𝔪 = 0 for q ≥ 3 (Grothendieck's vanishing theorem, dim U = 1), and for q ≥ 2 when 𝒢 is quasi-coherent (Serre). H²_𝔪 ≠ 0 can occur: for 𝒢 = (j_V)_!𝒪_V with V = Spec ℤ ∖ {(2)}, H²_𝔪(X, j_!𝒢) = H¹(U, 𝒢) = ℤ_(2)/ℤ ≠ 0 (the sixteenth referee's example; check N2 is the finite-model analogue).
- **CGS7–CGS8.** The "selected residue" functor is ℳ ↦ A₋, exact. RHom(i_*A, j_!𝒢) ≅ RHom(εA, RΓ(U, 𝒢))[−1]; boundaries are equivariant for commuting actions (checks C18–C19).
- **CGS9.** For ℛ itself the gluing class of 0 → j_!𝒪 → ℛ → i_*ℤ² → 0 is the identity (non-split), and 0 → i_*ℤ → ℛ → j_*𝒪 → 0 splits (checks C20–C21, with partial fractions over ℤ).
- **CGS10.** The classification is Deligne's recollement as recalled in Weil II (3.4.8), p. 209. No RH or purity claim is made.

## 2. What DCP4–DCP12 prove, and Lemma 39.3

The programme proves the comparison for its Ω in DCP5.1–5.3: there Ω ≅ f_*f^{−1}Ω and R^q f_*f^{−1}Ω = 0, so Rf_*𝒩 ≃ Ω and RΓ(X^dbl, 𝒩) ≃ RΓ(Y, Ω), and the global cohomology is carried by the base Y. DCP9 and DCP12 add that the faithful extension leaves H¹ = Q unchanged. Lemma 39.3 records that DCP5's proof uses nothing about Ω, and adds the supported form.

**Lemma 39.3 (the doubled source adds no cohomology; DCP5 for every Ω).**
- **Setting.** X^dbl = U ∪ {𝔪₊, 𝔪₋} with U = Spec ℤ, where X± = U ∪ {𝔪±} is the smallest open neighbourhood of 𝔪± (the only one inside X±). Connes–Consani's base Y = {x₊, η, x₋} has the opens ∅, {η}, Y± = {x±, η} (their U±) and Y. The map f sends 𝔪± to x± and U to η.
- **Statement.** For every sheaf of abelian groups Ω on Y:
  - f_*f^{−1}Ω = Ω and R^q f_* f^{−1}Ω = 0 for q > 0;
  - hence RΓ(X^dbl, f^{−1}Ω) ≅ RΓ(Y, Ω) and RΓ_{𝔪±}(X^dbl, f^{−1}Ω) ≅ RΓ_{x±}(Y, Ω).
- **Proof.**
  - The preimages of the opens of Y are ∅, U, X± and X^dbl. On U, f^{−1}Ω is the constant sheaf with value Ω_η; U is irreducible, so this sheaf is flabby, its sections over U are Ω_η = Ω({η}), and its higher cohomology vanishes. X± is the minimal open of 𝔪±, so sections over it are the stalk at 𝔪±, which is Ω_{x±} = Ω(Y±).
  - A cover of X^dbl contains X^dbl or both charts, which meet in U. So f^{−1}Ω(X^dbl) = Ω(Y₊) ×_{Ω_η} Ω(Y₋) = Ω(Y), and f_*f^{−1}Ω = Ω. The stalks of R^q f_* are H^q of these local pieces, which vanish for q > 0.
  - The Leray spectral sequence, and its supported version with Γ_{f^{−1}Z}(X^dbl, −) = Γ_Z(Y, f_* −), give the rest. ∎ (Checks D3–D5, E1 on random Ω.)
- **Consequence.** DCP's H* and supported H* are exactly Connes–Consani's. The faithful scalar extension of DCP8 only adds flabby summands supported at 𝔪±. They change only the degree-0 groups, H⁰ and the supported H⁰ (DCP9.1–9.3), and add k±_*V± to f_* (DCP9.4); every group of degree ≥ 1 is unchanged (checks D15–D18).

**The rest of DCP.**
- **DCP4–DCP6.** The pullback 𝒩 = f^{−1}Ω_CC is computed on every open (the presheaf pullback is already a sheaf, check D3). The Čech complex [V₊ ⊕ V₋ → A] with d = r₊ − r₋ is CC's (87), with the same sign. H⁰ is the graph of the Fourier transform plus the endpoint lines (CC Lemma 5.3), and H¹ = Q, the zeta quotient, given the closed-range theorem imported from SSI (`25_`).
- **DCP7.** The supported complexes and their maps to the Čech complex, with the orientation sign (plus for the plus support, minus for the minus support; checks D8–D11 with controls). The boundary V₋ → H¹_{𝔪₊} vanishes because of the Fourier lift, that is, Poisson summation. This is step (97)–(98) of Connes–Consani's proof of their Theorem 5.5: H⁰(P¹_{𝔽₁}, Ω) → H⁰(U₋, Ω) is onto by Lemma 5.3, so H¹_Y ≅ H¹ for Y = {0}, which corresponds to 𝔪₊. The other two steps of that proof, H¹_Y = coker Σ and the symmetry from the action of C_K ⋊ W, correspond to DCP6.3 (with SSI) and to DCP11.
- **DCP10–DCP11.** The dilations and the idèle action (CC (93)), the mirror (CC (95)–(96)), and jets j_ρ at zeros ρ with j_ρT_a = a^ρ exp(log a·N) j_ρ (checks D19–D24 and Z1–Z5; D21 at 40 digits, Z1–Z5 at 25). The "endpoint weights" 0, 2, 2, 0 are labels fixed by the normalization of the dilations, not results.
- **DCP12.** A summary; no RH or purity claim.

## 3. The three appendices

The appendices summarize results that are proved in other files of the same folder at the same commit 36a82ec: GAP, GER, GEX and CTF (appendix 1); ASD, GZR and JTB (appendix 2); PGD, PGC, SCL and DPL (appendix 3). This audit did not read those files in full; GZR is audited in `26_`. I checked the statements cited below (GEX1–GEX3, GEX7, the last paragraph of GEX9, SCL5–SCL7 and PGD4) against the files. Their checkable cores are correct:
- **Appendix 1** ("global adelic lifting propagation") reports GEX: every Ext group between the zeta quotient Q and the adelic endpoint groups B^{[r]} = Λ^r W_pr ⊗ ℂ² (GEX3.1) vanishes. On these groups the dilation generator acts by L_B = id ⊗ diag(0, 1) (GEX3.2). The vanishing holds over any operator algebra in which L(L − 1) is central (GEX7), and for strict topological Yoneda extensions (GEX8). The core is GEX2: L(L − 1) is invertible on Q = ℬ/I, where L is multiplication by s and I is the ideal of functions in ℬ that vanish to full order at every nontrivial zero (GEX1.2).
  - *Proof (GEX2; re-derived by the first pass and checked here).* Let ξ(s) = ½s(s − 1)π^{−s/2}Γ(s/2)ζ(s). Then F_* = ξ/4 lies in I (GEX2.1), and F_*(0) = F_*(1) = ξ(0)/4 = 1/8 ≠ 0 (GEX2.2).
    - For λ ∈ {0, 1} and G ∈ ℬ, the function G − (G(λ)/F_*(λ))F_* vanishes at λ and is divisible by s − λ in ℬ. So L − λ is onto Q. GEX2.3 makes the same correction at both endpoints at once.
    - If (s − λ)F ∈ I, then F ∈ I, because λ is not a nontrivial zero. So L − λ is injective on Q.
    - L(L − 1) acts invertibly on Q and by zero on every B^{[r]} (GEX3.3), so all Ext groups vanish (GEX7: on each Ext group this element acts both invertibly and by zero). Over ℂ[L] alone the computation is explicit. The resolution 0 → ℂ[L] ⊗ M → ℂ[L] ⊗ M → M → 0 makes Ext^n(M, N) the cohomology of φ ↦ L_Nφ − φL_M on Hom_ℂ(M, N), and zero for n ≥ 2. On the λ-eigenspace B_λ of L_B this map is φ ↦ −φ(L_Q − λ) on Hom(Q, B_λ) and φ ↦ (L_Q − λ)φ on Hom(B_λ, Q), both bijective.
  - This uses only ξ(0) ≠ 0 and ξ(1) ≠ 0, i.e. ζ(0) ≠ 0 and the pole of ζ at 1. GEX9 says so itself: its central separation excludes only the endpoint parameters 0 and 1, and "does not prove Re ρ = 1/2". DCP's appendix adds that full τ numerical purity "does not follow from endpoint separation". Check N4 shows that the finite-model analogue fails when the model polynomial vanishes at 0 and 1.
- **Appendix 2** ("supported duality and original-zeta trace"): the residue pairing with 1/ζ (GZR) is correct (`26_` Lemma 26.1). The passage to Weil's explicit-formula form and the chain map ASD14 are proved in JTB and ASD, which this audit did not read. The statement that weak-* density is not algebraic surjectivity is correct.
- **Appendix 3** ("finite lifting and a nonzero remainder"):
  - The class c_ζ in the algebraic cokernel of Q → Q′ is nonzero (PGD4). If it were zero, some F ∈ ℬ would satisfy F(ρ) = 1 at every nontrivial zero ρ (PGD4.4). But F decays in the strip |Re s| ≤ 2 (the seminorm b_{2,1}(F) is finite), and PGD4 proves from the Hadamard product of F_* that the zero heights are unbounded.
  - The invertibility of every nonzero polynomial in the cokernel generator is proved in SCL5–SCL6 and DPL. This audit read SCL5–SCL7 and did not read DPL. The generator is the operator 𝖳 induced by L^t on the algebraic cokernel, not a vector; the χ-twisted action has infinitesimal operator 1 − 𝖳, to which the same applies (SCL6). SCL5.2 proves that 𝖳 − a is bijective for every a ∈ ℂ. Given that, the lifting of finite-dimensional invariant subspaces follows formally (SCL7).

## 4. Negative results (goal 1)

- **39.N1. The doubling adds no cohomology** (DCP5.3, DCP9.1 and DCP12 state it; Lemma 39.3 gives it for every Ω and with supports). This is the programme's own statement. For the register it means that DCP's H¹ is exactly Connes–Consani's H¹(P¹_{𝔽₁}, Ω) in the trivial finite-unit sector for ℚ, the spectral realization of the zeros, and nothing more; the faithful extension adds only flabby summands.
- **39.N2. Nothing in CGS4–CGS10 or DCP4–DCP12 constrains where the zeros are.**
  - Every construction is functorial in the linear data (the chart spaces, the restriction maps, the reflection, the Fourier transform and the dilations), and every proof is uniform in the zero set.
  - The zeros enter in two places only. The first is the imported identification Q = A/J ≅ ℬ/I, where they are the spectrum of the dilation generator on H¹ (the spectral realization). The second is the jets, which need only that J lies in the kernel of each jet.
  - The two finite models have their zeros on Re s = ½ and off it. In both, all cohomology and supported groups have the same dimensions, and all ranks, signs, section families and gluing-class ranks agree (checks N1, N5; D2–D24 in both). Only the spectrum of L on H¹ differs. In each model the characteristic polynomial of L on H¹ is the model polynomial Z itself, so the weights 2Re ρ of the dilations on H¹ are {1} for Z = (s² − s + 5/4)² (roots ½ ± i) and {2/5, 8/5} for Z = (s² − s + 4/25)² (roots 1/5 and 4/5, since 1/5 + 4/5 = 1 and (1/5)(4/5) = 4/25).
- **39.N3. DCP's "lift" is not a weight argument.**
  - In Weil II §3.6 (Théorème 3.6.1, the local invariant cycle theorem, p. 213; proof on pp. 213–214), Deligne combines two exact sequences into the cross (8). One is 0 → H^{i−1}(X_η̄)_I(−1) → H^i(X_η) → H^i(X_η̄)^I → 0; the other is the supported sequence H^i(X) → H^i(X_η) → H^{i+1}_{X_s}(X), with H^{i+1}_{X_s}(X) ≅ H^{2N−i−1}(X_s)^∨(−N).
    - Lemma 3.6.2 gives H^i(X_η̄)^I weights ≤ i, and Lemma 3.6.3 gives the supported group weights ≥ i + 1.
    - After the exact functor W_i is applied, the boundary into the supported group vanishes on W_iH^i(X_η), which maps onto H^i(X_η̄)^I; the theorem follows.
    - The boundary need not vanish on all of H^i(X_η). Already for X = S (so N = 1) and i = 1: proper base change for the identity, as in Deligne's (7), gives H*(S) ≅ H*(s), which is zero in degrees ≥ 1 because k is algebraically closed. The supported sequence then makes the boundary H¹(η) → H²_s(S) an isomorphism, and H¹(η) = H¹(I, ℚ_ℓ) ≅ ℚ_ℓ(−1) ≠ 0 by Deligne's (3)–(4). This group has weight 2 = i + 1.
  - In DCP7.2 the corresponding boundary V₋ = H⁰(X₋) → H¹_{𝔪₊} vanishes on all of V₋. The reason is the Fourier lift, i.e. Poisson summation, and it vanishes in both finite models.
  - The analogue of Deligne's weight separation would be a statement about the weights 2Re ρ on H¹_{𝔪₊} = Q, which is RH-type information. No such statement is made or available. On the Schwartz part the dilations have continuous spectrum, so a numerical weight separation cannot even be formulated there.
  - DCP12 says the same: the comparison with Weil II §3.6 "has not been assumed", and DCP1–DCP12 provide the objects "to which a further numerical weight argument would have to apply".
- **39.N4. The Ext-vanishing of Appendix 1 sees only ζ(0) ≠ 0 and the pole at 1** (§3; GEX2 and GEX7, and GEX9, where the programme says so itself). It says nothing about the nontrivial zeros.
  - This holds in GEX's categories, which contain the generator L.
  - Over the dilation group alone, T_a − a^λ (a > 0, a ≠ 1) is multiplication by a^s − a^λ, which vanishes exactly on λ + (2πi/log a)ℤ. If (a^s − a^λ)F ∈ I and no nontrivial zero lies on that set, F vanishes to full order at every zero, so F ∈ I. The zeros on that set have real part λ ∈ {0, 1}. So this injectivity argument already uses ζ(1 + it) ≠ 0 at t ∈ (2π/log a)ℤ, t ≠ 0 (for λ = 0 through the functional equation). That is the nonvanishing of ζ on Re s = 1 (J. Hadamard, Bull. Soc. Math. France 24 (1896); C. de la Vallée Poussin, Ann. Soc. Sci. Bruxelles 20 (1896)), not only ζ(0) ≠ 0 and the pole.

## 5. Bridges (goal 2)

- **DCP = Connes–Consani §5** in the trivial finite-unit sector for ℚ (established item by item; the comparison of cohomology is DCP5.3, in general form Lemma 39.3).
- **DCP ↔ SSI** (`25_`): H¹(X^dbl, 𝒩) = Q ≅ ℬ/I, with the dilations acting as multiplication by a^s.
- **DCP ↔ GZR** (`26_` Lemma 26.1): the residue pairing B_ζ is nondegenerate on H¹, scales by a under the dilations, and the mirror sends it to its transpose; no symmetry or positivity follows.
- **CGS = recollement** (Weil II (3.4.8)).
- **No bridge to Weil II §3.6** (39.N3), and **none from the source monoid to the zeros**: the only place where τ and 1 act differently is an extra flabby summand, which appears neither in H¹ nor in any boundary.

## 6. Not checked

- The files behind the appendices (GAP, GER, GEX, CTF, ASD, JTB, PGD, PGC, SCL, DPL), apart from the statements cited in §3 (GEX1–GEX3, GEX7, the last paragraph of GEX9, SCL5–SCL7 and PGD4).
- The closed-range theorem of SSI, which DCP6.3 imports (audited in `25_`).
- Connes–Consani's text beyond the spot checks listed in §0.

## 7. Revision after the sixteenth referee pass

An independent referee pass (report completed at 20:26 UTC; 53 check items, 38 PASS and 15 FAIL, all 15 marked as expected and each documenting a finding) confirmed the verdict "no errors" for CGS4–CGS10 and DCP4–DCP12. It rebuilt the finite models independently, re-ran the script (83/83, output byte-identical) and read the printed Weil II pp. 209–215. It found three major points and nine minor ones, all about this note rather than the programme. I accepted all of them and checked the programme passages involved myself (GEX1–GEX3, GEX7, GEX9, SCL5–SCL7, PGD4, DCP5, DCP9.1, DCP12, and the OCR of Weil II pp. 212–215).
- **M1 (credit).** DCP5.1–5.3, inside the audited range, prove that the doubled source adds no cohomology for the programme's Ω; DCP9.1 and DCP12 add that the faithful extension leaves H¹ = Q unchanged. §2 now says so before Lemma 39.3, which records the same proof for every Ω and with supports, and 39.N1 cites DCP5.3, DCP9.1 and DCP12.
- **M2 (the appendix files).** The earlier statement that the files behind the appendices "were not provided" was false: all eleven are in the cited folder at 36a82ec. §3 now names them, credits the algebraic core of appendix 1 to GEX2 and GEX7 and its limitation to GEX9, removes a reference to an unpublished working file, and replaces "asserted" by "proved in files this audit did not read".
- **M3 ("depends" is false).** H¹ is the spectral realization of the zeros, so the spectrum of the dilations on H¹ does depend on where they are; in the two finite models the characteristic polynomial of L on H¹ is the model polynomial. The title, the file name (formerly `…_SEES_NO_ZERO_LOCATION.md`), the verdict and 39.N2 now say that nothing constrains where the zeros are.
- **Minor points.**
  - m1: DCP7.2 is step (97)–(98) of Connes–Consani's proof of their Theorem 5.5, not the whole proof (§2).
  - m2: the account of Weil II §3.6 in 39.N3 now follows pp. 213–214 (the cross (8), Lemmas 3.6.2–3.6.3, the exact functor W_i); the boundary vanishes on W_iH^i(X_η), not on all of H^i(X_η). 39.N3 also cites DCP12's own disclaimer.
  - m3: the attribution of the spectral realization (Meyer 2005; Connes 1999 realizes the critical zeros as an absorption spectrum).
  - m4: the setting of Lemma 39.3 (X± is the smallest open neighbourhood of 𝔪±; Y± instead of U±) and the gluing step of its proof.
  - m5: the extra flabby summands also change the supported H⁰ and add k±_*V± to f_*.
  - m6: an example with H²_𝔪 ≠ 0 on Spec ℤ itself; check N2 is only its finite-model analogue.
  - m7: the count of controls, the number of negative results, "pullback along a map to", and the precision of D21 and Z1–Z5.
  - m8: the off-line model has real zeros, which ζ cannot have in (0, 1) (ζ(σ) < 0 there); a model with a non-real off-line quadruple gives the same dimensions and ranks.
  - m9: the "cokernel generator" is the operator 𝖳 induced by L^t, not a vector. `26_` line 97 said that DPL calls c_ζ a cokernel generator; DPL does not mention c_ζ, and `26_` is corrected (register, list of corrections).
- **Added in the revision.** The explicit Ext computation over ℂ[L] in §3, the elementary example after Weil II (8) in 39.N3, and the remark in 39.N4 that over the dilation group alone the injectivity argument uses ζ(1 + it) ≠ 0.
