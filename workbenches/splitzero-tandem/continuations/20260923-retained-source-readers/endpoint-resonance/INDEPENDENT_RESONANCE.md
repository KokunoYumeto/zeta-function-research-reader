# Independent derivation of the endpoint resonances

Date: 2026-09-23. This note is an independent calculation for the positive-time full theta filter. It proves its two resonant moments on the original theta source, the resulting obstruction on tempered distributions, and the complete boundary Wronskians of the two specified lateral continuations. It also proves the independence of the median endpoint and its homogeneous jump modulo tempered distributions. It makes no assertion about RH.

## Reading and source record

The local source documents read in full are `../ENDPOINT_SECTORIAL_HEAT_EXTENSION.tex` (ESH1–18) and `../COMPLETION_FACTOR_FULL_HEAT_MAP.tex` (CF1–43). The calculations below use their actual original-coordinate theta definitions, their proof of the original-zeta residue, and their specified upper/lower continuation in the **q-plane**, where q=−t. No change of that orientation is made.

The original human theta source cited by those documents is Brad Rodgers and Terence Tao, [*The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), equations `phidef`, `htdef`, `hoz`, and `sas`. Their original TeX reading is recorded in CF1. The present note does not claim a new or complete reading of that paper. The erfc definition used below is the entire primitive in ESH3, with its original equation source [N. M. Temme, DLMF 7.2.2](https://dlmf.nist.gov/7.2.E2). Every identity beyond the input source formulas is proved below.

## ER1. Original objects and their real-axis distribution domain

Fix a real number t>0 throughout. Retain exactly

\[
\begin{split}
\Phi(u)&=\sum_{n=1}^{\infty}
  (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},\\
H_t(Z)&=\int_0^\infty e^{tu^2}\Phi(u)\cos(Zu)\,du,\\
\mathcal N_t&=-\frac{1+(Z-2t\partial_Z)^2}{64}\\
&=-\frac{1+Z^2-2t-4tZ\partial_Z+4t^2\partial_Z^2}{64}.
\end{split}\tag{ER1}
\]

The auxiliary expressions

\[
Q(Z)=\frac{Z^2}{4t},\qquad k=\frac1{2t},\qquad
c_t=\sqrt{\frac\pi t}\,e^{-1/(4t)}
\tag{ER2}
\]

are abbreviations for the displayed, fixed original coefficients; neither the coordinate nor the heat time is changed.

Let \(\mathcal S(\mathbb R)\) be the space of complex smooth functions for which every seminorm \(\sup_{Z\in\mathbb R}|Z^a\partial_Z^b\varphi(Z)|\), a,b≥0, is finite. Write \(\mathcal S'(\mathbb R)\) for its continuous complex-linear dual, using the bilinear pairing \(\langle T,\varphi\rangle\), with no conjugation in the test argument. Let \(\mathcal D'(\mathbb R)\) denote the distributions on compactly supported smooth tests. These domain choices matter: multiplication by \(e^{Q}\) is always defined on \(\mathcal D'\), but is not an unrestricted operation on \(\mathcal S'\).

For each integer m≥0,

\[
\sup_{Z\in\mathbb R}|\partial_Z^m H_t(Z)|
 \le \int_0^\infty u^m e^{tu^2}\Phi(u)\,du<\infty.
\tag{ER3}
\]

Indeed CF3 proves \(0<\Phi(u)\le K_\Phi e^{9u-\pi e^{4u}/2}\), where
\(K_\Phi=2\pi^2\sum_{n\ge1}n^4e^{-\pi n^2/2}<\infty\). This integrable majorant, multiplied by \(u^me^{tu^2}\), proves the asserted differentiations and bounds. Thus \(H_t\) defines a tempered distribution by integration. The polynomial-coefficient differential expression \(\mathcal N_t\) is a continuous map on both \(\mathcal S\) and \(\mathcal S'\), and also acts on \(\mathcal D'\). On \(\mathcal S'\) its transpose is defined by

\[
\langle\mathcal N_t T,\varphi\rangle
 =\langle T,\mathcal N_t^{\mathrm T}\varphi\rangle,
\qquad
\mathcal N_t^{\mathrm T}
 =-\frac{1+(Z+2t\partial_Z)^2}{64}
 =-\frac{1+Z^2+2t+4tZ\partial_Z+4t^2\partial_Z^2}{64}.
\tag{ER4}
\]

Every test in ER4 stays in \(\mathcal S\); there is no unproved integration boundary at infinity in this distributional definition.

## ER2. The exact arithmetic value entering the moments

Keep the original zeta function and its entire product comparison:

\[
16H_0\!\left(-2i(s-\tfrac12)\right)
 =s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{ER5}
\]

Here \(\zeta(s)=\sum_{n\ge1}n^{-s}\) initially for \(\Re s>1\), followed by its meromorphic continuation. For completeness its residue follows, on that half-plane, from

\[
\zeta(s)
 =s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx
 =\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\tag{ER6}
\]

The last integral is holomorphic on \(\Re s>0\): on a compact subset, every s-derivative is bounded by an integrable multiple of \(x^{-1-\delta}(1+|\log x|^m)\) for a positive δ. Hence \(\operatorname{Res}_{s=1}\zeta(s)=1\). Taking the full product limit in ER5, and retaining \(\Gamma(1/2)=\sqrt\pi\), gives

\[
16H_0(-i)
 =1\cdot\pi^{-1/2}\Gamma(1/2)
       \operatorname{Res}_{s=1}\zeta(s)=1.
\tag{ER7}
\]

Evenness of the original cosine gives \(H_0(i)=H_0(-i)=1/16\). At the other endpoint the same comparison retains \(s\Gamma(s/2)\to2\), \(s-1\to-1\), and \(\pi^{-s/2}\to1\), so the full factor has removable value −2 at zero, and ER5 gives \(\zeta(0)=-1/2\). Thus ER7 is an evaluation of the original full formula at its exceptional germs, rather than a replacement of that formula by a new function.

## ER3. Both resonant Gaussian moments, with the interchange proved

For ε∈{+1,−1}, define

\[
\psi_\varepsilon(Z)=e^{-Z^2/(4t)}e^{\varepsilon iZ/(2t)},
\qquad
\ell_\varepsilon(T)=\langle T,\psi_\varepsilon\rangle
\quad(T\in\mathcal S').
\tag{ER8}
\]

Every derivative of \(\psi_\varepsilon\) is a polynomial times the same Gaussian and bounded oscillatory exponential; hence \(\psi_\varepsilon\in\mathcal S\).

The double integral used to evaluate \(\ell_\varepsilon(H_t)\) is absolutely integrable, since

\[
\int_{\mathbb R}\int_0^\infty
 e^{-Z^2/(4t)}e^{tu^2}\Phi(u)|\cos(Zu)|\,du\,dZ
 \le 2\sqrt{\pi t}\int_0^\infty e^{tu^2}\Phi(u)\,du<\infty.
\tag{ER9}
\]

For real a the Gaussian Fourier integral is

\[
G_t(a):=\int_{\mathbb R}e^{-Z^2/(4t)}e^{iaZ}\,dZ
 =2\sqrt{\pi t}\,e^{-ta^2}.
\tag{ER10}
\]

One direct verification keeps its constants: differentiating under the Gaussian integral and integrating its Z-derivative gives \(G_t'(a)=-2taG_t(a)\), while the real Gaussian integral gives \(G_t(0)=2\sqrt{\pi t}\). This first-order equation proves ER10.

Expanding the actual cosine, without discarding either exponential, yields

\[
\begin{split}
&\int_{\mathbb R}e^{-Z^2/(4t)}e^{\varepsilon iZ/(2t)}
                   \cos(Zu)\,dZ\\
&\quad=\sqrt{\pi t}
 \left[e^{-t(u+\varepsilon/(2t))^2}
       +e^{-t(-u+\varepsilon/(2t))^2}\right]\\
&\quad=2\sqrt{\pi t}\,e^{-tu^2}e^{-1/(4t)}\cosh u.
\end{split}\tag{ER11}
\]

Fubini's theorem, ER11, and the original integral for \(H_0(i)\) now prove exactly

\[
\boxed{
\begin{split}
\ell_+(H_t)=\ell_-(H_t)
 &=2\sqrt{\pi t}\,e^{-1/(4t)}
      \int_0^\infty\Phi(u)\cosh u\,du\\
 &=2\sqrt{\pi t}\,e^{-1/(4t)}H_0(i)\\
 &=\frac{\sqrt{\pi t}}8e^{-1/(4t)}.
\end{split}}
\tag{ER12}
\]

In full arithmetic notation the last value is

\[
\frac{\sqrt{\pi t}}8e^{-1/(4t)}
 \bigl[1\cdot\pi^{-1/2}\Gamma(1/2)
       \operatorname{Res}_{s=1}\zeta(s)\bigr].
\tag{ER13}
\]

The cancellation of the two opposite heat weights in ER11–12 is an evaluated integral identity with both weights displayed; it does not alter the working definition ER1.

## ER4. The exact tempered-distribution obstruction

Direct differentiation gives

\[
(Z+2t\partial_Z)\psi_\varepsilon
 =\varepsilon i\psi_\varepsilon,
\qquad
\mathcal N_t^{\mathrm T}\psi_\varepsilon=0.
\tag{ER14}
\]

Consequently every \(T\in\mathcal S'\) satisfies

\[
\ell_\varepsilon(\mathcal N_tT)=0.
\tag{ER15}
\]

If \(\mathcal N_t T=H_t\) held in \(\mathcal S'\), ER15 would force both quantities in ER12 to vanish. Each is strictly positive for the fixed real t>0. Therefore

\[
\boxed{\text{There is no }T\in\mathcal S'(\mathbb R)
              \text{ with }\mathcal N_tT=H_t,\quad t>0.}
\tag{ER16}
\]

This conclusion covers arbitrary tempered distributions, rather than only functions of a chosen growth class. In particular it is not based on an unjustified assertion that every smooth tempered distribution has pointwise polynomial growth.

The two tests in ER8 are linearly independent, since after dividing by the nonzero Gaussian their quotient is the nonconstant exponential \(e^{iZ/t}\). They form the entire Schwartz kernel of \(\mathcal N_t^{\mathrm T}\). Indeed, for a smooth test \(\varphi=e^{-Q}v\), direct differentiation gives

\[
\mathcal N_t^{\mathrm T}\varphi
 =-\frac{e^{-Q}}{64}(v+4t^2v'').
\tag{ER17}
\]

The solutions of \(v''+k^2v=0\) are exactly \(a e^{ikZ}+b e^{-ikZ}\), giving ER8. The same statement for distribution solutions follows from the elementary first-order argument supplied in ER5 below. On even sources, \(\ell_+=\ell_-\), and their common restriction is the cosine moment. Their difference is the sine moment, which vanishes on every even distribution by reflection. Thus the original even theta source has one independent nonzero obstruction value, not two independently adjustable values.

There is a concrete representative of the obstruction class. Define the retained theta-only term

\[
L_t(Z)=8\int_0^\infty e^{tu^2+u}\psi(e^{4u})\cos(Zu)\,du,
\qquad \psi(x)=\sum_{n\ge1}e^{-\pi n^2x}.
\tag{ER18}
\]

The same domination as ER3 shows that \(L_t\) and every real-axis Z-derivative are bounded; in particular \(L_t\in\mathcal S'\). The retained integration boundary of ESH17 is

\[
\mathcal N_t L_t=H_t-\frac1{16}.
\tag{ER19}
\]

For an independent check of its sign, write \(r(u)=8e^u\psi(e^{4u})\). ESH9 gives \(r'(0)=-4\), and ESH10 gives \((r''-r)/64=\Phi\). The two full integrations by parts give
\(\int_0^\infty e^{tu^2}r''\cos(Zu)\,du=-r'(0)-(Z-2t\partial_Z)^2L_t\); these integrals converge for this theta-only r even at positive t. Thus \(64H_t=4+64\mathcal N_tL_t\), which is ER19. No endpoint term was dropped.

In the algebraic quotient \(\mathcal S'/\mathcal N_t\mathcal S'\), it follows that

\[
\boxed{[H_t]=[1/16]\ne0.}
\tag{ER20}
\]

Directly, \(\ell_\varepsilon(1/16)=G_t(\varepsilon/(2t))/16\), giving exactly ER12. ER19 proves equality of the quotient classes, stronger than merely observing equal moments. A theorem identifying the whole range on all of \(\mathcal S'\) is unnecessary for ER16 and ER20 and is not assumed here.

## ER5. All distribution solutions on the larger local domain

Multiplication by every smooth function is defined on \(\mathcal D'\). For any \(I\in\mathcal D'\), put \(g=e^{-Q}I\) there. The full product rule proves

\[
\mathcal N_t I=-\frac{e^Q}{64}(g+4t^2g''),
\qquad
\mathcal N_t I=H_t
\Longleftrightarrow
g''+k^2g=-\frac{16}{t^2}e^{-Q}H_t
\quad\text{in }\mathcal D'.
\tag{ER21}
\]

This is an exact identity of differential operators on the stated domain. No claim that multiplication by \(e^Q\) preserves \(\mathcal S'\) is used.

Here is the distribution kernel proof. If a distribution V satisfies \(V'=0\), then V is constant: a compactly supported smooth test of integral zero is the derivative of its compactly supported smooth indefinite integral, and V vanishes on every such derivative; subtracting a fixed unit-integral test proves the constant formula on all tests. It follows by multiplying by \(e^{-\lambda Z}\) that \((D-\lambda)V=0\) has exactly the solutions \(a e^{\lambda Z}\). If \((D^2+k^2)w=0\), put \(v=(D+ik)w\). Then \((D-ik)v=0\), hence \(v=a e^{ikZ}\). Multiplication by \(e^{ikZ}\) and one distributional integration give

\[
w=\frac{a}{2ik}e^{ikZ}+b e^{-ikZ}.
\tag{ER22}
\]

The ESH lateral functions \(I_\pm\) are entire in Z and satisfy \(\mathcal N_tI_\pm=H_t\). Subtract one of these particular solutions and apply ER21–22. Thus **every** \(\mathcal D'\) solution is the regular distribution of an entire function, and its complete form is

\[
I=I_+(t,Z)+e^{Z^2/(4t)}
                   (a e^{iZ/(2t)}+b e^{-iZ/(2t)}),
\qquad a,b\in\mathbb C.
\tag{ER23}
\]

The even solutions are exactly those with a=b, because \(I_+\) is even. None of ER23 is tempered, by ER16.

For later use the homogeneous kernel on \(\mathcal S'\) is zero. To prove this without a pointwise-growth shortcut, let \(p(Z)=a e^{ikZ}+b e^{-ikZ}\ne0\), whose period is \(T=4\pi t\). Choose a nonnegative compactly supported smooth \(\chi\) with \(\int\chi(y)|p(y)|^2dy>0\), and put \(\varphi_n(Z)=\chi(Z-nT)\overline{p(Z-nT)}\). Every Schwartz seminorm of \(\varphi_n\) grows at most polynomially in n. On the other hand the pairing of the regular distribution \(e^Qp\) with this test is

\[
\int e^{(nT+y)^2/(4t)}\chi(y)|p(y)|^2\,dy.
\tag{ER24}
\]

If the support lies in [−R,R], this is bounded below for sufficiently large n by \(e^{(nT-R)^2/(4t)}\int\chi|p|^2\), which grows faster than any polynomial. Such a functional is not continuous on \(\mathcal S\). Therefore \(e^Qp\notin\mathcal S'\), and the homogeneous tempered kernel is indeed zero.

## ER6. Exact Wronskian identity, including the original differential boundary

For any of the solutions ER23 and ε∈{+1,−1}, define

\[
\begin{split}
W_\varepsilon[I](Z)
&=e^{\varepsilon ikZ}\bigl[g'(Z)-\varepsilon ikg(Z)\bigr]\\
&=e^{-Z^2/(4t)}e^{\varepsilon iZ/(2t)}
 \left[I'(Z)-\left(\frac Z{2t}+\frac{\varepsilon i}{2t}\right)I(Z)\right].
\end{split}\tag{ER25}
\]

Differentiating the first line and using ER21 gives

\[
W_\varepsilon[I]'(Z)
 =-\frac{16}{t^2}\psi_\varepsilon(Z)H_t(Z).
\tag{ER26}
\]

In the original polynomial differential expression, the complete Green boundary on a finite interval [a,b] is

\[
\begin{split}
&\int_a^b\bigl[\psi_\varepsilon\mathcal N_t I
                  -I\mathcal N_t^{\mathrm T}\psi_\varepsilon\bigr]dZ\\
&\qquad=-\frac{t^2}{16}
 \left[\psi_\varepsilon I'-\psi_\varepsilon'I
                  -\frac Zt\psi_\varepsilon I\right]_a^b
 =-\frac{t^2}{16}[W_\varepsilon[I]]_a^b.
\end{split}\tag{ER27}
\]

This follows by integrating the second derivative twice and the drift term \(tZI'/16\) once. Its drift contribution is the displayed \(-Z\psi_\varepsilon I/t\) inside the bracket. Inserting \(\psi_\varepsilon'=(-Z/(2t)+\varepsilon i/(2t))\psi_\varepsilon\) gives ER25 exactly.

ER3 implies that the right side of ER26 is absolutely integrable on the real line. Hence the two limits \(W_\varepsilon[I](\pm\infty)\) exist, and ER12 proves the invariant boundary difference

\[
\boxed{
W_\varepsilon[I](+\infty)-W_\varepsilon[I](-\infty)
 =-\frac{16}{t^2}\ell_\varepsilon(H_t)
 =-2\sqrt\pi\,t^{-3/2}e^{-1/(4t)}
 =-\frac{2c_t}{t}.}
\tag{ER28}
\]

Adding a homogeneous term in ER23 changes the two endpoint values by the same constant. Specifically \(e^{ikZ}\) contributes \(2ik\) to \(W_-\) and zero to \(W_+\); \(e^{-ikZ}\) contributes \(-2ik\) to \(W_+\) and zero to \(W_-\). Thus ER28 is independent of every choice of homogeneous coefficients, while the separate endpoint values remember that choice.

## ER7. Lateral asymptotics and all four Wronskian endpoint values

The branch conventions of ESH3–6 are

\[
F_+(t,a)=-\frac{i}{2}\sqrt{\frac\pi t}
 e^{-a^2/(4t)}\operatorname{erfc}\!\left(\frac{a}{2i\sqrt t}\right),
\quad
B_\pm(t,Z)=\tfrac12[F_\pm(t,1-iZ)+F_\pm(t,1+iZ)],
\quad I_\pm=L_t-4B_\pm.
\tag{ER29}
\]

The upper sign means approach to q=−t from the upper q-half-plane. Substituting both original endpoint factors \(1-iZ\) and \(1+iZ\) into ER29 gives

\[
\begin{split}
g_+(Z):=e^{-Q}I_+(t,Z)
 &=e^{-Q}L_t(Z)\\
 &\quad+i c_t\left[
 e^{ikZ}\operatorname{erfc}\!\left(-\frac{Z+i}{2\sqrt t}\right)
 +e^{-ikZ}\operatorname{erfc}\!\left(\frac{Z-i}{2\sqrt t}\right)
 \right].
\end{split}\tag{ER30}
\]

These signs follow directly from \(1/(i\sqrt t)=-i/\sqrt t\) and \((1\mp iZ)^2=1\mp2iZ-Z^2\). The exact jump ESH6 is

\[
g_+(Z)-g_-(Z)=4ic_t\cos(kZ)
              =2ic_t(e^{ikZ}+e^{-ikZ}).
\tag{ER31}
\]

To justify all limits without relying on a sector asymptotic shorthand, for x>0 and fixed real y the horizontal integral for erfc satisfies

\[
\begin{split}
\operatorname{erfc}(x+iy)
 &=\frac2{\sqrt\pi}\int_x^\infty e^{-(v+iy)^2}\,dv,\\
|\operatorname{erfc}(x+iy)|
 &\le\frac{e^{y^2-x^2}}{\sqrt\pi x}.
\end{split}\tag{ER32}
\]

The first equality follows from the entire primitive: integrate to a real R through the horizontal segment and a vertical segment at R; the latter integral tends to zero because its length is |y| and its integrand is bounded by \(e^{-R^2+y^2}\). The bound follows from \(\int_x^\infty e^{-v^2}dv\le e^{-x^2}/(2x)\). The derivative formula \(\operatorname{erfc}'(z)=-2e^{-z^2}/\sqrt\pi\) gives the corresponding Gaussian bound on its derivative. For the negative direction use the exact identity \(\operatorname{erfc}(-z)=2-\operatorname{erfc}(z)\).

Since \(L_t,L_t'\) are bounded, \(e^{-Q}L_t\) and its derivative tend to zero at both real infinities. Equations ER30–32 therefore yield

\[
\begin{array}{c|cc}
 &Z\to+\infty&Z\to-\infty\\\hline
g_+(Z)&2ic_t e^{ikZ}+r_{+,+}(Z)&2ic_t e^{-ikZ}+r_{+,-}(Z)\\
g_-(Z)&-2ic_t e^{-ikZ}+r_{-,+}(Z)&-2ic_t e^{ikZ}+r_{-,-}(Z),
\end{array}\tag{ER33}
\]

where each remainder and its first derivative tends to zero at its stated end. The bounds just proved are enough even after the first derivative differentiates the linear erfc argument or the bounded oscillatory exponential. Using ER25 on each exponential in ER33 gives the exact table

\[
\begin{array}{c|cc|cc}
 &W_+(-\infty)&W_+(+\infty)
 &W_-(-\infty)&W_-(+\infty)\\\hline
I_+&2c_t/t&0&0&-2c_t/t\\
I_-&0&-2c_t/t&2c_t/t&0.
\end{array}\tag{ER34}
\]

Every difference in this table is exactly ER28. This proves the precise boundary relation between the resonant moments and the specified lateral continuations, including the sign determined by the q-plane convention.

## ER8. The median endpoint and jump are independent modulo tempered distributions

Define, retaining the endpoint density coefficient from ESH1,

\[
B_{\mathrm{med}}=\frac{B_++B_-}{2},\qquad
I_{\mathrm{med}}=L_t-4B_{\mathrm{med}},\qquad
J_t(Z)=e^{(Z^2-1)/(4t)}\cos\!\left(\frac Z{2t}\right).
\tag{ER35}
\]

The exact relations are

\[
\mathcal N_tB_{\mathrm{med}}=-\frac1{64},\qquad
\mathcal N_tJ_t=0,\qquad
I_+-I_-=4i\sqrt{\frac\pi t}\,J_t.
\tag{ER36}
\]

For the first relation, the original endpoint density is \(e^{-u}\), so its derivative at zero is −1 and its second derivative equals itself. The full ESH8 integration formula gives \(\mathcal N_tB=-1/64\) for negative time, followed by the specified analytic continuation to each lateral value. The second follows by substitution into ER21. The third is ER31 with \(c_t\) expanded.

The erfc bounds in ER32 give the stronger unweighted endpoint asymptotics

\[
B_{\mathrm{med}}(t,Z)=
\begin{cases}
 \frac{c_t}{2}e^{Z^2/(4t)}\sin(Z/(2t))+O(1/Z),& Z\to+\infty,\\
 -\frac{c_t}{2}e^{Z^2/(4t)}\sin(Z/(2t))+O(1/|Z|),& Z\to-\infty.
\end{cases}\tag{ER37}
\]

To see the constants, ER33 and \(I_\pm=L_t-4B_\pm\) give at positive infinity the median coefficient \((ic_t/4)(e^{-ikZ}-e^{ikZ})=(c_t/2)\sin(kZ)\), with the opposite sign at negative infinity. To obtain the stated O-bound one uses ER29–32 directly on B: each erfc remainder after multiplication by \(e^Q\) has modulus at most a t-dependent constant divided by |Z|. There is no \(L_t\) contribution to B.

The classes of \(B_{\mathrm{med}}\) and \(J_t\) in the algebraic quotient \(\mathcal D'/\mathcal S'\) are linearly independent. Indeed, suppose
\(aB_{\mathrm{med}}+bJ_t\in\mathcal S'\). Applying \(\mathcal N_t\) and ER36 gives the tempered distribution −a/64. ER15 forces

\[
0=-\frac a{64}\ell_\varepsilon(1)
 =-\frac a{64}\,2\sqrt{\pi t}\,e^{-1/(4t)},
\tag{ER38}
\]

so a=0. Then \(bJ_t\in\mathcal S'\); the translated-test proof ER24 applied to the nonzero cosine implies b=0. In particular each of these two nonzero classes must be retained in any direct enlargement by these directions. This argument does not infer independence merely from different informal growth descriptions.

For reference, the median Wronskians for \(I_{\mathrm{med}}\) are

\[
W_\pm[I_{\mathrm{med}}](-\infty)=c_t/t,
\qquad
W_\pm[I_{\mathrm{med}}](+\infty)=-c_t/t.
\tag{ER39}
\]

For \(B_{\mathrm{med}}\) the values are respectively \(-c_t/(4t)\) and \(c_t/(4t)\); for \(J_t\), \(W_+[J_t]=-i e^{-1/(4t)}/(2t)\) and \(W_-[J_t]=i e^{-1/(4t)}/(2t)\), constant at both ends. These values follow by linearity from ER34, the vanishing Wronskian limits of \(L_t\), and the exact exponential formula for \(J_t\).

## ER9. The same boundary functional with the complete original Gamma receiver

Keep the exact original coordinate and original multiplier

\[
s=\tfrac12+\tfrac{iZ}{2},\qquad
A(s)=\pi^{-s/2}\Gamma(s/2),\qquad
f_\pm(t,s)=\frac{I_\pm(t,-2i(s-1/2))}{A(s)}.
\tag{ER40}
\]

On the line \(\Re s=1/2\), A is holomorphic and nonzero. Since \(\partial_Z=(i/2)\partial_s\), ER25 is exactly

\[
\begin{split}
W_\varepsilon[I_\pm]
&=\exp\!\left(\frac{(s-\tfrac12)^2+
                  \varepsilon(s-\tfrac12)}t\right)\\
&\quad\times\left\{
 \frac i2\left[A'(s)f_\pm(t,s)+A(s)\partial_sf_\pm(t,s)\right]
 +\frac it\left(s-\frac{1+\varepsilon}{2}\right)
               A(s)f_\pm(t,s)\right\}.
\end{split}\tag{ER41}
\]

The complete first multiplier derivative here is

\[
A'(s)=\pi^{-s/2}\Gamma(s/2)
 \left[-\frac12\log\pi+\frac12\psi_\Gamma(s/2)\right],
\tag{ER42}
\]

with \(\psi_\Gamma\) the Gamma logarithmic derivative, distinct from the theta sum in ER18. Thus the same real-axis boundary is expressed on the actual arithmetic vertical line with both the Gamma and the power-of-pi contributions retained. The separate endpoint modes remain exactly

\[
f_+(t,s)-f_-(t,s)
=2i\sqrt{\frac\pi t}\,
  \frac{\pi^{s/2}}{\Gamma(s/2)}
       \left[e^{-s^2/t}+e^{-(s-1)^2/t}\right].
\tag{ER43}
\]

This is obtained by substituting the original coordinate into ER36; neither endpoint exponential is omitted. The nonzero boundary source in ER28 and the quotient representative in ER20 are fixed by the original residue calculation ER5–7. This calculation concerns the exact domains and receiving maps of the specified heat construction and supplies no statement about the location of zeta zeros.

## Bounded mathematical comparison with the companion derivation

The companion file `ENDPOINT_RESONANCE_AND_PRIME_CLASS.tex` was read and its formulas ER12–18 and ER31–33 were checked against the independent calculation above on 2026-09-23. No error in their signs, constants, or stated domains was found in those checked ranges. This is a bounded mathematical check, not a claim about unchecked external source coverage.

For its Schwartz inverse, the particular solution of
\(g''+(1/(4t^2))g=-(16/t^2)e^{-Z^2/(4t)}h\) is

\[
g(Z)=-\frac{32}{t}\int_{-\infty}^Z
 \sin((Z-y)/(2t))e^{-y^2/(4t)}h(y)\,dy.
\]

The first derivative differentiates the sine and the second derivative adds the upper endpoint \(-(16/t^2)e^{-Z^2/(4t)}h(Z)\); all other terms give \(-g/(4t^2)\). If both resonant moments vanish, the whole-line sine integral is zero because it is a fixed linear combination of those two moments. For Z>0, replacing the left integral by minus the right integral and then putting y=Z+v gives a negative coefficient again, since \(\sin(-v/(2t))=-\sin(v/(2t))\). For Z<0, putting y=Z−v in the left integral directly gives that same negative coefficient. Thus the companion's two-tail formula ER15 has the correct sign at both ends. Its differentiated integrands contain derivatives of h times powers of v and the majorant \(e^{-|Z|v/(2t)-v^2/(4t)}\); the estimate
\(\int_0^\infty v^j e^{-|Z|v/(2t)}dv=j!(2t/|Z|)^{j+1}\)
proves every asserted Schwartz seminorm bound. The formulas and the local Gaussian bounds also prove continuity on the bounded middle interval.

With \(\varphi_t=e^{-Z^2/(4t)}\) and \(A_t=\sqrt{2\pi t}e^{-1/(8t)}\), direct differentiation of
\(\int e^{-Z^2/(2t)}e^{iaZ}dZ=\sqrt{2\pi t}e^{-ta^2/2}\)
gives
\(\ell_\pm(\varphi_t)=A_t\) and
\(\ell_\pm(Z\varphi_t)=\pm iA_t/2\).
Hence the companion's ER17 section is onto, and the ER18 coefficient is exactly

\[
\frac{\ell_\pm(H_t)}{A_t}
 =\frac{\sqrt{\pi t}e^{-1/(4t)}/8}
        {\sqrt{2\pi t}e^{-1/(8t)}}
 =\frac{e^{-1/(8t)}}{8\sqrt2}.
\]

Finally let \(w=s-1/2\). For every complex w, direct Gaussian integration against both terms of \(\cos(Zu)\) gives

\[
\begin{split}
&\int_{\mathbb R}e^{-Z^2/(4t)}e^{-wZ}\cos(Zu)\,dZ\\
&\qquad=\sqrt{\pi t}\left[e^{t(-w+iu)^2}+e^{t(-w-iu)^2}\right]
 =2\sqrt{\pi t}\,e^{tw^2-tu^2}\cos(2twu).
\end{split}
\]

The absolute bound is the product of
\(\int e^{-Z^2/(4t)+|\Re w||Z|}dZ<\infty\)
and \(\int_0^\infty e^{tu^2}\Phi(u)du<\infty\), so interchange is valid for every such w. Multiplying by the retained original density gives precisely the companion's ER32. Multiplication by the separate cosine \(\cos(Z/(2t))\) shifts w to \(w-i/(2t)\) and \(w+i/(2t)\), producing ER31 with its coefficient \(\sqrt{\pi t}\). Under the original coordinate comparison ER5, the two arguments
\(2tw-i\) and \(2tw+i\) receive respectively
\(s'=1+itw\) and \(s'=itw\). Thus the two full products in the companion's ER33 are in the correct order, with exactly the factor 1/16. At w=0 their full exceptional products are both 1 by ER5–7, and the two terms give \(\sqrt{\pi t}e^{-1/(4t)}/8\), agreeing with the independently evaluated moments ER12.
