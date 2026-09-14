# Independent theta derivative and omitted-integer-tail audit

Prepared 13 September 2026 for the 12 September Toda source delivery. This audit reads the complete supplied `Tau_Toda_Volume_Control/NOTE.tex`, with the calculation below addressing its Section 9. It changes no parent proof, checker, or cumulative output.

The original source is

\[
 f_0(x)=2\sum_{n\geq1}(4\pi^2n^4x^4-6\pi n^2x^2)e^{-\pi n^2x^2},
 \qquad D=-x\frac{d}{dx}.
\]

The exact conclusions of this audit are: the derivative polynomial stated below includes the original factor two; the Mellin–Plancherel expression for the second Laplace derivative has no additional factor of two; converting its full positive-axis integral to the interval \([1,\infty)\) introduces exactly one factor two; and the omitted integer tail can be bounded explicitly, including every cross term in the square. The finite integral still requires directed-rounding evaluation to turn an approximate printed decimal into a certified enclosure.

## 1. Derivative with the original coefficients

For a fixed integer \(n\geq1\), put \(a=\pi n^2\) and, solely as a displayed coordinate map, \(z=ax^2\). On functions of this coordinate the operator is

\[
 -x\partial_x=-2z\partial_z.
\]

The original summand is \((8z^2-12z)e^{-z}\). Applying the displayed operator gives

\[
 \begin{aligned}
 D[(8z^2-12z)e^{-z}]
 &=-2z[(16z-12)-(8z^2-12z)]e^{-z}\\
 &=(16z^3-56z^2+24z)e^{-z},\\
 (D-\tfrac12)[(8z^2-12z)e^{-z}]
 &=(16z^3-60z^2+30z)e^{-z}.
 \end{aligned}
\]

Consequently, with \(H=(D-\tfrac12)f_0\),

\[
 \boxed{H(x)=\sum_{n\geq1}
 (16\pi^3n^6x^6-60\pi^2n^4x^4+30\pi n^2x^2)
 e^{-\pi n^2x^2}.}
 \tag{A1}
\]

Uniform convergence of the polynomial-Gaussian series and all its derivatives on every compact subset of \(x>0\) permits this termwise calculation. On \(x\geq1\), the explicit bounds in Section 4 below also supply summable dominating series and square-integrable dominating functions.

## 2. Exact Mellin and Fourier maps

Use the Mellin transform

\[
 (\mathcal M f)(s)=\int_0^\infty f(x)x^{s-1}\,dx
\]

and the unscaled Fourier transform with the **positive** kernel

\[
 (\mathcal F_+u)(t)=\int_{\mathbb R}u(y)e^{ity}\,dy.
\]

The unitary logarithmic-coordinate map and its inverse are

\[
 U:L^2((0,\infty),dx)\longrightarrow L^2(\mathbb R,dy),\qquad
 (Uf)(y)=e^{y/2}f(e^y),\qquad
 (U^{-1}u)(x)=x^{-1/2}u(\log x).
\]

Indeed the substitution \(x=e^y\) proves \(\int|Uf|^2dy=\int|f|^2dx\). On the smooth, rapidly decreasing endpoint functions used here,

\[
 \mathcal F_+Uf(t)=\mathcal M f(\tfrac12+it),\qquad
 U(D-\tfrac12)f=-\frac{d}{dy}(Uf),\qquad
 \mathcal F_+(-u')(t)=it\,\mathcal F_+u(t).
 \tag{A2}
\]

The last equality follows by integration by parts; the boundary term is zero. Thus the exact transformed multiplier is \(+it\), in the specified Fourier convention.

For completeness the original summand has, initially at \(\Re s>1\), Mellin transform

\[
 \begin{aligned}
 &2\int_0^\infty(4a^2x^4-6ax^2)e^{-ax^2}x^{s-1}dx\\
 &\quad=a^{-s/2}\{4\Gamma(s/2+2)-6\Gamma(s/2+1)\}\\
 &\quad=a^{-s/2}\Gamma(s/2)
       \{4(s/2)(s/2+1)-6(s/2)\}\\
 &\quad=s(s-1)a^{-s/2}\Gamma(s/2).
 \end{aligned}
\]

The sum is absolutely integrable there: both separated polynomial-Gaussian terms sum to a finite constant times \(\sum n^{-\Re s}\). Summing gives precisely

\[
 \mathcal M f_0(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=g(s).
\]

The endpoint identity proved in Section 3 makes the Mellin integral entire; hence the equality continues to the critical line. Fourier Plancherel in the above convention now proves

\[
 \begin{aligned}
 M_1''(0)
 &=\frac1{2\pi}\int_{\mathbb R}t^2|g(\tfrac12+it)|^2dt\\
 &=\int_{\mathbb R}|(Uf_0)'(y)|^2dy
 =\int_0^\infty |H(x)|^2dx.
 \end{aligned}
 \tag{A3}
\]

Here \(M_1(\theta)=(2\pi)^{-1}\int e^{\theta t}|g(1/2+it)|^2dt\) retains the unscaled mass. Differentiation twice at zero is permitted by the exponential domination on the strip \(|\Re\theta|<\pi/2\) proved in Section 3.1 of the supplied note: on each smaller real interval, multiplication by \(t^2\) is absorbed by an exponential from a slightly larger interval. No division by \(M_1(0)\) occurs in (A3).

## 3. Inversion and the factor two

Let

\[
 \vartheta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x^2}.
\]

Poisson summation for the Gaussian gives \(\vartheta(1/x)=x\vartheta(x)\) for \(x>0\). The constant term is killed by \(D(D-1)\), and direct differentiation of the nonconstant terms yields

\[
 f_0=D(D-1)\vartheta.
\]

The precise inversion operator is the complex-linear map

\[
 I:C^\infty((0,\infty))\longrightarrow C^\infty((0,\infty)),
 \qquad (If)(x)=x^{-1}f(1/x).
\]

It satisfies \(I^2=1\) and \(ID=(1-D)I\), by differentiation. On \(L^2(dx)\) it is unitary, by the substitution \(x\mapsto1/x\). Also \(UIU^{-1}u(y)=u(-y)\), so the inversion transports to the literal reflection of the logarithmic coordinate. The theta identity is \(I\vartheta=\vartheta\). Therefore

\[
 If_0=(1-D)(-D)\vartheta=D(D-1)\vartheta=f_0,
\]

and

\[
 IH=I(D-\tfrac12)f_0=-(D-\tfrac12)If_0=-H.
\]

Equivalently,

\[
 f_0(1/x)=x f_0(x),\qquad H(1/x)=-xH(x).
 \tag{A4}
\]

The rapid Gaussian decay at infinity of \(f_0\) and its Euler derivatives, followed by (A4) and its differentiated identities, gives the needed rapid endpoint decay at zero. The same identities imply that \(Uf_0\) is even and \(UH\) is odd. In particular \(H(1)=0\), although this zero is not needed for the integral substitution. Keeping the Jacobian,

\[
 \int_0^1|H(x)|^2dx
 =\int_1^\infty |H(1/u)|^2u^{-2}du
 =\int_1^\infty |H(u)|^2du.
\]

Combining this equality with (A3) proves

\[
 \boxed{M_1''(0)=2\int_1^\infty
 \left[\sum_{n\geq1}
 (16\pi^3n^6x^6-60\pi^2n^4x^4+30\pi n^2x^2)
 e^{-\pi n^2x^2}\right]^2dx.}
 \tag{A5}
\]

All summands are real at these arguments, so the displayed square equals the absolute square. For a finite integer truncation, the identities (A4) need not hold for the truncated function on the whole positive axis. The finite approximation below is defined directly by the exterior integral in (A5); it does not apply inversion to a truncated theta series.

## 4. A positive explicit omitted-integer-tail bound

Fix an integer \(J\geq1\), set \(L=J+1\), and define

\[
 Q(z)=16z^3-60z^2+30z,\quad
 H_J(x)=\sum_{n=1}^{J}Q(\pi n^2x^2)e^{-\pi n^2x^2},\quad
 R_J(x)=H(x)-H_J(x).
\]

No polynomial coefficient of \(H_J\) or \(R_J\) is changed in these definitions. For the omitted indices \(n\geq L\geq2\) and \(x\geq1\), one has \(z=\pi n^2x^2>12\). The identity

\[
 16z^2-60z+30=16z(z-12)+132z+30
\]

shows \(Q(z)>0\) there; and \(-60z^2+30z\leq0\) gives \(Q(z)\leq16z^3\). Define the original-parameter constants

\[
 r_L=\left(1+\frac1L\right)^6e^{-\pi(2L+1)},\qquad
 C_L=\frac{16\pi^3L^6}{1-r_L},\qquad b_L=2\pi L^2.
 \tag{A6}
\]

The ratio of successive positive majorant summands satisfies

\[
 \frac{(n+1)^6e^{-\pi(n+1)^2x^2}}
      {n^6e^{-\pi n^2x^2}}
 =\left(1+\frac1n\right)^6e^{-\pi(2n+1)x^2}
 \leq r_L<1.
\]

For example \(r_L\leq64e^{-15}<1/2\), using \(\pi>3\), \(L\geq2\), and \(e>8/3\); the last rational comparison is checked exactly in the companion script. Summing the geometric majorant proves the pointwise estimate

\[
 \boxed{0\leq R_J(x)\leq C_Lx^6e^{-\pi L^2x^2}\quad(x\geq1).}
 \tag{A7}
\]

Define the squared exterior norm \(\|f\|_+^2=2\int_1^\infty|f(x)|^2dx\). Substitution \(t=x^2-1\) gives

\[
 \begin{aligned}
 \|R_J\|_+^2
 &\leq2C_L^2\int_1^\infty x^{12}e^{-b_Lx^2}dx\\
 &=C_L^2e^{-b_L}\int_0^\infty(1+t)^{11/2}e^{-b_Lt}dt\\
 &\leq C_L^2e^{-b_L}\int_0^\infty(1+t)^6e^{-b_Lt}dt\\
 &= C_L^2e^{-b_L}\sum_{j=0}^6\binom6j\frac{j!}{b_L^{j+1}}
 =:\mathcal E_L.
 \end{aligned}
 \tag{A8}
\]

Every term in this last bound is positive. An exact special-function expression before its polynomial upper estimate is

\[
 2C_L^2\int_1^\infty x^{12}e^{-b_Lx^2}dx
 =C_L^2b_L^{-13/2}\Gamma(13/2,b_L).
\]

The elementary version (A8) avoids incomplete-gamma evaluation for the omitted tail.

## 5. Every square-integral cross term and a rational fallback

Put \(\mathcal M_J=\|H_J\|_+^2\). Expansion of the original square and Cauchy–Schwarz, on the same exterior measure \(2dx\), yield

\[
 \boxed{|M_1''(0)-\mathcal M_J|
 \leq2\sqrt{\mathcal M_J\mathcal E_L}+\mathcal E_L.}
 \tag{A9}
\]

In particular an enclosure \(\mathcal M_J\in[A,B]\) with \(0\leq A\leq B\) and \(\mathcal E_L\leq E\) produces the exact enclosure

\[
 M_1''(0)\in
 [\max\{0,\sqrt A-\sqrt E\}^{2},\; (\sqrt B+\sqrt E)^2].
 \tag{A10}
\]

This includes interactions between the retained integers and omitted integers, and interactions between different omitted integers.

There is also a completely rational upper bound. The inequalities \(\pi<22/7\), \((22/7)^3<32\), and \(r_L<1/2\) imply \(C_L<1024L^6\). Since \(b_L>6L^2\geq24\),

\[
 \sum_{j=0}^6\binom6j\frac{j!}{b_L^{j+1}}
 \leq\frac1{b_L}\sum_{j=0}^\infty\left(\frac6{b_L}\right)^j
 =\frac1{b_L-6}.
\]

Finally \(e>8/3\), as follows already from the sum of its first five Taylor terms. Thus

\[
 \boxed{\mathcal E_L<
 \frac{2^{20}L^{12}}{6L^2-6}\left(\frac38\right)^{6L^2}
 =:\widehat{\mathcal E}_L.}
 \tag{A11}
\]

For an independent bound on \(\mathcal M_J\), observe for every \(z\geq1/2\) that \(Q(z)\leq16z^3\) and

\[
 Q(z)+16z^3
 =z\{32(z-15/16)^2+15/8\}>0.
\]

Hence \(|Q(z)|\leq16z^3\) on the entire range \(z=\pi n^2x^2\), \(n\geq1,x\geq1\). Summing the positive majorant from integer one, its geometric ratio is bounded by \(r_1=64e^{-3\pi}<64(3/8)^9<1/2\), so its coefficient is less than \(1024\). Applying the finite sum version of (A8) with \(b_1=2\pi>6\) gives, for every finite \(J\),

\[
 \mathcal M_J<2^{20}\left(\frac38\right)^6
 \sum_{j=0}^6\binom6j\frac{j!}{6^{j+1}}
 =\frac{3669}{2}<4096.
 \tag{A12}
\]

The companion script compares the rational number (A11) exactly and proves

\[
 J=6:\quad\widehat{\mathcal E}_7<10^{-111},\qquad
 J=8:\quad\widehat{\mathcal E}_9<10^{-191}.
\]

Using \(\sqrt{\mathcal M_J}<64\) in (A9) proves the conservative, fully explicit omitted-integer square-integral bounds

\[
 \boxed{|M_1''(0)-\mathcal M_6|<10^{-52},\qquad
 |M_1''(0)-\mathcal M_8|<10^{-92}.}
 \tag{A13}
\]

For example at \(J=6\), the right side of (A9) is less than \(128\cdot10^{-55}+10^{-111}<129\cdot10^{-55}<10^{-52}\); the calculation at \(J=8\) uses \(10^{-95}\) in place of \(10^{-55}\). These bounds do not require a numerical evaluation of \(\pi\), an exponential, or an improper integral. They certify the omitted integer contribution to the derivative-square integral. They do not certify floating-point evaluation of the retained finite integral.

## 6. Exact retained finite integral

For convenient comparison with a finite incomplete-gamma evaluation, set

\[
 d_1=30,\quad d_2=-60,\quad d_3=16,\quad a_n=\pi n^2.
\]

Direct expansion of \(H_J^2\) and the substitution \(v=(a_m+a_n)x^2\) prove

\[
 \boxed{\mathcal M_J=
 \sum_{m,n=1}^{J}\sum_{r,s=1}^{3}
 d_rd_s a_m^r a_n^s
 \frac{\Gamma(r+s+1/2,a_m+a_n)}
      {(a_m+a_n)^{r+s+1/2}}.}
 \tag{A14}
\]

The exterior factor two cancels the factor one half in the integral substitution, yielding coefficient one in this formula. Negative cross terms from \(d_2=-60\) remain. The constants in (A14) follow from the derivative source (A1); the coefficient four in the supplied formula for \(M_1(\theta)\) has its own original source factors and cannot be copied into (A14).

## Check artifacts and scope

The standalone script `toda_theta_derivative_independent_check_20260912.py` uses SymPy for the displayed polynomial identities and exact rational arithmetic for the remaining comparisons. It completed 14 explicit checks and wrote `toda_theta_derivative_independent_check_result_20260912.json`. Explicit runtime checks are used; their enforcement does not depend on Python assertions. The proof of the infinite estimates is in (A6)–(A13), including the actual domains, constants, signs and exterior measure. This audit neither executes Lean nor claims a directed-rounding enclosure for the decimal approximation of \(M_1''(0)\).
