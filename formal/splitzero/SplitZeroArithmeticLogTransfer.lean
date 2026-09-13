import SplitZeroRestrictionSpectrum

/-!
# A signed, logarithm-free certificate for arithmetic/reference volume corrections

The two quotient metrics need not be ordered. A single positive numerical
scale c puts all four positive comparison spectra in (0,c]. It is not a
change of the source measure. The four q*log(c) terms cancel before any
bound is taken. The remaining enclosure uses the inherited trace certificate.
-/
noncomputable section
namespace SplitZero.ArithmeticLogTransfer
open Matrix
open scoped BigOperators
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- Explicit coordinate comparison; not an assertion of Euclidean normality. -/
structure LossWitness (H : Matrix ι ι ℂ) where
  U : Matrix ι ι ℂ
  V : Matrix ι ι ℂ
  x : ι → ℝ
  left_inverse : U * V = 1
  right_inverse : V * U = 1
  diagonalization : H = U * Matrix.diagonal (fun a => (x a : ℂ)) * V
  nonnegative : ∀ a, 0 ≤ x a
  below_one : ∀ a, x a < 1

def prefix (H : Matrix ι ι ℂ) (p : ℕ) : ℝ :=
  RestrictionSpectrum.matrixPrefix H p

def upper (H : Matrix ι ι ℂ) (p : ℕ) : ℝ :=
  prefix H p + (prefix H (2*p)-prefix H p)/(1-RestrictionSpectrum.moment H p)

def logDet (A : Matrix ι ι ℂ) : ℝ := Real.log A.det.re

def signedLog (A : Fin 4 → Matrix ι ι ℂ) : ℝ :=
  logDet (A 0) + logDet (A 1) - logDet (A 2) - logDet (A 3)

namespace LossWitness
variable {H : Matrix ι ι ℂ}

theorem det_positive (w : LossWitness H) : 0 < (1-H).det.re := by
  rw [RestrictionSpectrum.determinant_eq H w.U w.V w.x
    w.left_inverse w.diagonalization]
  exact Finset.prod_pos fun a _ha => sub_pos.mpr (w.below_one a)

theorem bounds (w : LossWitness H) (p : ℕ)
    (hs : RestrictionSpectrum.moment H p < 1) :
    prefix H p ≤ -Real.log (1-H).det.re ∧
    -Real.log (1-H).det.re ≤ upper H p := by
  constructor
  · rw [RestrictionSpectrum.log_volume_eq H w.U w.V w.x
      w.left_inverse w.diagonalization w.below_one]
    rw [show prefix H p = RestrictionLog.prefixTrace w.x p from
      RestrictionSpectrum.prefix_eq H w.U w.V w.x
        w.left_inverse w.right_inverse w.diagonalization p]
    exact RestrictionLog.prefix_lower w.x w.nonnegative w.below_one p
  · exact RestrictionSpectrum.matrix_certificate H w.U w.V w.x
      w.left_inverse w.right_inverse w.diagonalization w.nonnegative w.below_one p hs

theorem stopping (w : LossWitness H) :
    ∃ p : ℕ, 0 < p ∧ RestrictionSpectrum.moment H p < 1 :=
  RestrictionSpectrum.matrix_stopping_degree H w.U w.V w.x
    w.left_inverse w.right_inverse w.diagonalization w.nonnegative w.below_one

end LossWitness

/-- The determinant ratio is for the actual inverse-Gram composite. -/
theorem comparison_det (G₀ G₁ K₀ : Matrix ι ι ℂ)
    (hK : K₀ * G₀ = 1) (hG : G₀.det ≠ 0) :
    (K₀ * G₁).det = G₁.det / G₀.det := by
  apply (eq_div_iff hG).mpr
  have h := congrArg Matrix.det hK
  simp only [Matrix.det_mul, Matrix.det_one] at h ⊢
  calc
    K₀.det * G₁.det * G₀.det = (K₀.det * G₀.det) * G₁.det := by ring
    _ = G₁.det := by rw [h, one_mul]

theorem normalized_reconstruction (A : Matrix ι ι ℂ) (c : ℝ) (hc : c ≠ 0) :
    A = (c : ℂ) • (1 - (1 - (c : ℂ)⁻¹ • A)) := by
  rw [sub_sub_cancel, smul_smul, mul_inv_cancel₀ (by exact_mod_cast hc), one_smul]

/-- Scaling is recorded before taking the real logarithm. -/
theorem scaled_log (A H : Matrix ι ι ℂ) (c : ℝ) (hc : 0 < c)
    (hA : A = (c : ℂ) • (1-H)) (hd : 0 < (1-H).det.re) :
    logDet A = (Fintype.card ι : ℝ) * Real.log c + Real.log (1-H).det.re := by
  have he : A.det.re = c^(Fintype.card ι) * (1-H).det.re := by
    rw [hA, Matrix.det_smul]
    simp [Complex.mul_re, ← Complex.ofReal_pow]
  unfold logDet
  rw [he, Real.log_mul (ne_of_gt (pow_pos hc _)) (ne_of_gt hd), Real.log_pow]

/-- An unordered positive metric comparison is reduced to the existing certificate. -/
theorem scaled_interval (A H : Matrix ι ι ℂ) (c : ℝ) (hc : 0 < c)
    (hA : A = (c : ℂ) • (1-H)) (w : LossWitness H) (p : ℕ)
    (hs : RestrictionSpectrum.moment H p < 1) :
    (Fintype.card ι : ℝ)*Real.log c - upper H p ≤ logDet A ∧
    logDet A ≤ (Fintype.card ι : ℝ)*Real.log c - prefix H p := by
  rw [scaled_log A H c hc hA w.det_positive]
  obtain ⟨hl,hu⟩ := w.bounds p hs
  constructor <;> linarith

/-- The common scale cancels from the signed four-endpoint correction.
Only finite trace powers, sums and divisions occur in the resulting bounds. -/
theorem signed_four_certificate
    (A H : Fin 4 → Matrix ι ι ℂ) (c : ℝ) (hc : 0 < c)
    (hA : ∀ a, A a = (c : ℂ) • (1-H a))
    (w : ∀ a, LossWitness (H a)) (p : Fin 4 → ℕ)
    (hs : ∀ a, RestrictionSpectrum.moment (H a) (p a) < 1) :
    prefix (H 2) (p 2) + prefix (H 3) (p 3) - upper (H 0) (p 0) -
      upper (H 1) (p 1) ≤ signedLog A ∧
    signedLog A ≤ upper (H 2) (p 2) + upper (H 3) (p 3) -
      prefix (H 0) (p 0) - prefix (H 1) (p 1) := by
  have h0 := scaled_interval (A 0) (H 0) c hc (hA 0) (w 0) (p 0) (hs 0)
  have h1 := scaled_interval (A 1) (H 1) c hc (hA 1) (w 1) (p 1) (hs 1)
  have h2 := scaled_interval (A 2) (H 2) c hc (hA 2) (w 2) (p 2) (hs 2)
  have h3 := scaled_interval (A 3) (H 3) c hc (hA 3) (w 3) (p 3) (hs 3)
  unfold signedLog
  constructor <;> linarith [h0.1,h0.2,h1.1,h1.2,h2.1,h2.2,h3.1,h3.2]

/-- Separate finite stopping orders are enough; no bound uniform in k is asserted. -/
theorem four_stopping (H : Fin 4 → Matrix ι ι ℂ) (w : ∀ a, LossWitness (H a)) :
    ∃ p : Fin 4 → ℕ, ∀ a, 0 < p a ∧ RestrictionSpectrum.moment (H a) (p a) < 1 := by
  choose p hp using fun a => (w a).stopping
  exact ⟨p,hp⟩

/-- A certified negative upper endpoint bound proves a negative signed correction. -/
theorem certified_negative (A H : Fin 4 → Matrix ι ι ℂ) (c : ℝ) (hc : 0 < c)
    (hA : ∀ a, A a = (c : ℂ) • (1-H a))
    (w : ∀ a, LossWitness (H a)) (p : Fin 4 → ℕ)
    (hs : ∀ a, RestrictionSpectrum.moment (H a) (p a) < 1)
    (η : ℝ) (hu : upper (H 2) (p 2) + upper (H 3) (p 3) -
      prefix (H 0) (p 0) - prefix (H 1) (p 1) ≤ -η) :
    signedLog A ≤ -η :=
  (signed_four_certificate A H c hc hA w p hs).2.trans hu

end SplitZero.ArithmeticLogTransfer
