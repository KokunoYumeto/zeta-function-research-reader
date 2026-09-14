"""Reflow five complete boundary displays without altering any content token."""
from pathlib import Path
import re,json,hashlib
ROOT=Path(__file__).resolve().parent
ACTIVE=ROOT.parents[1]/'cumulative_source_v1'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def content_tokens(s):
    # Alignment controls, line breaks and explicit spacing are presentation
    # only. All ordinary commands, braces, numbers, words, signs and matrix
    # entries remain in their original order.
    s=s.replace(r'\begin{aligned}','').replace(r'\end{aligned}','')
    s=s.replace('\\\\','').replace('&','')
    s=re.sub(r'\\(?:qquad|quad)\b','',s)
    return re.findall(r'\\[A-Za-z@]+|\\[\s\S]|[A-Za-z0-9]+|[^\s]',s)

specs=[
('sga_constituent_period_curvature.tex','SC.u5',r'''
 \begin{aligned}
 \Pi_s&=e^{c/u}WD(u)P,\quad
 W_{jb}=e^{2\pi i j(b+1)/n}-1,\\
 D(u)_{bb}&=d_bu^{\beta_b},\quad
 \beta_b=(b+1)/n,\quad
 d_b=n^{\beta_b-1}e^{\pi i\beta_b}\Gamma(\beta_b).
 \end{aligned}
 \tag{SC.u5}
'''),
('period_laplacian_control_bridge.tex','LC.u1',r'''
 \begin{aligned}
 \partial_u\widetilde G&=-\Pi^{-*}G\Omega_u\Pi^{-1},\qquad
 \partial_{\bar u}\widetilde G=-\Pi^{-*}\Omega_u^*G\Pi^{-1},\\
 \partial_u\widetilde L_t&=\Pi[\Omega_u,L_t]\Pi^{-1},
 \quad
 \partial_u\widetilde A_t=\Pi[\Omega_u,A_t]\Pi^{-1}.
 \end{aligned}
 \tag{LC.u1}
'''),
('circle_critical_observation_diamond.tex','DC32',r'''
 \begin{aligned}
 H_b^{\rm obs}&=\Pi^{-*}T_b^*D_\nu T_b\Pi^{-1},
 \quad\ker H_b^{\rm obs}=\Pi K_b,\\
 \partial_uH_b^{\rm obs}
       &=-\Pi^{-*}T_b^*D_\nu T_b\Omega_u\Pi^{-1},\\
 \partial_{\bar u}H_b^{\rm obs}
       &=-\Pi^{-*}\Omega_u^*T_b^*D_\nu T_b\Pi^{-1}.
 \end{aligned}
 \tag{DC32}
'''),
('actual_tau_analytic_pole_complete.tex','APU9',r'''
 \boxed{\displaystyle
 \begin{aligned}
 \nabla_u&=\partial_u+\Omega_u,\qquad
 \Omega_u=
 \begin{bmatrix}
 -C(t)/u^2+B(t)/u&-Q(t)/u^2\\
 0&-F(t)/u^2
 \end{bmatrix},\\
 \nabla_t&=\partial_t+\Omega_t,\qquad
 \Omega_t=-\frac1u
 \begin{bmatrix}A(t)&B_0\\0&P\end{bmatrix}.
 \end{aligned}}
 \tag{APU9}
'''),
('marked_product_boundary_connection.tex',None,r'''
 \begin{aligned}
 n&=m+1,\qquad h(s)=(s-\rho)^m,\qquad
 y=s-\rho,\\
 \Phi_h(s)&=\frac{(s-\rho)^n-(-\rho)^n}{n}
          =\frac{y^n}{n}+c,\qquad
 c=-\frac{(-\rho)^n}{n}.
 \end{aligned}
''')]

records=[];before_parts=[];after_parts=[]
for filename,tag,new_inner in specs:
    p=ACTIVE/'tex'/filename
    raw=p.read_bytes();text=raw.decode('utf-8')
    if tag:
        marker=r'\tag{'+tag+'}'
        assert text.count(marker)==1
        mid=text.index(marker)
    else:
        marker=r'n=m+1,\qquad h(s)=(s-\rho)^m'
        assert text.count(marker)==1
        mid=text.index(marker)
    start=text.rfind(r'\[',0,mid);end=text.index(r'\]',mid)+2
    old=text[start:end]
    new=r'\['+new_inner+r'\]'
    if '\r\n' in text:new=new.replace('\n','\r\n')
    assert content_tokens(old)==content_tokens(new),(filename,'display content token change')
    # Every complete matrix must remain byte-for-byte identical up to the
    # original line-ending presentation; adding outer alignment cannot change
    # the original matrix row/column positions.
    matrix=re.compile(r'\\begin\{bmatrix\}.*?\\end\{bmatrix\}',re.S)
    old_m=[x.replace('\r\n','\n') for x in matrix.findall(old)]
    new_m=[x.replace('\r\n','\n') for x in matrix.findall(new)]
    assert old_m==new_m,(filename,'matrix row or column changed')
    changed=text[:start]+new+text[end:]
    assert changed.count(new)==1
    assert changed.replace(new,old,1).encode('utf-8')==raw
    assert content_tokens(text)==content_tokens(changed)
    before=ROOT/'before'/filename;after=ROOT/'after'/filename
    before.parent.mkdir(parents=True,exist_ok=True);after.parent.mkdir(parents=True,exist_ok=True)
    assert not before.exists() or before.read_bytes()==raw,'Historical overlay pin changed'
    before.write_bytes(raw);after.write_bytes(changed.encode('utf-8'))
    title=filename.replace('_',r'\_')
    local_before=(r'\begingroup\small'+'\n') if filename=='actual_tau_analytic_pole_complete.tex' else ''
    local_after=(r'\endgroup'+'\n') if local_before else ''
    before_parts.append(r'\subsection*{'+title+'}\n'+local_before+old+'\n'+local_after)
    after_parts.append(r'\subsection*{'+title+'}\n'+local_before+new+'\n'+local_after)
    records.append({'active_path':str(p),'before':pin(before),'after':pin(after),
        'old_display':old,'new_display':new,'exact_byte_inverse':True,
        'all_nonpresentation_tokens_identical':True,'complete_matrix_contents_and_row_column_separators_identical':True,
        'display_token_count':len(content_tokens(old)),'complete_source_token_count':len(content_tokens(text)),
        'display_tag':tag,'scratch_retained_local_context':local_before,
        'method':'Add outer aligned environment and line/column presentation controls; retain all original content in original order.'})
preamble=(ACTIVE/'tex/main.tex').read_bytes().decode('utf-8').split(r'\begin{document}',1)[0]
(ROOT/'ACTIVE_PREAMBLE_SNAPSHOT.tex').write_bytes(preamble.encode('utf-8'))
for name,parts in [('before',before_parts),('after',after_parts)]:
    doc=preamble+r'\begin{document}'+'\n'+r'\section*{Five boundary display preservation checks}'+'\n'+'\n'.join(parts)+r'\end{document}'+'\n'
    (ROOT/(name+'.tex')).write_bytes(doc.encode('utf-8'))
(ROOT/'OVERLAY_PROPOSALS.json').write_text(json.dumps({'scope':'Only the five assigned active cumulative boundary copies; original owner sources untouched.',
    'records':records,'all_exact_inverses':True,'all_matrix_row_column_data_identical':True,
    'active_files_modified':False,'preamble_snapshot':pin(ROOT/'ACTIVE_PREAMBLE_SNAPSHOT.tex')},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'overlay_count':len(records),'exact_inverses':True,'all_nonpresentation_tokens_identical':True,'matrix_row_column_data_identical':True,'active_files_modified':False}))
