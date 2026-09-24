# Arithmetic and Fourier actions on the prime-indexed endpoint defect

Independent derivation and exact comparison with the earlier FR calculation, 24 September 2026. Proof locators CSB0–CSB10.

## CSB0. The input stage and the source-domain distinction

This calculation continues CS2A of CC_SHEAF_ORIGINAL_ZETA_COHOMOLOGY.md. It concerns the already constructed adèlic coefficient spaces over \(\mathbb Q\), their rational scaling relations, and the explicit alternative quotient produced by restricting the generating domain of those relations. The prime labels and their valuations belong to this arithmetic stage. No arithmetic operation, vector, metric, or coordinate is introduced on \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\).

The earlier programme source ORIGINAL_ZETA_RETURN_FR.tex, FR15–FR25, already proves the algebraic spherical decomposition with two endpoint directions at every prime. That proof slice and its bibliography were read during this continuation. CSB10 proves the exact coordinate comparison, including its opposite rational-scaling convention and the distinction between its periodization seminorm and the stronger source topology here. The decomposition is not claimed as new. The older text's separate base and supported-zero conventions are not imported into the current user construction.

Before this calculation, the current READ_FIRST_USER_CONSTRUCTION.md, the correction-precedence table and active-target sections of USER_ARGUMENT_RECONSTRUCTION.md, the complete current PREREQUISITE_AND_OBSTRUCTION_CHECKS.md, and verbatim WU061–WU062 were read. The connected reconstruction and pertinent earlier corrections had already been read for CS0. The governing distinctions remain: retain complete-history reconstruction before arithmetic labels, preserve both branch counters separately, retain the carried stalk data, and derive the actual lifting mechanism rather than assigning a desired weight.

The original source is Connes–Consani, *Schemes over \(\mathbb F_1\) and zeta functions*, [arXiv:0903.2024v3](https://arxiv.org/abs/0903.2024v3), retained author file sources/CC_0903_2024_v3/author_source/announc3.tex. The relevant exact definitions were read in section 5, source lines 1376–1667. This continuation uses fonction1–fonction3, fourier, poisson2, rep1, liftw and compinv; fonction1–fonction3 were reread for the generating-domain check.

The source's fonction3 does not explicitly type its generating \(f\). CS uses the full-difference reading compatible with the stated Fourier-graph theorem and separately proves what happens under the null-generated alternative. This note preserves that textual qualification. Its subject is the exact mathematical relationship between those two written quotient definitions.

Use
\[
\mathcal S=\mathcal S(\mathbb A_{\mathbb Q}),\qquad
\epsilon(F)=\left(F(0),\int_{\mathbb A_{\mathbb Q}}F(x)\,dx\right),
\qquad E=\ker\epsilon.
\tag{CSB0.1}
\]
The topology is the adèlic Bruhat–Schwartz LF topology: on each fixed finite-place test-function stage it is a finite direct sum of real Schwartz spaces. At the finite places the additive Haar measure has
\(\operatorname{vol}(\widehat{\mathbb Z})=1\).
For \(q\in\mathbb Q^\times\), set
\[
(\mathsf D_qF)(x)=F(qx),\qquad r_q=I-\mathsf D_q.
\tag{CSB0.2}
\]
The product formula gives \(\epsilon(\mathsf D_qF)=\epsilon(F)\), so \(r_q\mathcal S\subset E\). Define
\[
\mathcal R_{\mathrm{full}}
=\operatorname{span}\{r_qF:F\in\mathcal S,\ q\in\mathbb Q^\times\},
\quad
\mathcal R_{\mathrm{null}}
=\operatorname{span}\{r_qF:F\in E,\ q\in\mathbb Q^\times\},
\]
\[
D_{\mathrm{full}}=E/\overline{\mathcal R_{\mathrm{full}}},
\qquad
D_{\mathrm{null}}=E/\overline{\mathcal R_{\mathrm{null}}}.
\tag{CSB0.3}
\]
Closures are taken in \(E\). Their natural quotient map is denoted
\(\pi:D_{\mathrm{null}}\to D_{\mathrm{full}}\).

For \(K=\widehat{\mathbb Z}^{\times}\), let \(P_K\) be normalized Haar averaging in the finite coordinates. Every \(P_KF\) has a unique finite expansion
\[
P_KF=\sum_d f_d\otimes1_{d\widehat{\mathbb Z}},
\qquad d\in\mathbb Q_{>0}.
\tag{CSB0.4}
\]
CS2 proves existence and uniqueness by finite products of nested local balls. Put
\[
\ell_p(F)=\sum_d v_p(d)
\left(f_d(0),\,d^{-1}\int_{\mathbb R}f_d(v)\,dv\right),\qquad
\mathscr L(F)=(\ell_p(F))_p,
\qquad
V=\bigoplus_{p\ {\rm prime}}\mathbb C^2.
\tag{CSB0.5}
\]
The direct sum has its locally convex direct-sum topology. Each test-function stage involves finitely many relevant \(p,d\), so \(\mathscr L:\mathcal S\to V\) is continuous. CS2A proves
\[
\ell_p(\mathsf D_qF)=\ell_p(F)-v_p(|q|)\epsilon(F),
\tag{CSB0.6}
\]
and consequently \(\mathscr L\) descends to \(D_{\mathrm{null}}\).
Its complete topological splitting is
\[
\Phi:D_{\mathrm{null}}\xrightarrow{\ \sim\ }D_{\mathrm{full}}\oplus V,
\qquad
[F]_{\mathrm{null}}\longmapsto([F]_{\mathrm{full}},\mathscr LF).
\tag{CSB0.7}
\]
CSB4 below restates the explicit inverse and computes its equivariance. In particular \(V\) denotes these extra prime-indexed directions; it does not denote either of the two original endpoint lines on either chart.

## CSB1. Fourier transformation with the finite volume factor retained

Choose the self-dual character and measures with real Fourier transform
\[
\widehat f(t)=\int_{\mathbb R}f(v)e^{-2\pi ivt}\,dv.
\tag{CSB1.1}
\]
At the finite places, the annihilator of \(d\widehat{\mathbb Z}\) is \(d^{-1}\widehat{\mathbb Z}\). Integration of its character is its volume when the character is trivial and zero otherwise. Therefore
\[
\widehat{1_{d\widehat{\mathbb Z}}}
=d^{-1}1_{d^{-1}\widehat{\mathbb Z}},\qquad
\widehat{f\otimes1_{d\widehat{\mathbb Z}}}
=d^{-1}\widehat f\otimes1_{d^{-1}\widehat{\mathbb Z}}.
\tag{CSB1.2}
\]
The factor \(d^{-1}\) is the full finite additive volume.

For the original tensor, write
\[
a=f(0),\qquad b=d^{-1}\int_{\mathbb R}f(v)\,dv.
\]
The transformed tensor has endpoint pair \((b,a)\), since
\[
d^{-1}\widehat f(0)=b,\qquad
(d^{-1})^{-1}\int_{\mathbb R}d^{-1}\widehat f(t)\,dt=a.
\tag{CSB1.3}
\]
Its ball label is \(d^{-1}\), hence its \(p\)-valuation is \(-v_p(d)\).
With
\[
J(a,b)=(b,a),\qquad S_V=-J,
\tag{CSB1.4}
\]
we obtain the exact identity
\[
\boxed{\ell_p(\widehat F)=-J\ell_p(F),\qquad
\mathscr L\widehat F=S_V\mathscr LF.}
\tag{CSB1.5}
\]
Here \(J,S_V\) act componentwise on the prime labels. To extend the calculation beyond the \(K\)-invariant tensors, observe that Fourier transformation exchanges finite unit scaling by \(k\) with scaling by \(k^{-1}\); the module of such a unit is one. Inversion preserves Haar measure on \(K\), so Fourier transformation commutes with \(P_K\).

Fourier transformation interchanges the two endpoint functionals, and hence preserves \(E\). Rational scaling satisfies
\[
\widehat{\mathsf D_qF}=\mathsf D_{q^{-1}}\widehat F.
\tag{CSB1.6}
\]
At \(q=p\), the real Fourier scalar is \(p^{-1}\), while the finite scalar is \(p\); their product is one, as required by \(|p|_{\mathbb A}=1\). It follows that Fourier transformation preserves both relation spaces in (CSB0.3) and their closures. Its square is \(\mathsf D_{-1}\), which is the identity on both quotients. Thus it gives continuous involutions \(\mathcal F_{\mathrm{full}}\) and \(\mathcal F_{\mathrm{null}}\).

Under (CSB0.7) their relationship is
\[
\boxed{
\Phi\mathcal F_{\mathrm{null}}\Phi^{-1}(x,v)
=(\mathcal F_{\mathrm{full}}x,-Jv).
}
\tag{CSB1.7}
\]
On each extra \(\mathbb C^2\), the Fourier \(+1\) eigenspace is \(\{(c,-c)\}\), and the Fourier \(-1\) eigenspace is \(\{(c,c)\}\). These signs follow from the inverted valuation, rather than from an omitted Fourier volume.

## CSB2. The full unshifted arithmetic action

For \(a>0\), use the source actions on the real coordinate
\[
A_+(a)F(v,x_f)=F(v/a,x_f),\qquad
A_-(a)F(v,x_f)=aF(av,x_f)
=aA_+(a^{-1})F(v,x_f).
\tag{CSB2.1}
\]
They commute with rational scaling, preserve \(E\), and continuously preserve the two relation closures. On each fixed real Schwartz seminorm, a fixed dilation multiplies the bound by an explicit power of \(a\); on the finite component it is the identity. Thus all induced quotient operators are continuous.

On the endpoint pair their matrices are
\[
B_+(a)=
\begin{pmatrix}1&0\\0&a\end{pmatrix},\qquad
B_-(a)=
\begin{pmatrix}a&0\\0&1\end{pmatrix}.
\tag{CSB2.2}
\]
For a ball tensor, real dilation changes neither \(d\) nor \(v_p(d)\); evaluation at zero and change of variables in the real integral give
\[
\boxed{
\ell_p(A_+(a)F)=B_+(a)\ell_p(F),\qquad
\ell_p(A_-(a)F)=B_-(a)\ell_p(F).
}
\tag{CSB2.3}
\]
The same equations hold after \(K\)-averaging. Finite units act trivially on \(V\). Every idèle class has its representative \((a,k)\in\mathbb R_{>0}\times K\), as proved in CS1.3. Therefore the full idèle-class action on \(V\) depends only on its module \(a\), and is exactly (CSB2.2). Rational changes of representative act identically on \(D_{\mathrm{null}}\), since their arguments lie in \(E\). The term \(v_p(q)\epsilon(F)\) in (CSB0.6) is consequently zero at this quotient stage.

The splitting (CSB0.7) therefore intertwines both chart actions:
\[
\Phi A_\pm(a)\Phi^{-1}(x,v)
=\bigl(A_{\pm,\mathrm{full}}(a)x,\ B_\pm(a)v\bigr).
\tag{CSB2.4}
\]
Fourier transformation exchanges the two chart actions:
\[
\widehat{A_+(a)F}=A_-(a)\widehat F,\qquad
S_VB_+(a)=B_-(a)S_V.
\tag{CSB2.5}
\]
All factors in \(A_-(a)=aA_+(a^{-1})\) have been retained.

For every positive integer \(n\), the plus-chart arithmetic and integral transfer matrices on an extra endpoint pair are
\[
F_n^{(+)}=B_+(n)=
\begin{pmatrix}1&0\\0&n\end{pmatrix},\qquad
V_n^{(+)}=nB_+(n^{-1})=
\begin{pmatrix}n&0\\0&1\end{pmatrix},
\]
\[
F_n^{(-)}=B_-(n)=
\begin{pmatrix}n&0\\0&1\end{pmatrix},\qquad
V_n^{(-)}=nB_-(n^{-1})=
\begin{pmatrix}1&0\\0&n\end{pmatrix}.
\tag{CSB2.6}
\]
Thus \(F_n^{(\pm)}V_n^{(\pm)}=nI\), all the multiplicative relations hold, and these matrices preserve
\(\bigoplus_p\mathbb Z^2\subset V\).
The prime label \(p\) of a defect component is not changed by an arithmetic operator indexed by \(n\). Fourier acts on this same lattice by \(-J\).

Differentiating at \(a=e^t\), \(t=0\), gives the actual infinitesimal matrices
\[
L_{V,+}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
L_{V,-}=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\tag{CSB2.7}
\]
Their dilation exponents are exactly 0 and 1, with no nilpotent contribution. They satisfy \(L_{V,\pm}(L_{V,\pm}-I)=0\). In the convention in which a Tate character \(a^r\) is assigned weight \(2r\), these are the two characters with labels 0 and 2. Equation (CSB2.7), rather than a new finite-field Frobenius assumption, is the statement proved here.

## CSB3. The Gaussian endpoint section and its exact source defect

Let \(g(v)=e^{-\pi v^2}\) and define a continuous endpoint section
\[
\sigma(c,d)(v,x_f)=
\left[c(1-2\pi v^2)+d\,2\pi v^2\right]g(v)
\,1_{\widehat{\mathbb Z}}(x_f).
\tag{CSB3.1}
\]
The Gaussian identities
\(\int g=1\) and \(\int v^2g=1/(2\pi)\) prove
\(\epsilon(\sigma(c,d))=(c,d)\).
In the real Fourier convention (CSB1.1),
\[
\widehat g=g,\quad
\widehat{2\pi v^2g}=(1-2\pi t^2)g(t),\quad
\widehat{(1-2\pi v^2)g}=2\pi t^2g(t).
\tag{CSB3.2}
\]
Together with the finite ball identity at \(d=1\), these give
\[
\boxed{\widehat{\sigma(c,d)}=\sigma(d,c)=\sigma(J(c,d)).}
\tag{CSB3.3}
\]
The chosen Gaussian endpoint section itself is exactly Fourier equivariant.

The source representative used in CS2A is
\[
\mathscr T(v)=\sum_p r_p\sigma(v_p)\in\mathcal R_{\mathrm{full}}
\subset E,\qquad \mathscr L\mathscr T(v)=v.
\tag{CSB3.4}
\]
Every sum is finite. The locally convex direct-sum topology makes this map continuous: its restriction to each finite-dimensional prime component is continuous into a fixed adèlic Schwartz stage.

Equations (CSB1.6) and (CSB3.3) show
\[
\widehat{\mathscr T(v)}
=\sum_p r_{p^{-1}}\sigma(Jv_p).
\tag{CSB3.5}
\]
The required action on \(V\) is \(-J\), so the source-level defect is
\[
\begin{aligned}
\widehat{\mathscr T(v)}-\mathscr T(-Jv)
&=\sum_p(r_{p^{-1}}+r_p)\sigma(Jv_p)\\
&=\sum_p r_p r_{p^{-1}}\sigma(Jv_p)\\
&=\sum_p\left(
2\sigma(Jv_p)-\mathsf D_p\sigma(Jv_p)
-\mathsf D_{p^{-1}}\sigma(Jv_p)\right).
\end{aligned}
\tag{CSB3.6}
\]
The middle equality uses \(\mathsf D_p\mathsf D_{p^{-1}}=I\).
The function \(r_{p^{-1}}\sigma(Jv_p)\) is moment-null, because rational scaling preserves both endpoint functionals. Hence every term in the middle line belongs to \(\mathcal R_{\mathrm{null}}\), without taking a closure. The induced section
\[
\iota:V\longrightarrow D_{\mathrm{null}},\qquad
\iota(v)=[\mathscr T(v)]_{\mathrm{null}}
\tag{CSB3.7}
\]
is already exactly Fourier equivariant, even though its displayed Schwartz representative has the nonzero defect (CSB3.6).

An explicit representative which is Fourier equivariant before quotienting is
\[
\boxed{
\mathscr T_{\mathrm{eq}}(v)
=\frac12\sum_p
\left(\mathsf D_{p^{-1}}\sigma(v_p)-\mathsf D_p\sigma(v_p)\right).
}
\tag{CSB3.8}
\]
Its endpoint pair vanishes term by term. Equation (CSB0.6) gives
\[
\ell_q(\mathsf D_{p^{-1}}\sigma(v_p))=\delta_{pq}v_p,\qquad
\ell_q(\mathsf D_p\sigma(v_p))=-\delta_{pq}v_p,
\]
\[
\mathscr L\mathscr T_{\mathrm{eq}}=\mathrm{id}_V,\qquad
\widehat{\mathscr T_{\mathrm{eq}}(v)}
=\mathscr T_{\mathrm{eq}}(-Jv).
\tag{CSB3.9}
\]
In the second identity use (CSB1.6) to exchange the two rational dilations, and (CSB3.3) to interchange the endpoint pair.
It represents the same quotient section, since
\[
\mathscr T_{\mathrm{eq}}(v)-\mathscr T(v)
=-\frac12\sum_p r_p r_{p^{-1}}\sigma(v_p)
\in\mathcal R_{\mathrm{null}}.
\tag{CSB3.10}
\]
The factor \(1/2\), both rational scales, and the sign of their difference are part of the actual formula.

For completeness, the chosen representatives also have exact dilation defects. Define
\[
\Delta_{\pm,a}(w)=A_\pm(a)\sigma(w)-\sigma(B_\pm(a)w)\in E.
\tag{CSB3.11}
\]
The zero endpoint assertion follows from (CSB2.2). If \(w=(c,d)\), their real components, with the common finite factor \(1_{\widehat{\mathbb Z}}\), are
\[
\begin{aligned}
\Delta_{+,a}(c,d)(v)
={}&\left[c(1-2\pi v^2/a^2)+d\,2\pi v^2/a^2\right]
e^{-\pi v^2/a^2}\\
&-\left[c(1-2\pi v^2)+ad\,2\pi v^2\right]e^{-\pi v^2},
\end{aligned}
\]
\[
\begin{aligned}
\Delta_{-,a}(c,d)(v)
={}&a\left[c(1-2\pi a^2v^2)+d\,2\pi a^2v^2\right]
e^{-\pi a^2v^2}\\
&-\left[ac(1-2\pi v^2)+d\,2\pi v^2\right]e^{-\pi v^2}.
\end{aligned}
\tag{CSB3.12}
\]
Commutation with rational scaling gives
\[
A_\pm(a)\mathscr T(v)-\mathscr T(B_\pm(a)v)
=\sum_p r_p\Delta_{\pm,a}(v_p)
\in\mathcal R_{\mathrm{null}},
\]
\[
A_\pm(a)\mathscr T_{\mathrm{eq}}(v)
-\mathscr T_{\mathrm{eq}}(B_\pm(a)v)
=\frac12\sum_p(r_p-r_{p^{-1}})\Delta_{\pm,a}(v_p)
\in\mathcal R_{\mathrm{null}}.
\tag{CSB3.13}
\]
These are exact differences of actual source functions. They prove dilation equivariance of the same quotient section without claiming that its Gaussian representative is fixed by every dilation.

## CSB4. The canonical quotient splitting and its inverse

The continuous inverse of \(\Phi\) in (CSB0.7) is
\[
\Phi^{-1}([F]_{\mathrm{full}},v)
=\left[F-\mathscr T\mathscr LF+\mathscr T v\right]_{\mathrm{null}}.
\tag{CSB4.1}
\]
Here \(F\in E\). The CS2A relation
\((I-\mathscr T\mathscr L)\overline{\mathcal R_{\mathrm{full}}}
\subset\overline{\mathcal R_{\mathrm{null}}}\)
makes the formula independent of \(F\). It also proves continuity through the defining quotient topology. Replacing \(\mathscr T\) by \(\mathscr T_{\mathrm{eq}}\) gives exactly the same quotient map by (CSB3.10).

Thus the exact sequence
\[
0\longrightarrow V\xrightarrow{\ \iota\ }
D_{\mathrm{null}}\xrightarrow{\ \pi\ }D_{\mathrm{full}}
\longrightarrow0
\tag{CSB4.2}
\]
has section
\[
s_0([F]_{\mathrm{full}})
=\left[F-\mathscr T\mathscr LF\right]_{\mathrm{null}},
\qquad \mathscr Ls_0=0.
\tag{CSB4.3}
\]
This is the unique section whose image lies in \(\ker\mathscr L\).
The coordinate transformation identities (CSB1.5) and (CSB2.3) prove that both \(\iota\) and \(s_0\) intertwine Fourier transformation and both chart actions, with precisely the matrices already computed.

The quotient section \(\iota\) does not depend on the Gaussian endpoint section. If \(\sigma'\) is another linear endpoint section, then
\(\epsilon((\sigma-\sigma')w)=0\), and
\[
\sum_p r_p(\sigma-\sigma')(v_p)\in\mathcal R_{\mathrm{null}}.
\tag{CSB4.4}
\]
Consequently both choices give the same \(\iota\), and therefore the same \(s_0\). The explicit Gaussian formulas provide representatives of an already well-defined quotient splitting.

## CSB5. The alternative sheaf and its entire cohomology

Let \(X=\{0,\eta,\infty\}\) have the same three-point topology as CS4:
\(U_+=\{0,\eta\}\), \(U_-=\{\eta,\infty\}\), and
\(U=U_+\cap U_-=\{\eta\}\).
On the trivial \(K\)-sector put
\[
S_0=\{f\in\mathcal S(\mathbb R):
f(-v)=f(v),\ f(0)=0,\ \int_{\mathbb R}f=0\}.
\tag{CSB5.1}
\]
CS2 and CS2A identify
\[
D_{\mathrm{full}}^K\simeq S_0,\qquad
D_{\mathrm{null}}^K\simeq S_0\oplus V
\tag{CSB5.2}
\]
topologically. In these coordinates Fourier acts by
\((f,v)\mapsto(\widehat f,-Jv)\).

Retain four original endpoint lines,
\[
E_+=\mathbb Ce_{+,0}\oplus\mathbb Ce_{+,1},\qquad
E_-=\mathbb Ce_{-,0}\oplus\mathbb Ce_{-,1}.
\tag{CSB5.3}
\]
The alternative chart section spaces are
\[
\widetilde A_+=S_0\oplus V_+\oplus E_+,\qquad
\widetilde A_-=S_0\oplus V_-\oplus E_-,
\tag{CSB5.4}
\]
where \(V_+,V_-\) are independent chart-labelled copies of \(V\).
The overlap is the same weighted smooth space
\[
H=\{h:\sup_{u>0}(u^N+u^{-N})
|(u\partial_u)^jh(u)|<\infty\text{ for all }N,j\ge0\}.
\tag{CSB5.5}
\]
The actual restrictions are
\[
\widetilde r_+(f,v_+,e_+)=Sf,\qquad
\widetilde r_-(h,v_-,e_-)=RSh=S\widehat h,
\]
\[
Sf(u)=\sum_{q\in\mathbb Q^\times}
f(qu)1_{\widehat{\mathbb Z}}(q)
=2\sum_{n\ge1}f(nu),\qquad
Rg(u)=u^{-1}g(1/u).
\tag{CSB5.6}
\]
The restrictions of the original endpoints vanish by their source definition. Those of \(V_\pm\) vanish because each representative \(r_p\sigma(v_p)\) has zero rational sum by reindexing. Absolute convergence of that sum for every idèle justifies the reindexing; one does not claim that the separate non-null Gaussian generators lie in the rapidly decreasing overlap.

Define global sections as the fibre product of the two chart restrictions. This constructs a sheaf \(\widetilde{\mathscr F}\) exactly as in CS4. The splitting in CSB4 supplies the explicit sheaf isomorphism
\[
\boxed{
\widetilde{\mathscr F}
\simeq\mathscr F
\oplus i_{0*}V_+
\oplus i_{\infty*}V_-.
}
\tag{CSB5.7}
\]
Here \(i_{0*}V_+\) means the sheaf with sections \(V_+\) on an open containing 0 and zero on any other open; the definition for \(\infty\) is analogous. On the overlap the isomorphism is the identity. On a chart it is exactly the quotient splitting (CSB0.7), together with its original endpoint summands. Thus (CSB5.7) is a map of the actual restrictions, not just an equality of dimensions.

For any sheaf with the corresponding full adèlic source coordinates, the same splitting argument gives its alternative as the original sheaf direct-summed with these two endpoint-supported sheaves. This statement does not require an additional injectivity theorem for the full adèlic summation map.

Use the ordered Čech differential
\[
\widetilde d(a,b)=\widetilde r_+a-\widetilde r_-b.
\tag{CSB5.8}
\]
CS3 proves \(S\) is injective on \(S_0\), and Poisson proves \(RS=S\widehat{\ }\). Therefore the complete degree-zero cohomology is
\[
\boxed{
H^0(X,\widetilde{\mathscr F})
=\left\{
\bigl((f,v_+,e_+),(\widehat f,v_-,e_-)\bigr):
f\in S_0,\ v_\pm\in V_\pm,\ e_\pm\in E_\pm
\right\}.
}
\tag{CSB5.9}
\]
In particular the two prime-indexed copies are unrestricted and independent. Replacing this formula by only the Fourier graph of \(D_{\mathrm{null}}^K\) would discard one full copy of \(V\).

If \(J_0=S(S_0)\subset H\), then
\[
\boxed{
H^1_{\mathrm{alg}}(X,\widetilde{\mathscr F})=H/J_0
=H^1_{\mathrm{alg}}(X,\mathscr F),
\quad
H^1_{\mathrm{Haus}}(X,\widetilde{\mathscr F})=H/\overline{J_0}
=H^1_{\mathrm{Haus}}(X,\mathscr F).
}
\tag{CSB5.10}
\]
The equalities are induced by the identity on \(H\), with the same images and quotient topologies. Higher cohomology vanishes. This follows either from the same two-term complex proof as CS5, or from (CSB5.7), since global sections of an endpoint-supported summand are the exact functor returning its vector space.

## CSB6. Fourier, Weyl, and every chart-labelled endpoint action

In the coordinates of (CSB5.9), positive real scaling is
\[
\begin{aligned}
\rho(a)(f,v_+,v_-,e_+,e_-)
=\bigl(&A_+(a)f,\ B_+(a)v_+,\ B_-(a)v_-,\\
&B_+(a)e_+,\ B_-(a)e_-\bigr).
\end{aligned}
\tag{CSB6.1}
\]
On \(E_\pm\), the matrices refer to the ordered coordinates evaluation and integral. The minus main coordinate is automatically
\(\widehat{A_+(a)f}=A_-(a)\widehat f\).

For every prime \(p\), write \(v_{+,p}=(c_{+,p},d_{+,p})\),
\(v_{-,p}=(c_{-,p},d_{-,p})\), and write
\(e_\pm=(c_\pm,d_\pm)\) for the original endpoints. The full list is
\[
\begin{array}{c|cccc}
\text{original line}&c_+&d_+&c_-&d_-\\ \hline
\rho(a)&1&a&a&1
\end{array}
\qquad
\begin{array}{c|cccc}
\text{extra line at }p&c_{+,p}&d_{+,p}&c_{-,p}&d_{-,p}\\ \hline
\rho(a)&1&a&a&1.
\end{array}
\tag{CSB6.2}
\]
There are four original endpoint lines in total and four extra lines for each prime. The repeated character values do not identify any of these labelled lines.

The source Weyl lift exchanges the two chart sections by the identity. Therefore on degree zero it is
\[
\boxed{
W^0(f,v_+,v_-,e_+,e_-)
=(\widehat f,v_-,v_+,e_-,e_+).
}
\tag{CSB6.3}
\]
In particular Weyl exchanges the independent prime-indexed copies without inserting \(-J\) in this chart-swap formula. Fourier transformation of a single source fibre, which does act by \(-J\), is a different map.

On the ordered degree-one Čech cochains the Weyl action remains
\[
W^1g=-Rg,\qquad
\widetilde d\,W^0=-R\,\widetilde d.
\tag{CSB6.4}
\]
The additional summands restrict to zero and introduce no new sign in this identity. In every degree the unshifted relation is
\[
\rho(a)W=aW\rho(a^{-1}).
\tag{CSB6.5}
\]
On the extra coordinates it says
\(B_+(a)=aB_-(a^{-1})\) and
\(B_-(a)=aB_+(a^{-1})\), which follow directly from (CSB2.2).

The Fourier graph inside the extra pair is
\[
G_V=\{(v_+,v_-)=(v,-Jv):v\in V\}.
\tag{CSB6.6}
\]
Its complementary opposite graph is
\[
A_V=\{(v_+,v_-)=(w,Jw):w\in V\}.
\tag{CSB6.7}
\]
The exact decomposition of arbitrary independent coordinates is
\[
g=\tfrac12(v_+-Jv_-),\qquad
h=\tfrac12(v_++Jv_-),\qquad
(v_+,v_-)=(g+h,-Jg+Jh).
\tag{CSB6.8}
\]
Both summands carry the plus-chart dilation matrix \(B_+(a)\), because
\(JB_-(a)=B_+(a)J\). Their Weyl actions are respectively
\[
g\longmapsto-Jg,\qquad h\longmapsto Jh.
\tag{CSB6.9}
\]
These identities explain exactly how the single-fibre Fourier sign is recovered on the Fourier-graph subspace, while the full cohomology still retains the independent opposite graph. The four original endpoint lines remain separately present as in (CSB6.2).

## CSB7. Supported maps and the split extension

The supported complexes for the alternative sheaf, with positive local restriction differentials, are
\[
\widetilde L_0=[\widetilde A_+\xrightarrow{\widetilde r_+}H],
\qquad
\widetilde L_\infty=[\widetilde A_-\xrightarrow{\widetilde r_-}H].
\tag{CSB7.1}
\]
Consequently
\[
H^0_{\{0\}}=V_+\oplus E_+,\qquad
H^0_{\{\infty\}}=V_-\oplus E_-,
\]
\[
H^1_{\{0\}}=H/J_0,\qquad
H^1_{\{\infty\}}=H/J_0.
\tag{CSB7.2}
\]
The support-to-global maps in degree one are still \(+\mathrm{id}\) and
\(-\mathrm{id}\), respectively: their degree-zero maps send a chart section to \((a,0)\) and \((0,b)\), and their degree-one maps send \(g\) to \(g\) and \(-g\). Thus each chain identity keeps the sign of the ordered Čech differential.

The alternative-to-full sheaf sequence is
\[
0\longrightarrow
i_{0*}V_+\oplus i_{\infty*}V_-
\longrightarrow\widetilde{\mathscr F}
\longrightarrow\mathscr F
\longrightarrow0.
\tag{CSB7.3}
\]
It has the explicit continuous, arithmetic-equivariant, Weyl-equivariant splitting (CSB5.7). The projection on global sections forgets only \(v_+,v_-\); the section sets these two defect coordinates equal to zero. The four original endpoints are preserved by both maps.

All connecting maps of this split sheaf extension are zero. This vanishing follows by applying the section to a cocycle, or directly by decomposing its entire complex as in (CSB5.7). The extension has therefore been completely calculated. It has not been identified with the different lifting-obstruction cross in Deligne §3.6 or with the user's requested common-weight construction.

## CSB8. The unchanged original-zeta receiver, with its full comparison

The cohomology identification retains the raw restriction and the original source map:
\[
Sf(u)=2u^{-1/2}\mathcal Ef(u),\qquad
\mathcal Ef(u)=u^{1/2}\sum_{n\ge1}f(nu),\qquad
Uh(u)=\tfrac12u^{1/2}h(u).
\tag{CSB8.1}
\]
The topological isomorphism \(U:H\to\mathcal A\) maps
\(\overline{J_0}\) to the proved closed original summation image
\(\mathcal C=\overline{\mathcal E(S_0)}\).
The centered Mellin transform is
\[
\mathcal Mk(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u},
\qquad
\Theta h(s)=\mathcal MUh(s)
=\tfrac12\int_0^\infty h(u)u^s\frac{du}{u}.
\tag{CSB8.2}
\]
The previous global synthesis theorem gives
\[
\Theta(\overline{J_0})=\mathcal I,\qquad
\mathcal I=\{F\in\mathcal B:
F^{(j)}(\rho)=0\text{ for all actual nontrivial }\rho,\
0\le j<m_\rho\},
\]
\[
\boxed{
H^1_{\mathrm{Haus}}(X,\widetilde{\mathscr F})
\xrightarrow[\ [h]\mapsto[\Theta h]\ ]{\ \sim\ }
\mathcal B/\mathcal I=\mathcal Q.
}
\tag{CSB8.3}
\]
Here \(\mathcal B\) is the entire strip-Schwartz space of CS7.3 with its full Fréchet topology:
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):
b_{A,M}(F)<\infty\text{ for all integers }A,M\ge0\},
\quad
b_{A,M}(F)=\sup_{\substack{|\sigma|\le A\\t\in\mathbb R}}
(1+|t|)^M|F(\sigma+it)|.
\tag{CSB8.3a}
\]
Write \(\mathcal M_0h(s)=\int_0^\infty h(u)u^s\,du/u\) for the raw Mellin isomorphism \(H\to\mathcal B\); thus \(\Theta=\tfrac12\mathcal M_0\). This is the same map for the full-difference sheaf; the additional prime-indexed endpoint summands do not alter it.

For \(\Re s>1\) the raw original-zeta identity remains
\[
\int_0^\infty Sf(u)u^s\frac{du}{u}
=2\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}.
\tag{CSB8.4}
\]
For the retained \(f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2}\), it is
\[
\Theta Sf_0(s)=F_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\int_0^\infty Sf_0(u)u^s\frac{du}{u}=2F_0(s).
\tag{CSB8.5}
\]
The endpoint values are \(F_0(0)=F_0(1)=1/8\), with raw values \(1/4\).
For \(r\ge1\), the complete finite value at the original trivial zero is
\[
2F_0(-2r)
=\frac{r(2r+1)(-1)^r\pi^r}{r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}4\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0.
\tag{CSB8.6}
\]
These Mellin endpoint values are separate from the four original sheaf endpoint lines and the extra prime-indexed endpoint directions.

The resulting action and ordered Čech reflection on this unchanged quotient are
\[
T_a[F(s)]=[a^sF(s)],\qquad
W^1[F(s)]=[-F(1-s)],\qquad
T_aW^1=aW^1T_{a^{-1}}.
\tag{CSB8.7}
\]
All actual zero multiplicities remain in \(\mathcal I\); no value-only quotient replaces the full jets.

The later complete inverse theorem, [SSI0–SSI9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/EXACT_SCHWARTZ_SUMMATION_IMAGE.md) and its independent derivation [ESI0–ESI9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/EXACT_SCHWARTZ_IMAGE_INDEPENDENT_CHECK.md), strengthens this comparison. Both proofs were read for this update. The theorem proves the topological isomorphism
\[
\mathcal M_0S:S_0\xrightarrow{\ \sim\ }\mathcal I,\qquad
J_0=\overline{J_0}=\mathcal M_0^{-1}\mathcal I.
\tag{CSB8.8}
\]
For a raw entire target \(F\in\mathcal I\), its actual source inverse is
\[
f_F(x)=\frac1{2\pi}\int_{\mathbb R}
\frac{F(2+it)}{2\zeta(2+it)}x^{-2-it}\,dt\quad(x>0),
\]
\[
f_F(-x)=f_F(x),\qquad f_F(0)=0,\qquad
\int_{\mathbb R}f_F=0,\qquad
\frac{f_F^{(2r)}(0)}{(2r)!}
=\frac{F(-2r)}{2\zeta'(-2r)}\quad(r\ge1).
\tag{CSB8.9}
\]
SSI4 and ESI4 prove rapid vertical-strip estimates after exactly the trivial poles in that strip have been cleared. They use the proved subquadratic division bound, the full functional multiplier on an odd negative vertical boundary, and the maximum principle with limits in the order \(T\to\infty\), then \(\varepsilon\downarrow0\). SSI5–SSI6 and ESI5–ESI7 prove the displayed even extension, every retained residue, and the continuity estimate
\[
\sup_{x\in\mathbb R}(1+|x|)^R|f_F^{(j)}(x)|
\le C_{R,j}\,b_{A,M}(F)
\tag{CSB8.10}
\]
for finite \(A,M\) depending on \(R,j\). Thus (CSB8.9) is an inverse into the actual Schwartz topology, and \(Sf_F=\mathcal M_0^{-1}F\). For our comparison coordinate \(G=\Theta Sf=\tfrac12\mathcal M_0Sf\), the same inverse uses \(F=2G\); its Mellin quotient is \(G/\zeta\). The raw factor two has not changed.

The ordinary-to-Hausdorff comparison kernel is now calculated, rather than left pending:
\[
\overline{J_0}/J_0=0,\qquad
0\longrightarrow0
\longrightarrow H^1_{\mathrm{alg}}(X,\widetilde{\mathscr F})
\longrightarrow\mathcal Q\longrightarrow0.
\tag{CSB8.11}
\]
Consequently ordinary \(H^1\), with its actual quotient topology, already equals the Hausdorff original-zeta receiver under (CSB8.3). This result removes the closure comparison kernel. It does not remove \(V_\pm\), which belong to the summation kernel in the source before taking that image.

## CSB9. Exact scope of the endpoint-character calculation

The computed alternative receiver is a continuous, equivariantly split extension of the full-difference receiver by the explicit space
\(\bigoplus_p\mathbb C^2\). Its single-fibre Fourier action is \(-J\); its chart actions are \(\operatorname{diag}(1,a)\) and \(\operatorname{diag}(a,1)\). The Gaussian section has no quotient-level equivariance defect, and (CSB3.8) supplies a source representative with exact Fourier equivariance.

The alternative sheaf has two independent copies of this defect, supported respectively at the two closed chart points. Its entire extra degree-zero cohomology, original four endpoint lines, Weyl maps, arithmetic characters, support maps, and connecting maps have been calculated. Its original-zeta \(H^1\) receiver is unchanged through the explicit map (CSB8.3).

These are the weights and maps of this specified endpoint relation defect. The calculation does not turn it into Deligne's geometric lifting obstruction merely because its characters have exponents 0 and 1. No assertion of RH, common-weight purity, or completion of the requested weight-separation mechanism is used or concluded.

## CSB10. Exact comparison with the prior FR prime-boundary proof

The prior proof actually read is [ORIGINAL_ZETA_RETURN_FR.tex](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/sources/ORIGINAL_ZETA_RETURN_FR.tex), FR15–FR25, source lines 115–207, together with its PM bibliography entry at line 328. That entry credits the earlier [Prime boundary classes in the actual adelic theta receiver, PM4–PM15](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/44d03e48849934edf59f645cb5021b639ab31ac4/workbenches/splitzero-tandem/continuations/20260923-original-zeta-return/sources/21_prime_memory_and_actual_theta_receiver.tex). The pinned public target was opened and verified as that TeX file at commit 44d03e48849934edf59f645cb5021b639ab31ac4. The complete proof used in the present comparison is the retained FR15–FR25 slice; this does not claim a fresh complete reading of PM1–PM23 or of the earlier base conventions.

Retain FR's group algebra
\[
\Gamma_+=\mathbb Q_{>0}^{\times},\qquad
R_\Gamma=\mathbb C[\Gamma_+],\qquad
I_\Gamma=\ker(\operatorname{aug}:R_\Gamma\to\mathbb C).
\tag{CSB10.1}
\]
Write \(S_{\mathrm{ev}}=\mathcal S(\mathbb R)^{\mathrm{even}}\), with endpoint map
\(m(h)=(h(0),\int_{\mathbb R}h)\). FR's source and quotient are
\[
M_0=\ker(\operatorname{aug}\otimes m:
R_\Gamma\otimes S_{\mathrm{ev}}\to\mathbb C^2),
\qquad Q_0=M_0/I_\Gamma M_0.
\tag{CSB10.2}
\]
Its coordinates map to the actual spherical adèlic source by
\[
\mathscr A(t_d\otimes h)(v,x_f)
=h(v/d)\,1_{d\widehat{\mathbb Z}}(x_f)
=\mathsf D_{d^{-1}}
\bigl(h\otimes1_{\widehat{\mathbb Z}}\bigr)(v,x_f).
\tag{CSB10.3}
\]
The simultaneous real and finite dilation preserves the two endpoint values:
the real integral has factor \(d\), and the finite volume has factor \(d^{-1}\). This is exactly FR16 and FR20. The finite ball independence used in CS2 proves that these coordinates are bijective onto the even \(K\)-invariant source. Multiplication by \(t_r\) corresponds to \(\mathsf D_{r^{-1}}\), so \(I_\Gamma M_0\) maps to the null-generated rational relations.

If an adèlic representative is \(\sum_d f_d(v)1_{d\widehat{\mathbb Z}}(x_f)\), the inverse coordinates are
\[
h_d(v)=f_d(dv),\qquad
m(h_d)=\left(f_d(0),d^{-1}\int_{\mathbb R}f_d\right).
\tag{CSB10.4}
\]
Thus FR's two maps in FR18 are precisely
\[
\Phi_{\mathrm{FR}}\left[\sum_d t_d\otimes h_d\right]
=\sum_dh_d=B\mathscr A\left(\sum_dt_d\otimes h_d\right),
\]
\[
\beta_{\mathrm{FR}}\left[\sum_d t_d\otimes h_d\right]
=\left(\sum_dv_p(d)m(h_d)\right)_p
=\mathscr L\mathscr A\left(\sum_dt_d\otimes h_d\right).
\tag{CSB10.5}
\]
The symbols \(\ell_p\) in FR15 are formal prime basis labels; the values of its \(\beta\) agree with the continuous component functionals denoted \(\ell_p(F)\) here.

For completeness, FR's algebraic decomposition follows by the endpoint section:
\[
M_0=(R_\Gamma\otimes S_0)\oplus(I_\Gamma\otimes\mathbb C^2),
\qquad
Q_0\simeq S_0\oplus(I_\Gamma/I_\Gamma^2)\otimes\mathbb C^2.
\tag{CSB10.6}
\]
The identity
\(t_{ab}-1=(t_a-1)+(t_b-1)+(t_a-1)(t_b-1)\)
and unique factorization identify \(I_\Gamma/I_\Gamma^2\) with
\(\bigoplus_p\mathbb C\), by \(t_d-1\mapsto(v_p(d))_p\).
The coordinate derivations \(t_d\mapsto v_p(d)\) vanish on \(I_\Gamma^2\) and prove independence; the same identity proves spanning, including negative prime powers. This gives the already established FR22 decomposition
\[
Q_0\simeq S_0\oplus V.
\tag{CSB10.7}
\]

Taking the Hausdorff quotient in the strong LF source therefore does not identify additional classes in this spherical algebraic quotient. Indeed the natural map
\[
Q_0\longrightarrow D_{\mathrm{null}}^K
\tag{CSB10.8}
\]
is surjective by the representative description (CSB10.3); in the coordinates (CSB10.5), both sides have exactly the pair \((B,\mathscr L)\). FR22 proves this pair injective on \(Q_0\), and CS2A proves it injective on \(D_{\mathrm{null}}^K\). Thus (CSB10.8) is an algebraic bijection, and with the induced locally convex quotient topology it is a homeomorphism: finite radial-ball coordinate changes are continuous on every finite LF stage, and the continuous inverse maps are the \(j\) and prime-boundary sections already written in CS2A.

The prior boundary lift at prime \(p\), FR19, uses \((t_p-1)\otimes h_w\), where \(m(h_w)=w\). Choosing \(h_w=\sigma(w)_\infty\) and applying (CSB10.3) gives
\[
b_{\mathrm{FR},p}(w)
=\left[(\mathsf D_{p^{-1}}-I)\sigma(w)\right]_{\mathrm{null}}.
\tag{CSB10.9}
\]
Our representative is \(r_p\sigma(w)=(I-\mathsf D_p)\sigma(w)\). Their actual difference is
\[
(\mathsf D_{p^{-1}}-I)\sigma(w)-r_p\sigma(w)
=-r_pr_{p^{-1}}\sigma(w)
\in\mathcal R_{\mathrm{null}}.
\tag{CSB10.10}
\]
Hence they define exactly the same boundary class, with the same sign and both endpoint coordinates. This also explains why the symmetric representative in (CSB3.8) can be used without changing the prior receiver.

The original weighted periodization seminorm in FR25 is a different receiving topology. Let \(\Theta_{\mathrm{FR}}h(u)=\sum_{n\in\mathbb Z\setminus\{0\}}h(nu)=Sh(u)\), and retain its periodization
\[
\mathcal E_{\mathrm{FR}}(c)(u)
=u^{1/2}\Theta_{\mathrm{FR}}\Phi_{\mathrm{FR}}c(u)
=2\mathcal E(\Phi_{\mathrm{FR}}c)(u).
\tag{CSB10.11}
\]
The compact-unit Haar mass in the stated convention is one. For every \(\delta>1\), FR25 is exactly
\[
\|c\|_{\delta,\mathrm{FR}}^2
=\int_0^\infty|\mathcal E_{\mathrm{FR}}(c)(u)|^2
(1+\log^2u)^{\delta/2}\frac{du}{u}
=4\int_0^\infty|\mathcal E(\Phi_{\mathrm{FR}}c)(u)|^2
(1+\log^2u)^{\delta/2}\frac{du}{u}.
\tag{CSB10.12}
\]
If the compact-unit Haar mass is \(c_K\) instead, both squared-norm expressions acquire that same factor \(c_K\).
The positive weight, continuity of the periodized function, and injectivity of \(S\) give
\[
\ker\|\cdot\|_{\delta,\mathrm{FR}}
=\ker\Phi_{\mathrm{FR}}
=b_{\mathrm{FR}}(V).
\tag{CSB10.13}
\]
Thus a nonzero \(v\) is zero in the Hausdorff quotient for this seminorm, while the continuous source coordinate \(\mathscr L\iota(v)=v\) detects it in the strong LF quotient. In particular \(\mathscr L\) cannot factor through that seminorm's Hausdorff quotient.

The new exact-image theorem \(J_0=\overline{J_0}\) in (CSB8.8) concerns the image of the summation map in the strong overlap function space. It makes ordinary first cohomology Hausdorff. It does not remove the separate kernel \(V\) before summation, and it does not change the kernel of the weaker periodization seminorm (CSB10.13). The maps (CSB10.5), (CSB10.8), and (CSB10.11) identify these three constructions explicitly.
