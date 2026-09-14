import Mathlib

/-!
The reverse map is the metric adjoint of the original identity transport.
No commutation of the canonical metrics with the arithmetic action is assumed.
The matrices K and G supplied below are the original inverse kernel and Gram.
-/
noncomputable section
namespace SplitZero.Restriction
open Matrix
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

def returnMap (Ki Gj : Matrix ι ι ℂ) : Matrix ι ι ℂ := Ki * Gj

def control (A K G : Matrix ι ι ℂ) (w : ℂ) : Matrix ι ι ℂ :=
  K * A.conjTranspose * G + A - w • 1

/-- This is precisely the matrix equation for the two-metric adjoint. -/
theorem metric_adjoint (Gi Ki Gj : Matrix ι ι ℂ) (h : Gi * Ki = 1) :
    Gi * returnMap Ki Gj = Gj := by
  simp only [returnMap, ← Matrix.mul_assoc, h, Matrix.one_mul]

/-- Adjoint transport reverses the original composable arrows. -/
theorem return_comp (Ki Gj Kj Gl : Matrix ι ι ℂ) (h : Gj * Kj = 1) :
    returnMap Ki Gj * returnMap Kj Gl = returnMap Ki Gl := by
  unfold returnMap
  calc
    (Ki * Gj) * (Kj * Gl) = Ki * (Gj * Kj) * Gl := by noncomm_ring
    _ = Ki * Gl := by rw [h]; simp

/-- The reverse map is invertible, but it is not the identity map. -/
theorem return_inverse (Ki Gi Kj Gj : Matrix ι ι ℂ)
    (hi : Ki * Gi = 1) (hj : Gj * Kj = 1) :
    returnMap Ki Gj * returnMap Kj Gi = 1 := by
  rw [return_comp Ki Gj Kj Gi hj]
  exact hi

/-- Keep the action defect instead of declaring reverse transport equivariant. -/
theorem action_defect (A Ki Gi Kj Gj : Matrix ι ι ℂ) (w : ℂ)
    (hi : Gi * Ki = 1) (hj : Gj * Kj = 1) :
    A * returnMap Ki Gj - returnMap Ki Gj * A =
      control A Ki Gi w * returnMap Ki Gj -
        returnMap Ki Gj * control A Kj Gj w := by
  have hleft : (Ki * A.conjTranspose * Gi) * (Ki * Gj) =
      Ki * A.conjTranspose * Gj := by
    calc
      _ = (Ki * A.conjTranspose) * (Gi * Ki) * Gj := by noncomm_ring
      _ = _ := by rw [hi]; simp
  have hright : (Ki * Gj) * (Kj * A.conjTranspose * Gj) =
      Ki * A.conjTranspose * Gj := by
    calc
      _ = Ki * (Gj * Kj) * A.conjTranspose * Gj := by noncomm_ring
      _ = _ := by rw [hj]; simp
  unfold control returnMap
  simp only [Matrix.sub_mul, Matrix.add_mul, Matrix.mul_sub, Matrix.mul_add,
    Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one]
  rw [hleft, hright]
  abel

/-- The deficit has its noncommutative composition law. -/
theorem deficit_comp (Ki Gj Kj Gl : Matrix ι ι ℂ) (h : Gj * Kj = 1) :
    1 - returnMap Ki Gl = (1 - returnMap Ki Gj) +
      returnMap Ki Gj * (1 - returnMap Kj Gl) := by
  rw [← return_comp Ki Gj Kj Gl h]
  noncomm_ring

/-- Determinant loss on the two specified metrics, without a new normalization. -/
theorem determinant_transport (Gi Ki Gj : Matrix ι ι ℂ) (h : Gi * Ki = 1) :
    Gi.det * (returnMap Ki Gj).det = Gj.det := by
  rw [← Matrix.det_mul, metric_adjoint Gi Ki Gj h]

/-- Low-source energy Gram calculated from the actual reverse map. -/
theorem retained_gram (Ki Gi Gj : Matrix ι ι ℂ)
    (hi : Gi * Ki = 1) (hKi : Ki.conjTranspose = Ki)
    (hGj : Gj.conjTranspose = Gj) :
    (returnMap Ki Gj).conjTranspose * Gi * returnMap Ki Gj = Gj * Ki * Gj := by
  rw [Matrix.mul_assoc, metric_adjoint Gi Ki Gj hi]
  simp only [returnMap, Matrix.conjTranspose_mul, hKi, hGj]

end SplitZero.Restriction
