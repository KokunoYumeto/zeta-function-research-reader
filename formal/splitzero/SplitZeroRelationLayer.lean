import SplitZeroSupportChange
import Mathlib.Analysis.InnerProductSpace.Projection.Basic

/-!
# The admitted relation layer and its original quotient maps

For L <= M and a retraction P onto L, construct M/L ~= M inter ker(P).
The orthogonal instance uses Mathlib's actual starProjection. The derivative
has source B/L and target B/M; it is not made an endomorphism of B/L.
-/
noncomputable section
namespace SplitZero.RelationLayer
universe u v

structure Data (R : Type u) (B : Type v) [CommRing R] [AddCommGroup B] [Module R B] where
  lower : Submodule R B
  upper : Submodule R B
  inclusion : lower ≤ upper
  project : B →ₗ[R] B
  project_mem : ∀ b, project b ∈ lower
  project_fix : ∀ b ∈ lower, project b = b

variable {R : Type u} {B : Type v} [CommRing R] [AddCommGroup B] [Module R B]
namespace Data
variable (S : Data R B)

abbrev lowerInUpper : Submodule R S.upper := S.lower.comap S.upper.subtype
abbrev Layer := S.upper ⧸ S.lowerInUpper
abbrev Complement : Submodule R B := S.upper ⊓ LinearMap.ker S.project

def residual : B →ₗ[R] B := LinearMap.id - S.project

theorem project_idempotent (x : B) : S.project (S.project x) = S.project x :=
  S.project_fix _ (S.project_mem x)

def residualOnUpper : S.upper →ₗ[R] S.Complement where
  toFun x := ⟨x.val - S.project x.val,
    S.upper.sub_mem x.property (S.inclusion (S.project_mem x.val)), by
      change S.project (x.val - S.project x.val) = 0
      rw [map_sub, S.project_idempotent, sub_self]⟩
  map_add' x y := by
    apply Subtype.ext
    change (x.val + y.val) - S.project (x.val + y.val) =
      (x.val - S.project x.val) + (y.val - S.project y.val)
    rw [map_add]
    abel
  map_smul' a x := by
    apply Subtype.ext
    change a • x.val - S.project (a • x.val) = a • (x.val - S.project x.val)
    rw [map_smul, smul_sub]

def descend : S.Layer →ₗ[R] S.Complement :=
  S.lowerInUpper.liftQ S.residualOnUpper (by
    intro x hx
    apply Subtype.ext
    change x.val - S.project x.val = 0
    rw [S.project_fix x.val hx, sub_self])

/-- Explicit inverse: include the complementary vector and take its old class. -/
def layerEquiv : S.Layer ≃ₗ[R] S.Complement where
  toFun := S.descend
  invFun y := S.lowerInUpper.mkQ ⟨y.val, y.property.1⟩
  left_inv x := by
    obtain ⟨z, rfl⟩ := Submodule.Quotient.mk_surjective S.lowerInUpper x
    apply (Submodule.Quotient.eq S.lowerInUpper).mpr
    change z.val - S.project z.val - z.val ∈ S.lower
    have he : z.val - S.project z.val - z.val = -S.project z.val := by abel
    rw [he]
    exact S.lower.neg_mem (S.project_mem z.val)
  right_inv y := by
    apply Subtype.ext
    change y.val - S.project y.val = y.val
    have hy : S.project y.val = 0 := y.property.2
    rw [hy, sub_zero]
  map_add' := S.descend.map_add
  map_smul' := S.descend.map_smul

@[simp] theorem layerEquiv_mk (z : S.upper) :
    (S.layerEquiv (S.lowerInUpper.mkQ z)).val = z.val - S.project z.val := rfl

/-- The same ambient representative, with more relations admitted. -/
def transition : (B ⧸ S.lower) →ₗ[R] (B ⧸ S.upper) :=
  S.lower.mapQ S.upper LinearMap.id (by
    intro x hx
    exact S.inclusion hx)

@[simp] theorem transition_mk (x : B) :
    S.transition (S.lower.mkQ x) = S.upper.mkQ x := rfl

theorem transition_kills_iff (x : B) :
    S.transition (S.lower.mkQ x) = 0 ↔ x ∈ S.upper :=
  Submodule.Quotient.mk_eq_zero S.upper

/-- The derivative is defined between consecutive relation quotients. -/
def derivative (D : B →ₗ[R] B) (hD : ∀ x ∈ S.lower, D x ∈ S.upper) :
    (B ⧸ S.lower) →ₗ[R] (B ⧸ S.upper) :=
  S.lower.mapQ S.upper D hD

@[simp] theorem derivative_mk (D : B →ₗ[R] B)
    (hD : ∀ x ∈ S.lower, D x ∈ S.upper) (x : B) :
    S.derivative D hD (S.lower.mkQ x) = S.upper.mkQ (D x) := rfl

/-- A nonzero class at the old level is killed by the actual transition. -/
theorem retained_then_killed (u : B) (huM : u ∈ S.upper) (huL : u ∉ S.lower) :
    S.lower.mkQ u ≠ 0 ∧ S.transition (S.lower.mkQ u) = 0 := by
  constructor
  · intro h
    exact huL ((Submodule.Quotient.mk_eq_zero S.lower).mp h)
  · exact (S.transition_kills_iff u).mpr huM

/-- The boundary identity is retained in the old, not the final, quotient. -/
theorem defect_class (b l u : B) (a : R) (hl : l ∈ S.lower)
    (hb : b = l - a • u) : S.lower.mkQ b = -(a • S.lower.mkQ u) := by
  have hz : S.lower.mkQ l = 0 := (Submodule.Quotient.mk_eq_zero S.lower).mpr hl
  rw [hb, map_sub, map_smul, hz, zero_sub]
end Data

section Orthogonal
variable {H : Type v} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

def orthogonalData (L M : Submodule ℂ H) [L.HasOrthogonalProjection] (hLM : L ≤ M) :
    Data ℂ H where
  lower := L
  upper := M
  inclusion := hLM
  project := L.starProjection.toLinearMap
  project_mem x := L.starProjection_apply_mem x
  project_fix x hx := (Submodule.starProjection_eq_self_iff).mpr hx
end Orthogonal
end SplitZero.RelationLayer
