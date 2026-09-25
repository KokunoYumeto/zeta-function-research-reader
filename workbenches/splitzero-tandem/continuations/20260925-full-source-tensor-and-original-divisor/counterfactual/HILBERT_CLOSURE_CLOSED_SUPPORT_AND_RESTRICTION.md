# The Hilbert closure defect on the actual closed support and restriction cross

25 September 2026. Independent derivation HCS0–HCS12.

## HCS0. Original objects, corpus check and sources

This calculation returns the whole-family critical-line Hilbert defect to the original sheaf, its entire arithmetic source, its supported localization sequence, and its continuous restriction extension. It computes the resulting supported cyclic map before taking any Hausdorff quotient. A second, intermediate cone records both directions of the comparison with the original residue cone.

The complete user passages USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2 and USR-6152e3bc6302258c, the operation rule USR-4322be19bff532cd and its forward-calculation amendment USR-64a88219a3ecddd3 were reread in the retained private corpus. The current corpus rules (private construction record; not distributed) govern the calculation. Source notation remains \(Z_0,Z_1/\tau,Z_2\). Primitive \(\tau\) has neither addition nor parity; the retracted self-sum is not used. All additions, duals, Hilbert completions and polynomial operations below belong to the already constructed complex receiving spaces. Arithmetic reconstruction precedes these operations. None of the calculated receiver kernels contradicts the user's prior whole-spectrum construction.

Human sources are Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), for the coefficient sheaf and Fourier restrictions; Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068v1, §III and Appendix I](https://arxiv.org/abs/math/9811068v1), for the weighted Hilbert spectral realization; Ralf Meyer, [*A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3), for the full closed-image realization; and Pierre Deligne, [*La conjecture de Weil. II*, §§3.6.1–3.6.3, pp.213–214](https://www.numdam.org/item/PMIHES_1980__52__137_0/), for the restriction/closed-support cross whose weights give his lifting result.

Actual reading for this derivation comprised all of [ORE0–ORE10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_RESTRICTION_EXTENSION_AND_DELIGNE_CROSS.md), [SCT0–SCT6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SUPPORTED_COMPARISON_QUOTIENT_TRIANGLE.md), the original supported localization in [ASD5–ASD6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ACTUAL_SUPPORTED_DUALITY_INDEPENDENT.md), and the full closure-return sequence in [VWR6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/FULL_VERTICAL_WEIGHT_RETURN.md). Deligne's retained French transcription [S20_FR_record_export.tex](https://www.numdam.org/item/PMIHES_1980__52__137_0/), lines2468–2595, is the source passage used; it is a transcription, not author TeX. Its retained SHA256 is d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351. This is not a claim to have freshly read all four human works in this bounded calculation.

The other exact programme inputs are [OMS](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), [GZR](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md), [SCL](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SPECTRAL_COKERNEL_DIVISIBILITY_AND_FINITE_LIFTING.md), [WHR](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/WEIGHTED_HILBERT_RETURN_AND_EXACT_KERNEL.md), and [VWR0–VWR10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/FULL_VERTICAL_WEIGHT_RETURN.md). Their full proofs remain dependencies of this note. No finite list of zeros substitutes for the global closure theorem.

## HCS1. The original coefficient spaces and the precise closure pullback

Keep
\[
S=\{h\in\mathcal S(\mathbb R;\mathbb C):
h(-v)=h(v),\ h(0)=0,\ \int_{\mathbb R}h(v)\,dv=0\},
\]
\[
A=\{b\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jb(u)|<\infty
\text{ for all integers }N,j\ge0\}.
\tag{HCS1.1}
\]
The original maps are
\[
\Sigma h(u)=2\sum_{n\ge1}h(nu),\qquad
\mathcal M_0b(s)=\int_0^\infty b(u)u^s\,\frac{du}{u},
\qquad Rb(u)=u^{-1}b(u^{-1}).
\tag{HCS1.2}
\]
Write \(J=\Sigma S\), \(Q=A/J\), and \(\pi:A\to Q\). The established closed-image theorem is used with its full inverse on \(S\), not just with necessary zero conditions. In the original Mellin image \(\mathcal B=\mathcal M_0A\),
\[
\mathcal M_0J=I
=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for every nontrivial zero }\rho
\text{ and }0\le j<m_\rho\}.
\tag{HCS1.3}
\]
Every actual multiplicity \(m_\rho\) is retained. The original identity is
\[
\mathcal M_0\Sigma h(s)=2\zeta(s)\mathcal M_Sh(s),\qquad
\mathcal M_Sh(s)=\int_0^\infty h(v)v^s\,\frac{dv}{v}.
\tag{HCS1.4}
\]
It is first absolute in \(\Re s>1\); OMS proves its full meromorphic continuation, including the endpoint constraints, the original pole and the trivial-zero division. Nothing here replaces \(\zeta\) by its completion.

For \(\delta>0\), define the actual receiver
\[
\mathcal H_\delta=L^2\!\left((0,\infty),
(1+\log^2u)^\delta\,du\right),\quad
C_\delta=\overline J^{\,\mathcal H_\delta},\quad
B_\delta=A\cap C_\delta,\quad Q_\delta=\mathcal H_\delta/C_\delta.
\tag{HCS1.5}
\]
The closure theorem WHR5 gives, on the original \(A\),
\[
B_\delta=\{b\in A:
(\mathcal M_0b)^{(j)}(\rho)=0
\text{ whenever }\Re\rho=\tfrac12,\
0\le j<m_\rho,\ j<\delta-\tfrac12\}.
\tag{HCS1.6}
\]
In particular \(B_\delta\) is closed in \(A\). The whole critical-line family, rather than any one finite weight, gives
\[
B_{\rm off}=\bigcap_{N\ge1}B_N
=\mathcal M_0^{-1}I_{\rm line},\qquad
K_{\rm off}=B_{\rm off}/J,
\tag{HCS1.7}
\]
where \(I_{\rm line}\) imposes every jet below the full multiplicity at every critical-line zero. The intersection is closed; \(B_{\rm off}\) and \(K_{\rm off}\) carry their inherited Fréchet and quotient Fréchet topologies. There is no identification of \(B_{\rm off}\) with \(B_\delta\) at a fixed finite \(\delta\).

The topology has three points
\(\mathcal Y=\{c_+,c_-,\eta\}\), minimal opens
\(U_\pm=\{c_\pm,\eta\}\), and open overlap \(\{\eta\}\).
Write the original closed stalks as \(W_\pm\), retaining both endpoint pairs and their full extra closed copies. Thus
\[
P=W_+\oplus W_-=(S\oplus\mathbb C^2)\oplus
(S\oplus\mathbb C^2)\oplus V_{\rm extra},\qquad
E=\mathbb C^4\oplus V_{\rm extra}.
\]
Their restrictions are \(r_+=\Sigma\), \(r_-=R\Sigma\) on their \(S\) coordinates, and zero on every endpoint and extra coordinate. Put
\[
d=r_+-r_-,\qquad d_Z=(r_+,r_-),\qquad H=\ker(d:P\to A).
\tag{HCS1.8}
\]
The full sheaf is \(\mathcal F_A=(W_+\to A\leftarrow W_-)\).
Since both restrictions have image \(J\), they also define actual sheaves
\(\mathcal F_{B_\delta},\mathcal F_{C_\delta},
\mathcal F_{\mathcal H_\delta}\).
The square
\[
\begin{array}{ccc}
\mathcal F_{B_\delta}&\longrightarrow&\mathcal F_A\\
\downarrow&&\downarrow\\
\mathcal F_{C_\delta}&\longrightarrow&\mathcal F_{\mathcal H_\delta}
\end{array}
\tag{HCS1.9}
\]
is cartesian: its closed-stalk squares are identities and its generic-stalk square is exactly
\(B_\delta=A\cap C_\delta\).
The inverse image of the full family of closure sheaves is
\(\mathcal F_{B_{\rm off}}=\bigcap_N\mathcal F_{B_N}\) inside
\(\mathcal F_A\). This constructs the source of the full defect without replacing the original \(Q\) by any Hausdorff quotient.

## HCS2. Closed support retains the whole defect, with every endpoint

For each of the actual spaces \(B=B_\delta\) and \(B=B_{\rm off}\), write \(K=B/J\), and retain \(Z=\{c_+,c_-\}\). The two-open complexes are
\[
R\Gamma(\mathcal Y,\mathcal F_B)=[P\xrightarrow d B],
\qquad
R\Gamma_Z(\mathcal Y,\mathcal F_B)
=[P\xrightarrow{d_Z}B^2]
\tag{HCS2.1}
\]
in degrees0,1. The second complex follows also by taking the mapping fibre of restriction to the generic point. Its map to the first is identity on \(P\), and
\((b_+,b_-)\mapsto b_+-b_-\) in degree1.

Both \(r_+\) and \(r_-\) are onto \(J\). Therefore
\(\operatorname{im}d=J\) and \(\operatorname{im}d_Z=J^2\).
The first kernel is exactly the existing Fourier graph \(H\), and the second kernel is \(E\): each \(S\) restriction is injective while its endpoint and extra coordinates restrict to zero. Hence
\[
H^0\mathcal F_B=H,\quad H^1\mathcal F_B=K,\quad
H_Z^0\mathcal F_B=E,\quad H_Z^1\mathcal F_B=K^2.
\tag{HCS2.2}
\]
All higher groups vanish. The full localization sequence, including its maps, is
\[
\boxed{
0\to E\to H\xrightarrow{\ \Sigma\ }B
\xrightarrow{\,b\mapsto([b],[b])\,}K^2
\xrightarrow{(k_+,k_-)\mapsto k_+-k_-}K\to0.}
\tag{HCS2.3}
\]
Here \(\Sigma\) means the common restriction of the Fourier-graph coordinate; it kills \(E\). Exactness can be checked without a derived formalism: its image is \(J\); the kernel of the diagonal quotient is \(J\); the kernel of the difference is the diagonal \(K\); and difference is onto.

The last map has the continuous, original-dilation-equivariant section
\[
k\longmapsto(k/2,-k/2).
\tag{HCS2.4}
\]
This proves precisely that closed support contains the entire \(K_{\rm off}\) when \(B=B_{\rm off}\), with an explicit return to it. It does not assert that its presence proves nonzero \(K_{\rm off}\). It computes the map for the actual, possibly zero, space. None of its classes is removed by a supported localization kernel.

For the generic extension by zero \(\mathcal N_B=j_{\eta!}B=(0\to B\leftarrow0)\), the same complexes are
\[
R\Gamma\mathcal N_B=[0\to B],\qquad
R\Gamma_Z\mathcal N_B=[0\to B^2].
\]
Their localization sequence is exactly
\[
0\to B\xrightarrow{\rm diagonal}B^2
\xrightarrow{\rm difference}B\to0.
\tag{HCS2.5}
\]
Thus zero closed stalks do not imply zero higher cohomology with closed support. This calculation, rather than a stalk-only argument, is required for the closure defect sheaf.

## HCS3. The complete closure ladder before Hausdorffization

At finite \(\delta\) the actual sheaf sequence is
\[
0\to j_{\eta!}C_\delta\to\mathcal F_{\mathcal H_\delta}
\to\overline{\mathcal F}_\delta\to0,\qquad
\overline{\mathcal F}_\delta
=(W_+\xrightarrow0Q_\delta\xleftarrow0W_-).
\tag{HCS3.1}
\]
It is exact on each stalk, which proves exactness of sheaves. Its global and supported complexes give the complete rows
\[
0\to H\to P\xrightarrow d C_\delta
\to\mathcal H_\delta/J\to Q_\delta\to0,
\tag{HCS3.2}
\]
\[
0\to E\to P\xrightarrow{d_Z}C_\delta^2
\to(\mathcal H_\delta/J)^2\to Q_\delta^2\to0.
\tag{HCS3.3}
\]
The generic row is \(0\to C_\delta\to\mathcal H_\delta\to Q_\delta\to0\).
These rows form a morphism of localization sequences: the maps from generic degree0 to supported degree1 are diagonal, and the supported-to-global degree1 maps are difference. For example, the two global connecting restrictions in the ladder are \(d\) and \(d_Z\), not zero; they have the original \(-\) sign in \(d\) and both \(+\) signs in \(d_Z\).

The algebraic cohomology is \(\mathcal H_\delta/J\). Its subsequent Hausdorffization is the distinct quotient
\[
0\to C_\delta/J\to\mathcal H_\delta/J\to Q_\delta\to0.
\tag{HCS3.4}
\]
The original \(Q\to\mathcal H_\delta/J\) is injective, because \(A\to\mathcal H_\delta\) is injective and \(J\) has not changed. The kernel appears only in \(Q\to Q_\delta\), and its exact value is \(B_\delta/J\). This follows immediately by pulling back \(C_\delta\) to \(A\); it is the sheaf pullback HCS1.9, not an identification imposed afterward.

For the whole critical family put
\[
B=B_{\rm off},\quad K=K_{\rm off},\quad V=Q/K\simeq A/B.
\tag{HCS3.5}
\]
There are two useful distinct exact sequences on the original source sheaf:
\[
0\to\mathcal F_B\to\mathcal F_A\to j_{\eta!}(A/B)\to0,
\tag{HCS3.6}
\]
\[
0\to j_{\eta!}B\to\mathcal F_A\to
\mathcal F_{\rm vis}\to0,\qquad
\mathcal F_{\rm vis}=(W_+\xrightarrow0A/B\xleftarrow0W_-).
\tag{HCS3.7}
\]
They are proved by their displayed stalks and restrictions. HCS3.6 gives the exact sequence \(0\to K\to Q\to V\to0\). HCS3.7 gives
\[
0\to H\to P\xrightarrow d B\to Q\to V\to0,
\qquad
0\to E\to P\xrightarrow{d_Z}B^2\to Q^2\to V^2\to0.
\tag{HCS3.8}
\]
The image of \(B\to Q\) is exactly \(K\). Consequently the entire off-critical kernel is already an image in the original sheaf's connecting sequence. Taking a Hilbert closure neither constructs nor destroys that original subspace; it specifies the later receiver that kills it.

## HCS4. Exact return to every arithmetic source point

The existing source is \(X^{\rm dbl}=U\cup\{m_+,m_-\}\), with \(U=\operatorname{Spec}\mathbb Z\). Its topology retains every nonempty ordinary open of \(U\), \(X_\pm=U\cup\{m_\pm\}\), and \(X^{\rm dbl}\). The proved source map is
\[
f:X^{\rm dbl}\to\mathcal Y,\qquad
f(U)=\eta,\quad f(m_\pm)=c_\pm.
\tag{HCS4.1}
\]
No arithmetic point of \(U\) is identified with another in \(X^{\rm dbl}\); \(f\) is the already specified receiving map, with its whole fibre retained.

Pull back every sheaf and every map in HCS1–HCS3 by \(f^{-1}\). This functor is exact, so the stalkwise sequences remain exact. On \(U\) these are constant sheaves with their displayed coefficient spaces. Every nonempty open of \(U\) is irreducible and connected; its locally constant sections are constant, and restrictions between nonempty opens are identity maps. Such a constant sheaf is flabby and has no higher cohomology on \(U\).

Every neighbourhood of \(m_+\) in \(X_+\) is \(X_+\) itself. Thus sections on \(X_+\) are the stalk at \(m_+\), an exact functor on sheaves of vector spaces; it has no higher derived functors. The same holds for \(X_-\). It follows directly that the cover \(X_+,X_-\), with overlap \(U\), computes all displayed global and supported cohomology. This is the original complex on \(P,B\), or \(P,B^2\), with every point of \(U\) still present. No unproved proper-base-change claim is used.

With closed support \(Z_X=\{m_+,m_-\}\), the localization rows are exactly HCS2.3 and HCS3.8. Also
\[
f^{-1}j_{\eta!}B=j_{U!}\underline B.
\tag{HCS4.2}
\]
This follows from the common stalks (coefficient \(B\) on all of \(U\), zero at \(m_\pm\)) and the same zero boundary restrictions. Its supported degree-one group is still \(B^2\), not zero.

The receiving coefficient ring remains the previously constructed \(\mathbb Z^3\), with \([\tau]=(1,1,1)\) and \([n]=(n,0,0)\). The retained extra closed copies record the other two scalar coordinates. All new maps are identities on those full copies or zero only where the original restrictions were already zero. Nothing here identifies primitive source \(\tau\) with integer \(1\), a scalar zero, or a parity state.

## HCS5. The actual pushout of the original restriction extension

From now on \(B=B_{\rm off}\), \(K=K_{\rm off}\), \(V=Q/K\). All duals are continuous duals; the exact sequences have their weak-* topologies, and every transpose is also continuous for the strong dual topology.

Write \(\chi_{\rm dil}(a)=a\) and
\[
Y=\chi_{\rm dil}Q',\quad
Y_K=\chi_{\rm dil}K',\quad
Y_{\rm vis}=\chi_{\rm dil}V',\quad
\widetilde A=\chi_{\rm dil}A',\quad
\widetilde B=\chi_{\rm dil}B',\quad
\widetilde S=\chi_{\rm dil}S'.
\]
The action is \(a(T_{a^{-1}})'\), with generator \(G=1-L^t\); \(L=-u\partial_u\) on \(A,B,Q,K\). The original parameter has not been shifted on the primal spaces.

Because \(J\) is closed in \(B\), and \(\Sigma:S\to J\) is a topological isomorphism, every continuous functional on \(S\) extends first to \(J\) and then to \(B\) by Hahn–Banach. A functional on \(B\) annihilates \(J\) exactly when it factors continuously through \(K\). Thus
\[
0\to Y_K\xrightarrow{i_B=\pi_B'}\widetilde B
\xrightarrow{\Sigma_B'}\widetilde S\to0
\tag{HCS5.1}
\]
is an actual exact extension, where \(\pi_B:B\to K\).
Restriction of continuous functionals gives the commutative diagram
\[
\begin{array}{ccccccccc}
0&\to&Y&\xrightarrow{\pi'}&\widetilde A&
\xrightarrow{\Sigma'}&\widetilde S&\to&0\\
&&\downarrow r_K&&\downarrow\iota'&&\Vert\\
0&\to&Y_K&\xrightarrow{\pi_B'}&\widetilde B&
\xrightarrow{\Sigma_B'}&\widetilde S&\to&0.
\end{array}
\tag{HCS5.2}
\]
Here \(\iota:B\hookrightarrow A\), and \(r_K\) restricts \(Q'\) to \(K\).
Both downward maps are onto by Hahn–Banach on the closed subspaces. Their kernels identify with the same \(Y_{\rm vis}\): a functional on \(A\) vanishes on \(B\) exactly when it factors through \(A/B=V\); a functional on \(Q\) vanishes on \(K\) exactly when it factors through \(Q/K=V\). The original injection \(\pi'\) identifies those kernels. Consequently the bottom row is precisely the pushout of the top row by \(r_K\). This proves the extension comparison, rather than merely asserting similarity of the two restrictions.

Dualizing HCS2.3 gives the full supported restriction cross
\[
0\to Y_K\xrightarrow{y\mapsto(y,-y)}Y_K^2
\xrightarrow{(y_+,y_-)\mapsto\pi_B'(y_++y_-)}
\widetilde B\to\chi_{\rm dil}H'
\to\chi_{\rm dil}E'\to0.
\tag{HCS5.3}
\]
The map from \(\widetilde B\) has Schwartz coordinate \(\Sigma_B'\) and zero endpoint/extra coordinates. The last map is restriction to \(E\). Exactness of this dual row follows also directly from Hahn–Banach on each closed image in HCS2.3. In particular the entire endpoint and extra part remains, with its original action.

For a nonzero polynomial \(q\), the operator \(q(G)\) is onto on \(\widetilde B\). Here are its prerequisites. On the original Mellin space \(I_{\rm line}\), the transpose's primal operator is multiplication by \(p(s)=q(1-s)\). It is injective. At a root \(\lambda\) of \(p\) of order \(r_\lambda\), membership in its image requires vanishing to order \(r_\lambda+m_\lambda\) if \(\lambda\) is a critical-line zero, and order \(r_\lambda\) otherwise; the original \(I_{\rm line}\) conditions at every other zero remain. These are finitely many additional continuous jet conditions, so the image is closed. Division by \(p\) is continuous there: away from small root discs it follows from the original strip seminorms and the reciprocal polynomial bound; inside each disc, Cauchy's formula on a slightly larger disc controls the divided holomorphic function and its derivatives. The prescribed vanishing makes that quotient remain in \(I_{\rm line}\). Its continuous inverse transports a functional on \(B\) to this closed image, and Hahn–Banach extends it to \(B\). Transposing gives the claimed surjectivity.

Publication source credit: Human-source attribution: the extension of continuous linear functionals is the Hahn–Banach theorem, not a programme result. See Terence Tao, [245B, Notes6: Duality and the Hahn–Banach theorem](https://terrytao.wordpress.com/2009/01/26/245b-notes-6-duality-and-the-hahn-banach-theorem/), Theorem1 and its complex proof (26 January2009). For the locally convex use here, continuity bounds a functional by a continuous seminorm; quotienting its kernel reduces this application to that normed-space theorem. No continuous splitting of the original quotient is thereby asserted.

The same closed-division argument for \(A\), and the original source Schwartz argument in ORE3, give surjectivity on \(\widetilde A,\widetilde S\). These are continuous-dual facts in the stated topology, not assumptions of an algebraic dual replacement.

## HCS6. The full residue return on the defect and its polynomial cokernel

The retained original form is
\[
\mathcal B_\zeta([b],[c])=
\frac1{2\pi i}
\left(\int_{\Re s=2}^{\uparrow}
-\int_{\Re s=-1}^{\uparrow}\right)
\frac{(\mathcal M_0b)(s)(\mathcal M_0c)(1-s)}{\zeta(s)}\,ds.
\tag{HCS6.1}
\]
GZR proves absolute convergence, descent, continuity and two-sided nondegeneracy on \(Q\). VWR8 proves that its restriction to \(K\times K\) is also two-sided nondegenerate, by the actual entire isolators at reflected off-critical zeros. Write
\[
D_\zeta:Q\to Y,\qquad
D_K:K\to Y_K,\qquad
\boxed{D_K=r_KD_\zeta\iota_K,}
\tag{HCS6.2}
\]
where \(\iota_K:K\hookrightarrow Q\). The identity follows by evaluating both sides at every \(k\in K\). Both maps are injective, continuous and intertwine all original \(T_a\), since
\(\mathcal B_\zeta(T_ax,T_ay)=a\mathcal B_\zeta(x,y)\).
The character \(a\) has numerical Deligne weight2; it is not a weight-one statement about either input and does not give a numerical weight to \(\tau\).

For clarity, the primary decomposition used below is finite for each polynomial. The original exact isolators give continuous primary projectors \(P_\rho\) onto each full block
\(\mathbb C[t]/(t^{m_\rho})\) in \(Q\).
At an off-critical zero every vector in this block belongs to \(K\), because its full jets at every critical-line zero vanish. At a critical-line zero \(P_\rho K=0\), by the defining equations for \(B\).
The original inverse of \(L-\rho\) on the complementary kernel of \(P_\rho\) commutes with every other \(P_\lambda\). Indeed the projector and \(L\) commute, and uniqueness of the inverse gives their commutation. Thus that inverse preserves the simultaneous kernel of all critical-line projectors, which is \(K\). The same argument passes to \(V=Q/K\). It follows that the primary blocks of \(K\) are exactly the full off-critical blocks, and those of \(V\) exactly the full critical-line blocks. Their complementary polynomial operators are invertible. No infinite sum of projectors is used.

Let
\[
C_K=Y_K/D_KK.
\tag{HCS6.3}
\]
Every nonzero polynomial \(q(G)\) is bijective on \(C_K\). To prove this, take the finite set of roots of \(q\) and the finite set of reflected roots required on the dual. The preceding projectors decompose \(K\) and \(Y_K\) into their finite primary parts and their complementary parts. On each retained primary part, HCS6.1 is the full residue pairing between reflected blocks and is nondegenerate; \(D_K\) is therefore an isomorphism onto that dual primary part. On the complementary parts \(q\) and its inverse act continuously. Intertwining implies that the inverse preserves \(D_KK\). Hence the primary quotient is zero and \(q\) is invertible on the complementary quotient, proving the assertion for all of \(C_K\). This does not assert \(C_K=0\), or surjectivity of \(D_K\).

This argument applies to the full \(K_{\rm off}\), not automatically to \(K_\delta=B_\delta/J\). For example at a critical-line block of multiplicity \(m\), let \(r\) be the number of jets retained by HCS1.6, capped at \(m\). The corresponding part of \(K_\delta\) is \(t^r\mathbb C[t]/(t^m)\). Pairing it with its reflected counterpart, the exact residue radical is
\[
t^{\max(r,m-r)}\mathbb C[t]/(t^m).
\tag{HCS6.4}
\]
Indeed a nonzero element of leading order \(k\ge r\) pairs nontrivially with an allowed leading order \(m-1-k\) precisely when \(m-1-k\ge r\); the nonzero original residue unit does not alter this triangular criterion. Thus the radical condition is \(k+r\ge m\). In particular a finite-\(\delta\) restricted cone can have nonzero degree-zero cohomology. It would be incorrect to apply the full-\(K_{\rm off}\) injectivity theorem to it without this calculation.

## HCS7. The complete restricted cyclic connecting map

Let \(\mathcal R=\mathbb C[X]\), with \(X=G\), and \(V_q=\mathcal R/(q)\).
Its explicit free resolution gives
\(\operatorname{Ext}^1_{\mathcal R}(V_q,Y_K)=Y_K/qY_K\).
For \(\eta\in\ker(q:\widetilde S\to\widetilde S)\), choose
\(\alpha_B\in\widetilde B\) with \(\Sigma_B'\alpha_B=\eta\).
Then \(q\alpha_B=\pi_B'y_B\) uniquely for \(y_B\in Y_K\), and
\[
\delta_q^K(\eta)=[y_B]\in Y_K/qY_K.
\tag{HCS7.1}
\]
Changing the lift changes \(y_B\) by \(qY_K\). Restricting any original lift in \(\widetilde A\) proves the exact naturality formula
\[
\boxed{\delta_q^K=(r_K\bmod q)\,\delta_q.}
\tag{HCS7.2}
\]
Surjectivity of \(q\) on \(\widetilde B\) proves the full row
\[
0\to\ker q_{Y_K}\to\ker q_{\widetilde B}
\xrightarrow{\Sigma_B'}\ker q_{\widetilde S}
\xrightarrow{\delta_q^K}Y_K/qY_K\to0.
\tag{HCS7.3}
\]

Here is its value with every original constant. At an actual nontrivial zero \(\rho\), of full multiplicity \(m\), put \(b=1-\rho\), \(N=G-b\), \(q=N^r\), \(r\ge1\). Use the raw original evaluations
\[
A_j(c)=(\mathcal M_0c)^{(j)}(\rho),\qquad
S_j(h)=(\mathcal M_Sh)^{(j)}(\rho).
\]
Write \(A_j^B=A_j|_B\). They satisfy
\[
\Sigma_B'A_j^B=
2\sum_{k=0}^j{j\choose k}\zeta^{(k)}(\rho)S_{j-k},
\quad NA_j^B=-jA_{j-1}^B,\quad NS_j=-jS_{j-1}.
\tag{HCS7.4}
\]
The full prime action is
\[
T_a^{\rm dual}A_j^B
=a^{1-\rho}\sum_{\ell=0}^j{j\choose\ell}
(-\log a)^{j-\ell}A_\ell^B,
\tag{HCS7.5}
\]
and the same formula holds for \(S_j\).
Put
\[
\zeta(\rho+t)=t^m u_\rho(t),\qquad
\frac1{2u_\rho(t)}=\sum_{k\ge0}v_kt^k,\qquad
v_0=\frac{m!}{2\zeta^{(m)}(\rho)}.
\]
The exact reciprocal identity determines every \(v_k\), retaining all higher derivatives of the original \(\zeta\). The lifts
\[
\alpha_j^B=j!\sum_{k=0}^j
v_k\frac{A_{m+j-k}^B}{(m+j-k)!}
\quad\text{satisfy}\quad\Sigma_B'\alpha_j^B=S_j.
\tag{HCS7.6}
\]
This follows by multiplying the Taylor series
\(2t^m u_\rho(t)\) by its displayed reciprocal and comparing every coefficient, equivalently substituting HCS7.4.
Their exact residual is
\[
N^r\alpha_j^B=(-1)^rj!\!
\sum_{\substack{0\le k\le j\\m+j-k-r\ge0}}
v_k\frac{A_{m+j-k-r}^B}{(m+j-k-r)!}.
\tag{HCS7.7}
\]
For \(0\le j<r\), every surviving index is less than \(m\).

If \(\Re\rho=1/2\), all those low evaluations on \(B\) are zero. Thus
\[
N^r\alpha_j^B=0,\qquad \delta_q^K(S_j)=0.
\tag{HCS7.8}
\]
This is an explicit fixed-order lift, not an inference from a Hilbert-space spectral slogan. In fact
\[
N\alpha_j^B=-j\alpha_{j-1}^B
-j!v_j A_{m-1}^B/(m-1)!
=-j\alpha_{j-1}^B.
\tag{HCS7.9}
\]
For \(j=0\) the first term is interpreted as zero, and the second is also zero. Hence the entire finite source chain lifts equivariantly. Uniqueness among \(q\)-annihilated lifts follows from invertibility of \(q\) on \(Y_K\) at this critical parameter, proved in HCS6.

If \(\Re\rho\ne1/2\), the full low jet block remains on \(B\). Arbitrary finite higher jets at \(\rho\) can also be prescribed in \(B\): start with the entire isolator \(E_{\rho,0}\), which is a unit at \(\rho\) and vanishes to full multiplicity at every other zero, and multiply it by the finite Taylor polynomial of the desired jet divided by that unit. A polynomial multiplier preserves \(\mathcal B\). All critical-line conditions remain satisfied. Thus no \(A_0^B,\ldots,A_{m+r-1}^B\) is lost through the restriction. The exact original triangular extension remains.

Via the isomorphism induced by \(D_K\) modulo \(q\), the value is
\[
\boxed{
(D_K\bmod q)^{-1}\delta_q^K(S_j)=
\left[
\frac{(-1)^j j!}{2}\,t^{r-1-j}
\pi^{b+t-1/2}
\frac{\Gamma((1-b-t)/2)}{\Gamma((b+t)/2)}
\right]_{\mathbb C[t]/(t^{\min(m,r)})}.}
\tag{HCS7.10}
\]
Here \(t=L_K-b\). This is the actual ORE5 residue computation restricted to the same full primary block; HCS5.2 and HCS6.2 prove equality of its maps before it is used. The factor \(1/2\) comes from the original \(2\) in \(\Sigma\). The Gamma ratio is the original functional-equation multiplier
\(\chi_\zeta(b+t)\), retained with every derivative. It is holomorphic and nonzero in this germ. Consequently the map on this source chain has rank \(\min(m,r)\). For a general polynomial \(q\), the Chinese remainder decomposition over its finitely many roots and the displayed connecting construction give the whole map. Its nontrivial primary values occur exactly on the surviving off-critical blocks; no hypothesis about their existence is imposed.

## HCS8. The exact cone span, without reversing a dual restriction

Set
\[
\Psi_A=\pi'D_\zeta\pi:A\to\widetilde A,\qquad
\Psi_B=\pi_B'D_K\pi_B:B\to\widetilde B.
\]
Direct evaluation gives
\[
\boxed{\Psi_B=\iota'\Psi_A\iota.}
\tag{HCS8.1}
\]
Thus the new pairing is the restriction of the actual original product pairing to both coefficient inputs. The dual map has direction \(\widetilde A\to\widetilde B\). There is no chosen equivariant extension \(\widetilde B\to\widetilde A\).

In degrees \(-1,0,1,2\), define the actual restricted cones
\[
K_B=[P\xrightarrow{-d}B\xrightarrow{\Psi_B}
\widetilde B\xrightarrow{d_B'}\chi_{\rm dil}P'],
\]
\[
L_B=[P\xrightarrow{-d}B\xrightarrow{(\Psi_B,-\Psi_B)}
\widetilde B^2\xrightarrow{d_{Z,B}'}\chi_{\rm dil}P'].
\tag{HCS8.2}
\]
The final differentials, with both endpoint pairs and the whole extra term, are
\[
d_B'\alpha=(\Sigma_B'\alpha,0,0,
-\Sigma_B'R_B'\alpha,0,0,0_{\rm extra}),
\]
\[
d_{Z,B}'(\alpha_+,\alpha_-)
=(\Sigma_B'\alpha_+,0,0,
\Sigma_B'R_B'\alpha_-,0,0,0_{\rm extra}).
\tag{HCS8.3}
\]
Here \(R_B\) is the actual restriction of \(R\); it preserves \(B\) by the reflected full critical-line conditions. All consecutive differentials vanish, since \(\Psi_B\) factors through \(K\) and lands in the annihilator of \(J\).

To compare with the original cones \(K_A=K_\zeta,L_A=L_\zeta\) in both directions, use the intermediate, explicitly constructed complexes
\[
K_\times=[P\xrightarrow{-d}B\xrightarrow{\Psi_A\iota}
\widetilde A\xrightarrow{d_A'}\chi_{\rm dil}P'],
\]
\[
L_\times=[P\xrightarrow{-d}B
\xrightarrow{(\Psi_A\iota,-\Psi_A\iota)}
\widetilde A^2\xrightarrow{d_{Z,A}'}
\chi_{\rm dil}P'].
\tag{HCS8.4}
\]
The exact span of cochain maps is
\[
\begin{array}{ccccc}
K_A&\longleftarrow&K_\times&\longrightarrow&K_B\\
\downarrow\mathcal J_A&&\downarrow\mathcal J_\times&&
\downarrow\mathcal J_B\\
L_A&\longleftarrow&L_\times&\longrightarrow&L_B .
\end{array}
\tag{HCS8.5}
\]
Leftward maps are \((1,\iota,1,1)\) degree by degree, and rightward maps are \((1,1,\iota',1)\), with \((\iota')^2\) in degree1 on \(L_\times\). The vertical maps are identity except for the anti-diagonal \(\alpha\mapsto(\alpha,-\alpha)\) in degree1. Equation HCS8.1 checks the middle square. The last squares follow from \(d_B'\iota'=d_A'\) and \(d_{Z,B}'(\iota')^2=d_{Z,A}'\), since every restriction already lands in \(B\).

Each column has a degreewise exact quotient triangle
\[
0\to K_\bullet\xrightarrow{\mathcal J_\bullet}L_\bullet
\xrightarrow{\nu_\bullet}\widetilde D_\bullet[-1]\to0,
\tag{HCS8.6}
\]
where \(\widetilde D_A=\widetilde D_\times=\widetilde A\),
\(\widetilde D_B=\widetilde B\), and
\(\nu(\alpha_+,\alpha_-)=\alpha_++\alpha_-\).
The quotient arrows in the span are identity leftward and \(\iota'\) rightward. Each graded section is
\(\sigma\alpha=(\alpha/2,\alpha/2)\), and its connecting cochain is
\[
\theta_\bullet\alpha=
(\Sigma_\bullet'\alpha/2,0,0,
\Sigma_\bullet'R_\bullet'\alpha/2,0,0,0_{\rm extra}).
\tag{HCS8.7}
\]
For the intermediate term the restrictions in this formula are the original ones. Substitution proves \(d_L\sigma=\mathcal J\theta\); every map in the span commutes with it. The explicit SCT2 contraction therefore remains a contraction of each corresponding identity-cone kernel, with no endpoint or extra term discarded.

## HCS9. Complete ordinary cohomology and the two exact cokernel maps

Define
\[
T=Y/D_\zeta K,\qquad C_\zeta=Y/D_\zeta Q.
\tag{HCS9.1}
\]
The full ordinary cohomology in degrees \(-1,0,1,2\) is
\[
\begin{array}{c|cccc}
&-1&0&1&2\\ \hline
K_A&H&0&C_\zeta&\chi_{\rm dil}H'\\
L_A&H&0&C_\zeta\oplus Y&\chi_{\rm dil}E'\\
K_\times&H&0&T&\chi_{\rm dil}H'\\
L_\times&H&0&T\oplus Y&\chi_{\rm dil}E'\\
K_B&H&0&C_K&\chi_{\rm dil}H'\\
L_B&H&0&C_K\oplus Y_K&\chi_{\rm dil}E'.
\end{array}
\tag{HCS9.2}
\]
Proof: the degree-zero kernels are \(J\), by injectivity of \(D_\zeta\) or \(D_K\); the preceding image is \(J\). The degree-one kernel of each final difference transpose is respectively \(\pi'Y\) or \(\pi_B'Y_K\). Dividing by the middle image gives exactly the three displayed cokernels. For \(L\), each of the two dual components annihilates \(J\); the coordinates are
\[
(\lambda_+,\lambda_-)\longmapsto
\left(\left[(\lambda_+-\lambda_-)/2\right],
(\lambda_++\lambda_-)/2\right).
\tag{HCS9.3}
\]
Surjectivity of the restrictions to \(S'\) gives the degree-two quotients \(\chi H'\) and \(\chi E'\), with the actual endpoint and extra coordinates. This proves the table, including its zero entries.

The maps on \(H,E'\) or \(H'\) are identities. In degree1 the intermediate-to-original map is
\[
T\to C_\zeta,\quad[y]\mapsto[y],
\]
and on \(L\) it is this map together with identity on \(Y\).
The intermediate-to-restricted map is
\[
T\to C_K,\quad[y]\mapsto[r_Ky],
\]
and on \(L\) it is this map together with \(r_K:Y\to Y_K\).
Both maps are onto, and their kernels fit the exact rows
\[
\boxed{0\to V\xrightarrow{\,[q]\mapsto[D_\zeta q]\,}
T\to C_\zeta\to0,}
\tag{HCS9.4}
\]
\[
\boxed{0\to Y_{\rm vis}\to T\to C_K\to0.}
\tag{HCS9.5}
\]
For HCS9.4, the kernel is \(D_\zeta Q/D_\zeta K\), and injectivity of \(D_\zeta\) identifies it with \(Q/K\). For HCS9.5, surjectivity of \(r_K\) proves onto. If \(r_Ky=D_Kk=r_KD_\zeta k\), then \(y-D_\zeta k\in Y_{\rm vis}\). Moreover \(Y_{\rm vis}\cap D_\zeta K=0\), since restriction of \(D_\zeta k\) is \(D_Kk\), which is zero only for \(k=0\). This proves precisely the second kernel.

The ordinary connecting sequence for the intermediate column is
\[
0\to T\to T\oplus Y
\xrightarrow{(t,y)\mapsto2\pi'y}\widetilde A
\xrightarrow{\Sigma'\text{ in the }S'\text{ coordinate}}
\chi H'\to\chi E'\to0.
\tag{HCS9.6}
\]
The original and restricted columns are the same formula with
\((T,Y,\widetilde A)\) replaced by
\((C_\zeta,Y,\widetilde A)\) and
\((C_K,Y_K,\widetilde B)\).
Evaluating HCS8.7 on the Fourier graph gives
\(\tfrac12\alpha(\Sigma h)+\tfrac12\alpha(R\Sigma\widehat h)
=\alpha(\Sigma h)\), because \(R\Sigma\widehat h=\Sigma h\).
This verifies the connecting map and every factor2 directly.

Although \(q\) is bijective on \(C_\zeta\) and \(C_K\), it need not be bijective on \(T\). HCS9.4 and the kernel-cokernel sequence for \(q\) prove
\[
\ker q_T\simeq\ker q_V,\qquad T/qT\simeq V/qV,
\tag{HCS9.7}
\]
with the latter isomorphism induced by \(D_\zeta\).
Thus this intermediate defect has exactly the finite critical-line primary quotients. Its presence cannot be erased by substituting the polynomial-divisibility result for the other two cokernels.

## HCS10. The full cyclic supported map, including the intermediate defect

For every column, \(G\) in the resolution denotes its actual cochain generator: it is the retained primal dilation generator on \(P,A,B\), and \(1-L^t\) on the uniformly twisted dual terms. Equivariance of the residue and restriction maps proves that these generators define a single \(\mathbb C[X]\)-complex. Use the actual cyclic resolution
\[
\mathscr H^n(K_\bullet)=K_\bullet^n\oplus K_\bullet^{n-1},
\qquad
\partial(u,v)=(d_Ku,d_Kv-(-1)^nq(G)u).
\tag{HCS10.1}
\]
For the restricted column, HCS5 and HCS6 justify the same complete cohomology calculation as the original ORE8, now on the constructed \(B\) row. Its nontrivial supported cyclic sequence is
\[
\boxed{
0\to\ker q_{Y_K}\xrightarrow{\,2\pi_B'\,}
\ker q_{\widetilde B}\xrightarrow{\gamma\mapsto(\Sigma_B'\gamma,0)}
\ker q_{\chi H'}
\xrightarrow{(\eta,e)\mapsto(-\delta_q^K(\eta)/2,e)}
Y_K/qY_K\oplus\ker q_{\chi E'}\to0.}
\tag{HCS10.2}
\]
Here \(\chi H'=\widetilde S\oplus\chi E'\). In degrees \(-1\) and0, the comparison \(K_B\to L_B\) is identity on \(\ker(q:H\to H)\) and \(H/qH\), respectively. In degree1 it is \(0\to\ker q_{Y_K}\). In degree2 it is the displayed \((-\delta_q^K/2,\mathrm{id})\). In degree3 it is the isomorphism
\[
(\chi H')/q(\chi H')\to(\chi E')/q(\chi E'),
\tag{HCS10.3}
\]
since \(q\) is onto on the complementary \(\widetilde S\). All further cohomology vanishes. Thus no endpoint polynomial or extra coefficient was excluded to isolate degree2.

The exact degree-two value at an off-critical primary block is
\[
\boxed{
(S_j,0)\longmapsto
\left(
\left[\frac{(-1)^{j+1}j!}{4}\,
t^{r-1-j}\pi^{b+t-1/2}
\frac{\Gamma((1-b-t)/2)}{\Gamma((b+t)/2)}
\right]_{\mathbb C[t]/(t^{\min(m,r)})},
0\right).}
\tag{HCS10.4}
\]
At a critical-line block this Schwartz coordinate is zero by HCS7.8; the endpoint/extra coordinate is still exactly \(e\). Both factors of \(1/2\), the complete reflected parameter, the multiplicity quotient and the Gamma derivatives have been kept.

For the intermediate column the additional component in HCS9.7 must be calculated. In the original plus-chart splitting,
\[
H^2\mathscr H(K_\times)
=(T/qT)\oplus\ker q_{\chi H'},\qquad
H^2\mathscr H(L_\times)
=(T/qT)\oplus(Y/qY)\oplus\ker q_{\chi E'}.
\tag{HCS10.5}
\]
This splitting is constructed by extending the \(S'\) coordinate of \(H'\) on the plus chart and retaining the endpoint/extra coordinates. It commutes with \(q\); the other summand is represented by degree-one cycles modulo their \(q\)-images. If \(p:Y/qY\to T/qT\) is the natural quotient, the complete map is
\[
\boxed{
([t],\eta,e)\longmapsto
\left([t]-\tfrac12p\delta_q(\eta),
-\tfrac12\delta_q(\eta),e\right).}
\tag{HCS10.6}
\]
To check the sign and the first component, let \(\Sigma'\alpha=\eta\).
In the target Hom complex subtract the boundary of the plus-chart lift \(((\alpha,0),0)\). Its remaining degree-one pair is
\((-q\alpha,0)\). In coordinates HCS9.3, its half-difference and half-sum are both \(-q\alpha/2\). The former gives
\(-p\delta_q(\eta)/2\) in \(T/qT\), and the latter
\(-\delta_q(\eta)/2\) in \(Y/qY\).
The original \([t]\) enters only the half-difference, and the endpoint/extra component is unchanged. This proves all three components.

The maps to the original and restricted columns take this formula respectively to
\[
(\eta,e)\mapsto(-\delta_q(\eta)/2,e),\qquad
(\eta,e)\mapsto(-\delta_q^K(\eta)/2,e),
\]
because the first component maps to the zero quotients
\(C_\zeta/qC_\zeta\) and \(C_K/qC_K\); the second maps by identity or \(r_K\bmod q\). The vanishing of the first component after these maps is proved by those polynomial inverses, not imposed on the intermediate source.

For the other degrees the intermediate supported map is identity on the same degree-\(-1\), degree0 and degree3 groups as above. In degree1 it is
\(\ker q_T\to\ker q_T\oplus\ker q_Y,\ t\mapsto(t,0)\).
This follows from the ordinary degree-one map \(t\mapsto(t,0)\) and \(H^0K_\times=H^0L_\times=0\). The full degree-two groups and map are HCS10.5–HCS10.6. These formulas specify the entire cyclic comparison.

At a critical parameter the term \(T/qT\simeq V/qV\) retains exactly the original critical primary block. Thus the intermediate first component in HCS10.6 can be nonzero even though the restricted row has an explicit lift. At an off-critical parameter \(T/qT=0\), because \(q\) is invertible on \(V\); the complete original \(Y/qY\) residual remains and restricts to the full \(Y_K/qY_K\) residual. This is the exact allocation of both classes in the comparison, without conflating two different quotient targets.

## HCS11. Actions, mirror, support labels, and what this cross proves

All sheaf maps, connecting cochains and cone maps intertwine the original positive dilation \(T_ab(u)=b(u/a)\), not a divided or shifted action. On the Hilbert receiver the exact retained bound is
\[
\|T_a\|_{\mathcal H_\delta}
=a^{1/2}
\left(\frac{(\log a)^2+2+
|\log a|\sqrt{(\log a)^2+4}}2\right)^{\delta/2}.
\tag{HCS11.1}
\]
WHR proves it from the original measure and derives the quotient upper bound. Applying it to powers and to the inverse proves purity of each Hausdorff receiver. HCS3 computes the exact map from the original cohomology to that receiver and its kernel. The supported calculation does not promote the receiver bound to a bound on that kernel.

The original mirror \(R\) preserves \(B\), \(K\) and \(V\), and satisfies
\(RT_a=aT_{a^{-1}}R\). The companion mirror on \(L_B^1\) is
\((\alpha_+,\alpha_-)\mapsto(-R_B'\alpha_-,-R_B'\alpha_+)\);
the corresponding quotient mirror is \(-R_B'\).
The intermediate mirror uses \(R_A'\) on its dual terms and \(R_B\) on its primal term, so every map in HCS8.5 intertwines the companion mirrors. The original and reflected residue denominators remain the companion maps; no equality of two unproved self-mirror pairings is used. On a cyclic resolution the polynomial changes from \(q(X)\) to \(q(1-X)\). Holding \(q\) fixed without that transformation would lose the reflection.

Each proved receiving linear map has the existing exact labelled lift
\((v,\lambda)\mapsto(f(v),\lambda)\) on the full support carrier.
Nontop zero-amplitude inputs keep their labels, and zero outputs retain the original supported zero rather than becoming primitive \(\tau\). Different inputs to a bilinear pairing keep their two independent labels. All coefficient identities above are in the specified receiving fibres, so no operation on primitive \(Z_1/\tau\) is inferred.

This cross supplies a concrete answer to the next calculation after the Hilbert limitation. Closed support does return the entire \(K_{\rm off}\): HCS2.3–HCS2.4 give an equivariant split quotient from its supported degree-one group. The actual restriction extension on that object exists, is a proved pushout, and has the complete connecting value HCS7.10. Its supported value HCS10.4 is nonzero on every surviving off-critical primary block, of exact rank \(\min(m,r)\). At critical parameters, by contrast, HCS7.6–HCS7.9 construct the required fixed-order lifts.

The off-critical source and target in this particular connecting map carry the same character \(a^{1-\rho}\) with the exact displayed nilpotent action. Thus their numerical weights, when evaluated from \(T_p\), are both \(2\Re(1-\rho)\); this map does not create a Deligne weight gap between them. This statement is the computed action of the actual map, not a claim that the source programme lacks another geometric comparison. Deligne's §§3.6.1–3.6.3 additionally prove distinct geometric weight bounds on his restriction and closed-support terms by his geometric constructions. Those bounds cannot be assigned to HCS5.3 merely from the formal existence of support.

The exact new objects left for the ongoing global calculation are the already constructed \(K_{\rm off}\), its actual full source sheaf \(\mathcal F_B\), and the restriction pushout HCS5.2. The finite residual formula is now connected to the full original source, every closure map, and every endpoint. No RH assumption, RH conclusion, or new conditional purity theorem has entered this derivation.

## HCS12. Independent verification boundary

The parallel independent check [CHC](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/HILBERT_CLOSURE_SUPPORT_INDEPENDENT_CHECK.md) verifies the supported rows, both cone maps and their cohomology, the finite-\(\delta\) residue radical, and the extra intermediate cyclic component. The finite-\(\delta\) radical is a reason to restrict HCS6–HCS10 to the actual whole-family \(B_{\rm off}\), as done above; it is not an omitted exception. The intermediate cokernel is deliberately not given the polynomial-divisibility property proved only for \(C_\zeta\) and \(C_K\).


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
