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

/-- Compose the actual radius sequence, common spectral lower bound and norm bound.
V 0, V 1, ... are the previous/current quotient volumes of a regular window.
The hypotheses keep the phase at every degree; Lambda is constructed as w/V.
-/
theorem canonical_norm_volume (V w e z : ℕ → ℝ) (L C : ℝ) (r : ℕ)
    (hV : ∀ j, 0 < V j) (hw : ∀ j, 0 < w j)
    (hmono : ∀ j, V (j+2) ≤ V (j+1))
    (hL : 0 ≤ L) (hLe : ∀ j, L ≤ e j)
    (henergy : ∀ j, e j ^ 2 =
      TodaVolume.energy (w (j+1) / w j) (V j) (V (j+1)) (V (j+2)) (z j))
    (hC : 0 < C) (hnorm : w r ≤ (C ^ 2) ^ r * w 0) :
    ((L / C) ^ 2) ^ r * V (r+1) ≤ V 1 := by
  have hstep (j : ℕ) : e j ^ 2 * (w j / V (j+1)) ≤ w (j+1) / V (j+2) :=
    radius_step (V j) (V (j+1)) (V (j+2)) (w j) (w (j+1)) (z j) (e j)
      (hV j) (hV (j+1)) (hV (j+2)) (hw j) (hw (j+1)) (hmono j) (henergy j)
  have hp := lower_bound_propagates e (fun j => w j / V (j+1)) L
    (fun j => div_nonneg (hw j).le (hV (j+1)).le) hL hLe hstep 0 r
  have hprop : (L ^ 2) ^ r * (w 0 / V 1) ≤ w r / V (r+1) := by
    simpa only [Nat.zero_add] using hp
  exact norm_bound_forces_volume L C (V 1) (V (r+1)) (w 0) (w r) r
    (hV 1) (hV (r+1)) (hw 0) hC hprop hnorm

end SplitZero.ConsecutiveWindow
