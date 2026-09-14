# Single-primary actual marked boundary calculation

## Assignment

Parent, verbatim:

> New concrete mixed-weightlessing calculation independent of root packaging: use stable work/marked_product_boundary_connection_20260913.tex BC source (6575b8...) and originalmarkednote to calculate ACTUAL SINGLE PRIMARY full packet h(s)=(s-rho)^m, d=m, t=0, preserving originalbasis s^b, Phi(0)=0, actualrho/order/unit g/h and theta source. Do not replaceobjectbytranslatedphase: construct explicit Pascal coordinate map for y=s-rho andretainoriginal scalar c=-(-rho)^(m+1)/(m+1), allbasisconstants. Expect C=cI; B conjugate diagonal beta_b=(b+1)/(m+1); exact ordered period matrix via binomial translation and original contour sector homology, irregularscalar exp(c/u), full analyticmonodromy eigenexp2pii beta_b, none1->invariants0. Proveactualboundarymonodromy/finitecoverN=0 onthissinglecritical-valuefamily, notstatinggeneralallpacketStokes. Prove reconstruction of original A=rhoI+N_ar and source/fullunit on SAMEspace; no claimgeometricN_boundary=N_ar. If doable finite-fieldh singlepower specialization p>m+1, derive Kummer/Gauss decomposition and actualV^I=0 (allnontrivialdegree m+1 chars, commonArtinSchreier c/u); relyonlyprimarysourcesverify. Coulddelegatefinitefieldpart tochild. Own newtotal_object/single_primary_weightlessing.tex plusreview. This is realcontinuation requesteduser mixedweightlessing, notassumedpurity. Rootbuildscurrentcumulativeclosureparallel. Send exactmathprogressandcompleteproofhashwhenready.

The parent owns the full current-session user provenance and active goal.
No global source or published artifact is edited by this lane.

## Source read coverage

Read complete BC source:
work/marked_product_boundary_connection_20260913.tex,
SHA256 6575B8E33FF00BEF8B08E214B974B9BD1E966C3BED4B573C5CA274206A69E9FA.

Read complete original marked note, including separate read of lines
326--411 after the first combined display truncated its middle:
work/deligne-handoff-portable-h8e5vq9g/sources/MARKED_PRODUCT_ORIGINAL_NOTE.tex,
SHA256 40749E2A9D599A322E7B125EB43AD0878A066A51B61DA52CC3BB2FFB94CBD841.

## Active mathematics

Let n=m+1, h=(s-rho)^m, y=s-rho, retaining Phi(0)=0:
Phi=y^n/n+c, c=-(-rho)^n/n.
The exact coefficient isomorphism is Pascal
P_ab=binomial(b,a)rho^(b-a), x_y=P x_s.
BC division is C=cI and B_s column b =
((b+1)s^b-b rho s^(b-1))/n; P B_s P^{-1}=diag((a+1)/n).

Ordered original sector contours are to be compared by an explicit
translation homology, not silently replaced. Period matrix expected:
Pi_s=e^(c/u) W diag(n^(beta-1)e^(pi i beta)Gamma(beta)u^beta) P.
Period-row continuation has positive fractional monodromy; horizontal
coefficient solutions have inverse monodromy. Both spectra contain all
nontrivial nth roots and no 1. The exact one-critical-value splitting
permits the finite cover u=v^n with logarithmic nilpotent N_boundary=0.
The scalar irregular factor remains when c is nonzero.

Arithmetic A_s=P^{-1}(rhoI+N_ar)P remains on the full marked fibre,
with its full Taylor unit. N_ar is not identified with N_boundary.
Retain source Gram and compute its exact period comparison. No claim
that the finite period Gram is positive on a larger polynomial source.

Independent child single_primary_complex_review verifies contours,
monodromy signs and exact coefficient maps.
Independent child single_primary_finite_field verifies only primary
sources and calculates the actual finite-field Kummer/Gauss decomposition,
including c=0 specialization and the common Artin--Schreier factor.

No conclusion about RH or the full multi-critical-value Stokes problem
has been asserted.

## User terminology correction relayed by the parent

The user corrected speech-to-text: the intended programme is the existing
mixed support, mixing the different split-support types. No new concept
or label is introduced. The proof module is now
single_primary_boundary_control.tex. Its content uses ordinary
boundary and monodromy terminology. The earlier assignment above is
retained verbatim only as provenance of the parent instruction.

## Stable completion and validation

The complete main proof is now single_primary_boundary_control.tex,
SHA256 80dcbc843df223a8b65fd92f728deba1b28e540c748e08dabbdf47a6f28958ea.
It contains SP.1–36 and the complete embedded finite-field companion
SPF.1–29; no external input is needed to read either proof.

The exact marked phase is y^(m+1)/(m+1)+c with
c=−(−rho)^(m+1)/(m+1), and the original s-basis is related by
the determinant-one Pascal matrix. The entire period matrix is
exp(c/u) W D(u) P, with every Gamma, phase and integer constant retained.
Original sector contours are transported by the proved translation
homology, including orientations and endpoint estimates. The boundary
monodromy contains each nontrivial (m+1)-st root once. Thus its original
invariants vanish, whereas the full marked fibre has dimension m.
The cover u=v^(m+1) gives the exact zero unipotent logarithm; the common
irregular exponential is retained and is not declared a meromorphic
gauge. The original arithmetic nilpotent and complete Taylor unit are
reconstructed on the same space, including their exact nonhorizontal
commutators and the derivative correction for multiplication on
twisted cohomology representatives.

The original theta-source Gram and period Gram are related by the
exact displayed matrix. Higher polynomial cutoffs retain the exact
differential-relation kernel, so their period Gram is only semidefinite.

The finite-field calculation retains the same primitive and the
specified specialization of the full finite Taylor class and its inverse.
Explicit power-map projectors and source-coordinate isomorphisms give
the complete Kummer/Gauss decomposition with common Artin–Schreier
factor. The proof computes original inertia invariants zero for both
c=0 and c≠0, Swan conductor 0 and m respectively, and trivial inertia
after the displayed finite cover. The unipotent logarithm is zero.
The direct Gauss absolute-square calculation proves weight one for
this sheaf. No identification of its Frobenius eigenvalues with
complex zeta zeros is asserted.

Independent complex review read the final SP.25–36 corrections and
support ending; the reviewed SP-only hash is
b68000ac12f65176f112c42af282656cee9640bd472f0705d43613bc053e5f52.
The finite-field module has a separate complete character-convention
and ramification review. Its stable source hash is
538b2da5adf307b54396e46f0848a49c63f0d81072844d191768016255c4fd53.

Combined draft-mode pdflatex compilation is 12 pages. Its final log
has no undefined references, LaTeX warnings, overfull or underfull
boxes, or errors. Only the expected draft-mode notice appears; no
new PDF was generated. Exact SymPy calculations passed m=1 through 7
with symbolic rho, including Pascal, companion, residue, commutator,
division and Taylor-unit differential remainders. The independent
finite-field integer cyclotomic reduction checked 1,872 original-phase
trace cases and the nontrivial Gauss absolute-square identity.

Parent was sent the stable main file and hash for the requested
source-only handoff folder. The finite-field book cache is research
material, not a proof input and not part of the handoff. The tensor
invariant warning is explicit: this one-factor result is not a claim
that character products have no invariants. No RH conclusion or global
goal completion is claimed. No further changes to the proof are planned
unless a substantive new issue is found.
