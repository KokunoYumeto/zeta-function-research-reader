# Independent complete review of OW.30–OW.40

Review date: 13 September 2026. Reviewer: the independently delegated `ow40_extension_review` agent. This file records a proof review; no checker, numerical optimization, Lean, or PDF build was run by this reviewer. Existing finite replay results are supplemental and are not premises of any argument below.

## Exact source editions and review scope

The complete text of OW.30–OW.40 was read, together with the necessary original definitions, signed minor calculation, optimizer classification and evaluation in OW.1–OW.29. The complete R48 addition was read. The original coordinate, quotient, least-lift and comparison definitions AU.1–AU.11 were also checked directly. No primary TeX file was edited.

| File | SHA-256 at review |
|---|---|
| `work/au_weight_optimizer_20260913.tex` | `677482a95ecbeafecf26f898f7426fb74ba31a5375cbe8862551e2c1a78e0952` |
| `work/endpoint_weight_conclusion_addition_20260913.tex` | `c9c45be0d16c51795794b665bbdc8d2670fe7102714b1d821f5167c20f719ba5` |
| `work/arithmetic_volume_upper_route_20260913.tex` | `21aaedc3585887fa7d2cb3e37e68d14415829a4b213566f7a08f4619835ef38b` |

Verdict: OW.30–OW.40 are correct at the pinned source edition. Their statements and exact comparison formulas are faithfully propagated into the pinned R48. No mathematical correction is required. The detailed derivation below includes the source and target of each map, the boundary passage, the mass and factorial accounting, and the precise extent of the asymptotic assertion.

## 1. Original objects, coordinates, kernels, and determinant orientation

Keep the original $g=2\xi$, the complete monic packet polynomial $h$,

\[
w_h(t)=\frac{|(g/h)(1/2+it)|^2}{2\pi},\qquad
m_k=w_h^{*k},\qquad \mu_h=\int_{\mathbb R}w_h(t)\,dt,
\qquad c=k/2.
\]

The arithmetic comparison in OW.25 is for $k\ge3$. The finite determinant arguments below hold for each declared $q\ge1$. At the arithmetic quartet, $q=[1+k(m-1)](k+1)^2$, with fixed complete common multiplicity $m\ge1$.

The source substitution is the ring isomorphism

\[
\Psi:\mathbb C[S]\longrightarrow\mathbb C[u],\qquad
P(S)\longmapsto P(c+iu),\qquad
\Psi^{-1}f=f((S-c)/i).
\]

It carries multiplication by $S$ to $c+iM_u$. Its order-$d$ derivative is $i^d\Psi(P^{(d)})$. Its degree-$N$ coefficient matrix is triangular with diagonal $1,i,\ldots,i^N$, so its determinant has modulus one. Thus the determinant of the transported quotient metric equals the original quotient volume; the substitution does not rescale the source mass.

For the original monic degree-$q$ relation,

\[
\psi(u)=i^{-q}\chi(c+iu)=\sum_{j=0}^q\psi_j u^j,
\qquad \psi_q=1,
\qquad \psi_j=\frac{i^{j-q}}{j!}\chi^{(j)}(c).
\]

Let $P_N=\mathbb C[u]_{\le N}$, with its ordered monomial coefficient space $\mathbb C^{N+1}$, and let $\mathcal E=\mathbb C[u]/(\psi)$ with its ordered remainder basis $1,u,\ldots,u^{q-1}$. Monic remainder is the surjective map

\[
J_N:\mathbb C^{N+1}\longrightarrow\mathbb C^q,
\qquad N\ge q-1.
\]

The raw derivative map $E_N:\mathbb C^{N+1}\to\mathbb C^q_{\mathrm{raw}}$ retains every root and every derivative order strictly below its original length. Its kernel is exactly the coefficient space of $(\psi)\cap P_N$, since vanishing of those raw derivatives is equivalent to divisibility by every corresponding prime power. Therefore $Z=E_{q-1}$ is invertible and

\[
E_N=ZJ_N.
\]

The source matrix is

\[
(H_N)_{ab}=\int_{\mathbb R}u^{a+b}m_k(u)\,du,
\qquad 0\le a,b\le N.
\]

The source form is conjugate-linear in its first argument: for coefficients $p$, its squared norm is $p^*H_Np$. Positivity of the density and the finite zero set of a nonzero polynomial imply $H_N>0$. Define

\[
K_N=J_NH_N^{-1}J_N^*,\quad
G_N=K_N^{-1},\quad V_N=\det G_N,
\quad K_N^{\mathrm{raw}}=E_NH_N^{-1}E_N^*.
\]

Surjectivity of $J_N$ makes $K_N>0$. The least-lift map

\[
R_N=H_N^{-1}J_N^*G_N:\mathbb C^q\longrightarrow\mathbb C^{N+1}
\]

satisfies $J_NR_N=I$. If $v\in\ker J_N$, then $v^*H_NR_Nx=v^*J_N^*G_Nx=0$. Hence every lift $R_Nx+v$ has squared norm $x^*G_Nx+v^*H_Nv$. This proves that $G_N$ is precisely the original minimum quotient form.

The raw-kernel identity and its determinant consequence are

\[
K_N^{\mathrm{raw}}=ZK_NZ^*,\qquad
\det K_N^{\mathrm{raw}}=\frac{|\det Z|^2}{V_N},\qquad
C_k=\log(V_q/V_{2q-1})
=\log\det K_{2q-1}^{\mathrm{raw}}-\log\det K_q^{\mathrm{raw}}.
\]

This fixes which raw kernel is the numerator and which is the denominator in every later estimate.

The exact comparator is

\[
d\nu_k(u)=c_h\vartheta_h^{k-3}e^{-(\pi/2)(k-3)}
e^{-(\pi/2)|u|}(k-2+|u|)^{-(42+2\deg h)}\,du.
\]

The previously proved lower-envelope inequality gives $d\nu_k\le m_k(u)\,du$. The identity on polynomials is consequently a contraction from the original source to the comparison source. In ordered monomials this says $H_N^\nu\preceq H_N$, and inversion gives

\[
K_N^{\mathrm{raw}}\preceq K_N^{\nu,\mathrm{raw}}.
\]

No changes to the comparator constants or its literal mass occur in OW.30–OW.40. For positive definite $A\preceq B$, the eigenvalues of $B^{-1/2}AB^{-1/2}$ lie in $(0,1]$. Its determinant is at most one, proving $\det A\le\det B$. The same eigenvalue argument, followed by congruence, proves order reversal on inversion. These are the determinant-order facts used below.

## 2. Signed minors and all factorials before determinant comparison

For the increasing column order, write

\[
\Delta_j=\det E_q[:,\{0,\ldots,q\}\setminus\{j\}].
\]

The vector with entries $(-1)^j\Delta_j$ lies in $\ker E_q$: append a row of $E_q$ as the final row of a square matrix and expand the resulting zero determinant. This kernel is one-dimensional, spanned by the coefficient vector of $\psi$. At its last coordinate $\Delta_q=\det Z$, so

\[
\Delta_j=(-1)^{q-j}\psi_j\det Z.
\]

In particular $\psi_j=0$ gives a zero minor on the original full matrix, retaining every column and raw-jet row. The confluent determinant itself retains

\[
\det Z=
\left(\prod_a\prod_{d=0}^{\ell_a-1}d!\right)
\prod_{a<a'}(\zeta_{a'}-\zeta_a)^{\ell_a\ell_{a'}}.
\]

Thus the raw derivative factorials and root ordering have not been discarded. For any nonnegative diagonal list $r_j$, Cauchy–Binet, or direct multilinear determinant expansion, gives

\[
\det(E_q\operatorname{diag}(r_j)E_q^*)
=\sum_{j=0}^q|\Delta_j|^2\prod_{l\ne j}r_l
=|\det Z|^2\sum_{j=0}^q|\psi_j|^2\prod_{l\ne j}r_l.
\]

The signs and phases were fixed before taking the squared absolute values. They remain recoverable through the displayed signed minors and the phase-preserving congruence OW.13.

Fix $0<b<\pi/2$ and retain

\[
\beta_j=\frac{b^{2j}}{(2j)!},\quad
B_\beta=\prod_{j=0}^q\beta_j,\quad
M_k=M_h(b)^k+M_h(-b)^k,
\quad M_h(b)=\int e^{bt}w_h(t)\,dt.
\]

Then

\[
\eta_j=\frac{|\psi_j|^2}{\beta_j}
=\frac{(2j)!}{(j!)^2b^{2j}}|\chi^{(j)}(c)|^2,
\qquad \eta_q=(2q)!b^{-2q}>0,
\]

and at the literal diagonal $r_j=\beta_j$,

\[
\det(E_q\operatorname{diag}(\beta_j)E_q^*)
=|\det Z|^2B_\beta\sum_{j=0}^q\eta_j.
\]

## 3. OW.30–OW.31: the joint even moment estimate

Put

\[
\mu_{2j}=\int_{\mathbb R}u^{2j}m_k(u)\,du,
\quad 0\le j\le q,
\qquad \mu_0=\mu_h^k,
\qquad S_q(b)=\sum_{j=0}^q\beta_j\mu_{2j}.
\]

The zeroth identity follows by iterated integration of the original nonnegative convolution. Every moment is strictly positive because $m_k>0$ almost everywhere and $u^{2j}>0$ away from zero. Finiteness follows from the finite original Laplace values and the nonnegative even exponential series. More explicitly,

\[
\int\cosh(bu)m_k(u)\,du
=\frac12\left(\int e^{bu}m_k(u)\,du+
\int e^{-bu}m_k(u)\,du\right)=\frac{M_k}{2}.
\]

For each sign, inserting $u=t_1+\cdots+t_k$ gives the product of the $k$ literal $M_h(\pm b)$. The integrands are nonnegative, so Tonelli justifies this identity before finiteness is invoked. The factor $1/2$ comes exactly from the definition of $\cosh$, with both Laplace values retained.

To make the Cauchy–Schwarz map explicit, define the coefficient isomorphism

\[
C_\beta:\mathbb C^{q+1}\longrightarrow\mathbb C^{q+1},
\qquad (p_j)\longmapsto(p_j/\sqrt{\beta_j}),
\]

and for real $u$ define the row functional

\[
e_\beta(u)(a)=\sum_{j=0}^q\sqrt{\beta_j}\,u^ja_j.
\]

Then $e_\beta(u)C_\beta p=\sum p_ju^j$, and the squared operator norm of $e_\beta(u)$ in the standard Hermitian coefficient space is $\sum\beta_ju^{2j}$. Consequently

\[
\left|\sum p_ju^j\right|^2
\le\left(\sum\frac{|p_j|^2}{\beta_j}\right)
\left(\sum\beta_ju^{2j}\right).
\]

Integration gives $H_q\preceq S_q(b)\operatorname{diag}(\beta_j^{-1})$. The tail

\[
\cosh(bu)-\sum_{j=0}^q\beta_ju^{2j}
=\sum_{j=q+1}^{\infty}\frac{b^{2j}u^{2j}}{(2j)!}
\]

is positive for every $u\ne0$. Its integral against the positive original density is strictly positive. Therefore

\[
0<S_q(b)<M_k/2,
\qquad
H_q\preceq S_q(b)\operatorname{diag}(\beta_j^{-1})
\prec(M_k/2)\operatorname{diag}(\beta_j^{-1}).
\]

The strict matrix inequality concerns the two diagonal matrices: their difference is the positive scalar $M_k/2-S_q(b)$ times the positive definite diagonal matrix. It does not require equality analysis of the first Cauchy–Schwarz inequality.

## 4. OW.32–OW.33: determinant transport and the exact gain

Inverting the preceding source inequality and applying $E_q$ gives

\[
K_q^{\mathrm{raw}}\succeq
S_q(b)^{-1}E_q\operatorname{diag}(\beta_j)E_q^*.
\]

The right side is positive definite because $E_q$ has full row rank. Taking determinants and using Section 2 gives

\[
\det K_q^{\mathrm{raw}}\ge
S_q(b)^{-q}|\det Z|^2B_\beta\sum_j\eta_j.
\]

The numerator estimate from Section 1 is

\[
\det K_{2q-1}^{\mathrm{raw}}
\le\frac{|\det Z|^2}{V_{2q-1}^\nu}.
\]

Taking the logarithm of the numerator divided by the denominator, after these exact identities are established, yields

\[
C_k\le\mathcal U_{\mathrm{fin}}
=q\log S_q(b)-\log B_\beta-\log\sum_j\eta_j
-\log V_{2q-1}^\nu.
\]

Replacing $S_q(b)$ by $M_k/2$ gives $\mathcal U_{\mathrm{cosh}}$, and

\[
\mathcal U_{\mathrm{cosh}}-\mathcal U_{\mathrm{fin}}
=q\log\frac{M_k}{2S_q(b)}>0.
\]

For the earlier family, with its own simplex weights,

\[
\mathcal U_{\mathrm{eq}}
=q\log M_k-\log B_\beta
-\log\frac{\sum_j\eta_j}{(q+1)^q}
-\log V_{2q-1}^\nu,
\]

so direct subtraction gives exactly

\[
\mathcal U_{\mathrm{eq}}-\mathcal U_{\mathrm{cosh}}
=q\log(2(q+1)).
\]

Writing the earlier optimization gain as

\[
\mathfrak g(\eta)
=\log\frac{d(\eta)}{\sum_j\eta_j/(q+1)^q}
=\mathcal U_{\mathrm{eq}}-\mathcal U_{\mathrm{opt}},
\]

one obtains

\[
\mathcal U_{\mathrm{opt}}-\mathcal U_{\mathrm{fin}}
=q\log(2(q+1))-\mathfrak g(\eta)
+q\log\frac{M_k}{2S_q(b)}.
\]

The earlier bound $0\le\mathfrak g(\eta)\le q\log(1+1/q)<1$ is sufficient: $q\log(2(q+1))\ge\log4>1$ for every $q\ge1$. The last term is strictly positive. Thus the claimed improvement over the earlier optimum is strict, including $q=1$.

## 5. OW.34–OW.36: the entire declared positive diagonal family

For an arbitrary list $r=(r_0,\ldots,r_q)\in\mathbb R_{>0}^{q+1}$, replace $\beta$ by $r$ in the maps $C_\beta,e_\beta(u)$ of Section 3. This gives, on precisely the same polynomial source,

\[
H_q\preceq s(r)\operatorname{diag}(r_j^{-1}),
\qquad s(r)=\sum_{j=0}^qr_j\mu_{2j}>0,
\]

and hence

\[
K_q^{\mathrm{raw}}\succeq
E_q\operatorname{diag}(r_j/s(r))E_q^*.
\]

Every source coefficient, moment, and raw-jet row is the original one. The weight map is the bijection

\[
\mathbb R_{>0}^{q+1}\longrightarrow
(0,\infty)\times\mathcal S_q^\circ,
\quad r\longmapsto\left(s(r),t_j=\frac{r_j\mu_{2j}}{s(r)}\right),
\]

where $\mathcal S_q^\circ=\{t_j>0:\sum t_j=1\}$. Its inverse is $r_j=st_j/\mu_{2j}$. Substitution gives $\sum r_j\mu_{2j}=s\sum t_j=s$, and then recovers $t_j$; the opposite composite recovers each $r_j$. All divisions use strictly positive actual moments. This changes auxiliary variables only; the original source measure is untouched.

Set $\kappa_j=|\psi_j|^2\mu_{2j}$, so $\kappa_q=\mu_{2q}>0$, and retain

\[
D_\kappa(t)=\sum_{j=0}^q\kappa_j\prod_{l\ne j}t_l.
\]

The determinant calculation is termwise:

\[
\begin{aligned}
\frac{\det(E_q\operatorname{diag}(r_j)E_q^*)}{s(r)^q}
&=|\det Z|^2\sum_{j=0}^q|\psi_j|^2
\prod_{l\ne j}\frac{r_l}{s(r)}\\
&=|\det Z|^2\sum_{j=0}^q|\psi_j|^2
\prod_{l\ne j}\frac{t_l}{\mu_{2l}}\\
&=|\det Z|^2
\left(\prod_{l=0}^q\mu_{2l}^{-1}\right)D_\kappa(t).
\end{aligned}
\]

There are $q+1$ factors in the common moment product. The omitted factor in the $j$-th degree-$q$ term is restored exactly by $\mu_{2j}$ in $\kappa_j$. In particular the full zeroth moment $\mu_h^k$ remains present. As a homogeneity check on this identity, multiplying every source moment by a scalar $a>0$ multiplies $\prod\mu_{2j}$ by $a^{q+1}$ and $d(\kappa)$ by $a$; their ratio therefore scales by $a^q$, exactly the determinant degree of the $q$-dimensional quotient metric. This calculation introduces no rescaling of the actual source.

## 6. Optimizer dependencies and the boundary passage in OW.37

The polynomial optimization applies because $\kappa_j\ge0$ and $\kappa_q>0$. Its value is positive at the equal simplex point. Compactness therefore provides $d(\kappa)=\max_{t\in\mathcal S_q}D_\kappa(t)>0$.

For completeness, the required complete classification follows from the same exact determinant model used in OW.9. Put $v_i=\sqrt{\kappa_i/\kappa_q}$ for $i<q$ and

\[
M(t)=\operatorname{diag}(t_0,\ldots,t_{q-1})+t_qvv^*,
\qquad D_\kappa(t)=\kappa_q\det M(t).
\]

The rank-one determinant expansion proves the identity for positive first $q$ coordinates; equality of polynomials extends it to every boundary point. On its positive domain, $\log D_\kappa$ is concave: along a real affine increment $E$, its second derivative is $-\operatorname{Tr}((M^{-1/2}EM^{-1/2})^2)\le0$. If at least three coefficients are positive, two entries of $v$ are nonzero. Their off-diagonal matrix entry detects an increment of $t_q$, and then the diagonal entries detect every remaining increment. Thus the affine matrix map is injective and the concavity is strict.

A point with two zero coordinates has objective zero. A positive boundary maximum has exactly one zero coordinate $t_j=0$. Its value is $\kappa_j\prod_{i\ne j}t_i$, maximized on that face precisely at the other weights $1/q$. The active partial derivatives there are $\kappa_j/q^{q-1}$, and the inactive derivative is $(\sum_i\kappa_i-\kappa_j)/q^{q-1}$. Concavity proves this point is globally maximal exactly when $\kappa_j\ge\sum_{i\ne j}\kappa_i$. If exactly two positive coefficients are equal, the factorization

\[
D_\kappa(t)=\left(\prod_{i\notin\{j,l\}}t_i\right)
\bigl(\kappa_jt_l+\kappa_lt_j\bigr).
\]

This gives exactly the maximizing segment $t_j+t_l=1/q$, with every other coordinate $1/q$. For unequal positive coefficients this allocation has a unique maximizing endpoint. With only one positive coefficient the product maximum is unique. For $q=1$, the polynomial is directly linear and its maximum is the larger coefficient, or every simplex point when they are equal.

If every coefficient is smaller than the sum of the others, there is no positive boundary maximum. The maximizer is the unique interior point. With $P=\prod t_i$ and $S=\sum\kappa_i/t_i$, differentiation of $D=PS$ and Euler's degree-$q$ identity give

\[
\kappa_i=St_i(1-qt_i).
\]

Zero coefficients therefore have $t_i=1/q$. At positive coefficients $y_i=1-qt_i$ satisfies $\sum y_i=1$, $0<y_i<1$, and $\kappa_i=c_*y_i(1-y_i)$, where $c_*=S/q$. At most one $y_i$ exceeds $1/2$; if one does, its coefficient is the unique largest one. The smaller roots are

\[
f_i(t)=\frac{1-\sqrt{1-\kappa_it}}2,
\qquad t=4/c_*\in(0,1/\max\kappa_i].
\]

Their sum is strictly increasing. If its value at the right endpoint is at least one, its unique crossing of one determines all $y_i$. Otherwise the unique largest index $j$ uses $1-f_j$, and dividing $\sum_{i\ne j}f_i=f_j$ by its positive right side gives the strictly decreasing scalar function in OW.17. Its left endpoint is greater than one and its right endpoint less than one; this determines its unique root. Direct multiplication gives $d(\kappa)=4(q^qt_*)^{-1}\prod_{i:\kappa_i>0}(1-y_i)$. Thus the earlier complete optimizer applies to the literal moment coefficients, with all their zero cases.

The coefficient Lipschitz bound and gradient certificate in OW.22–OW.22a are valid at these same boundary points: $D>0$ means $M>0$, so $\log D$ has a gradient on a neighborhood of the point. For any simplex candidate set $h=\max_i\partial_iD-qD\ge0$. The tangent inequality for $\log D$ gives $d\le D\exp(h/D)$, and $h<D$ gives $d\le D^2/(D-h)$. These statements permit certified approximation of the optimum without an unsupported choice at a radical equality. No arithmetic growth estimate is inferred from the finite optimizer.

For every positive $t$, Sections 1 and 5 yield

\[
C_k\le\sum_{j=0}^q\log\mu_{2j}
-\log D_\kappa(t)-\log V_{2q-1}^\nu.
\]

At a maximizing boundary point $t^*$, define

\[
t^\varepsilon=(1-\varepsilon)t^*+\varepsilon(1/(q+1),\ldots,1/(q+1)),
\quad r_j^\varepsilon=t_j^\varepsilon/\mu_{2j},
\quad 0<\varepsilon<1.
\]

Then $s(r^\varepsilon)=1$ and the proven inequality is

\[
K_q^{\mathrm{raw}}\succeq
E_q\operatorname{diag}(t_j^\varepsilon/\mu_{2j})E_q^*.
\]

Taking each quadratic form's limit preserves the inequality. The limiting right matrix is positive semidefinite and has determinant

\[
|\det Z|^2\left(\prod_j\mu_{2j}^{-1}\right)d(\kappa)>0,
\]

so it is positive definite. Its determinant and logarithm are therefore continuous at the limit. This proves

\[
C_k\le\mathcal U_{\mathrm{mom}}
=\sum_{j=0}^q\log\mu_{2j}-\log d(\kappa)-\log V_{2q-1}^\nu.
\]

The infimum over the entire declared family OW.34 equals this expression because the open simplex is dense in the closed simplex, $D_\kappa$ is continuous, and the positive maximum can be approached by the displayed positive regularization. At no point is $1/t_j^*$ or $1/r_j^*$ evaluated at a zero coordinate.

## 7. OW.38–OW.39: the exact reference point and its gain

The finite even-series diagonal $r_j=\beta_j$ corresponds exactly to

\[
t_j^\beta=\frac{\beta_j\mu_{2j}}{S_q(b)}.
\]

Substitution into each monomial gives

\[
\begin{aligned}
D_\kappa(t^\beta)
&=\sum_j |\psi_j|^2\mu_{2j}
\prod_{l\ne j}\frac{\beta_l\mu_{2l}}{S_q(b)}\\
&=\left(\prod_{l=0}^q\mu_{2l}\right)
\frac{B_\beta\sum_j\eta_j}{S_q(b)^q}>0.
\end{aligned}
\]

It follows that

\[
\mathcal U_{\mathrm{fin}}-\mathcal U_{\mathrm{mom}}
=\log\frac{d(\kappa)}{D_\kappa(t^\beta)}\ge0,
\]

and, combining this with Section 4,

\[
\mathcal U_{\mathrm{opt}}-\mathcal U_{\mathrm{mom}}
=q\log(2(q+1))-\mathfrak g(\eta)
+q\log\frac{M_k}{2S_q(b)}
+\log\frac{d(\kappa)}{D_\kappa(t^\beta)}.
\]

The previous bound smaller than one applies to the improvement from the equal simplex point for the same coefficient list. The reference point $t^\beta$ is instead the explicit, generally nonuniform image of the original finite-series diagonal. The exact map above and the displayed difference formula relate these reference points; they do not identify their gains. OW.39 correctly leaves the last term as its actual nonnegative value and assigns no smaller-than-one bound to it.

## 8. The exact $q\log q$ term and the limits actually proved

The removed term from $\mathcal U_{\mathrm{eq}}$ to $\mathcal U_{\mathrm{cosh}}$ is exactly $q\log(2(q+1))$. Its ratio to $q\log q$ tends to one as $q\to\infty$. For the quartet degree,

\[
\frac{q\log(2(q+1))}{q\log k}
=\frac{\log(2(q+1))}{\log k}.
\]

If $m=1$, then $q=(k+1)^2$, so this tends to two. If fixed $m>1$, then

\[
q/k^3=(m-1+1/k)(1+1/k)^2\longrightarrow m-1>0,
\]

so the ratio tends to three. Also $q\log(2(q+1))/q^2=\log(2(q+1))/q\to0$.

These limits concern the exact displayed term. The additional moment gain, the nonuniform reference-point gain, and the comparison determinant remain in the exact identity of Section 7. The source text and R48 do not infer their growth from these limits. In particular they do not transfer the removed term to AU's separate interval scalar estimate by an unproved equality. The complete valid arithmetic consequence is the source/quotient inequality proved in Sections 3–7.

## 9. OW.40: the full moment matrix and its Schur-complement loss

Let $\boldsymbol\psi=(\psi_0,\ldots,\psi_q)^T$ and let $T:\mathbb C^q\oplus\mathbb C\to\mathbb C^{q+1}$ send $(x,t)$ to the coefficients of

\[
\sum_{j=0}^{q-1}x_ju^j+t\psi(u).
\]

Its block matrix is

\[
T=\begin{pmatrix}I_q&\psi_{<q}\\0&1\end{pmatrix},
\qquad \det T=1,\qquad J_qT=(I_q,0).
\]

Thus this is a specified coefficient isomorphism, and the image of its last coordinate line is exactly the full degree-$q$ relation kernel. Write

\[
T^*H_qT=\begin{pmatrix}A&b\\b^*&d\end{pmatrix},
\qquad d=\boldsymbol\psi^*H_q\boldsymbol\psi>0.
\]

For every $x\in\mathbb C^q$ and $t\in\mathbb C$, completion of the scalar square gives

\[
\begin{pmatrix}x\\t\end{pmatrix}^*
T^*H_qT\begin{pmatrix}x\\t\end{pmatrix}
=x^*(A-bd^{-1}b^*)x
+d\left|t+d^{-1}b^*x\right|^2.
\]

The minimum among all lifts of $x$ is attained uniquely at $t=-d^{-1}b^*x$. By the already proved least-lift characterization, $G_q=A-bd^{-1}b^*$. Elementary block elimination has determinant one and gives

\[
\det(T^*H_qT)=d\det G_q.
\]

Since $\det T=1$, this proves exactly

\[
V_q=\frac{\det H_q}{\boldsymbol\psi^*H_q\boldsymbol\psi}.
\]

The boundary raw-kernel inequality established in Section 6 gives

\[
\frac{|\det Z|^2}{V_q}
\ge |\det Z|^2\left(\prod_{j=0}^q\mu_{2j}^{-1}\right)d(\kappa).
\]

Invertibility of $Z$ permits the stated cancellation. Equivalently,

\[
V_q\le\frac{\prod_{j=0}^q\mu_{2j}}{d(\kappa)}.
\]

Therefore, setting $\mathcal U_{\mathrm{low}}=\log V_q-\log V_{2q-1}^\nu$,

\[
\begin{aligned}
0\le\mathcal U_{\mathrm{mom}}-\mathcal U_{\mathrm{low}}
&=\sum_{j=0}^q\log\mu_{2j}-\log d(\kappa)-\log V_q\\
&=\sum_{j=0}^q\log\mu_{2j}-\log d(\kappa)
-\log\det H_q+\log(\boldsymbol\psi^*H_q\boldsymbol\psi).
\end{aligned}
\]

The numerator comparison also implies $V_{2q-1}^\nu\le V_{2q-1}$, hence $C_k\le\mathcal U_{\mathrm{low}}$. This verifies both directions of the OW.40 comparison, without a sign reversal.

Every entry of $H_q$ is the actual moment of order $a+b\le2q$. The scalar $\boldsymbol\psi^*H_q\boldsymbol\psi$ uses all mixed coefficient terms and their complex conjugates. No odd moment is dropped from $H_q$, and no orthogonality of its monomial columns is assumed. The diagonal-family optimum and the full source kernel are related by the original raw map and the exact displayed nonnegative determinant loss. An estimate on the growth of that loss is not supplied or assumed.

## 10. R48 propagation and review completion

The pinned R48 preserves the signed cofactor map, the coefficient factorials, the old-family optimization domain, and its smaller-than-one gain. Its joint-moment matrix inequality includes the factor $M_k/2$, the strict finite-sum inequality, and $\mu_0=\mu_h^k$. Its weight map is precisely OW.35, and its optimized expression retains all $q+1$ moment factors. Its total gain equals Section 7 term for term. Its stated limits concern the removed term and match Section 8. Its final nonnegative loss equals the complete Schur-complement calculation in Section 9.

No new hypothesis, arithmetic estimate, shortened jet space, discarded relation, or source rescaling is introduced by the reviewed extension. The finite source and quotient calculations are fully proved. The earlier AU analytic comparator is used with its existing constants and declared scope. The review supports the mathematical integration of the pinned OW.30–OW.40 and R48; it makes no claim about later source editions, PDF layout, execution receipts, or unproved arithmetic asymptotics.
