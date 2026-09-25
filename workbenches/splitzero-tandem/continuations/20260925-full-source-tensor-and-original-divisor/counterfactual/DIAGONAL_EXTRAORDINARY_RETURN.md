# The extraordinary diagonal return of the original residue pairing

25 September 2026. Independent derivation DER0–DER11. The calculation began late on 24 September and was completed on 25 September.

## DER0. The retained objects and the next actual operation

The original Connes–Consani finite topology is
\[
Y=\{c_+,c_-,\eta\},\qquad U_\pm=\{c_\pm,\eta\},\qquad U_\eta=\{\eta\}.
\]
Its opens are exactly \(\varnothing,U_\eta,U_+,U_-,Y\). We retain the full original coefficient sheaf
\[
F=(W_+\xrightarrow{r_+}A\xleftarrow{r_-}W_-),\qquad
W_\pm=(S\oplus\mathbb C^2)\oplus V_\pm^{\rm extra},
\]
with \(r_+=\Sigma\), \(r_-=R\Sigma\) on \(S\), and zero restriction on every endpoint and extra closed summand. Here
\[
\Sigma h(u)=2\sum_{n\geq1}h(nu),\qquad Rb(u)=u^{-1}b(u^{-1}),
\]
\(S\) is the actual even Schwartz space with \(h(0)=\int_{\mathbb R}h=0\), and \(A\) is the retained strong positive-real Schwartz space. The exact common closed image is \(J\subset A\), and \(Q=A/J\). Write
\[
P=W_+\oplus W_-,\qquad d=r_+-r_-,\qquad
H=\ker(d:P\to A).
\]
No endpoint or extra closed coefficient is removed.

The earlier complete calculations used here are [FTD0–FTD10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/FINITE_TOPOLOGY_DUALIZING_COMPLEX.md), [RPD0–RPD10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/RESIDUE_PRODUCT_DIAGONAL_INDEPENDENT.md), and the independently checked [PRS0–PRS9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/ORIGINAL_RESIDUE_PRODUCT_SHEAF_PAIRING.md). The current corpus and operation rules (private construction record; not distributed), the full corrected \(Z_0,Z_1/\tau,Z_2\) definitions, and the whole-spectrum arguments named there remain controlling. All operations below are on the constructed receiving sheaves. No addition, count, parity or numerical weight is assigned to primitive \(\tau\).

The geometric human source is Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The source comparison and its full arithmetic fibre are proved in [DCP](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SOURCE_CC_DOUBLE_PULLBACK.md), and the complete coefficient gluing is in [CGS](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SOURCE_COEFFICIENT_GLUE.md). The comparison sought with extraordinary inverse images in Pierre Deligne's [*La conjecture de Weil. II*](https://www.numdam.org/item/PMIHES_1980__52__137_0/) does not make the present diagonal a closed immersion. Its actual topology and the adjunction are calculated below.

Let \(k=\mathbb C\), let \(\chi_{\rm dil}(a)=a\), and let
\[
E=F\boxtimes F,\qquad K=j_{(\eta,\eta)!}\chi_{\rm dil}k
\]
on \(Y^2\). All tensor products are algebraic over \(k\) unless a topology is explicitly stated. The already proved sheaf map \(\beta:E\to K\) has zero components away from \((\eta,\eta)\), and at that point is the original contour
\[
B_A(a,b)=\frac1{2\pi i}
 \left(\int_{\Re s=2}^{\uparrow}-\int_{\Re s=-1}^{\uparrow}\right)
 \frac{M_0a(s)M_0b(1-s)}{\zeta(s)}\,ds,\qquad
M_0a(s)=\int_0^\infty a(u)u^s\frac{du}{u}.
\tag{DER0.1}
\]
The full original function \(\zeta\) remains the denominator. RPD1 and GZR retain the full functional-equation factor
\(\pi^{s-1/2}\Gamma((1-s)/2)/\Gamma(s/2)\), the values at zero and one, every trivial-zero residue, and every nontrivial-zero multiplicity. Those formulas are not replaced here. In particular \(B_A(J,A)=B_A(A,J)=0\), and
\(B_A(T_aa,T_ab)=aB_A(a,b)\).

RPD proved that ordinary diagonal pullback changes the target's nonzero global degree from two to one. Following the amended forward instruction, the next operation is the actual derived right adjoint of this diagonal's direct image. The construction is explicit, including its stalks, restrictions, counit, and the return of the entire coefficient sheaf.

## DER1. An exact second map on the nine-point topology

Write \(+\), \(-\) for \(c_+\), \(c_-\) inside pairs. Define
\[
q:Y^2\longrightarrow Y,\qquad
q(+,+)=c_+,\quad q(-,-)=c_-,\quad
q(x,y)=\eta\ \text{at the other seven points}.
\tag{DER1.1}
\]
Set
\[
O_+=Y^2\setminus\{(-,-)\},\qquad
O_-=Y^2\setminus\{(+,+)\},\qquad
O_\eta=Y^2\setminus\{(+,+),(-,-)\}.
\tag{DER1.2}
\]
Then \(q^{-1}U_x=O_x\). All three are open: \(O_+\) is the union of the minimal rectangles with corners \(++,+-,-+\), \(O_-\) the union for \(+-,-+,--\), and \(O_\eta\) the union for \(+-,-+\). Therefore \(q\) is continuous.

The actual diagonal \(\Delta(y)=(y,y)\) is continuous, since the inverse image of \(U_x\times U_y\) is \(U_x\cap U_y\), and \(q\Delta=\operatorname{id}_Y\). It is not closed: it contains \((\eta,\eta)\), whose closure is all nine points, but contains only three points. It is not open: the minimal neighbourhood of \((c_+,c_+)\) contains \((c_+,\eta)\). These assertions use every point of the original topology.

For any sheaf \(G\) on \(Y\), direct-image stalks have the exact form
\[
(\Delta_*G)_{(x,y)}
=\Gamma(U_x\cap U_y,G)
=\begin{cases}
G_+,&(x,y)=(+,+),\\
G_-,&(x,y)=(-,-),\\
G_\eta,&\text{otherwise}.
\end{cases}
\tag{DER1.3}
\]
The intersections are minimal opens, so the last equalities are evaluations, not limits requiring an acyclicity assumption. All restriction maps are the restrictions in \(G\) prescribed by \(q\). Hence there is a natural, stalkwise identity
\[
\boxed{\Delta_*=q^{-1}.}
\tag{DER1.4}
\]
In particular \(\Delta_*\) is exact. This equality constructs a map between the actual functors; it is not an identification of the nine product points.

## DER2. The adjunction and its full stalk formula

Since \(q^{-1}\) is exact and left adjoint to \(q_*\), the right derived functor \(Rq_*\) is right adjoint to \(q^{-1}\) on bounded derived categories. Here this statement can be verified on injective resolutions: \(q_*\) preserves injectives because its left adjoint is exact, and
\[
\operatorname{Hom}_{Y^2}(q^{-1}G,I^\bullet)
=\operatorname{Hom}_Y(G,q_*I^\bullet)
\]
is an equality of cochain complexes for every bounded-below injective resolution \(I^\bullet\). Together with DER1.4 this constructs
\[
\boxed{R\Delta^!=Rq_*.}
\tag{DER2.1}
\]
The notation on the left means the derived right adjoint to the actual \(\Delta_*\); no closed-immersion formula is invoked.

Let \(P_x=j_{U_x!}k\). As proved in FTD1,
\(\operatorname{Hom}(P_x,G)=G_x\), so the \(P_x\) are projective. Moreover
\[
\Delta_*P_x=q^{-1}P_x=j_{O_x!}k.
\]
The latter equality follows on all stalks: they are \(k\) exactly on \(O_x\), with identity restrictions there and zero elsewhere. Thus
\[
(R\Delta^!K)_x
=R\operatorname{Hom}_{Y^2}(\Delta_*P_x,K)
=R\Gamma(O_x,K).
\tag{DER2.2}
\]
The last equality follows from the exact open-extension adjunction, or by applying \(\operatorname{Hom}(j_{O_x!}k,-)\) to an injective resolution. The restrictions in DER2.2 are restriction from \(O_\pm\) to \(O_\eta\).

For every bounded sheaf complex \(G\) on \(Y^2\), not just \(K\), the same injective computation gives
\[
\boxed{R\Gamma(Y,Rq_*G)=R\Gamma(Y^2,G).}
\tag{DER2.3}
\]
Indeed \(\Gamma(Y,q_*I)=\Gamma(Y^2,I)\) term by term, and \(q_*I\) is injective. Thus the derived return retains the whole global complex.

## DER3. Direct local cohomology, with its restrictions

Label the four rectangles
\[
A_0=U_+\times U_+,\quad B_0=U_+\times U_-,
\quad C_0=U_-\times U_+,\quad D_0=U_-\times U_-.
\]
For this section use the usual ordered Čech differential
\((\delta z)_{ij}=z_j|_{ij}-z_i|_{ij}\) and
\((\delta w)_{ijk}=w_{jk}-w_{ik}+w_{ij}\).
The comparison with the original two-factor orientation is fixed by the injective and counit calculation in DER4–DER6.

For \(O_\eta=B_0\cup C_0\), the two sections of \(K\) are zero and the overlap is \(\{(\eta,\eta)\}\). Therefore its complex is
\[
[\,0\longrightarrow\chi_{\rm dil}k\,]\quad(\deg=0,1).
\tag{DER3.1}
\]
For \(O_+=A_0\cup B_0\cup C_0\), the only nonzero pair-intersection section is the \(B_0C_0\) section \(k\). The triple-intersection section is \(k\), with coefficient \(+1\) in \(\delta\). Thus its complex is
\[
[\,0\longrightarrow\chi_{\rm dil}k
 \xrightarrow{+1}\chi_{\rm dil}k\,]\quad(\deg=0,1,2).
\tag{DER3.2}
\]
For \(O_-=B_0\cup C_0\cup D_0\), the only nonzero pair-intersection section is again \(B_0C_0\), and its coefficient in the triple is again \(+1\). Its complex is DER3.2. Restriction to \(O_\eta\) is identity on the \(B_0C_0\) coordinate in degree one and zero in degree two.

These complexes compute derived sections. Every nonempty intersection is a minimal open rectangle and therefore has exact section evaluation. For its inclusion \(j\), every intersection with another minimal product open is minimal or empty, so every stalk of \(j_*\) is an exact evaluation or zero. This particular \(j_*\) is exact and preserves injectives, hence its terms are globally acyclic. The augmented Čech resolution is stalkwise the augmented simplex resolution for the charts containing that stalk. Its contracting homotopy is insertion of any one containing chart, with the alternating sign of its position. This proves exactness and the stated computation.

It follows, including all restrictions, that
\[
R^i q_*K=0\quad(i\ne1),\qquad
R^1q_*K=j_{\eta!}\chi_{\rm dil}k.
\tag{DER3.3}
\]
The next section retains an actual injective complex and the orientation, rather than replacing it by its cohomology alone.

## DER4. The full injective complex and an explicit contraction

Use the injectives of FTD1:
\[
I_\eta=(k,k,k;\operatorname{id},\operatorname{id}),\quad
I_+=(k,0,0),\quad I_-=(0,k,0).
\]
The sheaf \(P_\eta=j_{\eta!}k\) has the injective resolution
\[
0\to P_\eta\to I_\eta
 \xrightarrow{(\mathrm{ev}_+,-\mathrm{ev}_-)}I_+\oplus I_-\to0.
\tag{DER4.1}
\]
It is exact at the generic stalk and at both closed stalks. Its external tensor square is an injective resolution of the untwisted part of \(K\): exactness follows stalkwise from exactness of tensor product over \(k\), and \(I_x\boxtimes I_y\) is the evaluation-right-adjoint injective at \((x,y)\).

Order its degree-one summands by
\[
(I_{+\eta},I_{-\eta},I_{\eta+},I_{\eta-}),
\]
with coordinates \((a_+,a_-,b_+,b_-)\), and degree-two summands by
\((I_{++},I_{+-},I_{-+},I_{--})\). The differentials are
\[
d^0z=(z,-z,z,-z),
\]
\[
d^1(a_+,a_-,b_+,b_-)
=(-a_++b_+,\ a_++b_-,\ -a_--b_+,\ a_--b_-).
\tag{DER4.2}
\]
At a stalk where a displayed target summand vanishes, its coordinate is zero. In every other term the formula includes the corresponding restriction. These signs are those of
\(d(x\otimes y)=dx\otimes y+(-1)^{\deg x}x\otimes dy\).

Applying \(q_*\) gives a complex \(T^\bullet\) of injectives on \(Y\):
\[
T^0=I_\eta,\qquad T^1=I_\eta^4,\qquad
T^2=I_+\oplus I_\eta\oplus I_\eta\oplus I_-,
\tag{DER4.3}
\]
with exactly DER4.2. To verify the terms, sections of \(I_{xy}\) on \(O_z\) equal \(k\) if \((x,y)\in O_z\), and zero otherwise. Hence \(q_*I_{++}=I_+\), \(q_*I_{--}=I_-\), and the other seven evaluation injectives map to \(I_\eta\).

At \(\eta\), degree two retains only the mixed coordinates \(+-,-+\). At \(c_+\), it retains \(++,+-,-+\); at \(c_-\), it retains \(+-,-+,--\). Every closed-to-generic restriction is identity on the degree-zero and degree-one terms and discards only that closed corner in degree two. This specifies every stalk and every restriction.

Define
\[
T_{\rm small}
=[\,I_\eta\xrightarrow{(-\mathrm{ev}_+,+\mathrm{ev}_-)}
      I_+\oplus I_-\,]\quad(\deg=1,2).
\tag{DER4.4}
\]
There is an inclusion \(\iota:T_{\rm small}\to T\),
\[
\iota^1(a)=(a,0,0,-a),\qquad
\iota^2(u_+,u_-)=(u_+,0,0,u_-),
\tag{DER4.5}
\]
and a retraction \(\pi:T\to T_{\rm small}\),
\[
\pi^0=0,\qquad
\pi^1(a_+,a_-,b_+,b_-)=a_++a_-,
\]
\[
\pi^2(z_{++},z_{+-},z_{-+},z_{--})
=(z_{++}+\mathrm{ev}_+z_{-+},
  \mathrm{ev}_-z_{+-}+z_{--}).
\tag{DER4.6}
\]
All restrictions in these formulas are the actual maps \(I_\eta\to I_\pm\). Substituting DER4.2 proves both cochain identities and \(\pi\iota=\operatorname{id}\).

The complete homotopy \(h:T\to T[-1]\) is
\[
h^1(a_+,a_-,b_+,b_-)=-a_-,\qquad
h^2(z_{++},z_{+-},z_{-+},z_{--})=(0,0,-z_{-+},z_{+-}),
\tag{DER4.7}
\]
with every other component zero. Here \(h^2\) uses only the two \(I_\eta\) coordinates, so it is a sheaf morphism. In degree zero \(h^1d^0=\operatorname{id}\). In degree one,
\[
(dh+hd)(a_+,a_-,b_+,b_-)
=(-a_-,\,a_-,\,b_+,\,b_-+a_++a_-),
\]
which is \(\operatorname{id}-\iota\pi\). In degree two,
\[
(dh+hd)z=(-\mathrm{ev}_+z_{-+},\,z_{+-},\,z_{-+},
          -\mathrm{ev}_-z_{+-}),
\]
again \(\operatorname{id}-\iota\pi\). This proves a strong deformation retract with all terms retained.

The small complex is the shift by \(-1\) of DER4.1's injective resolution. The shifted differential acquires the displayed minus sign. Its quasi-isomorphism
\[
j_{\eta!}\chi_{\rm dil}k[-1]\longrightarrow
R\Delta^!K
\tag{DER4.8}
\]
sends the generic generator to \((1,0,0,-1)\) in \(T^1_\eta\), and has zero closed components. It is a cocycle at \(\eta\); all closed stalks of \(T\) are acyclic. Thus
\[
\boxed{R\Delta^!K\simeq j_{\eta!}\chi_{\rm dil}k[-1].}
\tag{DER4.9}
\]
This calculation differs from the ordinary pullback
\(\Delta^{-1}K=j_{\eta!}\chi_{\rm dil}k\) by an actually derived degree.

FTD's full dualizing complex is
\(\omega_Y=[I_\eta\to I_+\oplus I_-]\), degrees \(-1,0\), differential \((+,-)\). The explicit isomorphism
\[
T_{\rm small}\longrightarrow\chi_{\rm dil}\omega_Y[-2]
\]
is minus identity in degree one and identity in degree two. It commutes with the two displayed differentials and preserves the global trace below. This records the orientation sign in the precise dualizing comparison.

## DER5. The counit, its trace, and every corner coefficient

The adjunction counit is
\[
\epsilon:\Delta_*R\Delta^!K=q^{-1}Rq_*K\longrightarrow K.
\tag{DER5.1}
\]
For the product injective resolution in DER4.2, the evaluation
\(q^{-1}q_*I\to I\) is restriction of a section on \(O_{q(x,y)}\) to the stalk \((x,y)\). It is identity for \(I_{++}\), \(I_{--}\), and is the ordinary restriction \(I_{\eta\eta}\to I_{xy}\) for the other injectives. Consequently DER5.1 is represented, from \(q^{-1}T_{\rm small}\) to that resolution, by
\[
\epsilon^1(a)=
(\mathrm{ev}_{+\eta}a,\ 0,\ 0,\ -\mathrm{ev}_{\eta-}a),
\qquad
\epsilon^2(u_+,u_-)=(u_+,0,0,u_-).
\tag{DER5.2}
\]
The source complex has degree-one \(I_{\eta\eta}\), degree-two \(I_{++}\oplus I_{--}\), and differential \((-\mathrm{ev}_{++},+\mathrm{ev}_{--})\). Applying the target differential to \(\epsilon^1\) gives \((-\mathrm{ev}_{++},0,0,+\mathrm{ev}_{--})\); the two mixed contributions cancel exactly. This proves the cochain condition.

Global sections of \(T_{\rm small}\) are
\[
[\,\chi_{\rm dil}k\xrightarrow{(-1,+1)}
 \chi_{\rm dil}k^2\,]\quad(\deg=1,2).
\]
The degree-two trace is
\[
[(u_+,u_-)]\longmapsto u_++u_-.
\tag{DER5.3}
\]
Its kernel is precisely the image of \((-1,+1)\), so it is an isomorphism on \(H^2\).

Global sections of the original product injective resolution have degree-two \(k^4\), and the image in that degree is the image of the full matrix DER4.2. Its annihilating functional is
\[
(z_{++},z_{+-},z_{-+},z_{--})
 \longmapsto z_{++}+z_{+-}+z_{-+}+z_{--}.
\tag{DER5.4}
\]
The matrix has rank three: its kernel in degree one is exactly the span of \((1,-1,1,-1)\), by solving all four displayed rows. Therefore the kernel of DER5.4 is exactly that image, and DER5.4 is the top trace.

These are the original ordered two-factor traces. In one factor DER4.1 gives cokernel of \((1,-1)\), traced by the sum. Given closed data \((u_+,u_-)\), its two local lifts into \(I_\eta\) are \(u_+\) and \(-u_-\); the original Čech differential \(r_+-r_-\) gives \(u_++u_-\). Taking the external tensor of these two one-factor resolutions uses DER4.2's Koszul sign, and the product of the two sum maps is exactly the sum of all four corners in DER5.4. Thus this is the original ordered product trace, with coefficient \(+1\).

The counit sends \((u_+,u_-)\) to \((u_+,0,0,u_-)\). Equations DER5.3–DER5.4 prove that its map on the actual global degree-two target is identity, without a factor two or a suppressed sign:
\[
R\Gamma(Y,R\Delta^!K)\simeq
R\Gamma(Y^2,K)=\chi_{\rm dil}k[-2].
\tag{DER5.5}
\]
The whole derived trace therefore survives extraordinary return.

## DER6. Why the canonical comparison with ordinary pullback is zero

Apply \(\Delta^{-1}\) to DER5.1. Since
\(\Delta^{-1}\Delta_*=\operatorname{id}\) on this embedding, this is the canonical map
\[
R\Delta^!K\longrightarrow\Delta^{-1}K.
\tag{DER6.1}
\]
Its target resolution, obtained by pulling back the product injective resolution, is
\[
I_\eta\longrightarrow
I_+\oplus I_-\oplus I_+\oplus I_-
\longrightarrow I_+\oplus I_-
\quad(\deg=0,1,2),
\]
\[
d^0z=(\mathrm{ev}_+z,-\mathrm{ev}_-z,
       \mathrm{ev}_+z,-\mathrm{ev}_-z),\qquad
d^1(a_+,a_-,b_+,b_-)=(-a_++b_+,a_--b_-).
\tag{DER6.2}
\]
The two mixed corner injectives pull back to zero. The map from \(T_{\rm small}\) is
\[
c^1(a)=(\mathrm{ev}_+a,0,0,-\mathrm{ev}_-a),\qquad
c^2(u_+,u_-)=(u_+,u_-).
\]
Define a homotopy, with its only nonzero component, by
\[
h^2(u_+,u_-)=(-u_+,0,0,-u_-)
\]
into degree one of DER6.2. Then \(d h=c^2\) in degree two and
\(h d=c^1\) in degree one, since \(d_{T_{\rm small}}=(-,+)\). Hence
\[
\boxed{c=dh+hd.}
\tag{DER6.3}
\]
Thus the canonical comparison is zero in the derived category. This is compatible with the nonzero counit trace before ordinary pullback; the actual homotopy identifies exactly where that pullback loses it. The extraordinary map has been constructed rather than inferred from the failure of ordinary pullback.

## DER7. Return of the complete original coefficient sheaf

The same \(Rq_*\) applies to \(E=F\boxtimes F\), including all \(W_\pm\) endpoint and extra summands. At \(O_\eta\) its complete Čech complex is
\[
W_+\otimes W_-\ \oplus\ W_-\otimes W_+
 \xrightarrow{d_\eta} A\otimes A
\quad(\deg=0,1),
\]
\[
d_\eta(b,c)=(r_-\otimes r_+)c-(r_+\otimes r_-)b.
\tag{DER7.1}
\]
Its image is exactly \(J\otimes J\), since each \(r_\pm\) is onto \(J\). Therefore
\[
(R^1q_*E)_\eta=Q_\Delta:=(A\otimes A)/(J\otimes J).
\tag{DER7.2}
\]

At \(O_+\), write the corner sections as
\[
a\in W_+\otimes W_+,\quad
b\in W_+\otimes W_-,\quad
c\in W_-\otimes W_+.
\]
The full degree-one group is
\((W_+\otimes A)\oplus(A\otimes W_+)\oplus(A\otimes A)\),
with coordinates \((u,v,w)\) on \(A_0B_0,A_0C_0,B_0C_0\). The degree-two group is \(A\otimes A\), and
\[
\begin{aligned}
d^0(a,b,c)=\bigl(&(\operatorname{id}\otimes r_-)b
                   -(\operatorname{id}\otimes r_+)a,\\
                &(r_-\otimes\operatorname{id})c
                   -(r_+\otimes\operatorname{id})a,\\
                &(r_-\otimes r_+)c-(r_+\otimes r_-)b\bigr),\\
d^1(u,v,w)={}&w-(\operatorname{id}\otimes r_+)v
                  +(r_+\otimes\operatorname{id})u.
\end{aligned}
\tag{DER7.3}
\]
Substitution gives \(d^1d^0=0\), with all four terms cancelling by the same two tensor restrictions.

At \(O_-\), use corners
\(b\in W_+\otimes W_-\), \(c\in W_-\otimes W_+\),
\(d_0\in W_-\otimes W_-\).
Order the degree-one coordinates as \(u\) on \(C_0D_0\),
\(v\) on \(B_0D_0\), \(w\) on \(B_0C_0\); they lie in
\((W_-\otimes A)\oplus(A\otimes W_-)\oplus(A\otimes A)\). The full formulas are
\[
\begin{aligned}
d^0(b,c,d_0)=\bigl(&(\operatorname{id}\otimes r_-)d_0
                     -(\operatorname{id}\otimes r_+)c,\\
                 &(r_-\otimes\operatorname{id})d_0
                     -(r_+\otimes\operatorname{id})b,\\
                 &(r_-\otimes r_+)c-(r_+\otimes r_-)b\bigr),\\
d^1(u,v,w)={}&w-(\operatorname{id}\otimes r_-)v
                  +(r_-\otimes\operatorname{id})u .
\end{aligned}
\tag{DER7.4}
\]
Again \(d^1d^0=0\) directly. These are the original three-chart resolutions; the reordered minus coordinates are explicitly stated.

In either closed complex \(d^1\) is onto, since the coefficient of \(w\) is identity. A degree-one cycle is exactly
\[
w=(\operatorname{id}\otimes r_\pm)v
 -(r_\pm\otimes\operatorname{id})u.
\tag{DER7.5}
\]
For the plus complex, the independent \(b\) and \(c\) images fill
\((W_+\otimes J)\oplus(J\otimes W_+)\) in \((u,v)\); the \(a\) contribution is already in that sum. For the minus complex, the independent \(c\) and \(b\) images fill
\((W_-\otimes J)\oplus(J\otimes W_-)\), and the \(d_0\) contribution lies there too. Tensor product over a field is exact, so taking the displayed quotients proves
\[
(R^1q_*E)_{c_\pm}
=(W_\pm\otimes Q)\oplus(Q\otimes W_\pm),\qquad
R^iq_*E=0\quad(i\geq2).
\tag{DER7.6}
\]
Restriction to \(O_\eta\) selects the \(B_0C_0\) coordinate \(w\). Consequently the exact closed-to-generic restrictions are
\[
\sigma_\pm(u,v)
=-(r_\pm\otimes\operatorname{id}_Q)u
 +(\operatorname{id}_Q\otimes r_\pm)v
 \quad\text{in }Q_\Delta .
\tag{DER7.7}
\]
To interpret a tensor in \(J\otimes Q\) or \(Q\otimes J\) in this expression, choose any lift of its \(Q\) coordinate to \(A\). A different lift changes the result by \(J\otimes J\), so the map is well defined. Formula DER7.5 proves that it is the actual restriction, including both signs.

The degree-zero direct image \(q_*E\) is the kernel of each full \(d^0\) above and of DER7.1. These formulas retain every degree-zero coefficient. In particular its plus stalk is the complete fibre product specified by the two equalities
\[
(\operatorname{id}\otimes r_+)a=(\operatorname{id}\otimes r_-)b,
\qquad
(r_+\otimes\operatorname{id})a=(r_-\otimes\operatorname{id})c.
\tag{DER7.8}
\]
They imply the third equality in DER7.3. The minus stalk has the corresponding two equalities in DER7.4. The maps to the generic stalk retain the two cross-corner sections \((b,c)\).

## DER8. The exact mixed image, its quotient, and all lower groups

Let \(G=R^1q_*E\). In the generic stalk define the canonical mixed subspace
\[
M=(J\otimes Q)\oplus(Q\otimes J)\subset Q_\Delta.
\]
As proved directly in RPD7, there is an exact sequence
\[
0\to M\longrightarrow Q_\Delta
 \xrightarrow{\vartheta}Q\otimes Q\to0,
\qquad \vartheta([a\otimes b])=[a]\otimes[b].
\tag{DER8.1}
\]
For completeness, its two injections are lift independent modulo \(J\otimes J\), and
\((J\otimes A)\cap(A\otimes J)=J\otimes J\). The latter follows by decomposing \(A=J\oplus A_0\) as vector spaces and retaining all four tensor summands. This proves injectivity, the direct sum, and exactness without choosing a section of the original quotient as an equivariant map.

Equation DER7.7 and surjectivity \(r_\pm:W_\pm\to J\) show that the image of each closed restriction is precisely \(M\). Define the actual subsheaf
\[
N=\bigl(G_{c_+}\xrightarrow{\sigma_+}M
             \xleftarrow{\sigma_-}G_{c_-}\bigr)\subset G.
\]
Then there is a canonical exact sheaf row
\[
\boxed{0\to N\to R^1q_*E\to j_{\eta!}(Q\otimes Q)\to0.}
\tag{DER8.2}
\]
It is identity on the retained closed stalks and is DER8.1 at the generic stalk. This row is a quotient of the actual returned coefficients.

The original ordered global complex of \(N\) is
\[
G_{c_+}\oplus G_{c_-}
 \xrightarrow{\sigma_+-\sigma_-}M.
\]
It is onto: either closed restriction is already onto \(M\). Its kernel is
\[
H^0(Y,N)=(H\otimes Q)\oplus(Q\otimes H).
\tag{DER8.3}
\]
Indeed the \(J\otimes Q\) equation is
\(-r_+u_++r_-u_-=0\), which is the tensor with \(Q\) of the original equation \(r_+w_+=r_-w_-\); exactness of tensor over \(k\) identifies its kernel with \(H\otimes Q\). The second equation is \(r_+v_+-r_-v_-=0\) in \(Q\otimes J\), giving \(Q\otimes H\). Thus \(H^1(Y,N)=0\).

The sheaf \(j_{\eta!}(Q\otimes Q)\) has zero global sections and original degree-one cohomology \(Q\otimes Q\), by the two-chart complex. The long exact sequence of DER8.2 therefore gives
\[
H^0(Y,R^1q_*E)=(H\otimes Q)\oplus(Q\otimes H),\qquad
H^1(Y,R^1q_*E)=Q\otimes Q .
\tag{DER8.4}
\]

The direct-image sheaf \(q_*E\) also has no \(H^1\). Here is an explicit proof of the necessary surjective restriction, preserving its full degree-zero domain. For a generic compatible pair \((b,c)\) in DER7.1, put
\[
U=(\operatorname{id}\otimes r_-)b\in W_+\otimes J,\quad
V=(r_-\otimes\operatorname{id})c\in J\otimes W_+,
\quad
j=(r_+\otimes\operatorname{id})U
   =(\operatorname{id}\otimes r_+)V .
\]
Choose a linear section \(s_+:J\to W_+\) of the already constructed surjection \(r_+\). Define
\[
a=(\operatorname{id}\otimes s_+)U
 +(s_+\otimes\operatorname{id})V
 -(s_+\otimes s_+)j.
\tag{DER8.5}
\]
Applying \(\operatorname{id}\otimes r_+\) gives \(U\), because the last two terms cancel; applying \(r_+\otimes\operatorname{id}\) gives \(V\), because the first and last terms cancel. Hence \((a,b,c)\) is an actual plus-stalk lift by DER7.8. The minus restriction has the identical construction with \(r_-,s_-\). A vector-space section suffices for this algebraic claim; no additional equivariant section is asserted. Both restrictions onto the generic stalk are consequently surjective, and the original two-chart complex proves \(H^1(Y,q_*E)=0\).

Global sections of \(q_*E\) equal global sections of \(E\), which are \(H\otimes H\) by the exact tensor complex in RPD3. Thus
\[
R\Gamma(Y,q_*E)\simeq(H\otimes H)[0].
\tag{DER8.6}
\]
All endpoint and extra closed coefficients remain inside \(H\) and every \(W_\pm\).

Finally \(Rq_*E\) has cohomology sheaves only in degrees zero and one by DER7.6. The canonical truncation triangle
\[
q_*E\to Rq_*E\to(R^1q_*E)[-1]\to(q_*E)[1]
\]
and the already proved vanishing of \(H^i(Y,-)\) for \(i\geq2\) give
\[
\begin{aligned}
H^0(Y^2,E)&=H\otimes H,\\
H^1(Y^2,E)&=(H\otimes Q)\oplus(Q\otimes H),\\
H^2(Y^2,E)&=Q\otimes Q.
\end{aligned}
\tag{DER8.7}
\]
This is the whole global product calculation returned through the actual adjunction. It preserves the lower groups, not only the top pairing.

## DER9. The returned residue morphism and its scalar kernel

Apply \(Rq_*\) to the original sheaf map \(\beta:E\to K\). In the local Čech complexes, its map is zero except on the \(A\otimes A\) intersection coordinates, where it is exactly DER0.1. In the plus complex it sends \((u,v,w)\) to \(B_A(w)\) in degree one and \(z\) to \(B_A(z)\) in degree two; the terms involving \(u,v\) in DER7.3 are killed because one input lies in \(J\). The minus complex has the same verification using DER7.4. On \(O_\eta\) its degree-one map is \(B_A\). Thus the entire returned cochain map is proved, including its closed acyclic target complexes.

On cohomology sheaves it is
\[
R^1q_*\beta:G\longrightarrow j_{\eta!}\chi_{\rm dil}k,
\]
zero at both closed points and at the generic point
\[
Q_\Delta\xrightarrow{\vartheta}Q\otimes Q
 \xrightarrow{\overline B_\zeta}\chi_{\rm dil}k.
\tag{DER9.1}
\]
Equations DER7.7 and \(B_A(J,A)=B_A(A,J)=0\) prove sheaf naturality. It factors through DER8.2. Its complete scalar kernel is the sheaf with closed stalks \(G_{c_\pm}\) and generic stalk
\(\vartheta^{-1}\ker\overline B_\zeta\); the exact row is
\[
0\to N\longrightarrow\ker(R^1q_*\beta)
 \longrightarrow j_{\eta!}\ker\overline B_\zeta\to0.
\tag{DER9.2}
\]
This explicitly retains the difference between the mixed kernel \(\ker\vartheta=M\) and the generally larger scalar kernel. Nondegeneracy in the two inputs does not assert injectivity of a single functional on \(Q\otimes Q\).

Taking \(H^1(Y,-)\) in DER9.1 and using the trace orientation of DER5 gives the original
\[
Q\otimes Q\xrightarrow{\overline B_\zeta}\chi_{\rm dil}k.
\tag{DER9.3}
\]
There is no sign or factor introduced by this return. One can check the identification of its source independently for every algebraic functional on \(Q\otimes Q\): each such functional, composed with \(A\otimes A\to Q\otimes Q\), gives the same stalkwise product construction; DER5's corner calculation preserves its exact scalar. These functionals distinguish all vectors of \(Q\otimes Q\), so the source edge identification is the displayed identity, not merely an identification detected by one non-injective scalar pairing.

Consequently currying the returned global map yields exactly the already constructed
\[
\Psi:D=[P\xrightarrow d A]\longrightarrow
 \chi_{\rm dil}D_c'[-2],\qquad
\Psi^0=0,\quad \Psi^1=\pi_Q'D_\zeta\pi_Q,
\tag{DER9.4}
\]
where \(\pi_Q:A\to Q\). The continuous dual and all its endpoint and extra terms are those retained in FTD and PRS. The strong-dual continuity is the original contour bound applied to bounded sets; the finite sheaf return has introduced no new analytical completion.

## DER10. Actions, topology and the exact relation to weight control

Every injective matrix, contraction, restriction and counit above is tensored with the same character line \(\chi_{\rm dil}\). The entries are \(0,+1,-1\) and restrictions. Thus all maps commute with the full real action \(a>0\) and every original prime specialization \(a=p\). On the returned input sheaf, the actions are the original tensor actions on every \(W_\pm\), \(A\), \(J\), and \(Q\); their restrictions intertwine by the original construction of \(r_\pm\). No scalar action has been replaced by a prime dilation.

The source receiver's integer action is still \([n]=(n,0,0)\) in the faithful ring \(\mathbb Z^3\), and \([\tau]=(1,1,1)\). The two independent tensor-factor scalar actions remain independent; simultaneous integer inputs multiply the scalar pairing by \(n^2\), whereas simultaneous spectral dilation multiplies it by \(a\). The original closed extra copies therefore remain necessary and are retained in DER7–DER9.

The finite target complexes and all their maps are finite-dimensional continuous maps. For the analytic source, \(B_A\) is jointly continuous with the original GZR seminorm bound and extends to the projective completed tensor. Algebraic tensor cohomology in DER7–DER9 has not been silently replaced by completed tensor cohomology. The derived adjunction proved here is in the stated algebraic sheaf category; its specified finite matrices and analytic pairing are also continuous on their specified spaces. This proves the applicable continuous maps without asserting injectivity of arbitrary topological vector spaces.

For the full lattice receiver, each linear map has its degreewise support-preserving lift \((v,\lambda)\mapsto(fv,\lambda)\). Tensor inputs retain their ordered pair \((\lambda,\mu)\). The geometrical diagonal does not authorize identifying those two independent labels. A zero amplitude from any differential or residue keeps its complete original label. The map \(f:X^{\rm dbl}\to Y\) and its arithmetic fibre remain those of DCP; applying inverse image along \(f\) or \(f\times f\) returns the displayed coefficient maps on that full source without merging its primes.

The exact new conclusion is that extraordinary return repairs the degree loss of ordinary pullback and gives the entire product trace and coefficient quotient. Its weight content is still calculable from the original action:
\[
T_p|_{Q_\rho}
=p^\rho\sum_{j=0}^{m_\rho-1}\frac{(\log p)^j}{j!}N_\rho^j,\qquad
B_\zeta(N_\rho x,y)=-B_\zeta(x,N_{1-\rho}y).
\]
The reflected block has character \(p^{1-\rho}\), with its full nilpotent, and simultaneous pairing gives \(p\). Thus the numerical weights of the two paired characters are
\(2\Re\rho\) and \(2(1-\Re\rho)\), whose sum is two. All finite matrices in DER4 and DER5 act on the topological factors while retaining those coefficient actions, so this derived return neither changes those exponents nor turns a bilinear pairing into a Hermitian one. It does not prove either individual weight to be one.

## DER11. Exact consequence for the ongoing comparison

The previously constructed product morphism now has a complete extraordinary return:
\[
Rq_*(F\boxtimes F)\longrightarrow
R\Delta^!j_{(\eta,\eta)!}\chi_{\rm dil}k
 \simeq j_{\eta!}\chi_{\rm dil}k[-1],
\]
whose global target is \(\chi_{\rm dil}k[-2]\), whose counit preserves the original trace with coefficient \(+1\), and whose degree-one coefficient map is DER9.1. Its closed restriction images are exactly the mixed tensor subspace \(M\), and the actual quotient is \(Q\otimes Q\). The full scalar kernel is DER9.2.

This is an explicit advance from ordinary diagonal pullback: the correct right adjoint retains the missing degree and produces the precise quotient maps. It is not a same-site degree-zero map from \(F\) to that target. Indeed the target has cohomology only in degree one, so such a morphism from a sheaf concentrated in degree zero is zero; the actual source \(Rq_*(F\boxtimes F)\) has the calculated degree-one sheaf \(G\), which supplies the nonzero morphism.

All original zeros, multiplicities, primary nilpotents, endpoint coefficients, extra faithful-source copies, original-zeta factors and source support labels stay in the calculation. The derived return establishes this concrete geometric origin of the pairing. Further weight control has to use its now explicit coefficient maps together with the retained programme results; no unproved Deligne transfer or RH conclusion is inserted.

### Full arithmetic correspondence and its derived coefficient return

DERIVED_RETURN_FULL_SOURCE_CORRESPONDENCE.md, FSC0–FSC6, returns the receiving construction to the entire original arithmetic source. FSC2 rules out precisely a continuous single-valued lift of q that fixes the complete arithmetic diagonal. FSC3 immediately constructs the full alternative Z={(x,y,z):fz=q(fx,fy)}, with projections a,b and lifted diagonal x↦(x,x,x). Each nonexceptional a-fibre is the whole Spec Z; the two equal closed-corner fibres are singletons.

FSC6 proves the actual canonical derived comparison Ra_*b^{-1}f^{-1}G ≅ (f×f)^{-1}Delta_*G for bounded complexes of algebraic sheaves of complex vector spaces on Y. It computes the inverse images of all three receiving injectives, their exact direct images, and a functorial injective resolution; no general proper-base-change theorem is assumed. The comparison applies to the full derived input and trace target from DER and to their morphism. Every arithmetic point remains in the correspondence. The coefficient comparison does not assign a numerical weight to primitive Z_1/tau or settle the active numerical weight-separation target.

### The degree-one mixed obstruction has an explicit global equivariant contraction

GLOBAL_MIXED_RETURN_CONTRACTION.md, GMC0–GMC7, follows the generic mixed row into its complete global sheaf complex. The actual section s_+(j)=(Sigma^{-1}j,0,0) is continuous and dilation equivariant, using the already proved summation inverse. It gives S(m_1,m_2)=(-(s_+ tensor1)m_1,(1 tensor s_+)m_2,0,0), with d_M S=id. The exact global cochain map is (id-Sd_M,vartheta), onto K_0 in degree0 and Q tensor Q in degree1, with zero differential. Its entire kernel is [S(M)→iota(M)], contracted by h(iota m)=Sm. Every original prime action intertwines.

Thus the degree-one mixed obstruction is killed by the constructed contraction of ker(F)=[S(M)→iota(M)]. The full mixed subsheaf retains RΓ(Y,N)≃K_0[0], with K_0=(H tensor Q) direct-sum (Q tensor H); it is not asserted to be acyclic. The generic polynomial representative P(L_total)z=iota m becomes the exact global boundary d(Sm). All original endpoint and extra copies remain in K_0=(H tensor Q) direct-sum (Q tensor H); the original residue trace factors through the computed map with coefficient +1. This is a theorem in the specified algebraic tensor/sheaf calculation, with no assumption of completed-tensor cohomology, mirror equivariance of the plus-only section, or numerical purity. The remaining Q operators and all primary nilpotents are retained explicitly in GMC6.3.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
