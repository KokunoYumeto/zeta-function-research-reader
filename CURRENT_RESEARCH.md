# Zeta, theta cohomology and arithmetic weight control

This research collection develops explicit calculations about the Riemann zeta
function and the operators that encode it. The current focus is the
**Split-Zero and theta-cohomology programme**: preserve the information in
functions and their relations, extract finite spectral data, and calculate the
arithmetic matrices that control those data. The motivation comes partly from
Deligne's approach to weights in Weil II; the present work constructs and
calculates its own analytic objects rather than claiming that analogy alone
proves the Riemann hypothesis.

Start with the [216-page cumulative calculation reader](workbenches/splitzero-tandem/continuations/20260912-frontier/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf).
Its [complete proof sources, appendices and checks](workbenches/splitzero-tandem/continuations/20260912-frontier/)
are directly readable on GitHub. The broader [425-page zeta research reader](reader.pdf)
contains the literature reconstruction, CUE random-matrix calculations,
arithmetic transforms, and the source-directed fluid calculations.

## What the objects mean

- **Split-Zero coefficients** retain a ring's original zero as a supported
  element while adjoining a distinct external zero, denoted tau. Maps retain
  which fibre an element belongs to; killing its coefficient is not silently
  identified with forgetting that fibre.
- **Theta cohomology** here means a specified space of rapidly decreasing
  functions modulo the image of a specified theta-function summation map.
  Under the Mellin transform, that map becomes multiplication by
  `g(s)=2 xi(s)`, with `xi` the completed Riemann zeta function. The notes state
  the test spaces, inverses and quotient maps explicitly.
- A **spectral packet** is a finite collection of spectral points with their
  full multiplicities. The quotient `E_h=C[s]/(h)` records all derivatives up
  to those orders. Repeated roots therefore retain nilpotent directions.
- The **arithmetic Gram matrix** is the matrix of inner products of the chosen
  original theta-derived representatives. The control form measures how their
  scaling action departs from the central weight. Their relative size, not
  either matrix's absolute smallness, is the quantitative question.

## What was tried, why, and what it produced

| Calculation | Why try it? | Result and present scope |
|---|---|---|
| [Constrained interpolation](workbenches/tau-coherent-interpolation/) | Compute minimum-norm representatives from the actual arithmetic measure, rather than choose a convenient replacement metric. | Full-jet kernel/Gram inverse formulas, nested-packet comparisons and a joint total-degree tensor construction. The original local units and theta primitives remain in the maps. |
| [Boundary control from raw theta derivatives](workbenches/tau-boundary-layer-formal/) | Derive the small-rank control matrix from the actual derivative sequence. | Exact escape, relation-quotient and Gram-update formulas; five new Lean modules checked at the recorded PR15 head. The analytic theta specialization and integral estimates have separate written proofs, not an inferred Lean certificate. |
| [Theta norms and kernel layers](workbenches/splitzero-tandem/continuations/20260912-frontier/tex/kernel_layer_continuation.tex) | Connect the packet-dependent interpolation problem to the original theta norm sequence and track the next relation. | Complete norm/Gram-volume identities, a full relation-layer graph and derivative quotient, retaining initial indices and cross terms. See the cumulative reader's named kernel-layer sections for the complete formulas. |
| [Symmetric arithmetic frontier](workbenches/splitzero-tandem/continuations/20260912-frontier/) | Use the original conjugation/reflection symmetries to sharpen the actual control estimate. | Quartet parity removes the general factor two in the stated finite-stage bound. Literal orbit sums transport it to signed symmetric cohomology, retaining orbit multiplicities and zero cases. An asymptotic vanishing estimate is not asserted. |
| [Spectral-sum pushforward](workbenches/tau-spectral-sum/) | Carry a tensor calculation onto one spectral coordinate without discarding the relative directions. | One-variable matrix weights, exact Jacobians, duality, traces and complete nilpotent sum fibres. The original filtered image and arithmetic metric are retained. |
| [Axial source-to-arithmetic transport](satellites/29s_ns_axial_branch_radius.tex) | Determine exactly which singularity information from the specified fluid source survives its arithmetic transform. | The broad reader's Sections 35–37 give all-axis Mellin data, four complex branch points, the sharp moving radius and an invertible endpoint-residue map. This is a calculation on the stated source patch, not a new zeta-zero witness or independent certification of the imported fluid existence theorem. |

The full proofs, rather than this summary, fix domains, signs, coordinate
changes and the scope of each conclusion. The cumulative reader contains 22
proof sections and nine complete source appendices. Its checks include exact
finite regressions and separately identified arithmetic enclosures. The
publication does not conflate those checks with the complete written proofs.

## Continuing the shared work

The next quantitative questions concern the **same original arithmetic
columns, norms and filtered spaces**: what the finite-stage estimates do as
the degree and tensor order grow, and which explicit source estimates control
that growth. New contributions should identify the calculation attempted,
its motivation, the full map or estimate obtained, what failed or remains
unfinished, and the precise source revision. Earlier attempts remain in
[ATTEMPTS.md](ATTEMPTS.md); the broader library-to-programme map is
[RESEARCH_PROGRAMMES.md](RESEARCH_PROGRAMMES.md).

Frozen older editions remain linked in the repository. The current edition's
PDFs are separate readable files, with paired source packages and publication
identities. Raw conversation transcripts and local literature archives are
research references, not public payload.
