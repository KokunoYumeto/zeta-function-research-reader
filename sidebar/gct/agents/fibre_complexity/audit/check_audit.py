"""Exact symbolic replay of the field-degree audit's displayed identities.

Run: python check_audit.py
Uses only SymPy rational polynomial arithmetic. Written irreducibility,
integrality, chart-cover and finiteness arguments remain in audit.md.
"""

from pathlib import Path
import hashlib
import json
import sympy as s

x, y, w, a, b, c, r, h, t, z, lam = s.symbols("x y w a b c r h t z lam")
F = s.Matrix([
    (1+x*y)**3*w+y**2*(1+x*y)*(4+3*x*y),
    y+3*x*(1+x*y)**2*w+3*x*y**2*(4+3*x*y),
    2*x-3*x**2*y-x**3*w,
])
P = c*r**3-2*r**2+b*r-2*a
Delta = 4*(b**2-c*b**3+18*a*b*c-16*a-27*a**2*c**2)
checks = []

def check_zero(name, expression):
    numerator, _ = s.fraction(s.cancel(expression))
    assert s.Poly(s.expand(numerator),x,y,w,a,b,c,r,h,t,z,lam,domain=s.QQ).is_zero, (name, expression)
    checks.append({"name": name, "status": "proved-by-exact-identity"})

check_zero("original determinant", F.jacobian([x,y,w]).det()+2)
check_zero("original discriminant", s.discriminant(P,r)-Delta)
alpha = s.diff(P,r)/2
inverse_r = {x:1/alpha, y:r-alpha, w:5*alpha**2-3*r*alpha-c*alpha**3}
Fi = F.subs(inverse_r)
check_zero("r chart F1", Fi[0]-a-P/2)
check_zero("r chart F2", Fi[1]-b)
check_zero("r chart F3", Fi[2]-c)
check_zero("r recovered", (y+1/x).subs(inverse_r)-r)
M = s.Matrix([[0,0,2*a/c],[1,0,-b/c],[0,1,2/c]])
check_zero("multiplication derivative determinant", (3*c*M**2-4*M+b*s.eye(3)).det()+Delta/c)

v=1+x*y
check_zero("binary cubic source identity", F[2]*v**3-2*v**2*x+F[1]*v*x**2-2*F[0]*x**3)
check_zero("source h derivative identity", -2*v**2+2*F[1]*x*v-6*F[0]*x**2+2*v)
check_zero("source h y identity", y*v-F[1]*v+3*F[0]*x)
Q=c-2*h+b*h**2-2*a*h**3
d=s.diff(Q,h)
yh=b-3*a*h
inverse_h={x:-2*h/d,y:yh,w:-a*d**3/8-yh**2*d**2/4+3*yh**2*d/2}
Fh=F.subs(inverse_h)
check_zero("h chart F1", Fh[0]-a)
check_zero("h chart F2", Fh[1]-b)
check_zero("h chart F3", Fh[2]-c+Q)
check_zero("h chart v", v.subs(inverse_h)+2/d)
check_zero("h recovered", (x/v).subs(inverse_h)-h)
check_zero("chart polynomial transition", Q-h**3*P.subs(r,1/h))
check_zero("chart derivative transition", d-3*h**2*P.subs(r,1/h)+h*s.diff(P,r).subs(r,1/h))

H=c*(1+lam*z)**3-2*(1+lam*z)**2*z+b*(1+lam*z)*z**2-2*a*z**3
check_zero("finite chart full polynomial", H-(P.subs(r,lam)*z**3+(3*c*lam**2-4*lam+b)*z**2+(3*c*lam-2)*z+c))
check_zero("finite base cover unit identity", P.subs(r,1)+P.subs(r,-1)-2*P.subs(r,0)+4)
check_zero("projective chart discriminant", s.discriminant(H,z)-Delta)
arc={x:1/t,y:-3*t/2,w:13*t**2/2}
for i, expected in enumerate([-t**2/4,0,0]):
    check_zero(f"Laurent arc target coordinate {i+1}", F[i].subs(arc)-expected)

here=Path(__file__).resolve().parent
result={
    "check_type":"exact rational symbolic identities",
    "sympy_version":s.__version__,
    "checks":checks,
    "number_of_checks":len(checks),
    "all_passed":True,
    "proof_file_sha256":hashlib.sha256((here/"audit.md").read_bytes()).hexdigest(),
    "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(here/"certificate.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"all_passed":True,"number_of_checks":len(checks),"certificate":str(here/"certificate.json")}))
