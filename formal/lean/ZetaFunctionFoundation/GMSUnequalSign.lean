import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring

/-!
# Unequal-length CUE determinant sign

This file certifies the finite algebraic counterexample and the exponent
identity used in the correction to the unequal-length determinant formula in
Grover--Mezzadri--Simm, arXiv:2604.03051v1.

The formal result is deliberately cross-multiplied: it does not divide by a
Vandermonde and therefore has no hidden distinctness assumption.  It does not
formalize Haar integration, the general confluent determinant, or the
large-N limit.
-/

namespace ZetaFunctionFoundation.GMSUnequalSign

/-- The direct U(1) Haar moment after constant-Fourier-coefficient
extraction for K = 2, L = 1, N = 1. -/
def directMoment (z₁ z₂ w : ℂ) : ℂ :=
  1 + w * (z₁ + z₂)

/-- The kernel-first numerator in the formula printed in version 1:
K₂(r) = 1 + r, the kernel entries are zᵢ K₂(zᵢ w), and the
single excess column is 1. -/
def kernelFirstNumerator (z₁ z₂ w : ℂ) : ℂ :=
  z₁ * (1 + z₁ * w) - z₂ * (1 + z₂ * w)

/-- The Vandermonde convention used in the source. -/
def delta₂ (z₁ z₂ : ℂ) : ℂ :=
  z₂ - z₁

/-- The printed kernel-first numerator is the negative Vandermonde times
the direct moment.  This is the exact missing-sign counterexample. -/
theorem kernelFirstNumerator_eq_neg_delta_mul_directMoment
    (z₁ z₂ w : ℂ) :
    kernelFirstNumerator z₁ z₂ w =
      -delta₂ z₁ z₂ * directMoment z₁ z₂ w := by
  unfold kernelFirstNumerator delta₂ directMoment
  ring

/-- After inserting (-1)^(L(K-L)) = -1 for K = 2, L = 1,
the cross-multiplied determinant identity has the correct sign. -/
theorem corrected_K2_L1_cross_multiplication (z₁ z₂ w : ℂ) :
    (-1 : ℂ) * kernelFirstNumerator z₁ z₂ w =
      delta₂ z₁ z₂ * directMoment z₁ z₂ w := by
  rw [kernelFirstNumerator_eq_neg_delta_mul_directMoment]
  ring

/-- Twice the fixed-sign exponent identity with K = L + d.
The two final summands on the right are even, so the undoubled exponent has
the parity of L*d. -/
theorem doubled_fixed_exponent_identity (L d : ℤ) :
    (L + d) * (L + d - 1) + L * (L - 1) + d * (d - 1) =
      2 * (L * d + L * (L - 1) + d * (d - 1)) := by
  ring

end ZetaFunctionFoundation.GMSUnequalSign
