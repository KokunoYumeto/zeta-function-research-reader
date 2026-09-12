# Independent rank-two/exterior-trace audit

## Assignment and provenance

Public review scope: independent rank-two and exterior-trace proof review of the hash-pinned source, including quartet multiplicities, projector identities and endpoint conventions.

The archive SHA-256 was read independently and matches exactly:

168f977a9b54cf461f564e099fe55dc7b8feffbc09c563f541e0be2bb5746a94.

Read the applicable mathematical AGENTS instructions and the complete 30,446-byte RESEARCH_NOTE.md member through read-only .NET ZipFile/StreamReader. No archive script was executed. A read-only secondary mathematical auditor is independently checking the quartet combinatorics while this audit checks the rank-two operator and projections.

## Outcome and exact scope

The rank-two allowance, additive exterior estimate, determinant-line bound, projector identities, and slack formulas in sections 3, 4, 6 and 7 are correct. The quartet formula in section 8 is correct for the packet consisting exactly of that quartet. There is one substantive domain correction to make explicit: for a larger packet containing the quartet, its expression is a lower bound, not an equality for the whole packet's cyclic dimension, and the admissible source degree must use the whole packet's actual dimension. Endpoint conventions for the zero exterior degree should also be written explicitly wherever the displayed determinant/projector maps are used with no positive-defect block.

The exact RESEARCH_NOTE.md member SHA-256 is:

16c3e44879402dee9d8b2a7bc4be911fbfbb588978e01b418d0201cfdb5a970d.

This audit proves the bounded finite-dimensional and combinatorial claims below. The original analytic construction, source representative, cochain primitive, and source Gram identity are being audited separately by the parent; this document does not independently certify those inputs, does not infer an analytic upper bound, and makes no statement that an off-line zeta quartet exists.

## 1. Retained objects and parameter domains

Retain the note's fixed remainder-coordinate space

\[
C=\mathbb C[S]/(\chi),\qquad q=q_k=\deg\chi,\qquad A=M_S,
\]

its actual positive Hermitian matrix \(G=K^{-1}\), its monic polynomial remainder vectors \(b_j\), and its literal positive norm \(\omega_N\). The calculation applies for the note's nonempty packet, integer \(k\geq1\), and integer \(N\geq q-1\). In particular \(q\geq1\) and \(N\geq0\). Every adjoint below is in these original coordinates:

\[
T^{\sharp_G}=G^{-1}T^*G.
\]

The established source identity being used is

\[
W=A^*G+GA-kG
 =G\,\frac{b_{N+1}b_N^*+b_Nb_{N+1}^*}{\omega_N}\,G,
\qquad H=G^{-1}W.
\]

Reflection must mean the stated pairing
\(\lambda\longleftrightarrow k-\bar\lambda\) with the same full cyclic local length. The traceless conclusion needs that actual pairing (or independently the same real trace), not only a visually similar involution. No coordinate or mass normalization is used.

## 2. Rank-two spectrum and the literal epsilon formula

Put \(u=b_N\), \(v=b_{N+1}\), \(\omega=\omega_N>0\). Then

\[
H=\frac{vu^*G+uv^*G}{\omega}.
\]

Thus \({\rm im}\,H\subseteq{\rm span}\{u,v\}\), so \({\rm rank}\,H\leq2\).
Also \(GH=W=W^*=H^*G\), so \(H^{\sharp_G}=H\). Its metric eigenspaces are orthogonal, its eigenvalues are real, and it is diagonalizable; these are the ordinary finite-dimensional spectral theorem applied to the retained positive definite pairing.

The reflection pairing gives

\[
2\Re {\rm Tr}\,A=kq,\qquad
{\rm Tr}\,H=2\Re {\rm Tr}\,A-kq=0.
\]

A nonzero self-adjoint operator of rank at most two and trace zero has rank exactly two, with simple nonzero eigenvalues \(+\epsilon,-\epsilon\), where \(\epsilon>0\). A rank-one nonzero possibility is excluded by trace zero. If there are no nonzero eigenvalues, diagonalizability gives \(H=0\).

Define, exactly as in the note,

\[
a=u^*Gu,\qquad d=v^*Gv,\qquad c=u^*Gv.
\]

Taking the trace of the displayed rank-two formula yields

\[
0={\rm Tr}\,H=\frac{c+\bar c}{\omega},
\]

so \(c\) is purely imaginary. This identity follows from the actual traceless operator itself; no additional sign is necessary. Expanding all four terms of \(H^2\) gives

\[
{\rm Tr}(H^2)
=\frac{c^2+\bar c^{\,2}+2ad}{\omega^2}
=\frac{2(ad-|c|^2)}{\omega^2}.
\]

Consequently

\[
\epsilon=\frac{\sqrt{ad-|c|^2}}{\omega},\qquad
\epsilon^2=\frac{{\rm Tr}(H^2)}2.
\]

The radicand is nonnegative by the Cauchy--Schwarz inequality in the original \(G\)-pairing. These formulas include dependent or zero \(u,v\). In particular a vanishing radicand gives \(H=0\), not a nonzero nilpotent rank-two operator: self-adjointness rules out that alternative.

## 3. The additive exterior estimate and every exterior-degree endpoint

For \(1\leq p\leq q\), retain the unscaled increasing-index basis on \(\bigwedge^p C\), with

\[
G^{[p]}_{I,J}=\det G_{I,J}.
\]

For decomposable vectors \(x_1\wedge\cdots\wedge x_p\) and
\(y_1\wedge\cdots\wedge y_p\), the pairing is
\(\det(x_i^*Gy_j)_{i,j}\). Applying the determinant product rule separately to its rows and columns gives

\[
\bigl(A^{[p]}\bigr)^{\sharp_{G^{[p]}}}
 =\bigl(A^{\sharp_G}\bigr)^{[p]}.
\]

The operation \(T\mapsto T^{[p]}\) is linear, and
\((kI_C)^{[p]}=kpI_{\wedge^pC}\). It follows, in exactly the retained coordinates, that

\[
\bigl(A^{[p]}\bigr)^*G^{[p]}
 +G^{[p]}A^{[p]}-kpG^{[p]}
 =G^{[p]}H^{[p]}.
\]

If \(\epsilon>0\), write the metric orthogonal eigenspaces as
\(C=L_+\oplus Z_0\oplus L_-\), with dimensions \(1,q-2,1\) and eigenvalues
\(\epsilon,0,-\epsilon\). Their exterior direct-sum decomposition is

\[
\begin{split}
\bigwedge^p C={}&\bigwedge^p Z_0\\
&\oplus\left(L_+\wedge\bigwedge^{p-1}Z_0\right)
\oplus\left(L_-\wedge\bigwedge^{p-1}Z_0\right)\\
&\oplus\left(L_+\wedge L_-\wedge\bigwedge^{p-2}Z_0\right).
\end{split}
\]

Here an impossible exterior degree denotes the zero module. On the four summands \(H^{[p]}\) acts by \(0,\epsilon,-\epsilon,0\), respectively. The multiplicity of each nonzero eigenvalue is
\(\binom{q-2}{p-1}\). For \(1\leq p\leq q-1\), that binomial coefficient is positive, so both extrema are attained and

\[
-\epsilon G^{[p]}\preceq
\bigl(A^{[p]}\bigr)^*G^{[p]}+G^{[p]}A^{[p]}-kpG^{[p]}
\preceq\epsilon G^{[p]}
\]

has precisely the optimal allowance \(\epsilon\). There is no factor \(p\). At \(p=q\) the operator is scalar \({\rm Tr}\,H=0\), so the control is exactly zero, not merely bounded by \(\epsilon\). At \(\epsilon=0\), the same conclusion follows directly from \(H=0\) at every degree.

At \(p=0\), the complete convention is

\[
\bigwedge^0C=\mathbb C,\qquad G^{[0]}=(1),\qquad
A^{[0]}=H^{[0]}=0.
\]

Thus the control is exactly zero here too. At \(p>q\), the exterior module is zero. These cases should not be described as attaining an allowance \(\epsilon>0\).

The identity
\(\bigwedge^p(e^{tA})=e^{tA^{[p]}}\) follows by differentiating the multiplicative exterior map on each decomposable vector and using its value \(I\) at \(t=0\); both sides solve the same finite-dimensional matrix ODE. This uses the additive generator in the note, not the generally different multiplicative matrix \(\bigwedge^p A\).

## 4. Determinant of all positive cyclic generalized eigenspaces

Let

\[
C_>=\bigoplus_{\Re\lambda>k/2}C_\lambda,\qquad
C_\lambda=\ker(A-\lambda I)^{\ell_\lambda},\qquad
p=\dim C_>=\sum_{\Re\lambda>k/2}\ell_\lambda.
\]

These are the full generalized eigenspaces of the cyclic module \(C\). They are not asserted to be the entire generalized eigenspaces of the larger tensor algebra \(B_k\). Reflection pairs the positive and negative parts with equal dimensions. Hence \(p\leq\lfloor q/2\rfloor\); in particular \(0<p<q\) whenever the positive part is nonzero.

For any fixed unscaled basis \(e_1,\ldots,e_p\) of \(C_>\), put
\(v=e_1\wedge\cdots\wedge e_p\ne0\). In the expansion of \(A^{[p]}v\), an off-diagonal entry in the matrix of \(A|_{C_>}\) repeats one basis vector and hence gives zero. Its diagonal entries add, giving

\[
A^{[p]}v=\zeta_>v,\qquad
\zeta_>={\rm Tr}(A|_{C_>})
=\sum_{\Re\lambda>k/2}\ell_\lambda\lambda.
\]

This calculation retains every generalized vector before passing to the determinant. Nilpotent diagonal traces vanish; their full dimensions do not vanish.

Define

\[
L=2\Re\zeta_>-kp
=\sum_{\Re\lambda>k/2}\ell_\lambda(2\Re\lambda-k).
\]

For \(p>0\), inserting this actual eigenvector into the exterior control identity gives

\[
\frac{v^*\bigl((A^{[p]})^*G^{[p]}+G^{[p]}A^{[p]}-kpG^{[p]}\bigr)v}
{v^*G^{[p]}v}=L.
\]

The previous section bounds this quotient by \(\epsilon\), and every summand defining \(L\) is strictly positive. If \(p=0\), the sum is empty and \(L=0\). Thus

\[
0\leq L\leq\epsilon.
\]

The note's source norm \(R_p^*R_p=p!G^{[p]}\), once established by its source calculation, multiplies numerator and denominator by the identical literal \(p!\); no factor is lost or absorbed here.

Pairing the positive and negative terms also proves exactly

\[
L=\frac12\sum_\lambda\ell_\lambda|2\Re\lambda-k|
 =\sum_\lambda\ell_\lambda|\Re\lambda-k/2|.
\]

For a fixed basis column map \(B_>\) put \(G_>=B_>^*GB_>\), and let
\(A_>\) be the matrix of \(A|_{C_>}\) in that basis. For \(a>0\) and
\(U_>(a)=e^{(\log a)A_>}\),

\[
\det(U_>(a)^*G_>U_>(a))
=|\det U_>(a)|^2\det G_>
=a^{2\Re\zeta_>}\det G_>
=a^{kp+L}\det G_>.
\]

The equality \(\det e^T=e^{{\rm Tr}T}\) follows, for example, by triangularizing \(T\) and multiplying the diagonal exponential entries; it holds with all nilpotent blocks intact. For any nonzero exterior vector evolved by \(e^{tA^{[p]}}\), differentiating its squared norm gives logarithmic derivative between \(kp-\epsilon\) and \(kp+\epsilon\). Integrating for \(t=\log a\geq0\) proves the two source-volume bounds in section 6.2 with the same factor \(p!\). For \(0<a<1\), the inequalities reverse their endpoint order; the note correctly restricts the displayed order bound to \(a\geq1\).

## 5. CRT and metric projections, including the exact slack

For \(p>0\), retain the CRT idempotent \(Q=e_>(A)\), with range \(C_>\), and define

\[
P=B_>(B_>^*GB_>)^{-1}B_>^*G.
\]

The compressed Gram is positive definite because \(B_>\) is injective:
\(z^*B_>^*GB_>z=(B_>z)^*G(B_>z)>0\) for \(z\ne0\).
Direct multiplication gives \(P^2=P\), \(P^{\sharp_G}=P\), and
\(P B_>=B_>\). Thus \(P\) and \(Q\) have the same range and both restrict to its identity, although their kernels need not agree. Applying first one and then the other gives exactly the note's orientations

\[
QP=P,\qquad PQ=Q.
\]

Consequently

\[
(P-Q)^2=P^2-PQ-QP+Q^2=P-Q-P+Q=0.
\]

This is a square-zero difference, not a claim that the two projections coincide.

The range is \(A\)-invariant, so \((I-P)AP=0\) and \(PAP=AP\). Relative to the actual decomposition
\(C={\rm im}\,P\oplus\ker P\), the matrix of \(A\) is block upper triangular and the trace of \(PA\) is the trace of its first diagonal block. The same argument with \(Q\), or its commuting CRT form, proves

\[
{\rm Tr}(PA)={\rm Tr}(QA)=\zeta_>.
\]

Since trace commutes with adjoint conjugation and is cyclic,

\[
{\rm Tr}(PA^{\sharp_G})
={\rm Tr}(A^{\sharp_G}P)
={\rm Tr}((PA)^{\sharp_G})
=\overline{{\rm Tr}(PA)}.
\]

Also \({\rm Tr}\,P=p\). Therefore

\[
{\rm Tr}(PH)=2\Re\zeta_>-kp=L.
\]

No commutation \(PA=AP\) is assumed here. No inverse-compression formula
\((B_>^*GB_>)^{-1}=B_>^*G^{-1}B_>\) is used or generally available.

When \(\epsilon>0\), functional evaluation on the three eigenvalues of \(H\) proves that

\[
F_+=\frac{H^2+\epsilon H}{2\epsilon^2},\qquad
F_-=\frac{H^2-\epsilon H}{2\epsilon^2}
\]

are its rank-one metric orthogonal positive and negative projections, with
\(H=\epsilon(F_+-F_-)\). Taking the trace against \(P\) gives

\[
L=\epsilon\bigl({\rm Tr}(PF_+)-{\rm Tr}(PF_-)\bigr)
=\epsilon(1-\eta),
\]

\[
\eta=1-{\rm Tr}(PF_+)+{\rm Tr}(PF_-).
\]

For the retained metric Hilbert--Schmidt norm
\(\|T\|_{{\rm HS},G}^2={\rm Tr}(T^{\sharp_G}T)\), idempotence, self-adjointness and trace cyclicity give

\[
\begin{split}
\|(I-P)F_+\|_{{\rm HS},G}^2
&={\rm Tr}(F_+(I-P)F_+)\\
&=1-{\rm Tr}(PF_+),\\
\|PF_-\|_{{\rm HS},G}^2
&={\rm Tr}(F_-PF_-)
={\rm Tr}(PF_-).
\end{split}
\]

Thus the two terms in the stated slack are exactly nonnegative squared norms, not a discarded remainder. In this positive spectral application \(0\leq L\) further gives \(0\leq\eta\leq1\). The upper bound \(L=\epsilon\) is attained precisely when
\({\rm im}\,F_+\subseteq C_>\) and \({\rm im}\,F_-\subseteq C_>^{\perp_G}\).
If \(p=0\), set \(P=Q=0\); then \(L=0\) and \(\eta=1\) whenever \(\epsilon>0\). If \(\epsilon=0\), the displayed \(F_\pm\) expressions are undefined and must not be evaluated; the correct statement is directly \(H=0\) and \(L=0\).

The resolvent trace formula also retains full lengths. On a block
\(A_\lambda=\lambda I+N_\lambda\),

\[
(SI-A_\lambda)^{-1}
=\sum_{j=0}^{\ell_\lambda-1}
\frac{N_\lambda^j}{(S-\lambda)^{j+1}}.
\]

Each positive power of the nilpotent matrix has zero trace, so the block trace is \(\ell_\lambda/(S-\lambda)\). The residue of
\(S\,{\rm Tr}((SI-A)^{-1})\) around that block is therefore
\(\ell_\lambda\lambda\), exactly as required by the note's positively oriented contour.

## 6. Exact quartet grid, cyclic lengths, and parameter correction

For this subsection's equalities, specify the packet itself:

\[
h_Q(s)=\prod_{\varepsilon,\eta\in\{+1,-1\}}
\left(s-\left(\tfrac12+\varepsilon\delta+i\eta\gamma\right)\right)^m,
\quad
\delta>0,\quad\gamma>0,\quad m\in\mathbb Z_{\geq1}.
\]

Let \(k\in\mathbb Z_{\geq1}\). Counting the positive real and imaginary signs of an ordered \(k\)-tuple gives margins \(0\leq a,b\leq k\), and hence sum

\[
\lambda_{a,b}
=\frac k2+\delta(2a-k)+i\gamma(2b-k).
\]

Conversely the integer interval
\(\max(0,a+b-k)\leq t\leq\min(a,b)\) is nonempty because
\(a+b-k\leq a,b\) and \(0\leq a,b\). Its four occupation counts
\((t,a-t,b-t,k-a-b+t)\) are nonnegative and sum to \(k\), producing exactly those margins. Since \(\delta,\gamma\) are nonzero real numbers, the real and imaginary parts separately force equality of the two margins if two sums coincide. Thus there are exactly \((k+1)^2\) distinct sums.

On every ordered tuple's local tensor block retain

\[
T=\mathbb C[z_1,\ldots,z_k]/(z_1^m,\ldots,z_k^m),
\qquad M_S=\lambda+\mathcal N,\qquad
\mathcal N=M_{z_1+\cdots+z_k}.
\]

Every monomial of total degree greater than \(k(m-1)\) vanishes. The coefficient of the surviving top monomial
\(z_1^{m-1}\cdots z_k^{m-1}\) in
\((z_1+\cdots+z_k)^{k(m-1)}\) is the literal nonzero number

\[
\frac{(k(m-1))!}{((m-1)!)^k}.
\]

Hence \(\mathcal N\) has nilpotency index exactly
\(\ell_k=1+k(m-1)\) on each ordered block, including \(m=1\), where its zeroth power is the identity and its first power is zero. The minimal polynomial on the direct sum takes the maximum of these indices at each eigenvalue, which is still \(\ell_k\). Therefore

\[
\chi_{h_Q,k}(S)
=\prod_{a,b=0}^k(S-\lambda_{a,b})^{\ell_k},
\qquad q_{h_Q,k}=\ell_k(k+1)^2.
\]

This is the dimension of the cyclic algebra, not the dimension of the whole tensor algebra at a sum. In fact an ordered tuple is specified by independent subsets of positions bearing the positive real and imaginary signs. There are exactly
\(\binom ka\binom kb\) such tuples at \(\lambda_{a,b}\), and the full tensor generalized eigenspace there has dimension
\(\binom ka\binom kb\,m^k\). Its much larger dimension is not the exponent of the cyclic minimal polynomial. The note correctly uses \(\ell_k\).

Positive real defect means \(a>k/2\), so there are
\((k+1)\lceil k/2\rceil\) positive grid points. Thus

\[
p=\ell_k(k+1)\left\lceil\frac k2\right\rceil,
\qquad
L_{h_Q,k}
=2\delta\ell_k(k+1)
\sum_{a=\lfloor k/2\rfloor+1}^{k}(2a-k).
\]

For \(k=2n\), the last sum is \(2+4+\cdots+2n=n(n+1)\).
For \(k=2n+1\), it is \(1+3+\cdots+(2n+1)=(n+1)^2\).
Both equal \(\lfloor(k+1)^2/4\rfloor\). Consequently

\[
L_{h_Q,k}
=2\delta[1+k(m-1)](k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor
\leq\epsilon_{h_Q,k,N}^{\mathrm{cyc}},
\]

for the exact admissible range

\[
N\geq[1+k(m-1)](k+1)^2-1.
\]

The sum of imaginary parts is zero because
\(\sum_{b=0}^k(2b-k)=0\), including all positive-real columns and their common full lengths.

For \(m=1\) the displayed expression is
\(\delta k^3/2+O_h(k^2)\). For \(m>1\) it is
\(\delta(m-1)k^4/2+O_h(k^3)\).
The note's leading coefficients are correct. A bound
\(\epsilon_{h_Q,k,N(k)}^{\mathrm{cyc}}/k^3\to0\) at its actual admissible degrees would contradict the displayed inequality for a fixed \(\delta>0\) and any \(m\geq1\). This implication proves no such upper bound.

The corresponding two-point packet with fixed imaginary coordinate,
\(h_2(s)=\prod_{\varepsilon=\pm1}(s-(1/2+\varepsilon\delta+i\gamma))^m\),
has exactly \(k+1\) sums, all with the same length \(\ell_k\). Repeating the same positive-margin sum removes precisely the factor \(k+1\) from the quartet expression. The two-point bound in the note is correct for that packet and its own admitted degree \(N\geq\ell_k(k+1)-1\).

### 6.1 Necessary correction for a larger containing packet

Earlier sections allow an arbitrary nonempty reflection-stable packet \(h\). If it merely contains \(h_Q\), the identities
\(\chi_{h,k}=\chi_{h_Q,k}\) and
\(q_{h,k}=\ell_k(k+1)^2\) need not hold. Every quartet grid point is still a sum for the larger packet, with its actual maximal local length at least \(\ell_k\), but there can be additional points and larger lengths. The correct general statement is

\[
2\delta\ell_k(k+1)\left\lfloor\frac{(k+1)^2}{4}\right\rfloor
\leq L_{h,k}\leq\epsilon_{h,k,N}^{\mathrm{cyc}},
\qquad N\geq q_{h,k}-1.
\]

The quartet-only threshold cannot replace \(q_{h,k}-1\) here.

A concrete algebraic calibration demonstrating the degree issue is

\[
h_Q(s)=((s-\tfrac34)^2+1)((s-\tfrac14)^2+1),
\qquad
h(s)=h_Q(s)((s-\tfrac12)^2+4).
\]

It is monic, simple and stable under both reflection and conjugation. At
\(k=1\), the quartet has cyclic dimension four, but the containing packet has cyclic dimension six. The quartet threshold admits \(N=3\). In the six-dimensional remainder coordinates its matrix
\(K=\sum_{j=0}^{3}b_jb_j^*/\omega_j\) has rank at most four, so no inverse \(G=K^{-1}\) exists at that threshold, regardless of the choice of positive source norms. This is an explicit counterexample to the unrestricted algebraic degree claim. These calibration roots are not asserted to be zeta zeros. The correction in the actual-zero statement is simply to select \(h=h_Q\) explicitly, or to keep the larger packet's actual threshold.

If \(\delta=0\) or \(\gamma=0\), the four distinct roots and grid collapse; the quartet counting theorem does not extend with the same dimension formula. If \(m=0\), the packet is empty and this theorem does not apply. Although the finite grid identities can be extended combinatorially to \(k=0\), the source construction in the note is stated for \(k\geq1\); a zeroth-tensor extension must be named, not silently included.

## 7. Repeated roots, zero control, dimension one, and the empty packet

The determinant argument does not assert that critical-line Jordan blocks are absent whenever \(L=0\). For example, in literal coordinates \(G=I_2\) and

\[
A=\begin{pmatrix}k/2&1\\0&k/2\end{pmatrix}
\]

give \(L=0\) but
\(H=A^*+A-kI=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with
\(\epsilon=1\). This exact rank-two traceless calibration has a nontrivial critical-line Jordan block and confirms the note's distinction.

By contrast, if \(\epsilon=0\), then \(A-kI/2\) is \(G\)-skew-adjoint. Equivalently \(i(A-kI/2)\) is \(G\)-self-adjoint, so \(A\) is diagonalizable and all its eigenvalues have real part \(k/2\). For this cyclic algebra the minimal polynomial is exactly \(\chi\); diagonalizability therefore forces every \(\ell_\lambda=1\). Conversely critical-line spectrum alone does not force \(\epsilon=0\), as the preceding matrix shows. For \(k\geq1\), any root of \(h\) of multiplicity \(m>1\) supplies its repeated \(k\)-tuple, of local length \(1+k(m-1)>1\). Thus zero control is incompatible with any such root in this cyclic setting.

If \(d=\deg h=1\), reflection forces the unique root \(\rho\) to satisfy
\(\Re\rho=1/2\). Then \(q_k=1\), \(A=k\rho\), and for every actual positive scalar Gram \(G\),

\[
H=2k\Re\rho-k=0,\qquad \epsilon=0,\qquad L=0.
\]

There is no middle exterior degree: \(p=0,1\) are the two zero-control endpoints.

If \(h=1\) and \(k\geq1\), the coefficient spaces \(E_h,B_k,C\) are zero, \(\chi=1\), and \(q_k=0\). There is no nonzero coefficient Gram to invert. For every \(p\geq1\), \(\bigwedge^pC=0\), with unique zero maps. This does not imply that the analytic source amplitude or mass vanishes. Also
\(\bigwedge^0(0)=\mathbb C\), not zero: the zeroth exterior power is the tensor unit.

The note handles \(p=0\) separately in the proof of its inequality, which is correct. To make all later maps in sections 6.2 and 7 literally cover that endpoint, either restrict those paragraphs to \(p>0\), or state the conventions

\[
\det(0_{0\times0})=1,\quad
U_>(a)=I_{0\times0},\quad
P=Q=0,\quad
R_0:\mathbb C\longrightarrow\mathbb C
\text{ is the tensor-unit identity}.
\]

An empty \(0\times0\) Gram has its unique inverse as an endomorphism of the zero vector space; using that convention does not produce any nonzero spectral metric. The map \(R_0\) is into the zeroth source tensor power, not a claim about the \(k\)-fold analytic amplitude of an empty packet. These conventions make the volume equation exactly \(1=1\).

## 8. Supplementary independent finite checks and nilpotent interpretation

The primary auditor also ran 63 exact in-memory SymPy 1.13.1 guard checks, all passing with process exit zero. This was independently written code, not an archive script. For each \(q=2,3,4,5\), its literal fixture is

\[
T=I_q+\sum_{j=0}^{q-2}(j+1)E_{j,j+1},\qquad G=7T^*T,
\]

\[
A_0=I_q+2E_{0,0}-2E_{q-1,q-1}+3E_{0,q-1},
\quad A=T^{-1}A_0T,\quad k=2,
\]

\[
u=T^{-1}(2e_0-e_{q-1}),\quad
v=T^{-1}(e_0+2e_{q-1}+i(2e_0-e_{q-1})),\quad\omega=7.
\]

Its exact values are \(a=35,d=70,c=35i,\epsilon=5,L=4,\eta=1/5\), retaining both the nontrivial coordinate frame and the literal factor seven. Six conditions per dimension verify the rank-two source formula, epsilon radicand, rank/trace/adjoint identity, both projector products and square-zero difference, determinant trace, and both slack norms. Two conditions for every \(p=0,\ldots,q\) verify the complete exterior metric identity and characteristic polynomial, giving 36 exterior conditions. Three final conditions verify the nonzero critical Jordan example, the rank-four versus dimension-six source-degree obstruction, and the dimension-one zero control. Thus \(24+36+3=63\) conditions passed.

These calibration vectors do not claim to be the actual orthogonal-polynomial remainder vectors of the zeta measure. They test the exact finite-dimensional formulas and their coordinate/constant dependence; the general proofs above supply the mathematical argument for the actual input once its source identity is established.

A separately delegated read-only checker used its own in-memory Python combinatorics, not any archive script. It reported 132 successful exact conditions:

- Eight quartet fixtures \(k=0,\ldots,7\), with three conditions each: ordered-tuple margin multiplicities, positive-grid counts, and positive-defect sums.
- Fifty-four exterior fixtures \(n=1,\ldots,9\) and \(p=0,\ldots,n\), with two conditions each: the final nonzero power of the additive exterior of a nilpotent Jordan block, and its nonzero lowest-wedge coefficient.

The quartet check enumerates the \(4^k\) ordered bit-pair tuples and verifies their margin counts against \(\binom ka\binom kb\). The nilpotent check starts from the top wedge
\((n-p,\ldots,n-1)\); applying the additive Jordan lowering operator lowers one index by one, rejecting a term precisely if it hits \(-1\) or repeats the preceding index. Every surviving term retains its positive integer coefficient. The last nonzero power observed is \(p(n-p)\), its sole basis wedge is \((0,\ldots,p-1)\), and its coefficient is positive. The next power is zero.

This last observation has a direct exact proof for every \(n,p\), which also prevents a misleading interpretation of the note. On \(e_0,\ldots,e_{n-1}\) let \(Ne_j=e_{j-1}\) for \(j>0\), \(Ne_0=0\). The wedge index sum decreases by one at every surviving application of \(N^{[p]}\). Its range is from \(p(p-1)/2\) to \(p(2n-p-1)/2\), a difference of \(p(n-p)\), so the next power vanishes on the entire module. Starting with the top wedge, lower its first index to zero, then its second to one, and continue in increasing position order. Every step survives, no permutation sign is introduced, and the resulting coefficient in power \(p(n-p)\) is a positive integer. Thus the nilpotency index of \(N^{[p]}\) is exactly \(p(n-p)+1\), including \(p=0,n\), where the operator is zero on its one-dimensional exterior space.

The archive does not claim a complete Jordan decomposition of arbitrary exterior powers. On the full determinant of a generalized eigenspace it uses precisely the endpoint \(p=n\), where the nilpotent action is zero but the dimension \(n\) remains in the scalar trace. The independent tests are supplementary regression evidence; the proofs above establish the general statements.

## 9. Final handoff

No sign or factor correction is needed in the bounded rank-two, additive exterior, determinant, CRT-projector, or slack identities. Preserve the literal \(p!\), \(\omega_N\), original \(G\), and full cyclic local lengths. Make the quartet packet equality and source-degree domain explicit, and cover the \(p=0\) tensor-unit convention where the later determinant maps are displayed.

No archive code was executed by this audit. No canonical, release, or publication file was written. The sole written artifact is this permitted audit document. All substantive finite-dimensional claims assigned to this audit have been proved here; no analytic growth estimate or whole-source certification is inferred.
