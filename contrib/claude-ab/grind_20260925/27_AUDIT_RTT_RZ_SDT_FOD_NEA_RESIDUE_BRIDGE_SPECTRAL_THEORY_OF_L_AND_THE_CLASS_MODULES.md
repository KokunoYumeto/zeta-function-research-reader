# The residue bridge, the spectral theory of L, and the class modules: an audit of RTT, RZ, SDT, FOD and NEA

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 12:26 UTC. Board task 8, part 4: the remaining inputs of the chain audited in `24_`–`26_`.

**Sources.** All five blocks are in the zeta-function-research-reader repository at commit 064f33b, folder `…/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/`:
- RTT0–RTT11, `RESIDUE_TRACE_TRANSFER_INDEPENDENT.md`;
- RZ1–RZ12, `ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md`;
- SDT0–SDT9, `CC_STRONG_DUAL_TOPOLOGY_AND_JETS.md`;
- FOD0–FOD8, `CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md`;
- NEA0–NEA10, `CC_NORMAL_EXTENSION_ANNIHILATOR.md`.

**How this audit was done.**
- One subagent read all five blocks in full, between about 11:58 and 12:23 UTC. It re-derived the proofs step by step and wrote 47 numerical checks. The checks are copied, unchanged apart from a header, to `checks/rtt_rz_sdt_fod_nea_audit_checks.py`. I re-ran them at 12:26 UTC: 47/47 pass (`checks/rtt_rz_sdt_fod_nea_audit_checks_OUTPUT.txt`).
- I verified the following myself:
  - the equivalences of §2, with the proofs given there (the ninth referee pass checked them again);
  - the Fréchet–Schwartz property of B (Lemma 27.2, proof below);
  - the explicit-formula test. Its truncations are 25 zeros, n < 400, and |t| ≤ √(90/α) in the archimedean integral. The omitted zero and prime terms are below e^{−150}, and the archimedean tail is about 10⁻⁴⁰. The two sides agree to about 10⁻²⁶ at 25-digit precision (the ninth referee pass), well inside the tested tolerance 10⁻¹⁵.
  - RTT3, the residue lemma, and FOD2–FOD4, against the corresponding steps of GSL and GMS (`24_`).
- The blocks rest on further programme blocks that are not re-read here: GTR, RD, GIQ, GTAH, CDI, CSP, CLP and CW. §4 lists them.

## 0. Summary

1. **No errors were found in any of the five blocks.** The delicate signs and constants all hold:
   - the isolator coefficient m(−1)^{m−1}u_ρ(0);
   - the residue determinant u(0)^{−m};
   - the resolvent sign W(R_λx, y) = −W(x, R_{1−λ̄}y);
   - the sign conventions of the explicit formula.
2. **What the blocks are.** In plain terms, they are standard mathematics written in the programme's language:
   - RTT is the residue pairing plus Weil's explicit formula. RTT9.4 was re-derived and agrees numerically to better than 10⁻¹⁵ for three Gaussian tests.
   - RZ is the spectral theory of multiplication by s on B/I.
   - SDT is Fréchet–Montel duality.
   - FOD and NEA are elementary commutative and homological algebra on the class modules.
3. **Conditions that are RH (or simple zeros) by definition (§2).**
   - W ≥ 0 if and only if RH holds; W > 0 if and only if RH holds and all zeros are simple.
   - U_a = D_a^* for a single a ≠ 1 if and only if RH holds.
   - The trace image is dense if and only if all zeros are simple.
   - The residue bridge R̂(F, SG) = W(F, G) is Weil's explicit-formula functional, so its positivity is Weil's criterion.
4. **Two simplifications.**
   - B is itself a Fréchet–Schwartz space (Lemma 27.2). So SDT7 and RTT6 hold on B/I directly. SDT instead transfers them through κ: A/J ≅ B/I, which rests on the exact summation image.
   - RTT5's finite nets h_E(G) are exactly the truncations of PG to the blocks {1 − ρ : ρ ∈ E}.
5. **Lemmas extracted:** 27.1 (the spectral theory of multiplication by s on B/I_D), 27.2 (B is Fréchet–Schwartz), 27.3 (the local rank-one and residue lemmas), and 27.4 (the annihilator of a tautological extension).

## 1. Block-by-block verdicts

| Block | Main claims (plain terms) | Verdict |
|---|---|---|
| RTT | The value map E: Q → ℓ²(Z, m) is continuous with dense image. W(F,G) = ⟨EF, 𝖩EG⟩₊, and its radical is N₀ (classes vanishing at every zero). s²ζ′(1−s) is entire of polynomial growth, with value −1 at 0. P = L^{−2}M_{s²ζ′(1−s)}C has rank one on each block (RTT3). The residue pairing of F with PG is W(F,G) (RTT4). The strong closure of W(Q) is N₀^⊥ (RTT6). U_a = 𝖩D_a^*𝖩 (RTT8.3). RTT9.4 is Weil's explicit formula | verified; RTT5.1 is a definition, since H_res = Q′_β by construction |
| RZ | R_λF = (F − F₀F(λ)/F₀(λ))/(λ − s) inverts λ − L for λ ∉ Z (RZ3). Global isolators E_{ρ,j} (RZ5). The projectors P_ρ = [e_ρ·] have rank m_ρ, their ranges are ker(L−ρ)^{m_ρ}, there is one Jordan block per zero, and Spec L = Z (RZ6). Riesz formula (RZ7). T_n = n^ρ exp(log n·N_ρ) on each block, and n = 2, 3 already separate the zeros (RZ8). Reflection formulas (RZ9). Block structure and positivity equivalences of W (RZ10–11) | verified |
| SDT | A is Fréchet–Schwartz. Bounded sets of A and Q are relatively compact; compact sets lift through the quotient; Q′_β ≅ J^⊥. A, Q, J and Z are reflexive, and their strong duals complete. The jet functionals span a strongly dense subspace of the dual. Residue-matrix determinant u(0)^{−m} (SDT8.8) | verified; the density of the jet functionals needs no transfer through SSI (Lemma 27.2) |
| FOD | B/(I ∩ I₊) ≅ Q ⊕ Q₊ with inverse ([f],[g]) ↦ [cf + (1−c)g]. The pushout along h splits if and only if h extends M-linearly. Ann(e₀) = 𝔞 and Ann(e₊) = 𝔞₊. The joint class has annihilator 𝔞 ∩ 𝔞₊. The boundary module is Mδ ≅ M/𝔞₊, with cδ = 0, so δ∘f = 0 for every f from Q | verified; the derived-category part rests on GMS9 and CLP12 |
| NEA | Ann_M(e₊) = K₊ = Ann_M(Q₊), with an explicit continuous splitting after pushout. Hom_M(Q₊, I₊) = Hom_M(Q₊, B) = 0. The local probe reads the k-jet of h. Me₊ ≅ M/K₊. The spectrum and characters of λ on M/K₊ are the evaluations at ρ + 1, with log-moduli 2Re ρ + 2. RHom(Q, N₊) = RHom(N₊, Q) = 0 | verified; NEA3.4 duplicates FOD4.7, and NEA10 duplicates FOD7 |

## 2. Conditions that are RH, or simple zeros, by definition

Each item gives the condition, the block, and the proof.

1. **W ≥ 0 on Q if and only if RH holds. W is positive definite on Q if and only if RH holds and all zeros are simple (RZ11).**
   - *Proof.* On an off-line pair {ρ, ρ^#}, the block of W is [[0, m],[m, 0]], of signature (1, 1) (`25_` check 10). The global isolators realise every finite pattern of values, so an off-line pair gives a negative value. Under RH, W(F,F) = Σ m_ρ|F(ρ)|² ≥ 0. This is zero exactly when all values vanish, and that forces [F] = 0 exactly when all zeros are simple. Otherwise the isolator E_{ρ,1} is a nonzero class with W = 0.
2. **U_a = D_a^* for a single a > 0, a ≠ 1, if and only if RH holds (RTT8.3).**
   - *Proof.* On the coordinate ρ the multipliers are a^{1−ρ} and a^{ρ̄}. They agree exactly when (1 − 2Re ρ)log a ∈ 2πiℤ. The left side is real, so this means Re ρ = ½.
   - This is the same computation as the kernel of the defect D_n in PTQ1.2 (`25_` §2.1).
3. **The strong closure of the trace image is the whole dual if and only if all zeros are simple (RTT6).**
   - *Proof.* The closure is N₀^⊥, and N₀ = 0 if and only if no class has vanishing values without being zero. If m_ρ ≥ 2, the isolator E_{ρ,1} is such a class. If all m_ρ = 1, the values determine the class.
4. **The residue bridge carries no positivity of its own.** R̂(F, SG) = W(F, G) (RTT5), and RTT9.4 writes W(F, G) as Weil's explicit formula for the test A = F·G^#, where G^#(s) = conj G(1 − s̄). So the positivity of the bridge is Weil's criterion. RTT11 says that the comparison proves no new positivity theorem.
5. **FOD and NEA see only the divisor.**
   - The class modules M/𝔞 and M/𝔞₊ are determined by the zeros with their multiplicities.
   - The boundary obstructs nothing that comes from Q (δ∘f = 0, unconditionally).
   - The "weights" 2Re ρ + 2 of NEA7 re-encode Re ρ. Asking them all to equal 3 is RH by definition.

This extends `25_` §5. Every positivity, adjointness or weight statement in the five blocks is either unconditional, and then carries no information about Re ρ, or is RH (or simplicity) by definition.

## 3. Lemmas extracted

**Lemma 27.1 (the spectral theory of multiplication by s on B/I_D).**
- *Setting.* Let Φ ∈ B have zero divisor exactly D, and let I_D ⊂ B be the functions vanishing to the orders prescribed by D. Let L be multiplication by s on Q_D = B/I_D.
- *Statement.* Spec L = supp D. For λ ∉ supp D the resolvent is R_λF = (F − Φ·F(λ)/Φ(λ))/(λ − s). The Riesz projector at ρ is multiplication by an entire function e_ρ ∈ B. It has rank m_ρ, and L − ρ acts on its range as a single nilpotent Jordan block of length m_ρ.
- *Proof.* RZ3–RZ7, verified. `24_` Lemma 24.2, step 1, is the first part. The Riesz formula is the Fréchet analogue of the Banach-space version (Kato, *Perturbation Theory for Linear Operators*, ch. III).

**Lemma 27.2 (B is a Fréchet–Schwartz space).**
- *Statement.* For every A and M, the unit ball of b_{A+1,M+1} is precompact for b_{A,M}. Consequently B, and every quotient of B by a closed subspace, is Fréchet–Montel and reflexive, and the strong dual of B/I is I^⊥ ⊂ B′_β.
- *Proof.*
  1. Let b_{A+1,M+1}(F) ≤ 1. On |Re s| ≤ A + 1, |F(s)| ≤ (1+|t|)^{−M−1}.
  2. Cauchy's estimate on discs of radius ½ bounds |F′| by 2(1+|t|−½)^{−M−1} on |Re s| ≤ A + ½. So the ball is equicontinuous and bounded there.
  3. Given ε > 0, choose T with (1+T)^{−1} < ε. On |t| ≥ T, (1+|t|)^M|F| < ε for every F in the ball.
  4. On the compact rectangle |Re s| ≤ A, |t| ≤ T, Arzelà–Ascoli gives a finite ε(1+T)^{−M}-net in the supremum norm. Together with step 3, it is a 2ε-net for b_{A,M}.
  5. The consequences are the standard permanence properties of Fréchet–Schwartz spaces: Schwartz implies Montel, and quotients by closed subspaces stay Schwartz. For these, see a text that treats Schwartz spaces, for example Jarchow, *Locally Convex Spaces*, or Horváth, *Topological Vector Spaces and Distributions* (not re-read). Montel spaces are reflexive (Schaefer, *Topological Vector Spaces*, ch. IV).
  6. For the topological identity (B/I)′_β ≅ I^⊥ ⊂ B′_β, bounded sets must also lift. Bounded sets of B/I are relatively compact, and compact sets lift through the quotient map of a Fréchet space; SDT4's construction applies verbatim. So the strong topologies agree, as in SDT5. ∎
- *Why it matters.* SDT proves these properties for A and A/J, and transfers them to B/I through κ: A/J ≅ B/I, which rests on the exact summation image. The lemma proves them for B and B/I directly.

**Lemma 27.3 (local rank-one and residue lemmas).**
- If f(ρ + v) = v^m u(v) with u(0) ≠ 0, then f′(ρ − t) ≡ m(−1)^{m−1}u(0)t^{m−1} mod t^m (RTT3).
- Res_{s=ρ} Φ(s)ζ′(s)/ζ(s) = m_ρΦ(ρ) (RTT4).
- The residue matrix at a zero of multiplicity m has determinant u(0)^{−m} (SDT8.8; the same as GZR4.7, `26_`).
- All three are elementary. The first is the source of the rank-one blocks of P.

**Lemma 27.4 (the annihilator of a tautological extension; FOD4, NEA3).**
- *Statement.* Let I ⊂ B be an M-submodule and let e be the class of 0 → I → B → B/I → 0 in Ext¹_M(B/I, I). Suppose some g ∈ M with gB ⊂ I acts injectively on B. Then Ann_M(e) = Ann_M(B/I).
- For the zeta ideals, g = F₀·F₊ works. In FOD4.7 and NEA3.3, e^{s²} ∈ B is used to show Ann_M(B/I) = 𝔞 (respectively 𝔞₊ = K₊). The classes are nonzero because 1 ∉ 𝔞.
- A companion fact: Ext¹_M(M/(z^k), N) = N/z^kN, because M is an integral domain.

## 4. What was not checked

- **RTT:** GTR2–GTR4 (the sheaf-trace meaning of RTT7.5), RD8, GIQ2–GIQ3 and GIQ8, GTAH, and SSI's endpoint lines. GIQ9, the explicit formula, was re-derived independently.
- **RZ:** S1, S2 and S5 (read for `04_`), and G1–G5.
- **SDT:** CDI0–CDI3 and CDI8–CDI12, CSP0–CSP1, and RD2–RD4.
- **FOD and NEA:** GMS9 (the simultaneous complexes, read but not re-derived in `24_`), CLP12–CLP13, and CW1–CW8.

## 5. Items for the goals

- **Goal 3.** Lemmas 27.1–27.4. Lemma 27.2 is the most useful for later work, because it removes a dependency.
- **Goal 1.** The four RH- or simplicity-equivalences of §2 extend the negative result of `25_` §5. With `24_`–`27_`, the analytic core of the three-lane edition is now audited: the separator, the summation image, the dual constructions, the residue bridge and the class modules. The audited parts are correct, subject to the unread inputs listed in §4, and they contain no mechanism for Re ρ = ½.

## 6. Checks

`checks/rtt_rz_sdt_fod_nea_audit_checks.py` (47 items, all pass). The items cover:
- the Euler–Maclaurin formula, with a negative control on the sign of the remainder;
- H_ζ(0) = −1 and its s² coefficient −γ₁;
- the values of F₀;
- RTT9.4 for three Gaussian tests, with a control that flips the sign of the prime term;
- the Riesz projector integral at ρ₁;
- the residue-matrix determinant for m ≤ 7;
- the Schwartz-image inverse and its Taylor coefficients;
- the Weil-form identities on a synthetic divisor that contains an off-line pair;
- the CRT identities in a polynomial toy model.

## 7. Sources

- The programme blocks listed at the top (commit 064f33b).
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952), 252–265. Cited as the origin of RTT9.4; not re-read.
- T. Kato, *Perturbation Theory for Linear Operators*, ch. III; H. H. Schaefer, *Topological Vector Spaces*, ch. IV. Standard references for the Riesz projector and for Montel and reflexive spaces; not re-read for this note.

## 8. Revisions after the ninth referee pass (12:56 UTC)

One subagent refereed `27_` and `28_` and re-ran both check scripts (47/47 and 12/12, identical output). For `27_` it made no major finding. Applied here:
1. Lemma 27.2 gains step 6: bounded sets lift, so (B/I)′_β ≅ I^⊥ topologically. The references for Schwartz spaces are corrected.
2. "Why it matters" and §0 item 4 now say correctly that SDT transfers the properties to B/I through κ.
3. The explicit-formula bullet now names all three truncations and the actual agreement, about 10⁻²⁶.
4. §5 says "correct, subject to the unread inputs of §4".
5. Two wordings are fixed: the role of e^{s²} in Lemma 27.4, and what RTT11 says. The shebang of the copied script is restored to line 1.
