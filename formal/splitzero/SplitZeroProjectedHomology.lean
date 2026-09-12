import SplitZeroSignedProjector

/-!
# Homology of the actual projected subcomplex

The source's signed average is a chain idempotent. This file constructs the
projected window and proves that its homology is the fixed submodule of the
induced homology idempotent. Cycles and boundaries are the original library's
objects; no new definition of homology or spectral vanishing is introduced.
-/
noncomputable section
namespace SplitZero.ProjectedHomology
open SplitZero.Homology
universe u v
variable {R : Type u} [CommRing R]

/-- Fixed vectors of a linear endomorphism, with their original amplitudes. -/
def fixed {M : Type v} [AddCommGroup M] [Module R M] (p : M →ₗ[R] M) : Submodule R M where
  carrier := {x | p x = x}
  zero_mem' := p.map_zero
  add_mem' hx hy := by rw [map_add, hx, hy]
  smul_mem' r x hx := by rw [map_smul, hx]

structure Data (C : Window.{u,v} R) where
  p : ChainMap C C
  left_idem : ∀ x, p.left (p.left x) = p.left x
  mid_idem : ∀ x, p.mid (p.mid x) = p.mid x
  right_idem : ∀ x, p.right (p.right x) = p.right x

namespace Data
variable {C : Window.{u,v} R} (S : Data C)

/-- The actual fixed subcomplex, not just the image after computing cohomology. -/
def window : Window R where
  Mprev := fixed S.p.left
  M := fixed S.p.mid
  Mnext := fixed S.p.right
  prev :=
    { toFun := fun x => ⟨C.prev x.val, by
        change S.p.mid (C.prev x.val) = C.prev x.val
        have h := LinearMap.congr_fun S.p.prev_comm x.val
        change S.p.mid (C.prev x.val) = C.prev (S.p.left x.val) at h
        exact h.trans (congrArg C.prev x.property)⟩
      map_add' := fun x y => Subtype.ext (C.prev.map_add x.val y.val)
      map_smul' := fun r x => Subtype.ext (C.prev.map_smul r x.val) }
  next :=
    { toFun := fun x => ⟨C.next x.val, by
        change S.p.right (C.next x.val) = C.next x.val
        have h := LinearMap.congr_fun S.p.next_comm x.val
        change C.next (S.p.mid x.val) = S.p.right (C.next x.val) at h
        exact h.symm.trans (congrArg C.next x.property)⟩
      map_add' := fun x y => Subtype.ext (C.next.map_add x.val y.val)
      map_smul' := fun r x => Subtype.ext (C.next.map_smul r x.val) }
  square_zero := by
    ext x
    apply Subtype.ext
    exact LinearMap.congr_fun C.square_zero x.val

/-- The inclusion keeps the original chain-level representatives. -/
def inclusion : ChainMap S.window C where
  left := (fixed S.p.left).subtype
  mid := (fixed S.p.mid).subtype
  right := (fixed S.p.right).subtype
  prev_comm := rfl
  next_comm := rfl

/-- The specified idempotent, with codomain restricted to its fixed subcomplex. -/
def projection : ChainMap C S.window where
  left :=
    { toFun := fun x => ⟨S.p.left x, S.left_idem x⟩
      map_add' := fun x y => Subtype.ext (S.p.left.map_add x y)
      map_smul' := fun r x => Subtype.ext (S.p.left.map_smul r x) }
  mid :=
    { toFun := fun x => ⟨S.p.mid x, S.mid_idem x⟩
      map_add' := fun x y => Subtype.ext (S.p.mid.map_add x y)
      map_smul' := fun r x => Subtype.ext (S.p.mid.map_smul r x) }
  right :=
    { toFun := fun x => ⟨S.p.right x, S.right_idem x⟩
      map_add' := fun x y => Subtype.ext (S.p.right.map_add x y)
      map_smul' := fun r x => Subtype.ext (S.p.right.map_smul r x) }
  prev_comm := by
    ext x
    apply Subtype.ext
    exact LinearMap.congr_fun S.p.prev_comm x
  next_comm := by
    ext x
    apply Subtype.ext
    exact LinearMap.congr_fun S.p.next_comm x

/-- Inclusion after projection is the original induced homology operator. -/
theorem include_project :
    S.inclusion.onHomology.comp S.projection.onHomology = S.p.onHomology := by
  ext x
  induction x using Submodule.Quotient.induction_on with
  | _ z => rfl

/-- Projection after inclusion is identity, proved on the actual cycle quotient. -/
theorem project_include :
    S.projection.onHomology.comp S.inclusion.onHomology = LinearMap.id := by
  ext x
  induction x using Submodule.Quotient.induction_on with
  | _ z =>
    change S.window.classOf (S.projection.cyclesMap (S.inclusion.cyclesMap z)) =
      S.window.classOf z
    congr 1
    apply Subtype.ext
    apply Subtype.ext
    exact z.val.property

theorem inclusion_fixed (x : S.window.H) :
    S.p.onHomology (S.inclusion.onHomology x) = S.inclusion.onHomology x := by
  calc
    S.p.onHomology (S.inclusion.onHomology x) =
        S.inclusion.onHomology (S.projection.onHomology (S.inclusion.onHomology x)) :=
      (LinearMap.congr_fun S.include_project _).symm
    _ = S.inclusion.onHomology x :=
      congrArg S.inclusion.onHomology (LinearMap.congr_fun S.project_include x)

/-- Complete equivalence between projected-complex homology and the selected summand. -/
def homologyEquiv : S.window.H ≃ₗ[R] fixed S.p.onHomology where
  toFun x := ⟨S.inclusion.onHomology x, S.inclusion_fixed x⟩
  invFun x := S.projection.onHomology x.val
  left_inv x := LinearMap.congr_fun S.project_include x
  right_inv x := by
    apply Subtype.ext
    exact (LinearMap.congr_fun S.include_project x.val).trans x.property
  map_add' x y := Subtype.ext (S.inclusion.onHomology.map_add x y)
  map_smul' r x := Subtype.ext (S.inclusion.onHomology.map_smul r x)

@[simp] theorem homologyEquiv_class (z : S.window.Cycles) :
    (S.homologyEquiv (S.window.classOf z)).val =
      C.classOf (S.inclusion.cyclesMap z) := rfl
end Data

section Average
variable {G : Type*} [Group G] [Fintype G]
  [Invertible (Fintype.card G : ℂ)]
  {C : Window ℂ}

/-- The actual finite-group chain average supplies all idempotence hypotheses. -/
def ofAverage (S : SplitZero.SignedProjector.Action (G := G) C) : Data C where
  p := S.averageChain
  left_idem x := S.prevRep.averageMap_id _ (S.prevRep.averageMap_invariant x)
  mid_idem x := S.midRep.averageMap_id _ (S.midRep.averageMap_invariant x)
  right_idem x := S.nextRep.averageMap_id _ (S.nextRep.averageMap_invariant x)

/-- Signed actions are accommodated by supplying their character-twisted representation. -/
abbrev averageHomologyEquiv (S : SplitZero.SignedProjector.Action (G := G) C) :=
  (ofAverage S).homologyEquiv
end Average
end SplitZero.ProjectedHomology
