import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring

/-!
# Dehaye angular-jet crosswalk

This file certifies the finite algebraic part of the coordinate conversion
between Dehaye's angular value/derivative jet, the retained radial polynomial
jet, and the completed angular jet.  It also certifies the two exact affine
relations between the angular logarithmic derivatives and the Cauchy trace.

It does not formalize Haar integration, Schur-function identities, the
large-`N` limit, meromorphic continuation, or the separate number-theoretic
model transfers in the cited source.
-/

namespace ZetaFunctionFoundation.DehayeJetCrosswalk

noncomputable section

/-- The angular first jet obtained from the radial polynomial value `V` and
radial derivative `d`; the translation by `N` is retained. -/
def angularJet (N : ℕ) (V d : ℂ) : ℂ × ℂ :=
  (V, Complex.I * (d - (N : ℂ) * V))

/-- The explicit inverse of `angularJet`. -/
def angularJetInv (N : ℕ) (z0 z1 : ℂ) : ℂ × ℂ :=
  (z0, (N : ℂ) * z0 - Complex.I * z1)

/-- The angular jet has singleton fibres: inverse after forward recovers both
radial coordinates. -/
theorem angularJetInv_angularJet (N : ℕ) (V d : ℂ) :
    angularJetInv N (angularJet N V d).1 (angularJet N V d).2 = (V, d) := by
  simp only [angularJet, angularJetInv]
  apply Prod.ext
  · rfl
  · calc
      (N : ℂ) * V - Complex.I * (Complex.I * (d - (N : ℂ) * V)) =
          (N : ℂ) * V - (Complex.I * Complex.I) *
            (d - (N : ℂ) * V) := by ring
      _ = d := by rw [Complex.I_mul_I]; ring

/-- Forward after inverse recovers both angular coordinates. -/
theorem angularJet_angularJetInv (N : ℕ) (z0 z1 : ℂ) :
    angularJet N (angularJetInv N z0 z1).1
        (angularJetInv N z0 z1).2 = (z0, z1) := by
  simp only [angularJet, angularJetInv]
  apply Prod.ext
  · rfl
  · calc
      Complex.I * ((N : ℂ) * z0 - Complex.I * z1 - (N : ℂ) * z0) =
          -(Complex.I * Complex.I) * z1 := by ring
      _ = z1 := by rw [Complex.I_mul_I]; ring

/-- Pull-back of a completed radial jet along the angular coordinate. -/
def completedAngularJet (z0 z1 : ℂ) : ℂ × ℂ :=
  (z0, Complex.I * z1)

/-- Explicit inverse of the completed angular jet map. -/
def completedAngularJetInv (w0 w1 : ℂ) : ℂ × ℂ :=
  (w0, -Complex.I * w1)

/-- The completed angular jet map also has singleton fibres. -/
theorem completedAngularJetInv_completedAngularJet (z0 z1 : ℂ) :
    completedAngularJetInv (completedAngularJet z0 z1).1
        (completedAngularJet z0 z1).2 = (z0, z1) := by
  simp only [completedAngularJet, completedAngularJetInv]
  apply Prod.ext
  · rfl
  · calc
      -Complex.I * (Complex.I * z1) =
          -(Complex.I * Complex.I) * z1 := by ring
      _ = z1 := by rw [Complex.I_mul_I]; ring

/-- Forward after inverse for the completed angular jet. -/
theorem completedAngularJet_completedAngularJetInv (w0 w1 : ℂ) :
    completedAngularJet (completedAngularJetInv w0 w1).1
        (completedAngularJetInv w0 w1).2 = (w0, w1) := by
  simp only [completedAngularJet, completedAngularJetInv]
  apply Prod.ext
  · rfl
  · calc
      Complex.I * (-Complex.I * w1) =
          -(Complex.I * Complex.I) * w1 := by ring
      _ = w1 := by rw [Complex.I_mul_I]; ring

/-- The retained Cauchy trace expressed through the radial logarithmic
derivative coordinate `u`. -/
def cauchyTrace (N : ℕ) (u : ℂ) : ℂ :=
  -Complex.I * (2 * u - (N : ℂ))

/-- Exact uncompleted angular logarithmic derivative relation. -/
theorem uncompletedLogDerivative_trace (N : ℕ) (u : ℂ) :
    Complex.I * (u - (N : ℂ)) =
      -(cauchyTrace N u + Complex.I * (N : ℂ)) / 2 := by
  unfold cauchyTrace
  ring

/-- Exact completed angular logarithmic derivative relation. -/
theorem completedLogDerivative_trace (N : ℕ) (u : ℂ) :
    Complex.I * (u - (N : ℂ) / 2) = -cauchyTrace N u / 2 := by
  unfold cauchyTrace
  ring

end

end ZetaFunctionFoundation.DehayeJetCrosswalk
