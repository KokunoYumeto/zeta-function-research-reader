"""Exact complex-rational diagnostics; complete proofs are in the TeX sources."""
from pathlib import Path
import json
import sympy as S

def clean(x):
    return S.cancel(S.expand_complex(x))

def scalar(x):
    return clean(x[0])

def mat(x):
    return x.applyfunc(clean)

j = S.I
B = S.Matrix([[2, 1+j, 0], [0, 3, 1-j], [1, 0, 2]])
G = mat(B.H*B + S.eye(3))
b, v = S.Matrix([1+j, 2-j, 1]), S.Matrix([2-j, 1+2*j, 3])
omega = S.Rational(7, 3)
beta, E = scalar(b.H*G*b), scalar(v.H*G*v)
r = clean(omega/(omega+beta))
Gnext = mat(G-G*b*b.H*G/(omega+beta))
Enext = scalar(v.H*Gnext*v)
s = scalar(b.H*G*v)
p2 = clean(S.conjugate(s)*s/(E*beta))
eta = clean((1-r)*p2)
checks = []
for rank in range(4):
    I = S.eye(3)[:, :rank]
    H = mat(I.H*G*I)
    Hnext = mat(I.H*Gnext*I)
    P = mat(I*H.inv()*I.H*G) if rank else S.zeros(3)
    Pnext = mat(I*Hnext.inv()*I.H*Gnext) if rank else S.zeros(3)
    dK = clean(Hnext.det()/H.det()) if rank else S.Integer(1)
    alpha = clean(scalar(b.H*G*P*b)/beta)
    theta = clean(scalar(v.H*G*P*v)/E)
    thetanext = clean(scalar(v.H*Gnext*Pnext*v)/Enext)
    V = clean(scalar(b.H*G*P*v)/s)
    snext = scalar(b.H*Gnext*v)
    U = clean(scalar(b.H*Gnext*Pnext*v)/snext)
    p1next = clean(S.conjugate(snext)*snext/(Enext*scalar(b.H*Gnext*b)))
    pinext = clean(scalar(b.H*Gnext*Pnext*b)/scalar(b.H*Gnext*b))
    sb = scalar(b.H*G*(S.eye(3)-P)*v)
    sbnext = scalar(b.H*Gnext*(S.eye(3)-Pnext)*v)
    equalities = {
        "restriction_ratio": dK-(1-(1-r)*alpha),
        "adjacent_response": U-(1-(1-V)/dK),
        "class_energy": Enext/E-(1-eta),
        "theta": (1-eta)*(1-thetanext)-(1-theta-eta*(1-V)*S.conjugate(1-V)/dK),
        "boundary_energy": p1next-r*p2/(1-eta),
        "quotient_numerator": sbnext-r*sb/dK,
        "next_kernel_boundary_energy": pinext-r*alpha/dK,
        "quotient_ratio_from_next_kernel_energy": r/dK-(r+(1-r)*pinext),
    }
    for name, expression in equalities.items():
        ok = clean(expression) == 0
        checks.append(dict(rank=rank, identity=name, exact_zero=bool(ok)))
        if not ok:
            raise AssertionError((rank, name, clean(expression)))
result = {
    "status": str(len(checks))+" exact rational complex-algebra checks passed",
    "scope": "Conjugation, source transport and empty/full-kernel diagnostics; not hypothetical-zeta numerical data or asymptotic verification.",
    "G": str(G), "b": str(b), "v": str(v), "omega": str(omega),
    "checks": checks,
}
Path(__file__).with_name("OBSERVATION_UPDATE_CHECKS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf8")
print(result["status"])
