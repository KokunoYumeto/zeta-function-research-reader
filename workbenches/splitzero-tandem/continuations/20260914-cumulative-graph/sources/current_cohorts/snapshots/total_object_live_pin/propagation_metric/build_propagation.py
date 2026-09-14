from pathlib import Path
import hashlib, json, re

ROOT = Path(r'workspace:')
BASE = ROOT / 'output/tau_split_zero_counterfactual_continuation_20260913'
HERE = Path(__file__).resolve().parent
ENTRIES = []

def sha(b): return hashlib.sha256(b).hexdigest()
def load(rel):
    p=BASE/rel
    data=p.read_bytes()
    original=HERE/'originals'/rel
    original.parent.mkdir(parents=True,exist_ok=True)
    if original.exists():
        assert original.read_bytes()==data, f'Frozen input changed: {rel}'
    else: original.write_bytes(data)
    return data.decode('utf-8-sig').replace('\r\n','\n')
def replace(s,a,b):
    assert s.count(a)==1,(a[:100],s.count(a))
    return s.replace(a,b)
def segment(s,a,b,new):
    assert s.count(a)==1 and s.count(b)==1,(a,b)
    i=s.index(a);j=s.index(b,i)
    return s[:i]+new+s[j:]
def save(rel,s,changes):
    old=(HERE/'originals'/rel).read_bytes()
    bom=b'\xef\xbb\xbf' if old.startswith(b'\xef\xbb\xbf') else b''
    if b'\r\n' in old:s=s.replace('\n','\r\n')
    data=bom+s.encode('utf-8')
    assert data!=old,rel
    dest=HERE/'derived'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    ENTRIES.append(dict(current_file=str(BASE/rel),current_relative=rel,
        old_sha256=sha(old),derived_source=str(dest),new_sha256=sha(data),
        historical_copy=str(HERE/'originals'/rel),changes=changes))

# AT contains the complete strengthened proof at the earlier finite-source site.
rel='tex/modules/AT.tex';s=load(rel)
new=r'''\section{An exact finite-source bound for the correction}

Let $b_1\le\cdots\le b_{2q+1}$ be every positive eigenvalue of
$D_*=M_*(0)^{-1}M_*(1)$ in the original $M_*(0)$ metric, and put
$\kappa_*=b_{2q+1}/b_1$. These data are on the unchanged common
source $H=\cP_{2q}$; neither packet nor tensor order is suppressed.
For the exact $U,W,C$ in (AT11)--(AT15), let $c_j(t)$ be the
ordered eigenvalues of $C(t)$, $d(t)=c_{2q+1}(t)-c_1(t)$, and
$s(t)=\dim(\operatorname{ran}U\cap\operatorname{ran}W)$. All norms
and projections in the following formulas use $M_*(t)$:
\[
\begin{aligned}
S_{\rm spec}(t)&=c_{q+2}(t)-c_q(t)
 +2\sum_{j=1}^{q-1}(c_{2q+2-j}(t)-c_j(t)),\\
S_{\rm tr}(t)&=\tfrac12d(t)\|U(t)-W(t)\|_{1,t},\\
S_{\rm ov}(t)&=\tfrac12d(t)\min\{4q-2s(t),
 \sqrt{(2q+1)(8q-4-2\Tr(U(t)W(t)))}\},\\
\mathfrak C_*&=\int_0^1\min\{S_{\rm spec}(t),S_{\rm tr}(t)\}\,dt,\\
\mathfrak C_*^{\rm ov}&=\int_0^1\min\{S_{\rm spec}(t),S_{\rm ov}(t)\}\,dt,\\
L_q(D_*)&=\log\frac{b_{q+2}}{b_q}
 +2\sum_{j=1}^{q-1}\log\frac{b_{2q+2-j}}{b_j}.
\end{aligned}\tag{AT18a}
\]
The trace norm is the sum of absolute eigenvalues of the displayed
self-adjoint endomorphism. For $q=1$ the sums are empty. Under
$x=t$, these are literally the ACM/SP operators: their relation
matrix is $I_NB_N$, hence their projector is exactly (AT11);
their density $r_{1/4}^{*k}$ equals (AT4), with
$c_{1/4}=\sqrt{2\pi}$ and its full mass. Thus
$\mathfrak C_*^{\rm ov}$ is the original ACM pointwise minimum.
The sharper $\mathfrak C_*$ also retains SP's already proved exact
trace norm; no new source form is chosen.

\begin{theorem}
The actual signed correction satisfies
\[
\boxed{|\Delta\mathcal B|\le\mathfrak C_*
 \le\mathfrak C_*^{\rm ov}\le L_q(D_*)
 \le(2q-1)\log\kappa_* .}\tag{AT18}
\]
Consequently its original endpoint quantities obey
\[
\mathcal B^\Ga_{h,k}-\mathfrak C_*
 \le\mathcal B^\ar_{h,k}
 \le\mathcal B^\Ga_{h,k}+\mathfrak C_* .\tag{AT19}
\]
\end{theorem}
\begin{proof}
Multiplication by the same monic $\chi$ gives the nested relation
flag $\chi\cP_0\subset\chi\cP_{q-1}\subset\chi\cP_q$ of
dimensions $1,q,q+1$. On its orthogonal increments $U$ acts by
$1,2,1$, and acts by zero on the $q$-dimensional complement.
The polynomial flag $\cP_{q-1}\subset\cP_q\subset\cP_{2q-1}
\subset\cP_{2q}$ gives the same full spectrum for $W$:
$0^q,1^2,2^{q-1}$. Repeated spaces when $q=1$ give zero-dimensional
increments, not omitted endpoint maps. In particular
\[
\Tr U=\Tr W=2q,\quad \Tr U^2=\Tr W^2=4q-2,
\quad\Tr((U-W)^2)=8q-4-2\Tr(UW).
\]
For a rank-$r$ orthogonal projection $P$, its diagonal entries in
an orthonormal eigenbasis of $C$ lie in $[0,1]$ and sum to $r$.
Moving this fixed nonnegative mass to the $r$ smallest or largest
eigenvalues proves
$\sum_{j=1}^r c_j\le\Tr(PC)\le\sum_{j=2q+2-r}^{2q+1}c_j$.
Each of $U,W$ is its range projection of rank $q+1$ plus its
eigenvalue-two projection of rank $q-1$. Applying these two bounds
and subtracting the complete sums gives $|\Tr((U-W)C)|\le S_{\rm spec}$.

Since $\Tr(U-W)=0$, subtracting the midpoint of the extremes of
$C$ leaves the trace pairing unchanged. In an orthonormal eigenbasis
of $U-W$ every resulting diagonal entry of $C$ has absolute value
at most $d/2$. Therefore $|\Tr((U-W)C)|\le S_{\rm tr}$.
The two ranges have dimension $q+1$ in dimension $2q+1$, so $s\ge1$.
Let $E$ be their intersection projection. The inequalities
$U\succeq E$, $W\succeq E$ follow from their nonzero eigenvalues
being at least one. The two positive differences have trace $2q-s$;
their difference is $U-W$. Thus $\|U-W\|_1\le4q-2s$.
Cauchy--Schwarz on its $2q+1$ real eigenvalues proves the second
trace-norm upper bound in $S_{\rm ov}$. We have proved pointwise
\[
|\Tr((U-W)C)|\le\min\{S_{\rm spec},S_{\rm tr}\}
 \le\min\{S_{\rm spec},S_{\rm ov}\}.\tag{AT20}
\]
All the matrix entries are smooth on the compact interval. Eigenvalues
and trace norms are continuous. The intersection dimension is Borel,
since rank strata are specified by vanishing and nonvanishing minors.
The bounded nonnegative functions above are consequently integrable.

In the fixed coefficient space,
$C(t)=((1-t)I+tD_*)^{-1}(D_*-I)$, so
\[
c_j(t)=\frac{b_j-1}{1-t+tb_j},\qquad
\int_0^1c_j(t)\,dt=\log b_j,\qquad
\int_0^1d(t)\,dt=\log\kappa_* .\tag{AT21}
\]
The derivative of the fraction with respect to $b_j$ is
$(1-t+tb_j)^{-2}>0$, proving its order through both endpoints.
Integrating (AT20) in (AT15) proves the first inequalities of
(AT18). Integrating $S_{\rm spec}$ gives $L_q(D_*)$ exactly.
Its logarithmic ratios are each between zero and $\log\kappa_*$;
their total multiplicity is $1+2(q-1)=2q-1$. This proves the last
inequality. Substitution of (AT14) proves (AT19).
The preceding coarser $2q\log\kappa_*$ estimate is a corollary
because $\log\kappa_*\ge0$; its weaker coefficient is not used
in the current endpoint consequences.
\end{proof}

'''
s=segment(s,r'\section{An exact finite-source bound for the correction}', 'When $M_*(1)=cM_*(0)$',new)
s=replace(s,r''' \mathcal B^\ar_{h,k}\ge
 4q\log\!\left(\frac{\delta k}{2\sqrt5}\right)-2q\log\kappa_*,
 \quad
 \log\kappa_*\ge
 2\log\!\left(\frac{\delta k}{2\sqrt5}\right)
       -\frac{\mathcal B^\ar_{h,k}}{2q}.                   \tag{AT22}''',r'''\begin{aligned}
 \mathcal B^\ar_{h,k}&\ge
 4q\log\!\left(\frac{\delta k}{2\sqrt5}\right)-\mathfrak C_*,\\
 \mathfrak C_*&\ge\max\left\{0,
 4q\log\!\left(\frac{\delta k}{2\sqrt5}\right)-\mathcal B^\ar_{h,k}\right\},\\
 \log\kappa_*&\ge\frac{1}{2q-1}\max\left\{0,
 4q\log\!\left(\frac{\delta k}{2\sqrt5}\right)-\mathcal B^\ar_{h,k}\right\}.
\end{aligned}\tag{AT22}''')
save(rel,s,['AT18a explicitly identifies original AW/SP source and both pointwise controls.','AT18–21 complete independent proof with full spectra, exact trace norm and overlap; former coarse bound is a proved corollary.','AT19 and AT22 propagate sharper control into both endpoint bounds, necessary correction and condition-number thresholds.'])

# AW retains its complete spectral proof and uses the strengthened control in its theorem/application.
rel='tex/modules/AW.tex';s=load(rel)
s=replace(s,r''' |\Delta\mathcal B|\le\mathcal L_q(D)
                  \le(2q-1)\log\kappa(D).''',r''' |\Delta\mathcal B|\le\mathfrak C_*
 \le\mathfrak C_*^{\rm ov}\le\mathcal L_q(D)
 \le(2q-1)\log\kappa(D).''')
s=replace(s,'In particular the coefficient $2q$ in AT18 can be improved to\n$2q-1$, while the first bound retains the full relative spectrum.',
r'''Here $\mathfrak C_*,\mathfrak C_*^{\rm ov}$ are the original-source
pointwise minima defined in the revised (AT18a). The proof below
retains the full spectral calculation; the complete AT proof also
retains the exact trace norm and the overlap before integration.''')
s=replace(s,'the first inequality of (AW14). Every ratio in (AW13) lies','the spectral inequality in (AW14). For the preceding inequalities,\napply the independently proved (AT20) on the identical operators\n(AW4)--(AW5), then integrate in (AW6). Every ratio in (AW13) lies')
s=replace(s,r'''             -\mathcal L_q(D).''',r'''             -\mathfrak C_* .''')
s=replace(s,'into the proved first inequality of (AW14). It proves no','into the proved first inequality of (AW14), retaining the pointwise\nminimum before integration. Since $\mathfrak C_*\le\mathcal L_q(D)$,\nthe preceding spectral-only lower bound remains a corollary. It proves no')
save(rel,s,['AW14 strengthened on the identical typed source; complete AW15–17 spectral proof retained.','AW18 now subtracts exact joint control instead of the larger full-spectrum envelope.','AW19–23 q=1 angle theorem retained with original dimension and masses.'])

# ACM maintains the requested overlap minimum and retains the exact trace-norm predecessor.
rel='tex/continuation/ACM.tex';s=load(rel)
s=replace(s,r''' |\Delta_{h,k}|
 \le\int_0^1\min\{S_{\rm AW}(x),S_{\rm SP}(x)\}\,dx.}''',r''' |\Delta_{h,k}|
 \le\underbrace{\int_0^1\min\{S_{\rm AW}(x),
       \tfrac12d_x\|U_x-W_x\|_{1,M_x}\}\,dx}_{\mathfrak C_*}
 \le\underbrace{\int_0^1\min\{S_{\rm AW}(x),S_{\rm SP}(x)\}\,dx}
                _{\mathfrak C_*^{\rm ov}}.}''')
s=replace(s,'If $b_1\le\cdots\le b_{2q+1}$',
r'''The first bound preserves the exact trace norm already present in
(SP13); its proof above gives $d_x\|U_x-W_x\|_1/2\le S_{\rm SP}(x)$.
The identity maps (ACM1)--(ACM5) identify these quantities with
(AT18a), including the source density and its mass. If $b_1\le\cdots\le b_{2q+1}$''')
s=replace(s,r''' |\Delta_{h,k}|&\le
  \min\left\{\mathcal L_q(D),\int_0^1S_{\rm SP}(x)\,dx\right\},''',r''' |\Delta_{h,k}|&\le\mathfrak C_*
 \le\mathfrak C_*^{\rm ov}
 \le\min\left\{\mathcal L_q(D),\int_0^1S_{\rm SP}(x)\,dx\right\},''')
save(rel,s,['ACM11 and ACM13 include exact trace-norm minimum before requested AW/SP overlap minimum.','ACM1–10 prove literal source/operator identity; no Gamma mass or coordinate discarded.'])

# SP: combine its exact trace norm with the full spectrum at its actual terminal inequality.
rel='tex/continuation/SP.tex';s=load(rel)
s=replace(s,'Combining SP7--SP12 proves',r'''Let $c_1(x)\le\cdots\le c_{2q+1}(x)$ be all eigenvalues of
$T_x$ and put
$S_{\rm spec}(x)=c_{q+2}(x)-c_q(x)
+2\sum_{j=1}^{q-1}(c_{2q+2-j}(x)-c_j(x))$.
The source inclusions (SP2) give exactly (AT11), with relation
matrix $B_N^{\rm SP}=I_NB_N^{\rm AT}$; the Gamma convolution
has $c_{1/4}=\sqrt{2\pi}$, so its original mass agrees as well.
The projection trace proof (AT20) consequently applies to these
same operators. Combining it with SP7--SP12 proves''')
s=replace(s,r''' \leq\frac12\int_0^1d_x
          \|\mathcal R_x-\mathcal P_x\|_1\,dx
 \leq(2q-1)\log\frac{r_{\max}}{r_{\min}} .}''',r''' \leq\mathfrak C_*:=\int_0^1\min\{S_{\rm spec}(x),
       \tfrac12d_x\|\mathcal R_x-\mathcal P_x\|_1\}\,dx
 \leq\min\left\{L_q(R),
       \tfrac12\int_0^1d_x\|\mathcal R_x-\mathcal P_x\|_1\,dx\right\}
 \leq(2q-1)\log\frac{r_{\max}}{r_{\min}} .}''')
s=replace(s,'The first bound and its overlap refinement SP10 retain more\ninformation than the last bound.',
r'''Here $L_q(R)$ is the full-spectrum expression (AT18a) for the
actual $R$. Replacing its exact trace-norm term by the right side
of (SP10) yields $\mathfrak C_*^{\rm ov}$, the ACM pointwise
spectral/overlap minimum. Both refinements retain more information
than the final condition-number corollary.''')
save(rel,s,['SP13 now intersects full-spectrum and exact trace norm pointwise; SP10 overlap retained as explicit surrogate.','Typed relation inclusion and original Gamma mass verify AT transfer.'])

# Fixed sigma comparison: re-run all coefficient maps on the correct second reference.
rel='tex/continuation/CA.tex';s=load(rel)
a='The unchanged source flags and their minimum relation maps have the\nAW.7 spectrum'
b='The stronger nonlinear angle estimate is already proved'
new=r'''On this particular interpolation put $H(t)=(1-t)H_{2q}^\sigma
+tH_{2q}^{\rm ar}$ and $C^\sigma(t)=H(t)^{-1}(H_{2q}^{\rm ar}-H_{2q}^\sigma)$.
The identity coefficient maps (CA2) give
\[
\begin{aligned}
P_N^\sigma(t)&=I_N(I_N^*H(t)I_N)^{-1}I_N^*H(t),\\
Q_N^\sigma(t)&=I_NB_N(B_N^*I_N^*H(t)I_NB_N)^{-1}B_N^*I_N^*H(t),\\
U^\sigma&=Q_{2q-1}^\sigma+Q_{2q}^\sigma-Q_q^\sigma,\qquad
W^\sigma=P_{2q-1}^\sigma-P_{q-1}^\sigma+P_{2q}^\sigma-P_q^\sigma.
\end{aligned}\tag{CA14a}
\]
Here $Q_{q-1}^\sigma=0$. Each inverse is on the original nonzero
source or relation domain. Direct multiplication proves the same
orthogonal projector identities as (AT11); the nested spaces give
the full spectrum $0^q,1^2,2^{q-1}$ for both window operators.
Block determinants for (CA2), followed by differentiation, give
$\Delta_\sigma=\int_0^1\Tr((U^\sigma-W^\sigma)C^\sigma)\,dt$.
Thus the exact proof (AT18a)--(AT21) applies to these displayed
matrices, with no identification of $H^\sigma$ with the tensor
Gamma Gram. Define $S_{\rm spec}^\sigma,S_{\rm tr}^\sigma,
S_{\rm ov}^\sigma$ by (AT18a) using precisely
$(U^\sigma,W^\sigma,C^\sigma,H(t))$, and set
\[
\begin{aligned}
\mathfrak C_\sigma&=\int_0^1\min\{S_{\rm spec}^\sigma,S_{\rm tr}^\sigma\}\,dt,
&\mathfrak C_\sigma^{\rm ov}&=\int_0^1\min\{S_{\rm spec}^\sigma,S_{\rm ov}^\sigma\}\,dt,\\
L_q(D_*)&=\log\frac{b_{q+2}}{b_q}
 +2\sum_{j=1}^{q-1}\log\frac{b_{2q+2-j}}{b_j}.
\end{aligned}
\]
The resulting full comparison at this earlier theorem site is
\[
\boxed{|\Delta_\sigma|\le\mathfrak C_\sigma
 \le\mathfrak C_\sigma^{\rm ov}\le L_q(D_*)
 \le(2q-1)\Lambda_k.}\tag{CA14}
\]
Every step of the transferred proof holds: positivity follows from
(CA3)--(CA6), the source dimension is $2q+1$, and the same nested
flags give all trace and overlap bounds. Eigenvalues of $C^\sigma$
are $(b_j-1)/(1-t+tb_j)$ in the actual interpolated metric, so
integration gives the displayed logarithms. Both original masses
and the coefficient map commuting with $\mathcal O_N$ remain fixed.

'''
s=segment(s,a,b,new)
s=replace(s,r'B_\sigma-L_q(D_*)',r'B_\sigma-\mathfrak C_\sigma')
s=replace(s,r'B_\sigma+L_q(D_*)',r'B_\sigma+\mathfrak C_\sigma')
s=replace(s,'Each entry bounds the same original scalar (CA11); taking the indicated',
r'''The two spectral entries of the preceding edition are now obtained
as corollaries from $\mathfrak C_\sigma\le L_q(D_*)$; the current
interval retains the pointwise minimum before integration. Each
entry bounds the same original scalar (CA11); taking the indicated''')
save(rel,s,['CA14a supplies exact sigma source/relation maps; AT trace proof rerun on actual sigma interpolation.','CA14 and CA21 use joint control; full-spectrum and scalar estimates remain corollaries.','CA22 asymptotic rate remains valid by C_sigma≤L; CA26–29 compulsory old-Gamma spread unchanged.'])

# AAM propagates the sigma joint control into the actual error/control upper function.
rel='tex/continuation/AAM.tex';s=load(rel)
s=replace(s,r''' U_k^{\rm spec}=\mathcal B_k^\sigma+L_q(D_*),\qquad
 U_k^{\rm ang}''',r''' U_k^{\rm spec}=\mathcal B_k^\sigma+L_q(D_*),\qquad
 U_k^{\rm joint}=\mathcal B_k^\sigma+\mathfrak C_\sigma,\\
 U_k^{\rm ang}''')
s=replace(s,r'''These are the actual full-spectrum and angle bounds proved in
(CA14), (CA17b). They give
$\mathcal B_k\leq\min(U_k^{\rm spec},U_k^{\rm ang})$ and
$L_q(D_*)\leq(2q-1)\Lambda_k$. The full spectrum in
$L_q(D_*)$ is retained; its value has not been replaced by the
scalar envelope when taking the first minimum.''',r'''Here $\mathfrak C_\sigma$ is the integral in (CA14) on the
explicit coefficient interpolation (CA14a), whose initial density
is the original fixed $\sigma$, of mass $\sqrt{2\pi}$.
The full-spectrum, exact trace-norm, overlap and angle proofs give
$\mathcal B_k\le\min(U_k^{\rm joint},U_k^{\rm ang})$ with
$U_k^{\rm joint}\le U_k^{\rm spec}$ and
$\mathfrak C_\sigma\le\mathfrak C_\sigma^{\rm ov}
\le L_q(D_*)\le(2q-1)\Lambda_k$.
The tensor Gamma source is a separate comparison; no equality of
its Gram with $H^\sigma$ is used. The current minimum keeps the
actual interpolation and all its overlaps before integration.''')
s=replace(s,r'''                                  U_k^{\rm spec},U_k^{\rm ang}\}''',r'''                                  U_k^{\rm joint},U_k^{\rm ang}\}''')
s=replace(s,r'''The following are exact finite comparisons, obtained by substituting
$\mathcal B_k\leq U_k^{\rm all}$ into (AAM.12)--(AAM.14):''',
r'''This definition propagates the sharper common-source estimate
through the control calculation: because $U_k^{\rm joint}\le
U_k^{\rm spec}$, its value is no larger than the preceding
three-term upper function. The following finite comparisons use
this revised $U_k^{\rm all}$ in (AAM.12)--(AAM.14):''')
s=replace(s,r'''$U_k^{\rm spec}$ remains the explicitly defined original finite
matrix calculation in (AAM.24); none of (CA)--(TW) evaluates its
moving-$k$ spectrum by a smaller scalar error.''',
r'''$U_k^{\rm spec}$ and the sharper $U_k^{\rm joint}$ remain the
explicitly defined original finite matrix calculations in (AAM.24)
and (CA14a). No shrinking moving-$k$ bound for the joint spectral,
trace-norm and overlap integrand is inferred from its finite value.''')
save(rel,s,['AAM24 defines exact joint sigma upper function using CA14a.','AAM28 replaces spectral-only entry; AAM29 uses revised U_all in every average and individual control exponent.','AAM25 angle-overhead rate and AAM30 coarse rate remain exact statements about their named functions.'])

# QT uses the same joint control within its existing centered interval.
rel='tex/continuation/QT.tex';s=load(rel)
s=replace(s,'The original proof (AW14) and (QT.25) give simultaneously',
r'''The common-source proof (AT18a)--(AT21), with $\mathcal C=C$,
gives $|\Delta\mathcal B|\le\mathfrak C_*\le
\mathfrak C_*^{\rm ov}\le\mathfrak L_q$ on these exact matrices.
Combining this stronger value with (QT.25) gives simultaneously''')
s=replace(s,r'\max\{-\mathfrak L_q,\mathfrak E-\mathfrak F\}',r'\max\{-\mathfrak C_*,\mathfrak E-\mathfrak F\}')
s=replace(s,r'\min\{\mathfrak L_q,\mathfrak E+\mathfrak F\}',r'\min\{\mathfrak C_*,\mathfrak E+\mathfrak F\}')
save(rel,s,['QT26 now intersects centered relation-speed interval with joint pointwise control; original exact QT21 and QT24–25 energies unchanged.'])

# HC: current restrictions sharpen, while its coarse-width theorem retains its exact scope.
rel='tex/modules/HC.tex';s=load(rel)
s=replace(s,r'''must belong to the following explicit intervals:''',r'''must belong to the following explicit intervals. Let $\mathfrak C_*$
be (AT18a) on the same arithmetic and tensor Gamma moment matrices.
Its proof uses the original full packet and applies to exactly these
four determinants, so $|\Delta_k^\Gamma|\le\mathfrak C_*$.
Write $T_k=4q\log(D_hk)$ for this displayed scalar only:''')
s=replace(s,r''' \max\{0,-4q\log(D_hk)\}\leq\mathcal R_k
 \leq\widehat{\mathcal U}_k-4q\log(D_hk),''',r''' \max\{0,-T_k,\mathcal B_k^\Gamma-\mathfrak C_*-T_k\}
 \leq\mathcal R_k
 \leq\min\{\widehat{\mathcal U}_k,\mathcal B_k^\Gamma+\mathfrak C_*\}-T_k,''')
s=replace(s,r''' \max\{0,4q\log(D_hk)\}-\mathcal B_k^\Gamma
 \leq\Delta_k^\Gamma
 \leq\widehat{\mathcal U}_k-\mathcal B_k^\Gamma.''',r''' \max\{-\mathfrak C_*,\max\{0,4q\log(D_hk)\}-\mathcal B_k^\Gamma\}
 \leq\Delta_k^\Gamma
 \leq\min\{\mathfrak C_*,\widehat{\mathcal U}_k-\mathcal B_k^\Gamma\}.''')
s=replace(s,'These intervals have strictly positive width for every $k\geq3$.',
r'''The new entries follow by substituting
$\mathcal B_k=\mathcal B_k^\Gamma+\Delta_k^\Gamma$ and
$\mathcal R_k=\mathcal B_k-T_k$ into (AT18)--(AT19).
Their intersection width has not been evaluated for an actual
offcritical packet. Removing just the $\mathfrak C_*$ entries gives
the preceding coarse intervals, whose width is strictly positive
for every $k\geq3$.''')
s=replace(s,'This proves numerical compatibility of the stated actual bound\nfunctions.',
r'''This proves numerical compatibility of those coarse bound functions.
It does not prove compatibility of the refined (HC9)--(HC10), whose
source-dependent $\mathfrak C_*$ remains present.''')
s=replace(s,r'''Consequently (HC13)'s right side is at most
$\widehat{\mathcal U}_k+2q\log((1+\eta)/(1-\eta))$.''',
r'''Consequently (HC13)'s right side is at most
$\min\{\widehat{\mathcal U}_k,\mathcal B_k^\Gamma+\mathfrak C_*\}
+2q\log((1+\eta)/(1-\eta))$.
This substitution uses (AT19) on the original arithmetic form
before the explicitly proved phase allowance; it does not identify
the sampled phase metric with the original one.''')
save(rel,s,['HC9–10 refine residual and signed intervals by actual joint control.','HC11 coarse-positive-width proof retained with corrected scope, no compatibility claim for refined intersection.','HC14 consequence transports sharper original-source upper value through unchanged phase allowance.'])

# Actual lower-window and phase-generator consequences retain all their costs.
rel='tex/continuation/TW.tex';s=load(rel)
anchor=r'Since $E_k/q\to0$, the quantified refinement includes'
insert=r'''Let $\mathcal R_k^{\rm TW}$ denote exactly the right side of
(TW20), with every displayed contraction, phase, control and trace term.
The original Gamma four-volume $\mathcal B_k^\Gamma$ uses the
same $\chi$ and the original tensor Gamma density. Substituting
(AT19), whose $\mathfrak C_*$ is computed on that precise pair of
source Grams, gives the additional current consequence
\[
\mathcal R_k^{\rm TW}\le\mathcal B_k
 \le\mathcal B_k^\Gamma+\mathfrak C_*,\qquad
\mathfrak C_*\ge\max\{0,\mathcal R_k^{\rm TW}-\mathcal B_k^\Gamma\}.
\tag{TW20a}
\]
Both inequalities follow by substitution of the same scalar;
none of the nonnegative terms of (TW20) is discarded or assigned
an asymptotic cancellation. Since $E_k/q\to0$, the quantified refinement includes'''
s=replace(s,anchor,insert)
save(rel,s,['TW20a carries every original TW20 nonnegative residual into the joint Gamma upper comparison; TW21 lower asymptotic unchanged.'])

rel='tex/continuation/PAM.tex';s=load(rel)
anchor='Thus the strengthened energy enters exactly the same windows.'
insert=r'''Thus the strengthened energy enters exactly the same windows.
For the period selected by the original (HC14) source comparison,
write $\mathcal H_k(\eta)=2q\log((1+\eta)/(1-\eta))$ with
the same $0<\eta<1$. Let $\mathcal B_k^\Gamma$ be the original
tensor Gamma four-volume, and let $\mathfrak C_*$ be (AT18a)
on its original degree-$2q$ interpolation to the arithmetic source.
The literal metric comparison (HC14), then (AT19), gives
\[
\begin{aligned}
2\sum_{N=q-1}^{2q-1}w_N
 \log\max\left\{1,
       \frac{\mathcal L_{h,k}}{\sqrt{2J_N^\partial}}-1\right\}
&\le\mathcal B_{k,\theta}\\
&\le\min\{\widehat{\mathcal U}_k,
            \mathcal B_k^\Gamma+\mathfrak C_*\}+\mathcal H_k(\eta).
\end{aligned}\tag{PSC.6a}
\]
The first inequality is (PSC.6), and the second uses
$\mathcal B_{k,\theta}\le\mathcal B_k+\mathcal H_k(\eta)$
followed by the two proved original-source upper estimates.
This retains the sampling norm, period and phase; the subtraction
of $c^2q$ in (PSC.5) has not been replaced by an unphased energy.'''
s=replace(s,anchor,insert)
save(rel,s,['PSC6a propagates strengthened original-source upper bound to exact phase-generator residual via unchanged HC14 period/phase allowance.'])

# Combined restriction revises the actual earlier interval and its necessary compatibility condition.
rel='tex/combined_restriction.tex';s=load(rel)
anchor='Every eigenvalue here is computed from the two actual moment matrices'
s=replace(s,anchor,r'''Define $\mathfrak C_*$ and $\mathfrak C_*^{\rm ov}$ by
(AT18a) on this exact $D_*$ and its original interpolated Gram.
Their typed construction gives
$|\Delta|\le\mathfrak C_*\le\mathfrak C_*^{\rm ov}\le L_q$.
Thus the full spectrum is retained together with the actual
projection overlap before integration. Every eigenvalue here is computed from the two actual moment matrices''')
# Replace only uses, not the original definition of L_q.
s=s.replace(r'B_\Gamma-L_q',r'B_\Gamma-\mathfrak C_*').replace(r'B_\Gamma+L_q',r'B_\Gamma+\mathfrak C_*')
s=s.replace(r'-L_q\}',r'-\mathfrak C_*\}').replace(r'B_\Gamma,L_q\}',r'B_\Gamma,\mathfrak C_*\}')
s=replace(s,'eigenvalues give $|\Delta|\le L_q$ in (AW14).',
r'''eigenvalues and retained trace/overlap give
$|\Delta|\le\mathfrak C_*\le L_q$ in (AT18)--(AT20),
equivalently the revised (AW14) and (ACM11).''')
s=replace(s,r''' L_q\ge
 \max''',r''' L_q\ge\mathfrak C_*^{\rm ov}\ge\mathfrak C_*\ge
 \max''')
s=replace(s,'All logarithmic ratios defining $L_q$ are nonnegative, proving its\nlower bound by zero as well. This proves (CR6) with the actual relative\nspectrum, not a freely chosen condition number.',
r'''The integrands defining $\mathfrak C_*$ and
$\mathfrak C_*^{\rm ov}$ are nonnegative. Their proved order
below $L_q$ supplies the whole left chain in (CR6). This is the
necessary compatibility of the actual joint source calculation,
with its full spectrum and overlap, not a free condition number.''')
s=replace(s,'is the computed common-source integral (CR5), bounded by the actual\nrelative spectrum in (CR2)--(CR6).',
r'''is the computed common-source integral (CR5), bounded by the actual
pointwise spectral/trace minimum and its overlap surrogate in
(CR2)--(CR6).''')
save(rel,s,['CR3–4 replace spectral envelope at both sides by exact joint control.','CR6 strengthens every necessary compatibility threshold to C_* and retains chain through overlap and full spectrum.','Exact source integral CR5, observation defect and kernel CR7 remain unchanged.'])

# Reconstruction current mathematical overview includes exact updated endpoint statement.
rel='tex/reconstruction.tex';s=load(rel)
a='The final auxiliary Gamma counterexample retains the reference volumes'
b='Consequently the remaining issue after the mathematics below is the'
new=r'''For this exact interpolation write $M(t)=(1-t)M_{2q}^\Gamma
+tM_{2q}^{\rm ar}$, $C=M(t)^{-1}(M_{2q}^{\rm ar}-M_{2q}^\Gamma)$,
and take $U,W$ to be the original relation and polynomial window
operators (AT13), whose literal inclusion matrices are (AT11).
The complete revised proof (AT18a)--(AT21) defines
$\mathfrak C_*$ as the integral of the pointwise minimum of its
full-spectrum trace bound and $\tfrac12(\lambda_{\max}C-
\lambda_{\min}C)\|U-W\|_1$. It retains the overlap surrogate
$\mathfrak C_*^{\rm ov}$ of (ACM11), with
\[
\begin{aligned}
\left|\log\frac{T_{k,q-1}T_{k,q}}{T_{k,2q-1}T_{k,2q}}\right|
&\le\mathfrak C_*\le\mathfrak C_*^{\rm ov}\le L_q(M(0)^{-1}M(1)),\\
\mathcal B^\Gamma_{h,k}-\mathfrak C_*
&\le\mathcal B^{\rm ar}_{h,k}\le\mathcal B^\Gamma_{h,k}+\mathfrak C_*.
\end{aligned}\tag{R.8a}
\]
This is substitution into (R.8) on the same source; its density is
the actual convolution of $|g/h|^2/(2\pi)$ and its original Gamma
reference retains mass $(2\pi)^{k/2}$. The bound is propagated into
the earlier endpoint intervals, their necessary compatibility
inequalities, the relation-speed interval, and the arithmetic control
exponents below. The separate fixed-$\sigma$ comparison has its own
explicit interpolation (CA14a), of reference mass $\sqrt{2\pi}$;
it is not identified with this tensor Gamma source.
The coarse scalar bounds have compatible widths. The refined
intersection retains actual unevaluated source data, so neither a
certified offcritical zero nor exclusion of every such zero follows
from that coarse compatibility.

'''
s=segment(s,a,b,new)
support=HERE/'support_reconstruction_replacement.json'
if support.exists():
    obj=json.loads(support.read_text(encoding='utf-8'))
    s=replace(s,obj['old'],obj['new'])
save(rel,s,['R8a writes exact joint endpoint estimate and its source/type proof at original R8 use.','Current overview names downstream propagated use and distinguishes fixed sigma mass; no inferred RH conclusion.'])

# AGT keeps its nonlinear proof and explicitly intersects its original endpoint consequence.
rel='tex/continuation/AGT.tex';s=load(rel)
a='with strict inequality in this last comparison whenever\nthe two four-volumes differ.'
b='\nWhen $q=1$, $m=1$ and the second pair is identical.'
new=r'''with strict inequality in this last comparison whenever
the two four-volumes differ. At this same endpoint the revised
(AT18a)--(AT21) supplies the joint control $\mathfrak C_*$,
retaining the full spectrum and the exact trace norm before
integration. Intersecting its two-sided interval with (AGT19) gives
\[
\begin{aligned}
\max\{\mathcal B(0)-\mathfrak C_*,
 2m\log\cosh(\max\{0,A_0-L\})\}
&\le\mathcal B(1)\\
&\le\min\{\mathcal B(0)+\mathfrak C_*,
                    2m\log\cosh(A_0+L)\}.
\end{aligned}\tag{AGT19a}
\]
Each endpoint follows by taking the maximum or minimum of two
already proved bounds for the identical volume. The original
nonlinear angle bound, including its $m=2q-1$ and actual source
relation energies, is retained in full; no relative eigenvalue is
discarded or converted into an assumed tensor asymptotic.
'''
s=segment(s,a,b,new)
save(rel,s,['AGT19a propagates joint spectrum/trace/overlap bound into the actual nonlinear endpoint interval; full AGT11–19 and q=1 proof unchanged.'])

man=dict(scope='Complete derived copies for metric transitive propagation from sealed cumulative current sources; live output untouched.',
 entries=ENTRIES,control='C_* = integral min(full-spectrum trace bound, exact midpoint trace norm); C_* <= C_*^ov <= L_q. Sigma comparison typed separately.',
 source_manifests=[str(BASE/'provenance/PROOF_INPUT_MANIFEST.json'),str(BASE/'provenance/CONTINUATION_INPUT_MANIFEST.json')])
(HERE/'METRIC_PROPAGATION_MANIFEST.json').write_text(json.dumps(man,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(files=len(ENTRIES),manifest=str(HERE/'METRIC_PROPAGATION_MANIFEST.json')),indent=2))
