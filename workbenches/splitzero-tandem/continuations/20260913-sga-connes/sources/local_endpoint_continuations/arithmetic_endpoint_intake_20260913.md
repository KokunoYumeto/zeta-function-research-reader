# Arithmetic endpoint delivery: complete source intake and mathematical audit

This audit covers the complete 13 September 2026 arithmetic endpoint delivery. It proves the displayed dyadic norm estimate for the original arithmetic measure, supplies the intermediate constants and typed maps, and records exactly what the finite replay establishes. The source's equation numbers are retained as references. This file does not modify the source archive, the 478-page Gamma paper, a release, or a publication branch.

## 1. Exact source and execution record

The archive `Tau_Arithmetic_Endpoint_Bounds_2026-09-13.zip` has 781925 bytes and SHA-256 `c32ca4bebc86c6b7c7ffb58533a49b75e2140b00b31cdb6602cea6d8537ad9f6`. All 32 archive members were extracted with path traversal, absolute path, and conflicting-existing-byte checks into `sources/web_arithmetic_endpoint_delivery/Tau_Arithmetic_Endpoint_Bounds`. Every extracted byte agrees with its archive member. The original archive's 31-entry manifest checks every member other than that manifest itself.

The complete mathematical Markdown (28116 bytes, SHA `8fa97624a55c2f1baad54e465e4637c584329f24f6c198bb5d168a443811a280`) and complete 840-line TeX (31714 bytes, SHA `f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8`) were read. The complete second user paste, README, handoff, programme state, source review, checks description, Python checker, reader builder, manifest, all JSON receipts and all text logs were read. The add-only patch was completely parsed; all 15 added files reconstruct their corresponding delivered files byte for byte, including the explicitly recorded missing final newline of `checks/source-reading.json`. No patch was applied to any checkout.

The supplied HTML contains all 225 mathematical nodes from the Markdown in the same order and with exactly the same TeX annotation strings. Its 226th MathML element is the duplicate `g/h` in the table of contents. All 48 numbered displays are present. The supplied desktop, mobile and theorem PNGs were each actually viewed; the title and theorem regions shown are readable. Those three PNGs and browser-layout measurements remain historical evidence; this intake does not claim a fresh browser rendering or inspection of portions absent from those screenshots.

The checker `check_endpoint_bounds.py` has SHA `dcf57f151fd34865907bfa80f8fc063e5d46dbf69201ebee7e0a9b19b26fd2b7`. Complete inspection found only finite SymPy/unittest calculations and stdout output. Four sequential fresh processes were run with one thread in the BLAS/OpenMP environment, with bytecode writing disabled and an isolated working directory:

* Normal Python: all 18 named test methods passed.
* `python -O`: the same 18 methods passed; the full JSON stdout is byte-identical to the normal run and to the delivered successful payload.
* Normal `--fail-control`: exit 1 with the declared explicit exception.
* Optimized `--fail-control`: the same declared exit 1.

The failure option executes before the test suite is loaded. These are two guard-failure controls with **zero test methods executed and zero mathematical formula mutants**. They do not test mutation sensitivity of the analytic argument. All 37 entries in the inherited Gamma manifest were independently checked against the retained original Gamma files. The inherited 17-method executions are historical in this intake; their earlier root replay remains a separate record.

The fresh receipts are `work/arithmetic_endpoint_intake_replay_20260913/REPLAY.json` and `HTML_MATH_AUDIT.json`. The replay helper is `work/replay_arithmetic_endpoint_intake_20260913.py`. Its first byte-parser attempt stopped before all executions on the standard no-final-newline marker; the parser was repaired to retain that marker's exact semantics, after which all byte comparisons and all four executions completed. No delivered code or proof was repaired to obtain passing tests.

## 2. Original measure and the two exact quotient maps

Let

\[
g(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=2\xi(s),\qquad
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\qquad d=\deg h.
\]

The packet is fixed and finite, and each selected multiplicity is the actual full order of the zero of the entire nonzero function \(g\). Hence the unique holomorphic continuation \(v_h\) defined by \(g=hv_h\) is entire and nonzero. Define the original density and mass

\[
w_h(t)=\frac{|v_h(1/2+it)|^2}{2\pi},\quad
\mu_h=\int_{\mathbb R}w_h(t)\,dt,\quad
m_{h,k}=w_h^{*k},\quad \int m_{h,k}=\mu_h^k.
\]

No symmetry of the selected packet is required for the analytic norm theorem. Put \(c=k/2\). The source norm of \(P\in\mathbb C[S]\) is

\[
\|\mathcal V_{h,k}P\|^2=\int_{\mathbb R}|P(c+iu)|^2m_{h,k}(u)\,du.
\]

It is positive for every nonzero polynomial: the density is positive almost everywhere, and a nonzero polynomial has only finitely many real-line zeros. All moments exist by the exponential estimate proved below. Finite-dimensional projection therefore gives a unique monic minimizer \(p_n\), with positive squared norm \(\omega_{h,k,n}\), for each \(n\ge0\).

Writing \(\mathcal P_n=\mathbb C[S]_{\le n}\) and \(\mathcal P_j=0\) for \(j<0\), the leading coefficient map gives

\[
0\longrightarrow\mathcal P_{n-1}\longrightarrow\mathcal P_n
\xrightarrow{\operatorname{lc}_n}\mathbb C\longrightarrow0,
\qquad n\ge0.
\]

For monic \(\chi\) of degree \(q\ge1\), Euclidean division proves, for every \(n\ge q-1\),

\[
0\longrightarrow\mathcal P_{n-q}\xrightarrow{\times\chi}\mathcal P_n
\xrightarrow{\pi_\chi}\mathbb C[S]/(\chi)\longrightarrow0.
\]

The first arrow is injective because \(\mathbb C[S]\) is a domain; its image consists exactly of the degree-\(\le n\) multiples of \(\chi\). The remainder has degree \(<q\le n+1\), proving surjectivity of the last arrow at the stated endpoint. For \(n\ge q\), multiplication by \(\chi\) induces the exact isomorphism

\[
\overline{\times\chi}:\mathcal P_{n-q}/\mathcal P_{n-q-1}
\xrightarrow{\sim}\mathcal P_n/\mathcal P_{n-1},\qquad
\operatorname{lc}_n(\chi Q)=\operatorname{lc}_{n-q}Q.
\]

**Required typing correction to the sentence after source (13):** this graded isomorphism requires \(n\ge q\). At \(n=q-1\) its proposed source is zero while the target leading line has dimension one. The exact sequence at \(n=q-1\) remains valid, with zero relation source and \(\mathcal P_{q-1}\cong\mathbb C[S]/(\chi)\). Thus there is an exact endpoint description, not an identification of unequal spaces.

In each original admitted support fibre \(\lambda\), the lifted map is \((\lambda,P)\mapsto(\lambda,[P]_\chi)\), and it sends \(\tau\) to \(\tau\). Its kernel inside that fibre is precisely the polynomial relation space above, and a relation maps to \((\lambda,0)\). The leading coefficient square commutes because multiplication by the monic polynomial preserves the literal coefficient. The original arithmetic map remains

\[
J^{(k)}\mathcal V_{h,k}=\eta_{h,k}\pi_\chi,\qquad
\eta_{h,k}[P]=\upsilon_h^{\otimes k}P(A_k)1,
\quad \upsilon_h=j_h(g/h).
\]

These are the delivered original theta-source identities. The present norm proof uses their explicitly specified norm integral and does not replace the Taylor unit or the target of either map.

## 3. Full local mass argument and all compact cases

For \(|T|\ge10\) let \(f_T(z)=\zeta(1/2+iT+iz)\). The Joukowski image of \(|w|=8\) is the ellipse with semiaxes \(a=65/16\), \(b_0=63/16\). On and inside it, the image coordinate \(s\) satisfies

\[
-55/16\le\Re s\le71/16,\qquad
|\Im s-T|\le65/16,\qquad |\Im s|\ge95/16>0.
\]

The pole at \(s=1\) is consequently outside an open neighbourhood of the filled ellipse. For \(\sigma=\Re s\ge1/4\), summing \(\lfloor x\rfloor\) on \(\sigma>1\), then using locally uniform absolute convergence on \(\sigma>0\), gives

\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx,
\quad \left|\int_1^\infty\{x\}x^{-s-1}dx\right|\le\frac1\sigma\le4.
\]

The denominator \(|s-1|\) stays bounded away from zero on this set and \(|s|=O(1+|T|)\), so this part has a uniform \(O(1+|T|)\) bound. For \(\sigma\le1/4\), the functional equation and vertical-strip Gamma bound give

\[
\zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s),
\]

\[
|\sin(\pi s/2)\Gamma(1-s)|
\le C(1+|\Im s|)^{1/2-\sigma}.
\]

Here \(\Re(1-s)\in[3/4,71/16]\), so the preceding integral estimate bounds \(\zeta(1-s)\) by \(C'(1+|T|)\). The power is at most \(3/2+55/16=79/16<5\). All factors \(2^\sigma\pi^{\sigma-1}\) have fixed compact real range. Consequently one finite \(C_0\ge1\) gives

\[
|f_T(z)|\le M_T=C_0(1+|T|)^6
\]

on the full ellipse. The open neighbourhood noted above validates Cauchy's formula on each closed unit disc centred in \([-1,1]\): the discs lie in \(|\Re z|\le2, |\Im z|\le1\), and \(4/a^2+1/b_0^2<1\) (both semiaxes exceed three). Hence \(\sup_{[-1,1]}|f_T'|\le M_T\).

Let \(r_*=(3+\sqrt{13})/2\), so \(r_*-r_*^{-1}=3\), \(r_*<4\), and \(z_*=(-ir_*+(-ir_*)^{-1})/2=-3i/2\). The absolutely convergent Möbius series at real part two gives

\[
|\zeta(2+iT)|\ge c_*:=\zeta(2)^{-1}>0.
\]

The holomorphic function \(F_T(w)=f_T((w+w^{-1})/2)\) on \(1<|w|<8\) has inner-boundary bound \(m_T=\max_{[-1,1]}|f_T|>0\) and outer-boundary bound \(M_T\). Subtract from \(\log|F_T|\) the harmonic function linear in \(\log|w|\) with those boundary values. The subharmonic maximum principle, including any zeros of \(F_T\), gives

\[
c_*\le m_T^\vartheta M_T^{1-\vartheta},\quad
\vartheta=1-\frac{\log r_*}{\log8}>\frac13.
\]

Therefore \(m_T\ge c_*^{1/\vartheta}M_T^{-(1/\vartheta-1)}\ge c_*^3M_T^{-2}\), since \(0<c_*<1\), \(M_T\ge1\), \(1/\vartheta<3\). A maximizing point of the interval has a direction into the interval with at least one unit of available length. Since \(m_T\le M_T\), the length \(\ell=m_T/(2M_T)\le1/2\) fits in that direction. The derivative bound implies \(|f_T|\ge m_T/2\) on it. Thus

\[
I(T):=\int_{T-1}^{T+1}|\zeta(1/2+it)|^2dt
\ge\ell(m_T/2)^2
=\frac{m_T^3}{8M_T}
\ge\frac{c_*^9}{8C_0^7}(1+|T|)^{-42}.
\]

On \([-10,10]\), write \(I(T)=\int_{-1}^1|\zeta(1/2+i(T+x))|^2dx\). Continuity and uniform boundedness on a compact set give continuity in \(T\). If any such integral were zero, its continuous nonnegative integrand would vanish throughout a whole interval, and the identity theorem on the pole-free neighbourhood of the critical line would force \(\zeta\) identically zero, contradicting \(\zeta(2)>0\). Hence \(I_{\min}=\min_{[-10,10]}I(T)>0\). The literal choice

\[
c_\zeta=\min\{I_{\min},c_*^9/(8C_0^7)\}>0
\]

proves source (23) for every real \(T\), including the transition endpoints.

## 4. Carry every original factor to the convolution lower bound

Stirling's formula on the vertical line and the fact that Gamma has neither zeros nor poles at \(1/4+it/2\) show that

\[
c_\Gamma:=\inf_{t\in\mathbb R}
|\Gamma(1/4+it/2)|^2(1+|t|)^{1/2}e^{\pi|t|/2}>0.
\]

Indeed the expression has a positive finite limit as \(|t|\to\infty\); on the intervening compact set it is continuous and strictly positive. This supplies the stated global Gamma lower bound, including \(t=0\).

Let \(H_h=\prod_\rho(1+|\rho-1/2|)^{m_\rho}\). The triangle inequality gives \(|h(1/2+it)|\le H_h(1+|t|)^d\). Applying this to the entire identity \(g=hv_h\) gives \(|v_h|^2\ge |g|^2/[H_h^2(1+|t|)^{2d}]\) even at a selected centre: the denominator used is strictly positive and is never the zero value of \(h\). On the line, \(|s(s-1)|^2=(t^2+1/4)^2\) and \(|\pi^{-s/2}|^2=\pi^{-1/2}\). Moreover

\[
\frac{(t^2+1/4)^2}{(1+|t|)^{1/2}}\ge\frac1{16\sqrt2}.
\]

For \(|t|\le1\) this follows by numerator \(\ge1/16\) and denominator \(\le\sqrt2\); for \(|t|\ge1\) it follows from \(|t|^4/\sqrt{2|t|}\ge1/\sqrt2\). Thus a literal permissible source constant is

\[
c_h^{(0)}=\frac{c_\Gamma}{32\sqrt2\,\pi^{3/2}H_h^2},\quad
\alpha_0=\pi/2,
\]

and

\[
w_h(t)\ge c_h^{(0)}e^{-\alpha_0|t|}(1+|t|)^{-2d}
|\zeta(1/2+it)|^2.
\]

When \(|t-T|\le1\), \(|t|\le|T|+1\) and \(1+|t|\le2(1+|T|)\). Set

\[
B_h=42+2d,\qquad
c_h^{(1)}=c_h^{(0)}e^{-\alpha_0}2^{-2d}c_\zeta>0.
\]

Integrating proves the exact lower local mass

\[
\int_{T-1}^{T+1}w_h(t)dt\ge c_h^{(1)}e^{-\alpha_0|T|}(1+|T|)^{-B_h}.
\]

For completeness, the analytic upper properties used next also follow from the actual density. For sufficiently large \(|t|\), each factor \(|1/2+it-\rho|\ge|t|/2\). The upper Gamma estimate, the real-part-\(1/2\) integral estimate for zeta above, and this lower bound for \(h\) give an exponential \(e^{-\alpha_0|t|}\) times a fixed polynomial upper bound for \(w_h\). On compact sets its entire definition is continuous and bounded. It is therefore bounded and integrable and has finite Laplace values for \(|b|<\alpha_0\). Its zero set on the real line is discrete, because \(v_h\) is nonzero entire, so \(w_h>0\) almost everywhere.

For each real \(u\), the product \(w_h(t)w_h(u-t)\) is positive almost everywhere, integrable, and has a positive integral. In addition

\[
\|(w_h*w_h)(\cdot+a)-(w_h*w_h)\|_\infty
\le\|w_h\|_\infty\|w_h(\cdot+a)-w_h\|_1\longrightarrow0.
\]

Hence \(m_{h,2}\) is continuous and strictly positive. The quantities

\[
b_h=\min_{|v|\le1}m_{h,2}(v)>0,\quad
\vartheta_h=\int_{-1}^1w_h(v)dv>0,\quad c_h=b_hc_h^{(1)}>0
\]

are actual compact observations of the original measure. Restricting the positive convolution integral gives

\[
m_{h,3}(u)=\int w_h(t)m_{h,2}(u-t)dt
\ge b_h\int_{u-1}^{u+1}w_h(t)dt
\ge c_he^{-\alpha_0|u|}(1+|u|)^{-B_h}.
\]

For \(k>3\), the exact convolution integral is over \(v_4,\ldots,v_k\in\mathbb R\), with first factor \(m_{h,3}(u-\sum v_a)\). Tonelli applies. Restrict it to \([-1,1]^{k-3}\), where \(|\sum v_a|\le k-3\), and integrate each remaining factor. This proves, including \(k=3\) with an empty product,

\[
m_{h,k}(u)\ge c_h\vartheta_h^{k-3}
e^{-\alpha_0(|u|+k-3)}(1+|u|+k-3)^{-B_h}.
\]

Every factor in the omitted complement remains in the original nonnegative integral. There is no conclusion at \(k=1,2\) by substituting a negative number of factors. The density still has mass \(\mu_h^k\).

## 5. Exact monic norm and literal uniform constant

Fix \(0<b<\alpha_0\), and define \(M_h(\pm b)=\int e^{\pm bt}w_h(t)dt\). Tonelli and the definition of convolution give

\[
\int e^{\pm bu}m_{h,k}(u)du=M_h(\pm b)^k,
\quad\int e^{b|u|}m_{h,k}(u)du\le M_h(b)^k+M_h(-b)^k.
\]

The nonnegative exponential series implies \(|u|^{2j}\le(2j)!b^{-2j}e^{b|u|}\). The literal monic trial polynomial \((S-c)^j\) becomes \(i^ju^j\) on the original integration line. Consequently

\[
\omega_{h,k,j}\le(2j)!b^{-2j}[M_h(b)^k+M_h(-b)^k],\qquad j\ge0.
\]

The Legendre constant can be derived without dropping its leading coefficient. Let

\[
P_j(x)=\frac1{2^jj!}\frac{d^j}{dx^j}(x^2-1)^j,
\qquad \ell_j=\frac{(2j)!}{2^j(j!)^2}.
\]

Integration by parts \(j\) times proves its orthogonality against every polynomial of degree below \(j\), because the boundary terms vanish to the required orders. The same integration gives

\[
\int_{-1}^1P_j(x)^2dx
=\frac{\ell_j}{2^j}\int_{-1}^1(1-x^2)^jdx
=\frac{\ell_j}{2^j}\frac{2^{2j+1}(j!)^2}{(2j+1)!}
=\frac2{2j+1}.
\]

The beta integral in the middle equality follows by \(x=2y-1\) and integration by parts for \(\int_0^1y^j(1-y)^jdy=(j!)^2/(2j+1)!\). Thus the monic polynomial \(L^j\ell_j^{-1}P_j(u/L)\) has squared norm

\[
\mathfrak l_j(L)=\frac{2L^{2j+1}}{2j+1}
\left(\frac{2^j(j!)^2}{(2j)!}\right)^2.
\]

Any other polynomial with the same leading coefficient differs by a lower-degree polynomial. Orthogonality gives an exact sum of squared norms, proving minimality and uniqueness. A monic \(S\)-polynomial maps to a \(u\)-polynomial with leading coefficient \(i^j\). The explicit inverse image of the interval minimizer is

\[
\frac{i^jL^j}{\ell_j}P_j\left(\frac{S-c}{iL}\right),
\]

whose \(S^j\) coefficient is \(i^j i^{-j}=1\). This proves the claimed lower bound at the original coordinate type. Multiplication by the inside and outside characteristic functions is the exact isometry

\[
L^2(m_{h,k}du)\longrightarrow
L^2([-L,L],m_{h,k}du)\oplus L^2(\mathbb R\setminus[-L,L],m_{h,k}du),
\]

with inverse addition after extension by zero. Applying the lower envelope to its first component gives

\[
\omega_{h,k,j}\ge c_h\vartheta_h^{k-3}
e^{-\alpha_0(L+k-3)}(1+L+k-3)^{-B_h}\mathfrak l_j(L),
\quad k\ge3,\ j\ge0,\ L>0.
\]

Taking \(j=n,L=n\) here and \(j=2n\) above gives exactly source (35). To verify the constant in source (36), put

\[
M_* =\max\{1,M_h(b),M_h(-b)\},\quad
C_c=\max(1,c_h^{-1}),\quad C_\vartheta=\max(1,\vartheta_h^{-1}).
\]

The central binomial estimate \(\binom{2n}{n}\le4^n\) gives
\(\mathfrak l_n(n)\ge2n^{2n+1}/((2n+1)4^n)\). Combining the factor 2 from the two Laplace values with this prefactor, before taking roots, yields

\[
\left(\frac{2(4n)!}{\mathfrak l_n(n)}\right)^{1/(2n)}
\le32n(2+1/n)^{1/(2n)}\le64n.
\]

The first inequality uses \((4n)!\le(4n)^{4n}\). For the second, \(2+1/n\le4^n\) for every integer \(n\ge1\). For \(n\ge k\ge3\), the remaining factors satisfy

\[
M_*^{k/(2n)}\le\sqrt{M_*},\quad
c_h^{-1/(2n)}\le\sqrt{C_c},\quad
\vartheta_h^{-(k-3)/(2n)}\le\sqrt{C_\vartheta},
\]

\[
e^{\alpha_0(n+k-3)/(2n)}\le e^{\alpha_0},\quad
(1+n+k-3)^{B_h/(2n)}\le(2n)^{B_h/(2n)}
\le2^{B_h/2}e^{B_h/(2e)}.
\]

The final inequality follows by differentiating \(\log x/x\), whose maximum on \(x>0\) is \(1/e\). The factor \(b^{-4n}\) becomes exactly \(b^{-2}\). Multiplying proves the literal sufficient constant

\[
\boxed{C_h=64b^{-2}e^{\alpha_0}2^{B_h/2}e^{B_h/(2e)}
\sqrt{M_*\max(1,c_h^{-1})\max(1,\vartheta_h^{-1})}}
\]

and the theorem

\[
\boxed{\left(\frac{\omega_{h,k,2n}}{\omega_{h,k,n}}\right)^{1/(2n)}\le C_hn,
\qquad n\ge k\ge3.}
\]

The packet and the chosen \(b\) determine a finite constant; neither \(k\) nor \(n\) enters it. The compact minima are proved positive, and they have not been numerically enclosed. The same argument gives source (37) for integers \(k\ge3,n\ge0,r\ge1\) and \(L>0\), with numerator degree \(n+r\), exponent \(1/(2r)\), and all factors exactly as printed. An endpoint selection additionally requires \(n\ge q\).

## 6. Exact composition with the delivered endpoint theorem

The complete immutable PR23 note was read at commit `c720f40530eed2f5969dbabe94dfd3fddc0f507f`, from `work/endpoint_criterion_pr23_c720f405_20260913.md`. Only its endpoint theorem is used here. Its original local source estimate is

\[
0\le\epsilon_N\le A_N\sinh x_N,\quad
A_N=\sqrt{\omega_{N+1}/\omega_N}>0,\quad
x_N=\tfrac12\log(V_{N-1}/V_{N+1})\ge0.
\]

For a window \(N=n,\ldots,n+r-1\), \(n\ge q,r\ge1\), if one \(x_N=0\), the corresponding nonnegative allowance is zero. Otherwise \((\log\sinh x)''=-1/\sinh^2x<0\), so finite Jensen gives

\[
\prod\sinh x_N\le\sinh\left(\frac1r\sum x_N\right)^r.
\]

The minimum allowance raised to \(r\) is bounded by the product of the allowances. Both exact products telescope:

\[
\prod A_N=\sqrt{\omega_{n+r}/\omega_n},\qquad
2\sum x_N=\log\frac{V_{n-1}V_n}{V_{n+r-1}V_{n+r}}.
\]

Taking nonnegative roots proves source (38). The finite minimum is attained inside the existing family. Choosing \(r=n\ge\max(q,k)\), \(k\ge3\), and using the just-proved norm theorem yields source (39) with its original \(C_h\).

For the packet consisting exactly of a nonreal off-line quartet with common actual multiplicity \(m\), put \(\ell=1+k(m-1)\). The inherited aggregate exterior result supplies

\[
q_k=\ell(k+1)^2,\qquad
L_{h,k}=2\delta\ell(k+1)\left\lfloor\frac{(k+1)^2}{4}\right\rfloor
\le\epsilon_{h,k,N}
\]

at every admitted degree. The elementary finite sum behind the count is
\(\sum_{a>k/2}(2a-k)=\lfloor(k+1)^2/4\rfloor\). If \(k\) is even, \(4\lfloor(k+1)^2/4\rfloor=k(k+2)\ge k(k+1)\); if \(k\) is odd, it equals \((k+1)^2\ge k(k+1)\). Hence \(q_k\ge k\) and \(L_{h,k}/q_k\ge\delta k/2\). Applying (39) at \(n=q_k\) gives

\[
\mathcal B_{h,k}:=\log\frac{V_{q_k-1}V_{q_k}}{V_{2q_k-1}V_{2q_k}}
\ge2q_k\operatorname{arsinh}\left(\frac{\delta k}{2C_h}\right).
\]

For \(a>0\), \(\operatorname{arsinh}(ak)=\log k+\log(a+\sqrt{a^2+k^{-2}})\); its second summand tends to \(\log(2a)\). Dividing proves the source's threshold \(\liminf\mathcal B_{h,k}/(q_k\log k)\ge2\). This implication uses the existing exterior lower theorem; it does not assert the existence of such a quartet. Later exact-radius improvements belong to the parallel product lane and are not asserted to have been proved by the present delivered source.

## 7. Complete block boundary isomorphism and determinant transport

Here \(q\ge1\), \(i<j\), and \(i\ge q-1\). In the polynomial source let \(\mathcal D_a=\ker(\pi_\chi|_{\mathcal P_a})\). In the actual Hilbert source these are their images under the injective source map. Let \(R_i:E\to\mathcal P_i\) be the unique minimum norm section of \(\pi_\chi\), and \(G_i=R_i^*R_i\), with all adjoints taken in the stated original source metric and the fixed remainder coordinates. Let

\[
Tz=\sum_{a=i+1}^{j}z_a p_a,\quad
F=\pi_\chi T=[b_{i+1},\ldots,b_j],\quad
\Omega=\operatorname{diag}(\omega_{i+1},\ldots,\omega_j).
\]

The original orthogonality gives \(T^*T=\Omega\), \(T^*R_i=0\), and \(T^*\mathcal D_i=0\). Since \(R_i\perp\mathcal D_i\), the map \(B=T-R_iF\) takes values in \(\mathcal D_j\cap\mathcal D_i^\perp\). It has zero remainder because \(\pi_\chi R_i=I\). Its coefficients along the basis \(p_{i+1},\ldots,p_j\) are exactly \(z\), so it is injective. For any \(d\) in that intersection, choose \(z\) to be these upper coefficients of \(d\). Then \(d-Bz\in\mathcal P_i\), has zero remainder, and is perpendicular to \(\mathcal D_i\). Thus \(d-Bz=0\). This proves surjectivity and its explicit inverse.

The exact Gram and pairing identities are

\[
B^*B=H:=\Omega+F^*G_iF>0,\qquad B^*R_i=-F^*G_i.
\]

The section

\[
\widetilde R=R_i+BH^{-1}F^*G_i
\]

has remainder identity, is perpendicular to \(\mathcal D_i\), and satisfies \(B^*\widetilde R=-F^*G_i+HH^{-1}F^*G_i=0\). Since \(\mathcal D_j=\mathcal D_i\oplus\operatorname{im}B\) is the proved orthogonal decomposition, \(\widetilde R=R_j\). Expanding its Gram gives

\[
G_j=G_i-G_iFH^{-1}F^*G_i.
\]

An alternative direct kernel derivation retains the same maps: in the orthogonal monic basis,
\(K_i=G_i^{-1}=\sum_{a=0}^i b_a b_a^*/\omega_a\), hence

\[
K_j=K_i+F\Omega^{-1}F^*,\qquad
\frac{V_i}{V_j}=\det(I+\Omega^{-1}F^*G_iF).
\]

The determinant identity follows from \(V_i/V_j=\det K_j/\det K_i\) and \(\det(I+AB)=\det(I+BA)\). To specify its positive spectral type, \(\Omega^{-1}F^*G_iF\) is conjugate by \(\Omega^{1/2}\) to the Hermitian positive semidefinite matrix \(\Omega^{-1/2}F^*G_iF\Omega^{-1/2}\). Its eigenvalues are precisely the generalized eigenvalues of the pair \((F^*G_iF,\Omega)\). Therefore the determinant equals \(\prod_a(1+\lambda_a)>0\). Applying it to \((i,j)=(q-1,2q-1)\) and \((q,2q)\), then taking real logarithms, proves source (47). Integrating \((1+x)^{-1}\le1\) from 0 to \(\lambda_a\) gives \(\log(1+\lambda_a)\le\lambda_a\), proving (48) with its two separately typed matrices.

In original theta source coordinates, each column of \(B\) is the source image of a uniquely divisible polynomial \(\chi Q\). Thus its original cochain primitive is the inherited fixed-order division primitive for that \(Q\), and linear combination gives a primitive for every block column. The exact transport is

\[
\mathbb C^{j-i}\xrightarrow{B}\mathcal D_j/\mathcal D_i
\hookrightarrow\mathscr B^{\widehat\otimes k}/\mathcal D_i
\longrightarrow\mathscr B^{\widehat\otimes k}/\mathcal D_j.
\]

The final composite vanishes because the representative lies in \(\mathcal D_j\). Its marked lift remains the receiving fibre's supported zero. The direct-sum proof and the displayed Gram keep all source norms and pairings before this projection.

## 8. The confluent formula's exact domain and full-order bridge

The complete immutable PR24 note was fetched from commit `dfcbba5cbf7fec8c9301fe242c13e741d762013e` into `work/pr24_confluent_transfer_dfcbba5_20260913.md` (14007 bytes, SHA `d1046b75762e4248ded8f0b901c1ac12dc01065e4e684ca2d166b6a535425763`) and read in full. Its source determinant identity, source (41), gives source (42) simply by substitution of \(N=q-1,q,2q-1,2q\), for which \(a=N-q+1\) is exactly \(0,1,q,q+1\). Each numerator and denominator retains its product of \(q\) original monic norms. The common raw Vandermonde cancels in this quotient because it occurs twice on each side and is nonzero.

There is a domain precision needed when applying that raw-jet presentation to arbitrary finite packets. Define the exact ring map \(\Psi P=P(c+iu)\), and put \(\psi=i^{-q}\Psi\chi\), which is monic. The norm multiplier is always

\[
\Pi(u)=\overline\chi(c-iu)\chi(c+iu)=\overline\psi(u)\psi(u),
\]

of degree \(2q\), real and nonnegative on the real line. The formula \(\Pi=\psi^2\) with every node length doubled requires \(\psi\) real, equivalently invariance of the original root multiset under \(S\mapsto k-\overline S\). The exact quartet satisfies this. For an arbitrary packet, take the union of the roots of \(\psi\) and their conjugates, adding their orders whenever nodes coincide. These are the actual full orders of \(\Pi\). The raw jet map then has kernel exactly \((\Pi)\) by polynomial divisibility and has dimension \(2q\). Its Vandermonde is

\[
\det\mathsf V=
\left(\prod_a\prod_{d=0}^{r_a-1}d!\right)
\prod_{a<b}(z_b-z_a)^{r_ar_b}
\]

in the fixed displayed node and derivative order. The coefficient \(d\) in multiplication-by-\(u\) on raw jets remains \((Xv)_{a,d}=z_av_{a,d}+dv_{a,d-1}\).

The transfer proof itself applies to this general \(\Pi\): if a linear combination of \(Q_a,\ldots,Q_{a+2q-1}\) has all these raw jets zero, it equals \(\Pi H\) with \(\deg H<a\). Orthogonality gives \(0=\int\Pi|H|^2m_{h,k}\), which forces \(H=0\). Thus the actual jet matrix \(\mathsf F_a\) is invertible. Dividing the unique raw-jet cancellation of \(Q_{a+2q}\) by \(\Pi\) gives the monic relation-weight polynomial. Its norm is \(-d_{a,0}\omega_a>0\), and shifting the \(2q\) source columns gives \(\det\mathsf F_{a+1}/\det\mathsf F_a=-d_{a,0}\), with sign \((-1)^{2q-1}=-1\). Multiplication yields the relation/source determinant ratio; the original Schur determinant then gives (41). Therefore the analytic theorem remains valid for all fixed finite packets, and the literal doubled-node description is applied only on its proven symmetry domain. The parallel endpoint-product proof is expanding this transfer in its complete original coordinate dictionary.

## 9. Source-review claims and research integration status

The delivered source review records selected readings from a six-part S20 archive, its 216580466-byte concatenation and hash, and the discrepancy between an old TeX `<=2` and a current page record `<2` in Deligne 3.2.10, together with an explicit squared-eigenvalue correction. That external archive and its selected passages are **not included** among these 32 members. This intake has verified the complete delivered report and its manifest bytes; it does not independently reassert reassembly or inspection of files that it has not opened. The arithmetic estimate proved here uses the stated classical zeta/Gamma/Legendre facts and no finite-field purity theorem.

The resulting deliverable establishes a full written norm theorem at the original measure and a finite exact block-volume comparison. Its only newly identified literal source correction is the endpoint domain of the graded multiplication isomorphism; the raw-confluent symmetry domain is made explicit when applying the cited upstream presentation beyond quartets. Neither correction changes the dyadic norm proof or its constant. The theorem composes with the existing finite endpoint criterion exactly as shown. The growing-degree upper estimate for the quotient volumes is not a theorem of this delivery. The independently developing exact-radius and balanced-window improvements are separate additions; they should receive their own proof bodies and provenance before the next cumulative publication.

Classical primary references for the exact functions used above are [DLMF 25.4, Reflection Formulas](https://dlmf.nist.gov/25.4), [DLMF 5.11, Asymptotic Expansions](https://dlmf.nist.gov/5.11), and [DLMF 18.5, Explicit Representations](https://dlmf.nist.gov/18.5). The independent analytic review supplies its actual source-access record and a second full derivation.
