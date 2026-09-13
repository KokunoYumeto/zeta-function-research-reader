import Mathlib.RingTheory.AdjoinRoot
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Tactic

/-!
# The literal monic-remainder residue is perfect

The coefficient algebra is Mathlib's original polynomial quotient `AdjoinRoot h`.
No irreducibility, squarefreeness, discriminant inverse or root enumeration is used.
The proof detects a nonzero remainder by its leading coefficient.
-/
noncomputable section
namespace SplitZero.MonicResidue
open Polynomial

variable {K : Type*} [Field K] {h : K[X]}

/-- The actual top coefficient of the unique monic remainder. -/
def residue (hh : h.Monic) : AdjoinRoot h →ₗ[K] K :=
  (Polynomial.lcoeff K (h.natDegree - 1)).comp (AdjoinRoot.modByMonicHom hh)

@[simp] theorem residue_mk (hh : h.Monic) (p : K[X]) :
    residue hh (AdjoinRoot.mk h p) = (p %ₘ h).coeff (h.natDegree - 1) := rfl

/-- Below the original modulus degree, no reduction changes the coefficient. -/
theorem residue_mk_of_lt (hh : h.Monic) (p : K[X])
    (hp : p.natDegree < h.natDegree) :
    residue hh (AdjoinRoot.mk h p) = p.coeff (h.natDegree - 1) := by
  rw [residue_mk, (Polynomial.modByMonic_eq_self_iff hh).mpr]
  exact lt_of_le_of_lt Polynomial.degree_le_natDegree (by
    rw [Polynomial.degree_eq_natDegree hh.ne_zero]
    exact_mod_cast hp)

/-- The chosen representative remains below the full degree, including repeated factors. -/
theorem remainder_degree_lt (hh : h.Monic) (hd : 0 < h.natDegree)
    (x : AdjoinRoot h) :
    (AdjoinRoot.modByMonicHom hh x).natDegree < h.natDegree := by
  obtain ⟨p, rfl⟩ := AdjoinRoot.mk_surjective x
  change (p %ₘ h).natDegree < h.natDegree
  apply Polynomial.natDegree_modByMonic_lt p hh
  intro he
  rw [he, Polynomial.natDegree_one] at hd
  omega

/-- Construct a monomial detecting each nonzero class by the original residue. -/
theorem exists_detecting_monomial (hh : h.Monic) (hd : 0 < h.natDegree)
    (x : AdjoinRoot h) (hx : x ≠ 0) :
    ∃ n : ℕ, n < h.natDegree ∧
      residue hh ((AdjoinRoot.root h) ^ n * x) ≠ 0 := by
  let p := AdjoinRoot.modByMonicHom hh x
  have hp : p ≠ 0 := by
    intro hp0
    apply hx
    calc
      x = AdjoinRoot.mk h p := (AdjoinRoot.mk_leftInverse hh x).symm
      _ = 0 := by rw [hp0, map_zero]
  have hpd : p.natDegree < h.natDegree := remainder_degree_lt hh hd x
  let n := h.natDegree - 1 - p.natDegree
  have hn : n < h.natDegree := by dsimp [n]; omega
  have hsum : p.natDegree + n = h.natDegree - 1 := by dsimp [n]; omega
  have hprod : (X ^ n * p).natDegree < h.natDegree := by
    rw [Polynomial.natDegree_mul (pow_ne_zero n Polynomial.X_ne_zero) hp,
      Polynomial.natDegree_X_pow]
    omega
  refine ⟨n, hn, ?_⟩
  have hclass : (AdjoinRoot.root h) ^ n * x = AdjoinRoot.mk h (X ^ n * p) := by
    rw [map_mul, map_pow, AdjoinRoot.mk_X, AdjoinRoot.mk_leftInverse hh]
  rw [hclass, residue_mk_of_lt hh _ hprod, ← hsum, Polynomial.coeff_X_pow_mul]
  exact Polynomial.leadingCoeff_ne_zero.mpr hp

/-- Perfectness is obtained from actual quotient multiplication, not an added hypothesis. -/
theorem residue_separates (hh : h.Monic) (hd : 0 < h.natDegree)
    (x : AdjoinRoot h) (hx : ∀ y, residue hh (y * x) = 0) : x = 0 := by
  by_contra hn
  obtain ⟨n, _, hn⟩ := exists_detecting_monomial hh hd x hn
  exact hn (hx _)

/-- The finite residue duality map, retaining both arguments. -/
def residueDual (hh : h.Monic) :
    AdjoinRoot h →ₗ[K] (AdjoinRoot h →ₗ[K] K) where
  toFun x :=
    { toFun := fun y => residue hh (y * x)
      map_add' := by intros; simp [add_mul]
      map_smul' := by intros; simp [smul_mul_assoc] }
  map_add' := by intros; ext y; simp [mul_add]
  map_smul' := by intros; ext y; simp [mul_smul_comm]

@[simp] theorem residueDual_apply (hh : h.Monic) (x y : AdjoinRoot h) :
    residueDual hh x y = residue hh (y * x) := rfl

 theorem residueDual_injective (hh : h.Monic) (hd : 0 < h.natDegree) :
    Function.Injective (residueDual hh) := by
  intro x y hxy
  apply sub_eq_zero.mp
  apply residue_separates hh hd
  intro z
  have hz := LinearMap.congr_fun hxy z
  change residue hh (z * x) = residue hh (z * y) at hz
  simpa only [mul_sub, map_sub, hz, sub_self]

/-- The proved residue pairing as an actual linear equivalence with the dual. -/
def residueEquiv (hh : h.Monic) (hd : 0 < h.natDegree) :
    AdjoinRoot h ≃ₗ[K] (AdjoinRoot h →ₗ[K] K) := by
  letI : Module.Finite K (AdjoinRoot h) := hh.finite_adjoinRoot
  exact (residueDual hh).linearEquivOfInjective
    (residueDual_injective hh hd) (by simp)

@[simp] theorem residueEquiv_apply (hh : h.Monic) (hd : 0 < h.natDegree)
    (x y : AdjoinRoot h) :
    residueEquiv hh hd x y = residue hh (y * x) := rfl

end SplitZero.MonicResidue
