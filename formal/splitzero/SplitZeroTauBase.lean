import SplitZeroMaps

/-!
# The absolute pointed base and its finite-sum presentation

The base is the multiplicative monoid `{tau,1}`, NOT the Boolean semiring.
Its preaddition identifies precisely words with the same number of units;
zero terms can be removed. The original G(R) operations and reflect remain
unchanged. This file proves structural maps and prime inverse images. It
makes no assertion that a finite chart is an arithmetic scheme.
-/
namespace SplitZero.TauBase

abbrev F1 := WithZero Unit

/-- The unique pointed multiplicative structural map. -/
def structural (M : Type*) [MulZeroOneClass M] : F1 →*₀ M where
  toFun x := match x with
    | none => 0
    | some _ => 1
  map_zero' := rfl
  map_one' := rfl
  map_mul' x y := by
    rcases x with _ | ⟨⟩ <;> rcases y with _ | ⟨⟩ <;> simp

@[simp] theorem structural_zero (M : Type*) [MulZeroOneClass M] :
    structural M 0 = 0 := rfl
@[simp] theorem structural_one (M : Type*) [MulZeroOneClass M] :
    structural M 1 = 1 := rfl

theorem structural_unique {M : Type*} [MulZeroOneClass M] (f : F1 →*₀ M) :
    f = structural M := by
  ext x
  cases x with
  | none => exact f.map_zero
  | some u => cases u; exact f.map_one

theorem structural_natural {M N : Type*} [MulZeroOneClass M] [MulZeroOneClass N]
    (f : M →*₀ N) : f.comp (structural M) = structural N :=
  structural_unique _

/-- A multiplicative prime, with the absorbing element included. -/
structure MonoidPrime (M : Type*) [CommMonoidWithZero M] where
  carrier : Set M
  zero_mem : (0 : M) ∈ carrier
  one_not_mem : (1 : M) ∉ carrier
  absorb : ∀ a b, b ∈ carrier → a * b ∈ carrier
  prime : ∀ a b, a * b ∈ carrier → a ∈ carrier ∨ b ∈ carrier

/-- The unique prime of the absolute pointed base. -/
def basePrime : MonoidPrime F1 where
  carrier := {0}
  zero_mem := rfl
  one_not_mem := by decide
  absorb a b hb := by
    change a * b = 0
    change b = 0 at hb
    rw [hb, mul_zero]
  prime a b h := by
    rcases a with _ | ⟨⟩ <;> rcases b with _ | ⟨⟩ <;> simp_all

theorem basePrime_unique (P : MonoidPrime F1) : P = basePrime := by
  have hc : P.carrier = ({0} : Set F1) := by
    ext x
    cases x with
    | none =>
      change (0 : F1) ∈ P.carrier ↔ (0 : F1) ∈ ({0} : Set F1)
      simp [P.zero_mem]
    | some u =>
      cases u
      change (1 : F1) ∈ P.carrier ↔ (1 : F1) ∈ ({0} : Set F1)
      simp [P.one_not_mem]
  cases P
  cases hc
  rfl

instance : Unique (MonoidPrime F1) where
  default := basePrime
  uniq := basePrime_unique

/-- Inverse image of a proper coefficient ideal is the single base prime. -/
theorem prime_inverse_image {S : Type*} [CommSemiring S] (I : Ideal S)
    (hI : (1 : S) ∉ I) : (structural S) ⁻¹' (I : Set S) = {0} := by
  ext x
  cases x with
  | none => simp [I.zero_mem]
  | some u => cases u; simp [hI]

/-- Finite additive words. No addition is installed on F1. -/
def wordValue (w : List F1) : ℕ := (w.map (structural ℕ)).sum

def Related (v w : List F1) : Prop := wordValue v = wordValue w

@[simp] theorem wordValue_nil : wordValue [] = 0 := rfl
@[simp] theorem wordValue_cons (x : F1) (w : List F1) :
    wordValue (x :: w) = structural ℕ x + wordValue w := rfl
@[simp] theorem wordValue_append (v w : List F1) :
    wordValue (v ++ w) = wordValue v + wordValue w := by simp [wordValue]

theorem related_empty_tau : Related [] [0] := rfl

theorem units_not_idempotent : ¬ Related [1, 1] [1] := by decide

/-- The structural map preserves every relation of the base preaddition. -/
theorem structural_word_sum {S : Type*} [Semiring S] (w : List F1) :
    (w.map (structural S)).sum = (wordValue w : S) := by
  induction w with
  | nil => simp [wordValue]
  | cons x w ih =>
    change structural S x + (w.map (structural S)).sum =
      ((structural ℕ x + wordValue w : ℕ) : S)
    rw [Nat.cast_add, ih]
    congr 1
    cases x <;> simp [structural]

theorem structural_preserves_preaddition {S : Type*} [Semiring S]
    {v w : List F1} (h : Related v w) :
    (v.map (structural S)).sum = (w.map (structural S)).sum := by
  rw [structural_word_sum, structural_word_sum]
  exact congrArg (Nat.cast : ℕ → S) h

/-- The arithmetic quotient remains a commuting marked coefficient map. -/
theorem arithmetic_square {R : Type*} [CommRing R] :
    (reflect : G R →+* R).toMonoidWithZeroHom.comp (structural (G R)) = structural R :=
  structural_natural _

theorem tau_e_retained {R : Type*} [CommRing R] :
    structural (G R) 0 = tau ∧ (e : G R) ≠ structural (G R) 0 := by
  constructor
  · rfl
  · intro h; cases h

end SplitZero.TauBase
