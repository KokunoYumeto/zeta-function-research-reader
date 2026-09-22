# Original arithmetic evolution on a subexponential clock

22 September 2026. Independent derivation EE1–48. The incoming continuation is checked here on the unchanged original simple-quartet family, fixed arithmetic source, period and branch. Every estimate below uses the complete original source minimum and observation. The central additions are a growing source-jet estimate, characteristic-polynomial control of repeated rank-one feedback, and an actual inverse formula for the measured propagator. These give the previously inaccessible lower time plateau. They do not determine the residual terminal current or establish RH.

## 1. Exact original inputs, conventions and source locators

Let \(k\ge17\), \(k\equiv1\pmod4\), \(q=(k+1)^2\), \(q_0=(k-7)^2\), and \(\Delta=q-q_0=16k-48\). Retain
\[
Q_k(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta],
\quad 0<\delta<1/2,\quad\gamma>2,\quad E=\mathbb C[y]/Q_k .
\tag{EE1}
\]
The four cutoffs are \(N=q-1,q,2q-1,2q\), with return signs \(+,+,-,-\). Write \(s_N=(N+1-q)/q\). All estimates also hold throughout this original degree window when the stated finite guards hold.

Let \(G_N\) be the full source-minimum metric, \(\Lambda:E\to B\) the unchanged observation and
\[
Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
L_N=G_N^{-1}\Lambda^*Q_{B,N},\quad
J=L_NQ_{B,N}^{-1/2},\quad P=JJ^\dagger=L_N\Lambda,\quad\Pi=I-P.
\tag{EE2}
\]
The dagger is the original \(G_N\)-adjoint. Thus \(J^\dagger J=I_B\). All displayed compressed matrices act in these isometric coordinates; transporting them by \(Q_{B,N}^{1/2}\) gives precisely the original observed-metric operators.

The original orthogonal polynomials \(p_n\), their squared norms \(\omega_n\), and the complete relation minima give exactly
\[
M=C+R,\quad C=C^\dagger,\quad
R=\epsilon fe^\dagger,\quad e^\dagger f=0,\quad\|e\|=\|f\|=1,
\]
\[
e=[p_N]/\sqrt{E_N},\quad f=[p_{N+1}]/\sqrt{F_N},\quad
\epsilon=\sqrt{E_NF_N}/\omega_N.
\tag{EE3}
\]
These are [OCP5–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L90), rederived there by exact projection of real multiplication onto the complete minimum-lift subspace. The isometry and measured/intrinsic distinction are [CE2–3, CE24–29](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/EVOLUTION_PROOF.md#L18).

Put \(u=J^\dagger e\), \(v=J^\dagger f\), \(a=u^*u\), \(d=v^*v\), \(r=u^*v\), \(R_B=\epsilon vu^*\), and \(\epsilon_B=\epsilon\sqrt{ad}\). The complete two-column certificate is
\[
0\prec\Theta I_2\preceq
\begin{pmatrix}a&r\\\bar r&d\end{pmatrix}\preceq I_2,\qquad
ad-|r|^2\ge\Theta .
\tag{EE4}
\]
The determinant assertion is retained explicitly: the matrix lower bound alone would only give determinant at least \(\Theta^2\). It follows that
\[
\epsilon\sqrt\Theta\le\epsilon_B\le\epsilon,\quad
|r|=|e^\dagger\Pi f|\le\sqrt\alpha,\quad
\alpha=\|\Pi e\|^2.
\tag{EE5}
\]
Here \(e^\dagger f=0\) was used, with its sign: \(r=-e^\dagger\Pi f\).

The proved source cost and monic inputs are [RC22–25](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L222):
\[
\ell_k\|p\|_\sigma^2\le\|p\|_{\mu_k}^2\le u_k\|p\|_\sigma^2
\quad(\deg p\le2q+2),\qquad \log(u_k/\ell_k)=O_h(k+\log q),
\]
\[
\log\epsilon=q\psi(s_N)+O_{h,\varpi}(k\log(q+2)),\quad
-\log\Theta=O_{h,\varpi}(k\log(q+2)),
\quad\alpha\le e^{-2q\psi(s_N)+O_{h,\varpi}(k\log(q+2))}.
\tag{EE6}
\]
The Gamma measure is
\[
d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy,\qquad
h_n=\sqrt{2\pi}\,n!(1/2)_n.
\tag{EE7}
\]
Choose throughout
\[
c=\max\{1,\,2(N+1)\sqrt{u_k/\ell_k}\}.
\tag{EE8}
\]
It bounds the full arithmetic degree-\(N\) Jacobi compression \(Y_N\), its compression \(C\), and \(C_B=J^\dagger CJ\). Indeed the Gamma orthonormal recurrence has off-diagonal coefficient \(\sqrt{(n+1)(n+1/2)}\); the two neighboring diagonals bound real multiplication on degree at most \(N\) by \(2(N+1)\). Applying the same source comparison in degrees \(N,N+1\) proves EE8. This stronger choice is necessary when telescoping through \(Y_N\).

The human recurrence and generating function are T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, [DLMF18.22.8](https://dlmf.nist.gov/18.22.E8) and [18.23.7](https://dlmf.nist.gov/18.23.E7), with \(\lambda=1/4\), \(\phi=\pi/2\), \(x=y/2\). Their original equation TeX was read and retained in the preceding CE source directory. This reading covers those formulas, not the entire chapter. All programme-specific transfers are proved below.

## 2. Complete growing-jet estimates

The conductor from [OCP11–14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L157) is
\[
\mathcal T p=\sum_{a,b=0}^8a_{ab}p(y+\sigma_{ab}),\quad
\sigma_{ab}=(2b-8)\gamma-i(2a-8)\delta.
\]
Its first nonzero moment order \(v_0\le80\) is fixed, and its nonzero leading coefficient on degree \(n\) is
\[
\tau_n=i^{-v_0}\mu_{v_0}\binom n{v_0}.
\]
The exact lower-quotient map \(C_A[p]=[\mathcal Tp]_{Q_{k-8}}\) obeys \(K=\ker\Lambda\subset\ker C_A\). Thus every minimum-lift polynomial of an original kernel class satisfies
\[
\mathcal Tp\in Q_{k-8}\mathcal P_{D-q_0},\qquad D=N-v_0.
\tag{EE9}
\]
No equality of the two kernels is used. The full finite Gamma conductor norm is
\[
\|\mathcal T\|_{\sigma,\mathcal P_N\to\mathcal P_D}
\le\mathcal F_N=A_1e^{1+2\pi\gamma}(N+1)(2N+1)^{4\delta+1/2},
\quad A_1=\sum|a_{ab}|.
\tag{EE10}
\]
It follows by multiplying the original generating function by each \(e^{\sigma_{ab}\arctan z}\), applying Cauchy's coefficient bound at \(N/(N+1)\), and summing all diagonals; the full derivation is OCP13.

For an integer \(0\le J\le k\), retain the guard \(J\le D-q_0\). It holds at all four cutoffs: \(D-q_0-J\ge15k-49-v_0\ge0\) for the stated \(k\ge17,v_0\le80\). Let \(\nu_j^{-,\sigma}\) and \(\nu_j^{+,\sigma}\) be the complete monic minima for \(|Q_{k-8}|^2d\sigma\) and \(|Q_k|^2d\sigma\). Their original roots are all retained.

Here is a finite coefficient lemma used twice. If two monic polynomial families of degree at most \(D\) have all roots of modulus at most \(B\ge1\), the coefficient \(l\) places below their leading terms is at most \((DB)^l\). Conversion between the two families therefore costs at most \((2DB)^l\): recursively cancel the leading terms; with \(A=DB\), the coefficient bound satisfies
\[
b_l\le A^l+\sum_{j=0}^{l-1}b_jA^{l-j},\quad b_0=1,
\]
Direct triangular subtraction and induction therefore give
\(b_l\le A^l+\sum_{j=0}^{l-1}(2A)^jA^{l-j}
\le(2A)^l\).
This last sum is \(A^l(1+2^l-1)\). The bound includes all lower coefficients and needs no location on the real line for the roots of \(Q\).

The residual orthogonal polynomials for \(|Q|^2d\sigma\) do have real roots of modulus at most \(2(D+1)\): their zeros are eigenvalues of the compressed multiplication matrix on \(Q\mathcal P_{j-1}\), which is a compression of Gamma multiplication on degree at most \(D-1\). The ordinary Gamma polynomials have the same bound. The preceding coefficient lemma therefore applies with
\[
Z_-=2(D+1)\max\{1,R_{k-8},2(D+1)\},
\]
\[
(\mathcal E^-_{N,J})^2=
\sum_{i=0}^J\sum_{j=i}^J
Z_-^{2(j-i)}\frac{h_{D-j}}{\nu^{-,\sigma}_{D-q_0-i}}.
\tag{EE11}
\]
Expand every orthonormal relation row
\(Q_{k-8}U_{D-q_0-i}/\sqrt{\nu^{-,\sigma}_{D-q_0-i}}\)
in the original Gamma basis. Its coefficient at degree \(D-j\) is zero for \(j<i\), and at most the square root of the corresponding summand in EE11 otherwise. All other relation rows have degree below \(D-J\), so contribute exactly zero. The Frobenius bound on this complete finite matrix proves that \(\mathcal E^-_{N,J}\) bounds the full leading-jet map on the lower ideal.

Let \(A_J\) be the conductor matrix between the normalized Gamma top jets of degrees \(N,\ldots,N-J\) and \(D,\ldots,D-J\). Its diagonal entries are
\(\tau_{N-j}\sqrt{h_{D-j}/h_{N-j}}\), its norm is at most \(\mathcal F_N\), and it is triangular because the conductor lowers every degree by \(v_0\). Put
\[
\beta_{N,J}=
\max\left\{1,\mathcal F_N
\max_{0\le j\le J}\frac{\sqrt{h_{N-j}}}
{|\tau_{N-j}|\sqrt{h_{D-j}}}\right\},
\]
\[
\mathcal T_{N,J}=\beta_{N,J}
\sum_{\ell=0}^J[(J+1)\beta_{N,J}]^\ell.
\tag{EE12}
\]
To prove this inverse bound, divide \(A_J\) by \(\mathcal F_N\), split its diagonal and strictly triangular part, and invert \(I+H\) by \(\sum_{\ell=0}^J(-H)^\ell\). Each entry of \(A_J/\mathcal F_N\) has modulus at most one, its inverse diagonal norm is at most \(\beta_{N,J}\), and \(\|H\|\le(J+1)\beta_{N,J}\). Hence
\(\|(A_J/\mathcal F_N)^{-1}\|\le\mathcal T_{N,J}\).
For every \(p\) satisfying EE9,
\[
\|\operatorname{top}_{J+1}^{\sigma}p\|
\le\mathcal T_{N,J}\mathcal E^-_{N,J}\|p\|_\sigma.
\tag{EE13}
\]
The apparent missing conductor factor cancels exactly: applying the inverse gives \(1/\mathcal F_N\), whereas
\(\|\mathcal Tp\|_\sigma\le\mathcal F_N\|p\|_\sigma\).

Transfer the entire affine leading-jet fibre once. For every polynomial \(p\),
\[
\ell_k\,\operatorname{dist}_\sigma(p,\mathcal P_{N-J-1})^2
\le\operatorname{dist}_{\mu_k}(p,\mathcal P_{N-J-1})^2
\le u_k\,\operatorname{dist}_\sigma(p,\mathcal P_{N-J-1})^2.
\tag{EE14}
\]
Taking infima of the same source inequalities proves both sides. Let \(\Phi_{N,J}\) be the orthonormal arithmetic polynomial frame
\((p_N/\sqrt{\omega_N},\ldots,p_{N-J}/\sqrt{\omega_{N-J}})\).
Let \(P_K^{\rm pol}\) project onto the complete minimum-lift kernel in \(\mathcal P_N\), and \(P_I\) onto the full relation ideal \(Q_k\mathcal P_{N-q}\). Applying EE14 to EE13 on the former subspace, then taking the adjoint of its top-jet map, proves
\[
\|P_K^{\rm pol}\Phi_{N,J}\|
\le L_{K,N,J}:=\sqrt{u_k/\ell_k}\,
\mathcal T_{N,J}\mathcal E^-_{N,J}.
\tag{EE15}
\]
The metric ratio occurs once for this whole map, not at every jet order.

For the original upper relation ideal the same coefficient proof gives
\[
Z_+=2(N+1)\max\{1,R_k,2(N+1)\},
\]
\[
(\mathcal E^+_{N,J})^2=
\sum_{i=0}^{\min(J,N-q)}\sum_{j=i}^J
Z_+^{2(j-i)}\frac{h_{N-j}}{\nu^{+,\sigma}_{N-q-i}},
\quad
L_{I,N,J}:=\sqrt{u_k/\ell_k}\,\mathcal E^+_{N,J},
\]
\[
\|P_I\Phi_{N,J}\|\le L_{I,N,J}.
\tag{EE16}
\]
For \(N=q-1\) the ideal and this sum are zero. Every absent row has degree below the jet and contributes zero; no relation is omitted on the other three cutoffs.

The authoritative monic input is [LRS11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L83884), with its exact Gamma cancellation and original lower roots; its receiver RC23 states
\[
\log\frac{\nu^{(b),\sigma}_j}{h_{Q_b+j}}
=2Q_b\psi(j/Q_b)+O_h(\log q),\quad
0\le j\le2Q_b,\quad b=k,k-8.
\tag{EE17}
\]
All indices in EE11 and EE16 lie in that interval eventually, including zero. Replacing \(j\) by \(j-i\) shifts the argument by at most \(J/Q_b\). The exact endpoint derivative
\(\psi'(t)=\tfrac14\log t+\log(4/\pi)+O(\sqrt t)\), and bounded derivatives away from zero, give total exponent displacement \(O((k+J+1)\log(q+2))\), including \(q-q_0=O(k)\). Also
\[
\frac{h_{N-j}}{h_{N-i}}\le1\quad(j\ge i),\qquad
\log Z_\pm=O_h(\log q).
\]
The normalized conductor diagonal satisfies exactly
\[
|\tau_n|^2\frac{h_{n-v_0}}{h_n}
=\frac{|\mu_{v_0}|^2}{(v_0!)^2}
\prod_{l=0}^{v_0-1}\frac{n-l}{n-l-1/2},
\]
so its positive and negative logarithms are bounded on the fixed data. Thus \(\log\beta_{N,J}=O_{h,\varpi}(\log q)\) and
\(\log\mathcal T_{N,J}=O_{h,\varpi}((J+1)\log(q+2))\).
Counting the at most \((J+1)^2\) summands now proves the uniform estimate
\[
L_{K,N,J}+L_{I,N,J}
\le \exp[-q\psi(s_N)+
O_{h,\varpi}((k+J+1)\log(q+2))].
\tag{EE18}
\]
This is a proved growing-jet bound derived from the complete source, rather than a fixed-order estimate extrapolated to \(J=k\).

In polynomial coordinates the observed orthogonal projection is \(I-P_I-P_K^{\rm pol}\). The latter two projections have orthogonal ranges. Therefore
\[
[1-L_{K,N,J}^2-L_{I,N,J}^2]I
\preceq\Phi_{N,J}^*(I-P_I-P_K^{\rm pol})\Phi_{N,J}\preceq I.
\tag{EE19}
\]
This is the Gram of the specified source columns after their actual observation, not a replacement kernel frame.

Put \(S=I-P_I\), \(z=p_N/\sqrt{\omega_N}\), and \(\vartheta=\|Sz\|^2=E_N/\omega_N\). The isometry from source quotient to \(S\mathcal P_N\) sends \(e\) to \(Sz/\sqrt\vartheta\) and \(C\) to \(SY_NS\) restricted to that subspace. Since \(Y_N\) is tridiagonal, \(Y_N^jz\) belongs to the final \(j+1\) polynomial directions. Telescoping gives, for \(j\le J\),
\[
\|(SY_NS)^jSz-Y_N^jz\|\le(j+1)L_{I,N,J}c^j .
\]
The initial error is \(L_I\); each subsequent step adds at most \(L_Ic^j\), since \(\|Y_N\|\le c\). Taking \(P_K^{\rm pol}\) and using EE15 proves
\[
\|\Pi C^je\|\le c^j\Xi_{N,J},\quad
\Xi_{N,J}:=
\frac{L_{K,N,J}+(J+1)L_{I,N,J}}{\sqrt\vartheta}.
\tag{EE20}
\]
The exact monic formula OCP5, or EE16 at \(J=0\), gives \(\vartheta\ge1/2\) eventually. Since \(\min_{0\le s\le1+1/q}\psi(s)>0\) eventually, EE6 and EE18 yield
\[
\epsilon\Xi_{N,k}\le e^{O_{h,\varpi}(k\log(q+2))}.
\tag{EE21}
\]

## 3. Full characteristic feedback and a finite all-time remainder

Write \(R_{\rm root}=k\sqrt{\delta^2+\gamma^2}\) and
\(\rho=8q\max(1,c,R_{\rm root})\). The determinant identity, proved by multiplying \(z-C-\epsilon fe^\dagger\) by \((z-C)^{-1}\), is
\[
1-\epsilon e^\dagger(z-C)^{-1}f
=\frac{Q_k(z)}{\det(z-C)}.
\tag{EE22}
\]
On \(|z|=\rho\), use the logarithms of \(1-\lambda/z\), continuous from infinity, for all \(q\) original roots and all \(q\) eigenvalues of \(C\). Since every ratio has modulus at most \(1/(8q)\),
\[
\left|\log\frac{Q_k(z)}{\det(z-C)}\right|
\le2q\frac{1/(8q)}{1-1/(8q)}\le2/7.
\]
The resolvent identity then gives
\[
\|(z-M)^{-1}-(z-C)^{-1}\|
\le
\frac{\epsilon e^{2/7}}{\rho^2(1-1/(8q))^2}
<\frac{2\epsilon}{\rho^2}.
\tag{EE23}
\]
No diagonalization of \(M\) occurs; its full characteristic polynomial includes all multiplicities.

On the same circle, \(|1-Q_k/\det(z-C)|\le e^{2/7}-1<1\). Its Laurent coefficients give
\[
g_j=\epsilon e^\dagger C^jf,\quad g_0=0,\quad |g_j|\le\rho^{j+1}.
\tag{EE24}
\]
Cauchy's integral formula applied to EE23 gives
\(\|M^n-C^n\|\le2\epsilon\rho^{n-1}\).
For real \(t\), \(e^{itC}\) is unitary and
\(\|e^{itC}-I\|\le c|t|\). Remove the exact \(n=1\) term \(itR\) before summing:
\[
\boxed{\|e^{itM}-I-itR\|
\le F(|t|):=c|t|+\frac{2\epsilon}{\rho}
(e^{\rho|t|}-1-\rho|t|).}
\tag{EE25}
\]
This finite inequality holds at every real time. Its small relative error is used only on the explicit clock below.

## 4. Actual compressed spectrum and intrinsic evolution

Put \(D_B=J^\dagger MJ=C_B+\epsilon vu^*\). For \(0\le j\le k\), the same telescoping as EE20, now in \(E\), gives
\[
\|(PCP)^jPe-C^je\|\le(j+1)c^j\Xi_{N,k}.
\]
Taking its inner product with \(f\) and using selfadjointness of \(C_B\) proves
\[
|\epsilon u^*C_B^jv-g_j|
\le\epsilon(j+1)c^j\Xi_{N,k}.
\tag{EE26}
\]
Thus the growing-jet estimate is transported through the original observation, rather than assigning the full characteristic polynomial to \(D_B\).

Let
\[
H_*=\rho+c+(k+1)\epsilon\Xi_{N,k},\quad
r_B=\max\{2c,\;4(k+2)H_*,\;(8\epsilon_Bc^{k+1})^{1/(k+2)}\}.
\tag{EE27}
\]
The first \(k+1\) terms of \(\epsilon u^*(z-C_B)^{-1}v\) have modulus sum at most
\(\sum_{j=0}^k(H_*/|z|)^{j+1}<1/4\)
when \(|z|\ge r_B\). For \(j\ge1\), EE24 and EE26 are bounded by \(H_*^{j+1}\); the same bound for \(j=0\) follows from \(g_0=0\). The complete tail is at most
\[
\frac{\epsilon_Bc^{k+1}}{|z|^{k+2}(1-c/|z|)}
\le\frac{2\epsilon_Bc^{k+1}}{|z|^{k+2}}\le1/4.
\]
The determinant lemma for \(D_B\) therefore excludes every eigenvalue with \(|z|\ge r_B\). Moreover
\[
\log(1+r_B)=O_{h,\varpi}(k\log(q+2)).
\tag{EE28}
\]
For its third term, \(\log\epsilon_B/(k+2)=O(k)\) by EE6; all other terms use EE8 and EE21.

Take \(n_B=\dim B\) and \(\rho_B=8n_B\max(1,c,r_B)\). Repeating the complete proof of EE23–25 for the actual characteristic polynomial of \(D_B\) gives
\[
\boxed{\|e^{itD_B}-I-itR_B\|
\le F_B(|t|):=c|t|+\frac{2\epsilon_B}{\rho_B}
(e^{\rho_B|t|}-1-\rho_B|t|).}
\tag{EE29}
\]
Here \(R_B^2=(\epsilon r)R_B\); the proof does not assume that the observed rank-one map is square-zero.

## 5. Hidden evolution and the measured inverse

For \(0\le J\le k\), expand \(e^\dagger e^{itC}\Pi\) through order \(J\), use EE20 on the initial terms, and use \(\|C\|\le c\) on the tail. For \(|t|\le T\),
\[
\|e^\dagger e^{itC}\Pi\|
\le E_K(T,J):=e^{cT}
\left[\Xi_{N,J}+\frac{(cT)^{J+1}}{(J+1)!}\right].
\tag{EE30}
\]
The full scalar Duhamel equation for
\(F_K(t)=e^\dagger e^{itM}\Pi\) has free term
\(e^\dagger e^{itC}\Pi\) and convolution kernel
\(i\epsilon e^\dagger e^{itC}f\), with the orientation changed for negative \(t\). By EE24 its absolute integral over length \(T\) is at most
\[
\kappa_F(T)=e^{\rho T}-1-\rho T.
\]
Taking the supremum in the exact equation, whenever \(\kappa_F(T)<1\), gives
\(\sup\|F_K(t)\|\le E_K/(1-\kappa_F)\).
Substitute this in the vector Duhamel equation, using unitarity of \(e^{itC}\), to obtain
\[
\sup_{|t|\le T}\|(e^{itM}-I)\Pi\|
\le d_K(T,J):=cT+
\frac{\epsilon T E_K(T,J)}{1-\kappa_F(T)}.
\tag{EE31}
\]
This is a bound on the complete hidden source, with every feedback return included.

Set
\[
\mathcal L_k=k\log(q+2)\log\log(q+e^e),\qquad
T_k=e^{-\mathcal L_k}.
\tag{EE32}
\]
Because \(\log c,\log\rho=O(k+\log q)\), \(\log\rho_B=O(k\log q)\) and EE21 holds, the finite guards \(\rho_BT_k<1\), \(\kappa_F(T_k)<1/2\), \(d_K(T_k,k)<1/2\) all hold eventually. Direct substitution proves
\[
d_K(T_k,k)\le e^{-\mathcal L_k+O_{h,\varpi}(k\log(q+2))}.
\tag{EE33}
\]
For the Taylor tail, its logarithm is at most
\[
q\psi(0)-(k+2)\mathcal L_k+O_h(k^2+k\log q)-\log((k+1)!),
\]
which is smaller than \(-\mathcal L_k-Ck\log q\) for every fixed \(C\) eventually. This calculation is why the growing order is required.

Let \(U(t)=J^\dagger e^{itM}J\). Decompose \(e^{-itM}\) on the exact orthogonal sum \(PE\oplus\Pi E\):
\[
e^{-itM}=\begin{pmatrix}A_-&B_-\\C_-&D_-\end{pmatrix}.
\]
EE31 gives \(\|D_--I\|,\|B_-\|\le d_K(T,k)\), and EE25 gives
\(\|C_-\|\le T\epsilon+F(T)\).
If \(d_K<1\), block elimination gives a factorization with invertible lower block \(D_-\). Since the whole exponential is invertible, its Schur complement is invertible; the upper block of its inverse is \(U(t)\). Therefore
\[
\boxed{U(t)^{-1}=U(-t)-B_-D_-^{-1}C_-,}
\]
\[
\boxed{\|U(t)^{-1}-U(-t)\|
\le\frac{d_K(T,k)}{1-d_K(T,k)}
[T\epsilon+F(T)],\quad |t|\le T.}
\tag{EE34}
\]
This is the actual measured inverse. The second term generally does not vanish.

For a uniform relative norm estimate on \(0<|t|\le T_k\), use EE34 with \(T=|t|\), not with \(T_k\) in its numerator. All finite bounds are nondecreasing in \(T\) while their denominators remain positive. This keeps its factor \(|t|\epsilon\) before comparison with the shear; replacing it prematurely by \(T_k\epsilon\) would not prove uniformity near zero.

Jacobi's complementary determinant identity follows here from the same block factorization:
\[
\det U(t)=\det(e^{itM})\det D_-=\det D_-,
\]
since \(\operatorname{tr}M\) is the sum of all original roots and is zero. The logarithm of \(D_-=I+E\) has its convergent power series when \(\|E\|<1\). Thus, without choosing an unproved kernel-rank identification,
\[
|\log\det U(t)|
\le(\dim K)[-\log(1-d_K(T,k))]
\le q[-\log(1-d_K(T,k))].
\tag{EE35}
\]
The logarithm is the branch continuous from zero. It tends to zero uniformly on the clock. If the programme's stated \(\dim K=m\) is used, its sharper prefactor is exactly \(m\).

## 6. Uniform shear law and both original endpoint pairs

Put \(z_B=\epsilon r\), \(h_B=|z_B|/\epsilon_B\). By EE5–6,
\[
h_B\le\sqrt{\alpha/\Theta}
\le e^{-q\psi(s_N)+O_{h,\varpi}(k\log(q+2))}.
\]
A rank-one map of norm one and trace \(\zeta\) has matrix
\(\left(\begin{smallmatrix}\zeta&\sqrt{1-|\zeta|^2}\\0&0\end{smallmatrix}\right)\)
in a suitable orthonormal basis: take its image unit vector first and remove the trace component from its input unit vector. Its distance to
\(\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\)
is at most \(2|\zeta|\), because \(1-\sqrt{1-|\zeta|^2}\le|\zeta|\).
The latter shear has norm
\[
S(x)=\frac{\sqrt{x^2+4}+x}{2},\qquad
S(x)\ge1,\quad S(x)\ge x.
\tag{EE36}
\]
Its two singular values follow by solving the quadratic characteristic polynomial of its positive Gram, whose determinant is one.

For \(T=|t|\le T_k\), EE25 divided by \(S(T\epsilon_B)\) costs at most
\[
cT+\frac{\epsilon}{\epsilon_B}\rho T e^{\rho T}.
\]
The shear replacement costs at most \(2h_B\). EE29 costs at most
\(cT+\rho_BT e^{\rho_BT}+2h_B\).
The measured inverse correction EE34, with this same \(T\), costs at most
\[
\frac{d_K(T,k)}{1-d_K(T,k)}
\left[\frac{\epsilon}{\epsilon_B}+cT+
\frac{\epsilon}{\epsilon_B}\rho T e^{\rho T}\right].
\]
Here \(\epsilon/\epsilon_B\le\Theta^{-1/2}\) is retained. Each expression is at most
\(\eta_k=\exp[-\mathcal L_k+O_{h,\varpi}(k\log(q+2))]\);
the \(h_B\) term is even smaller since \(\mathcal L_k=o(q)\) and \(\psi(1)>0\).
Consequently, simultaneously for both time signs and all four cutoffs,
\[
\boxed{\begin{aligned}
\|U(t)\|&=S(|t|\epsilon_B)(1+O(\eta_k)),\\
\|U(t)^{-1}\|&=S(|t|\epsilon_B)(1+O(\eta_k)),\\
\|e^{itD_B}\|&=S(|t|\epsilon_B)(1+O(\eta_k)),\\
\|e^{-itD_B}\|&=S(|t|\epsilon_B)(1+O(\eta_k)).
\end{aligned}}
\tag{EE37}
\]
This proves measured invertibility on the entire interval and its least singular value, in the original metric.

For \(x>0\), \(0\le\log S(x)-(\log x)_+\le\log2\). Together with EE6 and EE5, EE37 proves
\[
\log s_{\max}U(t)=(\log|t|+q\psi(s_N))_++O(k\log q),
\]
\[
\log s_{\min}U(t)=-(\log|t|+q\psi(s_N))_++O(k\log q).
\tag{EE38}
\]
Both statements also hold for \(e^{itD_B}\). Put \(a_0=\psi(0)\), \(a_1=\psi(1)\). The endpoint expansions in RC8–10 give
\(q\psi(1/q)=qa_0+O(\log q)\) and
\(q\psi(1+1/q)=qa_1+O(1)\).
The positive-part map is 1-Lipschitz. Thus for every \(b>0\), with \(e^{-bq}\le T_k\) eventually,
\[
\mathcal R\log s_{\max}U(e^{-bq})
=2q[(a_0-b)_+-(a_1-b)_+]+O_{h,\varpi}(k\log q),
\]
\[
\mathcal R\log s_{\min}U(e^{-bq})
=-2q[(a_0-b)_+-(a_1-b)_+]+O_{h,\varpi}(k\log q),
\]
\[
\boxed{\mathcal R\log\operatorname{cond}U(e^{-bq})
=4q[(a_0-b)_+-(a_1-b)_+]+O_{h,\varpi}(k\log q).}
\tag{EE39}
\]
All four terms are present. The intrinsic operator has the same formulas. In particular the lower plateau \(0<b<a_1\), and also the moving time \(T_k\), give \(4(a_0-a_1)q+O(k\log q)\). The central scalar \(e^{kt/2}\) of the physical action changes no condition number; for four-cutoff norms it cancels because the four signs sum to zero.

## 7. Growing exterior ranks and the actual terminal class

Let \(r_k=\lceil2q/\mathcal L_k\rceil=o(k)\). The exact identity
\[
M^n-C^n=\sum_{j=0}^{n-1}M^{n-1-j}RC^j
\]
shows that \(\sum_{n=1}^{r_k}(it)^n(M^n-C^n)/n!\) has range contained in
\(\operatorname{span}\{f,Mf,\ldots,M^{r_k-1}f\}\), and hence rank at most \(r_k\). EE23 bounds its remaining exponential tail by
\[
\frac{2\epsilon}{\rho}e^{\rho T_k}
\frac{(\rho T_k)^{r_k+1}}{(r_k+1)!}\le e^{-q}
\tag{EE40}
\]
eventually. Indeed its logarithm is at most
\(a_0q-2q+O(q/\log\log q)+o(q)<-q\), since \(a_0<1\).
The same argument uses \(\rho_B\) and \(\epsilon_B\) for \(D_B\).
The unperturbed observed exponential differs from \(I_B\) by at most \(cT_k\).
Intersecting the kernel of the rank-\(r_k\) perturbation with the variational subspaces for decreasing singular values gives
\[
1-\delta_k\le s_j(U(t))\le1+\delta_k
\quad(r_k<j\le n_B-r_k),\quad
\delta_k=cT_k+e^{-q}.
\tag{EE41}
\]
The upper bound follows from the codimension-\(r_k\) kernel; applying the same variational intersection for the lower bound loses \(r_k\) dimensions at the other end. If the displayed interval is empty the assertion is empty; on the actual rank bound it is nonempty eventually.
At most \(2r_k\) singular values are outside this band. EE38 bounds the absolute logarithm of every one by \(O(q)\). Summing the first \(p\) decreasing logarithms therefore proves, uniformly for every exterior degree \(1\le p\le n_B\),
\[
\boxed{
\sup_{N,\,0<|t|\le T_k,\,1\le p\le n_B}
\frac{|\log\|\wedge^pU(t)\||}{kq}
=O_{h,\varpi}\!\left(\frac1{\log q\,\log\log q}\right)\longrightarrow0.
}
\tag{EE42}
\]
The same holds intrinsically. This conclusion concerns the first-order multiplication evolution; the positive-energy word determinants retain their separate original maps and previously evaluated coefficients.

For the original terminal eigenclass \(Mx=\omega x\), \(\omega=k\gamma-ik\delta\), let \(y=J^\dagger x\) and \(\theta=\|y\|^2/\|x\|^2\). On the exact [RC35–44 terminal domain](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L315), \(-\log\theta=O_{h,\varpi}(k\log q)\). The full identity
\[
U(t)y-e^{it\omega}y=-J^\dagger(e^{itM}-I)\Pi x
\]
gives
\[
\frac{\|U(t)y-e^{it\omega}y\|}{\|y\|}
\le d_K(T_k,k)\sqrt{\frac{1-\theta}{\theta}}
\le e^{-\mathcal L_k+O_{h,\varpi}(k\log q)}.
\tag{EE43}
\]

For completeness the intrinsic return has a separate proof. Put \(A_j=e^\dagger C^jx\), \(D_0=|\omega|+c\). The eigenclass equation gives
\(\epsilon|A_0|\le D_0\|x\|\), and
\(A_{j+1}=\omega A_j-g_jA_0\).
Induction using \(|\omega|\le\rho\) and EE24 yields
\[
\epsilon|A_j|\le D_0(j+1)\rho^j\|x\|.
\tag{EE44}
\]
EE26's vector comparison, paired now with \(x\), implies
\[
|\epsilon u^*C_B^jy-\epsilon A_j|
\le\epsilon(j+1)c^j\Xi_{N,k}\|x\|\quad(j\le k).
\]
Hence the free forcing satisfies, for \(|t|\le T\),
\[
|\epsilon u^*e^{itC_B}y|
\le B(T)\|x\|,
\]
\[
B(T)=D_0(1+\rho T)e^{\rho T}
+\epsilon\Xi_{N,k}(1+cT)e^{cT}
+\epsilon e^{cT}\frac{(cT)^{k+1}}{(k+1)!}.
\]
The exact scalar intrinsic Duhamel kernel has integral bound
\[
\kappa_B(T)\le\kappa_F(T)
+\epsilon\Xi_{N,k}Te^{cT}
+\epsilon_BTe^{cT}\frac{(cT)^{k+1}}{(k+2)!}.
\tag{EE45}
\]
For the middle term integrate the finite series:
\(\int_0^T\sum_{j\ge0}(j+1)(cs)^j/j!\,ds=Te^{cT}\).
For the tail integrate the full factorial series. Thus no missing growing factor is hidden in EE45.
At \(T=T_k\), \(\kappa_B=o(1)\) and \(B(T_k)\le e^{O(k\log q)}\).
The scalar equation bounds its solution by \(B\|x\|/(1-\kappa_B)\).
Its vector equation then gives
\[
\|e^{itD_B}y-y\|
\le cT\|y\|+\frac{TB(T)}{1-\kappa_B(T)}\|x\|.
\]
Finally \(|e^{it\omega}-1|\le T|\omega|e^{T|\omega|}\), so
\[
\boxed{
\sup_{|t|\le T_k}
\frac{\|e^{itD_B}y-e^{it\omega}y\|}{\|y\|}
\le e^{-\mathcal L_k+O_{h,\varpi}(k\log q)}.
}
\tag{EE46}
\]
This proves zero exponential transient gain for this same marked vector, while EE38 gives exponentially large maximizing gains. It does not permit differentiating a coarse error bound to assign the terminal current's sign. The actual imaginary interference term of TR20 remains.

## 8. Correct the constant collision and propagate it to RD15

The authoritative original kernel-volume coefficient is
\[
C_\partial=2J(1)=1.354281987825292132\ldots,
\]
as fixed by [025 EP19 and its following paragraph](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/ELLIPTIC_PROFILE_PROOF.md#L178), referring to [024 CK14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md#L148).
The distinct monic allowance difference is
\[
C_{\rm monic}=2[\psi(0)-\psi(1)]
=0.350091046500433050\ldots.
\tag{EE47}
\]
Their exact connecting map is [RC10–12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L93):
\[
J'=2\psi-2(1+t)\psi',\quad
C_\partial=8\int_0^1\psi(t)\,dt-8\psi(1)+4\psi(0).
\]
Thus there is an exact integral relation between them; they are not equal constants.
For independent evaluation use \(F(z)=2K(\sqrt z)/\pi\), \(t=4zF'(z)/F(z)\), \(z=z_t\), and
\[
J(t)=2\log F(z_t)-\tfrac t2\log z_t,
\]
\[
\psi(t)=(1+t)\log\frac4{\pi(1+t)(1-z_t)F(z_t)}
+\tfrac t4\log z_t.
\]
These retain B. C. Carlson's [DLMF19.5](https://dlmf.nist.gov/19.5) and [19.8.12](https://dlmf.nist.gov/19.8.E12) modulus conventions and are derived in the cited EP and RC proofs.

The published [027 RD15](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/40a766ed3a8e0eadd9947f591803255b6eecf184/workbenches/splitzero-tandem/continuations/20260922-terminal-response/RESPONSE_DENOMINATORS.md#L140) used \(C_\partial\) for \(C_{\rm monic}\). Its exact denominator inequalities remain valid. Its corrected four-cutoff consequence is
\[
\boxed{\mathcal R\log\mathfrak A_{\lambda,N}
=4[\psi(0)-\psi(1)]q+O_{h,\varpi}(k\log q)
=0.700182093000866100\ldots\,q+O_{h,\varpi}(k\log q).}
\tag{EE48}
\]
Indeed RD's separate denominator calculation gives
\(\log\mathfrak A_{\lambda,N}=2q\psi(s_N)+O(k\log q)\);
apply the four endpoint estimates used in EE39. The corrected scalar equals the lower propagator plateau, with the exact maps for each quantity supplied above. The kernel coefficient remains \(C_\partial\) throughout.

## 9. Verification and scope

The accompanying checker verifies the determinant lemma, original/full and observed rank-one algebra, exact Taylor coefficients, measured inverse defect, its determinant sign, the jet-fibre comparison on finite positive metrics, feedback-coefficient bounds, the sharp shear singular-value formula and independent scalar profile values. It includes controls that fail if observation is treated as multiplicative, if time reversal is substituted for the measured inverse, or if the two coefficient names are identified.

Finite examples supplement the analytic proofs and are identified as auxiliary matrices. They are not evaluations of an actual off-line zero or period. This derivation uses the complete previously proved source comparisons and uniform monic theorem, with exact locators above. It does not claim a fresh audit of every proof retained in the cumulative source bank. The incoming formulas survive after the explicit repairs EE4, EE8, EE34–35 and EE48; the growing-jet step is fully established by EE9–21.

