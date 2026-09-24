# The exact lifting boundary in the whole original arithmetic source

Root derivation, 24 September 2026. Proof locators GLB0–GLB8. This calculation keeps the actual Fréchet source, all original nontrivial zeros and their full multiplicities. It constructs and evaluates one specific boundary; it does not claim that this boundary is the geometric lifting obstruction in the user's proposal.

## GLB0. Source and prerequisite check

The supporting datum remains \(\tau\langle Z_1;\text{no }Z_2\rangle\). Arithmetic and analytic operations here occur after the complete arithmetic has been reconstructed. No operation in this note adds, subtracts, coordinatizes or measures that supporting datum. The user's complete correction chain and the prerequisite check for this calculation are in the private PC01 record. A coefficient zero below is not the supporting point or the user's \(Z_0\).

The precise receiving sources are S1–S7 of GLOBAL_MELLIN_SYNTHESIS.md, reread in full for this calculation, and RZ1–RZ2 of ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md. S5 proves equality of the zero-jet kernel with the closure of the actual original arithmetic summation image. It does not assert that this ideal consists of all multiples of one function inside the Fréchet space. That stronger statement is neither needed nor used.

The relevant Connes–Consani construction is the unordered generic overlap and its full signed stalk, original CC.tex lines499–600 and773–847, reconstructed in CG1–CG3. Its support comparison preserves \(\tau\langle Z_1;\text{no }Z_2\rangle\), the stalk torsion and both chart maps. Deligne's relevant construction is the specialization/localization cross of *La conjecture de Weil. II*, §3.6, reconstructed in DC1–DC9. Its source obstruction is \(\operatorname{im}\partial/\partial K\). The exact difference between that cross and the sequence below is calculated in GLB8; a shared use of the word “lift” does not identify the maps.

## GLB1. The complete source and its operations

Let
\[
\mathcal A=\{k\in C^\infty(\mathbb R_{>0}):
p_{N,j}(k)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jk(u)|<\infty
\text{ for all integers }N,j\ge0\},
\tag{GLB1.1}
\]
and
\[
\mathcal B=\{F\text{ entire}:b_{A,M}(F)=
\sup_{|\Re s|\le A}(1+|\Im s|)^M|F(s)|<\infty
\text{ for all integers }A,M\ge0\}.
\tag{GLB1.2}
\]
S1 proves the topological isomorphism
\[
\mathcal Mk(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u},\qquad
k(e^x)=\frac1{2\pi}\int_{\mathbb R}F(1/2+it)e^{-itx}\,dt.
\tag{GLB1.3}
\]
Let \(\mathscr Z\) be the complete distinct nontrivial zero set of the original \(\zeta\), with actual multiplicities \(m_\rho\). Put
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\ (\rho\in\mathscr Z,\ 0\le j<m_\rho)\},\qquad
\mathcal Q=\mathcal B/\mathcal I.
\tag{GLB1.4}
\]
Every jet is continuous by Cauchy's formula, hence \(\mathcal I\) is closed. The topology on \(\mathcal Q\) is the quotient Fréchet topology. S5 identifies its Mellin preimage ideal exactly with
\(\overline{\mathcal E(\mathcal S_0^{\rm even})}^{\mathcal A}\), where
\(\mathcal E f(u)=u^{1/2}\sum_{n\ge1}f(nu)\) and
\(\mathcal S_0^{\rm even}=\{f\text{ even Schwartz}:f(0)=0,\int_{\mathbb R}f=0\}\).
In particular this is the whole original source closure, not a finite zero truncation.

Retain the actual member of this image
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\quad
k_0(u)=u^{1/2}\sum_{n\ge1}f_0(nu),\quad
F_0(s)=\mathcal Mk_0(s)=c(s)\zeta(s),
\tag{GLB1.5}
\]
where the complete multiplier is
\[
c(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\tag{GLB1.6}
\]
The product has its entire continuation; its zeros are exactly \((\rho,m_\rho)\). Its endpoint values are \(F_0(0)=F_0(1)=1/8\), and at each trivial zero,
\[
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0\quad(r\ge1).
\tag{GLB1.7}
\]
These values retain the pole, Gamma-pole and trivial-zero cancellations. We use \(F_0\) as a member of the original summation image with the displayed exact comparison to \(\zeta\), never as a replacement arithmetic function.

Define \(\mathsf LF=sF\) and, for a recovered \(a>0\), \(\mathsf T_aF=a^sF\), using the real logarithm. They act continuously on \(\mathcal B\), because
\[
b_{A,M}(\mathsf LF)\le(A+1)b_{A,M+1}(F),\qquad
b_{A,M}(\mathsf T_aF)\le\max(a^A,a^{-A})b_{A,M}(F).
\tag{GLB1.8}
\]
They preserve every required zero order and therefore act on \(\mathcal I\) and \(\mathcal Q\); write \(L,T_a\) for the quotient actions. Direct multiplication gives \(\mathsf T_a\mathsf T_b=\mathsf T_{ab}\) and the inverse \(\mathsf T_{a^{-1}}\). Their source actions are
\[
\mathsf D=\tfrac12-u\partial_u,\qquad
(\mathsf W_a k)(u)=a^{1/2}k(u/a).
\tag{GLB1.9}
\]
Integration by parts in (GLB1.3), with both endpoints zero by (GLB1.1), gives \(\mathcal M\mathsf D=\mathsf L\mathcal M\). Substitution \(u=av\) gives \(\mathcal M\mathsf W_a=\mathsf T_a\mathcal M\), including the factor \(a^{1/2}\). Thus none of these operations is placed on \(\tau\).

## GLB2. Division on its actual domain

Fix \(\rho\in\mathscr Z\), put \(z=s-\rho\), and let \(r\ge1\) be an integer. For a member \(F\in\mathcal B\) vanishing to order at least \(r\) at \(\rho\), Taylor division gives the entire function \(F/z^r\). It still belongs to \(\mathcal B\). In fact outside \(|z|<1\) the denominator has modulus at least one. Inside \(|z|\le1\), the maximum principle for the holomorphic quotient on \(|z|\le2\) gives
\[
b_{A,M}(F/z^r)\le b_{A,M}(F)+2^{-r}(2+|\Im\rho|)^M b_{A',0}(F),
\quad A'\ge\max(A,|\Re\rho|+2).
\tag{GLB2.1}
\]
This also proves continuity on the closed subspace with those vanishing conditions.

Consequently
\[
z^r\mathcal I=\{F\in\mathcal I:\operatorname{ord}_\rho F\ge m_\rho+r\}.
\tag{GLB2.2}
\]
The forward inclusion follows by multiplication. For the reverse, divide by \(z^r\) using (GLB2.1). At \(\rho\) the quotient still has order at least \(m_\rho\), and at every other actual zero the divisor is a unit, so all original multiplicities remain. This proves (GLB2.2), and proves that \(z^r\mathcal I\) is closed without assuming \(\mathcal I=F_0\mathcal B\).

## GLB3. The two finite quotient receivers of the whole source

Write \(m=m_\rho\) and retain the local original unit
\[
\zeta(\rho+z)=z^m u_\rho(z),\quad
u_\rho(0)=\frac{\zeta^{(m)}(\rho)}{m!},\qquad
v_\rho(z)=c(\rho+z)u_\rho(z),\quad
F_0(\rho+z)=z^m v_\rho(z).
\tag{GLB3.1}
\]
Both \(u_\rho\) and \(v_\rho\) are holomorphic units near this nontrivial zero. Every derivative of the full \(c\) remains in \(v_\rho\).

Set \(R_r=\mathbb C[z]/(z^r)\), a coefficient algebra at this analytic zero. The maps
\[
\mathcal I/z^r\mathcal I\xrightarrow{\Phi_r}R_r,
\quad[F]\mapsto[F/F_0]_{\rho,r},\qquad
\mathcal B/z^r\mathcal B\xrightarrow{\Psi_r}R_r,
\quad[F]\mapsto[F]_{\rho,r}
\tag{GLB3.2}
\]
are topological linear isomorphisms. The first uses division only as a germ at \(\rho\): all \(F\in\mathcal I\) have sufficient order there. Its kernel is (GLB2.2); its inverse sends a polynomial class \([P]\) of degree less than \(r\) to \([F_0P]\). Changing \(P\) by \(z^rQ\) changes the representative by an element of \(z^r\mathcal I\). The maps are continuous because they depend on finitely many derivatives, division by the fixed nonzero number \(v_\rho(0)\), and multiplication by \(F_0\).

For the second map the kernel is \(z^r\mathcal B\) by (GLB2.1). It is onto: set \(G=F_0/z^m\in\mathcal B\), so \(G(\rho)=v_\rho(0)\ne0\). For a desired polynomial jet \(P\), let \(H\) be the Taylor polynomial through degree \(r-1\) of \(P(z)/G(\rho+z)\); then \(GH\in\mathcal B\) has the desired jet. This gives a continuous inverse in the quotient. In particular, using polynomial jets here does not assert that the constant function one belongs to \(\mathcal B\).

In these coordinates the inclusion-induced map between the two quotients is exactly
\[
R_r\longrightarrow R_r,\qquad[P]\longmapsto[z^m v_\rho(z)P]\pmod{z^r}.
\tag{GLB3.3}
\]
The full unit has not been made monic or omitted. Its kernel is all of \(R_r\) for \(r\le m\), and \(z^{r-m}R_r\) for \(r>m\). Its cokernel is \(\mathbb C[z]/(z^{\min(r,m)})\).

## GLB4. The connecting sequence and its full multiplicity

Apply the continuous differential \(\mathsf L-\rho\), raised to the power \(r\), to
\[
0\longrightarrow\mathcal I\longrightarrow\mathcal B
\longrightarrow\mathcal Q\longrightarrow0.
\tag{GLB4.1}
\]
It gives a short exact sequence of two-term cochain complexes, in degrees zero and one. Multiplication by \(z^r\) is injective on \(\mathcal B\) by the identity theorem, hence also on \(\mathcal I\). The resulting exact sequence is
\[
0\longrightarrow\ker(L-\rho)^r
\xrightarrow{\delta_{\rho,r}}\mathcal I/z^r\mathcal I
\longrightarrow\mathcal B/z^r\mathcal B
\longrightarrow\mathcal Q/(L-\rho)^r\mathcal Q
\longrightarrow0,
\tag{GLB4.2}
\]
where
\[
\delta_{\rho,r}[F]=[z^rF].
\tag{GLB4.3}
\]
Here \(z^rF\in\mathcal I\) is exactly the kernel condition in \(\mathcal Q\); changing \(F\) by \(I\) changes its image by \(z^rI\). Exactness can be checked without any spectral theorem: a boundary vanishes exactly when subtracting an element of \(\mathcal I\) makes \(z^rF=0\); a class of \(I\) dies in the middle quotient exactly when it equals \(z^rF\); and a member of \(B\) dies in the last quotient exactly when it lies in \(I+z^rB\).

For the complete basis of the first term, define
\[
V_{\rho,j}(s)=\frac{F_0(s)}{(s-\rho)^j},\qquad 1\le j\le m.
\tag{GLB4.4}
\]
Division is valid by (GLB2.1). Their classes are supported only at the full \(\rho\)-jet, because every other actual zero retains its original multiplicity. Their orders at \(\rho\) are \(m-j\), so the classes are independent. For \(j\le\min(r,m)\),
\[
\Phi_r\delta_{\rho,r}[V_{\rho,j}]=[z^{r-j}].
\tag{GLB4.5}
\]
These monomials form exactly the kernel computed in (GLB3.3). Exactness then proves they span all of \(\ker(L-\rho)^r\), not merely a chosen finite subspace. We have derived
\[
\dim\ker(L-\rho)^r=\min(r,m),\qquad
\mathcal Q/(L-\rho)^r\mathcal Q\cong
\mathbb C[z]/(z^{\min(r,m)}).
\tag{GLB4.6}
\]
The last map is the Taylor jet at \(\rho\) through degree \(\min(r,m)-1\). Its kernel is the actual image of \((L-\rho)^r\); to see this directly, subtract a representative with the same finitely many jets as needed, then apply (GLB2.1). Equivalently (GLB3.3) identifies the quotient. The kernel is closed because those finite jet functionals on \(\mathcal Q\) are continuous. All displayed finite-dimensional quotient identifications therefore also hold with their quotient topologies.

## GLB5. The exact one-dimensional boundary and its arithmetic action

For \(r=1\), the entire sequence is
\[
0\longrightarrow\mathbb C[V_{\rho,1}]
\xrightarrow{\delta_{\rho,1}}\mathbb C[F_0]
\xrightarrow{0}\mathbb C\xrightarrow{\operatorname{id}}\mathbb C
\longrightarrow0,
\quad\delta_{\rho,1}[V_{\rho,1}]=[F_0]\ne0.
\tag{GLB5.1}
\]
The brackets \([F_0]\) on this line mean its nonzero class in \(\mathcal I/z\mathcal I\), not its zero class in \(\mathcal Q\). Nonvanishing also follows directly: if \(F_0=zH\) with \(H\in\mathcal I\), its vanishing order at \(\rho\) would be at least \(m+1\), contradicting (GLB3.1).

Each \(T_a\) acts by \(a^\rho\) on both connecting lines. Indeed
\[
(a^s-a^\rho)V_{\rho,1}(s)
 =F_0(s)\frac{a^s-a^\rho}{s-\rho}\in\mathcal I.
\tag{GLB5.2}
\]
The right side belongs to \(\mathcal B\) by continuous multiplication on \(V_{\rho,1}\), and has the required orders at every zero. At \(\rho\) the quotient factor is the holomorphic value \(a^\rho\log a\). Likewise \((a^s-a^\rho)F_0\in z\mathcal I\), using (GLB2.2). Consequently \(\delta_{\rho,1}\) is equivariant for every recovered multiplicative character action and connects equal characters. No weight separation is present in this particular sequence.

The next full source object is
\[
\mathcal E_\rho=\mathcal B/z\mathcal I,
\qquad 0\longrightarrow\mathcal I/z\mathcal I
\longrightarrow\mathcal E_\rho\longrightarrow\mathcal Q
\longrightarrow0.
\tag{GLB5.3}
\]
All are actual Hausdorff Fréchet spaces by (GLB2.2). Multiplication and the operators preserve the displayed ideal. The kernel is square-zero: for \(F,G\in\mathcal I\), the product divided by \(z\) is in \(\mathcal I\), since it has order at least \(2m-1\ge m\) at \(\rho\), the required orders at every other zero, and belongs to \(\mathcal B\) by (GLB2.1). The module structure on this kernel is evaluation at \(\rho\), because \((H-H(\rho))F\in z\mathcal I\) for every \(H\in\mathcal B\), with the scalar expression interpreted in the ambient entire functions. This is a constructed global receiver retaining one further original jet and all other zero data.

## GLB6. Localization to the original germ sequence, including its multiplier

Restriction from \(\mathcal B\) to \(\mathcal O_\rho\) and from \(\mathcal I\) to \((\zeta)\mathcal O_\rho\) defines a commuting map from (GLB4.1) to the original germ sequence. The ideal inclusion is valid since each source function has order at least \(m\) and \(u_\rho\) is a unit. Under this map
\[
[V_{\rho,1}]\longmapsto
\left[c(s)\frac{\zeta(s)}{s-\rho}\right]
=c(\rho)\left[\frac{\zeta(s)}{s-\rho}\right],
\qquad
[F_0]\longmapsto c(\rho)[\zeta]
\tag{GLB6.1}
\]
on the respective one-dimensional quotient lines. The scalar evaluation is justified because the discarded difference is divisible by the indicated ideal; it is not a Taylor approximation. For \(r>1\), all derivatives through order \(r-1\) of the full \(c\) remain. Explicitly the coefficient of \(z^k\) in the product with a local \(\zeta\)-quotient jet \(h(z)\) is
\[
\sum_{j=0}^k\frac{c^{(k-j)}(\rho)}{(k-j)!}\frac{h^{(j)}(0)}{j!}.
\tag{GLB6.2}
\]
Thus the global boundary is identified exactly with the original germ boundary for differential \(s-\rho\). ZLB3 then compares the latter with differential \(a^s-a^\rho\), multiplying the connecting line by the full simple-zero quotient with value \(a^\rho\log a\). No completion factor is silently suppressed.

## GLB7. The full source functions solving the inhomogeneous equation

Let \(k_{\rho,0}=k_0\), and for \(1\le j\le m\) put
\[
k_{\rho,j}=\mathcal M^{-1}V_{\rho,j}\in\mathcal A.
\tag{GLB7.1}
\]
Existence and membership follow from (GLB2.1) and the topological isomorphism (GLB1.3). Their exact equations are
\[
(\mathsf D-\rho)k_{\rho,j}=k_{\rho,j-1}.
\tag{GLB7.2}
\]
The first source function is explicitly
\[
k_{\rho,1}(u)
=-u^{1/2-\rho}\int_0^u v^{\rho-1/2}k_0(v)\frac{dv}{v}
=u^{1/2-\rho}\int_u^\infty v^{\rho-1/2}k_0(v)\frac{dv}{v}.
\tag{GLB7.3}
\]
Both integrals converge by the endpoint decay in \(\mathcal A\), and they agree because their full integral is \(F_0(\rho)=0\). Differentiating the first proves (GLB7.2), including its sign and the coefficient \(1/2\). Choosing the first integral near zero and the second near infinity proves arbitrarily rapid endpoint decay: bound \(k_0(v)\) by an arbitrary power \(v^N\) or \(v^{-N}\) and integrate the resulting power, choosing \(N>|\Re\rho-1/2|\). Repeated logarithmic derivatives follow from the differential equation and the corresponding bounds for \(k_0\). This independently proves membership in \(\mathcal A\).

The same formula, replacing \(k_0\) by \(k_{\rho,j-1}\), holds for each \(1\le j\le m\). Its total integral is \(V_{\rho,j-1}(\rho)=0\) because the remaining vanishing order is \(m-j+1\ge1\). Thus every member of the entire original Jordan chain has an exact convergent source integral. A homogeneous solution is a scalar multiple of \(u^{1/2-\rho}\), which belongs to \(\mathcal A\) only when that scalar is zero: at least one endpoint violates arbitrary-power decay. Hence the displayed source solution is unique in \(\mathcal A\).

Modulo the closed arithmetic source image, the first equation says that \([k_{\rho,1}]\) is an eigenvector. In the actual source it has the nonzero right side \(k_0\). This precisely identifies the lifting boundary instead of claiming that a source preimage is an eigenfunction.

## GLB8. Comparison to the weight-separation target

Deligne's geometric obstruction in DC5 is the quotient \(\operatorname{im}\partial/\partial K\) in an exact specialization/localization cross. Its vanishing uses source weights at most \(i\) and target weights at least \(i+1\), constructed from properness, local monodromy and duality, including their Tate factors.

The exact global source sequence here instead has the nonzero boundary (GLB5.1), with equal arithmetic character \(a^\rho\) on both lines. It remains nonzero for any actual zero on the critical line as well. The calculation therefore cannot serve as a proposed contradiction to RH or as an obstruction to the user's construction merely because that construction also seeks a lift. No map in the cited construction or the CC support comparison identifies the requested geometric lift with an exact analytic eigenfunction lift through (GLB4.1).

The connecting construction actually obtained is (GLB5.3), retaining its square-zero extra jet and its continuous maps, together with the original-function germ comparison (GLB6.1) and the source integral chain (GLB7.3). These preserve all the arithmetic data. The separated coefficient extension in ZTM4 has a different, explicitly character-shifted kernel; its unique splitting is proved there. Identifying such a shift with the programme's geometric lifting obstruction requires deriving that shift from the actual source maps. It cannot be supplied by changing the action in (GLB4.1).
