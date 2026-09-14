import SplitZeroObservedIterates
import SplitZeroMonicResidue

/-!
# Exact residue-polynomial test for the original cyclic observation

Each actual observation row is converted by the EXISTING perfect monic
residue duality into an element of AdjoinRoot h. The complete invisible
kernel is their common annihilator. No squarefreeness or injected purity
hypothesis is used. The polynomial gcd evaluation of that annihilator is
recorded separately as a written consequence, not assumed in these proofs.
-/
noncomputable section
namespace SplitZero.ResidueObservation
open Polynomial
open scoped BigOperators

variable {K J : Type*} [Field K] {h : K[X]}

/-- The original multiplication action on the literal polynomial quotient. -/
def rootAction (h : K[X]) : Module.End K (AdjoinRoot h) where
  toFun x := AdjoinRoot.root h * x
  map_add' x y := mul_add _ _ _
  map_smul' r x := by simp

@[simp] theorem root_pow_apply (h : K[X]) (n : ℕ) (x : AdjoinRoot h) :
    (rootAction h ^ n) x = AdjoinRoot.root h ^ n * x := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [pow_succ', Module.End.mul_apply]
      change AdjoinRoot.root h * ((rootAction h ^ n) x) = _
      rw [ih, pow_succ', mul_assoc]

/-- Retain the actual rows, rather than an arbitrarily chosen detecting functional. -/
def observation (rows : J → AdjoinRoot h →ₗ[K] K) :
    AdjoinRoot h →ₗ[K] (J → K) := LinearMap.pi rows

/-- A row's coefficient is constructed by the previously proved residue equivalence. -/
def rowCoefficient (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (j : J) : AdjoinRoot h :=
  (MonicResidue.residueEquiv hh hd).symm (rows j)

theorem row_formula (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (j : J) (x : AdjoinRoot h) :
    rows j x = MonicResidue.residue hh (x * rowCoefficient hh hd rows j) := by
  have he := LinearMap.congr_fun
    ((MonicResidue.residueEquiv hh hd).apply_symm_apply (rows j)) x
  exact he.symm

/-- Annihilating all actual row coefficients kills every observed iterate. -/
theorem annihilator_kills_iterate (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (x : AdjoinRoot h)
    (hx : ∀ j, rowCoefficient hh hd rows j * x = 0) (n : ℕ) :
    observation rows ((rootAction h ^ n) x) = 0 := by
  funext j
  change rows j ((rootAction h ^ n) x) = 0
  rw [root_pow_apply, row_formula hh hd rows j]
  calc
    MonicResidue.residue hh
        ((AdjoinRoot.root h ^ n * x) * rowCoefficient hh hd rows j) =
      MonicResidue.residue hh
        (AdjoinRoot.root h ^ n * (rowCoefficient hh hd rows j * x)) := by
          congr 1
          ring
    _ = 0 := by rw [hx j, mul_zero, map_zero]

/-- All of the first deg(h) observations suffice, including every repeated-root jet. -/
theorem finite_kernel_iff (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (x : AdjoinRoot h) :
    x ∈ ObservedIterates.window (observation rows) (rootAction h) h.natDegree ↔
      ∀ j, rowCoefficient hh hd rows j * x = 0 := by
  constructor
  · intro hx j
    by_contra hn
    obtain ⟨n, hnd, hdetect⟩ := MonicResidue.exists_detecting_monomial hh hd
      (rowCoefficient hh hd rows j * x) hn
    have he := congrFun
      ((ObservedIterates.mem_window _ _ _ _).mp hx ⟨n, hnd⟩) j
    change rows j ((rootAction h ^ n) x) = 0 at he
    rw [root_pow_apply, row_formula hh hd rows j] at he
    apply hdetect
    simpa only [mul_assoc, mul_comm, mul_left_comm] using he
  · intro hx
    apply (ObservedIterates.mem_window _ _ _ _).mpr
    intro n
    exact annihilator_kills_iterate hh hd rows x hx n.val

/-- The largest invisible invariant kernel is exactly the common annihilator. -/
theorem invisible_kernel_iff (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (x : AdjoinRoot h) :
    x ∈ ObservedIterates.invisible (observation rows) (rootAction h) ↔
      ∀ j, rowCoefficient hh hd rows j * x = 0 := by
  constructor
  · intro hx
    apply (finite_kernel_iff hh hd rows x).mp
    exact (ObservedIterates.mem_window _ _ _ _).mpr fun n =>
      (ObservedIterates.mem_invisible _ _ _).mp hx n.val
  · intro hx
    exact (ObservedIterates.mem_invisible _ _ _).mpr
      (annihilator_kills_iterate hh hd rows x hx)

/-- Concrete finite determination, using residue detection rather than assuming recurrence. -/
theorem original_finite_determination (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) :
    ObservedIterates.window (observation rows) (rootAction h) h.natDegree =
      ObservedIterates.invisible (observation rows) (rootAction h) := by
  ext x
  rw [finite_kernel_iff hh hd, invisible_kernel_iff hh hd]

/-- A literal Bezout certificate suffices for faithfulness; it is not automatic. -/
theorem injective_of_bezout [Fintype J] (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (coeff : J → AdjoinRoot h)
    (hbezout : ∑ j, coeff j * rowCoefficient hh hd rows j = 1) :
    Function.Injective
      (ObservedIterates.observe (observation rows) (rootAction h) h.natDegree) := by
  rw [← LinearMap.ker_eq_bot, ObservedIterates.ker_observe]
  apply le_antisymm ?_ bot_le
  intro x hx
  have hann := (finite_kernel_iff hh hd rows x).mp hx
  change x = 0
  calc
    x = (∑ j, coeff j * rowCoefficient hh hd rows j) * x := by rw [hbezout, one_mul]
    _ = ∑ j, coeff j * (rowCoefficient hh hd rows j * x) := by
      rw [Finset.sum_mul]
      simp only [mul_assoc]
    _ = 0 := by simp only [hann, mul_zero, Finset.sum_const_zero]

end SplitZero.ResidueObservation
