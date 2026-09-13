import SplitZeroArithmeticLogTransfer

/-!
# Trace-data enclosures for the original signed arithmetic correction

The exact moments are not silently replaced by floating point values.
Lower and upper input bounds are explicit. The positive tail is summed
DIRECTLY, never as a difference of independently rounded prefixes.
-/
noncomputable section
namespace SplitZero.CertifiedTraceBounds
open Matrix
open scoped BigOperators

/-- A block of the log series, with every denominator retained. -/
def block (s : ℕ → ℝ) (start len : ℕ) : ℝ :=
  ∑ n ∈ Finset.range len, s (start+n+1) / (((start+n : ℕ) : ℝ)+1)

def lower (lo : ℕ → ℝ) (p : ℕ) : ℝ := block lo 0 p

def upper (hi : ℕ → ℝ) (p : ℕ) : ℝ :=
  block hi 0 p + block hi p p / (1-hi p)

theorem block_split (s : ℕ → ℝ) (p : ℕ) :
    block s 0 (2*p) = block s 0 p + block s p p := by
  rw [show 2*p = p+p by omega]
  unfold block
  rw [Finset.sum_range_add]
  simp only [zero_add]

theorem block_mono (s t : ℕ → ℝ) (a b : ℕ)
    (h : ∀ n, a+1 ≤ n → n ≤ a+b → s n ≤ t n) :
    block s a b ≤ block t a b := by
  unfold block
  apply Finset.sum_le_sum
  intro n hn
  have hn' := Finset.mem_range.mp hn
  apply div_le_div_of_nonneg_right (h (a+n+1) (by omega) (by omega))
  positivity

variable {ι : Type*} [Fintype ι]

theorem prefix_block (x : ι → ℝ) (p : ℕ) :
    RestrictionLog.prefixTrace x p = block (RestrictionLog.powerTrace x) 0 p := by
  simpa only [block, zero_add] using RestrictionLog.prefix_as_moments x p

/-- Valid for certified input intervals; no exact evaluation of a logarithm is used. -/
theorem spectral_interval (x : ι → ℝ)
    (hx0 : ∀ a, 0 ≤ x a) (hx1 : ∀ a, x a < 1)
    (p : ℕ) (hp : 0 < p) (lo hi : ℕ → ℝ)
    (hlo : ∀ n, 1 ≤ n → n ≤ 2*p → lo n ≤ RestrictionLog.powerTrace x n)
    (hhi : ∀ n, 1 ≤ n → n ≤ 2*p → RestrictionLog.powerTrace x n ≤ hi n)
    (hstop : hi p < 1) :
    lower lo p ≤ RestrictionLog.logVolume x ∧
    RestrictionLog.logVolume x ≤ upper hi p := by
  classical
  have hsp := hhi p hp (by omega)
  have hxp (a : ι) : x a ^ p ≤ hi p :=
    (Finset.single_le_sum (fun b _hb => pow_nonneg (hx0 b) p)
      (Finset.mem_univ a)).trans hsp
  have hh := Finset.sum_le_sum (s := Finset.univ)
    (fun a _ha => RestrictionLog.adaptive_scalar (x a) (hi p)
      (hx0 a) (hx1 a) p (hxp a) hstop)
  have hu : RestrictionLog.logVolume x ≤ RestrictionLog.prefixTrace x p +
      (RestrictionLog.prefixTrace x (2*p)-RestrictionLog.prefixTrace x p)/(1-hi p) := by
    simpa only [Finset.sum_add_distrib, ← Finset.sum_div, Finset.sum_sub_distrib,
      RestrictionLog.prefixTrace, RestrictionLog.logVolume] using hh
  rw [prefix_block, prefix_block, block_split, add_sub_cancel_left] at hu
  have hpre : block (RestrictionLog.powerTrace x) 0 p ≤ block hi 0 p :=
    block_mono _ _ 0 p (fun n hn hn' => hhi n (by omega) (by omega))
  have htail : block (RestrictionLog.powerTrace x) p p ≤ block hi p p :=
    block_mono _ _ p p (fun n hn hn' => hhi n (by omega) (by omega))
  constructor
  · have hl := block_mono lo (RestrictionLog.powerTrace x) 0 p
      (fun n hn hn' => hlo n (by omega) (by omega))
    change block lo 0 p ≤ _
    rw [← prefix_block] at hl
    exact hl.trans (RestrictionLog.prefix_lower x hx0 hx1 p)
  · exact hu.trans (add_le_add hpre
      (div_le_div_of_nonneg_right htail (by linarith)))

variable [DecidableEq ι]

/-- Same actual matrix, with its inherited two-sided spectral coordinate witness. -/
theorem matrix_interval (H : Matrix ι ι ℂ)
    (w : ArithmeticLogTransfer.LossWitness H)
    (p : ℕ) (hp : 0 < p) (lo hi : ℕ → ℝ)
    (hlo : ∀ n, 1 ≤ n → n ≤ 2*p → lo n ≤ RestrictionSpectrum.moment H n)
    (hhi : ∀ n, 1 ≤ n → n ≤ 2*p → RestrictionSpectrum.moment H n ≤ hi n)
    (hstop : hi p < 1) :
    lower lo p ≤ -Real.log (1-H).det.re ∧
    -Real.log (1-H).det.re ≤ upper hi p := by
  rw [RestrictionSpectrum.log_volume_eq H w.U w.V w.x
    w.left_inverse w.diagonalization w.below_one]
  apply spectral_interval w.x w.nonnegative w.below_one p hp lo hi
  · intro n hn hn'
    rw [← RestrictionSpectrum.moment_eq H w.U w.V w.x
      w.left_inverse w.right_inverse w.diagonalization n]
    exact hlo n hn hn'
  · intro n hn hn'
    rw [← RestrictionSpectrum.moment_eq H w.U w.V w.x
      w.left_inverse w.right_inverse w.diagonalization n]
    exact hhi n hn hn'
  · exact hstop

/-- A validated absolute error produces the exact lower/upper hypotheses. -/
theorem error_bounds (actual approx error : ℝ) (h : |approx-actual| ≤ error) :
    approx-error ≤ actual ∧ actual ≤ approx+error := by
  obtain ⟨h₁,h₂⟩ := abs_le.mp h
  constructor <;> linarith

/-- The four endpoint signs are retained AFTER the common scale cancels. -/
theorem signed_four_interval
    (A H : Fin 4 → Matrix ι ι ℂ) (c : ℝ) (hc : 0 < c)
    (hA : ∀ a, A a = (c : ℂ) • (1-H a))
    (w : ∀ a, ArithmeticLogTransfer.LossWitness (H a))
    (p : Fin 4 → ℕ) (hp : ∀ a, 0 < p a)
    (lo hi : Fin 4 → ℕ → ℝ)
    (hlo : ∀ a n, 1 ≤ n → n ≤ 2*p a → lo a n ≤ RestrictionSpectrum.moment (H a) n)
    (hhi : ∀ a n, 1 ≤ n → n ≤ 2*p a → RestrictionSpectrum.moment (H a) n ≤ hi a n)
    (hstop : ∀ a, hi a (p a) < 1) :
    lower (lo 2) (p 2) + lower (lo 3) (p 3) - upper (hi 0) (p 0) - upper (hi 1) (p 1)
      ≤ ArithmeticLogTransfer.signedLog A ∧
    ArithmeticLogTransfer.signedLog A ≤
      upper (hi 2) (p 2) + upper (hi 3) (p 3) - lower (lo 0) (p 0) - lower (lo 1) (p 1) := by
  have hiEach (a : Fin 4) := matrix_interval (H a) (w a) (p a) (hp a)
    (lo a) (hi a) (hlo a) (hhi a) (hstop a)
  have he (a : Fin 4) := ArithmeticLogTransfer.scaled_log (A a) (H a) c hc
    (hA a) (w a).det_positive
  unfold ArithmeticLogTransfer.signedLog
  rw [he 0, he 1, he 2, he 3]
  constructor <;> linarith [(hiEach 0).1,(hiEach 0).2,(hiEach 1).1,(hiEach 1).2,
    (hiEach 2).1,(hiEach 2).2,(hiEach 3).1,(hiEach 3).2]

/-- A negative correction can be certified from enclosures, not just exact moments. -/
theorem signed_negative
    (A H : Fin 4 → Matrix ι ι ℂ) (c : ℝ) (hc : 0 < c)
    (hA : ∀ a, A a = (c : ℂ) • (1-H a))
    (w : ∀ a, ArithmeticLogTransfer.LossWitness (H a))
    (p : Fin 4 → ℕ) (hp : ∀ a, 0 < p a)
    (lo hi : Fin 4 → ℕ → ℝ)
    (hlo : ∀ a n, 1 ≤ n → n ≤ 2*p a → lo a n ≤ RestrictionSpectrum.moment (H a) n)
    (hhi : ∀ a n, 1 ≤ n → n ≤ 2*p a → RestrictionSpectrum.moment (H a) n ≤ hi a n)
    (hstop : ∀ a, hi a (p a) < 1) (η : ℝ)
    (hu : upper (hi 2) (p 2) + upper (hi 3) (p 3) -
      lower (lo 0) (p 0) - lower (lo 1) (p 1) ≤ -η) :
    ArithmeticLogTransfer.signedLog A ≤ -η :=
  (signed_four_interval A H c hc hA w p hp lo hi hlo hhi hstop).2.trans hu

end SplitZero.CertifiedTraceBounds
