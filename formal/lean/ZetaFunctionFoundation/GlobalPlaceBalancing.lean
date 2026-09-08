import Mathlib.Tactic

/-!
# The finite three-coordinate place-balancing core

This file certifies the integer-linear-algebra layer of the one-finite-prime
case and its arbitrary finite-place extension below.  It does not construct
the C-star algebras, Busby pullback, multiplier-algebra codiagonal, or K-theory
naturality morphism; those analytic objects are proved separately in the
manuscript.
-/

namespace ZetaFunctionFoundation.GlobalPlaceBalancing

open scoped BigOperators

/-- The proved direct sum of the finite-prime and archimedean coordinate maps. -/
def directSumBoundary (k nPlus nMinus : ℤ) : ℤ × ℤ :=
  (-k, -(nPlus + nMinus))

/-- The additional integer codiagonal. -/
def codiagonal (x : ℤ × ℤ) : ℤ := x.1 + x.2

/-- The scalar balancing row, retained with its minus sign. -/
def scalarBoundary (k nPlus nMinus : ℤ) : ℤ :=
  -(k + nPlus + nMinus)

theorem codiagonal_directSumBoundary
    (k nPlus nMinus : ℤ) :
    codiagonal (directSumBoundary k nPlus nMinus) =
      scalarBoundary k nPlus nMinus := by
  simp [codiagonal, directSumBoundary, scalarBoundary]
  ring

theorem directSumKernel_iff
    (k nPlus nMinus : ℤ) :
    directSumBoundary k nPlus nMinus = (0, 0) ↔
      k = 0 ∧ nPlus + nMinus = 0 := by
  constructor
  · intro h
    have hFinite := congrArg Prod.fst h
    have hInfinite := congrArg Prod.snd h
    simp [directSumBoundary] at hFinite hInfinite
    exact ⟨hFinite, by omega⟩
  · rintro ⟨hFinite, hInfinite⟩
    simp [directSumBoundary, hFinite, hInfinite]

/-- Exact coordinates in the A2 kernel: a*(1,-1,0)+b*(0,1,-1). -/
theorem scalarKernel_coordinates_iff
    (k nPlus nMinus : ℤ) :
    scalarBoundary k nPlus nMinus = 0 ↔
      ∃ a b : ℤ,
        k = a ∧ nPlus = -a + b ∧ nMinus = -b := by
  constructor
  · intro h
    refine ⟨k, k + nPlus, rfl, ?_, ?_⟩
    · ring
    · simp [scalarBoundary] at h
      omega
  · rintro ⟨a, b, rfl, rfl, rfl⟩
    simp [scalarBoundary]

/-- The three retained Gram entries of the ordered simple-root basis. -/
theorem a2GramEntries :
    ((1 : ℤ) * 1 + (-1) * (-1) + 0 * 0 = 2) ∧
    ((1 : ℤ) * 0 + (-1) * 1 + 0 * (-1) = -1) ∧
    ((0 : ℤ) * 0 + 1 * 1 + (-1) * (-1) = 2) := by
  norm_num

/-!
## Arbitrarily many finite places

The following definitions certify the full finite-coordinate diagram used by
the stable Busby construction.  They do not formalize multiplier algebras,
Busby invariants, or the naturality theorem for C-star K-theory.
-/

/-- The direct sum of all finite-place `-1` maps and the retained
archimedean two-character map. -/
def directSumBoundaryN {n : ℕ}
    (k : Fin n → ℤ) (nPlus nMinus : ℤ) : (Fin n → ℤ) × ℤ :=
  (fun i => -k i, -(nPlus + nMinus))

/-- The codiagonal induced by the proved orthogonal-corner ideal map. -/
def codiagonalN {n : ℕ} (x : (Fin n → ℤ) × ℤ) : ℤ :=
  (∑ i, x.1 i) + x.2

/-- The scalar row obtained after the extension-level codiagonal. -/
def scalarBoundaryN {n : ℕ}
    (k : Fin n → ℤ) (nPlus nMinus : ℤ) : ℤ :=
  -((∑ i, k i) + nPlus + nMinus)

theorem codiagonal_directSumBoundaryN {n : ℕ}
    (k : Fin n → ℤ) (nPlus nMinus : ℤ) :
    codiagonalN (directSumBoundaryN k nPlus nMinus) =
      scalarBoundaryN k nPlus nMinus := by
  simp [codiagonalN, directSumBoundaryN, scalarBoundaryN]
  ring

theorem scalarKernelN_iff {n : ℕ}
    (k : Fin n → ℤ) (nPlus nMinus : ℤ) :
    scalarBoundaryN k nPlus nMinus = 0 ↔
      (∑ i, k i) + nPlus + nMinus = 0 := by
  unfold scalarBoundaryN
  omega

theorem scalarBoundaryN_surjective {n : ℕ} (r : ℤ) :
    ∃ (k : Fin n → ℤ) (nPlus nMinus : ℤ),
      scalarBoundaryN k nPlus nMinus = r := by
  refine ⟨fun _ => 0, 0, -r, ?_⟩
  simp [scalarBoundaryN]

/-- Once naturality identifies a candidate bottom boundary with the explicit
codiagonal of the direct-sum boundary, its complete coordinate formula follows
without an additional sign convention. -/
theorem boundary_from_naturality {n : ℕ}
    (bottomBoundary : (Fin n → ℤ) → ℤ → ℤ → ℤ)
    (hNaturality : ∀ k nPlus nMinus,
      bottomBoundary k nPlus nMinus =
        codiagonalN (directSumBoundaryN k nPlus nMinus))
    (k : Fin n → ℤ) (nPlus nMinus : ℤ) :
    bottomBoundary k nPlus nMinus =
      scalarBoundaryN k nPlus nMinus := by
  rw [hNaturality]
  exact codiagonal_directSumBoundaryN k nPlus nMinus

end ZetaFunctionFoundation.GlobalPlaceBalancing
