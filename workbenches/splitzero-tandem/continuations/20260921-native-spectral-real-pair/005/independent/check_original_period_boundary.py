"""Exact original coefficient-boundary jets; no sampled periods or unit phases."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
B, E, q = s.symbols('beta eta q')
phi = 1 + q + q**2 + q**3 + q**4
checks = []

def red(x):
    n, d = s.fraction(s.cancel(x))
    return s.cancel(s.rem(n, phi, q) / d)

def check(name, x):
    entries = list(x) if isinstance(x, s.MatrixBase) else [x]
    for entry in entries:
        assert red(entry) == 0, (name, s.factor(entry))
    checks.append({'name': name, 'entries': len(entries)})

def Rn(n):
    out = s.zeros(4)
    for a in range(1, 5):
        for r in range(4):
            T = 5*n+r+1-a
            for h in range(max(-1, T//4)+1):
                if (T-4*h) % 2:
                    continue
                p = (T-4*h)//2
                L = p+h-n
                assert L >= 0
                out[a-1, r] += B**p*E**h/(3**p*s.factorial(p)*s.factorial(h))*(-1)**L*5**L*s.rf(s.Rational(a, 5), L)
    return out

Q = s.Matrix([[0,0,1,0],[0,-1,0,B],[1,0,-B,0],[0,B,0,E-B**2]])
T = s.Matrix([[0,0,0,-E],[1,0,0,0],[0,1,0,-B],[0,0,1,0]])
R = [Rn(n) for n in range(3)]
Ri = [R[0].inv()]
for n in range(1, 3):
    Ri.append(s.expand(-Ri[0]*sum((R[k]*Ri[n-k] for k in range(1,n+1)),s.zeros(4))))
D = s.diag(q,q**2,q**3,q**4)
G = [s.expand(sum((Ri[k]*D*R[n-k] for k in range(n+1)),s.zeros(4))) for n in range(3)]
e0 = s.eye(4)[:,0]

def coefficient(m, n, matrices):
    # [xi^m z^n] of e^(-xi) f/(4 i delta gamma).
    return s.factor(sum(((matrices[k]*T**a*e0).dot(Q*matrices[n-k]*T**(m-a)*e0)/(s.factorial(a)*s.factorial(m-a))
                          for k in range(n+1) for a in range(m+1)),s.S.Zero))

for m in range(4):
    check(f'real-phase boundary jet {m}', coefficient(m,0,G))
a = B*(q**6-q**4)/36
c = B**2*q**3*(q-1)*(2*q**2+2*q+1)/9
d = -B**2*q**4*(B**2-9*E)*(q-1)*(q**2+3*q+1)/81
check('real-phase xi4', coefficient(4,0,G)-a)
check('real-phase xi z', coefficient(1,1,G)-c)
check('real-phase z2', coefficient(0,2,G)-d)
for m,n in [(0,0),(1,0),(2,0),(3,0),(0,1),(2,1),(1,2)]:
    check(f'real-phase zero coefficient {m},{n}',coefficient(m,n,G))

W = T**2+B*s.eye(4)/3
H = [(W.inv()*g*W).applyfunc(s.factor) for g in G]
X = B**4-27*B**2*E+81*E**2
Y = 3*B**4-27*B**2*E+81*E**2
a2 = -q**4*(q**2-1)*(X*q**2+Y)/(2*B**2-9*E)**2
c2 = coefficient(1,1,H)
d2 = coefficient(0,2,H)
c2_written = q**4*(q-1)/(54*(2*B**2-9*E)**2)*(2*B**6*(6*q**3+q**2+15*q+13)-B**4*E*(432*q**3+189*q**2+405*q+369)+(1944*B**2*E**2-4374*E**3)*(2*q**3+q**2+q+1))
d2_written = -q**4*(B**2-9*E)*(q-1)/(1458*(2*B**2-9*E)**2)*(2*B**6*(9*q**3-6*q**2+25*q+17)-27*B**4*E*(24*q**3-3*q**2+19*q+15)+(1944*B**2*E**2-4374*E**3)*(3*q**3+q+1))
check('second-phase written mixed polynomial',c2-c2_written)
check('second-phase written period polynomial',d2-d2_written)
check('second-phase constant',coefficient(0,0,H))
check('second-phase linear',coefficient(1,0,H))
check('second-phase xi2',coefficient(2,0,H)-a2)
check('second-phase z linear',coefficient(0,1,H))

alpha, chi, k, r = s.symbols('alpha chi k r', real=True)
C = B/(6*k)
vp = (q*(alpha+C*chi)+r*(-C*chi+s.I*chi))/(alpha+s.I*chi)
vm = (q*(alpha+C*chi)+r*(-C*chi-s.I*chi))/(alpha-s.I*chi)
expected = 4*s.I*chi*(alpha+C*chi)*(r-q)*(alpha*(alpha+C*chi)*q+chi*(chi-C*alpha)*r)/(alpha**2+chi**2)**2
check('full-unit boundary constant identity',vp**2-vm**2-expected)
check('multiplication root polynomial',T**4+B*T**2+E*s.eye(4))
delta,gamma=s.symbols('delta gamma',real=True)
roots=[delta+s.I*gamma,delta-s.I*gamma,-delta+s.I*gamma,-delta-s.I*gamma]
V=s.Matrix([[w**m for m in range(4)] for w in roots])
B0=s.Matrix([[0,0,0,s.Rational(1,2)],[0,0,-s.Rational(1,2),0],[0,-s.Rational(1,2),0,0],[s.Rational(1,2),0,0,0]])
check('literal quadratic coefficient identity',V.T*B0*V-4*s.I*delta*gamma*Q.subs({B:2*(gamma**2-delta**2),E:(delta**2+gamma**2)**2}))
check('second-phase multiplication determinant',W.det()-(E-2*B**2/9)**2)

def orbit_product(expr):
    p = s.S.One
    for j in range(1,5):
        p = red(p*expr.subs(q,q**j))
    return s.factor(p)

check('real-phase product leading',orbit_product(a)-5*(B/36)**4)
P = Y**4-X*Y**3+X**2*Y**2-X**3*Y+X**4
check('second-phase product leading',orbit_product(a2)-5*P/(2*B**2-9*E)**8)

# Independent confirmation of the root's fixed-cutoff inverse calculation.
xx = s.symbols('xx')
poly = s.S.One
for j in range(1,5):
    poly = red(s.expand(poly*(d.subs(q,q**j)+c.subs(q,q**j)*xx)))
L = 125*B**8*(B**2-9*E)**4/s.Integer(81)**4
t0 = 9/(B**2-9*E)
target = [1,-2*t0,2*t0**2,-t0**3]
for m in range(4):
    check(f'four-factor mixed coefficient {m}',s.expand(poly).coeff(xx,m)-L*target[m])
tt = s.symbols('tt')
check('reciprocal convolution through degree3',s.series((1-2*tt+2*tt**2-tt**3)*(1+2*tt+2*tt**2+tt**3),tt,0,4).removeO()-1)
H4 = s.Matrix([[1,2*tt,2*tt**2,tt**3],[0,1,2*tt,2*tt**2],[0,0,1,2*tt],[0,0,0,1]])
for size,value in [(1,tt**3),(2,2*tt**4),(3,tt**3),(4,1)]:
    check(f'inverse corner minor {size}',H4[:size,4-size:].det()-value)

receipt = {
    'status':'pass',
    'checks':checks,
    'groups':len(checks),
    'scalar_entries':sum(x['entries'] for x in checks),
    'scope':'Exact coefficient-boundary calculation; z=0 is inverse-period zero, never a finite original period. All four nontrivial fifth-root factors are retained.',
    'real_phase':{'xi4':str(a),'xi_z':str(c),'z2':str(d)},
    'second_phase':{'xi2':str(a2),'xi_z':str(c2),'z2':str(d2)},
    'R1':[[str(x) for x in row] for row in R[1].tolist()],
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(HERE/'ORIGINAL_PERIOD_BOUNDARY_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','groups':receipt['groups'],'scalar_entries':receipt['scalar_entries']}),flush=True)
