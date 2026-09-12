import Mathlib

/-!
# Split-zero scalars

Construction and research direction: KokunoYumeto / u/lepthymo.
This module adapts the earlier `SplitZero.lean` sidecar, preserving its carrier,
operations and names. Source: modern-latex-manuscripts, commit
f7ff59b176c7dc3941babd4cb9272dffc653070d, classical_candidates_20260626.
The arithmetic zero `e = ofR 0` is not the semiring zero `tau`.
No assumption that the coefficient ring is nontrivial is needed here.
-/

namespace SplitZero

universe u

structure G (R : Type u) where
  toOption : Option R
  deriving DecidableEq

variable {R : Type u}

def tau : G R := ⟨none⟩
def ofR (r : R) : G R := ⟨some r⟩
def e [Zero R] : G R := ofR 0

@[simp] theorem ofR_inj {a b : R} : (ofR a : G R) = ofR b ↔ a = b := by
  simp [ofR, G.mk.injEq]

@[simp] theorem ofR_ne_tau (a : R) : (ofR a : G R) ≠ tau := by
  simp [ofR, tau, G.mk.injEq]

section Semiring
variable [CommSemiring R]

protected def add : G R → G R → G R
  | ⟨none⟩, y => y
  | x, ⟨none⟩ => x
  | ⟨some a⟩, ⟨some b⟩ => ⟨some (a + b)⟩

protected def mul : G R → G R → G R
  | ⟨none⟩, _ => ⟨none⟩
  | _, ⟨none⟩ => ⟨none⟩
  | ⟨some a⟩, ⟨some b⟩ => ⟨some (a * b)⟩

instance : Add (G R) := ⟨SplitZero.add⟩
instance : Mul (G R) := ⟨SplitZero.mul⟩
instance : Zero (G R) := ⟨tau⟩
instance : One (G R) := ⟨ofR 1⟩

omit [CommSemiring R] in
@[simp] theorem zero_eq : (0 : G R) = ⟨none⟩ := rfl
@[simp] theorem one_eq : (1 : G R) = ⟨some 1⟩ := rfl
@[simp] theorem mk_none_add (y : G R) : (⟨none⟩ : G R) + y = y := rfl
@[simp] theorem mk_add_none (x : G R) : x + (⟨none⟩ : G R) = x := by
  obtain ⟨_ | a⟩ := x <;> rfl
@[simp] theorem mk_some_add (a b : R) : (⟨some a⟩ : G R) + ⟨some b⟩ = ⟨some (a + b)⟩ := rfl
@[simp] theorem mk_none_mul (y : G R) : (⟨none⟩ : G R) * y = ⟨none⟩ := rfl
@[simp] theorem mk_mul_none (x : G R) : x * (⟨none⟩ : G R) = ⟨none⟩ := by
  obtain ⟨_ | a⟩ := x <;> rfl
@[simp] theorem mk_some_mul (a b : R) : (⟨some a⟩ : G R) * ⟨some b⟩ = ⟨some (a * b)⟩ := rfl

instance instAddCommMonoid : AddCommMonoid (G R) where
  add := (· + ·)
  add_assoc a b c := by
    obtain ⟨_ | a⟩ := a <;> obtain ⟨_ | b⟩ := b <;> obtain ⟨_ | c⟩ := c <;>
      simp [add_assoc]
  zero := 0
  zero_add a := by simp
  add_zero a := by simp
  add_comm a b := by
    obtain ⟨_ | a⟩ := a <;> obtain ⟨_ | b⟩ := b <;> simp [add_comm]
  nsmul := nsmulRec

instance instCommMonoid : CommMonoid (G R) where
  mul := (· * ·)
  mul_assoc a b c := by
    obtain ⟨_ | a⟩ := a <;> obtain ⟨_ | b⟩ := b <;> obtain ⟨_ | c⟩ := c <;>
      simp [mul_assoc]
  one := 1
  one_mul a := by obtain ⟨_ | a⟩ := a <;> simp
  mul_one a := by obtain ⟨_ | a⟩ := a <;> simp
  mul_comm a b := by
    obtain ⟨_ | a⟩ := a <;> obtain ⟨_ | b⟩ := b <;> simp [mul_comm]
  npow := npowRec

instance instCommSemiring : CommSemiring (G R) :=
  { instAddCommMonoid, instCommMonoid with
    left_distrib := by
      intro a b c
      obtain ⟨_ | a⟩ := a <;> obtain ⟨_ | b⟩ := b <;> obtain ⟨_ | c⟩ := c <;>
        simp [mul_add]
    right_distrib := by
      intro a b c
      obtain ⟨_ | a⟩ := a <;> obtain ⟨_ | b⟩ := b <;> obtain ⟨_ | c⟩ := c <;>
        simp [add_mul]
    zero_mul := by intro a; simp
    mul_zero := by intro a; simp }

theorem ofR_add (a b : R) : ofR (a + b) = (ofR a : G R) + ofR b := rfl
theorem ofR_mul (a b : R) : ofR (a * b) = (ofR a : G R) * ofR b := rfl
@[simp] theorem ofR_one : (ofR (1 : R) : G R) = 1 := rfl
@[simp] theorem e_ne_zero : (e : G R) ≠ 0 := ofR_ne_tau 0
@[simp] theorem one_ne_zero : (1 : G R) ≠ 0 := ofR_ne_tau 1
@[simp] theorem e_add_e : (e : G R) + e = e := by simp [e, ofR]
@[simp] theorem e_mul_e : (e : G R) * e = e := by simp [e, ofR]
@[simp] theorem ofR_mul_e (a : R) : (ofR a : G R) * e = e := by simp [e, ofR]
@[simp] theorem e_mul_ofR (a : R) : (e : G R) * ofR a = e := by simp [e, ofR]
@[simp] theorem one_add_e : (1 : G R) + e = 1 := by simp [e, ofR]

/-- Structural zero cannot arise by cancellation of supported summands. -/
theorem add_eq_zero_iff (x y : G R) : x + y = 0 ↔ x = 0 ∧ y = 0 := by
  obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y <;> simp [G.mk.injEq]

/-- Collapse the support distinction. This is not an isomorphism. -/
def reflect : G R →+* R where
  toFun x := x.toOption.getD 0
  map_one' := rfl
  map_zero' := rfl
  map_add' x y := by obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y <;> simp
  map_mul' x y := by obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y <;> simp

@[simp] theorem reflect_ofR (a : R) : reflect (ofR a) = a := rfl
@[simp] theorem reflect_e : reflect (e : G R) = 0 := rfl

theorem ofR_reflect_of_ne_zero (x : G R) (hx : x ≠ 0) : ofR (reflect x) = x := by
  obtain ⟨_ | a⟩ := x
  · exact (hx rfl).elim
  · rfl

end Semiring

/-- Every homomorphism to a ring identifies the supported and structural zeros. -/
theorem hom_kills_e [CommSemiring R] {A : Type*} [CommRing A] (f : G R →+* A) :
    f e = 0 := by
  have hi : f e + f e = f e := by rw [← map_add, e_add_e]
  have he : f e + f e = 0 + f e := by rw [hi, zero_add]
  exact add_right_cancel he

end SplitZero
