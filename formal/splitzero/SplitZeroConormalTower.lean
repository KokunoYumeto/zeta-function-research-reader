import SplitZeroRelationLayerIntegration
import Mathlib.RingTheory.Derivation.Basic
import Mathlib.RingTheory.Ideal.Operations
import Mathlib.Tactic

/-!
# Derivatives on the original relation tower and its cyclic subquotients

The ambient quotient machinery is the merged Codex RelationLayer interface.
No derivative-stability of I and no squarefree hypothesis is assumed.
The cyclic level is the actual pullback of I^r along polynomial evaluation;
it is deliberately not the r-th power of the first cyclic relation ideal.
-/
noncomputable section
namespace SplitZero.ConormalTower

variable {R A : Type*} [CommRing R] [CommRing A] [Algebra R A]

/-- The original I-adic relation, as a coefficient submodule. -/
def level (I : Ideal A) (r : ℕ) : Submodule R A :=
  (I ^ r).restrictScalars R

/-- Product differentiation lowers ideal order by at most one. -/
theorem deriv_mem_pow (D : Derivation R A A) (I : Ideal A) (r : ℕ)
    {x : A} (hx : x ∈ I ^ (r + 1)) : D x ∈ I ^ r := by
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

/-- The derivative has different consecutive quotient types. -/
def descended (D : Derivation R A A) (I : Ideal A) (r : ℕ) :
    (A ⧸ level (R := R) I (r + 1)) →ₗ[R] (A ⧸ level (R := R) I r) :=
  SplitZero.RelationLayer.derivative (level I (r + 1)) (level I r)
    D.toLinearMap (fun _ hx => deriv_mem_pow D I r hx)

@[simp] theorem descended_mk (D : Derivation R A A) (I : Ideal A)
    (r : ℕ) (x : A) :
    descended D I r ((level I (r + 1)).mkQ x) = (level I r).mkQ (D x) := rfl

/-- Forget one retained layer without differentiating. -/
def projection (I : Ideal A) (r : ℕ) :
    (A ⧸ level (R := R) I (r + 1)) →ₗ[R] (A ⧸ level (R := R) I r) :=
  SplitZero.RelationLayer.transport (level I (r + 1)) (level I r)
    (fun _ hx => Ideal.pow_le_pow_right (Nat.le_succ r) hx)

@[simp] theorem projection_mk (I : Ideal A) (r : ℕ) (x : A) :
    projection (R := R) I r ((level I (r + 1)).mkQ x) = (level I r).mkQ x := rfl

theorem tower_square (D : Derivation R A A) (I : Ideal A) (r : ℕ) :
    (projection I r).comp (descended D I (r + 1)) =
      (descended D I r).comp (projection I (r + 1)) := by
  apply LinearMap.ext
  intro z
  obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective (level I (r + 2)) z
  rfl

/-- An original relation retains its derivative modulo the old ideal. -/
theorem conormal_product (D : Derivation R A A) (I : Ideal A)
    (z a : A) (hz : z ∈ I) :
    descended D I 1 ((level I 2).mkQ (z * a)) =
      (level I 1).mkQ (a * D z) := by
  rw [descended_mk, D.leibniz]
  change (level I 1).mkQ (z * D a + a * D z) = _
  rw [map_add]
  have hzero : (level (R := R) I 1).mkQ (z * D a) = 0 := by
    apply (Submodule.Quotient.mk_eq_zero _).mpr
    change z * D a ∈ I ^ 1
    rw [Submodule.pow_one]
    exact I.mul_mem_right (D a) hz
  rw [hzero, zero_add]

/-- The arithmetic Taylor multiplier contributes both Leibniz terms. -/
theorem multiplier_rule (D : Derivation R A A) (I : Ideal A)
    (r : ℕ) (u x : A) :
    descended D I r ((level I (r + 1)).mkQ (u * x)) =
      (level I r).mkQ (u * D x) + (level I r).mkQ (x * D u) := by
  rw [descended_mk, D.leibniz]
  exact (level I r).mkQ.map_add _ _

/-- The empty packet h=1 has the full relation ideal at every level. -/
theorem top_level_zero (r : ℕ) (x : A) :
    (level (R := R) (⊤ : Ideal A) r).mkQ x = 0 := by
  apply (Submodule.Quotient.mk_eq_zero _).mpr
  change x ∈ (⊤ : Ideal A) ^ r
  have h : (⊤ : Ideal A) ^ r = ⊤ := by
    simpa using (Ideal.span_singleton_pow (1 : A) r)
  rw [h]
  exact Submodule.mem_top

/-- Literal pullback of the r-th multivariable relation along S. -/
def cyclicLevel (S : A) (I : Ideal A) (r : ℕ) : Submodule R R[X] :=
  (level I r).comap (Polynomial.aeval S).toLinearMap

/-- Evaluation embeds the cyclic quotient in the original quotient. -/
def evaluation (S : A) (I : Ideal A) (r : ℕ) :
    (R[X] ⧸ cyclicLevel S I r) →ₗ[R] (A ⧸ level I r) :=
  (cyclicLevel S I r).mapQ (level I r) (Polynomial.aeval S).toLinearMap le_rfl

@[simp] theorem evaluation_mk (S : A) (I : Ideal A) (r : ℕ) (p : R[X]) :
    evaluation S I r ((cyclicLevel S I r).mkQ p) =
      (level I r).mkQ (Polynomial.aeval S p) := rfl

theorem evaluation_injective (S : A) (I : Ideal A) (r : ℕ) :
    Function.Injective (evaluation (R := R) S I r) := by
  intro x y hxy
  obtain ⟨p, rfl⟩ := Submodule.Quotient.mk_surjective (cyclicLevel S I r) x
  obtain ⟨q, rfl⟩ := Submodule.Quotient.mk_surjective (cyclicLevel S I r) y
  apply (Submodule.Quotient.eq (cyclicLevel S I r)).mpr
  change Polynomial.aeval S (p - q) ∈ I ^ r
  change (level I r).mkQ (Polynomial.aeval S p) =
    (level I r).mkQ (Polynomial.aeval S q) at hxy
  have hm := (Submodule.Quotient.eq (level (R := R) I r)).mp hxy
  simpa only [map_sub] using hm

theorem polynomial_chain_rule (D : Derivation R A A) (S : A)
    (hS : D S = 1) (p : R[X]) :
    D (Polynomial.aeval S p) = Polynomial.aeval S (Polynomial.derivative p) := by
  rw [D.map_aeval, hS]
  exact mul_one _

/-- Formal differentiation on the exact cyclic relation tower. -/
def cyclicDerivative (D : Derivation R A A) (S : A) (hS : D S = 1)
    (I : Ideal A) (r : ℕ) :
    (R[X] ⧸ cyclicLevel S I (r + 1)) →ₗ[R] (R[X] ⧸ cyclicLevel S I r) :=
  SplitZero.RelationLayer.derivative (cyclicLevel S I (r + 1))
    (cyclicLevel S I r) Polynomial.derivative (by
      intro p hp
      change Polynomial.aeval S (Polynomial.derivative p) ∈ I ^ r
      rw [← polynomial_chain_rule D S hS]
      exact deriv_mem_pow D I r hp)

@[simp] theorem cyclicDerivative_mk (D : Derivation R A A) (S : A)
    (hS : D S = 1) (I : Ideal A) (r : ℕ) (p : R[X]) :
    cyclicDerivative D S hS I r ((cyclicLevel S I (r + 1)).mkQ p) =
      (cyclicLevel S I r).mkQ (Polynomial.derivative p) := rfl

/-- The sum-generated derivative is the restriction of the original derivative. -/
theorem cyclic_square (D : Derivation R A A) (S : A) (hS : D S = 1)
    (I : Ideal A) (r : ℕ) :
    (descended D I r).comp (evaluation S I (r + 1)) =
      (evaluation S I r).comp (cyclicDerivative D S hS I r) := by
  apply LinearMap.ext
  intro x
  obtain ⟨p, rfl⟩ := Submodule.Quotient.mk_surjective (cyclicLevel S I (r + 1)) x
  change (level I r).mkQ (D (Polynomial.aeval S p)) =
    (level I r).mkQ (Polynomial.aeval S (Polynomial.derivative p))
  rw [polynomial_chain_rule D S hS]

/-- The extra unit-derivative term is retained before the arithmetic quotient. -/
theorem cyclic_unit_rule (D : Derivation R A A) (S : A) (hS : D S = 1)
    (I : Ideal A) (r : ℕ) (u : A) (p : R[X]) :
    descended D I r ((level I (r + 1)).mkQ (u * Polynomial.aeval S p)) =
      (level I r).mkQ (u * Polynomial.aeval S (Polynomial.derivative p)) +
      (level I r).mkQ (Polynomial.aeval S p * D u) := by
  rw [multiplier_rule, polynomial_chain_rule D S hS]

end SplitZero.ConormalTower
