"""Independent exact source-coordinate/profile audit, no author code imported."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
TEX=ROOT/'agents/ns_scaling_bridge/ns_scaling_bridge.tex'
text=TEX.read_text()
subsection=text.split('\\subsection{The exact source coordinates and differential operators}',1)[1].split('\\subsection{The material base',1)[0]
Q,X=s.symbols('Q X',positive=True)
xi,h,w,nu=s.symbols('xi h w nu',real=True)
A=s.Rational(1,2)+h
D=s.Rational(1,2)-h
d=1-xi**2
ell=1-2*h*xi**2
rho=s.sqrt(2*Q*X)
coords=s.Matrix([Q*d,Q**D*xi,Q*X])  # tau,z,sigma; sigma=rho^2/2
variables=(Q,xi,X)
J=coords.jacobian(variables)
inverse=J.inv()
checks=[]

def canonical(expr):
    return s.simplify(s.factor(s.powsimp(s.expand(expr),force=True)))

def check(name,expr):
    reduced=canonical(expr)
    assert reduced==0,(name,reduced)
    checks.append(name)

Dt=s.Matrix([-1/ell,D*xi/(Q*ell),X/(Q*ell)])
Dz=s.Matrix([2*xi*Q**(1-D)/ell,d/(Q**D*ell),-2*xi*X/(Q**D*ell)])
Dr=s.Matrix([0,0,rho/Q])
for i,var in enumerate(variables):
    check('inverse_jacobian_dt_'+str(var),Dt[i]+inverse[i,0])
    check('inverse_jacobian_dz_'+str(var),Dz[i]-inverse[i,1])
    check('inverse_jacobian_dr_'+str(var),Dr[i]-rho*inverse[i,2])
check('time_axial_jacobian',s.det(J[:2,:2])-Q**D*ell)

def field(coeffs,f):
    return sum(c*s.diff(f,v) for c,v in zip(coeffs,variables))

def dt(f): return field(Dt,f)
def dz(f): return field(Dz,f)
def dr(f): return field(Dr,f)

for first,second,n1,n2 in [(dt,dz,'t','z'),(dt,dr,'t','rho'),(dz,dr,'z','rho')]:
    for var in variables:
        check('commuting_'+n1+'_'+n2+'_'+str(var),first(second(var))-second(first(var)))

def T(v,f): return (-v*f+D*xi*s.diff(f,xi)+X*s.diff(f,X))/ell
def Z(v,f): return (2*v*xi*f+d*s.diff(f,xi)-2*xi*X*s.diff(f,X))/ell
def R(f): return 2*X*s.diff(f,X,2)+2*s.diff(f,X)
def R1(f): return R(f)-f/(2*X)

f=s.Function('f')(X,xi)
check('time_profile',dt(Q**w*f)-Q**(w-1)*T(w,f))
check('axial_profile',dz(Q**w*f)-Q**(w-D)*Z(w,f))
check('radial_profile',dr(dr(Q**w*f))+dr(Q**w*f)/rho-Q**(w-1)*R(f))
check('second_time_profile',dt(dt(Q**w*f))-Q**(w-2)*T(w-1,T(w,f)))
check('second_axial_profile',dz(dz(Q**w*f))-Q**(w-2*D)*Z(w-D,Z(w,f)))
check('axial_diffusion_exponent',w-2*D-(w-1+2*h))

primitive=s.Function('J')(X,xi)
U_primitive=s.diff(primitive,X)
V_integrated=(2*xi*X*U_primitive-2*D*xi*primitive-d*s.diff(primitive,xi))/ell
check('integrated_incompressibility',s.diff(V_integrated,X)+Z(-A,U_primitive))

E=s.Function('E')(X,xi)
U=s.Function('U')(X,xi)
V=s.Function('V0')(X,xi)
Pi=s.Function('Pi')(X,xi)
fr=V/s.sqrt(2*X)
ur=Q**s.Rational(-1,2)*fr
utheta=Q**(-A)*E
uz=Q**(-A)*U
pressure=Q**(-2*A)*Pi

def material(f): return dt(f)+ur*dr(f)+uz*dz(f)
def M(v,f): return T(v,f)+V*s.diff(f,X)+U*Z(v,f)
def lap(f): return dr(dr(f))+dr(f)/rho+dz(dz(f))

check('material_profile',material(Q**w*f)-Q**(w-1)*M(w,f))
check('divergence_profile',dr(rho*ur)/rho+dz(uz)-Q**(-1)*(s.diff(V,X)+Z(-A,U)))
check('radial_pressure_cancel',(dr(pressure)-utheta**2/rho).subs(s.diff(Pi,X),E**2/(2*X)))
check('radial_cancelled_exponent',-2*A-s.Rational(1,2)-(-s.Rational(3,2)-2*h))
check('axial_pressure_exponent',-2*A-D-(-A-1))

radial=material(ur)-utheta**2/rho-nu*(lap(ur)-ur/rho**2)+dr(pressure)
radial=radial.subs(s.diff(Pi,X),E**2/(2*X))
azimuthal=material(utheta)+ur*utheta/rho-nu*(lap(utheta)-utheta/rho**2)
axial=material(uz)-nu*lap(uz)+dz(pressure)
radial_claim=Q**s.Rational(-3,2)*(M(s.Rational(-1,2),fr)-nu*R1(fr))-nu*Q**(-s.Rational(3,2)+2*h)*Z(-s.Rational(1,2)-D,Z(-s.Rational(1,2),fr))
azimuthal_claim=Q**(-A-1)*(M(-A,E)+V*E/(2*X)-nu*R1(E))-nu*Q**(-A-1+2*h)*Z(-A-D,Z(-A,E))
axial_claim=Q**(-A-1)*(M(-A,U)-nu*R(U)+Z(-2*A,Pi))-nu*Q**(-A-1+2*h)*Z(-A-D,Z(-A,U))
check('full_radial_vector_residual',radial-radial_claim)
check('full_azimuthal_vector_residual',azimuthal-azimuthal_claim)
check('full_axial_vector_residual',axial-axial_claim)

receipt={'status':'pass','checks':checks,'check_count':len(checks),
         'author_tex_sha256_at_audit':sha256(TEX.read_bytes()).hexdigest(),
         'audited_first_subsection_sha256':sha256(subsection.encode()).hexdigest(),
         'scope':'Only first concentration-profile subsection: inverse coordinates, physical derivative fields, profile operators, incompressibility, material derivative and all vector residuals.',
         'domain':'0<h<1/2, Q>0, X>0, -1<xi<1; smooth-axis extension handled in proof note.',
         'method':'Independent exact inverse Jacobian and symbolic arbitrary-profile derivative calculations. Power combination is valid because Q and X are positive real.'}
(HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'pass','checks':len(checks),'subsection_sha256':receipt['audited_first_subsection_sha256']}))
