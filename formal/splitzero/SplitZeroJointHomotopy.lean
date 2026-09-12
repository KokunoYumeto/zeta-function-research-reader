import SplitZeroSupportChange
import SplitZeroTauHomotopy

/-!
# Every classified homotopy on the original four-mask chart

Bottom fibres are genuinely zero. Single-leg fibres contain exactly one
coordinate. The support-changing map sends active inputs to the joint face.
The coefficients and scalar action are those of the existing reconstruction.
-/

noncomputable section
namespace SplitZero.JointHomotopy
open SplitZero.Reconstruction

universe u
variable {R V B : Type u} [CommRing R]
  [AddCommGroup V] [Module R V] [AddCommGroup B] [Module R B]

abbrev Mask := Set Bool

def syncIndex : SupBotHom Mask Mask := by
  classical
  exact
    { toFun := fun A => if A = ∅ then ∅ else Set.univ
      map_bot' := by simp
      map_sup' := by
        intro A C
        by_cases ha : A = ∅ <;> by_cases hc : C = ∅ <;> simp [ha, hc] }

theorem le_sync (A : Mask) : A ≤ syncIndex A := by
  classical
  change A ⊆ (if A = ∅ then ∅ else Set.univ)
  split_ifs with h
  · exact le_of_eq h
  · exact Set.subset_univ A

def activeFibre (A : Mask) : Submodule R B where
  carrier := {b | A = ∅ → b = 0}
  zero_mem' _ := rfl
  add_mem' hx hy h := by rw [hx h, hy h, add_zero]
  smul_mem' a b hb h := by rw [hb h, smul_zero]

def active_le {A C : Mask} (h : A ≤ C) : activeFibre (R := R) (B := B) A ≤ activeFibre C := by
  intro b hb hc
  apply hb
  apply le_antisymm
  · simpa [hc] using h
  · exact bot_le

def activeDiagram : LinearDiagram R Mask where
  V A := activeFibre (R := R) (B := B) A
  map h := Submodule.inclusion (active_le h)
  map_id _ := by
    apply LinearMap.ext
    intro x
    apply Subtype.ext
    rfl
  map_comp _ _ := by
    apply LinearMap.ext
    intro x
    apply Subtype.ext
    rfl

def legFibre (A : Mask) : Submodule R (V × V) where
  carrier := {v | (false ∉ A → v.1 = 0) ∧ (true ∉ A → v.2 = 0)}
  zero_mem' := ⟨fun _ => rfl, fun _ => rfl⟩
  add_mem' hx hy := ⟨fun h => by
    change _ + _ = 0; rw [hx.1 h, hy.1 h, add_zero], fun h => by
    change _ + _ = 0; rw [hx.2 h, hy.2 h, add_zero]⟩
  smul_mem' a x hx := ⟨fun h => by
    change a • x.1 = 0; rw [hx.1 h, smul_zero], fun h => by
    change a • x.2 = 0; rw [hx.2 h, smul_zero]⟩

def leg_le {A C : Mask} (h : A ≤ C) :
    legFibre (R := R) (V := V) A ≤ legFibre C := by
  intro v hv
  exact ⟨fun hn => hv.1 (fun hm => hn (h hm)),
    fun hn => hv.2 (fun hm => hn (h hm))⟩

def legDiagram : LinearDiagram R Mask where
  V A := legFibre (R := R) (V := V) A
  map h := Submodule.inclusion (leg_le h)
  map_id _ := by
    apply LinearMap.ext
    intro x
    apply Subtype.ext
    rfl
  map_comp _ _ := by
    apply LinearMap.ext
    intro x
    apply Subtype.ext
    rfl

variable (theta : V →ₗ[R] B) (F : V ≃ₗ[R] V)

def differential :
    Hom (legDiagram (R := R) (V := V)) (activeDiagram (R := R) (B := B)) where
  app A :=
    { toFun p := ⟨SplitZero.TauHomotopy.delta theta F p.val, by
        intro hA
        have h1 : p.val.1 = 0 := p.property.1 (by simp [hA])
        have h2 : p.val.2 = 0 := p.property.2 (by simp [hA])
        change theta (p.val.1-F p.val.2) = 0
        rw [h1, h2, map_zero, sub_zero, map_zero]⟩
      map_add' x y := Subtype.ext ((SplitZero.TauHomotopy.delta theta F).map_add x.val y.val)
      map_smul' a x := Subtype.ext ((SplitZero.TauHomotopy.delta theta F).map_smul a x.val) }
  naturality _ _ := rfl

def syncLeg :
    ReindexedHom (legDiagram (R := R) (V := V)) (legDiagram (R := R) (V := V)) where
  index := syncIndex
  app A := Submodule.inclusion (leg_le (le_sync A))
  naturality _ _ := rfl

def syncActive :
    ReindexedHom (activeDiagram (R := R) (B := B)) (activeDiagram (R := R) (B := B)) where
  index := syncIndex
  app A := Submodule.inclusion (active_le (le_sync A))
  naturality _ _ := rfl

def activeEnd (T : B →ₗ[R] B) :
    Hom (activeDiagram (R := R) (B := B)) (activeDiagram (R := R) (B := B)) where
  app A :=
    { toFun b := ⟨T b.val, fun h => by rw [b.property h, map_zero]⟩
      map_add' x y := Subtype.ext (T.map_add x.val y.val)
      map_smul' a x := Subtype.ext (T.map_smul a x.val) }
  naturality _ _ := rfl

def legZero : Hom (legDiagram (R := R) (V := V)) (legDiagram (R := R) (V := V)) where
  app _ := 0
  naturality _ _ := by exact (map_zero _).symm

/-- Construct the actual support-changing lift, not a new scalar implementation. -/
def lift (H : B →ₗ[R] (V × V)) :
    ReindexedHom (activeDiagram (R := R) (B := B)) (legDiagram (R := R) (V := V)) where
  index := syncIndex
  app A :=
    { toFun b := ⟨H b.val, by
        classical
        by_cases hA : A = ∅
        · have hb : b.val = 0 := b.property hA
          simp [legFibre, syncIndex, hA, hb, map_zero]
        · simp [legFibre, syncIndex, hA]⟩
      map_add' x y := Subtype.ext (H.map_add x.val y.val)
      map_smul' a x := Subtype.ext (H.map_smul a x.val) }
  naturality _ _ := rfl

/-- Degree-one homotopy equation on the original reconstructed objects. -/
theorem lifted_boundary (kappa : B →ₗ[R] V)
    (H : SplitZero.TauHomotopy.Homotopies theta F kappa) :
    (differential theta F).total.comp (lift H.val).total =
      (syncActive (R := R) (B := B)).total.comp (activeEnd (theta.comp kappa)).total := by
  apply LinearMap.ext
  rintro ⟨A, b⟩
  apply congrArg (fun x : activeFibre (R := R) (B := B) (syncIndex A) =>
    (⟨syncIndex A, x⟩ : (activeDiagram (R := R) (B := B)).Total))
  apply Subtype.ext
  exact LinearMap.congr_fun H.property.1 b.val

/-- Degree-zero equation: its zero is the joint fibre zero, not global absence. -/
theorem lifted_cycle (kappa : B →ₗ[R] V)
    (H : SplitZero.TauHomotopy.Homotopies theta F kappa) :
    (lift H.val).total.comp (differential theta F).total =
      (syncLeg (R := R) (V := V)).total.comp (legZero (R := R) (V := V)).total := by
  apply LinearMap.ext
  rintro ⟨A, v⟩
  apply congrArg (fun x : legFibre (R := R) (V := V) (syncIndex A) =>
    (⟨syncIndex A, x⟩ : (legDiagram (R := R) (V := V)).Total))
  apply Subtype.ext
  exact H.property.2 (v.val.1-F v.val.2)

/-- Every parameter in the existing full classification receives that lift. -/
def classifiedLift (hTheta : Function.Injective theta) (kappa : B →ₗ[R] V)
    (hk : ∀ v, kappa (theta v) = 0)
    (alpha : (B ⧸ LinearMap.range theta) →ₗ[R] V) :
    ReindexedHom (activeDiagram (R := R) (B := B)) (legDiagram (R := R) (V := V)) :=
  lift ((SplitZero.TauHomotopy.cochainHomotopyEquiv theta F hTheta kappa hk) alpha).val

end SplitZero.JointHomotopy
