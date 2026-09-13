---
title: "Canonical restriction and the arithmetic endpoint volume"
subtitle: "The adjoint of the original support transition, exterior minor weights, and a logarithmic control certificate"
author: "Owner-directed SplitZero analytic continuation"
date: "13 September 2026"
---

# 1. Result, inherited input, and scope

The remaining quantity in the current endpoint criterion is a ratio of four canonical arithmetic quotient volumes. This note constructs its underlying restriction operator, proves composition and action identities for that operator, and gives two further ways to calculate and bound the same volume. No new arithmetic metric is selected.

The principal map is

$$
 T_{i,j}:(E,G_j)\longrightarrow(E,G_i),\qquad
 T_{i,j}=K_iG_j,\quad K_n=G_n^{-1},\quad i\le j.                 \tag{1}
$$

It is the **metric adjoint of the original arithmetic identity transport** from degree $i$ to degree $j$. It is also the map read by restricting the actual degree-$j$ canonical polynomial representative to degrees at most $i$:

$$
 R_iT_{i,j}=\operatorname{pr}_{\le i}R_j.                       \tag{2}
$$

The source coordinate inclusions in (2) are made explicit below. The return maps compose in the reverse direction,

$$
 T_{i,j}T_{j,l}=T_{i,l},\qquad
 \det T_{i,j}=V_j/V_i,\quad V_n=\det G_n.                        \tag{3}
$$

Their eigenvalues $g_{i,j,a}$ are in $(0,1]$ and have an exact source meaning: they are the squared singular values of the original identity transport equipped with its two actual quotient metrics, and also of the polynomial restriction on the canonical image. Hence

$$
 \boxed{\log(V_i/V_j)=-\sum_{a=1}^{\dim E}\log g_{i,j,a}.}       \tag{4}
$$

No arithmetic vector is killed by $T_{i,j}$ at a finite admitted degree. Its small eigenvalues quantify the cost of recovering the original arithmetic coordinates from a lower-degree portion of their representatives.

The new finite upper bounds express (4) through positive traces of powers of $I-T_{i,j}$, with an explicitly certified lower bound on $g_{i,j,a}$. A Cauchy--Binet expansion gives another exact representation, by nonnegative full-jet minor weights. The expansion retains the literal mass of the arithmetic source and does not assign its total weight the value one.

The preceding analytic continuation proved, for a fixed full packet $h$ and $n\ge k\ge3$,

$$
 \left(\frac{\omega_{h,k,2n}}{\omega_{h,k,n}}\right)^{1/(2n)}
 \le C_h n.                                                     \tag{5}
$$

We use this as an inherited written analytic theorem, not as a newly kernel-checked result. Composing the new upper certificates with that theorem and the formalizer's endpoint criterion gives an explicit control certificate for the original family.

For a packet consisting exactly of an off-line quartet, the already-established endpoint lower bound additionally implies the following new representative-level consequence: among the two indicated degree restrictions, at least one squared singular value is at most

$$
 \boxed{\exp\!\left[-\operatorname{arsinh}
                \left(\frac{\delta k}{2C_h}\right)\right].}       \tag{6}
$$

This is a necessary consequence of an off-line quartet, not an assertion that small singular values imply one. The calibration below retains a nilpotent on-line block with nontrivial restriction loss.

The general matrix and exterior mechanisms are classical. The contribution is their explicit propagation through this programme's actual source, full-jet quotient, support transitions, and arithmetic action. No upper estimate uniform in $k$ for the logarithmic loss is proved in this note.

# 2. Preserve the original base and source

Retain the marked coefficient square

$$
\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.
\end{array}                                                       \tag{7}
$$

Here $G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\}$, $e_R=0_R^\bullet$, and $p_R(\tau)=0_R$, $p_R(r^\bullet)=r$. The target of $p_{\mathbb Z}$ is infinite. The structural base remains $\mathfrak b_\tau$. Polynomial degree and relation depth do not adjoin another scalar zero.

Keep

$$
 C_+=[V\xrightarrow{\Theta}\mathscr B],\quad
 Q=\mathscr B/\Theta V,\quad D=-x\partial_x,\quad g=2\xi.          \tag{8}
$$

For a fixed finite packet, retain every selected zero with its complete order:

$$
 h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\qquad
 v_h=g/h,\qquad\mathcal MF_h=v_h.                                \tag{9}
$$

The arithmetic integration density at tensor degree $k$ is

$$
 w_h(t)=\frac{|v_h(1/2+it)|^2}{2\pi},\quad
 m_{h,k}=w_h^{*k},\quad
 \mu_h=\int w_h,\quad\int m_{h,k}=\mu_h^k.                        \tag{10}
$$

On the existing cyclic sum module use

$$
 E=\mathbb C[S]/(\chi_{h,k}),\quad q=\deg\chi_{h,k},\quad
 A=M_S,\quad S=s_1+\cdots+s_k,\quad c=k/2.                        \tag{11}
$$

The canonical arithmetic source is

$$
 \mathcal V P=P(D_1+\cdots+D_k)(F_h^{\otimes k}),                 \tag{12}
$$

and its norm is

$$
 \|\mathcal V P\|^2
 =\int_{\mathbb R}|P(c+iu)|^2m_{h,k}(u)\,du.                     \tag{13}
$$

The full arithmetic coefficient maps remain

$$
 J^{(k)}\mathcal V=\eta\pi_\chi,\qquad
 q^{(k)}\mathcal V=\sigma_h^{\otimes k}\eta\pi_\chi,\qquad
 \eta[P]=\upsilon_h^{\otimes k}P(A_k)1,\quad
 \upsilon_h=j_h(g/h).                                            \tag{14}
$$

All derivatives and arithmetic units in these jets remain. The quotient coordinate $[P]_\chi$ and its arithmetic image $\eta[P]_\chi$ are connected by this specified injective module map.

Let $p_0,p_1,\ldots$ be the original monic $S$-polynomials orthogonal for (13), with squared norms $\omega_n>0$. In particular $\omega_0=\mu_h^k$. No polynomial is divided by its norm.

For $N\ge q-1$, let

$$
 \mathcal P_N=\mathbb C[S]_{\le N},\qquad
 \mathcal D_N=\chi\mathcal P_{N-q},\qquad
 \mathcal P_{-1}=0.                                               \tag{15}
$$

The exact source sequence is

$$
 0\longrightarrow\mathcal P_{N-q}
 \xrightarrow{\times\chi}\mathcal P_N
 \xrightarrow{\pi_\chi}E\longrightarrow0.                         \tag{16}
$$

Monicity proves surjectivity and the displayed kernel, including at $N=q-1$. Under $\mathcal V$, the relation $\chi P$ is the same original theta boundary whose primitive was constructed by fixed-order division into the tensor factors. Its support label and both occurrences of every Koszul sign remain in that primitive.

All finite Gram inverses in the note require $q\ge1$. For $h=1$ the finite arithmetic packet is zero, all displayed determinant-line observations have empty determinant one, and no positive-rank inverse is introduced. Its analytic source and mass remain as in (10).

# 3. Construct the canonical degree transport and its adjoint

Use the ordered, unscaled basis $(p_0,\ldots,p_N)$ of $\mathcal P_N$. Define

$$
 O_N=\operatorname{diag}(\omega_0,\ldots,\omega_N),\quad
 B_N=[b_0,\ldots,b_N],\quad b_n=[p_n]_\chi.                         \tag{17}
$$

Here $B_N:\mathbb C^{N+1}\to E$ is the remainder map in the fixed quotient basis $1,S,\ldots,S^{q-1}$. Put

$$
 K_N=B_NO_N^{-1}B_N^*,\qquad G_N=K_N^{-1},\qquad
 R_N=O_N^{-1}B_N^*G_N:E\to\mathcal P_N.                            \tag{18}
$$

The formula gives

$$
 B_NR_N=I_E,\quad R_N^*O_NR_N=G_N,\quad
 \operatorname{im}R_N=\mathcal D_N^\perp.                          \tag{19}
$$

Indeed $B_N$ is onto, so $K_N$ is positive definite. For $z\in\ker B_N$,
$z^*O_NR_N=z^*B_N^*G_N=0$. Every representative is $R_Nu+z$; the two summands are orthogonal. Thus (18) is the unique minimum-norm representative for the original relation space, not an independently selected form.

The actual test-function representative is $\mathcal V R_N$. Every identity involving $R_N$ below passes to that source by (12)--(14).

For $i\le j$, let $L_{i,j}:\mathcal P_i\hookrightarrow\mathcal P_j$ be coefficient padding and let $P_{i,j}:\mathcal P_j\to\mathcal P_j$ keep exactly the first $i+1$ monic coordinates. Since the full monic family is orthogonal, this is the orthogonal projection onto the original lower-degree source. One has

$$
 B_jL_{i,j}=B_i,\qquad L_{i,j}^*O_jL_{i,j}=O_i.                   \tag{20}
$$

Let $\mathscr E_N$ denote $E$ with its actual quotient metric $G_N$. The original quotient transport is

$$
 I_{i,j}:\mathscr E_i\to\mathscr E_j,\quad u\mapsto u,
 \qquad B_jL_{i,j}=I_{i,j}B_i.                                    \tag{21}
$$

It intertwines $A$ exactly. Its Gram decreases, because the larger source admits the old representative and additional original relations:

$$
 G_j\preceq G_i.                                                  \tag{22}
$$

Its metric adjoint is the map in (1). To prove it, compute

$$
 \langle I_{i,j}u,v\rangle_{G_j}
 =u^*G_jv
 =u^*G_i(K_iG_jv)
 =\langle u,T_{i,j}v\rangle_{G_i}.                                \tag{23}
$$

This is an adjoint of the **existing** transport. It is not asserted to be a unital algebra homomorphism.

Direct substitution into (18) proves the representative restriction identity

$$
 \boxed{L_{i,j}R_iT_{i,j}=P_{i,j}R_j.}                             \tag{24}
$$

For example, the first $i+1$ coordinates of $R_j$ are $O_i^{-1}B_i^*G_j$; the right coordinates of $R_iT_{i,j}$ are
$O_i^{-1}B_i^*G_iK_iG_j$, which are identical.

The adjoints compose exactly:

$$
 T_{i,j}T_{j,l}=K_iG_jK_jG_l=K_iG_l=T_{i,l}.                      \tag{25}
$$

This agrees with contravariance of metric adjoints applied to the original identity transports. There is no intervening choice of a metric.

# 4. Record the arithmetic action and the actual boundary correction

Set

$$
 \mathsf H_N=G_N^{-1}(A^*G_N+G_NA-kG_N),\quad
 W_N=A^*G_N+G_NA-kG_N,\quad
 \mathsf V_N=AK_N+K_NA^*-kK_N.                                   \tag{26}
$$

The adjoint-action identity gives

$$
 \boxed{AT_{i,j}-T_{i,j}A
 =\mathsf H_iT_{i,j}-T_{i,j}\mathsf H_j
 =\mathsf V_iG_j-K_iW_j.}                                       \tag{27}
$$

For a direct proof, expand the rightmost expression and cancel the two occurrences of $K_iA^*G_j$ and of $kK_iG_j$. This records the full equivariance defect of the return map. The forward transport (21) is equivariant. The return need not be equivariant for the arithmetic action.

If $\epsilon_i,\epsilon_j$ are the actual operator norms of $\mathsf H_i,\mathsf H_j$ in their respective metrics, (22)--(23) imply the finite bound

$$
 \|AT_{i,j}-T_{i,j}A\|_{\mathscr E_j\to\mathscr E_i}
 \le\epsilon_i+\epsilon_j.                                      \tag{28}
$$

No spectral subspace of the return map is therefore declared invariant under $A$ merely because it is a useful metric diagnostic. Equation (27) is the explicit comparison.

Define the degree-restriction loss endomorphism

$$
 H_{i,j}=I_E-T_{i,j}=(K_j-K_i)G_j.                                \tag{29}
$$

The original relation correction is

$$
 \boxed{\mathfrak d_{i,j}=L_{i,j}R_i-R_j
 =L_{i,j}R_iH_{i,j}-(I-P_{i,j})R_j.}                              \tag{30}
$$

Both terms on the right have arithmetic remainder $H_{i,j}$. Their difference has zero remainder. Consequently

$$
 B_j\mathfrak d_{i,j}=0,\quad
 \operatorname{im}\mathfrak d_{i,j}\subseteq
 \mathcal D_j\cap\mathcal D_i^\perp,\quad
 \mathfrak d_{i,j}^*O_j\mathfrak d_{i,j}=G_i-G_j.                  \tag{31}
$$

The Gram identity follows because $R_j$ is orthogonal to every relation in $\mathcal D_j$. Thus the lower-degree canonical representative is the higher-degree representative plus the explicit original relation (30).

The split map of a single active fibre is

$$
 I_{i,j}^{\tau}:\mathscr E_i^\tau\to\mathscr E_j^\tau,
 \quad u^\bullet\mapsto u^\bullet,\quad\tau\mapsto\tau,
$$
$$
 T_{i,j}^{\tau}:\mathscr E_j^\tau\to\mathscr E_i^\tau,
 \quad u^\bullet\mapsto(T_{i,j}u)^\bullet,\quad\tau\mapsto\tau.    \tag{32}
$$

These are $G(\mathbb C)$-linear single-fibre maps. The forward maps embed into the original directed support diagram. The reverse maps are the metric-adjoint diagram; an additional naturality across the original forward transports is not presumed. Their actual reverse-composition identity is (25). Inclusion of a single-fibre lift into the reconstructed carrier sends $u^\bullet$ to $(\ell_N,u)$ and its external $\tau$ to the carrier's external zero.

Under the original degree-$j$ internal quotient, a supported value of $\mathfrak d_{i,j}$ becomes $(\ell_j,0)$; external absence remains external absence. The relation before that map remains available in (30)--(31), including its original theta primitive.

# 5. Exact volume as a restriction spectrum

The endomorphism $T_{i,j}$ is positive self-adjoint in both $G_i$ and $G_j$:

$$
 G_iT_{i,j}=G_j,\qquad
 G_jT_{i,j}=G_jK_iG_j.                                           \tag{33}
$$

Also $0\prec T_{i,j}\preceq I$ in either metric. For $G_i$, this is (22); for $G_j$, use $K_i\preceq K_j$. Let its $q$ eigenvalues, with multiplicities, be $g_a\in(0,1]$.

The singular values of $I_{i,j}:\mathscr E_i\to\mathscr E_j$ are exactly $\sqrt{g_a}$ because $I_{i,j}^\dagger I_{i,j}=T_{i,j}$. The same nonzero singular values belong to $T_{i,j}$ in the reverse Hilbert types and to the source restriction (24). This is the concrete principal-angle construction for the canonical image and the lower-degree source; it uses their actual inner products.

Taking determinants gives

$$
 \boxed{\det T_{i,j}=\frac{\det K_i}{\det K_j}
 =\frac{V_j}{V_i},\qquad
 \mathcal L_{i,j}:=\log\frac{V_i}{V_j}=-\sum_a\log g_a.}          \tag{34}
$$

The top exterior map $\bigwedge^qT_{i,j}$ acts by this literal determinant in the fixed determinant coordinates. With the source's unscaled alternating tensor representative, the determinant vector has squared norm $q!V_N$ at degree $N$. Both factorials remain in the ratio. This is determinant-line accounting through the same source--relation sequence as in the previous Deligne-oriented construction, not an imported purity conclusion.

An equivalent exact count is

$$
 \boxed{\mathcal L_{i,j}
 =\int_0^1\frac{\#\{a:g_a<t\}}{t}\,dt
 =\int_0^\infty\#\{a:g_a<e^{-s}\}\,ds.}                         \tag{35}
$$

For one $g\in(0,1]$, the first integral is $\int_g^1dt/t$; summing proves the formula. The second uses $t=e^{-s}$. Values at equality do not affect the integrals.

For the quartet endpoint window, (34) is applied twice, to

$$
 (i_0,j_0)=(q-1,2q-1),\qquad(i_1,j_1)=(q,2q).                   \tag{36}
$$

Their losses add to the original four-volume quantity $\mathcal B_{h,k}$.

# 6. An exterior expansion retains every full-jet basis weight

For a $q$-element subset $D=\{d_1<\cdots<d_q\}\subseteq\{0,\ldots,j\}$ define

$$
 a_D=\frac{|\det[b_{d_1},\ldots,b_{d_q}]|^2}
                 {\prod_{d\in D}\omega_d}.                     \tag{37}
$$

Cauchy--Binet applied to (18) gives

$$
 \boxed{\det K_j=\sum_{|D|=q}a_D.}                              \tag{38}
$$

This is an identity of positive finite scalar observations, with no assignment of the sum to one. The actual exterior map giving the numerator is

$$
 \bigwedge^q B_j:\bigwedge^q\mathcal P_j\to\det E,
 \quad p_{d_1}\wedge\cdots\wedge p_{d_q}
       \mapsto\det[b_{d_1},\ldots,b_{d_q}]\,e_0\wedge\cdots\wedge e_{q-1}.
                                                                    \tag{39}
$$

The squared norm of the source wedge is $\prod_{d\in D}\omega_d$. The determinant-coordinate line used to read its coefficient is specified; it is not the canonical arithmetic Gram reset to the identity.

Introduce the finite scalar polynomial

$$
 Z_{i,j}(z)=\det(K_i+z(K_j-K_i)).                                 \tag{40}
$$

Multilinearity and Cauchy--Binet prove the full coefficient identity

$$
 \boxed{Z_{i,j}(z)=
 \sum_{|D|=q}a_Dz^{\#(D\cap\{i+1,\ldots,j\})}.}                \tag{41}
$$

In particular $Z(0)=\det K_i>0$, $Z(1)=\det K_j$, and

$$
 \boxed{\frac{Z_{i,j}(z)}{\det K_j}
 =\det(T_{i,j}+zH_{i,j})
 =\prod_a\bigl(g_a+z(1-g_a)\bigr).}                              \tag{42}
$$

The scalar division is the displayed observation map from the retained pair $(Z,\det K_j)$; the original total and mass remain in (38)--(41). This determinant generating mechanism is classical in projection determinantal measures. Its present interpretation concerns the original degree-admission and full-jet maps, not a randomly selected alternative arithmetic source.

The first two occupation ratios are

$$
 \frac{Z'(1)}{Z(1)}=\operatorname{Tr}H_{i,j},\qquad
 \frac{Z''(1)+Z'(1)}{Z(1)}
 -\left(\frac{Z'(1)}{Z(1)}\right)^2
 =\operatorname{Tr}(H_{i,j}-H_{i,j}^2).                           \tag{43}
$$

These identities follow by differentiating (42); every denominator is the original positive scalar total. The weighted counts in (41) remain available before taking those ratios.

There are two explicit ways a term can be missing from a scalar total. An admitted subset with dependent full-jet columns has $a_D=0$, a supported zero. A subset containing an index above the admitted degree is outside that finite indexing object, and its extension to a larger indexing object is assigned external absence. For example, in the calibration $\chi=(S-1)^2$, $b_0$ and $b_2$ are dependent: the subset $\{0,2\}$ is admitted and has supported zero weight. The subset $\{0,4\}$ is absent from degree three. The algebraic specialization $z=0$ in (41) sends each positive-degree monomial to a supported scalar zero; its support record is not retroactively deleted.

Full derivatives are retained under a change to raw confluent jet coordinates. For roots $\lambda_a$ of orders $m_a$, let

$$
 C_\chi{}_{(a,r),b}
 =\left.\partial_S^rS^b\right|_{S=\lambda_a}
 =\begin{cases}\dfrac{b!}{(b-r)!}\lambda_a^{b-r},&b\ge r,\\0,&b<r.
 \end{cases}                                                     \tag{44}
$$

Its determinant, in the stated block order, is

$$
 \det C_\chi
 =\left(\prod_a\prod_{r=0}^{m_a-1}r!\right)
  \prod_{a<b}(\lambda_b-\lambda_a)^{m_am_b}.                      \tag{45}
$$

For any explicitly retained invertible arithmetic unit matrix $M_u$, the quotient-coordinate change is $C_\chi M_u$. Every weight (37) acquires the same factor $|\det(C_\chi M_u)|^2$, both totals acquire it, and (34), (42) are unchanged through that specified ratio. The action and return are conjugated by this matrix, and the canonical representative is precomposed with its inverse. No nilpotent derivative order is removed.

For the actual cyclic inclusion $\eta:E\hookrightarrow B_k^{S_k}$, the ambient matrix can be rectangular. Its correct exterior comparison is

$$
 \bigwedge^q(\eta B_D)
 = (\det B_D)(\bigwedge^q\eta)(e_0\wedge\cdots\wedge e_{q-1}).
$$

The fixed nonzero image vector is retained. There is no determinant of a rectangular matrix being inverted. A square coordinate change $C_\chi M_u$ applies only on a specified coordinate model of the finite image, or for an actual unit endomorphism of $E$. In the ambient symmetric module the original map remains $\eta$, including the complete factor $\upsilon_h^{\otimes k}$.

# 7. A certified finite logarithmic upper bound

Let $H=H_{i,j}$ and $s_m=\operatorname{Tr}(H^m)$. Positivity in the original metric implies $s_m\ge0$, and the eigenvalues lie in $[0,1)$. Therefore

$$
 \boxed{\mathcal L_{i,j}=\sum_{m=1}^{\infty}\frac{s_m}{m}.}       \tag{46}
$$

A valid rational or real lower gap $g_0>0$ is supplied by the **actual matrix inequality**

$$
 \boxed{K_i\succeq g_0K_j.}                                      \tag{47}
$$

It gives $H\preceq(1-g_0)I$ in $G_j$. Let $r=1-g_0$. For integer $p\ge1$ and $0<r<1$, set

$$
 c_p(r)=\frac{-\log(1-r)-\sum_{m=1}^pr^m/m}{r^{p+1}}.            \tag{48}
$$

The finite enclosure is

$$
 \boxed{
 \sum_{m=1}^p\frac{s_m}{m}
 \le\mathcal L_{i,j}
 \le U_p(H,g_0):=
 \sum_{m=1}^p\frac{s_m}{m}+c_p(r)s_{p+1}.}                        \tag{49}
$$

For $r=0$, (47) and $K_i\preceq K_j$ give $H=0$ and both bounds are zero.

**Proof.** For $0\le x\le r$, the tail of $-\log(1-x)$ is

$$
 x^{p+1}\sum_{m=p+1}^\infty\frac{x^{m-p-1}}m
 \le x^{p+1}\sum_{m=p+1}^\infty\frac{r^{m-p-1}}m
 =c_p(r)x^{p+1}.
$$

Apply this scalar inequality to the positive self-adjoint $H$ and take its trace. For every fixed admitted pair and fixed certified $g_0$, the lower and upper bounds converge to the same loss as $p\to\infty$. This is fixed-pair convergence, not a uniform assertion in tensor degree.

Already $p=1$ gives

$$
 \mathcal L_{i,j}\le s_1+
 \frac{-\log g_0-(1-g_0)}{(1-g_0)^2}s_2.                          \tag{50}
$$

It retains a second moment rather than replacing every loss by the maximum one. Higher $p$ retain the successive moments of the same operator. No eigenvalue of $A$ is inferred from an eigenvalue of $H$; their actual commutator is (27).

For the two windows in (36), verified gaps $g_0^{(0)},g_0^{(1)}$ give

$$
 \boxed{\mathcal B_{h,k}\le
 U_p(H^{(0)},g_0^{(0)})+U_p(H^{(1)},g_0^{(1)}).}                   \tag{51}
$$

Combining (5), the formalizer's endpoint theorem, and monotonicity of $\sinh$ gives the finite canonical-family estimate

$$
 \boxed{
 \min_{q\le N<2q}\epsilon_{h,k,N}
 \le C_hq\sinh\!\left(
 \frac{U_p(H^{(0)},g_0^{(0)})+U_p(H^{(1)},g_0^{(1)})}{2q}
 \right),\quad q\ge k\ge3.}                                     \tag{52}
$$

This theorem uses the explicit matrix certificate (47). Existence of some positive gap for each finite pair does not imply the uniform gap or moment control that would finish the arithmetic argument. Formula (52) states exactly the quantity a certified finite or uniform analytic estimate must bound.

## Error-aware certificate types

The checker supplies exact rational lower and upper bounds for $\log x$ on positive rational inputs. It uses $x=2^e y$, $1\le y<2$, and

$$
 \log y=2\sum_{a=0}^{m-1}\frac{t^{2a+1}}{2a+1}+\mathcal E_m,
 \quad t=\frac{y-1}{y+1},\quad
 0\le\mathcal E_m\le
 \frac{2t^{2m+1}}{(2m+1)(1-t^2)}.                                 \tag{53}
$$

The same formula encloses $\log2$; reciprocation handles $x<1$. Finite rational LDL or principal-minor checks certify (47). No floating-point eigenvalue is accepted as proof of that inequality.

For actual analytic matrix enclosures, a sufficient input is
$K_i^-\preceq K_i$ and $K_j\preceq K_j^+$ together with
$K_i^-\succeq g_0K_j^+$. Then (47) follows by transitivity. The trace moments in (49) also need certified input enclosures, or exact arithmetic; they are not automatically exact because a gap was enclosed. Independently,

$$
 \mathcal L_{i,j}\le\log\det K_j^+-\log\det K_i^-
                                                                    \tag{54}
$$

when both bounding matrices are positive definite. The implemented test fixtures have exact rational entries. This note supplies no interval certificate for the actual arithmetic integrals or root coordinates.

# 8. The off-line alternative forces a precise restriction phenomenon

For the packet consisting exactly of a quartet with displacement $\delta>0$, height $\gamma>0$, and common multiplicity $m$, retain

$$
 q_k=[1+k(m-1)](k+1)^2.                                           \tag{55}
$$

The inherited endpoint theorem and its proved norm input give

$$
 \mathcal B_{h,k}\ge
 2q_k\operatorname{arsinh}\!\left(\frac{\delta k}{2C_h}\right).
                                                                    \tag{56}
$$

There are $2q_k$ positive eigenvalues $g_a$ across the two return maps in (36). Equations (34) and (56) imply that at least one satisfies (6): otherwise every $-\log g_a$ would be smaller than the common lower average in (56), contradicting their sum.

An eigenvector $v$ for that $g_a$ is nonzero in the original arithmetic module. Equation (24) and the actual Gram calculation give

$$
 \boxed{
 \frac{\|P_{i,j}R_jv\|_{O_j}^2}{\|R_jv\|_{O_j}^2}
 =g_a,\qquad
 \frac{\|(I-P_{i,j})R_jv\|_{O_j}^2}{\|R_jv\|_{O_j}^2}=1-g_a.}      \tag{57}
$$

The old portion has arithmetic coordinate $g_av$, not $v$. The exact original representative of $v$ at degree $i$ is recovered by applying $T_{i,j}^{-1}$ in (24). The difference from the full degree-$j$ representative is the actual relation (30). Thus no arithmetic class is called absent, and no numerical near-zero is set equal to $e$.

The exact distributional statement is stronger than one selected direction:

$$
 \sum_{a=0}^1\int_0^\infty
   \#\{b:g_b^{(a)}<e^{-s}\}\,ds
 =\mathcal B_{h,k}.                                               \tag{58}
$$

The growing-degree task can now be stated as control of this cumulative small-restriction spectrum, or as the positive trace certificates (51). A proved upper limit below $2$ for $\mathcal B_{h,k}/(q_k\log k)$ would contradict (56). Such a uniform upper bound is not an output of the present finite identities.

# 9. Exact calibration retaining nilpotence and mass

Use the explicitly declared algebraic fixture

$$
 E=\mathbb C[S]/((S-1)^2),\qquad S=1+ix,
                                                                    \tag{59}
$$

with the Gaussian source $7e^{-x^2/2}dx/\sqrt{2\pi}$, of literal mass seven and variance one. This fixture is not asserted to be a zeta packet. Its source monic polynomials and norms are

$$
 p_0=1,\quad p_1=S-1,\quad
 p_{n+1}=(S-1)p_n+n p_{n-1},\quad \omega_n=7n!.                    \tag{60}
$$

The coordinate basis $(1,S-1)$ is connected to $(1,S)$ by

$$
 C=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
 (1,S)C=(1,S-1).                                                  \tag{61}
$$

In the $(1,S-1)$ coordinates, the kernel matrices are

$$
 K_1=\operatorname{diag}(1/7,1/7),\quad
 K_2=\operatorname{diag}(3/14,1/7),
$$
$$
 K_3=\operatorname{diag}(3/14,5/14),\quad
 K_4=\operatorname{diag}(15/56,5/14).                              \tag{62}
$$

The action remains $A=I+N$ with $N\ne0$ and $N^2=0$. It is not replaced by its reduced one-dimensional quotient.

The two return spectra are exactly

$$
 \operatorname{Spec}T_{1,3}=\{2/3,2/5\},\qquad
 \operatorname{Spec}T_{2,4}=\{4/5,2/5\}.                           \tag{63}
$$

Consequently

$$
 \mathcal B=\log(15/4)+\log(25/8)=\log(375/32)
 \approx2.46119012317068427.                                      \tag{64}
$$

For $H_{1,3}$ the first two trace moments are $14/15$ and $106/225$; for $H_{2,4}$ they are $4/5$ and $2/5$. Using $g_0=2/5$ and $p=2$ in (49) gives the two rigorously enclosed upper bounds whose displayed decimals are

$$
 1.32854908781965490,\qquad1.14133853675838303.                    \tag{65}
$$

Their sum is below $2.469887624578038$. The earlier direct bound by
$\operatorname{Tr}(K_i^{-1}(K_j-K_i))$ gives $2+7/4=3.75$ on these two windows. Thus the new finite certificate makes a strict, verified improvement on the same source and same metrics. The exact logarithmic enclosures, rather than the printed rounded values, certify the comparison.

The dependent subset $\{0,2\}$ in (37) has a supported zero minor because $[p_2]=[p_0]$ in this quotient. Nevertheless the first derivative coordinate at $S=1$ is retained and makes the quotient dimension two. A distinct-root replacement would not give the same matrices.

The test suite also contains off-line algebraic fixtures, nonconstant invertible jet units, and repeated confluent derivatives. It does not infer a zeta-zero statement from these fixtures.

# 10. Integration with the Deligne-oriented programme

The same cohomological transition now carries an explicit positive adjoint and a determinant-line norm. Its action covariance is (27), its theta-boundary correction is (30), and its original support quotient is retained in (32). This is a metric calculation on the existing characteristic-zero realization over $\mathfrak b_\tau$.

Deligne's use of determinant weights and the compact-to-ordinary image requires an actual estimate on the same image. This note supplies additional calculation and finite upper certificates for that estimate; it does not invoke his finite-field purity hypotheses for the theta object. The inherited source review's strict inequality in Lemma 3.2.10 and its squared-eigenvalue step in 3.2.13 are retained. This turn did not newly reassemble the Deligne archive or claim a complete rereading.

Current repository input was checked at main `7ea0a49945390eae14d3160a5730858899768b5f`. The current endpoint criterion retains the corrected top-exterior case and the actual second-exterior multiplicity cost. No second cost-free exterior amplification is used here. The proof status of the original norm bound (5) remains the inherited written analytic status; the present finite tests do not promote it to a Lean certificate.

The principal next quantity is no longer only an unnamed ratio of large determinants. It is the explicit log-loss of the original identity transports, with the canonical representative restriction, all original relations, full jets, arithmetic action, and complementary polynomial degrees attached. The uniform bound still needed is precisely the one on that constructed family.

# References and provenance

1. Owner-directed *Arithmetic endpoint bounds on the original tau-base source*, supplied TeX and archive, 13 September 2026. Equations (1), (35)--(39), and (43)--(48) are the inherited analytic input, endpoint composition, and original relation-layer formulas.
2. Parallel formalization session, `workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md`, read at main `7ea0a49945390eae14d3160a5730858899768b5f`; fetched Git blob `09d658b1c50245b9e340722817bc9487f1ce409a`. Endpoint selection is its written Jensen theorem; the finite telescope components have their separately reported formal scope.
3. Original SplitZero reconstruction/internal quotient and supplied full-jet kernel-layer note. The present construction reuses their quotient and support maps.
4. Lyons, R. (2003). *Determinantal probability measures*. Publications mathematiques de l'IHES 98, 167--212; arXiv:math/0204325. Background for the exterior/Cauchy--Binet generating mechanism, not a source for the arithmetic objects constructed here.
5. Drmac, Z. (2000). *On principal angles between subspaces of Euclidean space*. SIAM Journal on Matrix Analysis and Applications 22, 173--194, doi:10.1137/S0895479897320824. Background for principal angles and singular values. All weighted source maps needed here are proved explicitly.
6. Deligne, P. (1980). *La conjecture de Weil. II*. Publications mathematiques de l'IHES 52, 137--252. Used through the inherited precise reading record; no new finite-field purity application is claimed.
