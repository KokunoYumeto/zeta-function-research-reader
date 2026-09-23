# The sine companion, Hermitian pairing, and the original even receiver

Date: 2026-09-23. This independent derivation extends the actual test at the original heat time \(t=1/32\). It retains the original density, coordinates, filter, Mellin convention, and coefficients in \(f_\pm=f_c\pm if_s\).

Source reading: `../arithmetic_pairing_20260923/ACTUAL_ENDPOINT_PAIRING.tex` was read in full. Its original density and heat convention are Brad Rodgers and Terence Tao, [*The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), original-source equations `phidef`, `htdef`, `hoz`, and `sas`. The pairing convention is that of the AP proof, with Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068v1), Appendix II, cited there. This task read those programme formulas; it does not claim a new reading of the original author source archives.

The original prime receiver has domain \(\mathcal S(\mathbb R)^{\rm even}\). The odd test is sent to that domain through the explicit map proved in Section 6. It is never treated as an element of the original even domain.

## 1. The original two source functions

Put

\[
\begin{aligned}
\Phi(u)&=\sum_{n=1}^{\infty}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},\\
H(x)&=\int_0^\infty e^{u^2/32}\Phi(u)\cos(xu)\,du,\\
J_j&=\int_0^\infty u^je^{u^2/32}\Phi(u)\,du,
\qquad C=J_0.
\end{aligned}
\tag{PP1}
\]

Every original summand of \(\Phi\) is positive on \(u\ge0\). The AP8 bound, independently proved in `../arithmetic_pairing_20260923/INDEPENDENT_TAIL_BOUNDS.md`, TB1–5, is

\[
J_j<\frac{j!}{3^{j+1}},\qquad |H^{(j)}(x)|\le J_j.
\tag{PP2}
\]

Its proof retains the full density and uses
\(e^{4u}\ge1+4u+8u^2\), \(\pi>3\), \(\pi^2<10\), and
\(\sum_{n\ge1}n^2e^{-3n^2}<1/20\). In particular differentiation under PP1 is justified, \(H\) is real and even, and

\[
H(0)=C>0,\quad H'(0)=0,\quad H''(0)=-J_2<0.
\tag{PP3}
\]

Retain \(q(x)=e^{-8x^2}\), \(D=d/dx\), and \(L=D^2-1/4\). Define

\[
\begin{aligned}
h_c(x)&=q(x)H(x)\cos(16x),& f_c&=Lh_c,\\
h_s(x)&=q(x)H(x)\sin(16x),& f_s&=Lh_s,\\
h_\pm(x)&=q(x)H(x)e^{\pm16ix},& f_\pm&=Lh_\pm=f_c\pm if_s.
\end{aligned}
\tag{PP4}
\]

These are the unscaled cosine, sine, and exponential functions. In particular,

\[
f_c=\frac{f_++f_-}{2},\qquad
f_s=\frac{f_+-f_-}{2i}.
\tag{PP5}
\]

All functions and their derivatives have Gaussian decay times a polynomial by PP2. Thus they are Schwartz, their Mellin transforms are entire, and every convolution and integration by parts used below is absolutely justified. The functions \(h_c,f_c\) are real and even; \(h_s,f_s\) are real and odd.

For any function \(G\) with the requisite derivatives, put

\[
\begin{aligned}
\mathcal U_G(x)&=(256x^2-1089/4)G(x)-32xG'(x)+G''(x),\\
\mathcal V_G(x)&=512xG(x)-32G'(x).
\end{aligned}
\]

Direct differentiation of the full operator \(L\) gives

\[
\begin{aligned}
f_c(x)&=q(x)[\mathcal U_H(x)\cos(16x)+\mathcal V_H(x)\sin(16x)],\\
f_s(x)&=q(x)[\mathcal U_H(x)\sin(16x)-\mathcal V_H(x)\cos(16x)].
\end{aligned}
\tag{PP6}
\]

The sign of the sine companion's cosine coefficient is fixed by differentiating \(\sin(16x)\); the \(-1/4\) term of \(L\) contributes to the retained coefficient \(-1089/4\).

For later derivative checks, define

\[
\begin{aligned}
\mathcal P_G(x)&=(13060x-4096x^3)G(x)
+(768x^2-3265/4)G'(x)-48xG''(x)+G'''(x),\\
\mathcal Q_G(x)&=(4868-12288x^2)G(x)+1536xG'(x)-48G''(x).
\end{aligned}
\]

Then

\[
\begin{aligned}
f_c'(x)&=q(x)[\mathcal P_H(x)\cos(16x)+\mathcal Q_H(x)\sin(16x)],\\
f_s'(x)&=q(x)[\mathcal P_H(x)\sin(16x)-\mathcal Q_H(x)\cos(16x)].
\end{aligned}
\tag{PP7}
\]

For verification, differentiate \(q(\mathcal U_G\cos+\mathcal V_G\sin)\), using \(q'=-16xq\). Its coefficients are
\(\mathcal U_G'-16x\mathcal U_G+16\mathcal V_G\) and
\(\mathcal V_G'-16x\mathcal V_G-16\mathcal U_G\). Expanding gives exactly \(\mathcal P_G,\mathcal Q_G\). Differentiating the second line of PP6 gives the second line of PP7 with the same coefficients and its displayed minus sign.

## 2. Mellin transforms and every original completion factor

Use exactly

\[
\mathcal M f(s)=\int_{\mathbb R}f(x)e^{-(s-1/2)x}\,dx,
\qquad w=s-\frac12,
\qquad t=\frac1{32}.
\tag{PP8}
\]

Write \(F_c=\mathcal M f_c\), \(F_s=\mathcal M f_s\), and \(F_\pm=\mathcal M f_\pm\). Two integrations by parts give the exact factor

\[
\mathcal M(Lh)(s)=\left[(s-1/2)^2-\frac14\right]\mathcal M h(s)
=s(s-1)\mathcal M h(s).
\tag{PP9}
\]

Therefore all four filtered transforms vanish at both original endpoints \(s=0,1\).

For a complete original-zeta expression put
\(\sigma_1=1+itw\), \(\sigma_0=itw\), and retain

\[
\begin{aligned}
T_1(s)={}&e^{t(w-i/(2t))^2}
\sigma_1(\sigma_1-1)\pi^{-\sigma_1/2}
\Gamma(\sigma_1/2)\zeta(\sigma_1),\\
T_0(s)={}&e^{t(w+i/(2t))^2}
\sigma_0(\sigma_0-1)\pi^{-\sigma_0/2}
\Gamma(\sigma_0/2)\zeta(\sigma_0).
\end{aligned}
\tag{PP10}
\]

Each complete product is analytically continued at its exceptional arguments. In particular the original pole and Gamma contribution at arguments one and zero give product value one at each argument. Gaussian integration from the original density, as in ER32 and AP3, gives

\[
\begin{aligned}
F_c(s)&=\frac{s(s-1)\sqrt{\pi t}}{16}[T_1(s)+T_0(s)],\\
F_s(s)&=\frac{s(s-1)\sqrt{\pi t}}{16i}[T_1(s)-T_0(s)],\\
F_+(s)&=\frac{s(s-1)\sqrt{\pi t}}8T_1(s),\\
F_-(s)&=\frac{s(s-1)\sqrt{\pi t}}8T_0(s).
\end{aligned}
\tag{PP11}
\]

For example
\(\mathcal M h_+(s)=2\sqrt{\pi t}\,e^{t(w-i/(2t))^2}H_0(2tw-i)\),
and the original identity
\(16H_0(z)=\sigma(\sigma-1)\pi^{-\sigma/2}\Gamma(\sigma/2)\zeta(\sigma)\)
at \(\sigma=1/2+iz/2\) yields the first exponential formula. The negative exponential gives the second. PP5 then gives both factors \(1/16\) and \(1/(16i)\) in PP11. No coefficient rescaling has been made.

Parity and reality also prove the exact transform identities

\[
F_c(1-s)=F_c(s),\qquad F_s(1-s)=-F_s(s),
\qquad \overline{F_j(\bar s)}=F_j(s)\quad(j=c,s).
\tag{PP12}
\]

These statements follow directly by changing \(x\) to \(-x\) and conjugating the convergent integrals. They make no assertion about common zeros or time transport.

## 3. The Hermitian form and exact parity cancellation

For a complex source define its actual reflected conjugate by

\[
\widetilde f(x)=\overline{f(-x)}.
\]

For two sources \(f,g\), put

\[
k_{f,g}=f*\widetilde g,
\qquad
A_{f,g}(s)=F(s)\overline{G(1-\bar s)}
=\mathcal M k_{f,g}(s).
\tag{PP13}
\]

The second equality is Fubini applied to the convolution and the identity
\(\mathcal M\widetilde g(s)=\overline{G(1-\bar s)}\). This fixes the convention: the pairing is linear in its first entry and conjugate-linear in its second.

Let \(\rho\) run over all actual nontrivial zeros of the original zeta function with their multiplicities. Define

\[
\mathcal B(f,g)=\sum_\rho m_\rho
F(\rho)\overline{G(1-\bar\rho)}.
\tag{PP14}
\]

The Gaussian derivative estimates give arbitrary inverse-power decay of these transforms on every fixed vertical strip. Together with the zero count used in AP6, this proves absolute convergence. Therefore the original functional equation's multiplicity-preserving maps \(\rho\mapsto1-\rho\) and \(\rho\mapsto1-\bar\rho\) may be used to reindex the sum. In particular

\[
\mathcal B(f,g)=\overline{\mathcal B(g,f)}.
\tag{PP15}
\]

To check PP15 directly, conjugate \(\mathcal B(g,f)\) and reindex by \(\rho\mapsto1-\bar\rho\). This uses the original zero symmetry and does not replace a reflected product by an absolute square away from the critical line.

For the real parity sources,

\[
\widetilde f_c=f_c,\qquad \widetilde f_s=-f_s,
\qquad \widetilde f_\pm=f_\pm.
\tag{PP16}
\]

Define the two actual autocorrelations and one mixed convolution by

\[
k_c=f_c*f_c,\qquad k_s=-f_s*f_s,
\qquad m=f_c*f_s.
\tag{PP17}
\]

Here \(k_c,k_s\) are real and even and \(m\) is real and odd. Consequently

\[
\begin{aligned}
K_c&:=\mathcal B(f_c,f_c)=\sum_\rho m_\rho F_c(\rho)^2,\\
K_s&:=\mathcal B(f_s,f_s)=-\sum_\rho m_\rho F_s(\rho)^2,\\
\mathcal B(f_c,f_s)&=-\sum_\rho m_\rho F_c(\rho)F_s(\rho)=0,\\
\mathcal B(f_s,f_c)&=\sum_\rho m_\rho F_s(\rho)F_c(\rho)=0.
\end{aligned}
\tag{PP18}
\]

Indeed the product \(F_cF_s\) changes sign under \(s\mapsto1-s\) by PP12, and absolute convergence permits pairing the terms. Any fixed point of the involution contributes zero because an odd-about-\(1/2\) product vanishes there. Thus the cancellation also covers fixed points and multiplicities exactly.

The complete arithmetic expression has the same cancellation. For a Gaussian convolution \(k\), retain both prime legs and the symmetric Gamma numerator:

\[
\begin{aligned}
\mathcal P(k)&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
[k(\log n)+k(-\log n)],\\
\mathcal A_\infty(k)&=-(\gamma_{\rm E}+\log\pi)k(0)\\
&\quad+\int_0^\infty
\frac{e^{-x}k(0)-\tfrac12e^{-x/4}[k(x/2)+k(-x/2)]}{1-e^{-x}}\,dx.
\end{aligned}
\tag{PP19}
\]

On an even convolution PP19 is precisely AP4–5, including the prime factor two. On the odd convolution \(m\), every displayed term is zero: \(m(0)=0\), the two prime evaluations add to zero, and the two Gamma evaluations add to zero. This is a proof of cancellation in the full receiving formula, with every original prime power and both Gamma evaluations retained.

For \(k_s\), its Mellin transform is \(-F_s^2\), which is even under \(s\mapsto1-s\), is entire, and vanishes at \(s=0,1\). It therefore satisfies exactly the hypotheses of the AP6 contour calculation. The finite trivial-zero contribution is
\(U_N=\sum_{j=1}^N[-F_s(-2j)^2]\), the pole contribution is \(-A(1)=0\), and the Gamma-edge shift adds \(A(0)+U_N=U_N\). Subtracting these finite terms gives

\[
\boxed{K_j=\mathcal A_\infty(k_j)-\mathcal P(k_j)
=\mathcal A_\infty(k_j)
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}k_j(\log n),
\quad j=c,s.}
\tag{PP20}
\]

No independent infinite value is assigned to the individual trivial-zero sum. For the mixed product both its zero receiver and its arithmetic receiver vanish by the explicit parity calculations above. By sesquilinearity, these facts prove the complete arithmetic formula on the full complex span of \(f_c,f_s\).

## 4. The matrix in the unscaled exponential basis

For \(v=af_c+bf_s\), \(w=cf_c+df_s\), PP18 gives

\[
\boxed{\mathcal B(v,w)=K_ca\bar c+K_sb\bar d.}
\tag{PP21}
\]

Using exactly \(f_\pm=f_c\pm if_s\), the four source convolutions are

\[
\begin{aligned}
k_{+,+}&=k_c+k_s+2im,&
k_{-,-}&=k_c+k_s-2im,\\
k_{+,-}&=k_c-k_s,&
k_{-,+}&=k_c-k_s.
\end{aligned}
\tag{PP22}
\]

The imaginary odd contribution in the diagonal exponential convolutions is part of the source. PP19 proves that its entire arithmetic receiver is zero. Hence the exact Hermitian matrix, with rows and columns ordered \((f_+,f_-)\), is

\[
\boxed{
G_\pm=
\begin{pmatrix}
K_c+K_s&K_c-K_s\\
K_c-K_s&K_c+K_s
\end{pmatrix}.}
\tag{PP23}
\]

In particular, for the original exponential coefficients \(\alpha,\beta\),

\[
\begin{aligned}
\alpha f_++\beta f_-&=(\alpha+\beta)f_c+i(\alpha-\beta)f_s,\\
\mathcal B(\alpha f_++\beta f_-,\alpha f_++\beta f_-)
&=K_c|\alpha+\beta|^2+K_s|\alpha-\beta|^2.
\end{aligned}
\tag{PP24}
\]

The matrix's vectors \((1,1)\) and \((1,-1)\) have eigenvalues \(2K_c\) and \(2K_s\), respectively, by direct matrix multiplication. This does not replace the original vectors by vectors divided by \(\sqrt2\). Any sign for \(K_s\) is to be supplied by the separate interval calculation; parity alone has not assigned that sign.

## 5. The odd moment pair and its first nonzero jet

Because \(f_s\) is odd and integrable,

\[
\boxed{f_s(0)=0,\qquad \int_{\mathbb R}f_s(x)\,dx=0.}
\tag{PP25}
\]

This is an evaluation of two scalar functionals. It does not put \(f_s\) into the even domain of the original prime receiver.

The first derivative is nonzero. At zero PP7 and PP3 give

\[
\boxed{B_1:=f_s'(0)=-4868C-48J_2<0.}
\tag{PP26}
\]

One can verify every original derivative contribution directly. If \(a(x)=q(x)H(x)\), then
\(a(0)=C\), \(a''(0)=-16C-J_2\),
\(h_s'(0)=16C\), and

\[
h_s'''(0)=48(-16C-J_2)-4096C=-4864C-48J_2.
\]

Subtracting \(h_s'(0)/4=4C\), as required by the original filter, gives exactly PP26.

For the even source, retain the already evaluated moments

\[
A:=f_c(0)=-J_2-\frac{1089}{4}C<0,
\qquad
B_0:=\int_{\mathbb R}f_c(x)\,dx
=-\frac{\sqrt{\pi/32}}{32}e^{-8}<0.
\tag{PP27}
\]

The integral follows by integrating \(f_c=h_c''-h_c/4\) and retaining the exact endpoint-residue value
\(\int h_c=\sqrt{\pi/32}\,e^{-8}/8\). Thus on the actual two-dimensional source space

\[
V=\operatorname{span}_{\mathbb C}\{f_c,f_s\},
\]

the first two jets give a coefficient inverse:

\[
v=af_c+bf_s
\quad\Longrightarrow\quad
a=\frac{v(0)}{A},\qquad b=\frac{v'(0)}{B_1}.
\tag{PP28}
\]

The equations hold because \(f_s(0)=f_c'(0)=0\). Since both denominators are nonzero, this also proves linear independence of the two original sources. In exponential coefficients the same inverse is

\[
\alpha=\frac12\left(\frac{v(0)}A-\frac{i\,v'(0)}{B_1}\right),
\qquad
\beta=\frac12\left(\frac{v(0)}A+\frac{i\,v'(0)}{B_1}\right).
\tag{PP29}
\]

## 6. The exact bridge into the original even prime receiver

Write \(\mathcal H=\mathcal S(\mathbb R)^{\rm even}\). Let
\(P_ev(x)=[v(x)+v(-x)]/2\) and
\(P_ov(x)=[v(x)-v(-x)]/2\). On the specified domain \(V\), define

\[
U:V\longrightarrow\mathcal H,
\qquad Uv=P_ev+D(P_ov).
\tag{PP30}
\]

Thus

\[
U(af_c+bf_s)=af_c+bf_s'.
\]

The output is even. Its original two moments \(m(g)=(g(0),\int g)\) are

\[
\boxed{m(Uv)=
\begin{pmatrix}A&B_1\\B_0&0\end{pmatrix}
\binom ab=(Aa+B_1b,B_0a).}
\tag{PP31}
\]

Indeed \(f_s'\) is even and Schwartz, and \(\int f_s'=0\) because \(f_s\) tends to zero at both ends. The determinant is \(-B_0B_1\ne0\). Therefore \(U\) is an isomorphism from \(V\) onto its actual image \(W=\operatorname{span}\{f_c,f_s'\}\subset\mathcal H\), and its inverse coefficients on \(W\) are

\[
\boxed{a=\frac{m_1(g)}{B_0},\qquad
b=\frac{m_0(g)-A\,m_1(g)/B_0}{B_1}.}
\tag{PP32}
\]

Here \(m_0(g)=g(0)\) and \(m_1(g)=\int g\), so the subscript one labels the integral functional, not a derivative.

The inverse also has an exact antiderivative form. Define

\[
\mathcal H_{\int0}=\{g\in\mathcal H:\int_{\mathbb R}g=0\},
\qquad
(Jg)(x)=\int_0^xg(y)\,dy.
\]

Then \(D:\mathcal S^{\rm odd}\to\mathcal H_{\int0}\) is a continuous isomorphism with inverse \(J\). To prove this, differentiation and integration preserve the required parity. For \(g\in\mathcal H_{\int0}\), evenness implies \(\int_0^\infty g=0\), so for \(x>0\),
\(Jg(x)=-\int_x^\infty g(y)\,dy\); the negative half-line follows by oddness. Every Schwartz decay bound follows by integrating a stronger polynomial decay bound for \(g\), and every positive-order derivative of \(Jg\) is a derivative of \(g\). On bounded intervals continuity follows from the defining integral. Finally \(DJg=g\), and \(JDf=f-f(0)=f\) for odd \(f\). This proves the asserted two-sided inverse and its actual domains.

Consequently, for \(g\in W\), with \(a=m_1(g)/B_0\),

\[
\boxed{U^{-1}g=af_c+J(g-af_c).}
\tag{PP33}
\]

The subtracted function has integral zero by definition of \(a\), and on \(W\) it is exactly \(bf_s'\); the last term is therefore \(bf_s\). No claim is made that the formula \(P_e+DP_o\) is injective on the entire Schwartz space.

Now use the original ring and receiver without changing its domain:

\[
R=\mathbb C[\mathbb Q_{>0}^{\times}],\quad
I=\ker(\operatorname{aug}:R\to\mathbb C),\quad
M_0=\ker(\operatorname{aug}\otimes m),\quad Q_0=M_0/IM_0.
\]

For each prime \(p\), the original map satisfies

\[
\beta[(t_p-1)\otimes g]=\ell_p\otimes m(g),\qquad g\in\mathcal H.
\]

Its actual use for the two-source plane is therefore

\[
\begin{aligned}
\iota_p:V&\longrightarrow Q_0,
&\iota_p(v)&=[(t_p-1)\otimes Uv],\\
\beta\iota_p(v)&=\ell_p\otimes(Aa+B_1b,B_0a).
\end{aligned}
\tag{PP34}
\]

The class is defined because \(\operatorname{aug}(t_p-1)=0\). The vector \(\ell_p\) is the original nonzero valuation generator of \(I/I^2\). For completeness, its nonvanishing follows from \(v_p(t_p-1)=1\), while every product of two augmentation-zero elements is killed by the valuation map; thus the functional descends to \(I/I^2\) and detects this generator.

If \(\iota_p(v)=0\), applying \(\beta\) and then the coordinate functional taking \(\ell_p\) to one gives \(m(Uv)=0\). The invertible matrix PP31 gives \(a=b=0\). Hence \(\iota_p\) is injective. The same argument proves that \(\beta\) restricted to \(\iota_p(V)\) is an isomorphism onto the entire fibre \(\ell_p\otimes\mathbb C^2\). Equations PP32–33 are its explicit coefficient and source inverse after identifying that fixed fibre with \(\mathbb C^2\).

For the original exponential coefficients the receiver matrix is

\[
\boxed{
m\bigl(U(\alpha f_++\beta f_-)\bigr)
=\begin{pmatrix}A+iB_1&A-iB_1\\B_0&B_0\end{pmatrix}
\binom\alpha\beta,\qquad
\det=2iB_0B_1\ne0.}
\tag{PP35}
\]

Thus both original exponential coefficients are recovered without putting the odd function into the old even domain.

The Hermitian form carried to this original receiver is specified by its inverse. If \(z=(z_0,z_1)=m(Uv)\) and \(w=(w_0,w_1)=m(Uu)\), define

\[
\boxed{
\mathcal B_{\rm rec}(z,w)
=K_c\frac{z_1\overline{w_1}}{B_0^2}
+K_s\frac{(z_0-Az_1/B_0)\overline{(w_0-Aw_1/B_0)}}{B_1^2}.}
\tag{PP36}
\]

PP21 and PP32 prove \(\mathcal B_{\rm rec}(m(Uv),m(Uu))=\mathcal B(v,u)\). The matrix in the ordered coordinates \((z_0,z_1)\) is exactly

\[
\boxed{
G_{\rm rec}=\begin{pmatrix}
K_s/B_1^2&-AK_s/(B_0B_1^2)\\
-AK_s/(B_0B_1^2)&K_c/B_0^2+A^2K_s/(B_0^2B_1^2)
\end{pmatrix}.}
\tag{PP37}
\]

This transported form uses the explicit map \(U^{-1}\). The numerical Weil form evaluated directly on the even function \(Uv\) is a different stated calculation: indeed
\(\mathcal M(f_s')(s)=(s-1/2)F_s(s)\), by integration by parts, so its mixed transform with \(f_c\) is \((s-1/2)F_c(s)F_s(s)\), which is even under \(s\mapsto1-s\). The previous odd-product cancellation does not assert that this new mixed receiver vanishes. Thus the exact coefficient bridge and the transported form have been specified without silently imposing an isometry for direct evaluation on \(W\).

All these linear maps have the usual exact lift to the original support carrier: \((v,1_L)\mapsto(Uv,1_L)\), with every lower labelled zero \((0,\lambda)\) fixed. The inverse on \(W\) has the same property. Injectivity on the source plane and preservation of every support label follow from the proved linear inverse and the unchanged labels.

## 7. Complete residual bounds for the odd autocorrelation

Keep \(R(x)=H(x)-C\), and define the comparison function and its entire residual by

\[
\begin{aligned}
f_{s0}(x)&=Cq(x)[(256x^2-1089/4)\sin(16x)-512x\cos(16x)],\\
e_s(x)&=f_s(x)-f_{s0}(x)
=q(x)[\mathcal U_R(x)\sin(16x)-\mathcal V_R(x)\cos(16x)].
\end{aligned}
\tag{PP38}
\]

The original moment bounds give exactly

\[
|R(x)|\le J_2x^2/2,\quad |R'(x)|\le J_2|x|,
\quad |R''(x)|\le J_2,\quad |R'''(x)|\le J_3.
\tag{PP39}
\]

Define the same positive polynomials as in AP12:

\[
\begin{aligned}
A_*(r)&=1089/4+512r+256r^2,\\
E(r)&=1+32r+(1345/8)r^2+256r^3+128r^4,\\
B_*(r)&=4868+13060r+12288r^2+4096r^3,\\
E_1(r)&=48+(3457/4)r+3970r^2+7298r^3+6144r^4+2048r^5.
\end{aligned}
\tag{PP40}
\]

Stars here distinguish these envelope polynomials from the receiver constants \(A,B_0,B_1\); their values and coefficients are exactly those of AP12. PP6–7 and PP39 give

\[
\begin{array}{ll}
|f_{s0}(x)|\le Cq(x)A_*(|x|),&
|e_s(x)|\le J_2q(x)E(|x|),\\
|f_{s0}'(x)|\le Cq(x)B_*(|x|),&
|e_s'(x)|\le q(x)[J_2E_1(|x|)+J_3].
\end{array}
\tag{PP41}
\]

To prove the coefficient transfer precisely, the pairs of coefficient functions in PP38 and its derivative are \((\mathcal U_R,-\mathcal V_R)\) and \((\mathcal P_R,-\mathcal Q_R)\). Their absolute sums equal the absolute sums of the cosine residual's pairs \((\mathcal U_R,\mathcal V_R)\) and \((\mathcal P_R,\mathcal Q_R)\). Therefore every positive coefficient in the four envelopes is unchanged; no discarded residual or new coefficient convention is involved.

Define

\[
k_{s0}=-f_{s0}*f_{s0},\qquad \Delta_s=k_s-k_{s0}
=-2f_{s0}*e_s-e_s*e_s.
\tag{PP42}
\]

For any positive-coefficient polynomial \(P\), retain

\[
\mathcal I(P)=\int_{\mathbb R}e^{-16x^2}P(|x|)\,dx,
\qquad
\mathcal I(r^j)=16^{-(j+1)/2}\Gamma((j+1)/2).
\]

With the exact AP16 values

\[
\begin{aligned}
n_0&=C\sqrt{\mathcal I(A_*^2)},&
n_e&=J_2\sqrt{\mathcal I(E^2)},\\
n_1&=C\sqrt{\mathcal I(B_*^2)},&
n_{e1}&=\sqrt{J_2^2\mathcal I(E_1^2)+2J_2J_3\mathcal I(E_1)+J_3^2\mathcal I(1)},\\
d_0&=2n_0n_e+n_e^2,&d_2&=2n_1n_{e1}+n_{e1}^2,
\end{aligned}
\tag{PP43}
\]

Cauchy–Schwarz applied to PP42 and its second derivative proves

\[
\boxed{|\Delta_s(x)|\le d_0,\quad
|\Delta_s''(x)|\le d_2,\quad
|\Delta_s(x)-\Delta_s(0)|\le\min(2d_0,d_2x^2/2).}
\tag{PP44}
\]

For example \(k_s''=-f_s'*f_s'\), and the minus sign disappears only inside the absolute-value bound. The last bound uses the proved evenness of both odd-source autocorrelations. Thus it has exactly the same hypothesis as AP17.

The stronger prime envelope also transfers unchanged:

\[
\boxed{
|\Delta_s(x)|\le e^{-4x^2}\mathcal I\left(
2CJ_2A_*(r+|x|/2)E(r+|x|/2)
+J_2^2E(r+|x|/2)^2\right)=:\mathcal D(x).}
\tag{PP45}
\]

Indeed, under \(y=x/2+z\),
\(y^2+(x-y)^2=x^2/2+2z^2\), and both absolute arguments are bounded by \(|z|+|x|/2\). PP41 has nonnegative envelope coefficients, so integrating proves PP45 with its full factor two for the two residual cross terms.

By PP2 and PP6, the same actual-source envelope used in AP19 holds:

\[
|f_s(x)|,|f_{s0}(x)|
\le(95+175|x|+86x^2)e^{-8x^2}
\le(183+174x^2)e^{-8x^2}.
\]

Convolving the final polynomial gives exactly the same universal bound

\[
\boxed{|k_s(x)|,|k_{s0}(x)|
\le(16000+6900x^2+850x^4)e^{-4x^2}.}
\tag{PP46}
\]

For clarity, the polynomial before the integer ceilings is
\((\sqrt\pi/4)[9105363/256+(247167/16)x^2+(7569/4)x^4]\), as obtained by the substitution above and the Gaussian second and fourth moments. Hence this is a direct bound on the odd autocorrelation, despite its representation as a negative self-convolution.

It follows, with the identical monotone integral comparisons proved in AP20–21 and TB20–30, that

\[
2\sum_{n>64}\frac{\Lambda(n)}{\sqrt n}|k_s(\log n)|<10^{-21},
\tag{PP47}
\]

and

\[
\int_8^\infty\frac{e^{-x}k_s(0)-e^{-x/4}k_s(x/2)}{1-e^{-x}}\,dx
=-k_s(0)\log(1-e^{-8})-\mathcal R_{s,8},
\qquad |\mathcal R_{s,8}|<10^{-23}.
\tag{PP48}
\]

The same Gamma statement holds for \(k_{s0}\). These bounds require only PP46, which has just been proved for both functions; no parity sign remains unaccounted for in them. All prime powers are included through \(\Lambda(p^a)=\log p\).

The odd function's autocorrelation obeys

\[
k_s(0)=\int f_s(y)^2\,dy>0,\qquad
k_s(0)-k_s(x)=\frac12\int[f_s(y)-f_s(y-x)]^2\,dy\ge0.
\tag{PP49}
\]

The first strict inequality follows from PP26. Expanding the second square proves the identity, using oddness to write \(-f_s*f_s\) as its real autocorrelation. The same assertions hold for \(f_{s0}\). Therefore the combined Gamma integrand has endpoint value \(-3k_s(0)/4\), and its comparison origin interval \([0,\varepsilon]\), \(0<\varepsilon\le1\), has absolute integral at most

\[
\frac32k_{s0}(0)\varepsilon+\frac{n_1^2\varepsilon^2}{8}.
\tag{PP50}
\]

The proof uses \(1-e^{-x}\ge x/2\),
\(|e^{-x}-e^{-x/4}|\le3x/4\), and
\(0\le k_{s0}(0)-k_{s0}(x/2)\le n_1^2x^2/8\), obtained from the translation difference in PP49 by the fundamental theorem of calculus and Cauchy–Schwarz. Every term has the same sign and factor as AP22.

Finally the complete Gamma residual bound is exactly

\[
\begin{aligned}
|\mathcal A_\infty(k_s)-\mathcal A_\infty(k_{s0})|
\le{}&\left[\gamma_{\rm E}+\log\pi+\frac32+4\log(1/b)
+\frac{e^{-1}+4e^{-1/4}}{1-e^{-1}}\right]d_0
+d_2b^2/8,\qquad b=\frac1{16}.
\end{aligned}
\tag{PP51}
\]

To see the transfer without assuming the result, the numerator difference on \((0,1]\) is
\((e^{-x}-e^{-x/4})\Delta_s(0)+e^{-x/4}[\Delta_s(0)-\Delta_s(x/2)]\).
The first part costs \(3d_0/2\). PP44 bounds the second part by \(d_2x^2/8\) below \(b\) and by \(2d_0\) above \(b\); dividing by \(1-e^{-x}\ge x/2\) and integrating gives \(d_2b^2/8+4d_0\log(1/b)\). For \(x\ge1\), bound the original two numerator terms directly and integrate their two exponentials, giving the last fraction in PP51. The retained prefactor contributes \((\gamma_{\rm E}+\log\pi)d_0\).

The finite prime residual is bounded by the same expression as AP24:
\(2\sum_{2\le n\le64}\Lambda(n)n^{-1/2}\mathcal D(\log n)\).
All constants in these transferred error expressions are the identical functions of the identical original moments \(C,J_2,J_3\). Thus an already certified bound on those AP error expressions also bounds the odd-source errors. The comparison Gamma integral and comparison finite prime sum themselves must use the odd convolution below; their values are not transferred from the cosine calculation.

## 8. Exact comparison autocorrelation and mixed convolution

Let \(h_{c0}=Cq\cos(16x)\), \(h_{s0}=Cq\sin(16x)\). With \(y=x/2+z\), the full product identities are

\[
\begin{aligned}
\cos(16y)\cos(16(x-y))&=\tfrac12[\cos(16x)+\cos(32z)],\\
\sin(16y)\sin(16(x-y))&=\tfrac12[\cos(32z)-\cos(16x)],\\
\cos(16y)\sin(16(x-y))&=\tfrac12[\sin(16x)-\sin(32z)].
\end{aligned}
\]

The Gaussian integral of the last odd sine is zero, while
\(\int e^{-16z^2}\cos(32z)\,dz=(\sqrt\pi/4)e^{-16}\). Therefore

\[
\begin{aligned}
h_{c0}*h_{c0}&=\frac{C^2\sqrt\pi}{8}e^{-4x^2}[\cos(16x)+e^{-16}],\\
-h_{s0}*h_{s0}&=\frac{C^2\sqrt\pi}{8}e^{-4x^2}[\cos(16x)-e^{-16}],\\
h_{c0}*h_{s0}&=\frac{C^2\sqrt\pi}{8}e^{-4x^2}\sin(16x).
\end{aligned}
\tag{PP52}
\]

Apply exactly \(L^2=D^4-D^2/2+1/16\) to each full expression. Set

\[
P(x)=65536x^4-1622528x^2+1250369,
\]

\[
S(x)=2048x(256x^2-1121),\qquad
T(x)=65536x^4-49664x^2+3137.
\]

The resulting exact comparison functions are

\[
\boxed{\begin{aligned}
k_{c0}(x)&=\frac{C^2\sqrt\pi}{128}e^{-4x^2}
[P(x)\cos(16x)+S(x)\sin(16x)+e^{-16}T(x)],\\
k_{s0}(x)&=\frac{C^2\sqrt\pi}{128}e^{-4x^2}
[P(x)\cos(16x)+S(x)\sin(16x)-e^{-16}T(x)],\\
m_0(x)&:=f_{c0}*f_{s0}(x)
=\frac{C^2\sqrt\pi}{128}e^{-4x^2}
[P(x)\sin(16x)-S(x)\cos(16x)].
\end{aligned}}
\tag{PP53}
\]

For an algebraic coefficient proof, let \(z=-8x+16i\). The exact derivative identities give

\[
L^2e^{-4x^2+16ix}
=\left(z^4-\frac{97}{2}z^2+\frac{3137}{16}\right)e^{-4x^2+16ix}
=\frac{P(x)-iS(x)}{16}e^{-4x^2+16ix}.
\]

The same calculation at \(z=-8x\) gives
\(L^2e^{-4x^2}=T(x)e^{-4x^2}/16\). Taking the real and imaginary parts of the first identity, and retaining the second term of each line of PP52 with its original sign, proves every coefficient in PP53.

The corresponding comparison convolutions in the unscaled exponential basis are consequently

\[
\begin{aligned}
k_{+,+,0}(x)&=\frac{C^2\sqrt\pi}{64}e^{-4x^2}
[P(x)-iS(x)]e^{16ix},\\
k_{-,-,0}(x)&=\frac{C^2\sqrt\pi}{64}e^{-4x^2}
[P(x)+iS(x)]e^{-16ix},\\
k_{+,-,0}(x)&=k_{-,+,0}(x)
=\frac{C^2\sqrt\pi}{64}e^{-16}e^{-4x^2}T(x).
\end{aligned}
\tag{PP54}
\]

These formulas also follow by substituting PP53 into PP22, and retain the entire opposite-frequency term. They do not assume that the full-source comparison residual has any particular sign.

## 9. Independent sign and type checks for the specified original moment action

This subsection checks the algebra of the original moment action supplied to this derivation, with the actual receiver matrix PP31. The root calculation separately reports certified bounds \(50<K_c,K_s<64\); no new numerical certificate is computed here. The metric used in these calculations is exactly

\[
G=\operatorname{diag}(K_c,K_s).
\]

The parameter \(T\) in this subsection belongs to the specified original moment action. The original heat time in \(H\), \(f_c\), \(f_s\), and all source constants remains fixed at \(t=1/32\). For real \(T>0\), retain the specified original moment operator and coefficient

\[
J_T=\begin{pmatrix}0&\kappa_T\\0&1\end{pmatrix},
\qquad \kappa_T=(4\pi T)^{-1/2},\qquad
M=\begin{pmatrix}A&B_1\\B_0&0\end{pmatrix}.
\]

The matrix \(M\) maps the original coefficient column \((a,b)^{\mathsf T}\) to the original receiver moments, and its inverse is

\[
M^{-1}=\begin{pmatrix}0&1/B_0\\1/B_1&-A/(B_0B_1)\end{pmatrix}.
\]

Consequently the exact receiving action on the source coefficients is

\[
\boxed{E_T=M^{-1}J_TM=
\begin{pmatrix}1&0\\c(T)&0\end{pmatrix},
\qquad c(T)=\frac{\kappa_TB_0-A}{B_1}.}
\tag{PP55}
\]

This follows by multiplying \(J_TM=\left(\begin{smallmatrix}\kappa_TB_0&0\\B_0&0\end{smallmatrix}\right)\). The output has \(E_T^2=E_T\), image spanned by \(u_T=(1,c(T))^{\mathsf T}\), and kernel spanned by \((0,1)^{\mathsf T}\).

Since \(A,B_0,B_1\) are all real and strictly negative by PP26–27, \(c(T)\) is real. The condition for selfadjointness in the actual metric is
\(E_T^*G=GE_T\). The two matrices are

\[
E_T^*G=\begin{pmatrix}K_c&K_sc(T)\\0&0\end{pmatrix},
\qquad
GE_T=\begin{pmatrix}K_c&0\\K_sc(T)&0\end{pmatrix}.
\]

Thus the exact selfadjoint time is determined by

\[
\boxed{c(T)=0\quad\Longleftrightarrow\quad
T=T_*:=\frac{(B_0/A)^2}{4\pi}.}
\tag{PP56}
\]

Both sides of \(\kappa_T=A/B_0\) are positive, so solving this equation introduces no additional sign branch. For every positive \(T\), the complete factorization is

\[
\boxed{
c(T)=-\frac{B_0(T-T_*)}
{B_1\sqrt{4\pi}\sqrt T\sqrt{T_*}(\sqrt T+\sqrt{T_*})}.}
\tag{PP57}
\]

Indeed \(A=B_0/(\sqrt{4\pi}\sqrt{T_*})\); subtract the two reciprocal square roots and rationalize their difference to obtain PP57 with the displayed minus sign.

Let \(d(T)=K_c+K_sc(T)^2>0\). The actual \(G\)-orthogonal projection onto the image of \(E_T\) is

\[
\boxed{P_T=\frac1{d(T)}
\begin{pmatrix}K_c&K_sc(T)\\K_cc(T)&K_sc(T)^2\end{pmatrix}.}
\tag{PP58}
\]

The formula is \(u_T(u_T^*G)/(u_T^*Gu_T)\). Hence \(P_T^2=P_T\), \(P_Tu_T=u_T\), and \(P_T^*G=GP_T\), all by direct multiplication with real \(c(T)\).

Put \(w_T=(-K_sc(T),K_c)^{\mathsf T}\) and let

\[
S_T=[u_T,w_T]=\begin{pmatrix}1&-K_sc(T)\\c(T)&K_c\end{pmatrix}.
\]

Its determinant is exactly \(d(T)>0\). The frame has not been rescaled. Its two vectors are \(G\)-orthogonal, with squared lengths \(d(T)\) and \(K_cK_sd(T)\), respectively. Moreover

\[
E_Tu_T=u_T,\quad P_Tu_T=u_T,\quad
E_Tw_T=-K_sc(T)u_T,\quad P_Tw_T=0.
\]

Therefore the exact metric defect \(N_T=E_T-P_T\) satisfies

\[
\boxed{S_T^{-1}N_TS_T=
\begin{pmatrix}0&-K_sc(T)\\0&0\end{pmatrix},
\qquad N_T^2=0.}
\tag{PP59}
\]

It is nonzero exactly when \(T\ne T_*\). At every such time the map
\(a+b\epsilon\mapsto aI+bN_T\) identifies the algebra
\(\mathbb C[\epsilon]/(\epsilon^2)\) with the actual two-dimensional operator algebra it generates. To check injectivity, if \(aI+bN_T=0\), apply the operator to \(u_T\ne0\) to obtain \(a=0\), and then apply it to \(w_T\) to obtain \(b=0\). Multiplication agrees because \(N_T^2=0\). At \(T=T_*\), the actual defect is zero and this representation sends \(\epsilon\) to zero.

The positive metric also gives exact operator norms, without changing the basis. From \(E_T(a,b)^{\mathsf T}=a\,u_T\),

\[
\|E_T\|_G^2=\frac{d(T)}{K_c}
=1+\frac{K_s}{K_c}c(T)^2.
\]

Substitution of the original \(c(T)\) yields

\[
\boxed{\|E_T\|_G^2=
1+\frac{K_s}{K_cB_1^2}
\left[\frac{B_0^2}{4\pi T}
-\frac{2B_0A}{\sqrt{4\pi T}}+A^2\right].}
\tag{PP60}
\]

For the supremum in this norm formula, the denominator is
\(K_c|a|^2+K_s|b|^2\), while the numerator is \(d(T)|a|^2\); equality is attained at \(b=0\). In the orthogonal frame above, PP59 also gives

\[
\|N_T\|_G^2=\frac{K_s}{K_c}c(T)^2,
\quad \|E_T\|_G^2=1+\|N_T\|_G^2.
\]

Thus the precise leading coefficient at the positive endpoint is
\(\lim_{T\downarrow0}T\|E_T\|_G^2=K_sB_0^2/(4\pi K_cB_1^2)>0\).
The original \(T^{-1/2}\) term with its minus sign and the constant term remain present in PP60.

Differentiate PP55 on the positive real line:

\[
E_T'=\begin{pmatrix}0&0\\c'(T)&0\end{pmatrix},\qquad
c'(T)=-\frac{B_0}{2B_1\sqrt{4\pi}\,T^{3/2}},\qquad
[E_T',E_T]=E_T'.
\tag{PP61}
\]

The commutator identity follows from \(E_T'E_T=E_T'\) and \(E_TE_T'=0\). The exact transport with initial time \(T_0>0\) is

\[
\boxed{L(T,T_0)=
\begin{pmatrix}1&0\\c(T)-c(T_0)&1\end{pmatrix},
\quad E_TL(T,T_0)=L(T,T_0)E_{T_0}.}
\tag{PP62}
\]

Direct multiplication gives both sides equal to \(E_T\).
Also \(\partial_TL=E_T'L=[E_T',E_T]L\),
\(L(T_0,T_0)=I\), and

\[
L(T_2,T_1)L(T_1,T_0)=L(T_2,T_0),\qquad
L(T_0,T)=L(T,T_0)^{-1}.
\tag{PP63}
\]

These identities show that the transport around a closed path within the positive real parameter line is the identity. The formulas are regular at \(T=T_*\), since that parameter is strictly positive. This transport preserves the specified idempotent action; it is not asserted to preserve the metric. For example the off-diagonal entry of \(L^*GL\) is \(K_s[c(T)-c(T_0)]\), which need not vanish. No identification of this parameter transport with zeta-zero heat evolution is used.

For a subsequent complex-analytic use of these matrices, the formula PP58 with complex \(c(T)\) is the holomorphic continuation of the real projection, on a chosen square-root branch and a domain where its denominator is nonzero. It is then an idempotent with the specified image; the Hermitian selfadjoint assertion in PP58 was proved for real positive \(T\). Complex conjugates must be retained if a Hermitian orthogonal projection is instead required at a nonreal parameter.

## Derivation and verification log

1. Read the complete AP mathematical source and retained its original time, Mellin convention, reflection, two prime legs, Gamma factors, finite trivial-zero cancellation, and coefficient conventions.
2. Derived the sine formula and its derivative, PP6–7, from the original differential filter.
3. Proved exact Hermitian parity cancellation, the full exponential matrix, and the odd first jet.
4. Incorporated the original even-domain constraint by proving the map \(U\), its moment and antiderivative inverses, and the injective map into the existing prime quotient. The transported pairing includes its inverse explicitly.
5. Proved transfer of every AP residual envelope and tail to the actual odd autocorrelation, with all minus signs retained before absolute estimates.
6. Derived the exact odd and mixed comparison convolutions from Gaussian product integrals and the full filter.
7. Used exact symbolic differentiation to verify four identities: the sine filter formula, its derivative, the odd comparison convolution, and the mixed comparison convolution. All four checks passed.
8. Independently checked the specified original moment action's conjugation, unique selfadjoint time, exact metric defect, unscaled frame, dual-number representation, all three operator-norm terms, and the idempotent-preserving transport. Recorded the real versus holomorphic projection domains explicitly.
9. Exact symbolic matrix checks passed for \(M^{-1}J_TM\), the unscaled matrix of \(N_T\), \(N_T^2=0\), and the intertwining relation for \(L(T,T_0)\).

This derivation did not perform the new numerical interval evaluation, derive global Mellin-pair nonvanishing, derive coupled time transport, discover external files or literature, render figures, package artifacts, or publish anything.
