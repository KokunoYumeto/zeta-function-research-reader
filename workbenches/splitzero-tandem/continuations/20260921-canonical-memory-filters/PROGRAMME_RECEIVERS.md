# Receiving the memory and filter calculations in the original programme

These are complete receiving proofs for SZ-20260921-016. Keep the original quartet, divisor, source mass, physical coordinate \(S=k/2+iy\), actual period and full kernel frame of ME1–6. Every return below uses the four original cutoffs \(q-1,q,2q-1,2q\) with signs \(+,+,-,-\). Write this linear operation as \(\mathcal R\). Constants implicit in the stated asymptotics have the fixed original data specified in ME and RF. All finite domains in those proofs remain in force.

## 1. The original kernel receives an evaluated energy-action correction

Let \(I_K:\mathbb C^m\to E\) be the original full coefficient frame, \(H_{K,N}=I_K^*G_NI_K\), and let \(M\) be the original multiplication by \(y\). It is invertible because all original roots are nonzero. The image \(MI_K\) is therefore a full frame of \(MK\). Put
\[
H^{\mathrm{en}}_{K,N}=I_K^*M^*G_NMI_K.
\tag{BR1}
\]
The map \(I_KH_{K,N}^{-1/2}\) is an isometry onto the original kernel. Thus the block \(A_N\) in ME7 is exactly
\[
A_N=H_{K,N}^{-1/2}H^{\mathrm{en}}_{K,N}H_{K,N}^{-1/2},\qquad
\log\det H^{\mathrm{en}}_{K,N}-\log\det H_{K,N}=\log\det A_N.
\tag{BR2}
\]
This proves the full change of metric, including its determinant factor. ME32–34 now gives
\[
\left|\mathcal R\log\det H^{\mathrm{en}}_{K,N}
-\mathcal R\log\det H_{K,N}\right|
\le\sum_N|\log\det A_N|
=O_{h,A}(q\log(q+2))=o(kq).
\tag{BR3}
\]
The same formula describes the original source norm on the actual image \(MK\), through the map \(M|_K\). It evaluates the action-induced change of the initial kernel allocation. The initial allocation itself remains the full original determinant, with all invariant columns retained.

For the observed metric \(Q_{B,N}\), the actual energy quotient is
\[
\mathcal E_{B,N}
=[\Lambda(M^*G_NM)^{-1}\Lambda^*]^{-1}.
\tag{BR4}
\]
ME33 proves
\[
\log\det\mathcal E_{B,N}-\log\det Q_{B,N}
=2\log|\det M|-\log\det A_N.
\tag{BR5}
\]
The first term is independent of \(N\), so it cancels under \(\mathcal R\). Therefore the observed change is exactly the negative of the kernel change, and both are \(o(kq)\). These are complementary restrictions and attained quotients of the same original energy form. They have been connected by the complete determinant factorization, rather than by a rank allocation.

## 2. The graph correction has its own evaluated determinant

In original isometric coordinates, retain
\(L_{\mathrm{en},N}=(-A_N^{-1}B_{H,N},I)^T\),
\(Z_N=L_{\mathrm{en},N}^\dagger L_{\mathrm{en},N}\), and
\(J_{\mathrm{en},N}=L_{\mathrm{en},N}Z_N^{-1/2}\).
ME31–33 proves the exact relation
\[
\log\det(J_{\mathrm{en},N}^\dagger H_NJ_{\mathrm{en},N})
=2\log|\det M|-\log\det A_N-\log\det Z_N.
\tag{BR6}
\]
Consequently ME34 gives a zero \(kq\) coefficient for the four-cutoff return of the whole graph-energy determinant. The difference from BR5 is precisely \(-\mathcal R\log\det Z_N=o(kq)\). This identifies and bounds the entire change from observed coefficient coordinates to the energy-minimizing section equipped with its original norm.

## 3. A subexponential regularizer transfers the complete observed action

Let \(M_{B,N}=\Lambda ML_{B,N}\), using the original attained target metric. For \(z>0\), ME8 and ME22 give the exact identity
\[
\begin{split}
\log\det(zI+M_{B,N}^\dagger M_{B,N})
&=\log\det(zI+H_N)-\log\det(zI+A_N)\\
&\quad-\ell_N(z)+g_N(z).
\end{split}\tag{BR7}
\]
No coupling block is omitted. If the finite gap from ME29 is \(A_N\succeq\alpha_NI\), diagonalization of \(A_N\) gives
\[
0\le\log\det(zI+A_N)-\log\det A_N
\le m\log(1+z/\alpha_N).
\]
Together with ME24 this proves, for any four positive \(z_N\),
\[
\begin{split}
\left|\mathcal R\log\det(z_NI+M_{B,N}^\dagger M_{B,N})
-\mathcal R\log\det(z_NI+H_N)\right|\\
\le\sum_N\bigl[|\log\det A_N|
+m\log(1+z_N/\alpha_N)+\mathcal B_m(z_N)\bigr].
\end{split}\tag{BR8}
\]
This is a finite bound. For \(|\log z_N|=o(q)\), uniformly over the four endpoints, its right side is \(o(kq)\): use ME34, \(m=8k-16\), \(\log^+(1/\alpha_N)=O_{h,A}(k\log(q+2))\), and
\(\log(1+z/\alpha)\le\log2+\log^+z+\log^+(1/\alpha)\).
ME25 bounds the last term. Thus the actual observed compression and the full canonical action have the same four-cutoff coefficient at scale \(kq\) on this regularizer range. This evaluated receiving result strengthens the earlier memory comparison by retaining the kernel block as well.

The positive-regularizer domain is necessary for this formula as written. ME26 gives its exact boundary correction: when \(M_{B,N}\) has a kernel of dimension \(p_N\), the leakage contains \(-p_N\log z\). The original Schur energy quotient BR4 remains positive at zero. Its exact map and correction are BR4–6. The zero-regularizer memory bound alone does not delete this term.

## 4. All colliding filter directions enter the original quotient

For an admitted monic \(p_k\) of degree \(d_k\), RF37–60 proves in the unchanged numerator frame
\[
\mathcal R\log\det(U_{p_k}^*\Lambda^*Q_{B,N}\Lambda U_{p_k})
=C_\partial d_kq+o(d_kq),
\quad d_k\log(q+2)=o(q).
\tag{BR9}
\]
RF65–67 gives the exact original quotient \(\pi_{p_k}\) with kernel \(\operatorname{im}U_{p_k}\), including its low-polynomial right inverse. Its attained metric changes the original kernel determinant by at most
\(2\min(m,d_k)E_{k,d_k,N}\) at each endpoint, which is \(o(kq)\) after summing. Thus the kernel coefficient remains attached to the same full original frame under the rational quotient. This extends the earlier inverse-power quotient receivers to every stated colliding compact pole family.

RM24–26 gives the complete observed residue matrix at every repeated slow eigenvalue. RM28–31 then transfers all \(d_k\) slow eigenvalues to the actual energy graph and proves the determinant return \(-C_\partial d_kq+o(d_kq)\) for that cluster. The complete graph outside the cluster remains in the full matrix; BR6's whole-graph zero coefficient concerns the canonical degree-one multiplication operator.

For the explicit supplied filter
\(p_k=[(y-13)(y-4)(y-18)(y-468)]^k\), RF61–64 derives the arithmetic witness, unchanged degree \(4k\), physical-coordinate map and rank-one multiplication defect. BR9 evaluates its observed determinant as \(4C_\partial kq+o(kq)\), with \(5.415572<4C_\partial<5.419004\). The unweighted full heat return divided by \(4k\) tends to 2 at RF55's original common time; the actual measured heat is eventually positive with logarithmic rate zero after division by \(4k\), as proved in RF60. Its observation fractions remain explicit.

## Proof sources and affected earlier results

The original complete kernel is [MR1–23](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/ORIGINAL_KERNEL_MIXED_DETERMINANT.tex). BR1–6 supplies evaluated energy-action and graph corrections to that same determinant. The earlier memory construction is [UH1–32 in the complete 014 reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/f1ad8be11f329a12d562420edfa58fa464948ee2/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/UNIFORM_SOURCE_FAMILY_COMPLETE_READER.tex); ME20 and BR7–8 evaluate its canonical receiving bound at scale \(kq\), with the exact zero and positive regularizer domains stated above. The inverse-source receivers are [AK5–12 and AK20](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/KERNEL_CRITICAL_RECEIVERS.tex); RF65–67 and BR9 extend them to polynomial filters. Complete source texts are retained with the edition.

The human Feshbach–Schur source used at RM18–26 is Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, *The Feshbach–Schur map and perturbation theory*, [original author TeX, arXiv:2105.02058v1](https://arxiv.org/src/2105.02058v1), theorem `thm:isospF`, reconstruction equation `QP`, and proposition `prop:U-prop-SA`. The finite proofs of every identity used here are written out in RM. The original Gamma and Meixner–Pollaczek human sources are cited in RF1–15 and retained with their original attribution in the source collection. The higher-cutoff coefficient uses the previously retained monic-profile and zero-law input at its stated analytic scope.
