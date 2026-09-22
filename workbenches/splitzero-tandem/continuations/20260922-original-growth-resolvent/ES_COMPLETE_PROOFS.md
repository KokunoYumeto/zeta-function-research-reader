# Original four-label ES receiver: full spectrum and first corrections

Independent derivation, 22 September 2026. This file treats the ES sections of `relative_growth_arrival_20260922/03_Pasted text.txt` and `angular_strengthening_20260922/01_Pasted text.txt`. The accompanying primary-word resolvent source was read as context; its growing-dimensional RH observation is not identified with this four-label map. The source attribution remains Levent Alpöge's originating announcement, crediting Akhil Mathew and Claude Fable 5, with Tao's exposition credited separately. The following receiver is the later explicit linear extension, not an asserted Jacobian of that originating nonlinear construction.

The parent retains the complete session transcript. The assigned independent calculation is: derive the complete original ES receiver singular asymptotics, family corrections, and relation to the exact supplied inverse column; preserve the original denominators and maps; prove the relation between inverse rates and total volume. No discovery, packaging, publication, or subagent work is undertaken in this derivation.

## ES1. Original roots, chart, signs, and exact inverse

Retain four distinct positive labelled roots \(\ell=(p,a,Y,Z)\), the original sum \(S=p+a+Y+Z\), and
\[
f(x)=\prod_j(x-\ell_j),\quad A=-S^{-1},\quad H=Af,\quad d_j=Af'(\ell_j),\quad \xi_j^2d_j=1.
\tag{ES1}
\]
The source and target coefficient frames are exactly the four labels and the four displayed receiving coordinates. Their Euclidean receiver has columns
\[
o_j=\xi_j(1,-id_j,Ad_j^2+2\ell_jd_j,i(7\ell_j^2d_j-13d_j^2))^{\mathsf T}.
\tag{ES2}
\]
Thus every independent square-root sign is retained. Changing a sign is right multiplication by its diagonal sign isometry and changes the corresponding label coordinate of every inverse and observed vector.

Let \(e_2,e_3\) be the elementary symmetric sums of the literal roots, and put
\[
P_2(x)=x^2+\frac{19S}{7}x+\frac{e_2}{2}-\frac{10S^2}{7},\qquad
\mathfrak h=\sum_j\frac{P_2(\ell_j)}{d_j^2},
\]
\[
R_1(x)=i\left[x^3+\left(\frac{19S^2}{7}+e_2\right)x-\frac{10S^3}{7}+\frac{Se_2}{2}-\frac{3e_3}{4}\right],
\quad R_2(x)=\frac{5S^2-13Sx}{7},\quad R_3(x)=\frac{i(S-4x)}{28},
\quad \mathfrak r_\nu=\sum_jR_\nu(\ell_j)/d_j^2.
\tag{ES3}
\]
On the exact invertibility locus calculated in ES5, the supplied rational expressions are the actual inverse of ES2:
\[
(O^{-1}e_0)_j=\xi_j^{-1}\frac{P_2(\ell_j)/d_j^2}{\mathfrak h},
\qquad
(O^{-1})_{j\nu}=\frac{A\xi_j^{-1}}{d_j^2}
\left[R_\nu(\ell_j)-P_2(\ell_j)\frac{\mathfrak r_\nu}{\mathfrak h}\right],\quad1\le\nu\le3.
\tag{ES4}
\]
Here is a direct derivation, retaining all denominators. For target \(b\), put \(z_j=\xi_j(O^{-1}b)_j\) and \(t_j=d_jz_j\). There is a unique polynomial \(L(x)=l_3x^3+l_2x^2+l_1x+l_0\) with \(t_j=L(\ell_j)/f'(\ell_j)\). The coefficients of the Lagrange identity, or polynomial division by the monic \(f\), give
\[
\sum_j\ell_j^n/f'(\ell_j)=0,0,0,1,S,S^2-e_2\quad(0\le n\le5).
\]
Writing \(U_L=\sum_jL(\ell_j)\), the last three receiver equations become exactly
\[
l_3=ib_1,\quad A^2U_L+2(l_2+Sl_3)=b_2,
\quad7[l_1+Sl_2+(S^2-e_2)l_3]-13AU_L=-ib_3,
\]
\[
U_L=l_3(S^3-3Se_2+3e_3)+l_2(S^2-2e_2)+Sl_1+4l_0.
\]
The first equation fixes \(l_3\); the coefficient determinant in \((l_1,l_0)\) of the other two equations is \((1/S)(52/S)-(4/S^2)20=-28/S^2\ne0\). Hence their homogeneous solution space has dimension one. Substitution verifies that their complete solution is \(L=cP_2+\sum_{\nu=1}^3b_\nu R_\nu\). The remaining first equation is \(A\sum_jL(\ell_j)/d_j^2=b_0\), which determines \(c=(b_0/A-\sum b_\nu\mathfrak r_\nu)/\mathfrak h\) and proves ES4. This is an exact connecting map from the supplied auxiliary polynomial column to the original labelled inverse.

For the determinant put \(\Delta_\ell=\prod_{i<j}(\ell_j-\ell_i)\). Factoring each column by \(d_j\), applying the same polynomial coefficient elimination, and using the Vandermonde determinant gives
\[
\det O=28\epsilon A\left(\prod_jd_j\right)\mathfrak h,
\qquad \epsilon=A^2\Delta_\ell\prod_j\xi_j\in\{1,-1\}.
\tag{ES5}
\]
Indeed \(\prod_jf'(\ell_j)=\Delta_\ell^2\) for four roots, so \(\epsilon^2=1\). Equivalently, before any square-root choices, the determinant of the four unscaled columns in ES2 is \(28A^3\Delta_\ell(\prod d_j)\mathfrak h\). Thus among all distinct positive labelled roots the exact exceptional receiver space is \(\mathfrak h=0\); its complement is precisely the domain of ES4. Below, nonvanishing is proved directly throughout the large-\(w\) regime used by the asymptotics. No unproved global certificate at every smaller integral witness is needed for that calculation.

To verify the determinant coefficient explicitly, interpolate \(R_0(\ell_j)=1/d_j\), writing \(R_0=r_0+r_1x+r_2x^2+r_3x^3\). After factoring the \(d_j\) and cancelling the row constants \((-i)i=1\), the other three row polynomials are \(1\), \(A^2f'+2x\), and \(7x^2-13Af'\). The determinant of their four coefficient rows is
\[
\frac{28}{S^2}r_1+\frac{104}{S}r_2+
\left(64-\frac{14e_2}{S^2}\right)r_3
=28A^2\sum_j\frac{P_2(\ell_j)R_0(\ell_j)}{f'(\ell_j)}
=28A^3\mathfrak h.
\]
The equality uses exactly the Lagrange sums above. Multiplication by the evaluation determinant \(\Delta_\ell\), by \(\prod d_j\), and finally by \(\prod\xi_j\) proves ES5 with its stated sign.

The exceptional space also has exact connecting data. At \(\mathfrak h=0\), the last three receiver rows still have rank three by the coefficient determinant above. Hence \(O\) has rank exactly three, with kernel generated by the nonzero vector \((\xi_j^{-1}P_2(\ell_j)/d_j^2)_j\). Its image is precisely the hyperplane
\[
\{b\in\mathbb C^4:b_0/A-\mathfrak r_1b_1-\mathfrak r_2b_2-\mathfrak r_3b_3=0\}.
\]
The defining cokernel row is nonzero because \(A\ne0\). This follows from the first-row compatibility equation after solving all last-three-row equations. Thus the exact defect determines both kernel and cokernel and is not merely a failed inverse formula.

## ES2. Uniform large-\(w\) exterior spectrum

In the original exterior chart retain
\[
R=4a-p>0,\quad w=p/R,\quad t=a/p=(1+w^{-1})/4,\quad u\ge1,
\]
\[
Y=pw(t+t^2/u),\qquad Z=pw(t+u),\qquad
\frac YZ=\frac tu,\qquad\frac{YZ}{Y+Z}=pwt.
\tag{ES6}
\]
These equalities are literal algebraic identities; integrality remains an additional property of the original witness, not of an arbitrary real chart point. For \(w\ge256\), they imply \(a<p<Y<Z\), \(Y\ge pw/4\), \(Z\ge pw\). Set \(U=Y+Z\), \(\tau=(Z-Y)/U\). Since \(Y/Z=t/u\le257/1024\), one has \(1/2<\tau<1\).

Choose \(\xi_p=i/\sqrt{-d_p}\), \(\xi_a=1/\sqrt{d_a}\), \(\xi_Y=1/\sqrt{d_Y}\), \(\xi_Z=i/\sqrt{-d_Z}\). The exact derivative equations include
\[
-d_p=p^2wt(1-t)\frac{(1-p/Y)(1-p/Z)}{1+(p+a)/U},\quad
d_a=p^2wt(1-t)\frac{(1-a/Y)(1-a/Z)}{1+(p+a)/U},
\]
\[
d_Y=Y^2\tau\frac{(1-p/Y)(1-a/Y)}{1+(p+a)/U},\quad
-d_Z=Z^2\tau\frac{(1-p/Z)(1-a/Z)}{1+(p+a)/U}.
\tag{ES7}
\]
The bounds \(p/Y\le4/w\), \(p/Z\le1/w\), \((p+a)/U\le4/(3w)\) prove, with constants independent of \(u\ge1\),
\[
-d_p,d_a=\frac3{16}p^2w[1+O(w^{-1})],\quad
d_Y=Y^2\tau[1+O(w^{-1})],\quad-d_Z=Z^2\tau[1+O(w^{-1})].
\tag{ES8}
\]
All estimates in this section are uniform for \(p\ge1,u\ge1,w\ge256\); no nearly coincident-tail denominator is hidden in them.

For completeness \(\mathfrak h<0\) on this entire regime. Positivity of the four roots gives \(e_2\le3S^2/8\), while \(p/S\le1/w\). Consequently both core values satisfy \(P_2(p),P_2(a)\le-S^2\). ES7 gives \(|d_p|,d_a\le p^2w/4\), so the core contribution to \(\mathfrak h\) is at most \(-32S^2/(p^4w^2)\). At every root \(|P_2(\ell_j)|\le6S^2\). ES7 gives \(d_Y\ge Y^2/3\), \(-d_Z\ge Z^2/3\), hence the absolute tail contribution is at most
\[
54S^2(Y^{-4}+Z^{-4})\le27648S^2/(p^4w^4).
\]
The ratio of this last bound to the core magnitude is at most \(864/w^2<1\). This proves nonvanishing of ES4–5 directly, without relying on an unexecuted global coefficient certificate.

Define the positive literal-tail quantities
\[
A_3=\sqrt{\tau[Y^6(7-13\tau)^2+Z^6(7+13\tau)^2]},
\]
\[
A_{23}=\tau^2Y^2Z^2U\left(40-\frac{14YZ}{U^2}\right).
\tag{ES9}
\]
The bracket is at least \(73/2\). The complete increasingly numbered by decreasing size singular values are
\[
s_1=A_3[1+O(w^{-1})],\quad s_2=(A_{23}/A_3)[1+O(w^{-1})],
\]
\[
s_3=\sqrt{3/8}\,p\sqrt w[1+O(w^{-1})],\qquad
s_4=\sqrt{32/3}\,(p\sqrt w)^{-1}[1+O(w^{-1})].
\tag{ES10}
\]
Here and below singular values use the original Euclidean label and receiving metrics, until the explicit transport ES33–37 in `ES_FAMILY_CORRECTIONS.md`.

We prove all four rates by the complete exterior maps. The leading tail block in rows 2 and 3 is
\[
\begin{pmatrix}
Y^2\sqrt\tau(2-Y\tau/U)&-iZ^2\sqrt\tau(2+Z\tau/U)\\
iY^3\sqrt\tau(7-13\tau)&Z^3\sqrt\tau(7+13\tau)
\end{pmatrix}.
\tag{ES11}
\]
Its determinant is exactly \(A_{23}\): expanding the two terms reduces the remaining bracket to \(\tau U(40-14YZ/U^2)\). ES8 gives errors bounded entrywise by \(CY^2/w,CZ^2/w,CY^3/w,CZ^3/w\), respectively. The last-row norm is \(A_3[1+O(w^{-1})]\); its Z term is uniformly nonzero even if \(7-13\tau\) vanishes.

Here are the bounds for every omitted exterior coefficient. Core entries in rows 0,1,2,3 have respective sizes at most \(C/(p\sqrt w),Cp\sqrt w,Cp^2\sqrt w,Cp^3w^{3/2}\); tail entries in those rows have respective sizes at most \(C/L,CL,CL^2,CL^3\), for \(L=Y,Z\). Relative to \(A_{23}\ge(73/8)Y^2Z^3\), any other two-column minor is bounded by \(C/w\): for tail columns lowering row 2 costs at most \(C/Y\), and for one core column the largest ratio is bounded by \(C[p^2\sqrt w/Y^2+p^3w^{3/2}/(Y^2Z)]\). Both are at most \(C/w\); two core columns are smaller. The finite number of minors then bounds the entire second exterior map, not only one chosen coefficient.

At exterior rank three the two leading entries, in rows 1,2,3 and columns \((p,Y,Z)\), \((a,Y,Z)\), are
\[
-\frac{\sqrt3}{4}p\sqrt w A_{23}[1+O(w^{-1})],\quad
-\frac{i\sqrt3}{4}p\sqrt w A_{23}[1+O(w^{-1})].
\]
The other terms in either same minor cost at most \(Cp/Y+Cp^2w/(YZ)=O(w^{-1})\) relatively. A triple with two core columns has relative size at most \(Cw^{-3/2}\), and replacing row 1 by row 0 costs at most \(C/(p^2w)\). Thus the leading exterior map has one nonzero row with both displayed entries, giving
\[
\|\wedge^3O\|=\sqrt{3/8}\,p\sqrt w A_{23}[1+O(w^{-1})].
\tag{ES12}
\]
For the full determinant the core rows 0,1 minor equals \((d_a-d_p)/\sqrt{-d_pd_a}=2+O(w^{-1})\). The largest alternative pairing, core rows 0,2 and tail rows 1,3, has relative size at most \(Cp/Y\); core rows 0,3 and tail rows 1,2 cost at most \(Cp^2w/(YZ)\). The remaining pairings cost at most these bounds. Therefore
\[
|\det O|=2A_{23}[1+O(w^{-1})].
\tag{ES13}
\]
The identities \(\|\wedge^jO\|=s_1\cdots s_j\) now prove ES10 with all four singular values retained.

The same calculation, or ES4 with ES7, gives the inverse operator limit
\[
\frac{O^{-1}}{p\sqrt w}=\frac{\sqrt3}{8}(-i,1,0,0)^{\mathsf T}e_0^*+O(w^{-1})
\tag{ES14}
\]
in operator norm, uniformly in the stated regime. To see why all columns are controlled, the cofactor of column zero has the two ES12 leading triples, while every cofactor of column one has norm at most \(CA_{23}/(p\sqrt w)\); columns two and three have at most \(CA_{23}/(p^2\sqrt w)\) and \(CA_{23}/(p^3w^{3/2})\), respectively. Division by ES13 and then by \(p\sqrt w\) makes all these columns \(O(w^{-1})\), uniformly for \(p\ge1\). The leading two zero-column cofactors have the phases in ES14; their exact formula is ES4.

Let \(v_0=2^{-1/2}(-i,1,0,0)^{\mathsf T}\). Rank-one singular perturbation of ES14 and ES10 prove, for every fixed \(\tau_0>0\),
\[
e^{-\tau_0p^2wO^*O}\longrightarrow e^{-(32/3)\tau_0}v_0v_0^*,
\tag{ES15}
\]
uniformly as \(w\to\infty\) in this original chart. The other three exponents diverge because \(p^2w s_3^2\asymp p^4w^2\to\infty\). The four marked labels remain distinct in the limiting projection.


# Original ES family: complete first corrections and observation hierarchy

This is the continuation ES16–37 of `ES_PROOFS.md`, 22 September 2026. Every root, map, branch, and denominator is ES1–7 from that proof.

## ES3. Exact fixed-c integral family and its progression

Fix an integer \(c\ge2\), \(c\equiv2\pmod3\). At primes satisfying \(p\equiv1\pmod{12}\), \(c\mid a=(p+3)/4\), retain
\[
T=pa,\quad Y=(T+c)/3,\quad Z=T(T+c)/(3c).
\tag{ES16}
\]
Since \(p\equiv a\equiv1\pmod3\), \(T+c\equiv0\pmod3\); since \(c\mid T\), both \(Y,Z\) are integers. Direct fractions give \(Y^{-1}+Z^{-1}=3/T\) and \(a^{-1}+3/(pa)=4/p\). Thus this is an existing integral ES witness in the original chart, with \(R=3,w=p/3,u=a^2/c\ge1\) eventually. No occupancy assertion for every prime in a residue class is made.

The explicit choice \(c=29\), \(p\equiv3361\pmod{24360}\) satisfies \(p\equiv1\pmod{840}\), \(p\equiv-3\pmod{116}\), and \(\gcd(3361,24360)=1\). The classical coprime-progression theorem of P. G. Lejeune-Dirichlet gives infinitely many primes in this progression. The retained source is the 1837 paper in Ralf Stephan's English translation, [arXiv:0808.1408v2](https://arxiv.org/abs/0808.1408v2); its opening theorem and translator credit were read directly in the retained TeX. This translation is not described as Dirichlet's original German typesetting. The initial prime \(3361\) gives exactly
\[
(p;a,Y,Z)=(3361;841,942210,91836266490),\quad T=2826601.
\tag{ES17}
\]

## ES4. Full analytic matrix and every first singular correction

Use \(z=1/p\) here, to distinguish the expansion variable from the chart's \(t=a/p\). Define the exact weighted matrix
\[
B(z)=\operatorname{diag}(1,p^{-3},p^{-4},p^{-6})\,O_p\,
\operatorname{diag}(p^{3/2},p^{3/2},1,p^{-6}).
\tag{ES18}
\]
The roots and \(d_j\) are rational functions of \(z\). Their four derivative leading terms are \(-p^3/16,p^3/16,p^4/144,-p^8/(2304c^2)\). Factoring these terms out of the prescribed square roots leaves analytic functions equal to one at zero. Every exponent in ES18 is then integral and nonnegative. Hence \(B\) is analytic at zero, with a convergent local Taylor series for each fixed \(c\).

Direct substitution gives its complete first two coefficients:
\[
B_0=\begin{pmatrix}
4i&4&0&0\\-1/4&-i/4&0&0\\-i/2&1/8&1/72&0\\
13/64&-13i/64&-i/288&5/(27648c^3)
\end{pmatrix},
\]
\[
B_1=\begin{pmatrix}
20i&2&0&0\\5/4&i/8&-i/12&0\\5i/2&5/16&-1/48&0\\
-83/64&53i/128&31i/288&5/(1536c^3)
\end{pmatrix},\qquad B(z)=B_0+zB_1+O_c(z^2).
\tag{ES19}
\]
In particular \(\det B_0=5/(995328c^3)>0\). Its inverse is analytic, and
\[
B(z)^{-1}e_0=z_0+zz_1+O_c(z^2),
\]
\[
z_0=(-i/8,1/8,27/8,1728ic^3/5)^{\mathsf T},\quad
z_1=(-i/2,-19/16,135/16,-50112ic^3/5)^{\mathsf T}.
\tag{ES20}
\]
These are verified by \(B_0z_0=e_0\), \(B_0z_1=-B_1z_0\), giving their exact derivation without an inferred inverse rate. In particular the nonzero entry \((B_1)_{1Y}=-i/12\) and the original Y-coordinate \(27/8\) both enter the two core derivatives.

The exact inverse factorization is
\[
O_p^{-1}=\operatorname{diag}(p^{3/2},p^{3/2},1,p^{-6})B(1/p)^{-1}
\operatorname{diag}(1,p^{-3},p^{-4},p^{-6}).
\tag{ES21}
\]
Thus its first column has all four expansions
\[
(O_p^{-1}e_0)_p=-\frac i8p^{3/2}-\frac i2p^{1/2}+O_c(p^{-1/2}),
\quad (O_p^{-1}e_0)_a=\frac18p^{3/2}-\frac{19}{16}p^{1/2}+O_c(p^{-1/2}),
\]
\[
(O_p^{-1}e_0)_Y=\frac{27}{8}\left(1+\frac{5}{2p}+O_c(p^{-2})\right),
\quad (O_p^{-1}e_0)_Z=\frac{1728ic^3}{5}p^{-6}
\left(1-\frac{29}{p}+O_c(p^{-2})\right).
\tag{ES22}
\]
These expand the exact ES4 column, with the same roots, derivative denominators and square-root choices. They are not a different auxiliary receiver.

Every singular value has its first correction evaluated:
\[
\boxed{\begin{aligned}
s_1(O_p)&=\frac5{27648c^3}p^{12}\left(1+\frac{18}{p}+O_c(p^{-2})\right),\\
s_2(O_p)&=\frac1{72}p^4\left(1-\frac{3}{2p}+O_c(p^{-2})\right),\\
s_3(O_p)&=\frac1{2\sqrt2}p^{3/2}\left(1-\frac{41}{4p}+O_c(p^{-2})\right),\\
s_4(O_p)&=4\sqrt2\,p^{-3/2}\left(1+\frac{11}{4p}+O_c(p^{-2})\right).
\end{aligned}}
\tag{ES23}
\]
The complete determinant, with the retained branches, is
\[
\boxed{\det O_p=\frac5{995328c^3}p^{16}\left(1+\frac9p+O_c(p^{-2})\right).}
\tag{ES24}
\]
We prove the errors as well as the coefficients. The leading entry of \(O_p\) is row 3, column Z, namely \(p^{12}B_{3Z}\); every other entry is at most \(O_c(p^8)\). Thus its norm has the relative first correction 18 by ES19. For exterior rank two, the leading minor is rows 2,3 and columns Y,Z:
\[
p^{16}\det B_{\{2,3\},\{Y,Z\}}
=\frac5{1990656c^3}p^{16}\left(1+\frac{33}{2p}+O_c(p^{-2})\right).
\]
Every other minor is at most \(O_c(p^{15})\). Its squared Frobenius norm is therefore the squared leading minor times \(1+O_c(p^{-2})\); the operator norm lies between that leading modulus and the Frobenius norm. This proves the stated first correction for \(s_1s_2\).

For exterior rank three, both leading minors are in rows 1,2,3 and columns \((p,Y,Z)\), \((a,Y,Z)\), of scale \(p^{35/2}\). Their exact analytic coefficients are the corresponding minors \(M_p(z),M_a(z)\) of \(B\). Expanding ES19 gives
\[
\frac{\left.\frac d{dz}(|M_p(z)|^2+|M_a(z)|^2)\right|_{z=0}}
{2(|M_p(0)|^2+|M_a(0)|^2)}=\frac{25}{4}.
\]
The leading norm is \(5p^{35/2}/(3981312\sqrt2c^3)\). Every other entry is at most \(O_c(p^{16})\), so its squared contribution is relatively \(O_c(p^{-3})\). The norm of the complete leading row is a lower bound, and the Frobenius norm supplies the matching upper bound. Thus the first correction to \(s_1s_2s_3\) is \(25/4\). Finally \(\det O_p=p^{16}\det B(1/p)\), and \(\operatorname{Tr}(B_0^{-1}B_1)=9\). Taking successive exterior ratios gives \(18,33/2-18=-3/2,25/4-33/2=-41/4,9-25/4=11/4\), proving ES23–24.

A second route to the smallest singular value uses \(u_0=(-i,1,0,0)^{\mathsf T}/8\), \(u_1=(-i/2,-19/16,0,0)^{\mathsf T}\). ES21 gives the first normalized inverse column \(u_0+p^{-1}u_1+O_c(p^{-3/2})\); its \(p^{-3/2}\) term is in the orthogonal Y coordinate. The other normalized inverse columns are \(O_c(p^{-3})\). Since \(\|u_0\|^2=1/32\) and \(2\Re(u_0^*u_1)=-11/64\),
\[
p^{-3}\|O_p^{-1}\|^2=\frac1{32}-\frac{11}{64p}+O_c(p^{-2}),\qquad
\boxed{p^3s_4(O_p)^2=32+\frac{176}{p}+O_c(p^{-2}).}
\tag{ES25}
\]

## ES5. Exact slow-vector hierarchy and scalar observations

Let \(v_p\) be the right singular vector of \(O_p\) for \(s_4\), with its a coordinate positive. Put \(v_0=(-i,1,0,0)^{\mathsf T}/\sqrt2\), \(w_0=(i,1,0,0)^{\mathsf T}/\sqrt2\). Then
\[
v_p=v_0-\frac{27}{4p}w_0+\frac{27\sqrt2}{2p^{3/2}}e_Y+O_c(p^{-2}).
\tag{ES26}
\]
Both tail coordinates have stronger relative expansions:
\[
\boxed{e_Y^*v_p=\frac{27\sqrt2}{2}p^{-3/2}\left(1+\frac{21}{4p}+O_c(p^{-2})\right),}
\]
\[
\boxed{e_Z^*v_p=\frac{6912\sqrt2\,ic^3}{5}p^{-15/2}
\left(1-\frac{105}{4p}+O_c(p^{-2})\right).}
\tag{ES27}
\]
To prove relative accuracy, write exactly
\[
p^{-3/2}O_p^{-1}=D(z)B(z)^{-1}E(z),\quad
D(z)=\operatorname{diag}(1,1,z^{3/2},z^{15/2}),\quad
E(z)=\operatorname{diag}(1,z^3,z^4,z^6).
\]
The right Gram of this inverse has a simple leading eigenvalue \(1/32\). Its top eigenvector has coordinates \((1,O_c(z^3),O_c(z^4),O_c(z^6))\), up to scalar normalization: solve the three lower block equations, whose scalar eigenvalue stays separated from zero. Multiplication by \(E\) changes the coefficient vector from \(e_0\) by \(O_c(z^6)\). The left singular vector before normalization is therefore \(D(z)[B(z)^{-1}e_0+O_c(z^6)]\), preserving the powers in each tail coordinate. Its norm is \(\|u_0\|[1-11z/4+O_c(z^2)]\). ES20–22 give ES26 and the relative coefficients \(5/2+11/4=21/4\), \(-29+11/4=-105/4\) in ES27. A tiny component is not inferred from a larger vector error.

For \(\mathcal H_p(\tau)=e^{-\tau p^3O_p^*O_p}\), the three faster directions are \(O_c(e^{-c_1\tau p^6})\), while ES25 supplies the slow exponential. For each fixed nonzero scalar row \(\ell\), the following tests are exhaustive:

| Exact original-label test | Power \(\nu\) | Limit of \(p^\nu\ell\mathcal H_p(\tau)\ell^*\) |
|---|---:|---|
| \(\ell v_0\ne0\) | 0 | \(|\ell v_0|^2e^{-32\tau}\) |
| \(\ell v_0=0\), \(\ell w_0\ne0\) | 2 | \((729/16)|\ell w_0|^2e^{-32\tau}\) |
| \(\ell v_0=\ell w_0=0\), \(\ell e_Y\ne0\) | 3 | \((729/2)|\ell e_Y|^2e^{-32\tau}\) |
| \(\ell v_0=\ell w_0=\ell e_Y=0\) | 15 | \((95551488c^6/25)|\ell e_Z|^2e^{-32\tau}\) |

The vectors \(v_0,w_0\) span exactly the original core coordinates, so no nonzero row is missing. Convergence is locally uniform in \(\tau\in(0,\infty)\), without an assertion at zero time. The two pure tail observations also have evaluated first corrections:
\[
p^3e_Y^*\mathcal H_p(\tau)e_Y
=\frac{729}{2}e^{-32\tau}\left[1+\frac{21/2-176\tau}{p}+O_c(p^{-2})\right],
\]
\[
p^{15}e_Z^*\mathcal H_p(\tau)e_Z
=\frac{95551488c^6}{25}e^{-32\tau}\left[1-\frac{105/2+176\tau}{p}+O_c(p^{-2})\right].
\tag{ES28}
\]
These follow by squaring ES27 and multiplying the exponential from ES25; the faster modes remain below the remainder after either polynomial rescaling.

For the actual two-row observation \(L_{\rm obs}=\left(\begin{smallmatrix}1/\sqrt2&i/\sqrt2&0&0\\0&0&1&0\end{smallmatrix}\right)\), \(D_p=\operatorname{diag}(p,p^{3/2})\), its first row annihilates \(v_0\) and takes value \(i\) on \(w_0\). Hence
\[
D_pL_{\rm obs}\mathcal H_p(\tau)L_{\rm obs}^*D_p
\longrightarrow e^{-32\tau}
\begin{pmatrix}729/16&-729i\sqrt2/8\\729i\sqrt2/8&729/2\end{pmatrix}.
\tag{ES29}
\]
Replacing the core phases by their moduli before applying this observation would destroy its cancellation.

## ES6. Same inverse limits, different complete volume on the same map

For primes \(p\equiv13\pmod{24}\), retain the exact original-chart family
\[
a=(p+3)/4,\quad Y=(p+3)(3p+1)/32,\quad Z=p(3p+1)/4.
\tag{ES30}
\]
Writing \(p=24j+13\) gives \(p+3=8(3j+2)\), \(3p+1=8(9j+5)\), proving integrality. Direct substitution gives \(Y^{-1}+Z^{-1}=12/[p(p+3)]=3/(pa)\). Thus the same ES identity and receiver ES2 apply, with \(R=3,w=p/3,u=2\); the initial witness is \((13;4,20,130)\).

Here \(Y/p^2\to3/32\), \(Z/p^2\to3/4\), \(\tau\to7/9\). Substituting into the literal ES9 quantities gives
\[
s_1=\frac{7\sqrt{55508999}}{8192}p^6[1+O(p^{-1})],\quad
s_2=\frac{2737}{24\sqrt{55508999}}p^4[1+O(p^{-1})],
\]
\[
s_3=\frac1{2\sqrt2}p^{3/2}[1+O(p^{-1})],\quad
s_4=4\sqrt2p^{-3/2}[1+O(p^{-1})],\quad
|\det O_p|=\frac{19159}{98304}p^{10}[1+O(p^{-1})].
\tag{ES31}
\]
Both families have the same limits
\[
p^{-3/2}\|O_p^{-1}\|\to1/(4\sqrt2),\quad
\|\wedge^2O_p^{-1}\|\to1/2,\quad
e^{-\tau p^3O_p^*O_p}\to e^{-32\tau}v_0v_0^*.
\tag{ES32}
\]
Their complete determinants have different powers, \(p^{10}\) and \(p^{16}\). This compares existing integral families under the same receiver; it does not invent an unrelated spectrum. Their exact relation is \(|\det O|=(s_1s_2)/\|\wedge^2O^{-1}\|\): the two inverse limits control \(s_3,s_4\), while the original tail factor \(A_{23}=s_1s_2[1+O(w^{-1})]\) supplies the missing volume.

## ES7. Exact fixed-metric and conductor transport

For fixed positive label metric \(G\) and fixed positive receiving metric \(Q\), the original energy is \(H_{G,Q}=G^{-1}O_p^*QO_p\). Its orthonormal representative is \(\widehat O=Q^{1/2}O_pG^{-1/2}\), with exact inverse \(G^{1/2}O_p^{-1}Q^{-1/2}\). Put \(n_G=u_0^*Gu_0>0\), \(q_Q=e_0^*Q^{-1}e_0>0\). ES21 gives the rank-one inverse limit \(G^{1/2}u_0e_0^*Q^{-1/2}\), whence
\[
p^3\lambda_{\min}(H_{G,Q})\longrightarrow(n_Gq_Q)^{-1}.
\tag{ES33}
\]
Its metric-dependent first correction is
\[
\boxed{p^3\lambda_{\min}(H_{G,Q})
=\frac1{n_Gq_Q}\left[1-\frac{2\Re(u_0^*Gu_1)}{n_Gp}+O_{c,G,Q}(p^{-3/2})\right].}
\tag{ES34}
\]
Indeed the first inverse-column squared G norm is \(n_G+2\Re(u_0^*Gu_1)/p+O(p^{-3/2})\). Other inverse columns enter the weighted target contraction first at order \(p^{-3}\). The simple leading eigenvalue expansion, obtained from its complementary block Schur equation, yields ES34. A \(p^{-3/2}\) term may occur when G has nonzero core–Y entries; the stronger Euclidean remainder is not assigned to arbitrary metrics.

The observed covariance \(\ell e^{-\tau p^3H_{G,Q}}G^{-1}\ell^*\) has the same four powers \(0,2,3,15\), tested successively by \(\ell u_0\), \(\ell u_1\), \(\ell e_Y\), \(\ell e_Z\). Its respective leading numerators are
\[
|\ell u_0|^2,\quad |\ell u_1|^2,\quad |\ell(27e_Y/8)|^2,
\quad |\ell(1728ic^3e_Z/5)|^2,
\tag{ES35}
\]
each divided by \(n_G\) and multiplied by \(e^{-\tau/(n_Gq_Q)}\), after the preceding numerators vanish. For relative last-coordinate accuracy, write the inverse exactly as \(G^{1/2}D(z)B(z)^{-1}E(z)Q^{-1/2}\). Its top left singular vector, returned to label coordinates, is \(D(z)[B(z)^{-1}e_0+O_{G,Q}(z^3)]\), up to normalization: the off-diagonal terms in \(E Q^{-1}E\) first occur at order \(z^3\). The Y and Z coordinate powers therefore stay \(z^{3/2},z^{15/2}\), with the same nonzero leading coefficients. Normalization terms multiply earlier vectors and cancel under the successive annihilation tests. This proves the weighted hierarchy without imposing Euclidean orthogonality after transport.

The attained scalar observation metric is \(Q_\ell=(\ell G^{-1}\ell^*)^{-1}\); multiply the covariance by it to obtain measured scalar heat. On a fixed admitted invertible conductor restriction \(L\), take the actual metric \(Q=L^*Q_\Gamma L\). Then \(q_Q=e_0^*(L^*Q_\Gamma L)^{-1}e_0\) retains the full conductor inverse, Gamma mass, and period data.

For moving metrics or conductor restrictions, the underlying error transport is
\[
\|G^{1/2}(O^{-1}/(p\sqrt w)-a_*e_0^*)Q^{-1/2}\|
\le\sqrt{\lambda_{\max}(G)/\lambda_{\min}(Q)}\,
\|O^{-1}/(p\sqrt w)-a_*e_0^*\|,
\quad a_*=\sqrt3(-i,1,0,0)^{\mathsf T}/8.
\tag{ES36}
\]
Composition by the actual invertible conductor \(L\) has relative leading-operator error bounded by
\[
\frac{\|O^{-1}/(p\sqrt w)-a_*e_0^*\|\,\|L^{-1}\|}
{\|a_*\|\,\|e_0^*L^{-1}\|}.
\tag{ES37}
\]
This denominator is part of the proved connecting map. A conductor approaching a directional resonance need not have a uniform bound here. Neither the growing RH kernel coefficient nor a complex-current phase has been assigned from the ES soft mode.

## Verification

The exact checker derives ES19–20, all exterior first corrections, the complete rational inverse, integral families, and initial witness. Independent 110-digit SVD checks retain both core triples and test the four first singular corrections, soft energy, relative last-label component, and distinct-volume family. Large integer samples used for analytic asymptotics are not asserted to be primes. Source versions, reading coverage, and original/translated source distinctions are recorded in the accompanying ledger.
