import SplitZeroWeightedQuotientVolume
import Mathlib.LinearAlgebra.Matrix.PosDef

/-!
# Two canonical metrics on the same original source and relation map

All residuals use WeightedQuotientVolume.residual.  B and C never change.
The secant remainder is the Gram of an actual B-boundary, not an error
assigned a favourable sign.  Positivity is needed only for the order results.
-/
noncomputable section
namespace SplitZero.MetricVariation
open Matrix
open scoped ComplexOrder
variable {j n m : Type*} [Fintype j] [Fintype m] [DecidableEq m]

def gram (M : Matrix j j ℂ) (R : Matrix j n ℂ) : Matrix n n ℂ :=
  R.conjTranspose * M * R

/-- A specified source form and inverse of its original relation Gram. -/
structure Metric (B : Matrix j m ℂ) where
  form : Matrix j j ℂ
  hermitian : form.conjTranspose = form
  relInv : Matrix m m ℂ
  inverse_right : (B.conjTranspose * form * B) * relInv = 1

namespace Metric
variable {B : Matrix j m ℂ}

def sectionMap (M : Metric B) (C : Matrix j n ℂ) : Matrix j n ℂ :=
  WeightedQuotientVolume.residual M.form C B M.relInv

def correction (M : Metric B) (C : Matrix j n ℂ) : Matrix m n ℂ :=
  M.relInv * (B.conjTranspose * M.form * C)

def quotientGram (M : Metric B) (C : Matrix j n ℂ) : Matrix n n ℂ :=
  gram M.form (M.sectionMap C)

theorem section_formula (M : Metric B) (C : Matrix j n ℂ) :
    M.sectionMap C = C - B * M.correction C := rfl

theorem orthogonal (M : Metric B) (C : Matrix j n ℂ) :
    B.conjTranspose * M.form * M.sectionMap C = 0 :=
  WeightedQuotientVolume.residual_orthogonal _ _ _ _ M.inverse_right

/-- Both sections have the same actual polynomial observation. -/
theorem section_observation {d : Type*} (J : Matrix d j ℂ)
    (M : Metric B) (C : Matrix j n ℂ) (hJ : J * B = 0) :
    J * M.sectionMap C = J * C :=
  WeightedQuotientVolume.residual_observation _ _ _ _ _ hJ

/-- The primitive in the original relation columns is fully specified. -/
theorem section_difference (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    M₁.sectionMap C - M₀.sectionMap C =
      B * (M₀.correction C - M₁.correction C) := by
  simp only [section_formula, Matrix.mul_sub]
  abel

/-- Polarization before taking a quotient; the conjugate cross term is retained. -/
theorem gram_add_boundary (M : Metric B) (C : Matrix j n ℂ)
    (Z : Matrix m n ℂ) :
    gram M.form (M.sectionMap C + B * Z) =
      M.quotientGram C + gram M.form (B * Z) := by
  have hL := M.orthogonal C
  have hR : (M.sectionMap C).conjTranspose * M.form * B = 0 := by
    have h := congrArg Matrix.conjTranspose hL
    simpa only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
      M.hermitian, Matrix.conjTranspose_zero, Matrix.mul_assoc] using h
  simp only [gram, quotientGram, Matrix.conjTranspose_add, Matrix.conjTranspose_mul,
    Matrix.add_mul, Matrix.mul_add, Matrix.mul_assoc]
  simp only [← Matrix.mul_assoc, hR, Matrix.zero_mul, zero_add]
  simp only [Matrix.mul_assoc, hL, Matrix.mul_zero, add_zero]

/-- Finite Pythagoras in one metric for the other metric's canonical section. -/
theorem pythagoras (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    gram M₀.form (M₁.sectionMap C) = M₀.quotientGram C +
      gram M₀.form (M₁.sectionMap C - M₀.sectionMap C) := by
  have h := M₀.gram_add_boundary C (M₀.correction C - M₁.correction C)
  rw [← section_difference M₀ M₁ C, add_sub_cancel] at h
  exact h

/-- Upper secant: the exact nonnegative loss is an original boundary Gram. -/
theorem secant_upper_identity (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    M₁.quotientGram C - M₀.quotientGram C =
      gram (M₁.form - M₀.form) (M₀.sectionMap C) -
        gram M₁.form (M₁.sectionMap C - M₀.sectionMap C) := by
  have h := pythagoras M₁ M₀ C
  have hneg : gram M₁.form (M₀.sectionMap C - M₁.sectionMap C) =
      gram M₁.form (M₁.sectionMap C - M₀.sectionMap C) := by
    rw [← neg_sub (M₁.sectionMap C) (M₀.sectionMap C)]
    simp only [gram, Matrix.conjTranspose_neg, Matrix.neg_mul, Matrix.mul_neg, neg_neg]
  rw [hneg] at h
  have hg : gram (M₁.form - M₀.form) (M₀.sectionMap C) =
      gram M₁.form (M₀.sectionMap C) - M₀.quotientGram C := by
    simp only [gram, quotientGram, Matrix.mul_sub, Matrix.sub_mul]
  rw [hg, h]
  abel

/-- Lower secant, with the other source metric on the boundary Gram. -/
theorem secant_lower_identity (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    M₁.quotientGram C - M₀.quotientGram C =
      gram (M₁.form - M₀.form) (M₁.sectionMap C) +
        gram M₀.form (M₁.sectionMap C - M₀.sectionMap C) := by
  have h := pythagoras M₀ M₁ C
  simp only [gram, quotientGram, Matrix.mul_sub, Matrix.sub_mul] at h ⊢
  rw [h]
  abel

/-- The remainder in the upper tangent bound is positive semidefinite. -/
theorem upper_remainder_posSemidef [Fintype n] (M₀ M₁ : Metric B) (C : Matrix j n ℂ)
    (hM₁ : M₁.form.PosSemidef) :
    (gram (M₁.form - M₀.form) (M₀.sectionMap C) -
      (M₁.quotientGram C - M₀.quotientGram C)).PosSemidef := by
  rw [secant_upper_identity]
  have he : gram (M₁.form - M₀.form) (M₀.sectionMap C) -
      (gram (M₁.form - M₀.form) (M₀.sectionMap C) -
        gram M₁.form (M₁.sectionMap C - M₀.sectionMap C)) =
      gram M₁.form (M₁.sectionMap C - M₀.sectionMap C) := by abel
  rw [he]
  exact hM₁.conjTranspose_mul_mul_same _

/-- Lower tangent remainder; no Loewner ordering of the two source forms is assumed. -/
theorem lower_remainder_posSemidef [Fintype n] (M₀ M₁ : Metric B) (C : Matrix j n ℂ)
    (hM₀ : M₀.form.PosSemidef) :
    ((M₁.quotientGram C - M₀.quotientGram C) -
      gram (M₁.form - M₀.form) (M₁.sectionMap C)).PosSemidef := by
  rw [secant_lower_identity, add_sub_cancel_left]
  exact hM₀.conjTranspose_mul_mul_same _

/-- Exact concavity defect for a source-metric pencil on the same quotient. -/
theorem pencil_gap (M₀ M₁ Mt : Metric B) (C : Matrix j n ℂ) (a b : ℝ)
    (ht : Mt.form = a • M₀.form + b • M₁.form) :
    Mt.quotientGram C - (a • M₀.quotientGram C + b • M₁.quotientGram C) =
      a • gram M₀.form (Mt.sectionMap C - M₀.sectionMap C) +
      b • gram M₁.form (Mt.sectionMap C - M₁.sectionMap C) := by
  have hg : Mt.quotientGram C = a • gram M₀.form (Mt.sectionMap C) +
      b • gram M₁.form (Mt.sectionMap C) := by
    simp only [quotientGram, gram, ht, Matrix.mul_add, Matrix.add_mul,
      Matrix.mul_smul, Matrix.smul_mul]
  rw [hg, pythagoras M₀ Mt C, pythagoras M₁ Mt C]
  simp only [smul_add]
  abel

theorem pencil_concavity [Fintype n] (M₀ M₁ Mt : Metric B) (C : Matrix j n ℂ) (a b : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hM₀ : M₀.form.PosSemidef) (hM₁ : M₁.form.PosSemidef)
    (ht : Mt.form = a • M₀.form + b • M₁.form) :
    (Mt.quotientGram C - (a • M₀.quotientGram C + b • M₁.quotientGram C)).PosSemidef := by
  rw [pencil_gap M₀ M₁ Mt C a b ht]
  exact ((hM₀.conjTranspose_mul_mul_same _).smul ha).add
    ((hM₁.conjTranspose_mul_mul_same _).smul hb)

end Metric
end SplitZero.MetricVariation
