# The Deligne reader, part 1 (DP, DMG, DLM): the reconstruction checks out, five of its six corrections concern the printed Weil II, and an algebraic purity criterion

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 17:02 UTC. Board task 8: the Deligne reader outside the parts read earlier. The first pass was an audit by one subagent (47 checks); §0 says what I verified myself. Refereed in the thirteenth pass (17:50 UTC) and revised at 17:55 UTC; §8 lists the changes.

## 0. Source, method and checks

- **Source.** `DELIGNE_WEIGHT_CONTROL_FULL.md`, the programme's "Deligne reader": 4688 lines, SHA-256 `6478584d…26ffa595`. The same bytes are published in the reader repository at `workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/` (commit 36a82ec).
  - **Audited here:** DP0–DP9 (lines 79–344), DMG0–DMG7 (lines 345–770) and DLM1–DLM15 (lines 771–1477).
  - **Also read, for conventions and coverage claims:** the introduction (lines 1–78), the closing reading record (lines 4614–4688) and `DELIGNE_FULL_READING_LOG.md`.
  - **Read in earlier notes:** DB9, DR, DC, DW5–DW11 and MDB9–MDB11 (`07_`, `08_`).
- **Label note.** "DW" in this note, as in `07_`–`08_`, means the reader's sections DW0–DW11. `35_` uses "DW" for a different file.
- **The work it reconstructs.** P. Deligne, *La conjecture de Weil. II*, Publ. Math. IHÉS 52 (1980), 137–252, §§1.3–1.9. The reader works from a French transcription. I compared the displays in question with the printed pages (numdam scan).
- **Method.** One subagent made the first pass: an item-by-item verdict and 47 checks on explicit finite-dimensional models, all passing. My re-run at 16:59 UTC reproduces its output apart from the timing column. I verified the following myself:
  - the core purity argument, DP4–DP6 and DLM10, line by line (§1);
  - the reader's six corrections to its transcription, against the printed pages 166, 169, 170, 171 and 175, which I read (§2). I also read Deligne's Frobenius convention (1.1.7, p. 150) and his definition of N in (1.7.2, p. 171), which decide correction 5, and Proposition (1.6.9) on p. 167 (in the OCR text; the referee read the page image);
  - the subagent's five "errors", of which one is kept as an error (§3);
  - Lemmas 36.1–36.3, the negative results and the bridges, by the derivations given in §§4–6.
- **Checks.** `checks/deligne_reader_part1_checks.py`: the subagent's script, 47 items (C01–C46, with C08b), unchanged apart from the header. It needs sympy, mpmath and python-flint.

**Verdict.**
- **The reconstruction is correct as far as checked.** No step fails in a way that changes a conclusion. DLM10 follows the printed proof of Théorème 1.8.4 (p. 176) step by step, keeping β where Deligne twists to β = 0.
- **Gaps.** Several steps are compressed (§3). Two of them are compressed in the same way in the printed text.
- **The six corrections.** Five of the reader's six corrections concern the printed original. Four are misprints there: (1.6.7), (1.6.13), (1.6.14.3), and the index in (1.7.5). One is a coupled slip: the coefficient in (1.7.5), together with the type of λ. The sixth, (1.8.1.1), is a defect of the English transcription only.
- **The reader contradicts its own log.** Its DLM preamble (line 789) calls the six corrections "not accusations about Deligne's printed original", and its introduction (line 5) moves only two displays out of the transcription. Its reading log records a comparison with the printed pages that places items 1–5, and (1.3.10)(iv), in the original. The printed pages agree with the log.
- **No comparison with the programme.** Inside lines 79–1477, every mention of a programme object is a disclaimer. These three parts prove no comparison with the programme.

## 1. What the three parts prove

- **DP (Weil II §§1.3–1.5).** Let F₀ be an ι-real lisse sheaf on a curve over F_q. Then every constituent of F₀ is pointwise ι-pure. The steps:
  - DP1: rank-one characters are c^{deg}·ε with ε of finite order, by class field theory; the determinant weights follow.
  - DP2: a central element of positive degree in the monodromy group.
  - DP3: the trace formula; H_c² has weights ≤ b + 2 when the determinant weights are ≤ b.
  - DP4: even tensor powers have nonnegative local coefficients (Lemma 36.1).
  - DP5: the global L-function of F₀^{⊗2k} has no pole in |t| < R_k = q^{−kr−1}, where r is the largest determinant weight. By coefficientwise domination, each local factor converges there. A local pole |ια|^{−2k/d_x} ≥ R_k gives w(α) ≤ r + 1/k (check C11), for every k, hence w(α) ≤ r.
  - DP6: apply DP5 to ∧^{N_β+1}F₀, with N_β the rank of the constituents of determinant weight above β. The largest determinant weight there is β + Σ_{γ>β}n(γ)γ. Subtracting the determinant equalities gives w(α) ≤ β for every eigenvalue α of the weight-β constituents. Their sum equals n(β)β, so each equals β (check C12).
- **DMG (the group arguments of §1.3).** Monodromy groups, the radical, dominant pullback, compact normalizers and the étale criterion. The subagent finds these correct given their external inputs: class field theory, the structure of linear algebraic groups, and ℓ-adic Lie theory. I did not re-derive DMG6–DMG7.
- **DLM (§§1.6–1.9).**
  - DLM1–DLM4: the monodromy filtration, the SL(2) bookkeeping, and the uniqueness of the relative filtration (checks C14–C31).
  - DLM5: N and FNF^{−1} = Q^{−1}N.
  - DLM6: independence of the Frobenius lift (Lemma 36.3).
  - DLM7: tame specialization.
  - DLM8: boundary weights ≤ β, from the trace formula and all tensor powers (Weil II Lemme 1.8.1, p. 175). DLM9: weights ≤ β + 2 on H_c¹(X, j_*F) (Remarque 1.8.2, p. 175). I read p. 175.
  - DLM10: local purity, Gr_i^M of weight β + i. The reader's derivation matches the printed proof on p. 176: the boundary bound on ker N = V^I, the summand P_{−j} ⊗ P_{−j}(−j) of P₀(V ⊗ V) with eigenvalue α²Q^j, and the dual with eigenvalue α^{−1}Q^{−j}. Together these force |ια| = Q^{(β−j)/2}.
  - DLM11–DLM15: mixed input, extension, and several variables.

## 2. The six corrections, against the printed text

The reader lists six corrections of its transcription (lines 789–802). The printed pages decide where each defect lies.

| # | Display | Printed original | Assessment |
|---|---|---|---|
| 1 | (1.6.7) | p. 166: the exception is printed "i ≠ d" | The basis runs from e_d down to e_{−d} in steps of 2, so Ne_{−d} = 0 and the exception must be i ≠ −d. A misprint in the original. |
| 2 | (1.6.13) | p. 169: the chain is printed "k − 2i − 2 ≥ k ≥ 2j − k" | The first inequality fails for every i ≥ 0. What the proof needs is k − 2i − 2 ≥ 2j − k for k > i and j ≤ 0, and the chain with −k in the middle gives it: k − 2i − 2 ≥ −k because k ≥ i + 1, and −k ≥ 2j − k because j ≤ 0 (check C31). A misprint in the original; restoring one minus sign repairs it. |
| 3 | (1.6.14.3) | p. 170: positive twist P_{−j}((i+j)/2) | Deligne's weight mnemonic on the same page forces the negative twist, and so does the proof of 1.8.4 (checks C25; `35_` §1). A misprint in the original. |
| 4 | (1.7.5), the filtration | p. 171: M′_i = ∏_{j<i} V′_j | With j < i, Gr_i = V′_{i−1} has weight i − 1, but the proposition asserts weight i. So j ≤ i is meant (check C35). A misprint in the original. |
| 5 | (1.7.5), the coefficient | p. 171: λ ∈ Q_ℓ(−1), F″ⁿ = exp(λN)F′ⁿ, μ = λ/(1 − qⁿ) | A coupled slip in the original; see below. The reader's μ = λ/(1 − Q^{−n}) (DLM6.2) is right under the printed conventions. |
| 6 | (1.8.1.1) | p. 175: the denominator is H_c² | The printed text agrees with the French transcription. The H⁰ of the English transcription is a transcription defect only. |

**Correction 5 in detail.**
- **The conventions the printed text fixes.**
  - (1.1.7), p. 150: F is the geometric Frobenius, the inverse of x ↦ x^q. So F acts on Q_ℓ(1) by q^{−1}.
  - (1.7.2), p. 171: N is a map V(1) → V.
  - Hence λN is an endomorphism of V exactly when λ ∈ Q_ℓ(1): N lies in Hom(V(1), V) = End(V) ⊗ Q_ℓ(−1), and pairing with λ must cancel the twist. Then F′ⁿ(λN)F′^{−n} = q^{−n}λN, by the Weil-group equivariance of N (1.7.3).
- **The computation.** exp(μN)F′ⁿexp(−μN) = exp(μ(1 − q^{−n})N)F′ⁿ. So μ = λ/(1 − q^{−n}), which is the reader's value (check C33).
- **What the printed value corresponds to.** The printed 1 − qⁿ is what the same computation gives when F′ acts on λ by q, that is, for λ ∈ Q_ℓ(−1) as printed. But for λ ∈ Q_ℓ(−1), λN lies in End(V) ⊗ Q_ℓ(−2) and is not an endomorphism of V.
- **So the two printed choices agree with each other and disagree with (1.7.2).** The conclusion of (1.7.5) is unaffected, since it uses only 1 − q^{±n} ≠ 0.
- **The subagent's caveat.** It notes that 1 − qⁿ is exact in two other conventions (check C34): for arithmetic Frobenius, with the printed ordering and conjugation; and for the other ordering F″ⁿ = F′ⁿexp(λN) together with the reversed conjugation exp(−μN)F′ⁿexp(μN). (With the printed conjugation, the other ordering needs μ = λ/(qⁿ − 1).) That is right as algebra, but the printed ordering, the printed conjugation and (1.1.7) exclude both alternatives.
- **A further confirmation.** In (1.7.2.2), p. 171, ρ(σ) = exp(N·t_ℓ(σ)) with t_ℓ(σ) ∈ Z_ℓ(1). The λ of (1.7.5) is t_ℓ of an inertia element, so λ ∈ Z_ℓ(1) ⊂ Q_ℓ(1) can be read off directly.

**Two related displays.**
- The reader's DP1.6 corrects the exponent in (1.3.6). Its log records that the printed page 158 has the correct multiplied factor, so the defect is in the transcription. I did not read p. 158.
- (1.3.10)(iv) is a misprint in the original (p. 160; `35_` §5).
- The referee of the thirteenth pass read p. 158 and confirms the multiplied factor in (1.3.6).

**Other slips on the same pages** (found by the referee; each harmless):
- p. 171 cites "(1.6.14), (1.6.15)", but §1.6 ends with (1.6.14); a search of the OCR text finds no label (1.6.15).
- p. 176: the proof of 1.8.4 introduces an eigenvalue on P_{−i} and continues with P_{−j}.
- p. 166: the diagram after (1.6.4.1) labels its column P₁, …, P₄ where P_{−1}, …, P_{−4} are meant (P_j = 0 for j > 0).

**Novelty.** A quick search by the referee found no published erratum listing these displays (the IAS publication page for the paper lists none); one repository answered HTTP 429 and was not read. No novelty is claimed for the list.

## 3. The subagent's findings, with my assessment

- **E1 (DLM3.3, the index of the sum).** The display copies Deligne's own notation in (1.6.14.4), p. 170, where the sum is indexed by j ∈ P(j′, j″). It is to be read as a sum over the pairs (j′, j″) with j ∈ P(j′, j″). This is not an error of the reader, and the prose after the display states the twist correctly.
- **E2 (DLM5, line 1089).** "Except for the zero operator, a nilpotent operator cannot square to the identity." The zero operator on V ≠ 0 does not square to the identity either. The correct statement: on V ≠ 0 no nilpotent N has N² = 1, since N² = 1 would make N invertible. This is a side remark with no role in the argument. **Kept as an error (wording).**
- **E3 (DP1, line 116).** Not an error. The group, the geometric part of the abelianized Weil group (line 111), is abelian and profinite, hence the product of its pro-p part and its prime-to-p part. The prime-to-p part injects into the finite quotient by an open pro-p subgroup, so it is finite. The group is therefore finite-by-pro-p, as line 116 says, and also pro-p-by-finite, as DMG1 (line 384) says. Line 116 leaves implicit the commutativity that makes the two descriptions equivalent.
- **E4 (DMG1, line 386).** Read as the intersection inside the compact image, the sentence is correct: that intersection is a closed subgroup both of a pro-p group and of a pro-ℓ group. No change is needed.
- **E5 (correction 5 "convention-dependent").** Settled in §2: under Weil II's own conventions the reader's correction is right.
- **Compressed steps**, with the subagent's fillings:
  - DP5 does not restate that F₀ is ι-real, which DP4.2 needs.
  - DMG1 does not treat two points: the normalization of the curve joining two points, and the density of degree-zero Frobenius products in the kernel of the degree. The second follows in one line. The degree takes values in the discrete group ℤ, so its kernel K is open in the abelianized Weil group. The subgroup Γ generated by the Frobenius elements is dense (Čebotarev density), so Γ ∩ K is dense in K, and Γ ∩ K consists of the degree-zero products of Frobenius elements and their inverses.
  - DMG6 needs the equivariance of the logarithm under conjugation, on topologically unipotent elements.
  - DLM6 chooses n > 0 for which the powers of the two lifts differ by unipotent inertia (line 1110). This needs I₁ normal in the local Weil group: then conjugation by a Frobenius lift permutes the finite group I/I₁, and a suitable power gives F″ⁿ ≡ F′ⁿ mod I₁. The printed text compresses this in the same way (p. 171).
  - DLM7, DLM11–DLM13 sketch the tame specialization, the stratification and the reductions (SGA 1 XIII, Abhyankar's lemma).
  - DLM10 needs two further points. One is the Frobenius-equivariance of the primitive maps; check C38 constructs the vector explicitly. The other is a global finite cover inducing the required local extension; the printed proof also just replaces X₀ by a finite cover (p. 176).
  - DP2 defers the constant-field bookkeeping to DMG.

## 4. Standalone lemmas

**Lemma 36.1 (positivity and domination; DP4).**
- **Setting.** Let A_x be finitely many complex square matrices with real characteristic polynomials, and d_x ≥ 1 integers.
- **Statement.** For every k ≥ 1, each factor det(1 − A_x^{⊗2k}t^{d_x})^{−1} has nonnegative Taylor coefficients and constant term 1. It is dominated coefficientwise by the product of all the factors.
- **Proof.**
  - tr((A^{⊗2k})^j) = (tr A^j)^{2k}, and tr A^j is real by Newton's identities. So log det(1 − A^{⊗2k}t^{d})^{−1} = Σ_j (tr A^j)^{2k}t^{jd}/j has nonnegative coefficients.
  - The exponential of a series with nonnegative coefficients and zero constant term has nonnegative coefficients and constant term 1. A product of such series dominates each factor.
  - Check C09.
- **Reality is necessary.**
  - A = (i), k = 1: the factor is 1/(1 + t), whose t-coefficient is −1.
  - A = diag(1, i): (tr A)² = 2i is not real (check C10).

**Lemma 36.2 (an algebraic purity criterion: the core of DLM10 and of Weil II 1.8.4).**
- **Setting.** Let V be a finite-dimensional complex vector space, N a nilpotent operator and F an invertible operator with FNF^{−1} = Q^{−1}N, where Q ∈ ℂ and |Q| ≠ 1 (in Weil II, Q = N(s) > 1). Put w(α) = 2 log|α|/log|Q|. Let M be the monodromy filtration of N.
- **Dual.** On V^∨ put F^∨ = (F^{−1})^t and N^∨ = −N^t. These satisfy the same relation: F^∨N^∨(F^∨)^{−1} = −(FNF^{−1})^t = Q^{−1}N^∨.
- **Statement.** The following are equivalent.
  - (a) For every i, all eigenvalues of F on Gr_i^M V have weight β + i.
  - (b) All eigenvalues of F⊗F on ker(N⊗1 + 1⊗N) ⊂ V⊗V have weight ≤ 2β, and all eigenvalues of F^∨⊗F^∨ on ker(N^∨⊗1 + 1⊗N^∨) ⊂ V^∨⊗V^∨ have weight ≤ −2β.

*Proof.* (a) ⇒ (b):
- The monodromy filtration of N⊗1 + 1⊗N is M_k(V⊗V) = Σ_{a+b=k} M_a ⊗ M_b in characteristic 0 (Weil II Proposition (1.6.9)(i), p. 167; reader DLM2.3; check C20). So Gr_k(V⊗V) = ⊕_{a+b=k} Gr_a ⊗ Gr_b has weight 2β + k.
- N is injective on Gr_k for k ≥ 1, since N^k: Gr_k → Gr_{−k} is an isomorphism. Hence ker N_{V⊗V} ⊂ M₀(V⊗V), whose eigenvalues have weight ≤ 2β.
- The dual has M_i(V^∨) = M_{−i−1}(V)^⊥ (Weil II (1.6.9)(ii); reader DLM2.4; check C21), so Gr_i(V^∨) ≅ (Gr_{−i}V)^∨, of weight −β + i. So V^∨ satisfies (a) with −β, and the same argument applies to it.

(b) ⇒ (a):
- **Upper bound.** Let α be an eigenvalue of F on P_{−j} = ker(N: Gr_{−j} → Gr_{−j−2}), with j ≥ 0.
  - By (1.6.14.4) with j′ = j″ = j and target index 0, P_{−j} ⊗ P_{−j}(−j) is a direct summand of P₀(V⊗V). Once twisted, the isomorphisms (1.6.14) do not depend on the choice of N (Weil II, end of p. 169), so by transport of structure they commute with F, which acts on the line 𝔑 by Q^{−1}. The twist (−j) multiplies eigenvalues by Q^j, so α²Q^j is an eigenvalue there.
  - Directly: let x ∈ P_{−j} with Fx = αx, and y ∈ Gr_j^M V with N^j y = x; then Fy = αQ^j y. The vector z = Σ_s(−1)^s N^s y ⊗ N^{j−s}y ∈ Gr₀^M(V⊗V) = ⊕_a Gr_a ⊗ Gr_{−a} is nonzero. It is killed by N⊗1 + 1⊗N, because the sum telescopes to (−1)^j N^{j+1}y⊗y + y⊗N^{j+1}y = 0, and it has eigenvalue α²Q^j (check C38).
  - P₀(V⊗V) = Gr₀^M(ker N_{V⊗V}) by (1.6.6) (DLM1.7; check C17). So α²Q^j is an eigenvalue on ker N_{V⊗V}.
  - Hence 2w(α) + 2j ≤ 2β, that is, w(α) ≤ β − j.
- **Lower bound.** By (1.6.14.5), P_{−j}(V^∨) ≅ P_{−j}(V)^∨(j), which carries the eigenvalue α^{−1}Q^{−j}. The same argument on V^∨ gives −w(α) − 2j ≤ −β − j, that is, w(α) ≥ β − j.
- **Conclusion.** Every eigenvalue on P_{−j} has weight β − j. By the corrected (1.6.14.3), Gr_i ≅ ⊕_j P_{−j}(−(i + j)/2), which has weight β − j + (i + j) = β + i. ∎

Check C40 tests the equivalence on random models: 18 pure and 22 impure.

*Scope.* The lemma separates the algebra of Deligne's local theorem from its geometry. In Weil II, condition (b) is supplied by Lemme 1.8.1 for F₀ ⊗ F₀ and for F₀^∨ ⊗ F₀^∨, because for unipotent inertia ker N_{V⊗V} = (V⊗V)^I = (j_*(F₀⊗F₀))_s̄, and likewise for the dual. After the twist to β = 0 and the finite cover that makes inertia unipotent, the rest of the proof of 1.8.4 (p. 176) is the implication (b) ⇒ (a). The converse is not used there; its key step, ker N ⊂ M₀, is Remarque (1.8.8), p. 176.

*Novelty.* The implication (b) ⇒ (a) is Deligne's argument (p. 176). The implication (a) ⇒ (b) uses only (1.6.9) and ker N ⊂ M₀. The equivalence is not claimed to be new.

**Lemma 36.3 (independence of the Frobenius lift; DLM6).**
- **Setting.** Let N be nilpotent and F, F′ invertible with FNF^{−1} = Q^{−1}N, where |Q| ≠ 1, with weights w(α) = 2 log|α|/log|Q| as in Lemma 36.2, and F′ⁿ = exp(λN)Fⁿ for some n ≥ 1 and some scalar λ.
- **Statement.** With μ = λ/(1 − Q^{−n}), F′ⁿ = exp(μN)Fⁿexp(−μN). Hence the filtrations by generalized eigenspaces of weight ≤ i agree for F and F′.
- **Proof.**
  - exp(μN)Fⁿexp(−μN) = exp(μN)exp(−μQ^{−n}N)Fⁿ = exp(μ(1 − Q^{−n})N)Fⁿ.
  - The filtration ⊕_{w≤i}V_w is preserved by exp(μN), because N lowers weights by 2.
  - Passing from F to Fⁿ does not change the weights: w_{Qⁿ}(αⁿ) = w_Q(α). Check C33, C35. ∎

## 5. Negative results (goal 1)

- **36.N1. Determinant data at a point control only the sum of the weights** (DP1.5; check C03). Individual weights need the exterior powers together with a pole bound uniform in the tensor degree (DP5–DP6). This is the same missing input that `29_` 29.N4 and `35_` 35.N1 identify on the programme side.
- **36.N2. The boundary bounds for V and V^∨ alone do not force the conclusion of Théorème 1.8.4; the tensor square is needed.**
  - **Example.** Take V = ⟨v⟩ ⊕ ⟨v₁, v₀⟩ with Nv₁ = v₀ and Nv₀ = Nv = 0. Let Fv = av with w(a) = β, and Fv₁ = bv₁, Fv₀ = (b/Q)v₀ with w(b) = c + 1. So the 2-string has centre c.
  - **The bounds for V and V^∨.** ker N = ⟨v, v₀⟩ has weights β and c − 1. ker N^∨ = ⟨v^*, v₁^*⟩ has weights −β and −(c + 1). Both bounds hold exactly when β − 1 ≤ c ≤ β + 1.
  - **Condition (a).** Condition (a) of Lemma 36.2 holds exactly when c = β.
  - **The tensor square.** The vector v₁⊗v₀ − v₀⊗v₁ lies in the kernel of N⊗1 + 1⊗N and has weight 2c. So the criterion of Lemma 36.2 gives c ≤ β, and its dual gives c ≥ β.
  - Check C41 tests the 2-string alone, with β = 0 and c = 1; the summand ⟨v⟩ only adds the weights β and −β to the two kernels and does not change the outcome.
- **36.N3. An operator that commutes with N cannot carry Deligne's local weights unless N = 0.**
  - If WNW^{−1} = N, then N^i: Gr_i → Gr_{−i} is a W-equivariant isomorphism, so Gr_i and Gr_{−i} have the same W-eigenvalues. "Weight β + i on Gr_i" is then impossible for i ≠ 0 with Gr_i ≠ 0.
  - Also, Lemma 36.3 does not apply: its hypothesis |Q| ≠ 1 fails, 1 − Q^{−n} = 0, and exp(λN)W need not be conjugate to W (check C43, with W = 1).
  - This applies to the programme's counting operators W_p (on the jet blocks J_ρ with m ≥ 2; DW9.1 of `AMPLIFICATION_AND_GLOBAL_EULER_PRODUCT.md`) and C_b (on the blocks of Ẽ with d_λ ≥ 2; GJN5.2).
- **36.N4. The programme's ramification operator has no eigenvector on Ẽ, so Deligne's local weight filtration is not defined for it.**
  - *Setting.* Let b ≥ 2. P_b maps the block span{H_{λ,j}} into span{H_{bλ,j}} (GJN2.2) and is injective on Ẽ (GJN2.4).
  - *Proof.* Suppose v ≠ 0 in Ẽ, a finite sum of block components, and P_bv = cv.
    - Let λ₀ be a block of the support of v with |λ₀| minimal. It is nonzero, since Λ consists of multiples aρ of nonreal zeros.
    - Every block in the support of P_bv has modulus ≥ b|λ₀| > |λ₀|. So the λ₀-component of P_bv vanishes. Hence c·v_{λ₀} = 0, so c = 0, and then P_bv = 0 contradicts injectivity. ∎
  - *Consequence.* The relation NP_b = bP_bN has Deligne's form (`35_` §3). But the weight filtration that DLM6 and Lemma 36.3 build from a Frobenius needs generalized eigenspaces, and P_b has none on Ẽ.
  - On a finite-dimensional space with PNP^{−1} = b^{−1}N and |b| > 1 the construction would apply verbatim (check C45). The programme's P_b is not of that kind: it moves every block.

## 6. Bridges (goal 2)

- **Positivity.** DP4 is the same computation as ETR5.6–ETR5.9 (`29_`) and DW7.7 of the other DW file (`35_`): nonnegative coefficients from real traces of even tensor powers. DP5's input is a pole-free disc |t| < q^{−kr−1}, whose loss against the weight 2kr of F₀^{⊗2k} is the fixed +2 of H_c² = V_Π(−1), independent of k. Here r is the largest determinant weight of the constituents (Définition 1.3.5). For the quartet on ℝ, r = 2·max(Re ρ, 1 − Re ρ) and the disc is there; what the programme lacks is the same disc with r equal to the average weight 1, which Deligne has when the eigenvalues lie in one constituent (register negative result 52, `29_` 29.N4, `37_` §6; corrected after the fourteenth referee pass).
- **Remark 36.R1: the regraded jet blocks satisfy the conclusion of Théorème 1.8.4, with a centre that depends on the multiplicity.** For m ≥ 2 the block is mixed in the sense of Weil II (1.7.4), since it has m weights; its graded pieces Gr_i^M are pure of weight β_ρ + i. Later literature calls this property of a Weil–Deligne representation "pure of weight β_ρ" (R. Taylor and T. Yoshida, Compatibility of local and global Langlands correspondences, J. Amer. Math. Soc. 20 (2007), §1; arXiv:math/0412357); Weil II does not.
  - **The regraded block.** Under the regrading in DW9 of the other DW file (`35_` §2), F = p^ρS_p acts on the jet block of a zero ρ of multiplicity m, with basis ε⁰, …, ε^{m−1} and Nε^j = ε^{j+1}.
    - The monodromy filtration puts ε^j in degree (m − 1) − 2j.
    - The F-weight of ε^j relative to p is 2Re ρ − 2j = (2Re ρ − (m − 1)) + ((m − 1) − 2j).
    - So Gr_i^M has weight β_ρ + i, with β_ρ = 2Re ρ − (m − 1): the block satisfies Lemma 36.2(a) with centre β_ρ (check C44).
  - **The off-line quartet.** Take {ρ, ρ̄, 1 − ρ, 1 − ρ̄} with multiplicity m and Re ρ = σ. The four blocks have centres 2σ − (m − 1) and 2(1 − σ) − (m − 1). These are equal exactly when σ = ½.
  - **What this adds.** Nothing beyond `35_` 35.N1: only the constituent weights see an off-line zero. The regrading is chosen, not derived, so the remark is bookkeeping and not a constraint on zeros.
- **Answer to "does DLM give more than the comparison of relations?"**
  - For an abstract finite-dimensional operator satisfying the relation with |Q| ≠ 1, DLM gives two things: a canonical weight filtration (Lemma 36.3), and an exact criterion (Lemma 36.2) for that filtration to be the shifted monodromy filtration.
  - For the programme's operators neither applies: counting has Q = 1 (36.N3), and ramification has no eigenvectors (36.N4).
  - Nothing in DP, DMG or DLM supplies, for a programme operator, the tensor-square bound that Deligne gets from geometry.

## 7. Not checked

- The printed text outside pp. 150, 158, 160, 164–171 and 175–176 (the pages read by me or by the referee of the thirteenth pass).
- DMG6–DMG7 in detail: I rely on the subagent's check and its list of external inputs.
- The external theorems: class field theory, Grothendieck's trace formula and local monodromy theorem, SGA 1 XIII, the structure of algebraic groups.
- The reader's parts DB0–DB8, DB10, DBC1–DBC11, DW0–DW4 and MDB0–MDB8. These are the next block of board task 8.

## 8. Revision after the thirteenth referee pass (17:55 UTC)

One referee (a subagent) checked every statement against the reader, its log and the printed pages (pp. 150, 158, 160, 164–171 and 175–176 on page images), wrote its own check script (52 items, 42 PASS and 10 expected fails documenting findings; its re-run of `checks/deligne_reader_part1_checks.py` reproduces 47/47), and tested Lemma 36.2 on 72 exact and 30 complex random models, including non-semisimple F and |Q| < 1. It confirms every assessment of a printed display, the analysis of correction 5, Lemmas 36.1–36.3, the computations of 36.N2–36.N4 and Remark 36.R1. I checked the two major findings and applied them:
- **§3, E3.** The reader's "finite-by-pro-p" is correct, because the group is abelian (Sylow decomposition). E3 is withdrawn as an error.
- **§6, Remark 36.R1** (and register bridge 39, digest §4 item 26). A local representation is pure in Weil II's sense (1.7.4) when it has one weight. The regraded block with m ≥ 2 has m weights, so it is mixed. What 36.R1 shows is the conclusion of Théorème 1.8.4 (Gr_i pure of weight β_ρ + i), which later literature calls "pure" for Weil–Deligne representations (Taylor–Yoshida, checked on arXiv). The wording is corrected here, in 36.N2, in register negative result 61 and bridge 39, and in the digest.

Minor findings applied: the paraphrase of the subagent's caveat on 1 − qⁿ (§2); a further confirmation of correction 5 from (1.7.2.2); other slips on the same pages and the errata search (§2); the log statement (§0); DLM9 (§1); the density argument in DMG1 and the hypothesis for DLM6 (§3); the hypothesis |Q| ≠ 1 and the weights in Lemmas 36.2–36.3; the F-equivariance and the explicit vector in the proof of Lemma 36.2; its scope and novelty; the model of check C41 (36.N2); "does not apply" and the blocks for C_b (36.N3); the cross-references ETR5.6–5.9 and register negative result 52 (§6); "DW9" of the other file and σ for Re ρ (36.R1); the page lists (§0, §7).
