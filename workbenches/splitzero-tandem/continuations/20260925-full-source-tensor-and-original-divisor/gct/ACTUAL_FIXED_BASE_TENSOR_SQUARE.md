# The actual tensor square on one sphere: specialization, supported boundaries and angular degree

Complete independent derivation, **FST0–FST7**. This supplements the frozen TWC0–11 proof; it does not change that proof or claim that the original lifting obstruction vanishes.

## FST0. Stage and actual source

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). The coefficient operations below occur after complete-history arithmetic reconstruction. The two recovered branch counters and original return measures remain separate. No addition, numerical origin, metric, or coordinate operation is placed on the support. TWC0 records the connected correction-chain reading; its private reading receipt additionally records the recalled verbatim U060, U138–U141, WU050–WU055, WU061–WU062 and WU064–WU065 passages. A source tensor is not a pooled return measure.

Use the actual common-domain source complex on the sphere \(Y\), with two labelled poles \(p_+,p_-\):
\[
P=[\underline A_Y^{-1}\xrightarrow{(b_r,b_r)}i_+H_\infty\oplus i_-H_\infty],
\quad b_r=\beta_rq,
\quad(b_ra)_\rho=\delta_\rho(\Theta a)(\rho^\#),
\quad\delta_\rho=\overline{d_r(\rho)}.
\tag{FST0.1}
\]
Here \(H_\infty=H_{\infty,L}\oplus H_{\infty,O}\) retains the entire actual divisor and multiplicities; \(b_rA\subset H_{\infty,O}\) is dense there. Set \(A_O=\ker b_r\), so the actual original specialization source is \(\mathcal R=A/A_O\). Every endpoint summand is reattached explicitly in FST6.

The source and all analytic factors are the original ones in ADM1 and TWC1, including
\[
\Theta a(s)=\tfrac12\int_0^\infty a(u)u^s\,du/u,
\quad F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=\tfrac18,
\]
\[
F_0(-2j)=\frac{j(2j+1)(-1)^j\pi^j}{2\,j!}\zeta'(-2j)\quad(j\ge1),
\quad F_0(-1)=F_0(2)=\pi/24.
\tag{FST0.2}
\]
All local multiplicity germs and their full Leibniz derivatives, the normal factor \(F_0(\lambda-1)\), the unit term and all prime-power repetitions remain exactly TWC1.3–7 and TWC5.4. This supplement changes the receiving geometry, not the original zeta function.

## FST1. Same-base square with its complete differential

We construct the coefficientwise completed tensor square on the **same sphere**, not the external square on \(Y\times Y\). Since the support of the two pole skyscrapers is disjoint, their mixed same-base products are zero. Put
\[
V=A\widehat\otimes_\pi A,\qquad
L=(H_\infty\widehat\otimes_\pi A)\oplus(A\widehat\otimes_\pi H_\infty),
\qquad M=H_\infty\widehat\otimes_\pi H_\infty.
\tag{FST1.1}
\]
The explicit sheaf complex is
\[
K=[\underline V_Y^{-2}\xrightarrow{(d_0,d_0)}i_+L\oplus i_-L
\xrightarrow{d_1\oplus d_1}i_+M\oplus i_-M],
\tag{FST1.2}
\]
where, in each pole chart,
\[
d_0(a\otimes a')=(b_ra\otimes a',-a\otimes b_ra'),
\quad d_1(h\otimes a',a\otimes h')=h\otimes b_ra'+b_ra\otimes h'.
\tag{FST1.3}
\]
On elementary tensors the two terms of \(d_1d_0\) cancel. Continuity and density extend that identity to the full completed domain. Thus (FST1.2) is an actual complete coefficient cochain model. It agrees with the termwise tensor of (FST0.1) on the open stratum and the two pole strata, with their restriction maps. No exactness theorem for arbitrary completed tensor products is used or required by this explicit construction. It is a literal completed projective coefficient tensor complex, not a claim to compute an unspecified derived topological tensor functor.

## FST2. The actual same-base global cochain model

The two-pole Čech complex is
\[
V\oplus V\longrightarrow L\oplus L\oplus V
\longrightarrow M\oplus M\oplus V
\tag{FST2.1}
\]
in degrees \((-2,-1,0)\). Its differentials are
\[
(x_+,x_-)\longmapsto(d_0x_+,d_0x_-,x_+-x_-),
\qquad(\ell_+,\ell_-,c)\longmapsto(d_1\ell_+,d_1\ell_-,0).
\tag{FST2.2}
\]
To obtain it, use contractibility of either pole disk for the complete constant coefficient \(V\), and the annular cohomology \(V\) in angular degrees zero and one. The coefficient Poincaré contractions integrate continuous \(V\)-valued forms over compact intervals; completeness makes these integrals exist, and the usual derivative identities prove the contraction coefficientwise. A skyscraper has only its pole-section term and no overlap restriction. Consequently the overlap contributes exactly the third \(V\) in the two successive degrees, and its restriction difference is the last component of (FST2.2). Equivalently, this is the explicit Čech cone of the two pole complexes mapping to \(V[2]\) on the overlap, retaining the annular degree-one coordinate. The cone convention is the one displayed in (FST2.2).

There is a continuous cochain equivalence to
\[
G_2=[V^{-2}\xrightarrow{(d_0,d_0)}L^{-1}\oplus L^{-1}
\xrightarrow{d_1\oplus d_1}M^0\oplus M^0\oplus V^0],
\tag{FST2.3}
\]
with zero differential into its last \(V\). The projection is
\[
p^{-2}(x_+,x_-)=x_-,\quad
p^{-1}(\ell_+,\ell_-,c)=(\ell_+-d_0c,\ell_-),\quad p^0=1.
\tag{FST2.4}
\]
The inclusion is the diagonal in degree \(-2\), \((\ell_+,\ell_-)\mapsto(\ell_+,\ell_-,0)\) in degree \(-1\), and identity in degree zero. The homotopy is \(h^{-1}(\ell_+,\ell_-,c)=(c,0)\), zero elsewhere. Substitution into (FST2.2) gives \(dh+hd=1-ip\), using \(d_1d_0=0\). Hence no unsupported Künneth statement is needed.

The angular \(V\) records the sphere's oriented degree-two class after the shift by two. Under the unshifted positive de Rham comparison, the overlap form \(\vartheta=d\arg z/(2\pi)\) with Čech restriction \(x_+-x_-\) is compared to \(d\chi_+\wedge\vartheta\), whose integral is \(-1\), for \(\chi_+\) equal to one near the zero pole and zero near infinity. Thus this raw overlap coordinate is the negative of the positive integration coordinate. Multiplying this last coordinate by \(-1\) supplies the positively integrated version. The shift by two has de Rham differential \(+d\), unlike the single-shift \(-d\) convention in ACD6. This sign change is retained; it changes neither the zero differential into that term nor its positive covering-degree factor.

The cohomology of the displayed cochain model, with actual quotient topologies, is
\[
H^{-2}(G_2)=\ker d_0,
\quad H^{-1}(G_2)=(\ker d_1\oplus\ker d_1)/\operatorname{diag}(\operatorname{im}d_0),
\]
\[
H^0(G_2)=(M/\operatorname{im}d_1)\oplus(M/\operatorname{im}d_1)\oplus V.
\tag{FST2.5}
\]
Images in these formulas are not assumed closed. In particular an algebraic quotient is not silently replaced by its Hausdorff quotient.

## FST3. The specialization source remains at the first differential

On a punctured pole disk, the complex is \(\underline V[2]\). Its universal-cover nearby coefficient is \(V[2]\), with identity monodromy; this follows from the same constant-coefficient contraction. The map on the lowest stalk cohomology is the inclusion
\[
H^{-2}(i^*K)=\ker d_0\hookrightarrow V.
\tag{FST3.1}
\]
Therefore the actual invariant-cycle cokernel for this degree is
\[
\mathcal R_{\mathrm{sq}}=V/\ker d_0,
\qquad \ker d_0=\ker(b_r\widehat\otimes1_A)\cap\ker(1_A\widehat\otimes b_r).
\tag{FST3.2}
\]
This is a separated Fréchet quotient, since both kernels are closed. The actual target and boundary can also be read directly from the unshifted specialization cone. With cone convention \(\operatorname{Cone}(i^*K\to\Psi K)\), it is
\[
V^{-3}\longrightarrow(V\oplus L)^{-2}\longrightarrow M^{-1},
\quad v\longmapsto(v,-d_0v),\quad(x,\ell)\longmapsto-d_1\ell.
\tag{FST3.4}
\]
Its continuous projection to \([L^{-2}\xrightarrow{-d_1}M^{-1}]\) is \((x,\ell)\mapsto\ell+d_0x\) and identity on \(M\); the inclusion is \(\ell\mapsto(0,\ell)\). The homotopy \(h^{-2}(x,\ell)=x\) proves \(dh+hd=1-ip\). Hence the canonical map from the nearby \(V\) into the degree-minus-two vanishing group is exactly
\[
V\xrightarrow{d_0}\ker d_1=H^{-2}(\Phi K).
\tag{FST3.5}
\]
Its image is the same actual boundary image as (FST3.2), with both summands and the minus sign in (FST1.3). It is not the map \(b_r\widehat\otimes b_r\) into degree zero.

This kernel also has the full original partial-evaluation description
\[
\ker d_0=\{z\in V:
(\mathrm{ev}_{\rho^\#}\Theta\widehat\otimes1_A)z=0,
\ (1_A\widehat\otimes\mathrm{ev}_{\rho^\#}\Theta)z=0
\text{ for every }\rho\in\mathscr Z_O\}.
\tag{FST3.3}
\]
Indeed the coordinate of \((b_r\widehat\otimes1_A)z\) is the first displayed \(A\)-valued evaluation multiplied by the nonzero \(\delta_\rho\), and its line coordinates vanish. Coordinate evaluations separate \(H_\infty\widehat\otimes_\pi A\): the finite coordinate projection \(P_T\widehat\otimes1_A\) tends to identity there. To prove that convergence, it holds on each elementary tensor; its operators are uniformly bounded for every projective seminorm because \(p_N(P_Ty)\le p_N(y)\). Approximation by finite sums then proves it on the completion. Hence zero coordinates imply the zero tensor. The other factor is identical. This proves (FST3.3) without a completed-tensor exactness or injectivity assumption.

The new invariant-cycle source is zero exactly when the original map \(b_r\) is zero. One direction is immediate. For the other, take \(a\) with \(b_ra\ne0\). Then \(a\ne0\), and \(b_ra\otimes a\ne0\): a nonzero coordinate functional on \(b_ra\) and a continuous linear functional nonzero at \(a\), supplied by separation in the Fréchet space \(A\), detect its tensor. Therefore \(d_0(a\otimes a)\ne0\), proving that its class in (FST3.2) is nonzero. This is a theorem about the actual maps, not an assumed splitting of their source extensions.

## FST4. The tensor detector becomes a top boundary, with its lifting distinction retained

Define the continuous map
\[
B_2=b_r\widehat\otimes b_r:V\to M,
\quad H_2:V\to L,
\quad H_2(a\otimes a')=(b_ra\otimes a',0).
\tag{FST4.1}
\]
Direct computation gives
\[
\boxed{\quad d_1H_2=B_2.\quad}
\tag{FST4.2}
\]
There is also the continuous right-factor homotopy \(H_2^{\mathrm R}(a\otimes a')=(0,a\otimes b_ra')\). It obeys \(d_1H_2^{\mathrm R}=B_2\), and the exact difference is \(H_2-H_2^{\mathrm R}=d_0\). The two null-homotopies retain the original first differential in their difference. Consequently the map from \(V[0]\) to a pole's degree-zero \(M\) in the actual complex \(K\), with value \(B_2\), has the explicitly displayed continuous null-homotopy. The same identity applies at either retained pole in (FST2.3). It is not a statement that the first specialization boundary \(d_0\) vanishes: FST3 computes its separate source and image.

The original source quotient map \(q_R:A\to\mathcal R\) gives a continuous tensor map \(q_R\widehat\otimes q_R:V\to\mathscr R_2\). Its algebraic tensor image is dense, because each elementary source tensor has representatives in \(A\). On that image,
\[
B_2=b_2(q_R\widehat\otimes q_R).
\tag{FST4.3}
\]
The identity holds on the whole \(V\) by continuity. For algebraic tensors from \(\mathcal R\otimes\mathcal R\), choosing representatives supplies a top boundary via (FST4.2). For an arbitrary element of its completed tensor source, the same approximation proves only
\[
b_2(\mathscr R_2)\subset\overline{\operatorname{im}d_1}^{\,M}.
\tag{FST4.4}
\]
No surjective completed lift, closed image, or descent of the homotopy is assumed.

The displayed homotopy specifically does not descend through the two source quotients merely from the formula: replacing the second representative by \(a'+a_O\), with \(a_O\in A_O\), changes it by \((b_ra\otimes a_O,0)\), a retained element of \(\ker d_1\). Replacing the first representative by an element of \(A_O\) changes it by zero. Thus the apparent ambiguity is explicitly in the earlier-degree cocycles. It is retained rather than declared absent. The full source extension from ADM5 is still present in this same-base calculation.

## FST5. The exact Hausdorff supported top receiver

TWC2's proof with the whole actual zero set identifies
\[
M\simeq\{z:\sum_{\rho,\lambda}m_\rho m_\lambda
 w_\rho^{2N}w_\lambda^{2N}|z_{\rho,\lambda}|^2<\infty\ \forall N\}.
\tag{FST5.1}
\]
Let \(P_{LL}=P_L\widehat\otimes P_L\) be the continuous coordinate projection to the line-line tuples. Since \(b_rA\subset H_{\infty,O}\), (FST1.3) gives
\(P_{LL}d_1=0\). Conversely every finite coordinate tensor with at least one off-line coordinate belongs to \(\operatorname{im}d_1\): use an original source isolator realizing that coordinate under \(b_r\), and use the other factor's coordinate vector. Finite truncations converge in every norm in (FST5.1). Hence
\[
\boxed{\quad\overline{\operatorname{im}d_1}^{\,M}=\ker P_{LL},
\qquad M/\overline{\operatorname{im}d_1}\simeq
H_{\infty,L}\widehat\otimes_\pi H_{\infty,L}.\quad}
\tag{FST5.2}
\]
This is the exact Hausdorff receiving quotient at each pole. The nonseparated kernel \(\overline{\operatorname{im}d_1}/\operatorname{im}d_1\) of the map from the actual quotient remains explicit. In particular the reflected off-line pairs that survived TWC10's positive **product-cover** receiver are among these same-base supported boundaries after Hausdorff passage. The two constructions have different exact maps; neither is replaced by the other.

## FST6. Single-cover degree, all coefficient terms and endpoints

For a recovered integer \(n\ge1\), let \(R_n\) be the coefficient operator \(T_n\) on \(A\) and \(U_n^*\) on \(H_\infty\). The original intertwining \(b_rT_n=U_n^*b_r\) makes the tensor coefficient operator \(K_n=R_n\widehat\otimes R_n\) a cochain map of each local complex (FST1.1–3). Its inverse is the tensor of the continuous coefficient inverses.

Construct the genuine **single** cover \(f_n(z)=z^n\) on the same sphere. There are \(n\) nearby sheets for the coefficient \(V\), not \(n^2\). Its unit is the \(n\)-fold diagonal with coefficient \(K_n\); its weighted trace is sheet sum with coefficient \(K_n^{-1}\). On the constant pole term this is \(nK_n^{-1}\), and on each supported pole term take the same \(nK_n^{-1}\). These choices make all differential squares commute, because \(K_n\) is a cochain map. They therefore define actual maps of the displayed sheaf complex. Trace after unit is \(nI\); reverse order is the full nearby deck norm, and \(nI\) on each supported pole term. No augmentation sheet is discarded.

On the global model (FST2.3), the coefficient terms carry pullback \(K_n\) and weighted trace \(nK_n^{-1}\). The angular term carries instead
\[
n(T_n\widehat\otimes T_n),\qquad
T_{1/n}\widehat\otimes T_{1/n},
\tag{FST6.1}
\]
whose composite is \(nI\). Pullback has positive angular degree \(n\); the angular trace of the cover, before its chosen coefficient weighting, has factor one. Switching the raw angular coordinate to the positive integration coordinate conjugates both actions by the same sign and leaves (FST6.1) unchanged.

This is not the tensor of the original two weighted trace maps: on coefficient terms that tensor is \(n^2K_n^{-1}\), whereas the constructed same-base weighted trace is \(nK_n^{-1}\). Their exact comparison factor is \(1/n\). The distinction follows from the computed sheet count and is retained, not absorbed into a renamed action. The diagram is a single-cover tensor coefficient construction, not the external product of two degree-\(n\) covers.

For endpoints let \(E=i_+E_+\oplus i_-E_-\), with original coordinate labels \((c_0,c_1,d_0,d_1)\). The full source is \(P\oplus E[1]\); its square is exactly
\[
K\oplus(P\widehat\otimes E[1])\oplus(E[1]\widehat\otimes P)
\oplus(E\widehat\otimes E)[2].
\tag{FST6.2}
\]
At a fixed pole, the first mixed complex has terms \(A\otimes E_p\to H_\infty\otimes E_p\) in degrees \((-2,-1)\), differential \(+b_r\otimes1\); the second has \(E_p\otimes A\to E_p\otimes H_\infty\) in the same degrees, differential \(-1\otimes b_r\). The last endpoint tensor is in degree \(-2\), with zero differential. Endpoint tensors at distinct poles are zero because their supports are disjoint. Each finite-dimensional endpoint factor uses its original pullback character \(e(n)\in\{1,n\}\); the same-base square pullback multiplies the factor characters, and its weighted trace is \(n\) times the inverse product, exactly as for \(K_n\). In the original ordered tensor bases \((c_0c_0,c_0c_1,c_1c_0,c_1c_1)\) and \((d_0d_0,d_0d_1,d_1d_0,d_1d_1)\), the endpoint-square unit and weighted trace lists are respectively
\[
(1,n,n,n^2),\ (n,1,1,n^{-1});\qquad
(n^2,n,n,1),\ (n^{-1},1,1,n).
\]
Each coordinatewise product is \(n\). Thus all endpoint words, both mixed signs and their actual single-cover factors are retained. The same Čech reduction leaves all these supported endpoint terms unchanged, since the contraction acts only on the two constant V copies and their overlap. They have no nearby term. At a pole \(p\), the full lowest stalk group and specialization map are exactly
\[
\ker d_0\oplus(A_O\otimes E_p)\oplus(E_p\otimes A_O)\oplus(E_p\otimes E_p)
\longrightarrow V,\qquad(z,\xi,\eta,\epsilon)\longmapsto z.
\tag{FST6.3}
\]
Finite dimensionality of \(E_p\) identifies the two mixed kernels with the displayed finite direct sums of \(A_O\). Thus the full specialization domain retains these additional kernels; its image and cokernel are unchanged from FST3. Their highest new degree is minus one, with zero differential into \(M\), so they do not alter the supported top quotient in (FST5.2).

## FST7. What the fixed-base calculation proves

The same-base tensor square now has a constructed global model, the true single-sphere angular factor \(n\), all supported terms and endpoints, and its actual invariant-cycle source. It is not an independently chosen extension. Its first specialization obstruction is (FST3.2), and it vanishes exactly when the original actual boundary vanishes. The tensor detector in the later supported degree has the different fate (FST4.2): it is already a boundary on the original coefficient source, with its quotient-lifting ambiguity retained. The exact completed supported receiver is (FST5.2).

Thus obtaining the fixed geometric \(+2\) on one sphere does not permit applying Deligne's pole argument to the vanished top detector as if that detector were a surviving eigenclass. The map, its degree and its source quotient must be carried together. The calculation has done that for the actual square. TWC10 retains the original tensor Weil pairing on its specified source; no descent of that pairing to the different quotient in FST3.2 is asserted here. It supplies concrete same-base maps beyond TWC's external-product comparison without declaring the original \(b_r\), its first specialization source, or its full derived connecting class zero.

Reading and provenance: the frozen TWC proof and independent TRC calculation; ADM's full source/domain construction; ACD6–8's actual sphere, finite-sheet unit/trace and full endpoint comparison; DCA's distinct raw-cut correction and angular conventions; and DP3–DP6's reconstruction of Deligne's fixed-curve tensor-power argument. The human origins remain Connes–Consani, [arXiv:0903.2024v3 §5](https://arxiv.org/abs/0903.2024v3), and Deligne, [La conjecture de Weil. II](https://numdam.org/item/PMIHES_1980__52__137_0/), with the previously recorded author-source versus transcription distinctions. No new whole-human-paper reading is claimed. The new same-base square is a programme derivation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
