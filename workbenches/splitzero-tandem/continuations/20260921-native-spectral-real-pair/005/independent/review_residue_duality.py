"""Independent exact checks of RD1--29; no numerical approximation."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'RESIDUE_DUALITY_BODY.tex'
checks = []

def zero(expr):
    if isinstance(expr, s.MatrixBase):
        return all(s.cancel(v) == 0 for v in expr)
    return s.cancel(expr) == 0

def check(name, expr):
    assert zero(expr), (name, expr)
    checks.append(name)

r, R, x, y = s.symbols('r R x y')
A, B, C, D = s.symbols('A B C D', nonzero=True)
a, b, c, d, e = s.symbols('a b c d e', nonzero=True)
h = A*r**4+r**3+B*r**2+C*r+D
H = s.Matrix([[0,0,0,1/A], [0,0,1/A,-1/A**2],
              [0,1/A,-1/A**2,1/A**3-B/A**2],
              [1/A,-1/A**2,1/A**3-B/A**2,-1/A**4+2*B/A**3-C/A**2]])
J = s.Matrix([[C,B,1,A],[B,1,A,0],[1,A,0,0],[A,0,0,0]])
check('RD3 left inverse', H*J-s.eye(4))
check('RD3 right inverse', J*H-s.eye(4))
check('RD3 Bezout coefficients', (s.Matrix([1,x,x*x,x**3]).T*J*s.Matrix([1,y,y*y,y**3]))[0] - (h.subs(r,x)-h.subs(r,y))/(x-y))
check('RD4 determinant H', H.det()-A**-4)
BB = s.BlockMatrix([[s.zeros(4),H],[H,s.zeros(4)]]).as_explicit()
check('RD4 determinant B', BB.det()-A**-8)
Z = s.Matrix([[0,0,0,-D/A],[1,0,0,-C/A],[0,1,0,-B/A],[0,0,1,-1/A]])
L = 4*A*Z**3+3*Z**2+2*B*Z+C*s.eye(4)
Mt = s.BlockMatrix([[s.zeros(4), L], [s.eye(4), s.zeros(4)]]).as_explicit()
Md = 2*Mt**3
check('RD5 multiplication 2t^3', Md-2*s.BlockMatrix([[s.zeros(4),L**2],[L,s.zeros(4)]]).as_explicit())
check('RD6 full trace matrix', BB*Md-2*s.diag(H*L,H*L**2))
check('RD7 derivative determinant', L.det()-s.discriminant(h,r)/A**2)

hp = a*R**4+b*R**3+c*R**2+d*R+e
Hp = H.subs({A:a,B:c,C:d}, simultaneous=True)
# The original cubic coefficient was 1, so insert all powers of b explicitly.
Hp = s.Matrix([[0,0,0,1/a],[0,0,1/a,-b/a**2],
 [0,1/a,-b/a**2,b*b/a**3-c/a**2],
 [1/a,-b/a**2,b*b/a**3-c/a**2,-b**3/a**4+2*b*c/a**3-d/a**2]])
Jp = s.Matrix([[d,c,b,a],[c,b,a,0],[b,a,0,0],[a,0,0,0]])
check('RD25 general chart inverse', Hp*Jp-s.eye(4))
check('RD25 general chart determinant', Hp.det()-a**-4)

eps = s.symbols('eps')
for m in (2,3,4):
    gs = s.symbols('g0:'+str(5-m))
    g = sum(gs[k]*eps**k for k in range(len(gs)))
    invg = s.series(1/g,eps,0,m).removeO()
    lam = lambda q: s.expand(q*invg).coeff(eps,m-1)
    Hm = s.Matrix(m,m,lambda i,j: lam(eps**(i+j)))
    Bm = s.BlockMatrix([[s.zeros(m),Hm],[Hm,s.zeros(m)]]).as_explicit()
    check(f'RD10 local determinant m={m}', Bm.det()-(-1)**m*gs[0]**(-2*m))
    for j in range(m):
        for k in range(m):
            check(f'RD11 coefficient test m={m} j={j} k={k}', lam(eps**k*eps**(m-1-j)*g)-int(j==k))
    Em = s.zeros(m)
    for j in range(m-1): Em[j+1,j] = 1
    Lm = m*gs[0]*Em**(m-1)
    Mtm = s.BlockMatrix([[s.zeros(m),Lm],[s.eye(m),s.zeros(m)]]).as_explicit()
    Dm = 2*Mtm**3
    assert Dm.rank() == 1
    check(f'RD12 trace rank-one matrix m={m}', Bm*Dm-s.diag(2*m,*([0]*(2*m-1))))

gam = s.symbols('gamma', positive=True)
X, Xp = s.symbols('X Xprime')
for eta in (-1,1):
    I = s.I
    g = -s.Rational(1,2)*(eps+2*I*eta*gam)**2
    invg = s.series(1/g,eps,0,2).removeO()
    Lt = s.expand(invg).coeff(eps,1)
    Lt3 = 4*gam**2*s.expand(eps*invg).coeff(eps,1)
    check(f'RD14 Lambda t eta={eta}',Lt-I*eta/(2*gam**3))
    check(f'RD14 Lambda t3 eta={eta}',Lt3-2)
    Beta=s.Matrix([[0,Lt,0,2],[Lt,0,2,0],[0,2,0,0],[2,0,0,0]])
    check(f'RD14 determinant eta={eta}',Beta.det()-16)
    mt = X*Lt-I*eta*Xp/(2*gam**2)
    mt3 = 2*X
    check(f'RD16 derivative recovery eta={eta}',2*I*eta*gam**2*(mt-I*eta*mt3/(4*gam**3))-Xp)
    reta=s.Rational(1,2)+I*eta*gam
    rother=s.Rational(1,2)-I*eta*gam
    de=2*I*eta*gam
    proj=(r-rother)**2/de**2*(1-2*(r-reta)/de)
    check(f'RD17 selected jet eta={eta}',s.rem(proj-1,(r-reta)**2,r))
    check(f'RD17 other jet eta={eta}',s.rem(proj,(r-rother)**2,r))

q, sp = s.symbols('q sp')
Zp=s.Matrix(4,4,lambda i,j:s.expand(R**(3-j)*(q*R-1)**j).coeff(R,i))
check('RD27 receiver determinant',Zp.det()-1)
for j in range(4):
    F=s.expand(R**(3-j)*(q*R-1)**j)
    check(f'RD27 inverse monomial j={j}',(q-sp)**3*F.subs(R,1/(q-sp))-sp**j)

def rem(poly, modulus, var): return s.rem(s.cancel(poly),modulus,var)
def lam_global(poly, modulus, var):
    return s.expand(rem(poly,modulus,var)).coeff(var,3)/s.Poly(modulus,var).LC()

# Repeated roots are included in these exact overlap tests.
examples = [
 ('simple',r**4+r**3-7*r**2+2*r+3),
 ('double',(r-1)**2*(r+1)*(r+2)),
 ('triple',(r-1)**3*(r+4)),
 ('quadruple',(r+s.Rational(1,4))**4),
]
for name, hu in examples:
    hu=s.expand(hu)
    for p in (0,1,-1,2):
        if hu.subs(r,p)==0: continue
        huprime=s.diff(hu,r)
        transformed=s.cancel(R**4*hu.subs(r,p-1/R)).expand()
        invR=s.invert(R,transformed,R)
        ri=rem(p-invR,transformed,R)
        multiplier=s.invert((p-r)**4,hu,r)
        for i in range(4):
            iota_odd=rem(ri**i*invR,transformed,R)
            check(f'RD26 residue {name} p={p} i={i}',lam_global(r**i,hu,r)-lam_global(R**3*iota_odd,transformed,R))
            Fi=s.expand(R**(3-i)*(p*R-1)**i)
            for j in range(4):
                Fj=s.expand(R**(3-j)*(p*R-1)**j)
                check(f'RD28 pulled pairing {name} p={p} i={i} j={j}',lam_global(Fi*Fj,transformed,R)-lam_global(multiplier*r**(i+j),hu,r))
        # Establish trace formula on all eight basis elements without roots.
        hlead=s.Poly(hu,r).LC()
        Mr=s.zeros(4)
        for j in range(4):
            v=rem(r**(j+1),hu,r)
            Mr[:,j]=s.Matrix([v.coeff(r,i) for i in range(4)])
        for j in range(4):
            check(f'RD6 trace residue {name} power={j}',s.trace(Mr**j)-lam_global(huprime*r**j,hu,r))

h2=6*R**4-11*R**3+6*R**2-R
check('RD29 polynomial factorization',h2-R*(R-1)*(2*R-1)*(3*R-1))
check('RD29 discriminant',s.discriminant(h2,R)-4)
check('RD29 infinity sign equation',s.diff(h2,R).subs(R,0)+1)

result={'source':SOURCE.name,'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'result':'PASS','exact_checks':len(checks),'checks':checks,
 'coverage':'RD3--17 and RD24--29 exact algebra; RD18--23 reviewed by independent block-matrix derivation.'}
(HERE/'RESIDUE_DUALITY_REVIEW_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
