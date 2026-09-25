# Every vertical weight, the faithful original return, and its residue pairing

25 September 2026. Complete derivation, locators VWR0–VWR10.

## VWR0. Source, purpose, and constructed operations

The source is the user's corrected \(Z_0,Z_1,Z_2,\tau\) construction, with B1–B5, P1–P5 and retraction R1 in [the source operations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md). Primitive \(Z_1/\tau\) has neither parity nor addition. No numerical weight, coefficient, multiplicity, norm or sum of copies is assigned to it here. All integrations, Hilbert spaces and complex scalars below are receiving operations on the already reconstructed original zeta coefficient space. They do not reconstruct primitive presence from integer arithmetic.

The full-system and global-quotient arguments in the retained corpus, USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2 and USR-6152e3bc6302258c, control the interpretation: do not replace the actual whole spectrum with a selected finite or invented spectrum. The amended forward instruction USR-64a88219a3ecddd3 asks what would advance the target using everything already known. The concrete attempt here is to recover, in one faithful comparison, the classes that a single Hilbert receiver can discard, and calculate the original pairing on the entire discarded subspace.

Human provenance: Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, math/9811068v1](https://arxiv.org/abs/math/9811068v1), §III, Theorem 1, and Appendix I, approximate units and proof of Theorem III.1. His original author TeX was read at lines 521–1035 and 3574–4154. The critical-line weighted spectral mechanism and its multiplicity threshold are his results, not a new discovery here. His parameter is \(\delta_{\rm C}=2\delta\) in the notation below. The present calculation supplies the original full-complex comparison, the full family of vertical receivers, and the retained residue calculation.

The original coefficient sheaf and its two charts come from Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, 0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), with exact programme source comparison in [DCP0–DCP12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SOURCE_CC_DOUBLE_PULLBACK.md). The analytic closed-image theorem and actual global zero sections used below are proved in [OMS1–OMS6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), drawing on Ralf Meyer, [math/0412277v3](https://arxiv.org/abs/math/0412277v3). The original contour pairing, its full factors, continuity and two-sided nondegeneracy are proved in [GZR1–GZR7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md), with the exact original-coordinate return in [ASD1](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ACTUAL_SUPPORTED_DUALITY_INDEPENDENT.md). No infinite residue sum is assumed to converge.

## VWR1. The unchanged full coefficient complex

Keep
\[
S=\{h\in\mathcal S(\mathbb R):h(-v)=h(v),\ h(0)=0,\ \int_{\mathbb R}h(v)\,dv=0\},
\]
\[
A=\left\{b\in C^\infty(\mathbb R_{>0}):
 p_{N,j}(b)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jb(u)|<\infty
 \text{ for all }N,j\ge0\right\},
\]
\[
\Sigma h(u)=2\sum_{n\ge1}h(nu),\quad J=\Sigma S,\quad Q=A/J,
\quad M_0b(s)=\int_0^\infty b(u)u^s\frac{du}{u}.
\tag{VWR1.1}
\]
Here \(J\) is the actual closed Fréchet image, not a selected Hilbert closure. Write \(\mathcal B=M_0A\) and
\[
I=\{F\in\mathcal B:F^{(j)}(\rho)=0\text{ for every actual nontrivial zero }\rho,
 0\le j<m_\rho\}.
\]
The proved original Mellin map gives \(Q\cong\mathcal B/I\). Let
\[
P=W_+\oplus W_-,\qquad D=[P\xrightarrow{d=r_+-r_-}A],\qquad H=\ker d,
\tag{VWR1.2}
\]
in degrees 0,1. Each \(W_\pm\) retains the entire original \(S\), its two labelled endpoint lines, and its whole extra closed coefficient copy. The restrictions are \(\Sigma\) and \(R\Sigma\), zero on those endpoint and extra copies. Thus \(\operatorname{im}d=J\). The raw actions are
\[
T_ab(u)=b(u/a),\quad Lb=-u\partial_ub,\quad Rb(u)=u^{-1}b(u^{-1}),
\]
\[
M_0(T_ab)(s)=a^sM_0b(s),\quad M_0(Lb)(s)=sM_0b(s),\quad
M_0(Rb)(s)=M_0b(1-s).
\tag{VWR1.3}
\]
The source-return construction already proves that all these maps act on the indicated quotient. In particular \(RJ=J\), by the full Poisson identity
\[
\Sigma\widehat h(u)=u^{-1}\Sigma h(u^{-1})+u^{-1}h(0)-\int h.
\tag{VWR1.4}
\]
Its endpoint terms vanish on the stated \(S\), while their separate coefficient lines remain in \(P\).

## VWR2. Constructing the whole receiving family

For \(0<\sigma<1\) and \(\delta>0\) define
\[
\mathcal H_{\sigma,\delta}
=L^2\bigl(\mathbb R_{>0},u^{2\sigma-1}(1+(\log u)^2)^\delta\,du\bigr).
\tag{VWR2.1}
\]
The density and exponent in this formula are part of the object and are retained. The original inclusion \(A\hookrightarrow\mathcal H_{\sigma,\delta}\) is continuous: choose an integer \(N>|\sigma|+1\), bound \(|b(u)|\) by \(p_{N,0}(b)/(u^N+u^{-N})\), and integrate the resulting integrable function at both endpoints. It has dense image because smooth compactly supported functions of \(\log u\) lie in \(A\) and are dense in this weighted \(L^2\) space.

Only to compute the norm, introduce the explicitly invertible coordinate map
\[
(U_\sigma b)(x)=e^{\sigma x}b(e^x),\qquad
(U_\sigma^{-1}g)(u)=u^{-\sigma}g(\log u).
\]
Substitution \(u=e^x\) proves
\[
\|b\|_{\sigma,\delta}^2
=\int_{\mathbb R}|U_\sigma b(x)|^2(1+x^2)^\delta\,dx,
\quad
M_0b(\sigma+it)=\int_{\mathbb R}U_\sigma b(x)e^{itx}\,dx.
\tag{VWR2.2}
\]
This is a coordinate calculation on \(b\), not a replacement of \(\zeta\) or its parameter. In the earlier convention \(Eh=u^{1/2}\sum_{n\ge1}h(nu)\), the exact relation is \(E h(e^x)=\tfrac12U_{1/2}\Sigma h(x)\), so its squared norm is \(\tfrac14\|\Sigma h\|_{1/2,\delta}^2\). The factor is not suppressed.

Let
\[
C_{\sigma,\delta}=\overline J^{\,\mathcal H_{\sigma,\delta}},\qquad
Q_{\sigma,\delta}=\mathcal H_{\sigma,\delta}/C_{\sigma,\delta},\qquad
\alpha_{\sigma,\delta}:Q\longrightarrow Q_{\sigma,\delta},\quad[b]\longmapsto[b].
\tag{VWR2.3}
\]
The closure is explicit. The map is well defined and continuous, and its image is dense by the preceding density. Surjectivity or a topological embedding is not asserted.

## VWR3. Exact prime bound and its dependence on the vertical weight

Put \(t=\log a\). Direct substitution in (VWR2.1) gives
\[
\|T_ab\|_{\sigma,\delta}^2
=a^{2\sigma}\int_0^\infty |b(v)|^2v^{2\sigma-1}
 (1+(\log v+t)^2)^\delta\,dv.
\tag{VWR3.1}
\]
The supremum of \((1+(x+t)^2)/(1+x^2)\) is the largest eigenvalue of
\(\begin{pmatrix}1&t\\t&1+t^2\end{pmatrix}\): evaluating its quadratic form on \((x,1)\), then taking all directions by limits, proves this assertion. Its determinant is 1 and its trace is \(t^2+2\). Therefore
\[
\Lambda_+(t)=\frac{t^2+2+|t|\sqrt{t^2+4}}2,
\qquad
\|T_a\|_{\mathcal H_{\sigma,\delta}}=a^\sigma\Lambda_+(\log a)^{\delta/2}.
\tag{VWR3.2}
\]
Equality follows by functions supported in successively smaller neighborhoods of points approaching the supremum. The formula remains exact at \(a=1\).

Since \(T_aJ=J\), continuity and invertibility give \(T_aC_{\sigma,\delta}=C_{\sigma,\delta}\). The quotient action obeys the same upper bound. For every integer \(n\ge1\) and every prime \(p\),
\[
\|T_p^n\|_{Q_{\sigma,\delta}}
\le p^{n\sigma}\Lambda_+(n\log p)^{\delta/2},\qquad
\|T_p^{-n}\|_{Q_{\sigma,\delta}}
\le p^{-n\sigma}\Lambda_+(n\log p)^{\delta/2}.
\tag{VWR3.3}
\]
Since \(\Lambda_+(t)\le t^2+2\), its fixed-power contribution has \(n\)-th root tending to 1. The spectral-radius formula applied to \(T_p\) and its inverse gives
\[
\operatorname{Spec}(T_p\mid Q_{\sigma,\delta})\subseteq\{z:|z|=p^\sigma\}.
\tag{VWR3.4}
\]
On a zero Hilbert space the spectrum is empty and the inclusion still holds. Thus the square-root estimate at \(\sigma=1/2\) is a proved receiving estimate. The same computation gives the exact radius at every other \(\sigma\); it has not shown that those other receivers vanish.

## VWR4. Exact continuous jets and the whole closure

For \(\rho\in\mathbb C\) the derivative functional on \(A\) is
\[
\ell_{\rho,j}(b)=(M_0b)^{(j)}(\rho)
=\int_0^\infty b(u)u^{\rho-1}(\log u)^j\,du.
\]
It extends continuously to \(\mathcal H_{\sigma,\delta}\) exactly when
\[
\Re\rho=\sigma,\qquad j<\delta-\tfrac12.
\tag{VWR4.1}
\]
Indeed its logarithmic-coordinate dual density is
\(x^je^{(\rho-\sigma)x}\). The squared dual norm is
\(\int |x|^{2j}e^{2(\Re\rho-\sigma)x}(1+x^2)^{-\delta}dx\).
Exponential growth at one endpoint makes this infinite unless the real parts agree. When they agree, comparison at infinity gives precisely (VWR4.1). Necessity follows also from uniqueness of a distribution representing the functional on the dense compactly supported smooth subspace; a continuous functional would have exactly this density in the weighted dual.

For these allowed indices the Riesz vector, with inner product linear in the first argument, is
\[
r_{\rho,j}(u)=u^{\bar\rho-2\sigma}(\log u)^j(1+(\log u)^2)^{-\delta},
\]
\[
\|r_{\rho,j}\|_{\sigma,\delta}^2
=\frac{\Gamma(j+\tfrac12)\Gamma(\delta-j-\tfrac12)}{\Gamma(\delta)}.
\tag{VWR4.2}
\]
To obtain the constant substitute \(y=x^2\) in the integral over both half-lines, giving \(\int_0^\infty y^{j-1/2}(1+y)^{-\delta}dy\), then the beta integral. This establishes the exact vector, not only its existence.

Define \(r_\delta(\rho)\) to be the number of integers \(j\) satisfying \(0\le j<m_\rho\) and \(j<\delta-1/2\). Then
\[
C_{\sigma,\delta}
=\bigcap_{\substack{\rho\in\mathscr Z,\ \Re\rho=\sigma\\0\le j<r_\delta(\rho)}}\ker\ell_{\rho,j}
\quad\text{inside }\mathcal H_{\sigma,\delta}.
\tag{VWR4.3}
\]
Here is a proof of the reverse inclusion, including the global rather than finite support step. Put
\[
h_0(v)=\frac{\log|v|-2}{8\sqrt\pi}e^{-(\log|v|)^2/4}\quad(v\ne0),\qquad h_0(0)=0.
\]
Every derivative at zero and infinity has Gaussian decay in \(\log|v|\) dominating every fixed exponential, so \(h_0\) is even Schwartz. Completing the square in the Gaussian integral gives
\[
\int_0^\infty h_0(v)v^s\frac{dv}{v}=\frac{s-1}{2}e^{s^2},\qquad
\int_{\mathbb R}h_0(v)dv=0.
\]
Thus \(h_0\in S\), and its actual sum \(b_0=\Sigma h_0\in J\) has
\[
M_0b_0(s)=(s-1)\zeta(s)e^{s^2}.
\tag{VWR4.4}
\]
This identity is first obtained by absolutely convergent summation for \(\Re s>1\), then continued. It uses \(\zeta\) itself; the pole at 1 is explicitly canceled in this auxiliary test function, not removed from the programme. On any line \(0<\sigma<1\), its zeros are precisely the actual \(\zeta\) zeros on that line, with their full multiplicities.

A continuous complex-linear functional annihilating \(J\) has a logarithmic density \(w\in L^2((1+x^2)^{-\delta}dx)\). It is a tempered distribution. Annihilation of every dilation of \(b_0\) implies
\[
\widehat{U_\sigma b_0}(-t)\widehat w(t)=0,
\tag{VWR4.5}
\]
using \(\widehat g(t)=\int g(x)e^{itx}dx\); this follows by Fourier transforming \(\int (U_\sigma b_0)(x-y)w(x)dx\) in \(y\). The extra nonzero factor \(e^{\sigma y}\) in the original dilation does not alter its vanishing.

Take \(\theta\in C_c^\infty(\mathbb R)\) equal to 1 near zero. Multiplication of \(\widehat w\) by \(\theta(t/n)\) converges to \(\widehat w\) in the weighted-dual norm: its inverse Fourier operators are an approximate identity; translation on the weighted dual has at most polynomial norm by (VWR3.2), and Minkowski's inequality followed by dominated convergence proves strong convergence. This argument applies first to compactly supported smooth densities and then to all densities by density and the same uniform bound. Each cutoff retains (VWR4.5).

On a compact interval, the real-analytic multiplier in (VWR4.5) has finitely many zeros. Division by its nonzero part removes the distribution away from those points. At a zero of order \(m\), multiplication by \((t-t_0)^m\) annihilates it, so it is a linear combination of the delta distribution and its first \(m-1\) derivatives. This follows by subtracting the order-\(m-1\) Taylor polynomial of each test function; the remainder is divisible by \((t-t_0)^m\). The inverse transform is consequently a finite sum of \(x^je^{i\Im\rho x}\).

Membership in the weighted dual permits only the exponents in (VWR4.1). For completeness, in a finite exponential-polynomial sum a nonzero leading degree \(d\) cannot evade this bound by cancellation: the mean square of the leading trigonometric polynomial on \([R,2R]\) tends to its positive diagonal coefficient sum, since every distinct-frequency cross integral is bounded independently of \(R\). Lower polynomial degrees have smaller order. The weighted integral on successive dyadic intervals is therefore bounded below by a positive multiple of \(R^{2d-2\delta+1}\), and its sum diverges when \(d\ge\delta-1/2\). Repeating after removing the top degree proves the assertion for every term.

Every allowed term annihilates \(J\), since \(M_0J=I\). The finite allowed-jet functionals therefore have dense span in the entire annihilator of \(J\). Taking their common kernel proves (VWR4.3). This is the weighted mechanism of Connes's proof, applied here to the explicit original \(\Sigma\) and to every vertical line. In particular the intersection is the whole Hilbert space when its index set is empty.

## VWR5. The exact comparison and its jointly faithful family

Define the closed subspace of \(\mathcal B\)
\[
I_{\sigma,\delta}=\{F:F^{(j)}(\rho)=0\text{ whenever }\Re\rho=\sigma,
 \rho\in\mathscr Z,\ 0\le j<r_\delta(\rho)\}.
\]
Intersecting (VWR4.3) with \(A\) and using the actual Mellin isomorphism proves
\[
\ker\alpha_{\sigma,\delta}=I_{\sigma,\delta}/I.
\tag{VWR5.1}
\]
Hence the map
\[
\alpha_{\rm all}:Q\longrightarrow
\prod_{0<\sigma<1}\prod_{N=1}^{\infty}Q_{\sigma,N},
\qquad q\longmapsto(\alpha_{\sigma,N}q)_{\sigma,N}
\tag{VWR5.2}
\]
is continuous, equivariant for every raw dilation, and injective. To prove injectivity, let a class have zero image. For every actual zero \(\rho\) and every \(j<m_\rho\), choose \(\sigma=\Re\rho\) and \(N=j+1\); then \(j<N-1/2\), so that derivative vanishes by (VWR5.1). Every full jet vanishes, hence its representative lies in \(I\). The class is zero. This proof retains the whole infinite zero divisor; it does not identify \(Q\) with an unrestricted product of jets or claim the map has continuous inverse onto its image.

For the critical family alone put
\[
I_{\rm line}=\{F\in\mathcal B:F^{(j)}(\rho)=0\text{ at every }\Re\rho=1/2,
 0\le j<m_\rho\},\qquad K_{\rm off}=I_{\rm line}/I.
\tag{VWR5.3}
\]
Then
\[
\bigcap_{N=1}^{\infty}\ker\alpha_{1/2,N}=K_{\rm off}.
\tag{VWR5.4}
\]
This is an actual subspace of the original full quotient. It includes all possible infinite configurations admitted by that quotient topology, not only a direct sum of finite blocks. The assertion \(K_{\rm off}=0\) is equivalent to RH: RH makes \(I_{\rm line}=I\); conversely, the actual single-zero representatives in VWR8 give a nonzero member of \(K_{\rm off}\) for each noncritical zero. This equivalence is proved here to identify the exact subspace being tested; neither its vanishing nor its nonvanishing is assumed.

## VWR6. Location of the loss in the full original complex

Keep every summand of \(P\) and define
\[
D_{\sigma,\delta}^{\rm alg}=[P\xrightarrow d\mathcal H_{\sigma,\delta}].
\tag{VWR6.1}
\]
The original map \(D\to D_{\sigma,\delta}^{\rm alg}\) is identity on \(P\), inclusion on \(A\). It induces identity on \(H^0=H\) and the injective map
\[
A/J\hookrightarrow\mathcal H_{\sigma,\delta}/J.
\tag{VWR6.2}
\]
Injectivity is elementary: an element of \(A\) maps to zero in the right-hand quotient exactly when it already lies in \(J\). Thus no original class is removed at this algebraic step.

The further exact sequence is
\[
0\longrightarrow C_{\sigma,\delta}/J
\longrightarrow\mathcal H_{\sigma,\delta}/J
\longrightarrow\mathcal H_{\sigma,\delta}/C_{\sigma,\delta}
\longrightarrow0.
\tag{VWR6.3}
\]
Its middle term need not be Hausdorff. Intersecting its kernel with the original embedded \(Q\) gives exactly (VWR5.1). All original endpoint and extra copies remain in degree zero throughout. Thus the calculation locates the lost classes in a stated closure operation, not in an asserted failure of \(Z_1/\tau\) arithmetic.

The actual sheaf map is also constructed, without replacing the original sheaf by a constant diagram. Set
\[
\mathcal F_{\sigma,\delta}
=(W_+\xrightarrow{\iota_{\sigma,\delta}r_+}\mathcal H_{\sigma,\delta}
 \xleftarrow{\iota_{\sigma,\delta}r_-}W_-),
\quad \iota_{\sigma,\delta}:A\hookrightarrow\mathcal H_{\sigma,\delta}.
\tag{VWR6.4}
\]
The identity maps on \(W_+,W_-\) and \(\iota_{\sigma,\delta}\) on the generic stalk commute with both displayed restrictions. They therefore give an injective sheaf map \(\mathcal F\to\mathcal F_{\sigma,\delta}\) on the original three-point space. Evaluation on each minimal open is exact, so the two-open Čech complexes compute derived global sections of both sheaves. The induced map is precisely (VWR6.1), with its full original \(P\). Thus it preserves the entire support geometry as a stated coefficient morphism before the cohomological closure step.

For the already constructed full source map \(f:X\to Y\), its pullback is the sheaf map
\(f^{-1}\mathcal F\to f^{-1}\mathcal F_{\sigma,\delta}\).
At every arithmetic point it is the same original inclusion, and at the two added closed source points it is identity on the full \(W_\pm\). These assertions follow from the stalk formula for inverse image; its restrictions commute by the same calculation. If the full correspondence of FSC6 is used, both sheaves and this morphism satisfy its stated algebraic complex-vector coefficient hypotheses, so its derived comparison applies to this actual sheaf map. No assertion identifying sheaf cohomology with a Hausdorff quotient has entered: (VWR6.3) is still the explicit further operation.

Even that further operation has an exact sheaf sequence. Let
\[
\overline{\mathcal F}_{\sigma,\delta}
=(W_+\xrightarrow0 Q_{\sigma,\delta}\xleftarrow0 W_-).
\]
Identity on the closed stalks and projection on the generic stalk give
\[
0\longrightarrow j_{\eta!}C_{\sigma,\delta}
\longrightarrow\mathcal F_{\sigma,\delta}
\longrightarrow\overline{\mathcal F}_{\sigma,\delta}
\longrightarrow0.
\tag{VWR6.5}
\]
Stalkwise exactness proves this sequence, since \(r_\pm(W_\pm)=J\subset C_{\sigma,\delta}\). Its ordered Čech sequence is exactly
\[
0\to[0\to C_{\sigma,\delta}]
\to[P\xrightarrow d\mathcal H_{\sigma,\delta}]
\to[P\xrightarrow0Q_{\sigma,\delta}]\to0.
\]
The connecting map sends \(p\in P\) to \(dp\in C_{\sigma,\delta}\): lift \(p\) by the identity in degree zero and apply the original differential. Its entire nonzero cohomology sequence is consequently
\[
0\to H\to P\xrightarrow d C_{\sigma,\delta}
\longrightarrow\mathcal H_{\sigma,\delta}/J
\longrightarrow Q_{\sigma,\delta}\to0.
\tag{VWR6.6}
\]
The image of the middle arrow is precisely \(C_{\sigma,\delta}/J\); its intersection with the original embedded \(Q\) is exactly the computed kernel. This realizes the closure defect by its full sheaf and cochain maps. The sheaf \(j_{\eta!}C_{\sigma,\delta}\) has its stated generic support; it is not renamed as Deligne's closed-fibre support group.

## VWR7. The mirror, retained prime actions, and every support label

The substitution \(v=1/u\) proves
\[
\|Rb\|_{1-\sigma,\delta}^2
=\int_0^\infty|u^{-1}b(u^{-1})|^2u^{2(1-\sigma)-1}
 (1+(\log u)^2)^\delta du
=\|b\|_{\sigma,\delta}^2.
\tag{VWR7.1}
\]
Thus the original \(R\), with its factor \(u^{-1}\), extends to an isometry \(\mathcal H_{\sigma,\delta}\to\mathcal H_{1-\sigma,\delta}\). It carries the closures of \(J\) onto one another and induces the same isometry on the corresponding quotients. Direct evaluation gives
\[
RT_a=aT_{1/a}R,\qquad R^2=1,
\qquad (M_0Rb)^{(j)}(\rho)=(-1)^j(M_0b)^{(j)}(1-\rho).
\tag{VWR7.2}
\]
Complex conjugation acts at the same real weight and sends the zero label to \(\bar\rho\). The mirror interchanges \(\sigma\) and \(1-\sigma\); its prime radii consequently multiply to \(p\). This gives the exact character-\(a\) similitude without forcing either individual radius to be \(\sqrt p\). Under Deligne's convention \(|\alpha|=p^{w/2}\), the target character has weight 2, while each desired input weight is 1.

Each original supported receiving label can be retained by applying the coefficient map at that label, \((b,\lambda)\mapsto(\alpha_{\sigma,\delta}[b],\lambda)\), whenever that receiving carrier's stated coefficient slot is \(Q\). In the full family the coefficient map is injective and the label is unchanged. This sentence uses only the already constructed labelled coefficient carrier; it does not assert an additional operation on primitive \(\tau\), nor replace an unconstructed support carrier by a Cartesian product.

## VWR8. The complete original pairing on the discarded subspace

Write \(F=M_0b\), \(G=M_0c\). Retain the actual global form
\[
B_\zeta([b],[c])=\frac1{2\pi i}
\left(\int_{2-i\infty}^{2+i\infty}-\int_{-1-i\infty}^{-1+i\infty}\right)
\frac{F(s)G(1-s)}{\zeta(s)}ds.
\tag{VWR8.1}
\]
Both integrals are upward. The two absolute bounds and rapid-division descent are GZR2–GZR3. The pole at 1 is a zero of the reciprocal denominator; \(\zeta(0)=-1/2\); the trivial zeros lie outside these particular contours and remain in the original Schwartz return
\[
\operatorname{Res}_{s=-2r}\frac{F(s)}{\zeta(s)}
=\frac{F(-2r)}{\zeta'(-2r)},\quad
\zeta'(-2r)=(-1)^r2^{-2r-1}\pi^{-2r}(2r)!\zeta(1+2r).
\tag{VWR8.2}
\]
Reflection uses the full original meromorphic multiplier
\[
\zeta(s)=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}\zeta(1-s),
\tag{VWR8.3}
\]
holomorphic and nonzero at every nontrivial zero. No multiplier is deleted in constructing this return.

Here are the actual global sections needed in the proof. Use the existing auxiliary function
\[
F_*(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)\in I,
\quad F_*(0)=F_*(1)=\frac18,
\]
\[
F_*(-2r)=F_*(1+2r)
=\frac{(1+2r)2r}{8}\pi^{-(1+2r)/2}\Gamma((1+2r)/2)\zeta(1+2r).
\tag{VWR8.4}
\]
It is an auxiliary representative, not the working zeta function. For an actual zero \(\rho\), let \(m=m_\rho\), \(U_\rho(s)=F_*(s)/(s-\rho)^m\), and let
\[
a_{\rho,k}=F_*^{(m+k)}(\rho)/(m+k)!,\quad d_{\rho,0}=a_{\rho,0}^{-1},\quad
d_{\rho,n}=-a_{\rho,0}^{-1}\sum_{r=1}^na_{\rho,r}d_{\rho,n-r}.
\]
Then
\[
E_{\rho,j}(s)=U_\rho(s)\left(\sum_{n=0}^{m-1}d_{\rho,n}(s-\rho)^n\right)(s-\rho)^j
\quad(0\le j<m)
\tag{VWR8.5}
\]
lies in \(\mathcal B\), has exactly the Taylor jet \((s-\rho)^j\) modulo \((s-\rho)^m\), and has zero full jets at every other nontrivial zero. Taylor division at \(\rho\) proves holomorphy; division away from \(\rho\) and multiplication by the finite polynomial preserve the strip decay. These are the original GZR5 sections. Their raw representatives are
\[
b_{\rho,j}(u)=\frac1{2\pi}\int_{\mathbb R}
 E_{\rho,j}(\tfrac12+it)u^{-1/2-it}dt\in A,
\quad M_0b_{\rho,j}=E_{\rho,j}.
\tag{VWR8.6}
\]
Their \(\sigma\)-receiver image is nonzero precisely when \(\sigma=\Re\rho\) and \(j<\delta-1/2\), by VWR4–VWR5. Thus VWR5.2 retains every actual primary vector.

Write the full original germ as
\[
\zeta(\rho+t)=t^mu_\rho(t),\qquad
u_{\rho,k}=\zeta^{(m+k)}(\rho)/(m+k)!,
\]
\[
c_{\rho,0}=u_{\rho,0}^{-1},\quad
c_{\rho,n}=-u_{\rho,0}^{-1}\sum_{r=1}^nu_{\rho,r}c_{\rho,n-r}.
\tag{VWR8.7}
\]
For every local pair the exact finite residue is
\[
\sum_{i+j+k=m-1}\frac{F^{(i)}(\rho)}{i!}
 \frac{G^{(j)}(1-\rho)}{j!}(-1)^jc_{\rho,k}.
\tag{VWR8.8}
\]
This follows by taking the coefficient of \(t^{m-1}\) in \(F(\rho+t)G(1-\rho-t)u_\rho(t)^{-1}\). With either slot an isolator, the global integrand has just the one possible pole; GZR5's uniform strip division proves that the horizontal contour contributions vanish. Hence (VWR8.8) then equals the full form (VWR8.1), not a formal infinite sum.

**The restriction of \(B_\zeta\) to \(K_{\rm off}\times K_{\rm off}\) is two-sided nondegenerate.** To prove it, take a nonzero \([F]\in K_{\rm off}\). It has some nonzero jet, necessarily at a noncritical \(\rho\). Let \(\ell\) be its first nonzero Taylor degree there and set \(G=E_{1-\rho,m-1-\ell}\). Since \(1-\rho\) is also noncritical, \([G]\in K_{\rm off}\). Formula (VWR8.8) gives
\[
B_\zeta([F],[G])=(-1)^{m-1-\ell}
\frac{F^{(\ell)}(\rho)}{\ell!}\frac{m!}{\zeta^{(m)}(\rho)}\ne0.
\tag{VWR8.9}
\]
For nonzero \([G]\in K_{\rm off}\), take its first nonzero Taylor degree \(\ell\) at \(\eta\) and choose \(F=E_{1-\eta,m_\eta-1-\ell}\). The same formula gives \((-1)^\ell G^{(\ell)}(\eta)c_{1-\eta,0}/\ell!\ne0\). This proves the other side. No assertion that \(K_{\rm off}\) contains a nonzero element has been used.

Consequently any quotient map killing a nonzero part of \(K_{\rm off}\) cannot carry this original bilinear form in both slots: a killed vector pairs nontrivially with an actual retained vector. The full family VWR5.2 avoids that loss. More precisely, within \(\mathbb C[t]/t^m\), the kernel of a receiver retaining the first \(r\) Taylor coefficients is \(t^r\mathbb C[t]/t^m\). Its annihilator in the reflected block is \(v^{m-r}\mathbb C[v]/v^m\), because substitution \(v=-t\) and multiplication by the full invertible series \(u_\rho^{-1}\) preserve vanishing order; successively testing \(t^r,\ldots,t^{m-1}\) forces exactly those first \(m-r\) reflected coefficients to vanish. This computes the exact pairing return for every truncated multiplicity as well.

## VWR9. Exact relation to the lifting target and next calculation

The construction proves a faithful global family, the precise kernels of its individual components, a full-complex comparison retaining every closed summand, and a nondegenerate original residue form on the critical-family kernel. In particular, neither an unspecified change in prime counting nor a locally invented spectrum was used. Every primary section comes from the original full \(\zeta\).

The raw prime action on the family has radii \(p^\sigma\); reflection pairs \(p^\sigma\) with \(p^{1-\sigma}\). It therefore accounts for the already proved character-\(a\) bilinear similitude on the whole space, including its possible off-critical subspace. Its target has Deligne weight 2; the individual input weights are \(2\sigma\) and \(2(1-\sigma)\). The critical-line Hilbert estimate does not erase that subspace in the original complex. The mixed global contraction GMC acts on a different, explicitly constructed exact complex and likewise does not delete it.

Pierre Deligne's [Weil II, §3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/) first establishes opposing weight bounds for the actual invariant classes and support group, then uses exactness. The calculation here makes the next test concrete: use the already constructed full-source correspondence and original supported pairing to determine a geometric support restriction on the jointly faithful family (VWR5.2), rather than imposing \(\sigma=1/2\) by taking only one family component. The present derivation has attempted the full-family return and computed its original pairing; it has not proved the numerical exclusion of all \(\sigma\ne1/2\). That exclusion remains the active lifting target, not a premise inserted into a theorem.

## VWR10. The full arithmetic defect and the generic-point comparison

The preceding kernel calculation can be returned to the whole original prime trace, rather than stopping at a Hilbert-space statement. For \(b\in A\), put \(F=M_0b\) and define
\[
P_\zeta(b)=\sum_{n=2}^{\infty}\Lambda(n)
 \bigl(b(n)+n^{-1}b(n^{-1})\bigr),
\]
\[
A_\infty(b)=\frac1{2\pi}\int_{\mathbb R}F(\tfrac12+it)
 \left(\frac12\psi(\tfrac14+it/2)+\frac12\psi(\tfrac14-it/2)-\log\pi\right)dt.
\tag{VWR10.1}
\]
Here \(\Lambda(p^r)=\log p\), and it is zero at other integers; \(\psi=\Gamma'/\Gamma\). Thus all prime repetitions and both Gamma derivatives are explicit.

The full original explicit formula, with its retained endpoint and trivial-zero return, is
\[
Z(F):=\sum_{\rho\in\mathscr Z}m_\rho F(\rho)
=F(0)+F(1)+A_\infty(b)-P_\zeta(b).
\tag{VWR10.2}
\]
This is the earlier programme formula C10.1–C10.4 in [TAU_TWISTOR_TATE_AND_WEIL.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/TAU_TWISTOR_TATE_AND_WEIL.md), with its proof source OZC1–OZC15 and the public [SZW33–SZW38 derivation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/76f421965914beb133df797835f940849844dc4f/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md). C6–C10 were reread for this application. It is not a new explicit formula attributed to this note.

The exact change from that existing test convention is
\[
h(v)=e^{-v/2}b(e^{-v}),\qquad
\int_{\mathbb R}h(v)e^{-(s-1/2)v}dv=F(s).
\tag{VWR10.3}
\]
Substitution \(u=e^{-v}\) proves the second identity, including the reversed integration endpoints. Moreover
\[
\frac{h(\log n)+h(-\log n)}{\sqrt n}
=n^{-1}b(n^{-1})+b(n),
\]
and the source Fourier transform is exactly \(F(1/2+it)\). Since \(\psi(\bar z)=\overline{\psi(z)}\) in this domain, the two half-digamma terms in (VWR10.1) equal the source's real-part expression. This proves the comparison without suppressing either term.

To extend the source's compact smooth tests to this entire \(A\), take smooth logarithmic cutoffs tending to one. Their products with \(b\) converge to \(b\) in every \(p_{N,j}\): on the cutoff tails, use one additional exponential weight from \(p_{N+1,j}\), and retain each derivative of the cutoff by the Leibniz rule. The Mellin transforms therefore converge in \(\mathcal B\). The prime sum is continuous, since for \(N>2\) its absolute tail is bounded by a fixed multiple of
\(p_{N,0}(b)\sum_{n\ge2}(\log n)(n^{-N}+n^{-N-1})\).
The Gamma integrand has logarithmic growth in \(|t|\), controlled by the Mellin strip seminorm with decay power 2. The zero sum is continuous because the actual zero-count bound \(N(T)=O(T\log(eT))\) gives
\(\sum_\rho m_\rho(1+|\Im\rho|)^{-2}<\infty\).
This proves passage to the limit in every term of (VWR10.2), not only the spectral sum.

Publication source credit: Human-source attribution: the unconditional zero-counting estimate is the classical Riemann–von Mangoldt theorem. The inspected native-TeX witness is Alain Connes, [The Riemann Hypothesis: Past, Present and a Letter Through Time](https://arxiv.org/abs/2602.04022v1), the Hardy–Littlewood discussion immediately before “Zero-free regions and zero-density estimates” (author TeX line499). It states the asymptotic that implies the bound used here; this is not a new zero-counting theorem.

For every finite trivial-zero cutoff \(M\), retain also the unreduced identity from the same source:
\[
Z(F)+\sum_{r=1}^{M}F(-2r)-F(1)
=A_\infty(b)+F(0)+\sum_{r=1}^{M}F(-2r)-P_\zeta(b).
\tag{VWR10.4}
\]
The matching finite trivial-zero contributions have not been declared nonexistent, and no limit of this generally uncontrolled trivial-zero sum is taken. Equations (VWR8.2), (VWR8.3), and (VWR10.4) retain their full original return.

The scalar spectral defect after all critical-line observations is now the concrete continuous functional
\[
\begin{aligned}
\Theta_{\rm off}(b)
&=F(0)+F(1)+A_\infty(b)-P_\zeta(b)
 -\sum_{\Re\rho=1/2}m_\rho F(\rho)\\
&=\sum_{\Re\rho\ne1/2}m_\rho F(\rho).
\end{aligned}
\tag{VWR10.5}
\]
Both sums converge absolutely by the preceding estimate. Every element of \(J\) is annihilated, because all its zero values vanish; hence this functional descends continuously to the original \(Q\). It is a spectral distribution, not an assertion that a raw dilation on an infinite-dimensional Hilbert space has an ordinary trace. On the actual isolator (VWR8.6),
\[
\Theta_{\rm off}(b_{\rho,0})=
\begin{cases}m_\rho,&\Re\rho\ne1/2,\\0,&\Re\rho=1/2.\end{cases}
\tag{VWR10.6}
\]
Consequently this observable vanishes identically exactly when \(K_{\rm off}=0\). Higher primary jets need the full residue pairing VWR8, because a value trace alone does not distinguish them.

Alain Connes and Caterina Consani's [*On the Jacobian of \(\overline{\operatorname{Spec}\mathbb Z}\)*, 2602.15941v1, §8](https://arxiv.org/abs/2602.15941v1), original author TeX `Jacobian.tex` lines 2501–2630, gives the idèle-translation and generic-point interpretation used here. Their semilocal formula is, with all its terms,
\[
\operatorname{Tr}\bigl(\theta(h)\widehat P_\lambda P_\lambda\bigr)
=2h(1)\log\lambda+
\sum_{v\in S}\int_{\mathbb Q_v^\times}'
 \frac{h(u^{-1})}{|1-u|}\,d^*u+o(1).
\tag{VWR10.7}
\]
This formula concerns their stated semilocal Hilbert space and compactly supported idèle-class test; it is not substituted for (VWR10.2) by an assumed global limit. The cutoff product is the specified ordered product of two projections. The paper identifies the coefficient \(2h(1)\log\lambda\) with the generic-point contribution. It distinguishes translations from a finite-field Frobenius.

There is an exact test of whether a nonzero defect (VWR10.5) could be only an altered multiple of this evaluation-at-identity contribution in the multiplicative test variable. Choose an even \(\varphi\in C_c^\infty((-1/10,1/10))\) with \(\varphi(0)=1\), and set
\[
h_*(v)=\varphi(v-1)+\varphi(v+1)
 -\varphi(v-3/2)-\varphi(v+3/2).
\tag{VWR10.8}
\]
It is even, zero at zero, and has integral zero because the four translated integrals cancel with their displayed signs. Thus \(h_*\in S\). Its actual sum \(b_* =\Sigma h_*\in J\) satisfies
\[
b_*(1)=2\sum_{n\ge1}h_*(n)=2,
\qquad \Theta_{\rm off}(b_*)=0.
\tag{VWR10.9}
\]
Only the integer \(n=1\) meets the support of a positive-center first bump; neither bump centered at \(3/2\) meets an integer. This proves the value 2 exactly.

It follows that \(\Theta_{\rm off}=c\,[b\mapsto b(1)]\) as functionals on \(A\) forces \(c=0\), and then forces \(\Theta_{\rm off}=0\). Thus a nonzero off-critical defect cannot be absorbed as a changed scalar coefficient of that generic-point evaluation. This tests precisely that proposed absorption, not every possible geometric modification. It uses the entire summation image and its moment constraints; no source parity, addition or count is assigned to primitive \(\tau\). A geometric vanishing result must control the actual functional and the full jet pairing above, while preserving the displayed source maps.

## VWR11. Subsequent exact harmonic and closed-support return

The full continuation is [HSW0–HSW9, including HSW6A–6B](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/ORIGINAL_ZETA_HARMONIC_SWEEP_AND_OFFCRITICAL_DEFECT.md), [OPD1–OPD6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/ORIGINAL_PRIME_DILATION_FORCING_IDENTITY.md), and [HCS0–HCS12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/HILBERT_CLOSURE_CLOSED_SUPPORT_AND_RESTRICTION.md), with complete independent proofs alongside each calculation. These extend VWR6–VWR10 on the same original spaces. No receiver replaces the full original quotient.

The constructed original source test \(b_\dagger=\Sigma h_\dagger\in J\) has Mellin transform \(G(s)G(1-s)\), with \(G(s)=2\zeta(s)(s-1)e^{s^2}/2\), and endpoint values \(\exp(1)/2\). Its original zero trace is zero. The exact harmonic value is

\[
\mathcal H_{\rm off}(b_\dagger)=2\sum_\rho m_\rho|\Re\rho-\tfrac12|\|b_\rho\|_{L^2(du)}^2
=2\sum_\rho m_\rho|\Re\langle b_\rho,b_0\rangle|,
\]
\[
b_\rho(u)=u^{-\rho}\int_u^\infty v^{\rho-1}b_0(v)\,dv,\qquad b_0=\Sigma h_0.
\]

HSW5 supplies the complete explicit source functions, and HSW6A gives proved two-sided bounds for this convergent whole-divisor sum by \(\sum_{\rm off}m_\rho|\Re\rho-1/2|/(1+(\Im\rho)^2)\). HSW7 recovers the entire off-critical divisor from the poles and residues of its meromorphic harmonic density. OPD2–OPD5 retains every original prime-dilation return and proves the exact source-pairing identity; those Hilbert norms are norms of canonical representatives, not quotient norms.

HCS returns the actual whole-family closure subspace \(B_{\rm off}\) to the original source sheaf, closed-supported localization and restriction pushout. It constructs the fixed-order critical lifts and the complete surviving off-critical Gamma residual, retaining both factors of \(1/2\), every endpoint/extra copy, and the intermediate cone's additional cyclic component. CHC6.7 proves its global finite-cutoff radical by the original summation-image synthesis and a complete contour shift. These calculations do not prove the harmonic value is zero or the required numerical weight separation. They identify its actual original-source return for the continuing calculation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
