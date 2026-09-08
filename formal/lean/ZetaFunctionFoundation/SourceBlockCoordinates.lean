import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Lie.Classical
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.LinearCombination

/-!
# Exact retained coordinates for the first-derivative source block

This file formalizes `FORMAL-20260825-0007`.  It keeps every finite coordinate:
the `s^2` matrix coordinates, the dependent `mu` coordinates, the dependent
`nu` coordinates, and the lower-right scalar in the traceless block.  It does
not postulate or construct any map from a CUE object to these coordinates.
-/

open scoped BigOperators

namespace ZetaFunctionFoundation

/-- Coordinates in the retained direct sum `J_mu = direct_sum_i C^(mu_i)`. -/
abbrev JCoord (s : Nat) (mu : Fin s -> Nat) := Sigma fun i => Fin (mu i)

/-- Every coordinate of `End(C^s) direct_sum J_mu direct_sum J_nu^dual`. -/
abbrev SourceCoord (s : Nat) (mu nu : Fin s -> Nat) :=
  Sum (Fin s × Fin s) (Sum (JCoord s mu) (JCoord s nu))

/-- The source block as the full complex coordinate space, with nothing quotiented out. -/
abbrev SourceBlock (s : Nat) (mu nu : Fin s -> Nat) :=
  SourceCoord s mu nu -> Complex

theorem sourceCoord_card (s : Nat) (mu nu : Fin s -> Nat) :
    Fintype.card (SourceCoord s mu nu) =
      s ^ 2 + (Finset.univ.sum mu + Finset.univ.sum nu) := by
  simp [SourceCoord, JCoord, pow_two]

theorem sourceBlock_finrank (s : Nat) (mu nu : Fin s -> Nat) :
    Module.finrank Complex (SourceBlock s mu nu) =
      s ^ 2 + (Finset.univ.sum mu + Finset.univ.sum nu) := by
  simp [SourceBlock, pow_two]

/-- Matrix, column, and row coordinates retained separately. -/
abbrev FirstDerivativeSource (s : Nat) :=
  Matrix (Fin s) (Fin s) Complex × ((Fin s -> Complex) × (Fin s -> Complex))

/-- All four blocks of a matrix on `C^s direct_sum C`, before imposing trace zero. -/
abbrev BlockData (s : Nat) :=
  Matrix (Fin s) (Fin s) Complex ×
    ((Fin s -> Complex) × ((Fin s -> Complex) × Complex))

/-- The coordinate trace `Tr(A) + lambda` of a four-block matrix. -/
def blockTraceLinear (s : Nat) : BlockData s →ₗ[Complex] Complex where
  toFun X := Matrix.trace X.1 + X.2.2.2
  map_add' X Y := by
    simp [Matrix.trace_add, add_assoc, add_left_comm, add_comm]
  map_smul' c X := by
    simp [Matrix.trace_smul, mul_add]

/-- Traceless matrices on `C^s direct_sum C`, represented in the fixed four-block coordinates. -/
abbrev TracelessBlock (s : Nat) := LinearMap.ker (blockTraceLinear s)

/-- The displayed block map `(A,u,phi) |-> [[A,u],[phi,-Tr(A)]]`. -/
def sourceToTraceless (s : Nat) : FirstDerivativeSource s →ₗ[Complex] TracelessBlock s where
  toFun X :=
    ⟨(X.1, (X.2.1, (X.2.2, -Matrix.trace X.1))), by
      simp [blockTraceLinear]⟩
  map_add' X Y := by
    apply Subtype.ext
    apply Prod.ext
    · rfl
    · apply Prod.ext
      · rfl
      · apply Prod.ext
        · rfl
        · change -Matrix.trace (X.1 + Y.1) =
            -Matrix.trace X.1 + -Matrix.trace Y.1
          rw [Matrix.trace_add]
          ring
  map_smul' c X := by
    apply Subtype.ext
    apply Prod.ext
    · rfl
    · apply Prod.ext
      · rfl
      · apply Prod.ext
        · rfl
        · change -Matrix.trace (c • X.1) = c • (-Matrix.trace X.1)
          rw [Matrix.trace_smul]
          change -(c * Matrix.trace X.1) = c * (-Matrix.trace X.1)
          ring

/-- Block extraction discards no source coordinate. -/
def tracelessToSource (s : Nat) : TracelessBlock s →ₗ[Complex] FirstDerivativeSource s where
  toFun X := (X.1.1, (X.1.2.1, X.1.2.2.1))
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

theorem tracelessToSource_sourceToTraceless (s : Nat) (X : FirstDerivativeSource s) :
    tracelessToSource s (sourceToTraceless s X) = X := by
  rfl

theorem sourceToTraceless_tracelessToSource (s : Nat) (X : TracelessBlock s) :
    sourceToTraceless s (tracelessToSource s X) = X := by
  apply Subtype.ext
  rcases X with ⟨⟨A, u, phi, lambda⟩, htrace⟩
  change (A, u, phi, -Matrix.trace A) = (A, u, phi, lambda)
  have hlambda : lambda = -Matrix.trace A := by
    change Matrix.trace A + lambda = 0 at htrace
    linear_combination htrace
  simp [hlambda]

/-- Exact complex-linear coordinate equivalence, with the displayed extraction inverse. -/
def sourceTracelessEquiv (s : Nat) :
    FirstDerivativeSource s ≃ₗ[Complex] TracelessBlock s where
  toLinearMap := sourceToTraceless s
  invFun := tracelessToSource s
  left_inv := tracelessToSource_sourceToTraceless s
  right_inv := sourceToTraceless_tracelessToSource s

theorem sourceToTraceless_ker (s : Nat) :
    LinearMap.ker (sourceToTraceless s) = ⊥ := by
  exact LinearMap.ker_eq_bot.mpr (sourceTracelessEquiv s).injective

theorem sourceToTraceless_range (s : Nat) :
    LinearMap.range (sourceToTraceless s) = ⊤ := by
  exact LinearMap.range_eq_top.mpr (sourceTracelessEquiv s).surjective

theorem sourceToTraceless_fibre_singleton (s : Nat) (Y : TracelessBlock s) :
    {X : FirstDerivativeSource s | sourceToTraceless s X = Y} =
      {tracelessToSource s Y} := by
  ext X
  constructor
  · intro h
    change sourceToTraceless s X = Y at h
    change X = tracelessToSource s Y
    calc
      X = tracelessToSource s (sourceToTraceless s X) :=
        (tracelessToSource_sourceToTraceless s X).symm
      _ = tracelessToSource s Y := congrArg (tracelessToSource s) h
  · intro h
    change X = tracelessToSource s Y at h
    change sourceToTraceless s X = Y
    rw [h]
    exact sourceToTraceless_tracelessToSource s Y

/-- The displayed index decomposition for matrices on `C^s direct_sum C`. -/
abbrev BlockIndex (s : Nat) := Sum (Fin s) Unit

/-- Assemble the four retained blocks into the corresponding matrix. -/
def blockToMatrix (s : Nat) (X : BlockData s) :
    Matrix (BlockIndex s) (BlockIndex s) Complex := fun i j =>
  match i, j with
  | Sum.inl a, Sum.inl b => X.1 a b
  | Sum.inl a, Sum.inr _ => X.2.1 a
  | Sum.inr _, Sum.inl b => X.2.2.1 b
  | Sum.inr _, Sum.inr _ => X.2.2.2

/-- Extract the four blocks from a matrix on the displayed direct sum. -/
def matrixToBlock (s : Nat) (M : Matrix (BlockIndex s) (BlockIndex s) Complex) :
    BlockData s :=
  ( (fun i j => M (Sum.inl i) (Sum.inl j)),
    ( (fun i => M (Sum.inl i) (Sum.inr ())),
      ((fun j => M (Sum.inr ()) (Sum.inl j)), M (Sum.inr ()) (Sum.inr ())) ) )

def blockToMatrixLinear (s : Nat) :
    BlockData s →ₗ[Complex] Matrix (BlockIndex s) (BlockIndex s) Complex where
  toFun := blockToMatrix s
  map_add' X Y := by
    ext i j
    cases i <;> cases j <;> rfl
  map_smul' c X := by
    ext i j
    cases i <;> cases j <;> rfl

def matrixToBlockLinear (s : Nat) :
    Matrix (BlockIndex s) (BlockIndex s) Complex →ₗ[Complex] BlockData s where
  toFun := matrixToBlock s
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

theorem matrixToBlock_blockToMatrix (s : Nat) (X : BlockData s) :
    matrixToBlock s (blockToMatrix s X) = X := by
  rfl

theorem blockToMatrix_matrixToBlock
    (s : Nat) (M : Matrix (BlockIndex s) (BlockIndex s) Complex) :
    blockToMatrix s (matrixToBlock s M) = M := by
  ext i j
  cases i <;> cases j <;> rfl

/-- The exact four-block coordinate equivalence with full matrices. -/
def blockMatrixEquiv (s : Nat) :
    BlockData s ≃ₗ[Complex] Matrix (BlockIndex s) (BlockIndex s) Complex where
  toLinearMap := blockToMatrixLinear s
  invFun := matrixToBlock s
  left_inv := matrixToBlock_blockToMatrix s
  right_inv := blockToMatrix_matrixToBlock s

theorem trace_blockToMatrix (s : Nat) (X : BlockData s) :
    Matrix.trace (blockToMatrix s X) = blockTraceLinear s X := by
  simp [Matrix.trace, blockToMatrix, blockTraceLinear, Fintype.sum_sum_type]

/-- The coordinate traceless block mapped into Mathlib's actual special-linear Lie algebra. -/
def tracelessBlockToSL (s : Nat) :
    TracelessBlock s →ₗ[Complex]
      LieAlgebra.SpecialLinear.sl (BlockIndex s) Complex where
  toFun X :=
    ⟨blockToMatrix s X.1, by
      change Matrix.trace (blockToMatrix s X.1) = 0
      rw [trace_blockToMatrix]
      exact X.2⟩
  map_add' X Y := by
    apply Subtype.ext
    exact (blockToMatrixLinear s).map_add X.1 Y.1
  map_smul' c X := by
    apply Subtype.ext
    exact (blockToMatrixLinear s).map_smul c X.1

/-- Extract Mathlib's special-linear matrix back to the retained four blocks. -/
def slToTracelessBlock (s : Nat) :
    LieAlgebra.SpecialLinear.sl (BlockIndex s) Complex →ₗ[Complex]
      TracelessBlock s where
  toFun X :=
    ⟨matrixToBlock s X.1, by
      change blockTraceLinear s (matrixToBlock s X.1) = 0
      rw [← trace_blockToMatrix, blockToMatrix_matrixToBlock]
      exact X.2⟩
  map_add' X Y := by
    apply Subtype.ext
    rfl
  map_smul' c X := by
    apply Subtype.ext
    rfl

theorem slToTracelessBlock_tracelessBlockToSL
    (s : Nat) (X : TracelessBlock s) :
    slToTracelessBlock s (tracelessBlockToSL s X) = X := by
  apply Subtype.ext
  exact matrixToBlock_blockToMatrix s X.1

theorem tracelessBlockToSL_slToTracelessBlock
    (s : Nat) (X : LieAlgebra.SpecialLinear.sl (BlockIndex s) Complex) :
    tracelessBlockToSL s (slToTracelessBlock s X) = X := by
  apply Subtype.ext
  exact blockToMatrix_matrixToBlock s X.1

/-- Exact linear equivalence from retained traceless blocks to the special-linear Lie algebra. -/
def tracelessBlockSLEquiv (s : Nat) :
    TracelessBlock s ≃ₗ[Complex]
      LieAlgebra.SpecialLinear.sl (BlockIndex s) Complex where
  toLinearMap := tracelessBlockToSL s
  invFun := slToTracelessBlock s
  left_inv := slToTracelessBlock_tracelessBlockToSL s
  right_inv := tracelessBlockToSL_slToTracelessBlock s

/-- The complete displayed-coordinate equivalence to the actual special-linear Lie algebra. -/
def sourceSLEquiv (s : Nat) :
    FirstDerivativeSource s ≃ₗ[Complex]
      LieAlgebra.SpecialLinear.sl (BlockIndex s) Complex :=
  (sourceTracelessEquiv s).trans (tracelessBlockSLEquiv s)

/-- The matrix commutator pulled back through the exact coordinate equivalence. -/
def sourceCommutator (s : Nat)
    (X Y : FirstDerivativeSource s) : FirstDerivativeSource s :=
  (sourceSLEquiv s).symm ⁅sourceSLEquiv s X, sourceSLEquiv s Y⁆

theorem sourceSLEquiv_sourceCommutator (s : Nat)
    (X Y : FirstDerivativeSource s) :
    sourceSLEquiv s (sourceCommutator s X Y) =
      ⁅sourceSLEquiv s X, sourceSLEquiv s Y⁆ := by
  simp [sourceCommutator]

theorem sourceCommutator_matrix_formula (s : Nat)
    (X Y : FirstDerivativeSource s) :
    (sourceSLEquiv s (sourceCommutator s X Y)).1 =
      (sourceSLEquiv s X).1 * (sourceSLEquiv s Y).1 -
        (sourceSLEquiv s Y).1 * (sourceSLEquiv s X).1 := by
  rw [sourceSLEquiv_sourceCommutator]
  rfl

end ZetaFunctionFoundation
