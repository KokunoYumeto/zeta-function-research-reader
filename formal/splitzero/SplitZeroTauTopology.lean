import SplitZeroTauRetraction

/-!
# The actual quotient topology and continuous operator defects

These results use the quotient topology of B/range(theta). There is no
replacement by a Hilbert completion, discrete topology, or finite packet.
The analytic input still has to supply the specified continuous retraction.
-/
noncomputable section
namespace SplitZero.TauRetraction.Data
universe u
variable {R V B : Type u} [CommRing R]
  [AddCommGroup V] [Module R V] [AddCommGroup B] [Module R B]
  [TopologicalSpace V] [TopologicalSpace B]
variable (S : Data R V B)

theorem section_continuous [ContinuousSub B]
    (hTheta : Continuous S.theta) (hLambda : Continuous S.lambda) :
    Continuous S.sectionMap := by
  apply (LinearMap.range S.theta).isQuotientMap_mkQ.continuous_iff.mpr
  change Continuous S.projection
  exact S.projection_continuous hTheta hLambda

/-- The actual quotient is Hausdorff under the established closed-range condition. -/
theorem quotient_hausdorff [IsTopologicalAddGroup B] [T2Space B]
    (hTheta : Continuous S.theta) (hLambda : Continuous S.lambda) :
    T2Space S.Q := by
  letI : IsClosed ((LinearMap.range S.theta : Submodule R B) : Set B) :=
    S.closed_range hTheta hLambda
  infer_instance

/-- Both directions are continuous for the original quotient topology. -/
def splitHomeomorph [IsTopologicalAddGroup B]
    (hTheta : Continuous S.theta) (hLambda : Continuous S.lambda) :
    (V × S.Q) ≃ₜ B where
  toEquiv := S.splitEquiv.toEquiv
  continuous_toFun := (hTheta.comp continuous_fst).add
    ((S.section_continuous hTheta hLambda).comp continuous_snd)
  continuous_invFun := hLambda.prod_mk (LinearMap.range S.theta).continuous_mkQ

theorem changeSection_continuous [IsTopologicalAddGroup B]
    (hTheta : Continuous S.theta) (hLambda : Continuous S.lambda)
    (b : S.Q →ₗ[R] V) (hb : Continuous b) :
    Continuous (S.changeSection b) :=
  (S.section_continuous hTheta hLambda).add (hTheta.comp hb)

namespace Operator
variable {S} (A : S.Operator)

omit [TopologicalSpace V] in
theorem quotient_continuous (hA : Continuous A.onB) : Continuous A.onQuotient := by
  apply (LinearMap.range S.theta).isQuotientMap_mkQ.continuous_iff.mpr
  change Continuous (fun b => S.q (A.onB b))
  exact (LinearMap.range S.theta).continuous_mkQ.comp hA

theorem defect_continuous [ContinuousSub B]
    (hTheta : Continuous S.theta) (hLambda : Continuous S.lambda)
    (hA : Continuous A.onB) : Continuous A.defect :=
  hLambda.comp (hA.comp (S.section_continuous hTheta hLambda))
end Operator
end SplitZero.TauRetraction.Data
