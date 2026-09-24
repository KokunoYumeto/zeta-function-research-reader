# Global synthesis for the original-zeta Mellin quotient

Independent derivation, 24 September 2026. This note proves the equality left open in M9 of `PRIME_MONODROMY_STACKED_HISTORY.md`. It uses no RH assumption, no simplicity assumption, no bounded numerical experiment, and no assumed lower bound for zeta inside the critical strip. Addition at source tau is not used. The user's state-layer notation is unchanged.

## Source identity and actual reading

The existing machine-readable corpus index was queried before consulting further literature: `canonical research literature index (private routing database)`, table `canonical_units`, for spectral/zeta, spectral synthesis, Hadamard, and explicit-formula routing. Routing records were not treated as proofs. The relevant retained original author source is Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, [arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), original TeX `sources/2602.04022v1/author/rhready.tex`, SHA256 `7f1888d82b42263faca4264f3f9fc77e5750c348640f85db0ac4569fe88ebab2`. The author identity and version were checked against arXiv. Original TeX lines 501–546 and 1570–1600 were read; the theorem actually used is Hadamard factorization at lines 526–535. The source's subsequent symmetric-product presentation is not substituted for the full genus-one product used below. Its historical attribution is J. Hadamard, *Essai sur l'étude des fonctions données par leur développement de Taylor*, J. Math. Pures Appl. \(4\) 8 \(1892\), 101–186. That historical article was not newly read in this derivation.

The retained programme sources read here are M8–M9 in full, with the preceding M6–M7 context, and the C6 kernel formula cited there. The full original-zeta multiplier is preserved below, including its factor 1/8. Hadamard factorization is the standard complex-analysis theorem used; the division estimate needed for this particular space is proved here instead of assumed.

## S1. The exact function spaces and Mellin isomorphism

Write
\[
\mathcal A=\left\{k\in C^\infty(\mathbb R_{>0}):
p_{N,j}(k):=\sup_{u>0}(u^N+u^{-N})
\left|(u\partial_u)^j k(u)\right|<\infty\quad(N,j\ge0)\right\}.
\tag{S1.1}
\]
All indices in these seminorms are nonnegative integers. In the logarithmic coordinate \(x=\log u\), put \(K(x)=k(e^x)\). The topology is equivalently given by
\[
\|K\|_{N,j}=\sup_{x\in\mathbb R}e^{N|x|}|K^{(j)}(x)|.
\tag{S1.2}
\]
The equivalence follows from

\(e^{N|x|}\le e^{Nx}+e^{-Nx}\le2e^{N|x|}\).

Let \(\mathcal B\) be the space of entire functions \(F\) for which
\[
b_{A,M}(F)=\sup_{|\sigma|\le A,\ t\in\mathbb R}
(1+|t|)^M|F(\sigma+it)|<\infty
\quad(A,M\ge0).
\tag{S1.3}
\]
The centered Mellin map
\[
\mathcal M k(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u}
=\int_{\mathbb R}K(x)e^{(s-1/2)x}\,dx
\tag{S1.4}
\]
is a linear topological isomorphism \(\mathcal A\to\mathcal B\).

Here are the estimates and inverse. On each fixed real strip the integral and every derivative in \(s\) are absolutely convergent, because an arbitrary polynomial in \(x\) times \(e^{(\sigma-1/2)x}\) is controlled by a larger seminorm (S1.2). Repeated integration by parts in \(x\), applied to \(e^{(\sigma-1/2)x}K(x)\), proves (S1.3), uniformly in the strip. Boundary terms vanish by (S1.2). This proves continuity of the map.

For \(F\in\mathcal B\), define
\[
K(x)=\frac1{2\pi}\int_{\mathbb R}F(1/2+it)e^{-itx}\,dt.
\tag{S1.5}
\]
For any real \(c\), contour shifting in a finite vertical strip gives
\[
K(x)=\frac{e^{-(c-1/2)x}}{2\pi}
\int_{\mathbb R}F(c+it)e^{-itx}\,dt.
\tag{S1.6}
\]
Indeed, the horizontal sides of the rectangle for \(F(s)e^{-(s-1/2)x}\) tend to zero by (S1.3), uniformly between its two vertical sides. Differentiation \(j\) times inserts the exact factor \(-(c-1/2+it)\)^j in the integral. For \(x\ge0\) choose \(c=1/2+N+1\), and for \(x\le0\) choose \(c=1/2-N-1\). Integrability with \(M>j+1\) proves (S1.2) and continuity of the inverse. Fourier inversion gives (S1.4) on the line \(c=1/2\); the identity theorem gives it everywhere. The sign and constant in (S1.5) are fixed throughout.

Both spaces are complete metrizable locally convex spaces. For \(\mathcal A\), a Cauchy sequence in all seminorms converges in \(C^\infty\) on each compact interval; the weighted uniform limits give the same limit with every seminorm finite and convergence in every seminorm. The corresponding assertion for \(\mathcal B\) follows from this proved isomorphism (or from locally uniform holomorphic convergence together with the strip bounds).

## S2. One retained source kernel, with every factor

Set
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
k_0(u)=\mathcal E f_0(u)=u^{1/2}\sum_{n\ge1}f_0(nu).
\tag{S2.1}
\]
The even Schwartz function \(f_0\) satisfies \(f_0(0)=0\) and \(\int_{\mathbb R}f_0=0\). The Gaussian moments give the latter directly:
\[
\int v^2e^{-\pi v^2}dv=\frac1{2\pi},\quad
\int v^4e^{-\pi v^2}dv=\frac3{4\pi^2},\quad
\frac\pi2\left(2\pi\frac3{4\pi^2}-3\frac1{2\pi}\right)=0.
\]
For the Fourier convention \(\widehat f(t)=\int f(v)e^{-2\pi ivt}dv\), the Gaussian identity and differentiation give
\[
\widehat{v^2e^{-\pi v^2}}(t)=\left(\frac1{2\pi}-t^2\right)e^{-\pi t^2},
\]
\[
\widehat{v^4e^{-\pi v^2}}(t)=
\left(t^4-\frac3\pi t^2+\frac3{4\pi^2}\right)e^{-\pi t^2}.
\]
Substituting into (S2.1) proves \(\widehat f_0=f_0\). Poisson summation, with both endpoint terms zero, consequently proves \(k_0(u)=k_0(1/u)\). It also proves \(k_0\in\mathcal A\), as in M9.

For \(\Re s>1\), the absolutely convergent Mellin calculation is
\[
F_0(s):=\mathcal M k_0(s)
=\zeta(s)\int_0^\infty f_0(v)v^{s}\frac{dv}{v}
=\boxed{\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)}.
\tag{S2.2}
\]
For precision, the integral before the last equality equals
\[
\frac\pi2\left[
2\pi\cdot\frac12\pi^{-(s+4)/2}\Gamma((s+4)/2)
-3\cdot\frac12\pi^{-(s+2)/2}\Gamma((s+2)/2)
\right].
\]
Applying \(\Gamma(z+1)=z\Gamma(z)\) twice gives exactly the factor in (S2.2). Thus \(F_0=\xi/4\) for the source's definition of \(\xi\); no factor is absorbed. The Mellin integral makes \(F_0\) entire, and \(k_0(u)=k_0(1/u)\) gives \(F_0(s)=F_0(1-s)\).

The apparent endpoint and trivial-zero singularities in the displayed multiplier have the following explicit values:
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2m)=F_0(1+2m)
=\frac{(1+2m)(2m)}8\pi^{-(1+2m)/2}
\Gamma((1+2m)/2)\zeta(1+2m)\ne0\quad(m\ge1).
\tag{S2.3}
\]
At \(1\), the zeta residue is \(1\) and \(\pi^{-1/2}\Gamma(1/2)=1\); the value at \(0\) follows also by the functional equation. At every negative even integer the reflection gives the positive, finite expression in (S2.3). The Gamma factor has no zeros. Consequently the zeros of \(F_0\), with their orders, are exactly the nontrivial zeros of the ORIGINAL zeta function. Trivial zeros are cancelled in this auxiliary transform, with their values explicitly retained in (S2.3); S6 below recovers their full derivative data in the approximating source functions.

We also need the order of \(F_0\), for which no zero-distribution hypothesis is required. There exist \(B,c,C>0\) such that
\[
|k_0(u)|\le C u^B e^{-cu^2}\quad(u\ge1).
\]
This follows by summing the Gaussian series (S2.1), retaining a smaller positive Gaussian exponent to absorb its polynomial factors. Reflection supplies the other endpoint. Thus for \(|s|\le R\),
\[
|F_0(s)|\le2C\int_1^\infty u^{B+R+1/2}e^{-cu^2}\frac{du}{u}
\le \exp(C_1(R+2)\log(R+2)).
\tag{S2.4}
\]
The last bound follows by the Gamma integral after \(y=cu^2\); alternatively its maximum at \(y\) proportional to \(R+2\) and the remaining exponential tail give the same bound. Thus \(F_0\) has order at most \(1\). It is not zero, since \(F_0(2)=\pi/24\).

Jensen's formula at radius (2R), using \(F_0(0)=1/8\ne0\), now gives a constant \(C_2\) such that the zero count, with multiplicities, obeys
\[
n(R)\le C_2(R+2)^{3/2}\quad(R\ge1).
\tag{S2.5}
\]
Indeed each zero of modulus at most \(R\) contributes at least \(\log2\) to Jensen's sum at (2R), and (S2.4) is bounded by a constant times \((R+2)^{3/2}\). Hadamard's factorization theorem in the retained original TeX then gives
\[
F_0(s)=e^{a+bs}\prod_\rho
\left(1-\frac{s}{\rho}\right)e^{s/\rho},
\qquad e^a=\frac18,\quad b=\frac{F_0'(0)}{F_0(0)}.
\tag{S2.6}
\]
The product retains every repeated zero and every exponential factor. The value of \(b\) is exactly \(\tfrac12\log(4\pi)-1-\tfrac12\gamma\), as follows by expanding all factors of (S2.2) at \(0\); no value of \(b\) is needed to discard a term below. Formula (S2.5) implies convergence of \(\sum_\rho |\rho|^{-2}\), so the product in (S2.6) converges absolutely on compact subsets after its genus-one factors are grouped as displayed.

## S3. Global division with a proved subquadratic growth bound

Let \(F\in\mathcal B\) vanish at every zero \(\rho\) of \(F_0\) to at least the exact multiplicity \(m_\rho\). Then
\[
Q(s)=F(s)/F_0(s)
\tag{S3.1}
\]
extends to an entire function. This follows from Taylor division at each zero; the extensions agree with the quotient on punctured neighborhoods.

For every \(A\ge0\) there are constants \(C_{A,F},C>0\) such that
\[
\sup_{|\sigma|\le A}|Q(\sigma+it)|
\le C_{A,F}\exp\!\left(C(|t|+2)^{3/2}
\log(|t|+2)\right),\qquad t\in\mathbb R.
\tag{S3.2}
\]
The supremum is over the real coordinate at the fixed imaginary coordinate \(t\). This incorporates the independently verified notation correction in GLOBAL_MELLIN_SYNTHESIS_REVIEW.md R1.1. The exponent is strictly subquadratic. This is a statement on the whole unbounded strip, not a finite interval estimate.

We prove the bound including neighborhoods of arbitrarily close or multiple zeros. Fix a large \(R\). Around each zero with \(|\rho|\le8R\), take the disk of radius \(R^{-2}\), and let \(D_R\) be their union. By (S2.5) the sum of the radii, counted with multiplicity if necessary, is at most \(C R^{-1/2}\). For sufficiently large \(R\), each connected component of this finite union has diameter less than \(1\): a chain of intersecting disks joining two points has total diameter at most twice the sum of the radii in that chain.

For \(R/2\le|s|\le3R\) outside \(D_R\), use (S2.6). For the factors with \(|\rho|\le8R\),
\[
\left|1-\frac{s}{\rho}\right|
=\frac{|s-\rho|}{|\rho|}\ge\frac1{8R^3}.
\tag{S3.3}
\]
Their logarithms contribute at least \(-C R^{3/2}\log R\). The exponential parts contribute at least
\[
-|s|\sum_{|\rho|\le8R}|\rho|^{-1}\ge-C R^{3/2}.
\tag{S3.4}
\]
The last inequality follows by partial summation of (S2.5); the finitely many small zeros are harmless because \(F_0(0)\ne0\), so their moduli have a positive lower bound.

For \(|\rho|>8R\), the ratio \(w=s/\rho\) has \(|w|\le3/8\). The absolutely convergent logarithmic series gives
\[
\log|(1-w)e^w|
=\Re\left(-\sum_{j\ge2}\frac{w^j}{j}\right)
\ge-C|w|^2.
\]
Partial summation again gives
\[
\sum_{|\rho|>8R}|\rho|^{-2}\le C R^{-1/2}.
\]
Therefore the tail contributes at least \(-C R^{3/2}\). Finally \(e^{a+bs}\) contributes at least \(-|a|-3|b|R\). Altogether,
\[
|F_0(s)|\ge\exp(-C R^{3/2}\log R)
\quad(R/2\le|s|\le3R,\ s\notin D_R).
\tag{S3.5}
\]

Now take \(R\le|s|\le2R\) with \(|\Re s|\le A\). Outside \(D_R\), (S3.5) and the boundedness of \(F\) on the strip give the desired bound for \(Q\). Inside \(D_R\), the whole component containing \(s\) stays within distance \(1\) of \(s\). Its boundary lies in the strip \(|\Re z|\le A+1\), in the larger annulus used in (S3.5), and outside the open disk union. The same bound holds for \(Q\) on that boundary. Since \(Q\) is holomorphic even at all enclosed zeros, the maximum-modulus principle gives the bound inside. No zero spacing or simplicity has been assumed. Taking dyadic \(R\) proves (S3.2); the remaining compact region is bounded by continuity.

## S4. Gaussian division produces actual source functions

For every \(\varepsilon>0\), define the entire function
\[
Q_\varepsilon(s)=e^{\varepsilon(s-1/2)^2}Q(s).
\tag{S4.1}
\]
On the strip \(|\Re s|\le A\),
\[
|e^{\varepsilon(s-1/2)^2}|
\le e^{\varepsilon(A+1/2)^2}e^{-\varepsilon(\Im s)^2}.
\]
Together with (S3.2), this proves \(Q_\varepsilon\in\mathcal B\): for every fixed strip and every polynomial power, the negative quadratic dominates \(C|t|^{3/2}\log|t|\). The source preimage \(q_\varepsilon\in\mathcal A\) is therefore explicitly
\[
q_\varepsilon(e^x)=\frac1{2\pi}\int_{\mathbb R}
Q_\varepsilon(1/2+it)e^{-itx}\,dt.
\tag{S4.2}
\]

Let multiplicative convolution be
\[
(k*q)(u)=\int_0^\infty k(u/a)q(a)\frac{da}{a}.
\tag{S4.3}
\]
All such integrals and their logarithmic derivatives converge in \(\mathcal A\), because in logarithmic coordinate

\(e^{N|x|}\le e^{N|x-y|}e^{N|y|}\)

and the second factor is integrable against a seminorm with one additional exponential weight. The Mellin transform of (S4.3) is the product of Mellin transforms, with Fubini justified by the same bounds.

Define, retaining the full unitary factor of the source dilation,
\[
U_a f(v)=a^{-1/2}f(v/a),\qquad
f_\varepsilon(v)=\int_0^\infty q_\varepsilon(a)U_a f_0(v)\frac{da}{a}.
\tag{S4.4}
\]
This is an actual even Schwartz function. For a Schwartz seminorm \(\sup_v |v|^r|\partial_v^j f(v)|\), substitution \(v=aw\) bounds the corresponding seminorm of \(U_a f_0\) by

\(a^{r-j-1/2}\sup_w|w|^r|f_0^{(j)}(w)|\).

Every such power is integrable against \(q_\varepsilon(a)da/a\), by its arbitrary endpoint decay. This proves convergence in every Schwartz seminorm and permits all required differentiations. Evenness is preserved. Moreover
\[
f_\varepsilon(0)=0,
\qquad
\int_{\mathbb R}f_\varepsilon(v)dv
=\int_0^\infty q_\varepsilon(a)a^{1/2}\frac{da}{a}
\int_{\mathbb R}f_0(w)dw=0.
\tag{S4.5}
\]
Absolute convergence follows also from \(\|U_a f_0\|_1=a^{1/2}\|f_0\|_1\). Thus \(f_\varepsilon\in\mathcal S_0^{\rm even}\), the actual source space in M9.

The continuity \(\mathcal E:\mathcal S_0^{\rm even}\to\mathcal A\) follows directly from the estimates already used in M9. More explicitly, at \(u\ge1\) the differentiated series is bounded using a sufficiently high Schwartz seminorm and the convergent sum \(\sum n^{-M}\), \(M>1\); at \(u\le1\), Poisson gives \(\mathcal E f(u)=\mathcal E\widehat f(1/u)\), and Fourier transformation is continuous on Schwartz space. Consequently (S4.4), or direct absolute summation, gives the exact receiver identity
\[
\boxed{\mathcal E f_\varepsilon=k_0*q_\varepsilon.}
\tag{S4.6}
\]
It has Mellin transform
\[
\mathcal M\mathcal E f_\varepsilon(s)
=F_0(s)Q_\varepsilon(s)
=e^{\varepsilon(s-1/2)^2}F(s).
\tag{S4.7}
\]
Every source, domain and multiplier in this construction is specified; the argument has not inserted a hypothetical division preimage.

## S5. Exact global closure equality

Let
\[
\mathcal I_\zeta=
\left\{k\in\mathcal A:
(\mathcal M k)^{(j)}(\rho)=0
\text{ for every nontrivial zero }\rho
\text{ and every }0\le j<m_\rho\right\}.
\tag{S5.1}
\]
Then
\[
\boxed{
\overline{\mathcal E(\mathcal S_0^{\rm even})}^{\mathcal A}
=\mathcal I_\zeta.
}
\tag{S5.2}
\]

The inclusion from left to right is M9's original-zeta Mellin identity and continuity of every jet. For completeness, on \(\Re s>1\),
\[
\mathcal M\mathcal E f(s)
=\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}.
\]
The last integral is holomorphic on \(\Re s>-2\), since \(f\) is even and \(f(0)=0\). Its value at \(1\) is zero, cancelling the simple pole of zeta. Continuation into the critical strip therefore proves vanishing at every original nontrivial-zero jet of the required orders. Those functionals are continuous on \(\mathcal A\), so the closed image is contained in (S5.1).

For the reverse inclusion, take any \(k\in\mathcal I_\zeta\), let \(F=\mathcal M k\), and construct \(f_\varepsilon\) by S3–S4. Formula (S4.7) is the transform of logarithmic Gaussian convolution. Precisely, put
\[
g_\varepsilon(x)=\frac1{\sqrt{4\pi\varepsilon}}
e^{-x^2/(4\varepsilon)}.
\tag{S5.3}
\]
The full Gaussian integral gives
\[
\int_{\mathbb R}g_\varepsilon(x)e^{(s-1/2)x}dx
=e^{\varepsilon(s-1/2)^2}.
\]
Thus Mellin injectivity proves
\[
(\mathcal E f_\varepsilon)(e^x)=(g_\varepsilon*K)(x),
\qquad K(x)=k(e^x).
\tag{S5.4}
\]

These convolutions tend to \(K\) in every seminorm (S1.2). Here is a weighted proof, so that a weaker \(L^2\) convergence is not substituted. For each (N,j), the fundamental theorem of calculus gives
\[
\|K(\,\cdot-y)-K\|_{N,j}
\le |y|e^{N|y|}\|K\|_{N,j+1}.
\tag{S5.5}
\]
Indeed write the derivative difference as the integral of \(K^{(j+1)}(x-r)\) from \(r=0\) to \(r=y\), and use \(e^{N|x|}\le e^{N|x-r|}e^{N|r|}\). Therefore
\[
\|g_\varepsilon*K-K\|_{N,j}
\le\|K\|_{N,j+1}
\int_{\mathbb R}g_\varepsilon(y)|y|e^{N|y|}dy
\longrightarrow0.
\tag{S5.6}
\]
After \(y=\sqrt\varepsilon z\), the last integral is bounded for \(0<\varepsilon\le1\) by \(\sqrt\varepsilon\) times the finite integral of \(|z|e^{N|z|}e^{-z^2/4}/\sqrt{4\pi}\). This proves the asserted limit. Every approximant (S5.4) lies in the actual image by (S4.4)–(S4.6), proving the reverse inclusion globally.

The parameter \(\varepsilon\downarrow0\) is an explicit approximation to the identity on the entire space. It is not a restriction to finitely many zeros, a finite prime range, or an assumed convergence of a numerical experiment.

## S6. Exceptional points, source jets and endpoint recovery

The full construction retains the information at the places cancelled by the auxiliary factor \(F_0\). Put
\[
F_\varepsilon(s)=e^{\varepsilon(s-1/2)^2}F(s).
\]
The original, uncompleted zeta relation is
\[
\int_0^\infty f_\varepsilon(v)v^s\frac{dv}{v}
=\frac{F_\varepsilon(s)}{\zeta(s)}
\quad(\Re s>1),
\tag{S6.1}
\]
with meromorphic continuation retaining all terms.

For an even Schwartz function with \(f(0)=0\), subtracting its Taylor polynomial on \(0<v<1\) proves that its Mellin integral extends meromorphically to the whole plane. The only possible poles are simple poles at (-2m), \(m\ge1\), and their residues are \(f^{(2m)}(0)/(2m)!\). Indeed, the subtracted remainder \(O(v^{2M+2})\) gives a holomorphic integral on \(\Re s>-2M-2\), while each subtracted monomial contributes exactly \(f^{(2m)}(0)/((2m)!(s+2m))\). As \(M\) increases these continuations agree on their common domains.

At the simple trivial zero (-2m), (S6.1) consequently gives
\[
\boxed{
\frac{f_\varepsilon^{(2m)}(0)}{(2m)!}
=\frac{e^{\varepsilon(-2m-1/2)^2}F(-2m)}{\zeta'(-2m)}
\quad(m\ge1).
}
\tag{S6.2}
\]
This can also be checked directly from (S4.4): its (2m)-th derivative at \(0\) multiplies the coefficient of \(f_0\) by \(Q_\varepsilon(-2m)\); (S2.2) identifies that coefficient as \(F_0(-2m)/\zeta'(-2m)\). The trivial zeros are simple because the sine factor in the zeta functional equation has a simple zero there, whereas \(\Gamma(1+2m)\zeta(1+2m)\) is finite and nonzero. Equivalently, the finite nonzero value in (S2.3), together with the simple Gamma pole, gives the same conclusion.

At \(s=1\), since \(\zeta(s)=(s-1)^{-1}+O(1)\), the Mellin integral in (S6.1) has the exact expansion
\[
\int_0^\infty f_\varepsilon(v)v^s\frac{dv}{v}
=(s-1)F_\varepsilon(1)+O((s-1)^2).
\tag{S6.3}
\]
Its value is the required zero integral, and its first derivative records \(F_\varepsilon(1)\). At \(s=0\), \(\zeta(0)=-1/2\) gives
\[
\int_0^\infty f_\varepsilon(v)\frac{dv}{v}
=-2F_\varepsilon(0).
\tag{S6.4}
\]
The integral converges because \(f_\varepsilon(v)=O(v^2)\). No endpoint value of the receiver has been discarded merely because the source has zero endpoint constraints.

## S7. The resulting faithful receiver and its remaining mathematical role

By (S5.2), the joint actual-zero jet map has exactly the original closed image as its kernel:
\[
J:\mathcal A\longrightarrow
\prod_{\rho}\mathbb C^{m_\rho},
\qquad J(k)=\bigl((\mathcal M k)^{(j)}(\rho)\bigr)_{\rho,\,0\le j<m_\rho},
\]
\[
\ker J=\overline{\mathcal E(\mathcal S_0^{\rm even})}^{\mathcal A}.
\tag{S7.1}
\]
Thus \(J\) induces an injective linear map
\[
\boxed{
\mathcal Q\hookrightarrow\prod_\rho\mathbb C^{m_\rho}.
}
\tag{S7.2}
\]
Its image is \(J(\mathcal A)\), with the quotient topology if a topological isomorphism is desired. No claim that this image is the entire product, or is closed in the product topology, is made. The conclusion proved here is stronger than the prior existence of some descending zero functionals: **all actual zero jets together now distinguish every class in the quotient**. There is no additional quotient class invisible to every original zeta zero and its retained multiplicities.

The scaling action remains exactly
\[
J_{\rho,j}(V_a k)=a^{\rho-1/2}
\sum_{\ell=0}^j\binom j\ell(\log a)^{j-\ell}J_{\rho,\ell}(k).
\tag{S7.3}
\]
Thus the quotient has been identified using the actual zeta spectral data, including its full triangular multiplicity action. This theorem does not force \(\Re\rho=1/2\): it does not insert a positive definite norm on this quotient, and it does not assert that (S7.3) is unitary. M9's proof that the image is dense in the ordinary \(L^2(du/u)\) space still holds. The faithful jet receiver (S7.2), its finer topology, and the zero Hilbert quotient are all retained with their exact maps.

Finally, let \(C_{\rm rec}\) and the free support space \(\mathbb C^{(\mathcal L)}\) be exactly those of M9.7. Tensoring (S7.2) algebraically with these coefficient spaces gives an injective linear map: a finite basis expansion reduces the assertion to injectivity of \(J\) in each coordinate. This statement concerns the linear spaces after passage to tensors. That preceding passage identifies \(0_{\mathcal Q}\otimes e_\ell\) for every label, so it does not retain a support record at coefficient zero. The two coefficient sections are distinct maps, with the same zero value.

The exact repair is the disjoint family \(\widehat{\mathcal Q}=\coprod_{\ell\in\mathcal L}\{\ell\}\times\mathcal Q\), with \(\widehat J(\ell,q)=(\ell,Jq)\). This is injective because equality first retains the label and then determines the coefficient through S7.2. Its coefficient-zero fibre retains every \((\ell,0_{\mathcal Q})\). The map \((\ell,q)\mapsto q\otimes e_\ell\) is the explicit comparison to the old receiver: its zero fibre is that entire labelled family and every nonzero fibre in its image is a singleton. All arithmetic operators and projectors act on q while retaining the label. Section selections through \([\tau]\) and ([1]) can be included in the existing record as proved in SUPPORT_ZERO_RECEIVER_REPAIR.md ZR5. ZR1-ZR5 supply the complete proofs and the exact full-pairing map, incorporating the receiving task's I26.10 correction. No source addition or integer parity is assigned to \(\tau\).

The proof diagram is
\[
\begin{array}{ccc}
F\in\mathcal B,\ J(F)=0
&\xrightarrow{\quad /F_0\quad}&Q\text{ entire}\;\bigl(\log|Q|=O_A(|t|^{3/2}\log|t|)\bigr)\\
\big\downarrow\times e^{\varepsilon(s-1/2)^2}
&&\big\downarrow\times e^{\varepsilon(s-1/2)^2}\\
F_\varepsilon=F_0Q_\varepsilon
&\xleftarrow{\quad\mathcal M\quad}&
\mathcal E f_\varepsilon=k_0*q_\varepsilon,
\end{array}
\]
with \(F_\varepsilon\to F\) in \(\mathcal B\) proved through the equivalent \(\mathcal A\) convergence (S5.6). Every arrow is constructed above on its full domain.


## Subsequent exact-image theorem, 24 September 2026

The complete proof in [EXACT_SCHWARTZ_SUMMATION_IMAGE.md](EXACT_SCHWARTZ_SUMMATION_IMAGE.md),
SSI1–SSI7, independently checked in ESI0–ESI10, strengthens S5 to the
actual equality E(S)=I_zeta and proves a continuous inverse. Its raw
summation convention is Sigma f=2 sum f(nu); the exact centered comparison
is SSI6.4. Thus S4's Gaussian source approximants converge in Schwartz
space to the actual inverse, not only after summation. S1–S7 above remain
the complete historical proof of the closure result and its dependencies.
SSI8–SSI10 propagate the strengthened equality through ordinary sheaf
cohomology and both stated source conventions, retaining every endpoint.
This proves no weight-separation or RH statement.
