# Original-root innovations and constructive determinant extraction

21 September 2026. This derivation retains the complete original invariant rows, all lower-root constraints, the physical coordinate and the four source cutoffs. It gives an explicit connection between the original evaluation-column update and the weighted-polynomial cutoff calculation. Its selected-column approximation has a proved finite remainder. It does not assign the remaining native kernel coefficient or a complex-current sign.

## 1. The unchanged source and two exact representations

Keep the simple-quartet domain, original admitted period, conductor order v, full upper and lower root polynomials, and
\[
q=(k+1)^2,\quad q'=(k-7)^2,\quad c'=k/2-4,
\quad g=q-q'-v,\quad D=N-v,\quad M=D-q'.
\tag{RX1}
\]
Let chi-prime, written $\chi'(S')$, be the monic lower polynomial of degree $q'$. The entire ideal is $I_N=\chi'\mathcal P'_{\le M}$ inside $\mathcal P'_{\le D}$, with the original physical Gamma norm on $S'=c'+iy$:
\[
d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy,
\qquad M_\sigma=\sqrt{2\pi}.
\tag{RX2}
\]
Use its monic polynomials $p_n(y)$ with $p_0=1,p_1=y$,
$p_{n+1}=yp_n-n(n-1/2)p_{n-1}$ and squared norms
$h_n=M_\sigma n!(1/2)_n$. These exact conventions are those of Koornwinder, Wong, Koekoek and Swarttouw, with Reinhardt, [DLMF18.22.8](https://dlmf.nist.gov/18.22.E8) and [18.23.7](https://dlmf.nist.gov/18.23.E7). The source mass remains in $h_n$.

In the orthonormal basis $\phi_n=p_n/\sqrt{h_n}$ let $E_N$ evaluate at every lower root and let $W_N$ consist of the complete original invariant functionals $L_z$ on $\mathcal P'_{\le D}$. The weighted functional is $\ell_z(f)=L_z(\chi'f)$. Its fixed extension annihilates all original nonideal relations $u_L=\mathcal U_A(S^L)$. CL1–6 gives the exact extension and its original low-degree constraint elimination; it is not an independently chosen row family. The full covariance is
\[
P_N=I-E_N^*(E_NE_N^*)^{-1}E_N,
\qquad C_N=W_NP_NW_N^*.
\tag{RX3}
\]
The lower roots are distinct on this domain, and $D\ge q'-1$, so interpolation proves full row rank of $E_N$. The stated original invariant image has rank $r=g-(m-s_k)$ after low elimination, and its restriction to $I_N$ has full row rank. Thus $C_N>0$. If $r=0$, all observation determinants below are one and no pivots are needed.

## 2. A single original evaluation column gives the exact innovation

Append the original column at degree $D+1$:
\[
E_{N+1}=[E_N,e_N],\qquad W_{N+1}=[W_N,w_N],
\quad A_N=E_NE_N^*.
\]
Define
\[
\kappa_N=1+e_N^*A_N^{-1}e_N>0,\qquad
v_N=w_N-W_NE_N^*A_N^{-1}e_N.
\tag{RX4}
\]
The vector
\[
t_N=\kappa_N^{-1/2}
\begin{pmatrix}-E_N^*A_N^{-1}e_N\\1\end{pmatrix}
\tag{RX5}
\]
has norm one, lies in $\ker E_{N+1}$ and is orthogonal to the embedded $\ker E_N$: the old part lies in $\operatorname{im}E_N^*$. The new kernel dimension is one larger, so their orthogonal sum is the whole new ideal. Consequently
\[
P_{N+1}=\begin{pmatrix}P_N&0\\0&0\end{pmatrix}+t_Nt_N^*,
\qquad
\boxed{C_{N+1}=C_N+v_Nv_N^*/\kappa_N.}
\tag{RX6}
\]
Every complex cross term of RX4 remains. This proves the formula without replacing the projection by the identity.

The exact original-root phase and norm can also be evaluated. Let $\eta_{M+1}(S')$ be the monic polynomial orthogonal to all smaller degrees in the complete weight $|\chi'|^2d\sigma$, and let $\nu_{M+1}=\|\chi'\eta_{M+1}\|_\sigma^2$. Its product with $\chi'$ spans the new ideal direction. Its leading coefficient in y is $i^{D+1}$, so its last orthonormal coefficient is $i^{D+1}\sqrt{h_{D+1}}$. Comparing this with RX5, whose last coefficient is $1/\sqrt{\kappa_N}$, gives the exact vector identity
\[
[\chi'\eta_{M+1}]_{\phi}
=i^{D+1}\sqrt{h_{D+1}\kappa_N}\,t_N,
\qquad
\boxed{\nu_{M+1}=h_{D+1}\kappa_N.}
\tag{RX7}
\]
Therefore, for $f_{M+1}=\ell(\eta_{M+1})$,
\[
\boxed{\frac{v_N}{\sqrt{\kappa_N}}
=i^{-(D+1)}\frac{f_{M+1}}{\sqrt{\nu_{M+1}}}.}
\tag{RX8}
\]
The phase is exact; taking the outer product recovers CI7 and CL12. RX7 also supplies a source-pivot computation directly from the full lower-root evaluation Gram. Thus the two innovation presentations describe the same original vector with an explicitly proved coordinate map and mass factor.

## 3. Every source column in both original cutoff intervals

For $i=0,1$ put $l_i=q-1+i$, $u_i=2q-1+i$. Form the r-by-q matrix
\[
V_i=[v_{l_i}/\sqrt{\kappa_{l_i}},\ldots,
v_{u_i-1}/\sqrt{\kappa_{u_i-1}}],
\quad X_i=C_{l_i}^{-1/2}V_i.
\tag{RX9}
\]
Summing RX6 and applying a congruence proves
\[
C_{u_i}=C_{l_i}+V_iV_i^*,\qquad
G_i:=\log\frac{\det C_{u_i}}{\det C_{l_i}}
=\log\det(I_r+X_iX_i^*)\ge0.
\tag{RX10}
\]
Hence, with the original four signs,
\[
\boxed{\mathcal R\log\det C_N=-G_0-G_1.}
\tag{RX11}
\]
There is no adjacent-cutoff approximation. Both entire q-step intervals remain.

Here is the precise source interpretation of $[I_r,X_i]$. Let $R_l:I_l\to\mathbb C^r$ be the full original restriction, so $R_lR_l^*=C_l$. The map
$\Psi_l=R_l^*C_l^{-1/2}$ is an isometry because $\Psi_l^*\Psi_l=I_r$. In target coordinates $C_l^{-1/2}$, its observation is $I_r$. The new orthonormal ideal directions are the embedded RX5 vectors, and their observations are the columns of $X_i$. The old kernel of $R_l$ is an orthogonal source summand with zero observation. Thus $[I_r,X_i]$ is the exact reduced matrix of this original source map; no independent distribution is substituted.

## 4. Constructive selected volumes and a complete error

Put $\mathsf A=[I_r,X_i]$, with r+q columns. For every r-column subset J, write $\mathsf A_J$ for its square matrix. Expanding the Gram determinant by multilinearity and the permutation formula gives the Cauchy–Binet identity
\[
\det(\mathsf A\mathsf A^*)=\sum_{|J|=r}|\det\mathsf A_J|^2.
\tag{RX12}
\]
To see why cross terms disappear, expand each Gram entry as a sum over column indices. Any repeated selected index gives an alternating determinant with equal columns and is zero. Grouping the remaining distinct indices gives the determinant and its complex conjugate. This proves RX12 with all phases inside each minor.

Every selected minor of $[I_r,X_i]$ is, up to sign, a square minor of $X_i$, including the empty minor one. If $\Pi_i$ is the largest logarithm of its squared modulus, then
\[
0\le G_i-\Pi_i\le\log\binom{r+q}{r}.
\tag{RX13}
\]
This maximum is not required by the following algorithm. Select any independent r columns, initially the identity, as a matrix $\mathsf V$. After a column permutation write exactly
\[
\mathsf A\mathsf P=\mathsf V[I_r,\mathsf T].
\tag{RX14}
\]
If all entries of $\mathsf T$ have modulus at most 2, then
\[
\begin{aligned}
G_i&=\log|\det\mathsf V|^2+\log\det(I_r+\mathsf T\mathsf T^*),\\
0&\le\log\det(I_r+\mathsf T\mathsf T^*)\le r\log(1+4q).
\end{aligned}
\tag{RX15}
\]
Indeed its trace is at most4rq, and the arithmetic–geometric mean of the r positive eigenvalues of $I_r+\mathsf T\mathsf T^*$ proves the upper bound. No residual covariance has been declared zero.

If an entry of $\mathsf T$ has modulus greater than 3/2, replace its row-indexed selected column with that unselected column. Multilinearity shows the new determinant equals the old determinant times that entry: all other components duplicate a retained column and vanish. The squared volume increases by more than 9/4. Using enclosures, accept a complete candidate if every upper modulus bound is at most 2; otherwise swap whenever a lower modulus bound is greater than 3/2. Refining enclosures resolves at least one rule, including exact equality with either threshold, since the two thresholds overlap. This assertion presupposes actual converging input enclosures and does not invent a computable native period.

Every selected squared volume is bounded above by RX12. The initial identity volume is one, so the number of swaps is at most
\[
\frac{G_i}{2\log(3/2)}
\le\frac{r\log(U_i/\lambda_i)}{2\log(3/2)}
\tag{RX16}
\]
whenever the retained original bounds give $C_{l_i}\succeq\lambda_iI$ and $C_{u_i}\preceq U_iI$. The last comparison follows by congruence and determinant monotonicity. With the explicit source bounds this is $O_{h,A}(kq\log q)$. This counts swaps, not arithmetic operations or input-bit complexity.

The bounded-interpolation context is classical in Ming Gu and Stanley C. Eisenstat, *Efficient algorithms for computing a strong rank-revealing QR factorization*, SIAM Journal on Scientific Computing 17(4),848–869 (1996), [DOI 10.1137/0917055](https://doi.org/10.1137/0917055). RX12–16 is a complete direct derivation for the original columns; no uninspected theorem from that paper is used.

## 5. The exact original receiver and its phase-bearing inverse

Let $\mathcal A_{k,v}$ be the complete rational Gamma reference of CI24 and let $\mathcal E_k$ be the finite original-source remainder, with the sharper NG2 same-source receiver applied to KF49 and all low-angle/conductor terms retained. Its complete proof is in the accompanying 018 finite determinant source. The actual original kernel return satisfies
\[
|\mathcal K_k-\log\mathcal A_{k,v}+G_0+G_1|\le\mathcal E_k,
\qquad\mathcal E_k=O_{h,A}(q\log(q+2)).
\tag{RX17}
\]
For the two selected matrices $\mathsf V_0,\mathsf V_1$, put
$Z_k^{\rm piv}=\log\mathcal A_{k,v}-\log|\det\mathsf V_0\det\mathsf V_1|^2$. Then
\[
\boxed{Z_k^{\rm piv}-\mathcal E_k-2r\log(1+4q)
\le\mathcal K_k\le Z_k^{\rm piv}+\mathcal E_k.}
\tag{RX18}
\]
The extraction cost is $O(k\log q)$. The selected matrices still depend on the actual original rows; no asymptotic value is assigned to them by this bound.

For current calculations, retain the entire inverse
\[
(\mathsf A\mathsf A^*)^{-1}
=\mathsf V^{-*}(I_r+\mathsf T\mathsf T^*)^{-1}\mathsf V^{-1}.
\tag{RX19}
\]
The middle factor cannot be dropped from a phase calculation. For example, the selected-volume error only bounds its determinant, whereas a given mixed matrix element depends on its directions and complex cross terms. RX19 supplies the exact connecting map.

## 6. Exact executed illustrations and proof scope

The supplied two-column example starts with $E_0=(1,0,0)$ and $W_0$ selecting coordinates2 and3, then appends $(e_1,w_1)=(1,(1,i)^T)$ and $(e_2,w_2)=(i,(2,1)^T)$. RX4–6 gives
\[
v_1/\sqrt{\kappa_1}=(1,i)^T/\sqrt2,
\quad v_2/\sqrt{\kappa_2}=(4-i,3)^T/\sqrt6,
\]
\[
C_2=\begin{pmatrix}13/3&2-i\\2+i&3\end{pmatrix},\qquad\det C_2=8.
\tag{RX20}
\]
Its six squared minors are $1,1/2,1/2,3/2,17/6,5/3$, summing to8; the unprojected covariance has determinant 13. The checker verifies these exactly, all phases and the full projectors. It also tests RX7–8 against the complete weighted-polynomial example CI26, with every relation and both invariant rows. These are declared auxiliary finite examples, not evaluated native zeta or period data.

The executed checker passes 35 exact identities. In the complete CI26 weight it checks all seven successive source degrees5 through11, including the complex phase of both rows in RX8. A separate three-row, five-column complex fixture requires three actual exchanges from the identity selection. Its full Gram determinant is 433197; the selected squared volume is 267497 and the complete residual determinant is 433197/267497. The checker verifies the exact inverse RX19 as well as the determinant and the entry bound. Its receipt retains the actual columns, squared exchange factors and all check labels.

## Complete programme sources

The original maps are [KF1–55](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex) and [CG29–32](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/COMPLETE_CONDUCTOR_GRAPH_METRIC.tex#L224). The exact newer cutoff derivation CI1–26 and CL1–18 and its full finite original-source receiver accompany the018 edition. 


The preceding complete proofs are published at a fixed edition: [FI1–17; FR1–4](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/FINITE_INVARIANT_PROOFS.md), [CI1–26; CL1–18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/CUTOFF_INNOVATION_PROOFS.md), [IC1–42](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/COLLISION_PROOFS.md). All original source versions and human citations are retained in the accompanying source bank.
