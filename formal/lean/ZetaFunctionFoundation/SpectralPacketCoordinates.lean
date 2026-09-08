import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# Spectral packet coordinate identities

This file certifies the finite affine and commutative-algebra identities used
in Chapter 18.  It does not formalize the analytic continuation of zeta, the
Connes--Consani quotient spaces, their spectral theorem, or the existence and
location of any individual zero.
-/

namespace ZetaFunctionFoundation.SpectralPacketCoordinates

/-- The inverse of the retained affine spectral coordinate
`z = I * (s - 1/2)` is literally `s = 1/2 - I*z`. -/
theorem affineInverse (s : ℂ) :
    (1 / 2 : ℂ) - Complex.I * (Complex.I * (s - 1 / 2)) = s := by
  calc
    (1 / 2 : ℂ) - Complex.I * (Complex.I * (s - 1 / 2)) =
        1 / 2 - (Complex.I * Complex.I) * (s - 1 / 2) := by ring
    _ = s := by rw [Complex.I_mul_I]; ring

/-- The functional involution `s ↦ 1-s` becomes sign in the spectral
coordinate. -/
theorem functionalInvolutionBecomesSign (s : ℂ) :
    Complex.I * ((1 - s) - 1 / 2) =
      -(Complex.I * (s - 1 / 2)) := by
  ring

/-- The Connes--Consani Laplacian coordinate is the exact quadratic image of
the affine spectral coordinate. -/
theorem laplacianAffineIdentity (s : ℂ) :
    -(Complex.I * (s - 1 / 2)) ^ 2 - 1 / 4 =
      (s - 1 / 2) ^ 2 - 1 / 4 := by
  rw [mul_pow, Complex.I_sq]
  ring

/-- The centered and uncentered forms of the Laplacian value agree without a
rescaling. -/
theorem laplacianCenteredEqualsUncentered (s : ℂ) :
    (s - 1 / 2) ^ 2 - 1 / 4 = -s * (1 - s) := by
  ring

/-- Away from the branch point, equality of quadratic spectral values loses
exactly the sign of the spectral coordinate.  The statement includes the
branch point, where the two alternatives coincide. -/
theorem laplacianValueEqIffSign (z₁ z₂ : ℂ) :
    (-z₁ ^ 2 - 1 / 4 = -z₂ ^ 2 - 1 / 4) ↔
      z₂ = z₁ ∨ z₂ = -z₁ := by
  constructor
  · intro h
    have hfactor : (z₁ - z₂) * (z₁ + z₂) = 0 := by
      calc
        (z₁ - z₂) * (z₁ + z₂) = z₁ ^ 2 - z₂ ^ 2 := by ring
        _ = 0 := by linear_combination -h
    rcases mul_eq_zero.mp hfactor with hminus | hplus
    · left
      exact (sub_eq_zero.mp hminus).symm
    · right
      linear_combination hplus
  · intro h
    rcases h with rfl | rfl <;> ring

/-- Translating a centered square by `-1/4` gives the exact sum of the two
conjugate spectral roots before conjugation is imposed. -/
theorem spectralRootSum (A B : ℂ) :
    (A - 1 / 4) + (B - 1 / 4) = A + B - 1 / 2 := by
  ring

/-- Translating centered squares by `-1/4` gives the exact product of the two
spectral roots. -/
theorem spectralRootProduct (A B : ℂ) :
    (A - 1 / 4) * (B - 1 / 4) =
      A * B - (A + B) / 4 + 1 / 16 := by
  ring

/-- The quartic packet coefficients convert to the monic quadratic spectral
packet polynomial with every `1/4` term retained. -/
theorem quarticPacketToSpectralPolynomial
    (t A B c₂ c₄ : ℂ)
    (hc₄ : c₄ ≠ 0)
    (hprod : A * B = 1 / c₄)
    (hsum : A + B = -c₂ / c₄) :
    (t - (A - 1 / 4)) * (t - (B - 1 / 4)) =
      t ^ 2 + (c₂ / c₄ + 1 / 2) * t
        + (1 / c₄ + c₂ / (4 * c₄) + 1 / 16) := by
  calc
    (t - (A - 1 / 4)) * (t - (B - 1 / 4)) =
        t ^ 2 - (A + B - 1 / 2) * t
          + (A * B - (A + B) / 4 + 1 / 16) := by ring
    _ = t ^ 2 + (c₂ / c₄ + 1 / 2) * t
          + (1 / c₄ + c₂ / (4 * c₄) + 1 / 16) := by
      rw [hprod, hsum]
      field_simp [hc₄]
      ring

/-- In the critical two-point case the quadratic packet coefficient gives
the unique Laplacian value exactly. -/
theorem criticalPacketSpectralValue (γ : ℂ) (_hγ : γ ≠ 0) :
    -(1 / (1 / γ ^ 2)) - 1 / 4 = -γ ^ 2 - 1 / 4 := by
  field_simp

/-- The real part and modulus of `A = (a+iγ)^2` recover `a^2` when written
as the two elementary real-coordinate equations. -/
theorem recoverASquaredFromSquareCoordinates (a γ : ℂ) :
    ((a ^ 2 + γ ^ 2) + (a ^ 2 - γ ^ 2)) / 2 = a ^ 2 := by
  ring

/-- The same two equations recover `γ^2`. -/
theorem recoverGammaSquaredFromSquareCoordinates (a γ : ℂ) :
    ((a ^ 2 + γ ^ 2) - (a ^ 2 - γ ^ 2)) / 2 = γ ^ 2 := by
  ring

/-- A sign fibre carrying multiplicity `m` contributes `2m` after the
quadratic pushforward. -/
theorem signFibreMultiplicity (m : ℕ) : m + m = 2 * m := by
  omega

/-- The cycle-length substitution returns the original frequency after
clearing the nonzero denominators. -/
theorem cycleLengthFrequency
    (p n ν L : ℝ)
    (hν : ν ≠ 0)
    (hL : L = 2 * p * n / ν) :
    L * ν = 2 * p * n := by
  rw [hL]
  field_simp

end ZetaFunctionFoundation.SpectralPacketCoordinates
