# Native adjacent source steps have no whole-space word-sign transitions

22 September 2026. Independent derivation NW1–NW18. For every real polynomial word of degree at most half the original quotient dimension, its full current has the same balanced inertia throughout the actual next-source covariance step. The proof uses the original positive real source, every relation of the full root polynomial, and the actual next monic class. A final exact denominator congruence also settles real Möbius transforms of the original multiplication operator. These results concern full-space currents; their exact map to observed currents is retained below.

## 1. Original source and currents

Keep the original fixed simple quartet, period, arithmetic source and physical coordinate:
\[
q=(k+1)^2,\quad k\ge17,\quad k\equiv1\pmod4,\quad
Q(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta],\quad
E=\mathbb C[y]/Q,\quad M[f]=[yf].
\tag{NW1}
\]
Here \(0<\delta<1/2\), \(\gamma>2\). In the real monomial coefficient basis \(1,y,\ldots,y^{q-1}\), \(M\) is real and \(q\) is even. Pairing the roots with indices \(a,k-a\) proves exactly
\[
Q(y)=\prod_{b=0}^k\prod_{a=0}^{(k-1)/2}
\{[y-(2b-k)\gamma]^2+(2a-k)^2\delta^2\}>0
\quad(y\in\mathbb R).
\tag{NW2}
\]
In particular \(Q(0)>0\), and \(\det M=(-1)^qQ(0)=Q(0)>0\). The determinant formula follows from the companion matrix or the characteristic polynomial \(\det(zI-M)=Q(z)\).

Let \(p_j\) be the original real monic orthogonal polynomials for the complete positive arithmetic source \(d\mu\), let \(\omega_j=\|p_j\|_\mu^2>0\), and let \(b_j=[p_j]\) be their coefficient columns in \(E\). Every nonzero polynomial has positive squared source norm. The complete quotient covariance at degree \(N\ge q-1\) is
\[
D_N=G_N^{-1}=\sum_{j=0}^N\frac{b_jb_j^{\mathsf T}}{\omega_j}.
\tag{NW3}
\]
Indeed the matrix with all columns \(b_j/\sqrt{\omega_j}\) is the complete source map. Its kernel consists of all degree-at-most-\(N\) multiples of \(Q\). Minimizing its Euclidean coefficient norm on each fibre gives the inverse covariance \(G_N\), as proved in NV12 of the accompanying complete [native source-step proof](NATIVE_SOURCE_STEP_PROOF.md). Thus no relation or lower source component is removed.

Let \(p\in\mathbb R[y]\) have degree \(d\le q/2\), leading coefficient \(c_d\ne0\), and put \(T=p(M)\). Define the real skew matrix \(A_N=TD_N-D_NT^{\mathsf T}\), the Hermitian dual current \(S_N=iA_N\), and the native addition
\[
u=b_{N+1}/\sqrt{\omega_{N+1}},\quad
D(t)=D_N+tuu^{\mathsf T},\quad G(t)=D(t)^{-1},\quad0\le t\le1.
\]
\[
S(t)=i[TD(t)-D(t)T^{\mathsf T}]
=S_N+it[(Tu)u^{\mathsf T}-u(Tu)^{\mathsf T}].
\tag{NW4}
\]
In particular, the theorem applies to both literal original adjacent paths \(N=q-1\to q\) and \(N=2q-1\to2q\), retaining all four endpoints. The finite proof also holds for every \(N\ge q-1\) for which these same complete source moments are defined.

The source is real, so transpose is the complex adjoint of every displayed real matrix. The original full current in source-metric isometric coordinates is
\[
G(t)^{-1/2}i[G(t)T-T^{\mathsf T}G(t)]G(t)^{-1/2}
=G(t)^{1/2}S(t)G(t)^{1/2}.
\tag{NW5}
\]
This is an invertible congruence of the exact original current; its inertia agrees with that of \(S(t)\). Here inertia means the ordered triple of positive, negative and zero eigenvalue multiplicities. For an invertible congruence this invariance follows by mapping positive and negative subspaces bijectively and applying the maximal dimensions of such subspaces; this is the finite form argument used throughout.

At \(d=0\), \(T\) is scalar and every current is zero. Henceforth \(1\le d\le q/2\).

## 2. The complete boundary block

Expand the exact polynomial product \(p(y)p_j(y)\) in the original monic basis. Its coefficients satisfy
\[
p(y)p_j(y)=\sum_{\ell=0}^{j+d}a_{\ell j}p_\ell(y),\qquad
\frac{a_{\ell j}}{\omega_j}
=\frac{\langle p\,p_j,p_\ell\rangle_\mu}{\omega_j\omega_\ell}
=\frac{a_{j\ell}}{\omega_\ell}.
\]
All coefficients are real. By orthogonality \(a_{\ell j}=0\) for \(|\ell-j|>d\), and \(a_{j+d,j}=c_d\). Substitution in NW3 makes every pair with \(j,\ell\le N\) cancel. The only remaining rows have \(N-d+1\le j\le N\) and \(N+1\le\ell\le N+d\).

Write
\[
V_N=[b_{N-d+1},\ldots,b_N,b_{N+1},\ldots,b_{N+d}],
\quad
H_{rc}=\frac{a_{N+r,N-d+c}}{\omega_{N-d+c}},
\quad1\le r,c\le d.
\]
Then
\[
\boxed{A_N=V_NB_NV_N^{\mathsf T},\qquad
B_N=\begin{pmatrix}0&-H^{\mathsf T}\\H&0\end{pmatrix}.}
\tag{NW6}
\]
The bandwidth gives \(H_{rc}=0\) for \(r>c\), so \(H\) is upper triangular with
\[
H_{rr}=\frac{c_d}{\omega_{N-d+r}},\qquad
\det H=\frac{c_d^d}{\prod_{j=N-d+1}^{N}\omega_j}\ne0.
\tag{NW7}
\]
This proves the finite boundary matrix is nonsingular for every degree cutoff; no generic-position assumption is used.

Here is the required consecutive-class independence. For any \(\ell\ge0\) and \(1\le r\le q\), a relation
\(\sum_{j=\ell}^{\ell+r-1}v_jb_j=0\) gives a polynomial
\(P=\sum v_jp_j=Qh\) with
\(\deg h\le\ell+r-1-q\le\ell-1\). Orthogonality to \(h\) and NW2 yield
\[
0=\langle P,h\rangle_\mu=\int_{\mathbb R}Q(y)|h(y)|^2\,d\mu(y).
\tag{NW8}
\]
The integrand is strictly positive away from the zero set of \(h\); a nonzero \(h\) cannot vanish on the source's support because its squared norm is positive. Thus \(h=0\), \(P=0\), and monic triangularity gives every \(v_j=0\). If the degree bound for \(h\) is negative, divisibility already implies \(P=0\). The proof applies to complex coefficients as well, with the same Hermitian integral.

In particular \(V_N\) has full column rank \(2d\). The matrix \(iB_N\) is congruent to \(i\left(\begin{smallmatrix}0&-I\\I&0\end{smallmatrix}\right)\), by changing its second block with \(H^{-{\mathsf T}}\). That latter Hermitian matrix has \(d\) positive and \(d\) negative eigenvalues. Full-column-rank factorization in NW6 then proves
\[
\boxed{\operatorname{rank}S_N=2d,\quad
\operatorname{ran}S_N=\operatorname{span}\{b_{N-d+1},\ldots,b_{N+d}\},
\quad\operatorname{In}S_N=(d,d,q-2d).}
\tag{NW9}
\]
For rigor concerning the rectangular factor: choose a basis extending the columns of \(V_N\); its inverse transpose converts \(V_NB_NV_N^{\mathsf T}\) into \(B_N\oplus0\). This proves the exact range and the inertia assertion.

## 3. Degrees strictly below half dimension

Suppose \(2d<q\). Then \(u\) lies in \(\operatorname{ran}V_N\), so write \(u=V_Na\) with its unique real coordinate column \(a\). The product \(p(y)p_{N+1}(y)\) involves exactly the possible monic degrees \(N-d+1,\ldots,N+d+1\), with top coefficient \(c_d\ne0\). By NW8 these \(2d+1\) consecutive classes are independent. Hence \(Tu\) lies outside \(\operatorname{ran}V_N\), and
\(F=[V_N,Tu]\) has full column rank \(2d+1\).

Use this actual final vector \(Tu\) as a new coordinate; no orthogonal projection or replacement source direction is introduced. NW4 and NW6 give
\[
\boxed{S(t)=iF
\begin{pmatrix}B_N&-ta\\ta^{\mathsf T}&0\end{pmatrix}
F^{\mathsf T}.}
\tag{NW10}
\]
Since \(B_N^{-1}\) is real skew,
\(a^{\mathsf T}B_N^{-1}a=0\).
Put \(h=tB_N^{-1}a\) and
\(R_t=\left(\begin{smallmatrix}I&h\\0&1\end{smallmatrix}\right)\).
Direct multiplication gives
\[
R_t^{\mathsf T}
\begin{pmatrix}B_N&-ta\\ta^{\mathsf T}&0\end{pmatrix}
R_t=
\begin{pmatrix}B_N&0\\0&0\end{pmatrix}.
\tag{NW11}
\]
Indeed \(B_Nh=ta\), \(h^{\mathsf T}B_N=-ta^{\mathsf T}\), and the last scalar is \(t^2a^{\mathsf T}B_N^{-1}a=0\). Both coordinate maps are explicit and invertible on their indicated ranges. Therefore
\[
\boxed{\operatorname{In}S(t)=(d,d,q-2d)
\quad\hbox{for every real }t,\quad 2d<q.}
\tag{NW12}
\]
The original positive covariance interpretation is used on \(0\le t\le1\); the displayed algebraic inertia identity itself holds for all real \(t\). At no positive interior time does a whole-space current eigenvalue cross zero. The moving support and kernel are retained: in the coefficient matrix of NW10 its one-dimensional kernel is spanned by \((tB_N^{-1}a,1)\), and the original full kernel is the inverse image of this line under \(F^{\mathsf T}\). Thus the nullspace moves even though its dimension and the positive/negative counts stay fixed.

This also verifies the vanishing scalar in a bordered update argument without relying on a pseudoinverse identification. In the original coefficient basis, \(S_N^+\) is purely imaginary and skew under transpose, so \(u^*S_N^+u=0\) for real \(u\); NW11 proves the stronger complete congruence directly.

## 4. Half degree and Pfaffian orientation

Suppose \(2d=q\), so \(V_N\) is square and nonsingular. Its determinant has a fixed positive sign. To prove this without assuming any orientation of a generic source matrix, introduce only for this proof the pushforward measure \(\mu_\varepsilon\) under \(y=\varepsilon x\), for \(\varepsilon>0\). Its monic orthogonal polynomials are
\(p_j^{(\varepsilon)}(y)=\varepsilon^jp_j(y/\varepsilon)\).
Their orthogonality follows by substitution in the integral, and all nonzero polynomials retain positive norm. Keep the original \(Q\) fixed. The positivity proof NW8 therefore shows that the \(q\)-column matrix of their classes at degrees \(\ell,\ldots,\ell+q-1\) is nonsingular for every \(\varepsilon>0\).

Every entry is a polynomial in \(\varepsilon\), and at \(\varepsilon=0\) the columns become the original monomial classes
\([y^\ell],\ldots,[y^{\ell+q-1}]\). This limiting matrix is \(M^\ell\) in the stated monomial coefficient basis. Hence its determinant is \((\det M)^\ell>0\). Continuity and nonvanishing on \(\varepsilon>0\) prove, at \(\varepsilon=1\),
\[
\boxed{\det[b_\ell,\ldots,b_{\ell+q-1}]>0\quad(\ell\ge0).}
\tag{NW13}
\]
The scaled measure is an auxiliary orientation proof with its exact pullback given above; it does not replace any original source metric in NW3–12.

Define the Pfaffian of a real \(2d\)-dimensional skew matrix \(A\) by
\(\Omega_A^d/d!=\operatorname{Pf}(A)e_1\wedge\cdots\wedge e_{2d}\),
where \(\Omega_A=\sum_{i<j}A_{ij}e_i\wedge e_j\). Exterior expansion proves
\(\operatorname{Pf}(VAV^{\mathsf T})=\det V\,\operatorname{Pf}(A)\).
For NW6, taking the \(d\) cross-block terms in that expansion gives
\[
\operatorname{Pf}(B_N)=(-1)^{d(d+1)/2}\det H,\quad
\boxed{\operatorname{Pf}(A_N)=
(-1)^{d(d+1)/2}
\frac{c_d^d\det V_N}{\prod_{j=N-d+1}^N\omega_j}.}
\tag{NW14}
\]
The sign can also be checked at \(d=1\): the first upper entry is \(-H_{11}\), fixing the convention. All factors other than the explicitly displayed fixed sign and \(c_d^d\) are positive. Thus the endpoint Pfaffians at \(N,N+1\) have the same nonzero sign.

The update \(A(t)-A_N=t[(Tu)u^{\mathsf T}-u(Tu)^{\mathsf T}]\) has decomposable two-form. Its exterior square is zero, so the Pfaffian is affine in \(t\). At the actual endpoint, NW3–4 give \(A(1)=A_{N+1}\) for the same polynomial \(p\). Therefore
\[
\boxed{\operatorname{Pf}(A(t))
=(1-t)\operatorname{Pf}(A_N)+t\operatorname{Pf}(A_{N+1})\ne0
\quad(0\le t\le1).}
\tag{NW15}
\]
A skew matrix with a nonzero Pfaffian is nonsingular: a kernel vector, extended to a basis, would make its corresponding row and column zero after congruence and force the top exterior coefficient to vanish. A real skew matrix has opposite pairs of nonzero eigenvalues after multiplication by \(i\): complex conjugation sends an eigenvector of \(iA\) at real eigenvalue \(\lambda\) to an eigenvector at \(-\lambda\). Hence
\[
\boxed{\operatorname{In}S(t)=(q/2,q/2,0)\quad(0\le t\le1).}
\tag{NW16}
\]
No half-degree native whole-space transition occurs. Quantitatively its Pfaffian ratio is exactly
\[
\frac{\operatorname{Pf}(A_{N+1})}{\operatorname{Pf}(A_N)}
=\frac{\det V_{N+1}}{\det V_N}
\frac{\omega_{N-d+1}}{\omega_{N+1}}>0.
\]
This retains the complete consecutive-source determinants instead of replacing the endpoint sign by a continuity guess.

## 5. Exact rational receiver and observed maps

A real Möbius word in the original multiplication operator is settled by an exact denominator congruence. Let real \(a,b,c,d_0\) satisfy \((c,d_0)\ne(0,0)\) and put
\(R=cM+d_0I\). This \(R\) is automatically invertible: if \(c\ne0\), an eigenvalue \(-d_0/c\) would be a real root of \(Q\), excluded by NW2; if \(c=0\), it is a nonzero scalar. Define
\(T_{\rm mob}=(aM+bI)R^{-1}\). Multiplication, using commutativity of both polynomials in \(M\), proves
\[
\boxed{
R\,i[T_{\rm mob}D(t)-D(t)T_{\rm mob}^{\mathsf T}]R^{\mathsf T}
=(ad_0-bc)\,i[MD(t)-D(t)M^{\mathsf T}].
}
\tag{NW17}
\]
Indeed expand
\((aM+bI)D(cM+d_0I)^{\mathsf T}-(cM+d_0I)D(aM+bI)^{\mathsf T}\);
the \(MDM^{\mathsf T}\) and \(D\) terms cancel and the other two have the displayed determinant coefficient.
If \(ad_0-bc\ne0\), NW12 for degree one gives inertia \((1,1,q-2)\) at every native step point; multiplying a balanced inertia by a negative scalar preserves the triple. If \(ad_0-bc=0\), the numerator is a real scalar multiple of \(R\), the word is constant, and its current is zero. This settles this rational family completely. No general rational-function activation assertion is made.

Finally retain the original observation \(\Lambda\), its moving complete covariance metric \(Q_B(t)=(\Lambda D(t)\Lambda^*)^{-1}\), and minimum section \(L(t)=D(t)\Lambda^*Q_B(t)\). The observed word current is exactly
\[
\boxed{
iQ_B(t)\Lambda[TD(t)-D(t)T^{\mathsf T}]\Lambda^*Q_B(t)
=Q_B(t)\Lambda S(t)\Lambda^*Q_B(t).
}
\tag{NW18}
\]
Thus the full current reaches the observed one by the indicated compression and positive metric congruence. NW12 and NW16 do not assign the inertia of that compression or a marked vector's sign. The source-step identities NV1–26 supply their exact separate receiving maps. The no-transition theorem here applies to the entire original source space along the actual native source addition; it does not contradict activation formulas for other source columns.

## 6. Sources and finite verification

The incoming [WS39–44 full affine-activation proof](../whole_space_arrival_029/inputs/Whole_Space_Signs_20260922/COMPLETE_PROOFS.md) was read at lines508–601. It includes singular bordered updates and a positive-source example with observed transitions; it does not evaluate the special native next-monic column proved here. The independent [WD1–20 source and word-sign proof](../whole_space_arrival_029/word_derivation/WORD_SIGNATURE_PROOF.md) was also read, including the attained minimum, complete boundary factor and positivity independence. NW6–9 supplies the corresponding dual-coordinate factor directly; NW10–16 then proves its complete native adjacent-step continuation. Both previously unpublished incoming sources accompany the successor rather than receiving invented public links.

The complete original minimum covariance and source parity used above are proved in the accompanying [NV12–13](NATIVE_SOURCE_STEP_PROOF.md) and publicly in [OCP5–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L90). The original polynomial and complete metric are [RC1–2](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L7). These references preserve the human Gamma/orthogonal-polynomial source citations, including T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, DLMF18.22.8. The positive-source independence, full boundary factorization, native congruence and Pfaffian orientation are proved in full here.

The auxiliary checker retains all source covariance rows in a four-root Gamma quotient and tests degrees one and two, the literal low/high adjacent paths, the exact native skew factorization, the Pfaffian interpolation and its endpoint signs. It separately tests the rectangular congruence and Möbius denominator formula. These are finite algebraic checks, not numerical data for hypothetical zeta zeros or replacements for the original five-orbit observation. The analytic proof above covers the stated original degree range without relying on those finite examples.
