import SplitZeroInternalQuotient

/-!
# The typed supported-zero differential equation and internal homology

These constructions use the actual preceding, middle and following module
diagrams of a complex. The homology projection is proved to be the coequalizer
of the incoming differential into cycles and its supported-zero companion.
-/

noncomputable section
namespace SplitZero.InternalHomology.ComplexDiagram
open SplitZero.Reconstruction SplitZero.Homology

variable {R L : Type*} [CommRing R] [SemilatticeSup L] [OrderBot L]
variable (C : ComplexDiagram R L)

def previous : LinearDiagram R L where
  V i := (C.obj i).Mprev
  map h := (C.arrow h).left
  map_id i := by rw [C.arrow_id]; rfl
  map_comp h h' := congrArg ChainMap.left (C.arrow_comp h h')

def middle : LinearDiagram R L where
  V i := (C.obj i).M
  map h := (C.arrow h).mid
  map_id i := by rw [C.arrow_id]; rfl
  map_comp h h' := congrArg ChainMap.mid (C.arrow_comp h h')

def following : LinearDiagram R L where
  V i := (C.obj i).Mnext
  map h := (C.arrow h).right
  map_id i := by rw [C.arrow_id]; rfl
  map_comp h h' := congrArg ChainMap.right (C.arrow_comp h h')

def incoming : Hom C.previous C.middle where
  app i := (C.obj i).prev
  naturality h x := (congrArg (fun f => f x) (C.arrow h).prev_comm).symm

def outgoing : Hom C.middle C.following where
  app i := (C.obj i).next
  naturality h x := congrArg (fun f => f x) (C.arrow h).next_comm

/-- Zero with the correct source and target, preserving the label. -/
def supportedZero : Hom C.previous C.following where
  app _ := 0
  naturality _ _ := by simp

/-- This is d^(i+1) d^i = the fibre-zero map, not the global zero map. -/
theorem differential_square :
    C.outgoing.total.comp C.incoming.total = C.supportedZero.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  change (⟨i, (C.obj i).next ((C.obj i).prev x)⟩ : C.following.Total) = ⟨i, 0⟩
  have h := congrArg (fun f : (C.obj i).Mprev →ₗ[R] (C.obj i).Mnext => f x)
    (C.obj i).square_zero
  change (C.obj i).next ((C.obj i).prev x) = 0 at h
  rw [h]
  rfl

/-- The supported differential equation is genuinely distinct from constant absence
whenever the index contains a non-bottom support. -/
theorem supportedZero_ne_global (i : L) (hi : i ≠ ⊥) :
    C.supportedZero.total ≠ (0 : C.previous.Total →ₗ[G R] C.following.Total) := by
  intro h
  have he := congrArg (fun f : C.previous.Total →ₗ[G R] C.following.Total => f ⟨i, 0⟩) h
  exact C.following.fibre_zero_ne_global hi he

/-- Cycle condition as equality with the supported-zero action at the target. -/
theorem cycle_condition (i : L) (x : (C.obj i).M) :
    C.outgoing.total ⟨i, x⟩ = (e : G R) • C.outgoing.total ⟨i, x⟩ ↔
      (C.obj i).next x = 0 := by
  change (⟨i, (C.obj i).next x⟩ : C.following.Total) =
    (e : G R) • (⟨i, (C.obj i).next x⟩ : C.following.Total) ↔ _
  rw [C.following.supported_zero_action, C.following.same_label_eq]
  rfl

def boundary : Hom C.previous C.cycles where
  app i := (C.obj i).boundaryToCycles
  naturality h x := by
    apply Subtype.ext
    exact (congrArg (fun f => f x) (C.arrow h).prev_comm).symm

def boundaryZero : Hom C.previous C.cycles where
  app _ := 0
  naturality _ _ := by simp

theorem homology_coequalizes :
    C.project.comp C.boundary.total = C.project.comp C.boundaryZero.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  change (⟨i, (C.obj i).classOf ((C.obj i).boundaryToCycles x)⟩ : C.homology.Total) =
    ⟨i, (C.obj i).classOf 0⟩
  have h : (C.obj i).classOf ((C.obj i).boundaryToCycles x) = 0 :=
    ((C.obj i).class_zero_iff_boundary _).mpr ⟨x, rfl⟩
  rw [h, map_zero]

/-- The universal property uses the original incoming differential, not a
hypothesized already-computed homology space. -/
theorem homology_coequalizer {M : Type*} [AddCommMonoid M] [Module (G R) M]
    (f : C.cycles.Total →ₗ[G R] M)
    (hf : f.comp C.boundary.total = f.comp C.boundaryZero.total) :
    ∃! g : C.homology.Total →ₗ[G R] M, g.comp C.project = f := by
  apply C.boundaries.quotient_universal f
  intro i x hx
  obtain ⟨y, rfl⟩ := hx
  exact congrArg (fun g : C.previous.Total →ₗ[G R] M => g ⟨i, y⟩) hf

end SplitZero.InternalHomology.ComplexDiagram
