import Mathlib

/-!
Finite consequences of the Connes--Consani Laplacian comparison.
The analytic trace, Schwartz quotient, and periodization comparison are proved
in the accompanying written note, not postulated as Lean axioms here.
The statements below keep the original Gram matrix, action, and nilpotent jets.
-/
noncomputable section
namespace SplitZero.LaplacianControl
open Matrix

section Matrices
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

def weightDefect (k : ℂ) (A G : Matrix ι ι ℂ) : Matrix ι ι ℂ :=
  A.conjTranspose * G + G * A - k • G

def laplacian (k : ℂ) (A : Matrix ι ι ℂ) : Matrix ι ι ℂ := A*A-k • A

/-- The defect of Laplacian symmetry is determined by the original weight defect. -/
theorem adjoint_defect (k : ℂ) (hk : star k = k) (A G : Matrix ι ι ℂ) :
    (laplacian k A).conjTranspose * G - G * laplacian k A =
      A.conjTranspose * weightDefect k A G - weightDefect k A G * A := by
  simp only [laplacian, weightDefect, Matrix.conjTranspose_sub,
    Matrix.conjTranspose_mul, Matrix.conjTranspose_smul, hk,
    Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_add, Matrix.add_mul,
    Matrix.smul_mul, Matrix.mul_smul, Matrix.mul_assoc]
  abel

/-- The source energy formula retains the entire error contraction W*A. -/
theorem energy_identity (k : ℂ) (A G : Matrix ι ι ℂ) :
    G * laplacian k A = weightDefect k A G * A - A.conjTranspose * G * A := by
  simp only [laplacian, weightDefect, Matrix.mul_sub, Matrix.sub_mul,
    Matrix.add_mul, Matrix.smul_mul, Matrix.mul_smul, Matrix.mul_assoc]
  abel

/-- This is a conditional symmetry implication, not a purity assumption. -/
theorem symmetric_of_zero_defect (k : ℂ) (hk : star k = k)
    (A G : Matrix ι ι ℂ) (hW : weightDefect k A G = 0) :
    (laplacian k A).conjTranspose * G = G * laplacian k A := by
  apply sub_eq_zero.mp
  rw [adjoint_defect k hk A G, hW, Matrix.mul_zero, Matrix.zero_mul, sub_self]

/-- An actual constituent inclusion intertwines the polynomial Laplacian. -/
theorem constituent {κ : Type*} [Fintype κ]
    (k : ℂ) (A : Matrix ι ι ℂ) (B : Matrix κ κ ℂ) (J : Matrix ι κ ℂ)
    (h : A*J=J*B) : laplacian k A * J = J * laplacian k B := by
  unfold laplacian
  rw [Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul]
  rw [Matrix.mul_assoc A A J, h, ← Matrix.mul_assoc A J B, h, Matrix.mul_assoc]

/-- The complete quadratic jet, not just its diagonal eigenvalue. -/
theorem jet_expansion (k rho : ℂ) (N : Matrix ι ι ℂ) :
    laplacian k (rho • (1 : Matrix ι ι ℂ) + N) =
      (rho*rho-k*rho) • (1 : Matrix ι ι ℂ) + (2*rho-k) • N + N*N := by
  simp only [laplacian, Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul,
    Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one, smul_smul, smul_add]
  module
end Matrices

section Comparison
variable {K E F : Type*} [Field K] [AddCommGroup E] [Module K E]
  [AddCommGroup F] [Module K F]

/-- Intertwining propagates through every power, including the zeroth. -/
theorem intertwining_power (f : E →ₗ[K] F) (A : Module.End K E)
    (B : Module.End K F) (h : ∀ x, f (A x) = B (f x)) (m : ℕ) (x : E) :
    f ((A^m) x) = (B^m) (f x) := by
  induction m with
  | zero => simp only [pow_zero, Module.End.one_apply]
  | succ m ih => simp only [pow_succ', Module.End.mul_apply, h, ih]

theorem injective_power (B : Module.End K F) (hB : Function.Injective B) (m : ℕ) :
    Function.Injective (B^m) := by
  induction m with
  | zero => simpa only [pow_zero, Module.End.one_apply] using (Function.injective_id : Function.Injective (id : F → F))
  | succ m ih =>
      simpa only [pow_succ', Module.End.mul_apply, Function.comp_def] using hB.comp ih

/-- An injective target operator kills no vector, so an intertwined nilpotent vector maps to zero. -/
theorem nilpotent_image_zero (f : E →ₗ[K] F) (A : Module.End K E)
    (B : Module.End K F) (h : ∀ x, f (A x) = B (f x))
    (hB : Function.Injective B) (m : ℕ) (x : E) (hx : (A^m) x=0) : f x=0 := by
  apply injective_power B hB m
  rw [← intertwining_power f A B h m x, hx, map_zero, map_zero]

/-- The full generalized eigenspace is retained until this specified comparison kills it. -/
theorem shifted_nilpotent_image_zero (f : E →ₗ[K] F)
    (A : Module.End K E) (B : Module.End K F) (rho : K)
    (h : ∀ x, f (A x) = B (f x))
    (hB : Function.Injective (B-rho • 1))
    (m : ℕ) (x : E) (hx : ((A-rho • 1)^m) x=0) : f x=0 := by
  apply nilpotent_image_zero f (A-rho • 1) (B-rho • 1) _ hB m x hx
  intro y
  simp only [LinearMap.sub_apply, LinearMap.smul_apply, Module.End.one_apply,
    map_sub, map_smul, h]
end Comparison
end SplitZero.LaplacianControl
