# Independent review of the complete fixed-Gamma jet asymptotic

Review scope, received verbatim:

> Independent adversarial review complete new proof work/rh_counterfactual_20260913/continuation2/fixed_packet_kernel/fixed_gamma_full_jet_asymptotic.tex. Focus generating constants, Darboux C^J residual validity, beta gamma ratio proof, full confluent jet normalization, critical m² loglog exponent, cross blocks, exact CRT determinant. It proves fixed original χ det quotient V_N~const N^-A(logN)^-B. Do not edit. Need decisive defects if any; no numerical auxiliary arithmetic polynomial. Parent reading lower comparison concurrently.

The target proof was read completely. Its retained generating-integral source, `shared_thread_audit/segment29_40/sources/theta_gamma_reference.tex`, was read through the complete norm derivation TG7–TG14. No target source was edited by this reviewer; the owner added the explicit common-factor cancellation described below. No arithmetic polynomial, numerical substitute, Lean run, or publication was introduced. The parent maintains the complete user-input provenance.

## Verdict

No decisive defect was found in FPK.1–FPK.25. The determinant asymptotic is proved for the stated fixed original finite jet observation and fixed Gamma measure. It does not establish a contradiction to an off-line arithmetic zero. In particular, it contains no unproved uniformity in the packet or in k, and no sign assertion for the arithmetic four-window expression.

## Original normalization and coefficient estimates

The retained source gives

\[
\sum_{n\ge0}\frac{b_n(u)}{n!}z^n
 =(1+z^2)^{-1/4}\exp(u\arctan z),\qquad
\gamma_n=\sqrt2\,n!\Gamma(n+1/2).
\]

With the original definition \(p_n(c+w)=i^n b_n(w/i)\), the substitution is exactly \(z\mapsto iz\), \(u=w/i\). Since \(\arctan(iz)=i\operatorname{artanh}z\) near zero, the two exponents are \(-1/4-w/2\) at \(1-z\) and \(-1/4+w/2\) at \(1+z\). Thus FPK.7 preserves the original coordinate and phases.

The leading Taylor coefficient at z=1 is

\[
2^{-b(w)}\frac{n^{a(w)-1}}{\Gamma(a(w))}.
\]

Multiplication by

\[
\frac{n!}{\sqrt{\gamma_n}}
=2^{-1/4}n^{1/4}(1+O(n^{-1}))
\]

therefore gives exactly \(C_+(w)n^{w/2-1/2}\), with \(C_+(w)=2^{-1/2+w/2}/\Gamma(1/4+w/2)\). The other singularity gives the stated \((-1)^n C_-(w)n^{-w/2-1/2}\). There is no missing factor of two, factorial, or i.

The Darboux subtraction is global inside the open unit disc. Each list of subtracted terms is analytic at the opposite singularity. At z=1, the only nonanalytic remaining local factor is \((1-z)^{L-a(w)}A_L(z,w)\); at z=-1 it is the corresponding expression with b. Choosing L so that both real exponents exceed \(J_0+1\) makes all specified parameter derivatives and the first \(J_0\) angular derivatives continuous on the unit circle. Parameter derivatives introduce only finitely many logarithmic factors, dominated by the strict power margin. Periodic integration by parts consequently gives a uniform coefficient bound \(O(n^{-J_0})\). Taking \(J_0\ge J+1\) absorbs the normalization factor \(n^{1/4}\) and gives the residual \(O(n^{-J})\) used in FPK.10.

The beta-integral change of variables is correct:

\[
\frac{\Gamma(n+\alpha)}{\Gamma(n+1)}
=\frac{n^{\alpha-1}}{\Gamma(1-\alpha)}
\int_0^n(1-y/n)^{n+\alpha-1}y^{-\alpha}\,dy.
\]

First shifting the compact parameter set by a fixed integer ensures \(\Re\alpha<1\) with a strict uniform margin. For n sufficiently large, the other beta-integral condition \(\Re(n+\alpha)>0\) holds uniformly. Near y=0, all fixed powers of \(|\log y|\) remain integrable with \(y^{-\Re\alpha}\). On the first half interval the stated exponential majorant controls the difference to \(e^{-y}\) at order \(1/n\); the second half contributes an exponentially small integral, including all fixed parameter derivatives. Returning by the finite recurrence preserves the parameter-dependent factor \(n^{\alpha-1}\) and its logarithmic derivatives. Multiplication by the entire reciprocal gamma factors makes the coefficient conclusion valid at their zeros as well. This establishes the uniform differentiated FPK.10, rather than only a bound with the largest real exponent on a compact set.

## Off-critical full jets

Multiplication of normalized Taylor jets by a germ t is the lower triangular matrix whose entry (j,r), for r at most j, is \(t^{[j-r]}(w_i)\). Its determinant on a block of length \(m_i\) is \(t(w_i)^{m_i}\). For

\[
t(w)=\bigl(C_{\epsilon_i}(w)N^{\epsilon_iw/2}\bigr)^{-1},
\]

the gamma argument has positive real part at the original root, so this germ is analytic and nonzero on a neighborhood. Applying it to the entire Taylor jet, including all its triangular off-diagonal entries, yields FPK.15 exactly. No derivative of \(C_{\epsilon_i}\) or of the N-dependent factor has been discarded.

Writing \(d_i=|\delta_i|>0\), the nondominant squared norm is bounded by a fixed logarithmic power times \(N^{-d_i}\sum_{n\ge1}n^{-1-d_i}(1+\log n)^{2j}\), which tends to zero. The two slower remainder sums are bounded by logarithmic powers times

\[
N^{-d_i}\sum_{n=2}^N n^{d_i-3},\qquad
N^{-d_i}\sum_{n=2}^N n^{-1-d_i}.
\]

The first is respectively \(O(N^{-2})\), \(O(N^{-2}\log N)\), or \(O(N^{-d_i})\) according as \(d_i>2\), \(d_i=2\), or \(d_i<2\). The second is \(O(N^{-d_i})\). All tend to zero after any fixed logarithmic factor. Finitely many initial indices also vanish under this normalization.

The resulting same-half-plane Gram is precisely the integral FPK.16. Its real integrability exponent is positive. The logarithmic Riemann sums are uniformly integrable at zero. Opposite-half-plane products have the same absolute integrable envelope and an additional \((-1)^n\); pairing indices away from zero, followed by removing the uniformly small near-zero part, gives zero.

For positivity, setting \(x=e^{-y}\) leaves a common \(e^{y/2}\). The owner has now explicitly divided the identity by that factor before applying the annihilating differential operators. After this cancellation, the operators \((\partial_y+\epsilon w_a/2)^{m_a}\) remove exactly the other exponential-polynomial blocks. Their action on the remaining finite polynomial space is a product of invertible constant-plus-nilpotent operators because the original roots are distinct. Thus the complete lists of functions, including every repeated-root jet, are independent.

## Critical jets and all cross blocks

At a purely imaginary \(w_i\), differentiating \(n^{\pm w/2}\) j times and then dividing by j! gives \((\pm\log n/2)^j/j!\). Consequently FPK.18 has the correct relative sign \((-1)^{n+j}\). Every derivative falling on C has strictly lower logarithmic degree and vanishes in squared norm after scaling row j by \((\log N)^{-j-1/2}\).

At the same root, the nonalternating products yield the denominator \(j+l+1\) from

\[
(\log N)^{-j-l-1}\sum_{n\le N}\frac{(\log n)^{j+l}}n
\longrightarrow\frac1{j+l+1}.
\]

Because \(C_-(w_i)=\overline{C_+(w_i)}\), the resulting matrix is exactly FPK.19. It is a positive multiple of the moment Gram on [-1,1], after the explicit factors \(1/(2^j j!)\) in each row and column. All odd and even jet directions remain present. Its determinant is positive for every stated multiplicity.

For distinct critical roots, the nonalternating frequency is \(\theta=\Im(w_i-w_a)/2\ne0\). The derivative of \(x^{-1+i\theta}(\log x)^r\) is absolutely integrable, so comparison of the sum with its integral has bounded error. Substitution \(x=e^t\) and integration by parts give an integral of size \(O(1+(\log N)^r)\). Division by \((\log N)^{r+1}\) gives zero. The alternating sums are bounded by the same integrable-derivative pairing argument, including the within-root alternating products.

The mixed critical/off-critical argument also checks without cancellation: the normalized off-critical squared mass below \(Ne^{-R}\) tends to an integral that vanishes as R grows, whereas the normalized critical squared mass above that cutoff is \(O(R/\log N)\). Cauchy–Schwarz on the two index ranges, followed by the indicated order of limits, proves zero. The already established vanishing squared-norm remainders preserve all these Gram limits.

## CRT, determinant, and the claimed exponents

The observation matrix in the orthonormal polynomial coordinates is A, with \(AA^*=\mathsf K_N\). It is onto for \(N\ge q-1\), because the first q original monic polynomials span all degree-below-q polynomials, and their full Taylor observation at the roots is the Chinese remainder isomorphism. The minimum squared norm for jet y is \(y^*\mathsf K_N^{-1}y\); substituting \(y=\mathsf E_\chi v\) gives FPK.5 with its displayed adjoints.

The coalescing Vandermonde proof of FPK.6 correctly uses normalized derivatives. Its within-block leading determinant is \(\epsilon^{m_i(m_i-1)/2}\prod_{j<l}(x_{i,l}-x_{i,j})\), with no extra factorial because \(f^{[j]}=f^{(j)}/j!\). The ordinary Vandermonde has the stated increasing-column orientation. The cross-block limit is exactly \(\prod_{i<a}(\lambda_a-\lambda_i)^{m_im_a}\).

For an off-critical block,

\[
|\det\mathsf T_{N,i}|^2
=|C_{\epsilon_i}(w_i)|^{-2m_i}N^{-m_i|\delta_i|}.
\]

For a critical block,

\[
|\det\mathsf T_{N,i}|^2
=(\log N)^{-2\sum_{j=0}^{m_i-1}(j+1/2)}
=(\log N)^{-m_i^2}.
\]

Thus the full positive limiting Gram gives exactly the claimed \(\mathcal A_\chi=\sum_i m_i|\Re\lambda_i-c|\), \(\mathcal B_\chi=\sum_{\Re\lambda_i=c}m_i^2\), and the positive constant FPK.22. Undoing the actual congruence and then applying FPK.5 gives FPK.23–FPK.25. There is no square-root ambiguity: the object proved asymptotic is the determinant of the original quotient Gram.

## Completed second audit and original-reference corollary

A separately delegated adversarial review of FPK.7–FPK.13 reached the same conclusion: no decisive gap in the Darboux subtraction, beta-ratio estimates, or compact-uniform differentiated remainder. It independently checked the normalization against the retained Gamma chapter. Gamma-ratio formulas are used for sufficiently large n; the finitely many remaining polynomial coefficients are entire functions of w and are absorbed into the stated bounds.

The owner subsequently requested review of the appended FPK.26–FPK.29. These formulas were read in full and compared with the retained original density in `continuation2/quotient_transport/quotient_transport.tex`, QT.3. With \(a=k/4\), the retained TG norms are \(2^{1-2a}n!\Gamma(n+2a)\), and the retained mass is \(c_a=2^{1-2a}\Gamma(2a)\). Multiplying the density by \((2\pi)^{k/2}/c_a\) therefore gives exactly

\[
\gamma_{k,n}=(2\pi)^{k/2}\frac{n!\Gamma(n+k/2)}{\Gamma(k/2)}.
\]

The normalization of the corresponding generating coefficients is

\[
\frac{n!}{\sqrt{\gamma_{k,n}}}
=(2\pi)^{-k/4}\sqrt{\Gamma(k/2)}\,
 n^{1/2-k/4}(1+O(n^{-1})).
\]

Multiplying the two singular coefficients \(2^{-k/4\pm w/2}n^{k/4\pm w/2-1}/\Gamma(k/4\pm w/2)\) yields precisely FPK.28 and the powers \(n^{\pm w/2-1/2}\). Because k is a fixed positive integer, the same coefficient proof applies. The normalization power is at most \(1/4\), so the choice \(J_0\ge J+1\) still controls the smooth Fourier residual. The dominant gamma argument has real part \(k/4+|\delta_i|/2>0\), and at critical roots the two coefficients are conjugate. Every full-jet argument above therefore carries over with exactly the stated replacements of C. The original CRT map and the off-critical Cauchy Gram remain unchanged. The positive constant and both exponents in FPK.29 are correct, with the entire original mass retained.
