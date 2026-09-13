#!/usr/bin/env python3
"""Strict actual socle/quotient audit; the inherited fail-closed parser is reused."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
REPO=Path(__file__).resolve().parents[2]
ROOT=REPO/'formal/splitzero'
sys.path.insert(0,str(ROOT))
from check_derived import audit,strip_comments
MODULES=['SplitZeroBoundarySocle','SplitZeroBoundarySocleSupport']
TARGETS=['SplitZero.BoundarySocle.'+x for x in ['comparison','comparison_mk','comparison_killed','comparison_injective','toSocle_surjective','socleEquiv','sourceAction','targetAction','action_square','divide_intertwiner','powerDiagonal','positive_exponent_factor','powerDiagonal_injective','diagonalSocleEquiv']]+['SplitZero.BoundarySocleSupport.'+x for x in ['sourceRelations','targetRelations','comparisonHom','original_square','total_injective','range_iff_supported_killed','present_empty_face']]
def run(cmd):
 p=subprocess.run(cmd,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 print(p.stdout,flush=True)
 if p.returncode:raise RuntimeError('failed: '+repr(cmd))
 return p.stdout
if sys.argv[1:] not in ([],['--joint']):raise ValueError('unknown arguments')
if not sys.argv[1:]:
 for mod in MODULES:
  src=ROOT/(mod+'.lean');text=strip_comments(src.read_text())
  if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b',text):raise ValueError('proof escape')
  out=ROOT/'.lake/build/lib/lean'/(mod+'.olean');out.unlink(missing_ok=True)
  run(['lake','env','lean','--trust=0','-DwarningAsError=true','-o',str(out),src.name])
body=''.join('import '+m+'\n' for m in MODULES)
if sys.argv[1:]:body+='import SplitZeroCanonicalSourceContrast\nimport SplitZeroJointHomotopy\nimport SplitZeroConormalTower\n'
body+='\n'+''.join('#print axioms '+n+'\n' for n in TARGETS)
(ROOT/'AuditBoundarySocle.lean').write_text(body)
text=run(['lake','env','lean','--trust=0','-DwarningAsError=true','AuditBoundarySocle.lean'])
reports=audit(text,TARGETS)
record={'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),'modules':MODULES,'targets':len(TARGETS),'axioms':reports,'sha256':{m:hashlib.sha256((ROOT/(m+'.lean')).read_bytes()).hexdigest() for m in MODULES},'joint':bool(sys.argv[1:]),'scope':'Constructed v-kernel equivalence for the actual scalar-times-injective-map cokernel; diagonal lattice instance; induced actions and natural original SplitZero quotient maps. No l-adic inertia, period asymptotics or complete tensor-derived functor is asserted.'}
logdir=ROOT/'.boundary-socle-logs';logdir.mkdir(exist_ok=True)
(logdir/('joint.json' if sys.argv[1:] else 'receipt.json')).write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True),flush=True)
