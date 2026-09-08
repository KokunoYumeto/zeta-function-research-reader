import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp

/-!
# Exact deformed-Verblunsky/derivative-state crosswalk

This file certifies the finite algebraic part of the crosswalk between the
deformed Verblunsky coordinates of Bourgade--Nikeghbali--Rouault and the
phase-rotated coordinates used by the derivative peel.  Probability laws and
Radon--Nikodym derivatives remain stated and proved in the human-readable
manuscript from the cited source densities; they are not introduced here as
axioms.
-/

namespace ZetaFunctionFoundation.GammaBetaCrosswalk

noncomputable section

open scoped BigOperators

/-- Bourgade--Nikeghbali--Rouault's formula
`gamma_n(1) = conj(alpha_n) / b_n(1)` with
`b_n(1) = A_n / conj(A_n)`, written with the conjugate values retained as
independent algebraic coordinates. -/
def bnrGammaAtOne (alphaBar A Abar : ℂ) : ℂ :=
  alphaBar / (A / Abar)

/-- The local phase-rotated coordinate. -/
def localBeta (alphaBar A Abar : ℂ) : ℂ :=
  alphaBar * Abar / A

/-- The two coordinates are literally equal wherever the inverse Schur value
is defined.  No normalization or asymptotic identification is used. -/
theorem bnrGammaAtOne_eq_localBeta
    (alphaBar A Abar : ℂ) (hA : A ≠ 0) (hAbar : Abar ≠ 0) :
    bnrGammaAtOne alphaBar A Abar = localBeta alphaBar A Abar := by
  unfold bnrGammaAtOne localBeta
  field_simp [hA, hAbar]

/-- The exact logarithmic-derivative transition, now regarded as a lift of a
deformed Verblunsky coordinate sequence. -/
def transition (n : ℕ) (gamma u : ℂ) : ℂ :=
  (1 + u - gamma * ((n : ℂ) - starRingEnd ℂ u)) / (1 - gamma)

/-- The unique deterministic state obtained from a retained gamma sequence. -/
def stateLift (gamma : ℕ → ℂ) : ℕ → ℂ
  | 0 => 0
  | n + 1 => transition n (gamma n) (stateLift gamma n)

@[simp] theorem stateLift_zero (gamma : ℕ → ℂ) : stateLift gamma 0 = 0 := rfl

@[simp] theorem stateLift_succ (gamma : ℕ → ℂ) (n : ℕ) :
    stateLift gamma (n + 1) =
      transition n (gamma n) (stateLift gamma n) := rfl

/-- The graph lift has singleton fibres over a gamma sequence: any two states
with the same initial value and transition equations agree coordinatewise. -/
theorem stateLift_unique
    (gamma u : ℕ → ℂ)
    (hZero : u 0 = 0)
    (hStep : ∀ n, u (n + 1) = transition n (gamma n) (u n)) :
    ∀ n, u n = stateLift gamma n := by
  intro n
  induction n with
  | zero => simpa using hZero
  | succ n ih =>
      rw [hStep n, stateLift_succ, ih]

end

end ZetaFunctionFoundation.GammaBetaCrosswalk
