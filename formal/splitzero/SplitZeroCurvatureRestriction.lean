import SplitZeroRestrictionSpectrum
import SplitZeroRestrictionTransport

/-!
The curvature cost and the bounded restriction loss use different coordinates:
lambda >= 0 and x=lambda/(1+lambda). Both are retained explicitly.
The normalized coefficients are the rational expressions in the source's
all-order curvature-jet formula. Derivative interpretation beyond first
order remains a written theorem, not a hidden formal premise.
-/
noncomputable section
namespace SplitZero.CurvatureRestriction
open Matrix
open scoped BigOperators

def loss (l : ℝ) : ℝ := l/(1+l)
def radialMass (l t : ℝ) : ℝ := t*l/(1+t*l)
def density (l t : ℝ) : ℝ := l/(1+t*l)^2

theorem loss_nonneg (l : ℝ) (hl : 0 ≤ l) : 0 ≤ loss l := by
  unfold loss
  positivity

theorem loss_lt_one (l : ℝ) (hl : 0 ≤ l) : loss l < 1 := by
  unfold loss
  apply (div_lt_one (by linarith : 0 < 1+l)).mpr
  linarith

theorem one_sub_loss (l : ℝ) (hl : 0 ≤ l) : 1-loss l = (1+l)⁻¹ := by
  unfold loss
  field_simp
  ring

/-- A genuine derivative of cumulative radial curvature. -/
theorem radialMass_deriv (l t : ℝ) (h : 1+t*l ≠ 0) :
    HasDerivAt (radialMass l) (density l t) t := by
  have hd := (((hasDerivAt_id t).mul_const l).div
    ((hasDerivAt_const t 1).add ((hasDerivAt_id t).mul_const l)) h)
  change HasDerivAt (radialMass l) _ t at hd
  convert hd using 1
  dsimp [density]
  ring

/-- The first derivative retains the factor two and the cubic denominator. -/
theorem density_deriv (l t : ℝ) (h : 1+t*l ≠ 0) :
    HasDerivAt (density l) (-2*l^2/(1+t*l)^3) t := by
  have hd := ((hasDerivAt_const t l).div
    (((hasDerivAt_const t 1).add ((hasDerivAt_id t).mul_const l)).pow 2)
    (pow_ne_zero 2 h))
  change HasDerivAt (density l) _ t at hd
  convert hd using 1
  dsimp
  field_simp [h]
  ring

theorem density_at_one (l : ℝ) (hl : 0 ≤ l) :
    density l 1 = loss l - (loss l)^2 := by
  have h : 1+l ≠ 0 := by linarith
  unfold density loss
  simp only [one_mul]
  field_simp
  ring

/-- Exact change to the bounded return-loss spectrum. -/
theorem density_change (l t : ℝ) (hl : 0 ≤ l) (ht : 0 ≤ t) :
    density l t = loss l * (1-loss l) / (1-(1-t)*loss l)^2 := by
  have h1 : 1+l ≠ 0 := by linarith
  have h2 : 1+t*l ≠ 0 := ne_of_gt (by positivity : 0 < 1+t*l)
  have he : 1-(1-t)*loss l = (1+t*l)/(1+l) := by
    unfold loss
    field_simp
    ring
  rw [he, one_sub_loss l hl]
  unfold density loss
  rw [div_pow]
  field_simp [h1, h2]
  ring

/-- Rational normalized curvature-jet coefficient at t=1. -/
theorem jet_scalar (l : ℝ) (hl : 0 ≤ l) (n : ℕ) :
    l^(n+1)/(1+l)^(n+2) = (loss l)^(n+1) - (loss l)^(n+2) := by
  have h : 1+l ≠ 0 := by linarith
  unfold loss
  simp only [div_pow, pow_succ]
  field_simp
  ring

section Spectrum
variable {ι : Type*} [Fintype ι]

def curvature (l : ι → ℝ) (t : ℝ) : ℝ := ∑ a, density (l a) t
def cumulative (l : ι → ℝ) (t : ℝ) : ℝ := ∑ a, radialMass (l a) t
def cost (l : ι → ℝ) : ℝ := ∑ a, Real.log (1+l a)
def normalizedJet (l : ι → ℝ) (n : ℕ) : ℝ := ∑ a, (l a)^(n+1)/(1+l a)^(n+2)

theorem cumulative_at_one (l : ι → ℝ) :
    cumulative l 1 = RestrictionLog.powerTrace (fun a => loss (l a)) 1 := by
  simp [cumulative, radialMass, loss, RestrictionLog.powerTrace]

theorem curvature_at_one (l : ι → ℝ) (hl : ∀ a, 0 ≤ l a) :
    curvature l 1 = RestrictionLog.powerTrace (fun a => loss (l a)) 1 -
      RestrictionLog.powerTrace (fun a => loss (l a)) 2 := by
  simp only [curvature, density_at_one _ (hl _), Finset.sum_sub_distrib,
    RestrictionLog.powerTrace, pow_one]

theorem jet_as_difference (l : ι → ℝ) (hl : ∀ a, 0 ≤ l a) (n : ℕ) :
    normalizedJet l n = RestrictionLog.powerTrace (fun a => loss (l a)) (n+1) -
      RestrictionLog.powerTrace (fun a => loss (l a)) (n+2) := by
  simp only [normalizedJet, jet_scalar _ (hl _) n, Finset.sum_sub_distrib,
    RestrictionLog.powerTrace]

/-- All bounded trace powers are recovered with the radial mass retained. -/
theorem recover_moment (l : ι → ℝ) (hl : ∀ a, 0 ≤ l a) (p : ℕ) :
    RestrictionLog.powerTrace (fun a => loss (l a)) (p+1) =
      cumulative l 1 - ∑ n ∈ Finset.range p, normalizedJet l n := by
  induction p with
  | zero => simp [cumulative_at_one]
  | succ p ih =>
      rw [Finset.sum_range_succ, jet_as_difference l hl p]
      rw [show p+1+1=p+2 by omega]
      linarith

theorem cost_eq (l : ι → ℝ) (hl : ∀ a, 0 ≤ l a) :
    cost l = RestrictionLog.logVolume (fun a => loss (l a)) := by
  unfold cost RestrictionLog.logVolume
  apply Finset.sum_congr rfl
  intro a _ha
  rw [one_sub_loss (l a) (hl a), Real.log_inv, neg_neg]

/-- Compose the curvature cost with the previously proved adaptive certificate. -/
theorem curvature_certificate (l : ι → ℝ) (hl : ∀ a, 0 ≤ l a)
    (p : ℕ) (hp : RestrictionLog.powerTrace (fun a => loss (l a)) p < 1) :
    cost l ≤ RestrictionLog.prefixTrace (fun a => loss (l a)) p +
      (RestrictionLog.prefixTrace (fun a => loss (l a)) (2*p) -
        RestrictionLog.prefixTrace (fun a => loss (l a)) p) /
      (1-RestrictionLog.powerTrace (fun a => loss (l a)) p) := by
  rw [cost_eq l hl]
  exact RestrictionLog.adaptive_trace_upper _
    (fun a => loss_nonneg (l a) (hl a)) (fun a => loss_lt_one (l a) (hl a)) p hp

theorem stopping (l : ι → ℝ) (hl : ∀ a, 0 ≤ l a) :
    ∃ p : ℕ, 0 < p ∧ RestrictionLog.powerTrace (fun a => loss (l a)) p < 1 :=
  RestrictionLog.exists_stopping_degree _
    (fun a => loss_nonneg (l a) (hl a)) (fun a => loss_lt_one (l a) (hl a))
end Spectrum

section Matrices
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

theorem cost_operator (Ki Gi Kj Gj : Matrix ι ι ℂ)
    (hi : Ki*Gi=1) (hj : Kj*Gj=1) :
    Kj*(Gi-Gj) = (Kj-Ki)*Gi := by
  rw [Matrix.mul_sub, Matrix.sub_mul, hi, hj]

/-- I+Z is the inverse of the original return. -/
theorem return_cost (Ki Gi Kj Gj : Matrix ι ι ℂ)
    (hGi : Gi*Ki=1) (hGj : Gj*Kj=1) (hi : Ki*Gi=1) (hj : Kj*Gj=1) :
    (1+Kj*(Gi-Gj))*(Ki*Gj)=1 ∧ (Ki*Gj)*(1+Kj*(Gi-Gj))=1 := by
  have hz : 1+Kj*(Gi-Gj)=Kj*Gi := by rw [Matrix.mul_sub, hj]; abel
  rw [hz]
  constructor
  · calc
      _ = Kj*(Gi*Ki)*Gj := by simp only [Matrix.mul_assoc]
      _ = 1 := by rw [hGi, Matrix.mul_one, hj]
  · calc
      _ = Ki*(Gj*Kj)*Gi := by simp only [Matrix.mul_assoc]
      _ = 1 := by rw [hGj, Matrix.mul_one, hi]

/-- Actual complex matrix traces evaluate the certificate through a spectral witness. -/
theorem matrix_curvature_certificate (H U V : Matrix ι ι ℂ) (l : ι → ℝ)
    (hUV : U*V=1) (hVU : V*U=1)
    (hH : H=U*(Matrix.diagonal (fun a => (loss (l a) : ℂ)))*V)
    (hl : ∀ a, 0 ≤ l a) (p : ℕ) (hp : RestrictionSpectrum.moment H p < 1) :
    cost l ≤ RestrictionSpectrum.matrixPrefix H p +
      (RestrictionSpectrum.matrixPrefix H (2*p)-RestrictionSpectrum.matrixPrefix H p)/
      (1-RestrictionSpectrum.moment H p) := by
  rw [cost_eq l hl, ← RestrictionSpectrum.log_volume_eq H U V _ hUV hH
    (fun a => loss_lt_one (l a) (hl a))]
  exact RestrictionSpectrum.matrix_certificate H U V _ hUV hVU hH
    (fun a => loss_nonneg (l a) (hl a)) (fun a => loss_lt_one (l a) (hl a)) p hp
end Matrices
end SplitZero.CurvatureRestriction
