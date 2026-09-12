import SplitZeroQuotientVolume

/-!
# The quotient-volume calculation in the unchanged source moment matrix

The source metric M is retained in every composite. No orthonormal basis,
normalization of the measure, or replacement of the arithmetic Gram is used.
Only the relation Gram is inverted. Positivity and its analytic source are
separate inputs; the following identities hold already at matrix level.
-/
noncomputable section
namespace SplitZero.WeightedQuotientVolume
open Matrix
variable {j n m : Type*} [Fintype j] [Fintype m]

def residual (M : Matrix j j ℂ) (C : Matrix j n ℂ)
    (B : Matrix j m ℂ) (H : Matrix m m ℂ) : Matrix j n ℂ :=
  C - B * (H * (B.conjTranspose * M * C))

def sourceGram (M : Matrix j j ℂ) (C : Matrix j n ℂ) (B : Matrix j m ℂ) :
    Matrix (n ⊕ m) (n ⊕ m) ℂ :=
  Matrix.fromBlocks (C.conjTranspose * M * C) (C.conjTranspose * M * B)
    (B.conjTranspose * M * C) (B.conjTranspose * M * B)

theorem residual_orthogonal [DecidableEq m]
    (M : Matrix j j ℂ) (C : Matrix j n ℂ)
    (B : Matrix j m ℂ) (H : Matrix m m ℂ)
    (hH : (B.conjTranspose * M * B) * H = 1) :
    B.conjTranspose * M * residual M C B H = 0 := by
  calc
    _ = B.conjTranspose * M * C -
        ((B.conjTranspose * M * B) * H) * (B.conjTranspose * M * C) := by
      simp only [residual, Matrix.mul_sub, Matrix.mul_assoc]
    _ = 0 := by rw [hH, Matrix.one_mul, sub_self]

theorem residual_gram [DecidableEq m]
    (M : Matrix j j ℂ) (C : Matrix j n ℂ)
    (B : Matrix j m ℂ) (H : Matrix m m ℂ)
    (hH : (B.conjTranspose * M * B) * H = 1) :
    (residual M C B H).conjTranspose * M * residual M C B H =
      C.conjTranspose * M * C -
        C.conjTranspose * M * B * H * (B.conjTranspose * M * C) := by
  have ho := residual_orthogonal M C B H hH
  have hex : (residual M C B H).conjTranspose =
      C.conjTranspose - (H * (B.conjTranspose * M * C)).conjTranspose *
        B.conjTranspose := by
    simp only [residual, Matrix.conjTranspose_sub, Matrix.conjTranspose_mul]
  rw [hex]
  calc
    _ = C.conjTranspose * M * residual M C B H -
        (H * (B.conjTranspose * M * C)).conjTranspose *
          (B.conjTranspose * M * residual M C B H) := by
      simp only [Matrix.sub_mul, Matrix.mul_assoc]
    _ = C.conjTranspose * M * residual M C B H := by
      rw [ho, Matrix.mul_zero, sub_zero]
    _ = _ := by simp only [residual, Matrix.mul_sub, Matrix.mul_assoc]

theorem determinant_factor [Fintype n] [DecidableEq n] [DecidableEq m]
    (M : Matrix j j ℂ) (C : Matrix j n ℂ) (B : Matrix j m ℂ)
    [Invertible (B.conjTranspose * M * B)] :
    (sourceGram M C B).det =
      (B.conjTranspose * M * B).det *
        ((residual M C B (⅟(B.conjTranspose * M * B))).conjTranspose * M *
          residual M C B (⅟(B.conjTranspose * M * B))).det := by
  rw [sourceGram, Matrix.det_fromBlocks₂₂]
  rw [residual_gram M C B _ (mul_invOf_self _)]

theorem determinant_ratio [Fintype n] [DecidableEq n] [DecidableEq m]
    (M : Matrix j j ℂ) (C : Matrix j n ℂ) (B : Matrix j m ℂ)
    [Invertible (B.conjTranspose * M * B)]
    (hdet : (B.conjTranspose * M * B).det ≠ 0) :
    ((residual M C B (⅟(B.conjTranspose * M * B))).conjTranspose * M *
      residual M C B (⅟(B.conjTranspose * M * B))).det =
      (sourceGram M C B).det / (B.conjTranspose * M * B).det := by
  apply (eq_div_iff hdet).mpr
  simpa only [mul_comm] using (determinant_factor M C B).symm

theorem residual_observation {d : Type*}
    (J : Matrix d j ℂ) (M : Matrix j j ℂ) (C : Matrix j n ℂ)
    (B : Matrix j m ℂ) (H : Matrix m m ℂ) (hJ : J * B = 0) :
    J * residual M C B H = J * C := by
  simp only [residual, Matrix.mul_sub, ← Matrix.mul_assoc, hJ,
    Matrix.zero_mul, sub_zero]

end SplitZero.WeightedQuotientVolume
