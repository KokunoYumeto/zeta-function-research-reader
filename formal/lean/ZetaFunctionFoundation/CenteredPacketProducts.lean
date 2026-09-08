import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Centered packet-product coordinate identities

This file certifies the finite commutative-algebra identities used in Chapter
17.  It deliberately does not formalize Hadamard factorization, convergence of
the zeta zero product, analytic continuation, or any assertion about an
individual zero.
-/

namespace ZetaFunctionFoundation.CenteredPacketProducts

/-- Pairing the two genus-one numerators at opposite centered zeros removes
the linear terms. -/
theorem signPairFactor
    (z α : ℂ) (hα : α ≠ 0) :
    (1 - z / α) * (1 + z / α) = 1 - z ^ 2 / α ^ 2 := by
  field_simp
  ring

/-- The unnormalized four-point packet in centered real coordinates. -/
theorem fourPointRootExpansion (z a γ : ℂ) :
    (((z - a) ^ 2 + γ ^ 2) * ((z + a) ^ 2 + γ ^ 2)) =
      (a ^ 2 + γ ^ 2) ^ 2
        + 2 * (γ ^ 2 - a ^ 2) * z ^ 2
        + z ^ 4 := by
  ring

/-- The critical-line two-point numerator is quadratic. -/
theorem twoPointRootExpansion (z γ : ℂ) :
    (z - Complex.I * γ) * (z + Complex.I * γ) = z ^ 2 + γ ^ 2 := by
  calc
    (z - Complex.I * γ) * (z + Complex.I * γ) =
        z ^ 2 - (Complex.I * γ) ^ 2 := by ring
    _ = z ^ 2 + γ ^ 2 := by
      rw [mul_pow, Complex.I_sq]
      ring

/-- The quartic coefficient coordinate recovers the difference of the two
squared real coordinates before the final two-by-two linear inversion. -/
theorem quarticDeltaIdentity
    (a γ c₂ c₄ : ℂ)
    (hc₄ : c₄ ≠ 0)
    (_h₄ : c₄ * (a ^ 2 + γ ^ 2) ^ 2 = 1)
    (h₂ : c₂ = 2 * c₄ * (γ ^ 2 - a ^ 2)) :
    c₂ / (2 * c₄) = γ ^ 2 - a ^ 2 := by
  rw [h₂]
  field_simp

/-- Solving radius-squared and difference coordinates recovers a-squared. -/
theorem recoverASquared (a γ : ℂ) :
    ((a ^ 2 + γ ^ 2) - (γ ^ 2 - a ^ 2)) / 2 = a ^ 2 := by
  ring

/-- Solving radius-squared and difference coordinates recovers gamma-squared. -/
theorem recoverGammaSquared (a γ : ℂ) :
    ((a ^ 2 + γ ^ 2) + (γ ^ 2 - a ^ 2)) / 2 = γ ^ 2 := by
  ring

/-- The finite three-factor case of the elementary-symmetric Taylor
coordinate formula, retaining every sign. -/
theorem threeFactorSymmetricExpansion (z a b c : ℂ) :
    (1 - a * z ^ 2) * (1 - b * z ^ 2) * (1 - c * z ^ 2) =
      1
        - (a + b + c) * z ^ 2
        + (a * b + a * c + b * c) * z ^ 4
        - (a * b * c) * z ^ 6 := by
  ring

/-- Clearing denominators in the four-root logarithmic derivative gives the
derivative numerator of the monic quartic. -/
theorem fourRootLogDerivativeNumerator
    (s r₁ r₂ r₃ r₄ : ℂ) :
    (s - r₂) * (s - r₃) * (s - r₄)
      + (s - r₁) * (s - r₃) * (s - r₄)
      + (s - r₁) * (s - r₂) * (s - r₄)
      + (s - r₁) * (s - r₂) * (s - r₃) =
    4 * s ^ 3
      - 3 * (r₁ + r₂ + r₃ + r₄) * s ^ 2
      + 2 *
          (r₁ * r₂ + r₁ * r₃ + r₁ * r₄
            + r₂ * r₃ + r₂ * r₄ + r₃ * r₄) * s
      - (r₁ * r₂ * r₃ + r₁ * r₂ * r₄
          + r₁ * r₃ * r₄ + r₂ * r₃ * r₄) := by
  ring

/-- Multiplicity three retains the complementary value in the first nonzero
coefficient; the remainder begins in degree four. -/
theorem multiplicityThreeLeadingJet
    (t h₀ h₁ g₀ g₁ : ℂ) :
    (h₀ + h₁ * t) * (t * (g₀ + g₁ * t)) ^ 3 =
      h₀ * g₀ ^ 3 * t ^ 3
        + t ^ 4 *
          (3 * h₀ * g₀ ^ 2 * g₁
            + h₁ * g₀ ^ 3
            + t * (3 * h₀ * g₀ * g₁ ^ 2
              + 3 * h₁ * g₀ ^ 2 * g₁)
            + t ^ 2 * (h₀ * g₁ ^ 3
              + 3 * h₁ * g₀ * g₁ ^ 2)
            + t ^ 3 * h₁ * g₁ ^ 3) := by
  ring

end ZetaFunctionFoundation.CenteredPacketProducts
