import SplitZeroMetricResolvent
import SplitZeroMetricVariationSupport

/-!
The source resolvent is integrated with the inherited supported quotient.
No equality between the full observation kernel and the old boundary family
is used. The raw source generator is not presumed to preserve finite degree.
-/
noncomputable section
namespace SplitZero.MetricResolventSupport
open Matrix
open SplitZero.Reconstruction
open MetricVariation
variable {j n m : Type*} [Fintype j] [Fintype n] [Fintype m] [DecidableEq m]
variable {B : Matrix j m ℂ}

/-- Exact path composition of the old-relation coefficients. -/
omit [Fintype n] in
theorem primitive_cocycle (M₀ M₁ M₂ : Metric B) (C : Matrix j n ℂ) :
    MetricResolvent.primitive M₀ M₂ C = MetricResolvent.primitive M₀ M₁ C +
      MetricResolvent.primitive M₁ M₂ C := by
  simp only [MetricResolvent.primitive_eq_correction]
  abel

/-- Retain the entire change in the actual source-generator comparison. -/
theorem generator_defect (M₀ M₁ : Metric B) (C : Matrix j n ℂ)
    (D : Matrix j j ℂ) (A : Matrix n n ℂ) :
    (D * M₁.sectionMap C - M₁.sectionMap C * A) -
      (D * M₀.sectionMap C - M₀.sectionMap C * A) =
      -(D * (B * MetricResolvent.primitive M₀ M₁ C)) +
        (B * MetricResolvent.primitive M₀ M₁ C) * A := by
  simp only [MetricResolvent.section_update M₀ M₁ C, Matrix.mul_sub, Matrix.sub_mul]
  abel

variable {L : Type*} [SemilatticeSup L] [OrderBot L]
  {D : LinearDiagram ℂ L}

/-- The exact source difference, not merely its finite jet, is an old boundary. -/
theorem perturbation_membership (Brel : Relations D) (i : L)
    (coord : D.V i ≃ₗ[ℂ] (j → ℂ))
    (C : Matrix j n ℂ) (M₀ M₁ : Metric B)
    (hB : ∀ w, coord.symm (B *ᵥ w) ∈ Brel.fibre i) (v : n → ℂ) :
    coord.symm ((M₁.sectionMap C - M₀.sectionMap C) *ᵥ v) ∈ Brel.fibre i := by
  rw [MetricResolvent.section_difference, Matrix.neg_mulVec, map_neg]
  apply (Brel.fibre i).neg_mem
  rw [← Matrix.mulVec_mulVec]
  exact hB _

/-- This same computed relation goes to its nonbottom fibre zero, not absence. -/
theorem perturbation_supported_zero (Brel : Relations D) (i : L) (hi : i ≠ ⊥)
    (coord : D.V i ≃ₗ[ℂ] (j → ℂ))
    (C : Matrix j n ℂ) (M₀ M₁ : Metric B)
    (hB : ∀ w, coord.symm (B *ᵥ w) ∈ Brel.fibre i) (v : n → ℂ) :
    Brel.quotientMap.total ⟨i,coord.symm ((M₁.sectionMap C - M₀.sectionMap C) *ᵥ v)⟩ =
      (⟨i,0⟩ : Brel.quotientDiagram.Total) ∧
    Brel.quotientMap.total ⟨i,coord.symm ((M₁.sectionMap C - M₀.sectionMap C) *ᵥ v)⟩ ≠ 0 :=
  MetricVariationSupport.boundary_retained Brel i hi _
    (perturbation_membership Brel i coord C M₀ M₁ hB v)

/-- Equality in the original internal quotient, not in a substituted finite target. -/
theorem original_class_unchanged (Brel : Relations D) (i : L)
    (coord : D.V i ≃ₗ[ℂ] (j → ℂ))
    (C : Matrix j n ℂ) (M₀ M₁ : Metric B)
    (hB : ∀ w, coord.symm (B *ᵥ w) ∈ Brel.fibre i) (v : n → ℂ) :
    Brel.quotientMap.total ⟨i,coord.symm (M₁.sectionMap C *ᵥ v)⟩ =
      Brel.quotientMap.total ⟨i,coord.symm (M₀.sectionMap C *ᵥ v)⟩ := by
  apply (Brel.quotient_same_label_iff i _ _).mpr
  rw [← map_sub, ← Matrix.sub_mulVec]
  exact perturbation_membership Brel i coord C M₀ M₁ hB v

end SplitZero.MetricResolventSupport
