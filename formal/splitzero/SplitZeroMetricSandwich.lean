import SplitZeroMetricVariationSupport

/-!
# Source enclosures on the original canonical quotient

The relation matrix B, its source coordinates, and the quotient lifts C stay
fixed. Both scaled secants retain the actual boundary Gram. This extends the
existing Metric structure; it does not replace the arithmetic metric.
-/
noncomputable section
namespace SplitZero.MetricSandwich
open Matrix MetricVariation Reconstruction
open scoped ComplexOrder
variable {j n m : Type*} [Fintype j] [Fintype m] [DecidableEq m]
variable {B : Matrix j m ℂ}

/-- Lower scaled secant with its original-source boundary contribution. -/
theorem lower_identity (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (a : ℝ) :
    M₁.quotientGram C - a • M₀.quotientGram C =
      MetricVariation.gram (M₁.form - a • M₀.form) (M₁.sectionMap C) +
        a • MetricVariation.gram M₀.form (M₁.sectionMap C - M₀.sectionMap C) := by
  have hexpand : MetricVariation.gram (M₁.form - a • M₀.form) (M₁.sectionMap C) =
      M₁.quotientGram C - a • MetricVariation.gram M₀.form (M₁.sectionMap C) := by
    simp only [MetricVariation.gram, Metric.quotientGram, Matrix.mul_sub, Matrix.sub_mul,
      Matrix.mul_smul, Matrix.smul_mul]
  rw [hexpand, Metric.pythagoras M₀ M₁ C, smul_add]
  abel

/-- Upper scaled secant uses the receiving source metric on the boundary. -/
theorem upper_identity (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (b : ℝ) :
    b • M₀.quotientGram C - M₁.quotientGram C =
      MetricVariation.gram (b • M₀.form - M₁.form) (M₀.sectionMap C) +
        MetricVariation.gram M₁.form (M₁.sectionMap C - M₀.sectionMap C) := by
  have hneg : MetricVariation.gram M₁.form (M₀.sectionMap C - M₁.sectionMap C) =
      MetricVariation.gram M₁.form (M₁.sectionMap C - M₀.sectionMap C) := by
    rw [← neg_sub (M₁.sectionMap C) (M₀.sectionMap C)]
    simp only [MetricVariation.gram, Matrix.conjTranspose_neg, Matrix.neg_mul, Matrix.mul_neg, neg_neg]
  have hexpand : MetricVariation.gram (b • M₀.form - M₁.form) (M₀.sectionMap C) =
      b • M₀.quotientGram C - MetricVariation.gram M₁.form (M₀.sectionMap C) := by
    simp only [MetricVariation.gram, Metric.quotientGram, Matrix.mul_sub, Matrix.sub_mul,
      Matrix.mul_smul, Matrix.smul_mul]
  rw [hexpand, Metric.pythagoras M₁ M₀ C, hneg]
  abel

/-- Source Loewner bounds pass through the canonical minimum, not a chosen section. -/
theorem sandwich [Fintype n] (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (a b : ℝ)
    (ha : 0 ≤ a) (hM₀ : M₀.form.PosSemidef) (hM₁ : M₁.form.PosSemidef)
    (hLower : (M₁.form - a • M₀.form).PosSemidef)
    (hUpper : (b • M₀.form - M₁.form).PosSemidef) :
    (M₁.quotientGram C - a • M₀.quotientGram C).PosSemidef ∧
      (b • M₀.quotientGram C - M₁.quotientGram C).PosSemidef := by
  constructor
  · rw [lower_identity]
    exact (hLower.conjTranspose_mul_mul_same _).add
      ((hM₀.conjTranspose_mul_mul_same _).smul ha)
  · rw [upper_identity]
    exact (hUpper.conjTranspose_mul_mul_same _).add
      (hM₁.conjTranspose_mul_mul_same _)

variable {L : Type*} [SemilatticeSup L] [OrderBot L] {D : LinearDiagram ℂ L}

/-- The same metric enclosure is attached to equality in the ORIGINAL quotient. -/
theorem supported_sandwich [Fintype n] (Brel : Relations D) (i : L)
    (coord : D.V i ≃ₗ[ℂ] (j → ℂ)) (C : Matrix j n ℂ) (M₀ M₁ : Metric B)
    (hB : ∀ w, coord.symm (B *ᵥ w) ∈ Brel.fibre i) (v : n → ℂ)
    (a b : ℝ) (ha : 0 ≤ a)
    (hM₀ : M₀.form.PosSemidef) (hM₁ : M₁.form.PosSemidef)
    (hLower : (M₁.form - a • M₀.form).PosSemidef)
    (hUpper : (b • M₀.form - M₁.form).PosSemidef) :
    Brel.quotientMap.total ⟨i, coord.symm (M₁.sectionMap C *ᵥ v)⟩ =
      Brel.quotientMap.total ⟨i, coord.symm (M₀.sectionMap C *ᵥ v)⟩ ∧
    (M₁.quotientGram C - a • M₀.quotientGram C).PosSemidef ∧
    (b • M₀.quotientGram C - M₁.quotientGram C).PosSemidef := by
  exact ⟨MetricVariationSupport.canonical_metric_class Brel i coord B C M₀ M₁ hB v,
    sandwich M₀ M₁ C a b ha hM₀ hM₁ hLower hUpper⟩

end SplitZero.MetricSandwich
