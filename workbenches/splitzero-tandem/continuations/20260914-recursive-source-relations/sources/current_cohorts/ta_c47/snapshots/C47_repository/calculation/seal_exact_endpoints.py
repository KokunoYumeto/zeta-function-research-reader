"""Seal compact exact-rational comparisons and source provenance."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, sys, flint
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parent
def q(d):
    den=int(d["denominator"])
    if den<=0:
        raise ArithmeticError("Nonpositive rational denominator")
    return Fraction(int(d["numerator"]),den)
def interval(d):
    lo,hi=q(d["lower"]),q(d["upper"])
    if lo>hi:
        raise ArithmeticError("Reversed interval")
    return lo,hi
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
big=json.loads((ROOT/"certificate_dimension16_1024.json").read_text())
small=json.loads((ROOT/"certificate_dimension2_256.json").read_text())
source_sha=sha(ROOT/"certify_theta_hankel.py")
if big["source_sha256"]!=source_sha or small["source_sha256"]!=source_sha:
    raise ArithmeticError("Source pins do not match both runs")
if big["status"]!="positive_definite_certified":
    raise ArithmeticError("Large run did not certify")
bounds=[]
for shift,pivot_bounds,det_bounds in [
    ("0",(Fraction(6,10**107),Fraction(7,10**107)),(Fraction(9,10**822),Fraction(10,10**822))),
    ("1",(Fraction(7,10**111),Fraction(8,10**111)),(Fraction(6,10**878),Fraction(7,10**878)))
]:
    rows=big["matrices"][shift]["rows"]
    if len(rows)!=16:
        raise ArithmeticError("Wrong matrix dimension")
    for row in rows:
        for key in ["pivot","leading_determinant"]:
            lo,hi=interval(row[key])
            if lo<=0:
                raise ArithmeticError("Nonpositive certified lower endpoint")
    for name,coarse in [("pivot",pivot_bounds),("leading_determinant",det_bounds)]:
        lo,hi=interval(rows[-1][name])
        if not coarse[0]<lo<=hi<coarse[1]:
            raise ArithmeticError("Simple rational bound failed")
        bounds.append({"shift":int(shift),"object":name,
                       "strict_lower":str(coarse[0]),"strict_upper":str(coarse[1]),
                       "verified_from_exact_endpoint_fractions":True})
for j in range(5):
    blo,bhi=interval(big["moments"][j]["moment"])
    slo,shi=interval(small["moments"][j]["moment"])
    if not slo<=blo<=bhi<=shi:
        raise ArithmeticError("Higher precision moment is not nested in initial run")
receipt={
    "status":"PASS",
    "certificate_sha256":sha(ROOT/"certificate_dimension16_1024.json"),
    "source_sha256":source_sha,
    "small_certificate_sha256":sha(ROOT/"certificate_dimension2_256.json"),
    "python_flint_version":flint.__version__,
    "flint_version":flint.__FLINT_VERSION__,
    "verified_positive_pivot_lower_endpoints":32,
    "verified_positive_leading_determinant_lower_endpoints":32,
    "coarse_bounds":bounds,
    "five_small_moments_contain_larger_run_moments":True,
    "scope":"Exact rational comparisons and provenance; independent full recurrence replay is separately recorded by the parent.",
    "independent_review_sha256":sha(ROOT/"INDEPENDENT_TAIL_REVIEW.md"),
    "method_proof_sha256":sha(ROOT/"CERTIFIED_ORIGINAL_THETA_HANKEL.md"),
}
(ROOT/"EXACT_ENDPOINT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,indent=2))

