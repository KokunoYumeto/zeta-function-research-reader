import SplitZeroReconstruction

/-!
# Support-changing maps of the original reconstructed semimodules

The index map preserves bottom and binary joins. No coefficient transport
is assumed injective. The total map uses the unchanged SplitZero scalar.
-/
noncomputable section
namespace SplitZero.Reconstruction
universe u v w

structure SupportMap (L : Type v) (K : Type w)
    [SemilatticeSup L] [OrderBot L] [SemilatticeSup K] [OrderBot K] where
  toFun : L → K
  map_sup : ∀ i j, toFun (i ⊔ j) = toFun i ⊔ toFun j
  map_bot : toFun ⊥ = ⊥

namespace SupportMap
variable {L : Type v} {K : Type w} {J : Type*}
  [SemilatticeSup L] [OrderBot L] [SemilatticeSup K] [OrderBot K]
  [SemilatticeSup J] [OrderBot J]

theorem monotone (f : SupportMap L K) : Monotone f.toFun := by
  intro i j h
  apply sup_eq_right.mp
  rw [← f.map_sup, sup_eq_right.mpr h]

def id : SupportMap L L where
  toFun i := i
  map_sup _ _ := rfl
  map_bot := rfl

def comp (g : SupportMap K J) (f : SupportMap L K) : SupportMap L J where
  toFun i := g.toFun (f.toFun i)
  map_sup i j := by rw [f.map_sup, g.map_sup]
  map_bot := by rw [f.map_bot, g.map_bot]
end SupportMap

variable {R : Type u} [CommRing R]
  {L : Type v} {K : Type w} {J : Type*}
  [SemilatticeSup L] [OrderBot L] [SemilatticeSup K] [OrderBot K]
  [SemilatticeSup J] [OrderBot J]

structure HomOver (D : LinearDiagram R L) (E : LinearDiagram R K)
    (f : SupportMap L K) where
  app : ∀ i, D.V i →ₗ[R] E.V (f.toFun i)
  naturality : ∀ {i j} (h : i ≤ j) (x : D.V i),
    app j (D.map h x) = E.map (f.monotone h) (app i x)

namespace HomOver
variable {D : LinearDiagram R L} {E : LinearDiagram R K}
  {F : LinearDiagram R J} {f : SupportMap L K} {g : SupportMap K J}

def total (a : HomOver D E f) : D.Total →ₗ[G R] E.Total where
  toFun x := ⟨f.toFun x.1, a.app x.1 x.2⟩
  map_add' x y := by
    rcases x with ⟨i, x⟩
    rcases y with ⟨j, y⟩
    apply E.total_ext (f.map_sup i j)
    change E.map _ (a.app _ (D.map _ x + D.map _ y)) =
      E.map _ (a.app _ x) + E.map _ (a.app _ y)
    rw [map_add, map_add, a.naturality, a.naturality]
    simp only [LinearDiagram.map_map]
  map_smul' c x := by
    obtain ⟨_ | c⟩ := c
    · apply E.total_ext f.map_bot
      change E.map _ (a.app _ 0) = 0
      rw [map_zero, map_zero]
    · rcases x with ⟨i, x⟩
      change (⟨f.toFun i, a.app i (c • x)⟩ : E.Total) =
        ⟨f.toFun i, c • a.app i x⟩
      rw [map_smul]

@[simp] theorem total_apply (a : HomOver D E f) (i : L) (x : D.V i) :
    a.total (⟨i, x⟩ : D.Total) = ⟨f.toFun i, a.app i x⟩ := rfl

theorem total_support (a : HomOver D E f) (x : D.Total) :
    (a.total x).fst = f.toFun x.fst := rfl

theorem total_fibre_zero (a : HomOver D E f) (i : L) :
    a.total (⟨i, 0⟩ : D.Total) = ⟨f.toFun i, 0⟩ := by
  change (⟨f.toFun i, a.app i 0⟩ : E.Total) = ⟨f.toFun i, 0⟩
  rw [map_zero]

def comp (b : HomOver E F g) (a : HomOver D E f) :
    HomOver D F (g.comp f) where
  app i := (b.app (f.toFun i)).comp (a.app i)
  naturality h x := by
    change b.app _ (a.app _ (D.map h x)) = F.map _ (b.app _ (a.app _ x))
    rw [a.naturality, b.naturality]

theorem total_comp (b : HomOver E F g) (a : HomOver D E f) :
    (b.comp a).total = b.total.comp a.total := rfl

/-- An extensive support map supplies its actual transport, not a relabeling. -/
def promote (D : LinearDiagram R L) (f : SupportMap L L)
    (hf : ∀ i, i ≤ f.toFun i) : HomOver D D f where
  app i := D.map (hf i)
  naturality h x := by simp only [LinearDiagram.map_map]

theorem promote_apply (D : LinearDiagram R L) (f : SupportMap L L)
    (hf : ∀ i, i ≤ f.toFun i) (i : L) (x : D.V i) :
    (promote D f hf).total (⟨i, x⟩ : D.Total) = ⟨f.toFun i, D.map (hf i) x⟩ := rfl
end HomOver
end SplitZero.Reconstruction
