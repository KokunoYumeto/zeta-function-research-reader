import Mathlib.Tactic

/-!
# Exact top degree in a local monomial relation-power quotient

The quotient/remainder predicate is proved equivalent to the literal floor-sum
condition. Both the bound and an attaining exponent vector are constructed.
Identifying the monomials with the original polynomial quotient and applying
the characteristic-zero multinomial theorem are separate written steps.
-/
namespace SplitZero.CyclicDepth
open scoped BigOperators

variable {ι : Type*} [Fintype ι]

/-- Monomials surviving the r-th power, in quotient-remainder coordinates. -/
def Admissible (m : ι → ℕ) (r : ℕ) (a : ι → ℕ) : Prop :=
  ∃ q t : ι → ℕ, (∀ i, t i < m i) ∧
    (∀ i, a i = t i + m i * q i) ∧ (∑ i, q i) < r

/-- Every exponent satisfying the floor-sum condition has these coordinates. -/
theorem admissible_of_floor_sum (m a : ι → ℕ) (r : ℕ)
    (hm : ∀ i, 0 < m i) (ha : (∑ i, a i / m i) < r) :
    Admissible m r a := by
  refine ⟨fun i => a i / m i, fun i => a i % m i, ?_, ?_, ha⟩
  · exact fun i => Nat.mod_lt _ (hm i)
  · exact fun i => (Nat.mod_add_div _ _).symm

theorem floor_sum_of_admissible (m a : ι → ℕ) (r : ℕ)
    (ha : Admissible m r a) : (∑ i, a i / m i) < r := by
  obtain ⟨q, t, ht, he, hq⟩ := ha
  have hdiv (i : ι) : a i / m i = q i := by
    have hm : 0 < m i := Nat.lt_of_le_of_lt (Nat.zero_le (t i)) (ht i)
    rw [he i, Nat.add_mul_div_left _ _ hm, Nat.div_eq_of_lt (ht i), zero_add]
  simpa only [hdiv] using hq

theorem admissible_iff_floor_sum (m a : ι → ℕ) (r : ℕ)
    (hm : ∀ i, 0 < m i) :
    Admissible m r a ↔ (∑ i, a i / m i) < r :=
  ⟨floor_sum_of_admissible m a r, admissible_of_floor_sum m a r hm⟩

/-- The exact degree ceiling uses the largest multiplicity once per extra layer. -/
def ceiling (m : ι → ℕ) (r M : ℕ) : ℕ :=
  (∑ i, (m i - 1)) + (r - 1) * M

theorem degree_le (m a : ι → ℕ) (r M : ℕ)
    (hmax : ∀ i, m i ≤ M) (ha : Admissible m r a) :
    (∑ i, a i) ≤ ceiling m r M := by
  obtain ⟨q, t, ht, he, hq⟩ := ha
  have hqi : (∑ i, q i) ≤ r - 1 := by omega
  have hi (i : ι) : a i ≤ (m i - 1) + M * q i := by
    rw [he i]
    exact Nat.add_le_add (by have := ht i; omega)
      (Nat.mul_le_mul_right (q i) (hmax i))
  calc
    (∑ i, a i) ≤ ∑ i, ((m i - 1) + M * q i) := Finset.sum_le_sum (fun i _ => hi i)
    _ = (∑ i, (m i - 1)) + M * (∑ i, q i) := by
      rw [Finset.sum_add_distrib, Finset.mul_sum]
    _ ≤ (∑ i, (m i - 1)) + M * (r - 1) :=
      Nat.add_le_add_left (Nat.mul_le_mul_left M hqi) _
    _ = ceiling m r M := by unfold ceiling; rw [Nat.mul_comm M]

section Extremal
variable [DecidableEq ι]

/-- Choose the top monomial by putting all extra layers at one maximal coordinate. -/
def extremal (m : ι → ℕ) (r : ℕ) (j : ι) (i : ι) : ℕ :=
  (m i - 1) + m i * (if i = j then r - 1 else 0)

theorem extremal_admissible (m : ι → ℕ) (r : ℕ) (j : ι)
    (hm : ∀ i, 0 < m i) (hr : 0 < r) : Admissible m r (extremal m r j) := by
  refine ⟨fun i => if i = j then r - 1 else 0, fun i => m i - 1, ?_, ?_, ?_⟩
  · intro i
    change m i - 1 < m i
    have := hm i
    omega
  · exact fun _ => rfl
  · simp only [Finset.sum_ite_eq', Finset.mem_univ, if_true]
    omega

theorem extremal_degree (m : ι → ℕ) (r : ℕ) (j : ι) :
    (∑ i, extremal m r j i) = ceiling m r (m j) := by
  unfold extremal ceiling
  rw [Finset.sum_add_distrib]
  congr 1
  calc
    (∑ i, m i * (if i = j then r - 1 else 0)) =
        ∑ i, (if i = j then m j * (r - 1) else 0) := by
      apply Finset.sum_congr rfl
      intro i _
      by_cases h : i = j
      · subst i; simp
      · simp [h]
    _ = m j * (r - 1) := by simp
    _ = (r - 1) * m j := Nat.mul_comm _ _

theorem attained_maximum (m : ι → ℕ) (r : ℕ) (j : ι)
    (hm : ∀ i, 0 < m i) (hr : 0 < r) (hmax : ∀ i, m i ≤ m j) :
    (∀ a, Admissible m r a → (∑ i, a i) ≤ ceiling m r (m j)) ∧
      ∃ a, Admissible m r a ∧ (∑ i, a i) = ceiling m r (m j) := by
  constructor
  · exact fun a ha => degree_le m a r (m j) hmax ha
  · exact ⟨extremal m r j, extremal_admissible m r j hm hr, extremal_degree m r j⟩

omit [DecidableEq ι] in
theorem floor_attained_maximum (m : ι → ℕ) (r : ℕ) (j : ι)
    (hm : ∀ i, 0 < m i) (hr : 0 < r) (hmax : ∀ i, m i ≤ m j) :
    (∀ a : ι → ℕ, (∑ i, a i / m i) < r → (∑ i, a i) ≤ ceiling m r (m j)) ∧
      ∃ a : ι → ℕ, (∑ i, a i / m i) < r ∧ (∑ i, a i) = ceiling m r (m j) := by
  classical
  obtain ⟨hb, a, ha, hd⟩ := attained_maximum m r j hm hr hmax
  exact ⟨fun a ha => hb a (admissible_of_floor_sum m a r hm ha),
    a, floor_sum_of_admissible m a r ha, hd⟩
end Extremal

/-- Local nilpotency order, before taking a maximum over collided root tuples. -/
def localOrder (m : ι → ℕ) (r M : ℕ) : ℕ := ceiling m r M + 1

theorem localOrder_step (m : ι → ℕ) (r M : ℕ) (hr : 0 < r) :
    localOrder m (r + 1) M = localOrder m r M + M := by
  have hr' : r = r - 1 + 1 := by omega
  have hm : r * M = (r - 1) * M + M := by
    simpa only [Nat.add_mul, Nat.one_mul] using congrArg (fun n => n * M) hr'
  unfold localOrder ceiling
  rw [Nat.add_sub_cancel, hm]
  omega

end SplitZero.CyclicDepth
