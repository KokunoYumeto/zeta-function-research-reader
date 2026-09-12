import SplitZeroGramTrace

/-!
# A single trace budget for an entire retained filtration

Orthogonal graded-piece projectors of a nested invariant filtration form the
resolution used here. Their arithmetic invariance and quotient actions are
kept in the caller; no arbitrary complement is asserted invariant.
The total absolute defect has budget 2e, not the number of pieces times e.
-/
noncomputable section
namespace SplitZero.TraceFiltration
open Matrix
open scoped BigOperators
variable {n ι : Type*} [Fintype n] [DecidableEq n] [Fintype ι]

/-- The overlap masses sum to the trace of the retained control direction. -/
theorem overlap_sum (Q : ι → Matrix n n ℂ) (F : Matrix n n ℂ)
    (hQ : (∑ i, Q i) = 1) :
    (∑ i, (Matrix.trace (Q i * F)).re) = (Matrix.trace F).re := by
  calc
    _ = (Matrix.trace ((∑ i, Q i) * F)).re := by
      simp only [Matrix.sum_mul, Matrix.trace_sum]
      exact (map_sum Complex.reAddGroupHom (fun i => Matrix.trace (Q i * F)) Finset.univ).symm
    _ = (Matrix.trace F).re := by rw [hQ, one_mul]

/-- Full absolute budget, retaining both signed overlap distributions. -/
theorem resolution_budget (Q : ι → Matrix n n ℂ) (Fplus Fminus : Matrix n n ℂ)
    (e : ℝ) (he : 0 ≤ e)
    (hQ : (∑ i, Q i) = 1)
    (hQQ : ∀ i, Q i * Q i = Q i) (hQs : ∀ i, (Q i).conjTranspose = Q i)
    (hp : Fplus * Fplus = Fplus) (hps : Fplus.conjTranspose = Fplus)
    (hm : Fminus * Fminus = Fminus) (hms : Fminus.conjTranspose = Fminus)
    (htp : (Matrix.trace Fplus).re = 1) (htm : (Matrix.trace Fminus).re = 1) :
    (∑ i, |(Matrix.trace (Q i * SplitZero.TraceProjection.signedControl e Fplus Fminus)).re|)
      ≤ 2 * e := by
  have hb (i : ι) :
      |(Matrix.trace (Q i * SplitZero.TraceProjection.signedControl e Fplus Fminus)).re| ≤
        e * ((Matrix.trace (Q i * Fplus)).re + (Matrix.trace (Q i * Fminus)).re) := by
    obtain ⟨hp0, _⟩ := SplitZero.TraceProjection.projection_overlap_bounds
      (Q i) Fplus (hQQ i) (hQs i) hp hps htp
    obtain ⟨hm0, _⟩ := SplitZero.TraceProjection.projection_overlap_bounds
      (Q i) Fminus (hQQ i) (hQs i) hm hms htm
    rw [SplitZero.TraceProjection.signed_trace_formula, abs_mul, abs_of_nonneg he]
    apply mul_le_mul_of_nonneg_left _ he
    exact abs_le.mpr ⟨by linarith, by linarith⟩
  calc
    _ ≤ ∑ i, e * ((Matrix.trace (Q i * Fplus)).re + (Matrix.trace (Q i * Fminus)).re) :=
      Finset.sum_le_sum (fun i _ => hb i)
    _ = e * ((∑ i, (Matrix.trace (Q i * Fplus)).re) +
        (∑ i, (Matrix.trace (Q i * Fminus)).re)) := by
      rw [← Finset.mul_sum, Finset.sum_add_distrib]
    _ = 2 * e := by rw [overlap_sum Q Fplus hQ, overlap_sum Q Fminus hQ, htp, htm]; ring

omit [Fintype ι] [DecidableEq n] in
/-- Two consecutive nested metric projections give an actual graded-piece projector. -/
theorem nested_difference (P Q : Matrix n n ℂ)
    (hP : P * P = P) (hQ : Q * Q = Q)
    (hPQ : P * Q = P) (hQP : Q * P = P)
    (hPs : P.conjTranspose = P) (hQs : Q.conjTranspose = Q) :
    (Q - P) * (Q - P) = Q - P ∧ (Q - P).conjTranspose = Q - P := by
  constructor
  · calc
      _ = Q * Q - Q * P - P * Q + P * P := by noncomm_ring
      _ = Q - P := by rw [hP, hQ, hPQ, hQP]; abel
  · rw [Matrix.conjTranspose_sub, hPs, hQs]

/-- Keep the actual isometry when applying the budget to the original Gram. -/
theorem gram_resolution_budget {G : Matrix n n ℂ}
    (c : SplitZero.GramTrace.Coordinates G)
    (Q : ι → Matrix n n ℂ) (Fplus Fminus : Matrix n n ℂ) (e : ℝ) (he : 0 ≤ e)
    (hQ : (∑ i, Q i) = 1)
    (hQQ : ∀ i, Q i * Q i = Q i)
    (hQs : ∀ i, (Q i).conjTranspose * G = G * Q i)
    (hp : Fplus * Fplus = Fplus) (hps : Fplus.conjTranspose * G = G * Fplus)
    (hm : Fminus * Fminus = Fminus) (hms : Fminus.conjTranspose * G = G * Fminus)
    (htp : (Matrix.trace Fplus).re = 1) (htm : (Matrix.trace Fminus).re = 1) :
    (∑ i, |(Matrix.trace (Q i * SplitZero.TraceProjection.signedControl e Fplus Fminus)).re|)
      ≤ 2 * e := by
  have hQ' : (∑ i, c.transport (Q i)) = 1 := by
    calc
      _ = c.transport (∑ i, Q i) := by
        simp only [SplitZero.GramTrace.Coordinates.transport, Matrix.mul_sum, Matrix.sum_mul]
      _ = 1 := by rw [hQ, c.transport_one]
  have h := resolution_budget (fun i => c.transport (Q i))
    (c.transport Fplus) (c.transport Fminus) e he hQ'
    (fun i => c.transport_projection (Q i) (hQQ i))
    (fun i => c.transport_selfadjoint (Q i) (hQs i))
    (c.transport_projection Fplus hp) (c.transport_selfadjoint Fplus hps)
    (c.transport_projection Fminus hm) (c.transport_selfadjoint Fminus hms)
    (by simpa using htp) (by simpa using htm)
  have hs : SplitZero.TraceProjection.signedControl e (c.transport Fplus) (c.transport Fminus) =
      c.transport (SplitZero.TraceProjection.signedControl e Fplus Fminus) := by
    simp only [SplitZero.TraceProjection.signedControl, c.transport_smul, c.transport_sub]
  rw [hs] at h
  simpa only [c.transport_pair_trace] using h

end SplitZero.TraceFiltration
