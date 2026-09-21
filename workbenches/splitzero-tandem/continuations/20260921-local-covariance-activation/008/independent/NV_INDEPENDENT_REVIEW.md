# Independent mathematical review of NV1–9

**Result: NV1–9 is mathematically supported. No correction to its eigenline formulas, source–target orientation, or endpoint-inertia argument is required.** The certificate also passed a separate reconstruction of every endpoint determinant sign and whole-interval cofactor test from its stored matrix balls.

The numerical result concerns the five displayed poles, the four-dimensional rational numerator space, and the original permitted target Gamma parameter \(s=1\). Its four nonzero eigenvalues are target-native generalized eigenvalues. NV correctly describes the source vectors as exact conductor returns and does not assign the same numbers to the different source-native pencil.

## Reviewed sources and actual coverage

These complete files were read:

- ORIGINAL_NATIVE_WEIL_SPECTRUM_BODY.tex, NV1–9, SHA-256 7788bf6e2837921e0968ecb2861c011bd5090c35af5afa98092dc12bc07839d7.
- certify_original_native_weil.py, SHA-256 f82f339355289d9c41f4d7751ec60515466d74128cdeba7b8c3f57353935e5a6.
- ORIGINAL_NATIVE_WEIL_CERTIFICATES.json, SHA-256 dc2b5ba062ad5b3351d1cce8249928b34796c2031f19656415902d445ccb0c8b.

The producer-script hash inside the certificate matches the actual script bytes. The review also read MP6–15, including the original completion constants, absolute convergence, conjugate-linear-first convention, and generating-function signs. RW14–20 and NH1–42 are the preceding exact receiving derivations. No new reading of every inherited primary source is claimed here.

The independent executable is **review_native_eigenline_certificate.py**; its full receipt is **NV_INDEPENDENT_CERTIFICATE_REVIEW.json**. It uses python-flint 0.9.0 at 1024 bits to re-enclose determinants of the already stored matrices. It does not reevaluate xi, zeta, Gamma, a prime sum, or a zero list. The original input-ball radii remain in every reconstructed entry; higher working precision does not remove their uncertainty.

## 1. Arithmetic and native-metric orientations

At \(s=1\), \(b=1/2\), \(M=\sqrt{2\pi}\), the matrix \(K\) is the Gram of \(1,y,y^2,y^3\) in the original positive Gamma measure. Its full moments are retained. It is positive definite because a nonzero polynomial has positive squared integral against the strictly positive density.

Column \(j\) in the code is exactly the expansion of

\[
(d+i(y-\tau))^j(d-i(y-\tau))^{3-j},\qquad d=3/2.
\]

The first factor has constant term \(d-i\tau\) and \(y\)-coefficient \(i\); the second has constant term \(d+i\tau\) and \(y\)-coefficient \(-i\). Those are the code's two complex constant factors. Thus \(3Q^*KQ\) is precisely the original \(H_\omega\), with no conjugation reversal.

The center is retained by \(S'=z+c_*-1/2\). At \(S'=c_*+iy\) this gives \(z=1/2+iy\). This exact translation explains why no residual \(c_*\) appears in the evaluated Gram; it does not change the physical center or measure.

MP9–15 proves

\[
T_{ij}=c_{j-i},\quad c_{-n}=\overline{c_n},\quad
c_0=2\Re(\xi'/\xi)(\omega),\quad
(\xi'/\xi)(m_\omega(u))=(\xi'/\xi)(\omega)+\sum_{n\ge1}c_nu^n.
\]

The code's upper-diagonal coefficient and lower-diagonal conjugation therefore agree with the full-Weil form rather than its transpose. Since \(m_\omega'(0)=-3\ne0\) and \(\xi(\omega)\ne0\), both formal series divisions are valid. Eight coefficients before differentiation suffice for all degrees through three. Formal truncation here computes those exact Taylor coefficients with ball enclosures; it does not replace completed-function values by a finite zero sum.

The coordinate determinant phase also agrees: \(\sqrt3Q\) in the \(y\)-monomial basis has determinant \(-3^8\), whereas \(R_\omega\) in the spectral monomial basis has determinant \(+3^8\). The substitution \(z=1/2+iy\) has determinant \(i^{0+1+2+3}=-1\). Hence NV2 has exactly the unchanged positive Gram determinant from NH10.

## 2. Endpoint inertia proves complete simple positive eigenvalues

At a real endpoint \(x\), \(A(x)=T-xH\) is exactly Hermitian. Nonzero leading principal determinants give the factorization

\[
A=L\operatorname{diag}\left(\Delta_1,\frac{\Delta_2}{\Delta_1},
                   \frac{\Delta_3}{\Delta_2},\frac{\Delta_4}{\Delta_3}\right)L^*,
\]

where \(L\) is invertible unit lower triangular. Successive Schur complements prove the formula: after removing the first pivot, each residual leading determinant is the next original determinant divided by that pivot; induction gives all ratios. Congruence by \(L^*\) preserves positive and negative dimensions. Thus negative inertia equals the number of sign changes in

\[
(1,\Delta_1,\Delta_2,\Delta_3,\Delta_4).
\]

Because \(H>0\), congruence by \(H^{-1/2}\) identifies this with the inertia of

\[
H^{-1/2}TH^{-1/2}-xI.
\]

Its negative inertia counts all generalized eigenvalues below \(x\), with multiplicity. Nonzero \(\Delta_4(x)\) excludes an endpoint eigenvalue.

The independent reconstruction checked:

- All 160 endpoint leading-minor strict signs.
- All 40 endpoint inertias.
- Positivity of the stored full \(H\) and full \(T\) at all five poles.
- Strict positivity, ordering and disjointness of all rational intervals.
- Every exact relative-width inequality \( (u_j-l_j)/l_j<10^{-60}\).

For interval \(j\), the endpoint inertias are \(j-1\) and \(j\). Exactly one eigenvalue, counted with multiplicity, lies inside. It is therefore simple. The four intervals account for all four eigenvalues, so there is no additional root outside them or hidden multiplicity inside one.

An imaginary ball containing zero does not itself prove a determinant real. Exact Hermitian symmetry proves reality first; imaginary containment is then a consistency check, and the strict real ball sign determines the actual sign. NV uses these facts in the correct order. The rounded table entries play no role in the proof.

## 3. The cofactor formula constructs the exact eigenline

Let \(\lambda_j\) be the unique generalized eigenvalue in its certified rational interval, and \(k_j\) the selected index. The independent review rebuilt the ball enclosing the entire interval, checked that it contains both exact rational endpoints, and recomputed all 20 selected principal cofactors. Every real cofactor interval excludes zero, and every imaginary interval contains zero.

In particular,

\[
\big(\operatorname{adj}(T-\lambda_jH)\big)_{k_jk_j}\ne0.
\]

Therefore

\[
d_j=\operatorname{adj}(T-\lambda_jH)e_{k_j}\ne0,\qquad
(T-\lambda_jH)d_j=\det(T-\lambda_jH)e_{k_j}=0.
\]

The exact coordinate orientation is

\[
(d_j)_i=(-1)^{i+k_j}
\det(T-\lambda_jH)_{\{0,1,2,3\}\setminus\{k_j\},
                      \{0,1,2,3\}\setminus\{i\}}.
\]

The deleted row is \(k_j\), and the deleted column is \(i\), because the adjugate transposes the cofactor matrix. This confirms NV7. Each coordinate is a polynomial of degree at most three in the exactly defined \(\lambda_j\), with exact full-Weil and native Gram coefficients. Simplicity makes its nonzero line the complete eigenspace.

The interval cofactor check does not say that \(\operatorname{adj}(T-xH)e_{k_j}\) is an eigenvector for every \(x\) in the interval. It proves that the specified column cannot vanish at the root \(\lambda_j\). NV uses precisely that implication. Exact completed-function definitions, a unique-root isolating interval, and the explicit cofactor formula together specify an exact eigenline; the rounded eigenvalue alone would not.

## 4. Exact lift into the target-native eight-state pencil

Write \(z=E\alpha+O\beta\) and \(d=B_\omega z\). The complete Weil matrix is

\[
\mathbb W=[E\ O]^*B_\omega^*TB_\omega[E\ O],
\]

and the target-native squared norm is

\[
\alpha^*G_Y\alpha+z^*Gz.
\]

The exact relation is \(H=B_\omega^{-*}GB_\omega^{-1}\). For the proposed lift \(\alpha=0\), \(\beta=O^{-1}B_\omega^{-1}d_j\), direct substitution proves

\[
\begin{aligned}
\mathbb Wv_j
&=[E\ O]^*B_\omega^*Td_j\\
&=\lambda_j[E\ O]^*B_\omega^*Hd_j\\
&=\lambda_j[E\ O]^*GB_\omega^{-1}d_j
=\lambda_j\mathbb H_Wv_j.
\end{aligned}
\]

This proves the actual eight-state generalized eigenvector equation without declaring a coordinate map unitary. The factors \(1/2\) in the expansion in \(f_{\ell,+},f_{\ell,-}\) are the exact definition of \(\iota_-\), and NV8 retains them.

The physical target is

\[
\Psi B_\omega^{-1}d_j=C_{-\kappa}R_\omega d_j,
\]

and the physical source is

\[
\Phi B_\omega^{-1}d_j=T_A^{-1}C_{-\kappa}R_\omega d_j.
\]

These follow from \(B_\omega=R_\omega^{-1}C_\kappa\Psi\) and \(T_A\Phi=\Psi\). Thus the original center, full conductor moments and quotient inverse have the correct orientation.

The source vector is an exact conductor return of a target eigenline. Its source-native generalized eigenvalue is not asserted to equal \(\lambda_j\); that would require using \(H_U\) in the pencil. NV's final paragraph preserves this distinction correctly. NH26–42 gives the exact source matrices but does not assign numerical values to unspecified conductor moments.

## 5. Complete kernel and original-target orthogonality

The graph vectors

\[
g_\ell=\iota_+e_\ell-\iota_-O^{-1}Ee_\ell
\]

have zero evaluation, hence lie in the Weil kernel. Their independent even components prove independence. Conversely \(T>0\) forces a kernel vector to have \(d=0\), hence \(E\alpha+O\beta=0\), so it is exactly a combination of those four graph vectors. The nullity is precisely four.

For \(j\ne k\), Hermitian symmetry gives

\[
d_k^*Td_j=\lambda_jd_k^*Hd_j=\lambda_kd_k^*Hd_j.
\]

Distinct certified eigenvalues force \(d_k^*Hd_j=0\). This is original target-native orthogonality. Graph vectors have only the retained label component in the exact direct-sum description, whereas all \(v_j\) have only the evaluation component, so the two groups are also orthogonal. The graph vectors' mutual Gram remains \(G_Y\); NV does not claim that their displayed basis is Euclidean-orthonormal.

The four nonzero eigenvectors form a basis of the positive quotient, and the four graph vectors form a basis of its exact kernel. Together they give the complete eight-state eigenbasis.

## 6. Scope and the separate continuous bound

The checks establish 20 simple positive target-native eigenvalues and 20 exact cofactor eigenlines at the five poles, with the original allowed \(s=1\) metric. They concern the entire four-dimensional pencil, not one selected direction, and the full eight-state lift includes exactly four graph-null directions.

The separate continuous coefficient coercivity reported by the CP calculation can be transported through the original positive metrics using NW. It does not by itself prove simplicity or the same cofactor-column choice throughout the larger continuous interval. NV makes no such claim. This review has not extended a five-pole eigenline certificate into an all-height or all-degree theorem.

No mathematical correction is needed. The independent review additionally checks interval-box containment of both rational endpoints and imaginary containment for every selected cofactor; all pass. Those checks strengthen the evidence for the current claim without requiring a change to its formulas.

## Provenance retained

The arithmetic coefficient identity is MP6–15, with its stated human genus-one-product and functional-equation inputs. The interval arithmetic is Johansson's Arb through python-flint 0.9.0. The original Gamma dictionary retains Koornwinder, Wong, Koekoek, Swarttouw and Reinhardt's DLMF Chapter 18 attribution through WCF and NH. The signed-state construction retains the original four-dimensional polynomial and marked locales of The Clankers' canonical ES reader. This independent finite-dimensional and interval-algebra review does not transfer those earlier results' authorship to itself.
