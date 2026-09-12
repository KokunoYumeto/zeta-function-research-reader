import SplitZeroTodaVolume

/-!
# Selecting an admitted degree from endpoint volume data

The original consecutive quotient volumes and unscaled polynomial norms
are used throughout. Finite averaging is checked; an arithmetic budget
and the analytic Jensen argument in the handoff are not assumed proved.
-/
namespace SplitZero.VolumeWindow
open scoped BigOperators

/-- Finite averaging with the nonempty window hypothesis retained. -/
theorem exists_below_budget (f : ℕ → ℝ) (r : ℕ) (b : ℝ)
    (hr : 0 < r) (hb : (∑ j ∈ Finset.range r, f j) ≤ (r : ℝ) * b) :
    ∃ j < r, f j ≤ b := by
  by_contra! h
  have hs : (∑ j ∈ Finset.range r, b) < ∑ j ∈ Finset.range r, f j := by
    apply Finset.sum_lt_sum
    · intro j hj
      exact le_of_lt (h j (Finset.mem_range.mp hj))
    · exact ⟨0, Finset.mem_range.mpr hr, h 0 hr⟩
  have hc : (∑ j ∈ Finset.range r, b) = (r : ℝ) * b := by simp
  rw [hc] at hs
  exact (not_lt_of_ge hb) hs

/-- Only endpoint volumes are needed to select a small two-degree step. -/
theorem exists_log_step (V : ℕ → ℝ) (hV : ∀ n, 0 < V n)
    (r : ℕ) (b : ℝ) (hr : 0 < r)
    (hb : Real.log (V 0 / V (2*r)) ≤ (r : ℝ) * b) :
    ∃ j < r, Real.log (V (2*j) / V (2*j+2)) ≤ b := by
  apply exists_below_budget (fun j => Real.log (V (2*j) / V (2*j+2))) r b hr
  rw [SplitZero.TodaVolume.log_volume_telescope V hV r]
  exact hb

/-- The selected degree inherits any proved monotone local control function. -/
theorem exists_control_step (V e : ℕ → ℝ) (hV : ∀ n, 0 < V n)
    (r : ℕ) (b : ℝ) (hr : 0 < r)
    (hb : Real.log (V 0 / V (2*r)) ≤ (r : ℝ) * b)
    (Phi : ℝ → ℝ) (hPhi : Monotone Phi)
    (he : ∀ j < r, e j ≤ Phi (Real.log (V (2*j) / V (2*j+2)))) :
    ∃ j < r, e j ≤ Phi b := by
  obtain ⟨j, hj, hlog⟩ := exists_log_step V hV r b hr hb
  exact ⟨j, hj, (he j hj).trans (hPhi hlog)⟩

/-- The product of recurrence norm ratios retains only the original endpoints. -/
theorem norm_ratio_product (w : ℕ → ℝ) (hw : ∀ j, w j ≠ 0) (r : ℕ) :
    (∏ j ∈ Finset.range r, w (j + 1) / w j) = w r / w 0 := by
  induction r with
  | zero => simp [hw 0]
  | succ r ih =>
      rw [Finset.prod_range_succ, ih]
      calc
        (w r / w 0) * (w (r + 1) / w r) =
            (w r / w r) * (w (r + 1) / w 0) := by ring
        _ = w (r + 1) / w 0 := by rw [div_self (hw r), one_mul]

/-- Consecutive degree windows have four endpoint volumes, not two. -/
theorem overlapping_log_telescope (V : ℕ → ℝ) (hV : ∀ j, 0 < V j) (r : ℕ) :
    (∑ j ∈ Finset.range r, Real.log (V j / V (j + 2))) =
      Real.log ((V 0 * V 1) / (V r * V (r + 1))) := by
  have hs (j : ℕ) : Real.log (V j / V (j + 2)) =
      (Real.log (V j) - Real.log (V (j + 1))) +
      (Real.log (V (j + 1)) - Real.log (V (j + 2))) := by
    rw [Real.log_div (ne_of_gt (hV _)) (ne_of_gt (hV _))]
    ring
  simp_rw [hs]
  rw [Finset.sum_add_distrib]
  have h1 := SplitZero.TodaVolume.sum_differences (fun j => Real.log (V j)) r
  have h2 : (∑ j ∈ Finset.range r,
      (Real.log (V (j + 1)) - Real.log (V (j + 2)))) =
      Real.log (V 1) - Real.log (V (r + 1)) := by
    simpa [Nat.add_assoc] using
      SplitZero.TodaVolume.sum_differences (fun j => Real.log (V (j + 1))) r
  rw [h1, h2]
  rw [Real.log_div (mul_ne_zero (ne_of_gt (hV _)) (ne_of_gt (hV _)))
    (mul_ne_zero (ne_of_gt (hV _)) (ne_of_gt (hV _)))]
  rw [Real.log_mul (ne_of_gt (hV _)) (ne_of_gt (hV _)),
    Real.log_mul (ne_of_gt (hV _)) (ne_of_gt (hV _))]
  ring

end SplitZero.VolumeWindow
