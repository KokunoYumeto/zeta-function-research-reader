"""Exact identity checks for specified formulas in recovered U0001--U0015.

These finite checks supplement the source-pinned proofs in AUDIT.md. They do
not verify linked manuscripts or establish an arithmetic sign/zero claim.
"""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
checks = []

def verify(name, expression):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    values = [sp.factor(sp.together(v)) for v in entries]
    passed = all(v == 0 for v in values)
    checks.append({"identity": name, "passed": passed, "residual": [str(v) for v in values]})
    if not passed:
        raise ArithmeticError(name + ": " + str(values))

x, y, w = sp.symbols("x y w")
F = sp.Matrix([
    (1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
    y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),
    2*x-3*x*x*y-x**3*w,
])
J = F.jacobian([x, y, w])
verify("L662: determinant of original polynomial Jacobian", J.det()+2)
for point in [(0, 0, -sp.Rational(1,4)), (1, -sp.Rational(3,2), sp.Rational(13,2)), (-1, sp.Rational(3,2), sp.Rational(13,2))]:
    verify("L664--670: original three-point fibre " + str(point), F.subs(dict(zip((x,y,w),point)))-sp.Matrix([-sp.Rational(1,4),0,0]))

W1 = -sp.Rational(1,2)*sp.Matrix([sp.diff(F[1],v) for v in (x,y,w)]).cross(sp.Matrix([sp.diff(F[2],v) for v in (x,y,w)]))
W2 = -sp.Rational(1,2)*sp.Matrix([sp.diff(F[2],v) for v in (x,y,w)]).cross(sp.Matrix([sp.diff(F[0],v) for v in (x,y,w)]))
U = 2*W1+6*F[2]*W2
verify("L724--737: exact original coefficient-flow lift", J*U-sp.Matrix([2,6*F[2],0]))
verify("L735: divergence of original coefficient-flow lift", sum(sp.diff(U[i],v) for i,v in enumerate((x,y,w))))
r = sp.symbols("r", positive=True)
branch = {x:-1/r,y:sp.Rational(3,2)*r,w:sp.Rational(13,2)*r*r}
verify("L763--765: negative branch target", F.subs(branch)-sp.Matrix([-r*r/4,0,0]))
verify("L768--774: negative branch velocity", U.subs(branch)-sp.Matrix([-4/r**3,-6/r,-52]))
source_DU = sp.Matrix([
    [-sp.Rational(27,2)/r**2,-9/r**4,3/r**5],
    [-sp.Rational(129,4),-sp.Rational(27,2)/r**2,sp.Rational(9,2)/r**3],
    [-sp.Rational(423,2)*r,-93/r,27/r**2],
])
verify("L870--875: full original Euclidean derivative", U.jacobian([x,y,w]).subs(branch)-source_DU)
S=(source_DU+source_DU.T)/2
verify("L880--886: scaled strain limit", (r**5*S).applyfunc(lambda v:sp.limit(v,r,0,dir="+"))-sp.Matrix([[0,0,sp.Rational(3,2)],[0,0,0],[sp.Rational(3,2),0,0]]))
verify("L907: determinant quotient giving middle-eigenvalue limit -36", sp.limit(sp.det(S)/(-sp.Rational(9,4)*r**-10),r,0,dir="+")+36)
t=sp.symbols("t")
kappa=-4/(1-8*t)
verify("L847: reciprocal-coordinate Riccati equation",sp.diff(kappa,t)+2*kappa**2)

z, eta=sp.symbols("z eta")
thermal=3+2*sp.exp(eta)*sp.cos(z)
verify("L1606: five-state heat identity",sp.diff(thermal,eta)+sp.diff(thermal,z,2))

a,b,c=sp.symbols("a b c")
d=b-a
verify("L1729--1734: exterior contribution to neighbouring-gap derivative", 2*d*(2/(b-c)-2/(a-c))+4*d*d/((b-c)*(a-c)))

rho, rh=sp.symbols("rho rh",positive=True)
rad=rh+rho*rho/(4*rh)
verify("L3369--3372: Schwarzschild angular-clock coefficient", -(1-rh/rad)*4*rh**2+rho**2/(1+rho**2/(4*rh**2)))
verify("L3369--3372: Schwarzschild radial coefficient", sp.diff(rad,rho)**2/(1-rh/rad)-(1+rho**2/(4*rh**2)))

beta,gamma,Estar=sp.symbols("beta gamma Estar",real=True)
k=gamma/2-sp.I*(1-beta)/2
verify("L3017--3025: exact zeta-zero scattering coordinate",1-2*sp.I*k-(beta-sp.I*gamma))
verify("L3041--3048: complete complex energy",Estar*(k*k+sp.Rational(1,4))-Estar*(gamma**2/4-(1-beta)**2/4+sp.Rational(1,4))+sp.I*Estar*gamma*(1-beta)/2)

u=sp.symbols("u",real=True)
FH,A,kap,central,hbar=sp.symbols("FH A kap central hbar",nonzero=True)
ray=FH-A*sp.exp(-kap*u)
schwarzian=sp.diff(ray,u,3)/sp.diff(ray,u)-sp.Rational(3,2)*(sp.diff(ray,u,2)/sp.diff(ray,u))**2
verify("L4060: horizon-ray Schwarzian",schwarzian+kap**2/2)
entropy=-central*sp.log(sp.diff(ray,u))/12
verify("L4039--4045: entropy-to-flux identity on horizon ray",hbar/(2*sp.pi)*(6/central*sp.diff(entropy,u)**2+sp.diff(entropy,u,2))+hbar*central/(24*sp.pi)*schwarzian)

result={"source":"audit_segment_U0001_U0015.md", "sympy_version":sp.__version__,"scope":"Finite algebraic identities only; no RH, NS endpoint, or ER=EPR resolution", "checks":checks,"all_passed":all(c["passed"] for c in checks)}
(ROOT/"exact_checks.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"checks":len(checks),"all_passed":result["all_passed"]}))
