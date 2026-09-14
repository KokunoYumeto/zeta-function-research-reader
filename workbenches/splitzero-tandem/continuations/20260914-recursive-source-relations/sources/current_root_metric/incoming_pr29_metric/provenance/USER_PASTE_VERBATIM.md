**The current baseline is now the merged PR #29: the residue-detection theorem, canonical metric-variation identities, signed arithmetic/Gamma certificate, and their original SplitZero quotient maps are together in main.** It merged while I was working. I checked the merge against the reviewed implementation: the intervening changes were publication/index files, not alterations to those mathematical sources. The successful implementation run remains `34772920706`; I am not claiming a new compilation in this turn.

I continued from that implementation and derived two results directly relevant to the remaining estimate:

**First, one certified comparison of the original source moment matrices controls the error in the entire four-endpoint quantity. Second, the signed arithmetic correction is a single trace pairing with a traceless combination of four actual source projectors.** The latter retains cancellations that are lost when the four determinants are bounded separately.

These are complete mathematical derivations below. The accompanying Lean continuation uses the existing implementation, but remains **uncompiled** because the execution runtime is failing. The same failure prevented extraction of the new ZIP; I have not represented its contents as read or integrated. The current GitHub connection also exposes no write operation, so no new remote change is claimed.

## 1. One source-matrix enclosure controls all four endpoints

Fix the actual packet and tensor degree, retaining

$$
g=2\xi,\qquad
\mathcal MF_h=g/h,\qquad
E=\mathbb C[S]/(\chi_{h,k}),\qquad
q=\deg\chi_{h,k}\ge1.
$$

The source map and full arithmetic observation remain

$$
\mathcal V_{h,k}P=P(D_1+\cdots+D_k)F_h^{\otimes k},
\qquad
J^{(k)}\mathcal V_{h,k}=\eta_{h,k}\pi_\chi.
$$

In particular, the Taylor unit inside \(\eta_{h,k}\), the original source mass, and all multiplicities remain attached. The merged metric-transfer construction uses two norms on this **same polynomial presentation**, not a new arithmetic quotient for each norm.

Let \(M_0,M_1\) be positive-definite Hermitian source matrices on the common ambient space

$$
\mathcal P_{2q}=\mathbb C[S]_{\le2q}.
$$

For each

$$
N\in\{q-1,q,2q-1,2q\},
$$

restrict the source form to \(\mathcal P_N\), and construct its canonical quotient Gram \(G_N^{(a)}\) using the unchanged relation space

$$
\chi\mathcal P_{N-q}.
$$

Write \(V_N^{(a)}=\det G_N^{(a)}\), and

$$
\mathcal B(M_a)
=
\log\frac{V_{q-1}^{(a)}V_q^{(a)}}
{V_{2q-1}^{(a)}V_{2q}^{(a)}}.
$$

**Theorem.** If

$$
0<a\le b,\qquad aM_0\preceq M_1\preceq bM_0,
$$

then

$$
\boxed{
\left|\mathcal B(M_1)-\mathcal B(M_0)\right|
\le 2q\log\frac ba.
}
\tag{1}
$$

No ordering of the two arithmetic quotient metrics relative to one another is presumed beyond what follows from the stated source comparison.

### The proof retains the actual boundary correction

At any one admitted degree, let \(B\) contain the original relation columns and \(C\) fixed lifts of the quotient basis. The merged implementation constructs

$$
R_a=C-B(B^*M_aB)^{-1}B^*M_aC,
\qquad
G_a=R_a^*M_aR_a.
$$

Put

$$
\Delta=R_1-R_0.
$$

The existing theorem supplies its explicit original-relation primitive:

$$
\boxed{
\Delta
=
B\left[
(B^*M_0B)^{-1}B^*M_0C
-
(B^*M_1B)^{-1}B^*M_1C
\right].
}
\tag{2}
$$

It also proves the orthogonality and Pythagoras identities needed below.

Expanding with those identities gives the two scaled formulas

$$
\boxed{
G_1-aG_0
=
R_1^*(M_1-aM_0)R_1
+
a\,\Delta^*M_0\Delta,
}
\tag{3}
$$

$$
\boxed{
bG_0-G_1
=
R_0^*(bM_0-M_1)R_0
+
\Delta^*M_1\Delta.
}
\tag{4}
$$

Both right sides are positive semidefinite. Hence

$$
aG_N^{(0)}\preceq G_N^{(1)}\preceq bG_N^{(0)}
$$

at every endpoint. All \(q\) generalized eigenvalues therefore lie in \([a,b]\), giving

$$
q\log a
\le
\log\frac{V_N^{(1)}}{V_N^{(0)}}
\le
q\log b.
$$

There are two positive and two negative terms in the four-endpoint difference. Combining their correctly oriented bounds proves (1). \(\square\)

At the first degree \(N=q-1\), the relation space is zero-dimensional and \(\Delta=0\). The same formulas apply without introducing a preceding, inadmissible inverse.

### A usable consequence for certified arithmetic moments

Suppose \(\widehat M\) is an approximate source matrix and the actual arithmetic matrix satisfies a certified relative enclosure

$$
(1-\varepsilon_M)\widehat M
\preceq M
\preceq
(1+\varepsilon_M)\widehat M,
\qquad 0\le\varepsilon_M<1.
$$

Then

$$
\boxed{
\left|\mathcal B(M)-\mathcal B(\widehat M)\right|
\le
2q\log\frac{1+\varepsilon_M}{1-\varepsilon_M}.
}
\tag{5}
$$

Thus **one enclosure on the common degree-\(2q\) source propagates to all four canonical quotient metrics together**. Separate numerical logarithms of four poorly conditioned determinants are not required to justify their combined error.

For fixed \(\varepsilon_M<1\), the error in (5) is \(O(q)\), below the programme’s \(q\log k\) comparison scale. Establishing that relative source enclosure may still require substantial arithmetic precision; the theorem does not conceal that task.

The bound is also insensitive to a common scalar: replacing \(M_1\) by \(cM_1\) scales every \(q\)-dimensional quotient determinant by \(c^q\), which cancels in \(\mathcal B\). That is an explicit cancellation in the observation, not a normalization of the original source.

## 2. The signed correction is one operator pairing, not four unrelated estimates

The merged note already proves the first variation of a canonical quotient metric along the source pencil. I used that formula to assemble the four endpoints **before** estimating them.

Use a new parameter \(s\in[0,1]\):

$$
M_s=(1-s)M_\Gamma+sM_{\mathrm{ar}},
\qquad
\dot M=M_{\mathrm{ar}}-M_\Gamma.
$$

This is a comparison path between the two specified source forms. Its intermediate points are not asserted to be convolutions of an interpolated one-factor arithmetic amplitude.

Pad every canonical representative into the common source \(\mathcal P_{2q}\):

$$
\rho_N(s):E\longrightarrow\mathcal P_{2q},
\qquad
G_N(s)=\rho_N(s)^*M_s\rho_N(s).
$$

Define the **weighted source projector**

$$
P_N(s)
=
\rho_N(s)G_N(s)^{-1}\rho_N(s)^*M_s.
$$

It obeys

$$
P_N^2=P_N,\qquad
P_N^*M_s=M_sP_N,\qquad
\operatorname{Tr}P_N=q.
$$

It need not be Hermitian in the unweighted coordinate metric.

Now set

$$
X_s=M_s^{-1}\dot M,
$$

and form the single signed projector combination

$$
\boxed{
Q_s=P_{q-1}(s)+P_q(s)-P_{2q-1}(s)-P_{2q}(s).
}
\tag{6}
$$

Its trace is exactly zero.

**Theorem.**

$$
\boxed{
\frac d{ds}\mathcal B(M_s)=\operatorname{Tr}(X_sQ_s).
}
\tag{7}
$$

Consequently, the original signed arithmetic/Gamma correction is

$$
\boxed{
\mathcal C_{h,k}
:=
\mathcal B(M_{\mathrm{ar}})-\mathcal B(M_\Gamma)
=
\int_0^1\operatorname{Tr}(X_sQ_s)\,ds.
}
\tag{8}
$$

### Proof

The quotient observation is fixed:

$$
\pi_\chi R_N(s)=I_E.
$$

Therefore \(R_N'(s)\) is an original polynomial relation. Canonical orthogonality removes both cross terms when differentiating its Gram:

$$
G_N'(s)=\rho_N(s)^*\dot M\,\rho_N(s).
$$

Jacobi’s formula and cyclicity of trace give

$$
\begin{aligned}
\frac d{ds}\log\det G_N(s)
&=\operatorname{Tr}\!\left(
G_N^{-1}\rho_N^*\dot M\,\rho_N
\right)\\
&=\operatorname{Tr}(X_sP_N(s)).
\end{aligned}
$$

Add the four terms with their original signs and integrate. \(\square\)

This is an operator form of the signed density contrast in the merged note. It keeps the complete arithmetic source variation rather than replacing it by a positive envelope.

In particular, for every real scalar \(c_s\),

$$
\boxed{
\operatorname{Tr}(X_sQ_s)
=
\operatorname{Tr}\bigl((X_s-c_sI)Q_s\bigr).
}
\tag{9}
$$

The common scalar part of the source variation contributes nothing. **Only its nonscalar part, paired with the specified four-projector difference, changes the endpoint contrast.**

That matters when transporting coefficient errors or comparing Gamma and arithmetic moments: a large common mass factor need not be a large error in the desired quantity.

## 3. Its size is controlled by the existing restriction-loss data

For \(i\le j\), retain the original reverse restriction

$$
T_{i,j}=G_i^{-1}G_j.
$$

The source cross-Gram identity is

$$
\rho_j^*M_s\rho_i=G_j.
$$

It follows that

$$
\operatorname{Tr}(P_iP_j)=\operatorname{Tr}(G_i^{-1}G_j),
$$

and hence

$$
\boxed{
\operatorname{Tr}\bigl((P_i-P_j)^2\bigr)
=
2\operatorname{Tr}(I-T_{i,j}).
}
\tag{10}
$$

This is attached to the same representative restriction whose matrix and original boundary were already constructed; it does not identify its eigenspaces with arithmetic invariant subspaces. 

For the two endpoint pairs, write

$$
Q_s^{(0)}=P_{q-1}-P_{2q-1},
\qquad
Q_s^{(1)}=P_q-P_{2q},
$$

$$
s_1^{(0)}=\operatorname{Tr}(I-T_{q-1,2q-1}),
\qquad
s_1^{(1)}=\operatorname{Tr}(I-T_{q,2q}).
$$

Equation (10) gives the exact identity

$$
\boxed{
\operatorname{Tr}(Q_s^2)
=
2s_1^{(0)}+2s_1^{(1)}
+
2\operatorname{Tr}\!\left(Q_s^{(0)}Q_s^{(1)}\right).
}
\tag{11}
$$

The cross term stays. It is not assigned a favorable sign.

For a coarser bound,

$$
\operatorname{Tr}(Q_s^2)
\le4\bigl(s_1^{(0)}+s_1^{(1)}\bigr).
\tag{12}
$$

To justify the positivity and the inequality, conjugate all operators simultaneously by \(M_s^{1/2}\). The weighted-self-adjoint operators become Hermitian, and (12) is

$$
\|Q^{(0)}+Q^{(1)}\|_{\mathrm{HS}}^2
\le2\|Q^{(0)}\|_{\mathrm{HS}}^2
+2\|Q^{(1)}\|_{\mathrm{HS}}^2.
$$

This conjugation is a proof calculation carrying the original metric; it is not a replacement of the canonical metric.

Let \(d=\dim\mathcal P_{2q}=2q+1\), and define

$$
c_s=\frac{\operatorname{Tr}X_s}{d},
\qquad
\Sigma_s
=
\operatorname{Tr}(X_s^2)
-\frac{(\operatorname{Tr}X_s)^2}{d}
\ge0.
$$

Hilbert–Schmidt Cauchy–Schwarz, applied after that same conjugation, proves

$$
\boxed{
\left|\frac d{ds}\mathcal B(M_s)\right|
\le
\sqrt{\Sigma_s\,\operatorname{Tr}(Q_s^2)}
\le
2\sqrt{\Sigma_s\bigl(s_1^{(0)}+s_1^{(1)}\bigr)}.
}
\tag{13}
$$

The ingredients are finite traces in the original coordinates. The first restriction moments already belong to the existing logarithmic-certificate machinery.

### Retaining the sign rather than taking absolute values

For the desired negative arithmetic correction, (13) alone is not sufficient. A useful signed version is available.

Take a specified \(M_s\)-self-adjoint approximation \(Y_s\) to \(X_s-c_sI\), and retain the actual residual

$$
E_s=X_s-c_sI-Y_s.
$$

Then

$$
\boxed{
\begin{aligned}
\operatorname{Tr}(Y_sQ_s)
-\sqrt{\operatorname{Tr}(E_s^2)\operatorname{Tr}(Q_s^2)}
&\le \frac d{ds}\mathcal B(M_s)\\
&\le
\operatorname{Tr}(Y_sQ_s)
+\sqrt{\operatorname{Tr}(E_s^2)\operatorname{Tr}(Q_s^2)}.
\end{aligned}
}
\tag{14}
$$

Integrating gives a signed enclosure for \(\mathcal C_{h,k}\).

The central term is the retained arithmetic correlation. The error term is separately bounded. Choosing \(Y_s\) does not establish the desired sign unless its residual is actually controlled.

This supplies a concrete continuation target for the arithmetic coefficient work:

$$
\int_0^1
\left[
\operatorname{Tr}(Y_sQ_s)
+
\sqrt{\operatorname{Tr}(E_s^2)\operatorname{Tr}(Q_s^2)}
\right]ds.
$$

It uses the original four endpoints jointly and preserves the direction of the estimate.

## 4. The next Lean addition uses the merged implementation

The following proposed `SplitZeroMetricSandwich.lean` is written against the actual `MetricVariation.Metric` interface I retrieved. It proves (3)–(4), their positive-semidefinite consequence, and packages that consequence with equality in the **existing reconstructed quotient**.

It imports `SplitZeroMetricVariationSupport`, whose `canonical_metric_class` theorem already uses the explicit relation primitive and the original `Relations.quotientDiagram`. It does not replace original boundaries by the entire kernel of a finite observation.

**This is a complete proof-script draft, not a compiled certificate.**

```lean
import SplitZeroMetricVariationSupport

/-!
Source-metric bounds for the original canonical quotient.

B and C remain fixed. Every comparison retains the explicit
old-boundary difference between the two canonical sections.
-/

noncomputable section

namespace SplitZero.MetricSandwich

open Matrix MetricVariation Reconstruction

variable {j n m : Type*}
  [Fintype j] [Fintype n] [Fintype m] [DecidableEq m]
  {B : Matrix j m ℂ}

/-- The lower scaled comparison, including its original boundary Gram. -/
theorem lower_identity
    (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (a : ℝ) :
    M₁.quotientGram C - a • M₀.quotientGram C =
      gram (M₁.form - a • M₀.form) (M₁.sectionMap C) +
        a • gram M₀.form
          (M₁.sectionMap C - M₀.sectionMap C) := by
  have hexpand :
      gram (M₁.form - a • M₀.form) (M₁.sectionMap C) =
        M₁.quotientGram C -
          a • gram M₀.form (M₁.sectionMap C) := by
    simp only [gram, Metric.quotientGram,
      Matrix.mul_sub, Matrix.sub_mul,
      Matrix.mul_smul, Matrix.smul_mul]
  rw [hexpand, Metric.pythagoras M₀ M₁ C, smul_add]
  abel

/-- The upper scaled comparison uses the other source metric on the boundary. -/
theorem upper_identity
    (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (b : ℝ) :
    b • M₀.quotientGram C - M₁.quotientGram C =
      gram (b • M₀.form - M₁.form) (M₀.sectionMap C) +
        gram M₁.form
          (M₁.sectionMap C - M₀.sectionMap C) := by
  have hneg :
      gram M₁.form
          (M₀.sectionMap C - M₁.sectionMap C) =
        gram M₁.form
          (M₁.sectionMap C - M₀.sectionMap C) := by
    have he :
        M₀.sectionMap C - M₁.sectionMap C =
          -(M₁.sectionMap C - M₀.sectionMap C) := by
      abel
    rw [he]
    simp only [gram, Matrix.conjTranspose_neg,
      Matrix.neg_mul, Matrix.mul_neg, neg_neg]
  have hexpand :
      gram (b • M₀.form - M₁.form) (M₀.sectionMap C) =
        b • M₀.quotientGram C -
          gram M₁.form (M₀.sectionMap C) := by
    simp only [gram, Metric.quotientGram,
      Matrix.mul_sub, Matrix.sub_mul,
      Matrix.mul_smul, Matrix.smul_mul]
  rw [hexpand, Metric.pythagoras M₁ M₀ C, hneg]
  abel

/-- A source sandwich descends to the canonical quotient Grams. -/
theorem sandwich
    (M₀ M₁ : Metric B) (C : Matrix j n ℂ) (a b : ℝ)
    (ha : 0 ≤ a)
    (hM₀ : M₀.form.PosSemidef)
    (hM₁ : M₁.form.PosSemidef)
    (hLower : (M₁.form - a • M₀.form).PosSemidef)
    (hUpper : (b • M₀.form - M₁.form).PosSemidef) :
    (M₁.quotientGram C - a • M₀.quotientGram C).PosSemidef ∧
      (b • M₀.quotientGram C - M₁.quotientGram C).PosSemidef := by
  constructor
  · rw [lower_identity]
    exact (hLower.conjTranspose_mul_mul_same _).add
      ((hM₀.conjTranspose_mul_mul_same _).smul ha)
  · rw [upper_identity]
    exact (hUpper.conjTranspose_mul_mul_same _).add
      (hM₁.conjTranspose_mul_mul_same _)

variable {L : Type*} [SemilatticeSup L] [OrderBot L]
  {D : LinearDiagram ℂ L}

/-- The metric bounds accompany equality in the ORIGINAL supported quotient. -/
theorem supported_sandwich
    (Brel : Relations D) (i : L)
    (coord : D.V i ≃ₗ[ℂ] (j → ℂ))
    (C : Matrix j n ℂ) (M₀ M₁ : Metric B)
    (hB : ∀ w, coord.symm (B *ᵥ w) ∈ Brel.fibre i)
    (v : n → ℂ) (a b : ℝ)
    (ha : 0 ≤ a)
    (hM₀ : M₀.form.PosSemidef)
    (hM₁ : M₁.form.PosSemidef)
    (hLower : (M₁.form - a • M₀.form).PosSemidef)
    (hUpper : (b • M₀.form - M₁.form).PosSemidef) :
    Brel.quotientMap.total
        ⟨i, coord.symm (M₁.sectionMap C *ᵥ v)⟩ =
      Brel.quotientMap.total
        ⟨i, coord.symm (M₀.sectionMap C *ᵥ v)⟩ ∧
    (M₁.quotientGram C - a • M₀.quotientGram C).PosSemidef ∧
    (b • M₀.quotientGram C - M₁.quotientGram C).PosSemidef := by
  exact ⟨
    MetricVariationSupport.canonical_metric_class
      Brel i coord B C M₀ M₁ hB v,
    sandwich M₀ M₁ C a b ha hM₀ hM₁ hLower hUpper⟩

end SplitZero.MetricSandwich
```

The determinant/logarithm consequence (1), the projector-variation theorem (7), and the signed estimate (14) have the complete written proofs above. They are not silently included in this draft’s formal scope.

The positive-semidefinite operations used in the draft are the existing Mathlib congruence, addition, and nonnegative-scalar operations; the source code already uses that interface.  ([Lean Community][1])

## 5. What was independently checked in this turn

I executed new exact Wolfram calculations on canonical polynomial quotients, including

$$
\chi(S)=(S-\tfrac12)^2,\qquad
\chi(S)=1+(S-\tfrac12)^2,\qquad
\chi(S)=(S-\tfrac12)^3.
$$

The reference measure was a Gaussian of literal mass seven. The second measure multiplied it by

$$
2+2x+x^2=1+(x+1)^2>0.
$$

Its mass is therefore twenty-one. These are declared finite calibration examples, not claimed zeta-zero packets.

The checks constructed the moment matrices and canonical representatives rather than assigning quotient Grams. They verified both scaled identities, both Gram inequalities, and the actual polynomial primitive of every section difference at all four endpoints. They also verified the repeated-root cases, the zero-dimensional relation space at the first degree, and invariance of the section under common mass scaling.

For the two quadratic fixtures, independent symbolic differentiation of the determinant ratio agreed with \(\operatorname{Tr}(X_sQ_s)\). At \(s=0,\frac13,\frac12,1\), the weighted projector laws, trace cancellation, restriction-loss identity (10), and centered Cauchy–Schwarz bound all passed exactly. The source matrices did not commute. Reversing the sign of the retained boundary Gram failed in every tested case with a nonzero correction.

These computations support the new derivation. They are **not** a substitute for Lean compilation or certified arithmetic integration.

The new ZIP remains an explicit intake gap: it has no readable indexed text, and both container execution interfaces timed out before extraction. I therefore cannot yet reconcile these results with that package’s precise theorem statements or claim independent verification of its manifest and tests. The work above is grounded in the retrieved GitHub sources and the already-readable programme notes.

**The continuation now has a source-level error bound for the complete endpoint quantity and a joint, signed operator formula for its arithmetic correction.** The next arithmetic estimate can be applied to \(\operatorname{Tr}(X_sQ_s)\), with common scalar changes removed exactly and the restriction losses retained. Neither an auxiliary counterexample nor an unsigned positivity statement is being used to decide the programme’s outcome.

[1]: https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/PosDef.html?utm_source=chatgpt.com "Mathlib.LinearAlgebra.Matrix.PosDef"
