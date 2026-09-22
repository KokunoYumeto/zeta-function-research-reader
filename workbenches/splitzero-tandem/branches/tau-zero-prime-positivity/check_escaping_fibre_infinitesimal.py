"""Exact checks for EFI1–EFI63; proofs remain in the derivation."""
import json
from pathlib import Path
import sympy as s

checks = []

def same(name, actual, expected):
    entries = list(actual-expected) if isinstance(actual, s.MatrixBase) else [actual-expected]
    assert all(s.cancel(s.expand(t)) == 0 for t in entries), name
    checks.append(name)

x, y, w, r, alpha, c, a, b, d, z, lam, delta, kappa = s.symbols(
    "x y w r alpha c a b d z lam delta kappa"
)
F = s.Matrix([
    (1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
    y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),
    2*x-3*x*x*y-x**3*w,
])
same("EFI1 original determinant", F.jacobian([x,y,w]).det(), -2)
H = {x:1/alpha,y:r-alpha,w:5*alpha**2-3*r*alpha-c*alpha**3}
same("EFI3 original inverse composition", F.subs(H, simultaneous=True),
     s.Matrix([r*r+r*alpha-c*r**3,4*r+2*alpha-3*c*r*r,c]))
same("EFI7 quadratic actual fibre", F.subs({x:-1/(2*r),y:3*r,w:26*r*r},simultaneous=True),
     s.Matrix([-r*r,0,0]))
P = c*r**3-2*r*r+b*r-2*a
rs = 2/(3*c)
same("EFI22 triple heat polynomial",
     P.subs({r:rs+z,a:4/(27*c*c)+2*d,b:4/(3*c)+6*c*d}, simultaneous=True),
     c*(z**3+6*d*z))
mod = z**3+6*d*z
def red(t):
    return s.rem(s.expand(t),mod,z)
al = 3*c*z*z/2+3*c*d
eta = al*(rs+z-al)
omega = 5*al**3-3*(rs+z)*al**2-c*al**4
same("EFI26 recover u", red(2*(al-3*c*d)/(3*c)),z*z)
same("EFI26 recover v",red(-(eta-rs*al+al*al)/(6*c)),d*z)
same("EFI27 omega in graph subalgebra",red(omega),
     red(5*al**3-3*rs*al**2+18*c*al*d*z-c*al**4))
same("EFI28 u squared",red(z**4),-6*d*z*z)
same("EFI28 uv",red(z*z*d*z),-6*d*d*z)
same("EFI28 v squared",red(d*d*z*z),d*d*z*z)
Mz = s.Matrix([[0,0,0],[1,0,-6*d],[0,1,0]])
same("EFI39 root Gram",s.Matrix(3,3,lambda i,j:s.trace(Mz**(i+j))),
     s.Matrix([[3,0,-12*d],[0,-12*d,0],[-12*d,0,72*d*d]]))
G3=s.Matrix([[3,0,-12*d],[0,-12*d,0],[-12*d,0,72*d*d]])
same("EFI39 root trace determinant",G3.det(),-864*d**3)
Mu = s.Matrix([[0,0,0],[1,-6*d,0],[0,0,-6*d]])
Mv = s.Matrix([[0,0,0],[0,0,d*d],[1,-6*d,0]])
ms = [s.eye(3),Mu,Mv]
GG=s.Matrix(3,3,lambda i,j:s.trace(ms[i]*ms[j]))
same("EFI40 graph Gram",GG,
     s.Matrix([[3,-12*d,0],[-12*d,72*d*d,0],[0,0,-12*d**3]]))
same("EFI40 graph trace determinant",GG.det(),-864*d**5)
same("EFI39 actual polynomial discriminant",s.discriminant(c*mod,z),-864*c**4*d**3)
same("EFI35 trace x",1/(3*c*d)-2/(6*c*d),0)
same("EFI35 trace x squared",1/(9*c*c*d*d)+2/(36*c*c*d*d),1/(6*c*c*d*d))
same("EFI55 exact bridge", (z-lam/2)**2-lam**2/4,z*z-lam*z)
Gobs=s.Matrix([[2,lam],[lam,lam**2]])
Q=s.Matrix([[1,-lam/2],[0,1]])
same("EFI62 transported trace",Q.T*Gobs*Q,s.diag(2,lam**2/2))
same("EFI63 discriminant base change",(-4*a).subs(a,-lam**2/4),lam**2)
for sign in [-1,1]:
    same(f"EFI57 actual observed sheet {sign}",
         F.subs({x:sign/lam,y:-sign*3*lam/2,w:13*lam**2/2},simultaneous=True),
         s.Matrix([-lam**2/4,0,0]))
same("EFI58 first-order centered remainder",
     s.rem((z-kappa*delta/2)**2-z*z+kappa*delta*z,delta**2,delta),0)
out={"status":"passed","exact_identity_count":len(checks),"checks":checks,
     "scope":"Polynomial, rational, matrix, and discriminant identities; no RH assertion."}
Path(__file__).with_name("ESCAPING_FIBRE_EXACT_CHECKS.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
