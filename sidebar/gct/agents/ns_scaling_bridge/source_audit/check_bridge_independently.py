"""Independent exact algebra audit of the parent's NS/conic transport formulas."""
from pathlib import Path
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parent
Q, X = S.symbols('Q X', positive=True)
xi, h, w, nu = S.symbols('xi h w nu', real=True)
A = S.Rational(1,2)+h
D = S.Rational(1,2)-h
d = 1-xi**2
ell = 1-2*h*xi**2
rho = S.sqrt(2*Q*X)
E,U,V,Pi,f = [S.Function(n)(X,xi) for n in ['E','U','V','Pi','f']]
results = []

def check(name, expression):
    exact = S.simplify(S.powsimp(S.expand(expression), force=True))
    assert exact == 0, (name, exact)
    results.append(name)

def dt(g):
    return (-S.diff(g,Q)+D*xi/Q*S.diff(g,xi)+X/Q*S.diff(g,X))/ell

def dz(g):
    return (2*xi*Q**(1-D)*S.diff(g,Q)+d*Q**(-D)*S.diff(g,xi)-2*xi*X*Q**(-D)*S.diff(g,X))/ell

def dr(g):
    return rho/Q*S.diff(g,X)

def T(a,g):
    return (-a*g+D*xi*S.diff(g,xi)+X*S.diff(g,X))/ell

def Z(a,g):
    return (2*a*xi*g+d*S.diff(g,xi)-2*xi*X*S.diff(g,X))/ell

def R(g):
    return 2*X*S.diff(g,X,2)+2*S.diff(g,X)

def R1(g):
    return R(g)-g/(2*X)

def M(a,g):
    return T(a,g)+V*S.diff(g,X)+U*Z(a,g)

def lap(g):
    return dr(dr(g))+dr(g)/rho+dz(dz(g))

ur=Q**(-S.Rational(1,2))*V/S.sqrt(2*X)
utheta=Q**(-A)*E
uz=Q**(-A)*U
pressure=Q**(-2*A)*Pi

def material(g):
    return dt(g)+ur*dr(g)+uz*dz(g)

check('weighted physical time chain rule', dt(Q**w*f)-Q**(w-1)*T(w,f))
check('weighted physical axial chain rule', dz(Q**w*f)-Q**(w-D)*Z(w,f))
check('weighted radial scalar Laplacian', dr(dr(Q**w*f))+dr(Q**w*f)/rho-Q**(w-1)*R(f))
check('physical leading material derivative', material(Q**w*f)-Q**(w-1)*M(w,f))

fr=V/S.sqrt(2*X)
radial_raw=material(ur)-utheta**2/rho-nu*(lap(ur)-ur/rho**2)+dr(pressure)
radial_claim=Q**(-S.Rational(3,2))*(M(-S.Rational(1,2),fr)-nu*R1(fr))-nu*Q**(-S.Rational(3,2)+2*h)*Z(-S.Rational(1,2)-D,Z(-S.Rational(1,2),fr))
check('full radial residual under stated centrifugal pressure identity', (radial_raw-radial_claim).subs(S.diff(Pi,X),E**2/(2*X)))
azimuthal_raw=material(utheta)+ur*utheta/rho-nu*(lap(utheta)-utheta/rho**2)
azimuthal_claim=Q**(-A-1)*(M(-A,E)+V*E/(2*X)-nu*R1(E))-nu*Q**(-A-1+2*h)*Z(-A-D,Z(-A,E))
check('full azimuthal residual including cylindrical frame terms',azimuthal_raw-azimuthal_claim)
axial_raw=material(uz)-nu*lap(uz)+dz(pressure)
axial_claim=Q**(-A-1)*(M(-A,U)-nu*R(U)+Z(-2*A,Pi))-nu*Q**(-A-1+2*h)*Z(-A-D,Z(-A,U))
check('full axial residual including pressure and axial viscosity',axial_raw-axial_claim)

# Check the added viscosity transport on the actual rescaled field, with
# positive viscosity kept separate from the earlier arbitrary residual parameter.
viscosity=S.symbols('viscosity',positive=True)
rootnu=S.sqrt(viscosity)
rho_nu=rootnu*rho
drnu=lambda g:dr(g)/rootnu
dznu=lambda g:dz(g)/rootnu
lapnu=lambda g:drnu(drnu(g))+drnu(g)/rho_nu+dznu(dznu(g))
ur_nu,utheta_nu,uz_nu,pressure_nu=rootnu*ur,rootnu*utheta,rootnu*uz,viscosity*pressure
materialnu=lambda g:dt(g)+ur_nu*drnu(g)+uz_nu*dznu(g)
radial_rescaled=materialnu(ur_nu)-utheta_nu**2/rho_nu-viscosity*(lapnu(ur_nu)-ur_nu/rho_nu**2)+drnu(pressure_nu)
azimuthal_rescaled=materialnu(utheta_nu)+ur_nu*utheta_nu/rho_nu-viscosity*(lapnu(utheta_nu)-utheta_nu/rho_nu**2)
axial_rescaled=materialnu(uz_nu)-viscosity*lapnu(uz_nu)+dznu(pressure_nu)
check('viscosity covariance of full radial residual',radial_rescaled-rootnu*radial_raw.subs(nu,1))
check('viscosity covariance of full azimuthal residual',azimuthal_rescaled-rootnu*azimuthal_raw.subs(nu,1))
check('viscosity covariance of full axial residual',axial_rescaled-rootnu*axial_raw.subs(nu,1))
check('rescaled coordinate axial derivative factor',dznu(Q**w*f)-Q**(w-D)*Z(w,f)/rootnu)
check('rescaled coordinate radial Laplacian factor',drnu(drnu(Q**w*f))+drnu(Q**w*f)/rho_nu-Q**(w-1)*R(f)/viscosity)
check('divergence unchanged under viscosity scaling',drnu(ur_nu)+ur_nu/rho_nu+dznu(uz_nu)-dr(ur)-ur/rho-dz(uz))

s,b=S.symbols('s b')
beta=b/4
m=b**2/16-2*s
n=m+4
Hs=S.diag(0,-1/m,-1/n,-1/m-1/n)
Hb=-b/16*Hs
B=S.Matrix([[1,beta,0,0],[0,1,0,0],[0,0,1,beta],[0,0,0,1]])
Gs=S.Matrix([[0,beta/m,0,0],[0,-1/m,0,0],[0,0,-1/n,beta/m],[0,0,0,-1/m-1/n]])
Gb=S.Matrix([[0,S.Rational(1,4)-b*beta/(16*m),0,0],[0,b/(16*m),0,0],[0,0,b/(16*n),S.Rational(1,4)-b*beta/(16*m)],[0,0,0,b/(16*m)+b/(16*n)]])
for variable,H,G in [(s,Hs,Gs),(b,Hb,Gb)]:
    for i,expression in enumerate(G-B.inv()*H*B-B.inv()*B.diff(variable)):
        check(f'connection change of basis {variable} entry {i}',expression)
curvature=Gb.diff(s)-Gs.diff(b)+Gs*Gb-Gb*Gs
for i,entry in enumerate(curvature):
    check(f'connection curvature entry {i}',entry)
Js=S.diag(0,-1/m**2,-1/n**2,-1/m**2-1/n**2+2/(m*n))
Jb=S.diag(0,1/(16*m)-b**2/(256*m**2),1/(16*n)-b**2/(256*n**2),(1/m+1/n)/16-b**2*(1/m**2+1/n**2)/256+b**2/(128*m*n))
for variable,H,J in [(s,Hs,Js),(b,Hb,Jb)]:
    for i,entry in enumerate(J-H.diff(variable)-H*H):
        check(f'complete second derivative {variable} entry {i}',entry)

q,tau,p=S.symbols('q tau p', nonzero=True)
qint=lambda k: sum(q**j for j in range(k-1,-k,-2))
C=q**10-q**4-q**(-4)+q**(-10)
check('GCT full Laurent factorization',C-(q-1/q)**2*qint(7)*qint(3))
check('quantum integer three in p',qint(3)-((q+1/q)**2-1))
check('quantum integer seven in p',qint(7)-((q+1/q)**6-5*(q+1/q)**4+6*(q+1/q)**2-1))
factor=-2*tau*(3-2*tau)*(7-28*tau+28*tau**2-8*tau**3)
Bpoly=-42+196*tau-280*tau**2+160*tau**3-32*tau**4
check('coefficient full tau polynomial',factor-tau*Bpoly)
check('p polynomial under retained unit circle relation',(-2*tau*(p**2-1)*(p**6-5*p**4+6*p**2-1)).subs(p**2,4-2*tau)-factor)
check('scalar-germ exact exponent',1-A-D)
check('positive real unit-circle norm identity',(4-2*tau+2*tau)/4-1)
assert Bpoly.subs(tau,0)==-42
results.append('coefficient derivative at zero equals minus forty-two')

proof=ROOT.parent/'ns_scaling_bridge.tex'
receipt={
    'status':'passed',
    'proof_path':proof.as_posix(),
    'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
    'checks':len(results),
    'check_names':results,
    'scope':'Exact symbolic independent operator/residual/connection/polynomial identities. Does not verify the complete external NS theorem.',
}
(ROOT/'independent_formula_checks.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':receipt['status'],'checks':len(results),'proof_sha256':receipt['proof_sha256']}))
