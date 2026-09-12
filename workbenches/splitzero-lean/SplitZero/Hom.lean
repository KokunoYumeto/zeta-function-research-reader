import SplitZero.Core

/-!
# Reflection and recovery of all morphisms

This extends the user's split-zero scalar construction, not the analytic zeta
claims. The equivalences below are equivalences of actual homomorphism types.
A categorical equivalence of all semimodules is a separate development.
-/

namespace SplitZero

variable {R S A : Type*}

section Lift
variable [CommSemiring R] [CommSemiring S]

/-- Apply a coefficient homomorphism without forgetting support. -/
def lift (f : R →+* S) : G R →+* G S where
  toFun x := match x with
    | ⟨none⟩ => 0
    | ⟨some r⟩ => ofR (f r)
  map_zero' := rfl
  map_one' := by change ofR (f 1) = ofR 1; rw [map_one]
  map_add' x y := by
    obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y
    · rfl
    · rfl
    · rfl
    · change ofR (f (a + b)) = ofR (f a + f b); rw [map_add]
  map_mul' x y := by
    obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y
    · rfl
    · rfl
    · rfl
    · change ofR (f (a * b)) = ofR (f a * f b); rw [map_mul]

@[simp] theorem lift_ofR (f : R →+* S) (r : R) : lift f (ofR r) = ofR (f r) := rfl
@[simp] theorem lift_e (f : R →+* S) : lift f e = e := by
  change ofR (f 0) = ofR 0
  rw [map_zero]

theorem lift_id : lift (RingHom.id R) = RingHom.id (G R) := by
  ext x
  obtain ⟨_ | a⟩ := x <;> rfl

theorem lift_comp {T : Type*} [CommSemiring T] (g : S →+* T) (f : R →+* S) :
    lift (g.comp f) = (lift g).comp (lift f) := by
  ext x
  obtain ⟨_ | a⟩ := x <;> rfl

end Lift

section Reflection
variable [CommRing R] [CommRing A]

/-- Restrict a homomorphism to a ring after its supported zero has been killed. -/
def toRing (f : G R →+* A) : R →+* A where
  toFun r := f (ofR r)
  map_zero' := hom_kills_e f
  map_one' := f.map_one
  map_add' a b := f.map_add (ofR a) (ofR b)
  map_mul' a b := f.map_mul (ofR a) (ofR b)

/-- The full universal property of the ring reflection. -/
def ringHomEquiv : (G R →+* A) ≃ (R →+* A) where
  toFun := toRing
  invFun f := f.comp reflect
  left_inv f := by
    ext x
    obtain ⟨_ | a⟩ := x
    · change (toRing f) 0 = f 0
      simp
    · rfl
  right_inv f := by ext r; rfl

/-- Existence and uniqueness, without requiring clients to unpack the equivalence. -/
theorem existsUnique_factor_through_reflect (f : G R →+* A) :
    ∃! g : R →+* A, g.comp reflect = f := by
  refine ⟨toRing f, (ringHomEquiv (R := R) (A := A)).left_inv f, ?_⟩
  intro g hg
  have h := congrArg toRing hg
  exact h

end Reflection

section Recovery
variable [CommRing R] [CommRing S]

/-- Every semiring homomorphism between split-zero rings preserves support. -/
theorem hom_ofR_ne_zero (f : G R →+* G S) (r : R) : f (ofR r) ≠ 0 := by
  have he : f (e : G R) ≠ 0 := by
    intro he
    have hsum : (1 : G R) + ofR (-1 : R) = e := by
      change ofR (1 + (-1 : R)) = ofR 0
      rw [add_neg_cancel]
    have hz : (1 : G S) + f (ofR (-1 : R)) = 0 := by
      rw [← f.map_one, ← map_add, hsum, he]
    exact one_ne_zero ((add_eq_zero_iff _ _).mp hz).1
  intro hr
  apply he
  calc
    f e = f ((ofR r : G R) * e) := by rw [ofR_mul_e]
    _ = f (ofR r) * f e := f.map_mul _ _
    _ = 0 := by rw [hr, zero_mul]

/-- Recover the coefficient-ring homomorphism from an arbitrary split-zero hom. -/
def lower (f : G R →+* G S) : R →+* S := toRing (reflect.comp f)

/-- Full faithfulness at the level of hom sets; no support-preservation hypothesis is needed. -/
def homEquiv : (R →+* S) ≃ (G R →+* G S) where
  toFun := lift
  invFun := lower
  left_inv f := by ext r; rfl
  right_inv f := by
    ext x
    obtain ⟨_ | r⟩ := x
    · change (0 : G S) = f 0
      simp
    · change ofR (reflect (f (ofR r))) = f (ofR r)
      exact ofR_reflect_of_ne_zero _ (hom_ofR_ne_zero f r)

theorem hom_preserves_e (f : G R →+* G S) : f e = e := by
  rw [← (homEquiv (R := R) (S := S)).right_inv f]
  exact lift_e _

end Recovery

end SplitZero
