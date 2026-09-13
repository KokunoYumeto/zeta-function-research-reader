# Independent audit of the theta seed moments and gamma coefficients

This audit reads the complete `work/toda_theta_input_tail_20260912.tex`, the complete delivered `RESEARCH_NOTE.md`, and the complete delivered `evaluate_seed_coefficients.py`. It audits the exact moment construction through spectral degree six and the proposed positive omitted-integer tail. It does not execute the delivered numerical driver, modify the source delivery, certify a numerical interval, or run Lean.

The source bytes read have SHA-256 hashes:

| Source | SHA-256 |
|:--|:--|
| `work/toda_theta_input_tail_20260912.tex` | `e50a11c51293017b1a433f3ed9b499947a953e6b2955f59f3c46f14ed26a409d` |
| `sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent/RESEARCH_NOTE.md` | `886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b` |
| `sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent/evaluate_seed_coefficients.py` | `50986940edea09082d692746d261d672d0cf309ad4f49da9428760272c6f1dc8` |

The `sources` paths are relative to the cumulative continuation directory. The exact source locators are TI.2, TI.11, TI.25–TI.30; Gamma research note Section 4.1, equations (13) and (24), and Section 6.2 beginning at line 440; and the numerical driver's lines 8–30. Independent symbolic expansion using rational SymPy arithmetic agreed with every coefficient derived below. That finite cross-check supplements the calculations written here; it supplies no analytic or floating-point error claim.

## 1. The derivative polynomials, with the original theta factor

On the positive axis retain the original operator, original theta function, and original Mellin transform:

\[
D=-x\frac{d}{dx},\quad L=D-\frac12,\quad
f_0(x)=\sum_{n\ge1}P_0(\pi n^2x^2)e^{-\pi n^2x^2},\quad
P_0(y)=8y^2-12y,
\]

\[
g(s)=\int_0^\infty f_0(x)x^{s-1}\,dx=2\xi(s),\qquad
w_1(t)=\frac{|g(1/2+it)|^2}{2\pi}.
\]

Define \(H_r=L^rf_0\), for every integer \(r\ge0\). For a polynomial \(P\), the literal substitution \(y=\pi n^2x^2\) gives \(D=-2y\partial_y\) on its summand. Therefore

\[
L(P(y)e^{-y})=
\left[-2yP'(y)+(2y-1/2)P(y)\right]e^{-y}.
\]

Consequently the exact recurrence and representation are

\[
P_{r+1}(y)=-2yP_r'(y)+(2y-1/2)P_r(y),\qquad
H_r(x)=\sum_{n\ge1}P_r(\pi n^2x^2)e^{-\pi n^2x^2}.
\tag{IR.1}
\]

The original TI endpoint and compact-sector Gaussian bounds justify these derivatives term by term, to every fixed finite order. Write \(P_r(y)=\sum_a p_{r,a}y^a\), extending the coefficients by zero outside their support. Equating coefficients in (IR.1) proves

\[
p_{r+1,a}=2p_{r,a-1}-(2a+1/2)p_{r,a}.
\tag{IR.2}
\]

The recurrence keeps the constant coefficient zero, raises the degree by exactly one, and multiplies the leading coefficient by two. In particular \(\deg P_r=r+2\) and its leading coefficient is \(2^{r+3}\). Literal application of (IR.2) gives

\[
\begin{aligned}
P_0(y)&=8y^2-12y,\\
P_1(y)&=16y^3-60y^2+30y,\\
P_2(y)&=32y^4-224y^3+330y^2-75y,\\
P_3(y)&=64y^5-720y^4+2116y^3-1635y^2+\frac{375}{2}y.
\end{aligned}
\tag{IR.3}
\]

For example, the coefficients of \(P_3\) are obtained from those of \(P_2\) as follows:

\[
\begin{aligned}
p_{3,1}&=-\frac52(-75)=\frac{375}{2},\\
p_{3,2}&=2(-75)-\frac92(330)=-1635,\\
p_{3,3}&=2(330)-\frac{13}{2}(-224)=2116,\\
p_{3,4}&=2(-224)-\frac{17}{2}(32)=-720,\\
p_{3,5}&=2(32)=64.
\end{aligned}
\]

The half-integer \(375/2\) is required. The delivered driver uses \(q_0=4y^2-6y\) and the same linear recurrence. The exact morphism between its polynomial representation and (IR.1) is

\[
q_r\longmapsto P_r=2q_r,
\qquad
H_r=2\sum_{n\ge1}q_r(\pi n^2x^2)e^{-\pi n^2x^2}.
\tag{IR.4}
\]

It follows by induction from the initial values and recurrence. No theta coefficient or source function is changed by expressing this relationship.

## 2. Fourier sign, inversion parity, and the exact even moments

The unitary map used in TI.11 is

\[
U:L^2((0,\infty),dx)\longrightarrow L^2(\mathbb R,dy),
\qquad (UF)(y)=e^{y/2}F(e^y).
\]

Differentiation gives \(ULF=-(UF)'\). With the specified Fourier convention

\[
(\mathcal F_+u)(t)=\int_{\mathbb R}u(y)e^{ity}\,dy,
\]

integration by parts gives \(\mathcal F_+(u')=-it\mathcal F_+u\). The endpoint bounds justify every boundary term and give

\[
\mathcal F_+(UH_r)(t)=(it)^r g(1/2+it).
\tag{IR.5}
\]

Thus the original, unscaled spectral moments are

\[
\mu_{2r}:=\int_{\mathbb R}t^{2r}w_1(t)\,dt
=\frac1{2\pi}\int_{\mathbb R}|(it)^rg(1/2+it)|^2\,dt
=\int_0^\infty H_r(x)^2\,dx.
\tag{IR.6}
\]

The last equality uses the original Plancherel factor \(1/(2\pi)\) and the specified unitary map. The functions \(H_r\) are real on the positive axis by (IR.1).

For the linear inversion \((RF)(x)=x^{-1}F(1/x)\), direct differentiation gives \(DR=R(1-D)\), hence \(RL=-LR\). Since \(Rf_0=f_0\), induction yields

\[
RH_r=(-1)^rH_r,
\qquad H_r(1/x)=(-1)^rxH_r(x).
\tag{IR.7}
\]

Substituting \(x=1/u\) in the integral from zero to one, and using the actual Jacobian \(u^{-2}\), proves

\[
\int_0^1H_r(x)^2\,dx
=\int_1^\infty H_r(1/u)^2u^{-2}\,du
=\int_1^\infty H_r(u)^2\,du.
\]

Consequently

\[
\boxed{\mu_{2r}=2\int_1^\infty H_r(x)^2\,dx.}
\tag{IR.8}
\]

Both the phase \((it)^r\) and inversion sign \((-1)^r\) are retained before the absolute square. The seed is even in the spectral coordinate because \(g(1/2-it)=\overline{g(1/2+it)}\); therefore its odd spectral moments vanish. No statement about parity for an arbitrary packet is used here.

## 3. Exact finite integer sum and positive omitted tail

Let \(J\ge0\) be an integer and let \(H_{r,J}\) be (IR.1) restricted to \(1\le n\le J\). For real \(C>0\), define the original integral

\[
I_p(C)=\int_1^\infty x^pe^{-Cx^2}\,dx
=\frac{\Gamma((p+1)/2,C)}{2C^{(p+1)/2}}.
\tag{IR.9}
\]

Expansion of the finite square gives, with \(C_{mn}=\pi(m^2+n^2)\),

\[
\begin{aligned}
\mu_{2r,J}&:=2\int_1^\infty H_{r,J}(x)^2\,dx\\
&=2\sum_{m,n=1}^J\sum_{a,b=1}^{r+2}
p_{r,a}p_{r,b}(\pi m^2)^a(\pi n^2)^b I_{2a+2b}(C_{mn})\\
&=\sum_{m,n=1}^J\sum_{a,b=1}^{r+2}
p_{r,a}p_{r,b}(\pi m^2)^a(\pi n^2)^b
\frac{\Gamma(a+b+1/2,C_{mn})}{C_{mn}^{a+b+1/2}}.
\end{aligned}
\tag{IR.10}
\]

The endpoint coefficient two and the one-half in (IR.9) cancel exactly in the last line. Replacing each \(p_{r,a}\) by \(2q_{r,a}\) produces the delivered driver's coefficient eight in front of its \(I\)-sum. Its triangular summation uses multiplicity one for \(m=n\) and two for \(m>n\), which equals the full square sum by exchange of the two indices. Its integration recurrence follows from integration by parts:

\[
I_{2j+2}(C)=\frac{j+1/2}{C}I_{2j}(C)+\frac{e^{-C}}{2C},
\qquad
I_0(C)=\frac{\sqrt\pi\,\operatorname{erfc}(\sqrt C)}{2\sqrt C}.
\tag{IR.11}
\]

The driver's loop constructs all indices through \(2(r+2)\), as required for \(a+b\). These algebraic factors and index ranges are correct. The driver's floating-point arithmetic and agreement at two cutoffs are not interval certificates; the positive bound proved next is independent of that agreement.

For integers \(A\ge1\), \(p\ge0\), put \(\rho_A=e^{-\pi(2A+1)}\) and define

\[
\mathscr H_p(A)=
\sum_{j=0}^p\binom pj A^{p-j}
\sum_{b=0}^j
\left\{\begin{matrix}j\\b\end{matrix}\right\}
\frac{b!\rho_A^b}{(1-\rho_A)^{b+1}}.
\tag{IR.12}
\]

The braces denote the nonnegative integers \(S(j,b)\) specified by
\(S(0,0)=1\), zero out-of-range and at \(b=0<j\), and recurrence
\(S(j+1,b)=bS(j,b)+S(j,b-1)\). This is the same finite positive function denoted \(H_p(A,\pi)\) in TI.21; the different font prevents confusion with the differentiated theta function \(H_r(x)\).

For \(x\ge1\), writing \(n=A+v\) and using \(v^2\ge v\) for integers \(v\ge0\) gives

\[
\begin{aligned}
\sum_{n\ge A}n^pe^{-\pi n^2x^2}
&\le e^{-\pi A^2x^2}\sum_{v\ge0}(A+v)^p\rho_A^v\\
&=e^{-\pi A^2x^2}\mathscr H_p(A).
\end{aligned}
\tag{IR.13}
\]

The last equality follows by the binomial expansion, the finite identity
\(v^j=\sum_bS(j,b)(v)_b\), and
\(\sum_{v\ge0}(v)_b\rho^v=b!\rho^b/(1-\rho)^{b+1}\).
The finite identity follows inductively from
\(v(v)_b=(v)_{b+1}+b(v)_b\); the series identity follows by differentiating the geometric series \(b\) times.

Define the fully specified positive constants

\[
\mathscr A_r(A)=\sum_{a=1}^{r+2}|p_{r,a}|\pi^a\mathscr H_{2a}(A).
\tag{IR.14}
\]

Their explicit expansions for the four cases under audit are

\[
\begin{aligned}
\mathscr A_0(A)&=12\pi\mathscr H_2(A)+8\pi^2\mathscr H_4(A),\\
\mathscr A_1(A)&=30\pi\mathscr H_2(A)+60\pi^2\mathscr H_4(A)
 +16\pi^3\mathscr H_6(A),\\
\mathscr A_2(A)&=75\pi\mathscr H_2(A)+330\pi^2\mathscr H_4(A)
 +224\pi^3\mathscr H_6(A)+32\pi^4\mathscr H_8(A),\\
\mathscr A_3(A)&=\frac{375}{2}\pi\mathscr H_2(A)+1635\pi^2\mathscr H_4(A)
 +2116\pi^3\mathscr H_6(A)+720\pi^4\mathscr H_8(A)
 +64\pi^5\mathscr H_{10}(A).
\end{aligned}
\tag{IR.15}
\]

Since every \(a\le r+2\), the inequality \(x^{2a}\le x^{2r+4}\) holds on the specified interval \(x\ge1\). Applying (IR.13) separately to every original signed summand proves

\[
\begin{aligned}
|H_r(x)|,\ |H_{r,J}(x)|
&\le\mathscr A_r(1)x^{2r+4}e^{-\pi x^2},\\
|H_r(x)-H_{r,J}(x)|
&\le\mathscr A_r(J+1)x^{2r+4}e^{-\pi(J+1)^2x^2}.
\end{aligned}
\tag{IR.16}
\]

These bounds also justify absolute summation and integration of the infinite expanded double series. Applying
\(|H_r^2-H_{r,J}^2|\le|H_r-H_{r,J}|(|H_r|+|H_{r,J}|)\) and the actual endpoint coefficient two in (IR.8) gives

\[
\boxed{
|\mu_{2r}-\mu_{2r,J}|
\le 4\mathscr A_r(1)\mathscr A_r(J+1)
I_{4r+8}\!\left(\pi(1+(J+1)^2)\right).
}
\tag{IR.17}
\]

Thus the proposed coefficient four and exponent \(4r+8\) are correct when \(\mathscr A_r\) uses the coefficients of \(P_r\), including the original theta factor two. At \(r=0\), \(\mathscr A_0=2A\) with TI.22 at zero tilt, so (IR.17) equals its coefficient-sixteen tail TI.23. At \(r=1\), \(\mathscr A_1\) is exactly TI.29 and (IR.17) is TI.30. The next two integral indices are sixteen and twenty.

For each fixed \(r\), the denominators in (IR.12) are uniformly bounded away from zero for \(A\ge1\), so \(\mathscr A_r(A)\) is bounded by a constant times \((1+A)^{2r+4}\). Also, for \(C\ge\pi\),
\(I_{4r+8}(C)\le e^{-C}\int_1^\infty x^{4r+8}e^{-\pi(x^2-1)}dx\).
This proves that (IR.17) tends to zero with \(J\); no unknown remainder is left in that estimate.

## 4. The gamma polynomials and all original coefficient denominators

Retain \(\lambda=13/4\), \(\alpha=2\lambda=13/2\), the original coordinate \(t\), and

\[
d\sigma_\lambda(t)=\frac{|\Gamma(\lambda+it/2)|^2}{2\pi}\,dt,
\qquad
c_\lambda=2^{1-2\lambda}\Gamma(2\lambda)
=\frac{10395\sqrt{2\pi}}{4096}.
\tag{IR.18}
\]

The last equality follows by applying \(\Gamma(z+1)=z\Gamma(z)\) six times to \(\Gamma(1/2)=\sqrt\pi\). The actual seed mass remains \(\mu_0\); it is not identified with \(c_\lambda\).

For clarity the recurrence can be obtained directly from the delivered generating function. Set

\[
\mathcal G(t,z)=\sum_{n\ge0}\frac{b_n^{(\lambda)}(t)}{n!}z^n
=(1-iz)^{-\lambda+it/2}(1+iz)^{-\lambda-it/2}.
\]

Logarithmic differentiation at zero with the branches equal to zero for the logarithms at zero gives
\((1+z^2)\partial_z\mathcal G=(t-\alpha z)\mathcal G\).
Coefficient comparison proves

\[
b_0=1,\quad b_1=t,\quad
b_{n+1}=tb_n-n(n+\alpha-1)b_{n-1}.
\tag{IR.19}
\]

For real small \(z,w\), the generating function equals
\((1+z^2)^{-\lambda}e^{t\arctan z}\). The specified gamma Laplace transform
\(\int e^{\theta t}d\sigma_\lambda=c_\lambda\cos^{-\alpha}\theta\)
therefore gives

\[
\int\mathcal G(t,z)\mathcal G(t,w)d\sigma_\lambda(t)
=c_\lambda(1-zw)^{-\alpha}.
\]

Indeed
\(\cos(\arctan z+\arctan w)=(1-zw)/\sqrt{(1+z^2)(1+w^2)}\).
The exponential moments dominate all derivatives for sufficiently small \(z,w\), so comparing coefficients is justified. This proves both orthogonality and the norm

\[
\int b_j(t)b_n(t)d\sigma_\lambda(t)
=\delta_{jn}c_\lambda n!(\alpha)_n.
\tag{IR.20}
\]

Applying (IR.19) successively at \(\alpha=13/2\) gives every intermediate polynomial needed through degree six:

\[
\begin{aligned}
b_0(t)&=1,\\
b_1(t)&=t,\\
b_2(t)&=t^2-\frac{13}{2},\\
b_3(t)&=t^3-\frac{43}{2}t,\\
b_4(t)&=t^4-47t^2+\frac{663}{4},\\
b_5(t)&=t^5-85t^3+\frac{3931}{4}t,\\
b_6(t)&=t^6-\frac{275}{2}t^4+\frac{13801}{4}t^2-\frac{69615}{8}.
\end{aligned}
\tag{IR.21}
\]

For instance the last step is \(b_6=tb_5-(105/2)b_4\), since
\(5(5+13/2-1)=105/2\). It gives coefficients
\(-85-105/2=-275/2\),
\(3931/4+(105/2)47=13801/4\), and
\(-(105/2)(663/4)=-69615/8\), retaining all original terms.

The seed coefficients in the delivered note have exactly the type

\[
c_{1,n}=
\frac{\int_{\mathbb R}b_n^{(\lambda)}(t)w_1(t)\,dt}
{c_\lambda n!(\alpha)_n}.
\tag{IR.22}
\]

The four rising-factorial products are

\[
0!(\alpha)_0=1,\quad
2!(\alpha)_2=\frac{195}{2},\quad
4!(\alpha)_4=\frac{188955}{2},\quad
6!(\alpha)_6=\frac{1368978975}{4}.
\tag{IR.23}
\]

Substituting (IR.21) into (IR.22) and keeping its denominator gives the exact coefficient-to-moment maps

\[
\boxed{\begin{aligned}
c_{1,0}&=\frac{\mu_0}{c_\lambda},\\
c_{1,2}&=\frac{2\mu_2-13\mu_0}{195c_\lambda},\\
c_{1,4}&=\frac{4\mu_4-188\mu_2+663\mu_0}{377910c_\lambda},\\
c_{1,6}&=\frac{8\mu_6-1100\mu_4+27602\mu_2-69615\mu_0}
{2737957950c_\lambda}.
\end{aligned}}
\tag{IR.24}
\]

The numerators before multiplication by the displayed integer factors are respectively
\(\mu_0\),
\(\mu_2-13\mu_0/2\),
\(\mu_4-47\mu_2+663\mu_0/4\), and
\(\mu_6-275\mu_4/2+13801\mu_2/4-69615\mu_0/8\).
These maps retain cancellation between distinct original moments; a certified evaluator must enclose the whole signed combination with exact rational coefficients. Neither moment equality nor coefficient sign follows from dropping any of these terms.

## 5. Audit determination and execution boundary

The proposed derivative recurrence, moment integral, tail coefficient, tail exponent, gamma recurrence, and signed coefficient numerators are correct under their explicitly stated original conventions. No flaw was found in the delivered finite numerical driver's theta factor, symmetric summation multiplicities, integral recurrence, or coefficient denominators. The driver's numerical output remains a floating-point calculation. It supplies no bound on its rounding error or shared truncation error by itself.

The mathematical mechanism for an interval certificate is now exact: enclose the finite sums (IR.10) with directed ball operations; enlarge each ball by an upper enclosure of the positive bound (IR.17); enclose the strictly positive constant (IR.18); and apply the signed rational maps (IR.24). This review does not claim those interval operations were executed. That execution and its independently recorded endpoints belong to the parent's certificate. The analytic seed has finite arithmetic quotient zero, as the source states; all moments and gamma coefficients here belong to its original nonzero analytic source.

## 6. Final implementation review of GS.1–GS.40 and its certificate

This additional review reads the complete new proof `work/gamma_seed_intervals_20260913.tex`, complete checker `work/gamma_seed_intervals_20260913_check.py`, complete normal JSON, and the final ten-job replay ledger. It also verifies all ten output receipts and the thirty receipt/stdout/stderr file hashes referenced by that ledger. The final files reviewed are pinned as follows:

| File in `work` | Bytes | SHA-256 |
|:--|--:|:--|
| `gamma_seed_intervals_20260913.tex` | 27629 | `579c934bc3e6abba27008de20385bc276e10c824a9f7944156a7781eeb7768e7` |
| `gamma_seed_intervals_20260913_check.py` | 11588 | `a67942a8a4d89ba5fbee1f5d8797793209cba26eadc6d450dd2efaac13c02e4c` |
| `gamma_seed_intervals_20260913_normal.json` | 11821 | `8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1` |
| `gamma_seed_intervals_20260913_replay.json` | 11226 | `958492ae4e7b45a9df615ab7854d55cf2548a3b6aef69a2451a275f11d37700d` |

The first reading identified an execution-description mismatch: some finite comparisons described as exact verifications were ball-overlap checks. The parent corrected the text to say which comparisons test overlap and added literal Fraction checks for all seven gamma polynomial lists and the four denominator factors. The final checker above was read completely after those edits. The final replay now binds its checker hash to every job's observed `script_sha256`, and binds its proof hash to the final TeX above. An intermediate read during the parent's sequential edit/replay window saw unmatched old/new hashes; the final ten-job hash audit passed, so that transitional state is not the delivered certificate.

### 6.1 Analytic formulas checked beyond the initial polynomial audit

GS.1–GS.20 retain the exact definitions and signs proved in Sections 1–3 of this review. In particular `moment_tail` uses `degree=max(P)=r+2`, hence its integral argument `I(4*degree,...)` is exactly \(I_{4r+8}\). The finite sum uses every ordered pair \(1\le m,n\le8\), with the original full coefficients \(p_{r,a}\); no triangular multiplicity or extra endpoint factor is missing. The function `integral_twice[power]` represents

\[
2I_{2\,\mathrm{power}}(C)
=\frac{\Gamma(\mathrm{power}+1/2,C)}{C^{\mathrm{power}+1/2}}.
\]

Every required exponent \(a+b\) is between two and ten. The recurrence comparison uses powers two through nine at each of the sixty-four ordered pairs, hence exactly \(64\cdot8=512\) overlap comparisons, agreeing with each JSON record.

GS.21–GS.28 also preserve the original gamma scale. The beta integral in GS.22 has variables \(v\) and \(x\); Fourier inversion followed by \(t=2v\) contributes the factor two in
\(c_\lambda=2^{1-2\lambda}\Gamma(2\lambda)\). The shift of the beta-integral contour within \(|\Im x|<\pi\) gives the exponential moment domain required in GS.24 and GS.27. The coefficient comparison in GS.27 is dominated by a smaller admissible exponential weight near the origin, so it proves the actual norm \(c_\lambda n!(2\lambda)_n\), with no mass replacement. The recurrence and all the polynomials in GS.33 agree with (IR.19)–(IR.23).

The final TeX additionally proves gamma nonvanishing on the entire required half-plane. This paragraph was independently read after its addition. Repeated integration by parts gives \(B(z,n+1)=n!/[z(z+1)\cdots(z+n)]\) for \(\Re z>0\). After \(u=v/n\), its scaled integral is
\(n^z B(z,n+1)=\int_0^n v^{z-1}(1-v/n)^n\,dv\). Its absolute integrand is at most \(v^{\Re z-1}e^{-v}\), so dominated convergence gives \(\Gamma(z)\). The reciprocal of each finite expression is

\[
z\exp\left(z\left(\sum_{j=1}^n\frac1j-\log n\right)\right)
\prod_{j=1}^n(1+z/j)e^{-z/j}.
\]

The parenthetical real sequence has its finite limit by integral comparison; the logarithm of the tail product converges absolutely by \(\log(1+z/j)-z/j=O(j^{-2})\). All its factors are nonzero for \(\Re z>0\). Its limit is therefore finite and nonzero. Taking limits in the exact product of each expression and its reciprocal, which equals one, proves that this nonzero limit times \(\Gamma(z)\) is one. This argument does not assume gamma nonvanishing before proving it. The gamma integral is holomorphic on the half-plane by compact-subset domination, excluding poles there as well. The final source also explicitly gives \(g(2)>0\) from GS.5, which proves that its entire function is nonzero and its line zeros form a discrete set. These additions justify both inverse maps used in the amplitude argument without changing the checker or any numerical endpoint. The reobserved replay binds the final proof hash above, and all thirty job-file hashes were checked again.

The Hilbert-space amplitude map in GS.29 has the stated direction:

\[
M_A:L^2(\mathbb R,w(t)dt)\longrightarrow
L^2(\mathbb R,r_\lambda(t)dt),\qquad f\longmapsto A_{1,\lambda}f.
\]

Indeed \(\int|Af|^2r_\lambda=\int|f|^2w\). Away from the discrete zero set of the nonzero entire function \(g\) on the line, its inverse is \(h\mapsto h/A_{1,\lambda}\). The exceptional set has both measures zero. The inverse norm is \(\int|h/A|^2w=\int|h|^2r_\lambda\). Thus this is an actual surjective isometry between the stated equivalence classes, including the complex phase of \(A\).

Here is an independent full check of the constant and rational expression in GS.31. The continuation identity used in the proof gives, for \(s=1/2+it\),

\[
|\zeta(s)|\le \left|\frac{s}{s-1}\right|
+|s|\int_1^\infty x^{-3/2}dx
=1+2\sqrt{t^2+1/4}
\le4\sqrt{t^2+1/4}.
\]

The first quotient has modulus one; the last inequality holds because \(\sqrt{t^2+1/4}\ge1/2\). Squaring the complete numerator in GS.30 gives
\(\pi^{-1/2}(t^2+1/4)^2|\zeta(1/2+it)|^2\). The three squared gamma-shift factors give exactly

\[
\left|\prod_{j=0}^2(j+1/4+it/2)\right|^2
=4^{-3}(t^2+1/4)(t^2+25/4)(t^2+81/4).
\]

The constant is therefore \(16\cdot4^3/\sqrt\pi=1024/\sqrt\pi\), and the remaining quotient is precisely
\((t^2+1/4)^2/((t^2+25/4)(t^2+81/4))\). With \(x=t^2\), its denominator minus numerator is

\[
(x+25/4)(x+81/4)-(x+1/4)^2
=26x+\frac{253}{2}>0.
\]

This verifies GS.31, including the full sign and phase retained in GS.30 before taking the squared modulus. Since the gamma measure has finite mass, the displayed boundedness proves \(B_{1,13/4}\in L^2(r_{13/4}dt)\).

GS.34 has the degree-six denominator \(2737957950\), exactly as (IR.24). Its inverse GS.35 is correct: the moment map is triangular with respective nonzero coefficients \(1/c\), \(2/(195c)\), \(4/(377910c)\), and \(8/(2737957950c)\). Solving the four equations in that order gives exactly the four stated inverse expressions. Substitution reconstructs each original moment, with both masses retained.

GS.38 follows by multiplying the original generating functions with equal formal variable \(z\): their exponents add to \(-k\lambda\pm iu/2\), where \(u=t_1+\cdots+t_k\). In GS.39 the coefficient \(n!/(n_1!\cdots n_k!)\) is multiplied by the actual one-factor integrals \(c\,n_j!(\alpha)_{n_j}c_{n_j}\). The factorials cancel to give exactly \(c^k n!\prod_j a_{n_j}\); summing the finitely many compositions gives its claimed formula.

The mixed term in GS.40 has coefficient \(k(k-1)\). There are \(k\) choices of the factor contributing degree four and independently \(k-1\) choices of the different factor contributing degree two. The remaining \(k-2\) factors contribute \(c_0\). The degree-six term is therefore

\[
k c_0^{k-1}a_6
+k(k-1)c_0^{k-2}a_2a_4
+\binom{k}{3}c_0^{k-3}a_2^3.
\]

For the final term, an unordered set of three factors each contributes degree two, giving \(\binom{k}{3}\), with no additional factorial. For \(k=1\) and \(k=2\), the terms with insufficient factors have zero combinatorial coefficient. Their displayed negative powers of \(c_0\) are well-defined because the certified lower endpoint of \(c_0\) is positive. This proves the formula at every stated positive integer \(k\), including both small cases. The negative sign of \(a_2a_4\) is preserved because \(a_2>0\) and \(a_4<0\). The formula does not claim an asymptotic bound.

### 6.2 Certificate semantics and independent rational audit

The final code sets 256-bit precision and one arithmetic thread, and the observed JSON fields record exactly those values with python-flint 0.9.0. All derivative and gamma coefficients are Fractions. They enter Arb through `fmpq`; all powers and gamma arguments in the finite integral and tail use positive real balls representing the specified exact inputs. The `gamma_upper` call has the argument/order arrangement written in GS.13. This review checks that arrangement against the displayed formula, independently of the code's recurrence-overlap checks.

The code obtains each infinite-moment enclosure by adding `arb(0, tail.upper())` to the finite ball. The argument supplies a symmetric error ball with an outward radius at least as large as the upper endpoint of the positive tail bound. Thus the enclosure includes the omitted integer square proved in GS.18. The coefficient arithmetic uses these enlarged balls before any decimal display conversion. Positive mass comparisons make every coefficient division valid. The returned `ball` strings are human-readable approximations; the recorded dyadic endpoints and exact rational decimal endpoints are the precise stored interval data.

The final checker now compares the complete rational lists for \(P_0,\ldots,P_3\) and \(b_0,\ldots,b_6\), and the four rising-factorial denominator factors by exact equality. The recurrence and alternate integer coefficient forms remain ball-overlap regression comparisons, exactly as the final TeX states. Agreement of those ball evaluations is not used in place of the analytic proof or infinite-tail enlargement.

For the pinned final normal JSON, this reviewer independently executed a read-only Fraction audit, without importing or running the certificate checker. The audit checked all of the following with integer/rational arithmetic:

1. For each of the nine quantities, its decimal lower and upper strings equal the stored rational lower and upper strings exactly.
2. Each lower decimal endpoint is strictly below the stored lower dyadic endpoint; the dyadic interval is ordered; and the upper dyadic endpoint is strictly below the upper decimal endpoint.
3. Each of the nine displayed widths is exactly \(3/10^{40}\).
4. All eighteen decimal strings occur literally in the pinned TeX, so the printed endpoints match the certified receipt.
5. Each stored positive rational tail upper endpoint is strictly less than its corresponding rational cap in GS.36: \(7/10^{107}\), \(4/10^{103}\), \(2/10^{99}\), and \(14/10^{96}\).
6. Exact signed interval arithmetic applied to the stored dyadic moment intervals and the dyadic reference-mass interval in each of the four rational maps (IR.24) produces an interval strictly inside the corresponding printed coefficient interval.

For precision about the last operation, if a numerator has coefficients \(q_j\) and the dyadic interval for \(\mu_j\) is \([l_j,u_j]\), the independent lower numerator bound is
\(\sum_{q_j\ge0}q_jl_j+\sum_{q_j<0}q_ju_j\), and the upper bound interchanges \(l_j,u_j\). For positive denominator interval \(D[l_c,u_c]\), the lower and upper quotient bounds are the minimum and maximum of the four exact rational endpoint quotients. This verifies the inclusion with all cancellations, signs, and the original mass retained. It applies to \(c_0,c_2,c_4,c_6\) and makes no assumption of independence between the underlying moments.

All six sets of checks passed. In particular the negative upper endpoints prove the two actual coefficient signs \(c_4<0\), \(c_6<0\); this conclusion is based on enclosures of the infinite quantities.

### 6.3 Final execution receipts and scope

The final replay ledger records two successful ordinary runs and eight rejected fault runs: one ordinary and four faults in normal Python, and the same five cases with `-O`. This reviewer verified every referenced file hash, every job's embedded script hash against the final checker, each observed optimization flag, and equality of the full `results` object across all ten JSON receipts. For the ordinary runs the recorded exit code is zero, status is `passed`, and failed-fault count is zero. For every fault run the recorded exit code is one, status is `rejected`, and failed-fault count is exactly one. All thirty referenced receipt/stdout/stderr hashes agree with their files.

The four faults assert respectively that halving the fourth moment preserves it, that assigning reference mass one preserves \(c_0\), that \(c_4\ge0\), and that the zero-cutoff square with zero error contains the full positive mass. Each is false for the already enclosed quantities, and the code explicitly rejects it. The tail fault concerns the stated cutoff-zero error omission; it does not claim detection of every possible incorrect tail implementation at cutoff eight. The direct conditionals survive Python optimization.

The normal JSON certifies nine distinct scalar quantities: four original infinite seed moments, the gamma reference mass, and four arithmetic gamma coefficients. The repeated mode records do not create additional distinct mathematical quantities. The tensor formulas are exact symbolic transport identities and permit evaluation at a specified finite \(k\); the ten recorded jobs do not themselves claim evaluation of every tensor degree. Neither these jobs nor this review executes Lean, selects a nonempty zero packet, proves a growing-degree estimate, or independently certifies the implementation of the arithmetic library. The mathematical content of GS.1–GS.40 and the described finite certificate scope agree at the final pins above. PDF compilation and visual review belong to the parent's artifact workflow and are not claimed by this implementation audit.

## 7. Complete review of the separate source-cost continuation GS.41–GS.50

The source-cost continuation was supplied as a separate full fragment, preserving the GS.1–GS.40 TeX and its completed original arithmetic replay. This reviewer read the full fragment, its standalone wrapper, complete Fraction checker, complete normal receipt, and complete eight-job replay ledger. After the local macro scope was added, the complete final fragment was read again. Its `begingroup`, local definitions of `ii` and `dd`, and final `endgroup` preserve the complete mathematical body while preventing macro leakage into the cumulative TeX. Final files are pinned below.

| File in `work` | Bytes | SHA-256 |
|:--|--:|:--|
| `gamma_seed_intervals_20260913_source_costs.tex` | 9616 | `ca1e162b24842e939dbece5bf12f02e76001baed8bf2bd61a0e02b490a1e7331` |
| `gamma_seed_intervals_20260913_source_costs_check.py` | 5183 | `cd8a83921958727f85f36896c5794d8292358cdc56b3f017302324724b6fa63b` |
| `gamma_seed_intervals_20260913_source_costs_normal.json` | 9553 | `c23d09a0762d912530b34dc89a7ebab72200af403f7ce643b3cc997a614c3aff` |
| `gamma_seed_intervals_20260913_source_costs_replay.json` | 8247 | `24cfa2f1237d4730d40667e79358fbb8dc6005e66579f4b3d5e47a45673d34dc` |

The input certificate remains the actual infinite-moment normal JSON pinned in Section 6, SHA `8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1`. The cost checker rejects any different input bytes. The original analytic replay continues to bind its original GS.1–GS.40 proof, and the new replay binds GS.41–GS.50 separately; no later proof is represented as the earlier execution's input.

### 7.1 Original sum moments, positive polynomial norms, and all three costs

Let \(m_k=w^{*k}\) in the literal variable \(u=\sum_{j=1}^k t_j\). In the expansion of \(u^{2r}\), every term with an odd exponent in one factor integrates to zero. Keeping the mass of every unused factor therefore gives

\[
\begin{aligned}
M_0(k)&=\mu_0^k,\\
M_2(k)&=k\mu_2\mu_0^{k-1},\\
M_4(k)&=k\mu_4\mu_0^{k-1}+3k(k-1)\mu_2^2\mu_0^{k-2},\\
M_6(k)&=k\mu_6\mu_0^{k-1}
+15k(k-1)\mu_4\mu_2\mu_0^{k-2}
+15k(k-1)(k-2)\mu_2^3\mu_0^{k-3}.
\end{aligned}
\tag{IR.25}
\]

These are exactly GS.41. For degree six, the multinomial counts are \(k\) for one exponent six, \(k(k-1)6!/(4!2!)=15k(k-1)\) for exponents four and two, and \(\binom{k}{3}6!/(2!2!2!)=15k(k-1)(k-2)\) for three exponents two. The degree-four cross term has \(\binom{k}{2}4!/(2!2!)=3k(k-1)\) possibilities. Every displayed inverse power of \(\mu_0\) at small \(k\) is defined because its positive mass was proved; the accompanying zero coefficient gives the absent term.

The fragment proves all polynomial norms positive for this actual measure. A nonnegative integrable density of positive mass is positive on a set of positive Lebesgue measure. The real zero set of a nonzero polynomial is finite and therefore has measure zero. Removing that zero set leaves a set of positive measure on which the squared norm integrand is positive. Its integral is positive. This establishes positive definiteness of each finite polynomial Gram, including every denominator used below, without an additional positivity hypothesis.

Put \(\nu=\mu_2/\mu_0\). Orthogonality of \(1,u,u^2-k\nu,u^3-(M_4/M_2)u\) follows by parity and the two identities
\(M_2-k\nu M_0=0\) and \(M_4-(M_4/M_2)M_2=0\). Expanding their actual squared norms gives

\[
h_0=M_0,\quad h_1=M_2,\quad
h_2=M_4-\frac{M_2^2}{M_0},\quad
h_3=M_6-\frac{M_4^2}{M_2}.
\tag{IR.26}
\]

Multiplication by the real variable \(u\) is symmetric on this polynomial inner-product domain. The coefficient of \(p_{j-1}\) in \(up_j\) is consequently
\(\langle up_j,p_{j-1}\rangle/h_{j-1}=h_j/h_{j-1}\); coefficients of still lower degree vanish, while the coefficient of degree \(j\) vanishes by parity. This proves the norm-ratio recurrence interpretation for \(a_j^{(k)}\), including \(j=3\). Existence of the required monic \(p_4\) follows from the already proved positive finite Gram. Substituting (IR.25) into (IR.26) proves

\[
a_1^{(k)}=k\nu,\qquad
a_2^{(k)}=\frac{\mu_4}{\mu_2}+(2k-3)\nu,
\qquad
a_3^{(k)}=\frac{M_6-M_4^2/M_2}{M_4-M_2^2/M_0}.
\tag{IR.27}
\]

For a separate check of the expanded third cost, retain the scalar abbreviations \(r_4=\mu_4/\mu_0\) and \(r_6=\mu_6/\mu_0\), with the measure unchanged. The exact positive norms are

\[
\begin{aligned}
h_2&=k\mu_0^k\{r_4+(2k-3)\nu^2\},\\
h_3&=k\mu_0^k\{r_6-r_4^2/\nu
+9(k-1)r_4\nu+3(k-1)(2k-7)\nu^3\}.
\end{aligned}
\tag{IR.28}
\]

Indeed \(M_4^2/M_2\), divided by \(k\mu_0^k\), is
\(r_4^2/\nu+6(k-1)r_4\nu+9(k-1)^2\nu^3\). Its difference from the corresponding \(M_6\) expression gives the coefficient nine and the exact cubic term
\(15(k-1)(k-2)-9(k-1)^2=3(k-1)(2k-7)\). Dividing the two retained norms gives GS.44. This checks all cross terms, including those which are negative at small \(k\).

### 7.2 The precise original spectral coordinate and lower sign

GS.45 defines the algebra isomorphism
\(\Psi_kP(u)=P(c_k+iu)\), \(c_k=k/2\), with inverse
\(p\mapsto [S\mapsto p((S-c_k)/i)]\). Substitution in both directions gives the identity. The source norm in the \(S\) presentation is defined by that same substitution into the unchanged sum measure, so \(\Psi_k\) is a linear isometry onto the polynomial source in \(u\).

On monic polynomials of fixed degree \(j\), the exact monic correspondence is

\[
P_j(S)=i^j p_j((S-c_k)/i),\qquad
p_j(u)=i^{-j}P_j(c_k+iu).
\tag{IR.29}
\]

The two maps are inverse and each scalar phase has modulus one. They preserve the full norms \(h_j\). Applying (IR.29) to the first four real polynomials gives exactly GS.46, including the positive \(k\nu\) in \(P_2=(S-c_k)^2+k\nu\) and positive coefficient \(\mu_4/\mu_2+3(k-1)\nu\) in the cubic polynomial. Finally, multiplying \(up_j=p_{j+1}+a_jp_{j-1}\) by \(i^{j+1}\) gives

\[
(S-c_k)P_j=P_{j+1}-a_jP_{j-1},
\qquad
SP_j=P_{j+1}+c_kP_j-a_jP_{j-1}.
\tag{IR.30}
\]

The negative lower coefficient follows from \(i^{j+1}/i^{j-1}=i^2=-1\). Thus it is exactly related to the positive norm ratio, and no sign or original affine coordinate has been discarded.

### 7.3 Determinant correction and the all-tensor comparison

For a monic orthogonal basis, the matrix from the original monomial basis is triangular with diagonal one. It preserves the Gram determinant, so \(D_n=\prod_{j<n}h_j\). The gamma convolution has the original mass \(c_{13/4}^k\) and parameter \(13k/4\), as follows by multiplying GS.23's Fourier transforms and retaining the scalar convolution factor. Its monic norms are exactly
\(c_{13/4}^k j!(13k/2)_j\). The ratio of consecutive norms is
\((N+1)(N+13k/2)\). Taking consecutive ratios of \(X_n=D_n/D_n^\Gamma\) gives GS.48 directly.

Writing \(\eta=\mu_4/\mu_2\), the first two exact correction formulas are

\[
Q_0=\frac{2\nu}{13},\qquad
Q_1(k)=\frac{\eta+(2k-3)\nu}{13k+2}.
\]

Subtracting \(Q_0\) with the common denominator gives the retained difference numerator

\[
\eta+(2k-3)\nu-\frac{2\nu}{13}(13k+2)
=\eta-\frac{43}{13}\nu=\rho.
\tag{IR.31}
\]

The third cost gives \(Q_2(k)=2a_3^{(k)}/(39k+12)\), because the degree-three gamma cost is \(3(2+13k/2)\). These computations verify every denominator in GS.49.

The rational certificate encloses \(\rho\) with a strictly negative upper endpoint. Therefore for every integer \(k\ge1\),

\[
Q_1(k)=Q_0+\frac{\rho}{13k+2}<Q_0,
\qquad
Q_1(k+1)-Q_1(k)=\frac{-13\rho}{(13k+2)(13k+15)}>0.
\tag{IR.32}
\]

Moreover \(Q_1(1)=a_2^{(1)}/15>0\) by (IR.26), and the positive certified interval supplies the same strict inequality. This proves the full GS.50 statement, including equality of its first two terms when \(k=1\), and all its domains. It is a proved comparison at fixed original polynomial degree as tensor degree varies. It supplies no estimate for polynomial degree tending to infinity.

### 7.4 Independent verification of the saved-moment transport

The Fraction checker imports no special-function library and performs no floating-point arithmetic. The literal input pin is checked before reading any moments. All interval endpoints are constructed from the input's exact dyadic rational strings. Addition, subtraction, multiplication by all four endpoint products, and inversion after a positive-lower-endpoint check are the standard rational inclusion operations proved in the fragment. In particular Python expressions `1/b[1]` and `1/b[0]` have Fraction operands and retain exact rational values. The outward conversion uses integer floor and ceiling with exact rational arguments and explicitly checks both strict inclusion and width \(3/10^{40}\).

This reviewer independently reconstructed all ten output quantities from the pinned dyadic input using separate read-only Fraction arithmetic, without importing the cost checker. To check the nonlinear terms by a different algebraic presentation, the reconstruction first formed the full unscaled sum moments in (IR.25) for \(k=1\) and \(k=2\), then formed the norms (IR.26), and divided those norms to obtain \(a_2^{(1)},a_2^{(2)},a_3^{(1)}\). Thus the two second costs were independently evaluated from the full source-norm formulas, while the checker itself uses \(\eta-\nu\) and \(\eta+\nu\). The independent intervals obtained this way lie strictly inside the recorded decimal intervals.

For each of the ten named output quantities, both its recorded transport-rational interval and the separately reconstructed source-formula interval lie strictly inside its displayed decimal interval. Every decimal width equals its recorded rational width and equals \(3/10^{40}\). All four printed interval pairs in the proof occur literally in the normal receipt. The ten audited quantities are \(\nu\), \(\eta\), \(\mu_4\mu_0-\mu_2^2\), \(a_2^{(1)}\), \(a_2^{(2)}\), \(Q_0\), \(Q_1(1)\), \(\rho\), \(a_3^{(1)}\), and \(Q_2(1)\). Their positivity or negativity checks agree with the proof. In particular the independently reconstructed intervals include

\[
\begin{aligned}
a_3^{(1)}\in[&26.7777052276449079536144576882338057998976,\\
&26.7777052276449079536144576882338057998979],\\
Q_2(1)\in[&1.0501060873586238413182140269895610117605,\\
&1.0501060873586238413182140269895610117608].
\end{aligned}
\]

The eight final job receipts have the expected input hash and the final checker hash. This reviewer verified those eight observed script/input pairs, the observed optimization flags, equality of every complete mathematical `results` object to the normal result, and all twenty-four referenced receipt/stdout/stderr hashes. Both positive jobs record exit zero and status `passed`. All six fault jobs record exit one, status `rejected`, and exactly one failed-fault check. The final replay's proof-fragment hash matches the scoped fragment above.

The first fault has an exact source interpretation: at \(k=2\), deleting the original \(6\mu_2^2\) term in \(M_4\) while retaining \(M_2\) and \(M_0\) would give the false second cost \(\eta-2\nu\); its interval is disjoint from the true \(\eta+\nu\). The mass fault replaces \(\mu_0\) by one in \(\nu\), yielding the false value \(\mu_2\), whose interval is disjoint from that of \(\nu\). The final fault asserts \(Q_0<1\), rejected by the certified lower endpoint greater than one. These are explicit false-claim controls, preserved under optimization, and not claims of exhaustive fault coverage.

No additional quadrature was performed by the cost calculation or this audit. Its ten derived scalar enclosures and all-tensor formulas concern the original analytic source with polynomial degrees one through three. The same source's finite arithmetic quotient is still \(\mathbb C[S]/(1)=0\), whose quotient determinant is the empty determinant one. The positive norms above remain the actual source norms. The entire GS.41–GS.50 fragment, its fixed-source scalar certificates, typed coordinate maps, and stated execution scope are correct at the final pins above.
