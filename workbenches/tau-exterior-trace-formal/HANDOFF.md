# Handoff: determinant trace and filtered control

## Coordination

This contribution was started on PR #21, whose conormal/cyclic implementation has since been merged by the parallel session. It now includes main at `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f` in the review branch only. The only post-#21 inherited file change is the inspected CI-trigger correction keeping those proofs checked on main and on inherited formal dependency changes. Its bytes are preserved unchanged. The new trace workflow likewise covers inherited formal dependencies. No mathematical correction from Codex is overwritten; no main or other-session branch is edited by this integration.

## Bounded finite interface

The four new Lean modules are audited by `EXTERIOR_TRACE_TARGETS.json` (50 selected declarations). The PR records the final successful implementation commit/run after readback; an in-progress run is not a certificate.

`SplitZero.TraceCertificate.original_gram_bound` takes the actual Gram G with an explicit coordinate isometry, the arithmetic operator A, inclusion B and extraction L of an invariant subspace, and the actual two-coordinate factor H=UV. Its hypotheses retain LB=1, AB=B a, G-self-adjointness of BL, GH=A*G+GA-wG, tr(VU)=0 and det(VU)=-epsilon^2. It proves |2 Re tr(a)-w dim(E)|<=epsilon for epsilon>=0. It constructs the two control projections rather than assuming them, and handles epsilon=0 separately using Hermitian positivity.

The coordinate isometry does not choose a different metric. Its source map is R T^(-1), with the corresponding transported arithmetic jets and action. The inclusion B can select the full positive-defect generalized eigenspaces; diagonalizability of A is not required. Choosing that CRT subspace and constructing the isometry from a particular analytic G remain explicit caller interfaces.

`TraceProjection.projector_trace_comparison` keeps the oblique CRT projector and the orthogonal metric projector distinct. `signed_trace_slack` keeps both complementary overlap terms.

`TraceFiltration.gram_resolution_budget` proves that an actual resolution of the identity by G-orthogonal projections has total absolute trace defect at most 2epsilon. `nested_difference` constructs each graded projector from nested ones. This formalizes the finite projection calculation in Research Note section 2. The additional identification with arbitrary filtered-module quotient actions, their canonical Schur metrics, the subset budget, and the full Deligne monodromy filtration remain written proofs in that section; they are not extra Lean declarations.

## Research collaboration: an exact Deligne input

The original Weil II scan, printed p.165 section 1.6.1, supplies the nilpotent monodromy-filtration mechanism. On the existing primary module C[z]/z^ell, N=M_z, define M_j=span{z^a:ell-1-2a<=j}. The note proves N M_j subset M_(j-2), N^j:Gr_j -> Gr_(-j) isomorphisms with literal coefficient one, and duality (M_j)^perp=M_(-j-1) for the coefficient residue pairing. Every original nilpotent jet remains. The actual arithmetic A=lambda+N preserves the filtration and acts by lambda on every nonzero grade; its determinant trace is still ell*lambda. These auxiliary filtration indices are not asserted to be Frobenius weights.

This supplies a usable next formal target: construct those exact filtered modules and their residue-dual quotient maps, then apply the checked projection-resolution budget to their actual induced metrics. No new scalar implementation, no erasure of kernels, and no purity assumption is needed for that algebraic step.

## Analytic task remains with the existing source

For a fixed quartet, d_k=[1+k(m-1)](k+1)^2 and the source's exact positive defect is at least delta*k*d_k/2. Thus epsilon_(h,k,N(k))=o(k*d_k), with N(k)>=d_k-1, suffices for that contradiction route. The prior exact kernel update yields epsilon_N^2<=alpha_(N+1)*Lambda_N, where alpha is the original norm ratio and 1+Lambda_N=det K_(N+1)/det K_N. No estimate of that product uniform in tensor degree is claimed here. Neither the scalar Fisher estimate nor the filtration by itself supplies it.

## Scope of source reading and tests

Local runtime failures prevented opening the new six-part Deligne archive and the exterior ZIP. No archive reassembly, manifest audit, or rerun of their reported suites is claimed. The independent author-hosted original scan was inspected at printed pp.165,203,206. Exact source references and complete deductions are in RESEARCH_NOTE.md. No source PDF, private transcript, or external literature corpus is published.

The added standard-library Python checker has ten exact rational calibration methods, normal and optimized execution, and deliberate-failure controls. It exercises the projection calculations, nonnormal actions, original Gram transport, exterior factorial/signs and the proposed nilpotent filtration. These are not actual zeta packets or analytic interval certificates. Strict Lean execution and transitive-axiom reports supply the formal evidence separately.
