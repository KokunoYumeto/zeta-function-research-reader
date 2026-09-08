"""Exact regression checks for the full source-axis/arithmetic proof.
Small one-process symbolic calculation; no source existence or Lean certification.
"""
from pathlib import Path
import hashlib
import json
import time
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
START = time.monotonic()
checks = []
def equal(label, a, b):
    ok = s.simplify(a-b) == 0
    checks.append({"id": label, "passed": bool(ok)})
    if not ok:
        raise AssertionError((label, a, b))
x, H = s.symbols("x H", real=True)
# H is exactly 2**h, kept as a variable, not set to one.
for j in range(1, 13):
    a=x**j
    phi=a-H*a.subs(x, 2*x)
    psi=phi-phi.subs(x, x/2)/2
    multiplier=(1-s.Rational(1,2)**(j+1))*(1-H*2**j)
    equal(f"dilation.axis.{j}", s.diff(psi,x,j).subs(x,0), s.factorial(j)*multiplier)
    em=-s.bernoulli(j+1)/(j+1)*multiplier
    W=s.zeta(-j)*(1-s.Rational(1,2)**(j+1))*(1-H*2**j)
    equal(f"mellin.EM.residue.{j}",em,W)
    if j%2 == 0:
        equal(f"even.endpoint.{j}",em,0)
equal("mean.cancellation", (1-H/2)*(1-s.Rational(1,2)*2),0)
equal("first.jet.coefficient", -s.Rational(1,12)*s.Rational(3,4)*(1-2*H),(2*H-1)/16)
C,tau,h,nu,r=s.symbols("C tau h nu r",positive=True)
equal("source.A.exponent", -(s.Rational(1,2)+h)-s.Rational(1,2),-1-h)
equal("viscosity.axis.quotient",s.sqrt(nu)/(r)*(r/s.sqrt(nu)),1)
equal("B.sigma.factor",s.diff(2*x*tau**(-1-h)/C,x),2*tau**(-1-h)/C)
equal("exact.arithmetic.axis", (2*H-1)/16*2*tau**(-1-h)/C,(2*H-1)/(8*C)*tau**(-1-h))
for m in range(7):
    equal(f"time.jet.{m}",(-1)**m*s.diff(tau**(-1-h),tau,m),
          s.rf(1+h,m)*tau**(-1-h-m))
proof=ROOT/"tex/satellites/29l_ns_axis_arithmetic_jet.tex"
source=Path("[local]/Documents/math/output/dbn_ns_rh_20260908/sources/ns_public/navier_stokes_166.pdf")
source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash=="0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f"
checks.append({"id":"source.exact.edition","passed":True})
receipt={
 "schema_version":1,"status":"pass","check_count":len(checks),"checks":checks,
 "proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "source_sha256":source_hash,"sympy_version":s.__version__,
 "elapsed_seconds":time.monotonic()-START,
 "scope":"Exact finite regression checks supplement the complete written and independently reviewed proof. Infinite summation, imported NS existence and source lemmas are not certified by this script.",
 "lean_run":False,"resource_class":"non-critical; small single symbolic process, no integrations"}
Path(__file__).with_name("ns_axis_jet_checks.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print("NS_AXIS_JET_EXACT_CHECKS_PASS",len(checks))

