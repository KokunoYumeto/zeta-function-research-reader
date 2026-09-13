# The cyclic sum at every conormal depth {#sec:cyclic-sum-conormal}

This section continues the complete cyclic-sum source, especially its Sections 1--3 and 7--8, and the separately supplied conormal-tower proof. It retains the original packet, arithmetic unit, tensor variables and reflection. The new constructions are the retraction and invariant dimensions at every depth, the exact scalar first-jet image, its full conormal comparison, and the finite cyclic Weyl correction with its complementary map.

## Original coordinates and the exact collided annihilator

Let $k\geq1$, and let the nonempty original monic packet be 

$$
h(s)=\prod_{\nu=1}^{a}(s-\rho_\nu)^{m_\nu},
 \qquad d=\sum_{\nu=1}^{a}m_\nu\geq1.
 \tag{CC.1}
$$

 The $\rho_\nu$ are distinct, and every $m_\nu$ is the full order retained by the packet. In the arithmetic application $g=2\xi$, $v_h=g/h$, and the chosen packet consists of zeros of $g$ with those full orders. Thus $v_h(\rho_\nu)\ne0$. For the original arithmetic reflection and pairing, retain the delivered packet hypothesis: the map $\rho\mapsto1-\overline\rho$ permutes the packet and preserves each full multiplicity. This is the hypothesis used by the involution in (CC.42)--(CC.48). The polynomial-algebra statements below apply to the displayed original roots without any assumption that they lie on the critical line. Put 

$$
\begin{aligned}
 P&=\mathbb C[s_1,\ldots,s_k],\quad h_i=h(s_i),\quad I=(h_1,\ldots,h_k),
 \quad S=\sum_{i=1}^k s_i,\\
 B_r&=P/I^r,\qquad A_r=B_r^{\mathfrak S_k}\quad(r\geq1),\\
 U_r&=\left[\prod_{i=1}^k v_h(s_i)\right]_{I^r}\in A_r^\times .
\end{aligned}
\tag{CC.2}
$$

 An entire function in (CC.2) means its full finite Taylor class on each local factor. These classes are compatible under every quotient map. Their invertibility follows from their nonzero constant terms: in a finite local algebra a class $u_0+n$, with $u_0\ne0$ and $n^N=0$, has inverse $u_0^{-1}\sum_{j=0}^{N-1}(-n/u_0)^j$. This fixes $U_r$ without replacing any of its Taylor coefficients.

For an ordered tuple ${\bf t}=(\nu_1,\ldots,\nu_k)$, write 

$$
\begin{aligned}
 \lambda_{\bf t}&=\sum_i\rho_{\nu_i},&
 D_{\bf t}&=\sum_i(m_{\nu_i}-1),&
 M_{\bf t}&=\max_i m_{\nu_i},\\
 L_{{\bf t},r}&=1+D_{\bf t}+(r-1)M_{\bf t},&
 \ell_{\lambda,r}&=\max_{\lambda_{\bf t}=\lambda}L_{{\bf t},r},\\
 \Lambda_k&=\{\lambda_{\bf t}\},&
 \chi_r(T)&=\prod_{\lambda\in\Lambda_k}(T-\lambda)^{\ell_{\lambda,r}},
 \qquad q_r=\deg\chi_r .
\end{aligned}
\tag{CC.3}
$$

 The letter $T$ is the polynomial indeterminate in $\chi_r$; its evaluation in the original algebra is $T=S$. Equal sums are grouped before taking the maximum.

**Theorem (Full local depth and the exact scalar contraction).** There are algebra isomorphisms in the original shifted coordinates 

$$
B_r\ \longrightarrow\
 \prod_{{\bf t}\in\{1,\ldots,a\}^k}
 \mathbb C[z_1,\ldots,z_k]/(z_1^{m_{\nu_1}},\ldots,z_k^{m_{\nu_k}})^r,
 \qquad s_i\longmapsto\rho_{\nu_i}+z_i.
 \tag{CC.4}
$$

 In the ${\bf t}$-factor an exact basis consists of the monomials 

$$
z^\alpha,\qquad
 \sum_i\left\lfloor\frac{\alpha_i}{m_{\nu_i}}\right\rfloor\leq r-1.
 \tag{CC.5}
$$

 The nilpotency order of $S-\lambda_{\bf t}=\sum_i z_i$ on that factor is exactly $L_{{\bf t},r}$. Consequently 

$$
I^r\cap\mathbb C[S]=(\chi_r(S)),\qquad
 C_r:=\mathbb C[T]/(\chi_r)
 \ \xrightarrow{\ \alpha_r\ }\ A_r,\quad [F]\longmapsto[F(S)]
 \tag{CC.6}
$$

 is an injective unital algebra map. The original arithmetic coefficient map on the cyclic source is $\eta_r=M_{U_r}\alpha_r:C_r\longrightarrow A_r$. It is injective and intertwines multiplication by $T$ and $S$.

*Proof.* For $r=1$, separate-variable Chinese remainder division gives $I=\bigcap_{\bf t}J_{\bf t}$, where $J_{\bf t}=((s_i-\rho_{\nu_i})^{m_{\nu_i}})_i$. Two different tuples give comaximal ideals: in a coordinate where their roots differ the two one-variable powers are coprime, and their Bezout identity already gives $1$ in the sum of the two ideals. For finitely many pairwise comaximal ideals, intersection equals product. Therefore $I^r=(\prod J_{\bf t})^r=\prod J_{\bf t}^r=\bigcap J_{\bf t}^r$. The same Bezout identity, or its power expansion, proves that the powers remain comaximal. This proves (CC.4).

The local ideal is monomial. A monomial belongs to its $r$-th power precisely when some nonnegative integers $b_i$, with $\sum b_i=r$, satisfy $m_{\nu_i}b_i\leq\alpha_i$ for every $i$. Such $b_i$ exist precisely when the sum of the displayed floors is at least $r$. This proves (CC.5), including independence. Write $\alpha_i=m_{\nu_i}b_i+c_i$, $0\leq c_i<m_{\nu_i}$. The greatest surviving total degree is $D_{\bf t}+(r-1)M_{\bf t}$: put every allowed block $b_i$ in one coordinate attaining $M_{\bf t}$, and put $c_i=m_{\nu_i}-1$ in every coordinate. All monomials of larger degree vanish. In $(\sum z_i)^{D_{\bf t}+(r-1)M_{\bf t}}$ that chosen monomial has the nonzero coefficient $(D_{\bf t}+(r-1)M_{\bf t})!/\prod\alpha_i!$. Distinct monomials cannot cancel. The asserted exact order follows. The annihilator in $\mathbb C[T]$ of evaluation on this factor is therefore $((T-\lambda_{\bf t})^{L_{{\bf t},r}})$. Intersecting these ideals takes the maximum at each repeated $\lambda$, proving (CC.6). The class of $F(S)$ is invariant, and multiplication by the unit $U_r$ preserves injectivity and the stated intertwining. ◻

**Proposition (Degree, scalar powers and all endpoints).** For the nonempty packet, 

$$
\begin{aligned}
 q_r&\geq k(d-1)+(r-1)d+1,\\
 \chi_r&\mid\chi_1^r,\qquad
 \chi_r=\chi_1^r
 \ \Longleftrightarrow\
 (r=1)\ \text{or}\ (k=1)\ \text{or}\ (m_\nu=1\ \forall\nu).
\end{aligned}
\tag{CC.7}
$$

 These are assertions about the complete collided polynomials.

*Proof.* Repeated monic division in the unchanged variables gives the unique finite expansion 

$$
F=\sum_{{\bf b}\in\mathbb N^k,\ 0\leq c_i<d}
 a_{{\bf b},{\bf c}}\prod_i h_i^{b_i}s_i^{c_i}.
 \tag{CC.8}
$$

 The leading monomials have the pairwise distinct exponent vectors $d{\bf b}+{\bf c}$, so a finite dependence is impossible. Equivalently $P$ is free over $\mathbb C[h_1,\ldots,h_k]$ with the displayed remainder basis. Membership in $I^r$ is exactly the vanishing of the coefficients with $\sum b_i<r$. It follows that the highest homogeneous part of every element of $I^r$ belongs to $(s_1^d,\ldots,s_k^d)^r$. Indeed each highest-degree basis term has that property, and its lower terms have smaller total degree.

Put $D=k(d-1)+(r-1)d$. The monomial with exponents $(rd-1,d-1,\ldots,d-1)$ survives the corresponding monomial ideal and has degree $D$. For each $0\leq j\leq D$, choose a divisor of this monomial of degree $j$. Its floor sum is still at most $r-1$, and its coefficient in $S^j$ is a nonzero multinomial coefficient. Thus the leading homogeneous part $S^j$ of a monic polynomial of degree $j$ in $S$ cannot belong to that monomial ideal. Such a polynomial cannot lie in $I^r$. Apply this to $\chi_r(S)$ to obtain the lower bound.

For every tuple, $M_{\bf t}\leq1+D_{\bf t}=L_{{\bf t},1}$, so $L_{{\bf t},r}\leq rL_{{\bf t},1}$. Taking maxima proves divisibility. Each of the three stated equality cases follows directly from (CC.3). Conversely suppose $r,k>1$, and put $M=\max_\nu m_\nu>1$. Choose a root $\rho$ of order $M$ and its pure $k$-tuple. At $\lambda=k\rho$, every tuple has $D_{\bf t}\leq k(M-1)$ and $M_{\bf t}\leq M$; the pure tuple attains both bounds. Therefore 

$$
r\ell_{\lambda,1}-\ell_{\lambda,r}
 =(r-1)(k-1)(M-1)>0.
 \tag{CC.9}
$$

 This proves strict divisibility even when other tuples collide there. ◻

For one root of order $m$, (CC.3) reads $\chi_r(T)=(T-k\rho)^{1+k(m-1)+(r-1)m}$. For $k=1$, $\chi_r=h^r$ and $\alpha_r$ is an isomorphism. For $d=1$, $\chi_r=(T-k\rho)^r$, but the invariant algebra can have a complement to the cyclic image: for $k\geq2,r=3$, the two symmetric degree-two polynomials $\sum z_i^2$ and $\sum_{i<j}z_iz_j$ are independent. The empty packet $h=1$ is treated separately: $I=P$, $B_r=A_r=C_r=0$, $\chi_r=1$, and every displayed finite linear map is the zero map. No formula involving a chosen root or $q_r^{-1}$ is applied in that case. The arithmetic source itself need not be zero merely because its finite packet projection is zero.

The attaining tuple can change with depth. As a declared algebraic example, take roots $1/2+it$, $t=0,1,2,3$, of orders $6,4,4,1$, and $k=2$. At $\lambda=1+3i$ the only unordered pairs are $(0,3)$ and $(1,2)$; they give respectively $6r$ and $4r+3$. Thus $\ell_{\lambda,r}=\max(6r,4r+3)$. This example asserts no location or multiplicity of an arithmetic zero.

## Unscaled invariant bases and a full-unit retraction

For an occupation vector ${\bf n}=(n_1,\ldots,n_a)$ with $\sum n_\nu=k$, put $\lambda_{\bf n}=\sum n_\nu\rho_\nu$. In the factor for a fixed ordered tuple of that occupation, its stabilizer is $\prod_\nu\mathfrak S_{n_\nu}$. For each orbit of the surviving monomials (CC.5), take the sum of the distinct monomials in that orbit, with coefficient one. These are the original unscaled invariant basis elements. Their exact number is 

$$
a_{{\bf n},r}
 =\sum_{p=0}^{r-1}
 [t^p x_1^{n_1}\cdots x_a^{n_a}]
 \prod_{\nu=1}^a\prod_{j=0}^{r-1}
 (1-x_\nu t^j)^{-m_\nu},
 \qquad
 a_{\lambda,r}=\sum_{\lambda_{\bf n}=\lambda}a_{{\bf n},r}.
 \tag{CC.10}
$$

 Coefficient extraction here is finite formal algebra. Each variable in a group of order $m_\nu$ has a pair of labels $(j,c)$, $j\geq0,\ 0\leq c<m_\nu$, representing the original exponent $m_\nu j+c$. An orbit is a multiset of these labels, and the surviving condition is that their $j$'s sum to at most $r-1$. The geometric series for each label proves (CC.10). An invariant in the full product (CC.4) is determined by its entry at one ordered tuple per occupation; the other entries are its variable-permuted translates. The stabilizer condition is precisely the one just imposed. This proves both the claimed basis and 

$$
\begin{aligned}
 \dim B_r&=d^k\binom{r+k-1}{k},\\
 \dim A_r&=\sum_\lambda a_{\lambda,r}
 =\sum_{p=0}^{r-1}[t^p x^k]
       \prod_{j=0}^{r-1}(1-xt^j)^{-d},\\
 a_{{\bf n},1}&=\prod_\nu\binom{n_\nu+m_\nu-1}{m_\nu-1}.
\end{aligned}
\tag{CC.11}
$$

 For the first equality use (CC.8): there are $\binom{r+k-1}{k}$ vectors ${\bf b}$ with $\sum b_i<r$, and $d^k$ possible remainders. For the second alternative expression, permutation acts on that same basis by permuting its $k$ pairs $(b_i,c_i)$; its unscaled orbit sums give the stated series.

**Theorem (Constructive retraction at every depth).** There is an explicit $\mathbb C[T]$-linear retraction $\Pi_r:A_r\longrightarrow C_r$ of $\eta_r$, with the complete arithmetic unit retained. Put $K_r=\ker\Pi_r$ and $Q_r=1-\eta_r\Pi_r$. Then 

$$
\begin{aligned}
 C_r\oplus K_r&\longrightarrow A_r,& (c,v)&\longmapsto\eta_r(c)+v,\\
 A_r&\longrightarrow C_r\oplus K_r,& w&\longmapsto(\Pi_rw,Q_rw)
\end{aligned}
\tag{CC.12}
$$

 are inverse $\mathbb C[T]$-module isomorphisms. In particular $A_r/\eta_rC_r\longrightarrow K_r,\ [w]\longmapsto Q_rw$ is an isomorphism, inverse to inclusion followed by quotient.

*Proof.* For each $\lambda$, use the exact CRT idempotent $e_\lambda(T)$ in $C_r$, and let $A_{\lambda,r}=e_\lambda(S)A_r$. Write $N=S-\lambda$ on this summand. Choose an ordered tuple attaining $\ell=\ell_{\lambda,r}$. Choose a coordinate of maximal multiplicity in it, put all $r-1$ allowed blocks in that coordinate, and put every remainder at its maximum $m_{\nu_i}-1$. Call the resulting exponent $\alpha^*$. Thus $|\alpha^*|=\ell-1$. Let $\theta:A_{\lambda,r}\to\mathbb C$ extract the coefficient of $z^{\alpha^*}$ in that specific local factor, in the basis (CC.5). Define, with $X=T-\lambda$, 

$$
\begin{aligned}
 \Pi_\lambda^0(v)&=\sum_{j=0}^{\ell-1}
       \theta(N^{\ell-1-j}v)X^j\pmod{X^\ell},\\
 w_\lambda&=e_\lambda(S)U_r,\qquad
 p_\lambda(X)=\Pi_\lambda^0(w_\lambda),\\
 \Pi_\lambda(v)&=p_\lambda(X)^{-1}\Pi_\lambda^0(v).
\end{aligned}
\tag{CC.13}
$$

 The equality $N^\ell=0$ gives $\Pi_\lambda^0(Nv)=X\Pi_\lambda^0(v)$, coefficient by coefficient: the constant term on the left is zero and the other coefficients shift by one. Also 

$$
p_\lambda(0)=
 \left(\prod_i v_h(\rho_{\nu_i})\right)
 \frac{(\ell-1)!}{\prod_i\alpha_i^*!}\ne0.
 \tag{CC.14}
$$

 To verify (CC.14), the selected term in $N^{\ell-1}$ has that multinomial coefficient; multiplying by a positive-degree term of the unit would exceed the greatest surviving total degree. The idempotent $e_\lambda(S)$ is exactly one on this local factor. Set $t=p_\lambda/p_\lambda(0)-1$. Its exact inverse is $p_\lambda(0)^{-1}\sum_{j=0}^{\ell-1}(-t)^j$. This retains every coefficient of $p_\lambda$. The intertwining now gives $\Pi_\lambda(e_\lambda(S)U_rF(S))=F(\lambda+X)\bmod X^\ell$. Take the product of these maps and use scalar CRT to define $\Pi_r$. It is the asserted retraction. Its kernel is $S$-stable. The identities $Q_r\eta_r=0$, $\Pi_rQ_r=0$, and $Q_r|_{K_r}=1$ prove every map and inverse in (CC.12). ◻

For any polynomial or entire $f$, multiplication by $f(S)$ has on $A_{\lambda,r}$ the form $f(\lambda)1$ plus a polynomial without constant term in the nilpotent $N$. Powers of a nilpotent map have trace zero, as is seen in a basis adapted to its kernel filtration. The same statement holds on the two invariant summands in (CC.12). Thus 

$$
\begin{aligned}
 \operatorname{Tr}_{A_r}f(S)&=\sum_\lambda a_{\lambda,r}f(\lambda),\\
 \operatorname{Tr}_{C_r}f(T)&=\sum_\lambda\ell_{\lambda,r}f(\lambda),\\
 \operatorname{Tr}_{K_r}f(S)&=
       \sum_\lambda(a_{\lambda,r}-\ell_{\lambda,r})f(\lambda).
\end{aligned}
\tag{CC.15}
$$

 This also proves $a_{\lambda,r}\geq\ell_{\lambda,r}$. All nilpotent coordinates remain in (CC.4), (CC.10) and (CC.13); the trace formula follows from those actual operators.

## The derivative tower, scalar first jets, and the unit obstruction

Denote the quotient maps by $\pi_r:B_{r+1}\to B_r$ and $\rho_r:C_{r+1}\to C_r$. The original derivative is 

$$
\delta_r:B_{r+1}\longrightarrow B_r,\quad
 [F]\longmapsto\left[\frac1k\sum_i\partial_{s_i}F\right],
 \qquad
 \partial_r:C_{r+1}\longrightarrow C_r,\quad [F]\longmapsto[F'].
 \tag{CC.16}
$$

 Each is a complex linear map. Differentiating a product of $r+1$ elements of $I$ leaves at least $r$ such factors, so $\partial_S I^{r+1}\subset I^r$. Formula (CC.3) gives $\ell_{\lambda,r+1}\geq\ell_{\lambda,r}+1$. Thus the derivative of a multiple of $\chi_{r+1}$ is a multiple of $\chi_r$, proving the second descent as well. On representatives, 

$$
\begin{aligned}
 \delta_r\alpha_{r+1}&=\alpha_r\partial_r,&
 \pi_r\alpha_{r+1}&=\alpha_r\rho_r,\\
 \delta_r(xy)&=\pi_r(x)\delta_r(y)+\pi_r(y)\delta_r(x),&
 \pi_r\delta_{r+1}&=\delta_r\pi_{r+1}.
\end{aligned}
\tag{CC.17}
$$

 The last equality is a map $B_{r+2}\to B_r$. The symmetric subspaces are preserved because the derivative averages all $k$ coordinates with the literal factor $1/k$. Every $\delta_r$ is onto: the invertible coordinates $S,z_1,\ldots,z_{k-1}$, where $z_i=s_i-S/k$, have $\partial_S S=1$ and $\partial_Sz_i=0$. Integrating powers of $S$ gives a polynomial primitive of any polynomial representative. Averaging such a primitive proves surjectivity on the invariant subspaces too.

The same monic expansion (CC.8) identifies 

$$
I^j/I^{j+1}\cong
 (P/I)[\zeta_1,\ldots,\zeta_k]_j,\quad
 \zeta_i\longmapsto[h_i],
 \qquad
 \operatorname{gr}\delta
 =\frac1k\sum_i[h_i']\,\partial_{\zeta_i}.
 \tag{CC.18}
$$

 Indeed differentiating $h^{\bf b}r_{\bf b}$ in degree $j=|{\bf b}|$ gives $b_i h^{{\bf b}-e_i}h_i'r_{\bf b}/k$ in degree $j-1$; differentiating $r_{\bf b}$ stays in degree $j$. Both the integer $b_i$ and the original polynomial $h_i'$ survive.

Introduce a formal square-zero parameter $\epsilon$, with its ordinary coefficient algebra meaning. The two maps 

$$
\begin{aligned}
 \Phi_r:B_{r+1}&\longrightarrow B_r[\epsilon]/(\epsilon^2),
 &b&\longmapsto\pi_rb+\epsilon\delta_rb,\\
 \phi_r:C_{r+1}&\longrightarrow C_r[\epsilon]/(\epsilon^2),
 &F&\longmapsto\rho_rF+\epsilon\partial_rF
\end{aligned}
\tag{CC.19}
$$

 are unital algebra homomorphisms by (CC.17) and its one-variable product rule. Extending $\alpha_r$ coefficientwise to $\alpha_r^\epsilon$ gives the exact square $\Phi_r\alpha_{r+1}=\alpha_r^\epsilon\phi_r$. The coefficient projections of these algebra maps are precisely the quotient and derivative maps in (CC.16).

Put $R(T)=\prod_{\lambda\in\Lambda_k}(T-\lambda)$ and $\psi_r=\chi_rR$. Then 

$$
\begin{aligned}
 \ker\phi_r&=(\psi_r)/(\chi_{r+1}),&
 \dim\operatorname{im}\phi_r&=q_r+|\Lambda_k|,\\
 \ker\rho_r&=(\chi_r)/(\chi_{r+1})
       \cong\mathbb C[T]/(\chi_{r+1}/\chi_r),&
 \partial_r(\ker\rho_r)&=\chi_r'C_r .
\end{aligned}
\tag{CC.20}
$$

 For the first assertion, $F$ and $F'$ vanish modulo $(T-\lambda)^{\ell_{\lambda,r}}$ exactly when $F$ has order at least $\ell_{\lambda,r}+1$ there. The order implication in (CC.16) gives $\psi_r\mid\chi_{r+1}$, so the asserted kernel is well defined and has dimension $q_{r+1}-q_r-|\Lambda_k|$. This proves the image dimension and the injective factorization $\mathbb C[T]/(\psi_r)\hookrightarrow C_r[\epsilon]/(\epsilon^2)$. Multiplication by $\chi_r$ gives the displayed isomorphism onto $\ker\rho_r$; its kernel is exactly $(\chi_{r+1}/\chi_r)$. Differentiating $\chi_rF$ modulo $\chi_r$ gives $\chi_r'F$. At each $\lambda$, multiplication by $\chi_r'$ maps the input constant to a nonzero multiple of $(T-\lambda)^{\ell_{\lambda,r}-1}$. Its image has one dimension per $\lambda$, proving all image and kernel claims even at repeated collided roots.

Write 

$$
\beta_r=U_r^{-1}\delta_rU_{r+1}\in A_r,\qquad
 \Phi_r(U_{r+1})=U_r(1+\epsilon\beta_r),\qquad
 \Phi_r(U_{r+1}^{-1})=U_r^{-1}(1-\epsilon\beta_r).
 \tag{CC.21}
$$

 The first formula is the definition of the full logarithmic derivative class, the second follows directly from (CC.19), and the third follows by multiplication and $\epsilon^2=0$. In particular, 

$$
\delta_r\eta_{r+1}
   =\eta_r\partial_r+
      M_{\delta_rU_{r+1}}\alpha_r\rho_r.
 \tag{CC.22}
$$

 This formula retains the full derivative of the arithmetic unit.

There is a complete decomposition of its last term using (CC.12): 

$$
\begin{aligned}
 b_r&=\Pi_r(\delta_rU_{r+1})\in C_r,&
 n_r&=Q_r(\delta_rU_{r+1})\in K_r,\\
 \mathcal N_r:C_r&\longrightarrow K_r,&
 \mathcal N_r(F)&=\alpha_r(F)n_r,\\
 \delta_r\eta_{r+1}
   &=\eta_r(\partial_r+M_{b_r}\rho_r)+\mathcal N_r\rho_r .
\end{aligned}
\tag{CC.23}
$$

 Here $K_r$ is a $\mathbb C[T]$-submodule, so multiplication by $\alpha_r(F)$ preserves it. Both $\Pi_r$ and $Q_r$ intertwine this multiplication; applying them to the last term of (CC.22) proves (CC.23). To state the obstruction independently of the chosen retraction, let $\mathfrak q_r:A_r\to A_r/\eta_rC_r$ be the module quotient and put 

$$
\Omega_r=\mathfrak q_r M_{\delta_rU_{r+1}}\alpha_r:
 C_r\longrightarrow A_r/\eta_rC_r.
 \quad
 \mathfrak q_r\delta_r\eta_{r+1}=\Omega_r\rho_r,
 \qquad
 \Omega_r=0\ \Longleftrightarrow\ \beta_r\in\alpha_r(C_r).
 \tag{CC.24}
$$

 To prove the equivalence, evaluate $\Omega_r$ at $1$. Its vanishing says $\delta_rU_{r+1}=U_r\alpha_r(\gamma_r)$ for a unique $\gamma_r\in C_r$, precisely the condition on $\beta_r$. Conversely that equality makes every value of $\Omega_r$ zero by closure of the subalgebra $\alpha_r(C_r)$. Under (CC.12), $\Omega_r$ corresponds exactly to $\mathcal N_r$. When it vanishes, $b_r=\gamma_r$, and the exact pulled-back derivative is $\partial_r+M_{\gamma_r}\rho_r$. The formulas construct both the obstruction and its strongest scalar derivative correspondence without deleting the complementary directions.

## The finite cyclic derivative and its exact Weyl correction

The quotient derivative has two different depths in its domain and codomain. To compute its finite endomorphism on the prescribed scalar coordinates, let $s_r:C_r\to C_{r+1}$ send a class to the same polynomial of degree less than $q_r$ given by monic division by $\chi_r$. This is a complex-linear section of $\rho_r$. Put 

$$
\begin{aligned}
 L_r(F)&=[T^{q_r-1}]F_0(T),\qquad
 d_r=\partial_rs_r:C_r\to C_r,\\
 D_r^{\mathrm{red}}&=d_r+M_{b_r},\qquad
 A_r^C=M_T:C_r\to C_r,
 \end{aligned}\tag{CC.25}
$$

 where $F_0$ is that unchanged monic remainder. The scalar $L_r(F)$ retains its original coefficient; it is not a functional defined by dividing by a norm. The complete differentiated arithmetic map on this section is 

$$
\delta_r\eta_{r+1}s_r
   =\eta_rD_r^{\mathrm{red}}+\mathcal N_r:C_r\longrightarrow A_r.
 \tag{CC.26}
$$

 Thus the reduced derivative and its complementary component have explicit maps into the original arithmetic algebra.

**Theorem (Finite sum-coordinate Weyl relation).** For the original monic remainder coordinates, 

$$
\begin{aligned}
 [A_r^C-k/2,D_r^{\mathrm{red}}]
    &=-I_{C_r}+\mathsf J_r,&
 \mathsf J_r(F)&=[\chi_r']L_r(F),\\
 \operatorname{rank}\mathsf J_r&=1,&
 \mathsf J_r^2&=q_r\mathsf J_r,&
 \operatorname{Tr}\mathsf J_r&=q_r.
 \end{aligned}\tag{CC.27}
$$

 The full arithmetic correction is the image of the original retained relation: 

$$
\begin{aligned}
 \rho_r\bigl([\chi_r]_{\chi_{r+1}}L_r(F)\bigr)&=0,\\
 \delta_r\bigl(U_{r+1}\alpha_{r+1}([\chi_r]L_r(F))\bigr)
    &=\eta_r([\chi_r']L_r(F)).
 \end{aligned}\tag{CC.28}
$$

 No complementary derivative is suppressed in (CC.26).

*Proof.* Since $TF_0$ has degree at most $q_r$, its exact monic remainder is $TF_0-\chi_r L_r(F)$. Differentiating it and reducing gives 

$$
d_r A_r^C F=[F_0+TF_0'-\chi_r'L_r(F)],\qquad
 A_r^C d_r F=[TF_0'].
$$

 Their difference proves (CC.27), because multiplication by $b_r$ commutes with multiplication by $T$. The vector $[\chi_r']$ has degree $q_r-1$ and leading coefficient $q_r\ne0$. Thus $L_r([\chi_r'])=q_r$; the operator is rank one, its square is $q_r$ times itself, and its trace is that same scalar, either in the remainder basis or by the rank-one matrix formula. For (CC.28), the quotient kills $\chi_r$, and the product rule leaves $U_r\alpha_r(\chi_r')L_r(F)$; the term with $\delta_rU_{r+1}$ still contains $\alpha_r(\chi_r)=0$. The original relation itself remains in $B_{r+1}$ before this application. Finally $\mathcal N_r$ is $\mathbb C[T]$-linear by (CC.23). Consequently the full relation obtained by applying $S$ to (CC.26) and subtracting (CC.26) applied to $TF$ is exactly $-\eta_r+\eta_r\mathsf J_r$; this proves the intertwining including the complementary map. ◻

At $r=1,k=1$, $C_1=\mathbb C[s]/(h)$, $L_1$ is the coefficient of $s^{d-1}$, and (CC.27) gives $[M_{s-1/2},d_1+M_{b_1}]=-I+[h']L_1$. In the original weighted coordinates $u=\upsilon_h F$, its conjugated correction is $u\mapsto\upsilon_h h' L_1(\upsilon_h^{-1}u)$. Multiplication by $\upsilon_h$ and by $\upsilon_h^{-1}$ are the explicit inverse coordinate maps; the expression is the one-variable full-unit correction in the preceding finite Weyl calculation. Formula (CC.28) gives its all-depth extension using the actual relation layer rather than differentiating a quotient zero.

## All first jets and the symmetric conormal kernel

Set $E=B_1$, $E^{[2]}=B_2$, $A_h=\mathbb C[s]/(h)$, and write $c_i=[h'(s_i)]\in E$. Let $a$ continue to denote the number of distinct roots and put $b=d-a=\deg\gcd(h,h')$. The conormal coordinates are the actual isomorphism 

$$
\begin{aligned}
 \iota:E^k&\longrightarrow I/I^2,&
 (v_i)&\longmapsto\left[\sum_i h_i\widetilde v_i\right],\\
 \partial_N:E^k&\longrightarrow E,&
 (v_i)&\longmapsto\frac1k\sum_i c_iv_i .
 \end{aligned}\tag{CC.29}
$$

 Here $\widetilde v_i$ is its original separate-variable monic remainder. Changing a lift changes the displayed sum by $I^2$. Equation (CC.8) proves injectivity, surjectivity and the inverse coefficient extraction. Applying the product rule gives exactly $\delta_1\iota=\partial_N$. The full conormal differential and the specified contraction are the explicit maps 

$$
E^k\longrightarrow\bigoplus_i E\,ds_i\longrightarrow E,
 \qquad (v_i)\longmapsto\sum_i c_iv_i\,ds_i
       \longmapsto\frac1k\sum_i c_iv_i.
 \tag{CC.30}
$$

 Thus the intermediate cotangent module and every coefficient of the sum direction are retained.

**Theorem (Exact ranks and complete first-jet observations).** Put $T_h=\mathbb C[s]/(h,h')$. Then 

$$
\begin{aligned}
 \operatorname{im}\partial_N&=(c_1,\ldots,c_k),&
 \operatorname{coker}\partial_N&\cong T_h^{\otimes k},\\
 \operatorname{rank}_{\mathbb C}\partial_N&=d^k-b^k,&
 \dim\ker\partial_N&=(k-1)d^k+b^k.
 \end{aligned}\tag{CC.31}
$$

 Equip $E\oplus E^k$ with multiplication $(x,v)(y,w)=(xy,xw+yv)$, unit $(1,0)$. The maps 

$$
\begin{aligned}
 J_{\mathrm{all}}:B_2&\longrightarrow E\oplus E^k,&
 [F]&\longmapsto([F],([\partial_iF])_i),\\
 J_S:B_2&\longrightarrow E[\epsilon]/(\epsilon^2),&
 [F]&\longmapsto[F]+\epsilon\delta_1[F],\\
 \mathcal L:E\oplus E^k&\longrightarrow E[\epsilon]/(\epsilon^2),&
 (x,v)&\longmapsto x+\frac{\epsilon}{k}\sum_i v_i
 \end{aligned}\tag{CC.32}
$$

 are unital algebra homomorphisms and satisfy $J_S=\mathcal L J_{\mathrm{all}}$. Their kernels and ranks are 

$$
\begin{aligned}
 \ker J_S&=\iota(\ker\partial_N),&
 \dim\operatorname{im}J_S&=2d^k-b^k,\\
 \ker J_{\mathrm{all}}&=
    \iota\left(\bigoplus_i\operatorname{ann}_E(c_i)\right),&
 \dim\ker J_{\mathrm{all}}&=kb\,d^{k-1},\\
 \dim\operatorname{im}J_{\mathrm{all}}
    &=(k+1)d^k-kb\,d^{k-1}.&&
 \end{aligned}\tag{CC.33}
$$

 For squarefree $h$, $J_{\mathrm{all}}$ is an isomorphism onto the displayed square-zero algebra.

*Proof.* The row in (CC.29) has precisely the ideal of its entries as image. Quotienting by these entries in the separate tensor factors gives $T_h^{\otimes k}$, with the map induced by the original polynomial quotients. The Euclidean algorithm gives $(h,h')=(\gcd(h,h'))$, so $\dim T_h=b$. This proves the cokernel and rank in (CC.31), and rank-nullity on the $kd^k$-dimensional source proves its kernel dimension.

Each coordinate derivative maps $I^2$ into $I$; hence the maps in (CC.32) are well defined. The product rule for each derivative gives exactly the specified square-zero multiplication. The factor $1/k$ gives $J_S=\mathcal L J_{\mathrm{all}}$. An element in either jet kernel has zero ordinary quotient, so it is a conormal class. Applying (CC.29) gives its sum derivative, while applying each coordinate derivative gives $(c_iv_i)_i$. This proves the asserted kernels. Multiplication by $h'$ on $A_h$ has cokernel $T_h$, hence has rank $d-b$ and kernel dimension $b$. Tensoring the kernel and image with the other $k-1$ vector-space factors shows that $\dim\operatorname{ann}_E(c_i)=bd^{k-1}$. The dimension of $B_2$ is $(k+1)d^k$ by (CC.11), which proves both image dimensions. If $b=0$, the full map has zero kernel and equal source and target dimensions; its inverse is multiplicative because it is the inverse of a bijective algebra homomorphism. ◻

The images also have explicit coordinates. Let $j:E\to B_2$ choose the original remainder with $\deg_{s_i}<d$. Set $d_0(x)=\delta_1j(x)$ and $D_0(x)=([\partial_i j(x)])_i$. Directly from (CC.29), 

$$
\begin{aligned}
 \operatorname{im}J_S
   &=\{x+\epsilon(d_0(x)+v):x\in E,
                       \ v\in(c_1,\ldots,c_k)\},\\
 \operatorname{im}J_{\mathrm{all}}
   &=\{(x,D_0(x)+(c_iv_i)_i):x\in E,
                                       \ (v_i)\in E^k\}.
 \end{aligned}\tag{CC.34}
$$

 Every lift differs from $j(x)$ by exactly one conormal vector, which proves both inclusions of each image equality. In particular $\ker J_S=J_{\mathrm{all}}^{-1}(\ker\mathcal L)$, where $\ker\mathcal L=\{(0,v):\sum_i v_i=0\}$. This identifies precisely the relative directions removed by the sum contraction after all first derivatives have been retained.

The same calculation restricts to the permutation invariants. On $E^k$ the simultaneous action is $(\sigma v)_i=\sigma(v_{\sigma^{-1}i})$; all the maps above intertwine this action. Evaluation at the first component gives the explicit vector-space isomorphism 

$$
(E^k)^{\mathfrak S_k}\longrightarrow
 A_h\otimes(A_h^{\otimes(k-1)})^{\mathfrak S_{k-1}}.
 \tag{CC.35}
$$

 For its inverse, start with a tensor fixed by the stabilizer of index one. For each $i$, choose a permutation carrying one to $i$ and use its translate as component $i$. Two choices differ by the stabilizer, so the component is independent of that choice. The resulting tuple is invariant, proving the inverse in full. When $k=1$, the tensor with zero factors is $\mathbb C$ and both maps are the identity on $A_h$.

For a vector space of dimension $n$, the invariant tensors in its $k$-fold tensor power have a basis of unscaled sums over words with prescribed occupation numbers in a fixed basis. There are $\binom{n+k-1}{k}$ such occupations for $n\ge1$, and zero for $n=0,k\ge1$. This proves the dimensions used here directly. Taking invariants in the exact cokernel sequence of (CC.31) remains exact: average a lift by $k!^{-1}\sum_\sigma\sigma$ to lift any invariant image. Consequently 

$$
\begin{aligned}
 \operatorname{coker}\partial_N^{\mathrm{sym}}
      &\cong (T_h^{\otimes k})^{\mathfrak S_k},\\
 \dim(E^k)^{\mathfrak S_k}
      &=d\binom{d+k-2}{k-1},\\
 \operatorname{rank}\partial_N^{\mathrm{sym}}
      &=\binom{d+k-1}{k}-\binom{b+k-1}{k},\\
 \dim\ker\partial_N^{\mathrm{sym}}
      &=d\binom{d+k-2}{k-1}
        -\binom{d+k-1}{k}+\binom{b+k-1}{k}.
 \end{aligned}\tag{CC.36}
$$

 The final binomial is defined to be zero when $b=0$. For the declared polynomial fixture $h=s^2,k=2$, the row is $(v_1,v_2)\mapsto s_1v_1+s_2v_2$; its image is the span of $s_1,s_2,s_1s_2$, of dimension three, and its kernel has dimension five. On invariants the domain has dimension four, target dimension three, image span $s_1+s_2,s_1s_2$, and kernel dimension two. These are exact quotient computations in the stated algebraic fixture, without an assertion about arithmetic roots.

In the original cochain convention a permutation of $k$ factors of cochain degree one contributes $\operatorname{sgn}(\sigma)$. Thus the top-degree action of $k!^{-1}\sum_\sigma\operatorname{sgn}(\sigma)T_\sigma$ is $k!^{-1}\sum_\sigma\sigma$ on these tensor coefficients: the two signs multiply to one. This is the explicit identification with the prescribed symmetric cochain summand. Its top-degree supertrace multiplies each ordinary trace by the retained factor $(-1)^k$.

## Cyclic relation response and the full product Jacobian

Fix the monic-division identity $\chi_1(S)=\sum_i h_i B_i(\mathbf s)$ in the original polynomial ring; it exists by (CC.6) and (CC.8). Define 

$$
\begin{aligned}
 \mathcal B:C_1&\longrightarrow E^k,&
 F&\longmapsto([B_i]_{I}\alpha_1(F))_i,\\
 \partial_N\mathcal B(F)&=\alpha_1([\chi_1']F),\qquad
 \delta_1[U\chi_1(S)F(S)]_{I^2}
    =U_1\alpha_1([\chi_1']F).
 \end{aligned}\tag{CC.37}
$$

 The first map is well defined and $\mathbb C[T]$-linear because each coefficient multiplies the well-defined class $\alpha_1(F)$. Differentiate the displayed division identity with $k^{-1}\sum_i\partial_i$. Terms still containing $h_i$ vanish modulo $I$; the derivative of $S$ is exactly one. This proves the first identity. Differentiating the full-unit relation proves the second, since terms with an undifferentiated $\chi_1$ vanish only at the final reduction. These maps give the exact conormal-to-cyclic Jacobian comparison, including $\ker(\partial_N\mathcal B)=\ker M_{\chi_1'}$, since $\alpha_1$ is injective. Its rank is $|\Lambda_k|$ by (CC.20), and its kernel has dimension $q_1-|\Lambda_k|$.

The full product Jacobian has a different explicit factorization through the same original conormal row. Define 

$$
\begin{aligned}
 J_{\mathrm{prod}}&=\prod_i c_i\in E,\\
 \mathcal P:E&\longrightarrow E^k,&
 v&\longmapsto\left(v\prod_{j\ne i}c_j\right)_i,\\
 \partial_N\mathcal P&=M_{J_{\mathrm{prod}}}:E\to E.
 \end{aligned}\tag{CC.38}
$$

 Indeed each of the $k$ summands in the row is $J_{\mathrm{prod}}v/k$. This proves the factorization with the original factor $1/k$. It is permutation equivariant. Its exact kernel is $\mathcal P^{-1}(\ker\partial_N)=\operatorname{ann}_E(J_{\mathrm{prod}})$. Also $\ker\mathcal P=\bigcap_i\operatorname{ann}_E(\prod_{j\ne i}c_j)$; these equalities follow component by component and retain the intermediate directions rather than declaring the two observations interchangeable.

In a local factor $\mathbb C[z]/(z^m)$, the literal factorization $h(\rho+z)=z^m u_\rho(z)$ gives $h'(\rho+z)=m u_\rho(0)z^{m-1}$ modulo $z^m$. Thus in an ordered product factor, multiplication by $J_{\mathrm{prod}}$ sends a constant to $\prod_i m_i u_{\rho_i}(0)\prod_i z_i^{m_i-1}$, with nonzero coefficient, and annihilates the maximal ideal. There is one image dimension for each of the $a^k$ ordered root tuples. Therefore 

$$
\operatorname{rank}M_{J_{\mathrm{prod}}}=a^k,
 \qquad \ker M_{J_{\mathrm{prod}}}=\sqrt{0_E},
 \qquad \dim\sqrt{0_E}=d^k-a^k.
 \tag{CC.39}
$$

 To check the kernel assertion globally, a class is nilpotent precisely when its constant coefficient vanishes at each local factor: the local maximal ideals are nilpotent and the product is finite. This is exactly the computed annihilator. Under permutation invariants, one image dimension remains for each occupation of the distinct roots, giving rank $\binom{a+k-1}{k}$. The invariant kernel is $(\sqrt{0_E})^{\mathfrak S_k}$, either by restriction or by averaging a lift of each invariant image. The factorization (CC.38) continues to hold on these invariant spaces.

The arithmetic unit remains on every observed conormal vector: 

$$
\delta_1(U_2\iota(v))=U_1\partial_N(v),\qquad
 U_1\partial_N\mathcal P=M_{U_1J_{\mathrm{prod}}}.
 \tag{CC.40}
$$

 The first formula follows from (CC.17), since $\pi_1\iota(v)=0$. Multiplication by $U_1^{-1}$ is its explicit inverse change on the target, so the kernels and ranks remain those proved above while all actual Taylor coefficients stay in the map.

## Trace pairings and all four complementary operator blocks

For a monic one-variable polynomial $p$, all finite residue loops below have positive orientation. The functional $\lambda_p(F)=\sum_\zeta\operatorname{Res}_{T=\zeta}
F(T)p(T)^{-1}\,dT$ is well defined on $\mathbb C[T]/(p)$: adding $pQ$ adds an entire polynomial differential at every loop. At a root of order $m$, write $p=(T-\zeta)^m c(T)$, where $c(\zeta)\ne0$. Then $p'/p=m/(T-\zeta)+c'/c$. Hence 

$$
\lambda_p(p'F)=\sum_\zeta m_\zeta F(\zeta)
       =\operatorname{Tr}_{\mathbb C[T]/(p)}M_F.
 \tag{CC.41}
$$

 For the last equality, in each basis $1,T-\zeta,\ldots,(T-\zeta)^{m-1}$, the multiplication matrix has diagonal $F(\zeta)$ repeated $m$ times; positive nilpotent powers have zero diagonal. This proves the trace identity with all original multiplicities.

The packet reflection gives the conjugate-linear algebra involution 

$$
F^\dagger(\mathbf s)=\overline{F(1-\overline s_1,\ldots,
 1-\overline s_k)}
$$

 on each $B_r$, because it permutes the root factors of $h$ with their full orders. On the scalar algebra its restriction is $F^{\dagger_k}(T)=\overline{F(k-\overline T)}$. The sum set and all the exponents in (CC.3) are permuted by $\lambda\mapsto k-\overline\lambda$; hence $\chi_r^{\dagger_k}=(-1)^{q_r}\chi_r$. This proves well-definedness on each quotient and $\alpha_r(F)^{\dagger}=\alpha_r(F^{\dagger_k})$. Consequently the cyclic pairing 

$$
R_{\chi_r}(F,G)=\lambda_{\chi_r}(F^{\dagger_k}G)
 \quad\hbox{satisfies}\quad
 R_{\chi_r}(F,\chi_r'G)
   =\sum_\lambda\ell_{\lambda,r}
      \overline{F(k-\overline\lambda)}G(\lambda).
 \tag{CC.42}
$$

 This is (CC.41) applied to the same full quotient, with its specified involution.

For the original one-factor arithmetic pairing, put $\upsilon_h=[v_h]_h$, $\varepsilon_h=\upsilon_h^{-1}$, and $\mathscr R_Z(f,u)=\lambda_h(\varepsilon_h f^\dagger u)$. The identity $g'=h'v_h+hv_h'$ gives $j_h(g')=h'\upsilon_h$. Thus the complete unit calculation is 

$$
\begin{aligned}
 \mathscr R_Z(f,j_h(g')P)
 &=\lambda_h(\varepsilon_h f^\dagger\upsilon_h h'P)\\
 &=\lambda_h(f^\dagger h'P)
  =\operatorname{Tr}_{A_h}M_{f^\dagger P}.
 \end{aligned}\tag{CC.43}
$$

 The product functional $\lambda_h^{\otimes k}$ consequently satisfies $\lambda_h^{\otimes k}(J_{\mathrm{prod}}F)
=\operatorname{Tr}_{E}M_F$. To verify it without a tensor restriction on $F$, expand $F$ in the original separate-variable monomial basis and apply (CC.41) factor by factor; both sides are linear in every coefficient. The product $U_1^{-1}U_1$ gives the same exact unit cancellation for its original weighted arithmetic version. This describes the full product trace and (CC.38) supplies its map through the sum-direction conormal observation.

Let $\chi_{A,r}(T)=\prod_\lambda(T-\lambda)^{a_{\lambda,r}}$. Equation (CC.15) gives the genuine quotient trace of every entire $f(S)$ on $T_r=A_r/\eta_rC_r$: 

$$
\operatorname{Tr}_{T_r}f(S)
  =\sum_\lambda\operatorname{Res}_{T=\lambda}f(T)
       \left(\frac{\chi_{A,r}'}{\chi_{A,r}}
                    -\frac{\chi_r'}{\chi_r}\right)dT.
 \tag{CC.44}
$$

 Its proof is the local logarithmic derivative calculation (CC.41) with exponents $a_{\lambda,r}-\ell_{\lambda,r}$. It retains the module $T_r$; its formula is a trace of its induced operator, not a replacement of its nilpotent coordinates.

For an arbitrary linear endomorphism $M:A_r\to A_r$, use the fixed full-unit splitting (CC.12). Write $\iota_K:K_r\to A_r$ for inclusion and regard $Q_r$ as a map with codomain $K_r$. Its full transformed matrix is 

$$
\begin{pmatrix}
  \Pi_rM\eta_r&\Pi_rM\iota_K\\
  Q_rM\eta_r&Q_rM\iota_K
 \end{pmatrix}:C_r\oplus K_r\longrightarrow C_r\oplus K_r.
 \tag{CC.45}
$$

 Applying the two inverse maps of (CC.12) on either side of $M$ proves every block. In these original coordinates, 

$$
\operatorname{Tr}_{A_r}M
   =\operatorname{Tr}_{C_r}(\Pi_rM\eta_r)
       +\operatorname{Tr}_{K_r}(Q_rM\iota_K).
 \tag{CC.46}
$$

 The cross maps in (CC.45) remain part of the transformed operator. For completeness, invariance of trace under these inverse changes follows from $\operatorname{Tr}(XY)=\operatorname{Tr}(YX)$, proved by expanding $\sum_{i,j}X_{ij}Y_{ji}$. The quotient $T_r$ has the induced map $[v]\mapsto[Mv]$ exactly when $M\eta_rC_r\subseteq\eta_rC_r$, equivalently $Q_rM\eta_r=0$. Necessity follows by applying a well-defined quotient map to $[\eta_rc]=0$; sufficiency follows by comparing any two representatives. In that case (CC.12) identifies its map with $Q_rM\iota_K$. This proves the exact quotient criterion and the always-defined complementary compression when it fails.

For a multiplier $M=M_w$ with $w\in A_r$, this criterion is 

$$
M_w\eta_rC_r\subseteq\eta_rC_r
       \quad\Longleftrightarrow\quad w\in\alpha_r(C_r).
 \tag{CC.47}
$$

 Indeed its value on $\eta_r(1)=U_r$ gives necessity after multiplication by $U_r^{-1}$. Conversely subalgebra closure proves sufficiency. If $w=f(S)$, both cross maps in (CC.45) are zero by $\mathbb C[T]$-linearity, proving (CC.44) directly. The full weighted vector pairing is instead the explicitly typed trace 

$$
\operatorname{Tr}_{A_r}M_{(\eta_rF)^\dagger\eta_rG}
   =\operatorname{Tr}_{A_r}
      M_{U_r^\dagger U_r\alpha_r(F^{\dagger_k}G)}.
 \tag{CC.48}
$$

 Multiplicativity of the involution proves this identity before any trace calculation. Insert that unchanged multiplier into all four blocks of (CC.45) to compute its full decomposition. In particular $U_r^\dagger U_r$ has an induced quotient multiplier precisely when it satisfies (CC.47); no membership is assumed from invariance under permutations. If an original positive Hermitian form is represented by $H$ on $A_r$, the same coordinates give its full pullback 

$$
\begin{pmatrix}
 \eta_r^*H\eta_r&\eta_r^*H\iota_K\\
 \iota_K^*H\eta_r&\iota_K^*H\iota_K
 \end{pmatrix}.
 \tag{CC.49}
$$

 This follows by evaluating the form on $\eta_rc+\iota_Kv$ and $\eta_rc'+\iota_Kv'$; all four terms appear. The algebraic retraction entails no orthogonality assertion for that original metric.

## Exact two-factor symmetric presentation at every depth

For $k=2$, retain $S=s_1+s_2$, $R=s_1-s_2$ and $\Delta=R^2$, with inverse $s_1=(S+R)/2$, $s_2=(S-R)/2$. Write the original polynomial as $h(s)=\sum_{j=0}^d c_js^j$, $c_d=1$, and define 

$$
\begin{aligned}
 H_0(S,\Delta)
    &=\sum_{j=0}^d c_j2^{-j}
         \sum_{2a\le j}\binom j{2a}S^{j-2a}\Delta^a,\\
 H_1(S,\Delta)
    &=\sum_{j=1}^d c_j2^{-j}
         \sum_{2a+1\le j}\binom j{2a+1}
                  S^{j-2a-1}\Delta^a.
 \end{aligned}\tag{CC.50}
$$

 Binomial expansion gives exactly $h(s_1)=H_0+RH_1$, $h(s_2)=H_0-RH_1$, including $R=0$. Therefore the linear change of generators with coefficients $1/2$ gives $I=(H_0,RH_1)$ in $\mathbb C[S,R]$. For every $r\ge1$ the complete invariant relation ideal is 

$$
\begin{aligned}
 J_r&=\left(H_0^{r-j}\Delta^{\lceil j/2\rceil}H_1^j
                   :0\le j\le r\right)\subset\mathbb C[S,\Delta],\\
 A_r&\cong\mathbb C[S,\Delta]/J_r,
 \qquad
 C_r\lhook\joinrel\longrightarrow\mathbb C[S,\Delta]/J_r,
       \quad[F(T)]\longmapsto[F(S)].
 \end{aligned}\tag{CC.51}
$$

 To prove the ideal identity, express any element of $I^r$ as a sum of the generators $H_0^{r-j}R^jH_1^j$ times arbitrary polynomials in $S,R$. Average under $R\mapsto-R$. For even $j$, the coefficient's even part is a polynomial in $S,\Delta$, giving $\Delta^{j/2}$. For odd $j$, its odd part is $R$ times such a polynomial, giving $\Delta^{(j+1)/2}$. This proves containment in $J_r$. Each displayed generator is conversely an invariant member of $I^r$, proving equality. Every invariant quotient class has an invariant lift by the same average with coefficient $1/2$. Thus the induced algebra map is onto and has exactly this kernel. The injection in (CC.51) is precisely (CC.6) in those coordinates; its kernel before taking $C_r$ is $(\chi_r)$.

At depth one this recovers the literal presentation $\mathbb C[S,\Delta]/(H_0,\Delta H_1)$, with the relative factor $\Delta$ intact. Under the earlier quartet assumptions, its $H_0,H_1$ are exactly those of (SSP.9): both equal the even and odd coefficients of the same unchanged polynomial $h((S+R)/2)$. The further substitution $Z=S-1$, $x=-Z^2$ is its original (SSP.2) map, so the cyclic injection sends $F(T)$ to $F(1+Z)$ in the complete SSP algebra. Its weighted module injection sends it to $[v_h((S+R)/2)v_h((S-R)/2)]F(S)$; that product is invariant, and its finite Taylor class is exactly $U_r$. The inverse SSP coordinate formulas, and (CC.12) for the cyclic summand, retain the full relative and parity modules at every step.

The two parity modules themselves have exact formulas at every depth. Under those same quartet assumptions, put $\mathcal R=\mathbb C[x,\Delta]$ and use the unchanged polynomials $A_0,A_1$ of (SSP.3), so that $H_0=A_0(-Z^2,\Delta)$, $H_1=ZA_1(-Z^2,\Delta)$. For all indices within $0\le j\le r$, define 

$$
\begin{aligned}
 E_{2a}&=A_0^{r-2a}\Delta^a(-x)^a A_1^{2a},\\
 O_{2a+1}&=A_0^{r-2a-1}\Delta^{a+1}(-x)^a A_1^{2a+1},\\
 \mathfrak a_{e,r}&=(E_{2a},\ xO_{2a+1})\subset\mathcal R,
 &\mathfrak a_{o,r}&=(E_{2a},\ O_{2a+1})\subset\mathcal R,\\
 B_{e,r}&=\mathcal R/\mathfrak a_{e,r},
 & B_{o,r}&=\mathcal R/\mathfrak a_{o,r}.
 \end{aligned}\tag{CC.51a}
$$

 Then $A_r=B_{e,r}\oplus ZB_{o,r}$ as a module in these specified coordinates. Its exact maps and product are 

$$
\begin{aligned}
 \beta_r^{\mathrm{par}}:B_{e,r}&\to B_{o,r},& [a]&\mapsto[a],\\
 \gamma_r^{\mathrm{par}}:B_{o,r}&\to B_{e,r},& [b]&\mapsto[xb],\\
 (a,b)(c,e)&=(ac-\gamma_r^{\mathrm{par}}(be),\
       \beta_r^{\mathrm{par}}(a)e+\beta_r^{\mathrm{par}}(c)b),\\
 \gamma_r^{\mathrm{par}}\beta_r^{\mathrm{par}}&=xI_{B_{e,r}},&
 \beta_r^{\mathrm{par}}\gamma_r^{\mathrm{par}}&=xI_{B_{o,r}}.
 \end{aligned}\tag{CC.51b}
$$

 The superscript distinguishes these parity maps from the full logarithmic unit class $\beta_r$ defined in (CC.21). For a direct proof, substitute $Z^2=-x$ into each generator of (CC.51). Even $j=2a$ gives $E_{2a}$, and odd $j=2a+1$ gives $ZO_{2a+1}$. Before imposing them the module is freely $\mathcal R\oplus Z\mathcal R$, by monic division in $Z$. Multiplication by $c+Zd$ shows that their even coefficient ideal is exactly $(E_{2a},xO_{2a+1})$, and their odd coefficient ideal is exactly $(E_{2a},O_{2a+1})$. This proves both directions of the claimed decomposition. The containments between those ideals and their multiples by $x$ prove well-definedness of $\beta_r^{\mathrm{par}},
\gamma_r^{\mathrm{par}}$; multiplication in $\mathcal R[Z]/(Z^2+x)$ proves every sign, product and composition in (CC.51b). At $r=1$ these are exactly (SSP.6)--(SSP.7), because $E_0=A_0$ and $O_1=\Delta A_1=Q_\Delta$. The original unit is still the full class of the product in (CC.2), carried through these inverse coefficient maps.

## Split lifts, source provenance and quantitative scope

For a complex vector space $V$, retain $G(V)=\{\tau\}\sqcup\{v^\bullet:v\in V\}$, with $e_V=0_V^\bullet$, $\tau$ the additive identity, and $v^\bullet+w^\bullet=(v+w)^\bullet$. The scalar action is $c^\bullet v^\bullet=(cv)^\bullet$, and an absent scalar or vector produces $\tau$. For a complex-linear map $L:V\to W$, its exact lift sends $\tau\mapsto\tau$, $v^\bullet\mapsto(Lv)^\bullet$. It preserves addition and scalar action: on two supported inputs this is the linearity of $L$, and cases with $\tau$ follow from the given identity and absorbing rules. For an algebra homomorphism, the same formula also preserves supported products and units. These formulas apply to every map above with its proved type; a derivative uses the linear lift, while the maps (CC.19) and (CC.32) use the multiplicative lift.

In particular, for a conormal vector $n=\iota(v)$, 

$$
G(\pi_1)(n^\bullet)=e_E,\qquad
 G(J_S)(n^\bullet)=(\epsilon\partial_Nv)^\bullet,
 \qquad G(\delta_1)(n^\bullet)=(\partial_Nv)^\bullet.
 \tag{CC.52}
$$

 The common source is the retained thickening. Every arrow fixes external absence, and every supported kernel vector maps to the receiving supported zero. Equations (CC.37)--(CC.40) give the actual original-unit morphisms connecting cyclic, full conormal and product-Jacobian observations before this quotient.

The exact source map accompanying this section records hashes and line locators for the complete delivered cyclic note, the complete conormal pasted source, and the earlier proof fragments. The cyclic note's depth-one retraction and Sections 7--8 are proved here at every original depth, with complete invariant dimensions, the scalar-power equality classification, the higher-degree lower bound, and the full-unit complement in (CC.24). Equations (CC.45)--(CC.48) provide the precise operator interpretation for the general weighted trace. Equations (CC.29)--(CC.36) prove the first-jet and invariant rank calculations supplied in the pasted source. The uncompiled status of its embedded Lean text describes that historical delivered draft. The separately recorded PR 21 successor has its own checked CI provenance; it does not make the new written proofs of this chapter kernel-checked. No new Lean execution, zero-location calculation, or claimed arithmetic asymptotic is part of these proofs. The formulas give the exact finite algebra, retained relation derivatives and trace maps used by the adjoining cyclic metric calculation. The quantitative interpolation metric remains the original one, with its degree cost from (CC.7) and all its cross terms from (CC.49).
