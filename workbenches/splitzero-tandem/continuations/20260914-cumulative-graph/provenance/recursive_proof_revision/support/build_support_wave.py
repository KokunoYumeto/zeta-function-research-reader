from pathlib import Path
import hashlib,json,shutil

W=Path(r'workspace:')
S=W/'work/backpropagation_20260913/support'
B=W/'work/cumulative_deligne_build_20260913_v2'
for d in ['provenance/tex','updated/tex','fragments']:
    (S/d).mkdir(parents=True,exist_ok=True)
for f in ['support_diagrams.tex','tau_chain.tex','tau_boundary.tex']:
    shutil.copy2(B/'tex'/f,S/'provenance/tex'/f)
    shutil.copy2(B/'tex'/f,S/'updated/tex'/f)
shutil.copy2(W/'work/tau_mixed_coefficient_face_attachment_20260913.tex',S/'provenance/MCF.tex')

mcf=(S/'provenance/MCF.tex').read_text(encoding='utf-8')
mcf=mcf.replace('empty packet $h=1$, with $E_1=0$, $s_1=\\sigma_1=\\ell_1=0$, and',
'''empty packet $h=1$, with
$F_1=\\Theta\\phi_*$, $E_1=0$, $s_1=\\sigma_1=\\ell_1=0$, and''')
mcf=mcf.replace('at this zero-vector-space stage is used.  Thus the directed systems',
'''at this zero-vector-space stage is used.  The definition of $F_1$ is
forced by $1(D)F_1=\\Theta\\phi_*$ and gives $\\mathcal MF_1=g$.
Thus the directed systems''')
mcf=mcf.replace('The first identity holds in every full local factor and both polynomials',
'''When $h=1$, $b=H$ and the middle identity is exactly
$H(D)F_H=\\Theta\\phi_*=F_1$; the first and third identities have
zero domain and are zero-map identities.  The highest-coefficient,
action, and primitive identities below also have zero domain there.
For a nonempty $h$, the first identity holds in every full local factor and both polynomials''')
mcf=mcf.replace('eigenspace of eigenvalue $\\omega$, the actual full local action is',
'''eigenspace of eigenvalue $\\omega$, define the combined operator
$T_{a,q_0}=A_{a,h}\\Psi_{q_0}=\\Psi_{q_0}A_{a,h}$ on $B_{h,n}$.
Its actual full local action is''')

compat=r'''
\subsection{Literal comparison with the earlier finite source and its cocycle}

The earlier source (TC1) writes the spectral polynomial coordinate as
$t$ and the same residue representative as $R_Z(u)$; the coordinate
isomorphism sends $t$ to $s$, with $h_Z(t)$ sent to $h(s)$, every
power $(t-\rho)^r$ sent to $(s-\rho)^r$, and the full unit unchanged.
Consequently $R_Z(u)$ is $P_h(u)$ under this specified isomorphism.
For the actual source functions, not only their quotient classes,
\[
R_{\mathrm{ref}}=s_h:E_h\longrightarrow\mathscr B_X,
\qquad X=U\text{ or }\Omega\text{ as the packet requires}.
\tag{MCF42}
\]
Indeed applying $h(D)$ to either representative gives
$\Theta(P_h(u)(D)\phi_*)$.  The difference lies in $\mathscr B$
and is killed by the injective $h(D)$, hence vanishes.  This proves
the asserted equality with the original units and domains.

Put $t=\log a$, retaining its orientation when $a<1$, and define
\[
c_{t,h}(u)=\int_0^t\mathcal R_{e^{t-r}}\phi_*\,
                  \ell_h(e^{rA_h}u)\,dr:E_h\longrightarrow V.
\tag{MCF43}
\]
The integral converges in the original Schwartz topology.  In fact
on the compact interval joining $0$ and $t$, every derivative of
$\mathcal R_{e^{t-r}}\phi_*$ is a continuously varying rescaled
derivative of the same Schwartz function, with the scaling parameter
in a compact subset of $(0,\infty)$.  For every pair $N,k$, its
seminorm $\sup_x(1+|x|)^N|\partial_x^k(\cdot)|$ is uniformly
bounded there.  The finite matrix $e^{rA_h}$ is smooth and bounded
there too.  Riemann sums therefore converge in every seminorm in
the complete Schwartz space; parity and the two zero moments pass
to the limit by continuity, so the limit is in $V$.

Differentiate the actual $\mathscr B$-valued function
$\mathcal R_{e^{t-r}}s_he^{rA_h}u$.  Its derivative is
$-\mathcal R_{e^{t-r}}(Ds_h-s_hA_h)e^{rA_h}u$.
The same seminorm argument on $\mathscr B$, followed by (MCF5),
allows the fundamental theorem of calculus.  It gives
\[
\Theta c_{\log a,h}=\mathcal R_as_h-s_hA_{a,h},\qquad
\Psi_{a,h}=c_{\log a,h}.
\tag{MCF44}
\]
The second equality follows by comparing with (MCF24) and canceling
the injective map $\Theta:V\to\mathscr B$.  Thus the previous
oriented integral and the Euler-inverse primitive are the same map.
Their packet and coefficient-face naturality are literal, by
(MCF27) and coordinatewise integration.  The joint primitive is
$(c/2,-\widehat c/2)$; the difference between the two single-leg
primitives $(c,0)$ and $(0,-\widehat c)$ is the full cycle
$(c,\widehat c)$.  No diagonal is discarded by this comparison.

The earlier dual two-leg complex is obtained by applying algebraic
$\operatorname{Hom}_{\mathbb C}(-,\mathbb C)$, so the map induced
by $C_U\to C_+$ is restriction $\mathscr B^\vee\to\mathscr B_U^\vee$
in degree $-1$ and identity on both $V^\vee$ source coordinates in
degree zero.  Its differential, in the same order of legs, is
\[
\ell\longmapsto(\ell\Theta,-\ell\Theta\mathcal F),
\qquad \mathcal F\phi=\widehat\phi.
\tag{MCF45}
\]
Because $\Theta V\subseteq\mathscr B_U$, restriction followed by
this differential equals the differential followed by the identity.
Thus this is an actual cochain map.  It induces restriction
$Q^\vee\to(T_UQ)^\vee$ on degree $-1$ cohomology.  At a joint
source the two diagonal parameters $v\mapsto(v,\mathcal Fv)$ and
$w\mapsto(\mathcal Fw,w)$ agree under $w=\mathcal Fv$. Define
$\mathcal F^\vee:V^\vee\to V^\vee$ by
$\mathcal F^\vee(\ell)=\ell\circ\mathcal F$; the maps
$\pi_v,\pi_w:V^\vee\oplus V^\vee\to V^\vee$ are
\[
\pi_v(\alpha,\beta)=\alpha+\beta\mathcal F,
\quad \pi_w(\alpha,\beta)=\alpha\mathcal F+\beta,
\quad \pi_v=\mathcal F^\vee\circ\pi_w.
\tag{MCF46}
\]
These identities follow by evaluation on the displayed diagonals
and $\mathcal F^2=1$.  The original actions intertwine because
$\mathcal F\mathcal R_a=a\mathcal R_{1/a}\mathcal F$.
For a proper source $W$, dualizing $W\hookrightarrow V$ gives
restriction of diagonal functionals to $W$.  For coefficient faces,
dualizing zero insertion gives coordinate restriction.  These are
algebraic dual statements; no continuous splitting for arbitrary
nonclosed $W$ is asserted.
'''

outer=r'''
\subsection{The earlier reconstruction applied to every original source level}
\label{sec:support-propagated-original-levels}

We now evaluate (D2), (D6), and (D7) on the original theta source,
including the finite polynomial source levels used in (TC2) and
(TB.24)--(TB.26).  Let $\mathcal W$ contain every complex linear
subspace $W$ of the original $V$, ordered by inclusion; no closure
or invariance under $D$ is imposed for this cochain construction.
Fix $n\geq1$ and $I_n=\{0,\ldots,n-1\}$.  Its nonbottom labels are
\[
\lambda=(W,S;A),\qquad W\in\mathcal W,
\quad\varnothing\ne S\subseteq\{+,-\},\quad A\subseteq I_n.
\tag{D9}
\]
Adjoin one distinct bottom $\bot$, with zero fibre.  The join of two
nonbottom labels is $(W+W',S\cup S';A\cup A')$.  The bottom is
strictly below even $(0,S;\varnothing)$.  In degrees zero and one put
\[
\begin{split}
C_{W,S;A}^{X,0}&=
 \left(\bigoplus_{+\in S}W\ \oplus\!
       \bigoplus_{-\in S}\widehat W\right)^A,
\qquad C_{W,S;A}^{X,1}=\mathscr B_X^A,\\
d_{W,S;A}(\phi_i,\psi_i)_i&=(\Theta\phi_i-\Theta\widehat\psi_i)_i.
\end{split}
\tag{D10}
\]
Here $X=U$ or $\Omega$ as in (MCF41); missing legs use typed zeros.
The transition includes old subspaces and coordinates and inserts
typed zeros in newly present legs or coefficients.  Fourier
linearity gives $\widehat W\subseteq\widehat{W+W'}$; hence all
transitions have their stated domains.  Substitution into the
differential proves the cochain identity, and inclusions compose
literally.  Thus (D2) applies in each degree to this actual diagram.
At every nonbottom label with $A=\varnothing$ the amplitude fibre
is zero, but its element is $(W,S;\varnothing,0)$, while the global
zero is $(\bot,0)$.  Applying (D2) proves they remain distinct and
gives their exact joins.  No coefficient-mask colimit is taken.

For each $W$, put $Q_{W,X}=\mathscr B_X/\Theta W$.  The full
cohomology and the comparison to the full source are
\[
\begin{gathered}
H^0(C_{W,S;A}^X)=
 \begin{cases}W^A,&S=\{+,-\},\\0,&|S|=1,\end{cases}
\qquad H^1(C_{W,S;A}^X)=Q_{W,X}^A,\\
0\longrightarrow(V/W)^A\xrightarrow{\eta_W^A}Q_{W,X}^A
 \xrightarrow{\pi_W^A}(T_XQ)^A\longrightarrow0,
\qquad \eta_W[v]=[\Theta v]_W.
\tag{D11}
\end{gathered}
\]
Indeed the source differential has image $(\Theta W)^A$.  A
single-leg differential is injective.  At a joint slot the inverse
coordinates $u=\phi-\widehat\psi$, $v=(\phi+\widehat\psi)/2$,
$\phi=v+u/2$, $\psi=\widehat v-\widehat u/2$ identify its kernel
with $v\in W$.  For the last sequence, injectivity of $\Theta$
makes $\eta_W$ injective; a class killed by $\pi_W$ is represented
by $\Theta v$ for some $v\in V$, and every element of $T_XQ$ has
a representative in $\mathscr B_X$.  This proves exactness,
coordinatewise also for empty $A$.
The coequalizer (D6) uses precisely $(\Theta W)^A$, and (D7)
identifies the kernel of the full-source comparison with $(V/W)^A$
through this same $\eta_W^A$.  This is the all-label fibre kernel
of (D8); with unchanged support label, the global-zero categorical
kernel contains only its bottom fibre.  Both maps are retained.

For $W\subseteq W'$ the source transition therefore induces
\[
0\longrightarrow(W'/W)^A\xrightarrow{[v]\mapsto[\Theta v]_W}
 Q_{W,X}^A\longrightarrow Q_{W',X}^A\longrightarrow0.
\tag{D12}
\]
The proof uses the same kernel computation with $W'$ in place of
$V$.  Thus source refinement has its actual nonzero comparison
kernel before any full-source quotient is applied.

The critical-strip enlargement also has its original typed map:
\[
0\longrightarrow C_{W,S;A}^{U}\longrightarrow C_{W,S;A}^{\Omega}
 \longrightarrow(T_LQ)^A[-1]\longrightarrow0,
\qquad L=\{\Re s=1/2\}.
\tag{D13}
\]
The first map is identity on source legs and inclusion on the
central term.  Its degree-zero quotient is zero.  Its degree-one
quotient is $\mathscr B_\Omega^A/\mathscr B_U^A$, since the same
$\Theta W$ lies in both.  The quotient map $q$ identifies this
space with $(T_\Omega Q/T_UQ)^A$.  For any annihilator
$p=p_Up_L$ with its factors rooted in the disjoint sets $U,L$,
choose $ap_U+bp_L=1$.  The maps $b(D)p_L(D)$ and $a(D)p_U(D)$
split each killed class into its $U$ and $L$ parts.  Their
intersection is zero by the same Bezout identity; uniqueness makes
the splitting independent of the annihilator.  Thus the quotient
is exactly $(T_LQ)^A$, with every multiplicity retained.  All
three complexes keep the same outer and coefficient labels.

The original arithmetic operator has the following additional
type on this larger source diagram.  If $DW\subseteq W'$, then
\[
D_{W,W'}:C_{W,S;A}^X\longrightarrow C_{W',S;A}^X,
\quad(\phi_i,\psi_i)_i\longmapsto(D\phi_i,(1-D)\psi_i)_i,
\quad(F_i)_i\longmapsto(DF_i)_i.
\tag{D14}
\]
Fourier gives $(1-D)\widehat W=\widehat{DW}\subseteq\widehat W'$,
and $\Theta D=D\Theta$ proves the cochain identity.  Moreover
$D\mathscr B_X\subseteq\mathscr B_X$ because $D$ commutes with
each polynomial annihilator of a quotient class.  Thus every
displayed map has its original domain.  For $D$-invariant $W$,
take $W'=W$ to recover precisely (MCF34).  For the actual finite
source levels $W_m=\operatorname{span}\{\phi_*,D\phi_*,\ldots,D^m\phi_*\}$,
one instead has $DW_m\subseteq W_{m+1}$ and must use (D14) with
that codomain.  Linear independence of these vectors follows from
$H_{P(D)\phi_*}=P$, so $\dim(W_{m+1}/W_m)=1$ exactly.
Dilation likewise gives a cochain map from $W$ to $\mathcal R_aW$,
using $\mathcal R_a$ on the plus source and central term and
$a\mathcal R_{1/a}$ on the minus source.  The Fourier identity
proves its stated minus codomain $\widehat{\mathcal R_aW}$.
'''

tc=r'''
\subsection{Original supported maps at every independent source and coefficient face}

The passage from a finite source correction $C$ to its representative,
Gram, and boundary retains the earlier exact full-source formula
\[
C\longmapsto R_{\mathrm{ref}}+\Theta\Phi_LC
\longmapsto(qR,JR,R^*R,K_R)
=(\sigma_Z,1_E,G_R,K_R).
\tag{TC29}
\]
Here is its complete map before the full-source quotient.  Set
$T=\Phi_LC:E\to V$, so $R=s_h+\Theta T$ by (MCF42).  At an
arbitrary original source subspace $W\subseteq V$, define
$\sigma_{R,W}(u)=[Ru]_W\in Q_{W,\Omega}$.  Then
\[
\sigma_{R,W}-\sigma_{h,W}=\eta_W([T(\cdot)]_W),
\qquad \pi_W\sigma_{R,W}=\sigma_Z.
\tag{TC29a}
\]
These follow by subtracting the actual functions and using (D11).
Consequently a permitted full-source correction is invisible in
$Q$ but retains precisely its class in $V/W$ at a smaller source.
The map $\sigma_{R,W}$ is injective, since its composite with
$\pi_W$ is the injective $\sigma_Z$.

If $DW\subseteq W'$, the generator comparison has its exact type
\[
\overline D_{W,W'}\sigma_{R,W}-\sigma_{R,W'}A
      =\eta_{W'}([K_R(\cdot)]_{W'}),
\quad K_R=\phi_*\ell_Z+DT-TA.
\tag{TC29b}
\]
Indeed (TC3) is the source-function equality
$DR-RA=\Theta K_R$; taking its class modulo $\Theta W'$ proves
the formula.  The left action exists by (D14), so no invariant
source subspace is presumed here.  Its kernel class vanishes
exactly when $K_R(u)\in W'$ for the vector in question, by the
injectivity of $\eta_{W'}$.

For every $a>0$ the full corrected dilation primitive is
\[
\begin{split}
c_{R,a}&=\Psi_{a,h}+\mathcal R_aT-TA_{a,h}:E\to V,\\
\mathcal R_aR-RA_{a,h}&=\Theta c_{R,a},\\
\overline{\mathcal R}_a^{W\to\mathcal R_aW}\sigma_{R,W}
 -\sigma_{R,\mathcal R_aW}A_{a,h}
 &=\eta_{\mathcal R_aW}([c_{R,a}]_{\mathcal R_aW}).
\end{split}
\tag{TC29c}
\]
The first two equalities follow by substituting $R=s_h+\Theta T$
into (MCF24) and using $\mathcal R_a\Theta=\Theta\mathcal R_a$.
The last follows by quotienting by $\Theta\mathcal R_aW$.
Expanding the first expression and applying (MCF25) gives
\[
c_{R,ab}=\mathcal R_ac_{R,b}+c_{R,a}A_{b,h}.
\tag{TC29d}
\]
In the expansion, the terms $\mathcal R_aT A_{b,h}$ cancel
with their negative, leaving $\mathcal R_{ab}T-TA_{ab,h}$
and the original primitive $\Psi_{ab,h}$.  This proves the law
with its complete source action and ordered arithmetic product.

At a label $(W,S;A)$, apply all these maps independently to each
coordinate $u_i\in E$ for $i\in A$.  The proper-source residual
is then in $(V/W')^A$ or $(V/\mathcal R_aW)^A$, respectively.
When a primitive belongs to the declared source, its two single-leg
lifts are $(K_Ru,0)$ and $(0,-\widehat{K_Ru})$; their difference
is the entire diagonal $(K_Ru,\widehat{K_Ru})$.  If it does not
belong, its class in (D11) is retained instead.  The labels $W,S,A$
are unchanged by evaluating a zero amplitude, and an empty $A$
retains the outer label; external absence is still $(\bot,0)$.
Zero insertion commutes with the linear formulas, as does the
coefficient Frobenius using the same sign in source and target.
Every corrected metric and boundary formula (TC4)--(TC28) therefore
uses the same original functions as before, while (TC29a)--(TC29d)
record their full mixed-source comparison.
'''

tb=r'''
\subsection{Propagation through the original finite source tower}
\label{sec:tb-propagated-source-tower}

The finite spaces $W_m$ used after (TB.26) have the precise
source-domain maps (D14), because $DW_m\subseteq W_{m+1}$.
Let $T_m=\Phi_mB_m:E\to W_m$, so
$R_m=s_h+\Theta T_m$.  Retain every outer leg label and every
independent coefficient mask $A$.  Then
\[
\begin{gathered}
0\to(W_{m+1}/W_m)^A\to Q_{W_m,\Omega}^A
       \to Q_{W_{m+1},\Omega}^A\to0,\\
\sigma_{m,W_m}^A=\sigma_{h,W_m}^A,
\qquad \sigma_{m+1,W_{m+1}}^A=\sigma_{m,W_{m+1}}^A,
\end{gathered}
\tag{TB.37}
\]
where $\sigma_{m,W}u=[R_mu]_W$.  The exact sequence is (D12);
its kernel map is $[v_i]\mapsto[\Theta v_i]_{W_m}$, not an
erasure of a coefficient face.  The first section equality holds
because $T_m(E)\subseteq W_m$.  The second holds because the
actual difference $R_{m+1}-R_m$ belongs to $\Theta W_{m+1}$,
as proved by the numerator difference following (TB.26).

The entire primitive in (TB.35), with $f_0$ replaced by $\phi_*$,
belongs to $W_{m+1}$.  Hence (TC29b) and (TB.37) give the
adjacent-level arithmetic identity
\[
\overline D_{W_m,W_{m+1}}\sigma_{m,W_m}^A
        =\sigma_{m+1,W_{m+1}}^A A^A.
\tag{TB.38}
\]
This is an equality between the declared quotient spaces, obtained
from the actual nonzero source boundary in (TB.35).  It does not
discard the lower source term or identify $W_m$ with a
$D$-invariant source.  Before passing to $W_{m+1}$, that boundary
retains its class $[K_{R_m}]_{W_m}$ in $(V/W_m)^A$.
In particular, modulo $W_m$ its exact remaining term is
\[
[K_{R_m}u]_{W_m}
       =-[D^{m+1}\phi_*]_{W_m}\,d_mu,
\tag{TB.39}
\]
since $Q_m$ has degree $m$ and $Q_{m+1}$ is monic.  Linear
independence of the source iterates shows that this displayed
generator of $W_{m+1}/W_m$ is nonzero.  Thus the retained source
transition measures exactly the row $d_m$, while the full
primitive in $W_{m+1}$ retains also $d_{m+1}$ as in (TB.35).
The injective two-row observation (TB.36) therefore remains
compatible with, and more informative than, this one transition.

All maps here also commute with the original inclusion from
$\mathscr B_U$ to $\mathscr B_\Omega$ when the packet lies in $U$.
For a packet containing critical-line centres the codomain is
the specified $\mathscr B_\Omega$, whose quotient over
$\mathscr B_U$ is the full $(T_LQ)^A$ in (D13).  The Gram formulas
(TB.7)--(TB.8), rank-one updates (TB.25)--(TB.26), and full
source formula (TB.35) are unchanged actual functions at these
domains.  This propagates the later mixed-face and critical-line
precision through the original arithmetic source tower.
'''

tc=tc.replace('At a label $(W,S;A)$',r'At a label $(W,S;\mathfrak a)$, with $\mathfrak a\subseteq I_n$')
tc=tc.replace('for $i\\in A$',r'for $i\in\mathfrak a$').replace(')^A$',r')^{\mathfrak a}$')
tc=tc.replace('The labels $W,S,A$',r'The labels $W,S,\mathfrak a$').replace('an empty $A$',r'an empty $\mathfrak a$')
tb=tb.replace('coefficient mask $A$',r'coefficient mask $\mathfrak a\subseteq I_n$')
tb=tb.replace('^A',r'^{\mathfrak a}').replace('^\\mathfrak a',r'^{\mathfrak a}')
tb=tb.replace('where $\\sigma_{m,W}u=[R_mu]_W$.',r'where $\sigma_{m,W}u=[R_mu]_W$ and $A^{\mathfrak a}$ denotes the coordinatewise direct sum of the original packet operator $A$.')

for name,body in [('MCF_compatibility.tex',compat),('support_original_levels.tex',outer),('TC29_replacement.tex',tc),('TB_source_tower.tex',tb)]:
    (S/'fragments'/name).write_text(body,encoding='utf-8')
bridge=(S/'fragments/actual_quotient_source_bridge.tex').read_text(encoding='utf-8')
(S/'updated/tex/tau_mixed_coefficient_face_attachment.tex').write_text(mcf+compat+bridge,encoding='utf-8')
p=S/'updated/tex/support_diagrams.tex';p.write_text(p.read_text(encoding='utf-8')+outer,encoding='utf-8')
p=S/'updated/tex/tau_chain.tex';s=p.read_text(encoding='utf-8');start=s.index('\\subsection{Original supported maps and the precise result delivered}');end=s.index('The new conclusions are',start);s=s[:start]+tc+'\n'+s[end:];p.write_text(s,encoding='utf-8')
p=S/'updated/tex/tau_boundary.tex';s=p.read_text(encoding='utf-8')
tb_old=r'''The quotient map
\(\mathscr B/\Theta W_m\to\mathscr B/\Theta W_{m+1}\)
has kernel \(\Theta W_{m+1}/\Theta W_m\);
injectivity of \(\Theta\) identifies this kernel with the original
one-dimensional space \(W_{m+1}/W_m\).
The scalar \(e\) sends a class to the zero in its same support
fibre, while \(\tau\) sends it to external absence.  None of
(TB.24)--(TB.26) changes those maps.'''
tb_new=r'''The same source transition on the precise packet domain is
\(Q_{W_m,\Omega}\to Q_{W_{m+1},\Omega}\), where
\(Q_{W,\Omega}=\mathscr B_\Omega/\Theta W\).
Its kernel is \(\Theta W_{m+1}/\Theta W_m\), identified through
\([v]\mapsto[\Theta v]_{W_m}\) with the original one-dimensional
space \(W_{m+1}/W_m\).  The unchanged target inclusion
\(\mathscr B_\Omega\hookrightarrow\mathscr B\) embeds this
sequence in the original full-target quotient sequence.
At an independent coefficient mask \(\mathfrak a\), the kernel
is exactly \((W_{m+1}/W_m)^{\mathfrak a}\), with its outer source
and leg labels retained by (D12).  The scalar \(e\) gives the
zero at that same label; \(\tau\) gives external absence.
These spaces satisfy \(DW_m\subseteq W_{m+1}\), so their
generator is the actual adjacent-stage map (D14), not an assumed
endomorphism of \(W_m\).  The full surviving primitive and the
resulting arithmetic identity are proved in (TB.37)--(TB.39).
None of these typed source maps changes the Grams in
(TB.24)--(TB.26).'''
assert tb_old in s
s=s.replace(tb_old,tb_new)
p.write_text(s+tb,encoding='utf-8')

def info(p):
    b=p.read_bytes();return {'path':str(p.relative_to(S)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(b.splitlines())}
manifest={'baseline_root':str(B),'scope':'support/source wave; old editions retained; full live source not changed','files':[info(p) for p in sorted(S.rglob('*')) if p.is_file() and p.name!='MANIFEST.json']}
(S/'MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'stage':str(S),'files':len(manifest['files'])},indent=2))
