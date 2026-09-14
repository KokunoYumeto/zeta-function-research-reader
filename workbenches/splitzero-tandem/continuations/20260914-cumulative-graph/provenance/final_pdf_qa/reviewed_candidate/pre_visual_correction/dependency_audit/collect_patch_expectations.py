"""Capture current accepted-lane source pins as explicit active reader routes.

This records proposed active bytes, not mathematical acceptance. Independent
review receipts accompany their owning lanes. Final assembly must contain
these exact bytes and recursively include each TeX route from its real main.
"""
from pathlib import Path
import argparse,hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent

def read(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

rows=[]
parser=argparse.ArgumentParser()
parser.add_argument('--lane',choices=['all','boundary','metric'],default='all')
args=parser.parse_args()
def add(lane,source,reader_path,pin,include_required=True):
    source=Path(source)
    actual=sha(source)
    if actual!=pin: raise ValueError(('source pin stale',str(source),pin,actual))
    rows.append({'lane':lane,'source':str(source),'reader_path':reader_path,
                 'sha256':pin,'bytes':source.stat().st_size,'include_required':include_required})

for r in (read(ROOT/'metric/PATCH_MANIFEST.json')['rows'] if args.lane in ['all','metric'] else []):
    p=Path(r['revised'])
    rel=p.relative_to(ROOT/'metric/staged').as_posix().replace('tex/next_edition/','tex/')
    add('metric',p,rel,r['revised_sha256'])
for r in (read(ROOT/'metric/BASELINE_ENDPOINT_PATCH_MANIFEST.json')['files'] if args.lane in ['all','metric'] else []):
    add('metric',ROOT/'metric/baseline_patch'/r['path'],r['path'],r['new_sha256'],r['path'].endswith('.tex'))
cfmanifest=ROOT/'metric/cf_active_patch/PATCH_MANIFEST.json'
if args.lane in ['all','metric'] and cfmanifest.is_file():
    for r in read(cfmanifest)['files']:
        add('metric-cf',r['derived'],r['target_relative'],r['derived_sha256'])
for r in (read(ROOT/'support/MANIFEST.json')['files'] if args.lane=='all' else []):
    rel=r['path'].replace('\\','/')
    if rel.startswith('updated/tex/'):
        add('support',ROOT/'support'/rel,rel.removeprefix('updated/'),r['sha256'])
for role,r in (read(ROOT/'support/filtration/INVENTORY.json').items() if args.lane=='all' else []):
    if isinstance(r,dict) and 'revised_file' in r:
        target={'MW':'tex/tau_mixed_support_monodromy_filtration.tex',
                'MRE':'tex/tau_mixed_relative_extension_control.tex'}[role]
        add('support',r['revised_file'],target,r['revised_sha256'])
for r in (read(ROOT/'boundary/PATCH_MANIFEST.json')['records'] if args.lane in ['all','boundary'] else []):
    if 'revised' not in r:
        continue
    rel=r['revised'].replace('\\','/')
    active=rel.removeprefix('revised/')
    if active=='tex/marked_product_boundary_connection.tex':
        # Preserve the complete standalone edition while compiling the proved
        # complete body. The wrapper extraction is independently checked below.
        standalone=ROOT/'boundary'/rel
        add('boundary',standalone,'provenance/revised_complete_sources/marked_product_boundary_connection.tex',r['revised_sha256'],False)
        fragment=ROOT/'boundary/proofs/BC_CURRENT_FRAGMENT.tex'
        source_text=standalone.read_text(encoding='utf-8-sig')
        body=source_text.split(r'\begin{document}',1)[1].rsplit(r'\end{document}',1)[0]
        assert body.count(r'\maketitle')==1
        body=body.replace(r'\maketitle','',1).strip('\n')
        fragment_text=fragment.read_text(encoding='utf-8-sig')
        assert fragment_text.count(body)==1,'BC complete mathematical body not transferred exactly'
        receipt={'standalone_sha256':sha(standalone),'fragment_sha256':sha(fragment),
                 'complete_body_occurrences':fragment_text.count(body),'pass':True,
                 'exact_transform':'Strip document preamble and document delimiters; remove one maketitle; retain the complete abstract and body unchanged inside local macro group.'}
        (HERE/'BC_COMPLETE_BODY_TRANSFER_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
        add('boundary',fragment,active,sha(fragment))
        continue
    add('boundary',ROOT/'boundary'/rel,active,r['revised_sha256'],active.startswith('tex/') or active.startswith('build/'))

out={'schema':'active-proof-route-expectations-v1','patches':rows,
     'note':'Recollect after final lane pins; root conclusion and separately added proofs need their own explicit final rows. Exact paths are checked against actual main, not assumed from staging.'}
outpath=HERE/('EXPECTED_ACTIVE_PATCHES.json' if args.lane=='all' else 'EXPECTED_'+args.lane.upper()+'_PATCHES.json')
outpath.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'rows':len(rows),'output':str(outpath)}))
