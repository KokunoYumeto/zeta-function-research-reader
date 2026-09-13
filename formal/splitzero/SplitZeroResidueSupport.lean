import SplitZeroPeriodTransport

/-!
# Residue insertion and operator descent through original supported relations

Fibrewise source sections are not forced to be natural. The explicit
section defect is required to be an original relation before an operator
is assembled on the existing quotient diagram.
-/
noncomputable section
namespace SplitZero.Integration
open SplitZero.Reconstruction

universe u v
variable {R : Type u} [CommRing R] {L : Type v}
  [SemilatticeSup L] [OrderBot L]
  {D E : LinearDiagram R L}

section LocalResidue
variable {V F Q : Type*} [AddCommGroup V] [Module R V]
  [AddCommGroup F] [Module R F] [AddCommGroup Q] [Module R Q]

/-- The original residue insertion, with unit vector and functional specified. -/
def residueInsertion (one : V) (ell : V →ₗ[R] R) : V →ₗ[R] V :=
  ell.smulRight one

/-- The transverse map keeps both the quotient unit and restricted residue. -/
theorem residue_quotient_factor (one : V) (ell : V →ₗ[R] R)
    (inc : F →ₗ[R] V) (pi : V →ₗ[R] Q) :
    pi.comp ((residueInsertion one ell).comp inc) =
      (ell.comp inc).smulRight (pi one) := by
  apply LinearMap.ext
  intro x
  change pi (ell (inc x) • one) = ell (inc x) • pi one
  exact pi.map_smul _ _

/-- A normalized residue vector supplies the inverse on the image line. -/
theorem residue_image_line (one : V) (ell : V →ₗ[R] R)
    (pivot : V) (hp : ell pivot = 1) (y : V) :
    (∃ x, residueInsertion one ell x = y) ↔ ∃ c : R, c • one = y := by
  constructor
  · rintro ⟨x, hx⟩
    exact ⟨ell x, hx⟩
  · rintro ⟨c, hc⟩
    refine ⟨c • pivot, ?_⟩
    change ell (c • pivot) • one = y
    rw [map_smul, hp, smul_eq_mul, mul_one]
    exact hc

end LocalResidue

section QuotientAction
variable (J : Hom D E) (r : ∀ i, E.V i →ₗ[R] D.V i)
  (B : Relations D)
  (hB : ∀ i x, x ∈ B.fibre i → J.app i x = 0)
  (hdef : ∀ {i j} (h : i ≤ j) v, sectionDefect r h v ∈ B.fibre j)

/-- Actual operator on the already constructed internal quotient. -/
def quotientLiftOperator (A : Hom E E) : Hom B.quotientDiagram B.quotientDiagram where
  app i := (B.fibre i).mapQ (B.fibre i) (liftOperator J r A i) (by
    intro x hx
    rw [liftOperator_kills_kernel J r A i x (hB i x hx)]
    exact (B.fibre i).zero_mem)
  naturality {i j} h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x =>
      change (B.fibre j).mkQ (liftOperator J r A j (D.map h x)) =
        (B.fibre j).mkQ (D.map h (liftOperator J r A i x))
      apply Eq.symm
      apply (Submodule.Quotient.eq (B.fibre j)).mpr
      rw [liftOperator_transition J r A h x]
      exact hdef h _

/-- Operator and original observation commute on the reconstructed totals. -/
theorem quotient_operator_square
    (hr : ∀ i v, J.app i (r i v) = v) (A : Hom E E) :
    (observation J B hB).comp (quotientLiftOperator J r B hB hdef A).total =
      A.total.comp (observation J B hB) := by
  apply LinearMap.ext
  intro y
  obtain ⟨⟨i, x⟩, rfl⟩ := B.quotient_surjective y
  change observation J B hB
    (B.quotientMap.total ⟨i, liftOperator J r A i x⟩) =
      A.total (observation J B hB (B.quotientMap.total ⟨i, x⟩))
  rw [observed_class, observed_class]
  change (⟨i, J.app i (r i (A.app i (J.app i x)))⟩ : E.Total) =
    ⟨i, A.app i (J.app i x)⟩
  rw [hr]

/-- The operator keeps the zero of each original quotient fibre. -/
theorem quotient_operator_supported_zero (A : Hom E E) (i : L) :
    (quotientLiftOperator J r B hB hdef A).total
      (⟨i, 0⟩ : B.quotientDiagram.Total) = ⟨i, 0⟩ := by
  change (⟨i, (quotientLiftOperator J r B hB hdef A).app i 0⟩ :
    B.quotientDiagram.Total) = ⟨i, 0⟩
  rw [map_zero]

end QuotientAction
end SplitZero.Integration
