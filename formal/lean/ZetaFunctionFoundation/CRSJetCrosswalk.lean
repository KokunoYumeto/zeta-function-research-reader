import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Conrey--Rubinstein--Snaith first-jet crosswalk

This file certifies the finite algebraic part of the coordinate conversion
between the characteristic-polynomial convention of Conrey--Rubinstein--Snaith
and the retained value/derivative coordinates.  It also certifies the exact
factorization of the centered derivative through the Cauchy trace off the
value-zero locus.  It does not formalize the cited large-N asymptotics or the
separate number-theoretic conjecture.
-/

namespace ZetaFunctionFoundation.CRSJetCrosswalk

noncomputable section

/-- The first jet (value, derivative) of the CRS completed polynomial,
with the phase and the N/2 term retained. -/
def completedJet (rho : ℂ) (N : ℕ) (V d : ℂ) : ℂ × ℂ :=
  (rho * V, rho * (d - (N : ℂ) / 2 * V))

/-- The explicit inverse triangular jet map. -/
def completedJetInv (rho : ℂ) (N : ℕ) (z0 z1 : ℂ) : ℂ × ℂ :=
  (rho⁻¹ * z0, rho⁻¹ * (z1 + (N : ℂ) / 2 * z0))

/-- Applying the inverse after the completed-jet map recovers both source
coordinates.  Hence every fibre is a singleton when the phase is nonzero. -/
theorem completedJetInv_completedJet
    (rho : ℂ) (N : ℕ) (V d : ℂ) (hRho : rho ≠ 0) :
    completedJetInv rho N (completedJet rho N V d).1
        (completedJet rho N V d).2 = (V, d) := by
  simp only [completedJet, completedJetInv]
  apply Prod.ext
  · field_simp [hRho]
  · field_simp [hRho]
    ring

/-- Applying the completed-jet map after its displayed inverse recovers both
target coordinates. -/
theorem completedJet_completedJetInv
    (rho : ℂ) (N : ℕ) (z0 z1 : ℂ) (hRho : rho ≠ 0) :
    completedJet rho N (completedJetInv rho N z0 z1).1
        (completedJetInv rho N z0 z1).2 = (z0, z1) := by
  simp only [completedJet, completedJetInv]
  apply Prod.ext
  · field_simp [hRho]
  · field_simp [hRho]
    ring

/-- The polynomial coordinate that remains defined on the value-zero locus. -/
def centeredDerivative (N : ℕ) (V F : ℂ) : ℂ :=
  (N : ℂ) * (F - V / 2)

/-- The Winn--Forrester trace written in retained value/derivative
coordinates.  Its denominator records the exact exceptional locus. -/
def cauchyTrace (N : ℕ) (V F : ℂ) : ℂ :=
  -Complex.I * (2 * (N : ℂ) * F / V - (N : ℂ))

/-- Off V = 0, multiplying the trace by i V / 2 gives exactly the
centered derivative.  No phase or factor of N is discarded. -/
theorem cauchyTrace_factor
    (N : ℕ) (V F : ℂ) (hV : V ≠ 0) :
    (Complex.I / 2) * V * cauchyTrace N V F =
      centeredDerivative N V F := by
  unfold cauchyTrace centeredDerivative
  field_simp [hV]
  rw [Complex.I_sq]
  ring

/-- The centered derivative itself has a literal value at the exceptional
locus; only the quotient defining the trace is unavailable there. -/
@[simp] theorem centeredDerivative_value_zero (N : ℕ) (F : ℂ) :
    centeredDerivative N 0 F = (N : ℂ) * F := by
  simp [centeredDerivative]

end

end ZetaFunctionFoundation.CRSJetCrosswalk
