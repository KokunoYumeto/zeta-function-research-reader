import SplitZeroBoundaryControl
import Mathlib.Tactic

/-!
# Relative frontier estimates

The source is the owner's Symmetric Frontier Control continuation, Section 4.
These are estimates for actual pairs of coefficient maps with their stated
quadratic bounds. The arithmetic recurrence and its incidence estimate are
separate inputs, not conclusions inferred from a positive matrix.
-/
noncomputable section
namespace SplitZero.FrontierEstimate

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
local notation "⟪" x ", " y "⟫" => inner ℂ x y

/-- Cauchy--Schwarz with the Hermitian cross term, without losing its sign. -/
theorem cross_abs (x y : H) :
    |(⟪x, y⟫ + ⟪y, x⟫).re| ≤ 2 * (‖x‖ * ‖y‖) := by
  have h := (Complex.abs_re_le_norm (⟪x, y⟫)).trans (norm_inner_le_norm x y)
  have hs : (⟪y, x⟫).re = (⟪x, y⟫).re := by
    simpa using congrArg Complex.re (inner_conj_symm y x)
  rw [Complex.add_re, hs]
  apply abs_le.mpr
  rcases abs_le.mp h with ⟨hl, hu⟩
  constructor <;> linarith

/-- The finite bound includes zero costs and zero quadratic values. -/
theorem cross_bound (x y : H) {q gamma lam : ℝ}
    (hq : 0 ≤ q) (hg : 0 ≤ gamma) (hl : 0 ≤ lam)
    (hx : ‖x‖ ^ 2 ≤ lam * q) (hy : ‖y‖ ^ 2 ≤ gamma * q) :
    |(⟪x, y⟫ + ⟪y, x⟫).re| ≤ 2 * Real.sqrt (gamma * lam) * q := by
  have hm := mul_le_mul hx hy (sq_nonneg ‖y‖) (mul_nonneg hl hq)
  have hr := Real.sq_sqrt (mul_nonneg hg hl)
  have hroot := Real.sqrt_nonneg (gamma * lam)
  have hp : 0 ≤ ‖x‖ * ‖y‖ := mul_nonneg (norm_nonneg _) (norm_nonneg _)
  have htarget : 0 ≤ Real.sqrt (gamma * lam) * q := mul_nonneg hroot hq
  have hs : (‖x‖ * ‖y‖) ^ 2 ≤ (Real.sqrt (gamma * lam) * q) ^ 2 := by
    nlinarith [sq_nonneg q]
  have hc : ‖x‖ * ‖y‖ ≤ Real.sqrt (gamma * lam) * q := by
    nlinarith
  exact (cross_abs x y).trans (by nlinarith)

/-- The equivalent pair of upper and lower quadratic inequalities. -/
theorem two_sided (x y : H) {q gamma lam : ℝ}
    (hq : 0 ≤ q) (hg : 0 ≤ gamma) (hl : 0 ≤ lam)
    (hx : ‖x‖ ^ 2 ≤ lam * q) (hy : ‖y‖ ^ 2 ≤ gamma * q) :
    -(2 * Real.sqrt (gamma * lam) * q) ≤ (⟪x, y⟫ + ⟪y, x⟫).re ∧
      (⟪x, y⟫ + ⟪y, x⟫).re ≤ 2 * Real.sqrt (gamma * lam) * q :=
  abs_le.mp (cross_bound x y hq hg hl hx hy)

/-- The estimate acts on supplied linear maps, so it restricts to every submodule. -/
theorem map_bound {E : Type*} [AddCommGroup E] [Module ℂ E]
    (F Eplus : E →ₗ[ℂ] H) (q : E → ℝ) {gamma lam : ℝ}
    (hq : ∀ x, 0 ≤ q x) (hg : 0 ≤ gamma) (hl : 0 ≤ lam)
    (hF : ∀ x, ‖F x‖ ^ 2 ≤ lam * q x)
    (hE : ∀ x, ‖Eplus x‖ ^ 2 ≤ gamma * q x) (x : E) :
    |(⟪F x, Eplus x⟫ + ⟪Eplus x, F x⟫).re| ≤
      2 * Real.sqrt (gamma * lam) * q x :=
  cross_bound _ _ (hq x) hg hl (hF x) (hE x)

/-- A certificate may retain rational separate norm bounds rather than take a square root. -/
theorem cross_bound_product (x y : H) {q a b : ℝ}
    (hq : 0 ≤ q) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hx : ‖x‖ ^ 2 ≤ a ^ 2 * q) (hy : ‖y‖ ^ 2 ≤ b ^ 2 * q) :
    |(⟪x, y⟫ + ⟪y, x⟫).re| ≤ 2 * a * b * q := by
  have hm := mul_le_mul hx hy (sq_nonneg ‖y‖) (mul_nonneg (sq_nonneg a) hq)
  have hp := mul_nonneg (norm_nonneg x) (norm_nonneg y)
  have hab := mul_nonneg (mul_nonneg ha hb) hq
  have hle : ‖x‖ * ‖y‖ ≤ a * b * q := by nlinarith
  exact (cross_abs x y).trans (by nlinarith)

/-- The checked old boundary form uses the negative of this same cross term. -/
theorem old_boundary_bound {E : Type*} [AddCommGroup E] [Module ℂ E]
    (S : SplitZero.BoundaryControl.Data (E := E) (H := H))
    (x : E) {q gamma lam : ℝ}
    (hq : 0 ≤ q) (hg : 0 ≤ gamma) (hl : 0 ≤ lam)
    (hx : ‖S.representative x‖ ^ 2 ≤ lam * q)
    (hy : ‖S.boundary x‖ ^ 2 ≤ gamma * q) :
    |(S.control x x).re| ≤ 2 * Real.sqrt (gamma * lam) * q := by
  rw [S.control_boundary]
  simpa only [Complex.neg_re, abs_neg] using
    cross_bound (S.representative x) (S.boundary x) hq hg hl hx hy

/-- Pointwise Gram bounds pass through every specified inclusion unchanged. -/
theorem restrict_bound {E F : Type*} (i : F → E) (q w : E → ℝ) (eps : ℝ)
    (h : ∀ x, |w x| ≤ eps * q x) : ∀ y, |w (i y)| ≤ eps * q (i y) :=
  fun y => h (i y)

end SplitZero.FrontierEstimate
