import SplitZeroFibres

/-!
# Reverse reconstruction of a linear join diagram

The coefficient ring and split scalar object are the existing SplitZero ones.
No injectivity is required of transition maps. The bottom fibre is not forced
trivial; specializing it to zero gives the absent-plus-nonbottom carrier of
the source. This generality is necessary for dual diagrams.
-/

noncomputable section
namespace SplitZero.Reconstruction

universe u v w

structure LinearDiagram (R : Type u) (L : Type v) [CommRing R]
    [SemilatticeSup L] [OrderBot L] where
  V : L → Type w
  [group : ∀ i, AddCommGroup (V i)]
  [moduleR : ∀ i, Module R (V i)]
  map : {i j : L} → i ≤ j → V i →ₗ[R] V j
  map_id : ∀ i, map (le_refl i) = LinearMap.id
  map_comp : ∀ {i j k} (h : i ≤ j) (h' : j ≤ k),
    (map h').comp (map h) = map (le_trans h h')

attribute [instance] LinearDiagram.group LinearDiagram.moduleR

variable {R : Type u} [CommRing R] {L : Type v} [SemilatticeSup L] [OrderBot L]

namespace LinearDiagram
variable (D : LinearDiagram R L)

@[simp] theorem map_self (i : L) (x : D.V i) : D.map (le_refl i) x = x := by
  rw [D.map_id]; rfl

@[simp] theorem map_map {i j k : L} (h : i ≤ j) (h' : j ≤ k) (x : D.V i) :
    D.map h' (D.map h x) = D.map (le_trans h h') x :=
  congrArg (fun f => f x) (D.map_comp h h')

/-- Dependent disjoint union; the global zero is `(bottom,0)`. -/
def Total := Σ i, D.V i

instance totalZero : Zero D.Total := ⟨⟨⊥, 0⟩⟩
instance totalAdd : Add D.Total := ⟨fun x y =>
  ⟨x.1 ⊔ y.1, D.map le_sup_left x.2 + D.map le_sup_right y.2⟩⟩

/-- Equality checked after the uniquely determined change of equal label. -/
theorem total_ext {x y : D.Total} (h : x.1 = y.1)
    (hv : D.map h.le x.2 = y.2) : x = y := by
  rcases x with ⟨i, x⟩
  rcases y with ⟨j, y⟩
  dsimp at h
  subst j
  have hx : x = y := by simpa using hv
  subst y
  rfl

instance totalAddCommMonoid : AddCommMonoid D.Total where
  add := (· + ·)
  zero := 0
  add_assoc x y z := by
    rcases x with ⟨i, x⟩
    rcases y with ⟨j, y⟩
    rcases z with ⟨k, z⟩
    apply D.total_ext (sup_assoc i j k)
    change D.map _ (D.map _ (D.map _ x + D.map _ y) + D.map _ z) =
      D.map _ x + D.map _ (D.map _ y + D.map _ z)
    simp only [map_add, map_map]
    exact add_assoc _ _ _
  zero_add x := by
    rcases x with ⟨i, x⟩
    apply D.total_ext (bot_sup_eq i)
    change D.map _ (D.map _ (0 : D.V ⊥) + D.map _ x) = x
    simp
  add_zero x := by
    rcases x with ⟨i, x⟩
    apply D.total_ext (sup_bot_eq i)
    change D.map _ (D.map _ x + D.map _ (0 : D.V ⊥)) = x
    simp
  add_comm x y := by
    rcases x with ⟨i, x⟩
    rcases y with ⟨j, y⟩
    apply D.total_ext (sup_comm i j)
    change D.map _ (D.map _ x + D.map _ y) = D.map _ y + D.map _ x
    simp only [map_add, map_map]
    exact add_comm _ _
  nsmul := nsmulRec

instance totalSMul : SMul (G R) D.Total := ⟨fun a x =>
  match a.toOption with
  | none => 0
  | some r => ⟨x.1, r • x.2⟩⟩

@[simp] theorem tau_smul (x : D.Total) : (tau : G R) • x = 0 := rfl
@[simp] theorem ofR_smul (r : R) (i : L) (x : D.V i) :
    (ofR r : G R) • (⟨i, x⟩ : D.Total) = ⟨i, r • x⟩ := rfl

instance totalModule : Module (G R) D.Total where
  one_smul x := by
    rcases x with ⟨i, x⟩
    change (⟨i, (1 : R) • x⟩ : D.Total) = ⟨i, x⟩
    rw [one_smul]
  mul_smul a b x := by
    obtain ⟨_ | a⟩ := a <;> obtain ⟨_ | b⟩ := b
    · rfl
    · rfl
    · change (0 : D.Total) = ⟨⊥, a • (0 : D.V ⊥)⟩
      rw [smul_zero]; rfl
    · rcases x with ⟨i, x⟩
      change (⟨i, (a * b) • x⟩ : D.Total) = ⟨i, a • (b • x)⟩
      rw [mul_smul]
  smul_zero a := by
    obtain ⟨_ | a⟩ := a
    · rfl
    · change (⟨⊥, a • (0 : D.V ⊥)⟩ : D.Total) = ⟨⊥, 0⟩
      rw [smul_zero]
  smul_add a x y := by
    obtain ⟨_ | a⟩ := a
    · change (0 : D.Total) = 0 + 0
      rw [zero_add]
    · rcases x with ⟨i, x⟩
      rcases y with ⟨j, y⟩
      change (⟨i ⊔ j, a • (D.map _ x + D.map _ y)⟩ : D.Total) =
        ⟨i ⊔ j, D.map _ (a • x) + D.map _ (a • y)⟩
      simp only [map_smul, smul_add]
  zero_smul x := rfl
  add_smul a b x := by
    obtain ⟨_ | a⟩ := a <;> obtain ⟨_ | b⟩ := b
    · change (0 : D.Total) = 0 + 0
      rw [zero_add]
    · change (ofR b : G R) • x = 0 + (ofR b : G R) • x
      rw [zero_add]
    · change (ofR a : G R) • x = (ofR a : G R) • x + 0
      rw [add_zero]
    · rcases x with ⟨i, x⟩
      apply D.total_ext (sup_idem i).symm
      change D.map _ ((a + b) • x) = D.map _ (a • x) + D.map _ (b • x)
      simp only [add_smul, map_add]

@[simp] theorem supported_zero_action (i : L) (x : D.V i) :
    (e : G R) • (⟨i, x⟩ : D.Total) = ⟨i, 0⟩ := by
  change (⟨i, (0 : R) • x⟩ : D.Total) = ⟨i, 0⟩
  rw [zero_smul]

theorem fibre_zero_ne_global {i : L} (h : i ≠ ⊥) : (⟨i, 0⟩ : D.Total) ≠ 0 := by
  intro he
  exact h (congrArg Sigma.fst he)

/-- An ordinary module-valued observation at a chosen terminal label. -/
def observe [OrderTop L] (x : D.Total) : D.V ⊤ := D.map le_top x.2

theorem observe_add [OrderTop L] (x y : D.Total) :
    D.observe (x + y) = D.observe x + D.observe y := by
  rcases x with ⟨i, x⟩
  rcases y with ⟨j, y⟩
  change D.map _ (D.map _ x + D.map _ y) = D.map _ x + D.map _ y
  simp

end LinearDiagram

/-- Morphisms with fixed support labels; naturality is an actual equation. -/
structure Hom (D E : LinearDiagram R L) where
  app : ∀ i, D.V i →ₗ[R] E.V i
  naturality : ∀ {i j} (h : i ≤ j) (x : D.V i),
    app j (D.map h x) = E.map h (app i x)

namespace Hom
variable {D E F : LinearDiagram R L}

def id (D : LinearDiagram R L) : Hom D D where
  app _ := LinearMap.id
  naturality _ _ := rfl

def comp (g : Hom E F) (f : Hom D E) : Hom D F where
  app i := (g.app i).comp (f.app i)
  naturality h x := by
    change g.app _ (f.app _ (D.map h x)) = F.map h (g.app _ (f.app _ x))
    rw [f.naturality, g.naturality]

/-- Reconstructed morphism, bundled as a split-scalar linear map. -/
def total (f : Hom D E) : D.Total →ₗ[G R] E.Total where
  toFun x := ⟨x.1, f.app x.1 x.2⟩
  map_add' x y := by
    rcases x with ⟨i, x⟩
    rcases y with ⟨j, y⟩
    change (⟨i ⊔ j, f.app _ (D.map _ x + D.map _ y)⟩ : E.Total) =
      ⟨i ⊔ j, E.map _ (f.app _ x) + E.map _ (f.app _ y)⟩
    rw [map_add, f.naturality, f.naturality]
  map_smul' a x := by
    obtain ⟨_ | a⟩ := a
    · change (⟨⊥, f.app _ 0⟩ : E.Total) = ⟨⊥, 0⟩
      rw [map_zero]
    · rcases x with ⟨i, x⟩
      change (⟨i, f.app _ (a • x)⟩ : E.Total) = ⟨i, a • f.app _ x⟩
      rw [map_smul]

@[simp] theorem total_apply (f : Hom D E) (i : L) (x : D.V i) :
    f.total (⟨i, x⟩ : D.Total) = ⟨i, f.app i x⟩ := rfl

theorem total_comp (g : Hom E F) (f : Hom D E) :
    (comp g f).total = g.total.comp f.total := rfl

theorem total_id (D : LinearDiagram R L) : (id D).total = LinearMap.id := rfl

end Hom
end SplitZero.Reconstruction
