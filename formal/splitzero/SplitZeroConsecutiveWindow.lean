import SplitZeroTodaVolume

noncomputable section
namespace SplitZero.ConsecutiveWindow
open scoped BigOperators

/-- Reorganize the source radius without dropping the phase. -/
theorem exact_step (P M Q w wnext z e : ℝ)
    (hP : P ≠ 0) (hM : M ≠ 0) (hQ : Q ≠ 0) (hw : w ≠ 0)
    (he : e ^ 2 = TodaVolume.energy (wnext / w) P M Q z) :
    (e ^ 2 + z ^ 2) * (w / M) =
      (wnext / Q) * (1 - M / P) * (1 - Q / M) := by
  rw [he]
  unfold TodaVolume.energy
  field_simp
  ring

/-- Derive a consecutive Lambda=omega/V bound from the original identity. -/
theorem radius_step (P M Q w wnext z e : ℝ)
    (hP : 0 < P) (hM : 0 < M) (hQ : 0 < Q)
    (hw : 0 < w) (hwn : 0 < wnext) (hQM : Q ≤ M)
    (he : e ^ 2 = TodaVolume.energy (wnext / w) P M Q z) :
    e ^ 2 * (w / M) ≤ wnext / Q := by
  have hy0 : 0 ≤ 1 - Q / M := sub_nonneg.mpr ((div_le_one hM).mpr hQM)
  have hx1 : 1 - M / P ≤ 1 := by have := div_nonneg hM.le hP.le; linarith
  have hy1 : 1 - Q / M ≤ 1 := by have := div_nonneg hQ.le hM.le; linarith
  have hk : 0 ≤ wnext / Q := div_nonneg hwn.le hQ.le
  have hab : (wnext / Q) * (1 - M / P) * (1 - Q / M) ≤ wnext / Q := by
    calc
      _ ≤ (wnext / Q) * 1 * (1 - Q / M) :=
        mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hx1 hk) hy0
      _ ≤ (wnext / Q) * 1 * 1 :=
        mul_le_mul_of_nonneg_left hy1 (by positivity)
      _ = _ := by ring
  have hex := exact_step P M Q w wnext z e (ne_of_gt hP) (ne_of_gt hM)
    (ne_of_gt hQ) (ne_of_gt hw) he
  have hphase : 0 ≤ z ^ 2 * (w / M) := by positivity
  nlinarith

end SplitZero.ConsecutiveWindow
