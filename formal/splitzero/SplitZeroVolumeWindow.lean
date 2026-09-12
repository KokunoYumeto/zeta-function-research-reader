import SplitZeroTodaVolume

/-!
# Selecting an admitted degree from a volume budget

A total logarithmic volume budget yields one small adjacent contraction.
It does not assert that the budget or a recurrence estimate holds for the
arithmetic source. The index selected remains in the supplied degree window.
-/
namespace SplitZero.VolumeWindow
open scoped BigOperators

/-- Finite averaging with the nonempty window hypothesis retained. -/
theorem exists_below_budget (f : ℕ → ℝ) (r : ℕ) (b : ℝ)
    (hr : 0 < r) (hb : (∑ j ∈ Finset.range r, f j) ≤ (r : ℝ) * b) :
    ∃ j < r, f j ≤ b := by
  by_contra! h
  have hs : (∑ j ∈ Finset.range r, b) < ∑ j ∈ Finset.range r, f j := by
    apply Finset.sum_lt_sum_of_nonempty (Finset.nonempty_range_iff.mpr (Nat.ne_of_gt hr))
    intro j hj
    exact h j (Finset.mem_range.mp hj)
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

end SplitZero.VolumeWindow
