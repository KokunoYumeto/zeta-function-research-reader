"""Exact checks for the common torus, node divisor and induced modules."""
from pathlib import Path
import hashlib
import json
import sympy as S
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
u, v, R, T, a, eta, p, q, s, t, lam, mu = S.symbols(
    "u v R T a eta p q s t lam mu", nonzero=False
)
checks = {}

def check(name, expr):
    value = S.cancel(S.expand(expr))
    assert value == 0, (name, value)
    checks[name] = "passed"

node = S.groebner([u*v], u, v, domain=S.QQ)
r1, r2 = (u+v)/2, (v-u)/2
check("node_relation", node.reduce(S.expand(r1*r1-r2*r2))[1])
check("node_base", node.reduce(S.expand(-r1*r1+(u*u+v*v)/4))[1])
disc = lambda A,B,C,D: B*B*C*C-4*A*C**3-4*B**3*D-27*A*A*D*D+18*A*B*C*D
check("slice_discriminant", disc(0,-2,0,-2*a)+64*a)
check("node_discriminant", disc(0,-2,0,(u*u+v*v)/2)-16*(u*u+v*v))
psi = -2*R*R*T+(u*u+v*v)*T**3/2
check("common_torus_equivariance", psi.subs({R:eta**-1*R,T:eta**2*T}, simultaneous=True)
    -psi.subs({u:eta**3*u,v:eta**3*v}, simultaneous=True))
fatpoint = S.groebner([u*v,u*u+v*v],u,v,domain=S.QQ)
for name, poly in [("fatpoint_u_cube",u**3),("fatpoint_v_cube",v**3),
                    ("fatpoint_v_square",v*v+u*u)]:
    check(name,fatpoint.reduce(poly)[1])
g=S.Matrix([[p,q],[s,t]])
sigma=S.Matrix([[0,1],[1,0]])
diag=S.diag(lam,mu)
J=S.diag(1,-1)
Z=g*J*g.inv()
for i in range(2):
    for j in range(2):
        check(f"adjoint_torus_{i}_{j}", (g*diag*J*(g*diag).inv()-Z)[i,j])
        check(f"adjoint_swap_{i}_{j}", (g*sigma*J*(g*sigma).inv()+Z)[i,j])
check("induced_torsion_torus",(g*diag).det()/(lam*mu)-g.det())
check("induced_torsion_swap",-(g*sigma).det()-g.det())
# Differential Hilbert dimensions are computed as homogeneous relation ranks.
hilbert=[]
for n in range(1,9):
    # Ambient degree n consists of R_{n-1} du and R_{n-1} dv.
    monomials=[S.Integer(1)] if n==1 else [u**(n-1),v**(n-1)]
    basis=[(i,m) for i in range(2) for m in monomials]
    relcoeffs=[]
    relation_monomials=[] if n<2 else ([S.Integer(1)] if n==2 else [u**(n-2),v**(n-2)])
    for coeff in relation_monomials:
        entries=[node.reduce(S.expand(coeff*v))[1], node.reduce(S.expand(coeff*u))[1]]
        relcoeffs.append([S.expand(entries[i]).coeff(m) if m!=1 else entries[i] for i,m in basis])
    rank=S.Matrix(relcoeffs).rank() if relcoeffs else 0
    dimension=len(basis)-rank
    assert dimension == (3 if n==2 else 2), (n,dimension)
    hilbert.append({"degree":n,"dimension":dimension,"relation_rank":rank})
checks["differential_hilbert_degrees_1_through_8"]="passed"
receipt={"status":"passed","checked_at_utc":datetime.now(timezone.utc).isoformat(),
         "check_count":len(checks),"checks":checks,"hilbert":hilbert,
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "sympy_version":S.__version__,"scope":"Exact rational symbolic identities; written proofs give all-degree and module conclusions."}
(HERE/"supplement_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"passed","check_count":len(checks)}))
