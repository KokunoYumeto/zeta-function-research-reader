# Original quotient propagation before arithmetic realization

Research continuation, 11 September 2026. Additive draft contribution; existing notes and accepted claims are unchanged.

This note uses the original globalization congruences, not an ordinary quotient with a support label added afterward. It gives the universal quotient in the original semimodule category, the actual theta relation at every label, and the analytic realization and operator maps on that quotient. The source semimodule equivalence and theta multiplier are existing results, not new novelty claims.

## 1. Original congruences and their factor map

For a commutative ring R retain S=G(R)=R disjoint-union {tau}, with supported e=0_R and external additive identity tau. Supported elements use the ring operations; r+tau=r and r tau=tau.

For an ideal I define

\[
x\sim_I^{\mathrm{sp}}y
\iff (x=y=\tau)\ \text{or}\ (x,y\in R\text{ and }x-y\in I).
\]

The original quotient and its arithmetic observation are

\[
G(R)\xrightarrow{q_I^{\mathrm{sp}}}G(R/I)
\xrightarrow{p_{R/I}}R/I.
\]

The first map keeps tau separate from the supported zero residue. The second identifies them. These are the rho_n and rho'_n constructions of the original integer globalization note. For a ring map h carrying I into I', the induced G(h), G(bar h) and bar h commute with both arrows. Changing coefficient rings by these maps is not iteration of scalar zero-adjunction.

If R/I is finite, the source arithmetic norm is |R/I|, equivalently the cardinality of the supported fibre inside G(R/I), not |G(R/I)|. This retains the original Dedekind counting rule. We allow the zero ring here: G(0) is the two-element Boolean semiring.

## 2. The original-form quotient theorem

Chapter 14 presents an S-semimodule as M=disjoint-union_l M_l over the join-semilattice eM. Each fibre is an R-module; transport from l to l' is addition of the internal zero at l'. Write epsilon_N(y)=ey.

Let f=(phi,f_l):M->N be an S-linear map, with support map phi:L->K. Define

\[
B_k(f)=\sum_{\phi(l)\le k}
\rho^N_{\phi(l),k}(f_l(M_l))\subset N_k.
\]

All sums are finite sums of elements. The transports send B_k into B_k'. Define directly in the original operations

\[
x\approx_f y
\iff ex=ey=k\quad\text{and}\quad x+(-1_R)y\in B_k(f).
\]

**Theorem.** This is a semimodule congruence and

\[
\boxed{\mathsf Q_{\mathrm{sp}}(f)
=\bigsqcup_{k\in K}N_k/B_k(f)
=\operatorname{coeq}_{S\text{-SMod}}(f,\epsilon_Nf).}
\]

The quotient map is (k,y)->(k,[y]). Its support map is the identity of K, and

\[
e(k,[y])=(k,[0]),\qquad\tau(k,[y])=(0_K,[0]).
\]

**Proof.** The relation in each fibre is a module-quotient relation. Adding an element in N_m transports its difference to B_{k join m}; scalar multiplication preserves it, and tau sends both sides to the least-label zero. Thus it is a congruence. It equalizes f and epsilon_N f. Conversely, an S-linear h equalizing these maps kills each f_l(M_l) to its target fibre zero. Naturality kills every transported summand defining B_k. Therefore h factors uniquely through the displayed quotient. Its fibre zeros still recover exactly K. This proves the universal property without choosing representatives.

A commuting square (a,b) from f to f' induces

\[
\overline b(k,[y])=(\psi(k),[b_k(y)]),
\]

where psi is the support map of b. Naturality proves b_k B_k(f) is contained in B_psi(k)(f'). Thus identity and composition laws hold.

For the ideal inclusion I^tau -> G(R), this is exactly G(R/I), the original support-preserving quotient. The ordinary cokernel coequalizes f with the constant global-zero map instead; there is a canonical further quotient from Q_sp(f) to it. For multiplication by two on G(Z), these are respectively G(Z/2) and Z/2, related by p. This identifies the additional relation rather than treating the two quotients as interchangeable.

## 3. Arithmetic reflection and its information loss

The ordinary R-module reflection of N is

\[
\operatorname{Lin}(N)=\varinjlim_{k\in K}N_k,
\qquad (k,y)\mapsto[y].
\]

Any S-linear map to an R-module via S->R kills every support idempotent and has compatible fibre maps, proving this universal property. Since a join-semilattice is filtered,

\[
\operatorname{Lin}(\mathsf Q_{\mathrm{sp}}(f))
\cong\operatorname{coker}(\operatorname{Lin}(f)).
\]

At a fixed label the lost vector submodule is exactly

\[
\ker(N_k\to\operatorname{Lin}(N))
=\bigcup_{k'\ge k}\ker\rho_{k,k'}.
\]

Thus recording the label beside the already-reflected amplitude need not reconstruct N. The transport kernels have to be retained.

For a fixed-support cochain diagram, the original reconstructed equation d^(n+1)d^n is the fibrewise zero arrow, not the constant least-label map. Its cycles and cohomology are

\[
Z^n_{\mathrm{sp}}=\operatorname{Eq}(d^n,\epsilon d^n)
=\bigsqcup_l\ker d_l^n,
\]

\[
H^n_{\mathrm{sp}}=\bigsqcup_l\ker d_l^n/\operatorname{im}d_l^{n-1},
\]

using the same coequalizer theorem. Acyclic amplitude fibres leave the skeleton, which arithmetic reflection then maps to the ordinary zero module.

## 4. Apply the theorem to the actual theta relations

Retain V, the even Schwartz functions with phi(0)=hat phi(0)=0, Fourier kernel exp(-2 pi i x xi), and the strong-Schwartz space B on R_+ from ACTUAL_ADELIC_COMPARISON.md. Use

\[
\Theta\phi(x)=2\sum_{n\ge1}\phi(nx),\qquad
\mathcal MF(s)=\int_0^\infty F(x)x^s\,dx/x.
\]

The finite sums are original supported sums: a supported zero result is e, not tau. Their compact-local smooth limit is supported; Poisson gives the stronger endpoint bounds. This does not assert that each finite partial sum lies in B.

Use the same source label system as the existing arithmetic appendix: finite-dimensional W subset V, with join W+W'. At W nonzero the source fibre is W and target fibre is B; at the least label both are zero. The actual map is

\[
\widetilde\Theta(W,\phi)=(W,\Theta\phi).
\]

The quotient before projection is

\[
\boxed{
\mathfrak Q_\Theta
=\{\tau\}\sqcup\bigsqcup_{W\ne0}\{W\}\times(B/\Theta W).}
\]

Its exact relation and addition are

\[
(W,F)\sim(W',F')\iff W=W'\text{ and }F-F'\in\Theta W,
\]

\[
(W,[F])+(U,[G])=(W+U,[F+G]).
\]

For W subset W', transport has kernel

\[
\boxed{\ker(B/\Theta W\to B/\Theta W')
=\Theta W'/\Theta W\cong W'/W.}
\]

The last isomorphism follows from injectivity of Theta: on Re s>1 its Mellin multiplier is 2 zeta(s), which is nonzero, and Mellin/Fourier uniqueness then gives phi=0.

In particular, if phi_* is not in W, the class [Theta phi_*]_W is nonzero, but its transport to W+C phi_* is the supported zero at that larger label. It never becomes tau. This computes an actual difference among the quotient fibres; it is not a uniform tensor decoration of B/Theta V.

Arithmetic reflection and Hausdorff realization have exact kernels

\[
0\to\Theta V/\Theta W\to B/\Theta W\to B/\Theta V\to0,
\]

\[
B/\Theta V\twoheadrightarrow B/\overline{\Theta V},
\qquad\ker=\overline{\Theta V}/\Theta V.
\]

## 5. Keep the mixed chart masks

Index by (W,I), where I subset {+,-}, the empty I occurs only at W=0, and nonempty I with W=0 records supported zero-input faces. Join is (W+U,I union J).

Use source fibre direct-sum_{i in I} W_i, with W_+=W and W_-=hat W, and target B for nonempty I. Transports insert supported zero coordinates. The original-form differential is

\[
d_{W,I}=\mathbf1_{+\in I}\Theta\phi_+
-\mathbf1_{-\in I}\Theta\widehat\phi_-.
\]

Its image is Theta W for every nonempty I. The degree-one quotient is B/Theta W at the same (W,I). For phi_-=hat phi_+, its value is the internal zero of the two-slot face. For both absent it is external absence. No mask is inferred from the resulting amplitude.

The plus-chart inclusion on complexes sends phi to (phi,0) and F to F. The coordinate change (phi,psi)->(phi-hat psi,psi) splits off hat W in degree zero, proving the identity on the displayed degree-one quotient. Its supported label map sends the plus face to the two-slot face.

## 6. The Mellin quotient, including its exact kernel

The existing source identity, with all constants retained, is

\[
\mathcal M\Theta\phi=2\xi H_\phi,
\quad
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

\[
H_\phi(s)=\frac{2\pi^{s/2}M_+\phi(s)}{s(s-1)\Gamma(s/2)}.
\]

The source proves H_phi entire and supplies the actual phi_*=(4 pi^2 x^4-6 pi x^2)exp(-pi x^2), with H_phi*=1.

For O=O_C and W nonzero, retain

\[
J_W=(H_\phi:\phi\in W),\qquad I_W=(2\xi)J_W.
\]

Set A_W=O tensor W, B_W=O tensor B, delta_W=1 tensor Theta, alpha_W(h tensor phi)=h H_phi, and beta_W(h tensor F)=h MF. Then

\[
\beta_W\delta_W=(\times2\xi)\alpha_W.
\]

The induced supported map is

\[
\boxed{(W,[b])\longmapsto(W,[\beta_Wb])
\quad\text{in}\quad\bigsqcup_{W\ne0}O/I_W,\qquad\tau\mapsto\tau.}
\]

Its internal kernel at W is exactly

\[
\boxed{\beta_W^{-1}(I_W)/\delta_W A_W
\cong\ker\beta_W/\delta_W(\ker\alpha_W).}
\]

To prove the equality, subtract a delta_W image with the required element of I_W to enter ker beta_W. Its intersection with delta_W A_W is delta_W ker alpha_W, because multiplication by 2xi is injective. Local surjectivity of beta_W follows by choosing F(e^y)=exp(-s_0 y)h(y), with h nonnegative nonzero smooth compactly supported, so MF(s_0)=integral h is nonzero. Thus the map is locally onto.

For W subset W', the target transport has kernel I_W'/I_W. When W contains phi_*, I_W=(2xi); these labels are cofinal. The analytic amplitude stabilizes there, while the original B/Theta W quotients still have the transport kernels in section 4.

All sheaf-level disjoint unions mean sheafification: labels are locally constant on labelled opens, fibre sections glue there, and the empty open has one section. A raw disjoint-union presheaf is not silently used as a sheaf on disconnected opens.

## 7. The original scalar quotient at the actual analytic stalks

At s_0, with R_s0=O_{C,s_0}, the original congruence is unchanged:

\[
\boxed{G(R_{s_0})/\sim^{\mathrm{sp}}_{(2\xi)}
\cong G(R_{s_0}/(2\xi)).}
\]

Its arithmetic observation is p to R_s0/(2xi). Where xi(s_0) is nonzero, that ring is zero but the supported quotient is G(0)=B. The support skeleton has not vanished just because the amplitude sheaf vanishes.

At an actual zero rho of multiplicity m, put z=s-rho and keep

\[
u_\rho(z)=2\xi(\rho+z)/z^m,\qquad u_\rho(0)\ne0.
\]

The presentation square has horizontal maps times 2xi and times z^m, left vertical times u_rho and right vertical identity. Therefore the resulting supported Taylor map sends tau to tau and each supported germ to its class in G(C[z]/z^m). The analytic unit is retained in the square, not silently discarded.

For a finite jet family Z, the existing finite-jet map induces

\[
\widetilde J_Z(W,[F])=(W,J_ZF),
\quad
J_ZF=\left(\sum_{j<m_\rho}(\mathcal MF)^{(j)}(\rho)z_\rho^j/j!\right)_\rho.
\]

Its internal kernel is ker J_Z / Theta W. Finite-jet surjectivity from compactly supported smooth representatives is the interpolation result in the existing arithmetic appendix. Continuity gives the stated further Hausdorff factorization.

Dilation includes its label map:

\[
(W,[F])\mapsto(R_aW,[R_aF]),\quad R_aF(x)=F(ax),
\]

\[
J_ZR_aF|_\rho=a^{-\rho}\sum_{k<m_\rho}(-\log a)^kz_\rho^k/k!\,J_ZF|_\rho.
\]

For D=-x partial_x, the corresponding map has label DW and jet operator multiplication by rho+z_rho. This follows from DTheta=ThetaD and M D=s M. No individual W-invariance is assumed. Fourier acts through W->hat W and F(x)->x^{-1}F(1/x).

The existing finite-jet quotient metric becomes the observation (W,[F])->(W,nu_R(J_ZF)); its zero fibre is the just-calculated internal kernel, not external absence. A trace or pairing is treated the same way, retaining its input label or pair of labels until the explicitly named scalar observation. No positivity bound is inferred from the existence of these quotient maps.

## 8. The original mixed coefficient multiplication

For the original quadratic double D_A=G(A)^2 and a ring map lambda:A->A', the coefficient map D(lambda)(a,b)=(G(lambda)a,G(lambda)b) preserves

\[
(a,b)\star(c,d)=(ac\oplus(-1_A)bd,\ ad\oplus bc).
\]

For residue reduction modulo I, its kernel pair retains each mask and reduces each supported coefficient modulo I, giving exactly D_{A/I}. The square with amplitude maps to A[t]/(t^2+1) commutes with t->t. The synchronization idempotent E=(1,e) maps to E', and D(lambda)(Ex)=E'D(lambda)(x).

These are coefficient-algebra morphisms. Theta and Mellin are the linear arrows specified above, not claimed to preserve this star product. At finite pointed sets, every semimodule quotient map acts coordinatewise and commutes with the original finite fibre sums.

## Checks and integration

Run `python checks/check_original_congruence.py` and the same command with `python -O`. The dependency-free checker independently generates the least finite congruence by closing the generator pairs under addition, scalar multiplication and equivalence, then compares it with the formula of section 2. Six cases execute 5,443 exact pair comparisons, plus the explicit distinction between G(Z/2) and Z/2. Both runs passed and produced identical output. This tests finite examples, not the infinite-dimensional analytic inputs or an RH estimate.

The larger attached continuation has the full proofs, sheaf formulation, all operator and metric maps, and a SymPy checker with 17,712 exact comparisons. The public check is a subset of those congruence cases; the counts must not be added as independent evidence.

Source basis: original globalization congruence theorem; Zeta chapter 14, blob 49318a578b96462384000afa16794cfd5fe492c1; current ACTUAL_ADELIC_COMPARISON.md, blob c23656c2a43e0041d6f7aeb0b80d6e12a6b468d9, read at head 8a5b82a7c234ca5e283035788545ce1a296f8283; and the attached predecessor's actual theta comparison TeX. Only original TeX and authored notes were used for these readings. No full source books or private conversations are copied here. Research direction and split-zero framework remain attributed to the repository owner; these derivations and finite checks were developed in the current ChatGPT session. Draft only; no merge or endpoint theorem is asserted.
