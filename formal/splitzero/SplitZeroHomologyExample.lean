import SplitZeroInternalQuotient

/-!
# A nonzero cycle transported to a nonzero boundary

This is a parametric example over every nontrivial commutative coefficient ring.
The source and target complexes are fixed. One chain map kills the source class;
a second sends it to a surviving target class. Thus identical support labels,
fibre homology modules and terminal homology do not determine the transition kernel.
-/

noncomputable section
namespace SplitZero.HomologyExample
open SplitZero.Homology

variable (k : Type*) [CommRing k]

def first : k →ₗ[k] k × k := (LinearMap.id : k →ₗ[k] k).prod 0

def second : k →ₗ[k] k × k := (0 : k →ₗ[k] k).prod LinearMap.id

def source : Window k where
  Mprev := k
  M := k
  Mnext := k
  prev := 0
  next := 0
  square_zero := by ext x; rfl

def target : Window k where
  Mprev := k
  M := k × k
  Mnext := k
  prev := first k
  next := 0
  square_zero := by ext x; rfl

def killed : ChainMap (source k) (target k) where
  left := 0
  mid := first k
  right := 0
  prev_comm := by ext x <;> simp [source, target, first]
  next_comm := by ext x; rfl

def surviving : ChainMap (source k) (target k) where
  left := 0
  mid := second k
  right := 0
  prev_comm := by ext x <;> simp [source, target, first, second]
  next_comm := by ext x; rfl

def unitCycle : (source k).Cycles := ⟨1, rfl⟩

theorem unit_class_nonzero [Nontrivial k] : (source k).classOf (unitCycle k) ≠ 0 := by
  intro h
  obtain ⟨x, hx⟩ := ((source k).class_zero_iff_boundary (unitCycle k)).mp h
  exact zero_ne_one hx

theorem killed_map_zero : (killed k).onHomology = 0 := by
  apply LinearMap.ext
  intro x
  induction x using Submodule.Quotient.induction_on with
  | _ z =>
    exact ((killed k).mapped_class_zero_iff z).mpr ⟨z.val, rfl⟩

theorem chain_image_nonzero [Nontrivial k] : (killed k).mid (unitCycle k).val ≠ 0 := by
  intro h
  have h' : (1 : k) = 0 := congrArg Prod.fst h
  exact one_ne_zero h'

theorem surviving_class_nonzero [Nontrivial k] :
    (surviving k).onHomology ((source k).classOf (unitCycle k)) ≠ 0 := by
  intro h
  obtain ⟨x, hx⟩ := ((surviving k).mapped_class_zero_iff (unitCycle k)).mp h
  have h' : (0 : k) = 1 := congrArg Prod.snd hx
  exact zero_ne_one h'

/-- A genuine nonzero element of the induced kernel, with the actual representative. -/
theorem nonzero_transition_kernel [Nontrivial k] :
    ∃ x : (source k).H, x ≠ 0 ∧ (killed k).onHomology x = 0 := by
  refine ⟨(source k).classOf (unitCycle k), unit_class_nonzero k, ?_⟩
  rw [killed_map_zero]
  rfl

/-- Same source, same target, different homological observations. -/
theorem transition_maps_distinct [Nontrivial k] :
    (killed k).onHomology ≠ (surviving k).onHomology := by
  intro h
  apply surviving_class_nonzero k
  rw [← h, killed_map_zero]
  rfl

end SplitZero.HomologyExample
