from pathlib import Path
import hashlib,json,difflib
ROOT=Path(r'workspace:')
OUT=ROOT/'work/backpropagation_20260913/boundary'
def sha(b):return hashlib.sha256(b).hexdigest()
def norm(s):return s.replace('\r\n','\n')
route='sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex'
src=ROOT/'work/cumulative_actual_tau_draft_inputs_20260913_v21/source_snapshot'/route
old=src.read_bytes();assert sha(old)=='b15d25864e0c298478947e2e67e4642bb1b007cccd08b6db21ec4bac740ce221'
original=norm(old.decode('utf-8-sig'))
fragment=(OUT/'fragments/analytic_pole_u_connection.tex').read_bytes()
assert sha(fragment)=='1b42c530ccee6fd019b8536170277e3909ba43bfe4e3b2fefab3f7b9fc666c05'
body=norm(fragment.decode('utf-8-sig'))
needle=r'\subsubsection{5. Entire finite scaling and its retained extension term}'
assert original.count(needle)==1
revised=original.replace(needle,body+'\n\n'+needle)
oldscope='Completed scope: the original arithmetic polynomial cohomology injects into the analytic localization; all additional pole periods, their connection, finite scaling, unit-gauge image and linear dual are calculated.'
newscope='Completed scope: the original arithmetic polynomial cohomology injects into the analytic localization. The complete two-parameter connection, weighted-residue and oriented-loop maps, finite-scaling pullback including its shifted endpoint derivative, full Taylor gauge, dual and original theta-source endpoint have now been proved in APU1--23. All original additional pole classes and their finite-scaling extension integral remain in the same maps.'
assert revised.count(oldscope)==1
revised=revised.replace(oldscope,newscope)
for bucket in ['originals','revised']:(OUT/bucket/route).parent.mkdir(parents=True,exist_ok=True)
(OUT/'originals'/route).write_bytes(old)
(OUT/'revised'/route).write_text(revised,encoding='utf-8')
(OUT/'evidence/analytic_pole.diff').write_text(''.join(difflib.unified_diff(original.splitlines(True),revised.splitlines(True),fromfile='originals/'+route,tofile='revised/'+route)),encoding='utf-8')
manifest=json.loads((OUT/'PATCH_MANIFEST.json').read_text(encoding='utf-8'))
manifest['records']=[r for r in manifest['records'] if r.get('revised')!='revised/'+route]
manifest['records'].append(dict(source=str(src),original_sha256=sha(old),revised='revised/'+route,revised_sha256=sha((OUT/'revised'/route).read_bytes()),changes=['APU1--23: full u connection propagated through old rational-pole residue, loops, finite scaling, gauge, dual and theta endpoint']))
(OUT/'PATCH_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
master=OUT/'BOUNDARY_VERIFICATION.tex'
s=master.read_text(encoding='utf-8');line='\\input{revised/'+route+'}\n'
if line not in s:s=s.replace('\\input{proofs/BC_CURRENT_FRAGMENT.tex}',line+'\\input{proofs/BC_CURRENT_FRAGMENT.tex}')
master.write_text(s,encoding='utf-8')
print(json.dumps(dict(ap_current=str(OUT/'revised'/route),sha256=sha((OUT/'revised'/route).read_bytes())),indent=2))
