# The complete Cauchy–Weil matrix criterion

<!-- original-zeta-reconstruction-start -->
**Original-zeta receiving calculation.** The working meromorphic function is the original Riemann zeta, with its full Gamma/endpoints multiplier and its full trivial-zero and pole divisor retained. [TF1–42](FAITHFUL_THETA_COMPLETION_RETURN.md) proves the original labelled theta inverse and the actual heat-image defect. [UZ1–53](FAITHFUL_UNCOMPLETED_ZETA_HEAT.md) proves every exceptional-point fibre, jet, original-zeta heat term and reflection orientation. [OZC1–48](ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md) rederives the compact contour and interval operator directly from zeta, including the left-cutoff Gamma boundary, and specifies exactly which compensated pairing the bounds concern. [OZH1–49](ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION.md) rederives the actual meromorphic heat, rational signed trace, compact-test domain, contact drift and full causal arithmetic variation. The raw full divisor and the compensated Weil receiver are linked by their displayed correction, not identified. In particular the fixed-test trivial-zero sum converges exactly at translations at least 1/32 and equals the earlier R term; at zero translation it requires the proved cutoff compensation. [OZK1–38](ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md) reconstructs the original signed Cauchy trace, its full Gamma correction, resonant finite parts, every finite matrix and its index, and the complete local heat jets. Its invertible map retains the raw trace and correction separately. These complete receiving proofs govern the interpretation of the retained auxiliary calculations below.
<!-- original-zeta-reconstruction-end -->


This note proves an equivalence with the classical Riemann hypothesis. It does not assume or establish positivity of the matrices occurring in that equivalence. The full supported-zero arithmetic evaluation of those matrices is [HA10–HA20](HEAT_CAUCHY_ARITHMETIC_DERIVATION.md); every endpoint and lower support coordinate remains there.

## 1. The original kernel and zero sum

Put \(g=2\xi_R\), \(L=g'/g\), and \(\mathcal U=\{z:\Re z>1\}\). Define
\[
K(z,w)=\frac{L(w)+\overline{L(z)}}{w+\bar z-1},\qquad z,w\in\mathcal U.
\tag{CK1}
\]
The unconditional Euler product and functional equation imply that \(g\) is nonzero on \(\mathcal U\), so this definition requires no RH assumption. The exact global trace identity AG10–AG11 is
\[
K(z,w)=\sum_\rho m_\rho
\overline{F_z(\rho^\#)}F_w(\rho),\qquad
F_z(s)=\frac1{s-z},\quad\rho^\#=1-\bar\rho.
\tag{CK2}
\]
The sum converges absolutely and keeps all multiplicities. The reflection and Hadamard proof, with the zero count, is given in [AG1–AG11](ACTUAL_HEAT_ZERO_DISTRIBUTION_VARIATION.md).

A kernel is positive semidefinite on a set when, for every integer \(n\ge1\), every finite tuple of points in that set, and every \(c\in\mathbb C^n\), its quadratic sum \(\sum_{i,j}\bar c_iK(z_i,z_j)c_j\) is nonnegative. Under RH each \(\rho^\#=\rho\), so (CK2) gives
\[
\sum_{i,j}\bar c_iK(z_i,z_j)c_j
=\sum_\rho m_\rho\left|\sum_j c_jF_{z_j}(\rho)\right|^2\ge0.
\tag{CK3}
\]
This proves one direction. The converse is proved completely below, including the extension of a kernel known only on the observed subdomain.

## 2. A self-contained Schur extension from a positive kernel

The positive-kernel Hilbert construction and the transfer-function realization used in this section are classical. A primary-source treatment is Joseph A. Ball, Animikh Biswas, Quanlei Fang and Sanne ter Horst, *Multivariable generalizations of the Schur class: positive kernel characterization and transfer function realization*, [arXiv:0705.2042v3](https://arxiv.org/abs/0705.2042v3), §1, Theorem 1.1(2)–(3) and Proposition 1.2. Their proof discussion of Theorem 1.1, (2) ⇒ (3), identifies the equal-Gram construction as the standard lurking-isometry argument. The source orders its Hilbert sum as \(\mathcal H\oplus\mathbb C\), whereas CK5–CK7 use \(\mathbb C\oplus\mathcal H\). The unitary swap \(J(\alpha,h)=(h,\alpha)\) sends \(V=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) to \(JVJ^{-1}=\left(\begin{smallmatrix}d&c\\b&a\end{smallmatrix}\right)\). Thus the source's blocks are \((A,B,C,D)=(d,c,b,a)\), and its transfer formula \(D+zC(I-zA)^{-1}B\) is exactly CK7. In the scalar case its kernel \(K_f(y,x)\) is CK4's \(S(x,y)\), retaining the conjugate-linear-first convention. The cited theorem is stated on the full disc; the arbitrary-subset extension needed here is proved directly below, rather than asserted to be an additional theorem read in that source.

Let \(E\) be any nonempty subset of the unit disc, and let \(f:E\to\mathbb C\) satisfy positivity of
\[
S(x,y)=\frac{1-\overline{f(x)}f(y)}{1-\bar x y}.
\tag{CK4}
\]
We construct a holomorphic function \(\widetilde f\) on the whole unit disc, of modulus at most one, agreeing with \(f\) on \(E\). First construct a Hilbert space \(\mathcal H\) from formal vectors \(v_x\), setting \(\langle v_x,v_y\rangle=S(x,y)\), with the inner product conjugate-linear in its first variable. On finite linear combinations this is a nonnegative sesquilinear form. Cauchy–Schwarz for such a form follows from positivity of the quadratic polynomial in a complex scalar; consequently its zero-length vectors form its radical. Quotient by this radical and complete to obtain \(\mathcal H\).

The identity in (CK4) gives equal Gram matrices for the following two families in \(\mathbb C\oplus\mathcal H\):
\[
\begin{pmatrix}1\\xv_x\end{pmatrix}
\longmapsto
\begin{pmatrix}f(x)\\v_x\end{pmatrix},
\qquad
1+\bar x yS(x,y)=\overline{f(x)}f(y)+S(x,y).
\tag{CK5}
\]
The rule therefore defines a well-defined isometry on their algebraic span and extends to its closure \(\mathcal M\). Extend it to a contraction \(V\) on \(\mathbb C\oplus\mathcal H\) by setting it equal to zero on \(\mathcal M^\perp\). Write its bounded blocks as
\[
V=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad \|V\|\le1.
\tag{CK6}
\]
Here \(a\in\mathbb C\), \(b:\mathcal H\to\mathbb C\), \(c:\mathbb C\to\mathcal H\) is identified with \(c(1)\), and \(d:\mathcal H\to\mathcal H\). Equation (CK5) says
\(a+xbv_x=f(x)\) and \(c+xdv_x=v_x\). Since \(\|d\|\le1\), the Neumann series makes \(I-zd\) invertible for every \(|z|<1\). Define
\[
h(z)=(I-zd)^{-1}c,\qquad
\widetilde f(z)=a+zb(I-zd)^{-1}c.
\tag{CK7}
\]
The series makes both holomorphic and gives \(h(x)=v_x\), \(\widetilde f(x)=f(x)\). Moreover
\(V(1,zh(z))=(\widetilde f(z),h(z))\). Contractivity yields
\[
|\widetilde f(z)|^2+\|h(z)\|^2
\le1+|z|^2\|h(z)\|^2,
\quad
1-|\widetilde f(z)|^2\ge(1-|z|^2)\|h(z)\|^2\ge0.
\tag{CK8}
\]
This proves the required extension without invoking an unproved interpolation theorem. It is the classical Schur transfer construction, with its spaces and maps specified here; no novelty claim for the construction is made.

## 3. Positive Cauchy matrices exclude every zero off the line

Write \(v=s-1/2\). The half-plane \(\Re s>1/2\) is carried bijectively to the unit disc by
\[
x=\frac{v-1}{v+1}=\frac{s-3/2}{s+1/2},\qquad
s=\frac12+\frac{1+x}{1-x}.
\tag{CK9}
\]
Let \(U\) be any nonempty open subset of \(\mathcal U\) on which \(K\) is positive semidefinite. Its diagonal gives
\(2\Re L(s)/(2\Re s-1)\ge0\), hence \(\Re L(s)\ge0\) on \(U\). In particular \(L(s)+1\ne0\). Put
\[
f(x)=\frac{L(s)-1}{L(s)+1},\qquad x=x(s),\ s\in U.
\tag{CK10}
\]
The exact kernel transformation is
\[
\frac{1-\overline{f(x(z))}f(x(w))}{1-\overline{x(z)}x(w)}
=\overline{a(z)}K(z,w)a(w),\quad
a(s)=\frac{s+1/2}{L(s)+1}.
\tag{CK11}
\]
Indeed the numerator before division is \(2(\overline{L(z)}+L(w))/((\overline{L(z)}+1)(L(w)+1))\); the disc denominator is \(2(w+\bar z-1)/((\bar z+1/2)(w+1/2))\). Their quotient gives (CK11) exactly. A diagonal congruence preserves kernel positivity. Section 2 therefore extends \(f\) to a Schur function \(\widetilde f\) on the whole unit disc.

The extended function cannot take the value 1 inside the disc. Otherwise the maximum modulus principle makes it identically 1, contradicting (CK10) at any point of \(U\). Thus
\[
\widetilde L(s)=\frac{1+\widetilde f(x(s))}{1-\widetilde f(x(s))}
\tag{CK12}
\]
is holomorphic on \(\Re s>1/2\) and equals the original \(L\) on \(U\). The holomorphic function \(g'-\widetilde Lg\) on this connected half-plane vanishes on \(U\), so the identity theorem makes it zero throughout. If \(g\) had a zero \(\rho\) of positive multiplicity \(m\) there, then \(g'\) would have order \(m-1\) at \(\rho\), while \(\widetilde Lg\) has order at least \(m\). This contradicts the identity. Hence \(g\) has no zeros in \(\Re s>1/2\). The functional equation \(g(1-s)=g(s)\) excludes zeros in \(\Re s<1/2\) as well. Its zeros are exactly the nontrivial zeta zeros, proving RH.

Together with (CK3) this proves the exact equivalence
\[
\boxed{\begin{aligned}
\mathrm{RH}&\Longleftrightarrow K\text{ is positive semidefinite on }\mathcal U\\
&\Longleftrightarrow K\text{ is positive semidefinite on }U.
\end{aligned}}
\tag{CK13}
\]
The last phrase means that for each fixed such \(U\), its complete positivity condition is equivalent to RH. It does not replace all finite matrices by a single diagonal inequality.

## 4. One real point, with every Taylor coefficient retained

Fix a real \(\sigma>1\), write \(d=2\sigma-1\), and set \(\ell_n=L^{(n)}(\sigma)/n!\). All \(\ell_n\) are real. Define the infinite Hermitian coefficient matrix
\[
C_{jk}=[X^jY^k]\frac{L(\sigma+X)+L(\sigma+Y)}{d+X+Y},\qquad j,k\ge0.
\tag{CK14}
\]
The bracket denotes the convergent Taylor expansion near \(X=Y=0\), not a truncation of the underlying function. Expanding the denominator geometrically gives the explicit coefficients
\[
\begin{aligned}
C_{jk}={}&\sum_{n=0}^j
\ell_n\frac{(-1)^{j+k-n}\binom{j+k-n}{k}}{d^{j+k-n+1}}\\
&+\sum_{n=0}^k
\ell_n\frac{(-1)^{j+k-n}\binom{j+k-n}{j}}{d^{j+k-n+1}}.
\end{aligned}\tag{CK15}
\]
In particular, \(\ell_0\) occurs twice, as it must in the numerator of (CK14).

The entries are exactly the original rational-jet pairings
\[
C_{jk}=Z_0\!\left((Q_j)^\#Q_k\right),\qquad
Q_j(s)=\frac1{(s-\sigma)^{j+1}}.
\tag{CK16}
\]
To verify this, \(F_{\sigma+Y}(s)=\sum_{k\ge0}Y^k/(s-\sigma)^{k+1}\) on any sufficiently small parameter disc at each zero. The analogous reflected expansion uses \(X\). Derivatives may be taken in (CK2) locally: its large-zero tail, and every parameter derivative of that tail, are uniformly summable by the \(O(|\rho|^{-2})\) bound and the fixed distance of the poles from the critical strip. The finitely many remaining terms are analytic. Coefficient comparison now gives (CK16), with no missing factorial.

We prove the complete single-point criterion:
\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
(C_{jk})_{0\le j,k\le N}\succeq0\text{ for every integer }N\ge0.}
\tag{CK17}
\]
Under RH, (CK16) is a positive Gram matrix by (CK3). Conversely suppose every indicated finite section is positive. Choose a small disc \(|z-\sigma|<r\) contained in \(\mathcal U\), on whose product the double Taylor series in (CK14) converges absolutely. For finitely many points \(z_i\) in a smaller such disc and coefficients \(b_i\), put \(v_j=\sum_i b_i(z_i-\sigma)^j\). Positivity of the finite sections gives
\(\sum_{j,k=0}^N\bar v_jC_{jk}v_k\ge0\). Absolute convergence allows \(N\to\infty\), yielding \(\sum_{i,l}\bar b_iK(z_i,z_l)b_l\ge0\). Thus \(K\) is positive on a nonempty open disc, and (CK13) proves RH. This keeps the entire coefficient tower; no finite \(N\) is claimed sufficient.

The first two-by-two section retains a useful exact determinant:
\[
\begin{pmatrix}C_{00}&C_{01}\\C_{10}&C_{11}\end{pmatrix}
=\begin{pmatrix}
2\ell_0/d&\ell_1/d-2\ell_0/d^2\\
\ell_1/d-2\ell_0/d^2&-2\ell_1/d^2+4\ell_0/d^3
\end{pmatrix},\qquad
\det=\frac{4\ell_0^2-d^2\ell_1^2}{d^4}.
\tag{CK18}
\]
This follows by expanding the displayed determinant; no derivative of order two enters this particular mixed coefficient. Higher sections do retain higher derivatives through (CK15).

## 5. The actual heat response of the whole coefficient tower

Let \(L_t=g_t'/g_t\) for the original heat family. At the fixed real \(\sigma>1\), the positive integral makes \(g_t(\sigma)>0\) for every real time. Define \(C_{jk}(t)\) by the same local Taylor formula as (CK14). For each fixed time and each finite coefficient set the function is holomorphic on a time disc; the proof is AG1–AG11. Therefore
\[
\left.\partial_t^k C_{ij}(t)\right|_0
=[X^iY^j]\frac{B_k(L_0,L_0',\ldots)(\sigma+X)
+B_k(L_0,L_0',\ldots)(\sigma+Y)}{d+X+Y},
\tag{CK19}
\]
where the full recurrence and all mixed-prime coefficients are proved in [HM1–HM13](HEAT_MIXED_PRIME_RECURRENCE.md). Equation (CK19) is the exact map from the arithmetic heat derivative to the complete positivity tower. The rational tests in (CK16) carry the supported endpoints and lower fixed coordinates of SZW through AG16; no coordinate of that identity is removed to define the tower.

HA24–HA26 proves that \(C_{00}(t)>0\) and \(\partial_tC_{00}(t)>0\) for every real time, including negative times when the actual heat function has nonreal zeros. Thus positivity of that one entry is a proved property with a strictly smaller scope than (CK17). The remaining matrix entries and their exact response (CK19) are concrete mathematical data retained by the criterion.

## Method and sources

The transfer construction CK4–CK8 is a complete proof of the classical Schur/Pick extension method used here, rather than an appeal to an unstated interpolation hypothesis. Jensen, Hadamard and the original zeta facts required by CK1–CK3 are proved or invoked with verified hypotheses in AG and SZW. The original human explicit-formula source remains Alain Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Appendix II Theorem 6, as read and applied in [SZW19–SZW38](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3c022a0adde0a6aa3d8fc8e43ef42795d88e44b0/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md). Rodgers–Tao's original heat coordinates, source locators and archive are retained in AG and HA. No historical novelty claim for equivalent RH criteria or classical transfer methods is made. The exact in-programme contribution is the complete supported arithmetic and original-heat maps into this specified matrix family.


Ball, Joseph A.; Biswas, Animikh; Fang, Quanlei; ter Horst, Sanne. *Multivariable generalizations of the Schur class: positive kernel characterization and transfer function realization*. arXiv:0705.2042v3, 2 November 2007. https://arxiv.org/abs/0705.2042v3 . Original author TeX inspected, §1, Theorem 1.1, Proposition 1.2 and the proof discussion through (2) ⇒ (3).

The inspected treatment attributes the scalar positive-kernel Hilbert-space construction to N. Aronszajn, *Theory of reproducing kernels*, Transactions of the American Mathematical Society 68 (1950), 337–404. It cites J. A. Ball, *Linear systems, operator model theory and scattering: multivariable generalizations*, in *Operator Theory and Its Applications (Winnipeg, MB, 1998)*, Fields Institute Communications 25, American Mathematical Society, 2000, 151–178, for the lurking-isometry terminology. These two original works were not inspected for this repair; this historical attribution is through the inspected Ball–Biswas–Fang–ter Horst source. No historical novelty for these classical methods is claimed.

## One fixed primitive test and the entire prime window

The [prime-operator calculation](PRIME_PROJECTOR_MOBIUS_DERIVATION.md), PM1–41, proves both distinct Fourier support corrections and their exact map into the full Weil formula. The [local estimate](PRIMITIVE_SHORT_SUPPORT_DERIVATION.md), PS1–21, gives a positive translation-difference remainder. The [fixed-test proof](UNIVERSAL_PRIMITIVE_TRANSLATION_CRITERION.md), UP1–35, constructs one compact test whose transform is nonzero at every possible off-critical zero. The [complete arithmetic calculation](PRIMITIVE_PRIME_WINDOW_DERIVATION.md), PW1–22, expresses its entire translated correlation through a fixed-width prime window and an explicit archimedean remainder. Its boundedness is equivalent to RH; that bound remains unresolved. All boundary coordinates and supported-zero labels remain explicit.


## Original-zeta Gaussian and affine receiving maps

The complete extension OZG1–55 proves that Gaussian convolution of the test at every positive time makes the original trivial-zero scalar sum diverge for every real translation. Its admissible replacement retains each cutoff trace and the Gamma boundary with the identical finite sum U_N; OZG20–27 gives both maps and the inverse. The full coefficient tower, its raw non-Hermitian correction and exact compensated negative index are OZG28–39. No compact-support prime window is assumed after smoothing; all prime powers and Gamma terms, with explicit error bounds, are OZG40–52. This extension acts on the tests while fixing the original zeta zeros.

The different affine change of the actual original heat family is OZR1–36. Its multiplier is exp(chi) C(phi)/C, with the full inverse, exceptional units and local jets. The original generator contains every q derivative term. The signed divisor comparison is OZR19–24; its Cauchy logarithmic kernel has an additional growth contribution 2a. OZR33 proves the exact full negative index after that contribution is retained. The full support carrier and every lower coordinate are OZG53–55 and OZR34–36. These are the receiving maps for these specified extensions; the original preceding test, time and domains remain those stated in its proof.
