"""Exact supplementary checks for OM16--20 and OM34--35.

All group and metric claims have complete proofs in the companion TeX.
This script independently verifies the polynomial reductions and the
evaluated scalar observation using rational arithmetic, without roots.
"""
from pathlib import Path
import json
import sympy as s

r, A, B, C, D, c = s.symbols("r A B C D c")
h = A*r**4 + r**3 + B*r**2 + C*r + D
d = s.diff(h, r)
polys = [s.Integer(1), -s.I*d, A*d*d+2*r*d,
         s.I*(7*r*r*d-13*d*d)]
rems = [s.Poly(s.rem(p, h, r), r) for p in polys]
coeff = s.Matrix([[p.nth(j) for j in range(4)] for p in rems])
R = s.Matrix([
    [2*B, 3, 4*A],
    [4*A*B*C-8*A*D-7*C,
     4*A*B*B-2*A*C-16*A*A*D-5*B, 4*A*B-8*A*A*C-3],
    [20*C/A+76*D-52*B*C,
     20*B/A+5*C-52*B*B+208*A*D, 20/A-66*B+104*A*C]
])
checks = {}
actual_R = coeff[1:4,1:4].copy()
actual_R[0,:] = actual_R[0,:]/(-s.I)
actual_R[2,:] = actual_R[2,:]/s.I
checks["OM34_all_nine_original_coefficients"] = all(
    s.cancel(x) == 0 for x in actual_R-R)
checks["OM35_boundary_determinant_coefficient"] = (
    s.simplify(s.limit(A*R.det(), A, 0)-80*(3*C-B*B)) == 0)

c0 = -s.Rational(60,431)
hc = r**4+r**3+c*r
dc = s.diff(hc,r)
even = s.Matrix([0,-r,3*s.I*dc,(-17*r+r*r)*dc-2*dc*dc])
odd_unscaled = s.Matrix([1,-s.I*dc,dc*dc+2*r*dc,
                         s.I*(7*r*r*dc-13*dc*dc)])
ell = s.Matrix([[208*c0*c0,5*s.I*c0,60,-21*s.I]])
checks["OM16_all_odd_columns_annihilated"] = (
    s.rem((ell*odd_unscaled)[0].subs(c,c0),hc.subs(c,c0),r)==0)
f = s.Rational(60,185761)*(
    1073621*r**3+1680900*r*r+490909*r-75060)
checks["OM17_original_even_observation"] = (
    s.expand(s.rem(((ell*even)[0]/s.I).subs(c,c0),
                   hc.subs(c,c0),r)-f)==0)
p = {0:s.Integer(4),1:s.Integer(-1),2:s.Integer(1),3:-1-3*c0}
for j in range(4,7):
    p[j]=s.cancel(-p[j-1]-c0*p[j-3])
def tr_roots(polynomial):
    return s.cancel(sum(co*p[mon[0]]
                        for mon,co in s.Poly(polynomial,r).terms()))
tr1, tr2 = tr_roots(f), tr_roots(f*f)
lambda0=s.cancel(tr1*tr1/4)
lambda3=s.cancel((tr2-lambda0)/3)
checks["OM19_trace"] = tr1==s.Rational(15870600,185761)
checks["OM19_square_trace"] = tr2==s.Rational(
    348296871672000,34507149121)
checks["OM20_lambda0"] = lambda0==s.Rational(
    62968986090000,34507149121)
checks["OM20_lambda3"] = lambda3==s.Rational(
    95109295194000,34507149121)
checks["OM20_positive_even_coefficients"] = bool(lambda0>0 and lambda3>0)
result={
    "status":"passed" if all(checks.values()) else "failed",
    "method":"Exact SymPy rational polynomial reduction; no numerical roots.",
    "checks":checks,
    "lambda0":str(lambda0),"lambda3":str(lambda3),
    "lambda4":"0",
    "proof":"ORBIT_METRIC_DERIVATION.tex OM1--40",
    "scope":"Supplementary algebra checks; complete group and metric proofs are in TeX."
}
Path(__file__).with_name("ORBIT_METRIC_EXACT_CHECKS.json").write_text(
    json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
assert all(checks.values())
