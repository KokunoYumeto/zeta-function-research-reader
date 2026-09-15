# Split-Zero cohomology: outer first variation and original residual metric

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/00_CONTINUE_HERE.md).

[Read the current 161-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22759785/files/61-first-variation-reader.pdf/content) · [Published DOI 10.5281/zenodo.22759785](https://doi.org/10.5281/zenodo.22759785).

- [161-page first variation](https://zenodo.org/api/records/22759785/files/61-first-variation-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation) · [offline source ZIP](https://zenodo.org/api/records/22759785/files/62-first-variation-sources.zip/content).

The current 161-page reader evaluates the outer first variation in the original Gamma sources, constructs the fixed coefficient module and its exact original residual Schur metric, and propagates the combined kernel-plus-residual estimate through the arithmetic and signed cohomological return. Complete EIQ/QLG/OFV/FMC/OVR proofs and receiving statements retain the fixed original period, source orders 1 and k, full masses, phases, multiplicities and unequal finite errors.

## What is being calculated, and why

Split-Zero studies a finite arithmetic quotient associated with a selected
zeta-zero packet, its original theta cohomology and mixed-support maps. A
specified period observation has a common kernel K: the same kernel is
measured in the original source metrics at four degrees q-1, q, 2q-1 and 2q.
This is one fixed original period, not an intersection over different periods.
The aim is to calculate the contribution of that observation kernel and its
boundary complement to the original signed cohomological return.

The preceding 132-page edition expressed this kernel contribution as an outer
root-quotient term minus an explicit nonnegative residual-observation sum,
with both unequal finite error endpoints retained. Its moment comparison
identified seven same-source Gamma moment determinants to calculate. This
edition completes their first variation at the kq scale and constructs a fixed
coefficient module with the exact original residual metric still attached.

The main simple-quartet lane retains m=1, k=4l+1 with l>=1, q=(k+1)^2,
c=k/2, 0<delta<1/2, gamma>2 and every original branch |u|>=R_*.
The radius R_* comes from the actual quartet and full unit v_h=2xi/h.
The common kernel has rank r=8k-16 on this lane. The full multiplicity and
primary-coordinate algebra remains available without assigning this rank or
this metric conclusion to other multiplicities. The Gamma source orders are
the original s=1 and s=k; their masses, centres and coefficient phases remain.

## Completed outer first variation

OFV1-32 supplies the source-order recurrence, Gamma-to-exponential full-norm
comparison, scalar and growing-low determinant bounds, and high parity-block
estimate. EIQ1-33 and QLG1-32 provide the complete equilibrium density and
uniform finite-partition estimate used in that calculation. With

    Delta=q-(k-7)^2=16k-48,
    C_partial=4 log(4/pi)+2-2 I_(2,pi),
    I_(2,pi)=integral integral log|x-y| dmu_(2,pi)(x) dmu_(2,pi)(y),

the result for both original source orders is

    F_outer^(s)=Delta q C_partial+O_(delta,gamma)(q log q).

Here mu_(2,pi) is the proved EIQ equilibrium measure. The actual domain is
OSP23 together with k>=257: in particular epsilon=2^(-32), k>=29 and
k sqrt(delta^2+gamma^2)<=epsilon q/2 are retained. This eventual domain is
not confused with the conductor construction's earlier k>=9 domain.
The original period is fixed; no uniformity over moving periods is claimed.

## The original residual metric survives the coefficient construction

FMC1-38 constructs the rank-625 module over the original pure fifth powers,
its rank-125 invariant submodule, complete actual relation columns and a
terminating homogeneous reduction. The specified fixed-strip frame maps T_k
and T_k^(-1), including the residual map onto its image, have logarithmic
exterior cost O_actual(k^2)=o(kq) in every exterior rank. This estimate is
not assigned to the separate Vandermonde or degree-flag maps. The fixed
relation lists define actual-period constants; their full output for unknown
actual periods has not been numerically evaluated.

The exact map to the original source Gram G_N is

    J_k=N_k^transpose T_k^(-transpose),
    H_N=J_k* G_N J_k=[[H_11,N,H_12,N],[H_21,N,H_22,N]],
    Q_(Xi,N)^fix=H_11,N-H_12,N H_22,N^(-1) H_21,N.

The off-diagonal blocks and the full original Gamma metric are retained.
FMC27-28 gives the map to earlier certificate frames and the inherited period
Gram; FMC35-38 retains the primary-to-polynomial Vandermonde factor, literal
Lagrange interpolation and conductor degree-flag transition. Coefficient
conditioning therefore supplies explicit maps, not a replacement metric.

The equivalent ROQ constrained covariance uses the original certificate rows
D, relation rows C and source covariance R_N:

    Omega_N=D[R_N-R_N C*(C R_N C*)^(-1) C R_N]D*,
    Q_(Xi,N)=Omega_N^(-1).

Its exact nonnegative residual sum retains all original coefficients:

    Phi_(k,s)=log(1+eta_(q-1))
       +2 sum_(N=q)^(2q-2) log(1+eta_N)+log(1+eta_(2q-1))>=0.

## What the evaluated outer term proves for the original return

OVR1-11 carries the same residual through the source, arithmetic and signed
return maps. With Delta/k=16-48/k retained, it proves

    F_K^(s)+Phi_(k,s)=Delta q C_partial+R_(k,s),
    R_(k,s)=o(kq),
    (Phi_(k,k)-Phi_(k,1))/(kq) -> 0,
    (F_K^ar+Phi_(k,1))/(kq) -> 16 C_partial,
    (S_k^mix+Phi_(k,k))/(kq) -> 16 C_partial-C_Gamma/4.

These statements retain the two unequal signed finite error endpoints and
the original Gamma correction. The finite cap retains both actual first
positive-increment subtractions:

    F_K^(s)+Phi_(k,s)
       <=Delta(L_(s,q)+L_(s,q+1))-d_1-lambda_s.

Writing kappa_star=32 log(25 log3/(4pi)), OVR bounds each of the scaled kernel
and residual sequences between lower limit max(0,16 C_partial-kappa_star)
and upper limit min(kappa_star,16 C_partial). Their sum converges to
16 C_partial, and 0<=C_partial<=kappa_star/8. **This is not a proof that
either separate sequence has a limit.** The earlier finite pointwise KAF/AKS
minimum remains. Its asymptotic sourcewise ceiling is retained separately:
limsup F_K^a/(kq)<=kappa_star<25.02078097650 for a=sigma,0,ar.

## The current calculation

The next task is the leading contribution of Phi_(k,s) in its original metric,
using the complete ROQ constrained covariance or the equivalent FMC Schur
complement. Evaluated positive partial sums already yield valid finite
subtractions. A leading estimate must preserve the source-ideal graph,
kernel cross terms, complete relation denominator and all four endpoints.

Alongside it, the owner continuation asks for the exact quantitative connection
from the signed return to the canonical control of the same surviving
arithmetic class. The starting form is A*G_N+G_N A-kG_N, with its original
endpoint vectors, two nonzero eigenvalues, full radius and exterior spectral
defect. Its action, connection and boundary terms must be calculated in that
metric. A scalar volume estimate alone has not supplied an exclusion theorem.

The outer first variation is completed on its explicit eventual domain. The combined kernel-plus-residual leading value is established there; the separate residual and kernel leading values and the quantitative connection to the original control form remain active calculations. Coefficient conditioning does not replace the Gamma metric. No moving-period uniformity, RH exclusion or programme completion is claimed. Later outer-operator and control-form editions are not part of this sealed cut.

## Complete sources and recorded verification

[File14: complete editable proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex)
preserves the full 132-page predecessor and includes complete EIQ1-33,
QLG1-32, OFV1-32, FMC1-38 and OVR1-11. The receiving successors
[joint file09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/09_UPDATED_JOINT_NOTE.tex) and
[signed file10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/10_UPDATED_SIGNED_RETURN.tex) contain the complete
MRI4r-v and BRI6h-i refinements, retaining every earlier provider. Their
268/260-page builds establish compilation only, not visually accepted receiver
PDFs. [Arithmetic source file13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex)
retains the original correlated allowances and maps.

The delivered 161-page reader has the owner's full visual acceptance:
129 complete page images match the accepted predecessor; pages1,2,5 and
133-146 were inspected individually by the owner, and147-161 by an independent
reviewer. All footers were checked. The complete new written proofs and
receiving statements have their recorded independent acceptance.

FMC's diagnostic script records 30,634 exact checks in both normal and
optimized Python. These are finite fixtures, not actual zeta periods or the
full actual Groebner output. No new local Lean execution is claimed by this
edition. [File16](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md) preserves
its original complete four-module record: observed strict implementation
8e78bc7c240b04d297ade6afdadfd863e0c6db7b and final documentation/source head
9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6, with 33 local modules and 56 selected
transitive axiom targets. The appended PR34/35 report is historical coordination
at its stated inspected revisions, not a new whole-stack CI certificate.
Later integration status must come from the integration owner's exact receipts;
this reading index neither overwrites those records nor claims new checks.

[Validation12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/12_VALIDATION.md) states these precise scopes.
[Source map11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/11_SOURCE_MAP.json) distinguishes the original
SHA-256 `f3b01e7efc3f30858253db0626d60803598913465fefa27c194b855e33ab6226` from the public transported
SHA-256 `8ce030c567a5538e9afc77a61b655d0c23d1af4d1a8b40452cbd5584b47411c8`. Its metadata-only transport scope is:
891 literal historical private-account locator occurrences transported across802 values and8 path-valued keys. Mathematical bodies, original identities, numeric fields, source spans and other metadata unchanged. The other sixteen files and all eleven full TeX bodies
are unchanged by the publication transport.

The exact seventeen-file edition has one current continuation: original
owner00. This index is a reading guide, not a competing research prompt.
Later outer-operator and control-form drafts remain outside this sealed cut.

## Earlier complete source editions

- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 60-download edition](https://doi.org/10.5281/zenodo.22759221) remains
unchanged with its 132-page preview. This edition adds PDF61 and ZIP62.
The actual human-readable preview is the current 161-page PDF61; ZIP62
contains the seventeen source files for offline use. Every earlier download
and mathematical source remains intact.


[Release provenance](RELEASE.json) · [All file identities](ALL_ZENODO_FILES.json).

## All 62 downloads

- [61-first-variation-reader.pdf](https://zenodo.org/api/records/22759785/files/61-first-variation-reader.pdf/content) — 974,609 bytes; separate PDF.
- [62-first-variation-sources.zip](https://zenodo.org/api/records/22759785/files/62-first-variation-sources.zip/content) — 3,540,462 bytes; offline source archive.
- [01-main-reader.pdf](https://zenodo.org/api/records/22759785/files/01-main-reader.pdf/content) — 3,502,600 bytes; separate PDF.
- [02-fluid-reader.pdf](https://zenodo.org/api/records/22759785/files/02-fluid-reader.pdf/content) — 2,063,023 bytes; separate PDF.
- [03-heat-reader.pdf](https://zenodo.org/api/records/22759785/files/03-heat-reader.pdf/content) — 1,266,114 bytes; separate PDF.
- [04-connes-reader.pdf](https://zenodo.org/api/records/22759785/files/04-connes-reader.pdf/content) — 954,841 bytes; separate PDF.
- [05-gct-reader.pdf](https://zenodo.org/api/records/22759785/files/05-gct-reader.pdf/content) — 1,624,359 bytes; separate PDF.
- [06-vacuum-reader.pdf](https://zenodo.org/api/records/22759785/files/06-vacuum-reader.pdf/content) — 676,386 bytes; separate PDF.
- [07-complete-mathematical-sources.zip](https://zenodo.org/api/records/22759785/files/07-complete-mathematical-sources.zip/content) — 12,343,724 bytes; offline source archive.
- [08-splitzero-arithmetic-calculations.pdf](https://zenodo.org/api/records/22759785/files/08-splitzero-arithmetic-calculations.pdf/content) — 501,741 bytes; separate PDF.
- [09-unified-flow-calculations.pdf](https://zenodo.org/api/records/22759785/files/09-unified-flow-calculations.pdf/content) — 123,793 bytes; separate PDF.
- [10-splitzero-cohomology-and-weight-control.pdf](https://zenodo.org/api/records/22759785/files/10-splitzero-cohomology-and-weight-control.pdf/content) — 539,799 bytes; separate PDF.
- [11-current-calculation-sources.zip](https://zenodo.org/api/records/22759785/files/11-current-calculation-sources.zip/content) — 546,497 bytes; offline source archive.
- [12-tandem-calculation-sources.zip](https://zenodo.org/api/records/22759785/files/12-tandem-calculation-sources.zip/content) — 718,715 bytes; offline source archive.
- [13-main-reader-425p.pdf](https://zenodo.org/api/records/22759785/files/13-main-reader-425p.pdf/content) — 3,607,114 bytes; separate PDF.
- [14-splitzero-tau-kernel-continuation.pdf](https://zenodo.org/api/records/22759785/files/14-splitzero-tau-kernel-continuation.pdf/content) — 1,245,668 bytes; separate PDF.
- [15-current-integrated-sources.zip](https://zenodo.org/api/records/22759785/files/15-current-integrated-sources.zip/content) — 5,272,531 bytes; offline source archive.
- [16-tandem-continuation-sources.zip](https://zenodo.org/api/records/22759785/files/16-tandem-continuation-sources.zip/content) — 3,925,745 bytes; offline source archive.
- [17-main-reader-433p.pdf](https://zenodo.org/api/records/22759785/files/17-main-reader-433p.pdf/content) — 3,663,923 bytes; separate PDF.
- [18-splitzero-stieltjes-and-sum-connections.pdf](https://zenodo.org/api/records/22759785/files/18-splitzero-stieltjes-and-sum-connections.pdf/content) — 1,674,088 bytes; separate PDF.
- [19-current-main-and-proof-sources.zip](https://zenodo.org/api/records/22759785/files/19-current-main-and-proof-sources.zip/content) — 5,368,990 bytes; offline source archive.
- [20-tandem-stieltjes-continuation-sources.zip](https://zenodo.org/api/records/22759785/files/20-tandem-stieltjes-continuation-sources.zip/content) — 5,978,173 bytes; offline source archive.
- [21-main-reader-454p.pdf](https://zenodo.org/api/records/22759785/files/21-main-reader-454p.pdf/content) — 3,783,830 bytes; separate PDF.
- [22-splitzero-cyclic-control-and-exterior-trace.pdf](https://zenodo.org/api/records/22759785/files/22-splitzero-cyclic-control-and-exterior-trace.pdf/content) — 2,190,268 bytes; separate PDF.
- [23-current-main-and-exterior-proof-sources.zip](https://zenodo.org/api/records/22759785/files/23-current-main-and-exterior-proof-sources.zip/content) — 10,975,655 bytes; offline source archive.
- [24-tandem-cyclic-control-sources.zip](https://zenodo.org/api/records/22759785/files/24-tandem-cyclic-control-sources.zip/content) — 10,280,789 bytes; offline source archive.
- [25-main-reader-482p.pdf](https://zenodo.org/api/records/22759785/files/25-main-reader-482p.pdf/content) — 3,963,102 bytes; separate PDF.
- [26-splitzero-toda-continuation-424p.pdf](https://zenodo.org/api/records/22759785/files/26-splitzero-toda-continuation-424p.pdf/content) — 2,388,633 bytes; separate PDF.
- [27-current-main-and-toda-gamma-proof-sources.zip](https://zenodo.org/api/records/22759785/files/27-current-main-and-toda-gamma-proof-sources.zip/content) — 12,195,336 bytes; offline source archive.
- [28-tandem-toda-continuation-sources.zip](https://zenodo.org/api/records/22759785/files/28-tandem-toda-continuation-sources.zip/content) — 12,654,645 bytes; offline source archive.
- [29-main-reader-gamma-endpoint-control.pdf](https://zenodo.org/api/records/22759785/files/29-main-reader-gamma-endpoint-control.pdf/content) — 4,146,598 bytes; separate PDF.
- [30-splitzero-gamma-continuation-478p.pdf](https://zenodo.org/api/records/22759785/files/30-splitzero-gamma-continuation-478p.pdf/content) — 2,677,953 bytes; separate PDF.
- [31-current-main-and-gamma-endpoint-proof-sources.zip](https://zenodo.org/api/records/22759785/files/31-current-main-and-gamma-endpoint-proof-sources.zip/content) — 12,798,864 bytes; offline source archive.
- [32-tandem-gamma-continuation-sources.zip](https://zenodo.org/api/records/22759785/files/32-tandem-gamma-continuation-sources.zip/content) — 76,036,630 bytes; offline source archive.
- [33-splitzero-period-deligne-continuation-715p.pdf](https://zenodo.org/api/records/22759785/files/33-splitzero-period-deligne-continuation-715p.pdf/content) — 3,911,624 bytes; separate PDF.
- [34-splitzero-period-deligne-public-sources.zip](https://zenodo.org/api/records/22759785/files/34-splitzero-period-deligne-public-sources.zip/content) — 245,460,514 bytes; offline source archive.
- [35-splitzero-sga-connes-continuation-765p.pdf](https://zenodo.org/api/records/22759785/files/35-splitzero-sga-connes-continuation-765p.pdf/content) — 4,181,790 bytes; separate PDF.
- [36-splitzero-sga-connes-public-sources.zip](https://zenodo.org/api/records/22759785/files/36-splitzero-sga-connes-public-sources.zip/content) — 266,476,545 bytes; offline source archive.
- [37-splitzero-periodized-residue-continuation-821p.pdf](https://zenodo.org/api/records/22759785/files/37-splitzero-periodized-residue-continuation-821p.pdf/content) — 4,494,149 bytes; separate PDF.
- [38-splitzero-periodized-residue-public-sources.zip](https://zenodo.org/api/records/22759785/files/38-splitzero-periodized-residue-public-sources.zip/content) — 290,930,931 bytes; offline source archive.
- [39-splitzero-recursive-source-relations-public-reader.pdf](https://zenodo.org/api/records/22759785/files/39-splitzero-recursive-source-relations-public-reader.pdf/content) — 8,820,155 bytes; separate PDF.
- [40-splitzero-recursive-public-sources.zip](https://zenodo.org/api/records/22759785/files/40-splitzero-recursive-public-sources.zip/content) — 242,919,748 bytes; offline source archive.
- [41-splitzero-cumulative-graph-public-reader.pdf](https://zenodo.org/api/records/22759785/files/41-splitzero-cumulative-graph-public-reader.pdf/content) — 10,485,483 bytes; separate PDF.
- [42-splitzero-cumulative-graph-public-sources.zip](https://zenodo.org/api/records/22759785/files/42-splitzero-cumulative-graph-public-sources.zip/content) — 259,075,728 bytes; offline source archive.
- [43-joint-gamma-schur-reader.pdf](https://zenodo.org/api/records/22759785/files/43-joint-gamma-schur-reader.pdf/content) — 331,432 bytes; separate PDF.
- [44-joint-gamma-schur-public-sources.zip](https://zenodo.org/api/records/22759785/files/44-joint-gamma-schur-public-sources.zip/content) — 11,895,776 bytes; offline source archive.
- [45-original-relation-bulk-reader.pdf](https://zenodo.org/api/records/22759785/files/45-original-relation-bulk-reader.pdf/content) — 244,344 bytes; separate PDF.
- [46-original-relation-bulk-public-sources.zip](https://zenodo.org/api/records/22759785/files/46-original-relation-bulk-public-sources.zip/content) — 19,526,414 bytes; offline source archive.
- [47-complete-gamma-return-reader.pdf](https://zenodo.org/api/records/22759785/files/47-complete-gamma-return-reader.pdf/content) — 162,644 bytes; separate PDF.
- [48-complete-gamma-return-public-sources.zip](https://zenodo.org/api/records/22759785/files/48-complete-gamma-return-public-sources.zip/content) — 11,197,669 bytes; offline source archive.
- [49-gamma-growth-arithmetic-return-reader.pdf](https://zenodo.org/api/records/22759785/files/49-gamma-growth-arithmetic-return-reader.pdf/content) — 291,648 bytes; separate PDF.
- [50-gamma-growth-public-sources.zip](https://zenodo.org/api/records/22759785/files/50-gamma-growth-public-sources.zip/content) — 3,286,365 bytes; offline source archive.
- [51-original-gamma-volumes-reader.pdf](https://zenodo.org/api/records/22759785/files/51-original-gamma-volumes-reader.pdf/content) — 498,135 bytes; separate PDF.
- [52-original-gamma-volumes-public-sources.zip](https://zenodo.org/api/records/22759785/files/52-original-gamma-volumes-public-sources.zip/content) — 5,159,594 bytes; offline source archive.
- [53-original-kernel-matrices-reader.pdf](https://zenodo.org/api/records/22759785/files/53-original-kernel-matrices-reader.pdf/content) — 483,728 bytes; separate PDF.
- [54-original-kernel-matrices-sources.zip](https://zenodo.org/api/records/22759785/files/54-original-kernel-matrices-sources.zip/content) — 1,954,898 bytes; offline source archive.
- [55-conductor-kernel-reader.pdf](https://zenodo.org/api/records/22759785/files/55-conductor-kernel-reader.pdf/content) — 635,034 bytes; separate PDF.
- [56-conductor-kernel-sources.zip](https://zenodo.org/api/records/22759785/files/56-conductor-kernel-sources.zip/content) — 2,551,883 bytes; offline source archive.
- [57-exterior-kernel-reader.pdf](https://zenodo.org/api/records/22759785/files/57-exterior-kernel-reader.pdf/content) — 707,453 bytes; separate PDF.
- [58-exterior-kernel-sources.zip](https://zenodo.org/api/records/22759785/files/58-exterior-kernel-sources.zip/content) — 2,733,621 bytes; offline source archive.
- [59-quotient-moment-reader.pdf](https://zenodo.org/api/records/22759785/files/59-quotient-moment-reader.pdf/content) — 820,853 bytes; separate PDF.
- [60-quotient-moment-sources.zip](https://zenodo.org/api/records/22759785/files/60-quotient-moment-sources.zip/content) — 3,077,932 bytes; offline source archive.
