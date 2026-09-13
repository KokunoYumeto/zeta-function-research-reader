# Current R57 Split-Zero source: what was calculated and why

[Read the 765-page paper](workbenches/splitzero-tandem/continuations/20260913-sga-connes/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf) · [Source/build guide](workbenches/splitzero-tandem/continuations/20260913-sga-connes/README.md) · [Earlier frozen DOI](https://doi.org/10.5281/zenodo.22732414)

The 765-page Split-Zero paper retains the original theta-function source, zero multiplicities, full source mass, the coordinate S=k/2+iu and the least-norm quotient metric. Through R57 it adds the explicit Hochschild comparison kernel, constituent curvature and Laplacian control to the endpoint, period and determinant calculations. A uniform arithmetic upper estimate is not established; no RH conclusion is claimed.

For a selected zero packet h, the input is 2ξ/h, where ξ is the completed Riemann xi-function and h retains every selected zero order. At tensor degree k, the polynomial source has norm

$$\|\mathcal V_{h,k}P\|^2=\int_{\mathbb R}|P(k/2+iu)|^2m_{h,k}(u)\,du,$$

where w_h(t)=|(2ξ/h)(1/2+it)|²/(2π), m_{h,k}=w_h^{*k}, and *k means k-fold convolution. Its mass is not normalized away. The canonical quotient metric is obtained by minimizing this same norm among representatives of a polynomial class modulo its actual relation polynomial.

The reason to compute the comparison kernel is to know exactly which generalized zero blocks a trace observation retains. The R53–R57 continuation then computes constituent curvature and controls the Laplacian action in the original source-induced metric. The finite maps and defects are explicit; they do not supply the still-missing uniform arithmetic upper estimate. Both the historical damaged source paragraph after SGA50 and its complete SGAC7 correction remain disclosed in the source appendix.

[PR28](workbenches/tau-split-integration/RESEARCH_NOTE.md) independently integrates the original quotient, observation, residue and period-coordinate maps, including both transition defects. Lean checks cover the stated finite map identities; exact fixtures and the written arithmetic application retain their documented scopes. All eight actual merge-push workflow statuses were successful at the recorded observation; no new full postmerge log review is claimed here.

This fixed PDF/source cut ends at R57. Later R58–R62/FC/HG/HD work is not included. The following earlier guide is retained as a historical description of the 715-page DOI and preceding work, not relabelled as a newly published edition.

## Earlier edition and research guide (historical)

# Latest complete reader: Split-Zero cohomology, 715 pages

[Read the paper](https://zenodo.org/api/records/22732414/files/33-splitzero-period-deligne-continuation-715p.pdf/content)
· [Edit or rebuild its source](workbenches/splitzero-tandem/continuations/20260913-deligne/README.md)
· [Exact publication provenance](workbenches/splitzero-tandem/continuations/20260913-deligne/PUBLIC_DERIVATION.md)

[Published DOI 10.5281/zenodo.22732414](https://doi.org/10.5281/zenodo.22732414) · [All 34 files](calculation_edition_20260913_deligne/README.md). The 715-page PDF is the actual Zenodo preview; its matching public source archive is an offline download.

The aim is to relate the zeros of the Riemann xi function to the metric size of
their actual arithmetic quotient classes. The source is
`w_h(t)=|(2xi/h)(1/2+it)|^2/(2pi)`, where `h` retains every selected zero order;
tensor degree `k` uses its literal convolution `w_h^{*k}` and full mass. Polynomial
representatives are measured in `S=k/2+iu`, then mapped to the specified cyclic
arithmetic quotient. Its least-norm metric is retained throughout.

The cumulative calculation first expresses the metric and its phase in source
and relation determinant volumes. It then develops arithmetic endpoint norm
bounds, the exact product over consecutive degree windows, and the volume
contraction required by an off-line quartet. These are useful finite and
asymptotic comparisons; the opposing arithmetic volume upper estimate has not
been completed.

The new complete cut adds the endpoint optimizer, reflected relation fibres,
relation-moment comparison, and the next restriction/window calculations. Its
Deligne chapters supply the stated cohomological comparison maps, logarithmic
specialization and invariant-subspace coupling, polynomial-exponential
cohomology, a complete period determinant, and translation back to the original
arithmetic operator and metric. Source hypotheses, domains, codomains, measures,
phases and zero orders remain in the full proofs. The closing account runs
through R52 and retains 41 complete source witnesses. The primary-source
correction and execution-provenance correction are included, not hidden.

The 715-page PDF ends before the later SGA/Hochschild SC/CC increment. PR26 and
PR27 also remain separately available as working-source records below; their
own review/CI scope is not silently assigned to every analytic chapter here.
No RH conclusion, new Lean execution or fresh mathematical test replay follows
from this publication step.

The public source is a disclosed derivative of the completed owner cut. All
mathematical TeX/Lean/HTML, PDFs, images and ten delivery ZIPs retain their exact
bytes. Only recorded private-locator metadata/helper edits and a reference-only
full-page cache omission affect the public selection. The current manifest
describes the derivative, while inherited receipts and manifests retain their
historical scope. The original private source archive is not a public payload.

The following historical guide describes **the earlier DOI 10.5281/zenodo.22731295 edition**. Its 478/512-page downloads remain unchanged and are also retained among the new edition's 34 files. That earlier record does not contain the new 715-page reader.

---

[Earlier frozen DOI 10.5281/zenodo.22731295](https://doi.org/10.5281/zenodo.22731295) · [Paired PDFs and sources](calculation_edition_20260913_endpoint_gamma/README.md)

# Earlier frozen edition: arithmetic zeta packets: endpoint norms, exact window products and gamma source control

This edition joins the full arithmetic endpoint argument to the earlier
Toda--Gamma research synthesis. Its main reader keeps the original
theta-function source and its total mass, proves the diagonal and balanced
monic norm bounds, and retains every phase and repeated interior contraction
in the exact degree-window product. For any exact off-line quartet packet,
write `B_k = log(V_(q_k-1) V_(q_k) / (V_(2q_k-1) V_(2q_k)))`, where the
`V_j` are its canonical quotient volumes and `q_k=[1+k(m-1)](k+1)^2` retains
the quartet multiplicity `m`. The proved bound is
`liminf B_k/(q_k log k) >= 4`: for each positive epsilon, this logarithmic
volume ratio eventually grows at least `(4-epsilon) q_k log k`.
An opposing arithmetic volume upper estimate remains unproved; no RH
conclusion follows.

The source is the actual density
`w_h(t)=|(2xi/h)(1/2+it)|^2/(2pi)`, with convolution `w_h^{*k}` and mass
`mu_h^k`. Monic norms are measured in the original coordinate `S=k/2+iu`.
The quotient volumes come from the canonical least-norm representatives,
not a replacement metric. Keeping multiplicities and source factors is why
the endpoint calculation provides meaningful arithmetic control.

The main reader includes the complete arithmetic local-mass and convolution
proof, balanced-window extension, exact product with phase and zero cases,
four-volume synthesis, and corrected confluent-transfer proof. The
leading-coefficient isomorphism begins at n>=q. The squared transfer uses
dagger stability and the induced S=c+iu quotient with raw derivative phases
and factorials. Those qualifications are not omitted in the integrated text.

The separately paired 478-page Gamma companion has its own exact source
archive and review. It develops the coefficient join, seed intervals and
source costs, finite metric transfer, and phase/fibre transport on top of
the cumulative Toda source. Its scope is not silently enlarged to assert
that every newer endpoint chapter also appears there. Its contributed PDF
and independently rebuilt comparison PDF are distinct byte objects.

## Reading and reproducibility

- Begin with [Split-Zero Cohomology and Arithmetic Weight Control, the frozen 478-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0e11075765b6e0f4de2beb7d392e2ace94df0ffa/workbenches/splitzero-tandem/continuations/20260913-gamma/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf),
  distributed as `30-splitzero-gamma-continuation-478p.pdf` and shown as the Zenodo PDF preview.
- The [frozen 512-page integrated reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/reader.pdf),
  distributed as `29-main-reader-gamma-endpoint-control.pdf`, contains the broader research synthesis.
- This complete main source archive contains `main.tex`, its full recorded
  TeX closure, all previously selected authored work, and the complete
  [endpoint working-source guide](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/952ef9fee1e1419b6858d920354de8fa99430b7d/workbenches/tau-arithmetic-endpoint-bounds/README.md).
- The [original arithmetic note](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/952ef9fee1e1419b6858d920354de8fa99430b7d/workbenches/tau-arithmetic-endpoint-bounds/delivery/RESEARCH_NOTE.md),
  [exact product proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/952ef9fee1e1419b6858d920354de8fa99430b7d/workbenches/tau-arithmetic-endpoint-bounds/window/WINDOW_PRODUCT_PROOF.md),
  [four-volume synthesis](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/952ef9fee1e1419b6858d920354de8fa99430b7d/workbenches/tau-arithmetic-endpoint-bounds/FOUR_VOLUME_THRESHOLD.md),
  and [corrected transfer note](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/952ef9fee1e1419b6858d920354de8fa99430b7d/workbenches/tau-confluent-transfer/RESEARCH_NOTE.md)
  are complete texts, not replaced by this guide.
- The separate companion source ZIP retains the exact accepted frozen owner
  release and its declared verification closure.
- The broader [research attempts](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/952ef9fee1e1419b6858d920354de8fa99430b7d/ATTEMPTS.md),
  [research programmes](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/952ef9fee1e1419b6858d920354de8fa99430b7d/RESEARCH_PROGRAMMES.md),
  and [Polyclank participation guide](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/952ef9fee1e1419b6858d920354de8fa99430b7d/POLYCLANK_PARTICIPATION.md)
  remain part of the cumulative project, beyond this reader's endpoint focus.

Written analytic proofs, finite regressions, interval enclosures and Lean
checks keep their separate recorded scopes. The new analytic constants are
finite specified source quantities, not numerically enclosed constants.
The source inventory names every retained file and binds the PDF/build
identity; post-promotion source-commit binding remains an external receipt,
not a fabricated future hash embedded in its own source archive.
`EDITION_SOURCE_SELECTION.json` is the current archive inventory; retained
earlier public-file manifests are explicitly historical provenance. Full
original proof notes and portable mathematical checkers are included.
Private intake text, raw environment logs, source images, and local-only
integration scripts are excluded; selected review evidence retains its full
scope with private machine locators replaced by public aliases.

The preceding [Toda--Gamma edition](https://doi.org/10.5281/zenodo.22730756)
and all earlier downloads remain immutable. The
[versioned research collection](https://doi.org/10.5281/zenodo.22678085)
provides archived editions. This edition is published as DOI 10.5281/zenodo.22731295. Source ZIPs are offline downloads; the current 478-page Split-Zero
cohomology paper is the preview, not the main reader or either ZIP.

## Working sources after the frozen edition

The [restriction and trace-certificate calculation](workbenches/tau-restriction-certificate-formal/RESEARCH_NOTE.md)
continues the [consecutive-window argument](workbenches/tau-consecutive-window-formal/RESEARCH_NOTE.md).
The arithmetic source consists of polynomials measured by
`integral |P(k/2+iu)|^2 w_h^{*k}(u) du`, with its original mass retained.
Here `w_h(t)=|(2xi/h)(1/2+it)|^2/(2pi)`: xi is the completed Riemann
xi-function, h retains the selected zeros with their full orders, and `*k`
means k-fold convolution of that same density.
The quotient identifies polynomials whose difference belongs to the original
relation ideal `(chi_(h,k))`. Each quotient class has a canonical least-norm
representative at degree N; its Gram matrix is `G_N`, and `V_N=det G_N` is
the corresponding quotient volume.

PR26 writes the degree-j to degree-i restriction exactly as `T_ij=K_i G_j`,
where `K_i=G_i^(-1)`, and proves the commuting source-cutoff identity for
the representatives themselves. It retains the quotient coordinates, weighted
source columns and all q modes, including zero modes of `H=I-T_ij`.
Traces of powers of this finite matrix give a checkable logarithm bound:
with `P_p=sum_(m=1)^p Tr(H^m)/m` and `s_p=Tr(H^p)<1`,
`P_p <= log(V_i/V_j) <= P_p+(P_(2p)-P_p)/(1-s_p)`.
This turns the existing finite volume loss into a trace-only certificate.
For each fixed finite matrix the calculation reaches a stopping degree; it
does not establish a bound uniform in tensor degree k.

Lean checks cover the stated finite matrix and scalar-log identities; exact
fixtures and the written arithmetic application retain their documented scopes.
The finite fixtures do not certify unevaluated arithmetic moment integrals.
No opposing arithmetic volume upper bound or RH conclusion is established.
The actual PR26 merge includes its PR25 ancestor with the reviewed corrections;
GitHub closed PR25 through that ancestry, not through a separate merge action.
These working sources are not included in the frozen 512/478-page DOI edition.

## Specialization, Hochschild trace and the Laplacian

[PR27](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/27)
continues the same polynomial source and quotient, with multiplication by the
original coordinate represented by `A=M_S`. The purpose is to calculate how
source relations, boundary specialization and arithmetic action interact, so
that geometric information can be used in the existing volume estimate.

The [specialization calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/RESEARCH_NOTE.md)
joins two actual representatives by `R(z)=R_j+z delta R`.
Their source orthogonality gives `G(z)=G_j+|z|^2(G_i-G_j)`, with the same
quotient class throughout. At the boundary `w=1/z=0`, the local map
`(a,b)->(a,w b)` has both a kernel and a cokernel equal to the modified
summand. The transported action retains its possible `w^(-1)` term.
The least action-invariant enlargement is computed in `C[S]/(chi)` by a
polynomial gcd; the resulting metric pole contributes a signed curvature
atom at infinity. That atom accounts for the degree change rather than
silently cancelling the source's positive curvature density.

For the original restriction operators, `Z=K_j(G_i-G_j)` and `H=I-K_i G_j`,
the exact relation is `H=Z(I+Z)^(-1)`. Thus each cost eigenvalue `lambda`
has coordinate `x=lambda/(1+lambda)`, including zero modes. The curvature
coefficients recover `Tr(H^m)` by finite telescoping. This feeds the preceding
finite volume certificate; it does not establish a bound uniform in packet size.

The [Hochschild comparison](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/HOCHSCHILD_COMPARISON.md)
places the original theta sum `Theta phi(x)=2 sum_(n>=1) phi(nx)` in the
specified trace image of the adele crossed product. Its trace equals `Theta`
exactly. The half-density map `U F(x)=x^(1/2)F(x)` preserves the original
half-line norm and gives the chapter's map as `E=(1/2)U Theta`.
The Gaussian identity `(D^2-D) exp(-pi x^2)=phi_*`, with `D=-x d/dx`,
therefore reproduces the unchanged arithmetic seed `Theta phi_*` and its
Mellin transform `2xi`.

Restriction of the Mellin transform to `s=1/2+it` induces an explicit map
from the full arithmetic quotient to a Schwartz-function quotient on the
critical line. On each actual finite packet, its kernel is exactly the sum
of the off-critical generalized blocks. The critical blocks have a jet
recovery map with all factors `i^(-j)/j!` retained. This calculates the map's
failure of injectivity; it does not infer that the killed blocks are absent.

The same note checks a literal boundary issue in Connes--Consani's printed
zero-mode formula: the seed's raw coefficient is `xi(1/2)L^(-1/2)`, which
is nonzero and singular at length `L=0`. An augmented Fourier object retains
that line, with an explicit reconstruction of the raw coefficient. Gaussian
averaging of the original source then places the line in the closed
source-generated submodule, justifying its subsequent quotient. The result
is a written local smooth-flat comparison; no uniform source norm bound in
the growing heat parameter is claimed.

Finally, the [Laplacian estimate](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/LAPLACIAN_PARABOLA.md)
uses the original `G`, `A` and action defect `W=A*G+GA-kG`.
For `L=A^2-kA`, the exact adjoint defect is `L*G-GL=A*W-WA`.
If `epsilon` is the actual two-sided bound `-epsilon G <= W <= epsilon G`,
every numerical-range value `z=<v,Lv>_G/||v||_G^2` satisfies
`Re z <= (epsilon^2-k^2)/4` and
`(Im z)^2 <= epsilon^2((epsilon^2-k^2)/4-Re z)`.
This enclosure retains non-real values at positive error and the full
quadratic nilpotent term on repeated-zero blocks. The required arithmetic
limit `epsilon_k/k -> 0` is not proved here.

The five new Lean modules check their stated finite/local interfaces and
38 selected declarations, alongside 33 inherited declarations. The exact
17- and 10-method Python suites are separate finite calibrations, not Lean
proofs of Schwartz-space closure, heat limits, sheaf globalization or the
numerical-range estimate. These written arguments received a separate
mathematical review. The original source checkpoint remains unchanged;
current-head and actual-merge CI observations are recorded separately in
the publication metadata. No local Lean execution or RH conclusion is claimed.
All of this PR27 continuation remains outside the frozen 512/478-page DOI edition.
