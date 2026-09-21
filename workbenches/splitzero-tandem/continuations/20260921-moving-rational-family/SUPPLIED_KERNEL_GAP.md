**The original observation kernel has a spectral gap for the full arithmetic energy that is much larger than the smallest singular scale of the full quotient.** This permits the complete observed memory to be evaluated at the late spectral scales where the preceding general estimates were insufficient.

The new finite bound is

$$
\boxed{
I_K^\dagger M^\dagger M I_K
\ \succeq\
a_N I_K,
\qquad
a_N=\frac{\ell_N}{D_{-,N}^{\,2}}>0,
\qquad
-\log a_N=O_{h,\varpi}\!\bigl(k\log^2(q+2)\bigr)=o(q).
}
\tag{1}
$$

Here \(I_K\) is the inclusion of the **entire original observation kernel**, with its inherited metric. The estimate holds uniformly through the original cutoff window and every source activation \(0\le\alpha\le1\). It is an estimate for \(M\) acting on the kernel, including its leakage into the observation quotient, not for the compressed operator \(M_K\).

This produces an evaluated result in the original complete-memory receiver. At the already specified critical activation and late regularizer,

$$
\alpha_k^\diamond=e^{-2q\log(q/k)-(\beta_{\mathrm L}-a_0)q},
\qquad
z_k^*=e^{-2q\log(q/k)-\beta_*q},
$$

where

$$
a_0=\log(4/\pi),\qquad
\beta_*=-2-I_\square,\qquad
\beta_{\mathrm L}=\beta_*+2a_0,
$$

one obtains

$$
\boxed{
\mathcal R\log
\frac{\det\mathcal F_N(z_k^*)}
     {\det\mathcal F_N(0)}
=
2\log(4/\pi)\,q+o_{h,\varpi}(q).
}
\tag{2}
$$

The corresponding canonical value is \(4\log(4/\pi)q+o(q)\). Thus their difference is

$$
\boxed{-2\log(4/\pi)\,q+o(q),}
\tag{3}
$$

now for the **original observed resolvent with its full memory**, rather than only for the full-space spectral polynomial.

There is also a growing family of original arithmetic words whose kernel-volume distortion is proved to be \(o(kq)\). In particular, the original kernel, its image under \(M\), and its image under \(M^\dagger M\) have the same leading \(kq\) determinant coefficient. No inverse-power sector is removed to obtain this result.

[Complete derivation](sandbox:/mnt/data/Kernel_Gap_Complete_Memory_20260921/COMPLETE_PROOFS.md) · [Additive proof and exact-checking source package](sandbox:/mnt/data/Kernel_Gap_Complete_Memory_20260921.zip)

The finite arguments below use the published HAR/ACT/AK source bounds and the complete-memory definitions at commit `360d3c1d798da434966d35f7e407fc59c14f234b`. Only the final critical-scale limits invoke the retained analytic endpoint asymptotics; those retain their existing proof status. The new gap, word estimates, and memory comparison are proved below.

## 1. The original kernel cannot contain the soft inverse direction

Retain

$$
q=(k+1)^2,\qquad k\equiv1\pmod4,\qquad
0<\delta<\frac12,\qquad\gamma>2,
$$

$$
Q(y)=
\prod_{a,b=0}^{k}
[y-(2b-k)\gamma+i(2a-k)\delta],
$$

$$
E=\mathbb C[y]/(Q),\qquad M[p]=[yp].
$$

The physical coordinate is still \(S=k/2+iy\), and the source is the original \(w_h^{*k}(y)\,dy\).

At cutoff \(N\), write

$$
G=G_N(\alpha),\qquad
G_N(\alpha)^{-1}
=(1-\alpha)G_N^{-1}+\alpha(G_N^J)^{-1}.
$$

Keep the original onto observation \(\Lambda:E\to B\), its full kernel \(K\), and

$$
Q_B=(\Lambda G^{-1}\Lambda^*)^{-1},
\qquad
L=G^{-1}\Lambda^*Q_B,
\qquad
P_B=L\Lambda.
$$

Thus \(L\) is the actual minimum-lift isometry and \(P_B\) is the \(G\)-orthogonal projection onto \(K^{\perp_G}\).

Let

$$
u=[y^{-1}].
$$

The published all-activation harmonic comparison supplies a finite factor

$$
\boxed{
\theta_u:=
\frac{\|P_Bu\|_G^2}{\|u\|_G^2}
\ge\ell_N>0,
\qquad
-\log\ell_N
=O_{h,\varpi}(k\log^2(q+2)).
}
\tag{4}
$$

For example, \(\ell_N=e^{-2E_{1,N}}\) from AK2 is valid. It preserves the actual observation and all its kernel constraints.

The original polynomial division identity gives

$$
M^{-1}=B_{N,0}+u\,\ell_{N,0},
$$

where

$$
B_{N,0}=J_N\mathscr D\widehat R_N,\qquad
\mathscr Dp=\frac{p-p(0)}y,\qquad
\ell_{N,0}(x)=(\widehat R_Nx)(0).
$$

Here \(\widehat R_N\) is the complete canonical minimum section.

The covariance coisometry transports this exact identity to every activation:

$$
\boxed{
M^{-1}=B_{N,\alpha}+u\,\ell_{N,\alpha},
}
\tag{5}
$$

with

$$
\begin{aligned}
B_{N,\alpha}
={}&(1-\alpha)B_{N,0}G_N^{-1}G
+\alpha M^{-1}(G_N^J)^{-1}G,\\
\ell_{N,\alpha}
={}&(1-\alpha)\ell_{N,0}G_N^{-1}G.
\end{aligned}
$$

The rank-one term’s range is the same original line \(\mathbb Cu\).

Choose the explicit finite bound

$$
D_-=
\max\left\{
1,\,
\mathfrak d_N\sqrt{u_k/\ell_{k,N}},
\,
\frac{\sqrt{\mathbf L_k\mathbf B_k}}{\sqrt{\delta^2+\gamma^2}}
\right\}.
$$

The source estimates prove

$$
\|B_{N,\alpha}\|_G\le D_-,
\qquad
\log D_-=O_{h,\varpi}(k\log^2(q+2)).
$$

The first term is the original anchored-division estimate. The second uses the joint-source metric comparison, with all source factors retained.

Now take any \(x\in K\). Since the squared observed fraction of \(u\) is \(\theta_u\),

$$
|\langle u/\|u\|,x\rangle|
\le\sqrt{1-\theta_u}\,\|x\|.
$$

Therefore

$$
\|(I-P_u)x\|\ge\sqrt{\theta_u}\,\|x\|.
$$

Apply (5) to \(Mx\), then project away from the original inverse line:

$$
(I-P_u)x=(I-P_u)B_{N,\alpha}Mx.
$$

Consequently,

$$
\sqrt{\ell_N}\,\|x\|
\le D_-\|Mx\|.
$$

This proves (1).

The conclusion is stronger than invertibility of \(M\). The full quotient has a smallest energy eigenvalue at scale

$$
\exp[-2q\log(q/k)+O(q)].
$$

The entire original kernel has energy bounded below by

$$
\exp[-O(k\log^2q)].
$$

It therefore cannot contain a direction at the full soft scale.

This does not follow for \(M_K=P_KM|_K\) by itself. In the original orthogonal splitting,

$$
M=
\begin{pmatrix}
M_K&D_0\\
C_0&M_B
\end{pmatrix},
$$

the bounded-below energy is

$$
\boxed{
M_K^\dagger M_K+C_0^\dagger C_0.
}
\tag{6}
$$

The \(C_0^\dagger C_0\) term is essential.

## 2. Actual arithmetic words preserve the kernel’s leading determinant

Keep the original coefficient frame \(I_K\), rather than replacing it by a new value frame. Define

$$
K_0=I_K^*GI_K,
$$

$$
K_1=(MI_K)^*G(MI_K),
$$

$$
K_2=((M^\dagger M)I_K)^*G((M^\dagger M)I_K).
\tag{7}
$$

The canonical outgoing decomposition, transported by the same covariance coisometry, gives constants \(D_+,L_+\ge1\) with

$$
s_1(M;G)\le L_+,\qquad
s_j(M;G)\le D_+\quad(j\ge2),
$$

$$
\log L_+=O_{h,\varpi}(q),\qquad
\log D_+=O_{h,\varpi}(k\log^2(q+2)).
$$

One can take

$$
D_+=
\max\{1,C_{\mathrm{pol}}(N),
\sqrt{\mathbf L_k\mathbf B_k}\,k\sqrt{\delta^2+\gamma^2}\},
$$

$$
L_+=\max\{D_+,C_{\mathrm{pol}}(N)+\varepsilon_N\}.
$$

This retains the original canonical allowance \(\varepsilon_N\); it uses only that the remaining outgoing term has rank one.

Let \(m=\dim K=8k-16\), and set

$$
a_N=\ell_N/D_-^2.
$$

The complete exterior-power estimate gives

$$
\boxed{
m\log a_N
\le
\log\frac{\det K_1}{\det K_0}
\le
2\log L_++2(m-1)\log D_+.
}
\tag{8}
$$

For the lower bound, apply (1) to every vector in \(K\). For the upper bound,

$$
\|\wedge^m M\|\le L_+D_+^{m-1}.
$$

This counts every singular direction of \(M|_K\).

Put \(\mathsf H=M^\dagger M\). For a unit \(x\in K\), spectral Jensen gives

$$
\langle x,\mathsf H^2x\rangle
\ge\langle x,\mathsf Hx\rangle^2\ge a_N^2.
$$

The corresponding complete upper bound gives

$$
\boxed{
2m\log a_N
\le
\log\frac{\det K_2}{\det K_0}
\le
4\log L_++4(m-1)\log D_+.
}
\tag{9}
$$

Both logarithmic distortions are

$$
O_{h,\varpi}\!\left(q+k^2\log^2(q+2)\right)=o(kq).
$$

Hence, uniformly in activation,

$$
\boxed{
\mathcal R\log\det K_1
=
\mathcal R\log\det K_0+o(kq),
\qquad
\mathcal R\log\det K_2
=
\mathcal R\log\det K_0+o(kq).
}
\tag{10}
$$

This conclusion concerns the **original kernel before quotienting by an inverse sector**. The preceding IQR estimate first removed an inverse-power sector to obtain a comparable action bound.

### A growing family of powers is controlled

The argument extends beyond the first two words.

Exact polynomial division gives

$$
M^{-s}=B_{s,N,\alpha}+U_sR_{s,N,\alpha},
$$

with

$$
\|B_{s,N,\alpha}\|
\le
D_s:=
\max\left\{
1,\,
\mathfrak d_N^s\sqrt{u_k/\ell_{k,N}},
\,
\sqrt{\mathbf L_k\mathbf B_k}\,
(\delta^2+\gamma^2)^{-s/2}
\right\}.
$$

The harmonic observation estimate on the whole \(V_s=\operatorname{im}U_s\), followed by adjointing its cross projection, gives

$$
\|(I-P_{V_s})x\|\ge e^{-E_{s,N}}\|x\|,
\qquad x\in K.
$$

Projecting the preceding inverse identity proves

$$
\boxed{
\begin{aligned}
-2m(E_{s,N}+\log D_s)
&\le
\log
\frac{\det((M^sI_K)^*G(M^sI_K))}
     {\det K_0}\\
&\le
2s[\log L_++(m-1)\log D_+].
\end{aligned}}
\tag{11}
$$

For the positive words \(\mathsf H^j=(M^\dagger M)^j\), the corresponding estimate is

$$
\boxed{
\begin{aligned}
2mj\log a_N
&\le
\log
\frac{\det((\mathsf H^jI_K)^*G(\mathsf H^jI_K))}
     {\det K_0}\\
&\le
4j[\log L_++(m-1)\log D_+].
\end{aligned}}
\tag{12}
$$

Thus, for the explicit growing range

$$
1\le s,j\le
s_k:=\max\left\{1,
\left\lfloor\frac{k}{\log^3(q+2)}\right\rfloor\right\},
$$

all these logarithmic distortions are \(o(kq)\), uniformly in cutoff and activation.

Every word acts at the original cutoff \(N\). No occurrence of \(M^s\) has been reinterpreted as permission to use a larger unrestricted source cutoff.

There is also an exact quotient-action interpretation. The original map \(M^s\) induces

$$
\overline{M^s}:E/K\longrightarrow E/M^sK.
$$

Both quotients receive their full minimum metrics from the same \(G\). In the target coordinates supplied by \(\Lambda M^{-s}\),

$$
\boxed{
\log\det((\overline{M^s})^\dagger\overline{M^s})
=
2s\log|\det M|
-
\log
\frac{\det((M^sI_K)^*G(M^sI_K))}
     {\det K_0}.
}
\tag{13}
$$

The first term cancels under the original four signs. Therefore this full induced quotient action has zero leading \(kq\) distortion in the stated growing-power range. It is not the power \((\Lambda ML)^s\).

## 3. The complete observed memory has a controlled mass matrix

Use the same original orthogonal splitting \(K\oplus LB\) for the positive energy:

$$
\mathsf H=
\begin{pmatrix}
\mathsf A&\mathsf B\\
\mathsf B^\dagger&\mathsf D
\end{pmatrix}.
$$

The entries are

$$
\mathsf A=M_K^\dagger M_K+C_0^\dagger C_0,
$$

$$
\mathsf B=M_K^\dagger D_0+C_0^\dagger M_B,
\qquad
\mathsf D=D_0^\dagger D_0+M_B^\dagger M_B.
$$

They are exactly the complete-memory blocks already defined in H2–H4.

The new gap proves

$$
\mathsf A\succeq a_NI.
$$

Define

$$
\boxed{
\mathsf S=\mathsf D-\mathsf B^\dagger\mathsf A^{-1}\mathsf B\succ0,
\qquad
\mathsf W=I+\mathsf B^\dagger\mathsf A^{-2}\mathsf B\succeq I.
}
\tag{14}
$$

The first matrix is the complete energy Schur minimum. The second is the **exact first derivative of the original memory pencil at zero**, not a chosen weight.

It has the following exact original-word determinant:

$$
\boxed{
\det\mathsf W
=
\frac{\det K_2\,\det K_0}{(\det K_1)^2}.
}
\tag{15}
$$

Indeed, the kernel block of \(\mathsf H^2\) is

$$
\mathsf A^2+\mathsf B\mathsf B^\dagger.
$$

Sylvester’s determinant identity gives

$$
\det\mathsf W
=
\frac{\det(\mathsf A^2+\mathsf B\mathsf B^\dagger)}
     {(\det\mathsf A)^2},
$$

and restoring the original coefficient frame yields (15).

There is a stronger finite upper bound than estimating every entry separately. Let

$$
\rho_N=\operatorname{rank}\mathsf B.
$$

Since \(\mathsf H\) has at most one eigenvalue above \(D_+^2\), its cross block is one rank-one term plus a remainder of norm at most \(D_+^2\). Therefore

$$
s_1(\mathsf A^{-1}\mathsf B)\le L_+^2/a_N,
$$

and

$$
s_j(\mathsf A^{-1}\mathsf B)\le D_+^2/a_N
\quad(j\ge2).
$$

Consequently,

$$
\boxed{
\begin{aligned}
0\le\log\det\mathsf W
\le{}&
\mathbf1_{\rho_N>0}\log(1+L_+^4/a_N^2)\\
&+(\rho_N-1)_+\log(1+D_+^4/a_N^2)
=:B_{W,N}.
\end{aligned}}
\tag{16}
$$

Here

$$
B_{W,N}=O_{h,\varpi}(q+k^2\log^2q)=o(kq).
$$

Because \(\mathsf W\succeq I\), this is not a cancellation of large positive and negative logarithmic eigenvalues. Every restriction and every attained quotient of this particular mass metric has logarithmic volume cost between zero and \(B_{W,N}\).

The metric and energy maps are explicit:

$$
\mathcal E=L-I_K\mathsf A^{-1}\mathsf B,
$$

where the notation uses the kernel’s inherited metric in forming its adjoint. Then

$$
\Lambda\mathcal E=I,\qquad
\mathcal E^\dagger\mathcal E=\mathsf W,\qquad
\mathcal E^\dagger\mathsf H\mathcal E=\mathsf S.
$$

Thus

$$
\boxed{
\mathcal J=\mathcal E\mathsf W^{-1/2},
\qquad
\mathcal J^\dagger\mathcal J=I,
\qquad
\mathsf H_{\mathrm{eff}}
=
\mathcal J^\dagger\mathsf H\mathcal J
=
\mathsf W^{-1/2}\mathsf S\mathsf W^{-1/2}.
}
\tag{17}
$$

This is an isometric compression through the **full energy-minimum lift**. It is neither \(M_B^\dagger M_B\) nor the unweighted matrix \(\mathsf S\).

Its determinant is exactly

$$
\boxed{
\det\mathsf H_{\mathrm{eff}}
=
|Q(0)|^2\,\frac{\det K_1}{\det K_2}.
}
\tag{18}
$$

The full source metric cancels in \(\det(M^\dagger M)=|\det M|^2\); no restricted Gram is normalized away.

## 4. The low-frequency memory approximation has an exponentially small relative error

The original observed resolvent is

$$
\Lambda(zI+\mathsf H)^{-1}L
=
\mathcal F(z)^{-1},
$$

with

$$
\mathcal F(z)
=
zI+\mathsf D
-\mathsf B^\dagger(\mathsf A+zI)^{-1}\mathsf B.
$$

The published H8–H9 identities already give this complete pencil.

The gap now makes its low-frequency expansion quantitative:

$$
\boxed{
\mathcal F(z)
=
\mathsf S+z\mathsf W
-z^2\mathsf B^\dagger
\mathsf A^{-2}(\mathsf A+zI)^{-1}\mathsf B.
}
\tag{19}
$$

For every real \(z\ge0\),

$$
\boxed{
\frac{\mathsf S+z\mathsf W}{1+z/a_N}
\preceq\mathcal F(z)
\preceq\mathsf S+z\mathsf W.
}
\tag{20}
$$

For the lower bound, use

$$
\frac{\mathsf A}{\mathsf A+zI}
\succeq\frac{a_N}{a_N+z}I
$$

inside the complete \(\mathsf B\)-congruence. No commutation between \(\mathsf B\) and \(\mathsf A\) is required.

The difference in (19) has rank at most \(\rho_N\). Hence

$$
\boxed{
0\le
\log\det(\mathsf S+z\mathsf W)-\log\det\mathcal F(z)
\le
\rho_N\log(1+z/a_N).
}
\tag{21}
$$

There is a full operator version:

$$
\boxed{
\begin{aligned}
(zI+\mathsf H_{\mathrm{eff}})^{-1}
\preceq{}&
\mathsf W^{1/2}
\Lambda(zI+\mathsf H)^{-1}L
\mathsf W^{1/2}\\
\preceq{}&
(1+z/a_N)(zI+\mathsf H_{\mathrm{eff}})^{-1}.
\end{aligned}}
\tag{22}
$$

The earlier general memory estimate involved the potentially enormous scale

$$
m\log(1+\|M\|^2/z).
$$

The new estimate involves

$$
\rho_N\log(1+z/a_N).
$$

It is therefore strongest precisely at the late, small-\(z\) scales previously left outside that estimate. The old estimate and its full leakage terms are retained in the published UFR23 statement.

The entire expansion is controlled. For \(|z|<a_N\),

$$
\begin{aligned}
\mathcal F(z)
={}&\mathsf S+z\mathsf W\\
&+\sum_{j=2}^{p}(-1)^{j+1}z^j
\mathsf B^\dagger\mathsf A^{-(j+1)}\mathsf B
+R_p(z),
\end{aligned}
$$

where

$$
\boxed{
\|\mathsf W^{-1/2}R_p(z)\mathsf W^{-1/2}\|
\le
\frac{|z|^{p+1}}{a_N^p(1-|z|/a_N)}.
}
\tag{23}
$$

These are moments of the original memory:

$$
\int_0^\infty t^j\mathcal M(t)\,dt
=
j!\,\mathsf B^\dagger\mathsf A^{-(j+1)}\mathsf B,
\qquad
\mathcal M(t)=\mathsf B^\dagger e^{-t\mathsf A}\mathsf B.
$$

In particular,

$$
\int_0^\infty t\,\mathcal M(t)\,dt=\mathsf W-I,
$$

and

$$
\int_T^\infty\mathcal M(t)\,dt
\preceq
e^{-a_NT}\,
\mathsf B^\dagger\mathsf A^{-1}\mathsf B.
\tag{24}
$$

Thus the kernel memory has no pole at the full quotient’s ultrasmall energy scale. That scale comes from the complete Schur minimum and its mass, not from an ultrasmall eigenvalue of the kernel block.

## 5. The soft eigenvalue and its observed weight are carried through the memory

Let

$$
\lambda_N=\lambda_{\min}(\mathsf H).
$$

Equation (5) implies

$$
\lambda_2(\mathsf H)\ge D_-^{-2}.
$$

Suppose \(\lambda_N<a_N\), as holds eventually in the critical layer. Write a unit soft eigenvector in the original splitting as

$$
\psi=(x,b)\in K\oplus LB.
$$

The first block equation gives

$$
-\mathsf A^{-1}\mathsf B b
=x-\lambda_N\mathsf A^{-1}x.
$$

Therefore

$$
\boxed{
\begin{aligned}
b^\dagger\mathsf Wb
={}&1-2\lambda_N
\langle x,\mathsf A^{-1}x\rangle
+\lambda_N^2\langle x,\mathsf A^{-2}x\rangle\\
&\in[(1-\lambda_N/a_N)^2,1].
\end{aligned}}
\tag{25}
$$

If \(\theta_N=\|b\|^2\), the mass on the normalized observed soft vector is consequently

$$
\boxed{
\frac1{\theta_N}
\left(1+O(\lambda_N/a_N)\right).
}
\tag{26}
$$

This is the actual observed fraction, not an assigned value one.

The static Schur minimum has

$$
\boxed{
\frac{\lambda_N}{\theta_N+\lambda_ND_-^2}
\le
\lambda_{\min}(\mathsf S)
\le
\frac{\lambda_N}{\theta_N}.
}
\tag{27}
$$

Indeed,

$$
\mathsf S^{-1}
=
\lambda_N^{-1}bb^\dagger+R,
\qquad
0\preceq R\preceq D_-^2I.
$$

After the exact mass is included, the dynamic eigenvalue has the sharper comparison

$$
\boxed{
\lambda_N
\le
\lambda_{\min}(\mathsf H_{\mathrm{eff}})
\le
\frac{\lambda_N}{1-\lambda_N/a_N},
\qquad
\lambda_2(\mathsf H_{\mathrm{eff}})\ge D_-^{-2}.
}
\tag{28}
$$

The lower and second inequalities follow from the isometric compression (17). For the upper one, insert \(b\) into the exact equation

$$
\mathcal F(-\lambda_N)b=0,
$$

and use

$$
\mathsf W
\preceq
I+\mathsf B^\dagger
\mathsf A^{-1}(\mathsf A-\lambda_NI)^{-1}\mathsf B
\preceq
(1-\lambda_N/a_N)^{-1}\mathsf W.
$$

There is now a finite bound for the actual observed heat, with its memory mass retained:

$$
Y_N(\tau)=\Lambda e^{-\tau\mathsf H}L.
$$

Spectral expansion and (25) give

$$
\boxed{
\begin{aligned}
\left|
\operatorname{Tr}(\mathsf W Y_N(\tau))
-e^{-\tau\lambda_N}
\right|
\le{}&
\frac{2\lambda_N}{a_N}e^{-\tau\lambda_N}\\
&+(q-1)\|\mathsf W\|e^{-\tau/D_-^2},
\end{aligned}}
\tag{29}
$$

where

$$
\|\mathsf W\|\le1+(L_+^2/a_N)^2.
$$

The raw observed heat has coefficient \(\theta_N\). The coefficient in (29) is not obtained by dividing by that unknown number: it follows from the explicitly constructed matrix

$$
\mathsf W=\mathcal F'(0).
$$

The effective heat also satisfies

$$
\boxed{
\begin{aligned}
0\le{}&
\operatorname{Tr}e^{-\tau\mathsf H}
-\operatorname{Tr}e^{-\tau\mathsf H_{\mathrm{eff}}}\\
\le{}&
\frac{\lambda_N/a_N}{e(1-\lambda_N/a_N)}
+(q-1)e^{-\tau/D_-^2}.
\end{aligned}}
\tag{30}
$$

The first term is uniform for all positive \(\tau\), using
\(\sup_{x\ge0}xe^{-x}=1/e\).

## 6. Evaluate the complete-memory determinant and heat transition

The current critical-activation proof supplies

$$
-\log\lambda_{N,\mathrm L/\mathrm H}
=
2q\log(q/k)
+\kappa_{\mathrm L/\mathrm H}(\zeta)q+o(q),
$$

where

$$
\kappa_{\mathrm L/\mathrm H}(\zeta)
=\min(\beta_{\mathrm L/\mathrm H},\zeta),
\qquad
\beta_{\mathrm H}=\beta_{\mathrm L}-C_\partial/2.
$$

The identification of the inverse-sector coefficient with \(C_\partial\) is exact in IQR2.

Use the same regularizer at every cutoff:

$$
z_k(b)=e^{-2q\log(q/k)-bq}.
$$

Block determinant elimination gives the exact receiver

$$
\boxed{
\log\frac{\det\mathcal F_N(z)}{\det\mathcal F_N(0)}
=
\log\det(I+z\mathsf H_N^{-1})
-\log\det(I+z\mathsf A_N^{-1}).
}
\tag{31}
$$

The second determinant is bounded by the newly proved gap. The first has only one large inverse singular value. Consequently,

$$
\boxed{
\begin{aligned}
-m\log(1+z/a_N)
\le{}&
\log\frac{\det\mathcal F_N(z)}{\det\mathcal F_N(0)}
-\log(1+z/\lambda_N)\\
\le{}&
(q-1)\log(1+zD_-^2).
\end{aligned}}
\tag{32}
$$

At \(z=z_k(b)\), both errors are

$$
\exp[-2q\log(q/k)+O_{h,\varpi,b}(q)].
$$

Thus, including the thresholds,

$$
\boxed{
\frac1q\mathcal R
\log\frac{\det\mathcal F_N(z_k(b))}
         {\det\mathcal F_N(0)}
\longrightarrow
2\left[
(\kappa_{\mathrm L}(\zeta)-b)_+
-(\kappa_{\mathrm H}(\zeta)-b)_+
\right].
}
\tag{33}
$$

The same limit holds for

$$
\mathcal R\log\det(I+z_k(b)\mathsf H_{\mathrm{eff},N}^{-1}),
$$

with the finite rank-sensitive error (21).

For the late time

$$
\tau_k(b)=z_k(b)^{-1},
$$

the strict interval

$$
\kappa_{\mathrm H}(\zeta)<b<\kappa_{\mathrm L}(\zeta)
$$

gives, from (29)–(30),

$$
\boxed{
\mathcal R\operatorname{Tr}
\left[
\mathsf W_N\Lambda
e^{-\tau_k(b)M^{\dagger_{G_N(\alpha)}}M}
L_N
\right]
\longrightarrow2,
}
\tag{34}
$$

and

$$
\boxed{
\mathcal R\operatorname{Tr}
e^{-\tau_k(b)\mathsf H_{\mathrm{eff},N}}
\longrightarrow2.
}
\tag{35}
$$

Both limits are zero on the other two open regions. No step value is asserted when \(b\) equals a critical endpoint.

The first formula is a mass-weighted measurement of the **full original heat**. The second is the heat of the explicit isometric energy compression (17). Neither is renamed as the raw observed heat or the heat of \(M_B^\dagger M_B\).

For the retained concrete choice

$$
\zeta_\diamond=\beta_{\mathrm L}-a_0,
\qquad
b_*=\beta_{\mathrm L}-2a_0=-2-I_\square,
$$

the published inequality \(C_\partial>4a_0\) gives

$$
\beta_{\mathrm H}<b_*<\zeta_\diamond<\beta_{\mathrm L}.
$$

Therefore (34)–(35) apply at the original \(\tau_k^*\), and (33) becomes precisely (2). At \(\alpha=0\), it is \(4a_0q+o(q)\), proving (3). The finite interval and coefficient identification used here are the retained AK18 calculation.

The mass determinant has not been deleted from an unnormalized expression. Its cancellation in (31) is a same-cutoff ratio, and its separate cost is explicitly bounded by (16). In fact,

$$
\mathcal R\log\det\mathsf S_N=o(kq),
\qquad
\mathcal R\log\det\mathsf W_N=o(kq),
\qquad
\mathcal R\log\det\mathsf H_{\mathrm{eff},N}=o(kq).
\tag{36}
$$

These are leading \(kq\) statements. They do not assign their separate order-\(q\) constants.

## Result reached

The original kernel now has a quantitative positive-energy gap, despite the full quotient’s ultrasmall singular mode. That gap directly controls the complete memory poles and yields a relative low-frequency operator estimate with error \(z/a_N\). Its first memory moment is an exact positive mass matrix whose determinant is an original kernel-word ratio and costs only \(o(kq)\).

The same calculation proves that a growing family of actual arithmetic powers and positive words preserves the kernel’s leading \(kq\) determinant. It then evaluates the original complete-memory spectral determinant through order \(q\), and the memory-weighted original observed heat at the same late time.

The canonical kernel metric \(I_K^*G_NI_K\) still needs its initial \(kq\) coefficient; the comparisons above do not assign it one. The independent proper-source \(Z_R\) minimum and the first-order consecutive complex-current phase remain different quantities. The advance here is that the original kernel’s energy, its arithmetic words, and its complete observed memory can now be controlled without replacing the kernel by an inverse-power subspace or discarding a leakage term.

The accompanying checking script tests the finite identities on complete rational Gaussian-polynomial source metrics with complex observations. Those are auxiliary fixtures, not numerical evaluations of an arithmetic zero packet or period; no new verified execution count or remote publication is asserted.
