import SplitZeroReconstruction

/-!
# Support-changing morphisms of the existing reconstruction

The index map is part of the morphism. It preserves bottom and joins,
while the fibre maps satisfy the original naturality squares.
No injectivity of a transport is required.
-/

noncomputable section
namespace SplitZero.Reconstruction

universe u v w v' w'

variable {R : Type u} [CommRing R]
variable {L : Type v} {K : Type v'}
  [SemilatticeSup L] [OrderBot L] [SemilatticeSup K] [OrderBot K]

/-- A morphism with its support-index map explicitly retained. -/
structure ReindexedHom (D : LinearDiagram.{u,v,w} R L)
    (E : LinearDiagram.{u,v',w'} R K) where
  index : SupBotHom L K
  app : ∀ i, D.V i →ₗ[R] E.V (index i)
  naturality : ∀ {i j} (h : i ≤ j) (x : D.V i),
    app j (D.map h x) = E.map (index.monotone h) (app i x)

namespace ReindexedHom

variable {D : LinearDiagram.{u,v,w} R L}
  {E : LinearDiagram.{u,v',w'} R K}

/-- The total map is genuinely linear over the original split scalar. -/
def total (f : ReindexedHom D E) : D.Total →ₗ[G R] E.Total where
  toFun x := ⟨f.index x.1, f.app x.1 x.2⟩
  map_add' x y := by
    rcases x with ⟨i, x⟩
    rcases y with ⟨j, y⟩
    apply E.total_ext (f.index.map_sup i j)
    change E.map _ (f.app _ (D.map _ x + D.map _ y)) =
      E.map _ (f.app i x) + E.map _ (f.app j y)
    rw [map_add, f.naturality, f.naturality, map_add]
    simp only [LinearDiagram.map_map]
  map_smul' a x := by
    obtain ⟨_ | a⟩ := a
    · change (⟨f.index ⊥, f.app ⊥ 0⟩ : E.Total) = ⟨⊥, 0⟩
      apply E.total_ext f.index.map_bot
      simp only [map_zero]
    · rcases x with ⟨i, x⟩
      change (⟨f.index i, f.app i (a • x)⟩ : E.Total) =
        ⟨f.index i, a • f.app i x⟩
      rw [map_smul]

@[simp] theorem total_apply (f : ReindexedHom D E) (i : L) (x : D.V i) :
    f.total (⟨i, x⟩ : D.Total) = ⟨f.index i, f.app i x⟩ := rfl

/-- A killed amplitude lands at the zero of the target support fibre. -/
theorem killed_fibre (f : ReindexedHom D E) (i : L) (x : D.V i)
    (h : f.app i x = 0) :
    f.total (⟨i, x⟩ : D.Total) = ⟨f.index i, 0⟩ := by
  rw [total_apply, h]

theorem killed_not_absent (f : ReindexedHom D E) (i : L) (x : D.V i)
    (h : f.app i x = 0) (hi : f.index i ≠ ⊥) :
    f.total (⟨i, x⟩ : D.Total) ≠ 0 := by
  rw [f.killed_fibre i x h]
  exact E.fibre_zero_ne_global hi

theorem supported_zero (f : ReindexedHom D E) (i : L) (x : D.V i) :
    f.total ((e : G R) • (⟨i, x⟩ : D.Total)) =
      (⟨f.index i, 0⟩ : E.Total) := by
  rw [LinearDiagram.supported_zero_action, total_apply, map_zero]

end ReindexedHom

/-- The old fixed-index morphism embeds without changing its total map. -/
def Hom.reindexed {D E : LinearDiagram R L} (f : Hom D E) :
    ReindexedHom D E where
  index := SupBotHom.id L
  app := f.app
  naturality := f.naturality

theorem Hom.reindexed_total {D E : LinearDiagram R L} (f : Hom D E) :
    f.reindexed.total = f.total := rfl

end SplitZero.Reconstruction
