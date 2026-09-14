# Review of the shared exponential-period and translation proofs

Date: 13 September 2026. Result: bounded mathematical acceptance of the
two written proofs identified below. This is a source review plus independent
finite regression, not a new Lean certificate or an arithmetic asymptotic bound.

## Exact inputs and reading extent

The parent read both owner TeX files completely, not excerpts:

- `deligne_exponential_determinant_extension_20260913.tex`, XD1–26,
  9,616 bytes, SHA-256
  `4a6b6c237ca3cff29abceba6cb5f8285e080b080c5f923f0e09d6f130a30dfe8`.
- `deligne_translation_bridge_20260913.tex`, DT1–13 and all surrounding
  proofs, 14,083 bytes, SHA-256
  `39163624c54704c203a69481ff4d7df4262afa108ac1e0989171d5ba8d700c42`.

Both source files reside in the owning mathematics task's `work` directory.
They were read-only inputs. Their authorship and proof credit remain with that
shared task; this review does not repackage the calculation as a new discovery.
The full incoming `Tau_Relation_Moment_Control/RESEARCH_NOTE.md` and
`Tau_Deligne_Exponential_Comparison/RESEARCH_NOTE.md`, together with the latter's
`SOURCE_REVIEW.md`, were also read completely. Archive/source closure and
predecessor coverage are recorded separately in the intake review.

## What the construction is for

The original finite arithmetic coefficient space is
\(E=\mathbb C[S]/(\chi)\), with multiplication \(A=M_S\). Its canonical
theta-source representative has positive Gram \(G_N\) and volume
\(V_N=\det G_N\). The research question is to estimate the change in this
volume as the admitted polynomial degree grows. The previously proved
off-line-quartet lower budget applies to these same volumes.

The exponential comparison attaches to the literal polynomial \(\chi\) its
primitive \(\Phi\), with \(\Phi(0)=0\), and the differential
\(u\partial_S+\chi(S)-t\). Its degree-one coefficient cohomology has rank
\(q=\deg\chi\); at \(u=t=0\) it is the original space \(E\). For nonzero
\(u\), integration on specified decaying ray-difference contours gives a
period matrix \(\Pi\). These are explicit comparison maps, not an identification
of the arithmetic generator with finite-field Frobenius.

## XD: determinant proof checked

1. XD4–7 give a uniform compact-parameter majorant on each unbounded ray.
   The leading term is exactly \(-r^{q+1}/((q+1)|u|)\); the stated cutoff
   makes the lower-degree terms at most half its magnitude. Polynomial
   derivatives therefore remain integrable. The two finite endpoint values
   cancel with the signs in \(\Gamma_j=-\ell_0+\ell_j\).
2. Ordinary division of \(S^{m+b}\) by \(\chi-t\), for \(1\le m\le q\),
   gives a quotient of degree at most \(q-1\). Its derivative correction
   \(-uQ'_{m,b}\) has degree strictly below column index \(b\). Thus the
   correction matrix is retained but its trace vanishes. This proves the
   connection trace identity without equating the two reduction operators.
3. For \(\mathcal F=\operatorname{Tr}\Phi_t(A(t))\), the full matrix product
   rule under the trace gives the stated differential. The matrix-derivative
   contribution is zero because \(\chi(A(t))-tI=0\), not because \(dA\)
   was discarded or because \(A\) is normal.
4. The monomial matrix retains all gamma factors, powers of \(|u|\), and
   contour phases. The root-of-unity Gram is
   \((q+1)(I+\mathbf1\mathbf1^T)\), with determinant \((q+1)^{q+1}\).
5. The adjugate determinant derivative is valid even at a putative singular
   matrix. The scalar differential equation therefore proves globally
   \[
   \det\Pi=\det\Pi_{\rm mon}\exp(\mathcal F/u),
   \]
   including repeated critical points. There is no hidden simple-root step.
6. With \(B_N^{\rm per}=G_N^{-1}\Pi^*\Pi\), the exact same period factor
   appears at both indices, giving
   \[
   \log\det B_j^{\rm per}-\log\det B_i^{\rm per}=\log(V_i/V_j).
   \]
   This retains, rather than bounds away, the original arithmetic cost.

The rank-one sign is consistent: the prescribed ray difference is downward
on \(i\mathbb R\) when \(u>0\), so its constant is
\(-i\sqrt{2\pi u}\). The incoming note's separate upward-oriented contour
has \(+i\sqrt{2\pi u}\). They are not conflicting calculations.

## DT: translation proof checked

The literal substitution \(T_aP(X)=P(X+a)\) sends
\(\chi_a(S)=\chi(S-a)\) to \(\chi(X)\). Its upper-triangular coefficient
matrix \(C_a\) has determinant one and inverse \(C_{-a}\). It intertwines
the differentials and carries the special-fibre action to \(A+aI\), with
all primary multiplicities retained.

The potential constant and linear term are both required:
\[
h_a=-\Phi(-a)-ta,\qquad
\Pi_a=e^{h_a/u}\Pi C_a.
\]
The contour translation is justified by the explicitly vanishing connecting
segments at infinity. The scalar gauge intertwines the parameter connections
on \(u\ne0\); the source does not extend this exponential gauge through
\(u=0\).

The metric used after translation is explicitly the pullback
\(G_N^{[a]}=C_a^*G_NC_a\), not a claimed new theta metric for translated
zeros. It gives the control-trace increment \(2q\Re a\). The period-to-source
comparison is multiplied by \(|e^{h_a/u}|^2\) and conjugated by \(C_a\),
so its two-index determinant ratio remains exactly \(V_i/V_j\).

After a specified finite-field reduction, the same potential constant gives
a constant Artin–Schreier character line. The proof fixes its geometric
Frobenius trace convention explicitly. Addition of the two torsors supplies
the tensor map, and the resulting scalar is a root of unity. This verifies
the translation comparison in the stated convention; it does not transfer
Frobenius weights to an unproved arithmetic norm estimate.

## Independent regression executed here

`check_shared_period_maps.py` was written independently, without importing
the owner's checker. All 12 exact finite test methods pass under normal
Python and `-O`; their JSON receipts are identical. Cases include generic
coefficient derivatives through rank four; twisted reduction and companion
traces through rank five; repeated-root multiplicities; phase Grams through
rank six; nonreal coordinate translation and Hermitian pullback; and actual
finite-field coefficient identities in characteristics seven and eleven.

Two deliberately changed formulas are rejected in both modes:

- replacing \(\partial_t\mathcal F=-\operatorname{Tr}A(t)\) by the positive
  sign fails the potential-gradient test;
- removing \(-\Phi(-a)\) fails the translation-potential test.

Each negative run has one substantive assertion failure, zero runtime errors,
and exit code one. There is no unconditional synthetic-failure substitute.
Six execution receipts and the exact checker source are retained beside this
review. No contour quadrature, infinite arithmetic integral, or local Lean
execution is claimed.

## Relation-moment integration qualifications

The incoming two-trace bound keeps the original source operator
\(Z=(K_j-K_i)G_i\), its cross-pairings, its derived spectral cap, and the
positive Hermite remainder. The parent checked its full written proof.
It composes with the current threshold-four result rather than replacing it
with the older threshold two. Two clarifications from the intake review must
be carried into the integrated text:

- window inequalities dividing by \(r=j-i\) use \(i<j\); the valid empty
  block \(i=j\) instead has \(Z=0\), determinant ratio one and log loss zero;
- the zero-trace case has zero logarithmic loss, not zero volume ratio.

These statements preserve the endpoint construction and resolve wording/domain
ambiguities. They do not require a new arithmetic assumption.

## Literature and publication scope

The parent consulted the primary bibliographic record/abstract of Markov,
Tarasov and Varchenko, *The Determinant of a Hypergeometric Period Matrix*,
https://arxiv.org/abs/alg-geom/9709017, and the indexed primary record for
Varchenko, *Critical values and the determinant of the periods*,
DOI 10.1070/RM1989v044n04ABEH002151. These establish relevant prior-literature
context only; their full theorems were not read or made premises of this proof.
No novelty claim for the general period-determinant phenomenon is made.
Deligne's exact primary passages are checked separately in `primary_review`.

This review and its tests are newer working material outside the frozen
Zenodo edition. No public file, DOI, source branch, Overleaf or timer was
changed by this review. The accepted Split-Zero preview remains the 478-page
paper already selected by the user.
