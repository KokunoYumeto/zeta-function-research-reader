"""Exact finite regression checks; the companion Markdown contains the proof."""
from pathlib import Path
import json
import sympy as sp


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trunc(expr, z, m):
    return sp.series(expr, z, 0, m).removeO().expand()


def mult(expr, z, m):
    return sp.Matrix(m, m, lambda i, j:
                     trunc(expr * z**j, z, m).coeff(z, i))


def equal(left, right):
    return left.shape == right.shape and all(
        sp.expand(entry) == 0 for entry in left-right)


z = sp.Symbol("z")
receipts = []
for m in (1, 2, 3, 4):
    # Independent paired germs satisfy the exact reflection identity;
    # these are regression fixtures, not assertions of actual multiple zeros.
    unit = sum((j + 2 + sp.I * (2*j + 1))*z**j for j in range(m + 1))
    other = (-1)**m * sp.conjugate(unit.subs(z, -sp.conjugate(z))).expand()
    units = [unit, other]
    inv = [trunc(1/u, z, m) for u in units]
    gram = sp.zeros(2*m)
    for b in range(2):
        for i in range(m):
            for j in range(m):
                degree = m - 1 - i - j
                gram[(1-b)*m+i, b*m+j] = (
                    (-1)**i * inv[b].coeff(z, degree)
                    if degree >= 0 else 0)
    require(equal(gram.conjugate().T, -gram), f"skew sign m={m}")
    require(gram.det() != 0, f"perfectness m={m}")
    nlocal = mult(z, z, m)
    nilpotent = sp.diag(nlocal, nlocal)
    derivative = sp.diag(*[mult(sp.diff(u*z**m, z), z, m) for u in units])
    trace_form = (gram * derivative).applyfunc(sp.expand)
    require(equal(trace_form.conjugate().T, trace_form), f"trace sign m={m}")
    require(trace_form.rank() == 2, f"trace rank m={m}")
    require(equal(trace_form * nilpotent, sp.zeros(2*m)), f"radical m={m}")
    for q in (sp.Rational(2), sp.Rational(3, 2)):
        c = sp.diag(*([q**(-j) for j in range(m)] * 2))
        kappas = [trunc(q**(1-m) * u/u.subs(z, q*z), z, m) for u in units]
        k = sp.diag(*[mult(kappa, z, m) for kappa in kappas])
        adjoint = k * c.inv()
        require(equal(c.conjugate().T * gram * c, gram * k),
                f"Jacobian m={m},q={q}")
        require(equal(c.conjugate().T * gram, gram * adjoint),
                f"adjoint m={m},q={q}")
        require(equal(adjoint * derivative * c, derivative),
                f"derivative contraction m={m},q={q}")
        require(equal(c * nilpotent * c.inv(), nilpotent/q),
                f"nilpotent conjugation m={m},q={q}")
        require(equal(c.conjugate().T * trace_form * c, trace_form),
                f"trace invariance m={m},q={q}")
        reflected_kappa = sp.conjugate(
            kappas[1].subs(z, -sp.conjugate(z))).expand()
        require(sp.expand(reflected_kappa - kappas[0]) == 0,
                f"kappa dagger m={m},q={q}")
        # A missing dz Jacobian is decisively wrong, including at m=1.
        require(not equal(c.conjugate().T * gram * c, gram * (k/q)),
                f"missing Jacobian mutation escaped m={m},q={q}")
        if m > 1:
            require(not equal(c.conjugate().T * gram * c, gram),
                    f"false full-residue isometry m={m},q={q}")
            # Swapping the factors in the adjoint fails on nonconstant units.
            require(not equal(c.conjugate().T * gram, gram * (c.inv()*k)),
                    f"adjoint-order mutation escaped m={m},q={q}")
        receipts.append({"m":m, "q":str(q), "status":"pass"})

result = {
    "status": "pass",
    "fixtures": "formal paired units retaining nonconstant complex coefficients",
    "scope": "finite exact regression evidence, not actual zero multiplicity claims",
    "runs": receipts,
    "proof": "GERM_PAIRING_CHECK.md",
}
out = Path(__file__).with_name("GERM_PAIRING_CHECK_RECEIPT.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
