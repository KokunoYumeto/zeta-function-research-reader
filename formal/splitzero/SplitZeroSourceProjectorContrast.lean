import SplitZeroMetricVariation
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# The four-endpoint contrast on the common ORIGINAL source

Projectors are constructed from specified columns and their inverse Grams.
Trace identities keep the two old-to-new restrictions and their mixed term.
No source-path differentiation or arithmetic integral is assumed proved here.
-/
noncomputable section
namespace SplitZero.SourceProjectorContrast
open Matrix
variable {j n : Type*} [Fintype j] [Fintype n]

/-- The weighted source projector calculated from the given representative. -/
def projector (M : Matrix j j ℂ) (R : Matrix j n ℂ) (K : Matrix n n ℂ) :
    Matrix j j ℂ := R * K * R.conjTranspose * M

/-- The actual inverse-Gram equation proves idempotence. -/
theorem projector_idempotent [DecidableEq n] (M : Matrix j j ℂ) (R : Matrix j n ℂ)
    (K : Matrix n n ℂ) (hK : (R.conjTranspose * M * R) * K = 1) :
    projector M R K * projector M R K = projector M R K := by
  calc
    _ = R * K * ((R.conjTranspose * M * R) * K) * R.conjTranspose * M := by
      simp only [projector, Matrix.mul_assoc]
    _ = _ := by rw [hK, Matrix.mul_one]; rfl

/-- Weighted, not unweighted, self-adjointness. -/
theorem projector_adjoint (M : Matrix j j ℂ) (R : Matrix j n ℂ)
    (K : Matrix n n ℂ) (hM : M.conjTranspose = M) (hK : K.conjTranspose = K) :
    (projector M R K).conjTranspose * M = M * projector M R K := by
  simp only [projector, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
    hM, hK, Matrix.mul_assoc]

/-- The rank contribution is the quotient dimension, with empty dimensions allowed. -/
theorem projector_trace [DecidableEq n] (M : Matrix j j ℂ) (R : Matrix j n ℂ)
    (K : Matrix n n ℂ) (hK : (R.conjTranspose * M * R) * K = 1) :
    Matrix.trace (projector M R K) = (Fintype.card n : ℂ) := by
  calc
    _ = Matrix.trace ((R * K) * (R.conjTranspose * M)) := by
      simp only [projector, Matrix.mul_assoc]
    _ = Matrix.trace ((R.conjTranspose * M) * (R * K)) := Matrix.trace_mul_comm _ _
    _ = Matrix.trace ((R.conjTranspose * M * R) * K) := by
      simp only [Matrix.mul_assoc]
    _ = _ := by rw [hK, Matrix.trace_one]

/-- Finite tangent pairing; the actual Gram derivative is a separate analytic input. -/
theorem trace_tangent_pairing [DecidableEq j]
    (M J E : Matrix j j ℂ) (R : Matrix j n ℂ) (K : Matrix n n ℂ)
    (hJ : M * J = 1) :
    Matrix.trace (K * (R.conjTranspose * E * R)) =
      Matrix.trace ((J * E) * projector M R K) := by
  symm
  calc
    _ = Matrix.trace ((J * E * R * K * R.conjTranspose) * M) := by
      simp only [projector, Matrix.mul_assoc]
    _ = Matrix.trace (M * (J * E * R * K * R.conjTranspose)) := Matrix.trace_mul_comm _ _
    _ = Matrix.trace (E * R * K * R.conjTranspose) := by
      simp only [← Matrix.mul_assoc, hJ, Matrix.one_mul]
    _ = Matrix.trace (R.conjTranspose * (E * R * K)) := Matrix.trace_mul_comm _ _
    _ = Matrix.trace ((R.conjTranspose * E * R) * K) := by
      simp only [Matrix.mul_assoc]
    _ = _ := Matrix.trace_mul_comm _ _

/-- Original nested-source cross Gram determines the two projector overlap trace. -/
theorem overlap_trace [DecidableEq n] (M : Matrix j j ℂ) (Rᵢ Rⱼ : Matrix j n ℂ)
    (Kᵢ Kⱼ Gⱼ : Matrix n n ℂ)
    (hM : M.conjTranspose = M) (hG : Gⱼ.conjTranspose = Gⱼ)
    (hcross : Rⱼ.conjTranspose * M * Rᵢ = Gⱼ) (hK : Gⱼ * Kⱼ = 1) :
    Matrix.trace (projector M Rᵢ Kᵢ * projector M Rⱼ Kⱼ) =
      Matrix.trace (Kᵢ * Gⱼ) := by
  have hc : Rᵢ.conjTranspose * M * Rⱼ = Gⱼ := by
    have hh := congrArg Matrix.conjTranspose hcross
    simpa only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
      hM, hG, Matrix.mul_assoc] using hh
  calc
    _ = Matrix.trace ((Rᵢ * Kᵢ) *
        (Rᵢ.conjTranspose * M * Rⱼ * Kⱼ * Rⱼ.conjTranspose * M)) := by
      simp only [projector, Matrix.mul_assoc]
    _ = Matrix.trace ((Rᵢ.conjTranspose * M * Rⱼ * Kⱼ * Rⱼ.conjTranspose * M) *
        (Rᵢ * Kᵢ)) := Matrix.trace_mul_comm _ _
    _ = Matrix.trace ((Rᵢ.conjTranspose * M * Rⱼ) * Kⱼ *
        (Rⱼ.conjTranspose * M * Rᵢ) * Kᵢ) := by
      simp only [Matrix.mul_assoc]
    _ = Matrix.trace (Gⱼ * Kᵢ) := by rw [hc, hcross, hK, Matrix.one_mul]
    _ = _ := Matrix.trace_mul_comm _ _

section Contrast

/-- The original signs, on one common source; no endpoint is estimated separately. -/
def contrast (P : Fin 4 → Matrix j j ℂ) : Matrix j j ℂ :=
  P 0 + P 1 - P 2 - P 3

/-- Cancellation uses equal TRACES, not an incorrect claim about shell ranks. -/
theorem contrast_trace (P : Fin 4 → Matrix j j ℂ) (d : ℂ)
    (h : ∀ a, Matrix.trace (P a) = d) : Matrix.trace (contrast P) = 0 := by
  simp only [contrast, Matrix.trace_sub, Matrix.trace_add, h]
  ring

/-- A common scalar source change cancels exactly before any estimate. -/
theorem centered_pairing [DecidableEq j] (X Q : Matrix j j ℂ) (c : ℂ)
    (hQ : Matrix.trace Q = 0) :
    Matrix.trace ((X - c • (1 : Matrix j j ℂ)) * Q) = Matrix.trace (X * Q) := by
  rw [Matrix.sub_mul, Matrix.smul_mul, Matrix.one_mul, Matrix.trace_sub,
    Matrix.trace_smul, hQ, smul_zero, sub_zero]

/-- The finite four-endpoint pairing, without a diagonal or commuting assumption. -/
theorem contrast_pairing (X : Matrix j j ℂ) (P : Fin 4 → Matrix j j ℂ) :
    Matrix.trace (X * contrast P) =
      Matrix.trace (X * P 0) + Matrix.trace (X * P 1) -
        Matrix.trace (X * P 2) - Matrix.trace (X * P 3) := by
  simp only [contrast, Matrix.mul_sub, Matrix.mul_add, Matrix.trace_sub, Matrix.trace_add]

/-- The squared difference of two weighted projections uses their actual overlap. -/
theorem pair_loss_trace [DecidableEq j] (P Q : Matrix j j ℂ) (d : ℂ)
    (hP : P * P = P) (hQ : Q * Q = Q)
    (htP : Matrix.trace P = d) (htQ : Matrix.trace Q = d) :
    Matrix.trace ((P - Q)^2) = 2 * (d - Matrix.trace (P * Q)) := by
  simp only [pow_two, Matrix.sub_mul, Matrix.mul_sub, hP, hQ, Matrix.trace_sub]
  rw [Matrix.trace_mul_comm Q P, htP, htQ]
  ring

/-- The two restriction losses have a mixed cross term; it is not omitted. -/
theorem contrast_square [DecidableEq j] (P : Fin 4 → Matrix j j ℂ) :
    Matrix.trace ((contrast P)^2) =
      Matrix.trace ((P 0 - P 2)^2) + Matrix.trace ((P 1 - P 3)^2) +
        2 * Matrix.trace ((P 0 - P 2) * (P 1 - P 3)) := by
  have h : contrast P = (P 0 - P 2) + (P 1 - P 3) := by unfold contrast; abel
  rw [h]
  simp only [pow_two, Matrix.add_mul, Matrix.mul_add, Matrix.trace_add]
  rw [Matrix.trace_mul_comm (P 1 - P 3) (P 0 - P 2)]
  ring

end Contrast
end SplitZero.SourceProjectorContrast
