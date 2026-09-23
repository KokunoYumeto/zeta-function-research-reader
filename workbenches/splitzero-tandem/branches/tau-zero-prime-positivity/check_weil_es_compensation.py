"""Exact finite identities accompanying the analytic proof WEC1–18."""
from pathlib import Path
import sympy as s,json,hashlib
q=s.Rational;I=s.I
G=s.Matrix([[q(1,16),0,0,-q(7,144)],[0,q(2,9),0,0],[0,0,1,0],[-q(7,144),0,0,q(1,16)]])
A0=s.diag(q(1,4),q(1,4),-q(1,4),q(1,4));B=G*A0
J=s.Matrix([[0,0,12,3*s.sqrt(2)],[3,-3,0,0],[s.sqrt(2),s.sqrt(2),0,0],[0,0,12,-3*s.sqrt(2)]])
C=s.Matrix([[0,-1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
T=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
T0=s.diag(1,-1,1,1);TE=4*A0;U=s.diag(1,I,I,1)
checks={}
def eq(name,x,y):checks[name]=all(s.simplify(v)==0 for v in (x-y)) if isinstance(x,s.MatrixBase) else s.simplify(x-y)==0
eq('exact_form_isometry',J.conjugate().T*B*J,C)
eq('inverse',J*J.inv(),s.eye(4))
eq('initial_test_involution',J*T,T0*s.conjugate(J))
eq('unitary_for_ES_form',U.conjugate().T*B*U,B)
eq('corrected_involution',U*J*T,TE*s.conjugate(U*J))
eq('corrected_form_isometry',(U*J).conjugate().T*B*(U*J),C)
ts=[-q(1,2),q(1,2),I/2,-I/2];V=s.Matrix([[(-t)**k for t in ts] for k in range(4)])
checks['distinct_exponential_jets']=s.simplify(V.det())!=0
for name,y,value in [('negative_gain',[1,1,0,0],-2),('positive_gain',[1,-1,0,0],2)]:
    v=s.Matrix(y);eq(name,(v.T*C*v)[0],value)
out=Path(__file__).resolve().parent
report={'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'count':len(checks),'proof_sha256':hashlib.sha256((out/'WEIL_ES_COMPENSATION_DERIVATION.md').read_bytes()).hexdigest(),'scope':'Exact finite coordinate identities. Surjectivity on admissible smooth tests, positive Gram matrix and full explicit-formula compensation are proved in WEC1–18.'}
(out/'WEIL_ES_COMPENSATION_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'count':len(checks)}));assert all(checks.values())
