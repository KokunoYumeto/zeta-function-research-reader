# Independent review of the original-zeta Gaussian-translation reconstruction

Reviewed source: `ORIGINAL_ZETA_GAUSSIAN_TRANSLATION_RECONSTRUCTION.md`, SHA256 `a8093df5e71af1a8e1dcd423bb3bc17cd16b20203b2bbd99ab78403aab8058b9`, all OZG1–55 and OZG2a. The incoming mathematical source `translation_heat_intake_20260923/PRIME_TRANSLATION_EXTENSION.tex`, PWG1–28 including the nonsequential PWG24–28, was read in full. This review concerns mathematics only; it does not certify publication or any numerical sign of the complete Weil form.

**Conclusion.** The reconstructed domains, signs, coefficient and index maps, and the stated prime/source approximation bounds are valid. I found no mathematical correction needed in the controlling OZG source. Its correction of the incoming value of \(B_2(1/8)\) is necessary and correct. The positive-time original raw fixed-divisor sum diverges, so the proved positivity criterion applies to the specified augmented, compensated receiver, not an unconstructed scalar sum.

## 1. Original signed-divisor and Gamma-cutoff calculation

Put \(j=\zeta'/\zeta\), retain \(C=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\), and write \(q=C'/C\), \(\kappa=-\log\pi/2+\psi(s/2)/2\). At a trivial zero \(a=-2m\), the original local expressions are
\[
\zeta(a+h)=h u_m(h),\qquad C(a+h)=h^{-1}c_m(h),\qquad
j=h^{-1}+u_m'/u_m,\quad q=-h^{-1}+c_m'/c_m.
\tag{GTR1}
\]
OZG2a supplies the full nonvanishing unit \(c_m\), not just its leading coefficient. The test \(A=A_{\epsilon,a}\) is entire. Consequently the original local logarithmic-derivative residue is \(A(-2m)\), its opposite completion residue is \(-A(-2m)\), and each unit logarithmic derivative has a holomorphic product with \(A\). This proves why its residue is zero; it does not remove its value from the boundary integrals. The analogous original pole at 1 contributes \(-A(1)\), with compensation \(+A(1)\).

For a fixed \(N\), take the upward vertical lines \(b_N=-2N-1\) and \(\sigma>1\). Positively oriented rectangles give
\[
I_\sigma(Aj)-I_{b_N}(Aj)
=\sum_\rho m_\rho A(\rho)+\sum_{m\le N}A(-2m)-A(1).
\tag{GTR2}
\]
There is no omitted sign from the upward-line convention: the left edge of the positively oriented rectangle is traversed downward, accounting for the subtraction. The original zero count and separated-height contour argument bound the horizontal logarithmic derivatives by a polynomial. The factor \(e^{-\epsilon y^2}\) dominates it on the fixed strip. The constants need not and do not remain uniform as \(N\) increases. Both vertical lines are free of divisor points. The Euler series bounds the right line; the original functional equation and Gamma factors bound the left line. Thus the exhaustion in height is justified separately at each \(N\).

The original reflection identity is
\(j(s)+j(1-s)=-\kappa(s)-\kappa(1-s)\).
Substitution on the left edge of (GTR2) gives
\[
V_N=I_\sigma(Aj)+I_{b_N}(A(s)j(1-s))+
I_{b_N}(A(s)(\kappa(s)+\kappa(1-s))).
\tag{GTR3}
\]
The substitution \(w=1-s\) reverses the contour orientation and also gives \(ds=-dw\). Hence its second term is the upward integral
\(I_{1-b_N}(A(1-w)j(w))\), with a positive sign. Moving this line to \(\sigma\) stays within the zero-free Euler half-plane and crosses no pole. Termwise Fourier inversion in the absolutely convergent Euler series gives the two original terms
\(n^{-1/2}h_\epsilon(a-\log n)\) and
\(n^{-1/2}h_\epsilon(a+\log n)\).
The Euler logarithmic derivative has a minus sign, so these two terms give \(-P_\epsilon(a)\), exactly OZG23.

At the negative even integers including zero, \(\kappa(s)\) has residue \(-1\). At the positive odd integers, \(\kappa(1-s)\) has residue \(+1\), because of the reflected variable. Shifting from \(b_N\) to \(1/2\) crosses only \(0,-2,\ldots,-2N\). Therefore
\[
I_{1/2}(A(\kappa+\kappa(1-s)))
-I_{b_N}(A(\kappa+\kappa(1-s)))
=-A(0)-U_N.
\tag{GTR4}
\]
On the central line the Gamma sum is
\(\Re\psi(1/4+iy/2)-\log\pi\), and \(A(1/2+iy)\) is the Fourier transform of the stated shifted test. Thus (GTR4) is precisely
\(\mathcal G_N=A_\infty+A(0)+U_N\), with the positive sign of \(U_N\) in OZG24. Combining it with (GTR2) and (GTR3) gives the full equation
\[
K_\epsilon=A(0)+A(1)+A_\infty-P_\epsilon.
\tag{GTR5}
\]
The contour of the full \(q\), which also retains the endpoint polynomial, instead has value \(A(1)-U_N\). This verifies every sign in OZG20–27. In this test family \(A(0)=A(1)=0\) by the original factors \(F(0)=F(1)=0\); none of these calculations infer a vanishing support label from that scalar equality.

## 2. Fixed-divisor divergence and coefficient signs

For \(R_m=2m+1/2\), the trivial-zero value is
\[
d_m=4m^2(2m+1)^2e^{\epsilon R_m^2-aR_m}G_r(R_m)^2.
\tag{GTR6}
\]
Evenness and nonnegative mass one of \(b_r\) prove \(1\le G_r(R)\le e^{rR}\). Consequently \(\log d_m/R_m^2\to\epsilon\) at every fixed real \(a\). This proves divergence of the individual terms for positive \(\epsilon\), not merely failure of absolute convergence. The increasing polynomial and \(G_r\) factors give
\(d_{m+1}/d_m\ge e^{4\epsilon R_m+4\epsilon-2a}\to\infty\), proving \(U_N/d_N\to1\). At time zero, flatness of the original compact bump supplies every inverse power in its real-axis Laplace bound. Hence convergence includes \(a=2r\). Positive mass arbitrarily close to the support endpoint gives divergence for \(a<2r\). This verifies the exact domain transition and the noncommuting limits in OZG13–18.

No coordinate sum is assigned individually to \(d\) or \(-d\) at positive time. The quotient \(\mathbb C^{\mathbb N}/\ell^1\) and the paired-sum domain in OZG18–19 are defined algebraically. The indexed finite-cutoff comparison in OZG27 retains the original sequence \(d\), so it is injective. The scalar subtraction is proved by equal finite increments; it is not the subtraction of two previously assigned infinite numbers.

For the derivative source \(g_j=D^jf_\epsilon/j!\), integration by parts gives the exact Mellin multiplier \(c^j/j!\), where \(c=s-1/2\). Reflection gives \((-1)^jc^j/j!\) in the first slot. At \(c=-R_m\) their product has sign
\[
(-1)^j(-1)^{j+k}=(-1)^k.
\tag{GTR7}
\]
Thus OZG30 is correct in every degree, and its \((0,1)-(1,0)\) defect is exactly \(-2\sum_{m\le N}d_mR_m<0\). Each fixed-divisor entry has a constant sign and terms growing in modulus, proving the stated divergence for all indices. This is a non-Hermitian defect of the raw form, not a negative eigenvalue of a Hermitian compensated form.

Differentiation in \(\epsilon\) multiplies each coefficient by \(c^2\), including \(R_m^2\) on the fixed sector. The shifted coefficient \((j+1,k+1)\) reverses the reflected sign, so its multiplier is \(-(j+1)(k+1)\). Shifting either index by two retains its sign and supplies the two factorial multipliers in OZG32. Their average has the same value. This independently verifies that the raw, completion, and compensated matrices obey the displayed laws separately at each fixed cutoff.

## 3. Entire tower and exact negative index

The Gaussian factor is \(e^{\epsilon c^2}\), not \(e^{-\epsilon c^2}\). For \(c=x+iy\), its modulus is \(e^{\epsilon(x^2-y^2)}\). Since \(|x|<1/2\), it gives the Gaussian decay in height used in OZG9. The half-time factor in each source slot is essential: it makes the product equal this full factor. It proves normal convergence on every compact set in the complex translation parameter, and of every fixed derivative. This is sufficient for the entire two-variable Taylor expansion in OZG35 and its square-truncation limit; no merely smooth Taylor expansion is being treated as globally convergent.

For the boundedness converse, the coefficients
\(w_\rho e^{\epsilon c_\rho^2}\) are absolutely summable and decay in height. Their Cauchy sum is normally meromorphic on the complement of the discrete exponent set. At a right-hand off-critical exponent it has nonzero residue: the original bump transform has no zero off the imaginary axis, \(\rho(\rho-1)\ne0\), multiplicity is positive, and the exponential never vanishes. A bounded positive-half-line translation function has a holomorphic Laplace transform throughout \(\Re w>0\). Equality with the Cauchy sum first holds on \(\Re w>1/2\), then on the connected complement of its discrete poles in \(\Re w>0\). It makes each such pole removable, a contradiction. Reflection handles the opposite side. Under RH the coefficients are nonnegative real, so the full triangle inequality proves the bound in OZG33. This confirms both directions without assuming a sign outside their stated hypotheses.

To audit the stronger index statement, retain
\(\alpha_\rho=F(\rho)e^{\epsilon c_\rho^2/2}\),
\(\mathcal H_*=\ell^2(\mathcal Z_*,m)\), and
\((Ju)_\rho=u_{\rho^\#}\).
All off-critical points belong to \(\mathcal Z_*\), and the omitted critical points affect only the positive spectral part. The identities
\(\bar\alpha_{\rho^\#}=\alpha_\rho\) and
\(c_{\rho^\#}=-\bar c_\rho\) give exactly
\[
\langle JV_{c^j/j!},V_{c^k/k!}\rangle
=\sum_\rho m_\rho F(\rho)^2e^{\epsilon c_\rho^2}
\frac{(-1)^jc_\rho^{j+k}}{j!k!}.
\tag{GTR8}
\]
The complex square is correct; replacing it with a modulus square off the line would change the form.

The density proof is sound. Orthogonality to all polynomials makes all derivatives at zero of the entire transform
\(H_u(z)=\sum m_\rho\bar u_\rho\alpha_\rho e^{c_\rho z}\)
vanish. Cauchy–Schwarz gives normal convergence of every derivative because the square of \(\alpha_\rho\) in its modulus still contains Gaussian decay. The coefficients of its Laplace Cauchy transform are absolutely summable:
\[
\sum_\rho m_\rho|u_\rho\alpha_\rho|
\le\|u\|_{\mathcal H_*}
\left(\sum_\rho m_\rho|\alpha_\rho|^2\right)^{1/2}<\infty.
\tag{GTR9}
\]
Consequently that transform is normally meromorphic and its residues are the individual coefficients. The identity theorem and their nonzero \(\alpha_\rho\) imply \(u=0\). This proves density in the actual infinite weighted value space; it does not assume unrestricted infinite interpolation.

On each exchanged pair, \(J\) has one positive and one negative direction; on a fixed point it has one positive direction. Any finite negative polynomial subspace injects into the negative spectral part. Conversely a finite negative orthonormal column family \(U\) has \(U^*JU=-I\); an approximation \(V\) with \(\|V-U\|<1/4\) satisfies
\(\|V^*JV+I\|\le2\|V-U\|+\|V-U\|^2<9/16\).
Its Gram matrix stays strictly negative. A finite collection of approximating polynomials lies in one common finite degree block. This proves the equality of the supremal negative index with the actual number of exchanged pairs, including infinity, as asserted in OZG39.

## 4. Gaussian derivatives and complete error constants

The exact Gaussian derivative polynomial is
\[
\gamma_\epsilon^{(l)}(x)
=\gamma_\epsilon(x)\frac{l!}{2^l}
\sum_{j=0}^{\lfloor l/2\rfloor}
\frac{(-1)^{l-j}x^{l-2j}}
{\epsilon^{l-j}j!(l-2j)!}.
\tag{GTR10}
\]
For example its second derivative is
\((x^2/(4\epsilon^2)-1/(2\epsilon))\gamma_\epsilon\), and its fourth is
\((x^4/(16\epsilon^4)-3x^2/(4\epsilon^3)+3/(4\epsilon^2))\gamma_\epsilon\).
Splitting the Gaussian in half and maximizing each polynomial term gives exactly OZG42–43. At \(\epsilon=1/8\), direct substitution gives
\[
\mathcal B_2=16/\mathrm e+4,\qquad
\mathcal B_4=1024/\mathrm e^2+384/\mathrm e+48.
\tag{GTR11}
\]
Thus the incoming \(32/\mathrm e+4\) was not the value of its own defined \(B_2\). It was a larger bound. OZG corrects the value and retains a valid stronger estimate \(\mathcal C_{1/8,0}<503\).

The convolution with \(k_r\), a probability measure on \([-d,d]\), and the full filter \(D^4-D^2/2+1/16\) gives OZG44–45 by the triangle inequality. This bounds both translated legs and every derivative. For \(u=\log x\), the logarithmic derivative of the positive integer majorant is
\(1/u-1/2-(u-B)/(4\epsilon)\), nonpositive for \(u\ge\max(B,2)\). Therefore the sum over all integers \(n>N\) is bounded by the integral from \(N\) to infinity. Its exact value follows from
\[
\frac u2-\frac{(u-B)^2}{8\epsilon}
=-\frac{(u-B-2\epsilon)^2}{8\epsilon}
 +\frac B2+\frac\epsilon2.
\tag{GTR12}
\]
The integral of \((u-c_B)e^{-(u-c_B)^2/(8\epsilon)}\) is the first term \(4\epsilon e^{-(\log N-c_B)^2/(8\epsilon)}\); the constant \(c_B\) gives the complementary-error-function term with coefficient \(c_B\sqrt{2\pi\epsilon}\). This independently checks all factors in OZG46–47. It includes every omitted prime power and uses no prime-number estimate.

The finite source omits a probability convolution of radius \(d2^{-J}\). Its first-moment bound and the derivative bound give \(\eta_l=d2^{-J}\mathcal C_{\epsilon,l+1}\), exactly OZG48. For the Gamma expression near zero, write its full cancellation as OZG41. The first exponential difference is bounded by \(3x/4\); division by \(1-e^{-x}\ge x/2\) gives \(3\eta_l/2\). The central second difference is bounded by \(x^2\eta_{l+2}/4\); its extra factor \(1/2\), followed by the same denominator bound, integrates to \(\eta_{l+2}/8\) on \((0,1)\). On \((1,\infty)\), the exponential integrals give \((e^{-1}+4e^{-1/4})/(1-e^{-1})\) times \(\eta_l\). The constant Gamma term and both finite prime legs give exactly the remaining terms of OZG49. Thus this error bounds replacement of the source and omission of primes; evaluating the residual archimedean integral numerically would additionally need quadrature and rounding bounds, as the incoming PWG25–27 explicitly supplies.

At the stated cutoff, \(\epsilon=1/8\), \(B=1/32\),
\(c_B=9/32\), and \(x=16\log2-9/32>997/96\). The Gaussian-tail inequality gives
\[
\mathcal J<\frac{64}{59}\left(\frac12+\frac9{640}\right)
e^{-(997/96)^2}
=\frac{329}{590}e^{-994009/9216}.
\tag{GTR13}
\]
The first fraction follows from \(e^{5/64}<64/59\); the second error-function coefficient is \(9/(64x)<9/640\). The exact rational inequalities
\(994009/9216>46(7/3)\),
\(\sum_{k=0}^6(7/3)^k/k!=1071641/104976>10\), and
\(2\cdot503\cdot329/590<600\)
give OZG52. This proves a prime-tail error below \(6\cdot10^{-44}\). It is not a value or a sign of the whole first matrix entry.

## 5. Carrier and proof scope

OZG53 uses the actual carrier: nonzero amplitudes occur only at top support, while lower labels are distinct zero elements. Independent function values on those points are kept in their separate function space. The endpoint filter remains in each smoothed test; multiplying its zero endpoint values by the entire Gaussian factor leaves zero amplitudes with their original labels. At finite cutoff, the two top coefficients are \(K_\epsilon+U_N\) and \(-U_N\), so direct substitution proves
\(\boldsymbol B_L-\boldsymbol R_{\epsilon,N}=\boldsymbol D_L+\boldsymbol E_{\epsilon,N}\).
No separate norm for supported zero, scalar identification with \(\tau\), or unproved infinite fixed-divisor sum is used.

The review verifies the mathematical claims at their stated scope. It does not establish positivity of every coefficient block, boundedness of the translation function, or RH. It also does not infer a physical interpretation or an identity with a zero-moving heat flow. The actual content is the exact original-zeta cutoff comparison, its divergent fixed-sector obstruction, the entire compensated coefficient tower with unchanged full negative index, and the explicitly bounded arithmetic approximations.
