# Arithmetic endpoint norms and exact window products

These working sources continue the arithmetic zeta-packet calculations after
the [frozen Toda--Gamma edition](https://doi.org/10.5281/zenodo.22730756).
They are not part of that DOI, its PDFs or its source archives. Start with the
[four-volume synthesis](FOUR_VOLUME_THRESHOLD.md), then the complete
[original arithmetic note](delivery/RESEARCH_NOTE.md) or its
[downloadable HTML reader](delivery/index.html), and the [exact product proof](window/WINDOW_PRODUCT_PROOF.md).

## The source and the question

A packet is a finite selection of zeros of the completed zeta function
\(g=2\xi\), retaining every selected multiplicity. Its monic polynomial is
\(h\). The theta-function source has Mellin transform \(g/h\); on the
critical line its actual density is

\[
w_h(t)=\frac{|(g/h)(1/2+it)|^2}{2\pi},\qquad m_{h,k}=w_h^{*k}.
\]

The mass stays \(\mu_h^k\), not one. In the coordinate
\(S=k/2+iu\), \(\omega_{h,k,n}\) is the squared least norm of a monic
degree-\(n\) polynomial for this measure. The leading phase \(i^n\)
has modulus one. The canonical quotient metric has determinant \(V_N>0\);
its one-step contraction is \(\delta_N=V_N/V_{N-1}\in(0,1]\).
The quotient by the original cyclic relation polynomial \(\chi\)
sends \((\lambda_N,P)\) to \((\lambda_N,[P]_\chi)\). The fibre label
remains when the polynomial class is zero; that is not external absence.

The aim is to measure spectral displacement in this original source norm.
A window of degrees relates endpoint monic norms to quotient-volume losses.
Neither the density, generator, quotient nor its metric is replaced to make
an estimate easier. The source maps, full zero jets and multiplicities remain.

## What the calculations establish

The arithmetic note proves a polynomial lower bound for local zeta mass,
then a lower envelope for the actual convolution \(m_{h,k}\), for
\(k\ge3\). Exponential moments give an upper trial norm; the exact monic
Legendre minimum gives the lower norm. Together they prove

\[
\left(\frac{\omega_{h,k,2n}}{\omega_{h,k,n}}\right)^{1/(2n)}
\le C_h n,\qquad n\ge k\ge3.
\]

The [balanced-window extension](BALANCED_WINDOW_PROOF.md) proves, for the
same measure and fixed \(h\),

\[
\left(\frac{\omega_{h,k,n+r}}{\omega_{h,k,n}}\right)^{1/(2r)}
\le C_h^{\rm bal}n,\qquad n\ge k\ge3,\quad n/2\le r\le n.
\]

The full proofs specify finite constants through actual source masses,
compact minima and Laplace moments. These constants have not been enclosed
numerically. The theorem does not extend to \(k=1,2\) by substituting
negative convolution exponents.

The exact product keeps every interior contraction twice and retains the
actual real phase \(\phi_N\): for \(n\ge q,r\ge1\),

\[
\prod_{j=0}^{r-1}(\epsilon_{n+j}^2+\phi_{n+j}^2)
=\frac{\omega_{n+r}V_n}{\omega_nV_{n+r}}
(1-\delta_n)(1-\delta_{n+r})
\prod_{j=1}^{r-1}(1-\delta_{n+j})^2.
\]

Each contraction factor is at most one. The exterior estimate
\(L_{h,k}\le\epsilon_N\) therefore yields an endpoint inequality without
assuming the phase vanishes. A unit contraction directly forces \(L_{h,k}=0\).

For any exact off-line quartet \(1/2\pm\delta\pm i\gamma\), with
\(\delta,\gamma>0\) and common order \(m\), the full cyclic degree is
\(q_k=[1+k(m-1)](k+1)^2\). Choose \(n=q_k,r=q_k-1\).
The [complete synthesis](FOUR_VOLUME_THRESHOLD.md) proves the necessary growth

\[
\liminf_{k\to\infty}
\frac{\log(V_{q_k-1}V_{q_k}/(V_{2q_k-1}V_{2q_k}))}{q_k\log k}
\ge4.
\]

The original delivery's lower threshold of two remains a valid consequence
of its weaker endpoint bound; four is the strengthened result. This does not
assert that an off-line quartet exists. A proved upper normalized limit
strictly below four would contradict this growth, but no such arithmetic
volume upper bound is supplied. Positivity, fixed transfer width and finite
checks do not provide it. No RH proof or disproof is claimed.

## Read the original delivery with these current qualifications

The files in `delivery/` are unchanged historical source bytes. Their core
mass and norm proof is accepted. Apply the following two qualifications to
their ancillary relation/transfer statements:

1. The leading-coefficient multiplication isomorphism after equation (13)
   requires \(n\ge q\). At \(n=q-1\), the relation space is zero;
   the isomorphism is not asserted there.
2. The squared-polynomial transfer specialization in Section 8 and handoff
   item D requires dagger stability
   \(\overline\chi(k-S)=(-1)^q\chi(S)\). With \(c=k/2\) and
   \(\psi(u)=i^{-q}\chi(c+iu)\), this gives
   \(|\chi(c+iu)|^2=\psi(u)^2\). The induced quotient map is
   \([P(S)]\mapsto[P(c+iu)]\); raw derivative order \(d\) contributes
   \(i^d\). The exact quartet satisfies this condition. The analytic norm
   theorem for a general packet must not be confused with this specialized
   transfer identity.

For the exact-window and doubled-jet formulas, keep a nonempty
reflection/dagger-stable packet, \(q\ge1\), and one consistent deformation
parameter \(\theta\). The norm/threshold specialization uses \(\theta=0\).
Radius identities start at \(N\ge q\); \(r=1\) is treated separately,
and \(q=0\) is excluded. The \(q=1\) norm band is empty. Width-\(2q\)
raw jets retain their factorials, \(i^q\) coordinate factor and common phase.
Strictly positive local-factor sharpness requires its endpoint and interior
contractions to be strictly below one, as stated in the full window proof.

## Verification and source provenance

The [arithmetic review](verification/arithmetic/REVIEW.md) accepts the written
analytic proof with the two qualifications above; the
[window review](window/README.md) states its independent scope.
Both review lanes checked the four-volume synthesis. Written analytic
arguments and finite exact regression tests are kept separate. The original
checker has 18 methods, and the balanced extension has 12,017 exact checks in
each of ordinary and optimized Python, with deliberate failures rejected.
These are not Lean proofs of the analytic quantifiers or interval enclosures.

Run the portable finite checks from this directory with SymPy installed:

```text
python delivery/check_endpoint_bounds.py
python -O delivery/check_endpoint_bounds.py
python check_balanced_window.py
python -O check_balanced_window.py
python window/verify_window_product.py
```

`SOURCE_SELECTION.json` records original and public byte identities, exact
link-only relocations, and exclusions. All authored mathematical texts, the
readable HTML, checkers, source reports and structured check evidence from
the delivery are retained. Its six raw log captures and three layout
screenshots are omitted; the original archive and manifest hashes establish
provenance without republishing intake dumps. The unchanged original manifest
describes the supplied archive, including the omitted files, not this public
selection. `INTEGRATION.patch` is retained as historical data, not an
instruction to apply it over current sources.

The inherited Gamma/Deligne source-reading reports remain attributed earlier
evidence, not a new independent full literature audit. No external literature
corpus, private pasted report, local intake locator or credentials are included.
Existing source rights and citations are retained; no new attribution name or
license grant is inferred from local account information.
