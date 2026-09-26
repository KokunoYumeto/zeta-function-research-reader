# BML, BRC, GJN and BNS: the winding inverse, ramification, the norm shift and the return domains

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 15:04 UTC. Board task 8: the last three of the eight new result groups of the 25 September bulletin (BML/BMR/BMRL, BRC/BRR, GJN/GJNR), together with BNS. First passes by two subagents (14:22–14:59 UTC); §0 says what I verified myself. Refereed in the eleventh pass; the changes are listed at the end of this note.

## 0. Sources, method and checks

All files are in `quantum_tau_programme_bridge_20260924/next_edition_after_719`. SHA-256 is given after conversion of CRLF to LF; the recorded hashes are those of the reviews.

| file | block | SHA-256 (LF) | recorded by |
|---|---|---|---|
| `FULL_BOUNDARY_MONODROMY_DIFFERENCE_LIFT.md` | BML0–BML11 | `667d718f…ea16397f` | BMR13 |
| `FULL_BOUNDARY_MONODROMY_DIFFERENCE_LIFT_REVIEW.md` | BMR0–BMR13 | `99ab89ed…00722417` | — |
| `BOUNDARY_LIFT_LOCAL_COUNTING_INDEPENDENT_REVIEW.md` | BMRL0–BMRL6 | `10c27cc6…e10352f7` | BMR12 |
| `BOUNDARY_RAMIFICATION_AND_COUNTING_COMPARISON.md` | BRC0–BRC11 | `c66c2d06…d2ccb532` | BRR9, GJNR0 |
| `BOUNDARY_RAMIFICATION_ROOT_REVIEW.md` | BRR0–BRR9 | `5ba31ce8…49d30ca2` | — |
| `GLOBAL_JET_RAMIFICATION_NORM_SHIFT.md` | GJN0–GJN8 | `1bc0db07…82f7b113` | GJNR10 |
| `GJN_INDEPENDENT_REVIEW.md` | GJNR0–GJNR10 | `367cc665…3178c668` | — |
| `BOUNDARY_NORM_SHIFT_INDEPENDENT_CHECK.md` | BNS0–BNS7 | `38bea808…22a2f85e` | GJNR0 (the hash of the CRLF bytes, `802c0345…974f29ad`) |
| `PEER_EULER_AND_RAMIFICATION_INTAKE_REVIEW.md` | PER0–PER5 | `a84a2882…1ec404f1` | — |

**Hash bookkeeping.** Several reviews record earlier editions of the files they review, so those hashes cannot be verified here:
- BRR0 (BRC);
- BMR0 and BMRL0 (BML0–BML9);
- BMRL0 (HBWR);
- GJNR0 (GJN at `39feafa3…` and `6439295b…`);
- PER0 (GJN and GJNR at `75d13c70…`, ETR at `8428cf7d…`).

The receipts `PEER_EULER_RAMIFICATION_INTAKE_RECEIPT.json` and `HBWR_TYPOGRAPHY_CORRECTION.json` were not staged.

**Method.**
- Subagent A read BML, BMR and BMRL in full. It wrote 18 checks, copied here as `checks/bml_audit_checks.py`.
- Subagent B read BRC, BRR, GJN, GJNR, BNS and PER2–PER3 in full. It wrote 21 checks, copied here as `checks/brc_gjn_bns_audit_checks.py`. The source path of its informational hash lines is now an environment variable.
- My re-runs at 15:01–15:02 UTC give 18/18 and 21/21 PASS.
- The first runs had six failures, all from test design and none mathematical: cancellation with zero tolerance, tests made vacuous by d_r(ρ₁) = 0, float overflow, too-strict thresholds, and insufficient precision.
- I verified myself:
  - the invertibility bound and the near-projection form of the inverse (Lemma 33.1);
  - the composition law and the norm shift (Lemma 33.3);
  - the escape argument for the return domains (Lemma 33.4);
  - the collision criterion;
  - the truncation artifact in BML11 (33.N3).
- Everything else in §§1–2 is the subagents' audits, supported by their checks.
- PER is the programme's own review of GJN and ETR.
  - All three prose corrections it reports are present in the delivered texts.
  - Its PER5 classifies the fibres of the scalar Euler observation by Jordan partitions. This extends ETR10 and agrees with `29_` 29.N3.

**Verdict.** No mathematical error was found in BML, BMR, BMRL, BRC, BRR, GJN, GJNR or BNS. All the findings are structural (§§3–4).

## 1. BML (with BMR and BMRL): the winding difference and its inverse

**Setting.**
- The receiver of HBW writes the boundary image of y ∈ H_O as a singular germ Σ m_ρ a_ρ(y)(e^u − 1)u^{−1−ρ}, plus a holomorphic remainder, on the universal cover of a punctured disk.
- Continuation around the puncture (M) multiplies the ρ-term by λ_ρ = e^{−2πiρ}.
- BML inverts M − I on the space 𝒟 of such classes, builds a contraction and the lift of the specialization obstruction, and compares it with the original nearby monodromy (BML8).

**Verification.**
- BML1 = HBW8.7–8.9; the kernel statement is `32_` Lemma 32.2.
- BML2: λ_ρ has the correct sign. The opposite sign e^{+2πiρ} fails the jump test with relative error 1.
- BML3: the Gaussian stage maps G₂₁ and V_{k;t,t′} are exact.
- BML4–BML6: (M − I)𝒷 = 𝒷(M − I) = I and dh + hd = I; the whole-function equation (M − I)[f(By) + L·R(y)] = f(y) holds pointwise (checks C05–C06).
- BML7: the counting comparison holds with all three signs; flipping the log n term fails (C07–C11).
- BML10: the maximal closed winding operator on each fixed stage, normal, with an explicit graph-norm inverse bound (C12).
- BML11: the logarithmic enlargement 𝒱 = 𝒟 ⊕ ι(𝒪(D_{2π})) (C13, C16).

**What the reviews add.** BMR and BMRL correct nothing. They re-derive BML, supply BML10–11, and make the cover explicit (Ω = {Re v < log 2π}). Their constants are valid but loose:
- |Γ(1+ρ)| ≤ Γ(1+σ) ≤ 1, not merely ≤ 2;
- |d_r| < r − 1, not merely ≤ r + 1.

## 2. BRC, GJN and BNS (with BRR, GJNR and PER): ramification and the norm shift

**Setting.**
- In the cover coordinate w = log u, the three operators are pullbacks along affine maps:
  - ramification P_a along w ↦ aw;
  - counting C_b along w ↦ w − log b;
  - monodromy M along w ↦ w + 2πi.
- Each is conjugated by the unit h(u) = (e^u − 1)/u.
- On the singular classes, P_a sends the exponent ρ to aρ, C_b multiplies by b^ρ, and M by e^{−2πiρ}.

**Verification.**
- BRC1–BRC4.
  - P_mP_n = P_{mn} and M^kP_n = P_nM^{nk} (C04).
  - The counting comparison (C06).
  - The union-divisor isolators G_n = F₀(s)F₀(s/n), with G_n(0) = 1/64 (C19). This is `32_` Lemma 32.2 with G = G_n.
- BRC5–BRC11.
  - The one-step return domain, iterated return, the enlargement with its collision kernel, higher jets, the monodromy inverse on the enlargement, and the reflected return (C20–C21).
  - Typography: BRC5.2 contains ":;&", and BRC7.5 is printed after BRC7.8.
- GJN0–GJN8.
  - The integer ramification closure Σ_a P_aE and the tagged collision kernel: dim ker Π = Σ(fibre − 1) (C13–C14).
  - The scaled lowering: Π N̂ = NΠ; the unscaled lowering fails (C13).
  - The norm shift N P_b = b P_b N (C12).
  - The composition law T_{a,b}T_{c,d} = T_{ac, b^c d}. The forms b·d^a and b·d fail (C05).
  - The monodromy inverse (C17) and the return criterion (C15).
- GJNR adds:
  - tagged counting before the quotient (GJNR4);
  - the cokernel of P_a, ⊕_λ span{H̄_{λ,j} : d_{λ/a} ≤ j < d_λ}, which is nonzero for a ≥ 2 (GJNR6; C14);
  - the iterated-return filtration E_{a,L} = ⊕ span{j < min_{0≤k≤L} m_{a^kρ}}, whose intersection over L is 0 (GJNR7; C15).
  - GJNR1 corrects GJN's multiplier sentence.
- BNS re-derives the norm shift and the counting defect.
  - BNS1 extends HBW3's independence argument to all nonreal exponents.
  - BNS2.2 is ETR10's defect (1 − b^{−1})C_bN, of rank d − 1, up to N ↦ −N (C16).

## 3. Lemmas extracted

**Lemma 33.1 (the winding at the zeros is hyperbolic, and its inverse is almost a projection).** For every nontrivial zero ρ = σ + iγ, let λ_ρ = e^{−2πiρ} and b_ρ = 1/(λ_ρ − 1).
- |λ_ρ| = e^{2πγ}, and λ_ρ is a negative real number iff σ = ½.
- |b_ρ + 1_{γ<0}| ≤ 1/(e^{2π|γ|} − 1) ≤ 1/(e^{2πγ₁} − 1) < 2.7·10⁻³⁹, where γ₁ = 14.1347… is the smallest positive ordinate.
- So the inverse of the winding difference M − I is −P₋ + E, where P₋ is the coordinate projection onto zeros with γ < 0, and the error satisfies ‖E‖ < 2.7·10⁻³⁹.

*Proof.*
1. **Modulus and phase.** |e^{−2πi(σ+iγ)}| = e^{2πγ}, and arg λ_ρ = −2πσ. So λ_ρ < 0 iff σ ≡ ½ (mod 1), i.e. σ = ½ in the strip.
2. **γ > 0.** |b_ρ| ≤ 1/(e^{2πγ} − 1).
3. **γ < 0.** b_ρ + 1 = λ_ρ/(λ_ρ − 1), and |λ_ρ|/|1 − λ_ρ| ≤ e^{2πγ}/(1 − e^{2πγ}) = 1/(e^{2π|γ|} − 1).
4. **The constant.** No zero has |γ| < γ₁ = 14.1347…:
   - γ = 0 is excluded because ζ < 0 on (0, 1), as in ETR11 (`29_` §2);
   - 0 < γ ≤ 14 is excluded by the zero count N(14) = 0 (check C03 of `bml_audit_checks.py`);
   - γ < 0 follows by conjugation;
   - γ₁ = 14.134725… is the classical first ordinate, as tabulated in A. Odlyzko's tables of zeros of the Riemann zeta function.
   - Finally, e^{2πγ₁} = e^{88.81…} ≈ 3.7·10³⁸. ∎

BML2's constant C_B = max{(e^{2π} − 1)^{−1}, (1 − e^{−2π})^{−1}, …} is valid. The "finitely many zeros with |γ| ≤ 1" in its proof are none.

**Lemma 33.2 (the winding difference is onto on the universal cover; truncated logarithmic towers).** Let D* = {0 < |u| < R}, Ω = {Re v < log R} with u = e^v, and (Mf)(v) = f(v + 2πi) on 𝒪(Ω).
- (a) M − I is onto 𝒪(Ω), with kernel the functions pulled back from 𝒪(D*). This holds because H¹(D*, 𝒪) = 0 for the noncompact Riemann surface D* (O. Forster, *Lectures on Riemann Surfaces*, GTM 81, Chapter 3: the vanishing of H¹(X, 𝒪) for noncompact Riemann surfaces, and functions with prescribed summands of automorphy on the universal covering). Equivalently: every open subset of ℂ is Stein, and the Cartan–Leray comparison applies to the free ℤ-action on the Stein manifold Ω. The referee of the eleventh pass verified the argument.
  - Hence, in the germ quotient 𝒢 of BML, every class has a primitive. So BML5–6's existence of a lift carries no information about the obstruction; what BML supplies is an explicit continuous linear choice of lift.
- (b) Put L = log u/(2πi), so ML = L + 1, and let T_k(A) be the span of the classes of L^jA, 1 ≤ j ≤ k, for A holomorphic on the disk. On 𝒟 ⊕ T_k(A):
  - H⁰ = ι₁(A);
  - H¹ = ℂ·[L^kA], carried by the top level j = k;
  - for the full tower, H¹ = 0.
  - Indeed (M − I)[L^jA] = Σ_{i<j} C(j, i)[L^iA], and ι(A) = [LA] = (M − I)[(L² − L)A/2] as soon as L² is adjoined.
  - BML11.5, where H¹ ≅ ι(𝒪(D_{2π})), is the case k = 1 (C13, C16).

**Lemma 33.3 (the operator calculus is the calculus of affine maps of w = log u).** Let T_{a,b} = P_aC_b be pullback along φ_{a,b}(w) = aw − log b, conjugated by a fixed unit.
- T_{a,b}T_{c,d} = T_{ac, b^c d}, because φ_{c,d}∘φ_{a,b} = φ_{ac, b^c d}.
- M^kT_{a,b} = T_{a,b}M^{ak}, because φ_{a,b}(w + 2πik) = φ_{a,b}(w) + 2πiak.
- With N = (2πi)^{−1}log(q^{−1}M) on a generalized eigenspace of M with eigenvalue q: NP_b = bP_bN, NC_b = C_bN, and NT_{a,b} = aT_{a,b}N.
- The norm shift is the chain rule for w ↦ bw.
- N is the logarithm of the unipotent part of M on each generalized eigenspace. When exponents differ by integers, this means the whole generalized eigenspace.
  - This agrees with GJN4.1, which defines N on the exponent decomposition rather than by guessing an eigenvalue decomposition.
  - The programme computes the same logarithm in HBWR3.4 and BNS4.3, and PER5.1 does so for W_p.
- Every relation among P_a, C_b, M and N in BRC1, GJN4–GJN5 and BNS3–BNS4 reduces to these three lines. The global sheet sum BRC3.3 (= HSR7.2) and BNS3.5's change of basis are not of this kind.

**Lemma 33.4 (escape; the return domains).** Let Z be any set of points with 0 < Re ρ < 1, and let a ≥ 2.
- {k ≥ 0 : a^kρ ∈ Z} ⊂ {k : a^k Re ρ < 1}, which is finite.
- No nonempty S ⊂ Z satisfies aS ⊂ S.
- A point of Z can return to Z under ρ ↦ aρ only if Re ρ < 1/a.
  - Zeros on Re ρ = ½ never return for a ≥ 2.
- If Z = 1 − Z̄, then aρ and a(1 − ρ̄) are never both in Z, since Re ρ < 1/a and 1 − Re ρ < 1/a cannot both hold.
- The escape step of the theorems below is combinatorial and uses only 0 < Re ρ < 1, and for BRC11 the reflection ρ ↦ ρ#.
- The theorems concerned are:
  - the empty intersection of iterated returns (BRC6, the iterated part of GJN6, GJNR7.5);
  - the zero reflected return (BRC11).
- Their proofs also use:
  - nonreal points (BRC4 divides by e^{−2πiλ} − 1; GJN1.4);
  - discreteness with the weighted Gaussian bound (BRC2.5);
  - a generator in ℬ;
  - for BRC11, the reflection.
- Under these hypotheses they hold for every such Z.
- The one-step classification (BRC5, GJN6.3) is different: its content depends on the divisor (33.N4). ∎

**Collision criterion (for GJN3's kernel).** Two tagged exponents collide, aρ = a′ρ′ with ρ ≠ ρ′, only if ρ/ρ′ = a′/a ∈ ℚ_{>0}.
- For zeros on the critical line, (½ + iγ)/(½ + iγ′) is real only if γ = γ′.
- So under RH the collision kernels K and K_{r,n} are zero. (The subagent's check C13 includes a no-collision test among actual zeros, but it uses Re ρ = ½ as input, so it is only a sanity check.)

## 4. Negative results (goal 1)

- **33.N1. The vanishing of the receiver's monodromy cohomology adds no information about the obstruction.**
  - BML0 poses exactly this question: what does vanishing of the new receiver's monodromy cohomology say about the retained specialization obstruction 𝓡?
  - H⁰ and H¹ of M − I on 𝒟 vanish for every zero set that avoids the integers and has a positive distance from 1 in λ. For the vanishing itself, only ρ ∉ ℤ, inf|λ_ρ − 1| > 0 and 0 ≤ Re ρ ≤ 1 (for continuity) enter. Building 𝒟 needs more: the isolators and the Gaussian bounds.
  - Together with injectivity of j, the vanishing gives only that j is M-equivariant iff 𝓡 = 0 (33.N4).
  - BML5 and BML8 themselves state that the contraction coexists with the obstruction.
  - The critical line enters only through d_r(ρ) = 0 ⟺ Re ρ = ½, which decides which coordinates make up H_O.
  - BML8's comparison with the original nearby monodromy is a tautology here, because M − I is invertible. No map between the two punctures is constructed.
- **33.N2. The iterated-return and reflected-return theorems (BRC6, BRC11, the iterated part of GJN6, GJNR7.5) hold for every divisor in the open strip that satisfies the hypotheses listed in Lemma 33.4.** Their conclusions are therefore not evidence about zero locations. The one-step classification is excluded.
- **33.N3. BML11's H¹ is an artifact of truncating the logarithmic tower at L¹** (Lemma 33.2(b)). Its H⁰ = ι(𝒪) does not involve the zeros at all.
- **33.N4. Conditions equivalent to RH by construction, and conditions implied by RH.**
  - *By construction.* Each says H_O = 0:
    - 𝓡 = 0 (equivalently j, ℓ, 𝔈 or 𝒦 vanishes);
    - j is M-equivariant for the trivial action on 𝓡;
    - [𝒦y] ∈ 𝒟 for all y ∈ H_O. When RH fails, R(e_ρ)′(0) = −m d_r e^{t(1−ρ)²}ζ(−ρ)/(1 − ρ) ≠ 0 at an off-line ρ. Here ζ(−ρ) = χ(−ρ)ζ(1 + ρ), with ζ(1 + ρ) ≠ 0 since Re(1 + ρ) > 1, and χ(−ρ) = 2^{−ρ}π^{−ρ−1}sin(−πρ/2)Γ(1 + ρ) ≠ 0 since ρ is not an even integer (the value is checked numerically in C14);
    - the counting defect vanishes;
    - every λ_ρ is negative real (Lemma 33.1);
    - |b^ρ| = b^{1/2} on every block.
  - *Implied by RH, converse not shown:*
    - every one-step return domain is 0;
    - the collision kernels vanish;
    - coker P_a consists of full blocks at Λ ∖ aΛ.
- **33.N5. The norm-shift relation has no arithmetic content by itself.** For any nilpotent N and q ≠ 0, the solutions of NT = qTN are Γ·Z(N), where Z(N) is the centralizer of N and Γ is one fixed invertible solution.
  - Such a Γ exists: in a Jordan basis with Ne_k = e_{k+1} along each chain, take Γe_k = q^{−k}e_k. Then NΓe_k = q^{−k}e_{k+1} = qΓNe_k.
  - So invertible solutions always exist (elementary).
  - The ramification operators realize the relation by the chain rule (Lemma 33.3).

## 5. Bridges (goal 2)

- **The pole at s = 0 once more.** GJN5.2 at λ = 1, which is s = 0, with block length d = 2 has the same matrix as NPE4.2's n(I − log n·N) (`31_` Lemma 31.2(b), register S61); only the matrices coincide, since GJN's E and Ẽ exclude λ = 1.
  - That block lies outside GJN's E and Ẽ, whose exponents are nonreal.
  - BNS2.2/GJN5.3 is ETR10's defect up to N ↦ −N. By `29_` 29.N3, neither the norm shift nor the defect is visible to any tensor Euler product.
- **Kummer covers.** In the cover coordinate, ramification of degree e sends (monodromy, N) to (monodromy^e, eN). The programme's norm shift is this rule. Here I state only the chain-rule derivation of Lemma 33.3, not a comparison with any étale or Weil–Deligne statement.
- **One family of receivers.**
  - BRC4 is `32_` Lemma 32.2 with G = F₀(s)F₀(s/n).
  - BML1 is HBW8.
  - 𝒷 is HBWR3.3 with m = 1.
  - BRC3.3 is HSR7.2.
  - BNS5.3 = GJN7.5 = HBW0.4 combined with W_n*K_s = n^{1−s}K_s (ABH1.4).

## 6. Not checked

- ADC3 and ADC8.6: the file was not supplied, so the claims about identity nearby monodromy are taken as stated.
- The BNS7 figure, CEI §5, and the two receipts named in §0.
- The programme-vocabulary statements and the provenance claims.

## 7. Check lists

`checks/bml_audit_checks.py` (18 items):
- C01–C02: BML1.3–1.5 and the sign of λ_ρ.
- C03: BML2.2, and B + P₋ at the actual zeros.
- C04: BML3.
- C05–C06: BML4–6.
- C07–C11: BML7 and BMR8.
- C12: BML10.
- C13 and C16: BML11 and the truncation artifact.
- C14: ζ(−ρ) ≠ 0.
- C15: the phases at the zeros.
- C17: the integer slots.
- C18: BMR's constants.

`checks/brc_gjn_bns_audit_checks.py` (21 items):
- C01–C03: F₀ and the convergence bounds.
- C04–C05: the pullback calculus and the composition law.
- C06–C10: the counting, jet and ramification formulas at ρ₁.
- C11: independence.
- C12: the norm shift.
- C13–C15: the tagged kernel, the cokernel and the return filtration.
- C16–C17: the counting defect and the monodromy inverse.
- C18: χ(s) and GJN0.8.
- C19: G_n.
- C20–C21: BRC5, BRC6, BRC10 and BRC11 on a synthetic divisor with off-line zeros.

## Revision after the eleventh referee pass (applied at 15:34 UTC)

The referee re-ran both check scripts, whose outputs reproduced byte for byte, and verified Lemmas 33.1–33.4, the collision criterion and 33.N5, and more than 30 source statements. Applied to this note:

- **Major.** Lemma 33.3 misreported GJN4.1 as a "caution" contradicted by the determination of N by M. GJN4.1 only says that N is defined on the exponent decomposition; the programme itself computes N as a logarithm (HBWR3.4, BNS4.3, PER5.1). Corrected.
- **Minor.**
  - Lemma 33.1: the proof of γ₁ = 14.1347… is completed (γ = 0 excluded; the count covers only 0 < γ ≤ 14; conjugation) and a table is cited.
  - Lemma 33.2: a citation for (a) was added; H¹ = ℂ·[L^kA] in (b).
  - Lemma 33.3: the reduction is restricted to relations among P_a, C_b, M and N.
  - Lemma 33.4 and 33.N2: the hypotheses the proofs use are stated, and the one-step classification is excluded.
  - 33.N1 is reworded: the vanishing adds no information about 𝓡.
  - 33.N4: a one-line proof that ζ(−ρ) ≠ 0 was added.
  - The NPE4.2 bridge now says "has the same matrix as".
  - Hash bookkeeping was completed.
  - The unpublished mutation-probe claim and the reference to an unpublished lemma label were removed.
  - Two tests are relabelled as sanity checks.
