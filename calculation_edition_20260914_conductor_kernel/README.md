# Split-Zero cohomology: conductor inverses and four-endpoint kernel control

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/00_CONTINUE_HERE.md).

[Read the current 97-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22758735/files/55-conductor-kernel-reader.pdf/content) · [Published DOI 10.5281/zenodo.22758735](https://doi.org/10.5281/zenodo.22758735).

- [97-page conductor kernel](https://zenodo.org/api/records/22758735/files/55-conductor-kernel-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation) · [offline source ZIP](https://zenodo.org/api/records/22758735/files/56-conductor-kernel-sources.zip/content).

The current 97-page reader contains complete original kernel, conductor, residue and minimum-section proofs, with the sharper finite four-endpoint control and its retained KAF minimum. The seventeen-file package includes the exact current owner prompt, complete updated receivers and the complete PR32 formal source with written proofs and observed CI records. Original source metrics, unit jets, periods and multiplicities remain.

## What this calculation studies

Split-Zero studies a finite arithmetic quotient built from a selected zeta-zero
packet, together with the original theta cohomology and mixed-support maps.
This calculation follows the part of that quotient lost by a specified period
observation. That part is its kernel K. The same K is measured using the original
fixed-Gamma, tensor-Gamma and arithmetic source metrics, at four source degrees
q-1, q, 2q-1 and 2q. It is the kernel at the given period, not an intersection
over different periods.

The purpose is to calculate that kernel's contribution to the original signed
cohomological return. A conductor polynomial supplies an explicit coefficient
map into the kernel calculation. Here its inverse, degree information and metric
bounds are worked out in full, then returned to the existing joint and signed
receivers. The next step remains the actual leading determinant value, not the
introduction of a different observation or an assumed RH counterexample.

For the main simple-quartet lane, the source retains m=1, k=4l+1 with l>=1,
q=(k+1)^2, c=k/2, 0<delta<1/2 and gamma>2, on every original period branch
|u|>=R_*. The radius R_* is calculated from the actual quartet and full unit.
The proved kernel dimension is r=8k-16 on this domain. The full
all-multiplicity geometry and primary nilpotents remain in the sources;
that simple-quartet rank is not assigned to other multiplicities.

## What is now completed

For each original source s, the four compressed source Grams are
H_j^(s)=T_s^* (K_j^(s))^(-1) T_s, with T_s=C_s^(-1) I_K.
Their signed logarithmic determinant combination is

    F_K^(s) = log det H_0^(s) + log det H_1^(s)
              - log det H_q^(s) - log det H_(q+1)^(s).

AKS retains the first actual increment d_1^(s), its finite covariance bounds
L_(s,j), and the finite pointwise minimum with the previous KAF estimate:

    d_1^(s) <= F_K^(s)
       <= min(2r log Z_(k,1),
              r(L_(s,q)+L_(s,q+1)) - d_1^(s)).

The original fixed-Gamma, tensor-Gamma and arithmetic ratios have common limit
points and the sharper uniform upper ceiling

    limsup F_K^a/(kq) <= 32 log(25 log 3/(4 pi))
                      < 25.02078097650.

The complete original finite estimate is retained, not replaced by its
asymptotic ceiling. **No unique limit or exact leading value is asserted.**

AKJ proves the exact passage between the projector determinant and the
original conductor-frame determinant, including its endpoint-independent
denominator. It gives the residue inverse in the actual i^D D! primary
coefficients, the invisible primary ideals and the inclusion into K.
For k>=9, its conductor degree flag has O(k^2) deficit. All 81 actual biform
coefficients and the first nonzero moment denominator are retained.

AKP proves the theta primitive correction when changing a polynomial lift,
and the full corrected minimum-section/residual-Gram map. AIE gives a literal
finite conductor inverse, its actual coefficient-dependent norm, the
low-degree correction and exact quotient/exterior transfer. Its fixed-period
operator-log bound is O(q); exterior power keeps its rank multiplier and gives
O(kq), not a smaller volume error.

The finite inverse acts on coefficient representatives D<=q-1. At the larger
source endpoints, the same coefficient frame uses the original minimum-remainder
Gram G_N. The inverse bound does not silently substitute the source cutoff N
for the coefficient cutoff D. Original Gamma orders stay 1 and k, and source
masses, unit jets, phases, periods and all four endpoint roles remain explicit.

The conductor inverse and finite four-endpoint bounds are completed. Their operator-log O(q) estimate has a rank factor in the exterior metric, leaving O(kq) volume loss. The next calculation is the fixed-period leading common-kernel determinant in its original four minimum-remainder Grams. No unique limit, exact leading value or RH conclusion is asserted.

## Complete proofs, receiving maps and checked-source scope

[File14: complete current proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) contains all thirteen preceding
chapters and the full AKS, AKJ, AKP and AIE developments; it is the editable
source of the current 97-page reader. [Arithmetic source transfer, file13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex)
retains the signed finite errors and source-comparison maps.
[Joint receiver09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/09_UPDATED_JOINT_NOTE.tex) and
[signed receiver10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/10_UPDATED_SIGNED_RETURN.tex) retain all 31
preceding full providers and append the complete OCF/OKM/OKA/OMG/AKS/AKJ/AKP/AIE
proofs. MRI4e-f and BRI6c-d now contain the new finite bounds, correlated
arithmetic complements and signed consequences. The 211/203-page receiver
builds establish source closure and compilation, not visual approval of new
receiver PDFs. All 97 pages of the delivered current reader have the owner's
complete visual acceptance.

[File16: complete PR32 formal source and proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md)
contains the four new Lean modules, full written note, runner and recorded CI.
The recorded strict implementation is
8e78bc7c240b04d297ade6afdadfd863e0c6db7b; final documentation/source head
9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6 changes no checked Lean, runner, test
or workflow source. Both observed CI jobs passed, covering 33 local modules
and 56 selected transitive axiom reports. The finite section, residual Gram,
observed iterates and residue-annihilator statements have that checked scope.
The analytic estimates and polynomial-gcd dimension result retain written-proof
scope. No new local Lean run, actual zeta-zero evaluation or PR merge is claimed.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/12_VALIDATION.md) records these exact scopes.
[Source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/11_SOURCE_MAP.json) distinguishes owner-original
SHA-256 `cb9f2fb6ef611445529f7cb067d1cbec6a2edd60eb9f1b893e750787049b44c8` from public transported SHA-256
`2f774ae49790357ea1306254d1837937c6f4386d9e571c61789aaa8f347d1cd6`. Its metadata-only transport scope is:
722 literal private-account locator occurrences transported across 685 values and eight path-valued review keys, including nested JSON. Full mathematical bodies, source hashes and other metadata stay unchanged; embedded original identities still identify the original sources. The other sixteen files are unchanged.

This is exactly the accepted seventeen-file source edition. Its single current
prompt belongs to the mathematical owner; this index creates no competing
continuation prompt. The earlier sixteen-file edition, 72-page reader and
preceding Gamma reader remain intact as historical sources.

## Earlier complete source editions

- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 54-download edition](https://doi.org/10.5281/zenodo.22758480) remains frozen
with its 72-page preview. This edition adds PDF55 and ZIP56; the actual new
browser preview is the current 97-page PDF55. ZIP56 supplies all seventeen
flat source files for offline use, not a substitute preview. Every earlier
mathematical/source file remains unchanged.


[Release provenance](RELEASE.json) · [All file identities](ALL_ZENODO_FILES.json).

## All 56 downloads

- [55-conductor-kernel-reader.pdf](https://zenodo.org/api/records/22758735/files/55-conductor-kernel-reader.pdf/content) — 635,034 bytes; separate PDF.
- [56-conductor-kernel-sources.zip](https://zenodo.org/api/records/22758735/files/56-conductor-kernel-sources.zip/content) — 2,551,883 bytes; offline source archive.
- [01-main-reader.pdf](https://zenodo.org/api/records/22758735/files/01-main-reader.pdf/content) — 3,502,600 bytes; separate PDF.
- [02-fluid-reader.pdf](https://zenodo.org/api/records/22758735/files/02-fluid-reader.pdf/content) — 2,063,023 bytes; separate PDF.
- [03-heat-reader.pdf](https://zenodo.org/api/records/22758735/files/03-heat-reader.pdf/content) — 1,266,114 bytes; separate PDF.
- [04-connes-reader.pdf](https://zenodo.org/api/records/22758735/files/04-connes-reader.pdf/content) — 954,841 bytes; separate PDF.
- [05-gct-reader.pdf](https://zenodo.org/api/records/22758735/files/05-gct-reader.pdf/content) — 1,624,359 bytes; separate PDF.
- [06-vacuum-reader.pdf](https://zenodo.org/api/records/22758735/files/06-vacuum-reader.pdf/content) — 676,386 bytes; separate PDF.
- [07-complete-mathematical-sources.zip](https://zenodo.org/api/records/22758735/files/07-complete-mathematical-sources.zip/content) — 12,343,724 bytes; offline source archive.
- [08-splitzero-arithmetic-calculations.pdf](https://zenodo.org/api/records/22758735/files/08-splitzero-arithmetic-calculations.pdf/content) — 501,741 bytes; separate PDF.
- [09-unified-flow-calculations.pdf](https://zenodo.org/api/records/22758735/files/09-unified-flow-calculations.pdf/content) — 123,793 bytes; separate PDF.
- [10-splitzero-cohomology-and-weight-control.pdf](https://zenodo.org/api/records/22758735/files/10-splitzero-cohomology-and-weight-control.pdf/content) — 539,799 bytes; separate PDF.
- [11-current-calculation-sources.zip](https://zenodo.org/api/records/22758735/files/11-current-calculation-sources.zip/content) — 546,497 bytes; offline source archive.
- [12-tandem-calculation-sources.zip](https://zenodo.org/api/records/22758735/files/12-tandem-calculation-sources.zip/content) — 718,715 bytes; offline source archive.
- [13-main-reader-425p.pdf](https://zenodo.org/api/records/22758735/files/13-main-reader-425p.pdf/content) — 3,607,114 bytes; separate PDF.
- [14-splitzero-tau-kernel-continuation.pdf](https://zenodo.org/api/records/22758735/files/14-splitzero-tau-kernel-continuation.pdf/content) — 1,245,668 bytes; separate PDF.
- [15-current-integrated-sources.zip](https://zenodo.org/api/records/22758735/files/15-current-integrated-sources.zip/content) — 5,272,531 bytes; offline source archive.
- [16-tandem-continuation-sources.zip](https://zenodo.org/api/records/22758735/files/16-tandem-continuation-sources.zip/content) — 3,925,745 bytes; offline source archive.
- [17-main-reader-433p.pdf](https://zenodo.org/api/records/22758735/files/17-main-reader-433p.pdf/content) — 3,663,923 bytes; separate PDF.
- [18-splitzero-stieltjes-and-sum-connections.pdf](https://zenodo.org/api/records/22758735/files/18-splitzero-stieltjes-and-sum-connections.pdf/content) — 1,674,088 bytes; separate PDF.
- [19-current-main-and-proof-sources.zip](https://zenodo.org/api/records/22758735/files/19-current-main-and-proof-sources.zip/content) — 5,368,990 bytes; offline source archive.
- [20-tandem-stieltjes-continuation-sources.zip](https://zenodo.org/api/records/22758735/files/20-tandem-stieltjes-continuation-sources.zip/content) — 5,978,173 bytes; offline source archive.
- [21-main-reader-454p.pdf](https://zenodo.org/api/records/22758735/files/21-main-reader-454p.pdf/content) — 3,783,830 bytes; separate PDF.
- [22-splitzero-cyclic-control-and-exterior-trace.pdf](https://zenodo.org/api/records/22758735/files/22-splitzero-cyclic-control-and-exterior-trace.pdf/content) — 2,190,268 bytes; separate PDF.
- [23-current-main-and-exterior-proof-sources.zip](https://zenodo.org/api/records/22758735/files/23-current-main-and-exterior-proof-sources.zip/content) — 10,975,655 bytes; offline source archive.
- [24-tandem-cyclic-control-sources.zip](https://zenodo.org/api/records/22758735/files/24-tandem-cyclic-control-sources.zip/content) — 10,280,789 bytes; offline source archive.
- [25-main-reader-482p.pdf](https://zenodo.org/api/records/22758735/files/25-main-reader-482p.pdf/content) — 3,963,102 bytes; separate PDF.
- [26-splitzero-toda-continuation-424p.pdf](https://zenodo.org/api/records/22758735/files/26-splitzero-toda-continuation-424p.pdf/content) — 2,388,633 bytes; separate PDF.
- [27-current-main-and-toda-gamma-proof-sources.zip](https://zenodo.org/api/records/22758735/files/27-current-main-and-toda-gamma-proof-sources.zip/content) — 12,195,336 bytes; offline source archive.
- [28-tandem-toda-continuation-sources.zip](https://zenodo.org/api/records/22758735/files/28-tandem-toda-continuation-sources.zip/content) — 12,654,645 bytes; offline source archive.
- [29-main-reader-gamma-endpoint-control.pdf](https://zenodo.org/api/records/22758735/files/29-main-reader-gamma-endpoint-control.pdf/content) — 4,146,598 bytes; separate PDF.
- [30-splitzero-gamma-continuation-478p.pdf](https://zenodo.org/api/records/22758735/files/30-splitzero-gamma-continuation-478p.pdf/content) — 2,677,953 bytes; separate PDF.
- [31-current-main-and-gamma-endpoint-proof-sources.zip](https://zenodo.org/api/records/22758735/files/31-current-main-and-gamma-endpoint-proof-sources.zip/content) — 12,798,864 bytes; offline source archive.
- [32-tandem-gamma-continuation-sources.zip](https://zenodo.org/api/records/22758735/files/32-tandem-gamma-continuation-sources.zip/content) — 76,036,630 bytes; offline source archive.
- [33-splitzero-period-deligne-continuation-715p.pdf](https://zenodo.org/api/records/22758735/files/33-splitzero-period-deligne-continuation-715p.pdf/content) — 3,911,624 bytes; separate PDF.
- [34-splitzero-period-deligne-public-sources.zip](https://zenodo.org/api/records/22758735/files/34-splitzero-period-deligne-public-sources.zip/content) — 245,460,514 bytes; offline source archive.
- [35-splitzero-sga-connes-continuation-765p.pdf](https://zenodo.org/api/records/22758735/files/35-splitzero-sga-connes-continuation-765p.pdf/content) — 4,181,790 bytes; separate PDF.
- [36-splitzero-sga-connes-public-sources.zip](https://zenodo.org/api/records/22758735/files/36-splitzero-sga-connes-public-sources.zip/content) — 266,476,545 bytes; offline source archive.
- [37-splitzero-periodized-residue-continuation-821p.pdf](https://zenodo.org/api/records/22758735/files/37-splitzero-periodized-residue-continuation-821p.pdf/content) — 4,494,149 bytes; separate PDF.
- [38-splitzero-periodized-residue-public-sources.zip](https://zenodo.org/api/records/22758735/files/38-splitzero-periodized-residue-public-sources.zip/content) — 290,930,931 bytes; offline source archive.
- [39-splitzero-recursive-source-relations-public-reader.pdf](https://zenodo.org/api/records/22758735/files/39-splitzero-recursive-source-relations-public-reader.pdf/content) — 8,820,155 bytes; separate PDF.
- [40-splitzero-recursive-public-sources.zip](https://zenodo.org/api/records/22758735/files/40-splitzero-recursive-public-sources.zip/content) — 242,919,748 bytes; offline source archive.
- [41-splitzero-cumulative-graph-public-reader.pdf](https://zenodo.org/api/records/22758735/files/41-splitzero-cumulative-graph-public-reader.pdf/content) — 10,485,483 bytes; separate PDF.
- [42-splitzero-cumulative-graph-public-sources.zip](https://zenodo.org/api/records/22758735/files/42-splitzero-cumulative-graph-public-sources.zip/content) — 259,075,728 bytes; offline source archive.
- [43-joint-gamma-schur-reader.pdf](https://zenodo.org/api/records/22758735/files/43-joint-gamma-schur-reader.pdf/content) — 331,432 bytes; separate PDF.
- [44-joint-gamma-schur-public-sources.zip](https://zenodo.org/api/records/22758735/files/44-joint-gamma-schur-public-sources.zip/content) — 11,895,776 bytes; offline source archive.
- [45-original-relation-bulk-reader.pdf](https://zenodo.org/api/records/22758735/files/45-original-relation-bulk-reader.pdf/content) — 244,344 bytes; separate PDF.
- [46-original-relation-bulk-public-sources.zip](https://zenodo.org/api/records/22758735/files/46-original-relation-bulk-public-sources.zip/content) — 19,526,414 bytes; offline source archive.
- [47-complete-gamma-return-reader.pdf](https://zenodo.org/api/records/22758735/files/47-complete-gamma-return-reader.pdf/content) — 162,644 bytes; separate PDF.
- [48-complete-gamma-return-public-sources.zip](https://zenodo.org/api/records/22758735/files/48-complete-gamma-return-public-sources.zip/content) — 11,197,669 bytes; offline source archive.
- [49-gamma-growth-arithmetic-return-reader.pdf](https://zenodo.org/api/records/22758735/files/49-gamma-growth-arithmetic-return-reader.pdf/content) — 291,648 bytes; separate PDF.
- [50-gamma-growth-public-sources.zip](https://zenodo.org/api/records/22758735/files/50-gamma-growth-public-sources.zip/content) — 3,286,365 bytes; offline source archive.
- [51-original-gamma-volumes-reader.pdf](https://zenodo.org/api/records/22758735/files/51-original-gamma-volumes-reader.pdf/content) — 498,135 bytes; separate PDF.
- [52-original-gamma-volumes-public-sources.zip](https://zenodo.org/api/records/22758735/files/52-original-gamma-volumes-public-sources.zip/content) — 5,159,594 bytes; offline source archive.
- [53-original-kernel-matrices-reader.pdf](https://zenodo.org/api/records/22758735/files/53-original-kernel-matrices-reader.pdf/content) — 483,728 bytes; separate PDF.
- [54-original-kernel-matrices-sources.zip](https://zenodo.org/api/records/22758735/files/54-original-kernel-matrices-sources.zip/content) — 1,954,898 bytes; offline source archive.
