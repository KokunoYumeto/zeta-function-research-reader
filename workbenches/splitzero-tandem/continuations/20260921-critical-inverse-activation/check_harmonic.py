"""Independent exact finite checks for the harmonic receiver.

These are complex rational auxiliary data and original rectangular lattices.
They do not evaluate arithmetic moments or assert an eventual gap guard at k=9.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
checks = []


def require(name, condition):
    if not condition:
        raise ArithmeticError(name)
    checks.append(name)


def zero(name, matrix):
    require(name, all(sp.cancel(x) == 0 for x in matrix))


def psd(name, matrix):
    matrix = matrix.applyfunc(sp.cancel)
    zero(name + ": Hermitian", matrix - matrix.H)
    for size in range(1, matrix.rows + 1):
        for ids in combinations(range(matrix.rows), size):
            value = sp.cancel(matrix.extract(ids, ids).det())
            if value.is_nonnegative is not True:
                raise ArithmeticError(f"{name}: principal minor {ids}: {value}")
    checks.append(name + ": all principal minors")


# Exact squared products for the ORIGINAL coordinates delta=1/4, gamma=3.
# |omega_ab-omega_mn|^2=((a-m)^2+144(b-n)^2)/4.
for k in (1, 5, 9):
    indices = [(a, b) for a in range(k + 1) for b in range(k + 1)]
    products = {}
    for a, b in indices:
        value = 1
        for m, n in indices:
            if (a, b) != (m, n):
                value *= (a - m) ** 2 + 144 * (b - n) ** 2
        products[a, b] = value
    for a, b in indices:
        if b < k:
            rhs = Fraction(1)
            for m in range(k + 1):
                rhs *= Fraction((a - m) ** 2 + 144 * (b + 1) ** 2,
                                (a - m) ** 2 + 144 * (k - b) ** 2)
            require(f"k={k}, horizontal derivative ratio ({a},{b})",
                    Fraction(products[a, b + 1], products[a, b]) == rhs)
        if a < k:
            rhs = Fraction(1)
            for n in range(k + 1):
                rhs *= Fraction(144 * (b - n) ** 2 + (a + 1) ** 2,
                                144 * (b - n) ** 2 + (k - a) ** 2)
            require(f"k={k}, vertical derivative ratio ({a},{b})",
                    Fraction(products[a + 1, b], products[a, b]) == rhs)
    centres = {(a, b) for a in (k // 2, k // 2 + 1)
               for b in (k // 2, k // 2 + 1)}
    minimum = min(products.values())
    require(f"k={k}, precisely four derivative minima",
            {ab for ab, value in products.items() if value == minimum} == centres)
    centre = (k // 2, k // 2)
    for j in range(1, k + 1):
        shell = [ab for ab in indices
                 if max(abs(ab[0] - centre[0]), abs(ab[1] - centre[1])) == j]
        require(f"k={k}, full shell count j={j}", len(shell) <= 8 * j)
        require(f"k={k}, exact shell distance j={j}",
                all((a - centre[0]) ** 2 + 144 * (b - centre[1]) ** 2 >= j*j
                    for a, b in shell))


# A noncommuting complete-source fixture, with a three-dimensional observation.
I = sp.I
T = sp.diag(1, 3, 5, 7)
S = sp.Matrix([[1, I, 0, sp.Rational(1, 2)],
               [0, 1, sp.Rational(2, 3), 0],
               [0, 0, 1, -I], [0, 0, 0, 1]])
G0 = 13*T + S.H*S
W = sp.Matrix([[1, I], [I, 2], [1, -1], [0, 1]])
GJ = (T.inv() + W*W.H).inv()
Lambda = sp.Matrix([[1, 0, I, 1], [0, 1, 1, 0], [1, I, 0, 2]])
roots = [3+I/4, 3-I/4, -3+I/4, -3-I/4]
U = sp.Matrix([[z**-1, z**-2] for z in roots])
F = Lambda*U
Q0 = (Lambda*G0.inv()*Lambda.H).inv()
HE0 = U.H*G0*U
HB0 = F.H*Q0*F
R = HB0.inv()*F.H*Q0
c_trace = sp.cancel(sp.trace(T.inv()*G0))
L_joint = sp.cancel(sp.trace(T*GJ.inv()))
scale = sp.Rational(7)
Gamma = max(sp.Rational(1), c_trace / scale)
a = sp.cancel(1/(scale*sp.trace(HB0.inv())))
b = sp.cancel(sp.trace(HE0)/scale)
d = sp.cancel(sp.trace(U.H*T*U))
lower_factor = a/max(sp.Rational(1), L_joint*Gamma)
upper_factor = b+d
require("The fixture retains noncommuting complete matrices", G0*GJ != GJ*G0)
zero("Exact observed left inverse", R*F-sp.eye(2))
zero("Exact canonical dual minimum", R*Q0.inv()*R.H-HB0.inv())
psd("Full-space trace order", c_trace*G0.inv()-T.inv())
psd("Original canonical lower scalar sandwich", HB0-a*scale*sp.eye(2))
psd("Original canonical upper scalar sandwich", b*scale*sp.eye(2)-HE0)
psd("Full source lower metric enclosure", GJ-T/L_joint)
psd("Full source upper metric enclosure", T-GJ)

for alpha in (sp.Rational(0), sp.Rational(1, 13), sp.Rational(1, 2), sp.Rational(1)):
    covariance = (1-alpha)*G0.inv()+alpha*GJ.inv()
    G = covariance.inv()
    QB = (Lambda*covariance*Lambda.H).inv()
    HE, HB = U.H*G*U, F.H*QB*F
    denominator = 1-alpha+alpha*L_joint*Gamma*scale
    harmonic = scale/(1-alpha+alpha*scale)
    psd(f"alpha={alpha}, full-space harmonic lower order", G-G0/denominator)
    psd(f"alpha={alpha}, whole observed lower order", QB-Q0/denominator)
    psd(f"alpha={alpha}, complete observation minimum", HE-HB)
    psd(f"alpha={alpha}, harmonic frame lower bound",
        HB-lower_factor*harmonic*sp.eye(2))
    psd(f"alpha={alpha}, harmonic frame upper bound",
        upper_factor*harmonic*sp.eye(2)-HE)
    psd(f"alpha={alpha}, all-activation relative observation",
        HB-(lower_factor/upper_factor)*HE)

# A sharp scalar clipping check is the equivalent rational denominator order.
for scalar in (sp.Rational(1), sp.Rational(3, 2), sp.Rational(19), sp.Rational(1000)):
    for alpha in (sp.Rational(0), sp.Rational(1, 1000), sp.Rational(1, 19),
                  sp.Rational(1, 2), sp.Rational(1)):
        denominator = 1-alpha+alpha*scalar
        maximum = max(sp.Rational(1), alpha*scalar)
        require(f"Scalar clipping: s={scalar}, alpha={alpha}",
                maximum <= denominator <= 2*maximum)

receipt = {
    "passed": True,
    "check_count": len(checks),
    "checks": checks,
    "scope": "Exact rational lattice products and complex rational auxiliary full-source matrices; no native arithmetic moments, period, limiting coefficient, or eventual hard-gap claim is numerically certified.",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(HERE / "HARMONIC_EXACT_CHECKS.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps({"passed": True, "check_count": len(checks)}))
