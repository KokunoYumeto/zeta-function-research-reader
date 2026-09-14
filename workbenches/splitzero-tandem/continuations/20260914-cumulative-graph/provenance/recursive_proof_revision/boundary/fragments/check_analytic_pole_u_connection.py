"""Exact symbolic checks for APU1--23; fixtures are not asserted zeta packets."""
from pathlib import Path
import json
import sympy as S

root = Path(__file__).resolve().parent
s, p, u, t, c = S.symbols("s p u t c")
rows = []

def zero(expr):
    return S.cancel(S.expand(expr)) == 0

def matrix_zero(mat):
    return all(zero(e) for e in mat)

for d in range(1, 5):
    aa = S.symbols("a0:" + str(d))
    h = s**d + sum(aa[j]*s**j for j in range(d))
    phase = S.integrate(h, s) + c
    f = phase - t*s
    hh = h-t
    n = d+1
    def vec(poly):
        return S.Matrix([S.expand(poly).coeff(s, j) for j in range(d)])
    ccols, bcols, acols = [], [], []
    for b in range(d):
        qb, cb = S.div(f*s**b, hh, s)
        ccols.append(vec(cb))
        bcols.append(vec(S.diff(qb,s)))
        acols.append(vec(S.rem(s**(b+1),hh,s)))
    C = S.Matrix.hstack(*ccols)
    B = S.Matrix.hstack(*bcols)
    A = S.Matrix.hstack(*acols)
    e0 = S.eye(d)[:,0]
    fp = f.subs(s,p)
    qp = S.cancel((f-fp)/(s-p))
    quotient, remainder = S.div(qp,hh,s)
    Q = vec(remainder)
    Omega_u = (-C/u**2+B/u).row_join(-Q/u**2)
    Omega_u = Omega_u.col_join(S.zeros(1,d).row_join(S.Matrix([[-fp/u**2]])))
    Aext = A.row_join(e0).col_join(S.zeros(1,d).row_join(S.Matrix([[p]])))
    Omega_t = -Aext/u
    curvature = Omega_t.diff(u)-Omega_u.diff(t)+Omega_u*Omega_t-Omega_t*Omega_u
    flags = {
        "constant_quotient": zero(quotient-S.Rational(1,n)),
        "pole_remainder": zero(remainder-(qp-hh/S.Integer(n))),
        "pole_remainder_t": matrix_zero(Q.diff(t)+S.Rational(d,n)*e0),
        "polynomial_constant_column": matrix_zero(B*e0-e0/S.Integer(n)),
        "exact_extension_identity": matrix_zero((A-p*S.eye(d))*Q-C*e0+fp*e0),
        "full_matrix_curvature": matrix_zero(curvature),
    }
    # Parameter-dependent rational representatives check the degree correction.
    test = u*t*s**2 + u/(s-p) + t/(s-p)**3
    Dop = lambda x: u*S.diff(x,s)+hh*x
    Du0 = lambda x: S.diff(x,u)-f*x/u**2+x/u
    Du1 = lambda x: S.diff(x,u)-f*x/u**2
    Dt = lambda x: S.diff(x,t)-s*x/u
    flags["u_chain"] = zero(Du1(Dop(test))-Dop(Du0(test)))
    flags["t_chain"] = zero(Dt(Dop(test))-Dop(Dt(test)))
    flags["flat_representative"] = zero(Du1(Dt(test))-Dt(Du1(test)))
    # The original unit is fixed, with its repeated pole retained.
    nu = (s-p)**2
    Dnu = lambda x: u*S.diff(x,s)+(hh-u*S.diff(nu,s)/nu)*x
    flags["full_gauge"] = zero(Dnu(nu*test)-nu*Dop(test))
    flags["gauge_u_chain"] = zero(Du1(Dnu(test))-Dnu(Du0(test)))
    # Factor out the common nonzero exp(fp/u) only for checking the equality.
    R = S.zeros(1,d).row_join(S.ones(1,1))
    flags["weighted_residue_u"] = matrix_zero(-fp*R/u**2-R*Omega_u)
    flags["weighted_residue_t"] = matrix_zero(-p*R/u-R*Omega_t)
    rows.append({"degree": d, "generic_coefficients": [str(a) for a in aa],
                 "checks": flags, "passed": all(flags.values())})

result = {
    "scope": "Generic monic degree 1--4 polynomial identities, fixed pole; no arithmetic-zero fixture claim.",
    "rows": rows,
    "passed": all(row["passed"] for row in rows),
    "check_count": sum(len(row["checks"]) for row in rows),
}
output = root/"analytic_pole_u_connection_exact_checks.json"
output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"passed": result["passed"], "check_count": result["check_count"],
                  "output": str(output)}))
if not result["passed"]:
    raise SystemExit(1)
