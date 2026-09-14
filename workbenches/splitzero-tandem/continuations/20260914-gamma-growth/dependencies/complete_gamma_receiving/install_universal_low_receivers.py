from pathlib import Path
import hashlib, json, re, difflib

HERE=Path(__file__).resolve().parent
NB=HERE.parent.parent
JS=NB.parent
OLD=NB/'receiving'
sha=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda b:b.decode('utf-8').replace('\r\n','\n')
def write(p,s):p.write_bytes(s.encode('utf-8'))
for d in ['predecessors','spans','providers']:(HERE/d).mkdir(parents=True,exist_ok=True)
pins={
 'CURRENT_JOINT_SCHUR_NOTE.tex':'e5d30598bac423a60a2af93cefc7dc110cd1190329bc02b4748356d4a01d67dd',
 'SIGNED_RETURN_RECEIVER.tex':'a66e9b37a67241a52beeed85b51c8b75a1855739a5f3d97d90c72e0d8dea0931',
}
docs={}; records=[]; changes=[]
for name,pin in pins.items():
    raw=(OLD/name).read_bytes();assert sha(raw)==pin,(name,sha(raw))
    dst=HERE/'predecessors'/name
    if dst.exists():assert dst.read_bytes()==raw
    else:dst.write_bytes(raw)
    docs[name]=lf(raw)
    records.append({'file':name,'predecessor_source':str(OLD/name),'predecessor_copy':str(dst.relative_to(HERE)),'predecessor_sha256':pin})

def replace(s,old,new,name,label):
    assert s.count(old)==1,(name,label,s.count(old))
    a=HERE/'spans'/f'{name}.{label}.before.tex';b=HERE/'spans'/f'{name}.{label}.after.tex'
    write(a,old);write(b,new)
    changes.append({'file':name,'label':label,'before':str(a.relative_to(HERE)),'after':str(b.relative_to(HERE)),
       'before_sha256':sha(a.read_bytes()),'after_sha256':sha(b.read_bytes()),'start_line_at_replacement':s[:s.index(old)].count('\n')+1})
    return s.replace(old,new,1)

body=lf((HERE/'spans/W_RECEIVING_PROOF.tex').read_bytes())
name='SIGNED_RETURN_RECEIVER.tex';s=docs[name]
anchor='On BHR1 define the actual current receiving endpoints\nby the intersection of these two intervals with the\nexact-low trace endpoints of JSR24a:'
new=body+r'''
\subsection{The current four-interval receiver}
On BHR1 define the actual current receiving endpoints
by the intersection of the retained BHR10 and BHR11
intervals and the universal WRC5 interval with the
exact-low trace endpoints of JSR24a:'''
s=replace(s,anchor,new,name,'complete_universal_low_proof')
old=r''' L_k^{\rm cur}=\max\{\mathscr L_k,H_k^*-b_k^-,
                                      H_k^B-b_{B,k}^-\},\\
 U_k^{\rm cur}=\min\{\mathscr U_k,H_k^*+b_k^+,
                                      H_k^B+b_{B,k}^+\},'''
new=r''' L_k^{\rm cur}=\max\{\mathscr L_k,H_k^*-b_k^-,
              H_k^B-b_{B,k}^-,-W_k-b_k^--a_0\},\\
 U_k^{\rm cur}=\min\{\mathscr U_k,H_k^*+b_k^+,
              H_k^B+b_{B,k}^+,-W_k+b_k^++b_0\},'''
s=replace(s,old,new,name,'actual_fourth_interval')
old=r'''Each interval contains the very same scalar by the
proved morphisms JSR8--15 and BHR4--7. Thus its maximum
and minimum are ordered and preserve all original
information. For tensor orders outside BHR1 define'''
new=r'''Each interval contains the very same scalar by the
proved morphisms JSR8--15, BHR4--7 and WRC3--5.
WRC6 proves that the fourth lower entry is at most the
second, and the fourth upper entry is at least the second.
Thus these maximum and minimum values equal exactly
their previous three-entry values for every finite input.
The extra entry records the universal analytic centre;
it does not narrow the retained exact-low interval.
For tensor orders outside BHR1 define'''
s=replace(s,old,new,name,'actual_containment_proof')
old=r'''them with the two proved full-source enclosures.'''
new=r'''them with the three proved full-source enclosures.
The fourth total entry, contributed by WRC5, leaves
the prior endpoints exactly unchanged by WRC6; the
additional WRC7 presentation exposes the full universal centre.'''
s=replace(s,old,new,name,'actual_arithmetic_domain_description')
old=r'''proof including BRD41a, and the complete CTR1--54 proof. The companion JSON'''
new=r'''proof including BRD41a, the complete CTR1--54 proof,
the complete LET1--21 scalar-source proof, and the complete
PHT1--23/HCT1--39 positive moment and Hankel calculation.
WRC1--7 proves their receiving substitution and exact interval
containment. The companion JSON'''
s=replace(s,old,new,name,'complete_provider_statement')
docs[name]=s

name='CURRENT_JOINT_SCHUR_NOTE.tex';s=docs[name]
old=r'''All complete proofs accompany this text; the historical sealed
46-page edition remains unchanged.'''
new=r'''LET1--21 now also controls the original scalar low endpoint,
giving a fully universal centre $W_k$ whose exact positive
moment and parity-Hankel product is evaluated by PHT1--23/HCT1--39.
Its same-scalar interval contains the earlier interval with
the exact low endpoint. The four-entry intersection therefore
retains precisely the preceding finite endpoints, as proved below.
All complete proofs accompany this text; the historical sealed
46-page edition and the complete accepted predecessor remain unchanged.'''
s=replace(s,old,new,name,'current_integration_statement')
anchor=r'\subsection{Return to the original arithmetic criterion}'
insert=r'''\subsection{The universal scalar low endpoint and full reference}
On the same original threshold, let $\mu_j=\int_{\R}y^j\sigma(y)\,dy$
have its literal moment index. This is LET's $m_j$; PHT's
even-moment sequence has $\mu_n^{\rm even}=m_{2n}=\mu_{2n}$.
The original mass is $\mu_0=\sqrt{2\pi}$ and remains present
in both numerator and denominator. The complete LET1--18
scalar-source proof, reproduced in the receiving application
WRC1--2, gives
\begin{equation}
\begin{gathered}
 E_0=|\alpha_k^\chi|(\epsilon^{-2}-64^{-2})+2\delta_\chi,
 \quad E_\chi=lE_0,\\
 L_1^{\rm tail}=\log(1+\kappa_{I,1}+\kappa_F),\quad
 \kappa_{I,1}=\frac{2\epsilon}{\sqrt{\cos1}}
       \left(\frac43\,2^{-13}e^{2\pi}\right)^q,\\
 a_0=E_0+2L_1^{\rm tail},\quad b_0=a_0+\Delta_f,\quad
 e_0=\log\mathfrak r_\chi-
       \log\frac{\mu_{2q+2l}}{\mu_{2q}}\in[-a_0,b_0].
\end{gathered}\label{eq:universal-low-error}
\end{equation}
The exact maps on the original bulk are $u\mapsto(iy)^q u$
and $u\mapsto\chi(c+iy)u$, with bounded multiplication bridge
$h\mapsto\chi(c+iy)h/(iy)^q$ and its bounded inverse.
It commutes with the same original $f$ multiplication.
The scalar log-ratio density error is bounded by the oscillation
$E_0$; the original factor $|f|^2/|y|^{2l}$ gives an error
in $[0,\Delta_f]$. Each of the four scalar integrals equals
its own bulk integral times $e^{t_H}$ with
$0\leq t_H\leq L_1^{\rm tail}$, by the direct scalar tail
proof LET12--16. Their signs are $(+,-,-,+)$.
Adding these terms proves \eqref{eq:universal-low-error};
the high-rank restriction $r\geq l$ is never invoked at rank one.

Define the complete original-parameter reference
\begin{equation}
\begin{gathered}
 P_k=\log D_{l,q-1}+\log D_{l,q}
                         -\log D_{l,2q-1}-\log D_{l,2q},\\
 W_k=P_k-\log\frac{\mu_{2q+2l}}{\mu_{2q}}+\rho_q+\rho_{q+1},\\
 H_k^*=-W_k+e_0,\qquad
 R_k^0-R_k^\sigma=-W_k+e_0-e_q-e_{q+1}.
\end{gathered}\label{eq:universal-entire-centre}
\end{equation}
Substitute $C_{\rm rel}=P_k-\log\mathfrak r_\chi$
into \eqref{eq:universal-return} to prove both equalities.
All full-$y$ coordinate factors are already present in the
two $\rho_r$. Exponentiating gives exactly
\begin{equation}
 e^{W_k}=\frac{D_{l,q-1}D_{l,q}}{D_{l,2q-1}D_{l,2q}}
 \frac{\mu_{2q}}{\mu_{2q+2l}}
 \frac{\det\mathsf M_{q+l,q}}{\det\mathsf M_{q,q}}
 \frac{\det\mathsf M_{q+l,q+1}}{\det\mathsf M_{q,q+1}}.
 \label{eq:positive-entire-centre}
\end{equation}
The complete PHT/HCT calculation evaluates precisely this
positive rational expression through its finite positive moment
recurrence and parity-Hankel product; the original low factor
and every original source mass occur before cancellation.
No leading asymptotic value is assigned by this identity.

The high sum is in $[-b_k^+,b_k^-]$. Subtract that full
sum and add the low error to obtain
\begin{equation}
 -W_k-b_k^--a_0\leq R_k^0-R_k^\sigma
                         \leq-W_k+b_k^++b_0.
 \label{eq:universal-fourth-interval}
\end{equation}
The exact translation $H_k^*=-W_k+e_0$ moreover gives
\begin{equation}
 -W_k-b_k^--a_0\leq H_k^*-b_k^-,\qquad
 H_k^*+b_k^+\leq-W_k+b_k^++b_0.
 \label{eq:universal-interval-containment}
\end{equation}
The respective differences are $e_0+a_0\geq0$ and
$b_0-e_0\geq0$. Therefore the new interval contains
the previous exact-low interval at every stated finite input.
It supplies a universal centre for growing-family analysis
while preserving the tighter exact-low receiving values.

'''
s=replace(s,anchor,insert+anchor,name,'complete_universal_low_receiving_proof')
old=r''' L_k=\max\{\mathscr L_k,H_k^*-b_k^-,H_k^B-b_{B,k}^-\},\\
 U_k=\min\{\mathscr U_k,H_k^*+b_k^+,H_k^B+b_{B,k}^+\}.'''
new=r''' L_k=\max\{\mathscr L_k,H_k^*-b_k^-,H_k^B-b_{B,k}^-,
                                      -W_k-b_k^--a_0\},\\
 U_k=\min\{\mathscr U_k,H_k^*+b_k^+,H_k^B+b_{B,k}^+,
                                      -W_k+b_k^++b_0\}.'''
s=replace(s,old,new,name,'actual_fourth_interval')
old=r'''contains precisely $R_k^0-R_k^\sigma$ by BHR10--12, so
$L_k\leq U_k$ and $U_k-L_k\leq b_k^-+b_k^+=o(q)$.
Below the stated threshold set'''
new=r'''contains precisely $R_k^0-R_k^\sigma$ by BHR10--12 and
\eqref{eq:universal-entire-centre}--\eqref{eq:universal-fourth-interval},
so $L_k\leq U_k$ and $U_k-L_k\leq b_k^-+b_k^+=o(q)$.
By \eqref{eq:universal-interval-containment}, the fourth lower
entry is at most the second and the fourth upper entry is
at least the second. The maximum and minimum thus equal
their previous three-entry values exactly.
Below the stated threshold set'''
s=replace(s,old,new,name,'actual_containment_proof')
old=r'''It follows by adding the original arithmetic interval to
\eqref{eq:universal-return}, retaining every sign.'''
new=old+r'''
The same unchanged arithmetic allowance also gives
\begin{equation}
 \mathcal B_k^0-W_k-b_k^--a_0-a_k^-
 \leq\mathcal B_k^{\rm ar}
 \leq\mathcal B_k^0-W_k+b_k^++b_0+a_k^+,
 \label{eq:universal-centred-arithmetic}
\end{equation}
with a second valid interval obtained by replacing $a_k^\pm$
by their original $D_k^\pm$. This follows by adding the same
signed arithmetic interval to \eqref{eq:universal-fourth-interval}.
Its complete Gamma return is
$\Delta_k^\Gamma+W_k=\delta_k^\sigma+e_0-e_q-e_{q+1}$.
The current finite arithmetic and HC endpoints remain exactly
unchanged because the intersection endpoints are unchanged.
The new form exposes the full universal centre; it makes no
improvement to the original arithmetic defect allowance.
LET18 gives $a_0,b_0=O(1)$ for $m=1$ and $O(k^{-1})$
for fixed $m\geq2$, so the existing $o(q)$ Gamma error,
signed $q\log k$ constants and simple-zero $5/7$ rate
transport to this centre by addition, as proved in WRC7.'''
s=replace(s,old,new,name,'actual_universal_arithmetic_return')
old=r'''The full-source BRD/CTR estimate now controls the Gamma
comparison error at $o(q)$ and identifies the two remaining
universal Hankel ratios in \eqref{eq:fullsource-hankel}.
The exact relation-dependent low moment and the original
arithmetic deficit remain in the displayed upper slack.
The next growing-family evaluation therefore concerns
those specified Hankel determinants together with their
retained original low constant, rather than another
fixed-input trace approximation to the same Gamma return.'''
new=r'''The full-source BRD/CTR estimate and LET scalar-source
calculation give the entire universal centre
\eqref{eq:positive-entire-centre} with $o(q)$ Gamma error.
PHT1--23/HCT1--39 evaluates its exact positive moment and
parity-Hankel product. The exact relation-dependent low
moment remains in the tighter finite interval, and the
original arithmetic deficit remains in both presentations.
The next growing-family evaluation concerns precisely this
complete positive product, retaining its low moment ratio
and every high-rank factor. Its error estimate alone assigns
no leading value to that product.'''
s=replace(s,old,new,name,'current_analytic_continuation')
old=r'''The current full-source result is
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
new=r'''The current full-source result retains the exact identity
$R_k^0-R_k^\sigma=H_k^*-e_q-e_{q+1}$ and now also gives
$R_k^0-R_k^\sigma=-W_k+e_0-e_q-e_{q+1}$ with every finite
one-sided error in \eqref{eq:fullsource-hankel} and
\eqref{eq:universal-low-error}. The full universal centre
$W_k$ is the logarithm of the positive moment and parity-Hankel expression
\eqref{eq:positive-entire-centre}, evaluated by the complete
PHT/HCT proofs. Its new enclosure contains the retained
exact-low enclosure by \eqref{eq:universal-interval-containment};
the current finite intersection endpoints remain identical.
The mixed-Schur determinant remains the same scalar by
JSR8--15 and WRC3, and its trace bounds remain in that intersection.
The original arithmetic defect is still present with its
unchanged asymmetric bounds. The next calculation is the
growing-family evaluation of the displayed entire positive
product with all low and high factors retained. No RH endpoint
or leading Hankel value is asserted by this error estimate.'''
s=replace(s,old,new,name,'current_final_mathematical_state')
docs[name]=s

for rec in records:
    name=rec['file'];s=docs[name];restored=s
    for ch in reversed(changes):
        if ch['file']!=name:continue
        a=lf((HERE/ch['after']).read_bytes());b=lf((HERE/ch['before']).read_bytes())
        assert restored.count(a)==1,(name,ch['label'],'reverse')
        restored=restored.replace(a,b,1)
    raw=(OLD/name).read_bytes();assert sha(raw)==pins[name]
    assert restored==lf(raw)
    back=(restored.replace('\n','\r\n') if b'\r\n' in raw else restored).encode('utf-8')
    assert back==raw
    write(HERE/name,s)
    write(HERE/'predecessors'/(name+'.diff'),''.join(difflib.unified_diff(lf(raw).splitlines(True),s.splitlines(True),fromfile='accepted19/'+name,tofile='current20/'+name)))
    oldtags=re.findall(r'\\tag\{([^}]+)\}',lf(raw));newtags=re.findall(r'\\tag\{([^}]+)\}',s)
    oldlabels=re.findall(r'\\label\{([^}]+)\}',lf(raw));newlabels=re.findall(r'\\label\{([^}]+)\}',s)
    assert all(x in newtags for x in oldtags) and len(newtags)==len(set(newtags))
    assert all(x in newlabels for x in oldlabels) and len(newlabels)==len(set(newlabels))
    clean=re.sub(r'(?<!\\)%[^\n]*','',s);stack=[]
    for kind,env in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
        if kind=='begin':stack.append(env)
        else:assert stack and stack.pop()==env,(name,'environment',env)
    assert not stack and clean.count(r'\[')==clean.count(r'\]')
    assert not re.search(r'(?<!\\)\\\n',clean)
    rec.update({'successor_sha256':sha((HERE/name).read_bytes()),'bytes':len((HERE/name).read_bytes()),'new_tags':[x for x in newtags if x not in oldtags],'new_labels':[x for x in newlabels if x not in oldlabels]})
assert docs['SIGNED_RETURN_RECEIVER.tex'].count(body)==1

providers=[]
def copy(src,name,pin=None):
    raw=src.read_bytes()
    if pin:assert sha(raw)==pin,(name,sha(raw),pin)
    dst=HERE/'providers'/name;dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists():assert dst.read_bytes()==raw,(name,'provider changed')
    else:dst.write_bytes(raw)
    providers.append({'source':str(src),'copy':str(dst.relative_to(HERE)),'sha256':sha(raw),'bytes':len(raw)})
for src in sorted((OLD/'providers').rglob('*')):
    if src.is_file():copy(src,str(src.relative_to(OLD/'providers')))
copy(OLD/'FULL_RECEIVING_RECEIPT.json','accepted19/FULL_RECEIVING_RECEIPT.json','2a2ca2523d3353ddf2aa3fff5d7aaa3316f53cf1806e4b539b1eaea93b1f8a00')
copy(OLD/'DELTA_REVIEW.md','accepted19/DELTA_REVIEW.md')
copy(NB/'future_hankel/LOW_ENDPOINT_TRANSPORT.tex','LET/LOW_ENDPOINT_TRANSPORT.tex','a31250b693b9e687481bc7bfa7638707013930c4bfb9b6a8f39c201779d02a44')
copy(JS/'future_hankel/low_endpoint_review/REVIEW.md','LET/REVIEW.md','ec37eb7ee5bc23e785c11f76509fac3f80e516efaa176d6ac6173e8e86839b83')
copy(JS/'future_hankel/low_endpoint_review/RECEIPT.json','LET/RECEIPT.json','de1ef3e3bce8accef8815c7fc874ae9bbb638152ab29a9c9f274408f39c61075')
copy(JS/'future_hankel/PARITY_AND_TODA_TRANSPORT.tex','PHT/PARITY_AND_TODA_TRANSPORT.tex','3b5914ff3d99e18f881fc59a372787dadfe1e1ef8aa9ebeefebb62d6a6a9991d')
copy(JS/'future_hankel/independent_contiguous.tex','PHT/independent_contiguous.tex','e01021c3b9b659cd897cc95179391b3bde0de63397405426fef2cda420e81196')
copy(JS/'future_hankel/PARITY_TODA_INDEPENDENT_REVIEW.md','PHT/PARITY_TODA_INDEPENDENT_REVIEW.md','662dd547a4013607c5d4818a103819f6f01fec96d38af731915e9aabb7653cd8')
receipt={'scope':'Final source-only cut20 receiver under future_hankel/receiving. Accepted19 receiving files, folder19, older readers and outer seals are unchanged. No build or numerical run.',
 'receivers':records,'changes':changes,'providers':providers,
 'complete_receiving_proof':{'file':'spans/W_RECEIVING_PROOF.tex','sha256':sha((HERE/'spans/W_RECEIVING_PROOF.tex').read_bytes()),'tags':'WRC1--7','embedded_once_in':'SIGNED_RETURN_RECEIVER.tex','root_accepted':True},
 'mathematics':'Exact identity Hstar=-W+e0 and e0 in [-a0,b0] prove the new W interval contains the retained Hstar interval. Fourth max/min entries therefore leave current finite endpoints exactly unchanged. All original arithmetic allowances and outside-threshold branches remain. LET and PHT/HCT give a fully universal analytic centre and its positive rational expression, without assigning a leading asymptotic value.',
 'checks':['fixed predecessor and final provider pins verified','all predecessor raw bytes preserved and unchanged','exactly-once changed spans and reverse reconstruction to original bytes','all old tags and labels retained with no duplicates','ordered TeX environments, display delimiters and row separators checked','complete WRC body embedded exactly once'],
 'validation_scope':'Root accepted complete WRC1--7 with final sign-prose and moment-index dictionary repairs; final changed receiver spans submitted for bounded independent review. No compilation or PDF claim.'}
review=HERE/'DELTA_REVIEW.md'
if review.exists():
    text=review.read_text(encoding='utf-8')
    assert all(rec['successor_sha256'] in text for rec in records)
    receipt['independent_delta_review']={'file':review.name,'sha256':sha(review.read_bytes())}
    receipt['validation_scope']='Complete WRC and changed receiver mathematics accepted in their recorded scopes. No compilation or PDF claim; cut20 builder is a separate owner.'
write(HERE/'FULL_RECEIVING_RECEIPT.json',json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receivers':records,'proof':receipt['complete_receiving_proof'],'changes':len(changes),'providers':len(providers),'receipt_sha256':sha((HERE/'FULL_RECEIVING_RECEIPT.json').read_bytes())},indent=2))
