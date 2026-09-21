# Independent review of RD1–29

Review date: 2026-09-20. Reviewed source: `RESIDUE_DUALITY_BODY.tex`, SHA256 `57bc2c625fc1444c0b7ad3ee1dec9d13b319c2715fb56cf3212c37a4684aa76c`. The whole RD1–29 text was read. Definitions were compared with the cumulative source at SF2–3, RW14, RW17 and RW19, and the finite-completion source at FS6–8 and FS11–12.

**Finding:** the mathematical statements RD1–29 are correct with the stated fixed reference period. The coefficient receiver of RD27 is a vector-space isomorphism, whereas RD24 is an algebra isomorphism. Their exact comparison in RD28 is correct. No determinant factor or sign correction is needed.

Two source defects need correction before integration:

- RD21 has `\widetilde B_u\,widetilde D_u`; the second factor must be `\widetilde D_u`.
- The paragraph before RD28 has a carriage-return character inside both parity subscripts. Use `F_{\mathrm{even}}` and `F_{\mathrm{odd}}`.

No edit was made to the reviewed RD source. The independent verifier `review_residue_duality.py` and its `RESIDUE_DUALITY_REVIEW_CERTIFICATE.json` record 353 passing exact algebra checks. They supplement the proofs below. Finite examples in the verifier are not used as a substitute for the general chart proof.

## 1. Global residue matrix and its inverse

Write

\[
h(r)=Ar^4+r^3+Br^2+Cr+D,\qquad A\ne0.
\]

Every class in \(E=\mathbb C[r]/(h)\) has a unique cubic representative. If a numerator is changed by \(hq\), its residue differential changes by \(q\,dr\), which has no finite residue. The sum of finite residues of a cubic numerator is the coefficient of \(r^{-1}\) in its expansion divided by \(h\), hence its cubic coefficient divided by \(A\). Therefore the functional in RD2 descends to the quotient and includes multiple roots without an extra assumption.

Set \(l_j=\lambda(r^j)\). Then \(l_0=l_1=l_2=0\), \(l_3=A^{-1}\). Applying \(\lambda\) to \(h,rh,r^2h\) gives

\[
l_4=-A^{-2},\qquad
l_5=A^{-3}-BA^{-2},\qquad
l_6=-A^{-4}+2BA^{-3}-CA^{-2}.
\]

These are all entries of \(H=(l_{i+j})_{0\le i,j\le3}\). For

\[
J=\begin{pmatrix}C&B&1&A\\B&1&A&0\\1&A&0&0\\A&0&0&0\end{pmatrix},
\]

the identity \(HJ=JH=I\) follows entry by entry from these six values. It is also independently checked symbolically. The coefficient identity

\[
(1,x,x^2,x^3)J(1,y,y^2,y^3)^{\mathsf T}
=\frac{h(x)-h(y)}{x-y}
\]

fixes the Bezout sign directly, without a convention inferred from a name.

In \(S=E\oplus tE\), with \(t^2=h'\), the odd coefficient of
\((R+tS)(P+tQ)\) is \(RQ+SP\). Its residue matrix is therefore

\[
B_S=\begin{pmatrix}0&H\\H&0\end{pmatrix},\qquad
B_S^{-1}=\begin{pmatrix}0&J\\J&0\end{pmatrix}.
\]

The reversed diagonal of \(H\) has four entries \(A^{-1}\). Its reversal permutation has sign \((-1)^6=1\). Thus \(\det H=A^{-4}\); exchanging the two four-dimensional blocks has sign \((-1)^4=1\), so \(\det B_S=A^{-8}\). Neither determinant contains the quartic discriminant.

## 2. Exact map to ordinary trace

Let \(L=M_{h'}\) in \(E\). In the stated parity order,

\[
M_t=\begin{pmatrix}0&L\\I&0\end{pmatrix},\qquad
M_{2t^3}=2\begin{pmatrix}0&L^2\\L&0\end{pmatrix}.
\]

At a root \(r_0\) of multiplicity \(m\), multiplication by a polynomial \(R\) in \(\mathbb C[\epsilon]/(\epsilon^m)\) is triangular with diagonal \(R(r_0)\), repeated \(m\) times. Its trace is \(mR(r_0)\). Since \(h'/h=m/\epsilon+g'/g\), the residue of \(h'R/h\) is the same number. Adding the local equalities gives

\[
\operatorname{Tr}_E M_R=\lambda(h'R).
\]

Multiplication by \(R+tS\) in the signed algebra has diagonal blocks \(M_R,M_R\); therefore

\[
\operatorname{Tr}_S M_{R+tS}=2\lambda(h'R)
=\Lambda(2t^3(R+tS)).
\]

This proves \(T=B_SM_{2t^3}\) also on nonreduced fibres. At distinct roots,

\[
\det L=\prod_{j=1}^4h'(r_j)
=A^4\prod_{i<j}(r_i-r_j)^2
=\operatorname{Disc}(h)/A^2.
\]

The six signs in the unordered-pair product give \((-1)^6=1\). Both sides are coefficient identities with only powers of \(A\) inverted, so they extend to every fibre of this chart. Finally

\[
\det M_{2t^3}=2^8(\det L)^3,\qquad
\det T=256\operatorname{Disc}(h)^3/A^{14}.
\]

The companion matrix and derivative polynomial in RD7 are correct. The verifier independently checks the generic determinant of this derivative matrix.

## 3. Local algebra, lost trace directions and retained duality

If \(h(r_0+\epsilon)=\epsilon^mg(\epsilon)\), the exact local signed algebra is

\[
\mathbb C[\epsilon,t]/(\epsilon^m,t^2-mg_0\epsilon^{m-1}),
\quad g_0=g(0)\ne0.
\]

Terms of \(g\) above degree zero disappear from this second relation, but they do not disappear from the functional

\[
\Lambda(R+tS)=[\epsilon^{m-1}]S/g.
\]

The draft correctly keeps them in the inverse series \(1/g\). The Hankel matrix is anti-triangular with reversed diagonal \(g_0^{-1}\), and the block exchange contributes \((-1)^m\); hence the determinant of the full local residue matrix is \((-1)^mg_0^{-2m}\).

For \(F=\sum R_k\epsilon^k+t\sum S_k\epsilon^k\), multiplication by \(t\epsilon^{m-1-j}g\) has odd coefficient \(R\epsilon^{m-1-j}g\). Dividing by \(g\) and taking the top coefficient gives exactly \(R_j\). Multiplication by \(\epsilon^{m-1-j}g\) gives \(S_j\). This proves all RD11 test vectors, including arbitrary nonzero nilpotents.

For \(m\ge2\), \(t^4=0\) and

\[
2t^3F=2mg_0R_0t\epsilon^{m-1}.
\]

The image vector is nonzero in the displayed free parity basis. Thus the image has dimension one, the kernel is the maximal ideal \((\epsilon,t)\), and applying \(\Lambda\) gives trace \(2mR_0\). The trace pairing is \(2mR_0P_0\), of rank one. Simple roots instead have two distinct signed points and trace rank two. This proves the asserted total trace-rank formula.

For an entire function of order \(\nu\) at the root, its germ is \(\epsilon^\nu\) times an invertible germ. Multiplication by \(\epsilon^\nu\) has rank \(\max(m-\nu,0)\) on each of the even and odd summands. This proves the rank formula in the paragraph after RD16 without an assertion about the arithmetic value of \(\nu\).

## 4. Paired critical jets and the two root projectors

For the retained quartic factor \(-1/2\), one has

\[
g_\eta(\epsilon)=-\tfrac12(\epsilon+2i\eta\gamma)^2,
\quad g_0=2\gamma^2,\quad g_1=-2i\eta\gamma.
\]

Consequently \(t^2=4\gamma^2\epsilon\), \(\Lambda(t)=i\eta/(2\gamma^3)\), and \(\Lambda(t^3)=2\). The matrix RD14 and determinant 16 follow immediately; the independent calculation verifies them for both signs.

The derivative identity \(\xi'(1/2+i\eta\gamma)=-i\eta X'(\gamma)\) follows by the chain rule for \(\eta=1\), and by differentiating \(\xi(s)=\xi(1-s)\) for \(\eta=-1\). Thus the two measurements are

\[
m_3=2X,\qquad m_1=\frac{i\eta X}{2\gamma^3}-\frac{i\eta X'}{2\gamma^2}.
\]

Solving gives \(X=m_3/2\) and
\(X'=2i\eta\gamma^2(m_1-i\eta m_3/(4\gamma^3))\), exactly RD16.

For \(d=2i\eta\gamma\), the selected projector is
\((\epsilon+d)^2d^{-2}(1-2\epsilon/d)\). Its constant and linear terms at \(\epsilon=0\) are 1 and 0, while the factor \((\epsilon+d)^2\) kills both coefficients at the other root. The two squared root ideals are coprime, so these two congruences establish every projector identity in RD17. They also show that multiplying by the projector restricts the residue functional to the selected root component.

## 5. Original conductor maps and all metrics

The fixed reference quartet is essential: the draft does not replace \(X,Y,E,O\) by a colliding frame. On the fixed reference domain, the existing identities are \(Y=T_AX\), \(\Psi=T_A\Phi\), and \(O\) invertible. Therefore the block map

\[
J_W=\begin{pmatrix}Y&0\\\Psi E&\Psi O\end{pmatrix}
\]

is invertible with the exact two-step inverse in RD20. Its determinant is \(\det Y\det\Psi\det O\). Multiplying by the coefficient translation \(D_\kappa\), whose determinant is one, gives \(Q\) and its stated inverse.

For any invertible \(Q\), congruence gives

\[
\widetilde B=Q^{\mathsf T}B_SQ,
\quad\widetilde B^{-1}=Q^{-1}B_S^{-1}Q^{-\mathsf T},
\quad Q^{\mathsf T}TQ=\widetilde B(Q^{-1}M_{2t^3}Q).
\]

This proves all RD21 identities after the source typo is fixed. Its kernel is exactly \(Q^{-1}\ker M_{2t^3}\), because the first factor is invertible. The determinant is the square of the block-map determinant times \(A^{-8}\).

RW14 and RW19 confirm the distinct target and source Grams used in RD22: the first block is \(G_Y\) or \(G_X\), and the second is \(G\) or \(G_U\). In particular replacing the target diagonal by two copies of \(G\) would be incorrect; the draft does not do that. For a row \(\ell\), writing a vector as \(H^{-1/2}v\) proves that its squared dual norm is \(\ell H^{-1}\ell^*\). These are the original Grams, so this step makes no change to a moment, mass or norm.

Finally, if \(\mathbb W\) is Hermitian, then

\[
\mathscr A(z)=\widetilde B^{-1}\mathbb W^{\mathsf T}\bar z
=\widetilde B^{-1}\overline{\mathbb Wz}.
\]

Its kernel is therefore \(\ker\mathbb W\). Since \(\widetilde B\) is symmetric,
\((\mathscr A(z))^{\mathsf T}\widetilde Bw=z^*\mathbb Ww\).
This proves RD23, including the conjugations and transpose order. The comparison preserves the complete RW17 kernel, not merely its four-dimensional graph subspace.

## 6. Chart factors, polynomial inverse and the original seven-point fibre

Under \(r=p-R^{-1}\), the derivative is \(dr/dR=R^{-2}\). Thus

\[
h_p(R)=R^4h(p-R^{-1}),\qquad
h_p'(R)=4R^3h(p-R^{-1})+R^2h'(p-R^{-1}).
\]

Modulo \(h_p\), the first term vanishes. Consequently \(T=Rt\) satisfies \(T^2=h_p'(R)\). On the common chart \(A\ne0\), \(R\) is a unit because \(h_p(0)=A\). The substitution and its inverse are therefore algebra isomorphisms on exactly the stated overlap.

For \(F=U(r)+tV(r)\), its new odd coefficient is \(V(p-R^{-1})/R\). Meanwhile

\[
\frac{V(r)dr}{h(r)}
=\frac{R^2V(p-R^{-1})dR}{h_p(R)}.
\]

The factor multiplying the new odd coefficient is exactly \(R^3\). This proves RD26, including its sign. The same cubic-remainder argument as in section 1, now with cubic coefficient \(b\), proves the displayed general \(H_p\) and inverse in RD25.

For the separate physical coefficient map, put \(q=p+\kappa\). The forward images of the four monomials are

\[
R^3,\quad R^2(qR-1),\quad R(qR-1)^2,\quad(qR-1)^3.
\]

Their coefficient matrix has reversed-diagonal entries \(1,-1,1,-1\); the reversal sign and product of those entries are both 1. Its determinant is therefore 1. Substituting \(R=(q-S')^{-1}\) and multiplying by \((q-S')^3\) gives each original monomial \(S'^j\). This proves both inverse formulas as polynomial identities, including the apparent denominator points after multiplication. Thus no pole is introduced at \(R=0\).

Let \(F\) be the original algebra image of a physical input. Its even part is multiplied by \(R^3\) and its odd part by \(R^4\) under this physical receiver. The odd part of a product of two such images therefore gets the common factor \(R^7\). Formula RD26 removes \(R^3\), leaving exactly

\[
\Lambda_p(F_pG_p)=\Lambda_u(R^4FG)
=\Lambda_u((p-r)^{-4}FG).
\]

Even parts on the right do not contribute to \(\Lambda\). The remaining multiplier is invertible on the overlap. This proves RD28 for arbitrary algebra classes, including repeated roots. Exact overlap checks in the verifier additionally cover root multiplicities 1, 2, 3 and 4.

At the original target and \(p=2\),

\[
h_2(R)=R(R-1)(2R-1)(3R-1).
\]

The roots are \(0,1/3,1/2,1\), their six positive differences have product \(1/108\), and the leading coefficient is 6. Thus the discriminant is \(6^6/108^2=4\). At zero the derivative is \(-1\), giving \(T=\pm i\). FS7 gives \(T=\theta\) at the infinity root. FS12 then gives \(b=1/\theta\), so \(\theta=-i\) has \(b=i\), the original affine state, while \(\theta=i\) is the omitted state. This verifies the sign assertion, both determinants in RD29, and the inclusion of eight completed states with seven original affine states.

## Coverage limit

This review establishes the finite algebra, exact residue-to-trace map, critical jet measurements, and their full coefficient/conductor return. It proves no new Hermitian positivity from a complex bilinear form. It proves no additional arithmetic endpoint. The classical literature citation at the start of RD remains the source author's separately documented reading; this review verifies the displayed identities directly and does not claim another reading of that paper.
