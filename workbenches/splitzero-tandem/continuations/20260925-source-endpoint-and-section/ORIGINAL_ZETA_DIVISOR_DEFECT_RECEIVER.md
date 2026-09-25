# The actual specialization defect as a curvature of the original zeta

Complete derivation, **OZD0–OZD8**. This receiving calculation extends GTAH5; it does not claim that the positive defect trace was first constructed here.

## OZD0. Construction stage, original objects and the question

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Every scalar, analytic coordinate and coefficient operation in this note occurs after the complete-history arithmetic reconstruction. The two branches keep their own counters. No addition, arithmetic value, midpoint or metric is assigned to the support.

Let \(\mathscr Z\) be the set of distinct nontrivial zeros of the **original** \(\zeta(s)\), with their original multiplicities \(m_\rho\). Write \(\rho=\sigma+i\gamma\) and \(\rho^\#=1-\overline\rho\). The original functional equation gives \(m_{\rho^\#}=m_\rho\); it does not identify the two points. The source and its original quotient are
\[
\mathcal B=\{F\text{ entire}:\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|<\infty\text{ for every }A,N\},
\quad Q=\mathcal B/\mathcal I,
\tag{OZD0.1}
\]
where \(\mathcal I\) is the full vanishing-jet ideal, to order \(m_\rho\) at every \(\rho\). Put
\[
H=\ell^2(\mathscr Z,m_\rho),\quad (EF)_\rho=F(\rho),\quad
(Jx)_\rho=x_{\rho^\#},\quad
d_r(\rho)=e^{-i\gamma\log r}(r^\sigma-r^{1-\sigma}),\qquad r>1.
\tag{OZD0.2}
\]
Here and below evaluation of a class means evaluation of any representative. AST proves continuity of \(E\), and its full global isolators give every finitely supported value vector in its image. Its actual specialization boundary is
\[
\beta_r=D_r^*JE:Q\longrightarrow H_O,\qquad
\ker\beta_r=N_O,\qquad \mathcal R=Q/N_O,
\tag{OZD0.3}
\]
where \(D_r\) has multiplier \(d_r\), and \(H_O\) is the subspace of values at zeros with \(\Re\rho\ne1/2\). ADM retains its full source topology and common multiplier domain; GAP proves Gaussian approximation in that topology. Neither result replaces this boundary by its zero positive-transfer quotient.

For \(t>0\) use the actual source multiplier \(g_t(s)=e^{ts^2}\). The positive diagonal coefficient of
\((D_r^*JG_t)^*(D_r^*JG_t)\) is
\[
a_{r,t}(\rho)=q_r(\sigma)e^{2t(\sigma^2-\gamma^2)},\qquad
q_r(x)=(r^x-r^{1-x})^2=r^{2x}+r^{2-2x}-2r.
\tag{OZD0.4}
\]
Indeed \(J\) is a linear unitary involution, \(|d_r(\rho^\#)|^2=|d_r(\rho)|^2=q_r(\sigma)\), and hence the product is \(G_t^*D_r^*D_rG_t\). Keep the original divisor trace
\[
\mathcal E_r(t)=\sum_{\rho\in\mathscr Z}m_\rho q_r(\sigma)e^{2t(\sigma^2-\gamma^2)}.
\tag{OZD0.5}
\]
It is finite: \(0<\sigma<1\), \(q_r(\sigma)\le(r-1)^2\), and the full zero count \(\sum_{|\gamma|\le R}m_\rho=O(R\log(R+2))\) bounds the Gaussian series. GTAH5 already gives the related trace with \(e^{-t\gamma^2}\), including the distinction from the ordinary Hilbert trace. Formula (OZD0.5) keeps the exact additional factor \(e^{2t\sigma^2}\) of the source Gaussian.

The next question is an exact one: what does the original functional equation do to this actual boundary trace when the trace is received by \(\log|\zeta|\), with every pole and trivial zero still present? The following calculation answers it on the whole zero set.

## OZD1. Local divisor identity with its coefficient and sign

For \(s=x+iy\) use \(dA=dx\,dy\) and \(\Delta=\partial_x^2+\partial_y^2\). As distributions on \(\mathbb C\),
\[
\Delta\log|s-a|=2\pi\delta_a.
\tag{OZD1.1}
\]
Here is the coefficient computation. Integrate Green's identity over the support of a smooth compact test \(\psi\), with a disk of radius \(\varepsilon\) about \(a\) removed. On its inner boundary the outward normal for this punctured domain is minus the radial direction. The boundary integral for \(\int\log|s-a|\Delta\psi\) is
\[
\int_0^{2\pi}\{-\varepsilon\log\varepsilon\,\partial_r\psi(a+\varepsilon e^{i\theta})
+\psi(a+\varepsilon e^{i\theta})\}\,d\theta.
\]
It tends to \(2\pi\psi(a)\). The omitted disk integral tends to zero because \(\log|s-a|\) is locally integrable. This proves (OZD1.1).

A nonzero meromorphic function near \(a\) has the form \((s-a)^k u(s)\), where \(k\in\mathbb Z\) is its order and \(u\) is holomorphic and nowhere zero. On a small disk \(\log|u|\) is harmonic, being the real part of a holomorphic logarithm. Apply (OZD1.1) and a partition of unity. The original zeta, with its simple pole at \(1\) and its simple trivial zeros at \(-2,-4,\ldots\), consequently satisfies
\[
\boxed{\Delta\log|\zeta(s)|
=2\pi\left(\sum_{\rho\in\mathscr Z}m_\rho\delta_\rho
+\sum_{k\ge1}\delta_{-2k}-\delta_1\right).}
\tag{OZD1.2}
\]
All sums in this local distribution identity are locally finite. The usual original-zeta divisor facts and zero count used here are the same inputs retained in GTAH and AST, not RH or simplicity of the nontrivial zeros.

## OZD2. A global test domain, proved without discarding a boundary

We need tests compact in the real coordinate and Gaussian in the entire imaginary coordinate. We first prove the needed global integrability of the original logarithm. For every finite real interval \(K\),
\[
\int_{K\times[j,j+1]}|\log|\zeta(x+iy)||\,dx\,dy
\le C_K\log(|j|+2),\qquad j\in\mathbb Z.
\tag{OZD2.1}
\]

For completeness the required polynomial strip estimate can be obtained with all terms of Euler–Maclaurin. Define Bernoulli polynomials by
\(te^{ut}/(e^t-1)=\sum_{n\ge0}B_n(u)t^n/n!\), and write \((s)_j=s(s+1)\cdots(s+j-1)\), with \((s)_0=1\). For \(\Re s>1-2K_0\),
\[
\zeta(s)=\frac1{s-1}+\frac12
+\sum_{k=1}^{K_0}\frac{B_{2k}}{(2k)!}(s)_{2k-1}
-\frac{(s)_{2K_0}}{(2K_0)!}
\int_1^\infty B_{2K_0}(u-\lfloor u\rfloor)u^{-s-2K_0}\,du.
\tag{OZD2.2}
\]
To obtain the formula initially in \(\Re s>1\), integrate the Dirichlet sum against the counting staircase:
\(\zeta(s)=s\int_1^\infty\lfloor u\rfloor u^{-s-1}du\).
Use \(\lfloor u\rfloor=u-1/2-B_1(u-\lfloor u\rfloor)\). The resulting terms are \(1/(s-1)+1/2\) and \(-s\int B_1u^{-s-1}\). Integrate that last integral successively using \(B_n'=nB_{n-1}\). For \(n\ge2\), the values at the integer endpoints match, so the boundary terms telescope; the odd Bernoulli numbers above degree one vanish. The surviving endpoints give the displayed finite sum and the negative remainder with its full factor. Its integral converges locally uniformly for \(\Re s>1-2K_0\), which proves the continued identity there.

On any fixed strip \(a\le\Re s\le b\), choose \(K_0\) with \(a+2K_0>1\). The periodic Bernoulli factor is bounded, and its integral in absolute value is at most a constant divided by \(a+2K_0-1\). Thus the auxiliary **entire** function \(f(s)=(s-1)\zeta(s)\) has a polynomial bound in \(|\Im s|+1\) on that strip. This function is used only to prove the estimate; the pole of original \(\zeta\) is kept in every divisor formula.

At \(2+ij\), the absolutely convergent original reciprocal Dirichlet series gives
\[
|\zeta(2+ij)|\ge\frac1{\zeta(2)},\qquad
|f(2+ij)|\ge\frac{\sqrt{1+j^2}}{\zeta(2)}.
\tag{OZD2.3}
\]
The reciprocal series follows from multiplying the absolutely convergent prime factors, or from the Dirichlet inverse \(\sum\mu(n)n^{-s}\); its absolute sum is at most \(\zeta(2)\). This operation uses the completely reconstructed arithmetic and original series.

Choose a fixed disk radius \(R_K\) such that the disk centered at \(2+ij\) contains \(K\times[j,j+1]\) for every integer \(j\). The polynomial strip bound gives
\(\int_{D(2+ij,R_K)}\log^+|f|\le C\log(|j|+2)\).
The logarithm of a holomorphic function has the area submean inequality. It follows directly by factoring the finitely many zeros in each smaller closed disk: the circle average of \(\log|z-a|\) is \(\log\max(r,|a|)\), and the logarithm of the remaining nonzero factor has the mean-value property. Integrating the circle inequality in radius proves the area version. Therefore (OZD2.3) gives
\[
\int_{D(2+ij,R_K)}\log|f|\ge
\pi R_K^2\log|f(2+ij)|\ge-\pi R_K^2\log\zeta(2).
\]
Subtract this lower bound from the bound for the positive part to bound the negative part. Finally
\(\log|\zeta|=\log|f|-\log|s-1|\). The last logarithm is locally integrable and has an \(O(\log(|j|+2))\) absolute integral on the same rectangles. This proves (OZD2.1), including the rectangles meeting zeros or the pole.

It follows that every smooth \(\phi\) supported in a fixed real interval, whose derivatives through order two are bounded by a polynomial in \(|y|+1\) times \(e^{-c y^2}\) with \(c>0\), satisfies
\[
\int_{\mathbb C}\log|\zeta|\,\Delta\phi\,dA
=2\pi\left(\sum_\rho m_\rho\phi(\rho)
+\sum_{k\ge1}\phi(-2k)-\phi(1)\right).
\tag{OZD2.4}
\]
The integral is absolutely convergent. To prove the extension from compact tests, choose \(\theta\in C_c^\infty(\mathbb R)\), equal to one on \([-1,1]\), with support in \([-2,2]\), and put \(\theta_R(y)=\theta(y/R)\). The full derivative is
\[
\Delta(\phi\theta_R)=\theta_R\Delta\phi
+2\theta_R'\partial_y\phi+\theta_R''\phi.
\tag{OZD2.5}
\]
The last two terms are supported where \(R\le|y|\le2R\), have respectively factors \(R^{-1}\) and \(R^{-2}\), and their integrals against \(|\log|\zeta||\) tend to zero by (OZD2.1) and the Gaussian bound. Dominated convergence handles the first term. The full zero-count estimate and the same Gaussian bound handle the entire nontrivial-zero sum. The trivial-zero sum is finite because of real compact support. Thus every cutoff contribution has been calculated before taking the limit. No bounded zero calculation is used.

## OZD3. The exact original-zeta receiver of the positive boundary trace

Choose any real \(\eta\in C_c^\infty(\mathbb R)\) equal to one on a neighborhood of \([0,1]\). Define
\[
\phi_{r,t,\eta}(x,y)=\eta(x)q_r(x)e^{2t(x^2-y^2)}.
\tag{OZD3.1}
\]
It belongs to the proved test domain. Put \(h(x)=\eta(x)q_r(x)\) and \(L_r=\log r\). Retain the complete derivatives
\[
q_r'(x)=2L_r(r^{2x}-r^{2-2x}),\qquad
q_r''(x)=4L_r^2(r^{2x}+r^{2-2x}),
\tag{OZD3.2}
\]
\[
\Delta\phi_{r,t,\eta}
=e^{2t(x^2-y^2)}\left[h''+8txh'+16t^2(x^2+y^2)h\right],
\quad h'=\eta'q_r+\eta q_r',\quad
h''=\eta''q_r+2\eta'q_r'+\eta q_r''.
\tag{OZD3.3}
\]
In obtaining (OZD3.3), the \(+4th\) from the second real derivative and the \(-4th\) from the second imaginary derivative cancel exactly. No derivative of \(\eta\) is omitted.

Apply (OZD2.4), using \(\eta(\sigma)=1\) for every nontrivial zero. The exact result is
\[
\boxed{\mathcal E_r(t)=\frac1{2\pi}\int_{\mathbb C}
\log|\zeta(x+iy)|\,\Delta\phi_{r,t,\eta}(x,y)\,dx\,dy
+(r-1)^2e^{2t}
-\sum_{k\ge1}\eta(-2k)q_r(-2k)e^{8tk^2}.}
\tag{OZD3.4}
\]
The pole contribution and every trivial zero encountered by the real support are displayed. In particular a cutoff supported in \((-1/2,3/2)\) has no trivial-zero contribution because it is **zero at their actual locations**, not because zeta has been replaced by a completed function. Formula (OZD3.4) for arbitrary \(\eta\) proves the exact comparison when a wider cutoff includes them.

The result is independent of the chosen cutoff. Subtract the two instances of (OZD2.4): their difference vanishes at every nontrivial zero and at \(1\), so its logarithmic integral equals exactly the difference of the retained trivial-zero sums. This proves independence while keeping all terms.

## OZD4. Original-to-completed comparison with all factors restored

The programme source is the already established entire function
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{OZD4.1}
\]
Off its exceptional loci the full logarithmic comparison is
\[
\log|F_0(s)|=\log|s|+\log|s-1|-\log8
-\frac{x}{2}\log\pi+\log|\Gamma(s/2)|+\log|\zeta(s)|.
\tag{OZD4.2}
\]
Each term is locally integrable, so the identity holds as locally integrable functions and distributions across those loci. Gamma has a simple pole at each \(-2k\), \(k\ge0\), and no zero. Thus its full divisor comparison is
\[
\Delta\log|F_0|=\Delta\log|\zeta|
+2\pi\delta_0+2\pi\delta_1
-2\pi\sum_{k\ge0}\delta_{-2k}.
\tag{OZD4.3}
\]
The constant \(-\log8\) and affine term \(-x\log\pi/2\) have zero Laplacian; their zero contribution follows by differentiation. Combining (OZD4.3) with (OZD1.2) leaves exactly \(2\pi\sum_\rho m_\rho\delta_\rho\). The \(s=0\) cancellation and each trivial-zero cancellation occur between the explicitly displayed terms. The pole at \(1\) cancels with the explicitly displayed endpoint term. This is the comparison behind (OZD3.4); it is not permission to drop those terms from the original-zeta formula.

For compact tests all statements follow directly from OZD1. For the Gaussian tests, absolute logarithmic integrability of \(F_0\) also follows from the same disk argument: \(F_0\in\mathcal B\) bounds its positive logarithm on each fixed strip, while at \(2+iy\)
\[
|F_0(2+iy)|^2=
\frac{(4+y^2)(1+y^2)}{64\pi^2}
\frac{\pi y}{2\sinh(\pi y/2)}|\zeta(2+iy)|^2.
\tag{OZD4.4}
\]
The middle quotient has its continuous value one at \(y=0\). This equality follows from Gamma's reflection formula and recurrence, giving \(|\Gamma(1+iy/2)|^2=\pi y/(2\sinh(\pi y/2))\). With (OZD2.3), its logarithm is bounded below by \(-C(1+|y|)\). The area argument gives an \(O(1+|j|)\) bound for the absolute logarithm on unit-height rectangles. Equation (OZD4.2) then gives the same integrability for the Gamma term. Every Gaussian-tested comparison above is therefore justified by absolute convergence and the exact cutoff argument, not a formal integration at infinity.

## OZD5. What the original functional equation actually cancels

Let \(\mathsf R(x,y)=(1-x,y)\), and now choose \(\eta(1-x)=\eta(x)\). Such a smooth cutoff equal to one near \([0,1]\) exists; it can have any specified symmetric compact neighborhood as support. Keep
\[
L(s)=\log|\zeta(s)|,\quad
L_\pm=\tfrac12(L\pm L\circ\mathsf R),\quad
\phi_\pm=\tfrac12(\phi\pm\phi\circ\mathsf R).
\tag{OZD5.1}
\]
These are exact projection maps; \(L=L_++L_-\) and \(\phi=\phi_++\phi_-\). They are not coordinates or operations on \(\tau\).

Original zeta's functional equation, with the full multiplier, is
\[
\zeta(s)=\chi(s)\zeta(1-s),\qquad
\chi(s)=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}
=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s).
\tag{OZD5.2}
\]
Its real Dirichlet coefficients give \(|\zeta(1-s)|=|\zeta(1-\overline s)|\). Consequently
\[
L_-(s)=\tfrac12\log|\chi(s)|,
\tag{OZD5.3}
\]
as locally integrable functions, retaining all Gamma and power factors. The exact divisor of this multiplier is
\[
\frac1{2\pi}\Delta\log|\chi|
=\sum_{k\ge0}\delta_{-2k}-\sum_{k\ge0}\delta_{1+2k}.
\tag{OZD5.4}
\]
This follows from the simple Gamma poles in the quotient: the numerator has poles at \(1,3,5,\ldots\), and the reciprocal denominator has zeros at \(0,-2,-4,\ldots\). The exponential power of \(\pi\) has no divisor. Alternatively it follows by subtracting the reflected original divisor identity; the nontrivial terms cancel by their actual involution and equal multiplicities.

The reflection \(\mathsf R\) preserves area, and its pullback commutes with \(\Delta\). The integrals are absolutely convergent by OZD2 and (OZD5.3). The even–odd cross terms therefore vanish by change of variables. In particular
\[
\frac1{2\pi}\int L\Delta\phi\,dA
=\frac1{2\pi}\int L_+\Delta\phi_+\,dA
+\frac1{4\pi}\int\log|\chi|\Delta\phi_-\,dA.
\tag{OZD5.5}
\]
The last term has been determined exactly, not assigned a sign:
\[
\frac1{4\pi}\int\log|\chi|\Delta\phi_-\,dA
=\sum_{k\ge0}\phi_-(-2k)
=-\phi_-(1)+\sum_{k\ge1}\phi_-(-2k).
\tag{OZD5.6}
\]
Indeed \(\phi_-(1+2k)=-\phi_-(-2k)\), so the two sums in (OZD5.4) have precisely this difference and factor. The sums are finite, and the same global cutoff proof applies.

In (OZD3.4), decompose the pole and trivial-zero terms using \(\phi=\phi_++\phi_-\), then insert (OZD5.5)–(OZD5.6). The entire odd contribution cancels **with its known pole and trivial-zero terms**. The resulting exact identity is
\[
\boxed{\mathcal E_r(t)=\frac1{2\pi}\int_{\mathbb C}L_+\Delta\phi_+\,dA
+\phi_+(1)-\sum_{k\ge1}\phi_+(-2k).}
\tag{OZD5.7}
\]
No reflected zero pair was removed: its two contributions to (OZD0.5) add. In particular
\[
\phi_+(1)=\frac{(r-1)^2}{2}(e^{2t}+1),\qquad
\phi_-(1)=\frac{(r-1)^2}{2}(e^{2t}-1).
\tag{OZD5.8}
\]
For support in \((-1/2,3/2)\) the finite sums in (OZD5.6)–(OZD5.7) are empty, and both displayed endpoint quantities remain. The exact symmetric potential is
\(L_+(s)=\tfrac12\log|\zeta(s)\zeta(1-\overline s)|\); thus (OZD5.7) remains a formula in original zeta, not a completed working replacement.

## OZD6. Faithfulness on the actual boundary and its full source kernel

For fixed \(r>1,t>0\), every summand in (OZD0.5) is nonnegative and its Gaussian factor is strictly positive. Since \(x\mapsto r^x\) is strictly increasing,
\[
\mathcal E_r(t)=0
\quad\Longleftrightarrow\quad
d_r(\rho)=0\text{ for every original }\rho
\quad\Longleftrightarrow\quad\beta_r=0
\quad\Longleftrightarrow\quad\mathcal R=0.
\tag{OZD6.1}
\]
For the second equivalence, one direction follows from the formula for \(\beta_r\); the other uses each actual global value isolator in \(Q\), so a nonzero coordinate multiplier cannot annihilate the whole source. The final equivalence is the proved exact kernel statement (OZD0.3). Thus the positive trace detects the actual boundary, rather than the zero seminorm of a chosen positive completion.

The local trace comparison specifies the retained jet data. At each original zero there is the exact row
\[
0\longrightarrow(h)/(h^{m_\rho})\longrightarrow
\mathbb C[h]/(h^{m_\rho})\xrightarrow{\ h\mapsto0\ }\mathbb C\longrightarrow0.
\tag{OZD6.2}
\]
Multiplication by a holomorphic germ \(b(\rho+h)\) on the middle term has diagonal \(b(\rho)\) repeated \(m_\rho\) times, with its higher Taylor coefficients still present above or below that diagonal according to the ordered basis convention. Its trace is \(m_\rho b(\rho)\). The evaluation map has kernel precisely the displayed nilpotent ideal. Globally \(E\) has kernel \(N_0\). Therefore the divisor trace is a specified value receiver of the original full-jet construction; it does not claim that the jet kernel is zero. The source boundary \(\beta_r\) uses that same value receiver and its exact kernel \(N_O\), so (OZD6.1) makes no stronger faithfulness claim about the full jets.

For the nonholomorphic coefficient \(a_{r,t}(\rho)\), the positive divisor trace in (OZD0.5) is defined on the diagonal values, as in GTAH5. It is not a claim that this coefficient is an entire test for a holomorphic prime explicit formula. OZD1–OZD5 supply its actual distributional receiver and prove its domain, including the required endpoint corrections.

## OZD7. The next attempt from the combined source and symmetry results

GAP's Gaussian maps approximate identity on the original quotient and its actual boundary. ADM's separator acts as identity on that same boundary. SPF/SMC classify positive transfer receivers and prove that their quotient kernels can erase the whole actual boundary. These established facts make the faithful trace in (OZD6.1) a relevant next test.

The attempted cancellation through the **original** functional equation has now been computed: its whole antisymmetric contribution is (OZD5.6), already accounted for by the original pole and trivial-zero terms. The surviving symmetric receiver is exactly (OZD5.7). In a narrow cutoff its asserted vanishing would require the definite integral to equal
\(-\pi(r-1)^2(e^{2t}+1)\), with the \(1/(2\pi)\) in (OZD5.7) retained. That equality has not been substituted for a proof.

The subsequent actual calculation is the operator trace of the original degree action on this same energy. GDE computes the pair contributions, cyclic traces, determinants and the full Gaussian source limit. This tests whether the geometric degree relation supplies the cancellation missing from the scalar functional equation. OZD does not infer that all geometric receivers fail; it has calculated this receiver and the exact term it preserves. The original weight-separated vanishing goal remains active.

## OZD8. Sources and proof provenance

The local distribution lemma and the global Euler–Maclaurin/logarithmic estimate are proved in OZD1–OZD2. No assertion of novelty is made for those classical identities. Their new receiving calculation is OZD3–OZD7 on the existing specialization boundary and source Gaussian. The original-zeta functional equation, divisor and zero count are the previously retained human-source inputs; all multipliers used from them are written above.

Programme proof dependencies include [GTAH0–GTAH6, especially the earlier positive trace in GTAH5](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/geometric-positive-quotient/GEOMETRIC_TRANSFER_POSITIVE_ADJOINT_DEFECT.md) and [AST0–AST9, especially the actual boundary and its kernel in AST2](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/geometric-positive-quotient/ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md). The immutable public files were retrieved and compared: GTAH is byte-identical; AST's sole textual change repairs a dependency link, with its mathematical proof unchanged.

The complete [GAP0–GAP9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/GAUSSIAN_FULL_SOURCE_APPROXIMATION.md) and [ADM0–ADM9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md) proofs and audits accompany this subsequent edition; they are not represented as included in the preceding public cutoff. Their original source and global-isolator dependencies are retained. SPF/SMC enter only the attempted-repair account in OZD7. Full exact source copies and reading hashes accompany the cumulative edition. The canonical literature index was queried before this derivation; its routing record is private and is not represented as reading any returned paper. Original author TeX remains the literature-reading requirement.
