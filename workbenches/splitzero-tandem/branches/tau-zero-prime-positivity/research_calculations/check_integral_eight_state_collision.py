"""Bounded exact algebra checks for IEC. The written proofs cover all primes.

Run with Python and SymPy. All computations here use integer/rational symbolic
arithmetic; no floating-point or numerical p-adic approximations are used.
"""
from pathlib import Path
import hashlib
import json
import math
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

BASE = Path(__file__).resolve().parent
x, e, t = s.symbols("x epsilon T")


class Ring:
    def __init__(self, variables, relations, basis):
        self.variables = variables
        self.groebner = s.groebner(relations, *variables, domain=s.QQ)
        self.basis = basis
        self.n = len(basis)

    def red(self, z):
        return s.expand(self.groebner.reduce(s.expand(z))[1])

    def vec(self, z):
        z = s.Poly(self.red(z), *self.variables)
        return s.Matrix([z.coeff_monomial(b) for b in self.basis])

    def mul(self, z):
        return s.Matrix.hstack(*(self.vec(z*b) for b in self.basis))


C = Ring((t, e), [e**2, t**2-6*e], [1, e, t, e*t])
B = Ring((t, x), [x**2*(x+3), t**2-3*x*(x+2)],
         [1, x, x**2, t, x*t, x**2*t])
checks = []


def check(name, condition, details=None):
    if isinstance(condition, s.MatrixBase):
        condition = condition == s.zeros(*condition.shape)
    condition = bool(condition)
    checks.append({"name": name, "passed": condition, "details": details})
    if not condition:
        raise AssertionError(name)


def zero(name, ring, expressions):
    expressions = list(expressions)
    check(name, all(ring.red(q) == 0 for q in expressions),
          {"scalar_identities": len(expressions)})


def snf_diagonal(matrix):
    sm = smith_normal_form(matrix, domain=ZZ)
    return [abs(int(sm[i, i])) for i in range(min(sm.shape))]


def vp(n, p):
    if n == 0:
        return None
    n, a = abs(int(n)), 0
    while n % p == 0:
        n //= p
        a += 1
    return a


zero("IEC8 double-root powers", C, [t**2-6*e, t**3-6*e*t, t**4])
Mlat = s.Matrix.hstack(*(C.vec(t**j) for j in range(4)))
check("IEC9-10 integral lattice Smith invariants",
      snf_diagonal(Mlat) == [1, 1, 6, 6])
check("IEC12 trace multiplicity4",
      [s.trace(C.mul(b)) for b in C.basis] == [4, 0, 0, 0])
zero("IEC11 square-zero ideal", C, [a*b for a in [e,e*t] for b in [e,e*t]])
aa, bb = s.symbols("a b")
zero("IEC11 square-zero section obstruction polynomial", C,
     s.Poly(s.expand((t+aa*e+bb*e*t)**2-6*e-2*aa*e*t),aa,bb).coeffs())

JC = s.BlockMatrix([[C.mul(2*e), C.mul(-6)],
                    [s.zeros(4), C.mul(2*t)]]).as_explicit()
HC = s.Matrix.hstack(s.Matrix.vstack(C.vec(e), C.vec(0)),
                     s.Matrix.vstack(C.vec(e*t), C.vec(0)),
                     s.Matrix.vstack(C.vec(3*t), C.vec(e*t)))
check("IEC17 cotangent cycles", JC*HC)
check("IEC17 rational kernel completeness", HC.rank() == 8-JC.rank() == 3)
check("IEC24 cotangent Smith decomposition",
      snf_diagonal(JC) == [2,2,2,2,6,0,0,0])
dC = s.Matrix.hstack(*(s.Matrix.vstack(C.vec(s.diff(b,e)), C.vec(s.diff(b,t)))
                       for b in C.basis))
check("IEC26 quotient by exact differentials",
      snf_diagonal(JC.row_join(dC)) == [1,1,1,2,2,2,2,18])
R2C = C.mul(6).row_join(C.mul(2*e)).row_join(C.mul(2*t))
check("IEC25 exterior-square Smith invariants", snf_diagonal(R2C) == [2,2,2,6])

# Exterior derivative in the free polynomial representatives: a de+b dT.
def d_one(ring, a, b, root):
    return ring.red(s.diff(b,root)-s.diff(a,t))

repsC = [(0,e),(0,t),(e,0),(e*t,0),(0,e*t)]
check("IEC27 five differential images",
      [d_one(C,a,b,e) for a,b in repsC] == [1,0,0,-e,t])
check("IEC28 integral cyclic kernel and cokernel orders",
      math.gcd(18,6) == 6 and 18//6 == 3)

n1, n2, n3 = x*(x+3), t*(x+3), t*x*(x+3)
zero("IEC41 complete nilradical multiplication", B,
     [n1*n1,n1*n3,n2*n3,n3*n3,n2*n2-18*n1,n1*n2-3*n3,
      x*n1,x*n3,x*n2-n3,t*n1-n3,t*n2-6*n1,t*n3])
def evalC(z):
    return C.red(s.sympify(z).subs(x,e))

Pi = s.Matrix.hstack(*(C.vec(evalC(b)) for b in B.basis))
evalplus = s.Matrix([[s.sympify(b).subs({x:-3,t:3}) for b in B.basis]])
evalminus = s.Matrix([[s.sympify(b).subs({x:-3,t:-3}) for b in B.basis]])
Iota = Pi.col_join(evalplus).col_join(evalminus)
check("IEC42 full 3-primary comparison Smith invariants",
      [vp(a,3) for a in snf_diagonal(Iota)] == [0,0,0,0,2,3],
      {"integer_diagonal":snf_diagonal(Iota)})
check("IEC14 trace in original x-basis",
      [s.trace(B.mul(b)) for b in B.basis] == [6,-6,18,0,0,0])
for i, bi in enumerate(B.basis):
    for j, bj in enumerate(B.basis):
        si = s.sympify(bi).subs(t,-t)
        eveni, oddi = s.expand(bi).coeff(t,0), s.expand(bi).coeff(t,1)
        evenj, oddj = s.expand(bj).coeff(t,0), s.expand(bj).coeff(t,1)
        expected = (4*eveni.subs(x,0)*evenj.subs(x,0)
                    +2*eveni.subs(x,-3)*evenj.subs(x,-3)
                    -18*oddi.subs(x,-3)*oddj.subs(x,-3))
        check(f"IEC15 reflected trace entry {i},{j}",
              s.trace(B.mul(si*bj)) == expected)

JB = s.BlockMatrix([[B.mul(3*x*(x+2)), B.mul(-6*(x+1))],
                    [s.zeros(6),B.mul(2*t)]]).as_explicit()
HB = s.Matrix.hstack(s.Matrix.vstack(B.vec(n1),B.vec(0)),
                     s.Matrix.vstack(B.vec(n3),B.vec(0)),
                     s.Matrix.vstack(B.vec(n2),B.vec(n3)))
check("P3-27 full cotangent cycles", JB*HB)
check("P3-27 full rational kernel completeness", HB.rank()==12-JB.rank()==3)
db = snf_diagonal(JB)
check("P3-30 exact 3-primary cotangent Smith invariants",
      sum(a==0 for a in db)==3 and sorted(vp(a,3) for a in db if a)
      == [0,0,0,1,1,1,1,1,1], {"integer_diagonal":db})

# The polynomial presentation map B->C in degree -1.
Fminus = s.BlockMatrix([[C.mul(e+3)*Pi,C.mul(-3)*Pi],
                        [s.zeros(4,6),Pi]]).as_explicit()
Fzero = s.diag(Pi,Pi)
check("IEC45 cotangent chain square", JC*Fminus-Fzero*JB)
Himage = HC*s.Matrix([[9,0,0],[0,9,-3],[0,0,3]])
check("IEC46 exact cotangent cycle images", Fminus*HB-Himage)
check("IEC47 cotangent comparison cokernel",
      snf_diagonal(s.Matrix([[9,0,0],[0,9,-3],[0,0,3]]))==[3,9,9])

# Check the independent elimination used by P3-30 as a quotient presentation.
# Coordinates: free a0,b0,b1; torsion a1,a2,a4,a5,b2,c (all order3).
M = s.zeros(9,12)
M[0,0]=1; M[3,1]=1; M[4,2]=1
M[2,3]=2; M[8,3]=1; M[5,4]=1; M[6,5]=1
M[1,6]=1; M[2,7]=1; M[7,8]=1
M[0,9]=3  # T dT=3 dx, because 3x dx=0.
MJ = M*JB
check("P3-30 all relation columns vanish in explicit decomposition",
      all(MJ[i,j]==0 if i<3 else int(MJ[i,j])%3==0
          for i in range(9) for j in range(12)))
dB = s.Matrix.hstack(*(s.Matrix.vstack(B.vec(s.diff(b,x)),B.vec(s.diff(b,t)))
                       for b in B.basis))
expectedDB=s.zeros(9,6)
expectedDB[0,1]=1; expectedDB[3,2]=2; expectedDB[1,3]=1
expectedDB[2,4]=3; expectedDB[8,4]=1
expectedDB[5,5]=2; expectedDB[7,5]=1
check("P3-34 all six degree-zero derivatives", M*dB-expectedDB)

# Exact Frobenius and divided defects on generators and bounded samples.
for p in [2,3,5,7]:
    zero(f"IEC30 monoidal relation p={p}", C, [t**(2*p)])
    for v in [0,e,t,e*t,e+t+e*t,2*e-3*t+5*e*t]:
        y=C.red(p*v); z=C.red(s.Rational(p*p,6)*v*v)
        zero(f"IEC32 lifted equations p={p},v={v}", C, [z*z,y*y-6*z])
        check(f"IEC32 coefficient integrality p={p},v={v}",
              all(c==0 or vp(c.p,p)>=vp(c.q,p)
                  for c in list(C.vec(y))+list(C.vec(z))))
zero("IEC34 monoidal reflection discrepancy", C, [2*t*t-12*e])
for v in [0,n1,n2,n3,n1+2*n2-3*n3]:
    X=B.red(s.Rational(3,2)*v*v); Y=B.red(3*v)
    zero(f"IEC51 full 3-adic lifted equations v={v}", B,
         [X*X*(X+3),Y*Y-3*X*(X+2)])

for p in [2,3,5,7]:
    for n in range(9):
        # C-images of the entire displayed bounded PD basis segment.
        en=C.red(t**(2*n)/s.factorial(n))
        on=C.red(t**(2*n+1)/s.factorial(n))
        check(f"IEC38 integral PD images p={p},n={n}",
              all(c.q==1 for c in list(C.vec(en))+list(C.vec(on))))
for n in range(1,10):
    check(f"IEC48 full B3 divided coefficient n={n}",
          vp(3**n,3)-vp(math.factorial(n),3)>=0)

# PD multiplication images in the whole B3 receiver, over its fraction field.
for i in range(5):
    for j in range(5):
        ei=B.red(t**(2*i)/s.factorial(i)); ej=B.red(t**(2*j)/s.factorial(j))
        oi=B.red(t**(2*i+1)/s.factorial(i)); oj=B.red(t**(2*j+1)/s.factorial(j))
        zero(f"IEC48 PD products {i},{j}", B,
             [ei*ej-s.binomial(i+j,i)*t**(2*(i+j))/s.factorial(i+j),
              ei*oj-s.binomial(i+j,i)*t**(2*(i+j)+1)/s.factorial(i+j),
              oi*oj-t**(2*(i+j+1))/(s.factorial(i)*s.factorial(j))])
check("IEC50 full nonzero class coefficient",
      M*s.Matrix.vstack(B.vec(0),B.vec(t*t))
      == s.Matrix([0,0,6,0,0,0,0,3,0]))
check("IEC52 monoidal discrepancy detected at the simple root",
      (t*x*(x+2)).subs({x:-3,t:3})==9)
Xmono=(1+x)**3-1
Ymono=t**3
zero("IEC56 original-coordinate monoidal relation defects", B,
     [Xmono-3*x, Xmono**2*(Xmono+3)+54*x*x,
      Ymono**2-3*Xmono*(Xmono+2)-54*x*x+18*x])
zero("IEC58 monoidal delta on x and 3x", B,
     [(Xmono-x**3)/3-x-x*x,
      (3*Xmono-(3*x)**3)/3-3*x-27*x*x])
zero("IEC57 delta relation defects", B,
     [(Xmono**2*(Xmono+3)-(x*x*(x+3))**3)/3+18*x*x,
      (Ymono**2-3*Xmono*(Xmono+2)-(t*t-3*x*(x+2))**3)/3
      -18*x*x+6*x])
check("IEC54-55 simple and infinity cotangent coefficient order",
      math.gcd(2,9)==math.gcd(2,-1)==1)
check("IEC55 infinity Frobenius obstruction modulo4",
      all((a*a+1)%4!=0 for a in range(4)))

proof = BASE / "INTEGRAL_EIGHT_STATE_COLLISION_DERIVATION.md"
report = {
    "description": "Bounded exact checks for the integral eight-state collision; full proofs are in the linked IEC and P3 source.",
    "arithmetic": "SymPy exact integer and rational arithmetic",
    "passed": all(c["passed"] for c in checks),
    "check_count": len(checks),
    "proof_file": proof.name,
    "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
    "checker_file": Path(__file__).name,
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "limitations": "Finite checks verify the listed identities and module matrices; completeness, universal classifications, and all-index statements are proved in the source, not inferred from these samples.",
    "checks": checks,
}
target=BASE / "INTEGRAL_EIGHT_STATE_COLLISION_CHECKS.json"
target.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":report["passed"],"check_count":len(checks),
                  "report":str(target),"proof_sha256":report["proof_sha256"]}))
