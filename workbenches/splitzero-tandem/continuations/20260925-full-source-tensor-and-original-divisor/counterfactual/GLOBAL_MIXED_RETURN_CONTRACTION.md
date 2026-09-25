# Global contraction of the actual mixed return, with its prime action

Programme derivation, 25 September 2026. Proof locators GMC0–GMC7.

## GMC0. The source and the specific calculation

The user's corrected notation is retained: \(Z_0\) is absence, \(0=e=\varnothing\); primitive \(Z_1/\tau\) has no parity or source addition; integers retain their amount and \(Z_2\) parity. No operation below is addition on primitive \(\tau\). All additions, tensors and complexes are in the already constructed receiving complex vector spaces. The current source laws and retraction are B1–B5/P1–P5/R1 in [SOURCE_OPERATIONS_AND_PROOFS.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md).

This calculation applies the amended forward instruction: use the finding and everything already established to determine and attempt the next calculation. The input is the full returned sheaf, including its closed stalks. An obstruction in its generic stalk must therefore be tested in its global complex before it is called a global obstruction. The result below is an explicit global quasi-isomorphism and homotopy, with the original prime action. It is not a numerical purity assertion or a proof of RH.

The human source of the three-point geometry and coefficient restrictions is Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, 0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The comparison target is Pierre Deligne, [*La conjecture de Weil. II*, §§3.3.11 and 3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Their weight conclusions are not assumptions here. The exact summation-image theorem SSI and its receiving application DCP prove the inverse used below; full source locators and their actual reading coverage are retained in [SOURCE_CC_DOUBLE_PULLBACK.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SOURCE_CC_DOUBLE_PULLBACK.md), DCP0, DCP3 and DCP10. The actual returned sheaf, its signs and its complete restrictions are [DIAGONAL_EXTRAORDINARY_RETURN.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/DIAGONAL_EXTRAORDINARY_RETURN.md), DER7–DER9.

## GMC1. Full spaces, maps and actions

Retain the original spaces
\[
S=\{h\in\mathcal S(\mathbb R):h(-u)=h(u),\ h(0)=0,\ \int_{\mathbb R}h(u)\,du=0\},
\]
\[
A=\{b\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^j b(u)|<\infty
\text{ for all }N,j\geq0\},
\]
\[
\Sigma h(u)=2\sum_{n\geq1}h(nu),\qquad
J=\Sigma S,\qquad Q=A/J.
\tag{GMC1.1}
\]
Here \(J\) is closed and \(\Sigma:S\to J\) is the proved topological isomorphism, not an assumed inverse to a formal sum. The quotient is the actual Fréchet quotient. Its identification uses the original formula
\[
M_0\Sigma h(s)=2\zeta(s)M_Sh(s),\qquad
M_0b(s)=\int_0^\infty b(u)u^s\frac{du}{u}.
\tag{GMC1.2}
\]
No completed replacement of \(\zeta\) is made.

On the original three-point space \(Y\), put
\[
\mathcal F=(W_+\xrightarrow{r_+}A\xleftarrow{r_-}W_-),\qquad
W_\pm=(S\oplus\mathbb C^2_\pm)\oplus V_\pm^{\rm extra}.
\]
The two endpoint coordinates and the whole extra copy have zero restriction; on \(S\), \(r_+=\Sigma\) and \(r_-=R\Sigma\), where \(Rb(u)=u^{-1}b(u^{-1})\). Both images are exactly \(J\). Write
\[
H=\ker[W_+\oplus W_-\xrightarrow{r_+-r_-}A].
\tag{GMC1.3}
\]
Thus \(H\) retains its Fourier graph, four endpoint lines and both full extra copies.

The original action is \(T_t b(u)=b(u/t)\) for \(t>0\), with its already constructed chart actions \(\rho_\pm(t)\), satisfying
\[
r_\pm\rho_\pm(t)=T_t r_\pm.
\tag{GMC1.4}
\]
Their Schwartz summands are invariant. All tensor products in this note are algebraic over \(\mathbb C\). On a tensor, use the simultaneous action, and its full generator
\[
T_t\otimes T_t,\qquad L_{\rm tot}=L\otimes1+1\otimes L,
\qquad Lb=-u\partial_u b.
\tag{GMC1.5}
\]
These formulas are not the source-integer scalar action; both actions remain distinguished as in DCP10.

## GMC2. The existing inverse supplies an equivariant section

Define
\[
s_+:J\longrightarrow W_+,
\qquad s_+(j)=(\Sigma^{-1}j,0,0),
\tag{GMC2.1}
\]
where the two zero entries denote the entire endpoint pair and the entire extra copy. It is continuous because the inverse theorem supplies continuity of \(\Sigma^{-1}\). Its domain is \(J\), not all of \(A\). Direct substitution gives \(r_+s_+=\operatorname{id}_J\).

To prove equivariance, both \(\rho_+(t)s_+j\) and \(s_+T_tj\) belong to the invariant Schwartz summand. Their restrictions are equal by (GMC1.4), and \(r_+\) is injective on that summand. Therefore
\[
\rho_+(t)s_+=s_+T_t\quad(t>0).
\tag{GMC2.2}
\]
Differentiation at \(t=1\) gives the corresponding generator identity, since the Schwartz and \(A\) actions are differentiable there and the maps are continuous. Every prime specialization \(t=p\), every polynomial in the generator, and every polynomial in a fixed prime action also intertwines. This proves the needed section rather than assuming an equivariant vector-space complement.

## GMC3. The actual mixed row and its global differential

DER7–DER8 constructs the sheaf \(G=R^1q_*(\mathcal F\boxtimes\mathcal F)\), with
\[
G_\eta=Q_\Delta=(A\otimes A)/(J\otimes J),
\quad G_{c_\pm}=(W_\pm\otimes Q)\oplus(Q\otimes W_\pm).
\tag{GMC3.1}
\]
Let
\[
M=(J\otimes Q)\oplus(Q\otimes J),\qquad V=Q\otimes Q.
\]
The canonical exact row is
\[
0\longrightarrow M\xrightarrow{\iota}Q_\Delta
\xrightarrow{\vartheta}V\longrightarrow0.
\tag{GMC3.2}
\]
For \(j\otimes q\), the injection uses \(j\otimes\widetilde q\) modulo \(J\otimes J\); changing the lift changes the tensor by \(J\otimes J\). The second summand is defined in the other slot. Exactness and independence are proved in DER8.1; both summands remain.

Set \(C^0=G_{c_+}\oplus G_{c_-}\), \(C^1=Q_\Delta\). Write a degree-zero input as \(c=(u_+,v_+,u_-,v_-)\). The complete differential is \(d=\iota d_M\), where
\[
d_M(c)=\bigl(
-(r_+\otimes1)u_++(r_-\otimes1)u_-,\quad
(1\otimes r_+)v_+-(1\otimes r_-)v_-
\bigr)\in M.
\tag{GMC3.3}
\]
These are the two original restriction signs. This is the full ordered global Čech complex of \(G\), not just its generic row.

For \(m=(m_1,m_2)\in M\), define
\[
S(m)=\bigl(-(s_+\otimes1)m_1,\ (1\otimes s_+)m_2,\ 0,\ 0\bigr)\in C^0.
\tag{GMC3.4}
\]
Substituting (GMC2.1) into all four terms of (GMC3.3) proves
\[
d_M S=\operatorname{id}_M.
\tag{GMC3.5}
\]
Every entry in (GMC3.4) intertwines the simultaneous actions, so \(S\) does also. Tensor continuity is valid on the respective projective tensor topologies. This note asserts algebraic tensor cohomology and does not replace it by completed tensor cohomology.

## GMC4. Explicit global quasi-isomorphism and its kernel homotopy

Put \(K_0=\ker d_M\). Define the two-degree target complex
\[
T^0=K_0,\qquad T^1=V,\qquad d_T=0.
\]
The maps
\[
F^0(c)=c-Sd_Mc,\qquad F^1(z)=\vartheta z
\tag{GMC4.1}
\]
form a cochain morphism \(F:C^\bullet\to T^\bullet\). Indeed \(d_MF^0=0\) by (GMC3.5), and \(\vartheta d=0\) by (GMC3.2). Both degree maps are onto: \(F^0\) is identity on \(K_0\), and \(\vartheta\) is the quotient in (GMC3.2).

The complete kernel complex is
\[
\ker F=[S(M)\xrightarrow{\ d\ }\iota(M)].
\tag{GMC4.2}
\]
On it define the degree-minus-one homotopy
\[
h^1(\iota m)=Sm,\qquad h^0=0.
\tag{GMC4.3}
\]
Then \(dh^1(\iota m)=\iota m\) and \(h^1d(Sm)=Sm\). Thus \(dh+hd=\operatorname{id}\) on the entire kernel. All maps intertwine the original simultaneous dilation and every prime specialization, by GMC2–GMC3. Consequently (GMC4.1) is an explicit equivariant quasi-isomorphism
\[
\boxed{R\Gamma(Y,G)\longrightarrow
K_0[0]\oplus(Q\otimes Q)[-1].}
\tag{GMC4.4}
\]
The statement includes the displayed surjective cochain map and the exact kernel homotopy. It does not claim an equivariant section \(V\to Q_\Delta\) of the generic quotient.

The kernel identification retains every closed input:
\[
K_0\cong(H\otimes Q)\oplus(Q\otimes H).
\tag{GMC4.5}
\]
For the first component, (GMC3.3) imposes \(r_+u_+=r_-u_-\), which is the tensor with \(Q\) of the equation defining \(H\). Tensor over \(\mathbb C\) is exact, hence its kernel is \(H\otimes Q\). The other component gives \(Q\otimes H\) by the same displayed equation in the other slot. Both identifications intertwine the original actions because all maps in their defining kernels do. No endpoint or extra copy has been removed.

## GMC5. What happens to the generic polynomial obstruction

Let \(P\) be any specified nonzero polynomial over \(\mathbb C\) in the actual operator \(L_{\rm tot}\). For \(v\in V\) with \(P(L_{\rm tot})v=0\), choose an actual lift \(z\in Q_\Delta\). Its generic connecting representative is the unique \(m\in M\) such that
\[
\iota m=P(L_{\rm tot})z.
\tag{GMC5.1}
\]
Its class in \(M/P(L_{\rm tot})M\) is independent of the lift: replacing \(z\) by \(z+\iota a\) replaces \(m\) by \(m+P(L_{\rm tot})a\). This is the exact generic obstruction, not an assumption that it is zero.

In the actual global complex its same representative satisfies
\[
\boxed{P(L_{\rm tot})z=d(Sm).}
\tag{GMC5.2}
\]
This follows by (GMC3.5), with precisely the \(m\) in (GMC5.1). Thus the corresponding global cohomology class is annihilated by \(P(L_{\rm tot})\), as the isomorphism (GMC4.4) also shows. The primitive \(Sm\) retains its two plus-chart components and the displayed signs. No polynomial inverse on \(M\) is assumed or needed.

More generally the full mixed subsheaf \(N\subset G\), with the same closed stalks and generic stalk \(M\), has global complex \([C^0\xrightarrow{d_M}M]\). Its projection \(c\mapsto c-Sd_Mc\) is an equivariant quasi-isomorphism to \(K_0[0]\), with the same contracted kernel. This strengthens the earlier cohomological statement \(H^1(Y,N)=0\) by constructing its homotopy and actions.

The same proof, term by term, applies to a polynomial in \(T_p\otimes T_p\) for any actual prime \(p\), because (GMC2.2) holds before taking the polynomial. This is global cancellation of this exact mixed boundary. It neither erases its nonzero generic connecting class nor identifies it with Deligne's different specialization obstruction.

## GMC6. Original residue trace, numerical content and source return

The returned original trace is zero on \(C^0\) and in degree one is
\[
Q_\Delta\xrightarrow{\vartheta}Q\otimes Q
\xrightarrow{\overline B_\zeta}\chi_{\rm dil}\mathbb C.
\tag{GMC6.1}
\]
It therefore factors through the actual map \(F\) of (GMC4.1), with coefficient \(+1\). The full original contour remains
\[
B_\zeta(b,c)=\frac{1}{2\pi i}
\left(\int_{\Re s=2}^{\uparrow}-\int_{\Re s=-1}^{\uparrow}\right)
\frac{M_0b(s)M_0c(1-s)}{\zeta(s)}\,ds.
\tag{GMC6.2}
\]
The preceding residue proofs retain all functional-equation factors, multiplicities, contour orientation and the full comparison with any earlier coordinates. No contour term changes in GMC4 or GMC5.

On actual primary tensor blocks the generator is still
\[
L_{\rm tot}=(\rho+\sigma)\operatorname{id}
+N_\rho\otimes1+1\otimes N_\sigma,
\]
\[
(T_p\otimes T_p)|_{Q_\rho\otimes Q_\sigma}
=p^{\rho+\sigma}
\sum_{j=0}^{m_\rho-1}\sum_{k=0}^{m_\sigma-1}
\frac{(\log p)^{j+k}}{j!\,k!}N_\rho^j\otimes N_\sigma^k.
\tag{GMC6.3}
\]
Every term and multiplicity remains. The trace pairs the reflected blocks \(\sigma=1-\rho\), giving the character \(p\). The contraction changes none of these operators, so the actual calculation controls the mixed return while retaining the original exponents. It supplies no bound \(\Re\rho=1/2\) by itself.

The full arithmetic comparison is the correspondence and canonical derived map of [DERIVED_RETURN_FULL_SOURCE_CORRESPONDENCE.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/DERIVED_RETURN_FULL_SOURCE_CORRESPONDENCE.md), FSC3–FSC6. Its comparison is natural in bounded sheaf complexes. The map (GMC4.4) is a global complex of vector spaces, not a sheaf splitting of \(G\). To transport that global coefficient complex literally, apply the exact functor \(W\mapsto I_\eta(W)=(W\xrightarrow{1}W\xleftarrow{1}W)\) degree by degree. Its exactness follows at every stalk from its identity-valued diagram, and it sends the displayed cochain maps and homotopy to sheaf maps. FSC6 then applies to that specified constant-sheaf complex. This constructs its transport without identifying it with the original sheaf \(G\), whose separate derived return is DER/FSC. Every nonexceptional correspondence fibre remains the entire \(\operatorname{Spec}\mathbb Z\). No claim that an arbitrary arithmetic structure sheaf is constant on that fibre is made.

## GMC7. Precisely what was achieved

The source-derived return prompted a test of the actual mixed obstruction. GMC2 constructs an equivariant section using the previously established global summation inverse. GMC3–GMC5 use it to remove the complete mixed term from the global cohomological obstruction by a displayed contraction. GMC4 retains all lower cohomology and gives an equivariant quasi-isomorphism; GMC6 proves that the original residue trace passes through it unchanged. A generic-stalk obstruction has therefore been followed into the global complex and its exact fate computed.

This is an actual vanishing calculation for the degree-one mixed obstruction, with the explicit contraction of ker(F)=[S(M)→iota(M)] and the retained RΓ(Y,N)≃K_0[0], not a theorem obtained by assuming the numerical weight separation sought in the active goal. That goal still requires a derived numerical constraint on the remaining actual \(Q\) coefficients. The complete retained action (GMC6.3), rather than a renamed or truncated coefficient space, is the input for that next calculation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
