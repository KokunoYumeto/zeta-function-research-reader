"""Read-only independent rational and determinant replay of endpoint Weil balls.

Does not import the production Gram builder, its basis construction, or LDL.
Numerical quadrature has its own two combined-correlation cross-checks and may
be rerun separately. Here FLINT determinants replace Python LDL elimination.
"""
import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
from resource_ceiling import install_memory_ceiling
RESOURCE = install_memory_ceiling()
import hashlib
import json
from pathlib import Path
import sympy as sp
from flint import arb, acb, acb_mat, ctx

HERE=Path(__file__).resolve().parent


def run():
    ctx.prec=384
    ctx.threads=1
    receipt=json.loads((HERE/"endpoint_weil_results.json").read_text(encoding="utf-8"))
    for name, expected in receipt["source_hashes"].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected
    assert receipt["resource"]["ceiling_bytes"]==5_000_000_000
    assert receipt["resource"]["status"]=="enforced_windows_job"
    assert receipt["zero_ordinates_used"] is False
    def ball(q):
        q=sp.Rational(q)
        return arb(int(q.p))/int(q.q)
    n=17
    z=sp.symbols("z")
    # Independent moment generating function of four centered uniforms.
    mgf=sp.series((sp.sinh(z/2)/(z/2))**4,z,0,5).removeO()
    d=[sp.Rational(j-8,4) for j in range(n)]
    m=sp.Matrix([[sum(sp.binomial(k,r)*sp.factorial(r)*mgf.coeff(z,r)*s**(k-r)
                      for r in range(k+1)) for s in d] for k in range(5)])
    assert m==sp.Matrix(receipt["moment_matrix"])
    cols=receipt["basis_columns"]+receipt["complementary_jet_columns"]
    s=sp.Matrix.hstack(*(sp.Matrix(c) for c in cols))
    target=sp.zeros(5,n)
    target[0,0]=1
    for j in range(4): target[j+1,13+j]=1
    assert m*s==target and s.det()!=0
    # Exact signed-mollifier moments, independently of its analytic bump.
    mu2,mu4=sp.symbols('mu2 mu4',real=True)
    moments=[1,0,mu2,0,mu4]
    terms=[(0,1),(2,-mu2/2),(4,mu2**2/4-mu4/24)]
    for j in range(5):
        moment=sum(c*(-1)**r*sp.factorial(j)/sp.factorial(j-r)*moments[j-r]
                   for r,c in terms if r<=j)
        assert sp.expand(moment)==int(j==0)
    entries=[]
    for k,row in enumerate(receipt["entries"]):
        assert sp.Rational(row["d"])==sp.Rational(k,4) and row["T"]==-2
        g=acb(arb(row["real"]),arb(row["imag"]))
        entries.append((acb(0,ball(sp.Rational(k,2)))).exp()*g)
    g=acb_mat([[entries[j-i] if j>=i else entries[i-j].conjugate()
               for j in range(n)] for i in range(n)])
    sb=acb_mat([[ball(v) for v in row] for row in s.tolist()])
    h=sb.transpose()*g*sb
    determinants=[]
    for k in range(1,n+1):
        determinant=acb_mat([[h[i,j] for j in range(k)] for i in range(k)]).det()
        assert determinant.imag.contains(0) and determinant.real>0, (k,determinant)
        determinants.append(str(determinant.real))
    constrained=acb_mat([[h[i,j] for j in range(13)] for i in range(13)])
    inverse=constrained.inv()
    minimum=1/inverse[0,0]
    assert minimum.imag.contains(0) and minimum.real>0
    assert minimum.real.overlaps(arb(receipt["unit_zeroth_value_minimum"]))
    assert any(not h[0,j].contains(0) for j in range(1,13))
    for row in receipt["direct_combined_correlation_checks"]:
        assert arb(row["value"]).overlaps(arb(row["gram_value"]))
    return {"status":"pass","exact_full_channel_rank":17,"exact_moment_rank":5,
            "signed_smoothing_exact_moments":5,
            "independent_positive_leading_determinants":17,
            "unit_mass_minimum_by_inverse":str(minimum.real),
            "leading_determinants":determinants,"resource":RESOURCE,
            "numerical_scope":"saved full-form balls; determinant/inverse replay independent of production LDL",
            "RH_counterexample":False}


if __name__=="__main__":
    print(json.dumps(run()))
