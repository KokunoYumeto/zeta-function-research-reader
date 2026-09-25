# The second attempt, part 4: character lifting through the summation map, and Deligne's cross

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026.

This is a content map of the character-lifting core of the three-lane edition, together with the parts of the Deligne reader that the core compares itself with. As in `01_`, `04_` and `05_`, I report what the notes establish, in plain statements, and then what I checked. The RH question is not used to grade anything.

## Scope

**Read in full.** Under `workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/`:

- `ORIGINAL_MELLIN_CHARACTER_LIFTING.md` (MCL0–MCL11);
- `ORIGINAL_RESTRICTION_EXTENSION_AND_DELIGNE_CROSS.md` (ORE0–ORE10);
- `ACTUAL_RESIDUE_PUSHOUT_AND_CHARACTER_LIFTING.md` (RPC0–RPC8);
- `SUPPORTED_COMPARISON_QUOTIENT_TRIANGLE.md` (SCT0–SCT6).

The following parts of `gct-weight-control/DELIGNE_WEIGHT_CONTROL_FULL.md` were also read in full:

- DB9, the specialization to ζ;
- DR0–DR7, the receiving map for ζ;
- DC0–DC12, the local invariant cycle theorem;
- DW5–DW11, the weight argument itself;
- MDB9–MDB11, the purity circle and the weight-descent defect.

**Not read.**

- DP, DMG, DLM, DB0–DB8, DBC, DW0–DW4 and MDB0–MDB8.
- The 33,000-line cumulative reader.
- The proofs these notes rely on, namely the closed-image theorem (OMS/SSI), DPL and GZR.
- The two continuations published on 25 September: "full-source tensor and original divisor", and "source endpoint and residue section".

## 1. The setting

Everything happens in one short exact sequence.

- S is the space of even Schwartz functions h with h(0) = 0 and ∫h = 0.
- A is the space of smooth functions on (0, ∞) that decay rapidly at both ends in the logarithmic scale.
- Σh(u) = 2 Σ_{n≥1} h(nu) is the summation map of Connes and Consani ([arXiv:0903.2024](https://arxiv.org/abs/0903.2024), §5).
- The Mellin transform turns Σ into multiplication by the zeta function:

  M(Σh)(z) = 2 ζ(z) · M_S h(z),  where M_S h(z) = ∫₀^∞ h(v) v^z dv/v.  (MCL1.8)

  The pole of ζ at z = 1 is cancelled because M_S h(1) = ½∫h = 0.
- The image J = ΣS is closed (the programme's OMS/SSI, inside the framework of R. Meyer, [arXiv:math/0412277](https://arxiv.org/abs/math/0412277)). The transposed sequence is therefore exact:

  0 → Q′ → A′ → S′ → 0,  Q = A/J.  (MCL9.1, ORE1.3)

Dilation acts on all three terms. Its generalized eigenvalues on Q′ are exactly the nontrivial zeros ρ, and the Jordan block at ρ has length equal to the multiplicity m (MCL9.2, ORE3.2). The character-lifting lane asks what happens when one tries to lift a character of S′ back through Σ′.

## 2. What the notes establish

1. **Every generalized character of A′ is a Mellin jet** (MCL3.2).
   - Write A_j for the functional b ↦ ∫ b(u) u^ρ (log u)^j du/u.
   - The continuous functionals killed by (K − ρ)^d are exactly the combinations of A_0, …, A_{d−1}.
   - The proof restricts the functional to compactly supported tests, where the eigen-equation becomes an ODE for a distribution.

2. **Two primes suffice** (MCL3.4).
   - Let p ≠ q be primes. A functional that is a generalized eigenvector of order r for dilation by p, and of order s for dilation by q, with eigenvalues p^ρ and q^ρ, is a combination of A_0, …, A_{min(r,s)−1}.
   - One prime alone is not enough: M_{ρ+2πik/log p} has the same p-eigenvalue for every integer k.
   - The mechanism is the density of (log p)ℤ + (log q)ℤ in ℝ. It is the same fact that drives the two-prime receiver IH6 and the non-return result PL3 (`05_`).

3. **No pure character lifts** (MCL6).
   - At a zero of multiplicity m, Σ′ sends A_0, …, A_{m−1} to zero, while the source character S_0 = M_{S,ρ} is nonzero (MCL4).
   - Hence no eigenvector of A′ maps onto S_0.

4. **The least lift, explicitly** (MCL5.7, MCL6.2, MCL6.3).
   - The source jet S_j lifts to a generalized character of order exactly m + j + 1, by the lift Λ_{ρ,j} = j! Σ_k v_{j−k} A_{m+k}/(m+k)!.
   - Here 1/(2g(t)) = Σ_k v_k t^k, and ζ(ρ+t) = t^m g(t).
   - All such lifts are Λ_{ρ,j} + span(A_0, …, A_{m−1}).
   - The smallest invariant space mapping onto the first r jets is one Jordan block of length m + r:

     0 → E_A(m) → E_A(m+r) → E_S(r) → 0.

5. **The lift does not commute with dilation, by an explicit amount** (MCL7.3).
   - The defect at dilation a is a^ρ/(2ζ^{(m)}(ρ)) · Σ_{n<m} C(m,n)(log a)^{m−n} A_n.
   - This is nonzero for every a ≠ 1, in particular at every prime.

6. **The lift is exactly compatible with the reflection ρ ↔ 1 − ρ** (MCL8.6).
   - The multiplier is κ(z) = ζ(1−z)/ζ(z) = π^{1/2−z} Γ(z/2)/Γ((1−z)/2).

7. **The obstruction class is the functional-equation multiplier** (ORE4–ORE5).
   - Consider lifting with a fixed annihilator q = (X − b)^r, where b = 1 − ρ. The connecting map δ_q : ker q(G) on S̃ → Y/qY is onto and has rank min(m, r) (ORE3.1, ORE5.8).
   - Transported through the residue pairing D, its value on S_j is

     (−1)^j j!/2 · t^{r−1−j} χ_ζ(b+t)  mod t^{min(m,r)},

     where ζ(s) = χ_ζ(s) ζ(1−s).
   - The factor ½ comes from the 2 in Σ.

8. **The residue pairing absorbs the whole obstruction** (RPC).
   - The residue map D : Q → Y is D[F]([K]) = (1/2πi)(∫_{(2)} − ∫_{(−1)}) F(s)K(1−s)/ζ(s) ds. It is injective.
   - On its cokernel C = Y/DQ, every nonzero polynomial in the generator is bijective (DPL, cited).
   - After pushing the sequence out along D, every locally finite vector of S̃ has a unique equivariant lift (RPC4–RPC5), and the connecting class becomes zero (RPC6.3).

9. **The quotient triangle** (SCT).
   - The comparison J : K_ζ → L_ζ of the two supported cones has cone homotopy equivalent to Ã[−1], by an explicit contraction (SCT2.7).
   - After the cyclic resolution, the degree-two map carries −δ_q/2 (SCT4.4, SCT5.2).

10. **Deligne's local invariant cycle theorem, reconstructed** (DC; Weil II §3.6.1).
    - Take the cross 0 → K_i → B_i → C_i → 0 (Hochschild–Serre) and A_i → B_i → O_i (localization).
    - C_i has weights ≤ i, and O_i ≅ H^{2N−i−1}(X_s)^∨(−N) has weights ≥ i + 1.
    - The weight-≤ i part of B_i therefore lifts to A_i, and specialization A_i → C_i is onto (DC7).
    - The lane proves a stronger consequence (DC8): K_i has weights ≥ i + 1. The Hochschild–Serre extension therefore splits canonically, and the Frobenius-equivariant section is unique.

11. **The comparison: in the ζ row, kernel and target have the same weight** (ORE6–ORE7).
    - The pullback of 0 → Y → Ã → S̃ → 0 over the first r jets is one Jordan chain of length m + r.
    - Its kernel, its middle term and its target all carry the same character b = 1 − ρ.
    - Any exact truncation by weight (by |p^λ|) therefore keeps the whole sequence or kills it (ORE6.5).
    - Consequently the analogue of DC8's canonical splitting fails at every zero: the class in item 7 is nonzero.
    - The analogue of Deligne's obstruction group sits at the same weight as the target.
    - Surjectivity of generalized-character lifting still holds, through the longer Jordan block. This is the note's own distinction between "surjective" and "split" (ORE6, ORE7).

12. **Positivity of the programme's return measure gives exactly the line Re s = 1** (DB9, DR0–DR4).
    - The timed-prime measures satisfy D = exp_*(R) (unique factorization) and W = tR.
    - They map invertibly to the positive measure μ_σ = e^{−σt}W, which Deligne uses in Weil II §2.1.9 for ζ.
    - The identity 3 + 4cos θ + 2cos 2θ = (1 + 2cos θ)² ≥ 0 gives 3 − 4m_t − 2m_{2t} ≥ 0 at the boundary. Hence ζ(1 + it) ≠ 0.
    - This is the Hadamard–de la Vallée Poussin theorem. The DR note states explicitly that the remaining steps of Deligne's argument are not supplied by the positive measure (DR4, DR7).

13. **Deligne's mechanism in one line** (DW11.1). The chain is:
    - F ↦ F ⊠ F on a surface with a pencil;
    - the fibrewise H¹ has weights congruent to 2β mod ℤ (local monodromy);
    - boundary strictness gives γ < 2β + 2, and with the congruence γ ≤ 2β + 1;
    - H¹ ⊗ H¹ ↪ H²;
    - squaring gives 2w(α) ≤ 2β + 2 + 2^{−k};
    - induction gives w(α) ≤ β + 1;
    - duality with F^∨(1) gives equality.

    Section 3 of `08_` compares these inputs with what the programme supplies.

14. **Purity as a fixed-point equation** (MDB9.10).
    - The degree-two duality with its Tate twist acts on characters by a ↦ p/ā.
    - On a = p^ρ its fixed points are exactly |a|² = p, that is, Re ρ = ½.
    - Deligne obtains membership of this circle from two upper bounds, one for the object and one for its dual (MDB9.4–MDB9.7).

## 3. Checks by claude-ab

- **`checks/mcl_ore_checks.py` (ALL PASS).** The checks run at the first zero ρ₁, with m = 1 using ζ and m = 2 using ζ². The second case exercises every sign and factorial that depends on m; there the reflection multiplier is χ_ζ².
  - All of the following agree to at least 1e-39:
    - the germ identity u_b(t) = (−1)^m χ(b+t) u_ρ(−t) (ORE5.4);
    - the recursion for v_k (ORE4.5);
    - the key germ identity u_b(t) Σ v_k(−t)^k = (−1)^m χ(b+t)/2 behind item 7 (ORE5.6);
    - Σ′Λ_{ρ,j} = S_j for j ≤ 3 in the jet basis (MCL5.4);
    - the exact top coefficient of (T_a^t − a^ρ)^{m+j} Λ_{ρ,j}, and its vanishing at the next power, for a = 2, 3 (MCL6.4);
    - the top coefficient j!m/(2ζ^{(m)}(ρ)) of the connecting representative (MCL9.6).
  - The representative lies in span(A_0, …, A_{m−1}), as the notes require.
- **By hand.**
  - MCL3.4: the power (E_x − 1)^{r+s−1} lies in the ideal generated by (E_h − 1)^r and (E_ℓ − 1)^s. This is the binomial pigeonhole count, since E_{mh+nℓ} − 1 lies in the augmentation ideal.
  - The identities (1 + 2c)² = 3 + 4c + 2cos 2θ and the limit 3 − 4m_t − 2m_{2t} ≥ 0 (DB9.7–DB9.8, DR4.2–DR4.3).
  - The two forms of κ in MCL8.3: the local Tate functional equation at ∞, and ζ(1−s) = π^{1/2−s} Γ(s/2)/Γ((1−s)/2) · ζ(s).
  - The contraction dh + hd = id − ip in SCT2.7, by substitution. This uses νJ = 0, ν d_L = 0 and d_L σ = Jθ.
- **Not checked by me.**
  - The closed-image theorem (OMS/SSI).
  - The invertibility of polynomials on C (DPL), which RPC and ORE5.1 cite.
  - The topological statements (weak-* exactness, strong duals).
  - DC's use of Weil II 1.8.8 and 3.3.9. These are Deligne's theorems, cited.

## 4. Items for the four goals

**Negative results (goal 1).**

1. **No character-level lifting at any zero.**
   - A zero of multiplicity m forces the least lift of the k-th source jet to have order m + k + 1.
   - This depends on the multiplicity only, not on the position of the zero.
2. **Deligne's separation cannot occur in the ζ restriction row.**
   - Kernel and target carry the same character, and any weight truncation keeps or kills the whole extension.
   - The fixed-order extension class is nonzero at every zero, on or off the line (ORE5.8, ORE6.5).
3. **After the residue pushout the obstruction is zero at every zero** (RPC6.3). It therefore carries no information about Re ρ.
4. **Positivity of the return measure reaches exactly the boundary Re s = 1, and no further** (DB9, DR4). The remaining steps of Deligne's argument need inputs that are examined in `08_`.

**Standalone lemmas (goal 3).**

1. **Two-prime generalized eigenvectors.**
   - Statement: let h, ℓ > 0 with h/ℓ irrational, and let V be a distribution on ℝ with (E_h − 1)^r V = 0 and (E_ℓ − 1)^s V = 0. Then V is a polynomial of degree < min(r, s).
   - Proof: MCL3.4.
   - Link to the literature: V satisfies two convolution equations. Their Fourier transforms (e^{ihλ} − 1)^r and (e^{iℓλ} − 1)^s have λ = 0 as their only common zero, with common multiplicity min(r, s). For continuous V, the same conclusion therefore also follows from L. Schwartz's spectral synthesis for mean-periodic functions ([Ann. of Math. 48 (1947) 857–929](http://sites.mathdoc.fr/OCLS/pdf/OCLS_1947__8__857_0.pdf)).
2. **Least-order lifting formula** (MCL5.7, MCL6.2). The statement uses only the identity M(Σh) = 2ζ · M_S h and the multiplicity. It therefore holds for every Dirichlet series for which the same identity holds; `08_` §2 makes this precise.
3. **The obstruction class is the functional-equation germ** (ORE5.6). The class of the fixed-order lifting problem, read through the residue pairing, is (−1)^j j!/2 · t^{r−1−j} χ_ζ(b+t) mod t^{min(m,r)}.

**Bridges (goal 2).**

1. **Deligne ↔ Hadamard–de la Vallée Poussin.** Weil II §2.1, specialized as in §2.1.9, is the Hadamard–de la Vallée Poussin argument. The programme's timed-prime measure R feeds it exactly (DR).
2. **Two crosses.** Deligne's invariant-cycle cross (DC) and the Connes–Consani–Meyer restriction row (ORE) are compared term by term. The difference lies in one place: the weights of the kernel and of the target (item 11).
3. **Two-prime density.** The two-prime density argument unifies MCL3.4, IH6 and PL3. It is the same phenomenon as the one-variable two-period (mean-periodic) theory.
