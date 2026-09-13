import SplitZeroMetricVariation

/-!
# Exact finite perturbation through the original relation Gram

The two Metric structures and their canonical sections are the inherited
ones. B and C stay fixed. The resolvent is computed in the relation space;
its quotient loss is retained, rather than replaced by a chosen metric.
These are finite identities, not a claim that analytic derivatives have
been formalized. The pencil derivative formulas follow separately.
-/
noncomputable section
namespace SplitZero.MetricResolvent
open Matrix
open MetricVariation
open scoped ComplexOrder
variable {j n m : Type*} [Fintype j] [Fintype m] [DecidableEq m]
variable {B : Matrix j m ℂ}

/-- The original boundary/quotient cross block of the source perturbation. -/
def cross (M₀ M₁ : Metric B) (C : Matrix j n ℂ) : Matrix m n ℂ :=
  B.conjTranspose * (M₁.form - M₀.form) * M₀.sectionMap C

/-- The complete old-relation coefficient of the section correction. -/
def primitive (M₀ M₁ : Metric B) (C : Matrix j n ℂ) : Matrix m n ℂ :=
  M₁.relInv * cross M₀ M₁ C

theorem inverse_left (M : Metric B) :
    M.relInv * (B.conjTranspose * M.form * B) = 1 :=
  Matrix.mul_eq_one_comm.mp M.inverse_right

theorem inverse_hermitian (M : Metric B) : M.relInv.conjTranspose = M.relInv := by
  have hQ : (B.conjTranspose * M.form * B).conjTranspose =
      B.conjTranspose * M.form * B := by
    simp only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
      M.hermitian, Matrix.mul_assoc]
  have h := congrArg Matrix.conjTranspose M.inverse_right
  rw [Matrix.conjTranspose_mul, hQ, Matrix.conjTranspose_one] at h
  calc
    M.relInv.conjTranspose =
        (M.relInv.conjTranspose * (B.conjTranspose * M.form * B)) * M.relInv := by
      rw [Matrix.mul_assoc, M.inverse_right, Matrix.mul_one]
    _ = M.relInv := by rw [h, Matrix.one_mul]

theorem cross_normal (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    cross M₀ M₁ C = B.conjTranspose * M₁.form * M₀.sectionMap C := by
  simp only [cross, Matrix.mul_sub, Matrix.sub_mul, M₀.orthogonal C, sub_zero]

/-- The resolvent primitive is derived, not presumed to equal a section difference. -/
theorem primitive_eq_correction (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    primitive M₀ M₁ C = M₁.correction C - M₀.correction C := by
  unfold primitive
  rw [cross_normal, M₀.section_formula]
  calc
    _ = M₁.relInv * (B.conjTranspose * M₁.form * C) -
        (M₁.relInv * (B.conjTranspose * M₁.form * B)) * M₀.correction C := by
      simp only [Matrix.mul_sub, Matrix.mul_assoc]
    _ = M₁.correction C - M₀.correction C := by
      rw [inverse_left, Matrix.one_mul]
      rfl

/-- Exact resolvent for the original canonical representatives. -/
theorem section_update (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    M₁.sectionMap C = M₀.sectionMap C - B * primitive M₀ M₁ C := by
  rw [primitive_eq_correction]
  simp only [Metric.section_formula, Matrix.mul_sub]
  abel

theorem section_difference (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    M₁.sectionMap C - M₀.sectionMap C = -(B * primitive M₀ M₁ C) := by
  rw [section_update]
  abel

/-- Solve the actual perturbed normal equation on the relation columns. -/
theorem primitive_normal (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    B.conjTranspose * M₁.form * (B * primitive M₀ M₁ C) = cross M₀ M₁ C := by
  unfold primitive
  calc
    _ = ((B.conjTranspose * M₁.form * B) * M₁.relInv) * cross M₀ M₁ C := by
      simp only [Matrix.mul_assoc]
    _ = _ := by rw [M₁.inverse_right, Matrix.one_mul]

/-- The loss has a quotient-sized cross-block expression and a source-boundary Gram. -/
theorem boundary_loss (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    gram M₁.form (B * primitive M₀ M₁ C) =
      (cross M₀ M₁ C).conjTranspose * M₁.relInv * cross M₀ M₁ C := by
  unfold gram
  rw [Matrix.conjTranspose_mul]
  calc
    _ = (primitive M₀ M₁ C).conjTranspose *
        (B.conjTranspose * M₁.form * (B * primitive M₀ M₁ C)) := by
      simp only [Matrix.mul_assoc]
    _ = (primitive M₀ M₁ C).conjTranspose * cross M₀ M₁ C := by
      rw [primitive_normal]
    _ = _ := by
      simp only [primitive, Matrix.conjTranspose_mul, inverse_hermitian]

/-- Exact nonlinear quotient perturbation: no missing old-boundary loss. -/
theorem quotient_resolvent (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    M₁.quotientGram C = M₀.quotientGram C +
      gram (M₁.form - M₀.form) (M₀.sectionMap C) -
      (cross M₀ M₁ C).conjTranspose * M₁.relInv * cross M₀ M₁ C := by
  have h := M₀.secant_upper_identity M₁ C
  rw [section_difference] at h
  simp only [gram, Matrix.conjTranspose_neg, Matrix.neg_mul, Matrix.mul_neg,
    neg_neg] at h
  have hb := boundary_loss M₀ M₁ C
  unfold gram at hb
  rw [hb] at h
  unfold gram
  abel_nf at h ⊢
  exact h

theorem loss_posSemidef [Fintype n] (M₀ M₁ : Metric B) (C : Matrix j n ℂ)
    (hM : M₁.form.PosSemidef) :
    ((cross M₀ M₁ C).conjTranspose * M₁.relInv * cross M₀ M₁ C).PosSemidef := by
  rw [← boundary_loss]
  exact hM.conjTranspose_mul_mul_same _

/-- The perturbation makes no change exactly when its cross block vanishes.
The reverse implication uses the actual inverse relation Gram, not numerical tolerance. -/
theorem section_unchanged_iff (M₀ M₁ : Metric B) (C : Matrix j n ℂ) :
    M₁.sectionMap C = M₀.sectionMap C ↔ cross M₀ M₁ C = 0 := by
  constructor
  · intro h
    rw [cross_normal, ← h, M₁.orthogonal C]
  · intro h
    rw [section_update]
    simp only [primitive, h, Matrix.mul_zero, sub_zero]

end SplitZero.MetricResolvent
