# Independent review of the paired sum-connection calibration

Date: 2026-09-12. Reviewer: `paired_checker_review`, independently of the checker author.

## Scope and result

I read the complete checker `scripts/check_sum_connection_stieltjes.py`, the complete contemporaneous `tex/sum_connection_stieltjes.tex`, and all records in `checks/sum_connection_stieltjes.json`. The mathematical approval here concerns FC.1–20 and the specified finite calibrations only. The later arithmetic strictness and finite normal-image reconstruction subsections are outside this bounded review's proof certification.

No mathematical defect was found in FC.1–20 or in the finite original-derivative comparisons. One fixture-domain defect was reported and repaired by the author: the variable-frame test originally used a negative original sample coordinate as the paired radius. The paired coordinate requires the positive square root. The revised test uses its absolute value and a positive fallback at zero. The original negative-coordinate gauge test is still retained independently. Two literal TeX spacing typos in the later FC.31/FC.36 displays were also reported to the owner; no TeX was edited by this reviewer.

## Original frame and independence of the comparison

The original maps have their literal four-by-two matrices

\[
j(u)=\begin{pmatrix}1&0\\0&1\\a(u)&a(u)\\b(u)&2b(u)\end{pmatrix},
\]

with `(a,b)=(1+u,1+u²)` in the non-even example and `(1+u²,1+u⁴)` in the even example. The first two rows make each map injective at every real coordinate. With `r=(1,1)^T`, `s=(1,2)^T`, the complete original weight and mixed derivative are

\[
W=I+a^2rr^T+b^2ss^T,
\qquad B=aa'rr^T+bb'ss^T=W'/2.
\]

Thus the fixed-frame identity is proved here without presuming that a general real matrix frame has it. The two rank-one matrices do not commute: `r^Ts=3`, and `rr^Tss^T=3rs^T`, whereas `ss^Trr^T=3sr^T`. At `u=0` both coefficients are one. At `u=2` their squared values are `(9,25)` or `(25,289)`, respectively, so the commutator of the two sampled weights is nonzero. The non-even example retains the odd term in `(1+u)²`.

For each specified coefficient polynomial the checker forms `c(u)=f(center+i u)` directly. It computes the original derivative as `j'(u)c(u)+j(u)c'(u)` by differentiating those original polynomials. Its energy is the original ambient Euclidean squared norm of that four-vector on both branches. This quantity is compared with the independently assembled paired connection and normal Gram. It is not defined by rearranging the proposed paired energy identity. The tests use three centers, five positive radii, complex coefficients, two noncommuting frame families, and the full normal term. The rational sample equalities calibrate these stated finite examples; the general identity is supplied by the FC.14–16 proof, not by interpolation from samples.

The independent signed chain rule is also checked before energy formation. In branch coordinates `F=(c(v),c(-v))^T`, with `v>0`, it is

\[
\binom{c'(v)}{c'(-v)}
=\operatorname{diag}(2vI,-2vI)\partial_x F.
\]

The original coefficient covariant derivative is obtained by adding the original matrices `Γ(±v)c(±v)` to these separately differentiated values. Its comparison with `J(∂x+A)q` is consequently independent of the energy comparison.

## Density, connection and gauge constants

The checker retains both original weights in

\[
D=\frac{\operatorname{diag}(W(v),W(-v))}{2v},
\quad M=\begin{pmatrix}I&ivI\\I&-ivI\end{pmatrix},
\quad H=M^*DM.
\]

The factor `1/(2v)` is the measure Jacobian on each branch. Its derivative is `-1/(4v³)`, so differentiation of the full density gives

\[
\Gamma_b^*D+D\Gamma_b=D'+D/(2x).
\]

Here `Γ_b=diag(Γ(v)/(2v),-Γ(-v)/(2v))` uses the negative branch sign. The moving coefficient matrix contributes `M^{-1}M'=diag(0,I/(2x))`. Substitution proves the exact drift `A*H+HA=H'+H/(2x)` and the compatible shifted connection `A-I/(4x)`. The checker tests each term against the differentiated full density and rejects omission of the drift, the moving basis, the negative branch sign, or normal energy. The identity `J*HJ=4xH` keeps the same measure rather than changing it to a scalar reference weight.

For the variable complex frame `C(u)=[[1,u+i],[0,1]]`, the checker differentiates the changed original frame directly and obtains its own projection and normal map. It then compares these with the full transformation formulas. In particular it rejects `B^C=(W^C)'/2`: the connection's `C^{-1}C'` term is present. The repaired paired gauge checks use a positive radius. Gauge values at negative original `u` remain ordinary original-coordinate tests with no restriction on that coordinate.

## Gaussian-polynomial amplitude and unscaled mass

The complete calibration amplitude is `a(t)=t exp(-t²/2)`. Its mass is `μ=√π/2`, its Fisher integral is `I=3√π`, and `∫ a a'=0`. These are direct Gaussian integrals of `t²`, `(1-t²)²`, and the odd polynomial `t(1-t²)`.

For the original two-factor coordinates `t1=u/2+y`, `t2=u/2-y`, the full amplitude is

\[
\Psi=(u^2/4-y^2)e^{-u^2/4-y^2}.
\]

Consequently the polynomial multiplying its original `u` derivative is `∂u(u²/4-y²)-(u/2)(u²/4-y²)`. Integrating its square directly first in `y`, then in `u`, gives `μ I/8=3π/16`. This is exactly `μ^{k-1} I/(4k)` with `k=2`, including the original mass. The computed fibre mass is

\[
m(u)=\frac{\sqrt{\pi/2}}{16}(u^4-2u^2+3)e^{-u^2/2}.
\]

For `ρ(x)=m(√x)/√x`, differentiation gives

\[
\rho'+\rho/(2x)=m'(\sqrt{x})/(2x).
\]

It follows directly that `4x |ρ'+ρ/(2x)|²/ρ` equals `(m'^2/m)(√x)/√x`. The checker verifies this exact density equality, and separately rejects removal of the mass or the radial drift. It does not claim that the Gaussian-polynomial density is the arithmetic theta density.

## Exact endpoint-domain witness

The witness takes `c(v)=e^{-v}e1` and `c(-v)=2e^{-v}e1` in the non-even original frame. Its paired coefficients are

\[
q(x)=e^{-\sqrt{x}}\binom{(3/2)e_1}{i e_1/(2\sqrt{x})}.
\]

The two original branches have finite total squared norm `27/2` and finite open-branch derivative energy `9`; the checker obtains these values by exact exponential polynomial moments, with the full original frame retained. Their vector traces differ by

\[
j(0)e_1-2j(0)e_1=(-1,0,-1,-1)^T.
\]

Thus the distributional derivative of the joined original vector contains this nonzero coefficient times `δ0`. Its presence precludes an `L²` weak derivative, even though each open branch has finite derivative energy. The paired coefficient traces are `e1` and `2e1`, exactly as FC.18 requires them to be compared. The singular `b` component is allowed by the open-branch norms and therefore provides an effective witness that the joining condition is necessary.

For sufficiency, the FC.18 argument uses the locally bounded smooth inverse of the positive original weight, together with the bounded local original connection. Finite norm and covariant derivative energy therefore imply ordinary `H¹` control separately up to zero. Equality of the coefficient traces removes the unique jump distribution, yielding the original locally absolutely continuous coefficient and its global `L²` weak derivative. Both directions preserve the original `j(u)` and its derivative energy.

## Receipt scope

The initial inspected normal receipt passed all 847 records: 829 exact equalities or positivity facts and 18 negative controls. The positive-radius repair changes a fixture's domain but does not change the stated mathematical results or record count. I then read and checked all four repaired receipts: their embedded checker hashes equal the current script hash, record counts equal actual record-array lengths, and all record names are unique. Both ordinary modes have 847 passing records and zero false records. Both injected-failure modes have the same 847 successful records followed by precisely one false record, named `deliberate_failure/missing_signed_branch`; they report that exact `ArithmeticError`.

The reviewed repaired checker SHA256 is `c6c49731c2354068a4f8367d048d6f5ff32842f5da84d871747119563fdb8b6f`. The contemporaneous complete TeX read had SHA256 `ff30e49f3d33df24fbacbd4504ede5e82bff251d248cccb4d594905e26a97b45`; the mathematical approval remains scoped to FC.1–20 as stated above.

| Receipt in `checks/` | Outcome | SHA256 |
|---|---|---|
| `sum_connection_stieltjes.json` | 847 pass | `713412417dce24164768fe277b60683b151b25bf0c80a9f07bcf05a6d1677e76` |
| `sum_connection_stieltjes_optimized.json` | 847 pass | `97abb85a713e88a73bf36892a6f64cdefb22b8a593501e7d5e6bed49aeeac398` |
| `sum_connection_stieltjes_negative.json` | 847 pass, one deliberate failure | `584ed139e44acd318539d591d03da13ed00c6be1a23784562a6ba666e7b0c259` |
| `sum_connection_stieltjes_negative_optimized.json` | 847 pass, one deliberate failure | `34cb353725ca470d5f5f7836e523a41ee131f14dbbac49863e98845512ec65a7` |

The finite checker contains no Python `assert`, so the optimized receipts exercise its actual rejection mechanism as well. This reviewer has not substituted those finite checks for the complete FC.1–20 proofs and makes no arithmetic asymptotic or RH claim. The repaired calibration is approved within this exact scope.
