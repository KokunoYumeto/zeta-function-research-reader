import SplitZero.Reconstruction

/-!
# Universal property of the corrected generator relations

The uncontracted presentation needs [tau] = 0. With that relation and the
supported-addition relations, every multiplicative assignment extends uniquely
to a semiring homomorphism. This proves the corrected presentation's mapping
property; no explicit quotient construction is silently claimed.
-/

namespace SplitZero

variable {R A : Type*} [CommRing R] [CommSemiring A]

/-- Extend a multiplicative assignment satisfying the corrected zero and sum relations. -/
def extendCorrected (f : G R →* A) (hzero : f tau = 0)
    (hadd : ∀ a b : R, f (ofR (a + b)) = f (ofR a) + f (ofR b)) : G R →+* A where
  toFun := f
  map_zero' := hzero
  map_one' := f.map_one
  map_mul' := f.map_mul
  map_add' x y := by
    obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y
    · change f tau = f tau + f tau
      rw [hzero, zero_add]
    · change f (ofR b) = f tau + f (ofR b)
      rw [hzero, zero_add]
    · change f (ofR a) = f (ofR a) + f tau
      rw [hzero, add_zero]
    · exact hadd a b

/-- Every assignment satisfying the repaired presentation extends exactly once. -/
theorem corrected_assignment_extends_uniquely (f : G R →* A) (hzero : f tau = 0)
    (hadd : ∀ a b : R, f (ofR (a + b)) = f (ofR a) + f (ofR b)) :
    ∃! h : G R →+* A, h.toMonoidHom = f := by
  refine ⟨extendCorrected f hzero hadd, rfl, ?_⟩
  intro h hh
  apply RingHom.ext
  intro x
  exact congrArg (fun g : G R →* A => g x) hh

end SplitZero
