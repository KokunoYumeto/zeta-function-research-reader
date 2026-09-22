# Canonical polynomial, rational, and complete real-divisor currents

22 September 2026. Independent derivation of incoming WS1–WS24, including WS21a–e. The input is `Whole_Space_Signs_20260922/COMPLETE_PROOFS.md`. The proof below establishes the asserted signatures without relying on the input's finite-check count. No mathematical defect in those signatures was found. The maximal-isotropic extension argument and the large-degree divisor congruence are supplied explicitly.

## 1. The unchanged quotient and its attained metric

Let \(\mu\) be the original positive measure on \(\mathbb R\), with all moments used below finite and with positive definite polynomial Gram matrices. Let \(Q\in\mathbb R[y]\) be monic of degree \(q\), and suppose \(Q>0\) almost everywhere for \(\mu\). Set \(\mathcal P_j=\{0\}\) for \(j<0\), and otherwise let \(\mathcal P_j\) be the complex polynomials of degree at most \(j\). Every source inner product is conjugate-linear in its first argument:
\[
 \langle f,g\rangle_\mu=\int\overline{f(y)}g(y)\,d\mu(y).
 \tag{WD1}
\]
For \(N\ge q-1\), let \(J_N:\mathcal P_N\to E=\mathbb C[y]/(Q)\) be the remainder map. Its kernel is exactly \(Q\mathcal P_{N-q}\). Define \(H_N=(Q\mathcal P_{N-q})^\perp\subset\mathcal P_N\). The restriction \(J_N|_{H_N}\) is bijective: it is injective because a vector lying in a subspace and its orthogonal complement has zero norm, and it is onto by subtracting the orthogonal projection onto the kernel from any representative. Define
\[
 R_N=(J_N|_{H_N})^{-1},\qquad
 \langle x,z\rangle_{G_N}=\langle R_Nx,R_Nz\rangle_\mu.
 \tag{WD2}
\]
Every other representative is \(R_Nx+v\), \(v\in\ker J_N\), and has squared norm \(\|R_Nx\|_\mu^2+\|v\|_\mu^2\). This proves that WD2 is the complete attained quotient minimum. Moreover,
\[
 J_NR_N=I_E,\quad R_NJ_N=P_{H_N},\quad
 J_N^\dagger=R_N,\quad R_N^\dagger R_N=I_E.
 \tag{WD3}
\]
Indeed \(\langle J_Nf,x\rangle_{G_N}=\langle P_{H_N}f,R_Nx\rangle_\mu=\langle f,R_Nx\rangle_\mu\). In the following formulas \(G=G_N\), and an adjoint always uses this metric on \(E\) and the stated source metric or ordinary Euclidean metric on the other space.

In coefficient coordinates let \(\mathsf H_N\) be the full positive source moment matrix and write \(J_N\) also for the matrix of the remainder map. Then the complete formulas are
\[
 G_N=(J_N\mathsf H_N^{-1}J_N^*)^{-1},\qquad
 R_N=\mathsf H_N^{-1}J_N^*G_N.
 \tag{WD3a}
\]
The covariance is positive definite because \(J_N^*\) is injective and \(\mathsf H_N^{-1}>0\). These displayed matrices satisfy \(J_NR_N=I\), and for \(v\in\ker J_N\),
\(v^*\mathsf H_NR_Nx=(J_Nv)^*G_Nx=0\).
They therefore give precisely the inverse restriction in WD2. Multiplication also gives \(R_N^*\mathsf H_NR_N=G_N\), verifying the full metric formula directly.

Let \(M:E\to E\) be \(M[f]=[yf]\). For any polynomial or defined rational operator \(T\), put
\[
 W_T=i(T-T^{\dagger_G}),\qquad
 \mathfrak W_T=GW_T=i(GT-T^*G).
 \tag{WD4}
\]
The Hermitian operator \(G^{1/2}W_TG^{-1/2}\) and the Hermitian form matrix \(\mathfrak W_T\) have the same inertia, because one is the congruence of the other by \(G^{-1/2}\). Thus operator and form signatures refer to the same positive, negative, and zero counts.

These statements retain the source mass. Let \(p_j\) be the unique real monic polynomial orthogonal to \(\mathcal P_{j-1}\), let \(\omega_j=\int|p_j|^2\,d\mu>0\), and put \(\phi_j=p_j/\sqrt{\omega_j}\). They exist by orthogonal projection of \(y^j\) onto \(\mathcal P_{j-1}\); reality follows from the real moment matrix. In particular \(\omega_0=\mu(\mathbb R)\). No rescaling of \(\mu\) has been made.

## 2. The complete polynomial boundary factor

Let \(p(y)=\sum_{j=0}^da_jy^j\in\mathbb R[y]\), with \(a_d\ne0\) and \(1\le d\le q/2\). Define actual quotient-column maps from \(\mathbb C^d\) to \(E\) by
\[
 I_d=[J_N\phi_{N-d+1},\ldots,J_N\phi_N],\qquad
 O_d=[\,[\phi_{N+1}],\ldots,[\phi_{N+d}]\,].
 \tag{WD5}
\]
The outgoing polynomial may have degree greater than \(N\), but its class is measured by exactly \(G_N\); its representative is \(R_N[\phi_j]\). Define
\[
 B_p[r,s]=\langle\phi_{N+r},p\phi_{N-d+s}\rangle_\mu,
 \qquad 1\le r,s\le d.
 \tag{WD6}
\]
For \(r>s\), the second polynomial has degree at most \(N+s<N+r\), so \(B_p[r,s]=0\). When \(r=s\), subtracting
\(a_d\sqrt{\omega_{N+s}/\omega_{N-d+s}}\phi_{N+s}\)
from \(p\phi_{N-d+s}\) removes its leading coefficient. Its remaining degree is less than \(N+s\), proving
\[
 B_p[s,s]=a_d\sqrt{\frac{\omega_{N+s}}{\omega_{N-d+s}}}\ne0.
 \tag{WD7}
\]
Thus \(B_p\) is invertible, with its full source-norm ratios.

For \(x\in E\), expand \(R_Nx\) in the orthonormal source basis. Its last \(d\) coefficients are \(I_d^\dagger x\), because WD3 gives
\(\langle J_N\phi_j,x\rangle_G=\langle\phi_j,R_Nx\rangle_\mu\).
Multiplication by \(p\) sends every lower coefficient into \(\mathcal P_N\). The outgoing coefficients of \(pR_Nx\) are consequently exactly \(B_pI_d^\dagger x\). The part in \(\mathcal P_N\), followed by the remainder map, is
\[
 C_p=R_N^\dagger P_{\mathcal P_N}p(y)R_N.
\]
For \(x,z\in E\), its pairing is \(\langle R_Nx,pR_Nz\rangle_\mu\). Since \(p\) is real, this is the conjugate of the reversed pairing, so \(C_p=C_p^\dagger\). Taking quotient classes of the full expansion therefore proves
\[
 p(M)=C_p+O_dB_pI_d^\dagger.
 \tag{WD8}
\]
Set
\[
 Z_p=[I_d,O_dB_p],\qquad
 J_d=\begin{pmatrix}0&-iI_d\\iI_d&0\end{pmatrix}.
\]
Subtracting the adjoint of WD8, including the reversed matrix order, gives
\[
 W_p=Z_pJ_dZ_p^\dagger.
 \tag{WD9}
\]

## 3. Positivity proves all boundary columns independent

Suppose a linear combination \(F\) of the \(2d\) consecutive source polynomials in WD5 has zero quotient class. Polynomial divisibility gives \(F=Qh\), and
\[
 \deg h\le N+d-q\le N-d.
 \tag{WD10}
\]
Every polynomial appearing in \(F\) is orthogonal to \(\mathcal P_{N-d}\). Therefore
\[
 0=\langle h,F\rangle_\mu=\int Q(y)|h(y)|^2\,d\mu(y).
 \tag{WD11}
\]
The integrand is nonnegative and vanishes in integral only if \(h=0\) almost everywhere, since \(Q>0\) almost everywhere. Positive definiteness of the source Gram then gives \(h=0\) as a polynomial. Hence \(F=0\), and linear independence of the orthogonal source polynomials makes all its coefficients zero. This proves that \([I_d,O_d]\) and \(Z_p\) are injective. No root interpolation, root separation, or factor coprimality has entered the proof.

Let
\[
 R_p=Z_p^*GZ_p>0,\qquad V_p=Z_pR_p^{-1/2}.
 \tag{WD12}
\]
Then \(V_p^\dagger V_p=I_{2d}\). Its range is \(\operatorname{ran}Z_p\), and
\[
 V_p^\dagger W_pV_p=R_p^{1/2}J_dR_p^{1/2}.
 \tag{WD13}
\]
On \((\operatorname{ran}Z_p)^\perp=\ker Z_p^\dagger\), WD9 is zero. On the range, WD13 is nonsingular. The eigenvalues of \(J_d\) are \(+1\) and \(-1\), each \(d\) times: vectors \((u,iu)\) and \((u,-iu)\) give the respective eigenspaces. Invertible congruence preserves the maximal dimensions of positive and negative subspaces, since it maps such subspaces bijectively. Consequently
\[
 \boxed{\operatorname{In}W_p=(d,d,q-2d).}
 \tag{WD14}
\]

The exact relation with the original first-order current is
\[
 W_p=\sum_{j=1}^da_j\sum_{h=0}^{j-1}(M^\dagger)^hW_yM^{j-1-h}.
 \tag{WD15}
\]
For each \(j\), insert \(W_y=i(M-M^\dagger)\); every internal term cancels the following term and the two endpoints are \(i[M^j-(M^\dagger)^j]\). This proves WD15 without commuting \(M\) with its adjoint. For the unchanged physical action \(\mathscr A=kI/2+iM\),
\[
 \mathscr A^*G+G\mathscr A-kG=GW_y.
 \tag{WD16}
\]

## 4. All sign coordinates, zero directions, and isotropic spaces

For an arbitrary \(x\in E\), write \(t=Z_p^\dagger x=(a,b)\). The full inverse-coordinate decomposition is
\[
 x=Z_pR_p^{-1}t+x_0,\qquad x_0\in\ker Z_p^\dagger.
 \tag{WD17}
\]
It is unique because applying \(Z_p^\dagger\) to its first summand gives \(t\), and the two summands lie in orthogonal subspaces. In particular every \(t\) occurs and
\[
 \|x\|_G^2=t^*R_p^{-1}t+\|x_0\|_G^2.
 \tag{WD18}
\]
Set \(c_+=(a-ib)/\sqrt2\), \(c_-=(a+ib)/\sqrt2\). Matrix multiplication gives
\[
 \langle x,W_px\rangle_G
 =2\operatorname{Im}(a^*b)=\|c_+\|^2-\|c_-\|^2.
 \tag{WD19}
\]
Positive, negative, and zero form values are precisely the three corresponding norm comparisons. The radical is \(a=b=0\); zero form value alone does not imply membership in the radical.

Put
\[
 S_d=\frac1{\sqrt2}\begin{pmatrix}I_d&I_d\\iI_d&-iI_d\end{pmatrix}.
\]
Then \(t=S_d(c_+,c_-)\) and \(S_d^*J_dS_d=\operatorname{diag}(I_d,-I_d)\). Every maximal totally isotropic complex subspace has the exact form
\[
 \left\{Z_pR_p^{-1}S_d(u,Uu)+x_0:
 u\in\mathbb C^d,\ x_0\in\ker Z_p^\dagger\right\},\quad U^*U=I_d,
 \tag{WD20}
\]
and has dimension \(q-d\). Here maximality can mean maximal by inclusion. To prove this, a maximal isotropic subspace contains the radical, because adjoining a radical vector preserves every pairing. Quotient by the radical and use the \((c_+,c_-)\) coordinates. Projection of an isotropic space onto the positive coordinates is injective: a vector \((0,v)\) has value \(-\|v\|^2\). Thus the space is the graph of an isometry \(U_0:H_+\to H_-\) between subspaces of \(\mathbb C^d\). If their common dimension is less than \(d\), choose unit vectors perpendicular to \(H_+\) and \(H_-\), and map one to the other. This extends the graph to a strictly larger isotropic space, a contradiction. Hence both subspaces are the full \(\mathbb C^d\), and \(U_0\) is unitary. Conversely a unitary graph is isotropic and already has the maximum possible dimension. WD17 restores every original coordinate and metric.

Since \(Q\) and the moments are real, coefficient conjugation preserves the minimum problem and is antiunitary in \(G\). For real \(p\), it sends \(W_p\) to \(-W_p\). Applying conjugation to an eigenvector proves exact eigenvalue pairing \(+\sigma_j,-\sigma_j\), including multiplicities.

## 5. The reduced rational word and repeated poles

Let \(r=p/s\), where \(p,s\in\mathbb R[y]\), \(s\ne0\), \(\gcd(p,s)=1\), and \(\gcd(s,Q)=1\). Let \(d=\max(\deg p,\deg s)\) and assume \(1\le d\le q/2\). The Euclidean identity gives polynomials \(u,v\) with \(us+vQ=1\), so \(s(M)^{-1}=u(M)\). This is an inverse on the entire original quotient. Conversely, a common root of \(s,Q\) makes \(s(M)\) singular by evaluation at that root, so the invertibility condition is exact. Set
\[
 T_r=p(M)s(M)^{-1}.
 \tag{WD21}
\]
No rational function is integrated across a real pole. All integrations below are polynomial source pairings already defined in WD1.

The numerator \(s(x)p(y)-p(x)s(y)\) vanishes at \(y=x\). Its quotient by \(y-x\) is symmetric in \(x,y\), has real coefficients, and has degree at most \(d-1\) in each variable. Define its real symmetric coefficient matrix \(\mathcal B\) by
\[
 \frac{s(x)p(y)-p(x)s(y)}{y-x}
 =\sum_{i,j=0}^{d-1}\mathcal B_{ij}x^iy^j.
 \tag{WD22}
\]
We prove invertibility without assuming that any root is simple. If necessary interchange \(s,p\), which changes \(\mathcal B\) to \(-\mathcal B\), to arrange \(\deg s=d\). Write its leading coefficient as \(s_d\ne0\). In \(A=\mathbb C[x]/(s)\), multiplication by \(p\) is invertible by the Euclidean identity. Put
\[
 c_s(x,y)=\frac{s(y)-s(x)}{y-x}.
\]
Its \(d\)-by-\(d\) coefficient matrix is zero for \(i+j>d-1\) and is \(s_d\) for \(i+j=d-1\), so its determinant is \((-1)^{d(d-1)/2}s_d^d\ne0\). Modulo \(s(x)\), WD22 equals \(-p(x)c_s(x,y)\). To verify this even in the algebra with nilpotents, multiply both sides by \(y-x\). Their products agree, and multiplication by the monic polynomial \(y-x\) in \(A[y]\) is injective: the top nonzero coefficient of any polynomial remains its top nonzero coefficient one degree higher. Both sides have their unique remainder of degree less than \(d\) in \(x\). Thus \(\mathcal B\) is minus the product of two invertible coefficient matrices, and is invertible.

Retain the exact degree-one boundary factor \(W_y=Z_1J_1Z_1^\dagger\) from WD9, and define
\[
 \mathcal Z_d=[Z_1,M^\dagger Z_1,\ldots,(M^\dagger)^{d-1}Z_1].
 \tag{WD23}
\]
Let \(R_d\) denote the matrix with ones on its anti-diagonal and zeros elsewhere. WD15 for \(y^d\) says
\[
 W_{y^d}=\mathcal Z_d(R_d\otimes J_1)\mathcal Z_d^\dagger.
 \tag{WD24}
\]
By WD14 the left side has rank \(2d\). The right side has rank at most \(\operatorname{rank}\mathcal Z_d\le2d\). Hence \(\mathcal Z_d\) is injective.

Write \(S=s(M)\), \(P=p(M)\). Since \(P,S\) commute, \(T_rS=P\). Consequently
\[
 S^*\mathfrak W_rS=i(S^*GP-P^*GS).
 \tag{WD25}
\]
To evaluate the right side, use the linear substitution
\(x^iy^j\mapsto(M^*)^iGM^j\)
in \((y-x)\) times WD22. The image of a summand is
\[
 i\mathcal B_{ij}(M^*)^i(GM-M^*G)M^j
 =\mathcal B_{ij}(M^*)^iGW_yM^j.
\]
This is a calculation with commuting left and right multiplication operations on a middle matrix; it does not commute \(M\) and \(G\). Substitution of WD23 yields the exact denominator congruence
\[
 \boxed{S^*\mathfrak W_rS
 =G\mathcal Z_d(\mathcal B\otimes J_1)\mathcal Z_d^\dagger.}
 \tag{WD26}
\]
Equivalently, define the original-space map
\[
 Z_r=(S^{\dagger_G})^{-1}\mathcal Z_d.
\]
Then
\[
 W_r=Z_r(\mathcal B\otimes J_1)Z_r^\dagger,
 \qquad \operatorname{rank}Z_r=2d.
 \tag{WD27}
\]
Diagonalizing the real symmetric invertible matrix \(\mathcal B\) shows that each of its \(d\) nonzero eigenvalues contributes one positive and one negative eigenvalue when tensored with \(J_1\). Repeating the isometry argument WD12–14 proves
\[
 \boxed{\operatorname{In}W_r=(d,d,q-2d).}
 \tag{WD28}
\]
For a constant real rational word the current is zero. A common factor in an unreduced pair must be cancelled first, with its full multiplicity. Cancellation lowers the rational degree by its actual degree; an arbitrary unreduced degree has no signature significance. Repeated roots of the reduced denominator and repeated primaries of \(Q\) have been retained throughout.

For complete rational sign coordinates, put \(H_r=\mathcal B\otimes J_1\), \(R_r=Z_r^*GZ_r>0\). Diagonalize \(\mathcal B=U\operatorname{diag}(\beta_j)U^T\) with real orthogonal \(U\). The unitary eigenvectors \((1,i)/\sqrt2,(1,-i)/\sqrt2\) diagonalize \(J_1\). Form their tensor products with the columns of \(U\), multiply each vector by \(|\beta_j|^{-1/2}\), and order the resulting positive vectors first and negative vectors second. Let the resulting invertible matrix be \(A_r\). Then \(A_r^*H_rA_r=\operatorname{diag}(I_d,-I_d)\). For every original vector,
\[
 x=Z_rR_r^{-1}A_r(c_+,c_-)+x_0,\quad x_0\in\ker Z_r^\dagger,
 \tag{WD29}
\]
and
\[
 \langle x,W_rx\rangle_G=\|c_+\|^2-\|c_-\|^2,
 \quad
 \|x\|_G^2=(c_+,c_-)^*A_r^*R_r^{-1}A_r(c_+,c_-)+\|x_0\|_G^2.
 \tag{WD30}
\]
The same unitary-graph argument as WD20 gives all maximal isotropic subspaces. Reality of \(T_r\) gives the same exact eigenvalue pairing by the original conjugation.

For any invertible \(T\), direct expansion gives
\[
 i(T^{-1}-(T^{-1})^\dagger)
 =-(T^{-1})^\dagger i(T-T^\dagger)T^{-1}.
 \tag{WD31}
\]
Taking \(T=M^d\) gives the stated exact map between positive and negative power currents whenever \(Q(0)\ne0\).

At \(q=2d\), \(\mathcal Z_d\) is square invertible. The determinants of \(R_d\otimes J_1\) and \(\mathcal B\otimes J_1\) are respectively \((-1)^d\) and \((-1)^d(\det\mathcal B)^2\). Taking determinants in WD24 and WD26 and cancelling the common nonzero column-Gram determinant proves
\[
 \boxed{\det W_r=
 \frac{(\det\mathcal B)^2}{|\det s(M)|^2}\det W_{y^d}.}
 \tag{WD32}
\]
For a monic \(Q=\prod_\lambda(y-\lambda)^{m_\lambda}\), the exact primary decomposition of its quotient has blocks \(\mathbb C[\eta]/(\eta^{m_\lambda})\). On each block \(s(M)\) is triangular with diagonal \(s(\lambda)\). Therefore
\[
 \det s(M)=\prod_\lambda s(\lambda)^{m_\lambda}
 =\operatorname{Res}(Q,s).
 \tag{WD33}
\]
The Chinese-remainder decomposition is only across the distinct primary ideals, and the nilpotent powers within each block remain present. WD32 is independent of the source cutoff except through \(\det W_{y^d}\). A logarithmic return with weights summing to zero consequently cancels the displayed fixed rational factor exactly.

## 6. Real divisors at every degree

Let \(Q=DO\), where \(D,O\in\mathbb R[y]\) are monic, and put \(a=\deg D\), \(r=\deg O\), so \(a+r=q\). No assumption that \(D,O\) are coprime is made. Set \(T=D(M)\). Cancellation in the polynomial integral domain gives
\[
 \ker T=\{[Ob]:\deg b<a\},\qquad
 \operatorname{im}T=\{[Db]:\deg b<r\}.
 \tag{WD34}
\]
For the kernel, \(Q\mid Df\) is equivalent to \(O\mid f\). The classes displayed have unique representatives of degree below \(q\), so their dimension is \(a\). For the image, divide any polynomial \(f\) by \(O\); the \(O\)-multiple disappears after multiplication by \(D\), and the displayed \(r\) basis classes are independent by their degrees. Thus \(\operatorname{rank}T=r\).

If \(a=0\), then \(T=I\) and its current is zero. If \(r=0\), then \(T=0\) and its current is zero. If \(1\le a\le r\), WD14 applies and gives \((a,a,q-2a)\). It remains to prove the case \(1\le r\le a\).

Suppose \(x=[Db]\in\operatorname{im}T\cap(\ker T)^{\perp_G}\), with \(\deg b<r\). Its complete minimum representative is
\[
 F=R_Nx=Db+Qh=Dg,\qquad g=b+Oh,\quad \deg g\le N-a.
 \tag{WD35}
\]
It is orthogonal to \(Q\mathcal P_{N-q}\). It is also orthogonal in the source to \(O\mathcal P_{a-1}\): for such \(f\), WD3 gives \(\langle f,F\rangle_\mu=\langle J_Nf,x\rangle_G=0\). Division by the monic \(D\) proves the exact source-subspace identity
\[
 O\mathcal P_{a-1}+Q\mathcal P_{N-q}=O\mathcal P_{N-r}.
 \tag{WD36}
\]
Indeed any \(u\in\mathcal P_{N-r}\) has division \(u=Dv+w\), where \(\deg w<a\) and \(\deg v\le N-q\), while all polynomials on the left have degree at most \(N\). Because \(a\ge r\), WD35 gives \(\deg g\le N-a\le N-r\). Thus \(Og\) is one of the source polynomials in WD36, and
\[
 0=\langle Og,Dg\rangle_\mu=\int Q(y)|g(y)|^2\,d\mu(y).
 \tag{WD37}
\]
Reality of both factors has been used in this exact identity. Positivity, as in WD11, gives \(g=0\), and hence \(x=0\). We have proved
\[
 \operatorname{im}T\cap(\ker T)^{\perp_G}=\{0\}.
 \tag{WD38}
\]

Write \(K=\ker T\) and \(H=K^{\perp_G}\), with dimensions \(a\) and \(r\). Relative to this exact orthogonal decomposition,
\[
 T=\begin{pmatrix}0&B\\0&A\end{pmatrix},\qquad
 W_T=\begin{pmatrix}0&iB\\-iB^\dagger&i(A-A^\dagger)\end{pmatrix}.
 \tag{WD39}
\]
Here \(B:H\to K\) and \(A:H\to H\). If \(Bh=0\), then \(Th=Ah\in H\cap\operatorname{im}T\), so WD38 gives \(Th=0\), and then \(h\in H\cap K=0\). Hence \(B\) is injective. Set \(K_1=\operatorname{ran}B\), \(K_0=K\ominus K_1\). Every vector of \(K_0\) is annihilated by WD39, and \(\dim K_0=a-r=q-2r\).

On \(K_1\oplus H\), put \(C=iB:H\to K_1\), which is bijective, and \(H_0=i(A-A^\dagger):H\to H\). The current's quadratic form is
\[
 2\operatorname{Re}\langle x,Cy\rangle+\langle y,H_0y\rangle.
\]
Make the following full invertible coordinate map from \(H\oplus H\) into \(K_1\oplus H\):
\[
 x=(C^\dagger)^{-1}(u-\tfrac12H_0v),\qquad y=v.
 \tag{WD40}
\]
Its form value is exactly \(2\operatorname{Re}\langle u,v\rangle\), since \(H_0\) is Hermitian. Finally set \(u=(c_++c_-)/\sqrt2\), \(v=(c_+-c_-)/\sqrt2\). The value becomes \(\|c_+\|^2-\|c_-\|^2\). Thus there are \(r\) positive directions, \(r\) negative directions, and exactly the \(q-2r\) radical directions in \(K_0\). Combined with the low-degree case, this proves
\[
 \boxed{\operatorname{In}i[D(M)-D(M)^\dagger]
 =(s,s,q-2s),\qquad s=\min(\deg D,\deg O).}
 \tag{WD41}
\]
WD34–40 retain the common factors of \(D\) and \(O\) and all nilpotent primary data. They also specify a complete sign-coordinate map for the high-degree case rather than merely a count.

## 7. Native substitution and the unchanged observation

The native definitions are the original [RC1–2](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L7) and [OCP1–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L33):
\[
 k\ge17,\quad k\equiv1\pmod4,\quad q=(k+1)^2,\quad
 0<\delta<1/2,\quad\gamma>2,
\]
\[
 Q_k(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta],
 \quad d\mu_k(y)=w_h^{*k}(y)\,dy,
 \quad w_h(y)=\frac{|(2\xi/h)(1/2+iy)|^2}{2\pi}.
 \tag{WD42}
\]
The original source is even and positive, with the retained positive polynomial Grams. Since \(k\) is odd, the exact real factorization is
\[
 Q_k(y)=\prod_{b=0}^k\prod_{a=0}^{(k-1)/2}
 \left((y-(2b-k)\gamma)^2+(k-2a)^2\delta^2\right)>0
 \quad(y\in\mathbb R).
 \tag{WD43}
\]
This pairs \(a\) with \(k-a\) inside the actual product. Every squared imaginary displacement is strictly positive, so \(Q_k(0)>0\) as well. Thus no primary is removed when defining \(M^{-1}\). The degree \(q\) is even. At every original cutoff \(q-1\le N\le2q\), both actual words
\[
 r_+(y)=y^{q/2},\qquad r_-(y)=y^{-q/2}
\]
have full inertia \((q/2,q/2,0)\). The finite proofs in fact hold at every \(N\ge q-1\) where the source Grams are defined. They do not alter the programme's original four cutoff indices. Repeating the conjugate factors in WD43 preserves positivity and gives the same general theorems with the resulting full degree and primary multiplicities.

For the original onto observation \(\Lambda:E\to B\), let
\[
 Q_B=(\Lambda G^{-1}\Lambda^*)^{-1},\quad
 L=G^{-1}\Lambda^*Q_B,\quad J_B=LQ_B^{-1/2}.
 \tag{WD44}
\]
Direct multiplication gives \(\Lambda L=I_B\) and \(J_B^*GJ_B=I_B\). Thus \(J_B\) is an isometry onto \((\ker\Lambda)^{\perp_G}\). For a word factor \(W=ZHZ^\dagger\), the measured current is precisely
\[
 J_B^\dagger WJ_B=Z_BHZ_B^*,\qquad Z_B=Q_B^{1/2}\Lambda Z.
 \tag{WD45}
\]
This follows from \(J_B^*G=Q_B^{1/2}\Lambda\), so it retains the actual section and metric. If the full inertia is \((d,d,q-2d)\) and \(m=\dim\ker\Lambda\), a positive \(d\)-dimensional subspace intersects \(\operatorname{ran}J_B\) in dimension at least \(d-m\), by the dimension formula. Its restriction remains positive. No positive subspace of the restriction can exceed the maximum \(d\) in the full space. The identical argument for negative subspaces proves
\[
 (d-m)_+\le n_\pm(J_B^\dagger WJ_B)\le d.
 \tag{WD46}
\]
For \(m=8k-16\), the native half-degree words therefore have at least
\[
 \frac q2-m=\frac{(k-3)(k-11)}2>0
 \tag{WD47}
\]
observed directions of each sign. For a rational word use \(Z=Z_r\), \(H=\mathcal B\otimes J_1\); the same proof applies with its full denominator map.

For every invertible coefficient change \(S:E'\to E\), the exact transport is
\[
 G'=S^*GS,\quad M'=S^{-1}MS,\quad\Lambda'=\Lambda S,
 \quad T'=S^{-1}TS,\quad W'=S^{-1}WS,
 \quad\mathfrak W'=S^*\mathfrak WS.
 \tag{WD48}
\]
Substitution into the definition of the metric adjoint verifies these formulas. Original conjugation transports to \(S^{-1}\mathcal C S\). Hence the original physical-unit map, its inverse, and its complete metric can be carried through every theorem without changing any inertia. This calculation makes no assertion about the sign of a separately prescribed observed terminal eigenclass.

## 8. Exact boundaries of the statements

The real-coefficient condition is essential. For \(p=u+iv\), with \(u,v\) real, direct adjunction gives
\[
 W_p=W_u-[v(M)+v(M)^\dagger].
 \tag{WD49}
\]
For a concrete complete example, take \(Q=y^2+1\), the standard Gaussian probability measure, and \(N=1\). In the coefficient basis \(1,y\), \(G=I_2\), \(M=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), and \(W_y\) has eigenvalues \(2,-2\). For the nonreal factor \(D=y-i\), WD49 yields \(W_D=W_y+2I_2\), with eigenvalues \(4,0\). Thus the real-divisor theorem cannot be assigned to a nonreal pivot factor by its degree.

Positivity of \(Q\) is also doing exact work. For the same Gaussian source, \(N=1\), and \(Q=y^2-1\), the original companion matrix is \(M=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), so \(W_y=0\). The half-degree signature would fail, and WD11 fails precisely because \(Q\) changes sign. Finally, degree larger than \(q/2\) has no unrestricted signature law: the real polynomial \(p=Q\) has zero quotient action and zero current. The complete divisor formula WD41 determines that case and all other real divisors without extending WD14 beyond its proved domain.

## 9. Reading and result locators

The incoming sections 0, 1, and 2 were read in full, including all statements WS1–WS24 and WS21a–e. Incoming Section 1.1 is proved in WD5–14; Section 1.2 is proved in WD17–20 with the explicit extension of every nonmaximal partial unitary graph; Section 1.4 is proved in WD21–33; and Section 2 is proved in WD34–41 with its full source-space equality and explicit congruence. The native definitions were read directly from the retained RC1–2 and OCP source opening through OCP10. The existing machine-readable source-reading ledger for result028 supplied the programme routing before those provider reads. No exhaustive literature reading is asserted. The new identities above are derived from their stated finite inner products, polynomial division, and matrix multiplication; no unread external theorem is invoked.

The companion `check_direct_word_grams.py` constructs six independent auxiliary instances from the full source moment matrix \(\mathsf H_N\), using source mass 3 and variance 2. It computes the actual quotient metric as \((J_N\mathsf H_N^{-1}J_N^*)^{-1}\), where \(J_N\) here denotes the coefficient matrix of the unchanged remainder map. It does not obtain that metric from the orthogonal-polynomial boundary formula. It checks exact Hermitian rank, original conjugation, denominator congruence, coefficient ordering across \(G\), the high-rank determinant ratio, and the resultant with repeated primaries. The examples include a repeated real pole, a high-degree divisor sharing a primary with its complement, the first cutoff, and inverse powers. Ordinary and optimized Python produce byte-identical `DIRECT_WORD_GRAM_CHECKS.json`. These auxiliary matrix calculations supplement the written proofs and are not native-period evaluations.
