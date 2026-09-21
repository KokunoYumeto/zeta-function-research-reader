# Perfect residue, degenerating trace, and the complete inverse-exterior cost

## Original atlas and conventions

The attached `EXCEPTIONAL_ATLAS.md` supplies the smooth finite eight-sheet completion and the finite-root chart
\[
 \mathcal B_h=\mathbb C[r,t]/(h(r),t^2-h'(r)),\qquad
 h(r)=Ar^4+r^3+Br^2+Cr+D.
\tag{RE1}
\]
On this chart the original affine source has a=1/t. The present calculation is on the unchanged algebra, not its reduced root set. In sections 1--2 A is nonzero so that 1,r,r^2,r^3,t,tr,tr^2,tr^3 is the specified free basis. Section 3 uses the actual paired target h_w with A=-1/2. The letter g in those sections means gamma squared, not 2xi.

## 1. A perfect residue pairing through every finite collision

Every element of RE1 has a unique form p(r)+tq(r), with p,q of degree at most three. Define
\[
 \boxed{\ell_h(p+tq)=A^{-1}[r^3]q.}
\tag{RE2}
\]
Reduction modulo h is understood before the coefficient is taken. This is also the iterated residue in the order (h,t^2-h'), with volume dr wedge dt: at a simple point (r_j,t_j), its value on f is f(r_j,t_j)/(2t_jh'(r_j)). Summing the two t signs cancels the p part and gives q(r_j)/h'(r_j); polynomial partial fractions identify that sum with A^(-1)[r^3]q. The coefficient definition RE2 continues through every repeated-root fibre without division by h'(r).

Let R_h be the four-by-four matrix
\[
 (R_h)_{ij}=A^{-1}[r^3](r^{i+j}\bmod h),\quad0\le i,j\le3.
\]
Entries below total degree three vanish, and its anti-diagonal entries are 1/A. Consequently det R_h=A^(-4). The full bilinear residue matrix is
\[
 \boxed{\mathsf R_h=\begin{pmatrix}0&R_h\\R_h&0\end{pmatrix},
 \qquad \det\mathsf R_h=A^{-8}\ne0.}
\tag{RE3}
\]
Indeed multiplication of two odd elements gives h'qq', which is even and annihilated by ell_h. The two mixed terms give the two displayed blocks. This proves perfection even on the discriminant.

Let H=M_{h'(r)} on C[r]/h. Multiplication by t and by the Jacobian are
\[
 T=\begin{pmatrix}0&H\\I&0\end{pmatrix},\qquad
 \mathsf J=M_{2t^3}=2\begin{pmatrix}0&H^2\\H&0\end{pmatrix}.
\]
The exact trace identity is
\[
 \boxed{\operatorname{Tr}M_f=\ell_h(2t^3f),\qquad
 \mathsf{Tr}_h=\mathsf R_h\mathsf J
 =\operatorname{diag}(2R_hH,2R_hH^2).}
\tag{RE4}
\]
For distinct roots the residue expression sums f at all eight points after multiplication by 2t h'=2t^3. Both sides are polynomial expressions in the coefficients and A^(-1), so the identity extends to the discriminant. Alternatively it follows directly by traces of the two multiplication blocks. Thus the vanishing trace discriminant is exactly the effect of the displayed multiplier, not degeneration of the perfect residue pairing.

At a root r0 of multiplicity m, write h(r0+epsilon)=epsilon^m u(epsilon), u(0) nonzero. The local fibre is
\[
 \mathbb C[\epsilon,t]/(\epsilon^m,t^2-mu(0)\epsilon^{m-1}).
\]
The local functional is
\[
 \ell(p+tq)=[\epsilon^{m-1}]\frac{q(\epsilon)}{u(\epsilon)}.
\tag{RE5}
\]
This retains the whole local unit, not merely its constant. In particular ell(t epsilon^(m-1))=1/u(0). For m>=2, multiplication by
\[
 2t^3=2m u(0)t\epsilon^{m-1}
\]
has rank one and ell(2t^3)=2m. The ordinary trace therefore has rank one on this length-2m local fibre. By contrast the residue pairing RE5 is perfect.

For a holomorphic root function F of vanishing order nu at r0, multiplication acts equally on its even and odd C[epsilon]/epsilon^m summands. Its exact rank is
\[
 \operatorname{rank}M_F=2\max(m-\nu,0).
\tag{RE6}
\]
For example a first-order arithmetic zero on a double target root leaves rank two on each length-four state algebra, even though its trace is zero. This is the precise retained nilpotent information.

## 2. The residue functional has an explicit chart transformation

Use the atlas chart R=1/(p-r), T=t/(p-r). On the original incidence the new relations are
\[
 h_p(R)=R^4h(p-1/R),\qquad T^2-h_p'(R)=R^2(t^2-h'(r))-4R^3h(r).
\]
Their relation matrix has determinant R^6, while the coordinate volume Jacobian is R^3. Thus
\[
 \boxed{\ell_p(f)=\ell_h(R^{-3}f),\qquad
 \mathsf J_p=R^3\mathsf J_h.}
\tag{RE7}
\]
One can verify this at each simple state by the quotient of the two Jacobians; the polynomial identities then extend through collisions. Multiplying the two displayed transformation laws leaves the trace unchanged.

On the infinity chart v=1/r, theta=-t/r, the new relations are k(v), theta^2+k'(v). Their relation matrix is
\[
 \begin{pmatrix}v^4&0\\4v^3&v^2\end{pmatrix},
\]
and their coordinate Jacobian is v^3. Their Jacobian multiplier is -2theta^3=v^3(2t^3). Therefore ell_infinity(f)=ell_h(v^(-3)f), again with invariant trace. The residue functionals are not asserted to be identical without this factor.

## 3. The literal paired family, its reflection, and full nilpotents

Retain gamma>0, put g=gamma^2, w=delta^2, and x=r-1/2. The atlas paired target is
\[
 h_w(x)=-\tfrac12\{x^4+2(g-w)x^2+(g+w)^2\}.
\tag{RE8}
\]
The factor -1/2 retains its original cubic coefficient in r. In the ordered basis (1,x,x^2,x^3), multiplication by x is
\[
 X_w=\begin{pmatrix}
 0&0&0&-(g+w)^2\\1&0&0&0\\0&1&0&-2(g-w)\\0&0&1&0
 \end{pmatrix}.
\]
The derivative multiplier and base residue matrix are
\[
 H_w=-2X_w(X_w^2+(g-w)I),
\]
\[
 R_w=\begin{pmatrix}
 0&0&0&-2\\0&0&-2&0\\0&-2&0&4(g-w)\\-2&0&4(g-w)&0
 \end{pmatrix}.
\tag{RE9}
\]
These retain the original coefficient -1/2, not a monic rescaling of the residue.

Define the antilinear reflection on the completed algebra by
\[
 x^\sharp=-x,\qquad t^\sharp=it,
\]
with conjugation of coefficients. It respects t^2=h_w'(x), since h_w' is odd, and has square one. If c=(1+i)/sqrt2, define the Hermitian residue
\[
 \boxed{\mathcal R_w(f,g)=c\ell_h(f^\sharp g).}
\tag{RE10}
\]
Indeed ell_h(a^sharp)=-i conjugate(ell_h(a)), and -ic=conjugate(c). In coefficient coordinates put D=diag(1,-1,1,-1), S=diag(D,iD). Then
\[
 \mathcal R_w=cS\begin{pmatrix}0&R_w\\R_w&0\end{pmatrix},
 \qquad \det\mathcal R_w=256.
\]
Its off-diagonal block is invertible and its two diagonal blocks vanish. Congruence by that off-diagonal block reduces it to [0 I;I 0], proving inertia (4,4) at every w>=0, including w=0. The arithmetic label action
\[
 \mathscr A=\operatorname{diag}(\tfrac12I+X_w,\tfrac12I+X_w)
\]
satisfies exactly
\[
 \mathscr A^*\mathcal R_w+\mathcal R_w\mathscr A=\mathcal R_w.
\tag{RE11}
\]

The reflected ordinary trace is W_w=S Tr_h. With
\[
 \Theta_w=M_{2t^3}/c,
\]
RE4 gives
\[
 \boxed{W_w=\mathcal R_w\Theta_w.}
\tag{RE12}
\]
The multiplier commutes with the root action. For w>0, reflection pairs distinct off-critical states and W_w has inertia (4,4). At w=0 the two roots are fixed under reflection and the entire length-four local trace is four times its constant value. Thus
\[
 W_0(f,g)=4\sum_{\eta=\pm1}
       \overline{f(1/2+i\eta\gamma,0)}g(1/2+i\eta\gamma,0),
 \quad \operatorname{rank}W_0=2.
\tag{RE13}
\]
Six trace directions disappear; the perfect residue has none missing.

The completed root action at each critical primary is rho I+N, where N=t^2/(4gamma^2) and N^2=0, rank N=2. Every positive semidefinite complementary-Euler form on that block kills N. To prove this directly, N is skew-adjoint in its seminorm, so the squared seminorm of exp(sN)v=v+sNv is constant for real s. Its quadratic coefficient is the squared seminorm of Nv, hence zero; Cauchy--Schwarz places Nv in the radical. Conversely every positive form on B/NB defines a complementary form. The actual quotient map is
\[
 f_0+f_1t+f_2t^2+f_3t^3\longmapsto(f_0,f_1),
\]
with kernel t^2B. The two distinct heights have zero cross block: the cross Sylvester equation is a nonzero imaginary scalar plus commuting nilpotent operators, with its finite geometric-series inverse. Therefore the full positive cone consists of two arbitrary positive semidefinite two-by-two forms. Its maximum rank is four, while the ordinary trace in RE13 has rank two. These are forms on the completed algebra, not the original native G_N.

## 4. Exact inverse of the ramification multiplier

Polynomial reduction in RE8 gives
\[
 \boxed{H_w^2=-16gwX_w^2.}
\tag{RE14}
\]
For w>0, X_w is invertible and
\[
 \boxed{
 M_{2t^3}^{-1}
 =\frac12\begin{pmatrix}0&H_w^{-1}\\H_w^{-2}&0\end{pmatrix}
 =\begin{pmatrix}
 0&\dfrac{X_w^2+(g-w)I}{16gwX_w}\\[3pt]
 -\dfrac{X_w^{-2}}{32gw}&0
 \end{pmatrix}.}
\tag{RE15}
\]
Every entry has at most a first-order pole in w. Its leading residue has rank six:
\[
 w\,M_{2t^3}^{-1}\longrightarrow
 \begin{pmatrix}0&R_1\\R_2&0\end{pmatrix},
 \quad R_1=H_0/(32g^2),\quad R_2=-X_0^{-2}/(32g),
\]
\[
 \operatorname{rank}R_1=2,\qquad\operatorname{rank}R_2=4.
\tag{RE16}
\]
The determinant is exact, not just its pole order:
\[
 \boxed{\det H_w=256g^2w^2(g+w)^2,\qquad
 \det M_{2t^3}=2^{32}g^6w^6(g+w)^6.}
\tag{RE17}
\]
In particular det W_w=2^40 g^6w^6(g+w)^6, consistent with RE12 and det R=256.

## 5. All eight singular scales in an original Gamma norm

Fix an original Gamma order s>0, put b=s/2 and M_s=(2pi)^(s/2), and keep its original centre c0. The explicit coefficient translation
\[
 p(x)\longmapsto p(S'-c0),\qquad S'=c0+iy,
\]
identifies the polynomial x with iy in the same physical measure. Its inverse is S'=x+c0. Thus the coefficient Gram of 1,x,x^2,x^3 is exactly
\[
 G_4=M_s\begin{pmatrix}
 1&0&-b&0\\
 0&b&0&-m_4\\
 -b&0&m_4&0\\
 0&-m_4&0&m_6
 \end{pmatrix},
\]
\[
 m_4=3b^2+2b,\qquad m_6=15b^3+30b^2+16b.
\tag{RE18}
\]
This follows by differentiating the original characteristic function M_s(cosh t)^(-b); no mass is removed. Put G_8=diag(G_4,G_4) on the coefficient decomposition p+tq. This is a specified two-copy original Gamma norm. It is not an assertion that multiplication by t is an isometry or that this is a previously assigned norm on the abstract signed states.

On even indices (0,2) and odd indices (1,3), the Gram blocks are
\[
 E=M_s\begin{pmatrix}1&-b\\-b&m_4\end{pmatrix},\quad
 O=M_s\begin{pmatrix}b&-m_4\\-m_4&m_6\end{pmatrix}.
\]
Put
\[
 N_E=g^2-2bg+m_4,\quad N_O=bg^2-2m_4g+m_6,
\]
\[
 \boxed{
 s_a=2g\sqrt{\frac{N_EN_O}{6b^2(b+1)(b+2)}},\quad
 s_b=2\sqrt{\frac{N_EN_O}{2b(b+1)}}.}
\tag{RE19}
\]
These are the two nonzero singular values of H_0, not necessarily sorted. To verify, let v=(g,1)^T and r=(1,-g). The off-diagonal parity blocks of H_0 are 2gvr and -2vr. A rank-one map vr from metric O to E has squared singular value (v*Ev)(r O^(-1)r*). Inverting the two full two-by-two Grams gives RE19; the common mass M_s cancels on both sides.

Put
\[
 \chi_E=\frac{N_E}{\sqrt{2b(b+1)}},\qquad
 \chi_O=\frac{N_O}{\sqrt{6b^2(b+1)(b+2)}}.
\]
The four singular values of R_2 in RE16 are
\[
 \boxed{
 c_{E,\pm}=\frac{\sqrt{4g^2+\chi_E^2}\pm\chi_E}{64g^3},\quad
 c_{O,\pm}=\frac{\sqrt{4g^2+\chi_O^2}\pm\chi_O}{64g^3}.}
\tag{RE20}
\]
Indeed on either parity block -X_0^(-2)/(32g) equals
\[
 \frac1{32g^3}\begin{pmatrix}2g&-g^2\\1&0\end{pmatrix}
 =\frac1{32g^3}(gI+vr).
\]
Here rv=0, so the metric-conjugated rank-one vr is nilpotent, with zero trace. Its Hilbert--Schmidt square is chi_E^2 or chi_O^2. The squared singular sum of gI+vr is therefore 2g^2+chi^2 and its determinant is g^2. Solving these two scalar equations gives RE20.

Let c1>=...>=c6 be the sorted six positive numbers
\[
 \left\{\frac{s_a}{32g^2},\frac{s_b}{32g^2},
 c_{E,+},c_{E,-},c_{O,+},c_{O,-}\right\},
\]
and let d1>=d2 be the sorted numbers {1/(2s_a),1/(2s_b)}. The complete ordered singular values of Theta_w^(-1) have the asymptotic multiset
\[
 \boxed{\{c_1/w,\ldots,c_6/w,d_1,d_2\}\,[1+o(1)]
 \quad(w\downarrow0).}
\tag{RE21}
\]
Multiplication by c of modulus one does not change singular values. For the upper-right block in RE15, its four singular values are exactly the reciprocals of twice the singular values of H_w. Two remain finite with limits d1,d2 and two grow as the nonzero singular values of R1 divided by w. The lower-left block has all four growing limits from R2. The direct sum of their squared singular spectra proves RE21 without replacing the full matrix by just its determinant.

Consequently every inverse-exterior rank is evaluated:
\[
 \boxed{
 \begin{aligned}
 \|\wedge^r\Theta_w^{-1}\|
 &\sim w^{-r}\prod_{j=1}^r c_j,&&1\le r\le6,\\
 \|\wedge^7\Theta_w^{-1}\|
 &\sim w^{-6}\left(\prod_{j=1}^6c_j\right)d_1,\\
 \|\wedge^8\Theta_w^{-1}\|
 &=\frac1{2^{32}g^6w^6(g+w)^6}.
 \end{aligned}}
\tag{RE22}
\]
The r=0 norm is one. In the original delta coordinate the divergence exponent is 2 min(r,6). In particular it is twelve at the full rank. The exact product of RE19--20 is consistent with the top-rank leading coefficient 1/(2^32 g^12).

## 6. How this returns to the conductor bounds already in the programme

The coefficient translation preceding RE18 is an explicitly chosen isometry from the original two-copy Gamma target to the completed coefficient space. Denote its inverse, into that target, by C0. Thus Theta_W=C0 Theta_w C0^(-1) has exactly RE22 in the original Gamma target norm.

Let L=T_A|_U be the original four-dimensional conductor isomorphism with its original source quotient norm and target Gamma norm, and put C=L direct-sum L. The same-valued completed operation on the source is Theta_U=C^(-1)Theta_W C. This is an exact intertwining, C Theta_U=Theta_W C; it makes no assertion that C is an isometry. For every exterior rank 0<=r<=8, the actual composite inverse satisfies
\[
 \boxed{
 \frac{\|\wedge^r\Theta_W^{-1}\|}{\|\wedge^r C\|}
 \le\|\wedge^r(C^{-1}\Theta_W^{-1})\|
 \le\|\wedge^rC^{-1}\|\,\|\wedge^r\Theta_W^{-1}\|.
 }
\tag{RE23}
\]
The lower inequality follows by composing on the left with C; the upper follows by submultiplicativity. All forward and inverse conductor factors are the original ones. For C=L direct-sum L they are the maxima, over p+q=r, of the products of the original p- and q-exterior norms. Thus they are fixed finite factors as w varies, and the complete exponent 2 min(r,6) in delta survives the original conductor transport.

This operation is the actual trace-to-residue multiplier on the completed state algebra. It is not silently identified with the old linear conductor itself, with the nonlinear derivative DP, or with the growing arithmetic packet action. RE12, RE18 and RE23 provide the three specified comparisons to the original residue and Gamma calculations.

There is an exact signed-return consequence. Any fixed C0 or C has cutoff-independent determinant. Pulling all four original endpoint metrics through it adds the identical term 2 log|det C| at each endpoint, which cancels under (+,+,-,-). The singular metric loss in RE22 therefore cannot be subtracted from an old arithmetic action without also changing its specified receiver. The comparison bounds quantify its actual cost; they do not assign the missing native common-kernel or proper-source determinant value.

## 7. The entire reflected-trace relative spectrum, not just its determinant

There is a further exact value calculation in the same original Gamma metric RE18. Keep its full mass M_s. Set
\[
 D_E=2b(b+1),\quad D_O=6b^2(b+1)(b+2),\quad a=g-w,
\]
\[
 E_0=\begin{pmatrix}1&-b\\-b&m_4\end{pmatrix},\qquad
 O_0=\begin{pmatrix}b&-m_4\\-m_4&m_6\end{pmatrix}.
\]
These are G4's two parity blocks divided by their common scalar M_s; the formulas below explicitly restore that scalar. Direct multiplication in RE12 gives the two parity blocks of its even-in-t sector:
\[
 W_E=8\begin{pmatrix}1&-a\\-a&a^2-4gw\end{pmatrix},
\]
\[
 W_O=8\begin{pmatrix}a&-a^2+4gw\\-a^2+4gw&a^3-12agw\end{pmatrix}.
\tag{RE24}
\]
Their determinants are -256gw and -256gw(g+w)^2 respectively. In the odd-in-t sector the parity cross block is i64gw K_w, where
\[
 K_w=\begin{pmatrix}1&-2a\\-2a&3a^2-4gw\end{pmatrix},
 \qquad \det K_w=-(g+w)^2.
\]
The reverse cross block is its Hermitian adjoint. No cross term is omitted.

Put
\[
 t_E=\frac8{M_sD_E}(a^2-4gw-2ba+m_4),
\]
\[
 t_O=\frac8{M_sD_O}
       (am_6-2m_4a^2+8m_4gw+ba^3-12bagw),
\]
\[
 T_w=\operatorname{Tr}(E_0^{-1}K_wO_0^{-1}K_w),\qquad
 D_w=\frac{(g+w)^4}{D_ED_O},\qquad
 u_\pm=\sqrt{\frac{T_w\pm\sqrt{T_w^2-4D_w}}2}.
\tag{RE25}
\]
Every inverse here is an explicitly given positive two-by-two matrix; the entries are rational functions of b,g,w. The inner radical is nonnegative because it is the discriminant of the two squared singular values of E0^(-1/2) K_w O0^(-1/2), whose trace and determinant are exactly T_w,D_w.

The full spectrum of the original relative trace G8^(-1/2) W_w G8^(-1/2) is exactly
\[
 \boxed{
 \left\{
 \frac{t_E\pm\sqrt{t_E^2+1024gw/(M_s^2D_E)}}2,\quad
 \frac{t_O\pm\sqrt{t_O^2+1024gw(g+w)^2/(M_s^2D_O)}}2,\quad
 \pm\frac{64gw}{M_s}u_+,\quad
 \pm\frac{64gw}{M_s}u_-
 \right\}.}
\tag{RE26}
\]
This contains all eight values. The first two pairs follow from the exact traces and determinants of the generalized two-by-two eigenproblems. The second two pairs follow from the full Hermitian off-diagonal block, whose spectrum is plus and minus its singular values. This proves inertia (4,4) for every w>0 directly in the retained metric.

Their complete small-w limits are also explicit. Let
\[
 \alpha_E=\frac{8N_E}{M_sD_E},\qquad
 \alpha_O=\frac{8gN_O}{M_sD_O},
\]
\[
 n_E=\frac{32g}{M_sN_E},\qquad
 n_O=\frac{32g^2}{M_sN_O},\qquad
 \kappa_\pm=\frac{64g}{M_s}u_\pm\big|_{w=0}>0.
\]
Then the full asymptotic multiset is
\[
 \boxed{
 \{\alpha_E+O(w),\alpha_O+O(w),
 \kappa_+w+O(w^2),\kappa_-w+O(w^2),
 -\kappa_+w+O(w^2),-\kappa_-w+O(w^2),
 -n_Ew+O(w^2),-n_Ow+O(w^2)\}.}
\tag{RE27}
\]
The two finite positive directions are the critical rank-two trace. The other six disappear to first order in w=delta^2. Thus the order of the inverse cost in RE22 matches a directly evaluated loss of trace eigenvalues, rather than only a determinant count.

For a polynomial form of T_0, its numerator over D_E D_O is
\[
 \begin{aligned}
 \mathcal P(b,g)={}&45b^5+120b^4+108b^3+32b^2\
 &-(96b^4+168b^3+80b^2)g
 +(114b^3+156b^2+64b)g^2\
 &-(48b^2+24b)g^3+9bg^4.
 \end{aligned}
\tag{RE28}
\]
It is positive by its exact expression as the squared Hilbert--Schmidt norm in RE25. This polynomial and D_0=g^4/(D_E D_O) evaluate both kappa values with no unevaluated projection or large Gram.

These are spectral values for the explicitly transported finite trace form. They do not assign a negative full Weil pairing over the actual zeta zeros. In particular, varying w in RE8 does not assume the roots of every h_w are actual zeros. The Burnol theorem in the other continuation requires an actual divisor of 2xi with its exact multiplicities; that requirement is not bypassed by the geometric collision.

## 8. An explicit exceptional-characteristic trace loss with no dimension loss

The perfect residue calculation also supplies a concrete specialization map for an earlier programme issue. Work over the actual coefficient ring O=Z[1/2] and the finite completed local algebra
\[
 \mathcal B_{3,O}=O[\epsilon,t]/(\epsilon^3,t^2-3\epsilon^2).
\tag{RE29}
\]
It is free of rank six with basis 1,epsilon,epsilon^2,t,t epsilon,t epsilon^2. Its precise atlas target is h(r)=r^3(r+1), with A=1,B=C=D=0 and original cubic coefficient one. In O[r]/h, the polynomial e0=1+r^3 is idempotent: e0^2-e0=r^3(r+1)(1-r+r^2). The maps 1->e0, epsilon->e0 r and t->e0 t identify RE29 with that primary component of the completed fibre. On it r^3=0 and h'(r)=3r^2, proving both compositions by the displayed generators. The inherited atlas residue is [epsilon^2]q/(1+epsilon). The functional below is its multiplication by the actual unit 1+epsilon, with inverse 1-epsilon+epsilon^2. Since epsilon J=0, this unit change does not change the trace identity in RE30.

Define ell(t epsilon^2)=1 and ell to be zero on the other five basis elements. The residue pairing is perfect with unit determinant up to sign. The Jacobian multiplier and trace form are
\[
 \mathsf J=2t^3=6t\epsilon^2,
 \qquad\operatorname{Tr}(fg)=\ell(\mathsf Jfg),
 \qquad\mathsf{Tr}=\operatorname{diag}(6,0,0,0,0,0).
\tag{RE30}
\]
These identities follow either by multiplying the six basis elements or by RE4; in particular no nilpotent relation is deleted before the trace is taken.

Under the exact specialization O->F3 the algebra is
\[
 \mathbb F_3[\epsilon,t]/(\epsilon^3,t^2),
\]
still six dimensional, and its perfect residue pairing stays invertible. Its entire ordinary trace pairing, however, becomes zero because the displayed multiplier is zero. Thus the trace radical has dimension five in characteristic zero and six after this specialization. The specialization does not kill the algebra or its residue duality.

There is an exact module accounting. The cokernel of the trace map B->B* is O/(6) direct-sum O^5. Its Tor_1 over O with F3 is F3, computed from the two-term multiplication-by-6 resolution of O/(6). Tensoring that exact sequence identifies precisely the one new trace-kernel direction. The other five kernel directions were already the characteristic-zero trace radical. This is a calculated finite coefficient-stage loss, not an assertion about a hypothetical arithmetic Frobenius realization.
