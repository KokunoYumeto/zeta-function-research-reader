import Mathlib

/-!
Finite log-volume certificates for the actual restriction-loss eigenvalues.
The scalar logarithm series is proved in Mathlib; no power-series identity,
positive spectral gap, or desired upper volume estimate is postulated here.
The adaptive certificate uses only trace powers and rational operations.
-/
noncomputable section
namespace SplitZero.RestrictionLog
open scoped BigOperators
open Filter

 def term (x : ℝ) (n : ℕ) : ℝ := x ^ (n+1) / ((n : ℝ)+1)
 def prefix (x : ℝ) (p : ℕ) : ℝ := ∑ n ∈ Finset.range p, term x n
 def remainder (x : ℝ) (p : ℕ) : ℝ := -Real.log (1-x) - prefix x p

 theorem hasSum_remainder (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1) (p : ℕ) :
    HasSum (fun n : ℕ => term x (n+p)) (remainder x p) := by
  have hs := Real.hasSum_pow_div_log_of_abs_lt_one (by rwa [abs_of_nonneg hx0])
  exact (hasSum_nat_add_iff' p).2 hs

 theorem remainder_nonneg (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1) (p : ℕ) :
    0 ≤ remainder x p :=
  (hasSum_remainder x hx0 hx1 p).nonneg (fun n => by unfold term; positivity)

/-- The full remaining series after another block is controlled by x^p. -/
 theorem double_remainder_le (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1) (p : ℕ) :
    remainder x (2*p) ≤ x^p * remainder x p := by
  apply hasSum_le _ (hasSum_remainder x hx0 hx1 (2*p))
    ((hasSum_remainder x hx0 hx1 p).mul_left (x^p))
  intro n
  unfold term
  have hd0 : (0 : ℝ) < ((n+p : ℕ) : ℝ)+1 := by positivity
  have hd : ((n+p : ℕ) : ℝ)+1 ≤ ((n+2*p : ℕ) : ℝ)+1 := by
    push_cast
    linarith [show (0 : ℝ) ≤ p by positivity]
  calc
    _ ≤ x^(n+2*p+1) / (((n+p : ℕ) : ℝ)+1) :=
      div_le_div_of_nonneg_left (pow_nonneg hx0 _) hd0 hd
    _ = _ := by
      rw [show n+2*p+1 = p+(n+p+1) by omega, pow_add]
      ring

/-- The source's sharp coefficient c_p(r), with r>0 and all zero x cases retained. -/
 theorem sharp_remainder_le (x r : ℝ) (hx0 : 0 ≤ x) (hxr : x ≤ r)
    (hr0 : 0 < r) (hr1 : r < 1) (p : ℕ) :
    remainder x p ≤ (remainder r p / r^(p+1)) * x^(p+1) := by
  have hx1 := lt_of_le_of_lt hxr hr1
  have hm : remainder x p * r^(p+1) ≤ remainder r p * x^(p+1) := by
    apply hasSum_le _ ((hasSum_remainder x hx0 hx1 p).mul_right (r^(p+1)))
      ((hasSum_remainder r hr0.le hr1 p).mul_right (x^(p+1)))
    intro n
    have hp : x^n ≤ r^n := pow_le_pow_left₀ hx0 hxr n
    have ht := mul_le_mul_of_nonneg_right hp
      (mul_nonneg (pow_nonneg hx0 (p+1)) (pow_nonneg hr0.le (p+1)))
    have hd : (0 : ℝ) < ((n+p : ℕ) : ℝ)+1 := by positivity
    have hh := div_le_div_of_nonneg_right ht hd.le
    simpa only [term, show n+p+1 = n+(p+1) by omega, pow_add,
      mul_div_assoc, div_mul_eq_mul_div, mul_assoc, mul_left_comm, mul_comm] using hh
  have hd : 0 < r^(p+1) := pow_pos hr0 _
  have hh := (le_div_iff₀ hd).mpr hm
  simpa only [div_mul_eq_mul_div] using hh

/-- A rational certificate with no externally supplied spectral gap. -/
 theorem adaptive_scalar (x s : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1)
    (p : ℕ) (hxs : x^p ≤ s) (hs : s < 1) :
    -Real.log (1-x) ≤ prefix x p + (prefix x (2*p)-prefix x p)/(1-s) := by
  have hr := remainder_nonneg x hx0 hx1 p
  have hd := double_remainder_le x hx0 hx1 p
  have hm := mul_le_mul_of_nonneg_right hxs hr
  have htail : remainder x p ≤ (prefix x (2*p)-prefix x p)/(1-s) := by
    apply (le_div_iff₀ (by linarith : 0 < 1-s)).mpr
    unfold remainder at hd hm ⊢
    nlinarith
  unfold remainder at htail
  linarith

variable {ι : Type*} [Fintype ι]
 def powerTrace (x : ι → ℝ) (p : ℕ) : ℝ := ∑ a, x a ^ p
 def prefixTrace (x : ι → ℝ) (p : ℕ) : ℝ := ∑ a, prefix (x a) p
 def logVolume (x : ι → ℝ) : ℝ := ∑ a, -Real.log (1-x a)

/-- Prefixes are computed directly from the trace moments. -/
 theorem prefix_as_moments (x : ι → ℝ) (p : ℕ) :
    prefixTrace x p = ∑ n ∈ Finset.range p, powerTrace x (n+1)/((n : ℝ)+1) := by
  unfold prefixTrace prefix powerTrace term
  simp_rw [Finset.sum_div]
  exact Finset.sum_comm

 theorem prefix_lower (x : ι → ℝ) (hx0 : ∀ a, 0 ≤ x a)
    (hx1 : ∀ a, x a < 1) (p : ℕ) : prefixTrace x p ≤ logVolume x := by
  apply Finset.sum_le_sum
  intro a _ha
  have := remainder_nonneg (x a) (hx0 a) (hx1 a) p
  unfold remainder at this
  linarith

/-- The source's sharp finite enclosure, evaluated on every retained direction. -/
 theorem sharp_trace_upper (x : ι → ℝ) (r : ℝ)
    (hx0 : ∀ a, 0 ≤ x a) (hxr : ∀ a, x a ≤ r)
    (hr0 : 0 < r) (hr1 : r < 1) (p : ℕ) :
    logVolume x ≤ prefixTrace x p +
      (remainder r p / r^(p+1)) * powerTrace x (p+1) := by
  have hh := Finset.sum_le_sum (s := Finset.univ)
    (fun a _ha => sharp_remainder_le (x a) r (hx0 a) (hxr a) hr0 hr1 p)
  simpa only [remainder, Finset.sum_sub_distrib, ← Finset.mul_sum,
    logVolume, prefixTrace, powerTrace, sub_le_iff_le_add, add_comm] using hh

/-- The first 2p trace moments alone give a finite upper certificate once s_p<1. -/
 theorem adaptive_trace_upper (x : ι → ℝ) (hx0 : ∀ a, 0 ≤ x a)
    (hx1 : ∀ a, x a < 1) (p : ℕ) (hs : powerTrace x p < 1) :
    logVolume x ≤ prefixTrace x p +
      (prefixTrace x (2*p)-prefixTrace x p)/(1-powerTrace x p) := by
  classical
  have hxp (a : ι) : x a ^ p ≤ powerTrace x p := by
    exact Finset.single_le_sum (fun b _hb => pow_nonneg (hx0 b) p) (Finset.mem_univ a)
  have hh := Finset.sum_le_sum (s := Finset.univ)
    (fun a _ha => adaptive_scalar (x a) (powerTrace x p) (hx0 a) (hx1 a) p (hxp a) hs)
  simpa only [Finset.sum_add_distrib, ← Finset.sum_div, Finset.sum_sub_distrib,
    prefixTrace, logVolume] using hh

/-- Every fixed finite restriction admits a successful adaptive stopping degree. -/
 theorem powerTrace_tendsto_zero (x : ι → ℝ) (hx0 : ∀ a, 0 ≤ x a)
    (hx1 : ∀ a, x a < 1) : Tendsto (powerTrace x) atTop (nhds 0) := by
  have hh := tendsto_finset_sum Finset.univ
    (fun a _ha => tendsto_pow_atTop_nhds_zero_of_lt_one (hx0 a) (hx1 a))
  simpa only [powerTrace, Finset.sum_const_zero] using hh

 theorem exists_stopping_degree (x : ι → ℝ) (hx0 : ∀ a, 0 ≤ x a)
    (hx1 : ∀ a, x a < 1) : ∃ p : ℕ, 0 < p ∧ powerTrace x p < 1 := by
  have he : ∀ᶠ p in atTop, powerTrace x p < 1 :=
    (tendsto_order.1 (powerTrace_tendsto_zero x hx0 hx1)).2 1 zero_lt_one
  obtain ⟨N, hN⟩ := Filter.eventually_atTop.1 he
  exact ⟨N+1, Nat.succ_pos N, hN (N+1) (Nat.le_succ N)⟩

end SplitZero.RestrictionLog
