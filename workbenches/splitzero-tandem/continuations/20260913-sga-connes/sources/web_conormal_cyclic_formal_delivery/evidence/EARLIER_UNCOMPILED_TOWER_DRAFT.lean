import SplitZeroRelationLayerIntegration
import Mathlib.RingTheory.Derivation.Basic
import Mathlib.RingTheory.Ideal.Operations

/-!
Derivative maps between the original ideal-power quotients.

This draft reuses RelationLayer.derivative. It does not assume that
the ideal is derivative-stable or that the packet is squarefree.
-/

noncomputable section

namespace SplitZero.ConormalTower

variable {R A : Type*}
  [CommRing R] [CommRing A] [Algebra R A]

/-- The original ideal-power relation, viewed over the coefficient ring. -/
def level (I : Ideal A) (r : ℕ) : Submodule R A :=
  (I ^ r).restrictScalars R

/-- A derivation lowers ideal order by at most one. -/
theorem deriv_mem_pow
    (D : Derivation R A A) (I : Ideal A) (r : ℕ)
    {x : A} (hx : x ∈ I ^ (r + 1)) :
    D x ∈ I ^ r := by
  induction r generalizing x with
  | zero =>
      rw [Submodule.pow_zero, Ideal.one_eq_top]
      exact Submodule.mem_top
  | succ r ih =>
      rw [Submodule.pow_succ] at hx
      refine Submodule.mul_induction_on hx ?_ ?_
      · intro a ha b hb
        rw [D.leibniz]
        change a * D b + b * D a ∈ I ^ (r + 1)
        have hd : D a * b ∈ I ^ (r + 1) := by
          rw [Submodule.pow_succ]
          exact Ideal.mul_mem_mul (ih ha) hb
        exact (I ^ (r + 1)).add_mem
          ((I ^ (r + 1)).mul_mem_right (D b) ha)
          (by simpa only [mul_comm] using hd)
      · intro a b ha hb
        rw [map_add]
        exact (I ^ (r + 1)).add_mem ha hb

/-- The derivative on A/I^(r+1), with values in A/I^r. -/
def descended
    (D : Derivation R A A) (I : Ideal A) (r : ℕ) :
    (A ⧸ level (R := R) I (r + 1)) →ₗ[R]
      (A ⧸ level (R := R) I r) :=
  SplitZero.RelationLayer.derivative
    (level I (r + 1)) (level I r) D.toLinearMap
    (fun _ hx => deriv_mem_pow D I r hx)

@[simp]
theorem descended_mk
    (D : Derivation R A A) (I : Ideal A) (r : ℕ) (x : A) :
    descended D I r ((level I (r + 1)).mkQ x) =
      (level I r).mkQ (D x) :=
  rfl

/-- Forget one ideal-adic layer without differentiating. -/
def projection (I : Ideal A) (r : ℕ) :
    (A ⧸ level (R := R) I (r + 1)) →ₗ[R]
      (A ⧸ level (R := R) I r) :=
  SplitZero.RelationLayer.transport
    (level I (r + 1)) (level I r)
    (fun _ hx => Ideal.pow_le_pow_right (Nat.le_succ r) hx)

@[simp]
theorem projection_mk (I : Ideal A) (r : ℕ) (x : A) :
    projection (R := R) I r ((level I (r + 1)).mkQ x) =
      (level I r).mkQ x :=
  rfl

/-- Derivative and quotient transition form the actual commuting square. -/
theorem tower_square
    (D : Derivation R A A) (I : Ideal A) (r : ℕ) :
    (projection I r).comp (descended D I (r + 1)) =
      (descended D I r).comp (projection I (r + 1)) := by
  apply LinearMap.ext
  intro z
  obtain ⟨x, rfl⟩ :=
    Submodule.Quotient.mk_surjective (level I (r + 2)) z
  rfl

/-- On a retained relation z*a, only a*D(z) survives modulo I. -/
theorem conormal_product
    (D : Derivation R A A) (I : Ideal A)
    (z a : A) (hz : z ∈ I) :
    descended D I 1 ((level I 2).mkQ (z * a)) =
      (level I 1).mkQ (a * D z) := by
  rw [descended_mk, D.leibniz]
  change
    (level I 1).mkQ (z * D a + a * D z) =
      (level I 1).mkQ (a * D z)
  rw [map_add]
  have hzero : (level (R := R) I 1).mkQ (z * D a) = 0 := by
    apply (Submodule.Quotient.mk_eq_zero _).mpr
    change z * D a ∈ I ^ 1
    rw [Submodule.pow_one]
    exact I.mul_mem_right (D a) hz
  rw [hzero, zero_add]

end SplitZero.ConormalTower
