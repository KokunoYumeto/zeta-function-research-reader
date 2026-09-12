import SplitZeroTauHomotopy
import SplitZeroSupportChange
import SplitZeroJointHomotopy
import SplitZeroRelationLayer
import SplitZeroOrthogonalControl

/-!
# The new boundary layer in the existing theta comparison

The actual packet, representative, jet map and derivative-boundary map are
retained as typed maps. No claim about the analytic construction of these
maps is introduced as a new axiom.
-/

noncomputable section
namespace SplitZero.BoundaryIntegration

universe u
variable {R V B E : Type u} [CommRing R]
  [AddCommGroup V] [Module R V] [AddCommGroup B] [Module R B]
  [AddCommGroup E] [Module R E]

def packetProjector (rep : E →ₗ[R] B) (jet : B →ₗ[R] E) : B →ₗ[R] B :=
  rep.comp jet

theorem packetProjector_idempotent (rep : E →ₗ[R] B) (jet : B →ₗ[R] E)
    (hj : ∀ x, jet (rep x) = x) :
    (packetProjector rep jet).comp (packetProjector rep jet) = packetProjector rep jet := by
  apply LinearMap.ext
  intro x
  change rep (jet (rep (jet x))) = rep (jet x)
  rw [hj]

/-- The commutator is the original theta boundary composed with its jet map. -/
theorem projector_commutator (theta : V →ₗ[R] B)
    (D : B →ₗ[R] B) (A : E →ₗ[R] E)
    (rep : E →ₗ[R] B) (jet : B →ₗ[R] E) (K : E →ₗ[R] V)
    (hb : ∀ x, D (rep x) = rep (A x) + theta (K x))
    (hj : ∀ x, jet (D x) = A (jet x)) :
    D.comp (packetProjector rep jet) -
      (packetProjector rep jet).comp D = theta.comp (K.comp jet) := by
  apply LinearMap.ext
  intro x
  change D (rep (jet x)) - rep (jet (D x)) = theta (K (jet x))
  rw [hb, hj]
  abel

theorem packet_annihilator (theta : V →ₗ[R] B) (jet : B →ₗ[R] E)
    (K : E →ₗ[R] V) (hj : ∀ v, jet (theta v) = 0) (v : V) :
    (K.comp jet) (theta v) = 0 := by
  change K (jet (theta v)) = 0
  rw [hj, map_zero]

/-- The full checked homotopy family applied to this exact packet commutator. -/
def allPacketHomotopies (theta : V →ₗ[R] B) (F : V ≃ₗ[R] V)
    (hTheta : Function.Injective theta) (jet : B →ₗ[R] E)
    (K : E →ₗ[R] V) (hj : ∀ v, jet (theta v) = 0) :
    ((B ⧸ LinearMap.range theta) →ₗ[R] V) ≃
      SplitZero.TauHomotopy.Homotopies theta F (K.comp jet) :=
  SplitZero.TauHomotopy.cochainHomotopyEquiv theta F hTheta (K.comp jet)
    (packet_annihilator theta jet K hj)

/-- Replacing a representative by an admitted boundary preserves its actual jets. -/
theorem representative_jets (theta : V →ₗ[R] B) (rep : E →ₗ[R] B)
    (jet : B →ₗ[R] E) (b : E →ₗ[R] V)
    (hj : ∀ v, jet (theta v) = 0) (hr : ∀ x, jet (rep x) = x) (x : E) :
    jet ((rep - theta.comp b) x) = x := by
  change jet (rep x-theta (b x)) = x
  rw [map_sub, hr, hj, sub_zero]


section SupportedQuotient
open SplitZero.Reconstruction SplitZero.JointHomotopy

/-- The original quotient transport with its change to the next active support. -/
def quotientTransportLift (U W : Submodule R B) (h : U ≤ W) :
    ReindexedHom (activeDiagram (R := R) (B := B ⧸ U))
      (activeDiagram (R := R) (B := B ⧸ W)) where
  index := syncIndex
  app A :=
    { toFun x := ⟨SplitZero.RelationLayer.transport U W h x.val, by
        intro hs
        have ha : A = ∅ := le_antisymm
          (by simpa only [hs] using le_sync A) bot_le
        rw [x.property ha, map_zero]⟩
      map_add' x y := Subtype.ext
        ((SplitZero.RelationLayer.transport U W h).map_add x.val y.val)
      map_smul' a x := Subtype.ext
        ((SplitZero.RelationLayer.transport U W h).map_smul a x.val) }
  naturality _ _ := rfl

/-- The new relation is killed at its specified target label, not sent to tau. -/
theorem quotientTransport_fibre_zero (U W : Submodule R B) (h : U ≤ W)
    (A : Mask) (x : activeFibre (R := R) (B := B ⧸ U) A)
    (hx : SplitZero.RelationLayer.transport U W h x.val = 0) :
    (quotientTransportLift U W h).total ⟨A, x⟩ =
      (⟨syncIndex A, 0⟩ : (activeDiagram (R := R) (B := B ⧸ W)).Total) := by
  apply ReindexedHom.killed_fibre
  apply Subtype.ext
  exact hx

theorem quotientTransport_not_absent (U W : Submodule R B) (h : U ≤ W)
    (A : Mask) (hA : A ≠ ∅) (x : activeFibre (R := R) (B := B ⧸ U) A)
    (hx : SplitZero.RelationLayer.transport U W h x.val = 0) :
    (quotientTransportLift U W h).total ⟨A, x⟩ ≠ 0 := by
  rw [quotientTransport_fibre_zero U W h A x hx]
  apply LinearDiagram.fibre_zero_ne_global
  intro hs
  classical
  change syncIndex A = (∅ : Mask) at hs
  simpa [syncIndex, hA] using hs

end SupportedQuotient

end SplitZero.BoundaryIntegration
