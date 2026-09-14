import SplitZeroInternalQuotient
import Mathlib.Data.Finset.Lattice.Fold

/-!
# Full-source boundaries retained at a proper support

ISM42--43: the original quotient-kernel equivalence assembled into natural
SplitZero diagrams, with both inverse total maps and the supported image.
No transport or source comparison is assumed injective.
-/
noncomputable section
namespace SplitZero.RestrictedBoundary
open SplitZero.Reconstruction
variable {R L : Type*} [CommRing R] [SemilatticeSup L] [OrderBot L]
variable {D E : LinearDiagram R L}

def killedRelations (f : Hom D E) (C : Relations E) : Relations D where
  fibre i := (C.fibre i).comap (f.app i)
  stable := by
    intro i j h x hx
    change f.app j (D.map h x) ∈ C.fibre j
    rw [f.naturality]
    exact C.stable h hx

def residualRelations (f : Hom D E) (B : Relations D) (C : Relations E) :
    Relations (killedRelations f C).relationDiagram where
  fibre i := (B.fibre i).comap ((killedRelations f C).fibre i).subtype
  stable := by
    intro i j h x hx
    change D.map h x.val ∈ B.fibre j
    exact B.stable h hx

def quotientHom (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) :
    Hom B.quotientDiagram C.quotientDiagram where
  app i := (B.fibre i).mapQ (C.fibre i) (f.app i) (hf i)
  naturality := by
    intro i j h x
    obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective (B.fibre i) x
    change (C.fibre j).mkQ (f.app j (D.map h x)) =
      (C.fibre j).mkQ (E.map h (f.app i x))
    rw [f.naturality]

def kernelDiagram (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) : LinearDiagram R L where
  V i := LinearMap.ker ((quotientHom f B C hf).app i)
  map {i j} h :=
    { toFun := fun x => ⟨B.quotientDiagram.map h x.val, by
        change (quotientHom f B C hf).app j (B.quotientDiagram.map h x.val) = 0
        rw [(quotientHom f B C hf).naturality, x.property, map_zero]⟩
      map_add' := fun x y => Subtype.ext (map_add (B.quotientDiagram.map h) x.val y.val)
      map_smul' := fun r x => Subtype.ext (map_smul (B.quotientDiagram.map h) r x.val) }
  map_id i := by
    ext x
    exact B.quotientDiagram.map_self i x.val
  map_comp h h' := by
    ext x
    exact B.quotientDiagram.map_map h h' x.val

/-- Reuse the original proved coefficient equivalence on the literal fibres. -/
def residualEquiv (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) (i : L) :
    (residualRelations f B C).quotientDiagram.V i ≃ₗ[R]
      (kernelDiagram f B C hf).V i :=
  SplitZero.Homology.quotientKernelEquiv (B.fibre i) (C.fibre i) (f.app i) (hf i)

def kernelComparison (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) :
    Hom (residualRelations f B C).quotientDiagram (kernelDiagram f B C hf) where
  app i := (residualEquiv f B C hf i).toLinearMap
  naturality := by
    intro i j h x
    obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective ((residualRelations f B C).fibre i) x
    apply Subtype.ext
    rfl

def kernelInverse (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) :
    Hom (kernelDiagram f B C hf) (residualRelations f B C).quotientDiagram where
  app i := (residualEquiv f B C hf i).symm.toLinearMap
  naturality := by
    intro i j h x
    apply (residualEquiv f B C hf j).injective
    change (residualEquiv f B C hf j)
        ((residualEquiv f B C hf j).symm ((kernelDiagram f B C hf).map h x)) =
      (residualEquiv f B C hf j)
        ((residualRelations f B C).quotientDiagram.map h ((residualEquiv f B C hf i).symm x))
    rw [LinearEquiv.apply_symm_apply]
    have hn := (kernelComparison f B C hf).naturality h ((residualEquiv f B C hf i).symm x)
    simpa only [kernelComparison, LinearEquiv.coe_coe, LinearEquiv.apply_symm_apply] using hn.symm

theorem left_inverse_total (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) :
    (kernelInverse f B C hf).total.comp (kernelComparison f B C hf).total = LinearMap.id := by
  ext x
  rcases x with ⟨i, x⟩
  change (⟨i, (residualEquiv f B C hf i).symm ((residualEquiv f B C hf i) x)⟩ :
    (residualRelations f B C).quotientDiagram.Total) = ⟨i, x⟩
  rw [LinearEquiv.symm_apply_apply]

theorem right_inverse_total (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) :
    (kernelComparison f B C hf).total.comp (kernelInverse f B C hf).total = LinearMap.id := by
  ext x
  rcases x with ⟨i, x⟩
  change (⟨i, (residualEquiv f B C hf i) ((residualEquiv f B C hf i).symm x)⟩ :
    (kernelDiagram f B C hf).Total) = ⟨i, x⟩
  rw [LinearEquiv.apply_symm_apply]

def kernelInclusion (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) :
    Hom (kernelDiagram f B C hf) B.quotientDiagram where
  app i := (LinearMap.ker ((quotientHom f B C hf).app i)).subtype
  naturality _ _ := rfl

def residualInclusion (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) :
    Hom (residualRelations f B C).quotientDiagram B.quotientDiagram :=
  Hom.comp (kernelInclusion f B C hf) (kernelComparison f B C hf)

theorem original_square (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i)) :
    (residualInclusion f B C hf).total.comp (residualRelations f B C).quotientMap.total =
      B.quotientMap.total.comp (killedRelations f C).relationInclusion.total := by
  ext x
  rcases x with ⟨i, x⟩
  rfl

/-- Full-source vanishing compares to zero at the same fibre, not absence. -/
theorem range_iff_supported_zero (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i))
    (y : B.quotientDiagram.Total) :
    (∃ x, (residualInclusion f B C hf).total x = y) ↔
      (quotientHom f B C hf).total y = (e : G R) • (quotientHom f B C hf).total y := by
  constructor
  · rintro ⟨⟨i, x⟩, rfl⟩
    change (⟨i, (quotientHom f B C hf).app i ((residualEquiv f B C hf i x).val)⟩ :
      C.quotientDiagram.Total) = (e : G R) • ⟨i, _⟩
    rw [LinearDiagram.supported_zero_action]
    apply (C.quotientDiagram.same_label_eq i _ _).mpr
    exact (residualEquiv f B C hf i x).property
  · rcases y with ⟨i, y⟩
    intro hy
    change (⟨i, (quotientHom f B C hf).app i y⟩ : C.quotientDiagram.Total) =
      (e : G R) • ⟨i, (quotientHom f B C hf).app i y⟩ at hy
    rw [LinearDiagram.supported_zero_action] at hy
    have hk : (quotientHom f B C hf).app i y = 0 :=
      (C.quotientDiagram.same_label_eq i _ _).mp hy
    let z : (kernelDiagram f B C hf).V i := ⟨y, hk⟩
    refine ⟨⟨i, (residualEquiv f B C hf i).symm z⟩, ?_⟩
    change (⟨i, (residualEquiv f B C hf i ((residualEquiv f B C hf i).symm z)).val⟩ :
      B.quotientDiagram.Total) = ⟨i, y⟩
    rw [LinearEquiv.apply_symm_apply]

theorem proper_residual (f : Hom D E) (B : Relations D) (C : Relations E)
    (hf : ∀ i, B.fibre i ≤ (C.fibre i).comap (f.app i))
    (i : L) (x : D.V i) (hfull : f.app i x ∈ C.fibre i) (hproper : x ∉ B.fibre i) :
    B.quotientMap.total ⟨i, x⟩ ≠ (⟨i, 0⟩ : B.quotientDiagram.Total) ∧
      (quotientHom f B C hf).total (B.quotientMap.total ⟨i, x⟩) =
        (⟨i, 0⟩ : C.quotientDiagram.Total) := by
  constructor
  · intro he
    have hz : (B.fibre i).mkQ x = 0 := (B.quotientDiagram.same_label_eq i _ _).mp he
    exact hproper ((Submodule.Quotient.mk_eq_zero _).mp hz)
  · apply (C.quotientDiagram.same_label_eq i _ _).mpr
    exact (Submodule.Quotient.mk_eq_zero _).mpr hfull

theorem present_empty_residual {J : Type*} [DecidableEq J]
    (F : LinearDiagram R (L × Finset J)) (i : L) (hi : i ≠ ⊥) :
    (⟨(i, ∅), 0⟩ : F.Total) ≠ 0 := by
  apply F.fibre_zero_ne_global
  intro h
  exact hi (congrArg Prod.fst h)
end SplitZero.RestrictedBoundary
