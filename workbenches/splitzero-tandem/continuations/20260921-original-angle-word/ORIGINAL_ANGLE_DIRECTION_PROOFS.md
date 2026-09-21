# Direction of the complete original projection-angle spectrum

21 September 2026. This calculation strengthens AS40–43: the total downward movement of the centered logarithmic spectrum tends to zero over the entire original cutoff window. It keeps every invariant row and every lower-root constraint. The result gives an ordering of the remaining endpoint statistics; it does not evaluate their native arithmetic value.

## AD1. Original objects and the two positive increments

Use precisely the objects and finite guards of AS1–5. In particular, the fixed original row space has dimension
\[
r=8k-32-v+s_k>0,\qquad q=(k+1)^2,
\quad q'=(k-7)^2,\qquad c'=k/2-4.
\]
The full physical Gamma measure, its mass and its monic polynomial norms are
\[
d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy,
\quad M_\sigma=\sqrt{2\pi},\quad h_n=M_\sigma n!(1/2)_n.
\]
For every integer \(q-1\le N\le2q\), retain the complete lower ideal and the full invariant functional matrix. Their two covariances on the same fixed row space are
\[
C_N=W_NP_NW_N^*,\qquad B_N=W_NW_N^*,\qquad
P_N=I-E_N^*(E_NE_N^*)^{-1}E_N.
\tag{AD1}
\]
Here \(E_N\) evaluates at all original lower roots in the original orthonormal Gamma basis, and \(W_N\) is the fixed functional family restricted to degree \(N-v\). The full-root interpolation proof in AS4 gives the displayed projection, and AS10 gives \(C_N>0\). Thus \(0<C_N\preceq B_N\).

Append the actual next columns \(e_N,w_N\). RX4–8 proves, with the complete weighted source and the physical phase,
\[
a_N=\frac{w_N-W_NE_N^*(E_NE_N^*)^{-1}e_N}
{\sqrt{1+e_N^*(E_NE_N^*)^{-1}e_N}},
\qquad b_N=w_N,
\]
\[
C_{N+1}=C_N+a_Na_N^*,\qquad
B_{N+1}=B_N+b_Nb_N^*.
\tag{AD2}
\]
In weighted monic coordinates the very same column is
\(a_N=i^{-(N-v+1)}f_{N-v-q'+1}/\sqrt{\nu_{N-v-q'+1}}\).
The phase disappears from its outer product only after this vector identity has been proved. No new source measure or freely chosen row enters AD2.

## AD2. A one-step inequality with its direction retained

Write \(s_{1,N}\ge\cdots\ge s_{r,N}>0\) for the generalized eigenvalues of \((C_N,B_N)\). Let \(t_{1,N}\ge\cdots\ge t_{r,N}\) be those of \((C_{N+1},B_N)\). Generalized min–max follows by applying the usual finite-dimensional variational formula to \(B^{-1/2}CB^{-1/2}\). Its Rayleigh quotient is \(z^*Cz/(z^*Bz)\). AD2 therefore gives, for every ordered index including repeated eigenvalues,
\[
t_{j,N}\ge s_{j,N},\qquad t_{j,N}\ge s_{j,N+1}.
\tag{AD3}
\]
If \(s_{j,N+1}<s_{j,N}\), then
\(\log s_{j,N}-\log s_{j,N+1}\le\log t_{j,N}-\log s_{j,N+1}\).
If the strict inequality fails, the positive part on the left is zero while the right is nonnegative. The other direction is proved with the two s terms exchanged. Summing and using the products of generalized eigenvalues proves
\[
\begin{aligned}
\sum_{j=1}^r(\log s_{j,N}-\log s_{j,N+1})_+
&\le\log\frac{\det B_{N+1}}{\det B_N},\\
\sum_{j=1}^r(\log s_{j,N+1}-\log s_{j,N})_+
&\le\log\frac{\det C_{N+1}}{\det C_N}.
\end{aligned}
\tag{AD4}
\]
This proves two directed inequalities, not just their sum AS40. The determinant lemma also evaluates their allowances exactly as
\(\log(1+b_N^*B_N^{-1}b_N)\) and
\(\log(1+a_N^*C_N^{-1}a_N)\), respectively. To prove that lemma, conjugate by the positive square root: the rank-one matrix has one nonunit eigenvalue \(1+u^*H^{-1}u\) and all others one.

## AD3. The whole original window has negligible downward movement

Put \(\ell_k=\log(q/k)\),
\[
x_{j,N}=q^{-1}\log s_{j,N}+2\ell_k,
\qquad \mu_{k,N}=r^{-1}\sum_{j=1}^r\delta_{x_{j,N}}.
\tag{AD5}
\]
This centers a spectral observable; AD1 and the physical metrics are unchanged. Let
\[
V_k^-=\frac1r\sum_{N=q-1}^{2q-1}\sum_j
(x_{j,N}-x_{j,N+1})_+,\qquad
V_k^+=\frac1r\sum_{N=q-1}^{2q-1}\sum_j
(x_{j,N+1}-x_{j,N})_+.
\]
AD4 telescopes exactly:
\[
0\le V_k^-\le\frac{\log\det B_{2q}-\log\det B_{q-1}}{rq}
\le\varepsilon_k^B:=\frac{K_{q-1}+K_{2q}}{rq}
=O_{h,A}\!\left(\frac{\log(q+2)}k\right).
\tag{AD6}
\]
The \(K_N\) are the explicit AS41 constants proving
\(|\log(\det B_N/\det R_Z)|\le K_N=O(q\log(q+2))\).
The fixed \(R_Z\) cancels. In particular this is a bound on the sum of all downward movements over all q+1 steps; it has no extra factor q.

Subtracting the positive and negative parts of each real increment gives
\[
V_k^+-V_k^-=\bar x_{2q}-\bar x_{q-1},\qquad
\bar x_N=r^{-1}\sum_jx_{j,N}.
\tag{AD7}
\]
Ordered pairing realizes the Wasserstein distance on the real line: uncrossing a crossed pair cannot increase its absolute-distance sum, so a finite sequence of uncrossings gives ordered pairing. Hence
\[
0\le
\sum_{N=q-1}^{2q-1}W_1(\mu_{k,N+1},\mu_{k,N})
-(\bar x_{2q}-\bar x_{q-1})
=2V_k^-\le2\varepsilon_k^B.
\tag{AD8}
\]
AS43's complete path-length bound has thus been sharpened to its exact endpoint increase with an error tending to zero. The endpoint increase itself remains a native arithmetic quantity.

## AD4. Every increasing spectral observable has the same direction

Let f be any increasing real function of Lipschitz constant at most one, and set \(F_N=r^{-1}\sum_j f(x_{j,N})\). Pairing the ordered indices and using
\((f(x)-f(y))_+\le(x-y)_+\) proves
\[
\sum_{N=q-1}^{2q-1}(F_N-F_{N+1})_+
\le V_k^-\le\varepsilon_k^B.
\tag{AD9}
\]
Thus for every pair of actual cutoffs \(N_1\le N_2\),
\[
\int f\,d\mu_{k,N_1}\le\int f\,d\mu_{k,N_2}+\varepsilon_k^B.
\tag{AD10}
\]
The statement is simultaneous for all these f, including clipped linear functions and smooth increasing approximations to thresholds. A discontinuous threshold has no Lipschitz constant one, and is not silently included in the finite error.

There is also an exact nondecreasing comparison at every ordered index. Define
\(\widehat x_{j,N}=\max_{q-1\le M\le N}x_{j,M}\).
Both N-monotonicity and the ordering in j are immediate. If M realizes the maximum, subtracting all subsequent increments gives
\[
0\le\widehat x_{j,N}-x_{j,N}
\le\sum_{M=q-1}^{N-1}(x_{j,M}-x_{j,M+1})_+.
\]
For \(\widehat\mu_{k,N}=r^{-1}\sum_j\delta_{\widehat x_{j,N}}\), ordered matching now proves
\[
\sup_{q-1\le N\le2q}
W_1(\widehat\mu_{k,N},\mu_{k,N})\le\varepsilon_k^B.
\tag{AD11}
\]
This is an explicitly defined comparison of spectral data. It does not replace \(C_N\), \(B_N\), the original quotient map or its current. It records the entire finite defect in monotonicity and bounds that defect using the actual unprojected row increments.

## AD5. Exact relation to the determinant extraction

For \(l_i=q-1+i\), \(u_i=2q-1+i\), RX9–11 gives the actual innovation matrix \(X_i=C_{l_i}^{-1/2}[a_{l_i},\ldots,a_{u_i-1}]\) and
\(G_i=\log\det(I+X_iX_i^*)\). Determinants of generalized eigenvalues then give the exact identity
\[
rq(\bar x_{u_i}-\bar x_{l_i})
=G_i-\log\frac{\det B_{u_i}}{\det B_{l_i}},
\qquad i=0,1.
\tag{AD12}
\]
Thus the complete directed spectrum, the bounded selected-column extraction and the weighted-source innovations have the same original endpoint statistic. No identification of a projected direction with an arbitrarily chosen source direction is needed. Combining AD12 with RX17 gives
\[
\left|\mathcal K_k-\log\mathcal A_{k,v}
+rq\sum_{i=0}^1(\bar x_{u_i}-\bar x_{l_i})\right|
\le\mathcal E_k+\sum_{i=0}^1(K_{u_i}+K_{l_i}).
\tag{AD13}
\]
All four original signs remain. The right-hand side is \(O(q\log(q+2))=o(kq)\). This version uses the exact rational Gamma reference of CI24 and the finite comparison of FI1–17; it does not require the separate high-endpoint equilibrium asymptotic. It supplies a stronger finite receiver for AS54 while preserving the status of the latter's inherited scalar-profile input.

## AD6. The entire directed path for both original source orders

For the second original order-k Gamma source, retain its full physical mass. AS44–45 proves, with \(k=4\ell+1\),
\[
a_k\|p\|_\sigma^2\le\|p\|_{m_k}^2\le b_{k,2q}\|p\|_\sigma^2
\quad(\deg p\le2q),
\]
\[
\begin{aligned}
\beta_k&=(2\pi)^{k/2}/(\sqrt2\Gamma(k/2)),\\
a_k&=\beta_k\prod_{j<\ell}(2j+1/2)^2,\\
b_{k,2q}&=\beta_k\prod_{j<\ell}[2(2q+j+1)+2j+1/2]^2.
\end{aligned}
\]
These constants are the two actual Gamma-source constants, separate from the arithmetic-source constants in FI1. Set
\(J_k=\max(|\log a_k|,|\log b_{k,2q}|)\).
The exact half-integer identity
\(\Gamma(k/2)=(4\ell)!\sqrt\pi/[4^{2\ell}(2\ell)!]\), together with \(0\le\log(n!)\le n\log(n+1)\), gives \(J_k=O(k\log(q+2))\) directly; both finite products satisfy the same bound by bounding each displayed logarithm.

Taking suprema in the definition of the norm of every fixed row reverses the source inequalities. It follows that
\(b_{k,2q}^{-1}B_N^{(1)}\preceq B_N^{(k)}\preceq a_k^{-1}B_N^{(1)}\), and hence
\[
\left|\log\frac{\det B_N^{(k)}}{\det R_Z}\right|
\le K_N+rJ_k.
\]
For fixed k the order-k source itself is unchanged as N increases. Its full ideals and unrestricted source spaces are nested and each adds one orthogonal direction, so AD2–4 applies directly to this source's own two covariance increments. Consequently
\[
V_k^{-,(k)}\le\varepsilon_k^B+\frac{2J_k}{q}
=O_{h,A}(\log(q+2)/k)\longrightarrow0.
\tag{AD14}
\]
Thus AD8–11 holds for the entire order-k path with this explicit new allowance. The proof uses its actual source increments. A comparison at each separate cutoff alone would not justify summing q+1 such errors, and is not used here.

## Sources and scope

The actual full-root covariance is the one proved in [CGP2–11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/010/ORIGINAL_PROJECTION_CAUCHY_ACTION.tex). The complete adjacent source maps are [ACC17–22](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/010/ORIGINAL_ADJACENT_CUTOFF_CURRENT.tex). AS1–64, RX1–20 and the complete FI/CI/CL sources accompany this continuation with their fixed published proof links below.

The Gamma polynomial conventions are documented by T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, [DLMF 18.22.8](https://dlmf.nist.gov/18.22.E8) and [18.23.7](https://dlmf.nist.gov/18.23.E7); the retained original equation TeX was read in the source ledger. The order, rank-one determinant and one-dimensional pairing arguments needed here are proved in full above. A finite auxiliary checker tests AD2–4 and AD6–13 without treating its freely specified evaluation rows as native period data.


The preceding complete proofs are published at a fixed edition: [FI1–17; FR1–4](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/FINITE_INVARIANT_PROOFS.md), [CI1–26; CL1–18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/CUTOFF_INNOVATION_PROOFS.md), [IC1–42](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/COLLISION_PROOFS.md). All original source versions and human citations are retained in the accompanying source bank.
