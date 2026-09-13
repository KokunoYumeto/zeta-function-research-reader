# Independent final review: the full genus-zero proof and the positive theta tails

Date: 2026-09-13.

The complete files `tau_genus_zero_product_proof_20260913.tex` (GF1--GF13) and `theta_certified_tail_subreview_20260913.md` (TT1--TT12) were read and checked. The original workbench `NOTE.tex` was also read in full to check the exact function, coefficient convention, and invocation of the product theorem. A separate reviewer read the entire retained `certify_theta_hankel.py` and matched its callback and tail expressions to TT1--TT12. No source file was modified and no integration, Lean run, or remote publication was performed in this review.

**Acceptance:** GF1--GF13 and TT1--TT12 are mathematically valid with their original constants, signs, multiplicities, and domains. No correction is required. The explicit derivation below supplies the original-theta growth estimate invoked in the first paragraph of GF, and the remainder checks every step of the product argument and of the two tail estimates. The finite computation's exact arithmetic and numerical integration certification are outside this review; accepting the tail formulas does not by itself certify those separate operations.

## 1. Exact sources and the original analytic input

The reviewed bytes are:

| Source | Bytes | SHA-256 |
|---|---:|---|
| `tau_genus_zero_product_proof_20260913.tex` | 7008 | `9bade2c098f1b03ba4ec4e526f4dffe4ced36f70bd7a533931a16335b162c394` |
| `theta_certified_tail_subreview_20260913.md` | 6761 | `4e5c6ad421b6d893e551c1746e05a08be3bf3b0753fae69c16febd5b7025dedf` |
| `certify_theta_hankel.py` | 7472 | `a97486edc2fc1f05f155a9539ad280433be39a8f6924efbc8c1c1c4d71033950` |
| Original workbench `NOTE.tex` | 20408 | `df7854f73ecb396c21165f8c032722a851a2a4c893f2553c6da96f88014b62f6` |

The original source in the workbench is

\[
\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\qquad
f_0(x)=2\sum_{n\ge1}\phi_*(nx),\qquad
\psi(y)=e^{y/2}f_0(e^y).
\tag{GFR1}
\]

The supplied Mellin identity and reflection give

\[
g(1/2+iz)=\int_{\mathbb R}\psi(y)e^{izy}\,dy,\qquad
\psi(-y)=\psi(y),\qquad g=2\xi.
\tag{GFR2}
\]

The workbench's coefficients specify the entire function by

\[
F(w)=\sum_{j\ge0}\frac{(-1)^j M_{2j}}{(2j)!}w^j,
\quad M_{2j}=\int_{\mathbb R}y^{2j}\psi(y)\,dy,
\quad F(z^2)=g(1/2+iz).
\tag{GFR3}
\]

All factors of two in (GFR1)--(GFR3) are retained. In particular, the original value is
\(F(0)=g(1/2)=\int_{\mathbb R}\psi(y)\,dy>0\).

Here is a completely explicit route from the source to GF1. Put

\[
\rho=\exp(4-2\pi),\qquad
C_\theta=\frac{8\pi^2}{1-\rho}.
\tag{GFR4}
\]

Because \(\pi>3\), \(0<\rho<1\). For \(n\ge1\),

\[
\frac{(n+1)^4e^{-\pi((n+1)^2-1)}}{n^4e^{-\pi(n^2-1)}}
=(1+1/n)^4e^{-\pi(2n+1)}
\le e^{4/n-2\pi n}\le\rho.
\]

The first term of the sequence is one, so its sum is at most \((1-\rho)^{-1}\). For \(y\ge0\), the literal summand of \(\psi\) is positive and bounded above by its positive fourth-power term. Consequently

\[
\begin{split}
0<\psi(y)
&\le8\pi^2e^{9y/2-\pi e^{2y}}
\sum_{n\ge1}n^4e^{-\pi(n^2-1)e^{2y}}\\
&\le C_\theta e^{9y/2-\pi e^{2y}}.
\end{split}
\tag{GFR5}
\]

Reflection gives the same estimate with \(|y|\). For every fixed \(s\ge0\), this bound times \(e^{s|y|}\) is integrable. It justifies the power-series expansion and differentiations in (GFR2) by domination on every compact set of \(z\). The evenness of \(\psi\) removes exactly the odd coefficients. It also proves convergence of (GFR3) on every compact set of \(w\), since one can compare the absolute series with the even exponential series at \(|z|=\sqrt{|w|}\).

For \(R\ge1\) and every \(|w|\le R\), choose one number \(z\) with \(z^2=w\). This pointwise choice uses no holomorphic square-root branch; it only gives \(|z|\le\sqrt R\). Let \(a=9/4+\sqrt R/2\). Equation (GFR5) gives

\[
\begin{split}
|F(w)|
&\le2C_\theta\int_0^\infty
 e^{(9/2+\sqrt R)y-\pi e^{2y}}\,dy\\
&=C_\theta\int_1^\infty t^{a-1}e^{-\pi t}\,dt
\le C_\theta\pi^{-a}\Gamma(a).
\end{split}
\tag{GFR6}
\]

The substitution is exactly \(t=e^{2y}\), so \(dy=dt/(2t)\). The factor two from the two half-lines cancels this denominator two. For \(a>1\), the positive function \(t^{a-1}e^{-t/2}\) has its maximum at \(t=2(a-1)\); this follows from its logarithmic derivative \((a-1)/t-1/2\). Thus

\[
\Gamma(a)=\int_0^\infty
 \bigl(t^{a-1}e^{-t/2}\bigr)e^{-t/2}\,dt
\le2\left(\frac{2(a-1)}e\right)^{a-1}.
\tag{GFR7}
\]

Write \(K_0=\max\{0,\log(2C_\theta)\}\). Since
\(a-1=5/4+\sqrt R/2\le7\sqrt R/4\), equations (GFR6)--(GFR7) imply

\[
\log M_F(R)
\le K_0+\frac74\sqrt R\log\frac72
             +\frac78\sqrt R\log R.
\tag{GFR8}
\]

In deriving this upper bound, the terms \(-(a-1)-a\log\pi\) were discarded only because they are negative; the original function and its mass remain unchanged. For \(R\ge1\),
\(\log R/R^{1/4}\le4/e\): putting \(u=\log R\ge0\), the derivative of \(ue^{-u/4}\) is \(e^{-u/4}(1-u/4)\), whose maximum value is \(4/e\). Hence a concrete choice in GF1 is

\[
\alpha=\frac34,\qquad R_0=1,\qquad
C=K_0+\frac74\log\frac72+\frac7{2e}>0.
\tag{GFR9}
\]

This derivation proves the growth hypothesis for precisely the original \(F\). It does not use zero ordinates, a product formula, or an assumed location of zeros.

## 2. Counting all zeros, with their multiplicities

For the general entire function in GF1, \(F(0)\ne0\) ensures that the function is not identically zero and that all zeros have positive modulus. Zeros in any compact disk are finite, counting multiplicities. Choose a radius \(R\) whose circle has no zero and divide \(F\) by the factors \(z-a_j\) for all its zeros in that disk. The quotient extends holomorphically through those zeros and is nonvanishing on a slightly larger disk: the boundary circle is compact and nonvanishing, so an annular neighborhood of it contains no zero. Its logarithmic derivative has a primitive on this disk, obtained from its power series. If \(L'\) is that logarithmic derivative, differentiating the quotient times \(e^{-L}\) gives zero, so this quotient equals a nonzero constant times \(e^L\). A choice of a complex logarithm of the constant supplies its holomorphic logarithm.

The mean of the real part of a holomorphic logarithm equals its central value by its uniformly convergent Taylor series on the circle. For a removed zero \(|a_j|<R\), the uniformly convergent expansion

\[
\log(1-a_je^{-i\theta}/R)
=-\sum_{k\ge1}\frac{(a_j/R)^ke^{-ik\theta}}k
\]

has real part of mean zero. Thus the mean of \(\log|Re^{i\theta}-a_j|\) is exactly \(\log R\). Subtracting the central value of the removed linear factors gives GF3, including the term \(\log|F(0)|\) and each repeated zero.

For sufficiently large \(r\), the set of excluded radii in \((2r,3r)\) is finite. Choose any other \(R\) there. Every zero with \(|a_j|\le r\) contributes at least \(\log2\), whereas every other term in GF3 is nonnegative. Therefore

\[
n(r)\log2\le C(3r)^\alpha-\log|F(0)|.
\tag{GFR10}
\]

This proves \(n(r)\le C_1r^\alpha\) for all sufficiently large \(r\). Choose \(r_0>0\) strictly below the modulus of every zero. Such a radius exists by nonvanishing at zero; if the zero set is empty any positive radius works. On the remaining bounded interval, \(n(r)/r^\alpha\) is bounded above by a fixed finite count divided by \(r_0^\alpha\). Enlarging \(C_1\) therefore proves the estimate for every \(r\ge r_0\).

Partition the zeros into the half-open annuli
\(2^kr_0<|a_j|\le2^{k+1}r_0\), \(k\ge0\). There are no zeros omitted below or at \(r_0\). Each term in the \(k\)-th annulus is at most \((2^kr_0)^{-1}\), and that annulus contains at most \(n(2^{k+1}r_0)\) zeros. Consequently

\[
\sum_j|a_j|^{-1}
\le C_1 2^\alpha r_0^{\alpha-1}
\sum_{k\ge0}2^{k(\alpha-1)}<\infty.
\tag{GFR11}
\]

This verifies GF4 without a density assumption and with every multiplicity included.

## 3. Construction of the literal product and the selected-circle bound

Let \(P(z)=\prod_j(1-z/a_j)\). For a fixed disk \(|z|\le A\), only finitely many zeros have modulus at most \(2A\). For every remaining factor, the power-series logarithm obeys

\[
|\log(1-z/a_j)|
\le\sum_{k\ge1}|z/a_j|^k/k
\le\frac{|z/a_j|}{1-|z/a_j|}\le2A/|a_j|.
\tag{GFR12}
\]

By (GFR11) these logarithms have an absolutely and uniformly convergent sum. Its exponential has no zero on the disk. Multiplication by the preceding finite factors therefore gives a holomorphic function with exactly the prescribed zeros and orders there. The constructions agree on intersections because they use the same absolutely convergent tail and finite factors. They define the entire \(P\), independent of the enumeration of zeros, with \(P(0)=1\).

At each zero, \(F\) and \(P\) have the same order and a nonzero leading coefficient, so \(H=F/P\) extends as a nonvanishing holomorphic function. Thus \(H\) is nonvanishing entire. Integrating the entire power series of \(H'/H\) and choosing the constant at zero gives an entire \(h\) satisfying \(H=e^h\). No bound on \(1/P\) has been used in this construction.

For sufficiently large \(t\), set \(N_t=n(4t)\) and \(\delta_t=t/[4(N_t+1)]\). The union of the open intervals of radius \(\delta_t\) about the at most \(N_t\) zero moduli at most \(4t\) has total length at most
\(2N_t\delta_t=tN_t/[2(N_t+1)]<t/2\).
The interval \([t,2t]\) has length \(t\), so a radius \(R_t\) outside the union exists. For every \(|z|=R_t\) and every zero \(|a_j|\le4t\), the reverse triangle inequality yields

\[
|1-z/a_j|=\frac{|a_j-z|}{|a_j|}
\ge\frac{|R_t-|a_j||}{4t}
\ge\frac1{16(N_t+1)}.
\tag{GFR13}
\]

Repeated zeros merely repeat factors; counting their excluded intervals more than once only weakens the estimate on the union length. For every remaining zero, \(|a_j|>4t\) and \(|z|\le2t\), so \(|z/a_j|<1/2\). Equation (GFR12) implies
\(\log|1-z/a_j|\ge-2|z|/|a_j|\).
Using annuli \(2^k4t<|a_j|\le2^{k+1}4t\), exactly the counting argument above gives

\[
\sum_{|a_j|>4t}|a_j|^{-1}
\le\frac{C_1 2^\alpha4^{\alpha-1}}{1-2^{\alpha-1}}t^{\alpha-1}
=C_2t^{\alpha-1}.
\tag{GFR14}
\]

Both the finite log sum and its uniformly convergent infinite tail can now be evaluated on the full circle, giving

\[
\log|P(z)|
\ge-N_t\log(16(N_t+1))-2R_tC_2t^{\alpha-1}.
\tag{GFR15}
\]

For completeness, put \(A=C_1 4^\alpha\). For \(t\ge e\), \(N_t\le At^\alpha\),
\(N_t+1\le(A+1)t^\alpha\), and \(R_t\le2t\). Thus

\[
\begin{split}
N_t\log(16(N_t+1))
&\le At^\alpha[\log(16(A+1))+\alpha\log t],\\
2R_tC_2t^{\alpha-1}&\le4C_2t^\alpha.
\end{split}
\]

Taking \(C_3=A[\log(16(A+1))+\alpha]+4C_2\) proves GF9 for all these sufficiently large \(t\). The proof covers infinitely many, finitely many, or no zeros; an empty finite log sum contributes zero.

## 4. The exact argument forcing the zero-free quotient to be constant

On the selected circle, \(F\) and \(P\) are nonzero. Therefore
\(\Re h=\log|H|=\log|F|-\log|P|\).
For large \(t\), GF1 applies at \(R_t\) and yields

\[
\Re h(z)\le C\,2^\alpha t^\alpha+C_3t^\alpha\log t
\le B_t:=(C\,2^\alpha+C_3)t^\alpha\log t
\quad(|z|=R_t),
\tag{GFR16}
\]

where \(t\ge e\). The product \(C\,2^\alpha\) retains the original growth constant \(C\); the tail constant \(C_2\) has already entered through \(C_3\).

Write \(h(z)=\sum_{k\ge0}d_kz^k\). On any fixed circle this series and its conjugate converge uniformly. For every integer \(\ell\ge1\), multiplying

\[
\Re h(R_te^{i\theta})=
\frac12\sum_{k\ge0}d_kR_t^ke^{ik\theta}
+\frac12\sum_{k\ge0}\overline{d_k}R_t^ke^{-ik\theta}
\]

by \(e^{-i\ell\theta}\) and integrating gives exactly

\[
\frac1\pi\int_0^{2\pi}\Re h(R_te^{i\theta})e^{-i\ell\theta}\,d\theta
=d_\ell R_t^\ell.
\tag{GFR17}
\]

Only the first sum's term \(k=\ell\) survives. In particular, the coefficient \(1/\pi\) in GF10 is correct. The integral of the constant \(B_t\) times \(e^{-i\ell\theta}\) is zero. Since \(B_t-\Re h\ge0\), the triangle inequality and the mean-value identity give

\[
|d_\ell|R_t^\ell
\le\frac1\pi\int_0^{2\pi}(B_t-\Re h(R_te^{i\theta}))\,d\theta
=2(B_t-\Re h(0)).
\tag{GFR18}
\]

For fixed \(\ell\ge1\), divide by \(R_t^\ell\ge t^\ell\). The upper bound tends to zero because
\(t^{\alpha-\ell}\log t\to0\) and \(\alpha<1\le\ell\). Hence \(d_\ell=0\) for every positive \(\ell\). This proves that \(h\), and therefore \(H\), is constant. Its value is determined without modifying the original source: \(H(0)=F(0)/P(0)=F(0)\). The result is the literal factorization

\[
F(z)=F(0)\prod_j(1-z/a_j).
\tag{GFR19}
\]

This proof does not invoke the conclusion of a factorization theorem as an input. The counting, convergence, selected-circle lower bound, and Fourier-coefficient bound together prove the entire special case used by the workbench.

## 5. The logarithmic coefficient map retains every multiplicity

Group repeated zeros and put \(\beta_j=1/a_j\), now indexing distinct zeros with multiplicities \(m_j\). Equation (GFR11) gives \(S=\sum_jm_j|\beta_j|<\infty\), and the \(\beta_j\) are bounded because there is a zero-free neighborhood of zero. Choose \(r>0\) with \(r|\beta_j|\le1/2\) for all \(j\); if there are no zeros any positive \(r\) works. For \(|z|\le r\),

\[
\sum_j\left|\frac{m_j\beta_j}{1-\beta_jz}\right|\le2S.
\tag{GFR20}
\]

The uniform logarithm convergence used to construct \(P\), together with this uniform derivative bound, permits termwise differentiation there. Equivalently, integrate this uniformly convergent derivative series from zero and compare the analytic logarithms, whose values at zero are fixed. In either construction,

\[
-\frac{F'(z)}{F(z)}=
\sum_j\frac{m_j\beta_j}{1-\beta_jz}.
\]

The double geometric series is absolutely summable because

\[
\sum_j\sum_{n\ge0}m_j|\beta_j|^{n+1}r^n
=\sum_j\frac{m_j|\beta_j|}{1-r|\beta_j|}\le2S.
\tag{GFR21}
\]

Thus its sums can be interchanged, and the coefficient of \(z^n\) is exactly \(\sum_jm_j\beta_j^{n+1}\). This proves GF13 and the workbench's logarithmic coefficients in their original scalar coordinate. It leaves the reflected packet modules, their nilpotents, and their independent operator constructions unchanged upstream of that scalar map.

## 6. Verification of the positive tails and the exact omitted regions

For the half-line moment integrand define, exactly as in TT1,

\[
x_n(y)=\pi n^2e^{2y},\qquad
f_{J,n}(y)=y^Je^{y/2}(16x_n(y)^2-24x_n(y))e^{-x_n(y)}.
\tag{GFR22}
\]

Here \(y\ge0\), \(n\ge1\), and \(J\) is a nonnegative integer. At \(J=0\), \(y^J\) is the constant polynomial one. For even \(J\), summing and integrating (GFR22) is precisely \(M_J\) in (GFR3): the source factor two and the reflection factor two are both already present in the coefficients \(16\) and \(-24\).

Because \(x_n(y)\ge\pi>3/2\),
\(16x_n^2-24x_n=8x_n(2x_n-3)>0\). Therefore

\[
0\le f_{J,n}(y)
\le16\pi^2n^4 y^J e^{9y/2-\pi n^2e^{2y}}.
\tag{GFR23}
\]

The finite callback keeps \(1\le n<N\) on \([0,L]\). Up to their measure-zero common boundary, the omitted regions are exactly \(n\ge N,\ 0\le y\le L\) and \(n\ge1,\ y\ge L\). They are disjoint and their union is the full complement of the retained region. Positivity permits the sum and integral interchanges by Tonelli's theorem; the bounds below prove their total finiteness.

On \([0,L]\), the majorant in (GFR23) is at most
\(16\pi^2n^4 L^J e^{9L/2-\pi n^2}\). Integrating the interval of length \(L\) and setting \(a_n=n^4e^{-\pi n^2}\) gives the upper bound
\(16\pi^2L^{J+1}e^{9L/2}\sum_{n\ge N}a_n\).
For every \(n\ge N\),

\[
\frac{a_{n+1}}{a_n}
=(1+1/n)^4e^{-\pi(2n+1)}
\le e^{4/n-\pi(2n+1)}
\le e^{4/N-2\pi N}=:\rho_n.
\tag{GFR24}
\]

The final symbol is constant for the selected first omitted index \(N\); its subscript does not introduce a summation over ratios. For \(\rho_n<1\), induction and the geometric sum give the full upper bound

\[
T_n=\frac{16\pi^2L^{J+1}e^{9L/2}N^4e^{-\pi N^2}}
 {1-e^{4/N-2\pi N}}.
\tag{GFR25}
\]

For the omitted \(y\)-interval, apply the same exact ratio at fixed \(y\ge0\):

\[
\frac{(n+1)^4e^{-\pi(n+1)^2e^{2y}}}{n^4e^{-\pi n^2e^{2y}}}
\le e^{4/n-2\pi n e^{2y}}
\le e^{4-2\pi e^{2y}}
\le\rho_y:=e^{4-2\pi}<1.
\tag{GFR26}
\]

The first term is \(e^{-\pi e^{2y}}\); hence the full \(n\)-sum in (GFR23) is bounded by it divided by \(1-\rho_y\). Put
\(V_J(y)=y^Je^{9y/2-\pi e^{2y}}\), which is positive on \([L,\infty)\) when \(L>0\). Its logarithmic derivative is

\[
\frac{V_J'(y)}{V_J(y)}
=\frac Jy+\frac92-2\pi e^{2y}
\le\frac JL+\frac92-2\pi e^{2L}
=-\delta,\quad
\delta=2\pi e^{2L}-\frac92-\frac JL.
\tag{GFR27}
\]

When \(\delta>0\), integration from \(L\) to \(y\) gives
\(V_J(y)\le V_J(L)e^{-\delta(y-L)}\). Its integral is at most \(V_J(L)/\delta\). Thus the second omitted region is bounded above by

\[
T_y=\frac{16\pi^2L^J e^{9L/2-\pi e^{2L}}}
 {(1-e^{4-2\pi})(2\pi e^{2L}-9/2-J/L)}.
\tag{GFR28}
\]

These are exactly TT6 and TT10. At the actual parameters \(N=20\), \(L=4\), \(0\le J\le64\), the elementary bounds \(\pi>3\) and \(e^8>1+8=9\) give

\[
4/N-2\pi N<-599/5,\qquad
4-2\pi<-2,\qquad
\delta>54-9/2-16=67/2>0.
\tag{GFR29}
\]

All denominators are strictly positive. Consequently the literal omitted integral belongs to \([0,T_n+T_y]\). The negative summand \(-24x_n\) remains part of the exact integral and finite callback; its removal in (GFR23) is solely the proved inequality bounding the omitted tails.

## 7. Analytic callback and source-to-proof comparison

The retained callback extends to every complex \(y\) as

\[
y^Je^{y/2}\sum_{n=1}^{N-1}
\bigl(16\pi^2n^4e^{4y}-24\pi n^2e^{2y}\bigr)
 e^{-\pi n^2e^{2y}}.
\tag{GFR30}
\]

It is a finite sum of products and compositions of entire functions, and \(y^J\) is a polynomial. Thus it is entire, including at zero for every allowed \(J\). It has no branch choice or hidden singularity. Treating \(\pi\) as its exact real constant, or any fixed constant value in an enclosing ball, does not alter this analyticity statement. The callback's complex ball value must enclose the exact expression; a possibly wide or nonfinite enclosure is a numerical issue, not an analytic singularity. The retained caller separately rejects a nonfinite integration result.

The separate full code comparison verified the following literal correspondence: the callback loops through \(n=1,\ldots,N-1\); `tn` is (GFR25); `ty` and `decay` are (GFR28) and (GFR27); the default values are \(N=20,L=4\); dimension 16 requests exactly \(J=0,2,\ldots,64\); the retained integral is partitioned into the eight half-unit intervals with endpoints \(j/2,(j+1)/2\), \(0\le j\le7\). The denominator comparisons must succeed before the code proceeds. The code forms `arb(0).union((tn+ty).upper())`, which encloses the proved interval \([0,T_n+T_y]\) whenever the computed balls enclose the stated expressions. Ignoring the callback's `analytic` flag is consistent with the entire formula (GFR30). This establishes the exact code-to-tail-formula match without asserting an integration replay.

## 8. Acceptance and scope

Every numbered mathematical step GF1--GF13 and TT1--TT12 is accepted. The original-theta specialization of GF1 has the explicit constants in (GFR4) and (GFR9), and its product and logarithmic coefficients follow from the complete proof above. The original half-line tail formulas have the exact constants and denominator signs in (GFR25)--(GFR29). No alteration of the original input, source mass, coefficient coordinate, multiplicity, finite integration interval, or first omitted index is needed.

This review establishes these analytic statements and their exact callback correspondence. It makes no claim that a finite collection of positive Hankel matrices proves RH or that the broader absolute-base geometric program fails. Those conclusions do not follow from the statements proved here.
