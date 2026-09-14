"""Five exact display-line transports for the cumulative article geometry."""
from pathlib import Path
import json, shutil
from prepare_successor import STAGE,sha,row,save

changes=[
('tex/phase_graph_v2/dep01.tex',r''' \mathsf F=\mathsf S G^{-1/2},\quad \mathsf F^*\mathsf F=I_d,\quad
 J_0=G^{-1/2}JG^{-1/2},\quad X=A I_d+iJ_0,\quad
 C_0=G^{1/2}CG^{-1/2},\quad L=X-C_0.''',r''' \begin{gathered}
 \mathsf F=\mathsf S G^{-1/2},\quad \mathsf F^*\mathsf F=I_d,\\
 J_0=G^{-1/2}JG^{-1/2},\quad X=A I_d+iJ_0,\\
 C_0=G^{1/2}CG^{-1/2},\quad L=X-C_0.
 \end{gathered}'''),
('tex/phase_graph_v2/dep08.tex',r''' \left(\frac{\omega_{h,k,n+r}}{\omega_{h,k,n}}\right)^{1/(2r)}
 \le\left[
 \frac{(2(n+r))!b^{-2(n+r)}(M_h(b)^k+M_h(-b)^k)
       e^{\alpha_0(L+k-3)}(1+L+k-3)^{B_h}}
      {c_h\vartheta_h^{k-3}\mathfrak l_n(L)}
       \right]^{1/(2r)}.''',r''' \begin{gathered}
 \left(\frac{\omega_{h,k,n+r}}{\omega_{h,k,n}}\right)^{1/(2r)}\\
 \le\left[
 \frac{(2(n+r))!b^{-2(n+r)}(M_h(b)^k+M_h(-b)^k)
       e^{\alpha_0(L+k-3)}(1+L+k-3)^{B_h}}
      {c_h\vartheta_h^{k-3}\mathfrak l_n(L)}
       \right]^{1/(2r)}.
 \end{gathered}'''),
('tex/phase_graph_v2/RMT.tex',r''' \mathscr H_a(B)=2\operatorname{arcosh}(e^{B/(2a)}),\qquad
 \mathscr H_a'(B)=
 \frac{1}{a\sqrt{1-e^{-B/a}}},\qquad
 \mathscr H_a^{-1}(z)=2a\log\cosh(z/2)\quad(z>0).''',r''' \begin{gathered}
 \mathscr H_a(B)=2\operatorname{arcosh}(e^{B/(2a)}),\qquad
 \mathscr H_a'(B)=
 \frac{1}{a\sqrt{1-e^{-B/a}}},\\
 \mathscr H_a^{-1}(z)=2a\log\cosh(z/2)\quad(z>0).
 \end{gathered}'''),
('tex/phase_graph_v2/PGD.tex',r''' \boxed{\quad
 c_kM_N\preceq W_N\preceq(c_k+E_{k,N})M_N,\qquad
 c_k=1+k^2A^2,\quad
 E_{k,N}=\frac{k^2F_kL_ND_N}{a_k},\quad k\geq3, N\geq0.
 \quad}''',r''' \boxed{\begin{gathered}
 c_kM_N\preceq W_N\preceq(c_k+E_{k,N})M_N,\\
 c_k=1+k^2A^2,\quad
 E_{k,N}=\frac{k^2F_kL_ND_N}{a_k},\\
 k\geq3, N\geq0.
 \end{gathered}}'''),
('tex/research_conclusion.tex',r'''                                    \right\|^2,
 \quad Z_{2q}^{\rm mix}=(D_{\rm mix},f_{2q}).''',r'''                                    \right\|^2,\\
 &\quad Z_{2q}^{\rm mix}=(D_{\rm mix},f_{2q}).'''),
]

pdf=STAGE/'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
pin=sha(pdf)
if pin!='932c9c30bddb06f6b40e9d3b7019c4ffa153feb6f950652dd491912b228121e7':
    raise RuntimeError('Unexpected first cumulative candidate PDF.')
history=STAGE/'history/cumulative_build_candidates'/pin
for path in [pdf,*[p for p in (STAGE/'build').glob('*') if p.is_file() and (p.name.startswith('reader.') or p.name.startswith('current-xelatex-') or p.name.endswith('BUILD_RECEIPT.json'))],STAGE/'provenance/CURRENT_COMPILED_SOURCE_PINS.json',STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json']:
    target=history/path.relative_to(STAGE); target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(path,target)
transport=[]
for relative,old,new in changes:
    path=STAGE/relative; text=path.read_text(encoding='utf-8')
    if text.count(old)!=1: raise RuntimeError('Display target is not unique: '+relative)
    target=history/relative; target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(path,target)
    revised=text.replace(old,new)
    if revised.replace(new,old)!=text: raise RuntimeError('Display transport failed exact inverse.')
    path.write_text(revised,encoding='utf-8',newline='\n')
    transport.append({'path':relative,'before':row(target),'after':row(path),'old':old,'new':new,'count':1,'inverse_replay':'entire preceding source identical'})
expected_path=STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json'
expected=json.loads(expected_path.read_text(encoding='utf-8'))
for relative,old,new in changes: expected['files'][relative]=row(STAGE/relative)
save(expected_path,expected)
save(STAGE/'provenance/ARTICLE_DISPLAY_WIDTH_TRANSPORTS.json',{
    'status':'five_exact_display_line_transports','candidate_pdf_sha256':pin,
    'formula_changes':0,'tag_changes':0,'operations':transport,
    'reason':'Retain all mathematical tokens within the predecessor article width.'})
print(json.dumps({'status':'five_display_transports_verified','expected_source_manifest_sha256':sha(expected_path)}))
