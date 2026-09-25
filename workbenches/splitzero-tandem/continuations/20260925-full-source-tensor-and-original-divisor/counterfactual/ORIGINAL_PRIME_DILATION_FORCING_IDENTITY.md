# Exact original prime dilation and its summation-image return

25 September 2026. Complete derivation OPD1–OPD6. All operations concern the original complex coefficient spaces \(S,A,J,Q\). Primitive \(Z_1/\tau\) has no addition, parity or numerical weight. The source \(Z_0,Z_1,Z_2\) data are retained.

The inputs are the original Connes–Consani summation map \(\Sigma h(u)=2\sum_{n\ge1}h(nu)\), the closed original image \(J=\Sigma S\), and the canonical functions constructed in [HSW5–HSW6B](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/ORIGINAL_ZETA_HARMONIC_SWEEP_AND_OFFCRITICAL_DEFECT.md). Human sources for the coefficient construction are [Alain Connes and Caterina Consani, 0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), and [Ralf Meyer, math/0412277v3](https://arxiv.org/abs/math/0412277v3). The harmonic trace mechanism is [Alain Connes, math/9811068v1, §VIII](https://arxiv.org/abs/math/9811068v1). The numerical weight-separation target comes from [Pierre Deligne, *La conjecture de Weil. II*, §3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/); no purity theorem from that setting is assumed here.

## OPD1. The fully specified original representative

Keep

\[
h_0(v)=\frac{\log|v|-2}{8\sqrt\pi}
\exp\!\left(-\frac{(\log|v|)^2}{4}\right)\ (v\ne0),
\quad h_0(0)=0,\quad b_0=\Sigma h_0,
\]

\[
G(s)=M_0b_0(s)=2\zeta(s)\frac{s-1}{2}e^{s^2},
\quad G(0)=\tfrac12,\quad G(1)=\exp(1).
\tag{OPD1.1}
\]

HSW5 proves that \(h_0\in S\), with both original endpoint conditions, and \(b_0\in J\). For each actual nontrivial zero \(\rho=\beta+i\gamma\), including its actual multiplicity, HSW6B constructs

\[
b_\rho(u)=u^{-\rho}\int_u^\infty v^{\rho-1}b_0(v)\,dv
=-u^{-\rho}\int_0^u v^{\rho-1}b_0(v)\,dv\in A,
\]

\[
(L-\rho)b_\rho=b_0,\qquad
L=-u\partial_u,\qquad M_0b_\rho(s)=\frac{G(s)}{s-\rho}.
\tag{OPD1.2}
\]

Both endpoint formulas are retained. Their equality is exactly \(G(\rho)=0\). This is a canonical representative for the stated \(b_0\), not a choice of norm on its quotient class. The full primary coefficient and all multiplicities remain those in HSW6B.4 and the complete jet calculations FGR1–FGR6.

## OPD2. Every positive dilation has an explicit source return

Define \(T_ab(u)=b(u/a)\), and the identical dilation on the real argument of \(h\in S\). Both are continuous on the original Fréchet spaces, and direct substitution in the sum proves \(T_a\Sigma=\Sigma T_a\). The map \(t\mapsto T_{\exp t}b\) is differentiable in every defining seminorm, with derivative \(T_{\exp t}Lb\): on each bounded \(t\)-interval the chain rule and the mean-value integral are controlled by one higher Euler derivative and fixed exponential bounds.

For \(a>0\), define the following exact, oriented integrals; an upper limit \(\log a<0\) means minus the integral with its bounds exchanged:

\[
R_{a,\rho}=\int_0^{\log a} a^\rho e^{-\rho t}T_{\exp t}b_0\,dt,
\qquad
h_{a,\rho}=\int_0^{\log a} a^\rho e^{-\rho t}T_{\exp t}h_0\,dt.
\tag{OPD2.1}
\]

These are convergent Fréchet integrals on a compact parameter interval. More explicitly, each Schwartz seminorm of the integrand for \(h_{a,\rho}\) is bounded uniformly on that interval by a finite constant times a seminorm of \(h_0\). Its evenness and value at zero are unchanged. Also
\(\int_{\mathbb R}T_{\exp t}h_0(v)dv=\exp(t)\int h_0=0\).
Thus \(h_{a,\rho}\in S\). Continuity and the exact summation intertwining give

\[
R_{a,\rho}=\Sigma h_{a,\rho}\in J.
\tag{OPD2.2}
\]

This supplies the full original-source preimage, including the factor two in \(\Sigma\).

Differentiate \(e^{-\rho t}T_{\exp t}b_\rho\) using OPD1.2. Its derivative is \(e^{-\rho t}T_{\exp t}b_0\). The fundamental theorem of calculus in every defining seminorm yields

\[
\boxed{T_ab_\rho=a^\rho b_\rho+R_{a,\rho}.}
\tag{OPD2.3}
\]

For each rational prime, use \(a=p\). On the actual quotient \(Q=A/J\), the source return vanishes, giving the exact eigenvector action \(T_p[b_\rho]=p^\rho[b_\rho]\). On the original representative the entire term OPD2.1 remains.

The cocycle relation, with no suppressed power, is

\[
R_{ab,\rho}=b^\rho R_{a,\rho}+T_aR_{b,\rho}
=a^\rho R_{b,\rho}+T_bR_{a,\rho}.
\tag{OPD2.4}
\]

To prove it apply \(T_aT_b=T_{ab}\) to OPD2.3 twice and compare the coefficient of \((ab)^\rho b_\rho\). Commutativity of the original dilations gives the second expression. This is an exact relation for all positive dilations, not only for finitely many primes.

The return itself has the complete original Mellin formula

\[
M_0R_{a,\rho}(s)=G(s)\frac{a^s-a^\rho}{s-\rho}.
\tag{OPD2.5}
\]

The quotient has removable value \(a^\rho\log a\) at \(s=\rho\). To prove it, apply the continuous Mellin functional to OPD2.1 and integrate \(a^\rho\exp((s-\rho)t)\) over its actual oriented bounds. At \(s=\rho\), integrate the constant directly. In particular the full endpoint values are

\[
M_0R_{a,\rho}(0)=\frac{a^\rho-1}{2\rho},\qquad
M_0R_{a,\rho}(1)=\exp(1)\frac{a-a^\rho}{1-\rho}.
\tag{OPD2.6}
\]

For every \(a\ne1\), the entire multiplier in OPD2.5 is not the zero function. Since \(G\) is also not the zero function, their product is nonzero by the identity theorem. Hence \(R_{a,\rho}\ne0\) for every nonidentity dilation, including when \(\rho\) is on the critical line. The original quotient class is zero by its explicit preimage OPD2.2; the function is not zero.

## OPD3. The complete finite-dilation norm identity

All functions in OPD2 belong to \(A\subset L^2(\mathbb R_{>0},du)\). Use
\(\langle f,g\rangle=\int_0^\infty\overline{f(u)}g(u)du\).
Substitution \(u=av\) gives

\[
\|T_af\|_{L^2(du)}^2=a\|f\|_{L^2(du)}^2.
\tag{OPD3.1}
\]

Expanding the squared norm of the full OPD2.3, keeping its complex scalar and its cross term, proves

\[
\boxed{
(a-a^{2\beta})\|b_\rho\|_{L^2(du)}^2
=2\Re\!\left(a^{\bar\rho}\langle b_\rho,R_{a,\rho}\rangle\right)
 +\|R_{a,\rho}\|_{L^2(du)}^2.}
\tag{OPD3.2}
\]

This applies simultaneously to every prime \(p\). The equality uses the original Hilbert measure, every forcing coefficient, and the actual source return. Although \(R_{a,\rho}\) is zero in \(Q\), its Hilbert norm and its cross term cannot be set to zero in OPD3.2. That Hilbert norm has not descended to \(Q\).

Indeed, \(J\) is dense in ordinary \(L^2(du)\), as proved in ASD10 and WHR. The complete short argument with the present generator is also in HSW6B: under \(f(u)\mapsto e^{x/2}f(e^x)\), the dilates of \(b_0\) become scalar multiples of all translations; their Fourier transform \(G(1/2+it)\) is nonzero almost everywhere. Orthogonality to every translation forces the Fourier product to be zero, and then forces the orthogonal vector to be zero. Thus replacing the original norm by its quotient seminorm would give zero on every class. OPD3.2 deliberately keeps the actual representative and its exact return instead.

## OPD4. Infinitesimal weight displacement as an original-source pairing

For \(b\in A\), the function \(u|b(u)|^2\) vanishes at both endpoints. Integration by parts gives the exact identity

\[
2\Re\langle b,Lb\rangle
=-\int_0^\infty u\partial_u|b(u)|^2du
=\int_0^\infty|b(u)|^2du.
\tag{OPD4.1}
\]

The boundary values vanish by the defining decay of \(A\); no boundary value is merely omitted. Insert the actual differential equation OPD1.2 to obtain

\[
\boxed{(\beta-\tfrac12)\|b_\rho\|_{L^2(du)}^2
=-\Re\langle b_\rho,b_0\rangle.}
\tag{OPD4.2}
\]

The same equality follows by differentiating OPD3.2 at \(a=1\), because the derivative of the source return there is \(b_0\). The direct proof OPD4.1 establishes every domain and endpoint condition independently.

Since \(b_\rho\ne0\), its norm is strictly positive. Consequently the critical-line condition for this actual zero is exactly vanishing of this real source pairing. No orthogonality to all of \(J\) has been postulated. The latter would be incompatible with this nonzero representative because \(J\) is dense.

## OPD5. The whole harmonic defect as a noncancelling source interaction

HSW6B.7 and OPD4.2 combine, with their established absolute convergence, to give

\[
\boxed{
\mathcal H_{\rm off}(b_\dagger)
=2\sum_{\rho\in\mathscr Z}m_\rho
 \left|\Re\langle b_\rho,b_0\rangle\right|.}
\tag{OPD5.1}
\]

This is an identity on the full actual zero divisor. Critical zeros contribute zero, while every original multiplicity remains. The two-sided constants in HSW6A give the same complete upper and lower bounds on this expression by \(S_{\rm off}\). Thus the global harmonic discrepancy has a precise expression in terms of the original summation-image source and its canonical resolvent representatives.

Reflection also gives an exact caution about signed cancellation. Let \(\rho^\flat=1-\bar\rho\) be the horizontal partner. For \(s=1/2+it\),

\[
|s-\rho|^2=(t-\gamma)^2+(\beta-1/2)^2
=|s-\rho^\flat|^2.
\]

HSW6B.5 and \(M_0b_\rho=G/(s-\rho)\) therefore prove

\[
\|b_{\rho^\flat}\|_{L^2(du)}^2=\|b_\rho\|_{L^2(du)}^2,
\qquad
\Re\langle b_{\rho^\flat},b_0\rangle
=-\Re\langle b_\rho,b_0\rangle.
\tag{OPD5.2}
\]

For a critical zero the same statement reduces to zero real pairing. Since OPD5.1 proves absolute summability, pairing the full signed sum is legitimate and yields

\[
\sum_{\rho\in\mathscr Z}m_\rho\Re\langle b_\rho,b_0\rangle=0.
\tag{OPD5.3}
\]

Equation OPD5.3 is therefore compatible with a nonzero unsigned defect. The operation preserving the complete obstruction is the absolute-value sum OPD5.1, not the reflected signed cancellation. This is proved using the same original function and representatives throughout.

## OPD6. Relation to the actual lifting target

The construction computes the full prime return before quotienting and an exact global measure of its possible off-critical contribution. It neither assigns numerical weight to primitive tau nor changes the prime spectrum. It shows precisely how the Hilbert dilation character \(a\) and the original quotient eigenvalue \(a^\rho\) coexist: the source return in OPD2.1 supplies every cross term in OPD3.2.

The next source calculation can now act on the explicit family \(h_{a,\rho}\), or on the full pairing OPD5.1, in the actual closed-support lifting diagram. The target cannot be vanishing of the raw function \(R_{a,\rho}\): OPD2.5 proves it is nonzero even at critical zeros. The exact scalar needed in OPD4 is \(\Re\langle b_\rho,b_0\rangle\), and OPD5 constructs its full noncancelling global sum. The closed-support comparison in the accompanying continuation calculates the actual connecting morphisms with all endpoint/extra terms; the next comparison must connect those morphisms to this calculated scalar. The present identity does not substitute Hilbert quotienting or reflection cancellation for Deligne's derived separation of weights.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
