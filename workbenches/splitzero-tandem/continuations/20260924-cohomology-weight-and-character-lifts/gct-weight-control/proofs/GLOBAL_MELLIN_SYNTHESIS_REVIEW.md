# Independent proof audit of global Mellin synthesis, S3–S5

24 September 2026. Reviewed source: GLOBAL_MELLIN_SYNTHESIS.md, SHA256 8fbb7dcfe17ad124c02a3fa428019e8adb33241366606baf1ba88f350b6a12eb. The whole source was read to identify conventions and dependencies; the independent derivation below checks S3–S5, with S1's specified spaces and S2's displayed product and zero-count estimates as their inputs. It does not claim an independent reproof of the general Hadamard factorization theorem, nor a check of human-source reading receipts. No numerical range, RH assumption, zero simplicity, zero separation, or presumed lower bound on the original zeta inside the strip enters the audit.

**Outcome:** the division, source construction and approximation establish the closure equality as stated. One displayed bound should be written with an unambiguous supremum: S3.2 means a supremum in the real coordinate at a fixed imaginary coordinate. The precise repaired statement is R1.1 below. The source's following sentence already specifies that interpretation; the repair changes its notation, not its mathematical conclusion.

## R1. Correct form of the estimate and quotient extension

Let B consist of entire functions with rapid decrease on every closed vertical strip, with the source seminorms b_(A,M). Write

\[
F_0(s)=e^{a+bs}\prod_\rho(1-s/\rho)e^{s/\rho},
\qquad n(R)\le C_0(R+2)^{3/2},\quad F_0(0)\ne0.
\]

The product repeats each zero according to its multiplicity. If F belongs to B and all those zero jets vanish in F, division at each zero gives an entire Q=F/F_0. More explicitly, near rho factor F_0(s)=(s-rho)^m u(s) with u(rho) nonzero and F(s)=(s-rho)^m v(s). Then v/u is holomorphic near rho and agrees with Q off rho. The local extensions agree on overlaps by the identity theorem.

The checked estimate is

\[
\boxed{\sup_{|\sigma|\le A}|Q(\sigma+it)|
\le C_{A,F}\exp\big(C(|t|+2)^{3/2}\log(|t|+2)\big)
\quad(t\in\mathbb R).}
\tag{R1.1}
\]

C depends only on F_0 and fixed numerical choices. C_(A,F) may depend on the strip and F. No global supremum over all imaginary coordinates is intended. This correction removes the ambiguity in S3.2's displayed supremum.

## R2. Product lower bound outside small disks

The zero-count estimate implies the following two explicit growth orders as R tends to infinity:

\[
\sum_{|\rho|\le8R}\frac1{|\rho|}=O(R^{1/2}),
\qquad
\sum_{|\rho|>8R}\frac1{|\rho|^2}=O(R^{-1/2}).
\tag{R2.1}
\]

To verify the first, separate the finitely many zeros of modulus below 1. They have positive minimum modulus because F_0 is nonzero at 0 and zeros cannot accumulate in a compact set. On a dyadic shell 2^j<=|rho|<2^(j+1), the sum of reciprocals is at most n(2^(j+1))/2^j=O(2^(j/2)). The finite geometric sum through 8R is O(R^(1/2)). For the tail, the shell 2^j8R<|rho|<=2^(j+1)8R contributes at most n(2^(j+1)8R)/(2^j8R)^2=O(R^(-1/2)2^(-j/2)). The convergent geometric sum proves the second assertion. Multiplicity is included in both estimates.

Let D_R be the union of the **open** disks of radius R^(-2) about all zeros with |rho|<=8R. For R/2<=|s|<=3R outside D_R,

\[
|1-s/\rho|=|s-\rho|/|\rho|\ge1/(8R^3)
\quad(|\rho|\le8R).
\tag{R2.2}
\]

There are O(R^(3/2)) such factors. Their logarithmic contributions are at least -C R^(3/2)log R. The real parts of their exponential factors sum to at least -3R sum_(|rho|<=8R)1/|rho|, which is at least -C R^(3/2) by R2.1.

For every remaining factor w=s/rho obeys |w|<=3/8. Its actual genus-one logarithm satisfies

\[
\log|(1-w)e^w|
=\Re\left(-\sum_{j=2}^\infty w^j/j\right)
\ge-\frac{|w|^2}{1-|w|}\ge-\frac85|w|^2.
\tag{R2.3}
\]

Hence the total tail is at least -(8/5)(3R)^2 sum_(|rho|>8R)|rho|^(-2), again at least -C R^(3/2). Finally log|exp(a+bs)|=Re(a+bs)>=-|a|-3|b|R. Adding every contribution proves

\[
|F_0(s)|\ge\exp(-C R^{3/2}\log R)
\quad(R/2\le|s|\le3R,\ s\notin D_R).
\tag{R2.4}
\]

This is a proved lower bound on F_0 away from an explicitly controlled disk union. It is not an assumed lower bound on zeta or on F_0 at its zeros. The full exponential factors in the Hadamard product are essential to the calculation and have been included.

## R3. All clusters and multiplicities are covered by the maximum principle

The sum of the disk radii is at most R^(-2)n(8R)=O(R^(-1/2)). Each connected component of a finite union of disks can be traversed along a chain of pairwise-intersecting disks. A simple chain uses each disk at most once. The distance between any two points in such a component is at most twice the sum of the radii in that chain and hence at most twice the sum over the whole union. Therefore every component has diameter less than 1 for sufficiently large R. Counting a repeated center repeatedly only increases this upper bound and does not create an assumption of distinct zeros.

Take s with R<=|s|<=2R and |Re(s)|<=A. If it lies outside D_R, R2.4 and the strip bound for F give the quotient estimate. If it lies inside, let C_s be its component. Every point of its closure lies within distance at most 1 of s. Consequently its boundary lies in |Re(z)|<=A+1 and R-1<=|z|<=2R+1, hence in R/2<=|z|<=3R for R>=2. The boundary is outside the open union D_R: a point of D_R has an open neighborhood inside a component, so it cannot be a boundary point of a different component. Thus R2.4 holds everywhere on the boundary, and F is bounded there by b_(A+1,0)(F).

Q is entire, including at all enclosed zeros. It is continuous on the compact closure of the bounded component. The maximum-modulus principle therefore bounds its modulus throughout the component by its boundary maximum. This principle does not require the component to be simply connected or its boundary to be smooth. It follows, for example, by taking a point of maximum on the compact closure; an interior maximum would make Q constant on the component, which gives the same bound by continuity.

This proves the quotient estimate on the entire annulus, including all clusters. Apply the estimate at dyadic R. For fixed A and |t|>=max(A,2), |sigma+it| lies between |t| and sqrt(2)|t|, so the annular estimate gives R1.1 with a universal change in C. The remaining compact portion of the strip is absorbed into C_(A,F). Thus no zero-spacing estimate or simplicity has been used at any step.

## R4. The Gaussian quotient has an actual source preimage

For epsilon>0 put Q_epsilon(s)=exp(epsilon(s-1/2)^2)Q(s). On |Re(s)|<=A its Gaussian modulus is at most exp(epsilon(A+1/2)^2-epsilon t^2). R1.1 then gives, for every M,

\[
(1+|t|)^M|Q_\varepsilon(\sigma+it)|
\le C_{A,F}e^{\varepsilon(A+1/2)^2}
(1+|t|)^M
\exp\big(-\varepsilon t^2+C(|t|+2)^{3/2}\log(|t|+2)\big).
\tag{R4.1}
\]

The right side is bounded because t^(-1/2)log(t+2) tends to zero. Thus Q_epsilon is in B. The source Mellin isomorphism gives q_epsilon in A, with the source's full inversion factor 1/(2pi) and phase exp(-itx).

Use the source's actual even Schwartz kernel f_0 and unitary dilation U_a f_0(v)=a^(-1/2)f_0(v/a). Define

\[
f_\varepsilon(v)=\int_0^\infty q_\varepsilon(a)
a^{-1/2}f_0(v/a)\frac{da}{a}.
\tag{R4.2}
\]

Every Schwartz seminorm has an integrable bound. In detail,

\[
\sup_v |v|^r|\partial_v^j U_a f_0(v)|
=a^{r-j-1/2}\sup_w|w|^r|f_0^{(j)}(w)|.
\tag{R4.3}
\]

Because q_epsilon decreases faster than every power at both a=0 and a=infinity, the factor a^(r-j-1/2)|q_epsilon(a)| is integrable against da/a. Seminorms with (1+|v|)^r follow by the finite binomial expansion. The improper integral is therefore Cauchy in every Schwartz seminorm and converges in the complete Schwartz space. It is even; its value at zero is zero because f_0(0)=0. Its integral is zero by Fubini and integral f_0=0, with the absolute bound ||U_a f_0||_1=a^(1/2)||f_0||_1. Thus f_epsilon belongs to the required S_0^even, rather than merely to a larger formal module.

The already proved continuity E:S_0^even->A allows E to commute with these convergent improper integrals. Its exact covariance E(U_a f_0)(u)=k_0(u/a) yields

\[
E f_\varepsilon=k_0*q_\varepsilon,
\quad M(E f_\varepsilon)(s)=F_0(s)Q_\varepsilon(s)
=e^{\varepsilon(s-1/2)^2}F(s).
\tag{R4.4}
\]

For the convolution's Mellin product, the substitution u=av gives u^(s-1/2)=a^(s-1/2)v^(s-1/2). The centered exponent occurs in both factors, so no extra power of a is missing. Absolute Fubini is justified by the arbitrary endpoint decay of both convolution factors. This checks the actual preimage, including its half-power dilation and all source constraints.

## R5. Approximation in the entire test topology and closure equality

Let K(x)=k(e^x) and g_epsilon(x)=(4pi epsilon)^(-1/2)exp(-x^2/(4epsilon)). Its bilateral centered Mellin factor is exactly exp(epsilon(s-1/2)^2), with no removed constant. By Mellin injectivity, R4.4 therefore gives (E f_epsilon)(e^x)=(g_epsilon*K)(x).

For the weighted derivative seminorm ||K||_(N,j)=sup_x exp(N|x|)|K^(j)(x)|, the fundamental theorem of calculus proves

\[
\|K(\cdot-y)-K\|_{N,j}
\le |y|e^{N|y|}\|K\|_{N,j+1}.
\tag{R5.1}
\]

Indeed K^(j)(x-y)-K^(j)(x) is the oriented integral of -K^(j+1)(x-r) from r=0 to r=y, and exp(N|x|)<=exp(N|x-r|)exp(N|r|). This works for either sign of y. Integrating against the positive Gaussian, whose mass is exactly 1, gives

\[
\|g_\varepsilon*K-K\|_{N,j}
\le\|K\|_{N,j+1}\sqrt\varepsilon\,
\frac1{\sqrt{4\pi}}\int_{\mathbb R}
|z|e^{N|z|}e^{-z^2/4}dz
\longrightarrow0
\tag{R5.2}
\]

for 0<epsilon<=1, by y=sqrt(epsilon)z and exp(N sqrt(epsilon)|z|)<=exp(N|z|). The integral is finite for every fixed N because the negative quadratic dominates the linear term. Thus convergence holds in every seminorm of A, not only in L^2, pointwise, or on a finite set of zero evaluations.

Every approximant is in E(S_0^even) by R4.2–R4.4. Hence any k whose full Mellin transform vanishes to all required zero orders lies in the A-closure of that image. Conversely each such jet vanishes on E(S_0^even), by its original-zeta factorization, and is continuous on A, so it vanishes on the closure. These two proved inclusions give

\[
\overline{E(S_0^{\rm even})}^{A}
=\{k\in A:(Mk)^{(j)}(\rho)=0\text{ for all actual }\rho,
\ 0\le j<m_\rho\}.
\tag{R5.3}
\]

The proof uses all zeros simultaneously and leaves all multiplicities intact. Its Gaussian parameter is an approximation in the full topology; it is not a heat-flow claim that zeros move onto the critical line. In particular the proof identifies the quotient and its continuous zero-jet observations without establishing that the scaling factors a^(rho-1/2) have modulus one. The resulting synthesis theorem is a completed global closure calculation, and its distinction from a purity theorem is exact.
