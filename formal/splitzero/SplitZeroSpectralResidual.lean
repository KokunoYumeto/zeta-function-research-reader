import SplitZeroCanonicalSignedResolvent

/-!
# Transport the exact spectral residual into the original signed trace bound

A simultaneous diagonalization is supplied as explicit equations for an
isometry of the original metric. It is not a replacement of that metric.
The diagonalization can be numerically or algebraically instantiated; this
module does not manufacture a uniform bound over changing endpoint pairs.
-/
noncomputable section
namespace SplitZero.SpectralResidual
open Matrix SignedTraceEnclosure ResolventSeries CanonicalSignedResolvent
open scoped BigOperators ComplexOrder MatrixOrder
variable {j : Type*} [Fintype j] [DecidableEq j]
variable {M : Matrix j j ℂ} (F : MetricFrame M)

theorem frame_one : F.conjugate 1 = 1 := by
  simp only [MetricFrame.conjugate, Matrix.mul_one, F.forward_inverse]

theorem frame_sub (A B : Matrix j j ℂ) :
    F.conjugate (A - B) = F.conjugate A - F.conjugate B := by
  simp only [MetricFrame.conjugate, Matrix.mul_sub, Matrix.sub_mul]

theorem frame_smul (c : ℝ) (A : Matrix j j ℂ) :
    F.conjugate (c • A) = c • F.conjugate A := by
  simp only [MetricFrame.conjugate, Matrix.mul_smul, Matrix.smul_mul]

theorem frame_pow (A : Matrix j j ℂ) (p : ℕ) :
    F.conjugate (A ^ p) = F.conjugate A ^ p := by
  induction p with
  | zero => simpa only [pow_zero] using frame_one F
  | succ p ih => rw [pow_succ, F.conjugate_mul, ih, pow_succ]

theorem frame_center (A : Matrix j j ℂ) :
    F.conjugate (center A) = center (F.conjugate A) := by
  have ht : realTrace (F.conjugate A) = realTrace A :=
    congrArg Complex.re (F.trace_conjugate A)
  simp only [center, frame_sub, frame_smul, frame_one, ht]

theorem realTrace_diagonal (f : j → ℝ) :
    realTrace (Matrix.diagonal (fun i => (f i : ℂ))) = ∑ i, f i := by
  simp [realTrace, Matrix.trace]

theorem center_diagonal (f : j → ℝ) :
    center (Matrix.diagonal (fun i => (f i : ℂ))) =
      Matrix.diagonal (fun i => ((f i - mean f : ℝ) : ℂ)) := by
  rw [center, realTrace_diagonal]
  ext i k
  by_cases h : i = k
  · subst k
    simp [mean]
  · simp [Matrix.diagonal_apply, h]

theorem residual_diagonal (H X : Matrix j j ℂ) (h g : j → ℝ)
    (hH : F.conjugate H = Matrix.diagonal (fun i => (h i : ℂ)))
    (hX : F.conjugate X = Matrix.diagonal (fun i => (g i : ℂ))) (L : ℕ) :
    F.conjugate (H ^ (L + 1) * X) =
      Matrix.diagonal (fun i => ((residualSpectrum h g L i : ℝ) : ℂ)) := by
  rw [F.conjugate_mul, frame_pow, hH, hX, Matrix.diagonal_pow, Matrix.diagonal_mul_diagonal]
  congr 1
  funext i
  simp [residualSpectrum]

/-- This is an identity for the actual residual matrix, not only its rank. -/
theorem residual_energy (H X : Matrix j j ℂ) (h g : j → ℝ)
    (hH : F.conjugate H = Matrix.diagonal (fun i => (h i : ℂ)))
    (hX : F.conjugate X = Matrix.diagonal (fun i => (g i : ℂ))) (L : ℕ) :
    realTrace (center (H ^ (L + 1) * X) * center (H ^ (L + 1) * X)) =
      variance (residualSpectrum h g L) := by
  let d := residualSpectrum h g L
  have hd : F.conjugate (center (H ^ (L + 1) * X)) =
      Matrix.diagonal (fun i => ((d i - mean d : ℝ) : ℂ)) := by
    rw [frame_center, residual_diagonal F H X h g hH hX L, center_diagonal]
  have he : (Matrix.diagonal (fun i => ((d i - mean d : ℝ) : ℂ))) *
      (Matrix.diagonal (fun i => ((d i - mean d : ℝ) : ℂ))) =
      Matrix.diagonal (fun i => (((d i - mean d) ^ 2 : ℝ) : ℂ)) := by
    rw [Matrix.diagonal_mul_diagonal]
    congr 1
    funext i
    push_cast
    ring
  calc
    _ = realTrace (F.conjugate (center (H ^ (L + 1) * X) * center (H ^ (L + 1) * X))) :=
      (congrArg Complex.re (F.trace_conjugate _)).symm
    _ = variance d := by
      rw [F.conjugate_mul, hd, he, realTrace_diagonal]
      rfl

section Bound
variable [Nonempty j]

/-- A fixed-pair geometric bound for the centered error radius. -/
theorem spectral_radius_bound (h g a : j → ℝ) (θ Z : ℝ) (hθ : 0 ≤ θ) (hZ : 0 ≤ Z)
    (hh : ∀ i, |h i| ≤ θ) (hg : ∀ i, |g i| ≤ a i) (L : ℕ) :
    Real.sqrt (variance (residualSpectrum h g L) * Z) ≤
      radius θ (∑ i, a i ^ 2) Z L := by
  have hb := Real.sqrt_le_sqrt
    (mul_le_mul_of_nonneg_right (residual_variance_bound h g a θ hθ hh hg L) hZ)
  rw [mul_assoc, Real.sqrt_mul (sq_nonneg _), Real.sqrt_sq (pow_nonneg hθ _)] at hb
  exact hb

/-- Signed matrix error with the diagonalization transported back in full. -/
theorem signed_error (H T X Q : Matrix j j ℂ) (h g a : j → ℝ) (θ : ℝ)
    (hM : M.PosDef) (hHself : H.conjTranspose * M = M * H)
    (hXself : X.conjTranspose * M = M * X)
    (hQself : Q.conjTranspose * M = M * Q) (htQ : Matrix.trace Q = 0)
    (hc : H * X = X * H) (hsolve : (1 - H) * X = T)
    (hH : F.conjugate H = Matrix.diagonal (fun i => (h i : ℂ)))
    (hX : F.conjugate X = Matrix.diagonal (fun i => (g i : ℂ)))
    (hθ : 0 ≤ θ) (hh : ∀ i, |h i| ≤ θ) (hg : ∀ i, |g i| ≤ a i) (L : ℕ) :
    |realTrace (X * Q) - realTrace (partialSum H T L * Q)| ≤
      radius θ (∑ i, a i ^ 2) (realTrace (Q * Q)) L := by
  have hy := weighted_partialSum M H T X hHself hXself hc hsolve L
  have hsub : (X - partialSum H T L).conjTranspose * M = M * (X - partialSum H T L) := by
    simp only [Matrix.conjTranspose_sub, Matrix.sub_mul, Matrix.mul_sub, hXself, hy]
  have hb := weighted_schwarz M (center (X - partialSum H T L)) Q hM
    (weighted_center M _ hsub) hQself
  rw [centered_pairing _ _ htQ] at hb
  have he : realTrace ((X - partialSum H T L) * Q) =
      realTrace (X * Q) - realTrace (partialSum H T L * Q) := by
    simp only [realTrace, Matrix.sub_mul, Matrix.trace_sub, Complex.sub_re]
  rw [he, residual_exact H T X L hsolve, residual_energy F H X h g hH hX L] at hb
  have hq : 0 ≤ realTrace (Q * Q) := by
    have h := hermitian_square_nonneg (F.conjugate Q) (F.hermitian_conjugate Q hQself)
    rw [← F.conjugate_mul] at h
    exact (congrArg Complex.re (F.trace_conjugate (Q * Q))) ▸ h
  exact hb.trans (spectral_radius_bound h g a θ _ hθ hq hh hg L)
end Bound
end SplitZero.SpectralResidual
