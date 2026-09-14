import SplitZeroMetricVariationSupport

/-!
Source-metric bounds for the original canonical quotient.

B and C remain fixed. Every comparison retains the explicit
old-boundary difference between the two canonical sections.
-/

noncomputable section

namespace SplitZero.MetricSandwich

open Matrix MetricVariation Reconstruction

variable {j n m : Type*}
  [Fintype j] [Fintype n] [Fintype m] [DecidableEq m]
  {B : Matrix j m ℂ}

/-- The lower scaled comparison, including its original boundary Gram. -/
theorem lower_identity
    (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (a : ℝ) :
    M₁.quotientGram C - a • M₀.quotientGram C =
      gram (M₁.form - a • M₀.form) (M₁.sectionMap C) +
        a • gram M₀.form
          (M₁.sectionMap C - M₀.sectionMap C) := by
  have hexpand :
      gram (M₁.form - a • M₀.form) (M₁.sectionMap C) =
        M₁.quotientGram C -
          a • gram M₀.form (M₁.sectionMap C) := by
    simp only [gram, Metric.quotientGram,
      Matrix.mul_sub, Matrix.sub_mul,
      Matrix.mul_smul, Matrix.smul_mul]
  rw [hexpand, Metric.pythagoras M₀ M₁ C, smul_add]
  abel

/-- The upper scaled comparison uses the other source metric on the boundary. -/
theorem upper_identity
    (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (b : ℝ) :
    b • M₀.quotientGram C - M₁.quotientGram C =
      gram (b • M₀.form - M₁.form) (M₀.sectionMap C) +
        gram M₁.form
          (M₁.sectionMap C - M₀.sectionMap C) := by
  have hneg :
      gram M₁.form
          (M₀.sectionMap C - M₁.sectionMap C) =
        gram M₁.form
          (M₁.sectionMap C - M₀.sectionMap C) := by
    have he :
        M₀.sectionMap C - M₁.sectionMap C =
          -(M₁.sectionMap C - M₀.sectionMap C) := by
      abel
    rw [he]
    simp only [gram, Matrix.conjTranspose_neg,
      Matrix.neg_mul, Matrix.mul_neg, neg_neg]
  have hexpand :
      gram (b • M₀.form - M₁.form) (M₀.sectionMap C) =
        b • M₀.quotientGram C -
          gram M₁.form (M₀.sectionMap C) := by
    simp only [gram, Metric.quotientGram,
      Matrix.mul_sub, Matrix.sub_mul,
      Matrix.mul_smul, Matrix.smul_mul]
  rw [hexpand, Metric.pythagoras M₁ M₀ C, hneg]
  abel

/-- A source sandwich descends to the canonical quotient Grams. -/
theorem sandwich
    (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (a b : ℝ)
    (ha : 0 ≤ a)
    (hM₀ : M₀.form.PosSemidef)
    (hM₁ : M₁.form.PosSemidef)
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

variable {L : Type*} [SemilatticeSup L] [OrderBot L]
  {D : LinearDiagram ℂ L}

/-- The metric bounds accompany equality in the ORIGINAL supported quotient. -/
theorem supported_sandwich
    (Brel : Relations D) (i : L)
    (coord : D.V i ≃ₗ[ℂ] (j → ℂ))
    (C : Matrix j n ℂ) (M₀ M₁ : Metric B)
    (hB : ∀ w, coord.symm (B *ᵥ w) ∈ Brel.fibre i)
    (v : n → ℂ) (a b : ℝ)
    (ha : 0 ≤ a)
    (hM₀ : M₀.form.PosSemidef)
    (hM₁ : M₁.form.PosSemidef)
    (hLower : (M₁.form - a • M₀.form).PosSemidef)
    (hUpper : (b • M₀.form - M₁.form).PosSemidef) :
    Brel.quotientMap.total
        ⟨i, coord.symm (M₁.sectionMap C *ᵥ v)⟩ =
      Brel.quotientMap.total
        ⟨i, coord.symm (M₀.sectionMap C *ᵥ v)⟩ ∧
    (M₁.quotientGram C - a • M₀.quotientGram C).PosSemidef ∧
    (b • M₀.quotientGram C - M₁.quotientGram C).PosSemidef := by
  exact ⟨
    MetricVariationSupport.canonical_metric_class
      Brel i coord B C M₀ M₁ hB v,
    sandwich M₀ M₁ C a b ha hM₀ hM₁ hLower hUpper⟩

end SplitZero.MetricSandwich
