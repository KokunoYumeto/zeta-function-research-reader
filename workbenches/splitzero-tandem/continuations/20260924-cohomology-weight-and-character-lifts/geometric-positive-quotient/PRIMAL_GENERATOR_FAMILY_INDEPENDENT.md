# The full parameter and jet family of the original-zeta generator sequence

Independent derivation, 24 September 2026. Complete proof locators PGF0–PGF9.

## PGF0. Scope, prerequisites, and actual sources read

This calculation is on the arithmetic coefficient spaces after their complete global reconstruction. It does not construct arithmetic by selecting a few primes. The user's supporting notation \(Z_0,Z_1,Z_2,\ldots,\tau\) remains unchanged. Addition at \(\tau\) is retracted. None of the additions, derivatives, scalar operations, or coordinates below are operations on \(\tau\).

The governing `argument_reconstruction/CORPUS_AND_OPERATION_RULE.md` was read, including the recorded corrections concerning prerequisites and the full obstruction receiver. This derivation uses the already constructed exact row
\[
0\longrightarrow\mathcal I\xrightarrow{\iota}\mathcal B
\xrightarrow{q}\mathcal Q\longrightarrow0.
\tag{PGF0.1}
\]
It does not assert a new weight bound or an RH conclusion. The map calculated here is the parameter-dependent inclusion between the two generator cokernels and its actual snake boundary. It is not the sheaf connecting map \(Q\to J(-1)\), whose vanishing is already proved in CW4 and CW7.

Programme sources read for this derivation were:

- `GLOBAL_MELLIN_SYNTHESIS.md`, S1–S3, including the complete source multiplier and every exceptional value.
- `EXACT_SCHWARTZ_SUMMATION_IMAGE.md`, SSI0–SSI3, for the exact statement, source conventions, and original-zeta receiver. The completed SSI exact-image theorem is used as an established input, not reproved here.
- `../tau_weight_cohomology_20260924/CC_ACTUAL_WEIGHT_LIFT_COMPARISON.md`, CW0–CW9, for the actual source row, its full kernel, and the distinction between quotient characters and eigenvectors.
- `../tau_weight_cohomology_20260924/ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md`, RZ1–RZ8, for whole-space division estimates, holomorphic resolvents, and the already constructed generalized eigenspaces. The present proof does not claim those prior constructions as new.
- `CC_VERDIER_SUPPORT_INDEPENDENT.md`, VSD13, for the first-order closed-image statement and its separate algebraic-dual consequence. The present calculation concerns the primal sequence; it does not duplicate the dagger-dual lifting calculation.

The upstream source construction is Alain Connes and Caterina Consani, *Schemes over \(\mathbb F_1\) and zeta functions*, [arXiv:0903.2024v3](https://arxiv.org/abs/0903.2024v3), §5. SSI and CW record the original author-file identity, exact reading coverage, and receiving maps. This independent note makes no additional claim of having reread that complete author source. All new calculations used here are proved below.

## PGF1. Objects, operators, and the retained entire source function

Let \(\mathcal B\) be the complex Fréchet space of entire functions with
\[
b_{A,M}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^M|F(s)|<\infty
\quad(A,M\in\mathbb N).
\tag{PGF1.1}
\]
Let \(\mathscr Z\) be the actual nontrivial-zero set of the original Riemann zeta function, and let \(m_\rho\) be each full multiplicity. Put
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for all }\rho\in\mathscr Z,\ 0\le j<m_\rho\},
\qquad \mathcal Q=\mathcal B/\mathcal I.
\tag{PGF1.2}
\]
The ideal is closed because each indicated jet functional is continuous by Cauchy's formula. The quotient uses its actual Fréchet quotient topology.

Multiplication by \(s\), written \(L\) on each space where it is defined, is continuous and preserves \(\mathcal I\). For example,
\[
b_{A,M}(LF)\le(A+1)b_{A,M+1}(F).
\tag{PGF1.3}
\]
For every \(\lambda\in\mathbb C\) and positive integer \(r\), define
\[
M_{\lambda,r}=(L-\lambda)^r.
\tag{PGF1.4}
\]
This is an everywhere-defined continuous linear map on \(\mathcal B,\mathcal I,\mathcal Q\). The arithmetic coefficient field, polynomial, and integer \(r\) here are already reconstructed receivers.

Retain the entire source function with all its original factors:
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{PGF1.5}
\]
It belongs to \(\mathcal I\), and its divisor consists exactly of \((\rho,m_\rho)\). At the exceptional points its values are
\[
F_0(0)=F_0(1)=\frac18,
\tag{PGF1.6}
\]
\[
F_0(-2n)
=\frac{n(2n+1)(-1)^n\pi^n}{2\,n!}\zeta'(-2n)
=\frac{(1+2n)(2n)}8\pi^{-(1+2n)/2}
\Gamma((1+2n)/2)\zeta(1+2n)\ne0
\quad(n\ge1).
\tag{PGF1.7}
\]
These are the retained S2 and CW1 identities. In particular the original zeta pole at \(1\) and the trivial zeros at \(-2n\) are not additional zeros of this specified source function.

Set
\[
m_\lambda=\operatorname{ord}_\lambda F_0,
\tag{PGF1.8}
\]
with order zero where \(F_0(\lambda)\ne0\). Every \(F\in\mathcal I\) has an entire quotient \(F/F_0\), by local Taylor division at each zero. This quotient is not asserted to belong to \(\mathcal B\).

For later continuity, the division map
\[
\mathcal D:\mathcal I\longrightarrow\mathcal O(\mathbb C),
\qquad F\longmapsto F/F_0
\tag{PGF1.9}
\]
is continuous for the compact-open topology on the target. To prove it, put any given compact set inside a circle \(|s|=R\) which contains no zero of \(F_0\) on its boundary. Such an \(R\) exists because the zeros are discrete. The maximum principle applied to the entire quotient gives
\[
\sup_{|s|\le R}|F(s)/F_0(s)|
\le\frac{b_{A,0}(F)}{\min_{|s|=R}|F_0(s)|},\qquad A\ge R.
\tag{PGF1.10}
\]
The denominator is positive. Cauchy's formula on a slightly larger circle gives the same conclusion for every fixed derivative and every compact set.

## PGF2. Both complete jet quotients, with their exact topology

For a fixed \(r\ge1\), write
\[
R_r=\mathbb C[h]/(h^r),\qquad
j^r_\lambda H=\sum_{j=0}^{r-1}\frac{H^{(j)}(\lambda)}{j!}h^j
\quad\text{for an entire }H.
\tag{PGF2.1}
\]
Here \(h\) is the jet coordinate \(s-\lambda\) in an arithmetic coefficient receiver; it is not a coordinate of \(\tau\). Define
\[
\beta_{\lambda,r}:\mathcal B\to R_r,
\quad F\mapsto j^r_\lambda F,
\qquad
\alpha_{\lambda,r}:\mathcal I\to R_r,
\quad F\mapsto j^r_\lambda(F/F_0).
\tag{PGF2.2}
\]
Both are continuous. This follows for \(\beta\) from Cauchy estimates and for \(\alpha\) from (PGF1.9)–(PGF1.10).

They are both onto, with explicit continuous linear sections. If \(P\) is the unique polynomial of degree below \(r\) representing its class in \(R_r\), put
\[
\sigma^I_{\lambda,r}(P)(s)=F_0(s)P(s-\lambda).
\tag{PGF2.3}
\]
The product belongs to \(\mathcal I\), since polynomial multiplication preserves \(\mathcal B\) and all required zero orders. Its quotient by \(F_0\) is exactly \(P(s-\lambda)\), so \(\alpha\sigma^I=1\).

For the other section, retain the Gaussian and every truncated coefficient:
\[
\sigma^B_{\lambda,r}(P)(s)
=e^{(s-\lambda)^2}
\left.\operatorname{Tay}_{h,<r}\bigl(e^{-h^2}P(h)\bigr)
\right|_{h=s-\lambda}.
\tag{PGF2.4}
\]
The Gaussian times this finite polynomial belongs to \(\mathcal B\): on every bounded real strip the factor has modulus
\(e^{(\Re s-\Re\lambda)^2-(\Im s-\Im\lambda)^2}\), which dominates every polynomial decay requirement. Its Taylor polynomial at \(s=\lambda\) equals \(P\) modulo \(h^r\), so \(\beta\sigma^B=1\). These are sections of the specified quotient maps, not a section of \(\mathcal B\to\mathcal Q\).

The kernels are exactly
\[
\ker\beta_{\lambda,r}=(s-\lambda)^r\mathcal B,
\qquad
\ker\alpha_{\lambda,r}=(s-\lambda)^r\mathcal I.
\tag{PGF2.5}
\]
For the first identity, vanishing of the jet is precisely divisibility to order \(r\) at \(\lambda\). The quotient is entire and remains in \(\mathcal B\). An explicit division estimate is given below. For the second, \(\alpha(F)=0\) means that \(F/F_0\) has a zero of order at least \(r\). Thus \(F/(s-\lambda)^r\) retains the full zero order \(m_\lambda\) at \(\lambda\), as well as the full orders at all other original zeros, and belongs to \(\mathcal I\). The converse implications follow by direct multiplication.

For precision, if \(H\in\mathcal B\) vanishes to order at least \(r\) at \(\lambda\), its entire quotient obeys
\[
b_{A,M}\!\left(\frac{H}{(s-\lambda)^r}\right)
\le b_{A,M}(H)
+2^{-r}(2+|\Im\lambda|)^M b_{A',0}(H),
\quad A'\ge\max(A,|\Re\lambda|+2).
\tag{PGF2.6}
\]
Outside the radius-one disk, the denominator has modulus at least one. Inside that disk, apply the maximum principle to the quotient on the radius-two disk; its boundary value is bounded by \(2^{-r}\sup|H|\). The polynomial imaginary-coordinate weight is bounded by \((2+|\Im\lambda|)^M\) on the smaller disk. This proves the estimate, which is uniform for \(\lambda\) in a compact set after fixing \(A'\) and the displayed maximum of \(|\Im\lambda|\).

Consequently the maps
\[
\overline\alpha_{\lambda,r}:
\mathcal I/(L-\lambda)^r\mathcal I\xrightarrow{\sim}R_r,
\qquad
\overline\beta_{\lambda,r}:
\mathcal B/(L-\lambda)^r\mathcal B\xrightarrow{\sim}R_r
\tag{PGF2.7}
\]
are topological linear isomorphisms. Their continuous inverses are the quotient classes of (PGF2.3) and (PGF2.4). On both sides \(L\) acts as multiplication by \(\lambda+h\), so these are also exact \(\mathbb C[L]\)-module isomorphisms.

Their multiplicative meanings differ and must be retained. The map \(\overline\beta\) is an algebra isomorphism to the usual truncated polynomial algebra; its identity is the class represented by (PGF2.4) with \(P=1\). On the \(\mathcal I\)-quotient, (PGF2.7) transports the inherited product to
\[
P\star Q=f_{\lambda,r}(h)P(h)Q(h)\pmod{h^r},
\qquad
f_{\lambda,r}(h):=j^r_\lambda F_0.
\tag{PGF2.8}
\]
Indeed \((FG)/F_0=F_0(F/F_0)(G/F_0)\). Thus \(\overline\alpha\) is a linear and module isomorphism; it is not an identification with the usual multiplication on \(R_r\). This retains the full source coefficient rather than silently replacing its product.

## PGF3. The inclusion matrix and every retained factor

The inclusion \(\iota:\mathcal I\to\mathcal B\) induces, in (PGF2.7), exactly
\[
\mathsf T_r(\lambda):R_r\longrightarrow R_r,
\qquad P\longmapsto f_{\lambda,r}P\pmod{h^r}.
\tag{PGF3.1}
\]
Proof: \(F=F_0(F/F_0)\) as an identity of entire functions, so taking its full \(r\)-jet gives (PGF3.1). No local unit is removed in this map.

In the ordered basis \(1,h,\ldots,h^{r-1}\), write
\[
c_j(\lambda)=\frac{F_0^{(j)}(\lambda)}{j!}.
\tag{PGF3.2}
\]
Then the complete matrix is
\[
\mathsf T_r(\lambda)_{ij}=
\begin{cases}
c_{i-j}(\lambda),&0\le j\le i<r,\\
0,&0\le i<j<r.
\end{cases}
\tag{PGF3.3}
\]
It follows by the triangular determinant formula that
\[
\det\mathsf T_r(\lambda)=F_0(\lambda)^r
=\left[\frac{\lambda(\lambda-1)}8\pi^{-\lambda/2}
\Gamma(\lambda/2)\zeta(\lambda)\right]^r,
\tag{PGF3.4}
\]
where the expression on the right has its full entire continuation and the values (PGF1.6)–(PGF1.7). The exponent \(r\) is the matrix rank of this \(r\)-jet comparison. It is not a pooling of two arithmetic branches or a replacement of the original return measure by a power of zeta.

At a point where the individual factors are holomorphic, all coefficients in the matrix retain the full Leibniz sum. With \(P(s)=s(s-1)\), this is
\[
c_j(\lambda)=\frac{\pi^{-\lambda/2}}8
\sum_{\substack{a+b+c+d=j\\0\le a\le2}}
\frac{P^{(a)}(\lambda)}{a!}
\frac{(-\log\pi/2)^b}{b!}
\frac{2^{-c}\Gamma^{(c)}(\lambda/2)}{c!}
\frac{\zeta^{(d)}(\lambda)}{d!}.
\tag{PGF3.5}
\]
At \(0,1,-2,-4,\ldots\), the definition (PGF3.2) takes the derivatives of the full analytic product. Equivalently, its coefficient is the coefficient of \(h^j\) in the product of the full convergent Laurent expansions of
\[
\frac{(\lambda+h)(\lambda+h-1)}8,
\quad \pi^{-(\lambda+h)/2},
\quad\Gamma((\lambda+h)/2),
\quad\zeta(\lambda+h).
\tag{PGF3.6}
\]
Each has only the stated finite principal part at that point, so the coefficient of each fixed nonnegative power is a finite sum over the allowed Laurent exponents. This prescription keeps the cancellation derivatives, including the zeta residue and the trivial-zero derivatives. In particular, the diagonal is \(1/8\) at both endpoints, and equals (PGF1.7) at each negative even integer; the determinant there is the corresponding nonzero \(r\)-th power. The original zeta's pole and trivial zeros remain in (PGF3.6), rather than being asserted absent from the original function.

## PGF4. The full snake sequence and its actual boundary

Apply \(M_{\lambda,r}\) to all three terms of (PGF0.1). The first two vertical maps are injective, since an entire function multiplied by the nonzero polynomial \((s-\lambda)^r\) can vanish identically only when that entire function is zero. The full resulting snake sequence is
\[
0\longrightarrow K_{\lambda,r}
\xrightarrow{\partial_{\lambda,r}} R_r
\xrightarrow{\mathsf T_r(\lambda)}R_r
\xrightarrow{\pi_{\lambda,r}}C_{\lambda,r}
\longrightarrow0,
\tag{PGF4.1}
\]
where
\[
K_{\lambda,r}=\ker\bigl((L-\lambda)^r:\mathcal Q\to\mathcal Q\bigr),
\qquad
C_{\lambda,r}=\mathcal Q/(L-\lambda)^r\mathcal Q.
\tag{PGF4.2}
\]
Here is the explicit boundary, with its sign fixed:
\[
\boxed{\quad
\partial_{\lambda,r}[H]
=j^r_\lambda\!\left(\frac{(s-\lambda)^rH(s)}{F_0(s)}\right).
\quad}
\tag{PGF4.3}
\]
The hypothesis defining the kernel means that the numerator is in \(\mathcal I\), so its quotient is entire. If the representative \(H\) is changed by \(G\in\mathcal I\), the displayed quotient changes by \((s-\lambda)^rG/F_0\), whose first \(r\) Taylor coefficients vanish. Thus the boundary is well defined. Its positive sign is the diagram chase: lift \([H]\) to \(H\in\mathcal B\), apply \((s-\lambda)^r\), and take the resulting element of \(\mathcal I\), without a reversal of the subtraction order.

The last map sends a polynomial class \(P\in R_r\) to the class of any lift of \(P\) under \(\beta_{\lambda,r}\), followed by \(q\) and then the quotient in (PGF4.2). Different lifts differ by \((s-\lambda)^r\mathcal B\), whose image vanishes there. It is onto because every \(\mathcal Q\)-class has a representative in \(\mathcal B\).

For a direct proof of every exactness claim, first suppose \(\partial[H]=0\). Then \((s-\lambda)^rH=(s-\lambda)^rG\) for some \(G\in\mathcal I\), by (PGF2.5). Injectivity of polynomial multiplication on \(\mathcal B\) gives \(H=G\), so \([H]=0\). Next, if \(\partial[H]=P\), the jet of \((s-\lambda)^rH\) is zero, so \(\mathsf T_r P=0\). Conversely, if \(\mathsf T_r P=0\), take its unique polynomial representative of degree below \(r\). The function
\[
H_P(s)=\frac{F_0(s)P(s-\lambda)}{(s-\lambda)^r}
\tag{PGF4.4}
\]
is entire by the vanishing condition \(\mathsf T_rP=0\), belongs to \(\mathcal B\) by (PGF2.6), satisfies \((s-\lambda)^rH_P\in\mathcal I\), and has boundary exactly \(P\). Finally a jet maps to zero in \(C_{\lambda,r}\) exactly when a representative is the sum of an element of \(\mathcal I\) and an element of \((s-\lambda)^r\mathcal B\); its jet is therefore precisely in the image of \(\mathsf T_r\). This proves (PGF4.1) without replacing the full quotient by a product of jets.

Put \(m=m_\lambda\) and \(d=\min(r,m)\). At the fixed parameter, write
\[
F_0(\lambda+h)=h^m u_\lambda(h),\qquad
u_\lambda(0)=F_0^{(m)}(\lambda)/m!\ne0.
\tag{PGF4.5}
\]
This is a local factorization with the unit retained. Multiplication by its full truncated jet is an invertible map of \(R_r\), with inverse the truncated Taylor series of \(1/u_\lambda\). It follows that
\[
\ker\mathsf T_r(\lambda)=h^{r-d}R_r,
\qquad
\operatorname{im}\mathsf T_r(\lambda)=h^dR_r,
\tag{PGF4.6}
\]
where \(h^rR_r=0\). Consequently
\[
\dim K_{\lambda,r}=\dim C_{\lambda,r}=d.
\tag{PGF4.7}
\]
The actual kernel basis and its boundary are
\[
q_{\lambda,k}=\left[\frac{F_0(s)}{(s-\lambda)^k}\right],
\qquad
\partial_{\lambda,r}q_{\lambda,k}=h^{r-k},
\qquad 1\le k\le d.
\tag{PGF4.8}
\]
Each representative is entire because \(k\le m\), and its membership in \(\mathcal B\) follows from (PGF2.6). The distinct monomials prove independence. They span because those monomials span the kernel in (PGF4.6) and (PGF4.3) is an isomorphism onto that kernel. This gives the previously known generalized eigenspaces a full source-boundary comparison, including every \(r\), rather than asserting a new spectral location theorem.

The cokernel has an equally explicit map:
\[
C_{\lambda,r}\xrightarrow{\sim} R_d,
\qquad [[H]]\longmapsto j^d_\lambda H,
\tag{PGF4.9}
\]
where \(R_0=0\). It is well defined since \(d\le m\) and \(d\le r\). Its kernel can be checked constructively. If \(m\ge r\), a representative whose \(r\)-jet vanishes is directly divisible by \((s-\lambda)^r\) in \(\mathcal B\). If \(m<r\) and \(H\) vanishes to order at least \(m\), its local quotient \(H/F_0\) is holomorphic at \(\lambda\). Let
\[
P(h)=\operatorname{Tay}_{h,<r-m}\bigl(H(\lambda+h)/F_0(\lambda+h)\bigr).
\tag{PGF4.10}
\]
Then \(H(s)-F_0(s)P(s-\lambda)\) vanishes to order at least \(r\), belongs to \(\mathcal B\), and is divisible there by \((s-\lambda)^r\). Since the subtracted term belongs to \(\mathcal I\), the quotient class of \(H\) lies in \((L-\lambda)^r\mathcal Q\). The same argument with \(m=0\) shows that this map is onto all of \(\mathcal Q\) when \(\lambda\notin\mathscr Z\).

The map \(\mathcal Q\to R_d\) in (PGF4.9) is continuous, since it descends from continuous jets on \(\mathcal B\). Its kernel is thus closed; this proves closedness of \((L-\lambda)^r\mathcal Q\). All finite-dimensional identifications in (PGF4.1), (PGF4.8), and (PGF4.9) are topological. No density of the sum of the primal generalized eigenspaces is used or concluded.

## PGF5. The boundary in the original Schwartz and Mellin sources

The exact source spaces and map from SSI and CW are
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\ f(0)=0,
\ \int_{\mathbb R}f(v)\,dv=0\},
\]
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for all }N,j\},
\]
\[
\Sigma f(u)=2\sum_{n\ge1}f(nu),\qquad J=\Sigma S,
\qquad Q=A/J,
\tag{PGF5.1}
\]
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},
\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}F(1/2+it)u^{-it}\,dt.
\tag{PGF5.2}
\]
The established exact-image theorem says that \(\Sigma:S\to J\) and \(\Theta:A\to\mathcal B\) are topological isomorphisms onto their stated targets, with \(\Theta J=\mathcal I\). The quotient map \(\kappa:Q\to\mathcal Q\) is \([a]\mapsto[\Theta a]\). Every factor \(2,1/2,1/\pi\) in these maps remains explicit.

Define the actual source generators
\[
D_Sf(v)=-v f'(v),\qquad D_Aa(u)=-u a'(u).
\tag{PGF5.3}
\]
They preserve their indicated spaces continuously. Evenness and Schwartz estimates show this for \(S\); its value condition is preserved by the factor \(v\), and integration by parts gives \(\int D_Sf=\int f=0\). The weighted logarithmic-derivative seminorms prove the statement on \(A\). Termwise differentiation of the convergent Schwartz sum, with the same endpoint estimates as SSI2, and integration by parts in the Mellin integral give
\[
\Sigma D_S=D_A\Sigma,
\qquad \Theta D_A=L\Theta.
\tag{PGF5.4}
\]
All boundary terms vanish by the stated seminorms. These identities transport (PGF4.1) to the actual row \(0\to S\xrightarrow\Sigma A\to Q\to0\).

For the original Gaussian source
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},
\qquad \Theta\Sigma f_0=F_0,
\tag{PGF5.5}
\]
the kernel class in (PGF4.8) has the exact \(A\)-representative
\[
a_{\lambda,k}(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}
\frac{F_0(1/2+it)}{(1/2+it-\lambda)^k}u^{-it}\,dt,
\qquad 1\le k\le\min(r,m_\lambda).
\tag{PGF5.6}
\]
The integrand uses its removable entire value if \(1/2+it=\lambda\); no singular integral prescription is imposed. The numerator divided by that power belongs to \(\mathcal B\), so the established Mellin inverse estimates prove \(a_{\lambda,k}\in A\).

Using (PGF5.4) gives the equality in the actual prequotient source:
\[
(D_A-\lambda)^r a_{\lambda,k}
=\Sigma\bigl((D_S-\lambda)^{r-k}f_0\bigr).
\tag{PGF5.7}
\]
Indeed the Mellin transforms of the two sides both equal
\((s-\lambda)^{r-k}F_0(s)\), and \(\Theta\) is injective. Thus the original-source snake boundary is
\[
[a_{\lambda,k}]
\longmapsto
\bigl[(D_S-\lambda)^{r-k}f_0\bigr]
\quad\text{in }S/(D_S-\lambda)^rS.
\tag{PGF5.8}
\]
This proves the full map between the kernel class and its genuine Schwartz-source boundary. The representation does not assign a scalar or arithmetic operation to the support.

## PGF6. Holomorphic parameter dependence and the exact family cokernel

All entries of (PGF3.3) are entire in \(\lambda\). The quotient coordinates themselves form compatible holomorphic families; this can be proved directly, without assuming a holomorphic section of \(\mathcal B\to\mathcal Q\).

First \(\lambda\mapsto(L-\lambda)^r\) is a polynomial family of continuous operators on \(\mathcal B\) and \(\mathcal I\), by expansion into the finitely many continuous powers of \(L\). The section \(\sigma^I_{\lambda,r}\) is polynomial in \(\lambda\) with values in \(\mathcal I\). The Gaussian section \(\sigma^B_{\lambda,r}\) is entire with values in \(\mathcal B\): for \(\lambda\) in any compact set, each strip seminorm of the function and each parameter derivative is bounded by a constant times a Gaussian in \(\Im s\) times a fixed polynomial. Pointwise parameter Cauchy formulas can therefore be integrated in each seminorm; the corresponding Cauchy remainder estimates prove convergence of difference quotients in the Fréchet topology. Since the input space \(R_r\) is finite dimensional, this proves the assertion for the section as an operator family.

The jet maps \(\alpha_{\lambda,r}\) and \(\beta_{\lambda,r}\) are likewise holomorphic in \(\lambda\), uniformly on bounded input sets. For \(\beta\), apply Cauchy's formula to derivatives of \(F\) on a fixed larger compact set. For \(\alpha\), apply the same argument to the continuous map (PGF1.9). The estimate (PGF1.10) bounds the result by one input seminorm for every compact parameter set and derivative order. It also proves holomorphy on a parameter-dependent holomorphic \(\mathcal I\)-valued family by joint evaluation and the parameter Cauchy formula.

For completeness, these give exact sheaf rows of holomorphic families. Write \(\mathcal O_U(E)\) for holomorphic functions from an open parameter set \(U\subset\mathbb C\) into the indicated Fréchet space \(E\). For \(E=\mathcal B\) use \(\beta\), and for \(E=\mathcal I\) use \(\alpha\). Then
\[
0\longrightarrow\mathcal O_U(E)
\xrightarrow{\ (s-\lambda)^r\ }\mathcal O_U(E)
\xrightarrow{\ j_E\ }\mathcal O_U^{\,r}
\longrightarrow0
\tag{PGF6.1}
\]
is exact, with the sections just constructed. To check the sole analytic divisibility issue, take a holomorphic family \(H_\lambda\) in the kernel. Pointwise division \(H_\lambda(s)/(s-\lambda)^r\) is entire in \(s\). In local coordinates \((\lambda,h=s-\lambda)\), the first \(r\) coefficients of \(H_\lambda(\lambda+h)\) vanish identically, so Taylor division shows joint holomorphy of the quotient, including the diagonal. Estimate (PGF2.6), uniformly on compact parameter sets, bounds each output seminorm by input seminorms. Cauchy's parameter formula and remainder estimates therefore prove Fréchet holomorphy. For \(E=\mathcal I\), (PGF2.5) additionally proves that every divided value lies in \(\mathcal I\); since it is closed, the holomorphic family lies in that space. This proves exactness of both rows with their actual topologies.

The inclusion between the rows of (PGF6.1) induces the entire matrix map (PGF3.3). Define its coherent cokernel sheaf on the parameter plane by
\[
\mathscr C_r=
\operatorname{coker}\bigl(\mathcal O_{\mathbb C}^{\,r}
\xrightarrow{\mathsf T_r}\mathcal O_{\mathbb C}^{\,r}\bigr).
\tag{PGF6.2}
\]
The displayed map of sheaves is injective, although some of its fixed-parameter matrices have nonzero kernels. To prove injectivity, multiply a germ in its kernel by the adjugate matrix. Each component is then killed by the nonzero holomorphic germ \(F_0(\lambda)^r\). The local holomorphic ring is an integral domain, so each component is zero. Hence
\[
0\to\mathcal O_{\mathbb C}^{\,r}
\xrightarrow{\mathsf T_r}\mathcal O_{\mathbb C}^{\,r}
\to\mathscr C_r\to0
\tag{PGF6.3}
\]
is a free resolution of the exact family cokernel. No exactness assertion for the unconstructed sheaf of holomorphic \(\mathcal Q\)-valued lifts is needed for this statement.

Fix an actual zero \(\rho\), put \(x=\lambda-\rho\) and \(m=m_\rho\), and write
\[
F_0(\rho+y)=y^m u_\rho(y),\qquad u_\rho(0)\ne0.
\tag{PGF6.4}
\]
In the local free \(\mathbb C\{x\}\)-module \(\mathbb C\{x\}[h]/(h^r)\), the original map is multiplication by
\[
(x+h)^m u_\rho(x+h)\pmod{h^r}.
\tag{PGF6.5}
\]
Its unit comparison is the explicit domain automorphism given by multiplication by the full jet of \(u_\rho(x+h)\); its inverse uses the full jet of \(1/u_\rho(x+h)\). Multiplication by \((x+h)^m\) composed with that domain automorphism is exactly the original map (PGF6.5). Thus the original unit has a stated map and inverse throughout the comparison.

The resulting cokernel is consequently
\[
(\mathscr C_r)_\rho
\cong \mathbb C\{x,h\}/\bigl(h^r,(x+h)^m\bigr)
\cong \mathbb C\{y,h\}/(h^r,y^m),\qquad y=x+h.
\tag{PGF6.6}
\]
The two maps in the second isomorphism are exactly \(y\mapsto x+h\) and \(x\mapsto y-h\), with \(h\) fixed. Every convergent power series reduces uniquely to
\(\sum_{0\le i<m,\ 0\le j<r}a_{ij}y^ih^j\), so the length of this local parameter module is
\[
\operatorname{length}_{\mathbb C\{x\}}(\mathscr C_r)_\rho=mr.
\tag{PGF6.7}
\]
It is supported at \(x=0\): the action of \(x\) is \(y-h\), and \((y-h)^{m+r-1}=0\). Its power \((y-h)^{m+r-2}\) is nonzero, because its only surviving monomial is
\[
\binom{m+r-2}{m-1}(-1)^{r-1}y^{m-1}h^{r-1},
\tag{PGF6.8}
\]
with nonzero coefficient in the already recovered complex coefficient field. The length in (PGF6.7) includes these parameter-direction extensions; it must not be replaced by the dimension of a fixed fibre.

Indeed the fibre at \(\rho\) is
\[
\mathscr C_r\otimes_{\mathcal O}\mathbb C_\rho
\cong\mathbb C[h]/(h^r,h^m)\cong R_{\min(r,m)}.
\tag{PGF6.9}
\]
Applying the fibre functor to the proved free resolution (PGF6.3) also gives
\[
0\to\operatorname{Tor}^{\mathcal O}_1(\mathscr C_r,\mathbb C_\lambda)
\to R_r\xrightarrow{\mathsf T_r(\lambda)}R_r
\to\mathscr C_r\otimes\mathbb C_\lambda\to0.
\tag{PGF6.10}
\]
This is the same finite sequence as (PGF4.1), with the explicit isomorphism from the actual primal kernel supplied by its boundary (PGF4.3). Therefore
\[
K_{\lambda,r}\xrightarrow[\partial_{\lambda,r}]{\sim}
\operatorname{Tor}^{\mathcal O}_1(\mathscr C_r,\mathbb C_\lambda),
\qquad
C_{\lambda,r}\xrightarrow{\sim}\mathscr C_r\otimes\mathbb C_\lambda.
\tag{PGF6.11}
\]
The first arrow names the kernel inclusion in (PGF6.10) and uses its fixed positive sign. These are exact maps explaining why a sheaf injection can have a noninjective specialization; the missing fibre kernel is retained as the displayed Tor group.

## PGF7. Arithmetic actions and the full coefficient reflection

For every recovered positive real \(a\), the coefficient action is
\[
T_aF(s)=a^sF(s).
\tag{PGF7.1}
\]
On each of the two jet quotients in (PGF2.7), it acts as
\[
a^\lambda\sum_{j=0}^{r-1}\frac{(\log a)^j}{j!}M_h^j.
\tag{PGF7.2}
\]
This follows by taking the full jet of \(a^{\lambda+h}\); in the \(\mathcal I\)-quotient the division by \(F_0\) leaves exactly the same multiplier. The matrix \(\mathsf T_r\) commutes with that action because both are multiplication operators in \(R_r\). The boundary is equivariant by (PGF4.3), since \(T_a\) commutes with \((L-\lambda)^r\). On its explicit kernel basis the whole action is
\[
T_aq_{\lambda,k}
=a^\lambda\sum_{j=0}^{k-1}\frac{(\log a)^j}{j!}
q_{\lambda,k-j}.
\tag{PGF7.3}
\]
To verify the equality on the full quotient, subtract its right side from its left. The numerator of the difference is \(F_0\) times the remainder after subtracting the first \(k\) Taylor coefficients of \(a^s\) at \(\lambda\). That remainder is divisible by \((s-\lambda)^k\); after division the result belongs to \(\mathcal I\), with the strip estimates following from boundedness of \(a^s\) on each fixed strip and (PGF2.6). Thus every nilpotent coefficient is retained, not only the leading character.

If the same coefficient representation is given the actual normal-degree twist, its action is \(aT_a\); equations (PGF7.2)–(PGF7.3) acquire exactly the factor \(a\), equivalently \(a^{\lambda+1}\) instead of \(a^\lambda\). This is a receiving comparison; it does not identify \(\mathcal I(-1)\) with \(\mathcal Q(-1)\).

The coefficient reflection is
\[
\mathcal RF(s)=F(1-s),\qquad F_0(1-s)=F_0(s).
\tag{PGF7.4}
\]
The identity for \(F_0\) is the original source Fourier/Mellin identity retained in S2. Define \(\mathsf C_rP(h)=P(-h)\). Then
\[
\beta_{1-\lambda,r}(\mathcal RF)=\mathsf C_r\beta_{\lambda,r}(F),
\qquad
\alpha_{1-\lambda,r}(\mathcal RF)=\mathsf C_r\alpha_{\lambda,r}(F),
\tag{PGF7.5}
\]
and
\[
\mathsf T_r(1-\lambda)\mathsf C_r
=\mathsf C_r\mathsf T_r(\lambda).
\tag{PGF7.6}
\]
Each equality follows by substituting \(s=1-\lambda+h\), so that \(1-s=\lambda-h\), retaining every power of \(-1\).

There is also a required sign in the snake boundary:
\[
\boxed{
\partial_{1-\lambda,r}(\mathcal R x)
=(-1)^r\mathsf C_r\partial_{\lambda,r}(x).
}
\tag{PGF7.7}
\]
Indeed \((L-(1-\lambda))^r\mathcal R=(-1)^r\mathcal R(L-\lambda)^r\), as multiplication of entire functions verifies. Substituting this identity into (PGF4.3) proves (PGF7.7). On the basis it reads
\[
\mathcal Rq_{\lambda,k}=(-1)^kq_{1-\lambda,k},
\tag{PGF7.8}
\]
and the two signs in (PGF7.7) give the same \((-1)^k\). These are coefficient-reflection statements. Any additional sphere-orientation or cohomological-degree sign belongs to its separately specified geometric map and has not been silently added or removed here.

## PGF8. Exact information supplied to the lifting calculation

The parameter-dependent inclusion of the full primal coefficient ideals is now an explicit holomorphic matrix family, not merely a list of quotient characters. For every complex parameter and every jet order, its full entries are (PGF3.3), its actual source boundary is (PGF5.8), and its specialization kernel and cokernel are (PGF4.8)–(PGF4.9). The coherent family retains the longer parameter extension (PGF6.6), whose length is \(r m_\rho\), together with both the Tor kernel and ordinary fibre of dimension \(\min(r,m_\rho)\).

Off the actual nontrivial-zero divisor, the inclusion between the two jet quotients is an isomorphism with inverse multiplication by the complete truncated Taylor series of \(1/F_0\). At an actual zero, it is the full nilpotent multiplication by \(h^{m_\lambda}u_\lambda(h)\), with the unit and every derivative retained in the matrix. At \(0,1,-2,-4,\ldots\), the nonzero exceptional values (PGF1.6)–(PGF1.7) remain in this map. This describes precisely the divisor detected by this source construction; the original zeta's endpoint pole and trivial zeros still require their full comparison factors, already displayed in (PGF1.5) and (PGF3.6).

The family does not place every actual zero on a vertical line and does not turn a quotient character into an eigenvector of \(\mathcal I\). The calculation also does not claim the requested Deligne weight separation for the whole obstruction target \(J(-1)\). It supplies exact primal maps which any such calculation must use, while keeping the already established zero boundary of the actual sheaf lift distinct from the generally nonzero boundary (PGF4.3).

## PGF9. Independent internal checks of the formulas

These checks are symbolic identities for arbitrary \(r,\lambda,m_\lambda\), not bounded numerical tests.

1. Both maps in (PGF2.7) are proved with explicit continuous sections and an exact kernel calculation; there is no appeal to an unspecified quotient topology.
2. The matrix (PGF3.3) is the full product jet \(j^rF_0\,j^r(F/F_0)\). Its determinant, local unit, and all exceptional-point contributions are retained; the transported product on \(\mathcal I\) is separately recorded in (PGF2.8).
3. For every boundary basis vector, multiplication by \((s-\lambda)^r\) gives exactly \(F_0(s)(s-\lambda)^{r-k}\). Division by \(F_0\) therefore gives \(h^{r-k}\), fixing the boundary sign and verifying its actual Schwartz representative.
4. At \(m_\lambda=0\), the matrix is invertible and both primal kernel and cokernel vanish. At \(0<m_\lambda<r\), they each have dimension \(m_\lambda\). At \(m_\lambda\ge r\), the matrix specialization is zero and both have dimension \(r\). These exhaust all cases without assuming zero simplicity.
5. The sheaf map is injective because its determinant is a nonzero holomorphic germ, while its fibre kernel is exactly the Tor group in (PGF6.10). Thus no interchange of a sheaf kernel and its fibre has occurred.
6. The local parameter length \(r m_\rho\), fibre dimension \(\min(r,m_\rho)\), and nilpotence exponent \(m_\rho+r-1\) follow from the same explicit module (PGF6.6); they have not been identified with one another.
7. Reflection changes the parameter by \(\lambda\mapsto1-\lambda\), the jet coordinate by \(h\mapsto-h\), and the boundary by the additional factor \((-1)^r\). This is checked independently on every kernel basis vector in (PGF7.8).

No new purity statement, positivity statement, or conclusion about RH is asserted by these identities.
