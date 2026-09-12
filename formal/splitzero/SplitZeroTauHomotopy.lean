import SplitZeroTauChart
import SplitZeroTauDual

/-!
# All cochain homotopies of the two-leg comparison

Both cochain equations are retained. The affine solution set is parameterized
by maps from the actual cokernel, not arbitrary maps from the cochain space.
The analytic theta/Fourier instantiation is a separate obligation.
-/
noncomputable section
namespace SplitZero.TauHomotopy
universe u
variable {R V B : Type u} [CommRing R]
  [AddCommGroup V] [Module R V] [AddCommGroup B] [Module R B]
variable (Θ : V →ₗ[R] B) (F : V ≃ₗ[R] V)

def delta : (V × V) →ₗ[R] B :=
  Θ.comp ((LinearMap.fst R V V) - F.toLinearMap.comp (LinearMap.snd R V V))

abbrev thetaDiagram : SplitZero.TauChart.Diagram R where
  plus := ModuleCat.of R V
  minus := ModuleCat.of R V
  eta := ModuleCat.of R B
  sigma := SplitZero.TauChart.zeroObj
  left := Θ
  right := Θ.comp F.toLinearMap
  tail := 0

theorem chart_differential : (thetaDiagram Θ F).differential = delta Θ F := by
  apply LinearMap.ext
  rintro ⟨v, w⟩
  exact (Θ.map_sub v (F w)).symm

theorem delta_range : LinearMap.range (delta Θ F) = LinearMap.range Θ := by
  apply le_antisymm
  · rintro b ⟨⟨v, w⟩, rfl⟩
    exact ⟨v - F w, rfl⟩
  · rintro b ⟨v, rfl⟩
    refine ⟨(v, 0), ?_⟩
    change Θ (v - F 0) = Θ v
    rw [map_zero, sub_zero]

theorem boundary_vanishing_iff (H : B →ₗ[R] (V × V)) :
    H.comp (delta Θ F) = 0 ↔ ∀ v, H (Θ v) = 0 := by
  constructor
  · intro h v
    have hv := LinearMap.congr_fun h (v, 0)
    change H (Θ (v - F 0)) = 0 at hv
    simpa only [map_zero, sub_zero] using hv
  · intro h
    apply LinearMap.ext
    rintro ⟨v, w⟩
    exact h (v - F w)

def lift (κ a : B →ₗ[R] V) : B →ₗ[R] (V × V) :=
  (κ + a).prod (F.symm.toLinearMap.comp a)

abbrev Homotopies (κ : B →ₗ[R] V) :=
  { H : B →ₗ[R] (V × V) //
      (delta Θ F).comp H = Θ.comp κ ∧ ∀ v, H (Θ v) = 0 }

def annihilatorHomotopyEquiv (hΘ : Function.Injective Θ)
    (κ : B →ₗ[R] V) (hκ : ∀ v, κ (Θ v) = 0) :
    SplitZero.TauDual.annihilator (W := V) (LinearMap.range Θ) ≃ Homotopies Θ F κ where
  toFun a := by
    refine ⟨lift F κ a.val, ?_, ?_⟩
    · apply LinearMap.ext
      intro b
      change Θ (κ b + a.val b - F (F.symm (a.val b))) = Θ (κ b)
      rw [F.apply_symm_apply, add_sub_cancel_right]
    · intro v
      have ha : a.val (Θ v) = 0 := a.property (Θ v) ⟨v, rfl⟩
      apply Prod.ext
      · change κ (Θ v) + a.val (Θ v) = 0
        rw [hκ v, ha, add_zero]
      · change F.symm (a.val (Θ v)) = 0
        rw [ha, map_zero]
  invFun H := by
    refine ⟨F.toLinearMap.comp ((LinearMap.snd R V V).comp H.val), ?_⟩
    rintro b ⟨v, rfl⟩
    change F ((H.val (Θ v)).2) = 0
    rw [H.property.2 v]
    exact F.map_zero
  left_inv a := by
    apply Subtype.ext
    apply LinearMap.ext
    intro b
    change F (F.symm (a.val b)) = a.val b
    exact F.apply_symm_apply _
  right_inv H := by
    apply Subtype.ext
    apply LinearMap.ext
    intro b
    have hb := LinearMap.congr_fun H.property.1 b
    change Θ ((H.val b).1 - F ((H.val b).2)) = Θ (κ b) at hb
    have he := hΘ hb
    apply Prod.ext
    · change κ b + F ((H.val b).2) = (H.val b).1
      rw [← he, sub_add_cancel]
    · change F.symm (F ((H.val b).2)) = (H.val b).2
      exact F.symm_apply_apply _

def cochainHomotopyEquiv (hΘ : Function.Injective Θ)
    (κ : B →ₗ[R] V) (hκ : ∀ v, κ (Θ v) = 0) :
    ((B ⧸ LinearMap.range Θ) →ₗ[R] V) ≃ Homotopies Θ F κ :=
  (SplitZero.TauDual.quotientDualEquiv (W := V) (LinearMap.range Θ)).toEquiv.trans
    (annihilatorHomotopyEquiv Θ F hΘ κ hκ)

theorem two_lifts_difference (κ : B →ₗ[R] V) (b : B) :
    lift F κ 0 b - lift F κ (-κ) b = (κ b, F.symm (κ b)) := by
  apply Prod.ext
  · change (κ b + 0) - (κ b + -κ b) = κ b
    rw [add_zero, add_neg_cancel, sub_zero]
  · change F.symm 0 - F.symm (-κ b) = F.symm (κ b)
    rw [map_zero, map_neg, zero_sub, neg_neg]

theorem difference_is_cycle (v : V) : delta Θ F (v, F.symm v) = 0 := by
  change Θ (v - F (F.symm v)) = 0
  rw [F.apply_symm_apply, sub_self, map_zero]

theorem leg_agreement_iff (v : V) :
    ((v, 0) : V × V) = (0, -F.symm v) ↔ v = 0 := by
  constructor
  · intro h
    exact congrArg Prod.fst h
  · intro h
    subst v
    simp

theorem difference_nonzero {v : V} (hv : v ≠ 0) :
    ((v, F.symm v) : V × V) ≠ 0 := by
  intro h
  exact hv (congrArg Prod.fst h)

end SplitZero.TauHomotopy
