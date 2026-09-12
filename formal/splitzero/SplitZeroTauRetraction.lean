import SplitZeroTauHomotopy
import Mathlib.Topology.Algebra.Module.Basic

/-!
# Retractions of the actual quotient and their equivariance defects

The input is a retraction of a specified linear map, not a claim that the
analytic theta retraction has already been constructed in Lean. The section
of its cokernel is constructed, not assumed. The operators, their cocycle,
and changes of representatives keep that very quotient.
-/
noncomputable section
namespace SplitZero.TauRetraction
universe u v

structure Data (R V B : Type u) [CommRing R]
    [AddCommGroup V] [Module R V] [AddCommGroup B] [Module R B] where
  theta : V →ₗ[R] B
  lambda : B →ₗ[R] V
  left_inverse : Function.LeftInverse lambda theta

variable {R V B : Type u} [CommRing R]
  [AddCommGroup V] [Module R V] [AddCommGroup B] [Module R B]

namespace Data
variable (S : Data R V B)

abbrev Q := B ⧸ LinearMap.range S.theta
abbrev q : B →ₗ[R] S.Q := (LinearMap.range S.theta).mkQ

theorem theta_injective : Function.Injective S.theta := S.left_inverse.injective
@[simp] theorem retract_theta (v : V) : S.lambda (S.theta v) = v := S.left_inverse v
@[simp] theorem q_theta (v : V) : S.q (S.theta v) = 0 :=
  (Submodule.Quotient.mk_eq_zero _).mpr ⟨v, rfl⟩

def projection : B →ₗ[R] B := LinearMap.id - S.theta.comp S.lambda
@[simp] theorem projection_apply (b : B) :
    S.projection b = b - S.theta (S.lambda b) := rfl
@[simp] theorem projection_theta (v : V) : S.projection (S.theta v) = 0 := by
  rw [projection_apply, retract_theta, sub_self]
@[simp] theorem lambda_projection (b : B) : S.lambda (S.projection b) = 0 := by
  rw [projection_apply, map_sub, retract_theta, sub_self]

theorem projection_idempotent : S.projection.comp S.projection = S.projection := by
  apply LinearMap.ext
  intro b
  change S.projection b - S.theta (S.lambda (S.projection b)) = S.projection b
  rw [lambda_projection, map_zero, sub_zero]

theorem ker_projection : LinearMap.ker S.projection = LinearMap.range S.theta := by
  apply le_antisymm
  · intro b hb
    change b - S.theta (S.lambda b) = 0 at hb
    exact ⟨S.lambda b, (sub_eq_zero.mp hb).symm⟩
  · rintro b ⟨v, rfl⟩
    exact S.projection_theta v

theorem range_projection : LinearMap.range S.projection = LinearMap.ker S.lambda := by
  apply le_antisymm
  · rintro b ⟨x, rfl⟩
    exact S.lambda_projection x
  · intro b hb
    refine ⟨b, ?_⟩
    change S.lambda b = 0 at hb
    rw [projection_apply, hb, map_zero, sub_zero]

/-- The section is induced from id - theta lambda through the original quotient. -/
def sectionMap : S.Q →ₗ[R] B :=
  (LinearMap.range S.theta).liftQ S.projection (by
    rintro b ⟨v, rfl⟩
    exact S.projection_theta v)

@[simp] theorem section_mk (b : B) : S.sectionMap (S.q b) = S.projection b := rfl

@[simp] theorem quotient_section (u : S.Q) : S.q (S.sectionMap u) = u := by
  obtain ⟨b, rfl⟩ := Submodule.Quotient.mk_surjective (LinearMap.range S.theta) u
  change S.q (b - S.theta (S.lambda b)) = S.q b
  rw [map_sub, q_theta, sub_zero]

@[simp] theorem lambda_section (u : S.Q) : S.lambda (S.sectionMap u) = 0 := by
  obtain ⟨b, rfl⟩ := Submodule.Quotient.mk_surjective (LinearMap.range S.theta) u
  exact S.lambda_projection b

theorem decompose (b : B) : S.theta (S.lambda b) + S.sectionMap (S.q b) = b := by
  change S.theta (S.lambda b) + (b - S.theta (S.lambda b)) = b
  abel

def splitEquiv : (V × S.Q) ≃ₗ[R] B where
  toFun p := S.theta p.1 + S.sectionMap p.2
  invFun b := (S.lambda b, S.q b)
  left_inv p := by
    apply Prod.ext
    · change S.lambda (S.theta p.1 + S.sectionMap p.2) = p.1
      rw [map_add, retract_theta, lambda_section, add_zero]
    · change S.q (S.theta p.1 + S.sectionMap p.2) = p.2
      rw [map_add, q_theta, quotient_section, zero_add]
  right_inv b := S.decompose b
  map_add' p p' := by simp only [Prod.fst_add, Prod.snd_add, map_add]; abel
  map_smul' a p := by
    change S.theta (a • p.1) + S.sectionMap (a • p.2) =
      a • (S.theta p.1 + S.sectionMap p.2)
    rw [map_smul, map_smul, smul_add]

/-- The same input can be any finite packet map; no spectral assumption is inserted. -/
theorem normalize_representative {E : Type u} [AddCommGroup E] [Module R E]
    (f : E →ₗ[R] B) :
    S.sectionMap.comp (S.q.comp f) = f - S.theta.comp (S.lambda.comp f) := rfl

def changeSection (b : S.Q →ₗ[R] V) : S.Q →ₗ[R] B := S.sectionMap + S.theta.comp b

@[simp] theorem quotient_changeSection (b : S.Q →ₗ[R] V) (u : S.Q) :
    S.q (S.changeSection b u) = u := by
  change S.q (S.sectionMap u + S.theta (b u)) = u
  rw [map_add, quotient_section, q_theta, add_zero]

/-- Every other section has a uniquely determined change in the original source. -/
theorem section_change (s' : S.Q →ₗ[R] B) (hs' : ∀ u, S.q (s' u) = u) :
    s' = S.changeSection (S.lambda.comp s') := by
  apply LinearMap.ext
  intro u
  have h := S.decompose (s' u)
  rw [hs' u] at h
  change s' u = S.sectionMap u + S.theta (S.lambda (s' u))
  exact h.symm.trans (add_comm _ _)

theorem changeSection_injective : Function.Injective S.changeSection := by
  intro b c h
  apply LinearMap.ext
  intro u
  have hh := congrArg S.lambda (LinearMap.congr_fun h u)
  change S.lambda (S.sectionMap u + S.theta (b u)) =
    S.lambda (S.sectionMap u + S.theta (c u)) at hh
  simpa only [map_add, lambda_section, retract_theta, zero_add] using hh

structure Operator where
  onV : V →ₗ[R] V
  onB : B →ₗ[R] B
  intertwines : ∀ v, onB (S.theta v) = S.theta (onV v)

namespace Operator
variable {S} (A C : S.Operator)

def onQuotient : S.Q →ₗ[R] S.Q :=
  (LinearMap.range S.theta).mapQ (LinearMap.range S.theta) A.onB (by
    rintro b ⟨v, rfl⟩
    exact ⟨A.onV v, (A.intertwines v).symm⟩)

@[simp] theorem quotient_intertwines (b : B) :
    S.q (A.onB b) = A.onQuotient (S.q b) := rfl

def defect : S.Q →ₗ[R] V := S.lambda.comp (A.onB.comp S.sectionMap)

/-- The exact off-diagonal term of the original operator. -/
theorem block_section (u : S.Q) :
    A.onB (S.sectionMap u) = S.theta (A.defect u) + S.sectionMap (A.onQuotient u) := by
  have h := (S.decompose (A.onB (S.sectionMap u))).symm
  rw [quotient_intertwines, S.quotient_section] at h
  exact h

def comp : S.Operator where
  onV := A.onV.comp C.onV
  onB := A.onB.comp C.onB
  intertwines v := by
    change A.onB (C.onB (S.theta v)) = S.theta (A.onV (C.onV v))
    rw [C.intertwines, A.intertwines]

theorem onQuotient_comp : (A.comp C).onQuotient = A.onQuotient.comp C.onQuotient := by
  apply LinearMap.ext
  intro u
  obtain ⟨b, rfl⟩ := Submodule.Quotient.mk_surjective (LinearMap.range S.theta) u
  rfl

/-- Composition law; for a group action this is precisely its cocycle equation. -/
theorem defect_comp :
    (A.comp C).defect = A.onV.comp C.defect + A.defect.comp C.onQuotient := by
  apply LinearMap.ext
  intro u
  change S.lambda (A.onB (C.onB (S.sectionMap u))) =
    A.onV (C.defect u) + S.lambda (A.onB (S.sectionMap (C.onQuotient u)))
  rw [C.block_section u, map_add, A.intertwines, map_add, S.retract_theta]

def changeDefect (b : S.Q →ₗ[R] V) : S.Q →ₗ[R] V :=
  A.defect + A.onV.comp b - b.comp A.onQuotient

/-- A change of representatives changes the defect by exactly this coboundary. -/
theorem changed_block (b : S.Q →ₗ[R] V) (u : S.Q) :
    A.onB (S.changeSection b u) =
      S.theta (A.changeDefect b u) + S.changeSection b (A.onQuotient u) := by
  change A.onB (S.sectionMap u + S.theta (b u)) =
    S.theta (A.defect u + A.onV (b u) - b (A.onQuotient u)) +
      (S.sectionMap (A.onQuotient u) + S.theta (b (A.onQuotient u)))
  rw [map_add, A.intertwines, A.block_section]
  rw [map_sub, map_add]
  abel

/-- Equivariance is equivalent to vanishing of the computed defect, not assumed. -/
theorem changed_equivariant_iff (b : S.Q →ₗ[R] V) :
    A.onB.comp (S.changeSection b) = (S.changeSection b).comp A.onQuotient ↔
      A.changeDefect b = 0 := by
  constructor
  · intro h
    apply LinearMap.ext
    intro u
    have hu := LinearMap.congr_fun h u
    change A.onB (S.changeSection b u) = S.changeSection b (A.onQuotient u) at hu
    rw [A.changed_block b u] at hu
    have hz : S.theta (A.changeDefect b u) = 0 := by
      have hh := congrArg (fun z : B => z - S.changeSection b (A.onQuotient u)) hu
      simpa only [add_sub_cancel_right, sub_self] using hh
    exact S.theta_injective (hz.trans S.theta.map_zero.symm)
  · intro h
    apply LinearMap.ext
    intro u
    change A.onB (S.changeSection b u) = S.changeSection b (A.onQuotient u)
    rw [A.changed_block b u, h, LinearMap.zero_apply, map_zero, zero_add]
end Operator

section Topology
variable [TopologicalSpace V] [TopologicalSpace B] [ContinuousSub B]

theorem projection_continuous (hTheta : Continuous S.theta) (hLambda : Continuous S.lambda) :
    Continuous S.projection := continuous_id.sub (hTheta.comp hLambda)

/-- Valid for the actual locally convex topologies; no Banach norm is assumed. -/
theorem closed_range [T2Space B]
    (hTheta : Continuous S.theta) (hLambda : Continuous S.lambda) :
    IsClosed (Set.range S.theta) := by
  have h : Set.range S.theta = S.projection ⁻¹' ({0} : Set B) := by
    ext b
    constructor
    · rintro ⟨v, rfl⟩
      exact S.projection_theta v
    · intro hb
      change b - S.theta (S.lambda b) = 0 at hb
      exact ⟨S.lambda b, (sub_eq_zero.mp hb).symm⟩
  rw [h]
  exact isClosed_singleton.preimage (S.projection_continuous hTheta hLambda)
end Topology
end Data

section ReconstructionInput
variable {W : Type u} [AddCommGroup W] [Module R W]

/-- The algebraic reconstruction formula P N Y, with the inverse and moment maps explicit. -/
def fromReconstruction (theta : V →ₗ[R] B) (i : V →ₗ[R] W)
    (P : W →ₗ[R] V) (T N : W →ₗ[R] W) (Y : B →ₗ[R] W)
    (hP : ∀ v, P (i v) = v)
    (hN : ∀ w, N (w - T w) = w)
    (hY : ∀ v, Y (theta v) = i v - T (i v)) : Data R V B where
  theta := theta
  lambda := P.comp (N.comp Y)
  left_inverse v := by
    change P (N (Y (theta v))) = v
    rw [hY, hN, hP]
end ReconstructionInput

section Supported
open SplitZero.Reconstruction
variable {L : Type v} [SemilatticeSup L] [OrderBot L]
  {D E : LinearDiagram R L}
variable (theta : Hom D E) (lambda : Hom E D)

def residualHom : Hom E E where
  app i := LinearMap.id - (theta.app i).comp (lambda.app i)
  naturality h x := by
    change E.map h x - theta.app _ (lambda.app _ (E.map h x)) =
      E.map h (x - theta.app _ (lambda.app _ x))
    rw [lambda.naturality, theta.naturality, map_sub]

theorem supported_left_inverse
    (h : ∀ i (x : D.V i), lambda.app i (theta.app i x) = x) (x : D.Total) :
    lambda.total (theta.total x) = x := by
  rcases x with ⟨i, x⟩
  change (⟨i, lambda.app i (theta.app i x)⟩ : D.Total) = ⟨i, x⟩
  rw [h]

/-- A killed theta boundary lands at the same fibre zero, not at external absence. -/
theorem supported_boundary
    (h : ∀ i (x : D.V i), lambda.app i (theta.app i x) = x) (x : D.Total) :
    (residualHom theta lambda).total (theta.total x) = (e : G R) • theta.total x := by
  rcases x with ⟨i, x⟩
  change (⟨i, theta.app i x - theta.app i (lambda.app i (theta.app i x))⟩ : E.Total) =
    (e : G R) • (⟨i, theta.app i x⟩ : E.Total)
  rw [h, sub_self, LinearDiagram.supported_zero_action]

theorem residual_idempotent
    (h : ∀ i (x : D.V i), lambda.app i (theta.app i x) = x) (x : E.Total) :
    (residualHom theta lambda).total ((residualHom theta lambda).total x) =
      (residualHom theta lambda).total x := by
  rcases x with ⟨i, x⟩
  have hz : lambda.app i (x - theta.app i (lambda.app i x)) = 0 := by
    rw [map_sub, h, sub_self]
  change (⟨i, (x - theta.app i (lambda.app i x)) -
      theta.app i (lambda.app i (x - theta.app i (lambda.app i x)))⟩ : E.Total) =
    ⟨i, x - theta.app i (lambda.app i x)⟩
  rw [hz, map_zero, sub_zero]
end Supported
end SplitZero.TauRetraction
