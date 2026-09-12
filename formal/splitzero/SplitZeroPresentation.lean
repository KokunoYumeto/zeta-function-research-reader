import SplitZeroExtension

/-!
# Boolean support and the missing zero relation in the source presentation

The two-element semiring below is Boolean (addition OR, multiplication AND),
not the field of two elements. All of its laws are checked by finite case analysis.
-/

namespace SplitZero.Presentation
open SplitZero.Extension

inductive Bit where
  | absent
  | present
  deriving DecidableEq

namespace Bit

def add : Bit → Bit → Bit
  | absent, y => y
  | present, _ => present

def mul : Bit → Bit → Bit
  | absent, _ => absent
  | present, y => y

instance : Zero Bit := ⟨absent⟩
instance : One Bit := ⟨present⟩
instance : Add Bit := ⟨add⟩
instance : Mul Bit := ⟨mul⟩

instance bitAddCommMonoid : AddCommMonoid Bit where
  add := (· + ·)
  zero := 0
  add_assoc a b c := by cases a <;> cases b <;> cases c <;> rfl
  add_comm a b := by cases a <;> cases b <;> rfl
  zero_add a := by cases a <;> rfl
  add_zero a := by cases a <;> rfl
  nsmul := nsmulRec

instance bitCommMonoid : CommMonoid Bit where
  mul := (· * ·)
  one := 1
  mul_assoc a b c := by cases a <;> cases b <;> cases c <;> rfl
  mul_comm a b := by cases a <;> cases b <;> rfl
  one_mul a := by cases a <;> rfl
  mul_one a := by cases a <;> rfl
  npow := npowRec

instance : CommSemiring Bit :=
  { bitAddCommMonoid, bitCommMonoid with
    left_distrib := by intro a b c; cases a <;> cases b <;> cases c <;> rfl
    right_distrib := by intro a b c; cases a <;> cases b <;> cases c <;> rfl
    zero_mul := by intro a; cases a <;> rfl
    mul_zero := by intro a; cases a <;> rfl }

@[simp] theorem one_add_bit (b : Bit) : 1 + b = 1 := rfl
@[simp] theorem one_ne_zero : (1 : Bit) ≠ 0 := by decide

end Bit

variable {R : Type*} [CommRing R]

/-- The support character sends every supported element, including `e`, to one. -/
def supportCharacter : G R →+* Bit where
  toFun x := match x.toOption with | none => 0 | some _ => 1
  map_zero' := rfl
  map_one' := rfl
  map_add' x y := by obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y <;> rfl
  map_mul' x y := by obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y <;> rfl

theorem supportCharacter_unique (h : G R →+* Bit) : h = supportCharacter := by
  have he : h (e : G R) = 1 := by
    have hh := h.map_add (ofR (1 : R)) (ofR (-1 : R))
    have hi : (ofR (1 : R) : G R) + ofR (-1) = e := by
      rw [← ofR_add]
      change ofR (1 + -1 : R) = ofR 0
      rw [add_neg_cancel]
    rw [hi, ofR_one, h.map_one, Bit.one_add_bit] at hh
    exact hh
  apply RingHom.ext
  intro x
  obtain ⟨_ | r⟩ := x
  · exact h.map_zero
  · have hh := h.map_mul (ofR r) (e : G R)
    rw [ofR_mul_e, he, mul_one] at hh
    exact hh.symm

/-- Multiplicative generator evaluation for the countermodel. It is NOT a semiring map. -/
def constantOne : G R →* Bit where
  toFun _ := 1
  map_one' := rfl
  map_mul' _ _ := rfl

/-- The printed additive relations permit a nonzero image of the generator `[tau]`.
This is the explicit countermodel to the uncorrected presentation. -/
theorem missing_zero_relation_countermodel :
    ∃ f : G R →* Bit,
      (∀ a b : R, f (ofR a) + f (ofR b) = f (ofR (a + b))) ∧
      (∀ x : G R, f x + f tau = f x) ∧ f tau ≠ 0 := by
  refine ⟨constantOne, ?_, ?_, ?_⟩
  · intro a b; rfl
  · intro x; rfl
  · exact Bit.one_ne_zero

/-- Once the missing relation is included, the evaluation is a genuine semiring map.
This supplies the exact corrected universal property at the generator level. -/
def correctedPresentationLift {A : Type*} [CommSemiring A] (f : G R →* A)
    (hadd : ∀ a b : R, f (ofR (a + b)) = f (ofR a) + f (ofR b))
    (hzero : f tau = 0) : G R →+* A where
  toFun := f
  map_one' := f.map_one
  map_zero' := hzero
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

theorem correctedPresentationLift_unique {A : Type*} [CommSemiring A]
    (f : G R →* A)
    (hadd : ∀ a b : R, f (ofR (a + b)) = f (ofR a) + f (ofR b))
    (hzero : f tau = 0) (g : G R →+* A) (hg : ∀ x, g x = f x) :
    g = correctedPresentationLift f hadd hzero := by
  apply RingHom.ext
  exact hg

end SplitZero.Presentation
