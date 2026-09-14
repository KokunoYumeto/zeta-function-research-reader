# PR27 integration review

Reviewed head: `a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8`.
Reviewed base: `e4ee97cdce904d4b9bb5697d33095aaa00083f24`.
Date: 13 September 2026.

## Decision and scope

The written mathematics and the stated finite formal interfaces are suitable for integration, subject to the separate exact-head CI and finite-check receipt. This review does not promote the analytic discussion to a Lean theorem, establish a uniform arithmetic error estimate, or change the frozen Zenodo edition. The current Split-Zero cohomology PDF remains its human reading preview.

The parent read all of `RESEARCH_NOTE.md`, `HOCHSCHILD_COMPARISON.md`, `LAPLACIAN_PARABOLA.md`, all five new Lean modules, both new audit files, both complete finite checkers, the new workflow, `STATUS.md`, `VALIDATION.json`, and `COORDINATION.md`. The independent primary-source review in `hochschild/MATH_REVIEW.md` was read completely and is part of this decision. Its reviewer read the complete nineteen-page published Connes–Consani chapter and visually checked the sensitive passages. The parent did not independently render that chapter or rerun Lean locally.

## What the continuation does, and why

The existing programme computes a finite arithmetic quotient using representatives in its original theta source. Raising the permitted polynomial degree changes the least-norm representative and its Gram metric, even though the arithmetic class remains fixed. This continuation interpolates between those actual representatives, studies the specialization at infinity, and calculates the scalar curvature information that can feed the existing finite trace certificate. It also relates the original theta source to the published Hochschild trace construction, recording exactly which finite spectral classes survive critical-line restriction.

### 1. Representative curve and specialization

With the original observation operator retained, write `delta = X - R_j`. The identities `B delta = 0` and `R_j* O delta = 0` give the actual Gram curve

`G(z) = G_j + |z|^2 delta* O delta`.

No cross term has been silently discarded: it vanishes by the displayed source relation and orthogonality. Splitting the coefficient space into `E_0 = ker(delta)` and its `G_j`-orthogonal complement `E_1` gives the sheaf `E_0 O direct-sum E_1 O(-1)`. In the infinity chart the map is `(a,b) -> (a,w b)`. The two-term derived fibre consequently retains both kernel and cokernel `E_1`; it is not just the ordinary specialization image. Applying `B` and then `delta` proves injectivity of the displayed boundary representative.

Transport of the original action has a `w^-1 P_1 A P_0` term. Its vanishing is exactly invariance of `E_0` under `A`. The least invariant enlargement is the span of all `A^n E_0`, not a newly chosen metric or action. In the cyclic algebra `C[S]/(chi)`, its gcd description uses the ideal `(d)/(chi)` with `d = gcd(chi,p_1,...,p_m)`. Multiplication by `d` has the stated quotient domain because cancellation is performed in the polynomial ring. The zero-subspace and full-subspace endpoints are included. Finite Cayley–Hamilton truncation and coherent-sheaf globalization are written mathematics, not claimed among the selected Lean declarations.

### 2. Curvature and the original restriction operators

The coordinate formula `G_A = M* G_M M` carries the pole contribution `|w|^(-2 s_A)` into the determinant. The signed atom in the dual curvature is therefore retained as `-s_A delta_infinity` in the stated convention. The total degree agrees with `deg(d)`; it is not obtained by forgetting the pole.

The reciprocal spectral coordinates are those of the original kernel/metric pair:

`Z = K_j(G_i-G_j)`, `T = K_i G_j`, `H = I-T`, `(I+Z)T = I`.

For each nonnegative eigenvalue `lambda`, the coordinate is `x = lambda/(1+lambda)`. Differentiating `t lambda/(1+t lambda)` gives `lambda/(1+t lambda)^2`. The logarithmic integral is `log(1+lambda)`, while the curvature jets give successive differences of the retained trace moments. This is a calculable route to the existing finite certificate; it does not prove a uniform bound along the arithmetic tower. The formal spectral theorem carries its explicit witness instead of claiming that a general matrix's spectrum has already been constructed.

### 3. Hochschild trace and the full-to-critical map

For the specified finite-unit-invariant image in Hochschild homology, the original theta map is literally the trace: `Tr j(f) = 2 sum_(n>0) f(nu)`. Under the half-density isometry `U F(u) = u^(1/2) F(u)`, the chapter's map is `E = (1/2) U Theta`. Both the factor two and the half-line measure remain. The Gaussian calculation gives `(D^2-D)g_0 = (4 pi^2 x^4 - 6 pi x^2) exp(-pi x^2)` and `M Theta phi_* = 2 xi`.

Critical restriction defines a continuous quotient map, not a claim that the full and critical quotients are identical. On the retained actual finite packet its kernel is calculated: every off-critical generalized block is killed because the shifted multiplier has a Schwartz-preserving inverse. On a critical block, the jet functional has coefficients `i^(-j)/j!`, cancelling the `i^j` from differentiation along `s=1/2+it`. Together with the expressly retained earlier packet right inverse this proves the exact finite kernel formula, including all multiplicities. Earlier global retraction and packet realization results remain identified prior inputs, not newly verified by these finite tests.

### 4. Retaining and then quotienting the zero Fourier line

The primary review confirms the printed raw section has zero coefficient `L^(-1/2) xi(1/2)`, which is nonzero and not smooth at `L=0`. The replacement object retains a separate renormalized zero line. Its reconstruction and covering transfer are explicit, so the line is not erased by a change of notation.

For each fixed positive heat parameter, Gaussian averaging of the original dilations converges in the Schwartz source and preserves its two moment conditions. On bounded length intervals the nonzero Fourier modes tend to zero in every local smooth-flat seminorm, while the zero coefficient remains `xi(1/2)`. Thus the full zero line belongs to the closed source-generated submodule and can be removed by the displayed quotient map. This repairs that local section convention; it does not imply an RH counterexample or supply a uniformly bounded family in the original source as the heat parameter grows. The source's printed reciprocal-length limit is also identified explicitly rather than copied uncorrected.

### 5. Laplacian and numerical range

For the unchanged arithmetic action and metric,

`L = A^2-kA`, `W = A*G+GA-kG`, `B = A-kI/2`,

direct expansion gives `L*G-GL = A*W-WA` and `GL = WB-B*GB-k^2 G/4`. Jet evaluation retains `rho(rho-k)I+(2rho-k)N+N^2`, including the quadratic nilpotent term. The finite Lean modules verify the stated polynomial and intertwiner identities without inventing an invariant positive metric.

For a unit vector in the original `G`-metric, put `r=||Bv||` and `a+ib=<v,G^-1 W Bv>`. The actual two-sided control bound gives `a^2+b^2 <= epsilon^2 r^2`. The asserted parabola follows from the exact nonnegative remainder

`(a-epsilon^2/2)^2 + epsilon^2 r^2 - a^2 - b^2`.

It controls the full numerical range without diagonalization, including `epsilon=0`. Negative real part at a positive finite error is not asserted to be a real negative spectrum. The required arithmetic error-ratio limit is not proved here.

## Verification interpretation and publication handling

The original status files accurately name their earlier successful checkpoint; the integration receipt must additionally verify the exact current head and the actual resulting merge. Both new checkers' built-in negative switches are unconditional failure-path controls, not mathematical mutations. Independent substantive mutations, if run, must be reported separately. The CI trigger omissions identified by the workflow reviewer are a future trigger-coverage repair, not evidence that the observed exact-head executions failed. Keep that repair distinct from the immutable reviewed source.

Integrate only the sixteen reviewed additions, preserve all 6,030 current-base leaves and the source branch, and verify the complete resulting Git tree and public bytes. The analytic notes remain written results alongside their narrower checked interfaces. Do not insert private transcripts or reference PDFs into the repository or Zenodo payload. The next cumulative reader can incorporate these maps after its owner delivers an exact complete source cut; the completed current edition remains unchanged in the meantime.
