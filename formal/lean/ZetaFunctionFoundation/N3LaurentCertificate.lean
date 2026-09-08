import Mathlib.Data.Fin.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic.Ring

/-!
# Exact finite Laurent certificate at N = 3

This file formalizes the finite algebraic content of `FORMAL-20260825-0008`.
Each Laurent exponent is the displayed triple in `Z^3`.  A polynomial is a
finite list of exponent/coefficient contributions.  `collectTerms` combines
equal exponents only for executable efficiency, and the theorem
`coefficient_collectTerms` proves that this collection preserves every
coefficient exactly.  No analytic Haar-integration theorem, asymptotic claim,
or zeta-zero assertion is imported here.
-/

namespace ZetaFunctionFoundation

/-- A Laurent exponent with all three integer coordinates displayed. -/
abbrev Exponent3 := Int × Int × Int

/-- One exact exponent/coefficient contribution. -/
abbrev LaurentTerm := Exponent3 × Int

/-- A finite Laurent expression, retaining a finite contribution list. -/
abbrev Laurent3 := List LaurentTerm

def exponentZero : Exponent3 := (0, 0, 0)

def exponentAdd (a b : Exponent3) : Exponent3 :=
  (a.1 + b.1, a.2.1 + b.2.1, a.2.2 + b.2.2)

def exponentNeg (a : Exponent3) : Exponent3 := (-a.1, -a.2.1, -a.2.2)

def unitExponent : Fin 3 -> Exponent3
  | 0 => (1, 0, 0)
  | 1 => (0, 1, 0)
  | 2 => (0, 0, 1)

/-- Contribution of one term to one displayed exponent coordinate. -/
def termCoefficient (t : LaurentTerm) (e : Exponent3) : Int :=
  if t.1 = e then t.2 else 0

/-- The exact coefficient obtained by summing every matching contribution. -/
def coefficient (f : Laurent3) (e : Exponent3) : Int :=
  (f.map fun t => termCoefficient t e).sum

@[simp] theorem coefficient_nil (e : Exponent3) : coefficient [] e = 0 := rfl

@[simp] theorem coefficient_cons (t : LaurentTerm) (f : Laurent3) (e : Exponent3) :
    coefficient (t :: f) e = termCoefficient t e + coefficient f e := by
  rfl

/-- Insert one contribution, collecting it with the first equal exponent. -/
def insertTerm (t : LaurentTerm) : Laurent3 -> Laurent3
  | [] => [t]
  | u :: us =>
      if t.1 = u.1 then (u.1, t.2 + u.2) :: us
      else u :: insertTerm t us

theorem coefficient_insertTerm (t : LaurentTerm) (f : Laurent3) (e : Exponent3) :
    coefficient (insertTerm t f) e =
      coefficient f e + (if t.1 = e then t.2 else 0) := by
  induction f with
  | nil =>
      simp [insertTerm, coefficient, termCoefficient]
  | cons u us ih =>
      by_cases htu : t.1 = u.1
      · by_cases hue : u.1 = e
        · have hte : t.1 = e := htu.trans hue
          rw [insertTerm, if_pos htu, coefficient_cons, coefficient_cons]
          simp [termCoefficient, hue, hte]
          ring
        · have hte : t.1 ≠ e := by simpa [htu] using hue
          rw [insertTerm, if_pos htu, coefficient_cons, coefficient_cons]
          simp [termCoefficient, hue, hte]
      · rw [insertTerm, if_neg htu, coefficient_cons, ih, coefficient_cons]
        ring

/-- Coefficient-preserving collection of equal-exponent contributions. -/
def collectTerms (f : Laurent3) : Laurent3 :=
  f.foldl (fun acc t => insertTerm t acc) []

theorem coefficient_foldl_insertTerm
    (f acc : Laurent3) (e : Exponent3) :
    coefficient (f.foldl (fun a t => insertTerm t a) acc) e =
      coefficient acc e + coefficient f e := by
  induction f generalizing acc with
  | nil => simp [coefficient]
  | cons t ts ih =>
      rw [List.foldl_cons, ih]
      rw [coefficient_insertTerm, coefficient_cons]
      simp only [termCoefficient]
      ring

theorem coefficient_collectTerms (f : Laurent3) (e : Exponent3) :
    coefficient (collectTerms f) e = coefficient f e := by
  rw [collectTerms, coefficient_foldl_insertTerm]
  simp [coefficient]

def laurentOne : Laurent3 := [(exponentZero, 1)]

def laurentAdd (f g : Laurent3) : Laurent3 := collectTerms (f ++ g)

def laurentNeg (f : Laurent3) : Laurent3 := f.map fun t => (t.1, -t.2)

def laurentSub (f g : Laurent3) : Laurent3 := laurentAdd f (laurentNeg g)

def laurentScale (c : Int) (f : Laurent3) : Laurent3 :=
  f.map fun t => (t.1, c * t.2)

/-- Raw convolution contributions before coefficient-preserving collection. -/
def rawLaurentMul (f g : Laurent3) : Laurent3 :=
  f.flatMap fun a => g.map fun b => (exponentAdd a.1 b.1, a.2 * b.2)

def laurentMul (f g : Laurent3) : Laurent3 := collectTerms (rawLaurentMul f g)

theorem coefficient_laurentMul (f g : Laurent3) (e : Exponent3) :
    coefficient (laurentMul f g) e = coefficient (rawLaurentMul f g) e := by
  exact coefficient_collectTerms _ _

def laurentPow (f : Laurent3) : Nat -> Laurent3
  | 0 => laurentOne
  | q + 1 => laurentMul (laurentPow f q) f

def z (i : Fin 3) : Laurent3 := [(unitExponent i, 1)]

def zInv (i : Fin 3) : Laurent3 := [(exponentNeg (unitExponent i), 1)]

/-- Exponent reflection `alpha |-> -alpha`, term by term. -/
def reflectExponent (f : Laurent3) : Laurent3 :=
  f.map fun t => (exponentNeg t.1, t.2)

theorem exponentNeg_involutive (e : Exponent3) :
    exponentNeg (exponentNeg e) = e := by
  rcases e with ⟨a, b, c⟩
  simp [exponentNeg]

theorem reflectExponent_coeff (f : Laurent3) (e : Exponent3) :
    coefficient (reflectExponent f) e = coefficient f (exponentNeg e) := by
  induction f with
  | nil => simp [reflectExponent, coefficient]
  | cons t ts ih =>
      change termCoefficient (exponentNeg t.1, t.2) e +
          coefficient (reflectExponent ts) e =
        termCoefficient t (exponentNeg e) + coefficient ts (exponentNeg e)
      rw [ih]
      by_cases h : exponentNeg t.1 = e
      · have h' : t.1 = exponentNeg e := by
          calc
            t.1 = exponentNeg (exponentNeg t.1) := (exponentNeg_involutive t.1).symm
            _ = exponentNeg e := congrArg exponentNeg h
        rw [termCoefficient, termCoefficient, if_pos h, if_pos h']
      · have h' : t.1 ≠ exponentNeg e := by
          intro he
          apply h
          calc
            exponentNeg t.1 = exponentNeg (exponentNeg e) := congrArg exponentNeg he
            _ = e := exponentNeg_involutive e
        rw [termCoefficient, termCoefficient, if_neg h, if_neg h']

/-- `Phi_3'(1) = 3 - 2 e_1 + e_2`, with all seven terms displayed. -/
def derivativePolynomial : Laurent3 :=
  [ (exponentZero, 3),
    (unitExponent 0, -2),
    (unitExponent 1, -2),
    (unitExponent 2, -2),
    (exponentAdd (unitExponent 0) (unitExponent 1), 1),
    (exponentAdd (unitExponent 0) (unitExponent 2), 1),
    (exponentAdd (unitExponent 1) (unitExponent 2), 1) ]

/-- Torus conjugation/inversion, coefficientwise `pInv_alpha = p_(-alpha)`. -/
def derivativePolynomialInv : Laurent3 := reflectExponent derivativePolynomial

theorem derivativePolynomialInv_coeff (e : Exponent3) :
    coefficient derivativePolynomialInv e =
      coefficient derivativePolynomial (exponentNeg e) := by
  exact reflectExponent_coeff derivativePolynomial e

def laurentFactor (a b : Fin 3) : Laurent3 :=
  laurentSub laurentOne (laurentMul (z a) (zInv b))

/-- The six retained Weyl-density factors for `U(3)`. -/
def weylDensity3 : Laurent3 :=
  laurentMul
    (laurentMul
      (laurentMul
        (laurentMul
          (laurentMul (laurentFactor 0 1) (laurentFactor 1 0))
          (laurentFactor 0 2))
        (laurentFactor 2 0))
      (laurentFactor 1 2))
    (laurentFactor 2 1)

/-- The integer numerator before exact division by `3! = 6`. -/
def n3MomentNumerator (q : Nat) : Int :=
  coefficient
    (laurentMul
      (laurentMul (laurentPow derivativePolynomial q)
        (laurentPow derivativePolynomialInv q))
      weylDensity3)
    exponentZero

/-- Exact numerator evaluations via Lean's `native_decide`; the compiler trust boundary is
recorded in the replay receipt and is independently backed by the two non-Lean exact replays. -/
theorem n3MomentNumerators :
    n3MomentNumerator 1 = 84 ∧
    n3MomentNumerator 2 = 2250 ∧
    n3MomentNumerator 3 = 93060 ∧
    n3MomentNumerator 4 = 5083680 ∧
    n3MomentNumerator 5 = 331988544 := by
  native_decide

/-- Exact division by `6`, stated coordinate by coordinate rather than hidden in a list. -/
theorem n3MomentValues :
    n3MomentNumerator 1 / 6 = 14 ∧
    n3MomentNumerator 2 / 6 = 375 ∧
    n3MomentNumerator 3 / 6 = 15510 ∧
    n3MomentNumerator 4 / 6 = 847280 ∧
    n3MomentNumerator 5 / 6 = 55331424 := by
  rcases n3MomentNumerators with ⟨h1, h2, h3, h4, h5⟩
  simp [h1, h2, h3, h4, h5]

/-- Every computed numerator is exactly divisible by `6`. -/
theorem n3MomentNumerators_mod_six :
    n3MomentNumerator 1 % 6 = 0 ∧
    n3MomentNumerator 2 % 6 = 0 ∧
    n3MomentNumerator 3 % 6 = 0 ∧
    n3MomentNumerator 4 % 6 = 0 ∧
    n3MomentNumerator 5 % 6 = 0 := by
  rcases n3MomentNumerators with ⟨h1, h2, h3, h4, h5⟩
  simp [h1, h2, h3, h4, h5]

end ZetaFunctionFoundation
