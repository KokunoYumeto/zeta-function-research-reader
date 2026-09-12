import SplitZeroMaps
import Mathlib.RingTheory.TensorProduct.Quotient

/-!
# Operator-balanced finite jets

The quotient-tensor equivalence is an explicit application of Mathlib's
`quotIdealMapEquivTensorQuot`, not claimed as new general tensor algebra.
Here it is specialized to every jet order and connected to the exact
operator-balancing relation in the source's Mellin repair.
-/

noncomputable section
namespace SplitZero.FiniteJets
open TensorProduct

variable {k B : Type*} [CommRing k] [CommRing B] [Algebra (Polynomial k) B]

def jetIdeal (rho : k) (m : ℕ) : Ideal (Polynomial k) :=
  Ideal.span {((Polynomial.X - Polynomial.C rho) ^ m)}

/-- The exact target ideal, retaining the chosen coefficient-algebra map. -/
theorem mapped_jet_ideal (rho : k) (m : ℕ) :
    (jetIdeal rho m).map (algebraMap (Polynomial k) B) =
      Ideal.span {((algebraMap (Polynomial k) B Polynomial.X -
        algebraMap (Polynomial k) B (Polynomial.C rho)) ^ m)} := by
  simp [jetIdeal, Ideal.map_span]

/-- Full finite-jet base change, for all orders, without a flatness hypothesis. -/
def baseChange (rho : k) (m : ℕ) :
    B ⊗[Polynomial k] (Polynomial k ⧸ jetIdeal rho m) ≃ₐ[B]
      B ⧸ (jetIdeal rho m).map (algebraMap (Polynomial k) B) :=
  (Algebra.TensorProduct.quotIdealMapEquivTensorQuot B (jetIdeal rho m)).symm

@[simp] theorem baseChange_tmul (rho : k) (m : ℕ) (b : B) (p : Polynomial k) :
    baseChange rho m (b ⊗ₜ[Polynomial k] (Ideal.Quotient.mk (jetIdeal rho m) p)) =
      Ideal.Quotient.mk _ (algebraMap (Polynomial k) B p * b) := rfl

@[simp] theorem baseChange_inverse (rho : k) (m : ℕ) (b : B) :
    (baseChange rho m).symm (Ideal.Quotient.mk _ b) = b ⊗ₜ[Polynomial k] 1 := rfl

/-- The specific raw Mellin relation is zero in the operator-balanced tensor product. -/
theorem balanced_mellin_relation {V : Type*} [AddCommGroup V] [Module (Polynomial k) V]
    (v : V) :
    (1 - algebraMap (Polynomial k) B Polynomial.X) ⊗ₜ[Polynomial k]
        ((Polynomial.X : Polynomial k) • v) -
      (algebraMap (Polynomial k) B Polynomial.X) ⊗ₜ[Polynomial k]
        (v - (Polynomial.X : Polynomial k) • v) = 0 := by
  have h : (1 : B) ⊗ₜ[Polynomial k] ((Polynomial.X : Polynomial k) • v) =
      (algebraMap (Polynomial k) B Polynomial.X) ⊗ₜ[Polynomial k] v := by
    rw [TensorProduct.tmul_smul, TensorProduct.smul_tmul']
    simp [Algebra.smul_def]
  rw [TensorProduct.sub_tmul, TensorProduct.tmul_sub]
  rw [h]
  abel

end SplitZero.FiniteJets
