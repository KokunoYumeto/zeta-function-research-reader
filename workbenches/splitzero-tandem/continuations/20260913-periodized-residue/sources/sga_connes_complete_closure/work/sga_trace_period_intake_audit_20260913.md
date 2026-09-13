# Complete SGA trace-period intake and proof audit

The complete 664778-byte archive has SHA-256 e67cee138c0b5f1ce5127337a43d3b7abfc64612e8d8ee611d4c9cc2636516db. All 47 members are preserved in sources/web_sga_trace_period_delivery/Tau_SGA_Trace_Period_Control/, including the full HTML, LaTeX, Markdown, evidence and patch. Every extraction target was checked to remain inside that directory; different existing bytes would have caused an error. All 46 delivered manifest rows verified.

The raw NOTE.tex is 36422 bytes, SHA-256 07a89536c068e5631becad1acedec1bf70b0280edc631bfdaee509712f8f18e8. The Markdown is 32627 bytes, SHA-256 96061b31f6f99ce3d268bc4411b680bfe01592fdbfe0e879de9316ea81d0142b. The associated full user paste is 19263 bytes. These original proof sources remain unchanged.

## Full reading and review scope

Read completely: the paste, NOTE.tex in three nonoverlapping ranges, RESEARCH_NOTE.md, SOURCE_REVIEW.md, HANDOFF.md, CHECKS.md, README.md, PROGRAMME_STATE.md, check_trace_period.py, package_delivery.py and period_numerics.py. The entire XD1–26 determinant proof was reread. The relevant DS source and constituent-metric sections were read; one attempted full-sidebar output was truncated and is not counted as a full rereading.

The primary child visually read original French SGA printed pages 120–130 and 136–137; this agent read its complete report and receipt. Root independently read the complete SC proof, complete delivered note and primary report. No predecessor checker was rerun.

## Residue pairing, trace and source map

Let \(T=R[t]\), \(H=\chi-t\), and \(E_T=T[S]/H\), with χ monic of degree q>0. The ordered free basis is \(1,S,\ldots,S^{q-1}\). The original top-remainder coefficient is \(\lambda([P])=[S^{q-1}]\operatorname{rem}_H P\). Its pairing matrix has zero entries when the total exponent is below q−1 and ones on that antidiagonal. Column reversal gives a triangular matrix with diagonal one. The original determinant is therefore exactly \((-1)^{q(q-1)/2}\), over arbitrary commutative R.

The polynomial divided difference satisfies \((X-Y)\mathcal C_H=0\), \(\mu(\mathcal C_H)=\chi'\), and \((\lambda\otimes1)\mathcal C_H=1\). The last identity follows from its leading X-coefficient. Divisibility of \(P(X)-P(Y)\) by X−Y gives the full inverse identity

\[
(\lambda\otimes1)((P\otimes1)\mathcal C_H)=P.
\]

Thus this tensor is the actual coevaluation. Composing it with multiplication by P and evaluation proves

\[
\operatorname{Tr}_{E_T/T}M_P=\lambda(\chi'P),\qquad
\tau^\flat=\beta^\flat M_{\chi'},\qquad
\ker\tau^\flat=\operatorname{ann}(\chi').
\]

The perfect residue form, possibly degenerate trace form and original S-action are connected by these exact maps. No derivative or discriminant is inverted. At a multiplicity-m complex root, χ′ is m times \(x^{m-1}\) times its retained local unit, modulo \(x^m\); the radical has dimension m−1.

Dividing P=HQ+r shows that only the \(S^{q-1}\)-coefficient of r contributes to \(S^{-1}\) in P/H. Therefore λ is the sum of positive finite residues and the negative of the residue at infinity. No extra \(2\pi i\) factor enters the algebraic trace.

The original logarithm calculation retains the Mellin unit \(\mathcal U=\prod v_h(s_i)\). The derivative of \(\mathcal U\chi P\) in \((1/k)\sum\partial_{s_i}\) is

\[
(\partial\mathcal U)\chi P+\mathcal U\chi'P+\mathcal U\chi P',
\quad (1/k)\sum_i\partial_{s_i}S=1.
\]

The first and third terms are killed by the original relation. Its specified jet/retraction map removes the retained invertible unit in the middle term, giving \([\chi'P]_\chi\). The relation is differentiated before quotienting. Every support lift retains the receiving supported zero and sends external absence to τ. The conormal map onto the original contracted relation level retains its possible kernel.

## Complete diagonal resolution and derived collision fibre

In \(U=(T[Y]/H(Y))[X]\), both \(d=X-Y\) and \(b=\mathcal C_H\) are monic non-zero-divisors, and the tensor algebra is U/(db). Cancellation gives \(\ker d=\operatorname{im}b\) and \(\ker b=\operatorname{im}d\); the augmentation quotient by d is E_T. This proves full exactness of the periodic free resolution.

Diagonal tensoring gives alternating maps zero and χ′. Thus

\[
HH_0=E_T,\quad HH_{2a+1}=E_T/(\chi'),\quad
HH_{2a+2}=\operatorname{ann}_{E_T}(\chi')\quad(a\ge0).
\]

Multiplication by X becomes the original S-action. These are module identifications, with no uncalculated shuffle product or identification with the independent relation-depth index.

SC26–30 prove the exact specialization bridge. Over \(T=\mathbb C[t]\), t↦χ(S) identifies E_T with \(\mathbb C[S]\), so multiplication by the nonzero χ′ is injective. Its cokernel \(M=\mathbb C[S]/(\chi')\) has a two-term free T-resolution. At t₀, tensoring yields

\[
0\to\operatorname{Tor}_1^T(M,T/(t-t_0))
\to E_{t_0}\xrightarrow{\chi'}E_{t_0}
\to M\otimes_T T/(t-t_0)\to0.
\]

Odd fibre groups are the final quotient; positive even fibre groups are this Tor term, although the positive even family groups vanish. On representatives, \((\chi-t_0)v=\chi'w\) induces \([v]_{\chi'}\mapsto[w]_{\chi-t_0}\). Changing v by χ′a changes w by \((\chi-t_0)a\); cancellation and the same equation prove both inverse directions. All maps commute with S. The local odd and even modules are \(\mathbb C[x]/(x^{m-1})\) and \((x)/(x^m)\), joined by multiplication by the original x. Kernel formation therefore uses the displayed derived term under specialization; the coefficient maps themselves commute with base change.

## Determinant and Newton recovery

The differential quotient uses \(D=u\,d/dS+\chi-t\). Ordinary and differential remainders give inverse coefficient-module maps by fixing the same degree-below-q frame. They do not claim ideal reduction: \(D(S)=u+S(\chi-t)\) gives \([S(\chi-t)]=-u[1]\).

For \(1\le m\le q\), ordinary division \(S^{m+b}=(\chi-t)Q+R\) has \(\deg Q\le q-1\). Differential reduction is exactly R−uQ′. The correction has degree at most b−1, so its matrix is strictly upper triangular and has zero trace. This is the unchanged XD8–11 proof.

For \(\mathcal F=\operatorname{Tr}\Phi_t(A(t))\), XD14–15 uses \(d\operatorname{Tr}A^n=n\operatorname{Tr}(A^{n-1}dA)\). Matrix-derivative terms combine into \(\operatorname{Tr}((\chi(A(t))-tI)dA)=0\). The remaining coefficient derivatives are the actual power traces. This works at collisions; the packet's polynomial-continuation argument is also valid.

XD preserves the explicit compact-parameter cutoff, integrable ray majorant, all phases and cancellation of origin boundary terms. The monomial Fourier difference matrix has Gram \((q+1)(I+J)\). The adjugate determinant derivative integrates before invertibility is known to

\[
\det\Pi=\det\Pi_{\rm mon}\exp(\mathcal F/u).
\]

This agrees exactly with the existing shared XD1–26 calculation. SC6a–b add the explicit gamma evaluation: for d=q+1 the factors are \(d^{q+1}\), \((d|u|)^q/d^{2q}\), and \((2\pi)^q/d\). Their d powers cancel to zero. DLMF 5.5.6 at z=1/d gives 5.5.7, hence squared constant \((2\pi|u|)^q\). The unsquared phase and ray ordering remain SC6, including the rank-one downward/upward sign.

All first q coefficient-direction derivatives recover the power traces. The formal derivative of \(\log\det(I-zA)\) gives Newton recursion with its exact factors 1/n. Because the specified companion is cyclic, its characteristic polynomial equals its minimal polynomial and retains complete Jordan lengths. This does not classify a larger noncyclic module by trace alone.

## New SC1–37 proof and metric bridge

The standalone PDF contains the complete unchanged XD proof followed by SC1–37, including SC6a–b. This is a joint continuation: this intake derived the global normal identity; root supplied the neighboring-minor/Toda bridge and independently reviewed the entire integration.

For a proper nonzero invariant injection \(I:F\to E\), its image is an ideal because A=M_S generates the algebra. Its inverse polynomial ideal is generated by a unique monic g dividing χ. Cancellation proves \([a]_{\chi/g}\mapsto[ga]_\chi\) is an isomorphism. In the ordered basis \(g,Sg,\ldots,S^{p-1}g\), the last polynomial is monic of degree q−1. Therefore \(L=\ell I\) is onto while 1 lies outside the ideal.

For \(Y=\Pi I\), \(H=Y^*Y\), \(P=YH^{-1}Y^*\), \(N=1-P\) and \(z=N\Pi e_0\), invertibility of Π proves z never vanishes. Exact A-invariance gives

\[
NY'=-t zL/u.
\]

For t≠0 this has rank one, kernel ker L and image \(\mathbb Cz\). At zero its normal acceleration is \(-z(0)L/u\), again rank one. SC14 gives the actual source factorization through \(r_Ne_0\), \(j_E\) and \(N\Pi\).

Direct Wirtinger differentiation yields

\[
\partial_{\bar t}\partial_t\log\det H
=\operatorname{Tr}(H^{-1}Y'^*NY')
=|t|^2\frac{\|z\|^2 L H^{-1}L^*}{|u|^2}.
\]

The coefficient is strictly positive and real analytic everywhere. The curvature vanishes exactly to quadratic order at zero; SC18 also gives an actual cubic remainder from a bounded real gradient on a closed disk. SC17 retains the dual determinant convention and \(i\,dt\wedge d\bar t=2\,dx\wedge dy\).

The domain theta Gram remains \(G_{N,F}=I^*G_NI\). The squared theta-domain Hilbert–Schmidt norm of the normal acceleration is \(\|z(0)\|^2L G_{N,F}^{-1}L^*/|u|^2\). The curvature is related to it through the literal matrix identity \(H^{-1}=B_{N,F}^{-1}G_{N,F}^{-1}\). SC23–25 give the full moving original target metric, projection, positive Schur complement and derivative terms; these cancel exactly in \(Y^*\widetilde G_NY=G_{N,F}\).

The exact frame C satisfies \(IC=J_g\), retaining \(|\det C|^2\). For J₋ omitting the last polynomial column, \(J_+=[J_g,e_0]\), and \(h_J=\det(J^*\Pi^*\Pi J)\), Schur complement and an inverse cofactor give

\[
\partial_{\bar t}\partial_t\log h_g
=\frac{|t|^2}{|u|^2}\frac{h_+h_-}{h_g^2}.
\]

The same original theta volumes and comparison determinants obey \(h_J=v_{N,J}b_{N,J}\), retaining every theta factor in SC36. In codimension one, \(\det[J_g,e_0]=(-1)^{q-1}\), so the top minor equals the evaluated full determinant. Empty and full constituents retain their zero-curvature cases. These are calculated observables, not a claimed uniform arithmetic upper bound.

## Required embedding corrections and primary scope

1. Delivered (1) needs trace base R[t], already correct in (21). The family is generally not finite over R. Universal coefficient traces in (2) and (35) have base \(\mathbb C[\mathbf c,t]\); their specified complex fibres have finite \(\mathbb C\)-linear trace. The trace commutes with that coefficient specialization.
2. The universal version of (28) has ring \(\mathbb C[\mathbf c,u,t]\); the fixed original coefficients give \(\mathbb C[u,t]\). Both remainder calculations commute with specialization.
3. The generated NOTE.tex paragraph following (50) contains damaged Markdown rendering of \(\Pi^*\Pi\) and \(G_N^{-1}\Pi^*\Pi\). The original Markdown and displayed equations determine the intended formulas. Repair their embedding while preserving the raw source.
4. SGA §6 assumes a noetherian base. Formula (6.8.5) uses the smooth ambient map, regular immersion and finite flat composite; it does not require ambient properness, which belongs to (6.8.4). Arbitrary-base validity rests on the direct monic proof.
5. Original printed p.128 has three \(N_{Y/S}\) tokens where its definition and Hom isomorphism force \(N_{Y/X}=I/I^2\). Annotate literal transcription and retain the exact conormal map. The expected English master was not located in bounded paths; the actual original French scan independently verifies the operation. Its missing translation bytes are not claimed read.

The full primary report preserves the printed qualification about the proof/reference, exact pages, PDF hash and DLMF endpoint. The French PDF and page images are reference-only local review evidence, not new programme-authored corpus content for redistribution.

## Actual checks, PDF and final pin

The unchanged new package checker ran in Python 3.13.9 with SymPy 1.14.0. Eighteen methods pass in each mode. Three substantive false controls each returned exit code 1 in both modes: omitted Jacobian, false ideal reduction, and erased repeated factor. The eight jobs retain all commands, stdout, stderr and reports under sga_trace_period_replay_20260913/. Neither predecessor suite nor numerical quadrature was rerun. No interval certificate or Lean execution is claimed.

The independent companion checker has six methods covering actual cyclic ideals, complex-parameter normal maps, theta Schur complements, metric cancellation, neighboring minors with theta factors, and collision-Tor representatives. All six pass in both actual modes with full evidence under sga_constituent_curvature_replay_20260913/. The earlier four-method development source and successful result remain separately labelled.

All ten final PDF pages were rendered and visually inspected. The final log has no overfull/underfull boxes, undefined references or warnings. The first wrapper compile lacked mathrsfs; the actual failure log is preserved and the dependency repaired. A fraction escape and two comma exponents were corrected before sealing; no mathematical test failure was hidden. This audit replaces the initial escaped-text draft.

The final SC source is 21523 bytes, SHA-256 f7cbbb2da3a97722c9f9128602b4de64ad1ab9cfccdbb03e8ee9363321f7de63. Root's complete review accepts those exact bytes, including final layout-only SC10–11 splits. The final manifest binds the full archive, proofs, new execution evidence, independent reviews, PDF and visual receipt. The older frozen reader and publication were not changed by this intake; the complete addition is ready for the next cumulative snapshot.
