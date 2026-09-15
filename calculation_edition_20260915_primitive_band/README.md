# Split-Zero cohomology: source-volume estimates and boundary transport

[Read the delivered 549-page cumulative paper](https://zenodo.org/api/records/22773401/files/74-primitive-band-reader.pdf/content) · [Read the accepted 40-page source-band and boundary continuation](https://zenodo.org/api/records/22773401/files/75-primitive-band-supplement.pdf/content) · [DOI 10.5281/zenodo.22773401](https://doi.org/10.5281/zenodo.22773401) · [Exact current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/00_CONTINUE_HERE.md).

- [549-page primitive_band](https://zenodo.org/api/records/22773401/files/74-primitive-band-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation) · [offline source ZIP](https://zenodo.org/api/records/22773401/files/76-primitive-band-sources.zip/content).
- [40-page source-band and boundary supplement](https://zenodo.org/api/records/22773401/files/75-primitive-band-supplement.pdf/content) · complete accepted eight-provider continuation, separately readable.

## The calculation and its purpose

Split-Zero pursues a proposed cohomological approach to Riemann zeta zeros
over tau, the programme's proposed absolute base. The calculation carries
the original conductor relations into Gamma-function Hilbert metrics and
the cohomological connecting map. Native refers to those original inner
products and their induced quotient metrics. Repeated factors, branch
intersections, coefficients, phases and fixed frames are retained.

The original period observation divides into its kernel K and invariant
residual V_A/K. Their total determinant growth is known, but the separate
leading allocations and common long connecting/invariant loss are still
being calculated. This edition supplies quantitative source estimates and
an exact residual-boundary construction for that calculation; it does not
report an exhibited off-critical-line zero.

## What the accepted continuation establishes

- **Complete translated relation bands (PSG/SGT).** A leading-monomial norm
  alone did not control the translated relations. The full relation Gram
  H_e now satisfies
  log det H_e=log F_(k,e,s)+2 d_e q log(4/pi)+o(kq),
  where q=(k+1)^2, d_e=8k+24+e, and F_(k,e,s) is the explicit product of
  the original moment coefficient, mass and Gamma factorial norms. The
  full original translation retains the explicit 2 d_e q log(4/pi)
  contribution and the remaining o(kq) error.
  Its complete low-degree kernel and reciprocal-symbol principal parts
  remain; no zero-free unit disk is assumed.
- **The original four primitive rows (PFG).** A nonzero minor from the four
  earliest independent moment rows supplies the finite lower bound, and
  the complete coefficient expansion supplies the upper bound. For the
  actual matrix W and Q=(k+5)^2, this evaluates
  log det(W* H_1 W)=4 log M_s+8 Q log Q+O_actual(Q)=o(kq).
  The four-row determinant is calculated, not discarded because its rank
  is small.
- **Return through the same primitive coordinates (PSR).** The exact identity
  Theta_e^(s)=(R_e^pol)^T diag(r!) P_e^Tay retains the full original
  relation coefficients and prescribed Taylor complement. The native
  coefficient matrix cancels against its actual inverse. Thus the source
  determinant difference between the two original Gamma orders is o(kq).
  The connecting-order difference is returned to the original compatibility
  terms chi_X-chi_Y, with the exact source ratio and both directed errors
  still present before the limit.
- **The surviving boundary quotient (RQB).** Let J be the original invariant
  source, Phi the stacked multiplication B_cof followed by the original
  target quotient, and L=ker Phi. The computed kernels prove the maps
  V/(J+L) -> W/W_inv -> im Phi/im(Phi J_0), taking
  [x] to [B_cof x] and then to [Phi x], are isomorphisms.
  Full nonreduced branch divisibility constrains L and the exact residual
  rank. The original target minimum over W_inv gives its Gamma metric Q_b,
  while the source minimum over J+L supplies its denominator.

The boundary calculation also gives the positive four-row update

    Q_b(n)=Q_b(n-1)+R_n* (I_4+L_inv,n)^(-1) R_n.

Its covariance retains all preceding lower and invariant columns. The
specified four-endpoint return yields

    V_b+V_inv+V_o=4 Fhat_j,    V_b,V_inv,V_o >= 0.

V_o is the remaining target quotient, not an omitted remainder. This
provides an aggregate upper bound and directed residual interval; it does
not assign an individual leading coefficient to V_b or V_inv.

## Remaining work and full reading objects

The next calculation is the common long connecting/invariant return and
its actual kernel/residual allocation. The source estimate, four-row bound,
coordinate maps and residual quotient above are established inputs, not
tasks to recreate. The original Gamma orders, relation coefficients,
quotient denominators, fixed-period restrictions and signed returns stay
in their stated domains. A stronger comparison being investigated beyond
the accepted source cut is not silently promoted to a proved result here.

The separate 40-page reader contains all eight provider sources and 203
original tagged equations: PDS/CIT/PDI and PSG/SGT/PFG/PSR/RQB, with full
intervening proofs. Its accepted intake records 173 identity/tag checks
over 55 pinned files and reuses the owner's all-40-page visual acceptance.
Those are source-integrity and prior-review scopes, not new numerical
experiments, PDF audits or Lean execution by this publication task.

The 549-page cumulative reader and [complete delivered editable sources](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation)
are the actual root-accepted integrated handoff. Their byte identities,
current prompt and source membership come from its receipts; this guide
does not substitute a research-position report for complete proofs.

## Source restoration and previous editions

The package has 21 physical files restoring 19 logical owner
files. Its large source map is carried in ordered gzip parts [11_SOURCE_MAP.json.gz.part01](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/11_SOURCE_MAP.json.gz.part01), the
[manifest](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/SOURCE_MAP_TRANSPORT.json), and the
[decoder](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/restore_source_map.py). From the downloaded directory:

```text
python restore_source_map.py --folder RESTORED_19
```

The original logical source-map SHA-256 is `0ec0af1a8c91267390d06609d9edefac9418400b74498a199bb949ed89a1184a`;
the public logical SHA-256 is `65ec4ff61f73090dac40b4188048169ce7d87c281d79e0515a0ee8c2cfe27167`. The manifest
specifies exact restoration and recorded public locator transport.

The original/private predecessor source map and its published locator-only
derivative are different byte objects, recorded with different hashes. The
previous source asset73 restores the public derivative, not the original
private hash. Exact original predecessor restoration requires separately
supplied historical bytes matching that original identity. The current
decoder restores all 19 logical files independently of external
history; it does not fetch that predecessor map. Archive history keeps its
explicit unresolved-reference scope, and current source acceptance does
not claim unavailable historical bytes were recovered.

The [previous edition](https://doi.org/10.5281/zenodo.22772244) retains the 498-page
paper, its 13-page supplement and all 73 downloads unchanged. This edition
adds cumulative PDF74, separate 40-page PDF75 and complete ZIP76. All 76
downloads remain individually clickable; PDF74 is the pertinent preview.

- [Earlier 20260915 native conductor continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation).
- [Earlier 20260915 native boundary continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation).
- [Earlier 20260915 allocation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation).
- [Earlier 20260915 dual metric continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation).
- [Earlier 20260915 operator control continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation).
- [Earlier 20260915 first variation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation).
- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).


[Release provenance](RELEASE.json) · [All file identities](ALL_ZENODO_FILES.json).

## All 76 downloads

- [74-primitive-band-reader.pdf](https://zenodo.org/api/records/22773401/files/74-primitive-band-reader.pdf/content) — 3,133,248 bytes; separate PDF.
- [75-primitive-band-supplement.pdf](https://zenodo.org/api/records/22773401/files/75-primitive-band-supplement.pdf/content) — 309,244 bytes; separate PDF.
- [76-primitive-band-sources.zip](https://zenodo.org/api/records/22773401/files/76-primitive-band-sources.zip/content) — 40,561,250 bytes; offline source archive.
- [01-main-reader.pdf](https://zenodo.org/api/records/22773401/files/01-main-reader.pdf/content) — 3,502,600 bytes; separate PDF.
- [02-fluid-reader.pdf](https://zenodo.org/api/records/22773401/files/02-fluid-reader.pdf/content) — 2,063,023 bytes; separate PDF.
- [03-heat-reader.pdf](https://zenodo.org/api/records/22773401/files/03-heat-reader.pdf/content) — 1,266,114 bytes; separate PDF.
- [04-connes-reader.pdf](https://zenodo.org/api/records/22773401/files/04-connes-reader.pdf/content) — 954,841 bytes; separate PDF.
- [05-gct-reader.pdf](https://zenodo.org/api/records/22773401/files/05-gct-reader.pdf/content) — 1,624,359 bytes; separate PDF.
- [06-vacuum-reader.pdf](https://zenodo.org/api/records/22773401/files/06-vacuum-reader.pdf/content) — 676,386 bytes; separate PDF.
- [07-complete-mathematical-sources.zip](https://zenodo.org/api/records/22773401/files/07-complete-mathematical-sources.zip/content) — 12,343,724 bytes; offline source archive.
- [08-splitzero-arithmetic-calculations.pdf](https://zenodo.org/api/records/22773401/files/08-splitzero-arithmetic-calculations.pdf/content) — 501,741 bytes; separate PDF.
- [09-unified-flow-calculations.pdf](https://zenodo.org/api/records/22773401/files/09-unified-flow-calculations.pdf/content) — 123,793 bytes; separate PDF.
- [10-splitzero-cohomology-and-weight-control.pdf](https://zenodo.org/api/records/22773401/files/10-splitzero-cohomology-and-weight-control.pdf/content) — 539,799 bytes; separate PDF.
- [11-current-calculation-sources.zip](https://zenodo.org/api/records/22773401/files/11-current-calculation-sources.zip/content) — 546,497 bytes; offline source archive.
- [12-tandem-calculation-sources.zip](https://zenodo.org/api/records/22773401/files/12-tandem-calculation-sources.zip/content) — 718,715 bytes; offline source archive.
- [13-main-reader-425p.pdf](https://zenodo.org/api/records/22773401/files/13-main-reader-425p.pdf/content) — 3,607,114 bytes; separate PDF.
- [14-splitzero-tau-kernel-continuation.pdf](https://zenodo.org/api/records/22773401/files/14-splitzero-tau-kernel-continuation.pdf/content) — 1,245,668 bytes; separate PDF.
- [15-current-integrated-sources.zip](https://zenodo.org/api/records/22773401/files/15-current-integrated-sources.zip/content) — 5,272,531 bytes; offline source archive.
- [16-tandem-continuation-sources.zip](https://zenodo.org/api/records/22773401/files/16-tandem-continuation-sources.zip/content) — 3,925,745 bytes; offline source archive.
- [17-main-reader-433p.pdf](https://zenodo.org/api/records/22773401/files/17-main-reader-433p.pdf/content) — 3,663,923 bytes; separate PDF.
- [18-splitzero-stieltjes-and-sum-connections.pdf](https://zenodo.org/api/records/22773401/files/18-splitzero-stieltjes-and-sum-connections.pdf/content) — 1,674,088 bytes; separate PDF.
- [19-current-main-and-proof-sources.zip](https://zenodo.org/api/records/22773401/files/19-current-main-and-proof-sources.zip/content) — 5,368,990 bytes; offline source archive.
- [20-tandem-stieltjes-continuation-sources.zip](https://zenodo.org/api/records/22773401/files/20-tandem-stieltjes-continuation-sources.zip/content) — 5,978,173 bytes; offline source archive.
- [21-main-reader-454p.pdf](https://zenodo.org/api/records/22773401/files/21-main-reader-454p.pdf/content) — 3,783,830 bytes; separate PDF.
- [22-splitzero-cyclic-control-and-exterior-trace.pdf](https://zenodo.org/api/records/22773401/files/22-splitzero-cyclic-control-and-exterior-trace.pdf/content) — 2,190,268 bytes; separate PDF.
- [23-current-main-and-exterior-proof-sources.zip](https://zenodo.org/api/records/22773401/files/23-current-main-and-exterior-proof-sources.zip/content) — 10,975,655 bytes; offline source archive.
- [24-tandem-cyclic-control-sources.zip](https://zenodo.org/api/records/22773401/files/24-tandem-cyclic-control-sources.zip/content) — 10,280,789 bytes; offline source archive.
- [25-main-reader-482p.pdf](https://zenodo.org/api/records/22773401/files/25-main-reader-482p.pdf/content) — 3,963,102 bytes; separate PDF.
- [26-splitzero-toda-continuation-424p.pdf](https://zenodo.org/api/records/22773401/files/26-splitzero-toda-continuation-424p.pdf/content) — 2,388,633 bytes; separate PDF.
- [27-current-main-and-toda-gamma-proof-sources.zip](https://zenodo.org/api/records/22773401/files/27-current-main-and-toda-gamma-proof-sources.zip/content) — 12,195,336 bytes; offline source archive.
- [28-tandem-toda-continuation-sources.zip](https://zenodo.org/api/records/22773401/files/28-tandem-toda-continuation-sources.zip/content) — 12,654,645 bytes; offline source archive.
- [29-main-reader-gamma-endpoint-control.pdf](https://zenodo.org/api/records/22773401/files/29-main-reader-gamma-endpoint-control.pdf/content) — 4,146,598 bytes; separate PDF.
- [30-splitzero-gamma-continuation-478p.pdf](https://zenodo.org/api/records/22773401/files/30-splitzero-gamma-continuation-478p.pdf/content) — 2,677,953 bytes; separate PDF.
- [31-current-main-and-gamma-endpoint-proof-sources.zip](https://zenodo.org/api/records/22773401/files/31-current-main-and-gamma-endpoint-proof-sources.zip/content) — 12,798,864 bytes; offline source archive.
- [32-tandem-gamma-continuation-sources.zip](https://zenodo.org/api/records/22773401/files/32-tandem-gamma-continuation-sources.zip/content) — 76,036,630 bytes; offline source archive.
- [33-splitzero-period-deligne-continuation-715p.pdf](https://zenodo.org/api/records/22773401/files/33-splitzero-period-deligne-continuation-715p.pdf/content) — 3,911,624 bytes; separate PDF.
- [34-splitzero-period-deligne-public-sources.zip](https://zenodo.org/api/records/22773401/files/34-splitzero-period-deligne-public-sources.zip/content) — 245,460,514 bytes; offline source archive.
- [35-splitzero-sga-connes-continuation-765p.pdf](https://zenodo.org/api/records/22773401/files/35-splitzero-sga-connes-continuation-765p.pdf/content) — 4,181,790 bytes; separate PDF.
- [36-splitzero-sga-connes-public-sources.zip](https://zenodo.org/api/records/22773401/files/36-splitzero-sga-connes-public-sources.zip/content) — 266,476,545 bytes; offline source archive.
- [37-splitzero-periodized-residue-continuation-821p.pdf](https://zenodo.org/api/records/22773401/files/37-splitzero-periodized-residue-continuation-821p.pdf/content) — 4,494,149 bytes; separate PDF.
- [38-splitzero-periodized-residue-public-sources.zip](https://zenodo.org/api/records/22773401/files/38-splitzero-periodized-residue-public-sources.zip/content) — 290,930,931 bytes; offline source archive.
- [39-splitzero-recursive-source-relations-public-reader.pdf](https://zenodo.org/api/records/22773401/files/39-splitzero-recursive-source-relations-public-reader.pdf/content) — 8,820,155 bytes; separate PDF.
- [40-splitzero-recursive-public-sources.zip](https://zenodo.org/api/records/22773401/files/40-splitzero-recursive-public-sources.zip/content) — 242,919,748 bytes; offline source archive.
- [41-splitzero-cumulative-graph-public-reader.pdf](https://zenodo.org/api/records/22773401/files/41-splitzero-cumulative-graph-public-reader.pdf/content) — 10,485,483 bytes; separate PDF.
- [42-splitzero-cumulative-graph-public-sources.zip](https://zenodo.org/api/records/22773401/files/42-splitzero-cumulative-graph-public-sources.zip/content) — 259,075,728 bytes; offline source archive.
- [43-joint-gamma-schur-reader.pdf](https://zenodo.org/api/records/22773401/files/43-joint-gamma-schur-reader.pdf/content) — 331,432 bytes; separate PDF.
- [44-joint-gamma-schur-public-sources.zip](https://zenodo.org/api/records/22773401/files/44-joint-gamma-schur-public-sources.zip/content) — 11,895,776 bytes; offline source archive.
- [45-original-relation-bulk-reader.pdf](https://zenodo.org/api/records/22773401/files/45-original-relation-bulk-reader.pdf/content) — 244,344 bytes; separate PDF.
- [46-original-relation-bulk-public-sources.zip](https://zenodo.org/api/records/22773401/files/46-original-relation-bulk-public-sources.zip/content) — 19,526,414 bytes; offline source archive.
- [47-complete-gamma-return-reader.pdf](https://zenodo.org/api/records/22773401/files/47-complete-gamma-return-reader.pdf/content) — 162,644 bytes; separate PDF.
- [48-complete-gamma-return-public-sources.zip](https://zenodo.org/api/records/22773401/files/48-complete-gamma-return-public-sources.zip/content) — 11,197,669 bytes; offline source archive.
- [49-gamma-growth-arithmetic-return-reader.pdf](https://zenodo.org/api/records/22773401/files/49-gamma-growth-arithmetic-return-reader.pdf/content) — 291,648 bytes; separate PDF.
- [50-gamma-growth-public-sources.zip](https://zenodo.org/api/records/22773401/files/50-gamma-growth-public-sources.zip/content) — 3,286,365 bytes; offline source archive.
- [51-original-gamma-volumes-reader.pdf](https://zenodo.org/api/records/22773401/files/51-original-gamma-volumes-reader.pdf/content) — 498,135 bytes; separate PDF.
- [52-original-gamma-volumes-public-sources.zip](https://zenodo.org/api/records/22773401/files/52-original-gamma-volumes-public-sources.zip/content) — 5,159,594 bytes; offline source archive.
- [53-original-kernel-matrices-reader.pdf](https://zenodo.org/api/records/22773401/files/53-original-kernel-matrices-reader.pdf/content) — 483,728 bytes; separate PDF.
- [54-original-kernel-matrices-sources.zip](https://zenodo.org/api/records/22773401/files/54-original-kernel-matrices-sources.zip/content) — 1,954,898 bytes; offline source archive.
- [55-conductor-kernel-reader.pdf](https://zenodo.org/api/records/22773401/files/55-conductor-kernel-reader.pdf/content) — 635,034 bytes; separate PDF.
- [56-conductor-kernel-sources.zip](https://zenodo.org/api/records/22773401/files/56-conductor-kernel-sources.zip/content) — 2,551,883 bytes; offline source archive.
- [57-exterior-kernel-reader.pdf](https://zenodo.org/api/records/22773401/files/57-exterior-kernel-reader.pdf/content) — 707,453 bytes; separate PDF.
- [58-exterior-kernel-sources.zip](https://zenodo.org/api/records/22773401/files/58-exterior-kernel-sources.zip/content) — 2,733,621 bytes; offline source archive.
- [59-quotient-moment-reader.pdf](https://zenodo.org/api/records/22773401/files/59-quotient-moment-reader.pdf/content) — 820,853 bytes; separate PDF.
- [60-quotient-moment-sources.zip](https://zenodo.org/api/records/22773401/files/60-quotient-moment-sources.zip/content) — 3,077,932 bytes; offline source archive.
- [61-first-variation-reader.pdf](https://zenodo.org/api/records/22773401/files/61-first-variation-reader.pdf/content) — 974,609 bytes; separate PDF.
- [62-first-variation-sources.zip](https://zenodo.org/api/records/22773401/files/62-first-variation-sources.zip/content) — 3,540,462 bytes; offline source archive.
- [63-operator-control-reader.pdf](https://zenodo.org/api/records/22773401/files/63-operator-control-reader.pdf/content) — 1,381,726 bytes; separate PDF.
- [64-operator-control-sources.zip](https://zenodo.org/api/records/22773401/files/64-operator-control-sources.zip/content) — 7,137,657 bytes; offline source archive.
- [65-dual-metric-reader.pdf](https://zenodo.org/api/records/22773401/files/65-dual-metric-reader.pdf/content) — 1,679,928 bytes; separate PDF.
- [66-dual-metric-sources.zip](https://zenodo.org/api/records/22773401/files/66-dual-metric-sources.zip/content) — 21,332,888 bytes; offline source archive.
- [67-allocation-reader.pdf](https://zenodo.org/api/records/22773401/files/67-allocation-reader.pdf/content) — 1,822,478 bytes; separate PDF.
- [68-allocation-sources.zip](https://zenodo.org/api/records/22773401/files/68-allocation-sources.zip/content) — 29,783,877 bytes; offline source archive.
- [69-native-boundary-reader.pdf](https://zenodo.org/api/records/22773401/files/69-native-boundary-reader.pdf/content) — 2,412,141 bytes; separate PDF.
- [70-native-boundary-sources.zip](https://zenodo.org/api/records/22773401/files/70-native-boundary-sources.zip/content) — 108,010,120 bytes; offline source archive.
- [71-native-conductor-reader.pdf](https://zenodo.org/api/records/22773401/files/71-native-conductor-reader.pdf/content) — 2,859,954 bytes; separate PDF.
- [72-primitive-connecting-reader.pdf](https://zenodo.org/api/records/22773401/files/72-primitive-connecting-reader.pdf/content) — 136,798 bytes; separate PDF.
- [73-native-conductor-sources.zip](https://zenodo.org/api/records/22773401/files/73-native-conductor-sources.zip/content) — 240,583,874 bytes; offline source archive.
