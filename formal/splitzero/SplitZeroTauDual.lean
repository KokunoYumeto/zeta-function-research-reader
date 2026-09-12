import SplitZeroInternalQuotient

/-!
# Opposite-index dual transports and quotient duality

Dualization retains precomposition, rather than merely reversing a label.
The bottom fibre of the opposite diagram is not assumed to vanish. Quotient
functionals are identified with the exact annihilator of the original relations.
-/
noncomputable section
namespace SplitZero.TauDual
open SplitZero.Reconstruction

universe u v w
variable {R : Type u} [CommRing R]

section Precomposition
variable {A B C W : Type*} [AddCommGroup A] [Module R A]
  [AddCommGroup B] [Module R B] [AddCommGroup C] [Module R C]
  [AddCommGroup W] [Module R W]

def precompose (f : A →ₗ[R] B) : (B →ₗ[R] W) →ₗ[R] (A →ₗ[R] W) where
  toFun ℓ := ℓ.comp f
  map_add' ℓ m := by ext x; rfl
  map_smul' r ℓ := by ext x; rfl

@[simp] theorem precompose_apply (f : A →ₗ[R] B) (ℓ : B →ₗ[R] W) (x : A) :
    precompose f ℓ x = ℓ (f x) := rfl

theorem precompose_comp (f : A →ₗ[R] B) (g : B →ₗ[R] C) :
    precompose (W := W) (g.comp f) = (precompose f).comp (precompose g) := by
  ext ℓ x; rfl

def evaluate : A →ₗ[R] ((A →ₗ[R] W) →ₗ[R] W) where
  toFun x :=
    { toFun := fun ℓ => ℓ x
      map_add' := fun _ _ => rfl
      map_smul' := fun _ _ => rfl }
  map_add' x y := by ext ℓ; exact ℓ.map_add x y
  map_smul' r x := by ext ℓ; exact ℓ.map_smul r x

theorem evaluate_natural (f : A →ₗ[R] B) :
    (precompose (precompose f)).comp (evaluate (W := W)) = (evaluate (W := W)).comp f := by
  ext x ℓ; rfl

variable (P : Submodule R A)

def annihilator : Submodule R (A →ₗ[R] W) where
  carrier := {ℓ | ∀ x ∈ P, ℓ x = 0}
  zero_mem' := by simp
  add_mem' := by intro f g hf hg x hx; simp [hf x hx, hg x hx]
  smul_mem' := by intro r f hf x hx; simp [hf x hx]

def quotientDualEquiv : ((A ⧸ P) →ₗ[R] W) ≃ₗ[R] annihilator (W := W) P where
  toFun ℓ := ⟨ℓ.comp P.mkQ, by
    intro x hx
    change ℓ (P.mkQ x) = 0
    rw [show P.mkQ x = 0 from (Submodule.Quotient.mk_eq_zero P).mpr hx, map_zero]⟩
  invFun ℓ := P.liftQ ℓ.val (by intro x hx; exact ℓ.property x hx)
  left_inv ℓ := by
    apply LinearMap.ext
    intro x
    obtain ⟨a, rfl⟩ := Submodule.Quotient.mk_surjective P x
    rfl
  right_inv ℓ := by apply Subtype.ext; apply LinearMap.ext; intro x; rfl
  map_add' ℓ m := by apply Subtype.ext; apply LinearMap.ext; intro x; rfl
  map_smul' r ℓ := by apply Subtype.ext; apply LinearMap.ext; intro x; rfl

@[simp] theorem quotientDualEquiv_apply (ℓ : (A ⧸ P) →ₗ[R] W) (x : A) :
    (quotientDualEquiv P ℓ).val x = ℓ (P.mkQ x) := rfl

theorem precompose_injective_of_surjective (f : A →ₗ[R] B) (hf : Function.Surjective f) :
    Function.Injective (precompose (W := W) f) := by
  intro ℓ m h
  apply LinearMap.ext
  intro b
  obtain ⟨a, rfl⟩ := hf b
  exact congrArg (fun l : A →ₗ[R] W => l a) h

end Precomposition

section Diagrams
variable {L : Type v} [Lattice L] [BoundedOrder L]
variable (D : LinearDiagram R L) (W : Type w) [AddCommGroup W] [Module R W]

abbrev opposite : LinearDiagram R Lᵒᵈ where
  V i := D.V (OrderDual.ofDual i) →ₗ[R] W
  map h := precompose (D.map h)
  map_id i := by ext ℓ x; simp [precompose]
  map_comp h h' := by ext ℓ x; simp [precompose, LinearMap.comp_apply]

@[simp] theorem opposite_map_apply {i j : Lᵒᵈ} (h : i ≤ j)
    (ℓ : (opposite D W).V i) (x : D.V (OrderDual.ofDual j)) :
    (opposite D W).map h ℓ x = ℓ (D.map h x) := rfl

def doubleDual : Hom D (opposite (opposite D W) W) where
  app i := evaluate
  naturality h x := by ext ℓ; rfl

end Diagrams

section TwistedAction
variable {V W : Type*} [AddCommGroup V] [Module R V]
  [AddCommGroup W] [Module R W]

def twistedAction (a : R) (U : V ≃ₗ[R] V) : (V →ₗ[R] W) →ₗ[R] (V →ₗ[R] W) :=
  a • precompose U.symm.toLinearMap

@[simp] theorem twistedAction_apply (a : R) (U : V ≃ₗ[R] V)
    (ℓ : V →ₗ[R] W) (x : V) : twistedAction a U ℓ x = a • ℓ (U.symm x) := rfl

theorem twisted_evaluation (a : R) (U : V ≃ₗ[R] V) (ℓ : V →ₗ[R] W) (x : V) :
    twistedAction a U ℓ (U x) = a • ℓ x := by simp

theorem twisted_preserves_annihilator (P : Submodule R V) (a : R) (U : V ≃ₗ[R] V)
    (hU : ∀ x ∈ P, U.symm x ∈ P) (ℓ : annihilator (W := W) P) :
    twistedAction a U ℓ.val ∈ annihilator (W := W) P := by
  intro x hx
  change a • ℓ.val (U.symm x) = 0
  rw [ℓ.property _ (hU x hx), smul_zero]

end TwistedAction
end SplitZero.TauDual
