import SplitZeroRestrictionSource

/-!
The affine relation curve in the original weighted polynomial source.
No metric, arithmetic observation, or complementary relation is replaced.
The complex scalar `star z * z` is the literal squared modulus.
-/
noncomputable section
namespace SplitZero.RelationCurve
open Matrix
variable {ι σ : Type*}

def curve (R D : Matrix σ ι ℂ) (z : ℂ) : Matrix σ ι ℂ := R + z • D

@[simp] theorem at_zero (R D : Matrix σ ι ℂ) : curve R D 0 = R := by simp [curve]
@[simp] theorem at_one (X R : Matrix σ ι ℂ) : curve R (X-R) 1 = X := by simp [curve]

section Source
variable [Fintype σ]

theorem opposite_cross (R D : Matrix σ ι ℂ) (O : Matrix σ σ ℂ)
    (hO : O.conjTranspose = O) (h : R.conjTranspose * O * D = 0) :
    D.conjTranspose * O * R = 0 := by
  have hh := congrArg Matrix.conjTranspose h
  simpa only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
    Matrix.conjTranspose_zero, hO, Matrix.mul_assoc] using hh

theorem gram (R D : Matrix σ ι ℂ) (O : Matrix σ σ ℂ)
    (G C : Matrix ι ι ℂ) (hO : O.conjTranspose = O)
    (hR : R.conjTranspose * O * R = G)
    (hD : D.conjTranspose * O * D = C)
    (hcross : R.conjTranspose * O * D = 0) (z : ℂ) :
    (curve R D z).conjTranspose * O * curve R D z =
      G + (star z * z) • C := by
  have hop := opposite_cross R D O hO hcross
  simp [curve, Matrix.conjTranspose_add, Matrix.conjTranspose_smul,
    Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.mul_smul,
    smul_smul, hR, hD, hcross, hop, mul_comm]

variable [DecidableEq ι]

theorem observation (B : Matrix ι σ ℂ) (R D : Matrix σ ι ℂ)
    (hR : B * R = 1) (hD : B * D = 0) (z : ℂ) :
    B * curve R D z = 1 := by
  simp [curve, Matrix.mul_add, Matrix.mul_smul, hR, hD]

variable [Fintype ι]

/-- Orthogonality of the actual difference follows from the later dual equation. -/
theorem difference_cross (B : Matrix ι σ ℂ) (X R : Matrix σ ι ℂ)
    (O : Matrix σ σ ℂ) (G : Matrix ι ι ℂ)
    (hX : B * X = 1) (hR : B * R = 1)
    (hdual : R.conjTranspose * O = G * B) :
    R.conjTranspose * O * (X - R) = 0 := by
  rw [hdual, Matrix.mul_assoc, Matrix.mul_sub, hX, hR, sub_self, Matrix.mul_zero]

/-- Direct composition with the previously verified relation-Gram theorem. -/
theorem canonical_gram (B : Matrix ι σ ℂ) (X R : Matrix σ ι ℂ)
    (O : Matrix σ σ ℂ) (Gi Gj : Matrix ι ι ℂ)
    (hO : O.conjTranspose = O) (hGj : Gj.conjTranspose = Gj)
    (hX : B * X = 1) (hR : B * R = 1)
    (hGram : X.conjTranspose * O * X = Gi)
    (hDual : R.conjTranspose * O = Gj * B) (z : ℂ) :
    (curve R (X-R) z).conjTranspose * O * curve R (X-R) z =
      Gj + (star z * z) • (Gi-Gj) := by
  have hg : R.conjTranspose * O * R = Gj := by
    rw [hDual, Matrix.mul_assoc, hR, Matrix.mul_one]
  exact gram R (X-R) O Gj (Gi-Gj) hO hg
    (SplitZero.Restriction.relation_gram B O X R Gi Gj hO hGj hX hR hGram hDual)
    (difference_cross B X R O Gj hX hR hDual) z
end Source

section Coordinate
variable [Fintype ι]

/-- Restricting to a specified constituent keeps the actual source inclusion. -/
theorem constituent {κ : Type*} (R D : Matrix σ ι ℂ)
    (J : Matrix ι κ ℂ) (z : ℂ) :
    curve R D z * J = curve (R*J) (D*J) z := by
  simp [curve, Matrix.add_mul, Matrix.smul_mul]

/-- The original action defect is affine in the actual metric increment. -/
theorem control (A Gi Gj : Matrix ι ι ℂ) (weight : ℂ) (t : ℂ) :
    A.conjTranspose * (Gj + t • (Gi-Gj)) +
      (Gj + t • (Gi-Gj)) * A - weight • (Gj + t • (Gi-Gj)) =
    (A.conjTranspose * Gj + Gj * A - weight • Gj) +
      t • ((A.conjTranspose * Gi + Gi * A - weight • Gi) -
        (A.conjTranspose * Gj + Gj * A - weight • Gj)) := by
  simp only [Matrix.mul_add, Matrix.add_mul, Matrix.mul_sub, Matrix.sub_mul,
    Matrix.mul_smul, Matrix.smul_mul, smul_add, smul_sub, smul_smul]
  module
end Coordinate
end SplitZero.RelationCurve
