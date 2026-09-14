# Single-primary division, Pascal transport, and full-unit audit

This is the bounded independent algebra audit requested by the parent task. It proves the stated matrices in their precise domains and gives the exact coordinate transport of the complete arithmetic Taylor unit. It does not assert the existence of an offcritical zero or a conclusion about RH.

The assignment, verbatim:

> Bounded independent algebra audit only. For actual rho, m>=1,n=m+1,h=(s-rho)^m,P_ab=binom(b,a)rho^(b-a) coefficients s-to-y (y=s-rho), c=-(-rho)^n/n. Derive monic division f(s)s^b=(s-rho)^m q_b+r_b with f=((s-rho)^n-(-rho)^n)/n at t=0, hence C=cI, B column ((b+1)s^b-b rho s^(b-1))/n. Verify PBP^-1=diag((a+1)/n), A=P^-1(rhoI+N)P with N lower shift, [B,A]=P^-1 N P/n. Prove exact full Taylor unit U=sum v^(r)(rho)N^r/r! transported and unit weighted coordinate effects. Write ONLY work/rh_counterfactual_20260913/total_object/single_primary_review/matrix_audit.md. No global edits; send proof issues if any.

## 1. Objects, bases, and column convention

Fix the actual complex number \(\rho\), the integer \(m\geq1\), and \(n=m+1\). Retain
\[
 y=s-\rho,\qquad h(s)=(s-\rho)^m=y^m,\qquad
 c=-\frac{(-\rho)^n}{n},\qquad
 f(s)=\frac{(s-\rho)^n-(-\rho)^n}{n}=\frac{y^n}{n}+c.
\tag{MA1}
\]
In particular \(f(0)=0\) and \(f'(s)=h(s)\), including their constants and signs.

Let \(E=\mathbb C[s]/(h)\). Its two ordered bases are
\[
 \mathcal S=(1,s,\ldots,s^{m-1}),\qquad
 \mathcal Y=(1,y,\ldots,y^{m-1}).
\tag{MA2}
\]
All vectors below are columns. If \(p\) is the unique degree-less-than-\(m\) representative of a class, write \(x_{\mathcal S}(p)\) and \(x_{\mathcal Y}(p)\) for its coefficient columns. The change of coordinates is
\[
 x_{\mathcal Y}=P x_{\mathcal S},\qquad
 P_{ab}=
 \begin{cases}
 \binom ba\rho^{b-a},&0\leq a\leq b\leq m-1,\\
 0,&a>b.
 \end{cases}
\tag{MA3}
\]
This follows by expanding \(s^b=(y+\rho)^b\). Its inverse is
\[
 (P^{-1})_{ab}=
 \begin{cases}
 \binom ba(-\rho)^{b-a},&0\leq a\leq b\leq m-1,\\
 0,&a>b.
 \end{cases}
\tag{MA4}
\]
Indeed, expanding \(y^b=(s-\rho)^b\) gives this inverse directly. To check the matrix product, for \(a\leq b\) its \((a,b)\) entry is
\[
 \sum_{j=a}^{b}\binom ja\binom bj
       \rho^{j-a}(-\rho)^{b-j}
 =\binom ba
   \sum_{\ell=0}^{b-a}\binom{b-a}{\ell}
        \rho^\ell(-\rho)^{b-a-\ell}.
\]
It is one for \(a=b\) and zero otherwise. Both matrices have determinant one.

## 2. The complete monic division

For each integer \(0\leq b\leq m-1\), the literal polynomial identity is
\[
 f(s)s^b
 =h(s)\,\frac{(s-\rho)s^b}{n}+c s^b.
\tag{MA5}
\]
Because \(\deg(c s^b)<m\) when this polynomial is nonzero, the unique monic-division quotient and remainder are
\[
 q_b(s)=\frac{(s-\rho)s^b}{n},
 \qquad r_b(s)=c s^b.
\tag{MA6}
\]
Uniqueness follows because a nonzero difference of two remainders would be a multiple of the monic degree-\(m\) polynomial \(h\), but would have degree less than \(m\).

Let \(C\) have column \(b\) equal to \(x_{\mathcal S}(r_b)\), and let \(B\) have column \(b\) equal to \(x_{\mathcal S}(q_b')\). Then
\[
 C=cI_m,\qquad
 q_b'(s)=\frac{(b+1)s^b-b\rho s^{b-1}}{n}.
\tag{MA7}
\]
At \(b=0\), this last expression means \(q_0'=1/n\); it contains no negative-degree monomial. Thus
\[
 B_{ab}=
 \begin{cases}
 (b+1)/n,&a=b,\\
 -b\rho/n,&a=b-1,\ b\geq1,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{MA8}
\]
The derivative in the definition of \(B\) is essential: the division quotient itself is \(q_b\), not \(q_b'\).

Define on polynomials
\[
 \mathcal D p=\frac{p+(s-\rho)p'}{n}.
\tag{MA9}
\]
It preserves the ideal \((h)\), since
\[
 \mathcal D(hq)
 =\frac{hq+(s-\rho)(h'q+hq')}{n}
 =h\left(q+\frac{s-\rho}{n}q'\right),
\tag{MA10}
\]
where \((s-\rho)h'=mh\) and \(m+1=n\). Consequently \(\mathcal D\) induces an actual endomorphism of \(E\), whose matrix in \(\mathcal S\) is \(B\). In \(\mathcal Y\), it sends \(y^a\) to \((a+1)y^a/n\). Therefore
\[
 PBP^{-1}=D,\qquad
 D=\operatorname{diag}\left(\frac1n,\frac2n,\ldots,\frac mn\right).
\tag{MA11}
\]
In particular, without suppressing \(n=m+1\),
\[
 \operatorname{Tr}B=\frac{m(m+1)}{2n}=\frac m2,
 \qquad
 \det B=\frac{m!}{n^m}.
\tag{MA12}
\]

## 3. The original local multiplication operator

Let \(A:E\to E\) be multiplication by the original coordinate \(s\). Let \(N\) be the \(m\)-by-\(m\) matrix
\[
 Ne_a=
 \begin{cases}
 e_{a+1},&0\leq a<m-1,\\
 0,&a=m-1,
 \end{cases}
\tag{MA13}
\]
where \(e_a\) is the coordinate column of \(y^a\). This is the lower shift, so \(N^m=0\), and \(N^{m-1}\neq0\). Since \(s=\rho+y\), the exact transport is
\[
 PAP^{-1}=\rho I_m+N,
 \qquad A=P^{-1}(\rho I_m+N)P.
\tag{MA14}
\]
For completeness, its original \(\mathcal S\)-matrix has \(Ae_b=e_{b+1}\) for \(b<m-1\), and its final column is
\[
 A_{a,m-1}=-\binom ma(-\rho)^{m-a},
 \qquad 0\leq a\leq m-1,
\tag{MA15}
\]
because \(h=s^m+\sum_{a=0}^{m-1}\binom ma(-\rho)^{m-a}s^a\) vanishes in \(E\).

On \(e_a\) with \(a<m-1\),
\[
 (DN-ND)e_a
 =\left(\frac{a+2}{n}-\frac{a+1}{n}\right)e_{a+1}
 =\frac1n Ne_a,
\]
and both sides vanish on \(e_{m-1}\). Hence
\[
 [B,A]=BA-AB=\frac1n P^{-1}NP=\frac{A-\rho I_m}{n}.
\tag{MA16}
\]
The commutator sign is positive with the displayed order \(BA-AB\). For \(m=1\), \(N=0\), \(A=(\rho)\), \(B=(1/2)\), and the same formula gives zero. No semisimplification of \(A\) has occurred.

## 4. The complete Taylor unit and its inverse

Let \(v\) denote the original holomorphic unit germ at \(\rho\), with \(v(\rho)\neq0\). In the application it is the actual germ of \(g/h\) at a zero \(\rho\) of full order \(m\), and no derivative coefficient of that germ is replaced by a freely chosen value. Set
\[
 v_r=\frac{v^{(r)}(\rho)}{r!}\quad(0\leq r<m),
 \qquad
 \widehat v(y)=\sum_{r=0}^{m-1}v_r y^r.
\tag{MA17}
\]
For the actual \(v=g/(s-\rho)^m\), this is equivalently \(v_r=g^{(m+r)}(\rho)/(m+r)!\), by the Taylor expansion of \(g\) at its order-\(m\) zero.
Taylor's formula in the local holomorphic ring gives
\(v(\rho+y)-\widehat v(y)\in(y^m)\). Thus multiplication by the full class of \(v\) on \(E\) has exactly the matrix
\[
 U=\sum_{r=0}^{m-1}v_rN^r,
 \qquad
 (Ux)_a=\sum_{b=0}^{a}v_{a-b}x_b
\tag{MA18}
\]
in \(\mathcal Y\). Every coefficient that can act on the original length-\(m\) local algebra appears. Its determinant is \(v_0^m\neq0\).

Define \(w_0=v_0^{-1}\), and successively
\[
 w_r=-v_0^{-1}\sum_{j=1}^{r}v_jw_{r-j},
 \qquad 1\leq r<m.
\tag{MA19}
\]
The coefficient of \(y^0\) in \(\widehat v\sum w_ry^r\) is one, and the coefficient of \(y^r\), \(1\leq r<m\), is
\(v_0w_r+\sum_{j=1}^{r}v_jw_{r-j}=0\). Therefore
\[
 U^{-1}=\sum_{r=0}^{m-1}w_rN^r
       =\sum_{r=0}^{m-1}\frac{(1/v)^{(r)}(\rho)}{r!}N^r.
\tag{MA20}
\]
The last equality follows from the uniquely determined Taylor coefficients of \(v(1/v)=1\).

In the original coordinates the same endomorphism is
\[
 U_{\mathcal S}=P^{-1}UP
 =\sum_{r=0}^{m-1}
        \frac{v^{(r)}(\rho)}{r!}(A-\rho I_m)^r.
\tag{MA21}
\]
It commutes with \(A\). On the terminal vector \(e_{m-1}\) in \(\mathcal Y\) it acts by \(v_0\), because \(Ne_{m-1}=0\); on the other vectors the higher Taylor coefficients generally remain nonzero. The terminal scalar formula does not justify replacing \(U\) by \(v_0I_m\) on the whole algebra.

## 5. Unit-weighted coordinate effects

The following formulas specify the coordinate convention, so there is no inverse ambiguity. Let an old \(\mathcal Y\)-coordinate column \(x\) and a unit-weighted coordinate column \(z\) describe the same vector by
\[
 x=Uz.
\tag{MA22}
\]
Then the matrices in the \(z\)-coordinates are
\[
 A_{\mathrm{wt}}=U^{-1}(\rho I_m+N)U=\rho I_m+N,
 \quad C_{\mathrm{wt}}=cI_m,\quad
 B_{\mathrm{wt}}=U^{-1}DU.
\tag{MA23}
\]
Put
\[
 V_1=\sum_{r=1}^{m-1}r v_rN^r.
\tag{MA24}
\]
Since \(DN^r-N^rD=rN^r/n\), summation gives
\[
 [D,U]=\frac{V_1}{n},\qquad
 U^{-1}DU=D+\frac{U^{-1}V_1}{n},\qquad
 UDU^{-1}=D-\frac{V_1U^{-1}}{n}.
\tag{MA25}
\]
The matrix \(U^{-1}V_1\) is the exact multiplication matrix of the local class
\[
 \frac{y\,v'(\rho+y)}{v(\rho+y)}
       \pmod{y^m}.
\tag{MA26}
\]
This class has zero constant term. In particular the correction in (MA25) is strictly lower triangular, its trace is zero, and no \(v_r\) in (MA17) has been discarded. The second and third expressions in (MA25) correspond to inverse coordinate conventions; they must not be interchanged.

Returning to \(\mathcal S\), the convention \(x_{\mathcal S}=U_{\mathcal S}z_{\mathcal S}\) gives
\[
 B_{\mathcal S,\mathrm{wt}}
 =U_{\mathcal S}^{-1}BU_{\mathcal S}
 =P^{-1}\left(D+\frac{U^{-1}V_1}{n}\right)P,
 \qquad
 [B_{\mathcal S,\mathrm{wt}},A]
 =\frac{A-\rho I_m}{n}.
\tag{MA27}
\]
The last equality follows either by conjugating (MA16), or by observing that the correction in (MA27) is a polynomial in \(A-\rho I_m\) and therefore commutes with \(A\).

If \(G_{\mathcal S}\) is the actual Hermitian matrix of the source-induced form in the original coordinates, these coordinate changes give exactly
\[
 G_{\mathcal Y}=(P^{-1})^*G_{\mathcal S}P^{-1},
 \qquad
 G_{\mathrm{wt}}=U^*G_{\mathcal Y}U.
\tag{MA28}
\]
Indeed \(x_{\mathcal S}=P^{-1}Uz\), so
\(x_{\mathcal S}^*G_{\mathcal S}x_{\mathcal S}
=z^*U^*(P^{-1})^*G_{\mathcal S}P^{-1}Uz\).
Consequently
\[
 \det G_{\mathrm{wt}}=|v_0|^{2m}\det G_{\mathcal S},
\tag{MA29}
\]
using \(\det P=1\). For inverse-unit coordinates \(x=U^{-1}z\), the form is instead \((U^{-1})^*G_{\mathcal Y}U^{-1}\) and the determinant factor is \(|v_0|^{-2m}\). There is no general isometry assertion.

For an auxiliary parameter \(u\neq0\), independent of the fixed arithmetic unit \(v\), a connection expressed in \(\mathcal Y\)-coordinates as
\[
 \nabla_u=\partial_u-\frac{c}{u^2}I_m+\frac{D}{u}
\tag{MA30}
\]
has matrix in the coordinates (MA22)
\[
 U^{-1}\nabla_u U
 =\partial_u-\frac{c}{u^2}I_m
        +\frac1u\left(D+\frac{U^{-1}V_1}{n}\right).
\tag{MA31}
\]
This follows by applying the operator to \(Uz(u)\), using
\(\partial_u U=0\), and multiplying on the left by \(U^{-1}\).
Thus a full constant unit change affects the residue by its exact conjugate and does not change the scalar \(c/u^2\).

## 6. Exact relation to twisted de Rham representatives

The coordinate action just proved is not automatically multiplication on arbitrary representatives of the twisted de Rham quotient. Its precise comparison is as follows. Fix a complex parameter \(u\), and define the linear map
\[
 R_u:\mathbb C[s]\longrightarrow\mathbb C[s]\,ds,
 \qquad R_u(q)=(u q'+h q)\,ds,
 \qquad H_u=\mathbb C[s]\,ds/\operatorname{im}R_u.
\tag{MA32}
\]
This is the original plus-sign relation \(u\partial_s+h\). Its image is a vector subspace and has not been declared an ideal. If \(q\neq0\), then \(\deg(uq'+hq)=\deg q+m\): the leading term of \(hq\) cannot be canceled by the derivative term of smaller degree. It follows that no nonzero polynomial of degree less than \(m\) represents zero in \(H_u\). Conversely any polynomial of degree at least \(m\) can have its leading term canceled by a scalar multiple of \(R_u(s^j)/ds\), leaving a strictly smaller degree. Repeating finitely many times gives a unique representative of degree less than \(m\). Therefore the explicitly chosen linear map
\[
 \iota_u:E\longrightarrow H_u,\qquad
 [p]_h\longmapsto[p_{<m}(s)\,ds]_{R_u}
\tag{MA33}
\]
is an isomorphism of vector spaces, where \(p_{<m}\) is the unique monic-division remainder. It is not asserted to be induced by the identity on arbitrary polynomial representatives.

The full-unit coordinate action on \(H_u\) is the fully defined linear endomorphism
\[
 T_{v,u}=\iota_u\circ M_{[v]}\circ\iota_u^{-1}.
\tag{MA34}
\]
This supplies an exact commuting square between \(E\), \(H_u\), and the multiplication matrix (MA18). Its action uses the canonical representative, multiplies in \(E\), and then applies \(\iota_u\). It is constant in \(u\) in the chosen coefficient basis.

For an actual polynomial \(v\), multiplication on arbitrary representatives satisfies instead
\[
 v\,R_u(q)=R_u(vq)-u v'q\,ds.
\tag{MA35}
\]
This is the product rule with every sign retained. Hence multiplication by \(v\) descends through the quotient if and only if every \(u v'q\,ds\) lies in \(\operatorname{im}R_u\); a unit in \(E\) alone does not prove that property.

There is also an exact correction formula on the canonical representatives. For \(p\) of degree less than \(m\), perform ordinary monic division
\[
 v(s)p(s)=h(s)q(s)+r(s),\qquad\deg r<m.
\tag{MA36}
\]
Write \(\operatorname{red}_u\) for the unique degree-less-than-\(m\) representative just proved. Since \([h q\,ds]=-[u q'\,ds]\), the exact comparison is
\[
 \operatorname{red}_u(vp)
 =r-u\,\operatorname{red}_u(q'),
 \qquad
 \iota_u^{-1}T_{v,u}\iota_u[p]=[r]_h.
\tag{MA37}
\]
For the literal polynomial \(\widehat v(s-\rho)\) in (MA17), \(\deg\widehat v<m\), so \(\deg(\widehat v p)\leq2m-2\). Whenever \(q\neq0\), its degree is at most \(m-2\); thus \(q'\) already has degree less than \(m\), and (MA37) becomes the explicit formula \(r-u q'\). For \(m=1\) the quotient is zero because both factors are constant.

A concrete failure of representative-independent multiplication retains the original \(h=(s-\rho)^m\). Take \(v=1+y\), a unit of \(E\), and \(u\neq0\). Relation \(R_u(1)=h\,ds\) gives \([y^m ds]=0\). Relation \(R_u(y)=(u+y^{m+1})ds\) gives \([y^{m+1}ds]=-u[ds]\). Therefore
\[
 [(1+y)y^m ds]=-u[ds]\neq0.
\tag{MA38}
\]
Nonvanishing follows from the degree argument preceding (MA33). This proves the precise obstruction while (MA34) supplies the exact full-unit linear transport that remains valid. An analytic germ \(v\) requires, in addition, a specified larger representative space before multiplication on its representatives is even defined; all finite Taylor formulas (MA17)--(MA34) already make sense on the original finite local algebra and its chosen coefficient realization.

## Audit outcome

All requested division, Pascal, multiplication, and commutator identities are correct with the column convention above and with \(B\) explicitly defined from \(q_b'\). The full Taylor unit has the exact transport (MA18)--(MA21), exact inverse (MA19)--(MA20), exact residue correction (MA25)--(MA27), and exact metric change (MA28)--(MA29). The sole scope issue is any unstated identification of this finite coordinate action with multiplication on arbitrary twisted de Rham representatives; (MA34)--(MA38) give both the precise valid map and the full derivative correction.

## Independent read of the parent complex calculation

The complete current parent file single_primary_complex_review.tex, SPR.1--34, was read once independently after this algebra derivation. Its polynomial division and plus-sign complex agree with (MA5)--(MA10) and (MA32). The commutator of \(u\partial_s+h\) with \(\partial_u-f/u^2\) is \(-\partial_s-h/u\), so the displayed degree-zero correction \(1/u\) has the required positive sign. The closed connector contour gives original minus translated equal initial connector minus final connector; this agrees with SPR.10 and the preserved outward ray orientations. The gamma factors and determinant retain \(\sum_a(a+1)/n=m/2\), hence the factors \(n^{-m/2}e^{\pi i m/2}u^{m/2}e^{mc/u}\).

The period continuation acts on rows by \(W\operatorname{diag}(\zeta,\ldots,\zeta^m)W^{-1}\); horizontal sections formed from the inverse period matrix have its inverse monodromy, as SPR.21 states. The cover \(u=v^n\) and gauge \(x_a=v^{-(a+1)}z_a\) leave \(\partial_v-nc/v^{n+1}\) and the retained horizontal exponential \(e^{-c/v^n}\). The connection is exactly split before any asymptotic operation, so its claimed identity Stokes transitions follow from that explicit common model.

Finally the parent's source convention is \(q_s=U_sx_s\), the inverse of the convention used in (MA22). It therefore correctly uses \(U_sB_sU_s^{-1}\), the minus correction of (MA25), and the period matrix \(\Pi_sU_s^{-1}\). SPR.34 includes the precise derivative correction of (MA35). No further algebraic, sign, contour, monodromy, or unit-coordinate error was found in that complete read.
