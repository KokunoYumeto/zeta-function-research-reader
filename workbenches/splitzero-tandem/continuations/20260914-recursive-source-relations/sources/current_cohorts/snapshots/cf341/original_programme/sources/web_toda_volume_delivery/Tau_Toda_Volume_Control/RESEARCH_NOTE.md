---
title: "Source–boundary volume dynamics for the arithmetic control"
subtitle: "Two Hankel flows, the retained phase term, and a finite upper estimate after exterior amplification"
date: "12 September 2026"
---

# Results and scope

The preceding exterior construction proves an aggregate lower bound on the canonical arithmetic control. This continuation constructs a scalar route to its upper estimate without selecting another metric on the arithmetic quotient.

The actual canonical quotient determinant is

$$
V_N(\theta)=\det G_N(\theta)
=\frac{\mathfrak D_{N+1}(\theta)}{\mathfrak B_{N-q+1}(\theta)}.
\tag{1}
$$

The numerator is the Gram determinant of the original polynomial source. The denominator is the Gram determinant of the original theta relations in that source. Both determinants come from one retained arithmetic Laplace transform and an explicitly given differential filter. Both obey the classical Hankel–Toda identity. No new general integrable-system theorem is claimed.

For $N\ge q$, put

$$
 v_N=\log\frac{V_{N-1}}{V_N},\qquad
 a_{N+1}=\frac{\omega_{N+1}}{\omega_N},\qquad
 \ell_N=\log V_N,\qquad
 \sigma=\frac{\operatorname{Tr}A-(k/2)q}{i}\in\mathbb R.
$$

The following is an exact formula, at every real tilt in the stated domain:

$$
\boxed{
\epsilon_N^2
=a_{N+1}(1-e^{-v_N})(e^{v_{N+1}}-1)
-(\sigma-\partial_\theta\ell_N)^2.
}
\tag{2}
$$

At $\theta=0$, $\epsilon_N$ is the original allowance in the exterior-amplification note. The new formula retains the cross-term phase through a derivative of a scalar determinant. It is not an estimate that forgets that term.

In particular, with the actual two-step volume ratio

$$
\mathcal R_N=\frac{V_{N-1}}{V_{N+1}},
$$

one obtains the proved finite upper bound

$$
\boxed{
\epsilon_N\le
\sqrt{a_{N+1}}\frac{\mathcal R_N-1}{2\sqrt{\mathcal R_N}}.
}
\tag{3}
$$

Both nonnegative losses in this upper estimate are computed below. The previous aggregate spectral lower bound therefore forces an explicit minimum two-step contraction of the source/boundary volume ratio. This turns the remaining asymptotic question into a comparison between two specified scalar determinant flows. It does not prove that this comparison has the required subcubic bound.

# 1. Integration of the new formalization report

The supplied report identifies verified source commit `2abc351424ba87aeda948a5cfb846e15ed9373d1` in draft PR #21. The current PR metadata and its complete mathematical note were read. The report's successful execution is used with its stated scope; this session did not run Lean or replay the workflow log.

The checked coefficient interfaces are the original quotient derivative

$$
\delta_r:A_0/I^{r+1}\longrightarrow A_0/I^r,
$$

its square with quotient transitions, the cyclic injection obtained from the **literal** pullback

$$
\mathcal K_r=\{P:P(S)\in I^r\},
$$

and the full multiplier identity

$$
\delta_r([uP(S)])=[uP'(S)]+[(\partial u)P(S)].
$$

The report separately identifies the local quotient-basis and CRT interpretation as written proofs. That separation is maintained. Its relation-depth maximum includes attainment and permits the tuple maximizing a collided sum to change with depth.

Here the scalar relation determinant uses the first cyclic relation $\chi=\chi_{h,k,1}$. The weight $|\chi|^2$ is the **squared Hilbert norm of the multiplication map** $M_\chi$; it is not a declaration that the next contracted ideal is $(\chi^2)$. The map used is displayed in (11). At higher original depth the relevant polynomial remains $\chi_{h,k,r}$, through the checked pullback $\mathcal K_r$, not an assumed power of $\chi$.

The empty-packet correction is also kept. For $h=1$, $I$ is the whole coefficient ring and every positive-depth quotient is zero. The analytic seed $g$ and its mass remain. The split lift $G(0)$ retains two elements. In that case the determinant quotient below is the determinant of the zero-dimensional module, namely $1$, and no positive-dimensional inverse or spectral estimate is inferred.

# 2. Original base, coefficient square, and arithmetic source

Keep

$$
G(R)=\{\tau_R\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet,
$$

and the original square

$$
\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.
\end{array}
\tag{4}
$$

The target of $p_{\mathbb Z}$ remains infinite. The base remains $\mathfrak b_\tau$. Every lifted coefficient map fixes external absence and carries represented zero to represented zero.

The analytic source remains

$$
V=\{\phi\in\mathcal S(\mathbb R):\phi\text{ even},\ \phi(0)=\int\phi=0\},
$$

$$
\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):\sup_{x>0}x^b|D^jF(x)|<\infty\quad\forall b\in\mathbb Z,j\ge0\},
\qquad D=-x\partial_x,
$$

$$
\Theta\phi(x)=\sum_{n\ne0}\phi(nx),\qquad
C_+=[V\xrightarrow{\Theta}\mathscr B],\qquad Q=\mathscr B/\Theta V,
$$

$$
g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
$$

Let $h$ be a nonempty reflection-stable packet of actual zeros with complete orders. Set

$$
E_h=\mathbb C[s]/h,\quad v_h=g/h,\quad
\upsilon_h=j_h(v_h)\in E_h^\times,\quad \mathcal MF_h=v_h.
$$

Fix tensor degree $k\ge1$. Use the cyclic algebra already constructed:

$$
C=\mathbb C[S]/\chi,\quad q=\deg\chi\ge1,\quad c=k/2,\quad A=M_S,
$$

$$
\eta:C\hookrightarrow(E_h^{\otimes k})^{S_k},\qquad
\eta[P]=\upsilon_h^{\otimes k}P\!\left(\sum_iM_{s_i}\right)1.
$$

The source map is

$$
\mathcal V P=P(D_1+\cdots+D_k)(F_h^{\otimes k}).
$$

It retains

$$
J^{(k)}\mathcal V=\eta\pi_\chi,\qquad
q^{(k)}\mathcal V=\sigma_h^{\otimes k}\eta\pi_\chi.
\tag{5}
$$

Here $q^{(k)}$ denotes the original top cohomology quotient; $q=\deg\chi$ denotes a dimension. The full arithmetic unit is still in $\eta$.

The scalar norm is

$$
\|\mathcal VP\|^2=\int_{\mathbb R}|P(c+iu)|^2m_k(u)\,du,
\quad m_k=w_h^{*k},\quad
w_h(t)=\left|\frac{v_h(1/2+it)}{\sqrt{2\pi}}\right|^2.
\tag{6}
$$

Its mass is $\mu_h^k$, with $\mu_h=\int w_h$. No measure is divided by that mass.

# 3. One arithmetic function generates both determinant flows

## 3.1 Analytic domain

Define

$$
M_h(\theta)=\int_{\mathbb R}e^{\theta t}w_h(t)\,dt,
\qquad Z_{h,k}(\theta)=M_h(\theta)^k.
\tag{7}
$$

These are analytic on $|\Re\theta|<\pi/2$. Here and below positivity statements concern real $\theta$ in that interval.

A direct bound suffices. At $\Re s=1/2$, bounded partial sums of the alternating series and summation by parts give $|\eta(s)|\le C(1+|s|)$. The denominator $|1-2^{1-s}|$ is bounded below by $\sqrt2-1$. Stirling's vertical-strip estimate then gives, beyond a fixed compact set,

$$
w_h(t)\le C_h(1+|t|)^{11/2-2\deg h}e^{-\pi|t|/2}.
$$

On the compact set, $g/h$ is entire because the selected zero orders are complete. Thus every differentiated integral is locally uniformly dominated on the displayed strip. This is a sufficient domain, not a claim that it is the maximal analytic continuation of $M_h$.

Fubini and the exact sum coordinate give

$$
Z_{h,k}(\theta)=\int e^{\theta u}m_k(u)\,du,
\qquad
Z_{h,k}^{(j)}(\theta)=\int u^je^{\theta u}m_k(u)\,du.
\tag{8}
$$

In particular $Z_{h,k}(0)=\mu_h^k$.

## 3.2 The source and the relation filter

Let $\overline\chi$ mean coefficientwise conjugation, and define the differential operator and its output

$$
\mathcal F_\chi
=\overline\chi(c-i\partial_\theta)\chi(c+i\partial_\theta),
\qquad
Z_\chi(\theta)=\mathcal F_\chi Z_{h,k}(\theta).
\tag{9}
$$

Differentiation under the integral proves

$$
\boxed{Z_\chi(\theta)=\int|\chi(c+iu)|^2e^{\theta u}m_k(u)\,du>0.}
\tag{10}
$$

Both factors, their signs, and the coefficient $c=k/2$ remain. This filter is multiplication by a source polynomial under the Laplace transform. It is not the quotient-level derivation $\delta_r$.

For $\mathcal P_n=\mathbb C[S]_{\le n}$ and $N\ge q-1$, the actual source sequence is

$$
0\longrightarrow\mathcal P_{N-q}
\xrightarrow{\ M_\chi\ }\mathcal P_N
\xrightarrow{\pi_\chi}C\longrightarrow0,
\qquad M_\chi P=\chi P,
\tag{11}
$$

with $\mathcal P_{-1}=0$. Applying $\mathcal V$ identifies its first image with the original admitted theta boundaries.

The Laplace observation gives the typed identity

$$
\mathscr L_\theta(SP)=(c+i\partial_\theta)\mathscr L_\theta(P),
\quad
\mathscr L_\theta(P)=\int P(c+iu)e^{\theta u}m_k(u)\,du.
$$

Equation (10) is the Gram observation of $M_\chi$. A source relation has nonzero positive norm before the quotient sends it to a fibre zero.

## 3.3 The two determinants

Put

$$
\mathfrak D_n(\theta)
=\det[Z_{h,k}^{(i+j)}(\theta)]_{i,j=0}^{n-1},
\qquad
\mathfrak B_n(\theta)
=\det[Z_\chi^{(i+j)}(\theta)]_{i,j=0}^{n-1},
\tag{12}
$$

with the actual empty determinants $\mathfrak D_0=\mathfrak B_0=1$. Every positive-order determinant is positive. A zero norm polynomial would vanish on a full-measure subset of the real line.

The use of $u$-moments is linked to the original $S$-basis by

$$
S^j=(c+iu)^j=\sum_{r=0}^j\binom jr c^{j-r}i^ru^r.
$$

This triangular coordinate map has determinant $i^{n(n-1)/2}$ on dimension $n$. Its Gram determinant multiplier is exactly $1$, because that determinant has modulus one. No polynomial coefficient or factorial has been dropped.

The determinant has the exact integral representation

$$
\mathfrak D_n(\theta)=\frac1{n!}\int_{\mathbb R^n}
\prod_{i<j}(u_i-u_j)^2
\prod_{j=1}^ne^{\theta u_j}m_k(u_j)\,d^nu.
\tag{13}
$$

For $\mathfrak B_n$, insert $\prod_j|\chi(c+iu_j)|^2$. Expanding both Vandermonde determinants and integrating proves the formula, including $1/n!$. The total mass in the first expression scales as $(\mu_h^k)^n$, not as one.

# 4. The quotient determinant is the source/boundary volume ratio

At real $\theta$ equip the same polynomial source with

$$
\langle P,Q\rangle_\theta
=\int\overline{P(c+iu)}Q(c+iu)e^{\theta u}m_k(u)\,du.
\tag{14}
$$

Let $H_\theta=L^2(\mathbb R,e^{\theta u}m_k(u)du)$. The map $f\mapsto e^{\theta u/2}f$ is an isometry $H_\theta\to H_0$ with inverse $f\mapsto e^{-\theta u/2}f$. The source in each space is exactly the image of $\mathcal P_N$ under evaluation. This is an observation of the original source, not an enlargement of its admitted polynomials.

Let $J_N$ be its quotient matrix and $M_N(\theta)$ its source Gram. Define

$$
K_N=J_NM_N^{-1}J_N^*,\quad G_N=K_N^{-1},\quad
\widehat R_N=M_N^{-1}J_N^*G_N,\quad R_N=\mathcal V\widehat R_N.
\tag{15}
$$

The adjoints in this calculation use (14). At $\theta=0$ these are the preceding canonical arithmetic representatives and their original norm. At every $\theta$,

$$
J^{(k)}R_N=\eta,\qquad q^{(k)}R_N=\sigma_h^{\otimes k}\eta.
$$

Use the source basis

$$
1,S,\ldots,S^{q-1},\quad\chi,\chi S,\ldots,\chi S^{N-q}.
$$

Its change from $1,S,\ldots,S^N$ is triangular with diagonal one because the original $\chi$ is monic. The Schur complement of its boundary Gram is $G_N$. This proves

$$
\boxed{V_N:=\det G_N=\frac{\mathfrak D_{N+1}}{\mathfrak B_{N-q+1}}.}
\tag{16}
$$

Equivalently, the determinant line of (11) is mapped by the wedge of the **specified** kernel columns and quotient lifts. Orthogonal quotient representatives supply the Schur complement. This is the exact determinant-line map behind the ratio.

The original support lift is

$$
(\lambda_N,P)\longmapsto(\lambda_N,[P]_\chi),\qquad
(\lambda_N,\chi Q)\longmapsto(\lambda_N,0),\qquad \tau\longmapsto\tau.
\tag{17}
$$

The determinant $\mathfrak B_{N-q+1}$ retains the norm-volume of those nonzero source relations. Replacing that source by its quotient value would incorrectly replace the positive denominator by information-free zeros. The construction evaluates its Gram before applying (17).

For $h=1$, $\chi=1$ and $C=0$. Then $Z_\chi=Z_{h,k}$ and (16) is $1$ identically. This is the empty determinant, not an inverse on a nonzero spectral module.

# 5. The two classical Toda identities have their actual arithmetic input

The source determinants satisfy

$$
\boxed{
\mathfrak D_n\mathfrak D_n''-(\mathfrak D_n')^2
=\mathfrak D_{n+1}\mathfrak D_{n-1},\qquad n\ge1.
}
\tag{18}
$$

The relation determinants satisfy the same equation with $\mathfrak D$ replaced by $\mathfrak B$.

Here is a proof with the constants retained. For a real positive weight $e^{\theta u}d\mu(u)$, let $Q_j$ be the monic orthogonal polynomial obtained by subtracting lower-degree projections, with norm $h_j$. Multiplication has the recurrence

$$
u Q_j=Q_{j+1}+b_jQ_j+a_jQ_{j-1},\quad a_j=h_j/h_{j-1},\quad a_0=0,
$$

The variable remains $u$. Differentiating orthogonality gives

$$
\partial_\theta Q_j=-a_jQ_{j-1},\qquad
\partial_\theta\log h_j=b_j,\qquad b_j'=a_{j+1}-a_j.
$$

For the last identity, differentiate $h_jb_j=\int uQ_j^2e^{\theta u}d\mu$, substitute the derivative of $Q_j$, and use the recurrence. Since $\mathfrak D_n=\prod_{j<n}h_j$, the sum telescopes:

$$
\partial_\theta^2\log\mathfrak D_n=a_n
=\frac{\mathfrak D_{n+1}\mathfrak D_{n-1}}{\mathfrak D_n^2}.
$$

This proves (18). The relation weight is the same positive weight multiplied by $|\chi(c+iu)|^2$, which is independent of $\theta$, so the proof applies without alteration to its determinants.

The original $S$-monic polynomial norms are exactly

$$
\omega_j=\frac{\mathfrak D_{j+1}}{\mathfrak D_j},\qquad
\nu_j=\frac{\mathfrak B_{j+1}}{\mathfrak B_j}.
\tag{19}
$$

The phases linking monic polynomials in $S$ and $u$ are $i^j$ and $i^{-j}$; their norms agree because the phase has modulus one.

For $m=N-q+1\ge0$ this gives the exact quotient-volume curvature

$$
\boxed{
\partial_\theta^2\log V_N
=\frac{\mathfrak D_{N+2}\mathfrak D_N}{\mathfrak D_{N+1}^2}
-\frac{\mathfrak B_{m+1}\mathfrak B_{m-1}}{\mathfrak B_m^2}.
}
\tag{20}
$$

The second term is defined to be zero for $m=0$, because $\log\mathfrak B_0=0$. It is not a quotient involving $\mathfrak B_{-1}$.

## 5.1 The curvature comes from two actual source maps

Let $X$ be multiplication by $u$ on the polynomial realization in $H_\theta$. Let $P_N$ project to $\mathcal P_N$ and $P_{\mathcal D_N}$ project to the original boundary subspace $\mathcal D_N=\chi\mathcal P_{N-q}$. Write $R$ for its least-norm polynomial lift.

Differentiating the quotient condition and its orthogonality proves

$$
\partial_\theta R=-P_{\mathcal D_N}XR.
\tag{21}
$$

Thus its derivative is an original boundary, with a primitive obtained by literal monic division by $\chi$ and the existing theta division maps. Its quotient class and arithmetic jets stay fixed.

Define

$$
O_N=(1-P_N)XR:C\to\mathcal P_{N+1}\cap\mathcal P_N^\perp,
\qquad
I_N=P_{\mathcal D_N}XR:C\to\mathcal D_N.
$$

Direct differentiation, with the derivative of the measure included, yields

$$
\boxed{G_N''-G_N'G_N^{-1}G_N'=O_N^*O_N-I_N^*I_N.}
\tag{22}
$$

Indeed $G_N'=R^*XR$, $G_N''=R^*X^2R-2R^*XP_{\mathcal D_N}XR$, and $RG_N^{-1}R^*$ is the projection to the orthogonal quotient representatives. Their orthogonal direct sum with $\mathcal D_N$ is $\mathcal P_N$, which proves (22).

Both maps have rank at most one. For $O_N$ this follows from the highest polynomial degree. For $I_N^*$, multiplication sends every boundary of degree below its highest degree back into $\mathcal D_N$, orthogonal to $R$; only the highest boundary direction can contribute.

Taking $\operatorname{Tr}(G_N^{-1}\cdot)$ gives (20). The positive source contribution and the negative boundary contribution are retained. Positivity of each Gram separately is not assigned to their difference.

# 6. The phase in the rank-two control is a scalar volume derivative

Put $T=(A-cI)/i$ on $C$, with $c=k/2$. This is the coefficient operator corresponding to multiplication by $u$ under the explicit ring map $S\mapsto c+iu$. The actual scaling generator is still $A=cI+iT$.

Reflection makes the polynomial $i^{-q}\chi(c+iu)$ real. This assertion follows by substituting $S=c+iu$ into $\chi^\dagger=(-1)^q\chi$. The retained leading phase of $\chi(c+iu)$ is $i^q$. Its remainder ideal and coefficient extraction are transported through that scalar unit, rather than altering $\chi$ in the arithmetic source.

In those real coefficient coordinates let $Q_j(u)$ be the monic source polynomials and $d_j=[Q_j]$. Their norm is $\omega_j$. The metric and representatives have the same quotient definition. Define

$$
\ell_N=\log V_N,\qquad \sigma=\operatorname{Tr}T\in\mathbb R.
$$

The exact identity is

$$
\boxed{\frac{d_N^*G_Nd_{N+1}}{\omega_N}=\sigma-\ell_N'.}
\tag{23}
$$

To prove it, let $\mathfrak b_N=Q_{N+1}-R_Nd_{N+1}$ in the polynomial source. It is the actual next boundary and

$$
R_N^*\mathfrak b_N=-G_Nd_{N+1}.
$$

Multiplying the least-norm polynomial representative by $u$, its highest coefficient is $d_N^*G_N/\omega_N$. Therefore, modulo old boundaries,

$$
XR_N-R_NT=\mathfrak b_N\frac{d_N^*G_N}{\omega_N}.
$$

Multiplication by $R_N^*$ eliminates precisely those old boundary terms. Consequently

$$
\operatorname{Tr}(G_N^{-1}R_N^*XR_N)
=\operatorname{Tr}T-\frac{d_N^*G_Nd_{N+1}}{\omega_N}.
$$

The left side is $\ell_N'$ by (21) and differentiation of the norm. This proves (23).

In the original $S$-polynomial coordinates, $p_j(S)$ maps to $i^jQ_j(u)$. Hence the preceding source cross term satisfies

$$
\boxed{\frac{b_N^*G_Nb_{N+1}}{\omega_N}=i(\sigma-\ell_N').}
\tag{24}
$$

Both the sign and the factor $i$ are retained. In particular an auxiliary real tilt generally creates a nonzero imaginary cross term even from an initially even measure.

# 7. The exact scalar formula and a two-step upper bound

For $N\ge q$, define

$$
\delta_N=\frac{V_N}{V_{N-1}},\qquad v_N=-\log\delta_N\ge0,
\qquad a_{N+1}=\frac{\omega_{N+1}}{\omega_N}.
$$

The nonnegativity follows from the same minimum-norm comparison at nested source degrees. The rank-one kernel update and the matrix determinant lemma give

$$
\frac{b_N^*G_Nb_N}{\omega_N}=1-\delta_N,
\qquad
\frac{b_{N+1}^*G_Nb_{N+1}}{\omega_{N+1}}=\delta_{N+1}^{-1}-1.
\tag{25}
$$

Substitute (24)–(25) into the inherited exact rank-two radius. This proves

$$
\boxed{
\epsilon_N^2=a_{N+1}(1-e^{-v_N})(e^{v_{N+1}}-1)-(\sigma-\ell_N')^2.
}
\tag{26}
$$

All scalar inputs come from (7), (9), and (12). In particular

$$
\delta_N=\frac{\omega_N}{\nu_{N-q}},\qquad
\delta_{N+1}=\frac{\omega_{N+1}}{\nu_{N-q+1}}.
$$

This does not assert that Hankel determinant evaluation is well-conditioned; the exact formula still requires error enclosures for numerical certification.

## 7.1 The first admitted degree

At $N=q-1$, $K_{N-1}$ is not invertible. The displayed formula is replaced by its direct endpoint calculation:

$$
\boxed{
\epsilon_{q-1}^2
=\frac{\nu_0-\omega_q}{\omega_{q-1}}
-(\sigma-\ell_{q-1}')^2.
}
\tag{27}
$$

Here $\nu_0=Z_\chi$ is the actual norm of the first source relation. To prove (27), the first $q$ remainder vectors are a basis, so the final included column has leverage one; the next determinant update gives $d_N=\nu_0-\omega_q$. Formula (24) supplies the phase. No $V_{q-2}^{-1}$ is introduced.

## 7.2 Both losses in the finite upper bound

For $N\ge q$, put

$$
s_N=\frac{v_N+v_{N+1}}2,\qquad t_N=\frac{v_{N+1}-v_N}2.
$$

Direct scalar multiplication gives

$$
(1-e^{-v_N})(e^{v_{N+1}}-1)
=\sinh^2s_N-(e^{t_N}-\cosh s_N)^2.
$$

Thus

$$
\boxed{
\epsilon_N^2=a_{N+1}\sinh^2s_N
-a_{N+1}(e^{t_N}-\cosh s_N)^2
-(\sigma-\ell_N')^2.
}
\tag{28}
$$

In particular, with $\mathcal R_N=e^{2s_N}=V_{N-1}/V_{N+1}\ge1$,

$$
\boxed{
\epsilon_N^2\le a_{N+1}\frac{(\mathcal R_N-1)^2}{4\mathcal R_N}.
}
\tag{29}
$$

This upper estimate retains two computable losses: imbalance between consecutive volume contractions and the original cross-term phase. When the bound is too coarse, (26) or (28) is the exact replacement within the same construction.

# 8. What the exterior lower bound forces on these arithmetic volumes

The preceding exterior theorem gives

$$
L_{h,k}:=\sum_{\Re\lambda>k/2}\ell_\lambda(2\Re\lambda-k)
\le\epsilon_{h,k,N}.
$$

It uses the original representative on its determinant line, not a newly chosen scalar metric. Combining it with (29), at $\theta=0$, proves

$$
\boxed{
\log\frac{V_{N-1}}{V_{N+1}}
\ge2\operatorname{arsinh}\!\left(\frac{L_{h,k}}{\sqrt{a_{N+1}}}\right),\qquad N\ge q.
}
\tag{30}
$$

The equivalent inequality without logarithms is

$$
4\mathcal R_N L_{h,k}^2\le a_{N+1}(\mathcal R_N-1)^2.
$$

For disjoint successive two-degree steps the logarithms telescope. For every $N_0\ge q$ and integer $r\ge1$,

$$
\boxed{
\log\frac{V_{N_0-1}}{V_{N_0+2r-1}}
\ge 2\sum_{j=0}^{r-1}
\operatorname{arsinh}\!\left(
\frac{L_{h,k}}{\sqrt{a_{N_0+2j+1}}}\right).
}
\tag{31}
$$

This is a source-volume consequence for the actual nested relation quotients, not a claim that arithmetic classes disappear when their representative norms decrease. At every degree their jets and original classes remain fixed by (5) and (15).

For a full off-line quartet with displacement $\delta>0$, height $\gamma>0$, and common multiplicity $m$, the previous count is

$$
q=[1+k(m-1)](k+1)^2,
$$

$$
L_{h,k}=2\delta[1+k(m-1)](k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
\tag{32}
$$

The quotient (16) and its derivative therefore give an entirely scalar test of the exterior obstruction. For this full quartet $m_k$ and $|\chi(c+iu)|^2$ are even, so $\sigma=0$ and $\ell_N'(0)=0$. The phase term vanishes at zero tilt by this **additional** symmetry; it has not been removed from the general formula.

The sufficient subcubic target can now be tested from the quantities

$$
\frac{\sqrt{a_{N(k)+1}}}{k^3}
\frac{\mathcal R_{N(k)}-1}{2\sqrt{\mathcal R_{N(k)}}},
\qquad N(k)\ge q,
\tag{33}
$$

or, more sharply, from the full expression (26). An upper limit of zero for (33) would contradict (32) for that fixed quartet. This continuation proves the formula, the finite upper inequality, and the forced volume lower inequalities. It does not prove that limit.

# 9. The Laplace input can be evaluated from the original theta source

The inverse Mellin representation makes $F_h$ holomorphic in $|\arg z|<\pi/4$. Uniform vertical-strip bounds for $v_h$ permit differentiation and shifts on closed subsectors, and shifting the Mellin contour gives the required rapid endpoint bounds there.

The exact analytic-continuation map is

$$
E_\theta F_h(y)
=e^{(y+i\theta/2)/2}F_h(e^{y+i\theta/2}).
$$

For $|\theta|<\pi/2$, its Fourier transform, with kernel $e^{ity}$, is

$$
\mathcal F_+E_\theta F_h(t)=e^{\theta t/2}v_h(1/2+it).
$$

Contour shift proves the equality; Plancherel yields

$$
\boxed{M_h(\theta)=\int_0^\infty|F_h(e^{i\theta/2}x)|^2dx.}
\tag{34}
$$

The phase $e^{i\theta/4}$ in $E_\theta$ has modulus one and is retained before taking the norm.

Dagger stability gives the analytic identity

$$
F_h(1/\bar z)=(-1)^{\deg h}\bar z\,\overline{F_h(z)}.
$$

Substitute $z=e^{i\theta/2}x$ and change variables on $(0,1)$. This proves

$$
\boxed{M_h(\theta)=2\int_1^\infty|F_h(e^{i\theta/2}x)|^2dx.}
\tag{35}
$$

Evenness in $\theta$ requires conjugation stability as well; it is not inferred just from this endpoint identity.

For the **analytic seed** $h=1$, keep

$$
f_0(z)=2\sum_{n\ge1}(4\pi^2n^4z^4-6\pi n^2z^2)e^{-\pi n^2z^2}.
$$

Let $c_1=-6,c_2=4$ and

$$
C_{mn}(\theta)=\pi(m^2e^{i\theta}+n^2e^{-i\theta}).
$$

Substitution into (35), where $\Re C_{mn}>0$, gives

$$
\boxed{
M_1(\theta)=4\sum_{m,n\ge1}\sum_{r,s=1}^2
c_rc_s(\pi m^2)^r(\pi n^2)^s e^{i\theta(r-s)}
\frac{\Gamma(r+s+1/2,C_{mn}(\theta))}
{C_{mn}(\theta)^{r+s+1/2}}.
}
\tag{36}
$$

The complex power is the analytic branch on the open right half-plane agreeing with the positive real power on its positive axis. The sum converges locally uniformly for $|\theta|<\pi/2$, by the exterior Gaussian estimates. Thus all derivatives used by (12) can be taken there. The factor $4$ includes both the original two-sided theta sum and the change from the integral to the incomplete gamma function.

The accompanying numerical script evaluated (36) at 50 and 70 digits, with integer cutoffs 6 and 8. Their printed values agree:

$$
M_1(0)\approx1.279007247846485140479533592267193274492,
$$

$$
M_1(0.1)\approx1.345907178458249796968220592357629805161.
$$

An independent source integral gives

$$
M_1''(0)=\|(D-1/2)f_0\|^2
\approx13.05554930257055843539268465812319368243.
$$

Here $M_1'(0)=0$. Consequently the first source Toda coefficient for tensor degree $k$ is exactly

$$
a_1^{(k)}=k\frac{M_1''(0)}{M_1(0)}
\approx10.207564753485721688865761252237555175\,k.
\tag{37}
$$

This evaluates initial analytic data of the determinant flow. It is not a finite-packet control estimate: for $h=1$ the arithmetic cyclic quotient is zero. The numerical results have neither directed-rounding enclosures nor a numerical omitted-tail certificate.

# 10. Exact finite checks, an essential phase example, and current endpoint

The checker independently constructs source Gram matrices, quotient maps, representatives, action matrices, and scalar determinants in rational Gaussian fixtures. It compares the scalar result against $\operatorname{Tr}((G^{-1}W)^2)/2$.

For the declared coefficient fixture with weight $7e^{-u^2/2}du/\sqrt{2\pi}$, relation $u^2+u+1$, and degree $N=3$, it obtains

$$
\ell_N'(0)=-52/111,\qquad \sigma=-1,\qquad
\epsilon_N^2=1156/333.
$$

The phase subtraction is $(59/111)^2$, which is nonzero. Omitting it changes the answer. A tilted even-relation fixture gives the same warning: parity at zero tilt is not imposed at another tilt.

Twenty-four exact test methods passed in normal and optimized Python, with identical successful records. Both deliberate-failure controls failed. Repeated roots, source-coordinate phases, mass factors, the minimal-degree endpoint, both Toda equations, the curvature difference, the complete scalar radius, and the supported-zero relation are included. These are finite regression tests, not Lean certificates or verification of infinite arithmetic integrals.

All 34 members named in the preceding exterior package's manifest verified. Its 22-method checker passed a fresh normal run. A combined command attempting a subsequent optimized rerun timed out; no completed optimized rerun is claimed for that inherited suite. The new suite passed in both modes.

The present advance is an upper-estimate mechanism on the exact original family: its input is the one-factor arithmetic Laplace transform; its relation filter is the original cyclic annihilator; its output is the canonical quotient volume and complete control radius. The source–boundary curvature and the positive volume retained before an $e$-quotient are explicit maps. No uniform subcubic upper estimate, RH/GRH proof, additional Lean execution, or remote repository modification is claimed.

# References and source boundary

The original source, support, and cohomological conventions are those in the supplied `Tau_Exterior_Trace_Amplification` package and its predecessor `Tau_Cyclic_Sum_Control`. The new formalization report and pinned PR #21 note supply the checked coefficient interfaces, not the analytic estimates in this note.

The general determinant, norm, and Christoffel–Darboux identities are classical. NIST DLMF §18.2(iv), (v), and (ix) records them, including the caution that raw Hankel determinant formulas are often poorly conditioned numerically: https://dlmf.nist.gov/18.2 . The proof in §5 derives the needed Toda identity directly for the actual exponential deformation, without an isomonodromic or rational-logarithmic-derivative hypothesis. Gamma vertical-strip estimates used in §3 are recorded in DLMF §5.11: https://dlmf.nist.gov/5.11 .

The finite exterior trace bound remains the theorem proved in the supplied preceding note; this continuation changes its analytic upper-estimate realization, not its algebraic proof or the scope of the parallel formalization.
