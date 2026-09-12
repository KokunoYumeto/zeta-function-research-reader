import SplitZeroTraceCertificate
import SplitZeroTodaVolume

/-!
# Original-Gram trace certificate composed with source/boundary volume control

The trace allowance is derived using the integrated two-coordinate control
certificate. The analytic Toda radius identity is a separate, explicit input.
-/
noncomputable section
namespace SplitZero.TodaTrace
open Matrix
variable {n d : Type*} [Fintype n] [Fintype d] [DecidableEq n] [DecidableEq d]

/-- The aggregate invariant trace forces contraction of the original quotient volume. -/
theorem original_gram_volume
    (G : Matrix n n ℂ) (c : SplitZero.GramTrace.Coordinates G)
    (A : Matrix n n ℂ) (B : Matrix n d ℂ) (L : Matrix d n ℂ)
    (a : Matrix d d ℂ) (w e : ℝ)
    (U : Matrix n (Fin 2) ℂ) (V : Matrix (Fin 2) n ℂ)
    (he : 0 ≤ e) (hLB : L * B = 1) (hAB : A * B = B * a)
    (hP : (B * L).conjTranspose * G = G * (B * L))
    (hH : G * (U * V) = SplitZero.MetricRestriction.primal A G w)
    (ht : Matrix.trace (V * U) = 0) (hd : (V * U).det = -((e : ℂ) ^ 2))
    (alpha P M Q phase : ℝ)
    (halpha : 0 ≤ alpha) (hprev : 0 < P) (hnext : 0 < Q)
    (henergy : e ^ 2 = SplitZero.TodaVolume.energy alpha P M Q phase) :
    4 * P * Q * (2 * (Matrix.trace a).re - w * (Fintype.card d : ℝ)) ^ 2 ≤
      alpha * (P - Q) ^ 2 := by
  have hb := SplitZero.TraceCertificate.original_gram_bound G c A B L a w e U V
    he hLB hAB hP hH ht hd
  have hh := SplitZero.TodaVolume.lower_forces_volume alpha P M Q phase e
    |2 * (Matrix.trace a).re - w * (Fintype.card d : ℝ)|
    halpha hprev hnext (abs_nonneg _) hb henergy
  simpa only [sq_abs] using hh

end SplitZero.TodaTrace
