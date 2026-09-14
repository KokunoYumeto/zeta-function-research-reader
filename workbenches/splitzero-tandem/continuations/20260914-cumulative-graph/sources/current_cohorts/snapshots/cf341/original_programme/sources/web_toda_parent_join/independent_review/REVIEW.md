# Independent Toda intake and mathematical review

Date: 2026-09-12 UTC / 2026-09-13 Europe/Berlin.

Outcome: the new source/relation determinant formula, matrix curvature, original-coordinate phase, first-degree endpoint, two-loss scalar identity, and finite upper bound agree with independent derivations. The parent's four-loss join with the companion exterior calculation also agrees. There is one endpoint **notation correction**, not a change to the boxed formula. The original archive and all extracted source bytes remain unchanged.

## Intake and reading

The supplied ZIP is 677,293 bytes, SHA-256 `80b365233ba5ebaf1b52aeea369a7771d74bf774dbb4416f10a56503321b8f41`. All 36 regular members passed path, Windows collision, file-kind, CRC, expanded-size, SHA-256, and post-extraction checks. Its 35-entry internal manifest covers exactly every other member. Expanded size is 887,236 bytes. Nothing was promoted into a corpus or publication root.

Read the entire `NOTE.tex` (31,153 bytes; SHA-256 `027cd27a5fc104c5ebdf0102ee43aafd7b6218da4929ceb1b8913e3448cd2375`), the entire `check_toda_volume.py`, `evaluate_seed.py`, `HANDOFF.md`, `README.md`, `CHECKS.md`, and `SOURCE_REVIEW.md`. The archive's prose is source data, not task authority. No renderer/PDF was produced or visually certified by this reviewer.

## 1. Determinant-line map and unchanged source

Let `chi` be the actual monic degree-q relation and `N >= q-1`. The ordered columns

`(1, S, ..., S^(q-1), chi, chi S, ..., chi S^(N-q))`

give an invertible triangular coordinate map of determinant one from the original monomial source. In this basis its Gram is `[[U,B],[B*,C]]`; the original relation Gram is C, and the least-norm quotient Gram is exactly `U - B C^-1 B*`. The determinant factorization therefore gives

`det G_N = det M_N / det C = D_(N+1) / B_(N-q+1)`.

This is a map of the displayed exact sequence, not a choice of a different quotient metric. At `N=q-1`, the relation block is absent, its determinant is one, and the formula is still literal. At `q=0, chi=1`, numerator and denominator agree; the determinant of the zero-dimensional quotient is one without introducing a nonzero spectral module.

The coordinate substitution `S=c+i u` has diagonal `1,i,...,i^N`. The full source Gram changes by the squared modulus of its determinant, which is one. The relation columns acquire the same explicitly unimodular phases in their corresponding degrees. No mass division is involved: multiplying the actual measure by b multiplies `G_N` by b, its determinant by `b^q`, and source/relation determinants by `b^(N+1)` and `b^(N-q+1)` respectively.

The differential filter is also literal: expanding the two fixed coefficient polynomials in `conj(chi)(c-i d_theta) chi(c+i d_theta)` and differentiating the Laplace integral gives exactly `|chi(c+iu)|^2` in the integrand. The two signs and coefficient conjugation are necessary. This weight is the norm of multiplication by chi in the original source; it is not an identification of the pullback of a higher ideal power with `(chi^r)`.

## 2. Least-norm derivative and matrix curvature

Write `D_N=chi P_(N-q)` for the fixed relation subspace and `R` for the quotient lift in the moving weight `exp(theta u)m_k(u)du`. Because its quotient coordinates are fixed, `R'` lies in D_N. For every fixed d in D_N, differentiating `<d,R>_theta=0` gives `<d,R'>=-<d,XR>`. The unique vector in D_N with those pairings is

`R' = -P_D XR`.

Consequently `G'=R*XR`. Differentiating once more, including the weight derivative, gives `G''=R*X²R-2R*XP_D XR`. The projection to the quotient representatives is `P_E=RG^-1R*`, and the original source has `P_source=P_E+P_D`. Thus

`G''-G'G^-1G' = R*X(1-P_source)XR - R*XP_D XR = O*O-I*I`.

This verifies the **matrix** identity, not just its trace. The output of O is the one new polynomial direction. For `d=chi Q` below the highest relation degree, `Xd` remains in D_N and pairs to zero with R; therefore the adjoint of I vanishes on a codimension-one relation space. Both ranks are at most one. Differentiating a source class produces an actual old relation; monic division followed by the previously constructed theta primitive gives its cochain primitive. No relation is erased before its positive Gram is evaluated.

The source and relation Hankel flows each follow by differentiating the monic recurrence. Lower-degree orthogonality makes `Q_j'=-a_j Q_(j-1)`; then `(log h_j)'=b_j` and `b_j'=a_(j+1)-a_j`. Summing over `j<n` leaves `a_n`. Their difference therefore gives the stated determinant curvature. At relation dimension zero its logarithm is zero; no negative-index determinant is evaluated.

## 3. Phase identity in the actual S-coordinates

In the transported u-coordinates the quotient relation is real because of dagger reflection; this retains the phase `chi(c+iu)=i^q phi(u)`, not a replacement of chi. Put `T=(A-cI)/i`. Let `d_j=[Q_j]` and `beta=Q_(N+1)-R d_(N+1)`. Its quotient is zero. Since Q_(N+1) is orthogonal to P_N, `R*beta=-G d_(N+1)`.

The leading coefficient row of R is `d_N*G/omega_N`: expand R in its monic orthogonal source columns. Hence `XR-RT-beta(d_N*G/omega_N)` is an old relation of degree at most N. Multiplication by R* kills exactly that old relation. Taking the trace proves

`d_N*G d_(N+1)/omega_N = Tr(T) - (log det G)'`.

Transporting `p_j(c+iu)=i^j Q_j(u)` contributes `conj(i^N)i^(N+1)=i`. The correct original cross term is therefore **positive i** times the real trace-minus-volume derivative. A real auxiliary tilt does not impose zero phase. Both independent asymmetric finite fixtures and the source checker detect the nonzero subtraction.

## 4. Endpoint and scalar upper bound

For `N>=q`, the kernel update `K_N=K_(N-1)+b_N b_N*/omega_N` gives the stated leverage `b_N*G_N b_N/omega_N=1-delta_N`. The next update gives `b_(N+1)*G_N b_(N+1)/omega_(N+1)=delta_(N+1)^-1-1`. Their product and the phase identity yield the exact radius formula, without changing G or discarding its imaginary cross term.

At `N=q-1`, the correct endpoint quantity is

`d_q* G_(q-1) d_q = ||Q_q-phi||² = nu_0 - omega_q`,

where `phi=i^-q chi(c+iu)` is the explicit u-coordinate image, and equivalently `b_q*G_(q-1)b_q=||p_q-chi||²`. The equality follows because the monic difference has degree at most q-1 and is orthogonal to Q_q. Also `d_(q-1)*G_(q-1)d_(q-1)=omega_(q-1)`. Substitution gives boxed (27) exactly.

**Recorded notation fix:** the prose immediately following (27) says `d_N=nu_0-omega_q`, but `d_N` was already defined as a vector and the scalar is indexed by q, not q-1. In a future integrated copy replace that prose with the displayed quadratic-form equality above. The archive is preserved; boxed (27) itself is correct. This was independently noticed by the companion owner as well.

For `x=exp(v_N), y=exp(v_(N+1))`, direct expansion gives

`(1-1/x)(y-1) = (xy-1)^2/(4xy) - (sqrt(y/x)-(sqrt(xy)+1/sqrt(xy))/2)^2`.

Nested least-norm sources give `x,y>=1`, so `R=xy>=1`; both squares discarded by (29) are nonnegative. Taking nonnegative square roots, applying the earlier `L<=epsilon`, and using monotonicity of sinh on nonnegative arguments gives (30). Summing over the indices `N_0,N_0+2,...` cancels the intermediate log volumes and produces exactly denominator `V_(N_0+2r-1)` and recurrence indices `N_0+2j+1` in (31).

## 5. Analytic input and scope

For `s=1/2+it`, Abel summation of the alternating zeta series gives the stated rough `O(1+|t|)` bound; `|1-2^(1-s)|>=sqrt(2)-1`. Squaring the factors of `s(s-1) Gamma(s/2) zeta(s)` gives power `4-1/2+2=11/2` and exponential `exp(-pi|t|/2)`, with `|h|^-2` supplying `-2 deg h`. The finite canceled zeros cause no singularity on the compact remainder. This establishes every required locally dominated differentiated moment on `|Re theta|<pi/2`.

The same vertical-strip decay gives a holomorphic inverse Mellin transform for `|arg z|<pi/4`; shifting to any fixed vertical line supplies rapid endpoint bounds on closed subsectors. Translating `y` by `i theta/2` in the plus-kernel Fourier transform contributes `exp(theta t/2)`, with the retained prefactor phase `exp(i theta/4)`. Plancherel uses the original `1/(2pi)` norm. Dagger reflection relates the two x-endpoint integrals on the same ray and gives the factor two. Expanding the two factors of the original `2 sum_n` theta seed gives factor eight before the incomplete-gamma integral; that integral contributes one half, yielding precisely factor four in (36).

No new arithmetic asymptotic conclusion follows merely from the scalar representation. The infinite theta source, full unit in eta, literal k-fold convolution mass, fixed quotient jets, higher-depth pullbacks, and the actual selected packet all remain where the note places them. This review has not reconstructed the entire earlier theta quotient from scratch or replayed Lean. It checked the newly used finite/source maps, the new analytic transform argument, and the explicit addition to the existing exterior theorem. It does not turn the synthetic checker fixtures into actual zeta packets. The seed numerical values were read and their script reviewed, not freshly recomputed or interval-certified here.

## 6. Independent check of the parent's four-loss join

Read `../PARENT_EXACT_JOIN.md` fully, SHA-256 `71e275a8543448e57bcfafc5ead8cf3c7f98d594ae994582d1180999d98c6370`.

Read the companion source definitions/E1-E18, including the complete E8 and Sylvester proofs. Its local file is byte-identical to the GitHub content at commit `161089942cce70a09fbe441d08ba4d36c1fd810c`, path `workbenches/splitzero-tandem/continuations/20260912-cyclic/tex/exterior_trace_equality_continuation.tex`, 27,394 bytes, SHA-256 `313c321537673bf629e10a673daaacd5d74d234efcaadee0210a8c56909a921e`, Git blob `ddbcde363d3b9785f1541b82946cf2d566f3ce60`.

For the original orthogonal positive spectral projector P, invariance gives `PH(1-P)=PA(1-P)=C_N`. With `M` the compression of P to the two nonzero H eigenlines, `0<=M<=I` and the two determinant remainders are nonnegative. The calculation

`||C_N||² = epsilon²(a+b-a²-b²+2|c|²)`

and `L=epsilon(a-b)` gives E8 by expansion. Adding it to Toda (28) cancels epsilon² and no other term. The four-loss equality in the parent's join and the stronger inequality retaining `L² + phase² + ||C_N||²` are correct on the same G_N. The notation C_N correctly avoids identifying this off-diagonal map with the u-coordinate operator T. The Sylvester inverse has the stated positive sign: integration of the derivative of `exp(-tB)Y exp(tD)` returns Y, and real spectral separation plus finite nilpotent factors removes its upper boundary. No uniform singular-value lower bound has been inserted. The `L>0` and endpoint exclusions are explicit.

## 7. Executed finite checks and actual failures

- The immutable source checker passed 24 methods normally and with `-O`, zero errors/failures. Both 25-method negative runs failed the single deliberate `1 != 2` sentinel. This is one sentinel in two modes, not two formula-mutating tests. Full fresh logs were read. Peak observed RSS was below 86 MB; execution was sequential.
- The independent checker imports no source checker. Four nonuniform seven-atom fixtures are built directly in original complex S-coordinates, total mass 58, including first admitted degree, repeated roots, and asymmetric phase. It checks full matrix curvature, both rank-one maps, the actual quotient derivative, determinant identity, positive-i phase, radius, and finite bound. It rejects both a reversed-i formula and omission of the phase square in each fixture: eight formula-negative controls per mode. Normal and optimized runs passed with identical JSON and logs, peaks below 87 MB.
- Its first reviewer-authored implementation was voluntarily stopped after about 153 seconds because unevaluated rational matrix expressions grew computationally expensive. No mathematical discrepancy was reported. Intermediate exact cancellation was added without changing any formula; bounded reruns took about 41 and 34 seconds. This stopped attempt is preserved in `INDEPENDENT_REPLAY_RECEIPT.json`; it is not hidden as a source failure or counted as a pass.
- The inherited exterior suite was not repeated: its separate D-stage terminal review already exists. This package's own inherited timeout statement remains historical source evidence, not a new failure.

## 8. Bounded literature routing

Read the current corpus entrypoint, D/topic_route.json, and topic-route schema. Executed exactly two read-only canonical research_literature queries with limit four: `Hankel Toda` and `Aptekarev Branquinho Marcellan`. The former returned four nearby routing hits, none adopted or content-read; the exact author query returned no hit. This does not establish global literature absence. No shelf scan or index rebuild followed.

For the classical formulas, freshly read the relevant [DLMF moment section](https://dlmf.nist.gov/18.2#ix), including 18.2.26-30 and the numerical-conditioning warning; freshly read [DLMF 5.11.9](https://dlmf.nist.gov/5.11#E9) for uniform bounded-real-part gamma decay. The independent proof above supplies the arithmetic specialization. This reviewer's ScienceDirect request returned an internal error; no paper proof is attributed to that failed read. The parent separately verified publisher abstract/metadata for DOI 10.1016/S0377-0427(96)00138-0; that remains parent-scoped context. The precise machine-readable routing/read boundaries are in `topic_route.json`.
