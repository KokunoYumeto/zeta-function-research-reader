"""Independent full-jet Euclidean bi-Laplacian derivation in original coordinates.

The jet differentiation starts from the original F1/2, before restriction.
No asserted curve coefficients enter the derivative calculation.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
x, y, w = coords = s.symbols("x y w", real=True)
z = s.symbols("z", positive=True)
sigma = ((1+x*y)**3*w+y**2*(1+x*y)*(4+3*x*y))/2
grad = lambda h: s.Matrix([s.diff(h, q) for q in coords])
lap = lambda h: sum(s.diff(h, q, 2) for q in coords)
g = grad(sigma)
N = s.expand(g.dot(g))
L = s.expand(lap(sigma))
checks = {}

def zero(name, expression):
    vals = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    residuals = [s.cancel(v) for v in vals]
    checks[name] = all(v == 0 for v in residuals)
    if not checks[name]:
        raise AssertionError((name, residuals))

# A dictionary k -> a_k represents sum a_k(q) Z^(k)(sigma(q)).
# This differentiation includes both derivative-of-coefficient and chain terms.
def differentiate(jet, q):
    result = {}
    for k, a in jet.items():
        result[k] = result.get(k, 0)+s.diff(a, q)
        result[k+1] = result.get(k+1, 0)+a*s.diff(sigma, q)
    return {k:s.expand(a) for k,a in result.items() if a != 0}

def laplacian(jet):
    result = {}
    for q in coords:
        for k,a in differentiate(differentiate(jet,q),q).items():
            result[k] = result.get(k,0)+a
    return {k:s.expand(a) for k,a in result.items() if s.expand(a) != 0}

first = laplacian({0:s.Integer(1)})
second = laplacian(first)
zero("first_laplacian_full_Zprime",first[1]-L)
zero("first_laplacian_full_Zsecond",first[2]-N)
zero("bi_laplacian_full_Zfourth",second[4]-N**2)
zero("bi_laplacian_full_Zthird",second[3]-2*N*L-2*grad(N).dot(g))
zero("bi_laplacian_full_Zsecond",second[2]-lap(N)-2*grad(L).dot(g)-L**2)
zero("bi_laplacian_full_Zprime",second[1]-lap(L))
H=s.hessian(sigma,coords)
zero("Bochner_expansion_full",lap(N)-2*sum(e**2 for e in H)-2*grad(L).dot(g))
gamma = s.Matrix([1/z,-3*z/2,13*z**2/2])
restriction = dict(zip(coords,gamma))
restrict = lambda f:s.cancel(f.subs(restriction,simultaneous=True))
on_curve = {k:restrict(v) for k,v in second.items()}
curve_N, curve_L = restrict(N), restrict(L)
zero("original_curve_sigma",restrict(sigma)+z**2/8)
zero("original_curve_N",curve_N-(81*z**6+36*z**2+4)/1024)
zero("original_curve_L",curve_L-s.Rational(13,4)+s.Rational(27,4)*z**4)

# Only now compare independently derived coefficients with the proposed values.
proposed = {
4:curve_N**2,
3:-s.Rational(6561,2048)*z**10+s.Rational(243,2048)*z**6
  -s.Rational(135,1024)*z**4+s.Rational(351,512)*z**2+s.Rational(31,512),
2:s.Rational(26973,128)*z**8-s.Rational(4419,64)*z**4
  +s.Rational(135,64)*z**2+s.Rational(669,16)+s.Rational(15,16)/z**2,
1:-111*z**2+36/z**2,
}
for k in sorted(proposed):
    zero("curve_coefficient_Zderivative_"+str(k),on_curve[k]-proposed[k])
for k,v in {4:0,3:0,2:s.Rational(15,16),1:36}.items():
    zero("scaled_coefficient_limit_"+str(k),s.limit(z**2*on_curve[k],z,0,dir="+")-v)
zero("unscaled_N_limit",s.limit(curve_N,z,0,dir="+")-s.Rational(1,256))
zero("unscaled_L_limit",s.limit(curve_L,z,0,dir="+")-s.Rational(13,4))
zero("moment_sign_constant",s.Rational(15,16)*(-32)+30)
zero("first_laplacian_moment_constant",-32*s.Rational(1,256)+s.Rational(1,8))

# Formal even Taylor coefficients establish the remainder orders without a
# numerical approximation to the actual entire Newman function.
v=s.symbols("v")
j0,j2,j4,j6=s.symbols("Z0 Z2 Z4 Z6")
T=j0+j2*v**2/2+j4*v**4/24+j6*v**6/720
curve_jet={k:s.diff(T,v,k).subs(v,-z**2/8) for k in range(1,5)}
formal_second=s.expand(sum(on_curve[k]*curve_jet[k] for k in on_curve))
zero("even_jet_leading_bilaplacian",s.limit(z**2*formal_second,z,0,dir="+")-s.Rational(15,16)*j2)
zero("even_jet_constant_bilaplacian",s.limit(formal_second-s.Rational(15,16)*j2/z**2,z,0,dir="+")
     -(s.Rational(597,16)*j2+j4/s.Integer(65536)))
formal_first=s.expand(curve_N*curve_jet[2]+curve_L*curve_jet[1])
zero("even_jet_first_laplacian_limit",s.limit(formal_first,z,0,dir="+")-j2/256)

data = {
"schema_version":1,"status":"pass","number_of_checks":len(checks),
"all_passed":all(checks.values()),"checks":checks,"sympy_version":s.__version__,
"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
"original_sigma":str(sigma),"curve":[str(a) for a in gamma],
"curve_sigma":str(restrict(sigma)),"curve_gradient":[str(restrict(a)) for a in g],
"curve_hessian":[[str(restrict(H[i,j])) for j in range(3)] for i in range(3)],
"curve_N":str(curve_N),"curve_L":str(curve_L),
"curve_gradN_dot_gradsigma":str(restrict(grad(N).dot(g))),
"curve_gradL_dot_gradsigma":str(restrict(grad(L).dot(g))),
"curve_lapN":str(restrict(lap(N))),"curve_lapL":str(restrict(lap(L))),
"curve_bilaplacian_coefficients":{str(k):str(v) for k,v in sorted(on_curve.items())},
"full_chain_coefficient_formulas":{"4":"N^2","3":"2 N L+2 grad(N).grad(sigma)",
"2":"lap(N)+2 grad(L).grad(sigma)+L^2","1":"lap(L)"},
"scope":"Original polynomial derivatives, generic scalar-jet product rules, all four restricted coefficients and formal even-jet endpoint constants. Entire-function and moment estimates are proved separately in the review.",
"lean_used":False,"navier_stokes_disproof_established":False,
"tex_derivation":"tex/arithmetic_bilaplacian.tex",
"tex_derivation_sha256":hashlib.sha256((ROOT/"tex/arithmetic_bilaplacian.tex").read_bytes()).hexdigest(),
}
if __name__ == "__main__":
    output = ROOT/"checks/arithmetic_bilaplacian_checks.json"
    output.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"number_of_checks":len(checks),"all_passed":all(checks.values()),
        "output":output.relative_to(ROOT).as_posix(),
        "tex_derivation_sha256":data["tex_derivation_sha256"]},indent=2))
