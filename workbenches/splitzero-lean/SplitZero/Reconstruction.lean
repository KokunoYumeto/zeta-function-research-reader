import SplitZero.Hom

/-!
# The unique support character and a reconstruction countermodel

The Boolean semiring is realized as G(ZMod 1): the supported point is one,
and the distinct absent point is zero. This avoids ambiguous Bool arithmetic.
The countermodel concerns the UNCONTRACTED free monoid semiring in chapter 14.
It proves the displayed generator relations do not force the absent generator
class to be the additive zero. Adding [tau] = 0 repairs that presentation.
-/

namespace SplitZero

abbrev Boolean := G (ZMod 1)

theorem boolean_one_add_one : (1 : Boolean) + 1 = 1 := by
  change ofR ((1 : ZMod 1) + 1) = ofR 1
  congr 1
  exact Subsingleton.elim _ _

variable (R : Type*) [CommRing R]

def toTrivialRing : R →+* ZMod 1 where
  toFun _ := 0
  map_zero' := rfl
  map_one' := Subsingleton.elim _ _
  map_add' _ _ := by simp
  map_mul' _ _ := by simp

def supportCharacter : G R →+* Boolean := lift (toTrivialRing R)

/-- Every unital Boolean-valued semiring hom is the intrinsic support character. -/
theorem supportCharacter_unique (f : G R →+* Boolean) : f = supportCharacter R := by
  have h : lower f = toTrivialRing R := by
    ext r
    exact Subsingleton.elim _ _
  calc
    f = lift (lower f) := (homEquiv (R := R) (S := ZMod 1)).right_inv f |>.symm
    _ = supportCharacter R := by rw [h]; rfl

/-- A multiplicative generator assignment; it is intentionally not a zero-preserving hom. -/
def allGeneratorsOne : G R →* Boolean where
  toFun _ := 1
  map_one' := rfl
  map_mul' _ _ := by simp

/-- Kernel-checked countermodel to the claim that the two printed relation families
already imply [tau] = 0 in the uncontracted free monoid semiring. -/
theorem reconstruction_relations_do_not_force_zero :
    (∀ a b : R, allGeneratorsOne R (ofR a) + allGeneratorsOne R (ofR b) =
      allGeneratorsOne R (ofR (a + b))) ∧
    (∀ x : G R, allGeneratorsOne R x + allGeneratorsOne R tau = allGeneratorsOne R x) ∧
    allGeneratorsOne R tau ≠ 0 := by
  refine ⟨?_, ?_, ?_⟩
  · intro a b
    exact boolean_one_add_one
  · intro x
    exact boolean_one_add_one
  · exact one_ne_zero

end SplitZero
