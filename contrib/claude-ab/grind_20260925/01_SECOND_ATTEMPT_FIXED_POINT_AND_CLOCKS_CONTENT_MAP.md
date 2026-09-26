# The second attempt, part 1: fixed support, winding, prime clocks and timed primes

A content map of the published folder `workbenches/splitzero-tandem/temporary-arguments/20260924-fixed-generic-point-purity` (zeta-function-research-reader, commit 064f33b).

Claude (Opus 5.5 configuration), 25 September 2026.

## Scope and method

I read every mathematical file in the folder in full:

- the fixed-point record (README);
- the four prime-clock manuscripts: the CC1–CC5 fixed-point note, the W1–W10 winding note, the D1–D5 Deligne note, and the P1–P14 prime-clock note (the cumulative manuscript is their concatenation);
- the timed-prime reconstruction TP0–TP14;
- the clock-history note on a common radius.

That is about 3,300 lines. Labels such as W5 or TP10 are locators into those files. Each statement below is written out in full.

A statement marked **checked** was re-derived here, and in most cases also verified by the script `fgp_checks.py` (its output is reproduced at the end). The source texts cite the Connes–Consani preprints arXiv:2609.00299v1 and arXiv:2606.06604v1; their line numbers refer to the authors' TeX.

## 1. What the second attempt builds, in one pass

The construction takes the owner's primitive notions and realizes each one inside a specific published object: the archimedean component of Connes–Consani's absolute curve (arXiv:2609.00299, §§3–4). It then runs an explicit chain from that object to Spec ℤ and to the original ζ(s) on Re s > 1.

The chain is (W8, TP14):

(η, local data at η, mirror α) → the unit group G ≅ ℤ × ℤ/4 with its finite part H = ⟨J⟩ → the winding group L = G/H ≅ ℤ with its derived parity → the ring End(L) ≅ ℤ → Spec ℤ, with its local rings and residue sizes → the prime clocks ℤ/p and the first-appearance sieve → the prime periods log p on Connes–Consani's curves E_p = ℂ^×/p^ℤ → the measures of primitive and repeated returns → ζ, log ζ and −ζ′/ζ on Re s > 1.

Every arrow is an explicit map with a complete proof in the source files. The chain takes as input the infinite cyclic direction T^ℤ of the local data at η, which Connes–Consani supply. The notes state this themselves (W8, W9): they do not derive that direction from a bare point.

## 2. Dictionary: the owner's notions and the objects that realize them

| Owner's notion | Realizing object | Where proved | Status here |
|---|---|---|---|
| The pivot τ: fixed, present, without exchanged parity | The generic point η of the three-point space {+, −, η}. Every homeomorphism fixes it, and no two-state label exchanged by the mirror can be assigned to it equivariantly. | CC1–CC2, W1 | checked (topology; the fixed-point equation p(η) = r(p(η)) has no solution) |
| The mirror | The involution α, which swaps the two orderings of ℤ; on the unit group it acts by A(T^m J^k) = T^{−m} J^{2m−k} | CC3, W1 | checked |
| Half-turn; a full turn is not zero | The loop of lines with lifted angle mπ generates π₁(ℂ^×/ℝ^×) ≅ ℤ. The ray returns to itself exactly for even m, so a full turn counts 2. | P1 (from arXiv:2606.06604, Corollary "luriearch") | checked (standard covering theory) |
| Retained winding ("torsion") | The exponent m in the winding group L = G/⟨J⟩ ≅ ℤ | W1, P1 | checked |
| Parity arising from the mirror, not imposed | The map δ(g) = A(g)·g. For g = ε^a T^m J^b it equals ε^m, so it is a homomorphism L → {1, ε} with kernel 2L. | W2 | **checked** |
| No-turn state vs. returned states of equal parity | T⁰ and T² have the same parity ε⁰ = ε² = 1 but different exponents | W2, W10 | checked |
| The counting unit "1" is intrinsic, not calibrated | 1 is the identity endomorphism of L. End(L) ≅ ℤ as rings, independently of the choice of generator. | TP0, W3 | checked |
| Recovering Spec ℤ from the retained winding | Spec End(L) ≅ Spec ℤ as schemes, and the residue size at p is \|L/pL\| = p | W4 | checked |
| Prime "absorption channels" | The finite clocks C_n = L/nL. n is prime exactly when C_n is a nontrivial simple group. | P2, TP4 | checked (standard) |
| Composites create no new channel | The sequential rule (activate n exactly when no active channel divides n) activates exactly the primes | P9, TP3 | checked (this is Eratosthenes' sieve) |
| "The information is in the time intervals" | The prime gaps, anchored at 1, determine the list of primes, and conversely | TP5 | checked |
| The whole history, not a finite prefix | Every finite set P of prime readings leaves the ambiguity n + (∏P)ℤ; only infinitely many primes separate all integers | P6, P11 | checked |
| The global quotient of all clocks | The profinite completion Ĝ ≅ ℤ̂ × ℤ/4, with the mirror extended as Â(x, k) = (−x, 2(x mod 4) − k) | P12–P13 | checked (standard; the extension formula re-derived) |
| Prime periods | On Connes–Consani's E_p = ℂ^×/p^ℤ the scaling flow has primitive period log p (arXiv:2606.06604) | TP7 | checked |
| The full count rebuilt from primes and repetitions | The counting measure D = Σ_{n≥1} δ_{log n} is the convolution exponential of R = Σ_{p,k} (1/k) δ_{k log p}. Its Laplace transforms give ζ, log ζ and −ζ′/ζ on Re s > 1. | TP9–TP13 | **checked** (coefficient identity up to n = 400; −ζ′/ζ(2) numerically) |
| "Common weight / common distance" | Three separate realizations, next row | P12, D4, clock-history §5 | checked |
| (three realizations) | (i) continuous characters of the compact completion have modulus 1; (ii) the characters that stay bounded under all windings are exactly those with \|z\| = 1; (iii) the backward dilation D_n has spectrum exactly the circle \|λ\| = √n | as above | checked |

## 3. Results specific to Connes–Consani's object and not stated in their paper

These are elementary, but each is a precise statement about arXiv:2609.00299's archimedean local data. I found none of them in that paper, which I have read in full. I have not searched the wider literature for them.

1. **The parity norm and the equivariant non-splitting** (W2). The map g ↦ A(g)g realizes parity as a surjective homomorphism L → {1, ε}. No group section s of G → L satisfies A∘s = s∘(inversion). For every section t ↦ T J^c the defect is exactly the factor ε^m. **checked** (all four sections fail).
2. **Classification of the arithmetic maps compatible with the mirror** (W5). The endomorphisms of G that fix the sign ε and commute with A are exactly T ↦ T^n J^c, J ↦ J^b with n odd, c ∈ ℤ/4 and b ∈ {1, 3}. Composition is f_{n,c,b} ∘ f_{n′,c′,b′} = f_{nn′, cn′+bc′, bb′}. **checked** (exhaustive for \|n\| ≤ 9).
   - This extends Connes–Consani's restriction of the Frobenius to odd n (CC.tex L1095). They obtain it for the power maps x ↦ xⁿ; W5 obtains it for every sign-preserving map that commutes with the mirror.
   - For even n the two sides differ by exactly ε. So doubling exists on L, and (2) is a prime of Spec End(L), while no sign-preserving, mirror-compatible lift of doubling exists. (A lift that kills the sign, such as T ↦ T², J ↦ 1, does commute with the mirror; corrected in the final referee pass, part B.)
3. **The counting step as a product of two reflections** (W10). On L, b = S∘a (with S the winding step and a the inversion) is an involution, and S = b∘a. On the full group the corresponding map B = μ₁∘A, where μ₁ is multiplication by T, satisfies B² = multiplication by ε and B⁴ = id. **checked**. The lift of the count-advancing operation therefore has order four on the signed data, with square equal to the sign. The same order-four phenomenon appears in the running lane's twistor note (TD10), where a lift of the twistor involution squares to −I.
4. **The signed completion.** The mirror and every map in item 2 extend continuously to Ĝ ≅ ℤ̂ × ℤ/4 (P13). They also extend to the backward-dilation spaces ∏_{p\|n} ℚ_p × ∏_{p∤n} ℤ_p × ℤ/4 for odd n, commuting with the dilation (clock-history §6). **checked** (formulas re-derived; well-definedness modulo 4N).

## 4. Where the construction meets existing theory (bridges)

1. **Bost–Connes / Laca–Raeburn.**
   - Normalize P14's operators as S_n = √n·V_n on L²(ℤ̂). They are isometries with S_m S_n = S_{mn}, and P14.11 becomes S_m^* S_n = S_{n/d} S_{m/d}^* with d = gcd(m, n).
   - These are the relations of the semigroup crossed product C(ℤ̂) ⋊ ℕ^×. Laca–Raeburn (J. London Math. Soc. 59 (1999) 330–344) showed that the Bost–Connes Hecke algebra is such a crossed product.
   - The clock-history note itself identifies its zero-extension map with Connes–Marcolli–Ramachandran's α_n (arXiv:math/0501424).
   - So the owner's "global quotient of all prime clocks" is exactly the space on which the Bost–Connes system acts. Connes–Consani treat that system as an F₁ object in *On the arithmetic of the BC-system* (J. Noncommut. Geom. 8 (2014)).
2. **Beurling generalized primes.**
   - The identity D = exp_*(R) (TP10) is the specialization to the ordinary primes of Beurling's construction: the integer measure of a generalized prime system is the multiplicative-convolution exponential of its prime measure.
   - In that setting two facts pin down where any RH-relevant information in the chain can sit:
     - (a) If the generated integers are exactly 1, 2, 3, … with multiplicity one, the prime system is the ordinary primes. The proof is the first-appearance sieve (P9/TP3): a number that is not a product of earlier channels must be a new channel, and a second channel at a composite would double its multiplicity.
     - (b) Requiring only that the integers be very regular is not enough. Diamond–Montgomery–Vorhauer (Math. Ann. 334 (2006) 1–36) construct a system with N(x) = κx + O(x^θ), 1/2 < θ < 1, whose zeta function has infinitely many zeros on σ = 1 − a/log t. Zhang (Math. Ann. 337 (2007) 671–704) constructs two systems, both with N(x) = kx + O(x^{1/2} exp(c(log x)^{2/3})): one satisfies RH, and in the other the zeta function has zeros along a curve approaching σ = 1.
   - Consequence (my synthesis of cited facts, not a statement found in the programme files):
     - The multiplicative part of the chain (prime channels, their repetitions, exp_*) together with any regularity of the count up to x^{1/2+o(1)} is compatible with RH failing.
     - What distinguishes the actual system is exactness of the additive count: the integers produced are exactly the successive values of the counting step S.
     - The owner's admissibility rule (retain the complete original arithmetic, otherwise "swampland") therefore singles out one system. The question the programme asks becomes a question about how the counting step S constrains the multiplicative system.
3. **The adelic half-density factor.**
   - The √n circle of the backward dilation (clock-history §5) is the finite-place Haar modulus. When the real coordinate is added, the factors 1/n and n cancel (clock-history §8, R6).
   - This is the product formula. It is the same mechanism as the factor \|a\|^{1/2} in Connes' map E (arXiv:math/9811068, equations 18–19), which the note cites.
4. **Deligne.** D1–D5 state Deligne's notion exactly: a common weight is a common exponent w in \|ι(α_x)\| = N(x)^{w/2}, not a common radius across different residue sizes. They also correct two compressions in the historical English transcription against the French text (the det(1 − Ft) vs det(t − F) roots, and strict vs non-strict inequalities in 3.2.4).
5. **The two Connes–Consani papers.** P1 gives an explicit isomorphism between two objects:
   - the fundamental group of the ray/line covering ℂ^×/ℝ_{>0} → ℂ^×/ℝ^× from arXiv:2606.06604;
   - the winding group L of arXiv:2609.00299.

   Under it, ray-return parity goes to the parity δ. I have not read arXiv:2606.06604 in full, so I cannot say whether the authors state this map.

## 5. Items for the four goals from this folder

- **Standalone lemmas (goal 3):**
  - §3 items 1–4;
  - the Beurling uniqueness statement §4.2(a), which is the sieve read as a characterization of the ordinary primes among generalized prime systems;
  - the point counts 1 + p^r for Connes–Consani's odd Frobenius reduced mod p (from the running lane's twistor note, TD8; checked on 25 September).

  All are elementary. Novelty is unchecked.
- **Bridges (goal 2):** §4.1 (Bost–Connes / Laca–Raeburn), §4.2 (Beurling), §4.3 (adelic half-density), §4.5 (the two Connes–Consani papers).
- **F₁ context (goal 4):** the dictionary in §2 places the owner's τ at Connes–Consani's fixed generic point. The fixed sign ε still lives in the invariant local data there (see the reply of 25 September). §4.2 frames the programme's question in Beurling's terms.
- **Negative results (goal 1), stated plainly:**
  - Doubling has no lift that preserves the sign and commutes with the mirror (§3 item 2).
  - Modulus one for all continuous characters of a compact group holds for every compact group. The common-modulus theorem of P12 therefore carries no arithmetic information beyond the compactness of the completion; P12 says as much itself.
  - The √n radius of the finite-place dilation cancels against the real factor (§4.3), so it is not an invariant of the full adelic action.
  - The twistor involution does not fix the radius: the character values \|z\|^m are unrestricted, and equal radii occur exactly on \|z\| = 1 (W7).
  - The multiplicative reconstruction with regular counts does not force RH (§4.2(b), from the literature).

## Check output

```
W2 parity norm A(g)g = eps^m: True
W2 sections t->T J^c commuting with A (expect none): []
W5 degrees n allowed: [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9] ; c: [0, 1, 2, 3] ; b: [1, 3] ; count 80
W10 B^2 = eps*, B^4 = id: True
P11 lcm(4p) = 4 M_P: True
TP10 exp_*(R) = D on n <= 400 : True
TP13 -zeta'/zeta(2) = 0.569960993095 ; prime sum (p<20000) = 0.569911064242
clock-history shells: ||f_L||^2 = 50.0 (L s = 50.0 ); ||(D-lam)f_L||^2 = 6.0 (2 n s = 6.0 )
ALL PASS
```

## Sources

- Connes, Consani, *The Absolute Twistor Line and the Geometry of Spec ℤ* (compactified), [arXiv:2609.00299v1](https://arxiv.org/abs/2609.00299), read in full on 25 September 2026.
- Connes, Consani, *On the Absolute Geometry of Spec ℤ*, [arXiv:2606.06604v1](https://arxiv.org/abs/2606.06604); only the passages quoted in the programme files and the abstract.
- M. Laca, I. Raeburn, *A semigroup crossed product arising in number theory*, [J. London Math. Soc. 59 (1999) 330–344](https://academic.oup.com/jlms/article-abstract/59/1/330/809965).
- H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer, *Beurling primes with large oscillation*, [Math. Ann. 334 (2006) 1–36](https://link.springer.com/article/10.1007/s00208-005-0638-2).
- W.-B. Zhang, *Beurling primes with RH and Beurling primes with large oscillation*, [Math. Ann. 337 (2007) 671–704](https://link.springer.com/article/10.1007/s00208-006-0051-5).
- A. Connes, M. Marcolli, N. Ramachandran, *KMS states and complex multiplication*, [arXiv:math/0501424](https://arxiv.org/abs/math/0501424), as cited in the clock-history note.
- P. Deligne, *La conjecture de Weil. II*, [Publ. Math. IHÉS 52 (1980)](https://www.numdam.org/item/PMIHES_1980__52__137_0/), as reconstructed in D1–D5.
