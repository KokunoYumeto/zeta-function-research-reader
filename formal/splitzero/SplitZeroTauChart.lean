import SplitZeroHomology

/-!
# The four-point linear chart over the absolute point

The concrete diagram category for + < eta < sigma and - < eta < sigma.
All three generating restrictions and all four coefficient modules are retained.
Sections and the two-term cohomology model are constructed from those maps.
-/
noncomputable section
namespace SplitZero.TauChart
open SplitZero.Homology

universe u

inductive Point
  | plus | minus | eta | sigma
  deriving DecidableEq, Fintype

def Point.le : Point → Point → Prop
  | .plus, .plus => True
  | .minus, .minus => True
  | _, .sigma => True
  | .plus, .eta => True
  | .minus, .eta => True
  | .eta, .eta => True
  | _, _ => False

instance : PartialOrder Point where
  le := Point.le
  le_refl x := by cases x <;> trivial
  le_trans x y z h h' := by cases x <;> cases y <;> cases z <;> simp_all [Point.le]
  le_antisymm x y h h' := by cases x <;> cases y <;> simp_all [Point.le]

instance : DecidableRel ((· ≤ ·) : Point → Point → Prop) :=
  fun x y => by
    change Decidable (Point.le x y)
    cases x <;> cases y <;> simp only [Point.le] <;> infer_instance

instance : TopologicalSpace Point where
  IsOpen U := ∀ x ∈ U, ∀ y, x ≤ y → y ∈ U
  isOpen_univ := by simp
  isOpen_inter := by
    intro s t hs ht x hx y hxy
    exact ⟨hs x hx.1 y hxy, ht x hx.2 y hxy⟩
  isOpen_sUnion := by
    intro S hS x hx y hxy
    obtain ⟨s, hs, hx⟩ := Set.mem_sUnion.mp hx
    exact Set.mem_sUnion.mpr ⟨s, hs, hS s hs x hx y hxy⟩

def toBase : C(Point, Unit) := ⟨fun _ => (), continuous_const⟩

structure Diagram (R : Type u) [CommRing R] where
  plus : ModuleCat.{u} R
  minus : ModuleCat.{u} R
  eta : ModuleCat.{u} R
  sigma : ModuleCat.{u} R
  left : plus →ₗ[R] eta
  right : minus →ₗ[R] eta
  tail : eta →ₗ[R] sigma

variable {R : Type u} [CommRing R]

abbrev ZeroModule (R : Type u) := Fin 0 → R
abbrev zeroObj : ModuleCat.{u} R := ModuleCat.of R (ZeroModule R)

namespace Diagram
variable (F G H : Diagram R)

abbrev MapTuple := (F.plus →ₗ[R] G.plus) × (F.minus →ₗ[R] G.minus) ×
  (F.eta →ₗ[R] G.eta) × (F.sigma →ₗ[R] G.sigma)

def compatibleMaps : Submodule R (MapTuple F G) where
  carrier := {f | (∀ x, G.left (f.1 x) = f.2.2.1 (F.left x)) ∧
    (∀ y, G.right (f.2.1 y) = f.2.2.1 (F.right y)) ∧
    (∀ z, G.tail (f.2.2.1 z) = f.2.2.2 (F.tail z))}
  zero_mem' := by simp
  add_mem' := by
    intro f g hf hg
    constructor
    · intro x
      change G.left (f.1 x + g.1 x) = f.2.2.1 (F.left x) + g.2.2.1 (F.left x)
      rw [map_add, hf.1, hg.1]
    constructor
    · intro x
      change G.right (f.2.1 x + g.2.1 x) = f.2.2.1 (F.right x) + g.2.2.1 (F.right x)
      rw [map_add, hf.2.1, hg.2.1]
    · intro x
      change G.tail (f.2.2.1 x + g.2.2.1 x) = f.2.2.2 (F.tail x) + g.2.2.2 (F.tail x)
      rw [map_add, hf.2.2, hg.2.2]
  smul_mem' := by
    intro a f hf
    constructor
    · intro x
      change G.left (a • f.1 x) = a • f.2.2.1 (F.left x)
      rw [map_smul, hf.1]
    constructor
    · intro x
      change G.right (a • f.2.1 x) = a • f.2.2.1 (F.right x)
      rw [map_smul, hf.2.1]
    · intro x
      change G.tail (a • f.2.2.1 x) = a • f.2.2.2 (F.tail x)
      rw [map_smul, hf.2.2]

/-- A type-level wrapper retains the diagram parameters during elaboration. -/
def Hom : Type u := ↥(compatibleMaps F G)

instance : AddCommGroup (Hom F G) := inferInstanceAs (AddCommGroup ↥(compatibleMaps F G))
instance : Module R (Hom F G) := inferInstanceAs (Module R ↥(compatibleMaps F G))

namespace Hom
variable {F G H}
abbrev val (f : Hom F G) : MapTuple F G := (show ↥(compatibleMaps F G) from f).val
abbrev plus (f : Hom F G) := f.val.1
abbrev minus (f : Hom F G) := f.val.2.1
abbrev eta (f : Hom F G) := f.val.2.2.1
abbrev sigma (f : Hom F G) := f.val.2.2.2

@[ext] theorem ext {f g : Hom F G} (hp : f.plus = g.plus) (hm : f.minus = g.minus)
    (he : f.eta = g.eta) (hs : f.sigma = g.sigma) : f = g :=
  Subtype.ext (Prod.ext hp (Prod.ext hm (Prod.ext he hs)))

@[simp] theorem left_naturality (f : Hom F G) (x : F.plus) :
    G.left (f.plus x) = f.eta (F.left x) := (show ↥(compatibleMaps F G) from f).property.1 x
@[simp] theorem right_naturality (f : Hom F G) (x : F.minus) :
    G.right (f.minus x) = f.eta (F.right x) := (show ↥(compatibleMaps F G) from f).property.2.1 x
@[simp] theorem tail_naturality (f : Hom F G) (x : F.eta) :
    G.tail (f.eta x) = f.sigma (F.tail x) := (show ↥(compatibleMaps F G) from f).property.2.2 x
end Hom

def mkHom (p : F.plus →ₗ[R] G.plus) (m : F.minus →ₗ[R] G.minus)
    (e : F.eta →ₗ[R] G.eta) (s : F.sigma →ₗ[R] G.sigma)
    (hp : ∀ x, G.left (p x) = e (F.left x))
    (hm : ∀ x, G.right (m x) = e (F.right x))
    (hs : ∀ x, G.tail (e x) = s (F.tail x)) : Hom F G :=
  ⟨(p, m, e, s), hp, hm, hs⟩

def identity : Hom F F := mkHom F F LinearMap.id LinearMap.id LinearMap.id LinearMap.id
  (fun _ => rfl) (fun _ => rfl) (fun _ => rfl)

def compose (f : Hom F G) (g : Hom G H) : Hom F H :=
  mkHom F H (g.plus.comp f.plus) (g.minus.comp f.minus)
    (g.eta.comp f.eta) (g.sigma.comp f.sigma)
    (by intro x; simp) (by intro x; simp) (by intro x; simp)

@[simp] theorem compose_identity (f : Hom F G) : compose F G G f (identity G) = f := by
  apply Hom.ext <;> apply LinearMap.ext <;> intro x <;> rfl
@[simp] theorem identity_compose (f : Hom F G) : compose F F G (identity F) f = f := by
  apply Hom.ext <;> apply LinearMap.ext <;> intro x <;> rfl

theorem compose_assoc {K : Diagram R} (f : Hom F G) (g : Hom G H) (h : Hom H K) :
    compose F H K (compose F G H f g) h = compose F G K f (compose G H K g h) := by
  apply Hom.ext <;> apply LinearMap.ext <;> intro x <;> rfl

def differential : (F.plus × F.minus) →ₗ[R] F.eta :=
  F.left.comp (LinearMap.fst R F.plus F.minus) -
    F.right.comp (LinearMap.snd R F.plus F.minus)

@[simp] theorem differential_apply (x : F.plus) (y : F.minus) :
    F.differential (x,y) = F.left x - F.right y := rfl

abbrev Sections := LinearMap.ker F.differential

theorem sections_extend_iff (x : F.plus) (y : F.minus) :
    F.differential (x,y) = 0 ↔
      ∃! z : F.eta × F.sigma, F.left x = z.1 ∧ F.right y = z.1 ∧ F.tail z.1 = z.2 := by
  constructor
  · intro h
    have hxy : F.left x = F.right y := sub_eq_zero.mp h
    refine ⟨(F.left x, F.tail (F.left x)), ⟨rfl, hxy.symm, rfl⟩, ?_⟩
    rintro ⟨z,s⟩ ⟨hx, _, hs⟩
    apply Prod.ext
    · exact hx.symm
    · exact hs.symm.trans (congrArg F.tail hx.symm)
  · rintro ⟨z, hz, _⟩
    exact sub_eq_zero.mpr (hz.1.trans hz.2.1.symm)

/-- The actual window computing degree one of the chart complex. -/
def degreeOne : Window R where
  Mprev := F.plus × F.minus
  M := F.eta
  Mnext := F.eta
  prev := F.differential
  next := 0
  square_zero := by simp

/-- The actual window computing degree zero. -/
def degreeZero : Window R where
  Mprev := ZeroModule R
  M := F.plus × F.minus
  Mnext := F.eta
  prev := 0
  next := F.differential
  square_zero := by simp

def degreeOneMap (f : Hom F G) : ChainMap F.degreeOne G.degreeOne where
  left := f.plus.prodMap f.minus
  mid := f.eta
  right := f.eta
  prev_comm := by
    apply LinearMap.ext; rintro ⟨x,y⟩
    change f.eta (F.left x - F.right y) = G.left (f.plus x) - G.right (f.minus y)
    rw [map_sub, f.left_naturality, f.right_naturality]
  next_comm := by simp [degreeOne]

theorem restriction_homotopy (x : F.plus) (y : F.minus) :
    F.tail (F.left x) - F.tail (F.right y) = F.tail (F.differential (x,y)) := by
  rw [differential_apply, map_sub]

theorem restriction_on_sections (z : F.Sections) :
    F.tail (F.left z.1.1) = F.tail (F.right z.1.2) := by
  have h : F.left z.1.1 = F.right z.1.2 := sub_eq_zero.mp z.2
  rw [h]

end Diagram
end SplitZero.TauChart
