import SplitZeroFrontierEstimate

/-!
# The lowering-incidence estimate before arithmetic specialization

Raising and lowering have different target degree spaces. The off-diagonal
commutation identity is kept explicitly; no equality of these spaces is assumed.
In the source's orthogonal polynomial coordinates the two diagonal weights are
sum_j a_(alpha_j+1) and sum_j a_(alpha_j). This file proves the finite inequality
from those diagonal coefficients, rather than assuming the final operator bound.
-/
noncomputable section
namespace SplitZero.IncidenceEstimate
open scoped BigOperators
variable {ι : Type*} [Fintype ι]
variable {H K : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]
  [NormedAddCommGroup K] [InnerProductSpace ℝ K]

/-- Cauchy--Schwarz for a finite vector sum, including the empty index type. -/
theorem norm_sum_sq (u : ι → H) :
    ‖∑ i, u i‖ ^ 2 ≤ (Fintype.card ι : ℝ) * ∑ i, ‖u i‖ ^ 2 := by
  have ht := norm_sum_le (Finset.univ : Finset ι) u
  have hc := Finset.sum_mul_sq_le_sq_mul_sq (Finset.univ : Finset ι)
    (fun i => ‖u i‖) (fun _ => (1 : ℝ))
  have hs : (∑ i, ‖u i‖) ^ 2 ≤ (∑ i, ‖u i‖ ^ 2) * (Fintype.card ι : ℝ) := by
    simpa using hc
  have hnon : 0 ≤ ∑ i, ‖u i‖ := Finset.sum_nonneg (fun i _ => norm_nonneg (u i))
  nlinarith [norm_nonneg (∑ i, u i)]

/-- The commuted cross terms cancel; only the diagonal difference remains. -/
theorem raising_lowering_identity (u : ι → H) (v : ι → K)
    (hc : ∀ i j, i ≠ j → inner ℝ (u i) (u j) = inner ℝ (v i) (v j)) :
    ‖∑ i, u i‖ ^ 2 - ‖∑ i, v i‖ ^ 2 =
      (∑ i, ‖u i‖ ^ 2) - ∑ i, ‖v i‖ ^ 2 := by
  classical
  have hu : ‖∑ i, u i‖ ^ 2 = ∑ i, ∑ j, inner ℝ (u i) (u j) := by
    rw [← real_inner_self_eq_norm_sq]
    simp only [sum_inner, inner_sum]
  have hv : ‖∑ i, v i‖ ^ 2 = ∑ i, ∑ j, inner ℝ (v i) (v j) := by
    rw [← real_inner_self_eq_norm_sq]
    simp only [sum_inner, inner_sum]
  rw [hu, hv, ← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i _
  rw [← Finset.sum_sub_distrib]
  calc
    (∑ j, (inner ℝ (u i) (u j) - inner ℝ (v i) (v j))) =
        inner ℝ (u i) (u i) - inner ℝ (v i) (v i) := by
      apply Finset.sum_eq_single i
      · intro j _ hji
        rw [hc i j (Ne.symm hji), sub_self]
      · intro hi
        exact (hi (Finset.mem_univ i)).elim
    _ = ‖u i‖ ^ 2 - ‖v i‖ ^ 2 := by
      rw [real_inner_self_eq_norm_sq, real_inner_self_eq_norm_sq]

/-- This is the source's k-1 lowering cost, not k times the raising norm. -/
theorem raising_bound (u : ι → H) (v : ι → K)
    (hc : ∀ i j, i ≠ j → inner ℝ (u i) (u j) = inner ℝ (v i) (v j)) :
    ‖∑ i, u i‖ ^ 2 ≤ (∑ i, ‖u i‖ ^ 2) +
      ((Fintype.card ι : ℝ) - 1) * ∑ i, ‖v i‖ ^ 2 := by
  have hid := raising_lowering_identity u v hc
  have hsum := norm_sum_sq v
  nlinarith

/-- A computed coordinate-wise maximum supplies the operator estimate.
For the arithmetic shell, c_alpha is |coefficient_alpha|^2, with r_alpha
and l_alpha the displayed raising and lowering recurrence sums. -/
theorem diagonal_bound {κ : Type*} [Fintype κ]
    (u : ι → H) (v : ι → K) (c r l : κ → ℝ) (gamma : ℝ)
    (hc : ∀ i j, i ≠ j → inner ℝ (u i) (u j) = inner ℝ (v i) (v j))
    (hn : ∀ a, 0 ≤ c a)
    (hr : (∑ i, ‖u i‖ ^ 2) = ∑ a, r a * c a)
    (hl : (∑ i, ‖v i‖ ^ 2) = ∑ a, l a * c a)
    (hg : ∀ a, r a + ((Fintype.card ι : ℝ) - 1) * l a ≤ gamma) :
    ‖∑ i, u i‖ ^ 2 ≤ gamma * ∑ a, c a := by
  calc
    ‖∑ i, u i‖ ^ 2 ≤ (∑ i, ‖u i‖ ^ 2) +
        ((Fintype.card ι : ℝ) - 1) * ∑ i, ‖v i‖ ^ 2 := raising_bound u v hc
    _ = ∑ a, (r a + ((Fintype.card ι : ℝ) - 1) * l a) * c a := by
      rw [hr, hl, Finset.mul_sum, ← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl
      intro a _
      ring
    _ ≤ ∑ a, gamma * c a := Finset.sum_le_sum (fun a _ => mul_le_mul_of_nonneg_right (hg a) (hn a))
    _ = gamma * ∑ a, c a := (Finset.mul_sum _ _ _).symm

end SplitZero.IncidenceEstimate
