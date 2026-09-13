import SplitZeroWindowProduct

noncomputable section
namespace SplitZero.ConsecutiveWindow

/-- The separate first-degree input never uses a preceding singular inverse. -/
theorem first_radius_step (nu M Q w wnext z e : ℝ)
    (hM : 0 < M) (hQ : 0 < Q) (hw : 0 < w) (hwn : 0 ≤ wnext)
    (htransition : nu * Q = wnext * M)
    (he : e ^ 2 = (nu - wnext) / w - z ^ 2) :
    e ^ 2 * (w / M) ≤ wnext / Q := by
  have hb := TodaVolume.endpoint_square_bound nu wnext w z e hw he
  have htop : e ^ 2 * w ≤ nu := by nlinarith
  have hdiv := (div_le_div_iff_of_pos_right hM).mpr htop
  have hid : nu / M = wnext / Q := by
    apply (div_eq_div_iff (ne_of_gt hM) (ne_of_gt hQ)).mpr
    exact htransition
  calc
    _ = (e ^ 2 * w) / M := by ring
    _ ≤ nu / M := hdiv
    _ = _ := hid

/-- Compose a norm-window upper bound with the propagated spectral lower bound. -/
theorem norm_bound_forces_volume (L C vstart vend wstart wend : ℝ) (r : ℕ)
    (hv : 0 < vstart) (hvend : 0 < vend) (hw : 0 < wstart) (hC : 0 < C)
    (hprop : (L ^ 2) ^ r * (wstart / vstart) ≤ wend / vend)
    (hnorm : wend ≤ (C ^ 2) ^ r * wstart) :
    ((L / C) ^ 2) ^ r * vend ≤ vstart := by
  have h1 := (le_div_iff₀ hvend).mp hprop
  have h3 : (L ^ 2) ^ r * wstart * vend ≤ wend * vstart := by
    have ht := mul_le_mul_of_nonneg_right h1 hv.le
    field_simp at ht
    nlinarith
  have h4 := mul_le_mul_of_nonneg_right hnorm hv.le
  have h5 : (L ^ 2) ^ r * vend ≤ (C ^ 2) ^ r * vstart := by
    nlinarith
  have hd : 0 < (C ^ 2) ^ r := by positivity
  have hh := (div_le_iff₀ hd).mpr h5
  simpa only [div_pow, mul_div_assoc, div_mul_eq_mul_div] using hh

/-- Convert the positive-endpoint power inequality to its logarithmic budget. -/
theorem log_volume_forcing (t vstart vend : ℝ) (r : ℕ)
    (ht : 0 < t) (hvs : 0 < vstart) (hve : 0 < vend)
    (h : (t ^ 2) ^ r * vend ≤ vstart) :
    2 * (r : ℝ) * Real.log t ≤ Real.log (vstart / vend) := by
  have hp : 0 < (t ^ 2) ^ r * vend := by positivity
  have hlog := Real.log_le_log hp h
  rw [Real.log_mul (by positivity) (ne_of_gt hve), Real.log_pow, Real.log_pow] at hlog
  rw [Real.log_div (ne_of_gt hvs) (ne_of_gt hve)]
  nlinarith

end SplitZero.ConsecutiveWindow
