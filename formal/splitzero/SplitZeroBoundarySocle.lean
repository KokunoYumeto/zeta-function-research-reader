import SplitZeroInternalQuotient

/-!
# Retained boundary socle, not ordinary specialization

For an injective f and an injective scalar v, the actual quotient by range(v*f)
has v-kernel isomorphic to M/vM, via [x] -> [f x]. The map and inverse laws are
constructed before any arithmetic or inertia observation. This specializes to
D_v/v with exponents b, or k+sum(b)-1 on an ordered tensor boundary.
-/
noncomputable section
namespace SplitZero.BoundarySocle
open SplitZero.Reconstruction
variable {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]

def scalarMap (v : R) : M →ₗ[R] M := v • LinearMap.id

def sourceRel (v : R) : Submodule R M := LinearMap.range (scalarMap (M := M) v)
def targetRel (v : R) (f : M →ₗ[R] M) : Submodule R M := LinearMap.range (v • f)

/-- The actual map from the source specialization to the retained cokernel. -/
def comparison (v : R) (f : M →ₗ[R] M) :
    (M ⧸ sourceRel (M := M) v) →ₗ[R] (M ⧸ targetRel v f) :=
  (sourceRel v).mapQ (targetRel v f) f (by
    rintro x ⟨y, rfl⟩
    refine ⟨y, ?_⟩
    change v • f y = f (v • y)
    exact (f.map_smul v y).symm)

@[simp] theorem comparison_mk (v : R) (f : M →ₗ[R] M) (x : M) :
    comparison v f ((sourceRel v).mkQ x) = (targetRel v f).mkQ (f x) := rfl

/-- The image lies in the derived-kernel term, not in the ordinary quotient fibre. -/
theorem comparison_killed (v : R) (f : M →ₗ[R] M)
    (x : M ⧸ sourceRel (M := M) v) : v • comparison v f x = 0 := by
  obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective (sourceRel v) x
  rw [comparison_mk, ← map_smul]
  exact (Submodule.Quotient.mk_eq_zero _).mpr ⟨x, rfl⟩

def socle (v : R) (f : M →ₗ[R] M) : Submodule R (M ⧸ targetRel v f) :=
  LinearMap.ker (scalarMap v)

def toSocle (v : R) (f : M →ₗ[R] M) :
    (M ⧸ sourceRel (M := M) v) →ₗ[R] socle v f :=
  (comparison v f).codRestrict (socle v f) (comparison_killed v f)

theorem comparison_injective (v : R) (f : M →ₗ[R] M)
    (hf : Function.Injective f) : Function.Injective (comparison v f) := by
  intro x y h
  obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective (sourceRel v) x
  obtain ⟨y, rfl⟩ := Submodule.Quotient.mk_surjective (sourceRel v) y
  have hm : f x - f y ∈ targetRel v f :=
    (Submodule.Quotient.eq (targetRel v f)).mp h
  obtain ⟨z, hz⟩ := hm
  have he : f (v • z) = f (x - y) := by
    rw [f.map_smul, f.map_sub]
    exact hz
  exact (Submodule.Quotient.eq (sourceRel v)).mpr ⟨z, hf he⟩

/-- Cancellation is required on the prequotient source, not imposed on torsion. -/
theorem toSocle_surjective (v : R) (f : M →ₗ[R] M)
    (hv : Function.Injective (fun x : M => v • x)) :
    Function.Surjective (toSocle v f) := by
  intro y
  obtain ⟨z, hz⟩ := Submodule.Quotient.mk_surjective (targetRel v f) y.val
  have hy : v • (targetRel v f).mkQ z = 0 := by
    rw [hz]
    exact y.property
  have hm : v • z ∈ targetRel v f := by
    apply (Submodule.Quotient.mk_eq_zero _).mp
    rw [map_smul]
    exact hy
  obtain ⟨x, hx⟩ := hm
  have hfx : f x = z := hv hx
  refine ⟨(sourceRel v).mkQ x, ?_⟩
  apply Subtype.ext
  change (targetRel v f).mkQ (f x) = y.val
  rw [hfx, hz]

def socleEquiv (v : R) (f : M →ₗ[R] M)
    (hf : Function.Injective f)
    (hv : Function.Injective (fun x : M => v • x)) :
    (M ⧸ sourceRel (M := M) v) ≃ₗ[R] socle v f :=
  LinearEquiv.ofBijective (toSocle v f)
    ⟨fun x y h => comparison_injective v f hf (congrArg Subtype.val h),
      toSocle_surjective v f hv⟩

/-- Naturality through a specified commuting source map, with no injectivity of it. -/
theorem representative_naturality (v : R) (f A B : M →ₗ[R] M)
    (h : ∀ x, B (f x) = f (A x)) (x : M) :
    (targetRel v f).mkQ (B (f x)) = comparison v f ((sourceRel v).mkQ (A x)) := by
  rw [comparison_mk, h]

/-- The source action is reduced modulo its actual v-multiples. -/
def sourceAction (v : R) (A : M →ₗ[R] M) :
    (M ⧸ sourceRel (M := M) v) →ₗ[R] (M ⧸ sourceRel (M := M) v) :=
  (sourceRel v).mapQ (sourceRel v) A (by
    rintro x ⟨y, rfl⟩
    exact ⟨A y, (A.map_smul v y).symm⟩)

/-- The lattice intertwiner makes the receiving action descend. -/
def targetAction (v : R) (f A B : M →ₗ[R] M)
    (h : ∀ x, B (f x) = f (A x)) :
    (M ⧸ targetRel v f) →ₗ[R] (M ⧸ targetRel v f) :=
  (targetRel v f).mapQ (targetRel v f) B (by
    rintro x ⟨y, rfl⟩
    refine ⟨A y, ?_⟩
    change v • f (A y) = B (v • f y)
    rw [B.map_smul, h])

/-- An equality of induced operators, retaining the full source action. -/
theorem action_square (v : R) (f A B : M →ₗ[R] M)
    (h : ∀ x, B (f x) = f (A x)) :
    (targetAction v f A B h).comp (comparison v f) =
      (comparison v f).comp (sourceAction v A) := by
  apply LinearMap.ext
  intro x
  obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective (sourceRel v) x
  change (targetRel v f).mkQ (B (f x)) = (targetRel v f).mkQ (f (A x))
  rw [h]

/-- Divide the actual lattice intertwiner by v before quotienting. -/
theorem divide_intertwiner (v : R) (f A B : M →ₗ[R] M)
    (hv : Function.Injective (fun x : M => v • x))
    (h : ∀ x, B (v • f x) = v • f (A x)) :
    ∀ x, B (f x) = f (A x) := by
  intro x
  apply hv
  rw [← B.map_smul]
  exact h x

section Diagonal
variable {ι : Type*}

def powerDiagonal (v : R) (n : ι → ℕ) : (ι → R) →ₗ[R] (ι → R) where
  toFun x i := v ^ n i * x i
  map_add' x y := by ext i; exact mul_add _ _ _
  map_smul' a x := by ext i; simp only [Pi.smul_apply, smul_eq_mul]; ring

@[simp] theorem powerDiagonal_apply (v : R) (n : ι → ℕ) (x : ι → R) (i : ι) :
    powerDiagonal v n x i = v ^ n i * x i := rfl

theorem positive_exponent_factor (v : R) (n : ι → ℕ) :
    v • powerDiagonal v n = powerDiagonal v (fun i => n i + 1) := by
  ext x i
  change v * (v ^ n i * x i) = v ^ (n i + 1) * x i
  rw [pow_succ]
  ring

theorem powerDiagonal_injective [IsDomain R] (v : R) (hv : v ≠ 0) (n : ι → ℕ) :
    Function.Injective (powerDiagonal v n) := by
  intro x y h
  funext i
  exact mul_left_cancel₀ (pow_ne_zero _ hv) (congrFun h i)

/-- The whole diagonal lattice, including every mixed tensor exponent. -/
def diagonalSocleEquiv [IsDomain R] (v : R) (hv : v ≠ 0) (n : ι → ℕ) :
    ((ι → R) ⧸ sourceRel (M := ι → R) v) ≃ₗ[R] socle v (powerDiagonal v n) :=
  socleEquiv v (powerDiagonal v n) (powerDiagonal_injective v hv n) (by
    intro x y h
    funext i
    exact mul_left_cancel₀ hv (congrFun h i))
end Diagonal

end SplitZero.BoundarySocle
