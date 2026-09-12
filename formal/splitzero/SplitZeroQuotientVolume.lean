import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.ConjTranspose
import Mathlib.Tactic

/-!
# Source Gram, original relation Gram, and the quotient volume

The original column C is corrected only by columns of B. The residual,
its orthogonality, its Gram, and the determinant factorization are all
constructed. The determinant formula is instantiated from Mathlib's
Schur complement theorem, not advertised as new matrix mathematics.
-/
noncomputable section
namespace SplitZero.QuotientVolume
open Matrix
variable {j n m : Type*} [Fintype j] [Fintype n] [Fintype m]
  [DecidableEq n] [DecidableEq m]

def residual (C : Matrix j n ℂ) (B : Matrix j m ℂ) (H : Matrix m m ℂ) :
    Matrix j n ℂ := C - B * (H * (B.conjTranspose * C))

def sourceGram (C : Matrix j n ℂ) (B : Matrix j m ℂ) :
    Matrix (n ⊕ m) (n ⊕ m) ℂ :=
  Matrix.fromBlocks (C.conjTranspose * C) (C.conjTranspose * B)
    (B.conjTranspose * C) (B.conjTranspose * B)

omit [DecidableEq n] in
theorem residual_orthogonal (C : Matrix j n ℂ) (B : Matrix j m ℂ)
    (H : Matrix m m ℂ) (hH : (B.conjTranspose * B) * H = 1) :
    B.conjTranspose * residual C B H = 0 := by
  calc
    _ = B.conjTranspose * C -
        ((B.conjTranspose * B) * H) * (B.conjTranspose * C) := by
      simp only [residual, Matrix.mul_sub, Matrix.mul_assoc]
    _ = 0 := by rw [hH, Matrix.one_mul, sub_self]

omit [DecidableEq n] in
/-- Complete residual Gram, retaining all cross terms in the Schur complement. -/
theorem residual_gram (C : Matrix j n ℂ) (B : Matrix j m ℂ)
    (H : Matrix m m ℂ) (hH : (B.conjTranspose * B) * H = 1) :
    (residual C B H).conjTranspose * residual C B H =
      C.conjTranspose * C - C.conjTranspose * B * H * (B.conjTranspose * C) := by
  have ho := residual_orthogonal C B H hH
  calc
    _ = (C.conjTranspose - (H * (B.conjTranspose * C)).conjTranspose *
          B.conjTranspose) * residual C B H := by
      congr 1
      simp only [residual, Matrix.conjTranspose_sub, Matrix.conjTranspose_mul]
    _ = C.conjTranspose * residual C B H := by
      rw [Matrix.sub_mul, Matrix.mul_assoc, ho, Matrix.mul_zero, sub_zero]
    _ = _ := by simp only [residual, Matrix.mul_sub, Matrix.mul_assoc]

/-- Source volume = relation volume times the constructed quotient volume. -/
theorem determinant_factor (C : Matrix j n ℂ) (B : Matrix j m ℂ)
    [Invertible (B.conjTranspose * B)] :
    (sourceGram C B).det =
      (B.conjTranspose * B).det *
        ((residual C B (⅟(B.conjTranspose * B))).conjTranspose *
          residual C B (⅟(B.conjTranspose * B))).det := by
  rw [sourceGram, Matrix.det_fromBlocks₂₂]
  rw [residual_gram C B _ (mul_invOf_self _)]

/-- The ratio uses the actual nonzero relation determinant. -/
theorem determinant_ratio (C : Matrix j n ℂ) (B : Matrix j m ℂ)
    [Invertible (B.conjTranspose * B)]
    (hdet : (B.conjTranspose * B).det ≠ 0) :
    ((residual C B (⅟(B.conjTranspose * B))).conjTranspose *
      residual C B (⅟(B.conjTranspose * B))).det =
      (sourceGram C B).det / (B.conjTranspose * B).det := by
  apply (eq_div_iff hdet).mpr
  simpa only [mul_comm] using (determinant_factor C B).symm

omit [DecidableEq n] [DecidableEq m] in
/-- Any observation killing precisely these supplied relation columns is unchanged. -/
theorem residual_observation {d : Type*} [Fintype d]
    (J : Matrix d j ℂ) (C : Matrix j n ℂ) (B : Matrix j m ℂ)
    (H : Matrix m m ℂ) (hJ : J * B = 0) :
    J * residual C B H = J * C := by
  simp only [residual, Matrix.mul_sub, ← Matrix.mul_assoc, hJ,
    Matrix.zero_mul, sub_zero]

end SplitZero.QuotientVolume
