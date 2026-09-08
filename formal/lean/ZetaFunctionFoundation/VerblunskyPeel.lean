import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Exact finite algebra for the phase-rotated Verblunsky derivative peel

This file certifies the algebraic identities in Theorem
`thm:verblunsky-peel-derived` of the working synthesis.  The source theorem
on independent Haar Verblunsky parameters and the conditional probability-law
transport remain human-sourced/written inputs; no probability theorem is
postulated here.
-/

namespace ZetaFunctionFoundation.VerblunskyPeel

noncomputable section

open scoped BigOperators

/-- Cross-multiplied form of the logarithmic-derivative transition obtained by
differentating the Szegő recurrence.  Every displayed coordinate is retained. -/
theorem szegoDerivativeTransitionCross
    (A Abar D Dbar alphaBar n : ℂ)
    (hA : A ≠ 0) (hAbar : Abar ≠ 0) :
    let beta := alphaBar * Abar / A
    let u := D / A
    let ubar := Dbar / Abar
    let nextA := A - alphaBar * Abar
    let nextD := A + D - alphaBar * (n * Abar - Dbar)
    (1 - beta) * nextD = nextA * (1 + u - beta * (n - ubar)) := by
  dsimp
  field_simp [hA, hAbar]

/-- The literal rational `T_n` transition, with all nonzero denominators stated. -/
theorem szegoDerivativeTransition
    (A Abar D Dbar alphaBar n : ℂ)
    (hA : A ≠ 0) (hAbar : Abar ≠ 0)
    (hNextA : A - alphaBar * Abar ≠ 0)
    (hOneMinusBeta : 1 - alphaBar * Abar / A ≠ 0) :
    (A + D - alphaBar * (n * Abar - Dbar)) /
        (A - alphaBar * Abar) =
      (1 + D / A - (alphaBar * Abar / A) * (n - Dbar / Abar)) /
        (1 - alphaBar * Abar / A) := by
  field_simp [hA, hAbar, hNextA, hOneMinusBeta]

/-- Algebraic conjugate-pair form of the exact half-plane transport identity. -/
theorem halfPlaneTransport
    (w wbar beta betaBar : ℂ)
    (hBeta : 1 - beta ≠ 0) (hBetaBar : 1 - betaBar ≠ 0) :
    let nextW := (w + 1 + beta * (wbar + 1)) / (1 - beta)
    let nextWbar := (wbar + 1 + betaBar * (w + 1)) / (1 - betaBar)
    (nextW + nextWbar) / 2 =
      ((1 - beta * betaBar) / ((1 - beta) * (1 - betaBar))) *
        ((w + wbar) / 2 + 1) := by
  dsimp
  field_simp [hBeta, hBetaBar]
  ring

/-- Difference of the squared denominator and numerator of the actual
`η_n` coordinate. -/
theorem etaNormSqDifference
    (N n u ubar : ℂ) :
    (N - n + u) * (N - n + ubar) -
        (N - 1 - ubar) * (N - 1 - u) =
      (2 * N - n - 1) * (1 - n + u + ubar) := by
  ring

/-- Ordered-real coordinate form of the preceding identity. -/
theorem etaNormSqDifferenceReal
    (N n x y : ℝ) :
    ((N - n + x) ^ 2 + y ^ 2) -
        ((N - 1 - x) ^ 2 + y ^ 2) =
      (2 * N - n - 1) * (1 - n + 2 * x) := by
  ring

/-- The exact hypotheses under which the `η_n` numerator has strictly smaller
squared modulus than its denominator. -/
theorem etaSquaredModulusRatioLtOne
    (N n x y : ℝ)
    (hSize : 0 < 2 * N - n - 1)
    (hState : 0 < 1 - n + 2 * x) :
    ((N - 1 - x) ^ 2 + y ^ 2) /
        ((N - n + x) ^ 2 + y ^ 2) < 1 := by
  have hDiff :
      0 < ((N - n + x) ^ 2 + y ^ 2) -
        ((N - 1 - x) ^ 2 + y ^ 2) := by
    rw [etaNormSqDifferenceReal]
    exact mul_pos hSize hState
  have hDen : 0 < (N - n + x) ^ 2 + y ^ 2 := by
    linarith [sq_nonneg (N - 1 - x), sq_nonneg y]
  exact (div_lt_one hDen).2 (by linarith)

/-- The one-step `η_n` telescope, before any finite product is taken. -/
theorem oneStepTelescope
    (N n u ubar beta : ℂ) (hBeta : 1 - beta ≠ 0)
    (hStateDen : N - n + u ≠ 0) :
    let nextU := (1 + u - beta * (n - ubar)) / (1 - beta)
    let eta := (N - 1 - ubar) / (N - n + u)
    (1 - beta) * (N - n - 1 + nextU) =
      (N - n + u) * (1 - beta * eta) := by
  dsimp
  field_simp [hBeta, hStateDen]
  ring

/-- The inverse phase formula recovers the `β` coordinate exactly. -/
theorem triangularBetaRecovery
    (A Abar beta : ℂ) (hA : A ≠ 0) (hAbar : Abar ≠ 0) :
    let alphaBar := beta * A / Abar
    alphaBar * Abar / A = beta := by
  dsimp
  field_simp [hA, hAbar]

/-- The same inverse reproduces the exact `A_{n+1}=A_n(1-β_n)` transition. -/
theorem triangularARecovery
    (A Abar beta : ℂ) (hAbar : Abar ≠ 0) :
    let alphaBar := beta * A / Abar
    A - alphaBar * Abar = A * (1 - beta) := by
  dsimp
  field_simp [hAbar]

/-- Abstract finite-product telescope used by the complete derivative peel. -/
theorem finiteProductTelescope
    {M : Type*} [CommMonoid M]
    (q factor : ℕ → M)
    (hStep : ∀ n, q (n + 1) = q n * factor n) :
    ∀ N, q N = q 0 * ∏ n ∈ Finset.range N, factor n := by
  intro N
  induction N with
  | zero => simp
  | succ N ih =>
      rw [hStep N, ih, Finset.prod_range_succ]
      simp [mul_assoc]

/-- The sourced `A` transition and the one-step `η` identity combine into the
single multiplicative state used by `finiteProductTelescope`. -/
theorem combinedPeelStep
    (A nextA r nextR beta factor : ℂ)
    (hA : nextA = A * (1 - beta))
    (hR : (1 - beta) * nextR = r * factor) :
    nextA * nextR = (A * r) * factor := by
  rw [hA]
  calc
    A * (1 - beta) * nextR = A * ((1 - beta) * nextR) := by ring
    _ = A * (r * factor) := by rw [hR]
    _ = (A * r) * factor := by ring

/-- Terminal factor converts the partial telescope into the full derivative. -/
theorem terminalDerivativeTelescope
    (partialValue A r terminal derivative N : ℂ)
    (hN : N ≠ 0)
    (hPartial : partialValue = A * r / N)
    (hDerivative : derivative = A * r * terminal) :
    partialValue * terminal = derivative / N := by
  rw [hPartial, hDerivative]
  field_simp [hN]

/-- A constant unit-modulus phase preserves squared modulus exactly. -/
theorem unitPhasePreservesNormSq
    (phase value : ℂ) (hPhase : phase * starRingEnd ℂ phase = 1) :
    (phase * value) * starRingEnd ℂ (phase * value) =
      value * starRingEnd ℂ value := by
  simp only [map_mul]
  calc
    phase * value * (starRingEnd ℂ phase * starRingEnd ℂ value) =
        (phase * starRingEnd ℂ phase) *
          (value * starRingEnd ℂ value) := by ring
    _ = value * starRingEnd ℂ value := by rw [hPhase, one_mul]

end

end ZetaFunctionFoundation.VerblunskyPeel
