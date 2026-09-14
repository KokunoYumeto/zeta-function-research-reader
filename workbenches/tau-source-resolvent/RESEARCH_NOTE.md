# Exact source resolvents and certified input bounds

13 September 2026. Continuation of the original SplitZero programme on the verified PR29 source at `55f656ed738b8a33a777c58ff45005c0680afc20`. The original scalar, support reconstruction, quotient, arithmetic source, and full selected zero orders remain unchanged. This work adds finite proof interfaces; a counterexample to an auxiliary implication is not treated as a categorical verdict on the programme.

## Intake and source scope

The current GitHub main observed during intake is `820f83ef73d2c0938cb86a0c86a407d3aa3e1958`; it adds the R57 publication index to the earlier source snapshot. PR28 is merged. PR29 contains the completed original residue detection and signed metric transfer. Its mathematical note, handoff, new Lean files, runner, and workflow were read. The present contribution extends those actual definitions.

The newly attached `Tau_Marked_Product_Four_Endpoint_2026-09-13(1).zip` could not be opened: both container-backed execution interfaces timed out and the file reader returned no readable archive text. No archive manifest, member, or supplied test is claimed as inspected or replayed. The work below is based on the published sources, not an inferred reconstruction of that attachment. When the archive is accessible, its actual content must be reconciled before any assertion that it has been integrated.

The source-path derivative formulas in PR29 and the earlier AV/AC notes keep their attribution and written-proof scope. The general linear-algebra mechanisms used below are standard Schur/resolvent and logarithm-series arguments; no priority is claimed for those general principles.

## 1. Exact finite source perturbation

Fix the original polynomial presentation, with q-dimensional coefficient quotient:

\[
0\longrightarrow\mathcal P_{N-q}\xrightarrow{B=\times\chi}\mathcal P_N
\xrightarrow{J}E\longrightarrow0.
\]

The columns C lift the specified quotient basis. No replacement of the original arithmetic Taylor unit is implicit in these coordinates. It remains in the subsequent realization of E. Let M_0,M_1 be positive Hermitian forms on the SAME source, and keep

\[
Q_a=B^*M_aB,\quad H_a=Q_a^{-1},\quad Z_a=H_aB^*M_aC,
\quad R_a=C-BZ_a,\quad G_a=R_a^*M_aR_a.
\]

The empty relation space at N=q-1 is allowed. Its matrices have size zero and the identities use their ordinary empty conventions; no degree below the first admissible one is inverted.

Put E_M=M_1-M_0 and define the actual cross block and its solved relation coefficient:

\[
X_{01}=B^*E_MR_0,\qquad U_{01}=H_1X_{01}.
\]

Then

\[
\boxed{U_{01}=Z_1-Z_0,\qquad R_1=R_0-BU_{01}.}
\]

Proof: orthogonality B*M_0R_0=0 gives X_01=B*M_1R_0. Substituting R_0=C-BZ_0 and using H_1Q_1=1 gives U_01=Z_1-Z_0. This computes the primitive from the source perturbation instead of presuming it from equal finite observations.

The full quotient perturbation is

\[
\boxed{G_1=G_0+R_0^*E_MR_0-X_{01}^*H_1X_{01}.}
\]

The final term is exactly

\[
\boxed{X_{01}^*H_1X_{01}=(BU_{01})^*M_1(BU_{01})\succeq0.}
\]

Proof: Q_1H_1=1 and the Hermiticity of H_1 identify the two expressions. The inherited canonical Pythagoras identity applied to R_0=R_1+BU_01 then gives the quotient formula. All conjugate cross terms have been accounted for; no commutation of the forms or Grams is assumed.

There is also an exact rigidity test:

\[
R_1=R_0\quad\Longleftrightarrow\quad B^*(M_1-M_0)R_0=0.
\]

The forward direction uses both normal equations; the reverse direction uses the solved primitive. It does not imply G_1=G_0, because even an unchanged representative can receive a different norm.

For three source forms the coefficients satisfy

\[
U_{02}=U_{01}+U_{12}.
\]

This follows from their literal Z-differences and is compatible with transporting the same relation through each source comparison.

The exact new statements above are the targets of `SplitZeroMetricResolvent`. The source quotient and primitive cocycle are connected in `SplitZeroMetricResolventSupport`.

## 2. The original quotient and action remain attached

Every observation J annihilating the original columns B still has JR_1=JR_0=JC. More importantly, R_1-R_0=-BU_01 is an actual original relation, not just a vector in a possibly larger finite observation kernel.

For the specified source-coordinate equivalence into an original support fibre, the inherited `Relations.quotientDiagram` therefore identifies these two representatives. The new theorem `perturbation_supported_zero` proves that their difference maps to the receiving fibre zero and is not external absence when that support is nonbottom. The source generator comparison changes by

\[
(DR_1-R_1A)-(DR_0-R_0A)=-D(BU_{01})+(BU_{01})A.
\]

No assertion says D preserves the finite admitted relation degree. Where it raises the degree, its receiving relation layer and primitive must be supplied using the original shift map. The already established two-error formula for support transport remains an input; neither source-section naturality nor residue naturality is newly presumed.

## 3. A local sensitivity bound using only the relevant source blocks (written proof)

This is a further mathematical consequence of the exact resolvent. It is not an additional named Lean theorem in this push.

Use the original M_0-orthogonal frame formed by R_0 and B. Define

\[
T=Q_0^{-1/2}B^*E_MB Q_0^{-1/2},
\quad X=Q_0^{-1/2}B^*E_MR_0G_0^{-1/2},
\quad Y=G_0^{-1/2}R_0^*E_MR_0G_0^{-1/2}.
\]

These square roots specify a comparison for estimates, not a replacement of the original metric. The exact equation becomes

\[
\boxed{G_0^{-1/2}G_1G_0^{-1/2}=I+Y-X^*(I+T)^{-1}X.}
\]

If ||T||<=r<1 in the stated Euclidean operator norm of this comparison, functional calculus gives

\[
\frac1{1+r}I\preceq(I+T)^{-1}\preceq\frac1{1-r}I.
\]

Congruence by X yields

\[
I+Y-\frac{X^*X}{1-r}\preceq G_0^{-1/2}G_1G_0^{-1/2}
\preceq I+Y-\frac{X^*X}{1+r}.
\]

Put eta=||Y||+||X||^2/(1-r). If eta<1, the entire comparison is positive definite. Set Z=Y-X*(I+T)^(-1)X, retaining the displayed adjoint on the first X. The eigenvalues of Z are in [-eta,eta]. The scalar inequalities

\[
z-\frac{z^2}{2(1-\eta)}\le\log(1+z)\le z
\]

follow by bounding the tail of the logarithm power series absolutely. Summation, the trace bounds on X*(I+T)^(-1)X, and tr(Z^2)<=q eta^2 prove

\[
\boxed{\operatorname{tr}Y-\frac{\operatorname{tr}(X^*X)}{1-r}
-\frac{q\eta^2}{2(1-\eta)}
\le\log\frac{\det G_1}{\det G_0}
\le\operatorname{tr}Y-\frac{\operatorname{tr}(X^*X)}{1+r}.}
\]

The boundary loss has not been turned into an unsigned error. In particular, when Y=0 and X is nonzero, the logarithmic change is strictly negative. Applying the actual arithmetic source requires proving its T,X,Y bounds; the formula alone assigns no arithmetic sign. For a signed four-endpoint contrast, combine lower bounds at subtracted endpoints and upper bounds at added endpoints in their original orientation.

## 4. Certified moments rather than exact input assumptions

For the original comparison matrices in PR29 retain

\[
A_N=(G_N^\Gamma)^{-1}G_N^{\rm ar},\quad T_N=\det A_N,
\quad H_N=I-A_N/c,
\]

where one common positive numerical c places all four loss spectra in [0,1). The c is not a change of source mass. The original positive weighted spectral witness remains explicit and is not replaced by Euclidean normality.

For one H, put s_m=Re tr(H^m). Suppose finite certified inputs lo_m,hi_m satisfy

\[
\underline s_m\le s_m\le\overline s_m\quad(1\le m\le2p),
\qquad p\ge1,\quad\overline s_p<1.
\]

Define DIRECT finite blocks

\[
L_p=\sum_{m=1}^{p}\frac{\underline s_m}{m},
\quad P_p^+=\sum_{m=1}^{p}\frac{\overline s_m}{m},
\quad T_p^+=\sum_{m=p+1}^{2p}\frac{\overline s_m}{m},
\quad U_p=P_p^++\frac{T_p^+}{1-\overline s_p}.
\]

Then

\[
\boxed{L_p\le-\log\det(I-H)\le U_p.}
\]

Proof: for x in [0,1), the scalar log remainder r_p(x) satisfies r_(2p)(x)<=x^p r_p(x). For every retained eigenvalue x_a, x_a^p<=s_p<=hi_p. Summing the corresponding scalar remainder inequalities gives

\[
-\log\det(I-H)\le P_p+\frac{P_{2p}-P_p}{1-\overline s_p}.
\]

The finite prefix and tail are bounded termwise by the stated inputs, with their positive denominators. The lower bound follows from the nonnegative scalar log tail and the lower prefix data. This is exactly what `spectral_interval` and `matrix_interval` prove using the inherited Mathlib logarithm-series theorem and the original two-sided spectral coordinate maps.

The tail MUST be enclosed as its own sum. Subtracting two upper prefix estimates gives no valid upper estimate for their difference. No input is accepted when the upper stopping moment reaches or exceeds one.

For endpoints i0,i1,j0,j1 in the original order, all q log c terms cancel before applying intervals. Consequently

\[
\boxed{L_{j0}+L_{j1}-U_{i0}-U_{i1}
\le\log\frac{T_{i0}T_{i1}}{T_{j0}T_{j1}}
\le U_{j0}+U_{j1}-L_{i0}-L_{i1}.}
\]

The fully composed statement and its negative-upper-bound consequence are Lean targets. Each endpoint can use its own stopping order. This is a certificate for the signed correction, not four unrelated absolute-value bounds.

## 5. Supplying trace enclosures from entry or operator errors (written proof)

For a fixed coordinate matrix, suppose ||H-Hhat||<=d and ||H||,||Hhat||<=R in the specified Euclidean operator norm. Noncommutative telescoping gives

\[
H^m-Hhat^m=\sum_{a=0}^{m-1}H^a(H-Hhat)Hhat^{m-1-a}.
\]

Therefore

\[
|\operatorname{Re}\operatorname{tr}(H^m)-\operatorname{Re}\operatorname{tr}(Hhat^m)|
\le q\,m R^{m-1}d.
\]

The trace inequality is immediate in an orthonormal coordinate basis: each diagonal coefficient has modulus at most the operator norm. The estimate holds for nonnormal matrices and does not silently identify the coordinate norm with the arithmetic metric. Certified entry errors imply a Frobenius error bound, which in turn bounds the operator norm. Error in the matrix multiplications used to compute Hhat^m must also be added when they are not exact.

The elementary interval implication |approx-actual|<=error gives approx-error<=actual<=approx+error; `error_bounds` proves that implication. The power-error estimate and the analytic certification of original moment entries remain written/external inputs. Large p can amplify errors; fixed-matrix termination with exact data is not a guarantee that a fixed numerical precision will terminate.

## 6. Scope and verification

The workflow reuses PR29's fail-closed audit and exact source-closure preparation, strictly recompiles its inherited 35-file closure, then compiles the three additional files and a joint import. It prints the 24 selected new transitive reports. Actual success and the exact source commit are recorded only after observing completion; development scripts and this note do not confer a certificate by themselves.

The independent finite regression suite uses the original-style complex S=1/2+ix polynomial coordinates and a Gaussian of literal mass seven, with specified positive polynomial changes of its density. It checks canonical sections, original polynomial relations, exact cross-block losses, cocycles, noncommuting Grams, repeated roots, the first admissible degree, full generator defects, and signed logarithm intervals with deliberately non-exact bounded trace inputs. A rational atanh-series enclosure independently brackets the fixture logarithms. These are declared calibration measures, not actual zeta-zero packets or arithmetic quadrature certificates.

Both Python modes and explicit false-formula controls are retained. The inherited tests and original derived audit retain their recorded scopes. Main, original files, reference archives, and other branch refs are not to be rewritten by this continuation.

The outstanding arithmetic input is a uniform estimate on the actual signed four-endpoint quantity or its source cross blocks. The new results supply exact propagation and finite validation interfaces; they do not assert that generic positivity or auxiliary purity proves that estimate.

## References

Boyd, S., & Vandenberghe, L. (2004). *Convex optimization*. Cambridge University Press. Background for Schur-complement and matrix-fractional identities; not a source for the programme's arithmetic hypotheses.

The Mathlib Community. (2026). *Mathlib*, pinned revision `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. The inherited logarithm-series, finite sums, matrix inverse, and positivity theorems are reused under the repository's Lean 4.31.0 pin.

Original programme sources: PR29 at the source pin above; `SplitZeroMetricVariation`, `SplitZeroArithmeticLogTransfer`, `SplitZeroMetricVariationSupport`, and their AV/AC source-path dependencies. No mathematical content is inferred from the unread newly supplied archive.
