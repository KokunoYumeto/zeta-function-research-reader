# Weight-separated lifting with every original prime jet retained

24 September 2026. Independent finite-dimensional derivation for the expressly constructed receiving object of MJ4–MJ5. This document proves existence and uniqueness of an equivariant lift, gives the complete correction operator, extends it to all primary blocks, classifies tensor resonances, and carries every map through the complete support-labelled carrier. It does not assert that the auxiliary receiving object is the user's primitive \(Z_1\), or that it is already the full geometric specialization required by the research programme.

## WL0. Definitions consulted before operations

The controlling user record is USER_DEFINITIONS_VERBATIM.md (private construction record; not included), U01–U18, read in full before this derivation. The accompanying [SOURCE_OPERATIONS_AND_PROOFS.md](../foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md), B1–B5 and P1–P5, was also read in full.

The following restrictions are retained throughout.

* U01–U02: \(Z_1/\tau\) is presence without \(Z_2\) parity; source zero also has no parity. No map in this document assigns either source element a parity.
* U03–U04: no copies of primitive \(\tau\) are counted and no source sum \(\tau+\tau\) is introduced. The retracted law is not used.
* U06 and U10–U12: the source origin is not replaced by a numerical midpoint, a zero vector, or a coordinate extracted from integer arithmetic.
* U08, U11 and U18: existing arithmetic data are retained where they have been constructed; consequences are proved rather than added as source definitions.
* U15–U16: a statement about an auxiliary receiving operator is not a counterexample to the user's source definitions.

The input to the calculation is the already named complex Mellin-jet receiver of [the monodromy comparison](../deligne_quotient_weight_20260924/MONODROMY_JET_COMPARISON.md), MJ1 and MJ4–MJ5. The actual original-zeta map into this receiver is retained in [the integral-history proof](../integrality_purity_20260924/INTEGRAL_HISTORY_AND_PURITY.md), IH2–IH3, and is reproduced with its full Mellin factor in [the main lifting proof](TAU_LIFTING_AND_WEIGHT_SEPARATION.md), TL0. Its complex coefficient field and its spectral parameter are inputs from that receiver. They are not generated here from presence alone. Every addition, subtraction, exponential, tensor product, and inverse below has a stated domain in those existing receiving vector spaces. Section WL9 constructs the corresponding maps with arbitrary bounded distributive support labels; it does not declare a label-zero to be primitive \(\tau\).

The comparison with Pierre Deligne is the explicitly specified Frobenius-monodromy relation
\[
 F_aN F_a^{-1}=a^{-1}N.
\tag{WL0.1}
\]
For geometric Frobenius at a finite residue field this is the coordinate form of the Tate-twisted map in *La conjecture de Weil. II*, §1.7.2–§1.7.3. The authoritative publication is [Deligne, Publications Mathématiques de l'IHÉS 52 (1980), 137–252](https://www.numdam.org/item/PMIHES_1980__52__137_0/), DOI 10.1007/BF02684780. This independent calculation proves every operator assertion it uses and does not certify the earlier local transcription or claim a reading of the entire original article. The comparison with Connes–Consani must retain the original Mellin receiver and its source citations; no identification of the auxiliary object below with their full arithmetic geometry is asserted.

## WL1. The entire receiving object and all its actions

Let \(\rho\) be any specified complex spectral parameter and \(m\geq1\) its specified positive integer jet length. For an actual nontrivial zero of the original \(\zeta\), \(m\) is its original multiplicity. Define, as receiving complex algebras,
\[
 A_\rho=\mathbb C[t]/(t^m),\qquad
 B_\rho=\mathbb C[x,y]/(x,y)^m.
\tag{WL1.1}
\]
The quotient ideal \((x,y)^m\) contains exactly the monomials of total degree at least \(m\). Thus the classes \(x^iy^j\), \(i,j\geq0,\ i+j<m\), form a basis of \(B_\rho\). In particular
\[
 B_\rho=\bigoplus_{j=0}^{m-1}B_{\rho,j},\qquad
 B_{\rho,j}=y^j\mathbb C[x]/x^{m-j}.
\tag{WL1.2}
\]
Write \(T=M_t\), \(X=M_x\), and \(N=M_y\). Their products and nilpotence follow by multiplying the displayed monomials. For every positive real \(a\), using its real logarithm, define
\[
 \begin{aligned}
 W_{\rho,a}&=a^\rho\exp((\log a)T),\\
 D_a(x)&=x,\qquad D_a(y)=a^{-1}y,\\
 F_{\rho,a}&=M_{a^\rho\exp((\log a)x)}D_a.
 \end{aligned}
\tag{WL1.3}
\]
The exponentials are finite sums: their \(r\)-th terms vanish once \(r\geq m\). Substitution by \(D_a\) preserves \((x,y)^m\) and has inverse \(D_{a^{-1}}\), so it is well-defined. Since \(D_a\) fixes \(x\),
\[
 F_{\rho,a}F_{\rho,b}=F_{\rho,ab},\qquad
 W_{\rho,a}W_{\rho,b}=W_{\rho,ab}.
\tag{WL1.4}
\]
These equations follow by multiplying the finite exponential sums and using the binomial identity for the coefficient of each power. They include the inverses at \(a^{-1}\). Monomial evaluation also gives
\[
 F_{\rho,a}X=XF_{\rho,a},\qquad
 F_{\rho,a}NF_{\rho,a}^{-1}=a^{-1}N.
\tag{WL1.5}
\]
The restriction of \(F_{\rho,a}\) to \(B_{\rho,j}\) is exactly
\[
 a^{\rho-j}\exp((\log a)X_j),\qquad X_j=M_x\text{ on }\mathbb C[x]/x^{m-j}.
\tag{WL1.6}
\]
Thus no original exponential or jet coefficient has been discarded.

## WL2. An equivariant quotient and a complete lift

The following are well-defined algebra maps:
\[
 q_\rho:B_\rho\longrightarrow A_\rho,\quad x\longmapsto t,\quad y\longmapsto0,
 \qquad
 i_\rho:A_\rho\longrightarrow B_\rho,\quad t\longmapsto x.
\tag{WL2.1}
\]
Every total-degree-\(m\) monomial maps to zero under \(q_\rho\); \(x^m=0\) establishes the relation needed for \(i_\rho\). Their composition is \(q_\rho i_\rho=\mathrm{id}\). The basis of WL1 gives
\[
 \ker q_\rho=K_\rho=yB_\rho
 =\bigoplus_{j=1}^{m-1}B_{\rho,j},\qquad
 B_\rho=i_\rho A_\rho\oplus K_\rho.
\tag{WL2.2}
\]
Indeed \(q_\rho\) kills precisely the positive-\(y\)-degree basis vectors and sends the remaining basis bijectively to \(1,t,\ldots,t^{m-1}\).

Direct substitution, with the whole exponential retained, proves
\[
 \begin{aligned}
 q_\rho F_{\rho,a}&=W_{\rho,a}q_\rho,&
 F_{\rho,a}i_\rho&=i_\rho W_{\rho,a},\\
 q_\rho X&=Tq_\rho,&Xi_\rho&=i_\rho T.
 \end{aligned}
\tag{WL2.3}
\]
Consequently every original spectral jet lifts: \(t^r\) lifts to \(x^r\), with its original coefficient and its original prime action, for \(0\leq r<m\). This is an actual completed construction, including the case \(m=1\), when \(K_\rho=0\).

Uniqueness, rather than merely this displayed existence, is a consequence of the following weight calculation.

## WL3. The weight of every correction and the inverse that kills the defect

For \(1\leq j<m\), put \(n=m-j\) and
\[
 H_j=\operatorname{Hom}_{\mathbb C}(A_\rho,B_{\rho,j}).
\]
These are linear maps between the receiving spaces already constructed. Define
\[
 \mathscr L_j(h)=X_jh-hT,\qquad
 \mathscr C_{a,j}(h)=F_{\rho,a}|_{B_{\rho,j}}\,h\,W_{\rho,a}^{-1}.
\tag{WL3.1}
\]
Left multiplication by \(X_j\) and right multiplication by \(T\) commute as operators on \(H_j\). Their \(n\)-th and \(m\)-th powers vanish. Expanding the binomial therefore gives
\[
 \mathscr L_j^{\,n+m-1}=0.
\tag{WL3.2}
\]
For a term in that power to survive, its left exponent would need to be at most \(n-1\) and its right exponent at most \(m-1\); their sum would then be at most \(n+m-2\), a contradiction.

Multiplication of the finite sums in WL1 now proves the complete formula
\[
 \mathscr C_{a,j}
 =a^{-j}\exp((\log a)\mathscr L_j).
\tag{WL3.3}
\]
In particular its only eigenvalue is \(a^{-j}\). At a prime \(p>1\), its absolute value is \(p^{-j}<1\), and the associated numerical Frobenius weight, meaning \(2\log|\cdot|/\log p\), is \(-2j\). The original \(p^\rho\) factors canceled in this *Hom action* because they occur both in domain and codomain; neither original prime action was replaced or omitted.

Here is a finite exact inverse. Set
\[
 d=n+m-1,\quad E_{p,j}=\exp((\log p)\mathscr L_j),\quad
 U_{p,j}=E_{p,j}-I,\quad c_{p,j}=p^{-j}-1.
\]
The constant \(c_{p,j}\) is nonzero. Since \(U_{p,j}\) is \(\mathscr L_j\) times a polynomial, \(U_{p,j}^{\,d}=0\). Therefore
\[
 \boxed{
 (\mathscr C_{p,j}-I)^{-1}
 =
 \sum_{r=0}^{d-1}
 \frac{(-p^{-j})^r}{(p^{-j}-1)^{r+1}}U_{p,j}^{\,r}.
 }
\tag{WL3.4}
\]
To check the inverse, multiply the finite sum by \(c_{p,j}I+p^{-j}U_{p,j}\). The constant term is \(I\); every intermediate power cancels between the two adjacent terms; the final power is a multiple of \(U_{p,j}^{\,d}=0\). The same multiplication on the other side proves a two-sided inverse.

For an arbitrary receiving vector-space section \(s:A_\rho\to B_\rho\), define its exact prime defect
\[
 d_p(s)=F_{\rho,p}s-sW_{\rho,p}.
\tag{WL3.5}
\]
Its image lies in \(K_\rho\): application of \(q_\rho\) and WL2.3 gives \(W_{\rho,p}-W_{\rho,p}=0\). Let \(d_{p,j}(s)\) be its \(B_{\rho,j}\)-component. Then set
\[
 h_j=(\mathscr C_{p,j}-I)^{-1}
 \bigl(d_{p,j}(s)W_{\rho,p}^{-1}\bigr),\qquad
 s^\sharp=s-\sum_{j=1}^{m-1}h_j.
\tag{WL3.6}
\]
All terms are now constructed, including the inverse and its domain. The subtracted maps take values in \(K_\rho\), so \(q_\rho s^\sharp=\mathrm{id}\). Also
\[
 F_{\rho,p}h_j-h_jW_{\rho,p}
 =(\mathscr C_{p,j}-I)(h_j)W_{\rho,p}
 =d_{p,j}(s).
\]
Summing proves \(F_{\rho,p}s^\sharp=s^\sharp W_{\rho,p}\).

If \(s_1,s_2\) are two \(p\)-equivariant sections, their difference is a map \(A_\rho\to K_\rho\) fixed by \(\mathscr C_p\). The inverse WL3.4 forces each component to be zero. Hence the equivariant section is unique. Since \(i_\rho\) is one such section, the explicit correction always gives
\[
 \boxed{s^\sharp=i_\rho.}
\tag{WL3.7}
\]
It follows at once from WL2.3 that this corrected section is equivariant for every positive \(a\), not just for the prime used to compute it, and that it preserves the complete original spectral nilpotent \(T\).

No simplicity assumption on the original zero has been made.

## WL4. The lifting obstruction as a cocycle, with its vanishing proved

The preceding formula can be written independently of the initial choice of section. Let
\[
 H=\operatorname{Hom}_{\mathbb C}(A_\rho,K_\rho),\qquad
 \mathscr C_a(h)=F_{\rho,a}|_{K_\rho}hW_{\rho,a}^{-1}.
\]
The group \(G=\mathbb R_{>0}\), with multiplication, acts on \(H\) because of WL1.4. The same calculation applies to its subgroup \(\mathbb Q_{>0}\).

A degree-one cocycle here means exactly a function \(c:G\to H\) obeying
\[
 c(ab)=c(a)+\mathscr C_a c(b).
\tag{WL4.1}
\]
No topology or continuity is assumed. Commutativity of \(G\) gives
\[
 (\mathscr C_p-I)c(a)=(\mathscr C_a-I)c(p).
\tag{WL4.2}
\]
All \(\mathscr C_a\) commute, and therefore commute with the explicit inverse of \(\mathscr C_p-I\). With
\[
 h=(\mathscr C_p-I)^{-1}c(p)
\]
equation WL4.2 implies, for every \(a\),
\[
 c(a)=(\mathscr C_a-I)h.
\tag{WL4.3}
\]
This proves that every cocycle is a coboundary. It also proves that the correcting \(h\) is unique, since the common invariant subspace is zero by WL3.4. Thus both the invariants and the degree-one obstruction group vanish, in their explicit meanings just given.

For the arbitrary section \(s\), the function
\[
 c_s(a)=F_{\rho,a}sW_{\rho,a}^{-1}-s
\tag{WL4.4}
\]
has values in \(H\). Expanding \(F_{\rho,ab}sW_{\rho,ab}^{-1}-s\) proves WL4.1. Hence WL4.3 is precisely the correction in WL3, not an unrelated vanishing theorem.

The classes being lifted retain the exponent \(\rho\); the corrections have *relative* exponents \(-1,-2,\ldots,-(m-1)\). Their separation from exponent zero is the exact reason that the obstruction vanishes.

## WL5. Retractions, the previous return, and the additional monodromy requirement

Every equivariant linear retraction of \(i_\rho\) equals \(q_\rho\). To prove this, write any retraction \(r'\) as \(q_\rho+u\), with \(u i_\rho=0\). Thus \(u\) is determined by its restrictions \(B_{\rho,j}\to A_\rho\), \(j\geq1\). On each such Hom space, conjugation is
\[
 h\longmapsto W_{\rho,a}h(F_{\rho,a}|_{B_{\rho,j}})^{-1}
 =a^j\exp((\log a)(Th-hX_j)).
\tag{WL5.1}
\]
The exponent in parentheses is nilpotent by the same binomial argument. At \(a=p>1\), the only eigenvalue is \(p^j\ne1\). Therefore an equivariant \(u\) is zero.

More generally, every all-prime equivariant map \(B_\rho\to A_\rho\) is
\[
 M_{g(t)}q_\rho,\qquad g(t)\in\mathbb C[t]/t^m.
\tag{WL5.2}
\]
The positive-\(y\) components vanish by WL5.1. On the \(j=0\) block, commuting with \(W_{\rho,p}\) is equivalent to commuting with \(T\), because
\[
 (\log p)T=\log(p^{-\rho}W_{\rho,p})
 =\sum_{r=1}^{m-1}\frac{(-1)^{r+1}}r
 (p^{-\rho}W_{\rho,p}-I)^r.
\tag{WL5.3}
\]
The finite logarithm identity follows by composing the formal power series modulo \(t^m\). A map commuting with \(T\) is determined by its value \(g(t)\) at 1 and sends \(t^r\) to \(t^rg(t)\); hence it is multiplication by \(g\). The retraction condition forces \(g=1\).

The previous return \(r:B_\rho\to A_\rho\), \(x\mapsto t,\ y\mapsto t\), is still a well-defined algebra map. Its exact difference from the equivariant retraction is
\[
 (r-q_\rho)\left(\sum_{i+j<m}b_{ij}x^iy^j\right)
 =\sum_{\substack{i+j<m\\j\geq1}}b_{ij}t^{i+j}.
\tag{WL5.4}
\]
It preserves both \(X\) and \(N\) as \(T\), while its Frobenius defect is
\[
 (rF_{\rho,a}-W_{\rho,a}r)(b)
 =
 a^\rho e^{(\log a)t}
 \sum_{i+j<m}(a^{-j}-1)b_{ij}t^{i+j}.
\tag{WL5.5}
\]
This is the previously computed defect with no factors suppressed. Replacing \(r\) by the proved equivariant \(q_\rho\) changes \(rN=Tr\) into \(q_\rho N=0\); it does not pretend to retain that additional identification.

This last distinction has a complete calculation. The quotient operator induced by \(N\) is \(N_A=0\), since \(q_\rho N=0\). For \(m>1\), there is no section intertwining this \(N_A\) with \(N\). Indeed
\[
 \ker N=\operatorname{span}\{x^iy^j:i+j=m-1\},
 \qquad
 q_\rho(\ker N)=\mathbb C t^{m-1}.
\tag{WL5.6}
\]
Multiplication by \(y\) sends the monomials of degree at most \(m-2\) to distinct nonzero monomials, proving the kernel formula. Its displayed image is a proper subspace of \(A_\rho\) when \(m>1\). A section with \(Ns=0\) would take all of \(A_\rho\) into this kernel and would have image under \(q_\rho\) at most that one-dimensional subspace, contradicting \(q_\rho s=\mathrm{id}\). In particular \(Ni_\rho(1)=y\ne0\).

This is a statement about the three explicitly constructed receiving operators, after consulting U01, U04 and U12. It is not an obstruction assigned to primitive \(Z_1/\tau\). The weight-separated lift proved above retains Frobenius and the **original spectral nilpotent** \(T\). Requiring it also to identify the **additional monodromy nilpotent** with a prescribed operator is a different, explicitly calculated map condition.

## WL6. All original zero blocks together

Let \(\mathcal R\) be a set of specified distinct spectral parameters satisfying
\[
 0<\operatorname{Re}\rho<1,
\]
with each original multiplicity \(m_\rho\geq1\). Define the algebraic direct sums
\[
 A=\bigoplus_{\rho\in\mathcal R}A_\rho,\quad
 B=\bigoplus_{\rho\in\mathcal R}B_\rho,\quad
 K=\bigoplus_{\rho\in\mathcal R}K_\rho,
\tag{WL6.1}
\]
with the direct-sum maps \(q,i,W_a,F_a\). The set may be infinite; every individual vector has finite support. This is an algebraic receiver, not an unproved identification of its completion with the full analytic quotient.

For a map \(h:A_\sigma\to B_{\rho,j}\), \(j\geq1\), the complete conjugation formula is
\[
 \mathscr C_a(h)
 =a^{\rho-\sigma-j}
 \exp((\log a)\mathscr L)(h),
 \quad
 \mathscr L(h)=X_{\rho,j}h-hT_\sigma.
\tag{WL6.2}
\]
Its nilpotence exponent is at most
\[
 (m_\rho-j)+m_\sigma-1.
\tag{WL6.3}
\]
Because both parameters lie in the open strip,
\[
 \operatorname{Re}(\rho-\sigma-j)
 <1-j\leq0.
\tag{WL6.4}
\]
The inequality is strict, including \(j=1\). Hence for every prime \(p\), the only eigenvalue of \(\mathscr C_p\) has modulus strictly less than 1. Formula WL3.4 applies with \(p^{-j}\) replaced by \(p^{\rho-\sigma-j}\). It is therefore invertible on every such block.

This proves uniqueness of the section \(i:A\to B\), even allowing sections that mix different original zeros. It also gives the correction of every linear section by the formula of WL3 on all its component maps. For an infinite algebraic direct sum the formula is still well-defined: the image of the finite-dimensional space \(A_\sigma\) under a given section uses only finitely many target blocks; the correction acts inside those same blocks. No infinite sum of new target coordinates is created.

Every equivariant retraction \(B\to A\) likewise equals \(q\). The positive-\(y\) components vanish because their reverse Hom exponents have strictly positive real part.

For completeness, at \(j=0\) all-prime intertwiners between distinct original parameters vanish. Nonzero intertwining requires simultaneously
\[
 2^{\rho-\sigma}=1,\qquad3^{\rho-\sigma}=1.
\tag{WL6.5}
\]
The first equation forces \(\operatorname{Re}(\rho-\sigma)=0\). Writing \(\rho-\sigma=i u\), the two equations give \(u\log2=2\pi k\) and \(u\log3=2\pi l\), \(k,l\in\mathbb Z\). If \(u\ne0\), both integers are nonzero and \(\log2/\log3=k/l\), hence \(2^l=3^k\), which is impossible by unique factorization, including after clearing negative exponents. Thus \(u=0\) and \(\rho=\sigma\).

On a repeated parameter the same finite logarithm argument as WL5 gives exactly the \(\mathbb C[t]\)-module intertwiners. For the single original primary block of multiplicity \(m_\rho\), every endomorphism is multiplication by its uniquely determined \(g_\rho(t)\). Thus the preceding statements classify the maps rather than relying only on eigenvalue intuition.

### WL6a. Complete product receivers and continuity

There is also a simultaneous lift on the complete product observations, not only on the algebraic direct sum. Give
\[
 \mathbf A=\prod_{\rho\in\mathcal R}A_\rho,\qquad
 \mathbf B=\prod_{\rho\in\mathcal R}B_\rho,\qquad
 \mathbf K=\prod_{\rho\in\mathcal R}K_\rho
\]
their product topologies. The coordinatewise \(F_a,W_a,\mathbf q,\mathbf i\) are continuous: each output coordinate is a continuous map of the corresponding finite-dimensional input. The identity \(\mathbf q\mathbf i=\mathrm{id}\), equivariance, and \(\ker\mathbf q=\mathbf K\) all follow coordinate by coordinate.

Every continuous linear map from \(\mathbf A\) to a finite-dimensional receiving space \(V\) depends on finitely many input coordinates. Indeed choose a bounded neighbourhood \(U\) of zero in \(V\). Continuity supplies a product neighbourhood whose restrictions involve only finitely many input coordinates. The subspace on which those restricted coordinates vanish is contained in that neighbourhood and remains there under every complex scalar. Its image must therefore be zero: a nonzero image vector has unbounded scalar multiples, contradicting containment in \(U\). The map consequently factors through the finite product of the restricted coordinates.

Apply this to each coordinate of a continuous map \(\mathbf A\to\mathbf K\). Each output is a finite sum of the cross-block Hom maps of WL6. Their conjugation operators minus the identity are invertible by WL6.2–WL6.4. The inverse acts within the same finite set of input coordinates, so it again defines a continuous map to that output. These inverses for all outputs yield a well-defined continuous inverse on the space of continuous linear maps \(\mathbf A\to\mathbf K\), in the exact sense needed by the correction formula. Thus every continuous linear section of \(\mathbf q\) is corrected uniquely to \(\mathbf i\), which retains all original jets and all prime actions.

Let the already constructed actual observation map be \(\mathbf j:Q\to\mathbf A\), with components the original Mellin jets \(j_\rho\). Then
\[
 Q\xrightarrow{\mathbf j}\mathbf A
 \xrightarrow{\mathbf i}\mathbf B,\qquad
 \mathbf q\mathbf i\mathbf j=\mathbf j
\]
is the complete simultaneous lift of those observations. A map into a product is continuous precisely when each component is continuous, so the established continuity of the individual jets gives the continuity of this composite. The statement does not assert that \(\mathbf j\) is an isomorphism, onto, or injective. Its original kernel is unchanged.

## WL7. Tensor products retaining the original tuple

Fix a finite ordered tuple \(\boldsymbol\rho=(\rho_1,\ldots,\rho_d)\), with original lengths \(m_1,\ldots,m_d\). Define
\[
 A_{\boldsymbol\rho}=\bigotimes_{\nu=1}^d A_{\rho_\nu},
 \quad
 B_{\boldsymbol\rho}=\bigotimes_{\nu=1}^d B_{\rho_\nu},
 \quad
 q_{\boldsymbol\rho}=\bigotimes_\nu q_{\rho_\nu},
 \quad
 i_{\boldsymbol\rho}=\bigotimes_\nu i_{\rho_\nu}.
\tag{WL7.1}
\]
The bases are the tensor products of the bases in WL1, so the displayed maps are defined on every basis vector and satisfy \(q_{\boldsymbol\rho}i_{\boldsymbol\rho}=\mathrm{id}\).

Write \(\mathbf j=(j_1,\ldots,j_d)\), \(0\leq j_\nu<m_\nu\), \(J=\sum_\nu j_\nu\), and \(R=\sum_\nu\rho_\nu\). The exact decomposition is
\[
 B_{\boldsymbol\rho}
 =\bigoplus_{\mathbf j}
 \left(\bigotimes_{\nu=1}^d y_\nu^{j_\nu}
       \mathbb C[x_\nu]/x_\nu^{m_\nu-j_\nu}\right).
\tag{WL7.2}
\]
The kernel of \(q_{\boldsymbol\rho}\) consists of exactly the summands with \(J\geq1\); the \(\mathbf j=0\) summand is the entire image of \(i_{\boldsymbol\rho}\). On the \(\mathbf j\)-summand the operator is
\[
 a^{R-J}\exp\left((\log a)\sum_{\nu=1}^dX_\nu\right),
\tag{WL7.3}
\]
whereas the original tensor block has
\[
 a^R\exp\left((\log a)\sum_{\nu=1}^dT_\nu\right).
\tag{WL7.4}
\]
The nilpotence exponent of \(\sum X_\nu\) is at most
\[
 1+\sum_\nu(m_\nu-j_\nu-1),
\]
because every surviving monomial has total degree at most the sum in parentheses. The corresponding exponent of \(\sum T_\nu\) is at most \(1+\sum_\nu(m_\nu-1)\).

Thus on the Hom space from the original tensor block to a kernel summand, conjugation is
\[
 a^{-J}\exp((\log a)\mathscr L),
\quad
 \mathscr L(h)=\left(\sum X_\nu\right)h-h\left(\sum T_\nu\right),
\tag{WL7.5}
\]
with nilpotence exponent at most
\[
 1+2\sum_\nu(m_\nu-1)-J.
\tag{WL7.6}
\]
Since \(J\geq1\), the explicit inverse and cocycle argument of WL3–WL4 apply. Consequently \(i_{\boldsymbol\rho}\) is the unique equivariant section for this retained tuple, and \(q_{\boldsymbol\rho}\) the unique equivariant retraction. The correction retains every original tensor basis coefficient and all the original nilpotent terms.

The tuple is not discarded in this result. The following section calculates exactly what happens when different tuples may mix.

## WL8. Complete resonance condition when tensor tuples mix

Take a source tuple \(\boldsymbol\sigma\) and a target tuple \(\boldsymbol\rho\), with their specified jet lengths, and a target kernel label \(\mathbf j\) with \(J\geq1\). Put
\[
 \Delta=\sum_\nu\rho_\nu-\sum_\mu\sigma_\mu-J.
\tag{WL8.1}
\]
The complete Hom conjugation is
\[
 \mathscr C_a=a^\Delta\exp((\log a)\mathscr L),
\quad
 \mathscr L(h)=X_{\mathrm{sum}}h-hT_{\mathrm{sum}}.
\tag{WL8.2}
\]
For a nonzero all-prime invariant, both \(2^\Delta=1\) and \(3^\Delta=1\) are necessary: an exponential of a nilpotent has the single eigenvalue 1. The proof of WL6.5 therefore forces
\[
 \boxed{\sum_\nu\rho_\nu-\sum_\mu\sigma_\mu=J.}
\tag{WL8.3}
\]
Conversely, when this equality holds, all-prime invariance is exactly
\[
 X_{\mathrm{sum}}h=hT_{\mathrm{sum}}.
\tag{WL8.4}
\]
Indeed the equation implies commutation with every finite exponential. In the other direction, invariance for \(a=2\) gives \((\exp((\log2)\mathscr L)-I)h=0\). The operator in parentheses equals \(\mathscr L\) times a polynomial in \(\mathscr L\) whose constant coefficient is \(\log2\ne0\). That polynomial is invertible by a finite geometric series, so \(\mathscr Lh=0\).

Equations WL8.3–WL8.4 give all the mixed-tuple maps. They are explicitly constructible. For bases \(t^{\mathbf u}\) in the source and \(x^{\mathbf v}y^{\mathbf j}\) in the target, write the matrix as \(h_{\mathbf v,\mathbf u}\). Equation WL8.4 is the finite, fully specified set of equalities
\[
 \sum_{\nu:v_\nu\geq1}h_{\mathbf v-\mathbf e_\nu,\mathbf u}
 =
 \sum_{\mu:u_\mu+1<m_{\sigma_\mu}}
 h_{\mathbf v,\mathbf u+\mathbf e_\mu},
\tag{WL8.5}
\]
with each row and column constrained by its stated monomial ranges. This contains every coefficient of the map; no spectrum-only approximation has replaced its nilpotents.

There is always a nonzero solution at a genuine resonance. Put \(n_\nu=m_{\rho_\nu}-j_\nu\), let
\[
 v_{\mathrm{top}}=
 \prod_\nu x_\nu^{n_\nu-1}y_\nu^{j_\nu},
\quad
 h(f)=f(0,\ldots,0)v_{\mathrm{top}}.
\tag{WL8.6}
\]
The target monomial is nonzero and is killed by \(X_{\mathrm{sum}}\); the source constant-coefficient functional kills \(T_{\mathrm{sum}}\). Hence WL8.4 holds and \(h\ne0\).

If a numerical dimension is required, it is also determined by the actual nilpotent operators without an added assumption. Choose Jordan chains for their finite nilpotent matrices. For a source chain of length \(r\) and a target chain of length \(s\), every intertwiner sends the first source vector to an arbitrary element of the target's kernel of its \(r\)-th power, then sends the successive vectors to the successive images of that element. This is necessary and sufficient by direct evaluation. The target kernel has basis its last \(\min(r,s)\) chain vectors. Thus this pair contributes exactly \(\min(r,s)\) dimensions. Summing over all chains gives the complete dimension. The chain lengths themselves are determined by the finite matrices in WL7: if \(b_\ell=\dim\ker X^\ell\), the number of chains of length exactly \(\ell\) is \(2b_\ell-b_{\ell-1}-b_{\ell+1}\), as is verified by checking one chain and adding. These are finite exact linear calculations on the displayed monomials.

For a direct sum of tensor tuples, every equivariant section of the direct-sum quotient is therefore
\[
 i+h,
\]
where the only nonzero components of \(h:A\to K\) lie on the resonance locus WL8.3 and satisfy WL8.5. The canonical section \(i\) always exists. It is unique precisely when there are no such nonzero components. The strip restriction alone excludes all resonances in WL6, but does not establish their exclusion between arbitrary tensor tuples. This statement neither asserts that actual zeta zeros realize such a resonance nor assumes that they do not.

For example, the formal equality
\[
 \rho+\bar\rho-\bigl((1-\rho)+(1-\bar\rho)\bigr)=4\operatorname{Re}\rho-2
\]
shows exactly which condition would be tested in this particular quartet of tuples; \(J=1\) would require \(\operatorname{Re}\rho=3/4\), and a nonzero target \(j_\nu\) also requires the corresponding original jet length to exceed 1. No actual zero or multiplicity satisfying these conditions has been claimed.

## WL9. Every support label is retained

Let \(L\) be an arbitrary bounded distributive lattice, with bottom \(0_L\), top \(1_L\), join and meet. For each receiving complex vector space \(V\), form exactly the carrier
\[
 G_L(V)=\{(0,\lambda):\lambda\in L\}
       \ \cup\ (V\times\{1_L\}).
\tag{WL9.1}
\]
The two occurrences of \((0,1_L)\) denote the same element. A nonzero amplitude occurs only with top support.

The operations used on this receiving carrier are specified, not presumed:
\[
 (v,\lambda)\oplus(w,\mu)=(v+w,\lambda\vee\mu),
\tag{WL9.2}
\]
and the receiving scalar action from \(G_L(\mathbb C)\) is
\[
 (c,\lambda)\cdot(v,\mu)=(cv,\lambda\wedge\mu).
\tag{WL9.3}
\]
Both are closed. In WL9.2 a nonzero output amplitude requires at least one nonzero input amplitude and therefore at least one top label, so its join is top. In WL9.3 a nonzero output requires both input amplitudes to be nonzero and hence both labels to be top. Associativity, commutativity of addition, the receiving scalar laws, and distributivity follow respectively from the already existing vector and scalar operations and the lattice identities. The bounded distributive lattice assumption provides each required meet-over-join or join-over-meet identity. These receiving operations do not define an addition on primitive \(Z_1/\tau\).

For every complex linear map \(f:V\to W\), define the common-label map
\[
 G_L(f)(v,\lambda)=(f(v),\lambda).
\tag{WL9.4}
\]
It is well-defined: if \(\lambda\ne1_L\), the input amplitude is zero and \(f(0)=0\); if \(\lambda=1_L\), every output amplitude is admitted. The formula gives
\[
 G_L(gf)=G_L(g)G_L(f),\qquad
 G_L(\mathrm{id})=\mathrm{id},
\tag{WL9.5}
\]
and preserves WL9.2–WL9.3 by linearity, leaving both join and meet coordinates untouched. An invertible receiving linear map has the inverse common-label map \(G_L(f^{-1})\).

In particular all the maps \(q,i,F_a,W_a,X,N\) of WL1–WL2 have such lifts, and every proved composition identity lifts exactly. Thus
\[
 G_L(q)G_L(i)=\mathrm{id},\qquad
 G_L(F_a)G_L(i)=G_L(i)G_L(W_a).
\tag{WL9.6}
\]
The full zero-label carrier is \(Z_L(V)=\{(0,\lambda):\lambda\in L\}\). It is preserved pointwise, not identified to one point:
\[
 G_L(f)(0,\lambda)=(0,\lambda).
\tag{WL9.7}
\]
The full inverse image of this zero-label carrier under \(G_L(q)\) is exactly
\[
 G_L(q)^{-1}(Z_L(A))=G_L(K).
\tag{WL9.8}
\]
This is the **amplitude kernel with all labels**, not a claim that the semimodule kernel at the bottom zero contains every supported zero. When \(0_L\ne1_L\), the inverse image of the single bottom element \((0,0_L)\) is just that bottom element. When \(L\) has one element, the usual vector kernel is recovered. These assertions follow directly from the unchanged label in WL9.4 and retain the possible degenerate lattice.

There is no erased support under the weight correction. If \(s\) is the section of WL3, its correction \(h\) and its defect \(d_p(s)\) are already constructed receiving linear maps. On any allowed input \((v,\lambda)\), the common-label difference is
\[
 G_L(s)(v,\lambda)\oplus G_L(-h)(v,\lambda)
 =(s(v)-h(v),\lambda\vee\lambda)
 =(i(v),\lambda).
\tag{WL9.9}
\]
If the amplitude of the corrected defect is zero, its exact value is \((0,\lambda)\), not \((0,0_L)\) unless that was already the input label. Similarly the inverse WL3.4 fixes each zero-label input when lifted by WL9.4. No scalar image of primitive \(\tau\) has been used.

For an explicit decomposition, let \(P=iq\) and \(C=\mathrm{id}_B-iq\), defined on the receiving vector space. Then \(P^2=P\), \(C^2=C\), \(PC=CP=0\), \(qC=0\), \(Ci=0\). On the labelled carrier,
\[
 G_L(P)(v,\lambda)\oplus G_L(C)(v,\lambda)=(v,\lambda),
\]
while the zero-amplitude composites \(G_L(PC)\), \(G_L(qC)\), and \(G_L(Ci)\) return \((0,\lambda)\). This proves the retained-label meaning of every vanishing used here.

All previous results, including direct sums and tensors, are lifted by applying this construction to the entire explicitly constructed receiving space. No distributive operation on primitive \(\tau\), no tau-to-scalar-one map, and no comparison that forgets a support label is inserted.

## WL10. A complete length-two calculation

For \(m=2\), retain the ordered bases \(1,t\) and \(1,x,y\). Put \(\alpha=a^\rho\) and \(\ell=\log a\). Then
\[
 W_{\rho,a}=\alpha
 \begin{pmatrix}1&0\\ \ell&1\end{pmatrix},\qquad
 F_{\rho,a}=\alpha
 \begin{pmatrix}1&0&0\\ \ell&1&0\\ 0&0&a^{-1}\end{pmatrix}.
\tag{WL10.1}
\]
Every vector-space section has exactly the form
\[
 s(1)=1+c\,y,\qquad s(t)=x+d\,y.
\]
Its full defect is
\[
 d_a(s)(1)=\alpha\bigl((a^{-1}-1)c-\ell d\bigr)y,
 \qquad
 d_a(s)(t)=\alpha(a^{-1}-1)d\,y.
\tag{WL10.2}
\]
At \(a>1\), the factor \(a^{-1}-1\) is nonzero. If the two displayed coefficients are written as \(\alpha u\) and \(\alpha v\), the correction coefficients are exactly
\[
 d=\frac{v}{a^{-1}-1},\qquad
 c=\frac{u+\ell\,v/(a^{-1}-1)}{a^{-1}-1}.
\tag{WL10.3}
\]
Subtracting the corresponding map to \(\mathbb Cy\) gives \(1\mapsto1,\ t\mapsto x\). This displays the whole correction including the coupling \(-\ell d\); there is no diagonal-only argument and no loss of the original nilpotent. Its support-labelled value is obtained by retaining the same \(\lambda\) in every line of WL10.

## WL11. The exact result and its use

For the actual original primary-jet action inside MJ4–MJ5, the quotient \(q_\rho:x\mapsto t,\ y\mapsto0\) has a unique all-prime equivariant section preserving every original jet. Every initially chosen receiving section is corrected to it by the explicit finite inverse WL3.4. The complete correction space has relative weights \(-2j\), so its invariants and degree-one lifting obstruction vanish by WL4. The result persists across all original zeros in the open strip, with all multiplicities, by WL6, and across each retained tensor tuple by WL7. Mixed tensor resonances are exactly WL8.3–WL8.5. Every map and every zero-amplitude conclusion preserves every label of an arbitrary bounded distributive \(L\), by WL9.

The original absolute spectral parameter \(\rho\) was unrestricted in WL1–WL5. Consequently this completed weight-separated lifting calculation holds equally for a hypothetical off-critical primary block. It proves a specific lifting result and does not by itself force \(\operatorname{Re}\rho=1/2\). That is a proved scope statement: the formula and its inverse contain no constraint on \(\operatorname{Re}\rho\). A claimed application to a different, full geometric specialization must exhibit its exact receiving maps; the present note does not silently substitute \(B_\rho\) for that object.

The source of the \(Z_1,Z_2,\tau\) distinctions remains the user corpus U01–U18. Deligne is credited for the geometric weight and monodromy framework; the finite two-variable receiver and the calculations WL1–WL11 are explicitly programme derivations. This file makes no publication claim, no original-author-source reading claim beyond those stated in WL0, and no claim to have proved or disproved RH.

## Current propagation from OMS — 24 September 2026

[The complete synthesis proof](ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), OMS1–OMS5, proves that the original summation image is closed and that the full actual-zero jet map on Q has zero common kernel. Its image remains a proper dense subspace of the unrestricted product, carrying the stronger original quotient topology. Earlier statements leaving those two questions undetermined are superseded by that proof, not by an assumption. Every original zero multiplicity and support label remains.

OMS7A proves the exact return to AC0–AC4: the same original spaces give I0=2 E(S)=E(S), with the factor 2 retained in the periodization map and inverse. Thus D_cl=0, C_alg→Q is the identity-induced topological isomorphism, and the specific global two-extension class of the actual adelic two-term complex is zero. Both endpoint contributions at each prime and the higher derived-coinvariant groups remain unchanged. No vanishing of the entire Ext group or full tau purity is inferred.

## Global adelic lifting propagation - 24 September 2026

The complete current proofs are GLOBAL_ADELIC_LIFTING_AND_PRIME_BOUNDARY.md GAP0–GAP9 (including GAP6A–GAP6B), COMPLETE_GENERATOR_ENDPOINT_RETURN.md GER0–GER7, GLOBAL_ENDPOINT_EXTENSION_RETURN.md GEX0–GEX9, and COMPLETE_COMPARISON_TRIANGLE_FORMALITY.md CTF0–CTF8. Every original prime wedge, endpoint pair and nilpotent jet is retained. GER credits the existing RZ endpoint resolvents and gives their explicit original Schwartz return and covariance corrections. GEX proves vanishing of the entire extension groups between the whole actual Q and the stated endpoint modules, in the explicitly constructed algebraic and strict locally convex operator categories. This strengthens the earlier finite-block and particular-extension assertions without assigning that theorem to a larger unspecified category.

GAP and CTF construct the full derived adelic complex, its canonical cohomology map, the exact original CC comparison and its entire cone. The faithful coefficient copies distinguish primitive tau from integer one in both objects. All additional cone contractions and the final-arrow homotopy are explicit; no test-space section Q→A is asserted. On the separate supported-Q row the same polynomial is invertible, rather than zero. Full tau numerical purity does not follow from endpoint separation and remains unproved.
