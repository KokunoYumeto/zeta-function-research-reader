"""Exact polynomial tests for the retained mixed ideal and its Frobenius."""
from pathlib import Path
import json
import sympy as s
t,u=s.symbols('t u')
j=(t-1)*(u-1)
rows=[]
for p in (2,3,5,7):
    q=s.expand(sum(t**k for k in range(p))*sum(u**k for k in range(p)))
    h=s.Poly(s.expand((q-j**(p-1))/p),t,u)
    assert all(c.q==1 for c in h.coeffs())
    assert s.expand((t**p-1)*(u**p-1)-j*q)==0
    assert s.Poly(q-j**(p-1),t,u,modulus=p).is_zero
    for a,b in ((1,1),(2,3),(-1,2),(3,-2),(-2,-3)):
        w=(t**a-1)*(u**b-1)
        assert s.cancel(w.subs({t:1}))==0
        assert s.cancel(w.subs({u:1}))==0
        assert s.cancel(w.subs({t:t**p,u:u**p},simultaneous=True)-(t**(p*a)-1)*(u**(p*b)-1))==0
    rows.append({'prime':p,'delta_j_integral':True,'linearization_factor':str(q),'special_fibre_identity':True})
# A genuine torsion example: group ring C2 x C3, augmentation generators.
# W=I(C2) tensor I(C3), with basis a=(g-1)(h-1), b=(g-1)(h^2-1).
# g acts as -1; h sends a -> b-a, b -> -a.
G=-s.eye(2)
H=s.Matrix([[-1,-1],[1,0]])
assert G**2==s.eye(2) and H**3==s.eye(2)
F3=(G-s.eye(2)).row_join(H-s.eye(2))
minors=[int(F3[:,[i,k]].det()) for i in range(4) for k in range(i+1,4)]
from math import gcd
from functools import reduce
assert reduce(gcd,minors)==1
report={'frobenius':rows,'torsion_example':{'group':'C2 x C3','rank_W':2,'F3_generators':[[int(v) for v in row] for row in F3.tolist()],'maximal_minor_gcd':1},'all_passed':True}
root=Path(__file__).resolve().parent
(root/'FROBENIUS_CROSS_EFFECT_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('Frobenius mixed-ideal identities and the retained torsion example passed.')
