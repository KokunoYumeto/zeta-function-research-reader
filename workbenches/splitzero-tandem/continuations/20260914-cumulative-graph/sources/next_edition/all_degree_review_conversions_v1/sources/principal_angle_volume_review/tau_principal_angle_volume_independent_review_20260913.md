# Independent principal-angle calculation for the arithmetic four-volume

13 September 2026. This is a separate written derivation of the proposed canonical-section angle formula and its integrated metric comparison. No sealed source is edited.

## 1. Canonical sections in one original Hilbert space

Fix the original monic polynomial \(\chi\) of degree \(q\ge1\), the original real weight \(k\), and the literal finite polynomial space

\[
\mathcal H=\mathcal P_{2q},\qquad
E=\mathbb C[S]/(\chi),\qquad
J:\mathcal H\longrightarrow E
\tag{PA1}
\]

with its fixed coefficient basis and remainder map. Let \(M(t)>0\) be a continuously differentiable Gram on this common space. All orthogonal projections and norms below use that Gram at the same parameter value. The adjoint in the coefficient formula \(R^*MR\) is the ordinary conjugate transpose in the retained bases; no coefficient basis is changed implicitly.

For \(q-1\le N\le2q\), let \(P_N\) project onto \(\mathcal P_N\), and let \(Q_N\) project onto the original relation space \(\chi\mathcal P_{N-q}\), with \(Q_{q-1}=0\). Since the latter is a subspace of the former, their projections commute and satisfy \(P_NQ_N=Q_NP_N=Q_N\). Therefore

\[
N_N=P_N-Q_N
\tag{PA2}
\]

is exactly the orthogonal projection onto
\(K_N=\mathcal P_N\cap(\chi\mathcal P_{N-q})^\perp\).
The original least-norm remainder section \(R_N:E\to\mathcal P_N\) has \(JR_N=I_E\), image \(K_N\), and positive Gram

\[
G_N=R_N^*MR_N>0.
\tag{PA3}
\]

These assertions follow from the direct orthogonal decomposition of the surjective remainder sequence; its kernel is multiplication by the unchanged monic \(\chi\).

If \(i\le j\), both \(R_i x\) and \(R_jx\) are in \(\mathcal P_j\) and have remainder \(x\). Their difference belongs to \(\chi\mathcal P_{j-q}\), which is orthogonal to \(K_j\). Hence

\[
\boxed{R_j=N_jR_i},\qquad
R_i^*MR_j=G_j,
\qquad
G_i-G_j=(R_i-R_j)^*M(R_i-R_j)\succeq0.
\tag{PA4}
\]

The second identity follows by writing \(R_i=R_j+(R_i-R_j)\); its last summand is orthogonal to \(R_jE\). The same expansion gives the last identity with all cross terms accounted for.

## 2. Exact principal angles and the square-root order

Define the actual isometries

\[
V_i=R_iG_i^{-1/2},\qquad V_j=R_jG_j^{-1/2}.
\tag{PA5}
\]

Their domains have the usual coefficient inner product; their targets carry \(M\). Thus \(V_i^*MV_i=V_j^*MV_j=I\). Their cross-Gram and its two products, in their exact noncommutative orders, are

\[
\begin{aligned}
V_i^*MV_j&=G_i^{-1/2}G_j^{1/2},\\
(V_i^*MV_j)(V_j^*MV_i)
&=G_i^{-1/2}G_jG_i^{-1/2},\\
(V_j^*MV_i)(V_i^*MV_j)
&=G_j^{1/2}G_i^{-1}G_j^{1/2}.
\end{aligned}
\tag{PA6}
\]

The first follows from (PA4), with \(G_jG_j^{-1/2}=G_j^{1/2}\) in the adjacent factors. No commutation between \(G_i\) and \(G_j\) is used.

The singular values of the first matrix in (PA6) are the cosines of the principal angles between \(K_i\) and \(K_j\). This can be seen directly. Choose an orthonormal eigenbasis \(a_\ell\) of \(V_i^*MN_jV_i=G_i^{-1/2}G_jG_i^{-1/2}\), and let its eigenvalues be \(c_\ell^2\). By (PA3)–(PA4), \(0<c_\ell\le1\). Put

\[
x_\ell=V_i a_\ell,\qquad
y_\ell=c_\ell^{-1}N_jx_\ell.
\tag{PA7}
\]

The \(x_\ell\) form an orthonormal basis of \(K_i\). The projection identity gives
\(\langle y_\ell,y_r\rangle=\delta_{\ell r}\) and
\(\langle x_\ell,y_r\rangle=c_r\delta_{\ell r}\).
Since the \(q\) values \(c_\ell\) are positive, the \(y_\ell\) form an orthonormal basis of \(K_j\). These are principal bases. Set \(\theta_\ell=\arccos c_\ell\in[0,\pi/2)\). Consequently

\[
\boxed{\operatorname{spec}(G_i^{-1/2}G_jG_i^{-1/2})
=\{\cos^2\theta_\ell:1\le\ell\le q\}.}
\tag{PA8}
\]

The multiplicity of \(\cos\theta=1\) is exactly \(\dim(K_i\cap K_j)\). Indeed equality \(\|N_jx\|=\|x\|\) for an orthogonal projection is equivalent to \(x\in K_j\); apply this on \(x\in K_i\). The same multiplicity is \(\dim\ker(R_i-R_j)\): a common vector has the same remainder in both sections, and conversely equal section values define a vector in the intersection. Thus all unit cosines are retained, including multiplicities arising from coinciding section subspaces.

Taking the determinant of the actual positive matrix in (PA8) gives

\[
\log\frac{\det G_i}{\det G_j}
=\sum_{\ell=1}^q-\log\cos^2\theta_\ell.
\tag{PA9}
\]

All terms are finite and nonnegative, because the original section Grams are positive definite.

## 3. The two pairs and the forced unit cosine

Use exactly the pairs

\[
(i_1,j_1)=(q-1,2q),\qquad
(i_2,j_2)=(q,2q-1).
\tag{PA10}
\]

For the second pair, both section spaces are contained in

\[
\mathcal L=\mathcal P_{2q-1}\cap(\mathbb C\chi)^\perp,
\qquad \dim\mathcal L=2q-1.
\tag{PA11}
\]

For \(K_q\), this follows from its defining orthogonality to \(\chi\); for \(K_{2q-1}\), its relation space contains \(\chi\), so it has the same orthogonality. The dimension in (PA11) is exact because \(\chi\in\mathcal P_{2q-1}\) is nonzero and its norm is positive. Both section spaces have dimension \(q\). The identity
\(\dim(A\cap B)=\dim A+\dim B-\dim(A+B)\)
therefore gives an intersection of dimension at least one. By (PA8), at least one angle in the second pair has cosine one. For \(q=1\), the second pair is literally \((1,1)\), so its sole angle is zero and the whole pair contributes zero.

The original four-volume is precisely

\[
\begin{aligned}
\mathcal B(t)
&=\log\frac{\det G_{q-1}(t)\det G_q(t)}
                {\det G_{2q-1}(t)\det G_{2q}(t)}\\
&=\sum_{a=1}^2\sum_{\ell=1}^q
          -\log\cos^2\theta_{a,\ell}(t).
\end{aligned}
\tag{PA12}
\]

Remove one of the proved zero contributions from the second pair. There remain exactly \(m=2q-1\) nonnegative slots, with every additional zero slot kept. This removal changes neither the value nor either bound below. It is a pointwise assertion; no differentiability of a chosen angle enumeration at eigenvalue crossings is required.

## 4. Full projection-difference spectrum and derivative estimate

For a positive angle in (PA7), define
\(z_\ell=(y_\ell-c_\ell x_\ell)/\sin\theta_\ell\).
The principal-basis identities show that the \(z_\ell\) are orthonormal and orthogonal to \(K_i\), and that distinct positive-angle two-planes are orthogonal. In the ordered basis \((x_\ell,z_\ell)\), the two projections and their difference have the exact matrices

\[
N_i=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
N_j=\begin{pmatrix}c_\ell^2&c_\ell s_\ell\\c_\ell s_\ell&s_\ell^2\end{pmatrix},
\qquad
N_i-N_j=
\begin{pmatrix}s_\ell^2&-c_\ell s_\ell\\-c_\ell s_\ell&-s_\ell^2\end{pmatrix},
\tag{PA13}
\]

where \(s_\ell=\sin\theta_\ell\). The last matrix has trace zero and determinant \(-s_\ell^2\), hence eigenvalues \(+s_\ell,-s_\ell\). A zero-angle common vector has zero difference, and the orthogonal complement of the two spaces also has zero difference. Thus these are the complete nonzero eigenvalues with multiplicity. In particular

\[
\operatorname{Tr}(N_i-N_j)_+
=\operatorname{Tr}(N_i-N_j)_-
=\sum_{\ell=1}^q\sin\theta_\ell.
\tag{PA14}
\]

Here the positive and negative parts are positive operators, and the latter is the negative of the operator on its negative spectral subspace.

Let \(C=M^{-1}\dot M\), which is self-adjoint for the same \(M\). Let
\(\omega(C)=\lambda_{\max}(C)-\lambda_{\min}(C)\).
For any trace-zero self-adjoint \(D\), subtracting the scalar \(\lambda_{\min}(C)I\) leaves its trace pairing unchanged. The inequalities
\(0\preceq C-\lambda_{\min}(C)I\preceq\omega(C)I\), applied to the two positive parts of \(D\), give

\[
|\operatorname{Tr}(DC)|
\le\omega(C)\operatorname{Tr}D_+
\quad\text{if }\operatorname{Tr}D=0.
\tag{PA15}
\]

To verify the inequality without a commutation assumption, the trace of a product of two positive operators is nonnegative: it equals the trace of their positive conjugation \(A^{1/2}BA^{1/2}\). Hence each of the two positive-part trace terms lies between zero and \(\omega(C)\operatorname{Tr}D_+\), and their difference has the asserted absolute bound.

The differentiability of the canonical section follows from its explicit positive-Gram inverse formula. Because \(JR_N=I\), its derivative is a relation vector. Orthogonality to that relation space cancels the two section-derivative cross terms, giving

\[
\dot G_N=R_N^*\dot M R_N,
\qquad
\frac{d}{dt}\log\det G_N
=\operatorname{Tr}(N_NC),
\qquad N_N=R_NG_N^{-1}R_N^*M.
\tag{PA16}
\]

The last formula is the orthogonal projection onto \(R_NE\), since it is the identity there and annihilates its orthogonal complement. Cyclicity of the finite trace then proves the middle identity.

Using the two pairs (PA10), (PA12), (PA14)–(PA16), and the triangle inequality gives

\[
\boxed{
|\mathcal B'(t)|
\le \omega(C(t))\sum_{a=1}^2\sum_{\ell=1}^q
                  \sin\theta_{a,\ell}(t).
}
\tag{PA17}
\]

This bound does not presume that the two projection differences commute, or that either one commutes with \(C\).

For each of the \(m\) retained slots, set \(b_r=-\log\cos^2\theta_r\ge0\). Then \(\sum b_r=\mathcal B\) and \(\sin\theta_r=f(b_r)\), where

\[
f(b)=\sqrt{1-e^{-b}}.
\tag{PA18}
\]

It is continuous at zero and strictly concave on \((0,\infty)\), because

\[
f''(b)=-\frac{e^{-b}}{2\sqrt{1-e^{-b}}}
        -\frac{e^{-2b}}{4(1-e^{-b})^{3/2}}<0.
\]

Concavity extends to the endpoint by continuity: apply the interior inequality to all arguments increased by a positive number and let that number decrease to zero. Jensen's inequality, which follows by iterating the defining two-point concavity inequality, therefore gives

\[
\sum_{r=1}^m f(b_r)\le m f(\mathcal B/m).
\]

Combining this with (PA17) proves the proposed estimate with its exact constant:

\[
\boxed{
|\mathcal B'|
\le m\sqrt{1-e^{-\mathcal B/m}}\,\omega(M^{-1}\dot M),
\qquad m=2q-1.
}
\tag{PA19}
\]

## 5. Strict positivity for the actual moment Grams

The original arithmetic and Gamma norms have the common vertical coordinate \(S=k/2+iu\) and the form

\[
\langle P,R\rangle_{M(t)}
=\int_{\mathbb R}\overline{P(k/2+iu)}R(k/2+iu)m_t(u)\,du.
\tag{PA20}
\]

The original densities and their convex interpolation have the required finite moments and positive definite polynomial Grams. Write the unchanged polynomial as \(\chi(S)=\sum_{j=0}^q a_jS^j\), retaining its coefficients, and define the exact reflected polynomial

\[
\chi^\#(S)=\sum_{j=0}^q\overline{a_j}(k-S)^j.
\tag{PA21}
\]

On the original vertical line, \(k-S=\overline S\), so \(\chi^\#(S)=\overline{\chi(S)}\). It has degree \(q\), with leading coefficient \((-1)^q\overline{a_q}\); that sign is not removed. Hence \(\chi\chi^\#\in\chi\mathcal P_q\) and

\[
\langle1,\chi\chi^\#\rangle_{M(t)}
=\int|\chi(k/2+iu)|^2m_t(u)\,du
=\|\chi\|_{M(t)}^2>0.
\tag{PA22}
\]

All integrals are within the specified moment degree \(2q\). If the first pair in (PA10) had every cosine equal to one, its two \(q\)-dimensional spaces would coincide. Its first space is exactly \(\mathcal P_{q-1}\), and its second is \((\chi\mathcal P_q)^\perp\). The constant polynomial would then be orthogonal to \(\chi\chi^\#\), contradicting (PA22). Thus at least one angle in the first pair is positive, and

\[
\boxed{\mathcal B(t)>0}
\tag{PA23}
\]

for every actual moment Gram in this path. This proves strict positivity without a presumption about the zero locations or a discarded relation primitive. It also verifies the needed endpoint at \(q=1\), where the second pair contributes exactly zero.

## 6. Integrated arcosh comparison on the actual arithmetic/reference path

For \(b>0\), define

\[
F_m(b)=2\operatorname{arcosh}(e^{b/(2m)}),
\qquad
F_m'(b)=\frac{1}{m\sqrt{1-e^{-b/m}}}.
\tag{PA24}
\]

The derivative is obtained by differentiating the displayed exponential and \(\operatorname{arcosh}\); no rescaling of \(\mathcal B\) or its original mass is performed. By (PA23), the chain rule applies along the entire actual path. Equation (PA19) gives

\[
\left|\frac{d}{dt}F_m(\mathcal B(t))\right|
\le\omega(M(t)^{-1}\dot M(t)).
\tag{PA25}
\]

Now take exactly the convex source-metric interpolation
\(M(t)=(1-t)M_\Gamma+tM_{\rm ar}\), \(0\le t\le1\), inherited from the two actual densities in (PA20). Put

\[
A=M_\Gamma^{-1/2}M_{\rm ar}M_\Gamma^{-1/2}>0,
\qquad 0<\lambda_1\le\cdots\le\lambda_{2q+1},
\qquad \kappa=\lambda_{2q+1}/\lambda_1.
\tag{PA26}
\]

This is the complete common-source relative Gram, not a quotient-metric substitute. Factoring
\(M(t)=M_\Gamma^{1/2}((1-t)I+tA)M_\Gamma^{1/2}\)
shows that \(M(t)^{-1}\dot M(t)\) is similar to
\(((1-t)I+tA)^{-1}(A-I)\). Its eigenvalues are

\[
c_j(t)=\frac{\lambda_j-1}{1+t(\lambda_j-1)}.
\tag{PA27}
\]

Every denominator is positive. For fixed \(t\), the derivative of this scalar expression with respect to \(\lambda\) is \((1+t(\lambda-1))^{-2}>0\), so its largest and smallest values have the same indices as the original \(\lambda_j\). Therefore

\[
\begin{aligned}
\int_0^1\omega(M(t)^{-1}\dot M(t))\,dt
&=\int_0^1\left(
\frac{\lambda_{2q+1}-1}{1+t(\lambda_{2q+1}-1)}
-\frac{\lambda_1-1}{1+t(\lambda_1-1)}\right)dt\\
&=\log\lambda_{2q+1}-\log\lambda_1
=\log\kappa.
\end{aligned}
\tag{PA28}
\]

The identity also includes any \(\lambda_j=1\), whose integrand is zero, and cases in which both extreme eigenvalues are above or below one.

Integrating (PA25) and using (PA28) gives precisely

\[
\boxed{
\left|
2\operatorname{arcosh}\!\left(e^{\mathcal B_{\rm ar}/(2m)}\right)
-2\operatorname{arcosh}\!\left(e^{\mathcal B_\Gamma/(2m)}\right)
\right|
\le\log\kappa,
\qquad m=2q-1.
}
\tag{PA29}
\]

Every endpoint volume is the original four-volume in (PA12). All section angles are strictly below \(\pi/2\) because every finite quotient Gram is positive definite. The forced unit-cosine slot is retained through the exact common-space argument (PA11). For \(q=1\), \(m=1\) and the formula uses the single nontrivial pair. If \(\kappa=1\), the two source Grams differ by one positive scalar; all quotient Grams acquire that same scalar and their four-volume ratio is unchanged, consistently giving zero on both sides of (PA29).

The proposed formulas are accepted. This calculation proves their exact finite metric geometry and their application to the original positive moment interpolation. It supplies no bound on \(\kappa\) beyond its computed source definition, and no extra arithmetic conclusion is assigned to that quantity.
