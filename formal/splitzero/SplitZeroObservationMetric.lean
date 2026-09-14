import SplitZeroRestrictionSource
import Mathlib.Analysis.Matrix.Order

/-!
# OPR1--4: the original observation section and its retained kernel

The section is the existing `Restriction.representative`, instantiated with
source metric G and observation Lambda. No independently chosen quotient
metric or orthogonality assumption replaces that construction. Rectangular
columns keep every mixed Gram entry; the boundary image may be empty.
-/
noncomputable section
namespace SplitZero.ObservationMetric
open Matrix
open scoped ComplexOrder

variable {e b : Type*} [Fintype e] [DecidableEq e]
  [Fintype b] [DecidableEq b]

/-- The actual source inverse and observed covariance inverse. -/
structure Data (e b : Type*) [Fintype e] [DecidableEq e]
    [Fintype b] [DecidableEq b] where
  G : Matrix e e ℂ
  K : Matrix e e ℂ
  obs : Matrix b e ℂ
  Q : Matrix b b ℂ
  positive : G.PosDef
  hermitianG : G.conjTranspose = G
  hermitianK : K.conjTranspose = K
  hermitianQ : Q.conjTranspose = Q
  left_inverse : K * G = 1
  right_inverse : G * K = 1
  observed_inverse : (obs * K * obs.conjTranspose) * Q = 1

namespace Data
variable (O : Data e b)

/-- The old minimum section, now for the stated boundary observation. -/
def sectionMap : Matrix e b ℂ :=
  Restriction.representative O.obs O.K O.Q

theorem section_observation : O.obs * O.sectionMap = 1 :=
  Restriction.representative_section O.obs O.K O.Q O.observed_inverse

theorem section_adjoint : O.sectionMap.conjTranspose * O.G = O.Q * O.obs :=
  Restriction.representative_adjoint O.obs O.G O.K O.Q
    O.left_inverse O.hermitianK O.hermitianQ

theorem section_gram : O.sectionMap.conjTranspose * O.G * O.sectionMap = O.Q :=
  Restriction.representative_gram O.obs O.G O.K O.Q
    O.left_inverse O.hermitianK O.hermitianQ O.observed_inverse

theorem metric_section : O.G * O.sectionMap = O.obs.conjTranspose * O.Q := by
  simp only [sectionMap, Restriction.representative, ← Matrix.mul_assoc,
    O.right_inverse, Matrix.one_mul]

/-- All columns of X remain, including their off-diagonal pairings. -/
def residual {t : Type*} (X : Matrix e t ℂ) : Matrix e t ℂ :=
  X - O.sectionMap * (O.obs * X)

theorem residual_observation {t : Type*} (X : Matrix e t ℂ) :
    O.obs * O.residual X = 0 := by
  simp only [residual, Matrix.mul_sub, ← Matrix.mul_assoc,
    O.section_observation, Matrix.one_mul, sub_self]

theorem kernel_section_orthogonal {t : Type*} (I : Matrix e t ℂ)
    (hI : O.obs * I = 0) : I.conjTranspose * O.G * O.sectionMap = 0 := by
  rw [Matrix.mul_assoc, O.metric_section, ← Matrix.mul_assoc,
    ← Matrix.conjTranspose_mul, hI, Matrix.conjTranspose_zero, Matrix.zero_mul]

/-- Exact complete mixed Gram subtraction, not merely a scalar norm identity. -/
theorem residual_gram {t : Type*} (X : Matrix e t ℂ) :
    (O.residual X).conjTranspose * O.G * O.residual X =
      X.conjTranspose * O.G * X -
        (O.obs * X).conjTranspose * O.Q * (O.obs * X) := by
  let Z := O.obs * X
  let T := O.sectionMap * Z
  have hXT : X.conjTranspose * O.G * T = Z.conjTranspose * O.Q * Z := by
    dsimp [T, Z]
    rw [Matrix.mul_assoc, ← Matrix.mul_assoc O.G, O.metric_section]
    simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]
  have hTX : T.conjTranspose * O.G * X = Z.conjTranspose * O.Q * Z := by
    calc
      _ = Z.conjTranspose * (O.sectionMap.conjTranspose * O.G) * X := by
        simp only [T, Matrix.conjTranspose_mul, Matrix.mul_assoc]
      _ = Z.conjTranspose * (O.Q * O.obs) * X := by rw [O.section_adjoint]
      _ = _ := by simp only [Z, Matrix.mul_assoc]
  have hTT : T.conjTranspose * O.G * T = Z.conjTranspose * O.Q * Z := by
    dsimp [T]
    rw [Matrix.conjTranspose_mul]
    calc
      _ = Z.conjTranspose *
          (O.sectionMap.conjTranspose * O.G * O.sectionMap) * Z := by
            simp only [Matrix.mul_assoc]
      _ = _ := by rw [O.section_gram]
  change (X - T).conjTranspose * O.G * (X - T) = _
  calc
    _ = X.conjTranspose * O.G * X - X.conjTranspose * O.G * T -
          (T.conjTranspose * O.G * X - T.conjTranspose * O.G * T) := by
        simp only [Matrix.conjTranspose_sub, Matrix.sub_mul, Matrix.mul_sub]
        abel
    _ = _ := by rw [hXT, hTX, hTT]; dsimp [Z]; abel

theorem residual_difference_positive {t : Type*} [Fintype t] (X : Matrix e t ℂ) :
    (X.conjTranspose * O.G * X -
      (O.obs * X).conjTranspose * O.Q * (O.obs * X)).PosSemidef := by
  rw [← O.residual_gram X]
  exact O.positive.posSemidef.conjTranspose_mul_mul_same _

/-- Fixed-section and metric-section kernels differ by the stated kernel lift. -/
theorem fixed_section_correction {r t : Type*} [Fintype r]
    (I : Matrix e r ℂ) (kap : Matrix r e ℂ) (S : Matrix e b ℂ)
    (hsplit : I * kap = 1 - S * O.obs) (X : Matrix e t ℂ) :
    O.residual X = I * (kap * X - kap * O.sectionMap * (O.obs * X)) := by
  have hkS : I * kap * O.sectionMap = O.sectionMap - S := by
    rw [hsplit, Matrix.sub_mul, Matrix.one_mul, Matrix.mul_assoc,
      O.section_observation, Matrix.mul_one]
  calc
    _ = (1 - S * O.obs) * X - (O.sectionMap - S) * (O.obs * X) := by
      simp only [Matrix.sub_mul, Matrix.one_mul, Matrix.mul_assoc, residual]
      abel
    _ = (I * kap) * X - (I * kap * O.sectionMap) * (O.obs * X) := by
      rw [hkS, hsplit]
    _ = _ := by simp only [Matrix.mul_sub, Matrix.mul_assoc]

/-- A further corrected kernel basis has the original restricted Gram. -/
theorem corrected_kernel_gram {r t : Type*} [Fintype r]
    (I : Matrix e r ℂ) (V : Matrix r t ℂ) (X : Matrix e t ℂ)
    (hV : O.residual X = I * V) :
    V.conjTranspose * (I.conjTranspose * O.G * I) * V =
      X.conjTranspose * O.G * X -
        (O.obs * X).conjTranspose * O.Q * (O.obs * X) := by
  rw [← O.residual_gram X, hV]
  simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]

end Data

/-- Preserve the denominator and the original boundary-first elimination order. -/
theorem ordered_factors (t xi : ℝ) (hxi : 0 ≤ xi) (hres : xi ≤ t) :
    1 + xi > 0 ∧ 1 + (t - xi) / (1 + xi) ≥ 1 ∧
      (1 + xi) * (1 + (t - xi) / (1 + xi)) = 1 + t := by
  have hp : 0 < 1 + xi := by linarith
  refine ⟨hp, ?_, ?_⟩
  · exact le_add_of_nonneg_right (div_nonneg (sub_nonneg.mpr hres) hp.le)
  · field_simp
    ring

end SplitZero.ObservationMetric
