import SplitZeroQuotientTransport

/-!
# Original relations, finite observations, and non-natural representatives

The kernel of a finite observation is not identified with the original
boundary submodule. Representatives need only be fibrewise sections; their
failure of naturality is recorded explicitly before taking any quotient.
-/
noncomputable section
namespace SplitZero.Integration
open SplitZero.Reconstruction

universe u v
variable {R : Type u} [CommRing R] {L : Type v}
  [SemilatticeSup L] [OrderBot L]
  {D E : LinearDiagram R L}

/-- The further observation kernel, separately from the original relations. -/
def kernelRelations (J : Hom D E) : Relations D where
  fibre i := LinearMap.ker (J.app i)
  stable := by
    intro i j h x hx
    change J.app j (D.map h x) = 0
    change J.app i x = 0 at hx
    rw [J.naturality, hx, map_zero]

/-- Use the existing universal internal quotient, with its original source. -/
def observation (J : Hom D E) (B : Relations D)
    (hB : ∀ i x, x ∈ B.fibre i → J.app i x = 0) :
    B.quotientDiagram.Total →ₗ[G R] E.Total :=
  B.descend J.total (by
    intro i x hx
    change (⟨i, J.app i x⟩ : E.Total) = ⟨i, J.app i 0⟩
    rw [hB i x hx, map_zero])

theorem observed_class (J : Hom D E) (B : Relations D)
    (hB : ∀ i x, x ∈ B.fibre i → J.app i x = 0)
    (i : L) (x : D.V i) :
    observation J B hB (B.quotientMap.total ⟨i, x⟩) = ⟨i, J.app i x⟩ :=
  B.descend_quotient J.total _ ⟨i, x⟩

/-- It is the full finite-observation kernel, not just the boundary module. -/
theorem observation_kernel (J : Hom D E) (B : Relations D)
    (hB : ∀ i x, x ∈ B.fibre i → J.app i x = 0)
    (i : L) (x : D.V i) :
    observation J B hB (B.quotientMap.total ⟨i, x⟩) =
      (⟨i, 0⟩ : E.Total) ↔ J.app i x = 0 := by
  rw [observed_class, E.same_label_eq]

/-- The extra quotient is constructed only after retaining the original one. -/
def forgetToKernel (J : Hom D E) (B : Relations D)
    (hB : ∀ i x, x ∈ B.fibre i → J.app i x = 0) :
    Hom B.quotientDiagram (kernelRelations J).quotientDiagram where
  app i := (B.fibre i).mapQ (LinearMap.ker (J.app i)) LinearMap.id
    (fun x hx => hB i x hx)
  naturality h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x => rfl

theorem two_stage_square (J : Hom D E) (B : Relations D)
    (hB : ∀ i x, x ∈ B.fibre i → J.app i x = 0) :
    (forgetToKernel J B hB).total.comp B.quotientMap.total =
      (kernelRelations J).quotientMap.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  rfl

/-- A non-boundary may be killed by a further observation while staying present. -/
theorem retained_observation_kernel (J : Hom D E) (B : Relations D)
    (hB : ∀ i x, x ∈ B.fibre i → J.app i x = 0)
    (i : L) (x : D.V i) (hx : x ∉ B.fibre i) (hj : J.app i x = 0)
    (hi : i ≠ ⊥) :
    B.quotientMap.total ⟨i, x⟩ ≠ (⟨i, 0⟩ : B.quotientDiagram.Total) ∧
    observation J B hB (B.quotientMap.total ⟨i, x⟩) = (⟨i, 0⟩ : E.Total) ∧
    observation J B hB (B.quotientMap.total ⟨i, x⟩) ≠ 0 := by
  refine ⟨source_class_nonzero B i x hx, ?_, ?_⟩
  · exact (observation_kernel J B hB i x).mpr hj
  · rw [observed_class, hj]
    exact E.fibre_zero_ne_global hi

section Representatives
variable (J : Hom D E) (r : ∀ i, E.V i →ₗ[R] D.V i)
  (hr : ∀ i v, J.app i (r i v) = v)

/-- No naturality of the chosen section is imposed. -/
def sectionDefect {i j : L} (h : i ≤ j) : E.V i →ₗ[R] D.V j :=
  (D.map h).comp (r i) - (r j).comp (E.map h)

theorem sectionDefect_killed {i j : L} (h : i ≤ j) (v : E.V i) :
    J.app j (sectionDefect r h v) = 0 := by
  change J.app j (D.map h (r i v) - r j (E.map h v)) = 0
  rw [map_sub, J.naturality, hr, hr, sub_self]

/-- Compatibility across two enlargements keeps the actual source error. -/
theorem sectionDefect_cocycle {i j k : L} (h : i ≤ j) (h' : j ≤ k)
    (v : E.V i) :
    sectionDefect r (le_trans h h') v =
      D.map h' (sectionDefect r h v) + sectionDefect r h' (E.map h v) := by
  change D.map _ (r i v) - r k (E.map _ v) =
    D.map h' (D.map h (r i v) - r j (E.map h v)) +
      (D.map h' (r j (E.map h v)) - r k (E.map h' (E.map h v)))
  rw [map_sub, D.map_map, E.map_map]
  abel

/-- Naturality modulo original relations requires this extra, stated input. -/
theorem section_natural_mod (B : Relations D) {i j : L} (h : i ≤ j)
    (v : E.V i) (hv : sectionDefect r h v ∈ B.fibre j) :
    B.quotientMap.total ⟨j, D.map h (r i v)⟩ =
      B.quotientMap.total ⟨j, r j (E.map h v)⟩ :=
  (B.quotient_same_label_iff j _ _).mpr hv

/-- Includes the residue insertion operator as A; no naturality is invented. -/
def liftOperator (A : Hom E E) (i : L) : D.V i →ₗ[R] D.V i :=
  (r i).comp ((A.app i).comp (J.app i))

theorem liftOperator_observed (A : Hom E E) (i : L) (x : D.V i) :
    J.app i (liftOperator J r A i x) = A.app i (J.app i x) :=
  hr i _

theorem liftOperator_kills_kernel (A : Hom E E) (i : L) (x : D.V i)
    (hx : J.app i x = 0) : liftOperator J r A i x = 0 := by
  change r i (A.app i (J.app i x)) = 0
  rw [hx, map_zero, map_zero]

/-- The defect of the lifted operation is exactly the section defect. -/
theorem liftOperator_transition (A : Hom E E) {i j : L} (h : i ≤ j)
    (x : D.V i) :
    D.map h (liftOperator J r A i x) - liftOperator J r A j (D.map h x) =
      sectionDefect r h (A.app i (J.app i x)) := by
  change D.map h (r i (A.app i (J.app i x))) -
    r j (A.app j (J.app j (D.map h x))) =
    D.map h (r i (A.app i (J.app i x))) -
      r j (E.map h (A.app i (J.app i x)))
  rw [J.naturality, A.naturality]

end Representatives
end SplitZero.Integration
