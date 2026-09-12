import SplitZeroBoundaryControl
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

/-!
# Rank-two factorization and the exact scalar compression calculation

The cross matrix is factored through Fin 2. Nonzero eigenspaces transfer
through the displayed pair of maps. The scalar quadratic and its least
symmetric radius are proved, rather than inferred from a numerical sample.
-/
noncomputable section
namespace SplitZero.ControlCompression
universe u v

variable {ι : Type u} [Fintype ι]

def crossMatrix (h : ℝ) (a b : ι → ℂ) : Matrix ι ι ℂ :=
  fun i j => (h : ℂ) * (star (b i) * a j + star (a i) * b j)

def outMatrix (h : ℝ) (a b : ι → ℂ) : Matrix ι (Fin 2) ℂ :=
  fun i k => ![(h : ℂ) * star (b i), (h : ℂ) * star (a i)] k

def rowMatrix (a b : ι → ℂ) : Matrix (Fin 2) ι ℂ :=
  fun k j => ![a j, b j] k

theorem cross_factorization (h : ℝ) (a b : ι → ℂ) :
    crossMatrix h a b = outMatrix h a b * rowMatrix a b := by
  ext i j
  simp only [crossMatrix, outMatrix, rowMatrix, Matrix.mul_apply, Fin.sum_univ_two,
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons]
  ring

theorem rank_le_two (h : ℝ) (a b : ι → ℂ) :
    (crossMatrix h a b).rank ≤ 2 := by
  rw [cross_factorization]
  calc
    _ ≤ (outMatrix h a b).rank := Matrix.rank_mul_le_left _ _
    _ ≤ Fintype.card (Fin 2) := Matrix.rank_le_card_width _
    _ = 2 := rfl

/-- Actual control values on any specified finite family of coefficient vectors. -/
theorem control_matrix_rank_le_two
    {E : Type u} {H : Type v} [AddCommGroup E] [Module ℂ E]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (S : BoundaryControl.Data (E := E) (H := H)) (v : ι → E) :
    (Matrix.of fun i j => S.control (v i) (v j)).rank ≤ 2 := by
  have he : (Matrix.of fun i j => S.control (v i) (v j)) =
      crossMatrix S.normSquare (fun i => S.currentRow (v i))
        (fun i => S.nextRow (v i)) := by
    ext i j
    exact S.rank_two_formula (v i) (v j)
  rw [he]
  exact rank_le_two _ _ _

section EigenTransfer
variable {K : Type*} [Field K] {E F : Type*}
  [AddCommGroup E] [Module K E] [AddCommGroup F] [Module K F]

/-- Both directions of the nonzero eigenvalue transfer use actual maps. -/
theorem nonzero_eigen_transfer (f : E →ₗ[K] F) (g : F →ₗ[K] E)
    (c : K) (hc : c ≠ 0) :
    (∃ x : E, x ≠ 0 ∧ g (f x) = c • x) ↔
    (∃ y : F, y ≠ 0 ∧ f (g y) = c • y) := by
  constructor
  · rintro ⟨x, hx, he⟩
    refine ⟨f x, ?_, ?_⟩
    · intro hz
      rw [hz, map_zero] at he
      exact hx ((smul_eq_zero.mp he.symm).resolve_left hc)
    · rw [he, map_smul]
  · rintro ⟨y, hy, he⟩
    refine ⟨g y, ?_, ?_⟩
    · intro hz
      rw [hz, map_zero] at he
      exact hy ((smul_eq_zero.mp he.symm).resolve_left hc)
    · rw [he, map_smul]
end EigenTransfer

/-- The small matrix from the row/out-map composition, before its positive h factor. -/
def compressed (a b : ℝ) (c : ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![c, (a : ℂ); (b : ℂ), star c]

theorem compressed_determinant (a b x : ℝ) (c : ℂ) :
    (compressed a b c - (x : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ)).det =
      (((x - c.re)^2 + c.im^2 - a*b : ℝ) : ℂ) := by
  apply Complex.ext <;>
    simp [compressed, Matrix.det_fin_two, Matrix.sub_apply, Matrix.smul_apply,
      Matrix.one_apply, Complex.mul_re, Complex.mul_im] <;> ring

theorem real_roots (a b cr ci x : ℝ) (h : 0 ≤ a*b-ci^2) :
    (x-cr)^2+ci^2-a*b = 0 ↔
      x = cr + Real.sqrt (a*b-ci^2) ∨ x = cr - Real.sqrt (a*b-ci^2) := by
  have hs := Real.sq_sqrt h
  constructor
  · intro he
    have hp : (x-cr-Real.sqrt (a*b-ci^2)) * (x-cr+Real.sqrt (a*b-ci^2)) = 0 := by
      nlinarith
    rcases mul_eq_zero.mp hp with hp | hp
    · left; linarith
    · right; linarith
  · rintro (rfl | rfl) <;> nlinarith

theorem exact_radius (c q : ℝ) (hq : 0 ≤ q) :
    max |c+q| |c-q| = |c|+q := by
  apply le_antisymm
  · apply max_le
    · simpa only [abs_of_nonneg hq] using abs_add c q
    · simpa only [sub_eq_add_neg, abs_neg, abs_of_nonneg hq] using abs_add c (-q)
  · rcases le_total 0 c with hc | hc
    · calc
        |c|+q = c+q := by rw [abs_of_nonneg hc]
        _ = |c+q| := (abs_of_nonneg (add_nonneg hc hq)).symm
        _ ≤ max |c+q| |c-q| := le_max_left _ _
    · calc
        |c|+q = -(c-q) := by rw [abs_of_nonpos hc]; ring
        _ = |c-q| := (abs_of_nonpos (sub_nonpos.mpr (hc.trans hq))).symm
        _ ≤ max |c+q| |c-q| := le_max_right _ _

theorem traceless_radius (a b ci : ℝ) :
    max |Real.sqrt (a*b-ci^2)| |-Real.sqrt (a*b-ci^2)| = Real.sqrt (a*b-ci^2) := by
  simpa using exact_radius 0 (Real.sqrt (a*b-ci^2)) (Real.sqrt_nonneg _)
end SplitZero.ControlCompression
