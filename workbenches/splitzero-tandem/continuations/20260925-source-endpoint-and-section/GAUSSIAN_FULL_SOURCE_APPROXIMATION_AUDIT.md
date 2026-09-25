# Independent audit of the full-source Gaussian approximation

25 September 2026. Bounded mathematical audit, **GAPA0–GAPA5**.

## GAPA0. Final version, complete coverage and result

The entire written proof [GAUSSIAN_FULL_SOURCE_APPROXIMATION.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/GAUSSIAN_FULL_SOURCE_APPROXIMATION.md), **GAP0–GAP9**, was read and independently checked. The reviewed final SHA256 is

`1cb89804a1ad3990c5eab65c89b2c6c748764461a012194867d2250318a04a0e`.

The mathematical audit passes. Every displayed formula and its stated domain, topology, sign and convergence assertion was checked. No mathematical correction remains in that version. This audit concerns the stated source approximation and its actual receiving maps; it does not add a weight-purity or RH conclusion.

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). The operators reviewed here act on the already reconstructed original arithmetic coefficients. The separate branch counters, the retraction of arithmetic on the support, the original zeta function and all source multiplicities remain in force.

## GAPA1. Independent calculations and source coverage

Before the draft was available, the strip estimate, original half-Mellin kernel, reflected adjoint-defect action, trace limit and the failure of a rapid-source limit for the extension generator were derived independently. The complete ECR0–ECR7 and ECI0–ECI13 source proofs were then read, with versions:

- [EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md), SHA256 `0a4e004a008422f622beeca7af8babc9a9f6527c0d4eb43571ea6443c0975250`.
- [EXTENSION_CLASS_INVOLUTION_INDEPENDENT.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/EXTENSION_CLASS_INVOLUTION_INDEPENDENT.md), SHA256 `ba951baf03f04edfeed66f98708e3c3ae5c6b2657b23b569cb108af4316aec31`.

The exact full-source action GMS9.1–GMS9.4 was reread from [CC_GLOBAL_MULTIPLIER_SEPARATION.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/sources/programme/cc_sheaf/CC_GLOBAL_MULTIPLIER_SEPARATION.md), including both chart restrictions, both source sections, all four endpoint coordinates and the degree-two action by \(h(s+1)\). AST2–AST6’s actual source quotient, topology and two boundary-sign conventions were checked against [ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md), final SHA256 `1b38252f2816901d49e87e212db102833c8d6ce5d7a90a655f62860d50b0c89e`.

A separate bounded independent calculation checked the source/quotient estimates and the full strong-dual bounded-convergence topology. It subsequently checked the written GAP1–GAP2 and GAP4–GAP6, including the \(H_\infty\) domain, the exact constant \(te\), and the trace exponent \(k\ge d+4\). These checks supplement the complete GAP0–GAP9 reading reported in GAPA0; they are not a claim that every reviewer read every prerequisite paper.

## GAPA2. Source estimates, quotients, generator and original kernel

For \(0<t\le1\), \(s=x+iy\), and \(|x|\le A\),
\[
g_t(s)-1=\int_0^t s^2e^{us^2}\,du,
\quad |s^2|=x^2+y^2,
\quad |e^{us^2}|\le e^{A^2}.
\]
This proves precisely
\[
b_{A,N}((g_t-1)F)
\le te^{A^2}(A^2+1)b_{A,N+2}(F).
\tag{GAPA2.1}
\]
The proof preserves each full jet ideal and each stated value kernel. Taking the infimum over representatives proves the identical quotient-seminorm estimate; it does not choose a continuous section. Restriction to an invariant closed subspace and then quotienting gives the stated subquotient result. The second integral remainder gives the exact \(t^2e^{A^2}(A^2+1)^2/2\) bound with seminorm index \(N+4\), so the full bounded-set generator statement is justified.

The original half-Mellin transform gives the source convolution factor \(1/2\):
\(\Theta(a*_Mb)=2\Theta(a)\Theta(b)\). For a separate direct check, put \(x=\log(u/v)\). The full kernel in GAP3.3 is
\[
K_t(x)=\frac{e^{t/4}}{2\sqrt{\pi t}}
e^{-x/2}\exp\!\left(-\frac{(x-t)^2}{4t}\right).
\]
Its moment is exactly
\[
\int_{\mathbb R}K_t(x)e^{sx}\,dx
=e^{t/4}\exp\!\left(t(s-1/2)+t(s-1/2)^2\right)
=e^{ts^2}.
\tag{GAPA2.2}
\]
The displayed prefactor, exponent shift and half-Mellin constant all contribute to that equality. Absolute Fubini is justified by the finite absolute moments of the original source. Logarithmic integration by parts has zero boundary terms and gives \(\Theta(u\partial_u)=-s\Theta\); its square gives the claimed positive generator \((u\partial_u)^2\). The full Gaussian jet matrix in GAP2.2, its determinant and all original multiplicities also check.

## GAPA3. Actual specialization, Hilbert topology and strong duals

The exact target multiplier of the actual adjoint-defect map is
\[
(G_t^\#y)_\rho=g_t(\rho^\#)y_\rho,
\qquad \beta_rm_{g_t}=G_t^\#\beta_r.
\tag{GAPA3.1}
\]
The reflected value is not conjugated or replaced by its modulus. Its Hilbert adjoint has diagonal \(\overline{g_t(\rho^\#)}\). This proves the Riesz/continuous-transpose identities in GAP5.2 with their original multiplicity weights.

On the full \(H\), dominated summation proves strong convergence, and the uniform bound \(\|G_t^\#\|\le e^t\) gives uniform convergence on compact sets. Unbounded actual zero heights show \(\|G_t^\#-1\|\ge1\); no Hilbert operator-norm convergence is being asserted. On the explicitly constructed common domain,
\[
p_N((G_t^\#-1)y)\le te\,p_{N+2}(y),
\tag{GAPA3.2}
\]
because \(|\rho^\#|^2\le(1+|\Im\rho|)^2\). Weighted evaluations prove that the entire original source and its specialization image reach this domain continuously. This is a whole-source statement, with no finite-block density assumption.

For the strong-dual claim, if \(K\subset X\) is bounded, then
\[
D_K=\bigcup_{0<t\le1}t^{-1}(T_t-1)K
\]
is bounded by the proved source estimates. Therefore, for every strongly bounded \(\Lambda\subset X'_\beta\),
\[
\sup_{\lambda\in\Lambda}p_K((T_t'-1)\lambda)
\le t\sup_{\lambda\in\Lambda}p_{D_K}(\lambda)\longrightarrow0.
\tag{GAPA3.3}
\]
This verifies both bounded dual inputs and every strong target seminorm. It requires neither an arbitrary algebraic dual nor an unproved dual-family lifting theorem.

The complexes in GAP4.5 occupy degrees \((-1,0)\). Their maps commute with the differential by (GAPA3.1). The positive differentiate-a-lift SES boundary is \(+\overline\beta_r\); the retained positive quotient and positive final cone projection give the distinguished-triangle stalk boundary \(-\overline\beta_r\), represented by \((a,-b_ra)\). GAP4 retains both conventions correctly and does not identify a whole derived morphism from its stalk value alone.

## GAPA4. Trace, reflection, normal degree and original factors

For a fixed polynomial-growth multiplier with \(|h(\rho^\#)|\le C_hw_\rho^d\), the exact difference is bounded by
\[
teC_h\sum_\rho m_\rho|F(\rho)|w_\rho^{d+2}.
\]
Taking \(k\ge d+4\) gives \(2(d+2-k)\le-4\). Cauchy–Schwarz therefore yields precisely GAP6.2 with
\(C_0^2=\sum_\rho m_\rho w_\rho^{-4}\). Weighted evaluation is continuous on the actual quotient, so this proves convergence in \(Q'_\beta\), uniformly on every bounded test set. It makes no topology claim on the cyclic class module. The exact functional identity behind the reflected comparison is
\[
\mathcal W_M(g_th)=m_{g_t^{\#_1}}'\mathcal W_M(h),
\quad g_t^{\#_1}=d_tg_t,
\quad d_t=e^{t(1-2s)}.
\tag{GAPA4.1}
\]
The inverse factor in ECI12’s dual involution remains \(d_t^{-1}\). The normal transported Gaussian \(e^{t(\lambda-1)^2}\) and its factor \(e^{t(3-2\lambda)}\) are distinct from the simultaneous normal-term action \(g_t(s+1)\). All these exact formulas pass.

The argument that \([g_t]\) has no limit in \(Q\) is valid: a limit would have value one at every actual zero, contrary to rapid strip decay along the unbounded actual divisor. No such assertion is transferred to the possibly zero off-line quotient. Convergence of the functional traces does not assert convergence of a bilinear trace tested against a second varying, potentially unbounded class \(b_t(k)\).

The GMS source sections give precisely the four endpoint multipliers \((1,e^t,e^t,1)\). The full original multiplier
\(s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/8\), its exceptional values, the complete derivative sum, the original functional-equation factor and the finite trivial-divisor scope of GAP8 all check. The separator acts as identity on the original specialization source and as zero only after the stated different normal coordinate transport. No arithmetic weight or vanishing conclusion is inferred from this approximation.

## GAPA5. Correction history and final receipt

The complete initial draft was read at SHA256
`31dbe732c53e454198d7fb5e38337293c744bd2b55c0fd77d18ee2db348c94c7`.
It had no mathematical defect. The review requested two notation clarifications: state degrees \((-1,0)\) explicitly after GAP4.5 and write the denominator in GAP8.1 as \(2\,k!\). Both were applied by the author and checked in the final file.

The exact content comparison was verified by reversing those two text changes and converting CRLF back to LF; the resulting UTF-8 SHA256 is exactly the initial draft hash above. Thus the final change consists of those two requested clarifications and line-ending conversion. The final verified hash is the one in GAPA0. No accepted source proof was edited by this audit.
