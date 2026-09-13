import SplitZeroMetricVariation
import SplitZeroInternalQuotient

/-!
# Metric variation in the original SplitZero quotient

Raw fibre sections are not presumed natural. Boundary-valued naturality
is proved sufficient to construct a Hom into the existing quotient diagram.
An explicit change by old relations gives equality of actual G(R)-linear
maps on totals. The matrix theorem uses the primitive from MetricVariation.
-/
noncomputable section
namespace SplitZero.MetricVariationSupport
open SplitZero.Reconstruction
universe u v
variable {R : Type u} [CommRing R] {L : Type v}
  [SemilatticeSup L] [OrderBot L] {D E : LinearDiagram R L}

/-- A coefficient section descends when its stated transport error is an old boundary. -/
def quotientSection (B : Relations D) (r : ∀ i, E.V i →ₗ[R] D.V i)
    (hn : ∀ {i j} (h : i ≤ j) v,
      D.map h (r i v) - r j (E.map h v) ∈ B.fibre j) :
    Hom E B.quotientDiagram where
  app i := (B.fibre i).mkQ.comp (r i)
  naturality h v := by
    symm
    change (B.fibre _).mkQ (D.map h (r _ v)) =
      (B.fibre _).mkQ (r _ (E.map h v))
    exact (Submodule.Quotient.eq _).mpr (hn h v)

/-- Naturality modulo B survives any specified B-valued change of section. -/
theorem perturbed_naturality (B : Relations D)
    (r₀ r₁ : ∀ i, E.V i →ₗ[R] D.V i)
    (h₀ : ∀ {i j} (h : i ≤ j) v,
      D.map h (r₀ i v) - r₀ j (E.map h v) ∈ B.fibre j)
    (hd : ∀ i v, r₁ i v - r₀ i v ∈ B.fibre i)
    {i j} (h : i ≤ j) (v : E.V i) :
    D.map h (r₁ i v) - r₁ j (E.map h v) ∈ B.fibre j := by
  have he : D.map h (r₁ i v) - r₁ j (E.map h v) =
      (D.map h (r₀ i v) - r₀ j (E.map h v)) +
        D.map h (r₁ i v - r₀ i v) - (r₁ j (E.map h v) - r₀ j (E.map h v)) := by
    rw [map_sub]
    abel
  rw [he]
  exact (B.fibre j).sub_mem ((B.fibre j).add_mem (h₀ h v) (B.stable h (hd i v)))
    (hd j (E.map h v))

/-- Equality is in the original semimodule of classes, not just its finite observation. -/
theorem quotientSection_independent (B : Relations D)
    (r₀ r₁ : ∀ i, E.V i →ₗ[R] D.V i)
    (h₀ : ∀ {i j} (h : i ≤ j) v,
      D.map h (r₀ i v) - r₀ j (E.map h v) ∈ B.fibre j)
    (hd : ∀ i v, r₁ i v - r₀ i v ∈ B.fibre i) :
    (quotientSection B r₁ (perturbed_naturality B r₀ r₁ h₀ hd)).total =
      (quotientSection B r₀ h₀).total := by
  apply LinearMap.ext
  rintro ⟨i,v⟩
  change B.quotientMap.total ⟨i,r₁ i v⟩ = B.quotientMap.total ⟨i,r₀ i v⟩
  exact (B.quotient_same_label_iff i _ _).mpr (hd i v)

/-- An explicit boundary has a supported-zero image at its own nonbottom label. -/
theorem boundary_retained (B : Relations D) (i : L) (hi : i ≠ ⊥)
    (v : D.V i) (hv : v ∈ B.fibre i) :
    B.quotientMap.total ⟨i,v⟩ = (⟨i,0⟩ : B.quotientDiagram.Total) ∧
    B.quotientMap.total ⟨i,v⟩ ≠ 0 := by
  refine ⟨B.relation_maps_to_fibre_zero i v hv, ?_⟩
  intro h
  have := congrArg (fun z : B.quotientDiagram.Total => z.fst) h
  exact hi this

section Matrix
variable {j n m : Type*} [Fintype j] [Fintype n] [Fintype m] [DecidableEq m]
  {D : LinearDiagram ℂ L}

/-- The actual metric correction, after the specified source-coordinate equivalence. -/
theorem canonical_metric_class (Brel : Relations D) (i : L)
    (coord : D.V i ≃ₗ[ℂ] (j → ℂ))
    (B : Matrix j m ℂ) (C : Matrix j n ℂ)
    (M₀ M₁ : MetricVariation.Metric B)
    (hB : ∀ w, coord.symm (B *ᵥ w) ∈ Brel.fibre i) (v : n → ℂ) :
    Brel.quotientMap.total ⟨i,coord.symm (M₁.sectionMap C *ᵥ v)⟩ =
      Brel.quotientMap.total ⟨i,coord.symm (M₀.sectionMap C *ᵥ v)⟩ := by
  apply (Brel.quotient_same_label_iff i _ _).mpr
  rw [← map_sub, ← Matrix.sub_mulVec, MetricVariation.Metric.section_difference]
  rw [← Matrix.mulVec_mulVec]
  exact hB _

end Matrix
end SplitZero.MetricVariationSupport
