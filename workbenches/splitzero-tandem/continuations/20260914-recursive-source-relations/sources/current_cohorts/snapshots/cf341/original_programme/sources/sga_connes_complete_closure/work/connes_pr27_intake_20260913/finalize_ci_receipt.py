"""Analyze recorded CI evidence; never executes Lean or changes repo bytes."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
E=ROOT/'evidence'
O=ROOT/'finite_output'
manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
head=manifest['head']; base=manifest['base']
merge='59b5aadebcf91350430c0eba30ae6bae4087738d'
head_commit=json.loads((E/('commit_'+head+'.json')).read_text(encoding='utf-8'))
merge_commit=json.loads((E/('commit_'+merge+'.json')).read_text(encoding='utf-8'))
if head_commit['tree']['sha'] != merge_commit['tree']['sha']:
    raise RuntimeError('merge tree differs')
tree_hash_checks=[]
for label in ['head','base']:
    data=json.loads((E/(label+'_tree.json')).read_text(encoding='utf-8'))
    children={}
    expected={'':manifest[label+'_tree']}
    for item in data['tree']:
        parent,_,name=item['path'].rpartition('/')
        children.setdefault(parent,[]).append((name,item))
        if item['type']=='tree': expected[item['path']]=item['sha']
    for path,items in children.items():
        items.sort(key=lambda pair:(pair[0]+('/' if pair[1]['type']=='tree' else '')).encode('utf-8'))
        raw=b''.join((item['mode'].lstrip('0')+' '+name).encode('utf-8')+b'\0'+bytes.fromhex(item['sha']) for name,item in items)
        actual=hashlib.sha1(b'tree '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if actual!=expected[path]: raise RuntimeError('Git tree hash mismatch: '+label+' '+path)
    tree_hash_checks.append({'revision':label,'root_tree':expected[''],'recomputed_tree_nodes':len(children),'valid':True})
expected_files={f['filename']:f['sha'] for f in json.loads((E/'compare.json').read_text(encoding='utf-8'))['files']}
if len(expected_files)!=16 or len(manifest['tree_diff'])!=16 or any(x['status']!='added' for x in manifest['tree_diff']):
    raise RuntimeError('tree scope mismatch')
if expected_files != {x['path']:x['head_blob'] for x in manifest['tree_diff']}:
    raise RuntimeError('compare and tree differ')
run_data=json.loads((E/'current_head_runs.json').read_text(encoding='utf-8'))
runs=[]
for r in run_data['workflow_runs']:
    jobs=json.loads((E/('jobs_'+str(r['id'])+'.json')).read_text())['jobs']
    runs.append({k:r[k] for k in ['id','name','event','head_sha','status','conclusion','path','html_url']} | {'jobs':[{'id':j['id'],'name':j['name'],'conclusion':j['conclusion'],'completed_at':j['completed_at'],'steps':[{'name':s['name'],'conclusion':s['conclusion']} for s in j['steps']]} for j in jobs]})
    if r['head_sha']!=head or r['conclusion']!='success' or any(j['conclusion']!='success' for j in jobs):
        raise RuntimeError('CI not green exact head')
audits=[]
for job,checkout in [('103666603149',merge),('103666609598',head)]:
    log=(E/('job_'+job+'.full.log')).read_text()
    clean=re.sub(r'^\d{4}-\d{2}-\d{2}T\S+\s?','',log,flags=re.M)
    if '\n'+checkout+'\n' not in clean:
        raise RuntimeError('actual checkout evidence missing')
    records=re.findall(r"^'([^']+)' depends on axioms: \[([^\]]*)\]$",clean,flags=re.M)
    if len(records)!=71 or len({n for n,_ in records})!=71:
        raise RuntimeError('71 exact audit records required')
    declarations={n:[x.strip() for x in values.split(',') if x.strip()] for n,values in records}
    if any(not set(a)<={'propext','Classical.choice','Quot.sound'} for a in declarations.values()):
        raise RuntimeError('unexpected axiom')
    for label,lean_file,script,prefixes in [
        ('restriction','AuditRestrictionCertificate.lean','check_restriction.py',('SplitZero.Restriction.','SplitZero.RestrictionLog.')),
        ('spectrum','AuditRestrictionSpectrum.lean','check_spectrum_audit.py',('SplitZero.RestrictionSpectrum.',)),
    ]:
        expected=set(re.findall(r'^#print axioms (\S+)',(ROOT/'source/formal/splitzero'/lean_file).read_text(),flags=re.M))
        selected={n:v for n,v in declarations.items() if n.startswith(prefixes)}
        if set(selected)!=expected:
            raise RuntimeError('inherited audit exact target mismatch')
        path=O/(job+'.'+label+'.audit.log')
        path.write_text('\n'.join("'%s' depends on axioms: [%s]"%(n,', '.join(a)) for n,a in selected.items())+'\n')
        arguments=[str(ROOT/'source/workbenches/tau-restriction-certificate-formal'/script)]
        if label=='restriction': arguments+=['--audit']
        arguments+=[str(path)]
        result=subprocess.run([sys.executable,'-B',*arguments],cwd=O,capture_output=True,timeout=30)
        (O/(job+'.'+label+'.audit.stdout')).write_bytes(result.stdout)
        (O/(job+'.'+label+'.audit.stderr')).write_bytes(result.stderr)
        if result.returncode!=0 or json.loads(result.stdout)['status']!='PASS':
            raise RuntimeError('inherited parser failed')
    expected_markers=['SplitZeroRestrictionTransport','SplitZeroRestrictionSource','SplitZeroRestrictionLogCertificate','SplitZeroRestrictionSpectrum','SplitZeroRelationCurve','SplitZeroSpecializationChart','SplitZeroActionHull','SplitZeroCurvatureRestriction','SplitZeroLaplacianControl']
    if re.findall(r'^=== (\w+) ===$',clean,flags=re.M)!=expected_markers:
        raise RuntimeError('source marker mismatch')
    audits.append({'job':int(job),'actual_checkout':checkout,'selected_target_count':71,'counts':{'specialization':29,'laplacian':9,'restriction':26,'spectrum':7},'declarations':declarations,'source_markers':expected_markers,'log_sha256':hashlib.sha256((E/('job_'+job+'.full.log')).read_bytes()).hexdigest(),'log_bytes':(E/('job_'+job+'.full.log')).stat().st_size})
    start=clean.index('##[group]Run set -euo pipefail')
    finish=clean.index('Post job cleanup.')
    core=clean[start:finish]
    (E/('job_'+job+'.verification-section.log')).write_text(core)
core_equal=(E/'job_103666603149.verification-section.log').read_bytes()==(E/'job_103666609598.verification-section.log').read_bytes()
if not core_equal: raise RuntimeError('normalized verification sections differ')
pins={'checkout':'3d3c42e5aac5ba805825da76410c181273ba90b1','elan_script':'0e36a07b9bbcc5381fa6250df109f9a4f94d7bac','lean':'4.31.0','lean_reported_commit':'68218e876d2a38b1985b8590fff244a83c321783','mathlib':'fabf563a7c95a166b8d7b6efca11c8b4dc9d911f','CI_sympy':'1.14.0','CI_mpmath':'1.3.0','original_scalar_git_blob':'ff991f7383922e71cdf0e4a3bc85e89e18f808ef','original_scalar_bytes':7366}
receipt={'schema':'pr27-ci-source-review-v1','head':head,'base':base,'synthetic_merge':merge,'head_and_merge_tree':head_commit['tree']['sha'],'merge_parents':[p['sha'] for p in merge_commit['parents']],'tree_diff_proven_additions_only':True,'changed_files':manifest['tree_diff'],'source_file_count':len(manifest['files']),'full_specialization_logs_reviewed':audits,'normalized_verification_sections_byte_equal':core_equal,'exact_head_run_count':len(runs),'specialization_runs':2,'other_run_count':len(runs)-2,'all_runs':runs,'pins':pins,'finite_receipt':'FINITE_RECEIPT.json','no_local_lean':True,'no_installs':True,'no_remote_writes':True,'gaps':['specialization PR trigger excludes inherited formal dependencies and shared setup; both triggers exclude inherited restriction workbench','version and commit pins are not a fully hermetic binary environment','CI installs pin SymPy1.14.0 but local replay used pre-existing1.13.1','new audit parsers ignore unrecognized axiom-free extra reports and warning-only text; exact actual logs contain no such extras','selected theorem audits and finite calibrations do not certify all declarations or analytic written notes','API/PR checks show11total=2specialization+9other runs, not2+10']}
receipt['git_tree_hash_recomputation']=tree_hash_checks
(ROOT/'CI_RECEIPT.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
all_hashes=[]
for p in sorted(E.iterdir()):
    if p.is_file(): all_hashes.append({'file':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'EVIDENCE_MANIFEST.json').write_text(json.dumps(all_hashes,sort_keys=True,indent=2)+'\n')
print(json.dumps({'status':'PASS','runs':len(runs),'audit_counts':[len(a['declarations']) for a in audits],'normalized_sections_equal':core_equal,'source_files':len(manifest['files'])}))
