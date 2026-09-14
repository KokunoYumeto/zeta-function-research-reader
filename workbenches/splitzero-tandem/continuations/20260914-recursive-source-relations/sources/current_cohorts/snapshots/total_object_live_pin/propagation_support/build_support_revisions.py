from pathlib import Path
import hashlib, json

BASE = Path(r'workspace:')
LIVE = BASE / 'output/tau_split_zero_counterfactual_continuation_20260913'
HERE = Path(__file__).parent
OUT = HERE / 'derived'
records = []

def sha(b): return hashlib.sha256(b).hexdigest()

def revise(rel, changes):
    src = LIVE / rel
    original = src.read_bytes()
    txt = original.decode('utf-8-sig')
    entries = []
    for label, old, new, evidence in changes:
        assert txt.count(old) == 1, (rel, label, txt.count(old))
        old_line = original.decode('utf-8-sig').find(old)
        old_line = original.decode('utf-8-sig')[:old_line].count('\n') + 1
        txt = txt.replace(old, new)
        entries.append(dict(locator=label, original_line=old_line,
                            source_proofs=evidence, original_text=old,
                            revised_text=new))
    dst = OUT / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(txt, encoding='utf-8', newline='\n')
    records.append(dict(current_relative_path=rel, current_source=str(src),
                        derived_source=str(dst), old_sha256=sha(original),
                        new_sha256=sha(dst.read_bytes()), transformations=entries))

chain = r'''
The same original source also contains the exact all-strip comparison.
Put $\Omega=\{0<\Re s<1\}$, $L=\{\Re s=1/2\}\cap\Omega$,
and define $T_XQ$ and $\mathscr B_X=q^{-1}(T_XQ)$ by (AG2)'s
annihilator condition with roots in $X$, for $X=L,\Omega$.
With $C_X=[V\xrightarrow{\Theta}\mathscr B_X]$ and
$C_+=[V\xrightarrow{\Theta}\mathscr B]$ the arrows are
\[
 C_U\hookrightarrow C_\Omega\hookrightarrow C_+,
 \qquad T_\Omega Q=T_UQ\oplus T_LQ.                    \tag{AG3a}
\]
Each cochain inclusion is identity on $V$ and the original inclusion
on the degree-one functions. For the asserted direct sum, factor any
annihilator as $p=p_Up_L$, retaining all multiplicities, and choose
$a p_U+b p_L=1$. Its two components are
$u_U=b(D)p_L(D)u$ and $u_L=a(D)p_U(D)u$. Multiplication proves
$p_U(D)u_U=p_L(D)u_L=0$, and their sum is $u$. A vector in both
submodules is zero by the same Bezout identity. This also proves
independence of the annihilator and Bezout choice.
The resulting exact cochain quotients are
\[
\begin{split}
 0&\to C_U\to C_\Omega\to T_LQ[-1]\to0,\\
 0&\to C_\Omega\to C_+\to(Q/T_\Omega Q)[-1]\to0.
\end{split}                                                   \tag{AG3b}
\]
Their degree-zero quotients are zero. In degree one, $q$ identifies
$\mathscr B_\Omega/\mathscr B_U$ with $T_\Omega Q/T_UQ$:
its kernel condition is exactly $qF\in T_UQ$. The identical proof
gives the second quotient. Thus the later tensor and packet diagrams
retain their actual offcritical subobjects and their critical-line
comparison quotient; they do not replace $C_+$ by $C_U$.
The proof of (AG4)--(AG8) uses only the open-strip range identity
(AG1), and therefore also gives the same full-unit packet maps for
packets in $\Omega$, with target $\mathscr B_\Omega$. Restriction
to packets in $U$ is the literal original inclusion in (AG3a).
'''

free = r'''
At this same source vertex the distinction between the section and
its strict polynomial-linear realization has the following exact map.
Write $A_{\rm sp}=\mathbb C[s]$, let $s$ act on the original functions
by $D$, and put $e_h=r_h(\varepsilon_h)$. The section $s_h$ is not
$A_{\rm sp}$-linear for a nonempty packet: on $u=\upsilon_h$,
$s_hu=F_h$ and $h(D)F_h=\Theta\phi_*\ne0$, whereas $hu=0$.
Define instead the actual free complex and its cochain map
\[
\begin{gathered}
 P_h^{\rm free}=[A_{\rm sp}\xrightarrow{h}A_{\rm sp}],\qquad
 \kappa_h:P_h^{\rm free}\longrightarrow C_U,\\
 \kappa_h^0(P)=P(D)e_h(D)\phi_*,\qquad
 \kappa_h^1(P)=P(D)e_h(D)F_h .
\end{gathered}                                                   \tag{AG8a}
\]
The complex has degrees zero and one. Both components commute with
the polynomial action and
$\kappa_h^1(hP)=\Theta\kappa_h^0(P)$ by the defining equation
for $F_h$. For every $P\in A_{\rm sp}$ the exact comparison is
\[
 \kappa_h^1(P)-s_h([P]_h)
   =\Theta\left(
      \left(\frac{P e_h-r_h(\varepsilon_h[P]_h)}{h}\right)(D)
                 \phi_*\right).                              \tag{AG8b}
\]
The quotient is a polynomial because its numerator has zero full
$h$-remainder. Applying that numerator at $D$ to $F_h$ proves the
equation, including its full inverse unit. Hence the map on degree-one
cohomology is exactly $\sigma_h$, while the section itself retains
its nonzero boundary (AG8). At a stalk $O=\mathcal O_{\mathbb C,s_0}$,
the map $O\otimes_{A_{\rm sp}}\kappa_h$ is therefore defined;
$O\otimes_{A_{\rm sp}}s_h$ is not such an arrow. The stalk is
torsion-free over the PID $A_{\rm sp}$ and is flat, being a filtered
union of its finite generated free submodules. Thus balancing retains
this exact cohomology map. The full divisor homotopies and their
composition are (CFA.22a)--(CFA.22d), with the same $e_h$ and $F_h$.
The tensor contractions below remain complex-linear, as (AG8a)--(AG8b)
already require; their cohomology projection is polynomial-equivariant.
'''

independent = r'''
For the independent mixed coefficient observation, (AG38) is applied
coordinatewise before any synchronization. Fix $n\ge1$ and a coefficient
mask $A\subseteq I_n$. The labelled additive face of an amplitude space
$X$ is $\{A\}\times X^A$, with absent entries outside $A$ and supported
zeros at every zero entry inside $A$. For $A\subseteq B$, zero insertion
$z_A^B:X^A\to X^B$ is identity on old coordinates and inserts $0_X$
on new coordinates. It sends $e_A$ to $e_B$. Every linear map commutes
with this arrow because it sends $0_X$ to $0_Y$; it is not a pointed
map preserving the wholly absent coefficient tuple when $A$ is empty
and $B$ is not. The coordinatewise lift $G(L)^n$ instead preserves
the coefficient mask exactly and has supported-zero fibre
$\{A\}\times(\ker L)^A$.

Independently retain $W\subseteq V$, $D W\subseteq W$, and the original
nonempty leg mask $S\subseteq\{+,-\}$. For $X=U,\Omega$ set
\[
\begin{gathered}
 C^X_{W,S;A}=
 \left[\left(\bigoplus_{+\in S}W\oplus
                  \bigoplus_{-\in S}\widehat W\right)^A
          \xrightarrow{(\phi_i,\psi_i)\mapsto
                  (\Theta\phi_i-\Theta\widehat\psi_i)}
                         \mathscr B_X^A\right],\\
 Q_{W,X}=\mathscr B_X/\Theta W,\qquad
 0\to(V/W)^A\xrightarrow{[v_i]\mapsto[\Theta v_i]_W}
 Q_{W,X}^A\to(T_XQ)^A\to0 .
\end{gathered}                                                   \tag{AG38a}
\]
The minus action is $1-D$ on $\widehat W$. Injectivity of $\Theta$
proves injectivity of the displayed first map, its image is the kernel
of the quotient modulo $\Theta V$, and that quotient is onto by
definition of $\mathscr B_X$. The joint-leg change
$u=\phi-\widehat\psi$, $v=(\phi+\widehat\psi)/2$ has inverse
$\phi=v+u/2$, $\psi=\widehat v-\widehat u/2$. Therefore
$H^0=W^A$ for the joint mask and $0$ for a single leg, while
$H^1=Q_{W,X}^A$ in every case. All source, coefficient and leg
inclusions commute with these formulas coordinate by coordinate.
In particular the proper-source kernel and the joint-leg diagonal
are different degrees and neither disappears in the full-source
arithmetic observation. The inclusions in (AG3a) induce these same
cochain inclusions and their first quotient $(T_LQ)^A$ at every
$W,S,A$, since the denominator $\Theta W$ is unchanged.

At $A=\varnothing$ the amplitude complex is zero but the label
$(W,S;\varnothing,0)$ remains; it is distinct from the global external
point $\tau_{\rm out}$. No coefficient-face colimit identifies those
labels. The full-unit section, (AG8)'s source boundary and the strict
map (AG8a) are applied on each active coordinate at their stated types.
For a proper source the residual Euler class is precisely
$([\phi_*\ell_h(u_i)])_i\in(V/W)^A$ under (AG38a). Its vanishing
means these source vectors lie in $W$. Dilation sends the label to
$R_aW$ and the corresponding residual source lies in $(V/R_aW)^A$,
as computed with its full primitive in (CFA.15)--(CFA.25).

The multiplication types at these vertices remain explicit. The
Cartesian semiring $\prod_iG(R_i)$ multiplies masks by intersection;
the original negacyclic convolution on $G(E_h)^n$ multiplies them by
sumset modulo $n$, including supported cancellations. For $n=2$ its
product is $(a,b)\star(c,d)=(ac+(-1)^\bullet bd,ad+bc)$, not the
Cartesian product. Its filling localization has target
$G(E_h[t]/(t^2+1))$ and supported-zero fibre $\{X_0,Y_0,Z_0\}$;
the synchronized section is additive and multiplicative but has unit
image $Z_1$, whereas the unsynchronized unit is $X_1$. These formulas
and their exact ideal branches are proved in (MFC.11)--(MFC.30).
The higher-lattice arrows retain their own threshold/localization
fibres from MFC; neither their join/meet operations nor their separate
ideal product is inserted as a multiplication of the theta source.
At the latter vertex the product is exactly the signed tensor
concatenation (AG14)--(AG15).
'''

revise('tex/continuation/AG.tex', [
 ('AG3 full source inclusions and quotient',
  'is the actual exact sequence, with the original arrows.\n',
  'is the actual exact sequence, with the original arrows.\n'+chain,
  ['MCF41a--MCF41g','CFA.30--CFA.31']),
 ('AG8 section and strict cochain realization',
  'by $h$, has degree at most $d_h$, and has quotient exactly\n$\\ell_h(u)$.  Applying $\\mathcal T_h$ proves it.\n',
  'by $h$, has degree at most $d_h$, and has quotient exactly\n$\\ell_h(u)$.  Applying $\\mathcal T_h$ proves it.\n'+free,
  ['CFA.19--CFA.22d']),
 ('AG9 empty packet source function',
  'mean $E_1=0$, $s_1=0$, and $\\Theta V$; no inverse unit is required\nin the zero space.\n',
  r'''mean $E_1=0$, $s_1=\sigma_1=\ell_1=0$, and $\Theta V$.
The named source function is $F_1=\Theta\phi_*$, since $1(D)$ is
the identity; hence $\mathcal M F_1=g$. This boundary function is not
the zero section on $E_1$. No inverse unit is used in the zero space.
''', ['EPE1--EPE2']),
 ('AG12 empty divisor endpoint proof',
  '$\\mu_{K/H}\\mu_{H/h}=\\mu_{K/h}$.\n',
  r'''$\mu_{K/H}\mu_{H/h}=\mu_{K/h}$.
The unit and remainder calculations above concern nonempty stages.
For $h=1\mid H$, the source identity is still literally
$H(D)F_H=F_1=\Theta\phi_*$, including $H=1$. Every equation with
domain $E_1$ is the equality of zero maps; no old local factor or
unit inverse is invoked. This proves (AG12) at the directed endpoint
as well as at every nonempty divisor transition.
''', ['EPE1--EPE2','MCF26']),
 ('AG19 nonempty jet domain',
  'For $k\\ge1$ and $M\\ge k(d_h-1)$, put\n',
  'For a nonempty full packet $h$, $k\\ge1$ and $M\\ge k(d_h-1)$, put\n',
  ['AG6','EPE1']),
 ('AG38 independent support and downstream products',
  'original split-zero identity, not a replacement of $e$ by $\\tau$.\n',
  'original split-zero identity, not a replacement of $e$ by $\\tau$.\n'+independent,
  ['CFA.3--CFA.7','MCF34--MCF41g','MFC.4--MFC.30','CFA.29'])
])

revise('tex/continuation/MCF.tex', [
 ('MCF4 source endpoint definition',
  'empty packet $h=1$, with $E_1=0$, $s_1=\\sigma_1=\\ell_1=0$, and\n$\\mathscr B_1=\\Theta V$.  Its maps into other packet stages are zero\n',
  r'''empty packet $h=1$, with $E_1=0$, $s_1=\sigma_1=\ell_1=0$,
$\mathscr B_1=\Theta V$, and the named source function
$F_1=\Theta\phi_*$. Since $1(D)$ is the identity, it satisfies
$1(D)F_1=\Theta\phi_*$ and $\mathcal MF_1=g$; it is a theta
boundary and does not define a nonzero class in $E_1$.
Its maps into other packet stages are zero
''', ['EPE1--EPE2']),
 ('MCF26 divisor endpoint proof',
  'Together they prove the third.  Monicity of $b$ preserves the highest\n',
  r'''Together they prove the third. At $h=1\mid H$, the function
identity is $H(D)F_H=F_1=\Theta\phi_*$, including $H=1$.
The identities on the zero domain $E_1$ are the unique zero maps;
the nonempty remainder and inverse-unit argument is not applied to
that domain. Thus (MCF26) retains its source-function equation even
at the empty endpoint. Monicity of $b$ preserves the highest
''', ['EPE1--EPE2'])
])

revise('tex/continuation/CFA.tex', [
 ('CFA2 full source and proper-source domain propagation',
  'This is the original Euler polynomial algebra\n$\\mathbb C[t]$ under its explicit isomorphism $t\\mapsto x$.\n',
  r'''This is the original Euler polynomial algebra
$\mathbb C[t]$ under its explicit isomorphism $t\mapsto x$.
Retain also $\Omega=\{0<\Re s<1\}$ and
$L=\Omega\setminus U$. Define $T_XQ$ by the same annihilator
condition with roots in $X$ and $\mathscr B_X=q^{-1}(T_XQ)$.
The exact inclusions $C_U\hookrightarrow C_\Omega\hookrightarrow
C_+=[V\to\mathscr B]$ have identity degree-zero components.
Their quotients are $T_LQ[-1]$ and $(Q/T_\Omega Q)[-1]$:
factor an annihilator as $p_Up_L$ and apply the Bezout maps
$u\mapsto b(D)p_L(D)u$, $u\mapsto a(D)p_U(D)u$ for
$ap_U+bp_L=1$ to prove $T_\Omega Q=T_UQ\oplus T_LQ$.
The first quotient follows because $qF\in T_UQ$ is exactly
$F\in\mathscr B_U$; the second uses the identical inverse-image
calculation. These are the actual source maps (AG3a)--(AG3b) and
(MCF41a)--(MCF41g), not an identification of their distinct domains.
Every face map below applies coordinatewise to these inclusions;
every full packet in $\Omega$ uses $\mathscr B_\Omega$, while its
offcritical restriction uses $\mathscr B_U$.
''', ['MCF41a--MCF41g','AG3a--AG3b revised']),
 ('CFA8 explicit empty seed with zero amplitude stage',
  'The statements on an empty packet use $E_1=0$ and zero\nmaps, without asking for an inverse unit in a zero vector space.\n',
  r'''The statements on an empty packet use $E_1=0$ and zero maps.
The named source function is $F_1=\Theta\phi_*$, with
$\mathcal MF_1=g$ and $H(D)F_H=F_1$ for $1\mid H$.
These identities follow respectively from $1(D)=1$, the theta
seed equation, and the defining equation for $F_H$. At this stage
$s_1=\sigma_1=\ell_1=0$ on $E_1$; the nonzero boundary $F_1$
is not a nonzero amplitude class. No inverse-unit or nonzero-ring
assertion is used at this zero vector-space stage, whose additive
split carrier still retains every coefficient face of $G(0)^n$.
''', ['EPE1--EPE2','MCF4 revised']),
 ('CFA14 divisor endpoint use',
  'On each coefficient face, (CFA.14) holds in every active coordinate.\n',
  r'''At the empty divisor $1\mid H$, (CFA.14)'s function identity
is $H(D)F_H=F_1$. Its section and arithmetic maps with domain
$E_1$ are the zero maps; the inverse-unit and nonempty remainder
proofs above concern only nonempty stages. This verifies the
endpoint without replacing $F_1$ by zero.
On each coefficient face, (CFA.14) holds in every active coordinate.
''', ['EPE1--EPE2','CFA.14']),
 ('CFA23 proper source and all-strip quotient consequences',
  'The coordinate maps commute with\nall face arrows by their explicit zero-insertion formula.\n',
  r'''The coordinate maps commute with
all face arrows by their explicit zero-insertion formula.
At the original restricted central terms set
$Q_{W,X}=\mathscr B_X/\Theta W$ for $X=U,\Omega$. The same
proof gives $0\to(V/W)[A]\to Q_{W,X}[A]\to(T_XQ)[A]\to0$.
Because both central terms contain $\Theta V$ and the denominator
$\Theta W$ is fixed, the original inclusion gives the exact sequence
\[
 0\to Q_{W,U}[A]\to Q_{W,\Omega}[A]\to(T_LQ)[A]\to0.
                                                               \tag{CFA.23a}
\]
Indeed its quotient is $\mathscr B_\Omega/\mathscr B_U$, which
the inverse-image proof after (CFA.2) identifies with $T_LQ$.
For $A=\varnothing$ all these amplitudes are zero, but the outer
label $(W,S;\varnothing,0)$ remains distinct from every other
outer label and from the global external point $\tau_{\rm out}$.
This follows from the labelled disjoint union, not from a nonzero
vector in the zero amplitude complex. Consequently the proper-source
residuals below remain on both sides of the full source inclusion,
with a separate critical-line quotient and with every label retained.
''', ['MCF35--MCF36','MCF41g'])
])

revise('tex/continuation/OCQ.tex', [
 ('OCQ32 independent coefficient kernels before coherent factorization',
  'flatness of $O$ over $A$ prove\n',
  'flatness of $O$ over $A$ prove\n', ['OCQ.31--OCQ.32']),
 ('OCQ33 facewise derived comparison at use',
  'previous factorization argument proves exactness at the others.\n',
  r'''previous factorization argument proves exactness at the others.
For every independent coefficient mask $B\subseteq I_n$, take
the direct sum of these exact modules in the active coordinates,
retaining the independent outer label $(W,S)$. Thus (OCQ.32) has
kernel $L_W^B$, and the kernel of the balanced Mellin observation
fits into $0\to L_W^B\to\ker b_W^B\to K^B\to0$.
For a fixed finite target $E$, the factorization criterion is exactly
$f|_{L_W^B}=0$ for $f:M_W^B\to E$. To prove the criterion,
quotient by $L_W^B$ to obtain $M^B$ and apply (OCQ.9) to each
coordinate inclusion $M\to M^B$; their finite sum gives the
factorization through $N^B$. The obstruction sequence is (OCQ.33)
with $N,M_W,L_W,M$ replaced by their $B$-indexed direct sums.
Its connecting map is the same explicit pushout and its splitting
proof is unchanged on tuples. No condition that the proper-source
kernel be a field-vector space was used.

These are also the precise kernels attached before and after the
source restriction $C_U\hookrightarrow C_\Omega\hookrightarrow
C_+$. Before balancing, (MCF41g) gives
$0\to Q_{W,U}^B\to Q_{W,\Omega}^B\to(T_LQ)^B\to0$.
Balancing retains it by the same flatness already used in (OCQ.32).
The source change has kernel $(V/W)^B$ on each restricted central
term, by $[v_i]\mapsto[\Theta v_i]_W$, and its balanced kernel
is the stated coordinatewise tensor of that module. Thus the
full-source coherent quotient and the proper-source kernel are
connected by the exact maps at this factorization step, including
the separate critical-line quotient.
''', ['MCF36','MCF41g','CFA.23--CFA.23a','OCQ.9']),
 ('OCQ34 actual independent labelled fibres and empty outer point',
  'kernel fibre is identified with external absence.\n',
  r'''kernel fibre is identified with external absence.
On independent coefficient faces the full notation is
$(W,S;B,(v_i))\mapsto(W',S';B,(f(v_i)))$. Its kernel fibre
at that target face consists exactly of $v_i\in\ker f$ for every
$i\in B$. A coefficient inclusion $B\subseteq B'$ has instead
the explicit zero insertion into new active coordinates, so it sends
$e_B$ to $e_{B'}$ and is an arrow between labelled additive faces.
These statements are proved coordinatewise from (OCQ.34).
The empty face retains $(W,S;\varnothing,0)$ and its outer labels;
it is distinct from global external $\tau_{\rm out}$. Even when all
coefficients of a quotient vanish, its supported-zero fibre and its
label therefore remain among the original observations.
''', ['MCF34--MCF36','CFA.3--CFA.7']),
 ('OCQ35 forward trace use at independent faces',
  'including all multiplicities.\nThe dilation on the full balanced module remains the original\n',
  r'''including all multiplicities.
At coefficient face $B$, if the removed local depth in slot $i$ is
$r_i$ with $0\le r_i\le m$, the removed module is precisely
$\bigoplus_{i\in B}(z^{r_i})/(g)$. Applying the displayed
triangular action in each coordinate gives its dimension
$\sum_{i\in B}(m-r_i)$ and trace
$a^\rho\sum_{i\in B}(m-r_i)$. For empty $B$ both are zero,
while its outer label is retained as above. This is the exact
independent-face propagation of the same arithmetic trace, without
identifying a vanished amplitude observation with an absent label.
The dilation on the full balanced module remains the original
''', ['OCQ.35','MCF35--MCF36'])
])

revise('tex/continuation/EPE.tex', [
 ('EPE current-reading provenance after in-place propagation',
  'The historical MCF bytes are preserved in this reader. Equations\n(EPE1)--(EPE2) supply their explicit endpoint convention, also\naccepted by the author of the coordinating source.\n',
  r'''The historical MCF bytes remain preserved with the sealed edition
and source provenance. In the present edition, (EPE1)--(EPE2) are
also incorporated at the MCF, AG and CFA source definitions and
divisor identities themselves. Their endpoint convention was accepted
by the author of the coordinating source. Thus the current earlier
source diagrams already use the displayed function $F_1$ and the
distinct zero amplitude stage $E_1$.
''', ['EPE1--EPE2','current derived-source manifest'])
])

# Disallow identity transformations: an inspected-but-unchanged site is not a revision.
for rec in records:
    rec['transformations'] = [x for x in rec['transformations']
                             if x['original_text'] != x['revised_text']]

payload = dict(schema_version=1, lane='support', base_edition='341-page sealed',
               files=records, ownership_transfers=[
                   dict(path='tex/continuation/MW.tex', owner='/root/purity_program',
                        content='Independent coefficient and outer labels, empty-packet endpoint'),
                   dict(path='tex/reconstruction.tex', owner='/root/metric_transitive_propagation',
                        content='Support-only reconstruction replacement supplied by earlier-module child'),
                   dict(path='tex/continuation/TO.tex', owner='/root', content='Exact proposal only'),
                   dict(path='tex/continuation/CAU.tex', owner='/root', content='Exact proposal only')])
(HERE / 'SUPPORT_PROPAGATION_MANIFEST.json').write_text(json.dumps(payload, indent=2), encoding='utf-8')
print(json.dumps([dict(path=r['current_relative_path'], old=r['old_sha256'], new=r['new_sha256'],
                       transformations=len(r['transformations'])) for r in records], indent=2))
