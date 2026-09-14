import SplitZeroCanonicalSourceContrast
import SplitZeroResolventSeries
import SplitZeroSignedTraceEnclosure

/-!
# Signed finite resolvents on the original canonical source columns

The four projectors come from the existing canonical sections and their actual
inverse Grams. Relation ranks can differ. All pairings use one original form.
-/
noncomputable section
namespace SplitZero.CanonicalSignedResolvent
open Matrix MetricVariation SourceProjectorContrast SignedTraceEnclosure
open scoped ComplexOrder MatrixOrder BigOperators
variable {j n : Type*} [Fintype j] [DecidableEq j] [Fintype n] [DecidableEq n]

section Algebra
omit [Fintype n] [DecidableEq n] [DecidableEq j] in
theorem weighted_mul (M A B : Matrix j j ℂ)
    (ha : A.conjTranspose * M = M * A) (hb : B.conjTranspose * M = M * B)
    (hc : A * B = B * A) :
    (A * B).conjTranspose * M = M * (A * B) := by
  calc
    _ = B.conjTranspose * (A.conjTranspose * M) := by
      simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]
    _ = M * (B * A) := by rw [ha, ← Matrix.mul_assoc, hb, Matrix.mul_assoc]
    _ = _ := by rw [← hc]

omit [Fintype n] [DecidableEq n] in
theorem weighted_pow (M H : Matrix j j ℂ)
    (hh : H.conjTranspose * M = M * H) (p : ℕ) :
    (H ^ p).conjTranspose * M = M * H ^ p := by
  induction p with
  | zero => simp
  | succ p ih =>
    rw [pow_succ]
    exact weighted_mul M (H ^ p) H ih hh (by simpa only [pow_one] using pow_mul_comm H p 1)

omit [Fintype n] [DecidableEq n] in
theorem weighted_partialSum (M H T X : Matrix j j ℂ)
    (hh : H.conjTranspose * M = M * H) (hx : X.conjTranspose * M = M * X)
    (hc : H * X = X * H) (hsolve : (1 - H) * X = T) (L : ℕ) :
    (ResolventSeries.partialSum H T L).conjTranspose * M =
      M * ResolventSeries.partialSum H T L := by
  have hcomm : Commute H X := hc
  have hr := weighted_mul M (H ^ (L + 1)) X (weighted_pow M H hh _) hx
    (hcomm.pow_left (L + 1)).eq
  have he : ResolventSeries.partialSum H T L = X - H ^ (L + 1) * X := by
    have h := ResolventSeries.residual_exact H T X L hsolve
    rw [← h]
    abel
  rw [he]
  simp only [Matrix.conjTranspose_sub, Matrix.sub_mul, Matrix.mul_sub, hx, hr]
end Algebra

variable (m : Fin 4 → Type*) [∀ a, Fintype (m a)] [∀ a, DecidableEq (m a)]
variable (B : ∀ a, Matrix j (m a) ℂ) (M : ∀ a, Metric (B a))
variable (C : Fin 4 → Matrix j n ℂ) (K : Fin 4 → Matrix n n ℂ)
variable (source : Matrix j j ℂ) (hcommon : ∀ a, (M a).form = source)
variable (hK : ∀ a, (M a).quotientGram (C a) * K a = 1)

def canonicalContrast : Matrix j j ℂ :=
  contrast (fun a => projector source ((M a).sectionMap (C a)) (K a))

include hcommon hK in
omit [DecidableEq j] in
theorem canonical_properties :
    Matrix.trace (canonicalContrast m B M C K source) = 0 ∧
      (canonicalContrast m B M C K source).conjTranspose * source =
        source * canonicalContrast m B M C K source := by
  refine ⟨CanonicalSourceContrast.canonical_contrast_trace m B M C K source hcommon hK, ?_⟩
  have hp (a : Fin 4) :
      (projector source ((M a).sectionMap (C a)) (K a)).conjTranspose * source =
        source * projector source ((M a).sectionMap (C a)) (K a) := by
    rw [← hcommon a]
    exact (CanonicalSourceContrast.canonical_frame (B a) (M a) (C a) (K a) (hK a)).2.1
  simp only [canonicalContrast, contrast, Matrix.conjTranspose_sub, Matrix.conjTranspose_add,
    Matrix.sub_mul, Matrix.add_mul, Matrix.mul_sub, Matrix.mul_add, hp]

include hcommon hK in
theorem canonical_interval (hsource : source.PosDef) (X Y : Matrix j j ℂ)
    (hx : X.conjTranspose * source = source * X)
    (hy : Y.conjTranspose * source = source * Y) :
    let Q := canonicalContrast m B M C K source
    let E := center (X - Y)
    let err := Real.sqrt (realTrace (E * E) * realTrace (Q * Q))
    realTrace (Y * Q) - err ≤ realTrace (X * Q) ∧
      realTrace (X * Q) ≤ realTrace (Y * Q) + err := by
  have hp := canonical_properties m B M C K source hcommon hK
  exact signed_interval source X Y _ hsource hx hy hp.2 hp.1

include hcommon hK in
/-- The approximation error is the constructed finite Neumann residual. -/
theorem canonical_resolvent_interval (hsource : source.PosDef) (H T X : Matrix j j ℂ)
    (hh : H.conjTranspose * source = source * H)
    (hx : X.conjTranspose * source = source * X)
    (hc : H * X = X * H) (hsolve : (1 - H) * X = T) (L : ℕ) :
    let Q := canonicalContrast m B M C K source
    let Y := ResolventSeries.partialSum H T L
    let E := center (H ^ (L + 1) * X)
    let err := Real.sqrt (realTrace (E * E) * realTrace (Q * Q))
    realTrace (Y * Q) - err ≤ realTrace (X * Q) ∧
      realTrace (X * Q) ≤ realTrace (Y * Q) + err := by
  have hy := weighted_partialSum source H T X hh hx hc hsolve L
  have h := canonical_interval m B M C K source hcommon hK hsource X _ hx hy
  dsimp only at h ⊢
  rw [ResolventSeries.residual_exact H T X L hsolve] at h
  exact h

include hcommon hK in
theorem canonical_tangent (J E : Matrix j j ℂ) (hJ : source * J = 1) :
    Matrix.trace ((J * E) * canonicalContrast m B M C K source) =
      Matrix.trace (K 0 * (((M 0).sectionMap (C 0)).conjTranspose * E * (M 0).sectionMap (C 0))) +
      Matrix.trace (K 1 * (((M 1).sectionMap (C 1)).conjTranspose * E * (M 1).sectionMap (C 1))) -
      Matrix.trace (K 2 * (((M 2).sectionMap (C 2)).conjTranspose * E * (M 2).sectionMap (C 2))) -
      Matrix.trace (K 3 * (((M 3).sectionMap (C 3)).conjTranspose * E * (M 3).sectionMap (C 3))) :=
  (CanonicalSourceContrast.canonical_signed_pairing m B M C K source J E hcommon hK hJ).2
end SplitZero.CanonicalSignedResolvent
