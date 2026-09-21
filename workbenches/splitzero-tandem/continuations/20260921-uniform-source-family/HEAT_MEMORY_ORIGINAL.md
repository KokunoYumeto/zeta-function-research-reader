# Uniform observed heat with full memory and the original metric

Date: 2026-09-21. This independent derivation verifies equations (18)–(23) and (33)–(51) of the supplied **Uniform control of the original source families** intake. Its unchanged text is retained in `USER_INTAKE_VERBATIM.txt`. All results below concern the original finite metric spaces and maps. Orthonormal coordinates are used only through explicitly stated isometries. No kernel-invariance assumption is imposed.

## 1. Original metric, attained quotient, and exact block maps

Let \(E\) be a complex vector space of dimension \(q\), with positive Hermitian metric \(G\), and let \(\Lambda:E\to B\) be onto, where \(n=\dim B\). Let \(K=\ker\Lambda\), \(m=\dim K=q-n\), and define
\[
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\qquad
 L=G^{-1}\Lambda^*Q.
\]
Then
\[
 \Lambda L=I_B,\qquad L^*GL=Q.
\]
For \(k\in K\) and \(b\in B\),
\[
 k^*GLb=k^*\Lambda^*Qb=(\Lambda k)^*Qb=0.
\]
Thus \(L\) is the exact isometry from \((B,Q)\) onto \(K^{\perp_G}\); \(P_B=L\Lambda\) is the \(G\)-orthogonal projection onto that image and \(P_K=I-P_B\). For every operator \(T:E\to E\), cyclicity of finite-dimensional trace gives
\[
 \operatorname{Tr}_B(\Lambda TL)=\operatorname{Tr}_E(P_BT).
 \tag{H1}
\]
This identity retains the observation target and its minimum section.

Choose any isometric inclusion \(I_K:(K,G|_K)\to(E,G)\). In the orthogonal sum \(K\oplus LB\), the fixed original action \(M:E\to E\) is
\[
 M=
 \begin{pmatrix}M_K&D\\ C&M_B\end{pmatrix},
\quad
 M_K=I_K^\dagger MI_K,\quad D=I_K^\dagger ML,\quad
 C=\Lambda MI_K,\quad M_B=\Lambda ML.
 \tag{H2}
\]
Every dagger in these blocks uses the displayed domain and target metrics. In particular \(D:B\to K\), \(C:K\to B\), and \(C\) need not vanish. The full positive operator is
\[
 H=M^\dagger M=
 \begin{pmatrix}A&B_H\\ B_H^\dagger&D_H\end{pmatrix},
 \tag{H3}
\]
where
\[
 A=M_K^\dagger M_K+C^\dagger C,\qquad
 B_H=M_K^\dagger D+C^\dagger M_B,\qquad
 D_H=D^\dagger D+M_B^\dagger M_B.
 \tag{H4}
\]
These are precisely the intake's complete blocks. Set \(J_B=M_B^\dagger M_B\).

All subsequent eigenvalue, norm, and matrix calculations may be made after isometries of \((K,G|_K)\) and \((B,Q)\) to Euclidean spaces. Their values are unchanged by those isometries.

## 2. Positive memory without a spectral-gap hypothesis

### 2.1 The exact Schur remainder

If \(k\in\ker A\), positivity of \(H\) applied to \((uk,b)\), with arbitrary \(u\in\mathbb C\), gives
\[
 0\le 2\Re(\overline u\,\langle k,B_Hb\rangle)+\langle b,D_Hb\rangle.
\]
An unbounded choice of the phase and modulus of \(u\) forces \(\langle k,B_Hb\rangle=0\) for every \(b\). Therefore
\[
 \ker A\subseteq\ker B_H^\dagger,\qquad
 \operatorname{ran}B_H\subseteq\operatorname{ran}A.
 \tag{H5}
\]
Let \(A^+\) denote its positive-range inverse, zero on \(\ker A\). Completing the square, for every \(k,b\),
\[
\begin{aligned}
 \langle(k,b),H(k,b)\rangle
 ={}&\langle k+A^+B_Hb,\ A(k+A^+B_Hb)\rangle\\
 &+\langle b,(D_H-B_H^\dagger A^+B_H)b\rangle.
\end{aligned}
\]
Taking \(k=-A^+B_Hb\) proves
\[
 T=B_H^\dagger A^+B_H\succeq0,\qquad
 S=D_H-T\succeq0,\qquad T\preceq D_H.
 \tag{H6}
\]

Let \(P_\lambda\) be the spectral projection of \(A\) at the distinct positive eigenvalue \(\lambda\), and put
\[
 C_\lambda=\lambda^{-1}B_H^\dagger P_\lambda B_H\succeq0.
\]
Equation (H5) yields
\[
 T=\sum_{\lambda>0}C_\lambda,\qquad
 \mathcal M(t):=B_H^\dagger e^{-tA}B_H
 =\sum_{\lambda>0}\lambda e^{-t\lambda}C_\lambda.
 \tag{H7}
\]
In particular no unrecorded memory remains at the zero eigenvalue.

For \(z\) off the negative spectrum of \(A\), the exact memory pencil is
\[
\begin{aligned}
 \mathcal F(z)
 &=zI_B+D_H-B_H^\dagger(zI_K+A)^{-1}B_H\\
 &=zI_B+S+\sum_{\lambda>0}\frac{z}{z+\lambda}C_\lambda.
\end{aligned}
 \tag{H8}
\]
Whenever the full resolvent and these expressions are defined, block elimination gives
\[
 \Lambda(zI_E+H)^{-1}L=\mathcal F(z)^{-1}.
 \tag{H9}
\]
For \(\Re z>0\), all expressions are defined because \(H\succeq0\). For \(\Im z>0\),
\[
 \Im\mathcal F(z)
 =(\Im z)\left[I_B+\sum_{\lambda>0}
       \frac{\lambda}{|z+\lambda|^2}C_\lambda\right]\succ0.
 \tag{H10}
\]
This also proves invertibility there. The matrices \(C_\lambda\) are never required to commute.

For completeness, define \(Y(t)=\Lambda e^{-tH}L\) and let \(X(t)\) be the kernel block of \(e^{-tH}L\). The original block evolution is
\[
 X'=-AX-B_HY,\quad X(0)=0,\qquad
 Y'=-B_H^\dagger X-D_HY,\quad Y(0)=I_B.
\]
Consequently
\[
 X(t)=-\int_0^t e^{-(t-u)A}B_HY(u)\,du,
\]
and the full observed equation is exactly
\[
 Y'(t)=-D_HY(t)+\int_0^t\mathcal M(t-u)Y(u)\,du,\qquad Y(0)=I_B.
 \tag{H11}
\]
Both \(D^\dagger D\) inside \(D_H\) and the full memory convolution remain.

### 2.2 Derivatives, integrals, and the half-plane bounds

For every integer \(j\ge0\),
\[
 (-1)^j\mathcal M^{(j)}(t)
 =\sum_{\lambda>0}\lambda^{j+1}e^{-t\lambda}C_\lambda\succeq0.
\]
By the substitution \(u=\lambda t\) and the elementary gamma integral,
\[
 \int_0^\infty t^j(-1)^j\mathcal M^{(j)}(t)\,dt
 =j!\sum_{\lambda>0}C_\lambda=j!T\preceq j!D_H.
 \tag{H12}
\]
Also \(\sup_{u\ge0}u^{j+1}e^{-u}=((j+1)/e)^{j+1}\), so
\[
 t^{j+1}(-1)^j\mathcal M^{(j)}(t)
 \preceq ((j+1)/e)^{j+1}T.
 \tag{H13}
\]
These estimates have no lower positive bound for \(\lambda\).

Differentiating the finite rational expression (H8), for \(j\ge1\),
\[
 (-1)^{j-1}\bigl(\mathcal F^{(j)}(z)-\mathbf1_{j=1}I_B\bigr)
 =j!\sum_{\lambda>0}\frac{\lambda}{(z+\lambda)^{j+1}}C_\lambda
 \quad(z>0).
\]
Writing \(u=\lambda/z\), the scalar maximum
\[
 \sup_{u\ge0}\frac{u}{(1+u)^{j+1}}
 =\frac{j^j}{(j+1)^{j+1}}
\]
occurs at \(u=1/j\). Hence
\[
 0\preceq z^j(-1)^{j-1}
 \bigl(\mathcal F^{(j)}(z)-\mathbf1_{j=1}I_B\bigr)
 \preceq j!\frac{j^j}{(j+1)^{j+1}}T.
 \tag{H14}
\]
This proves every constant in intake equations (35)–(41).

### 2.3 Exact minimal memory and its original-space isometry

The original coupled kernel space is
\[
 K_{\rm coupled}=\bigoplus_{\lambda>0}\operatorname{ran}(P_\lambda B_H).
\]
Each summand lies in a distinct eigenspace of \(A\). Its orthogonal complement in \(K\) is \(A\)-invariant and annihilated by \(B_H^\dagger\). Thus the full \(H\) splits as its restriction to \(K_{\rm coupled}\oplus LB\), plus the original decoupled kernel block.

Let \(R_\lambda=\operatorname{ran}C_\lambda\), with its inherited metric, and define
\[
 J_\lambda=\lambda^{-1/2}P_\lambda B_HC_\lambda^{+1/2}:R_\lambda\to K.
\]
Because \(B_H^\dagger P_\lambda B_H=\lambda C_\lambda\),
\[
 J_\lambda^\dagger J_\lambda
 =C_\lambda^{+1/2}C_\lambda C_\lambda^{+1/2}=I_{R_\lambda}.
\]
The image is exactly \(\operatorname{ran}(P_\lambda B_H)\), because multiplying by the positive-range inverse does not change that range. The direct sum \(J=\bigoplus J_\lambda\) is therefore an isometry onto \(K_{\rm coupled}\). Let
\[
 A_{\min}=\bigoplus_{\lambda>0}\lambda I_{R_\lambda},\qquad
 B_{\min}=\operatorname{stack}_{\lambda>0}\sqrt\lambda\,C_\lambda^{1/2}.
\]
Then
\[
 AJ=JA_{\min},\qquad
 J_\lambda\sqrt\lambda C_\lambda^{1/2}
 =P_\lambda B_H C_\lambda^{+1/2}C_\lambda^{1/2}
 =P_\lambda B_H.
\]
The last equality holds since \(C_\lambda\) and \(P_\lambda B_H\) have the same kernel. Summing proves \(JB_{\min}=B_H\). Therefore
\[
 \begin{pmatrix}A_{\min}&B_{\min}\\B_{\min}^\dagger&D_H\end{pmatrix}
\]
is the exact isometric restriction of \(H\) to its coupled block, and is positive. It gives the identical \(Y(t)\), memory, and compressed resolvent.

Its kernel-state dimension is
\[
 r_{\rm mem}=\sum_{\lambda>0}\operatorname{rank}C_\lambda.
\]
To prove minimality, take any finite selfadjoint realization
\(\widetilde B^\dagger(zI+\widetilde A)^{-1}\widetilde B\)
of the same memory transform. At the pole \(-\lambda\), its residue is
\(\widetilde B^\dagger\widetilde P_\lambda\widetilde B\); equality of the rational transforms forces this residue to equal \(\lambda C_\lambda\). Therefore
\[
 \dim\operatorname{ran}\widetilde P_\lambda
 \ge\operatorname{rank}C_\lambda.
\]
The eigenspaces for distinct poles are disjoint. Summing proves the required lower bound \(r_{\rm mem}\). Extra states with zero residue are decoupled from the memory and cannot lower it.

## 3. Uniform heat comparison by the original coupling and leakage ranks

Put
\[
 H_0=\operatorname{diag}(A,D_H),\qquad
 O=H-H_0=
 \begin{pmatrix}0&B_H\\B_H^\dagger&0\end{pmatrix},\qquad
 r_c=\operatorname{rank}B_H.
\]
Let
\[
 Q_{\rm mix}(t)=\operatorname{Tr}e^{-tH}
       -\operatorname{Tr}e^{-tA}-\operatorname{Tr}e^{-tD_H}.
\]

### 3.1 Nonnegative trace gaps on each original block

If \(v\) is a unit eigenvector of \(A\), regard it as \((v,0)\in E\). Its spectral measure \(\mu_v\) for \(H\) is a probability measure. The scalar convexity of \(x\mapsto e^{-tx}\) gives
\[
 \langle v,e^{-tH}v\rangle
 =\int e^{-tx}\,d\mu_v(x)
 \ge e^{-t\int x\,d\mu_v(x)}
 =e^{-t\langle v,Hv\rangle}.
\]
Sum over an orthonormal eigenbasis of \(A\). The result is
\[
 \operatorname{Tr}(P_Ke^{-tH})-\operatorname{Tr}e^{-tA}\ge0.
\]
An eigenbasis of \(D_H\) similarly gives
\[
 a(t):=\operatorname{Tr}(P_Be^{-tH})-\operatorname{Tr}e^{-tD_H}\ge0.
\]
Thus
\[
 0\le a(t)\le Q_{\rm mix}(t).
 \tag{H15}
\]
This is a trace argument; an operator order between the two observed heat matrices is not used.

### 3.2 Signed rank bound, with its full interlacing proof

The nonzero eigenvalues of \(O\) are the pairs
\(\pm\sigma_j(B_H)\), \(1\le j\le r_c\). Hence its positive and negative parts \(O_+\) and \(O_-\) each have rank \(r_c\).

Here is the needed rank fact. If \(X,Y\succeq0\), \(X=Y-R\), \(R\succeq0\), and \(\operatorname{rank}R\le r\), order their \(q\) eigenvalues increasingly. Min–max gives
\[
 \lambda_j(X)\le\lambda_j(Y),\qquad
 \lambda_j(X)\ge\lambda_{j-r}(Y)\quad(j>r).
\]
For a decreasing function \(0\le f\le1\) on \([0,\infty)\),
\[
 \sum_jf(\lambda_j(X))
 \le r+\sum_{j=1}^{q-r}f(\lambda_j(Y))
 \le r+\sum_{j=1}^qf(\lambda_j(Y)).
 \tag{H16}
\]
The first eigenvalue inequality also gives nonnegative trace difference.

Apply (H16) to \(X=H\), \(Y=H_0+O_+\), and \(R=O_-\). Both endpoint matrices are positive, and \(Y=H+O_-\). Then
\[
 \operatorname{Tr}e^{-tH}
 \le r_c+\operatorname{Tr}e^{-t(H_0+O_+)}
 \le r_c+\operatorname{Tr}e^{-tH_0},
\]
where the second inequality follows from min–max and \(O_+\succeq0\). Therefore
\[
 0\le Q_{\rm mix}(t)\le r_c.
 \tag{H17}
\]
The signed ranks give \(r_c\), not the total rank \(2r_c\).

### 3.3 The exact small-time quadratic estimate

For \(0\le s\le1\), \(H_s=H_0+sO=(1-s)H_0+sH\succeq0\). Put
\(\phi(s)=\operatorname{Tr}e^{-tH_s}\).
Differentiating the exponential by its convergent power series and cyclically moving factors in the trace gives
\[
 \phi'(s)=-t\operatorname{Tr}(Oe^{-tH_s}),
\]
and a second differentiation gives
\[
 \phi''(s)=t^2\int_0^1
       \operatorname{Tr}(Oe^{-(1-u)tH_s}Oe^{-utH_s})\,du.
 \tag{H18}
\]
In an orthonormal eigenbasis of \(H_s\), the integrand is
\[
 \sum_{i,j}|O_{ij}|^2e^{-t[(1-u)\lambda_j+u\lambda_i]},
\]
which lies between \(0\) and \(\|O\|_{\rm HS}^2\). Since
\(\phi'(0)=0\) and \(\|O\|_{\rm HS}^2=2\|B_H\|_{\rm HS}^2\),
\[
 Q_{\rm mix}(t)=\int_0^1(1-s)\phi''(s)\,ds
 \le t^2\|B_H\|_{\rm HS}^2.
\]
Together with (H17),
\[
 0\le Q_{\rm mix}(t)
 \le \min\{r_c,\ t^2\|B_H\|_{\rm HS}^2\}.
 \tag{H19}
\]

### 3.4 Leakage and the complete observed error

Since \(D_H=J_B+D^\dagger D\), let
\[
 b(t)=\operatorname{Tr}e^{-tJ_B}-\operatorname{Tr}e^{-tD_H}\ge0.
\]
The rank fact (H16), with \(r_D=\operatorname{rank}D\), gives \(b(t)\le r_D\). Also
\[
 b(t)=t\int_0^1
 \operatorname{Tr}\bigl(D^\dagger D\,e^{-t(J_B+sD^\dagger D)}\bigr)\,ds.
\]
The exponential is a positive contraction, so
\[
 0\le b(t)\le\min\{r_D,\ t\|D\|_{\rm HS}^2\}.
 \tag{H20}
\]
The actual observed error is exactly \(a(t)-b(t)\). Equations (H15), (H19), and (H20) prove
\[
\boxed{
 -\min\{r_D,t\|D\|_{\rm HS}^2\}
 \le
 \operatorname{Tr}_B(\Lambda e^{-tM^\dagger M}L)
 -\operatorname{Tr}_B e^{-tM_B^\dagger M_B}
 \le
 \min\{r_c,t^2\|B_H\|_{\rm HS}^2\}.}
 \tag{H21}
\]
Because \(D:B\to K\) and \(B_H:B\to K\), both ranks are at most
\(\min(m,n)\). In particular,
\[
\boxed{
 \sup_{t\ge0}
 \left|
 \operatorname{Tr}_B(\Lambda e^{-tM^\dagger M}L)
 -\operatorname{Tr}_B e^{-tM_B^\dagger M_B}
 \right|
 \le\max(r_D,r_c)\le\min(m,n).}
 \tag{H22}
\]
This slightly strengthens the intake's dimension bound when the observed target is smaller than the kernel. No step sets \(C=0\), drops \(D^\dagger D\), or discards memory.

For a source family where the established original kernel rank is \(m_k=8k-16\), (H22) yields the claimed \(8k-16\) bound at every allowed cutoff, metric, and heat time. If additionally \(q_k=(k+1)^2\), then
\[
 0\le\frac{\sup_{t\ge0}|\text{observed error}|}{q_k}
 \le\frac{8k-16}{(k+1)^2}\longrightarrow0.
\]
These last two arithmetic dimension identities are inputs from the original family; the finite-dimensional theorem does not derive them independently.

### 3.5 Sharpness and a finite operator-order counterexample

Both signs in (H21) are needed. In the Euclidean space \(\mathbb C^2=K\oplus B\), take
\[
 M_-=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
Then \(J_B=0\), \(H=\operatorname{diag}(0,1)\), and the observed error is
\[
 e^{-t}-1\longrightarrow-1.
\]
Thus the coefficient one in the dimension bound cannot be lowered.

For the positive sign, take
\[
 M_+=\begin{pmatrix}0&0\\\sqrt a&\sqrt d\end{pmatrix},
 \qquad a,d>0.
\]
Here \(D=0\), \(C=\sqrt a\ne0\), \(J_B=d\), and
\[
 H=\begin{pmatrix}a&\sqrt{ad}\\\sqrt{ad}&d\end{pmatrix}.
\]
Since \(H^2=(a+d)H\),
\[
 \operatorname{Tr}(P_Be^{-tH})
 =\frac{a}{a+d}+\frac{d}{a+d}e^{-t(a+d)}.
\]
The error tends to \(a/(a+d)\), arbitrarily close to one when \(a/d\) grows. This example has a noninvariant kernel. Direct sums produce the corresponding sharp rank-scale examples.

The observed trace inequality (H15) cannot be upgraded to operator order. At \(t=\log2\), take
\[
 M=\begin{pmatrix}0&0&0\\1&0&-2\\-2&-1&0\end{pmatrix},
 \qquad
 H=M^*M=\begin{pmatrix}5&2&-2\\2&1&0\\-2&0&4\end{pmatrix},
 \qquad K=\mathbb Ce_1.
\]
The eigenvalues of \(H\) are \(0,3,7\), and \(D_H=\operatorname{diag}(1,4)\). The spectral-projector formula
\[
 2^{-H}=\sum_{\lambda\in\{0,3,7\}}2^{-\lambda}
 \prod_{\mu\ne\lambda}\frac{H-\mu I}{\lambda-\mu}
\]
gives the exact rational difference
\[
 (2^{-H})_{BB}-2^{-D_H}
 =
 \begin{pmatrix}
 1523/5376&-403/2688\\
 -403/2688&95/1344
 \end{pmatrix}.
 \tag{H23}
\]
Its determinant is \(-211/86016<0\), while its trace is
\(1903/5376>0\). Thus it has one negative and one positive eigenvalue. This exact fixture explains why the scalar spectral-measure proof is essential.

## 4. Determinant mixing and the original observed pencil

For \(z>0\), define
\[
 g(z)=\log\det(zI_K+A)+\log\det(zI_B+D_H)
                    -\log\det(zI_E+H).
\]
The exact block determinant identity gives
\[
 g(z)=\log\det(zI_B+D_H)-\log\det\mathcal F(z).
 \tag{H24}
\]
For positive numbers \(x,y\),
\[
 \log x-\log y=\int_0^\infty(e^{-ty}-e^{-tx})\,dt/t.
\]
One can prove this by differentiating in \(x\), integrating \(e^{-tx}\), and fixing the zero value at \(x=y\). Apply it to the finite lists of positive eigenvalues after adding \(z\). Equality of their total dimensions cancels the constant term at \(t=0\), and (H19) gives absolute convergence. Hence
\[
 g(z)=\int_0^\infty e^{-zt}\frac{Q_{\rm mix}(t)}t\,dt\ge0.
 \tag{H25}
\]
For \(j\ge1\), differentiation is justified by the same bounds near zero and exponential decay at infinity, giving
\[
 (-1)^jg^{(j)}(z)=
 \int_0^\infty e^{-zt}t^{j-1}Q_{\rm mix}(t)\,dt\ge0.
\]
Consequently
\[
 0\le g(z)\le\|B_H\|_{\rm HS}^2/z^2,
 \tag{H26}
\]
and
\[
 0\le(-1)^jg^{(j)}(z)
 \le
 \min\left\{\frac{r_c(j-1)!}{z^j},
       \frac{\|B_H\|_{\rm HS}^2(j+1)!}{z^{j+2}}\right\}.
 \tag{H27}
\]

For the logarithmic rank bound, put \(R_z=B_H^\dagger(zI_K+A)^{-1}B_H\). It is positive of rank at most \(r_c\), and
\[
 zI_B+D_H=\mathcal F(z)+R_z,\qquad \mathcal F(z)\succeq zI_B
\]
by (H8). Thus
\[
 g(z)=\log\det(I_B+\mathcal F(z)^{-1/2}R_z\mathcal F(z)^{-1/2}).
\]
There are at most \(r_c\) nonzero eigenvalues in its added matrix. Moreover
\[
 zI_B+D_H
 \preceq (1+\|D_H\|/z)\mathcal F(z),
\]
since the right side is at least \((z+\|D_H\|)I_B\). Therefore each corresponding multiplicative eigenvalue is at most \(1+\|D_H\|/z\), and
\[
 g(z)\le r_c\log(1+\|D_H\|/z).
\]
Applying the same block determinant identity in the other order proves
\[
 0\le g(z)\le r_c\log\left(1+\frac{\min(\|A\|,\|D_H\|)}z\right).
 \tag{H28}
\]

The original leakage determinant is
\[
 \ell(z)=\log\det(zI_B+D_H)-\log\det(zI_B+J_B).
\]
It has the exact form
\[
 \ell(z)=\log\det\left(I_B+
 (zI_B+J_B)^{-1/2}D^\dagger D(zI_B+J_B)^{-1/2}\right)\ge0.
\]
At most \(r_D\) eigenvalues are nonzero, and each is at most \(\|D\|^2/z\). Thus
\[
 0\le\ell(z)\le r_D\log(1+\|D\|^2/z).
 \tag{H29}
\]
Subtracting (H24) gives the original comparison
\[
 \log\det\mathcal F(z)-\log\det(zI_B+J_B)=\ell(z)-g(z).
 \tag{H30}
\]
The two nonnegative terms are retained. The usable asymmetric bound is
\[
\boxed{
 -r_c\log\left(1+\frac{\min(\|A\|,\|D_H\|)}z\right)
 \le\ell(z)-g(z)
 \le r_D\log(1+\|D\|^2/z).}
 \tag{H31}
\]
Every block compression has norm bounded by the full positive operator norm, and \(D\) is a compression of \(M\). Therefore
\[
 \|A\|,\|D_H\|,\|D\|^2\le\|M\|_G^2,
\]
and
\[
 |\ell(z)-g(z)|
 \le\max(r_D,r_c)\log(1+\|M\|_G^2/z)
 \le m\log(1+\|M\|_G^2/z).
 \tag{H32}
\]
This proves intake equation (50), with a sharper version in (H31).

The intake additionally supplies, for its joint-source metric,
\(\log^+\|M\|_{G_N^J}=O_h(k\log^2(q+2))\). For fixed \(z>0\),
\[
 \log(1+\|M\|^2/z)
 \le\log(1+z^{-1})+2\log^+\|M\|.
\]
Together with \(m=O(k)\), this gives
\[
 |\ell(z)-g(z)|=O_h(k^2\log^2(q+2)).
\]
If \(q=(k+1)^2\), division by \(kq\) gives
\[
 O_h\!\left(\frac{k\log^2((k+1)^2+2)}{(k+1)^2}\right)\to0.
\]
The asymptotic implication is proved here. The source-family norm estimate itself remains the cited original arithmetic input, and is not proved or altered by the finite-dimensional argument.

## 5. Metric changes and complete heat derivatives

### 5.1 Endpoint comparison in the original fixed coefficient space

Suppose two positive metrics \(G_x,G_y\) on the same coefficient space obey
\[
 e^{-b}G_x\preceq G_y\preceq e^{-a}G_x,\qquad a\le b.
 \tag{H33}
\]
For every nonzero coefficient vector \(v\),
\[
 e^{-(b-a)}
 \frac{\|Mv\|_{G_x}^2}{\|v\|_{G_x}^2}
 \le
 \frac{\|Mv\|_{G_y}^2}{\|v\|_{G_y}^2}
 \le
 e^{b-a}
 \frac{\|Mv\|_{G_x}^2}{\|v\|_{G_x}^2}.
\]
The min–max formula for the eigenvalues of the positive squared action, applied to the same coefficient subspaces at both endpoints, therefore gives
\[
 e^{-(b-a)/2}s_j(M;G_x)
 \le s_j(M;G_y)\le
 e^{(b-a)/2}s_j(M;G_x).
 \tag{H34}
\]
This compares the exact metric singular values, with the identity of coefficient spaces as the linking map.

Let \(r=\operatorname{rank}M\), \(\delta=b-a\). The \(q-r\) zero singular directions have the same heat contribution at both endpoints. For each positive squared singular value pair \(\lambda,\mu\),
\(|\log\mu-\log\lambda|\le\delta\). The function
\(s\mapsto e^{-t e^s}\) has absolute derivative
\(te^s e^{-te^s}\le1/e\). Summing yields
\[
 \sup_{t\ge0}|\operatorname{Tr}e^{-tH_y}-\operatorname{Tr}e^{-tH_x}|
 \le r\delta/e.
 \tag{H35}
\]
For \(z>0\), the derivative of \(\log(z+e^s)\) lies in \((0,1)\), giving
\[
 |\log\det(zI+H_y)-\log\det(zI+H_x)|\le r\delta.
 \tag{H36}
\]
These are intake (18)–(19).

A sharper bounded finite-change version of (H35) is also available. Put
\[
 \Psi(0)=0,\qquad
 \Psi(\delta)=(1-e^{-\delta})
     \exp\left[-\frac{\delta}{e^\delta-1}\right]\quad(\delta>0).
\]
For \(\alpha=e^\delta>1\), the maximum of
\(e^{-u}-e^{-\alpha u}\), \(u\ge0\), occurs at
\(u=(\log\alpha)/(\alpha-1)\), and equals \(\Psi(\delta)\).
A smaller allowed ratio gives a smaller maximum because
\(e^{-u}-e^{-\alpha u}\) increases pointwise in \(\alpha\).
Hence
\[
 \sup_{t\ge0}|\operatorname{Tr}e^{-tH_y}-\operatorname{Tr}e^{-tH_x}|
 \le r\Psi(\delta)\le r\min(\delta/e,1).
 \tag{H37}
\]
No norm bound for \(M\) is needed.

### 5.2 The compatible frame for logarithmic source paths

Use the original positive covariance family
\[
 C(x)=G_\circ^{-1}+\sum_i e^{x_i}\Omega_i,\qquad G(x)=C(x)^{-1},
 \quad\Omega_i\succeq0.
\]
Along \(x(s)=x_0+sv\), put
\[
 v_-=\min(0,v_1,\ldots,v_p),\quad
 v_+=\max(0,v_1,\ldots,v_p),\quad
 \Delta_v=v_+-v_-.
\]
Since
\[
 C'=\sum_i v_i e^{x_i}\Omega_i,
\]
the positive baseline and source terms imply
\[
 v_-C\preceq C'\preceq v_+C.
\]
Differentiating \(GC=I\), \(G'=-GC'G\), gives
\[
 -v_+G\preceq G'\preceq-v_-G.
 \tag{H38}
\]

Choose \(F(s_0)^*G(s_0)F(s_0)=I\) and solve the linear matrix equation
\[
 F'=-\tfrac12G^{-1}G'F.
 \tag{H39}
\]
Its fundamental solution is invertible. Direct differentiation gives
\[
 (F^*GF)'=-\tfrac12F^*G'F+F^*G'F-\tfrac12F^*G'F=0.
\]
Thus \(F^*GF=I\), \(F^{-1}=F^*G\), and
\[
 B(s)=F^*G'F=B^*,\qquad -v_+I\preceq B\preceq-v_-I.
 \tag{H40}
\]
The spectral width of \(B\) is at most \(\Delta_v\).

Write the fixed original action in this frame as
\(\widetilde M=F^{-1}MF\). Then \(F^{-1}F'=-B/2\), so
\[
 \widetilde M'=\tfrac12[B,\widetilde M].
 \tag{H41}
\]
All following matrices are in this frame; the original coefficient action \(M\) is unchanged. With \(\widetilde H=\widetilde M^*\widetilde M\),
\[
 \widetilde H'=\widetilde M^*B\widetilde M
                  -\tfrac12(B\widetilde H+\widetilde H B).
 \tag{H42}
\]
Let \(c\) be the midpoint of the extreme eigenvalues of \(B\), and \(B_0=B-cI\). The scalar terms cancel identically in (H42), and
\[
 \|B_0\|\le\Delta_v/2.
 \tag{H43}
\]
This subtraction acts on the connection matrix only; it does not replace the original arithmetic action.

### 5.3 Both divided-difference constants

For \(x,y\ge0\), let
\[
 d_t(x,y)=
 \begin{cases}
 (e^{-tx}-e^{-ty})/(x-y),&x\ne y,\\
 -te^{-tx},&x=y.
 \end{cases}
\]
Then
\[
 \sqrt{xy}\,|d_t(x,y)|\le1/e,\qquad
 \frac{x+y}{2}|d_t(x,y)|\le1/2.
 \tag{H44}
\]
For the first inequality, if \(x,y>0\), the function
\(u\mapsto e^{-t e^u}\) is \(1/e\)-Lipschitz, so
\[
 |e^{-tx}-e^{-ty}|\le|\log x-\log y|/e.
\]
Writing \(x=\rho e^a,y=\rho e^{-a}\) proves
\[
 \frac{\sqrt{xy}|\log x-\log y|}{|x-y|}
 =\frac{|a|}{|\sinh a|}\le1.
\]
The diagonal limit is \(txe^{-tx}\le1/e\); if either \(x\) or \(y\) is zero, the product is zero.

For the second inequality take \(tx=b+d\), \(ty=b\), \(b,d\ge0\). For \(d>0\), twice the required left side is
\[
 e^{-b}(1+2b/d)(1-e^{-d}).
\]
For \(d\ge2\), this decreases with \(b\), so its maximum is
\(1-e^{-d}<1\). For \(0<d<2\), its maximum occurs at
\(b=1-d/2\) and equals
\[
 \frac2e\frac{\sinh(d/2)}{d/2}
 \le\frac2e\sinh1=1-e^{-2}<1.
\]
Here \(\sinh u/u\) increases for \(u>0\), because
\(u\cosh u-\sinh u\) has derivative \(u\sinh u>0\) and value zero at zero. The limits \(d=0\) and \(t=0\) follow by continuity. Both individual constants are sharp: the first at \(tx=ty=1\), the second as \(ty=0\) and \(tx\to\infty\).

The derivative formula for a matrix exponential can be read directly from
\[
 \frac d{ds}e^{-t\widetilde H}
 =-\int_0^t e^{-(t-u)\widetilde H}\widetilde H'
                       e^{-u\widetilde H}\,du.
\]
In an eigenbasis of \(\widetilde H\), its \(ij\)-entry equals
\(d_t(\lambda_i,\lambda_j)\widetilde H'_{ij}\).

Let \(\widetilde M=U\widetilde H^{1/2}\) be its actual polar decomposition. Equation (H42) gives
\[
 \widetilde H'_{ij}
 =\sqrt{\lambda_i\lambda_j}(U^*B_0U)_{ij}
       -\tfrac12(\lambda_i+\lambda_j)(B_0)_{ij}.
\]
Applying (H44) entry by entry and the Hilbert–Schmidt triangle inequality proves
\[
 \left\|\frac d{ds}e^{-t\widetilde H}\right\|_{\rm HS}
 \le e^{-1}\|U^*B_0U\|_{\rm HS}+\tfrac12\|B_0\|_{\rm HS}
 \le\left(\frac1e+\frac12\right)\frac{\sqrt q}{2}\Delta_v.
 \tag{H45}
\]
This proves intake (20), including zero and repeated eigenvalues.

There is a useful rank refinement. Put \(r=\operatorname{rank}M\) and let \(P_+\) be the support projection of \(\widetilde H\). The first term satisfies
\(\|U^*B_0U\|_{\rm HS}\le\sqrt r\,\|B_0\|\).
The second term has zero entries on
\(\ker\widetilde H\times\ker\widetilde H\). If \(B_{++}\) and \(B_{+0}\) are its blocks, the square of the norm of the remaining entries is
\[
 \|B_{++}\|_{\rm HS}^2+2\|B_{+0}\|_{\rm HS}^2
 \le2r\|B_0\|^2,
\]
because
\(\|B_{++}\|_{\rm HS}^2+\|B_{+0}\|_{\rm HS}^2
 =\|P_+B_0\|_{\rm HS}^2\le r\|B_0\|^2\).
It is also at most \(q\|B_0\|^2\). Thus
\[
 \left\|\frac d{ds}e^{-t\widetilde H}\right\|_{\rm HS}
 \le\frac{\Delta_v}{2}
       \left(\frac{\sqrt r}{e}
              +\frac{\sqrt{\min(q,2r)}}2\right).
 \tag{H46}
\]
This refinement is zero when the original action is zero.

### 5.4 Moving fixed-kernel projections, with the exact sign

Let \(K\subset E\) be fixed in original coefficient coordinates and let
\(P(s)\) be the Euclidean orthogonal projection onto \(F(s)^{-1}K\).
A fixed vector \(k\in K\) has frame coordinates
\(u(s)=F(s)^{-1}k\), satisfying \(u'=Bu/2\). Since \(Pu=u\),
differentiation gives
\[
 P'u=(I-P)u'=\tfrac12(I-P)Bu.
\]
Differentiating \(P^2=P\) gives zero diagonal blocks for \(P'\); differentiating \(P^*=P\) makes its off-diagonal blocks adjoints. Hence
\[
 P'=\tfrac12[(I-P)BP+PB(I-P)].
 \tag{H47}
\]
This is intake (22) with its positive sign. The complementary projection has the negative derivative.

Let \(\ell=\operatorname{rank}P\), \(d=\min(\ell,q-\ell)\), and
\(T_P=(I-P)B_0P\). The nonzero eigenvalues of \(P'\) are
\(\pm\sigma_j(T_P)/2\). Therefore
\[
 \operatorname{Tr}(P')_+
 =\operatorname{Tr}(P')_-
 =\tfrac12\|T_P\|_1
 \le d\Delta_v/4.
 \tag{H48}
\]
For any positive contraction \(Z\),
\[
 -\operatorname{Tr}(P')_-\le\operatorname{Tr}(P'Z)
                    \le\operatorname{Tr}(P')_+.
\]
Apply this to \(Z=e^{-t\widetilde H}\). The same bound holds for the complementary projection.

Finally, for either the fixed-kernel projection or its complement,
\[
 \frac d{ds}\operatorname{Tr}(Pe^{-t\widetilde H})
 =\operatorname{Tr}(P'e^{-t\widetilde H})
  +\operatorname{Tr}\left(P\frac d{ds}e^{-t\widetilde H}\right).
\]
Hilbert–Schmidt Cauchy–Schwarz gives the second term's absolute value at most \(\sqrt\ell\) times (H45). Therefore
\[
\boxed{
 \left|\frac d{ds}\operatorname{Tr}(Pe^{-t\widetilde H})\right|
 \le\Delta_v\left[
 \frac{\min(\ell,q-\ell)}4+
 \frac{1/e+1/2}{2}\sqrt{\ell q}\right].}
 \tag{H49}
\]
This is exactly intake (23). A stronger version replaces its second term by
\[
 \frac{\sqrt\ell}{2}
 \left(\frac{\sqrt r}{e}+\frac{\sqrt{\min(q,2r)}}2\right).
 \tag{H50}
\]
For the original fixed observation, (H1) identifies this trace with
\(\operatorname{Tr}_B(\Lambda e^{-tM^{\dagger_G}M}L)\).
Thus the bound includes the moving minimum section and both moving metric factors.

These projection formulas require the original subspace \(K\) to be fixed along the source-weight path; they do not require \(MK\subseteq K\). If the observation itself varies, its additional subspace velocity must be added to (H47). An unconstrained velocity has no dimension-only bound.

## 6. Status of the intake equations

The finite-dimensional claims (18)–(23) and (33)–(50) are valid with the complete original metric interpretation. Equation (51) follows from the supplied joint-source action-norm estimate and the original dimension growth; this derivation verifies that implication, not the separate arithmetic norm estimate.

The additional established refinements are (H22), (H31), (H37), and (H46)/(H50). Equation (H23) is an exact finite counterexample to an operator-order strengthening that the intake correctly does not claim. The fixture script and its output distinguish exact rational checks from finite-precision sampling. Neither substitutes for the complete proofs above.
