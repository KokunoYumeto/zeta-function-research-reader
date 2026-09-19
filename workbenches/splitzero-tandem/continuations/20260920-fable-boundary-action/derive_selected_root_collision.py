"""Exact derivative and every compound on the original selected-root branch."""
import sympy as s
import itertools
import json
from pathlib import Path
a,y,z,w=s.symbols('a y z w')
eps=s.symbols('epsilon',positive=True)
P=s.Matrix([a**3*z+2*a**2*y-s.I*a,
 -a**3*y**2*z-2*s.I*a**2*y*z+a**2*w-2*a**2*y**3-10*s.I*a*y**2+3*a*z+y,
 2*a**3*y**3*z+6*s.I*a**2*y**2*z+2*a**2*w*y+4*a**2*y**4+2*s.I*a*w
 -4*s.I*a*y**3-2*a*y*z+2*s.I*z+7*y**2,
 2*a**3*y**4*z+8*s.I*a**2*y**3*z+a**2*w*y**2+4*a**2*y**5+2*s.I*a*w*y
 +7*s.I*a*y**4-10*a*y**2*z-4*s.I*y*z-w-3*y**3])
q=s.Matrix([1/eps,-s.I*eps,3*s.I*eps**2,eps**2-13*s.I*eps**3])
sub=dict(zip([a,y,z,w],q))
assert (P.subs(sub,simultaneous=True)-s.Matrix([0,1,eps**2,0])).applyfunc(s.expand)==s.zeros(4,1)
J=P.jacobian([a,y,z,w]).subs(sub,simultaneous=True).applyfunc(s.expand)
assert s.expand(J.det()+2)==0
Ji=J.inv().applyfunc(s.expand)
assert (J*Ji-s.eye(4)).applyfunc(s.expand)==s.zeros(4)
assert (Ji*J-s.eye(4)).applyfunc(s.expand)==s.zeros(4)
assert (J*q.diff(eps)-s.Matrix([0,0,2*eps,0])).applyfunc(s.expand)==s.zeros(4,1)
out={'all_assertions_passed':True,'derivative':str(J),'inverse':str(Ji),'compounds':{}}
for name,M in [('forward',J),('inverse',Ji)]:
    records=[]
    for k in range(1,5):
        ix=list(itertools.combinations(range(4),k))
        compound=s.Matrix([[s.expand(M.extract(I,K).det()) for K in ix] for I in ix])
        valuation=min(int(term.as_powers_dict().get(eps,0)) for f in compound if f!=0
                      for term in s.Add.make_args(f))
        leading=compound.applyfunc(lambda f:s.expand(eps**(-valuation)*f).subs(eps,0))
        record={'k':k,'pole_order':-valuation,
                'index_order':[[j+1 for j in I] for I in ix],
                'leading':[[str(x) for x in row] for row in leading.tolist()],
                'rank':leading.rank()}
        records.append(record)
        print(name,k,'pole',-valuation,'leading',leading,flush=True)
    out['compounds'][name]=records
print('J inverse:',Ji,flush=True)
Path(__file__).with_name('selected_root_collision_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Exact original derivative, inverse, all compounds and branch velocity passed.',flush=True)
