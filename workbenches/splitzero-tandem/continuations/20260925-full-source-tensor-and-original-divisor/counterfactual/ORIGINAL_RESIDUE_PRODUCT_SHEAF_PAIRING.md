# The original residue pairing on the product of the actual coefficient spaces

24 September 2026. Complete receiving derivation PRS0–PRS9.

## PRS0. Source data, provenance and the calculation being attempted

The user's amended instruction is to ask what would advance the target using both the finding and everything already established, then attempt that calculation. The immediately preceding finding is [FTD9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/FINITE_TOPOLOGY_DUALIZING_COMPLEX.md): the existing global residue map has a constructed continuous-dual sheaf target, but cannot be the derived global sections of a degree-zero morphism to that target on the same three-point space. The calculation here constructs its actual product-space origin. No source operation is inferred from a receiving scalar calculation.

The current source remains [B1–B5, P1–P5 and R1](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md). In the user's notation, \(Z_0\) is absence, \(Z_1/\tau\) is presence without \(Z_2\) parity or addition, and the supplied integer layer retains its integer amounts and \(Z_2\) data. Neither copies of primitive \(\tau\) nor a numerical weight on it are introduced. Every tensor, sum, dual and contour below is an operation on the explicitly constructed receiving vector spaces.

Alain Connes and Caterina Consani construct the three-point base, coefficient restrictions, ordered Čech complex and Fourier lift in [*Schemes over \(\mathbb F_1\) and zeta functions*, 0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). Their original author TeX and exact locators are retained in [DCP0](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SOURCE_CC_DOUBLE_PULLBACK.md). The faithful source comparison is the complete DCP and [CGS](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SOURCE_COEFFICIENT_GLUE.md) construction, including all arithmetic points and the added closed copies. Ralf Meyer's [*A spectral interpretation for the zeros of the Riemann zeta function*, math/0412277v3](https://arxiv.org/abs/math/0412277v3) supplies the analytic framework used in the retained [OMS proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md). The exact original denominator, division, continuity and two-sided nondegeneracy are proved in [GZR1–GZR8](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md), with their unshifted return in [ASD1 and ASD14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ACTUAL_SUPPORTED_DUALITY_INDEPENDENT.md).

Pierre Deligne's [*La conjecture de Weil. II*, §§3.3.11, 3.4.8 and 3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/) is the human source for the duality, gluing and lifting comparison being sought. The retained French text is an identified transcription, not author TeX. In particular §3.3.11 identifies the dualizing-complex property used for the Poincaré argument. We calculate our actual complexes rather than assigning them that property.

## PRS1. Full coefficients and original analytic pairing

Write the receiving base as
\[
Y=\{c_+,c_-,\eta\},\quad U_\pm=\{c_\pm,\eta\},\quad U_\eta=\{\eta\}.
\]
Its opens are \(\varnothing,U_\eta,U_+,U_-,Y\). Retain
\[
S=\{h\in\mathcal S(\mathbb R;\mathbb C):h(-v)=h(v),\ h(0)=0,\ \int_{\mathbb R}h(v)\,dv=0\},
\]
\[
A=\{b\in C^\infty(\mathbb R_{>0}):\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jb(u)|<\infty\text{ for all }N,j\geq0\},
\]
\[
\Sigma h(u)=2\sum_{n\geq1}h(nu),\qquad Rb(u)=u^{-1}b(u^{-1}),\qquad
M_0b(s)=\int_0^\infty b(u)u^s\frac{du}{u}.
\tag{PRS1.1}
\]
The full coefficient sheaf is
\[
\mathcal F=\Omega_{\rm full}=(W_+\xrightarrow{r_+}A\xleftarrow{r_-}W_-),\qquad
W_\pm=(S\oplus\mathbb C^2_\pm)\oplus V_\pm^{\rm extra},
\]
\[
r_+(h,c_0,c_1,v)=\Sigma h,\qquad r_-(h,d_0,d_1,v)=R\Sigma h.
\tag{PRS1.2}
\]
The extra copies are the full copies supplied by DCP, not just their endpoint subspaces. The Fourier convention is \(\widehat h(t)=\int h(v)e^{-2\pi ivt}\,dv\). Its complete Poisson formula is
\[
\Sigma\widehat h(u)=u^{-1}\Sigma h(u^{-1})+u^{-1}h(0)-\int h(v)\,dv.
\tag{PRS1.3}
\]
The two last terms vanish on the stated \(S\); all four endpoint coordinates remain in (PRS1.2). The proved image theorem gives the closed subspace
\[
J=\Sigma S=r_+(W_+)=r_-(W_-),\qquad Q=A/J,
\]
and identifies \(M_0J\) with the entire functions rapidly decreasing on bounded vertical strips whose full required jets vanish at every actual nontrivial zero of \(\zeta\). Thus none of these zeros or their multiplicities is selected in advance.

For \(b,c\in A\) put
\[
\mathcal B_\zeta(b,c)=\frac1{2\pi i}
\left(\int_{2-i\infty}^{2+i\infty}-\int_{-1-i\infty}^{-1+i\infty}\right)
\frac{(M_0b)(s)(M_0c)(1-s)}{\zeta(s)}\,ds.
\tag{PRS1.4}
\]
Both edges are upward. The reciprocal on the right edge is bounded by \(\zeta(2)\); on the left it is bounded by \(4\pi^2\zeta(2)(1+|t|)^{-3/2}\), as derived in GZR2 from the complete multiplier
\[
\chi_\zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)},\qquad
\zeta(s)=\chi_\zeta(s)\zeta(1-s).
\tag{PRS1.5}
\]
In particular, writing \(b_{2,1}(F)=\sup_{|\sigma|\leq2,t}(1+|t|)|F(\sigma+it)|\),
\[
|\mathcal B_\zeta(b,c)|\leq
\frac{\zeta(2)(1+4\pi^2)}{\pi}\,b_{2,1}(M_0b)b_{2,1}(M_0c).
\tag{PRS1.6}
\]
This proves joint continuity. It is not a completed-zeta pairing. At zero, \(\zeta(0)=-1/2\); at one, its reciprocal has a zero. The trivial zeros lie outside the indicated strip. The original Schwartz return still contains their residues
\[
\operatorname{Res}_{s=-2m}\frac{H(s)}{\zeta(s)}=\frac{H(-2m)}{\zeta'(-2m)},\quad
\zeta'(-2m)=(-1)^m2^{-2m-1}\pi^{-2m}(2m)!\zeta(1+2m),\quad m\geq1.
\tag{PRS1.7}
\]
For an earlier centered representative \(k\), the already constructed return is \(\mathcal Tk(u)=2u^{-1/2}k(u)\), so \(M_0\mathcal Tk=2\mathcal Mk\). In the notation of GZR2 the exact identity is
\[
\mathcal B_\zeta(\mathcal Tk,\mathcal Tl)=4\mathfrak B_\zeta(\mathcal Mk,\mathcal Ml).
\]
The right-hand arguments are the original centered Mellin transforms, while the left-hand arguments are their unshifted physical representatives. The factor four is retained, not replaced by a choice of representative.

The actual division theorem makes \((M_0b)/\zeta\) holomorphic and rapidly decreasing on this closed strip when \(b\in J\). Cauchy's theorem on the rectangle, followed by the vanishing horizontal integrals of length three, then proves \(\mathcal B_\zeta(J,A)=0\). Reflection preserves every zero multiplicity by (PRS1.5), so the same proof gives \(\mathcal B_\zeta(A,J)=0\). Hence
\[
\mathcal B_\zeta(b,c)=B_\zeta(\pi b,\pi c),\qquad
D_\zeta:Q\longrightarrow\chi_{\rm dil}Q',\quad D_\zeta x(y)=B_\zeta(x,y),
\tag{PRS1.8}
\]
where \(\pi:A\to Q\) and \(\chi_{\rm dil}(a)=a\). The two-sided nondegeneracy theorem GZR6 applies through the displayed factor-four return. It asserts zero left and right radicals; it does not assert that the linear map \(Q\otimes Q\to\mathbb C\) is injective or that \(D_\zeta\) is onto.

## PRS2. A genuine product-space sheaf morphism

All tensor products in this proof are algebraic over \(\mathbb C\) unless a topology is explicitly stated. Define the external tensor sheaf on the finite product topology by
\[
\mathcal E_{(x,y)}=\mathcal F_x\otimes\mathcal F_y,
\]
with restriction \(r_{xx'}\otimes r_{yy'}\) for each ordered specialization to a more generic point. These maps compose because the original restrictions do. A finite-topology diagram specifies a sheaf by compatible families on each open; gluing holds componentwise. This constructs \(\mathcal E=\mathcal F\boxtimes\mathcal F\) without a completed tensor-product assertion.

Let \(j_{\eta\eta}:\{(\eta,\eta)\}\hookrightarrow Y^2\) and
\[
\mathcal K=j_{\eta\eta!}\chi_{\rm dil}\mathbb C.
\]
Its stalk at \((\eta,\eta)\) is the displayed character line and its other eight stalks are zero. All nonidentity restrictions are zero. This is extension by zero: a morphism from this diagram is exactly a map from its generic value to the generic value of the target, with no further condition.

Define \(\beta_\zeta:\mathcal E\to\mathcal K\) at the generic pair by
\[
\beta_{\zeta,\eta\eta}(b\otimes c)=\mathcal B_\zeta(b,c),
\tag{PRS2.1}
\]
and by zero on the other eight stalks. Bilinearity gives a unique linear map on the algebraic tensor. For any restriction into the generic pair from a different point, at least one component lies in \(r_+(W_+)=J\) or \(r_-(W_-)=J\). Equation (PRS1.8) kills it. Every other compatibility has both sides zero. Thus (PRS2.1) is an actual sheaf morphism, with all nine stalk maps and restrictions checked.

The bound (PRS1.6) also extends the generic bilinear map continuously to the completed projective tensor product. The sheaf and cohomology calculations below use the already specified algebraic tensor; no equality with a completed Künneth object is required or claimed.

## PRS3. Ordered product Čech complex and trace

Put \(P=W_+\oplus W_-\) and \(d(p_+,p_-)=r_+p_+-r_-p_-\). The original complex is
\[
D=[P\xrightarrow{d}A],\qquad \deg P=0,\quad\deg A=1.
\]
For the two ordered covers \((U_+,U_-)\), the product Čech double complex has total complex
\[
C^0=P\otimes P,\quad
C^1=(P\otimes A)\oplus(A\otimes P),\quad
C^2=A\otimes A,
\]
\[
d_C^0(p\otimes q)=(p\otimes dq,dp\otimes q),\qquad
d_C^1(x,y)=(d\otimes1)x-(1\otimes d)y.
\tag{PRS3.1}
\]
The sign follows from \(d_{D\otimes D}=d\otimes1+(-1)^i1\otimes d\) on first degree \(i\). Direct substitution gives \(d_C^1d_C^0=dp\otimes dq-dp\otimes dq=0\).

Here is why this complex computes the indicated sheaf cohomology. Every nonempty intersection of the product cover is a minimal open \(U_x\times U_y\). Sections over it are its value at \((x,y)\), an exact evaluation functor, so higher cohomology on it vanishes. The augmented Čech resolution is exact stalkwise: at a point belonging to both one-dimensional charts it is the split augmented sequence \(0\to V\to V^2\to V\to0\), and at a point belonging to only one chart it is the identity augmentation. Taking the two successive resolutions gives an exact product resolution, with precisely the total sign in (PRS3.1). Its terms are globally acyclic. Indeed, for the inclusion \(j\) of any such intersection, the intersection with any other minimal product open is again minimal or empty. Thus every stalk of \(j_*G\) is an exact evaluation of \(G\) or zero, proving that this particular \(j_*\) is exact. It also preserves injectives because its left adjoint, restriction, is exact. Applying it to an injective resolution therefore proves \(R\Gamma(Y^2,j_*G)=R\Gamma(\operatorname{dom}j,G)\), whose positive cohomology vanishes by exact evaluation. This proves the required Čech computation rather than assuming a topological Künneth theorem.

For \(\mathcal K\) the same double complex is zero except at bidegree \((1,1)\), where it is \(\chi_{\rm dil}\mathbb C\). Therefore
\[
R\Gamma(Y^2,\mathcal K)=\chi_{\rm dil}\mathbb C[-2],\qquad
\operatorname{tr}_{\eta\eta}:H^2(Y^2,\mathcal K)\to\chi_{\rm dil}\mathbb C,\quad z\mapsto z.
\tag{PRS3.2}
\]
The trace is the coefficient in the ordered pair of overlaps, with sign \(+1\). The resulting cochain map is
\[
C\longrightarrow\chi_{\rm dil}\mathbb C[-2],\qquad
\beta^0=\beta^1=0,\quad \beta^2(b\otimes c)=\mathcal B_\zeta(b,c).
\tag{PRS3.3}
\]
Its cochain equation is exactly the two annihilations in (PRS1.8), applied to the two terms in \(d_C^1\). Endpoints and both full extra copies remain in \(C^0,C^1\); their restrictions are the original zero maps, not discarded summands.

The top cohomology has the precise form
\[
H^2(C)=(A\otimes A)/(J\otimes A+A\otimes J)\xrightarrow{\ \pi\otimes\pi\ }Q\otimes Q.
\tag{PRS3.4}
\]
This arrow is an isomorphism. A bilinear map on \(A\times A\) factors through \(Q\times Q\) exactly when it vanishes on \(J\) in each slot; the universal properties of the two tensors give inverse maps between the quotient and \(Q\otimes Q\). Thus its kernel and surjectivity are both proved. The other two cohomology groups are retained as
\[
H^0(C)=\ker d_C^0,\qquad H^1(C)=\ker d_C^1/\operatorname{im}d_C^0.
\tag{PRS3.5}
\]
No vanishing of these groups is used to define the trace.

## PRS4. Exact return to the original global dual map

The continuous dual complex \(D'_c\) is \([A'\xrightarrow{d'}P']\) in degrees \(-1,0\), with \((d'\lambda)(p)=\lambda(dp)\). Thus \(\chi_{\rm dil}D'_c[-2]\) has degrees \(1,2\). Currying (PRS3.3), retaining the first factor as source, gives
\[
\Phi:D\longrightarrow\chi_{\rm dil}D'_c[-2],\qquad
\Phi^0=0,\quad (\Phi^1b)(c)=\mathcal B_\zeta(b,c).
\tag{PRS4.1}
\]
There is no factor permutation and hence no permutation sign. Continuity is (PRS1.6). The two cochain conditions are
\[
\Phi^1dp=0,\qquad (d'\Phi^1b)(p)=\mathcal B_\zeta(b,dp)=0.
\]
By (PRS1.8), as an equality of the original maps with their complete domains and codomains,
\[
\boxed{\Phi^1=\pi'D_\zeta\pi=\Psi_\zeta^1.}
\tag{PRS4.2}
\]
Consequently this is exactly the global comparison in ASD14 and SCT, with its previously calculated full cone. It is not an independent substitute having the same zero set.

FTD8 constructs its same-space target as \(R\Gamma(Y,\chi_{\rm dil}\mathbb D_c\mathcal F[-2])\). FTD9 proves that the degree-zero same-space sheaf morphism to that specific target vanishes. Equations (PRS2.1)–(PRS4.2) explain the nonzero global map by the external product and its degree-two trace. The two degree-one inputs are essential to this construction. No Poincaré-duality identification is inferred from the resulting degree two.

## PRS5. Both original supports: full matrix and exact radical

Retain the actual two-support complex and its map to the original global complex:
\[
D_Z=[P\xrightarrow{d_Z}A\oplus A],\quad
d_Z(p_+,p_-)=(r_+p_+,r_-p_-),
\]
\[
u^0=\operatorname{id}_P,\qquad u^1(a_+,a_-)=a_+-a_-.
\tag{PRS5.1}
\]
The equality \(u^1d_Z=d\) proves the cochain condition. Pulling (PRS3.3) back through \(u\otimes u\) gives in degree two
\[
\begin{aligned}
\mathcal B_Z((a_+,a_-),(b_+,b_-))={}&\mathcal B_\zeta(a_+,b_+)-\mathcal B_\zeta(a_+,b_-)\\
&-\mathcal B_\zeta(a_-,b_+)+\mathcal B_\zeta(a_-,b_-).
\end{aligned}
\tag{PRS5.2}
\]
Each boundary is killed because each of its components belongs to \(J\). On \(H^1(D_Z)=Q\oplus Q\), its curried map is exactly
\[
\begin{pmatrix}D_\zeta&-D_\zeta\\-D_\zeta&D_\zeta\end{pmatrix}.
\tag{PRS5.3}
\]
The left radical is \(\Delta Q=\{(q,q):q\in Q\}\). Indeed a vector in this diagonal has difference zero. Conversely, if its pairing with all \((y,0)\) vanishes, then \(B_\zeta(q_+-q_-,y)=0\) for all \(y\), and the proved left nondegeneracy gives \(q_+=q_-\). The same argument with right nondegeneracy proves the right radical is also \(\Delta Q\).

The original boundary from the open part is \(A\to Q^2\), \(a\mapsto(\pi a,\pi a)\). Its image is exactly this radical because \(\pi\) is onto. The induced quotient map
\[
(Q\oplus Q)/\Delta Q\longrightarrow Q,\qquad [(q_+,q_-)]\longmapsto q_+-q_-
\tag{PRS5.4}
\]
is an isomorphism: it is onto via \((q,0)\), and its kernel is the displayed diagonal. The induced form is precisely \(B_\zeta\). In the symmetric splitting used in SCT, \((q_+,q_-)=(h+k,h-k)\); (PRS5.2) is therefore \(4B_\zeta(k,l)\), with the factor four retained. This constructs the exact relationship between the open boundary and the pairing radical, without asserting that a single linear functional on \(Q\otimes Q\) is injective.

## PRS6. All real and prime actions, and the source scalar action

For \(a>0\), \(T_ab(u)=b(u/a)\) gives \(M_0T_ab(s)=a^sM_0b(s)\). Therefore, directly in the original integral,
\[
\mathcal B_\zeta(T_ab,T_ac)=a\mathcal B_\zeta(b,c).
\tag{PRS6.1}
\]
The restrictions intertwine this action with
\[
\rho_+(a)(h,c_0,c_1)=(h(\cdot/a),c_0,ac_1),\qquad
\rho_-(a)(h,d_0,d_1)=(a h(a\cdot),ad_0,d_1),
\]
and the retained corresponding actions on the extra copies. Consequently the product sheaf morphism is equivariant for the simultaneous dilation and target character \(a\); the global transpose has action \(a(T_{a^{-1}})'\). Substituting every original prime \(p\) retains all prime factors. Differentiation yields \(B_\zeta(Lx,y)+B_\zeta(x,Ly)=B_\zeta(x,y)\), where \(L=-u\partial_u\); this is an identity of the actual operators, not a choice of numerical weight on source \(\tau\).

The source comparison instead has receiving ring \(\mathbb Z^3\), source integer image \([n]=(n,0,0)\), and \([\tau]=(1,1,1)\). At the generic stalk only its first coordinate acts. The exact scalar balance is
\[
\mathcal B_\zeta(nb,c)=n\mathcal B_\zeta(b,c)=\mathcal B_\zeta(b,nc),\qquad
\mathcal B_\zeta(nb,nc)=n^2\mathcal B_\zeta(b,c).
\tag{PRS6.2}
\]
Thus a simultaneous source integer action is not silently replaced by the dilation character in (PRS6.1). On the full tensor sheaf the commuting scalar actions in the two factors remain independent. At every stalk each restriction respects the original scalar action, including zero integer action on the two extra copies. Primitive \(\tau\)'s supplied multiplicative image acts as identity; that does not identify it with integer one in the full coefficients.

## PRS7. Return to the full arithmetic source and its labels

DCP constructs the continuous map \(f:X^{\rm dbl}\to Y\), whose generic fibre is the complete \(U=\operatorname{Spec}\mathbb Z\), and whose other two fibres are \(m_+,m_-\). No arithmetic primes are removed from \(U\). Pulling (PRS2.1) back along \(f\times f\) gives an exact sheaf map
\[
(f\times f)^{-1}(\mathcal F\boxtimes\mathcal F)
\longrightarrow(f\times f)^{-1}\mathcal K.
\tag{PRS7.1}
\]
At \((x,y)\) its map is (PRS2.1) on the corresponding stalks \(\mathcal F_{f(x)}\otimes\mathcal F_{f(y)}\). Thus its value is the original bilinear form at every pair in \(U\times U\); outside that open at least one target stalk is zero. The pullback target identifies with extension by zero of the constant character line on \(U\times U\). To prove the identification, the restriction on that open is constant because \(f\times f\) is constant there. Extension-by-zero adjunction gives a map from that extension to the pullback; it is identity on each stalk in \(U\times U\), and both stalks are zero elsewhere. It is therefore a sheaf isomorphism. This proves the exact source return used here without assuming that all inverse-image or tensor functors commute with an unspecified duality.

All support labels can be retained through this new receiving operation. Explicitly let \(L\) be the established bounded support lattice and
\[
G_L(V)=\{(0,\lambda):\lambda\in L\}\cup\{(v,1_L):v\in V\}.
\]
For the two independent factors retain their ordered pair of labels. The map
\[
G_L(A)\times G_L(A)\longrightarrow G_{L\times L}(\mathbb C),\quad
((b,\lambda),(c,\mu))\longmapsto(\mathcal B_\zeta(b,c),(\lambda,\mu))
\tag{PRS7.2}
\]
is well defined. A non-top \(\lambda\) forces \(b=0\); a non-top \(\mu\) forces \(c=0\). In either case the output amplitude is zero, so it is allowed at the original ordered support. If both supports are top, any output amplitude is allowed. In particular a zero produced by the pairing retains \((\lambda,\mu)\). The map of each linear tensor stalk and every cochain restriction has the usual label-preserving lift. These are maps of the named receiving carriers, not an addition or a count of primitive \(\tau\).

## PRS8. What the construction says about numerical characters

The direct consequence of (PRS6.1) can be calculated without a weight assumption. For actual eigenvectors \(T_ax=a^\rho x\), \(T_ay=a^\sigma y\), a nonzero \(B_\zeta(x,y)\) forces
\[
a^{\rho+\sigma}=a\quad\text{for every }a>0,
\quad\text{hence}\quad\rho+\sigma=1.
\tag{PRS8.1}
\]
For the last implication put \(a=e^t\), differentiate at \(t=0\), and divide by the nonzero pairing. This calculation pairs the two characters; it is not an equality of either character with its complex conjugate. The original pairing is complex bilinear throughout.

For comparison with all retained jets, on the actual primary quotient at a zero \(\rho\) of order \(m\), the original action is
\[
p^{\rho+t}=p^\rho\sum_{j=0}^{m-1}\frac{(\log p)^j}{j!}t^j
\quad\text{in }\mathbb C[t]/(t^m),
\tag{PRS8.2}
\]
and the reflected factor has argument \(1-\rho-t\). Their product is exactly \(p\) in the full quotient, since the two finite exponential series multiply as the truncation of \(e^{t\log p}e^{-t\log p}=1\). No nilpotent or logarithm is dropped. The exact residue coefficient remains
\[
\operatorname{Res}_{s=\rho}\frac{F(s)G(1-s)}{\zeta(s)}
=\sum_{i+j+k=m-1}\frac{F^{(i)}(\rho)}{i!}
\frac{(-1)^jG^{(j)}(1-\rho)}{j!}
\frac{(1/g)^{(k)}(0)}{k!},\qquad
\zeta(\rho+t)=t^m g(t).
\tag{PRS8.3}
\]
The finite sum follows by multiplying the three full Taylor series and taking the coefficient of \(t^{m-1}\). It is the original denominator, including its unit germ \(g\), not a replacement denominator.

The support radical result (PRS5.4) and the character identity (PRS8.1) are the exact new receiving conclusions. Neither asserts the numerical separation needed by Deligne's lifting proof. The next calculation prompted by the amended rule is the actual diagonal comparison: determine whether the just-constructed product trace returns along the diagonal in a degree and with maps that can produce that separation. That calculation is carried out independently in the accompanying product/diagonal derivation; it cannot be replaced by calling the diagonal a closed immersion without checking the original topology.

## PRS9. Verification and limits of use

All nine stalk compatibilities, the two ordered Čech differentials, the factor-four unshifted return, the exact global currying, both support radicals, every real/prime dilation, source scalar balance and arithmetic pullback have been constructed above. The finite exact checks accompanying this proof test signs and boundary terms; the proof uses the full original spaces. The complete original cone and its nonzero global dual remainder from SCT, RPC and FPO remain present after (PRS4.2). This result supplies a geometric product origin for the existing global map. It supplies no assertion that primitive \(Z_1/\tau\) carries a numerical weight and no RH conclusion.

### The derived diagonal operation restores the original trace

The next calculation is completed in DIAGONAL_EXTRAORDINARY_RETURN.md. Define q:Y^2→Y by q(c+,c+)=c+, q(c-,c-)=c-, and send the other seven points to eta. Its inverse images of the three minimal opens are computed explicitly. The stalk identity Delta_*=q^{-1}, including all restrictions, proves that the derived right adjoint of Delta_* is Rq_*. It is not ordinary diagonal pullback.

For K=j_(eta,eta)!chi C, the full injective complex has terms I_eta, I_eta^4, and I_+ direct-sum I_eta^2 direct-sum I_- in degrees0,1,2. All signs and contractions are retained in the proof. Its cohomology is j_eta!chi C[-1], and derived global sections recover the original chi C[-2] trace with coefficient +1. Thus the degree loss under ordinary pullback is not a general obstruction to a diagonal-derived realization. This follows by the constructed right adjoint, not by an assumed closed immersion or a numerical purity statement. The full global identity RΓ Rq_*=RΓ also retains every other original cohomological degree.

### Full arithmetic correspondence and its derived coefficient return

DERIVED_RETURN_FULL_SOURCE_CORRESPONDENCE.md, FSC0–FSC6, returns the receiving construction to the entire original arithmetic source. FSC2 rules out precisely a continuous single-valued lift of q that fixes the complete arithmetic diagonal. FSC3 immediately constructs the full alternative Z={(x,y,z):fz=q(fx,fy)}, with projections a,b and lifted diagonal x↦(x,x,x). Each nonexceptional a-fibre is the whole Spec Z; the two equal closed-corner fibres are singletons.

FSC6 proves the actual canonical derived comparison Ra_*b^{-1}f^{-1}G ≅ (f×f)^{-1}Delta_*G for bounded complexes of algebraic sheaves of complex vector spaces on Y. It computes the inverse images of all three receiving injectives, their exact direct images, and a functorial injective resolution; no general proper-base-change theorem is assumed. The comparison applies to the full derived input and trace target from DER and to their morphism. Every arithmetic point remains in the correspondence. The coefficient comparison does not assign a numerical weight to primitive Z_1/tau or settle the active numerical weight-separation target.

### The degree-one mixed obstruction has an explicit global equivariant contraction

GLOBAL_MIXED_RETURN_CONTRACTION.md, GMC0–GMC7, follows the generic mixed row into its complete global sheaf complex. The actual section s_+(j)=(Sigma^{-1}j,0,0) is continuous and dilation equivariant, using the already proved summation inverse. It gives S(m_1,m_2)=(-(s_+ tensor1)m_1,(1 tensor s_+)m_2,0,0), with d_M S=id. The exact global cochain map is (id-Sd_M,vartheta), onto K_0 in degree0 and Q tensor Q in degree1, with zero differential. Its entire kernel is [S(M)→iota(M)], contracted by h(iota m)=Sm. Every original prime action intertwines.

Thus the degree-one mixed obstruction is killed by the constructed contraction of ker(F)=[S(M)→iota(M)]. The full mixed subsheaf retains RΓ(Y,N)≃K_0[0], with K_0=(H tensor Q) direct-sum (Q tensor H); it is not asserted to be acyclic. The generic polynomial representative P(L_total)z=iota m becomes the exact global boundary d(Sm). All original endpoint and extra copies remain in K_0=(H tensor Q) direct-sum (Q tensor H); the original residue trace factors through the computed map with coefficient +1. This is a theorem in the specified algebraic tensor/sheaf calculation, with no assumption of completed-tensor cohomology, mirror equivariance of the plus-only section, or numerical purity. The remaining Q operators and all primary nilpotents are retained explicitly in GMC6.3.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
