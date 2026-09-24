# An explicit global object in the original-zeta dual cokernel

24 September 2026. Complete derivation PGD0–PGD7. This continuation constructs a nonzero rational-function line in the actual algebraic comparison cokernel. It also constructs its entire representatives and exact maps. It does not identify that cokernel with a space of RH counterexamples.

## PGD0. Why this is the next calculation, and which operations are present

The amended instruction USR-64a88219a3ecddd3 asks what would advance the target using the current finding and everything already known, and then asks us to attempt that calculation. ASD14 constructed the actual dual-comparison cone. SCL and DPL then proved that its degree-one cokernel has no nonzero polynomial-annihilated vector. The next question was whether anything actually remains in that cokernel. This note answers it by constructing a global element, rather than assuming nonvanishing or replacing the quotient by its zero Hausdorffization.

The controlling source is the complete preserved user corpus, in particular USR-4322be19bff532cd, the global arguments USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2 and USR-6152e3bc6302258c, and B1–B5/P1–P5 with retraction R1 in [the source operations](../foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md). The notation remains \(Z_0\) for absence, \(Z_1/\tau\) for primitive presence without parity or source addition, and \(Z_2\) for the supplied integer parity data. Integer amounts are retained. The constant arithmetic function \(1\) below comes from the already reconstructed arithmetic layer; it is not primitive \(\tau\). No multiplication, addition, division or derivative below has primitive \(\tau\) as an operand.

The receiving spaces, contour map, topologies and operation prerequisites are constructed in [GZR0–GZR9](GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md), [SCL0–SCL9](SPECTRAL_COKERNEL_DIVISIBILITY_AND_FINITE_LIFTING.md), and [DPL0–DPL8](DUALITY_COKERNEL_POLYNOMIAL_LIFTING_INDEPENDENT.md). The full source-faithful comparison is [ASD14](ACTUAL_SUPPORTED_DUALITY_INDEPENDENT.md). All its other cohomology groups and extra closed copies remain present. This note concerns the named receiving cokernel, not an impossibility for the user's source.

Human provenance is Alain Connes and Caterina Consani, [*Schemes over F1 and zeta functions*, arXiv:0903.2024v3 §5](https://arxiv.org/abs/0903.2024v3), for the actual coefficient geometry; Ralf Meyer, [*A spectral interpretation for the zeros of the Riemann zeta function*, math/0412277v3](https://arxiv.org/abs/math/0412277v3), for the analytic framework, with the stronger original-space image theorem proved in OMS; and Pierre Deligne, [*La conjecture de Weil II*, §§3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/), for the target weight-separated lifting argument. Hadamard's full factorization is retained in GZR1/S2, with the indexed original [Connes treatment](https://arxiv.org/abs/2602.04022v1), author TeX `rhready.tex`, lines526–535. The elementary new maps below are proved here, rather than attributed to those authors.

## PGD1. Construct the larger multiplier domain and the exact contour map

Retain the actual Fréchet space
\[
\mathcal B=\{F\text{ entire}:b_{A,N}(F)=
\sup_{|\sigma|\le A,t\in\mathbb R}(1+|t|)^N|F(\sigma+it)|<\infty
\quad\text{for every }A,N\ge0\}.
\]
Let \(\mathscr Z\) be the actual nontrivial zero set of the original \(\zeta\), with multiplicities \(m_\rho\), and retain
\[
I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\ (\rho\in\mathscr Z,\ 0\le j<m_\rho)\},\qquad Q=\mathcal B/I.
\tag{PGD1.1}
\]
This is the original quotient, with its already proved Mellin comparison and quotient topology. It is not an unrestricted product of jets.

Define the receiving multiplier algebra
\[
\mathcal M=\{H\text{ entire}: \text{for each }A\ge0\text{ there are }C_A>0,d_A\ge0
\text{ with } |H(\sigma+it)|\le C_A(1+|t|)^{d_A}
\text{ whenever }|\sigma|\le A\}.
\tag{PGD1.2}
\]
Here \(d_A\) can be taken an integer. Addition and multiplication preserve this domain: use the maximum and the sum of the two growth exponents, respectively. It contains \(\mathcal B\), every polynomial, and \(r^s=\exp(s\log r)\) for each positive real \(r\). Multiplication by a fixed \(H\in\mathcal M\) sends \(\mathcal B\) continuously to itself, since
\[
b_{A,N}(HF)\le C_A b_{A,N+d_A}(F).
\tag{PGD1.3}
\]
All quotients of \(\mathcal M\) below are algebraic unless explicitly stated otherwise. No unconstructed topology on this union of growth classes is used.

For \(H\in\mathcal M\), define a functional on the original quotient by
\[
\lambda_H([F])=\frac1{2\pi i}
\left(\int_{2-i\infty}^{2+i\infty}-\int_{-1-i\infty}^{-1+i\infty}\right)
\frac{H(s)F(1-s)}{\zeta(s)}\,ds.
\tag{PGD1.4}
\]
Both edges are oriented upward; the integrals are taken separately before subtraction. The denominator is the original \(\zeta\).

Choose \(C,d\) bounding \(H\) on the strip \(-2\le\Re s\le2\). The exact edge estimates proved in GZR2 are
\[
|1/\zeta(2+it)|\le\zeta(2),\qquad
|1/\zeta(-1+it)|\le4\pi^2\zeta(2)(1+|t|)^{-3/2}.
\]
Consequently both integrals converge absolutely and
\[
|\lambda_H([F])|\le
\frac{C\zeta(2)(1+4\pi^2)}{\pi}\,b_{2,d+2}(F).
\tag{PGD1.5}
\]
Indeed each edge is bounded using \((1+|t|)^{-2}\), whose integral over the real line is exactly2. These estimates retain the constants of the original contour.

To prove descent, let \(F\in I\). Reflection preserves all original zero multiplicities. Thus \(H(s)F(1-s)\in\mathcal B\) by PGD1.3 and reflection, and it belongs to \(I\). The actual OMS/SSI division theorem says that its quotient by \(\zeta\) is holomorphic in a neighborhood of the closed strip \(-1\le\Re s\le2\) and rapidly decreasing there. The horizontal sides of its rectangles therefore tend to zero. Cauchy's theorem gives equality of its two vertical integrals, proving \(\lambda_H(F)=0\). Taking the infimum in PGD1.5 over representatives proves continuity on the actual \(Q\). Hence \(\lambda_H\in Q'\), the continuous complex-linear dual, without replacing it by an algebraic dual.

The original endpoint behavior is unchanged: \(\zeta(0)=-1/2\), while \(1/\zeta\) has a zero at1. No pole is introduced at either endpoint in PGD1.4. The trivial zeros \(-2,-4,\ldots\) remain outside the two stated edges. They have not been deleted from the source formula or enclosed by a replacement contour.

## PGD2. Every full jet is detected, and the kernel is calculated exactly

For each \(a\in\mathscr Z\), retain the actual global isolators \(E_{a,j}\in\mathcal B\) from GZR5/SCL1, for \(0\le j<m_a\). They have the prescribed monomial jet at \(a\) and every required jet zero at every other actual zero. Their construction retains the entire auxiliary source transform
\[
F_*(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
F_*(0)=F_*(1)=\frac18,
\]
\[
F_*(-2r)=\frac{(1+2r)2r}{8}\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0.
\tag{PGD2.1}
\]
This auxiliary function is not substituted for the denominator of PGD1.4.

Put \(b=1-a\), \(m=m_a=m_b\), and write the original germ
\[
\zeta(b+t)=t^m u_b(t),\qquad
u_b(t)=\sum_{k\ge0}\frac{\zeta^{(m+k)}(b)}{(m+k)!}t^k,
\qquad u_b(0)\ne0.
\]
Then
\[
\boxed{\lambda_H([E_{a,j}])=(-1)^j
[t^{m-1-j}]\frac{H(b+t)}{u_b(t)}.}
\tag{PGD2.2}
\]
For its global justification, the numerator \(H(s)E_{a,j}(1-s)\) belongs to \(\mathcal B\) by PGD1.3. Its quotient by the original \(\zeta\) has only the possible pole at \(b\). GZR5's finite-pole contour theorem applies to this numerator: multiplying out its finitely many possible poles puts the numerator in \(I\), and OMS rapid division kills the horizontal edges. Its residue is precisely PGD2.2. Thus no infinite formal residue sum has been substituted for the actual contour.

Define
\[
\mathcal J=\{H\in\mathcal M:H^{(j)}(\rho)=0
\ (\rho\in\mathscr Z,\ 0\le j<m_\rho)\}.
\tag{PGD2.3}
\]
If \(\lambda_H=0\), PGD2.2 vanishes for every \(j=0,\ldots,m-1\). These equations give every Taylor coefficient of \(H(b+t)/u_b(t)\) through degree \(m-1\), in reverse order with the stated signs. They are all zero. Since \(u_b(0)\ne0\), every corresponding coefficient of \(H\) is zero. Reflection permutes the actual zero set, so \(H\in\mathcal J\).

Conversely, if \(H\in\mathcal J\), then for every \(F\in\mathcal B\) the product \(H(s)F(1-s)\) lies in \(I\). The same exact rapid-division argument as in PGD1 proves \(\lambda_H(F)=0\). We have proved
\[
\boxed{\ker(H\mapsto\lambda_H)=\mathcal J.}
\tag{PGD2.4}
\]
Every multiplicity is retained in both directions.

## PGD3. The full multiplier quotient maps injectively into the actual cone

Write \(D=\mathcal D_L\), so that for \(F\in\mathcal B\), \(\lambda_F=D[F]\) by the original definition. Set
\[
Y=\chi\otimes Q',\quad (T_r^\diamond\lambda)(x)=r\lambda(T_{r^{-1}}x),
\quad G=1-L^t,\quad
\mathcal C_\zeta=Y/DQ.
\tag{PGD3.1}
\]
This is the degree-one cokernel of ASD14 with its exact twist, not a new unspecified obstruction.

Since \(I=\mathcal B\cap\mathcal J\), there is a commutative diagram of exact algebraic rows
\[
\begin{array}{ccccccccc}
0&\longrightarrow&Q&\longrightarrow&\mathcal M/\mathcal J
&\longrightarrow&\mathcal M/(\mathcal B+\mathcal J)&\longrightarrow&0\\
&&\Vert&&\downarrow\Theta&&\downarrow\overline\Theta&&\\
0&\longrightarrow&Q&\xrightarrow{D}&Y
&\longrightarrow&\mathcal C_\zeta&\longrightarrow&0,
\end{array}
\tag{PGD3.2}
\]
where \(\Theta[H]=\lambda_H\) and \(\overline\Theta[H]=[\lambda_H]\). Both vertical maps are injective. For the middle map this is PGD2.4. For the right map, its kernel means \(\lambda_H=D[F]=\lambda_F\) for some \(F\in\mathcal B\). PGD2.4 gives \(H-F\in\mathcal J\), exactly \(H\in\mathcal B+\mathcal J\). This proves the asserted kernel and hence injectivity. Exactness of the upper row follows directly from the two stated subspace quotients; exactness of the lower row is its actual image quotient. No surjectivity of \(\Theta\) onto the full dual is claimed.

The generator and full real action are exact:
\[
G\lambda_H=\lambda_{sH},\qquad
T_r^\diamond\lambda_H=\lambda_{r^sH}\quad(r>0).
\tag{PGD3.3}
\]
For the first, the integrand for \(\lambda_H-\lambda_H\circ L\) contains
\(H(s)(1-(1-s))F(1-s)=sH(s)F(1-s)\).
For the second, the factor is exactly
\(r\,r^{-(1-s)}=r^s\).
The growth domains proved in PGD1 justify each resulting integral. Multiplication by \(s\) and \(r^s\) preserves \(\mathcal B,\mathcal J\) and \(\mathcal M\), so these identities descend through every map in PGD3.2. They apply at every original prime \(r=p\). No infinite-dimensional exponential has been inferred from a generator identity.

## PGD4. A nonzero constant class and all polynomial classes

There are infinitely many actual nontrivial zeros with unbounded imaginary part. Here is the needed argument from the retained full factors, without a numerical RH assumption. The complete Hadamard formula GZR1/S2 is
\[
F_*(s)=\frac18 e^{b_0s}
\prod_{\rho\in\mathscr Z}\left(1-\frac{s}{\rho}\right)^{m_\rho}
e^{m_\rho s/\rho},\qquad
b_0=\frac12\log(4\pi)-1-\frac\gamma2.
\tag{PGD4.1}
\]
If it had only finitely many zeros, for positive real \(\sigma\) this formula would give
\[
\log|F_*(\sigma)|\le-\log8+
\sigma\left(|b_0|+\sum_\rho m_\rho/|\rho|\right)
+\sum_\rho m_\rho\log(1+\sigma/|\rho|).
\tag{PGD4.2}
\]
The sums here are finite under the assumption being tested.

On the other hand, the exact original formula on \(\sigma>1\) is
\[
F_*(\sigma)=\frac{\sigma(\sigma-1)}8\pi^{-\sigma/2}
\Gamma(\sigma/2)\zeta(\sigma)>0.
\]
For \(x\ge2\), Euler's defining Gamma integral gives the elementary bound
\[
\Gamma(x)=\int_0^\infty v^{x-1}e^{-v}\,dv
\ge\int_x^{x+1}x^{x-1}e^{-x-1}\,dv
=x^{x-1}e^{-x-1}.
\]
The original Dirichlet series gives \(\zeta(\sigma)\ge1\). Thus for \(\sigma\ge4\), with all original factors retained,
\[
\log F_*(\sigma)\ge
\log\frac{\sigma(\sigma-1)}8-\frac\sigma2\log\pi
+\left(\frac\sigma2-1\right)\log\frac\sigma2-\frac\sigma2-1.
\tag{PGD4.3}
\]
After dividing the bounds by \(\sigma\log\sigma\), the right side of PGD4.2 tends to0 and the right side of PGD4.3 tends to \(1/2\). This contradicts the two inequalities for the same function. Hence the zero set is infinite. Its zeros lie in the retained bounded critical strip, and an entire nonzero function has only finitely many zeros in each compact set. Their imaginary parts must therefore be unbounded.

Now let \(P\ne0\) be any complex polynomial. If \([\lambda_P]=0\) in \(\mathcal C_\zeta\), PGD3.2 supplies \(F\in\mathcal B\) with \(P-F\in\mathcal J\). In particular
\[
F(\rho)=P(\rho)\quad(\rho\in\mathscr Z).
\tag{PGD4.4}
\]
Along a sequence of these zeros of unbounded height, the left side tends to0 by \(b_{2,1}(F)<\infty\). A nonzero constant polynomial stays nonzero. For degree \(d\ge1\), writing its leading coefficient \(p_d\ne0\), the triangle inequality gives
\(|P(z)|\ge |p_d||z|^d/2\) for all sufficiently large \(|z|\), because its finitely many lower terms have strictly smaller powers. Thus the right side cannot tend to0. This contradiction proves
\[
\boxed{P\longmapsto[\lambda_P]\text{ is an injective map }
\mathbb C[s]\longrightarrow\mathcal C_\zeta.}
\tag{PGD4.5}
\]
In particular the explicit class
\[
\boxed{c_\zeta=[\lambda_1]\ne0,\qquad
\lambda_1([F])=\frac1{2\pi i}
\left(\int_{2-i\infty}^{2+i\infty}-\int_{-1-i\infty}^{-1+i\infty}\right)
\frac{F(1-s)}{\zeta(s)}\,ds.}
\tag{PGD4.6}
\]
This is an actual nonzero global cokernel class. It is not an off-critical zero and not a numerical or parity assignment to \(\tau\).

## PGD5. Construct the rational-function line, including entire representatives

SCL5–SCL6 and DPL2–DPL3 prove that every nonzero polynomial in the actual \(G\) is bijective on \(\mathcal C_\zeta\). Therefore the exact operation
\[
\iota:\mathbb C(s)\longrightarrow\mathcal C_\zeta,\qquad
\iota(P/Q)=P(G)Q(G)^{-1}c_\zeta\quad(Q\ne0)
\tag{PGD5.1}
\]
is defined only after those inverses have been constructed. Equality of fractions gives equality of these operators by cross multiplication and the commuting inverses. This is linear over the receiving field \(\mathbb C(s)\). It is injective: if \(P/Q\ne0\), then \(P(G)\) and \(Q(G)\) are bijective, so their composition cannot send the nonzero \(c_\zeta\) to zero. In the polynomial case PGD3.3 identifies PGD5.1 with PGD4.5 exactly.

Here is an entire representative for every fraction; it keeps the correction used to remove every pole. Given \(P,Q\), let \(d=\deg Q\). For \(d=0\), set \(B_{P,Q}=0\) and \(H_{P,Q}=P/Q\). For \(d>0\), prescribe at every root \(a\) of \(Q\), through its multiplicity \(k_a\), the Taylor coefficients of the entire function \(e^{-s^2}P(s)\). There exists a unique polynomial \(T_{P,Q}\) of degree less than \(d\) with these prescribed jets. Indeed the evaluation map from polynomials of degree less than \(d\) to these \(d\) jet coordinates is injective: a kernel polynomial is divisible by every \((s-a)^{k_a}\), hence by \(Q\), and must be zero by its degree. Equal finite dimensions prove bijectivity and give its coefficients by an invertible finite linear system.

Define
\[
B_{P,Q}(s)=e^{s^2}T_{P,Q}(s),\qquad
H_{P,Q}(s)=\frac{P(s)-B_{P,Q}(s)}{Q(s)}.
\tag{PGD5.2}
\]
On each bounded vertical strip, \(|e^{s^2}|=e^{(\Re s)^2-(\Im s)^2}\), so \(B_{P,Q}\in\mathcal B\). The interpolation makes the numerator vanish through the full order of every denominator root. Thus \(H_{P,Q}\) extends to an entire function. At a root \(a\) of order \(k_a\), its value is exactly
\[
H_{P,Q}(a)=\frac{(P-B_{P,Q})^{(k_a)}(a)}{Q^{(k_a)}(a)}.
\tag{PGD5.3}
\]
Higher removable jets are obtained by the full Taylor division of the same numerator and denominator. Outside fixed disks around the finitely many roots, polynomial division and PGD1.3 bound this function by a polynomial on each vertical strip. Inside those disks it is entire and bounded on compact sets. Hence \(H_{P,Q}\in\mathcal M\).

The identity with every counterterm retained is
\[
Q(s)H_{P,Q}(s)=P(s)-B_{P,Q}(s).
\]
Applying PGD3.3 repeatedly gives
\[
Q(G)\lambda_{H_{P,Q}}=\lambda_P-D[B_{P,Q}].
\tag{PGD5.4}
\]
Taking the actual cokernel and using the proved inverse yields
\[
\boxed{[\lambda_{H_{P,Q}}]=\iota(P/Q).}
\tag{PGD5.5}
\]
This supplies actual continuous-dual representatives for the entire embedded field. Different choices of an interpolating function in \(\mathcal B\) with the same required jets would give the same class: their difference divided by \(Q\) is entire and remains in \(\mathcal B\), by fixed polynomial division and the removable local values. Thus the possible difference is explicitly a \(D(Q)\) term, not an ignored pole correction.

The full positive-real orbit also has exact representatives
\[
T_r^\diamond c_\zeta=[\lambda_{r^s}],\qquad r>0.
\tag{PGD5.6}
\]
Each is nonzero: at all actual zeros, \(|r^\rho|\) is bounded below by \(\min(1,r)>0\), whereas values of a member of \(\mathcal B\) tend to0 along unbounded heights. PGD3.2 therefore excludes its being in \(DQ\). This gives the actual prime orbit at \(r=p\), rather than assigning an unsupported eigenvalue to \(c_\zeta\). No assertion that this real orbit stays inside the particular rational-function line is needed or made.

## PGD6. Source labels and the actual cone

The source receiving-ring action on the spectral term is the same scalar action as in ASD14. It acts on every map in PGD3.2 by linearity. The full source distinction between \(\tau\) and integer1 remains on the faithful extra closed copies in the complete coefficient complex and its dual; this calculation does not remove them.

For the existing support lattice \(L_{\rm supp}\), every displayed receiving linear map has the exact lift
\[
G_{L_{\rm supp}}(f)(v,\alpha)=(f(v),\alpha),\qquad
G_{L_{\rm supp}}(V)=\{(0,\alpha):\alpha\in L_{\rm supp}\}
\cup\{(v,1_{L_{\rm supp}}):v\in V\}.
\tag{PGD6.1}
\]
If the input label is not top, its amplitude is zero and linearity sends it to zero. A nonzero output therefore has top support. Substitution proves preservation of identities and composition; injective maps remain injective. A zero amplitude retains its label. These are operations in the named receiving carrier, not on primitive \(\tau\).

ASD14 identifies \(H^1(K_\zeta)=\mathcal C_\zeta\). Therefore PGD4 proves this actual algebraic cohomology group nonzero. It does not contradict its weak-* Hausdorff quotient being zero: \(DQ\) is dense, and an algebraic quotient by a dense proper subspace need not be zero. The equality of its Hausdorff quotient with zero and the explicit nonzero class PGD4.6 are retained together, with their distinct specified categories.

SCL/DPL still prove that this nonzero group contains no nonzero generalized eigenvector of \(G\), no nonzero finite-dimensional \(G\)-invariant subspace, and no nonzero finite-dimensional equivariant quotient. Thus \(c_\zeta\) is a genuine infinite-dimensional remaining object: the vectors \(c_\zeta,Gc_\zeta,\ldots\) are linearly independent, by PGD4.5. It cannot be substituted for an undetected single zero. All original zeros, on or off the critical line, already occur in the retained finite primary spaces of \(Q\).

The other actual cone groups remain
\[
H^{-1}(K_\zeta)=H_0\oplus V_{\rm extra},\quad
H^0(K_\zeta)=0,\quad
H^2(K_\zeta)=\chi\otimes(H_0'\oplus V_{\rm extra}').
\tag{PGD6.2}
\]
No full dual-comparison isomorphism is asserted.

## PGD7. What was attempted and obtained

The preceding limitation was that weak-* density and finite-class lifting did not decide the entire algebraic cokernel. The attempted next step was to use the complete original contour with the globally present arithmetic unit, then test it against every retained multiplicity jet. PGD1–PGD4 prove that this produces an explicit nonzero class. PGD5 then answers the further question of what its whole polynomial and rational operator orbit is: an embedded copy of \(\mathbb C(s)\), with entire corrected representatives for every fraction and the full real/prime orbit separately constructed. PGD3 supplies the larger exact multiplier quotient and its injective comparison.

These calculations settle those questions on the actual global receiver. They do not prove the requested numerical separation of geometric weights. They identify precisely why deleting the dual cokernel merely because its Hausdorff quotient is zero would lose an actual object. They also retain the proved finite-class lifts, so the newly constructed class is not used as a false counterexample to those lifts or to the user's primitive source. The next geometric calculation must use the actual comparison and its retained full cone rather than replace it by a perfect pairing. The current full tau lifting goal remains active.

## Full global prime action and actual supported placement

The new complete proofs GGT0–GGT8, FPO0–FPO8 and UOS0–UOS9 (including UOS8A) strengthen the preceding global remainder calculation. The original-zeta Gaussian trace has a TlogT leading term only at the identity scale and at most order T at every other fixed positive scale. Testing a proposed finite relation against every inverse scale proves all coefficients zero. Consequently the entire finite group algebra C[R_+^×], including the Laurent algebra of all original primes, injects into the original multiplier quotient and linearly into the actual comparison cokernel. This computes relations after the actual zero-jet quotient, not only among entire functions before quotienting.

UOS constructs the full chain map into the actual dual-supported comparison cone. It sends c_r to (c_r,0), acts identically on H, and restricts χH′ to χE′ with every endpoint and extra closed copy retained. Its companion mirror is c_r→−r c_(1/r) with the companion denominator; the oriented global-dual mirror has the opposite sign. The ordinary Fourier restriction still has its explicit section. Thus the new classes are relative residue-representation classes with proved supported placement, not a claimed failure of that existing Fourier lift. The source Z_0, Z_1/tau and integer Z_2 have not changed, and the full numerical weight-separation target remains active.

The original Connes–Consani explicit formula has been applied with a proved cutoff extension; the exact archimedean comparison is W_R(f_T,x)=A_T(x)+1, retaining the endpoint at zero and every finite trivial-zero contour correction. Complete human citations, author-source archive and bounded reading coverage are recorded with these proofs. All complete proof bodies and inspected reproducible diagrams are in the cumulative TeX.
