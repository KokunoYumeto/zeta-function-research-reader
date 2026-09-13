import SplitZeroSourcePresentation

/-!
# Period coordinates inside the original support diagram

Given the specified coefficient isomorphisms (for example a proved invertible
period matrix), construct the target transports by conjugating the original
ones. The result is an equivalence over G R, not just an amplitude isomorphism.
The existence of the analytic period isomorphisms is an explicit input.
-/
noncomputable section
namespace SplitZero.Integration
open SplitZero.Reconstruction

universe u v w w'
variable {R : Type u} [CommRing R] {L : Type v}
  [SemilatticeSup L] [OrderBot L]
  (E : LinearDiagram.{u,v,w} R L)
  (W : L → Type w') [∀ i, AddCommGroup (W i)] [∀ i, Module R (W i)]
  (Phi : ∀ i, E.V i ≃ₗ[R] W i)

/-- All original coefficient transports are conjugated, not replaced by identities. -/
def periodDiagram : LinearDiagram R L where
  V := W
  map {i j} h := (Phi j).toLinearMap.comp ((E.map h).comp (Phi i).symm.toLinearMap)
  map_id i := by
    apply LinearMap.ext
    intro x
    change Phi i (E.map (le_refl i) ((Phi i).symm x)) = x
    rw [E.map_self, (Phi i).apply_symm_apply]
  map_comp {i j k} h h' := by
    apply LinearMap.ext
    intro x
    change Phi k (E.map h' ((Phi j).symm (Phi j (E.map h ((Phi i).symm x))))) =
      Phi k (E.map (le_trans h h') ((Phi i).symm x))
    rw [(Phi j).symm_apply_apply, E.map_map]

def periodForward : Hom E (periodDiagram E W Phi) where
  app i := (Phi i).toLinearMap
  naturality {i j} h x := by
    change Phi j (E.map h x) = Phi j (E.map h ((Phi i).symm (Phi i x)))
    rw [(Phi i).symm_apply_apply]

def periodBackward : Hom (periodDiagram E W Phi) E where
  app i := (Phi i).symm.toLinearMap
  naturality {i j} h x := by
    change (Phi j).symm (Phi j (E.map h ((Phi i).symm x))) =
      E.map h ((Phi i).symm x)
    rw [(Phi j).symm_apply_apply]

/-- Both inverse laws and the complete original scalar action are retained. -/
def periodTotalEquiv : E.Total ≃ₗ[G R] (periodDiagram E W Phi).Total where
  toFun := (periodForward E W Phi).total
  invFun := (periodBackward E W Phi).total
  left_inv := by
    rintro ⟨i, x⟩
    change (⟨i, (Phi i).symm (Phi i x)⟩ : E.Total) = ⟨i, x⟩
    rw [(Phi i).symm_apply_apply]
  right_inv := by
    rintro ⟨i, x⟩
    change (⟨i, Phi i ((Phi i).symm x)⟩ : (periodDiagram E W Phi).Total) = ⟨i, x⟩
    rw [(Phi i).apply_symm_apply]
  map_add' := (periodForward E W Phi).total.map_add
  map_smul' := (periodForward E W Phi).total.map_smul

@[simp] theorem periodTotal_apply (i : L) (x : E.V i) :
    periodTotalEquiv E W Phi (⟨i, x⟩ : E.Total) = ⟨i, Phi i x⟩ := rfl

theorem period_preserves_support (x : E.Total) :
    (periodTotalEquiv E W Phi x).fst = x.fst := rfl

theorem period_supported_zero (i : L) :
    periodTotalEquiv E W Phi (⟨i, 0⟩ : E.Total) = ⟨i, 0⟩ := by
  rw [periodTotal_apply, map_zero]
  rfl

theorem period_absence :
    periodTotalEquiv E W Phi 0 = 0 := (periodTotalEquiv E W Phi).map_zero

/-- The original action, with the same transports, in period coordinates. -/
def periodAction (A : Hom E E) : Hom (periodDiagram E W Phi) (periodDiagram E W Phi) :=
  Hom.comp (periodForward E W Phi) (Hom.comp A (periodBackward E W Phi))

theorem period_action_square (A : Hom E E) :
    (periodAction E W Phi A).total.comp (periodForward E W Phi).total =
      (periodForward E W Phi).total.comp A.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  change (⟨i, Phi i (A.app i ((Phi i).symm (Phi i x)))⟩ :
    (periodDiagram E W Phi).Total) = ⟨i, Phi i (A.app i x)⟩
  rw [(Phi i).symm_apply_apply]

section OriginalSource
variable {D : LinearDiagram R L} (J : Hom D E)

def periodObservation : Hom D (periodDiagram E W Phi) :=
  Hom.comp (periodForward E W Phi) J

/-- Period coordinates add no kernel to the finite observation, but erase none of it. -/
theorem period_observation_kernel (i : L) (x : D.V i) :
    (periodObservation E W Phi J).app i x = 0 ↔ J.app i x = 0 := by
  change Phi i (J.app i x) = 0 ↔ J.app i x = 0
  constructor
  · intro h
    apply (Phi i).injective
    rw [h, map_zero]
  · intro h
    rw [h, map_zero]

/-- Exact total composite through the already constructed internal quotient. -/
theorem period_quotient_square (B : Relations D)
    (hB : ∀ i x, x ∈ B.fibre i → J.app i x = 0) :
    (periodForward E W Phi).total.comp (observation J B hB) =
      observation (periodObservation E W Phi J) B
        (fun i x hx => (period_observation_kernel E W Phi J i x).mpr (hB i x hx)) := by
  apply LinearMap.ext
  intro y
  obtain ⟨⟨i, x⟩, rfl⟩ := B.quotient_surjective y
  change (periodForward E W Phi).total (observation J B hB (B.quotientMap.total ⟨i, x⟩)) = _
  rw [observed_class, observed_class]
  rfl

end OriginalSource
end SplitZero.Integration
