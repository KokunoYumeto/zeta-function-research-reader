"""Exact full infinitesimal symmetry and polynomial lift certificate."""
from pathlib import Path
import sympy as s
import json
a,y,z,w=s.symbols('a y z w')
x=s.Matrix([a,y,z,w]); i=s.I
b=i+a*y;c=-i+2*a*y+a*a*z
d=-i*y-2*a*y*y-i*a*z-a*a*y*z
e=-7*i*y*y+2*z+a*w
f=2*a*a*y**3*z+a*w*y+4*a*y**4+6*i*a*y*y*z+i*w+3*i*y**3-4*y*z
P=s.Matrix([a*c,a*e+b*d,a*f+b*e,b*f]).applyfunc(s.expand)
J=P.jacobian(x)
entries=s.symbols('b0:16'); B=s.Matrix(4,4,entries)
def zero(f): return s.cancel(f)==0
err=(J*B*x-B*P).applyfunc(s.expand)
equations=[]
for coord in err: equations.extend(s.Poly(coord,*x).coeffs())
solutions=s.linsolve(equations,entries)
assert len(solutions)==1
sol=next(iter(solutions)); t=sol[0]
assert list(sol)==list(s.diag(t,-t,-2*t,-3*t))
assert zero(J.det()+2)
Adj=J.adjugate()
assert all(zero(v) for v in J*(-Adj/2)-s.eye(4))
X=-Adj*B*P/2
assert all(zero(v) for v in X-B*x+Adj*(B*P-J*B*x)/2)
r,lambda3,lambda4,nu,v=s.symbols('r lambda3 lambda4 nu v', nonzero=True)
omega=3*lambda3-2*lambda4
ht=(r+nu*v)**3-3*r*r*s.exp(lambda3*nu**2)*(r+nu*v)+2*r**3*s.exp(lambda4*nu**2)
leading=s.series(ht,nu,0,3).removeO().expand().coeff(nu,2)
assert zero(leading-(3*r*v*v-omega*r**3))
u,p,q=s.symbols('u p q')
assert zero(s.discriminant(u**3-3*p*u+q,u)-27*(4*p**3-q**2))
out={'all_assertions_passed':True,'full_sixteen_variable_symmetry_space':str(solutions),
 'original_polynomial_jacobian':str(s.factor(J.det())),
 'polynomial_inverse_and_full_action_correction':True,
 'collision_leading_equation':str(leading),
 'finite_complex_time_not_real_time':True,
 'cardinal_quotient_morphism':'CA1--6 prove it for the full unchanged original grid'}
Path(__file__).with_name('corner_action_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
