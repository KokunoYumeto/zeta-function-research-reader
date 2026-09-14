from pathlib import Path
import re, json, hashlib, difflib

HERE=Path(__file__).resolve().parent
NB=HERE.parent
JS=NB.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda b:b.decode('utf-8').replace('\r\n','\n')
def write(p,s):p.write_bytes(s.encode('utf-8'))
inputs={
 'CURRENT_JOINT_SCHUR_NOTE.tex':(JS/'CURRENT_JOINT_SCHUR_NOTE.tex','9e9900e742e4c2df083088ea8cac37584b672087b24a877e923f06669e00cee3'),
 'SIGNED_RETURN_RECEIVER.tex':(JS/'SIGNED_RETURN_RECEIVER.tex','2a22fa6d6f7bc7f861e8e142d2027bcd1391e013a01ea775b24a3bf0b156969d'),
}
documents={}; records=[]; changes=[]
for name,(path,pin) in inputs.items():
    raw=path.read_bytes();assert sha(raw)==pin,(name,sha(raw))
    dst=HERE/'predecessors'/name
    if dst.exists():assert dst.read_bytes()==raw
    else:dst.write_bytes(raw)
    documents[name]=lf(raw)
    records.append({'file':name,'source':str(path),'source_sha256':pin,'predecessor':str(dst.relative_to(HERE))})

def replace(s,old,new,name,label):
    assert s.count(old)==1,(name,label,s.count(old))
    a=HERE/'spans'/f'{name}.{label}.before.tex'
    b=HERE/'spans'/f'{name}.{label}.after.tex'
    write(a,old);write(b,new)
    changes.append({'file':name,'label':label,'before':str(a.relative_to(HERE)),
       'after':str(b.relative_to(HERE)),'before_sha256':sha(a.read_bytes()),'after_sha256':sha(b.read_bytes()),
       'start_line_at_replacement':s[:s.index(old)].count('\n')+1})
    return s.replace(old,new,1)

body=lf((HERE/'spans/BHR_APPLICATION_BODY.tex').read_bytes())
wrapper=r'''\documentclass[11pt,a4paper]{article}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage[margin=23mm]{geometry}
\usepackage{hyperref}
\allowdisplaybreaks
\newcommand{\C}{\mathbb C}
\newcommand{\R}{\mathbb R}
\title{Full-source Hankel control returned to the original signed criterion}
\author{Split-Zero research programme}
\date{14 September 2026}
\begin{document}
\maketitle
This standalone application is accompanied by the complete original
JSR source, the complete BRD and CTR proofs, and the full earlier
providers. Its BHR1--15 body is also inserted, byte for byte, into
the complete JSR successor. A cumulative compiler should print that
body once, while retaining both complete source presentations.

'''
write(HERE/'FULL_SOURCE_RECEIVING_APPLICATION.tex',wrapper+body+'\n\\end{document}\n')

name='SIGNED_RETURN_RECEIVER.tex';s=documents[name]
anchor=r'\section{The finite arithmetic majorant at each original degree}'
s=replace(s,anchor,body+'\n'+anchor,name,'complete_full_source_proof')
old=r''' \mathcal B_k^0+\mathscr L_k-a_k^-
 &\leq\mathcal B_k^{\rm ar}
 \leq\mathcal B_k^0+\mathscr U_k+a_k^+,\\
 \mathcal B_k^0+\mathscr L_k-D_k^-
 &\leq\mathcal B_k^{\rm ar}
 \leq\mathcal B_k^0+\mathscr U_k+D_k^+.'''
new=old.replace(r'\mathscr L_k',r'L_k^{\rm cur}').replace(r'\mathscr U_k',r'U_k^{\rm cur}')
s=replace(s,old,new,name,'actual_arithmetic_endpoints')
old=r'''Indeed the unchanged TWA equality is exactly
$\mathcal B_k^{\rm ar}=\mathcal B_k^0+
\mathcal H_k+\delta_k^\sigma$; add its two proved
signed intervals. The first line is contained in the
note's interval with the same trace endpoints and
$\pm2\Xi_{k,2q}$. The second line evaluates the arithmetic
allowances by their complete finite source constants.'''
new=r'''Indeed the unchanged TWA equality is exactly
$\mathcal B_k^{\rm ar}=\mathcal B_k^0+
\mathcal H_k+\delta_k^\sigma$; add the signed original
arithmetic interval to the current Gamma intersection BHR12.
Its endpoints equal the exact-low trace endpoints below
the explicit full-source threshold and otherwise intersect
them with the two proved full-source enclosures.
The first line is contained in the preceding trace-only
interval because the Gamma lower endpoint increases and
its upper endpoint decreases. The same original
$a_k^-,a_k^+$ are retained. The second line evaluates
those unchanged arithmetic allowances by the same full
finite source constants $D_k^-,D_k^+$; the full-source
Gamma result does not improve the arithmetic deficit itself.'''
s=replace(s,old,new,name,'actual_arithmetic_proof')
old=r'''The constants in JSR21 apply to this exact difference,
not to $\Delta_k^\Gamma$ with its Gamma return omitted.'''
new=r'''The constants in JSR21 apply to this exact difference.
The full-source calculation additionally gives
$\Delta_k^\Gamma-H_k^*=\delta_k^\sigma-e_q-e_{q+1}$,
with every finite signed error in BHR7 and BHR10.
Thus BHR14 transports the same arithmetic constants to
the explicitly specified Hankel centre with its $o(q)$
Gamma error. Neither formula omits the Gamma return.'''
s=replace(s,old,new,name,'actual_hankel_centre_return')
old=r'''   (\mathscr U_k+a_k^+)-(\mathscr L_k-a_k^-)}{q\log k}'''
new=old.replace(r'\mathscr U_k',r'U_k^{\rm cur}').replace(r'\mathscr L_k',r'L_k^{\rm cur}')
s=replace(s,old,new,name,'actual_exact_width')
old=r'''   (\mathscr U_k+D_k^+)-(\mathscr L_k-D_k^-)}{q\log k}'''
new=old.replace(r'\mathscr U_k',r'U_k^{\rm cur}').replace(r'\mathscr L_k',r'L_k^{\rm cur}')
s=replace(s,old,new,name,'actual_evaluated_width')
old=r'''The finite widths are bounded by
$1+a_k^-+a_k^+$ and $1+D_k^-+D_k^+$ respectively.'''
new=r'''The current Gamma interval is contained in this exact-low
trace interval, so the finite arithmetic widths are still
bounded by $1+a_k^-+a_k^+$ and $1+D_k^-+D_k^+$ respectively.
Independently of this adaptive trace-order choice, BHR12
already gives $o(q)$ for the Gamma width on the original
growing-family domain, from its complete integral bounds.'''
s=replace(s,old,new,name,'current_width_proof')
old=r''' \max\{0,\mathcal B_k^0+\mathscr L_k-D_k^-
                         -4q\log(D_hk)\}
 \leq\mathcal R_k\\
 \leq\mathcal B_k^0+\mathscr U_k+D_k^+
                         -4q\log(D_hk).'''
new=old.replace(r'\mathscr L_k',r'L_k^{\rm cur}').replace(r'\mathscr U_k',r'U_k^{\rm cur}')
s=replace(s,old,new,name,'actual_HC_endpoints')
old=r'''GSR1--33/JQR1--39 source, ODD1--14, and the accepted full
HMR successor including HMR44a--44c.'''
new=r'''GSR1--33/JQR1--39 source, ODD1--14, the accepted full
HMR successor including HMR44a--44c, the complete BRD1--42
proof including BRD41a, and the complete CTR1--54 proof.'''
s=replace(s,old,new,name,'complete_provider_statement')
documents[name]=s

name='CURRENT_JOINT_SCHUR_NOTE.tex';s=documents[name]
old=r'''concrete PR31 resolvent return. These proofs accompany this text.'''
new=r'''concrete PR31 resolvent return. The full BRD source integrals
and CTR rank-$l$ transport now reduce both original high relation
determinants to explicit universal full-line Hankel ratios with
proved $o(q)$ errors. BHR1--15 returns their exact one-sided
errors through the same signed Gamma and arithmetic criteria.
All complete proofs accompany this text; the historical sealed
46-page edition remains unchanged.'''
s=replace(s,old,new,name,'current_integration_statement')
old=r'''DMR/QDC, as stated in the new request, give $|\delta_k^\sigma|\le2\Xi_{k,2q}$ and the asserted rate for $\Xi$. This note does not reattribute that theorem or replace its full determinant proof by diagonal estimates. The supplied proof-file inventory is recorded separately. When a requested proof body is absent from that inventory, its theorem is an explicitly inherited input, not a claim of independent verification. All results from Section~\ref{sec:gamma} through Section~\ref{sec:rank} below have their proofs here and do not assume the missing growing-family upper bound.'''
new=r'''The complete retained DMR/QDC and ODD providers prove the
original source deficits and their signed quotient, kernel and
boundary return. In the present receiving source the actual bounds
are $-a_k^-\leq\delta_k^\sigma\leq a_k^+$, with both original
low and high endpoint sums defined below, and with their full
finite majorants in JSR17--21. The new BRD/CTR integral comparison
controls the Gamma term while preserving these arithmetic inputs.
Its full proof bodies and exact source pins accompany the complete
current note; no source estimate is replaced by a diagonal-moment
assertion or by an assumed growing-family upper value.'''
s=replace(s,old,new,name,'actual_inherited_source_input')
anchor=r'\subsection{Return to the original arithmetic criterion}'
insert=r'''\subsection{The complete high relation integrals now have a universal return}
The complete BRD proof controls the original inner and far regions;
the complete CTR proof transports the ratio of the same two
restriction Grams with coefficient $l$, retaining its actual
intersection and both residual metric blocks. On the original
domain $k\geq2048\sqrt{\delta^2+\gamma^2}$, put
$\epsilon=2^{-10}$, $d=\delta^2$, $g=\gamma^2$ and retain
\begin{equation}
\begin{gathered}
 \alpha_k^\chi=\frac{k(k+2)(d-g)}{3q},\quad
 \tau_\epsilon=\frac{k^2(d+g)}{q^2\epsilon^2},\quad
 \delta_\chi=\frac{q\tau_\epsilon^2}{2(1-\tau_\epsilon)},\\
 E_\chi=l\{|\alpha_k^\chi|(\epsilon^{-2}-64^{-2})+2\delta_\chi\},
 \quad\Delta_f=\frac{l(16l^2-12l-1)}{12q^2\epsilon^2},\\
 \kappa_{I,r}=\frac{2\epsilon r^2}{\sqrt{\cos1}}
       \left(\frac43\,2^{-13}e^{2\pi}\right)^q,\quad
 \kappa_F=\frac{512q}{59\sqrt{\cos1}}e^{-19q},\quad
 L_r^{\rm tail}=r\log(1+\kappa_{I,r}+\kappa_F).
\end{gathered}\label{eq:fullsource-constants}
\end{equation}
Let $R_{q+r-1}$ be the complete original ratio of the
$r$-column Grams $(f\chi S^j)_{j<r}$ and $(\chi S^j)_{j<r}$.
For $r=q,q+1$ the full-line Hankel ratio satisfies
\begin{equation}
\begin{gathered}
 (\mathsf M_{a,r})_{ij}=\int_{\R}y^{2a+i+j}\sigma(y)\,dy,
 \quad\rho_r=\log\frac{\det\mathsf M_{q+l,r}}{\det\mathsf M_{q,r}},\\
 -E_\chi-2L_r^{\rm tail}\leq
 e_r:=\log R_{q+r-1}-\rho_r
 \leq E_\chi+r\Delta_f+2L_r^{\rm tail}.
\end{gathered}\label{eq:fullsource-hankel}
\end{equation}
The proof is the complete CTR47 decomposition, retained in BHR7:
the density-ratio error is in $[-E_\chi,E_\chi]$, multiplication
by the original $f$ contributes a scalar in $[0,r\Delta_f]$,
and each of the four original/reference tail logarithms is in
$[0,L_r^{\rm tail}]$ with signs $(+,-,-,+)$. These follow
from the full polynomial source inequalities before determinants
are taken. The exact coefficient map to the Hankel source is
$J_{hj}=\binom jh c^{j-h}(\sqrt{-1})^h$, so $|\det J|=1$.
Thus these full-$y$ ratios contain all coordinate factors already;
there is no additional $2lr\log q$ in \eqref{eq:fullsource-hankel}.

The moment entries are determined exactly by CTR50--53:
$\mu_{2n+1}=0$ and $\mu_{2n}=\sqrt{2\pi}(-1)^nc_n$,
where $c_0=1$ and
\begin{equation}
 c_n=-\sum_{j=1}^{n-1}\binom{2n-1}{2j-1}c_j
          -\frac12\sum_{j=0}^{n-1}\binom{2n-1}{2j}c_j.
\end{equation}
This is the coefficient recurrence of the proved original
characteristic function $\sqrt{2\pi}(\cosh t)^{-1/2}$.
Both original mass factors occur in the positive determinant
ratio before cancellation. No comparison measure is unspecified.

Retain the exact low endpoints and their complete product:
\begin{equation}
\begin{gathered}
 D_{l,N}=\prod_{a=0}^N\prod_{j=0}^{2l-1}(a+j+\tfrac12),\quad
 \mathfrak r_\chi=\frac{\int|f\chi|^2d\sigma}{\int|\chi|^2d\sigma},\\
 C_{\rm rel}=\log D_{l,q-1}+\log D_{l,q}
 -\log\mathfrak r_\chi-\log D_{l,2q-1}-\log D_{l,2q},\\
 H_k^*=-C_{\rm rel}-\rho_q-\rho_{q+1},\quad
 L_\Sigma=L_q^{\rm tail}+L_{q+1}^{\rm tail},\\
 b_k^-=2E_\chi+(2q+1)\Delta_f+2L_\Sigma,\qquad
 b_k^+=2E_\chi+2L_\Sigma,\\
 H_k^*-b_k^-\leq R_k^0-R_k^\sigma=-\mathfrak T_k
                         \leq H_k^*+b_k^+.
\end{gathered}\label{eq:universal-return}
\end{equation}
The exact GSR identity gives
$R_k^0-R_k^\sigma=H_k^*-e_q-e_{q+1}$, proving both
signs in the final line. In particular the one-sided
$\Delta_f$ term belongs only to its lower allowance.
The full finite constants give $b_k^\pm=O(k)=o(q)$ for
each fixed original packet, and $O(1)$ for fixed $m\geq2$,
as proved in BHR8--10. The actual $\mathfrak r_\chi$ and
all of its unit, multiplicity and coefficient data remain
in $C_{\rm rel}$; JSR24b evaluates it on its original finite
coefficient Gram. These formulas do not assign a leading
value to the universal Hankel determinant ratios.

'''
s=replace(s,anchor,insert+anchor,name,'complete_full_source_receiving_section')
old=r'''If $[L_k,U_k]$ is the certificate \eqref{eq:cert}, the current arithmetic
receiver is'''
new=r'''Let $[\mathscr L_k,\mathscr U_k]$ be the exact-low trace
interval of JSR24a, obtained from \eqref{eq:cert} by the two
exact GSR low endpoints. On the full-source threshold define
\begin{equation}
\begin{gathered}
 L_k=\max\{\mathscr L_k,H_k^*-b_k^-,H_k^B-b_{B,k}^-\},\\
 U_k=\min\{\mathscr U_k,H_k^*+b_k^+,H_k^B+b_{B,k}^+\}.
\end{gathered}
\end{equation}
Here $H_k^B,b_{B,k}^\pm$ are the full explicit BRD receiving
values in BHR11, with the exact same original integrals and
their retained $2l(2q+1)\log q$ coordinate factor. Each interval
contains precisely $R_k^0-R_k^\sigma$ by BHR10--12, so
$L_k\leq U_k$ and $U_k-L_k\leq b_k^-+b_k^+=o(q)$.
Below the stated threshold set
$L_k=\mathscr L_k$, $U_k=\mathscr U_k$.
The current arithmetic receiver is'''
s=replace(s,old,new,name,'actual_arithmetic_Gamma_intersection')
old=r'''All original mixed
covariance factors remain in that narrower interval.'''
new=r'''All original mixed covariance factors remain in that interval.
The full-source refinement then narrows its Gamma endpoints
by \eqref{eq:universal-return}; the exact arithmetic allowances
$a_k^\pm$ and their established majorants $D_k^\pm$ remain
unchanged. The direct Hankel-centred arithmetic interval is
\begin{equation}
 \mathcal B_k^0+H_k^*-b_k^--a_k^-
 \leq\mathcal B_k^{\rm ar}
 \leq\mathcal B_k^0+H_k^*+b_k^++a_k^+.
\end{equation}
It follows by adding the original arithmetic interval to
\eqref{eq:universal-return}, retaining every sign.'''
s=replace(s,old,new,name,'actual_direct_Hankel_arithmetic_interval')
old=r'''The remaining growing-family calculation concerns the relation-dependent
Schur term together with the original arithmetic deficit in the displayed
upper slack. Fixed-input convergence and the free summand alone do not
supply a sign for that entire expression.'''
new=r'''The full-source BRD/CTR estimate now controls the Gamma
comparison error at $o(q)$ and identifies the two remaining
universal Hankel ratios in \eqref{eq:fullsource-hankel}.
The exact relation-dependent low moment and the original
arithmetic deficit remain in the displayed upper slack.
The next growing-family evaluation therefore concerns
those specified Hankel determinants together with their
retained original low constant, rather than another
fixed-input trace approximation to the same Gamma return.'''
s=replace(s,old,new,name,'current_analytic_continuation')
old=r'''The unresolved expression after these calculations is explicit: the signed sum of $\log\det(I+X_N)$ and $\log\det(I-Y_N)$ in \eqref{eq:return}, or equivalently the mixed term in \eqref{eq:freeplusmixed}, combined with the inherited actual arithmetic $\delta_k^\sigma$. Formula \eqref{eq:cert} is a terminating fixed-input enclosure, not a tensor-uniform estimate. Formula \eqref{eq:arithmeticinterval} is its exact return to the original contradiction criterion. No claim of an RH contradiction, an actual counterexample, or failure of the absolute-base programme is made.'''
new=r'''The current full-source result is
$R_k^0-R_k^\sigma=H_k^*-e_q-e_{q+1}$ with the complete
one-sided error \eqref{eq:fullsource-hankel} and
$e_q+e_{q+1}=o(q)$. The centre $H_k^*$ contains the two
explicit positive universal Hankel ratios at the original
ranks $q,q+1$ and the unchanged exact low constant.
Its finite moment recurrence, source maps and arithmetic
return are proved above and in the complete BHR/CTR providers.
The mixed-Schur determinant remains the exact same scalar
by JSR8--15; its finite trace bounds are retained in the
current intersection. The original arithmetic defect
is still present with its proved asymmetric bounds.
The next calculation is the growing-family evaluation of
the displayed Hankel expressions and their full low-term
return. No RH endpoint or leading Hankel value is asserted
by this approximation-error result.'''
s=replace(s,old,new,name,'current_final_mathematical_state')
documents[name]=s

for rec in records:
    name=rec['file'];s=documents[name];restored=s
    for ch in reversed(changes):
        if ch['file']!=name:continue
        a=lf((HERE/ch['after']).read_bytes());b=lf((HERE/ch['before']).read_bytes())
        assert restored.count(a)==1,(name,ch['label'],'reverse')
        restored=restored.replace(a,b,1)
    raw=inputs[name][0].read_bytes()
    assert restored==lf(raw)
    as_raw=(restored.replace('\n','\r\n') if b'\r\n' in raw else restored).encode('utf-8')
    assert as_raw==raw
    write(HERE/name,s)
    write(HERE/'predecessors'/(name+'.diff'),''.join(difflib.unified_diff(lf(raw).splitlines(True),s.splitlines(True),fromfile='previous/'+name,tofile='current/'+name)))
    oldtags=re.findall(r'\\tag\{([^}]+)\}',lf(raw));newtags=re.findall(r'\\tag\{([^}]+)\}',s)
    assert all(x in newtags for x in oldtags)
    assert len(newtags)==len(set(newtags))
    labels_old=re.findall(r'\\label\{([^}]+)\}',lf(raw));labels_new=re.findall(r'\\label\{([^}]+)\}',s)
    assert all(x in labels_new for x in labels_old)
    assert len(labels_new)==len(set(labels_new))
    rec.update({'successor_sha256':sha((HERE/name).read_bytes()),'bytes':len((HERE/name).read_bytes()),'new_tags':[x for x in newtags if x not in oldtags]})

providers=[]
def copy(src,name,pin=None):
    raw=src.read_bytes()
    if pin:assert sha(raw)==pin,(name,sha(raw),pin)
    dst=HERE/'providers'/name;dst.parent.mkdir(exist_ok=True,parents=True)
    if dst.exists(): assert dst.read_bytes()==raw,(name,'frozen provider differs')
    else:dst.write_bytes(raw)
    providers.append({'source':str(src),'copy':str(dst.relative_to(HERE)),'sha256':sha(raw),'bytes':len(raw)})
copy(NB/'ORIGINAL_RELATION_BULK_CONTROL.tex','BRD.tex','4d6e3df419edcedbe7e66e6f802bdeca6e088d9036c5b4c17692517995ebcba9')
copy(NB/'contrast_transport.tex','CTR.tex','3763cc964d03552ef9281d8fc4b21c9f9ffa8fa7e47c70fe2d66c8084e1fe4b2')
copy(NB/'CONTRAST_TRANSPORT_REVIEW.md','CONTRAST_TRANSPORT_REVIEW.md','aec6f8be1ac41b1252dcd7f1ee1d9ac92e1fd308ec725a82ebec54729da4567d')
copy(NB/'CONTRAST_TRANSPORT_RECEIPT.json','CONTRAST_TRANSPORT_RECEIPT.json','8b1eeef9dc97c3f7ea0c7a72ac33f3369e2766d3331b6c4e9a55e65d6d8ceabd')
for name in ['independent_constants.tex','far_tail_independent.tex','contrast_transport_independent.tex']:
    copy(NB/name,name)
for src in sorted((JS/'SIGNED_RETURN_PROVENANCE').glob('*')):
    if src.is_file():copy(src,'earlier/'+src.name)
copy(JS/'RATIONAL_GAMMA_CERTIFICATE.tex','RATIONAL_GAMMA_CERTIFICATE.tex')
sealed_math=NB/'reader/dependencies/joint_schur_46/provenance/math_sources'
for name in ['JOINT_SCHUR_RESOLVENT_APPLICATION.tex','JOINT_SCHUR_EXACT_INTEGRATION.tex','FREE_BOUNDARY_PROOF.tex','CALIBRATION.tex']:
    copy(sealed_math/name,'earlier/'+name)
ind=JS.parent.parent/'next_phase_graph_intake/boundary_row_stability/high_moment_return/next_determinant_review/determinant_backpropagation/odd_receiving_precision'
copy(ind/'HANKEL_SIGNED_RECEIVING.tex','HANKEL_SIGNED_RECEIVING.tex')

for name in ['CURRENT_JOINT_SCHUR_NOTE.tex','SIGNED_RETURN_RECEIVER.tex','FULL_SOURCE_RECEIVING_APPLICATION.tex']:
    s=(HERE/name).read_text(encoding='utf-8');clean=re.sub(r'(?<!\\)%[^\n]*','',s)
    stack=[]
    for kind,env in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
        if kind=='begin':stack.append(env)
        else:assert stack and stack.pop()==env,(name,'environment',env)
    assert not stack,(name,stack)
    assert clean.count(r'\[')==clean.count(r'\]'),(name,'display')
    assert not re.search(r'(?<!\\)\\\n',clean),(name,'single row separator')

receipt={'scope':'New receiving directory only; complete NOTE/JSR successors and complete full-source application. No sealed46/folder18 bytes or outer seals changed. No build.',
 'receivers':records,'changes':changes,'providers':providers,
 'standalone_application':{'file':'FULL_SOURCE_RECEIVING_APPLICATION.tex','sha256':sha((HERE/'FULL_SOURCE_RECEIVING_APPLICATION.tex').read_bytes()),'body':'spans/BHR_APPLICATION_BODY.tex','body_sha256':sha((HERE/'spans/BHR_APPLICATION_BODY.tex').read_bytes()),'embedded_once_in':'SIGNED_RETURN_RECEIVER.tex'},
 'mathematics':'Complete BRD/CTR full-source signed error returned through exact original high ranks q,q+1, low rchi and Crel, -T, Gamma intersection and unchanged exact arithmetic allowances. Hankel full-y centre has no additional q-coordinate factor.',
 'checks':['original and provider pins verified','all original full receiver bytes preserved','every replacement matches once and reverse reconstruction restores exact predecessor bytes','all old tags/labels retained with no local duplicates','ordered TeX environments/display delimiters and row separators checked'],
 'remaining_validation':'Root final review of receiving edits; no compilation or PDF claim.'}
review=HERE/'DELTA_REVIEW.md'
if review.exists():
    review_text=review.read_text(encoding='utf-8')
    assert all(rec['successor_sha256'] in review_text for rec in records), 'final receiver pin missing from delta review'
    receipt['independent_delta_review']={'file':review.name,'sha256':sha(review.read_bytes()),'scope':'changed actual NOTE/JSR receiving formulas and claims only; root separately accepted complete BHR body'}
    receipt['remaining_validation']='New body and changed receiving mathematics accepted in their recorded scopes. No compilation or PDF claim from this task; reader is a separate owner.'
write(HERE/'FULL_RECEIVING_RECEIPT.json',json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receivers':records,'application':receipt['standalone_application'],'changes':len(changes),'provider_count':len(providers),'receipt_sha256':sha((HERE/'FULL_RECEIVING_RECEIPT.json').read_bytes())},indent=2))
