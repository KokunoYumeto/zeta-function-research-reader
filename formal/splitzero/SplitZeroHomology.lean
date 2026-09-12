import SplitZeroReconstruction

/-!
# Induced homology maps and their complete kernels

A window is any three consecutive terms of a cochain complex. Its homology
is constructed as cycles modulo the actual range of the incoming differential.
The kernel equivalence below is for every chain map, with no injectivity,
surjectivity, finite dimension, or spectral hypothesis.
-/

noncomputable section
namespace SplitZero.Homology

universe u v
variable {R : Type u} [CommRing R]

section QuotientKernel
variable {M N : Type v} [AddCommGroup M] [Module R M]
  [AddCommGroup N] [Module R N]
variable (P : Submodule R M) (Q : Submodule R N) (f : M →ₗ[R] N)
  (hf : P ≤ Q.comap f)

/-- Representatives whose image becomes a target relation. -/
abbrev Killing := Q.comap f
/-- Original relations inside the module of killed representatives. -/
abbrev OldRelations := P.comap (Killing Q f).subtype

/-- The actual map of killed representatives onto the kernel of the quotient map. -/
def kernelRepresentative : Killing Q f →ₗ[R] LinearMap.ker (P.mapQ Q f hf) where
  toFun x := ⟨P.mkQ x.val, by
    change (Q.mkQ (f x.val)) = 0
    exact (Submodule.Quotient.mk_eq_zero _).mpr x.property⟩
  map_add' x y := Subtype.ext (P.mkQ.map_add x.val y.val)
  map_smul' r x := Subtype.ext (P.mkQ.map_smul r x.val)

/-- Descend by exactly the original source relations, not by all killed representatives. -/
def kernelDescent : (Killing Q f ⧸ OldRelations P Q f) →ₗ[R]
    LinearMap.ker (P.mapQ Q f hf) :=
  (OldRelations P Q f).liftQ (kernelRepresentative P Q f hf) (by
    intro x hx
    apply Subtype.ext
    exact (Submodule.Quotient.mk_eq_zero _).mpr hx)

theorem kernelDescent_bijective : Function.Bijective (kernelDescent P Q f hf) := by
  constructor
  · intro x y hxy
    induction x using Submodule.Quotient.induction_on with
    | _ x =>
      induction y using Submodule.Quotient.induction_on with
      | _ y =>
        apply (Submodule.Quotient.eq (OldRelations P Q f)).mpr
        change x.val - y.val ∈ P
        apply (Submodule.Quotient.eq P).mp
        exact congrArg Subtype.val hxy
  · rintro ⟨x, hx⟩
    obtain ⟨m, rfl⟩ := Submodule.Quotient.mk_surjective P x
    have hm : m ∈ Killing Q f := by
      change (Q.mkQ (f m)) = 0 at hx
      exact (Submodule.Quotient.mk_eq_zero _).mp hx
    exact ⟨Submodule.Quotient.mk (⟨m, hm⟩ : Killing Q f), Subtype.ext rfl⟩

/-- Exact kernel formula, as a linear equivalence with specified forward map. -/
def quotientKernelEquiv : (Killing Q f ⧸ OldRelations P Q f) ≃ₗ[R]
    LinearMap.ker (P.mapQ Q f hf) :=
  LinearEquiv.ofBijective (kernelDescent P Q f hf) (kernelDescent_bijective P Q f hf)

@[simp] theorem quotientKernelEquiv_mk (x : Killing Q f) :
    ((quotientKernelEquiv P Q f hf) (Submodule.Quotient.mk x)).val = P.mkQ x.val := rfl

end QuotientKernel

/-- The data at one degree of an arbitrary cochain complex. -/
structure Window (R : Type u) [CommRing R] where
  Mprev : Type v
  M : Type v
  Mnext : Type v
  [prevGroup : AddCommGroup Mprev]
  [midGroup : AddCommGroup M]
  [nextGroup : AddCommGroup Mnext]
  [prevModule : Module R Mprev]
  [midModule : Module R M]
  [nextModule : Module R Mnext]
  prev : Mprev →ₗ[R] M
  next : M →ₗ[R] Mnext
  square_zero : next.comp prev = 0

attribute [instance] Window.prevGroup Window.midGroup Window.nextGroup
  Window.prevModule Window.midModule Window.nextModule

namespace Window
variable (C : Window R)

abbrev Cycles := LinearMap.ker C.next

def boundaryToCycles : C.Mprev →ₗ[R] C.Cycles where
  toFun x := ⟨C.prev x, by
    have h := congrArg (fun f : C.Mprev →ₗ[R] C.Mnext => f x) C.square_zero
    exact h⟩
  map_add' x y := Subtype.ext (C.prev.map_add x y)
  map_smul' r x := Subtype.ext (C.prev.map_smul r x)

def boundaries : Submodule R C.Cycles := LinearMap.range C.boundaryToCycles

abbrev H := C.Cycles ⧸ C.boundaries

def classOf : C.Cycles →ₗ[R] C.H := C.boundaries.mkQ

theorem class_zero_iff_boundary (z : C.Cycles) :
    C.classOf z = 0 ↔ ∃ x, C.prev x = z.val := by
  change Submodule.Quotient.mk z = 0 ↔ _
  rw [Submodule.Quotient.mk_eq_zero]
  constructor
  · rintro ⟨x, hx⟩
    exact ⟨x, congrArg Subtype.val hx⟩
  · rintro ⟨x, hx⟩
    exact ⟨x, Subtype.ext hx⟩

end Window

structure ChainMap (C D : Window R) where
  left : C.Mprev →ₗ[R] D.Mprev
  mid : C.M →ₗ[R] D.M
  right : C.Mnext →ₗ[R] D.Mnext
  prev_comm : mid.comp C.prev = D.prev.comp left
  next_comm : D.next.comp mid = right.comp C.next

namespace ChainMap
variable {C D E : Window R}

def cyclesMap (f : ChainMap C D) : C.Cycles →ₗ[R] D.Cycles where
  toFun z := ⟨f.mid z.val, by
    have h := congrArg (fun g : C.M →ₗ[R] D.Mnext => g z.val) f.next_comm
    change D.next (f.mid z.val) = f.right (C.next z.val) at h
    rw [z.property, map_zero] at h
    exact h⟩
  map_add' x y := Subtype.ext (f.mid.map_add x.val y.val)
  map_smul' r x := Subtype.ext (f.mid.map_smul r x.val)

theorem maps_boundaries (f : ChainMap C D) :
    C.boundaries ≤ D.boundaries.comap f.cyclesMap := by
  rintro z ⟨x, rfl⟩
  refine ⟨f.left x, ?_⟩
  apply Subtype.ext
  exact (congrArg (fun g : C.Mprev →ₗ[R] D.M => g x) f.prev_comm).symm

def onHomology (f : ChainMap C D) : C.H →ₗ[R] D.H :=
  C.boundaries.mapQ D.boundaries f.cyclesMap f.maps_boundaries

@[simp] theorem onHomology_class (f : ChainMap C D) (z : C.Cycles) :
    f.onHomology (C.classOf z) = D.classOf (f.cyclesMap z) := rfl

theorem mapped_class_zero_iff (f : ChainMap C D) (z : C.Cycles) :
    f.onHomology (C.classOf z) = 0 ↔ ∃ y, D.prev y = f.mid z.val :=
  D.class_zero_iff_boundary (f.cyclesMap z)

/-- Cycles sent to boundaries, modulo the original boundaries, are precisely
    the kernel of the induced homology map. -/
def homologyKernelEquiv (f : ChainMap C D) :
    (Killing D.boundaries f.cyclesMap ⧸ OldRelations C.boundaries D.boundaries f.cyclesMap)
      ≃ₗ[R] LinearMap.ker f.onHomology :=
  quotientKernelEquiv C.boundaries D.boundaries f.cyclesMap f.maps_boundaries

/-- Identity and composition are retained before and after taking homology. -/
def id (C : Window R) : ChainMap C C where
  left := LinearMap.id
  mid := LinearMap.id
  right := LinearMap.id
  prev_comm := rfl
  next_comm := rfl

def comp (g : ChainMap D E) (f : ChainMap C D) : ChainMap C E where
  left := g.left.comp f.left
  mid := g.mid.comp f.mid
  right := g.right.comp f.right
  prev_comm := by
    ext x
    have h := congrArg (fun k : C.Mprev →ₗ[R] D.M => k x) f.prev_comm
    have h' := congrArg (fun k : D.Mprev →ₗ[R] E.M => k (f.left x)) g.prev_comm
    exact (congrArg g.mid h).trans h'
  next_comm := by
    ext x
    have h := congrArg (fun k : D.M →ₗ[R] E.Mnext => k (f.mid x)) g.next_comm
    have h' := congrArg (fun k : C.M →ₗ[R] D.Mnext => k x) f.next_comm
    exact h.trans (congrArg g.right h')

theorem onHomology_id (C : Window R) : (id C).onHomology = LinearMap.id := by
  apply LinearMap.ext
  intro x
  induction x using Submodule.Quotient.induction_on with
  | _ x => rfl

theorem onHomology_comp (g : ChainMap D E) (f : ChainMap C D) :
    (comp g f).onHomology = g.onHomology.comp f.onHomology := by
  apply LinearMap.ext
  intro x
  induction x using Submodule.Quotient.induction_on with
  | _ x => rfl

end ChainMap
end SplitZero.Homology
