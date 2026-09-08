"""Independent audit of the arbitrary-b connection, including zero-order terms."""
from pathlib import Path
import json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
b,z,r,q=s.symbols('b s r q')
beta=b/4
delta=b*b-32*z
L=4+b*b/16-2*z
h=2*z-b*b/16
Ab=s.Matrix([[0,4*b/delta],[0,-16/delta]])
G=s.diag(Ab,Ab-s.eye(2)/L)
Z=s.Matrix([[0,64*b/delta**2,0,0],[0,-256/delta**2,0,0],
 [0,0,-1/L**2,64*b/delta**2-8*b/(delta*L)],
 [0,0,0,-256/delta**2+32/(delta*L)-1/L**2]])
tests=[]
def eq(name,left,right):
    vals=list(left-right) if isinstance(left,s.MatrixBase) else [left-right]
    assert all(s.cancel(v)==0 for v in vals),name
    tests.append(name)
eq('full connection square with all zero-order terms',G.diff(z)+G**2,Z)
eq('b0 square complete',Z.subs(b,0),s.diag(0,-1/(4*z*z),-1/(4-2*z)**2,
 -1/(4*z*z)-1/(z*(4-2*z))-1/(4-2*z)**2))
R=s.Matrix([[0,-2*z],[1,b/2]])
eq('connection multiplication commutator',R.diff(z)+Ab*R-R*Ab,4*(b*s.eye(2)-4*R)/delta)
eq('quadratic original relation',R**2-b*R/2+2*z*s.eye(2),s.zeros(2))
K=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,2+b*b/16-2*z],[0,0,1,0]])
Ki=-K**3+(2+b*b/16-2*z)*K
RR=beta*s.eye(4)+K-Ki
PP=K+Ki
eq('quartic inverse both sides',K*Ki,s.eye(4))
eq('quartic inverse reverse',Ki*K,s.eye(4))
eq('recovered original s',b*RR/4-RR**2/2,z*s.eye(4))
eq('added p coordinate',PP**2,L*s.eye(4))
T=s.Matrix([[1,beta,0,h-2],[0,h-1,3-h,beta*(3-h)],[0,0,0,2],[0,1,-1,-beta]])
eq('basis determinant',T.det(),4)
eq('original root basis intertwining',RR*T,T*s.diag(R,R))
eta=q-1/q
pq=q+1/q
sq=b*b/32-eta*eta/2
D=-q/(eta*pq)
eq('Laurent base derivative',D*s.diff(sq,q),1)
eq('Laurent root derivative',D*s.diff(beta+eta,q),-1/eta)
eq('Laurent trace derivative',D*s.diff(pq,q),-1/pq)
eq('original ramification divisor',delta.subs(z,sq),16*eta**2)
eq('added ramification divisor',L.subs(z,sq),pq**2)
for index,expected in [(0,0),(1,1),(2,2),(3,3)]:
    basis=[s.Integer(1),beta+eta,pq,(beta+eta)*pq]
    vector=G[:,index]
    represented=sum(basis[k]*vector[k].subs(z,sq) for k in range(4))
    eq('connection column '+str(index),D*s.diff(basis[index],q),represented)
receipt={'status':'passed','check_count':len(tests),'checks':tests,
 'scope':'exact arbitrary-parameter identities, independent column derivation and operator square',
 'proof_sha256':hashlib.sha256((ROOT/'agents/material_extension/material_extension.tex').read_bytes()).hexdigest()}
(HERE/'arbitrary_b_checks.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(tests)}))
