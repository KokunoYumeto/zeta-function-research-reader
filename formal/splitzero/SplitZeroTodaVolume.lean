import Mathlib

/-!
# Exact adjacent-volume control, with both discarded squares retained

P, M, Q are the original positive quotient volumes at three consecutive
polynomial degrees. The analytic identification of the control radius with
`energy` is an input; no asymptotic estimate is assumed or manufactured.
-/
noncomputable section
namespace SplitZero.TodaVolume
open scoped BigOperators

def energy (a P M Q z : ℝ) : ℝ :=
  a * (1 - M / P) * (M / Q - 1) - z ^ 2

/-- Rational form of the two-loss identity; no logarithm or tilt is suppressed. -/
theorem two_losses (a P M Q z : ℝ) (hP : P ≠ 0) (hQ : Q ≠ 0) :
    energy a P M Q z =
      a * (P - Q) ^ 2 / (4 * P * Q) -
      a * (2 * M - P - Q) ^ 2 / (4 * P * Q) - z ^ 2 := by
  unfold energy
  field_simp
  ring

/-- The source control is bounded by the full two-step volume ratio. -/
theorem square_bound (a P M Q z e : ℝ)
    (ha : 0 ≤ a) (hP : 0 < P) (hQ : 0 < Q)
    (he : e ^ 2 = energy a P M Q z) :
    e ^ 2 ≤ a * (P - Q) ^ 2 / (4 * P * Q) := by
  rw [he, two_losses a P M Q z (ne_of_gt hP) (ne_of_gt hQ)]
  have hm : 0 ≤ a * (2 * M - P - Q) ^ 2 / (4 * P * Q) :=
    div_nonneg (mul_nonneg ha (sq_nonneg _)) (by positivity)
  nlinarith [sq_nonneg z]

/-- The upper estimate in the source note, in original volume coordinates. -/
theorem radius_bound (a P M Q z e : ℝ)
    (ha : 0 ≤ a) (hP : 0 < P) (hQ : 0 < Q) (hQP : Q ≤ P)
    (_he0 : 0 ≤ e) (he : e ^ 2 = energy a P M Q z) :
    e ≤ Real.sqrt a * (P - Q) / (2 * Real.sqrt (P * Q)) := by
  have hb := square_bound a P M Q z e ha hP hQ he
  have hpq : 0 < P * Q := mul_pos hP hQ
  let b := Real.sqrt a * (P - Q) / (2 * Real.sqrt (P * Q))
  have hb0 : 0 ≤ b := by dsimp [b]; positivity
  have hb2 : b ^ 2 = a * (P - Q) ^ 2 / (4 * P * Q) := by
    dsimp [b]
    simp only [div_pow, mul_pow, Real.sq_sqrt ha, Real.sq_sqrt hpq.le]
    norm_num
    ring
  change e ≤ b
  nlinarith

/-- Every established spectral lower allowance constrains the actual volumes. -/
theorem lower_forces_volume (a P M Q z e L : ℝ)
    (ha : 0 ≤ a) (hP : 0 < P) (hQ : 0 < Q)
    (hL : 0 ≤ L) (hLe : L ≤ e)
    (he : e ^ 2 = energy a P M Q z) :
    4 * P * Q * L ^ 2 ≤ a * (P - Q) ^ 2 := by
  have hb := square_bound a P M Q z e ha hP hQ he
  have hsq : L ^ 2 ≤ e ^ 2 := by nlinarith
  have hden : 0 < 4 * P * Q := by positivity
  have hh : L ^ 2 ≤ a * (P - Q) ^ 2 / (4 * P * Q) := hsq.trans hb
  have hc := (le_div_iff₀ hden).mp hh
  nlinarith

/-- Exact characterization of the two terms lost by the coarse bound. -/
theorem upper_equality_iff (a P M Q z : ℝ)
    (ha : 0 < a) (hP : 0 < P) (hQ : 0 < Q) :
    energy a P M Q z = a * (P - Q) ^ 2 / (4 * P * Q) ↔
      2 * M = P + Q ∧ z = 0 := by
  rw [two_losses a P M Q z (ne_of_gt hP) (ne_of_gt hQ)]
  have hd : 0 < 4 * P * Q := by positivity
  have ht : 0 ≤ a * (2 * M - P - Q) ^ 2 / (4 * P * Q) := by positivity
  constructor
  · intro h
    have hz2 : z ^ 2 = 0 := by nlinarith [sq_nonneg z]
    have ht0 : a * (2 * M - P - Q) ^ 2 / (4 * P * Q) = 0 := by
      nlinarith
    have hp0 := (div_eq_zero_iff).mp ht0
    have hs : (2 * M - P - Q) ^ 2 = 0 := by
      rcases hp0 with hp | hp
      · exact (mul_eq_zero.mp hp).resolve_left (ne_of_gt ha)
      · exact False.elim ((ne_of_gt hd) hp)
    constructor <;> nlinarith
  · rintro ⟨hm, rfl⟩
    have hzero : 2 * M - P - Q = 0 := by linarith
    rw [hzero]
    simp

/-- The first admissible degree has its own input, not a singular previous inverse. -/
theorem endpoint_square_bound (nu wnext wprev z e : ℝ)
    (hw : 0 < wprev)
    (he : e ^ 2 = (nu - wnext) / wprev - z ^ 2) :
    wprev * e ^ 2 ≤ nu - wnext := by
  have h : e ^ 2 ≤ (nu - wnext) / wprev := by rw [he]; nlinarith [sq_nonneg z]
  have := (le_div_iff₀ hw).mp h
  nlinarith

theorem sum_differences (f : ℕ → ℝ) (r : ℕ) :
    (∑ j ∈ Finset.range r, (f j - f (j + 1))) = f 0 - f r := by
  induction r with
  | zero => simp
  | succ r ih => rw [Finset.sum_range_succ, ih]; ring

/-- Literal telescoping over disjoint two-degree steps. -/
theorem log_volume_telescope (V : ℕ → ℝ) (hV : ∀ n, 0 < V n) (r : ℕ) :
    (∑ j ∈ Finset.range r, Real.log (V (2*j) / V (2*j+2))) =
      Real.log (V 0 / V (2*r)) := by
  have hlog (j : ℕ) : Real.log (V (2*j) / V (2*j+2)) =
      Real.log (V (2*j)) - Real.log (V (2*j+2)) :=
    Real.log_div (ne_of_gt (hV _)) (ne_of_gt (hV _))
  simp_rw [hlog]
  rw [Real.log_div (ne_of_gt (hV _)) (ne_of_gt (hV _))]
  convert sum_differences (fun j => Real.log (V (2*j))) r using 1
  simp [Nat.mul_add]

/-- A common rescaling of the same quotient volumes cancels explicitly. -/
theorem mass_scaling (a P M Q z c : ℝ) (hc : c ≠ 0) :
    energy a (c*P) (c*M) (c*Q) z = energy a P M Q z := by
  simp only [energy, mul_div_mul_left _ _ hc]

end SplitZero.TodaVolume
