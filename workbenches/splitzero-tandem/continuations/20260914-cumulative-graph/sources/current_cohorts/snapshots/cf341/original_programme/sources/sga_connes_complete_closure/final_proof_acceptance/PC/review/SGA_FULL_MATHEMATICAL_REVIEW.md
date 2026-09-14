# Full root review and determinant extension

Reviewed on 2026-09-13: the complete source `sga_constituent_period_curvature_20260913.tex`, equations SC1–37, including SC6a–b. This records direct mathematical reading, not a numerical or Lean execution. The final source pin is recorded in a companion receipt after the two specific typography/quotient clarifications below are closed.

## The period, coefficient and original-source maps

The fixed-ray exponential integral has a uniform majorant on each compact coefficient set. For r at least max(1,2(q+1)M), all lower terms have modulus at most M r^q/|u|, whereas the leading real part is −r^(q+1)/((q+1)|u|). Every coefficient derivative adds a fixed polynomial factor, still integrable against the retained tail. The two ray integrals have opposite origin orientations. Their integration-by-parts terms cancel there and vanish at infinity. For the top period column the exact relation is S^q=t−sum(c_a S^a), yielding Π′=−Π(A+t e_0 ℓ)/u with the displayed plus sign in the companion perturbation.

The original section j_E r_N=1 gives both j_E D_t=(A+t e_0 ℓ)j_E and D_t r_N−r_N(A+t e_0 ℓ)=dK_N^prim. These are actual equalities on the retained source domain; the added perturbation cancels exactly. The source kernel is preserved. The determinant formula used for invertibility has already been proved in XD with full contour and repeated-root coverage. Its Gamma-product constant needs the explicit multiplication calculation before it is cited in evaluated form (2π|u|)^q; that addition was requested from the author.

## Proper constituents, rank and curvature

For a nonzero proper A-invariant image, closure under all polynomials in A makes it an ideal of C[S]/χ. Its inverse image in C[S] has a unique monic generator g dividing χ. Write χ=gh and p=deg h. Cancellation in C[S] proves [a]_h↦[ga]_χ is an isomorphism onto the original ideal. In the actual ordered frame g,Sg,…,S^(p−1)g the last polynomial is monic of degree q−1 and every predecessor has lower degree. Therefore the top-coefficient functional L is onto. The unit is outside this proper ideal. These proofs retain repeated factors and the original module action.

For Y=ΠI, H=Y*Y, P=Y H^(−1)Y* and N=1−P, invertibility of Π and injectivity of I give H>0. The vector z=NΠe_0 never vanishes: a vanishing value would imply e_0 lies in the proper ideal. Invariance AI=IA_F gives the global identity NY′=−t zL/u. Thus the normal map has rank one and kernel ker L for t≠0. Its normal acceleration at zero is −z(0)L/u and also has rank one. The displayed source factorization through r_N e_0, j_E and NΠ proves the exact translation back to the arithmetic source. Every support lift takes a killed present vector to supported zero and takes external τ to τ.

Differentiating H and H^(−1) with Wirtinger derivatives gives

    ∂bar_t ∂t log det H = Tr(H^(−1) Y′* N Y′)
                         = |t|² ||z||² L H^(−1)L* / |u|².

Every factor in the final coefficient is positive for 0<p<q. The identity holds for all complex t, not only in a Taylor expansion. The coefficient is real analytic because Π is entire and det H never vanishes. A bound on its real gradient on a closed disk supplies the stated cubic remainder after multiplication by |t|². The first derivatives of P vanish at zero directly from NY′(0)=0. The first Chern convention for the dual determinant gives +(i/(2π)) times the positive scalar times dt∧dbar t, with i dt∧dbar t=2 dx∧dy. The empty and full constituents have the separately stated zero-curvature formulas.

## Exact original metric comparison

With the original domain Gram G_F=I*G_N I, the rank-one normal acceleration has squared Hilbert–Schmidt norm ||z(0)||² L G_F^(−1)L*/|u|². It is the unique nonzero squared singular value because the corresponding positive endomorphism has rank one. For B=G_F^(−1)H, the literal matrix identity H^(−1)=B^(−1)G_F^(−1) gives SC22 with the correct order.

For the full moving target metric Gtilde=Π^(−*)G_NΠ^(−1), the projection ΠI G_F^(−1)I*G_NΠ^(−1) is idempotent and Gtilde-self-adjoint. Its projected unit has squared norm equal to the displayed positive original-Gram Schur complement. Differentiation of Π^(−1) gives (A+tR)Π^(−1)/u, hence ∂t Gtilde=Π^(−*)G_N(A+tR)Π^(−1)/u. The conjugate derivative has the adjoint factor on the other side. These metric derivatives cancel the derivatives of Y in Y*Gtilde Y=G_F. Thus the fixed period metric curvature and the transported original metric are related by complete explicit congruences; no unproved isometry or uniform arithmetic bound has been inserted.

## New exact neighboring-determinant bridge sent to the author

Let J_g be the actual q×p coefficient matrix [g,Sg,…,S^(p−1)g] in the retained increasing-power basis. Let C be the unique invertible frame map satisfying I C=J_g. Then H_g=C*H C and L C is the last coordinate row. Let J_- be the first p−1 columns, with empty determinant one, and let J_+=[J_g,e_0]. The latter is injective because the unit is outside the ideal. Define h_J=det(J*Π*ΠJ).

The Schur complement for J_+ gives ||z||²=h_+/h_g. The last diagonal entry of H_g^(−1) is its principal cofactor divided by det H_g, so L H^(−1)L*=h_-/h_g. Therefore

    ∂bar_t ∂t log h_g
       = |t|² h_+ h_- / (|u|² h_g²).

This is the exact neighboring-volume identity, with no choice of orthonormal frame. It retains C explicitly. For v_J=det(J*G_NJ) and b_J=det((J*G_NJ)^(−1)J*Π*ΠJ), one has h_J=v_J b_J and therefore

    c_F = (v_+v_-/v_g²)(b_+b_-/b_g²)/|u|².

All original theta-volume factors remain. When p=q−1, g is monic linear. Expansion of [g,Sg,…,S^(q−2)g,e_0] along its last column gives determinant (−1)^(q−1); thus h_+=|det Π|² with the full previously proved Gamma and exponential factor. This proof is now present in the integration-ready source as SC31–37.

## Final extension reading, SC6a–b and SC26–37

The appended determinant-minor proof is complete and agrees with the derivation above. It gives the frame map explicitly as C=(I*I)^(−1)I*J_g, verifies its inverse-space type and retains |det C|². The only observed transcription defect was a literal comma in each of the two squared denominators in SC36; the author was instructed to remove both commas before sealing.

The Gamma evaluation retains all powers: the Fourier difference matrix contributes d^(q+1), the column scales contribute (d|u|)^q/d^(2q), and the squared Gamma product contributes (2π)^q/d. Since d=q+1, the total exponent of d is zero. The displayed multiplication identity and its z=1/d specialization were verified directly against [DLMF 5.5.6](https://dlmf.nist.gov/5.5.E6) and [5.5.7](https://dlmf.nist.gov/5.5.E7). This evaluates the squared modulus without changing the complex phase formula.

For derived specialization, the ring isomorphism C[t,S]/(χ(S)−t)→C[S], [P]↦P(χ(S),S), proves multiplication by the nonzero polynomial χ′ is injective on the full family. Its cokernel M has the two-term free C[t]-resolution displayed in SC27. The periodic diagonal resolution is exact because X−Y and the divided difference are both monic regular elements in the polynomial ring before quotient by their product. Tensoring by the diagonal gives alternately zero and χ′. Consequently all positive even family groups vanish and all odd ones are M.

Tensoring the free resolution by C[t]/(t−t_0) gives precisely SC28, including its first Tor term. The explicit representative map is correct: if (χ−t_0)v=χ′w, send [v] modulo χ′ to [w] modulo χ−t_0. Replacing v by v+χ′a changes w by (χ−t_0)a. Vanishing of the latter class implies v is divisible by χ′ by cancellation in C[S]; conversely every χ′-annihilated class supplies such v. This proves both inverse directions and compatibility with the original S-action. No exactness of ordinary specialization of kernels has been presumed.

At a local root of multiplicity m, write χ−t_0=x^m a(x). In the quotient by x^m, χ′=m x^(m−1)a(x); the pre-quotient derivative also has x^m a′(x). The author was asked to state the quotient explicitly. The retained local unit and nonzero integer m show that the odd module is C[x]/(x^(m−1)) and the even module is (x)/(x^m). Multiplication by the same local coordinate x gives the displayed module isomorphism and preserves S=λ+x. Both dimensions are m−1, with no removal of nilpotents.

The complete delivered SGA `NOTE.tex` was also read, including a separate bounded read of §§6.1–7 after an output truncation. Its arbitrary-base residue/trace proof, coevaluation, periodic resolution, coefficient-linear comparison, original-source conormal derivative, determinant and Newton recovery, exact period-metric congruence and constituent differentiation all agree with the extension's inputs. The earlier analytic source retraction and finite-field purity theorem remain explicitly inherited from their proof-bearing chapters. This reading did not re-execute their checks or enlarge a finite check's scope.

## Final disposition

The two requested corrections are closed in source SHA-256 `f7cbbb2da3a97722c9f9128602b4de64ad1ab9cfccdbb03e8ee9363321f7de63`. The mathematics of SC1–37, including SC6a–b, is accepted after the complete reading described above. Final layout edits only split the displayed SC10–11 lines; their maps and equalities are unchanged.

Root also read the complete independent primary review `sga_trace_period_primary_review_20260913.md`. Its actual original-French witness is SGA5.pdf SHA-256 `79bd542454ca2a5b3ac60488b14d3d91af9c7f8e68fa5acc0c48cf6068a89ad5`, with the reviewer visually reading printed 120–130 and136–137. Root did not repeat those visual readings. The source supplies finite-flat trace (6.8.5) without requiring the ambient smooth map to be proper; (6.8.4) adds that properness. Its noetherian scope remains explicit, and arbitrary-base validity rests on the actual monic finite-free proof. The printed page128 conormal-index typo is preserved as typography, with the exact I/I²→Ω¹ map identifying the correct mathematical conormal. The missing exact English master is a recorded provenance limitation, not a reason to omit the independently verified original-French operation or the full direct proof.
