# The Jacobian-conjecture counterexample of Alpöge: fibres, a torus action, a Whitney-cusp normal form, and the Weyl algebra — an audited record with new results

*Claude (Anthropic, model `claude-opus-5-5`), 27 September 2026. Published at the author's request ahead of the author's review; the author may revise or withdraw it. This record replaces the Jacobian part of note 52\_, which was withdrawn on 27 September 2026.*

## Abstract

On 20 July 2026 Levent Alpöge announced a polynomial map F: ℂ³ → ℂ³ with constant Jacobian determinant −2 that is not injective, a counterexample to the Jacobian conjecture in dimension three, crediting Akhil for the question and Fable for the work. We verify the counterexample and describe its geometry explicitly. Its fibres are the simple roots of binary cubics in an affine slice, which we realize through an explicit isomorphism with a polynomial inverse; the fibre theorem holds over every field of characteristic different from 2, so fibres have 0, 1 or 3 rational points and never 2. The map carries a one-parameter torus symmetry, and off one coordinate hypersurface it is the product of the identity on ℂ∗ with the Whitney cusp map with its critical curve removed; the discriminant becomes the classical A₂ discriminant. The commuting vector fields lifting the coordinate fields are divergence-free, and their escaping integral curve is a torus orbit. As consequences we write out an explicit non-surjective endomorphism of the Weyl algebra A₃ and the corresponding Poisson endomorphism.

## 0. Introduction

### 0.1 Why this record

The counterexample [P] settles the Jacobian conjecture in dimension three, and Tao's exposition [T] explains it through the multiplication of a linear form with a quadratic form, normalized by their resultant, on an affine slice of binary cubics. The author's research programme studies typed maps from the counterexample to other areas: singularity theory, the arithmetic of cubic forms, the Weyl and Poisson algebras, and polynomial flows. For that purpose one needs the counterexample in explicit coordinates, with its symmetries and a normal form. This record provides them, with every statement proved and checked by computer.

### 0.2 Main results

- **Theorem 2.1 and Corollaries 2.2, 2.4.** An explicit isomorphism ι of ℂ³ onto a smooth complete intersection W ⊂ ℂ⁵, with polynomial inverse, under which the fibres of F correspond to the simple roots of the slice cubic; the fibre sizes 3, 1 and 0 over the complement of the discriminant, the discriminant minus the triple-root curve, and that curve; the same trichotomy over every field with 2 invertible, and 3 or 1 real preimages according to the sign of the discriminant.
- **Theorem 2.3.** The minimal polynomials of the coordinates over ℚ[F₁, F₂, F₃]; y and w are integral, and only x can escape, only over the discriminant.
- **Theorems 3.1–3.2 and Corollary 3.3** (*new*). A torus action (λ⁻¹x, λy, λ²w) ↦ (λ²F₁, λF₂, λ⁻¹F₃), and the normal form F|\_{F₃≠0} = g × id with g the Whitney cusp map minus its critical curve, in explicit coordinates.
- **Lemma 4.1 and §4.** Divergence-free polynomial lifts of affine fields, with the escaping curve γ(τ) = z·(1, −3/2, 13/2), a torus orbit.
- **Propositions 5.1–5.2.** The explicit non-surjective endomorphism x\_i ↦ F\_i, ∂\_i ↦ D\_i of A₃, and the Poisson cotangent lift.

### 0.3 What the results mean

The normal form makes the geometry of the counterexample transparent: a fibre over a point with c ≠ 0 is the set of simple roots of a cubic, escape to infinity is a simple root running into the fold of the Whitney cusp, and the missing curve lies over the cusp point. This reduces a global phenomenon, non-injectivity with constant Jacobian, to a classical local model, and it suggests looking for higher-dimensional examples among normal forms of higher A\_k singularities (Question 2). The explicit fields and endomorphisms turn the known implications between the Jacobian, Dixmier and Poisson conjectures into concrete maps, and the integer points of F give a concrete family of reducible cubic forms (§6.1).

### 0.4 How this record was made

This is an audit of the counterexample by an AI system, carried out for the author's programme. Every statement of [P] used here was re-derived and checked by computer, and all of them hold. Statements carry one of four statuses, as in the companion papers: *verified* (proved here or re-computed by a program listed in §8), *not verified here*, *my assessment* (a view with its reasons, in the first person), and *proved negative* (with the counterexample or derivation in the text). This record replaces the Jacobian part of note 52\_, which was withdrawn on 27 September 2026.

### 0.5 Organization

Part A (§§1–4) contains the verified results: the map (§1), the fibre theorem (§2), the torus action and the normal form (§3), and the vector fields (§4). Part B (§5) records the consequences for the Jacobian, Dixmier and Poisson conjectures in dimension three. Part C (§6) describes connections to other areas with my assessment, §7 lists open questions and §8 the verification.

---

# Part A. Verified results

## 1. The map

  F₁ = (1 + xy)³w + y²(1 + xy)(4 + 3xy),
  F₂ = y + 3x(1 + xy)²w + 3xy²(4 + 3xy),
  F₃ = 2x − 3x²y − x³w.

Then det DF = −2 identically. The three points (0, 0, −1/4), (1, −3/2, 13/2) and (−1, 3/2, 13/2) all map to (−1/4, 0, 0).

## 2. Binary cubics and the fibre theorem

Attach to a point (a, b, c) ∈ ℂ³ the binary cubic f\_{(a,b,c)}(s, t) = as³ + bs²t + 4st² + 4ct³. These are the cubics with st²-coefficient 4, the slice of [T]. Put

  u = −2x,  v = 1 + xy,
  A = (1 + xy)²w + y²(4 + 3xy),
  B = x(1 + xy)w + y(1 + 3xy),
  C = 2(2 − 3xy − x²w).

**Theorem 2.1.**

1. f\_{F(x,y,w)}(s, t) = (vs − ut)(As² + Bst + Ct²).
2. Au² + Buv + Cv² = 4, the resultant normalization, and vC − uB = 4, the slice condition.
3. The map ι(x, y, w) = (u, v, A, B, C) is an isomorphism of ℂ³ onto the smooth complete intersection W = {vC − uB = 4, Au² + Buv + Cv² = 4} ⊂ ℂ⁵. Its inverse is
   - x = −u/2,
   - y = (Au + 2Bv)/2,
   - w = [(C³v − 3BC²u)(v²w) + (3B²Cv − B³u)(u²w)]/64,

   where v²w = A − y²(4 + 3xy) and u²w = 4(2 − 3xy − C/2) are polynomials on W.
4. For every cubic f in the slice, F⁻¹(f) is in bijection with the set of simple roots of f in ℙ¹.

*Proof.* (1) and (2) are polynomial identities.

(3) The composites in both orders are the identity on ℂ³ and on W; the second modulo the two equations of W. The formula for w uses 1 = ((Cv − Bu)/4)³, whose expansion lies in the ideal (u², v²). Smoothness: the two equations and the 2×2 minors of their Jacobian generate the unit ideal.

(4) Let [u₀ : v₀] be a root of f, and write f = (v₀s − u₀t)Q₀. Rescaling (u, v) = μ(u₀, v₀) divides Q₀ by μ, so Q(u, v) = μQ₀(u₀, v₀). The normalization Q(u, v) = 4 therefore has exactly one solution μ when Q₀(u₀, v₀) ≠ 0, that is, when the root is simple, and none when it is multiple. The slice condition holds automatically, since it is the st²-coefficient of f. ∎

The root belonging to a point is also [u : v] = [2(y − F₂) : 3F₁].

Let Δ = 27a²c² − 18abc + 16a + b³c − b². Then Disc(as³ + bs² + 4s + 4c) = −16Δ, and

  Δ∘F = 4AC − B² = −Disc(Q),

which is Disc(LQ) = Res(L, Q)²·Disc(Q) = 16·Disc(Q). Δ is irreducible over ℂ: it is quadratic in c with coprime coefficients, and its c-discriminant (b² − 12a)³ is not a square.

**Corollary 2.2** ([P], [T]; here in these coordinates).

1. Fibres of F have 3 points off Δ = 0, 1 point on Δ = 0 off the triple-root curve, and none on that curve.
2. The triple-root curve is Γ = {(4/(27c²), 4/(3c), c) : c ≠ 0}, the affine part of the twisted cubic, consisting of the cubics (4/(27c²))(s + 3ct)³. On Δ = 0 it is cut out by 3bc = 4. The image of F is ℂ³ ∖ Γ.
3. F is finite over Δ ≠ 0 and not proper at any point of Δ = 0. So Jelonek's set of non-properness [J] is S\_F = {Δ = 0}.
4. The monodromy of the étale cover over ℂ³ ∖ {Δ = 0} is S₃.

*Proof.* (1) and (2) follow from Theorem 2.1(4).

(3) Finiteness follows from Theorem 2.3 below. For non-properness: F is étale. Properness over a connected neighbourhood of a point of Δ = 0 would make F a finite covering there, with constant fibre size; but the fibre sizes near such a point are 3 and at most 1.

(4) The cover is connected, since its total space is the complement of a hypersurface in ℂ³. Its function field is generated by a root of as³ + bs² + 4s + 4c, which is irreducible over ℂ(a, b, c) (it is linear in c with coprime coefficients). The discriminant −16Δ is not a square, since Δ(a, 0, 0) = 16a. ∎

**Theorem 2.3 (minimal polynomials).** Over ℚ[F₁, F₂, F₃]:

- x satisfies Δ(F)x³ + (4 − 3F₂F₃)x − 2F₃ = 0, a cubic with discriminant −4Δ(27ac² − 9bc + 8)²;
- y satisfies 2y³ − 3F₂y² + 18F₁y + (27F₁²F₃ − 18F₁F₂ + F₂³) = 0;
- w satisfies an explicit cubic with leading coefficient 8.

These are the minimal polynomials. So y and w are integral over ℚ[F], and on bounded sets of the target only x can become unbounded, and only over Δ = 0.

*Proof.* Each identity is a polynomial identity in x, y, w. For y it is the root relation: f(2(Y − b), 3a) = 4a(2Y³ − 3bY² + 18aY + 27a²c − 18ab + b³).

Minimality: over the point (1, 2, 3), the three fibre points have three distinct values of x, of y and of w. The set of targets over which two fibre points share a value is a closed analytic subset of ℂ³ ∖ {Δ = 0}, and it is proper, so each coordinate takes three distinct values on a generic fibre. By transitivity of the monodromy, these three values are conjugate over ℚ(F). The square factor in the discriminant of the x-cubic marks where two fibre points share x, for example over (−8/27, 0, 1). ∎

**Corollary 2.4 (other fields).** ι and ι⁻¹ are defined over ℤ[1/2]. Hence, for every field k with 2 ∈ k^×, F⁻¹(f)(k) is in bijection with the k-rational simple roots of f. The number of k-rational points in a fibre is 0, 1 or 3, never 2: if two simple roots are rational, so is the third, which is then simple or equal to one of them.

Over 𝔽\_p the fibre-size counts are {0: 6, 1: 18, 3: 3} for p = 3, {0: 36, 1: 71, 3: 18} for p = 5, {0: 102, 1: 190, 3: 51} for p = 7 and {0: 410, 1: 716, 3: 205} for p = 11, by exhaustive computation.

Over ℝ, a target has 3 real preimages where Δ < 0 and 1 where Δ > 0. So F restricted to ℝ³ is a real polynomial map with constant Jacobian −2 that is 3-to-1 over {Δ < 0}.

## 3. A torus action and the Whitney-cusp normal form

**Theorem 3.1.** For λ ∈ ℂ∗, F(λ⁻¹x, λy, λ²w) = (λ²F₁, λF₂, λ⁻¹F₃), and Δ(λ²a, λb, λ⁻¹c) = λ²Δ(a, b, c).

On the slice of cubics this action is the substitution (s, t) ↦ (μ²s, μ⁻¹t) with μ³ = λ. It is the one-parameter subgroup of the symmetries (L, Q) ↦ (λ₁L, λ₂Q) and (L, Q) ↦ (L∘T, Q∘T) of [T] given by T = diag(α, α⁻¹), λ₁ = α⁻¹, λ₂ = α² (so λ = α²), which preserves the resultant and the slice.

*The orbit structure.*

- The curve Γ missing from the image is a single orbit, that of (4/27, 4/3, 1), the cubic (4/27)(s + 3t)³.
- The element λ = −1 fixes exactly the w-axis, and F(0, 0, w) = (w, 0, 0).
- Over the punctured a-axis, which is one orbit with stabilizer μ₂, the preimage consists of two orbits: the free orbit of (1, −3/2, 13/2), which maps 2:1, and the punctured w-axis, which maps 1:1.
- The three-point fibre over (−1/4, 0, 0) is therefore 2 + 1, and every a ≠ 0 behaves the same way.

**Theorem 3.2 (normal form).** Put n = 2 − 3xy − x²w (= C/2) and m = (1 + xy)n (= vC/2). Then

  F₃ = xn,  F₁F₃² = m(n + m − m²),  F₂F₃ = 2n + 4m − 3m².

The map (x, y, w) ↦ (c, m, n) = (F₃, m, n) is an isomorphism of U = {F₃ ≠ 0} onto ℂ∗ × ℂ × ℂ∗, with inverse x = c/n, y = (m − n)/c, w = (2 − 3(m/n − 1) − n)n²/c². On the target, (a, b, c) ↦ (P, Q, c) = (ac², bc, c) identifies {c ≠ 0} with ℂ² × ℂ∗. In these coordinates

  F|\_U = g × id\_{ℂ∗},  g(m, n) = (m(n + m − m²), 2n + 4m − 3m²),  det Dg = 2n.

Moreover g(m, n) = (P, Q) exactly when h(m) := m³ − 2m² + Qm − 2P = 0 and n = h′(m)/2.

*Proof.* The identities and both composites are polynomial identities; the solution of g(m, n) = (P, Q) is direct substitution. ∎

**Corollary 3.3.**

- Put m = m′ + 2/3 and α = Q − 4/3. Then h + 2P = m′³ + αm′ + (2Q/3 − 16/27) and n = (3m′² + α)/2. So, off {F₃ = 0} and after polynomial changes of coordinates, F is the product of the identity on ℂ∗ with the Whitney cusp map [Wh] (m′, α) ↦ (m′³ + αm′, α), restricted to the complement of its critical curve 3m′² + α = 0.
- The discriminant of h is −4(27P² − 18PQ + 16P + Q³ − Q²) = −4c²Δ. With β = 2Q/3 − 2P − 16/27 one has 4(27P² − 18PQ + 16P + Q³ − Q²) = 4α³ + 27β², the A₂ discriminant. Its cusp (P, Q) = (4/27, 4/3) is the image of the missing orbit Γ.
- The two root variables are related by m = −2c/S, where S is the root of the slice cubic: f(S, 1) = (4c/m³)·h(m).

In this form the geometry of the counterexample is transparent. A fibre of F over a point with c ≠ 0 is the set of simple roots of the cubic h. Escape to infinity is a simple root running into the fold, n → 0, where x = c/n → ∞. The missing curve lies over the cusp of the fold.

## 4. Divergence-free vector fields and escaping flows

Let D\_i = Σ\_k (DF⁻¹)\_{ki}∂\_k. Then DF·D\_i = e\_i, so D\_i is F-related to the coordinate field ∂/∂a\_i. The D\_i commute, since their bracket annihilates F₁, F₂, F₃ and the dF\_j are pointwise independent. Their coefficients are polynomials over ℤ[1/2] of total degrees 6 to 11. A computer listing of all nine coefficients accompanies this paper.

**Lemma 4.1.** Let F: ℝⁿ → ℝⁿ or ℂⁿ → ℂⁿ be polynomial with det DF ≡ c ≠ 0, let V be an affine vector field, and put U = DF⁻¹(V∘F). Then:

1. U is a polynomial vector field with div U = (div V)∘F.
2. F maps integral curves of U to integral curves of V.
3. If F has a polynomial inverse G, every maximal integral curve of U is complete, namely γ(τ) = G(Φ^V\_τ(F(γ(0)))).

*Proof.*

1. DF⁻¹ = adj(DF)/c is polynomial. The Piola identity Σ\_j ∂\_j adj(DF)\_{ji} = 0 and the chain rule give c·div U = c·(div V)(F).
2. d/dτ F(γ) = DF(γ)γ′ = V(F(γ)).
3. By (2), F∘γ is the flow line of V through F(γ(0)), which exists for all time because V is affine; apply G. ∎

In particular the D\_i are divergence-free, and so is U = DF⁻¹(2, 0, 0) = 2D₁. Its integral curve γ(τ) = (z⁻¹, −3z/2, 13z²/2), with z = √(1 − 8τ), satisfies F(γ(τ)) = (−1/4 + 2τ, 0, 0). It leaves every compact set as τ ↑ 1/8, while its image tends to (0, 0, 0) ∈ {Δ = 0}.

Along γ, the root [u : v] = [4/z : 1] of the associated cubic runs into [1 : 0], the double root of f = 4st². By Theorem 3.1, γ(τ) = z·(1, −3/2, 13/2) is the torus orbit of one of the three points over (−1/4, 0, 0).

So the finite-time escape of this divergence-free polynomial flow is a torus orbit along which a simple root collides with its partner. By Lemma 4.1(3), no polynomial automorphism admits such a curve.

---

# Part B. Proved negative results

## 5. The Jacobian, Dixmier and Poisson conjectures in dimension three

The counterexample is itself a negative result: the Jacobian conjecture JC₃ is false. This part records the consequences that follow from it by known implications, with the maps made explicit.

**Proposition 5.1.** Let K be a field of characteristic 0, and let A₃ be the Weyl algebra K⟨x\_i, ∂\_i⟩. Then x\_i ↦ F\_i, ∂\_i ↦ D\_i defines an injective ring endomorphism φ of A₃ whose image contains none of x, y, w. The same holds over ℤ[1/2].

*Proof.* [D\_i, F\_j] = D\_i(F\_j) = δ\_{ij}, [D\_i, D\_j] = 0 and [F\_i, F\_j] = 0. So φ respects the defining relations. It is injective because A₃ is simple [Co].

Commuting with F₁, F₂, F₃ forces order 0: if P has order m ≥ 1 and principal symbol σ, then the order-(m−1) symbol of [P, F\_i] gives DF·∇\_ξσ = 0, and hence σ = 0. So the centralizer of {F\_i} is K[x], and likewise that of {x\_i}.

If φ(P) = x\_i, then φ([P, x\_j]) = [x\_i, F\_j] = 0. So P ∈ K[x] by injectivity, and x\_i = P(F) ∈ K[F]. This contradicts Theorem 2.3, since x\_i takes three distinct values on a generic fibre. ∎

So the Dixmier conjecture [Di] fails for A\_n with n ≥ 3. This is the classical implication from the Dixmier conjecture to the Jacobian conjecture, recorded by Adjamagbo and van den Essen [AvdE] and credited there to Bass, Connell and Wright [BCW]. Proposition 5.1 makes the endomorphism explicit.

**Proposition 5.2.** On the Poisson algebra K[x, p] in six variables, with {p\_i, x\_j} = δ\_{ij}, the cotangent lift x\_i ↦ F\_i, p\_i ↦ Σ\_k (DF⁻¹)\_{ki}p\_k is a Poisson endomorphism and not an automorphism. As a polynomial map of ℂ⁶ it has Jacobian determinant 1 and is not injective: the three points (x\_j, DF(x\_j)ᵀ(1, 1, 1)) over (−1/4, 0, 0) have the same image.

This is the failure of the Poisson conjecture PC₃, which also follows from the implication PC\_n ⇒ DC\_n of [AvdE]. Long [L] constructed an explicit counterexample to the rank-two Poisson conjecture PC₂ from F, in four variables, using a Hamiltonian correction. That counterexample gives PC\_n false for every n ≥ 2.

The implications used here give no statement about the Dixmier conjecture for A₁ and A₂. The known implications in that range run in the other direction: Tsuchimoto [Ts] and Kanel-Belov and Kontsevich [KBK] proved that JC\_{2n} implies DC\_n, so a counterexample to DC₁ or DC₂ would give one to JC₂ or JC₄.

---

# Part C. Connections and directions

## 6. Connections

The counterexample connects to several areas through explicit typed maps. This section states what is established about each and gives my assessment.

### 6.1 Integer points and binary cubic forms

At (x, y, w) ∈ ℤ³, f\_F is an integral binary cubic form. It factors over ℤ as L·Q with L = vs − ut and Q = As² + Bst + Ct² integral, gcd(u, v) ∈ {1, 2}, and Disc(f\_F) = 16·Disc(Q) = −16Δ(F). Since Res(L, Q) = 4 ≠ 0, the ℚ-algebra of f\_F is ℚ × K\_Q, where K\_Q is the rank-2 algebra of Q, non-reduced when Disc Q = 0. Under the Delone–Faddeev correspondence, in the form extended by Gan, Gross and Savin [GGS] (see [Bh, §2]), the integer points of F thus parametrize reducible binary cubic forms and the corresponding cubic rings with a rational factor.

My assessment: I think this is a concrete arithmetic bridge, because it turns the integer points of F into a parametrization of cubic rings with a rational factor, a family for which counting methods exist [Bh]. Which rings occur, and with what density, is Question 3.

### 6.2 The normal form as a bridge to singularity theory

By Theorem 3.2 and Corollary 3.3, off {F₃ = 0} the counterexample is the Whitney cusp map with its critical curve removed, times the identity on ℂ∗. Its non-properness is the fold of the cusp, and its missing curve lies over the cusp point. My assessment: I think this is the most useful structural description for further work, because it reduces the global geometry of the counterexample to a classical local model. It suggests looking for counterexamples in higher dimensions among maps that are normal forms of higher A\_k singularities with their critical sets removed (Question 2).

### 6.3 The author's four-dimensional map

The author's programme contains a four-dimensional polynomial map P with det DP = −2, whose completed factor map has the discriminant as its exact non-proper set. That statement is not verified here. Whether P carries a torus action, and whether it has a normal form of Whitney or swallowtail type off a coordinate hypersurface, is Question 2.

## 7. Questions

1. On the hypersurface {F₃ = 0} the normal form of Theorem 3.2 does not apply. What is the local structure of F there? On that hypersurface lie the w-axis and the orbits of the points with x = 0 or n = 0.
2. Does the author's four-dimensional map P (§6.3) carry a torus action, and does it have a normal form of Whitney or swallowtail type off a coordinate hypersurface? More generally, are there counterexamples in higher dimensions that are normal forms of higher A\_k singularities with their critical sets removed?
3. The integral points of F parametrize reducible cubic forms with Res(L, Q) = 4. Which cubic rings occur, and with what density?

## 8. Verification

The scripts are in the record's `checks/jacobian/` folder, with their outputs.

- `jac52_checks.py` (40 checks) verifies:
  - the Jacobian and the three-point fibre;
  - Theorem 2.1, including both composites and the smoothness of W;
  - the discriminant identities and the irreducibility of Δ;
  - Theorem 2.3;
  - Corollary 2.2(2);
  - the escaping curve;
  - the degrees and denominators of DF⁻¹;
  - the relations [D\_i, F\_j] = δ\_{ij} and [D\_i, D\_j] = 0;
  - the Jacobian and non-injectivity of the cotangent lift;
  - Theorem 3.1, the orbit statements and the cusp.
- `ver52_referee_claims.py` verifies:
  - Theorem 3.2 and Corollary 3.3;
  - the μ₂-structure;
  - Corollary 2.4 over 𝔽₃, 𝔽₅, 𝔽₇ and 𝔽₁₁ by exhaustion;
  - the three distinct values over (1, 2, 3), at 50-digit precision.
- An independent referee, a separate Claude instance, re-derived all statements with separately written code.
- Lemma 4.1 was verified, including the Piola identity, when it was first proved.
- `jac52_weyl_witness.py` prints the fields D₁, D₂, D₃.

## References

- [P] A Counterexample to the Jacobian Conjecture, 20 July 2026, https://www.ulam.ai/research/jacobian.pdf.
- [T] T. Tao, A digestion of the Jacobian conjecture counterexample, terrytao.wordpress.com, 21 July 2026.
- [AvdE] P. K. Adjamagbo, A. van den Essen, A proof of the equivalence of the Dixmier, Jacobian and Poisson conjectures, Acta Math. Vietnam. 32 (2007) 205–214.
- [BCW] H. Bass, E. Connell, D. Wright, The Jacobian conjecture: reduction of degree and formal expansion of the inverse, Bull. Amer. Math. Soc. 7 (1982) 287–330.
- [Bh] M. Bhargava, Higher composition laws II, Ann. of Math. 159 (2004) 865–886.
- [Co] S. C. Coutinho, A Primer of Algebraic D-Modules, LMS Student Texts 33, 1995.
- [Di] J. Dixmier, Sur les algèbres de Weyl, Bull. Soc. Math. France 96 (1968) 209–242.
- [GGS] W. T. Gan, B. Gross, G. Savin, Fourier coefficients of modular forms on G₂, Duke Math. J. 115 (2002).
- [J] Z. Jelonek, The set of points at which a polynomial map is not proper, Ann. Polon. Math. 58 (1993) 259–266.
- [KBK] A. Kanel-Belov, M. Kontsevich, The Jacobian conjecture is stably equivalent to the Dixmier conjecture, Mosc. Math. J. 7 (2007) 209–218.
- [L] C. D. Long, An explicit counterexample to the rank-two Poisson conjecture, arXiv:2608.23777.
- [Ts] Y. Tsuchimoto, Endomorphisms of Weyl algebra and p-curvatures, Osaka J. Math. 42 (2005).
- [Wh] H. Whitney, On singularities of mappings of Euclidean spaces I, Ann. of Math. 62 (1955) 374–410.
