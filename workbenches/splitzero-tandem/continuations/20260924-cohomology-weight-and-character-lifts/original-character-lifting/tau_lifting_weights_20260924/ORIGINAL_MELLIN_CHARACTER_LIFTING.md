# Exact Mellin-character lifting through the original summation transpose

24 September 2026. Independent derivation MCL0–MCL11. This computes every finite Mellin-jet lift at every actual nontrivial zero of the original zeta function, proves its least generalized-character order in the full original continuous dual, and places its exact connecting class in the original supported localization row.

## MCL0. Source, prerequisites and prior work used

The controlling source is the user's \(Z_0\) absence, primitive \(Z_1/\tau\) without parity or source addition, and the supplied integer layer with its full amounts and \(Z_2\) data. B1–B5, P1–P5 and retraction R1 were read in [SOURCE_OPERATIONS_AND_PROOFS.md](../foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md). The current CORPUS_AND_OPERATION_RULES.md (private construction record; not included) and complete relevant passages USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, USR-6152e3bc6302258c, USR-4322be19bff532cd and USR-64a88219a3ecddd3 were consulted in their retained verbatim corpus. Their full arithmetic-reconstruction and global-quotient arguments precede this receiving calculation. Neither a Mellin parameter nor an integer coefficient is constructed from primitive \(\tau\).

A bounded search of the retained proof corpus located the existing summation/Mellin identity, closed-image theorem, continuous-dual exact row and finite spectral lifts. The calculation below uses these proved maps; its new content is the least order for lifting through the actual \(\Sigma'\), its full prime defect, Fourier return, and the resulting character connecting map. It is not a repetition of the earlier lift from \(Q'\) into \(Q\) under the residue pairing: its source and target are the actual \(A'\to S'\).

The human source of the coefficients, Fourier identity and two-chart restrictions is Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). Their original author TeX and full relevant reading coverage were retained in [DCP0–DCP3](SOURCE_CC_DOUBLE_PULLBACK.md); DCP3 and DCP10 were read for this calculation. The closed-image analytic context is Ralf Meyer, [*A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3). The exact original-space image and inverse used here are proved in [OMS1–OMS5](ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md) and its retained SSI derivation. The dual topology and supported maps were read in [ASD1–ASD5](ACTUAL_SUPPORTED_DUALITY_INDEPENDENT.md) and [UOS1–UOS8](GLOBAL_UNIT_ORBIT_AND_SUPPORTED_COMPARISON.md).

Pierre Deligne's [*La conjecture de Weil. II*, §§3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/) supplies the requested supported lifting mechanism. Its geometric duality and weight estimates are not premises here. MCL9 constructs an actual connecting map for the specified original coefficient sequence; MCL10 locates it in the source-supported receiver. All needed sums, derivatives, distribution equations and quotients are constructed below in those receiving spaces.

## MCL1. Original spaces and the full holomorphic Mellin families

Retain
\[
 S=\{h\in\mathcal S(\mathbb R;\mathbb C):
 h(-v)=h(v),\ h(0)=0,\ \int_{\mathbb R}h(v)\,dv=0\}
\]
with its closed-subspace Schwartz topology, and
\[
 A=\{b\in C^\infty(0,\infty):
 p_{N,j}(b)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jb(u)|<\infty
 \text{ for all }N,j\ge0\}.
 \tag{MCL1.1}
\]
For \(z\in\mathbb C\), define the continuous linear functional
\[
 M_{A,z}(b)=\int_0^\infty b(u)u^z\,\frac{du}{u}.
 \tag{MCL1.2}
\]
For \(\Re z>-2\), define
\[
 M_{S,z}(h)=\int_0^\infty h(v)v^z\,\frac{dv}{v}.
 \tag{MCL1.3}
\]
These are full original positive-axis Mellin integrals. Their domains differ and are retained.

For \(z\) in a compact set \(K\subset\mathbb C\), choose an integer \(N>1+\sup_{z\in K}|\Re z|\). On \(u\le1\), \(|b(u)|\le p_{N,0}(b)u^N\); on \(u\ge1\), \(|b(u)|\le p_{N,0}(b)u^{-N}\). Multiplying these bounds by \(u^{\Re z-1}|\log u|^j\) gives uniformly finite integrals for every \(j\). Thus
\[
 \partial_z^jM_{A,z}(b)
 =\int_0^\infty b(u)u^z(\log u)^j\,\frac{du}{u}.
 \tag{MCL1.4}
\]
The same estimates, using a slightly larger compact parameter set and the exponential Taylor remainder, prove locally uniform convergence of the Taylor series on each bounded set of \(A\). In particular \(M_{A,z}\) is entire as a family in the strong continuous dual, not only after one fixed evaluation.

Evenness and \(h(0)=0\) give \(h'(0)=0\). Taylor's integral formula gives
\[
 |h(v)|\le \frac{v^2}{2}\sup_{|t|\le1}|h''(t)| \quad(0<v\le1).
\]
Together with Schwartz decay at infinity, this bounds the integrand of every \(z\)-derivative in (MCL1.3), uniformly on compact subsets of \(\Re z>-2\). The same Taylor-remainder argument proves holomorphy there, with
\[
 \partial_z^jM_{S,z}(h)
 =\int_0^\infty h(v)v^z(\log v)^j\,\frac{dv}{v}.
 \tag{MCL1.5}
\]
Its endpoint identity is exactly
\[
 M_{S,1}(h)=\int_0^\infty h(v)\,dv
 =\frac12\int_{\mathbb R}h(v)\,dv=0.
 \tag{MCL1.6}
\]
This particular zero functional is not omitted or relabelled as an arbitrary eigenvector.

Retain the actual two-sign summation and its transpose:
\[
 \Sigma h(u)=2\sum_{n\ge1}h(nu),\qquad
 \Sigma':A'\longrightarrow S',\quad
 (\Sigma'\lambda)(h)=\lambda(\Sigma h).
 \tag{MCL1.7}
\]
For \(\Re z>1\), Tonelli applied to absolute values gives
\[
 \sum_{n\ge1}\int_0^\infty |h(nu)|u^{\Re z}\frac{du}{u}
 =\left(\sum_{n\ge1}n^{-\Re z}\right)
 \int_0^\infty |h(v)|v^{\Re z}\frac{dv}{v}<\infty.
\]
Changing \(v=nu\), with the original factor2, proves
\[
 \boxed{\Sigma'M_{A,z}=2\zeta(z)M_{S,z}.}
 \tag{MCL1.8}
\]
This extends through \(\Re z>-2\). Indeed the only pole of \(\zeta\) there is at one, and (MCL1.6) makes its product removable; both sides are holomorphic after that specified removal. Evaluation on every \(h\) and the identity theorem proves equality, and the uniform estimates above give the same dual-family identity.

The contribution at the original pole has an explicit value. Write
\(\zeta(z)=(z-1)^{-1}+\gamma+O(z-1)\). Then
\[
 \Sigma'M_{A,1}=2\,\partial_zM_{S,z}\big|_{z=1}.
 \tag{MCL1.9}
\]
The pole has combined with the first source Mellin derivative, rather than being silently discarded. Only actual nontrivial zeros \(0<\Re\rho<1\), never this endpoint, are used below.

For the prior centered receiver retain
\[
 \mathcal Tk(u)=2u^{-1/2}k(u),\qquad
 \mathcal T^{-1}b(u)=\frac12u^{1/2}b(u),\qquad
 F_k(z)=\int_0^\infty k(u)u^{z-1/2}\frac{du}{u}.
\]
Consequently
\[
 \mathcal T'\big(\partial_z^jM_{A,z}\big)(k)
 =2\,\partial_z^jF_k(z).
 \tag{MCL1.10}
\]
Every factor and exponent of this earlier comparison survives.

## MCL2. Actual dilation, transpose, contragredient and twist

For \(a>0\), set
\[
 T_ab(u)=b(u/a),\qquad D_ah(v)=h(v/a).
\]
Both are continuous automorphisms of their stated spaces; dilation multiplies the zero integral of \(h\) by \(a\), keeps its zero value and evenness, and scales each defining seminorm by finite powers of \(a,a^{-1}\). Direct summation gives
\[
 \Sigma D_a=T_a\Sigma.
 \tag{MCL2.1}
\]
The generators for \(a=e^t\) are the continuous operators
\[
 L_A=-u\partial_u,\qquad L_S=-v\partial_v .
\]
For \(L_S\), evenness is preserved, its value at zero vanishes, and integration by parts gives \(\int L_Sh=\int h=0\). Differentiating in the stated topologies follows from the integral Taylor remainder for translation in \(t\), bounded by the next two derivative seminorms. Write
\[
 K_A=L_A^t,\qquad K_S=L_S^t,\qquad
 \Sigma'K_A=K_S\Sigma'.
 \tag{MCL2.2}
\]
Here \(t\) denotes the ordinary continuous transpose, not a contragredient convention.

Substitution and differentiation prove the full formulas
\[
 T_a^tM_{A,z}=a^zM_{A,z},\qquad
 D_a^tM_{S,z}=a^zM_{S,z},
\]
\[
 T_a^t\partial_z^jM_{A,z}
 =a^z\sum_{k=0}^j\binom jk(\log a)^{j-k}
       \partial_z^kM_{A,z},
\]
\[
 D_a^t\partial_z^jM_{S,z}
 =a^z\sum_{k=0}^j\binom jk(\log a)^{j-k}
       \partial_z^kM_{S,z}.
 \tag{MCL2.3}
\]
All identities hold before specializing \(a\) to a prime.

The continuous-dual representation used in the supported row has the contragredient followed by the stated character:
\[
 T_a^\vee=(T_{a^{-1}})^t,\qquad
 \mathcal U_a^A=a(T_{a^{-1}})^t,\qquad
 \mathcal U_a^S=a(D_{a^{-1}})^t,\qquad \chi(a)=a.
\]
Its generators are \(G_A=1-K_A\), \(G_S=1-K_S\), and
\[
 \mathcal U_a^A\partial_z^jM_{A,z}
 =a^{1-z}\sum_{k=0}^j\binom jk(-\log a)^{j-k}
       \partial_z^kM_{A,z},
 \tag{MCL2.4}
\]
with the identical formula in \(S'\). Thus ordinary transpose character \(a^z\), contragredient character \(a^{-z}\), and the supported twisted character \(a^{1-z}\) are explicitly different. The twist is an operation on the receiving representation, not a property assigned to primitive \(\tau\).

## MCL3. Classify all generalized Euler characters on the original \(A'\)

Fix \(\rho\in\mathbb C\) and abbreviate
\[
 A_j=\partial_z^jM_{A,z}\big|_{z=\rho}\quad(j\ge0).
\]
Then
\[
 (K_A-\rho)A_j=jA_{j-1},\qquad
 (K_A-\rho)A_0=0.
 \tag{MCL3.1}
\]
We prove the complete classification
\[
 \boxed{\ker(K_A-\rho)^d
       =\operatorname{span}\{A_0,\ldots,A_{d-1}\}
       \quad(d\ge1).}
 \tag{MCL3.2}
\]
This concerns every continuous functional on \(A\) satisfying the equation, not a selected Mellin subspace.

Put \(x=\log u\), \(\phi(x)=b(e^x)\). This identifies \(A\) topologically with the smooth functions on \(\mathbb R\) for which
\[
 q_{N,j}(\phi)=\sup_x(e^{Nx}+e^{-Nx})|\phi^{(j)}(x)|<\infty
\]
for all \(N,j\). The generator becomes \(-\partial_x\). The compactly supported smooth functions are dense. To prove this, choose \(\eta\in C_c^\infty(\mathbb R)\) equal to one on \([-1,1]\), and set \(\eta_R(x)=\eta(x/R)\), \(R\ge1\). Leibniz's rule bounds each \(q_{N,j}((1-\eta_R)\phi)\) by a finite sum of tails of \(\phi^{(k)}\) on \(|x|\ge R\), with coefficients \(R^{-(j-k)}\) bounded by one. Those tails tend to zero using \(q_{N+1,k}(\phi)\) and the factor \(e^{-|x|}\). Hence \(\eta_R\phi\to\phi\) in every seminorm.

A continuous functional on this space restricts to a distribution on \(C_c^\infty(\mathbb R)\): on each fixed compact set, the inclusion is continuous for the usual smooth test topology. If \(\lambda\) satisfies the left side of (MCL3.2), its restricted distribution \(U\) satisfies
\[
 (\partial_x-\rho)^dU=0.
\]
Indeed distribution differentiation means \(U'(\phi)=-U(\phi')\), exactly the transpose of \(-\partial_x\). Multiplication of distributions by the smooth function \(e^{-\rho x}\) is defined by testing against that multiplier. The product rule gives
\[
 \partial_x^d(e^{-\rho x}U)=0.
\]

Here is the required distribution equation proof. If \(V'=0\), choose a compactly supported smooth \(\eta_0\) with integral one. A compact test \(\psi\) of integral zero is the derivative of the compactly supported smooth function
\(\int_{-\infty}^x\psi(t)\,dt\). Therefore \(V(\psi)=0\), and
\(V(\phi)=V(\eta_0)\int\phi\); it is the constant distribution. Inductively, if \(V^{(d)}=0\), then \(V^{(d-1)}\) is constant; subtract that constant times \(x^{d-1}/(d-1)!\), and apply the induction hypothesis. Thus \(V\) is a polynomial of degree at most \(d-1\). It follows that \(U\) has density \(e^{\rho x}P(x)\) with \(\deg P<d\).

Every such density is continuous on the entire original space by the exponential estimates in MCL1. Density of compact tests proves that its extension agrees with \(\lambda\) everywhere. The density \(e^{\rho x}x^j\) is precisely \(A_j\). These densities are linearly independent on compact tests, proving (MCL3.2) and uniqueness of the coefficients.

For any nonzero \(\lambda=\sum_{j=0}^Jc_jA_j\) with \(c_J\ne0\), (MCL3.1) gives
\[
 (K_A-\rho)^J\lambda=c_JJ!A_0\ne0,\qquad
 (K_A-\rho)^{J+1}\lambda=0.
 \tag{MCL3.3}
\]
Thus its exact generalized-character order is \(J+1\).

The full real action and simultaneous arithmetic-prime conditions admit the same classification. To make this assertion exact, let \(p,q\) be two distinct primes and let \(r,s\ge1\). Then
\[
 \boxed{
 \ker(T_p^t-p^\rho)^r\cap\ker(T_q^t-q^\rho)^s
 =\operatorname{span}\{A_j:0\le j<\min(r,s)\}.
 }
 \tag{MCL3.4}
\]
Here is a direct proof retaining the possible one-prime ambiguity. Restrict a functional to compact tests, write its distribution as \(U=e^{\rho x}V\), and let \(\mathsf E_h\) translate the density by \(x\mapsto x+h\). The two equations become
\((\mathsf E_h-1)^rV=0\) and
\((\mathsf E_\ell-1)^sV=0\), with \(h=\log p\), \(\ell=\log q\).
The commuting ideal generated by these two differences has its \((r+s-1)\)-st power killing \(V\), by the binomial pigeonhole count. For integers \(m,n\),
\(\mathsf E_{mh+n\ell}-1\) belongs to that ideal with coefficients that are finite translation sums. Negative integers are included using
\(\mathsf E_{-h}-1=-\mathsf E_{-h}(\mathsf E_h-1)\).
Consequently
\[
 (\mathsf E_{mh+n\ell}-1)^{r+s-1}V=0.
\]
The ratio \(h/\ell\) is irrational, since a rational relation would give equal positive powers of distinct primes. Integer combinations \(mh+n\ell\) are dense in \(\mathbb R\): the pigeonhole principle applied to fractional parts of multiples of \(h/\ell\) gives nonzero such combinations arbitrarily close to zero, and integer multiples approximate any fixed real number. Translation is continuous on compact tests in their test topology, so the last difference equation holds at every real step. Dividing by that step to the power \(r+s-1\) and taking its limit at zero gives \(\partial_x^{r+s-1}V=0\). Thus \(V\) is a polynomial. A nonzero finite difference with fixed nonzero step reduces polynomial degree exactly by one; its original two equations force degree \(<r\) and \(<s\). The density and extension argument above finishes (MCL3.4).

For one prime alone the conclusion would be false: \(M_{A,\rho+2\pi i k/\log p}\), \(k\in\mathbb Z\), has the same \(p^\rho\) eigenvalue. MCL3.4 proves that retaining two distinct original primes removes those aliases. It justifies the full-character minimality below also under simultaneous all-prime generalized-character requirements; no single-prime converse is assumed.

## MCL4. The actual source Mellin jets are independent

Fix an actual nontrivial zero \(\rho\), so \(0<\Re\rho<1\), and put
\[
 S_j=\partial_z^jM_{S,z}\big|_{z=\rho}.
\]
All these functionals are defined by MCL1. They satisfy
\[
 (K_S-\rho)S_j=jS_{j-1},\qquad (K_S-\rho)S_0=0.
 \tag{MCL4.1}
\]
They are linearly independent, including \(S_0\ne0\).

To prove it, test against \(h(v)=f(|v|)\), where
\(f\in C_c^\infty(0,\infty)\) and \(\int_0^\infty f(v)\,dv=0\).
Such \(h\) belongs to the original \(S\). If \(\sum_{j=0}^Jc_jS_j=0\), the smooth function
\[
 v^{\rho-1}P(\log v),\qquad P(X)=\sum_{j=0}^Jc_jX^j,
\]
annihilates every such zero-integral test. Choose one compact test of integral one and subtract its multiple from each arbitrary test. It follows that the displayed smooth function equals a constant on \((0,\infty)\), as distributions and hence pointwise. In \(x=\log v\), differentiating this constant identity gives
\[
 P'(x)+(\rho-1)P(x)=0.
\]
Since \(\rho-1\ne0\), comparison of the leading coefficient of a nonzero polynomial makes that impossible. Hence every \(c_j=0\). This also shows exactly why the endpoint \(z=1\), where MCL1.6 holds, must not be included in this assertion.

## MCL5. The exact triangular lift of every jet

Let \(m\ge1\) be the actual multiplicity of \(\rho\):
\[
 \zeta^{(k)}(\rho)=0\quad(0\le k<m),\qquad
 \zeta^{(m)}(\rho)\ne0.
\]
Differentiating the full original identity (MCL1.8) gives
\[
 \Sigma'A_n
 =2\sum_{k=0}^n\binom nk
       \zeta^{(n-k)}(\rho)S_k .
 \tag{MCL5.1}
\]
In particular
\[
 \Sigma'A_n=0\quad(n<m),
\]
\[
 \boxed{\Sigma'A_{m+j}
 =2\sum_{k=0}^j\binom{m+j}{k}
       \zeta^{(m+j-k)}(\rho)S_k.}
 \tag{MCL5.2}
\]
The coefficient of \(S_j\) is
\(2\binom{m+j}{j}\zeta^{(m)}(\rho)\ne0\).
Define the explicit lifts recursively:
\[
 \Lambda_{\rho,0}=\frac{A_m}{2\zeta^{(m)}(\rho)},
\]
\[
 \boxed{
 \Lambda_{\rho,j}
 =
 \frac{A_{m+j}
 -2\sum_{k=0}^{j-1}\binom{m+j}{k}
       \zeta^{(m+j-k)}(\rho)\Lambda_{\rho,k}}
 {2\binom{m+j}{j}\zeta^{(m)}(\rho)}\quad(j\ge1).
 }
 \tag{MCL5.3}
\]
Induction using (MCL5.2) proves
\[
 \Sigma'\Lambda_{\rho,j}=S_j.
 \tag{MCL5.4}
\]
These are finite linear combinations of continuous functionals on the original \(A\), so their continuity does not rely on an unspecified distribution completion.

There is a full analytic family giving the same lifts. In a disk about \(t=0\) containing no other zero and with \(\Re(\rho+t)>-2\), write the exact factorization
\[
 \zeta(\rho+t)=t^m g_\rho(t),\qquad
 g_\rho(0)=\frac{\zeta^{(m)}(\rho)}{m!},\qquad
 v_\rho(t)=\frac1{2g_\rho(t)}.
 \tag{MCL5.5}
\]
This is a proved local factor of the original \(\zeta\), whose derivatives are retained; it does not replace it as a working function. The dual-valued Taylor remainder
\[
 \mathcal A_\rho(t)=
 \frac{M_{A,\rho+t}
       -\sum_{n=0}^{m-1}t^nA_n/n!}{t^m}
\]
has its unique removable continuation at zero by MCL1. Since every subtracted functional lies in \(\ker\Sigma'\), (MCL1.8) gives
\[
 \boxed{\Sigma'\big(v_\rho(t)\mathcal A_\rho(t)\big)
        =M_{S,\rho+t}.}
 \tag{MCL5.6}
\]
Differentiating it yields the full expression
\[
 \boxed{
 \Lambda_{\rho,j}
 =j!\sum_{k=0}^j
 \frac{v_\rho^{(j-k)}(0)}
      {(j-k)!(m+k)!}\,A_{m+k}.
 }
 \tag{MCL5.7}
\]
Its leading coefficient is
\[
 \frac{j!\,m!}{2(m+j)!\zeta^{(m)}(\rho)}.
 \tag{MCL5.8}
\]
Formulas (MCL5.3) and (MCL5.7) agree because both lie in
\(\operatorname{span}(A_m,\ldots,A_{m+j})\), and (MCL5.2) is injective on that span. Every derivative of the reciprocal in (MCL5.7) is determined by the full identity \(2g_\rho v_\rho=1\). No derivative, multiplicity, sign or factor2 has been removed.

## MCL6. Least generalized-character enlargement in the full dual

Let \(N_A=K_A-\rho\), \(N_S=K_S-\rho\). For integers \(d\ge0\), write
\[
 \mathcal E_A(d)=\operatorname{span}(A_0,\ldots,A_{d-1}),
 \qquad \mathcal E_A(0)=0,
\]
and \(\mathcal E_S(r)=\operatorname{span}(S_0,\ldots,S_{r-1})\) for \(r\ge1\).
MCL3 and MCL5 prove
\[
 \ker\!\left(\Sigma'|_{\mathcal E_A(d)}\right)
   =\mathcal E_A(\min(d,m)),
\]
\[
 \Sigma'\mathcal E_A(d)=
 \begin{cases}0,&d\le m,\\
 \mathcal E_S(d-m),&d>m.
 \end{cases}
 \tag{MCL6.1}
\]
The proof uses the nonzero triangular coefficients (MCL5.2) and the independence in MCL4; it is valid for the complete functionals, not only their formal Taylor symbols.

Consequently every lift of \(S_j\) that is a generalized \(\rho\)-character has order at least \(m+j+1\). The lift in (MCL5.7) has exactly that order by its nonzero coefficient (MCL5.8) and (MCL3.3). Moreover all finite generalized \(\rho\)-character lifts of that particular \(S_j\) are precisely
\[
 \boxed{
 \Lambda_{\rho,j}+\mathcal E_A(m).
 }
 \tag{MCL6.2}
\]
Indeed a larger highest derivative would give a nonzero source jet of index greater than \(j\), by the same triangular calculation. The remaining difference lies in the stated kernel.

For the whole target block of length \(r\), the least possible finite invariant preimage is the exact original sequence
\[
 \boxed{
 0\longrightarrow\mathcal E_A(m)
 \longrightarrow\mathcal E_A(m+r)
 \xrightarrow{\ \Sigma'\ }\mathcal E_S(r)
 \longrightarrow0.
 }
 \tag{MCL6.3}
\]
It is invariant under every positive real dilation, hence under every original prime. Its middle term is a single Jordan block of length \(m+r\); the target is a block of length \(r\); the full original kernel is the block of length \(m\).

For completeness, any finite \(K_A\)-invariant subspace of generalized \(\rho\)-characters that surjects onto \(\mathcal E_S(r)\) must contain a preimage with highest derivative index at least \(m+r-1\). Its successive \(N_A\)-images then span every \(A_n\), \(0\le n\le m+r-1\), by triangular elimination. It therefore contains \(\mathcal E_A(m+r)\). This proves the asserted least subspace, not merely a lower bound on a conveniently chosen lift.

A pure \(\rho\)-character lift of \(S_0\) does not exist: MCL3 says it would be a multiple of \(A_0\), whereas (MCL5.1) sends every such multiple to zero and MCL4 gives \(S_0\ne0\). This is a statement about the actual receiving map \(\Sigma'\). Its exact replacement is (MCL6.3) with \(r=1\), of length \(m+1\), not a claim that the source or the full programme has no relation to a lift.

By (MCL3.4), the same least-order assertion holds for lifts subject to simultaneous generalized \(p^\rho\) and \(q^\rho\) conditions for two distinct original primes. A one-prime character condition alone is not silently substituted for that hypothesis. For the constructed lift, its exact order is visible at each individual nonidentity dilation too. In the finite action (MCL2.3), one application of \(T_a^t-a^\rho\) lowers the highest derivative index by one with coefficient \(a^\rho n\log a\). Iterating and retaining (MCL5.8) gives
\[
 (T_a^t-a^\rho)^{m+j}\Lambda_{\rho,j}
 =a^{(m+j)\rho}
 \frac{j!\,m!}{2\zeta^{(m)}(\rho)}
 (\log a)^{m+j}A_0\ne0\quad(a\ne1),
 \qquad
 (T_a^t-a^\rho)^{m+j+1}\Lambda_{\rho,j}=0.
 \tag{MCL6.4}
\]
For the twisted action the same expression has \(a^{(m+j)(1-\rho)}\) and \((-\log a)^{m+j}\), obtained directly from (MCL2.4). Thus no prime logarithmic factor is hidden in the order assertion.

## MCL7. Full prime logarithms and the exact lifting defect

Write the retained coefficients
\[
 \ell_{jk}
 =\frac{j!\,v_\rho^{(j-k)}(0)}
       {(j-k)!(m+k)!},\qquad
 \Lambda_{\rho,j}=\sum_{k=0}^j\ell_{jk}A_{m+k}.
\]
Applying the complete action (MCL2.3) gives
\[
 T_a^t\Lambda_{\rho,j}
 =a^\rho\sum_{k=0}^j\ell_{jk}
       \sum_{n=0}^{m+k}\binom{m+k}{n}
       (\log a)^{m+k-n}A_n.
 \tag{MCL7.1}
\]
The image under \(\Sigma'\) is exactly \(D_a^tS_j\), so the failure of the chosen section to intertwine dilation is the explicit kernel element
\[
 \boxed{
 \begin{aligned}
 \mathfrak d_{\rho,j}(a)
 &:=
 T_a^t\Lambda_{\rho,j}
 -a^\rho\sum_{i=0}^j\binom ji(\log a)^{j-i}
       \Lambda_{\rho,i}\\
 &=a^\rho\sum_{n=0}^{m-1}
   \left[
    \sum_{k=0}^j\ell_{jk}\binom{m+k}{n}
       (\log a)^{m+k-n}
   \right]A_n.
 \end{aligned}
 }
 \tag{MCL7.2}
\]
To verify the second equality, first expand the first term by (MCL7.1). The second term has only derivative indices at least \(m\). The image of their difference is zero; injectivity of \(\Sigma'\) on the high-derivative span forces all coefficients with \(n\ge m\) to cancel. Its remaining coefficients are precisely the displayed low-derivative terms. This proves the equality in the full \(A'\), including all kernel data.

For the pure target,
\[
 \boxed{
 \mathfrak d_{\rho,0}(a)
 =\frac{a^\rho}{2\zeta^{(m)}(\rho)}
 \sum_{n=0}^{m-1}\binom mn(\log a)^{m-n}A_n .
 }
 \tag{MCL7.3}
\]
For every \(a\ne1\), its coefficient of \(A_{m-1}\) is
\(a^\rho m\log a/(2\zeta^{(m)}(\rho))\ne0\).
In particular every original prime has a nonzero defect for this chosen lift, while the complete block (MCL6.3) carries its exact action without losing those terms.

Under the supported contragredient twist the corresponding identity is
\[
 \boxed{
 \mathcal U_a^A\Lambda_{\rho,j}
 -a^{1-\rho}\sum_{i=0}^j\binom ji(-\log a)^{j-i}
       \Lambda_{\rho,i}
 =a\,\mathfrak d_{\rho,j}(a^{-1}).
 }
 \tag{MCL7.4}
\]
It follows by applying (MCL7.2) at \(a^{-1}\), then multiplying by the original scalar character \(a\). Thus every logarithm, its sign and the exact exponent \(1-\rho\) are retained.

## MCL8. Exact Fourier return and the reflected zero block

The original involutions are
\[
 Rb(u)=u^{-1}b(u^{-1}),\qquad
 \mathcal Fh(t)=\int_{\mathbb R}h(v)e^{-2\pi ivt}\,dv .
\]
Poisson summation, with both endpoint terms retained before their vanishing on \(S\), gives
\(\Sigma\mathcal F=R\Sigma\), and hence
\[
 \mathcal F^t\Sigma'=\Sigma'R^t.
 \tag{MCL8.1}
\]
The raw Mellin integrals give directly
\[
 R^tM_{A,z}=M_{A,1-z},\qquad
 R^t A_j(\rho)=(-1)^jA_j(1-\rho).
 \tag{MCL8.2}
\]
Let \(b=1-\rho\). The original functional equation makes \(b\) an actual zero of the same multiplicity \(m\). On a neighborhood of \(\rho\), its exact multiplier
\[
 \kappa(z)=\frac{\zeta(1-z)}{\zeta(z)}
 =\pi^{1/2-z}\frac{\Gamma(z/2)}{\Gamma((1-z)/2)}
 =\frac1{2^z\pi^{z-1}\sin(\pi z/2)\Gamma(1-z)}
 \tag{MCL8.3}
\]
is holomorphic and nonzero, with all factors displayed. This formula is only used on its proved local domain; no Gamma factor is declared globally invertible through its poles.

Applying (MCL1.8) and (MCL8.1) first where division by \(\zeta\) is legitimate, then continuing through its removable ratio at \(\rho\), gives
\[
 \mathcal F^tM_{S,z}=\kappa(z)M_{S,1-z}.
\]
All source Mellin integrals in this equality are defined on their common strip \(-2<\Re z<3\), with the exact removable or meromorphic comparisons as appropriate. In the chosen neighborhood of \(\rho\) the full derivative formula is
\[
 \boxed{
 \mathcal F^t S_j(\rho)
 =\sum_{k=0}^j\binom jk\kappa^{(j-k)}(\rho)
            (-1)^k S_k(b).
 }
 \tag{MCL8.4}
\]
At order zero the retained coefficient is
\[
 \kappa(\rho)=
 \frac{(-1)^m\zeta^{(m)}(b)}{\zeta^{(m)}(\rho)}.
 \tag{MCL8.5}
\]

The chosen high-derivative lifts satisfy the stronger exact identity
\[
 \boxed{
 R^t\Lambda_{\rho,j}
 =\sum_{k=0}^j\binom jk\kappa^{(j-k)}(\rho)
            (-1)^k\Lambda_{b,k}.
 }
 \tag{MCL8.6}
\]
Both sides lie in \(\operatorname{span}(A_m(b),\ldots,A_{m+j}(b))\), by (MCL5.7) and (MCL8.2). Their images under \(\Sigma'\) agree by (MCL8.1) and (MCL8.4). The triangular injectivity in MCL5 then proves equality, without discarding a kernel ambiguity. In particular this chosen lift is exactly Fourier-compatible across the reflected blocks, although its dilation defect is the nonzero expression MCL7.

The unshifted transpose relation is
\(T_a^tR^t=aR^tT_{a^{-1}}^t\), as can also be checked on (MCL8.2). The twisted relation is
\(\mathcal U_a^AR^t=aR^t\mathcal U_{a^{-1}}^A\).
The oriented Cech dual adds the separately retained minus sign of ASD/UOS. No new sign or Tate twist is inferred from the Fourier ratio.

## MCL9. The actual character connecting map and its nonzero class

The proved closed-image theorem makes
\(\Sigma:S\to J=\Sigma S\) a topological isomorphism onto a closed subspace of \(A\). Its actual continuous-dual sequence is
\[
 0\longrightarrow Q'
 \xrightarrow{\pi'}A'\xrightarrow{\Sigma'}S'
 \longrightarrow0,\qquad Q=A/J.
 \tag{MCL9.1}
\]
It is algebraically exact and strictly exact for weak-* topologies; the transposes are also strong-dual continuous. For clarity, surjectivity follows by transporting a continuous functional from \(S\) to \(J\) using \(\Sigma^{-1}\), then extending it to \(A\) by complex Hahn–Banach. Its kernel is \(J^\perp=\pi'Q'\). This is the actual sequence in ASD2, not a presumed spectral expansion of arbitrary distributions.

The generalized \(\rho\)-character part of its kernel is exactly
\[
 J^\perp\cap\bigcup_{d\ge1}\ker(K_A-\rho)^d
 =\mathcal E_A(m).
 \tag{MCL9.2}
\]
This follows immediately from the full classification MCL3, MCL5's triangular map, and MCL4's independence. It shows that the \(m\) kernel levels in the least enlargement are the actual original multiplicity block of \(Q'\).

To construct the connecting map rather than name one, put
\(N=K-\rho\) on each of the three terms of (MCL9.1). For each \(r\ge1\), form the two-term complex
\([E\xrightarrow{N^r}E]\) in degrees zero and one. The operators commute with the maps in (MCL9.1), so these three complexes form a degreewise short exact sequence. Its cohomological connecting map is
\[
 \partial_{\rho,r}:
 \ker(N_S^r:S'\to S')
 \longrightarrow Q'/N_Q^rQ'.
\]
An actual lift \(\lambda\in A'\) of \(s\in\ker N_S^r\) satisfies
\(N_A^r\lambda\in J^\perp\), and
\[
 \boxed{\partial_{\rho,r}(s)
       =[(\pi')^{-1}N_A^r\lambda].}
 \tag{MCL9.3}
\]
Another lift differs by \(\pi'\eta\), so its value changes by \(N_Q^r\eta\). This proves that the formula is well-defined and is the connecting map of the displayed complexes.

For the pure character \(s=S_0\), \(r=1\), the exact lift in MCL5 gives
\[
 \boxed{
 \partial_{\rho,1}(S_0)
 =
 \left[
 \frac{m}{2\zeta^{(m)}(\rho)}
  (\pi')^{-1}A_{m-1}
 \right]\ne0 .
 }
 \tag{MCL9.4}
\]
To prove nonzero in the full quotient, suppose
\(N_Q\eta=\frac{m}{2\zeta^{(m)}(\rho)}(\pi')^{-1}A_{m-1}\).
Then
\(N_A^{m+1}\pi'\eta=0\), so MCL3 places \(\pi'\eta\) in a finite generalized-character space. Since it belongs to \(J^\perp\), MCL9.2 puts it in \(\mathcal E_A(m)\). Its \(N_A\)-image is then in
\(\operatorname{span}(A_0,\ldots,A_{m-2})\), and cannot equal
\(\frac{m}{2\zeta^{(m)}(\rho)}A_{m-1}\), whose coefficient is nonzero. The same proof covers \(m=1\), when this last span is zero. Thus no functional outside the initially chosen finite block supplies a missed preimage: the proposed equation itself forces it into that block.

For every jet \(s=S_j\), put \(r=j+1\). It lies in \(\ker N_S^r\), and the full representative of its connecting class is
\[
 \boxed{
 N_A^r\Lambda_{\rho,j}
 =j!\sum_{\substack{0\le k\le j\\m+k\ge r}}
 \frac{v_\rho^{(j-k)}(0)}
 {(j-k)!(m+k-r)!}\,A_{m+k-r}.
 }
 \tag{MCL9.5}
\]
Its highest term is
\[
 \frac{j!\,m}{2\zeta^{(m)}(\rho)}A_{m-1}\ne0.
 \tag{MCL9.6}
\]
Every term in (MCL9.5) lies in the original kernel. If the class were in \(N_Q^rQ'\), a putative preimage would satisfy
\(N_A^{m+r}\pi'\eta=0\), hence again lie in \(\mathcal E_A(m)\) by MCL9.2. But \(N_A^r\mathcal E_A(m)\) has derivative indices strictly below \(m-1\), contradicting (MCL9.6). Therefore each \(\partial_{\rho,j+1}(S_j)\) is nonzero.

In the actual supported twisted representation the operator is
\(G-(1-\rho)=-(K-\rho)\). Replacing \(N^r\) accordingly multiplies the exact representative (MCL9.5) by \((-1)^r\); it does not alter its nonvanishing or replace the character \(a^{1-\rho}\) by \(a^\rho\).

This character connecting map is not the quotient map from the residue-duality cone in ASD14. It is constructed from the different actual exact sequence (MCL9.1), with its maps and endomorphism complexes explicit. The zero or nonzero status of one cannot be substituted for that of the other.

## MCL10. Exact location in the source-supported row, including all closed terms

Use the actual global graph and faithful extra coefficients:
\[
 H=H_0\oplus V_{\mathrm{extra}},\qquad
 H_0=\{((h,c_0,c_1),(\widehat h,d_0,d_1)):h\in S\}
 \simeq S\oplus\mathbb C^4,
\]
\[
 V_{\mathrm{extra}}=V_+^{\mathrm{extra}}\oplus V_-^{\mathrm{extra}},
 \qquad E=\mathbb C^4\oplus V_{\mathrm{extra}}.
\]
The original supported row and its complete transpose in UOS3 are
\[
 0\to E\to H\xrightarrow{\mathrm{res}}A
 \to Q^2\to Q\to0,
\]
\[
 0\to Q'\to(Q')^2\to A'
 \xrightarrow{\mathrm{res}'}H'\to E'\to0.
 \tag{MCL10.1}
\]
Here \(\mathrm{res}((h,c),(\widehat h,d),w)=\Sigma h\), hence
\[
 \boxed{
 \mathrm{res}'\lambda
 =(\Sigma'\lambda,0,0,0,0,0),\qquad
 H'=S'\oplus(\mathbb C^4)'\oplus V_{\mathrm{extra}}'.
 }
 \tag{MCL10.2}
\]
The last zero denotes the entire pair of extra coefficient duals, not only their endpoints. Let
\[
 \jmath_S:S'\to H',\quad
 s\mapsto(s,0,0,0,0,0).
\]
Then the lift calculation has the exact supported identity
\[
 \boxed{\mathrm{res}'\Lambda_{\rho,j}=\jmath_SS_j.}
 \tag{MCL10.3}
\]
The map \(H'\to E'\) is restriction to all four endpoint and extra coordinates; it kills these particular \(\jmath_SS_j\), exactly because they lie in the image of (MCL10.2). It remains nonzero on the retained endpoint and extra copies. Thus these original supported functionals do lift as continuous functionals. MCL6 and MCL9 compute the precise extra generalized-character structure needed, rather than denying the continuous lift.

Twisting the whole row by \(\chi\) yields the actual supported dual actions used in UOS. Parametrization of \(H_0\) by \(h\) identifies its \(S\)-action with \(D_a h\); its four endpoint characters stay \(1,a,a,1\), and the full extra copies retain the two original chart actions. Therefore \(\jmath_S\), (MCL10.2) and (MCL10.3) have exactly the actions in MCL2. Their transpose Fourier mirror on the \(S'\)-coordinate is \(\mathcal F^t\), with the chart/orientation signs of the full row retained separately. Formula (MCL8.6) proves the mirror compatibility of these actual lifts.

The source receiving ring is the already constructed \(\mathbb Z^3\), with source
\([n]=(n,0,0)\), \([\tau]=(1,1,1)\).
On \(A',S'\) and the \(S'\)-coordinate of \(H'\), the first ring coordinate acts by its scalar. On the two complete extra closed copies, their corresponding additional coordinates act. Formula (MCL10.2) is receiving-ring linear. Thus all lift formulas preserve the source action: original integer \(n\) acts as scalar \(n\), independently of the spectral operator at \(a=n>0\). Primitive \(\tau\) remains distinguished from integer one by the faithful extra coefficients of the full object. No addition or numerical weight of \(\tau\) is introduced.

For each bounded distributive receiving support lattice \(L_{\mathrm{supp}}\), every linear map here has the already constructed lift
\[
 G_{L_{\mathrm{supp}}}(f)(v,\alpha)=(f(v),\alpha),\qquad
 G_{L_{\mathrm{supp}}}(V)
 =\{(0,\alpha):\alpha\in L_{\mathrm{supp}}\}
   \cup\{(v,1_{L_{\mathrm{supp}}}):v\in V\}.
 \tag{MCL10.4}
\]
If \(\alpha\ne1_{L_{\mathrm{supp}}}\), the amplitude is zero and linearity keeps it zero with that same label. At the top label, an amplitude cancellation likewise keeps its label. Identity and composition follow by substitution. Independent labels on separate closed factors remain separate; no common-label carrier is equated with their product. In particular the vanishing amplitudes for \(A_0,\ldots,A_{m-1}\) under \(\Sigma'\) retain their original receiving support labels and are not relabelled as primitive \(\tau\).

## MCL11. What this completes in the lifting calculation

For every actual nontrivial zero \(\rho\) and every actual multiplicity \(m\), the original supported transpose has the explicit lift (MCL5.7) of every source Mellin jet. Its least generalized-character order is exactly \(m+j+1\), proved against all continuous generalized eigen-distributions of the original \(A\). Simultaneous conditions at two distinct arithmetic primes recover the same full-character statement. The full least enlargement, every prime logarithm and the exact Fourier return are (MCL6.3), (MCL7.2)–(MCL7.4), and (MCL8.6).

The actual character connecting map is nonzero on these targets by (MCL9.4)–(MCL9.6). Its class is an element of the original spectral-kernel quotient, with a complete representative and proof that no omitted global dual functional makes it zero. The continuous supported lift itself exists by (MCL10.3). These two statements refer to explicitly different requirements on that same computed lift, with their exact comparison given.

This calculation neither assumes nor proves \(\Re\rho=1/2\). It occurs at every original zero, including any zero on the critical line, with the same formulas and its actual multiplicity. Consequently its nonzero character extension is not an RH disproof or a failure of the user's reconstructed arithmetic. Nor is the needed nilpotent enlargement a Deligne weight separation: its kernel and target retain the same character exponent, and the complete prime-action coupling is the calculated nonzero polynomial in \(\log a\). The result specifies the actual supported lifting object and its exact coupling, which must be retained in the next comparison with Deligne's geometric argument.
