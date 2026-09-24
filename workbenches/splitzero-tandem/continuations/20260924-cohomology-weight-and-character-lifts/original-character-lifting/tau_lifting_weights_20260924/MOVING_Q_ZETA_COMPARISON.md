# The original moving \(q^r\) functions and the original-zeta Mellin quotient

Independent receiving derivation MQ0–MQ9, 24 September 2026. This extends CW0–CW7 from constant Connes–Consani coefficients to their actual moving functions. Every rational exponent is retained. All sums below are finite unless their domain explicitly states otherwise.

The controlling corpus and operation rules were read, including the complete preserved arguments USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2 and USR-6152e3bc6302258c. This calculation uses the already reconstructed arithmetic. The complex coefficient algebra, its unit, the coordinates below, and its addition are not primitive \(Z_1/\tau\). No addition, parity, coordinate, metric or counting is assigned to primitive \(\tau\).

Human source: Alain Connes and Caterina Consani, [The Riemann–Roch strategy: Complex lift of the Scaling Site, arXiv:1805.10501v1](https://arxiv.org/abs/1805.10501v1), original author TeX sources/thecurve_K.tex, §5.1 Lemma adelicomp, §5.4 equations Jdefn1 and the following right action, Proposition classorb1 and Proposition proetcov, and §7.1 equations holom–holom2, Proposition functionq and Remark perfectoid. The exact reading record is at MQ9.

## MQ0. The full original source

Retain
\[
W_{\mathrm{alg}}=\mathbb C[\mathbb R_{>0}^{\times}],\quad
[x][z]=[xz],\quad\theta_\mu[x]=[x^\mu],
\quad\chi_\lambda[x]=x^\lambda,\qquad\mu,\lambda>0.
\tag{MQ0.1}
\]
The symbol \([1]\) is this named group algebra's unit.

Put \(G=\mathbb A_{\mathbb Q}/\mathbb Q\). Let \(\alpha\) be the standard additive character of \(\mathbb A_{\mathbb Q}\), trivial on the diagonal \(\mathbb Q\), whose real component is \(\exp(2\pi i X_\infty)\). Write
\[
e_r(g)=\alpha(rX),\quad r\in\mathbb Q,\quad g=[X]\in G.
\]
This is well defined, \(e_re_s=e_{r+s}\), and
\[
e_r(\iota_\infty(v))=\exp(2\pi i rv).
\tag{MQ0.2}
\]
The characters \(e_r\) are distinct: for \(r\ne s\), choosing real \(v\) with \((r-s)v\notin\mathbb Z\) distinguishes them.

The original classical orbit is
\[
\Gamma_{\mathbb Q,\mathrm{cl}}\simeq G\times\mathbb R_{>0}.
\]
Its right real action is
\[
(g,Y)\cdot
\begin{pmatrix}u&v\\0&1\end{pmatrix}
=(g+\iota_\infty(vY),uY).
\tag{MQ0.3}
\]
In particular right geometric scaling acts by \(R(u)F(g,Y)=F(g,uY)\).

The original functions and every character evaluation are
\[
q^r(g,Y)=e_r(g)[\exp(-2\pi rY)],
\]
\[
\chi_\lambda(q^r)(g,Y)
=e_r(g)\exp(-2\pi r\lambda Y),\qquad r\in\mathbb Q.
\tag{MQ0.4}
\]
Negative \(r\) gives growth at infinity; this is retained. The algebraic source imposes no decay condition in \(Y\). Source holomorphy is tested by the complete character family, with
\[
L_\lambda=Y(\lambda\partial_{X_\infty}+i\partial_Y).
\]
Differentiation gives
\[
L_\lambda\chi_\lambda(q^r)
=Y(2\pi i\lambda r-2\pi i\lambda r)\chi_\lambda(q^r)=0.
\tag{MQ0.5}
\]

## MQ1. The moving algebra is an actual injective geometric evaluation

Use a formal rational-frequency basis \(\mathbf u_r\), with
\(\mathbf u_r\mathbf u_s=\mathbf u_{r+s}\), and put
\[
\mathcal P=W_{\mathrm{alg}}\otimes_{\mathbb C}\mathbb C[\mathbb Q].
\]
Define its geometric evaluation by
\[
\operatorname{Ev}_W\left(\sum_r w_r\mathbf u_r\right)(g,Y)
=\sum_r w_rq^r(g,Y)
=\sum_r e_r(g)w_r[\exp(-2\pi rY)].
\tag{MQ1.1}
\]
It preserves addition and multiplication by the displayed source laws.

This evaluation is injective. Give \(G\) its Haar probability measure \(dg\). Translation invariance proves character orthogonality: for \(r\ne s\), choose \(g_0\) with \(e_{r-s}(g_0)\ne1\); changing \(g\) to \(g+g_0\) shows that the integral of \(e_{r-s}\) is zero. The integral of \(e_0\) is one. At any fixed \(Y_0>0\), the function in (MQ1.1) takes values in the finite-dimensional span of its displayed coefficients, so its Fourier integral is an ordinary finite-dimensional integral and equals
\[
\int_G \operatorname{Ev}_W(F)(g,Y_0)\overline{e_r(g)}\,dg
=w_r[\exp(-2\pi rY_0)].
\]
The basis element on the right is invertible. Hence the exact return is
\[
\boxed{
w_r=[\exp(2\pi rY_0)]
\int_G \operatorname{Ev}_W(F)(g,Y_0)\overline{e_r(g)}\,dg.}
\tag{MQ1.2}
\]
This recovers every \(w_r\), is independent of the chosen \(Y_0\), and proves injectivity. Thus the formal algebra above realizes the original \(W[q^r]\), rather than deleting its moving functions.

The complete scalar character evaluations also distinguish these \(W\)-valued functions. Indeed distinct positive numbers \(x_1,\ldots,x_d\) give an invertible evaluation matrix \((x_j^\lambda)_{\lambda=1,\ldots,d}\), whose determinant is
\[
\left(\prod_jx_j\right)\prod_{i<j}(x_j-x_i).
\]
Apply this to each finite \(W\)-valued Fourier coefficient. A single character is not substituted for the full family.

## MQ2. Arithmetic Frobenius and the faithful coefficientwise map

The source arithmetic Frobenius is
\[
\mathfrak F_\mu=\theta_\mu R(\mu^{-1}).
\]
Using (MQ0.4) gives, with no omitted radial factor,
\[
\mathfrak F_\mu(w_rq^r)(g,Y)
=\theta_\mu(w_r)e_r(g)
[\exp(-2\pi rY/\mu)^\mu]
=\theta_\mu(w_r)q^r(g,Y).
\tag{MQ2.1}
\]
Therefore its exact action on \(\mathcal P\) is
\[
\mathfrak F_\mu=\theta_\mu\otimes\mathrm{id}_{\mathbb C[\mathbb Q]}.
\tag{MQ2.2}
\]
This holds for every real \(\mu>0\), and hence for all primes and prime powers simultaneously.

Retain the original CW domain \(V_+=\operatorname{span}_{\mathbb C}\{[x]:x>1\}\), the strong Mellin space \(\mathcal A\), and the original-zeta quotient
\[
Q=\mathcal A/I,\qquad
I=\overline{\mathcal E(S_0^{\mathrm{even}})}^{\mathcal A},\qquad
\mathcal Ef(u)=u^{1/2}\sum_{n\ge1}f(nu).
\]
The retained transforms, action and exact comparison are
\[
F_k(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u},
\qquad W_a k(u)=a^{1/2}k(u/a),
\]
\[
b(u)=\exp(-(\log u)^2),\quad
K_b[x]=W_{\log x}b,\quad
\overline K_b=\pi_QK_b,
\]
\[
B(s)=\sqrt\pi\exp((s-\tfrac12)^2/4),\qquad
F_{K_b[x]}(s)=B(s)(\log x)^s,\qquad
\overline K_b\theta_\mu=W_\mu\overline K_b.
\tag{MQ2.3}
\]
CW3 proves \(\overline K_b\) injective into the actual \(Q\). It uses the original identity
\[
F_{\mathcal Ef}(s)
=\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}
\]
and the complete actual zero multiplicities, together with the unconditional original-zeta zero count. No completed zeta function is substituted here.

Define
\[
\mathcal K_+=\overline K_b\otimes\mathrm{id}:
V_+\otimes\mathbb C[\mathbb Q]
\longrightarrow Q\otimes\mathbb C[\mathbb Q].
\tag{MQ2.4}
\]
Every vector is a finite sum in the frequency basis. Thus equality of images implies equality of every \(\overline K_bw_r\), and injectivity of CW gives equality of every \(w_r\). Therefore \(\mathcal K_+\) is injective. Its exact action intertwining is
\[
\mathcal K_+\mathfrak F_\mu
=(W_\mu\otimes\mathrm{id})\mathcal K_+.
\tag{MQ2.5}
\]

This acts on the actual moving functions by
\(\mathcal K_+\operatorname{Ev}_W^{-1}\); (MQ1.2) supplies the explicit inverse rather than merely asserting one. Importantly, the coefficient is extracted before applying CW. A basis value
\([x\exp(-2\pi rY)]\) can cross the value \([1]\), even when \(x>1\). Nothing in (MQ2.4) treats such a moving value as a positive constant coefficient. MQ6 below provides a separate pointwise map that retains those crossings.

## MQ3. Geometric realization of the coefficientwise receiver and full zero jets

The target \(Q\otimes\mathbb C[\mathbb Q]\) has the faithful geometric realization
\[
\operatorname{Ev}_{Q,\lambda}
\left(\sum_r v_r\mathbf u_r\right)(g,Y)
=\sum_r e_r(g)\exp(-2\pi r\lambda Y)v_r,
\qquad\lambda>0.
\tag{MQ3.1}
\]
Fourier integration at any \(Y_0\), followed by multiplication by
\(\exp(2\pi r\lambda Y_0)\), recovers \(v_r\). Thus even a fixed \(\lambda\) distinguishes this target's coefficients; retaining all \(\lambda\) additionally retains the original geometric character family.

The arithmetic action on the full target family is
\[
(\widehat{\mathfrak F}_\mu H)_\lambda(g,Y)
=W_\mu H_{\lambda\mu}(g,Y/\mu).
\tag{MQ3.2}
\]
Substitution in (MQ3.1) gives
\[
\widehat{\mathfrak F}_\mu\operatorname{Ev}_Q(v_r\mathbf u_r)
=\operatorname{Ev}_Q(W_\mu v_r\mathbf u_r),
\]
since \(-2\pi r(\lambda\mu)(Y/\mu)=-2\pi r\lambda Y\). The factors are retained in the calculation rather than suppressed.

For every actual nontrivial zero \(\rho\) of multiplicity \(m_\rho\), put
\[
A_\rho=\mathbb C[T_\rho]/(T_\rho^{m_\rho}),\quad
j_\rho([k])=\sum_{h=0}^{m_\rho-1}
\frac{F_k^{(h)}(\rho)}{h!}T_\rho^h.
\]
For \(x>1\), all moving jets are exactly
\[
(j_\rho\otimes\mathrm{id})\mathcal K_+([x]\mathbf u_r)
=B(\rho+T_\rho)(\log x)^\rho
\exp((\log\log x)T_\rho)\mathbf u_r,
\]
\[
B(\rho+T_\rho)=
\sqrt\pi\exp((\rho-\tfrac12)^2/4)
\exp((\rho-\tfrac12)T_\rho/2+T_\rho^2/4).
\tag{MQ3.3}
\]
The exponentials are taken with every surviving term modulo
\(T_\rho^{m_\rho}\). Arithmetic Frobenius acts by
\[
p^\rho\exp((\log p)T_\rho)\otimes\mathrm{id}
\tag{MQ3.4}
\]
on every frequency \(r\). No \(r\)-dependent numerical weight appears in this full action.

For every finite set of zeros and every finite set of rational frequencies, the map from \(V_+\otimes\mathbb C[\mathbb Q]\) to the product of the specified zero blocks at those frequencies is onto. CW4 proves simultaneous finite-zero interpolation; apply it separately to each frequency. These choices form a finite sum and therefore lie in the stated source.

The map to all zero blocks at all frequencies is injective. If every such jet vanishes, then for each of the finitely many source frequencies the complete CW4 observation vanishes; its injectivity forces that coefficient to be zero. No surjectivity onto the infinite product is asserted. In particular a source element has finite frequency support, whereas an arbitrary element of that product need not.

## MQ4. Separate geometric and coefficient scaling, with the complete radial family

Neither pure \(R(\mu)\) nor pure \(\theta_\mu\) preserves the original holomorphic algebra \(W[q^r]\) in general. The exact extension that accommodates both is
\[
\mathcal P_{\mathrm{rad}}
=W_{\mathrm{alg}}\otimes\mathbb C[\mathbb Q]\otimes\mathbb C[\mathbb R],
\]
with basis written \([x]\mathbf v_{r,c}\), and evaluation
\[
\operatorname{Ev}_{\mathrm{rad}}([x]\mathbf v_{r,c})(g,Y)
=e_r(g)[x\exp(-2\pi cY)].
\tag{MQ4.1}
\]
Here \(c\) is a named radial frequency, independent of primitive \(\tau\). Multiplication multiplies \(x\) and adds the two frequency coordinates.

This evaluation is injective. Fourier projection separates the finite set of \(r\)'s. For a fixed \(r\), combine duplicate pairs \((\log x,c)\). Distinct pairs yield distinct affine functions
\(\log x-2\pi cY\), except at finitely many intersection values of \(Y\). Choose any \(Y>0\) outside this finite set. Their \(W\)-basis values are then distinct, so vanishing of the evaluated sum forces every combined coefficient to be zero.

The exact actions are
\[
R(v):[x]\mathbf v_{r,c}\longmapsto[x]\mathbf v_{r,vc},
\]
\[
\theta_\mu:[x]\mathbf v_{r,c}\longmapsto[x^\mu]\mathbf v_{r,\mu c},
\]
\[
\mathfrak F_\mu=\theta_\mu R(\mu^{-1}):
[x]\mathbf v_{r,c}\longmapsto[x^\mu]\mathbf v_{r,c}.
\tag{MQ4.2}
\]
These follow directly from (MQ4.1), so their representation and commutation laws hold on the evaluated functions as well.

The source holomorphy condition identifies the diagonal exactly:
\[
L_\lambda\chi_\lambda
\bigl(\operatorname{Ev}_{\mathrm{rad}}([x]\mathbf v_{r,c})\bigr)
=2\pi i\lambda Y(r-c)\,
e_r(g)x^\lambda\exp(-2\pi c\lambda Y).
\tag{MQ4.3}
\]
For a finite sum annihilated for every \(\lambda>0\), Fourier projection separates \(r\). At a positive \(Y\) avoiding the finitely many intersections used above, the values \(x\exp(-2\pi cY)\) are distinct. Their complete character evaluations are linearly independent by the Vandermonde calculation in MQ1. Since \(2\pi i\lambda Y\ne0\), every coefficient with \(c\ne r\) must vanish. Conversely each \(c=r\) term is annihilated by (MQ4.3). Hence
\[
\boxed{\text{The holomorphic subalgebra in }\mathcal P_{\mathrm{rad}}
\text{ is exactly }W_{\mathrm{alg}}\otimes
\operatorname{span}\{\mathbf v_{r,r}:r\in\mathbb Q\}.}
\tag{MQ4.4}
\]
This is the original moving algebra under \(\mathbf u_r\mapsto\mathbf v_{r,r}\).

On \(V_+\)-coefficients the map
\(\overline K_b\otimes\mathrm{id}\otimes\mathrm{id}\) is again injective. Its target operations are
\[
R(v):(v_0,r,c)\mapsto(v_0,r,vc),\quad
\theta_\mu:(v_0,r,c)\mapsto(W_\mu v_0,r,\mu c),\quad
\mathfrak F_\mu:(v_0,r,c)\mapsto(W_\mu v_0,r,c).
\]
Thus the larger representation retains both separate actions; the original holomorphic diagonal is preserved by their arithmetic combination.

## MQ5. A faithful map for all constant \(W\)-coefficients, retaining the unit and both signs

To include the source coefficient \([1]\) and all moving evaluations, use the exact invariant decomposition
\[
W_{\mathrm{alg}}=\mathbb C[1]\oplus V_+\oplus V_-,
\qquad V_-=\operatorname{span}\{[x]:0<x<1\}.
\]
Define
\[
\widehat Q=\mathbb C\oplus Q_+\oplus Q_-,
\qquad \widehat W_\mu=\mathrm{id}_{\mathbb C}\oplus W_\mu\oplus W_\mu,
\]
where \(Q_+\) and \(Q_-\) are two distinguished copies of the actual original-zeta quotient. Set
\[
J([1])=(1,0,0),
\]
\[
J([x])=
\begin{cases}
(0,\overline K_b[x],0),&x>1,\\
(0,0,\overline K_b[x^{-1}]),&0<x<1.
\end{cases}
\tag{MQ5.1}
\]
This preserves the sign of \(\log x\) as an explicit summand; it does not identify \([x]\) with \([x^{-1}]\).

The map \(J\) is injective, because the three source summands are disjoint and each nontrivial summand map is CW's injection composed, for \(V_-\), with the bijection \([x]\mapsto[x^{-1}]\). It intertwines every positive real scaling:
\[
J\theta_\mu=\widehat W_\mu J,
\tag{MQ5.2}
\]
since \(x^\mu\) stays in the same sign sector and
\((x^\mu)^{-1}=(x^{-1})^\mu\).

The original multiplicative law is also recoverable without asserting that \(J\) is a homomorphism for an unstated product on \(Q\). Let
\(\mathsf v_t=J([e^t])\), \(t\in\mathbb R\). These are a linearly independent basis of \(J(W_{\mathrm{alg}})\). Define the transported product there by
\[
\mathsf v_t\star\mathsf v_u=\mathsf v_{t+u}.
\tag{MQ5.3}
\]
This is associative and commutative by addition of the original real logarithms, with unit \(\mathsf v_0\). It retains transitions between sign sectors and every source product, and makes \(J\) an algebra isomorphism onto this explicitly supplied image algebra. No ordinary quotient multiplication on \(Q\) is assumed.

The full coefficientwise moving map
\[
J\otimes\mathrm{id}:\mathcal P\longrightarrow
\widehat Q\otimes\mathbb C[\mathbb Q]
\tag{MQ5.4}
\]
is injective and intertwines arithmetic Frobenius with
\(\widehat W_\mu\otimes\mathrm{id}\). This includes every original \(q^r\), whose source coefficient is \([1]\).

## MQ6. The actual pointwise moving map and every crossing

There is also a direct map on the original moving functions:
\[
\boxed{
\mathcal J_{\mathrm{mov}}(F)(g,Y)
=J\bigl(\operatorname{Ev}_W(F)(g,Y)\bigr).}
\tag{MQ6.1}
\]
It takes values in \(\widehat Q\), is linear, and is injective because both \(J\) and \(\operatorname{Ev}_W\) are injective.

The same formula with \(\operatorname{Ev}_{\mathrm{rad}}\) gives an injective map on the larger space in MQ4. Thus its separate coefficient and geometric actions are also defined there, even when they move a holomorphic diagonal term away from that diagonal.

For a source basis function \([x]q^r\), put
\[
\eta(x,r,Y)=\log x-2\pi rY.
\]
Its exact image is
\[
\mathcal J_{\mathrm{mov}}([x]\mathbf u_r)(g,Y)
=e_r(g)
\begin{cases}
(0,\overline K_b[e^{\eta(x,r,Y)}],0),&\eta(x,r,Y)>0,\\
(1,0,0),&\eta(x,r,Y)=0,\\
(0,0,\overline K_b[e^{-\eta(x,r,Y)}]),&\eta(x,r,Y)<0.
\end{cases}
\tag{MQ6.2}
\]
In particular the crossing height, whenever positive, is
\[
Y=\frac{\log x}{2\pi r}.
\]
The unit is retained at the crossing, and the two sides remain in different copies of \(Q\). There is no positive dilation by zero.

The actual action on this function receiver is
\[
(\mathfrak F_\mu^{\mathrm{mov}}H)(g,Y)
=\widehat W_\mu H(g,Y/\mu).
\tag{MQ6.3}
\]
Equations (MQ2.1) and (MQ5.2) prove
\[
\mathcal J_{\mathrm{mov}}\mathfrak F_\mu
=\mathfrak F_\mu^{\mathrm{mov}}\mathcal J_{\mathrm{mov}}.
\]
On (MQ6.2), the complete identity is
\[
\log(x^\mu)-2\pi rY
=\mu\bigl(\log x-2\pi rY/\mu\bigr).
\tag{MQ6.4}
\]
Its positive multiplier preserves the sign, takes the crossing to its correct new height, and applies \(W_\mu\) in the corresponding quotient summand.

The coefficientwise map (MQ5.4) and the pointwise map (MQ6.1) are exactly related on their images, not identified without a comparison:
\[
\mathcal T=
\mathcal J_{\mathrm{mov}}\circ
(J\otimes\mathrm{id})^{-1}.
\tag{MQ6.5}
\]
The inverse of \(J\) on its image is unique by its injection; (MQ1.2) explicitly recovers the frequency coefficients from the moving function. Thus (MQ6.5) is a bijection of the two images intertwining their stated arithmetic actions. Formula (MQ6.2) evaluates it on every basis vector.

We do not assert differentiability of (MQ6.2) in an unstated topology on \(\widehat Q\) at its crossings. The source's exact holomorphic observation structure has an explicit return. Define, on \(J(W_{\mathrm{alg}})\),
\[
\widetilde\chi_\lambda=\chi_\lambda J^{-1}.
\]
On the three basis types in (MQ5.1), its values are respectively \(1,x^\lambda,x^\lambda\), retaining the original \(x<1\) in the last case. Hence
\[
\widetilde\chi_\lambda\mathcal J_{\mathrm{mov}}(F)
=\chi_\lambda\operatorname{Ev}_W(F).
\tag{MQ6.6}
\]
Every source scalar holomorphic equation is therefore recovered exactly. This proves a relation of the specified character-observed objects, without silently substituting an unrelated distributional or Hilbert topology.

## MQ7. The original \(q^r\) itself: apparent zero weights and their exact cancellation

Take \(x=1\). For \(r>0\), (MQ6.2) becomes
\[
\mathcal J_{\mathrm{mov}}(\mathbf u_r)(g,Y)
=e_r(g)(0,0,\overline K_b[\exp(2\pi rY)]).
\]
For \(r<0\) it is
\[
e_r(g)(0,\overline K_b[\exp(-2\pi rY)],0),
\]
and \(r=0\) gives \((1,0,0)\). Every nonzero rational frequency is retained, including its sign.

For either nonzero sign, the complete actual-zero jet in its designated summand is
\[
e_r(g)\,
\sqrt\pi\exp((\rho-\tfrac12)^2/4)
\exp((\rho-\tfrac12)T_\rho/2+T_\rho^2/4)
(2\pi|r|Y)^\rho
\exp(\log(2\pi|r|Y)T_\rho).
\tag{MQ7.1}
\]
The \(2\pi\), \(|r|\), height, Gaussian factor and every nilpotent coefficient are explicit. Its length is the actual \(m_\rho\).

Pure geometric scaling \(Y\mapsto pY\) multiplies (MQ7.1) by
\(p^\rho\exp((\log p)T_\rho)\). The coefficient action alone supplies the same multiplier. In the full arithmetic Frobenius, the geometric argument is instead \(Y/p\), and the two factors cancel exactly:
\[
p^\rho e^{(\log p)T_\rho}\,
(2\pi|r|Y/p)^\rho e^{\log(2\pi|r|Y/p)T_\rho}
=(2\pi|r|Y)^\rho e^{\log(2\pi|r|Y)T_\rho}.
\tag{MQ7.2}
\]
The Gaussian factor commutes with these multiplications and remains unchanged. Thus the full moving image of each \(q^r\) is arithmetic-Frobenius invariant, exactly as the original source proves.

This explains precisely why a zero-jet power seen at fixed height cannot be declared a new arithmetic weight of \(q^r\). The full operator also changes that height. For general constant \(W\)-coefficients, their nontrivial arithmetic action remains as in MQ2–MQ3; the original \(q^r\) factors themselves contribute the invariant representation. Neither conclusion fixes \(\Re\rho\).

## MQ8. Full left rational affine action, finite valuation frame, and the classical quotient

Retain the original covering action
\[
\ell(a,b)(X_f,X_\infty,Y_f,Y_\infty)
=(aX_f+b,aX_\infty+b,aY_f,aY_\infty),
\quad a\in\mathbb Q_{>0},\ b\in\mathbb Q.
\tag{MQ8.1}
\]
Define the actual covering functions
\[
U_r(X,Y)
=\psi_f(rX_f)\exp(2\pi irX_\infty)
[\exp(-2\pi rY_\infty)]
=\alpha(rX)[\exp(-2\pi rY_\infty)].
\tag{MQ8.2}
\]
The standard global additive character satisfies
\(\psi_f(rb)\exp(2\pi irb)=\alpha(rb)=1\) for rational \(rb\). Hence
\[
\boxed{U_r\circ\ell(a,b)=U_{ar}.}
\tag{MQ8.3}
\]
Both the finite phase and the archimedean phase are retained and cancel; dropping the finite phase would give an incorrect extra factor. More generally, a finite locally constant coefficient \(f\) transforms by
\[
(fU_r)\circ\ell(a,b)=(f\circ L_f(a,b))U_{ar}.
\tag{MQ8.4}
\]
Constant \(W\)-coefficients are unchanged by this geometric pullback.

For the larger radial functions the same calculation sends
\((r,c)\mapsto(ar,ac)\), with no global rational-translation phase. It commutes with the arithmetic action in MQ4. On the coefficientwise receivers it acts on frequency labels, together with the stated pullback of finite coefficients; it does not introduce an unstated Mellin eigenvalue on the constant \(W\)-coefficient.

The original quotient's \(q^r\) is related to these covering functions by a precise frame-dependent frequency. On the classical preimage suppose \(Y_f\) is a finite idele. Define its positive rational valuation representative and retained unit part by
\[
c(Y_f)=\prod_p p^{v_p(Y_p)}\in\mathbb Q_{>0},
\qquad Y_f=c(Y_f)u_f,\quad u_f\in\widehat{\mathbb Z}^{\,*}.
\tag{MQ8.5}
\]
Only finitely many factors are different from one. The source's quotient by finite units and left positive rationals gives its classical coordinates
\[
g=[X/c(Y_f)]\in G,\qquad
Y=Y_\infty/c(Y_f).
\tag{MQ8.6}
\]
These formulas can also be proved directly: multiplication by \(c(Y_f)^{-1}\) sends the finite \(Y\) valuations to zero, finite units then send \(Y_f/c(Y_f)\) to one, and diagonal rational translations identify \(X/c(Y_f)\) modulo \(\mathbb Q\).

The pullback of the original quotient function is therefore
\[
\boxed{
q^r(g,Y)=
\alpha\!\left(\frac{rX}{c(Y_f)}\right)
[\exp(-2\pi rY_\infty/c(Y_f))]
=U_{\,r/c(Y_f)}(X,Y).}
\tag{MQ8.7}
\]
Under (MQ8.1),
\[
c(aY_f)=ac(Y_f),\qquad
\left[\frac{aX+b}{ac(Y_f)}\right]
=\left[\frac{X}{c(Y_f)}\right],\qquad
\frac{aY_\infty}{ac(Y_f)}=\frac{Y_\infty}{c(Y_f)}.
\]
The middle identity holds because \(b/(ac(Y_f))\in\mathbb Q\). Equivalently,
\[
U_{\,r/(ac(Y_f))}\circ\ell(a,b)
=U_{\,r/c(Y_f)}.
\tag{MQ8.8}
\]
Thus the original quotient \(q^r\) is invariant under the covering gauge action, whereas a fixed-frequency cover function \(U_r\) changes frequency as in (MQ8.3). These are related by the explicit map (MQ8.7). On the representative with \(c(Y_f)=1\), \(U_r\) restricts to \(q^r\).

The valuation representative is retained as part of this comparison. No assertion is made that it extends as a locally constant function on all of \(\mathbb A_f\), or across \(Y_f=0\). The idele topology makes it locally constant on finite ideles; the subspace topology inherited from additive \(\mathbb A_f\) need not do so. Equations (MQ8.5)–(MQ8.8) are pointwise identities on the stated classical preimage and identify the exact quotient maps. They do not turn the original classical orbit into the finite boundary \(Y_f=0\).

For completeness there is a different, explicitly defined self-map of the classical-coordinate product:
\[
A_{a,b}(g,Y)=(ag+\iota_\infty(b),aY),
\quad a\in\mathbb Q_{>0},\ b\in\mathbb R.
\]
Its pullback satisfies
\[
A_{a,b}^*q^r=\exp(2\pi irb)q^{ar}.
\tag{MQ8.9}
\]
The calculation uses only (MQ0.2). This coordinate self-map is not the diagonal covering gauge action (MQ8.1), which also rescales the finite valuation frame. Equation (MQ8.7) supplies their precise difference. The phases in (MQ8.9) compose consistently:
\(A_{a,b}A_{a',b'}=A_{aa',ab'+b}\), and pullbacks compose in the reverse order.

## MQ9. Result and source-reading record

The established objects are:

1. An injective geometric evaluation of the complete finite algebra \(W[q^r]\), with an explicit Fourier return for every rational frequency.
2. An injective moving coefficient map from \(V_+\otimes\mathbb C[\mathbb Q]\) to \(Q\otimes\mathbb C[\mathbb Q]\), with the complete original-zero multiplicities and all prime actions.
3. An exact larger radial-frequency representation in which separate geometric and coefficient scalings are retained and the original holomorphic subalgebra is calculated, not assumed.
4. A faithful extension of CW to all \(W\)-coefficients using \(\mathbb C\oplus Q_+\oplus Q_-\), and a pointwise map of the original moving functions retaining every crossing through \([1]\).
5. The exact comparison between covering \(U_r\), the finite valuation frame, and the quotient's invariant \(q^r\).

These are actual representation and geometric-evaluation maps. The displayed source multiplication is retained by its specified transported image law; ordinary quotient multiplication, a positive metric and a full purity theorem are not inferred. On the proved image, nonzero \(q\)-frequencies supply invariant factors for the full arithmetic Frobenius, while their fixed-height zero-jet powers have the explicitly calculated cancellation (MQ7.2).

Read in this derivation:

- CORPUS_AND_OPERATION_RULES.md completely.
- The complete preserved user passages USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2 and USR-6152e3bc6302258c.
- CC_W_MELLIN_INDEPENDENT.md CW0–CW7, whose complete proofs provide the original quotient injection, finite-jet interpolation and label functor.
- Original author thecurve_K.tex: §5.1 Lemma adelicomp and its proof; §5.2 equations actionpq, algspaceiota and Lemma Pdescrofgamma; §5.4 lines 1634–1708, including Jdefn1, the complete classical right action, classorb1 and proetcov; §7.1 lines 2560–2626, including holom, holombis, holom1, frobarith, holom2, functionq and perfectoid. These are bounded reading passages, not a whole-paper reading claim.

The source authors are Alain Connes and Caterina Consani. The original-zeta count used by CW3 is due to Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, [Counting zeros of the Riemann zeta function, arXiv:2107.06506v1](https://arxiv.org/abs/2107.06506v1), Corollary 1.2; its full constants and proof-use record remain in CW3. The MQ comparisons and all claims about their exact receiving maps are derived above, without a historical novelty claim.

Every linear map here extends to the programme's already specified labelled receiver by
\[
(v,\ell)\longmapsto(f(v),\ell).
\]
CW7 proves this functor preserves its receiving operations and labels, including zero amplitudes. Applying it to each stated linear map retains every support label. Neither a source \(\tau\) nor a support label is assigned the numerical coordinate of a \(W\)-basis element, a Fourier frequency, or a zeta jet.
