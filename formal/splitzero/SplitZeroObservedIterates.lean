import SplitZeroInternalQuotient
import Mathlib.LinearAlgebra.Quotient.Basic

/-!
# OPG23--24: observing iterates without assuming an invariant raw kernel

`invisible` is the largest A-invariant submodule inside ker(obs). The finite
comparison uses an explicit original polynomial recurrence, not a spectral
normality assumption. The case q=0 is also typed: its recurrence forces id=0.
-/
noncomputable section
namespace SplitZero.ObservedIterates
open scoped BigOperators

variable {R V W : Type*} [CommRing R]
  [AddCommGroup V] [Module R V] [AddCommGroup W] [Module R W]

/-- All source vectors invisible under every iterate of the SAME action. -/
def invisible (obs : V →ₗ[R] W) (A : Module.End R V) : Submodule R V :=
  ⨅ n : ℕ, LinearMap.ker (obs.comp (A ^ n))

/-- The finite window retains the complete tuple of observed vectors. -/
def window (obs : V →ₗ[R] W) (A : Module.End R V) (q : ℕ) : Submodule R V :=
  ⨅ j : Fin q, LinearMap.ker (obs.comp (A ^ j.val))

def observe (obs : V →ₗ[R] W) (A : Module.End R V) (q : ℕ) :
    V →ₗ[R] (Fin q → W) :=
  LinearMap.pi fun j => obs.comp (A ^ j.val)

@[simp] theorem mem_invisible (obs : V →ₗ[R] W) (A : Module.End R V) (x : V) :
    x ∈ invisible obs A ↔ ∀ n : ℕ, obs ((A ^ n) x) = 0 := by
  simp only [invisible, Submodule.mem_iInf, LinearMap.mem_ker, LinearMap.comp_apply]

@[simp] theorem mem_window (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (x : V) :
    x ∈ window obs A q ↔ ∀ j : Fin q, obs ((A ^ j.val) x) = 0 := by
  simp only [window, Submodule.mem_iInf, LinearMap.mem_ker, LinearMap.comp_apply]

@[simp] theorem observe_apply (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (x : V) (j : Fin q) :
    observe obs A q x j = obs ((A ^ j.val) x) := rfl

theorem ker_observe (obs : V →ₗ[R] W) (A : Module.End R V) (q : ℕ) :
    LinearMap.ker (observe obs A q) = window obs A q := by
  ext x
  simp only [LinearMap.mem_ker, mem_window, funext_iff, observe_apply, Pi.zero_apply]

theorem invisible_le_kernel (obs : V →ₗ[R] W) (A : Module.End R V) :
    invisible obs A ≤ LinearMap.ker obs := by
  intro x hx
  simpa using (mem_invisible obs A x).mp hx 0

theorem invariant (obs : V →ₗ[R] W) (A : Module.End R V)
    {x : V} (hx : x ∈ invisible obs A) : A x ∈ invisible obs A := by
  apply (mem_invisible obs A (A x)).mpr
  intro n
  simpa only [pow_succ, Module.End.mul_apply] using
    (mem_invisible obs A x).mp hx (n + 1)

/-- A raw observation kernel need not be stable; this constructs its largest stable part. -/
theorem largest_invariant (obs : V →ₗ[R] W) (A : Module.End R V)
    (P : Submodule R V) (hP : P ≤ LinearMap.ker obs)
    (hA : ∀ x ∈ P, A x ∈ P) : P ≤ invisible obs A := by
  intro x hx
  apply (mem_invisible obs A x).mpr
  intro n
  apply hP
  induction n with
  | zero => simpa using hx
  | succ n ih =>
      simpa only [pow_succ', Module.End.mul_apply] using hA ((A ^ n) x) ih

/-- The literal action polynomial closes all higher observation equations. -/
theorem all_iterates_of_window (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (c : Fin q → R)
    (hpoly : A ^ q = ∑ j : Fin q, c j • A ^ j.val)
    (x : V) (hx : x ∈ window obs A q) :
    ∀ n : ℕ, obs ((A ^ n) x) = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
      by_cases hn : n < q
      · exact (mem_window obs A q x).mp hx ⟨n, hn⟩
      · have hqn : q ≤ n := Nat.le_of_not_gt hn
        have he : n = q + (n - q) := by omega
        have hr : obs ((A ^ n) x) =
            ∑ j : Fin q, c j • obs ((A ^ (j.val + (n - q))) x) := by
          conv_lhs => rw [he, pow_add, hpoly, Finset.sum_mul]
          simp only [smul_mul_assoc, ← pow_add, LinearMap.sum_apply,
            LinearMap.smul_apply, map_sum, map_smul]
        rw [hr]
        apply Finset.sum_eq_zero
        intro j _
        rw [ih (j.val + (n - q)) (by have := j.isLt; omega), smul_zero]

theorem finite_determination (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (c : Fin q → R)
    (hpoly : A ^ q = ∑ j : Fin q, c j • A ^ j.val) :
    window obs A q = invisible obs A := by
  ext x
  constructor
  · intro hx
    exact (mem_invisible obs A x).mpr (all_iterates_of_window obs A q c hpoly x hx)
  · intro hx
    exact (mem_window obs A q x).mpr fun j => (mem_invisible obs A x).mp hx j.val

/-- The action on the genuine quotient is induced by the proved stability. -/
def quotientAction (obs : V →ₗ[R] W) (A : Module.End R V) :
    Module.End R (V ⧸ invisible obs A) :=
  (invisible obs A).mapQ (invisible obs A) A (fun _ hx => invariant obs A hx)

@[simp] theorem quotient_action_mk (obs : V →ₗ[R] W) (A : Module.End R V) (x : V) :
    quotientAction obs A ((invisible obs A).mkQ x) =
      (invisible obs A).mkQ (A x) := rfl

/-- Intertwining of arbitrary powers, with no injectivity hypothesis on transport. -/
theorem powers_intertwine {V' : Type*} [AddCommGroup V'] [Module R V']
    (T : V →ₗ[R] V') (A : Module.End R V) (A' : Module.End R V')
    (h : ∀ x, T (A x) = A' (T x)) (n : ℕ) (x : V) :
    T ((A ^ n) x) = (A' ^ n) (T x) := by
  induction n with
  | zero => rfl
  | succ n ih =>
      simp only [pow_succ', Module.End.mul_apply, h, ih]

/-- Exact faithful-observation criterion, permitting a noninjective one-step map. -/
theorem window_injective_iff (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (c : Fin q → R)
    (hpoly : A ^ q = ∑ j : Fin q, c j • A ^ j.val) :
    Function.Injective (observe obs A q) ↔ invisible obs A = ⊥ := by
  rw [← LinearMap.ker_eq_bot, ker_observe, finite_determination obs A q c hpoly]

end SplitZero.ObservedIterates
