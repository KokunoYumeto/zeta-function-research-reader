# CUE, Mellin and support geometry: work already present and connections still open

**Comparison date: 10 September 2026.** This is a navigation and source-comparison contribution. It adds no theorem, new proof certification, or claim of novelty. The inspected zeta revision is `42d00e359b16d52ca71568ce5e3db5341949d929`. The corresponding ES revision is `9a3ddfe8b38a424f1ff0426201a1f4f6f9d2772f`.

The CUE material recovered during ES archive work belongs primarily in this zeta workbench. Much of it is **already incorporated here**, with proofs and explicit structural maps. The work to do is to expose those connections and identify the arrows still absent, not to import the elementary results as new discoveries.

## Start with the existing mathematical sources

The root [main.tex](main.tex) includes [Literature foundations](satellites/10_literature_foundations.tex). That chapter in turn includes the [CUE–Mellin programme audit](satellites/13_cue_mellin_complete_programme_audit.tex) and [split-zero/shifted Dedekind chapter](satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex). These are part of the root working source, not merely loose files. The separately frozen six-reader archive is a different edition; its ZIP payload was not byte-compared in this pass.

### From a random unitary matrix to a compact measure

The programme starts with the normalized Haar law on U(N), the characteristic polynomial Phi_N(z)=det(zI-U), and X_N=|Phi_N'(1)|². Its pushforward measure has support [0,N²4^(N-1)] for N at least 2. The peeled variable Y_N=X_N/N² has a different normalization. A crosswalk must retain that factor when moving moments or endpoint coefficients between sources.

The existing CUE chapter states and proves the exact-support and Hausdorff/Bernstein reconstruction results, the measure-valued Verblunsky recursion, complete U(2) formulas, and phase-retaining U(3) constructions. Start at labels **thm:cueM-fixedN-support**, **thm:cueM-Hausdorff-Bernstein**, **thm:cueM-measure-peel**, **cor:cueM-U2-3F2**, and **thm:cueM-U3-trace-descent**. The first three recovered CUE–Mellin source identities are recorded at [lines 1–34](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/42d00e359b16d52ca71568ce5e3db5341949d929/satellites/13_cue_mellin_complete_programme_audit.tex#L1-L34). This pass does not equate every CUE draft in the uploaded notes with those particular versions.

### From the measure to analytic transforms

For finite signed compactly supported measures on [0,infinity), the existing **thm:cueM-transform-algebra** carries additive convolution to multiplication of Laplace transforms. Its Bose integral maps that Laplace transform to the averaged Hurwitz zeta function; the finite part at s=1 gives the digamma transform. The triple retains the measure because its Laplace component is injective. The transformed peeling recursion is an average of dilation operators, not an identification of averaging with convolution multiplication. The domain, formulas and distinction are already written at [lines 399–518](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/42d00e359b16d52ca71568ce5e3db5341949d929/satellites/13_cue_mellin_complete_programme_audit.tex#L399-L518).

### From support-sensitive algebra to endpoint geometry

The [split-zero chapter](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/42d00e359b16d52ca71568ce5e3db5341949d929/satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex#L13-L88) already constructs G(R), distinguishes absence from supported cancellation, proves its coordinate-model and unique Boolean support-character result, and develops a semimodule/diagram equivalence. This is not merely a suggested analogy.

The same chapter's **thm:gcue-support-endpoint-map** gives an explicit support-lattice correspondence with two endpoint principal-part directions. For u=s(s-1) and v=2s-1, the differential A ds/u+Bv ds/u has endpoint residue coordinates (-A+B,A+B), with inverse A=(b-a)/2, B=(a+b)/2. The support projection's fibres R^I are retained in the statement: it is lossless on the support skeleton, not on all amplitudes. See [lines 612–706](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/42d00e359b16d52ca71568ce5e3db5341949d929/satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex#L612-L706).

### The finite phase-space algebra is already here

The ES integration note called **X6** is already covered by **prop:finite-weyl-coordinate-isomorphism** in [Literature foundations, lines 3293–3410](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/42d00e359b16d52ca71568ce5e3db5341949d929/satellites/10_literature_foundations.tex#L3293-L3410). The public proof gives the full operator basis for an arbitrary finite abelian group, the cocycle-twisted multiplication, an explicit trace-coefficient inverse, and the traceless restriction. X6 should be an alternate exposition linked to this existing result, not counted as another discovery.

The final paragraph states the remaining issue precisely: no map from that Weyl-coordinate algebra to a CUE measure, shifted-Hurwitz transform, or Kostka-labelled summand is constructed there. A finite matrix basis does not itself provide those additional correspondences.

## Contributions that would add something

**Complete the source-to-result crosswalk.** Match each assertion in the recovered CUE/Hurwitz drafts to the current theorem and proof, a correction, or an assertion not yet accounted for. Record normalization changes and retain source attribution. Matching a subject or title is not enough. The recovered `split_zero_cue_shifted_hurwitz_phase_space.tex` has SHA-256 `52f2a6bccdb15213b1992abef9f8d6476d6e9ea5566ee7ed9d85c9a2d7cc2705`; its finite basis appears at lines 1273–1418. Raw private notes are not republished here.

**Construct a missing structural arrow.** Investigate an explicit connection between the finite Weyl algebra and a specified CUE/Hurwitz object, or the requested representation-theoretic interpretation of a microscopic moment exponent. Specify domain, codomain, action, measure, and which property is preserved. The existing [interface boundary](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/42d00e359b16d52ca71568ce5e3db5341949d929/satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex#L965-L991) names these questions. Independent mathematics is a valid outcome even without an RH implication.

**Review or formalize an existing result.** Pick its exact statement and dependencies. Record what was actually checked; a source's report of a completed replay is not a replay by this new session. Numerical cases, a symbolic identity, a written general proof, and a formal certificate remain different evidence.

**Create a readable results package.** Extract complete definitions and proofs with source links rather than copy isolated conclusions. Build it from current statements; do not restore a superseded formula from an earlier draft just because it was recovered later.

These are open contribution opportunities, not compulsory directions or a claim that the entire CUE programme is unfinished. Existing structural maps and open ones remain separately visible.

## Comparison and rights scope

Public Git blob identities were compared with the supplied local zeta archive. `10_literature_foundations.tex` matches blob `04c807f069503632456a7bb94d3b10e19c2f0c90`; `14_globalization_cue_split_zero_and_shifted_sheets.tex` matches blob `49318a578b96462384000afa16794cfd5fe492c1`. Those matches support reading the complete local counterparts as the same files. Selected passages of the current chapter 13 were read directly from GitHub; its local counterpart is not byte-identical and was not silently substituted as the current file.

No archive code, Lean project, or mathematical replay was executed. No paper is identified as withdrawn or deleted. The new editorial text is offered under CC0-1.0 to the extent rights are held; all source rights and attributions remain unchanged. [Contributor entry methods](POLYCLANK_PARTICIPATION.md).
