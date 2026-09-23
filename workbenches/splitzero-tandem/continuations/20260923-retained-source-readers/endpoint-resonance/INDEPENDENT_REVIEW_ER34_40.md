# Independent mathematical review of ER34–40

Date: 2026-09-23. Scope: the extension ER34–40 in `ENDPOINT_RESONANCE_AND_PRIME_CLASS.tex`, checked against the independent theta-resonance calculation in `INDEPENDENT_RESONANCE.md` and the established original-zeta conventions in `ORIGINAL_ZETA_GAUSSIAN_TRANSLATION_RECONSTRUCTION.md`, specifically OZG1–5, OZG20–27 and OZG40–41. The latter is retained locally under `work/identity_absorber_exploration_20260919/receivers/`. Its historical directory name does not affect the mathematical source identity of the original-zeta reconstruction being checked.

The review finds no mathematical correction needed in ER34–40. This document gives the actual independent checks, including the distribution sign, the Mellin reflection, and every sign in the finite-cutoff contour. It makes no claim about the sign of the resulting Weil pairing.

## R34. Exact test filter and its inverse on Schwartz space

Throughout, t>0 is real, the original coordinate is Z, and

\[
\begin{split}
H_t(Z)&=\int_0^\infty e^{tu^2}\Phi(u)\cos(Zu)\,du,\\
h_t(Z)&=e^{-Z^2/(4t)}H_t(Z)\cos(Z/(2t)),\\
T&=\partial_Z^2-\tfrac14,\qquad
f_t=Th_t,\qquad
\mathcal Mf(s)=\int_{\mathbb R}f(Z)e^{-(s-1/2)Z}\,dZ.
\end{split}\tag{R1}
\]

No coordinate, time, or factor in this definition is replaced. The original theta bound gives, for every integer j≥0,

\[
\sup_{Z\in\mathbb R}|H_t^{(j)}(Z)|
 \le\int_0^\infty u^je^{tu^2}\Phi(u)\,du<\infty.
\tag{R2}
\]

Consequently every derivative of h_t and f_t is bounded by a fixed polynomial in |Z| times \(e^{-Z^2/(4t)}\), with constants allowed to depend on t and the derivative order. Thus the integrations by parts below are valid for every complex s, with zero boundary at both real infinities. Putting w=s−1/2 gives

\[
\mathcal M(Th_t)(s)
 =(w^2-\tfrac14)\mathcal Mh_t(s)
 =s(s-1)\mathcal Mh_t(s)=F_t(s).
\tag{R3}
\]

Both factors are retained. Since \(\mathcal Mh_t\) is entire by Gaussian domination, R3 evaluates \(F_t(0)=F_t(1)=0\) exactly. These are the weighted moments \(\int f_t(Z)e^{Z/2}dZ\) and \(\int f_t(Z)e^{-Z/2}dZ\), respectively; they do not assert the vanishing of the unweighted moment \(\int f_t\).

The proposed inverse kernel has the correct sign and coefficient:

\[
G(Z)=-e^{-|Z|/2}.
\tag{R4}
\]

For Z≠0 one has \(G''=G/4\). Its one-sided derivatives are \(G'(0+)=1/2\) and \(G'(0-)=-1/2\). A continuous piecewise smooth function contributes its first-derivative jump times δ₀ to its distributional second derivative. That jump is +1, so

\[
(D^2-\tfrac14)G=\delta_0.
\tag{R5}
\]

For any f∈\(\mathcal S(\mathbb R)\), the convolution G*f is Schwartz. To check the precise estimate, write the convolution with variable v=Z−y, move derivatives to f, and use

\[
\begin{split}
&(1+|Z|)^M|(G*f)^{(j)}(Z)|\\
&\quad\le
\int_{\mathbb R}(1+|v|)^M|G(v)|
 (1+|Z-v|)^M|f^{(j)}(Z-v)|\,dv\\
&\quad\le
\left[\int_{\mathbb R}(1+|v|)^Me^{-|v|/2}\,dv\right]
\sup_y(1+|y|)^M|f^{(j)}(y)|.
\end{split}\tag{R6}
\]

The finite bracket proves continuity for every Schwartz seminorm. R5 yields \(T(G*f)=f\). Conversely G*(Tf)=f follows by two integrations by parts in the convolution, equivalently by transferring T from the Schwartz factor to the integrable distribution G and using R5. The only distribution solutions of Tu=0 are \(a e^{Z/2}+b e^{-Z/2}\), by factoring the two distinct first-order operators and applying integrating factors. None of these is nonzero and Schwartz. Thus G* is the two-sided inverse of T on \(\mathcal S\), proving the exact reconstruction

\[
h_t(Z)=-\int_{\mathbb R}e^{-|Z-y|/2}f_t(y)\,dy.
\tag{R7}
\]

For arbitrary Schwartz f the result need not have Gaussian decay. For this actual input f_t, R7 is an equality with the original Gaussian-decaying h_t, because R3 and R5 are exact identities on their stated spaces. No stronger mapping assertion for all Schwartz inputs is required.

## R36. The two original prime-boundary moments

The factor \(q_t(Z)=e^{-Z^2/(4t)}\cos(Z/(2t))\) is even and satisfies

\[
q_t(0)=1,\qquad q_t'(0)=0,\qquad
q_t''(0)=-\frac1{2t}-\frac1{4t^2}.
\tag{R8}
\]

Since H_t is even, differentiating the actual product h_t=q_tH_t and then applying T gives

\[
f_t(0)=H_t''(0)
 -\left(\frac1{2t}+\frac1{4t^2}+\frac14\right)H_t(0).
\tag{R9}
\]

Gaussian decay gives \(\int h_t''=h_t'(+\infty)-h_t'(-\infty)=0\). The independently evaluated resonance gives

\[
\begin{split}
\int_{\mathbb R}h_t(Z)\,dZ
 &=\frac{\sqrt{\pi t}}8e^{-1/(4t)}=:r_t,\\
\int_{\mathbb R}f_t(Z)\,dZ
 &=-\frac14r_t
 =-\frac{\sqrt{\pi t}}{32}e^{-1/(4t)}.
\end{split}\tag{R10}
\]

The complete theta summands satisfy

\[
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}
 =\pi n^2e^{5u}(2\pi n^2e^{4u}-3)e^{-\pi n^2e^{4u}}>0
\]

for u≥0 and n≥1. This equality is used only to evaluate the sign of the original summand; no term is discarded from the density. Therefore

\[
H_t(0)>0,\qquad H_t''(0)
 =-\int_0^\infty u^2e^{tu^2}\Phi(u)\,du<0.
\tag{R11}
\]

R9 and R10 are both strictly negative. Under the existing exact prime receiver \(\beta[(t_p-1)\otimes f]=\ell_p\otimes(f(0),\int f)\), these calculations reproduce every entry and sign in ER36. They are signs of those two moment coordinates only.

## R37. Reflected test convention and the convolution square

The source h_t is real and even on the real line, and T preserves both properties. Define the actual reflection on a general complex source by

\[
f^\#(Z)=\overline{f(-Z)}.
\tag{R12}
\]

Substitution y=−Z proves, with the same centered Mellin measure,

\[
\mathcal M(f^\#)(s)
 =\overline{\mathcal Mf(1-\bar s)}.
\tag{R13}
\]

For the actual f_t one has \(f_t^\#=f_t\), so

\[
\overline{F_t(1-\bar s)}=F_t(s).
\tag{R14}
\]

Also \(F_t(1-s)=F_t(s)\) by evenness and \(F_t(\bar s)=\overline{F_t(s)}\) by reality. Absolute Gaussian integration on \(\mathbb R^2\) proves the convolution identity

\[
k_t=f_t*f_t=f_t*f_t^\#,
\qquad A_t(s)=\mathcal Mk_t(s)=F_t(s)^2.
\tag{R15}
\]

Thus at each original nontrivial zero ρ, the reflected Weil term is
\(F_t(\rho)\overline{F_t(1-\bar\rho)}=F_t(\rho)^2\).
Replacing this by \(|F_t(\rho)|^2\) at a general off-line ρ would change the test. No such replacement occurs in ER37. On the critical line the two expressions agree, as follows directly from R14.

The zeros entering \(K_t=\sum_\rho m_\rho F_t(\rho)^2\) are the nontrivial zeros of the original ζ. The t-dependent source changes the test; it does not replace those zeros by zeros of H_t or of a different transported family.

## R38. Convergence required for the original-zeta contours

Each derivative of f_t is bounded by a polynomial times \(e^{-Z^2/(4t)}\), as proved in R2–3. Completing the full square in the convolution gives

\[
y^2+(Z-y)^2=\frac{Z^2}{2}+2(y-Z/2)^2.
\tag{R16}
\]

Consequently every derivative of k_t is bounded by a polynomial in |Z| times \(e^{-Z^2/(8t)}\): the remaining integral in the shifted variable is a finite Gaussian polynomial moment. In particular, for every bounded real interval of c values, all derivatives of \(e^{-(c-1/2)Z}f_t(Z)\) and of \(e^{-(c-1/2)Z}k_t(Z)\) are integrable with bounds uniform in c. Repeated integration by parts gives arbitrary inverse-power decay of F_t(c+iy) and A_t(c+iy), uniformly on that fixed strip.

The inherited original-zeta zero count \(N(T)=O(T\log(T+2))\), counting multiplicities, therefore proves absolute convergence of \(\sum_\rho m_\rho|F_t(\rho)|^2\). For example an arbitrary inverse-power estimate of order 2 for F_t yields order 4 for its squared modulus, which is enough to sum against this count. The original nontrivial zeros lie in the fixed strip 0<Re ρ<1.

The contour-height construction is the one already justified in OZG20–21: use the genus-one logarithmic derivative of the full factored product Cζ, subtract the exact full logarithmic derivative C'/C, and choose heights separated from zero ordinates by at least a reciprocal polynomial in the height. The zero count leaves such heights. On each fixed finite-width strip the resulting bound for j=ζ'/ζ is polynomial along those horizontal edges. The arbitrary inverse-power decay of A_t makes their integrals vanish. This check needs no Gaussian decay in the vertical spectral variable; the established inverse-power estimates are sufficient. No estimate uniform in the left cutoff N is asserted.

The prime series in ER40 is absolutely convergent. Indeed R16 gives a bound of the form

\[
\frac{\Lambda(n)}{\sqrt n}|k_t(\log n)|
 \le C_t(\log n)(1+\log n)^M n^{-1/2}
                   e^{-(\log n)^2/(8t)}.
\tag{R17}
\]

For sufficiently large n, the last exponential is at most \(n^{-2}\), and the remaining power of log n is summable against \(n^{-5/2}\). Here \(\Lambda(p^j)=\log p\), with every prime power present; \(\Lambda(n)=0\) otherwise. This proves the series convergence without a truncation of its support.

## R39. Original reflection and every finite-cutoff sign

The companion uses the full factor

\[
C_{\rm ER}(s)=s(s-1)\pi^{-s/2}\Gamma(s/2).
\tag{R18}
\]

The referenced OZG reconstruction uses
\(C_{\rm OZG}(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\).
Their exact comparison is \(C_{\rm ER}=2C_{\rm OZG}\). Differentiating this full equality shows that their logarithmic derivatives coincide, because the derivative of the retained constant 2 is zero. This justifies using the same logarithmic-derivative convention without identifying or replacing the original full factors in the theta receiver.

Write

\[
j(s)=\frac{\zeta'(s)}{\zeta(s)},\qquad
\kappa(s)=-\tfrac12\log\pi+\tfrac12\psi_\Gamma(s/2).
\tag{R19}
\]

The original theta reflection for C_ERζ and the full derivative
\(C_{\rm ER}'/C_{\rm ER}=1/s+1/(s-1)+\kappa(s)\)
give

\[
j(s)+j(1-s)=-\kappa(s)-\kappa(1-s).
\tag{R20}
\]

The endpoint terms have been accounted for exactly: their sum is
\(1/s+1/(s-1)+1/(1-s)+1/(-s)=0\)
as a meromorphic identity. The remaining expression retains both Gamma derivatives and both powers-of-pi contributions in R19–20.

Fix an integer N≥0, put \(b_N=-2N-1\), choose σ>1, and integrate each vertical line upward with factor \(1/(2\pi i)\). The original divisor inside the strip consists of all nontrivial zeros, the trivial zeros −2,…,−2N, and the pole 1. The convergent exhaustion from R38 gives

\[
I_\sigma(A_tj)-I_{b_N}(A_tj)
 =K_t+\sum_{m=1}^NA_t(-2m)-A_t(1)
 =:V_{N,t}.
\tag{R21}
\]

There is no original-zeta zero or pole at 0. Its later occurrence comes from the Gamma factor, as calculated below.

The two Euler contributions have negative signs. Mellin inversion in the stated convention proves

\[
I_\sigma(A_t(s)n^{-s})=n^{-1/2}k_t(-\log n).
\tag{R22}
\]

For example, on s=σ+iy, the Fourier integral selects Z=−log n from \(k_t(Z)e^{-(\sigma-1/2)Z}\), leaving precisely \(n^{-1/2}\). Hence
\(I_\sigma(A_tj)=-\sum_{n\ge2}\Lambda(n)n^{-1/2}k_t(-\log n)\).
Insert R20 in the left edge. The change r=1−s converts the upward integral on the left into an upward integral on the right after reversing the bounds; it introduces no extra overall sign. The resulting term contains A_t(1−r), and inversion gives the other value k_t(log n). Shifting its Euler half-plane line crosses no pole. Thus

\[
V_{N,t}=-P_t+\mathcal G_{N,t},\qquad
P_t=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
            [k_t(\log n)+k_t(-\log n)].
\tag{R23}
\]

The source k_t is even by R15, proving the factor 2 in ER40.

At s=−2m, m≥0, the residue of \(\kappa(s)\) is −1: the Gamma logarithmic derivative at −m has residue −1, its argument s/2 gives a chain factor 2, and the prefactor 1/2 retains the result −1. At s=1+2m the residue of \(\kappa(1-s)\) is +1, because the reflected argument has the opposite derivative. Shifting the line of \(A_t(s)[\kappa(s)+\kappa(1-s)]\) from b_N to 1/2 therefore crosses exactly the residues

\[
-A_t(0)-\sum_{m=1}^NA_t(-2m).
\tag{R24}
\]

The right-edge integral minus the left-edge integral equals that sum. It follows that

\[
\mathcal G_{N,t}=I_{1/2}\{A_t[\kappa+\kappa\circ(1-\cdot)]\}
                 +A_t(0)+U_{N,t}.
\tag{R25}
\]

Combining R21, R23 and R25 gives exactly

\[
K_t=A_t(0)+A_t(1)+A_\infty(k_t)-P_t.
\tag{R26}
\]

For the actual test R3 evaluates both endpoint terms to zero; their separate contributions and reasons for vanishing remain in the formula. Every cutoff N retains the actual finite sum U_N,t. No infinite sum of the trivial-zero values has been assigned or assumed convergent.

## R40. The full Gamma integral

On the center line s=1/2+iy, the retained two Gamma factors give

\[
\kappa(s)+\kappa(1-s)
 =\Re\psi_\Gamma(1/4+iy/2)-\log\pi.
\tag{R27}
\]

Also \(A_t(1/2+iy)=\widehat{k_t}(y)\), with
\(\widehat k(y)=\int k(Z)e^{-iyZ}dZ\) and inverse measure dy/(2π). The full digamma integral, valid for Re z>0, is

\[
\psi_\Gamma(z)=-\gamma_{\rm E}
 +\int_0^\infty\frac{e^{-x}-e^{-zx}}{1-e^{-x}}\,dx.
\tag{R28}
\]

Average z=1/4+iy/2 and its conjugate. Fourier inversion then gives

\[
\begin{split}
A_\infty(k)
&=-(\gamma_{\rm E}+\log\pi)k(0)\\
&\quad+\int_0^\infty
\frac{e^{-x}k(0)-\tfrac12e^{-x/4}[k(x/2)+k(-x/2)]}
     {1-e^{-x}}\,dx.
\end{split}\tag{R29}
\]

All constants and both translated source evaluations match ER40. The Gamma numerator can be written, as an exact equality retaining both pieces,

\[
(e^{-x}-e^{-x/4})k(0)
-\tfrac12e^{-x/4}[k(x/2)+k(-x/2)-2k(0)].
\tag{R30}
\]

The first piece is O(x), and the symmetric second difference is O(x²); hence division by \(1-e^{-x}\) is locally bounded. At infinity the displayed exponential factors are integrable against the bounded Gaussian-decaying source.

For the Fourier/digamma interchange itself, on 0<x≤1 the modulus of
\([e^{-x}-e^{-x/4}\cos(yx/2)]/(1-e^{-x})\)
is bounded by a constant times \(1+y^2\), using \(|1-\cos a|\le a^2/2\). The Schwartz function \(\widehat k\) is integrable with that weight. For x≥1 use the majorant \(C(e^{-x}+e^{-x/4})|\widehat k(y)|\). These bounds prove the required absolute interchange before the inverse transform is applied.

R3–R30 verify ER34–40 with the original endpoint, Gamma, prime-power, and trivial-zero contributions retained. The resulting K_t is a well-defined compensated pairing for the specified test. Neither the two negative source moments nor any step of this review evaluates its sign.
