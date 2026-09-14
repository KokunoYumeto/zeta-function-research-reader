import SplitZeroObservedIterates
import SplitZeroRestrictedBoundary

/-!
# The observed-iterate quotient on the ORIGINAL support reconstruction

The new relation is explicitly an observation kernel, not an assertion that
it equals the original theta boundary. Noninjective support transports are
allowed. Both the old one-step kernel and its action-stable submodule remain.
-/
noncomputable section
namespace SplitZero.ObservedIterates
open SplitZero.Reconstruction

universe u v
variable {R : Type u} [CommRing R] {L : Type v}
  [SemilatticeSup L] [OrderBot L]
  {D E : LinearDiagram R L}

/-- The original one-step observation kernel, with its actual transports. -/
def rawRelations (obs : Hom D E) : Relations D where
  fibre i := LinearMap.ker (obs.app i)
  stable {i j} h {x} hx := by
    change obs.app j (D.map h x) = 0
    rw [obs.naturality, hx, map_zero]

/-- All iterates are checked in each fibre before the original reconstruction. -/
def invisibleRelations (obs : Hom D E) (A : Hom D D) : Relations D where
  fibre i := invisible (obs.app i) (A.app i)
  stable {i j} h {x} hx := by
    apply (mem_invisible (obs.app j) (A.app j) (D.map h x)).mpr
    intro n
    have hp := powers_intertwine (D.map h) (A.app i) (A.app j)
      (fun y => (A.naturality h y).symm) n x
    rw [← hp, obs.naturality, (mem_invisible (obs.app i) (A.app i) x).mp hx n,
      map_zero]

/-- A new quotient action only after proving stability of the retained relation. -/
def actionHom (obs : Hom D E) (A : Hom D D) :
    Hom (invisibleRelations obs A).quotientDiagram
      (invisibleRelations obs A).quotientDiagram where
  app i := quotientAction (obs.app i) (A.app i)
  naturality h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x =>
      change (invisible (obs.app _) (A.app _)).mkQ (A.app _ (D.map h x)) =
        (invisible (obs.app _) (A.app _)).mkQ (D.map h (A.app _ x))
      rw [A.naturality]

/-- The first observation descends, without being declared injective. -/
def observationHom (obs : Hom D E) (A : Hom D D) :
    Hom (invisibleRelations obs A).quotientDiagram E where
  app i := (invisible (obs.app i) (A.app i)).liftQ (obs.app i)
    (invisible_le_kernel (obs.app i) (A.app i))
  naturality h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x => exact obs.naturality h x

/-- Forgetting the additional iterate data has its own receiving quotient. -/
def forgetIterates (obs : Hom D E) (A : Hom D D) :
    Hom (invisibleRelations obs A).quotientDiagram (rawRelations obs).quotientDiagram where
  app i := (invisible (obs.app i) (A.app i)).mapQ (LinearMap.ker (obs.app i))
    LinearMap.id (fun _ hx => invisible_le_kernel (obs.app i) (A.app i) hx)
  naturality h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x => rfl

theorem action_square (obs : Hom D E) (A : Hom D D) :
    (actionHom obs A).total.comp (invisibleRelations obs A).quotientMap.total =
      (invisibleRelations obs A).quotientMap.total.comp A.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  rfl

theorem observation_square (obs : Hom D E) (A : Hom D D) :
    (observationHom obs A).total.comp (invisibleRelations obs A).quotientMap.total =
      obs.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  rfl

theorem forget_square (obs : Hom D E) (A : Hom D D) :
    (forgetIterates obs A).total.comp (invisibleRelations obs A).quotientMap.total =
      (rawRelations obs).quotientMap.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  rfl

/-- A one-step-zero vector can remain nonzero once its future observations are retained. -/
theorem transient_kernel_retained (obs : Hom D E) (A : Hom D D)
    (i : L) (x : D.V i) (h0 : obs.app i x = 0)
    (hfuture : x ∉ invisible (obs.app i) (A.app i)) :
    (invisibleRelations obs A).quotientMap.total ⟨i, x⟩ ≠
        (⟨i, 0⟩ : (invisibleRelations obs A).quotientDiagram.Total) ∧
      (observationHom obs A).total
        ((invisibleRelations obs A).quotientMap.total ⟨i, x⟩) =
        (⟨i, 0⟩ : E.Total) := by
  constructor
  · intro hz
    have hq : (invisible (obs.app i) (A.app i)).mkQ x = 0 :=
      ((invisibleRelations obs A).quotientDiagram.same_label_eq i _ _).mp hz
    exact hfuture ((Submodule.Quotient.mk_eq_zero _).mp hq)
  · change (⟨i, obs.app i x⟩ : E.Total) = ⟨i, 0⟩
    rw [h0]

/-- Vanishing is tested against e in the receiving fibre, never against global absence. -/
theorem observed_zero_iff (obs : Hom D E) (A : Hom D D) (i : L) (x : D.V i) :
    (observationHom obs A).total
      ((invisibleRelations obs A).quotientMap.total ⟨i, x⟩) =
        (⟨i, 0⟩ : E.Total) ↔ obs.app i x = 0 :=
  E.same_label_eq i (obs.app i x) 0

theorem observed_output_not_absent (obs : Hom D E) (A : Hom D D)
    (i : L) (x : D.V i) (hi : i ≠ ⊥) :
    (observationHom obs A).total
      ((invisibleRelations obs A).quotientMap.total ⟨i, x⟩) ≠ 0 := by
  intro h
  exact hi (congrArg (fun y : E.Total => y.fst) h)

/-- Original mixed-support inner faces are preserved by the inherited theorem. -/
theorem present_empty_face {J : Type*} [DecidableEq J]
    (F : LinearDiagram R (L × Finset J)) (i : L) (hi : i ≠ ⊥) :
    (⟨(i, ∅), 0⟩ : F.Total) ≠ 0 :=
  RestrictedBoundary.present_empty_residual F i hi

end SplitZero.ObservedIterates
