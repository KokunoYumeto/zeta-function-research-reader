import Mathlib

/-!
# Full-jet and invariant-coordinate matrix identities

All coordinate maps are explicit. In particular inverse compression requires
an invariant summand and is not asserted for an arbitrary rectangular matrix.
-/
noncomputable section
namespace SplitZero.MetricRestriction
open Matrix
variable {n d : Type*} [Fintype n] [DecidableEq n] [Fintype d] [DecidableEq d]

def primal (A G : Matrix n n ℂ) (w : ℝ) : Matrix n n ℂ :=
  A.conjTranspose * G + G * A - (w : ℂ) • G

def kernel (A K : Matrix n n ℂ) (w : ℝ) : Matrix n n ℂ :=
  A * K + K * A.conjTranspose - (w : ℂ) • K

/-- The exact primal-to-antidual congruence, retaining the weight. -/
theorem kernel_congruence (A G K : Matrix n n ℂ) (w : ℝ)
    (hGK : G * K = 1) (hKG : K * G = 1) :
    K * primal A G w * K = kernel A K w := by
  calc
    K * primal A G w * K =
        (K * A.conjTranspose) * (G * K) + (K * G) * (A * K) -
          (w : ℂ) • ((K * G) * K) := by
      simp only [primal, mul_add, add_mul, mul_sub, sub_mul,
        mul_smul_comm, smul_mul_assoc]
      noncomm_ring
    _ = kernel A K w := by simp [hGK, hKG, kernel, add_comm]

/-- Defect compression under an intertwining inclusion. -/
theorem primal_compression (A G : Matrix n n ℂ) (As : Matrix d d ℂ)
    (I : Matrix n d ℂ) (w : ℝ) (hAI : A * I = I * As) :
    I.conjTranspose * primal A G w * I =
      primal As (I.conjTranspose * G * I) w := by
  have hstar := congrArg Matrix.conjTranspose hAI
  simp only [Matrix.conjTranspose_mul] at hstar
  calc
    I.conjTranspose * primal A G w * I =
        (I.conjTranspose * A.conjTranspose) * (G * I) +
        (I.conjTranspose * G) * (A * I) -
        (w : ℂ) • (I.conjTranspose * G * I) := by
      simp only [primal, Matrix.mul_add, Matrix.add_mul, Matrix.mul_sub,
        Matrix.sub_mul, Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_assoc]
    _ = primal As (I.conjTranspose * G * I) w := by
      rw [hstar, hAI]
      simp only [primal, Matrix.mul_assoc]

/-- Orbit sums use I for inclusion and L for coefficient extraction.
The self-adjoint orbit projection is I L, not generally I I*. -/
theorem inverse_compression (G K : Matrix n n ℂ)
    (I : Matrix n d ℂ) (L : Matrix d n ℂ)
    (hLI : L * I = 1) (hP : (I * L).conjTranspose = I * L)
    (hKP : (I * L) * K = K * (I * L)) (hGK : G * K = 1) :
    (I.conjTranspose * G * I) * (L * K * L.conjTranspose) = 1 := by
  have hPI : (I * L) * I = I := by rw [Matrix.mul_assoc, hLI, Matrix.mul_one]
  have hIP : I.conjTranspose * (I * L) = I.conjTranspose := by
    have h := congrArg Matrix.conjTranspose hPI
    rw [Matrix.conjTranspose_mul, hP] at h
    exact h
  calc
    (I.conjTranspose * G * I) * (L * K * L.conjTranspose) =
        I.conjTranspose * G * ((I * L) * K) * L.conjTranspose := by
      simp only [Matrix.mul_assoc]
    _ = I.conjTranspose * G * (K * (I * L)) * L.conjTranspose := by rw [hKP]
    _ = I.conjTranspose * (G * K) * (I * L) * L.conjTranspose := by
      simp only [Matrix.mul_assoc]
    _ = I.conjTranspose * L.conjTranspose := by rw [hGK, Matrix.mul_one, hIP]
    _ = (L * I).conjTranspose := (Matrix.conjTranspose_mul L I).symm
    _ = 1 := by rw [hLI, Matrix.conjTranspose_one]

/-- The complementary trace is kept at the same ambient operator. -/
theorem complementary_trace (P A : Matrix n n ℂ) :
    Matrix.trace (P * A) + Matrix.trace ((1 - P) * A) = Matrix.trace A := by
  rw [← Matrix.trace_add]
  congr 1
  noncomm_ring

/-- Explicit matrix-inverse witnesses for a change of coordinates. -/
theorem coordinate_inverse (G K T U : Matrix n n ℂ)
    (hTU : T * U = 1) (hGK : G * K = 1) :
    (T.conjTranspose * G * T) * (U * K * U.conjTranspose) = 1 := by
  calc
    (T.conjTranspose * G * T) * (U * K * U.conjTranspose) =
        T.conjTranspose * G * (T * U) * K * U.conjTranspose := by
      simp only [mul_assoc]
    _ = T.conjTranspose * (G * K) * U.conjTranspose := by
      rw [hTU, mul_one]
      simp only [mul_assoc]
    _ = (U * T).conjTranspose := by
      rw [hGK, mul_one, Matrix.conjTranspose_mul]
    _ = 1 := by
      have hUT : U * T = 1 := mul_eq_one_comm.mp hTU
      rw [hUT, Matrix.conjTranspose_one]

end SplitZero.MetricRestriction
