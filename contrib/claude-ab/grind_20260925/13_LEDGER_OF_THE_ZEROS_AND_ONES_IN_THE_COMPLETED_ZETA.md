# A ledger of the zeros and ones in the completed zeta function

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 06:03 UTC; §2(c)–(d) and the pivot slot in §4 added at 06:06 UTC, after the owner's description of τ as the pivot.

The owner asked that the classical "pole at 0" be tracked carefully. The word may cover several objects that the historical development merged, and the programme's τ may sit at that place, not the number 0.

This note separates every object called "0" or "1" in the classical derivation of the poles of the zeta function. For each one it derives which term or pole it produces. §1–§3 are derivations and checks. §4 is a proposal and is labelled as one.

## 1. The identity with every term kept

Let h be even and Schwartz on ℝ, with no moment conditions. Define

  ĥ(ξ) = ∫h(v)e^{−2πivξ}dv,  Σh(u) = 2Σ_{n≥1}h(nu),  M_S h(s) = ∫₀^∞h(v)v^{s−1}dv.

For Re s > 1, integrating term by term gives ∫₀^∞Σh(u)u^{s−1}du = 2ζ(s)M_S h(s).

Poisson summation over the whole lattice gives Σ_{n∈ℤ}h(nu) = u^{−1}Σ_{n∈ℤ}ĥ(n/u). Separating the two n = 0 terms:

  Σh(u) = u^{−1}Σĥ(1/u) + u^{−1}ĥ(0) − h(0).  (1)

Now split the Mellin integral at u = 1 and use (1) on (0, 1). This is Riemann's second proof of 1859, with the boundary terms kept:

  2ζ(s)M_S h(s) = ∫₁^∞Σh(u)u^{s−1}du + ∫₁^∞Σĥ(w)w^{−s}dw + ĥ(0)/(s−1) − h(0)/s.  (2)

The two integrals are entire in s. So (2) is the meromorphic continuation, and it has exactly two poles:

- at s = 0, the term −h(0)/s, from the lattice's n = 0 term in (1);
- at s = 1, the term ĥ(0)/(s−1) with ĥ(0) = ∫h, from the dual lattice's n = 0 term in (1).

The exchange (h, s) ↔ (ĥ, 1−s) swaps the two integrals and the two pole terms. For h = ĥ it is the functional equation, and its fixed line is Re s = ½.

**Check** (`checks/zero_ledger_check.py`). The test function is h(v) = (1+v²)e^{−πv²}, with ĥ(ξ) = (1 + 1/(2π) − ξ²)e^{−πξ²}.

- (2) holds at s = 2, 0.3 + 2i, −0.7 + i and 0.5 + 14i, with differences below 10⁻³¹.
- The residue at 0 is −1 = −h(0). The residue at 1 is 1.159154943 = ∫h.
- M_S h has residue h″(0)/2 = −2.14159… at s = −2. That pole is cancelled in 2ζM_S h by the zero ζ(−2) = 0.
- 1 + 2ζ(0) = 0 exactly.

## 2. Two derived facts that separate the poles

**(a) The pole at 0 sees one point, and the pole at 1 sees the density.** Replace ℤ by the lattice cℤ, with c > 0. The same computation gives 2c^{−s}ζ(s)M_S h(s). So:

- the residue at 0 is −h(0) for every c, since c⁰ = 1;
- the residue at 1 is (∫h)/c, the density 1/c of the lattice times the average of h.

The pole at 0 counts the single excluded point, whatever the spacing. The pole at 1 measures how densely the other points fill the line. The two differ in kind, as the owner said.

**(b) The position of the pole at 0 is set by the local model at the origin.**

- Suppose h(v) = c·v^α + O(v^{α+1}) as v → 0. Then ∫₀¹h(v)v^{s−1}dv = c/(s+α) + (holomorphic near −α).
- The classical smooth even model has α = 0, 2, 4, …. Evenness removes the odd exponents, and the trivial zeros ζ(−2k) = 0 cancel the exponents 2, 4, …. Only the constant term survives, at s = 0.
- A different local model at the origin moves this pole to −α or removes it.
- The pole at 1 depends on the behaviour of ĥ at ξ = 0, which is the average ∫h. A smooth local model at v = 0 is not needed for it.

**(c) The two poles are exchanged by duality: a point and a density.**

- The pole at 0 is the point evaluation h(0) = ⟨δ₀, h⟩. The pole at 1 is the average ∫h = ⟨1, h⟩ = ĥ(0).
- The Fourier transform sends δ₀ to the constant 1. The exchange (h, s) ↔ (ĥ, 1−s) carries ĥ(0)/(s−1) − h(0)/s to itself, because ĥ̂ = h for even h.
- So the two poles are the same type of object seen from the two sides of Fourier duality. On one side they differ in kind: a point against a density, as in (a).
- For the Gaussian, where h = ĥ, this is Λ(s) = π^{−s/2}Γ(s/2)ζ(s) = Λ(1−s), with residues −1 at 0 and +1 at 1.

**(d) The pivot of the exchange.**

- On the spectral side the exchange is the half-turn s ↦ 1 − s about the point ½. With complex conjugation it becomes the reflection s ↦ s^# = 1 − s̄, whose fixed set is exactly the line Re s = ½.
- On the scale side the same exchange is u ↦ 1/u, with pivot u = 1 (O4).
- The nontrivial zeros are #-symmetric. RH is equivalent to ρ^# = ρ for every nontrivial zero: every zero lies in the fixed set and has no exchanged partner. An off-line zero comes with the distinct partner ρ^#.
- This is a restatement of RH, not a new result.

## 3. The ledger

| # | Object called "0" or "1" | Where it enters (1)–(2) | What it produces | Status in the classical setting |
|---|---|---|---|---|
| Z1 | the lattice point 0 ∈ ℤ, the additive identity of the lattice | left out of Σ (n ≥ 1); returns as the term −h(0) in (1) | the pole at s = 0, residue −h(0), independent of spacing | input: the lattice contains its origin |
| Z2 | the dual-lattice point 0 | the term u^{−1}ĥ(0) in (1) | the pole at s = 1, residue ∫h/(covolume) | derived from Z1 by Poisson summation |
| Z3 | the origin v = 0 of the additive line, where h is evaluated | h(0) and its Taylor germ | pole positions 0, −2, −4, … of M_S h | input: the smooth even local model at the origin |
| Z4 | the value s = 0 of the Mellin variable | position of the pole from Z1 and Z3 | equals −(local exponent at Z3) | derived from the model at Z3 |
| Z5 | the scalar 0 ∈ ℂ | the conditions h(0) = 0 and ∫h = 0, and the equation ζ(ρ) = 0 | removal of both poles (the programme's source S); the zeros | the coefficient field's zero |
| Z6 | the fixed point of the sign involution, 0 = −0: the only non-free orbit of ±1 on ℤ and on ℝ | evenness of h at the origin | no poles at odd negative integers; with the trivial zeros, only s = 0 survives | input: the ±1 symmetry, the 𝔽_{1²}-structure |
| Z7 | absence, 0 = e = ∅ in the owner's notation (Z₀) | nowhere in (1)–(2) | nothing | listed only to keep it separate; never to be identified with τ |
| O1 | the integer 1, first term of Σ_{n≥1} and multiplicative identity of ℤ | 1^{−s} = 1 in ζ | the term 1 of the Dirichlet series | input |
| O2 | the exponent 1 in u^{−1}: the dimension of ℝ and the covolume of ℤ | Poisson summation (1) | the position s = 1 of the dual-zero pole, and the reflection s ↦ 1 − s | input: Fourier analysis on a one-dimensional line |
| O3 | the residue 1 of ζ at 1 | 2ζ·M_S h at s = 1 | the density of ℤ | derived: 1/covolume |
| O4 | the unit u = 1 of the multiplicative group ℝ_{>0}, i.e. log u = 0, the start of the clock | where the Mellin integral is split; fixed point of u ↦ 1/u | the symmetric split of (2) | a choice of split point; (2) is independent of it |
| H1 | the line Re s = ½ | fixed line of (h, s) ↔ (ĥ, 1−s) | the critical line; midpoint of the two pole positions | derived from O2 |

Two remarks on the table:

- **O4.** Splitting at u = a instead of u = 1 changes the two integrals and adds compensating terms, but not the poles: the left side of (2) does not depend on the split. So the start of the clock is a symmetric choice. It is the point that makes the two sides of the exchange look alike, and it is a different object from the additive origin Z3.
- **Z1, Z3 and Z6.** Classically, three of the "zeros" are at the same place with different roles: the lattice origin, the additive origin with its smooth germ, and the fixed point of the sign. The pole at 0 is produced by all three together: Z1 supplies the term, Z3 its position, and Z6 the cancellations. The owner's suspicion of a historical merger is, in this precise sense, correct.

## 4. Where τ could go (proposal, not a result)

The owner's own picture puts τ at the pivot:

- a hand swings from the side 0 to the side 1 around τ, then around again to 2, then to 3;
- τ is not 0.

In the zeta picture that is the pivot of §2(d): s = ½ (the line Re s = ½) on the spectral side, and u = 1 (O4) on the clock side.

- Under this assignment, "no Z₂" at τ is the statement that the pivot has no exchanged partner.
- RH becomes the statement that every zero shares this property (§2(d)).
- The alternation of sides after n half-turns is the parity of n. The pivot is the only point without a side.

This is a proposal of a typed map, from the pivot of the owner's swing to the pivot of the pole exchange. It is not a theorem about τ.

The other slots, each asking for a different definition:

- **Z1, the excluded lattice point.** An exclusion rule. The programme's Σ already excludes it.
- **Z3, the local germ at the origin.** A local model of test functions at τ. §2(b) then computes the pole: position −α, residue c.
- **Z6, the fixed point of the sign.** A statement about the ±1 action at τ, with its two readings in the register (goal 4, item 1): no exchanged label, or no sign at all.
- **O4, the start of the clock.** A choice of the symmetric split point, which does not change (2). This is the pivot slot on the clock side.

The rule "never identify τ with e" keeps it away from Z7. Which slot τ occupies, and with what local data, is the programme's definition to make. Until it is made, the pole at τ is an open definition, not a theorem (register, goal 4, item 11).

## 5. Items for the goals

- **Goal 4 (F1 context).** The classical pole at 0 merges three roles at one place: lattice origin, additive origin with its germ, and fixed point of the sign. The programme's τ asks for these to be separated. The ledger makes that separation explicit and computable. The ±1 structure (Z6) is the same structure that defines 𝔽_{1²} (register, goal 4, items 2 and 9).
- **Goal 3 (a lemma, classical in content).** For any lattice cℤ, the residue at 0 of the Mellin transform of the punctured lattice sum is −h(0), independent of c, while the residue at 1 is (∫h)/c. The pole at 0 counts a point; the pole at 1 measures a density.
- **Literature.**
  - Riemann's 1859 memoir (second proof of the functional equation) is the source of (2).
  - Tate's thesis gives the same structure in adelic form, with local factors (J. Tate, *Fourier analysis in number fields and Hecke's zeta-functions*, thesis 1950, printed in J. W. S. Cassels and A. Fröhlich (eds.), *Algebraic Number Theory*, Academic Press 1967). There the archimedean local factor, Γ(s/2) for the Gaussian, is the local model at Z3.
