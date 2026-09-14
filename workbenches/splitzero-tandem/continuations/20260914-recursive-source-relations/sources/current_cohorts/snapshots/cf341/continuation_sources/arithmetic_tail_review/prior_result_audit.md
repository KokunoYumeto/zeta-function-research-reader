# Bounded audit of prior arithmetic norm results

Date: 2026-09-13. Read-only review of inherited mathematical sources; this report is the only file written by this audit.

## Finding and scope

The reviewed inherited results do not prove the proposed actual convolution estimate

\[
\log\omega_{h,k,n}
=\log\!\bigl(\sqrt2\,n!\Gamma(n+\tfrac12)\bigr)
 +O_h\!\bigl(k+\log(n+1)\bigr),
\]

or the resulting limit \((\omega_{h,k,i+q}/\omega_{h,k,i})^{1/(2q)}/q\to4/e\), with \(i=q-1,q\) and \(q=[1+k(m-1)](k+1)^2\). The proposed estimate is strictly stronger than the actual norm bounds proved in the reviewed sources. This is a comparison with the stated target, not a verification of its new proof.

All source paths below are relative to `output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/`. The audit read the complete `consecutive_first_window_join.tex`; an independent subreview read all of `theta_gamma_reference.tex`. It read the identified Schur, norm, and volume statements with their complete local proofs in the other files. Filename inventory and targeted text searches covered this TeX directory; those searches do not establish completeness of other repositories, all dependencies, or unreviewed chapters. Neither `window_schur_transport.tex` nor `arithmetic_norm_control.tex` occurs in the supplied snapshot's filename inventory. The matching retained content is in `endpoint_product_sharpening.tex` and `consecutive_first_window_join.tex`.

## 1. Actual comparable norm windows already proved

`consecutive_first_window_join.tex:258–340`, equations CJ.15–CJ.19, is the closest result. It retains the actual density \(m_{h,k}=w_h^{*k}\), \(w_h=|(g/h)(1/2+it)|^2/(2\pi)\), and the monic polynomial space on \(S=k/2+iu\), as defined at lines 23–35.

* CJ.15, lines 260–268, uses the positive convolution lower envelope
  \[
  m_{h,k}(u)\ge c_h\vartheta_h^{k-3}
  e^{-(\pi/2)(k-3+|u|)}(k-2+|u|)^{-B},\qquad B=42+2\deg h.
  \]
* CJ.16–CJ.17, lines 269–283, define literal constants \(\ell_h,U_h>0\) and prove
  \[
  (\ell_h n)^{2n}\le\omega_{h,k,n}\le(U_h n)^{2n},\qquad n\ge k\ge3.
  \]
  The full local proof is lines 285–313. The lower estimate restricts the retained integral to \([-n,n]\), uses the exact monic Legendre minimum, and bounds the retained envelope factors. The upper estimate uses the monic trial polynomial \((S-k/2)^n\), the two original Laplace values, and \((2n)!\). This calculation is a complete coarse estimate, not a Gamma comparison with a sharp linear term.
* CJ.18, lines 315–331, divides these norm estimates to obtain
  \[
  (\omega_{h,k,n+r}/\omega_{h,k,n})^{1/(2r)}\le C_h^{\rm win}n,
  \qquad n\ge k\ge3,\quad n/2\le r\le2n.
  \]
  It explicitly applies this to both retained windows \((i,j)=(q-1,2q-1),(q,2q)\). The proof gives a finite constant, not its limiting value.

Taking logarithms of CJ.17 proves exactly
\[
2n\log n+2n\log\ell_h\le\log\omega_{h,k,n}
\le2n\log n+2n\log U_h.
\]
Thus the existing result gives \(\log\omega_{h,k,n}=2n\log n+O_h(n)\), uniformly in its admitted \(n,k\) range. Its undetermined linear error does not determine the coefficient \(-2n\) in the claimed Gamma main term.

`endpoint_product_sharpening.tex:634–654`, EP.39–EP.40, records the earlier doubled-window bound \((\omega_{h,k,2n}/\omega_{h,k,n})^{1/(2n)}\le C_h n\), with the literal sufficient constant and an explicit attribution to the accompanying arithmetic endpoint proof. Lines 813–829, EP.50a–EP.50b, record the balanced extension \(n/2\le r\le n\), again with an explicit constant and an attribution to its complete source proof. These passages do not locally prove a sharper asymptotic; CJ supplies a complete local proof of the stronger admitted window range above. `research_conclusion.tex:1326–1347` reports these same results as R42, rather than a further asymptotic theorem.

## 2. Exact Schur transport already proved

`endpoint_product_sharpening.tex:370–457`, EP.32–EP.38, proves a triangular source-coordinate map with determinant one, the positive Schur complement, the full remainder-map update, and the exact determinant identities
\[
\omega_N=\mathfrak D_{N+1}/\mathfrak D_N,
\quad V_N=\mathfrak D_{N+1}/\mathfrak B_{N-q+1},
\quad\Lambda_N=\mathfrak B_{N-q+1}/\mathfrak D_N.
\]
The proof retains both source and relation determinants. It expresses the original norm ratios through actual Schur blocks; it does not estimate the asymptotic growth of those blocks. These are exact maps available to receive the new norm estimate, not a pre-existing proof of that estimate.

## 3. Arithmetic volume upper bounds already proved

`arithmetic_volume_upper_route.tex:148–236`, AU.10–AU.15, retains the same positive convolution lower envelope, explicitly evaluates the comparison moments by a positive integral, and proves the identity-on-polynomials contraction to the comparison measure. Minimization on identical affine remainder fibres gives the finite higher-volume comparison AU.14. The envelope's underlying analytic derivation is attributed to the supplied arithmetic endpoint source; the local comparison proof is fully written here.

Lines 263–318, AU.17–AU.20, prove a second finite determinant bound from the two original Laplace values by Cauchy–Schwarz and positive-matrix inversion. Lines 363–510, AU.24–AU.29, prove the scalar Hermitian upper comparison using the exact affine-coordinate transport, Legendre coefficient bound, original monic remainder map, and the retained density on an interval. Lines 513–581, AU.30–AU.33, derive
\[
0\le\log(V_q/V_{2q-1})
\le(\alpha D+\log256)q^2+O_h(kq+q\log(q+1)),\qquad\alpha=\pi/2,
\]
with the full constants displayed in AU.31. AU.33 computes the positive quadratic gap between these explicit upper and lower estimates. Line 581 explicitly states that no upper asymptotic for the sharper comparison determinants is inserted. These are quotient-volume results; none of the reviewed proofs identifies the sharp asymptotic of the actual monic norms.

## 4. Exact fixed Gamma reference already proved

`theta_gamma_reference.tex:77–189`, TG.7–TG.14, derives the generating integral, justifies coefficient extraction using exponential integrability, proves monicity and orthogonality, and obtains
\[
\gamma_n^{(\lambda)}=2^{1-2\lambda}n!\Gamma(n+2\lambda),
\qquad\gamma_n=\sqrt2\,n!\Gamma(n+\tfrac12)
\]
for precisely \(d\sigma_{1/4}(u)=|\Gamma(1/4+iu/2)|^2du/(2\pi)\). TG.14 is at lines 184–189. Thus the proposed main term, including its literal constant and coordinate scale, is inherited exactly.

Lines 235–277, TG.16–TG.17, prove the actual one-copy identities
\[
\mathfrak h_n=\gamma_nD_n/D_{n-1},\qquad
\kappa_n^{(h)}=\gamma_nD_n^{(h)}/D_{n-1}^{(h)}.
\]
Their proof uses triangular monic basis changes and the exact affine phase. It supplies no growth estimate for the determinant quotients. The chapter does not prove a uniform convolution-norm asymptotic for varying \(k\).

Lines 410–416 explicitly distinguish the cited expansion-coefficient asymptotics from an estimate of these arithmetic determinants. Lines 439–487 prove an obstruction to specified exponential-weight hypotheses for the unsmoothed packet multiplier using its infinitely many retained real zeros, and expressly leave other asymptotic methods available. That argument makes no obstruction claim for the positive convolution density.

## Exact improvement represented by the stated target

The existing CJ bounds leave an \(O_h(n)\) logarithmic error. The stated target replaces that error by \(O_h(k+\log(n+1))\). In the requested quartet regime, \(q\ge(k+1)^2\), so \((k+\log(q+1))/q\to0\). It therefore fixes a term that CJ.17 leaves undetermined.

The origin of the proposed constant is precise: TG.14 and the Gamma recurrence give
\[
\gamma_n=\sqrt{2\pi}\,(2n)!/4^n,
\qquad\log\gamma_n=2n\log n-2n+O(\log(n+1)).
\]
For the second equality no sharp Stirling remainder is needed: monotonicity of \(\log x\) gives, for each integer \(N\ge1\),
\[
N\log N-N+1\le\log N!\le N\log N-N+1+\log N.
\]
Apply this at \(N=2n\) in the preceding exact factorial identity.
For \(i=q\) and separately \(i=q-1\), this yields
\[
\frac{\log\gamma_{i+q}-\log\gamma_i}{2q}
=\log q+\log4-1+O(\log(q+1)/q).
\]
The stated new error contributes \(O_h((k+\log(q+1))/q)\) to this equation for the actual norm quotient, producing the claimed \(4/e\) limit. None of the reviewed prior norm inequalities fixes this constant. This comparison does not assert an upper estimate on the original quotient-volume correction, an off-critical zero, or a contradiction.
