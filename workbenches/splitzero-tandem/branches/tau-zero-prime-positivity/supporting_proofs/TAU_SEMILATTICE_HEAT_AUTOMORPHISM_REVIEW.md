# The unlocalized supported-zero action and invertible heat flow

Independent bounded derivation, 23 September 2026. This note uses the original supported-zero action and its semilattice adjunction directly. The earlier localization calculation remains in TAU_HEAT_ZERO_LOCALIZATION_REVIEW.md; no localization is used as a premise here.

The coefficient semiring is the programme object \(S=G(A)=\{\tau\}\sqcup A^\bullet\), for a commutative unital ring \(A\), with supported zero \(e=0_A^\bullet\), supported unit \({\bf1}=1_A^\bullet\), and the operations in the original definition. In particular \(e+e=e\), \(e^2=e\), \(ea^\bullet=e\) for every supported scalar, \(\tau\) is the global additive identity and multiplicative absorber, and \(\tau\ne e\). The original definition is restated in [ZH1–ZH3](../SUPPORTED_ZERO_HEAT_IDENTITY_DERIVATION.md). All module and heat comparisons below are proved from this definition.

## SH1. The exact support projection and its section

Let \(M\) be a unital \(S\)-semimodule, with additive identity \(0_M\). Thus its addition is a commutative monoid operation, scalar multiplication distributes in both arguments, \({\bf1}m=m\), \(\tau m=0_M\), and \(s0_M=0_M\).

Define
\[
L=eM,\qquad p_M:M\longrightarrow L,\quad p_M(m)=em,
\qquad i_M:L\longrightarrow M,\quad i_M(l)=l.
\tag{SH1}
\]
Both maps are \(S\)-linear. Additivity of \(p_M\) follows from scalar distributivity. For scalar \(s\), commutativity of \(S\) gives \(p_M(sm)=e(sm)=s(em)\). The inclusion is linear for the inherited operations. On \(l=em\),
\[
p_Mi_M(l)=el=e^2m=em=l,
\qquad
i_Mp_M(m)=em.
\tag{SH2}
\]
Thus the supported-zero operator is an idempotent projection with a specified section. It is the identity on its image.

The addition on \(L\) is idempotent:
\[
l+l=(e+e)m=em=l.
\]
Define \(l\le k\) by \(l+k=k\). This is a partial order: reflexivity is idempotence; if \(l+k=k\) and \(k+l=l\), commutativity gives \(l=k\); if \(l+k=k\) and \(k+j=j\), then \(l+j=l+k+j=k+j=j\). The element \(0_M\) is the least element, and \(l+k\) is the least upper bound of \(l,k\), by associativity and the definition of the order. Therefore \(L\) is a bottomed join-semilattice.

Every supported scalar acts as the identity on \(L\):
\[
a^\bullet(em)=(a^\bullet e)m=em.
\tag{SH3}
\]
The scalar \(\tau\) acts as the map to the bottom element. Thus \(e\), in particular, is its own inverse as an acting operator on \(L\). This is an exact instance of the asserted invertibility of supported zero. It uses the original action on the original image \(eM\).

In the scalar semiring itself, the same mechanism is the corner \(eS=\{\tau,e\}\), whose multiplicative identity is \(e\). Its unit group is \(\{e\}\). The map \(s\mapsto es\) is a unital homomorphism into that corner, taking \({\bf1}\) to the corner unit \(e\). Hence this corner and (SH1) describe the same supported-zero mechanism in scalar and module form.

## SH2. Both semilattice adjunctions, with their actual maps

Let \(\mathsf{JSL}_0\) denote bottomed join-semilattices with maps preserving the bottom element and binary joins. Each such object \(L\) becomes an \(S\)-semimodule \(I(L)\) by taking join as addition, making every supported scalar act as the identity, and making \(\tau\) act as zero.

These rules satisfy the scalar addition law: a sum of two supported scalars is supported, so its action is identity; the sum of their two actions on \(l\) is \(l+l=l\). Cases involving \(\tau\) use the bottom element. Scalar multiplication, both identity laws, and distributivity over joins follow directly. A join-preserving map is \(S\)-linear for these actions, and an \(S\)-linear map between these objects preserves their joins and bottom. Thus \(I\) is a fully faithful inclusion of this category into \(S\)-semimodules.

Write \(E(M)=eM\), with the preceding semilattice structure. For an \(S\)-linear map \(F:M\to N\), define \(E(F)=F|_{eM}\). Its target lies in \(eN\), because
\[
F(em)=eF(m).
\tag{SH4}
\]
It preserves joins and bottom, so this defines the functor \(E\).

First, every \(S\)-linear \(f:M\to I(L)\) factors uniquely through \(p_M\):
\[
f(m)=ef(m)=f(em),\qquad
f=\bar f\,p_M,\quad \bar f=f|_{eM}.
\tag{SH5}
\]
Conversely, every join map \(\bar f:eM\to L\) gives such an \(S\)-linear composite. Restriction and composition are inverse operations, by \(p_Mi_M=\mathrm{id}\). They commute with composition of source and target maps. This proves the natural bijection
\[
\operatorname{Hom}_{\mathsf{JSL}_0}(E(M),L)
\simeq \operatorname{Hom}_S(M,I(L)).
\tag{SH6}
\]
Thus \(E\) is left adjoint to \(I\), with the displayed unit \(p_M\).

Second, every \(S\)-linear \(g:I(L)\to M\) has image in \(eM\):
\[
g(l)=g(el)=eg(l).
\tag{SH7}
\]
It therefore factors uniquely as \(g=i_M\bar g\), where \(\bar g:L\to eM\) is its corestriction. Conversely every such join map gives an \(S\)-linear composite with \(i_M\). These inverse operations are again natural. Hence
\[
\operatorname{Hom}_S(I(L),M)
\simeq\operatorname{Hom}_{\mathsf{JSL}_0}(L,E(M)).
\tag{SH8}
\]
Thus \(E\) is also right adjoint to \(I\), with the displayed counit \(i_M\). The two adjunctions retain both maps in (SH1); neither treats the supported-zero image as an element to discard.

## SH3. Every support fibre and every transition map

For each \(l\in L\), put
\[
M_l=\{m\in M:em=l\}.
\tag{SH9}
\]
This is an \(A\)-module with its additive identity equal to the actual element \(l\).

Here is the complete verification. If \(m,n\in M_l\), then \(e(m+n)=l+l=l\), so the fibre is closed under addition. For \(m\in M_l\),
\[
l+m=em+m=(e+{\bf1})m={\bf1}m=m.
\]
The supported scalar \((-1_A)^\bullet\) gives an inverse:
\[
m+(-1_A)^\bullet m=({\bf1}+(-1_A)^\bullet)m=em=l.
\]
Its support is again \(l\), because \(e(-1_A)^\bullet=e\). Every supported scalar preserves the fibre, and its zero scalar \(e\) acts by the constant value \(l\), exactly the zero action of the fibre module. The remaining ring-module axioms are the semimodule distributivity and associativity laws restricted to supported scalars. This proves the assertion.

When \(l\le k\), there is an exact \(A\)-linear transition
\[
r_l^k:M_l\longrightarrow M_k,\qquad m\longmapsto m+k.
\tag{SH10}
\]
Its target has support \(l+k=k\). It sends the zero \(l\) to \(k\). Its additivity follows from \(k+k=k\), and its scalar compatibility follows from (SH3). Moreover
\[
r_l^l=\mathrm{id}_{M_l},\qquad r_k^j r_l^k=r_l^j
\quad(l\le k\le j).
\tag{SH11}
\]
Both identities follow by adding the indicated idempotent elements and using their order relations.

Thus the original semimodule contains the semilattice of supports, an \(A\)-module at every support, and all the displayed transition maps. The point \(l\) is simultaneously a retained element of \(M\), a support label, and the additive zero of its own fibre. These are the relationships proved by (SH9)–(SH11).

## SH4. Interaction with every linear automorphism

Let \(F:M\to M\) be an \(S\)-linear automorphism. Then
\[
p_MF=\alpha\,p_M,\qquad Fi_M=i_M\alpha,
\qquad\alpha=F|_L.
\tag{SH12}
\]
The first equality is \(eF(m)=F(em)\), and the second is restriction. The inverse of \(F\) is also \(S\)-linear, so \(\alpha\) is an automorphism of the bottomed join-semilattice \(L\).

Every label is transported by this specified map, and the fibre map is
\[
F_l:M_l\xrightarrow{\sim}M_{\alpha(l)}.
\tag{SH13}
\]
It is \(A\)-linear by restriction, sends the source zero \(l\) to the target zero \(\alpha(l)\), and has inverse \((F^{-1})_{\alpha(l)}\). For \(l\le k\),
\[
F_k r_l^k=r_{\alpha(l)}^{\alpha(k)}F_l.
\tag{SH14}
\]
Indeed both sides send \(m\) to \(F(m)+\alpha(k)\). These formulas prove the whole interaction with the retained fibre system.

For a one-parameter group \(F_t\) of \(S\)-linear automorphisms,
\[
F_{t+s}=F_tF_s,\quad F_0=\mathrm{id}_M,\quad F_t^{-1}=F_{-t},
\]
the induced support maps satisfy the same equations
\[
\alpha_{t+s}=\alpha_t\alpha_s,\quad\alpha_0=\mathrm{id}_L,
\quad\alpha_t^{-1}=\alpha_{-t}.
\tag{SH15}
\]
A general semimodule need not have every label fixed pointwise. Equations (SH12)–(SH15) give the exact transport when labels move.

## SH5. The split lift of the heat state space

Let \(V\) be an \(A\)-module and put
\[
\operatorname{Spl}(V)=\{\tau_V\}\sqcup V^\bullet.
\tag{SH16}
\]
The addition is the supported addition of \(V\), with \(\tau_V\) as a new additive identity. A supported scalar acts by
\(a^\bullet v^\bullet=(av)^\bullet\), every scalar kills \(\tau_V\) to \(\tau_V\), and \(\tau v^\bullet=\tau_V\). These operations satisfy all semimodule axioms by direct substitution into the module laws; a sum of supported values remains supported, including a sum whose vector value is zero.

Here the actual support semilattice is the two-element set
\[
e\operatorname{Spl}(V)=\{\tau_V,0_V^\bullet\},
\quad
p(\tau_V)=\tau_V,\quad p(v^\bullet)=0_V^\bullet.
\tag{SH17}
\]
Its fibres are
\[
M_{\tau_V}=\{\tau_V\},\qquad
M_{0_V^\bullet}=V^\bullet.
\tag{SH18}
\]
The transition from the first to the second sends \(\tau_V\) to \(0_V^\bullet\), by addition of \(0_V^\bullet\). The latter fibre has exactly the original \(A\)-module \(V\), with its supported zero retained.

For any \(A\)-linear automorphism \(U:V\to V\), define
\[
\widehat U(\tau_V)=\tau_V,\qquad
\widehat U(v^\bullet)=(Uv)^\bullet.
\tag{SH19}
\]
It is \(S\)-linear, and its inverse is \(\widehat{U^{-1}}\). This follows on supported sums and scalar multiples from the linearity of \(U\), and on terms involving \(\tau_V\) from their defined zero laws.

Both support labels in (SH17) are fixed:
\[
\widehat U(\tau_V)=\tau_V,\qquad
\widehat U(0_V^\bullet)=0_V^\bullet.
\tag{SH20}
\]
The exact commutative square is
\[
p\,\widehat U=p,\qquad \widehat U\,i=i.
\tag{SH21}
\]
The map on the supported fibre is the original automorphism \(U\); the map on the unsupported fibre is its single possible map.

A heat group \(U_t\) of \(A\)-linear automorphisms therefore lifts to a group \(\widehat U_t\), retaining both labels and every vector. At time zero, \(\widehat U_0=\mathrm{id}_{\operatorname{Spl}(V)}\), including both zeros. The scalar \(e\) acts as the identity on the support semilattice throughout this group.

On the full split module, the relation between the two operators is exactly
\[
e\,\widehat U_t=\widehat U_t\,e=e,
\tag{SH22}
\]
where the last \(e\) denotes the projection \(i p\). At time zero, \(\widehat U_0\) is the identity on the whole module, while \(e=ip\) is its identity on the support image. Their equality on that image and their connection on the whole module are (SH2), (SH21), and (SH22).

## SH6. The analytic heat-space lift keeps the same mechanism

Consider the vector space specified for the heat representation:
\[
V=\left\{q:\mathbb R\to\mathbb C\ \text{even and measurable}:
\int_{\mathbb R}e^{a u^2}|q(u)|\,du<\infty
\text{ for every }a>0\right\},
\tag{SH23}
\]
taking equality almost everywhere. For real \(t\), let
\[
U_tq(u)=e^{tu^2}q(u).
\tag{SH24}
\]
These are complex-linear automorphisms. For any \(a>0\), choose \(b>\max\{a+t,0\}\); then
\[
\int e^{au^2}|U_tq(u)|\,du
=\int e^{(a+t)u^2}|q(u)|\,du
\le\int e^{bu^2}|q(u)|\,du<\infty.
\]
Evenness and measurability are preserved. Pointwise multiplication gives
\[
U_tU_s=U_{t+s},\qquad U_0=\mathrm{id},\qquad U_t^{-1}=U_{-t}.
\tag{SH25}
\]
Thus all the maps of SH5 apply with \(A=\mathbb C\), including time zero.

For completeness, the even Fourier integral
\[
\mathcal C(q)(z)=\int_{\mathbb R}q(u)\cos(zu)\,du
\tag{SH26}
\]
defines an entire function. On a compact set with \(|\operatorname{Im}z|\le R\), its integrand and every derivative in \(z\) are dominated by
\(|u|^n e^{R|u|}|q(u)|\). For every \(a>0\), the continuous function
\(|u|^n e^{R|u|-a u^2}\) is bounded on \(\mathbb R\); hence that majorant is integrable by (SH23). Uniform dominated differentiation on compact sets proves the assertion.

Likewise \(H_q(t,z)=\mathcal C(U_tq)(z)\) satisfies
\[
\partial_t H_q=-\partial_z^2H_q.
\tag{SH27}
\]
For \(t\) in a compact real interval, the required \(u^2\) factor is dominated by the same argument with a larger positive \(a\). The sign is exact because \(\partial_z^2\cos(zu)=-u^2\cos(zu)\). This proves the heat equation for this defined representation without changing the coefficient of \(tu^2\).

The zero/nonzero state and the support labels remain as in (SH16)–(SH22). A further statement that a particular entire function has only real zeros is a property of that function in the supported fibre. It does not alter the already proved inverse \(U_{-t}\).

## SH7. An exact unlocalized heat countermodel

A finite-dimensional example proves directly that the supported-zero identity mechanism and invertibility of the full heat group allow opposite real-rootedness behaviour.

Take \(A=\mathbb R\) and
\[
V=\mathbb R[z]_{\le2},\qquad
U_t=I-t\partial_z^2.
\tag{SH28}
\]
On this vector space \((\partial_z^2)^2=0\), so exact multiplication gives
\[
U_tU_s=I-(t+s)\partial_z^2=U_{t+s},\qquad
U_t^{-1}=U_{-t}.
\]
For \(P(t,z)=U_tP(0,z)\), differentiation gives the same backward heat equation as (SH27).

Its two states \(P_-^0=z^2-1\) and \(P_+^0=z^2+1\) evolve as
\[
U_tP_-^0=z^2-1-2t,\qquad
U_tP_+^0=z^2+1-2t.
\tag{SH29}
\]
At zero time, the first has roots \(\pm1\), and the second has roots \(\pm i\). For every real \(t\), \(U_t\) is invertible, the supported-zero action on \(e\operatorname{Spl}(V)\) is its identity, and every support label is fixed. No localization has been performed.

The real-rooted time sets of these two states are respectively \([-1/2,\infty)\) and \([1/2,\infty)\), since their root squares are \(1+2t\) and \(2t-1\). Thus the first state loses real-rootedness under sufficiently negative heat time despite the invertibility of that time map; the second gains it after a positive collision time, again without any change in operator invertibility or supported-zero action.

This is a countermodel to inferring either outcome at \(t=0\) from those algebraic premises alone. It does not deny the supported-zero identity: that identity was built into and proved for the example.

## SH8. The exact real-rooted locus that the heat group transports

Let \(\mathcal R\subset V\) be the set of states whose specified entire transform is not identically zero and has only real zeros. The zero state is kept in \(V\) and in its support fibre; it is excluded only from this particular zero-property set so that “all zeros are real” is not applied to an identically zero function.

For every real \(t\), define
\[
\mathcal R_t=U_{-t}(\mathcal R).
\tag{SH30}
\]
Then
\[
q\in\mathcal R_t\quad\Longleftrightarrow\quad U_tq\in\mathcal R.
\]
For every \(s,t\), the full heat automorphism restricts to the exact bijection
\[
U_s:\mathcal R_{t+s}\xrightarrow{\sim}\mathcal R_t,
\tag{SH31}
\]
because \(U_tU_s=U_{t+s}\), with inverse \(U_{-s}\). The failure of a fixed real-rooted locus to be preserved at time \(s\) is the explicitly defined set
\[
\mathcal D_s=\mathcal R\cap U_{-s}(V\setminus\mathcal R).
\tag{SH32}
\]
These definitions retain the objects specified by that failure and their exact connecting maps.

The supported-zero projection and the lifted heat group commute on every one of these states by (SH21), whether a state belongs to \(\mathcal R_t\) or not. Accordingly a proposed implication about the original zeta heat family must determine the membership of its particular state in these exact loci. The unlocalized semilattice adjunction and the invertible heat group remain valid throughout; neither by itself computes that membership.

## Review of the current ZH derivation

The complete [SUPPORTED_ZERO_HEAT_IDENTITY_DERIVATION.md](../SUPPORTED_ZERO_HEAT_IDENTITY_DERIVATION.md), ZH1–ZH26, was read for an independent mathematical review. No mathematical error was found in its module adjunctions, invertible weighted-integrability heat group, split evaluation maps, residue-generated automorphisms, invariant positive-semidefinite-form criterion, or cancelling-atom calculation. The analytic threshold results used for its actual-family comparison are cited inputs in that note; this review does not claim a new proof or a fresh literature reading of those theorems.

Three precise checks support this conclusion. First, the kernel bound ZH15 follows term by term from \(2n^2e^{4u}\ge e^{4u}+n^2\), valid for \(n\ge1,u\ge0\), together with \(e^{5u}\le e^{9u}\). This retains exactly the stated half-exponential bound. Second, invariance of a positive semidefinite Hermitian form under \(I+aD\), with \(a\ne0,D^2=0\), forces \(Q(aDv,aDv)=0\) by the coefficient of \(n^2\) in \(Q(v+naDv,v+naDv)=Q(v,v)\); positivity makes its entire image radical. The converse follows by expanding the form, so the quotient criterion in ZH24 is exact. Third, the measure in ZH26 is \(\Phi(u)\,du/2\), which is atomless; its decomposition into \(\delta_0/16\) and the indicated remainder contains opposite atoms, and multiplication by \(e^{tu^2}\) preserves that cancellation because its value at zero is 1.

The constant and the compensating remainder in ZH26 are interpreted in the explicitly enlarged measure representation there. They are not separately asserted to belong to the original density transform space. This keeps the original function space and its actual heat group intact.
