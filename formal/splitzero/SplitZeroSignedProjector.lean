import SplitZeroHomology
import Mathlib.RepresentationTheory.Invariants
import Mathlib.Tactic

/-!
# Signed finite-group projections and the original homology

Mathlib supplies the Reynolds projector. We retain its literal order inverse,
twist an actual representation by a character, and build the induced chain map
on the pre-existing SplitZero homology window. The top-degree Koszul sign is
cancelled by the second sign, rather than replacing the chain action silently.
-/
noncomputable section
namespace SplitZero.SignedProjector

variable {G V W : Type*} [Group G] [Fintype G]
  [AddCommGroup V] [Module ℂ V] [AddCommGroup W] [Module ℂ W]
  [Invertible (Fintype.card G : ℂ)]

/-- Twist the supplied chain representation by its actual character. -/
def twist (chi : G →* ℂ) (rho : Representation ℂ G V) : Representation ℂ G V where
  toFun g := chi g • rho g
  map_one' := by simp
  map_mul' g h := by
    ext x
    simp [map_mul, Module.End.mul_apply, smul_smul, mul_comm]

theorem average_apply (rho : Representation ℂ G V) (x : V) :
    rho.averageMap x = ⅟(Fintype.card G : ℂ) • ∑ g : G, rho g x := by
  simp [Representation.averageMap, GroupAlgebra.average, map_sum]

/-- This retains the coefficient 1/|G| in the signed average. -/
theorem signed_average_apply (chi : G →* ℂ) (rho : Representation ℂ G V) (x : V) :
    (twist chi rho).averageMap x =
      ⅟(Fintype.card G : ℂ) • ∑ g : G, chi g • rho g x := by
  rw [average_apply]
  rfl

theorem average_idempotent (rho : Representation ℂ G V) :
    rho.averageMap.comp rho.averageMap = rho.averageMap := by
  apply LinearMap.ext
  intro x
  exact rho.averageMap_id _ (rho.averageMap_invariant x)

/-- An invariant vector is preserved, not replaced by an orbit representative. -/
theorem preserves_invariant (rho : Representation ℂ G V) (x : V)
    (hx : ∀ g, rho g x = x) : rho.averageMap x = x :=
  rho.averageMap_id x hx

/-- The exact naturality used for derivatives, jets and representatives. -/
theorem average_natural (rho : Representation ℂ G V) (sigma : Representation ℂ G W)
    (f : V →ₗ[ℂ] W) (hf : ∀ g x, f (rho g x) = sigma g (f x)) :
    f.comp rho.averageMap = sigma.averageMap.comp f := by
  apply LinearMap.ext
  intro x
  simp only [LinearMap.comp_apply, average_apply, map_smul, map_sum, hf]

/-- Cancelling both signs gives the ordinary invariant projector at top degree. -/
theorem top_double_sign (chi : G →* ℂ) (rho sigma : Representation ℂ G V)
    (hchi : ∀ g, chi g * chi g = 1)
    (htop : ∀ g x, sigma g x = chi g • rho g x) :
    (twist chi sigma).averageMap = rho.averageMap := by
  have he : twist chi sigma = rho := by
    ext g x
    change chi g • sigma g x = rho g x
    rw [htop, smul_smul, hchi, one_smul]
  rw [he]

/-- A repeated invariant eigenvector survives the correctly signed top projector. -/
theorem top_preserves_invariant (chi : G →* ℂ) (rho sigma : Representation ℂ G V)
    (hchi : ∀ g, chi g * chi g = 1)
    (htop : ∀ g x, sigma g x = chi g • rho g x)
    (x : V) (hx : ∀ g, rho g x = x) :
    (twist chi sigma).averageMap x = x := by
  rw [top_double_sign chi rho sigma hchi htop]
  exact preserves_invariant rho x hx

section Window
open SplitZero.Homology
variable (C : Window ℂ)

/-- A finite group acting on every term of the original window, with its actual d. -/
structure Action where
  prevRep : Representation ℂ G C.Mprev
  midRep : Representation ℂ G C.M
  nextRep : Representation ℂ G C.Mnext
  prev_comm : ∀ g x, C.prev (prevRep g x) = midRep g (C.prev x)
  next_comm : ∀ g x, C.next (midRep g x) = nextRep g (C.next x)

namespace Action
variable {C} (S : Action (G := G) C)

def averageChain : ChainMap C C where
  left := S.prevRep.averageMap
  mid := S.midRep.averageMap
  right := S.nextRep.averageMap
  prev_comm := (average_natural S.prevRep S.midRep C.prev S.prev_comm).symm
  next_comm := average_natural S.midRep S.nextRep C.next S.next_comm

/-- Idempotence is proved after the actual quotient by boundaries. -/
theorem homology_idempotent :
    S.averageChain.onHomology.comp S.averageChain.onHomology =
      S.averageChain.onHomology := by
  apply LinearMap.ext
  intro x
  induction x using Submodule.Quotient.induction_on with
  | _ z =>
    change C.classOf (S.averageChain.cyclesMap (S.averageChain.cyclesMap z)) =
      C.classOf (S.averageChain.cyclesMap z)
    congr 1
    apply Subtype.ext
    exact S.midRep.averageMap_id _ (S.midRep.averageMap_invariant z.val)

/-- An invariant source cycle retains its exact homology class. -/
theorem invariant_class (z : C.Cycles) (hz : ∀ g, S.midRep g z.val = z.val) :
    S.averageChain.onHomology (C.classOf z) = C.classOf z := by
  change C.classOf (S.averageChain.cyclesMap z) = C.classOf z
  congr 1
  apply Subtype.ext
  exact S.midRep.averageMap_id z.val hz

/-- The complementary homology map is retained as part of the decomposition. -/
def complementHomology : C.H →ₗ[ℂ] C.H :=
  LinearMap.id - S.averageChain.onHomology

theorem homology_decomposition (x : C.H) :
    S.averageChain.onHomology x + S.complementHomology x = x := by
  change S.averageChain.onHomology x + (x - S.averageChain.onHomology x) = x
  abel

theorem complement_idempotent :
    S.complementHomology.comp S.complementHomology = S.complementHomology := by
  apply LinearMap.ext
  intro x
  have hi := LinearMap.congr_fun S.homology_idempotent x
  change S.averageChain.onHomology (S.averageChain.onHomology x) =
    S.averageChain.onHomology x at hi
  change (x - S.averageChain.onHomology x) -
    S.averageChain.onHomology (x - S.averageChain.onHomology x) =
      x - S.averageChain.onHomology x
  rw [map_sub, hi]
  abel
end Action
end Window
end SplitZero.SignedProjector
