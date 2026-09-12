# Arithmetic cohomology over the tau-base

Publication edition of the preceding authored tau-base note. This file retains the model, its maps and proofs; `FINITE_OPERATOR_COMPARISON.md` continues its arithmetic realization. These are research derivations, not Lean-verified analytic theorems.

## Scope

The geometric base is the one-point absolute pointed base with absorber tau. The main calculation is the right adjoint to global cohomology on a specified finite-chart realization. A projective resolution computes arithmetic cohomology; a dual injective complex computes its right adjoint. The arithmetic theta map, finite Mellin jets, nilpotent actions, and original e/tau distinction remain attached.

The category is specified below. No assertion is made that this chart model is an arithmetic scheme, that it supplies all prime correspondences, that its right-adjoint object is an involutive Verdier duality on every sheaf, or that it proves a weight estimate. The dual in the adjunction is algebraic. A continuous-dual identification would require its own map.

## 1. The absolute base and the infinite arithmetic quotient

Let

$$\mathbf F_{1,\tau}=\{\tau,1\}$$

be the pointed multiplicative monoid with identity 1 and absorber tau. Its blueprint zero relation identifies the empty sum with tau; no additive equation $1+1=1$ is imposed. Its spectrum $\mathfrak b_\tau$ has the single prime $\{\tau\}$.

For a nonzero commutative ring $R$, retain

$$G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet.$$

Let $B_R$ be the blueprint with this multiplicative carrier and all its original finite additive relations, including $[\tau]=0$. There is the actual blueprint morphism

$$\jmath_R:\mathbf F_{1,\tau}\longrightarrow B_R,
\qquad \tau\mapsto\tau,\quad1\mapsto1_R^\bullet.$$

On spectra it gives

$$a_R:\operatorname{Spec}B_R\longrightarrow\mathfrak b_\tau.$$

Every prime has inverse image $\{\tau\}$. The arithmetic quotient stays attached:

$$p_R:G(R)\longrightarrow R,\quad p_R(\tau)=0_R,
\quad p_R(r^\bullet)=r.$$

For a domain, the original primes and arithmetic inclusion are

$$P_\tau=\{\tau\},\quad P_0=\{\tau,e_R\},\quad
i_R:\operatorname{Spec}R\hookrightarrow\operatorname{Spec}_{\rm sr}G(R),
\quad\mathfrak p\mapsto\mathfrak p\sqcup\{\tau\}.$$

The image is $V(e_R)=\overline{\{P_0\}}$. The source's infinite quotient at $R=\mathbb Z$ is therefore retained without assigning an additional finite ideal norm.

The Boolean observation is another specified map:

$$\chi_R:G(R)\to\mathbb B,\qquad\chi_R(\tau)=0,
\quad\chi_R(r^\bullet)=1.$$

It gives

$$\operatorname{Spec}\mathbb B\xrightarrow{\operatorname{Spec}\chi_R}
\operatorname{Spec}_{\rm sr}G(R)\xrightarrow{a_R}\mathfrak b_\tau.$$

The first arrow lands at $P_\tau$. The source localization is

$$G(R)[e_R^{-1}]\cong\mathbb B.$$

Indeed $e_R^2=e_R$ and invertibility give $e_R=1$, and $e_Rr^\bullet=e_R$ identifies all supported scalars with 1. External absence remains distinct. The structural morphism $a_R$, with $p_R$ retained, is used for the base change; the localization is its named support observation.

The coefficient realization preserves the infinite arithmetic quotient through

$$\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C,
\end{array}\qquad j:\mathbb Z\hookrightarrow\mathbb C.$$

Both supported zero and external absence have their own images in this square.

## 2. The actual characteristic-zero chart

Set $E=\mathbb C$. Let $P$ be the four-point poset

$$+<\eta<\sigma,\qquad -<\eta<\sigma,$$

with $+$ and $-$ incomparable and with the upper-set topology. Its proper nonempty opens are

$$\{\sigma\},\quad\{\eta,\sigma\},\quad
\{+,\eta,\sigma\},\quad\{-,\eta,\sigma\}.$$

The structural sheaf has $G(E)$ on every open containing an arithmetic chart point and $\mathbb B$ on $\{\sigma\}$. Restriction to sigma is $\chi_E$, and other nontrivial restrictions are identities. Compatibility at sigma forces an entire local family to be absent or supported. In the supported case ordinary amplitudes glue. This proves the sheaf assertion.

Together with $\jmath_E$, this defines a space with a sheaf of blueprints over $\mathfrak b_\tau$. The structural map to $\operatorname{Spec}_{\rm sr}G(E)$ sends $+,-,\eta$ to $P_0$ and sigma to $P_\tau$. Compose with the map induced by $G(j)$ to $\operatorname{Spec}_{\rm sr}G(\mathbb Z)$. On its arithmetic stalks the map is $G(\mathbb Q)\to G(E)$, and at sigma it is $\mathbb B\to\mathbb B$.

This particular chart has generic arithmetic image. Its finite-prime geometry is not being claimed to cover the closed prime fibres. Prime information in this realization enters through the theta map and its Euler/explicit formula.

Retain the exact coefficient spaces and transforms

$$V=\{\phi\in\mathcal S(\mathbb R):\phi\text{ even},\ \phi(0)=0,
\ \widehat\phi(0)=0\},\qquad
\widehat\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi i x\xi}\,dx,$$

$$\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):
\sup_{x>0}x^b|(-x\partial_x)^kF(x)|<\infty
\text{ for all }b\in\mathbb Z,\ k\ge0\},$$

$$\Theta\phi(x)=\sum_{n\in\mathbb Z\setminus\{0\}}\phi(nx),
\qquad JF(x)=x^{-1}F(1/x).$$

Poisson gives $J\Theta\psi=\Theta\widehat\psi$. Define the coefficient diagram

$$\mathcal T_+=V,\quad\mathcal T_-=V,\quad
\mathcal T_\eta=\mathscr B,\quad\mathcal T_\sigma=0,
\quad r_+=\Theta,\quad r_-=J\Theta=\Theta\mathcal F.$$

### The full original support diagram

Let $L=\mathcal P(\{+,-\})$. For nonempty $A\in L$, retain a copy of $V$ at a source leg exactly when that leg lies in $A$. At eta retain $\mathscr B$, and at sigma retain the ordinary zero vector space. Set $\mathcal T_\varnothing=0$. For $A\subseteq A'$, the transports are the coordinate inclusions at the source legs and the identity at eta.

The reconstructed sheaf is

$$\widetilde{\mathcal T}=\{\tau\}\sqcup
\bigsqcup_{A\ne\varnothing}\{A\}\times\mathcal T_A.$$

At sigma its stalk is the complete semilattice $L$, with Boolean scalar action. Restrictions there are semilinear along $\chi_E$:

$$e_E(A,v)=(A,0)\longmapsto A,\qquad
\tau\longmapsto\varnothing.$$

In degree zero the reconstructed module is the original two-leg carrier $(V^\tau)^2$. A missing leg and a supported zero in that leg have different masks. The zero coefficient space for a missing leg is always accompanied by this mask; it does not add a support to that leg.

## 3. Compute global cohomology

Use the declared linear-fibre category

$$\mathcal A=\operatorname{Fun}(P,\operatorname{Vect}_E).$$

Its passage to the original supported sheaf is the reconstruction just given, with internal quotients. It is a realization category, not an asserted new etale-sheaf category.

For $x\in P$, define the projective diagram

$$P_x(y)=\begin{cases}E&x\le y,\\0&\text{otherwise},\end{cases}
\qquad\operatorname{Hom}_{\mathcal A}(P_x,F)=F_x.$$

The constant diagram $\mathbf E$ has the exact projective resolution

$$\boxed{0\to P_\eta\xrightarrow{v\mapsto(v,-v)}P_+\oplus P_-
\xrightarrow{(u,v)\mapsto u+v}\mathbf E\to0.}$$

At $+$ and $-$ the last map is the identity. At eta and sigma it is addition with the specified anti-diagonal kernel. The formulas commute with every arrow.

Therefore

$$\boxed{\mathsf A_\tau(F):=R\Gamma(P,F)
\simeq[F_+\oplus F_-\xrightarrow{r_+-r_-}F_\eta],}$$

in degrees zero and one.

There is an actual comparison to restriction at sigma:

$$\operatorname{res}_\sigma:\mathsf A_\tau(F)\to F_\sigma[0].$$

Representatives in degree zero are $(x,y)\mapsto r_{+\sigma}x$ and $(x,y)\mapsto r_{-\sigma}y$. Their difference is $r_{\eta\sigma}(r_+x-r_-y)$. Hence they are chain homotopic with homotopy $r_{\eta\sigma}$, and define the same derived morphism.

For the actual theta sheaf,

$$\mathsf A_\tau(\mathcal T)
=[V\oplus V\xrightarrow{\Theta(\phi-\widehat\psi)}\mathscr B],$$

$$H^0\mathsf A_\tau(\mathcal T)\cong V,
\quad\psi\mapsto(\widehat\psi,\psi),\qquad
H^1\mathsf A_\tau(\mathcal T)=Q:=\mathscr B/\Theta V.$$

Injectivity of theta follows by its Mellin transform on $\Re s>1$, nonvanishing of the Euler product there, and Mellin uniqueness. It uses no assertion about zeros in the critical strip.

The original supported differential is

$$\widetilde d(\phi,\psi)=(A,\Theta p(\phi)-J\Theta p(\psi)),$$

with $A$ the set of present legs; an absent pair maps to tau. Its cohomology uses

$$Z^i_{\rm sp}=\operatorname{Eq}(d,\varepsilon d),\qquad
H^i_{\rm sp}=\operatorname{coeq}(b,\varepsilon b),\qquad
\varepsilon(x)=ex.$$

For every nonempty $A$, the degree-one fibre is $Q$. A single-leg degree-zero fibre is zero, and the joint degree-zero fibre is $V$. Thus

$$\boxed{\widetilde H^1_\tau=\{\tau\}\sqcup
\bigsqcup_{A\ne\varnothing}\{A\}\times Q.}$$

Restriction to sigma sends its classes to the supported zero of their label in the sigma skeleton. Their global cohomology classes remain present in the displayed object.

## 4. Compute the right adjoint on this base

For $x\in P$ and a vector space $W$, define

$$I_x(W)(y)=\begin{cases}W&y\le x,\\0&\text{otherwise},\end{cases}
\qquad\operatorname{Hom}_{\mathcal A}(F,I_x(W))
=\operatorname{Hom}_E(F_x,W).$$

Evaluation is exact and every vector space is injective over $E$, so $I_x(W)$ is injective. Define

$$\boxed{K_\tau(W)=
[I_\eta(W)\xrightarrow{(+\mathrm{res},-\mathrm{res})}I_+(W)\oplus I_-(W)]}$$

in degrees $-1,0$.

For a sheaf $F$ the actual adjunction is

$$\boxed{R\operatorname{Hom}_{\mathcal A}(F,K_\tau(W))
\cong R\operatorname{Hom}_E(\mathsf A_\tau(F),W).}$$

Both sides are the complex

$$\operatorname{Hom}(F_\eta,W)\longrightarrow
\operatorname{Hom}(F_+,W)\oplus\operatorname{Hom}(F_-,W),
\qquad\ell\mapsto(\ell r_+,-\ell r_-).$$

For a bounded complex $W$, totalize with its specified original differential. On the four stalks,

$$K_\tau(W)_+=[W\xrightarrow{1}W],\quad
K_\tau(W)_-=[W\xrightarrow{-1}W],\quad
K_\tau(W)_\eta=W[1],\quad K_\tau(W)_\sigma=0.$$

If $S_\eta W$ denotes the diagram concentrated at eta, this proves

$$\boxed{K_\tau(W)\simeq S_\eta W[1].}$$

The shift places $W$ in degree $-1$ and is derived from the resolution. This is the right adjoint to algebraic $R\Gamma$ on the declared category. It has not been declared to be extraordinary pullback for an unconstructed proper arithmetic morphism or an involutive local Verdier duality.

Apply the calculation fibrewise to the retained support diagrams. Every zero coefficient stalk reconstructs as its labelled zero, including at sigma. The dual transports are

$$\rho_{AB}^{\vee}:\operatorname{Hom}(H_B,W)\to
\operatorname{Hom}(H_A,W),\qquad\ell\mapsto\ell\rho_{AB}.$$

Their index category is $L^{\rm op}$. The reconstruction interface in PR #6 permits a nonzero bottom fibre when that opposite diagram has one; it must not be forced to zero without an additional quotient.

## 5. The characteristic-zero arithmetic action

For $a>0$, retain

$$U_aF(x)=F(x/a),\qquad
\mathcal MF(s)=\int_0^\infty F(x)x^s\frac{dx}{x}.$$

The exact transforms are

$$\mathcal MU_aF(s)=a^s\mathcal MF(s),\qquad
\widehat{U_a\phi}=aU_{1/a}\widehat\phi.$$

Consequently the chain action is

$$\boxed{(\phi,\psi)\mapsto(U_a\phi,aU_{1/a}\psi),
\qquad F\mapsto U_aF.}$$

Direct calculation gives $U_aJ=aJU_{1/a}$ and

$$d(U_a\phi,aU_{1/a}\psi)=U_ad(\phi,\psi).$$

It fixes every original support mask and the support skeleton at sigma. The base remains the same point while its pushforward retains the arithmetic action.

The moment map supplies two actual coefficient lines,

$$\mathcal L_0:E\text{ with action }1,\qquad
\mathcal L_1:E\text{ with action }a,$$

$$m(\phi)=(\phi(0),\int_{\mathbb R}\phi(x)\,dx),
\qquad mU_a=\operatorname{diag}(1,a)m.$$

Using $K_\tau(\mathcal L_1)$ gives the dual action

$$\boxed{(U_a\ell)(v)=a\,\ell(U_a^{-1}v).}$$

The factor $a$ is retained from the second moment representation, not deduced from the cardinality of a base point.

## 6. The finite arithmetic map into the computed dual

Put $g=2\xi$ and let $Z$ be a finite reflection-stable set of actual zeros with multiplicities $m_\rho$. Define

$$A_Z=\bigoplus_{\rho\in Z}\mathcal O_\rho/(g),\qquad
(J_ZF)_\rho=\sum_{j<m_\rho}
\frac{(\mathcal MF)^{(j)}(\rho)}{j!}z_\rho^j.$$

The source identity $\mathcal M\Theta\phi=gH_\phi$, with $H_\phi$ entire, proves that

$$\mathcal T\longrightarrow S_\eta A_Z$$

is a sheaf morphism: use $J_Z$ at eta and zero at the other points. It induces the specified degree-one map $Q\to A_Z$. The finite jet map is onto by independence of $e^{\rho y}y^j/j!$ on every nonempty interval and a compactly supported smooth interpolation construction. The continuation computes its exact operator kernel and a spectral section.

The scaling action is

$$U_a|_\rho=a^\rho\sum_{j<m_\rho}\frac{(\log a)^j}{j!}N_\rho^j,
\qquad N_\rho z^j=z^{j+1}.$$

Retain the reflected germ map

$$f^\dagger(s)=\overline{f(1-\bar s)},\qquad
\sum c_jz_{\iota\rho}^j\mapsto\sum(-1)^j\bar c_jz_\rho^j.$$

The actual perfect finite residue pairing is

$$R_Z(f,h)=\sum_{\rho\in Z}\operatorname{Res}_{\rho}
\frac{f^\dagger(s)h(s)}{g(s)}\,ds.$$

Locally write $g=u(z)z^{m_\rho}$ with its actual unit. The residue pairs $z^i$ with $u(z)z^{m_\rho-1-i}$, proving nondegeneracy with the units retained. Its raw skew-Hermitian orientation is not changed by inserting a phase. Its scaling is

$$R_Z(U_af,U_ah)=aR_Z(f,h).$$

Precomposition with the degree-one jet map gives the actual injective map

$$\boxed{\overline{A_Z}\longrightarrow
H^{-1}R\operatorname{Hom}_{\mathcal A}
(\mathcal T,K_\tau(\mathcal L_1)),}$$

$$\bar f\longmapsto\left([F]\longmapsto
\sum_{\rho\in Z}\operatorname{Res}_{\rho}
\frac{f^\dagger(s)\mathcal MF(s)}{g(s)}\,ds\right).$$

The target is $\operatorname{Hom}_E(Q,\mathcal L_1)$ by the computed adjunction. Well-definedness follows because a theta relation adds the holomorphic residue expression $f^\dagger H_\phi$. Surjectivity of the finite jet map and perfectness prove injectivity. The displayed dual action and scaling identity prove equivariance.

The arithmetic trace contraction uses the specified Jacobian map

$$J_g:A_Z\to A_Z,\qquad[h]\mapsto[g'h],$$

$$\boxed{R_Z(f,J_gh)=
\sum_\rho m_\rho\overline{f(1-\bar\rho)}h(\rho)
=\operatorname{Tr}(M_{f^\dagger h}|A_Z).}$$

At a zero of order $m$, $g'\equiv m u(z)z^{m-1}\pmod{z^m}$. The radical of the trace contraction consists of the jets with zero residue value. The original internal quotient sends them to their supported zero; the residue pairing before contraction retains all jet orders.

All these maps lift at each support label. A vanishing functional is the supported zero functional of its label. The external scalar tau retains its own image. Changes of source labels commute with the maps, and the dual arrows are the stated precomposition maps.

## 7. Tensor powers over the same base

Take products of the declared chart $P$ over the underlying point of $\mathfrak b_\tau$ and external products of coefficient sheaves. The coefficient tensors are over $E$. The topological product with these coefficients is the declared model; no identification with the schematic square of the full arithmetic space is assumed.

The external tensor product of the projective resolution has differential

$$d(x_1\otimes\cdots\otimes x_r)=
\sum_{j=1}^r(-1)^{\sum_{k<j}|x_k|}
 x_1\otimes\cdots\otimes dx_j\otimes\cdots\otimes x_r.$$

Because tensoring over $E$ is exact, this gives the explicit Kunneth map and

$$\boxed{H^r\mathsf A_{\tau,r}(\mathcal T^{\boxtimes r})
\cong Q^{\otimes_E r}.}$$

The numerator is $\mathscr B^{\otimes r}$. Its top boundaries are the sum of subspaces with $\Theta V$ in at least one factor, so the quotient is exactly the displayed one. Other support fibres and their transports remain in the full diagram; this equation is its specified joint-support evaluation.

A tensor relation is quotiented internally at its support label. A tensor containing external absence has its specified absorbing basepoint. Coefficient balancing and support-index products remain the two actual operations, with their reconstruction maps retained.

Dualizing the tensor resolution gives

$$\boxed{K_{\tau,r}(W)\simeq S_{(\eta,\ldots,\eta)}W[r].}$$

The degree $-r$ is calculated by the tensor complex, with the same Koszul signs. The finite spectral quotient of the top cohomology has action

$$a^{\rho_1+\cdots+\rho_r}
\exp\left((\log a)\sum_jN_{\rho_j,j}\right).$$

For a repeated spectral exponent the exact modulus comparison is

$$\boxed{\log\frac{|a^{r\rho}|^2}{a^r}
=r(2\Re\rho-1)\log a\qquad(a>1).}$$

At this stage it is a statement about the finite spectral quotient. The continuation constructs its actual finite invariant section in the original cohomology. No bound on this quantity follows from the tensor identity alone.

## 8. Structural projection, internal null relations, and packet deletion

The structural map sends every geometric point to the base point. The derived pushforward retains coefficient relations and operators. Restriction to sigma is the separate derived morphism calculated in Section 3, and has the support skeleton as its supported target in this model.

For ordinary vector spaces $W,W'$ with single-active-fibre lifts, a $G(E)$-linear map

$$f:W^\tau\to(W')^\tau$$

that sends one supported vector to tau sends every supported vector to tau. Indeed $f(0_W^\bullet)=f(ev)=ef(v)=\tau$. For every supported $w$, $ef(w)=f(ew)=\tau$. In this specified target only tau has e-multiple equal to tau. This assertion is not made for a general semimodule with nonzero bottom group fibre.

For a reflection-stable finite set $Z=C\sqcup B$, the actual packet deletion is

$$A_Z\twoheadrightarrow A_C,\qquad\ker=A_B.$$

Its removed convolution trace is

$$\operatorname{Tr}(H_h|A_Z)-\operatorname{Tr}(H_h|A_C)
=\sum_{\rho\in B}m_\rho\mathcal Mh(\rho).$$

Finite Mellin interpolation makes this nonzero for some admissible compactly supported smooth $h$ whenever $B$ is nonempty. The cone of $A_Z[-1]\to A_C[-1]$ has $H^0=A_B$. That is the explicit cohomological contribution of this deletion.

An internal quotient by a subspace $N$ instead uses

$$q_N^{\rm sp}:W^\tau\to(W/N)^\tau,\qquad
n^\bullet\mapsto0_{W/N}^\bullet,\quad\tau\mapsto\tau.$$

This is the map used throughout the programme. A proved null relation becomes a supported zero while its quotient kernel remains recorded.

## 9. Output and remaining geometry

The calculated model supplies

$$\widetilde{\mathcal T}\text{ over }\mathfrak b_\tau
\xrightarrow{\mathsf A_\tau}\widetilde H^1_\tau
\xrightarrow{J_Z}A_Z^\tau,$$

with the right-adjoint object $K_\tau(\mathcal L_1)$, the cohomological residue map into that adjoint, its Jacobian trace contraction, and the tensor-power morphisms. It is a characteristic-zero scaling calculation.

The structural square retains $G(\mathbb Z)\to\mathbb Z$. The generic chart image is explicit. A global prime-sensitive geometric realization with its full Lefschetz theorem and the two-sided weight estimates is not established by the finite chart topology. The continuation calculates a further analytic comparison without treating that remaining geometric step as proved.

## Sources and validation scope

- Owner's `globalization_note.tex`: localizations, stalks, contracted monoid algebra and blueprint remark; the supplied structural formalization supplies the explicit `[tau]=0` presentation correction.
- Existing actual-theta comparison in the workbench: source test spaces, theta/Mellin maps, complete multiplier and finite jets. The earlier generated notes are retained research inputs, not a blanket independent audit.
- Selected supplied French Weil II TeX, sections 3.3 and 6.2.1-6.2.7: the comparison-image and duality architecture. Reading these windows is not verification of the whole source corpus. Historical transcription qualifications remain.
- O. Lorscheid, *The geometry of blueprints. Part I*, arXiv:1103.1745, for the declared blueprint framework, not for the new finite-chart calculations.
- PR #6 at `5f6ee6575550d8a20c6fc3990359cb4f67855f80` for the original reconstruction and internal-homology interfaces. This publication retains its generalized bottom-fibre treatment.

`check_tau_base.py` executes finite regressions for the projective resolution, adjoint complex, support differential, action compatibility, tensor signs and trace deletion. These checks are not analytic proof certificates or a verification of Deligne's theorem or RH. The preceding source's spectral statements were about finite quotients; `FINITE_OPERATOR_COMPARISON.md` now constructs their explicit sections and finite invariant subspaces.
