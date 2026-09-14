# Accepted analytic continuation of the actual Taylor-unit gauge

13 September 2026. Root read the complete independent review and its final
acceptance of AP1--26, including AP19a--b. All reported corrections are resolved.

- Full proof `ANALYTIC_POLE_RESIDUE_TRANSPORT.md`: SHA256
  `357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652`.
- Full independent review `ANALYTIC_POLE_INDEPENDENT_REVIEW.md`: SHA256
  `5dc90ea5d545b674faf02d5f05ccdbd32efdeb03c6b27df793fbedaf32f91d0a`.

This is new written mathematics on the original h, full Taylor unit nu,
polynomial exponential complex and its actual localization. At nonzero u,
the original rank-d cohomology injects into a rank-(d+r) analytic extension.
Its exact cokernel is the r weighted residues at the distinct nu-pole points.
Every higher principal part is treated by the displayed derivative/residue
formulas; no multiplicity of h is removed.

The full proof calculates the block connection, its upper-right scaling
integral, both residue frames and all their exponential factors, the complete
period determinant including the oriented 2 pi i loop factors, the actual
nu-gauge period identities, the ordinary dual, and the explicit special-fibre
quotient J0 carrying the extended action back to the original A.

The p=0 residue-factor exception and the constant-nu empty-pole case are
explicit. The prior coefficientwise formal contraction is not evaluated at
nonzero u. The added analytic residue cokernel is computed, rather than
declared absent because the formal complex was contracted. The new period
matrix and endpoint quotient give the exact comparison maps.

The source owner supplied the residue sequence and simple-pole connection;
root wrote their full continuation and scaling/dual proof; the independent
reviewer supplied and checked the extended determinant and endpoint kernel.
Those contributions are explicitly recorded in the proof's provenance.

Verification scope is full written proof and independent proof review. No
numerical fixture, Lean execution, arithmetic-zero certificate or uniform
theta-metric bound is claimed. This does not retroactively modify the frozen
715- or 765-page publications. It is a sealed input for the next cumulative
reader, and the corresponding continuation prompt must not ask to redo these
completed pole, contour or endpoint calculations.
