# Exact nested relative-frame calibration in the original coordinates

This is one completely explicit polynomial family with ambient space
\(\mathbb C^5\), larger coefficient space \(\mathbb C^3\), and smaller
coefficient space \(\mathbb C^2\). The ambient inner product is the standard
Hermitian product. All coefficient weights below are retained. The example
proves the displayed finite-dimensional identities and gives a nonzero witness
for both normal contributions. It makes no assertion about a particular
arithmetic density or a uniform analytic bound.

The accompanying script is `nested_relative_frame_fixture_20260912.py`.
Its SHA256 is
`5d98655ec940645fd410e85986f5cea126feaaf9b3c7b95840b9c9e3a8e2b674`.
It stores the original symbolic matrices and all rational sample matrices in
JSON. Its 24 checks perform complete exact rational-function calculations;
they do not replace the original frame with orthonormal coordinates.

## Original family and all coefficient weights

For every real \(u\), put
\[
p=1+u,\qquad q=1+u+u^2,\qquad
j_L(u)=\begin{pmatrix}
1&0&0\\0&1&0\\0&0&1\\p&2p&-p\\2q&-q&q
\end{pmatrix},\qquad
E=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}.
\]
The constant map \(E:\mathbb C^2\to\mathbb C^3\) is injective, and the
literal composite \(j_M=j_LE:\mathbb C^2\to\mathbb C^5\) is
\[
j_M(u)=\begin{pmatrix}1&0\\0&1\\1&1\\0&p\\3q&0\end{pmatrix}.
\]
Write \(a=(1,2,-1)^T\), \(b=(2,-1,1)^T\). Direct multiplication gives
\[
W_L=j_L^*j_L=I_3+p^2aa^T+q^2bb^T,
\qquad
W_M=j_M^*j_M=E^*W_LE
=\begin{pmatrix}2+9q^2&1\\1&2+p^2\end{pmatrix}.
\]
For nonzero \(z\in\mathbb C^3\),
\(z^*W_Lz=\|z\|^2+p^2|a^Tz|^2+q^2|b^Tz|^2>0\).
For nonzero \(c\in\mathbb C^2\), the injectivity of \(E\) gives
\(c^*W_Mc=(Ec)^*W_L(Ec)>0\). Thus every inverse used below exists for
every real \(u\). Moreover,
\[
B_L=j_L^*j_L'=pp'aa^T+qq'bb^T=\tfrac12W_L',\qquad
B_M=j_M^*j_M'=\operatorname{diag}(9qq',pp')=\tfrac12W_M'.
\]
Evenness and commutativity are both genuinely absent:
\[
W_M(1)-W_M(-1)=\begin{pmatrix}72&0\\0&4\end{pmatrix},
\quad
[W_M(0),W_M(1)]=\begin{pmatrix}0&-69\\69&0\end{pmatrix},
\]
\[
W_L(1)-W_L(-1)=4aa^T+8bb^T,\qquad
[W_L(0),W_L(1)]=
\begin{pmatrix}0&25&-15\\-25&0&-5\\15&5&0\end{pmatrix}.
\]
All displayed differences are nonzero matrices in their original bases.

## Exact maps and normal partition

For \(X=L,M\), define
\[
\Pi_X=j_XW_X^{-1}j_X^*,\qquad
\Gamma_X=W_X^{-1}j_X^*j_X',\qquad
N_X=(I_5-\Pi_X)j_X'.
\]
The formulas \(\Pi_X^*=\Pi_X\), \(\Pi_X^2=\Pi_X\), and
\(\Pi_Xj_X=j_X\) follow by direct multiplication using
\(j_X^*j_X=W_X\). Since \(j_M=j_LE\), one obtains
\(\Pi_L\Pi_M=\Pi_M\), hence also \(\Pi_M\Pi_L=\Pi_M\) by adjoints.
Put
\[
A=(\Pi_L-\Pi_M)j_M',\qquad R=N_LE,
\qquad K=\Gamma_LE-E\Gamma_M.
\]
Here \(A,R:\mathbb C^2\to\mathbb C^5\) and
\(K:\mathbb C^2\to\mathbb C^3\). Because \(E\) is constant,
\(j_M'=j_L'E\). Expanding the two projectors therefore gives
\[
N_M=A+R,
\qquad
A=j_LK,
\qquad
\Gamma_M=W_M^{-1}E^*W_L\Gamma_LE.
\]
For the last identity, multiply out
\(E^*W_L\Gamma_LE=E^*j_L^*j_L'E=j_M^*j_M'\).
The middle identity follows from
\(\Pi_Lj_M'=j_L\Gamma_LE\) and
\(\Pi_Mj_M'=j_M\Gamma_M=j_LE\Gamma_M\).
Furthermore,
\[
E^*W_LK
=E^*W_L\Gamma_LE-E^*W_LE\Gamma_M
=j_M^*j_M'-W_M\Gamma_M=0.
\]
The relation
\((\Pi_L-\Pi_M)(I_5-\Pi_L)=0\) proves \(A^*R=0\).
Consequently the full normal Gram identity is
\[
N_M^*N_M=E^*N_L^*N_LE+K^*W_LK.
\]
For an arbitrary differentiable coefficient curve
\(c:\mathbb R\to\mathbb C^2\), the literal product rule gives
\[
(j_Mc)'=j_M(c'+\Gamma_Mc)+Ac+Rc.
\]
The three terms lie respectively in
\(\operatorname{im}j_M\),
\(\operatorname{im}j_L\cap(\operatorname{im}j_M)^\perp\), and
\((\operatorname{im}j_L)^\perp\). They are pairwise orthogonal, so
\[
\|(j_Mc)'\|^2
=(c'+\Gamma_Mc)^*W_M(c'+\Gamma_Mc)
+c^*K^*W_LKc+c^*E^*N_L^*N_LEc.
\]
This is a pointwise identity. For \(c\in C_c^1(\mathbb R;\mathbb C^2)\)
it may be integrated as an identity of finite integrals: \(c,c'\) are
continuous and bounded on the compact support, and every matrix here is smooth
there.

## Independent exact sample at \(u=1\)

At \(u=1\), let \(J=j_L(1)\), \(J_M=j_M(1)\), and
\(D_M=j_M'(1)\). Then
\[
J=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\\2&4&-2\\6&-3&3\end{pmatrix},
\quad
J_M=\begin{pmatrix}1&0\\0&1\\1&1\\0&2\\9&0\end{pmatrix},
\quad
D_M=\begin{pmatrix}0&0\\0&0\\0&0\\0&1\\9&0\end{pmatrix},
\]
\[
W_L(1)=\begin{pmatrix}41&-10&14\\-10&26&-17\\14&-17&14\end{pmatrix},
\qquad W_M(1)=\begin{pmatrix}83&1\\1&6\end{pmatrix},
\qquad
\Gamma_M(1)=\frac1{497}\begin{pmatrix}486&-2\\-81&166\end{pmatrix}.
\]
The transition projection admits an independent direct construction. Put
\[
v=\begin{pmatrix}171\\-277\\-603\\440\\48\end{pmatrix}.
\]
Direct multiplication verifies
\(v=J(171,-277,-603)^T\), \(J_M^*v=0\), and
\(v^*v=665483\). The ranks of \(J\) and \(J_M\) are respectively
three and two, as their first three rows show. Hence
\[
\Pi_L(1)-\Pi_M(1)=\frac{vv^*}{665483},
\qquad
A(1)=\frac8{665483}v\begin{pmatrix}54&55\end{pmatrix}.
\]
The remaining normal matrix is
\[
R(1)=\frac1{1339}
\begin{pmatrix}-1458&-146\\459&-202\\-567&92\\54&55\\225&6\end{pmatrix}.
\]
For a direct check of its defining projection, put
\[
T=\frac1{1339}
\begin{pmatrix}1458&146\\-459&202\\567&-92\end{pmatrix}.
\]
Then
\[
W_L(1)T=J^*D_M=
\begin{pmatrix}54&2\\-27&4\\27&-2\end{pmatrix},
\qquad R(1)=D_M-JT.
\]
Thus \(T=W_L(1)^{-1}J^*D_M\) and
\(R(1)=(I_5-\Pi_L(1))D_M\) exactly. Direct multiplication also gives
\(J^*R(1)=0\) and \(v^*R(1)=0\), proving
\(A(1)^*R(1)=0\) without using the connection formula. Both matrices
are nonzero, and their retained Gram matrices are
\[
A(1)^*A(1)=\frac1{665483}
\begin{pmatrix}186624&190080\\190080&193600\end{pmatrix},
\qquad
R(1)^*R(1)=\frac1{1339}
\begin{pmatrix}2025&54\\54&55\end{pmatrix}.
\]

## Full coefficient derivative and its three nonzero terms

Choose the original coefficient curve
\(c(u)=(1+iu,u^2-i)^T\). Its value and derivative at one are
\(c(1)=(1+i,1-i)^T\) and \(c'(1)=(i,2)^T\). The derivative computed
before any projection is
\[
w=D_Mc(1)+J_Mc'(1)
=\begin{pmatrix}i\\2\\2+i\\5-i\\9+18i\end{pmatrix},
\qquad w^*w=441.
\]
The tangent term is
\[
t=\frac1{497}
\begin{pmatrix}484+985i\\1079-247i\\1563+738i\\2158-494i\\4356+8865i\end{pmatrix}.
\]
The two normal terms are
\[
A(1)c(1)=\frac{8(109-i)}{665483}v,
\qquad
R(1)c(1)=\frac1{1339}
\begin{pmatrix}-1604-1312i\\257+661i\\-475-659i\\109-i\\231+219i\end{pmatrix}.
\]
They sum exactly to \(w\), and the preceding orthogonality calculations
give the complete energy decomposition
\[
441=\frac{217065}{497}+\frac{58496}{51191}+\frac{320}{103}.
\]
The summands are respectively \(\|t\|^2\),
\(\|A(1)c(1)\|^2\), and \(\|R(1)c(1)\|^2\).
Both normal summands are strictly positive. Omitting either one changes the
original derivative energy by the corresponding displayed positive rational
number. The scalar 441 is a pointwise energy at \(u=1\), not an integral
over the real line. To realize the same sample with compact support, multiply
\(c(u)\) by a smooth compactly supported function equal to one on a
neighborhood of \(u=1\); this preserves both the sample value and derivative.

## Verification provenance

The symbolic calculation preserves the original matrices and checks the
identities for all real \(u\) using exact rational arithmetic. A separate
agent independently computed the displayed sample from \(J\), \(D_M\),
and \(E\), constructed the rank-one transition projection from \(v\), and
verified the rational energy terms. No shared TeX, cumulative build, frozen
edition, or publication-stage file was edited by this fixture task.

Normal and optimized Python each passed all 24 checks. Independent review
identified a missing plus sign in the written general energy formula and the
need to require \(C_c^1\) for its finite integrated form; both are corrected
above. The executable used explicit exception checks, so optimization does
not disable verification.
