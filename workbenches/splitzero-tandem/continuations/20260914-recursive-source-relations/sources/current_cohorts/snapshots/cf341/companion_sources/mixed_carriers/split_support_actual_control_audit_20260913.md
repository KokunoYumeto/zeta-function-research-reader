# Independent mixed-support audit of the current arithmetic assembly

This audit concerns the user's **mixed support**, including independently present coefficient slots and all mixed faces. The initial two-leg reading is retained below only as one explicitly typed subdiagram. It does not exhaust mixed support. Sources were read in full: `total_object/total_object.tex`, `total_object/coherent_assembly.tex`, `total_object/arithmetic_gluing.tex`, `shared_thread_audit/segment16_28/PACKET_SURVIVAL.tex`, and `sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`. Paths beginning with `total_object` or `shared_thread_audit` are under `work/rh_counterfactual_20260913`; the NOTE is under `output/split_zero_rh_tandem_2026-09-12`.

## 1. Independent mixed support and its exact synchronized subobject

For a commutative ring R, the scalar carrier is

\[
G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet.
\tag{MSA1}
\]

Its supported addition and multiplication use those of R; tau is the additive identity and multiplicative absorber. A supported sum whose ring coefficient cancels is e, with its support retained. For two coefficient rings A and B, the actual map from a synchronized split product into the independent product is

\[
j:G(A\times B)\longrightarrow G(A)\times G(B),\qquad
j(\tau)=(\tau,\tau),\quad j((a,b)^\bullet)=(a^\bullet,b^\bullet).
\tag{MSA2}
\]

It is an injective unital semiring map: checking two supported inputs reduces both operations to the componentwise ring operations, and checking an absent input uses the identity or absorber. Injectivity follows separately on its absent point and its supported pairs. Define chi by chi(tau)=0 and chi(r^bullet)=1, with target the Boolean semiring. Then the exact image is

\[
\operatorname{im}j=G(A)\times_{\mathbb B}G(B)
=\{(u,v):\chi_A(u)=\chi_B(v)\}.
\tag{MSA3}
\]

The inverse on this image sends the pair of absent coordinates to tau and a pair of supported coordinates to the supported pair. The independent product also has the two entire mixed faces

\[
\{(a^\bullet,\tau):a\in A\},\qquad
\{(\tau,b^\bullet):b\in B\},
\tag{MSA4}
\]

which MSA2 does not cover. In particular the points (e_A,tau) and (tau,e_B) are distinct from both (tau,tau) and (e_A,e_B). This identifies the exact missing part of a synchronized product; it does not infer that the two products are unrelated. For n rings, the same formula gives an injection of G(product R_i) into product G(R_i), with image consisting precisely of the all-absent and all-present masks. The independent object has all 2^n masks.

## 2. The mixed coefficient algebra actually constructed in PS

`PACKET_SURVIVAL.tex:47–89` constructs a richer product on the independent carrier. Retain an actual full arithmetic packet

\[
h_Z(x)=\prod_{\rho\in Z}(x-\rho)^{m_\rho},\quad
E_Z=\mathbb C[x]/h_Z(x),\quad D_{E_Z,n}=G(E_Z)^n.
\tag{MSA5}
\]

The original spectral variable is x. The new coefficient variable t has the relation t^n+1=0. The negacyclic product and its original unit are

\[
(b\star c)_k=
\mathop{\bigoplus}_{i+j=k} b_i c_j\ \oplus\!
\mathop{\bigoplus}_{i+j=k+n}(-1)^\bullet b_i c_j,
\qquad 1_D=(1^\bullet,\tau,\ldots,\tau).
\tag{MSA6}
\]

All indices i,j,k lie between 0 and n−1. For b let A(b)={i:b_i is supported}. Then

\[
A(b+c)=A(b)\cup A(c),\qquad
A(b\star c)=A(b)+A(c)\quad\hbox{in }\mathbb Z/n\mathbb Z.
\tag{MSA7}
\]

For addition, an output is present exactly when at least one input is present. For the product, an output is present exactly when there is a pair of present input positions whose sum is its residue class. Every wrap factor is supported. The sum of any nonempty family of supported summands remains supported even if its ring coefficient is zero. This proves both equalities including empty masks and cancellation.

The amplitude map is

\[
\pi_n:D_{E_Z,n}\to B_n:=E_Z[t]/(t^n+1),\qquad
\pi_n(b)=\sum_{i=0}^{n-1}p(b_i)t^i.
\tag{MSA8}
\]

The monic relation gives the free E_Z basis 1,t,...,t^{n−1}; its inverse coordinate extraction determines every p(b_i). Adding the independent mask then determines each b_i, including whether a zero coefficient is e or tau. Hence b↦(A(b),pi_n(b)) is injective.

There is also an exact fibre count, useful for auditing what synchronization forgets. Write f=Σ c_i t^i and J(f)={i:c_i≠0}. The fibre pi_n^{-1}(f) consists of exactly one point for each A with J(f)⊆A⊆{0,...,n−1}. For a point indexed by A, slot i has value c_i^bullet when i∈A and tau otherwise. Therefore

\[
|\pi_n^{-1}(f)|=2^{n-|J(f)|}.
\tag{MSA9}
\]

This includes f=0, whose fibre has all 2^n masks.

Retain the synchronization idempotent

\[
\mathsf E_n=(1^\bullet,e,\ldots,e),\qquad s_n(b)=\mathsf E_n\star b.
\tag{MSA10}
\]

Its amplitude is 1. If b has a present slot j, then each output position k has a supported term using position k−j of E_n. Thus s_n fills every output slot while preserving all ring coefficients; it fixes the all-absent vector. This proves E_n²=E_n and identifies its image with G(B_n). Any unital semiring map sending E_n to an invertible element sends it to 1, since an invertible idempotent is 1; it therefore identifies b and E_n b. This proves the localization universal property

\[
D_{E_Z,n}[\mathsf E_n^{-1}]\simeq\mathsf E_nD_{E_Z,n}\simeq G(B_n).
\tag{MSA11}
\]

The image's unit is E_n. Its inclusion into D has precisely that unit image; it is not asserted to preserve 1_D. The exact fibres of s_n are

\[
s_n^{-1}(\tau)=\{(\tau,\ldots,\tau)\},\qquad
s_n^{-1}(f^\bullet)=\{A:J(f)\subseteq A,\ A\ne\varnothing\}.
\tag{MSA12}
\]

For f≠0 the second cardinality is 2^{n−|J(f)|}; for f=0 it is 2^n−1. The original mixed masks have therefore been calculated explicitly, and the full pair (mask, amplitude) reconstructs them exactly. Synchronization alone does not retain that pair.

## 3. What the current total-object definition actually includes

The current TO representation is generated in `total_object.tex:83–128` by the original arithmetic and two-leg complexes, all-polynomial transitions, and the finite polynomial, jet, conormal, cyclic, metric and source-label observations of AG and CAU. In `coherent_assembly.tex:481–529`, the source labels are a D-invariant W⊆V and a nonempty leg mask S⊆{+,−}. Those three leg masks are retained. External tensor words retain their specified vertices and coordinate permutations. AG27–36e retain all conormal depths, all tensor nilpotents, and their full-unit divisor maps.

In the three defining files read, there is **no explicit generating vertex** D_{E_Z,n}, no face diagram indexed by all coefficient masks in P({0,...,n−1}), and no arrow identifying that independent face diagram with the synchronization/localization MSA10–12. TO132–160 and AG770–802 apply a single split lift G(X) to each displayed vector-space vertex. Applying G to X=E_Z^n supplies its all-absent point and fully supported coefficient vectors. MSA2–4 prove the exact map to the independent product and display its omitted mixed faces. The CAU leg masks are indexed by two source legs; they do not specify the additional n coefficient masks of MSA5.

This is a precise integration omission in the defining represented category, not a claim that the mixed algebra was never built. PS supplies the full independent algebra and the Frobenius calculations below. The complete manuscript can contain that proof without its defining TO diagram having explicitly adjoined its vertices and face maps. The safe correction is to adjoin the existing PS object and the full face diagram, with their specified arithmetic maps; replacing independent masks by a single external G after forming a coefficient vector space is not that correction.

Here is the full linear and source-level attachment, so the correction does not stop at an instruction. For every n and A⊆{0,...,n−1}, define

\[
E_Z[A]=\bigoplus_{i\in A}E_Z,
\qquad C_U[A]=\bigoplus_{i\in A}[V\xrightarrow\Theta\mathscr B_U].
\tag{MSA13}
\]

For A⊆B use zero insertion in each missing coefficient slot, in every cochain degree. These are cochain maps because the differential acts independently in each coordinate. They compose by the literal zero-insertion formula. Reconstruct the mixed carrier as the disjoint union of its labelled faces, including one all-absent point for A empty. At degree one the internal quotient is

\[
\prod_{i=0}^{n-1}G(\mathscr B_U)
\longrightarrow\prod_{i=0}^{n-1}G(T_UQ),
\quad(F_i^\bullet)\longmapsto([F_i]^\bullet),
\tag{MSA14}
\]

with each absent input coordinate remaining absent. On face A its kernel over the supported zero is (Theta V)^A. Indeed a vector has zero quotient in every active coordinate exactly when every such F_i belongs to Theta V. Quotienting by those coordinatewise relations gives (T_UQ)^A. Equalizers and coequalizers remain within the fixed face A; cancellation changes coefficients without deleting that face.

Use the original finite section s_h:E_Z→B_U and injection sigma_h=q s_h, with the original full-unit convention from AG6–8. Then

\[
(s_h)^A:E_Z[A]\longrightarrow\mathscr B_U^A,
\quad(\sigma_h)^A:E_Z[A]\hookrightarrow(T_UQ)^A
\tag{MSA15}
\]

commute with all face inclusions. On each coordinate the exact failure of equivariance before the quotient is

\[
D s_h-s_h M_x=\Theta\phi_*\ell_h,
\quad\ell_h(u)=[x^{d_h-1}]r_h(\varepsilon_h u),
\quad\varepsilon_h=j_h(g/h)^{-1}.
\tag{MSA16}
\]

After q the right side is zero, proving equivariance of sigma_h on every independently supported face. The nilpotent coefficients, source boundary, and the full unit have not been discarded. MSA15 is a map of vector-space/support diagrams; the source function spaces have not been assigned an invented pointwise algebra structure making s_h a ring map. The negacyclic multiplication MSA6 remains at its actual finite arithmetic-algebra observation vertex. These precise arrows attach every independent mask to the existing original arithmetic carrier.

## 4. The mixed coefficient Frobenius and its exact arithmetic retract

`PACKET_SURVIVAL.tex:93–138` gives

\[
\iota_n:E_Z\to B_n,\ f\mapsto f,\qquad
r_n:B_n\to E_Z,\quad
r_n(b)=\frac1n\operatorname{Tr}_{B_n/E_Z}(M_b).
\tag{MSA17}
\]

For 1≤i<n, multiplication by t^i shifts every basis index by nonzero i modulo n, so has no diagonal entries. Its wrap entries retain the minus signs. Multiplication by b_0 has n identical diagonal entries b_0. Consequently Tr(M_{Σb_it^i})=n b_0, r_n(b)=b_0 and r_n iota_n=1. This gives the exact decomposition of E_Z-modules

\[
B_n=\iota_n E_Z\oplus\bigoplus_{i=1}^{n-1}E_Zt^i,
\qquad\ker r_n=\bigoplus_{i=1}^{n-1}E_Zt^i.
\tag{MSA18}
\]

The scalar factor 1/n is part of this retraction; no trace pairing has been rescaled. It lifts to the supported module retract and, through synchronization, carries f^bullet to (f^bullet,e,...,e).

For an odd prime power q with gcd(q,n)=1, the integral algebra map on Z[t]/(t^n+1) is Psi_q(t)=t^q. It is well-defined because (t^q)^n=−1. An r with q^r≡1 mod 2n gives Psi_q^r=1. In the original basis it is the signed permutation

\[
t^i\longmapsto(-1)^{\lfloor qi/n\rfloor}t^{qi\bmod n}.
\tag{MSA19}
\]

On D_{E_Z,n} it permutes precisely those coefficient slots and multiplies their supported values by the same signs, with absent values preserved. This carries mask A to qA modulo n, so every independent face is included. Both multiplication orders agree on supported monomials including their wrap sign; distributivity and the absorbing absent cases prove it is a semiring map. It fixes E_n and therefore commutes with MSA11. Reduction modulo the characteristic gives coefficient Frobenius; complex extension uses the same integral matrix. It follows that every complex eigenvalue of Psi_q is a root of unity and that Psi_q is diagonalizable, because X^r−1 has distinct roots over C.

The original arithmetic action on the rho-local packet is

\[
A_a|_{E_\rho}=a^\rho
\sum_{j=0}^{m_\rho-1}\frac{(\log a)^j}{j!}N_\rho^j,
\qquad N_\rho=M_{x-\rho}.
\tag{MSA20}
\]

Extend it coefficientwise to A_a^B on B_n. Psi_q is E_Z-linear, while A_a is multiplication by the full element j_h(a^s); hence they commute. The retraction obeys

\[
\Psi_q\iota_n=\iota_n,\quad r_n\Psi_q=r_n,
\quad A_a^B\iota_n=\iota_n A_a,\quad r_n A_a^B=A_a r_n.
\tag{MSA21}
\]

Thus the original arithmetic representation is an exact invariant retract of the mixed-coefficient construction. On a Psi_q eigenspace of eigenvalue omega the full joint action is

\[
\omega a^\rho\sum_{j=0}^{m_\rho-1}
\frac{(\log a)^j}{j!}N_\rho^j.
\tag{MSA22}
\]

For each rho, the original vector v_rho=e_rho(x−rho)^{m_rho−1} is nonzero, killed by N_rho, and has A_a eigenvalue a^rho. Its image under iota_n is nonzero by MSA17 and fixed by Psi_q. Its k-fold tensor over C remains nonzero: choose a linear functional taking v_rho to 1 and tensor that functional k times. For rho=1/2+delta+i gamma, the exact surviving modulus is

\[
\log\frac{|a^{k\rho}|^2}{a^k}=2k\delta\log a.
\tag{MSA23}
\]

MSA21–23 are the exact relation between finite coefficient purity and the original arithmetic weight. They prove that finite coefficient purity by itself has not bounded the arithmetic factor in this constructed object. This finding concerns the displayed construction; it does not establish failure of the wider tau-base programme or prevent additional geometric control on the same source.

## 5. The original two-leg chart and arithmetic support remain attached

The original NOTE164–188 constructs masks S in P({+,−}), with source legs present exactly according to S. Its reconstruction is tau disjoint union the labelled coefficient spaces. Its scalar epsilon keeps S and replaces its amplitude by zero. Its supported cohomology is calculated using Eq(d,epsilon d) and the boundary coequalizer; on a fixed mask these are the original vector-space cycle and quotient operations. Thus

\[
\widetilde H^1_\tau=\{\tau\}\sqcup
\coprod_{\varnothing\ne S\subseteq\{+,-\}}\{S\}\times Q,
\qquad Q=\mathscr B/\Theta V.
\tag{MSA24}
\]

The restriction to sigma has fibre {S}×Q over its labelled zero e_S. The external-absence fibre contains only tau. This concerns the original disjoint-union theta model; general split semimodules can have a nontrivial bottom group fibre, as NOTE563 explicitly states.

The arithmetic support is connected by a stronger amplitude map proved in CAU9–13:

\[
T_UQ\xrightarrow{\sim}\bigoplus_{\rho\in U:g(\rho)=0}
\mathcal O_\rho/(g),\qquad[F]\mapsto([\mathcal MF]_\rho)_\rho,
\quad U=\{0<\Re s<1,\ \Re s\ne1/2\}.
\tag{MSA25}
\]

Its complete inverse takes finitely many prescribed full jets alpha, forms h=product(x−rho)^{m_rho}, chooses the unique remainder P with j_hP=j_h(g/h)^{-1}alpha, and takes

\[
F_\alpha=S_h\Theta(P(D)\phi_*),\quad
\mathcal MF_\alpha=(g/h)P,
\quad\phi_*=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}.
\tag{MSA26}
\]

The supplied Euler range identity provides S_h on this exact moment-zero input. Changing P by hR changes F_alpha by the actual boundary Theta(R(D)phi_*). Conversely, a vanishing Mellin jet gives H_phi divisible by the original annihilator p; the original range identity gives phi=p(D)psi, and injectivity of p(D) on B gives F=Theta psi. This proves both inverse identities with every unit and multiplicity retained. In every independently supported coordinate, MSA25–26 and MSA15 give the map to the actual full local arithmetic jet, keeping its coefficient mask.

After balancing, CAU18–20 constructs an inclusion j:N_U→M and projection beta:M→N_U with beta j=1 and M=N_U⊕K, where N_U=O_U/(g). The joint complex has the displayed derived coordinates

\[
C_\tau\simeq\mathcal V_+[0]\oplus\mathcal N_U[-1]\oplus\mathcal K[-1].
\tag{MSA27}
\]

The degree-zero reversible coordinate map is u=phi−hat(psi), v=(phi+hat(psi))/2, with inverse phi=v+u/2, psi=hat(v)−hat(u)/2. The differential is Theta u. The comparison keeps N_U and has precisely V_+[0]⊕K[-1] as kernel complex. Thus there is a proved arithmetic support detector and an exact retained comparison kernel. Neither that detector nor the binary supported-zero lift can substitute for the mixed coefficient face diagram in sections 1–4.

## 6. Audit conclusion at the exact scope checked

The machinery built includes the full unsynchronized negacyclic mixed-support algebra, all coefficient masks, synchronization with its exact fibres, integral coefficient Frobenius, full arithmetic packet retract, theta-source intertwining, full nilpotent jets, and tensor amplification. The current TO defining category does not explicitly attach the independent coefficient face diagram; MSA13–16 gives its exact attachment.

The built finite coefficient Frobenius controls its own root-of-unity factors. The original arithmetic weight remains in the invariant retract MSA21, with the exact tensor growth MSA23. No theorem in the files audited forces the marked offcritical arithmetic support in MSA25 to be empty. An amplitude quotient, synchronization, finite coefficient purity, and a computation that a comparison kernel survives each have the explicit kernels and maps above. None supplies the missing arithmetic upper estimate by itself. The Deligne mixed-sheaf and weight-control comparison is being audited independently by the parent task; this file makes no claim to have audited that separate proof.

More specifically, the proved mask permutation MSA19 has no supplied identification in these sources with a weight filtration on the original arithmetic sheaf whose graded pieces satisfy two-sided arithmetic weight estimates. The computed chart adjunction NOTE27–30 supplies a right adjoint to its declared finite-poset section functor; its stated calculation does not assert those estimates. The invariant retract MSA21 is the strongest exact bridge available here between the coefficient-pure construction and the actual arithmetic representation: a weight estimate for the latter would have to hold on its unchanged eigenvector iota_n(v_rho). This inspection result identifies the missing geometric control assertion, rather than inferring a failure of the programme from a difference between presentations.

## Source pins at the audited state

- `total_object/total_object.tex`, 255 lines: SHA256 `7e1d84cae27e7dde708b892e21a586ad53216388224764a1bc70d94dd06a5191`.
- `total_object/coherent_assembly.tex`, 708 lines: SHA256 `39b51b6183993af1cbd431f984fd1a35a12fb8077294defe12433767ecc2784f`.
- `total_object/arithmetic_gluing.tex`, 810 lines: SHA256 `4203a3b119231058507741ce8376958da751460d2034b2477e028c33c8f38893`.
- `shared_thread_audit/segment16_28/PACKET_SURVIVAL.tex`, 342 lines: SHA256 `28a88d2155489a6c921c6b7533b15ca7ecb81cc2078ff1d49eed5467556c23eb`.
- `sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`, 611 lines: SHA256 `d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3`.
