import SplitZeroRelationLayer
import Mathlib.Tactic

/-!
# The local orthogonal relation layer produces the control form

The input is one adjacent pair of the source note's finite Krylov stages.
The scalar core and arithmetic quotient are not changed. The analytic source
must supply its integration-by-parts identity and its one-layer escape law.
The control form is defined from A and the actual residual representative,
then derived from these inputs; the rank-two formula is not an input.
The ambient inner-product space need not be complete. In particular, D is
only required on the original test-function space, not on all of L2.
-/
noncomputable section
namespace SplitZero.BoundaryControl
universe u v
variable {E : Type u} {H : Type v}
  [AddCommGroup E] [Module ℂ E]
  [NormedAddCommGroup H] [InnerProductSpace ℂ H]
local notation "⟪" x ", " y "⟫" => inner ℂ x y

structure Data where
  lower : Submodule ℂ H
  [hasProjection : lower.HasOrthogonalProjection]
  source : E →ₗ[ℂ] H
  action : E →ₗ[ℂ] E
  deriv : H →ₗ[ℂ] H
  fzero : H
  extensionRow : E →ₗ[ℂ] ℂ
  fzero_mem : fzero ∈ lower
  source_boundary : ∀ x, deriv (source x) = source (action x) + extensionRow x • fzero
  green : ∀ x y, ⟪deriv x, y⟫ + ⟪x, deriv y⟫ = ⟪x, y⟫
  nextVector : H
  next_orthogonal : ∀ z ∈ lower, ⟪nextVector, z⟫ = 0
  normSquare : ℝ
  next_norm : ⟪nextVector, nextVector⟫ = (normSquare : ℂ)
  currentRow : E →ₗ[ℂ] ℂ
  nextRow : E →ₗ[ℂ] ℂ
  next_pair : ∀ x, ⟪nextVector, source x⟫ = (normSquare : ℂ) * nextRow x
  escape : ∀ x,
    deriv (lower.starProjection (source x)) -
      lower.starProjection (deriv (lower.starProjection (source x))) =
        currentRow x • nextVector

attribute [instance] Data.hasProjection
namespace Data
variable (S : Data (E := E) (H := H))

def representative : E →ₗ[ℂ] H :=
  S.source - S.lower.starProjection.toLinearMap.comp S.source

@[simp] theorem representative_apply (x : E) :
    S.representative x = S.source x - S.lower.starProjection (S.source x) := rfl

theorem representative_orthogonal (x : E) (z : H) (hz : z ∈ S.lower) :
    ⟪S.representative x, z⟫ = 0 :=
  Submodule.starProjection_inner_eq_zero (S.source x) z hz

def boundary : E →ₗ[ℂ] H :=
  S.deriv.comp S.representative - S.representative.comp S.action

theorem boundary_apply (x : E) :
    S.boundary x = S.extensionRow x • S.fzero -
      S.deriv (S.lower.starProjection (S.source x)) +
      S.lower.starProjection (S.source (S.action x)) := by
  change S.deriv (S.source x - S.lower.starProjection (S.source x)) -
      (S.source (S.action x) - S.lower.starProjection (S.source (S.action x))) = _
  rw [map_sub, S.source_boundary]
  abel

/-- The form A*G+GA-G, before any use of its boundary representation. -/
def control (x y : E) : ℂ :=
  ⟪S.representative (S.action x), S.representative y⟫ +
  ⟪S.representative x, S.representative (S.action y)⟫ -
  ⟪S.representative x, S.representative y⟫

theorem control_boundary (x y : E) :
    S.control x y = -(⟪S.representative x, S.boundary y⟫ +
      ⟪S.boundary x, S.representative y⟫) := by
  change _ = -(⟪S.representative x,
      S.deriv (S.representative y) - S.representative (S.action y)⟫ +
    ⟪S.deriv (S.representative x) - S.representative (S.action x),
      S.representative y⟫)
  rw [inner_sub_right, inner_sub_left]
  unfold control
  rw [← S.green (S.representative x) (S.representative y)]
  ring

theorem control_cross (x y : E) :
    S.control x y =
      ⟪S.representative x, S.deriv (S.lower.starProjection (S.source y))⟫ +
      ⟪S.deriv (S.lower.starProjection (S.source x)), S.representative y⟫ := by
  rw [S.control_boundary, S.boundary_apply, S.boundary_apply]
  have h0 (z : E) : ⟪S.representative z, S.fzero⟫ = 0 :=
    S.representative_orthogonal z S.fzero S.fzero_mem
  have h0' (z : E) : ⟪S.fzero, S.representative z⟫ = 0 := inner_eq_zero_symm.mp (h0 z)
  have hp (z : E) (w : H) : ⟪S.representative z, S.lower.starProjection w⟫ = 0 :=
    S.representative_orthogonal z _ (S.lower.starProjection_apply_mem w)
  have hp' (z : E) (w : H) : ⟪S.lower.starProjection w, S.representative z⟫ = 0 :=
    inner_eq_zero_symm.mp (hp z w)
  simp only [inner_add_right, inner_sub_right, inner_smul_right,
    inner_add_left, inner_sub_left, inner_smul_left, h0, h0', hp, hp', mul_zero]
  ring

theorem next_pair_representative (x : E) :
    ⟪S.nextVector, S.representative x⟫ = (S.normSquare : ℂ) * S.nextRow x := by
  rw [S.representative_apply, inner_sub_right, S.next_pair,
    S.next_orthogonal _ (S.lower.starProjection_apply_mem _), sub_zero]

theorem representative_pair_next (x : E) :
    ⟪S.representative x, S.nextVector⟫ =
      (S.normSquare : ℂ) * star (S.nextRow x) := by
  rw [← inner_conj_symm (S.representative x) S.nextVector, S.next_pair_representative]
  simp

/-- The source note's rank-two expression is derived from the actual boundary. -/
theorem rank_two_formula (x y : E) :
    S.control x y = (S.normSquare : ℂ) *
      (star (S.nextRow x) * S.currentRow y +
       star (S.currentRow x) * S.nextRow y) := by
  rw [S.control_cross]
  have hr := congrArg (fun z => ⟪S.representative x, z⟫) (S.escape y)
  rw [inner_sub_right,
    S.representative_orthogonal x _ (S.lower.starProjection_apply_mem _),
    sub_zero, inner_smul_right] at hr
  have hl := congrArg (fun z => ⟪z, S.representative y⟫) (S.escape x)
  have hp : ⟪S.lower.starProjection (S.deriv (S.lower.starProjection (S.source x))),
      S.representative y⟫ = 0 :=
    inner_eq_zero_symm.mp (S.representative_orthogonal y _
      (S.lower.starProjection_apply_mem _))
  rw [inner_sub_left, hp, sub_zero, inner_smul_left] at hl
  rw [hr, hl, S.representative_pair_next, S.next_pair_representative]
  simp only [starRingEnd_apply]
  ring

/-- The next residual, with the new relation's original unscaled norm retained. -/
def nextRepresentative : E →ₗ[ℂ] H :=
  S.representative - S.nextRow.smulRight S.nextVector

theorem gram_downdate (x y : E) :
    ⟪S.representative x, S.representative y⟫ -
      ⟪S.nextRepresentative x, S.nextRepresentative y⟫ =
        (S.normSquare : ℂ) * star (S.nextRow x) * S.nextRow y := by
  change _ - ⟪S.representative x - S.nextRow x • S.nextVector,
    S.representative y - S.nextRow y • S.nextVector⟫ = _
  simp only [inner_sub_left, inner_sub_right, inner_smul_left, inner_smul_right,
    S.next_pair_representative, S.representative_pair_next, S.next_norm, starRingEnd_apply]
  ring

/-- The same one-dimensional escape is retained in the old quotient. -/
theorem boundary_quotient (x : E) :
    S.lower.mkQ (S.boundary x) =
      -(S.currentRow x • S.lower.mkQ S.nextVector) := by
  have hp (z : H) : S.lower.mkQ (S.lower.starProjection z) = 0 :=
    (Submodule.Quotient.mk_eq_zero S.lower).mpr (S.lower.starProjection_apply_mem z)
  have h0 : S.lower.mkQ S.fzero = 0 :=
    (Submodule.Quotient.mk_eq_zero S.lower).mpr S.fzero_mem
  have he := congrArg S.lower.mkQ (S.escape x)
  rw [map_sub, hp, sub_zero, map_smul] at he
  rw [S.boundary_apply, map_add, map_sub, map_smul, h0, smul_zero, hp,
    add_zero, zero_sub, he]
end Data
end SplitZero.BoundaryControl
