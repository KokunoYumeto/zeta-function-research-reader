# Independent projection and quotient review

Reviewed scope: equations GP.6–GP.11 and GP.20–GP.23 of `gamma_phase_fibre_transport_20260913.tex`. The current source has the first block at lines 92–184 and the second block at lines 352–405. The scoped blocks were read in full twice. The source SHA-256 at the second read was `bd3a5f44f5d832e55bed7556721dca53e72dbf8f9ef3d989b54170eb39ed7d6d`; concurrent changes elsewhere in the source do not extend this review's scope.

**Verdict: no mathematical error found in the reviewed equations or their scoped proofs.** In particular, the complex conjugation in the adjoint and the upper-right entry of the fibre projection matrix have the correct orientations. Both original measures retain their masses. The quotient correction has two separate positive semidefinite terms; the second is positive definite under the paper's stated strict quartet variance, so the strict quotient conclusion follows. The first term can vanish and the source explicitly treats the empty-boundary case.

The finite models below verify the operator algebra. They make no claim to be actual zeta packets or evaluations of an arithmetic integral. They preserve complex amplitudes, original masses, original monomial coordinates, and the exact boundary map.

## 1. Complete adjoint calculation and domains

The inner product is antilinear in its first argument. Let the gamma product measure be \(\nu\), its pushforward under the unchanged sum map be \(\nu_\Sigma\), and its conditional measures be \(\nu_u\). The identity

\[
\int F\,d\nu=\int\left(\int F\,d\nu_u\right)d\nu_\Sigma(u)
\]

retains \(\nu(\mathbb R^k)=\nu_\Sigma(\mathbb R)=c_\lambda^k\). Only \(\nu_u\) has unit mass, by the stated fibre denominator. Thus \(U^*=C\), \(CU=I\), and \(U\) is an isometry without changing either original measure.

Write \(b=C(|a|^2)\), and retain the two arithmetic measures \(|a|^2d\nu\) and \(b\,d\nu_\Sigma\). The exact norm equalities are

\[
\|aF\|_{L^2(\nu)}^2=\|F\|_{L^2(|a|^2\nu)}^2,
\qquad
\|\sqrt b f\|_{L^2(\nu_\Sigma)}^2
=\|f\|_{L^2(b\nu_\Sigma)}^2.
\]

Division off the zero sets gives inverses with those same equalities. The source proves the zero sets null. These maps are therefore surjective isometries, even though the inverse expressions need not be bounded multipliers on the unweighted spaces.

For the arithmetic inclusion, disintegration gives

\[
\begin{aligned}
\langle U_h f,F\rangle_{|a|^2\nu}
&=\int \overline{f(u)}C(|a|^2F)(u)\,d\nu_\Sigma(u)\\
&=\int \overline{f(u)}\frac{C(|a|^2F)(u)}{b(u)}
                         b(u)\,d\nu_\Sigma(u).
\end{aligned}
\]

Hence \(C_h^{\rm sum}=M_{b^{-1}}CM_{|a|^2}\) on its correct complete domain. Transport gives

\[
Jf=aU(f/\sqrt b),
\quad
\langle Jf,F\rangle_\nu
=\int\overline{f(u)}\frac{C(\overline a F)(u)}{\sqrt{b(u)}}d\nu_\Sigma(u),
\]

so \(J^*=M_{b^{-1/2}}CM_{\overline a}\), exactly as in GP.7. The conjugate amplitude cannot be omitted. Moreover

\[
J^*Jf=b^{-1/2}C\bigl(|a|^2U(b^{-1/2}f)\bigr)=f.
\]

Thus \(Q=JJ^*\) is an orthogonal projection, and explicitly

\[
QF=aU\left(\frac{C(\overline aF)}b\right)
=TP_hT^{-1}F.
\]

Truncation where the denominators are bounded below proves the formulas first on dense domains; the isometries extend them. No product of unbounded factors on an unstated larger space is needed.

Let \(\gamma=Ca/\sqrt b\) and \(N=J-UM_\gamma\). Then \(U^*N=0\), and

\[
I=J^*J=M_{\overline\gamma}M_\gamma+N^*N,
\quad
N^*N=M_{1-|\gamma|^2}=M_{(b-|Ca|^2)/b}.
\]

On each fibre, \(e_0=1\), \(v=a/\sqrt b\), and \(\langle e_0,v\rangle=\gamma\). For \(s=\sqrt{1-|\gamma|^2}>0\), the defined vector \(e_1=(v-\gamma e_0)/s\) gives the coordinate column \(v=(\gamma,s)^T\). Therefore

\[
Q_u=vv^*=
\begin{pmatrix}|\gamma|^2&\gamma s\\\overline\gamma s&s^2\end{pmatrix}.
\]

Both GP.10 identities follow by multiplication:

\[
\operatorname{Tr}(P_u-Q_u)^2=2(1-|\gamma|^2),
\qquad
\operatorname{Tr}([P_u,Q_u]^*[P_u,Q_u])
=2|\gamma|^2(1-|\gamma|^2).
\]

When \(s=0\), the projections coincide, so both quantities vanish without introducing \(e_1\). The variance identity GP.11 follows by expanding

\[
\frac12\iint(|a(t)|^2+|a(s)|^2
-a(t)\overline{a(s)}-\overline{a(t)}a(s))d\nu_u(t)d\nu_u(s)
=b-|Ca|^2.
\]

All of these traces are fibre finite-rank traces. This calculation supplies no global trace-class assertion.

## 2. Exact rational complex fibre fixture

Take the original two-point measure to have mass seven, with Gram matrix

\[
D=\operatorname{diag}(7/3,14/3),\qquad
U=\binom11,\quad C=(1/3,2/3),\qquad a=\binom{1+i}{2+i}.
\]

The sum space has Gram matrix \((7)\). The arithmetic source Gram is
\(D_h=\operatorname{diag}(14/3,70/3)\), and the arithmetic sum Gram is \((28)\). Thus

\[
b=4,\quad Ca=5/3+i,\quad d=2/9,\quad
T=\operatorname{diag}(1+i,2+i),\quad T_\Sigma=2,
\quad C_h=(1/6,5/6).
\]

For a map from a space with Gram \(D_1\) to a space with Gram \(D_2\), the adjoint is \(A^\dagger=D_1^{-1}\overline A^T D_2\). Direct application gives

\[
J=\binom{(1+i)/2}{1+i/2},\qquad
J^*=((1-i)/6,(2-i)/3),\qquad J^*J=1.
\]

The two original projection matrices are

\[
P=\begin{pmatrix}1/3&2/3\\1/3&2/3\end{pmatrix},
\qquad
Q=\begin{pmatrix}
1/6&(3+i)/6\\(3-i)/12&5/6
\end{pmatrix}.
\]

They satisfy \(Q=TU C_hT^{-1}=JJ^*\), \(Q^2=Q\), and \(D^{-1}Q^*D=Q\). Here \(Q^*\) in the last expression denotes ordinary conjugate transpose; the weighted adjoint was written explicitly. The unequal original masses are essential to that equality.

The angle and defect are

\[
\gamma=5/6+i/2,\quad |\gamma|^2=17/18,\quad
N=\binom{-1/3}{1/6},\quad U^*N=0,\quad N^*N=1/18=d/b.
\]

Consequently

\[
\operatorname{Tr}(P-Q)^2=1/9,\qquad
\|[P,Q]\|_{\mathrm{HS},D}^2=17/162.
\]

The unscaled variance calculation is

\[
\frac12\sum_{j,l=1}^2p_jp_l|a_j-a_l|^2
=p_1p_2|a_1-a_2|^2=2/9,
\quad (p_1,p_2)=(1/3,2/3).
\]

The original source norm of the relative amplitude is \(7d=14/9\), retaining the mass seven. This fixture would detect an omitted conjugate in \(J^*\), a missing factor \(b\), an incorrect weighted adjoint, or an accidental replacement of the original mass by one.

## 3. Exact finite quotient calculation

Put \(B=B_\chi\), \(M=M_h=M_c+M_r\), where \(M_c=M_{\rm coh}>0\) and \(M_r=M_{\rm rel}\geq0\). Every section of the original quotient differs from \(R_c\) by \(BL\). Since \(B^*M_cR_c=0\), the arithmetic orthogonality equation for \(R_c-BK\) is

\[
0=B^*M(R_c-BK)=B^*M_rR_c-(B^*MB)K.
\]

The injectivity of \(B\) and positivity of \(M\) make \(B^*MB\) invertible on the boundary space. Hence

\[
K=(B^*MB)^{-1}B^*M_rR_c,\qquad R_h=R_c-BK.
\]

This is GP.20 and the first identity in GP.21 with the exact type \(K:C_\chi\to E_\partial\). Expansion gives

\[
\begin{aligned}
R_h^*M_cR_h
&=R_c^*M_cR_c-R_c^*M_cBK-K^*B^*M_cR_c
   +K^*B^*M_cBK\\
&=G_c+K^*B^*M_cBK.
\end{aligned}
\]

Adding the unchanged relative pullback proves the exact two-term identity

\[
G_h-G_c=K^*B^*M_cBK+R_h^*M_rR_h.
\]

Each term is positive semidefinite. If \(M_r>0\) and the quotient is nonzero, then \(R_h\) is injective because \(\pi R_h=I\), and therefore its pullback is positive definite. This proves the source's strict conclusion using its stated strict relative Gram result. It does not require the boundary contribution to be strictly positive.

For \(\Delta=G_h-G_c\), the precise factorization is

\[
G_h=G_c^{1/2}\bigl(I+G_c^{-1/2}\Delta G_c^{-1/2}\bigr)G_c^{1/2}.
\]

Taking determinants proves GP.23 without replacing either metric. An empty boundary sets \(K=0\). The zero quotient has empty determinant one. These edge conventions agree with the manuscript.

## 4. Rational complex quotient fixture with nonzero correction

Retain \(E=\mathcal P_2(S)\), \(E_\partial=\mathcal P_0(S)\),

\[
\chi(S)=S^2+(1+i)S+(2-i),\qquad
B=\begin{pmatrix}2-i\\1+i\\1\end{pmatrix},\qquad
\pi=\begin{pmatrix}1&0&-2+i\\0&1&-1-i\end{pmatrix}.
\]

The quotient coordinates are \(([1],[S])\). Define the exact transport from the fixed frame \((1,S,\chi)\) to the original monomial frame by

\[
L=\begin{pmatrix}1&0&2-i\\0&1&1+i\\0&0&1\end{pmatrix},\qquad\det L=1.
\]

In the explicitly identified frame, take

\[
M_{c,x}=\operatorname{diag}(4,9,2),\qquad
M_{r,x}=\begin{pmatrix}2&1&i\\1&2&1+i\\-i&1-i&3\end{pmatrix}.
\]

The relative matrix's leading principal minors are \(2,3,5\), proving positive definiteness by Sylvester's criterion. The exact original monomial matrices \(M_j=L^{-*}M_{j,x}L^{-1}\) are

\[
M_c=\begin{pmatrix}
4&0&-8+4i\\0&9&-9-9i\\-8-4i&-9+9i&40
\end{pmatrix},\qquad
M_r=\begin{pmatrix}
2&1&-5+2i\\1&2&-3\\-5-2i&-3&17
\end{pmatrix}.
\]

The original arithmetic matrix is exactly \(M_h=M_c+M_r\). The coherent section and nonzero correction are

\[
R_c=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix},\qquad
K=\frac15(-i,1-i).
\]

In the original monomial frame the arithmetic section is

\[
R_h=R_c-BK=
\frac15\begin{pmatrix}
6+2i&-1+3i\\-1+i&3\\i&-1+i
\end{pmatrix}.
\]

Direct multiplication gives \(\pi B=0\), \(\pi R_c=\pi R_h=I\), \(B^*M_cR_c=0\), and \(B^*M_hR_h=0\). The quotient metrics are

\[
G_c=\begin{pmatrix}4&0\\0&9\end{pmatrix},\qquad
G_h=\frac15\begin{pmatrix}29&4-i\\4+i&53\end{pmatrix}.
\]

The two individually retained terms are

\[
K^*B^*M_cBK=\frac1{25}
\begin{pmatrix}2&2+2i\\2-2i&4\end{pmatrix},
\qquad
R_h^*M_rR_h=\frac1{25}
\begin{pmatrix}43&18-7i\\18+7i&36\end{pmatrix}.
\]

Their sum is

\[
\Delta=G_h-G_c=\frac15\begin{pmatrix}9&4-i\\4+i&8\end{pmatrix}.
\]

The first term is nonzero of rank one. The second has positive first diagonal entry and determinant \(47/25\). The total difference has determinant \(11/5\). Thus this fixture tests the nonzero section correction and strict positivity independently.

Since the actual \(G_c^{-1/2}=\operatorname{diag}(1/2,1/3)\), its exact matrix in GP.22 is

\[
E_q=\begin{pmatrix}9/20&(4-i)/30\\(4+i)/30&8/45\end{pmatrix},
\quad\det E_q=11/180,\quad\det(I+E_q)=76/45.
\]

Finally,

\[
\det G_h=304/5=36\cdot76/45
=\det G_c\det(I+E_q).
\]

## 5. Reproducible exact checks

The companion script `gamma_phase_fibre_projection_fixture_check_20260913.py` executes all 37 equalities over exact rational complex SymPy expressions. It raises an explicit exception on a nonzero residual and uses no Python `assert` statements. One ordinary Python run completed successfully and produced `gamma_phase_fibre_projection_fixture_check_20260913.json`; no Lean run was made.

- Checker SHA-256: `e2cf0a3f4a6ff87db683abd918e9740e328d39ad47085b629fac8a9f696fc7a2`.
- Result SHA-256: `702b90216ebe2221e0cc8ca827c74b0f34c86a09d32756af3c436f0d59fa4b37`.
- Checked result: 37/37 exact identities passed.
- Root mathematical source modifications by this reviewer: none.

The direct proofs above establish the general operator identities in the reviewed scope. The finite fixtures supply independent nonreal, nonzero-correction checks of their conjugations, masses, signs, basis transport, and determinant factors.
