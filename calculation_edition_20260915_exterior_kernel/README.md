# Split-Zero cohomology: exterior conductor control and four-endpoint determinants

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/00_CONTINUE_HERE.md).

[Read the current 110-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22758970/files/57-exterior-kernel-reader.pdf/content) · [Published DOI 10.5281/zenodo.22758970](https://doi.org/10.5281/zenodo.22758970).

- [110-page exterior kernel](https://zenodo.org/api/records/22758970/files/57-exterior-kernel-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation) · [offline source ZIP](https://zenodo.org/api/records/22758970/files/58-exterior-kernel-sources.zip/content).

The current 110-page reader adds the complete RUI/CEP exterior-conductor proofs to the original kernel, residue, finite-bound and minimum-section constructions. It proves a subleading o(kq) error for the actual conductor transport at each fixed period, all four original endpoints and all actual exterior ranks. The seventeen-file package preserves the sole owner prompt, complete updated receivers and recorded PR32 source/CI.

## What this calculation studies

Split-Zero follows a finite arithmetic quotient attached to a selected zeta-zero
packet, together with its original theta cohomology and mixed-support maps.
The specified period observation loses a subspace K. The calculation measures
that same kernel using the original fixed-Gamma, tensor-Gamma and arithmetic
source metrics at four degrees: q-1, q, 2q-1 and 2q. This is K at the specified
period, not an intersection over periods.

The purpose is to determine the kernel contribution to the original signed
cohomological return. An actual conductor polynomial gives a concrete map to
a smaller root grid. Earlier work constructed its inverse; this edition proves
that its four-endpoint determinant error is subleading. The remaining work is
now an explicit difference of original total determinants and an actual
residual observation determinant, not the older conductor-conditioning problem.

The main simple-quartet lane retains m=1, k=4l+1 with l>=1, q=(k+1)^2,
c=k/2, 0<delta<1/2 and gamma>2, on each original branch |u|>=R_*.
R_* is calculated from the actual quartet and full unit, and dim K=r=8k-16
on this domain. The all-multiplicity geometry and primary nilpotents remain
in the sources; this simple-quartet rank is not assigned to other multiplicities.
For k>=9, the actual conductor uses all 81 biform coefficients, its first
nonzero moment denominator and the exact lower grid. No generic period
matrix or assumed nonzero minor replaces those data.

## The completed conductor estimate

RUI uses the original finite conductor's determinant-one property. On the
degree-N source, its complementary exterior norms satisfy

    ||wedge^t T^(-1)|| = ||wedge^(N+1-t) T||
       <= [C_v exp(B_sh(H_N+2))]^(N+1-t),
    T = B_(N+1)(partial).

All coefficient constants and the moment denominator remain in this bound.
CEP extends it through the original endpoint maps, the exact low-degree
relation graph and all actual exterior ranks. The precise current identity is

    F_K^(s) = T_k^(s) - F_(Xi,k)^(s) + E_(A,k)^(s),
    |E_(A,k)^(s)| <= epsilon_k^(s) = 2 sum_N E_N^(s) = o(kq).

Here s remains the original source order 1 or k, and

    T_k^(s) = sum_N sigma_N
                 (log det G_N^(s) - log det G'_(N-v)^(s)),
    F_(Xi,k)^(s) = sum_N sigma_N log det Q_(Xi,N)^(s),
    N = q-1, q, 2q-1, 2q; sigma = (1, 1, -1, -1).

G and G' are the original upper- and lower-grid total Grams; Q_Xi is the
actual residual observation quotient Gram. The lower grid keeps
k'=k-8, q'=(k-7)^2, Delta=q-q'=16k-48, centre c'=c-4 and cutoffs N-v.
Its source order is still the original s. The retained map
Xi: V_A -> V_A/K has rank 8k-32. Its rank does not determine its volume:
the full graph, cross terms, coefficients and original action defect remain.

The estimate o(kq) holds for each fixed actual period, at all four original
endpoints and all actual exterior ranks. It sharpens the previous AIE
O(kq) exterior error **for this actual conductor transport**. AIE's finite
inverse and exact quotient maps remain valid. This is not a general
improvement for unrelated maps, nor a uniform bound for moving periods.

## What remains to calculate

The next two quantities are T_k^(s) and F_(Xi,k)^(s), in their displayed
original combination. Relative to the lower grid's natural endpoints,
the shifts are Delta-v at the lower pair and 2Delta-v at the upper pair.
The next total-Gram calculation must retain these shifts, roots, masses and
centres and control the first variation. The existing q^2 leading estimate
does not itself supply that error bound.

The other calculation is the actual rank-(8k-32) Xi observation determinant,
or equivalently its full low-degree graph quotient with cross terms.
No leading coefficient is inferred from rank alone. Bounds on the actual
period-dependent constants would be needed for a moving-period extension;
such uniformity is not claimed in this edition.

AKS's preceding bound retains its finite pointwise minimum with the original
KAF estimate and first actual increment:

    d_1^(s) <= F_K^(s)
       <= min(2r log Z_(k,1),
              r(L_(s,q)+L_(s,q+1)) - d_1^(s)),
    limsup F_K^a/(kq) <= 32 log(25 log 3/(4 pi))
                      < 25.02078097650.

Here L_(s,j) denotes AKS's actual finite covariance bound. The original
fixed-Gamma, tensor-Gamma and arithmetic ratios share limit points.
**No unique limit or exact leading value is asserted.** The original q^2
baseline and finite centre with its nonzero error radius remain intact.

The actual conductor error is now proved subleading. The next calculations are the shifted upper/lower total-Gram difference and the retained original rank-(8k-32) Xi observation determinant in F_K=T-F_Xi+E_A. No unique leading value, moving-period uniformity or RH conclusion is asserted; later CTV/Xi drafts are outside this edition.

## Complete proofs, receivers and checked-source scope

[File14: complete current proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) contains all preceding chapters
and the complete RUI1-15 and CEP1-49 proofs; it is the editable source of the
current 110-page reader. The source/remainder square, omitted-root products,
determinant phase, ideal map, low-degree graph and action defect are explicit.
[Arithmetic source transfer, file13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex)
retains the finite errors, correlated arithmetic allowances and source maps.

[Joint receiver09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/09_UPDATED_JOINT_NOTE.tex) and
[signed receiver10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/10_UPDATED_SIGNED_RETURN.tex) retain all 31
preceding providers and the complete OCF/OKM/OKA/OMG/AKS/AKJ/AKP/AIE/RUI/CEP
proofs. Their current receiving sites are MRI4e-k and BRI6c-e; newly installed
MRI4g-k and BRI6e carry the refined intervals and exact signed consequences.
The original theta primitive and corrected minimum section remain intact.
The 226/218-page receiver builds establish compilation and source closure,
not visual approval of receiver PDFs.

The delivered reader's full 110 pages have the owner's visual acceptance:
93 page images match the accepted predecessor, four changed earlier pages
were inspected individually, and every new page98-110 was inspected
individually. The complete new written proofs and receiving changes have
independent acceptance. Finite diagnostic fixtures exercise their declared
endpoint shapes; they are not evaluations at actual zeta zeros or periods.

[File16: complete PR32 formal source and proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md)
is unchanged. It preserves four new Lean modules, the full note, runner and
recorded successful two-job CI at implementation
8e78bc7c240b04d297ade6afdadfd863e0c6db7b, with unchanged checked source at final
head9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6. Its receipt covers 33 local modules
and 56 selected transitive axiom targets. The new analytic estimates have
written-proof scope; no new local Lean run or PR merge is claimed here.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/12_VALIDATION.md) records these exact scopes.
[Source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/11_SOURCE_MAP.json) distinguishes owner-original
SHA-256 `242ff297064007ffdb435cd36f6c0884e2a50bc58797237a0840428b37b829f1` from public transported SHA-256
`269397ca3e92a083c451cb9016cd9ccbcb1f769a455f057e3138611d547ed79c`. Its metadata-only transport scope is:
735 literal private-account locator occurrences transported across 698 values and eight path-valued review keys, including nested JSON. Full mathematical bodies, source hashes and other metadata stay unchanged; embedded original identities still identify the original sources. The other sixteen files are unchanged.

This is exactly the accepted seventeen-file edition and the sole current
owner prompt. No competing prompt is created. Later CTV/Xi drafts are not
included. Earlier 97-page, 72-page and Gamma editions remain immutable
historical sources, rather than the current next-calculation statement.

## Earlier complete source editions

- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 56-download edition](https://doi.org/10.5281/zenodo.22758735) remains frozen
with its 97-page preview. This edition adds PDF57 and ZIP58. The actual
new browser preview is the current 110-page PDF57; ZIP58 supplies all seventeen
flat source files for offline use, not a substitute preview. Every earlier
mathematical/source file remains unchanged.


[Release provenance](RELEASE.json) · [All file identities](ALL_ZENODO_FILES.json).

## All 58 downloads

- [57-exterior-kernel-reader.pdf](https://zenodo.org/api/records/22758970/files/57-exterior-kernel-reader.pdf/content) — 707,453 bytes; separate PDF.
- [58-exterior-kernel-sources.zip](https://zenodo.org/api/records/22758970/files/58-exterior-kernel-sources.zip/content) — 2,733,621 bytes; offline source archive.
- [01-main-reader.pdf](https://zenodo.org/api/records/22758970/files/01-main-reader.pdf/content) — 3,502,600 bytes; separate PDF.
- [02-fluid-reader.pdf](https://zenodo.org/api/records/22758970/files/02-fluid-reader.pdf/content) — 2,063,023 bytes; separate PDF.
- [03-heat-reader.pdf](https://zenodo.org/api/records/22758970/files/03-heat-reader.pdf/content) — 1,266,114 bytes; separate PDF.
- [04-connes-reader.pdf](https://zenodo.org/api/records/22758970/files/04-connes-reader.pdf/content) — 954,841 bytes; separate PDF.
- [05-gct-reader.pdf](https://zenodo.org/api/records/22758970/files/05-gct-reader.pdf/content) — 1,624,359 bytes; separate PDF.
- [06-vacuum-reader.pdf](https://zenodo.org/api/records/22758970/files/06-vacuum-reader.pdf/content) — 676,386 bytes; separate PDF.
- [07-complete-mathematical-sources.zip](https://zenodo.org/api/records/22758970/files/07-complete-mathematical-sources.zip/content) — 12,343,724 bytes; offline source archive.
- [08-splitzero-arithmetic-calculations.pdf](https://zenodo.org/api/records/22758970/files/08-splitzero-arithmetic-calculations.pdf/content) — 501,741 bytes; separate PDF.
- [09-unified-flow-calculations.pdf](https://zenodo.org/api/records/22758970/files/09-unified-flow-calculations.pdf/content) — 123,793 bytes; separate PDF.
- [10-splitzero-cohomology-and-weight-control.pdf](https://zenodo.org/api/records/22758970/files/10-splitzero-cohomology-and-weight-control.pdf/content) — 539,799 bytes; separate PDF.
- [11-current-calculation-sources.zip](https://zenodo.org/api/records/22758970/files/11-current-calculation-sources.zip/content) — 546,497 bytes; offline source archive.
- [12-tandem-calculation-sources.zip](https://zenodo.org/api/records/22758970/files/12-tandem-calculation-sources.zip/content) — 718,715 bytes; offline source archive.
- [13-main-reader-425p.pdf](https://zenodo.org/api/records/22758970/files/13-main-reader-425p.pdf/content) — 3,607,114 bytes; separate PDF.
- [14-splitzero-tau-kernel-continuation.pdf](https://zenodo.org/api/records/22758970/files/14-splitzero-tau-kernel-continuation.pdf/content) — 1,245,668 bytes; separate PDF.
- [15-current-integrated-sources.zip](https://zenodo.org/api/records/22758970/files/15-current-integrated-sources.zip/content) — 5,272,531 bytes; offline source archive.
- [16-tandem-continuation-sources.zip](https://zenodo.org/api/records/22758970/files/16-tandem-continuation-sources.zip/content) — 3,925,745 bytes; offline source archive.
- [17-main-reader-433p.pdf](https://zenodo.org/api/records/22758970/files/17-main-reader-433p.pdf/content) — 3,663,923 bytes; separate PDF.
- [18-splitzero-stieltjes-and-sum-connections.pdf](https://zenodo.org/api/records/22758970/files/18-splitzero-stieltjes-and-sum-connections.pdf/content) — 1,674,088 bytes; separate PDF.
- [19-current-main-and-proof-sources.zip](https://zenodo.org/api/records/22758970/files/19-current-main-and-proof-sources.zip/content) — 5,368,990 bytes; offline source archive.
- [20-tandem-stieltjes-continuation-sources.zip](https://zenodo.org/api/records/22758970/files/20-tandem-stieltjes-continuation-sources.zip/content) — 5,978,173 bytes; offline source archive.
- [21-main-reader-454p.pdf](https://zenodo.org/api/records/22758970/files/21-main-reader-454p.pdf/content) — 3,783,830 bytes; separate PDF.
- [22-splitzero-cyclic-control-and-exterior-trace.pdf](https://zenodo.org/api/records/22758970/files/22-splitzero-cyclic-control-and-exterior-trace.pdf/content) — 2,190,268 bytes; separate PDF.
- [23-current-main-and-exterior-proof-sources.zip](https://zenodo.org/api/records/22758970/files/23-current-main-and-exterior-proof-sources.zip/content) — 10,975,655 bytes; offline source archive.
- [24-tandem-cyclic-control-sources.zip](https://zenodo.org/api/records/22758970/files/24-tandem-cyclic-control-sources.zip/content) — 10,280,789 bytes; offline source archive.
- [25-main-reader-482p.pdf](https://zenodo.org/api/records/22758970/files/25-main-reader-482p.pdf/content) — 3,963,102 bytes; separate PDF.
- [26-splitzero-toda-continuation-424p.pdf](https://zenodo.org/api/records/22758970/files/26-splitzero-toda-continuation-424p.pdf/content) — 2,388,633 bytes; separate PDF.
- [27-current-main-and-toda-gamma-proof-sources.zip](https://zenodo.org/api/records/22758970/files/27-current-main-and-toda-gamma-proof-sources.zip/content) — 12,195,336 bytes; offline source archive.
- [28-tandem-toda-continuation-sources.zip](https://zenodo.org/api/records/22758970/files/28-tandem-toda-continuation-sources.zip/content) — 12,654,645 bytes; offline source archive.
- [29-main-reader-gamma-endpoint-control.pdf](https://zenodo.org/api/records/22758970/files/29-main-reader-gamma-endpoint-control.pdf/content) — 4,146,598 bytes; separate PDF.
- [30-splitzero-gamma-continuation-478p.pdf](https://zenodo.org/api/records/22758970/files/30-splitzero-gamma-continuation-478p.pdf/content) — 2,677,953 bytes; separate PDF.
- [31-current-main-and-gamma-endpoint-proof-sources.zip](https://zenodo.org/api/records/22758970/files/31-current-main-and-gamma-endpoint-proof-sources.zip/content) — 12,798,864 bytes; offline source archive.
- [32-tandem-gamma-continuation-sources.zip](https://zenodo.org/api/records/22758970/files/32-tandem-gamma-continuation-sources.zip/content) — 76,036,630 bytes; offline source archive.
- [33-splitzero-period-deligne-continuation-715p.pdf](https://zenodo.org/api/records/22758970/files/33-splitzero-period-deligne-continuation-715p.pdf/content) — 3,911,624 bytes; separate PDF.
- [34-splitzero-period-deligne-public-sources.zip](https://zenodo.org/api/records/22758970/files/34-splitzero-period-deligne-public-sources.zip/content) — 245,460,514 bytes; offline source archive.
- [35-splitzero-sga-connes-continuation-765p.pdf](https://zenodo.org/api/records/22758970/files/35-splitzero-sga-connes-continuation-765p.pdf/content) — 4,181,790 bytes; separate PDF.
- [36-splitzero-sga-connes-public-sources.zip](https://zenodo.org/api/records/22758970/files/36-splitzero-sga-connes-public-sources.zip/content) — 266,476,545 bytes; offline source archive.
- [37-splitzero-periodized-residue-continuation-821p.pdf](https://zenodo.org/api/records/22758970/files/37-splitzero-periodized-residue-continuation-821p.pdf/content) — 4,494,149 bytes; separate PDF.
- [38-splitzero-periodized-residue-public-sources.zip](https://zenodo.org/api/records/22758970/files/38-splitzero-periodized-residue-public-sources.zip/content) — 290,930,931 bytes; offline source archive.
- [39-splitzero-recursive-source-relations-public-reader.pdf](https://zenodo.org/api/records/22758970/files/39-splitzero-recursive-source-relations-public-reader.pdf/content) — 8,820,155 bytes; separate PDF.
- [40-splitzero-recursive-public-sources.zip](https://zenodo.org/api/records/22758970/files/40-splitzero-recursive-public-sources.zip/content) — 242,919,748 bytes; offline source archive.
- [41-splitzero-cumulative-graph-public-reader.pdf](https://zenodo.org/api/records/22758970/files/41-splitzero-cumulative-graph-public-reader.pdf/content) — 10,485,483 bytes; separate PDF.
- [42-splitzero-cumulative-graph-public-sources.zip](https://zenodo.org/api/records/22758970/files/42-splitzero-cumulative-graph-public-sources.zip/content) — 259,075,728 bytes; offline source archive.
- [43-joint-gamma-schur-reader.pdf](https://zenodo.org/api/records/22758970/files/43-joint-gamma-schur-reader.pdf/content) — 331,432 bytes; separate PDF.
- [44-joint-gamma-schur-public-sources.zip](https://zenodo.org/api/records/22758970/files/44-joint-gamma-schur-public-sources.zip/content) — 11,895,776 bytes; offline source archive.
- [45-original-relation-bulk-reader.pdf](https://zenodo.org/api/records/22758970/files/45-original-relation-bulk-reader.pdf/content) — 244,344 bytes; separate PDF.
- [46-original-relation-bulk-public-sources.zip](https://zenodo.org/api/records/22758970/files/46-original-relation-bulk-public-sources.zip/content) — 19,526,414 bytes; offline source archive.
- [47-complete-gamma-return-reader.pdf](https://zenodo.org/api/records/22758970/files/47-complete-gamma-return-reader.pdf/content) — 162,644 bytes; separate PDF.
- [48-complete-gamma-return-public-sources.zip](https://zenodo.org/api/records/22758970/files/48-complete-gamma-return-public-sources.zip/content) — 11,197,669 bytes; offline source archive.
- [49-gamma-growth-arithmetic-return-reader.pdf](https://zenodo.org/api/records/22758970/files/49-gamma-growth-arithmetic-return-reader.pdf/content) — 291,648 bytes; separate PDF.
- [50-gamma-growth-public-sources.zip](https://zenodo.org/api/records/22758970/files/50-gamma-growth-public-sources.zip/content) — 3,286,365 bytes; offline source archive.
- [51-original-gamma-volumes-reader.pdf](https://zenodo.org/api/records/22758970/files/51-original-gamma-volumes-reader.pdf/content) — 498,135 bytes; separate PDF.
- [52-original-gamma-volumes-public-sources.zip](https://zenodo.org/api/records/22758970/files/52-original-gamma-volumes-public-sources.zip/content) — 5,159,594 bytes; offline source archive.
- [53-original-kernel-matrices-reader.pdf](https://zenodo.org/api/records/22758970/files/53-original-kernel-matrices-reader.pdf/content) — 483,728 bytes; separate PDF.
- [54-original-kernel-matrices-sources.zip](https://zenodo.org/api/records/22758970/files/54-original-kernel-matrices-sources.zip/content) — 1,954,898 bytes; offline source archive.
- [55-conductor-kernel-reader.pdf](https://zenodo.org/api/records/22758970/files/55-conductor-kernel-reader.pdf/content) — 635,034 bytes; separate PDF.
- [56-conductor-kernel-sources.zip](https://zenodo.org/api/records/22758970/files/56-conductor-kernel-sources.zip/content) — 2,551,883 bytes; offline source archive.
