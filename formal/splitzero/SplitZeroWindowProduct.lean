import SplitZeroConsecutiveWindow

noncomputable section
namespace SplitZero.ConsecutiveWindow
open scoped BigOperators

/-- Both appearances of each interior contraction are retained. -/
theorem exact_product (f lam loss : ℕ → ℝ)
    (hlam : ∀ j, lam j ≠ 0)
    (hstep : ∀ j, f j * lam j = lam (j+1) * loss j * loss (j+1))
    (n r : ℕ) :
    (∏ j ∈ Finset.range (r+1), f (n+j)) * lam n =
      lam (n+r+1) * loss n * loss (n+r+1) *
        (∏ j ∈ Finset.range r, loss (n+j+1)) ^ 2 := by
  induction r with
  | zero => simpa using hstep n
  | succ r ih =>
    have hs := hstep (n+r+1)
    apply mul_right_cancel₀ (hlam (n+r+1))
    rw [Finset.prod_range_succ, Finset.prod_range_succ]
    have hi : n + (r + 1) = n+r+1 := by omega
    have hi2 : n + (r + 1) + 1 = n+r+1+1 := by omega
    simp only [hi, hi2]
    calc
      _ = ((∏ j ∈ Finset.range (r+1), f (n+j)) * lam n) *
          (f (n+r+1) * lam (n+r+1)) := by ring
      _ = (lam (n+r+1) * loss n * loss (n+r+1) *
          (∏ j ∈ Finset.range r, loss (n+j+1)) ^ 2) *
          (lam (n+r+1+1) * loss (n+r+1) * loss (n+r+1+1)) := by rw [ih, hs]
      _ = _ := by ring

/-- Propagate an upper bound in the unchanged norm-volume sequence. -/
theorem product_bound (f lam : ℕ → ℝ)
    (hf : ∀ j, 0 ≤ f j)
    (hstep : ∀ j, f j * lam j ≤ lam (j+1))
    (n r : ℕ) :
    (∏ j ∈ Finset.range r, f (n+j)) * lam n ≤ lam (n+r) := by
  induction r with
  | zero => simp
  | succ r ih =>
    rw [Finset.prod_range_succ]
    calc
      _ = f (n+r) * ((∏ j ∈ Finset.range r, f (n+j)) * lam n) := by ring
      _ ≤ f (n+r) * lam (n+r) := mul_le_mul_of_nonneg_left ih (hf _)
      _ ≤ lam (n+r+1) := hstep _
      _ = _ := by congr 1; omega

/-- The same proven spectral lower allowance persists at every degree. -/
theorem lower_bound_propagates (e lam : ℕ → ℝ) (L : ℝ)
    (hlam : ∀ j, 0 ≤ lam j) (hL : 0 ≤ L) (hLe : ∀ j, L ≤ e j)
    (hstep : ∀ j, e j ^ 2 * lam j ≤ lam (j+1))
    (n r : ℕ) :
    (L ^ 2) ^ r * lam n ≤ lam (n+r) := by
  have hs (j : ℕ) : L ^ 2 * lam j ≤ lam (j+1) := by
    have hsq : L ^ 2 ≤ e j ^ 2 := by nlinarith [hLe j]
    exact (mul_le_mul_of_nonneg_right hsq (hlam j)).trans (hstep j)
  simpa using product_bound (fun _ => L ^ 2) lam (fun _ => sq_nonneg L) hs n r

end SplitZero.ConsecutiveWindow
