"""Exact checks for RD1--29; the proof is RESIDUE_DUALITY_BODY.tex."""
from pathlib import Path
import hashlib
import json
import sympy as s

BASE = Path(__file__).resolve().parent
checks = []
def zero(name, value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    bad = [s.factor(x) for x in entries if s.factor(x) != 0]
    if bad:
        raise ArithmeticError((name, bad[:3]))
    checks.append({"name": name, "scalar_entries": len(entries), "passed": True})

A, B, C, D, r = s.symbols('A B C D r')
h = A*r**4 + r**3 + B*r**2 + C*r + D
rem = lambda f: s.rem(f, h, r)
lam = lambda f: s.Poly(rem(f), r).nth(3)/A
coeff = lambda f: s.Matrix([s.Poly(rem(f), r).nth(j) for j in range(4)])
mul = lambda f: s.Matrix.hstack(*[coeff(f*r**j) for j in range(4)])
H = s.Matrix(4, 4, lambda i,j: lam(r**(i+j)))
J = s.Matrix([[C,B,1,A],[B,1,A,0],[1,A,0,0],[A,0,0,0]])
Bu = s.zeros(4).row_join(H).col_join(H.row_join(s.zeros(4)))
Bi = s.zeros(4).row_join(J).col_join(J.row_join(s.zeros(4)))
zero('RD3 inverse', Bu*Bi-s.eye(8))
zero('RD4 determinant', Bu.det()-A**-8)
Z = mul(r)
L = mul(s.diff(h,r))
zero('RD7 derivative multiplication', L-(4*A*Z**3+3*Z**2+2*B*Z+C*s.eye(4)))
Mt = s.zeros(4).row_join(L).col_join(s.eye(4).row_join(s.zeros(4)))
Md = 2*Mt**3
Mb = [s.diag(mul(r**j),mul(r**j)) for j in range(4)]
Mb += [Mt*Mb[j] for j in range(4)]
Tr = s.Matrix(8,8,lambda i,j: s.trace(Mb[i]*Mb[j]))
zero('RD6 full trace comparison', Tr-Bu*Md)
disc = s.discriminant(h,r)
zero('RD8 derivative determinant', L.det()-disc/A**2)

ep = s.symbols('epsilon')
local = []
for m in (2,3,4):
    gs = s.symbols('g0:'+str(m))
    gg = sum(gs[k]*ep**k for k in range(m))
    inv = s.series(1/gg,ep,0,m).removeO()
    Hm = s.Matrix(m,m,lambda i,j: s.expand(inv).coeff(ep,m-1-i-j) if i+j<=m-1 else 0)
    Gm = s.Matrix(m,m,lambda i,j: gs[i+j-m+1] if i+j>=m-1 else 0)
    zero(f'RD11 local dual vectors m={m}',Hm*Gm-s.eye(m))
    zero(f'RD10 determinant m={m}',(-1)**m*Hm.det()**2-(-1)**m/gs[0]**(2*m))
    Ne = s.zeros(m)
    for j in range(m-1): Ne[j+1,j]=1
    Lm=m*gs[0]*Ne**(m-1)
    Nt=s.zeros(m).row_join(Lm).col_join(s.eye(m).row_join(s.zeros(m)))
    BM=s.zeros(m).row_join(Hm).col_join(Hm.row_join(s.zeros(m)))
    expected=s.zeros(2*m);expected[0,0]=2*m
    zero(f'RD12 complete local trace m={m}',BM*(2*Nt**3)-expected)
    zero(f'RD12 t fourth power m={m}',Nt**4)
    local.append({'multiplicity':m,'dimension':2*m,'trace_rank':1,'residue_rank':2*m})

g = s.symbols('gamma',positive=True)
xx, xp = s.symbols('X Xprime')
for eta in (1,-1):
    ll=s.I*eta/(2*g**3)
    BB=s.Matrix([[0,ll,0,2],[ll,0,2,0],[0,2,0,0],[2,0,0,0]])
    zero(f'RD14 determinant eta={eta}',BB.det()-16)
    f=s.Matrix([xx,0,-s.I*eta*xp/(4*g**2),0])
    v1=s.Matrix([0,1,0,0]);v3=s.Matrix([0,0,0,1])
    m1=(f.T*BB*v1)[0];m3=(f.T*BB*v3)[0]
    zero(f'RD16 value eta={eta}',m3/2-xx)
    zero(f'RD16 derivative eta={eta}',2*s.I*eta*g**2*(m1-s.I*eta*m3/(4*g**3))-xp)
    rr=s.Rational(1,2)+s.I*eta*g;dd=2*s.I*eta*g
    ee=(r-(s.Rational(1,2)-s.I*eta*g))**2/dd**2*(1-2*(r-rr)/dd)
    h0=-s.Rational(1,2)*((r-s.Rational(1,2))**2+g**2)**2
    zero(f'RD17 projector eta={eta}',s.rem(s.expand(ee*ee-ee),h0,r))

aa,bb,cc,dd,ee,R,p,k=s.symbols('aa bb cc dd ee R p kappa')
hh=aa*R**4+bb*R**3+cc*R**2+dd*R+ee
ll=lambda f:s.Poly(s.rem(f,hh,R),R).nth(3)/aa
HH=s.Matrix(4,4,lambda i,j:ll(R**(i+j)))
JJ=s.Matrix([[dd,cc,bb,aa],[cc,bb,aa,0],[bb,aa,0,0],[aa,0,0,0]])
zero('RD25 general retained coefficient inverse',HH*JJ-s.eye(4))
Zp=s.Matrix(4,4,lambda i,j:s.Poly(s.expand(R**(3-j)*((p+k)*R-1)**j),R).nth(i))
zero('RD27 coefficient determinant',Zp.det()-1)
sp=s.symbols('Sprime')
for j in range(4):
    zz=R**(3-j)*((p+k)*R-1)**j
    zero(f'RD27 polynomial inverse j={j}',(p+k-sp)**3*zz.subs(R,1/(p+k-sp))-sp**j)
hp=s.expand((2*R-1)**3*R-(2*R-1)*R**3)
zero('RD29 exact polynomial',hp-(6*R**4-11*R**3+6*R**2-R))
zero('RD29 discriminant',s.discriminant(hp,R)-4)

# Check RD26 and RD28 on a symbolic rational transition modulo a
# specific square-free quartic; universal proofs are in the TeX.
ht=r**4+r**3-2*r**2+3*r-1
hpt=s.expand(R**4*ht.subs(r,2-1/R))
hpcoeff=s.Poly(hpt,R).LC()
def lpf(f):
    num,den=s.fraction(s.cancel(f))
    val=s.rem(num*s.invert(den,hpt,R),hpt,R)
    return s.Poly(val,R).nth(3)/hpcoeff
def lff(f):
    num,den=s.fraction(s.cancel(f))
    val=s.rem(num*s.invert(den,ht,r),ht,r)
    return s.Poly(val,r).nth(3)
for j in range(7):
    zero(f'RD26 rational overlap monomial{j}',lff(r**j)-lpf(R**2*(2-1/R)**j))
    zero(f'RD28 physical overlap monomial{j}',lpf(R**6*(2-1/R)**j)-lff(r**j/(2-r)**4))

out={'proof':'RESIDUE_DUALITY_BODY.tex','proof_sha256':hashlib.sha256((BASE/'RESIDUE_DUALITY_BODY.tex').read_bytes()).hexdigest(),
     'checks':checks,'check_groups':len(checks),'scalar_entries':sum(x['scalar_entries'] for x in checks),
     'local_fibres':local,'scope':'Exact algebraic identities RD1--29. The general residue and conductor proofs are in the TeX; the chart rational sample supplements those proofs.'}
(BASE/'RESIDUE_DUALITY_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('check_groups','scalar_entries','proof_sha256')}))
