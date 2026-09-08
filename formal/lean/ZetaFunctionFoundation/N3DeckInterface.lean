import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# Exact finite algebra for the first-peeled N=3/deck-curve interface

This file formalizes the algebraic carrier and sheet maps, the target deck
involution, and the fixed-locus obstruction used in Theorem
`thm:n3-deck-interface` of the working synthesis.  The real open-disc
inequalities and the complete semialgebraic fibre intervals remain in the
human-readable proof.
-/

namespace ZetaFunctionFoundation.N3DeckInterface

noncomputable section

/-- The two displayed coordinates of the affine deck curve. -/
abbrev DeckCoordinates := Complex × Complex

/-- The polynomial parametrization `s ↦ (s(s-1), 2s-1)`. -/
def deckF (s : Complex) : DeckCoordinates :=
  (s * (s - 1), 2 * s - 1)

theorem deckF_curve (s : Complex) :
    (deckF s).2 ^ 2 = 1 + 4 * (deckF s).1 := by
  simp [deckF]
  ring

/-- The affine curve with every target coordinate retained. -/
def DeckCurve := {p : DeckCoordinates // p.2 ^ 2 = 1 + 4 * p.1}

/-- The point of the deck curve with parameter `s`. -/
def deckPoint (s : Complex) : DeckCurve :=
  ⟨deckF s, deckF_curve s⟩

/-- The exact inverse parameter `(b+1)/2`. -/
def deckInverse (p : DeckCurve) : Complex :=
  (p.1.2 + 1) / 2

theorem deckInverse_deckPoint (s : Complex) :
    deckInverse (deckPoint s) = s := by
  simp [deckInverse, deckPoint, deckF]

theorem deckPoint_deckInverse (p : DeckCurve) :
    deckPoint (deckInverse p) = p := by
  apply Subtype.ext
  apply Prod.ext
  · change ((p.1.2 + 1) / 2) * (((p.1.2 + 1) / 2) - 1) = p.1.1
    have hcurve := p.2
    dsimp [DeckCoordinates] at hcurve
    linear_combination (1 / 4 : Complex) * hcurve
  · change 2 * ((p.1.2 + 1) / 2) - 1 = p.1.2
    ring

theorem deckPoint_injective : Function.Injective deckPoint := by
  intro s t h
  have := congrArg deckInverse h
  simpa [deckInverse_deckPoint] using this

/-- The target deck involution `(a,b) ↦ (a,-b)`. -/
def deckTau (p : DeckCurve) : DeckCurve :=
  ⟨(p.1.1, -p.1.2), by
    change (-p.1.2) ^ 2 = 1 + 4 * p.1.1
    calc
      (-p.1.2) ^ 2 = p.1.2 ^ 2 := by ring
      _ = 1 + 4 * p.1.1 := p.2⟩

theorem deckTau_deckPoint (s : Complex) :
    deckTau (deckPoint s) = deckPoint (1 - s) := by
  apply Subtype.ext
  change (s * (s - 1), -(2 * s - 1)) =
    ((1 - s) * ((1 - s) - 1), 2 * (1 - s) - 1)
  apply Prod.ext <;> dsimp <;> ring

theorem deckTau_involutive (p : DeckCurve) :
    deckTau (deckTau p) = p := by
  apply Subtype.ext
  change (p.1.1, -(-p.1.2)) = p.1
  apply Prod.ext
  · rfl
  · simp

/-- The target deck involution has exactly one fixed point. -/
theorem deckTau_fixed_unique (p : DeckCurve) (hp : deckTau p = p) :
    p = deckPoint (1 / 2) := by
  have hb : -p.1.2 = p.1.2 := by
    exact congrArg (fun q : DeckCurve => q.1.2) hp
  have hb0 : p.1.2 = 0 := by
    linear_combination (-1 / 2 : Complex) * hb
  have hcurve := p.2
  rw [hb0] at hcurve
  have ha : p.1.1 = -(1 / 4 : Complex) := by
    linear_combination (-1 / 4 : Complex) * hcurve
  apply Subtype.ext
  apply Prod.ext
  · change p.1.1 = (1 / 2 : Complex) * (1 / 2 - 1)
    rw [ha]
    ring
  · change p.1.2 = 2 * (1 / 2 : Complex) - 1
    rw [hb0]
    ring

/-- A general fixed-locus obstruction: two distinct fixed source points cannot
map injectively and equivariantly to this one-fixed-point deck curve. -/
theorem no_equivariant_injective_of_two_fixed
    {X : Type*}
    (kappa : X → X)
    (M : X → DeckCurve)
    (x₀ x₁ : X)
    (hne : x₀ ≠ x₁)
    (hfix₀ : kappa x₀ = x₀)
    (hfix₁ : kappa x₁ = x₁)
    (hequivariant : ∀ x, M (kappa x) = deckTau (M x)) :
    ¬ Function.Injective M := by
  intro hinjective
  have hM₀fixed : deckTau (M x₀) = M x₀ := by
    rw [← hequivariant x₀, hfix₀]
  have hM₁fixed : deckTau (M x₁) = M x₁ := by
    rw [← hequivariant x₁, hfix₁]
  have hM₀ := deckTau_fixed_unique (M x₀) hM₀fixed
  have hM₁ := deckTau_fixed_unique (M x₁) hM₁fixed
  apply hne
  apply hinjective
  exact hM₀.trans hM₁.symm

/-- The retained physical base denominator `h=1-3u+8v`. -/
def physicalH (u v : Complex) : Complex :=
  1 - 3 * u + 8 * v

/-- The full recovered `β₀` coordinate used by the lossless carrier map. -/
def recoveredBeta (u v J : Complex) : Complex :=
  (1 - 9 * u + 32 * v) / (4 * physicalH u v) +
    8 * J / ((u - 1) * physicalH u v)

/-- The algebraic carrier into the deck curve. -/
def carrierPoint (u v J : Complex) : DeckCurve :=
  deckPoint (recoveredBeta u v J)

theorem carrier_recovers_parameter (u v J : Complex) :
    deckInverse (carrierPoint u v J) = recoveredBeta u v J := by
  exact deckInverse_deckPoint _

/-- The equivariant sheet parameter `1/2+8J/((u-1)h)`. -/
def sheetParameter (u v J : Complex) : Complex :=
  1 / 2 + 8 * J / ((u - 1) * physicalH u v)

/-- The corresponding sheet map into the deck curve. -/
def sheetPoint (u v J : Complex) : DeckCurve :=
  deckPoint (sheetParameter u v J)

theorem sheetParameter_neg_J (u v J : Complex) :
    sheetParameter u v (-J) = 1 - sheetParameter u v J := by
  simp [sheetParameter]
  ring

theorem sheetPoint_equivariant (u v J : Complex) :
    sheetPoint u v (-J) = deckTau (sheetPoint u v J) := by
  unfold sheetPoint
  rw [sheetParameter_neg_J]
  exact (deckTau_deckPoint (sheetParameter u v J)).symm

theorem sheetPoint_second_coordinate (u v J : Complex) :
    (sheetPoint u v J).1.2 =
      16 * J / ((u - 1) * physicalH u v) := by
  simp [sheetPoint, deckPoint, deckF, sheetParameter]
  ring

theorem sheetPoint_first_coordinate (u v J : Complex)
    (hu : u ≠ 1) (hh : physicalH u v ≠ 0) :
    (sheetPoint u v J).1.1 =
      64 * J ^ 2 / ((u - 1) ^ 2 * physicalH u v ^ 2) - 1 / 4 := by
  have hu1 : u - 1 ≠ 0 := sub_ne_zero.mpr hu
  simp only [sheetPoint, deckPoint, deckF, sheetParameter]
  field_simp [hu1, hh]
  ring

end

end ZetaFunctionFoundation.N3DeckInterface
