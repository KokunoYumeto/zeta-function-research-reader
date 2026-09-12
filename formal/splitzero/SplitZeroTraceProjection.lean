import Mathlib

/-!
# Projection traces for the source-generated rank-two control

The two control projections are explicit inputs, not projections of A.
The invariant arithmetic subspace has an inclusion and a left inverse.
No normality of A and no orthogonality of its spectral projector is assumed.
The final theorem is a finite trace theorem. Exterior source maps and the
analytic construction of the canonical Gram are separate interfaces.
-/
noncomputable section
namespace SplitZero.TraceProjection
open Matrix
open scoped ComplexOrder
variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Squared Hilbert--Schmidt norm in the displayed coordinates. -/
def hsSq (M : Matrix n n ℂ) : ℝ := (Matrix.trace (M.conjTranspose * M)).re

theorem hsSq_nonneg (M : Matrix n n ℂ) : 0 ≤ hsSq M := by
  exact (RCLike.nonneg_iff.mp
    (Matrix.posSemidef_conjTranspose_mul_self M).trace_nonneg).1

/-- The overlap of two orthogonal projections is a squared norm. -/
theorem projection_overlap_eq (P F : Matrix n n ℂ)
    (hP : P * P = P) (hPs : P.conjTranspose = P)
    (hF : F * F = F) (hFs : F.conjTranspose = F) :
    hsSq (F * P) = (Matrix.trace (P * F)).re := by
  have he : (F * P).conjTranspose * (F * P) = (P * F) * P := by
    rw [Matrix.conjTranspose_mul, hFs, hPs]
    calc
      (P * F) * (F * P) = P * (F * F) * P := by noncomm_ring
      _ = (P * F) * P := by rw [hF]
  unfold hsSq
  rw [he]
  have ht : Matrix.trace ((P * F) * P) = Matrix.trace (P * F) := by
    calc
      _ = Matrix.trace (P * (P * F)) := Matrix.trace_mul_comm _ _
      _ = Matrix.trace ((P * P) * F) := by rw [Matrix.mul_assoc]
      _ = Matrix.trace (P * F) := by rw [hP]
  rw [ht]

/-- The metric complement remains an actual projection. -/
theorem complement_projection (P : Matrix n n ℂ)
    (hP : P * P = P) (hPs : P.conjTranspose = P) :
    (1 - P) * (1 - P) = 1 - P ∧ (1 - P).conjTranspose = 1 - P := by
  constructor
  · calc
      _ = 1 - P - P + P * P := by noncomm_ring
      _ = 1 - P := by rw [hP]; abel
  · simp only [Matrix.conjTranspose_sub, Matrix.conjTranspose_one, hPs]

/-- Rank-one normalization is recorded as the literal trace one. -/
theorem projection_overlap_bounds (P F : Matrix n n ℂ)
    (hP : P * P = P) (hPs : P.conjTranspose = P)
    (hF : F * F = F) (hFs : F.conjTranspose = F)
    (htr : (Matrix.trace F).re = 1) :
    0 ≤ (Matrix.trace (P * F)).re ∧ (Matrix.trace (P * F)).re ≤ 1 := by
  have h0 := hsSq_nonneg (F * P)
  rw [projection_overlap_eq P F hP hPs hF hFs] at h0
  obtain ⟨hC, hCs⟩ := complement_projection P hP hPs
  have h1 := hsSq_nonneg (F * (1 - P))
  rw [projection_overlap_eq (1 - P) F hC hCs hF hFs] at h1
  have he : (Matrix.trace ((1 - P) * F)).re =
      1 - (Matrix.trace (P * F)).re := by
    rw [sub_mul, one_mul, Matrix.trace_sub, Complex.sub_re, htr]
  rw [he] at h1
  exact ⟨h0, by linarith⟩

/-- Signed control on the same coefficient space. -/
def signedControl (e : ℝ) (Fplus Fminus : Matrix n n ℂ) : Matrix n n ℂ :=
  (e : ℂ) • (Fplus - Fminus)

theorem signed_trace_formula (P Fplus Fminus : Matrix n n ℂ) (e : ℝ) :
    (Matrix.trace (P * signedControl e Fplus Fminus)).re =
      e * ((Matrix.trace (P * Fplus)).re - (Matrix.trace (P * Fminus)).re) := by
  simp [signedControl, Matrix.mul_smul, mul_sub, Complex.mul_re]

/-- The allowance is e, independently of the dimension of the selected space. -/
theorem signed_trace_bound (P Fplus Fminus : Matrix n n ℂ) (e : ℝ)
    (he : 0 ≤ e) (hP : P * P = P) (hPs : P.conjTranspose = P)
    (hp : Fplus * Fplus = Fplus) (hps : Fplus.conjTranspose = Fplus)
    (hm : Fminus * Fminus = Fminus) (hms : Fminus.conjTranspose = Fminus)
    (htp : (Matrix.trace Fplus).re = 1)
    (htm : (Matrix.trace Fminus).re = 1) :
    -e ≤ (Matrix.trace (P * signedControl e Fplus Fminus)).re ∧
      (Matrix.trace (P * signedControl e Fplus Fminus)).re ≤ e := by
  obtain ⟨hp0, hp1⟩ := projection_overlap_bounds P Fplus hP hPs hp hps htp
  obtain ⟨hm0, hm1⟩ := projection_overlap_bounds P Fminus hP hPs hm hms htm
  rw [signed_trace_formula]
  constructor <;> nlinarith

/-- Exact slack, including both complementary overlaps. -/
theorem signed_trace_slack (P Fplus Fminus : Matrix n n ℂ) (e : ℝ)
    (hP : P * P = P) (hPs : P.conjTranspose = P)
    (hp : Fplus * Fplus = Fplus) (hps : Fplus.conjTranspose = Fplus)
    (hm : Fminus * Fminus = Fminus) (hms : Fminus.conjTranspose = Fminus)
    (htp : (Matrix.trace Fplus).re = 1) :
    (Matrix.trace (P * signedControl e Fplus Fminus)).re =
      e * (1 - hsSq (Fplus * (1 - P)) - hsSq (Fminus * P)) := by
  obtain ⟨hC, hCs⟩ := complement_projection P hP hPs
  rw [projection_overlap_eq (1 - P) Fplus hC hCs hp hps,
    projection_overlap_eq P Fminus hP hPs hm hms, signed_trace_formula]
  rw [sub_mul, one_mul, Matrix.trace_sub, Complex.sub_re, htp]
  ring

/-- Two different projectors onto the same range need not be equal. -/
theorem projector_difference_square (P Q : Matrix n n ℂ)
    (hP : P * P = P) (hQ : Q * Q = Q)
    (hQP : Q * P = P) (hPQ : P * Q = Q) :
    (P - Q) * (P - Q) = 0 := by
  calc
    _ = P * P - P * Q - Q * P + Q * Q := by noncomm_ring
    _ = 0 := by rw [hP, hQ, hQP, hPQ]; abel

/-- The orthogonal and spectral projectors give the same invariant trace. -/
theorem projector_trace_comparison (P Q A : Matrix n n ℂ)
    (hQP : Q * P = P) (hPQ : P * Q = Q) (hAQ : A * Q = Q * A) :
    Matrix.trace (P * A) = Matrix.trace (Q * A) := by
  calc
    _ = Matrix.trace ((Q * P) * A) := by rw [hQP]
    _ = Matrix.trace ((P * A) * Q) := by
      rw [Matrix.trace_mul_comm, Matrix.mul_assoc]
    _ = Matrix.trace (P * (A * Q)) := by rw [Matrix.mul_assoc]
    _ = Matrix.trace (P * (Q * A)) := by rw [hAQ]
    _ = Matrix.trace ((P * Q) * A) := by rw [Matrix.mul_assoc]
    _ = Matrix.trace (Q * A) := by rw [hPQ]

/-- Trace of the actual compression, using inclusion and coefficient extraction. -/
theorem invariant_trace {d : Type*} [Fintype d] [DecidableEq d]
    (A : Matrix n n ℂ) (B : Matrix n d ℂ) (L : Matrix d n ℂ)
    (a : Matrix d d ℂ) (hLB : L * B = 1) (hAB : A * B = B * a) :
    Matrix.trace ((B * L) * A) = Matrix.trace a := by
  calc
    _ = Matrix.trace ((L * A) * B) := by
      rw [Matrix.mul_assoc, Matrix.trace_mul_comm]
    _ = Matrix.trace (L * (A * B)) := by rw [Matrix.mul_assoc]
    _ = Matrix.trace (L * (B * a)) := by rw [hAB]
    _ = Matrix.trace ((L * B) * a) := by rw [Matrix.mul_assoc]
    _ = Matrix.trace a := by rw [hLB, one_mul]

/-- Real trace of the control, with the weight kept. -/
theorem defect_trace (P A : Matrix n n ℂ) (w : ℝ)
    (hPs : P.conjTranspose = P) :
    (Matrix.trace (P * (A.conjTranspose + A - (w : ℂ) • 1))).re =
      2 * (Matrix.trace (P * A)).re - w * (Matrix.trace P).re := by
  have hs : Matrix.trace (P * A.conjTranspose) = star (Matrix.trace (P * A)) := by
    calc
      _ = Matrix.trace (A.conjTranspose * P) := Matrix.trace_mul_comm _ _
      _ = Matrix.trace ((P * A).conjTranspose) := by
        rw [Matrix.conjTranspose_mul, hPs]
      _ = star (Matrix.trace (P * A)) := Matrix.trace_conjTranspose _
  simp only [mul_sub, mul_add, Matrix.mul_smul, mul_one, Matrix.trace_sub,
    Matrix.trace_add, Matrix.trace_smul, hs]
  simp only [Complex.sub_re, Complex.add_re, smul_eq_mul, Complex.mul_re,
    Complex.ofReal_re, Complex.ofReal_im, zero_mul, sub_zero, Complex.star_def,
    Complex.conj_re]
  ring

/-- Determinant-line excess for the supplied invariant subspace, without a p factor. -/
theorem invariant_excess_bound {d : Type*} [Fintype d] [DecidableEq d]
    (A : Matrix n n ℂ) (B : Matrix n d ℂ) (L : Matrix d n ℂ)
    (a : Matrix d d ℂ) (w e : ℝ) (Fplus Fminus : Matrix n n ℂ)
    (hLB : L * B = 1) (hAB : A * B = B * a)
    (hP : (B * L).conjTranspose = B * L) (he : 0 ≤ e)
    (hp : Fplus * Fplus = Fplus) (hps : Fplus.conjTranspose = Fplus)
    (hm : Fminus * Fminus = Fminus) (hms : Fminus.conjTranspose = Fminus)
    (htp : (Matrix.trace Fplus).re = 1) (htm : (Matrix.trace Fminus).re = 1)
    (hH : A.conjTranspose + A - (w : ℂ) • 1 = signedControl e Fplus Fminus) :
    |2 * (Matrix.trace a).re - w * (Fintype.card d : ℝ)| ≤ e := by
  have hPP : (B * L) * (B * L) = B * L := by
    calc
      _ = B * (L * B) * L := by simp only [Matrix.mul_assoc]
      _ = B * L := by rw [hLB, mul_one]
  have ht : (Matrix.trace (B * L)).re = (Fintype.card d : ℝ) := by
    rw [Matrix.trace_mul_comm, hLB, Matrix.trace_one]
    simp
  have hid := defect_trace (B * L) A w hP
  rw [invariant_trace A B L a hLB hAB, ht, hH] at hid
  rw [← hid]
  exact abs_le.mpr (signed_trace_bound (B * L) Fplus Fminus e he hPP hP
    hp hps hm hms htp htm)

end SplitZero.TraceProjection
