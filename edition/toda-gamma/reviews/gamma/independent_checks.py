"""Small independent exact fixtures; does not import the delivered checker."""
import argparse
import json
from pathlib import Path
import psutil
import sympy as s

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def eq(a, b):
    if isinstance(a, s.MatrixBase):
        return all(s.simplify(v) == 0 for v in a-b)
    return s.simplify(a-b) == 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    dest = args.json.resolve()
    require(dest.parent == here / "fresh_checks" and not dest.exists(), "unsafe output or overwrite")
    positives = []
    negatives = []

    def good(label, a, b):
        require(eq(a,b), label)
        positives.append(label)

    def bad(label, wrong, correct):
        rejected = False
        try:
            require(eq(wrong,correct), label)
        except RuntimeError:
            rejected = True
        require(rejected, "false formula was accepted: " + label)
        negatives.append(label)

    # Independent moments come directly from the gamma Laplace transform,
    # not from the source checker's polynomial-orthogonality recurrence.
    theta, x, y, z, u = s.symbols("theta x y z u", real=True)
    alpha, mass = s.Rational(3,2), s.Integer(7)
    jet = s.series(s.cos(theta)**(-alpha), theta, 0, 9).removeO()
    moments = [mass * s.factorial(j) * jet.coeff(theta,j) for j in range(9)]
    sumjet = s.series(s.cos(theta)**(-2*alpha), theta, 0, 9).removeO()
    summoments = [mass**2 * s.factorial(j) * sumjet.coeff(theta,j) for j in range(9)]

    def one(poly, variable=x):
        return s.expand(sum(c*moments[m[0]] for m,c in s.Poly(poly,variable).terms()))

    def joint(poly):
        return s.expand(sum(c*moments[m[0]]*moments[m[1]] for m,c in s.Poly(poly,x,y).terms()))

    def summed(poly):
        return s.expand(sum(c*summoments[m[0]] for m,c in s.Poly(poly,u).terms()))

    good("literal product mass", joint(s.Integer(1)), 49)
    bad("probability normalization erases literal mass", s.Integer(1), joint(s.Integer(1)))
    good("degree-two addition with multiplicity", (x+y)**2-2*alpha,
         (x*x-alpha)+(y*y-alpha)+2*x*y)
    bad("missing addition multinomial", (x*x-alpha)+(y*y-alpha)+x*y,
        (x+y)**2-2*alpha)
    projection = alpha/(2*(2*alpha+1))*(u*u-2*alpha)
    for j in range(5):
        good("conditional projection moment " + str(j), joint(x*y*(x+y)**j), summed(projection*u**j))
    bad("missing projection Pochhammer denominator", summed(alpha**2*(u*u-2*alpha)*u*u),
        joint(x*y*(x+y)**2))
    good("relative norm retained", joint((x*y-projection.subs(u,x+y))**2),
         joint(x*x*y*y)-summed(projection**2))
    require(joint((x*y-projection.subs(u,x+y))**2) > 0, "nonzero relative fixture vanished")

    # Check the parent's new generating-function join independently through
    # a theta jet using a positive polynomial fixture, not an actual packet.
    B = 2+x+x*x
    Mjet = sum(one(B*x**j)*theta**j/s.factorial(j) for j in range(7))
    kernel = s.series((1+z*z)**(-alpha/2)*s.exp(x*s.atan(z)), z, 0, 7).removeO()
    A = sum(one(B*s.expand(kernel).coeff(z,j))/mass*z**j for j in range(7))
    pull = s.series((1+z*z)**(-alpha/2)*Mjet.subs(theta,s.atan(z))/mass,z,0,7).removeO()
    good("generating-function join to order six", s.expand(A),s.expand(pull))
    inv = s.series(mass*s.cos(theta)**(-alpha)*A.subs(z,s.tan(theta)),theta,0,7).removeO()
    good("inverse generating join to order six", s.expand(inv),s.expand(Mjet))
    bad("missing inverse mass", s.expand(inv/mass),s.expand(Mjet))
    quotient = s.series((Mjet/mass)**2*s.cos(theta)**(2*alpha),theta,0,7).removeO()
    power = s.series(A.subs(z,s.tan(theta))**2,theta,0,7).removeO()
    good("two-factor Laplace ratio retains all scales", s.expand(quotient),s.expand(power))

    # A complex, non-diagonal finite source, same quotient J and relation Bc.
    # It detects conjugation errors that even weights can hide.
    Mgamma = s.diag(2,3)
    Mh = s.Matrix([[4,1+s.I],[1-s.I,5]])
    J = s.Matrix([[1,0]])
    Bc = s.Matrix([[0],[1]])
    Rgamma = s.Matrix([[1],[0]])
    correction = Bc*(Bc.H*Mh*Bc).inv()*Bc.H*Mh*Rgamma
    R = Rgamma-correction
    good("same quotient under representative correction", J*R,s.eye(1))
    good("actual arithmetic relation orthogonality", Bc.H*Mh*R,s.zeros(1,1))
    good("actual quotient Schur metric", (R.H*Mh*R)[0],s.Rational(18,5))
    good("quotient source-bound determinant exponent", (Rgamma.H*Mgamma*Rgamma)[0],2)
    require((3*Mgamma-Mh).det()>0 and (3*Mgamma-Mh)[0,0]>0, "source bound fixture")
    require((R.H*Mh*R)[0] <= 3*(Rgamma.H*Mgamma*Rgamma)[0], "quotient bound fixture")
    bad("omitted old-relation correction", Bc.H*Mh*Rgamma,s.zeros(1,1))
    Rwrong = s.Matrix([[1],[-(1+s.I)/5]])
    bad("wrong complex conjugation in correction", Bc.H*Mh*Rwrong,s.zeros(1,1))
    memory = psutil.Process().memory_info()
    peak = getattr(memory,"peak_wset",memory.rss)
    require(peak < 200_000_000,"memory budget exceeded")
    result = {"status":"passed", "positive_checks":positives,
              "formula_negative_controls_rejected":negatives,
              "peak_working_set_bytes":peak,"sympy":s.__version__,
              "source_checker_imported":False,
              "scope":"Finite rational/generating-jet fixtures, not an arithmetic packet, numerical interval, global analytic proof or Lean certificate."}
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result))

if __name__ == "__main__":
    main()
