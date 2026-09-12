# PR15 exact-source and execution-status audit — 12 September 2026

This bounded audit stages and reads the current PR15 contribution, preserving all remote bytes. It runs no Lean, Lake or Elan process and changes no pre-existing mathematical source. Parent task: `kernel_asymptotic_route`; repository integration remains with the authorized root/Zeta owner. The five new Lean files and the complete research note were read, with a second independent reading of the support/relation files and their inherited reconstruction module.

## Immutable source and primary execution evidence

- Repository: `KokunoYumeto/zeta-function-research-reader`.
- PR: <https://github.com/KokunoYumeto/zeta-function-research-reader/pull/15>.
- Verified head: `21970bbf4760d0bbca512a4a7996a2e38f968947`.
- Head branch: `codex/tau-boundary-layer-20260912`.
- State at retrieval: open, draft.
- Base branch: `codex/tau-formal-recovery-20260912`; base commit `5d2772ea0a16d177ac3e01ff70394b90ba95a232`.
- The PR-files API supplies thirteen added files, with no modified or deleted files. All thirteen staged byte strings have Git blob SHA1 equal to the API's exact blob identifiers. Eleven contextual files fetched from the same commit are also blob-verified.
- GitHub Actions run **34705607593** has `head_sha` equal to the exact head, event `push`, status `completed`, conclusion `success`.
- Its job **103584974563** has the same head, status `completed`, conclusion `success`; every one of its nine returned step records has conclusion `success`.
- Primary job URL: <https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34705607593/job/103584974563>.

The exact checked workflow source has strict source invocations `lake env lean --trust=0 -DwarningAsError=true`, then executes the selected declaration axiom audits. It preserves Lean `4.31.0` and Mathlib commit `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. The source checking loop retains failures in a status variable and exits nonzero if any source invocation fails; the axiom-audit step uses `set -euo pipefail`. The previously pinned core is fetched by `prepare.py` and checked against Git blob `ff991f7383922e71cdf0e4a3bc85e89e18f808ef`. The original Lake default targets do not include the five new modules; the added manifest and explicit invocations cover them.

The raw public job-log endpoint returned HTTP 403, `Must have admin rights to Repository`. The run-artifacts endpoint returned zero artifacts. Therefore this audit independently verifies successful remote execution status plus its exact source/configuration, but does **not** claim to have independently replayed the raw transitive-axiom output. The PR author reports reading the full log. That author statement is recorded separately from this audit's primary evidence. No local Lean execution occurred.

The inherited `formal/splitzero/VALIDATION.json` certifies an older structural run at commit `8196e4f4d4f09a8cfc8a4e8ce8683ded359adbf6`; it is not a PR15 receipt. It is preserved under `context/` with this scope recorded.

`BOUNDARY_TARGETS.json` selects exactly **38 declarations** from five modules: SupportChange 7, RelationLayer 11, BoundaryControl 9, ControlCompression 8, KrylovStep 3. These counts include definitions and infrastructure. The prior checked manifests select 87 tau, 73 derived and 28 structural declarations. Counts are not counts of theorems, discoveries or independent analytic inputs. The reused parser in `check_derived.py` rejects missing, unexpected, repeated and nonstandard axiom reports, allowing only `propext`, `Classical.choice`, `Quot.sound`.

## Byte identities and local artifact locations

All paths below `staging` mean:

`package:/sources/web_pr15_status_review`.

| New exact Lean source | SHA256 |
| --- | --- |
| `files/formal/splitzero/SplitZeroBoundaryControl.lean` | `78bd445b8efcde4e8e58bc489a574195f3606df9335eaeff659d0dac419343f7` |
| `files/formal/splitzero/SplitZeroControlCompression.lean` | `9149de8bbaaf132569b5b61ec9e07b058d5d295e8f9a305fd70651831191aa10` |
| `files/formal/splitzero/SplitZeroKrylovStep.lean` | `9f4902c3376bc3c3b92e3eedb4a67ca6a05b06dc2a0cea1fd2e558a0a2f2d225` |
| `files/formal/splitzero/SplitZeroRelationLayer.lean` | `719da6c00cc0e9fd828bc53753980314e2a442c27cb96ccede84c80b4c9c0578` |
| `files/formal/splitzero/SplitZeroSupportChange.lean` | `e245230b06d099fcf4c41948813a7f4d278379287506eca4293f28aa18957a26` |

`SOURCE_STATUS_RECEIPT.json` includes byte counts, SHA256 and Git blob identifiers for every staged source/context file, source URLs, primary API snapshots, selected declarations and scope findings. Reproduce the byte/status validation with `python verify_staged_sources.py` from the staging directory. It only reads sources and rewrites its own receipt; it does not invoke a theorem prover. `files/workbenches/tau-boundary-layer-formal/RESEARCH_NOTE.md` is the complete authored written proof note, and `NUMERICAL_RECORD.json` gives the explicitly non-interval numerical record.

## Exact source-level mathematical interfaces

### Support-changing maps preserve the original carrier

`SplitZeroSupportChange.lean:13–105` defines a bottom-and-join preserving map `f:L→K` and a natural family of R-linear coefficient maps `a_i:D_i→E_(f(i))`. The complete naturality identity is

\[
a_jD_{ij}=E_{f(i),f(j)}a_i\qquad(i\le j).
\]

`HomOver.total` at line 55 is the actual G(R)-linear map

\[
\coprod_{i\in L}D_i\longrightarrow\coprod_{k\in K}E_k,
\qquad(i,x)\longmapsto(f(i),a_i x).
\]

The inherited total carrier is the dependent disjoint union from `SplitZeroReconstruction.lean:42`; its global zero is `(bottom,0)`, addition transports both coefficients to the join, and scalar G(R) is unchanged. No transport, coefficient or support map is assumed injective. `total_fibre_zero` proves `(i,0)→(f(i),0)`, and `total_comp` proves compatibility with composition. `promote` at line 97 uses the actual transport `D_(i,f(i))` for an extensive support map; it is not merely a relabeling.

The exact global-zero criterion is

\[
a^{\rm total}(i,x)=0
\iff f(i)=\bot\ \text{and the transported coefficient }a_i x=0.
\]

Indeed equality in the dependent union gives equality of supports, and after transport along that equality gives equality of coefficients; the reverse direction reconstructs equality of the pair. Thus the generic support map can collapse a nonbottom fibre to bottom. For extensive promotion, `i≤f(i)=bottom` forces `i=bottom`, so a killed coefficient starting in a nonbottom fibre remains a nonbottom supported zero. The phrase “receiving fibre zero rather than external tau” in a specific quotient-transition application uses precisely this nonbottom receiving-support fact; it is not an unconditional assertion for every generic `HomOver`.

### The retained relation layer and derivative have explicit different targets

`SplitZeroRelationLayer.Data` at line 15 has a commutative ring R, an R-module B, submodules L≤M, and a linear retraction P with P(B)⊆L and P|L=1. It constructs

\[
M/L\xrightarrow{\ \sim\ }M\cap\ker P,
\quad[z]\mapsto z-Pz,
\qquad y\mapsto[y]
\]

as `layerEquiv` at line 60. Well-definedness follows because `(1-P)L=0`; the inverse identities use `P²=P`. This is an algebraic linear equivalence. No quotient-norm or continuity claim is bundled into it.

`transition` at line 82 is `T:B/L→B/M,[b]→[b]`. `derivative` at line 95 is the separately defined map `Dbar:B/L→B/M,[b]→[Db]` under the exact hypothesis D(L)⊆M. It assumes neither D(L)⊆L nor D(M)⊆M. There is an exact source consequence

\[
M/L\xrightarrow{\sim}\ker T,\qquad[u]_{M/L}\mapsto[u]_{B/L}.
\]

Both quotient equivalence relations identify differences in L, proving well-definedness and injectivity; `transition_kills_iff` says a class in the kernel has a representative in M, proving surjectivity. Composing with `layerEquiv` identifies this kernel with `M∩ker P`. The bundled kernel equivalence itself is not a separately declared target in the two files. `retained_then_killed` proves `[u]_L≠0` and `T[u]_L=0` for u∈M\L. `defect_class` retains the exact sign `[l-au]_L=-a[u]_L`.

`orthogonalData` at line 121 uses Mathlib's actual `starProjection`. The hypothesis is `L.HasOrthogonalProjection`; arbitrary submodules are not silently given projections, and ambient completeness is not required.

### Finite raw columns construct boundary escape

`SplitZeroKrylovStep.escape_of_expansion` at line 30 takes a complex inner-product space H, a subspace L with an orthogonal projection P, linear maps D:H→H and s:E→H, raw vectors f_j and linear rows a_j. Its assumptions are

\[
f_j\in L,quad Df_j=f_{j+1}\quad(0\le j\le n),
\qquad Ps=\sum_{j=0}^n f_j a_j.
\]

It concludes

\[
(1-P)DPs=a_n(1-P)f_{n+1}.
\]

For j<n, `(1-P)Df_j=(1-P)f_(j+1)=0`; the j=n term remains. This is the complete finite sum argument in Lean. `lastResidual_ne_zero` at line 24 proves `u=(1-P)f_(n+1)≠0` from `f_(n+1)∉L`.

`toBoundaryData` at line 57 adds the source identity `Ds=sA+f_0 ell` and Green identity

\[
\langle Dx,y\rangle+\langle x,Dy\rangle=\langle x,y\rangle.
\]

It constructs every field of `BoundaryControl.Data`: next vector u; the original unscaled `h=||u||²`; current row a_n; next row `t=h^{-1}〈u,s(·)〉`; and the derived escape law. Positivity/nonvanishing of h follows from u≠0. It does not assume the rank-two control formula.

`SplitZeroBoundaryControl` defines `R=(1-P)s`, `B=DR-RA`, and

\[
W(x,y)=\langle RAx,Ry\rangle+\langle Rx,RAy\rangle-\langle Rx,Ry\rangle.
\]

Its `control_boundary`, `control_cross`, `rank_two_formula`, `gram_downdate`, and `boundary_quotient` declarations are at lines 78, 90, 118, 141 and 152. They prove, retaining the given inner-product convention,

\[
W=-(R^*B+B^*R)=h(t^*a_n+a_n^*t),
\quad R_+=R-ut,
\quad R^*R-R_+^*R_+=ht^*t,
\quad[Bx]_{H/L}=-a_n(x)[u]_{H/L}.
\]

These statements allow arbitrary coefficient module E. A positive definite finite Gram matrix is additional actual-packet information, not an input silently inserted into the generic rank identity.

## Actual-theta instantiation in the current written paper

The exact written instantiation is available from the existing `tex/arithmetic_input.tex:27–45,214–270,307–328` and `tex/tau_boundary.tex`, with the following map dictionary. It is not additional Lean execution.

Use the original smooth space

\[
\mathscr B=\{F:\sup_{x>0}x^b|D^kF(x)|<\infty\text{ for every }b\in\mathbb Z,k\ge0\},
\quad D=-x\partial_x,
\quad\langle F,H\rangle=\int_0^\infty\overline F H\,dx.
\]

The integral converges by the two-end bounds. A smooth function of zero L2 norm is zero everywhere: a nonzero value would give a neighborhood of positive integral by continuity. Hence this is a genuine inner-product space on the original functions. D maps the space into itself because its k-th weighted seminorm is the `(k+1)`-st original seminorm. The ambient space is not replaced by its L2 completion.

For F,H in this space, `x overline(F)H` tends to zero at both endpoints by the same bounds. Integration of its derivative gives

\[
\int_0^\infty[-x\overline{F'}H-x\overline FH']dx
=\int_0^\infty\overline FHdx,
\]

which is the exact Lean Green input, with the original sign and dx measure.

Take `E=C[t]/h_Z`, with all actual zero orders retained; `A` is multiplication by t. Take `s=R_ref` from the cumulative paper, where `M s(u)=(g/h_Z)R_Z(u)`, `g=2xi`, `R_Z(u)` is the degree<d representative of the original unit `j_(h_Z)(h_Z/g)u`, and `ell(u)=[t^(d-1)]R_Z(u)`. Polynomial division gives

\[
tR_Z(u)-R_Z(tu)=h_Z\ell(u),
\]

so Mellin injectivity gives `Ds-sA=f_0 ell`, without altering the arithmetic unit or the zero multiplicities.

Set `f_j=D^j f_0` and `L_n=span{f_0,...,f_n}`. A finite dependence would Mellin-transform to `P(s)g(s)=0`. Since g is entire and nonzero on a nonempty open set, P vanishes on that set and therefore is identically zero. Thus every raw column is independent of its predecessors.

Let `F_n:C^(n+1)→mathscr B` synthesize the raw columns and `H_n=F_n^*F_n`. For a nonzero vector c, `c^*H_nc=||F_nc||²>0`, proving invertibility. The explicit projection is

\[
P_n=F_nH_n^{-1}F_n^*.
\]

It maps into L_n, fixes each F_n c, is self-adjoint, and its residual is orthogonal to L_n because `F_n^*(1-P_n)=0`. This supplies the actual finite orthogonal projection in the incomplete original space. The raw projection coefficients are the rows of `H_n^{-1}F_n^*s`; therefore the finite expansion in `escape_of_expansion` is an identity. The shift `Df_j=f_(j+1)` holds by definition. The next residual, norm square, inner-product row and all boundary identities above are consequently instantiated for every finite n in the written mathematics.

For `u_j=(1-P_(j-1))f_j`, the expansion `P_ns=sum_(j≤n)u_j r_j` is related to the raw expansion by an upper triangular monic basis change. Since u_n has coefficient one on f_n and earlier u_j have zero f_n coefficient, the last raw row is exactly r_n. The next constructor row is exactly `r_(n+1)=h_(n+1)^{-1}u_(n+1)^*s`. This proves the raw-to-orthogonal row correspondence used in the source note.

The packet maps `qR_n=qs` and `J_ZR_n=1` follow because the correction lies in the original theta relation space and J_Z annihilates it. They give positive definiteness of the finite packet Gram matrix `G_n=R_n^*R_n` using the smooth zero-norm argument above. They do not identify the arithmetic quotient with a quotient by an L2 closure.

## Relative Gram-volume calculation and exact declaration scope

`SplitZeroControlCompression.lean:18–127` factors the finite control matrix through `Fin 2`, proves rank≤2, and proves nonzero eigenvalue transfer using the actual two linear maps. It computes the determinant of `[[c,a],[b,conj c]]-lambda I`, its real roots under the displayed radicand hypothesis, and the scalar identity `max(|c+q|,|c-q|)=|c|+q` for q≥0. It does not bundle positive G, Cauchy–Schwarz, the Hermitian similarity, the generalized spectrum and the Loewner optimum into one declaration. Section 4 of the research note supplies that written chain:

\[
a_n=r_nG_n^{-1}r_n^*,\quad b_n=r_{n+1}G_n^{-1}r_{n+1}^*,
\quad c_n=r_nG_n^{-1}r_{n+1}^*,
\]

\[
\epsilon_n=h_{n+1}\bigl(|\Re c_n|+\sqrt{a_nb_n-(\Im c_n)^2}\bigr).
\]

Cauchy–Schwarz in the positive G_n inverse metric gives `a_nb_n≥|c_n|²`. The same positive G_n supplies the similarity `G_n^{-1}W_n ~ G_n^{-1/2}W_nG_n^{-1/2}`, whose self-adjoint spectral radius is the least two-sided form bound. The factorization transfers every nonzero eigenvalue to the displayed 2×2 matrix; zero rows and dependent rows preserve the formula because extra zero eigenvalues do not change its radius.

For a reflection-stable packet, including multiplicities,

\[
\operatorname{Tr}(G_n^{-1}W_n)=2\Re\operatorname{Tr}A-d=0=2h_{n+1}\Re c_n.
\]

Thus `Re c_n=0` and `epsilon_n²=h_(n+1)²(a_nb_n-|c_n|²)`. Define the **source note's** ratio `delta_n=det G_(n+1)/det G_n`. From the proved Gram downdate, the determinant lemma gives

\[
\delta_n=1-h_{n+1}b_n,\qquad0<\delta_n\le1.
\]

For n≥1, the backward Gram update is `G_(n-1)=G_n+h_nr_n^*r_n`, so taking its determinant gives

\[
\delta_{n-1}^{-1}=1+h_na_n.
\]

Combining these identities gives the full written identity, including the retained cross term,

\[
\epsilon_n^2=
\frac{h_{n+1}}{h_n}(\delta_{n-1}^{-1}-1)(1-\delta_n)
-h_{n+1}^2|c_n|^2.
\]

Dropping the nonnegative final quantity gives the note's bound. These determinant/reflection identities occur in the written note at lines 175–205; none is a selected new Lean declaration.

For the cumulative continuation's ratio `r_m^vol=det G_m/det G_(m-1)`, the exact index dictionary is

\[
\delta_n=r_{n+1}^{\rm vol},\qquad\delta_{n-1}=r_n^{\rm vol}.
\]

Here `h_n` belongs to the original |g|² measure. It must not be conflated with `kappa_N` for the |g/h_Z|² measure in `kernel_terminal_continuation.tex`. That file's Christoffel identity uses N=d+m, the same packet G_m, and the quotient-measure recurrence coefficient `kappa_(d+m+1)/kappa_(d+m)`. The exact common object is G_m; the determinant ratio dictionary above is the immediate bridge. The different coefficient sequences cannot be replaced by each other without the full polynomial-quotient comparison already retained in the cumulative paper.

## Analytic and numerical scope findings

The research note's Section 5 proves the actual theta Krylov span dense in L2(dx) using the logarithmic/Mellin unitary map, exponential decay of g on `Re s=1/2`, density of polynomials in `L2(|g|²dt/(2pi))` by analytic Fourier uniqueness, and multiplication by g, which is nonzero almost everywhere. It derives `G_n=sum_(j>n)h_j r_j^*r_j` and `G_n→0` for each finite packet. These are written analytic arguments, outside the 38-target Lean manifest. Neither decreasing G_n nor rank≤2 gives a vanishing relative control estimate.

Section 2's exact real diagonal coefficient 1/2 uses the actual real-valued seed and real monic orthogonalization. Green's identity alone only fixes the real part for a general complex seed. The source explicitly retains that distinction and proves the real-seed recurrence.

The numerical record is a Wolfram Language evaluation of the first four original unscaled theta norm squares with 65-digit working precision and integer cutoff 8. It explicitly says validated rounding=false, inverse-Gram error certified=false, source nineteen-test suite rerun=false, Lean certificate for numerics=false. Section 6 separately proves an omitted-integer-tail bound below 1e-80 per exact raw 4×4 Gram entry. That bound does not certify the floating-point Schur complement or inverse-Gram error. This audit reads the script and proof; it neither runs Wolfram nor substitutes numerical agreement for proof.

## Outcome and handoff

No contradiction was found in the complete five-file source review or the written finite algebra. The exact theta specialization is available as written mathematics through the explicit dictionary and proofs above; it is not currently one of the new Lean packages. The support-changing homotopy of the entire specific theta chart and the full analytic formalization remain outside PR15's declared scope. Source and execution-status evidence are sufficient to integrate this as an exact-head formal contribution with those scope labels. Its raw axiom logs were not available through the unauthenticated public endpoint, so this report does not claim an independently replayed log certificate.

All thirteen authored source files, their exact contextual pins, this report and `SOURCE_STATUS_RECEIPT.json` are ready for the root/Zeta owner. No remote merge or publication was performed in this audit.
