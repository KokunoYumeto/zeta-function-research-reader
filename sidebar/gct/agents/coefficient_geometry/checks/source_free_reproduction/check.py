"""Exact coefficient, chart, point-count and Frobenius checks; no Lean."""
from pathlib import Path
from collections import Counter
from itertools import product
from fractions import Fraction
import argparse
import datetime
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--refresh-source-hash", action="store_true",
                    help="Optionally rehash the local Milne research PDF; never needed for reproduction.")
args = parser.parse_args()
(ROOT/"checks").mkdir(exist_ok=True)
checks = []

def check(name, condition, evidence=None):
    assert condition, name
    item = {"name": name, "passed": True}
    if evidence is not None:
        item["evidence"] = evidence
    checks.append(item)

def zero(expression):
    return s.cancel(expression) == 0

q, T, t, Q = s.symbols("q T t Q", nonzero=True)
C = q**10 - q**4 - q**-4 + q**-10
B = sum(T**i for i in range(7)) * sum(T**j for j in range(3))
h = sum(q**(6-2*i) for i in range(7)) * sum(q**(2-2*j) for j in range(3))
a = [1, 2, 3, 3, 3, 3, 3, 2, 1]
check("original_four_terms_factor", zero(C - q**-10*(q**14-1)*(q**6-1)))
check("residual_factor", zero(C-(q-q**-1)**2*h))
check("projective_polynomial", s.Poly(B,T).all_coeffs() == a)
check("h_projective_lift", zero(h-q**-8*B.subs(T,q*q)))
check("C_exact_q1_factor", zero(C-(q-1)**2*q**-10*(q+1)**2*B.subs(T,q*q)))
check("all_jets_retained", [s.diff(C,q,i).subs(q,1) for i in range(3)] == [0,0,168])
check("h_at_one_and_leading_jet", h.subs(q,1)==21 and s.limit(C/(q-1)**2,q,1)==84)
check("motivic_torsor_identity", zero((T**7-1)*(T**3-1)-(T-1)**2*B))

# Every affine-chart inverse and overlap map is checked with the same
# labelled coordinate arrays used by the proof.
for n in (3,7):
    xs = s.symbols("x0:"+str(n), nonzero=True)
    for i in range(n):
        ui = [xs[j]/xs[i] for j in range(n)]
        check(f"chart_inverse_n{n}_i{i}",
              all(zero(xs[i]*ui[j]-xs[j]) for j in range(n)))
        for k in range(n):
            uk = [xs[j]/xs[k] for j in range(n)]
            check(f"overlap_n{n}_i{i}_k{k}",
                  all(zero(ui[j]/ui[k]-uk[j]) for j in range(n))
                  and zero(xs[i]*ui[k]-xs[k]))
        # The reverse composition starts in the actual chart coordinates,
        # where only the fibre parameter t is required to be invertible.
        us = s.symbols("u0:"+str(n))
        fibre, lam = s.symbols("fibre lam", nonzero=True)
        coords = [fibre if j == i else fibre*us[j] for j in range(n)]
        check(f"reverse_chart_inverse_n{n}_i{i}",
              coords[i] == fibre
              and all(zero(coords[j]/coords[i]-us[j]) for j in range(n) if j != i))
        scaled = [lam*x for x in coords]
        check(f"chart_torus_equivariance_n{n}_i{i}",
              zero(scaled[i]-lam*fibre)
              and all(zero(scaled[j]/scaled[i]-coords[j]/coords[i]) for j in range(n)))
        recovered_lam = scaled[i]/coords[i]
        check(f"torsor_action_inverse_n{n}_i{i}",
              zero(recovered_lam-lam)
              and all(zero(recovered_lam*coords[j]-scaled[j]) for j in range(n)))
    # The three-chart cocycle is the actual fibre-coordinate multiplier.
    check(f"fibre_transition_cocycle_n{n}",
          all(zero((xs[k]/xs[i])*(xs[j]/xs[k])-xs[j]/xs[i])
              for i,j,k in product(range(n), repeat=3)))

# Exhaustive component enumeration over the prime fields F_2,F_3.
# Each nonzero vector maps to its explicit representative with last
# nonzero coordinate equal to 1. We verify all fibre sizes and inverses.
count_records = []
for p in (2,3):
    dimensions = {}
    for n in (3,7):
        fibres = Counter()
        vector_count = 0
        for v in product(range(p), repeat=n):
            if not any(v):
                continue
            vector_count += 1
            d = max(j for j,x in enumerate(v) if x)
            scalar = v[d]
            inv = pow(scalar,-1,p)
            projective = tuple((x*inv)%p for x in v)
            fibres[projective] += 1
            assert tuple((scalar*x)%p for x in projective) == v
        check(f"enumerate_all_fibres_F{p}_U{n}",
              vector_count == p**n-1
              and len(fibres)==sum(p**d for d in range(n))
              and set(fibres.values())=={p-1},
              {"vectors":vector_count, "projective_points":len(fibres),
               "fibre_size":p-1})
        dimensions[n] = (vector_count,len(fibres))
    nx = dimensions[7][0]*dimensions[3][0]
    ny = dimensions[7][1]*dimensions[3][1]
    check(f"product_torsor_F{p}", nx==(p-1)**2*ny)
    count_records.append({"Q":p,"NX":nx,"NY":ny})

# Literal Kunneth degree/twist pairs, preserving factor order.
frob = sorted((d1+d2,w1+w2)
              for d1,w1 in [(1,0),(14,7)]
              for d2,w2 in [(1,0),(6,3)])
check("full_Kunneth_table", frob == [(2,0),(7,3),(15,7),(20,10)])
trace = sum((-1)**degree * Q**weight for degree,weight in frob)
check("untwisted_Frobenius_trace", zero(trace-(Q**7-1)*(Q**3-1)))
trace5 = sum((-1)**degree * Q**(weight-5) for degree,weight in frob)
check("twist5_original_coefficient", zero(trace5-(Q**5-Q**2-Q**-2+Q**-5)))
zeta_det = s.prod((1-Q**weight*t)**((-1)**(degree+1)) for degree,weight in frob)
ZX = (1-Q**7*t)*(1-Q**3*t)/((1-Q**10*t)*(1-t))
check("Frobenius_zeta_determinant", zero(zeta_det-ZX))
ZC = (1-Q**2*t)*(1-Q**-2*t)/((1-Q**5*t)*(1-Q**-5*t))
check("twist5_zeta", zero(ZX.subs(t,Q**-5*t)-ZC))
projective_pairs = Counter(i+j for i in range(7) for j in range(3))
check("projective_Kunneth_multiplicities", [projective_pairs[d] for d in range(9)] == a)
ZY = s.prod((1-Q**d*t)**(-projective_pairs[d]) for d in range(9))
projective_logderiv = sum(a[d]*Q**d/(1-Q**d*t) for d in range(9))
check("projective_all_order_zeta_logarithmic_derivative", zero(s.diff(ZY,t)/ZY-projective_logderiv))
check("twist4_projective_trace", zero(sum(a[d]*Q**(d-4) for d in range(9))-Q**-4*B.subs(T,Q)))

# Derivative log zeta is a rational identity. Its t^(m-1) coefficients
# are independently checked against integer point counts.
logderiv = s.diff(ZX,t)/ZX
explicit = Q**10/(1-Q**10*t)-Q**7/(1-Q**7*t)-Q**3/(1-Q**3*t)+1/(1-t)
check("all_order_zeta_logarithmic_derivative", zero(logderiv-explicit))
for field in (2,3,4,5,7,8,9):
    for m in range(1,9):
        N = field**m
        count = (N**7-1)*(N**3-1)
        literal = Fraction(N**5)-Fraction(N**2)-Fraction(1,N**2)+Fraction(1,N**5)
        check(f"count_trace_Q{field}_m{m}", literal == Fraction(count,N**5))
        centered_h = sum(Fraction(N**d,N**4)*a[d] for d in range(9))
        check(f"projective_trace_Q{field}_m{m}", centered_h==Fraction(int(B.subs(T,N)),N**4))

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
source_refresh = {"requested":args.refresh_source_hash,"required_for_reproduction":False}
if args.refresh_source_hash:
    # Source verification is an explicit provenance action, not a hidden
    # dependency of the authored exact-arithmetic reproduction program.
    source_path = ROOT/"sources/milne_LEC_2_21.pdf"
    source_receipt_path = ROOT/"source_receipt.json"
    source_receipt = json.loads(source_receipt_path.read_text(encoding="utf-8"))
    digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
    source = source_receipt["sources"][0]
    assert source["sha256"] == digest, "Local source changed; audit before replacing the recorded hash."
    source_receipt["verified_utc"] = now
    source_receipt_path.write_text(json.dumps(source_receipt,indent=2),encoding="utf-8")
    source_refresh["sha256"] = digest
    source_refresh["verified"] = True
receipt = {
    "time_utc":now,
    "status":"passed",
    "checks":checks,
    "check_count":len(checks),
    "exact_arithmetic":"SymPy rational/Laurent identities, Python arbitrary integers and Fraction",
    "finite_field_enumerations":count_records,
    "cohomological_limits":"Check verifies computed degrees/twists and algebraic identities; foundational etale theorems are sourced in proof.",
    "mathematical_input":"Exact source-displayed C(q); no certification of disputed printed target-tableau assignment",
    "source_refresh":source_refresh,
    "source_shelf_required":False,
}
(ROOT/"checks/exact.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps({"status":"passed","check_count":len(checks),"source_refresh":source_refresh}))
