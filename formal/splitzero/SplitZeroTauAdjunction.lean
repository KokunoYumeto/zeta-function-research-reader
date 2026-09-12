import SplitZeroTauChart
import SplitZeroTauDual

/-!
# The computed tau-chart right-adjoint complex

The Hom equivalences, the signs, the two cofree terms, and their injective
lifting properties are proved, not assumed. Algebraic quotient functionals
are identified with degree minus one of the displayed Hom complex. This file
does not identify algebraic functionals with a continuous Schwartz dual.
-/
noncomputable section
namespace SplitZero.TauChart
open Diagram SplitZero.TauDual
universe u
variable {R : Type u} [CommRing R]

abbrev cofreeEta (W : ModuleCat.{u} R) : Diagram R where
  plus := W
  minus := W
  eta := W
  sigma := zeroObj
  left := LinearMap.id
  right := LinearMap.id
  tail := 0

abbrev cofreePair (W : ModuleCat.{u} R) : Diagram R where
  plus := W
  minus := W
  eta := zeroObj
  sigma := zeroObj
  left := 0
  right := 0
  tail := 0

abbrev simpleEta (W : ModuleCat.{u} R) : Diagram R where
  plus := zeroObj
  minus := zeroObj
  eta := W
  sigma := zeroObj
  left := 0
  right := 0
  tail := 0

def homEtaEquiv (F : Diagram R) (W : ModuleCat.{u} R) :
    Diagram.Hom F (cofreeEta W) ≃ₗ[R] (F.eta →ₗ[R] W) where
  toFun f := f.eta
  invFun ℓ := Diagram.mkHom F (cofreeEta W) (ℓ.comp F.left) (ℓ.comp F.right) ℓ 0
    (fun _ => rfl) (fun _ => rfl) (fun _ => rfl)
  left_inv f := by
    apply Diagram.Hom.ext
    · apply LinearMap.ext; intro x; exact (f.left_naturality x).symm
    · apply LinearMap.ext; intro x; exact (f.right_naturality x).symm
    · rfl
    · exact Subsingleton.elim _ _
  right_inv ℓ := rfl
  map_add' f g := rfl
  map_smul' a f := rfl

def homPairEquiv (F : Diagram R) (W : ModuleCat.{u} R) :
    Diagram.Hom F (cofreePair W) ≃ₗ[R] ((F.plus →ₗ[R] W) × (F.minus →ₗ[R] W)) where
  toFun f := (f.plus, f.minus)
  invFun f := Diagram.mkHom F (cofreePair W) f.1 f.2 0 0
    (fun _ => rfl) (fun _ => rfl) (fun _ => rfl)
  left_inv f := by
    apply Diagram.Hom.ext
    · rfl
    · rfl
    · exact Subsingleton.elim _ _
    · exact Subsingleton.elim _ _
  right_inv f := rfl
  map_add' f g := rfl
  map_smul' a f := rfl

/-- K_tau(W) is this arrow in degrees -1,0. -/
def adjointDifferential (W : ModuleCat.{u} R) :
    Diagram.Hom (cofreeEta W) (cofreePair W) :=
  Diagram.mkHom _ _ LinearMap.id (-LinearMap.id) 0 0
    (fun _ => rfl) (fun _ => rfl) (fun _ => rfl)

def simpleInclusion (W : ModuleCat.{u} R) :
    Diagram.Hom (simpleEta W) (cofreeEta W) :=
  Diagram.mkHom _ _ 0 0 LinearMap.id 0
    (fun _ => rfl) (fun _ => rfl) (fun _ => rfl)

theorem simpleInclusion_comp (W : ModuleCat.{u} R) :
    Diagram.compose _ _ _ (simpleInclusion W) (adjointDifferential W) = 0 := by
  apply Diagram.Hom.ext <;> apply LinearMap.ext <;> intro x
  · rfl
  · change -(0 : W) = 0; exact neg_zero
  · rfl
  · rfl

def postcompose {F G H : Diagram R} (g : Diagram.Hom G H) :
    Diagram.Hom F G →ₗ[R] Diagram.Hom F H where
  toFun f := Diagram.compose F G H f g
  map_add' f h := by
    apply Diagram.Hom.ext <;> apply LinearMap.ext <;> intro x
    · exact g.plus.map_add _ _
    · exact g.minus.map_add _ _
    · exact g.eta.map_add _ _
    · exact g.sigma.map_add _ _
  map_smul' a f := by
    apply Diagram.Hom.ext <;> apply LinearMap.ext <;> intro x
    · exact g.plus.map_smul a _
    · exact g.minus.map_smul a _
    · exact g.eta.map_smul a _
    · exact g.sigma.map_smul a _

def dualDifferential (F : Diagram R) (W : ModuleCat.{u} R) :
    (F.eta →ₗ[R] W) →ₗ[R] ((F.plus →ₗ[R] W) × (F.minus →ₗ[R] W)) where
  toFun ℓ := (ℓ.comp F.left, -(ℓ.comp F.right))
  map_add' f g := by ext x <;> simp <;> abel
  map_smul' a f := by ext x <;> simp

/-- The two Hom descriptions have exactly the same signed differential. -/
theorem adjunction_square (F : Diagram R) (W : ModuleCat.{u} R) :
    (homPairEquiv F W).toLinearMap.comp (postcompose (adjointDifferential W)) =
      (dualDifferential F W).comp (homEtaEquiv F W).toLinearMap := by
  apply LinearMap.ext
  intro f
  apply Prod.ext
  · apply LinearMap.ext; intro x
    exact f.left_naturality x
  · apply LinearMap.ext; intro x
    exact congrArg Neg.neg (f.right_naturality x)

def homProductEquiv (A B W : ModuleCat.{u} R) :
    ((A × B) →ₗ[R] W) ≃ₗ[R] ((A →ₗ[R] W) × (B →ₗ[R] W)) where
  toFun ℓ := (ℓ.comp (LinearMap.inl R A B), ℓ.comp (LinearMap.inr R A B))
  invFun f := f.1.coprod f.2
  left_inv ℓ := by
    apply LinearMap.ext
    rintro ⟨x,y⟩
    change ℓ (x,0) + ℓ (0,y) = ℓ (x,y)
    rw [← map_add]
    congr 1
    simp
  right_inv f := by
    apply Prod.ext <;> apply LinearMap.ext <;> intro x <;> simp
  map_add' f g := rfl
  map_smul' a f := rfl

theorem duality_square (F : Diagram R) (W : ModuleCat.{u} R) :
    (homProductEquiv F.plus F.minus W).toLinearMap.comp (precompose F.differential) =
      dualDifferential F W := by
  apply LinearMap.ext
  intro ℓ
  apply Prod.ext <;> apply LinearMap.ext <;> intro x
  · change ℓ (F.left x - F.right 0) = ℓ (F.left x)
    rw [map_zero, sub_zero]
  · change ℓ (F.left 0 - F.right x) = -ℓ (F.right x)
    rw [map_zero, zero_sub, map_neg]

theorem dualDifferential_zero_iff (F : Diagram R) (W : ModuleCat.{u} R)
    (ℓ : F.eta →ₗ[R] W) : dualDifferential F W ℓ = 0 ↔
      ∀ z ∈ LinearMap.range F.differential, ℓ z = 0 := by
  constructor
  · intro h z hz
    obtain ⟨⟨x,y⟩, rfl⟩ := hz
    have hp := congrArg (fun p : (F.plus →ₗ[R] W) × (F.minus →ₗ[R] W) => p.1 x) h
    have hm := congrArg (fun p : (F.plus →ₗ[R] W) × (F.minus →ₗ[R] W) => p.2 y) h
    change ℓ (F.left x) = 0 at hp
    change -ℓ (F.right y) = 0 at hm
    rw [neg_eq_zero] at hm
    change ℓ (F.left x - F.right y) = 0
    rw [map_sub, hp, hm, sub_self]
  · intro h
    apply Prod.ext <;> apply LinearMap.ext <;> intro x
    · change ℓ (F.left x) = 0
      have hh := h (F.differential (x,0)) ⟨(x,0),rfl⟩
      simpa using hh
    · change -ℓ (F.right x) = 0
      have hh := h (F.differential (0,x)) ⟨(0,x),rfl⟩
      have hz : ℓ (F.right x) = 0 := by simpa using hh
      rw [hz, neg_zero]

def annihilatorKernelEquiv (F : Diagram R) (W : ModuleCat.{u} R) :
    annihilator (W := W) (LinearMap.range F.differential) ≃ₗ[R]
      LinearMap.ker (dualDifferential F W) where
  toFun ℓ := ⟨ℓ.val, (dualDifferential_zero_iff F W ℓ.val).mpr ℓ.property⟩
  invFun ℓ := ⟨ℓ.val, (dualDifferential_zero_iff F W ℓ.val).mp ℓ.property⟩
  left_inv _ := rfl
  right_inv _ := rfl
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

def degreeOneDualEquiv (F : Diagram R) (W : ModuleCat.{u} R) :
    ((F.eta ⧸ LinearMap.range F.differential) →ₗ[R] W) ≃ₗ[R]
      LinearMap.ker (dualDifferential F W) :=
  (quotientDualEquiv (LinearMap.range F.differential)).trans (annihilatorKernelEquiv F W)

@[simp] theorem degreeOneDualEquiv_apply (F : Diagram R) (W : ModuleCat.{u} R)
    (ℓ : (F.eta ⧸ LinearMap.range F.differential) →ₗ[R] W) (z : F.eta) :
    (degreeOneDualEquiv F W ℓ).val z = ℓ ((LinearMap.range F.differential).mkQ z) := rfl

/-- Cofree eta terms extend maps across every pointwise monomorphism over a field. -/
theorem cofreeEta_injective {k : Type u} [Field k] {F G : Diagram k}
    (W : ModuleCat.{u} k) (f : Diagram.Hom F G) (hf : Function.Injective f.eta)
    (g : Diagram.Hom F (cofreeEta W)) :
    ∃ h : Diagram.Hom G (cofreeEta W), Diagram.compose _ _ _ f h = g := by
  obtain ⟨s, hs⟩ := f.eta.exists_leftInverse_of_injective (LinearMap.ker_eq_bot.mpr hf)
  refine ⟨(homEtaEquiv G W).symm (g.eta.comp s), ?_⟩
  apply (homEtaEquiv F W).injective
  apply LinearMap.ext
  intro x
  change g.eta (s (f.eta x)) = g.eta x
  exact congrArg g.eta (LinearMap.congr_fun hs x)

/-- The degree-zero cofree pair is injective by the two separate extensions. -/
theorem cofreePair_injective {k : Type u} [Field k] {F G : Diagram k}
    (W : ModuleCat.{u} k) (f : Diagram.Hom F G)
    (hp : Function.Injective f.plus) (hm : Function.Injective f.minus)
    (g : Diagram.Hom F (cofreePair W)) :
    ∃ h : Diagram.Hom G (cofreePair W), Diagram.compose _ _ _ f h = g := by
  obtain ⟨sp, hsp⟩ := f.plus.exists_leftInverse_of_injective (LinearMap.ker_eq_bot.mpr hp)
  obtain ⟨sm, hsm⟩ := f.minus.exists_leftInverse_of_injective (LinearMap.ker_eq_bot.mpr hm)
  refine ⟨(homPairEquiv G W).symm (g.plus.comp sp, g.minus.comp sm), ?_⟩
  apply (homPairEquiv F W).injective
  apply Prod.ext
  · apply LinearMap.ext; intro x
    exact congrArg g.plus (LinearMap.congr_fun hsp x)
  · apply LinearMap.ext; intro x
    exact congrArg g.minus (LinearMap.congr_fun hsm x)

end SplitZero.TauChart
