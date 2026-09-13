import SplitZeroMonicResidue
import SplitZeroResidueSupport

/-!
# Exact nonzero transverse residue on every proper invariant constituent

The original multiplication action is multiplication by `AdjoinRoot.root h`.
Its invariant coefficient submodule is not presumed invariant for residue insertion.
The original quotient and existing `Integration.residueInsertion` are reused.
-/
noncomputable section
namespace SplitZero.MonicResidue
open Polynomial

variable {K : Type*} [Field K] {h : K[X]}

/-- Invariance under the actual original sum generator. -/
def RootStable (F : Submodule K (AdjoinRoot h)) : Prop :=
  ∀ x, x ∈ F → AdjoinRoot.root h * x ∈ F

theorem root_pow_mul_mem (F : Submodule K (AdjoinRoot h)) (hF : RootStable F)
    {x : AdjoinRoot h} (hx : x ∈ F) (n : ℕ) :
    (AdjoinRoot.root h) ^ n * x ∈ F := by
  induction n with
  | zero => simpa using hx
  | succ n ih => simpa only [pow_succ', mul_assoc] using hF _ ih

/-- Root invariance implies closure under every original quotient multiplier. -/
theorem stable_mul_mem (F : Submodule K (AdjoinRoot h)) (hF : RootStable F)
    {x : AdjoinRoot h} (hx : x ∈ F) (y : AdjoinRoot h) : y * x ∈ F := by
  induction y using AdjoinRoot.induction_on with
  | ih p =>
    induction p using Polynomial.induction_on' with
    | add p q hp hq => simpa only [map_add, add_mul] using F.add_mem hp hq
    | monomial n a =>
      rw [← Polynomial.C_mul_X_pow_eq_monomial, map_mul, map_pow, AdjoinRoot.mk_X]
      simpa only [Algebra.smul_def, mul_assoc] using
        F.smul_mem a (root_pow_mul_mem F hF hx n)

/-- A proper original invariant constituent does not contain the cyclic unit. -/
theorem unit_not_mem (F : Submodule K (AdjoinRoot h))
    (hF : RootStable F) (htop : F ≠ ⊤) : (1 : AdjoinRoot h) ∉ F := by
  intro h1
  apply htop
  apply eq_top_iff.mpr
  intro x _
  simpa only [mul_one] using stable_mul_mem F hF h1 x

/-- A nonzero invariant constituent is detected by the literal top residue. -/
theorem restricted_residue_ne_zero (hh : h.Monic) (hd : 0 < h.natDegree)
    (F : Submodule K (AdjoinRoot h)) (hF : RootStable F) (hbot : F ≠ ⊥) :
    (residue hh).comp F.subtype ≠ 0 := by
  intro hz
  apply hbot
  apply eq_bot_iff.mpr
  intro x hx
  change x = 0
  apply residue_separates hh hd
  intro y
  have hy := stable_mul_mem F hF hx y
  have hval := LinearMap.congr_fun hz (⟨y * x, hy⟩ : F)
  exact hval

/-- An actual normalized residue vector, not a rank-one nonvanishing assumption. -/
theorem exists_residue_one (hh : h.Monic) (hd : 0 < h.natDegree)
    (F : Submodule K (AdjoinRoot h)) (hF : RootStable F) (hbot : F ≠ ⊥) :
    ∃ v : F, residue hh (v : AdjoinRoot h) = 1 := by
  have hne := restricted_residue_ne_zero hh hd F hF hbot
  have hex : ∃ v : F, residue hh (v : AdjoinRoot h) ≠ 0 := by
    by_contra hn
    push Not at hn
    apply hne
    ext v
    exact hn v
  obtain ⟨v, hv⟩ := hex
  refine ⟨(residue hh (v : AdjoinRoot h))⁻¹ • v, ?_⟩
  simp [map_smul, hv]

/-- The already integrated residue insertion, followed by the original constituent quotient. -/
def transverse (hh : h.Monic) (F : Submodule K (AdjoinRoot h)) :
    F →ₗ[K] (AdjoinRoot h ⧸ F) :=
  F.mkQ.comp ((SplitZero.Integration.residueInsertion 1 (residue hh)).comp F.subtype)

@[simp] theorem transverse_apply (hh : h.Monic) (F : Submodule K (AdjoinRoot h))
    (v : F) : transverse hh F v = residue hh (v : AdjoinRoot h) • F.mkQ 1 := by
  change F.mkQ (residue hh (v : AdjoinRoot h) • (1 : AdjoinRoot h)) = _
  exact F.mkQ.map_smul _ _

theorem quotient_unit_ne_zero (F : Submodule K (AdjoinRoot h))
    (hF : RootStable F) (htop : F ≠ ⊤) : F.mkQ 1 ≠ 0 := by
  intro hz
  exact unit_not_mem F hF htop ((Submodule.Quotient.mk_eq_zero F).mp hz)

/-- Every scalar multiple of the retained quotient-unit class is attained. -/
theorem transverse_range (hh : h.Monic) (hd : 0 < h.natDegree)
    (F : Submodule K (AdjoinRoot h)) (hF : RootStable F) (hbot : F ≠ ⊥) :
    LinearMap.range (transverse hh F) = Submodule.span K {F.mkQ 1} := by
  obtain ⟨pivot, hp⟩ := exists_residue_one hh hd F hF hbot
  ext y
  constructor
  · rintro ⟨x, rfl⟩
    rw [transverse_apply]
    exact Submodule.smul_mem _ _ (Submodule.subset_span (by simp))
  · intro hy
    obtain ⟨c, hc⟩ := Submodule.mem_span_singleton.mp hy
    refine ⟨c • pivot, ?_⟩
    simpa [transverse_apply, map_smul, hp] using hc

/-- Kernel equality retains all undetected directions, rather than deleting them. -/
theorem transverse_kernel (hh : h.Monic) (F : Submodule K (AdjoinRoot h))
    (hF : RootStable F) (htop : F ≠ ⊤) :
    LinearMap.ker (transverse hh F) = LinearMap.ker ((residue hh).comp F.subtype) := by
  ext v
  change transverse hh F v = 0 ↔ residue hh (v : AdjoinRoot h) = 0
  rw [transverse_apply]
  simp only [smul_eq_zero, quotient_unit_ne_zero F hF htop, or_false]

/-- Exact rank one on every nonzero proper invariant constituent, including multiple roots. -/
theorem transverse_rank_one (hh : h.Monic) (hd : 0 < h.natDegree)
    (F : Submodule K (AdjoinRoot h)) (hF : RootStable F)
    (hbot : F ≠ ⊥) (htop : F ≠ ⊤) :
    Module.finrank K (LinearMap.range (transverse hh F)) = 1 := by
  rw [transverse_range hh hd F hF hbot]
  exact finrank_span_singleton (quotient_unit_ne_zero F hF htop)

/-- The exact codimension-one kernel; this does not assert injectivity on a larger constituent. -/
theorem transverse_nullity (hh : h.Monic) (hd : 0 < h.natDegree)
    (F : Submodule K (AdjoinRoot h)) (hF : RootStable F)
    (hbot : F ≠ ⊥) (htop : F ≠ ⊤) :
    Module.finrank K (LinearMap.ker (transverse hh F)) + 1 = Module.finrank K F := by
  letI : Module.Finite K (AdjoinRoot h) := hh.finite_adjoinRoot
  rw [transverse_kernel hh F hF htop]
  exact Module.Dual.finrank_ker_add_one_of_ne_zero
    (restricted_residue_ne_zero hh hd F hF hbot)

/-- No nonzero proper original invariant constituent is also preserved by insertion. -/
theorem not_insertion_stable (hh : h.Monic) (hd : 0 < h.natDegree)
    (F : Submodule K (AdjoinRoot h)) (hF : RootStable F)
    (hbot : F ≠ ⊥) (htop : F ≠ ⊤) :
    ¬ (∀ v : F, SplitZero.Integration.residueInsertion 1 (residue hh) v ∈ F) := by
  intro hs
  obtain ⟨v, hv⟩ := exists_residue_one hh hd F hF hbot
  have hm := hs v
  change residue hh (v : AdjoinRoot h) • (1 : AdjoinRoot h) ∈ F at hm
  rw [hv, one_smul] at hm
  exact unit_not_mem F hF htop hm

end SplitZero.MonicResidue
