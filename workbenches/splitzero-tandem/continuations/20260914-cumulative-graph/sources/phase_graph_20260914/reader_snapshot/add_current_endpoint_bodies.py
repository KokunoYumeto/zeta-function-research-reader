"""Add final full current endpoint sources and correlation proof by accepted pins."""
from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parent
N=ROOT.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
extras=ROOT/'EXTRA_DEPENDENCIES.json';data=json.loads(extras.read_text())
sources=[('PGRC',N/'relation_tail_control/relation_row_correlations.tex',
 'fa3e6658130d88d1a301f3e229202cfa8e07630d6f2ec02a95553b38e410b4bc',
 'The full correlations of the original relation rows'),
 ('ACM',N/'relation_tail_control/backprop/replacement/ACM.tex',
 'b516364e11b9a36141c17fddf96b316518aa55905f60182330e7cbd041ac6c31',
 'The original arithmetic metric, relation rows and full correlation control'),
 ('HC',N/'relation_tail_control/backprop/replacement/HC.tex',
 '3534a89af3f688585e1f0b128294f35ae969109ee0a171d91e84410d5715fe9a',
 'The refined arithmetic endpoint and its original holonomy transport')]
for key,p,pin,title in sources:
    assert sha(p)==pin,(p,sha(p),pin)
    if key not in {e['key'] for e in data['files']}:
        data['files'].append({'key':key,'path':str(p),'sha256':pin,'title':title,
          'role':'Complete independently reviewed current source calculation'})
titles={'GR':'Complete Gamma-reference lower bound and arithmetic determinant comparison',
 'TVB':'The original source and relation Toda flows with their exact control maps',
 'EW':'Gamma endpoint-window control and canonical minimum sections'}
for e in data['files']:
    if e['key'] in titles:e['title']=titles[e['key']]
extras.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'extra_sources':len(data['files'])}))
