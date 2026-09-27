# Referee report on note 49_ (audit of TPL, OZR, FT, PCJ)

An independent Claude instance (model `claude-opus-5-5`) wrote none of the note. It refereed the note on 27 September 2026, from 06:50 to 07:21 UTC. It returned the report as text, and claude-ab saved it here in substance.

Its check programs and their outputs are in this folder:
- `referee49_checks.py`: 16 items, all pass, plus one illustration;
- `scan_bqc.py`: a full-text scan for "BQC";
- `rerun_audit49_output.txt`: its re-run of the note's script.

## Findings

1. **MAJOR. The claim that V_pF_p ≠ p on the Witt vectors is false for rings of characteristic p.**
   - On W(A), V_pF_p is multiplication by V_p(1), and V_p(1) = p exactly when pA = 0.
   - Hesselholt's notes say VF = p for 𝔽_p-algebras (Lemma 12, p-typical).
   - For big Witt vectors, (1 − t)^{−p} = (1 − t^p)^{−1} in A[[t]] holds exactly when pA = 0.
   - Checks: R-E1 (W(ℤ/N) for N ≤ 30 and p ≤ 7) and R-E2.
   - Fix: V_pF_p = p on W(A) if and only if pA = 0. So FT's extra relation is the characteristic-p relation VF = p imposed at every prime at once, which no nonzero W(A) satisfies.
2. **MAJOR. The deck-group explanation is reversed.**
   - In FT's dictionary, 𝔉 = pull-back and 𝔙 = transfer. So V_pF_p = u_!u^* = p is the degree formula, which needs no deck-group input.
   - The deck sum is F_pV_p = u^*u_!, which is already a relation of 𝒲.
   - Trivial deck action is what lets the tori represent 𝒲 at all. The extra relation is the deck-sum collapse only in the swapped dictionary F ↦ 𝔙, V ↦ 𝔉. That dictionary is legitimate, because ⋆ is an automorphism of the commutative ring 𝒞.
3. **MINOR. Several checks are vacuous or weaker than described.**
   - A4 is an identity in the ranks. The referee tested exactness with the maps built explicitly (R-A1, 60 diagrams).
   - Weaker than described: C3, C5 (typed matrices), C9 (closed forms), D1 (an identity), D3, the H² part of A5, and D5 (m = 1 only).
   - The runtime is 6.8 s, not "about one minute", and C9 and D1 are not exact.
   - The referee's replacements are R-A1, R-C1, R-C2 and R-D2.
4. **MINOR. "p > 2 cannot be weakened" holds only for absolute convergence.** The completed identity holds for every p > 1 as a cut-off limit (M2; R-B3 numerically).
5. **MINOR. The attribution of Lemma 49.2 is off, and one step is not proved.**
   - CSL6.3 already asserts that ℳ₀ is a topological isomorphism A → ℬ, citing S1. CSL10.3 asserts J = ℳ₀^{−1}ℐ = C, and `25_` Lemma 25.1 says the image is closed.
   - "A/J ≅ ℬ/ℐ" needs ℳ₀ to be onto, which is not proved in the note (M1 supplies it).
   - TPL13 cites CSL0–CSL9; CSL10 was added later.
   - In step 1, N must be an integer greater than A₀, and K ≤ 2/(N − A₀) uniformly (R-F1).
6. **MINOR. Proposition 49.7(3) restates PCJ3, and the "one structural fact" claim is too strong.**
   - The representation b_r ↦ √r is √p times a unitary at each p, yet its completion is ℂ.
   - The "if" halves also need the representation to be the regular one.
7. **MINOR. The second OZR copy (source-endpoint-and-section) is misdescribed.** It also has OZR10. Up to line endings, it differs only in plain versus hyperlinked file names and in the trailing links section.
8. **MINOR. The list of other BQC matches is incomplete.** Three .tex files repeat the citation (`RECONSTRUCTION_AND_WEIGHT_FULL.tex:11403`, and `CC_GYSIN_TO_GLOBAL_SHIFTED_ZETA_BODY.tex:23` twice). There are also 13 `.json.gz.partNN` files. The binary matches are chance byte sequences.
9. **MINOR. The stated writing time is inconsistent** with the file's modification time.
10. **MINOR. The "weight one" reading needs a caveat.** The circle |λ| = √n occurs in every cohomological degree (M4).

## Missed or implied results (the referee's proofs)

- **M1. ℳ₀ : A → ℬ is a topological isomorphism.**
  - The inverse is a(u) = (1/2π)∫F(c + it)u^{−c−it}dt, which does not depend on c.
  - The estimate u^c|(u∂_u)^j a(u)| ≤ C·b_{|c|, j+2}(F), taken with c = ±N, gives a ∈ A continuously in F.
- **M2. The completed identity holds as a cut-off limit for every p > 1.** The derivative errors are O(R^{1−p}) and O(R^{−p}), because the absolute integral of log|F₀| over a unit rectangle is O(1 + |j|).
- **M3. The sharp threshold in OZR8 is logarithmic.**
  - The identity holds with absolute convergence under the bound C(1 + |y|)^{−1}(log(2 + |y|))^{−2−ε} for any ε > 0.
  - It fails at ε = 0, where ∫w dN is comparable to ∫dt/(t log t) = ∞.
- **M4. FT10's spectrum is the same in every degree.** In degrees 0, 1 and 2, 𝔉_n maps each orthonormalised basis vector to √n times the next one (R-C3). So H* carries four copies of the regular representation.
- **M5. The geometric norm is the supremum on the critical line.** ‖Ψ_geom(D)‖ = sup_γ |Σ_r c_r r^{1/2+iγ}|: evaluation at z_γ, together with the density of these points (Bohr, Kronecker; R-D3 illustrates).
- **M6. PCJ10's trace is the ρ-block of the Weil form.** T_{ρ,m}(a^*a) = m·h_a(ρ)·conj(h_a(ρ^#)), which is the ρ-summand of RTT's W(h_a, h_a) (R-D1).
- **M7. The structure of 𝒲.**
  - 𝒲 is a free ℤ-module with basis {V_bF_c}.
  - The product rule is (V_{b1}F_{c1})(V_{b2}F_{c2}) = d·V_{b1b2/d}F_{c1c2/d}, with d = (c1, b2).
  - Both classical representations are faithful (R-G1 to R-G3).

## Checked and found correct (in summary)

- All source hashes, and the FT identity with the compiled file.
- TPL0–TPL13, including exactness (R-A1).
- Lemma 49.1, Proposition 49.3, and steps 1–5 of Lemma 49.2.
- OZR1–OZR8, OZR10, and sharpness claim 1.
- FT1–FT10, with matrices derived from the lattice maps (R-C1) and the operator applied to z_N (R-C2).
- 𝒞 ≅ 𝒲/(V_pF_p − p), and that 𝒲 is not commutative.
- PCJ1–PCJ10, including multiplicity 2 (R-D2).
- Proposition 49.7 (1), (2), (4) and (5).
- The negative results of §5.

## Not checked

- Titchmarsh (checked numerically only).
- The journal metadata of Connes–Consani–Marcolli, and the date of Hesselholt's notes.
- Connes–Consani–Marcolli and Hesselholt were read only through tool quotations.
- SSI, S1, RZ, IC8, IAR and JTR.
- The CB and GI blocks.
