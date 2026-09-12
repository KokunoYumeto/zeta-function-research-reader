import SplitZero.Core

/-!
# Intrinsic support, fibre modules and coherent transport

Source: the user's chapter 14, lemmas `gcue-all-idempotents` and
`gcue-fibre-modules`, including the forward morphism construction.
This constructs actual `AddCommGroup`, `Module` and `LinearMap` objects.
It does not claim the reverse reconstruction or the full categorical equivalence.
-/

namespace SplitZero

def support (R : Type*) [CommRing R] {M : Type*}
    [AddCommMonoid M] [Module (G R) M] (m : M) : M := (e : G R) • m

def Skeleton (R M : Type*) [CommRing R] [AddCommMonoid M] [Module (G R) M] :=
  {l : M // support R l = l}

def Fiber (R M : Type*) [CommRing R] [AddCommMonoid M] [Module (G R) M]
    (l : Skeleton R M) := {m : M // support R m = l.val}

section
variable (R : Type*) [CommRing R]
variable {M : Type*} [AddCommMonoid M] [Module (G R) M]

@[simp] theorem support_zero : support R (0 : M) = 0 := smul_zero _

theorem add_support (m : M) : m + support R m = m := by
  change m + (e : G R) • m = m
  calc
    m + (e : G R) • m = (1 : G R) • m + (e : G R) • m := by rw [one_smul]
    _ = ((1 : G R) + e) • m := (add_smul _ _ _).symm
    _ = m := by rw [one_add_e, one_smul]

@[simp] theorem support_add (m n : M) : support R (m + n) = support R m + support R n :=
  smul_add _ _ _

@[simp] theorem support_support (m : M) : support R (support R m) = support R m := by
  change (e : G R) • ((e : G R) • m) = (e : G R) • m
  rw [← mul_smul, e_mul_e]

theorem support_add_self (m : M) : support R m + support R m = support R m := by
  change (e : G R) • m + (e : G R) • m = (e : G R) • m
  rw [← add_smul, e_add_e]

@[simp] theorem support_smul (r : R) (m : M) :
    support R ((ofR r : G R) • m) = support R m := by
  change (e : G R) • ((ofR r : G R) • m) = (e : G R) • m
  rw [← mul_smul, e_mul_ofR]

@[simp] theorem ofR_smul_support (r : R) (m : M) :
    (ofR r : G R) • support R m = support R m := by
  change (ofR r : G R) • ((e : G R) • m) = (e : G R) • m
  rw [← mul_smul, ofR_mul_e]

theorem negation_add (m : M) : (ofR (-1 : R) : G R) • m + m = support R m := by
  calc
    (ofR (-1 : R) : G R) • m + m =
        (ofR (-1 : R) : G R) • m + (1 : G R) • m := by rw [one_smul]
    _ = ((ofR (-1 : R) : G R) + 1) • m := (add_smul _ _ _).symm
    _ = (e : G R) • m := by
      congr 1
      change ofR ((-1 : R) + 1) = ofR 0
      rw [neg_add_cancel]

/-- Support fixed points are precisely the intrinsic additive idempotents. -/
theorem support_eq_self_iff (m : M) : support R m = m ↔ m + m = m := by
  constructor
  · intro h
    calc
      m + m = support R m + support R m := by rw [h]
      _ = support R m := support_add_self R m
      _ = m := h
  · intro h
    have hjoin : m + support R m = support R m := by
      rw [← negation_add R m]
      calc
        m + ((ofR (-1 : R) : G R) • m + m) =
            (ofR (-1 : R) : G R) • m + (m + m) := by ac_rfl
        _ = (ofR (-1 : R) : G R) • m + m := by rw [h]
    exact hjoin.symm.trans (add_support R m)

instance skeletonSemilatticeSup : SemilatticeSup (Skeleton R M) where
  le l m := l.val + m.val = m.val
  le_refl l := (support_eq_self_iff R l.val).mp l.property
  le_trans l m n hlm hmn := by
    change l.val + n.val = n.val
    calc
      l.val + n.val = l.val + (m.val + n.val) := by rw [hmn]
      _ = (l.val + m.val) + n.val := (add_assoc _ _ _).symm
      _ = n.val := by rw [hlm, hmn]
  le_antisymm l m hlm hml := by
    apply Subtype.ext
    exact hml.symm.trans ((add_comm _ _).trans hlm)
  sup l m := ⟨l.val + m.val, by rw [support_add, l.property, m.property]⟩
  le_sup_left l m := by
    change l.val + (l.val + m.val) = l.val + m.val
    rw [← add_assoc, (support_eq_self_iff R l.val).mp l.property]
  le_sup_right l m := by
    change m.val + (l.val + m.val) = l.val + m.val
    calc
      m.val + (l.val + m.val) = l.val + (m.val + m.val) := by ac_rfl
      _ = l.val + m.val := by rw [(support_eq_self_iff R m.val).mp m.property]
  sup_le l m n hln hmn := by
    change (l.val + m.val) + n.val = n.val
    rw [add_assoc, hmn, hln]

instance skeletonOrderBot : OrderBot (Skeleton R M) where
  bot := ⟨0, support_zero R⟩
  bot_le l := zero_add l.val

theorem skeleton_smul (r : R) (l : Skeleton R M) : (ofR r : G R) • l.val = l.val := by
  calc
    (ofR r : G R) • l.val = (ofR r : G R) • support R l.val := by rw [l.property]
    _ = support R l.val := ofR_smul_support R r l.val
    _ = l.val := l.property

/-- Each fibre has its own additive zero, namely its support label. -/
instance fiberAddCommGroup (l : Skeleton R M) : AddCommGroup (Fiber R M l) where
  add x y := ⟨x.val + y.val, by
    rw [support_add, x.property, y.property]
    exact (support_eq_self_iff R l.val).mp l.property⟩
  zero := ⟨l.val, l.property⟩
  neg x := ⟨(ofR (-1 : R) : G R) • x.val, (support_smul R _ _).trans x.property⟩
  add_assoc x y z := Subtype.ext (add_assoc x.val y.val z.val)
  zero_add x := by
    apply Subtype.ext
    change l.val + x.val = x.val
    rw [← x.property, add_comm]
    exact add_support R x.val
  add_zero x := by
    apply Subtype.ext
    change x.val + l.val = x.val
    rw [← x.property]
    exact add_support R x.val
  add_comm x y := Subtype.ext (add_comm x.val y.val)
  neg_add_cancel x := Subtype.ext ((negation_add R x.val).trans x.property)
  nsmul := nsmulRec
  zsmul := zsmulRec

/-- The supported scalar action becomes an ordinary coefficient-ring module on each fibre. -/
instance fiberModule (l : Skeleton R M) : Module R (Fiber R M l) where
  smul r x := ⟨(ofR r : G R) • x.val, (support_smul R r x.val).trans x.property⟩
  one_smul x := by
    apply Subtype.ext
    change (ofR (1 : R) : G R) • x.val = x.val
    rw [ofR_one, one_smul]
  mul_smul r s x := by
    apply Subtype.ext
    change (ofR (r * s) : G R) • x.val = (ofR r : G R) • ((ofR s : G R) • x.val)
    rw [ofR_mul, mul_smul]
  smul_zero r := Subtype.ext (skeleton_smul R r l)
  smul_add r x y := Subtype.ext (smul_add (ofR r : G R) x.val y.val)
  zero_smul x := Subtype.ext x.property
  add_smul r s x := by
    apply Subtype.ext
    change (ofR (r + s) : G R) • x.val = (ofR r : G R) • x.val + (ofR s : G R) • x.val
    rw [ofR_add, add_smul]

/-- The canonical transport along the support order. -/
def transport (l m : Skeleton R M) (hlm : l ≤ m) : Fiber R M l →ₗ[R] Fiber R M m where
  toFun x := ⟨x.val + m.val, by
    rw [support_add, x.property, m.property]
    exact hlm⟩
  map_add' x y := by
    apply Subtype.ext
    change (x.val + y.val) + m.val = (x.val + m.val) + (y.val + m.val)
    calc
      (x.val + y.val) + m.val = (x.val + y.val) + (m.val + m.val) := by
        rw [(support_eq_self_iff R m.val).mp m.property]
      _ = (x.val + m.val) + (y.val + m.val) := by ac_rfl
  map_smul' r x := by
    apply Subtype.ext
    change (ofR r : G R) • x.val + m.val = (ofR r : G R) • (x.val + m.val)
    rw [smul_add, skeleton_smul R r m]

theorem transport_refl (l : Skeleton R M) : transport R l l le_rfl = LinearMap.id := by
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  change x.val + l.val = x.val
  rw [← x.property]
  exact add_support R x.val

theorem transport_trans (l m n : Skeleton R M) (hlm : l ≤ m) (hmn : m ≤ n) :
    (transport R m n hmn).comp (transport R l m hlm) = transport R l n (le_trans hlm hmn) := by
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  change (x.val + m.val) + n.val = x.val + n.val
  rw [add_assoc, hmn]

variable {N : Type*} [AddCommMonoid N] [Module (G R) N]

theorem support_map (f : M →ₗ[G R] N) (m : M) : support R (f m) = f (support R m) :=
  (f.map_smul (e : G R) m).symm

def skeletonMap (f : M →ₗ[G R] N) (l : Skeleton R M) : Skeleton R N :=
  ⟨f l.val, by rw [support_map, l.property]⟩

theorem skeletonMap_mono (f : M →ₗ[G R] N) {l m : Skeleton R M} (h : l ≤ m) :
    skeletonMap R f l ≤ skeletonMap R f m := by
  change f l.val + f m.val = f m.val
  rw [← map_add, h]

def fiberMap (f : M →ₗ[G R] N) (l : Skeleton R M) :
    Fiber R M l →ₗ[R] Fiber R N (skeletonMap R f l) where
  toFun x := ⟨f x.val, by rw [support_map, x.property]; rfl⟩
  map_add' x y := Subtype.ext (f.map_add x.val y.val)
  map_smul' r x := Subtype.ext (f.map_smul (ofR r : G R) x.val)

/-- Actual fibre maps commute with actual transport, not merely with a supplied square. -/
theorem fiberMap_transport (f : M →ₗ[G R] N) (l m : Skeleton R M) (h : l ≤ m) :
    (fiberMap R f m).comp (transport R l m h) =
      (transport R (skeletonMap R f l) (skeletonMap R f m) (skeletonMap_mono R f h)).comp
        (fiberMap R f l) := by
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  exact f.map_add x.val m.val

end

end SplitZero
