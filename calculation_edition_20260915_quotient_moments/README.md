# Split-Zero cohomology: outer moments and residual observations

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/00_CONTINUE_HERE.md).

[Read the current 132-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22759221/files/59-quotient-moment-reader.pdf/content) · [Published DOI 10.5281/zenodo.22759221](https://doi.org/10.5281/zenodo.22759221).

- [132-page quotient kernel](https://zenodo.org/api/records/22759221/files/59-quotient-moment-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation) · [offline source ZIP](https://zenodo.org/api/records/22759221/files/60-quotient-moment-sources.zip/content).

The current 132-page reader adds complete CTV/ROQ/OSP/OAR/PMR proofs. The original kernel contribution is now expressed as seven same-source Gamma moment determinants minus the actual positive residual-increment sum, with two unequal o(kq) error endpoints in the stated fixed-period and eventual parameter domains. The seventeen-file package preserves the sole owner prompt, complete receiving proofs and unchanged recorded PR32 source/CI.

## What this calculation studies

Split-Zero follows a finite arithmetic quotient attached to a selected zeta-zero
packet, with its original theta cohomology and mixed-support maps. A specified
period observation loses a subspace K. The calculation measures that same
kernel in the original source metrics at four degrees q-1, q, 2q-1 and 2q.
The goal is its contribution to the original signed cohomological return,
not a conclusion inferred merely from the dimension of K.

The preceding conductor calculation gave a smaller root grid and controlled
the transport error by o(kq) for each fixed actual period. This edition
constructs the resulting outer quotient and residual observation explicitly.
It then compares the outer quotient with same-source power-weight moments.
The result is an explicit seven-determinant expression minus the actual
positive residual-increment sum, with both unequal finite error endpoints.

The main simple-quartet lane retains m=1, k=4l+1 with l>=1, q=(k+1)^2,
c=k/2, 0<delta<1/2 and gamma>2, at every original branch |u|>=R_*.
R_* is calculated from the actual quartet and full unit. The kernel dimension
is r=8k-16 on that domain; the full all-multiplicity geometry and primary
nilpotents remain without assigning that rank to other multiplicities.
For k>=9, the conductor construction retains all original coefficients,
periods and its nonzero moment denominator.

## Completed outer quotient and residual observation

CTV proves the original central-root factorization
P_k=P_(k-8) P_(partial,k), with every root unchanged. Multiplication by the
full P_(k-8) supplies the exact metric |P_(k-8)(y)|^2 dm_s(y), retaining
the original mass. The outer quotient has rank Delta=16k-48 and source
degrees Delta-1, Delta, q+Delta-1 and q+Delta. The lower-grid quantities
remain k'=k-8, q'=(k-7)^2, centre c'=c-4 and source order s=1 or k.
Every primary Vandermonde factor, affine phase, shifted endpoint and signed
monic-norm tail is retained.

ROQ builds the actual residual map Xi: V_A -> C^j, j=8k-32, from the
original certificate rows D=F^transpose. It retains the original boundary
basis, inherited period-word metric, pivot determinant, source metric and
full kernel-plus-ideal graph. Its constrained covariance is

    Omega_N = D [R_N - R_N C* (C R_N C*)^(-1) C R_N] D*,
    Q_(Xi,N) = Omega_N^(-1).

No generic residual matrix or rank-only volume is substituted. Its complete
positive cutoff-increment sum is

    Phi_(k,s) = F_(Xi,k)^(s)
      = log(1+eta_(q-1))
        + 2 sum_(N=q)^(2q-2) log(1+eta_N)
        + log(1+eta_(2q-1)) >= 0.

Each eta_N is given in the actual original coefficients and constrained
covariance update. OAR keeps both unequal signed error endpoints:

    F_K^(s) = F_(partial,k)^(s) - Phi_(k,s) + e_(k,s),
    -e_(k,s)^- <= e_(k,s) <= e_(k,s)^+,
    e_(k,s)^- = o(kq), e_(k,s)^+ = o(kq).

The kernel caps subtract the actual first positive residual increment.
Additional evaluated positive increments supply further finite subtractions;
the correlated arithmetic boundary and signed return retain those same signs.

## Comparison with seven original Gamma moment determinants

OSP compares the full original root-polynomial norms with same-source
power-weight norms, in every polynomial direction, including the entire
small-real-coordinate region. Its explicit eventual domain is

    epsilon = 2^(-32), k>=29,
    k sqrt(delta^2+gamma^2) <= epsilon q/2.

This domain is separate from the conductor's k>=9 domain. The original source
orders remain s=1 and k; no zero, period or source mass is replaced. In this
domain the proved comparison is

    |F_(partial,k)^(s) - F_(0,k)^(s)|
       <= c_k^circle = 4(q+Delta+1) E_k
       = O_(delta,gamma)(q) = o(kq).

F_(0,k)^(s) is the seven signed moment determinants written in OSP32, not seven
scalar moments. Each is constructed from the exact same-source moments

    mu_j^(s) = M_s [d^j/dz^j (cos z)^(-s/2)]_(z=0),
    D_a(Q;s) = det [mu_(2Q+i+j)^(s)]_(0<=i,j<a).

M_s is the full original source mass. OSP35 supplies the exact even/odd
factorization. PMR carries the additional comparison error into the original
arithmetic kernel, correlated boundary and signed mixed return:

    F_K^(s) = F_(0,k)^(s) - Phi_(k,s) + e_(k,s)^0,
    -e_(k,s)^(0,-) <= e_(k,s)^0 <= e_(k,s)^(0,+),
    e_(k,s)^(0,-) = o(kq), e_(k,s)^(0,+) = o(kq).

**The two finite error endpoints remain unequal.** PMR8 proves that interval
intersection alone preserves the previous outer-root finite endpoints exactly.
The moment comparison supplies a concrete analytic target; it does not by
itself tighten that previous interval. Evaluating additional actual residual
increments is the stated source of finite subtractions.

All these conductor and residual statements retain the fixed-period scope.
No moving-period uniformity or RH conclusion is asserted. The earlier AKS
finite pointwise minimum with KAF and its ceiling25.02078097650 remain valid.

## What remains to calculate

The next calculation is the kq-scale difference between all seven determinants
F_(0,k)^(s) and the actual residual sum Phi_(k,s). For the moment term, the
first variation compares q'=(k-7)^2 with q=(k+1)^2 at the original source
order. High parity blocks have dimension proportional to q; the growing low
blocks have dimension proportional to k and a different parameter ratio;
D_1(q;s) is scalar. The existing q^2 asymptotic alone gives no uniform
first-variation error estimate for those different regimes.

For the residual term, the exact period certificates and constrained covariance
updates already specify the sum. The full denominator, source-ideal terms and
kernel cross terms must remain in any estimate. **No unique limit or exact
leading value is asserted.** Newer first-variation and fixed-module-conditioning
drafts are not part of this sealed edition.

The exact outer quotient, residual covariance and same-source moment comparison are completed. The next calculation is their kq-scale first variation and actual residual sum. PMR8 proves that interval intersection alone does not tighten the preceding outer-root finite endpoints. No leading value, moving-period uniformity or RH conclusion is asserted; newer first-variation and fixed-module-conditioning drafts are excluded.

## Complete proofs, receivers and checked-source scope

[File14: complete current proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) preserves the full preceding
110-page development and adds complete CTV1-22, ROQ1-27, OSP1-35, OAR1-11
and PMR1-8 proofs. It is the editable source of the current 132-page reader.
[Arithmetic source transfer, file13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex)
retains the original correlated source allowances and their exact maps.

[Joint receiver09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/09_UPDATED_JOINT_NOTE.tex) and
[signed receiver10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/10_UPDATED_SIGNED_RETURN.tex) retain all 31
preceding providers and the complete later proofs. Current receiving sites
are MRI4e-q and BRI6c-g, with new MRI4l-q and BRI6f-g carrying the complete
outer, moment and residual refinements. Their 249/240-page builds establish
compilation and source closure, not visual acceptance of receiver PDFs.
Those separate PDF builds are not delivered as visually accepted papers.

The current reader's complete 132 pages have the owner's visual acceptance:
106 body regions match the accepted predecessor; five opening pages and every
new page112-132 were inspected individually. All 132 footers were checked
visually and against sequential PDF text. Complete new written proofs and
receiving replacements have independent acceptance. The declared diagnostic
fixtures are not actual-zero or actual-period evaluations.

[File16: complete PR32 formal source and proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md)
is unchanged. It retains the four modules, full note, runner and successful
two-job CI at implementation8e78bc7c240b04d297ade6afdadfd863e0c6db7b and
unchanged checked source at finalhead9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6.
The recorded scope remains 33 local modules and 56 selected transitive axiom
targets. No new local Lean run or PR merge is claimed; the new analytic
estimates have written-proof scope.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/12_VALIDATION.md) records these exact scopes.
[Source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/11_SOURCE_MAP.json) distinguishes owner-original
SHA-256 `4375c0cbad44222cdb690cf6ad6ff4335173e542bfb90688358c26528a2e0c7f` from public transported SHA-256
`3c1f19a98303915846e65260894348f7ad6290ae7c2e1a22a3b74ee38d065a6c`. Its metadata-only transport scope is:
777 literal historical private-account locator occurrences transported across739 values and8 path-valued keys, including nested JSON. Full mathematical bodies, original source hashes and other metadata remain unchanged. Original embedded identities still identify pre-transport sources. The other sixteen files are unchanged.

This is exactly the accepted seventeen-file edition. The original owner00
remains the sole current continuation; this index creates no competing prompt.
The preceding 110-page, 97-page, 72-page and Gamma editions remain intact.

## Earlier complete source editions

- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 58-download edition](https://doi.org/10.5281/zenodo.22758970) remains frozen
with its 110-page preview. This edition adds PDF59 and ZIP60. The actual
new browser preview is the current 132-page PDF59; ZIP60 supplies all seventeen
flat source files for offline use, not a substitute preview. Every earlier
mathematical/source file remains unchanged.


[Release provenance](RELEASE.json) · [All file identities](ALL_ZENODO_FILES.json).

## All 60 downloads

- [59-quotient-moment-reader.pdf](https://zenodo.org/api/records/22759221/files/59-quotient-moment-reader.pdf/content) — 820,853 bytes; separate PDF.
- [60-quotient-moment-sources.zip](https://zenodo.org/api/records/22759221/files/60-quotient-moment-sources.zip/content) — 3,077,932 bytes; offline source archive.
- [01-main-reader.pdf](https://zenodo.org/api/records/22759221/files/01-main-reader.pdf/content) — 3,502,600 bytes; separate PDF.
- [02-fluid-reader.pdf](https://zenodo.org/api/records/22759221/files/02-fluid-reader.pdf/content) — 2,063,023 bytes; separate PDF.
- [03-heat-reader.pdf](https://zenodo.org/api/records/22759221/files/03-heat-reader.pdf/content) — 1,266,114 bytes; separate PDF.
- [04-connes-reader.pdf](https://zenodo.org/api/records/22759221/files/04-connes-reader.pdf/content) — 954,841 bytes; separate PDF.
- [05-gct-reader.pdf](https://zenodo.org/api/records/22759221/files/05-gct-reader.pdf/content) — 1,624,359 bytes; separate PDF.
- [06-vacuum-reader.pdf](https://zenodo.org/api/records/22759221/files/06-vacuum-reader.pdf/content) — 676,386 bytes; separate PDF.
- [07-complete-mathematical-sources.zip](https://zenodo.org/api/records/22759221/files/07-complete-mathematical-sources.zip/content) — 12,343,724 bytes; offline source archive.
- [08-splitzero-arithmetic-calculations.pdf](https://zenodo.org/api/records/22759221/files/08-splitzero-arithmetic-calculations.pdf/content) — 501,741 bytes; separate PDF.
- [09-unified-flow-calculations.pdf](https://zenodo.org/api/records/22759221/files/09-unified-flow-calculations.pdf/content) — 123,793 bytes; separate PDF.
- [10-splitzero-cohomology-and-weight-control.pdf](https://zenodo.org/api/records/22759221/files/10-splitzero-cohomology-and-weight-control.pdf/content) — 539,799 bytes; separate PDF.
- [11-current-calculation-sources.zip](https://zenodo.org/api/records/22759221/files/11-current-calculation-sources.zip/content) — 546,497 bytes; offline source archive.
- [12-tandem-calculation-sources.zip](https://zenodo.org/api/records/22759221/files/12-tandem-calculation-sources.zip/content) — 718,715 bytes; offline source archive.
- [13-main-reader-425p.pdf](https://zenodo.org/api/records/22759221/files/13-main-reader-425p.pdf/content) — 3,607,114 bytes; separate PDF.
- [14-splitzero-tau-kernel-continuation.pdf](https://zenodo.org/api/records/22759221/files/14-splitzero-tau-kernel-continuation.pdf/content) — 1,245,668 bytes; separate PDF.
- [15-current-integrated-sources.zip](https://zenodo.org/api/records/22759221/files/15-current-integrated-sources.zip/content) — 5,272,531 bytes; offline source archive.
- [16-tandem-continuation-sources.zip](https://zenodo.org/api/records/22759221/files/16-tandem-continuation-sources.zip/content) — 3,925,745 bytes; offline source archive.
- [17-main-reader-433p.pdf](https://zenodo.org/api/records/22759221/files/17-main-reader-433p.pdf/content) — 3,663,923 bytes; separate PDF.
- [18-splitzero-stieltjes-and-sum-connections.pdf](https://zenodo.org/api/records/22759221/files/18-splitzero-stieltjes-and-sum-connections.pdf/content) — 1,674,088 bytes; separate PDF.
- [19-current-main-and-proof-sources.zip](https://zenodo.org/api/records/22759221/files/19-current-main-and-proof-sources.zip/content) — 5,368,990 bytes; offline source archive.
- [20-tandem-stieltjes-continuation-sources.zip](https://zenodo.org/api/records/22759221/files/20-tandem-stieltjes-continuation-sources.zip/content) — 5,978,173 bytes; offline source archive.
- [21-main-reader-454p.pdf](https://zenodo.org/api/records/22759221/files/21-main-reader-454p.pdf/content) — 3,783,830 bytes; separate PDF.
- [22-splitzero-cyclic-control-and-exterior-trace.pdf](https://zenodo.org/api/records/22759221/files/22-splitzero-cyclic-control-and-exterior-trace.pdf/content) — 2,190,268 bytes; separate PDF.
- [23-current-main-and-exterior-proof-sources.zip](https://zenodo.org/api/records/22759221/files/23-current-main-and-exterior-proof-sources.zip/content) — 10,975,655 bytes; offline source archive.
- [24-tandem-cyclic-control-sources.zip](https://zenodo.org/api/records/22759221/files/24-tandem-cyclic-control-sources.zip/content) — 10,280,789 bytes; offline source archive.
- [25-main-reader-482p.pdf](https://zenodo.org/api/records/22759221/files/25-main-reader-482p.pdf/content) — 3,963,102 bytes; separate PDF.
- [26-splitzero-toda-continuation-424p.pdf](https://zenodo.org/api/records/22759221/files/26-splitzero-toda-continuation-424p.pdf/content) — 2,388,633 bytes; separate PDF.
- [27-current-main-and-toda-gamma-proof-sources.zip](https://zenodo.org/api/records/22759221/files/27-current-main-and-toda-gamma-proof-sources.zip/content) — 12,195,336 bytes; offline source archive.
- [28-tandem-toda-continuation-sources.zip](https://zenodo.org/api/records/22759221/files/28-tandem-toda-continuation-sources.zip/content) — 12,654,645 bytes; offline source archive.
- [29-main-reader-gamma-endpoint-control.pdf](https://zenodo.org/api/records/22759221/files/29-main-reader-gamma-endpoint-control.pdf/content) — 4,146,598 bytes; separate PDF.
- [30-splitzero-gamma-continuation-478p.pdf](https://zenodo.org/api/records/22759221/files/30-splitzero-gamma-continuation-478p.pdf/content) — 2,677,953 bytes; separate PDF.
- [31-current-main-and-gamma-endpoint-proof-sources.zip](https://zenodo.org/api/records/22759221/files/31-current-main-and-gamma-endpoint-proof-sources.zip/content) — 12,798,864 bytes; offline source archive.
- [32-tandem-gamma-continuation-sources.zip](https://zenodo.org/api/records/22759221/files/32-tandem-gamma-continuation-sources.zip/content) — 76,036,630 bytes; offline source archive.
- [33-splitzero-period-deligne-continuation-715p.pdf](https://zenodo.org/api/records/22759221/files/33-splitzero-period-deligne-continuation-715p.pdf/content) — 3,911,624 bytes; separate PDF.
- [34-splitzero-period-deligne-public-sources.zip](https://zenodo.org/api/records/22759221/files/34-splitzero-period-deligne-public-sources.zip/content) — 245,460,514 bytes; offline source archive.
- [35-splitzero-sga-connes-continuation-765p.pdf](https://zenodo.org/api/records/22759221/files/35-splitzero-sga-connes-continuation-765p.pdf/content) — 4,181,790 bytes; separate PDF.
- [36-splitzero-sga-connes-public-sources.zip](https://zenodo.org/api/records/22759221/files/36-splitzero-sga-connes-public-sources.zip/content) — 266,476,545 bytes; offline source archive.
- [37-splitzero-periodized-residue-continuation-821p.pdf](https://zenodo.org/api/records/22759221/files/37-splitzero-periodized-residue-continuation-821p.pdf/content) — 4,494,149 bytes; separate PDF.
- [38-splitzero-periodized-residue-public-sources.zip](https://zenodo.org/api/records/22759221/files/38-splitzero-periodized-residue-public-sources.zip/content) — 290,930,931 bytes; offline source archive.
- [39-splitzero-recursive-source-relations-public-reader.pdf](https://zenodo.org/api/records/22759221/files/39-splitzero-recursive-source-relations-public-reader.pdf/content) — 8,820,155 bytes; separate PDF.
- [40-splitzero-recursive-public-sources.zip](https://zenodo.org/api/records/22759221/files/40-splitzero-recursive-public-sources.zip/content) — 242,919,748 bytes; offline source archive.
- [41-splitzero-cumulative-graph-public-reader.pdf](https://zenodo.org/api/records/22759221/files/41-splitzero-cumulative-graph-public-reader.pdf/content) — 10,485,483 bytes; separate PDF.
- [42-splitzero-cumulative-graph-public-sources.zip](https://zenodo.org/api/records/22759221/files/42-splitzero-cumulative-graph-public-sources.zip/content) — 259,075,728 bytes; offline source archive.
- [43-joint-gamma-schur-reader.pdf](https://zenodo.org/api/records/22759221/files/43-joint-gamma-schur-reader.pdf/content) — 331,432 bytes; separate PDF.
- [44-joint-gamma-schur-public-sources.zip](https://zenodo.org/api/records/22759221/files/44-joint-gamma-schur-public-sources.zip/content) — 11,895,776 bytes; offline source archive.
- [45-original-relation-bulk-reader.pdf](https://zenodo.org/api/records/22759221/files/45-original-relation-bulk-reader.pdf/content) — 244,344 bytes; separate PDF.
- [46-original-relation-bulk-public-sources.zip](https://zenodo.org/api/records/22759221/files/46-original-relation-bulk-public-sources.zip/content) — 19,526,414 bytes; offline source archive.
- [47-complete-gamma-return-reader.pdf](https://zenodo.org/api/records/22759221/files/47-complete-gamma-return-reader.pdf/content) — 162,644 bytes; separate PDF.
- [48-complete-gamma-return-public-sources.zip](https://zenodo.org/api/records/22759221/files/48-complete-gamma-return-public-sources.zip/content) — 11,197,669 bytes; offline source archive.
- [49-gamma-growth-arithmetic-return-reader.pdf](https://zenodo.org/api/records/22759221/files/49-gamma-growth-arithmetic-return-reader.pdf/content) — 291,648 bytes; separate PDF.
- [50-gamma-growth-public-sources.zip](https://zenodo.org/api/records/22759221/files/50-gamma-growth-public-sources.zip/content) — 3,286,365 bytes; offline source archive.
- [51-original-gamma-volumes-reader.pdf](https://zenodo.org/api/records/22759221/files/51-original-gamma-volumes-reader.pdf/content) — 498,135 bytes; separate PDF.
- [52-original-gamma-volumes-public-sources.zip](https://zenodo.org/api/records/22759221/files/52-original-gamma-volumes-public-sources.zip/content) — 5,159,594 bytes; offline source archive.
- [53-original-kernel-matrices-reader.pdf](https://zenodo.org/api/records/22759221/files/53-original-kernel-matrices-reader.pdf/content) — 483,728 bytes; separate PDF.
- [54-original-kernel-matrices-sources.zip](https://zenodo.org/api/records/22759221/files/54-original-kernel-matrices-sources.zip/content) — 1,954,898 bytes; offline source archive.
- [55-conductor-kernel-reader.pdf](https://zenodo.org/api/records/22759221/files/55-conductor-kernel-reader.pdf/content) — 635,034 bytes; separate PDF.
- [56-conductor-kernel-sources.zip](https://zenodo.org/api/records/22759221/files/56-conductor-kernel-sources.zip/content) — 2,551,883 bytes; offline source archive.
- [57-exterior-kernel-reader.pdf](https://zenodo.org/api/records/22759221/files/57-exterior-kernel-reader.pdf/content) — 707,453 bytes; separate PDF.
- [58-exterior-kernel-sources.zip](https://zenodo.org/api/records/22759221/files/58-exterior-kernel-sources.zip/content) — 2,733,621 bytes; offline source archive.
