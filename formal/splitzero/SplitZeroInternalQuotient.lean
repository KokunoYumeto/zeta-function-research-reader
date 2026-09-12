import SplitZeroHomology

/-!
# Support-preserving quotients and their universal property

The quotient is assembled from genuine module quotients. Its universal property
is proved against every split-linear target, not only against fixed-support maps.
In particular it is a coequalizer of a relation inclusion and its supported-zero map.
-/

noncomputable section
namespace SplitZero.Reconstruction

universe u v w
variable {R : Type u} [CommRing R] {L : Type v} [SemilatticeSup L] [OrderBot L]

namespace LinearDiagram
variable (D : LinearDiagram R L)

theorem same_label_add (i : L) (x y : D.V i) :
    (⟨i, x⟩ : D.Total) + ⟨i, y⟩ = ⟨i, x + y⟩ := by
  apply D.total_ext (sup_idem i)
  change D.map _ (D.map _ x + D.map _ y) = x + y
  simp

theorem same_label_eq (i : L) (x y : D.V i) :
    (⟨i, x⟩ : D.Total) = ⟨i, y⟩ ↔ x = y := by
  simp only [LinearDiagram.Total.mk.injEq, heq_eq_eq, true_and]

end LinearDiagram

structure Relations (D : LinearDiagram R L) where
  fibre : ∀ i, Submodule R (D.V i)
  stable : ∀ {i j} (h : i ≤ j) {x : D.V i}, x ∈ fibre i → D.map h x ∈ fibre j

namespace Relations
variable {D : LinearDiagram R L} (B : Relations D)

def quotientDiagram : LinearDiagram R L where
  V i := D.V i ⧸ B.fibre i
  map {i j} h := (B.fibre i).mapQ (B.fibre j) (D.map h) (fun _ hx => B.stable h hx)
  map_id i := by
    apply LinearMap.ext
    intro x
    induction x using Submodule.Quotient.induction_on with
    | _ x =>
      change Submodule.Quotient.mk (D.map (le_refl i) x) = Submodule.Quotient.mk x
      rw [D.map_self]
  map_comp h h' := by
    apply LinearMap.ext
    intro x
    induction x using Submodule.Quotient.induction_on with
    | _ x =>
      change Submodule.Quotient.mk (D.map h' (D.map h x)) =
        Submodule.Quotient.mk (D.map (le_trans h h') x)
      rw [D.map_map]

def quotientMap : Hom D B.quotientDiagram where
  app i := (B.fibre i).mkQ
  naturality _ _ := rfl

theorem quotient_surjective : Function.Surjective B.quotientMap.total := by
  rintro ⟨i, x⟩
  obtain ⟨y, rfl⟩ := Submodule.Quotient.mk_surjective (B.fibre i) x
  exact ⟨⟨i, y⟩, rfl⟩

theorem quotient_same_label_iff (i : L) (x y : D.V i) :
    B.quotientMap.total ⟨i, x⟩ = B.quotientMap.total ⟨i, y⟩ ↔ x - y ∈ B.fibre i := by
  change (⟨i, (B.fibre i).mkQ x⟩ : B.quotientDiagram.Total) =
    ⟨i, (B.fibre i).mkQ y⟩ ↔ _
  rw [B.quotientDiagram.same_label_eq]
  exact Submodule.Quotient.eq (B.fibre i)

/-- An old relation is sent to its fibre zero, not a different support label. -/
theorem relation_maps_to_fibre_zero (i : L) (x : D.V i) (hx : x ∈ B.fibre i) :
    B.quotientMap.total ⟨i, x⟩ = ⟨i, 0⟩ := by
  change (⟨i, Submodule.Quotient.mk x⟩ : B.quotientDiagram.Total) = ⟨i, 0⟩
  rw [(Submodule.Quotient.mk_eq_zero _).mpr hx]

section Universal
variable {M : Type w} [AddCommMonoid M] [Module (G R) M]
variable (f : D.Total →ₗ[G R] M)
variable (hf : ∀ i (x : D.V i), x ∈ B.fibre i → f ⟨i, x⟩ = f ⟨i, 0⟩)

theorem constant_on_quotient_fibres {x y : D.Total}
    (h : B.quotientMap.total x = B.quotientMap.total y) : f x = f y := by
  rcases x with ⟨i, x⟩
  rcases y with ⟨j, y⟩
  have hij : i = j := congrArg (fun z : B.quotientDiagram.Total => z.fst) h
  subst j
  have hxy : x - y ∈ B.fibre i := (B.quotient_same_label_iff i x y).mp h
  have he : y + (x - y) = x := by abel
  calc
    f ⟨i, x⟩ = f ⟨i, y + (x - y)⟩ := by rw [he]
    _ = f ((⟨i, y⟩ : D.Total) + ⟨i, x - y⟩) := by rw [D.same_label_add]
    _ = f ⟨i, y⟩ + f ⟨i, x - y⟩ := f.map_add _ _
    _ = f ⟨i, y⟩ + f ⟨i, 0⟩ := by rw [hf i (x - y) hxy]
    _ = f ((⟨i, y⟩ : D.Total) + ⟨i, 0⟩) := (f.map_add _ _).symm
    _ = f ⟨i, y⟩ := by rw [D.same_label_add, add_zero]

/-- The descended map is constructed from the proved surjection. -/
def descend : B.quotientDiagram.Total →ₗ[G R] M where
  toFun y := f (Classical.choose (B.quotient_surjective y))
  map_add' x y := by
    let sx := Classical.choose (B.quotient_surjective x)
    let sy := Classical.choose (B.quotient_surjective y)
    have hx : B.quotientMap.total sx = x := Classical.choose_spec (B.quotient_surjective x)
    have hy : B.quotientMap.total sy = y := Classical.choose_spec (B.quotient_surjective y)
    have h := B.constant_on_quotient_fibres f hf
      (x := Classical.choose (B.quotient_surjective (x + y))) (y := sx + sy) (by
        rw [map_add, hx, hy]
        exact Classical.choose_spec (B.quotient_surjective (x + y)))
    exact h.trans (f.map_add sx sy)
  map_smul' r x := by
    let sx := Classical.choose (B.quotient_surjective x)
    have hx : B.quotientMap.total sx = x := Classical.choose_spec (B.quotient_surjective x)
    have h := B.constant_on_quotient_fibres f hf
      (x := Classical.choose (B.quotient_surjective (r • x))) (y := r • sx) (by
        rw [map_smul, hx]
        exact Classical.choose_spec (B.quotient_surjective (r • x)))
    exact h.trans (f.map_smul r sx)

theorem descend_quotient (x : D.Total) : B.descend f hf (B.quotientMap.total x) = f x :=
  B.constant_on_quotient_fibres f hf (Classical.choose_spec (B.quotient_surjective _))

/-- The universal property against arbitrary semimodule targets. -/
theorem quotient_universal : ∃! g : B.quotientDiagram.Total →ₗ[G R] M,
    g.comp B.quotientMap.total = f := by
  refine ⟨B.descend f hf, ?_, ?_⟩
  · ext x
    exact B.descend_quotient f hf x
  · intro g hg
    apply LinearMap.ext
    intro y
    obtain ⟨x, rfl⟩ := B.quotient_surjective y
    exact (congrArg (fun k : D.Total →ₗ[G R] M => k x) hg).trans
      (B.descend_quotient f hf x).symm

end Universal

/-- The diagram of relation submodules itself, with its actual transition maps. -/
def relationDiagram : LinearDiagram R L where
  V i := B.fibre i
  map h :=
    { toFun := fun x => ⟨D.map h x.val, B.stable h x.property⟩
      map_add' := fun x y => Subtype.ext (map_add (D.map h) x.val y.val)
      map_smul' := fun r x => Subtype.ext (map_smul (D.map h) r x.val) }
  map_id i := by
    ext x
    exact D.map_self i x.val
  map_comp h h' := by
    ext x
    exact D.map_map h h' x.val

def relationInclusion : Hom B.relationDiagram D where
  app i := (B.fibre i).subtype
  naturality _ _ := rfl

/-- Zero in each original fibre, as opposed to the constant globally absent map. -/
def relationZero : Hom B.relationDiagram D where
  app _ := 0
  naturality _ _ := by simp

theorem coequalizes :
    B.quotientMap.total.comp B.relationInclusion.total =
      B.quotientMap.total.comp B.relationZero.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  change (⟨i, (B.fibre i).mkQ x.val⟩ : B.quotientDiagram.Total) =
    ⟨i, (B.fibre i).mkQ 0⟩
  have hx : (B.fibre i).mkQ x.val = 0 := (Submodule.Quotient.mk_eq_zero _).mpr x.property
  rw [hx, map_zero]

/-- The full (unbundled) categorical coequalizer universal property. -/
theorem coequalizer_universal {M : Type w} [AddCommMonoid M] [Module (G R) M]
    (f : D.Total →ₗ[G R] M)
    (hf : f.comp B.relationInclusion.total = f.comp B.relationZero.total) :
    ∃! g : B.quotientDiagram.Total →ₗ[G R] M, g.comp B.quotientMap.total = f := by
  apply B.quotient_universal f
  intro i x hx
  exact congrArg (fun g : B.relationDiagram.Total →ₗ[G R] M => g ⟨i, ⟨x, hx⟩⟩) hf

end Relations
end SplitZero.Reconstruction

namespace SplitZero.InternalHomology
open SplitZero.Reconstruction SplitZero.Homology

universe u v w
variable {R : Type u} [CommRing R] {L : Type v} [SemilatticeSup L] [OrderBot L]

/-- Coherent support-indexed chain windows. These assumptions are chain-level
coherence, not conclusions about their homology. -/
structure ComplexDiagram (R : Type u) (L : Type v) [CommRing R]
    [SemilatticeSup L] [OrderBot L] where
  obj : L → Window.{u,w} R
  arrow : {i j : L} → i ≤ j → ChainMap (obj i) (obj j)
  arrow_id : ∀ i, arrow (le_refl i) = ChainMap.id (obj i)
  arrow_comp : ∀ {i j k} (h : i ≤ j) (h' : j ≤ k),
    ChainMap.comp (arrow h') (arrow h) = arrow (le_trans h h')

namespace ComplexDiagram
variable (C : ComplexDiagram R L)

def cycles : LinearDiagram R L where
  V i := (C.obj i).Cycles
  map h := (C.arrow h).cyclesMap
  map_id i := by rw [C.arrow_id]; rfl
  map_comp h h' := congrArg ChainMap.cyclesMap (C.arrow_comp h h')

def boundaries : Relations C.cycles where
  fibre i := (C.obj i).boundaries
  stable h hx := (C.arrow h).maps_boundaries hx

/-- Actual fibrewise cycle quotient, already equipped with its semimodule structure. -/
def homology : LinearDiagram R L := C.boundaries.quotientDiagram

def project : C.cycles.Total →ₗ[G R] C.homology.Total := C.boundaries.quotientMap.total

theorem project_surjective : Function.Surjective C.project := C.boundaries.quotient_surjective

theorem project_eq_iff (i : L) (x y : (C.obj i).Cycles) :
    C.project ⟨i, x⟩ = C.project ⟨i, y⟩ ↔ x - y ∈ (C.obj i).boundaries :=
  C.boundaries.quotient_same_label_iff i x y

theorem transition_is_induced {i j : L} (h : i ≤ j) :
    C.homology.map h = (C.arrow h).onHomology := rfl

/-- A retained class dies exactly when its transported representative is a boundary. -/
theorem transition_kills_iff {i j : L} (h : i ≤ j) (z : (C.obj i).Cycles) :
    C.homology.map h ((C.obj i).classOf z) = 0 ↔
      ∃ y, (C.obj j).prev y = (C.arrow h).mid z.val :=
  (C.arrow h).mapped_class_zero_iff z

/-- No source class is forgotten in advance of the chosen projection. -/
theorem retained_class_nonzero (i : L) (z : (C.obj i).Cycles)
    (hz : ¬ ∃ x, (C.obj i).prev x = z.val) :
    (⟨i, (C.obj i).classOf z⟩ : C.homology.Total) ≠ ⟨i, 0⟩ := by
  intro h
  have he := (C.homology.same_label_eq i _ _).mp h
  exact hz ((C.obj i).class_zero_iff_boundary z |>.mp he)

/-- Coequalizer property for the internal boundary quotient against every target. -/
theorem homology_universal {M : Type*} [AddCommMonoid M] [Module (G R) M]
    (f : C.cycles.Total →ₗ[G R] M)
    (hf : f.comp C.boundaries.relationInclusion.total =
      f.comp C.boundaries.relationZero.total) :
    ∃! g : C.homology.Total →ₗ[G R] M, g.comp C.project = f :=
  C.boundaries.coequalizer_universal f hf

end ComplexDiagram
end SplitZero.InternalHomology
