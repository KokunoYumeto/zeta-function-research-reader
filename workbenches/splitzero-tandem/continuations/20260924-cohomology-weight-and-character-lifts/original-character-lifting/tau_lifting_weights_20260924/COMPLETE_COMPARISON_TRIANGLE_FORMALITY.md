# The whole comparison triangle: canonical projections and exact contractions

24 September 2026. CTF0–CTF8. Independent derivation from the actual GAP, FDB and DCP complexes. The result strengthens GAP6 and FDB8 from a calculation of every cohomology group to an explicit equivariant quasi-isomorphism of the entire comparison cone and a derived comparison of the entire triangle. It also retains the faithful source extension on both objects and contracts precisely its identity comparison cone.

## CTF0. Scope, original sources, and category

The files GLOBAL_ADELIC_LIFTING_AND_PRIME_BOUNDARY.md GAP0–GAP9, FULL_DERIVED_PRIME_BOUNDARY_REVIEW.md FDB0–FDB9, and SOURCE_CC_DOUBLE_PULLBACK.md DCP0–DCP12 were read, including a separate complete reading of DCP8–DCP9 after a combined tool output truncated that passage. CORPUS_AND_OPERATION_RULES.md was reread. The complete user global arguments were read for OMS and continue to govern the receiving operations: primitive \(Z_1/\tau\) has no source addition or parity, and the arithmetic and complex coefficient operations below occur after the whole-spectrum reconstruction.

Human sources retain their authorship: Alain Connes, [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function](https://arxiv.org/abs/math/9811068v1); Alain Connes, Caterina Consani and Matilde Marcolli, [The Weil proof and the geometry of the adeles class space](https://arxiv.org/abs/math/0703392v1); Alain Connes and Caterina Consani, [Schemes over \(\mathbb F_1\) and zeta functions, §5](https://arxiv.org/abs/0903.2024v3); Ralf Meyer, [A spectral interpretation for the zeros of the Riemann zeta function](https://arxiv.org/abs/math/0412277v3). The original-source reading records are the cited programme proofs; this note does not claim a new full reading of those papers. The closed summation-image theorem used below was proved and independently checked in OMS/SSI. Jean-Louis Koszul's resolution is retained with its actual differential and the exactness argument recalled in CTF1.

All adelic group algebras and exterior powers below are algebraic, and the complete calculation is in complexes of complex representations of the specified real dilations, diagonal rational action and mirror. The mirror and dilation satisfy their original twisted relation. Where spaces have the original Schwartz or strong Fréchet topologies, the displayed maps on those spaces are continuous. No topology on an infinite algebraic direct sum is added. No equivariant section of the quotient \(Q_{\rm cen}\) into its test space is asserted.

Canonical in this note means that the maps are explicitly determined by the original Fourier transform, ordered two-chart comparison, rational valuation derivations, endpoint moments, and quotient maps. It does not assert uniqueness among every conceivable quasi-isomorphism.

## CTF1. The exact original source complex and its existing comparison

Keep
\[
G=\mathbb Q_{>0}^{\times},\quad R=\mathbb C[G],\quad
\varepsilon(t_a)=1,\quad x_p=t_p-1,\quad
W_{\rm pr}=\bigoplus_{p\ {\rm prime}}\mathbb C\ell_p,
\]
\[
H=\mathcal S_{\rm even}(\mathbb R),\quad
m(h)=\left(h(0),\int_{\mathbb R}h(v)\,dv\right),\quad
S=\ker m,\quad M_0=\ker(\varepsilon\otimes m:R\otimes H\to\mathbb C^2),
\]
\[
\Phi=\varepsilon\otimes\mathrm{id}:M_0\to S,\quad
\mathcal Eh(u)=u^{1/2}\sum_{r\ge1}h(ru),\quad
J=2\mathcal E\Phi.
\tag{CTF1.1}
\]
The original strong space \(\mathcal A\) consists of the smooth functions with
\(\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jk(u)|<\infty\) for every \(N,j\ge0\).
Put \(Q_{\rm cen}=\mathcal A/(2\mathcal ES)\).
The original complex has \(C^1=\mathcal A\) and \(C^{-k}=M_0\otimes\Lambda^kW_{\rm pr}\), \(k\ge0\), with \(d_C^0=J\) and
\[
d_C(c\otimes\ell_{p_1}\wedge\cdots\wedge\ell_{p_k})
=\sum_{i=1}^k(-1)^{i-1}x_{p_i}c\otimes
\ell_{p_1}\wedge\cdots\widehat{\ell_{p_i}}\cdots\wedge\ell_{p_k}.
\tag{CTF1.2}
\]
The primes are ordered increasingly in each wedge. No factor two or Koszul sign is changed.

The established map to the zero-differential complex
\[
H_C=Q_{\rm cen}[-1]\oplus\bigoplus_{n\ge1}B_n[n-1],
\quad B_n=\Lambda^nW_{\rm pr}\otimes\mathbb C^2,
\quad(K[r])^j=K^{j+r},
\]
is
\[
\Gamma^1=\pi_{\rm cen},\qquad
\Gamma^{-k}\left(\left(\sum_i r_i\otimes h_i\right)\otimes\omega\right)
=\frac1{k+1}\sum_{p,i}D_p(r_i)\,
\ell_p\wedge\omega\otimes m(h_i),
\tag{CTF1.3}
\]
where \(D_p(\sum_ac_at_a)=\sum_ac_av_p(a)\) is the scalar augmentation derivation. Its product rule gives \(D_p(x_qr)=\delta_{pq}\varepsilon(r)\). Therefore applying \(\Gamma\) to (CTF1.2) produces \(k\) copies of the same ordered wedge divided by \(k\), each multiplied by the zero moment \(\sum_i\varepsilon(r_i)m(h_i)=0\). At the final differential, \(\pi_{\rm cen}J=0\). Thus \(\Gamma\) is a chain map.

For the quasi-isomorphism, the ordered Koszul complex of \(R\) resolves the augmentation module. On a finite prime set, successive quotients by \(t_p-1\) remain Laurent polynomial algebras; the next \(t_p-1\) is a nonzero divisor. Taking the cone of its multiplication proves exactness inductively. Every cycle in the full algebraic complex uses finitely many variables and wedge indices, so the finite proof gives a finite primitive. Applying this resolution to
\[
0\to M_0\to R\otimes H\to\mathbb C^2\to0
\]
gives \(H^1(C)=Q_{\rm cen}\) and \(H^{1-n}(C)=B_n\).
Indeed the middle resolved module has only degree-zero homology \(H\), while the last has zero differential and terms \(\Lambda^nW_{\rm pr}\otimes\mathbb C^2\). Its connecting representative is
\[
z_{\omega,u}=
\sum_{i=1}^n(-1)^{i-1}
(x_{p_i}\otimes\sigma(u))\otimes
\ell_{p_1}\wedge\cdots\widehat{\ell_{p_i}}\cdots\wedge\ell_{p_n},
\tag{CTF1.4}
\]
for any moment section \(m\sigma=\mathrm{id}\).
One available section is
\(\sigma(u_0,u_1)(v)=[u_0(1-2\pi v^2)+u_1\,2\pi v^2]e^{-\pi v^2}\).
Changing it changes the representative by a Koszul boundary, since the difference has both moments zero. Each of the \(n\) terms in (CTF1.4) contributes \(\omega\otimes u/n\) under \(\Gamma^{1-n}\). Hence \(\Gamma\) induces identity on \(B_n\), and it induces the quotient identity in degree one. This proves the established quasi-isomorphism with every degree retained.

The source is the oriented complex \(C^{\rm or}\) of GAP5/FDB7: its differential is unchanged, and its mirror is \(-\mathcal F_k\) in degree \(-k\) and \(-R_{\rm cen}\) in degree one, where \(R_{\rm cen}k(u)=k(1/u)\) and
\[
\mathcal F_k((r\otimes h)\otimes\ell_P)
=(-1)^k(t_P^{-1}\iota(r)\otimes\widehat h)\otimes\ell_P,\quad
t_P=\prod_{p\in P}t_p,\quad\iota(t_a)=t_{a^{-1}}.
\tag{CTF1.5}
\]
The identity \(\iota(x_p)=-t_p^{-1}x_p\) proves that this commutes with the Koszul differential. Applying \(D_p\) to the inverted coefficient gives the extra sign and the augmentation-moment term, which vanishes. Thus under \(\Gamma\), the oriented mirror is
\[
w_{H_C}|_{B_n}=(-1)^{n+1}\mathrm{id}\otimes S_2,\quad
S_2(u_0,u_1)=(u_1,u_0),\qquad
w_{H_C}|_{Q_{\rm cen}}=-R_{\rm cen}.
\tag{CTF1.6}
\]
Real dilation acts by \(h(v)\mapsto h(v/a)\) on the \(H\) coefficient, by \(W_ak(u)=a^{1/2}k(u/a)\) on \(\mathcal A\), and by \(\mathrm{id}\otimes\operatorname{diag}(1,a)\) on each \(B_n\). The moment formula proves equivariance of \(\Gamma\). The diagonal rational action \(t_b\) has an extra derivative \(v_p(b)\sum_i\varepsilon(r_i)m(h_i)=0\), so it acts trivially on all terms of \(H_C\). This retains both kinds of arithmetic action separately.

## CTF2. A canonical projection of the actual two-chart complex

Use the original raw spaces
\[
V_+=S\oplus\mathbb C^2,\quad V_-=S\oplus\mathbb C^2,\quad
D^0=V_+\oplus V_-,\quad D^1=A,
\]
\[
\Sigma h(u)=2\sum_{r\ge1}h(ru),\quad R_{\rm raw}b(u)=u^{-1}b(1/u),
\]
\[
d_D((h,c_0,c_1),(g,d_0,d_1))=\Sigma h-R_{\rm raw}\Sigma g,
\quad Q_{\rm raw}=A/\Sigma S.
\tag{CTF2.1}
\]
Here \(A\) has the strong raw test-space seminorms of DCP3. The full Poisson formula
\[
\Sigma\widehat h(u)=u^{-1}\Sigma h(u^{-1})
+u^{-1}h(0)-\int_{\mathbb R}h(v)\,dv
\]
gives \(R_{\rm raw}\Sigma h=\Sigma\widehat h\) on this \(S\), with its two endpoint conditions imposed and its separate chart endpoint coordinates retained. Fourier is involutive on even functions, and \(\Sigma\) is injective with its closed image by the proved original-zeta synthesis. Consequently
\[
H_D^0=\ker d_D
=\{((h,c_0,c_1),(\widehat h,d_0,d_1)):h\in S\},\qquad
H_D^1=Q_{\rm raw}.
\tag{CTF2.2}
\]
Let \(H_D=H_D^0[0]\oplus Q_{\rm raw}[-1]\), with zero differential.

Define
\[
\begin{aligned}
\Pi_D^0((h,c_0,c_1),(g,d_0,d_1))
={}&\left(\left(\frac{h+\widehat g}{2},c_0,c_1\right),
\left(\frac{\widehat h+g}{2},d_0,d_1\right)\right),\\
\Pi_D^1(b)={}&\pi_{\rm raw}(b).
\end{aligned}
\tag{CTF2.3}
\]
The second Schwartz entry is the Fourier transform of the first, so the output lies in \(H_D^0\). The endpoint coordinates are all unchanged. The chain equation in degree zero is \(\pi_{\rm raw}d_D=0\); in the other degrees it is between zero maps. The restriction of \(\Pi_D^0\) to \(\ker d_D\) is identity, and the induced map on degree-one cohomology is the quotient identity. Therefore
\[
\boxed{\Pi_D:D\longrightarrow H_D\ \text{is a canonical quasi-isomorphism}.}
\tag{CTF2.4}
\]
Both components are continuous on the original section and quotient topologies.

Its kernel is also exact on the stated spaces. In degree zero it is precisely
\[
A_{\rm anti}=
\{((h,0,0),(-\widehat h,0,0)):h\in S\},
\]
and in degree one it is \(\Sigma S\). On the displayed degree-zero vector the differential is \(2\Sigma h\), with continuous inverse
\[
b\longmapsto
\left(\left(\frac12\Sigma^{-1}b,0,0\right),
\left(-\frac12\widehat{\Sigma^{-1}b},0,0\right)\right).
\tag{CTF2.5}
\]
Thus this kernel complex has a concrete contraction on its own domain. This proves no equivariant section of the quotient map \(A\to Q_{\rm raw}\) with image in \(A\): (CTF2.5) has domain \(\Sigma S\), not \(Q_{\rm raw}\).

## CTF3. Every action on the projection

For \(a>0\), write \(R_ah(v)=h(v/a)\) and \(M_ag(v)=a g(av)\). The original chart action is
\[
\rho_D^0(a)((h,c_0,c_1),(g,d_0,d_1))
=((R_ah,c_0,ac_1),(M_ag,ad_0,d_1)),
\quad \rho_D^1(a)b(u)=b(u/a).
\tag{CTF3.1}
\]
Fourier change of variables proves
\[
\widehat{R_ah}=M_a\widehat h,\qquad
\widehat{M_ag}=R_a\widehat g.
\tag{CTF3.2}
\]
The first Schwartz entry of \(\Pi_D^0\rho_D^0(a)v\) is consequently
\(R_a(h+\widehat g)/2\), and its second is
\(M_a(\widehat h+g)/2\). These are exactly the entries of
\(\rho_{H_D}^0(a)\Pi_D^0v\), while all four endpoint factors agree individually. In degree one, the quotient is equivariant because dilation preserves \(\Sigma S\).

The ordered chart-swap mirror is
\[
w_D^0(v_+,v_-)=(v_-,v_+),\qquad
w_D^1=-R_{\rm raw}.
\tag{CTF3.3}
\]
On swapping \(h,g\), the first and second Schwartz entries in (CTF2.3) interchange. Therefore \(\Pi_D^0w_D^0=w_{H_D}^0\Pi_D^0\). In degree one the quotient retains the negative reflection, so \(\Pi_D^1w_D^1=w_{H_D}^1\Pi_D^1\). No change of scale is made; the original relation remains
\(\rho(a)w=a\,w\rho(a^{-1})\).
The full diagonal rational action is trivial on \(D\), hence also on \(H_D\), so its equivariance is immediate.

## CTF4. The strict commuting square for the whole comparison

Keep the exact test-space isomorphism and its induced quotient map:
\[
\mathcal T:\mathcal A\to A,\quad
\mathcal Tk(u)=2u^{-1/2}k(u),\quad
\mathcal T^{-1}b(u)=\tfrac12u^{1/2}b(u),\quad
\overline{\mathcal T}:Q_{\rm cen}\xrightarrow{\sim}Q_{\rm raw}.
\tag{CTF4.1}
\]
The map takes \(2\mathcal ES\) onto \(2\Sigma S=\Sigma S\); it has
\(\mathcal M_0(\mathcal Tk)=2F_k\), so its complete receiving factor two is retained.
It intertwines the real actions and the two oriented degree-one mirrors:
\[
\mathcal TW_a=T_a\mathcal T,\qquad
\mathcal T(-R_{\rm cen})=-R_{\rm raw}\mathcal T.
\tag{CTF4.2}
\]

The actual GAP5/FDB7 map is
\[
F_{\rm sym}^1=\mathcal T,\qquad
F_{\rm sym}^0(c)=((\Phi c,0,0),(-\widehat{\Phi c},0,0)),
\qquad F_{\rm sym}^j=0\quad(j<0).
\tag{CTF4.3}
\]
Its chain equation retains both summation factors:
\[
d_DF_{\rm sym}^0c
=\Sigma\Phi c+R_{\rm raw}\Sigma\widehat{\Phi c}
=2\Sigma\Phi c
=\mathcal T(2\mathcal E\Phi c)=F_{\rm sym}^1Jc.
\]
Also \(\Phi d_C=0\) on the negative differential. Equations (CTF3.2) and (CTF4.2), and the oriented mirror (CTF1.5), prove the equivariance recorded in FDB7.

Define the zero-differential comparison
\[
\beta:H_C\to H_D,\qquad
\beta^1=\overline{\mathcal T},\qquad
\beta^{1-n}|_{B_n}=0\quad(n\ge1).
\tag{CTF4.4}
\]
It is equivariant by (CTF4.2), with zero maps in the remaining degrees. Direct substitution into (CTF2.3) gives
\[
\Pi_D^0F_{\rm sym}^0(c)=0
\]
since \(\widehat{-\widehat{\Phi c}}=-\Phi c\); all endpoint entries are zero. In degree one,
\(\pi_{\rm raw}\mathcal T=\overline{\mathcal T}\pi_{\rm cen}\).
All lower components vanish. We have therefore proved the strict square
\[
\boxed{\Pi_DF_{\rm sym}=\beta\Gamma}
\tag{CTF4.5}
\]
on all cochains, not merely on their cohomology.

## CTF5. The entire cone and the exact comparison map

Retain precisely the original cochain cone convention
\[
K^j=D^j\oplus(C^{\rm or})^{j+1},\qquad
d_K(v,c)=(d_Dv+F_{\rm sym}c,-d_Cc).
\tag{CTF5.1}
\]
The plus sign in the off-diagonal term and the minus sign in the shifted differential are both required. Write \(K_H=\operatorname{Cone}(\beta)\) with the same convention. The strict square (CTF4.5) gives
\[
\Xi:K\to K_H,\qquad
\Xi^j(v,c)=(\Pi_D^jv,\Gamma^{j+1}c).
\tag{CTF5.2}
\]
No additional sign is applied to the shifted component. Indeed
\[
\Xi d_K(v,c)=
(\Pi_Dd_Dv+\Pi_DF_{\rm sym}c,-\Gamma d_Cc)
=(\beta\Gamma c,0)
=d_{K_H}\Xi(v,c),
\]
since the target two complexes have zero differentials.
All actions are componentwise on each cone, so equivariance follows from the proved equivariance of \(\Gamma,\Pi_D,F_{\rm sym}\).

For completeness, \(\Xi\) is a quasi-isomorphism without a bounded-below hypothesis. The cone short exact sequences
\[
0\to D\to K\to C^{\rm or}[1]\to0,\qquad
0\to H_D\to K_H\to H_C[1]\to0
\]
are degreewise split. Their connecting map sends a class \([c]\in H^{j+1}(C)\), represented in the shifted term, to \([F_{\rm sym}c]\in H^{j+1}(D)\): the lift \((0,c)\) has differential \((F_{\rm sym}c,0)\), with positive sign. The strict square gives a map of these exact sequences. For each degree the long exact cohomology rows have isomorphisms on the source and target-complex terms because \(\Gamma,\Pi_D\) are quasi-isomorphisms. The exactness diagram chase makes the middle cone map an isomorphism. This argument uses only the five neighboring groups in any degree, so the infinitely many negative degrees introduce no limit operation.

The explicit terms of \(K_H\) are
\[
K_H^{-n}=B_n\quad(n\ge1),\qquad
K_H^0=H_D^0\oplus Q_{\rm cen},\qquad
K_H^1=Q_{\rm raw},
\]
\[
d_{K_H}^0(h,q)=\overline{\mathcal T}q,
\quad\text{all other differentials zero}.
\tag{CTF5.3}
\]
Let
\[
E=H_D^0[0]\oplus\bigoplus_{n\ge1}B_n[n],
\qquad d_E=0.
\tag{CTF5.4}
\]
Its canonical projection \(p:K_H\to E\) is identity on each \(B_n\), sends \((h,q)\mapsto h\) in degree zero and sends degree one to zero. Its canonical inclusion \(i:E\to K_H\) is identity on the negative terms and \(h\mapsto(h,0)\) in degree zero.

There is a complete explicit degree-minus-one homotopy
\[
h^1:Q_{\rm raw}\to H_D^0\oplus Q_{\rm cen},\quad
h^1(q)=(0,\overline{\mathcal T}^{-1}q),\qquad
h^j=0\quad(j\ne1).
\tag{CTF5.5}
\]
In degree zero, \(hd(h,q)=(0,q)\); in degree one, \(dh(q)=q\); in every negative degree both are zero. Therefore
\[
\boxed{dh+hd=\mathrm{id}_{K_H}-ip,\qquad pi=\mathrm{id}_E.}
\tag{CTF5.6}
\]
Also \(h^2=0\), \(hi=0\), and \(ph=0\), directly from the component formulas. The inverse \(\overline{\mathcal T}^{-1}\) is equivariant, including the negative reflection on both quotient terms; all these maps and the homotopy preserve the original actions.

The resulting direct cone projection is
\[
\boxed{\Pi_K=p\Xi:K\longrightarrow
H_D^0[0]\oplus\bigoplus_{n\ge1}B_n[n]}
\tag{CTF5.7}
\]
with the exact formulas
\[
\Pi_K^0(v,k)=\Pi_D^0v,\qquad
\Pi_K^{-n}(c)=\Gamma^{1-n}c\ (n\ge1),\qquad
\Pi_K^1=0.
\tag{CTF5.8}
\]
At degree \(-1\), its chain equation is precisely
\(\Pi_D^0F_{\rm sym}^0c=0\); at lower degrees it is \(\Gamma d_C=0\), with the retained cone minus sign. This is an equivariant quasi-isomorphism of the actual entire cone. It strengthens the prior all-degree cohomology calculation, rather than asserting that every original cochain is already a direct sum of cohomology representatives.

One can also check the degree-zero assertion directly on the original complex, with an explicit boundary. A cycle is \((v,k)\) with \(d_Dv+\mathcal Tk=0\). Write \(v=((h,c_0,c_1),(g,d_0,d_1))\), and put \(t=(h-\widehat g)/2\in S\). Then
\[
v-\Pi_D^0v=((t,0,0),(-\widehat t,0,0)),\qquad
d_Dv=2\Sigma t,\qquad k=-2\mathcal Et.
\]
The element \(c=t_1\otimes t\in M_0=C^0=K^{-1}\) has \(\Phi c=t\), so
\[
d_Kc=(F_{\rm sym}^0c,-Jc)
=(v-\Pi_D^0v,k).
\]
Thus every degree-zero cone cycle differs from its projected \(H_D^0\) representative by this actual boundary, including the negative shifted differential. Conversely \(\Pi_D^0F_{\rm sym}^0=0\) shows that a nonzero \(H_D^0\) representative is not a boundary. This use of the supplied arithmetic unit \(t_1\) and the explicit \(t\in S\) is not a section of a Mellin quotient.

## CTF6. The whole triangle and its final connecting homotopy

The square in CTF4 and map \(\Xi\) give a strict map of the two cone triangles before contraction. After contraction, the derived triangle is represented by
\[
H_C\xrightarrow{\beta}H_D
\xrightarrow{\alpha}E\xrightarrow{\delta}H_C[1],
\tag{CTF6.1}
\]
where \(\alpha\) is projection to \(H_D^0\) in degree zero and zero on \(Q_{\rm raw}\), while \(\delta\) is identity from each \(B_n\) in degree \(-n\) to the same \(B_n\subset H_C^{1-n}\) and zero on \(H_D^0\). The connecting sign is positive: the cone projection is \((v,c)\mapsto c\), and the differential on \(C[1]\) is \(-d_C\), already accounted for in (CTF5.1).

It is essential to distinguish strict equality from homotopy in the final square. On \(K_H\), let \(q_H(v,c)=c\) be the cone projection. Then
\(q_H-\delta p\) is the projection from \(Q_{\rm cen}\subset K_H^0\) to \(H_C[1]^0=Q_{\rm cen}\).
Define a degree-minus-one map to \(H_C[1]\) by
\[
\eta_H^1(q_{\rm raw})=\overline{\mathcal T}^{-1}q_{\rm raw}
\in H_C[1]^0,\qquad \eta_H^j=0\ (j\ne1).
\]
Since \(d_{H_C[1]}=0\), (CTF5.3) gives
\[
q_H-\delta p=d_{H_C[1]}\eta_H+\eta_Hd_{K_H}.
\tag{CTF6.2}
\]
On the original cone this reads
\[
\Gamma[1]\operatorname{pr}_C-\delta\Pi_K
=d_{H_C[1]}\eta+\eta d_K,\qquad
\eta^1(b)=\overline{\mathcal T}^{-1}\pi_{\rm raw}(b)
\quad(b\in K^1=A),
\tag{CTF6.3}
\]
and every other \(\eta^j\) is zero. In degree zero,
\[
\eta^1(d_Dv+\mathcal Tk)=
\overline{\mathcal T}^{-1}\pi_{\rm raw}(d_Dv+\mathcal Tk)
=\pi_{\rm cen}k,
\]
which is exactly the difference in that degree. In every negative degree the two connecting maps coincide.
The second square commutes strictly:
\(\Pi_K(v,0)=\alpha\Pi_Dv\).
Thus the full triangle comparison is canonical in the homotopy/derived category, with a specified homotopy where strict commutation fails.

Nothing in this proof gives an equivariant section \(Q_{\rm cen}\to\mathcal A\) or \(Q_{\rm raw}\to A\). The inverse in (CTF5.5) has codomain the other quotient, not a test space. The contraction is of the explicit intermediate cone of an isomorphism of quotients. A strict equivariant inverse to \(\Gamma\), \(\Pi_D\), or \(\Xi\) on the original complexes is not used.

## CTF7. Faithful source extension and its retained identity cone

DCP8 supplies the actual extra closed copies
\[
V=V_+\oplus V_-,
\]
as degree-zero terms, where each \(V_\pm=S\oplus\mathbb C^2\) retains its complete Schwartz component and its two labelled endpoint coordinates. Define exactly
\[
C_{\rm full}=C^{\rm or}\oplus V[0],\quad
D_{\rm full}=D\oplus V[0],\quad
F_{\rm full}=F_{\rm sym}\oplus\mathrm{id}_{V[0]}.
\tag{CTF7.1}
\]
The target is precisely the global Cech complex of DCP8–DCP9 after ordering the summands by their receiving idempotents.
The source is the displayed faithful extension of the original \(C^{\rm or}\); no identification of a different geometric derived source with this extension is presumed.

The global receiving ring is \(\mathbb Z^3\). A triple \((r,b_+,b_-)\) acts by scalar \(r\) on the original \(C,D\) summands and by \(b_+,b_-\) on the two respective copies in \(V\). Thus
\[
[\tau]=(1,1,1)\text{ acts as identity},\qquad
[n]=(n,0,0)\text{ acts as scalar }n\text{ on }C,D
\text{ and as zero on }V.
\tag{CTF7.2}
\]
These actions preserve every differential and the comparison. They are faithful as actions of the supplied source monoid: distinct integers act differently on the original nonzero complex coefficient spaces; \(\tau\) acts differently from each integer on the nonzero extra closed copies. No source addition on \(\tau\) is defined.

The real action on \(V_+\) is \(\rho_+(a)\) and on \(V_-\) is \(\rho_-(a)\), exactly as in (CTF3.1). The mirror on \(V\) is
\[
w_V(v_+,v_-)=(v_-,v_+),
\tag{CTF7.3}
\]
using the original identification of the two typed copies. It is semilinear for the receiving ring swap \((r,b_+,b_-)\mapsto(r,b_-,b_+)\), and fixes every supplied source element (CTF7.2). It retains
\(\rho_V(a)w_V=a\,w_V\rho_V(a^{-1})\), checked on the Schwartz terms and on each endpoint coordinate using the original actions. There is no extra cone-orientation sign on this degree-zero identity comparison. The oriented action on \(C^{\rm or}\) remains the one in CTF1.
The diagonal rational action on these already periodized \(V\) coefficients is trivial, as it is on the original \(D\) coefficients; it is not the independent real spectral dilation.

Set
\[
H_{C,\rm full}=H_C\oplus V[0],\quad
H_{D,\rm full}=H_D\oplus V[0],
\]
\[
\Gamma_{\rm full}=\Gamma\oplus\mathrm{id}_V,\quad
\Pi_{D,\rm full}=\Pi_D\oplus\mathrm{id}_V,\quad
\beta_{\rm full}=\beta\oplus\mathrm{id}_V.
\tag{CTF7.4}
\]
All maps are receiving-ring linear, equivariant for the source action, real action, full diagonal rational action and the mirror, and
\[
\Pi_{D,\rm full}F_{\rm full}=\beta_{\rm full}\Gamma_{\rm full}
\]
strictly. Both vertical maps are quasi-isomorphisms.

The componentwise regrouping gives the exact cone isomorphism
\[
\operatorname{Cone}(F_{\rm full})
\cong K\oplus\operatorname{Cone}(\mathrm{id}_{V[0]}).
\tag{CTF7.5}
\]
The added cone has \(V_{\rm source}\) in degree \(-1\), \(V_{\rm target}\) in degree zero, and differential \(+\mathrm{id}_V\). This follows directly from the retained formula
\(d(v,c)=(d_Dv+Fc,-d_Cc)\): \(d_V=0\), so the off-diagonal identity has positive sign.
Its contracting homotopy is
\[
h_V^0:V_{\rm target}\to V_{\rm source},\quad h_V^0(v)=v,
\qquad h_V^j=0\ (j\ne0),
\]
and satisfies \(d h_V+h_Vd=\mathrm{id}\) in both degrees. Because both copies carry exactly the same actions, this contraction is receiving-ring linear and equivariant, including the mirror swap of \(V_+\) and \(V_-\).

In the intermediate full cone, take \(h_{\rm full}=h\oplus h_V\), \(p_{\rm full}=p\oplus0\), and \(i_{\rm full}=i\oplus0\). Equation (CTF5.6) holds with these full maps and the same final target \(E\). The resulting exact original-cone projection is
\[
\begin{aligned}
\Pi_{\rm full}^0(v,w_{\rm target},k)&=\Pi_D^0v,\\
\Pi_{\rm full}^{-1}(c,w_{\rm source})&=\Gamma^0c,\\
\Pi_{\rm full}^{-n}(c)&=\Gamma^{1-n}c\quad(n\ge2),\\
\Pi_{\rm full}^{1}&=0 .
\end{aligned}
\tag{CTF7.6}
\]
The receiving-ring action on the resulting \(E\) is through its arithmetic coordinate \(r\); this describes the cone comparison, not the action on either full source object. In particular the extra \(V\) terms are still present in both full objects and in both cohomology complexes in (CTF7.4). They disappear only from their identity cone by the displayed contraction. Thus the full objects retain the faithful distinction \(\tau\ne1\).

The full triangle's last square has the same explicit homotopy as CTF6, with the additional component
\[
\eta_{\rm full}^0(v,w_{\rm target},k)
=(0,w_{\rm target})\in H_{C,\rm full}[1]^{-1}
=B_1\oplus V.
\tag{CTF7.7}
\]
Its degree-one component is still
\(\eta_{\rm full}^1(b)=\overline{\mathcal T}^{-1}\pi_{\rm raw}(b)\).
On a degree-\(-1\) cone cochain, the differential sends the extra source copy \(w_{\rm source}\) to \(+w_{\rm source}\) in the target copy, so (CTF7.7) returns it with positive sign. This is exactly the difference between the full cone projection to \(H_{C,\rm full}[1]\) and the map through \(E\). In degree zero the difference is still \(\pi_{\rm cen}k\). Every other degree agrees strictly. This verifies all cone and connecting signs in the faithful triangle as well.

## CTF8. Exact resulting statement

The original oriented comparison admits the explicit equivariant quasi-isomorphism
\[
\boxed{\operatorname{Cone}(F_{\rm sym})
\xrightarrow{\Pi_K}
H^0(D)[0]\oplus\bigoplus_{n\ge1}
(\Lambda^nW_{\rm pr}\otimes\mathbb C^2)[n].}
\tag{CTF8.1}
\]
Its degree-zero Fourier graph, all four original endpoint lines, every original prime wedge, and both moment coordinates survive with their specified real actions and mirror signs. Its full faithful extension has the same cone model by (CTF7.5)–(CTF7.6), while retaining the extra complete closed copies in both compared objects.

This proves formality of the specified whole comparison triangle in the derived representation category, with a strict comparison square, explicit cone map, and the displayed final-arrow homotopy. It strengthens the earlier statement that no derived splitting of this cone had yet been proved. It does not assert a strict equivariant homotopy inverse on the original test complexes, a lift of \(Q\) into a strong test space, or a new weight/purity theorem. The surviving original-zeta quotient is identified by its full factor-preserving source map; no completed replacement, missing multiplicity, or extra source operation on \(\tau\) enters the argument.

## Complete supported duality and original-zeta trace - 24 September 2026

The full continuation is ACTUAL_SUPPORTED_DUALITY_INDEPENDENT.md ASD0–ASD14, GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md GZR0–GZR9, and ORIGINAL_ZETA_JACOBIAN_TRACE_BRIDGE.md JTB0–JTB8. The original Fréchet coefficient complex now has its explicit continuous-dual localization row, with all faithful extra closed copies and every orientation sign. Its residue pairing is a pair of absolutely convergent integrals with the original denominator zeta(s); it descends to the entire actual quotient and detects every multiplicity jet. The exact derivative operator maps this pairing to the existing Weil form, with the original pole correction and full Gamma factors retained.

ASD14 constructs the resulting actual chain map into the character-a-twisted shifted dual and computes its complete cone. Its spectral cokernel is Q′/D_L(Q); weak-* density makes its Hausdorff quotient zero but is not treated as algebraic surjectivity. The original H0 and its continuous dual remain in the cone. This strengthens the explicit duality comparison without declaring a Verdier isomorphism, numerical purity or an RH proof. Current source Z_0, Z_1/tau and integer Z_2 data are unchanged; no tau addition is introduced. The complete relevant user corpus and later corrections were checked before interpreting these maps.

## Explicit global continuation: finite lifting and a nonzero remainder

The earlier uncertainty about algebraic surjectivity is now resolved by GLOBAL_POLYNOMIAL_DUAL_DEFECT.md PGD1–PGD6, independently checked in PGC0–PGC7: the actual algebraic cokernel is nonzero. Its explicit class c_zeta is the original-zeta contour functional with the constant arithmetic function 1 in the first slot. A lift would require a rapidly decreasing entire representative to equal 1 at all actual zeros, which the proved unbounded zero heights exclude. PGD constructs an injected rational-function line, entire representatives retaining all Hermite pole corrections, and the whole real/prime orbit. This is a receiving cokernel class, not primitive tau or a claimed off-critical zero.

SCL0–SCL9 and DPL0–DPL9 prove every nonzero polynomial in the actual cokernel generator invertible. Thus all finite-dimensional invariant dual spaces lift uniquely, continuously and with the original real/prime action. DPL gives explicit extension splittings and computes every degree of the cyclic derived Hom into the actual cone. These results retain its H and H′ terms, all faithful closed copies and support labels. The weak-* Hausdorff quotient remains zero alongside the now proved nonzero algebraic quotient. Current source Z_0, Z_1/tau and Z_2 are unchanged. Complete proofs and exact human citations are in the linked continuation files; the full geometric weight-separation goal remains active.
