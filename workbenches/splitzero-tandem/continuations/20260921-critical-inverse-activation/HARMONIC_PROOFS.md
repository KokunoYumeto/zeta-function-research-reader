# Full-space harmonic control of the original critical activation

21 September 2026. Independent derivation of the received critical-activation equations (10)–(26), with the original physical coordinates, complete source covariance, and complete observed minimum retained. The new finite result is a full-space covariance comparison and its harmonic restriction to the original inverse-power frame. Its asymptotic high endpoint uses the already established IFH8–10 monic-profile and zero-law theorem at that theorem's stated scope.

All constants in the received finite comparison are valid on the explicit IVO guards below. Two useful strengthenings are proved here: the lattice-product error is \(O_{\delta,\gamma}(k)\), and the clipped critical law is uniform on the entire physical activation range, expressed as \(\zeta\ge-2\log(q/k)\), not merely on fixed compact sets of \(\zeta\).

## 1. Source identity, inherited finite inputs, and exact guards

The complete received manuscript `SUPPLIED_CRITICAL_ACTIVATION.md` was read, SHA-256 `5925D871EC57D58F3E993D97240F5061DE0D4726D3C4B3581481999929B6DA5C`. The entire second attachment `SUPPLIED_CODE_AND_PROOF.md` was also read, SHA-256 `63F17FA57E656542C108048942750D7C992ECAD55046FBDAAC99888E89C6AD3A`. Its code and reported receipts are provenance, not an additional theorem or an execution performed here. In particular its preceding activation-source hash `6fc047f2513c6c61e0568e47bda23ccb5ccc4394e7704bb7f3f4e5aa9d871e29` agrees with the retained original activation proof previously read.

The web attachment's manifest identifies its inverse-observation input as 28,714 bytes, SHA-256 `bfdae1dd6fc2b99a045277141c3c0cdaf075cc3d7cc8408ed2eaf29f3e0f5e4b`. It does not byte-match the retained `../observation_inverse_power_intake_20260921/INVERSE_POWER_OBSERVATION_SUPPLIED.md`, which is 29,503 bytes, SHA-256 `78B06ADF8AA4065DACD76F901515D8FE88C736672107F4D6859892F3CE5FCD19`; the retained supplied file in `publication_012` has this same latter size and hash. Consequently the manifest is not evidence of identical input versions. The verified IVO and IFH proofs listed below are the actual accepted providers used in this derivation.

The mathematical input files actually inspected are:

- `../publication_012/INDEPENDENT_FINITE_OBSERVATION.tex`, complete IVO1–26, SHA-256 `D9889E4493C966DCD712E9A10840004794D4D41A79A91C8C9393CE15D7AC2E1E`. Its [pinned complete proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INDEPENDENT_FINITE_OBSERVATION.tex) supplies IVO3, IVO9–11 and IVO24–26.
- `../INVERSE_FLAG_AND_RELATIVE_HEAT.tex`, IFH2–10, lines 41–190, SHA-256 `468C92EE4224A3659BE44F122EFB9FBFC0C2A469624FF5DA6D16280AA069A6CA`. The [pinned IFH proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INVERSE_FLAG_AND_RELATIVE_HEAT.tex#L41) identifies the finite scalar sandwich and the inherited high-endpoint coefficient.
- `../verified_public_providers/NATIVE_GAUSSIAN_TRANSFER.tex`, NG1–3, lines 27–75, SHA-256 `8A9FD3921F4A8667A88BBB5896AB7D5A19E5BE043FCB9B79BB883858888B72CA`; [NG2 in its pinned original source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/NATIVE_GAUSSIAN_TRANSFER.tex#L50).
- The complete joint-source proof J3, lines 634–643 of `../../../JOINT_MINIMUM_COMPLETE.tex`, previously read together with its physical section and full normal-source maps J5–J8. SHA-256 `70DC576A470E1FDC15AFE7C7CA49EFCDD569BF1EA2A429094D0E19B97EBCD416`. Its complete source is retained with the [uniform-source-family edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/f1ad8be11f329a12d562420edfa58fa464948ee2/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/JOINT_MINIMUM_COMPLETE.tex#L634).
- R. A. Askey and R. Roy's [DLMF Gamma product 5.8.3](https://dlmf.nist.gov/5.8.E3), original TeX at `../kernel_derivation/graph_primary_sources/DLMF_5_8_E3_Gamma_product_original.tex`, was read directly. SHA-256 `83583AB37D82A6DE75A23F3183890BCE04A340AD4045A706993C2038EED1A34E`. The Gamma bounds in Section 6 below are explicitly derived from it. IVO retains the original Meixner–Pollaczek conventions of T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw, with W. P. Reinhardt, [DLMF 18.22.8](https://dlmf.nist.gov/18.22.E8) and [18.23.7](https://dlmf.nist.gov/18.23.E7); no replacement measure is used here.

Keep the original simple-quartet domain

\[
\begin{gathered}
0<\delta<\tfrac12,\quad\gamma>2,\quad k\equiv1\pmod4,
\quad q=(k+1)^2,\\
S=k/2+iy,\quad R_0=\sqrt{\delta^2+\gamma^2},\quad R=kR_0,
\end{gathered}
\tag{HAR1}
\]

and the complete polynomial

\[
Q(y)=\prod_{a,b=0}^k(y-\omega_{ab}),\qquad
\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,
\qquad E=\mathbb C[y]/(Q).
\tag{HAR2}
\]

All roots are distinct and nonzero. The polynomial is real, even, and positive on the real axis. The native source remains \(d\mu=w_h^{*k}(y)\,dy\), and the reference measure remains

\[
d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy,
\qquad M_\sigma=\sqrt{2\pi}.
\tag{HAR3}
\]

Keep the full scalar and joint attained metrics \(G_N,G_N^J\), and the same physical tensor section at all cutoffs. The source activation is exactly

\[
C_N(\alpha)=G_N(\alpha)^{-1}
=(1-\alpha)G_N^{-1}+\alpha(G_N^J)^{-1},\qquad0\le\alpha\le1.
\tag{HAR4}
\]

The full-source comparison, in the same value coordinates, is

\[
\mathbf L_k^{-1}T_k\preceq G_N^J\preceq\mathbf B_kT_k,
\qquad G_N^J\preceq G_N,
\tag{HAR5}
\]

where \(T_k\) is the complete fixed tensor-value metric. In root-value coordinates its diagonal entries are the original ordered-tuple weights:

\[
T_k=\operatorname{diag}(W_\omega),\qquad
W_\omega\ge a_{\min}^k>0,
\qquad\sum_\omega W_\omega=A_w^k.
\tag{HAR6}
\]

The inequalities HAR5 follow from J3 before taking the minimum over the full source fibre on the lower side, and from the actual tensor section on the upper side. The already proved A6–7 bounds give individual logarithmic costs \(O_h(k\log^2(q+2))\) for \(\mathbf L_k,\mathbf B_k\); both use the same section and a degree allowance covering the four original cutoffs. A bound only on their product would not, by itself, bound either separate constant without further information. Here the retained source construction supplies that information.

For the onto original observation \(\Lambda:E\to B\), define
\(Q_{B,N}(\alpha)=(\Lambda C_N(\alpha)\Lambda^*)^{-1}\).
Use the literal inverse-power frame
\(U_rd=\sum_{j=1}^rd_j[y^{-j}]\), and its original source and observed Grams

\[
H^E_{r,N}(\alpha)=U_r^*G_N(\alpha)U_r,
\quad H^B_{r,N}(\alpha)=U_r^*\Lambda^*Q_{B,N}(\alpha)\Lambda U_r.
\tag{HAR7}
\]

Set

\[
n_0=2\left\lfloor\frac{N+1-q}{2}\right\rfloor,
\quad K_N=\mathsf K_{Q,n_0}(0,0),
\quad \mathsf S_N=\frac{u_k}{|Q(0)|^2K_N}.
\tag{HAR8}
\]

The kernel is for the complete measure \(Q^2d\sigma\), and \(u_k\) is the unchanged NG2 constant. IVO/IFH gives the finite sandwich

\[
a_{r,N}\mathsf S_N I_r\preceq H^B_{r,N}(0)
\preceq H^E_{r,N}(0)\preceq b_{r,N}\mathsf S_N I_r,
\tag{HAR9}
\]

with exactly

\[
a_{r,N}=\frac{\ell_{k,N}}{u_k}
\left(\frac{\mathcal L_*\mathcal R_*}{2\mathcal F_N\mathcal B^{Jr}}\right)^2,
\qquad b_{r,N}=\mathcal U_{r,N}^2.
\tag{HAR10}
\]

Here each conductor constant is the complete displayed IVO constant, for an actual nonzero selected conductor coefficient. The finite domain retained is IVO24:

\[
q_-=(k-7)^2\ge16,\quad R\le2^{-14}q_-,\quad
n_-+2\le2q_-,\quad
\mathcal L_*\mathcal R_*T_N^{\rm lb}\ge2\mathcal A,
\quad n_-=N-v+Jr-q_-.
\tag{HAR11}
\]

Also retain \(1\le r\le q\), the actual conductor identity through the full observation, and its proved five-orbit period domain. Under the eventual regime \(r\log(q+2)=o(q)\), every guard in HAR11 holds for the same fixed original data, as proved in IVO24–26. In particular

\[
\log^+(a_{r,N}^{-1})+\log^+b_{r,N}
=O_{h,A}((k+Jr)\log(q+Jr+2)).
\tag{HAR12}
\]

No part of the argument below asserts these eventual guards at the small lattice sizes used only for exact algebraic checks.

## 2. The exact lattice cardinal bound

Write \(D_{ab}=|Q'(\omega_{ab})|\). For a fixed row \(m\ne a\), the factors in \(D_{a,b+1}^2/D_{ab}^2\) cancel successively along that row; only its two end factors remain. In row \(m=a\), the omitted self-factor gives the horizontal product \((2\gamma)^{2k}(b!)^2((k-b)!)^2\), whose adjacent ratio is \((b+1)^2/(k-b)^2\). Combining all rows proves exactly

\[
\frac{D_{a,b+1}^2}{D_{ab}^2}
=\prod_{m=0}^k
\frac{\delta^2(a-m)^2+\gamma^2(b+1)^2}
{\delta^2(a-m)^2+\gamma^2(k-b)^2}.
\tag{HAR13}
\]

All factors are less than one if \(b<(k-1)/2\), equal to one if \(b=(k-1)/2\), and greater than one afterwards. Interchanging the two coordinate directions proves the same statement in \(a\). Hence precisely the four central roots minimize \(D_{ab}\), with equal minima. Each has modulus \(R_0\).

Choose a central root \(\omega_c\). A shell of index displacement \(j=\max(|a-a_c|,|b-b_c|)\) contains at most \(8j\) roots, and every distance in that shell is at least \(2\delta j\). The largest possible \(j\) is \((k+1)/2\), in particular at most \(k\). Since
\(|\omega|\le|\omega-\omega_c|+R_0\), the inequality \(\log(1+x)\le x\) gives

\[
\begin{aligned}
\log\frac{|Q(0)|}{R_0|Q'(\omega_c)|}
&=\sum_{\omega\ne\omega_c}\log\frac{|\omega|}{|\omega-\omega_c|}\\
&\le R_0\sum_{\omega\ne\omega_c}\frac1{|\omega-\omega_c|}
\le\frac{2(k+1)R_0}{\delta}
\le\frac{4kR_0}{\delta}.
\end{aligned}
\tag{HAR14}
\]

The exact minimum property of the central derivative now proves the supplied constant

\[
\boxed{\frac{|Q(0)|}{|Q'(\omega)|}
\le R_0e^{4kR_0/\delta}\quad\text{for every original root}.}
\tag{HAR15}
\]

The preceding line also supplies the smaller exponent \(2(k+1)R_0/\delta\), if desired. HAR15 retains the received constant exactly.

## 3. Cardinal lifts and the complete trace comparison

The IVO hard gap has \(\beta_q=2^{-27}q^2\). HAR11 implies
\(R^2\le2^{-28}q_-^2\le\beta_q/2\). Also \(q\ge16\) and \(n_0\le q\le2q-2\) at every original cutoff. Thus IVO11 applies to

\[
H(y)=\frac{\mathsf K_{Q,n_0}(y,0)}{K_N},
\quad H(0)=1,
\quad\|QH\|_\sigma^2=K_N^{-1},
\quad |H(z)|\ge e^{-n_0R^2/\beta_q}\quad(|z|\le R).
\tag{HAR16}
\]

The last inequality follows from the paired zeros of the odd polynomial \(yH(y)\): their nonzero squares are at least \(\beta_q\), and \(\log(1-u)\ge-2u\) for \(0\le u\le1/2\). This is exactly the IVO11 constant, now with its required radius and degree guards checked.

For each original root use the actual polynomial

\[
P_\omega(y)=\frac{Q(y)H(y)}{(y-\omega)Q'(\omega)H(\omega)}.
\tag{HAR17}
\]

Its degree is at most \(q+n_0-1\le N\), and its complete root values are \(P_\omega(\omega')=\mathbf1_{\omega=\omega'}\). Thus it lifts the original cardinal class \(e_\omega\), without replacing its value coordinates. For real \(y\), oddness of \(k\) gives \(|\operatorname{Im}\omega|\ge\delta\), so \(|y-\omega|\ge\delta\). NG2, applied to this full degree-\(N\) polynomial, yields

\[
\|e_\omega\|_{G_N}^2\le
\frac{u_k e^{2n_0R^2/\beta_q}}{\delta^2|Q'(\omega)|^2K_N}.
\tag{HAR18}
\]

In the original root-value frame, \(e_\omega\) is the corresponding coordinate vector and HAR6 is diagonal. Consequently

\[
\operatorname{Tr}(T_k^{-1}G_N)
=\sum_\omega\frac{\|e_\omega\|_{G_N}^2}{W_\omega}
\le\Gamma_N\mathsf S_N,
\tag{HAR19}
\]

where the received explicit constant is

\[
\boxed{\Gamma_N=
\max\left(1,\frac{qR_0^2}{\delta^2a_{\min}^k}
\exp\left[\frac{8kR_0}{\delta}+
\frac{2n_0R^2}{\beta_q}\right]\right).}
\tag{HAR20}
\]

Changing back to the fixed polynomial frame changes both \(T_k\) and \(G_N\) by the same congruence, so the trace and the inequality are unchanged. The term \(2n_0R^2/\beta_q\) is bounded at fixed \(\delta,\gamma\), since \(n_0\le q\) and \(k^2/q\le1\). Therefore \(\log\Gamma_N=O_h(k+\log q)\). This controls the full metric, including all cross terms; no diagonal replacement of \(G_N\) was made.

## 4. The full-space harmonic comparison and the original observation

For any positive \(T,G\), the positive matrix \(G^{1/2}T^{-1}G^{1/2}\) is at most its trace times the identity. Congruence by \(G^{-1/2}\) proves

\[
T^{-1}\preceq\operatorname{Tr}(T^{-1}G)G^{-1}.
\tag{HAR21}
\]

Invert the lower half of HAR5 and apply HAR19–21 to obtain

\[
(G_N^J)^{-1}\preceq\mathbf L_kT_k^{-1}
\preceq\mathbf L_k\Gamma_N\mathsf S_NG_N^{-1}.
\]

Substitution in the complete covariance HAR4 and inversion give the stronger full-space result

\[
\boxed{
G_N(\alpha)\succeq
\frac{G_N}{1-\alpha+\alpha\mathbf L_k\Gamma_N\mathsf S_N}.
}
\tag{HAR22}
\]

Applying the unchanged \(\Lambda,\Lambda^*\) to the covariance order before inversion gives, on the whole observation space,

\[
Q_{B,N}(\alpha)\succeq
\frac{Q_{B,N}(0)}{1-\alpha+\alpha\mathbf L_k\Gamma_N\mathsf S_N}.
\tag{HAR23}
\]

Restriction to \(F=\Lambda U_r\) is exactly the received observed lower bound. This derivation never commutes a restriction with inversion.

The left inverse used in received (14) is also exact. With \(H_0=F^*Q_{B,N}(0)F>0\), put \(R_N=H_0^{-1}F^*Q_{B,N}(0)\). Multiplication gives \(R_NF=I_r\) and \(R_NQ_{B,N}(0)^{-1}R_N^*=H_0^{-1}\). For any positive \(Q_B\), minimizing \(x^*Q_Bx\) under \(R_Nx=d\) gives the attained metric \((R_NQ_B^{-1}R_N^*)^{-1}\). The vector \(Fd\) is one admissible lift, so \(F^*Q_BF\succeq(R_NQ_B^{-1}R_N^*)^{-1}\). This verifies that route as well, with the full target minimum retained.

The two upper covariance comparisons yield

\[
H^E_{r,N}(\alpha)\preceq
\frac{b_{r,N}\mathsf S_N}{1-\alpha}I_r,
\qquad
H^E_{r,N}(\alpha)\preceq
\frac{\mathbf B_k}{\alpha}U_r^*T_kU_r,
\tag{HAR24}
\]

where the corresponding inequality is omitted if its denominator is zero. For every coefficient vector \(d\), the original root-value norm satisfies

\[
\begin{aligned}
d^*U_r^*T_kU_rd
&=\sum_\omega W_\omega\left|\sum_{j=1}^rd_j\omega^{-j}\right|^2\\
&\le\|d\|^2\sum_\omega W_\omega\sum_{j=1}^r|\omega|^{-2j}
\le\frac{A_w^k}{R_0^2-1}\|d\|^2.
\end{aligned}
\tag{HAR25}
\]

Here every root satisfies \(|\omega|\ge R_0>2\), and the two displayed coefficient sums include all inverse powers and all original root weights.

Define, with the received notation,

\[
h_N(\alpha)=\frac{\mathsf S_N}{1-\alpha+\alpha\mathsf S_N},
\quad L_{r,N}=\frac{a_{r,N}}{\max(1,\mathbf L_k\Gamma_N)},
\quad U_{r,N}=b_{r,N}+\frac{\mathbf B_kA_w^k}{R_0^2-1}.
\tag{HAR26}
\]

For positive \(b,d,s\) and \(0<\alpha<1\),

\[
\min\left(\frac{bs}{1-\alpha},\frac d\alpha\right)
\le(b+d)\frac{s}{1-\alpha+\alpha s}.
\tag{HAR27}
\]

To verify it, if the first fraction is smaller, its ratio to the rightmost \(s/(1-\alpha+\alpha s)\) is \(b+b\alpha s/(1-\alpha)\le b+d\). If the second is smaller the same calculation gives \(d+d(1-\alpha)/(\alpha s)\le d+b\). At the endpoints retain the finite fraction. Also
\(1-\alpha+\alpha c s\le\max(1,c)(1-\alpha+\alpha s)\).
Thus HAR9, HAR23–27 give

\[
\boxed{
L_{r,N}h_N(\alpha)I_r\preceq H^B_{r,N}(\alpha)
\preceq H^E_{r,N}(\alpha)\preceq U_{r,N}h_N(\alpha)I_r
\quad(0\le\alpha\le1).
}
\tag{HAR28}
\]

The middle inequality is the original observed minimum over its full fibre, which includes the original vector as one lift.

Set \(E_{r,N}=\max(0,-\log L_{r,N},\log U_{r,N})\). The individual source constants, HAR12, HAR20, and the fixed masses in HAR6 show

\[
E_{r,N}=O_{h,A}\left(k\log^2(q+2)+(k+Jr)\log(q+Jr+2)\right)=o(q)
\tag{HAR29}
\]

under \(r\log(q+2)=o(q)\). Indeed \(J\) is fixed, \(r=o(q/\log q)\), and \(k\log^2q=o(q)\). No assertion about a smaller source rank is used. Every original Gram eigenvalue therefore obeys

\[
|\log\lambda_j(H^X_{r,N}(\alpha))-\log h_N(\alpha)|\le E_{r,N},
\quad X=E,B,
\tag{HAR30}
\]

and \(|\log\det H^X_{r,N}(\alpha)-r\log h_N(\alpha)|\le rE_{r,N}\). The full relative observation bound is \(H^B\succeq e^{-2E_{r,N}}H^E\), uniformly in \(\alpha\). Its kernel consequences are recorded by the receiving kernel derivation; no initial angle has been discarded here.

At the four original cutoffs, \(n_0=0,0,q,q\), since \(q\) is even. Hence there are exactly two values \(\mathsf S_L,\mathsf S_H\). With the unchanged four signs,

\[
\boxed{
\left|\mathcal R\log\det H^X_{r,N}(\alpha)
-2r\log\frac{\mathsf S_L(1-\alpha+\alpha\mathsf S_H)}
{\mathsf S_H(1-\alpha+\alpha\mathsf S_L)}\right|
\le r\sum_N E_{r,N}.
}
\tag{HAR31}
\]

This is a finite all-activation enclosure using the two original scalar relation kernels.

## 5. Exact rectangular integral and a controlled lattice product

Write

\[
I_\square=\frac1{4\delta\gamma}
\int_{-\delta}^{\delta}\int_{-\gamma}^{\gamma}\log(x^2+y^2)\,dy\,dx.
\tag{HAR32}
\]

The logarithmic singularity is integrable. On the positive rectangle, apply
\(\operatorname{div}((x,y)\log(x^2+y^2))=2\log(x^2+y^2)+2\)
after removing a small quarter-disc; its circular boundary term tends to zero. The two outer boundary integrals use
\(\int_0^b\log(a^2+t^2)dt=b\log(a^2+b^2)-2b+2a\arctan(b/a)\).
Dividing by the rectangle area gives

\[
I_\square=\log(\delta^2+\gamma^2)-3
+\frac\delta\gamma\arctan\frac\gamma\delta
+\frac\gamma\delta\arctan\frac\delta\gamma.
\tag{HAR33}
\]

Here is a finite error bound for the exact lattice rather than an informal Riemann-sum argument. Put \(n=k+1\), and let
\(x_a=(2a-k)/n\), \(0\le a\le k\), be the midpoint grid on \([-1,1]\). For \(f(x,y)=\log(\delta^2x^2+\gamma^2y^2)\), the original product is exactly

\[
\log|Q(0)|^2=2q\log n+\sum_{a,b=0}^k f(x_a,x_b).
\tag{HAR34}
\]

The four central cells have centres \((\pm1/n,\pm1/n)\). Their centre value is \(-2\log n+\log R_0^2\), while their cell average is \(-2\log n+\log4+I_\square\), by the exact scaling of HAR32. Their total error is at most \(4|\log R_0^2-\log4-I_\square|\).

The shell with maximum centre-coordinate magnitude \((2j+1)/n\), \(j\ge1\), has \(8j+4\le12j\) cells. Every point in each such cell has Euclidean distance at least \(2j/n\) from zero. Since
\(\|\nabla f\|\le2\gamma^2/(\delta^2\sqrt{x^2+y^2})\), and the distance from the centre to a point of its cell is at most \(\sqrt2/n\), each centre-versus-cell-average error is at most \(\sqrt2\gamma^2/(\delta^2j)\). Summing at most \(n/2\) shells proves

\[
\left|\log|Q(0)|^2-2q\log k-qI_\square\right|
\le2q\log\frac{k+1}{k}
+\frac{6\sqrt2\gamma^2}{\delta^2}(k+1)
+4|\log R_0^2-\log4-I_\square|.
\tag{HAR35}
\]

The right side is \(O_{\delta,\gamma}(k)\), which also proves the received \(O_h(k\log(k+2))\) bound. The four central cells and every original root are retained.

## 6. The low Gamma monic norm and the unchanged source mass

Let \(\sigma_0=\Gamma(1/4)^2/(2\pi)\), \(a=1/4\), and \(u=|y|/2\). The original-author Gamma product gives

\[
\frac{\sigma(y)}{\sigma_0}=
\prod_{j=0}^\infty\left(1+\frac{u^2}{(j+a)^2}\right)^{-1}.
\]

The positive summand \(g(x)=\log(1+u^2/(x+a)^2)\) decreases, so its sum lies between \(\int_0^\infty g\) and \(g(0)+\int_0^\infty g\). Direct integration gives
\(\int_0^\infty g=2u\arctan(u/a)-a\log(1+u^2/a^2)\).
Substitution and \(0\le |y|\arctan(1/(2|y|))\le1/2\) prove

\[
\frac{\sigma_0e^{-\pi|y|/2}}{1+4y^2}
\le\sigma(y)
\le\sigma_0 e^{1/2}(1+4y^2)^{1/4}e^{-\pi|y|/2}.
\tag{HAR36}
\]

For the lower side the integral comparison first gives the stronger denominator \((1+4y^2)^{3/4}\), which implies the displayed bound. At \(y=0\) the formulas follow by continuity. Thus both received Gamma envelope constants are verified.

Let \(\nu_0^\Gamma=\int|Q(y)|^2d\sigma(y)\), retain \(R=kR_0\), and put \(c=\pi/2\), \(x_0=2q/c=4q/\pi\). The full root product gives \(|Q(y)|\le(|y|+R)^q\) everywhere, and \(|Q(y)|\ge(|y|-R)^q\) when \(|y|\ge R+1\). HAR36 and \((1+4y^2)^{1/4}\le1+2|y|\) give the explicit upper bound

\[
\nu_0^\Gamma\le
2\sigma_0e^{1/2+cR}
\left[\frac{\Gamma(2q+1)}{c^{2q+1}}
+\frac{2\Gamma(2q+2)}{c^{2q+2}}\right].
\tag{HAR37}
\]

For a lower bound integrate only \(y\in[R+x_0,R+x_0+1]\), where \(x_0>1\). No root is removed from \(Q\); the discarded integration region is used only for a lower bound. This gives

\[
\nu_0^\Gamma\ge
\frac{\sigma_0 x_0^{2q}e^{-c(R+x_0+1)}}
{1+4(R+x_0+1)^2}.
\tag{HAR38}
\]

The factorial estimate \(\log(n!)=n\log n-n+O(\log(n+2))\), obtainable by bounding the sum of \(\log j\) between its two adjacent integrals, now yields

\[
\log\nu_0^\Gamma
=2q\log q+(2\log(4/\pi)-2)q+O_h(k+\log q).
\tag{HAR39}
\]

It remains necessary to bound the actual \(u_k\), rather than only its ratio with the lower source constant. Put \(m_h=\int_{\mathbb R}w_h(y)dy>0\). The constant polynomial in NG2 gives
\(\ell_{k,N}\le m_h^k/M_\sigma\le u_k\).
The exact retained NG2 constants have
\(u_k=A_k\), \(\ell_{k,N}=a_k/[1+4(N+M)^2]^M\), \(M=25\) on this simple-quartet domain, and
\(\log(u_k/\ell_{k,N})=O_h(k+\log(N+1))\).
Therefore

\[
\log\frac{m_h^k}{M_\sigma}
\le\log u_k
\le\log\frac{m_h^k}{M_\sigma}
+\log\frac{u_k}{\ell_{k,N}},
\qquad |\log u_k|=O_h(k+\log q).
\tag{HAR40}
\]

The second inequality uses both the constant-polynomial bounds and the comparison ratio. The constant-polynomial test alone would be insufficient. No source mass has been divided out or changed.

Since \(K_{Q,0}(0,0)=1/\nu_0^\Gamma\), equations HAR8, HAR35, HAR39–40 prove

\[
\log\mathsf S_L=2q\ell_k+\beta_Lq+O_h(k+\log q),
\quad \ell_k=\log(q/k),
\quad a_0=\log(4/\pi),
\quad\beta_L=2a_0-2-I_\square.
\tag{HAR41}
\]

This lower endpoint has been derived directly from the full original lattice and Gamma product.

## 7. The high endpoint and the clipped coefficient

At the high endpoint, the exact IFH8 identity retains the monic polynomials \(V_j\) and squared norms \(\nu_j^\Gamma\) of \(Q^2d\sigma\):

\[
\log\frac{K_{Q,q}(0,0)}{K_{Q,0}(0,0)}
=2\log|V_q(0)|+\log\nu_0^\Gamma-\log\nu_q^\Gamma+\log\Xi_q.
\tag{HAR42}
\]

The original parity, Christoffel–Darboux formula, and finite hard gap give \(1\le\Xi_q\le4(2q+2)^2/\beta_q\), so \(\log\Xi_q=O(1)\). IFH8–10 applies the already retained full monic profile and zero law to the other terms, in their original source scale, and proves

\[
\log\frac{K_{Q,q}(0,0)}{K_{Q,0}(0,0)}
=\frac{\mathfrak C}{2}q+o_h(q),
\qquad
\mathfrak C=4[\psi(0)-\psi(1)-J(1)-1].
\tag{HAR43}
\]

This is the precise analytic source theorem imported for the high endpoint. Its original finite-zero gap permits the logarithmic test function in the zero law. The inherited positive interval \(1.353893<\mathfrak C<1.354751\) is not a new numerical computation in this note. Therefore

\[
\log\mathsf S_H=2q\ell_k+\beta_Hq+o_h(q),
\qquad\beta_H=\beta_L-\mathfrak C/2<\beta_L.
\tag{HAR44}
\]

In particular both \(\mathsf S_L,\mathsf S_H\) exceed 1 eventually.

For any \(s\ge1\), \(0\le\alpha\le1\), the exact denominator obeys
\(\max(1,\alpha s)\le1-\alpha+\alpha s\le2\max(1,\alpha s)\).
Taking logarithms proves

\[
\min(\log s,-\log\alpha)-\log2
\le\log\frac{s}{1-\alpha+\alpha s}
\le\min(\log s,-\log\alpha),
\tag{HAR45}
\]

with \(-\log0=+\infty\). This proves the constant \(\log2\) uniformly, including the activation endpoints.

Let
\(\alpha_k(\zeta)=\exp[-2q\ell_k-\zeta q]\).
Its exact physical domain is \(\zeta\ge-2\ell_k\); \(\alpha=0\) is its endpoint \(\zeta=+\infty\). Define the endpoint error

\[
\epsilon_k^{\rm end}=
\max_{T=L,H}|\log\mathsf S_T-2q\ell_k-\beta_Tq|=o_h(q).
\tag{HAR46}
\]

Since \(x\mapsto\min(x,c)\) is 1-Lipschitz, HAR30 and HAR45 imply the finite uniform estimate

\[
\boxed{
\left|\log\lambda_j(H^X_{r,N}(\alpha_k(\zeta)))
-2q\ell_k-q\min(\beta_{L/H},\zeta)\right|
\le E_{r,N}+\epsilon_k^{\rm end}+\log2.
}
\tag{HAR47}
\]

It holds for every eigenvalue, \(X=E,B\), and every physical \(\zeta\ge-2\ell_k\), once \(\mathsf S_L,\mathsf S_H\ge1\). Thus the limiting error is uniform on that entire moving domain, not only on its fixed compact subsets. It applies to every sequence of physical activations through this exact finite inequality.

Summing the \(r\) eigenvalue logarithms with the unchanged four cutoff signs yields

\[
\boxed{
\mathcal R\log\det H^X_{r,N}(\alpha_k(\zeta))
=rq\mathfrak C_{\rm inv}(\zeta)+o_{h,A}(rq),
\quad
\mathfrak C_{\rm inv}(\zeta)=2[\min(\beta_L,\zeta)-\min(\beta_H,\zeta)].
}
\tag{HAR48}
\]

An explicit error is
\(r\sum_NE_{r,N}+4r\epsilon_k^{\rm end}+4r\log2\), independent of \(\zeta\). Because \(\mathfrak C>0\), this coefficient equals 0 on \(\zeta\le\beta_H\), equals \(2(\zeta-\beta_H)\) between the two thresholds, and equals \(\mathfrak C\) on \(\zeta\ge\beta_L\). The theorem covers \(r=k\) and every admitted \(r\log(q+2)=o(q)\).

Finally \(\log(x^2+y^2)>\log(y^2)\) almost everywhere in the positive rectangle, so
\(I_\square>\gamma^{-1}\int_0^\gamma\log(y^2)dy=2\log\gamma-2\).
Hence

\[
\beta_L<2\log\frac4{\pi\gamma}<0.
\tag{HAR49}
\]

For the coarser source activation \(e^{-2bq\ell_k}\), \(b\ge0\), the exact substitution is \(\zeta_k=2(b-1)\ell_k\). The uniform result HAR48 therefore gives zero return coefficient for fixed \(0\le b<1\), and \(\mathfrak C\) for fixed \(b>1\). At \(b=1\), \(\zeta=0>\beta_L\) by HAR49, so the latter value includes that endpoint. This is an application of a proved uniform finite estimate, not a moving-parameter substitution into a merely pointwise theorem.

## 8. Exact finite checks and their limits

`check_harmonic.py` was written independently in this intake and executed with Python and SymPy. Its `HARMONIC_EXACT_CHECKS.json` records **358 passing exact checks**. They include both coordinate-direction derivative-product identities on the actual rectangular coordinates \(\delta=1/4,\gamma=3\), at \(k=1,5,9\); the exact four central derivative minima; every shell-count and shell-distance inequality used above; and a noncommuting complex-rational source fixture with all source and observation cross terms present.

For that fixture every principal minor is checked exactly for the full-space trace order, the joint metric enclosure, the canonical observed left inverse, and the harmonic source and observed inequalities at activations \(0,1/13,1/2,1\). Its coefficient frame consists of the literal inverse powers of the four roots \(\pm3\pm i/4\). The scalar clipping check uses its equivalent rational denominator bounds, including both activation endpoints.

These checks establish exact finite algebra for their declared fixtures. They do not evaluate native arithmetic moments or an actual period, and the small lattice tests do not claim the eventual hard-gap guards. The asymptotic high coefficient retains the exact IFH/H-profile source status identified in HAR42–44. The complete received arithmetic-action and heat statements outside equations (10)–(26) are not claimed to have been independently proved by this harmonic derivation.
