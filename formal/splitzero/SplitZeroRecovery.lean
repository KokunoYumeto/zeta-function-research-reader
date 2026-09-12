import SplitZeroReconstruction

/-!
# Reconstruction recovers the original SplitZero semimodule

This connects the new diagram construction to the previously checked intrinsic
support/fibre construction. The equivalence preserves the full scalar action,
not only the carrier or the Boolean support observation.
-/

noncomputable section
namespace SplitZero.Recovery
open SplitZero.Reconstruction SplitZero.Extension

variable (R M : Type*) [CommRing R] [AddCommMonoid M] [Module (G R) M]

def intrinsic : LinearDiagram R (SplitZero.Diagram.Support R M) where
  V l := SplitZero.Diagram.Fiber l
  map h := SplitZero.Diagram.transport h
  map_id l := SplitZero.Diagram.transport_self l
  map_comp h h' := SplitZero.Diagram.transport_comp h h'

/-- Reassembling the intrinsic fibres recovers the original semimodule. -/
def recoverEquiv : (intrinsic R M).Total ≃ₗ[G R] M where
  toFun x := x.2.val
  invFun m := ⟨⟨support (R := R) m, support_support m⟩, ⟨m, rfl⟩⟩
  left_inv x := by
    rcases x with ⟨⟨l, hl⟩, ⟨m, hm⟩⟩
    cases hm
    rfl
  right_inv _ := rfl
  map_add' x y := by
    rcases x with ⟨i, x⟩
    rcases y with ⟨j, y⟩
    change (x.val + (i.val + j.val)) + (y.val + (i.val + j.val)) = x.val + y.val
    have hij : i.val + j.val = support (R := R) (x.val + y.val) := by
      rw [support_add, x.property, y.property]
    rw [hij]
    calc
      (x.val + support (R := R) (x.val + y.val)) +
          (y.val + support (R := R) (x.val + y.val)) =
          (x.val + y.val) + (support (R := R) (x.val + y.val) +
            support (R := R) (x.val + y.val)) := by ac_rfl
      _ = x.val + y.val := by rw [support_add_self, add_support]
  map_smul' a x := by
    obtain ⟨_ | a⟩ := a
    · rfl
    · rfl

@[simp] theorem recover_apply (l : SplitZero.Diagram.Support R M)
    (x : SplitZero.Diagram.Fiber l) :
    recoverEquiv R M ⟨l, x⟩ = x.val := rfl

@[simp] theorem recover_inverse (m : M) :
    (recoverEquiv R M).symm m =
      ⟨⟨support (R := R) m, support_support m⟩, ⟨m, rfl⟩⟩ := rfl

end SplitZero.Recovery
