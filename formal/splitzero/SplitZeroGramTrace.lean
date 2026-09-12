import SplitZeroTraceProjection
import SplitZeroMetricRestriction

/-!
# Trace control in the original Gram coordinates

The coordinate factor is an explicit isometry of G, not another chosen metric.
The arithmetic inclusion B and extraction L are transported with the action.
An oblique spectral projector is never treated as an orthogonal projector.
Existence of an isometric coordinate factor and of the two control spectral
projections is a separate spectral-theorem input to the finite interface.
-/
noncomputable section
namespace SplitZero.GramTrace
open Matrix
variable {n : Type*} [Fintype n] [DecidableEq n]

structure Coordinates (G : Matrix n n ℂ) where
  forward : Matrix n n ℂ
  inverse : Matrix n n ℂ
  left_inverse : inverse * forward = 1
  right_inverse : forward * inverse = 1
  gram : forward.conjTranspose * forward = G

namespace Coordinates
variable {G : Matrix n n ℂ} (c : Coordinates G)

def transport (M : Matrix n n ℂ) : Matrix n n ℂ :=
  c.forward * M * c.inverse

theorem transport_mul (M N : Matrix n n ℂ) :
    c.transport (M * N) = c.transport M * c.transport N := by
  unfold transport
  calc
    _ = c.forward * M * (c.inverse * c.forward) * N * c.inverse := by
      rw [c.left_inverse, mul_one]; simp only [Matrix.mul_assoc]
    _ = _ := by simp only [Matrix.mul_assoc]

@[simp] theorem transport_one : c.transport 1 = 1 := by
  simp only [transport, mul_one, c.right_inverse]

@[simp] theorem transport_add (M N : Matrix n n ℂ) :
    c.transport (M + N) = c.transport M + c.transport N := by
  simp only [transport, mul_add, add_mul]

@[simp] theorem transport_sub (M N : Matrix n n ℂ) :
    c.transport (M - N) = c.transport M - c.transport N := by
  simp only [transport, mul_sub, sub_mul]

@[simp] theorem transport_smul (z : ℂ) (M : Matrix n n ℂ) :
    c.transport (z • M) = z • c.transport M := by
  simp only [transport, Matrix.mul_smul, Matrix.smul_mul]

@[simp] theorem transport_trace (M : Matrix n n ℂ) :
    Matrix.trace (c.transport M) = Matrix.trace M := by
  unfold transport
  rw [Matrix.trace_mul_cycle, c.left_inverse, one_mul]

theorem inverse_star_gram : c.inverse.conjTranspose * G = c.forward := by
  rw [← c.gram, ← Matrix.mul_assoc, ← Matrix.conjTranspose_mul,
    c.right_inverse, Matrix.conjTranspose_one, one_mul]

theorem gram_inverse : G * c.inverse = c.forward.conjTranspose := by
  rw [← c.gram, Matrix.mul_assoc, c.right_inverse, mul_one]

theorem congruence_left (M : Matrix n n ℂ) :
    c.inverse.conjTranspose * (G * M) * c.inverse = c.transport M := by
  rw [← Matrix.mul_assoc, c.inverse_star_gram]
  rfl

theorem congruence_right (M : Matrix n n ℂ) :
    c.inverse.conjTranspose * (M.conjTranspose * G) * c.inverse =
      (c.transport M).conjTranspose := by
  calc
    _ = c.inverse.conjTranspose * M.conjTranspose * (G * c.inverse) := by
      simp only [Matrix.mul_assoc]
    _ = c.inverse.conjTranspose * M.conjTranspose * c.forward.conjTranspose := by
      rw [c.gram_inverse]
    _ = _ := by simp only [transport, Matrix.conjTranspose_mul, Matrix.mul_assoc]

theorem congruence_gram : c.inverse.conjTranspose * G * c.inverse = 1 := by
  rw [c.inverse_star_gram, c.right_inverse]

/-- G-self-adjointness transports along this same isometry. -/
theorem transport_selfadjoint (M : Matrix n n ℂ)
    (hM : M.conjTranspose * G = G * M) :
    (c.transport M).conjTranspose = c.transport M := by
  rw [← c.congruence_right, hM, c.congruence_left]

theorem transport_projection (P : Matrix n n ℂ) (hP : P * P = P) :
    c.transport P * c.transport P = c.transport P := by
  rw [← c.transport_mul, hP]

/-- The original weighted control, not a replacement action. -/
theorem control_transfer (A H : Matrix n n ℂ) (w : ℝ)
    (hGH : G * H = SplitZero.MetricRestriction.primal A G w) :
    c.transport H = (c.transport A).conjTranspose + c.transport A - (w : ℂ) • 1 := by
  rw [← c.congruence_left H, hGH]
  simp only [SplitZero.MetricRestriction.primal, mul_add, add_mul, mul_sub,
    sub_mul, Matrix.mul_smul, Matrix.smul_mul]
  rw [c.congruence_right, c.congruence_left, c.congruence_gram]

/-- Isometric transport does not change a compression trace. -/
theorem transport_pair_trace (P H : Matrix n n ℂ) :
    Matrix.trace (c.transport P * c.transport H) = Matrix.trace (P * H) := by
  rw [← c.transport_mul, c.transport_trace]

/-- Full invariant-subspace trace bound in G with the original inclusion attached. -/
theorem invariant_excess_bound {d : Type*} [Fintype d] [DecidableEq d]
    (A H : Matrix n n ℂ) (B : Matrix n d ℂ) (L : Matrix d n ℂ)
    (a : Matrix d d ℂ) (w e : ℝ) (Fplus Fminus : Matrix n n ℂ)
    (hLB : L * B = 1) (hAB : A * B = B * a)
    (hP : (B * L).conjTranspose * G = G * (B * L)) (he : 0 ≤ e)
    (hp : Fplus * Fplus = Fplus)
    (hps : Fplus.conjTranspose * G = G * Fplus)
    (hm : Fminus * Fminus = Fminus)
    (hms : Fminus.conjTranspose * G = G * Fminus)
    (htp : (Matrix.trace Fplus).re = 1) (htm : (Matrix.trace Fminus).re = 1)
    (hGH : G * H = SplitZero.MetricRestriction.primal A G w)
    (hH : H = SplitZero.TraceProjection.signedControl e Fplus Fminus) :
    |2 * (Matrix.trace a).re - w * (Fintype.card d : ℝ)| ≤ e := by
  have hLB' : (L * c.inverse) * (c.forward * B) = 1 := by
    calc
      _ = L * (c.inverse * c.forward) * B := by simp only [Matrix.mul_assoc]
      _ = 1 := by rw [c.left_inverse, mul_one, hLB]
  have hAB' : c.transport A * (c.forward * B) = (c.forward * B) * a := by
    calc
      _ = c.forward * A * (c.inverse * c.forward) * B := by
        simp only [transport, Matrix.mul_assoc]
      _ = c.forward * (A * B) := by
        rw [c.left_inverse, mul_one]; simp only [Matrix.mul_assoc]
      _ = _ := by rw [hAB, Matrix.mul_assoc]
  have hP' : ((c.forward * B) * (L * c.inverse)).conjTranspose =
      (c.forward * B) * (L * c.inverse) := by
    have hh := c.transport_selfadjoint (B * L) hP
    simpa only [transport, Matrix.mul_assoc] using hh
  have hH' : (c.transport A).conjTranspose + c.transport A - (w : ℂ) • 1 =
      SplitZero.TraceProjection.signedControl e (c.transport Fplus) (c.transport Fminus) := by
    rw [← c.control_transfer A H w hGH, hH]
    simp only [SplitZero.TraceProjection.signedControl, c.transport_smul, c.transport_sub]
  exact SplitZero.TraceProjection.invariant_excess_bound
    (c.transport A) (c.forward * B) (L * c.inverse) a w e
    (c.transport Fplus) (c.transport Fminus) hLB' hAB' hP' he
    (c.transport_projection Fplus hp) (c.transport_selfadjoint Fplus hps)
    (c.transport_projection Fminus hm) (c.transport_selfadjoint Fminus hms)
    (by simpa using htp) (by simpa using htm) hH'

end Coordinates
end SplitZero.GramTrace
