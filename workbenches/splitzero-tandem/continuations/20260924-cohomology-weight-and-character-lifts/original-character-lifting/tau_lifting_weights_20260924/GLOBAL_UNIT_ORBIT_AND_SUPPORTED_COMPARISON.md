# The global unit orbit, its companion mirror and its exact supported placement

24 September 2026. Independent derivation UOS0–UOS9. This computes the actual prime and companion-mirror action on the global multiplier functionals, maps them through the original supported localization row, and constructs the full comparison with the dual-supported complex. It does not identify the relative residue-comparison cokernel with an RH counterexample space.

## UOS0. Source, retained constructions and operation scope

The source remains the user's \(Z_0\) absence, primitive \(Z_1/\tau\) without parity or source addition, and the original integer layer with its \(Z_2\) data and complete amounts. B1–B5/P1–P5 and the retraction of source \(\tau\) addition are retained in [SOURCE_OPERATIONS_AND_PROOFS.md](../foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md). The complete user corpus and its global arguments are recorded in CORPUS_AND_OPERATION_RULES.md (private construction record; not included), particularly USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, USR-6152e3bc6302258c and USR-4322be19bff532cd. The receiving comparisons below come after the already reconstructed arithmetic and original zeta, as those arguments require.

The arithmetic constant \(1\) in the multiplier algebra is not primitive \(\tau\). Every sum, scalar, transpose, cone, and quotient below is an operation in the already constructed coefficient category. No such operation has primitive \(\tau\) as an additive or numerical operand.

The original coefficient geometry and Fourier localization are due to Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), with their author-source definitions and reading coverage retained in DCP0. The analytic closed-image framework is due to Ralf Meyer, [*A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3), with the original-space image and inverse proofs in OMS. The lifting argument being compared is Pierre Deligne's [*La conjecture de Weil. II*, §§3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/); its geometric duality and weight bounds are not assumed for this receiver.

The complete inputs are:
- [DCP7–DCP12](SOURCE_CC_DOUBLE_PULLBACK.md), the actual source-supported coefficient maps and faithful extra closed copies;
- [ASD3–ASD14](ACTUAL_SUPPORTED_DUALITY_INDEPENDENT.md), their full continuous dual, all signs, and the residue-comparison cone;
- [GZR7–GZR9](GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md), the companion denominator, real action and support lifts of the full residue pairing;
- [PGD0–PGD7](GLOBAL_POLYNOMIAL_DUAL_DEFECT.md), the complete multiplier map and explicit nonzero class, independently checked in PGC;
- [SCL1, SCL6–SCL9](SPECTRAL_COKERNEL_DIVISIBILITY_AND_FINITE_LIFTING.md), actual original jet representatives, finite lifts and the exact cokernel action.

Those proof files retain their full source provenance. No completeness or finite-dimensionality of the whole spectral quotient is introduced.

## UOS1. The original spaces, multiplier functionals and their exact actions

Here \(S=S_{00}^{\mathrm{even}}\) is the complex Schwartz space of even functions \(h\) on \(\mathbb R\) satisfying \(h(0)=0\) and \(\int_{\mathbb R}h(v)\,dv=0\), with its closed-subspace Schwartz topology. The original strong space \(A\) consists of the smooth functions \(b:(0,\infty)\to\mathbb C\) for which
\[
 \sup_{u>0}(u^N+u^{-N})\left|(u\partial_u)^jb(u)\right|<\infty
 \qquad(N,j\ge0),
\]
with these seminorms. Its entire Mellin image is \(\mathcal B\), the functions rapidly decreasing on every bounded vertical strip, with every polynomial vertical seminorm. The restrictions come from the complete closed coefficient spaces \(V_\pm=S\oplus\mathbb C^2\); their two endpoint coordinates have zero restriction. Retain the original two-sign summation
\[
 \Sigma h(u)=2\sum_{n\ge1}h(nu),\qquad
 Rb(u)=u^{-1}b(u^{-1}),\qquad
 \mathcal M_0b(s)=\int_0^\infty b(u)u^s\,\frac{du}{u}.
 \tag{UOS1.1}
\]
Its exact image \(J=\Sigma S\) is closed, and
\[
 \pi:A\to Q=A/J\simeq\mathcal B/I_\zeta.
\]
The original zeta identity is
\[
 \mathcal M_0\Sigma h(s)
 =2\zeta(s)\int_0^\infty h(v)v^s\,\frac{dv}{v}.
 \tag{UOS1.2}
\]
The equivalent centered test entry retains
\(\mathcal Tk=2u^{-1/2}k\), \(\mathcal T^{-1}b=\frac12u^{1/2}b\), and
\(\mathcal M_0\mathcal Tk=2F_k\). These factors are unchanged.

Let \(\mathcal M\) be the entire functions of polynomial growth on every bounded vertical strip, and \(\mathcal J\subset\mathcal M\) the full actual zero-jet ideal of PGD2. For \(H\in\mathcal M\), the actual continuous functionals are
\[
 \lambda_H^\zeta([F])=
 \frac1{2\pi i}\left(
 \int_{2-i\infty}^{2+i\infty}
 -\int_{-1-i\infty}^{-1+i\infty}\right)
 \frac{H(s)F(1-s)}{\zeta(s)}\,ds ,
\]
\[
 \lambda_H^{\zeta^\vee}([F])=
 \frac1{2\pi i}\left(
 \int_{2-i\infty}^{2+i\infty}
 -\int_{-1-i\infty}^{-1+i\infty}\right)
 \frac{H(s)F(1-s)}{\zeta(1-s)}\,ds .
 \tag{UOS1.3}
\]
Both edges run upward. PGD proves convergence and descent for the first functional. For the second, reflection exchanges the two edge estimates; the same entire-numerator division proof, or the exact identity in UOS2, proves convergence, descent and continuity. The companion notation does not replace its denominator by a completed function.

Let \(T_a[F]=[a^sF(s)]\), \(a>0\), and
\[
 T_a^\vee\lambda=\lambda\circ T_{a^{-1}},\qquad
 \mathcal U_a\lambda=aT_a^\vee\lambda,\qquad
 Y=\chi\otimes Q',\quad\chi(a)=a .
\]
Here \(Q'\) is the continuous dual of the original Fréchet quotient. Use its weak-* topology for exact quotient topology assertions; the constructed transposes are also strong-dual continuous. The action on \(Y\) is \(\mathcal U_a\). It satisfies, for both denominators,
\[
 \mathcal U_a\lambda_H=\lambda_{a^sH},\qquad
 (1-L^t)\lambda_H=\lambda_{sH}.
 \tag{UOS1.4}
\]
These follow directly inside the absolutely convergent integrals from
\(a\,a^{-(1-s)}=a^s\) and \(1-(1-s)=s\). They are not inferred from a global exponential of an infinitesimal generator.

Write
\[
 D_\zeta x(y)=B_\zeta(x,y),\qquad
 D_{\zeta^\vee}x(y)=B_{\zeta^\vee}(x,y),
\]
\[
 C_\zeta=Y/D_\zeta Q,\qquad
 C_{\zeta^\vee}=Y/D_{\zeta^\vee}Q,\qquad
 c_H^\zeta=[\lambda_H^\zeta],\quad
 c_H^{\zeta^\vee}=[\lambda_H^{\zeta^\vee}].
 \tag{UOS1.5}
\]
These cokernels include the action \(\chi\); there is no second implicit twist on \(C_\zeta\). PGD constructs \(c_1^\zeta\ne0\) and the complete orbit
\[
 c_r^\zeta:=c_{r^s}^\zeta,\qquad
 \mathcal U_a c_r^\zeta=c_{ar}^\zeta,\qquad r,a>0.
 \tag{UOS1.6}
\]
No group-algebra independence theorem is needed for the calculations below.

## UOS2. Compute the complete companion reflection

On quotient Mellin functions, \(RF(s)=F(1-s)\). Direct substitution in UOS1.3 gives
\[
 (R'\lambda_H^\zeta)([F])
 =\lambda_H^\zeta([RF])
 =\frac1{2\pi i}\left(\int_{\Re s=2}^{\uparrow}
        -\int_{\Re s=-1}^{\uparrow}\right)
        \frac{H(s)F(s)}{\zeta(s)}\,ds.
\]
Set \(w=1-s\). In a single edge integral, the reversal of traversal and \(ds=-dw\) cancel; its image is an upward edge integral. The two edges exchange places, producing the remaining minus sign. Therefore
\[
 \boxed{R'\lambda_H^\zeta
   =-\lambda_{RH}^{\zeta^\vee},\qquad
   RH(s)=H(1-s).}
 \tag{UOS2.1}
\]
Reflection preserves \(\mathcal M\): a bounded strip maps into a bounded strip, with the same imaginary growth degree. Both operations in UOS2.1 are thus defined on the complete stated domains. Applying the same calculation to the companion gives its inverse identity. In particular its multiplier kernel is also \(\mathcal J\), because \(R\) preserves that full jet ideal and \(R'\) is invertible.

For \(H=r^s\) the exact factor is
\[
 RH(s)=r^{1-s}=r(r^{-1})^s,
\]
\[
 \boxed{R'\lambda_{r^s}^\zeta
   =-r\lambda_{(r^{-1})^s}^{\zeta^\vee}.}
 \tag{UOS2.2}
\]
No coefficient \(r\) has been absorbed into the variable or action.

The original full residue maps satisfy
\[
 R'D_\zeta=-D_{\zeta^\vee}R.
 \tag{UOS2.3}
\]
Indeed for \(x=[F]\in Q\), \(D_\zeta x=\lambda_F^\zeta\), and UOS2.1 is exactly this equality. It proves that \(R'\) induces a well-defined isomorphism of the two cokernels. The resulting classes obey
\[
 R'c_H^\zeta=-c_{RH}^{\zeta^\vee},\qquad
 R'c_r^\zeta=-r c_{1/r}^{\zeta^\vee},\qquad
 R'c_1^\zeta=-c_1^{\zeta^\vee}.
 \tag{UOS2.4}
\]
Thus the companion constant class is nonzero as well. The statement is about the two actual residue denominators; it is not an assertion that the individual pairing is reflection-invariant.

The functional-equation comparison of the denominators remains
\[
 \frac1{\zeta(1-s)}
 =\frac{2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)}{\zeta(s)}
 =\frac{\pi^{s-1/2}\Gamma((1-s)/2)}
        {\Gamma(s/2)\zeta(s)}.
 \tag{UOS2.5}
\]
The companion reciprocal vanishes at \(s=0\) and has value \(-2\) at \(s=1\). No meromorphic multiplier in UOS2.5 has been declared a member of the entire multiplier algebra \(\mathcal M\); UOS2.1 uses the separately defined companion contour and is valid without such an identification.

On the dual representation the precise prime/reflection identity is
\[
 \boxed{\mathcal U_a R'=aR'\mathcal U_{a^{-1}}.}
 \tag{UOS2.6}
\]
It follows from the original \(T_aR=aRT_{a^{-1}}\) after taking the contragredient and retaining its twist. On the full unit orbit it can also be checked without an operator convention:
\[
 \mathcal U_aR'c_r^\zeta
 =-r c_{a/r}^{\zeta^\vee}
 =aR'\mathcal U_{a^{-1}}c_r^\zeta.
\]
The oriented global dual mirror is \(-R'\), not \(R'\); it sends
\(c_r^\zeta\) to \(+r c_{1/r}^{\zeta^\vee}\).
The comparison cone uses \(R'\) in its degree-one term, as proved in ASD14. These distinct signs will be retained below.

## UOS3. The original localization row and its full transpose

Write
\[
 P=V_+\oplus V_-\oplus V_{\rm extra},\qquad
 d(v_+,v_-,w)=r_+v_+-r_-v_-,\qquad
 D_{\rm full}=[P\xrightarrow d A].
\]
The extra term is the complete pair of closed copies
\(V_{\rm extra}=V_+^{\rm extra}\oplus V_-^{\rm extra}\).
Let
\[
 H=\ker d=H_0\oplus V_{\rm extra},\qquad
 E=\mathbb C^4\oplus V_{\rm extra}.
\]
The four endpoint coordinates in \(H_0\) retain their labels
\(c_0,c_1,d_0,d_1\). The actual primal localization sequence is
\[
 0\to E\xrightarrow{\iota}H
 \xrightarrow{\operatorname{res}}A
 \xrightarrow{\beta}Q\oplus Q
 \xrightarrow{\delta}Q\to0,
\]
\[
 \operatorname{res}((h,c),(\widehat h,d),w)=\Sigma h,\qquad
 \beta(b)=(\pi b,\pi b),\qquad
 \delta(q_+,q_-)=q_+-q_-.
 \tag{UOS3.1}
\]
It is the original DCP7/DCP9 row, with no term erased.

Its exact continuous-dual row, twisted uniformly by \(\chi\), is
\[
 0\to Y\xrightarrow{\delta'}Y\oplus Y
 \xrightarrow{\beta'}\chi A'
 \xrightarrow{\operatorname{res}'}\chi H'
 \xrightarrow{\iota'}\chi E'\to0,
\]
\[
 \delta'\lambda=(\lambda,-\lambda),\qquad
 \beta'(\lambda_+,\lambda_-)=\pi'(\lambda_++\lambda_-),
\]
\[
 \operatorname{res}'\ell=(\Sigma'\ell,0,0,0,0,0),
 \qquad
 \iota'(u,c_0',c_1',d_0',d_1',w')
 =(c_0',c_1',d_0',d_1',w').
 \tag{UOS3.2}
\]
ASD2–ASD6 proves strict exactness for weak-* topologies, with all maps strong-dual continuous. In particular \(\pi'Q'=J^\perp\). The right-hand \(\iota'\) is an actual restriction map, including every extra closed functional.

For each \(H_{\rm mult}\in\mathcal M\), set \(\lambda=\lambda_{H_{\rm mult}}^\zeta\) and construct two different supported dual elements:
\[
 a_\lambda=(\lambda,-\lambda),\qquad
 b_\lambda=(\lambda/2,\lambda/2).
 \tag{UOS3.3}
\]
They satisfy
\[
 a_\lambda=\delta'\lambda,\quad
 \beta'a_\lambda=0,\quad
 \beta'b_\lambda=\pi'\lambda,\quad
 \operatorname{res}'\pi'\lambda=0,\quad
 \tfrac12(a_{\lambda,+}-a_{\lambda,-})=\lambda.
 \tag{UOS3.4}
\]
Every factor and sign follows by evaluation in UOS3.2. The first placement comes from the global dual and annihilates the image of the original boundary. The second evaluates that boundary:
\[
 a_\lambda(\beta b)=0,\qquad
 b_\lambda(\beta b)=\lambda(\pi b).
 \tag{UOS3.5}
\]
Thus the unit functional has explicit maps to the actual support row and its dual. It does not create an additional endpoint term in \(H'\): the exact map into \(H'\) is zero by UOS3.4.

This second evaluation is genuinely nonzero for the constructed unit. Pick any actual zero \(a\) of order \(m\) and let \(b=1-a\). Let \(q_a=e_{a,m-1}\) be its globally isolated top jet from SCL1. Then PGD2.2 gives
\[
 \lambda_1^\zeta(q_a)
 =(-1)^{m-1}\frac{m!}{\zeta^{(m)}(1-a)}\ne0.
 \tag{UOS3.6}
\]
An actual raw representative with \(\pi f_a=q_a\) is
\[
 f_a(u)=\frac1{2\pi}\int_{\mathbb R}
 E_{a,m-1}(1/2+it)\,u^{-1/2-it}\,dt\in A.
 \tag{UOS3.7}
\]
Its Mellin transform is the full \(E_{a,m-1}\), by the original inverse theorem. If \(k_a\) denotes the earlier centered representative, then
\(f_a=u^{-1/2}k_a=\frac12\mathcal T k_a\), retaining the factor2 comparison. Consequently
\(b_{\lambda_1}(\beta f_a)\) is exactly UOS3.6. This is an evaluation of the original boundary, not a claim that a functional is a primal cohomology class.

The original mirrors on the dual row are respectively \(-R'\) on its first \(Y\), exchange followed by \(R'\) on its middle pair, and \(R'\) on the final overlap dual. Hence
\[
 (a_{\lambda_H^\zeta})^{\rm mirror}
    =a_{\lambda_{RH}^{\zeta^\vee}},\qquad
 (b_{\lambda_H^\zeta})^{\rm mirror}
    =-b_{\lambda_{RH}^{\zeta^\vee}}.
 \tag{UOS3.8}
\]
For \(H=r^s\), the respective factors are \(+r\) and \(-r\) with parameter \(1/r\). Direct substitution in the exchange map proves both identities, and shows why the two placements must not share an invented mirror sign.

## UOS4. A complete map between the condensed primal and dual rows

After the exact preceding quotient by \(J\), the primal row in UOS3.1 is
\[
 0\to Q\xrightarrow{\Delta}Q^2\xrightarrow{\delta}Q\to0,
 \qquad\Delta q=(q,q),\quad\delta(q_+,q_-)=q_+-q_-.
\]
The condensed dual row is
\[
 0\to Y\xrightarrow{\alpha}Y^2\xrightarrow{\sigma}Y\to0,
 \qquad\alpha\lambda=(\lambda,-\lambda),\quad
 \sigma(\lambda_+,\lambda_-)=\lambda_++\lambda_-.
\]
There is an actual map of these exact rows:
\[
 \begin{array}{ccccccccc}
 0&\to&Q&\xrightarrow{\Delta}&Q^2&\xrightarrow{\delta}&Q&\to&0\\
 &&\downarrow D_\zeta&&
 \downarrow\operatorname{diag}(D_\zeta,-D_\zeta)&&
 \downarrow D_\zeta\\
 0&\to&Y&\xrightarrow{\alpha}&Y^2&\xrightarrow{\sigma}&Y&\to&0.
 \end{array}
 \tag{UOS4.1}
\]
Indeed its first square sends \(q\) to \((D_\zeta q,-D_\zeta q)\) on both paths; its second square sends \((q_+,q_-)\) to
\(D_\zeta(q_+-q_-)\) on both paths. Each column is injective, and each is equivariant for the original real and prime actions because \(D_\zeta T_a=\mathcal U_aD_\zeta\). These are constructed maps of the actual coefficient spaces, not an assumed duality of sheaves.

Taking the three displayed cokernels gives an exact row
\[
 \boxed{
 0\to C_\zeta\xrightarrow{c\mapsto(c,-c)}
 C_\zeta^2\xrightarrow{(c_+,c_-)\mapsto c_++c_-}
 C_\zeta\to0.}
 \tag{UOS4.2}
\]
A direct proof is that the first map is injective, the sum is surjective, and its kernel consists exactly of pairs \((c,-c)\). Its section is \(c\mapsto(c/2,c/2)\), and the retraction onto the first entry is half-difference. Thus this row preserves the full relative class \(c_1^\zeta\), while already calculating its exact localization maps.

The companion mirror is compatible with the entire diagram UOS4.1. On the primal row its three mirrors are \(R\), exchanged \(R\), and \(-R\). On the dual row they are \(-R'\), exchanged \(R'\), and \(R'\). UOS2.3 gives
\(D_\zeta R=-R'D_{\zeta^\vee}\), so both endpoint squares commute with these companion actions. On the middle term,
\[
 \operatorname{diag}(D_\zeta,-D_\zeta)
       (Rq_-,Rq_+)
 =(-R'D_{\zeta^\vee}q_-,\,R'D_{\zeta^\vee}q_+),
\]
which is exactly the exchanged dual mirror of
\((D_{\zeta^\vee}q_+,-D_{\zeta^\vee}q_-)\).
Therefore the first and last \(C_\zeta\)'s in UOS4.2 have respectively the induced companion maps \(-R'\) and \(R'\); the middle retains exchanged \(R'\). These are the distinct orientations of the same underlying quotient and group action.

The anti-diagonal map into the original, unquotiented \(Y^2\) does not factor through \(C_\zeta\) while keeping the stated maps. If it did, it would kill \(D_\zeta Q\); but for \(x\ne0\),
\(\alpha D_\zeta x\ne0\) by injectivity of both maps. Thus UOS4.2 constructs the exact relative target needed to descend that map. This proves the specific nonfactorization and immediately provides its replacement, rather than treating the objects as unrelated.

## UOS5. Construct the actual map to the dual-supported complex

Let \(K_Z\) be the original both-closed-support complex:
\[
 K_Z^0=P,\qquad K_Z^1=A\oplus A,\qquad
 d_Z(v_+,v_-,w)=(r_+v_+,r_-v_-).
 \tag{UOS5.1}
\]
The supported-to-global cochain map \(u:K_Z\to D_{\rm full}\) is
\[
 u^0=\operatorname{id}_P,\qquad
 u^1(b_+,b_-)=b_+-b_-.
\]
Both sides of its cochain equation are \(r_+v_+-r_-v_-\).

With the actual dual convention in ASD3, define
\[
 T_D=\chi D_{\rm full}^\vee[-2],\qquad
 T_Z=\chi K_Z^\vee[-2].
\]
Their only nonzero degrees are1 and2. Their differentials are
\[
 d_{T_D}^1\lambda=(r_+'\lambda,-r_-'\lambda,0),\qquad
 d_{T_Z}^1(\lambda_+,\lambda_-)
       =(r_+'\lambda_+,r_-'\lambda_-,0).
 \tag{UOS5.2}
\]
The transpose map \(j=\chi u^\vee[-2]:T_D\to T_Z\) is
\[
 j^1\lambda=(\lambda,-\lambda),\qquad
 j^2=\operatorname{id}_{\chi P'}.
 \tag{UOS5.3}
\]
Substitution in UOS5.2 verifies its cochain identity including the internal minus sign.

Compose the already constructed residue comparison with this actual transpose:
\[
 F_\zeta=j\Psi_\zeta:D_{\rm full}\to T_Z.
\]
It has degree-zero component0 and degree-one component
\[
 \boxed{
 F_\zeta^1b
 =(\pi'D_\zeta\pi b,\,-\pi'D_\zeta\pi b).}
 \tag{UOS5.4}
\]
The first source differential is killed because \(\pi d=0\); the target differential kills both components because \(\pi'Q'=J^\perp\). This proves the full cochain map on the original spaces.

No equivalence between original source restriction and numerical weights has been assumed. Formula UOS5.4 is the exact source-to-dual-supported comparison constructed from the original residue pairing and the existing support map.

## UOS6. Compute the full new cone and the map from the original comparison cone

Let
\[
 \mathcal K_\zeta=\operatorname{Cone}(\Psi_\zeta),\qquad
 \mathcal L_\zeta=\operatorname{Cone}(F_\zeta),
\]
using \(\operatorname{Cone}(f)^n=T^n\oplus D_{\rm full}^{n+1}\) and
\(d(v,c)=(d_Tv+fc,-dc)\). The second cone is the exact complex
\[
 \boxed{
 P\xrightarrow{-d}A
 \xrightarrow{(\Psi_\zeta^1,-\Psi_\zeta^1)}
 \chi A'^2\xrightarrow{d_{T_Z}^1}\chi P'
 }
 \quad\text{in degrees }-1,0,1,2.
 \tag{UOS6.1}
\]
Let \(M_\zeta=D_\zeta Q\subset Y\). Its cohomology is
\[
 H^{-1}(\mathcal L_\zeta)=H,\qquad
 H^0(\mathcal L_\zeta)=0,\qquad
 H^1(\mathcal L_\zeta)=Y^2/\alpha M_\zeta,\qquad
 H^2(\mathcal L_\zeta)=\chi E'.
 \tag{UOS6.2}
\]
For the first two groups, the argument is the actual source kernel and injectivity of \(D_\zeta\), as in ASD14. For the third,
\(\ker d_{T_Z}^1=\pi'Q'\oplus\pi'Q'\), and the image of the previous arrow is exactly
\((\pi'D_\zeta q,-\pi'D_\zeta q)\), since \(\pi\) is onto. The identification by \(\pi'\) proves the quotient. For the fourth, restriction of \(P'\) to
\(\ker d_Z=E\) gives the cokernel \(\chi E'\), as proved directly with continuous transposes in ASD5.

The full degree-one quotient has the explicit decomposition
\[
 \boxed{
 Y^2/\alpha M_\zeta
 \xrightarrow{\sim} C_\zeta\oplus Y,\qquad
 [(\lambda_+,\lambda_-)]
 \longmapsto
 \left(
 \left[\frac{\lambda_+-\lambda_-}{2}\right],
 \frac{\lambda_++\lambda_-}{2}
 \right).}
 \tag{UOS6.3}
\]
Adding \((D_\zeta q,-D_\zeta q)\) changes the first component by \(D_\zeta q\) and the second by zero, proving well-definedness. The inverse sends
\(([\lambda],\mu)\) to \([(\lambda+\mu,-\lambda+\mu)]\); a different representative of \([\lambda]\) changes the pair by \(\alpha M_\zeta\). Substitution gives both inverse identities. The maps are continuous for the indicated quotient weak-* topologies, since both underlying half-sum and half-difference maps and their inverses are continuous. In particular its Hausdorff quotient is \(Y\), whereas the nonzero \(C_\zeta\) summand retains the algebraic defect proved in PGD.

The strict square with identity on the source and \(j\) on the target gives the actual cone map
\[
 \mathcal J_\zeta:\mathcal K_\zeta\to\mathcal L_\zeta.
\]
Its four components are
\[
 \mathcal J_\zeta^{-1}=\operatorname{id}_P,\quad
 \mathcal J_\zeta^0=\operatorname{id}_A,\quad
 \mathcal J_\zeta^1\lambda=(\lambda,-\lambda),\quad
 \mathcal J_\zeta^2=\operatorname{id}_{\chi P'}.
 \tag{UOS6.4}
\]
Every cochain equation follows from UOS5.2–UOS5.4. On the complete cohomology it is
\[
 \begin{array}{c|c}
 \text{degree}&H^n(\mathcal J_\zeta)\\ \hline
 -1&\operatorname{id}_H\\
 0&0\to0\\
 1&C_\zeta\to C_\zeta\oplus Y,\quad c\mapsto(c,0)\\
 2&\chi H'\to\chi E',\quad\iota'.
 \end{array}
 \tag{UOS6.5}
\]
The degree2 map is not an unspecified comparison: it is the actual restriction
\[
 (u,c_0',c_1',d_0',d_1',w')
 \longmapsto(c_0',c_1',d_0',d_1',w')
\]
from UOS3.2. Its kernel is precisely the \(S'\) coordinate, and its section appends zero there. All four endpoint lines and both full extra copies remain.

Consequently the nonzero orbit \(c_r^\zeta\) has a proved nonzero image
\((c_r^\zeta,0)\) in the actual dual-supported comparison cone. Its image does not acquire a component in the additional \(Y\) summand. These are concrete maps locating the class, rather than a declaration that the two cones are the same.

## UOS7. The companion mirror on both cones and on the split result

Let \(w_D\) be the original Cech mirror: chart and extra swap in degree0 and \(-R\) in degree1. Let \(w_Z\) be the original supported mirror: the same degree-zero swap and
\((b_+,b_-)\mapsto(Rb_-,Rb_+)\) in degree1. The map \(u\) is equivariant; hence \(j\) intertwines their shifted dual mirrors \(w_{T_D}\) and \(w_{T_Z}\).

ASD14 proves
\[
 \Psi_\zeta w_D=-w_{T_D}\Psi_{\zeta^\vee}.
\]
Composing with \(j\) gives the exact companion identity
\[
 F_\zeta w_D=-w_{T_Z}F_{\zeta^\vee}.
 \tag{UOS7.1}
\]
Therefore the cone mirror from the companion to the original is
\[
 (v,c)\longmapsto(-w_Tv,w_Dc)
\]
for each target \(T=T_D,T_Z\). The same formula with the denominators exchanged is its inverse; the two target signs cancel on applying it twice. This is an actual cochain map by the displayed identity.

In degree1 of \(\mathcal K_\zeta\), that map is \(R'\), because
\(w_{T_D}^1=-R'\). Thus its action on the unit orbit is exactly the signed companion action UOS2.4. In degree1 of \(\mathcal L_\zeta\), the map is
\[
 (\lambda_+,\lambda_-)
 \longmapsto(-R'\lambda_-,-R'\lambda_+).
 \tag{UOS7.2}
\]
Under the exact half-difference/half-sum decomposition UOS6.3, it becomes
\[
 (c,\mu)\longmapsto(R'c,-R'\mu)
 \quad\text{with the companion denominators exchanged}.
 \tag{UOS7.3}
\]
Indeed the new half-difference is
\(R'(\lambda_+-\lambda_-)/2\), while the new half-sum is
\(-R'(\lambda_++\lambda_-)/2\).
This verifies all signs and the compatibility of \(c\mapsto(c,0)\) with the mirror.

For the orbit from the original to the companion, UOS7.3 gives
\[
 (c_r^\zeta,0)\longmapsto(-r c_{1/r}^{\zeta^\vee},0).
 \tag{UOS7.4}
\]
Each receiving real action satisfies
\(\mathcal U_a w=a\,w\mathcal U_{a^{-1}}\), including these companion maps, by UOS2.6 and the fixed signs. The source terms obey the same original relation by DCP11. Thus the full cone map UOS6.4, the companion map and every prime action commute in the stated squares with the exact factor \(a\). No self-mirror pairing or missing Tate twist is presumed.

## UOS8. Source ring, all retained labels, and the original Fourier lift

The source receiving ring remains
\(\mathbb Z^3\) with \(\epsilon=(1,0,0)\), \(e_+=(0,1,0)\), \(e_-=(0,0,1)\). The source map is
\[
 [n]=(n,0,0),\qquad[\tau]=(1,1,1).
\]
On the spectral term \(Q\), its dual and all the core cokernels, \((r,b_+,b_-)\) acts by the scalar \(r\). On the complete extra closed copies and their duals it acts respectively by \(b_+\) and \(b_-\). Every new chain map above is receiving-ring linear: the overlap maps have the same scalar on both sides, their zero components commute with all actions, and the maps on extra copies in UOS6.4 are identities. The mirror exchanges \(e_+,e_-\), fixes \(\epsilon\), and hence fixes each original source integer and \(\tau\).

Thus, on the orbit,
\[
 [n]c_r^\zeta=n c_r^\zeta,\qquad
 [\tau]c_r^\zeta=c_r^\zeta,\qquad
 \mathcal U_p c_r^\zeta=c_{pr}^\zeta.
 \tag{UOS8.1}
\]
The source integer scalar and the independent spectral prime action are explicitly different operations. Their notation is not interchanged. The faithful source distinction between \(\tau\) and integer1 remains in every full \(P,P'\) and extra closed term.

For the existing receiving support lattice \(L_{\rm supp}\), each receiving linear map \(f\) above has the exact label-preserving lift
\[
 G_{L_{\rm supp}}(f)(v,\alpha)=(f(v),\alpha),\qquad
 G_{L_{\rm supp}}(V)=
 \{(0,\alpha):\alpha\in L_{\rm supp}\}
 \cup\{(v,1_{L_{\rm supp}}):v\in V\}.
 \tag{UOS8.2}
\]
Linearity proves that a nontop-labelled zero stays a zero with its original label. Identity and composition follow by substitution. In particular injectivity of \(c\mapsto(c,0)\) remains injectivity on the lifted common-label carrier. Independently labelled closed factors remain separate factors of products; no common-label carrier is identified with such a product. Vanishing amplitudes in UOS3.4 retain their support labels and are not identified with primitive \(\tau\).

The original single-chart lifting map is also still present:
\[
 (h,d_0,d_1)\longmapsto
 ((\widehat h,0,0),(h,d_0,d_1))
\]
from \(V_-\) to the global Fourier graph. The equality
\(\Sigma\widehat h=R\Sigma h\) proves it is a continuous section of restriction. For the full source-faithful coefficients append the given minus extra coordinate and zero plus extra coordinate. This gives the corresponding section there too. Its ordinary localization connecting map is zero by that explicit section. The nonzero class \(c_1^\zeta\) does not alter this original map or turn that proved section into a failure.

## UOS8A. The entire faithful group orbit in the actual supported comparison

The original-zeta calculation [GGT0–GGT8](GLOBAL_GAUSSIAN_ORIGINAL_ZETA_TRACE.md) has now been read completely. It proves the following bounds for the actual zeros with all multiplicities:
\[
 S_T(x)=\sum_{\rho}m_\rho x^\rho e^{\rho^2/T^2},\qquad T\ge1,
\]
\[
 S_T(1)=\frac{T}{2\sqrt\pi}
 \left[\log T-\log(4\pi)-\frac\gamma2\right]
 +1+O(\log(2+T)),\qquad
 S_T(x)=O_x(T)\quad(x\ne1).
 \tag{UOS8A.1}
\]
These are consequences of the full original formula GGT3.2, with both prime series, the exact archimedean contour and the original pole term. GGT3.3–GGT3.6 retains all crossed trivial-zero terms in every finite contour comparison. GGT8 also proves that for each \(F\in\mathcal B\) and fixed \(x>0\),
\[
 \sup_{T\ge1}\sum_\rho m_\rho
 |x^\rho F(\rho)e^{\rho^2/T^2}|<\infty .
 \tag{UOS8A.2}
\]
We use these full-space results to determine the orbit's actual algebraic size.

Let \(r_1,\ldots,r_N>0\) be pairwise distinct. Suppose
\[
 \sum_{i=1}^N a_i c_{r_i}^\zeta=0 .
\]
By the definition of the cokernel and linearity of the contour, there is a single \(F\in\mathcal B\) for which
\[
 \lambda_H^\zeta=D_\zeta[F]=\lambda_F^\zeta,
 \qquad H(s)=\sum_{i=1}^N a_i r_i^s.
\]
PGD2's complete kernel theorem then says \(H-F\in\mathcal J\): the full original multiplicity jets agree, in particular \(H(\rho)=F(\rho)\) at every original zero. Fix \(j\) and multiply this value equality by
\(m_\rho r_j^{-\rho}e^{\rho^2/T^2}\). The sums are absolutely convergent by GGT1 and UOS8A.2, so summation gives exactly
\[
 \sum_{i=1}^N a_i S_T(r_i/r_j)
 =\sum_\rho m_\rho r_j^{-\rho}F(\rho)e^{\rho^2/T^2}.
 \tag{UOS8A.3}
\]
The right side is \(O_{F,r_j}(1)\). The term with \(i=j\) equals
\(a_jT\log T/(2\sqrt\pi)+O(T)\), and each other term is \(O(T)\) because \(r_i/r_j\ne1\). Divide by \(T\log T\) and let \(T\to\infty\). The result is \(a_j/(2\sqrt\pi)=0\). This holds for each \(j\), proving linear independence of the entire positive-real orbit. The argument uses the necessary value consequence of full jet equality; it neither discards the higher jets from \(Q\) nor assumes their synthesis.

Define the group algebra \(\mathbb C[\mathbb R_+^\times]\) to consist of finite formal sums of basis elements \([r]\), with \([r][a]=[ra]\). These brackets are receiving group-algebra notation, distinct from the source-action brackets in UOS8. The explicit module map is
\[
 \boxed{
 \iota_{\mathrm{orb}}:
 \mathbb C[\mathbb R_+^\times]\longrightarrow C_\zeta,
 \qquad \sum_r a_r[r]\longmapsto\sum_r a_r c_r^\zeta .
 }
 \tag{UOS8A.4}
\]
It is injective by the preceding proof and intertwines left translation by \([a]\) with the actual receiving action \(\mathcal U_a\). Consequently its image is the regular cyclic submodule generated by \(c_1^\zeta\). This is an algebraic equivariant linear embedding into a module; it does not equip \(C_\zeta\) with an invented multiplication or identify the embedding as a ring homomorphism. No Hausdorff topological embedding into this non-Hausdorff cokernel is asserted.

The subgroup of positive rationals is free abelian on the original arithmetic primes, by the already reconstructed unique integer factorization and its extension to ratios. Therefore UOS8A.4 restricts to the injective module map
\[
 \mathbb C[t_p,t_p^{-1}:p\ {\rm an\ original\ prime}]
 \longrightarrow C_\zeta,\qquad
 \prod_p t_p^{n_p}\longmapsto c_{\prod_p p^{n_p}}^\zeta ,
 \tag{UOS8A.5}
\]
where each monomial and polynomial involves finitely many primes. Every original prime dilation is retained; this is not a finite packet or a quotient by relations among distinct prime products.

Composing with the actual cone map UOS6.5 gives the proved supported placement of this whole regular module:
\[
 \boxed{
 \mathbb C[\mathbb R_+^\times]\hookrightarrow
 H^1(\mathcal L_\zeta)=C_\zeta\oplus Y,
 \qquad [r]\longmapsto(c_r^\zeta,0).
 }
 \tag{UOS8A.6}
\]
It is injective because both constituent maps are injective. On the two residue denominators, its exact comparison-cone companion mirror is the linear involution
\[
 [r]_\zeta\longmapsto -r[1/r]_{\zeta^\vee}.
 \tag{UOS8A.7}
\]
Its square is identity since \((-r)(-1/r)=1\). The original oriented global-dual mirror instead has \(+r[1/r]\). The minus sign in UOS8A.7 means it is not a unital group-algebra homomorphism; it is the exact companion linear symmetry of the cone. Both variants retain the relation \(\mathcal U_a w=a\,w\mathcal U_{a^{-1}}\).

Finally the complete source action on this module is the one already proved in UOS8: source \(n\) acts by the scalar \(n\) and source \(\tau\) by identity on this receiving summand, while a spectral prime translates its basis. The source distinction remains faithful on the retained extra closed copies of the full complexes. None of UOS8A.1–UOS8A.7 assigns a numerical weight to primitive \(Z_1/\tau\) or turns the regular module into a purity theorem. It determines the size, exact prime action, companion inversion and actual supported placement of the global object that has been constructed.


## UOS9. Exact mathematical placement of the global orbit

There are three proved statements, with their actual maps:

1. The functional \(\lambda_1^\zeta\) is in the ordinary continuous dual \(Q'\). Its anti-diagonal supported class is \(\delta'\lambda_1^\zeta\), so it already comes from the global dual. Its half-diagonal evaluates the actual original boundary nontrivially by UOS3.6. Both maps retain all support and orientation data.

2. Its class \(c_1^\zeta\) is nonzero because \(\lambda_1^\zeta\notin D_\zeta Q\). This is exactly a failure of representation by the specified original-zeta residue pairing. It is the actual residue-comparison cone class, not a newly asserted obstruction to the original Fourier restriction lift. The direct anti-diagonal supported map cannot descend through this cokernel without the further quotient proved in UOS4.

3. The exact chain map UOS6.4 injects this relative class into the dual-supported comparison cone, where its image is \((c_1^\zeta,0)\). The full real orbit and companion inversion are respectively
\((c_r^\zeta,0)\mapsto(c_{ar}^\zeta,0)\) and
\((c_r^\zeta,0)\mapsto(-r c_{1/r}^{\zeta^\vee},0)\).
The map on \(H\) is identity, and the map on \(H'\) is the explicit endpoint/extra restriction, so these terms have not been omitted.

These constructions establish the orbit's precise relationship to the original supported localization mechanism. They prove no numerical separation of the weights on that mechanism, and they do not turn the arithmetic constant \(1\), a functional, or a comparison-cone class into primitive \(Z_1/\tau\). The new mathematical result is the complete companion and prime action together with the actual localization-row and cone morphisms locating the already constructed global object.

## Exact original character lifting and its full supported return

MCL0–MCL11 now computes the original transpose A′→S′ on every actual zero and all its Mellin jets. A target jet of order j needs generalized-character length exactly m+j+1 at a zero of multiplicity m. The full Euler-distribution classification proves minimality against the whole original continuous dual; two actual primes remove the single-prime character aliases. Every prime logarithm and the full Gamma/Fourier return remain. This is an actual continuous lift, with a nonzero class only when its original annihilator must be preserved.

RPC0–RPC8 constructs the original restriction's actual pushout by the residue image, proves its precise cochain location and a single coherent real/prime-equivariant section on all locally finite classes. ORE0–ORE10 calculates the unmodified connecting class, including its full Gamma germ and rank min(m,r), then proves its place in every degree of the full supported derived comparison. The degree-two map is (eta,e)↦(−delta_q(eta)/2,e). Thus its image in C_zeta/qC_zeta is zero, while the full supported map retains its Y/qY component. Both assertions follow from the constructed maps; no cone degree or extra coefficient is discarded.

These results refine the meaning of the prior finite-lift statement without withdrawing its proved scope. Fixed-annihilator splitting is stronger than the surjectivity in Deligne's invariant-cycle theorem. The original longer-chain map is already surjective. The present numerical character truncation retains its same-character extension whenever it retains the target; it is not Deligne's independently proved geometric weight gap. Complete proofs, independent checks and inspected reproducible diagrams have been inserted into the cumulative TeX. The actual tau weight-separation goal remains active.
