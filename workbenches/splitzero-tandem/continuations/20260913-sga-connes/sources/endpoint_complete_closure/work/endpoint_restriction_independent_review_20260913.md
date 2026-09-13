# Independent mathematical review of canonical endpoint restriction

Date: 2026-09-13. The complete NOTE.tex and RESEARCH_NOTE.md in
sources/web_endpoint_restriction_delivery/Tau_Endpoint_Restriction_Control
were read. Their retained source pins are:

- NOTE.tex: 33,850 bytes, 962 lines, SHA-256
  ff4cc53cb4d3b10a9547a8a2365db7fd5d874bf1ecf7dd8542b8d1f05f433ef6.
- RESEARCH_NOTE.md: 30,508 bytes, 638 lines, SHA-256
  905ad0dcd20a2630eb6338488206a387265223590a527f867c1266b85bb27491.

The finite operator identities, all trace-certificate orders, and the exact
Gaussian comparison are correct. No tests, compiler, or Lean process were
run by this review, and no raw source was edited. Earlier theta primitives
and the arithmetic norm theorem are retained inputs, not newly certified
by these finite calculations.

Two endpoint conventions must accompany reuse of the formulas. The scalar
formula (50) with denominator $(1-g_0)^2$ uses $0<g_0<1$; at $g_0=1$
the source's preceding branch gives $H=0$ and $U_p=0$. The decimals in (65)
are rounded observations slightly below the exact upper-certificate values.
The source explicitly reserves certification to exact logarithmic enclosures;
its total bound below $2.469887624578038$ is valid.

The exterior conventions and rectangular exterior image require explicit
maps, supplied in Sections 6 and 7 below. In particular the unscaled
alternating tensor map has squared norm factor $q!$, and a rectangular
exterior map is evaluated on the domain determinant generator before it is
identified with a target vector. The raw projection in (24) is already an
endomorphism of the larger polynomial space; its dimensions are retained
in Section 2.

## 1. Original source, quotient, and minimum lift

Fix $q\ge1$ and admitted degrees $q-1\le i\le j$. Retain the coordinate
$S=k/2+iu$, original density, and unscaled monic orthogonal polynomials $p_a$
with squared norms $\omega_a>0$. The original constant norm is
$\omega_0=\mu_h^k$. On $\mathcal P_N=\mathbb C[S]_{\le N}$ use its diagonal
Gram $O_N=\operatorname{diag}(\omega_0,\ldots,\omega_N)$.
The relation space is $\mathcal D_N=\chi\mathcal P_{N-q}$, zero at
$N=q-1$. Euclidean division gives the exact quotient map $B_N$ with
columns $b_a=[p_a]_\chi$ in the fixed quotient basis.

The dimensions are $O_N:(N+1)\times(N+1)$,
$B_N:q\times(N+1)$, $K_N,G_N:q\times q$, and
$R_N:(N+1)\times q$. Since $B_N$ is onto, $B_N^*$ is injective and

\[
u^*K_Nu=u^*B_NO_N^{-1}B_N^*u>0\quad(u\ne0).
\]

Thus $K_N=B_NO_N^{-1}B_N^*$ and $G_N=K_N^{-1}$ are positive Hermitian.
For $R_N=O_N^{-1}B_N^*G_N$, direct multiplication proves

\[
B_NR_N=I,\qquad R_N^*O_NR_N=G_N,\qquad
z^*O_NR_N=0\quad(z\in\ker B_N).
\]

Every representative of $u$ has the form $R_Nu+z$ with $z\in\mathcal D_N$,
so its squared norm is $u^*G_Nu+z^*O_Nz$. This proves the minimum property
and uniqueness in the original source form. Both $\operatorname{im}R_N$
and $\mathcal D_N^\perp$ have dimension $q$, so they are equal.

## 2. Padding, projection, and the metric adjoint

The inclusion $L=L_{i,j}:\mathcal P_i\to\mathcal P_j$ is the
$(j+1)\times(i+1)$ padding matrix
$(I_{i+1},0)^T$. It obeys $L^*O_jL=O_i$ and $B_jL=B_i$.
Its metric adjoint is

\[
L^\dagger=O_i^{-1}L^*O_j=L^*:\mathcal P_j\to\mathcal P_i.
\]

The equality follows because the first $i+1$ weights of $O_j$ are
exactly $O_i$. Consequently $P=P_{i,j}=LL^\dagger=LL^*$ is an
$O_j$-orthogonal projection with size $(j+1)\times(j+1)$, range
$L\mathcal P_i$ of dimension $i+1$, and kernel of dimension $j-i$.
The truncated coordinate map $L^\dagger$ and projection $P$ have the
different codomains stated here.

The forward coordinate identity $I:(E,G_i)\to(E,G_j)$ is contractive,
because $LR_i u$ is an admitted representative at degree $j$:

\[
u^*G_ju\le\|LR_i u\|_{O_j}^2=u^*G_i u.
\]

Also, directly from the added monic columns,

\[
K_j-K_i=\sum_{a=i+1}^j\frac{b_ab_a^*}{\omega_a}\succeq0.
\]

With inner product conjugate-linear in its first argument,

\[
\langle Iu,v\rangle_{G_j}=u^*G_jv
=u^*G_iK_iG_jv.
\]

Hence the metric adjoint, with its actual Hilbert types, is

\[
T=I^\dagger:(E,G_j)\to(E,G_i),\qquad T=K_iG_j,
\quad T^\dagger=I.
\]

Restriction of the actual canonical representative gives

\[
L^\dagger R_j=O_i^{-1}B_i^*G_j
=O_i^{-1}B_i^*G_iK_iG_j=R_iT.
\]

Its padded version is therefore the exact map identity

\[
\boxed{LR_iT=PR_j:E\to\mathcal P_j.}
\]

For $i\le j\le l$, $T_{i,j}T_{j,l}=K_iG_jK_jG_l=K_iG_l=T_{i,l}$,
as asserted. Each return is invertible, with $T_{i,j}^{-1}=K_jG_i$.

## 3. Canonical ranges and principal angles

Work in the common source $(\mathcal P_j,O_j)$ and put

\[
\mathcal C_i^{(j)}=\operatorname{im}(LR_i),\qquad
\mathcal C_j=\operatorname{im}R_j.
\]

Both have dimension $q$. The former is contained in the
$(i+1)$-dimensional space $L\mathcal P_i$ and is its orthogonal
complement to $L\mathcal D_i$. The maps $LR_i$ and $R_j$ are isometric
isomorphisms from the two original arithmetic Hilbert spaces to these
canonical ranges.

Invertibility of $T$ and the restriction formula show
$P(\mathcal C_j)=\mathcal C_i^{(j)}$. For $v\in\mathcal C_j$,
$v-Pv$ is orthogonal to $L\mathcal P_i$ and therefore to
$\mathcal C_i^{(j)}$. Hence the projection to the larger lower-degree
source and the projection to its canonical range agree on $\mathcal C_j$:

\[
P|_{\mathcal C_j}
=\Pi_{\mathcal C_i^{(j)}}|_{\mathcal C_j}
=(LR_i)T(R_j|_E)^{-1}.
\]

The actual ambient projection matrices are

\[
\Pi_{\mathcal C_i^{(j)}}=LR_iK_iR_i^*L^*O_j,\qquad
\Pi_{\mathcal C_j}=R_jK_jR_j^*O_j.
\]

Their idempotence follows from the lift Gram identities; their ranges
and weighted self-adjointness prove that they are the stated orthogonal
projections. Both matrices have size $(j+1)\times(j+1)$.

Since $LR_i u-R_j u$ is a relation in $\mathcal D_j$, the higher canonical
representative is its projection:
$\Pi_{\mathcal C_j}LR_i u=R_j u$.
Thus the adjoint of the restriction between the two canonical ranges is
$\Pi_{\mathcal C_j}|_{\mathcal C_i^{(j)}}$, corresponding exactly to $I$.

The coordinate endomorphism $T$ is positive self-adjoint in both endpoint
forms, since

\[
G_iT=G_j,\qquad G_jT=G_jK_iG_j
\]

are positive Hermitian. Moreover
$G_i(I-T)=G_i-G_j\succeq0$ and
$G_j(I-T)=G_j(K_j-K_i)G_j\succeq0$.
Its eigenvalues are therefore $g_a\in(0,1]$.
Because $I^\dagger I=T$, the squared singular values of $I$ are $g_a$.
The same singular values belong to its adjoint $T$ with reverse Hilbert
types, and to the source restriction just identified.

These are the squared cosines of the $q$ principal angles between
$\mathcal C_j$ and $\mathcal C_i^{(j)}$. They also give the $q$ principal
angles between $\mathcal C_j$ and $L\mathcal P_i$, since the projections
agree on $\mathcal C_j$ and $\min(q,i+1)=q$. This retains the full
projection dimension $i+1$ and the canonical dimension $q$.

Finally
$\operatorname{rank}(I-T)=\operatorname{rank}(K_j-K_i)\le\min(q,j-i)$,
so at most that many angles are nonzero. At $i=j$ all eigenvalues are one.

## 4. The action commutator with its two metrics

Retain the original arithmetic matrix $A$ and real integer $k$. Set

\[
W_N=A^*G_N+G_NA-kG_N,\quad
\mathsf H_N=K_NW_N,\quad
\mathsf V_N=AK_N+K_NA^*-kK_N.
\]

$W_N$ is Hermitian, hence $\mathsf H_N$ is self-adjoint in $G_N$.
The forward identity intertwines $A$ exactly. Expansion gives

\[
\begin{aligned}
\mathsf H_iT&=K_iA^*G_j+AK_iG_j-kK_iG_j,\\
T\mathsf H_j&=K_iA^*G_j+K_iG_jA-kK_iG_j.
\end{aligned}
\]

Their difference is $AT-TA$. Expanding
$\mathsf V_iG_j-K_iW_j$ cancels the same $K_iA^*G_j$ and $kK_iG_j$
terms, giving the same difference. This proves all three expressions in (27).

The cross-metric singular values of $T$ are $\sqrt{g_a}\le1$.
For $\epsilon_N=\|\mathsf H_N\|_{(E,G_N)\to(E,G_N)}$ as specified,

\[
\|AT-TA\|_{(E,G_j)\to(E,G_i)}
\le(\epsilon_i+\epsilon_j)\|T\|\le\epsilon_i+\epsilon_j.
\]

Each product uses its displayed source and target form. This is the exact
comparison with the arithmetic action; it supplies no automatic invariance
of a return eigenspace under $A$.

## 5. Relation correction, range, and its exact Gram

Put $H=I-T=(K_j-K_i)G_j$. The padded restriction identity gives

\[
\mathfrak d=LR_i-R_j
=LR_iH-(I-P)R_j.
\]

The first term has remainder $B_jLR_iH=H$. The second has remainder
$B_j(I-P)R_j=I-T=H$. Thus $B_j\mathfrak d=0$.
Both $LR_i u$ and $R_j u$ are orthogonal to $L\mathcal D_i$;
the latter uses $L\mathcal D_i\subseteq\mathcal D_j$. Therefore

\[
\operatorname{im}\mathfrak d
\subseteq\mathcal D_j\cap(L\mathcal D_i)^\perp.
\]

This is the common-space interpretation of source (31). The boundary
layer has dimension $j-i$, whereas the domain of $\mathfrak d$ has
dimension $q$; surjectivity onto that layer is not asserted.

Orthogonality of $R_j$ to every relation gives
$R_j^*O_jLR_i=G_j$, and taking the adjoint gives the other cross term.
Consequently

\[
\begin{aligned}
\mathfrak d^*O_j\mathfrak d
&=R_i^*L^*O_jLR_i-R_i^*L^*O_jR_j
-R_j^*O_jLR_i+R_j^*O_jR_j\\
&=G_i-G_j-G_j+G_j=G_i-G_j.
\end{aligned}
\]

This proves the full original source Gram. Its kernel is that of $I-T$,
because $G_i(I-T)=G_i-G_j$ and the source form is positive definite.
Thus the return eigenvalue one means precisely that the canonical
representative has not changed for that coordinate.

If $Tv=gv$, then $G_jv=gG_iv$ and

\[
\|PR_jv\|_{O_j}^2=g^2v^*G_iv,\qquad
\|R_jv\|_{O_j}^2=gv^*G_iv.
\]

The first ratio in (57) is $g$; orthogonality of $P$ gives the other
ratio $1-g$. Its lower-degree remainder is $gv$.
The exact recovery map for the original coordinate is
$LR_i=PR_jT^{-1}$, whose difference from $R_j$ is $\mathfrak d$.

For a single active fibre, complex-linear $F$ lifts to
$u^\bullet\mapsto(Fu)^\bullet$ and $\tau\mapsto\tau$.
In the standard single-fibre lift, active addition and multiplication
are inherited from vector addition and scalar multiplication.
Checking the cases of two active elements, one external element, and
two external elements proves that this lift is $G(\mathbb C)$-linear.
Applying it to $I$ and $T$ proves (32); its reverse composition is the
already proved return composition. Reduction of the labelled relation
$\mathfrak d v$ gives the supported zero at the receiving label, while
the external point stays external. The source relation and its full norm
remain in the displayed map before this reduction.

## 6. Determinant ratios, alternating tensors, and spectral counting

Directly,

\[
\det T=\frac{\det K_i}{\det K_j}=\frac{V_j}{V_i}
=\prod_ag_a>0,\qquad
\mathcal L_{i,j}=\log(V_i/V_j)=-\sum_a\log g_a.
\]

The usual exterior inner product assigns the fixed coefficient
determinant vector squared norm $V_N$. Its exact map to the unscaled
alternating tensor representative is

\[
\operatorname{Alt}_q(v_1\wedge\cdots\wedge v_q)
=\sum_{\sigma\in S_q}\operatorname{sgn}(\sigma)
v_{\sigma(1)}\otimes\cdots\otimes v_{\sigma(q)}.
\]

Expansion of its squared norm gives

\[
\sum_{\sigma,\tau}\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)
\prod_a\langle v_{\sigma(a)},v_{\tau(a)}\rangle
=q!\det[\langle v_a,v_b\rangle].
\]

For each fixed $\sigma$, reindexing $\tau$ gives the determinant, and
there are $q!$ choices of $\sigma$. Hence
$\operatorname{Alt}_q^*\operatorname{Alt}_q=q!I$.
This proves the exact factor relating the convention after source (34)
to the exterior Gram convention in (39). No factorial is discarded.

The coordinate scalar of $\bigwedge^qT$ is $\det T$. Its squared norm
between the actual reverse determinant Hilbert types is

\[
|\det T|^2\frac{q!V_i}{q!V_j}
=\frac{V_j}{V_i}=\prod_ag_a.
\]

The same result holds in the usual exterior convention via the map
$\operatorname{Alt}_q$ just proved.

For a scalar $g\in(0,1]$,

\[
\int_0^1\frac{\mathbf1_{\{g<t\}}}{t}\,dt
=\int_g^1\frac{dt}{t}=-\log g.
\]

Summing this finite list proves the first counting identity in (35).
Substituting $t=e^{-s}$, with its reversed limits, proves the second.
At $g=1$ both integrals vanish; equality points do not affect them.

## 7. Exterior weights, generating identity, and full jet coordinates

For $D=\{d_1<\cdots<d_q\}$ let $B_D$ be the corresponding square column
submatrix. Cauchy--Binet gives

\[
\det K_j=\sum_{|D|=q}\det B_D\det B_D^*
\prod_{d\in D}\omega_d^{-1}
=\sum_{|D|=q}\frac{|\det B_D|^2}{\prod_{d\in D}\omega_d}.
\]

Thus every weight $a_D$ in (37) is nonnegative with its literal source
norm denominator. The source exterior vector
$p_{d_1}\wedge\cdots\wedge p_{d_q}$ has squared norm
$\prod_{d\in D}\omega_d$ in the ordinary exterior metric, by its
diagonal Gram determinant. Its image under $\bigwedge^q B_j$ is
$\det B_D$ times the fixed quotient-coordinate determinant vector.
Section 6 gives the exact alternating-tensor comparison.

Let $D(z)$ be diagonal on $\mathcal P_j$, with entry $1/\omega_d$
for $d\le i$ and $z/\omega_d$ for $d>i$. Then

\[
K_i+z(K_j-K_i)=B_jD(z)B_j^*.
\]

Cauchy--Binet over the polynomial ring $\mathbb C[z]$ proves (41),
without choosing a square root of $z$:

\[
Z_{i,j}(z)=\sum_{|D|=q}a_D z^{|D\cap\{i+1,\ldots,j\}|}.
\]

Multiplication of the matrix by $G_j$ on the right gives $T+zH$, so

\[
\frac{Z_{i,j}(z)}{\det K_j}
=\det(T+zH)=\prod_a(g_a+z(1-g_a)).
\]

The denominator is the original positive total. If $x_a=1-g_a$,
the last product has value one at $z=1$, first derivative $\sum_ax_a$,
and second derivative $\sum_{a\ne b}x_ax_b$. Hence

\[
\frac{Z'(1)}{Z(1)}=\operatorname{Tr}H,\qquad
\frac{Z''(1)+Z'(1)}{Z(1)}
-\left(\frac{Z'(1)}{Z(1)}\right)^2
=\operatorname{Tr}(H-H^2).
\]

This proves the occupation ratios while keeping their underlying weighted
totals. Dependent admitted columns give a supported zero weight at that
subset. A subset above the admitted degree belongs to a larger indexing
object, on which the extension records external absence. Specializing
$z=0$ annihilates a positive-degree monomial by scalar multiplication
while preserving its index record.

For completeness, the full derivative matrix has row $(a,r)$ and column
$b$ equal to $\partial_S^r S^b|_{\lambda_a}$, with
$0\le r<m_a$ and $0\le b<q$. Differentiation gives the factorial
$b!/(b-r)!$ when $b\ge r$, and zero otherwise. Its determinant formula
can be proved without dropping those factorials.

Replace the repeated nodes in block $a$ temporarily by
$\lambda_a+\varepsilon t_r$, with distinct $t_r$ in their fixed row
order. Taylor expansion of the evaluation rows shows that the first
nonzero determinant term from this block has distinct derivative orders
$0,\ldots,m_a-1$, coefficient

\[
\varepsilon^{m_a(m_a-1)/2}
\frac{\prod_{r<s}(t_s-t_r)}{\prod_{r=0}^{m_a-1}r!},
\]

and the unscaled derivative rows of $C_\chi$. The ordinary Vandermonde
of all distinct temporary nodes has the same internal factor
$\prod_a\varepsilon^{m_a(m_a-1)/2}\prod_{r<s}(t_s-t_r)$
and external factor
$\prod_{a<b}(\lambda_b-\lambda_a)^{m_am_b}$.
Comparing the leading coefficients proves

\[
\det C_\chi
=\left(\prod_a\prod_{r=0}^{m_a-1}r!\right)
\prod_{a<b}(\lambda_b-\lambda_a)^{m_am_b}.
\]

All auxiliary factors cancelled here are explicitly nonzero; the original
full derivative rows remain unscaled.

For the specified invertible coordinate map $Q=C_\chi M_u$, the complete
matrix transformations are

\[
B_N'=QB_N,\quad K_N'=QK_NQ^*,\quad
G_N'=Q^{-*}G_NQ^{-1},\quad R_N'=R_NQ^{-1},\quad
T'=QTQ^{-1},\quad A'=QAQ^{-1}.
\]

Thus every weight and both totals acquire $|\det Q|^2$, and all
determinant ratios and return eigenvalues agree through these exact maps.
The full derivative orders and actual arithmetic unit are retained.

For an injective rectangular map $\eta:E\to F$, the fully typed
exterior statement is evaluated on the domain determinant generator:

\[
\bigwedge\nolimits^q(\eta B_D)
(\varepsilon_1\wedge\cdots\wedge\varepsilon_q)
=(\det B_D)(\bigwedge\nolimits^q\eta)
(e_0\wedge\cdots\wedge e_{q-1}).
\]

The target vector is nonzero by injectivity of $\eta$. This is the
precise evaluation that the short rectangular display in the source
denotes. It requires no determinant of a rectangular matrix.

## 8. All logarithmic certificate orders and the zero-loss endpoint

In the original $G_j$ metric, $H=I-T$ is positive self-adjoint with
eigenvalues $x_a=1-g_a\in[0,1)$. Consequently
$s_m=\operatorname{Tr}(H^m)=\sum_ax_a^m\ge0$ and the scalar logarithm
series, summed over the finite spectrum, gives

\[
\mathcal L_{i,j}=\sum_{m=1}^{\infty}\frac{s_m}{m}.
\]

A checked matrix inequality $K_i\succeq g_0K_j$, $g_0>0$, implies
$g_0\le1$, since $K_i\preceq K_j$ and the nonzero space has positive
quadratic forms. Congruence by $G_j$ gives $G_jT\succeq g_0G_j$,
hence $0\le x_a\le r=1-g_0$.

If $g_0=1$, then $K_i=K_j$, $T=I$, and $H=0$. Every trace moment
and loss is zero, and $U_p=0$ for every $p\ge1$. This is the explicit
endpoint branch; no division by $r=0$ is performed.

For $0<g_0<1$, the exact coefficient is

\[
c_p(r)=\sum_{\ell=0}^\infty\frac{r^\ell}{p+1+\ell}
=\frac{-\log(1-r)-\sum_{m=1}^pr^m/m}{r^{p+1}}.
\]

For every $0\le x\le r$ and integer $p\ge1$,

\[
0\le-\log(1-x)-\sum_{m=1}^p\frac{x^m}{m}
=x^{p+1}\sum_{\ell=0}^\infty\frac{x^\ell}{p+1+\ell}
\le c_p(r)x^{p+1}.
\]

The $x=0$ case has zero tail. Summing over the actual eigenvalues
proves the two finite bounds $L_p\le\mathcal L_{i,j}\le U_p$, where

\[
L_p=\sum_{m=1}^p\frac{s_m}{m},\qquad U_p=L_p+c_p(r)s_{p+1}.
\]

Their width has the explicit bound

\[
0\le U_p-L_p\le\frac{s_{p+1}}{(p+1)(1-r)}
\le\frac{q\,r^{p+1}}{(p+1)g_0}\longrightarrow0.
\]

The first inequality follows by bounding the denominator
$p+1+\ell\ge p+1$ in the positive series defining $c_p$. This proves
the asserted fixed-pair convergence at every certificate order.

The upper certificates are also monotonically decreasing. The exact
coefficient recurrence is $c_p(r)=1/(p+1)+r c_{p+1}(r)$, so

\[
U_p-U_{p+1}
=c_{p+1}(r)(r s_{p+1}-s_{p+2})
=c_{p+1}(r)\sum_ax_a^{p+1}(r-x_a)\ge0.
\]

The lower certificates increase by $s_{p+1}/(p+1)\ge0$.
At $p=1$ the formula in (50) follows for $0<g_0<1$; its
$g_0=1$ case is the zero branch above. These conclusions retain all
original moments and only use the actual supplied gap inequality.

For rational logarithms, differentiating
$\log((1+t)/(1-t))$ gives $2/(1-t^2)$. Integration of the geometric
series from zero to $t\in[0,1)$ proves

\[
\log\frac{1+t}{1-t}
=2\sum_{a=0}^{m-1}\frac{t^{2a+1}}{2a+1}+E_m,\qquad
0\le E_m\le\frac{2t^{2m+1}}{(2m+1)(1-t^2)}.
\]

This gives (53) with $t=(y-1)/(y+1)$, and every finite value and
tail bound is rational for rational $y$. If the power of two used in
the decomposition has a negative exponent, multiplication of its
logarithm enclosure reverses the endpoints; reciprocation gives the
equivalent sign rule.

The error-aware certificate implication is valid by transitivity:
$K_i^-\preceq K_i$, $K_j\preceq K_j^+$, and
$K_i^-\succeq g_0K_j^+$ imply $K_i\succeq g_0K_j$.
The trace moments remain separately required certified quantities.
For $0\prec X\preceq Y$, the eigenvalues of
$X^{-1/2}YX^{-1/2}$ are at least one, proving
$\det Y\ge\det X$. Applying this to both bounding pairs proves (54).

## 9. The two arithmetic endpoint windows

For $(i,j)=(q-1,2q-1)$ and $(q,2q)$, the two logarithmic losses add
exactly to

\[
\log(V_{q-1}/V_{2q-1})+\log(V_q/V_{2q})
=\log\frac{V_{q-1}V_q}{V_{2q-1}V_{2q}}=\mathcal B_{h,k}.
\]

Adding the two finite upper certificates proves (51). For
$q\ge k\ge3$, the inherited original norm bound and endpoint selection
theorem bound the minimum allowance by
$C_hq\sinh(\mathcal B_{h,k}/(2q))$. Monotonicity of $\sinh$ on the
nonnegative real axis then proves (52) with its exact domain.

For the fixed off-line quartet the inherited lower estimate is
$\mathcal B_{h,k}\ge2q_k a_k$, where
$a_k=\operatorname{arsinh}(\delta k/(2C_h))>0$.
Across the two return maps there are $2q_k$ eigenvalues.
If all were greater than $e^{-a_k}$, all their negative logarithms
would be strictly below $a_k$ and their sum would be strictly below
$2q_k a_k$. This contradicts the actual lower bound and proves (6).
The exact source ratios and recovery map for that direction were
proved in Section 5. Adding the two exact spectral counting integrals
proves (58).

These are consequences for the existing finite canonical representatives.
They do not establish a converse zero statement from a small restriction
eigenvalue. The retained nilpotent Gaussian example in the appended
calculation has a positive loss with an on-line action.

For the empty packet $q=0$, the determinant observations are the empty
product one and logarithmic loss zero, with no positive-rank inverse.
No claim involving a positive quartet dimension is applied to that case.

## 10. Full independent Gaussian calibration

The following complete companion derivation is appended verbatim. It was
read in full by this reviewer and independently checked at the exact
polynomial, kernel, gap, trace, and upper-constant formulas. In particular

\[
U_{13}=\frac{62}{243}+\frac{854}{729}\log(5/2),\qquad
U_{24}=\frac{43}{225}+\frac{28}{27}\log(5/2)
\]

are the upper constants, with all original mass-seven norms retained.
Both printed decimal observations in source (65) are slightly below these
exact values; the strictly positive rational margin in the appendix proves
the asserted total upper bound. The companion's source hash is the same
retained NOTE.tex pin listed at the start of this review.

Companion filename: endpoint_restriction_gaussian_independent_20260913.md.
Companion SHA-256:
b8dc29ffa3fe62b6fb637b3bae498256aaca859a6c8c7e9360c94f522155b414.

No operation in this review promotes the inherited arithmetic analytic
proof to a new formal certificate. The parent lane's checker and source
manifest retain their own execution counts and scope. The original
mathematical source bytes remain unchanged.


# Independent Gaussian calibration and logarithmic certificate derivation

Date: 13 September 2026. Scope: Section 9, equations (59)–(65), of the supplied *Canonical restriction and the arithmetic endpoint volume*, together with the trace certificate (48)–(49) used there. The source is `sources/web_endpoint_restriction_delivery/Tau_Endpoint_Restriction_Control/NOTE.tex`, SHA-256 `ff4cc53cb4d3b10a9547a8a2365db7fd5d874bf1ecf7dd8542b8d1f05f433ef6`.

This is a paper derivation. No mathematical test, compiler, or Lean run was performed; the supplied source was not edited. The general operator constructions are being reviewed separately by the parent reviewer. All calculations below use the specified source measure, full two-dimensional quotient, and the original monic polynomial coordinates.

## 1. The original source and all monic norms

Set

\[
 d\nu(x)=\frac{7}{\sqrt{2\pi}}e^{-x^2/2}\,dx,
 \qquad S=1+ix,\qquad z=S-1,
 \qquad E=\mathbb C[S]/(z^2).
\]

The measure has mass \(7\), and its second moment is also \(7\). In particular the statement that its variance is one concerns the quotient of those two retained moments; the mass has not been assigned the value one. Polynomial norms are

\[
 \langle P,Q\rangle_\nu
 =\int_{\mathbb R}\overline{P(1+ix)}Q(1+ix)\,d\nu(x).
\]

Let

\[
 \operatorname{He}_n(x)
 =(-1)^n e^{x^2/2}\frac{d^n}{dx^n}e^{-x^2/2}.
\]

Repeated differentiation proves that this is a monic polynomial of degree \(n\). Repeated integration by parts has no boundary term, since every derivative of the Gaussian is a polynomial times the same Gaussian. Consequently, for a polynomial \(Q\) of degree below \(n\),

\[
 \int\operatorname{He}_n(x)Q(x)\,d\nu(x)
 =\int Q^{(n)}(x)\,d\nu(x)=0.
\]

Putting \(Q=\operatorname{He}_n\) instead gives

\[
 \int\operatorname{He}_n(x)^2\,d\nu(x)
 =n!\int d\nu(x)=7n!.
\]

Define the polynomial in the original \(S\) coordinate by

\[
 p_n(S)=i^n\operatorname{He}_n((S-1)/i).
\]

Its leading coefficient is exactly one. The evaluation map on the source line sends it to \(i^n\operatorname{He}_n(x)\), so Hermitian orthogonality gives the exact original squared norm

\[
 \omega_n=\|p_n\|_\nu^2=7n!.
\]

For completeness, the generating identity

\[
 e^{tx-t^2/2}=\sum_{n\ge0}\operatorname{He}_n(x)t^n/n!
\]

follows by applying the Taylor expansion of \(e^{-y^2/2}\) at \(y=x\) to \(y=x-t\). Its derivative in \(t\), followed by coefficient comparison, gives
\(\operatorname{He}_{n+1}=x\operatorname{He}_n-n\operatorname{He}_{n-1}\).
Multiplication by \(i^{n+1}\) and substitution \(x=z/i\) therefore yield the original-coordinate recurrence, including its plus sign:

\[
 p_0=1,\qquad p_1=z,\qquad p_{n+1}=zp_n+n p_{n-1}.
\]

In particular,

\[
 p_2=z^2+1,\qquad p_3=z^3+3z,
 \qquad p_4=z^4+6z^2+3.
\]

No polynomial in this calculation is divided by its norm.

## 2. The full quotient and its coordinate maps

The coordinate isomorphism

\[
 \mathbb C^2\longrightarrow E,
 \quad(a,b)^T\longmapsto [a+bz]
\]

has inverse \([P]\mapsto(P(1),P'(1))^T\). This is well-defined because the kernel of the unfactored map \(P\mapsto(P(1),P'(1))\) is exactly \((S-1)^2\mathbb C[S]\): Taylor division gives
\(P=P(1)+P'(1)(S-1)+(S-1)^2Q\).
The derivative coordinate is therefore retained literally.

The specified coordinate relation to the original basis is

\[
 (1,S)C=(1,z),\qquad
 C=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.
\]

Thus an \((1,z)\)-column becomes an \((1,S)\)-column by multiplication by \(C\); this statement fixes the direction of the basis map. In the \((1,z)\) coordinates,

\[
 b_0=\binom10,\quad b_1=\binom01,\quad
 b_2=\binom10,\quad b_3=\binom03,\quad b_4=\binom30.
\]

Multiplication by \(S=1+z\) is

\[
 A=\begin{pmatrix}1&0\\1&1\end{pmatrix}=I+N,
 \quad N=\begin{pmatrix}0&0\\1&0\end{pmatrix},
 \quad N^2=0,\quad N\ne0.
\]

The map onto the reduced quotient \(E/(z)\) is explicitly \((a,b)\mapsto a\), with kernel \(\mathbb C\cdot[z]\); it would discard the second coordinate. None of the matrices below is obtained by taking that further quotient. The relation \(b_2=b_0\) proves that the admitted exterior minor with indices \(\{0,2\}\) is zero while the two-dimensional quotient remains present.

## 3. All four kernel and Gram matrices

In these coordinates the formula being calibrated is

\[
 K_j=\sum_{d=0}^{j}\frac{b_db_d^*}{\omega_d},\qquad G_j=K_j^{-1}
 \quad(j\ge1).
\]

The literal mass appears in each denominator. Direct substitution of the five columns and the norms gives

\[
\begin{aligned}
 K_1&=\operatorname{diag}(1/7,1/7),\\
 K_2&=K_1+\operatorname{diag}(1/14,0)
      =\operatorname{diag}(3/14,1/7),\\
 K_3&=K_2+\operatorname{diag}(0,9/42)
      =\operatorname{diag}(3/14,5/14),\\
 K_4&=K_3+\operatorname{diag}(9/168,0)
      =\operatorname{diag}(15/56,5/14).
\end{aligned}
\]

Inversion yields

\[
\begin{array}{c|c|c}
 j&G_j&V_j=\det G_j\\\hline
 1&\operatorname{diag}(7,7)&49\\
 2&\operatorname{diag}(14/3,7)&98/3\\
 3&\operatorname{diag}(14/3,14/5)&196/15\\
 4&\operatorname{diag}(56/15,14/5)&784/75.
\end{array}
\]

Every matrix is positive definite. The equalities do not replace the literal mass with a normalized source.

## 4. Return spectra, gaps, traces, and total loss

The specified return map has type

\[
 T_{i,j}:(E,G_j)\longrightarrow(E,G_i),\qquad T_{i,j}=K_iG_j.
\]

Its underlying coordinate endomorphisms for the two windows are exactly

\[
 T_{1,3}=\operatorname{diag}(2/3,2/5),
 \qquad T_{2,4}=\operatorname{diag}(4/5,2/5).
\]

The proposed common gap has a literal matrix certificate:

\[
 K_1-\tfrac25K_3=\operatorname{diag}(2/35,0)\succeq0,
 \qquad
 K_2-\tfrac25K_4=\operatorname{diag}(3/28,0)\succeq0.
\]

The complementary endomorphisms and all moments needed for \(p=2\) are

\[
\begin{array}{c|c|c|c|c}
 &H=I-T&s_1&s_2&s_3\\\hline
 (1,3)&\operatorname{diag}(1/3,3/5)&14/15&106/225&854/3375\\
 (2,4)&\operatorname{diag}(1/5,3/5)&4/5&2/5&28/125.
\end{array}
\]

Consequently the losses are

\[
 \mathcal L_{1,3}=\log\frac{V_1}{V_3}=\log\frac{15}{4},
 \qquad
 \mathcal L_{2,4}=\log\frac{V_2}{V_4}=\log\frac{25}{8},
\]

and their sum is exactly

\[
 \mathcal B=\log(375/32).
\]

The older trace estimate on the same inputs has the stated values:

\[
\begin{aligned}
 \operatorname{Tr}(K_1^{-1}(K_3-K_1))&=1/2+3/2=2,\\
 \operatorname{Tr}(K_2^{-1}(K_4-K_2))&=1/4+3/2=7/4.
\end{aligned}
\]

## 5. Exact upper constants before any decimal observation

Put \(L=\log(5/2)\). For \(p=2\) and \(g_0=2/5\), the coefficient (48) is

\[
 c_2(3/5)=\frac{125}{27}\left(L-\frac{39}{50}\right).
\]

Substituting the trace moments into (49), with every rational term retained, gives

\[
\begin{aligned}
 U_{13}
 &=\frac{14}{15}+\frac{53}{225}
    +\frac{854}{3375}\frac{125}{27}
        \left(L-\frac{39}{50}\right)\\
 &=\frac{62}{243}+\frac{854}{729}L,\\
 U_{24}
 &=\frac45+\frac15
    +\frac{28}{125}\frac{125}{27}
        \left(L-\frac{39}{50}\right)\\
 &=\frac{43}{225}+\frac{28}{27}L.
\end{aligned}
\]

The second lines are exact equalities with the preceding original trace expressions; no remainder is omitted. In particular,

\[
 U_{13}+U_{24}=\frac{2711}{6075}+\frac{1610}{729}L.
\]

For each eigenvalue \(x\) of either \(H\), \(0\le x\le3/5\). Expanding \(-\log(1-x)\) and bounding each coefficient of the tail by the corresponding power of \(3/5\) proves

\[
 -\log(1-x)\le x+\frac{x^2}{2}+c_2(3/5)x^3.
\]

Taking the sum over the two eigenvalues proves that the exact \(U_{13},U_{24}\) above are upper bounds for their respective losses.

## 6. Explicit rational logarithmic certificate

For \(0\le t<1\), integration of the geometric series gives

\[
 \log\frac{1+t}{1-t}
 =2\sum_{a=0}^{m-1}\frac{t^{2a+1}}{2a+1}+E_m(t),
 \qquad
 0\le E_m(t)\le\frac{2t^{2m+1}}{(2m+1)(1-t^2)}.
\]

The latter follows term by term from \(2a+1\ge2m+1\) for every remaining index \(a\ge m\). No floating-point logarithm enters the following certificate.

Use \(\log(5/2)=\log2+\log(5/4)\), for which the two \(t\)'s are \(1/3\) and \(1/9\). Define the explicit rational numbers

\[
 S=2\sum_{a=0}^{20}\frac{1}{(2a+1)3^{2a+1}}
   +2\sum_{a=0}^{10}\frac{1}{(2a+1)9^{2a+1}},
\]

\[
 R=\frac{9}{172\cdot3^{43}}
       +\frac{81}{920\cdot9^{23}}.
\]

Thus \(S\le L\le S+R\). Here the powers in the tail can be written explicitly as
\(3^{43}=328256967394537077627\) and
\(9^{23}=8862938119652501095929\).
The finite rational comparisons are

\[
 \frac{916290731874155065}{10^{18}}<S,
 \qquad
 S+R<\frac{916290731874155066}{10^{18}}.
 \tag{R1}
\]

For an entirely integral form of this small certificate, set

\[
 P=\prod_{a=0}^{20}(2a+1),\quad D=3^{42}P,
\]

\[
 N=2\sum_{a=0}^{20}\frac{P}{2a+1}3^{41-2a}
   +2\sum_{a=0}^{10}\frac{P}{2a+1}3^{40-4a}.
\]

Then \(S=N/D\), all displayed quotients defining \(N\) are integers, and (R1) consists precisely of the two positive-denominator comparisons

\[
 10^{18}N>916290731874155065D,
\]

\[
 \frac{916290731874155066D-10^{18}N}{10^{18}D}
 >\frac{9}{172\cdot328256967394537077627}
  +\frac{81}{920\cdot8862938119652501095929}.
\]

These expressions provide the finite rational arithmetic in the proof; they are not a claim that a checker was executed. In particular they imply the slightly wider, convenient upper bound

\[
 L<\ell_+=\frac{91629073187415507}{10^{17}}.
\]

Let the stated target be the exact rational
\(T=2469887624578038/10^{15}\).
Substituting \(\ell_+\) into the total, all denominators are positive, and the comparison is explicit:

\[
\begin{aligned}
 \frac{2711}{6075}+\frac{1610}{729}\ell_+
 &=\frac{4501370195793474156750}{18225\cdot10^{17}},\\
 T&=\frac{4501370195793474255000}{18225\cdot10^{17}},\\
 T-\left(\frac{2711}{6075}+\frac{1610}{729}\ell_+\right)
 &=\frac{98250}{18225\cdot10^{17}}>0.
\end{aligned}
\]

Therefore

\[
 \boxed{\mathcal B\le U_{13}+U_{24}<2.469887624578038<15/4.}
\]

This proves the strict improvement against the original total trace upper bound \(2+7/4=15/4\).

## 7. The printed decimals are rounded observations

The source explicitly says that its exact logarithmic enclosures certify the comparison rather than its printed rounded values. That qualification matters: both decimals in (65) are strictly smaller than their exact \(U\)'s. To see this using (R1), put

\[
 \ell_- =916290731874155065/10^{18}<L.
\]

The exact differences at this lower endpoint are

\[
 \left(\frac{62}{243}+\frac{854}{729}\ell_-\right)
       -1.32854908781965490
 =\frac{3410}{729\cdot10^{18}}>0,
\]

\[
 \left(\frac{43}{225}+\frac{28}{27}\ell_-\right)
       -1.14133853675838303
 =\frac{250}{675\cdot10^{18}}>0.
\]

Thus neither printed decimal should be used as a rational upper endpoint. For readers needing standalone decimal upper endpoints, the wider pair

\[
 U_{13}<1.32854908781965492,
 \qquad U_{24}<1.14133853675838304
\]

follows from \(L<\ell_+\), again by positive-denominator rational comparison. Their sum is \(2.46988762457803796\), still strictly below the stated target. The exact expressions in Section 5 remain the preferred mathematical statement. The source's two displayed values are compatible with its description as rounded observations; the direction of rounding supplies no counterexample to the exact upper certificate or the total bound.

The approximate total in (64) is also consistent: the same series at \(t=1/7\) encloses \(\log(4/3)\), while
\(\log(375/32)=3L-\log(4/3)\). The exact determinant calculation above already proves the claimed total independent of that decimal observation.

## Finding

The mass-seven Gaussian norms, the nilpotent quotient and all remainder columns, the four kernel matrices, both return spectra, the literal gap certificates, the exact total \(\log(375/32)\), and the strict total upper comparison are valid. The two decimals in (65) must remain labeled as rounded observations; the exact upper bounds are the logarithmic expressions proved here.
