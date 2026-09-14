# Exact variation and sharp spectral bounds for the residue metric product

Date: 2026-09-13. This is a standalone algebraic review of the fixed-space metric variation proposed for the residue curvature intake. It proves the derivative, sharp differential bound, straight-path integral, endpoint bounds, and all corresponding equality conditions. It does not alter the parent TeX, consult primary sources, or rerun earlier calculations.

The formulas in the proposed variation are valid. Two distinctions in their statement matter: the condition number in the exact straight-path integral is the ratio of positive generalized eigenvalues; and equality in a prescribed coefficient family requires the eigenvector alignment proved below. Full positive-metric freedom supplies sharpness, but an arbitrary restricted coefficient family need not supply it.

## 1. Fixed objects, coordinates, and positivity

Let
\[
E=\mathbb C[S]/(\chi),\qquad n=\deg\chi,
\]
and let \(A:E\to E\) be multiplication by the original coordinate \(S\). Retain the original vector \(e=[1]\), the original polynomial \(\chi\), and fixed coordinates on \(E\). Let \(F\subset E\) be a fixed, proper, nonzero \(A\)-invariant subspace, of dimension \(m\). Thus
\[
1\le m\le n-1,\qquad n\ge2.
\]
Choose fixed coordinates on \(F\), and denote the actual inclusion by the full-column-rank matrix
\[
I:\mathbb C^m\longrightarrow\mathbb C^n.
\]
Let \(\ell:E\to\mathbb C\) be a fixed complex-linear functional, and retain its restriction as the row
\[
L=\ell I:\mathbb C^m\longrightarrow\mathbb C.
\]
Assume \(L\ne0\). This is equivalent to the positivity condition on \(d\) in the question; it is not implied merely by \(F\ne0\).

The vector \(e\) does not belong to \(F\). Indeed, if \(e\in F\), invariance would imply \(A^ke\in F\) for every nonnegative integer \(k\). Every element of \(E\) is a polynomial in \(A\) applied to \(e\), so this would imply \(F=E\), contrary to properness. This is the only use of the polynomial-cyclic presentation and \(A\)-invariance in the metric proof. The subsequent formulas retain the resulting fixed \(E,F,I,e,L\).

Let \(M(s)\) be a \(C^1\) path of positive-definite Hermitian matrices in the fixed \(E\)-coordinates. Write
\[
\langle x,y\rangle_M=x^*My,\qquad B=I^*MI.
\]
Since \(I\) has full column rank, \(B\) is positive-definite Hermitian. Define exactly
\[
P=IB^{-1}I^*M,\qquad
r=(1-P)e,\qquad
w=IB^{-1}L^*,
\]
\[
q=r^*Mr,\qquad d=w^*Mw,\qquad c=qd.
\]
Every one of these quantities is \(C^1\) along the path; this follows from \(C^1\) matrix inversion on the invertible matrices.

Direct multiplication gives
\[
P^2=P,\qquad PI=I,\qquad P^*M=MP,\qquad I^*M(1-P)=0.
\]
Thus \(P\) is precisely the \(M\)-orthogonal projection onto \(F\), and
\[
r\perp_M F,\qquad e-r\in F.
\]
Since \(e\notin F\), \(r\ne0\) and \(q>0\).

The vector \(w\) lies in \(F\) and is its exact Riesz representative for the restriction of \(\ell\):
\[
w^*MIx
=LB^{-1}I^*MIx
=Lx
=\ell(Ix)
\qquad(x\in\mathbb C^m).
\]
In particular
\[
d=w^*Mw=LB^{-1}L^*>0,
\]
because \(L\ne0\). Since \(r\perp_M F\) and \(w\in F\),
\[
r^*Mw=0.
\]
Consequently \(c>0\), and \(\log c\) throughout this review is the ordinary real logarithm.

The minimization identity used later is
\[
q(M)=\min_{x\in\mathbb C^m}(e-Ix)^*M(e-Ix).
\tag{1}
\]
To prove it, put \(x_M=B^{-1}I^*Me\). For every \(x\),
\[
e-Ix=r+I(x_M-x),
\]
and the cross terms vanish by \(r\perp_M F\). Hence
\[
(e-Ix)^*M(e-Ix)
=q(M)+(x_M-x)^*B(x_M-x).
\]
The minimizer is unique and equals \(x_M\).

## 2. Exact differentiation

Write \(H=M'(s)\), retaining the derivative in the original coordinates. Since \(e\) and \(I\) are fixed,
\[
r'=-I\frac{d}{ds}\bigl(B^{-1}I^*Me\bigr)\in F.
\]
Therefore \(r'^*Mr=r^*Mr'=0\). Differentiation gives the complete formula
\[
q'=r'^*Mr+r^*Hr+r^*Mr'=r^*Hr.
\tag{2}
\]
There is no missing derivative of the projection: its contribution is the pair of zero cross terms displayed here.

Since \(B'=I^*HI\) and
\[
(B^{-1})'=-B^{-1}B'B^{-1},
\]
the dual-norm derivative is
\[
d'
=-LB^{-1}(I^*HI)B^{-1}L^*
=-w^*Hw.
\tag{3}
\]
Combining (2) and (3) proves
\[
\boxed{
\frac{d}{ds}\log c
=\frac{r^*M'r}{q}-\frac{w^*M'w}{d}.
}
\tag{4}
\]
The minus sign in the second term comes from differentiation of the inverse restricted Gram matrix.

For completeness, all these identities have the expected exact scaling behavior. If \(a>0\), then
\[
P(aM)=P(M),\quad r(aM)=r(M),\quad w(aM)=a^{-1}w(M),
\]
\[
q(aM)=a\,q(M),\quad d(aM)=a^{-1}d(M),\quad c(aM)=c(M).
\tag{5}
\]
Thus a scalar metric variation \(M'=aM\) has zero derivative in (4). No metric or vector has been rescaled in the definition of \(c\); (5) is a proved invariance of that original definition.

## 3. Rank-one projections and the trace formula

Define endomorphisms of the original \(E\) by
\[
R=\frac{rr^*M}{q},\qquad W=\frac{ww^*M}{d}.
\tag{6}
\]
They satisfy
\[
R^2=R,\qquad W^2=W,\qquad R^*M=MR,\qquad W^*M=MW,
\]
and, because \(r^*Mw=0\),
\[
RW=WR=0.
\]
Their ranges are respectively \(\mathbb Cr\) and \(\mathbb Cw\). They are rank-one \(M\)-orthogonal projections.

Let \(D=R-W\). Then
\[
Dr=r,\qquad Dw=-w,
\]
and \(D\) vanishes on \((\mathbb Cr\oplus\mathbb Cw)^{\perp_M}\). Since \(r,w\ne0\) and are orthogonal, this is an orthogonal direct decomposition of \(E\). Consequently \(D\) is \(M\)-self-adjoint with eigenvalues
\[
1\text{ once},\quad -1\text{ once},\quad 0\text{ with multiplicity }n-2.
\tag{7}
\]
For \(n=2\), the zero eigenspace has dimension zero. Also \(\operatorname{Tr}D=0\).

Put
\[
T=M^{-1}H.
\]
This matrix need not be Hermitian for the original Euclidean coordinate inner product, but
\[
T^*M=H=MT,
\]
so it is \(M\)-self-adjoint. The trace of a rank-one operator gives
\[
\operatorname{Tr}(RT)
=\operatorname{Tr}\!\left(\frac{rr^*H}{q}\right)
=\frac{r^*Hr}{q},
\]
and the corresponding identity holds for \(W\). Equation (4) is therefore exactly
\[
\boxed{
\frac{d}{ds}\log c
=\operatorname{Tr}\!\left[
\left(\frac{rr^*M}{q}-\frac{ww^*M}{d}\right)M^{-1}M'
\right].
}
\tag{8}
\]
Every product in (8) is an endomorphism of the original \(E\).

## 4. Sharp differential estimate and its complete equality criterion

Introduce an auxiliary isometry, without replacing the original objects:
\[
J_M:(E,\langle\, ,\,\rangle_M)\longrightarrow
(\mathbb C^n,\langle\, ,\,\rangle_{\mathrm{Euclidean}}),
\qquad J_Mx=M^{1/2}x.
\]
The positive Hermitian square root exists and is invertible. Define
\[
u=\frac{M^{1/2}r}{\sqrt q},\qquad
v=\frac{M^{1/2}w}{\sqrt d},\qquad
K=M^{-1/2}HM^{-1/2}.
\tag{9}
\]
Then \(u,v\) are orthonormal, \(K\) is Hermitian, and
\[
J_MTJ_M^{-1}=K,\qquad
J_MDJ_M^{-1}=uu^*-vv^*.
\]
In particular the eigenvalues of \(T=M^{-1}M'\) are real and equal those of \(K\). Equation (4) becomes
\[
\frac{d}{ds}\log c=u^*Ku-v^*Kv.
\tag{10}
\]

Let
\[
a=\lambda_{\max}(K)=\lambda_{\max}(M^{-1}M'),\qquad
b=\lambda_{\min}(K)=\lambda_{\min}(M^{-1}M').
\]
For every unit vector \(z\), the spectral decomposition of \(K\) gives
\[
b\le z^*Kz\le a.
\]
Indeed, writing \(z\) in an orthonormal eigenbasis expresses \(z^*Kz\) as a weighted average of the eigenvalues, with nonnegative weights summing to one. Applying this to \(u\) and \(v\) proves
\[
\boxed{
\left|\frac{d}{ds}\log c\right|
\le \lambda_{\max}(M^{-1}M')
-\lambda_{\min}(M^{-1}M').
}
\tag{11}
\]

If \(a>b\), positive equality in (11) is equivalent to
\[
u^*Ku=a,\qquad v^*Kv=b.
\]
Necessity follows because
\[
(a-b)-(u^*Ku-v^*Kv)
=(a-u^*Ku)+(v^*Kv-b)
\]
is a sum of two nonnegative terms. The weighted-average proof above shows that \(u^*Ku=a\) holds exactly when \(Ku=au\); similarly \(v^*Kv=b\) holds exactly when \(Kv=bv\). Thus the exact criterion, in the original coordinates, is
\[
\frac{d}{ds}\log c=a-b
\iff
M'r=aMr,\qquad M'w=bMw.
\tag{12}
\]
Negative equality is exactly
\[
\frac{d}{ds}\log c=-(a-b)
\iff
M'r=bMr,\qquad M'w=aMw.
\tag{13}
\]
These statements allow arbitrary multiplicity of the extreme eigenvalues.

If \(a=b\), Hermitian \(K\) equals \(a\,\mathbf1\), so \(M'=aM\). Both sides of (11) vanish. Equality is then automatic, consistently with (5). This includes the zero derivative direction.

### Explicit sharp paths in the full positive-metric cone

Fix a metric \(M_0\) and the corresponding \(r_0,w_0,q_0,d_0,u_0,v_0\). Choose real numbers \(a>b\) and \(h\in[b,a]\), and set
\[
K_0=a\,u_0u_0^*+b\,v_0v_0^*
+h(\mathbf1-u_0u_0^*-v_0v_0^*).
\]
The path
\[
M(s)=M_0^{1/2}\exp(sK_0)M_0^{1/2}
\tag{14}
\]
is positive-definite Hermitian for every real \(s\), begins at \(M_0\), and has
\[
M'(0)=M_0^{1/2}K_0M_0^{1/2}.
\]
Let \(U=M_0^{1/2}F\). Since \(u_0\perp U\) and \(v_0\in U\), the operator \(K_0\), and hence \(\exp(sK_0)\), preserves \(U\) and \(U^\perp\). It follows in the original coordinates that
\[
r(s)=r_0,\qquad w(s)=e^{-bs}w_0,
\]
\[
q(s)=e^{as}q_0,\qquad d(s)=e^{-bs}d_0,\qquad
c(s)=e^{(a-b)s}c(0).
\tag{15}
\]
The first equality follows because \(r_0\) remains orthogonal to \(F\), and \(e-r_0\in F\). The second follows because
\[
(e^{-bs}w_0)^*M(s)z=w_0^*M_0z=\ell(z)
\qquad(z\in F).
\]
The remaining equalities follow from the definitions.

Moreover,
\[
M(s)^{-1}M'(s)=M_0^{-1/2}K_0M_0^{1/2},
\]
whose maximum and minimum eigenvalues are \(a,b\). Thus (11) is saturated with positive sign at every \(s\) along (14). Exchanging \(a,b\) on \(u_0,v_0\) supplies negative saturation. One may take \(a=0\), \(b<0\), and \(h\in[b,0]\) to obtain a Loewner-decreasing sharp path. Hence the estimate remains sharp even among decreasing metrics when the full metric directions are available.

### Exact criterion for coefficient-restricted directions

Suppose a given real parameter space supplies only metrics \(M(\theta)\), and write its actual derivative map at \(\theta_0\) as
\[
dM_{\theta_0}:T_{\theta_0}\Theta\longrightarrow
\operatorname{Herm}(E).
\]
For a tangent vector \(\xi\), substitute \(H=dM_{\theta_0}(\xi)\) in (12) and (13). Those equations are necessary and sufficient for saturation in that particular coefficient direction. No dimension count or freedom in the unrestricted positive cone proves that the image of \(dM_{\theta_0}\) contains such a direction.

There is a concrete counterexample to automatic sharpness in every restricted family using the exact polynomial-cyclic setting. Take
\[
E=\mathbb C[S]/(S^2),\quad
e=[1],\quad F=\operatorname{span}_{\mathbb C}\{[S]\},\quad
I=\begin{pmatrix}0\\1\end{pmatrix},\quad
L=1
\]
in the ordered coordinates \(([1],[S])\). Multiplication by \(S\) preserves this proper nonzero subspace. Let \(\ell([1])=0\), \(\ell([S])=1\), and consider only
\[
M(t)=\begin{pmatrix}1&t\\t&1\end{pmatrix},
\qquad t\in(-1,1)\subset\mathbb R.
\tag{16}
\]
Its eigenvalues are \(1+t,1-t\), so it is positive definite. Directly,
\[
B(t)=1,\quad
r(t)=\begin{pmatrix}1\\-t\end{pmatrix},\quad
w(t)=\begin{pmatrix}0\\1\end{pmatrix},\quad
q(t)=1-t^2,\quad d(t)=1.
\]
Thus \(c(t)=1-t^2\) and
\[
\left.\frac d{dt}\log c(t)\right|_{t=0}=0.
\]
But
\[
M(0)^{-1}M'(0)=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
has eigenvalues \(1,-1\), hence spread \(2\). Every nonzero tangent direction within this one-real-parameter family has zero derivative of \(\log c\) at \(0\), and positive spectral spread. The unrestricted sharpness assertion is proved by (14); this family demonstrates why it cannot be strengthened to automatic sharpness for arbitrary coefficient restrictions.

All derivative results above hold with \(E,F,I,e,L\) fixed. A family that also changes these data is not the stated fixed-object variation; its derivatives contain the corresponding extra terms. The criterion here applies after retaining the specified fixed maps, not after silently differentiating a different object.

## 5. The exact straight-path spectral integral

Let \(G_i,G_j\) be any two positive-definite Hermitian matrices in the same original coordinates. The first part of this section does not require Loewner ordering. Put
\[
C=G_i^{-1/2}G_jG_i^{-1/2},
\]
and denote its ordered positive eigenvalues by
\[
0<\mu_1\le\cdots\le\mu_n,\qquad
\alpha=\mu_1,\qquad \beta=\mu_n.
\]
The matrix \(G_i^{-1}G_j\) is similar to \(C\), so it has these same positive eigenvalues. Define the precise spectral ratio
\[
\kappa_{\mathrm{sp}}(G_i,G_j)=\frac{\beta}{\alpha}.
\tag{17}
\]
This is also the Euclidean spectral condition number of the Hermitian matrix \(C\). It need not equal the Euclidean singular-value condition number of the generally nonnormal matrix \(G_i^{-1}G_j\).

For \(s\in[0,1]\), retain the actual straight segment
\[
M_s=G_i+s(G_j-G_i)
=G_i^{1/2}\bigl[\mathbf1+s(C-\mathbf1)\bigr]G_i^{1/2}.
\tag{18}
\]
Every \(M_s\) is positive definite. Write \(h_\mu(s)=1+s(\mu-1)>0\). Direct matrix multiplication gives the similarity
\[
G_i^{1/2}\bigl[M_s^{-1}(G_j-G_i)\bigr]G_i^{-1/2}
=\bigl[\mathbf1+s(C-\mathbf1)\bigr]^{-1}(C-\mathbf1).
\]
Consequently the eigenvalues of \(M_s^{-1}M_s'\) are exactly
\[
f_s(\mu_k)=\frac{\mu_k-1}{1+s(\mu_k-1)}.
\tag{19}
\]
For fixed \(s\in[0,1]\),
\[
\frac{\partial}{\partial\mu}f_s(\mu)
=\frac1{[1+s(\mu-1)]^2}>0.
\]
Thus its extreme eigenvalues are \(f_s(\beta)\) and \(f_s(\alpha)\), even when eigenvalues repeat. Their spread is
\[
f_s(\beta)-f_s(\alpha)
=\frac{\beta-\alpha}{h_\alpha(s)h_\beta(s)}.
\tag{20}
\]
Integrating exactly,
\[
\begin{aligned}
\int_0^1
\bigl[\lambda_{\max}(M_s^{-1}M_s')
-\lambda_{\min}(M_s^{-1}M_s')\bigr]\,ds
&=
\left[\log h_\beta(s)-\log h_\alpha(s)\right]_{0}^{1}\\
&=\log\beta-\log\alpha\\
&=\log\kappa_{\mathrm{sp}}(G_i,G_j).
\end{aligned}
\tag{21}
\]
All logarithms here have positive real arguments.

The fundamental theorem of calculus, followed by the triangle inequality and (11), yields
\[
\boxed{
\left|\log\frac{c(G_j)}{c(G_i)}\right|
\le\log\kappa_{\mathrm{sp}}(G_i,G_j).
}
\tag{22}
\]
This proves the proposed integrated bound with the original straight path and no omitted constants.

## 6. Independent endpoint proof and exact endpoint equality

The Loewner inequalities
\[
\alpha G_i\le G_j\le\beta G_i
\tag{23}
\]
follow by congruence from \(\alpha\mathbf1\le C\le\beta\mathbf1\).
Let \(r_i,w_i\) denote the original vectors at \(G_i\), and similarly let \(r_j,w_j\) denote the vectors at \(G_j\). From the minimization identity (1),
\[
\alpha q(G_i)\le q(G_j)\le\beta q(G_i).
\tag{24}
\]

The upper equality in (24) holds precisely when
\[
G_jr_i=\beta G_ir_i.
\tag{25}
\]
Indeed,
\[
q(G_j)\le r_i^*G_jr_i\le\beta q(G_i).
\]
Equality of the endpoints forces
\[
r_i^*(\beta G_i-G_j)r_i=0.
\]
A positive-semidefinite Hermitian matrix \(Q\) satisfies \(x^*Qx=0\) exactly when \(Qx=0\): write \(x^*Qx=\|Q^{1/2}x\|^2\). Thus (25) is necessary. Conversely, (25) implies
\[
I^*G_jr_i=\beta I^*G_ir_i=0.
\]
Since \(e-r_i\in F\), uniqueness in (1) gives \(r_j=r_i\), and (25) gives the upper equality.

The lower equality in (24) holds precisely when
\[
G_jr_i=\alpha G_ir_i.
\tag{26}
\]
For necessity, use
\[
q(G_j)=r_j^*G_jr_j
\ge\alpha r_j^*G_ir_j
\ge\alpha q(G_i).
\]
Equality forces \(r_j=r_i\) by uniqueness of the minimizing residual, and then forces (26) by the positive-semidefinite kernel criterion. Conversely, (26) again makes \(r_i\) the \(G_j\)-orthogonal residual and gives the lower equality.

To prove the dual bounds and their equality cases, put
\[
B_i=I^*G_iI,\qquad B_j=I^*G_jI,\qquad
C_F=B_i^{-1/2}B_jB_i^{-1/2},\qquad z=B_i^{-1/2}L^*.
\]
Then
\[
\alpha\mathbf1\le C_F\le\beta\mathbf1,\qquad
d(G_i)=z^*z,\qquad d(G_j)=z^*C_F^{-1}z.
\]
The Hermitian spectral decomposition gives
\[
\frac1\beta\,d(G_i)\le d(G_j)\le\frac1\alpha\,d(G_i).
\tag{27}
\]
The upper equality is equivalent to \(C_Fz=\alpha z\). Writing \(x=B_i^{-1}L^*\) and \(w_i=Ix\), that equality implies
\[
w_i^*(G_j-\alpha G_i)w_i=0.
\]
Since \(G_j-\alpha G_i\) is positive semidefinite, it is equivalent to
\[
G_jw_i=\alpha G_iw_i.
\tag{28}
\]
Conversely, (28) implies \(B_jx=\alpha B_ix=\alpha L^*\), hence \(B_j^{-1}L^*=\alpha^{-1}x\), which proves the upper equality in (27). The lower equality holds precisely when
\[
G_jw_i=\beta G_iw_i,
\tag{29}
\]
by the same argument with \(\beta G_i-G_j\).

Multiplying the positive bounds (24) and (27) gives the stronger unsymmetrized statement
\[
\boxed{
\frac{\alpha}{\beta}\le
\frac{c(G_j)}{c(G_i)}
\le\frac{\beta}{\alpha}.
}
\tag{30}
\]
Since both factors are strictly positive, equality at either end of (30) forces equality in both corresponding factor bounds. Thus, when \(\alpha<\beta\),
\[
\boxed{
\frac{c(G_j)}{c(G_i)}=\frac{\beta}{\alpha}
\iff
G_jr_i=\beta G_ir_i,\quad
G_jw_i=\alpha G_iw_i,
}
\tag{31}
\]
\[
\boxed{
\frac{c(G_j)}{c(G_i)}=\frac{\alpha}{\beta}
\iff
G_jr_i=\alpha G_ir_i,\quad
G_jw_i=\beta G_iw_i.
}
\tag{32}
\]
Equivalently, \(G_i^{1/2}r_i\) and \(G_i^{1/2}w_i\) belong to opposite extreme eigenspaces of \(C\), with the order selecting the sign. This proves necessity and sufficiency for equality in (22), not merely a sufficient construction.

Under the positive equality conditions (31), the entire original-coordinate straight-path solution is
\[
r_s=r_i,\qquad
w_s=h_\alpha(s)^{-1}w_i,
\]
\[
q(M_s)=h_\beta(s)q(G_i),\qquad
d(M_s)=h_\alpha(s)^{-1}d(G_i),
\]
\[
\frac{c(M_s)}{c(G_i)}
=\frac{h_\beta(s)}{h_\alpha(s)}.
\tag{33}
\]
To check the first two equations, use
\[
M_sr_i=h_\beta(s)G_ir_i,\qquad
M_sw_i=h_\alpha(s)G_iw_i
\]
and the defining orthogonality and Riesz conditions from Section 1. The remaining equations then follow directly. Differentiation gives
\[
\frac d{ds}\log c(M_s)
=\frac{\beta-\alpha}{h_\alpha(s)h_\beta(s)},
\]
so the pointwise bound is saturated with constant positive sign along the whole segment. Under (32), interchange \(\alpha,\beta\) in (33), obtaining constant negative sign.

If \(\alpha=\beta\), then \(G_j=\alpha G_i\), and (5) gives \(c(G_j)=c(G_i)\). Both sides of (22) vanish and equality is automatic. In this case the two named extreme eigenspaces coincide with the whole space, rather than being disjoint subspaces.

## 7. The determinant bound for ordered metrics, including equality

Now impose the hypothesis in the question,
\[
G_i\ge G_j>0.
\]
Then
\[
0<\alpha=\mu_1\le\cdots\le\mu_n=\beta\le1.
\]
Because determinant is invariant under similarity and multiplicative under the explicit congruence defining \(C\),
\[
\frac{\det G_j}{\det G_i}=\det C=\prod_{k=1}^n\mu_k.
\tag{34}
\]
Therefore
\[
\begin{aligned}
\log\frac{\det G_i}{\det G_j}
-\log\frac{\beta}{\alpha}
&=-\sum_{k=1}^n\log\mu_k-\log\beta+\log\alpha\\
&=-\sum_{k=2}^{n-1}\log\mu_k-2\log\beta\\
&\ge0.
\end{aligned}
\tag{35}
\]
The sum is empty for \(n=2\). Combining (22) and (35) proves exactly
\[
\boxed{
\left|\log\frac{c(G_j)}{c(G_i)}\right|
\le
\log\frac{\lambda_{\max}(G_i^{-1}G_j)}
{\lambda_{\min}(G_i^{-1}G_j)}
\le
\log\frac{\det G_i}{\det G_j}.
}
\tag{36}
\]

Equality in the second inequality of (36) holds precisely when
\[
\beta=1,\qquad \mu_2=\cdots=\mu_{n-1}=1.
\]
Equivalently, the eigenvalues are \(\alpha,1,\ldots,1\), including the case \(\alpha=1\). By congruence this is equivalent to
\[
\operatorname{rank}(G_i-G_j)\le1.
\tag{37}
\]
If \(G_i\ne G_j\), equality throughout (36) requires (37) together with one of the exact opposite-extreme assignments (31) or (32). If \(G_i=G_j\), all quantities in (36) are zero.

Both signs of the final determinant bound are attained by original-coordinate endpoint pairs. At any fixed \(G_i\), let \(R_i,W_i\) be the projections (6), and choose \(0<\alpha<1\). Define
\[
G_j^{(+)}=G_i\bigl[\mathbf1+(\alpha-1)W_i\bigr],
\qquad
G_j^{(-)}=G_i\bigl[\mathbf1+(\alpha-1)R_i\bigr].
\tag{38}
\]
The products in (38) are Hermitian because \(R_i,W_i\) are \(G_i\)-self-adjoint. Their congruences by \(G_i^{-1/2}\) have eigenvalues \(\alpha,1,\ldots,1\), so both are positive definite and at most \(G_i\). For the plus endpoint, \(r_i\) has generalized eigenvalue \(1\) and \(w_i\) has eigenvalue \(\alpha\); for the minus endpoint the roles reverse. Thus
\[
\frac{c(G_j^{(+)})}{c(G_i)}=\alpha^{-1},\qquad
\frac{c(G_j^{(-)})}{c(G_i)}=\alpha,\qquad
\frac{\det G_i}{\det G_j^{(\pm)}}=\alpha^{-1}.
\tag{39}
\]
This establishes sharpness of the final ordered-metric determinant inequality, as well as sharpness of the intermediate spectral estimate.

## 8. Review disposition

The proposed equations for \(q'\), \(d'\), \((\log c)'\), the trace expression, and the spectrum of the projection difference are proved in (2)–(8). The differential spread bound and its exact extremal-direction criterion are (11)–(13), with a full explicit sharp path in (14)–(15). The exact straight-path integrated spread is (21), and the endpoint inequality with necessary and sufficient equality cases is (30)–(33). The ordered-metric determinant bound, its equality condition, and explicit sharp endpoints are (36)–(39).

The needed wording correction is to state sharpness in the full positive-metric cone, or to require the proved alignment criterion for an actual coefficient direction. Example (16) refutes automatic attainment inside every restricted coefficient family. Also define \(\kappa\) as the generalized spectral ratio (17), and retain the fixed \(E,F,I,e,L\) hypotheses during differentiation.

An independent equality-case audit by a second mathematical worker agreed with the endpoint necessity/sufficiency and the complete straight-path equality formulas. No primary searches, external publication, Lean runs, or checker reruns were performed for this review.

## 9. Exact review of the new source RCX9–RCX24

After the standalone argument above was written, the parent supplied the completed source

    workspace:/work/residue_constituent_extension_20260913.tex

at SHA-256

    9aa18c3f3afc5a69707d785fb3f80303886b69d140fa84812455327240ca8167

The metric block was read completely, including its setup and the explanations after its last display: source lines 116–329, containing (RCX9)–(RCX24). Lines 1–115 were also read to fix the residue functional, the meaning of (RCX3), and the source pullback \(G_N=r_N^*r_N\). This is a read-only mathematical review of that exact source pin. No source edit or test run was performed. The source's dimension \(q\) is this report's \(n\), and its \(\dim F=p\) is this report's \(m\); the scalar \(q_M\) is the report's \(q(M)\).

While the report was being finalized, the parent source advanced to SHA-256

    449d2107fb97369eeb27dfcc0151012da831222a25432cc5b3e1894ff06defc0

The entire metric block was read again at that new pin, lines 116–330 including the trailing blank line. Its setup, formulas, and proofs agree with the block reviewed above; the mathematical acceptance below applies to this new pin as well. A byte-preserving local snapshot is retained at

    workspace:/work/residue_metric_variation_review_evidence_20260913/source_449d2107fb97369eeb27dfcc0151012da831222a25432cc5b3e1894ff06defc0.tex

This snapshot, rather than any subsequently advancing parent filename, fixes the final source receipt.

### Positivity and the original arithmetic pullback

In the source, \(\ell\) is specifically the coefficient of \(S^{q-1}\) in the original monic remainder. Therefore its assertion \(L\ne0\) for a nonzero invariant \(F\) is proved, rather than additionally assumed as it was for the general functional in Section 1 above. Indeed, (RCX3) makes the pairing
\[
\beta(x,y)=\ell(xy)
\]
nondegenerate. If \(\ell|_F=0\), then \(A\)-invariance implies \(\ell(A^jz)=0\) for all \(z\in F\) and \(0\le j<q\). The vectors \(A^je\) form the retained power basis, so \(\beta(x,z)=0\) for every \(x\in E\). Nondegeneracy gives \(z=0\) for every \(z\in F\), contradicting \(F\ne0\). The other assertion \(e\notin F\) is exactly the cyclicity proof in Section 1.

The minimum in (RCX10) is (1). Its supremum formula follows from the actual restricted Riesz representative: putting \(x=M_F^{-1}L^*\), one has
\[
Lv=x^*M_Fv,\qquad
|Lv|^2\le(x^*M_Fx)(v^*M_Fv)=d_M(v^*M_Fv).
\]
Equality holds at \(v=x\ne0\), so the supremum is exactly \(d_M\).

The passage from (RCX10) to (RCX11) is the exact pullback identity
\[
y^*G_Ny=y^*r_N^*r_Ny=\|r_Ny\|^2,
\]
applied separately to \(y=e-Iv\) and \(y=Iv\). It does not discard either the quotient-unit mass or the restricted functional norm.

### Transport under the actual coefficient map

For the invertible map \(C:E'\to E\) in (RCX12), write
\[
\widetilde I=C^{-1}I,\quad
\widetilde e=C^{-1}e,\quad
\widetilde\ell=\ell C,\quad
\widetilde M=C^*MC
\]
to avoid confusing transport with the derivative symbol in Section 2. Then
\[
\widetilde L=\widetilde\ell\,\widetilde I=L,\qquad
\widetilde I^*\widetilde M\widetilde I
=I^*(C^{-1})^*C^*MCC^{-1}I=M_F.
\]
It follows by direct substitution that
\[
\widetilde P=C^{-1}PC,\quad
\widetilde r=C^{-1}r,\quad
\widetilde w=C^{-1}w.
\]
For example,
\[
\widetilde r^*\widetilde M\widetilde r
=r^*(C^{-1})^*C^*MCC^{-1}r=r^*Mr.
\]
The same calculation gives \(\widetilde d=d\), hence the exact covariance statement in (RCX12). Its scalar specialization is (5).

### Differential and relative spectrum

Equations (RCX13)–(RCX17), including their pointwise equality statement, agree exactly with (2)–(13) and the fundamental theorem of calculus in this report. The source makes no claim that every restricted coefficient family has an attaining direction. Its equality statement also covers a scalar \(M^{-1}\dot M\): the greatest and least eigenspaces then both equal \(E\), and both sides of the bound are zero.

For (RCX18)–(RCX20), the source works with \(T=G_i^{-1}G_j\) in the original coordinates. Its factorization
\[
M(s)=G_i(\mathbf1+s(T-\mathbf1))
\]
and the displayed formula for \(M(s)^{-1}\dot M(s)\) are direct matrix identities; the similar Hermitian operator used in Section 5 justifies the real ordered eigenvalues. Thus its \(\theta,\eta\) are respectively the \(\alpha,\beta\) here, with all multiplicities retained.

The additional intermediate steps in (RCX21) are valid:
\[
\log(\eta/\theta)\le-\log\theta
\]
because \(0<\eta\le1\), and
\[
-\log\theta\le\log(V_i/V_j)
\]
because the other positive eigenvalues of \(T\) are at most one, so
\[
\det T=\prod_{k=1}^q\mu_k\le\theta.
\]
Here \(\det T=V_j/V_i\). No singular-value condition number is substituted in that source display.

### Every frame and volume factor in RCX22–RCX24

The source's ideal representation is valid for the fixed invariant subspace. Its inverse image under \(\mathbb C[S]\to E\) is an ideal containing \((\chi)\), hence has its unique monic generator \(g\) with \(g\mid\chi\). Writing \(\chi=gh\) and \(\deg h=p\), the map
\[
\mathbb C[S]/(h)\longrightarrow F,\qquad [a]_h\longmapsto[ga]_\chi
\]
is surjective by the ideal description. If \([ga]_\chi=0\), then \(gh\mid ga\); cancellation of the nonzero polynomial \(g\) in \(\mathbb C[S]\) gives \(h\mid a\), so the map is injective. Thus the frame
\[
J_g=[g,Sg,\ldots,S^{p-1}g]
\]
has independent columns spanning the actual \(F\).

The source keeps its coefficient map
\[
C=(I^*I)^{-1}I^*J_g.
\]
Since the columns of \(J_g\) lie in the image of \(I\), this formula gives exactly \(IC=J_g\). Both \(I\) and \(J_g\) are frames of the same \(p\)-dimensional subspace, so \(C\) is invertible. Consequently
\[
J_g^*MJ_g=C^*M_FC,\qquad
\det(J_g^*MJ_g)=|\det C|^2\det M_F.
\tag{40}
\]
The source retains this determinant factor explicitly.

Because \(g\) is the actual monic divisor of degree \(q-p\), the powers \(S^ag\) have degrees \(q-p+a\le q-1\) for \(0\le a<p\); none is reduced further modulo \(\chi\). Only the final one has degree \(q-1\), with coefficient one. Thus
\[
\ell J_g=LC=e_{p-1}^T.
\tag{41}
\]
This proves the stated last-coordinate identity from the actual coefficient functional.

Let \(B_g=J_g^*MJ_g\), \(J_-=[g,\ldots,S^{p-2}g]\), and \(J_+=[J_g,e]\). The Gram matrix of \(J_+\) is
\[
\begin{pmatrix}
B_g&J_g^*Me\\
e^*MJ_g&e^*Me
\end{pmatrix}.
\]
Multiplication on the left by
\[
\begin{pmatrix}
\mathbf1&0\\
-e^*MJ_gB_g^{-1}&1
\end{pmatrix}
\]
has determinant one and turns this Gram matrix into a block upper-triangular matrix with lower-right entry
\[
e^*Me-e^*MJ_gB_g^{-1}J_g^*Me=q_M.
\]
The last equality holds because \(J_g\) and \(I\) span the same \(F\), hence give the same orthogonal projection. Taking determinants proves
\[
q_M=\frac{\det(J_+^*MJ_+)}{\det(J_g^*MJ_g)}.
\tag{42}
\]

From (40) and (41),
\[
e_{p-1}^TB_g^{-1}e_{p-1}
=LC(C^{-1}M_F^{-1}(C^*)^{-1})C^*L^*
=LM_F^{-1}L^*=d_M.
\]
The last diagonal entry of the inverse matrix is its last principal cofactor divided by its determinant. This follows directly from \(B_g^{-1}=\operatorname{adj}(B_g)/\det B_g\), and the deleted row and column have the same final index, so their cofactor sign is \(+1\). The remaining principal Gram matrix is exactly \(J_-^*MJ_-\). Therefore
\[
d_M=\frac{\det(J_-^*MJ_-)}{\det(J_g^*MJ_g)}.
\tag{43}
\]
For \(p=1\), the remaining matrix is \(0\times0\) with determinant one, giving exactly the same formula.

Equations (42) and (43) prove all three identities (RCX23), including
\[
\mathfrak c_F(M)
=\frac{v_{J_+}(M)v_{J_-}(M)}{v_{J_g}(M)^2}.
\]
All determinants are positive because their nonempty frames have independent columns and \(M>0\); the empty determinant is one. Thus ordinary real logarithms are defined, and taking their ratio between \(G_i\) and \(G_j\) proves (RCX24) without any branch or sign choice. Under \(M\mapsto sM\), their dimensions give respectively \(s^{p+1}\), \(s^{p-1}\), and \(s^{2p}\), whose exponents cancel exactly. This agrees with the separately proved scalar law.

**Disposition of the pinned block:** (RCX9)–(RCX24), including the frame-volume part and its stated pointwise equality condition, are mathematically accepted as written at the SHA above. This review's explicit sharp paths, endpoint equality cases, and counterexample to unrestricted coefficient-family attainment are additional proved material; they are not repairs required by that block.
