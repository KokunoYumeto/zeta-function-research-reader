"""Independent exact checks for the global dualizing and deck calculation.

No floating point arithmetic, rendering, source discovery, or publication.
The divisor argument is proved in the accompanying TeX, not inferred from tests.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
A, B, C, D, r = s.symbols('A B C D r')
a, y, z, w = s.symbols('a y z w')
i = s.I
checks = []

def zero(name, value):
    items = list(value) if isinstance(value, (s.MatrixBase, list, tuple)) else [value]
    bad = [str(s.factor(v)) for v in items if s.factor(v) != 0]
    checks.append({'name': name, 'entries': len(items), 'passed': not bad})
    if bad:
        raise AssertionError((name, bad))

h = A*r**4 + r**3 + B*r**2 + C*r + D
hp = s.diff(h, r)
ee = [s.Integer(1), A*r, A*r**2+r, A*r**3+r**2+B*r]
oo = [A, A*r+1, A*r**2+r+B, A*r**3+r**2+B*r+C]
E = s.Matrix([[1,0,0,0], [0,A,1,B], [0,0,A,1], [0,0,0,A]])
O = s.Matrix([[A,1,B,C], [0,A,1,B], [0,0,A,1], [0,0,0,A]])

def rem(poly):
    return s.Poly(s.rem(poly, h, r), r)

def col(poly):
    q = rem(poly)
    return s.Matrix([q.nth(j) for j in range(4)])

def res(poly):
    return s.cancel(rem(poly).nth(3)/A)

C0 = s.Matrix([[res(f*q) for q in oo] for f in ee])
Cexpect = s.Matrix([[0,0,0,1],[0,0,A,0],[0,A,1,0],[A,1,B,0]])
zero('all sixteen residue cross entries', C0-Cexpect)
zero('cross determinant', C0.det()-A**3)
B0 = s.zeros(8)
B0[:4,4:] = C0
B0[4:,:4] = C0.T
zero('full pairing determinant', B0.det()-A**6)
Cinv = s.Matrix([[0,A**-3-B*A**-2,-A**-2,A**-1],
                 [0,-A**-2,A**-1,0],[0,A**-1,0,0],[1,0,0,0]])
zero('both cross inverse products', list(C0*Cinv-s.eye(4))+list(Cinv*C0-s.eye(4)))
assert B0.subs(A,0).rank() == 6
checks.append({'name':'A=0 rank, including every B,C,D','entries':1,'passed':True})
rad = s.zeros(8,2); rad[1,0]=1; rad[4,1]=1
zero('A=0 full radical generators', B0.subs(A,0)*rad)

e1square = (E.inv()*col(ee[1]**2)).applyfunc(s.cancel).subs(A,0)
e1o0 = (O.inv()*col(ee[1]*oo[0])).applyfunc(s.cancel).subs(A,0)
o0square = (E.inv()*col(hp*oo[0]**2)).applyfunc(s.cancel).subs(A,0)
zero('infinity even idempotent relation', e1square+s.Matrix([0,1,0,0]))
zero('infinity even-odd relation', e1o0+s.Matrix([1,0,0,0]))
zero('infinity odd square relation', o0square-s.Matrix([0,1,0,0]))
# Express the two-dimensional infinity ideal in the basis (e_infty,o0).
def infmul(v, q):
    return s.Matrix([v[0]*q[0]-v[1]*q[1],v[0]*q[1]+v[1]*q[0]])
plus=s.Matrix([s.Rational(1,2),i/2])
minus=s.Matrix([s.Rational(1,2),-i/2])
zero('both infinity projectors and their orthogonality',
     list(infmul(plus,plus)-plus)+list(infmul(minus,minus)-minus)
     +list(infmul(plus,minus))+list(plus+minus-s.Matrix([1,0])))
zero('included and omitted infinity signs',
     [plus[0]+plus[1]*(-i)-1,plus[0]+plus[1]*i,
      minus[0]+minus[1]*(-i),minus[0]+minus[1]*i-1])

# Independent evaluation construction at the original seven-point target.
rows=[]; weights=[]
for rr, tt in [(-1,s.sqrt(2)),(-1,-s.sqrt(2)),(0,i),(0,-i),
               (1,s.sqrt(2)),(1,-s.sqrt(2))]:
    rows.append([f.subs({A:0,B:0,C:-1,D:0,r:rr}) for f in ee]
                +[tt*q.subs({A:0,B:0,C:-1,D:0,r:rr}) for q in oo])
    weights.append(1/(2*tt**3))
for theta in [-i,i]:
    rows.append([1,-1,0,1,theta,0,-theta,0]); weights.append(s.Integer(0))
V=s.Matrix(rows)
T=V.T*V
zero('original-target trace determinant',s.simplify(T.det())-2**14)
zero('original-target residue via eight evaluation weights',
     (V.T*s.diag(*weights)*V-B0.subs({A:0,B:0,C:-1,D:0})).applyfunc(s.simplify))

# Reconstruct the original polynomial and check the fixed deck identities.
b=i+a*y; c=-i+2*a*y+a*a*z
d=-i*y-a*(i*z+2*y*y)-a*a*y*z
e=2*z-7*i*y*y+a*w
f=i*w+3*i*y**3-4*y*z+a*(6*i*y*y*z+w*y+4*y**4)+2*a*a*y**3*z
P=s.Matrix([a*c,a*e+b*d,a*f+b*e,b*f])
q=s.Matrix([a,y,z,w])
Sigma=s.Matrix([-a,y+2*i/a,-z+6*i/a**2,
                w-14*i*y*y/a+28*y/a**2+40*i/a**3])
sub=dict(zip(q,Sigma))
zero('original unit relation',a*d+b*c-1)
zero('original resultant-one relation',a**3*f-a**2*b*e+a*b*b*d-b**3*c-1)
zero('original constant Jacobian',P.jacobian(q).det()+2)
zero('deck fixes every original target coordinate',P.subs(sub,simultaneous=True)-P)
zero('deck squares to identity',Sigma.subs(sub,simultaneous=True)-q)
weighted=(a**3*Sigma/2).applyfunc(s.expand)
F=s.Matrix([-a**4/2,a**3*y/2+i*a*a,-a**3*z/2+3*i*a,
            a**3*w/2-7*i*a*a*y*y+14*a*y+20*i])
zero('every weighted deck coordinate',weighted-F)
zero('weighted boundary value',F.subs(a,0)-s.Matrix([0,0,0,20*i]))
J=F.jacobian(q)
zero('weighted Jacobian determinant',J.det()-a**12/4)
J0=s.zeros(4); J0[:,0]=s.Matrix([0,0,3*i,14*y])
zero('entire weighted boundary differential',J.subs(a,0)-J0)
assert J0.rank()==1
checks.append({'name':'weighted boundary differential rank one','entries':1,'passed':True})
zero('unweighted cubic leading vector',(a**3*Sigma).applyfunc(s.expand).subs(a,0)-s.Matrix([0,0,0,40*i]))

# Complex Hermitian metrics: these deliberately have nonreal off-diagonal
# entries, so an erroneous replacement of transpose by adjoint is detected.
Ve=s.Matrix([[1,i,1,0],[0,2,1+i,1],[i,0,1,2],[1,1,0,1]])
Vo=s.Matrix([[2,0,i,1],[1,1,0,i],[0,i,2,1],[i,1,1,1]])
Ge=Ve.H*Ve+s.eye(4)
Go=Vo.H*Vo+s.eye(4)
Cs=C0.subs({A:0,B:2+3*i})
L=Go.inv()*Cs.H*Ge.inv().T*Cs
k2=Go[0,0]*Ge[1,1]
lam=s.symbols('lam')
cp=s.Poly(L.charpoly(lam).as_expr(),lam)
zero('complex-metric rank-three spectral constant',s.cancel(-cp.nth(1)-k2/(Ge.det()*Go.det())))
zero('complex-metric spectral zero',cp.nth(0))
zero('complex-metric first invariant',s.cancel(cp.nth(3)+s.trace(L)))
zero('complex-metric second invariant',s.cancel(cp.nth(2)-(s.trace(L)**2-s.trace(L*L))/2))
K=s.zeros(4);K[0,1]=1
zero('rank-one original-metric leading norm',s.trace(Go*K*Ge.T*K.H)-k2)
eta=s.Matrix([1+i,2-i,3+2*i,-1+3*i])
zero('exact dual Gram transpose convention',(eta.T*Ge.inv()*s.conjugate(eta)-eta.H*Ge.inv().T*eta)[0])
zero('complex boundary cross adjugate',Cs.adjugate()-K)
C1=s.Matrix([[0,0,0,0],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
K2=s.Matrix([[0,-B,-1,0],[0,-1,0,0],[0,0,0,0],[0,0,0,0]])
K1=s.Matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[0,0,0,0]])
K0=s.Matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]])
zero('finite-parameter forward difference',C0-C0.subs(A,0)-A*C1)
zero('finite-parameter complete inverse difference',Cinv-(K/A**3+K2/A**2+K1/A+K0))
hs=[s.simplify(s.trace(Go.inv()*C1.H*Ge.inv().T*C1))]
hs += [s.simplify(s.trace(Ge.T*kj.subs(B,2+3*i).H*Go*kj.subs(B,2+3*i)))
       for kj in [K0,K1,K2]]
assert all(x.is_Rational and x>0 for x in hs)
checks.append({'name':'exact complex-metric positivity of all four finite-bound coefficients',
               'entries':4,'passed':True})

sources={}
for rel in ['FINITE_COMPLETION_ACCEPTED_BODY.tex','RESIDUE_DUALITY_BODY.tex',
            'independent/GLOBAL_SIGNED_BASIS_INDEPENDENT.tex',
            'GLOBAL_RESIDUE_DUALITY_BODY.tex',
            'independent/GLOBAL_DUALIZING_REVIEW.tex']:
    path=BASE/rel
    if path.exists():
        sources[rel]=hashlib.sha256(path.read_bytes()).hexdigest()
report={'status':'PASS','check_groups':len(checks),
        'scalar_entries':sum(x['entries'] for x in checks),
        'checks':checks,'source_sha256':sources,
        'limits':'Divisor multiplicities, nontriviality of the dualizing line, and metric limits are proved in the TeX; no finite list of algebra checks replaces those arguments.'}
(HERE/'GLOBAL_DUALIZING_REVIEW.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'check_groups':report['check_groups'],'scalar_entries':report['scalar_entries']}))
