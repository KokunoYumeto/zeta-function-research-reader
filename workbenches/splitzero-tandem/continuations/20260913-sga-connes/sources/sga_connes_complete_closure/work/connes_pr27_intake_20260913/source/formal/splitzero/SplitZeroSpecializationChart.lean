import Mathlib

/-!
An explicit local presentation of the effective-divisor modification.
The original infinity parameter is Polynomial.X. The residue map is constant
coefficient, not a substitution of external absence for a represented vector.
These are local algebra and fibre calculations, not a sheaf-cohomology API.
-/
noncomputable section
namespace SplitZero.SpecializationChart
open Polynomial
variable {K : Type*} [Field K] {ι σ : Type*}

/-- The actual local lattice inclusion, in the specified two summands. -/
def localMap : ((ι → K[X]) × (σ → K[X])) →ₗ[K[X]] ((ι → K[X]) × (σ → K[X])) where
  toFun v := (v.1, fun a => X * v.2 a)
  map_add' v w := by ext <;> simp [mul_add]
  map_smul' c v := by ext <;> simp [mul_left_comm]

/-- The boundary has residue-field coefficients. -/
def boundary : ((ι → K[X]) × (σ → K[X])) →ₗ[K] (σ → K) where
  toFun v := fun a => (v.2 a).coeff 0
  map_add' v w := by ext; simp
  map_smul' c v := by ext; simp

theorem local_injective : Function.Injective (localMap (K := K) (ι := ι) (σ := σ)) := by
  rintro ⟨a,b⟩ ⟨c,d⟩ h
  change (a, fun i => X * b i) = (c, fun i => X * d i) at h
  obtain ⟨ha,hb⟩ := Prod.mk.inj h
  apply Prod.ext ha
  funext i
  have hi := congrFun hb i
  exact mul_left_cancel₀ (Polynomial.X_ne_zero) hi

/-- Exactness uses the actual polynomial division by the local equation. -/
theorem local_exact (v : (ι → K[X]) × (σ → K[X])) :
    boundary v = 0 ↔ ∃ u, localMap u = v := by
  constructor
  · intro h
    refine ⟨(v.1, fun a => (v.2 a).divX), ?_⟩
    change (v.1, fun a => X * (v.2 a).divX) = v
    apply Prod.ext
    · rfl
    · funext a
      have ha : (v.2 a).coeff 0 = 0 := congrFun h a
      change X * (v.2 a).divX = v.2 a
      simpa only [ha, Polynomial.C_0, add_zero] using Polynomial.X_mul_divX_add (v.2 a)
  · rintro ⟨u,rfl⟩
    ext a
    simp [boundary, localMap]

theorem boundary_surjective : Function.Surjective (boundary (K := K) (ι := ι) (σ := σ)) := by
  intro v
  refine ⟨(0, fun a => Polynomial.C (v a)), ?_⟩
  ext a
  simp [boundary]

/-- Specialization retains both full fibre summands. -/
def fibreMap : ((ι → K) × (σ → K)) →ₗ[K] ((ι → K) × (σ → K)) where
  toFun v := (v.1,0)
  map_add' _ _ := by ext <;> simp
  map_smul' _ _ := by ext <;> simp

def residue (v : (ι → K[X]) × (σ → K[X])) : (ι → K) × (σ → K) :=
  (fun a => (v.1 a).coeff 0, fun a => (v.2 a).coeff 0)

theorem specialization_square (v : (ι → K[X]) × (σ → K[X])) :
    residue (localMap v) = fibreMap (residue v) := by
  ext <;> simp [residue, localMap, fibreMap]

/-- The modified summand is the degree-minus-one kernel. -/
theorem fibre_kernel (v : (ι → K) × (σ → K)) :
    fibreMap v = 0 ↔ v.1 = 0 := by
  simp [fibreMap, Prod.ext_iff]

/-- Second projection gives the degree-zero cokernel. -/
theorem fibre_exact (v : (ι → K) × (σ → K)) :
    v.2 = 0 ↔ ∃ u, fibreMap u = v := by
  constructor
  · intro h
    refine ⟨v, ?_⟩
    change (v.1,0) = v
    exact Prod.ext rfl h.symm
  · rintro ⟨u,h⟩
    change (u.1,0) = v at h
    exact (congrArg Prod.snd h).symm

section Projector
variable {E : Type*} [AddCommGroup E] [Module K E]

def chart (P : Module.End K E) (w : K) : Module.End K E := P + w • (1-P)

theorem chart_mul (P : Module.End K E) (hP : P*P=P) (w v : K) :
    chart P w * chart P v = chart P (w*v) := by
  have h01 : P*(1-P)=0 := by rw [mul_sub, mul_one, hP, sub_self]
  have h10 : (1-P)*P=0 := by rw [sub_mul, one_mul, hP, sub_self]
  have h11 : (1-P)*(1-P)=1-P := by noncomm_ring [hP]
  simp only [chart, add_mul, mul_add, smul_mul_assoc, mul_smul_comm,
    hP, h01, h10, h11, smul_zero, zero_add, add_zero, smul_smul]
  rw [mul_comm v w]

@[simp] theorem chart_zero (P : Module.End K E) : chart P 0=P := by simp [chart]
@[simp] theorem chart_one (P : Module.End K E) : chart P 1=1 := by simp [chart]

theorem chart_inverse (P : Module.End K E) (hP : P*P=P) (w : K) (hw : w≠0) :
    chart P w * chart P w⁻¹ = 1 ∧ chart P w⁻¹ * chart P w = 1 := by
  constructor <;> rw [chart_mul P hP] <;> simp [hw]

/-- All four action blocks remain; no equivariance is presumed. -/
theorem transported_action (P A : Module.End K E) (w : K) (hw : w≠0) :
    chart P w⁻¹ * A * chart P w =
      P*A*P + w • (P*A*(1-P)) + w⁻¹ • ((1-P)*A*P) + (1-P)*A*(1-P) := by
  simp only [chart, add_mul, mul_add, smul_mul_assoc, mul_smul_comm,
    smul_add, smul_smul]
  rw [mul_inv_cancel₀ hw, one_smul]
  abel

/-- For a projector, the polar coefficient vanishes exactly when its image is invariant. -/
theorem pole_iff_invariant (P A : Module.End K E) (_hP : P*P=P) :
    (1-P)*A*P=0 ↔ ∀ x, P (A (P x)) = A (P x) := by
  constructor
  · intro h x
    have hx := LinearMap.congr_fun h x
    change A (P x) - P (A (P x)) = 0 at hx
    exact (sub_eq_zero.mp hx).symm
  · intro h
    ext x
    change A (P x) - P (A (P x)) = 0
    rw [h x, sub_self]
end Projector
end SplitZero.SpecializationChart
