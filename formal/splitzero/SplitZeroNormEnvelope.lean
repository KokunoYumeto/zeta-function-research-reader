import SplitZeroWindowForcing

noncomputable section
namespace SplitZero.ConsecutiveWindow

/-- The analytic upper and lower monic norm envelopes imply the doubling estimate. -/
theorem doubling_from_envelope (lo up wn w2n : ℝ) (n : ℕ)
    (hlo : 0 < lo) (_hup : 0 ≤ up)
    (hlower : (lo * (n : ℝ)) ^ (2*n) ≤ wn)
    (hupper : w2n ≤ (up * (2*(n : ℝ))) ^ (4*n)) :
    w2n ≤ ((4 * up ^ 2 / lo) * (n : ℝ)) ^ (2*n) * wn := by
  have hbase : ((4 * up ^ 2 / lo) * (n : ℝ)) * (lo * (n : ℝ)) =
      (up * (2*(n : ℝ))) ^ 2 := by
    field_simp
    ring
  have hid : (up * (2*(n : ℝ))) ^ (4*n) =
      ((4 * up ^ 2 / lo) * (n : ℝ)) ^ (2*n) *
        (lo * (n : ℝ)) ^ (2*n) := by
    rw [← mul_pow, hbase, ← pow_mul]
    congr 1
    omega
  calc
    w2n ≤ (up * (2*(n : ℝ))) ^ (4*n) := hupper
    _ = _ := hid
    _ ≤ _ := mul_le_mul_of_nonneg_left hlower (by positivity)

end SplitZero.ConsecutiveWindow
