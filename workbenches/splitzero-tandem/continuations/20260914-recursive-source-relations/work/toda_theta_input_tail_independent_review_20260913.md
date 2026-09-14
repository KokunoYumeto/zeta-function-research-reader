# Independent review of the original theta input and its certified tails

Review completed 13 September 2026. The complete standalone proof, TI.1–TI.32, and the complete executable were read. The final reviewed source is `toda_theta_input_tail_20260912.tex`, SHA256 `e50a11c51293017b1a433f3ed9b499947a953e6b2955f59f3c46f14ed26a409d`. The reviewed executable is `toda_theta_input_tail_check_20260912.py`, SHA256 `db01839848cb6b67d24f5702789f6b9eb27d523a80c40cc58b25b9634ce101c5`.

The analytic construction and the three infinite-value enclosures, together with the first recurrence coefficient, are accepted at those pins. This review verifies the exact analytic maps, the original theta coefficients and measure mass, the complex branches, every term of the omitted-square-tail bound, and the computational enclosure logic. It also records the precise passage to a finite zero packet. All calculations below use the original coordinate, or explicitly exhibit the coordinate map when another variable is introduced.

## 1. Original source, inversion, and Mellin transform

The source and Euler operator are

\[
 \vartheta(z)=\sum_{n\in\mathbb Z}e^{-\pi n^2z^2},\qquad
 D=-z\partial_z,\qquad
 f_0(z)=2\sum_{n\ge1}(4\pi^2n^4z^4-6\pi n^2z^2)e^{-\pi n^2z^2}.
\]

Their domain is the open sector \(\mathcal S_{\pi/4}=\{z\ne0:|\arg z|<\pi/4\}\), with the principal logarithm restricted to that sector. For the single summand with \(a=\pi n^2\), direct differentiation gives

\[
 D e^{-az^2}=2az^2e^{-az^2},\qquad
 D^2e^{-az^2}=(4a^2z^4-4az^2)e^{-az^2}.
\]

Consequently \(D(D-1)e^{-az^2}=(4a^2z^4-6az^2)e^{-az^2}\), and the two terms with integer indices \(n\) and \(-n\) give the original factor two in \(f_0=D(D-1)\vartheta\). On a compact subset of the sector, all differentiated summands have a dominating bound \(C n^N e^{-c n^2}\), with \(c>0\). This proves holomorphy and every termwise differentiation used here.

For real \(x>0\), the Fourier transform of \(e^{-\pi x^2t^2}\), using kernel \(e^{-2\pi i\xi t}\), is \(x^{-1}e^{-\pi\xi^2/x^2}\). One can derive the value at zero by squaring the Gaussian integral and using polar coordinates; differentiating in \(\xi\) and integrating by parts then gives the equation \(I'(\xi)=-(2\pi\xi/x^2)I(\xi)\), determining the displayed transform. Periodizing the Gaussian gives an absolutely convergent Fourier series with these coefficients. Its value at zero is

\[
 \vartheta(x)=x^{-1}\vartheta(1/x).
\]

Both sides are holomorphic in the connected sector, so the equality holds throughout it. Define the complex-linear inversion \((RF)(z)=z^{-1}F(1/z)\). Direct differentiation proves

\[
 R^2=1,\qquad DR=R(1-D),\qquad D(D-1)R=RD(D-1).
\]

It follows that

\[
 f_0(z)=z^{-1}f_0(1/z),\qquad f_0(\bar z)=\overline{f_0(z)}.
\]

On a closed subsector \(|\arg z|\le\alpha<\pi/4\), the real part of \(z^2\) is at least \(|z|^2\cos(2\alpha)\). For \(|z|\ge1\), the differentiated series is bounded by a fixed polynomial in \(|z|\) times a Gaussian in \(|z|\). The identity \(D^jR=R(1-D)^j\) transports these estimates to zero. Hence for each real \(A>0\), every Euler derivative is \(O(|z|^{-A})\) at infinity and \(O(|z|^A)\) at zero, uniformly on that closed subsector.

With the unchanged Mellin convention

\[
 (\mathcal MF)(s)=\int_0^\infty F(x)x^{s-1}\,dx,
\]

the endpoint estimates prove that \(\mathcal Mf_0\) is entire. For \(\Re s>1\), the sums of absolute integrals of both polynomial terms converge as a constant times \(\sum_{n\ge1}n^{-\Re s}\). Substitution \(u=\pi n^2x^2\) therefore gives

\[
 \begin{aligned}
 \mathcal Mf_0(s)
 &=\pi^{-s/2}\zeta(s)\bigl[4\Gamma(s/2+2)-6\Gamma(s/2+1)\bigr]\\
 &=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=g(s).
 \end{aligned}
\]

The first line retains the source factor two and the substitution factor one half. The second follows from integration by parts in the gamma integral. The entire Mellin integral provides the continuation. Substituting \(x=1/u\), including \(dx=-u^{-2}du\), proves \(g(1-s)=g(s)\); conjugation of the integral proves \(\overline{g(\bar s)}=g(s)\).

## 2. Exact packet division and its source map

Let \(h(s)=\prod_\rho(s-\rho)^{m_\rho}\) be the stated monic finite divisor of the entire function \(g\): every selected multiplicity is at most the actual vanishing order, and the selected multiset is invariant under \(\rho\mapsto1-\bar\rho\). Set \(d=\deg h\), \(v_h=g/h\) with removable values filled in, and \(h^\dagger(s)=\overline{h(1-\bar s)}\). The roots of \(h^\dagger\) are the selected roots, with the selected multiplicities, and its leading coefficient is \((-1)^d\). Thus

\[
 h^\dagger=(-1)^dh,\qquad v_h^\dagger=(-1)^dv_h.
\]

The proof constructs its source rather than supposing endpoint decay for an inverse transform. For \(|\beta|<\pi/4\), rotate the Mellin contour to \(e^{i\beta}\mathbb R_{>0}\). The rapid endpoint estimates annihilate both closing arcs and prove

\[
 g(s)=e^{i\beta s}\int_0^\infty f_0(e^{i\beta}x)x^{s-1}\,dx.
\]

On each compact interval of \(\sigma=\Re s\), the absolute integral is uniformly bounded. Choosing the sign of \(\beta\) to agree with that of \(t=\Im s\) gives \(|g(\sigma+it)|\le C e^{-|\beta||t|}\). For large \(|t|\) the finite product obeys \(|h(\sigma+it)|\ge c(1+|t|)^d\), uniformly on the same interval of \(\sigma\). On the remaining compact rectangle, \(v_h\) is bounded by its holomorphy. Hence the same exponential estimate holds for \(v_h\).

This estimate also supplies bounds for its derivatives used in inversion: choose a fixed small circle about \(\sigma+it\), contained in a slightly larger vertical strip. Cauchy's formula bounds the \(j\)-th derivative by \(j!\delta^{-j}\) times the supremum on that circle. The latter is at most a fixed constant times \(e^{-|\beta||t|}\), since the imaginary coordinate differs from \(t\) by at most \(\delta\). Thus each derivative is integrable on each vertical line.

The integral

\[
 F_h(z)=\frac1{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
 v_h(s)z^{-s}\,ds
\]

converges absolutely and locally uniformly with all Euler derivatives: choose \(|\beta|>|\arg z|\). Horizontal contour segments tend to zero uniformly between two fixed vertical lines, proving independence of \(\sigma\). Taking \(\sigma\) arbitrarily positive or negative proves the two rapid endpoint estimates for \(F_h\). Fourier inversion in \(x=e^y\) then gives \(\mathcal MF_h=v_h\). The exact constants follow by writing \(ds=i\,dt\): the inverse on the line \(\Re s=\sigma\) is \((2\pi)^{-1}\int v_h(\sigma+it)e^{-ity}dt\), multiplied by \(e^{-\sigma y}\). The integrable derivative estimates justify ordinary inversion; alternatively multiplication by \(e^{-\varepsilon t^2}\) gives a Gaussian approximate identity of total integral one and proves the same statement by taking its limit.

Let \(\mathcal A\) denote the vector space of holomorphic sector functions having the proved rapid estimates for every Euler derivative on each closed subsector. The differential operator is the well-defined map \(h(D):\mathcal A\to\mathcal A\). Its Mellin transform multiplies by \(h(s)\), by integration by parts with vanishing endpoints. Therefore

\[
 h(D)F_h=f_0,\qquad
 (\mathcal M\circ h(D))(F_h)=h(s)\mathcal MF_h(s)=g(s).
\]

This proves the specified intertwining map with its actual domain, without removing any polynomial factor. For the conjugate-linear source involution \((\mathcal RF)(x)=x^{-1}\overline{F(1/x)}\), substitution gives \(\mathcal M\mathcal RF=(\mathcal MF)^\dagger\). Mellin uniqueness and holomorphic continuation therefore give

\[
 F_h(1/\bar z)=(-1)^d\bar z\,\overline{F_h(z)}.
\]

The sign is fixed by the degree of the original monic divisor.

## 3. Unitary logarithmic map, analytic tilt, and the original mass

The map and inverse

\[
 U:L^2((0,\infty),dx)\longrightarrow L^2(\mathbb R,dy),\quad
 UF(y)=e^{y/2}F(e^y),\quad
 U^{-1}u(x)=x^{-1/2}u(\log x)
\]

are unitary, since \(e^y dy=dx\). For \(F\in\mathcal A\) and real \(|\theta|<\pi/2\), define the analytic translation

\[
 E_\theta F(y)=e^{(y+i\theta/2)/2}F(e^{y+i\theta/2})\in L^2(\mathbb R,dy).
\]

The positive Fourier convention is \(\mathcal F_+u(t)=\int u(y)e^{ity}dy\). In the contour shift \(z=y+i\theta/2\), the exponential is
\(e^{ity}=e^{\theta t/2}e^{itz}\); the vertical edges vanish by the endpoint bounds. This proves the exact map identity

\[
 \mathcal F_+(E_\theta F_h)(t)=e^{\theta t/2}v_h(1/2+it).
\]

The source factor \(e^{i\theta/4}\) remains in \(E_\theta\). For real \(\theta\) its modulus equals one. Plancherel with the given kernel has constant \(1/(2\pi)\), so

\[
 \begin{aligned}
 w_h(t)&=\frac{|v_h(1/2+it)|^2}{2\pi},\\
 M_h(\theta)&=\int_\mathbb R e^{\theta t}w_h(t)dt
 =\|E_\theta F_h\|_{L^2(dy)}^2
 =\int_0^\infty|F_h(e^{i\theta/2}x)|^2dx.
 \end{aligned}
\]

The source inversion gives

\[
 F_h(e^{i\theta/2}/x)=(-1)^de^{-i\theta/2}x\,
 \overline{F_h(e^{i\theta/2}x)}.
\]

Substituting \(u=1/x\) in the integral from zero to one cancels the squared factor \(u^2\) against the Jacobian \(u^{-2}\), proving

\[
 M_h(\theta)=2\int_1^\infty |F_h(e^{i\theta/2}x)|^2dx.
\]

The sign \((-1)^d\) has been retained up to taking its absolute square. The exponential vertical-line estimate proves absolute convergence of all moment derivatives locally on \(|\Re\theta|<\pi/2\): on any compact substrip choose \(\beta\) with \(2|\beta|>\sup|\Re\theta|\), leaving positive exponential decay after multiplication by any fixed power of \(t\).

Ordinary conjugation of the selected multiset implies \(h(\bar s)=\overline{h(s)}\) and the same identity for \(v_h\). This gives \(w_h(-t)=w_h(t)\) and \(M_h(-\theta)=M_h(\theta)\). The dagger identity above supplies the inversion for every dagger-stable packet; this additional root symmetry supplies evenness. In particular it holds for the seed \(h=1\).

The seed-to-packet relation remains exact even at line zeros:

\[
 h(1/2+it)v_h(1/2+it)=g(1/2+it),\qquad
 w_1(t)=|h(1/2+it)|^2 w_h(t).
\]

It follows from the entire quotient filled in at its removable values. Thus it never evaluates a quotient of two recorded zero values. These maps explicitly connect the seed data and the packet data while retaining the original multiplier and source mass \(\mu_h=M_h(0)\).

## 4. Double series, its branch, and the omitted square

For real \(\theta\), let \(f^\pm(x)=f_0(e^{\pm i\theta/2}x)\). Their product is the absolute square, and the preceding integral gives \(M_1(\theta)=2\int_1^\infty f^+(x)f^-(x)dx\). With \(c_1=-6,c_2=4\), the product of the two original source factors and the endpoint factor is \(2\cdot2\cdot2=8\). For \(\Re C>0\),

\[
 I_p(C)=\int_1^\infty x^p e^{-Cx^2}dx
 =\frac{\Gamma((p+1)/2,C)}{2C^{(p+1)/2}}.
\]

For positive \(C\), substitution \(u=Cx^2\) proves this equality. On the right half-plane the logarithm is the unique holomorphic branch real on its positive axis; both sides are holomorphic there, and analytic continuation proves the equality for all such \(C\). Hence with

\[
 C_{mn}(\theta)=\pi(m^2e^{i\theta}+n^2e^{-i\theta}),\qquad
 \alpha_{rs}=r+s+\tfrac12,
\]

the exact coefficient after integration is \(8/2=4\), giving

\[
 M_1(\theta)=4\sum_{m,n\ge1}\sum_{r,s=1}^2
 c_rc_s(\pi m^2)^r(\pi n^2)^s e^{i\theta(r-s)}
 \frac{\Gamma(\alpha_{rs},C_{mn}(\theta))}
      {C_{mn}(\theta)^{\alpha_{rs}}}.
\]

The phase is \(e^{i\theta r}\) from the first factor and \(e^{-i\theta s}\) from the second. The double sum over a square is essential: \(M_{1,J}\) retains exactly \(1\le m,n\le J\), including every mixed term inside that square.

For the locally uniform estimate let \(|\Re\theta|\le\theta_0<\pi/2\), \(|\Im\theta|\le B\), and set \(d_0=\pi e^{-B}\cos\theta_0>0\). Then

\[
 \Re(\pi n^2e^{\pm i\theta})\ge d_0n^2,\qquad
 |e^{\pm ir\theta}|\le e^{rB}.
\]

For each integer \(a\ge1\), put \(\rho_a=e^{-d_0(2a+1)}\). If \(n=a+j\), \(j\ge0\), then

\[
 n^2-a^2=2aj+j^2\ge(2a+1)j.
\]

Because \(x\ge1\), this proves

\[
 \sum_{n\ge a}n^p e^{-d_0n^2x^2}
 \le e^{-d_0a^2x^2}\sum_{j\ge0}(a+j)^p\rho_a^j.
\]

The last sum is the finite positive rational expression

\[
 H_p(a,d_0)=\sum_{j=0}^p\binom pj a^{p-j}
 \sum_{b=0}^j {j\brace b}\frac{b!\rho_a^b}{(1-\rho_a)^{b+1}}.
\]

To verify it, expand \((a+j)^p\) by the binomial theorem, write \(j^r=\sum_b{r\brace b}(j)_b\), and differentiate \(\sum_{j\ge0}\rho^j=(1-\rho)^{-1}\) exactly \(b\) times. The falling-factorial expansion follows by induction from \(j(j)_b=(j)_{b+1}+b(j)_b\), with the stated Stirling initial values. This derives every denominator and numerator in \(H_p\).

Define

\[
 A_a=6\pi e^B H_2(a,d_0)+4\pi^2e^{2B}H_4(a,d_0),\qquad L=J+1.
\]

Using \(x^2\le x^4\) solely in the majorant gives

\[
 |f^\pm|,|f_J^\pm|\le2A_1x^4e^{-d_0x^2},\qquad
 |f^\pm-f_J^\pm|\le2A_Lx^4e^{-d_0L^2x^2}.
\]

The exact series still contains its original \(-6\) and \(4\) coefficients. Its error obeys the exact product decomposition

\[
 f^+f^--f_J^+f_J^-=(f^+-f_J^+)f^-+f_J^+(f^--f_J^-).
\]

Each summand on the right is bounded by \(4A_1A_Lx^8e^{-d_0(1+L^2)x^2}\). Summing these two bounds and integrating with the original endpoint factor two gives

\[
 |M_1(\theta)-M_{1,J}(\theta)|
 \le16A_1A_L I_8(d_0(1+L^2))=\mathcal E_J(\theta_0,B).
\]

In particular the estimate includes retained–omitted and omitted–omitted interactions; it is a bound for the whole omitted part of the square.

The same majorants prove absolute, locally uniform integrability of the full expanded double sum. For fixed \(d_0\), all denominators \(1-\rho_L\) stay bounded away from zero for \(L\ge1\), and \(H_p(L,d_0)\le C_p(1+L)^p\). If \(b\ge d_0\), then

\[
 I_8(b)\le e^{-b}\int_1^\infty x^8e^{-d_0(x^2-1)}dx,
\]

whose second factor is finite. Thus \(\mathcal E_J\to0\) exponentially in \(L^2\). For complex \(\theta\), both dilated sources stay in the sector, \(C_{mn}\) stays in the right half-plane, and \(2\int f^+f^-\) is holomorphic throughout the strip. It agrees with \(M_1\) on the real interval, so the holomorphic identity theorem proves the double-series identity on the whole strip. On a closed disc of radius \(r>0\) contained in a permissible rectangle, Cauchy's formula applied to the analytic error gives

\[
 |M_1^{(j)}(\theta)-M_{1,J}^{(j)}(\theta)|
 \le j!r^{-j}\mathcal E_J(\theta_0,B).
\]

This conclusion retains the derivative order, disc radius, and rectangle explicitly.

## 5. Second derivative and its independent tail

For a fixed original integer \(n\), the coordinate map \(y=\pi n^2x^2\) transports \(D\) to \(-2y\partial_y\). With \(P(y)=8y^2-12y\), the exact calculation is

\[
 \begin{aligned}
 (D-\tfrac12)(P(y)e^{-y})
 &=\bigl[-2yP'(y)+2yP(y)-P(y)/2\bigr]e^{-y}\\
 &=(16y^3-60y^2+30y)e^{-y}.
 \end{aligned}
\]

Hence \(H=(D-1/2)f_0\) has coefficients \(d_1=30,d_2=-60,d_3=16\), without an extra outer factor two. Differentiating \(UF\) gives \(U(D-1/2)F=-(UF)'\); integration by parts in the positive Fourier kernel gives \(\mathcal F_+(-u')=it\mathcal F_+u\). Therefore

\[
 M_1''(0)=\frac1{2\pi}\int_\mathbb R t^2|g(1/2+it)|^2dt
 =\int_0^\infty |H(x)|^2dx.
\]

Since \(R(D-1/2)=-(D-1/2)R\) and \(Rf_0=f_0\), one has \(RH=-H\), equivalently \(H(1/x)=-xH(x)\). Substitution in the small-end integral again gives

\[
 M_1''(0)=2\int_1^\infty H(x)^2dx.
\]

The exact truncated quantity is defined by \(T_J=2\int_1^\infty H_J(x)^2dx\). It never invokes inversion for the truncated theta function. Expanding this square and integrating gives

\[
 T_J=\sum_{m,n=1}^J\sum_{r,s=1}^3d_rd_s(\pi m^2)^r(\pi n^2)^s
 \frac{\Gamma(r+s+1/2,\pi(m^2+n^2))}
 {\bigl(\pi(m^2+n^2)\bigr)^{r+s+1/2}}.
\]

Its coefficient is one, because the exterior factor two cancels the integral's factor one half. All negative cross terms with \(d_2=-60\) remain present.

Set

\[
 B_a=30\pi H_2(a,\pi)+60\pi^2H_4(a,\pi)+16\pi^3H_6(a,\pi).
\]

The preceding weighted-geometric calculation gives

\[
 |H|,|H_J|\le B_1x^6e^{-\pi x^2},\qquad
 |H-H_J|\le B_Lx^6e^{-\pi L^2x^2}.
\]

It follows directly from \(|H^2-H_J^2|\le|H-H_J|(|H|+|H_J|)\), followed by the exterior factor two, that

\[
 |M_1''(0)-T_J|\le4B_1B_LI_{12}(\pi(1+L^2))=\mathcal T_J.
\]

This independently checks TI.25–TI.30 with every coefficient and cross term. The separately supplied derivative audit also gives a purely rational, weaker error bound \(|M_1''(0)-T_8|<10^{-92}\), including the full retained–omitted interaction; its derivation was read. That rational bound can be added to the same finite arithmetic enclosure to recover the displayed forty-decimal interval, since it is much smaller than its distance to either decimal endpoint. The sharper \(\mathcal T_8\) in the reviewed executable is evaluated with Arb.

For the original convolution \(m_k=w_1^{*k}\), absolute integrability and Fubini give \(Z_k(\theta)=M_1(\theta)^k\) and total mass \(\mu_1^k\). Evenness gives \(Z_k'(0)=0\). In the original sum coordinate \(u\), the degree-zero and degree-one monic polynomials are \(1\) and \(u\), with norms

\[
 h_0=\mu_1^k,\qquad h_1=Z_k''(0)=k\mu_1^{k-1}M_1''(0).
\]

The first monic recurrence coefficient is therefore exactly

\[
 a_1^{(k)}=h_1/h_0=kM_1''(0)/M_1(0).
\]

Both original norms and the measure mass remain specified in this equality.

## 6. Interval computation and its trust boundary

The reviewed executable uses installed `python-flint 0.9.0`, 256-bit Arb midpoints, Acb rectangular balls, exact integer/rational inputs, and one arithmetic thread. Its real and complex arithmetic enclosures are supplied by the library. The documented constructor encloses midpoint plus/minus radius and rounds a nonzero radius upward; `lower()` and `upper()` return directed, exact dyadic endpoint bounds. These are the semantics used in the error inflation and exact receipt extraction. [Arb interface](https://python-flint.readthedocs.io/en/latest/arb.html)

The call `C.gamma_upper(alpha)` means the unregularized upper incomplete gamma \(\Gamma(\alpha,C)\). Every evaluated \(C\) is checked to have a strictly positive real ball, keeping its power and incomplete-gamma argument in the proved half-plane. [Acb interface](https://python-flint.readthedocs.io/en/latest/acb.html) The underlying power convention uses the principal logarithm, agreeing with the branch specified above on this half-plane. [FLINT complex powers and logarithm](https://flintlib.org/doc/acb.html)

Specifically, `seed_finite` retains \(m,n=1,\ldots,8\), \(c_1=-6,c_2=4\), the outer factor four, and the integer power `plus**(r-s)` of \(e^{i\theta}\). `minus` supplies the other phase in \(C\). The half-integer parameter is made from the exact rational \((2r+2s+1)/2\). In `derivative_finite`, the coefficient map is exactly \(30,-60,16\), and the outer factor is one. `H` implements the finite Stirling expression with integer arithmetic for all combinatorial coefficients.

An exact rational input such as \(1/10\) is converted to an enclosing Arb ball; the mathematical input is still that exact rational, rather than a machine binary approximation substituted for it. All subsequent operations enclose the values on their input balls. In particular evaluating the tail expression at those balls encloses its value at the desired \(d_0\), \(\theta_0\), and \(B\).

Let \(Q\) be the computed real ball for a finite sum and let \(E\) be a computed ball containing its proved positive tail bound. The script takes \(u=E.\mathrm{upper}()\), so the exact error bound is at most the dyadic \(u\). The constructor `arb(0,u)` contains \([-u,u]\), and the Arb sum `Q + arb(0,u)` contains every possible finite value plus every possible omitted error. It therefore contains the infinite quantity. This is the exact enclosure implication; agreement between approximations at different precisions is not used. For the seed sum, reality is proved by conjugating and interchanging its finite indices. Checking that the computed imaginary ball contains zero is an additional consistency test, and taking its real component retains the true real sum.

The positive mass ball allows interval division of the second-derivative ball by the mass ball. Thus the resulting ratio ball encloses \(a_1^{(k)}/k\) for every integer \(k\ge1\), by the exact tensor identity above.

For each final ball \(Q\), the executable constructs decimal endpoints by directed lower/upper dyadic extraction, multiplication by the integer \(10^{40}\), floor/ceiling, and one further decimal unit outward on each side. It then explicitly checks strict interval comparisons with the resulting exact rational endpoints. Those final comparisons certify inclusion even if an intermediate outward endpoint extraction was wider than necessary. `fmpq()` on the exact endpoints preserves their exact dyadic values in the receipt.

The accepted intervals are

| Quantity | Exact rational decimal lower endpoint | Exact rational decimal upper endpoint |
|---|---|---|
| \(M_1(0)\) | 1.2790072478464851404795335922671932744916 | 1.2790072478464851404795335922671932744919 |
| \(M_1(1/10)\) | 1.3459071784582497969682205923576298051604 | 1.3459071784582497969682205923576298051607 |
| \(M_1''(0)\) | 13.0555493025705584353926846581231936824343 | 13.0555493025705584353926846581231936824346 |
| \(a_1^{(k)}/k\) | 10.2075647534857216888657612522375551749964 | 10.2075647534857216888657612522375551749967 |

All four widths are \(3\cdot10^{-40}\). The evaluated positive-tail comparisons are \(\mathcal E_8(0,0)<7\cdot10^{-107}\), \(\mathcal E_8(1/10,0)<3\cdot10^{-106}\), and \(\mathcal T_8<4\cdot10^{-103}\). The proof supplies the infinite mathematical inequalities; the ball operations certify the finite evaluations appearing in those inequalities. The library's enclosure contract, its installed implementation, and the Python execution remain the computational trust boundary. No local Lean run or machine-checked formal proof of Arb's implementation is asserted.

## 7. Executed records, targeted checks, and repairs

The final four-mode replay receipt is `toda_theta_input_tail_replay_receipt_20260912.json`, SHA256 `1c74d398871ff0bde77002f15890e3d03da3dc1099db3dd7238cc06fe61ad1cb`. The positive normal and optimized JSON files have SHA256 respectively

- `toda_theta_input_tail_result_normal_20260912.json`: `2d5ebb1a40f1f33cff8d227ae57d68fb3ae0a18d084b74973d08fcf2c1cc32cc`;
- `toda_theta_input_tail_result_optimized_20260912.json`: `3d5f835f6f4f39f130ade91077e9ec9c1f8a808782faed5d8491598c41961bb7`.

Both positive runs exited zero and pin the current executable. Their mathematical records coincide; the optimization field records the actual different run modes. Both negative runs exited one at the explicitly checked false inequality \(a_1^{(k)}/k<1\). Both stderr files were read and reach the exact message `deliberate false recurrence bound rejected`. The exception precedes successful receipt writing; the replay records no success result for either negative run. This verifies that the deliberate failure remains enforced under optimization, without interpreting a negative run as an additional theorem check.

The separate `Fraction`-only endpoint review is `toda_theta_tail_rational_receipt_review_20260913.json`, SHA256 `c2c1b36d540816a4fea2338f0da74ef77fd11a8eb6957b92cf60ab075649c135`, produced by the fully read reusable script `toda_theta_tail_rational_receipt_check_20260913.py`, SHA256 `a52b27568e2f627fc0483064b2bc73d6aadbd92109be1c4943c23ecda0251e2b`. For the two refreshed receipts it verifies eight strict decimal enclosures, eight widths exactly equal to \(3\cdot10^{-40}\), all sixteen raw and reduced dyadic denominators, and positive mass. In each receipt the saved dyadic ratio interval contains the entire external-endpoint quotient interval

\[
 \left[
 \frac{M_{1,\mathrm{lower}}''(0)}{M_{1,\mathrm{upper}}(0)},
 \frac{M_{1,\mathrm{upper}}''(0)}{M_{1,\mathrm{lower}}(0)}
 \right].
\]

The printed rational decimal ratio interval strictly contains this quotient interval as well. The comparison follows from exact rational cross multiplication with positive denominators. These are independent checks on the saved endpoints; the analytic enclosure of the infinite quantities follows from Sections 1–6 and the reviewed Arb execution.

The independent targeted checker `toda_theta_tail_independent_check_20260913.py`, SHA256 `1e5d684acd3c80354a4681d66e2577c851584e0463bd893264fb0f05ae317ffc`, passed 27 explicit checks. Its result is `toda_theta_tail_independent_check_result_20260913.json`, SHA256 `aba07a82fb95823421b1c444a9f3654c73bf5acfbf3e19684d06a59f8017d5ad`. Seven exact symbolic checks compare \(H_p\), \(0\le p\le6\), with the independently generated expression \((a+\rho\partial_\rho)^p(1-\rho)^{-1}\). The remaining checks examine the half-plane, every needed half-gamma order via the alternative identity

\[
 \Gamma(1/2,C)=\sqrt\pi\operatorname{erfc}(\sqrt C),\qquad
 \Gamma(\alpha+1,C)=\alpha\Gamma(\alpha,C)+C^\alpha e^{-C},
\]

at positive and conjugate nonreal sample arguments; reject a swapped argument/parameter call by disjoint balls; and check inclusion of both exact dyadic endpoints by the radius constructor. The half-gamma identity follows for positive \(C\) by \(u=t^2\), with the recurrence from integration by parts, then throughout the right half-plane by holomorphic continuation. The overlap tests are diagnostics of the alternate computational path; the written identities prove the equality itself.

Two literal TeX control-word typos in TI.23 and TI.30 were reported and repaired: `cal E` and `cal T` now render the same calligraphic error symbols used by TI.24 and TI.32. The initial optimized receipt pinned a predecessor script. The author refreshed all four runs at the accepted executable pin; the final records above close that provenance issue. The Stirling-brace presentation was also repaired without changing its recurrence or coefficients. No unresolved mathematical defect was found at the accepted proof pin.

## 8. Exact scope of the result and its integration

The result supplies three particular infinite analytic-seed values and the exactly related first tensor recurrence coefficient. It also supplies a locally uniform rectangle tail formula and Cauchy bounds for every fixed finite derivative order, with the order and rectangle parameters present. The proof's finite-packet map is \(F_h\xmapsto{h(D)}f_0\), transported by Mellin/Fourier transform to multiplication by \(h(1/2+it)\), and its density identity is \(w_1=|h|^2w_h\). This is the actual relation needed when using the seed alongside packet inputs.

For \(h=1\), the quotient map \(\mathbb C[S]\to\mathbb C[S]/(1)\) sends every polynomial to zero, since every polynomial belongs to the unit ideal. Its codomain is the zero vector space. At the same time the source measure has the explicitly positive mass \(M_1(0)\), and its tensor source norms are the positive values given above. These are their exact maps and values. The four scalar enclosures evaluate no determinant for a nonempty zero packet and prove no upper bound with a growing tensor degree or determinant dimension. The accepted continuation retains those domains when its analytic input is incorporated in the source determinant flow.
