import Mathlib

/-!
The smallest invariant enlargement is constructed, not selected by a new
metric. This module is independent of finite dimension; the cyclic gcd
and finite Cayley-Hamilton descriptions are proved in the accompanying note.
-/
noncomputable section
namespace SplitZero.ActionHull
variable {K E : Type*} [Field K] [AddCommGroup E] [Module K E]

def hull (A : Module.End K E) (U : Submodule K E) : Submodule K E :=
  Submodule.span K {y | ∃ n : ℕ, ∃ x : E, x ∈ U ∧ y = (A^n) x}

theorem orbit_mem (A : Module.End K E) (U : Submodule K E)
    (n : ℕ) (x : E) (hx : x ∈ U) : (A^n) x ∈ hull A U :=
  Submodule.subset_span ⟨n,x,hx,rfl⟩

theorem contains (A : Module.End K E) (U : Submodule K E) : U ≤ hull A U := by
  intro x hx
  simpa only [pow_zero, Module.End.one_apply] using orbit_mem A U 0 x hx

theorem stable (A : Module.End K E) (U : Submodule K E)
    (x : E) (hx : x ∈ hull A U) : A x ∈ hull A U := by
  induction hx using Submodule.span_induction with
  | mem y hy =>
      obtain ⟨n,z,hz,rfl⟩ := hy
      have hh := orbit_mem A U (n+1) z hz
      simpa only [pow_succ', Module.End.mul_apply] using hh
  | zero => simpa only [map_zero] using (hull A U).zero_mem
  | add x y _hx _hy hx hy =>
      simpa only [map_add] using (hull A U).add_mem hx hy
  | smul a x _hx hx =>
      simpa only [map_smul] using (hull A U).smul_mem a hx

/-- Every invariant subspace containing U contains this actual span. -/
theorem least (A : Module.End K E) (U W : Submodule K E)
    (hUW : U ≤ W) (hW : ∀ x ∈ W, A x ∈ W) : hull A U ≤ W := by
  apply Submodule.span_le.mpr
  rintro y ⟨n,x,hx,rfl⟩
  induction n with
  | zero => simpa only [pow_zero, Module.End.one_apply] using hUW hx
  | succ n ih =>
      simpa only [pow_succ', Module.End.mul_apply] using hW ((A^n) x) ih

theorem monotone (A : Module.End K E) {U W : Submodule K E} (h : U ≤ W) :
    hull A U ≤ hull A W :=
  least A U (hull A W) (le_trans h (contains A W)) (stable A W)

theorem idempotent (A : Module.End K E) (U : Submodule K E) :
    hull A (hull A U) = hull A U := by
  apply le_antisymm
  · exact least A (hull A U) (hull A U) le_rfl (stable A U)
  · exact contains A (hull A U)

theorem eq_self_iff (A : Module.End K E) (U : Submodule K E) :
    hull A U = U ↔ ∀ x ∈ U, A x ∈ U := by
  constructor
  · intro h x hx
    have hh := stable A U x ((contains A U) hx)
    simpa only [h] using hh
  · intro h
    exact le_antisymm (least A U U le_rfl h) (contains A U)

/-- The action on a retained initial vector never leaves the constructed hull. -/
theorem all_iterates (A : Module.End K E) (U : Submodule K E)
    (n : ℕ) (x : E) (hx : x ∈ hull A U) : (A^n) x ∈ hull A U := by
  induction n with
  | zero => simpa only [pow_zero, Module.End.one_apply] using hx
  | succ n ih => simpa only [pow_succ', Module.End.mul_apply] using stable A U ((A^n) x) ih
end SplitZero.ActionHull
