import SplitZeroSourceProjectorContrast
import SplitZeroMixedSupportMetric

/-!
# Canonical source instances of the four-projector calculation

The columns here are the inherited Metric.sectionMap, not independent matrices
chosen to have the same dimension. Different endpoints can have different
numbers of original relation columns. The form is one specified common source.
-/
noncomputable section
namespace SplitZero.CanonicalSourceContrast
open Matrix MetricVariation SourceProjectorContrast
variable {j n : Type*} [Fintype j] [Fintype n] [DecidableEq n]

/-- Construct all three projector properties from the canonical source Gram. -/
theorem canonical_frame {m : Type*} [Fintype m] [DecidableEq m]
    (B : Matrix j m ℂ) (M : Metric B) (C : Matrix j n ℂ) (K : Matrix n n ℂ)
    (hK : M.quotientGram C * K = 1) :
    projector M.form (M.sectionMap C) K * projector M.form (M.sectionMap C) K =
      projector M.form (M.sectionMap C) K ∧
    (projector M.form (M.sectionMap C) K).conjTranspose * M.form =
      M.form * projector M.form (M.sectionMap C) K ∧
    Matrix.trace (projector M.form (M.sectionMap C) K) = (Fintype.card n : ℂ) := by
  have hG : (M.quotientGram C).conjTranspose = M.quotientGram C := by
    simp only [Metric.quotientGram, MetricVariation.gram, Matrix.conjTranspose_mul,
      Matrix.conjTranspose_conjTranspose, M.hermitian, Matrix.mul_assoc]
  have hkprod : K.conjTranspose * M.quotientGram C = 1 := by
    simpa only [Matrix.conjTranspose_mul, hG, Matrix.conjTranspose_one] using
      congrArg Matrix.conjTranspose hK
  have hkstar : K.conjTranspose = K := by
    calc
      K.conjTranspose = K.conjTranspose * (M.quotientGram C * K) := by
        rw [hK, Matrix.mul_one]
      _ = (K.conjTranspose * M.quotientGram C) * K := (Matrix.mul_assoc _ _ _).symm
      _ = K := by rw [hkprod, Matrix.one_mul]
  exact ⟨projector_idempotent M.form (M.sectionMap C) K hK,
    projector_adjoint M.form (M.sectionMap C) K M.hermitian hkstar,
    projector_trace M.form (M.sectionMap C) K hK⟩

/-- All four actual endpoint residuals share the stated source, with different relation ranks. -/
theorem canonical_contrast_trace
    (m : Fin 4 → Type*) [∀ a, Fintype (m a)] [∀ a, DecidableEq (m a)]
    (B : ∀ a, Matrix j (m a) ℂ) (M : ∀ a, Metric (B a))
    (C : Fin 4 → Matrix j n ℂ) (K : Fin 4 → Matrix n n ℂ)
    (Msource : Matrix j j ℂ) (hcommon : ∀ a, (M a).form = Msource)
    (hK : ∀ a, (M a).quotientGram (C a) * K a = 1) :
    Matrix.trace (contrast (fun a => projector Msource ((M a).sectionMap (C a)) (K a))) = 0 := by
  apply contrast_trace _ (Fintype.card n : ℂ)
  intro a
  rw [← hcommon a]
  exact (canonical_frame (B a) (M a) (C a) (K a) (hK a)).2.2

/-- The source tangent and traceless cancellation are composed on canonical columns. -/
theorem canonical_signed_pairing [DecidableEq j]
    (m : Fin 4 → Type*) [∀ a, Fintype (m a)] [∀ a, DecidableEq (m a)]
    (B : ∀ a, Matrix j (m a) ℂ) (M : ∀ a, Metric (B a))
    (C : Fin 4 → Matrix j n ℂ) (K : Fin 4 → Matrix n n ℂ)
    (Msource J E : Matrix j j ℂ) (hcommon : ∀ a, (M a).form = Msource)
    (hK : ∀ a, (M a).quotientGram (C a) * K a = 1) (hJ : Msource * J = 1) :
    Matrix.trace (contrast (fun a => projector Msource ((M a).sectionMap (C a)) (K a))) = 0 ∧
    Matrix.trace ((J * E) * contrast (fun a => projector Msource ((M a).sectionMap (C a)) (K a))) =
      Matrix.trace (K 0 * (((M 0).sectionMap (C 0)).conjTranspose * E * (M 0).sectionMap (C 0))) +
      Matrix.trace (K 1 * (((M 1).sectionMap (C 1)).conjTranspose * E * (M 1).sectionMap (C 1))) -
      Matrix.trace (K 2 * (((M 2).sectionMap (C 2)).conjTranspose * E * (M 2).sectionMap (C 2))) -
      Matrix.trace (K 3 * (((M 3).sectionMap (C 3)).conjTranspose * E * (M 3).sectionMap (C 3))) := by
  refine ⟨canonical_contrast_trace m B M C K Msource hcommon hK, ?_⟩
  rw [contrast_pairing]
  rw [← trace_tangent_pairing Msource J E ((M 0).sectionMap (C 0)) (K 0) hJ,
    ← trace_tangent_pairing Msource J E ((M 1).sectionMap (C 1)) (K 1) hJ,
    ← trace_tangent_pairing Msource J E ((M 2).sectionMap (C 2)) (K 2) hJ,
    ← trace_tangent_pairing Msource J E ((M 3).sectionMap (C 3)) (K 3) hJ]

end SplitZero.CanonicalSourceContrast
