import SplitZeroRankTwoControl
import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.LinearCombination

/-!
# Actual orthogonal representatives and boundary pairings

The ambient inner-product space may be infinite dimensional. The indices
label finitely many actual test vectors, not a replacement spectral model.
The integration-by-parts input is kept explicit as a Green identity.
-/

noncomputable section
namespace SplitZero.OrthogonalControl

open scoped ComplexConjugate Matrix
universe u v
variable {I : Type u} [Fintype I]
  {H : Type v} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

def gram (R : I → H) : Matrix I I ℂ :=
  fun i j => inner ℂ (R i) (R j)

def boundaryForm (R B : I → H) : Matrix I I ℂ :=
  fun i j => -(inner ℂ (R i) (B j) + inner ℂ (B i) (R j))

def residual (U : Submodule ℂ H) [U.HasOrthogonalProjection] (x : H) : H :=
  x - U.starProjection x

theorem residual_orthogonal (U : Submodule ℂ H) [U.HasOrthogonalProjection]
    (x y : H) (hy : y ∈ U) :
    inner ℂ (residual U x) y = 0 :=
  U.starProjection_inner_eq_zero x y hy

theorem residual_relation_invariant (U : Submodule ℂ H)
    [U.HasOrthogonalProjection] (x y : H) (hy : y ∈ U) :
    residual U (x+y) = residual U x := by
  unfold residual
  rw [map_add, U.starProjection_eq_self_iff.mpr hy]
  abel

theorem pythagorean_pair (U : Submodule ℂ H) [U.HasOrthogonalProjection]
    (x y a b : H) (ha : a ∈ U) (hb : b ∈ U) :
    inner ℂ (residual U x+a) (residual U y+b) =
      inner ℂ (residual U x) (residual U y) + inner ℂ a b := by
  have h1 := residual_orthogonal U x b hb
  have h2 : inner ℂ a (residual U y) = 0 :=
    inner_eq_zero_symm.mp (residual_orthogonal U y a ha)
  simp only [inner_add_left, inner_add_right, h1, h2, add_zero, zero_add]

omit [Fintype I] in
/-- Completion of the Gram square within the admitted relation space. -/
theorem gram_minimum_decomposition (U : Submodule ℂ H) [U.HasOrthogonalProjection]
    (R C : I → H) (hC : ∀ i, C i ∈ U) :
    gram (fun i => R i+C i) =
      gram (fun i => residual U (R i)) +
      gram (fun i => U.starProjection (R i)+C i) := by
  ext i j
  have hi : R i+C i = residual U (R i)+(U.starProjection (R i)+C i) := by
    unfold residual; abel
  have hj : R j+C j = residual U (R j)+(U.starProjection (R j)+C j) := by
    unfold residual; abel
  change inner ℂ (R i+C i) (R j+C j) = _
  rw [hi, hj]
  exact pythagorean_pair U (R i) (R j) _ _
    (U.add_mem (U.starProjection_apply_mem _) (hC i))
    (U.add_mem (U.starProjection_apply_mem _) (hC j))

/-- The next projector step, retaining the unscaled vector and its norm. -/
def nextRepresentative (R : I → H) (u : H) (s : I → ℂ) : I → H :=
  fun i => R i - s i • u

omit [Fintype I] in
theorem next_row_zero (R : I → H) (u : H) (s : I → ℂ) (h : ℝ)
    (hu : inner ℂ u u = (h : ℂ))
    (hr : ∀ i, inner ℂ u (R i) = (h : ℂ)*s i) (i : I) :
    inner ℂ u (nextRepresentative R u s i) = 0 := by
  simp only [nextRepresentative, inner_sub_right, inner_smul_right, hr, hu]
  ring

omit [Fintype I] in
/-- Exact rank-one Gram downdate, with no normalization of u. -/
theorem gram_downdate (R : I → H) (u : H) (s : I → ℂ) (h : ℝ)
    (hu : inner ℂ u u = (h : ℂ))
    (hr : ∀ i, inner ℂ u (R i) = (h : ℂ)*s i) :
    gram R - gram (nextRepresentative R u s) =
      Matrix.vecMulVec (fun i => (h : ℂ)*conj (s i)) s := by
  ext i j
  have hleft (i : I) : inner ℂ (R i) u = (h : ℂ)*conj (s i) := by
    rw [← inner_conj_symm, hr]
    simp
  simp only [gram, nextRepresentative, Matrix.sub_apply, Matrix.vecMulVec_apply,
    inner_sub_left, inner_sub_right, inner_smul_left, inner_smul_right, hu, hr, hleft]
  ring

theorem gram_downdate_rank_le_one (R : I → H) (u : H) (s : I → ℂ) (h : ℝ)
    (hu : inner ℂ u u = (h : ℂ))
    (hr : ∀ i, inner ℂ u (R i) = (h : ℂ)*s i) :
    (gram R - gram (nextRepresentative R u s)).rank ≤ 1 := by
  rw [gram_downdate R u s h hu hr]
  exact Matrix.rank_vecMulVec_le _ _

omit [Fintype I] in
/-- Old relation vectors stay present; only their pairings vanish. -/
theorem one_new_relation_control (R old : I → H) (u : H)
    (r s : I → ℂ) (h : ℝ)
    (ho : ∀ i j, inner ℂ (R i) (old j) = 0)
    (hr : ∀ i, inner ℂ u (R i) = (h : ℂ)*s i) :
    boundaryForm R (fun i => old i - r i • u) =
      SplitZero.RankTwoControl.control h r s := by
  ext i j
  have hleft : inner ℂ (R i) u = (h : ℂ)*conj (s i) := by
    rw [← inner_conj_symm, hr]
    simp
  have hor : inner ℂ (old i) (R j) = 0 :=
    inner_eq_zero_symm.mp (ho j i)
  simp only [boundaryForm, SplitZero.RankTwoControl.control,
    inner_sub_left, inner_sub_right, inner_smul_left, inner_smul_right,
    ho, hor, hr, hleft]
  ring

/-- The same low-rank theorem in arbitrary packet dimension. -/
theorem one_new_relation_rank_le_two (R old : I → H) (u : H)
    (r s : I → ℂ) (h : ℝ)
    (ho : ∀ i j, inner ℂ (R i) (old j) = 0)
    (hr : ∀ i, inner ℂ u (R i) = (h : ℂ)*s i) :
    (boundaryForm R (fun i => old i-r i • u)).rank ≤ 2 := by
  rw [one_new_relation_control R old u r s h ho hr]
  exact SplitZero.RankTwoControl.rank_le_two h r s

/-- Integration by parts plus the actual derivative-boundary equation. -/
theorem green_identity (A : Matrix I I ℂ) (R B : I → H)
    (hgreen : ∀ i j,
      inner ℂ ((∑ k, A k i • R k)+B i) (R j) +
      inner ℂ (R i) ((∑ k, A k j • R k)+B j) =
      inner ℂ (R i) (R j)) :
    A.conjTranspose * gram R + gram R * A - gram R = boundaryForm R B := by
  ext i j
  have he := hgreen i j
  simp only [inner_add_left, inner_add_right, sum_inner, inner_sum,
    inner_smul_left, inner_smul_right] at he
  change (∑ k, conj (A k i)*inner ℂ (R k) (R j)) +
      (∑ k, inner ℂ (R i) (R k)*A k j) - inner ℂ (R i) (R j) =
    -(inner ℂ (R i) (B j)+inner ℂ (B i) (R j))
  simp only [mul_comm (A _ _) (inner ℂ _ _)] at he
  linear_combination he

end SplitZero.OrthogonalControl
