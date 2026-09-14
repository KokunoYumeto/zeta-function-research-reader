import SplitZeroSourceProjectorContrast
import Mathlib.Analysis.Matrix.Order
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic

/-!
# Centered signed trace enclosures in a specified positive source metric

The proof constructs a metric isometry, applies Hilbert--Schmidt
Cauchy--Schwarz, and transports every product trace back. Centering removes
only the scalar direction annihilated by the actual traceless contrast.
-/
noncomputable section
namespace SplitZero.SignedTraceEnclosure
open Matrix
open scoped BigOperators ComplexOrder
variable {j : Type*} [Fintype j] [DecidableEq j]

def realTrace (A : Matrix j j ℂ) : ℝ := (Matrix.trace A).re

/-- An isometry out of the original form, with its inverse retained. -/
structure MetricFrame (M : Matrix j j ℂ) where
  forward : Matrix j j ℂ
  inverse : Matrix j j ℂ
  forward_inverse : forward * inverse = 1
  inverse_forward : inverse * forward = 1
  gram : forward.conjTranspose * forward = M

namespace MetricFrame
variable {M : Matrix j j ℂ} (F : MetricFrame M)

def conjugate (A : Matrix j j ℂ) : Matrix j j ℂ := F.forward * A * F.inverse

theorem conjugate_mul (A B : Matrix j j ℂ) :
    F.conjugate (A * B) = F.conjugate A * F.conjugate B := by
  simp only [conjugate, Matrix.mul_assoc, ← Matrix.mul_assoc F.inverse F.forward,
    F.inverse_forward, Matrix.one_mul]

theorem trace_conjugate (A : Matrix j j ℂ) :
    Matrix.trace (F.conjugate A) = Matrix.trace A := by
  unfold conjugate
  rw [Matrix.trace_mul_comm (F.forward * A) F.inverse]
  simp only [← Matrix.mul_assoc, F.inverse_forward, Matrix.one_mul]

theorem hermitian_conjugate (A : Matrix j j ℂ)
    (hA : A.conjTranspose * M = M * A) :
    (F.conjugate A).conjTranspose = F.conjugate A := by
  have hs : F.inverse.conjTranspose * F.forward.conjTranspose = 1 := by
    rw [← Matrix.conjTranspose_mul, F.forward_inverse, Matrix.conjTranspose_one]
  calc
    _ = F.inverse.conjTranspose * (A.conjTranspose * M) * F.inverse := by
      rw [← F.gram]
      simp only [conjugate, Matrix.conjTranspose_mul, Matrix.mul_assoc,
        F.forward_inverse, Matrix.mul_one]
    _ = F.inverse.conjTranspose * (M * A) * F.inverse := by rw [hA]
    _ = F.conjugate A := by
      rw [← F.gram]
      simp only [conjugate, ← Matrix.mul_assoc, hs, Matrix.one_mul]

/-- Positive definiteness supplies the frame; it is not an extra metric choice. -/
def ofPosDef (M : Matrix j j ℂ) (hM : M.PosDef) : MetricFrame M := by
  obtain ⟨W, hW, he⟩ :=
    CStarAlgebra.isStrictlyPositive_iff_eq_star_mul_self.mp hM.isStrictlyPositive
  obtain ⟨u, rfl⟩ := hW
  refine ⟨(u : Matrix j j ℂ), (↑(u⁻¹) : Matrix j j ℂ), by simp, by simp, ?_⟩
  simpa only [star_eq_conjTranspose] using he.symm
end MetricFrame

/-- Hilbert--Schmidt positivity, proved without dropping matrix entries. -/
theorem hermitian_square_nonneg (A : Matrix j j ℂ)
    (hA : A.conjTranspose = A) : 0 ≤ realTrace (A * A) := by
  have hp := (Matrix.posSemidef_conjTranspose_mul_self A).trace_nonneg
  have hr := (RCLike.nonneg_iff.mp hp).1
  simpa only [realTrace, hA] using hr

/-- The full Hermitian trace Schwarz inequality, including off-diagonal terms. -/
theorem hermitian_schwarz_sq (A B : Matrix j j ℂ)
    (hA : A.conjTranspose = A) (hB : B.conjTranspose = B) :
    (realTrace (A * B)) ^ 2 ≤ realTrace (A * A) * realTrace (B * B) := by
  letI : SeminormedAddCommGroup (Matrix j j ℂ) :=
    Matrix.toMatrixSeminormedAddCommGroup 1 Matrix.posSemidef_one
  letI : InnerProductSpace ℂ (Matrix j j ℂ) :=
    Matrix.toMatrixInnerProductSpace 1 Matrix.posSemidef_one
  have ha : ‖A‖ ^ 2 = realTrace (A * A) := by
    rw [norm_sq_eq_re_inner]
    change (Matrix.trace (A * 1 * A.conjTranspose)).re = _
    rw [Matrix.mul_one, hA]
    rfl
  have hb : ‖B‖ ^ 2 = realTrace (B * B) := by
    rw [norm_sq_eq_re_inner]
    change (Matrix.trace (B * 1 * B.conjTranspose)).re = _
    rw [Matrix.mul_one, hB]
    rfl
  have hc := norm_inner_le_norm A B
  change ‖Matrix.trace (B * 1 * A.conjTranspose)‖ ≤ ‖A‖ * ‖B‖ at hc
  rw [Matrix.mul_one, hA, Matrix.trace_mul_comm B A] at hc
  have hd : |realTrace (A * B)| ≤ ‖A‖ * ‖B‖ :=
    (Complex.abs_re_le_norm _).trans hc
  have hsq := (sq_le_sq₀ (abs_nonneg (realTrace (A * B)))
    (mul_nonneg (norm_nonneg A) (norm_nonneg B))).mpr hd
  simpa only [sq_abs, mul_pow, ha, hb] using hsq

/-- Both factors are self-adjoint for the SAME original positive form. -/
theorem weighted_schwarz (M A B : Matrix j j ℂ) (hM : M.PosDef)
    (hA : A.conjTranspose * M = M * A) (hB : B.conjTranspose * M = M * B) :
    |realTrace (A * B)| ≤ Real.sqrt (realTrace (A * A) * realTrace (B * B)) := by
  let F := MetricFrame.ofPosDef M hM
  have ha := F.hermitian_conjugate A hA
  have hb := F.hermitian_conjugate B hB
  have tr (U V : Matrix j j ℂ) :
      realTrace (F.conjugate U * F.conjugate V) = realTrace (U * V) := by
    rw [← F.conjugate_mul]
    exact congrArg Complex.re (F.trace_conjugate (U * V))
  have ha0 : 0 ≤ realTrace (A * A) := by
    simpa only [tr] using hermitian_square_nonneg _ ha
  have hb0 : 0 ≤ realTrace (B * B) := by
    simpa only [tr] using hermitian_square_nonneg _ hb
  have hs : (realTrace (A * B)) ^ 2 ≤ realTrace (A * A) * realTrace (B * B) := by
    simpa only [tr] using hermitian_schwarz_sq _ _ ha hb
  apply (sq_le_sq₀ (abs_nonneg _) (Real.sqrt_nonneg _)).mp
  rw [sq_abs, Real.sq_sqrt (mul_nonneg ha0 hb0)]
  exact hs

/-- Centering uses the real trace divided by the actual source dimension. -/
def center (A : Matrix j j ℂ) : Matrix j j ℂ :=
  A - (realTrace A / (Fintype.card j : ℝ)) • (1 : Matrix j j ℂ)

theorem centered_pairing (A B : Matrix j j ℂ) (hB : Matrix.trace B = 0) :
    realTrace (center A * B) = realTrace (A * B) := by
  unfold center realTrace
  simp only [Matrix.sub_mul, Matrix.smul_mul, Matrix.one_mul,
    Matrix.trace_sub, Matrix.trace_smul, hB, smul_zero, sub_zero]

theorem weighted_center (M A : Matrix j j ℂ)
    (hA : A.conjTranspose * M = M * A) :
    (center A).conjTranspose * M = M * center A := by
  simp [center, Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul, hA]

/-- The exact two-sided interval has its original signed center. -/
theorem signed_interval (M X Y Q : Matrix j j ℂ) (hM : M.PosDef)
    (hX : X.conjTranspose * M = M * X) (hY : Y.conjTranspose * M = M * Y)
    (hQ : Q.conjTranspose * M = M * Q) (htQ : Matrix.trace Q = 0) :
    let E := center (X - Y)
    let e := Real.sqrt (realTrace (E * E) * realTrace (Q * Q))
    realTrace (Y * Q) - e ≤ realTrace (X * Q) ∧
      realTrace (X * Q) ≤ realTrace (Y * Q) + e := by
  dsimp only
  have hsub : (X - Y).conjTranspose * M = M * (X - Y) := by
    simp only [Matrix.conjTranspose_sub, Matrix.sub_mul, Matrix.mul_sub, hX, hY]
  have hs := weighted_schwarz M (center (X - Y)) Q hM (weighted_center M _ hsub) hQ
  rw [centered_pairing _ _ htQ] at hs
  have he : realTrace ((X - Y) * Q) = realTrace (X * Q) - realTrace (Y * Q) := by
    simp only [realTrace, Matrix.sub_mul, Matrix.trace_sub, Complex.sub_re]
  rw [he] at hs
  exact ⟨by linarith [(abs_le.mp hs).1], by linarith [(abs_le.mp hs).2]⟩
end SplitZero.SignedTraceEnclosure
