"""Independent exact checks of the original PCL first variation.

This script derives entries from the defining finite coefficient sum.
It does not execute any script supplied by an incoming proof note.
"""
import json
from pathlib import Path
import sympy as s

checks = []


def equal(name, lhs, rhs):
    difference = s.factor(s.together(lhs-rhs))
    assert difference == 0, (name, difference)
    checks.append({"name": name, "passed": True})


beta, eta = s.symbols("beta eta")


def pcl_coefficient(a, r, n):
    degree = 5*n+r+1-a
    value = 0
    for h in range(max(0, degree//4)+1):
        for p in range(max(0, degree//2)+1):
            if 2*p+4*h != degree:
                continue
            ell = p+h-n
            assert ell >= 0
            value += (beta**p*eta**h /
                      (3**p*s.factorial(p)*s.factorial(h)) *
                      (-1)**ell*5**ell*s.rf(s.Rational(a, 5), ell))
    return s.factor(value)


J = s.eye(4)
J[0, 2] = -beta/3
J[1, 3] = -2*beta/3
J_derived = s.Matrix(4, 4, lambda i, j: pcl_coefficient(i+1, j, 0))
R1 = s.Matrix(4, 4, lambda i, j: pcl_coefficient(i+1, j, 1))
R1_claimed = s.Matrix([
    [0, beta*(beta**2-9*eta)/27, 0,
     -(11*beta**4-108*beta**2*eta+162*eta**2)/324],
    [-(beta**2-9*eta)/9, 0, beta*(7*beta**2-54*eta)/81, 0],
    [0, -(beta**2-6*eta)/6, 0, beta*(4*beta**2-27*eta)/27],
    [beta/3, 0, -(2*beta**2-9*eta)/9, 0],
])
for i in range(4):
    for j in range(4):
        equal(f"PCL constant ({i+1},{j+1})", J_derived[i,j], J[i,j])
        equal(f"PCL first variation ({i+1},{j+1})", R1[i,j], R1_claimed[i,j])
K = R1*J.inv()
equal("K23", K[1,2], beta*(4*beta**2-27*eta)/81)
equal("K14", K[0,3], -(beta**4-12*beta**2*eta+54*eta**2)/108)

R, T, p, b = s.symbols("R T p b", nonzero=True)
u, v = (2*R-T)/3, (2*T-R)/3
e0, e1, e2 = p-b, p*u-b*v, p*u**2-b*v**2
o0, o1, o2 = -p*R+b*T, p*R*v-b*T*u, -p*R*v**2+b*T*u**2
equal("even determinant", e0*e2-e1**2, -p*b*(R-T)**2)
equal("odd determinant", o0*o2-o1**2, -p*b*R*T*(R-T)**2)
equal("coordinate-line obstruction", T*u**2-R*v**2,
      -(R-T)*(R**2-7*R*T+T**2)/9)
factor = R**4-23*R**3*T+33*R**2*T**2-23*R*T**3+T**4
equal("exceptional full factorization", T*u**4-R*v**4, -(R-T)*factor/81)
equal("exceptional symmetric polynomial", factor,
      (R+T)**4-27*(R+T)**2*R*T+81*R**2*T**2)
equal("retained-phase squared ratio", (o1**2-R*T*e1**2).subs(b,p*u**2/v**2),
      p**2*(R-T)**2*(R**2-7*R*T+T**2)*factor/(9*(R-2*T)**4))
x = s.symbols("x")
negative_branch = -(x**4-12*x**2+54)/108-x*(4*x**2-27)/81
numerator = s.together(negative_branch-(108-45*x)/324).as_numer_denom()[0]
equal("negative-branch reduction", s.rem(numerator, x**2+3*x-9, x), 0)
equal("positive exceptional root quadratic", (3*(s.sqrt(5)-1)/2)**2+
      3*(3*(s.sqrt(5)-1)/2)-9, 0)
payload = {
    "kind": "independent exact symbolic calculation",
    "check_count": len(checks),
    "all_passed": all(item["passed"] for item in checks),
    "checks": checks,
    "first_variation_matrix": str(R1),
    "scope": "Finite defining PCL sums and CP7-14 algebra; proofs in CR1-26 cover the module claims.",
}
Path(__file__).with_name("cofactor_first_variation_exact.json").write_text(
    json.dumps(payload, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"checks": len(checks), "all_passed": payload["all_passed"]}))
