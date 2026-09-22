# The complete Gamma-power jet minimum

Independent derivation, 22 September 2026. This proof addresses §§6.1–6.3 of the supplied *The original kernel coefficient*. It proves the complete finite comparison in the original measure and reduces its scalar part to an explicitly displayed diagonal remainder. It assigns no new coefficient to the original arithmetic kernel.

## PJ1. Original measure, mass, cutoffs and coefficient maps

Retain

\[
d\sigma(y)=w(y)\,dy,\qquad
w(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi},\qquad
d\nu_n(y)=|y|^{2n}d\sigma(y),\qquad
d_n=\int_{\mathbb R}d\nu_n.
\tag{PJ1}
\]

Its complete mass is \(d_0=\sqrt{2\pi}\). To verify the scalar, put \(g_a(u)=e^{au-e^u}\), \(a>0\). The substitution \(x=e^u\) gives \(\int g_a(u)e^{itu}\,du=\Gamma(a+it)\). Plancherel and the substitution \(x=e^u\) give

\[
\int_{\mathbb R}|\Gamma(a+it)|^2\frac{dt}{2\pi}
=\int_{\mathbb R}e^{2au-2e^u}\,du=2^{-2a}\Gamma(2a).
\]

The original variable is \(y=2t\), so its measure contributes twice this integral. At \(a=1/4\) this is \(2^{1/2}\Gamma(1/2)=\sqrt{2\pi}\). None of the measures in (PJ1) is divided by its mass.

Let \(\mathcal P_m=\{P\in\mathbb C[y]:\deg P\le m\}\). For integers \(q\ge40\) and \(1\le s\le q/10\), set \(n=q-s\), and define the surjective linear map

\[
J_{q,s}:\mathcal P_m\longrightarrow\mathbb C^s,
\qquad (J_{q,s}P)_j=q^j[y^j]P(y),\quad0\le j<s,
\qquad m\ge s-1.
\tag{PJ2}
\]

The positive Hermitian minimum metric \(H_{n,m}^{(q,s)}\) is specified by

\[
a^*H_{n,m}^{(q,s)}a
=\min\{\|P\|_{\nu_n}^2:P\in\mathcal P_m,\ J_{q,s}P=a\}.
\tag{PJ3}
\]

Existence and uniqueness follow from orthogonal projection onto the finite-dimensional affine fibre; positivity follows because its homogeneous coefficient map is surjective. All coefficients may be complex. The four original power-quotient cutoffs correspond exactly to

\[
\begin{array}{c|cccc}
N&q-1&q&2q-1&2q\\ \hline
m=N-(q-s)&s-1&s&q+s-1&q+s.
\end{array}
\tag{PJ4}
\]

Indeed \(F(y)=y^{q-s}P(y)\) has norm \(\|P\|_{\nu_n}\), and the relation \(F\bmod y^q\) prescribes exactly (PJ2). Multiplication by \(y^{q-s}\) is a bijection between these polynomial fibres and the original power-quotient fibres. This proves the norm correspondence, including the source degree, rather than merely identifying two coefficient lists.

## PJ2. The full Laguerre derivative matrix and inverse moments

The auxiliary comparison measure is

\[
d\lambda_n(y)=|y|^{\alpha}e^{-\theta|y|}\,dy,
\qquad \alpha=2n-\tfrac12,\quad\theta=\pi/2.
\tag{PJ5}
\]

It is a separate explicitly defined measure used to bound (PJ1). On the positive half-line write \(\|\cdot\|_{\alpha,\theta}\) for its norm. The original DLMF equations [18.9.23](https://dlmf.nist.gov/18.9.E23) and [18.9.13](https://dlmf.nist.gov/18.9.E13), read in their original equation TeX, imply

\[
\frac{d}{dz}L_j^{(\alpha)}(z)
=-L_{j-1}^{(\alpha+1)}(z)
=-\sum_{i=0}^{j-1}L_i^{(\alpha)}(z).
\tag{PJ6}
\]

For completeness, the finite expression [DLMF 18.5.12](https://dlmf.nist.gov/18.5.E12) gives the Rodrigues identity by the product rule. Integrating that identity by parts \(j\) times against \(z^i\), with \(i<j\), proves orthogonality; the boundary terms vanish because \(\alpha>-1\) and the differentiated factor is \(z^{j+\alpha}e^{-z}\). The same calculation against the leading term \((-1)^jz^j/j!\) proves

\[
\int_0^\infty L_i^{(\alpha)}(\theta y)L_j^{(\alpha)}(\theta y)
y^\alpha e^{-\theta y}\,dy
=\mathbf1_{i=j}\,h_j,
\quad h_j=\theta^{-\alpha-1}\frac{\Gamma(j+\alpha+1)}{j!}.
\tag{PJ7}
\]

In the orthonormal basis \(L_j^{(\alpha)}(\theta y)/\sqrt{h_j}\), the derivative matrix therefore has, for \(i<j\), the exact entry

\[
D_{ij}=-\theta\sqrt{\frac{j!\Gamma(i+\alpha+1)}{i!\Gamma(j+\alpha+1)}}
=-\theta\prod_{r=i+1}^j\sqrt{\frac r{r+\alpha}}.
\tag{PJ8}
\]

For \(n\ge2\) and degree \(d\le2n+2\), put
\(\rho=(2n+2)/(4n+3/2)\). Then \(\rho\le12/19<16/25\). Hence each absolute row sum and each absolute column sum is at most

\[
\theta\sum_{j\ge1}\rho^{j/2}
=\theta\frac{\sqrt\rho}{1-\sqrt\rho}<4\theta.
\]

The inequality \(\|D\|_2^2\le\|D\|_1\|D\|_\infty\), proved by applying weighted Cauchy–Schwarz in each row and summing, now gives the full, degree-uniform estimate

\[
\|P'\|_{\alpha,\theta}\le4\theta\|P\|_{\alpha,\theta},
\qquad P\in\mathcal P_{2n+2},\ n\ge2.
\tag{PJ9}
\]

The same estimate applies to \(P(-y)\) on the positive half-line, including its derivative sign.

Put \(N=\|P\|_{\alpha,\theta}^2>0\), \(B_1=N^{-1}\int_0^\infty|P|^2y^{\alpha-1}e^{-\theta y}dy\), and \(B_2=N^{-1}\int_0^\infty|P|^2y^{\alpha-2}e^{-\theta y}dy\). Integrating the derivatives of \(|P|^2y^\alpha e^{-\theta y}\) and \(|P|^2y^{\alpha-1}e^{-\theta y}\) gives, with \(L=4\theta\),

\[
\alpha B_1\le\theta+2L,
\qquad
(\alpha-1)B_2\le\theta B_1+2L\sqrt{B_2}.
\tag{PJ10}
\]

The boundary terms vanish at infinity and at zero, since \(\alpha>1\). For \(z=\sqrt{B_2}\), solving the resulting quadratic and using
\(\sqrt{L^2+(1-1/\alpha)\theta(\theta+2L)}\le L+\theta\) yields

\[
\left\|\frac P y\right\|_{\alpha,\theta}
\le\frac{2L+\theta}{\alpha-1}\|P\|_{\alpha,\theta}
\le\frac{8\theta}{n}\|P\|_{\alpha,\theta}.
\tag{PJ11}
\]

Summing the squared inequalities for \(P(y)\) and \(P(-y)\) gives the same estimate in \(\lambda_n\). The rational expression \(P/y\) is integrated with its actual weight; no assertion that it is a polynomial is needed.

The Laguerre recurrence can also be checked coefficient by coefficient in the same finite expression:

\[
zL_j^{(\alpha)}(z)=-(j+1)L_{j+1}^{(\alpha)}(z)
+(2j+\alpha+1)L_j^{(\alpha)}(z)-(j+\alpha)L_{j-1}^{(\alpha)}(z).
\]

In the orthonormal basis its off-diagonal magnitudes are
\(\sqrt{(j+1)(j+\alpha+1)}/\theta\). The row and column sums of the multiplication matrix, including its last raising row, are at most \(20n/\theta\) through source degree \(2n+1\), for \(n\ge2\). For example its entries are bounded by the diagonal \((6n+7/2)/\theta\) and two copies of \(\sqrt{(2n+2)(4n+3/2)}/\theta\); their sum is less than \(20n/\theta\). Thus

\[
\|yP\|_{\lambda_n}\le\frac{20n}{\theta}\|P\|_{\lambda_n},
\qquad\deg P\le2n+1.
\tag{PJ12}
\]

## PJ3. The near-zero Gamma comparison and full multiplication bounds

The original Gamma asymptotic [DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9), read as equation TeX, gives

\[
g(x):=x^{1/2}e^{\theta x}w(x)\longrightarrow\sqrt2
\quad(x\to+\infty).
\]

The positive function \(g\) is continuous on \((0,\infty)\), extends continuously with \(g(0)=0\), and has no zero for \(x>0\). Consequently

\[
A:=\inf_{x\ge1}g(x)>0,\qquad
B:=\sup_{x\ge0}g(x)<\infty.
\tag{PJ13}
\]

In particular a global *pointwise* lower comparison to (PJ5) would be false at zero. The following argument supplies the required whole-polynomial lower comparison. By (PJ11), for \(\deg P\le2n+2\),

\[
\int_{|y|<1}|P|^2d\lambda_n
\le\int\frac{|P|^2}{|y|^2}d\lambda_n
\le\frac{64\theta^2}{n^2}\|P\|_{\lambda_n}^2.
\]

Our range has \(n\ge36>16\theta\), so the last factor is at most \(1/4\). Applying the upper pointwise comparison everywhere and the lower comparison on \(|y|\ge1\) proves

\[
\frac A2\|P\|_{\lambda_n}^2
\le\|P\|_{\nu_n}^2\le B\|P\|_{\lambda_n}^2,
\qquad\deg P\le2n+2.
\tag{PJ14}
\]

The constant polynomial gives the same two bounds between the complete masses \(d_n\) and \(\lambda_n(\mathbb R)\). Define \(\kappa=\sqrt{2B/A}\). The upper pointwise comparison also applies directly to the integrable function \(P/y\). Combining it with (PJ11), (PJ12), and the lower bound in (PJ14), yields

\[
\|P/y\|_{\nu_n}\le\frac{8\theta\kappa}{n}\|P\|_{\nu_n},
\qquad
\|yP\|_{\nu_n}\le\frac{20\kappa n}{\theta}\|P\|_{\nu_n}.
\tag{PJ15}
\]

Cauchy–Schwarz applied to \(P/y\) and \(yP\) supplies the missing lower raising bound. Thus there are fixed \(0<c\le1\le C\) such that

\[
cn\|P\|_{\nu_n}\le\|yP\|_{\nu_n}\le Cn\|P\|_{\nu_n},
\qquad\deg P\le2n+1,
\tag{PJ16}
\]

with the last raising degree included. One may take the smaller of \(1,(8\theta\kappa)^{-1}\) for \(c\) and the larger of \(1,20\kappa/\theta\) for \(C\). These are fixed constants attached to the literal Gamma density, not to \(q,s\) or a coefficient direction.

## PJ4. Root gaps, including the odd zero

Let \(U_j^{[n]}\) be the monic degree-\(j\) polynomial orthogonal for \(\nu_n\), and \(h_j^{[n]}=\|U_j^{[n]}\|_{\nu_n}^2\). The density is positive away from one point, so its polynomial Gram matrices are positive definite. Uniqueness and the even density give
\(U_j^{[n]}(-y)=(-1)^jU_j^{[n]}(y)\).

Under the actual map \(x=y^2\), the pushforward measure is

\[
d\rho_n(x)=\frac{x^{n-1/2}}{2\pi}
|\Gamma(1/4+i\sqrt{x}/2)|^2\,dx,\qquad x>0.
\tag{PJ17}
\]

Indeed the two half-lines each contribute \(dy=dx/(2\sqrt{x})\); both are retained. Thus
\(U_{2m}^{[n]}(y)=R_m(y^2)\), where \(R_m\) is monic orthogonal for \(\rho_n\), and
\(U_{2m+1}^{[n]}(y)=yS_m(y^2)\), where \(S_m\) is monic orthogonal for \(x\,d\rho_n\). These assertions follow by substituting every even test monomial in the original orthogonality identities; odd test monomials vanish by parity.

For any positive measure with all moments and positive polynomial Gram matrices, the zeros of its monic degree-\(m\) orthogonal polynomial are the eigenvalues of multiplication by \(x\) compressed to \(\mathcal P_{m-1}\). To verify this statement, use the orthonormal polynomial basis: multiplication is tridiagonal because \(\langle xp_j,p_i\rangle=\langle p_j,xp_i\rangle=0\) for \(i<j-1\). Its off-diagonal coefficients are positive ratios of leading coefficients. Expansion of the compressed characteristic determinant along its last row gives the identical monic three-term recurrence and the initial determinants \(1\) and \(x-b_0\). Hence the determinants are precisely the monic orthogonal polynomials. A symmetric tridiagonal matrix with all off-diagonal entries nonzero has simple eigenvalues: an eigenvector is determined by its first coordinate, and a zero first coordinate forces every coordinate to vanish. The recurrence, evaluated at consecutive simple zeros, gives strict interlacing by alternating signs and the leading signs at infinity.

For the \(\rho_n\) compression its Rayleigh quotient at a polynomial \(R\) is exactly

\[
\frac{\int x|R(x)|^2d\rho_n}{\int|R(x)|^2d\rho_n}
=\frac{\|yR(y^2)\|_{\nu_n}^2}{\|R(y^2)\|_{\nu_n}^2}.
\]

For the \(x\rho_n\) compression the same quotient is
\(\|y^2R(y^2)\|_{\nu_n}^2/\|yR(y^2)\|_{\nu_n}^2\).
Every polynomial on the right is within the degree range of (PJ16) for all uses below. Therefore all the compressed eigenvalues lie in \([c^2n^2,C^2n^2]\). Consequently every nonzero root of each used \(U_j^{[n]}\) lies in

\[
[-Cn,-cn]\ \cup\ [cn,Cn].
\tag{PJ18}
\]

An odd polynomial has exactly its one additional simple root at zero. It is never included in a product that is divided by a nonzero root. In particular (PJ18) applies to all degrees at most \(2n+2\), since the Rayleigh source polynomial has degree at most \(j-2\).

## PJ5. Low degree: the full coefficient metric

For \(0\le j\le s\), use polynomials monic in the actual scaled coefficient variable \(x=y/q\):

\[
\ell_j(x)=\frac{(-1)^j j!}{(\theta q)^j}L_j^{(\alpha)}(\theta qx).
\]

By (PJ7), their squared norms for the positive half-line, divided only here to express the ratio to that half-line's complete mass, are

\[
\frac{\|\ell_j(y/q)\|_{\alpha,\theta}^2}
{\Gamma(\alpha+1)\theta^{-\alpha-1}}
=\frac{j!(\alpha+1)_j}{(\theta q)^{2j}}.
\tag{PJ19}
\]

Since \(9q/10\le n\le q\) and \(j\le s\le q/10\), every factor \((\alpha+r)/(\theta^2q)\), \(1\le r\le j\), is between two fixed positive constants. The elementary bounds \((j/e)^j\le j!\le j^j\) then give, uniformly for \(0\le j\le s\),

\[
e^{-s\log(C_1q/s)-C_1s}
\le\frac{j!(\alpha+1)_j}{(\theta q)^{2j}}\le e^{C_1s}.
\tag{PJ20}
\]

At \(j=0\) the ratio is exactly one. For the lower bound at \(1\le j\le s\), use monotonicity of \(u\mapsto u\log(C_1q/u)\) on this interval, increasing \(C_1\) if necessary.

The finite Laguerre expansion gives

\[
[x^i]\ell_j(x)
=(-1)^{j-i}\binom ji\frac{(\alpha+i+1)_{j-i}}{(\theta q)^{j-i}}.
\tag{PJ21}
\]

The inverse triangular transformation has exactly the same coefficients without the sign:

\[
x^j=\sum_{i=0}^j\binom ji
\frac{(\alpha+i+1)_{j-i}}{(\theta q)^{j-i}}\ell_i(x).
\tag{PJ22}
\]

To verify (PJ22), substitute (PJ21). In the coefficient at \(x^r\), the product of the two rising factorials is always \((\alpha+r+1)_{j-r}\), and the remaining sum is
\(\binom jr\sum_{i=r}^j(-1)^{i-r}\binom{j-r}{i-r}\), equal to zero for \(r<j\) and one for \(r=j\). All entries in both transformations are at most \(\binom jiC_2^{j-i}\) in absolute value. Their Euclidean operator norms are at most \((s+1)(1+C_2)^s\). Combining (PJ19)–(PJ22) therefore controls the whole coefficient Gram, rather than individual monomial norms.

On the negative half-line the change from \(P(y)\) to \(P(-y)\) is the diagonal unitary coefficient map \(a_j\mapsto(-1)^ja_j\), so the same lower and upper bounds hold there. Summing both halves and using (PJ14), including its constant-polynomial mass comparison, proves the following with a fixed enlarged constant \(C_3\): put

\[
E_0(q,s)=C_3\{s\log(C_3q/s)+s+\log(q+2)\}.
\tag{PJ23}
\]

For every \(P(y)=\sum_{j=0}^{s}b_j(y/q)^j\),

\[
d_ne^{-E_0}\|b\|_2^2\le\|P\|_{\nu_n}^2
\le d_ne^{E_0}\|b\|_2^2.
\tag{PJ24}
\]

At degree \(s-1\), (PJ24) is the desired metric directly. At degree \(s\), every complete fibre has coefficient vector \((a,b_s)\). The lower bound survives because \(\|(a,b_s)\|_2\ge\|a\|_2\); the upper bound follows by selecting \(b_s=0\). Hence the *attained* low metrics obey

\[
d_ne^{-E_0}I\preceq H_{n,s-1}^{(q,s)},\ H_{n,s}^{(q,s)}
\preceq d_ne^{E_0}I.
\tag{PJ25}
\]

## PJ6. The complete high covariance: upper bound

Let \(p_j^{[n]}=U_j^{[n]}/\sqrt{h_j^{[n]}}\), and define

\[
\mathsf K_{n,m}(y,z)=\sum_{j=0}^mp_j^{[n]}(y)\overline{p_j^{[n]}(z)},
\qquad
\mathsf C_{n,M}^{(q,s)}=J_{q,s}J_{q,s}^*.
\tag{PJ26}
\]

The adjoint uses the full \(\nu_n\) polynomial Hilbert space. In an orthonormal basis, \(\mathsf C=\sum_{j=0}^M v_jv_j^*\), where \((v_j)_r=q^r[y^r]p_j^{[n]}\). The minimum is obtained at \(J^*(JJ^*)^{-1}a\), because it has jet \(a\) and is orthogonal to \(\ker J\). This proves the exact identity

\[
\mathsf C_{n,M}^{(q,s)}=(H_{n,M}^{(q,s)})^{-1}.
\tag{PJ27}
\]

Take \(M=q+s-1\) or \(q+s\). Factor an even polynomial by its actual positive roots:

\[
p_{2m}^{[n]}(y)=p_{2m}^{[n]}(0)
\prod_{i=1}^{m}(1-y^2/a_i^2).
\]

By (PJ18), \(a_i\ge cn\), and therefore

\[
\big|q^{2r}[y^{2r}]p_{2m}^{[n]}\big|
\le|p_{2m}^{[n]}(0)|\binom mr(q/(cn))^{2r}.
\tag{PJ28}
\]

For an odd polynomial retain its zero at zero separately:

\[
p_{2m+1}^{[n]}(y)=(p_{2m+1}^{[n]})'(0)y
\prod_{i=1}^{m}(1-y^2/b_i^2),
\]

and the analogous coefficient bound has \(q|(p_{2m+1}^{[n]})'(0)|\) as its initial factor. The squared norm of the derivative evaluation functional on the *whole odd subspace* is bounded using the exact map \(Q\mapsto yQ\):

\[
\sup_{0\ne P\in\mathcal P_M,\ P\text{ odd}}
\frac{|P'(0)|^2}{\|P\|_{\nu_n}^2}
=\sup_{0\ne Q\in\mathcal P_{M-1},\ Q\text{ even}}
\frac{|Q(0)|^2}{\|yQ\|_{\nu_n}^2}
\le\frac{\mathsf K_{n,M}(0,0)}{c^2n^2}.
\tag{PJ29}
\]

The last step is (PJ16) and the reproducing-kernel evaluation norm. Thus, after summing squared coefficients in the orthonormal basis, every even coefficient row is bounded by \(\mathsf K_{n,M}(0,0)\binom{\lfloor M/2\rfloor}{r}^2B_0^{4r}\), and every odd row by an additional fixed factor \(B_0^2\), with \(B_0\ge q/(cn)\) fixed.

For \(1\le r\le s/2\),
\(\binom{\lfloor M/2\rfloor}{r}\le(eM/(2r))^r\).
Together with the \(r=0\) rows and at most \(s\) rows, this proves
\(\operatorname{Tr}\mathsf C\le e^{E_1(q,s)}\mathsf K_{n,M}(0,0)\), where \(E_1\) has the same form as (PJ23). A positive matrix is bounded above by its trace times identity, so

\[
\mathsf C_{n,M}^{(q,s)}
\preceq e^{E_1(q,s)}\mathsf K_{n,M}(0,0)I.
\tag{PJ30}
\]

This controls arbitrary linear combinations of all coefficient directions; no diagonal covariance substitution is made.

## PJ7. The complete high covariance: a right inverse for every jet

Put \(L=M-s\), hence \(L=q-1\) or \(q\), and define the actual kernel polynomial

\[
H(y)=\frac{\mathsf K_{n,L}(y,0)}{\mathsf K_{n,L}(0,0)}.
\tag{PJ31}
\]

Then \(H(0)=1\), \(\deg H\le L\), and
\(\|H\|_{\nu_n}^2=1/\mathsf K_{n,L}(0,0)\). Write \(2m=2\lfloor L/2\rfloor\). The kernel ignores odd polynomials, so \(H\) is even of exact degree \(2m\). Its leading coefficient is nonzero because \(p_{2m}^{[n]}(0)\ne0\), by (PJ18).

There is also a direct verification of its root gap, without presuming a kernel-root theorem. For \(1\le j\le m\), reproduction gives \(\langle H,y^{2j}\rangle_{\nu_n}=0\). Consequently \(H(y)\), written as a polynomial in \(x=y^2\), is a nonzero scalar times the degree-\(m\) orthogonal polynomial for \(x\rho_n\). By the exact compression argument in PJ4 all its positive roots \(b_i\) in the \(y\) coordinate obey \(b_i\ge cn\). Thus

\[
H(qx)=\prod_{i=1}^m(1-q^2x^2/b_i^2),
\qquad
[x^{2r}]\frac1{H(qx)}
\le\binom{m+r-1}{r}B_0^{2r}.
\tag{PJ32}
\]

The second identity uses the finite set of weak compositions of \(r\) into \(m\) nonnegative parts; each term is a product of \(r\) factors at most \(B_0^2\). Odd coefficients vanish. If \(m=0\), the reciprocal is exactly one. The same binomial estimate as in PJ6, now with \(m+r\le Cq\), gives

\[
\sum_{j=0}^{s-1}\left|[x^j]\frac1{H(qx)}\right|
\le\exp\{C_4[s\log(C_4q/s)+s+\log(q+2)]\}.
\tag{PJ33}
\]

For an arbitrary requested vector \(a\in\mathbb C^s\), put \(a(x)=\sum_{j<s}a_jx^j\) and

\[
b(x)=\operatorname{rem}_{x^s}\frac{a(x)}{H(qx)},
\qquad
\mathcal R_{n,M,q,s}a(y)=H(y)b(y/q).
\tag{PJ34}
\]

Here the remainder means the first \(s\) coefficients of the formal Taylor series, well-defined because \(H(0)=1\). Polynomial multiplication shows exactly that
\(H(qx)b(x)\equiv a(x)\pmod{x^s}\). Therefore

\[
J_{q,s}\mathcal R_{n,M,q,s}=I_{\mathbb C^s},
\qquad
\deg\mathcal R_{n,M,q,s}a\le L+s-1=M-1\le M.
\tag{PJ35}
\]

The right inverse is linear in all \(s\) entries. From the convolution estimate and Cauchy–Schwarz,
\(\|b\|_1\le\sqrt{s}\|a\|_2\sum_{j<s}|[x^j]H(qx)^{-1}|\).
Repeated use of the upper half of (PJ16), always at source degree at most \(L+s-2<M\), gives

\[
\|(y/q)^jH\|_{\nu_n}\le(Cn/q)^j\|H\|_{\nu_n}.
\]

Triangle inequality and (PJ33) now give, with \(E_2\) again of the form (PJ23),

\[
\|\mathcal R_{n,M,q,s}a\|_{\nu_n}^2
\le\frac{e^{E_2(q,s)}}{\mathsf K_{n,L}(0,0)}\|a\|_2^2.
\tag{PJ36}
\]

Taking the actual minimum and inverting positive matrices yields

\[
e^{-E_2(q,s)}\mathsf K_{n,M-s}(0,0)I
\preceq\mathsf C_{n,M}^{(q,s)}.
\tag{PJ37}
\]

Combining (PJ30) and (PJ37), and increasing a fixed constant, proves exactly

\[
e^{-E(q,s)}\mathsf K_{n,M-s}(0,0)I
\preceq(H_{n,M}^{(q,s)})^{-1}
\preceq e^{E(q,s)}\mathsf K_{n,M}(0,0)I,
\tag{PJ38}
\]

where
\(E(q,s)=C_5[s\log(C_5q/s)+s+\log(q+2)]\).
The same \(E\) may be chosen in (PJ25).

## PJ8. Changing the power at a fixed degree

The needed comparison is slightly more general than manuscript (6.5), so that it also treats its odd diagonal endpoint. Let \(a\ge36\), \(b=a+\delta\), \(\delta\ge0\), and suppose \(d+\delta\le2a+2\). Applying (PJ16) successively to \(P,yP,\ldots,y^{\delta-1}P\) gives, for every \(P\in\mathcal P_d\),

\[
(ca)^{2\delta}\|P\|_{\nu_a}^2
\le\|P\|_{\nu_b}^2
\le(Ca)^{2\delta}\|P\|_{\nu_a}^2.
\tag{PJ39}
\]

For \(\delta=0\) this is equality. Applying it to the constant polynomial and to the complete evaluation minimum at zero gives respectively

\[
(ca)^{2\delta}d_a\le d_b\le(Ca)^{2\delta}d_a,
\qquad
(Ca)^{-2\delta}\mathsf K_{a,d}(0,0)
\le\mathsf K_{b,d}(0,0)
\le(ca)^{-2\delta}\mathsf K_{a,d}(0,0).
\]

Here evaluation minimum equals \(1/\mathsf K\), by the same adjoint computation as (PJ27). The factors involving \(a\) cancel in the mass-kernel product, proving the exact finite bound

\[
\left|\log[d_a\mathsf K_{a,d}(0,0)]
-\log[d_b\mathsf K_{b,d}(0,0)]\right|
\le2\delta\log(C/c).
\tag{PJ40}
\]

Take \(a=n=q-s\), \(b=d=t\), with \(t=L\) or \(M\). Then \(0\le t-n\le2s\) and
\(d+\delta=2t-n\le q+3s\le1.3q<2n+2\). Every multiplication used is inside its proved degree range. In particular,

\[
\left|\log[d_n\mathsf K_{n,t}(0,0)]
-\log[d_t\mathsf K_{t,t}(0,0)]\right|
\le2(t-n)\log(C/c),\qquad t\in\{M-s,M\}.
\tag{PJ41}
\]

## PJ9. The diagonal Christoffel factor and parity

The original Christoffel–Darboux formula [DLMF 18.2.12](https://dlmf.nist.gov/18.2.E12), read as equation TeX, has its full leading-coefficient factor. For monic polynomials it is

\[
\mathsf K_{n,t}(x,y)=\frac{U_{t+1}^{[n]}(x)U_t^{[n]}(y)-U_t^{[n]}(x)U_{t+1}^{[n]}(y)}{h_t^{[n]}(x-y)}
\tag{PJ42}
\]

for real \(x,y\), extended at coincidence. This identity can also be obtained by multiplying the three-term recurrence at \(x\) and \(y\), subtracting, and telescoping; the coefficient relation is \(h_j/h_{j-1}\), so the denominator is exactly \(h_t\).

For even \(t=2m\), set \(n=t\), and abbreviate \(U_j=U_j^{[t]}\), \(h_t=h_t^{[t]}\). At zero,

\[
d_t\mathsf K_{t,t}(0,0)
=\frac{d_tU_t(0)^2}{h_t}\,
D_t,\qquad D_t=\frac{U_{t+1}'(0)}{U_t(0)}.
\tag{PJ43}
\]

This scalar has a uniform bound, which requires both the root gap and interlacing. Write the positive roots of \(U_t\) as \(a_1<\cdots<a_m\), and those of \(U_{t+1}\), apart from zero, as \(b_1<\cdots<b_m\). Strict interlacing, with the zero at zero retained, gives

\[
0<a_1<b_1<a_2<b_2<\cdots<a_m<b_m.
\]

Their signs at zero are both \((-1)^m\), so

\[
1\le D_t=\prod_{i=1}^m\frac{b_i^2}{a_i^2}
\le\frac{b_m^2}{a_1^2}\le(C/c)^2.
\tag{PJ44}
\]

The middle inequality follows by using \(b_i<a_{i+1}\) for every \(i<m\); it is the complete telescoping product. A separate bound on each ratio would instead allow an erroneous exponentially large factor.

For odd \(t\), parity gives exactly
\(\mathsf K_{t,t}(0,0)=\mathsf K_{t,t-1}(0,0)\). Apply (PJ40) with \(a=t-1\), \(b=t\), \(d=t-1\), \(\delta=1\). It follows that

\[
\left|\log[d_t\mathsf K_{t,t}(0,0)]
-\log[d_{t-1}\mathsf K_{t-1,t-1}(0,0)]\right|
\le2\log(C/c).
\tag{PJ45}
\]

This is the exact map between the odd and preceding even diagonal scalars. It does not drop the power change or replace the degree by a new cutoff.

## PJ10. Explicit scalar remainder and the all-direction conclusion

Retain the existing scalar \(\beta=C_\partial/2\) in the incoming manuscript's (1.7), and define the actual finite numbers

\[
R_t:=\log[d_t\mathsf K_{t,t}(0,0)]-\beta t,
\qquad
\mathcal D(q,s):=\max_{q-1\le t\le q+s}|R_t|.
\tag{PJ46}
\]

No convergence assumption is needed for the following finite estimate. Combine (PJ25), (PJ38), and (PJ41). For either \((l,u)=(q-1,2q-1)\) or \((q,2q)\), put \(M=u-(q-s)\), \(L=M-s\), and retain the original notation \(H^{\mathrm{pow}}_{s,N}=H_{n,N-(q-s)}^{(q,s)}\). For every \(0\ne a\in\mathbb C^s\),

\[
\log[d_n\mathsf K_{n,L}(0,0)]-2E(q,s)
\le\log\frac{a^*H^{\mathrm{pow}}_{s,l}a}{a^*H^{\mathrm{pow}}_{s,u}a}
\le\log[d_n\mathsf K_{n,M}(0,0)]+2E(q,s).
\tag{PJ47}
\]

Since \(|L-q|\le1\), \(|M-q|\le s\), \(M-n\le2s\), this proves

\[
\boxed{
\left|\log\frac{a^*H^{\mathrm{pow}}_{s,l}a}{a^*H^{\mathrm{pow}}_{s,u}a}
-\frac{C_\partial q}{2}\right|
\le2E(q,s)+4s\log(C/c)+|C_\partial|\,(s+1)/2
+\mathcal D(q,s).
}
\tag{PJ48}
\]

Thus the finite non-scalar error is exactly of size
\(O(s\log(Cq/s)+s+\log q)\), and the scalar remainder is explicitly (PJ46). The comparison holds on every coefficient subspace because it was proved for every vector, with no orientation assumption.

The incoming diagonal limit (1.7) states \(R_t/t\to0\). Its precise consequence in (PJ48) is uniform over the displayed finite interval: for any \(\varepsilon>0\), eventually \(|R_t|\le\varepsilon t\) for all \(t\ge q-1\), hence \(\mathcal D(q,s)\le\varepsilon(q+s)\le1.1\varepsilon q\). In particular \(\mathcal D(q,s)=o(q)\). This uses a single convergent scalar sequence and proves the required moving-interval consequence explicitly.

To record exactly what the retained monic and zero-law inputs must feed into this scalar, put

\[
a_0=\log(4/\pi),\qquad
\gamma_j=\sqrt{2\pi}\,j!(1/2)_j,
\]

and let \(\psi(1)\) and \(L\) retain the incoming monic-profile and logarithmic zero-statistic conventions. For even \(t\), define exact remainders

\[
\begin{aligned}
r_d(t)&=\log d_t-[2t\log t+(2a_0-2)t],\\
r_h(t)&=\log h_t^{[t]}-\log\gamma_{2t}-2t\psi(1),\\
r_U(t)&=\log|U_t^{[t]}(0)|-t\log t-\tfrac t2L,\\
r_\gamma(t)&=\log\gamma_{2t}-[4t\log t+(4\log2-4)t].
\end{aligned}
\tag{PJ49}
\]

The mass estimate in (PJ14) and the exact mass of \(\lambda_t\) give
\(\log d_t=\log[2\Gamma(2t+1/2)\theta^{-2t-1/2}]+O(1)\).
The original Gamma asymptotic [DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1), read in equation TeX, then proves \(r_d(t)=O(\log t)\). Also
\(\gamma_{2t}=\sqrt{2\pi}\,(4t)!/4^{2t}\), so the same formula proves \(r_\gamma(t)=O(\log t)\).

Substitution in the exact identity (PJ43) gives, with no unlisted term,

\[
\begin{aligned}
\log[d_t\mathsf K_{t,t}(0,0)]
={}&t[2a_0-2\psi(1)+L+2-4\log2]\\
&+r_d(t)-r_h(t)+2r_U(t)-r_\gamma(t)+\log D_t.
\end{aligned}
\tag{PJ50}
\]

In the retained source conventions the bracket is \(C_\partial/2\). Accordingly the exact even diagonal remainder is

\[
R_t=r_d(t)-r_h(t)+2r_U(t)-r_\gamma(t)+\log D_t,
\qquad 0\le\log D_t\le2\log(C/c).
\tag{PJ51}
\]

For odd \(t\), (PJ45) gives
\(|R_t-R_{t-1}|\le2\log(C/c)+|C_\partial|/2\).
Only \(r_h\) and \(r_U\) in (PJ51) require the monic-profile and zero-law calculations. PJ12–PJ14 prove their exact pure-power versions from the located, read providers and the unchanged Gamma measure. No unlocated tag is treated as evidence that a proof has been read. The finite result (PJ48) displays the complete scalar dependence before those asymptotics are applied.

## PJ11. Audit outcome and human-source use

The claimed large-jet comparison survives this independent derivation. Three compressed steps need the full arguments supplied here: the Gamma lower norm comparison requires removal of the small interval in PJ3; the diagonal Christoffel factor needs the telescoping interlacing product (PJ44); and the odd diagonal passage uses the fixed-degree transport (PJ40), not a silent interchange of degree and weight.

All powers, factors of \(q\), the source mass, both real half-lines, the odd zero, the complete covariance, and the last raising degree are retained. The incoming apparent typesetting corruption at the end of its (6.2) contributes no mathematical term.

Human-source formulas actually used are R. A. Askey and R. Roy, DLMF Chapter 5, equations 5.11.1 and 5.11.9; and T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw, DLMF Chapter 18, equations 18.9.23, 18.9.13, 18.5.12 and 18.2.12. The original equation TeX files are retained beside this proof. Reading coverage is those complete formulas and the source pages' equation identities, not the complete chapters. Their use is recorded in SOURCE_READING_USE_LEDGER.json. The incoming research manuscript is identified separately from those human-source formulas.

The following sections complete the connection to the actual retained providers. The full AP1–AP3 proof was read in the sealed source bank, lines 145674–145931, and the full NG10–NG15 proof at lines 130818–130970. Their source extracts are retained beside this proof, with their exact bank intervals and hashes recorded in the ledger. The needed monic and zero-law claims are proved below using these located providers and their exact dictionaries.

## PJ12. The actual diagonal monic norm, including both integration regions

Let \(t\) be even, \(m=t/2\). The retained [EIQ1–EIQ33 proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/09_INPUT_CUMULATIVE_PROOFS.tex#L4381) defines the unique equilibrium probability \(\mu\) for

\[
V(x)=\pi\sqrt{x}-2\log x,\qquad x>0.
\tag{PJ52}
\]

Its support is \([a,b]=[u^2,v^2]\), with \(0<u<v\),
\(uK(\kappa)=2\), \(vE(\kappa)=4\), and \(\kappa^2=1-u^2/v^2\). Its actual density is

\[
\rho(x)=\frac{\sqrt{(b-x)(x-a)}}{4\pi x}
\int_0^\infty\frac{\sqrt r\,dr}{(x+r)\sqrt{(a+r)(b+r)}}
\quad(a<x<b),
\tag{PJ53}
\]

and zero outside. These are EIQ10–EIQ14 at \((\alpha,\beta)=(2,\pi)\). The integral is bounded on \([a,b]\): its integrand is bounded by a fixed multiple of \(\sqrt r\) for \(0<r\le1\) and \(r^{-3/2}\) for \(r\ge1\). Thus \(\rho\) is bounded, and its logarithmic energy is finite. EIQ16–EIQ23 proves the exact Euler relation and uniqueness,

\[
V(x)-2\int\log|x-z|d\mu(z)=\lambda\quad(a\le x\le b),
\qquad
V(x)-2\int\log|x-z|d\mu(z)\ge\lambda\quad(x>0).
\tag{PJ54}
\]

Let \(I_m\) be the monic degree-\(m\) minimum for the full positive-line weight
\(e^{-mV(x)}x^{-3/4}dx\). The retained AP1 proof specializes exactly to

\[
c_1e^{-m\lambda}\le I_m\le C_1(m+2)^{C_1}e^{-m\lambda}.
\tag{PJ55}
\]

Here is the entire specialization. Let \(\omega\) be the arcsine probability on \([a,b]\), and \(\operatorname{cap}=(b-a)/4\). Its logarithmic potential satisfies
\(\int\log|x-z|d\omega(x)\ge\log\operatorname{cap}\) for every complex \(z\), with equality when \(z\in[a,b]\). To verify this, put \(x=(a+b)/2+(b-a)\cos\vartheta/2\) and factor \(x-z\) into its two reciprocal factors in \(e^{i\vartheta}\). The mean of \(\log|e^{i\vartheta}-w|\) is \(\log\max(1,|w|)\): expand the logarithm for \(|w|<1\), factor out \(w\) for \(|w|>1\), and pass through the integrable logarithm at \(|w|=1\). The two reciprocal factors give the claimed bound and equality.

For a monic \(P\) of degree \(m\), apply this to every one of its complex roots. Jensen's inequality, applied after writing the interval integral against \(\omega\), gives

\[
\log\int_a^b|P|^2e^{-mV}x^{-3/4}dx
\ge2m\log\operatorname{cap}-m\int Vd\omega
+\int\log\frac{x^{-3/4}}{\omega'(x)}d\omega.
\]

The last integral is finite because \(a>0\) and the arcsine endpoint logarithms are integrable. Integrating (PJ54) against \(\omega\) gives
\(\int Vd\omega-2\log\operatorname{cap}=\lambda\); the exchanged logarithms are integrable on the compact interval. This proves the interval-only lower bound in (PJ55). Roots on the interval produce integrable logarithms and may be handled first by adding a positive regularizer in Jensen and then taking its limit.

For the upper bound choose the \(m\) midpoint quantiles \(x_j\in[a,b]\) of \(\mu\), and \(P_m(x)=\prod_{j=1}^m(x-x_j)\). Their empirical distribution function differs from that of \(\mu\) by at most \(1/(2m)\). Fix \(B_*>2b+1\). For \(x\in[0,B_*]\), the function
\(f_x(z)=\log\max(|x-z|,1/m)\) has total variation at most \(C+2\log(m+2)\) on \([a,b]\). Integration by parts against the two distribution functions gives

\[
\left|\sum_{j=1}^mf_x(x_j)-m\int f_xd\mu\right|
\le C+\log(m+2).
\]

If \(M_\rho=\sup\rho\), then
\(0\le\int(f_x-\log|x-z|)d\mu(z)\le2M_\rho/m\), by integrating \(\log((1/m)/r)\) for \(0<r<1/m\). The discrete untruncated sum is at most the truncated sum. Consequently
\(\log|P_m(x)|\le m\int\log|x-z|d\mu(z)+C\log(m+2)\) throughout \([0,B_*]\). The Euler inequality (PJ54) proves

\[
|P_m(x)|^2e^{-mV(x)}x^{-3/4}
\le(m+2)^Ce^{-m\lambda}x^{-3/4}
\quad(0<x\le B_*).
\]

This integrable bound includes the full neighborhood of zero. Increase \(B_*\), if necessary, so that
\(4\log x-\pi\sqrt{x}\le-\lambda-(\pi/2)\sqrt{x}\) for all \(x\ge B_*\). Such a choice exists because \(\log x/\sqrt{x}\to0\). All roots are in \((0,b]\), hence \(|P_m(x)|\le x^m\) on that tail. Its integrand is bounded by
\(e^{-m\lambda}x^{-3/4}e^{-m\pi\sqrt{x}/2}\), whose integral is bounded by a fixed multiple of \(e^{-m\lambda}\) for \(m\ge1\). This proves the full upper estimate in (PJ55).

Now return to the original measure. Parity and monicity give the exact polynomial map

\[
U_t^{[t]}(y)=t^t p_m(y^2/t^2),\qquad p_m\text{ monic of degree }m.
\tag{PJ56}
\]

The map between monic polynomials is bijective. On the whole line, with both half-lines included, it gives

\[
\|U_t^{[t]}\|_{\nu_t}^2
=t^{4t+1}\int_0^\infty x^{t-1/2}|p_m(x)|^2w(t\sqrt{x})\,dx.
\tag{PJ57}
\]

The global Gamma upper envelope from (PJ13), and its lower envelope on \(x\in[a,b]\) when \(t\sqrt a\ge1\), give the scale factor \(t^{4t+1/2}\). The remaining integrand is exactly
\(e^{-mV(x)}x^{-3/4}|p_m(x)|^2\). The upper trial and interval-only lower proof just given therefore show

\[
\log h_t^{[t]}=(4t+\tfrac12)\log t-\tfrac t2\lambda+O(\log(t+2)).
\tag{PJ58}
\]

This is also the precise dictionary to AP2–AP3: its ideal exponent is \(L=t\), its residual monic degree is \(r=t\), its \(h=t/2\), its \(\epsilon=0\), its total source degree is \(n=L+r=2t\), and its profile parameter \(r/L\) equals one. No source parameter is sent to a singular endpoint. AP3's profile identity at this value is

\[
\psi(1)=2-2\log2-\lambda/4.
\tag{PJ59}
\]

Combining (PJ58) with the exact \(\gamma_{2t}\) therefore strengthens the monic remainder in (PJ49) to

\[
r_h(t)=O(\log(t+2)).
\tag{PJ60}
\]

## PJ13. The pure-power zero law and its logarithmic statistic

The complete source used here is [NG10–NG15, including its determinant proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/NATIVE_GAUSSIAN_TRANSFER.tex#L203). Its required pure-power connection is proved below rather than asserted for a different relation. The map is \(q_{\rm NG}=t\), \(n_{\rm NG}=m=t/2\), \(s_{\rm NG}=1\), and its full positive-line measure is now precisely

\[
\eta_t=(y\mapsto y^2/t^2)_*\nu_t,
\quad
d\eta_t(x)=t^{2t+1}x^{t-1/2}w(t\sqrt{x})\,dx.
\tag{PJ61}
\]

The source's root-product bound specializes to the identity
\(|(t\sqrt{x})^t|^2=t^{2t}x^t\); its root-radius error is zero. This is a new application to the already specified power measure, not an equality between the original arithmetic relation \(Q_k\) and \(y^t\).

Let \(D_m(\zeta)\) denote the determinant of the monomial Gram matrix through degree \(m-1\) in a positive measure \(\zeta\). Expanding two determinants by permutations and integrating term by term proves the Vandermonde identity

\[
D_m(\zeta)=\frac1{m!}\int_{(0,\infty)^m}
\prod_{i<j}(x_i-x_j)^2\prod_{i=1}^md\zeta(x_i).
\tag{PJ62}
\]

Fix \(A_*>0\), put \(\phi(x)=\log(A_*+x)\), and write

\[
f_t(z)=\log D_m((A_*+x)^z\eta_t),\qquad
F(\tau)=\sup_{\pi}\left\{\iint\log|x-y|d\pi(x)d\pi(y)
-\int Vd\pi+\tau\int\phi d\pi\right\}.
\tag{PJ63}
\]

The supremum is over probabilities on \((0,\infty)\), and the extended value is defined by the bounded-above energy kernel. All integrals defining \(f_t(z)\) are finite for real \(z\): \(\phi\) is bounded near zero and grows logarithmically at infinity. Let \(\kappa_t=t^{2t+1/2}\). We prove the two exact asymptotic directions used by the source:

\[
\limsup_{t\to\infty,\,t\ {\rm even}}
\frac{f_t(m\tau)-m\log\kappa_t}{m^2}\le F(\tau),
\qquad
\liminf\frac{f_t(0)-m\log\kappa_t}{m^2}\ge F(0).
\tag{PJ64}
\]

For the upper bound the Gamma envelope in (PJ13) gives everywhere
\(d\eta_t\le B\kappa_t e^{-mV(x)}x^{-3/4}dx\).
Use the probability
\(d\omega_0=(2\sqrt\pi)^{-1}x^{-3/4}e^{-\sqrt{x}}dx\); its mass is one by \(u=\sqrt x\). For \(\tau\) in a fixed small interval put \(Q_\tau=V-\tau\phi\) and
\(K_\tau(x,y)=\log|x-y|-(Q_\tau(x)+Q_\tau(y))/2\).
The exponent in the Vandermonde integral is exactly

\[
\sum_{i\ne j}K_\tau(x_i,x_j)
+\sum_i(\sqrt{x_i}-Q_\tau(x_i)).
\]

The last summand is bounded above uniformly in \(x_i\) and in this \(\tau\)-interval: it tends to minus infinity at both ends because \(\pi>1\) and the logarithmic barrier has coefficient two. It contributes only \(O(m)\). The other prefactor has logarithm \(O(m\log(m+2))\), including \(m!\).

Compactify \((0,\infty)\) by the two endpoints zero and infinity. The kernel \(K_\tau\) is continuous off the diagonal and tends uniformly to minus infinity at either boundary or the diagonal. The latter statements follow from
\(\log|x-y|\le\log(1+x)+\log(1+y)\) and the square-root and logarithmic barriers in \(Q_\tau\). Thus \(K_{\tau,T}=\max(K_\tau,-T)\) extends continuously to the compact square. With the empirical probability \(L_m\), its diagonal value is \(-T\), and

\[
\frac1{m^2}\sum_{i\ne j}K_\tau(x_i,x_j)
\le\iint K_{\tau,T}dL_m^2+T/m.
\]

Integration against \(\omega_0^m\) is bounded by the maximum of the right side. The maxima of the truncated energies decrease, as \(T\to\infty\), to \(F(\tau)\): choose maximizing probabilities for the continuous kernels, pass to a weakly convergent subsequence on the compactification, compare its energy with every fixed truncation, and then let that truncation grow. A limit with boundary mass has energy minus infinity and cannot improve the finite test value at \(\mu\). This proves the upper half of (PJ64).

For the lower bound restrict every variable to \([a,b]\). The lower Gamma envelope gives
\(d\eta_t\ge A\kappa_t e^{-mV(x)}x^{-3/4}dx\) there for all sufficiently large \(t\). Change the integral in (PJ62) to \(\mu^{\otimes m}\) and apply Jensen. The logarithm is bounded below by

\[
m\log\kappa_t+m(m-1)\iint\log|x-y|d\mu^2
-m^2\int Vd\mu+O(m)-\log(m!).
\]

The \(O(m)\) term is the finite entropy integral of \(Ax^{-3/4}/\rho(x)\). Finiteness follows from \(a>0\), the positive bounded factor in (PJ53), and the integrability of its square-root endpoint logarithms. EIQ uniqueness identifies the energy at \(\mu\) as \(F(0)\), proving the lower half of (PJ64). The upper half at zero then gives an actual limit at zero.

The same compact-kernel argument provides a maximizing probability for \(F(\tau)\). It also proves differentiability at zero, as follows. Uniformly for small \(\tau\),
\(K_\tau(x,y)\le C-c(\sqrt x+|\log x|)-c(\sqrt y+|\log y|)\)
with fixed positive \(c,C\). Testing on \(\mu\) gives a common finite lower bound for the maximum, so the maximizing probabilities have uniformly bounded indicated moments. Their \(\phi\)-integrals are uniformly integrable because \(\log(A_*+x)/\sqrt{x}\to0\) at infinity and \(\phi\) is bounded near zero. As \(\tau\to0\), every weak limit of maximizing measures maximizes the unperturbed energy, by the upper-semicontinuity argument with fixed truncated kernels. EIQ23 forces this limit to be \(\mu\). Testing each potential on the other one's maximizer bounds the secant of \(F\) by the two \(\phi\)-integrals. They converge to the same value, so

\[
F'(0)=\int\log(A_*+x)d\mu(x).
\tag{PJ65}
\]

The Vandermonde expression makes \(f_t\) convex, by Hölder's inequality. For \(\epsilon>0\) and \(m\epsilon\ge1\), its secants give

\[
\frac{f_t(0)-f_t(-m\epsilon)}{m^2\epsilon}
\le\frac{f_t(1)-f_t(0)}m
\le\frac{f_t(m\epsilon)-f_t(0)}{m^2\epsilon}.
\]

The exact \(m\log\kappa_t\) cancels in both differences. Apply precisely the two directions in (PJ64) and then let \(\epsilon\downarrow0\). Equation (PJ65) proves

\[
\frac{f_t(1)-f_t(0)}m\longrightarrow\int\log(A_*+x)d\mu(x).
\tag{PJ66}
\]

The monic degree-\(m\) orthogonal polynomial for \(\eta_t\) is exactly \(p_m\) in (PJ56). Its determinant expression has the first \(m\) rows \((\mu_i,\ldots,\mu_{i+m})\), \(0\le i<m\), and the final row \((1,z,\ldots,z^m)\), divided by \(D_m(\eta_t)\). It is monic; integration against \(z^j\), \(j<m\), duplicates the \(j\)-th moment row, proving orthogonality. Expanding the Vandermonde expression for that determinant also gives
\(p_m(z)=\int\prod_i(z-x_i)\,\Delta(x)^2\prod d\eta_t/(m!D_m(\eta_t))\).
At \(z=-A_*\), this is the exact identity

\[
(-1)^mp_m(-A_*)=\frac{D_m((A_*+x)\eta_t)}{D_m(\eta_t)}.
\tag{PJ67}
\]

Let \(\zeta_t\) be the empirical probability of the \(m\) zeros of \(p_m\). They all lie in the fixed interval \([c^2,C^2]\), by (PJ18) and (PJ56). Equations (PJ66)–(PJ67) say
\(\int\log(A_*+x)d\zeta_t\to\int\log(A_*+x)d\mu\) for every \(A_*>0\).
Any weak limit of \(\zeta_t\) is compactly supported. For \(A_*\) larger than both compact supports, the uniformly convergent series

\[
\log(A_*+x)=\log A_*+
\sum_{j\ge1}\frac{(-1)^{j+1}x^j}{jA_*^j}
\]

shows that the two measures have identical moments, by uniqueness of power-series coefficients. Polynomial approximation on the common compact interval proves equality of the measures. Thus \(\zeta_t\Rightarrow\mu\). Both supports are separated from zero, so \(\log x\) is a continuous bounded test function there. With the exact EIQ logarithmic statistic \(L=\mathcal L(2,\pi)=\int\log x\,d\mu\),

\[
\log|U_t^{[t]}(0)|
=t\log t+\log|p_m(0)|
=t\log t+\frac t2L+o(t).
\tag{PJ68}
\]

This proves \(r_U(t)=o(t)\) in its original coordinate and establishes the entire required specialization of the retained zero-law proof. The division by the number of roots in an empirical probability does not change the polynomial or its norm; its factor \(m=t/2\) is restored explicitly in (PJ68).

## PJ14. Closed diagonal conclusion and its exact provider dictionary

Equations (PJ60), (PJ68), (PJ51), and the odd transport (PJ45) prove

\[
\frac1t\log[d_t\mathsf K_{t,t}(0,0)]
\longrightarrow 2\log(4/\pi)-2\psi(1)+\mathcal L(2,\pi)+2-4\log2.
\tag{PJ69}
\]

The exact equality of this expression to the incoming elliptic constant is proved in [ELLIPTIC_LOG_MOMENT_PROOF.md, EL11–EL12](ELLIPTIC_LOG_MOMENT_PROOF.md). That complete local proof is part of this derivation's source set; this link is not represented as an already-public publication. Its entire EL1–EL14 argument was read and its endpoint derivatives and constants independently checked. In the original endpoint variables \(w=(u+v)/2\), \(z=uv\), \(c_{\rm cap}=(v^2-u^2)/4\), it proves

\[
\mathcal L(2,\pi)=6\log w-2\log z-2,
\quad\lambda(2,\pi)=8-4\log w-2\log c_{\rm cap},
\]

so the right side of (PJ69) is exactly

\[
2\log\frac{4w^2}{\pi z\sqrt{c_{\rm cap}}}
=2\log\frac{E(\kappa)(1+r)^2}{2\pi r\kappa}
=C_\partial/2.
\tag{PJ70}
\]

This is a proved identity between the scalar from the original Gamma measure and the supplied elliptic coefficient, not a coefficient assigned from original arithmetic kernel data. Equivalently, (PJ59) writes it as \(2\log(4/\pi)-2+\lambda(2,\pi)/2+\mathcal L(2,\pi)\). Substitution into (PJ48) completes the requested low/high comparison with its explicit scalar diagonal remainder. In particular, when \(s/q\to0\), both the finite jet error and the scalar remainder are \(o(q)\).

The full argument now depends on the retained and read EIQ1–EIQ33 equilibrium construction, with explicit parameter value \((2,\pi)\); its use of AP1–AP3 and NG10–NG15 is supplied as a complete specialization above. No inferred UIT or IVO locator is needed to close this proof.
