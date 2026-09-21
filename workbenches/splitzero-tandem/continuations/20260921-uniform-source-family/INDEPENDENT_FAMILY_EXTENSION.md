# Independent derivation of the source-family and filter receivers

21 September 2026. This derivation checks UFR6, UFR9–12, and UFR14–19 in `ORIGINAL_FAMILY_RECEIVERS.md`. The complete source file was read; its recorded SHA-256 is `CB66F25C1DB1606FBEABB8F804DC75DB2EBBAE73C4CE0F36907221140487C395`. The work below is an independent finite-dimensional derivation. It preserves each original source metric, quotient, physical coordinate, observation, and filter. It does not evaluate an unproved arithmetic positivity guard.

The estimates are correct with one correction to UFR18: its small matrix is positive semidefinite before the guard is checked, and its eigenvalues include zeros when the remainder map has deficient rank. UFR19 itself forces positive definiteness, so its conclusion is unchanged. The rational degree guard is sharp for the stated unreduced-numerator recovery; this does not assert failure of every possible conductor inverse beyond that guard.

## 1. Several logarithmic source weights

Let \(G_\circ>0\) be the original fixed coefficient metric, and let \(\Omega_i\succeq0\) be the complete prescribed source covariances, including all entries of each \(F_iH_i^+F_i^*\). Set

\[
C(\mathbf x)=G_\circ^{-1}+\sum_{i=1}^p e^{x_i}\Omega_i,
\qquad G(\mathbf x)=C(\mathbf x)^{-1}.
\tag{IFE1}
\]

Fix disjoint subspaces \(K,V\), of dimensions \(m,r\), and fixed full frames \(I_K,U\). Define the angle loss using exactly the concatenated frame:

\[
\delta=\log\det(I_K^*GI_K)+\log\det(U^*GU)
-\log\det([I_K,U]^*G[I_K,U]).
\tag{IFE2}
\]

For a segment \(\mathbf x(s)=\mathbf x+s\mathbf v\), \(\mathbf v=\mathbf y-\mathbf x\), define
\(a=\min(0,v_1,\ldots,v_p)\), \(b=\max(0,v_1,\ldots,v_p)\).
The positive operators

\[
K_0=G^{1/2}G_\circ^{-1}G^{1/2},\qquad
K_i=e^{x_i(s)}G^{1/2}\Omega_iG^{1/2}
\]

sum to \(G^{1/2}CG^{1/2}=I\). Thus

\[
D=G^{1/2}C'G^{1/2}=\sum_i v_iK_i,
\qquad aI\preceq D\preceq bI.
\tag{IFE3}
\]

Let \(\widetilde P_X\) be the Euclidean orthogonal projection onto \(G^{1/2}X\), and set
\(A=\widetilde P_K+\widetilde P_V-\widetilde P_{K+V}\).
For any fixed frame \(I_X\), differentiation of \(G=C^{-1}\) gives

\[
\frac{d}{ds}\log\det(I_X^*GI_X)
=-\operatorname{Tr}(D\widetilde P_X),
\quad
\widetilde P_X=G^{1/2}I_X(I_X^*GI_X)^{-1}I_X^*G^{1/2}.
\tag{IFE4}
\]

Therefore \(\delta'=-\operatorname{Tr}(DA)\).

Here is the required spectrum without an assumption of orthogonality between the physical subspaces. Choose orthonormal frames of \(G^{1/2}K\) and \(G^{1/2}V\), and perform a singular-value decomposition of their cross Gram. Their paired unit vectors satisfy \(e_i^*f_j=c_i\delta_{ij}\), with \(0\le c_i<1\); equality \(c_i=1\) would contradict disjointness. In the orthonormal pair
\(e_i,(f_i-c_ie_i)/\sqrt{1-c_i^2}\), the matrix of \(A\) is

\[
\begin{pmatrix}c_i^2&c_i\sqrt{1-c_i^2}\\
c_i\sqrt{1-c_i^2}&-c_i^2\end{pmatrix}.
\tag{IFE5}
\]

Its eigenvalues are \(c_i,-c_i\). All unpaired directions and all directions outside the two-subspace sum give zero. Thus, writing \(A=A_+-A_-\),

\[
\operatorname{Tr}A=0,
\qquad \operatorname{Tr}A_+=\operatorname{Tr}A_-=
\sum_i c_i\le\min(m,r).
\tag{IFE6}
\]

By IFE3, \(0\preceq D-aI\preceq(b-a)I\). Each number
\(\operatorname{Tr}((D-aI)A_\pm)\) lies between zero and
\((b-a)\sum_i c_i\). Their difference therefore has absolute value at most this latter bound. Since \(\operatorname{Tr}A=0\), integration over \(0\le s\le1\) proves

\[
\boxed{|\delta(\mathbf y)-\delta(\mathbf x)|
\le\min(m,r)
\left[\max(0,y_1-x_1,\ldots,y_p-x_p)
-\min(0,y_1-x_1,\ldots,y_p-x_p)\right].}
\tag{IFE7}
\]

This is UFR6. Neither commutation of the \(\Omega_i\) nor a norm or rank estimate for them was used. The fixed source term in IFE1 accounts for the zero included in both extrema. All weights on the segment are positive; zero weights require a separate endpoint argument.

With the original four signs \(+,+,-,-\), the triangle inequality gives UFR7. If each weight ratio belongs to \([q^{-A},q^A]\), each width is at most \(2A\log q\), hence the four-cutoff cost is at most \(8A\min(m,r)\log q\). For \(m=8k-16\), \(q=(k+1)^2\), this is \(o(kq)\). Subtracting the exact Schur identity
\(\log\det\widehat H_K=\log\det H_K-\delta\)
at the two endpoints gives UFR8 with the initial-minus-final cost convention. No initial angle has been set equal to zero.

## 2. The optimal projection fraction

All operators in this section are orthogonal projections for the same original metric \(G_N\). Let \(P_B+P_K=I\), and suppose

\[
\|P_Bu\|^2\ge\ell\|u\|^2\quad(u\in U),
\qquad 0<\ell\le1,
\qquad \|(I-P_U)P_V\|\le\varepsilon\le1.
\tag{IFE8}
\]

The first condition gives \(\|P_KP_U\|\le\sqrt{1-\ell}\). Taking adjoints yields the identical bound for \(P_UP_K\). For a unit \(x\in V\), put \(t=\|(I-P_U)x\|\le\varepsilon\), so
\(x=\sqrt{1-t^2}u+tw\), where \(u\in U\), \(w\perp U\) are unit whenever their coefficients are nonzero. For any unit \(z\in K\), let \(a_z=\|P_Uz\|\le\sqrt{1-\ell}\). Orthogonal decomposition and Cauchy–Schwarz give

\[
|\langle z,x\rangle|
\le a_z\sqrt{1-t^2}+\sqrt{1-a_z^2}\,t.
\tag{IFE9}
\]

If \(\varepsilon<\sqrt\ell\), the right side increases in \(a_z\) for \(0\le a_z\le\sqrt{1-\ell}\): its derivative is nonnegative exactly when \(a_z^2+t^2\le1\), which holds. After setting \(a_z=\sqrt{1-\ell}\), its value increases in \(t\le\sqrt\ell\), by the same derivative calculation. Thus

\[
\|P_Kx\|\le
\sqrt{1-\ell}\sqrt{1-\varepsilon^2}+\sqrt\ell\,\varepsilon.
\]

The identity

\[
1-\left(\sqrt{1-\ell}\sqrt{1-\varepsilon^2}
+\sqrt\ell\,\varepsilon\right)^2
=\left(\sqrt\ell\sqrt{1-\varepsilon^2}
-\sqrt{1-\ell}\,\varepsilon\right)^2
\]

proves the desired bound in this case. If \(\varepsilon\ge\sqrt\ell\), the expression inside the positive part is nonpositive, and the bound is zero. Rescaling \(x\) proves, in every case,

\[
\boxed{\|P_Bx\|^2\ge
\left(\sqrt\ell\sqrt{1-\varepsilon^2}
-\sqrt{1-\ell}\,\varepsilon\right)_+^2\|x\|^2
\quad(x\in V).}
\tag{IFE10}
\]

If \(K=\{0\}\), the estimate follows directly from \(P_B=I\); zero components in the displayed decompositions follow by their limiting values. This also covers \(\ell=1\).

The bound is sharp over all data satisfying IFE8. In an auxiliary Euclidean two-plane set
\(K=\mathbb Ce_1\), \(B=\mathbb Ce_2\), and
\(u=\sqrt{1-\ell}e_1+\sqrt\ell e_2\). If \(0\le\varepsilon<\sqrt\ell\), take

\[
x=\sqrt{1-\varepsilon^2}\,u
+\varepsilon(\sqrt\ell e_1-\sqrt{1-\ell}e_2),
\qquad U=\mathbb Cu,\quad V=\mathbb Cx.
\tag{IFE11}
\]

The two terms are orthogonal, \(x\) is unit, the distance condition is exactly \(\varepsilon\), and its observed coordinate equals the positive expression in IFE10. For \(\varepsilon\ge\sqrt\ell\), choose \(V=K\); its distance from \(U\) is \(\sqrt\ell\le\varepsilon\), and its observed fraction is zero. Thus the transition at \(\varepsilon=\sqrt\ell\) is also optimal. These examples test the inequality; they do not replace the original arithmetic subspaces.

## 3. Exact polynomial division and the complete slow singular space

Let \(E=\mathbb C[y]/(Q_k)\), \(\deg Q_k=q\), with multiplication \(M[f]=[yf]\), and keep the full source polynomial space \(\mathcal P_N\) with its original positive metric. Let \(J_N:\mathcal P_N\to E\) be the original value map, and let \(\widehat R_N:E\to\mathcal P_N\) be its minimum section. In the attained metric \(G_N\), \(\widehat R_N\) is an isometry and \(J_N\) is contractive.

Take a monic polynomial \(p\), \(1\le d=\deg p\le q\), coprime to \(Q_k\), with \(N\ge q-1\). Polynomial division gives
\(f=p\mathfrak Q_pf+\mathfrak R_pf\), where
\(\deg\mathfrak R_pf<d\). If \(N<d\), the quotient map is zero; among the retained endpoints this is exactly \(N=q-1,d=q\). Otherwise it maps to \(\mathcal P_{N-d}\), with its native source metric.

Since \(p(M)\) is invertible, applying the value map and its inverse to the division of \(\widehat R_Nx\) proves

\[
X:=p(M)^{-1}=B_p+F_p,
\quad B_p=J_N\mathfrak Q_p\widehat R_N,
\quad F_p=U_pT_p,
\quad T_p=\mathfrak R_p\widehat R_N,
\quad U_pr=[r/p].
\tag{IFE12}
\]

The last map is injective: if \([r/p]=0\), multiplication by the invertible class \([p]\) gives \([r]=0\), and \(\deg r<d\le q\) forces \(r=0\). Thus \(\dim\operatorname{ran}U_p=d\), while \(\operatorname{rank}F_p\le d\). With
\(D_p=\|\mathfrak Q_p\|\), contractivity and isometry give \(\|B_p\|\le D_p\). No rational function has been assigned a source integral here.

Let \(\sigma_1(X)\ge\cdots\ge\sigma_q(X)>0\), and let \(V_d\) be a top \(d\) left singular space, with any admissible choice inside a tied singular eigenspace. Expanding a vector \(x\in V_d\) in left singular vectors gives its unique preimage \(u=X^{-1}x\), with

\[
\|u\|\le\|x\|/\sigma_d(X),\qquad
\|(I-P_{\operatorname{ran}U_p})x\|
=\|(I-P_{\operatorname{ran}U_p})B_pu\|
\le D_p\|u\|.
\tag{IFE13}
\]

Thus the distance hypothesis of IFE8 holds with
\(\varepsilon_p=\min(1,D_p/\sigma_d(X))\).
On \(\ker F_p\), a subspace of dimension at least \(q-d\), the identity IFE12 gives \(X=B_p\). The singular-value minimum-over-subspaces formula therefore yields

\[
\sigma_{d+1}(X)\le D_p\qquad(d<q).
\tag{IFE14}
\]

For an exact observation bound \(\|P_Bu\|^2\ge\ell_p\|u\|^2\) on \(\operatorname{ran}U_p\), IFE10 proves the UFR16 factor

\[
\ell_{\rm sharp}=
\left(\sqrt{\ell_p}\sqrt{1-\varepsilon_p^2}
-\sqrt{1-\ell_p}\,\varepsilon_p\right)_+^2.
\tag{IFE15}
\]

To verify the heat operator's singular orientation, write an original-metric singular decomposition
\(Xv_j=\sigma_j u_j\). Then
\(p(M)u_j=\sigma_j^{-1}v_j\), so
\(p(M)^\dagger p(M)u_j=\sigma_j^{-2}u_j\).
The top left singular vectors of \(X\), exactly the vectors used in IFE13, are therefore the slow heat eigenvectors. For any orthogonal projection \(P\),

\[
\operatorname{Tr}(Pe^{-\tau p(M)^\dagger p(M)})
=\sum_{j=1}^q e^{-\tau/\sigma_j^2}\|Pu_j\|^2.
\tag{IFE16}
\]

The weights for \(P_B\) on the first \(d\) vectors are at least \(\ell_{\rm sharp}\), and those for \(P_K\) are at most \(1-\ell_{\rm sharp}\). All remaining weights lie in \([0,1]\). Together with IFE14, this proves both UFR17 bounds for every \(\tau\ge0\), with the tail \((q-d)e^{-\tau/D_p^2}\) when \(d<q\). If \(D_p=0\), IFE12 and invertibility of \(X\) imply \(q=\operatorname{rank}F_p\le d\), so \(d=q\) and the tail is omitted. No division by zero is necessary.

## 4. The small matrix and the sufficient positive guard

In the original coefficient coordinates set

\[
H_p=U_p^*G_NU_p>0,\qquad
\mathcal S_p=H_p^{1/2}T_pG_N^{-1}T_p^*H_p^{1/2}\succeq0.
\tag{IFE17}
\]

The map \(U_pH_p^{-1/2}:\mathbb C^d\to(E,G_N)\) is an isometry. Hence the singular values of \(F_p=U_pT_p\) are those of
\(H_p^{1/2}T_p:(E,G_N)\to\mathbb C^d\), with extra zeros in the \(q\)-dimensional presentation if needed. Its product with its metric adjoint is exactly \(\mathcal S_p\). Therefore the \(d\) eigenvalues of \(\mathcal S_p\) are the squares of the first \(d\) singular values of \(F_p\), including zeros. In particular

\[
\sigma_d(F_p)=\sqrt{\mu_d},\qquad
\mu_d=\lambda_{\min}(\mathcal S_p)\ge0.
\tag{IFE18}
\]

The singular-value maximum-over-subspaces formula and \(\|X-F_p\|\le D_p\) give

\[
\sigma_d(X)\ge\sigma_d(F_p)-D_p=\sqrt{\mu_d}-D_p.
\tag{IFE19}
\]

Indeed, on a top \(d\) right singular space of \(F_p\), the triangle inequality gives
\(\|Xz\|\ge\|F_pz\|-D_p\|z\|\ge(\sigma_d(F_p)-D_p)\|z\|\); maximizing over such subspaces gives IFE19. A negative right side is harmless.

If

\[
\boxed{\sqrt{\mu_d}>D_p(1+\ell_p^{-1/2}),}
\tag{IFE20}
\]

then \(\sqrt{\mu_d}-D_p>0\), and

\[
\varepsilon_p\le
\widehat\varepsilon_p:=\frac{D_p}{\sqrt{\mu_d}-D_p}
<\sqrt{\ell_p}.
\tag{IFE21}
\]

The factor in IFE15 is decreasing as a function of \(\varepsilon\) before its zero, so replacing \(\varepsilon_p\) by this larger explicit bound preserves the lower estimate and makes it strictly positive. This proves UFR19 and the resulting heat lower bound. It also proves \(\mu_d>0\), including the case \(D_p=0\).

Positive definiteness before IFE20 cannot be inferred merely from the division identity. An auxiliary exact polynomial example demonstrates the missing inference. Take \(Q(y)=y-1\), \(q=1\), \(N=1\), and a probability source of mean zero and second moment one. Its metric on \(a+by\) is \(|a|^2+|b|^2\). The attained metric at the value \(f(1)\) is \(G_N=1/2\), with minimum section \(\widehat R_Nx=x(1+y)/2\). For \(p(y)=y+1\), coprime to \(Q\), division of every minimum lift has zero remainder. Thus \(T_p=0\) and \(\mathcal S_p=0\), while \(X=p(M)^{-1}=1/2\) remains invertible. This is a test of the general finite reasoning, not a replacement of the programme polynomial. The correction is to retain zero eigenvalues until the actual guard is checked.

## 5. Exact rational recovery and its degree guard

Keep the physical coordinate \(S\), the complete upper relation \(\chi\) of degree \(q\), the complete lower relation \(\widehat\chi\) of degree \(q'\), and shifts satisfying
\(\widehat\chi(S)\mid\chi(S+b_j)\). Set

\[
\mathcal T_Af(S)=\sum_{j=1}^J a_jf(S+b_j),\qquad
E_A(z)=\sum_ja_je^{b_jz},\qquad
v=\operatorname{ord}_0E_A<\infty,
\quad \mu_h=\sum_ja_jb_j^h.
\tag{IFE22}
\]

Thus \(\mu_h=0\) for \(h<v\), and \(\mu_v\ne0\). Let \(D\) be monic of degree \(1\le d\le q\), coprime to \(\chi\); set
\(L=Jd\), \(\mathcal B=\prod_jD(S+b_j)\), and \(U_Dp=[p/D]\) for \(\deg p<d\).

For a nonzero such numerator, write \(n_0=d-\deg p\ge1\) and
\(p/D=cS^{-n_0}+O(S^{-n_0-1})\), \(c\ne0\). Expanding each translated Laurent monomial at infinity shows that the first surviving coefficient of its sum is

\[
\mathcal T_A(p/D)
=(-1)^v\binom{n_0+v-1}{v}\mu_vc\,S^{-n_0-v}
+O(S^{-n_0-v-1}).
\tag{IFE23}
\]

All earlier coefficients vanish because their moments have index below \(v\). Contributions from later Laurent monomials to the coefficient displayed in IFE23 also have lower moment index and vanish. Its coefficient is nonzero. This proves injectivity of \(\mathcal T_A\) on nonzero proper rational functions.

The complete numerator
\(N_p=\mathcal B\mathcal T_A(p/D)\) is a polynomial. Since \(\mathcal B\) is monic of degree \(L\), IFE23 proves the exact degree formula

\[
\deg N_p=L-n_0-v\le L-v-1.
\tag{IFE24}
\]

In particular the upper bound is attained for \(p=S^{d-1}\). A negative value on the right for a nonzero numerator would contradict IFE23 and polynomiality, so no inconsistent negative-degree case is introduced.

A Bézout identity \(DP+\chi R=1\), shifted by \(b_j\) and reduced modulo \(\widehat\chi\), proves that every \(D(S+b_j)\) is a unit of the complete lower quotient. Therefore \(\mathcal B\) is a unit there, including all multiple-root jets. The same shifted identity proves the exact relation

\[
M_{\mathcal B}^{(-)}C_AU_Dp=[N_p]_{\widehat\chi}.
\tag{IFE25}
\]

This establishes the rational action from the original polynomial conductor, without evaluating only selected roots.

Let \(T_D\) be the \(L\)-by-\(d\) coefficient matrix of the numerators \(N_{S^\ell}\), \(0\le\ell<d\). Injectivity in IFE23 gives full column rank, so \(T_D^*T_D>0\). If

\[
Jd-v=L-v\le q',
\tag{IFE26}
\]

then every \(N_p\) has degree below \(q'\) by IFE24 and is already its unique lower remainder. Taking its first \(L\) coefficient rows, with zero padding or truncation of the lower-remainder coordinate space as required, returns exactly \(T_Dp\). Hence

\[
W_D=(T_D^*T_D)^{-1}T_D^*
\operatorname{coef}_{<L}M_{\mathcal B}^{(-)},
\qquad \boxed{W_DC_AU_D=I_d.}
\tag{IFE27}
\]

This proves UFR10 even if \(q'<L\). The last \(v\) numerator rows vanish exactly. The condition IFE26 is sharp for all these numerators being unreduced remainders, because IFE24 attains degree \(L-v-1\). Beyond IFE26 a conductor may still be injective for other reasons, but that conclusion does not follow from this unreduced-numerator argument.

For completeness, retain the original observation \(\Lambda\), with \(\ker\Lambda\subseteq\ker C_A\), the positive metric \(G\), and
\(Q=(\Lambda G^{-1}\Lambda^*)^{-1}\),
\(\Gamma_A=C_AG^{-1}C_A^*\), \(H_D=U_D^*GU_D>0\).
The containment of kernels gives a unique map on the observation image with \(C_A=R_A\Lambda\). Every lift of an observed value is therefore a lift of its conductor value. The minimum source norm on the latter fibre is
\(z^*\Gamma_A^+z\) for \(z\in\operatorname{ran}C_A\), as follows by the minimum lift \(G^{-1}C_A^*\Gamma_A^+z\) and orthogonality to \(\ker C_A\). Consequently

\[
U_D^*\Lambda^*Q\Lambda U_D
\succeq(C_AU_D)^*\Gamma_A^+(C_AU_D).
\tag{IFE28}
\]

IFE27 gives \(\|C_AU_Da\|\ge\|a\|/\|W_D\|\). On its positive range, \(\Gamma_A^+\succeq\lambda_{\max}(\Gamma_A)^{-1}I\), while \(H_D\preceq\lambda_{\max}(H_D)I\). Combining these inequalities proves the UFR12 factor

\[
U_D^*\Lambda^*Q\Lambda U_D\succeq\ell_DH_D,
\qquad
\ell_D=\frac1{\lambda_{\max}(\Gamma_A)\|W_D\|^2\lambda_{\max}(H_D)}>0.
\tag{IFE29}
\]

Injectivity in IFE27 ensures a nonzero conductor image, so the denominator is positive. The observed minimum is at most the original norm, which forces \(\ell_D\le1\). Thus the exact original-metric factor required in IFE8 is available on the stated conductor guard, with all maps and source terms retained.

The application to the monic \(y\)-filter in IFE12 has the following exact physical-coordinate map. Retain \(S=s_0+iy\), \(s_0=k/2\), and put

\[
D(S)=i^d p((S-s_0)/i),\qquad
(Tr)(S)=i^d r((S-s_0)/i).
\tag{IFE30}
\]

The polynomial \(D\) is monic of degree \(d\), and \(T\) is invertible on the degree-below-\(d\) numerator space. Under the exact algebra identification between the original \(y\) and physical-\(S\) quotients,
\(\Phi([f(y)])=[f((S-s_0)/i)]\),

\[
\Phi\bigl(U_pr\bigr)=U_D(Tr),
\qquad
\frac{i^d r((S-s_0)/i)}{i^d p((S-s_0)/i)}
=\frac{r((S-s_0)/i)}{p((S-s_0)/i)}.
\tag{IFE31}
\]

The complete relations correspond under the same substitution; their nonzero leading factors do not change their ideals. Transporting the original metric through this exact coordinate identification gives \(H_p=T^*H_DT\), and the observed Gram transforms by the same congruence. Therefore IFE29 gives \(\|P_Bu\|^2\ge\ell_D\|u\|^2\) on \(\operatorname{ran}U_p\), with the exact scalar \(\ell_p=\ell_D\). No physical-coordinate scale or numerator coefficient has been dropped.

The independent conclusions are UFR6, the sharp UFR14, UFR15–17, the corrected semidefinite form of UFR18, the sufficient positive guard UFR19, and the full unreduced-numerator guard in UFR9–12. None requires replacing the original filter by a compressed observation action.
