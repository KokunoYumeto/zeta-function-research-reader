import SplitZeroSupportChangeIntegration
import SplitZeroInternalQuotient
import SplitZeroMaps

/-!
# Quotient transport on the original SplitZero reconstruction

No scalar, carrier, relation quotient, or support-changing map is redefined.
The new descent is an instance of the existing HomOver and Relations APIs.
Nonbottom support is stated explicitly where absence is excluded.
-/
noncomputable section
namespace SplitZero.Integration
open SplitZero.Reconstruction

universe u v w
variable {R : Type u} [CommRing R]
  {L : Type v} {K : Type w}
  [SemilatticeSup L] [OrderBot L] [SemilatticeSup K] [OrderBot K]
  {D : LinearDiagram R L} {E : LinearDiagram R K}
  {f : SupportMap L K}

/-- Both relation families are retained in the support-changing quotient map. -/
def descendOver (a : HomOver D E f) (B : Relations D) (C : Relations E)
    (ha : ∀ i x, x ∈ B.fibre i → a.app i x ∈ C.fibre (f.toFun i)) :
    HomOver B.quotientDiagram C.quotientDiagram f where
  app i := (B.fibre i).mapQ (C.fibre (f.toFun i)) (a.app i) (ha i)
  naturality h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x =>
      change (C.fibre _).mkQ (a.app _ (D.map h x)) =
        (C.fibre _).mkQ (E.map (f.monotone h) (a.app _ x))
      rw [a.naturality]

/-- The total square commutes before applying any amplitude observation. -/
theorem quotient_square (a : HomOver D E f) (B : Relations D) (C : Relations E)
    (ha : ∀ i x, x ∈ B.fibre i → a.app i x ∈ C.fibre (f.toFun i)) :
    (descendOver a B C ha).total.comp B.quotientMap.total =
      C.quotientMap.total.comp a.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  rfl

/-- Exact receiving-boundary criterion, with the receiving support unchanged. -/
theorem quotient_killed_iff (a : HomOver D E f) (B : Relations D) (C : Relations E)
    (ha : ∀ i x, x ∈ B.fibre i → a.app i x ∈ C.fibre (f.toFun i))
    (i : L) (x : D.V i) :
    (descendOver a B C ha).total (B.quotientMap.total ⟨i, x⟩) =
      (⟨f.toFun i, 0⟩ : C.quotientDiagram.Total) ↔
      a.app i x ∈ C.fibre (f.toFun i) := by
  change (⟨f.toFun i, (C.fibre _).mkQ (a.app i x)⟩ :
    C.quotientDiagram.Total) = ⟨f.toFun i, 0⟩ ↔ _
  rw [C.quotientDiagram.same_label_eq]
  exact Submodule.Quotient.mk_eq_zero _

/-- A class nonzero in the original quotient remains recorded there. -/
theorem source_class_nonzero (B : Relations D) (i : L) (x : D.V i)
    (hx : x ∉ B.fibre i) :
    B.quotientMap.total ⟨i, x⟩ ≠ (⟨i, 0⟩ : B.quotientDiagram.Total) := by
  intro h
  have hq : (B.fibre i).mkQ x = 0 :=
    (B.quotientDiagram.same_label_eq i _ _).mp h
  exact hx ((Submodule.Quotient.mk_eq_zero _).mp hq)

/-- This does not assume that a general support map reflects bottom. -/
theorem quotient_output_not_absent
    (a : HomOver D E f) (B : Relations D) (C : Relations E)
    (ha : ∀ i x, x ∈ B.fibre i → a.app i x ∈ C.fibre (f.toFun i))
    (i : L) (x : D.V i) (hi : f.toFun i ≠ ⊥) :
    (descendOver a B C ha).total (B.quotientMap.total ⟨i, x⟩) ≠ 0 := by
  intro h
  exact hi (congrArg (fun y : C.quotientDiagram.Total => y.fst) h)

/-- Codex's SupBotHom presentation feeds the same quotient constructor. -/
def asHomOver (a : ReindexedHom D E) :
    HomOver D E
      { toFun := a.index, map_sup := map_sup a.index, map_bot := map_bot a.index } where
  app := a.app
  naturality := a.naturality

theorem asHomOver_total (a : ReindexedHom D E) :
    (asHomOver a).total = a.total := rfl

section FixedSupport
variable {E' : LinearDiagram R L}

/-- The established terminal amplitude observation, not a new projection. -/
theorem observe_natural [OrderTop L] (a : Hom D E') (x : D.Total) :
    E'.observe (a.total x) = a.app ⊤ (D.observe x) := by
  rcases x with ⟨i, x⟩
  exact (a.naturality le_top x).symm

/-- The original coefficient quotient commutes with scalar extension. -/
theorem coefficient_square {S : Type*} [CommRing S] (j : R →+* S) :
    SplitZero.reflect.comp (SplitZero.Maps.liftRingHom j) =
      j.comp SplitZero.reflect :=
  SplitZero.Maps.reflection_natural j

end FixedSupport
end SplitZero.Integration
