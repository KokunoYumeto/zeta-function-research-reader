# Joint Gamma Schur Return

*Exact integration, rational certificates and signed receiving bounds — 14 September 2026*

Read [the complete 46-page paper](Joint_Gamma_Schur_Continuation.pdf).
This supplement studies how the original theta-function source and its
zero-jet quotient can be compared with an explicitly calculable Gamma
measure. The purpose is to estimate the original arithmetic determinant,
not replace it by a different metric or discard its relation subspace.
Complete definitions, calculations and proofs are included in the paper
and editable sources.

## The source and the comparison

The theta-source construction uses the Mellin transform of the completed
Riemann xi function, with a selected full zero packet divided out. Its
polynomial representatives retain the original source norm, complete zero
multiplicities and quotient relations. Tensor degree is denoted by \(k\).
The source scalar \(\tau\), represented zero, absent faces, tensor order and
actual unit multiplications remain part of the construction.

The present Gamma comparison works on \(k=4l+1\), \(l\ge1\), with \(c=k/2\).
The full quartet parameters satisfy \(0<\delta<1/2\) and \(\gamma>2\); with
multiplicity \(m\ge1\), put \(e=1+k(m-1)\) and \(q=(k+1)^2e\). The cyclic
quotient retains the complete polynomial

\[
\chi(S)=\prod_{a,b=0}^{k}
[S-c-(2a-k)\delta-i(2b-k)\gamma]^e.
\]

The exact Gamma multiplier is

\[
f(S)=\prod_{j=0}^{l-1}(S-c-2j-\tfrac12),
\qquad dm_0=C_k|f|^2d\sigma.
\]

Here \(d\sigma\) is the reference Gamma measure, \(dm_0\) the original Gamma
convolution measure and \(C_k\) its retained mass factor, evaluated explicitly
in the paper. Multiplication by \(f\) is an automorphism on the full quotient:
its real roots are disjoint from the original odd-subsequence packet roots.
The weighted cyclic inclusion carries this operation to \(f(\sum_i s_i)\)
on the original tensor source.

## What the mixed Schur calculation keeps

For an original cutoff \(N\), the joint observation at \(M=N+l\) records both
the quotient jets \(J_M\) and the additional-node observation \(Z_M\). Its
covariance and the resulting metric are

\[
\begin{pmatrix}K_M&C_M\\C_M^*&A_M\end{pmatrix},
\qquad
G_N^0=C_kM_f^*(K_M-C_MA_M^{-1}C_M^*)^{-1}M_f.
\]

The full cross block \(C_M\) remains. The minimum-section correction is an
actual multiplication-by-\(\chi\) relation; its original theta primitive and
source norm are retained. JSA1–40 calculates the exact maps, including the
invertible conversion between raw and divided derivatives at every order.

The complete mixed determinant factor is

\[
\mathfrak d_N=\det(I+X_N)\det(I-Y_N)
=|\det M_f|^2\mathfrak R_N/D_{l,N}.
\]

The factors represent the degree update and the retained relation correction.
Their full definitions and original metrics are in the source. Neither the
degree-update logarithm alone nor an independently chosen positive metric
is substituted for this expression.

The four original cutoffs are \((q-1,q,2q-1,2q)\), with signs \((+,+,-,-)\).
The return \(R^0-R^\sigma\) equals **minus** the previously defined GSR
functional \(T\); the arithmetic substitution remains
\(\Delta_\Gamma=\delta_\sigma-T\).

## Evaluated contributions and remaining work

The free additional-node determinant is evaluated through explicit adjoint
polynomial maps. With \(B_l=l(l-1/2)\), its finite expansion is

\[
C_{\mathrm{free}}=2B_l\log2-\frac{B_l(l+1/4)}q+R_{q,l},
\qquad
0\le R_{q,l}\le\frac{B_l(14l^2+5l+3)}{16q^2}.
\]

The second-order calculation gives the constant \(167/2048\) on the original
simple-quartet sequence. This evaluates the free summand; the
relation-dependent Schur summand is still present.

The two low relation determinants are known exactly. Substituting them leaves
four high-endpoint matrix series. RGC1–16 supplies a rational construction
over \(\mathbb Q(\delta^2,\gamma^2)\) and a signed scalar logarithm certificate.
The complete \(k=5,q=36\) calibration uses all four cutoffs \(35,36,71,72\);
its chosen parameters are not asserted to be zeros of xi.

JRA1–29 applies the signed-resolvent machinery to the original eight-block
metric, retaining its \(8l\) trace factor, centered variance and path integral.
The signed arithmetic receiver keeps the asymmetric allowances:

\[
\mathcal B_{\rm ar}\in
[\mathcal B_0+L-D_-,\,\mathcal B_0+U+D_+].
\]

The unresolved growing-family estimate concerns the two high relation Grams
and the original arithmetic correction. It must control their actual
\(|\chi|^2d\sigma\) density, including interior, controlled exterior and far-tail
contributions. Fixed-input certificates do not supply this uniform estimate.
No RH conclusion or off-critical xi zero is asserted.

## Complete source and evidence

The seven full proof sections are in `sources/`; full inherited proofs,
receiving texts, exact calibration and formal-source snapshots are in
`dependencies/`. Author originals and display-change records are retained in
`provenance/`. [Current source pins](CURRENT_SOURCE_PINS.json) and the
[public derivation ledger](PUBLIC_DERIVATION.json) distinguish author,
prepared and public metadata identities.

The [owner delivery receipt](provenance/owner_delivery/DELIVERY_RECEIPT.json)
records the unchanged PDF and completed all-46-page visual review. Mathematical
acceptance belongs to the responsible mathematical task and is reused at its
stated scope. No new proof review, PDF build or Lean execution is claimed here;
the written JRA application is not relabelled as a compiled Lean theorem.

Private incoming pasted messages and archive wrappers are not public source
files. Historical metadata paths use the documented
[relative origin aliases](source-records/README.md); original owner receipt
hashes retain their meaning.

## Build

From this directory, run XeLaTeX three times to resolve the contents and
references:

```text
xelatex -interaction=nonstopmode -halt-on-error -file-line-error Joint_Gamma_Schur_Continuation.tex
```

The retained `prepare_reader.py` is historical authoring code, not the current
build entry point. The accepted prepared sources already include their
separately recorded display repairs.
