# Exact powers and exponential returns in the character-zero sector

This audit proves the requested statements directly for the specified truncated tensor algebra. The truncation exponent, character shift, and operator are retained exactly.

## 1. Definitions and the exact matrix

Fix integers \(m,k\geq1\), put \(N=m+1\) and \(D=k(m-1)\), and define
\[
V=\mathbb C[y_1,\ldots,y_k]/(y_1^m,\ldots,y_k^m),\qquad
S=y_1+\cdots+y_k,\qquad T=M_S:V\longrightarrow V.
\tag{PA.1}
\]
For
\[
\mathcal A=\{a=(a_1,\ldots,a_k):0\leq a_i\leq m-1\},
\qquad |a|=\sum_i a_i,
\]
write \(e_a=y_1^{a_1}\cdots y_k^{a_k}\). These vectors form a basis of \(V\). Fix a primitive \(N\)-th root of unity \(\zeta\), and define the linear character operator
\[
g(e_a)=\zeta^{k+|a|}e_a,\qquad
E_0=\frac1N\sum_{j=0}^{N-1}g^j,\qquad
W=E_0V.
\tag{PA.2}
\]
Thus \(g\) includes exactly the prescribed shift by \(k\); it is a linear operator and need not preserve the algebra unit. The finite geometric sum gives
\[
E_0e_a=
\begin{cases}
e_a,&k+|a|\equiv0\pmod N,\\
0,&k+|a|\not\equiv0\pmod N.
\end{cases}
\tag{PA.3}
\]
In particular \(E_0^2=E_0\).

For every integer \(q\geq0\), the multinomial formula in the polynomial ring, followed by passage to the stated quotient, gives
\[
T^qe_a=
\sum_{\substack{c\in\mathbb Z_{\geq0}^k\\
|c|=q\\a_i+c_i\leq m-1\ (1\leq i\leq k)}}
\frac{q!}{c_1!\cdots c_k!}e_{a+c}.
\tag{PA.4}
\]
Every omitted term is zero in \(V\), since one of its exponents is at least \(m\). Consequently, in the full basis \((e_a)_{a\in\mathcal A}\),
\[
(E_0T^qE_0)_{b,a}=
\begin{cases}
\displaystyle\frac{q!}{\prod_{i=1}^k(b_i-a_i)!},
&\begin{array}{l}
a,b\in\mathcal A,\ b_i\geq a_i\text{ for every }i,\\
|b|-|a|=q,\quad k+|a|\equiv k+|b|\equiv0\pmod N,
\end{array}\\[4pt]
0,&\text{otherwise}.
\end{cases}
\tag{PA.5}
\]
In particular,
\[
E_0T^qE_0=0\quad\text{if }N\nmid q.
\tag{PA.6}
\]
All displayed nonzero coefficients in (PA.5) are strictly positive integers, so their existence cannot be defeated by cancellation. Directly on each monomial, \(gT=\zeta Tg\), including the terms killed by truncation. Hence \(T^N\) commutes with \(g\) and \(E_0\).

## 2. Complete nonzero criterion

Let \(d_{\min}\) be the least nonnegative residue of \(-k\) modulo \(N\):
\[
d_{\min}=N\left\lceil\frac{k}{N}\right\rceil-k,\qquad
0\leq d_{\min}\leq N-1=m.
\tag{PA.7}
\]
The possible invariant degrees are exactly
\[
d_{\min},\ d_{\min}+N,\ d_{\min}+2N,\ldots
\]
that do not exceed \(D\).

Every integer \(d\) with \(0\leq d\leq D\) is the degree of at least one basis monomial. Indeed, distribute \(d\) units successively among the \(k\) coordinates, placing at most \(m-1\) in each. If some units remained after all coordinates had been filled, then \(d>k(m-1)=D\), a contradiction. This argument covers \(m=1\): the only permitted degree is then \(d=0\).

For any \(a\in\mathcal A\) and any \(q\geq0\), a vector \(c\) occurring in (PA.4) exists if and only if
\[
q\leq\sum_i(m-1-a_i)=D-|a|.
\tag{PA.8}
\]
Necessity follows by summing the coordinate bounds. For sufficiency, distribute \(q\) units successively among the capacities \(m-1-a_i\). The same capacity argument proves termination with no units remaining.

For every integer \(r\geq1\),
\[
\boxed{E_0T^{rN}E_0\ne0
\quad\Longleftrightarrow\quad
d_{\min}+rN\leq D.}
\tag{PA.9}
\]
To prove necessity, any nonzero matrix entry has a starting invariant degree \(|a|\geq d_{\min}\), and (PA.8) implies \(|a|+rN\leq D\). To prove sufficiency, first choose \(a\in\mathcal A\) with \(|a|=d_{\min}\), which is possible because the assumed inequality implies \(0\leq d_{\min}\leq D\). Then (PA.8) supplies \(c\) with \(|c|=rN\) and \(a+c\in\mathcal A\). Both degrees are invariant, and (PA.5) gives the nonzero entry \((rN)!/\prod_i c_i!\).

At \(q=0\), the same argument shows
\[
W\ne0\quad\Longleftrightarrow\quad d_{\min}\leq D.
\tag{PA.10}
\]
If \(W\ne0\), put \(B=T^N|_W\in\operatorname{End}_{\mathbb C}(W)\). Its powers are
\[
B^r=(E_0T^{rN}E_0)|_W.
\tag{PA.11}
\]
Define the integer
\[
R=\left\lfloor\frac{D-d_{\min}}N\right\rfloor
=k-2\left\lceil\frac{k}{N}\right\rceil.
\tag{PA.12}
\]
The equality follows without altering \(D\): set \(c=\lceil k/N\rceil\), so
\[
\frac{D-d_{\min}}N
=\frac{k(m-1)-Nc+k}{N}
=k-c-\frac{k}{N},
\]
whose floor is \(k-c-\lceil k/N\rceil=k-2c\).
Since \(D\geq0\) and \(d_{\min}\leq N-1\), one always has \(R\geq-1\).
Thus \(W=0\) exactly when \(R=-1\); otherwise \(R\geq0\), \(B^r\ne0\) for \(0\leq r\leq R\), and \(B^{R+1}=0\). The nilpotence index of \(B\) on nonzero \(W\) is exactly \(R+1\), where a zero operator on a nonzero space has index one.

## 3. Invariance under the original infinitesimal operator

For \(w\in W\), the identity \(gT=\zeta Tg\) implies
\[
g(Tw)=\zeta Tw.
\tag{PA.13}
\]
Because \(N\geq2\) and \(\zeta\ne1\), the eigenvalue-\(\zeta\) subspace of \(g\) intersects \(W\), its eigenvalue-one subspace, only in zero. It follows that
\[
T(W)\subseteq W\quad\Longleftrightarrow\quad T|_W=0.
\tag{PA.14}
\]
For a monomial \(e_a\), (PA.4) at \(q=1\) has one nonzero summand for each coordinate with \(a_i<m-1\). These summands are distinct basis monomials. Hence
\[
Te_a=0\quad\Longleftrightarrow\quad |a|=D.
\tag{PA.15}
\]
If \(d_{\min}<D\), an invariant monomial of degree \(d_{\min}\) therefore has nonzero image, proving failure of invariance. If \(d_{\min}>D\), then \(W=0\). If \(d_{\min}=D\), then \(W\) is spanned by the single top monomial \(\prod_i y_i^{m-1}\), which \(T\) kills. Therefore
\[
T(W)\subseteq W
\quad\Longleftrightarrow\quad
d_{\min}\geq D
\quad\Longleftrightarrow\quad
(m=1\text{ or }k=1).
\tag{PA.16}
\]
For the last equivalence: if \(m=1\), then \(D=0\leq d_{\min}\). If \(k=1\), then \(d_{\min}=m>D=m-1\). Conversely, suppose \(m\geq2\) and \(k\geq2\). For \(k=2\), one has \(d_{\min}=m-1<2m-2=D\). For \(k\geq3\), one has
\[
D=k(m-1)\geq3(m-1)>m\geq d_{\min},
\]
where \(3(m-1)>m\) holds for every integer \(m\geq2\).

The statement concerns invariance of the whole space \(W\). Individual nonzero vectors in \(W\) may belong to \(\ker T\) even when (PA.16) fails.

## 4. The compressed exponential and its exact composition defect

Since \(T^{D+1}=0\), its exponential is the finite polynomial
\[
\exp(tT)=\sum_{q=0}^D\frac{t^q}{q!}T^q,\qquad t\in\mathbb C.
\tag{PA.17}
\]
Define the compression with its stated domain and codomain:
\[
F(t)=(E_0\exp(tT)E_0)|_W:W\longrightarrow W.
\tag{PA.18}
\]
If \(W=0\), this is the unique endomorphism of the zero vector space, which is its identity, and all composition identities are automatic. If \(W\ne0\), (PA.6), (PA.11), and (PA.12) give exactly
\[
F(t)=\sum_{r=0}^{R}\frac{t^{rN}}{(rN)!}B^r,\qquad
F(0)=I_W,\qquad F'(0)=0.
\tag{PA.19}
\]
Every \(F(t)\) is invertible: it is \(I_W\) plus a polynomial in nilpotent \(B\) with zero constant term, and a finite geometric series is an inverse. Invertibility alone therefore does not establish the group law.

The operators \(F(t)\) form a one-parameter group, meaning
\[
F(s+t)=F(s)F(t)\quad\text{for every }s,t\in\mathbb C,
\tag{PA.20}
\]
if and only if
\[
\boxed{d_{\min}+N>D.}
\tag{PA.21}
\]
If this inequality holds, then either \(W=0\), or (PA.9) gives \(B=0\). Thus \(F(t)=I_W\) for every \(t\), proving the group law. Conversely, assume \(W\ne0\) and the group law. Differentiate it with respect to \(t\) at \(t=0\). The polynomial formulas justify differentiation exactly and give \(F'(s)=F(s)F'(0)=0\). Hence \(F\) is constant and equal to \(I_W\). Its coefficient of \(t^N\) in (PA.19) is \(B/N!\), so \(B=0\). By (PA.9), this is equivalent to (PA.21). If \(W=0\), then \(d_{\min}>D\) already implies (PA.21).

The exact departure-and-return expression is
\[
F(s+t)-F(s)F(t)
=\left(E_0\exp(sT)(I_V-E_0)\exp(tT)E_0\right)|_W.
\tag{PA.22}
\]
Indeed, \(\exp((s+t)T)=\exp(sT)\exp(tT)\) follows by grouping the finite sums by total degree and applying the binomial formula. Inserting \(I_V=E_0+(I_V-E_0)\) between the factors yields (PA.22).

For \(W\ne0\), expansion and (PA.6) give
\[
\begin{aligned}
F(s+t)-F(s)F(t)
&=\sum_{r=1}^{R}
\left(
\frac{(s+t)^{rN}}{(rN)!}
-\sum_{a=0}^r
\frac{s^{aN}t^{(r-a)N}}{(aN)!((r-a)N)!}
\right)B^r\\
&=\sum_{r=1}^{R}
\left(
\sum_{\substack{1\leq p\leq rN-1\\N\nmid p}}
\frac{s^pt^{rN-p}}{p!(rN-p)!}
\right)B^r.
\end{aligned}
\tag{PA.23}
\]
The lowest potentially nonzero total degree in \(s,t\) is \(N\), with term
\[
\frac{(s+t)^N-s^N-t^N}{N!}\,B.
\tag{PA.24}
\]
If \(B\ne0\), this polynomial is nonzero: the coefficient of \(s\,t^{N-1}\) is \(B/(N-1)!\). Terms of degree \(2N\) or higher cannot cancel it. More strongly, (PA.22) is nonzero for every pair of positive real numbers \(s,t\). Choose a nonzero entry of \(B\) from a degree \(d_{\min}\) input to a degree \(d_{\min}+N\) output using (PA.9). For those particular basis indices every \(B^r\) with \(r\geq2\) has zero entry because it raises degree by \(rN\). Thus that entry of (PA.23) is the nonzero \(B\)-entry times the strictly positive scalar in (PA.24).

The first return has the exact factorization
\[
E_0T^NE_0
=E_0T(I_V-E_0)T(I_V-E_0)\cdots T(I_V-E_0)TE_0,
\tag{PA.25}
\]
with \(N\) factors \(T\) and \(N-1\) factors \(I_V-E_0\). Starting from \(W\), the vector after \(j\) applications of \(T\) lies in the character-\(\zeta^j\) sector for \(1\leq j\leq N-1\). Each intermediate projector therefore acts as the identity on that vector, even if it is zero. The final projector retains the character-one sector reached after \(N\) steps. This proves an identity of the original operators, including all truncated terms.

## 5. Exhaustive parameter classification and requested edge cases

By (PA.12), the group condition is equivalently \(R\leq0\). Its exhaustive classification is
\[
\boxed{F\text{ is a one-parameter group}
\quad\Longleftrightarrow\quad
m=1,\ \text{or }k\in\{1,2\},\ \text{or }(m,k)=(2,4).}
\tag{PA.26}
\]
Proof: the cases \(m=1\) and \(k\leq2\) are calculated below. For \(m=2\), one has \(N=3\), \(D=k\), and \(d_{\min}\leq2\). The cases \(k=3\) and \(k=4\) give respectively \(d_{\min}+N=3\leq D=3\) and \(d_{\min}+N=5>D=4\). For \(k\geq5\), one has \(d_{\min}+N\leq5\leq D\), so the group law fails. If \(m=3\), \(k=3\) gives \(d_{\min}+N=1+4=5\leq6=D\); every \(k\geq4\) satisfies \(d_{\min}+N\leq7<8\leq D\). Finally, if \(m\geq4\) and \(k\geq3\), then
\[
d_{\min}+N\leq m+(m+1)=2m+1
\leq3m-3\leq k(m-1)=D.
\]
Thus no remaining case satisfies the group condition.

### The case \(k=1\)

For every \(m\geq1\), one has \(d_{\min}=m\), \(D=m-1\), and \(R=-1\). Hence \(W=0\), all compressed powers vanish, and the group law holds on the zero vector space. In particular the invariant sector does not contain the algebra unit when \(k=1\).

### The case \(m=1\), equivalently \(N=2\)

The original quotient is \(V=\mathbb C\), since every \(y_i=0\). Thus \(T=0\), \(D=0\), and \(g=(-1)^k I_V\). If \(k\) is even, \(d_{\min}=0\), \(W=\mathbb C\), \(R=0\), and \(F(t)=I_{\mathbb C}\). If \(k\) is odd, \(d_{\min}=1\), \(W=0\), and \(R=-1\). In both cases \(W\) is \(T\)-invariant, and every compressed power \(E_0T^{rN}E_0\), \(r\geq1\), is zero. There is no additional \(N=2\) case, because \(N=m+1\) is part of the fixed definition.

### The case \(k=2\)

For every \(m\geq1\), one has \(d_{\min}=m-1\), \(D=2m-2\), and \(R=0\). There is exactly one invariant degree, \(m-1\), and
\[
W=\operatorname{span}_{\mathbb C}
\{y_1^i y_2^{m-1-i}:0\leq i\leq m-1\},
\qquad\dim_{\mathbb C}W=m.
\tag{PA.27}
\]
The next invariant degree is \(2m>D\). Therefore every \(E_0T^{rN}E_0\), \(r\geq1\), vanishes and \(F(t)=I_W\).

Nevertheless, when \(m\geq2\), \(W\) is not \(T\)-invariant. The exact action is
\[
T(y_1^i y_2^{m-1-i})
=\mathbf1_{\{i\leq m-2\}}y_1^{i+1}y_2^{m-1-i}
+\mathbf1_{\{i\geq1\}}y_1^i y_2^{m-i}.
\tag{PA.28}
\]
The output has degree \(m\). To verify the kernel without identifying different degree spaces, let \(w_i=y_1^i y_2^{m-1-i}\) and \(z_j=y_1^j y_2^{m-j}\), \(1\leq j\leq m-1\). The coefficient of \(z_j\) in \(T(\sum_{i=0}^{m-1}c_iw_i)\) is \(c_{j-1}+c_j\). Hence the kernel equations are \(c_j=-c_{j-1}\) for every \(j\), and
\[
\ker(T|_W)
=\mathbb C\sum_{i=0}^{m-1}(-1)^i y_1^i y_2^{m-1-i},
\qquad
\operatorname{rank}(T|_W)=m-1.
\tag{PA.29}
\]
For \(m=1\), the same kernel formula gives the full one-dimensional space and rank zero; the list \((z_j)\) and the kernel equations are empty. Thus for \(k=2,m\geq2\), there are departures but no permitted return degree. This proves that failure of \(T\)-invariance does not by itself force failure of the compressed group law.

### The squarefree case \(m=2\), including the exceptional \(k=4\)

Here \(N=3\), \(D=k\), and every exponent is zero or one. A nonzero entry of \(T^q\) between monomials indexed by subsets \(A\subseteq B\subseteq\{1,\ldots,k\}\), with \(|B\setminus A|=q\), is exactly \(q!\). Thus
\[
E_0T^{3r}E_0\ne0
\quad\Longleftrightarrow\quad
(-k\bmod3)+3r\leq k.
\tag{PA.30}
\]
For \(k=4\), the invariant degree is only \(2\), so \(W\) has the six squarefree degree-two monomials as basis. One has \(T|_W\ne0\), but \(B=0\) and \(F(t)=I_W\).

For the smallest nontrivial return, \(m=2,k=3\), one has
\[
W=\operatorname{span}_{\mathbb C}\{1,Y\},\qquad
Y=y_1y_2y_3,\qquad
B(1)=6Y,\quad B(Y)=0.
\tag{PA.31}
\]
With the exact factorial retained,
\[
F(t)(1)=1+t^3Y,\qquad F(t)(Y)=Y,
\]
and
\[
\big(F(s+t)-F(s)F(t)\big)(1)
=\big((s+t)^3-s^3-t^3\big)Y
=3st(s+t)Y.
\tag{PA.32}
\]
This is a nonzero composition defect computed in the stated tensor algebra.

## 6. Scope, provenance, and independent review

The bounded assignment was: “Let N=m+1,m,k>=1, V=C[y1,..,yk]/(yi^m), T=sum multiplication yi, totalcapacityD=k(m-1). Grade character zeta^(k+|a|) on basis y^a, invariant projector E0. Derive exact nonzero criterion E0 T^(rN) E0≠0 iff d_min+rN<=D where d_min=(-k modN), for r>=1. Give full multinomial matrix entries and all edge cases k1,m1,N2,k2. Derive whether E0 space T-invariant, and whether compressed exp(tT) is a one-parameter group or fails due departures/returns.”

A separate agent independently derived the group law and invariance criteria without reading this text. Its results agree with (PA.9), (PA.12), (PA.16), (PA.21), and (PA.26), including the exceptional case \(m=2,k=4\). The proof here incorporates explicit arguments for every classification and edge case rather than relying on the review as evidence.

These results concern precisely the displayed character projection and its powers. They construct no new zeros of the Riemann zeta function and assert no contradiction to, or disproof of, the Riemann hypothesis.

## 7. Main tensor-module review receipt

Read equations TPR.1–34 of tensor_primary_review.tex in full, with the requested focused review of TPR.13–27. The subsequently recorded 17,618-byte module hash below includes the added TPR.35; this power audit certifies TPR.1–34, while the separate unit audit certifies the added TPR.35. The recorded complete module SHA-256 is

4da8ed2cc768770d5ff3328550365b2f422b4ca0d9a5c3c3d4ebf0b84db3778c.

No mathematical error was found. The following connections were checked exactly.

- TPR.18 is (PA.9), including the nonzero zeroth power when and only when the invariant space is nonzero.
- TPR.19–20 agree with (PA.11)–(PA.12), with the notation distinction that the main module calls the return operator \(R\) and its maximum nonzero exponent \(q_*\); this audit calls them \(B\) and \(R\), respectively.
- TPR.15 agrees with (PA.16), and TPR.25 is compatible with this classification: \(TQ_0\ne0\) does not force \(Q_0T^NQ_0\ne0\).
- In TPR.26, the proposed indices \(\alpha=(m-2,0,0)\) and \(\beta=(m-1,m-1,1)\) are permitted for every \(m\geq2\). Their prescribed character exponents are \(k+|\alpha|=N\) and \(k+|\beta|=2N\), and the increment is \((1,m-1,1)\). Therefore the exact power entry is \(N!/(m-1)!\), and the exponential entry is \(z^N/(m-1)!\), including \(m=2\).
- The period factor in TPR.22 is exactly \(u^q\). The displayed period conjugation contributes \(u^{1/N}\) to each degree-one step. An invariant return has \(qN\) steps, giving \((u^{1/N})^{qN}=u^q\) on the retained branch. The original marked coefficient formula TPR.21 has no such factor.
- TPR.27 and its adjoining argument correctly isolate \(k=2\) and \((m,k)=(2,4)\) among \(m,k\geq2\) as the cases with no positive return power.
- TPR.30 retains the coordinatewise increment bound for every individual unit monomial. TPR.31 is a finite inverse for the compressed unit; TPR.32 is the exact distinction between that inverse and compression of the full inverse. TPR.33–34 explicitly conjugate the projector through the complete source unit, rather than assuming it commutes with that projector.

As an additional finite check, direct iterative multiplication by \(T\), using dictionaries of integer monomial coefficients, was compared against (PA.4) for every invariant starting monomial and every power \(0\leq q\leq D\), over the 24 parameter pairs \(1\leq m\leq5\), \(1\leq k\leq6\) satisfying \(m^k\leq256\). All 2,296 vector-power comparisons and 1,184 retained matrix entries agreed exactly. The same run checked the dimension formula \((m^k+m(-1)^k)/(m+1)\), the return exponent, invariance classification, and group-law classification. These finite checks are supplementary; the unrestricted proofs are given above.
