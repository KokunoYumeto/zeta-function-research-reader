import SplitZeroTauHomotopy
import SplitZeroSupportChange
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

end SplitZero.BoundaryIntegration
