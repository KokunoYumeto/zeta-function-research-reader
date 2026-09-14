# Independent review of the metric backpropagation

Review date: 2026-09-13.
Reviewer: independent mathematical review agent.
Outcome: **PASS for the three staged mathematical edits below. No mathematical correction requested.**

I read the complete staged AT, AW and SP mathematical bodies, including every proof, and the complete corresponding original bodies. This review is not a tag inventory or a compilation receipt. It checks the actual formulas and maps in their source contexts. I did not edit any of the six reviewed files. The original analytic source constructions and the quartet Gamma theorem remain explicitly identified dependencies; this bounded review does not claim to reread their entire source closure.

## Exact source pins and preservation

All paths in this table are relative to this review's containing directory.

| Source | Original SHA-256 | Staged SHA-256 |
|---|---|---|
| tex/next_edition/AT_complete.tex | a89fed1c68bb104fe4169acc25bf67a101d1220648588027d2e4c5b36f561325 | aed46ea606dd146f30e1f405546de8c84d42f9ac1962b5fe6b3693c128868c09 |
| tex/next_edition/AW_complete.tex | 1165fc98707d8f54a34fa6a15ff3edf7e1d384da1638e7806d340534c3d73877 | 4310eda618704d7d654a17401f5279777a854582cb2ba8645129ac2d14a100c2 |
| tex/tau_signed_projection_control.tex | 180cd8a83a59e692fc0fa16a6622794927360df42317dc9d0ec3bdd6dbd7cd1a | 1cdaa647a1298a5c389bc5b6eadd2a8cb289855b69ce443669778efb42dfc997 |

Original copies are below originals/ and revised files below staged/. Independent Get-FileHash calls confirmed all six hashes against PATCH_MANIFEST.json. The three live source paths named by that manifest also still match their original copies byte for byte. The staging therefore preserves the original sources while providing separate revisions.

## Original source, measures and typed relation maps

The revisions retain \(H=\mathcal P_{2q}\), the original monomial coefficient frame, \(S=k/2+iu\), \(\chi=\chi_{h,k}\), \(E=\mathbb C[S]/(\chi)\), the full invertible Taylor unit, and the observation \(\sigma_h^{\otimes k}\eta J_{2q}\). No polynomial coordinate is divided by \(k\).

AT4a, AW13a and SP1a give the same Gamma measure. In the retained convention \(c_a=2^{1-2a}\Gamma(2a)\), direct substitution gives \(c_{1/4}=2^{1/2}\Gamma(1/2)=\sqrt{2\pi}\). Thus the original convolution formula \(r_{1/4}^{*k}=c_{1/4}^k r_{k/4}/c_{k/4}\) gives exactly the displayed AT4/AW3 density, with mass \((2\pi)^{k/2}\). The arithmetic density remains \(w_h^{*k}\), with mass \(\mu_h^k\). No scalar mass adjustment is involved.

The relation arrows differ in their displayed codomains: \(B_N^{\rm AT}=B_N^{\rm AW}:\mathcal P_{N-q}\to\mathcal P_N\), whereas \(B_N^{\rm SP}:\mathcal P_{N-q}\to H\). The revisions prove the exact equation \(B_N^{\rm SP}=I_NB_N^{\rm AW}\). Hence
\[
(B_N^{\rm SP})^*M B_N^{\rm SP}
=B_N^*I_N^*MI_NB_N=B_N^*M_NB_N.
\]
Substitution into the projector formula gives the same endomorphism of \(H\). This verifies the typed comparison; it does not equate the two different codomains without their inclusion. The \(x=t,\ y=u\) variable dictionary retains the original source coordinate and the two different roles of frequency and metric interpolation.

The AT6--AT17 arguments remain valid in their full contexts. In particular the minimum section satisfies \(JR=I\) and \(B^*MR=0\); differentiating those two identities determines \(\dot R\), \(\dot G\), and the negative second variation. The monic determinant-line change has determinant \((-1)^{q(N-q+1)}\), whose squared modulus is one. The signed four-window trace follows with \(U-W\), rather than its negative. The kernel \(v(U-W)M^{-1}v^*\) in SP keeps the required inverse metric. All these earlier maps and signs remain present.

## Full window spectrum and pointwise minimum

For \(U\), the flag dimensions \(1,q,q+1,2q+1\) give successive eigenvalues \(1,2,1,0\) of multiplicities \(1,q-1,1,q\). For \(W\), the source flag gives eigenvalues \(0,1,2,1\) of multiplicities \(q,1,q-1,1\). Therefore both have rank \(q+1\), trace \(2q\), and squared trace \(4q-2\). For \(A=U-W\), this proves
\[
\operatorname{Tr}A=0,\qquad
\operatorname{Tr}A^2=8q-4-2\operatorname{Tr}(UW).
\]
The revised text correctly distinguishes rank from trace and retains the multiplicity-two directions. It also correctly attributes the earlier spectra and condition-number coefficient to AW.

Let \(c_1\le\cdots\le c_{2q+1}\) be the eigenvalues of the actual self-adjoint metric derivative. Every orthogonal projection of rank \(r\) has diagonal entries in \([0,1]\) summing to \(r\), in an eigenbasis of that derivative. Its trace pairing therefore lies between the sums of the smallest and largest \(r\) eigenvalues. Decomposing either \(U\) or \(W\) into its range projection plus its eigenvalue-two projection gives the two sums printed in AT20b, AW15 and SP10b. Their upper-minus-lower difference is exactly
\[
S_{\rm AW}
=c_{q+2}-c_q+
2\sum_{j=1}^{q-1}(c_{2q+2-j}-c_j).
\]
In particular there is no extra factor of two from bounding the two traces.

Both ranges have dimension \(q+1\) in dimension \(2q+1\), so their intersection has dimension \(s\ge1\). Its orthogonal projection \(E_L\) is dominated by each operator: \(U\) and \(W\) each dominate their own range projection, and the range projection dominates \(E_L\). Thus \(U-E_L\) and \(W-E_L\) are positive with trace \(2q-s\). Their difference is \(A\), giving \(\|A\|_1\le4q-2s\). Cauchy--Schwarz on all real eigenvalues of \(A\) gives \(\|A\|_1\le\sqrt{(2q+1)\operatorname{Tr}A^2}\).

Subtracting the scalar midpoint of the extreme \(c_j\) changes no trace pairing because \(\operatorname{Tr}A=0\). In an eigenbasis of \(A\), each diagonal value of the centered metric derivative is bounded in absolute value by \(d/2=(c_{2q+1}-c_1)/2\). Hence
\[
|\operatorname{Tr}(AC)|
\le S_{\rm SP}
=\frac d2\min\left\{4q-2s,
\sqrt{(2q+1)(8q-4-2\operatorname{Tr}(UW))}\right\}.
\]
Both estimates bound the same actual signed integrand, so their pointwise minimum is valid before integration. The square-root argument is nonnegative by the proved trace-square identity. No mutual commutation of \(U,W,C\) was used. Smooth positive Grams give bounded overlaps and eigenvalues; the rank formula for the intersection gives Borel \(s(t)\). Thus the minimum is integrable.

## Integration, exact commutator and propagated endpoint

In the unchanged coefficient frame \(M(t)=M(0)((1-t)I+tD)\), so
\[
C(t)=((1-t)I+tD)^{-1}(D-I),\qquad
c_j(t)=\frac{b_j-1}{1-t+tb_j}.
\]
The positive \(b_j\) are ordered identically throughout the interval because the derivative in \(b_j\) is \((1-t+tb_j)^{-2}>0\). The original \(M(0)\)-orthogonal eigenvectors remain orthogonal for \(M(t)\), with squared lengths multiplied by the positive factors \(1-t+tb_j\). This justifies the spectral formula in the varying original metric.

The identity \(\int_0^1c_j(t)\,dt=\log b_j\) follows directly by differentiation of \(\log(1-t+tb_j)\), including \(b_j=1\). It proves that the integral of \(S_{\rm AW}\) equals the displayed \(\mathcal L_q(D)\). Every retained logarithmic ratio is at most \(\log\kappa(D)\), with total coefficient \(1+2(q-1)=2q-1\). Consequently all three staged sources correctly obtain
\[
|\Delta\mathcal B|\le\mathcal J_{h,k}
\le\mathcal L_q(D)\le(2q-1)\log\kappa(D),
\qquad
\mathcal J_{h,k}=\int_0^1\min(S_{\rm AW},S_{\rm SP})\,dt.
\]
The separate exact trace-norm integral in SP13 remains valid. No unwarranted ordering between that integral and the full-spectrum bound is claimed.

AW9--AW10 constructs the source isometry using the original positive Gram lengths, including every coefficient of the relation and quotient frames. Its eigenvalue matching gives \(U=TWT^{-1}\). Cyclicity then gives
\[
\operatorname{Tr}((U-W)C)
=\operatorname{Tr}(WT^{-1}CT-WC)
=\operatorname{Tr}(WT^{-1}[C,T]).
\]
The sign and order are correct. The SP reuse explicitly distinguishes this isometry from its metric derivative \(T_x=C\). The observation defect is exactly \(\mathcal OT-\mathcal O=\sigma_h^{\otimes k}\eta J_{2q}(T-I)\); injectivity of the two indicated observation arrows gives \(\ker(\mathcal OT)=T^{-1}(\chi\mathcal P_q)\). The equations do not assign an additional cohomology intertwining property to the metric isometry.

For AT22, write \(L=4q\log(\delta k/(2\sqrt5))\). The retained Gamma theorem supplies \(\mathcal B^\Gamma\ge L\), while the proved comparison gives \(\mathcal B^{\rm ar}\ge\mathcal B^\Gamma-\mathcal J\). Hence \(\mathcal B^{\rm ar}\ge L-\mathcal J\ge L-\mathcal L_q\ge L-(2q-1)\log\kappa\), exactly as printed. Rearranging the last inequality gives \(\log\kappa\ge(L-\mathcal B^{\rm ar})/(2q-1)\), with a positive denominator. The earlier coefficient \(2q\) has therefore been updated in the actual endpoint theorem and its necessary condition, not only in an appended remark. AW18 is updated with the same sign and \(-\mathcal J\).

## Edge cases and retained scope

At \(N=q-1\), the relation domain is zero, its determinant is one, and every composition through it is zero. The revised Gram and projector comparisons include this case. At \(q=1\), the four endpoints are \(0,1,1,2\); the two middle determinant factors coincide and cancel in that specified ratio. The multiplicity \(q-1\) and every associated sum are empty. The spectral estimate reduces to \(S_{\rm AW}=c_3-c_1\), and \(\mathcal L_1=\log(b_3/b_1)\); no nonexistent eigenvalue is evaluated.

AW19--AW23 retain the independent stronger angle calculation for \(q=1\). Its strict positivity follows from the original line identity \(\overline S=k-S\), which would otherwise make the positive norm of \(\chi\) vanish. Its projection difference has eigenvalues \(\sin\theta,0,-\sin\theta\), and differentiating \(2\operatorname{arcosh}(e^{B/2})\) gives the displayed positive factor. These formulas are unchanged and compatible with the general estimates.

For proportional Grams \(M(1)=cM(0)\), all metric-derivative eigenvalues agree and both displayed general bounds vanish. Each quotient determinant receives the actual factor \((1-t+tc)^q\), which cancels only in the specified four-endpoint ratio. Repeated relative eigenvalues and an eigenvalue equal to one cause no singularity.

The packet restrictions, full observation units, and source dependencies remain explicit. The revised results are actual finite controls and exact comparison maps. They contain no assertion of a uniform arithmetic estimate, existence of an off-line quartet, or conclusion about RH or the entire programme.
