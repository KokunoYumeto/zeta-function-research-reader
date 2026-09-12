import SplitZeroBoundaryControl

/-!
# Construct the local boundary-control input from a finite Krylov expansion

This file derives the one-layer escape law. It does not assume the rank-two
formula or that law in its constructor. The next vector and its row are the
actual orthogonal residual and its inner-product coordinate. The finite
projection expansion is retained, including its coefficient maps.
-/
noncomputable section
namespace SplitZero.KrylovStep
universe u v
variable {E : Type u} {H : Type v}
  [AddCommGroup E] [Module ℂ E]
  [NormedAddCommGroup H] [InnerProductSpace ℂ H]
local notation "⟪" x ", " y "⟫" => inner ℂ x y

variable (L : Submodule ℂ H) [L.HasOrthogonalProjection]

def lastResidual (f : ℕ → H) (n : ℕ) : H :=
  f (n+1) - L.starProjection (f (n+1))

theorem lastResidual_ne_zero (f : ℕ → H) (n : ℕ) (hf : f (n+1) ∉ L) :
    lastResidual L f n ≠ 0 := by
  intro he
  have hfix : L.starProjection (f (n+1)) = f (n+1) := (sub_eq_zero.mp he).symm
  exact hf (Submodule.starProjection_eq_self_iff.mp hfix)

theorem escape_of_expansion (f : ℕ → H) (n : ℕ) (D : H →ₗ[ℂ] H)
    (s : E →ₗ[ℂ] H) (coeff : ℕ → E →ₗ[ℂ] ℂ)
    (hf : ∀ j ≤ n, f j ∈ L)
    (hD : ∀ j ≤ n, D (f j) = f (j+1))
    (hexpand : ∀ x, L.starProjection (s x) =
      ∑ j ∈ Finset.range (n+1), coeff j x • f j) (x : E) :
    D (L.starProjection (s x)) - L.starProjection (D (L.starProjection (s x))) =
      coeff n x • lastResidual L f n := by
  let K : H →ₗ[ℂ] H := LinearMap.id - L.starProjection.toLinearMap
  let T : H →ₗ[ℂ] H := K.comp D
  change T (L.starProjection (s x)) = _
  rw [hexpand, map_sum, Finset.sum_range_succ]
  have hz : (∑ j ∈ Finset.range n, T (coeff j x • f j)) = 0 := by
    apply Finset.sum_eq_zero
    intro j hj
    have hjn : j < n := Finset.mem_range.mp hj
    rw [map_smul]
    change coeff j x • (D (f j) - L.starProjection (D (f j))) = 0
    rw [hD j (Nat.le_of_lt hjn),
      Submodule.starProjection_eq_self_iff.mpr (hf (j+1) (Nat.succ_le_of_lt hjn)),
      sub_self, smul_zero]
  rw [hz, zero_add, map_smul]
  change coeff n x • (D (f n) - L.starProjection (D (f n))) = _
  rw [hD n le_rfl]
  rfl

/-- No escape law is assumed: it is supplied by `escape_of_expansion`. -/
def toBoundaryData (f : ℕ → H) (n : ℕ) (D : H →ₗ[ℂ] H)
    (s : E →ₗ[ℂ] H) (A : E →ₗ[ℂ] E) (ell : E →ₗ[ℂ] ℂ)
    (coeff : ℕ → E →ₗ[ℂ] ℂ)
    (hf : ∀ j ≤ n, f j ∈ L) (hnew : f (n+1) ∉ L)
    (hD : ∀ j ≤ n, D (f j) = f (j+1))
    (hexpand : ∀ x, L.starProjection (s x) =
      ∑ j ∈ Finset.range (n+1), coeff j x • f j)
    (hsource : ∀ x, D (s x) = s (A x) + ell x • f 0)
    (hgreen : ∀ x y, ⟪D x, y⟫ + ⟪x, D y⟫ = ⟪x, y⟫) :
    BoundaryControl.Data (E := E) (H := H) where
  lower := L
  source := s
  action := A
  deriv := D
  fzero := f 0
  extensionRow := ell
  fzero_mem := hf 0 (Nat.zero_le n)
  source_boundary := hsource
  green := hgreen
  nextVector := lastResidual L f n
  next_orthogonal z hz := Submodule.starProjection_inner_eq_zero (f (n+1)) z hz
  normSquare := ‖lastResidual L f n‖^2
  next_norm := by simp [inner_self_eq_norm_sq_to_K]
  currentRow := coeff n
  nextRow := (((‖lastResidual L f n‖^2 : ℝ) : ℂ)⁻¹) •
    ((innerₛₗ ℂ (lastResidual L f n)).comp s)
  next_pair x := by
    have hu := lastResidual_ne_zero L f n hnew
    have hz : (((‖lastResidual L f n‖^2 : ℝ) : ℂ)) ≠ 0 := by
      exact_mod_cast pow_ne_zero 2 (norm_ne_zero_iff.mpr hu)
    change ⟪lastResidual L f n, s x⟫ =
      (((‖lastResidual L f n‖^2 : ℝ) : ℂ)) *
      ((((‖lastResidual L f n‖^2 : ℝ) : ℂ))⁻¹ * ⟪lastResidual L f n, s x⟫)
    rw [← mul_assoc, mul_inv_cancel₀ hz, one_mul]
  escape := escape_of_expansion L f n D s coeff hf hD hexpand
end SplitZero.KrylovStep
