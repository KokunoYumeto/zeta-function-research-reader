# Original Relation Bulk Control

*Full-source Gamma comparison and the signed arithmetic receiver — 14 September 2026*

Read [the complete 33-page paper](Original_Relation_Bulk_Control.pdf). This supplement controls the two original high relation-Gram ratios over their full integration domains and compares them with explicitly specified Gamma Hankel determinants. Its five complete proof bodies cover the bulk density, independent inner and far-tail estimates, the degree-\(l\) contrast calculation, and the receiving application.

The result is a quantitative comparison, not an asymptotic evaluation of the remaining growing determinants. It does not improve the separate arithmetic residual estimate or establish a conclusion about the Riemann hypothesis.

## The original family and source

The parameter domain is

\[
 k=4l+1,\quad l\ge1,\quad m\ge1,\quad e=1+k(m-1),\quad
 q=e(k+1)^2,\quad c=k/2,\quad 0<\delta<1/2,\quad\gamma>2,
\]

where \(l,m\) are integers. The full quartet-sum polynomial and original degree-\(l\) multiplier are

\[
 \chi(S)=\prod_{a,b=0}^{k}
 [S-c-(2a-k)\delta-i(2b-k)\gamma]^e,
 \qquad
 f(S)=\prod_{j=0}^{l-1}(S-c-2j-1/2).
\]

The Gamma source has density

\[
 \sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi},
 \qquad \int_{\mathbb R}\sigma(y)\,dy=\sqrt{2\pi}.
\]

All Grams use \(S=c+iy\) in this density. At \(N=q+r-1\), the original relation determinant is

\[
 \mathfrak R_{q+r-1}
 =\frac{\det\operatorname{Gram}_{\sigma}(f\chi S^j)_{j<r}}
 {\det\operatorname{Gram}_{\sigma}(\chi S^j)_{j<r}},
 \qquad r=q,\ q+1.
\]

These are the distinct high cutoffs \(2q-1\) and \(2q\). Both ranks, all confluent multiplicities, source mass, coefficient maps, original arithmetic quotient, units, and mixed covariance are retained.

## What the comparison proves

The three-region estimates cover the entire real line: the inner interval \(|y|<q\epsilon\), bulk \(q\epsilon\le|y|\le64q\), and both far tails \(|y|>64q\), with \(\epsilon=2^{-10}\). Their explicit sufficient threshold is
\(k\ge2048\sqrt{\delta^2+\gamma^2}\). The exact tail corrections are retained before applying their bounds; no region is declared negligible without its supplied estimate.

The contrast proof constructs the original-metric projectors for degree-at-most-\(r-1\) polynomials and their multiples by \(f\). Their intersection has dimension \(r-l\); the projector difference has rank \(2l\), with its full cross-Gram spectral frame retained. For a bounded real density change \(w\mapsto e^\psi w\), it proves

\[
 |\log\mathcal R_{e^\psi w}(f)-\log\mathcal R_w(f)|
 \le l\,\operatorname{osc}_w\psi,
\]

where \(\mathcal R_w(f)\) is the corresponding complete Gram determinant ratio and \(\operatorname{osc}\) is the essential range width. Thus the coefficient is the multiplier degree \(l\), although each Gram has \(r\) columns.

The full-source reference is explicit:

\[
 (\mathsf M_{a,r})_{ij}
 =\int_{\mathbb R}y^{2a+i+j}\sigma(y)\,dy\quad(0\le i,j<r),
 \qquad
 \mathcal H_{q,l,r}=\frac{\det\mathsf M_{q+l,r}}{\det\mathsf M_{q,r}}.
\]

The proved comparison is

\[
 -E_{\chi,l}-2L_r
 \le\log\mathfrak R_{q+r-1}-\log\mathcal H_{q,l,r}
 \le E_{\chi,l}+r\Delta_f+2L_r,
 \qquad r=q,q+1.
\]

Here \(E_{\chi,l}\) is the explicit degree-\(l\) density allowance, \(\Delta_f\) the nonnegative multiplier allowance, and \(L_r\) the explicit inner/far-tail allowance defined in the paper. The proof keeps four separate tail logarithms with signs \((+,-,-,+)\). The multiplier error appears only on the upper side.

For each fixed original quartet and multiplicity, the comparison error is \(O(k)=o(q)\); for each fixed original quartet with fixed multiplicity \(m\ge2\), it is \(O(1)\). These statements concern the comparison error, not the size or asymptotic value of the Hankel determinants. The real-\(y\) Hankel formula has no additional \(2lr\log q\) term: the scaling factors belong to the earlier bulk-coordinate presentation and must not be counted twice. Original mass factors are retained before cancellation.

## Exact signed return and arithmetic use

The low-endpoint data remain exact:

\[
 D_{l,N}=\prod_{a=0}^{N}\prod_{j=0}^{2l-1}(a+j+1/2),\qquad
 \mathfrak r_\chi=\frac{\int|f\chi|^2\,d\sigma}{\int|\chi|^2\,d\sigma},
\]
\[
 C_{\rm rel}=\log D_{l,q-1}+\log D_{l,q}-\log\mathfrak r_\chi
 -\log D_{l,2q-1}-\log D_{l,2q}.
\]

The exact signed identity is

\[
 \mathfrak T_k=C_{\rm rel}+\log\mathfrak R_{2q-1}
 +\log\mathfrak R_{2q},\qquad
 R_k^0-R_k^\sigma=-\mathfrak T_k,\qquad
 \Delta_\Gamma=\delta_\sigma-\mathfrak T_k.
\]

Define the specified centre and allowances by

\[
 V_k=C_{\rm rel}+\log\mathcal H_{q,l,q}+\log\mathcal H_{q,l,q+1},
\]
\[
 A_k=2E_{\chi,l}+2(L_q+L_{q+1}),\qquad
 B_k=A_k+(2q+1)\Delta_f.
\]

Then \(R_k^0-R_k^\sigma\in[-V_k-B_k,-V_k+A_k]\). Negation places the one-sided multiplier term in the lower Gamma allowance. The complete receiving sources intersect this interval with the existing bulk and exact-low trace intervals; below the stated full-source threshold, the exact-low trace interval remains available.

The unchanged arithmetic allowances are
\(a_-=\Xi_{k,q-1}+\Xi_{k,q}\) and
\(a_+=\Xi_{k,2q-1}+\Xi_{k,2q}\), with
\(\delta_\sigma\in[-a_-,a_+]\). Consequently,

\[
 B_{\rm ar}\in
 [B_0-V_k-B_k-a_-,\ B_0-V_k+A_k+a_+].
\]

Their existing finite majorants, asymmetric constants, and separate simple-quartet regime remain in force. The original HC residual is still \(B_{\rm ar}-4q\log(D_hk)\), with its original \(D_h\).

## What remains, and where to read

The next specified calculation is to evaluate the two Hankel ratios at the actual joint growth \(r=q,q+1\), \(q=e(k+1)^2\), \(l=(k-1)/4\), together with the unchanged low moment ratio and products in \(C_{\rm rel}\). It must retain the finite remainders and cancellations needed by the full signed functional and arithmetic receiver. Exact finite moments do not supply that growing-degree evaluation by themselves. This remaining mathematics is not a prerequisite for reading or sharing the completed cut; later parity/Toda work is outside this edition.

- [Main LaTeX entry point](Original_Relation_Bulk_Control.tex) and [five complete prepared proof bodies](sources/) provide the editable reader; [author originals](provenance/math_sources/) preserve the pre-preparation sources.
- [Complete current receiving sources](dependencies/current_receiving/README.md) include the full [Joint-Schur note](dependencies/current_receiving/CURRENT_JOINT_SCHUR_NOTE.tex), [signed receiver](dependencies/current_receiving/SIGNED_RETURN_RECEIVER.tex), and [standalone application](dependencies/current_receiving/FULL_SOURCE_RECEIVING_APPLICATION.tex), with complete predecessors and providers. The application body is also embedded in the signed receiver.
- [The inherited 46-page Joint-Schur paper](dependencies/joint_schur_46/Joint_Gamma_Schur_Continuation.pdf) and its [source/dependency guide](dependencies/joint_schur_46/README.md) supply the preceding exact interfaces.

The completed delivery records acceptance of all five mathematical bodies and visual review of all 33 actual rendered pages. The receiving delta review covers the changed receiving formulas and relies on the already accepted application body; it is not another whole-file review. These are inherited records, not new proof, PDF, archive, or Lean checks performed in preparing this guide. Public provenance handling preserves mathematical sources and lineage without treating private incoming material or raw owner archives as public source substitutes.
