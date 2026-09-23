"""Auxiliary exact identities and explicitly non-certified numerical checks."""
from pathlib import Path
import json
import sympy as s
import mpmath as mp

out = Path(__file__).resolve().parent
z, t, w, u = s.symbols("Z t w u", positive=True)
i = s.I
exact = []
def check(name, expr):
    residual = s.simplify(s.expand(expr))
    if residual != 0:
        raise ArithmeticError((name, residual))
    exact.append(name)
def N(f):
    return -(f + z*z*f - 2*t*f - 4*t*z*s.diff(f,z) + 4*t*t*s.diff(f,z,2))/64
def NT(f):
    return -(f + z*z*f + 2*t*f + 4*t*z*s.diff(f,z) + 4*t*t*s.diff(f,z,2))/64
for sign in [-1, 1]:
    check(f"adjoint null mode {sign}", NT(s.exp(-z*z/(4*t)+sign*i*z/(2*t))))
    check(f"full homogeneous mode {sign}", N(s.exp(z*z/(4*t)+sign*i*z/(2*t))))
    for shift in [-1, 1]:
        a = w + sign*i/(2*t)
        check(f"Gaussian exponent {sign} {shift}",
              t*u*u + t*(-a+shift*i*u)**2 -
              (t*a*a-2*shift*i*t*a*u))
    a = w + sign*i/(2*t)
    check(f"original arithmetic argument {sign}",
          s.Rational(1,2)+i*(2*t*a)/2 - (i*t*w+(1-sign)/2))
    test = s.exp(-z*z)
    psi = s.exp(-z*z/(4*t)+sign*i*z/(2*t))
    W = psi*(s.diff(test,z)-(z/(2*t)+sign*i/(2*t))*test)
    check(f"full Green boundary derivative {sign}",
          s.diff(W,z) + 16/t**2*psi*N(test))
R = s.sqrt(s.pi*t)*s.exp(-1/(4*t))/8
A = s.sqrt(2*s.pi*t)*s.exp(-1/(8*t))
check("Schwartz complement coefficient",
      R/A - s.exp(-1/(8*t))/(8*s.sqrt(2)))
H0,H1,H2 = s.symbols("H0 H1 H2")
local = (H0+H1*z+H2*z*z/2)*s.exp(-z*z/(4*t))*s.cos(z/(2*t))
check("filtered point moment", s.diff(local,z,2).subs(z,0)-H0/4 -
      (H2-(1/(2*t)+1/(4*t*t)+s.Rational(1,4))*H0))

mp.mp.dps = 45
def phi(x):
    return mp.fsum((2*mp.pi**2*n**4*mp.exp(9*x)-3*mp.pi*n*n*mp.exp(5*x))
                  *mp.exp(-mp.pi*n*n*mp.exp(4*x)) for n in range(1,9))
def prod(q):
    if q == 0 or q == 1:
        return mp.mpf(1)
    return q*(q-1)*mp.pi**(-q/2)*mp.gamma(q/2)*mp.zeta(q)
numerical=[]
for tv,wv in [(mp.mpf("0.125"),mp.mpf("0.2")),
              (mp.mpf("0.4"),mp.mpc("0.3","0.2")),
              (mp.mpf("0.75"),mp.mpc("-0.1","0.4"))]:
    am=wv-mp.j/(2*tv)
    ap=wv+mp.j/(2*tv)
    source=mp.sqrt(mp.pi*tv)*mp.quad(
        lambda x: phi(x)*(mp.exp(tv*am**2)*mp.cos(2*tv*am*x)
                        +mp.exp(tv*ap**2)*mp.cos(2*tv*ap*x)),
        [0,mp.mpf(".2"),mp.mpf(".5"),1,mp.mpf("1.7")])
    receiver=mp.sqrt(mp.pi*tv)/16*(
        mp.exp(tv*am**2)*prod(1+mp.j*tv*wv)
        +mp.exp(tv*ap**2)*prod(mp.j*tv*wv))
    err=abs(source-receiver)
    if err>mp.mpf("1e-35"):
        raise ArithmeticError(("original-zeta receiver",tv,wv,err))
    numerical.append({"t":str(tv),"w":str(wv),"absolute_error":str(err)})

receipt={"exact_checks":len(exact),"exact_passed":exact,
         "non_certified_source_quadrature_checks":numerical,
         "scope":"Exact auxiliary identities plus finite numerical comparisons. The proofs establish the infinite integrals and domains; these quadratures do not certify error intervals or an RH claim."}
(out/"VERIFICATION.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,indent=2))
