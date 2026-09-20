from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, flint
from flint import acb, arb, ctx
P=Path(__file__).parent
ctx.prec=384
ctx.threads=1
rows=[]
for t,expected in [(14,1),(15,-1),(21,-1),(22,1)]:
    s=acb(arb(1)/2,t)
    value=s*(s-1)/2*(-s/2*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()
    passed=bool(value.real*expected>0) and bool(value.imag.contains(0))
    rows.append({'height':t,'xi_ball':str(value),'real_sign':expected,'certified':passed})
assert all(r['certified'] for r in rows)
receipt={'created_utc':datetime.now(timezone.utc).isoformat(),'library':'python-flint '+flint.__version__,
         'precision_bits':ctx.prec,'thread_count':ctx.threads,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'rows':rows,'mathematical_receiver':'Continuity and conjugation/functional equation give real xi(1/2+it); sign changes imply gamma1 in (14,15), gamma2 in (21,22), with reflected negative zeros.'}
(P/'FOUR_CRITICAL_ZERO_CERTIFICATES.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
