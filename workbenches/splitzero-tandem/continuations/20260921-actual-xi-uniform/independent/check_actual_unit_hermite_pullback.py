"""Exact algebra checks for AUH; the complete analytic proofs are in its TeX."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []

def zero(name, expr):
    if isinstance(expr, s.MatrixBase):
        entries = list(expr)
    elif isinstance(expr, (list, tuple)):
        entries = list(expr)
    else:
        entries = [expr]
    failed = [str(e) for e in entries if s.cancel(s.expand(e)) != 0]
    if failed:
        raise AssertionError((name, failed[:3]))
    checks.append({"name": name, "entries": len(entries), "passed": True})

lp, lm, y, w = s.symbols('lambda_plus lambda_minus y w')
d = lp-lm
beta, eta = -lp-lm, lp*lm
fp, fm, fpp, fpm = s.symbols('f_plus f_minus f_prime_plus f_prime_minus')
l1 = (fp-fm)/d
l0 = (lp*fm-lm*fp)/d
ap = (fpp-l1)/d
am = -(fpm-l1)/d
m1 = (ap-am)/d
m0 = (lp*am-lm*ap)/d
L, H, M = l0+l1*y, (y-lp)*(y-lm), m0+m1*y
J = L+H*M
zero('AUH3 original-value interpolation', [L.subs(y,lp)-fp,L.subs(y,lm)-fm])
zero('AUH5 and AUH10 all four Hermite jets', [
    J.subs(y,lp)-fp,J.subs(y,lm)-fm,
    s.diff(J,y).subs(y,lp)-fpp,s.diff(J,y).subs(y,lm)-fpm])
jet_inverse = s.Matrix([[1,lp,0,0],[1,lm,0,0],[0,1,d,0],[0,1,0,-d]])
zero('AUH7 full four-jet inverse determinant', jet_inverse.det()-d**3)
to_values = s.Matrix([[1,lp],[1,lm]])
zero('AUH10 residual-and-linear-unit jet determinant',
     jet_inverse.det()*to_values.det()+d**4)

for degree in range(10):
    F=y**degree
    LL=s.cancel(((y-lm)*F.subs(y,lp)-(y-lp)*F.subs(y,lm))/d)
    QQ=s.cancel((F-LL)/H)
    aa=s.cancel((s.diff(F,y).subs(y,lp)-s.diff(LL,y))/d)
    ab=s.cancel(-(s.diff(F,y).subs(y,lm)-s.diff(LL,y))/d)
    MM=s.cancel(((y-lm)*aa-(y-lp)*ab)/d)
    zero(f'AUH3 exact division on monomial degree {degree}', F-LL-H*QQ)
    zero(f'AUH9 actual quotient interpolation on monomial degree {degree}',
         [QQ.subs(y,lp)-aa,QQ.subs(y,lm)-ab])
    _, rem=s.div(s.cancel(F-LL-H*MM),s.expand(H**2),y)
    zero(f'AUH10 double divisibility on monomial degree {degree}',rem)

bb, ee, mm0, mm1, ll0, ll1 = s.symbols('beta eta m0 m1 ell0 ell1')
hc = w**4+bb*w**2+ee
def matmul_primary(c0,c1):
    return s.Matrix([[c0,0,-ee*c1,0], [0,c0,0,-ee*c1],
                     [c1,0,c0-bb*c1,0], [0,c1,0,c0-bb*c1]])

MM=matmul_primary(mm0,mm1)
LL=matmul_primary(ll0,ll1)
for j in range(4):
    rem=s.rem((mm0+mm1*w**2)*w**j,hc,w)
    zero(f'AUH12 original primary column {j}',
         [MM[i,j]-rem.coeff(w,i) for i in range(4)])
kappa=mm0**2-bb*mm0*mm1+ee*mm1**2
MI=matmul_primary((mm0-bb*mm1)/kappa,-mm1/kappa)
zero('AUH12 determinant',MM.det()-kappa**2)
zero('AUH13 both exact unit inverse products',list(MM*MI-s.eye(4))+list(MI*MM-s.eye(4)))
T=s.Matrix(4,4,lambda r,c:s.binomial(c,r)*s.Rational(1,2)**(c-r) if r<=c else 0)
Ti=s.Matrix(4,4,lambda r,c:s.binomial(c,r)*s.Rational(-1,2)**(c-r) if r<=c else 0)
zero('AUH14 original half-translation and inverse',list(T*Ti-s.eye(4))+list(Ti*T-s.eye(4)))
wp_general,wm_general=s.symbols('w_plus w_minus')
nodes_general=[wp_general,wm_general,-wm_general,-wp_general]
bg=-wp_general**2-wm_general**2
eg=wp_general**2*wm_general**2
Vg=s.Matrix([[q**j for j in range(4)] for q in nodes_general])
Vgi=s.Matrix.hstack(*[s.Matrix([q**3+bg*q,q**2+bg,q,1])/
                      (4*q**3+2*bg*q) for q in nodes_general])
zero('AUH11 generic original-label Vandermonde inverse both ways',
     list(Vg*Vgi-s.eye(4))+list(Vgi*Vg-s.eye(4)))
zero('AUH11 generic ordered Vandermonde determinant',
     Vg.det()-4*wp_general*wm_general*(wp_general**2-wm_general**2)**2)
zero('AUH12 generic reflected unit diagonal',
     Vg*MM.subs({bb:bg,ee:eg})-s.diag(*[mm0+mm1*q**2 for q in nodes_general])*Vg)
KL=s.zeros(4); KL[0,2]=KL[1,3]=ll1
G8=LL.row_join(s.zeros(4)).col_join((MM+KL).row_join(LL))
polyjet=ll0+ll1*w**2+hc*(mm0+mm1*w**2)
for j in range(8):
    basis=w**j if j<4 else hc*w**(j-4)
    rem=s.rem(polyjet*basis,hc**2,w)
    p1,p0=s.div(rem,hc,w)
    expected=s.Matrix([p0.coeff(w,i) for i in range(4)]+[p1.coeff(w,i) for i in range(4)])
    zero(f'AUH15 eight-jet multiplication column {j}',G8[:,j]-expected)

delta=s.Rational(1,4); gamma=s.Integer(3)
wp=delta+s.I*gamma; wm=delta-s.I*gamma
ww=[wp,wm,-wm,-wp]
beta_value=2*(gamma**2-delta**2); eta_value=(delta**2+gamma**2)**2
V=s.Matrix([[q**j for j in range(4)] for q in ww])
Vi=s.Matrix.hstack(*[s.Matrix([q**3+beta_value*q,q**2+beta_value,q,1])/
                     (4*q**3+2*beta_value*q) for q in ww])
zero('AUH11 original-label Vandermonde inverse both ways',list(V*Vi-s.eye(4))+list(Vi*V-s.eye(4)))
zero('AUH11 original determinant at retained quartet',V.det()+64*delta**2*gamma**2*(delta**2+gamma**2))
Vp=s.Matrix([[0]+[j*q**(j-1) for j in range(1,4)] for q in ww])
Dh=s.diag(*[4*q**3+2*beta_value*q for q in ww])
J8=V.row_join(s.zeros(4)).col_join(Vp.row_join(Dh*V))
J8i=Vi.row_join(s.zeros(4)).col_join((-Vi*Dh.inv()*Vp*Vi).row_join(Vi*Dh.inv()))
zero('AUH16 jet coordinate inverse',J8*J8i-s.eye(8))
subs={bb:beta_value,ee:eta_value}
gval=[ll0+ll1*q**2 for q in ww]
gder=[2*q*ll1+(4*q**3+2*beta_value*q)*(mm0+mm1*q**2) for q in ww]
jet_product=s.diag(*gval).row_join(s.zeros(4)).col_join(s.diag(*gder).row_join(s.diag(*gval)))
zero('AUH16 full conjugation with every residual carry',J8*G8.subs(subs)-jet_product*J8)

x,r,c,z = s.symbols('x r c z', nonzero=True)
Jd=s.diag(1,-1,-1,1)
WR=s.eye(4)+s.I*x*Jd
WI=z*s.eye(4)+s.I*Jd
zero('AUH18 real-part chart inverse',WR*(s.eye(4)-s.I*x*Jd)/(1+x*x)-s.eye(4))
zero('AUH18 imaginary-part chart inverse',WI*(z*s.eye(4)-s.I*Jd)/(1+z*z)-s.eye(4))
zero('AUH19 overlap matrix morphism',WI.subs(z,1/x)-WR/x)

aa,ab=s.symbols('a_plus a_minus',nonzero=True)
p=s.symbols('p1:5');q=s.symbols('q1:5')
vectors=[aa*p[i]+ab*q[i] for i in range(4)]
literal=vectors[0]*vectors[3]/aa**2-vectors[1]*vectors[2]/ab**2
theta=ab/aa
laurent=p[0]*p[3]+theta*(p[0]*q[3]+q[0]*p[3])+theta**2*q[0]*q[3]
laurent-=theta**-2*p[1]*p[2]+theta**-1*(p[1]*q[2]+q[1]*p[2])+q[1]*q[2]
numerator=ab**2*vectors[0]*vectors[3]-aa**2*vectors[1]*vectors[2]
zero('AUH24 exact phase Laurent polynomial with all signs',literal-laurent)
zero('AUH25 chart-free denominator and full numerator',literal-numerator/(aa**2*ab**2))

# Differential checks regard the two original squared nodes as independent.
fp2,fm2,dlp,dlm=s.symbols('f_plus_second f_minus_second dlambda_plus dlambda_minus')
variables=(lp,lm,fp,fm,fpp,fpm)
variations=(dlp,dlm,fpp*dlp,fpm*dlm,fp2*dlp,fm2*dlm)
diff=lambda expr:sum(s.diff(expr,var)*val for var,val in zip(variables,variations))
dd=dlp-dlm
dl1=(fpp*dlp-fpm*dlm-l1*dd)/d
dap=(fp2*dlp-dl1-ap*dd)/d
dam=-(fm2*dlm-dl1+am*dd)/d
zero('AUH27 divided-difference variation',diff(l1)-dl1)
zero('AUH27 both amplitude variations',[diff(ap)-dap,diff(am)-dam])

source=HERE/'ACTUAL_UNIT_HERMITE_PULLBACK.tex'
receipt={
    'result':'PASS',
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'proof_file':source.name,
    'proof_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy_version':s.__version__,
    'check_groups':len(checks),
    'scalar_entries_checked':sum(c['entries'] for c in checks),
    'checks':checks,
    'scope':'Exact finite algebra checks; convergence, analytic division, source identity and the actual Xi graph are proved and read in the TeX. No root existence or arithmetic intersection is inferred from these checks.'
}
(HERE/'ACTUAL_UNIT_HERMITE_PULLBACK_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='checks'},indent=2))
