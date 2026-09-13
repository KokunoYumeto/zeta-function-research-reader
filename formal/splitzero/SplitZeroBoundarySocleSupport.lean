import SplitZeroBoundarySocle
import Mathlib.Data.Finset.Lattice.Fold

/-! Support integration of the actual derived boundary map. A present outer
label with an empty coefficient face is not the outer bottom. All transports
are those in the supplied original diagram; no injectivity is imposed on them. -/
noncomputable section
namespace SplitZero.BoundarySocleSupport
open SplitZero.Reconstruction
variable {R L : Type*} [CommRing R] [SemilatticeSup L] [OrderBot L]
variable {D : LinearDiagram R L}

def sourceRelations (D : LinearDiagram R L) (v : R) : Relations D where
  fibre i := BoundarySocle.sourceRel (M := D.V i) v
  stable := by
    rintro i j h x ⟨y, rfl⟩
    refine ⟨D.map h y, ?_⟩
    change v • D.map h y = D.map h (v • y)
    exact (map_smul (D.map h) v y).symm

def targetRelations (f : Hom D D) (v : R) : Relations D where
  fibre i := BoundarySocle.targetRel v (f.app i)
  stable := by
    rintro i j h x ⟨y, rfl⟩
    refine ⟨D.map h y, ?_⟩
    change v • f.app j (D.map h y) = D.map h (v • f.app i y)
    rw [f.naturality, map_smul]

def comparisonHom (f : Hom D D) (v : R) :
    Hom (sourceRelations D v).quotientDiagram (targetRelations f v).quotientDiagram where
  app i := BoundarySocle.comparison v (f.app i)
  naturality := by
    intro i j h x
    obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective ((sourceRelations D v).fibre i) x
    change ((targetRelations f v).fibre j).mkQ (f.app j (D.map h x)) =
      ((targetRelations f v).fibre j).mkQ (D.map h (f.app i x))
    rw [f.naturality]

/-- Both paths use the original internal quotient's total map. -/
theorem original_square (f : Hom D D) (v : R) :
    (comparisonHom f v).total.comp (sourceRelations D v).quotientMap.total =
      (targetRelations f v).quotientMap.total.comp f.total := by
  ext x
  rcases x with ⟨i,x⟩
  rfl

theorem total_injective (f : Hom D D) (v : R)
    (hf : ∀ i, Function.Injective (f.app i)) :
    Function.Injective (comparisonHom f v).total := by
  rintro ⟨i,x⟩ ⟨j,y⟩ h
  have hij : i = j := congrArg (fun z => z.fst) h
  subst j
  apply ((sourceRelations D v).quotientDiagram.same_label_eq i x y).mpr
  apply BoundarySocle.comparison_injective v (f.app i) (hf i)
  exact ((targetRelations f v).quotientDiagram.same_label_eq i _ _).mp h

/-- Exact image is the equalizer of v and supported zero, not external absence. -/
theorem range_iff_supported_killed (f : Hom D D) (v : R)
    (hv : ∀ i, Function.Injective (fun x : D.V i => v • x))
    (y : (targetRelations f v).quotientDiagram.Total) :
    (∃ x, (comparisonHom f v).total x = y) ↔
      (ofR v : G R) • y = (e : G R) • y := by
  constructor
  · rintro ⟨⟨i,x⟩, rfl⟩
    change (⟨i, v • BoundarySocle.comparison v (f.app i) x⟩ :
        (targetRelations f v).quotientDiagram.Total) =
        (e : G R) • ⟨i, BoundarySocle.comparison v (f.app i) x⟩
    rw [LinearDiagram.supported_zero_action, BoundarySocle.comparison_killed]
  · rcases y with ⟨i,y⟩
    intro h
    rw [LinearDiagram.ofR_smul, LinearDiagram.supported_zero_action] at h
    have hy : v • y = 0 :=
      ((targetRelations f v).quotientDiagram.same_label_eq i _ _).mp h
    let z : BoundarySocle.socle v (f.app i) := ⟨y, hy⟩
    obtain ⟨x,hx⟩ := BoundarySocle.toSocle_surjective v (f.app i) (hv i) z
    refine ⟨⟨i,x⟩, ?_⟩
    apply ((targetRelations f v).quotientDiagram.same_label_eq i _ _).mpr
    exact congrArg Subtype.val hx

/-- Fibre zero on an empty inner face survives at every nonbottom outer label. -/
theorem present_empty_face {J : Type*} [DecidableEq J]
    (F : LinearDiagram R (L × Finset J)) (i : L) (hi : i ≠ ⊥) :
    (⟨(i, ∅), 0⟩ : F.Total) ≠ 0 := by
  apply F.fibre_zero_ne_global
  intro h
  exact hi (congrArg Prod.fst h)

end SplitZero.BoundarySocleSupport
