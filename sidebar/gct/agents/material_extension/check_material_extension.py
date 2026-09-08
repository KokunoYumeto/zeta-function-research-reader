"""Exact retained-b conic, original-coordinate and coefficient connection checks.

Run: python check_material_extension.py
Requires SymPy. Writes only this directory's checks.json.
"""
from pathlib import Path
import datetime
import hashlib
import json
import sympy as sy

ROOT = Path(__file__).resolve().parent
b, s, r, eta, q, p, z = sy.symbols('b s r eta q p z')
beta = b / 4
h = 2*s-b**2/16
delta = b**2-32*s
L = 4+b**2/16-2*s
I = sy.eye(4)
results = []

def check(name, expression):
    entries = list(expression) if isinstance(expression, sy.MatrixBase) else [expression]
    ok = all(sy.cancel(e) == 0 for e in entries)
    results.append({'name': name, 'passed': ok, 'scalar_identities': len(entries)})
    if not ok:
        raise AssertionError(name)

eq = q-1/q
pq = q+1/q
sq = b**2/32-eq**2/2
check('conic p eta relation', pq**2-eq**2-4)
check('original s polynomial with retained r and b',
      b*(beta+eq)/4-(beta+eq)**2/2-sq)
check('quartic on Laurent coordinate', q**4+(2*sq-b**2/16-2)*q**2+1)
check('q inverse in monic quotient after Laurent substitution',
      -q**3+(2-2*sq+b**2/16)*q-1/q)
check('both conic inverse generators',
      sy.Matrix([(pq+eq)/2-q,(pq-eq)/2-1/q]))
check('original discriminant square', delta.subs(s,sq)-16*eq**2)
check('added branch relation', L.subs(s,sq)-pq**2)

K = sy.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,2-2*s+b**2/16],[0,0,1,0]])
Ki = -K**3+(2-2*s+b**2/16)*K
Eta = K-Ki
P = K+Ki
R = beta*I+Eta
check('companion characteristic polynomial',
      K.charpoly(z).as_expr()-(z**4+(2*s-b**2/16-2)*z**2+1))
check('quartic matrix identity', K**4+(2*s-b**2/16-2)*K**2+I)
check('inverse left and right', (K*Ki-I).col_join(Ki*K-I))
check('original r quadratic relation', R**2-b*R/2+2*s*I)
check('eta and added p exact squares', (Eta**2+h*I).col_join(P**2-L*I))
check('recover original s from original r', beta*R-R**2/2-s*I)
check('recover original s from K', b**2*I/32-(K-Ki)**2/2-s*I)

T = sy.Matrix([[1,beta,0,h-2],
               [0,h-1,3-h,beta*(3-h)],
               [0,0,0,2],[0,1,-1,-beta]])
e0 = I[:,0]
check('complete basis columns', T-sy.Matrix.hstack(e0,R*e0,P*e0,R*P*e0))
check('basis determinant retains constant four', T.det()-4)
qcol = sy.Matrix([-beta/2,sy.Rational(1,2),sy.Rational(1,2),0])
q2col = sy.Matrix([(2-h)/2,0,-beta/2,sy.Rational(1,2)])
q3col = sy.Matrix([-beta,1,0,0])-(h-1)*qcol
check('inverse basis q q2 q3',
      (T*qcol-I[:,1]).col_join(T*q2col-I[:,2]).col_join(T*q3col-I[:,3]))
Rb = sy.Matrix([[0,-2*s],[1,b/2]])
check('two original root blocks', R*T-T*sy.diag(Rb,Rb))

def qinteger(n):
    return sum(q**(n-1-2*j) for j in range(n))

C = q**10-q**4-q**(-4)+q**(-10)
Cb = (b**2/16-2*s)*(L**3-5*L**2+6*L-1)*(L-1)
Ch = -h*(7-14*h+7*h**2-h**3)*(3-h)
check('actual source coefficient factor', C-eq**2*qinteger(7)*qinteger(3))
check('trace polynomials for both q integers',
      sy.Matrix([qinteger(7)-(pq**6-5*pq**4+6*pq**2-1),qinteger(3)-(pq**2-1)]))
check('source coefficient descends to retained b and s', C-Cb.subs(s,sq))
check('complete descended polynomial equivalence', Cb-Ch)
check('operator source coefficient', K**10-K**4-Ki**4+Ki**10-Cb*I)
check('branch coefficient has no divided factor', Cb.subs(s,b**2/32))
check('branch first jet with b retained', sy.diff(Cb,s).subs(s,b**2/32)+42)

Dq = -q/(eq*pq)
for name, func, target in [('b',b,0),('s',sq,1),('eta',eq,-1/eq),
                           ('original r',beta+eq,-1/eq),('p',pq,-1/pq)]:
    check('Laurent derivation '+name, Dq*sy.diff(func,q)-target)
check('source coefficient exact derivative',
      Dq*sy.diff(C,q)-sy.diff(Cb,s).subs(s,sq))

A = sy.Matrix([[0,4*b/delta],[0,-16/delta]])
Gamma = sy.diag(A,A-sy.eye(2)/L)
Z = sy.Matrix([[0,64*b/delta**2,0,0],[0,-256/delta**2,0,0],
               [0,0,-1/L**2,64*b/delta**2-8*b/(delta*L)],
               [0,0,0,-256/delta**2+32/(delta*L)-1/L**2]])
check('connection A derivative', A.diff(s)-32*A/delta)
check('connection A square', A**2+16*A/delta)
check('full square with every zero order coefficient', Gamma.diff(s)+Gamma**2-Z)
check('original root commutator', Rb.diff(s)+A*Rb-Rb*A-4*(b*sy.eye(2)-4*Rb)/delta)

# Independent derivation in the Laurent realization tests every basis column.
basisq = sy.Matrix([[1,beta+eq,pq,(beta+eq)*pq]])
Gammaq = Gamma.subs(s,sq)
Zq = Z.subs(s,sq)
check('all four basis derivatives in Laurent algebra',
      Dq*basisq.diff(q)-basisq*Gammaq)
check('all four second basis derivatives in Laurent algebra',
      Dq*(Dq*basisq.diff(q)).diff(q)-basisq*Zq)
# Product-rule check with nonconstant coefficients exercises first-order terms.
fv = sy.Matrix([s**2+b*s,s+b**2,s+b,1+s])
actualq = sy.cancel((basisq*fv.subs(s,sq))[0])
predictedq = sy.cancel((basisq*(fv.diff(s,2)+2*Gamma*fv.diff(s)+Z*fv).subs(s,sq))[0])
check('full operator square on nonconstant coefficient column',
      Dq*sy.diff(sy.cancel(Dq*sy.diff(actualq,q)),q)-predictedq)

x = -1/(2*eta)
y = beta+3*eta
w = 26*eta**2+3*b*eta/2
F1 = (1+x*y)**3*w+y**2*(1+x*y)*(4+3*x*y)
F2 = y+3*x*(1+x*y)**2*w+3*x*y**2*(4+3*x*y)
F3 = 2*x-3*x**2*y-x**3*w
check('original F exact retained three coordinates',
      sy.Matrix([F1-(b**2/16-eta**2),F2-b,F3]))
check('original chart inverse r equals y plus inverse x', y+1/x-beta-eta)
De = lambda e: -sy.diff(e,eta)/eta
DH = sy.Matrix([-1/(2*eta**3),-3/eta,-52-3*b/(2*eta)])
check('all original coordinate material derivatives',
      sy.Matrix([De(x),De(y),De(w)])-DH)
check('all original target material derivatives',sy.Matrix([De(F1)-2,De(F2),De(F3)]))
check('full original second material derivatives',
      sy.Matrix([De(De(x)),De(De(y)),De(De(w))])-
      sy.Matrix([-3/(2*eta**5),-3/eta**3,-3*b/(2*eta**3)]))
check('boundary point original F1', (2*s-4*b**2)+4*b**2-2*s)
check('original ramification values q plus minus one',
      sy.Matrix([sq.subs(q,1)-b**2/32,sq.subs(q,-1)-b**2/32]))
check('extra ramification values q plus minus i',
      sy.Matrix([sq.subs(q,sy.I)-b**2/32-2,sq.subs(q,-sy.I)-b**2/32-2]))
check('b zero full connection', Gamma.subs(b,0)-
      sy.diag(0,1/(2*s),-1/(4-2*s),1/(2*s)-1/(4-2*s)))
check('b zero full zero order square', Z.subs(b,0)-
      sy.diag(0,-1/(4*s**2),-1/(4-2*s)**2,
              -1/(4*s**2)-1/(s*(4-2*s))-1/(4-2*s)**2))
check('b zero original source chart',sy.Matrix([x,y,w]).subs(b,0)-
      sy.Matrix([-1/(2*eta),3*eta,26*eta**2]))
check('b zero original coefficient', Cb.subs(b,0)-
      (-2*s)*(7-28*s+28*s**2-8*s**3)*(3-2*s))

receipt = {
    'status': 'passed',
    'timestamp_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'method': 'Exact rational identities over Q in the displayed original variables, with matrix checks entry by entry.',
    'limitations': 'Finite regression certificates supplement complete TeX proofs; no derivative action or rational inverse on the topological arithmetic quotient is asserted.',
    'check_count': len(results),
    'scalar_identity_count': sum(v['scalar_identities'] for v in results),
    'sympy_version': sy.__version__,
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'tex_sha256': hashlib.sha256((ROOT/'material_extension.tex').read_bytes()).hexdigest(),
    'checks': results,
}
(ROOT/'checks.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(f"PASS {receipt['check_count']} retained-b checks / {receipt['scalar_identity_count']} scalar identities")
