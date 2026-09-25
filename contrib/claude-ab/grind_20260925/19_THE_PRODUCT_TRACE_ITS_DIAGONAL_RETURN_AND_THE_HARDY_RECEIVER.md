# The product trace, its diagonal return, the full arithmetic correspondence, and the Hardy receiver (FTD, PRS, DER, FSC, FEM, NHJ4–NHJ9)

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 08:45 UTC.

This is a content map of the remaining blocks of board task 5, each read in full:

- FTD0–FTD10 (`FINITE_TOPOLOGY_DUALIZING_COMPLEX.md`);
- PRS0–PRS9 (`ORIGINAL_RESIDUE_PRODUCT_SHEAF_PAIRING.md`);
- DER0–DER11 (`DIAGONAL_EXTRAORDINARY_RETURN.md`);
- FSC0–FSC6 (`DERIVED_RETURN_FULL_SOURCE_CORRESPONDENCE.md`);
- FEM0–FEM10 (`FULL_SOURCE_RETURN_EQUIVARIANCE_AND_MIXED_TENSOR_CLASS.md`);
- NHJ4–NHJ9 (`NOOR_FULL_DUAL_INJECTIVITY_AND_HILBERT_DOMAIN.md`). NHJ0–NHJ3 were mapped in `16_`.

With this note, task 5 is complete.

**The line of argument, in one paragraph.**
- The Connes–Consani base is a three-point space Y = {c₊, c₋, η}. On it, sheaf cohomology has only degrees 0 and 1, and its dualizing complex is concentrated at the generic point in degree −1 (FTD).
- So the residue pairing of the zeta quotient, which has target degree 2, cannot come from a degree-zero sheaf map on Y itself (FTD9). It comes from the product Y × Y (PRS).
- Returning the product trace along the diagonal needs the right adjoint RΔ^!. That adjoint equals Rq_* for an explicit map q : Y² → Y, and it keeps the trace with coefficient +1, whereas ordinary pullback loses a degree (DER).
- Carried back to the arithmetic source X = Spec ℤ ∪ {m₊, m₋}, no single-valued return map exists. A correspondence does exist, with an exact derived comparison (FSC). It transports every operator and every extension class faithfully (FEM).
- The paired characters always multiply to p, so the pair's weights always sum to 2. Nothing in this chain forces the individual weight 1 (DER10, FEM7).
- Separately, NHJ proves that the Gaussian-corrected Noor tests are dense in ℬ, so the Hardy receiver is injective on the whole dual. The only obstruction to cover-invariance of its Hilbert domain is an explicit boundary pole 1/(1−z).

## 1. FTD: the three-point base and its dualizing complex

- **Sheaves are diagrams (FTD1).** A sheaf on Y is a diagram V₊ → A ← V₋. The projectives P_x represent the stalks, and the injectives I_x(W) satisfy Hom(F, I_x(W)) = Hom(F_x, W).
- **Cohomology and its right adjoint (FTD2).**
  - RΓ(Y, F) = [V₊ ⊕ V₋ → A], with differential r₊ − r₋, in degrees 0 and 1.
  - The right adjoint is p^!W = [I_η(W) → I₊(W) ⊕ I₋(W)], with RHom(F, p^!W) = RHom(RΓ(F), W).
- **The dualizing complex (FTD3).** ω_Y = p^!k ≃ j_!k[1]. It lives at the generic point in degree −1; it is not the constant sheaf shifted by 2.
- **Duals (FTD4–FTD8).**
  - FTD4 gives the algebraic dual 𝔻F. It is injective termwise, and RΓ(𝔻F) = Hom(RΓ(F), k).
  - FTD5 gives the local supports, with an explicit contraction Ri_±^!𝔻F ≃ V_±*.
  - FTD7 gives the continuous dual. Its gap to the algebraic dual is computed as the discontinuity quotients Q*/Q′ and E*/E′.
  - FTD8.3 presents the ASD receiving target at sheaf level, with the character χ_dil(a) = a and the shift [−2].
- **No same-site lift (FTD9).** Hom_{D(Sh(Y))}(Ω_full, χ𝔻_cΩ_full[−2]) = 0, for degree reasons: the source sits in degree 0 and the target in degrees 1 and 2. The global residue map Ψ¹ = π′D_ζπ is nonzero, so it cannot be the global sections of such a sheaf map.

## 2. PRS: the pairing lives on the product

- **The residue pairing (PRS1).** B_ζ(b, c) = (1/2πi)(∫_{Re s=2} − ∫_{Re s=−1}) M₀b(s)M₀c(1−s)/ζ(s) ds.
  - It is jointly continuous. The bound uses |1/ζ(−1+it)| ≤ 4π²ζ(2)(1+|t|)^{−3/2} (GZR2); I checked this bound numerically, with the worst sampled ratio 0.444.
  - It vanishes when either argument lies in J, so it descends to D_ζ : Q → χ_dil Q′.
  - Two-sided nondegeneracy is GZR6. It does not make Q ⊗ Q → ℂ injective.
- **The product sheaf map (PRS2).** β_ζ : F⊠F → K = j_{(η,η)!}χ_dil ℂ, checked at all nine stalks.
- **Product Čech complex and trace (PRS3).**
  - RΓ(Y², K) = χℂ[−2].
  - H²(C) = (A⊗A)/(J⊗A + A⊗J) ≅ Q⊗Q.
  - The trace has coefficient +1.
- **Currying (PRS4).** Currying returns exactly Ψ¹ = π′D_ζπ.
- **Two supports (PRS5).** The matrix is [[D_ζ, −D_ζ], [−D_ζ, D_ζ]], and the radical is exactly the diagonal ΔQ.
- **Characters (PRS6, PRS8).**
  - B_ζ(T_ab, T_ac) = a·B_ζ(b, c): the target carries the character of the pole at 1.
  - For eigenvectors with T_ax = a^ρx and T_ay = a^σy, a nonzero pairing forces ρ + σ = 1.
  - This pairing is bilinear. It pairs ρ with 1 − ρ, not with ρ̄ or 1 − ρ̄. (This is the Lebesgue-type pairing of `17_` Proposition 17.4(d), not the Hermitian ½-centred pairing of `17_` §5.)

## 3. DER: the diagonal needs the right adjoint

- **The map q (DER1).**
  - q(c₊,c₊) = c₊, q(c₋,c₋) = c₋, and q = η at the other seven points of Y².
  - q is continuous, and Δ_* = q^{−1} stalkwise.
  - The diagonal of Y² is neither open nor closed.
- **The right adjoint (DER2).** RΔ^! = Rq_*, and RΓ(Y, Rq_*G) = RΓ(Y², G) for every bounded complex G.
- **The extraordinary return of the trace (DER3–DER5).**
  - RΔ^!K ≃ j_{η!}χ_dil k[−1], through an explicit injective complex T of length 3 and a strong deformation retract onto a two-term complex.
  - The counit preserves the global trace with coefficient +1: RΓ(Y, RΔ^!K) ≃ RΓ(Y², K) = χk[−2].
  - Ordinary pullback gives Δ^{−1}K = j_{η!}χk, a degree lower.
- **The comparison map vanishes (DER6).** The canonical comparison RΔ^!K → Δ^{−1}K is zero in the derived category, by an explicit homotopy.
- **The whole coefficient sheaf returned (DER7–DER8).** For E = F⊠F:
  - R¹q_*E has closed stalks (W_± ⊗ Q) ⊕ (Q ⊗ W_±) and generic stalk Q_Δ = (A⊗A)/(J⊗J).
  - H⁰(Y², E) = H⊗H, H¹(Y², E) = (H⊗Q) ⊕ (Q⊗H), and H²(Y², E) = Q⊗Q.
- **The residue morphism (DER9).** The returned morphism is the original B_ζ on Q⊗Q, with no new sign or factor.
- **Weights (DER10).**
  - T_p acts on Q_ρ by p^ρ Σ_j (log p)^j N_ρ^j/j!, and B_ζ(N_ρx, y) = −B_ζ(x, N_{1−ρ}y).
  - The paired characters therefore have weights 2Re ρ and 2(1 − Re ρ), which sum to 2.
  - In the programme's words, the return "does not prove either individual weight to be one".

## 4. FSC and FEM: back to the whole arithmetic source

- **No single-valued return (FSC2).**
  - Let X = Spec ℤ ∪ {m₊, m₋} and f : X → Y. There is no continuous q̃ : X² → X with f q̃ = q(f×f) and q̃Δ_X = id.
  - Proof: for every prime p, the closure of (p,p) contains (m₊,m₋). So q̃(m₊,m₋) lies in the intersection of the closures {p, m₊, m₋}, which is {m₊, m₋}. But f q̃(m₊,m₋) = q(c₊,c₋) = η forces a point of U.
- **The correspondence (FSC3–FSC6).**
  - 𝒵 = {(x,y,z) : f(z) = q(f(x), f(y))}, with projections a, b and the lifted diagonal x ↦ (x,x,x).
  - Every fibre of a is the whole Spec ℤ, except the two equal-corner fibres, which are single points.
  - The derived comparison Ra_*b^{−1}f^{−1}G ≅ (f×f)^{−1}Δ_*G is proved through injective resolutions. It uses the facts that every nonempty open contains the generic point and that point-direct-images are injective.
- **Faithful transport (FEM1–FEM3).**
  - FEM verifies FSC6 independently.
  - It constructs a continuous section i : Y → X (η ↦ the generic point, c_± ↦ m_±), with (i×i)Δ a left inverse of v = q(f×f). So derived morphisms and extension classes are transported faithfully.
  - All real and prime dilations and the chart mirror are transported. The mirror carries B_ζ to its companion: B_ζ(Rx, Ry) = −B_{ζ∨}(x, y), where ζ∨(s) = ζ(1−s).
- **No finite characters in the tensor row (FEM4–FEM5).**
  - A contains no nonzero finite-dimensional subspace invariant under L_A = −u d/du. An eigenfunction would be c·u^{−λ}, which lies in A only if c = 0. The same holds for each prime operator T_p.
  - Hence Q_Δ has no finite-character vectors, and q(L_tot) is injective on it for every polynomial q ≠ 0.
- **The connecting classes (FEM6–FEM8).**
  - The connecting map δ_q : ker q|_{Q⊗Q} → M/qM is injective and equivariant, with an exact mirror relation carrying a sign (−1)^r.
  - At primary blocks ρ, σ the explicit representative (FEM7.4) keeps every binomial coefficient.
  - For σ = 1 − ρ the class has character p, of weight 2, "regardless of whether either zero is on the critical line. Thus these classes can be nonzero even when RH holds. They are not counterexamples to RH." (FEM7)
  - In the full global complex the explicit section S kills these classes: q(L_tot)e = d_G S(m). The global complex is quasi-isomorphic to K₀[0] ⊕ (Q⊗Q)[−1] (FEM8, GMC).

## 5. NHJ4–NHJ9: the Hardy receiver of Noor's tests

Notation from `16_`: F_{t,m} = g_tψ_m, where ψ_m = (m^{1−s} − (m+1)^{1−s} + 8F₀)/s for m ≥ 1, ψ₀ = (−1 + 8F₀)/s, and g_t(s) = e^{ts²}.

1. **Injectivity on the whole dual (NHJ4).** Suppose Λ ∈ ℬ′ annihilates all F_{t,m}.
   - The Jensen step of NHJ3 gives Λ(e^{us²}F) = 0 for u > t, using the half-Mellin integral.
   - Holomorphy in u on Re u > 0 extends this to the whole half-plane.
   - Letting u ↓ 0, with the strip estimate of GAP1, gives Λ(F) = 0.
   - So ker 𝓗_t = 0 on ℬ′, and the tests span ℬ densely (NHJ4.7). The same holds for any entire C of polynomial strip growth with C(0) = 1 in place of 8F₀, and for complex t with Re t > 0.
2. **The quotients (NHJ5).** The receiver is injective on Q′ and on the specialization dual ℛ′. The jet coefficients keep all Leibniz terms.
3. **The maximal Hilbert domain (NHJ6).** 𝔇_t = {Λ : Σ_m |Λ(F_{t,m})|² < ∞}. The receiver has closed graph and zero kernel on it, and B_t(λ, μ) = ⟨C_tμ, C_tλ⟩ is a positive form with zero radical.
4. **The boundary pole (NHJ7).**
   - The telescoping identity is Σ_{a<n} F_{t,nm+a} − U_nF_{t,m} = δ_{n,t} = 8g_tF₀(n − n^{1−s})/s. It gives W_n*𝓗Λ − 𝓗U_n′Λ = conj Λ(δ_{n,t})/(1 − z).
   - Since 1/(1−z) ∉ H², the covers preserve the Hilbert domain exactly when Λ(δ_{n,t}) = 0.
   - On the zeta quotients: C_tU_n′ = W_n*C_t, W_n*W_n = nI, W_nW_n* = nP_n, and the defect is nB_t(λ,μ) − B_t(U_n′λ, U_n′μ) = n⟨(I−P_n)C_tμ, (I−P_n)C_tλ⟩ ≥ 0 on the diagonal.
5. **Noor's regularity, pulled back (NHJ8).**
   - The finite-jet graph is closable and injective.
   - Noor's theorem pulls back to: no nonzero source vector in the closed finite-jet domain has its image in dom(((I−S)^{−1})*).
   - The explicit arithmetic test for that regularity (NAD) is recorded.
6. **What remains open (NHJ9, the programme's).** The programme does not prove that ℛ′ has finite Hardy norm, that NHJ7.6 vanishes, or that B_t is the Weil or residue pairing.

## 6. Relation to `17_` and `18_`

- DER10 and FEM7 are the programme's own statement of the point made in `17_` §6. The pairing of ρ with its partner 1 − ρ always has total weight 2, "regardless of whether either zero is on the critical line". Pair cancellation therefore holds for every zero and cannot locate one.
- PRS8 pairs ρ with 1 − ρ bilinearly, with the character a of the pole at 1. The Hermitian ½-centred Weil pairing of `17_` §5 pairs ρ with 1 − ρ̄. The two differ by complex conjugation, and only the Hermitian one carries a positivity criterion.
- FEM5's lemma, that A has no finite-dimensional dilation-invariant subspace because u^{−λ} ∉ A, is the precise form of the observation in `17_` §4: the characters on the critical line and on its mirror are generalized eigenvectors, never vectors of the space. Eigenvalues appear only in the quotient Q.

## 7. Checks

`checks/der_fsc_fem_ftd_prs_nhj_checks.py`, output in `checks/der_fsc_fem_ftd_prs_nhj_checks_OUTPUT.txt`.

| item | test | result |
|---|---|---|
| DER4.2 | d¹d⁰ = 0; rank d¹ = 3; ker d¹ = span(1,−1,1,−1); the corner sum annihilates im d¹ | exact (sympy) |
| DER4.5–4.7 | chain maps ι, π; πι = id; dh + hd = id − ιπ in degrees 1 and 2; h¹d⁰ = id | exact, with ev = id at the generic level |
| DER6.2–6.3 | target differential squares to 0; c = dh + hd | exact |
| PRS3.1 | the total product Čech differential squares to 0 (random integer d) | 0 |
| FSC2 | finite model U = {o, 2, 3, 5}: closure(p) = {p, m₊, m₋}; intersection over p is {m₊, m₋}; (m₊, m₋) ∈ closure(p,p) | confirmed |
| NHJ7.2 | telescoping discrepancy = 8g_tF₀(n − n^{1−s})/s, 27 cases (three s, n ∈ {2,3,7}, m ∈ {0,1,4}) | ≤ 6·10⁻²³ |
| NHJ7.5 | W_n*W_n = nI, W_nW_n* = nP_n, P_n² = P_n (n = 2, 3, 5; 60 coefficients) | exact |
| PRS1.5 | \|1/ζ(−1+it)\| ≤ 4π²ζ(2)(1+\|t\|)^{−3/2} for 244 sampled t ∈ [0, 1000] | worst ratio 0.444 |

The remaining steps were read for correctness without re-derivation: the long homological arguments (FTD2.6, FTD7.3, FSC6, FEM1.3, FEM8.4, DER7–DER9), and the Hahn–Banach and graph-closure steps (NHJ6, NHJ8).

## 8. Items for the goals

- **Negative results (goal 1).**
  - The residue pairing cannot come from a degree-zero sheaf map on the three-point base (FTD9).
  - No single-valued return map fixes the arithmetic diagonal (FSC2).
  - Ordinary diagonal pullback loses the trace's degree, and its comparison with the right adjoint is zero (DER6).
  - The reflected-pair classes have weight 2 whether or not RH holds, and the global boundary kills them (FEM7–FEM8).
  - Each is a precise statement about the specified spaces and maps; none bears on where the zeros are.
- **Bridges (goal 2).**
  - The right-adjoint dualizing complex of the Connes–Consani base (j_!k[1]) is the finite-topology analogue of Verdier duality. PRS8 and DER10 are the Poincaré-duality shape "weights w and 2 − w pair to the weight-2 class", which is also the shape of `17_` Proposition 17.4(d).
  - NHJ connects the programme's source to Noor's Hardy-space Nyman–Beurling criterion (arXiv:1809.09577) with an exact boundary-pole defect.
- **Lemmas (goal 3).**
  1. On a topological space in which every nonempty open contains a fixed generic point, the constant sheaf with value V equals the point direct image of V. In the algebraic category it is injective (FSC6, FEM1).
  2. The space A of functions on (0,∞) with rapid decay at both ends, with all u∂_u-derivatives, has no nonzero finite-dimensional subspace invariant under u d/du or under any single dilation T_p (FEM5).
  3. The Hardy telescoping identity NHJ7.2 and the exact domain criterion NHJ7.4.
  - Status: proved in the programme and checked as above. Novelty not searched.

## 9. Board task 5: status

Complete. Content maps:
- `12_`: OZD, SPF, GSP, CTS, FGR, WHR, HCS, GMC;
- `14_`: VWR, ATG;
- `15_`: PMS;
- `16_`: NCI, RSS, NHJ0–NHJ3;
- `18_`: SMC, GAP, ADM;
- `19_`: FTD, PRS, DER, FSC, FEM, NHJ4–NHJ9.

Blocks cited but not read in full: AST, ECI, ECR, GSL/GMS, GZR, OMS, DCP, CGS, RPD and SSI. GMC was mapped in `12_`, and FEM10 verifies it again.
