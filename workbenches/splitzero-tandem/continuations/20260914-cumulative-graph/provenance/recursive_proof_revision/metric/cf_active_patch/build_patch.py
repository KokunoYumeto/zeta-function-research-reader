from pathlib import Path
import hashlib,json,difflib
P=Path(__file__).resolve().parent
B=P.parent.parent/'cumulative_source_v1'
def sha(x): return hashlib.sha256(x).hexdigest()
files=['tex/cohorts/cf/13_ACM.tex','tex/cohorts/cf/31_HC.tex']
manifest=[]
for rel in files:
    src=B/rel
    raw=src.read_bytes()
    original=raw.decode('utf-8').replace('\r\n','\n')
    text=original
    if rel.endswith('13_ACM.tex'):
        anchor='Both bounds are finite and measurable on $[0,1]$.'
        assert text.count(anchor)==1
        text=text.split(anchor,1)[0]+(P/'acm_tail.tex').read_text(encoding='utf-8')+'\n'
        sites=['ACM11a/11','ACM13','ACM14--16 and original support primitive']
    else:
        start='No auxiliary polynomial is introduced and no sign is imposed on\n$\\Delta_k^\\Gamma$.'
        end='Indeed all nonquadratic terms of $\\mathcal U_k$ are nonnegative,'
        i,j=text.index(start),text.index(end)
        text=text[:i]+(P/'hc_gamma.tex').read_text(encoding='utf-8')+'\n'+text[j:]
        old='This proves numerical compatibility of the stated actual bound\nfunctions.'
        new=('This proves the stated width of the coarse bound functions obtained\n'
             'by removing the source-dependent entries in (HC9)--(HC10). The\n'
             'refined intersection retains those computed entries; (HC11) makes\n'
             'no assertion that its width equals the coarse width.')
        assert text.count(old)==1
        text=text.replace(old,new)
        start='Finally the supplied holonomy construction allows any fixed\n'
        end='For the averaged original phase metrics the already proved stronger\n'
        i,j=text.index(start),text.index(end)
        averaged=original[original.index(end):original.index('\\subsection{The sharper finite comparison')]
        text=text[:i]+(P/'hc_phase.tex').read_text(encoding='utf-8')+text[j:]
        assert averaged in text
        sites=['HC9/10 signed Gamma interval','HC11 precise coarse-width scope','HC14 exact source restriction and all controls','HC13a/HC14d propagated derivative-source budget']
    target=P/'derived'/rel
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(text,encoding='utf-8',newline='\n')
    oldpath=P/'originals'/rel
    oldpath.parent.mkdir(parents=True,exist_ok=True)
    oldpath.write_bytes(raw)
    diff=''.join(difflib.unified_diff(original.splitlines(True),text.splitlines(True),fromfile=rel+' (active original)',tofile=rel+' (updated)'))
    (P/(Path(rel).stem+'.diff')).write_text(diff,encoding='utf-8')
    manifest.append({'target_relative':rel,'source':str(src),'source_sha256':sha(raw),'derived':str(target),'derived_sha256':sha(target.read_bytes()),'sites':sites,'averaged_quotient_gram_unchanged':True if rel.endswith('31_HC.tex') else None})
deps=[]
for dep in [P.parent.parent/'recursive_metric_transport.tex',P.parent.parent/'incoming_pr29_metric/incoming_source_metric_control.tex']:
    deps.append({'path':str(dep),'sha256':sha(dep.read_bytes())})
(P/'PATCH_MANIFEST.json').write_text(json.dumps({'status':'proof written; compilation pending','files':manifest,'complete_input_proofs':deps},indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))
