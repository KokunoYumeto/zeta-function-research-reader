# Gaussian spectral synthesis on the complete original source

Complete derivation, stable locators **GSP0–GSP9**. This is programme mathematics. The independent verification is recorded separately; this file does not imply its own acceptance.

## GSP0. Construction stage, question, and prior inputs

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). All coefficient spaces and arithmetic actions below occur after the complete-history reconstruction. Each branch retains its own recovered counter. None of the following arithmetic, spectral coordinates, seminorms, or operations is an operation on that support. Addition at the support remains retracted.

The current construction guide, connected argument and correction table were recalled, including the full WU050–WU051, WU061–WU062 and WU064–WU065 passages. The new attempt combines results already obtained: RZ's actual global resolvent and finite full-jet projectors, S3's original-source Hadamard estimate, and GAP's Gaussian approximation on the full Fréchet quotient. The question is whether the finite spectral projectors recover that quotient in its original topology, rather than only its value receiver. SDT7 explicitly established strong density of jet **functionals** without claiming this primal density. PSC3 retained the algebraic reconstruction quotient without assuming its Hausdorff quotient was zero. These are the points addressed here.

Publication source credit: The factorization theorem is due to Jacques Hadamard. The inspected author-source witness is Alain Connes, [arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), original rhready.tex lines526-535; its exact source hash and historical attribution are retained in the [preceding synthesis, source identity and S3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/GLOBAL_MELLIN_SYNTHESIS.md). The full genus-one product is retained. Hadamard's 1892 original was not newly read.

The proof uses RZ1–RZ7 and its original representative corrections in ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md; GLOBAL_MELLIN_SYNTHESIS.md S2–S3 for the complete original divisor and the proved lower bound away from small zero disks; GAP1–GAP2 for bounded-set Gaussian approximation; ADM1–ADM3 for the actual specialization source; and PSC2–PSC3 for the reconstruction sequence. The underlying human-source identities and reading scopes remain those of these input proofs. This derivation is not a new claim to have read an entire human paper.

## GSP1. Original objects and all factors

Retain the original source
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\ f(0)=0,
\ \int_{\mathbb R}f(v)\,dv=0\},
\quad \Sigma f(u)=2\sum_{n\ge1}f(nu),
\]
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty\ \forall N,j\ge0\},
\quad J=\Sigma S,\quad Q=A/J.
\tag{GSP1.1}
\]
The exact-image theorem proves that \(J\) is closed. The actual half-Mellin comparison is
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}{\pi}
\int_{\mathbb R}F(1/2+it)u^{-it}\,dt.
\tag{GSP1.2}
\]
It identifies \(A\) with the complete Fréchet space
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):
b_{a,N}(F)=\sup_{|\Re s|\le a}(1+|\Im s|)^N|F(s)|<\infty
\ \forall a,N\ge0\}.
\tag{GSP1.3}
\]
The image of \(J\) is exactly the closed ideal \(\mathcal I\) of full vanishing jets at the actual nontrivial zeros \(\rho\) of original \(\zeta\), with orders \(m_\rho\). Write \(\mathcal Q=\mathcal B/\mathcal I\), and
\[
q_{a,N}([F])=\inf_{H\in\mathcal I}b_{a,N}(F+H).
\tag{GSP1.4}
\]
These are the original quotient seminorms. No product topology on unrestricted jets is substituted for them.

The entire source element and its original arithmetic formula remain
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
F_0(s)=\Theta\Sigma f_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{GSP1.5}
\]
Its zeros are precisely those actual nontrivial zeros, with their full orders. The exceptional values are
\[
F_0(0)=F_0(1)=\frac18,\qquad F_0(-1)=F_0(2)=\frac\pi{24},
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)
=F_0(1+2k)\ne0\quad(k\ge1).
\tag{GSP1.6}
\]
At any \(\rho\), all local coefficients are calculated from
\[
F_0(\rho+z)=z^{m_\rho}
\frac{(\rho+z)(\rho+z-1)}8\pi^{-(\rho+z)/2}
\Gamma((\rho+z)/2)\frac{\zeta(\rho+z)}{z^{m_\rho}}.
\tag{GSP1.7}
\]
Every derivative of this product is its complete Leibniz sum. The original unit and repetitions are retained as
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'(s)}{\zeta(s)}=\sum_p\sum_{k\ge1}(\log p)p^{-ks}
\quad(\Re s>1).
\tag{GSP1.8}
\]
The older RZ Mellin presentation uses \(\mathcal Mk(s)=\int k(u)u^{s-1/2}du/u\). Its exact comparison is \(k(u)=u^{1/2}a(u)/2\), so \(\mathcal Mk=\Theta a\). Thus its generator \(1/2-u\partial_u\) on \(k\) corresponds to \(-u\partial_u\) on \(a\), and both correspond to multiplication by the original \(s\). This factor is not discarded when importing the RZ formulas.

## GSP2. A uniform resolvent estimate on the actual contour

Let \(L[F]=[sF]\). For \(\lambda\) outside the actual divisor, RZ3 constructs
\[
\mathscr R_\lambda F(s)
=\frac{F(s)-F_0(s)F(\lambda)/F_0(\lambda)}{\lambda-s},\qquad
R_\lambda[F]=[\mathscr R_\lambda F]=(\lambda-L)^{-1}[F].
\tag{GSP2.1}
\]
The numerator vanishes at \(s=\lambda\); its removable value is
\(-F'(\lambda)+F_0'(\lambda)F(\lambda)/F_0(\lambda)\).
The correction containing the full \(F_0\) is essential. The two identities before quotienting are
\[
(\lambda-s)\mathscr R_\lambda F=F-F_0F(\lambda)/F_0(\lambda),
\quad \mathscr R_\lambda((\lambda-s)F)=F.
\tag{GSP2.2}
\]
RZ2 proves entire division in each original seminorm. More explicitly, for \(|\Re\lambda|\le2\), put \(a'=\max(a,4)\). Its estimate gives a constant \(C_{a,N}\), independent of \(\lambda\) and \(F\), with
\[
b_{a,N}(\mathscr R_\lambda F)
\le C_{a,N}(2+|\Im\lambda|)^N
\bigl(1+|F_0(\lambda)|^{-1}\bigr)b_{a',N}(F).
\tag{GSP2.3}
\]
Indeed the numerator is bounded by
\(b_{a,N}(F)+|F_0(\lambda)|^{-1}b_{a,N}(F_0)b_{a',0}(F)\).
Outside \(|s-\lambda|<1\), division only decreases its absolute value. On the unit disk, the maximum principle for its entire divided function bounds it by half the numerator supremum on the radius-two circle, contained in \(|\Re s|\le4\); the output weight is at most \((2+|\Im\lambda|)^N\). This proves (GSP2.3) with the same input strip. Taking the infimum over representatives proves the corresponding bound for \(q_{a,N}(R_\lambda[F])\).

For completeness specify precisely the growth estimate being imported. S2–S3 proves the genus-one factorization of the complete (GSP1.5), the count \(\sum_{|\rho|\le R}m_\rho\le C(R+2)^{3/2}\), and the following bound. Let \(D_R\) be the union of radius \(R^{-2}\) disks around the zeros with \(|\rho|\le8R\). For sufficiently large \(R\),
\[
|F_0(\lambda)|^{-1}\le
\exp(CR^{3/2}\log R)
\quad(R/2\le|\lambda|\le3R,\ \lambda\notin D_R).
\tag{GSP2.4}
\]
It follows by retaining every factor in the Hadamard product: the finitely many factors have \(|1-\lambda/\rho|\ge1/(8R^3)\), their exponentials contribute at worst \(-CR^{3/2}\) to the logarithm, and the full remaining genus-one tail contributes at worst \(-CR^{3/2}\) because \(\sum_{|\rho|>8R}m_\rho|\rho|^{-2}\le CR^{-1/2}\). The affine exponential in the factorization is retained in the constant. No lower bound on distances between zeros enters this estimate.

The vertical lines \(\Re\lambda=-2,2\) have distance at least one from the divisor. Applying (GSP2.4) with \(R=|\Im\lambda|\) at large height and using the nonzero minimum on the remaining compact segments gives
\[
1+|F_0(\pm2+iy)|^{-1}\le C_0\exp(C_0\omega(y)),
\quad \omega(y)=(|y|+2)^{3/2}\log(|y|+2).
\tag{GSP2.5}
\]
The constants here depend on the original \(F_0\), not on \(F\) or an assumed RH.

## GSP3. The infinite contour gives the exact Gaussian multiplier

Put \(g_t(\lambda)=e^{t\lambda^2}\), \(t>0\). On either vertical line,
\[
|g_t(\pm2+iy)|=e^{4t-ty^2}.
\tag{GSP3.1}
\]
Equations (GSP2.3)–(GSP2.5) therefore make the following two improper integrals converge in every quotient seminorm, uniformly on bounded input sets:
\[
\mathcal C_t=
\frac1{2\pi i}\left(
\int_{2-i\infty}^{2+i\infty}g_t(\lambda)R_\lambda\,d\lambda
-\int_{-2-i\infty}^{-2+i\infty}g_t(\lambda)R_\lambda\,d\lambda
\right).
\tag{GSP3.2}
\]
The second sign is the positive orientation of the left side. Existence can be checked on the representatives (GSP2.1) in the complete space \(\mathcal B\) with the same estimates, then passed to the quotient. RZ4's parameter holomorphy justifies each finite contour integral.

To identify the result, retain every derivative at a given zero \(\rho\). On its order-\(m_\rho\) jet, \(R_\lambda\) acts by the Taylor jet of \(1/(\lambda-s)\). Thus the jet of (GSP3.2) is the jet of
\[
F(s)\frac1{2\pi i}\left(
\int_{2-i\infty}^{2+i\infty}\frac{g_t(\lambda)}{\lambda-s}d\lambda
-\int_{-2-i\infty}^{-2+i\infty}\frac{g_t(\lambda)}{\lambda-s}d\lambda
\right)
=g_t(s)F(s),\quad -2<\Re s<2.
\tag{GSP3.3}
\]
The scalar equality is Cauchy's formula on finite rectangles followed by the limit: the two horizontal scalar integrals tend to zero because their lengths are four and their numerators are bounded by \(e^{4t-tT^2}\). The same argument on a small disk around \(\rho\) permits every required derivative. Continuous jet functionals commute with the seminorm-convergent vector integral. Equality of all full jets is equality in the original \(\mathcal Q\), so
\[
\boxed{\mathcal C_t=m_{g_t}\quad\text{on the whole original }\mathcal Q.}
\tag{GSP3.4}
\]
This is an equality on the complete source, not only its value image. The representatives of the two sides may differ by a member of the retained original ideal \(\mathcal I=\Theta J\); no equality before that quotient has been asserted.

## GSP4. One sequence of finite full-jet operators converges on the full source

Choose, for every sufficiently large positive integer \(j\), \(R_j=j^6\). The projection of \(D_{R_j}\) onto imaginary heights has total length at most
\[
2R_j^{-2}\sum_{|\rho|\le8R_j}m_\rho\le C R_j^{-1/2}<1.
\tag{GSP4.1}
\]
The actual zero set is invariant under complex conjugation. Consequently the union of excluded height intervals is symmetric. Choose \(T_j\in[R_j,R_j+1]\) outside that union; then both horizontal segments \(\Im\lambda=\pm T_j\), \(-2\le\Re\lambda\le2\), avoid the disks. For the finitely many smaller \(j\), choose any positive zero-free contour heights. Those choices do not affect convergence. Let \(\Gamma_j\) be the positively oriented rectangle with these sides, and set
\[
K_j=\frac1{2\pi i}\int_{\Gamma_j}e^{\lambda^2/j}R_\lambda\,d\lambda.
\tag{GSP4.2}
\]
For each enclosed zero let \(P_\rho\) be the RZ full-jet projector and \(N_\rho=(L-\rho)|_{P_\rho\mathcal Q}\), with \(N_\rho^{m_\rho}=0\). The entire finite residue formula is
\[
K_j=\sum_{|\Im\rho|<T_j}\sum_{a=0}^{m_\rho-1}
\frac{g_{1/j}^{(a)}(\rho)}{a!}(L-\rho)^aP_\rho.
\tag{GSP4.3}
\]
It follows directly from the retained resolvent Laurent expansion
\(R_\lambda=\sum_{a=0}^{m_\rho-1}(L-\rho)^aP_\rho/(\lambda-\rho)^{a+1}+\text{holomorphic}\).
In particular all nilpotent coefficients and all original multiplicities remain. Since \(g_{1/j}(\rho)\ne0\), the restriction to each enclosed block is invertible and \(\operatorname{rank}K_j=\sum_{|\Im\rho|<T_j}m_\rho\).

Here is the full convergence estimate. On a horizontal side, (GSP2.3)–(GSP2.4) bound the output seminorm by a constant times
\[
(2+T_j)^N\exp\{-T_j^2/j+4/j+C R_j^{3/2}\log R_j\}
q_{a',N}(F).
\tag{GSP4.4}
\]
The side length is four. The exponent's negative term is at most \(-j^{11}\), whereas its positive growing term is \(6Cj^9\log j\); therefore the expression tends to zero for every fixed \(a,N\).

For the two omitted vertical tails use (GSP2.5). For all sufficiently large \(j\) and all \(y\ge T_j\),
\(C_0\omega(y)\le y^2/(2j)\), because \(\omega(y)/y^2\) decreases to zero beyond a fixed height and at \(j^6\) its product with \(j\) is \(O(j^{-2}\log j)\). Their integral is consequently bounded by a constant times
\[
q_{a',N}(F)e^{4/j}\int_{T_j}^\infty(2+y)^N e^{-y^2/(2j)}dy\longrightarrow0.
\tag{GSP4.5}
\]
For an explicit justification of the last limit, split the exponential into two equal factors, bound one by \(e^{-T_j^2/(4j)}\), and integrate the other over \([0,\infty)\). After \(y=\sqrt j\,v\), that integral is at most \(C_N j^{(N+1)/2}\) for \(j\ge1\). The exponential dominates this polynomial. These estimates use one fixed input seminorm for each fixed output seminorm and are uniform on bounded input sets.

By (GSP3.4), the difference just estimated is \(K_j-m_{g_{1/j}}\). GAP1 gives independently
\[
q_{a,N}((m_{g_{1/j}}-1)F)
\le j^{-1}e^{a^2/j}(a^2+1)q_{a,N+2}(F).
\tag{GSP4.6}
\]
Combining these estimates proves
\[
\boxed{K_j\longrightarrow1_{\mathcal Q}
\text{ uniformly on every bounded subset of the original }\mathcal Q.}
\tag{GSP4.7}
\]
No bounded zero-height scan, spectral gap, separation of neighboring zeros, or simple-zero hypothesis replaces this global limit. The finite contours define the approximating operators; their limit is proved over the complete actual divisor.

One may also write every \(K_j\) as an actual entire multiplier. RZ5 supplies \(e_\rho\in\mathcal B\) whose full jet is one at \(\rho\) and zero at every other zero. It is constructed from \(F_0(s)/(s-\rho)^{m_\rho}\) times its reciprocal Taylor polynomial at \(\rho\), retaining all coefficients (GSP1.7). Then
\[
k_j(s)=\sum_{|\Im\rho|<T_j}e_\rho(s)
\sum_{a=0}^{m_\rho-1}\frac{g_{1/j}^{(a)}(\rho)}{a!}(s-\rho)^a
\in\mathcal B\subset M,\qquad K_j=m_{k_j}\text{ on }\mathcal Q.
\tag{GSP4.8}
\]
The equality follows on every full jet. Multiplication \(m_{k_j}\) on the representative space \(\mathcal B\) is not asserted finite rank. The representative **contour** operator does have the finite-rank lift proved in RZ7:
\[
\mathscr K_jF=\sum_{|\Im\rho|<T_j}\sum_{a=0}^{m_\rho-1}
\frac{g_{1/j}^{(a)}(\rho)}{a!}\mathscr C_{\rho,a}F,
\quad
\mathscr C_{\rho,a}F(s)=A_\rho(s)(s-\rho)^a
\operatorname{Tay}_{\rho,<m_\rho-a}(F/A_\rho)(s),
\quad A_\rho(s)=\frac{F_0(s)}{(s-\rho)^{m_\rho}}.
\tag{GSP4.9}
\]
The Taylor division is at \(\rho\), where \(A_\rho(\rho)\ne0\). The outputs are entire original source functions. This lift annihilates \(\mathcal I\) and descends continuously from \(\mathcal Q\) to \(\mathcal B\); its quotient is \(K_j\). Its difference from \(m_{k_j}\) has image in \(\mathcal I\). The convergence proved in (GSP4.7) is in \(\mathcal Q\); no convergence \(\mathscr K_jF\to F\) in \(\mathcal B\) is asserted.

## GSP5. Closed multiplier submodules have exact full-jet synthesis

Write \(\mathcal Q_\rho=P_\rho\mathcal Q\simeq\mathbb C[z]/(z^{m_\rho})\), with \(z=L-\rho\). Equation (GSP4.7) first proves
\[
\overline{\bigoplus_{\rho\in\mathscr Z}\mathcal Q_\rho}^{\ \mathcal Q}=\mathcal Q.
\tag{GSP5.1}
\]
The direct sum means finite sums, followed by closure in the original quotient topology.

Now let \(X\) be any closed submodule for the full strip-polynomial multiplier ring \(M\). Each \(P_\rho=m_{e_\rho}\) preserves \(X\). Thus \(X_\rho=P_\rho X=X\cap\mathcal Q_\rho\) is a finite-dimensional \(\mathbb C[z]\)-submodule. There is a unique \(k_\rho\in\{0,\ldots,m_\rho\}\) with
\[
X_\rho=z^{k_\rho}\mathbb C[z]/(z^{m_\rho}).
\tag{GSP5.2}
\]
To prove this rather than assume a classification, take the least nonzero order \(k_\rho\) of any element when the submodule is nonzero. Such an element is \(z^{k_\rho}u(z)\) with \(u(0)\ne0\). Its inverse modulo \(z^{m_\rho}\) is a polynomial (the finite geometric series after its nonzero constant is factored). Polynomial multiplication therefore puts \(z^{k_\rho}\) and all higher powers in the submodule; minimality excludes lower orders. The zero submodule is the case \(k_\rho=m_\rho\).

Every \(K_j\) preserves \(X\) and has image in the finite sum of its \(X_\rho\). Conversely any class whose \(\rho\)-jet lies in \(X_\rho\) has \(K_jF\in X\) for all \(j\), and (GSP4.7) with closedness gives \(F\in X\). Hence the exact classification and its constructive limit are
\[
\boxed{X=\{[F]:F^{(a)}(\rho)=0\ (0\le a<k_\rho,\ \rho\in\mathscr Z)\}
=\overline{\bigoplus_\rho X_\rho}^{\ \mathcal Q}.}
\tag{GSP5.3}
\]
The numerical indices describe the already reconstructed coefficient jets. They are not parity labels placed on \(\tau\).

In particular this proves primal finite-jet density in \(N_O\), \(N_L\) and the all-value radical \(N_0\), as well as in the full source. Their orders are respectively: one at off-line zeros and zero at line zeros; one at line zeros and zero off the line; and one everywhere. Orders above zero remain capped by the full \(m_\rho\). It also applies to the full-jet sector kernels of PSC2. The subspaces have not been replaced by a Hilbert closure.

## GSP6. Exact consequence for the full source reconstruction defect

Use the actual sets \(\mathscr Z_L\) and \(\mathscr Z_O\), without asserting that the latter is empty. Set
\[
J_L=\{F\in\mathcal B:\operatorname{ord}_\rho F\ge m_\rho\ (\rho\in\mathscr Z_L)\},
\quad
J_O=\{F\in\mathcal B:\operatorname{ord}_\rho F\ge m_\rho\ (\rho\in\mathscr Z_O)\}.
\tag{GSP6.1}
\]
The actual intersection is \(\mathcal I\). PSC3's full reconstruction sequence remains
\[
0\longrightarrow\mathcal Q\xrightarrow{\Delta}
\mathcal B/J_L\oplus\mathcal B/J_O
\xrightarrow{([f],[g])\mapsto[f-g]}C_{\rm rec}\longrightarrow0,
\quad C_{\rm rec}=\mathcal B/(J_L+J_O).
\tag{GSP6.2}
\]
Every finite full-jet class lies in \((J_L+J_O)/\mathcal I\): an isolator at a line zero belongs to \(J_O\), and an isolator off the line belongs to \(J_L\). Equation (GSP5.1) therefore implies
\[
\boxed{\overline{J_L+J_O}=\mathcal B.}
\tag{GSP6.3}
\]
Here the closure is in \(\mathcal B\). Indeed the image of \(J_L+J_O\) is dense in the quotient; its preimage is dense because the quotient map is open and the subspace contains \(\mathcal I\). This proves the claimed source-topology statement.

It follows that the Hausdorff quotient of \(C_{\rm rec}\) is zero, and its continuous dual is zero. It does **not** follow that the algebraic vector space \(C_{\rm rec}\) is zero. The distinction is retained explicitly by (GSP6.2). The topology of a quotient by a dense proper vector subspace is non-Hausdorff; this is a property of that quotient, not a license to remove its vectors.

Moreover \(\Delta(\mathcal Q)\) is dense in the entire product in (GSP6.2). For explicit approximants to \(([f]_{J_L},[g]_{J_O})\), choose \(l_j\in J_L,o_j\in J_O\) with \(l_j+o_j\to f-g\), possible by (GSP6.3), and put \(F_j=f-l_j\). Then its first observation equals \([f]_{J_L}\) exactly, and its second tends to \([g]_{J_O}\), since \(F_j-g-o_j\to0\). The displayed product is consequently the Hausdorff completion of \(\mathcal Q\) for the topology induced by these two observations. It need not be the original quotient topology. Every compatibility class is still present in the algebraic sequence.

PSC3 proved that the inverse of \(\Delta\) on its image is continuous exactly when \(J_L+J_O\) is closed. Together with (GSP6.3), the precise remaining distinction is now whether the dense sum is the whole space; no positive completion or separation of weights has been inferred from its density.

## GSP7. The actual specialization and its continuous dual

Retain ADM's actual quotient and maps
\[
\mathcal R=\mathcal Q/N_O,\qquad
\beta_r=D_r^*\mathsf J E:\mathcal Q\to H_\infty,
\quad (\beta_rF)_\rho=\overline{d_r(\rho)}F(\rho^\#),
\]
\[
\rho^\#=1-\overline\rho,\quad
d_r(\rho)=e^{-i\Im\rho\log r}
(r^{\Re\rho}-r^{1-\Re\rho}),\quad r>1.
\tag{GSP7.1}
\]
This is the previously constructed original-source specialization. The finite contour operators preserve \(N_O\), because they are full multipliers. They induce finite-rank operators \(\overline K_j\) on \(\mathcal R\), and
\[
\overline K_j\longrightarrow1_{\mathcal R}
\text{ uniformly on bounded sets},\qquad
(\beta_rK_jF)_\rho=
\mathbf1_{\{|\Im\rho|<T_j\}}e^{(\rho^\#)^2/j}(\beta_rF)_\rho.
\tag{GSP7.2}
\]
For the first assertion, the single-input-seminorm estimates (GSP4.4)–(GSP4.6) pass through the quotient by taking infima over \(N_O\). They give the same convergence for its quotient seminorms. Alternatively AST's actual bounded lifts give bounded-set convergence directly. The second assertion is the reflected multiplier action proved in ADM3; the cutoff is reflection-invariant because \(\Im\rho^\#=\Im\rho\). Thus no source jet, reflected argument, or defect coefficient is lost before its specified quotient.

The finite-rank transposes also approximate the identity on the **full strong dual** of \(\mathcal Q\), and on that of \(\mathcal R\), uniformly on bounded subsets. Here is a direct topological proof. A strongly bounded dual set \(C\) is pointwise bounded, because singletons are bounded. A pointwise bounded family on a Fréchet space is equicontinuous: the closed sets \(\{x:\sup_{\ell\in C}|\ell(x)|\le n\}\) cover the space; Baire gives one with interior, and taking differences and scaling gives a common continuous-seminorm bound \(|\ell(x)|\le C_1p(x)\). For a bounded primal set \(D\), therefore,
\[
\sup_{\ell\in C}\sup_{x\in D}
|((K_j'-1)\ell)(x)|
\le C_1\sup_{x\in D}p((K_j-1)x)\longrightarrow0.
\tag{GSP7.3}
\]
The same proof uses \(\overline K_j\) for \(\mathcal R\). This constructs a specific common primal/dual approximation compatible with the actual source triangle, in addition to SDT7's earlier independent density argument.

All genuine integer cover coefficient actions commute with \(K_j\), because their source actions are multiplication by \(n^s\), and their traces retain \(n^{1-s}\). On a full order-\(m_\rho\) block these still act by
\[
T_n=n^\rho\sum_{a=0}^{m_\rho-1}\frac{(\log n)^a}{a!}N_\rho^a,
\qquad U_n=n^{1-\rho}\sum_{a=0}^{m_\rho-1}\frac{(-\log n)^a}{a!}N_\rho^a.
\tag{GSP7.4}
\]
The normal top-degree factor and both poles in ADM8/ACD7 remain as stated there. These commuting source maps are not an extra geometric cover or a Tate shift.

## GSP8. An actual continuous Gaussian lift and its full multiplier defect

Use the same two oriented infinite lines as in (GSP3.2), now with the original representative \(\mathscr R_\lambda\) of (GSP2.1), and call their integral \(\mathscr L_tF\in\mathcal B\). The estimates already proved give convergence in every original \(\mathcal B\) seminorm and continuity. On any \(F\in\mathcal I\), the parameter poles of \(\mathscr R_\lambda F\) disappear: the factor \(F(\lambda)/F_0(\lambda)\) is entire, and the removable diagonal is already handled by (GSP2.1). Thus every finite rectangle integral is zero. The horizontal and tail estimates for fixed \(t>0\) prove \(\mathscr L_tF=0\). Consequently this integral descends to an actual continuous map
\[
\mathcal L_t:\mathcal Q\longrightarrow\mathcal B,\qquad
q\mathcal L_t=m_{g_t},\quad q:\mathcal B\to\mathcal Q.
\tag{GSP8.1}
\]
Continuity on the quotient follows either from its definition or by taking the infimum in the input seminorm estimates. This proves an original-source lift of every Gaussian-regularized class. The underlying exact sequence is the original \(0\to\mathcal I\to\mathcal B\to\mathcal Q\to0\); a new extension has not been substituted. Its approximate sections satisfy \(q\mathcal L_t\to1\) uniformly on bounded subsets by GAP. No limit of \(\mathcal L_t\) in maps to \(\mathcal B\) has been asserted.

On the original half-Mellin source the exact lift is
\[
(\Theta^{-1}\mathcal L_tx)(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}(\mathcal L_tx)(1/2+iy)u^{-iy}\,dy.
\tag{GSP8.2}
\]
It belongs to \(A\) by the inverse-transform estimates of (GSP1.2), and represents the actual regularized class. Its discrepancy from the original Gaussian convolution source representative is in \(J=\Sigma S\). Neither that discrepancy nor its original Schwartz preimage is discarded.

To calculate exactly what this lift does to the arithmetic action, let \(h\in M\). Define the actual continuous map
\[
\mathfrak a_t(h;x)=\mathcal L_t(hx)-h\mathcal L_tx\in\mathcal I.
\tag{GSP8.3}
\]
Its target is \(\mathcal I\), since multiplication by \(h\) commutes with \(g_t\) in (GSP8.1). Using any representative \(F\) of \(x\), the full formula is
\[
\mathfrak a_t(h;x)(s)=\frac{F_0(s)}{2\pi i}
\int_{\partial V}g_t(\lambda)\frac{F(\lambda)}{F_0(\lambda)}
\frac{h(s)-h(\lambda)}{\lambda-s}\,d\lambda.
\tag{GSP8.4}
\]
Here \(\partial V\) denotes the right line upward and the left line downward, exactly as in (GSP3.2). The divided difference has its removable value at \(\lambda=s\). The equality follows by subtracting the two representative resolvents; all terms involving \(F(s)\) cancel and the displayed full \(F_0(s)\) remains. Convergence in \(\mathcal B\) follows from the two convergent vector integrals in (GSP8.3), or directly from the polynomial strip growth of \(h\) and the same division estimate. Independence of the representative follows from \(\mathscr L_t\mathcal I=0\) and \(h\mathcal I\subset\mathcal I\).

This defect obeys the exact cocycle identity
\[
\mathfrak a_t(hk;x)=\mathfrak a_t(h;kx)+h\mathfrak a_t(k;x),
\tag{GSP8.5}
\]
as is seen by adding and subtracting \(h\mathcal L_t(kx)\). Thus continuity of the lift does not silently imply its multiplier equivariance.

For the original generator \(h(s)=s\), (GSP8.4) becomes the particularly explicit rank-one representative defect
\[
\mathfrak a_t(s;x)=-F_0\lambda_t(x),\qquad
\lambda_t([F])=\frac1{2\pi i}\int_{\partial V}
e^{t\lambda^2}\frac{F(\lambda)}{F_0(\lambda)}d\lambda.
\tag{GSP8.6}
\]
The scalar integral is absolutely convergent by (GSP2.5). It annihilates \(\mathcal I\), using the same finite-contour and tail argument, so it is a continuous functional on the original quotient. Its complete grouped residue formula is
\[
\lambda_t([F])=\lim_{j\to\infty}
\sum_{|\Im\rho|<T_j}
\operatorname{Res}_{\lambda=\rho}
\frac{e^{t\lambda^2}F(\lambda)}{F_0(\lambda)}.
\tag{GSP8.7}
\]
The convergence is uniform on bounded source sets, from the fixed-\(t\) estimates. The residue at each multiple zero uses every Taylor coefficient of the full original product (GSP1.7). For every positive integer \(k\), the complete polynomial version is
\[
\mathfrak a_t(s^k;x)
=-F_0(s)\sum_{a=0}^{k-1}s^{k-1-a}\lambda_t(L^a x).
\tag{GSP8.8}
\]
It follows from \((s^k-\lambda^k)/(\lambda-s)=-\sum_{a=0}^{k-1}s^{k-1-a}\lambda^a\), with no omitted lower terms. Formula (GSP8.4) also applies to the genuine recovered-degree multipliers \(h(s)=n^s\) and the full trace multipliers \(h(s)=n^{1-s}\).

Finally retain how this relates to the actual specialization: composing (GSP8.1) with ADM's strict quotient \(\mathcal Q\to\mathcal R\) and with \(\beta_r\) gives exactly the reflected Gaussian action of (GSP7.2), without its finite cutoff. This is a concrete regularized lift into the original analytic source, together with its calculated equivariance defect. It supplies neither an extra Tate factor nor a weight-separation assertion for the original connecting map.

## GSP9. What the attempt establishes for the lifting calculation

The previously unproved primal density is now obtained in the original topology, with a single explicit family of finite-rank full-jet operators and its continuous transpose. It classifies closed multiplier submodules by their complete local jet orders. It also determines the previously retained reconstruction defect's Hausdorff quotient: zero, with the original algebraic quotient still present. The same contour constructs an actual continuous Gaussian lift through the original source extension, and (GSP8.4) calculates its full multiplier-equivariance defect. These are derived properties of the full original source, not assumed finite-block descriptions.

The next distinction in the geometric calculation is now precise. A continuous actual lifting arrow is determined by its restrictions to all full-jet blocks, by (GSP4.7). An arrow vanishing on every such block vanishes globally, including the strong-dual comparison with (GSP7.3). For the actual \(\beta_r\), however, (GSP7.2) retains its exact coefficient \(d_r(\rho)\); the approximation does not turn this coefficient into zero. The normal separator of ADM remains identity on that original specialization source and has the distinct translated action \(c(s+1)\) on the normal coefficient. Those source and target actions have not changed under spectral synthesis.

The Deligne comparison must therefore use an actual geometric operation on these complete blocks and their convergent reconstruction. The parallel tensor calculation is testing the genuine product/transfer operation while retaining the original specialization. Neither density nor the vanishing of a Hausdorff reconstruction quotient proves the vanishing of this original connecting map. The full original-zeta arithmetic and Weil contribution stay those of PSC5, with both endpoints and every trivial-zero term in its stated domain.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
