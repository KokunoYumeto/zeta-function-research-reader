import SplitZeroResidueConstituent

/-!
# Residue detection inside the original supported source quotient

Use an original relation family on an original linear diagram. A finite packet
section is injected into that quotient using the actual jet identity, not by
identifying all jet-kernel vectors with theta boundaries. The residue response
is observed through the same section and the same quotient.
-/
noncomputable section
namespace SplitZero.MonicResidue
open Polynomial SplitZero.Reconstruction

universe u v
variable {K : Type u} [Field K] {h : K[X]}
  {L : Type v} [SemilatticeSup L] [OrderBot L]
  {D : LinearDiagram K L} (B : Relations D) (i : L)
  (J : D.V i →ₗ[K] AdjoinRoot h) (r : AdjoinRoot h →ₗ[K] D.V i)
  (hr : ∀ x, J (r x) = x)
  (hB : ∀ x, x ∈ B.fibre i → J x = 0)

/-- The actual section followed by the original internal quotient. -/
def sourcePacketClass (x : AdjoinRoot h) : B.quotientDiagram.Total :=
  B.quotientMap.total ⟨i, r x⟩

include hr hB in
/-- Equality is checked in the original relation quotient, before further observations. -/
theorem sourcePacketClass_eq_iff (x y : AdjoinRoot h) :
    sourcePacketClass B i r x = sourcePacketClass B i r y ↔ x = y := by
  constructor
  · intro he
    have hq : (B.fibre i).mkQ (r x) = (B.fibre i).mkQ (r y) :=
      (B.quotientDiagram.same_label_eq i _ _).mp he
    have hm := (Submodule.Quotient.eq (B.fibre i)).mp hq
    have hz := hB (r x - r y) hm
    rw [map_sub, hr, hr] at hz
    exact sub_eq_zero.mp hz
  · rintro rfl
    rfl

/-- A represented zero at nonbottom support is not global absence. -/
theorem sourcePacketClass_not_absent (x : AdjoinRoot h) (hi : i ≠ ⊥) :
    sourcePacketClass B i r x ≠ 0 := by
  intro hz
  exact hi (congrArg (fun y : B.quotientDiagram.Total => y.fst) hz)

/-- Literal finite-rank source operation; no extension to a Hilbert completion is assumed. -/
def sourceResidueOperator (hh : h.Monic) : D.V i →ₗ[K] D.V i :=
  r.comp ((SplitZero.Integration.residueInsertion 1 (residue hh)).comp J)

include hr in
theorem sourceResidueOperator_section (hh : h.Monic) (x : AdjoinRoot h) :
    sourceResidueOperator i J r hh (r x) =
      r (residue hh x • (1 : AdjoinRoot h)) := by
  change r (residue hh (J (r x)) • (1 : AdjoinRoot h)) = _
  rw [hr]

include hB in
/-- The original source boundary is still killed by the lifted operation. -/
theorem sourceResidueOperator_boundary (hh : h.Monic) (x : D.V i)
    (hx : x ∈ B.fibre i) : sourceResidueOperator i J r hh x = 0 := by
  change r (residue hh (J x) • (1 : AdjoinRoot h)) = 0
  rw [hB x hx, map_zero, zero_smul, map_zero]

include hr hB in
/-- Every nonzero packet class has a nonzero original supported residue response
    after an explicitly bounded power of the actual multiplication generator. -/
theorem source_residue_detects (hh : h.Monic) (hd : 0 < h.natDegree)
    (x : AdjoinRoot h) (hx : x ≠ 0) :
    ∃ n : ℕ, n < h.natDegree ∧
      B.quotientMap.total
        ⟨i, sourceResidueOperator i J r hh (r ((AdjoinRoot.root h)^n * x))⟩ ≠
          (⟨i, 0⟩ : B.quotientDiagram.Total) := by
  obtain ⟨n, hn, hdet⟩ := exists_detecting_monomial hh hd x hx
  refine ⟨n, hn, ?_⟩
  apply SplitZero.Integration.source_class_nonzero B i
  intro hb
  have hz := hB _ hb
  rw [sourceResidueOperator_section i J r hr, hr] at hz
  have hnontriv : (1 : AdjoinRoot h) ≠ 0 := by
    intro h1
    have hzero : (AdjoinRoot.root h)^n * x = 0 := by
      calc
        _ = 1 * ((AdjoinRoot.root h)^n * x) := (one_mul _).symm
        _ = 0 := by rw [h1, zero_mul]
    exact hdet (by rw [hzero, map_zero])
  exact hdet ((smul_eq_zero.mp hz).resolve_right hnontriv)

include hr in
/-- The source observation of the constituent response is the proved transverse map. -/
theorem source_transverse_square (hh : h.Monic)
    (F : Submodule K (AdjoinRoot h)) (x : F) :
    F.mkQ (J (sourceResidueOperator i J r hh (r x))) = transverse hh F x := by
  rw [sourceResidueOperator_section i J r hr, hr]
  rfl

end SplitZero.MonicResidue
