# A uniform strong-coupling gap, heat flow and complementary relaxation for the SU(2) Kogut–Susskind Hamiltonian: an audited record of the Yang–Mills workbench

*Claude (Anthropic, model `claude-opus-5-5`), 27 September 2026. Published at the author's request ahead of the author's review; the author may revise or withdraw it. This record replaces the Yang–Mills reader (Zenodo 10.5281/zenodo.22987531) and note 46\_, which were withdrawn on 27 September 2026.*

## Abstract

The Yang–Mills workbench of the author (`KokunoYumeto/yang-mills-interacting-workbench`, Zenodo record 10.5281/zenodo.22883643) studies the Kogut–Susskind Hamiltonian of SU(2) lattice gauge theory on open cubic boxes. Its central result is an explicit lower bound on the spectral gap above the ground state, on the whole gauge-invariant space, uniform in the box size and the lattice spacing, for bare coupling g² ≥ 3.6836 in the workbench's normalization. We give the proof, with a sharp form of its key Casimir inequality: on any graph the best uniform constant is the girth. With inputs recomputed in this audit, the same argument gives a gap of at least 1.52κ for g² ≥ 3.9781, which includes the workbench's benchmark g² = 4. We add a bound at every truncation order, the gap on the full (non-gauge-invariant) space, the persistence of the gap at complex coupling, so that the ground state is analytic on a disk of box-independent radius, and an upper bound that locates the gap in [2.90κ, 3.0003κ] for g² ≥ 13. For the heat flow of plaquettes we re-derive every constant of the box-independent heat remainder, improve its prefactor from 67896/169 to 2829/13, derive the kinetic-row constants, and sharpen the relaxation bounds into the complementary physical space. We also state the proved limits of the global perturbative route and of the workbench's continuum path, and the typed maps from the workbench to the Jacobian, Navier–Stokes and S⁶ material.

## 0. Introduction

### 0.1 Why this record

The Clay problem asks for a quantum Yang–Mills theory on ℝ⁴ with a mass gap [JW]. Lattice gauge theory approaches it through regulated models, and at strong coupling mass gaps are classical in the Euclidean setting [OS]. The workbench works in the Hamiltonian setting of Kogut and Susskind [KS] and aims at explicit bounds that are uniform in the volume, on the full physical space, with closed coupling thresholds, together with the machinery that such bounds make available: heat correlations, relaxation into the complementary space, and analyticity in the coupling. Its material spans five Zenodo editions and several hundred pages. This record states what is proved, with the proofs, and what it means.

### 0.2 Main results

- **Theorem 2.1** (the workbench's fifth-reference gap bound). Δ\_L ≥ κ d₅(ξ) for every box L ≥ 2, every spacing a > 0 and every ξ ≤ α₅, that is g² ≥ 3.6836; in particular Δ\_L ≥ 1.5453κ on that range and Δ\_L > 1.9068κ for g² ≥ 4. Conditional on the computed coefficient bounds of orders 3–5.
- **Lemma 2.2** (*generalized here*). On a graph of girth g, gauge invariance forces Σ\_f j\_f ≥ g·j\_e on every Peter–Weyl block, and the girth is the best constant uniform over the links; Remark 2.3 gives the exact constant for each link.
- **Corollary 2.6** (*generalized here*). The gap bound at every truncation order N; with audited inputs of orders 1–2 it holds for g² ≥ 3.9781 with Δ\_L ≥ 1.52κ.
- **Corollary 2.7 and Proposition 2.8** (*new*). The gap on the full space is at least κd\_N/4, sharp at ξ = 0; at complex coupling |ζ| ≤ α\_N the ground state is algebraically simple and separated by a strip, so it is analytic in the coupling on a disk whose radius does not depend on the box.
- **Theorem 3.1** (*improved here*). A box-independent heat remainder on |ξ| < 1/55 with prefactor 2829/13 and rate 13/8, and a family of radii.
- **Propositions 3.3–3.5.** Relaxation bounds into the complementary physical space, the derived kinetic-row constants, and the benchmark tables: at g² ≥ 13 the energy loss is below 0.000237 and at g² ≥ 16 below 0.0000194.
- **Proposition 3.6** (*new*). An upper bound on the gap from plaquette states, which locates the gap in [2.9047, 3.00024]κ for g² ≥ 13 and shows that the true gap has no first-order term in ξ.

### 0.3 What the results mean

At strong coupling the workbench obtains, for the SU(2) Hamiltonian on open boxes, a spectral gap with explicit constants that is uniform in the volume and holds on the entire physical space. The proof rests on two structural facts: gauge invariance forces the Casimir of every nonconstant physical block to be at least 3 (the girth of the cubic lattice is 4), and the vacuum, written as an exponential, can be controlled in local Fourier-algebra norms that do not grow with the box. The same control gives box-independent heat correlations, near-complete relaxation of the plaquette family, analyticity of the ground state in the coupling on a box-independent disk, and an upper bound that pins the gap within 0.03% of 3κ at g² ≥ 13.

These are statements at fixed lattice spacing and strong bare coupling. The continuum problem requires a → 0 with g → 0, the opposite regime, and the workbench's standing continuum path leaves the domain of these estimates after finitely many steps (Proposition 6.2). What would connect the two regimes is a bound of this kind that persists along a path to weak coupling; the questions in §8 state precisely which ingredients of the present proof would have to be extended. The workbench also pursues the opposite construction: sequences driven by the S⁶ period data in which box, spacing and coupling vary together, aimed at models that are gapped at every regulator but whose continuum limit is gapless (§7).

### 0.4 How this record was made

This is an audit, carried out by an AI system, of research that was itself carried out with AI systems. The workbench credits its tools to the literature: the exponential form of the vacuum and its character calculus to Schütte, Zheng and Hamer [SZH], the Fourier-algebra estimates to Eymard [Ey], semigroup generation to Lumer and Phillips [LP], and the creation method of its first volume-uniform gap to Yarotsky [Ya], with Baez's spin networks [Ba] for the physical space. Two inputs of side branches are credited by the workbench to Levent Alpöge: the Jacobian-conjecture counterexample (whose announcement credits Akhil for the question and Fable for the work) and the S⁶ construction [A]. The Navier–Stokes material rests on OpenAI's manuscript [O].

The audit read the two proof manuscripts of the latest edition in full (F1–F42 and H1–H34), re-derived the analytic arguments, recomputed the constants and thresholds in exact arithmetic, recomputed the order-2 inputs from explicit SU(2) tensors, re-ran the workbench's order-5 producer and auditor with byte-identical output, and added the results marked *new* or *generalized here*. Statements carry one of four statuses, as in the companion papers: *verified* (proved here or re-computed by a program listed in §9), *not verified here*, *my assessment* (a view with its reasons, in the first person), and *proved negative* (with the counterexample or derivation in the text). Where a result depends on inputs that were not recomputed, it is stated as conditional on them, and the inputs are named.

### 0.5 Organization

Part A contains the verified results: the setting (§1), the gap (§2), heat flow and relaxation (§3), the earlier editions (§4), and the typed maps from the side branches (§5). Part B (§6) contains the proved limits of specific routes. Part C (§7) describes the directions that remain open, with my assessment. §8 lists questions and §9 the verification.

---

# Part A. Verified results

## 1. The setting

**Box and space.** The vertices form the open box {−L, …, L}³, L ≥ 2. The links e are the positively oriented nearest-neighbour edges inside the box and the plaquettes p the elementary faces inside it; there are M\_L = 12L²(2L + 1) plaquettes. Each link carries U\_e ∈ SU(2), and the configuration space carries the product Haar probability measure. The physical Hilbert space is the subspace of L² invariant under the gauge transformations at every vertex, boundary vertices included.

**Hamiltonian** (the workbench's normalization):

  H\_L = κK + κξ(2M\_L − S),  K = −Σ\_{e,a} X²\_{e,a},  S = Σ\_p W\_p,  κ = 2g²/a,  ξ = 1/(4g⁴).

Here X\_{e,a} differentiates U\_e along e^{tT\_a} with T\_a = −iσ\_a/2, so K is the sum of the link Casimirs, and W\_p is the trace of the ordered product of the four links around p. The plaquette term equals (2g²a)⁻¹Σ\_p(2 − W\_p) ≥ 0. The gap Δ\_L is the distance from the ground energy E₀ to the rest of the spectrum on the physical space. At ξ = 0 it equals 3κ: one plaquette in the fundamental representation, four links of Casimir 3/4. Large g is strong coupling, where ξ is small. The workbench records the conversion g\_C = 2^{3/4}g to the convention of [SZH]; the thresholds below are in the workbench's normalization.

**The approach.** The ground state is positive, so it can be written ψ = e^v/‖e^v‖. The eigenvalue equation becomes v = ξv₁ + B(v, v) with v₁ = S/3 (Lemma 2.4), whose formal solution is Σξⁿvₙ. The workbench computes v₁, …, v₅ exactly, bounds them in weighted Fourier-algebra norms that are local, so that nothing grows with the box, and solves for the remainder by a contraction; returning to the eigenvalue equation bounds every excitation energy from below (Proposition 2.5).

## 2. The strong-coupling gap

**Theorem 2.1 (the fifth-reference gap bound; F26–F42).** Let (m\_i, t\_i), i = 1, …, 5, be the ten rationals of the workbench's F26, ℓ₅(x) = Σ(m\_i + 4t\_i)x^i, δ₅(x) = Σ\_{i,j≤5, i+j≥6} 3(m\_it\_j + m\_jt\_i)x^{i+j}, 𝒟₅ = (1 − ℓ₅)² − (8/3)δ₅, α₅ the first positive root of 𝒟₅, and

  d₅(x) = (3/2)(1 + √𝒟₅(x)) + Σ\_{i≤5} ((3/2)m\_i − 6t\_i)x^i.

If the (m\_i, t\_i) bound the local norms of the vacuum coefficients, as the workbench's computations assert, then for every L ≥ 2, every a > 0 and every 0 < ξ ≤ α₅,

  Δ\_L ≥ κ d₅(ξ).

Here ξ ≤ α₅ ⟺ g² ≥ 1/(2√α₅) = 3.6835519839857273…, with α₅ = 0.0184249535761176166818…; d₅ decreases on [0, α₅] from 3 to d₅(α₅) = 1.5453…, so Δ\_L ≥ 1.5453κ for all g² ≥ 3.6836, and since d₅(1/64) = 1.9068301567…, Δ\_L > 1.9068κ for all g² ≥ 4, uniformly in the box and the spacing.

*Status.* Conditional on the computed coefficient bounds of orders 3, 4 and 5 for the threshold 3.6836 and the constants d₅. Order 1 is verified by hand. Order 2 was recomputed from explicit SU(2) coefficient tensors: m(v₂) = 134.0673… and t(v₂) = 19.7953…, below the workbench's 5834/39 and 137/6. Order 5 (662 representatives, 124,864 anchored multisets, 5,726 rational primal/dual certificates) was reproduced by re-running the workbench's producer and auditor, with byte-identical output; its logic was read, not re-implemented. Orders 3–4 are inherited from earlier continuations and pinned by hash. The analytic argument is verified; α₅, the threshold and d₅ were recomputed by exact bisection and root isolation. The qualitative content holds with verified inputs for g² ≥ 3.9781 (Corollary 2.6(b)).

The proof has two lemmas and an analytic core.

**Lemma 2.2 (the gauge-invariance Casimir inequality; generalized here).** Let the links form a finite graph without loops, parallel links allowed, in which every cycle has length at least g. On every Peter–Weyl block j that contains a nonzero gauge-invariant vector, Σ\_f j\_f ≥ g·j\_e for every link e. Hence c\_j ≥ (3g/2)j\_e for every e, Σ\_e j\_e ≤ (2/3)c\_j, and c\_j ≥ 3g/4 on the nonconstant physical space. For the cubic box (g = 4): c\_j ≥ 6j\_e and c\_j ≥ 3. The first inequality holds for all real weights j\_f ≥ 0 satisfying the vertex inequalities j\_f ≤ Σ\_{f′∋v, f′≠f} j\_{f′}, and it is an equality for j = 1/2 on a cycle of length g through e and 0 elsewhere.

*Proof.* A block contains a nonzero invariant exactly when at every vertex the tensor product of the spins j\_f (f ∋ v) contains the trivial representation; by the Clebsch–Gordan rule this gives the vertex inequalities, which are all that is used.

*A matching at each vertex.* At v the inequalities say that no j\_f exceeds half of J\_v = Σ\_{f∋v} j\_f. By Gale's supply–demand theorem this is the condition for a transport plan between the links at v with supplies and demands j\_f and the diagonal forbidden. Symmetrizing gives a symmetric M^v ≥ 0 with zero diagonal and row sums j\_f.

*A circulation.* Give each orientation (dart) of a link f the weight j\_f/2, and let the dart arriving at v along f pass to the dart leaving v along f′ ≠ f with weight M^v\_{ff′}/2. This is a circulation on the darts, hence a nonnegative combination Σ\_C w\_C[C] of closed walks in which consecutive links differ, with Σ\_C w\_C|C| = Σ\_f j\_f and Σ\_C w\_C n\_e(C) = j\_e, where n\_e(C) counts the traversals of e.

*Each walk.* Cut a walk C with n\_e(C) ≥ 1 at its traversals of e = uw. Each piece avoids e and is nonempty. A piece that returns to its starting endpoint is a closed walk with consecutive links distinct, so it contains a cycle and has length at least g; a piece joining u and w contains a path, which with e forms a cycle, so it has length at least g − 1. Hence |C| ≥ g·n\_e(C), and summing gives Σ\_f j\_f ≥ g·j\_e.

*The Casimir.* Every nonzero spin is at least 1/2, so j\_f(j\_f + 1) ≥ (3/2)j\_f, which gives c\_j ≥ (3/2)Σ\_f j\_f and the remaining inequalities. The equality case is j = 1/2 on a cycle of length g. ∎

The workbench's F7 is the case g = 4 on the cubic lattice, proved there from the absence of triangles. The inequality was checked exhaustively over half-integer spins with vertex singlets on the cube graph, K₃,₃, the 5-cycle, the Petersen graph, the 6-cycle and a triangle, and by linear programming over real weights on thirteen graphs of girth 3 to 8 (among them the Petersen, Heawood, McGee and Tutte–Coxeter graphs, the dodecahedron and the box {−1, 0, 1}³), on three parallel links and on the bridge between two triangles. On every link that lies on a shortest cycle the optimum is the girth, and on the bridge it is 4, larger than the girth 3.

**Remark 2.3 (the exact constant for each link).** For a link e = uw let g\_e be the length of a shortest cycle through e (∞ if none) and ℓ\_x the length of a shortest closed walk at x in the graph without e in which consecutive links differ, except possibly the last and the first. Then Σ\_f j\_f ≥ γ\_e j\_e with γ\_e = min(g\_e, 1 + (ℓ\_u + ℓ\_w)/2) ≥ g, and γ\_e is attained by half-integer spins with vertex singlets.

*Proof.* Cut each walk of the circulation at its traversals of e as above. A piece joining u and w has length at least g\_e − 1; a piece returning to its starting endpoint x has length at least ℓ\_x, and since C is closed the returning pieces come in pairs, one at u and one at w. Hence |C| ≥ n\_e(C)γ\_e. For attainment, spin 1/2 on a shortest cycle through e gives g\_e; for the other value take C = eP\_we⁻¹P\_u with P\_w, P\_u shortest walks of the kind defining ℓ\_w, ℓ\_u, and j\_f = n\_f(C)/2. ∎

**Lemma 2.4 (ground-state transform; F33–F36).** Let Γ(f, h) = Σ\_{e,a}(X\_{e,a}f)(X\_{e,a}h), P\_H the Haar mean and Q\_H = I − P\_H. For real or complex v, e^v is an eigenfunction of H\_L with eigenvalue E if and only if Kv = ξS + Q\_HΓ(v, v) and E = κ(2M\_Lξ − P\_HΓ(v, v)); then (H\_L − E)(e^vh) = κe^v(Kh − 2Γ(v, h)) for every h.

*Proof.* From X²(e^vh) = e^v(h(Xv)² + 2(Xv)(Xh) + hX²v + X²h) one gets K(e^vh) = e^v(h(Kv − Γ(v, v)) − 2Γ(v, h) + Kh). With h = 1, H\_Le^v = Ee^v exactly when Kv − Γ(v, v) − ξS is constant, and taking Haar means identifies the constant. The identities are algebraic, so they hold for complex v and ξ; only the positivity of e^v, used for the ground state, needs v real. ∎

With v₁ = S/3 (each W\_p has Casimir 3) and B = K⁻¹Q\_HΓ, the vacuum equation is v = ξv₁ + B(v, v), with formal solution Σξⁿvₙ, vₙ = Σ\_{i+j=n}B(v\_i, v\_j); this is the coupled-cluster ansatz of [SZH].

**The analytic core (F4–F32; verified).** In the Fourier-algebra norm ‖f‖\_X = Σ\_j‖A\_j(f)‖₁, which is submultiplicative [Ey], and in local weighted norms m(·), t(·), ‖·‖\_loc anchored at a link, one has ‖B(f, h)‖\_loc ≤ 3(m(f)t(h) + m(h)t(f)) ≤ (2/3)‖f‖\_loc‖h‖\_loc, by Lemma 2.2. With q₅ = Σ\_{i≤5}ξ^iv\_i, the residual ξv₁ + B(q₅, q₅) − q₅ has degrees 6–10 and local norm at most δ₅(ξ), and J₅ = 2B(q₅, ·) has norm at most ℓ₅(ξ). For 0 < ξ ≤ α₅ a Neumann inverse and a binary-tree majorant give v = q₅ + w with ‖w‖\_loc ≤ w∗ = (3/4)(1 − ℓ₅ − √𝒟₅), the small root of (2/3)w² − (1 − ℓ₅)w + δ₅ = 0. The bounds are uniform in the box: each vₙ is a sum of universal cluster functions over plaquette multisets, so the anchored sums of the infinite lattice bound every box, and the orientation dependence of the norm is handled by the maximum over the eight axis reflections.

**Proposition 2.5 (spectral return; F35–F37).** Under the analytic core, every eigenvalue λ > 0 of H\_L − E₀ on the physical space satisfies λ ≥ κd₅(ξ).

*Proof.* Let φ be a physical eigenvector, h = φ/ψ and h′ = Q\_Hh ≠ 0. By Lemma 2.4, (K − λ/κ)h′ = 2Q\_HΓ(v, h′), and ‖Kh′‖\_X is finite (F36). If λ/κ ≥ 3 there is nothing to prove, since d₅ ≤ 3. Otherwise c\_j ≥ 3 on every nonconstant physical block (Lemma 2.2), so ‖(K − λ/κ)h′‖\_X ≥ (1 − λ/(3κ))‖Kh′‖\_X. The core gives ‖2Γ(v, h′)‖\_X ≤ 4t(v)‖Kh′‖\_X ≤ χ‖Kh′‖\_X with χ = 4Σt\_iξ^i + (2/3)w∗, and Q\_H does not increase ‖·‖\_X. Hence λ ≥ 3κ(1 − χ), and substituting w∗ gives 3(1 − χ) = d₅(ξ). ∎

Nothing in this argument uses the truncation order, which gives the following.

**Corollary 2.6 (the gap at every truncation order; generalized here).** For 1 ≤ N ≤ 5 define ℓ\_N, δ\_N, 𝒟\_N, α\_N and d\_N as above with 5 replaced by N and the residual degrees i + j ≥ N + 1. If (m\_i, t\_i), i ≤ N, bound the local norms of the first N vacuum coefficients, then Δ\_L ≥ κd\_N(ξ) for every L ≥ 2, a > 0 and 0 < ξ ≤ α\_N, and d\_N decreases on [0, α\_N]. In particular:

- (a) N = 1: 𝒟₁(ξ) = 1 − 256ξ/3 exactly and (3/2)m₁ − 6t₁ = 0, so Δ\_L ≥ (3/2)κ(1 + √(1 − 64/(3g⁴))) for all g² ≥ 8/√3 ≈ 4.6188, with 2.0745κ at g² = 5 and 2.8304κ at g² = 10.
- (b) N = 2: with the workbench's pair (m₂, t₂) = (5834/39, 137/6), the threshold is g² ≥ 4.0186791538833… with Δ\_L ≥ 1.52094κ. With the recomputed values rounded up to (134.0674, 19.7954), the threshold is g² ≥ 3.97807… with Δ\_L ≥ 1.52054κ on that range and Δ\_L ≥ 1.64707κ at g² = 4.
- (c) N = 4: g² ≥ 3.7159603625…, with d₄(1/64) = 1.898118.

*Proof.* Replace q₅ by q\_N in the core. The residual is Σ\_{i,j≤N, i+j≥N+1}ξ^{i+j}B(v\_i, v\_j), of local norm at most δ\_N, and ‖2B(q\_N, ·)‖ ≤ ℓ\_N. On [0, α\_N], ℓ\_N < 1, since ℓ\_N(ξ₁) = 1 would give 𝒟\_N(ξ₁) < 0. The Neumann inverse and Proposition 2.5 give λ ≥ κd\_N(ξ), and differentiating the quadratic for w∗ gives w∗′√𝒟\_N = δ\_N′ + ℓ\_N′w∗ > 0, so d\_N decreases. For N = 1, (m₁, t₁) = (64/3, 16/3) gives the closed form. ∎

The recomputed order-2 values have closed forms m(v₂) = 6 + 11200/117 + 112/9 + 448√3/39 and t(v₂) = 3/2 + 80/9 + 256/39 + 64√3/39, which agree with the tensor computation to ten digits. So the qualitative content of Theorem 2.1, a gap on the whole physical space uniform in the box and the spacing, holds with verified inputs for g² ≥ 3.9781, which includes the benchmark g² = 4; orders 3–5 lower the threshold to 3.6836 and raise the constants. Part (a) is the workbench's own order-1 theorem of its 14–16 September continuation, and (b) strengthens its single-norm order-2 theorem (threshold ≈ 4.1156).

**Corollary 2.7 (the gap on the full space; new).** Under the hypotheses of Corollary 2.6, every eigenvalue λ > 0 of H\_L − E₀ on the whole space L², not only the physical space, satisfies λ ≥ (1/4)κd\_N(ξ). This is sharp at ξ = 0, where the gap on L² is (3/4)κ: one link in spin 1/2.

*Proof.* The positive ground state is unique on L² as well. Lemma 2.4 holds for every h, and the bound ‖2Γ(v, h)‖\_X ≤ 4t(v)‖Kh‖\_X uses only Σ\_e j\_e ≤ (2/3)c\_j, which holds on every block. On L² the nonconstant blocks have c\_j ≥ 3/4 instead of 3, so the proof of Proposition 2.5 gives λ ≥ (3/4)κ(1 − χ) = (1/4)κd\_N. ∎

**Proposition 2.8 (the gap at complex coupling; new).** Suppose the inputs of Corollary 2.6 are valid through order N, and let ζ ∈ ℂ with |ζ| ≤ α\_N. For every L ≥ 2, on the physical space:

1. H\_L(ζ)e^{v(ζ)} = E₀(ζ)e^{v(ζ)} with E₀(ζ) = κ(2M\_Lζ − P\_HΓ(v, v)), analytic in |ζ| < α\_N;
2. every other eigenvalue E₀(ζ) + λ of H\_L(ζ) has Re λ ≥ κd\_N(|ζ|);
3. E₀(ζ) is algebraically simple.

Hence the ground-state Riesz projection of H\_L(ζ) is analytic in |ζ| < α\_N, for every L.

*Proof.* (1) The fifth-reference manuscript states the core for complex ξ with |ξ| ≤ α, and Lemma 2.4 holds for complex v; the vₙ and w are analytic in ζ, being locally uniform limits of polynomials. (2) For an eigenvector with eigenvalue E₀ + λ, λ ≠ 0, put h′ = Q\_H(e^{−v}φ) ≠ 0; then (K − λ/κ)h′ = 2Q\_HΓ(v, h′). On blocks with c\_j ≥ 3, |c\_j − λ/κ| ≥ c\_j(1 − Re λ/(3κ)) if Re λ ≥ 0, and |c\_j − λ/κ| ≥ c\_j if Re λ < 0. With χ < 1 the case Re λ < 0 is impossible, and otherwise Re λ ≥ 3κ(1 − χ). (3) With λ = 0 the same argument gives h′ = 0; a generalized eigenvector e^vh with (H\_L − E₀)(e^vh) = e^v would give Kh′ = 2Q\_HΓ(v, h′), so h′ = 0 and then 0 = 1. The family H\_L(ζ) is holomorphic of type (A) with compact resolvent, and the simple eigenvalue is separated by a strip, so its Riesz projection is analytic [Ka, Ch. VII]. ∎

By contrast, the global perturbative route certifies only |ζ| < 3/(4M\_L), at most 1/320 (Proposition 6.1).

The proof of Theorem 2.1 uses the Hamiltonian, its Fourier calculus and the computed coefficients. The Jacobian, Navier–Stokes and S⁶ inputs of the workbench enter other results, described in §5.

## 3. Heat flow and the complementary physical space

The second manuscript of the latest edition (H1–H34) uses the control of the vacuum for two further purposes: box-independent bounds on the heat correlations of plaquettes, and bounds on how much the plaquette family mixes with the rest of the physical space.

**Objects.** Let A = H\_L − E₀ on the centred physical space and ρ = ψ². The centred plaquette states and their heat correlations are r\_p = (W\_p − ⟨W\_p⟩\_ρ)ψ and Ĉ\_pq(τ; ξ) = ⟨r\_p, e^{−τA/κ}r\_q⟩, τ = κt. The row norm is ‖B‖\_row = max\_p Σ\_q|B\_pq|. C₀, C₂, C₄ are the coefficients of ξ⁰, ξ², ξ⁴ in Ĉ, computed by the workbench. In the coordinates f ↦ ψf, Lemma 2.4 turns A/κ into K − D\_v with D\_vh = 2Γ(v, h), and ‖D\_vh‖\_X ≤ χ‖Kh‖\_X with χ as in Proposition 2.5, so 3(1 − χ) = d₅(ξ).

**Theorem 3.1 (heat remainder; H13, prefactor improved here).** For every L ≥ 2, every τ ≥ 0 and every |ξ| < 1/55,

  ‖Ĉ(τ; ξ) − C₀(τ) − ξ²C₂(τ) − ξ⁴C₄(τ)‖\_row ≤ (2829/13) e^{−13τ/8} (55|ξ|)⁶/(1 − (55|ξ|)²).

The workbench states this with the prefactor 67896/169 = 401.75… in place of 2829/13 = 217.61…; its bound is also valid.

*Status.* Conditional on the analytic core of Theorem 2.1, hence on the same order-3 to order-5 inputs. Every constant is re-derived below; the semigroup construction (H5–H7) and the continuation to complex ξ were read, and Proposition 2.8 gives the spectral side of that continuation.

*Proof.* (i) *The mean and the semigroup.* Put T = Q\_HD\_vK⁻¹ and p = P\_HD\_vK⁻¹ on the nonconstant physical coefficients. Since ‖·‖\_X adds the scalar and the nonconstant parts, |py| + ‖Ty‖\_X ≤ χ‖y‖\_X, so S = (I − T)⁻¹ exists with ‖S‖ ≤ 1/(1 − χ), and the mean is μ(F) = P\_HF + pSQ\_HF. The additive form of the inequality gives |(μ − P\_H)F| ≤ χ‖Q\_HF‖\_X, sharper than the workbench's χ‖Q\_HF‖\_X/(1 − χ): with y = Q\_HF and z = Sy one has z = y + Tz, so |pz| ≤ χ‖z‖\_X − ‖Tz‖\_X ≤ χ‖y‖\_X − (1 − χ)‖Tz‖\_X ≤ χ‖y‖\_X. For L₀ = (I − T)K and h > 0, ‖(I + hL₀)f‖\_X ≥ (1 + 3h(1 − χ))‖f‖\_X by Lemma 2.2, and with the range condition (H5) the Lumer–Phillips theorem [LP] gives E(τ) = e^{−τL₀} with ‖E(τ)‖ ≤ e^{−3(1−χ)τ}.

(ii) *A formula for the correlations.* With h\_τ = K⁻¹SE(τ)W\_p and G\_z = Σ\_q z\_qW\_q, |z\_q| ≤ 1, the Poisson equation (H3) and one integration by parts give Σ\_q z\_qĈ\_pq(τ) = μΓ(h\_τ, G\_z), with ‖Kh\_τ‖\_X ≤ (8/(1 − χ))e^{−3(1−χ)τ}.

(iii) *Evenness.* The map U\_{(n,i)} ↦ (−1)^{Σ\_{k<i}n\_k}U\_{(n,i)} multiplies each link by a central element, preserves the Haar measure, K and the gauge action, and sends every W\_p to −W\_p. It conjugates H\_L(ξ) to H\_L(−ξ) plus a constant, so Ĉ(τ; −ξ) = Ĉ(τ; ξ) and only even powers occur (checked on all 240 faces of the box L = 2).

(iv) *Cauchy's estimate.* By Proposition 3.2 below, on the circle |ζ| = 1/55 every phase-weighted row sum of Ĉ(τ; ζ) is at most (2829/13)e^{−13τ/8}; so the coefficient of ζ²ⁿ has row norm at most (2829/13)e^{−13τ/8}55²ⁿ, and summing over n ≥ 3 gives the tail. ∎

**Proposition 3.2 (the constants; H9–H12).**

1. ‖Γ(h, G\_z)‖\_X ≤ 32‖Kh‖\_X.
2. |P\_HΓ(h, G\_z)| ≤ (1/8)‖Kh‖\_X.
3. ‖Ĉ(τ)‖\_row ≤ ((1 + 255χ)/(1 − χ)) e^{−3(1−χ)τ}, and a fortiori the workbench's (1 + 255χ)/(1 − χ)² e^{−3(1−χ)τ}.
4. At |ξ| = 1/55 one has 1/55 < α₅ and d₅(1/55) = 1.637… > 13/8, so χ < 11/24; the prefactor is at most (1 + 255·11/24)/(13/24) = 2829/13 and the rate at least 13/8.

*Proof.* (1) By (F10), ‖Γ(h, G)‖\_X ≤ 2t(G)‖Kh‖\_X. W\_q has one Fourier block, spin 1/2 on the four links of q, with coefficient trace norm 2³ = 8 (F12); a link lies on at most four plaquettes, so t(G\_z) ≤ 4·(1/2)·8 = 16. (2) Integration by parts gives P\_HΓ(h, G\_z) = 3Σ\_q z\_q∫hW\_q, and the component a\_q of h on the line ℂW\_q contributes 3·8|a\_q| to ‖Kh‖\_X. (3) μΓ = P\_HΓ + (μ − P\_H)Q\_HΓ, and step (i), (2) and (1) give |μΓ(h\_τ, G\_z)| ≤ ((1 − χ)/8 + 32χ)‖Kh\_τ‖\_X ≤ ((1 + 255χ)/(1 − χ))e^{−3(1−χ)τ}. (4) is checked in exact rational arithmetic. ∎

**Other radii (generalized here).** Nothing in the proof uses R = 1/55 except the numbers of Proposition 3.2(4). For every 0 < R ≤ α₅ the same proof gives Theorem 3.1 with 55|ξ| replaced by |ξ|/R, the prefactor by C(R) = (1 + 255χ\_R)/(1 − χ\_R) and the rate by d₅(R), where χ\_R = 1 − d₅(R)/3. At R = 1/55 the exact χ\_R = 0.45412… gives the prefactor 213.97… and the rate 1.6376…; at R = α₅ the prefactor is 241.99… and the rate 1.5453…; at R = 45/4096, the radius of the earlier edition's bound U29b, the prefactor is 85.00… and the rate 2.2588…, which supersedes U29b (prefactor 6184/25, rate 15/8). At ξ = 0 one has C₀(τ) = e^{−3τ}I exactly.

**Relaxation into the whole complementary space.** Let R be the map with columns r\_p and Φ = κA⁻¹R, with Grams G₀ = R∗R, G₁ = R∗Φ, G₂ = Φ∗Φ, energy E = κG₁ and K\_o = κ⁻¹R∗AR. Put P = ΦG₂⁻¹Φ∗, Q = I − P, B\_Φ = QR and D\_Q = QAQ on Q𝓗₀. Allowing the family Φc to relax into every h ∈ Q𝓗₀ gives E\_full = E − κ²B\_Φ∗D\_Q⁻¹B\_Φ and G\_full = G₂ + κ²B\_Φ∗D\_Q⁻²B\_Φ.

**Proposition 3.3 (relaxation bounds; H20–H29).** Suppose ‖G\_k − 3^{−k}I‖ ≤ w\_k (k = 0, 1, 2), ‖K\_o − 3I‖ ≤ w\_K, 0 ⪯ J = G₀ − 6G₁ + 9G₂ ⪯ βI and A ≥ κd\_ph. Put l\_k = 3^{−k} − w\_k > 0, u\_k = 3^{−k} + w\_k and u\_K = 3 + w\_K. Then:

1. the fraction of each Φc seen by the plaquette states is at least max{l₁²/(u₀u₂), 1 − β/(9l₂)};
2. (1 − η\_E)E ⪯ E\_full ⪯ E and G₂ ⪯ G\_full ⪯ (1 + η\_G)G₂, with η\_E = β/(d\_ph l₁) and η\_G = β/(d\_ph² l₂);
3. the energy of (I − P\_R)Φc is at most (u₁u\_K/l₀² − 1) times c∗Ec.

*Proof.* (1) ‖P\_RΦc‖² = c∗G₁G₀⁻¹G₁c ≥ (l₁²/u₀)|c|² and ‖Φc‖² ≤ u₂|c|². For the second bound (new here): G₁ is symmetric, so J = (R − 3Φ)∗(R − 3Φ) and ‖(I − P\_R)Φc‖² ≤ ‖Φc − Rc/3‖² ≤ β|c|²/9, while ‖Φc‖² ≥ l₂|c|². (2) B\_Φ∗B\_Φ = G₀ − G₁G₂⁻¹G₁ is the least value of (R − ΦX)∗(R − ΦX), and X = 3I gives J; with D\_Q ⪰ κd\_ph the bounds follow. (3) Since AΦ = κR, the mixed energy is κc∗G₁c, and expanding gives κc∗(G₁G₀⁻¹K\_oG₀⁻¹G₁ − G₁)c ≤ (u\_Ku₁/l₀² − 1)κc∗G₁c. ∎

**Proposition 3.4 (the kinetic rows; H14, derived here).** For each plaquette p:

1. Γ(W\_p, W\_p) = 3 − χ₁(U\_p), of norm 3 + 27 = 30;
2. for each of the 12 plaquettes q adjacent to p, Γ(W\_p, W\_q) = (3/4)P₀ − (1/4)P₁, where P₀, P₁ are the parts of W\_pW\_q with spin 0 and 1 on the shared link; ‖Γ(W\_p, W\_q)‖\_X is 24 for 8 of the q and 6 + 6√3 for the other 4, both below the workbench's 48; for non-adjacent q ≠ p, Γ(W\_p, W\_q) = 0;
3. hence Σ\_q|μΓ(W\_p, W\_q)| ≤ 3 + χ(27 + 192 + 24 + 24√3) < 134 for χ < 11/24, against the workbench's 606.

*Proof.* From 2Γ(f, h) = (c\_f + c\_h)fh − K(fh) for block eigenfunctions (F17): W\_p² = 1 + χ₁(U\_p), and χ₁(U\_p) has Casimir 8 and norm 3³ = 27; for adjacent faces 2Γ = 6(P₀ + P₁) − (9/2)P₀ − (13/2)P₁, and the trace norms of P₀, P₁ are (16, 48) for two thirds of the adjacent pairs and (8, 24√3) for the rest (computed from explicit SU(2) tensors). Non-adjacent faces share no link. ∎

**Proposition 3.5 (the benchmark tables; H5).** From the workbench's inherited degree-2 and degree-4 row bounds and the constants C = 67896/169, C\_J and 606, Proposition 3.3 gives, for every L ≥ 2 and a > 0:

| Coupling | Observed fraction | Energy loss η\_E | Gram increase η\_G |
|---|---|---|---|
| g² ≥ 10 | > 0.9778 | < 0.01057 | < 0.01123 |
| g² ≥ 12 | > 0.9975 | < 0.00115 | < 0.00120 |
| g² ≥ 25/2 | > 0.9984 | < 0.00071 | < 0.00073 |
| g² ≥ 13 | > 0.99904 | < 0.000436 | < 0.000451 |
| g² ≥ 16 | > 0.99991 | < 0.0000357 | < 0.0000364 |

This reproduces the workbench's table: at g² ≥ 13 the energy loss and the Gram increase are below 1/2000, and at g² ≥ 16 below 1/25000. With the sharper constants of this record (the prefactor 2829/13, the leakage prefactor C\_J·13/24 = 782.29…, the kinetic bound 134 and the second bound of Proposition 3.3(1)) the same computation gives:

| Coupling | Observed fraction | Energy loss η\_E | Gram increase η\_G |
|---|---|---|---|
| g² ≥ 10 | > 0.99458 | < 0.005713 | < 0.006053 |
| g² ≥ 12 | > 0.99940 | < 0.000623 | < 0.000647 |
| g² ≥ 25/2 | > 0.99963 | < 0.000380 | < 0.000394 |
| g² ≥ 13 | > 0.99977 | < 0.000237 | < 0.000244 |
| g² ≥ 16 | > 0.999981 | < 0.0000194 | < 0.0000198 |

*Status.* Recomputed in exact rational arithmetic from the stated inputs; at g² = 13, with the workbench's d\_ph = 29047/10000, the first table agrees with its diagnostics to ten digits. Conditional on the inherited row bounds and on the inputs of Theorem 2.1. The widths are monotone in ξ, so each row holds for all larger g².

**Proposition 3.6 (an upper bound on the gap; new).**

1. For every L ≥ 2, a, g > 0 and every plaquette p,
  Δ\_L ≤ κ (3 − ⟨χ₁(U\_p)⟩\_ρ)/(1 + ⟨χ₁(U\_p)⟩\_ρ − ⟨W\_p⟩\_ρ²).
2. With the widths of Proposition 3.3, Δ\_L/κ ≤ (3 + w\_K)/(1 − w₀); with the constants above the gap lies in [2.8382, 3.0055]κ for g² ≥ 10, in [2.9047, 3.00024]κ for g² ≥ 13 and in [2.9372, 3.00003]κ for g² ≥ 16, the lower ends being d₅(ξ) under the inputs of Theorem 2.1.
3. At each fixed L the first-order term of Δ\_L at ξ = 0 vanishes, and Δ\_L ≤ 3κ + O(ξ²) uniformly in L; every lower bound d\_N is 3 − 64ξ + O(ξ²), so its first-order loss is a feature of the method.

*Proof.* (1) r\_p is gauge invariant and orthogonal to ψ; by min–max, Δ\_L ≤ q\_A(r\_p)/‖r\_p‖², with q\_A(r\_p) = κ(3 − ⟨χ₁⟩\_ρ) by Proposition 3.4(1) and ‖r\_p‖² = 1 + ⟨χ₁⟩\_ρ − ⟨W\_p⟩\_ρ². (2) The two quantities are (K\_o)\_pp ≤ 3 + w\_K and (G₀)\_pp ≥ 1 − w₀. (3) At ξ = 0 the eigenvalue 3κ has eigenspace spanned by the W\_p (by Lemma 2.2, c\_j = 3 only for spin 1/2 on a 4-cycle); the first-order matrix ⟨W\_q, SW\_{q′}⟩ vanishes because in each product W\_qW\_rW\_{q′} of faces some link occurs exactly once in spin 1/2, and ∫W\_q³ = 0; the ground energy has no first-order term since ∫S = 0; and d\_N′(0) = −64. ∎

**Heat horizons, support quotients and the spatial limit.** Replacing Φ by Φ\_T = (I − e^{−TA})Φ changes the Grams by factors between (1 − ε)² and 1 with ε = e^{−κd\_ph T}; for a signed sum of log det terms of total rank B the error is at most 2Bε/(1 − ε), and T = (κd\_ph)⁻¹log(1 + 2B/η) makes it at most η (H33; the choice of T checked here). The support quotients (H31–H32) and the spatial limit at fixed spacing (H34, an outline) are not verified here; H34 builds, from the box-independence of Theorem 3.1, the infinite-volume heat semigroup, its invariant state and the relaxation bounds at fixed a and g.

## 4. The earlier editions

The gap and heat bounds of the continuations of 14–21 September are superseded by §§2–3; their other calculations remain in the record as dated editions.

- **14–16 September** (the 297-page web continuation). A gauge-native order-1 theorem (G22, G26–G29) with Δ\_L > 2.07445κ at g² ≥ 5, which is Corollary 2.6(a); a single-norm order-2 theorem (R10) for g² ≥ 4.1156, strengthened by Corollary 2.6(b); and an order-2 theorem (L17) for g² ≥ 3.8260, which uses a computed bound 944984/351 for the cubic term of the residual that is not verified here. One arithmetic line of this edition justifies its self bound 40/27 by "38/81 + 1564/810 = 40/27", whose left side equals 12/5; the value 40/27 = 3·(1/81)·8 + 15·(1/810)·64 is correct for the self cluster, so the bound stands.
- **17 September** (the 49-page quartic cube reader). The fourth-order vacuum source in two presentations, equal as polynomials (78 representatives, 8,621 anchored multisets); the sixth-order vacuum energy with the cube contribution −83/1944; and Δ\_L > 1.6584κ for g² ≥ 15/4, which is Corollary 2.6(c) at ξ = 4/225 (Theorem 2.1 gives d₅(4/225) > 1.6993 there).
- **18–19 September.** The sixth vacuum source, the eighth-order energy and a response estimate on the 240 faces of the box L = 2; the workbench records that the new spatial tables and the final execution package were not supplied. Not verified here.
- **21 September, heat and volume** (the 46-page reader). The fourth-order heat coefficients (84 time functions over 17 geometric cases), a heat remainder on |ξ| < 3/256, the spatial limit at fixed spacing, and the full-complement energy retained above 999/1000 at g² ≥ 16; superseded quantitatively by §3.

**The foundations of 8–9 September.** Three manuscript lines contain the workbench's first results, stated for the full finite Hamiltonian with open boundaries and all gauge constraints. The quantum line (79 pages) has exact extensive blocking maps, volume-independent lower bounds on the high-energy spectral weight of selected dressed Wilson-loop channels, a first volume-uniform gap Δ ≥ κ(3 − 512ξ) for 0 < ξ ≤ 1/49152 (its §10, proved there with the creation method of [Ya]), a nonzero non-Abelian vertex on the box L = 2, and the Jacobian-map and Navier–Stokes branches. The spatial line (129 pages) studies sequences in which box, spacing and coupling vary together. The volume line (81 pages) has local electric moments at every coupling, the exact free physical threshold 3κ, and estimates on the S⁶-derived cusp at 0 < ξ ≤ 10⁻¹⁶. Apart from the items treated in this record, these lines are not verified here.

**Proposition 4.1 (the first volume-uniform gap is implied).** For 0 < ξ ≤ 3/256, d₁(ξ) ≥ 3 − 128ξ. So the quantum line's Δ ≥ κ(3 − 512ξ) on 0 < ξ ≤ 1/49152 follows from Corollary 2.6(a), which holds on the larger range ξ ≤ 3/256 (g² ≥ 8/√3).

*Proof.* With y = 256ξ/3 ∈ (0, 1], d₁(ξ) = (3/2)(1 + √(1 − y)) ≥ (3/2)(2 − y) = 3 − 128ξ, since √s ≥ s on [0, 1]. ∎

## 5. The typed maps from the side branches

Three branches of the workbench bring material from outside lattice gauge theory into the Hamiltonian setting, each through an explicit map. This section states each map and what is established about it.

**The Jacobian map → local-energy trial states.** The map F of Alpöge's counterexample (det DF = −2, three preimages of (−1/4, 0, 0); see the companion record on the counterexample) generates an incompressible polynomial flow, from which the workbench builds a material tensor, lattice local-energy weights and trial states, ending in its Theorem 14.2. That theorem is a valid diagonal argument, conditional on fixed-box weak-coupling limits that the file sketches. Its energy quotients equal, up to a factor 1 ± 1/(10j), the lowest free two-gluon colour-singlet energy of an open box of side j/50 at couplings g\_j < 1/j. So the map carries the Jacobian flow to trial states whose energies track the free two-gluon threshold, and the data of F enter the quotients within that window.

**Navier–Stokes → an abelian connection.** The velocity field of a solution becomes a reducible SU(2) connection A\_i = λu\_iT, with curvature density −2Σ\_{i<j}tr F\_ij² = λ²|curl u|², and gauge-invariant curvature states built from it are followed along a weak-coupling diagonal (quantum line §§20–22). The identity and the constants of the curvature masses are verified. The zero-quotient diagonal exists along couplings g → 0 and rests on rate bounds for the Navier–Stokes solution; those rates are derived, conditionally on four named statements of OpenAI's manuscript, in the companion record on the Navier–Stokes workbench (its Theorem 3.1). The manuscript's main theorem is not verified here.

**S⁶ → a magnetic background.** The spatial and volume lines use the imaginary-period block of the regular-fibre period matrix of the S⁶ construction [A] to build a magnetic background, magnetic link transports and a gauge-covariant map into the Wilson Hilbert space. On the patch these lines use, the period data enter through the single positive number D = L\_Tq\_T + 6m\_T², with L\_T = Im τ\_T, q\_T = −Im β\_T and m\_T = Im μ\_T, through the angle θ = 2πa²/D. The global statement of [A] is not verified here; the monodromy of the same period system is the subject of the companion record on the S⁶ monodromy.

**Zeta → the heat edition.** The zeta programme's Gram-sandwich lemma, (1 − δ)²Φ∗Φ ⪯ Φ\_J∗Φ\_J ⪯ (1 + δ)²Φ∗Φ when ‖(Φ\_J − Φ)x‖ ≤ δ‖Φx‖ and δ ≤ 1, is used in the 21 September heat edition with δ = e^{−Tλ₀} from the heat semigroup; its steps are verified, and the condition δ ≤ 1 is necessary for the lower bound. **Collatz → a regression fixture.** The identity X\_v − X\_u = (q − 3)(q + 4)/32 is used as a regression fixture; it is verified.

---

# Part B. Proved limits of specific routes

## 6. The global perturbative route and the continuum path

**Proposition 6.1 (the collapse of the global analyticity disk; spatial line §27, generalized here).** Write H = (2g²/a)(H₀ − ξW\_L) + const on the full space, with H₀ = Σ\_e E\_e the sum of the link Casimirs and W\_L = Σ\_p W\_p. The operator-norm Neumann series certifies the isolated rank-one ground-state projection on the circle |z| = 3/8 exactly for |ξ| < 3/(16M\_L) = 1/(64L²(2L + 1)), and on no contour separating 0 from the rest of the spectrum does the norm-product criterion give more. On the physical space the same route gives exactly |ξ| < 3/(4M\_L), on the circle |z| = 3/2.

*Proof.* |W\_p| ≤ 2 with equality at U ≡ I, so ‖ξW\_L‖ = 2|ξ|M\_L, also on the physical space (the indicator of the gauge-invariant set {W\_L > 2M\_L − ε} is a physical vector). The spectrum of H₀ lies in {0} ∪ [3/4, ∞), so ‖(H₀ − z)⁻¹‖ ≤ 8/3 on |z| = 3/8, and both factors are attained. Any separating contour crosses (0, 3/4), where the resolvent norm is at least 8/3. On the physical space the spectrum of H₀ lies in {0} ∪ [3, ∞) by Lemma 2.2, which gives the resolvent norm 2/3 on |z| = 3/2 and the radius 3/(4M\_L). ∎

The radius shrinks with the box, so at any fixed coupling this route eventually fails. It does not bound the true analyticity radius, which by Proposition 2.8 is at least α\_N uniformly in the box under the inputs of Corollary 2.6. The comparison explains why the workbench's proof uses local norms: at L = 2 the global route certifies only |ξ| < 1/1280 on the full space and |ξ| < 1/320 on the physical space, far inside α₅ ≈ 1/54.3.

**Proposition 6.2 (the standing continuum path leaves the domain).** Write c = 1/g², so ξ = c²/4 and ξ ≤ α₅ exactly when c ≤ 2√α₅ = 0.27147…. On the workbench's standing path a\_n = a₀2^{−n}, c\_n = g₀^{−2} + βn log 2 with β > 0, the condition fails for every n > (2√α₅ − g₀^{−2})/(β log 2); so at most 1 + ⌊(2√α₅ − g₀^{−2})/(β log 2)⌋ points of the path lie in the domain, and every point in the domain has spacing a\_n ≥ a₀e^{−2√α₅/β}.

*Proof.* c ↦ c²/4 is increasing, and c\_n increases linearly without bound; a point in the domain has n ≤ 2√α₅/(β log 2). ∎

So the estimates of §§2–3 hold along the path only down to a spacing bounded below in terms of a₀ and β; the workbench states the first part itself (§H7).

**Further limits recorded by the workbench.** Each of the following is stated in the workbench, and each concerns one method, sequence or observable:

- re-centring the elementary order-1, single-norm certificate to extend the source domain returns its old endpoint 3/256 = α₁ (§H7);
- lower bounds for dressed channels are not bounds for the whole spectral measure (quantum line §11);
- along the logarithmic coupling path the upper end of the certified spectral window of the weighted covariance diverges, which the document calls a limitation of its own estimate (volume line §26);
- the zero-quotient sequence of the Navier–Stokes branch exists only along couplings tending to 0 (§5).

In the passages read, each is stated by the workbench with the scope of its proof.

---

# Part C. Directions

## 7. The open directions, and my assessment

The workbench explored its problem the way the other programmes did: many routes, tested quickly with AI systems, some of which produced theorems and some of which mapped out what a route needs. This part states, for each open direction, what is established and my assessment.

**Locally gapped, globally gapless sequences.** The spatial line (129 pages) builds sequences in which the box, the spacing and the coupling vary together, driven by the S⁶ period data through the magnetic background of §5. Its conclusion (§28) states three results: along a fixed-coupling diagonal with g₀⁴ ≥ 12288 the magnetic excitation probability eventually has zero weight on every bounded energy interval; for fixed Wilson-loop states there is a positive high-energy mass and a failure of strong continuity; and on a selected weak-coupling diagonal the finite gaps close while the corrected magnetic probability escapes to high energy (§§17–18), with a unique-vacuum realization of a selected macroscopic limit of a second observable (§20). These are statements of the workbench and are not verified here. The aim of the direction, as the author describes it, is an object that has a gap at every finite regulator but whose continuum limit has none, because in the limit the spectrum becomes continuous; the S⁶ period data supply the background that drives the sequences, and the author proposes extending the construction to higher-dimensional period data related to the Leech lattice (not verified here). My assessment: the mechanism the spatial line exhibits, finite gaps that close along a joint limit while spectral weight escapes, is the phenomenon that separates a lattice gap from a continuum gap, so the direction is well posed. Its next requirement is a sequence of this kind whose limit satisfies the reconstruction axioms under which the continuum problem is posed [JW, §4], since the present sequences are selected diagonals (Question 7).

**Toward weak coupling.** Every result of the workbench holds at a fixed lattice spacing and strong bare coupling, and Proposition 6.2 says how far along the standing path the estimates reach. The spatial line's conclusion names the interacting local continuum and a nonzero low-energy spectral weight as its target (§28). My assessment: I think the most transferable ingredients of the present proof are Lemma 2.2, which is purely combinatorial and holds for every coupling, and the ground-state transform of Lemma 2.4, which is exact; what is specific to strong coupling is the convergence of the vacuum expansion in local norms. A route toward weak coupling would have to replace that expansion by a multiscale control of the vacuum, and the workbench's blocking maps of the quantum line are a natural starting point for that.

**Lower thresholds.** The workbench names the same-support linearized action J₅ with a preconditioned residual as its next candidate. For certificates built only from majorant series with nonnegative coefficients, Pringsheim's theorem suggests that re-centring cannot pass α\_N; the workbench's calculation shows this for N = 1. Whether signed or same-support information can pass it is Question 2.

**Independent confirmation of the inputs.** An implementation independent of the workbench's programs would remove the condition in Theorem 2.1. An independent referee computed the order-3 norms numerically with its own implementation (Clebsch–Gordan contraction over 612 anchored labels in 22 symmetry classes): m(v₃) = 1203.1424… and t(v₃) = 127.2886…, below the workbench's 1611.59 and 180.35, with the record's energy coefficient e₄ = 5M/216 − 2J/1053 reproduced exactly. If confirmed in exact arithmetic, orders 1–3 give Δ\_L ≥ κd₃(ξ) for g² ≥ 3.7154, with d₃(1/64) = 1.902 (recomputed here from the referee's values rounded up). The computation of the norms is not repeated here.

**The first-order loss.** The true gap has no first-order term (Proposition 3.6(3)), while the lower bounds lose one because the spectral return bounds 2Γ(v, h′) by 4t(v)‖Kh′‖\_X. My assessment: I think a second-order lower bound Δ\_L ≥ κ(3 − cξ²) is within reach of the same method, because the loss comes from one estimate that ignores the vanishing of the first-order perturbation on the plaquette eigenspace.

**Clustering.** If, as §H34 asserts, the coefficient of ξⁿ in Ĉ\_pq vanishes unless the face distance of p and q is at most n, then the bounds of §3 give |Ĉ\_pq(τ; ξ)| ≤ (2829/13)e^{−13τ/8}(55|ξ|)^{2⌈d(p,q)/2⌉}/(1 − (55|ξ|)²), uniformly in L. A written proof of that locality statement is open.

**The bridges.** The typed maps of §5 bring the Jacobian flow, Navier–Stokes solutions and the S⁶ period data into the Hamiltonian setting. My assessment: of these, the S⁶ map is the most economical, since it needs one positive number D, and the Navier–Stokes map is the most developed, since its rates are now derived conditionally (companion record). For the Jacobian map, the result that its trial states track the free two-gluon threshold identifies what the map produces; which properties of F would move the quotients outside the window 1 ± 1/(10j) is Question 6.

## 8. Questions

1. Can the vacuum expansion of §2 be replaced by a multiscale control that persists along a path to weak coupling?
2. Can a re-centred certificate of order N pass α\_N if it uses signed or same-support information?
3. Confirm the coefficient bounds of orders 3–5 by an independent, preferably exact, implementation.
4. Is there c > 0 with Δ\_L ≥ κ(3 − cξ²) for all L and all small ξ > 0?
5. Prove the locality statement of §H34 for the heat coefficients.
6. For the Jacobian branch, which properties of the map move the energy quotients of the trial states outside the window around the free two-gluon threshold?
7. Can a sequence of the spatial line's kind, in which finite gaps close while spectral weight escapes to high energy, be realized along a path whose limit satisfies the reconstruction axioms of the continuum problem?

## 9. Verification

The scripts are in the record's `checks/ym/` folder, with their outputs:

- `ymr_heat_constants.py` and `ymr_referee_checks.py`: the constants of Propositions 3.2 and 3.4, the tables of Proposition 3.5, the windows of Proposition 3.6, the radii family, and α\_N, d\_N and the thresholds of Corollary 2.6 by exact root isolation;
- `ym_order2_threshold.py`: the order-2 threshold 3.9781 with the rounding √3 < 1.7320509;
- `generality_checks.py` and `workbench_reader_claims_checks.py`: Lemma 2.2 on the listed graphs (exhaustive search and linear programming), the order-2 tensor norms, and Proposition 6.1;
- the order-5 replay: the workbench's producer (662 rows) and auditor, re-run with byte-identical output;
- `ymr_record_inventory.py`: the inventory of the Zenodo record by MD5.

## References

- [A] A compact complex threefold fibred by tori over the projective line, and the six-sphere, manuscript circulated by L. Alpöge, 2026.
- [Ba] J. C. Baez, Spin network states in gauge theory, Adv. Math. 117 (1996) 253–272.
- [Ey] P. Eymard, L'algèbre de Fourier d'un groupe localement compact, Bull. Soc. Math. France 92 (1964) 181–236.
- [JW] A. Jaffe, E. Witten, Quantum Yang–Mills theory, official problem description, Clay Mathematics Institute.
- [Ka] T. Kato, Perturbation Theory for Linear Operators, 2nd ed., Springer, 1976.
- [KS] J. Kogut, L. Susskind, Hamiltonian formulation of Wilson's lattice gauge theories, Phys. Rev. D 11 (1975) 395–408.
- [LP] G. Lumer, R. S. Phillips, Dissipative operators in a Banach space, Pacific J. Math. 11 (1961) 679–698.
- [O] OpenAI, Finite Time Blowup for Navier–Stokes, manuscript, 2026.
- [OS] K. Osterwalder, E. Seiler, Gauge field theories on a lattice, Ann. Physics 110 (1978) 440–471.
- [SZH] D. Schütte, Zheng Weihong, C. J. Hamer, Coupled cluster method in Hamiltonian lattice field theory, Phys. Rev. D 55 (1997) 2974.
- [Ya] D. A. Yarotsky, Quasi-particles in weak perturbations of non-interacting quantum lattice systems, arXiv:math-ph/0411042 (2004).
