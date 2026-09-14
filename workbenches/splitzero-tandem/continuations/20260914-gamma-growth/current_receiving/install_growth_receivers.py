from pathlib import Path
import hashlib, json, re, difflib

HERE=Path(__file__).resolve().parent
GROWTH=HERE.parent
JS=GROWTH.parent
OLD=JS/'next_bulk_density/future_hankel/receiving'
sha=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda b:b.decode('utf-8').replace('\r\n','\n')
def write(p,s):p.write_bytes(s.encode('utf-8'))
for d in ['predecessors/cut20','spans','providers/growth']:(HERE/d).mkdir(parents=True,exist_ok=True)

old_snapshot=[]
for src in sorted(OLD.rglob('*')):
    if not src.is_file():continue
    raw=src.read_bytes();rel=src.relative_to(OLD)
    dst=HERE/'predecessors/cut20'/rel;dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists():assert dst.read_bytes()==raw,('changed predecessor',str(rel))
    else:dst.write_bytes(raw)
    old_snapshot.append({'path':str(rel),'sha256':sha(raw),'bytes':len(raw)})

pins={
 'CURRENT_JOINT_SCHUR_NOTE.tex':'c94cf1fd34170bd7194ce3a5fcd4e7e06e9e3dad3114d9a824673b54ad084d7c',
 'SIGNED_RETURN_RECEIVER.tex':'2d353afa6e5f0ed9f8ac9756356447b2d0538e30a6688154ca4dc8cd1ddbfb5c',
}
docs={};records=[];changes=[]
for name,pin in pins.items():
    raw=(OLD/name).read_bytes();assert sha(raw)==pin,(name,sha(raw))
    docs[name]=lf(raw)
    records.append({'file':name,'predecessor_source':str(OLD/name),'predecessor_copy':'predecessors/cut20/'+name,'predecessor_sha256':pin})

def replace(s,old,new,name,label):
    assert s.count(old)==1,(name,label,s.count(old))
    a=HERE/'spans'/f'{name}.{label}.before.tex';b=HERE/'spans'/f'{name}.{label}.after.tex'
    write(a,old);write(b,new)
    changes.append({'file':name,'label':label,'before':str(a.relative_to(HERE)),'after':str(b.relative_to(HERE)),
      'before_sha256':sha(a.read_bytes()),'after_sha256':sha(b.read_bytes()),'start_line_at_replacement':s[:s.index(old)].count('\n')+1})
    return s.replace(old,new,1)

body=lf((HERE/'spans/GROWTH_RECEIVING_BODY.tex').read_bytes())
appendix=r'''
\clearpage
\part*{Complete proofs of the growing Gamma return}
The following are the complete accepted proof bodies, included without
mathematical alteration. Their exact source pins, the complete cut20
predecessor and all earlier source providers are retained alongside
this complete successor.
\input{providers/growth/original_product_expansion.tex}
\input{providers/growth/recurrence_bounds.tex}
\paragraph{Exact dictionary for the equilibrium provider.}
The elliptic modulus $k$ used locally in EIQ is the $\kappa$ of GEL,
and EIQ's local $m=(u^2+v^2)/2$ is an endpoint midpoint. They are
distinctly indexed coordinates from the original packet
$k_{\rm packet}=4l+1$ and multiplicity $m_{\rm packet}$.
GEL3 gives their exact parameter map
$\alpha=a/n$, $\beta=\pi q/(2n)$, tending to $(2,\pi)$ on
the original sequences. GEL's constant $C_\Gamma=\Gamma(1/4)^2/(2\pi)$
in its source bound retains that definition; the leading coefficient
is the separately defined $\mathcal C_\Gamma$ in GEL18.
\input{providers/growth/EXACT_SQRT_LOG_EQUILIBRIUM.tex}
\input{providers/growth/GAMMA_ENSEMBLE_LEADING_RETURN.tex}
\input{providers/growth/signed_growth_receiver.tex}
'''

name='CURRENT_JOINT_SCHUR_NOTE.tex';s=docs[name]
s=replace(s,r'\end{abstract}',r'''The complete original Gamma centre now satisfies
$lq/64\leq W_k\leq6lq$ and $W_k/(lq)\to\mathcal C_\Gamma>0$,
where the exact equilibrium integral is given below. Returning it
through the same mixed quotient and arithmetic maps proves
$\Delta_k^\Gamma/(kq)\to-\mathcal C_\Gamma/4$ and the necessary
baseline and HC relations, retaining all original source allowances.
\end{abstract}''',name,'current_abstract_growth')
old=r'''Its same-scalar interval contains the earlier interval with
the exact low endpoint. The four-entry intersection therefore
retains precisely the preceding finite endpoints, as proved below.'''
new=r'''Its same-scalar interval contains the earlier interval with
the exact low endpoint. The four-entry intersection retains precisely
those exact finite endpoints. RWB1--27 now proves finite positive
bounds for this unchanged $W_k$, and GEL/EIQ proves its leading
equilibrium value. WGR1--15 returns that value through the original
kernel, boundary, arithmetic and HC maps. The finite evaluated
enclosures and the exact signed limit are installed below; the
complete WGP1--14/RWB1--27/EIQ1--33/GEL/WGR proof bodies are
included in this source through valid local inputs.'''
s=replace(s,old,new,name,'current_integration_growth')
old=r'''coefficient Gram. These formulas do not assign a leading
value to the universal Hankel determinant ratios.'''
new=r'''coefficient Gram. The entire original product of these two
high ratios with the retained low ratio and D-product is now
evaluated at leading order by GEL18, with its explicit positive
coefficient and complete finite receiving return in GRI1--7 below.'''
s=replace(s,old,new,name,'actual_high_ratio_growth_site')
old='No leading asymptotic value is assigned by this identity.'
new=r'''For this exact product, RWB1--27 and GEL18 now prove
$lq/64\leq W_k\leq6lq$ and
$W_k/(lq)\to\mathcal C_\Gamma>0$, with the unchanged
original moments and parity blocks. GRI1--2 gives the precise
constant and domains; the complete proofs are included below.'''
s=replace(s,old,new,name,'actual_positive_product_growth_site')
anchor=r'\subsection{Return to the original arithmetic criterion}'
s=replace(s,anchor,body+'\n'+anchor,name,'complete_growth_receiving_proof')
old=r'''signed $q\log k$ constants and simple-zero $5/7$ rate
transport to this centre by addition, as proved in WRC7.'''
new=r'''signed $q\log k$ constants and simple-zero $5/7$ rate
transport to this centre by addition, as proved in WRC7.
GRI4 now substitutes the finite RWB bounds into this actual
arithmetic interval, and GRI5 proves the complete signed limit
$\Delta_k^\Gamma/(kq)\to-\mathcal C_\Gamma/4$ in both
original multiplicity branches. The exact current endpoints
remain available; the evaluated interval contains them by GRI3.'''
s=replace(s,old,new,name,'actual_arithmetic_growth_return')
old=r'''The full-source BRD/CTR estimate and LET scalar-source
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
new=r'''The full-source BRD/CTR and LET comparison identifies
\eqref{eq:positive-entire-centre} with $o(q)$ Gamma error.
RWB and GEL now evaluate its actual growth:
$lq/64\leq W_k\leq6lq$ and $W_k/(lq)\to\mathcal C_\Gamma>0$.
The complete EIQ integral specifies the coefficient. GRI5--7
then proves the negative limit of the full Gamma/arithmetic
difference and its necessary relation to the unchanged baseline
and HC residual. The next calculation concerns those original
objects and the finer $q$-scale remainder. The finite WGP13/GEL17b
terms, original low moment and all arithmetic allowances remain;
the proved GEL remainder is $o(lq)$ and is not replaced by $o(q)$.'''
s=replace(s,old,new,name,'current_analytic_continuation')
old=r'''The mixed term in \eqref{eq:freeplusmixed}, however, remains necessary; neither its sign nor its growing-family cancellation has been supplied by the free determinant alone.'''
new=r'''The mixed term in \eqref{eq:freeplusmixed} remains in the exact
return. Its sum with the free contribution now has the evaluated
limit $(R_k^0-R_k^\sigma)/(kq)\to-\mathcal C_\Gamma/4$ by
GEL19 and $l/k\to1/4$. The original source comparison transports
this same limit to $\Delta_k^\Gamma$ in GRI5, using the complete
mixed quotient and boundary maps rather than dropping that term.'''
s=replace(s,old,new,name,'actual_mixed_growth_conclusion')
old=r'''The original arithmetic defect is still present with its
unchanged asymmetric bounds. The next calculation is the
growing-family evaluation of the displayed entire positive
product with all low and high factors retained. No RH endpoint
or leading Hankel value is asserted by this error estimate.'''
new=r'''The original arithmetic defect is still present with its
unchanged asymmetric bounds. The complete growth calculation now
gives the precise positive coefficient $\mathcal C_\Gamma$ for
this entire product and the negative signed limit GRI5.
GRI7 proves the actual baseline and HC difference limits and
the necessary bound $\liminf\mathcal B_k^0/(kq)\geq\mathcal C_\Gamma/4$.
Neither the baseline nor the nonnegative residual is set to zero.
The next calculation keeps those objects and the finite $q$-scale
terms retained in WGP13/GEL17b; no sharper remainder is assumed.'''
s=replace(s,old,new,name,'current_final_mathematical_state')
s=replace(s,r'\end{document}',appendix+'\n'+r'\end{document}',name,'complete_growth_proof_inputs')
docs[name]=s

name='SIGNED_RETURN_RECEIVER.tex';s=docs[name]
old=r'''The complete PHT/HCT providers give its positive moment
and parity-Hankel evaluation without changing this original
expression or assigning it an asymptotic value.'''
new=r'''The complete PHT/HCT providers give its positive moment
and parity-Hankel expression. The complete RWB and GEL/EIQ
proofs now evaluate this exact expression: GRI1--2 below proves
$lq/64\leq W_k\leq6lq$ and
$W_k/(lq)\to\mathcal C_\Gamma>0$ with every original
low moment, D-product and high parity factor retained.'''
s=replace(s,old,new,name,'actual_positive_product_growth_site')
old=r'''is the fully universal centre WRC4 for subsequent growing-
family evaluation; the exact low moment remains an input
to the narrower previous interval.'''
new=r'''is the fully universal centre WRC4, whose growth is now
proved by RWB and GEL and returned in GRI1--7 below.
The exact low moment remains an input to the narrower
previous finite interval.'''
s=replace(s,old,new,name,'actual_universal_centre_growth_site')
old=r'''arithmetic defect. It assigns no asymptotic value to
$H_k^*$ and makes no RH endpoint assertion.'''
new=r'''arithmetic defect. The exact relation $H_k^*=-W_k+e_0$
and the now proved GEL18 limit give
$H_k^*/(lq)\to-\mathcal C_\Gamma$.
GRI4--7 below returns the evaluated finite bounds and
complete signed limit to the same arithmetic and HC objects,
including their necessary baseline relation.'''
s=replace(s,old,new,name,'actual_HC_growth_site')
anchor=r'\section{The finite arithmetic majorant at each original degree}'
s=replace(s,anchor,body+'\n'+anchor,name,'complete_growth_receiving_proof')
old=r'''Gamma result does not improve the arithmetic deficit itself.'''
new=r'''Gamma result does not improve the arithmetic deficit itself.
GRI1 and GRI4 now give the corresponding finite evaluated
arithmetic interval using $w^-_{q,l},w^+_{q,l}$, and GRI5
proves its complete signed growing limit. The exact current
finite endpoints remain unchanged because GRI3 contains
the retained exact-$W_k$ interval.'''
s=replace(s,old,new,name,'actual_arithmetic_growth_return')
old=r'''Thus BHR14 transports the same arithmetic constants to
the explicitly specified Hankel centre with its $o(q)$
Gamma error. Neither formula omits the Gamma return.'''
new=r'''Thus BHR14 transports the same arithmetic constants to
the explicitly specified Hankel centre with its $o(q)$
Gamma error. GEL18 and GRI5 now evaluate the full return:
$\Delta_k^\Gamma/(kq)\to-\mathcal C_\Gamma/4$ on both
original multiplicity branches. Neither formula omits
the Gamma return or changes its arithmetic allowance.'''
s=replace(s,old,new,name,'actual_signed_limit_site')
old=r'''It makes no assertion of an RH endpoint or of a leading
value for the signed Gamma term.'''
new=r'''The full signed Gamma value is now evaluated by GRI5.
GRI6 gives the finite RWB substitution into this same HC
formula, and GRI7 proves the two exact difference limits
and $\liminf\mathcal B_k^0/(kq)\geq\mathcal C_\Gamma/4$.
The original baseline and nonnegative residual remain
present, together with the finite $q$-scale terms and
the proved $o(lq)$ equilibrium remainder.'''
s=replace(s,old,new,name,'actual_final_HC_growth_return')
old=r'''WRC1--7 proves their receiving substitution and exact interval
containment. The companion JSON'''
new=r'''WRC1--7 proves their receiving substitution and exact interval
containment. The complete WGP1--14, RWB1--27, EIQ1--33,
GEL1--19 including GEL17a--b and GEL18a, and WGR1--15
proof bodies are included below. GRI1--7 installs their exact
finite evaluated and asymptotic consequences in this original
receiver, retaining the smaller-scale terms. The companion JSON'''
s=replace(s,old,new,name,'complete_growth_provider_statement')
s=replace(s,r'\end{document}',appendix+'\n'+r'\end{document}',name,'complete_growth_proof_inputs')
docs[name]=s

providers=[]
def copy(src,name,pin=None):
    raw=src.read_bytes()
    if pin:assert sha(raw)==pin,(name,sha(raw))
    dst=HERE/'providers'/name;dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists():assert dst.read_bytes()==raw,(name,'frozen provider')
    else:dst.write_bytes(raw)
    providers.append({'source':str(src),'copy':str(dst.relative_to(HERE)),'sha256':sha(raw),'bytes':len(raw)})
for src in sorted((OLD/'providers').rglob('*')):
    if src.is_file():copy(src,str(src.relative_to(OLD/'providers')))
newproofs=[
 ('original_product_expansion.tex',GROWTH/'original_product_expansion.tex','e6122af0f0cc54028ceee5383c97070e7738d9d8ec1a5bc5481b349761e5fbfe'),
 ('recurrence_bounds.tex',GROWTH/'recurrence_bounds.tex','580f282cb2be5225383da4913dec33810d5482a5d02097ed594173f0bc70b87f'),
 ('EXACT_SQRT_LOG_EQUILIBRIUM.tex',GROWTH/'equilibrium/independent/EXACT_SQRT_LOG_EQUILIBRIUM.tex','a0a0346a19d0e035a186590dbd69881cdf7a30e8fef602d47bba0932f175e731'),
 ('GAMMA_ENSEMBLE_LEADING_RETURN.tex',GROWTH/'equilibrium/GAMMA_ENSEMBLE_LEADING_RETURN.tex','2014e7fefdcd963b70b00fb89d597e24c0826582a2541dd1ff44d63051979fc1'),
 ('signed_growth_receiver.tex',GROWTH/'signed_growth_receiver.tex','9b42c91c8cbc5e8a01aaf130f9d5d5ac3855880bfe85dd72c8ac6add2bfb5479'),
]
for dest,src,pin in newproofs:copy(src,'growth/'+dest,pin)
for src in sorted(GROWTH.glob('REVIEW*.md')):copy(src,'growth/'+src.name)
copy(GROWTH/'equilibrium/FINAL_EQUILIBRIUM_RECEIPT.json','growth/FINAL_EQUILIBRIUM_RECEIPT.json')
copy(GROWTH/'equilibrium/review/INDEPENDENT_GEL_EIQ_REVIEW.md','growth/INDEPENDENT_GEL_EIQ_REVIEW.md','bae8016ce51e71b75fcdd948eec49e437237875fe87acde66597e0bd6e9cdea2')

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
    write(HERE/'predecessors'/(name+'.diff'),''.join(difflib.unified_diff(lf(raw).splitlines(True),s.splitlines(True),fromfile='accepted20/'+name,tofile='current21/'+name)))
    expanded=s
    for target in re.findall(r'\\input\{([^}]+)\}',s):
        path=HERE/target;assert path.is_file(),target
        fragment=lf(path.read_bytes())
        assert not re.search(r'\\(?:documentclass|begin\{document\}|end\{document\})',fragment)
        expanded=expanded.replace(r'\input{'+target+'}',fragment,1)
    oldtags=re.findall(r'\\tag\{([^}]+)\}',lf(raw));newtags=re.findall(r'\\tag\{([^}]+)\}',expanded)
    oldlabels=re.findall(r'\\label\{([^}]+)\}',lf(raw));newlabels=re.findall(r'\\label\{([^}]+)\}',expanded)
    assert all(x in newtags for x in oldtags) and len(newtags)==len(set(newtags)),(name,'tags')
    assert all(x in newlabels for x in oldlabels) and len(newlabels)==len(set(newlabels)),(name,'labels')
    clean=re.sub(r'(?<!\\)%[^\n]*','',expanded);stack=[]
    for kind,env in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
        if kind=='begin':stack.append(env)
        else:assert stack and stack.pop()==env,(name,'environment',env)
    assert not stack and clean.count(r'\[')==clean.count(r'\]')
    assert s.count(body)==1
    rec.update({'successor_sha256':sha((HERE/name).read_bytes()),'bytes':len((HERE/name).read_bytes()),'direct_new_tags':['GRI'+str(i) for i in range(1,8)],'full_new_proof_inputs':[d for d,_,_ in newproofs],'expanded_tag_count':len(newtags)})

for item in old_snapshot:
    raw=(OLD/item['path']).read_bytes()
    assert sha(raw)==item['sha256'] and len(raw)==item['bytes']
receipt={'scope':'Complete current NOTE/JSR successors under growing_w_20260914/receiving only. The entire cut20 receiving tree is cloned unchanged into predecessors/cut20; the original cut20 and all earlier deliveries remain unchanged. No rebuild, PDF, numerical calculation, nested agent or publication.',
 'receivers':records,'changes':changes,'providers':providers,'complete_cut20_predecessor_snapshot':old_snapshot,
 'receiving_application':{'file':'spans/GROWTH_RECEIVING_BODY.tex','tags':'GRI1--7','sha256':sha((HERE/'spans/GROWTH_RECEIVING_BODY.tex').read_bytes()),'embedded_once_in_each_receiver':True},
 'mathematics':'Actual current proof and prose sites now use finite lq/64<=W<=6lq, exact explicit C_Gamma equilibrium limit and DeltaGamma/(kq)->-C_Gamma/4. Finite evaluated arithmetic/HC intervals preserve original asymmetric allowances. The evaluated interval contains the retained exact-W interval, so existing four-entry exact endpoints remain unchanged. WGR15 baseline and residual difference limits and necessary baseline liminf are installed. The GEL o(lq) remainder is not promoted to o(q); WGP13 finite terms remain.',
 'checks':['all final proof-source pins matched','entire cut20 raw-byte snapshot copied and verified unchanged after installation','twelve-plus exact before/after spans reverse to original complete source bytes','every new local proof input exists and is a full input fragment','all prior tags/labels retained and no duplicates after expanding new inputs','ordered TeX environments and display delimiters checked on expanded sources','complete GRI body occurs once in each current receiver'],
 'acceptance':'All five provider proofs already fully root and independently accepted at the copied pins. This bounded source integration constructs their receiving substitution; no new audit layer or compilation is performed.'}
receipt['checks'][2]=f"{len(changes)} exact before/after spans reverse to original complete source bytes"
write(HERE/'FULL_RECEIVING_RECEIPT.json',json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receivers':records,'application':receipt['receiving_application'],'changes':len(changes),'providers':len(providers),'cut20_files_preserved':len(old_snapshot),'receipt_sha256':sha((HERE/'FULL_RECEIVING_RECEIPT.json').read_bytes())},indent=2))
