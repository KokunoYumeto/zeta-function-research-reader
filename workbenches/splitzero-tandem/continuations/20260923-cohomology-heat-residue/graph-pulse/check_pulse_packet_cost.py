"""Exact matrix-series checks for PCO9--11 in nontrivial jet coordinates."""
from pathlib import Path
import json
import sympy as s

M=s.Matrix([[s.I,0,0],[1,s.I,0],[0,0,1-s.I]])
P=s.Matrix([[1,s.I,2,0],[0,1,1,s.I],[1,0,1,2]])
Ma=M*M-s.eye(3)/4
C=Ma*P*P.H*Ma.H
K=C.inv()
A=s.Integer(5);B=s.Integer(3);mu=s.Integer(2);k=s.Rational(1,4)
T=k*M*M
# Order-two coefficient of an inverse comes from differentiating C(e)H(e)=I.
C0=mu**2*C
C2=mu**2*(T*C+C*T.H)
H0=C0.inv()
H2=-H0*C2*H0
native0=A*H0
native2=B*H0/2+A*H2
expected0=A*K/mu**2
expected2=(B*K/2-A*k*((M*M).H*K+K*M*M))/mu**2
checks=0
def eq(a,b,name):
    global checks
    difference=a-b
    ok=(difference.applyfunc(s.simplify)==s.zeros(*difference.shape)
        if isinstance(difference,s.MatrixBase) else s.simplify(difference)==0)
    if not ok: raise ArithmeticError(name)
    checks+=1
eq(native0,expected0,'leading matrix')
eq(native2,expected2,'complete first correction')
eq(s.trace(native0.inv()*native2),3*B/(2*A)-2*k*s.re(s.trace(M*M)),
   'full log determinant correction')
eq(C2,mu**2*(Ma*T*P*P.H*Ma.H+Ma*P*P.H*T.H*Ma.H),
   'multiplication order')
# The nilpotent derivative row really participates: its correction differs.
Mr=s.diag(s.I,s.I,1-s.I)
omitted=(B*K/2-A*k*((Mr*Mr).H*K+K*Mr*Mr))/mu**2
if (expected2-omitted).applyfunc(s.simplify)==s.zeros(3):
    raise ArithmeticError('negative control failed to detect removed jet')
checks+=1
result={'status':'passed','exact_predicates':checks,
        'negative_control':'Removing the retained nilpotent derivative changes the matrix correction.',
        'scope':'Auxiliary three-dimensional jet matrices; verifies PCO9--11 orientation and coefficients. Bump constants in the proof remain their original integrals; these test constants are not asserted to be their values.'}
Path(__file__).with_name('PULSE_PACKET_COST_VERIFICATION.json').write_text(
    json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
