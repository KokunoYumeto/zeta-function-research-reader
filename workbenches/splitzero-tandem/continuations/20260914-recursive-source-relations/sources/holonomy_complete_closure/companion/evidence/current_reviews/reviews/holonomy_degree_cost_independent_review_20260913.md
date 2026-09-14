# Independent full proof review of the fixed-phase degree cost

Date: 2026-09-13. This review accepts HD1–10 in `holonomy_degree_cost_20260913.tex`, SHA-256 `9a1ba6cd7e8bee67c6d7868c74f2cf4f9d8c11fa255d9d278c7a2420cf0daca6`. The initial HD1–9 source was read completely. The root then corrected its closing split-kernel type statement at this reviewer's request, adding the exact two preimage formulas HD10; that final correction was read directly. The analytic and finite-source arguments below were independently checked in full. The complete supplied holonomy note and actual residue/metric-transfer sources had already been read for the accompanying HG1–25 plus HG11a review.

The scope fixes (h,k,a,L) as stated and varies the polynomial degree cutoff (N). No tensor-degree growth rate is derived, and no fixed-degree asymptotic is substituted for such a rate. Every matrix, evaluation row, phase, sample mass, and original Hilbert norm is retained. No mathematical source was edited by this reviewer; the parent made the requested precise type correction. No Lean or finite/numerical test was run or needed for these analytic proofs.

## 1. Original measure and finite polynomial Gram

Retain the full-order packet, (g=2\xi), and

\[
 c=k/2,\qquad S(u)=c+iu,\qquad
 w_h(u)=\frac{|(g/h)(1/2+iu)|^2}{2\pi},\qquad
 m=w_h^{*k},\qquad d\nu(u)=m(u)\,du.
 \tag{RHD1}
\]

The original source norm of a polynomial (P) is exactly (int|P(S(u))|^2d\nu(u)), not that integral after changing its density or mass. The established source estimate gives a finite positive exponential moment of (w_h) for any (0<b<\pi/2). Since the integrands are nonnegative, Tonelli and (|\sum_i u_i|\le\sum_i|u_i|) give, with every tensor factor present,

\[
 \begin{aligned}
 \int e^{b|u|}m(u)\,du
 &=\int_{\mathbb R^k} e^{b|u_1+\cdots+u_k|}
                    \prod_{i=1}^kw_h(u_i)\,d^ku\\
 &\le\prod_{i=1}^k\int_{\mathbb R}e^{b|u_i|}w_h(u_i)\,du_i
 <\infty.
 \end{aligned}
 \tag{RHD2}
\]

Thus (\nu) is finite, all its polynomial moments exist, and it is atomless because its definition is an absolutely continuous measure. The full-order quotient (g/h) is an entire nonzero function. On its vertical real-parameter line its zeros are isolated, so (w_h>0) almost everywhere. For (k\ge2), its convolution is positive at every real (u): at fixed (u), both factors (w_h(t)) and (w_h(u-t)) are positive outside a null set, so their integrable product is positive almost everywhere and has strictly positive integral. The original source estimates give boundedness and integrability of these factors; repeated convolution preserves the assertion. This also proves the sufficient almost-everywhere positivity for every (k\ge1).

A nonzero polynomial in (S(u)) vanishes at at most finitely many real (u). Hence it cannot have zero (L^2(\nu)) norm. All finite coefficient Grams (M_N) are therefore strictly positive. In particular, polynomial evaluation is well-defined on the polynomial subspace of (L^2(\nu)): distinct polynomials cannot represent the same Hilbert class.

## 2. HD2–3: exact evaluation norm and its minimum polynomial

For a fixed real (u_0), retain (S_0=c+iu_0) and the row (a_N=(1,S_0,\ldots,S_0^N)). For a coefficient column (v), its polynomial has evaluation (a_Nv) and squared norm (v^*M_Nv). The representing vector for this row in the original (M_N)-metric is (M_N^{-1}a_N^*), since

\[
 \langle M_N^{-1}a_N^*,v\rangle_{M_N}=a_Nv.
 \tag{RHD3}
\]

Its squared metric norm is (Lambda_N=a_NM_N^{-1}a_N^*>0); positivity follows from (a_N\ne0). Cauchy–Schwarz yields

\[
 |a_Nv|^2\le\Lambda_N,v^*M_Nv,
 \tag{RHD4}
\]

with equality for (v=M_N^{-1}a_N^*). Thus the supremum in HD3 is exactly (\Lambda_N), with all phases and all entries of (M_N) retained.

The displayed coefficient vector (c_N=M_N^{-1}a_N^*/\Lambda_N) has

\[
 a_Nc_N=1,\qquad c_N^*M_Nc_N=\Lambda_N^{-1}.
 \tag{RHD5}
\]

It is also the unique polynomial of minimum original squared norm with evaluation one. Indeed, every other such coefficient column is (c_N+w) with (a_Nw=0). Its cross term is (c_N^*M_Nw=(a_Nw)/\Lambda_N=0), so its squared norm is (Lambda_N^{-1}+w^*M_Nw), strictly larger unless (w=0). This proves the complete minimization assertion with the actual affine constraint. No vector mass is assigned a replacement value; the equality-one constraint specifies this particular family of source polynomials.

## 3. HD4–5: divergence of the evaluation norm

The polynomial spaces are nested by the actual inclusion (\mathcal P_N\hookrightarrow\mathcal P_{N+1}), which appends a zero coefficient and preserves both evaluation and original integral norm. Therefore (\Lambda_N\) is nondecreasing.

Assume for contradiction that (\Lambda_N\le K<\infty) for all (N). Then the linear functional (P\mapsto P(S_0)) on the union of those spaces is bounded by (\sqrt K\|P\|_{L^2(\nu)}). It extends uniquely by continuity to their Hilbert closure. The Hilbert representation theorem gives (f) in that closure with

\[
 P(S_0)=\int\overline{f(u)}P(S(u))\,d\nu(u)
 \quad\text{for every polynomial }P.
 \tag{RHD6}
\]

This step does not assume that the polynomials are dense in all of (L^2(\nu)); their own closed Hilbert subspace suffices. Since (u=(S-c)/i), every polynomial in (u) is exactly a polynomial in (S), with its full affine coefficients. Thus the finite complex measure

\[
 d\sigma(u)=\overline{f(u)}\,d\nu(u)-d\delta_{u_0}(u)
 \tag{RHD7}
\]

has all polynomial moments zero. It is finite because (\nu) is finite and (f\in L^2(\nu)). Furthermore, Cauchy–Schwarz gives the complete weighted estimate

\[
 \int e^{b|u|/2}|f(u)|\,d\nu(u)
 \le\|f\|_{L^2(\nu)}\left(\int e^{b|u|}\,d\nu(u)\right)^{1/2}<\infty.
 \tag{RHD8}
\]

The Dirac term also has finite exponential integral (e^{b|u_0|/2}). Hence (int e^{b|u|/2}d|\sigma|(u)<\infty).

Define (F(z)=\int e^{izu}d\sigma(u)). On each closed smaller strip (|\operatorname{Im}z|\le d<b/2), choose (d<d'<b/2). For every integer (j\ge0), the quantity (|u|^je^{-(d'-d)|u|}) is bounded; multiplying by (e^{d'|u|}) supplies an integrable majorant using RHD8. Therefore differentiation under the integral is valid at every order and locally uniform, so (F) is holomorphic on the connected strip (|\operatorname{Im}z|<b/2). Its derivatives at zero are

\[
 F^{(j)}(0)=i^j\int u^j,d\sigma(u)=0.
 \tag{RHD9}
\]

Its holomorphic Taylor series is zero near zero; the identity theorem makes (F) zero on the whole strip, in particular on its entire real axis.

Here is the full finite-measure uniqueness argument, including the constants and limiting test functions. For (t>0), take the actual Gaussian

\[
 \gamma_t(x)=(4\pi t)^{-1/2}e^{-x^2/(4t)}
 =\frac1{2\pi}\int_{\mathbb R}e^{-t\zeta^2}e^{-i\zeta x}\,d\zeta.
 \tag{RHD10}
\]

The Fourier representation follows by completing the square in the Gaussian integral, or its real Gaussian transform. Because (|\sigma|(\mathbb R)<\infty) and (e^{-t\zeta^2}) is integrable, Fubini applies absolutely. It gives

\[
 \begin{aligned}
 (\sigma*\gamma_t)(x)
 &=\frac1{2\pi}\int e^{-t\zeta^2}e^{-i\zeta x}
                  \left(\int e^{i\zeta u}d\sigma(u)\right)d\zeta\\
 &=0.
 \end{aligned}
 \tag{RHD11}
\]

For (\varphi\in C_c(\mathbb R)), another absolutely justified interchange and evenness of (\gamma_t) imply

\[
 \int(\varphi*\gamma_t)(u)\,d\sigma(u)
 =\int\varphi(x)(\sigma*\gamma_t)(x)\,dx=0.
 \tag{RHD12}
\]

The continuous compactly supported function (\varphi) is uniformly continuous on the whole real line. For any (\varepsilon>0), split its convolution error into (|y|<\varepsilon) and (|y|\ge\varepsilon). The first term is uniformly bounded by its modulus of continuity, and the second by (2\|\varphi\|_\infty\int_{|y|\ge\varepsilon}\gamma_t(y)dy). Under (y=\sqrt t,v), that tail tends to zero as (t\downarrow0). Thus (\varphi*\gamma_t\to\varphi) uniformly. Finiteness of (|\sigma|) lets RHD12 pass to the limit, giving (\int\varphi,d\sigma=0) for every (C_c) test function. Uniqueness of finite regular complex measures on these test functions gives (\sigma=0).

But the absolutely continuous measure (\overline f\nu) assigns zero mass to the singleton ({u_0}), whereas (\delta_{u_0}) assigns mass one. This contradicts RHD7 with (\sigma=0). Therefore the nondecreasing positive sequence (\Lambda_N) is unbounded and hence tends to infinity. No property of (\chi(S_0)) enters this proof; it is valid whether or not (S_0) is a root of the unchanged cyclic polynomial.

By RHD5, the actual source columns (\mathcal U_k\mathcal V P_N^{u_0}) have squared norm (\Lambda_N^{-1}\to0), while their evaluations stay equal to one. This proves HD5. The evaluation operator on the polynomial domain in its original Hilbert closure is not closable: its graph contains a sequence converging to ((0,1)), whereas an extension which is a linear operator must map zero to zero. This is the stated specific evaluation map. Every finite-degree evaluation and its minimum polynomial remain well-defined and exactly computed.

## 4. HD6–8: positive sample atom and the actual correlation-cost lower bound

Fix (L>0), (0\le\theta<2\pi), and an integer (n_0) giving (u_0=(2\pi n_0+\theta)/L) with (m(u_0)>0). Retain the actual sample mass

\[
 \omega_0=\frac{2\pi}{L}m(u_0)>0.
 \tag{RHD13}
\]

The sample Gram is the exact positive sum in HD6, with its (2\pi/L) factor and evaluations at (S((2\pi n+\theta)/L)). Its single (n_0) summand is (\omega_0a_N^*a_N). Every remaining summand is positive semidefinite, including zero summands, so

\[
 M_{N,\theta}\succeq\omega_0a_N^*a_N.
 \tag{RHD14}
\]

The endomorphism (M_N^{-1}M_{N,\theta}) is positive semidefinite and self-adjoint for the actual (M_N)-metric, even if the phase Gram is singular. Its largest eigenvalue is the supremum of its Rayleigh quotients. Insert exactly (c_N) from HD2 into RHD14 and use RHD5:

\[
 \frac{c_N^*M_{N,\theta}c_N}{c_N^*M_Nc_N}
 \ge\frac{\omega_0|a_Nc_N|^2}{\Lambda_N^{-1}}
 =\omega_0\Lambda_N.
 \tag{RHD15}
\]

This proves HD7 with the original sample mass. In particular, no division by a phase Gram or positivity of every atom is needed.

For the fixed actual weighted exponent (a>0), retain the source-weight comparison value (\kappa_{a,N}). The correlation estimate previously proved by the absolutely convergent two weighted tails is

\[
 M_{N,\theta}\preceq
 \left(1+\frac{\kappa_{a,N}}{e^{aL}-1}\right)M_N.
 \tag{RHD16}
\]

The proof of this upper inequality uses only the finite weighted source norms, correlation unfolding, and the geometric series; it never uses that the resulting error is smaller than one. The latter restriction was used elsewhere solely to obtain positive lower/inverse bounds. Thus applying RHD16 at all (N) here is legitimate even after its error grows.

Taking the largest generalized eigenvalue and combining RHD15–16 gives

\[
 \omega_0\Lambda_N\le1+\frac{\kappa_{a,N}}{e^{aL}-1},\qquad
 \kappa_{a,N}\ge(e^{aL}-1)(\omega_0\Lambda_N-1).
 \tag{RHD17}
\]

Every factor outside the parentheses is fixed and strictly positive. Since (\Lambda_N\to\infty), this proves (\kappa_{a,N}\to\infty) for the fixed original packet and tensor degree. For small (N), the right side may be negative; the inequality remains true and the eventual divergence is unaffected.

The exact finite matrix expression for (\Lambda_N) is the stated lower certificate. To satisfy (\kappa_{a,N}/(e^{aL_N}-1)\le\delta_0) with (0<\delta_0<1), solve this scalar inequality without changing the parameter:

\[
 e^{aL_N}\ge1+\kappa_{a,N}/\delta_0,\qquad
 L_N\ge a^{-1}\log(1+\kappa_{a,N}/\delta_0).
 \tag{RHD18}
\]

This is the required restriction for this particular correlation estimate. It does not prove a rate in (N), a rate in (k), or a restriction on every possible arithmetic estimate. In particular, (h,k) are held fixed throughout the divergent sequence.

## 5. HD9: the same exact columns in the all-phase and one-phase observations

The full holonomy transform from HG2 is an isometry into the direct integral with phase measure (d\vartheta/(2\pi)). Apply it to the exact column (\mathcal U_k\mathcal V P_N^{u_0}). Using RHD5 gives

\[
 \int\|\mathcal Z_{L,\vartheta}\mathcal U_k\mathcal V P_N^{u_0}\|^2
                \frac{d\vartheta}{2\pi}
 =\Lambda_N^{-1}\longrightarrow0.
 \tag{RHD19}
\]

At the fixed chosen phase, the same sample inequality before dividing by the source norm gives

\[
 \|\mathcal Z_{L,\theta}\mathcal U_k\mathcal V P_N^{u_0}\|^2
 =c_N^*M_{N,\theta}c_N\ge\omega_0.
 \tag{RHD20}
\]

The finite columns have the actual regularity that makes their pointwise phase values meaningful, so RHD19 and RHD20 concern precisely the same source sequence. A direct-integral class is defined modulo null phase sets; it does not carry a canonical bounded evaluation at a fixed phase. If a bounded operator extended the displayed fixed-phase observation from this source domain through that direct integral, RHD19 would force its images to converge to zero in norm, contradicting RHD20. This proves the stated failure of a bounded extension. It does not assert convergence of the fixed-phase images to a particular nonzero vector, nor does it infer nonclosability of this entire vector-valued phase map solely from their positive lower norm; the separate scalar evaluation nonclosability already has the explicit graph limit RHD5.

## 6. Exact factorization through the cyclic quotient and retained primary factors

On the full polynomial space, let (J:\mathbb C[S]\to E=\mathbb C[S]/(\chi)) be the original quotient. If evaluation at (S_0) factors through (J), it must vanish on (\chi\in\ker J), so (\chi(S_0)=0). Conversely, if (\chi(S_0)=0), every element (\chi Q\in\ker J) evaluates to zero. Therefore

\[
 [P]\longmapsto P(S_0)
 \tag{RHD21}
\]

is a well-defined linear and algebra map (E\to\mathbb C), giving exactly the asserted factorization. The polynomial evaluation kernel is the literal principal ideal ((S-S_0)); taking its image in (E) gives the stated kernel ((S-S_0)/(\chi)). This notation uses the ideal inclusion ((\chi)\subseteq(S-S_0)), which follows from the root condition.

If (\chi=(S-S_0)^r q_0) with (q_0(S_0)\ne0), the two factors are coprime, so their actual Chinese-remainder decomposition is

\[
 E\simeq\mathbb C[S]/((S-S_0)^r)\oplus\mathbb C[S]/(q_0).
 \tag{RHD22}
\]

The evaluation of the first component is its constant coefficient after the exact coordinate (x=S-S_0); its kernel is ((x)/(x^r)). The second summand maps to zero: its idempotent equals zero modulo ((S-S_0)^r), hence evaluates to zero at (S_0). The nilpotent coefficients of the first block and the entire cofactor block remain in the source and are precisely recorded in the kernel. Further decomposition of (q_0) into primary factors gives the source statement for all other primary blocks. No multiplicity or cofactor is removed.

If (\chi(S_0)\ne0), the polynomial evaluation still exists and satisfies HD2–HD9, but it sends a vector in (\ker J) to the explicit nonzero scalar (\chi(S_0)). This computes the exact obstruction to factorization; it does not claim that the evaluation observation and the cyclic quotient are unrelated. Their common polynomial source and this kernel calculation specify their relationship.

## 7. Positive support for (k=1) and choice of a phase

For (k\ge2), the positivity argument in Section 1 makes every sample mass positive. For (k=1), zero values can occur at unselected line zeros of (g/h), so HD7 explicitly requires its chosen sample mass to be positive. At a sampled selected root with its full original order, write (h(S)=(S-S_0)^r h_0(S)), where (h_0(S_0)\ne0), and (r=\operatorname{ord}_{S_0}g). Cancelling those exact common factors in the analytic quotient gives the removable value

\[
 (g/h)(S_0)=\frac{g^{(r)}(S_0)}{r!h_0(S_0)}\ne0.
 \tag{RHD23}
\]

This equality retains the full derivative, factorial, cofactor and original phase. Its sampled mass is (omega_0=L^{-1}|(g/h)(S_0)|^2>0). Other zero-mass atoms are quotient zero coordinates in the receiving discrete Hilbert space and do not supply the positive rank-one lower summand RHD14.

For the divergence of (\kappa_{a,N}), no root of (\chi) at a given phase is needed. Since (m>0) almost everywhere, choose any real (u_0) with (m(u_0)>0). For the fixed (L), write (Lu_0=2\pi n_0+\theta) with the unique integer (n_0) and (0\le\theta<2\pi). This supplies a fixed positive sample for RHD17. The argument neither assumes that every one-fold phase contains a selected root nor discards any zero-mass case under a blanket positivity statement.

## 8. HD10: exact source-kernel preimages under the split lift

For a fixed retained label (\lambda), the coefficient map (f:V\to W) lifts to (widetilde f(\lambda,v)=(\lambda,fv)), and external (\tau) maps to external (\tau). The source and target are disjoint unions of their represented coefficient fibres and external absence. Therefore no represented input can map to (\tau), and external absence cannot map to a represented point. In the represented fibre, equality with its zero means exactly (fv=0). Hence

\[
 \widetilde f^{-1}(\{(\lambda,0_W)\})
 =\{(\lambda,v):v\in\ker f\},\qquad
 \widetilde f^{-1}(\{\tau\})=\{\tau\}.
 \tag{RHD24}
\]

These are the precise formulas now stated as HD10. They retain all potentially nonzero source vectors of the kernel, with their original labels. Their images are the receiving represented zero; those images are not mistaken for the source kernel itself. The external inverse image is the separate displayed singleton. The parent corrected the initial imprecise sentence to this exact statement, so the final source has no unresolved type defect.

## Disposition

Accept the corrected complete HD1–10 source at `9a1ba6cd7e8bee67c6d7868c74f2cf4f9d8c11fa255d9d278c7a2420cf0daca6`. The Christoffel/evaluation norm divergence follows from the actual exponential moment and atomless measure via the fully proved transform uniqueness argument. Its minimum-polynomial coefficients and all-phase/single-phase observations are exact. The positive sample lower bound forces divergence of the actual fixed-exponent weighted comparison constant with (N), at fixed (h,k), and gives the stated period-length constraint for that estimate. The cyclic quotient factorization and all primary kernels are explicit, and HD10 fixes the final split-lift type statement with exact preimages.

The source proof and this review make no claim to have evaluated the source Grams numerically or obtained a tensor-degree rate. They preserve all original maps and constants and provide the full fixed-cutoff-degree result, including its exact limitations and morphisms.
