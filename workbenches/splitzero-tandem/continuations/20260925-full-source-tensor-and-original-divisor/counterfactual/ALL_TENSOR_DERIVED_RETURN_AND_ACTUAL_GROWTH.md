# All tensor powers of the derived return and their actual growth estimates

25 September 2026. Independent derivation ATG0–ATG10.

## ATG0. Source, earlier results, and the specific new calculation

The earlier [QS6–QS9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/deligne_quotient_weight_20260924/QUOTIENTS_AND_TENSOR_WEIGHT_ERROR.md) already compute finite primary tensor blocks and their exact exponential errors. The [Deligne reconstruction, D1–D7 and P2](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/deligne_quotient_weight_20260924/DELIGNE_GLOBAL_QUOTIENT_AND_WEIGHT.md) retains the two distinct amplification mechanisms and the full shifted-zeta tensor Euler product. Those calculations were read for this continuation. They are not claimed as new results here.

The new calculation uses the actual full coefficient sheaf and every product degree after [DER](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/DIAGONAL_EXTRAORDINARY_RETURN.md), [FEM](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/FULL_SOURCE_RETURN_EQUIVARIANCE_AND_MIXED_TENSOR_CLASS.md), and [GMC](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/GLOBAL_MIXED_RETURN_CONTRACTION.md): all \(H\) factors, all \(Q\) factors, the whole diagonal right adjoint, the original residue trace, and quantitative seminorm estimates with their dependence on the tensor exponent.

Human sources remain Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), Ralf Meyer, [arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3), and Pierre Deligne, [*La conjecture de Weil. II*](https://www.numdam.org/item/PMIHES_1980__52__137_0/). The exact Mellin image and return are the prior [OMS](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md) results, and the original residue form is [GZR](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md). The human-source reading kinds and coverage remain those of their retained ledgers; no new original-author reading is claimed by citing these programme calculations.

Primitive \(Z_1/\tau\) receives no addition, parity, numerical coordinate or weight. The whole corrected source and its lattice are retained. Every tensor and polynomial below belongs to the stated complex receiving category. Tensor cohomology is algebraic; each analytic seminorm and each continuous map is separately specified. No completed-tensor cohomology identification is assumed.

Write
\[
F=(W_+\xrightarrow{r_+}A\xleftarrow{r_-}W_-),\quad
W_\pm=(S\oplus\mathbb C^2_\pm)\oplus V_\pm^{\rm extra},
\]
\[
r_+=\Sigma,\quad r_-=R\Sigma\text{ on }S,\qquad
\Sigma h(u)=2\sum_{n\ge1}h(nu),\quad Rb(u)=u^{-1}b(u^{-1}).
\]
All endpoint and extra restrictions are zero. The original common image is the closed subspace \(J\), and
\[
Q=A/J,\quad
D=[P=W_+\oplus W_-\xrightarrow{r_+-r_-}A],\quad H=\ker d.
\]
Let \(E_\pm=\ker r_\pm=\mathbb C^2_\pm\oplus V_\pm^{\rm extra}\). The embeddings \(E_+\to H\), \(e\mapsto(e,0)\), and \(E_-\to H\), \(e\mapsto(0,e)\), have disjoint images. They preserve the original source and spectral actions.

## ATG1. The complete k-fold product complex

Fix an integer \(k\ge1\), and order the coordinates \(1,\ldots,k\). For \(F_k=F^{\boxtimes k}\) on \(Y^k\), the ordered product Čech complex is
\[
D_k=D^{\otimes k},\qquad
D_k^j=\bigoplus_{\substack{I\subset\{1,\ldots,k\}\\|I|=j}}
\bigotimes_{\nu=1}^k V_{\nu,I},\qquad
V_{\nu,I}=\begin{cases}A,&\nu\in I,\\P,&\nu\notin I.\end{cases}
\tag{ATG1.1}
\]
On a homogeneous tensor, its differential is the full formula
\[
d(x_1\otimes\cdots\otimes x_k)
=\sum_{\nu=1}^k(-1)^{\deg x_1+\cdots+\deg x_{\nu-1}}
x_1\otimes\cdots\otimes dx_\nu\otimes\cdots\otimes x_k.
\tag{ATG1.2}
\]
It squares to zero because applying the differentials at two distinct coordinates occurs twice with opposite signs, and each one-factor differential squares to zero.

This computes \(R\Gamma(Y^k,F_k)\). Tensoring the finite projective resolutions of the constant sheaf from FTD2 gives a projective resolution on \(Y^k\): exactness is stalkwise tensor exactness over \(\mathbb C\); each product projective represents evaluation at a minimal product open. Applying Hom gives precisely ATG1.1–ATG1.2, with the displayed ordering. Equivalently, every intersection in the ordered product cover is a minimal open and has exact section evaluation.

Its complete cohomology is canonically
\[
\boxed{
H^j(D_k)=
\bigoplus_{\substack{I\subset\{1,\ldots,k\}\\|I|=j}}
\bigotimes_{\nu=1}^k C_{\nu,I},\qquad
C_{\nu,I}=\begin{cases}Q,&\nu\in I,\\H,&\nu\notin I.\end{cases}}
\tag{ATG1.3}
\]
One proof retains all degrees by choosing vector-space complements in
\(P\to J\subset A\): \(D\) is a direct sum of \(H[0]\), \(Q[-1]\), and a complex \([J\xrightarrow1J]\). The latter is contractible. Its tensor with any bounded complex is contractible by its degree-minus-one contraction tensored with identity; the two cross terms cancel using ATG1.2. Expanding all \(k\) factors proves ATG1.3. The isomorphism is the canonical map sending tensors of cycles to their cohomology classes, so its equivariance does not depend on the complements used in this proof. No equivariant section \(Q\to A\) is asserted.

Every factor \(H\) retains the entire Fourier graph, all four endpoints and both extra closed copies. The formula has not been truncated to degree \(k\).

## ATG2. The actual k-fold diagonal right adjoint

Define
\[
\Delta_k:Y\to Y^k,\quad y\mapsto(y,\ldots,y),
\]
\[
q_k:Y^k\to Y,\qquad
q_k(c_+,\ldots,c_+)=c_+,\quad
q_k(c_-,\ldots,c_-)=c_-,
\]
and \(q_k=\eta\) at every other point. Write
\[
O_+=Y^k\setminus\{c_-^k\},\quad
O_-=Y^k\setminus\{c_+^k\},\quad
O_\eta=Y^k\setminus\{c_+^k,c_-^k\}.
\tag{ATG2.1}
\]
For \(k=1\) these formulas are the original opens. The two removed points are closed, so \(q_k^{-1}U_x=O_x\) proves continuity. Also \(q_k\Delta_k=\operatorname{id}\).

The intersection of \(k\) minimal opens is \(U_+\) when every coordinate is \(c_+\), \(U_-\) when every coordinate is \(c_-\), and \(U_\eta\) otherwise. Therefore, on every stalk and restriction,
\[
\boxed{\Delta_{k*}=q_k^{-1},\qquad R\Delta_k^!=Rq_{k*}.}
\tag{ATG2.2}
\]
The first functor is exact. The second identity follows from \(q_k^{-1}\dashv q_{k*}\), using injective resolutions, as in DER2. For every bounded complex \(G\),
\[
R\Gamma(Y,Rq_{k*}G)=R\Gamma(Y^k,G)
\tag{ATG2.3}
\]
term by term on those resolutions. For \(k\ge2\), the diagonal is not closed and is not assigned a closed-immersion formula.

Here is a complete stalk-complex model for this return on \(F_k\). Define the one-support complexes
\[
C_+=[W_+\xrightarrow{r_+}A],\qquad
C_-=[W_-\xrightarrow{r_-}A]
\quad(\deg=0,1)
\]
and their actual maps to \(D\):
\[
i_+^0(w)=(w,0),\quad i_+^1(a)=a,\qquad
i_-^0(w)=(0,w),\quad i_-^1(a)=-a.
\tag{ATG2.4}
\]
The cochain identities follow by applying \(d=r_+-r_-\). The minus sign is the original ordered support sign.

Put \(D_k=D^{\otimes k}\), \(C_{\pm,k}=C_\pm^{\otimes k}\), and \(i_{\pm,k}=i_\pm^{\otimes k}\). Then the full stalk models are
\[
\begin{aligned}
(Rq_{k*}F_k)_{c_+}&=\operatorname{Cone}(i_{-,k}:C_{-,k}\to D_k),\\
(Rq_{k*}F_k)_{c_-}&=\operatorname{Cone}(i_{+,k}:C_{+,k}\to D_k),\\
(Rq_{k*}F_k)_\eta&=\operatorname{Cone}(i_{+,k}+i_{-,k}:
 C_{+,k}\oplus C_{-,k}\to D_k).
\end{aligned}
\tag{ATG2.5}
\]
Our cone has \(\operatorname{Cone}(f)^n=D_k^n\oplus C^{n+1}\) and differential
\[
d(x,y)=(d_Dx+fy,-d_Cy).
\tag{ATG2.6}
\]
Both closed-to-generic restrictions are identity on \(D_k\), together with the inclusion of the stated support summand into \(C_{+,k}\oplus C_{-,k}\). Thus ATG2.5 includes every restriction, not only the stalk cohomology dimensions.

To prove this model, the local-support complex at a closed point \(c_\pm\) is \(C_\pm\), with map ATG2.4 to global sections. This is the exact mapping-fibre calculation of FTD5. Use the actual finite injective resolution
\[
0\to F\to I_\eta(A)\oplus I_+(W_+)\oplus I_-(W_-)
\to I_+(A)\oplus I_-(A)\to0.
\]
Here the two closed differentials are \((b,w_\pm)\mapsto b-r_\pm w_\pm\). External products of these injectives are injective: the product of \(I_{x_\nu}(V_\nu)\) represents the right adjoint to evaluation at the product point, with coefficient \(\bigotimes V_\nu\). Vector spaces over \(\mathbb C\) are injective, and tensor exactness makes the total external resolution an injective resolution of \(F_k\). On an elementary product injective, sections supported on the all-plus corner vanish unless every factor is \(I_+\); in that remaining case they are exactly the tensor of the coefficient spaces. The analogous assertion holds for the all-minus corner. Thus applying supported sections to this resolution is termwise the tensor of the one-factor supported-section complexes. The map to global sections is the tensor of their one-factor maps. Comparing with their explicit one-factor mapping-fibre representatives gives exactly \(C_{\pm,k}\) and \(i_{\pm,k}\), including the tensor signs in ATG2.4. This argument does not require the unrefined corner-complement intersections to be minimal opens.

The one-factor comparison and its signs can be verified without choosing an unrecorded equivalence. Global sections of the displayed injective resolution give
\[
X^0=A\oplus W_+\oplus W_-,\quad X^1=A\oplus A,\qquad
d_X(b,w_+,w_-)=(b-r_+w_+,\,b-r_-w_-).
\]
The chain map to \(D\) is
\[
\pi^0(b,w_+,w_-)=(w_+,w_-),\qquad \pi^1(u,v)=v-u.
\]
Its kernel is \([A\to\operatorname{diag}(A,A)]\), \(b\mapsto(b,b)\), an explicit contractible complex. Thus \(\pi\) is a quasi-isomorphism. Supported sections at \(c_\pm\) give \([W_\pm\xrightarrow{-r_\pm}A]\); the map from \(C_\pm\) to this complex is identity in degree zero and minus identity in degree one. Its inclusion into \(X\) followed by \(\pi\) is exactly \(i_\pm\) in ATG2.4. Tensoring these comparisons gives commuting maps from the full product support complexes into \(D_k\). Tensor exactness and the displayed contraction prove the required quasi-isomorphisms. The cone models therefore retain the actual restrictions with these signs.

Sections supported on the two disjoint closed corners split as their direct sum: restrict to the complements of the other corner and glue with zero on their intersection. This construction also applies termwise to the injective resolution. The open/closed localization triangle for each complement in ATG2.1 is therefore exactly its cone in ATG2.5. Naturality of the localization construction gives the displayed restrictions.

## ATG3. All cohomology degrees of the returned sheaf

Set \(V_j=H^j(D_k)\), retaining its ordered decomposition ATG1.3, and set
\[
A_{\pm,j}=
\bigoplus_{|I|=j}
\bigotimes_{\nu=1}^k B_{\pm,\nu,I},\qquad
B_{\pm,\nu,I}=\begin{cases}Q,&\nu\in I,\\E_\pm,&\nu\notin I.\end{cases}
\]
The cohomology map \(A_{+,j}\to V_j\) uses the embeddings \(E_+\to H\) and identity on each \(Q\). The map \(A_{-,j}\to V_j\) uses \(E_-\to H\), with the exact scalar \((-1)^j\) from its \(j\) degree-one factors. Denote their images by \(S_{+,j},S_{-,j}\). Both maps are injective by tensor exactness.

For \(j<k\), the two images intersect trivially. In every ordered summand at least one factor is \(H\); its \(E_+\) and \(E_-\) subspaces are disjoint, so the corresponding two tensor subspaces have zero intersection, as a vector-space direct decomposition of that factor proves. At \(j=k\), both source spaces are \(Q^{\otimes k}\), and the map from their sum is
\[
(u,v)\longmapsto u+(-1)^kv.
\tag{ATG3.1}
\]

The exact cohomology sequence of each cone now gives
\[
(R^jq_{k*}F_k)_{c_+}=V_j/S_{-,j},\qquad
(R^jq_{k*}F_k)_{c_-}=V_j/S_{+,j}\quad(0\le j<k),
\tag{ATG3.2}
\]
and both closed stalks vanish in degree \(k\) and above. For the generic stalk, the complete formulas are
\[
(R^jq_{k*}F_k)_\eta
=V_j/(S_{+,j}+S_{-,j})\qquad(0\le j<k-1),
\tag{ATG3.3}
\]
and the actual remaining extension is
\[
\boxed{
0\to V_{k-1}/(S_{+,k-1}+S_{-,k-1})
\to (R^{k-1}q_{k*}F_k)_\eta
\to \ker[(1,(-1)^k):Q^{\otimes k}\oplus Q^{\otimes k}\to Q^{\otimes k}]
\to0.}
\tag{ATG3.4}
\]
Its kernel on the right is isomorphic to \(Q^{\otimes k}\), with the signs in ATG3.1 retained. The generic groups in degree \(k\) and above vanish. For \(k=1\), ATG3.4 is the original row \(0\to J\to A\to Q\to0\). For \(k=2\), it is exactly the earlier mixed row \(0\to(J\otimes Q)\oplus(Q\otimes J)\to Q_\Delta\to Q\otimes Q\to0\), with the explicit identification in DER7.

All restriction maps and extension classes in these formulas are induced by the full cones ATG2.5. In particular this has not replaced the extension in ATG3.4 by a direct sum. For \(k>2\), the lower quotients still contain mixed choices of the two endpoint-support types inside the \(H\) factors. They are not removed by the two all-equal-corner quotients.

## ATG4. Ordered diagonal return of the trace target

For a specified coefficient vector space \(V\) with its already given action, let
\[
K_k(V)=j_{\eta^k!}V=P_\eta^{\boxtimes k}\otimes V .
\]
The one-factor global and one-support complexes for \(P_\eta\) are each \(\mathbb C[-1]\); their support maps are \(+1\) and \(-1\). ATG2.5 therefore gives an especially explicit target model. Its closed stalks are
\[
[\,V\xrightarrow{(-1)^k}V\,]\text{ at }c_+,\qquad
[\,V\xrightarrow{+1}V\,]\text{ at }c_-,
\]
and its generic stalk is
\[
[\,V\oplus V\xrightarrow{(1,(-1)^k)}V\,],
\tag{ATG4.1}
\]
all in degrees \(k-1,k\). The restrictions in degree \(k-1\) include the closed-plus copy as the second generic copy and the closed-minus copy as the first; in degree \(k\) both are identity. These give an actual sheaf complex.

Its only cohomology sheaf is \(j_{\eta!}V\) in degree \(k-1\). A specified quasi-isomorphism sends the generic generator \(z\) to
\[
((-1)^{k+1}z,z)
\]
in the degree-\((k-1)\) term of ATG4.1. Thus
\[
\boxed{R\Delta_k^!K_k(V)\simeq j_{\eta!}V[-(k-1)].}
\tag{ATG4.2}
\]

The complete model ATG4.1 retains the original ordered trace. Its degree-\((k-1)\) sheaf is \(P_-\otimes V\oplus P_+\otimes V\), both globally acyclic with zero global sections; its degree-\(k\) sheaf is the constant \(I_\eta(V)\), with sections \(V\) and no higher cohomology. Hence its global complex has only \(V\) in degree \(k\), and the trace is the identity on that coordinate.

The sign of the displayed quasi-isomorphism can also be checked directly. Put \(\epsilon=(-1)^k\), \(\sigma=(-1)^{k-1}\), and use total differential \(d_{\rm internal}+(-1)^{\rm internal\ degree}d_{\rm Cech}\), with original Čech difference \(r_+-r_-\). A local degree-\((k-1)\) pair \((a,b)\) has differential
\[
(\epsilon a,b;\ -\sigma b,\sigma a)
\]
in the two closed degree-\(k\) coordinates and the two overlap degree-\((k-1)\) coordinates. The image of \(z\) under the quasi-isomorphism has overlap coordinates \((-\epsilon z,z)\). Subtract the boundary with \(a=\sigma z\), \(b=-z\). The overlap becomes zero and the two closed coordinates become \((z,z)\). Their global value is \(z\). This proves the exact trace coefficient \(+1\), for every \(k\).

The counit \(\Delta_{k*}R\Delta_k^!K_k(V)\to K_k(V)\) is restriction/evaluation on an injective resolution, as in DER5. Taking global sections identifies it with the identity between the equal section complexes in ATG2.3. It therefore preserves this same ordered trace, including its coefficient and degree. No Tate or numerical character is created by the shift \(k-1\); the action remains the given action on \(V\).

## ATG5. The k-fold original residue form, full constants and orientation

The original raw two-input form is
\[
B_A(a,b)=\frac1{2\pi i}
\left(\int_{\Re s=2}^{\uparrow}-\int_{\Re s=-1}^{\uparrow}\right)
\frac{M_0a(s)M_0b(1-s)}{\zeta(s)}\,ds.
\]
Keep the full original reciprocal bounds
\[
|\zeta(2+it)^{-1}|\le\zeta(2),\qquad
|\zeta(-1+it)^{-1}|\le
4\pi^2\zeta(2)(1+|t|)^{-3/2}.
\tag{ATG5.1}
\]
The second bound follows from the original multiplier
\[
\chi_\zeta(s)=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)},\qquad
|\chi_\zeta(-1+it)|^2=
\pi^{-3}(t/2)\coth(\pi t/2)((t/2)^2+1/4),
\]
with its continuous value at \(t=0\), as proved in GZR2. No completed denominator is used.

Let \(b_{2,1}(F)=\sup_{|\Re s|\le2}(1+|\Im s|)|F(s)|\). The two integrals and
\(\int_{\mathbb R}(1+|t|)^{-2}dt=2\) give
\[
|B_A(a,b)|\le C_\zeta\,b_{2,1}(M_0a)b_{2,1}(M_0b),
\qquad C_\zeta=\frac{\zeta(2)(1+4\pi^2)}{\pi}.
\tag{ATG5.2}
\]
Its exact descent through \(J\) in both slots is the prior original Schwartz-division theorem, including the endpoint and trivial-zero terms.

Define the algebraic tensor form on \(Q^{\otimes k}\) by
\[
B_k(x_1\otimes\cdots\otimes x_k,\ y_1\otimes\cdots\otimes y_k)
=\prod_{\nu=1}^k B_\zeta(x_\nu,y_\nu).
\tag{ATG5.3}
\]
For actual finite sums of test tensors, its full contour formula is
\[
\frac1{(2\pi i)^k}
\sum_{\epsilon_1,\ldots,\epsilon_k\in\{2,-1\}}
(-1)^{\#\{\nu:\epsilon_\nu=-1\}}
\int_{\Re s_1=\epsilon_1}^{\uparrow}\cdots
\int_{\Re s_k=\epsilon_k}^{\uparrow}
\frac{F(s_1,\ldots,s_k)G(1-s_1,\ldots,1-s_k)}
{\prod_{\nu=1}^k\zeta(s_\nu)}\,ds_1\cdots ds_k.
\tag{ATG5.4}
\]
Every original denominator and all \(2^k\) boundary-contour terms remain. Absolute convergence follows first for simple tensors from ATG5.2, and then for finite sums. The separate original division theorem gives descent in each factor.

For the projective tensor seminorm built from the quotient seminorm induced by \(b_{2,1}\), ATG5.2 gives
\[
\boxed{|B_k(X,Y)|\le C_\zeta^k\,
 \overline b_{2,1}^{\,\otimes_\pi k}(X)
 \overline b_{2,1}^{\,\otimes_\pi k}(Y).}
\tag{ATG5.5}
\]
Take an arbitrary finite tensor decomposition, apply the product bound, sum, and infimize over decompositions and representatives. This proves the displayed bound and its continuous extension to the corresponding completed projective tensors, without identifying that completion with algebraic sheaf cohomology.

The generic coefficient map on the product of \(2k\) sites with coordinate order
\((x_1,\ldots,x_k,y_1,\ldots,y_k)\) is ATG5.3, with target
\(K_{2k}(\chi_{\rm dil}^k\mathbb C)\). It kills every incoming restriction because one factor then belongs to \(J\). It is therefore a sheaf map. Its ordered trace uses ATG4 with \(2k\) factors.

If instead it is formed as the tensor of the \(k\) original degree-two pairing maps, using interleaved order
\((x_1,y_1,\ldots,x_k,y_k)\), the graded shuffle on top degree contributes
\[
(-1)^{k(k-1)/2}.
\tag{ATG5.6}
\]
There are exactly \(k(k-1)/2\) crossings of degree-one factors \(y_i,x_j\) with \(i<j\). Thus the standard shuffled derived tensor of the pairing maps is this sign times ATG5.3. The two ordered descriptions and their exact sign are retained; neither is silently substituted for the other.

For all \(a>0\), substitution in each original Mellin coordinate gives
\[
\boxed{B_k(T_a^{\otimes k}X,T_a^{\otimes k}Y)=a^k B_k(X,Y).}
\tag{ATG5.7}
\]
Indeed each factor in the integrand receives \(a^{s_\nu}a^{1-s_\nu}=a\). The target character is therefore the actual \(\chi_{\rm dil}^k\), of numerical weight \(2k\), not a claim that each input has weight \(k\). Currying retains the entire dual complex and the degree shift \(-2k\); all lower \(H\)-containing cohomology factors remain in its source and target, even though this scalar top trace is zero on degrees below \(2k\).

## ATG6. Exact operator growth from the original Schwartz topology

For \(N,j\ge0\), retain the original seminorm
\[
p_{N,j}(a)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|.
\]
Since Euler differentiation commutes with \(T_ta(u)=a(u/t)\), direct substitution gives
\[
p_{N,j}(T_ta)
=\sup_{v>0}(t^Nv^N+t^{-N}v^{-N})|(v\partial_v)^ja(v)|
\le \max(t^N,t^{-N})p_{N,j}(a).
\tag{ATG6.1}
\]
For fixed \(t\ge1\), \(N>0\), this exponent is sharp on the original test space: choose a nonzero smooth compactly supported function in logarithmic coordinates and translate its support toward \(+\infty\). On the translated support, the ratio
\((t^Nv^N+t^{-N}v^{-N})/(v^N+v^{-N})\) tends uniformly to \(t^N\). Apply it to the fixed nonzero \(j\)-th Euler derivative of that function. The corresponding seminorm ratio tends to \(t^N\). Thus the source operator seminorm cannot be reduced by treating the coordinate weights as independent of the dilation.

The quotient seminorm
\[
\nu([a])=\inf_{h\in J}p_{1,0}(a+h)
\tag{ATG6.2}
\]
is a genuine norm on the actual \(Q\), though no assertion that this single norm is complete is made. To prove separation, for any actual zero \(\rho=\beta+i\gamma\), \(0<\beta<1\), and integer \(j\ge0\),
\[
|(M_0a)^{(j)}(\rho)|
\le p_{1,0}(a)
 \int_0^\infty\frac{|\log u|^j u^\beta}{u+u^{-1}}\frac{du}{u}
\]
\[
\le j!\left((1-\beta)^{-j-1}+(1+\beta)^{-j-1}\right)p_{1,0}(a).
\tag{ATG6.3}
\]
For the second bound put \(x=\log u\) and use
\((e^x+e^{-x})^{-1}\le e^{-|x|}\), then integrate the two exponential moments. If \(\nu([a])=0\), apply this bound to representatives with arbitrarily small \(p_{1,0}\). All original zero jets vanish. The exact original synthesis theorem then gives \(a\in J\), proving separation.

Taking the infimum in ATG6.1 proves, for \(t\ge1\),
\[
\nu(T_t x)\le t\,\nu(x).
\]
On the algebraic projective tensor norm, it gives the uniform-in-\(k\) formula
\[
\boxed{\nu^{\otimes_\pi k}(T_t^{\otimes k}X)
 \le t^k\nu^{\otimes_\pi k}(X).}
\tag{ATG6.4}
\]
The projective norm is nondegenerate on algebraic tensors: continuous linear functionals on the normed factors separate each finite tensor, by extension from its finite-dimensional factor spans. For simple tensors the projective norm is the product of the factor norms, by the upper bound from that decomposition and the matching lower bound from norm-one functionals. Thus ATG6.4 is a bound on a separating norm of the whole actual tensor quotient, not an observation that discards some primary blocks.

A tempting smaller seminorm does discard such data. The original \(p_{0,0}=2\sup|a|\) satisfies \(p_{0,0}(T_ta)=p_{0,0}(a)\). Its quotient seminorm \(\nu_0\) is invariant under both \(T_t\) and \(T_t^{-1}\). On every actual primary block with \(0<\Re\rho<1\), however,
\[
\nu_0|_{Q_\rho}=0.
\tag{ATG6.5}
\]
For an eigenvector \(x\), invariance and \(T_px=p^\rho x\) imply
\(\nu_0(x)=p^{\Re\rho}\nu_0(x)\), hence zero. Induct up a Jordan chain: all lower vectors already have zero seminorm, so the triangle inequality applied in both directions identifies the seminorm of \(T_px\) with that of \(p^\rho x\), giving the same conclusion. Therefore the isometric bound in this seminorm cannot be used as a bound that still sees these zeros. This is a calculated quotient defect, not a new purity assertion.

The raw Mellin seminorms give the corresponding formula
\[
b_{B,M}(M_0T_ta)\le t^B b_{B,M}(M_0a)\qquad(t\ge1),
\tag{ATG6.6}
\]
because \(|t^s|=t^{\Re s}\) on \(|\Re s|\le B\). Their tensor exponents are \(kB\), with every factor retained.

## ATG6A. Exact comparison with the jointly faithful vertical Hilbert return

After the preceding calculation, the complete independent [VWR0–VWR9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/FULL_VERTICAL_WEIGHT_RETURN.md) was read. Its original coefficient maps are
\[
\alpha_{\sigma,N}:Q\longrightarrow
Q_{\sigma,N}=\mathcal H_{\sigma,N}/\overline J^{\,\mathcal H_{\sigma,N}},
\quad
\mathcal H_{\sigma,N}=
L^2(\mathbb R_{>0},u^{2\sigma-1}(1+(\log u)^2)^Ndu).
\]
For \(0<\sigma<1\), \(N\ge1\), its exact source norm and quotient upper bound are
\[
\|T_t\|_{\mathcal H_{\sigma,N}}
=t^\sigma\Lambda_+(\log t)^{N/2},\qquad
\|T_t\|_{Q_{\sigma,N}}\le
t^\sigma\Lambda_+(\log t)^{N/2},
\]
\[
\Lambda_+(v)=\frac{v^2+2+|v|\sqrt{v^2+4}}2.
\tag{ATG6A.1}
\]
VWR4–VWR5 proves the kernel: the receiver sees precisely the original derivatives at zeros with real part \(\sigma\) and derivative order \(j<N-1/2\). The entire family is injective on \(Q\), including all multiplicities.

For every ordered tuple \((\boldsymbol\sigma,\boldsymbol N)\), construct the exact tensor map
\[
\alpha_{\boldsymbol\sigma,\boldsymbol N}:
Q^{\otimes k}\longrightarrow
\widehat{\bigotimes}_{\nu=1}^k Q_{\sigma_\nu,N_\nu}
\tag{ATG6A.2}
\]
by the algebraic tensor of the original maps followed by the Hilbert tensor inclusion. Every map is equivariant, and the family of all these maps is jointly injective on the algebraic tensor. To prove that assertion, continuous linear functionals composed with the maps \(\alpha_{\sigma,N}\) separate \(Q\): a nonzero vector has a nonzero image in some Hilbert quotient, where its inner product with that image is a separating functional. On any finite-dimensional subspace of \(Q\), the restrictions of these functionals span its full dual, since their common annihilator is zero. A nonzero finite tensor is separated by a product of dual functionals on its finite-dimensional factor spans. Expand each of those functionals into a finite linear combination from this separating family; at least one resulting product is nonzero on the tensor. That product factors through one of ATG6A.2. This proves joint injectivity without identifying an algebraic tensor of infinite products with their completed product.

The operator bound on this actual receiving component is
\[
\boxed{\|T_t^{\otimes k}\|_{\boldsymbol\sigma,\boldsymbol N}
 \le t^{\sigma_1+\cdots+\sigma_k}
 \Lambda_+(\log t)^{(N_1+\cdots+N_k)/2}.}
\tag{ATG6A.3}
\]
For elementary tensors it follows by multiplication of the one-factor norms. The Hilbert tensor operator bound follows first on finite sums from the tensor product of positive operators \(T_t^*T_t\), whose norm is bounded by the product of the factor norms, and then by density. Equivalently, the usual Hilbert tensor norm identity for bounded operators follows by applying orthonormal expansions one factor at a time; the reverse inequality is obtained on simple vectors approaching each factor norm. This establishes the operator calculation on the stated completion. It does not replace algebraic sheaf cohomology by that completion.

Taking \(t=p^\ell\) leaves the exact exponential exponent
\(\sigma_1+\cdots+\sigma_k\). The \(\Lambda_+\) factor is polynomial in \(\ell\) for fixed \(k,\boldsymbol N\), so its \(\ell\)-th root tends to one. On an actual tensor of primary blocks, ATG6A.2 can retain a nonzero vector only if
\(\sigma_\nu=\Re\rho_\nu\) in every factor and its derivative orders fall below the respective thresholds. Increasing the \(N_\nu\) retains every derivative. Thus the improved exponent in each component is accompanied by a proved, explicit selection map.

The family with every \(\sigma_\nu=1/2\) has the exact common kernel
\[
\boxed{
\sum_{\nu=1}^k
 Q^{\otimes(\nu-1)}\otimes K_{\rm off}
 \otimes Q^{\otimes(k-\nu)}.}
\tag{ATG6A.4}
\]
Indeed VWR5 identifies the one-factor common kernel as \(K_{\rm off}\). Every map factors through \(Q/K_{\rm off}\), and the induced family on that quotient is jointly injective. The finite-tensor separation argument above therefore proves joint injectivity on \((Q/K_{\rm off})^{\otimes k}\). Tensor exactness over \(\mathbb C\) identifies the kernel of \(Q^{\otimes k}\to(Q/K_{\rm off})^{\otimes k}\) with the displayed sum, proving ATG6A.4.

Consequently the genuine exponent \(k/2\) on the critical Hilbert components and the faithful original estimate \(k\) in ATG6.4 concern explicit different maps. The full vertical family remains faithful and has the component exponents \(\sum\sigma_\nu\); reflection pairs each \(\sigma_\nu\) with \(1-\sigma_\nu\), with the full raw factor \(t\) per pair. No claim that a critical-family kernel is zero was inserted. This comparison retains both the stronger Hilbert bound and its exact original-domain kernel.

## ATG7. The bounds in every H/Q cohomology degree

For a Schwartz function on the original real line put
\[
\sigma_{N,j}(h)=\sup_{x\in\mathbb R}(1+|x|)^N|h^{(j)}(x)|.
\]
Equip \(W_+\oplus W_-\) with the maximum of all \(\sigma_{N,j}\), \(0\le j\le J_0\), on every original and extra Schwartz coordinate, and the absolute values of all endpoint coordinates. Call this seminorm \(w_{N,J_0}\), and restrict it to \(H\).

For \(t\ge1\), the original plus action has
\(\sigma_{N,j}(h(\cdot/t))\le t^{N-j}\sigma_{N,j}(h)\le t^N\sigma_{N,j}(h)\).
The original minus action has
\(\sigma_{N,j}(t h(t\cdot))\le t^{j+1}\sigma_{N,j}(h)\).
The endpoint actions are \(1,t,t,1\), with the same complete action on extra copies. Hence
\[
w_{N,J_0}(\rho(t)x)\le t^{K_+}w_{N,J_0}(x),
\qquad K_+=\max(N,J_0+1).
\tag{ATG7.1}
\]
For \(0<t\le1\) the analogous explicit bound is
\[
w_{N,J_0}(\rho(t)x)\le t^{-K_-}w_{N,J_0}(x),
\qquad K_-=\max(J_0,N-1,0).
\tag{ATG7.2}
\]
The plus derivative factor is at most \(t^{-J_0}\), the minus factor at most \(t^{1-N}\), and the endpoint maximum is one, proving ATG7.2.

Give each ordered summand of ATG1.3 the projective tensor seminorm formed from these original \(H\) seminorms and the separating quotient norm \(\nu\) on \(Q\). The full degree-\(j\) action then satisfies
\[
\boxed{\|\rho_k(t)X\|_{N,J_0;j}
 \le t^{(k-j)K_++j}\|X\|_{N,J_0;j}\qquad(t\ge1).}
\tag{ATG7.3}
\]
Use the sum of the seminorms over the \(\binom{k}{j}\) ordered summands. The estimate on each follows from ATG6.4 and ATG7.1; summing gives the same factor. It retains all endpoint and extra factors. These are seminorms on the explicitly identified algebraic tensor cohomology spaces; no unproved identification with a completed derived tensor topology is used.

The cone restrictions and support maps in ATG2 contain only the original \(r_\pm\), inclusions, tensor differentials and the displayed signs. Their continuity constants may depend on \(k\) and the specified seminorms, but are independent of the repetition of a fixed prime action. Thus the diagonal return does not convert the factor \(t^k\) on \(Q^{\otimes k}\) into \(t^{k/2+c}\) by shifting a cohomological degree.

## ATG8. Actual finite traces and the precise amplification comparison

Let \(\mathscr S\) be any finite set of actual nontrivial zeros, with their original multiplicities, and let
\[
V_{\mathscr S}=\bigoplus_{\rho\in\mathscr S}Q_\rho,\qquad
d_{\mathscr S}=\sum_{\rho\in\mathscr S}m_\rho.
\]
These are actual finite invariant subspaces of \(Q\) by the prior full projectors. Restricting the separating norm in ATG6 to them and to their tensors gives
\[
\left|\operatorname{Tr}\bigl((T_p^{\otimes k})^\ell
 \mid V_{\mathscr S}^{\otimes k}\bigr)\right|
 \le d_{\mathscr S}^{\,k}p^{k\ell},
\qquad p\text{ prime},\ \ell,k\ge1 .
\tag{ATG8.1}
\]
Indeed every eigenvalue of a finite-dimensional operator is bounded in modulus by its operator norm, and its trace is the sum of \(d_{\mathscr S}^k\) eigenvalues with algebraic multiplicity. ATG6.4 bounds that operator norm by \(p^{k\ell}\). This derives the estimate from the actual full quotient topology, not only from a list of finite characters.

For a retained ordered tuple \((\rho_1,\ldots,\rho_k)\), the full operator is
\[
p^{\rho_1+\cdots+\rho_k}
 \prod_{\nu=1}^k\sum_{j=0}^{m_{\rho_\nu}-1}
 \frac{(\log p)^j}{j!}N_\nu^j.
\tag{ATG8.2}
\]
The total nilpotent order is
\(1+\sum_\nu(m_{\rho_\nu}-1)\): the highest surviving power has coefficient
\[
\frac{(\sum_\nu(m_{\rho_\nu}-1))!}
 {\prod_\nu(m_{\rho_\nu}-1)!}
 \prod_\nu N_\nu^{m_{\rho_\nu}-1}\ne0.
\]
Thus every nilpotent and mixed sector is retained. Triangularity proves
\[
\operatorname{Tr}\bigl((T_p^{\otimes k})^\ell
 \mid V_{\mathscr S}^{\otimes k}\bigr)
 =\left(\sum_{\rho\in\mathscr S}m_\rho p^{\ell\rho}\right)^k.
\tag{ATG8.3}
\]

The exact finite exponential rate is the earlier QS7 result:
\[
\limsup_{\ell\to\infty}
 \frac{\log|\operatorname{Tr}((T_p^{\otimes k})^\ell)|}{\ell\log p}
 =k\max_{\rho\in\mathscr S}\Re\rho.
\tag{ATG8.4}
\]
One can verify it without excluding cancellations at individual \(\ell\): the generating function of the traces of a finite matrix is
\(\sum_\lambda d_\lambda/(1-\lambda z)\), with strictly positive algebraic multiplicities. Distinct poles cannot cancel, so its convergence radius is the reciprocal of the maximal eigenvalue modulus. The tensor eigenvalues are those in ATG8.2. This gives ATG8.4.

For a reflection-stable actual finite set, put
\(B=\max_{\rho\in\mathscr S}\Re\rho\ge1/2\).
The supplied bound ATG8.1 has exponent \(k\), hence error \(k/2\) relative to the hoped-for \(k/2\) exponent. The exact measured error is
\[
k(B-1/2).
\tag{ATG8.5}
\]
There is no fixed error furnished by ATG6.4, ATG7.3 or the diagonal trace identity.

The comparison with Deligne is numerical and exact: a separately proved bound with exponent \(k/2+c\), with \(c\) independent of \(k\), would compare with ATG8.4 as \(k(B-1/2)\le c\). Factors depending on \(k\), and polynomial factors in \(\ell\), disappear on taking the \(\ell\)-th root for fixed \(k\); a linear-in-\(k\) exponential error does not. This identifies the effect of estimate shapes, not a new assumed theorem completing the programme. The actual estimate proved here is ATG8.1.

In the already read Deligne proof, D6.8 produces the doubled-input bound with one copy of the preceding error, using the pencil and its actual vanishing-cycle/weight calculation. D6.11 then halves that error. Directly tensoring an old estimate would have two copies and yield no improvement. The entire returned geometry above has now been calculated, but its demonstrated seminorm bounds are of the latter, additive-exponent type.

## ATG9. Whole-spectrum trace domain and its exact regularized estimates

An ordinary trace of \(T_p^{\otimes k}\) on the entire infinite \(Q^{\otimes k}\) has not been defined by the finite traces. In fact, for every \(k\ge2\), this tensor has an infinite-dimensional eigenspace. Choose infinitely many distinct actual zeros \(\rho\), take nonzero top eigenvectors in \(Q_\rho\) and \(Q_{1-\rho}\), and for \(k>2\) append fixed top eigenvectors at fixed zeros. Their eigenvalue is
\[
p^{\,1+\rho_3+\cdots+\rho_k},
\]
independent of the varying reflected pair. The tensors are linearly independent: a finite relation is separated by the actual first-factor primary projectors. Infinitely many actual zeros and those projectors are established in the retained original-zeta sources.

Thus a scalar test depending only on the sum of the generators, with nonzero value at that eigenvalue parameter, still has infinite multiplicity there. It does not give an absolutely summable whole-spectrum trace. This calculation identifies the exact trace-domain issue; it does not discard the whole tensor object.

There is an explicit whole-spectrum trace with the original separate Mellin tests. Let each \(\Phi_\nu\) be in the actual entire Schwartz Mellin space, and choose an integer \(M\ge2\). The original zero-count bound gives
\[
C_M=\sum_{\rho}m_\rho(1+|\Im\rho|)^{-M}<\infty.
\]
To check convergence, divide zero heights into dyadic intervals and use
\(N(T)=O(T\log(eT))\); the resulting majorant is a constant multiple of
\(\sum_{j\ge0}(j+1)2^{-j(M-1)}\), plus the finite low-height contribution.

Define with every original zero and multiplicity
\[
\Theta_{k,\boldsymbol\Phi}(t)=
\sum_{\rho_1,\ldots,\rho_k}
 \prod_{\nu=1}^k
 \bigl(m_{\rho_\nu}\Phi_\nu(\rho_\nu)t^{\rho_\nu}\bigr).
\tag{ATG9.1}
\]
For \(t\ge1\), this is absolutely convergent and
\[
\boxed{|\Theta_{k,\boldsymbol\Phi}(t)|
 \le t^k C_M^k
 \prod_{\nu=1}^k b_{1,M}(\Phi_\nu).}
\tag{ATG9.2}
\]
Here \(0<\Re\rho<1\) and the defining Mellin bound give the majorant term by term; the product of the \(k\) absolutely convergent sums proves the formula. It equals the product of the \(k\) original one-factor smoothed spectral traces. Thus a valid whole-spectrum estimate is available, with all coordinates observed separately, and its exponent is again \(k\). Neither its test domain nor its estimate has been replaced by a formal trace on an unrestricted tensor spectrum.

## ATG10. Full arithmetic return, labels and the exact result

For these \(k\)-fold receiving maps retain the full source correspondence
\[
\mathcal Z_k=
\{(x_1,\ldots,x_k,z)\in X^k\times X:
 f(z)=q_k(fx_1,\ldots,fx_k)\}.
\]
Its two exceptional fibres are the singleton all-plus and all-minus source corners; every other fibre over \(X^k\) is the complete \(U=\operatorname{Spec}\mathbb Z\). Put
\(a_k:\mathcal Z_k\to X^k\), \(b_k:\mathcal Z_k\to X\),
\(v_k=q_k f^k\), \(g_k=fb_k=v_ka_k\). The proof of FSC6 applies with all \(k+1\) coordinates retained: every nonempty relative open contains the original generic tuple; inverse images of the three receiving injectives are the generic-point constant sheaf and the two exceptional point skyscrapers. Their direct images under \(a_k\) are the corresponding injectives on \(X^k\). The same finite functorial resolution proves
\[
v_k^{-1}\mathcal G\xrightarrow{\ \simeq\ }
Ra_{k*}g_k^{-1}\mathcal G
\tag{ATG10.1}
\]
for every bounded receiving sheaf complex. Its section \(y\mapsto(i(y),\ldots,i(y))\) gives the same left inverse on receiving morphisms as FEM2. All action comparisons are termwise identities; no arithmetic prime is lost.

All support labels remain ordered \(k\)-tuples, or ordered \(2k\)-tuples for the two-input tensor pairing. Every differential and every amplitude-zero outcome preserves those labels. The ordinary geometric diagonal does not identify the labels of independent coefficient inputs. No label is silently identified with primitive \(\tau\).

The full product and its derived diagonal return have now been calculated, including every \(H/Q\) degree, the target trace, its action and all quantitative seminorm factors. The actual separating quotient norm gives \(t^k\), the actual top residue form has target character \(t^k\), and the valid whole-spectrum separately tested trace obeys the same exponent bound. None of these statements removes the exponent error by tensor amplification. They specify exactly what the proved geometry and topology supply, while leaving the original character operators and full programme objects unchanged for the further weight calculation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
