"""Read-only full Weil-component recombination for the exact source vector."""
from resource_ceiling import install_memory_ceiling
RESOURCE=install_memory_ceiling()
from pathlib import Path
import json
from flint import arb,ctx
ctx.prec=256
ctx.threads=1
path=Path(__file__).with_name('xi4_weil_results.json')
r=json.loads(path.read_text(encoding='utf-8'))
c=[arb(0),-arb(59)/275184,arb(1)/336,arb(1)/1296,arb(3)/132496]
totals={k:arb(0) for k in ('pole','gamma','prime','value')}
for row in r['entries']:
    i,j=row['i'],row['j']
    a=c[i]*c[j]*(1 if i==j else 2)
    for k in totals:
        v=(arb(row[k]) if k!='gamma' else
           arb(row[k]['central'])+arb(0,arb(row[k]['tail_absolute_bound']).upper()))
        totals[k]+=a*v
combined=totals['pole']+totals['gamma']-totals['prime']
assert combined.overlaps(totals['value']) and combined>0
print(json.dumps({'status':'pass','resource':RESOURCE,
    'components':{k:str(v) for k,v in totals.items()},'combined':str(combined),
    'scope':'The compact test w(u)*exp(2iu)*b4(u), not TD Xi(gamma).'},indent=2))
