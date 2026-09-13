import SplitZeroRestrictionTransport

/-!
The original source matrices are retained, including all monic norms.
Rectangular matrices keep the source, cyclic quotient and padding types separate.
-/
noncomputable section
namespace SplitZero.Restriction
open Matrix
variable {ι σ τ : Type*}
  [Fintype ι] [DecidableEq ι] [Fintype σ] [DecidableEq σ]
  [Fintype τ] [DecidableEq τ]

def sourceKernel (B : Matrix ι σ ℂ) (Oinv : Matrix σ σ ℂ) : Matrix ι ι ℂ :=
  B * Oinv * B.conjTranspose

def representative (B : Matrix ι σ ℂ) (Oinv : Matrix σ σ ℂ)
    (G : Matrix ι ι ℂ) : Matrix σ ι ℂ := Oinv * B.conjTranspose * G

omit [DecidableEq σ] in
/-- Surjectivity is verified by the original kernel/Gram inverse equation. -/
theorem representative_section (B : Matrix ι σ ℂ) (Oinv : Matrix σ σ ℂ)
    (G : Matrix ι ι ℂ) (h : sourceKernel B Oinv * G = 1) :
    B * representative B Oinv G = 1 := by
  simpa only [sourceKernel, representative, Matrix.mul_assoc] using h

omit [DecidableEq ι] in
/-- The least-norm dual identity, in the original source metric O. -/
theorem representative_adjoint (B : Matrix ι σ ℂ) (O Oinv : Matrix σ σ ℂ)
    (G : Matrix ι ι ℂ) (hInv : Oinv * O = 1)
    (hOi : Oinv.conjTranspose = Oinv) (hG : G.conjTranspose = G) :
    (representative B Oinv G).conjTranspose * O = G * B := by
  simp only [representative, Matrix.conjTranspose_mul,
    Matrix.conjTranspose_conjTranspose, hOi, hG, Matrix.mul_assoc,
    hInv, Matrix.mul_one]

/-- The constructed representative has the supplied canonical quotient Gram. -/
theorem representative_gram (B : Matrix ι σ ℂ) (O Oinv : Matrix σ σ ℂ)
    (G : Matrix ι ι ℂ) (hInv : Oinv * O = 1)
    (hOi : Oinv.conjTranspose = Oinv) (hG : G.conjTranspose = G)
    (hKG : sourceKernel B Oinv * G = 1) :
    (representative B Oinv G).conjTranspose * O * representative B Oinv G = G := by
  rw [representative_adjoint B O Oinv G hInv hOi hG, Matrix.mul_assoc,
    representative_section B Oinv G hKG, Matrix.mul_one]

omit [DecidableEq σ] [DecidableEq τ] in
/-- Restriction of dual columns yields restriction of the canonical source lift.
The cutoff identity is an identity of the raw weighted columns, not the conclusion.
For diagonal monic norms it is literal extraction of the first source coordinates.
-/
theorem source_restriction (Ci : Matrix σ ι ℂ) (Cj : Matrix τ ι ℂ)
    (L : Matrix τ σ ℂ) (P : Matrix τ τ ℂ) (Gi Ki Gj : Matrix ι ι ℂ)
    (hcut : P * Cj = L * Ci) (hi : Gi * Ki = 1) :
    L * (Ci * Gi) * returnMap Ki Gj = P * (Cj * Gj) := by
  unfold returnMap
  calc
    _ = L * Ci * (Gi * Ki) * Gj := by simp only [Matrix.mul_assoc]
    _ = (L * Ci) * Gj := by rw [hi]; simp
    _ = P * (Cj * Gj) := by rw [← hcut]; simp only [Matrix.mul_assoc]

/-- The two pieces of the original relation remain separately available. -/
theorem relation_decomposition (X R : Matrix σ ι ℂ)
    (P : Matrix σ σ ℂ) (T : Matrix ι ι ℂ) (h : P * R = X * T) :
    X - R = X * (1 - T) - (1 - P) * R := by
  simp only [Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_one, Matrix.one_mul]
  rw [h]
  abel

/-- Both pieces have the same original arithmetic image. -/
theorem relation_observations (B : Matrix ι σ ℂ) (X R : Matrix σ ι ℂ)
    (P : Matrix σ σ ℂ) (T : Matrix ι ι ℂ)
    (hX : B * X = 1) (hR : B * R = 1) (h : P * R = X * T) :
    B * (X * (1 - T)) = 1 - T ∧
    B * ((1 - P) * R) = 1 - T ∧ B * (X - R) = 0 := by
  constructor
  · rw [← Matrix.mul_assoc, hX, Matrix.one_mul]
  constructor
  · rw [Matrix.sub_mul, Matrix.one_mul, h, Matrix.mul_sub,
      ← Matrix.mul_assoc, hR, hX, Matrix.one_mul]
  · simp only [Matrix.mul_sub, hX, hR, sub_self]

omit [DecidableEq σ] in
/-- Difference-of-representatives energy is the canonical metric loss.
The cross Gram is derived from the source dual equation and original observations.
-/
theorem relation_gram (B : Matrix ι σ ℂ) (O : Matrix σ σ ℂ)
    (X R : Matrix σ ι ℂ) (Gi Gj : Matrix ι ι ℂ)
    (hO : O.conjTranspose = O) (hGj : Gj.conjTranspose = Gj)
    (hX : B * X = 1) (hR : B * R = 1)
    (hGram : X.conjTranspose * O * X = Gi)
    (hDual : R.conjTranspose * O = Gj * B) :
    (X - R).conjTranspose * O * (X - R) = Gi - Gj := by
  have hRX : R.conjTranspose * O * X = Gj := by
    rw [hDual, Matrix.mul_assoc, hX, Matrix.mul_one]
  have hRR : R.conjTranspose * O * R = Gj := by
    rw [hDual, Matrix.mul_assoc, hR, Matrix.mul_one]
  have hXR : X.conjTranspose * O * R = Gj := by
    have hh := congrArg Matrix.conjTranspose hRX
    simpa only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
      hO, hGj, Matrix.mul_assoc] using hh
  calc
    _ = X.conjTranspose * O * X - X.conjTranspose * O * R -
        (R.conjTranspose * O * X - R.conjTranspose * O * R) := by
      simp only [Matrix.conjTranspose_sub, Matrix.sub_mul, Matrix.mul_sub]
      abel
    _ = Gi - Gj := by rw [hGram, hXR, hRX, hRR]; abel

omit [Fintype ι] [DecidableEq ι] [Fintype σ] [DecidableEq σ] in
/-- Three stages retain the additive relation itself, not just its determinant. -/
theorem relation_cocycle (X Y Z : Matrix σ ι ℂ) :
    X - Z = (X - Y) + (Y - Z) := by abel

end SplitZero.Restriction
