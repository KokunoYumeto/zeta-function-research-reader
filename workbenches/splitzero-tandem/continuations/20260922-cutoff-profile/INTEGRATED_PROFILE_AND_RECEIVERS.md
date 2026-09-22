# The complete cutoff profile and its original receiving maps

Result **SZ-20260922-025** extends the evaluated original kernel coefficient to every cutoff between \(q-1\) and \(2q\). The proof includes the full constrained kernel, each exceptional quotient, every affine source minimum and the separate positive-word and observed-heat maps. Its endpoint returns agree with the published024 result; they are not added a second time.

## IR1. Original objects, domain and complete result

Retain the original fixed hypothetical simple quartet with \(0<\delta<1/2\), \(\gamma>2\), its admitted actual period, branch and arithmetic unit. Keep

\[
 k\ge17,\ k\equiv1\pmod4,\quad q=(k+1)^2,\quad q'=(k-7)^2,
 \quad m=8k-16,\quad\Delta=q-q'=16k-48.
 \tag{IR1}
\]

The coefficient space is \(E_k=\mathbb C[y]/(Q_k)\), where

\[
 Q_k(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta]=D_k(y)O_k(y).
 \tag{IR2}
\]

The physical coordinate is \(S=k/2+iy\), and the arithmetic action is \(k/2+iM\), \(M[p]=[yp]\). The fixed original onto map \(\Lambda:E_k\to B_k\) has its full kernel \(K_k\) and fixed frame \(I_K\). This kernel includes every extra invariant row in addition to the conductor condition. Its rank is \(m\). At the original complete source cutoff \(N\), \(G_N\) is the attained coefficient metric and

\[
 H_{K,N}=I_K^*G_NI_K,\quad Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},
 \quad L_N=G_N^{-1}\Lambda^*Q_{B,N}.
 \tag{IR3}
\]

All roots, difference factors, complex cross terms, Gamma mass \(\sqrt{2\pi}\), and both real integration regions remain as in024. The original four-cutoff return is

\[
 \mathcal RF=F_{q-1}+F_q-F_{2q-1}-F_{2q}.
 \tag{IR4}
\]

Set \(N_j=q-1+j\), \(t_j=j/q\), \(0\le j\le q+1\). Define \(J\) by EP1–EP8, equivalently the supplied CP3, with \(J(0)=0\). For

\[
 B_{ij}=H_{K,N_j}^{-1/2}H_{K,N_i}H_{K,N_j}^{-1/2},\quad
 d_{ij}=q[J(t_j)-J(t_i)],
 \tag{IR5}
\]

the completed independent proof PP1–PP45 gives

\[
 \sup_{0\le i\le j\le q+1}\sum_{a=1}^m
 |\log\lambda_a(B_{ij})-d_{ij}|=o(mq).
 \tag{IR6}
\]

Its finite estimate, before limits, is

\[
 \sum_a|\log\lambda_a(B_{ij})-d_{ij}|
 \le2mq\eta_{k,\epsilon}
 +2(v_0+c_R)q[C_0+J(1+1/q)].
 \tag{IR7}
\]

Here \(\eta_{k,\epsilon}\) is the full explicit quantity PP40; it includes the complete jet error PP36, the actual two-region source comparison and the arithmetic/Gamma width. The fixed residue error has codimension at most \(v_0+c_R\) *after restriction to the actual invariant kernel*. Its complete exceptional quotient has not been deleted. First \(k\to\infty\) for fixed \(\epsilon,R\); then \(\epsilon\downarrow0\). The proof does not exchange these limits or allow an unproved moving-period substitution.

Summing the actual relative eigenvalues proves

\[
 \boxed{\log\frac{\det H_{K,q-1}}{\det H_{K,N_j}}
 =mqJ(j/q)+o(kq),\quad\text{uniformly for all }0\le j\le q+1.}
 \tag{IR8}
\]

The original four signs give

\[
 \mathcal R\log\det H_{K,N}
 =mq[J(1)+J(1+1/q)-J(1/q)]+o(kq)
 =mC_\partial q+o(kq),
 \tag{IR9}
\]

because \(J(1)=C_\partial/2\) and \(J\) is continuous. Both adjacent degrees are present. This recovers [024 CK14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md#L148) without changing its coefficient.

## IR2. Exact single-source growth and its limiting measure

Let \(\phi_{N+1}\) be the next actual original source polynomial of unit norm, and \(u_N=[\phi_{N+1}]\in E_k\) its entire remainder. The complete source covariance is the sum of its column outer products, so appending this source gives exactly

\[
 G_{N+1}^{-1}=G_N^{-1}+u_Nu_N^*.
 \tag{IR10}
\]

In the actual metric at \(N\), put

\[
 \rho_N=u_N^*G_Nu_N,\quad b_N=I_K^*G_Nu_N,\quad
 \chi_N=b_N^*H_{K,N}^{-1}b_N,\quad
 \beta_N=(\Lambda u_N)^*Q_{B,N}(\Lambda u_N).
 \tag{IR11}
\]

The two maps \(P_K=I_KH_{K,N}^{-1}I_K^*G_N\) and \(P_B=L_N\Lambda\) are complementary \(G_N\)-orthogonal projections. Indeed \(\Lambda L_N=I\), \(\Lambda I_K=0\), \(L_N^*G_NI_K=0\), and their ranks sum to \(q\). Thus \(u_N=P_Ku_N+P_Bu_N\) gives

\[
 \rho_N=\chi_N+\beta_N.
 \tag{IR12}
\]

Multiplying \(G_N-G_Nu_Nu_N^*G_N/(1+\rho_N)\) by the covariance in IR10 gives the identity matrix directly. Restricting that inverse to the unchanged original kernel and taking its determinant gives

\[
 H_{K,N+1}=H_{K,N}-\frac{b_Nb_N^*}{1+\rho_N},\qquad
 \boxed{a_{j,k}:=\log\frac{\det H_{K,N_j}}{\det H_{K,N_{j+1}}}
 =\log\frac{1+\rho_{N_j}}{1+\beta_{N_j}}\ge0.}
 \tag{IR13}
\]

To verify the determinant step, conjugate by \(H_{K,N}^{-1/2}\). The resulting rank-one perturbation has eigenvalue \(1-\chi_N/(1+\rho_N)=(1+\beta_N)/(1+\rho_N)>0\) on its one possible nontrivial direction and eigenvalue one on its orthogonal complement. This also covers \(b_N=0\). All complex pairings in IR11 are kept. The finite inverse update is the classical Sherman–Morrison identity; the direct proof here fixes its exact domain and convention rather than relying on its name.

Define the actual finite positive measure, with the last adjacent increment included,

\[
 \nu_k=\frac1{mq}\sum_{j=0}^{q}a_{j,k}\,\delta_{j/q}.
 \tag{IR14}
\]

Its mass tends to \(J(1)=C_\partial/2\); it is not declared a probability. Put

\[
 \varepsilon_k=\max_{0\le j\le q+1}
 \left|\frac1{mq}\log\frac{\det H_{K,N_0}}{\det H_{K,N_j}}-J(j/q)\right|.
\]

IR6 gives \(\varepsilon_k\to0\), with its finite estimate IR7 divided by \(mq\). For \(0\le t\le1\), telescoping gives

\[
 \left|\nu_k([0,t])-J(t)\right|
 \le\varepsilon_k+\omega_J(1/q),\quad
 \max_j\frac{a_{j,k}}{mq}\le2\varepsilon_k+\omega_J(1/q).
 \tag{IR15}
\]

Here \(\omega_J(h)=\sup|J(x)-J(y)|\) for \(x,y\in[0,1+1/q]\), \(|x-y|\le h\). To obtain the first bound use the exact index \(\lfloor qt\rfloor+1\); at \(t=1\) this is \(q+1\), not \(q\). To obtain the second subtract the two endpoint determinant approximations. EP12 gives \(\omega_J(h)\le J(h)\).

For a continuously differentiable test \(\varphi\), integration of 

\[
 \varphi(s)=\varphi(1)-\int_s^1\varphi'(t)dt
\]

against the difference of the two finite measures, followed by Fubini, yields

\[
 \left|\int\varphi\,d\nu_k-\int_0^1\varphi(t)f(t)dt\right|
 \le\left(|\varphi(1)|+\int_0^1|\varphi'(t)|dt\right)
 [\varepsilon_k+J(1/q)],\quad
 f(t)=\log\frac{1+r_t}{1-r_t}.
 \tag{IR16}
\]

The endpoint singularity of \(f\) is integrable by EP15. Piecewise linear approximation of any continuous test, together with the bounded total masses in IR15, proves \(\nu_k\Rightarrow f(t)dt\). This is the full first-response angular-increment conclusion. It does not differentiate a finite-grid error or infer an individual microscopic source allocation from a macroscopic profile.

For fixed \(0\le a<b\le1\), let \(i=\lfloor aq\rfloor\), \(j=\lfloor bq\rfloor\). For all sufficiently large \(q\), \(i<j\). The original observable fractions obey the exact product identity

\[
 \left[\prod_{h=i}^{j-1}\frac{1+\beta_{N_h}}{1+\rho_{N_h}}\right]^{1/[m(j-i)]}
 =\exp\left(-\frac{\log\det H_{K,N_i}-\log\det H_{K,N_j}}{m(j-i)}\right)
 \longrightarrow\exp\left(-\frac{J(b)-J(a)}{b-a}\right).
 \tag{IR17}
\]

The exponent and its division by \(m(j-i)\) are part of this explicitly defined scalar observable. IR13 proves its map from the unchanged source data.

## IR3. Every complete fixed subquotient

Let \(I_X:X\to K_k\) be a fixed coefficient injection and \(R:X\to Z\) a fixed onto coefficient map, both independent of cutoff. Define

\[
 H_{X,N}=I_X^*H_{K,N}I_X,\qquad Q_{Z,N}=(R H_{X,N}^{-1}R^*)^{-1}.
 \tag{IR18}
\]

The minimum section \(H_{X,N}^{-1}R^*Q_{Z,N}\) maps \(z\) to a lift with norm squared \(z^*Q_{Z,N}z\); every other lift differs by a vector of \(\ker R\) orthogonal to it. Pythagoras proves that IR18 is the minimum over the entire affine fibre, with all cross terms retained.

For restriction, set \(V_j=H_{K,N_j}^{1/2}I_XH_{X,N_j}^{-1/2}\). Direct multiplication gives

\[
 V_j^*V_j=I_X,\quad
 H_{X,N_j}^{-1/2}H_{X,N_i}H_{X,N_j}^{-1/2}=V_j^*B_{ij}V_j.
 \tag{IR19}
\]

For the complete quotient, put

\[
 C_{ij}=H_{X,N_i}^{1/2}H_{X,N_j}^{-1}H_{X,N_i}^{1/2},\qquad
 U_i=Q_{Z,N_i}^{1/2}R H_{X,N_i}^{-1/2}.
\]

Then

\[
 U_iU_i^*=I_Z,\qquad
 Q_{Z,N_i}^{1/2}Q_{Z,N_j}^{-1}Q_{Z,N_i}^{1/2}=U_iC_{ij}U_i^*.
 \tag{IR20}
\]

The eigenvalues of \(C_{ij}\) equal those of the relative pair in IR19: they are the eigenvalues of the two matrices \(AA^*\) and \(A^*A\), for \(A=H_{X,N_j}^{-1/2}H_{X,N_i}^{1/2}\), up to exchanging their order. The corresponding equality holds for the two orientations of the relative quotient matrix in IR20. These are similarities of positive matrices, not identifications of their eigenvectors.

To see precisely why the bounded exceptional count persists, suppose a self-adjoint matrix has at most \(c\) eigenvalues above \(u\). Its quadratic form is at most \(u\) on the orthogonal complement of their spectral space. If an isometric compression had \(c+1\) eigenvalues above \(u\), its corresponding image would intersect that complement nontrivially, a contradiction. The argument below a lower threshold is identical with the inequality reversed. IR19 and IR20 therefore preserve PP42–PP44's at most \(c\) exceptions at each end, and preserve its full coarse interval \(1\le\lambda\le e^{C_0q}\).

For \(d_k=\dim Z\to\infty\), the identical finite argument gives

\[
 \sum_{a=1}^{d_k}\left|
 \log\lambda_a(Q_{Z,N_j}^{-1/2}Q_{Z,N_i}Q_{Z,N_j}^{-1/2})-d_{ij}\right|
 \le2d_kq\eta_{k,\epsilon}
 +2(v_0+c_R)q[C_0+J(1+1/q)].
 \tag{IR21}
\]

First let \(k\to\infty\), then \(\epsilon\downarrow0\), as before. Dividing by \(d_kq\) proves CQ3, uniformly over all pairs of cutoffs. Determinants and the entire increment measure IR14–IR16 follow with \(m\) replaced by \(d_k\). No lower bound on the growth rate of \(d_k\) is needed beyond its divergence: the exceptional codimension is fixed before this limit. For fixed \(d_k\), IR21 remains a finite bound; its exceptional term cannot be dropped. This retains rather than assumes the missing information in that different rank regime.

## IR4. Measured phase and heat receivers

Keep \(T=D_k(M)\), \(H_N=G_N^{-1}T^*G_NT\) and the same \(L_N,\Lambda\). The full proofs PH1–PH41 supply the exact image map, all-vector word metric, every compressed kernel energy and the resolvent determinant. In particular, with

\[
 c_k(t)=2q\log q+q[2\log(4/\pi)-2-J(t)],
\]

the complete positive word spectrum has logarithms \(c_k(t_j)+o(q)\) uniformly over every direction and cutoff. The paired compressed-kernel energies have total logarithmic transport \(o(kq)\). PH18–PH20 then prove for every cutoff pair

\[
 \frac2\pi\int_0^\infty(\Theta_{N_i}(\omega)-\Theta_{N_j}(\omega))\frac{d\omega}\omega
 =\Delta q[J(t_j)-J(t_i)]+o(kq).
 \tag{IR22}
\]

The finite error is \(\mathcal B_{ij}=D_{ij}+E_i^W+E_j^W\) in PH15, and the full \(L^1(d\omega/\omega)\) error is at most \(\pi\mathcal B_{ij}/2\). Both frequency ends are included. Adding pairs \((0,q)\) and \((1,q+1)\) gives \(+\Delta C_\partial q+o(kq)\), preserving the original four signs. At \(\omega=q^{2q}e^{bq}\), the pair phase divided by \(k\) approaches height \(8\pi\) between the evaluated boundaries \(\eta(t_j)\) and \(\eta(t_i)\); the original four-cutoff height is \(16\pi\).

The first response's separate heat calculation is retained in PH22–PH41. It uses the physical time \(\tau=q^{-2q}e^{-q\xi}\) and the \(q\) declared averaging cutoffs \(j=0,\ldots,q-1\). The original integer-subtracted measured heat \(M_k\) has the exact decomposition \(M_k=F_k+D_k^{\rm ang}\), where \(F_k\) is the full positive-word heat average and \(0\le D_k^{\rm ang}\le\alpha_k\). Its left endpoint is \(\alpha_k\), not zero. PH34 sharpens its uniform smoothing error to

\[
 \varepsilon_k^{\rm heat}=\frac{\delta_k}{f(1)}+\frac1q
 +\frac{\gamma_{\rm E}+2E_1(1)}{qf(1)}.
 \tag{IR23}
\]

The actual measured error is bounded by this quantity plus its retained angle defect. The affine map to a probability heat is proved in PH36, and its complete transport and exact Euler-constant bias are in PH38–PH40. These are additional observables connected to the original one, not replacements for it.

## IR5. Corrections, checks, and the continuing programme

Both final responses were already in the incoming paste. Comparison with the full session transcript found only formatting, source-link display, and duplicated attachment labels. Their distinct mathematical passages are both included: first-response heat, rank-one increments and endpoint expansion; second-response complete subquotients.

The exact scalar computation keeps a term that the incoming text's phrase about cancelling every power of \(n\) omitted: PP24 contains \(-\tfrac12\log n\) in its finite remainder. The leading coefficient is unchanged. EP16 strengthens the endpoint expansion and EP18 independently certifies the half-volume position. Incoming scripts were not provided with the files; their reported59 exact checks are recorded as supplied reports. This edition's independent exact and interval checks have their own receipts and scope.

This result extends control of the original kernel, word energies, observed resolvent and measured heat throughout the source window. The separate complex arithmetic current remains the original insertion

\[
 i(Q_{B,N}M_{B,N}-M_{B,N}^*Q_{B,N}).
 \tag{IR24}
\]

Its individual marked-class pairings involve the actual complex response ratios and complete-action cancellation. The positive-word spectra in IR22 do not assign their signs. The exact original current and response maps remain in the retained proof sources; the next programme calculation is their phase-bearing numerator. No result here claims an RH proof or a hypothetical zero computation.
