# Complete Original Gamma Return

*An exact positive product for the universal Gamma centre — 14 September 2026*

Read [the complete 15-page paper](Complete_Gamma_Return.pdf). It prints the accepted LET1–21, PHT1–23 including PHT17a, and HCT1–39 proof bodies, retaining all 84 original equation tags. LET supplies the low-endpoint comparison; PHT gives the parity and weighted-Toda maps; HCT provides the positive contiguous recurrence and determinant reconstruction.

“Complete” refers to this full new proof cut and its complete Gamma reference. The PDF does not reprint the entire receiving/dependency tree, which accompanies it as editable source. No leading asymptotic value, improved arithmetic allowance, or Riemann-hypothesis conclusion is asserted.

## Original family and moments

Retain integers \(l,m\ge1\) and parameters

\[
 k=4l+1,\quad e=1+k(m-1),\quad q=e(k+1)^2,\quad
 c=k/2,\quad 0<\delta<1/2,\quad\gamma>2,
\]
\[
 \chi(S)=\prod_{a,b=0}^{k}
 [S-c-(2a-k)\delta-i(2b-k)\gamma]^e,\qquad
 f(S)=\prod_{j=0}^{l-1}(S-c-2j-1/2).
\]

The source remains
\(\sigma(y)=|\Gamma(1/4+iy/2)|^2/(2\pi)\), evaluated at \(S=c+iy\). The original quotient, complete primary jets, source mass, unit multiplications, mixed cross Grams, support faces, and contour orientations remain in the supplied interfaces.

Define literal moments and the even-moment Hankel determinants by

\[
 m_j=\int_{\mathbb R}y^j\sigma(y)\,dy,\qquad
 \mu_j=m_{2j},\qquad
 H_n^{(a)}=\det[\mu_{a+i+j}]_{i,j<n},\quad H_0^{(a)}=1.
\]

The two sheets \(y=\pm\sqrt t\) together give the positive-axis measure
\(d\nu(t)=\sigma(\sqrt t)\,dt/\sqrt t\), with full mass \(\sqrt{2\pi}\). The parity map retains the original coordinate coupling

\[
 M_y\longleftrightarrow\begin{pmatrix}0&M_t\\I&0\end{pmatrix}.
\]

The supplied weighted maps also retain the off-diagonal terms of the linear-tilt Gram. The even-moment index \(\mu_j\) here means the literal moment \(m_{2j}\); the complete receivers preserve this dictionary.

## The universal centre and its positive product

For the original even integer \(q\), put \(n=q/2\) and

\[
 Z_a=H_n^{(a)}H_{n+1}^{(a)}(H_n^{(a+1)})^2,\qquad
 D_{l,N}=\prod_{a=0}^{N}\prod_{j=0}^{2l-1}(a+j+1/2),
\]
\[
 P_k=\log D_{l,q-1}+\log D_{l,q}
      -\log D_{l,2q-1}-\log D_{l,2q}.
\]

The two high reference determinants, at original relation ranks \(q\) and \(q+1\), combine to \(Z_{q+l}/Z_q\). The low reference is \(H_1^{(q+l)}/H_1^{(q)}\). The complete centre is therefore the logarithm

\[
 W_k=P_k+\log(Z_{q+l}/Z_q)
             -\log(H_1^{(q+l)}/H_1^{(q)}).
\]

All original Gamma mass factors remain in the determinants before their proved cancellation. HCT supplies the initial data

\[
 c_j^{(0)}=(2j+1)(2j+1/2),\qquad
 d_j^{(0)}=2j(2j-1/2).
\]

At each shift \(a\to a+1\), use the auxiliary variable \(\eta_j\), distinct from the packet multiplicity \(e\):

\[
 \eta_0=c_0^{(a)},\quad d_0^{(a+1)}=0,\quad
 c_0^{(a+1)}=\eta_0+d_1^{(a)},
\]
\[
 \eta_j=\frac{c_j^{(a)}\eta_{j-1}}{\eta_{j-1}+d_j^{(a)}},\qquad
 d_j^{(a+1)}=\frac{c_j^{(a)}d_j^{(a)}}{\eta_{j-1}+d_j^{(a)}},\qquad
 c_j^{(a+1)}=\eta_j+d_{j+1}^{(a)}\quad(j\ge1).
\]

Every denominator is positive. The full finite-array endpoint rules and source maps are given in HCT. At the original indices \(n=q/2\) and shifts \(a=q,\ldots,q+l\), the exact positive product is

\[
 \exp W_k=
 \frac{D_{l,q-1}D_{l,q}}{D_{l,2q-1}D_{l,2q}}
 \prod_{s=0}^{l-1}
 \frac{
  (\prod_{j=0}^{n-1}c_j^{(q+s)})
  (\prod_{j=0}^{n}c_j^{(q+s)})
  (\prod_{j=0}^{n-1}c_j^{(q+s+1)})^2}
 {c_0^{(q+s)}}.
\]

This retains the high determinant blocks, low scalar denominator, and all four signed \(D\)-products. Finite positivity and exact recurrence do not by themselves evaluate the product along the growing family.

## Signed enclosure and its precise scope

The inherited full-source estimates include the inner interval, bulk, and both far tails. Their stated bulk is \(q\epsilon\le|y|\le64q\), with \(\epsilon=2^{-10}\) and sufficient threshold \(k\ge2048\sqrt{\delta^2+\gamma^2}\). LET separately proves the low scalar comparison, including the case where the multiplier degree \(l\) exceeds the scalar rank one.

The high-error sum lies in \([-A,B]\), where

\[
 A=2E_{\chi,l}+2(L_q+L_{q+1}),\qquad
 B=A+(2q+1)\Delta_f.
\]

Here \(E_{\chi,l}\), \(L_r\), and \(\Delta_f\) are the supplied finite density, tail, and one-sided multiplier allowances. LET's low error lies in \([-a_0,b_0]\), with its complete constants and four-tail decomposition. Its contribution reverses sign in the complete functional:

\[
 W_k-A-b_0\le\mathfrak T_k\le W_k+B+a_0,
\]
\[
 -W_k-B-a_0\le R_k^0-R_k^\sigma=-\mathfrak T_k
 \le-W_k+A+b_0.
\]

For each fixed original packet and multiplicity, the total Gamma comparison error is \(O(k)=o(q)\), and it is \(O(1)\) for a fixed original packet with fixed \(m\ge2\). For a fixed original packet, the low comparison error is \(O(1)\) for \(m=1\) and \(O(k^{-1})\) for fixed \(m\ge2\). The finite constants and threshold retain \(\delta,\gamma\).

Crucially, the previous exact-low centre satisfies

\[
 H_k^*=-W_k+e_0,\qquad e_0\in[-a_0,b_0].
\]

Consequently the new universal interval contains the earlier interval
\([H_k^*-B,H_k^*+A]\). Adding it to the existing finite intersection does **not** tighten the exact-input Gamma, arithmetic, or HC endpoints. The new content is the universal positive product with controlled growing-family error. The complete receivers preserve the earlier exact-low, deformed-bulk, and finite-trace intervals and all outside-threshold branches.

The original arithmetic correction remains \(\delta_\sigma\in[-a_-,a_+]\), with its existing asymmetric finite majorants. The signed identity is \(\Delta_\Gamma=\delta_\sigma-\mathfrak T_k\), and the direct receiving bound is

\[
 B_0-W_k-B-a_0-a_-\le B_{\rm ar}
 \le B_0-W_k+A+b_0+a_+.
\]

The HC residual still subtracts the original \(4q\log(D_hk)\), retaining its source, constants, and nonnegativity.

## Remaining calculation and source guide

The remaining task is to evaluate this positive product at the original growing indices, with finite remainders preserving every term that survives at order \(q\) after the \(D\)-product cancellations. The result must then return through the unchanged arithmetic and cohomology maps, with any smaller accuracy scale justified by that receiver. This delivery supplies the exact object and comparisons, not its leading asymptotic value or an endpoint conclusion.

- [Main LaTeX entry point](Complete_Gamma_Return.tex), [LET](sources/LET.tex), [PHT](sources/PHT.tex), and [HCT](sources/HCT.tex) form the complete printed closure. The three complete [author documents](originals/) and [source-transport record](SOURCE_TRANSPORTS.json) preserve their lineage.
- The [67-file current receiving tree](dependencies/complete_gamma_receiving/README.md) includes the full [NOTE](dependencies/complete_gamma_receiving/CURRENT_JOINT_SCHUR_NOTE.tex), [JSR](dependencies/complete_gamma_receiving/SIGNED_RETURN_RECEIVER.tex), and [WRC1–7 body](dependencies/complete_gamma_receiving/spans/W_RECEIVING_PROOF.tex), embedded once in JSR, together with providers and exact predecessors.
- The [68-file preceding receiving tree](dependencies/current_receiving/README.md), [complete bulk proof providers](dependencies/bulk_sources/), and [preceding Joint-Schur textual dependencies](dependencies/joint_schur_previous/) retain the earlier mathematical interfaces. The latter copy omits inventoried duplicate media, not mathematical source bodies.

The final delivery records complete LET/PHT/HCT acceptance, WRC receiving acceptance, and completed review of the final 15-page PDF. These are inherited records, not new proof, archive, PDF, or Lean checks performed for this guide. Earlier sealed readers retain their own historical source cuts and are not replaced or relabelled by this supplement.
