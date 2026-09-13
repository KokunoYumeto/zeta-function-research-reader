import SplitZeroMetricSandwich
import SplitZeroMetricResolventSupport
import Mathlib.Data.Finset.Lattice.Fold

/-!
# Mixed support and full source pairings

Finite sums use the EXISTING Total addition, hence its actual join and
coefficient transports. Relations become the receiving fibre's zero.
Their Gram is a double sum; different support labels imply no orthogonality.
This is not a replacement tensor category or a new definition of SplitZero.
-/
noncomputable section
namespace SplitZero.MixedSupportMetric
open SplitZero.Reconstruction
open scoped BigOperators

section Supports
variable {R L ι : Type*} [CommRing R] [SemilatticeSup L] [OrderBot L]
variable {D : LinearDiagram R L}

/-- Exact support of a finite sum, including the empty sum. -/
theorem sum_support (s : Finset ι) (x : ι → D.Total) :
    (∑ a ∈ s, x a).fst = s.sup (fun a => (x a).fst) := by
  classical
  induction s using Finset.induction_on with
  | empty => rfl
  | @insert a s ha ih =>
    rw [Finset.sum_insert ha, Finset.sup_insert]
    change (x a).fst ⊔ (∑ b ∈ s, x b).fst = _
    rw [ih]

/-- Even a zero supported coefficient retains its input support. -/
theorem supported_scalar_label (r : R) (x : D.Total) :
    ((ofR r : G R) • x).fst = x.fst := by
  rcases x with ⟨i,v⟩
  rfl

/-- Original coefficient signs and zeros cannot delete a support slot. -/
theorem weighted_sum_support (s : Finset ι) (x : ι → D.Total) (c : ι → R) :
    (∑ a ∈ s, (ofR (c a) : G R) • x a).fst = s.sup (fun a => (x a).fst) := by
  rw [sum_support]
  exact Finset.sup_congr rfl (fun a _ha => supported_scalar_label (c a) (x a))

/-- A sum of fibre zeros retains the join, not external absence. -/
theorem sum_fibre_zeros (s : Finset ι) (i : ι → L) :
    (∑ a ∈ s, (⟨i a, 0⟩ : D.Total)) = ⟨s.sup i, 0⟩ := by
  classical
  induction s using Finset.induction_on with
  | empty => rfl
  | @insert a s ha ih =>
    rw [Finset.sum_insert ha, ih, Finset.sup_insert]
    change (⟨i a ⊔ s.sup i, D.map _ 0 + D.map _ 0⟩ : D.Total) = ⟨_, 0⟩
    simp only [map_zero, add_zero]

/-- The original quotient sends a mixed family of original relations to its join zero. -/
theorem quotient_sum_relations (B : Relations D) (s : Finset ι) (i : ι → L)
    (v : ∀ a, D.V (i a)) (hv : ∀ a ∈ s, v a ∈ B.fibre (i a)) :
    B.quotientMap.total (∑ a ∈ s, (⟨i a, v a⟩ : D.Total)) =
      (⟨s.sup i, 0⟩ : B.quotientDiagram.Total) := by
  rw [map_sum]
  calc
    _ = ∑ a ∈ s, (⟨i a, 0⟩ : B.quotientDiagram.Total) := by
      apply Finset.sum_congr rfl
      intro a ha
      exact B.relation_maps_to_fibre_zero (i a) (v a) (hv a ha)
    _ = _ := sum_fibre_zeros s i

/-- The same joined quotient equation for the original signed scalar action. -/
theorem weighted_relation_sum (B : Relations D) (s : Finset ι) (i : ι → L)
    (v : ∀ a, D.V (i a)) (c : ι → R)
    (hv : ∀ a ∈ s, v a ∈ B.fibre (i a)) :
    B.quotientMap.total (∑ a ∈ s, (ofR (c a) : G R) • (⟨i a,v a⟩ : D.Total)) =
      (⟨s.sup i,0⟩ : B.quotientDiagram.Total) :=
  quotient_sum_relations B s i (fun a => c a • v a)
    (fun a ha => (B.fibre (i a)).smul_mem (c a) (hv a ha))

/-- A nonbottom mixed join is not made absent even if every amplitude cancels. -/
theorem quotient_sum_not_absent (B : Relations D) (s : Finset ι) (i : ι → L)
    (v : ∀ a, D.V (i a)) (hv : ∀ a ∈ s, v a ∈ B.fibre (i a))
    (hjoin : s.sup i ≠ ⊥) :
    B.quotientMap.total (∑ a ∈ s, (⟨i a, v a⟩ : D.Total)) ≠ 0 := by
  rw [quotient_sum_relations B s i v hv]
  exact B.quotientDiagram.fibre_zero_ne_global hjoin

/-- Equality of mixed sums uses original relation membership in EVERY input fibre. -/
theorem quotient_sum_congr (B : Relations D) (s : Finset ι) (i : ι → L)
    (v₀ v₁ : ∀ a, D.V (i a))
    (hd : ∀ a ∈ s, v₁ a - v₀ a ∈ B.fibre (i a)) :
    B.quotientMap.total (∑ a ∈ s, (⟨i a, v₁ a⟩ : D.Total)) =
      B.quotientMap.total (∑ a ∈ s, (⟨i a, v₀ a⟩ : D.Total)) := by
  rw [map_sum, map_sum]
  apply Finset.sum_congr rfl
  intro a ha
  exact (B.quotient_same_label_iff (i a) _ _).mpr (hd a ha)

/-- All transports into a common support act before adding relations. -/
theorem transported_relation_sum (B : Relations D) (s : Finset ι) (i : ι → L)
    (J : L) (h : ∀ a, i a ≤ J) (v : ∀ a, D.V (i a))
    (hv : ∀ a ∈ s, v a ∈ B.fibre (i a)) :
    (∑ a ∈ s, D.map (h a) (v a)) ∈ B.fibre J := by
  exact (B.fibre J).sum_mem (fun a ha => B.stable (h a) (hv a ha))

/-- The exact zero criterion tests the transported SUM, not its summands separately. -/
theorem gathered_zero_iff (B : Relations D) (s : Finset ι) (i : ι → L)
    (J : L) (h : ∀ a, i a ≤ J) (v : ∀ a, D.V (i a)) :
    B.quotientMap.total (⟨J,∑ a ∈ s, D.map (h a) (v a)⟩ : D.Total) =
      B.quotientMap.total (⟨J,0⟩ : D.Total) ↔
      (∑ a ∈ s, D.map (h a) (v a)) ∈ B.fibre J := by
  simpa only [sub_zero] using
    B.quotient_same_label_iff J (∑ a ∈ s, D.map (h a) (v a)) 0

end Supports

section Grams
open Matrix MetricVariation
variable {j n ι : Type*} [Fintype j]

/-- The complete polarized source Gram, including all off-diagonal support terms. -/
theorem gram_finite_sum (M : Matrix j j ℂ) (s : Finset ι)
    (F : ι → Matrix j n ℂ) :
    MetricVariation.gram M (∑ a ∈ s, F a) =
      ∑ a ∈ s, ∑ b ∈ s, (F a).conjTranspose * M * F b := by
  simp only [MetricVariation.gram, Matrix.conjTranspose_sum, Matrix.sum_mul, Matrix.mul_sum]
  rw [Finset.sum_comm]

variable {L : Type*} [SemilatticeSup L] [OrderBot L] {D : LinearDiagram ℂ L}

/-- Columns are transported from their original labels before the Gram observation. -/
def transportedColumns (i : ι → L) (J : L) (h : ∀ a, i a ≤ J)
    (coord : D.V J ≃ₗ[ℂ] (j → ℂ)) (F : ∀ a, n → D.V (i a)) :
    ι → Matrix j n ℂ :=
  fun a row col => coord (D.map (h a) (F a col)) row

/-- The full mixed amplitude at the explicitly supplied common support. -/
def gatheredColumns (s : Finset ι) (i : ι → L) (J : L) (h : ∀ a, i a ≤ J)
    (coord : D.V J ≃ₗ[ℂ] (j → ℂ)) (F : ∀ a, n → D.V (i a)) : Matrix j n ℂ :=
  fun row col => coord (∑ a ∈ s, D.map (h a) (F a col)) row

omit [Fintype j] in
theorem gathered_eq_sum (s : Finset ι) (i : ι → L) (J : L) (h : ∀ a, i a ≤ J)
    (coord : D.V J ≃ₗ[ℂ] (j → ℂ)) (F : ∀ a, n → D.V (i a)) :
    gatheredColumns s i J h coord F = ∑ a ∈ s, transportedColumns i J h coord F a := by
  ext row col
  simp only [gatheredColumns, map_sum, Matrix.sum_apply, Finset.sum_apply, transportedColumns]

/-- Formula for the actual mixed-source observation, not just independent fibre Grams. -/
theorem gathered_gram (M : Matrix j j ℂ) (s : Finset ι) (i : ι → L) (J : L)
    (h : ∀ a, i a ≤ J) (coord : D.V J ≃ₗ[ℂ] (j → ℂ))
    (F : ∀ a, n → D.V (i a)) :
    MetricVariation.gram M (gatheredColumns s i J h coord F) =
      ∑ a ∈ s, ∑ b ∈ s,
        (transportedColumns i J h coord F a).conjTranspose * M *
          transportedColumns i J h coord F b := by
  rw [gathered_eq_sum]
  exact gram_finite_sum M s _

/-- Each column still has the original relation witness at the receiving support. -/
theorem gathered_column_boundary (B : Relations D) (s : Finset ι) (i : ι → L)
    (J : L) (h : ∀ a, i a ≤ J) (F : ∀ a, n → D.V (i a))
    (hF : ∀ a ∈ s, ∀ col, F a col ∈ B.fibre (i a)) (col : n) :
    B.quotientMap.total (⟨J, ∑ a ∈ s, D.map (h a) (F a col)⟩ : D.Total) =
      (⟨J, 0⟩ : B.quotientDiagram.Total) :=
  B.relation_maps_to_fibre_zero J _
    (transported_relation_sum B s i J h (fun a => F a col) (fun a ha => hF a ha col))

end Grams

section Canonical
open Matrix MetricVariation
variable {L ι j n m : Type*} [SemilatticeSup L] [OrderBot L]
  [Fintype j] [Fintype n] [Fintype m] [DecidableEq m]
variable {D : LinearDiagram ℂ L}

/-- Canonical metric changes at distinct supports preserve the sum's original class. -/
theorem mixed_canonical_classes (Brel : Relations D) (s : Finset ι) (i : ι → L)
    (coord : ∀ a, D.V (i a) ≃ₗ[ℂ] (j → ℂ))
    (B : ι → Matrix j m ℂ) (C : ι → Matrix j n ℂ)
    (M₀ M₁ : ∀ a, Metric (B a))
    (hB : ∀ a w, (coord a).symm (B a *ᵥ w) ∈ Brel.fibre (i a))
    (v : ι → n → ℂ) :
    Brel.quotientMap.total
      (∑ a ∈ s, (⟨i a, (coord a).symm ((M₁ a).sectionMap (C a) *ᵥ v a)⟩ : D.Total)) =
    Brel.quotientMap.total
      (∑ a ∈ s, (⟨i a, (coord a).symm ((M₀ a).sectionMap (C a) *ᵥ v a)⟩ : D.Total)) := by
  rw [map_sum, map_sum]
  apply Finset.sum_congr rfl
  intro a _ha
  exact MetricResolventSupport.original_class_unchanged
    Brel (i a) (coord a) (C a) (M₀ a) (M₁ a) (hB a) (v a)

end Canonical
end SplitZero.MixedSupportMetric
