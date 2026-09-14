# Exact finite remainder bound and affine raw-jet transport

This note proves the finite coefficient estimate requested for the volume-comparator calculation. All roots are counted with their original multiplicities. The degree, affine unit, complex phase, domains, and codomains remain explicit throughout.

## 1. Polynomial spaces and the remainder map

Let \(q\geq1\) be an integer and write

\[
\chi_x(x)=\prod_{a=1}^{q}(x-\lambda_a),\qquad |\lambda_a|\leq R,
\qquad R\geq0.
\tag{RB.1}
\]

Repeated entries of \((\lambda_1,\ldots,\lambda_q)\) record root multiplicity. Set

\[
\mathcal P_d(x)=\left\{\sum_{j=0}^{d}u_jx^j:u_j\in\mathbb C\right\},
\qquad
\|P\|_{1,x}=\sum_{j=0}^{d}|u_j|.
\tag{RB.2}
\]

The exact linear map in this note is

\[
\mathcal R_{\chi_x}:\mathcal P_{2q-1}(x)\longrightarrow\mathcal P_{q-1}(x),
\qquad P=\chi_x Q+\mathcal R_{\chi_x}P,
\quad Q\in\mathcal P_{q-1}(x).
\tag{RB.3}
\]

Existence follows by subtracting the leading coefficient times the corresponding monomial multiple of the monic polynomial \(\chi_x\), decreasing the degree at each step until it is below \(q\). For uniqueness, the difference of two decompositions satisfies \(\chi_x(Q_1-Q_2)=r_2-r_1\), where the right side has degree below \(q\). A nonzero left side has degree at least \(q\), so both sides vanish. Applying this uniqueness to linear combinations proves linearity. In particular \(\mathcal R_{\chi_x}x^j=x^j\) for \(0\leq j<q\).

## 2. The complete homogeneous division formula

Let \(e_a\) be the elementary symmetric polynomial of degree \(a\) in the listed roots, with \(e_0=1\), and define the complete homogeneous polynomials by

\[
h_\ell(\lambda_1,\ldots,\lambda_q)
=\sum_{\substack{\alpha_1,\ldots,\alpha_q\geq0\\
                  \alpha_1+\cdots+\alpha_q=\ell}}
\lambda_1^{\alpha_1}\cdots\lambda_q^{\alpha_q},
\qquad h_0=1.
\tag{RB.4}
\]

As an identity of formal power series,

\[
\left(\sum_{a=0}^{q}(-1)^ae_at^a\right)
\left(\sum_{\ell=0}^{\infty}h_\ell t^\ell\right)
=\prod_{a=1}^{q}(1-\lambda_at)
 \prod_{a=1}^{q}\left(\sum_{b=0}^{\infty}(\lambda_at)^b\right)=1.
\tag{RB.5}
\]

There is no convergence requirement: every coefficient uses only finitely many factors and terms. Thus, for every integer \(s\geq1\),

\[
\sum_{a=0}^{\min(q,s)}(-1)^ae_ah_{s-a}=0.
\tag{RB.6}
\]

For \(0\leq m\leq q-1\), put

\[
Q_m(x)=\sum_{\ell=0}^{m}h_\ell x^{m-\ell}.
\tag{RB.7}
\]

The coefficient of \(x^{q+m}\) in \(\chi_xQ_m\) is one. For \(1\leq s\leq m\), the coefficient of \(x^{q+m-s}\) is the left side of (RB.6), hence zero. Therefore

\[
x^{q+m}-\chi_x(x)Q_m(x)\in\mathcal P_{q-1}(x).
\]

The uniqueness in (RB.3) now gives the exact division identity

\[
\boxed{\mathcal R_{\chi_x}x^{q+m}=x^{q+m}-\chi_xQ_m.}
\tag{RB.8}
\]

For completeness its individual coefficients are

\[
[x^r]\mathcal R_{\chi_x}x^{q+m}
=-\sum_{\substack{0\leq a\leq q,\ 0\leq\ell\leq m\\
                   a+\ell=q+m-r}}
(-1)^ae_ah_\ell,
\qquad 0\leq r<q.
\tag{RB.9}
\]

This expression remains valid for repeated and zero roots without taking limits.

## 3. Explicit coefficient-norm bound

The coefficient norm is submultiplicative. Indeed, if \(U=\sum u_jx^j\) and \(V=\sum v_kx^k\), then

\[
\|UV\|_{1,x}
=\sum_r\left|\sum_{j+k=r}u_jv_k\right|
\leq\sum_{j,k}|u_j||v_k|
=\|U\|_{1,x}\|V\|_{1,x}.
\tag{RB.10}
\]

Consequently

\[
\|\chi_x\|_{1,x}\leq\prod_{a=1}^{q}(1+|\lambda_a|)\leq(1+R)^q.
\tag{RB.11}
\]

The number of weak compositions of \(\ell\) into \(q\) nonnegative parts is \(\binom{q+\ell-1}{\ell}\): place \(q-1\) separators among a row of \(\ell\) markers and those separators. Thus (RB.4) yields

\[
|h_\ell|\leq\binom{q+\ell-1}{\ell}R^\ell,
\qquad
\|Q_m\|_{1,x}\leq
\sum_{\ell=0}^{m}\binom{q+\ell-1}{\ell}R^\ell.
\tag{RB.12}
\]

In (RB.8), the leading monomial \(x^{q+m}\) and the remainder have disjoint degree supports. In particular

\[
\|\chi_xQ_m\|_{1,x}=1+\|\mathcal R_{\chi_x}x^{q+m}\|_{1,x}.
\tag{RB.13}
\]

Combining (RB.10)--(RB.13) proves, with the original radius retained,

\[
\boxed{
\|\mathcal R_{\chi_x}x^{q+m}\|_{1,x}
\leq (1+R)^q
\sum_{\ell=0}^{m}\binom{q+\ell-1}{\ell}R^\ell-1,
\quad 0\leq m\leq q-1.}
\tag{RB.14}
\]

When \(R\leq1\), the finite sum of binomial coefficients is

\[
\sum_{\ell=0}^{m}\binom{q+\ell-1}{\ell}=\binom{q+m}{m}.
\tag{RB.15}
\]

To verify this identity, its \(m=0\) case is \(1=1\), and its induction step is Pascal's identity
\(\binom{q+m-1}{m-1}+\binom{q+m-1}{m}=\binom{q+m}{m}\).
The right side of (RB.15) increases with \(m\), as is also immediate from its sum expression. Define the exact integer

\[
C_q=2^q\binom{2q-1}{q-1}-1.
\tag{RB.16}
\]

Then \(C_q\geq1\), with \(C_1=1\), and every column of the remainder map satisfies

\[
\max_{0\leq j\leq2q-1}\|\mathcal R_{\chi_x}x^j\|_{1,x}\leq C_q.
\tag{RB.17}
\]

The two central coefficients \(\binom{2q-1}{q-1}\) and \(\binom{2q-1}{q}\) are equal. Their sum is at most the sum of all coefficients of \((1+t)^{2q-1}\) at \(t=1\), which is \(2^{2q-1}\). Therefore

\[
\boxed{C_q\leq2^{3q-2}-1<8^q.}
\tag{RB.18}
\]

For an arbitrary \(P=\sum_{j=0}^{2q-1}u_jx^j\), linearity and the triangle inequality give

\[
\boxed{\|\mathcal R_{\chi_x}P\|_{1,x}
\leq C_q\|P\|_{1,x}<8^q\|P\|_{1,x}\quad(P\neq0).}
\tag{RB.19}
\]

The non-strict version with \(8^q\) holds also for \(P=0\). In fact the induced operator norm between these coefficient \(\ell^1\) spaces equals the maximum column norm: the displayed triangle inequality proves the upper bound, and applying the operator to a monomial attaining the finite maximum proves the reverse inequality.

## 4. Raw jets and the exact quotient section

Write the distinct roots as \(\lambda_1^*,\ldots,\lambda_s^*\), with multiplicities \(m_1,\ldots,m_s\), so \(\sum_\nu m_\nu=q\). Define the raw-jet space and map by

\[
\mathcal J_x=\bigoplus_{\nu=1}^{s}\mathbb C^{m_\nu},\qquad
J_{\chi_x,d}:\mathcal P_d(x)\longrightarrow\mathcal J_x,
\qquad P\longmapsto
\left(P^{(r)}(\lambda_\nu^*)\right)_{
 1\leq\nu\leq s,\ 0\leq r<m_\nu}.
\tag{RB.20}
\]

The exact Taylor identity at a root is

\[
P(x)=\sum_{r=0}^{d}\frac{P^{(r)}(\lambda_\nu^*)}{r!}
(x-\lambda_\nu^*)^r.
\]

It shows that the first \(m_\nu\) raw derivatives vanish precisely when \((x-\lambda_\nu^*)^{m_\nu}\) divides \(P\). Simultaneous divisibility by these distinct-root factors is equivalent to divisibility by their product \(\chi_x\): in the factorization of a nonzero polynomial over \(\mathbb C\), the exponent at each distinct root must be at least the listed multiplicity. The zero polynomial is divisible by every factor. Hence, for \(d\geq q\),

\[
\ker J_{\chi_x,d}=\chi_x\mathcal P_{d-q}(x).
\tag{RB.21}
\]

The restriction \(J_{\chi_x,q-1}\) has zero kernel by degree, and both its domain and codomain have dimension \(q\). It is therefore an isomorphism. Equation (RB.3) gives

\[
\boxed{
J_{\chi_x,q-1}\mathcal R_{\chi_x}=J_{\chi_x,2q-1},
\qquad
\mathcal R_{\chi_x}=J_{\chi_x,q-1}^{-1}J_{\chi_x,2q-1}.}
\tag{RB.22}
\]

Thus this remainder map preserves every specified raw jet, including every derivative order required by multiplicity. Equivalently, the inclusion of \(\mathcal P_{q-1}(x)\) followed by the quotient map is an isomorphism onto \(\mathbb C[x]/(\chi_x)\), and (RB.3) is the unique representative of degree below \(q\) in that quotient class.

## 5. Original \(S\) variable, affine unit, and phase

Let the original monic annihilator be

\[
\chi(S)=\prod_{\nu=1}^{s}(S-\zeta_\nu)^{m_\nu},
\qquad c\in\mathbb C,\quad T>0.
\tag{RB.23}
\]

Use the requested transformed-polynomial notation with its full definition:

\[
\boxed{
\bar\chi(x)=(iT)^{-q}\chi(c+iTx)
=\prod_{\nu=1}^{s}\left(x-\frac{\zeta_\nu-c}{iT}\right)^{m_\nu}.}
\tag{RB.24}
\]

Here the bar symbol is defined by (RB.24); complex conjugation of a polynomial, if used elsewhere, has its separate coefficientwise definition. The displayed unit \((iT)^{-q}\) proves monicity and retains the full complex phase. The transformed root radius is exactly bounded by

\[
\left|\frac{\zeta_\nu-c}{iT}\right|
=\frac{|\zeta_\nu-c|}{T};
\quad\text{in particular }\max_\nu|\zeta_\nu-c|\leq T
\Longrightarrow R\leq1.
\tag{RB.25}
\]

For every \(d\geq0\), define the invertible linear map

\[
A_{c,T,d}:\mathcal P_d(S)\longrightarrow\mathcal P_d(x),
\quad (A_{c,T,d}P)(x)=P(c+iTx),
\]
\[
A_{c,T,d}^{-1}F(S)=F\left(\frac{S-c}{iT}\right).
\tag{RB.26}
\]

Substitution also defines an algebra isomorphism on the whole polynomial rings. In particular it sends the principal ideal \((\chi)\) onto \((\bar\chi)\), because \(A\chi=(iT)^q\bar\chi\) and the factor \((iT)^q\) is a nonzero scalar unit. Thus the induced quotient map is exactly

\[
\widehat A_{c,T}:\mathbb C[S]/(\chi)\longrightarrow\mathbb C[x]/(\bar\chi),
\qquad [P]\longmapsto[P(c+iTx)],
\tag{RB.27}
\]

with inverse induced by the second formula in (RB.26).

Apply (RB.26) to the original division \(P=\chi Q+\mathcal R_\chi P\). One obtains

\[
A_{c,T,2q-1}P
=\bar\chi\,\big((iT)^q A_{c,T,q-1}Q\big)
 +A_{c,T,q-1}\mathcal R_\chi P.
\tag{RB.28}
\]

The last term has degree below \(q\). Uniqueness of division gives the exact commuting identity

\[
\boxed{
\mathcal R_{\bar\chi}A_{c,T,2q-1}
=A_{c,T,q-1}\mathcal R_\chi.}
\tag{RB.29}
\]

For raw jets, set \(\lambda_\nu^*=(\zeta_\nu-c)/(iT)\). Let \(J_{\chi,d}\) be defined using derivatives in \(S\) at \(\zeta_\nu\), and let \(J_{\bar\chi,d}\) use derivatives in \(x\) at \(\lambda_\nu^*\), with the same ordering and multiplicities. Repeated application of the ordinary chain rule gives, for every integer \(r\geq0\),

\[
\frac{d^r}{dx^r}P(c+iTx)=(iT)^rP^{(r)}(c+iTx).
\]

Define the invertible diagonal map

\[
D_T:\bigoplus_\nu\mathbb C^{m_\nu}\longrightarrow
\bigoplus_\nu\mathbb C^{m_\nu},
\quad (v_{\nu,r})\longmapsto((iT)^rv_{\nu,r}).
\tag{RB.30}
\]

The complete raw-jet transport identity is therefore

\[
\boxed{J_{\bar\chi,d}A_{c,T,d}=D_TJ_{\chi,d}.}
\tag{RB.31}
\]

Every scalar \((iT)^r\), including its phase, appears in (RB.30)--(RB.31); the jet coordinates throughout are raw derivatives. Combining (RB.22), (RB.29), and (RB.31) proves preservation of the original raw jets as well as the transformed raw jets.

## 6. Exact norm transfer back to the original coordinates

Define a norm on the original polynomial space by the displayed affine transport,

\[
\|P\|_{c,T,1}:=\|A_{c,T,d}P\|_{1,x}.
\tag{RB.32}
\]

This definition is independent of the choice of \(d\geq\deg P\), because adding zero coefficients does not change the sum. Invertibility of \(A\) proves that it is a norm. Equations (RB.19) and (RB.29), under the root-radius hypothesis in (RB.25), yield

\[
\boxed{\|\mathcal R_\chi P\|_{c,T,1}
\leq C_q\|P\|_{c,T,1},
\qquad P\in\mathcal P_{2q-1}(S).}
\tag{RB.33}
\]

The same estimate expressed using the untransformed coefficient norm also has fully explicit constants. For \(0\leq j\leq d\), the binomial theorem gives

\[
\|A_{c,T,d}S^j\|_{1,x}=(|c|+T)^j,
\qquad
\|A_{c,T,d}^{-1}x^j\|_{1,S}
=\left(\frac{1+|c|}{T}\right)^j.
\tag{RB.34}
\]

The maximum-column characterization of the coefficient \(\ell^1\) operator norm, proved after (RB.19), consequently gives the exact operator norms

\[
\|A_{c,T,d}\|_{1\to1}=\max\{1,(|c|+T)^d\},
\quad
\|A_{c,T,d}^{-1}\|_{1\to1}
=\max\left\{1,\left(\frac{1+|c|}{T}\right)^d\right\}.
\tag{RB.35}
\]

Thus the original-coordinate estimate is

\[
\boxed{
\|\mathcal R_\chi P\|_{1,S}
\leq C_q
\max\left\{1,\left(\frac{1+|c|}{T}\right)^{q-1}\right\}
\max\{1,(|c|+T)^{2q-1}\}
\|P\|_{1,S}.}
\tag{RB.36}
\]

Finally, for any \(x\in\mathbb C\) and any polynomial \(r\) of degree below \(q\), the coefficient triangle inequality gives
\(|r(x)|\leq\|r\|_{1,x}\max\{1,|x|^{q-1}\}\). Applying this to the exact representative in (RB.29) yields

\[
\boxed{
|(\mathcal R_\chi P)(c+iTx)|
\leq C_q\|P\|_{c,T,1}\max\{1,|x|^{q-1}\}.}
\tag{RB.37}
\]

In particular the maximum on the segment \(S=c+iTx\), \(-1\leq x\leq1\), is at most \(C_q\|P\|_{c,T,1}\). Equations (RB.24), (RB.27), (RB.29), and (RB.31) specify the exact relation to the original annihilator, quotient, representative, and raw-jet coordinates; no measure or quotient metric is replaced in this coefficient calculation.
