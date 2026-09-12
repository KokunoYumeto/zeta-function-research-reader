import SplitZero.Support

/-!
# Forward decomposition and morphism coherence

These are the remaining object/morphism identities for extracting the user's
linear join diagram from a split-zero semimodule. The reverse reconstruction
from an arbitrary diagram and a bundled categorical equivalence are not asserted.
-/

namespace SplitZero

section
variable (R : Type*) [CommRing R]
variable {M N P : Type*}
variable [AddCommMonoid M] [Module (G R) M]
variable [AddCommMonoid N] [Module (G R) N]
variable [AddCommMonoid P] [Module (G R) P]

/-- The semimodule carrier is exactly the disjoint union of its support fibres. -/
def fiberDecomposition : M ≃ (Σ l : Skeleton R M, Fiber R M l) where
  toFun m := ⟨⟨support R m, support_support R m⟩, ⟨m, rfl⟩⟩
  invFun x := x.2.val
  left_inv _ := rfl
  right_inv := by
    rintro ⟨⟨l, hl⟩, ⟨m, hm⟩⟩
    cases hm
    rfl

theorem skeletonMap_bot (f : M →ₗ[G R] N) :
    skeletonMap R f ⊥ = ⊥ := Subtype.ext f.map_zero

theorem skeletonMap_sup (f : M →ₗ[G R] N) (l m : Skeleton R M) :
    skeletonMap R f (l ⊔ m) = skeletonMap R f l ⊔ skeletonMap R f m :=
  Subtype.ext (f.map_add l.val m.val)

theorem skeletonMap_id (l : Skeleton R M) :
    skeletonMap R (LinearMap.id : M →ₗ[G R] M) l = l := rfl

theorem skeletonMap_comp (g : N →ₗ[G R] P) (f : M →ₗ[G R] N) (l : Skeleton R M) :
    skeletonMap R (g.comp f) l = skeletonMap R g (skeletonMap R f l) := rfl

theorem fiberMap_id (l : Skeleton R M) :
    fiberMap R (LinearMap.id : M →ₗ[G R] M) l = LinearMap.id := by
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  rfl

theorem fiberMap_comp (g : N →ₗ[G R] P) (f : M →ₗ[G R] N) (l : Skeleton R M) :
    (fiberMap R g (skeletonMap R f l)).comp (fiberMap R f l) =
      fiberMap R (g.comp f) l := by
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  rfl

end

end SplitZero
