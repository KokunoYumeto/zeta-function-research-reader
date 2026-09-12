# Actual theta norms: source-first literature route and exact gamma comparison

Date: 12 September 2026. Scope: the measure

\[
d\mu(t)=|2\xi(1/2+it)|^2\,dt/(2\pi)
\]

and the fixed-full-packet measure \(d\nu_h=|2\xi/h|^2dt/(2\pi)\), with every selected order in \(h\) retained. This investigation changes no frozen reader, main branch, or corpus index. The complete mathematical continuation is in `tex/theta_gamma_reference.tex`, equations TG.1–TG.28. The machine-readable route is `work/theta_norm_literature_route_20260912.json`.

## What the bounded search establishes

The canonical external-literature CLI was used for eleven targeted queries. Raw results, exact publication-unit IDs and executed timestamps are retained in `work/theta_norm_literature_queries`. The index is a routing instrument: each mathematical use below comes from reading the identified text or page images. No theorem for the actual zeta-modulated recurrence sequence was found in these bounded hits. That is a statement about this search, not a claim that the whole literature lacks such a theorem.

The main local hit was Junghanns–Mastroianni–Notarangelo, *Weighted Polynomial Approximation and Numerical Methods for Integral Equations* (2021), unit `PUBUNIT-FC77B3CF3B2C63B25968D88F`. I read its section structure and the relevant Ch.4 passages, printed pp.148–155, especially Lemma4.1.3 and Proposition4.1.4. The displayed generalized-Freud parameter there satisfies \(\lambda>1\). This particular class does not include the theta tail order1. Its cited literature led to the original stronger result below.

The author's publication page routes to Lubinsky–Mhaskar–Saff, [*A proof of Freud's conjecture for exponential weights*](https://math.vanderbilt.edu/saffeb/texts/81.pdf), Constructive Approximation4 (1988),65–83. This theorem **does** include order1. I read Definitions2.1–2.2, Theorems2.3–2.6, and the entire printed proof of Theorems2.3–2.4 on pp.80–81. Relevant predecessor lemmas in pp.77–79 were also read. The scan contains20 PDF pages, including a blank final page; printed p65 is PDFpage1. No OCR was run. Only the selected theorem/proof page images were rendered.

### The exact hypotheses that fail for the proposed direct application

For \(W=e^{-Q}\), Definition2.1 requires even continuous \(Q\), \(Q'\) on \((0,\infty)\), bounded \(xQ'(x)\) at0, and eventually

\[
Q'>0,\quad x^2|Q'''|/Q'\le C,\quad1+xQ''/Q'\to\alpha>0.
\]

Theorem2.3 permits a finite generalized Jacobi factor, a polynomial exponential of degree below \(\alpha\), and bounded nonnegative \(\Psi\to1\). Theorem2.4 admits an additional \(V\), but requires \(\log V/Q\to0\) and bounded reciprocal approximation on the expanding interval by degree-\(o(n)\) polynomials. The proof uses these assumptions to invoke its restricted-range estimate and approximation lemma. Consequently its proof does not discard the multiplier's deep zero neighbourhoods.

The exact obstruction is TG.26–TG.28. Hardy's original1914 result supplies critical zeros with unbounded ordinates; a fixed packet removes finitely many. At every remaining ordinate \(T_j\),

\[
a_h(t)=(t-T_j)^{\ell_j}v_j(t),\qquad\ell_j\ge1,\quad v_j(T_j)\ne0.
\]

For a continuous positive reference amplitude \(B\) near these points, \(|a_h|/B\) is arbitrarily small on a positive-measure interval about each \(T_j\). Thus it cannot be \(\Psi\to1\). Given an eventually positive continuous \(Q\), choose that interval so that \(Q(t)\le Q(T_j)+1\) and \(|a_h(t)|/B(t)<e^{-j(Q(T_j)+1)}\). The quotient \(\log(|a_h|/B)/Q\) is then below \(-j\) there. It cannot be \(V\) with the stated logarithmic limit. A finite Jacobi factor or a tail factor converging to1 does not change this proof. Altering the value at isolated zeros does not repair intervals of positive measure.

This is an explicit failure of those hypotheses, followed by the exact comparison below. It does not establish that norm asymptotics are inaccessible by other arguments, including arguments measuring how much space those intervals occupy.

## Exact comparison that retains the arithmetic

Write the original factorization, including its phase,

\[
2\xi(1/2+it)=\Gamma(1/4+it/2)a(t),\quad
a(t)=-\pi^{-1/4}(t^2+1/4)e^{-it\log\pi/2}\zeta(1/2+it).
\]

Set \(d\sigma_\lambda=|\Gamma(\lambda+it/2)|^2dt/(2\pi)\). The exact maps are

\[
U_a:L^2(\mu)\to L^2(\sigma_{1/4}),\quad F\mapsto aF,
\]

and \(U_{a_h}:L^2(\nu_h)\to L^2(\sigma_{1/4})\), where \(a_h=(g/h)/\Gamma\) uses the entire quotient at every critical packet centre. Both are surjective isometries: cancellation proves the norm identity, and division off the discrete zero set gives the inverse. Their polynomial images remain \(a\mathbb C[t]\) and \(a_h\mathbb C[t]\). The full packet inclusion is the commuting identity \(U_{a_h}(h(1/2+it)P)=U_aP\).

TG.7–TG.14 prove the reference norms directly from the beta integral and Fourier inversion. In particular

\[
\int e^{iyt}\,d\sigma_\lambda(t)
=2^{1-2\lambda}\Gamma(2\lambda)(\cosh y)^{-2\lambda}.
\]

The factor2 is the Jacobian of \(t=2u\). The reference generating function is

\[
F_\lambda(z,t)=(1-iz)^{-\lambda+it/2}(1+iz)^{-\lambda-it/2}.
\]

Integrating its product at \(z,w\) gives
\(2^{1-2\lambda}\Gamma(2\lambda)(1-zw)^{-2\lambda}\). Its monic coefficients
\(b_n^{(\lambda)}(t)=n!P_n^{(\lambda)}(t/2;\pi/2)\) therefore have exactly

\[
\gamma_n^{(\lambda)}=2^{1-2\lambda}n!\Gamma(n+2\lambda),\qquad
b_{n+1}^{(\lambda)}=tb_n^{(\lambda)}-n(n+2\lambda-1)b_{n-1}^{(\lambda)}.
\]

For \(\lambda=1/4\), \(\gamma_n=\sqrt2\,n!\Gamma(n+1/2)\). This is an exact reference sequence, not the asserted value of an arithmetic norm. NIST [DLMF18.19.8–18.19.9](https://dlmf.nist.gov/18.19) and [18.22.8](https://dlmf.nist.gov/18.22) independently fix the usual polynomial convention.

All differentiated generating integrals are justified in the TeX. A contour shift of the beta integrand through any strip narrower than \(|\operatorname{Im}x|<\pi\) proves every exponential moment \(\int e^{v|t|}d\sigma_\lambda<\infty\), \(v<\pi/2\). No estimate for zeta is left implicit: Euler summation gives

\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}dx,
\quad |\zeta(1/2+it)|\le1+2\sqrt{t^2+1/4}.
\]

Hence \(a\) has at most cubic growth and all the following moments converge. Fixed packet divisors preserve that conclusion, with their cancelled germs controlling compact intervals.

Define the full monic arithmetic Gram matrix \(\mathsf B_N\), reference metric \(\mathsf\Gamma_N=\mathrm{diag}(\gamma_0,\ldots,\gamma_N)\), and their exact congruence

\[
(\mathsf B_N)_{ij}=\int b_i b_j|a|^2d\sigma_{1/4},\quad
\mathsf J_N=\mathsf\Gamma_N^{-1/2}\mathsf B_N\mathsf\Gamma_N^{-1/2},
\quad D_N=\det\mathsf J_N,\quad D_{-1}=1.
\]

Both metrics are retained, with inverse congruence explicitly given. Since the actual orthogonal monic basis differs by a triangular matrix of determinant1,

\[
\boxed{\mathfrak h_n=\gamma_nD_n/D_{n-1}},\qquad
\boxed{\mathfrak h_{n+1}/\mathfrak h_n
=(n+1)(n+1/2)D_{n+1}D_{n-1}/D_n^2}.
\]

The same construction with \(a_h\) gives \(\kappa_n^{(h)}=\gamma_nD_n^{(h)}/D_{n-1}^{(h)}\). It combines with KL.24 to give TG.18, with the original full degree \(d\) and its exact gamma-factor ratio. For a full conjugation/reflection packet the boundary identity is now

\[
\boxed{\epsilon_m^2=(m+1)(m+1/2)
\frac{D_{m+1}D_{m-1}}{D_m^2}
(r_m^{-1}-1)(1-r_{m+1})}.
\]

The unknown arithmetic determinant quotient is displayed as an actual positive matrix expression. It has not been replaced by1 or bounded by a hypothesized generic asymptotic theorem.

### Full original-coordinate kernel

The algebra map is \(\Psi p(t)=p(1/2+it)\). Its degree-\(n\) monic version \(i^{-n}\Psi p\) is used only on the corresponding affine monic space; it is not presented as a linear map on all polynomials.

Let \(\widehat b_j(s)=i^j b_j((s-1/2)/i)\), \(\Delta_N=\mathrm{diag}(i^j)\), and let \(C_N\) contain the full original remainders \([\widehat b_j]_h\). TG.20–TG.22 prove

\[
B_{N,s}^{(h)}=\Delta_N^*B_N^{(h)}\Delta_N,\qquad
K_N=C_N(B_{N,s}^{(h)})^{-1}C_N^*,\qquad
G_{N-d}=U_{\varepsilon_h}^*K_N^{-1}U_{\varepsilon_h}.
\]

The formula includes the initial \(N=d-1\) metric. At \(t_\rho=(\rho-1/2)/i\), every divided derivative is
\(\widehat b_j^{[\ell]}(\rho)=i^{j-\ell}b_j^{[\ell]}(t_\rho)\).
This keeps every nilpotent order, local unit and phase. No individual kernel column is assumed invertible.

## Relation to the xi-expansion literature

I read Romik's full proof of Theorem3.1 and Theorem3.2, printed/PDFpp.25–33, and the relevant AppendixA.2 formulas on pp.61–62. Its source is [the author's final PDF](https://www.math.ucdavis.edu/~romik/data/uploads/papers/riemannxi-final.pdf), with69pages. Theorems3.1–3.2 concern an entire xi expansion in a fixed parameter3/4 gamma basis and the asymptotics of its expansion coefficients. Their statement does not give the monic norms for the weight \(|2\xi|^2\).

The exact finite parameter map is proved in TG.23:

\[
b_n^{(1/4)}=\sum_{k\le n/2}\frac{n!}{(n-2k)!}\binom{1/2}{k}b_{n-2k}^{(3/4)},
\]

with inverse obtained by replacing \(\binom{1/2}{k}\) by \(\binom{-1/2}{k}\). This follows from the exact generating-function quotient \((1+z^2)^{1/2}\). It is a finite triangular isomorphism at every degree, preserves parity, transports all confluent columns, and preserves the kernel under full Gram congruence. The separate Hilbert isometry between the reference measures multiplies by \(\Gamma(1/4+it/2)/\Gamma(3/4+it/2)\), as proved in TG.24.

Inoue [arXiv1412.1220](https://arxiv.org/abs/1412.1220), §2.1–2.2/PDFpp.2–5, supplies a related modified Mellin transform and an asymptotic expansion-coefficient argument. Its variable uses \(s=1/2+2it\), and its function called \(\Xi\) in the introduction omits the \(s(s-1)/2\) completion factor used by Romik and this paper. Those conventions were read explicitly. The source's phrase “orthonormal basis” on p3 is immediately followed by norms \((\nu)_n/n!\); the displayed norms are retained. No expansion-coefficient estimate from it is substituted for the arithmetic determinant quotient above.

## A checked obstruction in the local secondary route

The local weighted-approximation book's Proposition4.1.4, printed pp.154–155, states a lower bound for multiplication by
\(T(x)=p_m^w(x)\sqrt{w(x)}|a_m^2-x^2|^{1/4}\), uniformly for arbitrary \(g\in L^p\), \(1\le p<\infty\), with constant independent of \(g\). In that unrestricted form it fails.

Fix an interior polynomial zero \(x_0\) of \(p_m^w\), away from any singularity of the weight. Near \(x_0\), \(T\) is continuously differentiable and \(T(x_0)=0\), so \(|T(x)|\le C|x-x_0|\) on a sufficiently small interval. Let \(g_\epsilon=\mathbf1_{(x_0-\epsilon,x_0+\epsilon)}\), with that interval inside \((-a_m,a_m)\). Then

\[
\|g_\epsilon T\|_p\le C\epsilon(2\epsilon)^{1/p},\qquad
\|g_\epsilon\|_{L^p(-a_m,a_m)}=(2\epsilon)^{1/p}.
\]

Their ratio tends to0. Thus there is no positive lower constant independent of \(g\). This explicit multiplication-map obstruction explains why that source proposition was not used as a coercivity estimate. The separate original LMS recurrence theorem is unaffected by this observation.

## Evidence and exact continuation

Raw source hashes are in `theta_norm_literature_sources/download_receipt.json`. Core editions:

| Source | SHA-256 | Read scope |
|---|---|---|
| LMS1988 full paper | `dbf5d1449cd3fe8aa9e6e5b0caf1442c46b1ce650450e398b6d9a578169f852a` | printed66–70,77–82; full main theorem proof80–81 |
| LMS1986 announcement | `579bf77f8676c1559f10d25f3dd0e828855423cf96b7d284bbd712869f14cd77` | all five printed pages217–221 |
| Romik final PDF | `608866c3ca1f37f6555959c8a0f3b61a312855782a781d4c64502ed4108d7fc5` | TOC,25–35,61–63; full Theorems3.1–3.2 proofs |
| Inoue arXiv PDF | `8b96150a7b8f2f3f79e2adfc7f341ab684ae0da548fab5e1edfb977b570b1294` | introduction/structure,2–5; no claim of full source audit |

The full TeX receives an independent audit and exact finite calibration in `checks/theta_gamma_reference_independent*.json`. These checks cover algebraic constants, parameter maps, phase/jet transformations and determinant identities on exact finite models. They do not certify asymptotics for the arithmetic zeta weight.

The next analytic calculation is now concrete: estimate the consecutive arithmetic Gram determinants \(D_{n+1}D_{n-1}/D_n^2\), together with the confluent remainder determinants in TG.18, using the original multiplier in TG.2. The exact formulas above remain valid during any such estimate. The current literature route leaves the full expanding-interval effect of zeta's small-value sets unresolved; no assumed theorem replaces that calculation.
