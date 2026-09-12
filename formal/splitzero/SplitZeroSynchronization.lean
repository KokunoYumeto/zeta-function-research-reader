import SplitZeroMaps

/-!
# The actual mixed-double synchronization and its pullback strictness

Source: the owner's split-support/Rees research continuation, section 2.1,
PR #3 at 37b2cc9b9baee3ffe25a7649314adb025302509f.
This extends PR #4 rather than duplicating its scalar/fibre library.

The literal mixed multiplication, idempotent E = (1,e), and amplitude in
A[t]/(t^2+1) are defined below. Idempotence and amplitude preservation are
proved for these maps, not assumed as hypotheses. The set-image theorem
applies to every level of any amplitude-pullback filtration. No general Rees
module, analytic theorem, or unrelated comparison map is certified here.
-/

namespace SplitZero.Synchronization

abbrev Mixed (A : Type*) := G A × G A

variable {A : Type*} [CommRing A]

/-- The mixed multiplication specified in the research note. -/
def mixedMul (x y : Mixed A) : Mixed A :=
  (x.1 * y.1 + (ofR (-1 : A) : G A) * (x.2 * y.2),
   x.1 * y.2 + x.2 * y.1)

def syncIdempotent : Mixed A := (1, e)

/-- Synchronization expressed without a choice of amplitude section. -/
def synchronize (x : Mixed A) : Mixed A :=
  (x.1 + (e : G A) * x.2, x.2 + (e : G A) * x.1)

theorem synchronize_absent : synchronize (tau, tau : G A) = (tau, tau) := rfl

theorem synchronize_supported (a b : A) :
    synchronize (ofR a, ofR b) = (ofR a, ofR b) := by
  change (ofR (a + 0 * b), ofR (b + 0 * a)) = (ofR a, ofR b)
  rw [zero_mul, zero_mul, add_zero, add_zero]

theorem synchronize_absent_left (b : A) :
    synchronize (tau, ofR b) = (e, ofR b) := by
  change (ofR (0 * b), ofR b) = (ofR 0, ofR b)
  rw [zero_mul]

theorem synchronize_absent_right (a : A) :
    synchronize (ofR a, tau) = (ofR a, e) := by
  change (ofR a, ofR (0 * a)) = (ofR a, ofR 0)
  rw [zero_mul]

/-- Idempotence is proved for the actual synchronization operation. -/
theorem synchronize_idempotent (x : Mixed A) : synchronize (synchronize x) = synchronize x := by
  obtain ⟨⟨_ | a⟩, ⟨_ | b⟩⟩ := x
  · rfl
  · exact (congrArg synchronize (synchronize_absent_left b)).trans
      ((synchronize_supported (0 : A) b).trans (synchronize_absent_left b).symm)
  · exact (congrArg synchronize (synchronize_absent_right a)).trans
      ((synchronize_supported a (0 : A)).trans (synchronize_absent_right a).symm)
  · exact (congrArg synchronize (synchronize_supported a b)).trans (synchronize_supported a b)

/-- This is multiplication by the source's specific element E = (1,e). -/
theorem synchronize_eq_mul (x : Mixed A) : synchronize x = mixedMul syncIdempotent x := by
  have he : (ofR (-1 : A) : G A) * e = e := by
    change ofR ((-1 : A) * 0) = ofR 0
    rw [mul_zero]
  apply Prod.ext
  · change x.1 + (e : G A) * x.2 = 1 * x.1 + (ofR (-1 : A) : G A) * (e * x.2)
    rw [one_mul, ← mul_assoc, he]
  · change x.2 + (e : G A) * x.1 = 1 * x.2 + (e : G A) * x.1
    rw [one_mul]

theorem mul_E_E : mixedMul (syncIdempotent : Mixed A) syncIdempotent = syncIdempotent := by
  rw [← synchronize_eq_mul]
  exact synchronize_supported (1 : A) 0

/-- The image of synchronization is exactly its fixed locus. -/
theorem synchronize_fixed_iff_mem_range (x : Mixed A) :
    synchronize x = x ↔ x ∈ Set.range (synchronize (A := A)) := by
  constructor
  · intro h
    exact ⟨x, h⟩
  · rintro ⟨y, rfl⟩
    exact synchronize_idempotent y

def amplitudeCoordinates (x : Mixed A) : A × A := (reflect x.1, reflect x.2)

theorem amplitudeCoordinates_synchronize (x : Mixed A) :
    amplitudeCoordinates (synchronize x) = amplitudeCoordinates x := by
  apply Prod.ext
  · change reflect (x.1 + (e : G A) * x.2) = reflect x.1
    rw [map_add, map_mul]
    change reflect x.1 + 0 * reflect x.2 = reflect x.1
    rw [zero_mul, add_zero]
  · change reflect (x.2 + (e : G A) * x.1) = reflect x.2
    rw [map_add, map_mul]
    change reflect x.2 + 0 * reflect x.1 = reflect x.2
    rw [zero_mul, add_zero]

/-- The literal quotient algebra A[t]/(t^2+1), not a substitute scalar invariant. -/
abbrev Amplitude (A : Type*) [CommRing A] :=
  AdjoinRoot ((Polynomial.X : Polynomial A) ^ 2 + 1)

def amplitude (x : Mixed A) : Amplitude A :=
  algebraMap A (Amplitude A) (reflect x.1) +
    AdjoinRoot.root ((Polynomial.X : Polynomial A) ^ 2 + 1) *
      algebraMap A (Amplitude A) (reflect x.2)

theorem amplitude_synchronize (x : Mixed A) : amplitude (synchronize x) = amplitude x := by
  exact congrArg (fun z : A × A =>
    algebraMap A (Amplitude A) z.1 +
      AdjoinRoot.root ((Polynomial.X : Polynomial A) ^ 2 + 1) *
        algebraMap A (Amplitude A) z.2) (amplitudeCoordinates_synchronize x)

/-- Exact image equality for every amplitude-pullback set, hence for every
filtration level. No idempotence or strictness hypothesis is assumed. -/
theorem synchronize_strict (F : Set (Amplitude A)) :
    synchronize '' (amplitude ⁻¹' F) =
      Set.range (synchronize (A := A)) ∩ (amplitude ⁻¹' F) := by
  ext y
  constructor
  · rintro ⟨x, hx, rfl⟩
    refine ⟨⟨x, rfl⟩, ?_⟩
    change amplitude (synchronize x) ∈ F
    rw [amplitude_synchronize]
    exact hx
  · rintro ⟨⟨x, rfl⟩, hx⟩
    exact ⟨synchronize x, hx, synchronize_idempotent x⟩

/-- The same strictness statement for the research note's literal E multiplication. -/
theorem mul_E_strict (F : Set (Amplitude A)) :
    (mixedMul syncIdempotent) '' (amplitude ⁻¹' F) =
      Set.range (mixedMul (syncIdempotent : Mixed A)) ∩ (amplitude ⁻¹' F) := by
  have h : (mixedMul syncIdempotent : Mixed A → Mixed A) = synchronize := by
    funext x
    exact (synchronize_eq_mul x).symm
  rw [h]
  exact synchronize_strict F

end SplitZero.Synchronization
