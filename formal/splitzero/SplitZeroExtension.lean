import SplitZero

/-!
# Structural extension of the owner's split-zero construction

The original core is materialized unchanged by `prepare.py` at its recorded Git blob.
Source statements: Zeta reader, chapter 14, support skeleton and ideal lattice.
This module does not assert a completed categorical equivalence or any analytic theorem.
-/

namespace SplitZero.Extension

variable {R : Type*} [CommRing R]

@[simp] theorem ofR_add (a b : R) : (ofR (a + b) : G R) = ofR a + ofR b := rfl
@[simp] theorem ofR_mul (a b : R) : (ofR (a * b) : G R) = ofR a * ofR b := rfl
@[simp] theorem ofR_one : (ofR (1 : R) : G R) = 1 := rfl
@[simp] theorem e_mul_ofR (r : R) : (e : G R) * ofR r = e := by
  change ofR (0 * r) = ofR 0
  rw [zero_mul]
@[simp] theorem ofR_mul_e (r : R) : (ofR r : G R) * e = e := by
  rw [mul_comm, e_mul_ofR]
@[simp] theorem e_mul_e : (e : G R) * e = e := e_mul_ofR 0
@[simp] theorem one_add_e : (1 : G R) + e = 1 := by
  change ofR (1 + 0 : R) = ofR 1
  rw [add_zero]

section Reflection
variable {A : Type*} [CommRing A]

/-- Restriction of a map to a ring kills the supported zero, hence is a ring map. -/
def restrictToRing (h : G R →+* A) : R →+* A where
  toFun r := h (ofR r)
  map_zero' := hom_kills_e h
  map_one' := h.map_one
  map_add' a b := by rw [ofR_add, h.map_add]
  map_mul' a b := by rw [ofR_mul, h.map_mul]

/-- Exact universal property of the amplitude/ring reflection. -/
def ringHomEquiv : (G R →+* A) ≃ (R →+* A) where
  toFun := restrictToRing
  invFun f := f.comp reflect
  left_inv h := by
    ext x
    obtain ⟨_ | r⟩ := x
    · change h (ofR 0) = h 0
      rw [hom_kills_e h, h.map_zero]
    · rfl
  right_inv f := by ext r; rfl

/-- Every map into a ring factors uniquely through `reflect`. -/
theorem existsUnique_ring_factor (h : G R →+* A) :
    ∃! f : R →+* A, f.comp reflect = h := by
  refine ⟨restrictToRing h, (ringHomEquiv.left_inv h), ?_⟩
  intro f hf
  have hh := congrArg restrictToRing hf
  exact hh

end Reflection

section Semimodule
variable {M : Type*} [AddCommMonoid M] [Module (G R) M]

/-- The supported-zero action, not the global additive zero. -/
def support (m : M) : M := (e : G R) • m

@[simp] theorem support_zero : support (R := R) (0 : M) = 0 := smul_zero _
@[simp] theorem support_add (m n : M) :
    support (R := R) (m + n) = support (R := R) m + support (R := R) n := smul_add _ _ _
@[simp] theorem support_support (m : M) :
    support (R := R) (support (R := R) m) = support (R := R) m := by
  unfold support
  rw [← mul_smul, e_mul_e]
@[simp] theorem add_support (m : M) : m + support (R := R) m = m := by
  calc
    m + (e : G R) • m = (1 : G R) • m + (e : G R) • m := by rw [one_smul]
    _ = ((1 : G R) + e) • m := (add_smul _ _ _).symm
    _ = m := by rw [one_add_e, one_smul]
@[simp] theorem support_add_self (m : M) :
    support (R := R) m + support (R := R) m = support (R := R) m := by
  unfold support
  rw [← add_smul, e_add_e]
@[simp] theorem support_ofR_smul (r : R) (m : M) :
    support (R := R) ((ofR r : G R) • m) = support (R := R) m := by
  unfold support
  rw [← mul_smul, e_mul_ofR]
@[simp] theorem ofR_smul_support (r : R) (m : M) :
    (ofR r : G R) • support (R := R) m = support (R := R) m := by
  unfold support
  rw [← mul_smul, ofR_mul_e]

/-- Support is exactly the additive-idempotent locus, for every semimodule. -/
theorem support_eq_self_iff (m : M) : support (R := R) m = m ↔ m + m = m := by
  constructor
  · intro h
    simpa only [h] using support_add_self (R := R) m
  · intro h
    have hn : support (R := R) m = m + (ofR (-1 : R) : G R) • m := by
      calc
        (e : G R) • m = (ofR (1 + -1 : R) : G R) • m := by simp [e]
        _ = m + (ofR (-1 : R) : G R) • m := by rw [ofR_add, add_smul, ofR_one, one_smul]
    calc
      support (R := R) m = m + (ofR (-1 : R) : G R) • m := hn
      _ = (m + m) + (ofR (-1 : R) : G R) • m := by rw [h]
      _ = m + (m + (ofR (-1 : R) : G R) • m) := add_assoc _ _ _
      _ = m + support (R := R) m := by rw [← hn]
      _ = m := add_support m

/-- In a cancellative ambient additive monoid, support necessarily vanishes. -/
theorem support_eq_zero_of_cancel [IsCancelAdd M] (m : M) : support (R := R) m = 0 := by
  apply add_left_cancel (a := m)
  simpa using add_support (R := R) m

/-- A split-linear map commutes with the support operation. -/
theorem map_support {N : Type*} [AddCommMonoid N] [Module (G R) N]
    (f : M →ₗ[G R] N) (m : M) : f (support (R := R) m) = support (R := R) (f m) :=
  f.map_smul _ _

end Semimodule

section Ideals

/-- Lift a ring ideal without erasing the distinction between `tau` and `e`. -/
def liftIdeal (I : Ideal R) : Ideal (G R) := Ideal.comap reflect I

@[simp] theorem ofR_mem_liftIdeal (I : Ideal R) (r : R) : ofR r ∈ liftIdeal I ↔ r ∈ I := Iff.rfl
@[simp] theorem e_mem_liftIdeal (I : Ideal R) : (e : G R) ∈ liftIdeal I := I.zero_mem

theorem liftIdeal_ne_bot (I : Ideal R) : liftIdeal I ≠ ⊥ := by
  intro h
  have he := e_mem_liftIdeal I
  rw [h, Ideal.mem_bot] at he
  exact e_ne_tau he

theorem liftIdeal_le_iff (I K : Ideal R) : liftIdeal I ≤ liftIdeal K ↔ I ≤ K := by
  constructor
  · intro h r hr
    exact h (show ofR r ∈ liftIdeal I from hr)
  · intro h x hx
    exact h hx

theorem liftIdeal_injective : Function.Injective (liftIdeal (R := R)) := by
  intro I K h
  apply le_antisymm
  · exact (liftIdeal_le_iff I K).mp (le_of_eq h)
  · exact (liftIdeal_le_iff K I).mp (le_of_eq h.symm)

/-- Every non-bottom semiring ideal contains the supported zero. -/
theorem e_mem_of_ne_bot (J : Ideal (G R)) (hJ : J ≠ ⊥) : (e : G R) ∈ J := by
  obtain ⟨x, hx, hxbot⟩ := SetLike.exists_of_lt (bot_lt_iff_ne_bot.mpr hJ)
  obtain ⟨_ | r⟩ := x
  · exact False.elim (hxbot (show (0 : G R) ∈ (⊥ : Ideal (G R)) from Ideal.zero_mem _))
  · have hh := J.mul_mem_left (e : G R) hx
    simpa only [← ofR_eq, e_mul_ofR] using hh

/-- Restriction is an ideal only after membership of the supported zero is established. -/
def lowerIdeal (J : Ideal (G R)) (he : (e : G R) ∈ J) : Ideal R where
  carrier := {r | ofR r ∈ J}
  zero_mem' := he
  add_mem' := by
    intro a b ha hb
    change ofR (a + b) ∈ J
    rw [ofR_add]
    exact J.add_mem ha hb
  smul_mem' := by
    intro a b hb
    change ofR (a * b) ∈ J
    rw [ofR_mul]
    exact J.mul_mem_left (ofR a) hb

theorem lift_lowerIdeal (J : Ideal (G R)) (he : (e : G R) ∈ J) :
    liftIdeal (lowerIdeal J he) = J := by
  ext x
  obtain ⟨_ | r⟩ := x
  · change (0 : G R) ∈ liftIdeal (lowerIdeal J he) ↔ (0 : G R) ∈ J
    simp
  · rfl

/-- The complete, disjoint ideal classification. -/
theorem ideal_classification (J : Ideal (G R)) :
    J = ⊥ ∨ ∃! I : Ideal R, liftIdeal I = J := by
  by_cases hJ : J = ⊥
  · exact Or.inl hJ
  · right
    refine ⟨lowerIdeal J (e_mem_of_ne_bot J hJ), lift_lowerIdeal J _, ?_⟩
    intro I hI
    exact liftIdeal_injective (hI.trans (lift_lowerIdeal J _).symm)

/-- The target is the non-bottom ideal poset, not the whole ideal lattice. -/
def nonzeroIdealOrderIso : Ideal R ≃o {J : Ideal (G R) // J ≠ ⊥} where
  toFun I := ⟨liftIdeal I, liftIdeal_ne_bot I⟩
  invFun J := lowerIdeal J.1 (e_mem_of_ne_bot J.1 J.2)
  left_inv I := by ext r; rfl
  right_inv J := by apply Subtype.ext; exact lift_lowerIdeal _ _
  map_rel_iff' := by intro I K; exact liftIdeal_le_iff I K

/-- The empty join in the ambient ideal lattice is NOT preserved by lifting. -/
theorem lift_bottom_not_ambient_bottom : liftIdeal (⊥ : Ideal R) ≠ ⊥ := liftIdeal_ne_bot _

end Ideals

end SplitZero.Extension
