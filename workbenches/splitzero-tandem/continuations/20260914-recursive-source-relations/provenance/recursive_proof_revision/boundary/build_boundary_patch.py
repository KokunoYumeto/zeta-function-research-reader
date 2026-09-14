from pathlib import Path
import hashlib, json, difflib, re

ROOT=Path(r'workspace:')
BASE=ROOT/'work/cumulative_next_edition_staging_20260913_v19/reader'
OUT=ROOT/'work/backpropagation_20260913/boundary'
for directory in ['originals/tex','revised/tex','fragments','proofs','reviews','evidence']:
    (OUT/directory).mkdir(parents=True,exist_ok=True)
def sha(b): return hashlib.sha256(b).hexdigest()
def norm(s): return s.replace('\r\n','\n')
records=[]
def revise(name, operations):
    p=BASE/'tex'/name
    old=p.read_bytes(); source=norm(old.decode('utf-8-sig')); updated=source
    for label,needle,replacement in operations:
        assert updated.count(needle)==1,(name,label,updated.count(needle))
        updated=updated.replace(needle,replacement)
    (OUT/'originals/tex'/name).write_bytes(old)
    new=updated.encode('utf-8'); (OUT/'revised/tex'/name).write_bytes(new)
    diff=''.join(difflib.unified_diff(source.splitlines(True),updated.splitlines(True),fromfile='originals/tex/'+name,tofile='revised/tex/'+name))
    (OUT/'evidence'/(name+'.diff')).write_text(diff,encoding='utf-8')
    records.append(dict(source=str(p),original_sha256=sha(old),revised='revised/tex/'+name,revised_sha256=sha(new),changes=[x[0] for x in operations]))
def fragment(name,s):
    (OUT/'fragments'/name).write_text(s,encoding='utf-8'); return s

xd=fragment('xd_u_connection.tex',r'''
\subsubsection{The full singular parameter connection on this same cyclic family}

The original determinant (XD19) is retained.  Its complete parameter
connection is now computed on the same coefficient quotient, before
taking traces.  For every original column $0\le b<q$, perform the
unique monic division
\[
 \Phi_t(S)S^b=(\chi(S)-t)Q_b^\Phi(S,t)+R_b^\Phi(S,t),
 \qquad \deg R_b^\Phi<q,\quad\deg Q_b^\Phi\le b+1.
 \tag{XD.u1}
\]
Write $C_\chi(t)$ for the matrix of the remainders and $B_\chi$ for
the matrix of the derivatives $(Q_b^\Phi)'$, in the unchanged basis.
The differential gives the exact, already reduced identity
\[
 \operatorname{red}_{u,t}(\Phi_t S^b)=R_b^\Phi-u(Q_b^\Phi)',\qquad
 C_\chi(t)=\Phi_t(A(t)).                              \tag{XD.u2}
\]
The second equality uses ordinary multiplication in $\mathbb C[S]/(\chi-t)$;
the first retains its differential correction.  Comparing division
coefficients above degree $q$ shows that only the constant coefficient
of $Q_b^\Phi$ can depend on $t$: both $-tS^{b+1}$ and $-tQ_b^\Phi$
have degree at most $q$.  Differentiation removes that constant.
Its leading term is $S^{b+1}/(q+1)$.  Therefore
\[
 (B_\chi)_{bb}=\frac{b+1}{q+1},\quad
 (B_\chi)_{rb}=0\ (r>b),\quad
 \partial_t B_\chi=0,\quad \operatorname{Tr}B_\chi=q/2.
 \tag{XD.u3}
\]
On degrees zero and one of the original two-term complex the connections
are respectively
\[
 \nabla_u^0=\partial_u-\Phi_t/u^2+1/u,\qquad
 \nabla_u^1=\partial_u-\Phi_t/u^2.                    \tag{XD.u4}
\]
Indeed, writing $L=u\partial_S+\chi-t$, direct commutators give
$[L,\partial_u]=-\partial_S$ and
$[L,-\Phi_t/u^2]=-(\chi-t)/u$.  Hence
$\nabla_u^1L=L\nabla_u^0$.  Reduction by (XD.u2) proves the full
top connection and period differential:
\[
 \Omega_u=-C_\chi(t)/u^2+B_\chi/u,
 \quad\nabla_u=\partial_u+\Omega_u,
 \quad \partial_u\Pi=\Pi\Omega_u,
 \quad\Omega_t=-A(t)/u,\quad\partial_t\Pi=\Pi\Omega_t.
 \tag{XD.u5}
\]
All these statements hold locally on every retained branch of $u\ne0$.
One may deform the labelled contours within the same decay sectors;
the tail estimate (XD5), locally uniform in $u\ne0$, removes the
connecting arcs.  Differentiation in $u$ inserts $-\Phi_t/u^2$,
so (XD.u2) proves the asserted period equation without changing a ray
orientation.  The scalar commutators
$[\partial_u-\Phi_t/u^2,\partial_t-S/u]=0$, with the same
degree-zero correction, prove flatness.  Equivalently the retained
matrices obey
\[
 \partial_u\Omega_t-\partial_t\Omega_u+
                    [\Omega_u,\Omega_t]=0.           \tag{XD.u6}
\]
Taking the exterior power of (XD.u5) gives
$\partial_u\det\Pi=(-\mathcal F/u^2+q/(2u))\det\Pi$,
where $\mathcal F$ is precisely (XD13).  If
$\zeta=e^{2\pi i/(q+1)}$, $\beta_b=(b+1)/(q+1)$ and
$W_{jb}=\zeta^{j(b+1)}-1$, its retained constant is
\[
 K_q=(q+1)^{-q/2}e^{\pi i q/2}
          \det W\prod_{b=0}^{q-1}\Gamma(\beta_b),\qquad
 \det\Pi=K_q u^{q/2}e^{\mathcal F/u}.                \tag{XD.u7}
\]
This is exactly (XD16)--(XD19): each original column factor is
$[(q+1)u]^{\beta_b}e^{\pi i\beta_b}\Gamma(\beta_b)/(q+1)$
on the specified branch, and $\sum_b\beta_b=q/2$.
It adds the full singular connection to the earlier determinant proof;
the determinant itself is the same proved result.

The packet polynomial $h$ in the marked-product calculation and the
cyclic polynomial $\chi_{h,k}$ have distinct specified coefficient
maps.  Formula (XD.u1) applies literally to the present $\chi$.
For $k=1$, $\chi_{h,1}=h$ via $S\mapsto s$, and every displayed
matrix is the matrix $C_h,B_h$ under that exact variable isomorphism.
For general $k$ the product lattice is instead connected to $E$
at the marked fibre by the original injection
$\eta_k[P]=\upsilon_h^{\otimes k}P(\sum_i s_i)1$.
Its full source identity is
$q_{\mathscr B}^{\widehat\otimes k}\mathcal V_{h,k}P
=\sigma_h^{\widehat\otimes k}\eta_k[P]$.
In the unweighted polynomial product family its cyclic relation has
the explicit parameter image
$[\chi(S)P(S)]=\sum_i[t_iQ_i-u\partial_iQ_i]$ whenever
$\chi(S)P(S)=\sum_i h(s_i)Q_i$ in the original polynomial ring.
Thus the two connections have a common specified marked-fibre map;
no equality of the two families or their ranks is inserted.
''')
revise('deligne_exponential_determinant_extension.tex',[
 ('XD.u1--u7; full parameter matrix and retained determinant',r'\subsubsection{The determinant, including every monomial factor}',xd+'\n'+r'\subsubsection{The determinant, including every monomial factor}')])

ds=fragment('ds_source_connection.tex',r'''
The same family now also has the full $u$-connection.  Use the
literal division (XD.u1) for this $\chi$, with matrices $C_\chi(t)$,
$B_\chi$ and $\Omega_u=-C_\chi(t)/u^2+B_\chi/u$.
The connections on the two terms of (DS67) are
\[
 \partial_u-\Phi_t/u^2+1/u\quad\hbox{and}\quad
 \partial_u-\Phi_t/u^2,                              \tag{DS70}
\]
in degrees zero and one.  Their chain identity is the commutator
$[u\partial_S+\chi-t,\partial_u-\Phi_t/u^2]
=-(u\partial_S+\chi-t)/u$, proved before quotienting in (XD.u4).
On an ordered product of $k$ such polynomial factors, the same
calculation in cochain degree $j$ gives
\[
 \nabla_u^{(j)}=\partial_u-\frac{\sum_i\Phi_{t_i}(S_i)}{u^2}
                         +\frac{k-j}{u}.             \tag{DS71}
\]
Each summand of the exterior differential has commutator $-L_i/u$;
the adjacent-degree scalar difference is $+L_i/u$, so all terms
cancel with their original exterior signs.  This includes the
non-top degrees rather than imposing the top formula on them.

There is an exact source lift for the fixed cyclic observer already
used in (DS69).  On parameter-dependent vectors of its original
admitted theta-source domain define
\[
 \nabla_{u,N}^{\rm src}=\partial_u+r_N\Omega_u j_E,
 \qquad \nabla_{t,N}^{\rm src}=\partial_t+r_N\Omega_t j_E,
 \qquad\Omega_t=-(A+t\mathcal R)/u.                  \tag{DS72}
\]
The domain is the original one on which $j_E$, $D^{(k)}$, $r_N$ and
the boundary primitive are defined, with holomorphic parameter
coefficients on a branch of $u\ne0$.  The maps $j_E,r_N$ are
constant in these parameters.  Multiplying by $j_Er_N=I$ gives
\[
 j_E\nabla_{a,N}^{\rm src}=(\partial_a+\Omega_a)j_E,
 \qquad\nabla_{a,N}^{\rm src}r_N=r_N(\partial_a+\Omega_a),
 \qquad a=u,t.                                      \tag{DS73}
\]
The source splitting is the exact identity
$x=r_Nj_Ex+(x-r_Nj_Ex)$, with its second term in $\ker j_E$.
On that kernel (DS72) is ordinary parameter differentiation.
Since $r_Nj_Er_Nj_E=r_Nj_E$, the full source curvature equals
$r_N(\partial_u\Omega_t-\partial_t\Omega_u+
[\Omega_u,\Omega_t])j_E=0$ by (XD.u6).
The original source differential still gives, for each $a=u,t$,
\[
 [D^{(k)},\nabla_{a,N}^{\rm src}]
   =r_N[A,\Omega_a]j_E+dK_N\Omega_a j_E.             \tag{DS74}
\]
To prove this, insert $D^{(k)}r_N=r_NA+dK_N$ and
$j_ED^{(k)}=Aj_E$ into the commutator; $D^{(k)}$ commutes with
parameter differentiation.  Every term has the original source
target, and $K_N\Omega_a j_E$ is the displayed full primitive.
Thus the parameter-flat source observation and the original Euler
action are related by their exact commutator, retaining its
coefficient part and theta boundary.  No source norm or full Taylor
unit in $r_N$ has been changed.
''')
needle='The logarithmic comparison retains the original exact coefficient\nsequence'
revise('deligne_split_sidebar.tex',[
 ('DS70--74; degree-correct chain connection and actual theta-source commutator',needle,ds+'\n'+needle),
 ('DS69 forward reference made current','The exponential note\'s contour periods and finite-field\nspecializations develop this new family further; equations\n(DS66)--(DS69) are its complete coefficient, cohomological and\nsource-level join to the logarithmic machinery in this sidebar.',
  'The exact period equation (XD.u5), chain terms (DS70)--(DS71),\nand source connection and commutator (DS72)--(DS74) now develop this\nsame family in both parameters. The finite-field boundary extension\nand the full single-primary calculation are included with their exact\nspecialization hypotheses. Equations (DS66)--(DS74) give the\ncoefficient, cohomological and source-level join used here.')])

dt=fragment('dt_u_translation.tex',r'''
\subsection{Translation of the full singular connection and boundary character}
The same retained scalar $h_a(t)=-\Phi(-a)-ta$ also controls the
$u$ direction.  Write $\nabla_u^a$ for the degree-one connection
of the translated phase and $\nabla_u$ for that of the original
phase, both including their exact matrices (XD.u1)--(XD.u5).
Literal substitution in the full polynomial complex gives
\[
 T_a\nabla_u^aT_a^{-1}=\nabla_u-\frac{h_a(t)}{u^2}I,
 \qquad\nabla_u(f_aT_av)=f_aT_a\nabla_u^av.          \tag{DT.14}
\]
Indeed $T_a\Phi_t^aT_a^{-1}=\Phi_t+h_a(t)$ and $T_a$ is
independent of $u$.  Differentiating the unchanged exponential
gives $\partial_u f_a=-h_a(t)f_a/u^2$, proving the second identity
term by term.  In degree zero each side additionally contains
the same $1/u$ term.  Together with DT.3 and DT.6 this proves a
flat two-parameter intertwiner on $u\ne0$, with its singular
scalar retained.  In matrix form, if $\Omega_u^a,\Omega_u$ are
the two original remainder matrices,
\[
 C_a\Omega_u^a C_a^{-1}
       =\Omega_u-h_a(t)I/u^2.                        \tag{DT.15}
\]
It follows equally by differentiating DT.6 in $u$, using
invertibility of the original period matrix.  Its determinant
has the scalar $f_a^q$, in agreement with the complete constant
and phase in (XD.u7).

Before fixing $u=u_0$ in the finite-field calculation, the same
polynomial substitution is a morphism over the actual parameter
scheme. Use the specified coefficient map
$R_0[a]\to\mathbb F_Q$ of characteristic $p>d=q+1$, the same
$\ell\ne p$, and the nontrivial additive character $\psi$ fixed
in the finite-field comparison below.  Write
$\mathscr U=\mathbb G_{m,\mathbb F_Q,u}\times
\mathbb A^1_{\mathbb F_Q,t}$, and let
$\pi_X:\mathbb A^1_X\times\mathscr U\to\mathscr U$ and
$\pi_S:\mathbb A^1_S\times\mathscr U\to\mathscr U$ be the
literal projections. Define the full derived complexes
\[
 \mathcal F=R\pi_{X!}\mathcal L_\psi((\Phi(X)-tX)/u),\qquad
 \mathcal F_a=R\pi_{S!}\mathcal L_\psi((\Phi_a(S)-tS)/u).
\]
The base-defined isomorphism $\sigma_a(X,u,t)=(X+a,u,t)$
satisfies $\pi_S\sigma_a=\pi_X$.  Its exact derived
compact-support direct-image identity, in every cohomology degree, is
\[
 \mathcal F_a\simeq\mathcal F\otimes
                    \mathcal L_\psi(h_a(t)/u).        \tag{DT.16}
\]
The Artin--Schreier torsor addition proving DT.12 works over
this coefficient ring without any change, and the character line
is pulled back from the parameter scheme, so it factors out of
the compact-support complex.  Restricting to a specified
$(u_0,t_0)$ is exactly DT.12--DT.13.  At fixed $t_0$, its
possible singular boundary character is therefore the full
$\mathcal L_\psi(h_a(t_0)/u)$; it cannot be replaced by its
value at a nonzero $u_0$.  This is the precise family map used
when passing from the translated single-primary phase to its
local boundary representation.
''')
revise('deligne_translation_bridge.tex',[
 ('DT14--16; complete u gauge and unfrozen finite-field character',r'\subsection{The original positive forms and their control operators}',dt+'\n'+r'\subsection{The original positive forms and their control operators}')])

sc=fragment('sc_two_parameter_curvature.tex',r'''
\subsubsection{The full two-parameter curvature in the same original frames}
Allow the original $u\ne0$ to vary on a retained contour branch,
keeping the same $\chi$, $F$, $I$, $G_N$, and target metric.
Use $C_\chi(t)$ and $B_\chi$ from the literal division (XD.u1).
For $a=u,t$ put
\[
 \Omega_u=-C_\chi(t)/u^2+B_\chi/u,
 \qquad\Omega_t=-(A+t\mathcal R)/u,
 \qquad Y_a=\Pi\Omega_a I,
 \qquad Z_a=N\Pi\Omega_a I.                         \tag{SC.u1}
\]
The convergence and full reduction in (XD.u1)--(XD.u5) prove
these are precisely $\partial_aY$ and its original normal
projection.  For every $a,b\in\{u,t\}$, the complete Hermitian
matrix of curvature coefficients is
\[
 \boxed{\partial_{\bar a}\partial_b\log\det H
          =\operatorname{Tr}(H^{-1}Z_a^*Z_b).}         \tag{SC.u2}
\]
For the proof, holomorphy gives $\partial_bH=Y^*Y_b$,
$\partial_{\bar a}H=Y_a^*Y$, and
$\partial_{\bar a}\partial_bH=Y_a^*Y_b$.
The derivative of $H^{-1}$ is
$-H^{-1}Y_a^*YH^{-1}$.  Substitution in the logarithmic
determinant derivative gives
$\operatorname{Tr}(H^{-1}Y_a^*(I-YH^{-1}Y^*)Y_b)$.
Since $N^2=N=N^*$, this is (SC.u2).  In particular every
linear combination has value
$\operatorname{Tr}(H^{-1}(\sum_b v_bZ_b)^*
(\sum_b v_bZ_b))\ge0$, using the original positive $H$.
This proves the mixed coefficients as well as both diagonal
ones, with the original one-form ordering
$du\wedge d\bar u$, $dt\wedge d\bar u$,
$du\wedge d\bar t$, $dt\wedge d\bar t$.

At $t=0$, $C_\chi(0)=\Phi(A)$ is a polynomial in the
original action, so $C_\chi(0)I=I\Phi(A_F)$.
Consequently the order-two term has zero normal projection
there, while the complete first-order term remains:
\[
 Z_u(u,0)=u^{-1}N\Pi B_\chi I,\qquad Z_t(u,0)=0,
 \quad
 \partial_{\bar u}\partial_u\log\det H(u,0)
 =|u|^{-2}\operatorname{Tr}
       (H^{-1}I^*B_\chi^*\Pi^*N\Pi B_\chi I).
 \tag{SC.u3}
\]
Thus the earlier stationary $t$ tangent retains the calculated
$u$ normal map.  No invariance of $F$ under $B_\chi$ is assumed.
For $t\ne0$, the complete expression in (SC.u1) retains both
$-C_\chi(t)/u^2$ and $B_\chi/u$ before taking its squared norm.

The positive original source Gram is constant in both parameters.
The transported metric therefore has the exact derivatives
\[
 \partial_a\widetilde G_N
       =-\Pi^{-*}G_N\Omega_a\Pi^{-1},\qquad
 \partial_{\bar a}\widetilde G_N
       =-\Pi^{-*}\Omega_a^*G_N\Pi^{-1},\quad a=u,t.
 \tag{SC.u4}
\]
They follow from $\partial_a\Pi^{-1}=-\Omega_a\Pi^{-1}$;
holomorphy gives $\partial_a\Pi^{-*}=0$.
In the product rule for $Y^*\widetilde G_NY$ these terms
cancel the derivatives of $Y$ and $Y^*$, giving exactly the
fixed $I^*G_NI$.  Formula (SC25) is its $a=t$ case.
The full original source comparison is (DS72)--(DS74);
in particular its theta boundary $dK_N\Omega_a j_E$ remains
in the Euler commutator.  All curvature coefficients (SC.u2)
also apply to $\log\det(G_{N,F}^{-1}H)$, since the determinant
of $G_{N,F}$ is constant in both parameters.

For every neighboring inclusion $J$ in (SC31), the identity
$h_J=v_{N,J}b_{N,J}$ in (SC35) now holds on this same
two-parameter branch.  Its $u$ and mixed logarithmic
derivatives are the corresponding formula (SC.u2) with
$I=J$, $H=J^*\Pi^*\Pi J$, and its own actual normal
projection.  For a zero-column inclusion its determinant is
$1$ and every derivative is zero; for the full inclusion the
normal projection is zero.  This propagates the singular
connection through all three retained minor maps rather than
replacing a rectangular minor by the full determinant.

\subsubsection{The full primary matrix now evaluates every original ideal volume}
The completed single-primary proof specializes this calculation
to the original $h(s)=(s-\rho)^m$, $t=0$, with $n=m+1$,
$c=-(-\rho)^n/n$ and $y=s-\rho$.  Its exact Pascal matrix
is $P_{ab}=\binom ba\rho^{b-a}$ for $a\le b$, zero otherwise;
$e_s=e_yP$ and $P^{-1}$ has $-\rho$ in place of $\rho$.
Retain its full ordered period matrix
\[
 \Pi_s=e^{c/u}WD(u)P,\quad
 W_{jb}=e^{2\pi i j(b+1)/n}-1,\quad
 D(u)_{bb}=d_bu^{\beta_b},\quad
 \beta_b=(b+1)/n,\quad
 d_b=n^{\beta_b-1}e^{\pi i\beta_b}\Gamma(\beta_b).
 \tag{SC.u5}
\]
The proof SP.10--15 of this formula is included in full: it
uses the original contour translation, the decaying endpoint
connectors and the gamma radial integral, so both $c$ and all
phases in (SC.u5) have their original values.

For an original invariant constituent of dimension $p$, put
$r=m-p$ and let $J_r$ have the literal polynomial columns
$y^r,y^{r+1},\ldots,y^{m-1}$ in the original $s$ basis.
Every ideal of the primary algebra is $(y^r)/(y^m)$ by
division in $\mathbb C[y]$, so its specified inclusion has
the unique form $I=J_r C_F$ for an invertible constant
$p$-by-$p$ matrix $C_F$.  Let $W_r$ select the columns
$r,\ldots,m-1$ from $W$, and $D_r$ the same diagonal entries
from $D$.  Since $PJ_r$ is the literal inclusion of those
translated coordinates,
\[
 Y=e^{c/u}W_rD_r C_F,\qquad
 H=e^{2\operatorname{Re}(c/u)}
            C_F^*D_r^*(W_r^*W_r)D_r C_F.             \tag{SC.u6}
\]
The exact root-of-unity sum gives
$W_r^*W_r=n(I_p+\mathbf1_p\mathbf1_p^*)$:
including the zero row adds zero, and expansion of the
three nonconstant character sums leaves $n\delta_{ab}+n$.
This matrix has eigenvalue $n(p+1)$ on $\mathbf1_p$
and eigenvalue $n$ on its perpendicular complement, so
its determinant is $n^p(p+1)$.  Taking determinants in
the unchanged matrices therefore gives
\[
 \boxed{\det H(u,0)=|\det C_F|^2 n^p(p+1)
       e^{2p\operatorname{Re}(c/u)}
       \prod_{b=r}^{m-1}|d_b|^2|u|^{2\beta_b}.}       \tag{SC.u7}
\]
No frame determinant, contour phase or Taylor coefficient
in the original source Gram $G_{N,F}=I^*G_NI$ is removed.
The determinant of the actual comparison is exactly
the right side divided by $\det G_{N,F}$; its complete
matrix is $G_{N,F}^{-1}$ times (SC.u6).
For $p=0$ all products and determinants are empty and equal
one, and for $p=m$ this is the full determinant formula.

In particular $Y(F)=\operatorname{im}W_r$ is constant as
$u$ varies on $u\ne0$: $D_r$ and $C_F$ are invertible.
Thus its normal $u$ derivative and its $u$ curvature vanish
on this exact primary slice.  Equivalently,
$PB_hP^{-1}=\operatorname{diag}(\beta_b)$ preserves
$PJ_r(F)$ in (SC.u3).  This evaluates that previously
retained $B_h/u$ normal term on the actual primary ideals.
The $t$-normal map and its full acceleration are still
(SC12)--(SC13); the tensor boundary requires the ordered
character products calculated in TP/TPF rather than
propagating the one-factor invariant-space dimension.
''')
revise('sga_constituent_period_curvature.tex',[
 ('SC.u1--u4; u curvature, mixed Hessian, source metric and all three minors',r'\subsubsection{The exact derived base change at a collision}',sc+'\n'+r'\subsubsection{The exact derived base change at a collision}')])

pc=fragment('pc_u_kernel.tex',r'''
\subsubsection{The singular connection on the retained critical kernel}
The fixed-$u$ formulas above now extend on each original branch
of $u\ne0$ using (XD.u1)--(XD.u5), with $\chi=h$ at $k=1$.
Their coefficient identification is exactly (PC4), and the full
$\upsilon_h$ in (PC6)--(PC8) remains unchanged.  Put
$\Omega_u=-C_h(t)/u^2+B_h/u$ in these original coordinates.
The observer and its full kernel obey
\[
 \mathcal C_{h,u,t}=\mathcal C_h\Pi(u,t)^{-1},\quad
 \ker\mathcal C_{h,u,t}=\Pi(u,t)E_o,\quad
 \partial_u\mathcal C_{h,u,t}
       =\mathcal C_h(C_h(t)/u^2-B_h/u)\Pi^{-1}.
 \tag{PC.u1}
\]
Invertibility proves the first two identities; differentiating
$\Pi^{-1}\Pi=I$ with (XD.u5) proves the third.
The displayed critical target, all local inverse units in (PC15),
and the right inverse $\Pi|_{E_c}\mathcal R_c$ are unchanged.

For $Y=\Pi I$, $H=Y^*Y$ and $N=I-YH^{-1}Y^*$ from (PC22),
the normal $u$ map is
\[
 N\partial_uY=N\Pi(-C_h(t)/u^2+B_h/u)I.              \tag{PC.u2}
\]
The full curvature and both metric derivatives are exactly
(SC.u2)--(SC.u4), now on this particular kernel inclusion.
To check the marked boundary parameter $t=0$ directly,
$C_h(0)=\Phi_h(A)$ preserves the ideal $E_o$, so the
normal image of its order-two term is zero; its retained
first-order term is $u^{-1}N\Pi B_hI$.
Thus
\[
 \partial_{\bar u}\partial_u\log\det H(u,0)
 =|u|^{-2}\operatorname{Tr}
   (H^{-1}I^*B_h^*\Pi^*N\Pi B_hI),\qquad
 \partial_{\bar u}\partial_t\log\det H(u,0)=0.
 \tag{PC.u3}
\]
The second equality follows because the normal $t$ map is zero
at $t=0$, as already proved in (PC23).  Empty and full kernels
have zero normal maps and use the same empty determinant
convention.  At other $t$ the complete two terms of (PC.u2),
their cross pairing and the mixed $u,t$ coefficient remain.

For each cyclic tensor packet (PC29), apply this calculation
to the literal polynomial $\chi_{h,k}$ with its degree $q_k$,
not to a product of one-factor period matrices.  Replace
$h,E_o,I,\mathcal C_h$ by
$\chi_{h,k},F_k,I_k,\mathcal C_k$ in (PC.u1)--(PC.u3).
Their proofs use precisely the already proved ideal and
intertwining identities (PC34)--(PC38), so this gives the
full $u$ derivative of the same critical observation and the
two-parameter curvature of every existing kernel minor.
The marked-product period map instead has domain
$E_h^{\otimes k}$ and restricts to $E_k$ through the exact
weighted injection $\eta_k$ in (PC29).  Its retained
rectangular period form is
$\eta_k^*\Pi_{\rm prod}^*\Pi_{\rm prod}\eta_k$.
These typed maps and the parameter cyclic relation in
(XD.u7)'s following paragraph carry the two families together;
their different coefficient domains are never silently identified.
''')
revise('period_critical_kernel_bridge.tex',[
 ('PC.u1--u3; exact u derivative and critical-kernel curvature through every tensor packet',r'\subsubsection{The exact completed tensor comparison and its collision jets}',pc+'\n'+r'\subsubsection{The exact completed tensor comparison and its collision jets}')])

lc=fragment('lc_u_control.tex',r'''
The same complete transport now varies in $u\ne0$ as well as $t$.
With $\Omega_u=-C_\chi(t)/u^2+B_\chi/u$ from (XD.u1)--(XD.u5),
the precise derivative equations are
\[
 \partial_u\widetilde G=-\Pi^{-*}G\Omega_u\Pi^{-1},\qquad
 \partial_{\bar u}\widetilde G=-\Pi^{-*}\Omega_u^*G\Pi^{-1},
 \quad
 \partial_u\widetilde L_t=\Pi[\Omega_u,L_t]\Pi^{-1},
 \quad
 \partial_u\widetilde A_t=\Pi[\Omega_u,A_t]\Pi^{-1}.
 \tag{LC.u1}
\]
Here $G,A_t,L_t$ are independent of $u$.  Each formula follows
by differentiating its literal definition (LC12), inserting
$\Pi_u=\Pi\Omega_u$ and
$(\Pi^{-1})_u=-\Omega_u\Pi^{-1}$, and retaining both product
terms.  Thus the full numerical-range identity (LC10)--(LC12)
holds at every such $u$ with exactly the same original bound
$E_N(t)$, while its moving metric has the displayed derivatives.
This statement makes no bound on the unweighted target metric.
For the original source lift the exact $u$ commutator is
$r_N[A,\Omega_u]j_E+dK_N^{\rm prim}\Omega_u j_E$
by (DS74); the primitive is in the original cochain degree.

The actual comparison numbers used in (LC14)--(LC16) are now
the eigenvalues $m(u,t),M(u,t)$ of
$G^{-1}\Pi(u,t)^*\Pi(u,t)$.  Their original proof by two
quadratic-form inequalities applies pointwise without alteration.
The full $u$ and mixed curvatures of this same constituent are
(SC.u1)--(SC.u4), with its actual inclusion $I$ and Gram $I^*GI$.
In particular the exact order-two and order-one normal terms
must both be used at $t\ne0$; the original $t$-curvature
comparison (LC15) remains its own calculated matrix entry.
''')
revise('period_laplacian_control_bridge.tex',[
 ('LC.u1; u transport of action, Laplacian, metric and original source primitive',r'\subsubsection{The exact finite comparison with constituent curvature}',lc+'\n'+r'\subsubsection{The exact finite comparison with constituent curvature}')])

dc=fragment('dc_u_diamond.tex',r'''
The entire diamond now also has its exact singular $u$ equation.
Use the division (XD.u1) for the same cyclic $\chi$, and write
$C_\chi(t),B_\chi$ in its unchanged increasing-power basis.
On every retained contour branch let
$T_{s,u,t}=T_s\Pi(u,t)^{-1}$.  For all four formal roles,
\[
 \boxed{\partial_uT_{s,u,t}
       =T_s(C_\chi(t)/u^2-B_\chi/u)\Pi(u,t)^{-1},
          \qquad s\in\{a,b,d,l\}.}                 \tag{DC31}
\]
This follows from $\partial_u\Pi^{-1}=-\Omega_u\Pi^{-1}$
and the original constant maps $T_s$, with
$\Omega_u=-C_\chi(t)/u^2+B_\chi/u$.
The same composition gives kernels $\Pi(u,t)K_s$ and right
inverses from (DC23), so all intersections, sums and exact
quotients in (DC24) remain valid in both parameters.
Multiplying (DC31) by $f_a,f_b$ gives the common equation
because $f_aT_a=f_bT_b=T_d$; the joint equation has the same
two components.  The factorization maps (DC18)--(DC19) are
parameter-independent and commute with this derivative for
the same reason.  This proves the full differential diamond.

The actual circle weights of (DC6)--(DC8) are unchanged.
Let $D_\nu=\operatorname{diag}(\nu_n)_{n\in\mathcal Z_L}$
in the stated circle coordinate basis, including an empty
matrix for an empty sample set.  Its exact pulled-back
positive semidefinite form on the period coordinates is
\[
 H_b^{\rm obs}=\Pi^{-*}T_b^*D_\nu T_b\Pi^{-1},
 \quad\ker H_b^{\rm obs}=\Pi K_b,\qquad
 \partial_uH_b^{\rm obs}
       =-\Pi^{-*}T_b^*D_\nu T_b\Omega_u\Pi^{-1},
 \quad
 \partial_{\bar u}H_b^{\rm obs}
       =-\Pi^{-*}\Omega_u^*T_b^*D_\nu T_b\Pi^{-1}.
 \tag{DC32}
\]
The kernel identity follows since all retained $\nu_n$ are
strictly positive, so zero norm is precisely $T_b\Pi^{-1}x=0$.
The derivatives follow by the same inverse-matrix product
rule, keeping the original weights in every term.
Under (DC28), the shared and new circle sums therefore still
use exactly those same $\nu_n$; the map itself is constant in
$u,t$.  The actual polynomial lift (DC29), all inverse-unit
factors and the receiving support labels remain unchanged.
''')
revise('circle_critical_observation_diamond.tex',[
 ('DC31--32; four u equations and original weighted circle metric',
  'All coefficient arrows above have their original supported\nSplit-Zero lifts:',dc+'\nAll coefficient arrows above have their original supported\nSplit-Zero lifts:')])

rcx=fragment('rcx_two_parameter_jets.tex',r'''
\subsubsection{Every $u,t$ jet and the retained translation derivatives}
The recursion (RCX30) now has its full two-parameter version on
each original branch of $u\ne0$.  Use the exact matrices
$\Omega_u=-C_\chi(t)/u^2+B_\chi/u$ and
$\Omega_t=-A_t/u$ from (XD.u1)--(XD.u6).  Starting at
$Q_{0,0}=I$, define
\[
 Q_{r+1,s}=\partial_uQ_{r,s}+\Omega_uQ_{r,s},\qquad
 Q_{r,s+1}=\partial_tQ_{r,s}+\Omega_tQ_{r,s}.          \tag{RCX.u1}
\]
These prescriptions are compatible.  The commutator of their
two left-acting differential operators is multiplication by
$\partial_u\Omega_t-\partial_t\Omega_u+
[\Omega_u,\Omega_t]=0$.  Starting at $I$ they therefore give
the same matrix for every ordering with $r$ $u$ derivatives
and $s$ $t$ derivatives.  The product rule and
$\partial_a\Pi=\Pi\Omega_a$ prove by induction the exact
identity
$\partial_u^r\partial_t^s\Pi=\Pi Q_{r,s}$.
All coefficient matrices remain in the algebra on the same
remainder frame.  In particular, retaining the order of
every product,
\[
 \begin{split}
 Q_{1,0}&=-C_\chi/u^2+B_\chi/u,\\
 Q_{2,0}&=C_\chi^2/u^4+
       (2C_\chi-C_\chi B_\chi-B_\chi C_\chi)/u^3
                         +(B_\chi^2-B_\chi)/u^2,\\
 Q_{1,1}&=C_\chi A_t/u^3+(A_t-B_\chi A_t)/u^2.
 \end{split}                                      \tag{RCX.u2}
\]
Indeed $\partial_uC_\chi=\partial_uB_\chi=0$ and
$\partial_u(-A_t/u)=A_t/u^2$.  Expanding
$\partial_u\Omega_u+\Omega_u^2$ and
$\partial_u\Omega_t+\Omega_u\Omega_t$ gives exactly
these three formulas.  Setting $r=0$ gives every earlier
matrix (RCX30)--(RCX32), including its $3R^2/u^2$ term.

For $H=\Pi^*\Pi$ the exact derivative is
$\partial_uH=H\Omega_u$ and
$\partial_{\bar u}H=\Omega_u^*H$.  Thus along an arbitrary
specified differentiable curve $(u(s),t(s))$ the metric
derivative in (RCX13)--(RCX17) is the actual Hermitian matrix
\[
 \dot H=\Omega_{\rm path}^*H+H\Omega_{\rm path},
 \qquad\Omega_{\rm path}=\dot u\,\Omega_u+\dot t\,\Omega_t.
 \tag{RCX.u3}
\]
Substitution into (RCX13) supplies both original Rayleigh
quotients and their exact signed difference, including the
full singular $u$ terms.  The constituent Hermitian Hessian
is (SC.u2) on the same $I,H_F$, so the pure $t$ fourth-jet
identity (RCX26)--(RCX28) is retained as that exact slice.
Differentiating the already proved forced equation (RCX33)
also gives its complete $u$ descendant:
\[
 2u\Pi_{tt}+u^2\Pi_{utt}+k\Pi_t+ku\Pi_{ut}
       +\Pi R+u\Pi_uR=\Pi\Omega_u L_t.             \tag{RCX.u4}
\]
The coefficient factors and every derivative term follow from
the product rule; $L_t$ and $R$ are independent of $u$.
Composing with the fixed original $j_E$ gives the exact same
identity on its admitted theta-source domain.  Its original
Euler-action connection defect is precisely (DS74), so no
boundary primitive is discarded by this extension.

For the translated phase retain $h_a(t)=-\Phi(-a)-ta$.
The exact identity (RCX38) holds in both parameters:
\[
 \psi_a(u,t)-\psi(u,t)=
             2p\operatorname{Re}(h_a(t)/u).          \tag{RCX.u5}
\]
This is pluriharmonic on $u\ne0$, so all mixed holomorphic--
antiholomorphic derivatives of this difference vanish.  Its
pure $u$ derivatives are explicitly retained:
\[
 \partial_u(\psi_a-\psi)=-p h_a(t)/u^2,\quad
 \partial_u^2(\psi_a-\psi)=2p h_a(t)/u^3,\quad
 \partial_u\partial_t(\psi_a-\psi)=p a/u^2.          \tag{RCX.u6}
\]
They follow by differentiating $p(h_a/u+\overline{h_a/u})$
in Wirtinger coordinates, with $\partial_t h_a=-a$.
Consequently the earlier vanishing of derivatives of order
at least two concerns the fixed-$u$ $t$ derivatives only.
The full translated singular connection is the proved map
(DT.14)--(DT.16), and these additional pure derivatives
are carried into (RCX.u1)--(RCX.u4) through that exact map.
''')
revise('residue_constituent_extension.tex',[
 ('RCX.u1--u6; full u,t recursion and original metric/forced-Laplacian descendants',r'\subsubsection{Source chronology and exact comparison scope}',rcx+'\n'+r'\subsubsection{Source chronology and exact comparison scope}'),
 ('RCX38 derivative scope made explicit','function, so its \\(\\partial_t\\partial_{\\bar t}\\) derivative and\nevery derivative of total order at least two vanish.',
  'function of \\(t\\) at fixed \\(u\\), so its\n\\(\\partial_t\\partial_{\\bar t}\\) derivative and every pure or mixed\n\\(t,\\bar t\\) derivative of total order at least two vanish.')])

# The full authoritative proofs are copied without mutating their originals.
for key,src in [('BC','work/marked_product_boundary_connection_20260913.tex'),('SPC','work/rh_counterfactual_20260913/total_object/single_primary_boundary_control.tex')]:
    p=ROOT/src; b=p.read_bytes(); (OUT/'proofs'/f'{key}_ORIGINAL.tex').write_bytes(b)
    records.append(dict(proof=key,source=str(p),sha256=sha(b),copied=f'proofs/{key}_ORIGINAL.tex'))
(OUT/'PATCH_MANIFEST.json').write_text(json.dumps(dict(schema='boundary-backpropagation-v1',baseline=str(BASE),sealed_sources_modified=False,records=records),indent=2),encoding='utf-8')
print(json.dumps(dict(revised_files=8,proofs=2,manifest=str(OUT/'PATCH_MANIFEST.json')),indent=2))
