import SplitZeroRestrictionLogCertificate

/-!
An explicit spectral comparison for the original restriction-loss matrix.
U and V are inverse coordinate maps. The comparison does not require H to be
Hermitian in Euclidean coordinates or the arithmetic action to commute with H.
The finite certificate is computed from the original matrix powers.
-/
noncomputable section
namespace SplitZero.RestrictionSpectrum
open Matrix
open scoped BigOperators
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

def moment (H : Matrix ι ι ℂ) (n : ℕ) : ℝ := (Matrix.trace (H^n)).re

def matrixPrefix (H : Matrix ι ι ℂ) (p : ℕ) : ℝ :=
  ∑ n ∈ Finset.range p, moment H (n+1) / ((n : ℝ)+1)

/-- A literal two-sided inverse comparison carries every power. -/
theorem conjugate_power (H U V D : Matrix ι ι ℂ)
    (hUV : U*V=1) (hVU : V*U=1) (hH : H=U*D*V) (n : ℕ) :
    H^n = U*D^n*V := by
  induction n with
  | zero => simp [hUV]
  | succ n ih =>
    rw [pow_succ, ih, hH]
    calc
      (U*D^n*V)*(U*D*V) = U*(D^n*(V*U)*D)*V := by noncomm_ring
      _ = U*D^(n+1)*V := by rw [hVU, Matrix.mul_one, ← pow_succ]

/-- The real trace of the actual matrix power is the finite spectral moment. -/
theorem moment_eq (H U V : Matrix ι ι ℂ) (x : ι → ℝ)
    (hUV : U*V=1) (hVU : V*U=1)
    (hH : H=U*(Matrix.diagonal (fun a => (x a : ℂ)))*V) (n : ℕ) :
    moment H n = RestrictionLog.powerTrace x n := by
  unfold moment
  rw [conjugate_power H U V _ hUV hVU hH n,
    Matrix.trace_mul_comm (U * (Matrix.diagonal (fun a => (x a : ℂ)))^n) V,
    ← Matrix.mul_assoc, hVU, Matrix.one_mul, Matrix.diagonal_pow,
    Matrix.trace_diagonal]
  simp [RestrictionLog.powerTrace, ← Complex.ofReal_pow]

/-- Prefix sums need only original trace powers, not computed eigenvectors. -/
theorem prefix_eq (H U V : Matrix ι ι ℂ) (x : ι → ℝ)
    (hUV : U*V=1) (hVU : V*U=1)
    (hH : H=U*(Matrix.diagonal (fun a => (x a : ℂ)))*V) (p : ℕ) :
    matrixPrefix H p = RestrictionLog.prefixTrace x p := by
  unfold matrixPrefix
  simp_rw [moment_eq H U V x hUV hVU hH]
  exact (RestrictionLog.prefix_as_moments x p).symm

/-- Determinant comparison retains the actual inverse coordinate maps. -/
theorem determinant_eq (H U V : Matrix ι ι ℂ) (x : ι → ℝ)
    (hUV : U*V=1)
    (hH : H=U*(Matrix.diagonal (fun a => (x a : ℂ)))*V) :
    ((1-H).det).re = ∏ a, (1-x a) := by
  have hd : Matrix.diagonal (fun a => (1 : ℂ)-(x a : ℂ)) =
      1-Matrix.diagonal (fun a => (x a : ℂ)) := by
    ext a b
    by_cases h : a=b <;> simp [h]
  have hc : 1-H = U*(Matrix.diagonal (fun a => (1 : ℂ)-(x a : ℂ)))*V := by
    rw [hd, Matrix.mul_sub, Matrix.mul_one, Matrix.sub_mul, hUV, hH]
  have he : (1-H).det = ∏ a, ((1 : ℂ)-(x a : ℂ)) := by
    rw [hc]
    calc
      _ = (U*V).det * (Matrix.diagonal (fun a => (1 : ℂ)-(x a : ℂ))).det := by
        simp only [Matrix.det_mul]
        ring
      _ = _ := by rw [hUV, Matrix.det_one, one_mul, Matrix.det_diagonal]
  rw [he]
  norm_cast

/-- No complex logarithm branch is needed: the determinant is positive. -/
theorem log_volume_eq (H U V : Matrix ι ι ℂ) (x : ι → ℝ)
    (hUV : U*V=1)
    (hH : H=U*(Matrix.diagonal (fun a => (x a : ℂ)))*V)
    (hx1 : ∀ a, x a < 1) :
    -Real.log (((1-H).det).re) = RestrictionLog.logVolume x := by
  rw [determinant_eq H U V x hUV hH,
    Real.log_prod (fun a _ha => ne_of_gt (sub_pos.mpr (hx1 a)))]
  simp only [RestrictionLog.logVolume, Finset.sum_neg_distrib]

/-- Closed upper formula on the actual H. Its spectral witness proves applicability;
the witness entries are not used to evaluate the finite certificate. -/
theorem matrix_certificate (H U V : Matrix ι ι ℂ) (x : ι → ℝ)
    (hUV : U*V=1) (hVU : V*U=1)
    (hH : H=U*(Matrix.diagonal (fun a => (x a : ℂ)))*V)
    (hx0 : ∀ a, 0 ≤ x a) (hx1 : ∀ a, x a < 1)
    (p : ℕ) (hs : moment H p < 1) :
    -Real.log (((1-H).det).re) ≤ matrixPrefix H p +
      (matrixPrefix H (2*p)-matrixPrefix H p)/(1-moment H p) := by
  rw [log_volume_eq H U V x hUV hH hx1,
    prefix_eq H U V x hUV hVU hH p,
    prefix_eq H U V x hUV hVU hH (2*p),
    moment_eq H U V x hUV hVU hH p]
  apply RestrictionLog.adaptive_trace_upper x hx0 hx1 p
  rwa [moment_eq H U V x hUV hVU hH p] at hs

/-- Every fixed source restriction terminates this trace-only gap search. -/
theorem matrix_stopping_degree (H U V : Matrix ι ι ℂ) (x : ι → ℝ)
    (hUV : U*V=1) (hVU : V*U=1)
    (hH : H=U*(Matrix.diagonal (fun a => (x a : ℂ)))*V)
    (hx0 : ∀ a, 0 ≤ x a) (hx1 : ∀ a, x a < 1) :
    ∃ p : ℕ, 0 < p ∧ moment H p < 1 := by
  simpa only [moment_eq H U V x hUV hVU hH] using
    RestrictionLog.exists_stopping_degree x hx0 hx1

end SplitZero.RestrictionSpectrum
