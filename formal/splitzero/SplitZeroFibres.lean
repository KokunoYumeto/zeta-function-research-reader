import SplitZeroExtension

/-!
# Support fibres as actual modules, with coherent linear transport

Formalizes the forward structural construction in Zeta chapter 14. The reverse
construction for an arbitrary diagram and the category equivalence are not claimed here.
-/

namespace SplitZero.Diagram
open SplitZero.Extension

variable {R M : Type*} [CommRing R] [AddCommMonoid M] [Module (G R) M]

/-- Intrinsic support labels: fixed points of the supported-zero action. -/
def Support (R M : Type*) [CommRing R] [AddCommMonoid M] [Module (G R) M] :=
  {l : M // support (R := R) l = l}

theorem label_idempotent (l : Support R M) : l.val + l.val = l.val :=
  (support_eq_self_iff l.val).mp l.property

instance : SemilatticeSup (Support R M) where
  le l k := l.val + k.val = k.val
  le_refl l := label_idempotent l
  le_trans l k n hlk hkn := by
    calc
      l.val + n.val = l.val + (k.val + n.val) := by rw [hkn]
      _ = (l.val + k.val) + n.val := (add_assoc _ _ _).symm
      _ = n.val := by rw [hlk, hkn]
  le_antisymm l k hlk hkl := by
    apply Subtype.ext
    calc
      l.val = k.val + l.val := hkl.symm
      _ = l.val + k.val := add_comm _ _
      _ = k.val := hlk
  sup l k := ⟨l.val + k.val, by rw [support_add, l.property, k.property]⟩
  le_sup_left l k := by
    change l.val + (l.val + k.val) = l.val + k.val
    rw [← add_assoc, label_idempotent l]
  le_sup_right l k := by
    change k.val + (l.val + k.val) = l.val + k.val
    calc
      k.val + (l.val + k.val) = l.val + (k.val + k.val) := by ac_rfl
      _ = l.val + k.val := by rw [label_idempotent k]
  sup_le l k n hln hkn := by
    change (l.val + k.val) + n.val = n.val
    rw [add_assoc, hkn, hln]

instance : OrderBot (Support R M) where
  bot := ⟨0, support_zero⟩
  bot_le l := zero_add l.val

/-- A fibre over a label. Its own zero is that label, not generally `0 : M`. -/
def Fiber (l : Support R M) := {m : M // support (R := R) m = l.val}

variable (l : Support R M)

instance : Zero (Fiber l) := ⟨⟨l.val, l.property⟩⟩
instance : Add (Fiber l) := ⟨fun x y =>
  ⟨x.val + y.val, by rw [support_add, x.property, y.property, label_idempotent l]⟩⟩
instance : Neg (Fiber l) := ⟨fun x =>
  ⟨(ofR (-1 : R) : G R) • x.val, by rw [support_ofR_smul, x.property]⟩⟩

instance fiberAddCommGroup : AddCommGroup (Fiber l) where
  add := (· + ·)
  zero := 0
  neg := Neg.neg
  add_assoc x y z := Subtype.ext (add_assoc _ _ _)
  add_comm x y := Subtype.ext (add_comm _ _)
  zero_add x := by
    apply Subtype.ext
    change l.val + x.val = x.val
    exact (add_comm l.val x.val).trans
      ((congrArg (fun z : M => x.val + z) x.property.symm).trans (add_support x.val))
  add_zero x := by
    apply Subtype.ext
    change x.val + l.val = x.val
    exact (congrArg (fun z : M => x.val + z) x.property.symm).trans (add_support x.val)
  neg_add_cancel x := by
    apply Subtype.ext
    change (ofR (-1 : R) : G R) • x.val + x.val = l.val
    calc
      (ofR (-1 : R) : G R) • x.val + x.val =
          ((ofR (-1 : R) : G R) + 1) • x.val := by rw [add_smul, one_smul]
      _ = support (R := R) x.val := by
        change ((ofR (-1 : R) : G R) + ofR 1) • x.val = (ofR 0 : G R) • x.val
        rw [← ofR_add, neg_add_cancel]
      _ = l.val := x.property
  nsmul := nsmulRec
  zsmul := zsmulRec

instance : SMul R (Fiber l) := ⟨fun r x =>
  ⟨(ofR r : G R) • x.val, by rw [support_ofR_smul, x.property]⟩⟩

instance fiberModule : Module R (Fiber l) where
  one_smul x := by
    apply Subtype.ext
    change (ofR (1 : R) : G R) • x.val = x.val
    rw [ofR_one, one_smul]
  mul_smul r s x := by
    apply Subtype.ext
    change (ofR (r * s) : G R) • x.val = (ofR r : G R) • ((ofR s : G R) • x.val)
    rw [ofR_mul, mul_smul]
  smul_zero r := by
    apply Subtype.ext
    change (ofR r : G R) • l.val = l.val
    rw [← l.property]
    exact ofR_smul_support r l.val
  smul_add r x y := Subtype.ext (smul_add (ofR r : G R) x.val y.val)
  add_smul r s x := by
    apply Subtype.ext
    change (ofR (r + s) : G R) • x.val = (ofR r : G R) • x.val + (ofR s : G R) • x.val
    rw [ofR_add, add_smul]
  zero_smul x := Subtype.ext x.property

@[simp] theorem fiber_zero_val : (0 : Fiber l).val = l.val := rfl
@[simp] theorem fiber_add_val (x y : Fiber l) : (x + y).val = x.val + y.val := rfl
@[simp] theorem fiber_smul_val (r : R) (x : Fiber l) : (r • x).val = (ofR r : G R) • x.val := rfl

variable {l}

/-- The exact transport in the source, now an actual `LinearMap`. -/
def transport {l k : Support R M} (h : l ≤ k) : Fiber l →ₗ[R] Fiber k where
  toFun x := ⟨x.val + k.val, by rw [support_add, x.property, k.property]; exact h⟩
  map_add' x y := by
    apply Subtype.ext
    change (x.val + y.val) + k.val = (x.val + k.val) + (y.val + k.val)
    calc
      (x.val + y.val) + k.val = (x.val + y.val) + (k.val + k.val) := by rw [label_idempotent k]
      _ = (x.val + k.val) + (y.val + k.val) := by ac_rfl
  map_smul' r x := by
    apply Subtype.ext
    change (ofR r : G R) • x.val + k.val = (ofR r : G R) • (x.val + k.val)
    have hk : (ofR r : G R) • k.val = k.val := by
      rw [← k.property]
      exact ofR_smul_support r k.val
    rw [smul_add, hk]

theorem transport_self (l : Support R M) : transport (le_refl l) = LinearMap.id := by
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  change x.val + l.val = x.val
  exact (congrArg (fun z : M => x.val + z) x.property.symm).trans (add_support x.val)

theorem transport_comp {l k n : Support R M} (h : l ≤ k) (h' : k ≤ n) :
    (transport h').comp (transport h) = transport (le_trans h h') := by
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  change (x.val + k.val) + n.val = x.val + n.val
  rw [add_assoc, show k.val + n.val = n.val from h']

variable {N : Type*} [AddCommMonoid N] [Module (G R) N]

/-- Restriction of a split-linear map to the support labels. -/
def mapSupport (f : M →ₗ[G R] N) (l : Support R M) : Support R N :=
  ⟨f l.val, (map_support f l.val).symm.trans (congrArg f l.property)⟩

theorem mapSupport_mono (f : M →ₗ[G R] N) {l k : Support R M} (h : l ≤ k) :
    mapSupport f l ≤ mapSupport f k := by
  change f l.val + f k.val = f k.val
  rw [← f.map_add, show l.val + k.val = k.val from h]

/-- The fibre restriction is genuinely linear over the original ring. -/
def fiberMap (f : M →ₗ[G R] N) (l : Support R M) : Fiber l →ₗ[R] Fiber (mapSupport f l) where
  toFun x := ⟨f x.val, (map_support f x.val).symm.trans (congrArg f x.property)⟩
  map_add' x y := Subtype.ext (f.map_add x.val y.val)
  map_smul' r x := Subtype.ext (f.map_smul (ofR r) x.val)

/-- Naturality square for transports and every split-linear map. -/
theorem fiberMap_transport (f : M →ₗ[G R] N) {l k : Support R M}
    (h : l ≤ k) (x : Fiber l) :
    fiberMap f k (transport h x) = transport (mapSupport_mono f h) (fiberMap f l x) := by
  apply Subtype.ext
  exact f.map_add x.val k.val

/-- Every element is recovered from its intrinsic support and fibre coordinate. -/
def fiberDecomposition : M ≃ Σ l : Support R M, Fiber l where
  toFun m := ⟨⟨support (R := R) m, support_support m⟩, ⟨m, rfl⟩⟩
  invFun x := x.2.val
  left_inv _ := rfl
  right_inv x := by
    rcases x with ⟨⟨l, hl⟩, ⟨m, hm⟩⟩
    cases hm
    rfl

/-- The source's reconstructed sum is exactly the original ambient sum. -/
theorem reconstruct_add (m n : M) :
    let x := fiberDecomposition (R := R) m
    let y := fiberDecomposition (R := R) n
    (transport (le_sup_left : x.1 ≤ x.1 ⊔ y.1) x.2 +
      transport (le_sup_right : y.1 ≤ x.1 ⊔ y.1) y.2).val = m + n := by
  change (m + (support (R := R) m + support (R := R) n)) +
    (n + (support (R := R) m + support (R := R) n)) = m + n
  rw [← support_add]
  calc
    (m + support (R := R) (m + n)) + (n + support (R := R) (m + n)) =
        (m + n) + (support (R := R) (m + n) + support (R := R) (m + n)) := by ac_rfl
    _ = m + n := by rw [support_add_self, add_support]

end SplitZero.Diagram
