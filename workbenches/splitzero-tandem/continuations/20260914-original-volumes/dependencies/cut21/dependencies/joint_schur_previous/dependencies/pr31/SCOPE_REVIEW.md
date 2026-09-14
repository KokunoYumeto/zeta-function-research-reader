# PR31: exact declaration scope and application interface

Read on 2026-09-14: every declaration and proof body in the five downloaded Lean modules, and the complete `RESEARCH_NOTE.md` and `STATUS.md`. Sources are the files pinned by `FETCH_RECEIPT.json` to head `b4060b25c21f1a49a5e7730e9aff76d4c93c820d`; the reported checked implementation is `04ef2f962d69186ef48f07679a339b57486ef471`. This is a bounded source review. No Lean process was launched, imported dependency proof bodies were not reread, and this review does not independently re-execute or attest the historical CI.

All names below have prefix `SplitZero.`. Let `tr_R(A) = Re(trace A)` and `center(A) = A - tr_R(A) I / card(j)`, exactly as implemented. The scalar in the centering map is real.

## 1. Finite series: the ring calculation is proved

`ResolventSeries.partialSum H T L` is `(sum r in range(L+1), H^r) T`, including its constant term. In an arbitrary ring, `geometric_right` proves

\[
\left(\sum_{r=0}^{n-1}H^r\right)(1-H)=1-H^n
\]

by induction. `residual_exact H T X L hX` uses the literal equation `(1-H) X = T` to prove `X - partialSum H T L = H^(L+1) X`. Its proof uses associativity and distributivity; it does not require a commutative ring, `HX=XH`, or any observable. `partialSum_zero` proves the finite sum is `T` at `H=0`, for every `L`.

The scalar declarations `blend_lower`, `blend_pos`, `blend_mono`, `tangent_bound`, `midpoint_deviation`, `blend_contraction`, and `contraction_range` prove the fixed positive endpoint interval inequalities written in SR7. In particular `blend_contraction lo hi b x` requires `0 < lo`, `lo <= b <= hi`, and `0 <= x <= 1`, and concludes the bound `(hi-lo)/(lo+hi)`. No estimate over changing endpoint data is supplied by this declaration.

For a finite nonempty spectrum, `variance_formula` proves the full energy minus mean-square identity. `residual_variance_bound` uses only the explicit scalar bounds `|h_i| <= theta`, `|g_i| <= a_i`, and `theta >= 0`; it retains the exponent `L+1`. `radius_tendsto_zero` and `exists_stopping_degree` establish convergence and an existential finite stopping degree for fixed `0 <= theta < 1`, fixed `K,Z`, and positive requested tolerance. They do not compute a packet-uniform degree.

## 2. Weighted Cauchy–Schwarz is constructed, not a certificate field

`SignedTraceEnclosure.MetricFrame M` consists of matrices `forward`, `inverse`, both inverse equations, and `forward* forward = M`, where the first star denotes conjugate transpose. Its `conjugate A` is `forward A inverse`.

`MetricFrame.ofPosDef M hM` constructs such a frame from `M.PosDef` using Mathlib's positive factorization into the star-square of a unit. `conjugate_mul`, `trace_conjugate`, and `hermitian_conjugate` prove product, trace, and self-adjointness transport. The last declaration takes the original-coordinate equation `A* M = M A`.

`hermitian_schwarz_sq` installs the matrix Hilbert–Schmidt inner product, applies `norm_inner_le_norm`, bounds the real part by the complex norm, and identifies both squared norms with `tr_R(A^2)` and `tr_R(B^2)`. `weighted_schwarz` transports this proof through the constructed metric frame and proves

\[
|\operatorname{tr}_{\mathbb R}(AB)|\le
\sqrt{\operatorname{tr}_{\mathbb R}(A^2)
      \operatorname{tr}_{\mathbb R}(B^2)}.
\]

Its inputs are `M.PosDef`, `A* M = M A`, and `B* M = M B`. No commutation between `A` and `B` is required.

`centered_pairing` takes the literal complex equality `trace B = 0`. `weighted_center` preserves the original metric adjoint equation. `signed_interval` takes `M.PosDef`, original-metric self-adjointness of `X,Y,Q`, and `trace Q = 0`. With `E=center(X-Y)`, it encloses `tr_R(XQ)` around the signed center `tr_R(YQ)` with radius `sqrt(tr_R(E^2) tr_R(Q^2))`. It requires no canonical-projector presentation of `Q` and no commutation with `Q`.

## 3. The canonical four-projector specialization has additional data

`CanonicalSignedResolvent.canonicalContrast` uses four original relation matrices `B a`, four `Metric (B a)` structures `M a`, four coefficient matrices `C a`, four inverse quotient Grams `K a`, and one `source` form. The relation indices `m a` may differ, but the coefficient/quotient index `n` is shared by all four endpoints. The common-form equations are `(M a).form = source`, and the inverse equations are `(M a).quotientGram (C a) * K a = I`.

The contrast is exactly the inherited construction

\[
Q=P_0+P_1-P_2-P_3,\qquad
P_a=\rho_aK_a\rho_a^*\,\mathrm{source},\quad
\rho_a=(M_a).\mathrm{sectionMap}(C_a).
\]

`canonical_properties` composes imported canonical-frame theorems to prove `trace Q=0` and `Q* source = source Q`. `canonical_interval` additionally takes `source.PosDef` and original-metric self-adjointness of `X,Y`, then applies the preceding generic signed interval.

`weighted_mul` requires `AB=BA` in addition to the two weighted adjoint equations. `weighted_pow` proves the power equation. `weighted_partialSum` requires `H,X` weighted self-adjoint, `HX=XH`, and `(I-H)X=T`; it derives weighted self-adjointness of the actual partial sum from the exact residual. Thus `canonical_resolvent_interval` has these same algebraic inputs. It requires no commutation of `Q` with `H` or `X`.

`canonical_tangent` also takes `source J = I`. It proves the exact complex-trace identity between `trace((JE)Q)` and the four signed quotient terms `trace(K_a rho_a* E rho_a)`. It does not differentiate a determinant, an arithmetic integral, or a path. Those analytic identifications must come from the written application calculation.

## 4. Spectral residual: explicit simultaneous diagonalizing equations

`SpectralResidual` takes a specified `MetricFrame M`. This frame need not be the particular choice made by `MetricFrame.ofPosDef`. The declarations `frame_one`, `frame_sub`, `frame_smul`, `frame_pow`, and `frame_center` prove the exact algebraic transports.

`residual_diagonal` and `residual_energy` take two explicit equations for that same frame:

\[
FHF^{-1}=\operatorname{diag}(h_i),\qquad
FXF^{-1}=\operatorname{diag}(g_i),\qquad h_i,g_i\in\mathbb R.
\]

They prove the actual residual matrix has eigenvalue expression `h_i^(L+1) g_i` and that its centered square trace is the finite scalar variance. Combining `residual_energy` with `ResolventSeries.variance_formula` supplies the full subtracted mean-square formula SR8. The chosen frame and these two equations are inputs; positive factorization alone does not supply simultaneous diagonalization.

`signed_error` requires a finite **nonempty** matrix index, `M.PosDef`, weighted self-adjointness of `H,X,Q`, `trace Q=0`, `HX=XH`, `(I-H)X=T`, both simultaneous diagonalization equations, and scalar bounds `|h_i|<=theta`, `|g_i|<=a_i`, `theta>=0`. It concludes

\[
|\operatorname{tr}_{\mathbb R}(XQ)-
  \operatorname{tr}_{\mathbb R}(S_L(H,T)Q)|
\le \theta^{L+1}
\sqrt{\left(\sum_i a_i^2\right)
      \operatorname{tr}_{\mathbb R}(Q^2)}.
\]

The proof derives nonnegativity of `tr_R(Q^2)` by the specified metric isometry, rather than taking it as an unexplained premise. The theorem itself only requires `theta>=0`; convergence uses the separate strict upper bound `theta<1`.

For the proposed eight-block joint-Schur application, `signed_interval` and `signed_error` are the direct interfaces once the actual block metric, isometry, self-adjoint matrices, zero-trace observable, and scalar spectral bounds have been constructed. Calling this a specialization of `canonical_resolvent_interval` additionally requires the explicit four canonical relation/section presentations listed above. The five modules contain no theorem identifying the joint-Schur determinant return with the integrated signed trace; that exact identification belongs in the new written calculation.

## 5. Proper-boundary construction and exact type scope

`RestrictedBoundary` works over a commutative coefficient ring, a support semilattice with bottom, original linear diagrams `D,E`, a natural linear map `f`, stable relation families `B,C`, and the fibrewise relation-preservation equations `B_i <= f_i^{-1}(C_i)`.

`killedRelations` constructs the actual preimages and proves stability. `residualRelations` constructs the restricted original relation family. `quotientHom` proves naturality by quotient representatives. `kernelDiagram` restricts the original quotient transports to their kernels; no transport injectivity is assumed. `residualEquiv` applies the imported `Homology.quotientKernelEquiv` on the literal fibres. `kernelComparison` and `kernelInverse` prove naturality, and `left_inverse_total` and `right_inverse_total` prove the two inverse laws on total maps.

`original_square` is the exact total-map quotient square. `range_iff_supported_zero` characterizes the total image by `qf(y) = e • qf(y)` in the receiving total module. `proper_residual` proves that a representative outside `B_i` whose image belongs to `C_i` gives a nonzero proper quotient class mapping to the receiving same-label zero. `present_empty_residual` proves that the total element `((i, empty),0)` differs from the **global zero of that total module** when `i != bottom`; its literal statement is not an equality between a vector and the scalar constructor `tau`. These are the precise types in the module. The imported SplitZero action supplies the receiving supported-zero meaning used by the preceding range theorem.

## Review conclusion

The five source files agree with the stated scope in the research note and status: the finite noncommutative residual and weighted trace inequality are proved, the generic signed interval is attached to the original canonical four-projector construction through an explicit specialization, and the matrix spectral residual is transported by explicit original-metric isometry equations. No mathematical error was identified in the inspected declaration/proof bodies. The application must retain the required constructions and the nonempty spectral index; at `l=0`, an intended `8l`-dimensional application needs its separate zero-dimensional evaluation before invoking `SpectralResidual.signed_error`.
