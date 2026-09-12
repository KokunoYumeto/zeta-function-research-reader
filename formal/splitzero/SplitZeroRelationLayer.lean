import SplitZeroHomology
import Mathlib.Analysis.InnerProductSpace.Projection.Basic

/-!
# The next admitted relation and the original quotient transport

Quotients are by the specified submodules, not by closures and not by all
theta relations at once. The layer isomorphism uses the actual orthogonal
projection. The ambient inner-product space need not be finite dimensional.
-/

noncomputable section
namespace SplitZero.RelationLayer

universe u v
variable {R : Type u} [CommRing R]
  {B : Type v} [AddCommGroup B] [Module R B]

def transport (U W : Submodule R B) (h : U ≤ W) :
    (B ⧸ U) →ₗ[R] (B ⧸ W) :=
  U.mapQ W LinearMap.id h

@[simp] theorem transport_mk (U W : Submodule R B) (h : U ≤ W) (x : B) :
    transport U W h (U.mkQ x) = W.mkQ x := rfl

theorem transport_kills_iff (U W : Submodule R B) (h : U ≤ W) (x : B) :
    transport U W h (U.mkQ x) = 0 ↔ x ∈ W :=
  Submodule.Quotient.mk_eq_zero W

/-- Reuse the already checked comparison-kernel equivalence. -/
def kernelEquiv (U W : Submodule R B) (h : U ≤ W) :
    (SplitZero.Homology.Killing W (LinearMap.id : B →ₗ[R] B) ⧸
      SplitZero.Homology.OldRelations U W LinearMap.id)
        ≃ₗ[R] LinearMap.ker (transport U W h) :=
  SplitZero.Homology.quotientKernelEquiv U W LinearMap.id h

/-- A derivative is allowed to increase the admitted relation level. -/
def derivative (U W : Submodule R B) (D : B →ₗ[R] B)
    (hD : U ≤ W.comap D) : (B ⧸ U) →ₗ[R] (B ⧸ W) :=
  U.mapQ W D hD

@[simp] theorem derivative_mk (U W : Submodule R B) (D : B →ₗ[R] B)
    (hD : U ≤ W.comap D) (x : B) :
    derivative U W D hD (U.mkQ x) = W.mkQ (D x) := rfl

/-- The old component vanishes, but the new relation class is still recorded. -/
theorem boundary_class (U : Submodule R B) (old u : B) (a : R)
    (ho : old ∈ U) :
    U.mkQ (old - a • u) = -(a • U.mkQ u) := by
  have hz : U.mkQ old = 0 := (Submodule.Quotient.mk_eq_zero U).mpr ho
  rw [map_sub, map_smul, hz, zero_sub]

theorem boundary_dies_next (U W : Submodule R B) (h : U ≤ W)
    (old u : B) (a : R) (ho : old ∈ U) (hu : u ∈ W) :
    transport U W h (U.mkQ (old - a • u)) = 0 := by
  apply (transport_kills_iff U W h _).mpr
  exact W.sub_mem (h ho) (W.smul_mem a hu)

section OneDimensional
variable {k : Type u} [Field k]
  {M : Type v} [AddCommGroup M] [Module k M]

theorem class_smul_nonzero_iff (U : Submodule k M) (u : M) (hu : u ∉ U) (a : k) :
    U.mkQ (a • u) ≠ 0 ↔ a ≠ 0 := by
  have hq : U.mkQ u ≠ 0 := by
    intro h
    exact hu ((Submodule.Quotient.mk_eq_zero U).mp h)
  rw [map_smul]
  simp only [ne_eq, smul_eq_zero, hq, or_false]

def scalarKernel (U W : Submodule k M) (h : U ≤ W) (u : M) (hu : u ∈ W) :
    k →ₗ[k] LinearMap.ker (transport U W h) where
  toFun a := ⟨U.mkQ (a • u),
    (transport_kills_iff U W h _).mpr (W.smul_mem a hu)⟩
  map_add' a b := by
    apply Subtype.ext
    change U.mkQ ((a+b) • u) = U.mkQ (a • u) + U.mkQ (b • u)
    rw [add_smul, map_add]
  map_smul' a b := by
    apply Subtype.ext
    change U.mkQ ((a*b) • u) = a • U.mkQ (b • u)
    rw [mul_smul, map_smul]

theorem scalarKernel_bijective (U W : Submodule k M) (h : U ≤ W)
    (u : M) (hu : u ∈ W) (hnot : u ∉ U)
    (hspan : W = U ⊔ Submodule.span k {u}) :
    Function.Bijective (scalarKernel U W h u hu) := by
  constructor
  · intro a b hab
    have hh : U.mkQ (a • u) = U.mkQ (b • u) := congrArg Subtype.val hab
    have hz : U.mkQ ((a-b) • u) = 0 := by
      rw [sub_smul, map_sub, hh, sub_self]
    by_contra hn
    exact ((class_smul_nonzero_iff U u hnot (a-b)).mpr (sub_ne_zero.mpr hn)) hz
  · rintro ⟨x, hx⟩
    obtain ⟨y, rfl⟩ := Submodule.Quotient.mk_surjective U x
    have hy : y ∈ W := (transport_kills_iff U W h y).mp hx
    rw [hspan] at hy
    obtain ⟨l, hl, z, hz, hy⟩ := Submodule.mem_sup.mp hy
    obtain ⟨a, rfl⟩ := Submodule.mem_span_singleton.mp hz
    refine ⟨a, ?_⟩
    apply Subtype.ext
    change U.mkQ (a • u) = U.mkQ y
    have hlq : U.mkQ l = 0 := (Submodule.Quotient.mk_eq_zero U).mpr hl
    rw [← hy, map_add, hlq, zero_add]

/-- The entire kernel is one scalar coordinate, with both inverse laws. -/
def oneNewRelationEquiv (U W : Submodule k M) (h : U ≤ W)
    (u : M) (hu : u ∈ W) (hnot : u ∉ U)
    (hspan : W = U ⊔ Submodule.span k {u}) :
    k ≃ₗ[k] LinearMap.ker (transport U W h) :=
  LinearEquiv.ofBijective (scalarKernel U W h u hu)
    (scalarKernel_bijective U W h u hu hnot hspan)

@[simp] theorem oneNewRelationEquiv_apply (U W : Submodule k M) (h : U ≤ W)
    (u : M) (hu : u ∈ W) (hnot : u ∉ U)
    (hspan : W = U ⊔ Submodule.span k {u}) (a : k) :
    (oneNewRelationEquiv U W h u hu hnot hspan a).val = U.mkQ (a • u) := rfl
end OneDimensional

section Orthogonal
variable {H : Type v} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
variable (U W : Submodule ℂ H) [U.HasOrthogonalProjection] (h : U ≤ W)

/-- This is literally z |-> z-P_U z on the next relation space. -/
def residual : W →ₗ[ℂ] (W ⊓ Uᗮ : Submodule ℂ H) where
  toFun z := ⟨z.val - U.starProjection z.val,
    W.sub_mem z.property (h (U.starProjection_apply_mem _)),
    U.sub_starProjection_mem_orthogonal z.val⟩
  map_add' x y := by
    apply Subtype.ext
    simp only [Submodule.coe_add, map_add]
    abel
  map_smul' a x := by
    apply Subtype.ext
    change a • x.val - U.starProjection (a • x.val) =
      a • (x.val - U.starProjection x.val)
    rw [map_smul, smul_sub]

def layerMap :
    (W ⧸ U.comap W.subtype) →ₗ[ℂ] (W ⊓ Uᗮ : Submodule ℂ H) :=
  (U.comap W.subtype).liftQ (residual U W h) (by
    intro z hz
    apply Subtype.ext
    change z.val - U.starProjection z.val = 0
    change z.val ∈ U at hz
    rw [U.starProjection_eq_self_iff.mpr hz, sub_self])

theorem layerMap_bijective : Function.Bijective (layerMap U W h) := by
  constructor
  · intro x y he
    induction x using Submodule.Quotient.induction_on with
    | _ x =>
      induction y using Submodule.Quotient.induction_on with
      | _ y =>
        apply (Submodule.Quotient.eq (U.comap W.subtype)).mpr
        change x.val - y.val ∈ U
        apply (Submodule.Quotient.eq U).mp
        have he' := congrArg (fun z : (W ⊓ Uᗮ : Submodule ℂ H) => U.mkQ z.val) he
        change U.mkQ (x.val - U.starProjection x.val) =
          U.mkQ (y.val - U.starProjection y.val) at he'
        have hx0 : U.mkQ (U.starProjection x.val) = 0 :=
          (Submodule.Quotient.mk_eq_zero U).mpr (U.starProjection_apply_mem x.val)
        have hy0 : U.mkQ (U.starProjection y.val) = 0 :=
          (Submodule.Quotient.mk_eq_zero U).mpr (U.starProjection_apply_mem y.val)
        rw [map_sub, map_sub, hx0, hy0, sub_zero, sub_zero] at he'
        exact he'
  · intro z
    refine ⟨Submodule.Quotient.mk (⟨z.val, z.property.1⟩ : W), ?_⟩
    apply Subtype.ext
    change z.val - U.starProjection z.val = z.val
    have hz : U.starProjection z.val = 0 := by
      have hz' := U.orthogonalProjectionOnto_apply_of_mem_orthogonal z.property.2
      exact congrArg (fun x : U => (x : H)) hz'
    rw [hz, sub_zero]

/-- The complete relation-layer equivalence, not just an equality of dimensions. -/
def orthogonalLayerEquiv :
    (W ⧸ U.comap W.subtype) ≃ₗ[ℂ] (W ⊓ Uᗮ : Submodule ℂ H) :=
  LinearEquiv.ofBijective (layerMap U W h) (layerMap_bijective U W h)

@[simp] theorem orthogonalLayerEquiv_apply (z : W) :
    (orthogonalLayerEquiv U W h (Submodule.Quotient.mk z)).val =
      z.val - U.starProjection z.val := rfl

end Orthogonal
end SplitZero.RelationLayer
