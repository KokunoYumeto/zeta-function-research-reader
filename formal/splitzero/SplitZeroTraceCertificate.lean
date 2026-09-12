import SplitZeroGramTrace

/-!
# Construct the two control projections from the actual two-coordinate factor

No eigenvectors of the arithmetic action are chosen. Cayley--Hamilton is
proved directly for the 2 by 2 compressed matrix. Its trace and determinant
produce the control polynomial and its rank-one spectral projectors.
-/
noncomputable section
namespace SplitZero.TraceCertificate
open Matrix
variable {n : Type*} [Fintype n] [DecidableEq n]

theorem two_cayley (C : Matrix (Fin 2) (Fin 2) ℂ) :
    C * C - Matrix.trace C • C + C.det • 1 = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two,
      Matrix.det_fin_two, Matrix.one_apply] <;> ring

theorem two_square (C : Matrix (Fin 2) (Fin 2) ℂ) (z : ℂ)
    (ht : Matrix.trace C = 0) (hd : C.det = -(z ^ 2)) :
    C * C = z ^ 2 • 1 := by
  have h := two_cayley C
  rw [ht, hd, zero_smul, sub_zero, neg_smul] at h
  exact sub_eq_zero.mp (by simpa only [sub_eq_add_neg] using h)

/-- A cubic annihilator for the ambient operator, derived from its factorization. -/
theorem factor_cubic (U : Matrix n (Fin 2) ℂ) (V : Matrix (Fin 2) n ℂ)
    (z : ℂ) (ht : Matrix.trace (V * U) = 0)
    (hd : (V * U).det = -(z ^ 2)) :
    (U * V) * (U * V) * (U * V) = z ^ 2 • (U * V) := by
  calc
    _ = U * ((V * U) * (V * U)) * V := by simp only [Matrix.mul_assoc]
    _ = U * (z ^ 2 • 1) * V := by rw [two_square (V * U) z ht hd]
    _ = z ^ 2 • (U * V) := by simp only [Matrix.mul_smul, Matrix.smul_mul, mul_one]

theorem factor_trace (U : Matrix n (Fin 2) ℂ) (V : Matrix (Fin 2) n ℂ)
    (ht : Matrix.trace (V * U) = 0) : Matrix.trace (U * V) = 0 := by
  rw [Matrix.trace_mul_comm, ht]

theorem factor_square_trace (U : Matrix n (Fin 2) ℂ) (V : Matrix (Fin 2) n ℂ)
    (z : ℂ) (ht : Matrix.trace (V * U) = 0)
    (hd : (V * U).det = -(z ^ 2)) :
    Matrix.trace ((U * V) * (U * V)) = 2 * z ^ 2 := by
  calc
    _ = Matrix.trace (U * (V * (U * V))) := by rw [Matrix.mul_assoc]
    _ = Matrix.trace ((V * (U * V)) * U) := Matrix.trace_mul_comm _ _
    _ = Matrix.trace ((V * U) * (V * U)) := by simp only [Matrix.mul_assoc]
    _ = Matrix.trace (z ^ 2 • (1 : Matrix (Fin 2) (Fin 2) ℂ)) := by
      rw [two_square (V * U) z ht hd]
    _ = 2 * z ^ 2 := by simp [Matrix.trace_smul]; ring

def numerator (H : Matrix n n ℂ) (z : ℂ) : Matrix n n ℂ := H * H + z • H

def spectralProjection (H : Matrix n n ℂ) (z : ℂ) : Matrix n n ℂ :=
  (2 * z ^ 2)⁻¹ • numerator H z

theorem numerator_square (H : Matrix n n ℂ) (z : ℂ)
    (h3 : H * H * H = z ^ 2 • H) :
    numerator H z * numerator H z = (2 * z ^ 2) • numerator H z := by
  have h4 : (H * H) * (H * H) = z ^ 2 • (H * H) := by
    calc
      _ = (H * H * H) * H := by noncomm_ring
      _ = (z ^ 2 • H) * H := by rw [h3]
      _ = z ^ 2 • (H * H) := Matrix.smul_mul _ _ _
  have h3r : H * (H * H) = z ^ 2 • H := by rw [← Matrix.mul_assoc, h3]
  calc
    _ = (H * H) * (H * H) + z • ((H * H) * H) +
        z • (H * (H * H)) + (z * z) • (H * H) := by
      simp only [numerator, mul_add, add_mul, Matrix.mul_smul,
        Matrix.smul_mul, smul_smul]
      abel
    _ = (2 * z ^ 2) • numerator H z := by
      rw [h4, h3, h3r]
      ext i j
      simp only [numerator, Matrix.smul_apply, Matrix.add_apply, smul_eq_mul]
      ring

theorem spectralProjection_idempotent (H : Matrix n n ℂ) (z : ℂ) (hz : z ≠ 0)
    (h3 : H * H * H = z ^ 2 • H) :
    spectralProjection H z * spectralProjection H z = spectralProjection H z := by
  unfold spectralProjection
  rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, numerator_square H z h3, smul_smul]
  have hs : (2 * z ^ 2)⁻¹ * (2 * z ^ 2)⁻¹ * (2 * z ^ 2) = (2 * z ^ 2)⁻¹ := by
    field_simp
  rw [hs]

theorem spectralProjection_selfadjoint (H : Matrix n n ℂ) (e : ℝ)
    (hH : H.conjTranspose = H) :
    (spectralProjection H (e : ℂ)).conjTranspose = spectralProjection H (e : ℂ) := by
  simp [spectralProjection, numerator, Matrix.conjTranspose_smul,
    Matrix.conjTranspose_mul, hH, Complex.star_def]

theorem spectralProjection_trace (H : Matrix n n ℂ) (z : ℂ) (hz : z ≠ 0)
    (ht : Matrix.trace H = 0) (ht2 : Matrix.trace (H * H) = 2 * z ^ 2) :
    Matrix.trace (spectralProjection H z) = 1 := by
  have hd : 2 * z ^ 2 ≠ 0 := mul_ne_zero (by norm_num) (pow_ne_zero _ hz)
  simp only [spectralProjection, numerator, Matrix.trace_smul, Matrix.trace_add,
    ht, ht2, smul_eq_mul, mul_zero, add_zero]
  exact inv_mul_cancel₀ hd

theorem spectralProjection_difference (H : Matrix n n ℂ) (z : ℂ) (hz : z ≠ 0) :
    z • (spectralProjection H z - spectralProjection H (-z)) = H := by
  ext i j
  simp only [spectralProjection, numerator, Matrix.smul_apply, Matrix.sub_apply,
    Matrix.add_apply, smul_eq_mul, neg_sq]
  field_simp
  ring

/-- The aggregate trace estimate with the control projections constructed, not assumed. -/
theorem positive_certificate_bound {d : Type*} [Fintype d] [DecidableEq d]
    (A : Matrix n n ℂ) (B : Matrix n d ℂ) (L : Matrix d n ℂ)
    (a : Matrix d d ℂ) (w e : ℝ)
    (U : Matrix n (Fin 2) ℂ) (V : Matrix (Fin 2) n ℂ)
    (he : 0 < e) (hLB : L * B = 1) (hAB : A * B = B * a)
    (hP : (B * L).conjTranspose = B * L)
    (hH : A.conjTranspose + A - (w : ℂ) • 1 = U * V)
    (ht : Matrix.trace (V * U) = 0) (hd : (V * U).det = -((e : ℂ) ^ 2)) :
    |2 * (Matrix.trace a).re - w * (Fintype.card d : ℝ)| ≤ e := by
  let H := U * V
  have h3 : H * H * H = (e : ℂ) ^ 2 • H := factor_cubic U V _ ht hd
  have htH : Matrix.trace H = 0 := factor_trace U V ht
  have htH2 : Matrix.trace (H * H) = 2 * (e : ℂ) ^ 2 := factor_square_trace U V _ ht hd
  have heC : (e : ℂ) ≠ 0 := by exact_mod_cast (ne_of_gt he)
  have hnC : -(e : ℂ) ≠ 0 := neg_ne_zero.mpr heC
  have hHs : H.conjTranspose = H := by
    change (U * V).conjTranspose = U * V
    rw [← hH]
    simp only [Matrix.conjTranspose_sub, Matrix.conjTranspose_add,
      Matrix.conjTranspose_conjTranspose, Matrix.conjTranspose_smul,
      Matrix.conjTranspose_one, Complex.star_def, Complex.conj_ofReal]
    abel
  have h3n : H * H * H = (-(e : ℂ)) ^ 2 • H := by simpa only [neg_sq] using h3
  have htH2n : Matrix.trace (H * H) = 2 * (-(e : ℂ)) ^ 2 := by
    simpa only [neg_sq] using htH2
  have hps := spectralProjection_selfadjoint H e hHs
  have hms : (spectralProjection H (-(e : ℂ))).conjTranspose =
      spectralProjection H (-(e : ℂ)) := by
    simpa only [Complex.ofReal_neg] using spectralProjection_selfadjoint H (-e) hHs
  apply SplitZero.TraceProjection.invariant_excess_bound A B L a w e
    (spectralProjection H (e : ℂ)) (spectralProjection H (-(e : ℂ)))
    hLB hAB hP (le_of_lt he)
    (spectralProjection_idempotent H _ heC h3) hps
    (spectralProjection_idempotent H _ hnC h3n) hms
  · rw [spectralProjection_trace H _ heC htH htH2]; rfl
  · rw [spectralProjection_trace H _ hnC htH htH2n]; rfl
  · rw [hH]
    exact (spectralProjection_difference H _ heC).symm

end SplitZero.TraceCertificate
