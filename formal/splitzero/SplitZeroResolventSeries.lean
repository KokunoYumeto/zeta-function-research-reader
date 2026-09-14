import Mathlib

/-!
# Finite source resolvents, with a fixed-pair convergence certificate

Finite algebra and spectral estimates in ISM28--ISM34 and the fixed-pair
stopping step of ISM37. No uniformity over changing arithmetic packets or
tensor orders is asserted. The constant term and the last power are retained.
-/
noncomputable section
namespace SplitZero.ResolventSeries
open scoped BigOperators
open Filter

section Ring
variable {A : Type*} [Ring A]

def partialSum (H T : A) (L : ℕ) : A :=
  (∑ r ∈ Finset.range (L + 1), H ^ r) * T

theorem geometric_right (H : A) (n : ℕ) :
    (∑ r ∈ Finset.range n, H ^ r) * (1 - H) = 1 - H ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, add_mul, ih, mul_sub, mul_one, ← pow_succ]
    noncomm_ring

/-- No commutation with the observable is required. -/
theorem residual_exact (H T X : A) (L : ℕ) (hX : (1 - H) * X = T) :
    X - partialSum H T L = H ^ (L + 1) * X := by
  rw [partialSum, ← hX, ← mul_assoc, geometric_right]
  noncomm_ring

theorem partialSum_zero (T : A) (L : ℕ) : partialSum 0 T L = T := by
  have h := residual_exact (0 : A) T T L (by simp)
  have hz : T - partialSum 0 T L = 0 := by simpa using h
  exact (sub_eq_zero.mp hz).symm
end Ring

section Scalar
def blend (b x : ℝ) : ℝ := 1 - x + x * b

theorem blend_lower (b x : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) :
    min 1 b ≤ blend b x := by
  by_cases hb : b ≤ 1
  · rw [min_eq_right hb]
    unfold blend
    nlinarith [mul_nonneg (sub_nonneg.mpr hx1) (sub_nonneg.mpr hb)]
  · have hb' : 1 ≤ b := le_of_lt (lt_of_not_ge hb)
    rw [min_eq_left hb']
    unfold blend
    nlinarith [mul_nonneg hx0 (sub_nonneg.mpr hb')]

theorem blend_pos (b x : ℝ) (hb : 0 < b) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) :
    0 < blend b x := lt_of_lt_of_le (lt_min zero_lt_one hb) (blend_lower b x hx0 hx1)

theorem blend_mono (b c x : ℝ) (hbc : b ≤ c) (hx : 0 ≤ x) :
    blend b x ≤ blend c x := by
  unfold blend
  nlinarith [mul_nonneg hx (sub_nonneg.mpr hbc)]

theorem tangent_bound (b x : ℝ) (hb : 0 < b) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) :
    |(b - 1) / blend b x| ≤ |b - 1| / min 1 b := by
  rw [abs_div, abs_of_pos (blend_pos b x hb hx0 hx1)]
  exact div_le_div_of_nonneg_left (abs_nonneg _) (lt_min zero_lt_one hb)
    (blend_lower b x hx0 hx1)

theorem midpoint_deviation (lo hi t : ℝ) (hlo : 0 < lo)
    (hlt : lo ≤ t) (hth : t ≤ hi) :
    |1 - 2 * t / (lo + hi)| ≤ (hi - lo) / (lo + hi) := by
  have hs : 0 < lo + hi := by linarith
  have he : 1 - 2 * t / (lo + hi) = (lo + hi - 2 * t) / (lo + hi) := by
    field_simp
  rw [he, abs_div, abs_of_pos hs]
  apply div_le_div_of_nonneg_right _ hs.le
  exact abs_le.mpr ⟨by linarith, by linarith⟩

/-- Uniformity is only on x in [0,1] for this fixed positive endpoint pair. -/
theorem blend_contraction (lo hi b x : ℝ) (hlo : 0 < lo)
    (hlb : lo ≤ b) (hbh : b ≤ hi) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) :
    |1 - 2 * blend b x / (blend lo x + blend hi x)| ≤ (hi - lo) / (lo + hi) := by
  have hlh : lo ≤ hi := hlb.trans hbh
  have hh : 0 < hi := lt_of_lt_of_le hlo hlh
  have hlx := blend_pos lo x hlo hx0 hx1
  have hhx := blend_pos hi x hh hx0 hx1
  apply (midpoint_deviation _ _ _ hlx (blend_mono lo b x hlb hx0)
    (blend_mono b hi x hbh hx0)).trans
  apply (div_le_div_iff₀ (by linarith : 0 < blend lo x + blend hi x)
    (by linarith : 0 < lo + hi)).mpr
  unfold blend
  nlinarith [mul_nonneg (sub_nonneg.mpr hx1) (sub_nonneg.mpr hlh)]

theorem contraction_range (lo hi : ℝ) (hlo : 0 < lo) (hlh : lo ≤ hi) :
    0 ≤ (hi - lo) / (lo + hi) ∧ (hi - lo) / (lo + hi) < 1 := by
  have hs : 0 < lo + hi := by linarith
  constructor
  · exact div_nonneg (sub_nonneg.mpr hlh) hs.le
  · apply (div_lt_one hs).mpr
    linarith
end Scalar

section Spectrum
variable {ι : Type*} [Fintype ι] [Nonempty ι]

def mean (f : ι → ℝ) : ℝ := (∑ i, f i) / (Fintype.card ι : ℝ)
def variance (f : ι → ℝ) : ℝ := ∑ i, (f i - mean f) ^ 2

theorem centered_sum (f : ι → ℝ) : ∑ i, (f i - mean f) = 0 := by
  have hn : (Fintype.card ι : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
  simp only [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  unfold mean
  field_simp
  ring

/-- The exact centered energy retains the subtracted mean-square term. -/
theorem variance_formula (f : ι → ℝ) :
    variance f = (∑ i, f i ^ 2) - (∑ i, f i) ^ 2 / (Fintype.card ι : ℝ) := by
  have hn : (Fintype.card ι : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
  have he : variance f = (∑ i, f i ^ 2) - 2 * (∑ i, f i) * mean f +
      (Fintype.card ι : ℝ) * (mean f) ^ 2 := by
    unfold variance
    simp only [sub_sq, Finset.sum_add_distrib, Finset.sum_sub_distrib,
      Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    rw [← Finset.sum_mul, ← Finset.mul_sum]
  rw [he]
  unfold mean
  field_simp
  ring

omit [Nonempty ι] in
theorem variance_nonneg (f : ι → ℝ) : 0 ≤ variance f :=
  Finset.sum_nonneg fun _ _ => sq_nonneg _

theorem variance_le_energy (f : ι → ℝ) : variance f ≤ ∑ i, f i ^ 2 := by
  rw [variance_formula]
  have hd : 0 ≤ (∑ i, f i) ^ 2 / (Fintype.card ι : ℝ) := by positivity
  linarith

def residualSpectrum (h g : ι → ℝ) (L : ℕ) : ι → ℝ :=
  fun i => h i ^ (L + 1) * g i

theorem residual_variance_bound (h g a : ι → ℝ) (θ : ℝ) (hθ : 0 ≤ θ)
    (hh : ∀ i, |h i| ≤ θ) (hg : ∀ i, |g i| ≤ a i) (L : ℕ) :
    variance (residualSpectrum h g L) ≤ (θ ^ (L + 1)) ^ 2 * ∑ i, a i ^ 2 := by
  apply (variance_le_energy _).trans
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i _hi
  have ha : 0 ≤ a i := (abs_nonneg _).trans (hg i)
  have hp : |h i ^ (L + 1)| ≤ θ ^ (L + 1) := by
    rw [abs_pow]
    exact pow_le_pow_left₀ (abs_nonneg _) (hh i) _
  have hm : |h i ^ (L + 1) * g i| ≤ θ ^ (L + 1) * a i := by
    rw [abs_mul]
    exact mul_le_mul hp (hg i) (abs_nonneg _) (pow_nonneg hθ _)
  have hs := (sq_le_sq₀ (abs_nonneg (h i ^ (L + 1) * g i))
    (mul_nonneg (pow_nonneg hθ _) ha)).mpr hm
  simpa only [sq_abs, mul_pow, residualSpectrum] using hs

def radius (θ K Z : ℝ) (L : ℕ) : ℝ := θ ^ (L + 1) * Real.sqrt (K * Z)

theorem radius_tendsto_zero (θ K Z : ℝ) (hθ0 : 0 ≤ θ) (hθ1 : θ < 1) :
    Tendsto (radius θ K Z) atTop (nhds 0) := by
  change Tendsto (fun L : ℕ => θ ^ (L + 1) * Real.sqrt (K * Z)) atTop (nhds 0)
  have hp := (tendsto_pow_atTop_nhds_zero_of_lt_one hθ0 hθ1).mul_const
    (θ * Real.sqrt (K * Z))
  simpa only [pow_succ, mul_assoc, zero_mul] using hp

theorem exists_stopping_degree (θ K Z ε : ℝ) (hθ0 : 0 ≤ θ) (hθ1 : θ < 1)
    (hε : 0 < ε) : ∃ L : ℕ, radius θ K Z L < ε := by
  have he : ∀ᶠ L in atTop, radius θ K Z L < ε :=
    (tendsto_order.1 (radius_tendsto_zero θ K Z hθ0 hθ1)).2 ε hε
  exact he.exists
end Spectrum
end SplitZero.ResolventSeries
