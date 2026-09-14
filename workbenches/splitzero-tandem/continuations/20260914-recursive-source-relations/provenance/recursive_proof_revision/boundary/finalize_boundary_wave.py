from pathlib import Path
import hashlib,json,difflib

ROOT=Path(r'workspace:')
OUT=ROOT/'work/backpropagation_20260913/boundary'
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return p.read_text(encoding='utf-8-sig').replace('\r\n','\n')
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(s.encode('utf-8'))
manifest=json.loads(read(OUT/'PATCH_MANIFEST.json'))
pins={
 'tensor_primary_update.tex':'b3493b70b40ce3e0691e8aa974748f166e8b8e23ac723c4a929011e0e66845f7',
 'PC30_coefficient_insertion.tex':'2035d2e0553d0019f2090c0395e87388f48366cabd8f059b651e6e83d61a07a2',
 'single_primary_conclusion_update.tex':'00270df74a5e4cccb8b8bb78928a2299483688e2ffb0a5e571d0b5bafce6f16b'}
for name,pin in pins.items():assert sha((OUT/'fragments'/name).read_bytes())==pin

# Direct insertion into the original PC30 proof neighborhood.
pc=OUT/'revised/tex/period_critical_kernel_bridge.tex'
s=read(pc);anchor=r'Let $\chi_{c,k}$ be the same polynomial formed using only tuples'
assert s.count(anchor)==1
if r'\label{eq:pc30a-update}' not in s:
 s=s.replace(anchor,read(OUT/'fragments/PC30_coefficient_insertion.tex')+'\n\n'+anchor)
write(pc,s)

# Complete tensor proofs are a source dependency of those earlier insertions.
tensor_current='tex/tensor_primary_boundary_backpropagation.tex'
tensor_body=read(OUT/'fragments/tensor_primary_update.tex')
write(OUT/'revised'/tensor_current,'\\begingroup\n\\section{Original cyclic coefficients and the tensor boundary maps}\n'+tensor_body+'\n\\endgroup\n')

# Replace the previously future tensor calculation in the current BC body.
bc=OUT/'revised/tex/marked_product_boundary_connection.tex'
s=read(bc)
start=s.index('For several distinct primary critical values, the remaining')
end=s.index('The continuing induced relation-form calculation',start)
prefix='For several distinct primary critical values, the continuing calculation\nincludes the sector transitions and local extensions between the computed\nblocks, with their exact maps through the retained mixed faces.  The\nsingle-primary tensor calculation now gives the following complete\ncontinuation on the original parameter line.\n\n'
if r'\label{eq:spbt1}' not in s:
 s=s[:start]+prefix+read(OUT/'fragments/single_primary_conclusion_update.tex')+'\n\n'+s[end:]
s=s.replace('The exact single-primary branch now also includes its full period\nmatrix, boundary monodromy, finite cover, source-unit maps and finite-field\ncharacter decomposition.', 'The exact single-primary branch now includes its full period matrix,\nboundary monodromy, finite cover, source-unit maps and finite-field\ncharacter decomposition through every ordered tensor degree, together\nwith the exact original coefficient lattice and its specialization maps.')
write(bc,s)
bc_src=ROOT/'work/marked_product_boundary_connection_20260913.tex'
(OUT/'originals/tex/marked_product_boundary_connection.tex').write_bytes(bc_src.read_bytes())
body=s[s.index('\\maketitle')+len('\\maketitle'):s.rindex('\\end{document}')]
macros=r'''
\begingroup
\def\Tr{\operatorname{Tr}}\def\coker{\operatorname{coker}}
\def\Spec{\operatorname{Spec}}\def\rem{\operatorname{rem}}
\def\diag{\operatorname{diag}}\def\C{\mathbb C}\def\F{\mathbb F}
\def\A{\mathbb A}\def\Gm{{\mathbb G_m}}\def\HH{\mathcal H}\def\BB{\mathscr B}
'''
write(OUT/'proofs/BC_CURRENT_FRAGMENT.tex',macros+body+'\n\\endgroup\n')

# Exact compiled AP wrapper mapping: heading depth and literal provenance URLs.
ap_route='sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex'
wrapper_src=ROOT/'work/backpropagation_20260913/typesetting_v21/originals/tex/actual_tau_analytic_pole_complete.tex'
wrapper_bytes=wrapper_src.read_bytes()
assert sha(wrapper_bytes)=='9b8d347629143b6c5347d5385789dbd89f96b80aa4cc1da55a24300edaa2dd13'
w=read(wrapper_src);ap_old=read(OUT/'originals'/ap_route);ap_new=read(OUT/'revised'/ap_route)
start=w.index('\\subsubsection{Actual Taylor-unit')
end=w.rindex('\\endgroup');end=w.rindex('\\endgroup',0,end)
old_wrapped=w[start:end].strip()
def presentation(x):
 x=x.replace(r'\subsection{Actual Taylor-unit',r'\subsubsection{Actual Taylor-unit',1)
 x=x.replace(r'ACTUAL\_TAYLOR\_UNIT\_FORMAL\_GAUGE.md',r'\nolinkurl{ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md}')
 x=x.replace(r'../f1\_scaling\_frobenius/ACTUAL\_TAU\_SCALING\_AND\_EXPONENTIAL\_FLOW.md',r'\nolinkurl{../f1_scaling_frobenius/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW.md}')
 for pin in ['9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f','4e4cb66e3cbbff6379ae389ddaaad65045ac0ed380f17a87ac7c4241c45e6c08']:
  x=x.replace('SHA256 '+pin,'SHA256 \\nolinkurl{'+pin+'}')
 return x.strip()
assert presentation(ap_old)==old_wrapped
revision_note=r'''\noindent\textbf{Current mathematical continuation.} APU1--23 below are inserted into the complete original proof at the AP13--AP14 transition. Their source is \path{sources/current_boundary/fragments/analytic_pole_u_connection.tex}, SHA-256 \nolinkurl{1b42c530ccee6fd019b8536170277e3909ba43bfe4e3b2fefab3f7b9fc666c05}. The preceding source record identifies the preserved historical body; the exact current body and reversible wrapper mapping are pinned by the boundary patch manifest.\par\medskip
'''
new_w=w[:start]+revision_note+presentation(ap_new)+'\n\n'+w[end:]
wrapper_route='tex/actual_tau_analytic_pole_complete.tex'
(OUT/'originals'/wrapper_route).write_bytes(wrapper_bytes)
write(OUT/'revised'/wrapper_route,new_w)
mapping={'original_wrapper':str(wrapper_src),'original_wrapper_sha256':sha(wrapper_bytes),'original_body_route':ap_route,'original_body_sha256':sha((OUT/'originals'/ap_route).read_bytes()),'new_body_sha256':sha((OUT/'revised'/ap_route).read_bytes()),'new_wrapper_route':wrapper_route,'new_wrapper_sha256':sha((OUT/'revised'/wrapper_route).read_bytes()),'mapping':'Exact original inner body equals source after first heading subsection->subsubsection and four provenance token->nolinkurl changes. The identical presentation function is applied to the complete revised body. Historical wrapper prefix/suffix preserved; current continuation provenance inserted before body.','original_inner_body_equality_pass':True}
write(OUT/'AP_WRAPPER_MAPPING.json',json.dumps(mapping,indent=2)+'\n')

def add_record(source,route,changes):
 manifest['records']=[r for r in manifest['records'] if r.get('revised')!='revised/'+route]
 manifest['records'].append({'source':str(source),'original_sha256':sha(source.read_bytes()),'revised':'revised/'+route,'revised_sha256':sha((OUT/'revised'/route).read_bytes()),'changes':changes})
add_record(bc_src,'tex/marked_product_boundary_connection.tex',['Replace future single-primary boundary work with full SPC proofs and SPBT1--3 tensor continuation; retain complete original BC source'])
add_record(OUT/'fragments/tensor_primary_update.tex',tensor_current,['Complete BPC1--14, BTP1--11 and BTF1--11 companion proofs used by PC30 and the current boundary conclusion'])
add_record(wrapper_src,wrapper_route,['Active compiled AP route: exact reversible inner-body mapping; APU1--23 inserted at AP13--AP14 with full proofs'])
tp=ROOT/'work/rh_counterfactual_20260913/total_object/tensor_primary_boundary_control.tex'
manifest['records']=[r for r in manifest['records'] if r.get('proof')!='TP']
manifest['records'].append({'proof':'TP','source':str(tp),'sha256':sha(tp.read_bytes()),'copied':'proofs/TENSOR_ORIGINAL.tex'})
for rec in manifest['records']:
 if 'revised' in rec:
  current=OUT/rec['revised'];rec['revised_sha256']=sha(current.read_bytes())
  src=Path(rec['source']);assert sha(src.read_bytes())==rec['original_sha256']
  if current.name=='period_critical_kernel_bridge.tex':
   rec['changes']=['PC.u1--u3: exact u derivative and critical-kernel curvature','PC30a--g: full original factorial lattice, specialized kernel, exact residual-collision polynomial and image at the earlier PC30 proof site']
  if current.name=='sga_constituent_period_curvature.tex':
   rec['changes']=['SC.u1--u7: full u/mixed curvature and original source metric; exact single-primary ideal determinants with all frame/Gamma constants and proved zero u-normal curvature']
  original=read(src);new=read(current)
  write(OUT/'evidence'/f'{current.name}.diff',''.join(difflib.unified_diff(original.splitlines(True),new.splitlines(True),fromfile=str(src),tofile=rec['revised'])))
 else:
  assert sha(Path(rec['source']).read_bytes())==rec['sha256']
  assert sha((OUT/rec['copied']).read_bytes())==rec['sha256']
manifest['final_byte_hashes']=True
manifest['active_ap_route']=wrapper_route
manifest['proof_companion_route']=tensor_current
manifest['current_bc_fragment']='proofs/BC_CURRENT_FRAGMENT.tex'
write(OUT/'PATCH_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')

master=read(OUT/'BOUNDARY_VERIFICATION.tex')
master=master.replace('\\input{revised/'+ap_route+'}','\\input{revised/'+wrapper_route+'}')
inclusion='\\input{revised/'+tensor_current+'}\n'
if inclusion not in master:master=master.replace('\\input{proofs/BC_CURRENT_FRAGMENT.tex}',inclusion+'\\input{proofs/BC_CURRENT_FRAGMENT.tex}')
write(OUT/'BOUNDARY_VERIFICATION.tex',master)
print(json.dumps({'records':len(manifest['records']),'active_ap_sha256':mapping['new_wrapper_sha256'],'pc_current_sha256':sha(pc.read_bytes()),'bc_current_sha256':sha(bc.read_bytes()),'complete_companion_sha256':sha((OUT/'revised'/tensor_current).read_bytes()),'historical_sources_unchanged':True},indent=2))
