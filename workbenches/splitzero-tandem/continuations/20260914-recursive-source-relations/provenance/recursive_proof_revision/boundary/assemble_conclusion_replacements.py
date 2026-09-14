from pathlib import Path
import re,json,hashlib
ROOT=Path(r'workspace:')
OUT=ROOT/'work/backpropagation_20260913/boundary'
def read(p):return p.read_text(encoding='utf-8-sig').replace('\r\n','\n')
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(s.encode('utf-8'))
frag=OUT/'fragments/research_conclusion_boundary_updates.tex'
s=read(frag)
s=s.replace(r'\nquotient','\nquotient').replace(r'\nits product','\nits product').replace(r'\nThe last arrow','\nThe last arrow')
s=s.replace('The kernel is zero when \\(D<p\\).','The kernel is zero when \\(D<p\\).')
s=s.replace('When the specified map includes all one-factor CRT\n+data,', 'When the specified map includes all one-factor CRT\ndata,')
s=s.replace('When the specified map includes all one-factor CRT\ndata, (PC30f)', 'When the specified map includes all one-factor CRT\ndata and \\(p>m_\\rho\\) for every retained primary order, (PC30f)')
s=s.replace('The last arrow is the proved module map','The last arrow is the proved module map')
write(frag,s)
fragments={}
for source in [frag,OUT/'fragments/actual_geometry_boundary_updates.tex']:
 for key,body in re.findall(r'% BEGIN RCB:([A-Z0-9_]+)\n(.*?)\n% END RCB:\1',read(source),re.S):
  assert key not in fragments;fragments[key]=body
sources={
 'research_conclusion':ROOT/'work/cumulative_next_edition_staging_20260913_v19/reader/tex/research_conclusion.tex',
 'actual_geometry':ROOT/'work/tau_actual_geometry_current_results_20260913.tex'}
records=[];proofview=[]
for lane,ids in [('research_conclusion',[51,52,56,57,59,62]),('actual_geometry',[68,69,70,71])]:
 src=sources[lane];text=read(src)
 for n in ids:
  match=re.search(r'\\paragraph\{Result R'+str(n)+r':.*?(?=\\paragraph\{Result R|\Z)',text,re.S)
  assert match
  old=match.group(0);new=old
  if n==51:
   title=new[:new.index('\n')]
   new=new.replace(title,fragments['R51_TITLE'],1)
  else:
   if n==52:
    old_phase='finite-field realization tensors the corresponding constant\nArtin--Schreier character line.'
    new_phase=r'''finite-field realization retains the character sheaf
\(\mathcal L_\psi((-\Phi(-a)-ta)/u)\) on the original
\((u,t)\)-base; its point restriction is the stated constant
character line. The complete derived direct-image map and
its projections are proved in (DT.14)--(DT.16).'''
    assert new.count(old_phase)==1
    new=new.replace(old_phase,new_phase)
   if n==62:
    old_translation='The exact Pascal translation preserves\nthese derivatives of order at least two while its scalar factor\nretains the first-derivative trace shift $2p\\operatorname{Re}a$.'
    assert new.count(old_translation)==1
    new=new.replace(old_translation,fragments['R62_TRANSLATION_REPLACEMENT'])
   new=new.rstrip()+'\n\n'+fragments[f'R{n}_CONTINUATION']+'\n\n'
  rec={'result':f'R{n}','source':str(src),'source_sha256':sha(src.read_bytes()),
       'original_start_line':text[:match.start()].count('\n')+1,
       'original_end_line':text[:match.end()].count('\n')+1,
       'operation':'replace_exact_original_result_block','old':old,'new':new,
       'old_sha256_utf8_lf':sha(old.encode()),'new_sha256_utf8_lf':sha(new.encode()),
       'scope':'Preserve every original result proof paragraph and append its exact current connection maps; R51 title, R52 family character wording and R62 derivative-domain wording receive literal precision corrections.'}
  records.append(rec);proofview.append(new)
out={'schema':'boundary-current-result-replacements-v1','historical_sources_modified':False,
     'source_documents':[{'path':str(v),'sha256':sha(v.read_bytes())} for v in sources.values()],
     'records':records,
     'fragments':[{'path':str(p),'sha256':sha(p.read_bytes())} for p in [frag,OUT/'fragments/actual_geometry_boundary_updates.tex']],
     'parent_merge':'Apply each exact old block once to the full current result text; preserve all other lanes. If a current block differs, compare against the recorded source and merge its preserved body with this continuation instead of replacing other changes.'}
write(OUT/'CONCLUSION_REPLACEMENTS.json',json.dumps(out,ensure_ascii=False,indent=2)+'\n')
write(OUT/'fragments/COMPLETE_CURRENT_RESULT_REPLACEMENTS.tex','\n'.join(proofview))
master=read(OUT/'BOUNDARY_VERIFICATION.tex')
master=master[:master.index('\\input{revised/tex/deligne_split_sidebar.tex}')]+r'\input{fragments/COMPLETE_CURRENT_RESULT_REPLACEMENTS.tex}'+'\n\\end{document}\n'
write(OUT/'CURRENT_RESULTS_VERIFICATION.tex',master)
print(json.dumps({'records':len(records),'json_sha256':sha((OUT/'CONCLUSION_REPLACEMENTS.json').read_bytes()),'full_replacement_tex_sha256':sha((OUT/'fragments/COMPLETE_CURRENT_RESULT_REPLACEMENTS.tex').read_bytes())},indent=2))
