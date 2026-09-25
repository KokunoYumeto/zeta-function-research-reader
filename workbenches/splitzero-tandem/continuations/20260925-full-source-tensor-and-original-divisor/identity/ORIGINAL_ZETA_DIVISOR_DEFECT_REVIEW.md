# Independent verification of the original-zeta divisor receiver

25 September 2026. Complete independent mathematical review, **OZR0–OZR10**.

## OZR0. Exact object, reading coverage and verdict

The entire proof [ORIGINAL_ZETA_DIVISOR_DEFECT_RECEIVER.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/identity/ORIGINAL_ZETA_DIVISOR_DEFECT_RECEIVER.md), OZD0–OZD8, was read and checked. The reviewed SHA256 is `99db537dc218c77468e315c77bf2dfa393cfcf895559bea932e1cacab3b8dc25`.

For the exact programme interfaces the review also read GTAH0 and GTAH4–GTAH6 in [GEOMETRIC_TRANSFER_POSITIVE_ADJOINT_DEFECT.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/geometric-positive-quotient/GEOMETRIC_TRANSFER_POSITIVE_ADJOINT_DEFECT.md), AST0–AST2 in [ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md), GAP0 and GAP4 in [GAUSSIAN_FULL_SOURCE_APPROXIMATION.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/identity/GAUSSIAN_FULL_SOURCE_APPROXIMATION.md), and ADM1 in [ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/identity/ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md). These scoped readings are not claims to have reread every part of those dependencies. Their respective whole-file SHA256 values are:

- GTAH: `dd27d0022c6cc0b82fc0cabcc5d43aed84d18fe762f382ba3be16e2fa50dc739`.
- AST: `1b38252f2816901d49e87e212db102833c8d6ce5d7a90a655f62860d50b0c89e`.
- GAP: `1cb89804a1ad3990c5eab65c89b2c6c748764461a012194867d2250318a04a0e`.
- ADM: `cefa50caadcb598df0936191e98a1a6beaf1495d932d86527cca110519b9db7e`.

**Verdict:** every stated mathematical identity and implication in OZD0–OZD8 passes this review. No mathematical correction is required. The review supplies below a proved extension of the test domain from Gaussian decay to decay of any fixed power strictly greater than one. This is an additional consequence, not a replacement of the actual source Gaussian or a claim of boundary vanishing.

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Arithmetic operations below are on the reconstructed coefficient system. The review supplies no addition, coordinate, parity or metric on that support. In particular none of the scalar reflection calculations changes the user's information-layer notation.

## OZR1. The source boundary and its positive coefficient

Use precisely the existing weighted value space
\[
H=\ell^2(\mathscr Z,m),\qquad
\langle x,y\rangle=\sum_\rho m_\rho x_\rho\overline{y_\rho},
\quad (Jx)_\rho=x_{\rho^\#},\quad \rho^\#=1-\overline\rho.
\]
The involution preserves multiplicities, hence \(J^*=J=J^{-1}\). To make the operator notation completely explicit, \(G_t\) means the bounded diagonal operator with coefficient \(g_t(\rho)=e^{t\rho^2}\). On \(0<\Re\rho<1\), \(\|G_t\|\le e^t\). The operator \(D_r\) is the bounded diagonal operator with the existing coefficient
\[
d_r(\rho)=e^{-i\gamma\log r}(r^\sigma-r^{1-\sigma}),\qquad r>1.
\]
Reflection changes this coefficient to its negative and leaves its squared modulus fixed:
\[
d_r(\rho^\#)=-d_r(\rho),\qquad
|d_r(\rho^\#)|^2=|d_r(\rho)|^2=q_r(\sigma).
\]
Consequently the actual product, before any trace is taken, is
\[
\begin{aligned}
(D_r^*JG_t)^*(D_r^*JG_t)
&=G_t^*JD_rD_r^*JG_t\\
&=G_t^*D_r^*D_rG_t.
\end{aligned}
\tag{OZR1.1}
\]
Its diagonal coefficient is exactly
\[
q_r(\sigma)|g_t(\rho)|^2
=(r^\sigma-r^{1-\sigma})^2e^{2t(\sigma^2-\gamma^2)}.
\tag{OZR1.2}
\]
Both the exponent and the reflection are therefore correct in OZD0. The identity is compatible with GAP4's distinct intertwining formula
\(\beta_rm_{g_t}=G_t^\#\beta_r\), where \(G_t^\#\) has coefficient \(g_t(\rho^\#)\). Moving the Gaussian through the boundary reflects its argument; computing the positive source-side product in (OZR1.1) produces the unreflected argument. These are the same operator calculation in the two displayed positions.

The divisor trace is \(\sum m_\rho a_{r,t}(\rho)\), not the ordinary operator trace \(\sum a_{r,t}(\rho)\). The distinction was already proved in GTAH5 and is preserved in OZD. Since \(q_r(\sigma)\le(r-1)^2\) and \(e^{2t\sigma^2}\le e^{2t}\), the complete zero count proves absolute convergence. For example the dyadic height shell \(2^j\le|\gamma|<2^{j+1}\) contributes at most
\[
C_{r,t}\,2^{j+1}(j+2)e^{-2t\,2^{2j}},
\]
whose series converges. Finitely many low zeros contribute a finite amount. No finite-height replacement is made.

## OZR2. Local divisor sign and original terms

With \(\Delta=\partial_x^2+\partial_y^2\) and \(dA=dx\,dy\), Green's identity on a punctured test-support domain gives
\[
\int \log|s-a|\Delta\psi\,dA
=\lim_{\varepsilon\downarrow0}\int_0^{2\pi}
\bigl[-\varepsilon\log\varepsilon\,\partial_r\psi(a+\varepsilon e^{i\theta})
+\psi(a+\varepsilon e^{i\theta})\bigr]d\theta
=2\pi\psi(a).
\tag{OZR2.1}
\]
The inward radial normal at the removed disk is the outward normal of the remaining domain. This fixes the positive sign of \(2\pi\delta_a\). Local integrability follows from \(\int_0^\varepsilon r|\log r|dr<\infty\).

For a meromorphic germ \((s-a)^ku(s)\), \(u\) nonvanishing holomorphic, the second term \(\log|u|\) is harmonic and contributes no divisor. Thus the exact original-zeta identity is
\[
\Delta\log|\zeta|
=2\pi\left(\sum_{\rho\in\mathscr Z}m_\rho\delta_\rho
+\sum_{k\ge1}\delta_{-2k}-\delta_1\right).
\tag{OZR2.2}
\]
The simple original pole has coefficient \(-1\); each simple trivial zero has coefficient \(+1\). No contribution at \(s=0\) belongs to this original divisor, because \(\zeta(0)=-1/2\). OZD1 retains these distinctions correctly.

## OZR3. Euler–Maclaurin and the global logarithmic estimate

For \(\Re s>1\), the counting-staircase integral is
\[
\zeta(s)=s\int_1^\infty\lfloor u\rfloor u^{-s-1}du.
\]
Writing \(\lfloor u\rfloor=u-\tfrac12-B_1(\{u\})\) gives
\[
\zeta(s)=\frac1{s-1}+\frac12-s\int_1^\infty B_1(\{u\})u^{-s-1}du.
\]
The first integration by parts contributes \(+B_2s/2!\) and the remainder \(-s(s+1)\int B_2(\{u\})u^{-s-2}du/2!\). Repeating retains the same negative remainder sign at every even stage and gives OZD2.2, namely
\[
\frac1{s-1}+\frac12+
\sum_{k=1}^{K_0}\frac{B_{2k}}{(2k)!}(s)_{2k-1}
-\frac{(s)_{2K_0}}{(2K_0)!}\int_1^\infty B_{2K_0}(\{u\})u^{-s-2K_0}du.
\tag{OZR3.1}
\]
The periodic Bernoulli function is bounded. For \(\Re s\ge a\) and \(a+2K_0>1\), the integral is bounded by \(\|B_{2K_0}(\{\cdot\})\|_\infty/(a+2K_0-1)\). Local uniform convergence also proves analytic continuation of this formula on \(\Re s>1-2K_0\). Multiplying by \(s-1\) removes its displayed pole for the purpose of the estimate and yields an entire function \(f(s)=(s-1)\zeta(s)\) with polynomial growth on each fixed vertical strip.

The reciprocal Dirichlet series at \(2+ij\) has absolute sum at most \(\zeta(2)\); hence
\[
|f(2+ij)|\ge\sqrt{1+j^2}/\zeta(2).
\tag{OZR3.2}
\]
For a fixed real interval \(K\), choose a fixed radius \(R_K\) large enough that the open disk \(D_j=D(2+ij,R_K)\) contains \(K\times[j,j+1]\). All these disks lie in one fixed vertical strip. Polynomial growth gives
\[
\int_{D_j}\log^+|f|\,dA\le C_K\log(|j|+2).
\]
The area submean inequality supplies
\[
\int_{D_j}\log|f|\,dA
\ge\pi R_K^2\log|f(2+ij)|\ge-\pi R_K^2\log\zeta(2).
\]
This inequality does not require an upper bound on the number or multiplicity of zeros in \(D_j\). Local logarithmic integrability follows from the local factorization already used above; circle means followed by radius integration prove the inequality. Subtracting yields the same logarithmic bound for the negative part. Finally \(\log|\zeta|=\log|f|-\log|s-1|\), and the absolute integral of the last term on these rectangles is \(O_K(\log(|j|+2))\), including its locally integrable singularity near \(1\). This proves OZD2.1 exactly.

For OZD's Gaussian tests, the terms
\[
\theta_R\Delta\phi,\qquad 2\theta_R'\partial_y\phi,
\qquad \theta_R''\phi
\]
are the full product-rule expansion. On \(R\le|y|\le2R\), the last two have respectively extra factors \(R^{-1}\) and \(R^{-2}\); the rectangle estimate and Gaussian decay force both pairings to zero. Dominated convergence applies to the first and to the original divisor sum. The proof therefore establishes the claimed global test domain, not merely a formal distribution identity applied to an inadmissible test.

## OZR4. Exact test Laplacian and endpoint receiver

Write \(h=\eta q_r\). Direct differentiation gives
\[
\partial_x^2(he^{2t(x^2-y^2)})
=e^{2t(x^2-y^2)}[h''+8txh'+(4t+16t^2x^2)h],
\]
\[
\partial_y^2(he^{2t(x^2-y^2)})
=e^{2t(x^2-y^2)}(-4t+16t^2y^2)h.
\]
The \(4t\) terms cancel, leaving precisely OZD3.3. Also
\[
q_r'=2(\log r)(r^{2x}-r^{2-2x}),\qquad
q_r''=4(\log r)^2(r^{2x}+r^{2-2x}),
\]
with every derivative of \(\eta\) retained in \(h'\) and \(h''\).

At a nontrivial zero the test equals \(q_r(\sigma)e^{2t(\sigma^2-\gamma^2)}\). At the pole it equals \((r-1)^2e^{2t}\). At the \(k\)-th trivial zero it equals \(\eta(-2k)q_r(-2k)e^{8tk^2}\). Substituting into (OZR2.2) and solving for the nontrivial-zero sum yields exactly OZD3.4, including the positive pole term and negative trivial-zero terms on its right side. The latter sum is finite because \(\eta\) is compactly supported. Subtraction for two cutoffs proves cutoff independence with those finite sums retained. A narrow cutoff makes these evaluations zero by support, without altering the original zeta function.

## OZR5. The complete-factor comparison

The exact multiplier is \(s(s-1)\pi^{-s/2}\Gamma(s/2)/8\). Taking logarithms of absolute values gives OZD4.2 almost everywhere; all terms are locally integrable. The Laplacians of \(-\log8\) and \(-x\log\pi/2\) vanish by direct differentiation. Gamma has poles, with order \(-1\), at all \(-2k\), including \(k=0\). Thus
\[
\Delta\log|F_0|=\Delta\log|\zeta|
+2\pi\delta_0+2\pi\delta_1
-2\pi\sum_{k\ge0}\delta_{-2k}
\]
has the correct sign and every endpoint. In particular the two contributions at \(0\) cancel each other; there was no original-zeta zero there to cancel.

At \(s=2+iy\), the squared modulus is exactly
\[
\frac{(4+y^2)(1+y^2)}{64\pi^2}
\frac{\pi y}{2\sinh(\pi y/2)}|\zeta(2+iy)|^2.
\]
The quotient involving \(y\) is positive for both signs of \(y\) and has limit one at zero. The lower bound (OZR3.2) and this identity give \(\log|F_0(2+iy)|\ge-C(1+|y|)\). The same disk argument bounds the absolute logarithm of \(F_0\) on a unit-height rectangle by \(O(1+|j|)\). The exact logarithmic comparison then bounds the Gamma logarithm there by the same order. This proves every Gaussian pairing used in OZD4. There is no exchange of conditionally convergent integrals.

## OZR6. Reflection and the full odd contribution

The reflection is \(\mathsf R(x,y)=(1-x,y)\), rather than complex conjugation alone. It preserves area and commutes with \(\Delta\). The original functional equation has the full multiplier
\[
\chi(s)=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\]
Together with the real-coefficient conjugation identity this gives
\(L-L\circ\mathsf R=\log|\chi|\). Its divisor has zeros at \(0,-2,-4,\ldots\) and poles at \(1,3,5,\ldots\), with their stated simple orders. This proves OZD5.3–OZD5.4.

An even function times an odd function has zero area integral whenever that integral converges absolutely, by the change of variables \(s\mapsto\mathsf R s\). The preceding estimates establish that convergence here. Therefore the cross terms vanish, leaving
\[
\frac1{2\pi}\int L\Delta\phi
=\frac1{2\pi}\int L_+\Delta\phi_+
+\frac1{4\pi}\int\log|\chi|\Delta\phi_-.
\]
The last coefficient is \(1/(4\pi)\), because \(L_-=\tfrac12\log|\chi|\). Applying the divisor of \(\chi\) gives
\[
\frac12\sum_{k\ge0}[\phi_-(-2k)-\phi_-(1+2k)]
=\sum_{k\ge0}\phi_-(-2k)
=-\phi_-(1)+\sum_{k\ge1}\phi_-(-2k).
\tag{OZR6.1}
\]
In the second equality, \(\phi_-\circ\mathsf R=-\phi_-\); in the third, the \(k=0\) point \(0\) is the reflection of \(1\). These are exactly the missing factors that would spoil the calculation if either reflection or endpoint were omitted. They are present in OZD.

The odd part of the original pole term is \(+\phi_-(1)\), and that of the subtracted trivial-zero terms is \(-\sum_{k\ge1}\phi_-(-2k)\). They cancel (OZR6.1) exactly. The surviving identity is consequently OZD5.7. At the pole,
\[
\phi_+(1)=\tfrac12(r-1)^2(e^{2t}+1),\qquad
\phi_-(1)=\tfrac12(r-1)^2(e^{2t}-1),
\]
so both OZD5.8 and the definite-integral value stated in OZD7 are correct. On a narrow cutoff, zero energy requires the unscaled integral to be \(-\pi(r-1)^2(e^{2t}+1)\). The derivation does not assert that this value has been proved.

## OZR7. Exact source kernel and multiplicity trace

Each summand defining \(\mathcal E_r(t)\) is nonnegative and the Gaussian never vanishes. For fixed \(r>1\), its coefficient vanishes exactly when \(\sigma=1/2\). Thus zero energy is equivalent to vanishing of every \(d_r(\rho)\). If one such coefficient is nonzero, choose the existing source isolator whose value at \(\rho^\#\) is one and whose other values are zero. The corresponding coordinate of \(\beta_r\) is \(\overline{d_r(\rho)}\ne0\). Conversely every coefficient zero makes the boundary zero. AST2 gives \(\ker\beta_r=N_O\), so the remaining equivalence with \(\mathcal R=Q/N_O=0\) follows exactly. There is no claim that its positive-transfer completion being zero proves this source quotient zero.

For \(A_\rho=\mathbb C[h]/(h^{m_\rho})\), evaluation has the exact kernel \((h)/(h^{m_\rho})\). In the ordered basis \(1,h,\ldots,h^{m_\rho-1}\), multiplication by \(b(\rho+h)\) has diagonal \(b(\rho)\) repeated \(m_\rho\) times. Its trace is \(m_\rho b(\rho)\). Changing basis changes neither trace nor kernel. If \(m_\rho=1\), the displayed nilpotent ideal is zero, as it should be. Globally the value kernel is the already retained \(N_0\); the off-line value kernel is \(N_O\). Higher jets have not been identified with zero in the original source.

OZD also correctly confines \(a_{r,t}\), which involves conjugate and real-coordinate data, to its diagonal value algebra. It does not falsely declare this coefficient an entire holomorphic multiplier on all source jets. The curvature identity is the receiving map that is actually proved for that coefficient.

## OZR8. Proved stronger test domain

The Gaussian hypothesis of OZD2.4 can be weakened. Let \(p>1\), let \(K\subset\mathbb R\) be compact, and let \(\phi\in C^\infty(\mathbb C)\) have support in \(K\times\mathbb R\). Assume, with one finite constant for the finitely many derivatives, that
\[
|\partial_x^a\partial_y^b\phi(x,y)|
\le C(1+|y|)^{-p}\qquad(a+b\le2).
\tag{OZR8.1}
\]
Then the same exact original divisor identity holds:
\[
\frac1{2\pi}\int_{\mathbb C}\log|\zeta|\Delta\phi\,dA
=\sum_\rho m_\rho\phi(\rho)+\sum_{k\ge1}\phi(-2k)-\phi(1).
\tag{OZR8.2}
\]
Every displayed integral and series is absolutely convergent. Indeed OZD2.1 bounds the integral of its absolute integrand by a constant times
\(\sum_{j\in\mathbb Z}(1+|j|)^{-p}\log(|j|+2)\), which converges for \(p>1\). On each dyadic zero-height shell the absolute divisor contribution is at most
\[
C\,2^{-jp}\bigl(2^{j+1}\log(2^{j+1}+2)\bigr),
\]
and the sum converges because \(1-p<0\). The real compact support leaves only finitely many trivial zeros.

For the cutoff \(\theta_R\) in OZD2, the union of rectangles meeting \(R\le|y|\le2R\) has logarithmic absolute integral \(O_K(R\log(R+2))\). Thus the first derivative error has absolute integral at most
\[
C R^{-1}R^{-p}R\log(R+2)=C R^{-p}\log(R+2)\longrightarrow0,
\]
and the second derivative error is at most \(C R^{-p-1}\log(R+2)\to0\). Dominated convergence handles the other terms. Applying the compact distribution identity and taking this limit proves (OZR8.2).

This stronger domain also preserves the original functional-equation splitting: \(\log|\chi|=L-L\circ\mathsf R\) has the same logarithmic area bound on reflected fixed strips, so OZD5's proof applies verbatim to tests satisfying (OZR8.1). This observation concerns the original-zeta and functional-equation formulas. The completed comparison OZD4 has only the proved linear-height logarithmic bound, so the same argument for each completed-factor integral separately is asserted here for \(p>2\), or for the existing Gaussian tests. No stronger Gamma estimate has been silently assumed.

For an explicit additional positive receiver take
\[
w_p(y)=(1+y^2)^{-p/2},\qquad
\phi_{r,p,\eta}(x,y)=\eta(x)q_r(x)w_p(y).
\]
All derivatives through order two satisfy (OZR8.1). The resulting exact global energy is
\[
\mathcal E^{(p)}_r=\sum_\rho m_\rho q_r(\sigma)(1+\gamma^2)^{-p/2}
=\frac1{2\pi}\int\log|\zeta|\Delta\phi_{r,p,\eta}\,dA
+(r-1)^2-\sum_{k\ge1}\eta(-2k)q_r(-2k).
\tag{OZR8.3}
\]
Here
\[
\Delta\phi_{r,p,\eta}=h''(x)(1+y^2)^{-p/2}
+h(x)\,p\bigl((p+1)y^2-1\bigr)(1+y^2)^{-p/2-2},
\quad h=\eta q_r.
\tag{OZR8.4}
\]
The second formula follows by two direct derivatives of \(w_p\). The pole has weight one at \(y=0\), as do the trivial-zero evaluations, producing all constants in (OZR8.3). The strictly positive weight and the same global isolators prove
\[
\mathcal E^{(p)}_r=0\quad\Longleftrightarrow\quad\beta_r=0.
\tag{OZR8.5}
\]
This is a proved additional receiver of the same actual boundary. It leaves the original Gaussian source, its approximation theorem and all source-jet maps intact.

## OZR9. Result and next mathematical use

The original functional equation controls the antisymmetric logarithmic potential and cancels exactly its known pole and trivial-zero terms. The positive actual-boundary trace is received by the remaining symmetric original-zeta potential. These facts are established by OZD and verified above; neither establishes that this symmetric quantity is zero.

The concrete follow-through is to use the full geometric degree action on that same faithful energy, as the parallel GDE calculation does, retaining its actual point and source actions. The additional power-decay receiver (OZR8.3) allows an exact test of that action without requiring a Gaussian limit. It supplies another proved map to the same source boundary, not a substituted vanishing assumption or a numerical test on a bounded range.

## OZR10. Changed-portion review and explicit wording repair

The revised OZD file has SHA256 `14ad4cf0c961e66abc4080638e2eaa32380a64a27ce35b72778e3ff5b5133d9b`. This review reread the changed OZD5 sentence and the changed OZD8 source-provenance paragraphs. It did not repeat the whole-proof review documented in OZR0–OZR9.

The previous OZD5 sentence said, inaccurately, that both the reflection and the Laplacian preserve area. Its exact replacement is:

> The reflection \(\mathsf R\) preserves area, and its pullback commutes with \(\Delta\).

The replacement is correct. The Jacobian matrix of \(\mathsf R(x,y)=(1-x,y)\) is \(\operatorname{diag}(-1,1)\), whose determinant has absolute value one, proving preservation of the area measure. The chain rule gives
\[
\partial_x^2(f\circ\mathsf R)=(\partial_x^2f)\circ\mathsf R,
\qquad
\partial_y^2(f\circ\mathsf R)=(\partial_y^2f)\circ\mathsf R,
\]
and hence \(\Delta(f\circ\mathsf R)=(\Delta f)\circ\mathsf R\). A differential operator is not the area-preserving transformation in this argument. OZR6 already used this correct statement, but the initial review did not explicitly flag the inaccurate source sentence. This addendum records that missed wording error and its repair. All displayed OZD formulas and the proof using change of variables remain unchanged.

The revised OZD8 links GTAH and AST to their exact proof files at immutable GitHub commit `36a82ecca98addb8a98b48204e349737856c7223`, with the relevant proof locations named. The text attributes byte comparison and the AST dependency-link repair to the completed publication/source verification. It also explicitly keeps the subsequent GAP/ADM proofs separate from the preceding public cutoff. This review checked the resulting source identities and scope wording; it does not claim an additional independent network retrieval. These changes do not add or alter a mathematical premise. Subject to the explicit wording correction just recorded, the mathematical verification and the additional OZR8 consequences remain in force for the revised OZD version.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
