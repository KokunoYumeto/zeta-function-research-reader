# Independent bounded audit of U0012, A0618, U0013, U0014, A0626, and A0638

## Scope and provenance

Read in full: `output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0001_U0015.md`, lines **1995–2838**, on 2026-09-13. Every numbered source pin below refers to that file. This audit does not infer a later F1 programme from these turns. It distinguishes calculations actually displayed, cited external constructions, proposed constructions, and the user's explicitly provisional physical interpretation.

The user insists on preserving signs, coordinates, and exact maps in U0012 (**1995–1997**). U0013 (**2819–2823**) corrects the assistant's target: the requested explanation is physical, and merely calling the missing object a surviving arithmetic class does not answer that request. U0014 (**2825–2829**) supplies the proposed modular-time/Rindler/KMS/gravitational chain and explicitly asks to investigate it provisionally. A0626 and A0638 (**2831–2837**) state intentions to examine freely falling observables and mass inflation; they do not yet perform those calculations.

Two primary-source checks were made using read-only web tools, without operating the root browser:

1. [Connes–Consani, *BC-system, absolute cyclotomy and the quantized calculus*, published PDF](https://alainconnes.org/wp-content/uploads/BC-system-absoute-cyclotomypublished.pdf), printed p. 469, equations (20)–(24). Its extracted text confirms the nonpositive criterion and the factor one half in the trace formula. PDF text extraction mangles some superscript signs; no claim of visually verifying its rendered page is made in this audit.
2. [Ha–Paugam, arXiv:math/0507101v1](https://arxiv.org/pdf/math/0507101), Definitions 4.4.5 and Lemma 6.2.1, printed pp. 19 and 24. The Gibbs-state result is stated for a summable BCM pair, an invertible point, and a convergent partition function. This verifies a material hypothesis omission in A0618.

## 1. Exact arithmetic criterion and test-function calculations

### 1.1 The sign correction is mathematically material

At **2001–2023**, A0618 gives the source criterion

\[
\mathrm{RH}\iff W(g*g^*)\leq0\quad(g\in\mathscr T),
\qquad W=\sum_vW_v.
\]

Thus the sign required to contradict this criterion is \(W(g*g^*)>0\). At **2231–2239**, the assistant explicitly identifies the earlier numerical quantity as

\[
Q_{\mathrm{previous}}(g)=-W(g*g^*).
\]

Consequently a positive value of that earlier scalar is a negative value of the source scalar. This is an exact sign reversal, not a counterexample and not a discretionary replacement of notation. This assigned portion records the correction; it does not reproduce the earlier numerical code, so the claim about that code's actual implementation must also be checked against its own source elsewhere.

### 1.2 Involution, transform, and admissibility checks

Definitions appear at **2029–2078**. They fix

\[
(g_1*g_2)(x)=\int_0^\infty g_1(y)g_2(x/y)\frac{dy}{y},\quad
g^*(x)=\overline{g(x^{-1})},\quad
\widehat g(s)=\int_0^\infty g(x)x^{-is}\frac{dx}{x}.
\]

With precisely this exponent,

\[
\widehat g(i/2)=\int_0^\infty g(x)x^{1/2}\frac{dx}{x},\qquad
\widehat g(-i/2)=\int_0^\infty g(x)x^{-1/2}\frac{dx}{x}.
\]

The two displayed moment conditions are therefore correct. Substitution \(y=x^{-1}\), with the reversal of endpoints included, gives

\[
\begin{aligned}
\widehat{g^*}(s)
&=\int_0^\infty\overline{g(x^{-1})}x^{-is}\frac{dx}{x}\\
&=\int_0^\infty\overline{g(y)}y^{is}\frac{dy}{y}
=\overline{\widehat g(\bar s)}.
\end{aligned}
\]

Compact support justifies interchanging the integrals in the convolution transform, so

\[
\widehat{g*g^*}(s)=\widehat g(s)\overline{\widehat g(\bar s)}.
\]

This proves **2080–2092**, including its restriction of the absolute-square identity to real \(s\). That restriction does not assume that the nontrivial zeta zeros have real \(s\)-coordinates. In particular it does not replace the value at a nonreal zero by an absolute square.

The map \(g\mapsto g*g^*\) is quadratic over real scalars and satisfies \(f_{cg}=|c|^2f_g\); it is not complex-linear. A0618 explicitly recognizes this at **2080**.

### 1.3 The finite-prime reduction and the real-valued scalar

At **2094–2116**, the actual local functionals are displayed, including the archimedean subtraction. If \(\operatorname{supp}g\subset[a,b]\), a nonzero integrand in \((g*g^*)(x)\) requires both \(y\in[a,b]\) and \(y/x\in[a,b]\). Hence \(a/b\leq x\leq b/a\). This proves **2118–2124**.

For \(p>b/a\) and \(m\geq1\), both \(p^m>b/a\) and \(p^{-m}<a/b\), so both evaluations in \(W_p\) vanish. For any fixed prime only finitely many powers can contribute. Including the archimedean place and every prime at most \(b/a\) is therefore sufficient, without approximation.

For \(f=g*g^*\), the involution identity \(f^*=f\) gives \(f(x^{-1})=\overline{f(x)}\), and

\[
f(1)=\int_0^\infty |g(y)|^2\frac{dy}{y}\geq0.
\]

Every prime term and the archimedean term are consequently real. The inequality applied to their sum is well typed. The archimedean integral exists: its numerator vanishes at \(x=1\), canceling the first-order zero of \(x-x^{-1}\); outside the supports of \(f(x)\) and \(f(x^{-1})\), its integrand is exactly

\[
-\frac{2f(1)}{x-x^{-1}}\frac{dx}{x},
\]

which is integrable at infinity. No subtraction or sign has been discarded in this check.

### 1.4 The trace arrow is cited, not completely constructed in this excerpt

At **2128–2175**, A0618 introduces \(\mathscr H_S\), the multiplier \(u_S\), and the projection \(P_S\) by reference to the source calculus. It does not give the exact local multiplier formulas or an independent definition of the projection, and it does not prove trace-class membership. Its statement at **2163** explicitly limits the arrow to the domain of a cited trace theorem.

Thus the displayed operator-to-arithmetic equality is a cited theorem application, with its factor \(1/2\) retained. It is not a standalone construction and proof of the entire analytic morphism in these lines. The diagram at **2146–2160** should not be read as extending the trace-class arrow to arbitrary entire functions, or beyond the source theorem's actual domain. There is no basis here to conclude that the cited trace theorem is false.

### 1.5 The block calculation is correct, and compactness does not determine the sign

Use the exact order of summands at **2179–2187**:

\[
\mathscr H_S=(I-P_S)\mathscr H_S\oplus P_S\mathscr H_S,
\quad P_S=\begin{pmatrix}0&0\\0&I\end{pmatrix},
\quad U_S=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
\]

Direct multiplication gives

\[
\begin{aligned}
\frac12U_S^*[2P_S-I,U_S]
&=U_S^*P_SU_S-P_S\\
&=\begin{pmatrix}C^*C&C^*D\\D^*C&D^*D-I\end{pmatrix}.
\end{aligned}
\]

The lower-right block of \(U_S^*U_S=I\) is \(B^*B+D^*D=I\). Therefore, with the usual compatible inner-product convention, the quadratic form is exactly

\[
\|Cx\|^2+2\operatorname{Re}\langle Cx,Dy\rangle-\|By\|^2.
\]

This verifies **2192–2227**. If \(C=0\), the operator is negative semidefinite. The appropriate positive multiplier can then yield a nonpositive trace when the source trace-class hypotheses justify the trace pairing. Neither the unitary matrix calculation nor the multiplier is a freely chosen sign convention.

The actual source property cited at **2229** is only triangularity modulo compact operators. That does not imply negativity. For example, on \(\mathbb C\oplus\mathbb C\), take

\[
P=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
U=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Here \(C=1\) is compact, yet \(U^*PU-P=\operatorname{diag}(1,-1)\), whose value on \((1,0)\) is positive. Even its trace weighted by the positive matrix \(\operatorname{diag}(1,0)\) is positive. This elementary example is an obstruction to inferring an operator sign from compactness. It is **not** an arithmetic counterexample: it does not identify that matrix weight with one of the actual multipliers \(M_{|\widehat g|^2}\), nor that unitary with \(U_S\).

## 2. The BC state at beta one is actually constructed

### 2.1 Groupoid operations

The source and target at **2245–2266** force the intermediate point \(r\rho\) in convolution. An arrow \((r,\rho)\) followed by \((gr^{-1},r\rho)\) has product \((g,\rho)\); this proves the formula at **2268–2281**. The inverse arrow is \((r^{-1},r\rho)\), proving the involution formula as well. Since \((qr)^{it}=q^{it}r^{it}\), the time evolution is compatible with convolution, and its compatibility with involution follows from \((r^{-1})^{it}=\overline{r^{it}}\) for real \(t\).

This verifies the composability correction discussed at **2350**. The allegation of a misprint in the named book page is a provenance claim not independently checked here; the correct groupoid formula follows directly from the displayed source and target, regardless of that allegation.

### 2.2 Haar measure and the KMS sign

At **2285–2348**, the functional is

\[
\varphi(f)=\int_{\widehat{\mathbb Z}}f(1,\rho)\,d\mu(\rho).
\]

To verify the exact measure factor at **2324–2346**, write \(r=a/b\) in lowest positive terms. Then

\[
\Omega_r=b\widehat{\mathbb Z},\quad
r\Omega_r=a\widehat{\mathbb Z}=\Omega_{r^{-1}},\quad
\mu(\Omega_r)=1/b,\quad\mu(r\Omega_r)=1/a.
\]

The multiplication map is an isomorphism between these compact additive groups. Haar uniqueness and these total masses give, for measurable \(E\subset\Omega_r\),

\[
\mu(rE)=r^{-1}\mu(E).
\]

Thus under \(\eta=r\rho\) one has \(d\mu(\rho)=r\,d\mu(\eta)\). After setting \(q=r^{-1}\), this is precisely \(q^{-1}d\mu(\eta)\), the factor in **2339–2340**. The transformed integrand is

\[
f_2(q^{-1},q\eta)\,q^{-1}f_1(q,\eta),
\]

which is the integrand of \(\varphi(f_2*\sigma_i(f_1))\), since \(q^{i i}=q^{-1}\). The KMS sign and ordering are correct.

For positivity, the unit value of \(f^**f\) is

\[
(f^**f)(1,\rho)=\sum_{r:\,r\rho\in\widehat{\mathbb Z}}|f(r,\rho)|^2,
\]

which proves **2313–2320**. The identity function on the compact unit space has \(\varphi(1)=1\). For the reduced groupoid norm, evaluation \(f(1,\rho)\) is a matrix coefficient of the regular representation at the unit arrow, so \(|f(1,\rho)|\leq\|f\|\). Integration is therefore bounded. This supplies the extension to a state; it also pulls back along the full-to-reduced quotient if the full completion is used. Compactly supported functions have finite support in the discrete rational-arrow coordinate, making them entire analytic under multiplication by \(r^{iz}\). The dense analytic KMS calculation therefore yields the stated state.

No zeta-zero or RH assumption enters these computations. A0618's claim of RH-independent existence at **2348** is justified. It does not assert a trace-class Gibbs representation at \(\beta=1\).

## 3. Shimura formalism: correct intertwining, one material domain omission

### 3.1 The partial action and determinant

The data and partial action are at **2354–2404**. For composable \(h,g\), applying \(g\) then \(h\) gives

\[
(\phi(hg)\rho,[z,lg^{-1}h^{-1}])
=(\phi(hg)\rho,[z,l(hg)^{-1}]),
\]

so the claimed formula is a left action on its domain. The quotient action preserves the relevant source and target classes. The qualification at **2404** retains the difference between an ordinary groupoid and the quotient stack; it does not supply the full stack-level algebra construction by itself.

The determinant formula at **2408–2424** is multiplicative because each valuation of a determinant is additive. Only finitely many valuations are nonzero for an invertible finite adelic matrix. The level inclusion \(\phi(K)\subset K_M^\times\subset\operatorname{GL}(L\otimes\widehat{\mathbb Z})\) forces determinant valuations zero on \(K\). Hence the map descends to the displayed double-coset set. Its sign and reciprocal have not been changed.

The diagonal real operator at **2443–2459** has the correct self-adjoint multiplication-operator domain. Because \(d_\phi(gh^{-1})=d_\phi(g)d_\phi(h)^{-1}\), the calculation at **2467–2496** proves the stated time-evolution intertwining. It does not require positivity of \(H_y\), and it does not prove trace-classness of \(e^{-\beta H_y}\).

### 3.2 The Gibbs expression needs its actual domain

At **2498–2528**, the multiplicity \(m_K\) is retained correctly: if the relevant trace is finite, then

\[
m_K\zeta_y(\beta)=\operatorname{Tr}(e^{-\beta H_y}),
\]

and the displayed functional takes the value one on the identity. Replacing both numerator and denominator by the same virtual-trace factor leaves that ratio unchanged.

However, A0618 has introduced arbitrary \(y\) at **2426–2432**, and gives the Gibbs functional without a convergence hypothesis. This is not valid for every such \(y\). In its own multiplicative datum (**2532–2542**), choose \(\rho=0\). Then every finite idele is in \(G_y\), and

\[
K\backslash G_y=\widehat{\mathbb Z}^{\times}\backslash\mathbb A_f^{\times}
\cong\mathbb Q_{>0}^{\times}.
\]

On the basis indexed by positive rationals,

\[
H_y\delta_r=(\log r)\delta_r,\qquad
e^{-\beta H_y}\delta_{1/n}=n^\beta\delta_{1/n}.
\]

For every \(\beta>0\), this operator is unbounded; in particular it is not trace class. Dividing its trace expression by its partition function cannot produce the displayed Gibbs state. Even at an invertible rank-one point, the ordinary trace \(\sum_{n\geq1}n^{-\beta}\) diverges at \(\beta=1\).

The primary-source hypothesis check cited in the provenance section confirms that the low-temperature Gibbs result was stated with precisely a convergence regime and invertible point. The general partition-function definition may take the value infinity; the normalized Gibbs functional cannot. This is a concrete missing-domain defect in **2515–2528**, not a defect in the independent Haar construction of the BC \(\mathrm{KMS}_1\) state.

### 3.3 The rank-one identification is a real exact map

The arrow at **2544–2578** preserves source, target, composition, and the same time parameter, as claimed. The equality \([1,r^{-1}]=[1,1]\) uses the positive rational element of the diagonal \(\mathbb Q^\times\)-action; its positivity leaves the \(\{\pm1\}\)-coordinate equal to \(1\). Also

\[
d_\phi(r)=\prod_pp^{v_p(r)}=r
\]

for positive rational \(r\). Thus no reversal of time occurs.

A0618 cites, rather than proves, bijectivity. It can be checked directly in this datum. Every finite idele has a unique factorization \(l=a u\), with \(a\in\mathbb Q_{>0}^{\times}\), \(u\in\widehat{\mathbb Z}^{\times}\). Its Shimura class can be written uniquely as \([1,u]\). The \(K\)-action sends the object \((\rho,[1,u])\) to \((u\rho,[1,1])\). For an arrow with \(g=r v\), \(r\) positive rational and \(v\) a profinite unit, the change of source representative uses \(k_2=u\), while the change of target representative uses \(k_1=u v^{-1}\). Its transformed group component is

\[
k_1gk_2^{-1}=(u v^{-1})(r v)u^{-1}=r.
\]

It is exactly the image of the unique BC arrow \((r,u\rho)\). This establishes the representative-level inverse and proves that the identification does not identify every higher-rank Shimura BCM system with rank one.

## 4. Cooling and distillation: the exact quotient calculation has limited scope

### 4.1 Scaling shifts the implementing Hamiltonian, not beta

At **2580–2642**, the asserted cooling representation is on a specified trace-class subalgebra and a field of operator spaces. A0618 explicitly retains the possible bundle obstruction at **2605–2614**; it does not prove the general cooling construction within the excerpt.

The intertwining calculation itself is exact. Since the scalar operator commutes with \(H\),

\[
e^{it(H+(\log\lambda)I)}
=e^{it\log\lambda}e^{itH}=\lambda^{it}e^{itH}.
\]

Substitution into the integrated representation proves

\[
\Pi_{\epsilon,H}(\theta_\lambda X)
=\Pi_{\epsilon,H+(\log\lambda)I}(X).
\]

The sign is plus, and \(\beta\) is fixed. This calculation is not a heat-loss differential equation, a finite-rate cooling law, or a statement about a finite-time thermal catastrophe.

### 4.2 The cyclic-module notation hides a construction that cannot be ordinary functoriality of scalar trace

At **2644–2655**, A0618 writes

\[
\delta_\beta=(\operatorname{Tr}\circ\Pi)^\natural:
\widehat{\mathcal A}_{\beta,\tau}^\natural
\longrightarrow\mathscr S^\natural(\widetilde\Omega_\beta).
\]

The scalar trace is not an algebra homomorphism. For the matrix units \(E_{11},E_{22}\in M_2(\mathbb C)\),

\[
\operatorname{Tr}(E_{11}E_{22})=0,
\qquad\operatorname{Tr}(E_{11})\operatorname{Tr}(E_{22})=1.
\]

Consequently the notation cannot mean simply applying the usual algebra-to-cyclic-module functor to the scalar trace. A generalized trace on cyclic chains, together with the source's domain and decay conditions, can be the intended cited construction. For finite matrix algebras its degree-\(n\) map involves the sum

\[
A_0\otimes\cdots\otimes A_n\longmapsto
\sum_{i_0,\ldots,i_n}
(A_0)_{i_0i_1}\otimes(A_1)_{i_1i_2}
\otimes\cdots\otimes(A_n)_{i_ni_0},
\]

rather than applying scalar trace independently in each tensor factor. The trace-class field version also requires its analytic convergence and target conditions. A0618 does not display those higher-degree maps or establish those conditions. This is a precise omitted construction / potentially misleading notation, not a disproof of the cited cyclic cooling theory.

### 4.3 What the quotient argument proves

For any genuine degree-zero map \(\delta_{\beta,0}:A\to B\), let \(q_\beta:B\to B/\operatorname{im}\delta_{\beta,0}\) be its cokernel projection. For every \(a\in A\), the class of \(\delta_{\beta,0}(a)\) is zero by the definition of the quotient. Hence **2659–2679** correctly proves

\[
q_\beta\delta_{\beta,0}J=0
\]

for every map \(J\) of the specified type. The same annihilation holds if a topological quotient by the closed image is used.

It proves annihilation for that **particular factorization**. It does not prove that every NS-to-arithmetic map factors in this way, and it does not prove that NS data have no arithmetic relation. A0618 does not claim either universal conclusion. The map \(\mathcal I\) and nonzero quotient condition at **2681–2692** are a desired alternative construction, not a construction carried out. The need for a further sign-bearing pairing at **2694** is correctly acknowledged. A nonzero quotient class alone is not an RH counterexample.

Moreover, this is a chosen route through cooling/distillation, not a proof that every possible disproof of the source arithmetic criterion must use this route. At this point the admissible-test space \(\mathscr T\), the target \(\mathscr S(\widetilde\Omega_\beta)\), and any pairing on its quotient have not been connected by an explicit additional map in the excerpt.

## 5. The NS observation map is actually defined and admissible, but no transport of dynamics is proved

### 5.1 Exact admissibility proof

The unaveraged angular-momentum integral at **2702–2711** retains its factor \(r\) and full integral over \([0,2\pi]\). With the cutoff hypothesis at **2713**, \(b(r,t)=\chi(r,t)a_u(r,t)\) is smooth and compactly supported away from \(r=0\), with support locally uniform in \(t\). Therefore

\[
g_t=(D_r^2-1/4)b(\cdot,t),\quad D_r=r\partial_r,
\]

is a smooth test-function-valued family. For any fixed real \(s\), compact support gives

\[
\int_0^\infty(D_rb)(r)r^s\frac{dr}{r}
=-s\int_0^\infty b(r)r^s\frac{dr}{r},
\]

and a second integration by parts gives the factor \(s^2\). Taking \(s=1/2\) and \(s=-1/2\) proves the two required moments vanish. This proves **2715–2747** exactly with the coefficient \(-1/4\).

The expansion at **2749–2758** is the product rule, including both cutoff derivatives. Since \(D_r\) is independent of \(t\), the derivative at **2760–2767** is also exact. Inserting the given NS equation under the angular integral proves **2769–2785** whenever the source fields are smooth enough there; its viscosity, convective, pressure, and force signs are retained.

Thus **2787–2795** really defines a scalar-valued observation of a smooth preterminal solution at each \(t<1\). It does not prove a finite endpoint value or a controlled limiting test function at \(t=1\). The interval explicitly excludes that endpoint, and the support hypothesis is only locally uniform on preterminal compact intervals.

### 5.2 Why a differentiated observation is not yet a dynamics intertwiner

The derivative formula still contains the full fields \(u,p,f\) and \(\chi\); it does not give a closed arithmetic evolution for \(g_t\), prove \(\mathcal T_\chi\) equivariant for a specified target dynamics, identify its cooling class, or determine the sign of \(W(g_t*g_t^*)\). A0618 explicitly says all of this at **2797–2817**. These are accurate limits on what it has proved, although listing the future tasks does not answer U0013's requested physical identification.

The kinematic flexibility can be tested exactly without changing any given source solution. For a real admissible test \(g\), define

\[
b(r)=r^{1/2}\int_0^r y^{-1/2}g(y)\frac{dy}{y}
-r^{-1/2}\int_0^r y^{1/2}g(y)\frac{dy}{y}.
\]

Below the support of \(g\), both integrals vanish. Above it, both vanish by the two admissibility moments. Hence \(b\) is smooth and compactly supported away from zero. Differentiating gives

\[
D_rb=\frac12r^{1/2}\int_0^r y^{-1/2}g(y)\frac{dy}{y}
+\frac12r^{-1/2}\int_0^r y^{1/2}g(y)\frac{dy}{y},
\]

and then \(D_r^2b=b/4+g\). Thus \((D_r^2-1/4)b=g\) exactly.

Choose a cutoff \(\chi\) equal to one on \(\operatorname{supp}b\), and a smooth compactly supported function \(\eta(z)\) with \(\eta(0)=1\). The velocity

\[
u(x,y,z)=\frac{b(r)\eta(z)}{2\pi r^2}(-y,x,0),\qquad r=\sqrt{x^2+y^2},
\]

extends by zero near \(r=0\), is smooth, and has zero divergence. Indeed the two nonzero divergence terms are \(-y\partial_x F+x\partial_y F=0\) for the radial coefficient \(F=b(r)\eta(z)/(2\pi r^2)\). On \(z=0\), its angular integral is exactly \(a_u(r)=b(r)\). Consequently \(\mathcal T_\chi(u)=g\).

If one is free to choose a smooth stationary forced NS problem, setting \(p=0\) and \(f=(u\cdot\nabla)u-\nu\Delta u\) makes this field solve the displayed NS equation with its original viscosity symbol. This proves that arbitrary real admissible tests can be realized by suitable such kinematic/forced data and cutoffs. It does **not** identify the source's particular force, pulses, or singular solution with these constructed ones. It demonstrates precisely why mere test-function realization cannot supply the missing statement about that particular dynamics or its RH sign.

## 6. Physical-chain status at the boundary of this assignment

U0014 at **2829** proposes, under an explicit provisional assumption, the chain: modular/thermal time; uniformly accelerated-observer and Unruh/KMS descriptions; an arithmetic thermal spectrum; a localized runaway with a possible black-hole or anomaly interpretation. It also proposes treating every entangling massive object as an observer and associating a Rindler horizon with it. Those are the user's research proposals in this turn, not theorems established by A0618.

No observable-algebra identification with a relativistic quantum field theory, Lorentz boost generator, acceleration, stress tensor, spacetime metric, Einstein equation, curvature invariant, horizon, detector response, or mass observable is defined or computed within **1995–2838**. In particular neither the name “cooling” nor the exact \(+\log\lambda\) shift supplies a rate of energy removal in a three-dimensional physical evolution.

At **2833** A0626 proposes checking freely falling measurements; at **2837** A0638 proposes comparison with black-hole mass inflation. These statements are prospective. This bounded record contains no mass-inflation or gravitational-backreaction calculation to validate or invalidate. It must not be credited with an established physical particle/singularity identification, and it must not be treated as proving that the proposed physical relation is impossible.

## Audit disposition and exact pins

| Item | Source pins | Disposition |
|---|---:|---|
| Source RH sign and correction of prior numerical scalar | 2001–2023; 2231–2239 | Sign relation exact; earlier implementation not reproduced here |
| Involution, Fourier/Mellin exponent, two moments | 2029–2092 | Directly verified |
| Prime support reduction and local functional | 2094–2124 | Directly verified, without approximation |
| Trace-class/operator equality | 2128–2175 | Cited analytic construction; exact domain and operators not fully constructed here |
| Projection block and cross term | 2179–2229 | Directly verified; compactness alone gives no required sign |
| Haar \(\mathrm{KMS}_1\) state | 2241–2350 | Actual RH-independent construction; exact measure and analytic KMS signs check |
| General BCM action and Hamiltonian intertwining | 2354–2496 | Algebraic calculations check; full stack/C*-construction cited |
| Level multiplicity and Gibbs state | 2498–2528 | Multiplicity retained; convergence/invertibility regime omitted in Gibbs assertion |
| Rank-one BC–Shimura isomorphism | 2530–2578 | Actual exact relation; inverse representative calculation supplied above |
| Cooling dual scaling | 2580–2642 | \(H\mapsto H+(\log\lambda)I\) at fixed beta checks |
| Cyclic trace morphism | 2644–2655 | Intended external generalized-trace construction; scalar trace is not an algebra homomorphism |
| Cokernel annihilation | 2659–2694 | Exact only for specified factorization; alternative surviving map unconstructed |
| NS-to-admissible-test map | 2700–2795 | Actual kinematic map and moment proof; no endpoint/dynamics/cooling/sign theorem |
| Admitted outstanding arithmetic assertions | 2797–2817 | Explicitly unproved in A0618 |
| Physical research request and initial responses | 2819–2837 | User's provisional programme; responses here contain intentions only |
