import SplitZeroPresentation

/-!
# Exact morphisms of split-zero scalars

Maps into ordinary rings necessarily erase support. Maps between split-zero
objects, in contrast, correspond bijectively to ring maps of amplitudes.
-/

namespace SplitZero.Maps
open SplitZero.Extension SplitZero.Presentation

variable {R S : Type*} [CommRing R] [CommRing S]

/-- No map from split-zero scalars into an ordinary ring can be injective. -/
theorem no_injective_ring_target {A : Type*} [CommRing A] (h : G R →+* A) :
    ¬ Function.Injective h := by
  intro hi
  exact e_ne_tau (hi ((hom_kills_e h).trans h.map_zero.symm))

/-- Amplitude and support jointly retain all information. -/
def coordinates : G R →+* R × Bit := reflect.prod supportCharacter

theorem coordinates_injective : Function.Injective (coordinates (R := R)) := by
  intro x y h
  obtain ⟨_ | r⟩ := x <;> obtain ⟨_ | s⟩ := y
  · rfl
  · have hh : Bit.absent = Bit.present := congrArg Prod.snd h
    cases hh
  · have hh : Bit.present = Bit.absent := congrArg Prod.snd h
    cases hh
  · have hh : r = s := congrArg Prod.fst h
    cases hh
    rfl

/-- The image is precisely the supported coordinate subsemiring from the source. -/
theorem coordinates_image (r : R) (b : Bit) :
    (∃ x : G R, coordinates x = (r, b)) ↔ (b = 0 → r = 0) := by
  constructor
  · rintro ⟨⟨_ | s⟩, h⟩ hb
    · exact (congrArg Prod.fst h).symm
    · have hs : (1 : Bit) = b := congrArg Prod.snd h
      exact False.elim (Bit.one_ne_zero (hs.trans hb))
  · intro h
    cases b with
    | absent =>
      have hr := h rfl
      subst r
      exact ⟨tau, rfl⟩
    | present => exact ⟨ofR r, rfl⟩

/-- A ring homomorphism acts on amplitudes without erasing support. -/
def liftRingHom (f : R →+* S) : G R →+* G S where
  toFun x := ⟨x.toOption.map f⟩
  map_zero' := rfl
  map_one' := by change ofR (f 1) = ofR (1 : S); rw [f.map_one]
  map_add' x y := by
    obtain ⟨_ | r⟩ := x <;> obtain ⟨_ | s⟩ := y
    · rfl
    · rfl
    · rfl
    · change ofR (f (r + s)) = ofR (f r + f s)
      rw [f.map_add]
  map_mul' x y := by
    obtain ⟨_ | r⟩ := x <;> obtain ⟨_ | s⟩ := y
    · rfl
    · rfl
    · rfl
    · change ofR (f (r * s)) = ofR (f r * f s)
      rw [f.map_mul]

theorem reflection_natural (f : R →+* S) :
    reflect.comp (liftRingHom f) = f.comp reflect := by
  apply RingHom.ext
  intro x
  obtain ⟨_ | r⟩ := x
  · exact f.map_zero.symm
  · rfl

/-- A split-to-split semiring map is determined by its amplitude map. -/
theorem amplitude_faithful (f g : G R →+* G S)
    (h : reflect.comp f = reflect.comp g) : f = g := by
  apply RingHom.ext
  intro x
  apply coordinates_injective
  apply Prod.ext
  · exact congrArg (fun k : G R →+* S => k x) h
  · have hf := supportCharacter_unique ((supportCharacter (R := S)).comp f)
    have hg := supportCharacter_unique ((supportCharacter (R := S)).comp g)
    exact congrArg (fun k : G R →+* Bit => k x) (hf.trans hg.symm)

/-- Full faithfulness at the level of hom sets: no extra split-to-split maps appear. -/
def splitHomEquiv : (G R →+* G S) ≃ (R →+* S) where
  toFun h := restrictToRing (reflect.comp h)
  invFun := liftRingHom
  left_inv h := by
    apply amplitude_faithful
    exact (reflection_natural _).trans (ringHomEquiv.left_inv (reflect.comp h))
  right_inv f := by
    apply RingHom.ext
    intro r
    rfl

end SplitZero.Maps
