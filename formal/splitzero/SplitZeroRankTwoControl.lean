import Mathlib.Data.Complex.Basic
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.ConjTranspose
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# Rank-two boundary control and its two-dimensional certificate

The two rows are not independent spectral models. They are the two rows
extracted from the specified representative and the next admitted relation.
This module proves the finite linear algebra used by that extraction.
-/

set_option autoImplicit false
noncomputable section
namespace SplitZero.RankTwoControl

open scoped ComplexConjugate Matrix
universe u
variable {I : Type u} [Fintype I]

def control (h : ℝ) (r s : I → ℂ) : Matrix I I ℂ :=
  fun i j => (h : ℂ) * (conj (s i) * r j + conj (r i) * s j)

def rows (r s : I → ℂ) : Matrix (Fin 2) I ℂ := ![r, s]

def columns (h : ℝ) (r s : I → ℂ) : Matrix I (Fin 2) ℂ :=
  fun i => ![(h : ℂ) * conj (s i), (h : ℂ) * conj (r i)]

omit [Fintype I] in
theorem factorization (h : ℝ) (r s : I → ℂ) :
    control h r s = columns h r s * rows r s := by
  ext i j
  simp [control, columns, rows, Matrix.mul_apply, Fin.sum_univ_two]
  ring

theorem rank_le_two (h : ℝ) (r s : I → ℂ) :
    (control h r s).rank ≤ 2 := by
  rw [factorization]
  exact (Matrix.rank_mul_le_left _ _).trans
    (by simpa using (Matrix.rank_le_card_width (columns h r s)))

omit [Fintype I] in
theorem hermitian (h : ℝ) (r s : I → ℂ) :
    (control h r s).IsHermitian := by
  apply Matrix.IsHermitian.ext
  intro i j
  change conj ((h : ℂ)*(conj (s j)*r i+conj (r j)*s i)) =
    (h : ℂ)*(conj (s i)*r j+conj (r i)*s j)
  simp only [map_mul, map_add, Complex.conj_ofReal, Complex.conj_conj]
  ring

/-- The normalized map still factors through two coordinates. -/
theorem normalized_factorization (Ginv : Matrix I I ℂ) (h : ℝ) (r s : I → ℂ) :
    Ginv * control h r s = (Ginv * columns h r s) * rows r s := by
  rw [factorization, Matrix.mul_assoc]

section Transfer
variable {E F : Type*} [AddCommGroup E] [Module ℂ E]
  [AddCommGroup F] [Module ℂ F]

/-- Nonzero eigenvectors transfer along the actual two-composition maps. -/
theorem eigenvector_transfer (f : E →ₗ[ℂ] F) (g : F →ₗ[ℂ] E)
    (μ : ℂ) (hμ : μ ≠ 0) (x : E) (hx : x ≠ 0)
    (he : g (f x) = μ • x) :
    f x ≠ 0 ∧ f (g (f x)) = μ • f x := by
  constructor
  · intro hf
    have hz : μ • x = 0 := by rw [← he, hf, map_zero]
    exact (smul_ne_zero hμ hx) hz
  · rw [he, map_smul]

theorem nonzero_eigenvalues_iff (f : E →ₗ[ℂ] F) (g : F →ₗ[ℂ] E)
    (μ : ℂ) (hμ : μ ≠ 0) :
    (∃ x, x ≠ 0 ∧ g (f x) = μ • x) ↔
      ∃ y, y ≠ 0 ∧ f (g y) = μ • y := by
  constructor
  · rintro ⟨x, hx, he⟩
    exact ⟨f x, eigenvector_transfer f g μ hμ x hx he⟩
  · rintro ⟨y, hy, he⟩
    exact ⟨g y, eigenvector_transfer g f μ hμ y hy he⟩
end Transfer

def compressed (a b : ℝ) (c : ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![c, (a : ℂ); (b : ℂ), conj c]

theorem compressed_det (a b : ℝ) (c : ℂ) :
    (compressed a b c).det = (c.re ^ 2 + c.im ^ 2 - a*b : ℝ) := by
  apply Complex.ext
  · simp [compressed, Matrix.det_fin_two, pow_two]
  · simp [compressed, Matrix.det_fin_two, pow_two]
    ring

theorem compressed_real_root (a b t : ℝ) (c : ℂ) :
    (compressed a b c - (t : ℂ) • 1).det = 0 ↔
      (t - c.re)^2 = a*b - c.im^2 := by
  have hd :
      (compressed a b c - (t : ℂ) • 1).det =
        (((t-c.re)^2 - (a*b-c.im^2) : ℝ) : ℂ) := by
    apply Complex.ext <;>
      simp [compressed, Matrix.det_fin_two, pow_two] <;> ring
  rw [hd, Complex.ofReal_eq_zero, sub_eq_zero]

theorem radicand_nonnegative (a b : ℝ) (c : ℂ)
    (hc : c.re^2 + c.im^2 ≤ a*b) :
    0 ≤ a*b - c.im^2 := by
  nlinarith [sq_nonneg c.re]

theorem real_roots (a b t : ℝ) (c : ℂ)
    (hc : c.re^2 + c.im^2 ≤ a*b) :
    (compressed a b c - (t : ℂ) • 1).det = 0 ↔
      t = c.re + Real.sqrt (a*b-c.im^2) ∨
      t = c.re - Real.sqrt (a*b-c.im^2) := by
  rw [compressed_real_root]
  have hs := Real.sq_sqrt (radicand_nonnegative a b c hc)
  constructor
  · intro ht
    have hh : (t-c.re-Real.sqrt (a*b-c.im^2)) *
        (t-c.re+Real.sqrt (a*b-c.im^2)) = 0 := by nlinarith
    rcases mul_eq_zero.mp hh with hp | hm
    · left; linarith
    · right; linarith
  · rintro (rfl | rfl) <;> nlinarith

/-- Exact largest absolute value of the two real roots, including rank one. -/
theorem max_abs_roots (x s : ℝ) (hs : 0 ≤ s) :
    max |x+s| |x-s| = |x|+s := by
  rcases le_total 0 x with hx | hx
  · have hp : |x+s| = x+s := abs_of_nonneg (by linarith)
    have hm : |x-s| ≤ x+s := (abs_le).mpr ⟨by linarith, by linarith⟩
    rw [hp, max_eq_left hm, abs_of_nonneg hx]
  · have hm : |x-s| = -x+s := by
      rw [abs_of_nonpos (by linarith)]
      ring
    have hp : |x+s| ≤ -x+s := (abs_le).mpr ⟨by linarith, by linarith⟩
    rw [hm, max_eq_right hp, abs_of_nonpos hx]

/-- The scalar expression in the supplied rank-two certificate. -/
theorem symmetric_allowance (h a b : ℝ) (c : ℂ) (hh : 0 ≤ h) :
    max |h*(c.re+Real.sqrt (a*b-c.im^2))|
        |h*(c.re-Real.sqrt (a*b-c.im^2))| =
      h*(|c.re|+Real.sqrt (a*b-c.im^2)) := by
  rw [abs_mul, abs_mul, abs_of_nonneg hh, ← mul_max_of_nonneg _ _ hh,
    max_abs_roots _ _ (Real.sqrt_nonneg _)]

/-- Reflection-stable trace-zero data remove the real-part term exactly. -/
theorem trace_zero_allowance (h a b : ℝ) (c : ℂ) (hc : c.re = 0) :
    h*(|c.re|+Real.sqrt (a*b-c.im^2)) =
      h*Real.sqrt (a*b-c.im^2) := by
  rw [hc, abs_zero, zero_add]

end SplitZero.RankTwoControl
