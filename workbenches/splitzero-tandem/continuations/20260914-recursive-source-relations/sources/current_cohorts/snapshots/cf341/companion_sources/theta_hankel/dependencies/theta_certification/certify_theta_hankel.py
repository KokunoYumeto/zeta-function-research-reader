"""Certified original theta moments and unscaled logarithmic Hankel matrices.

Finite integrals are validated by python-flint/Arb; omitted positive tails
are explicitly enclosed.  No zero ordinates enter this computation.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, sys, time
from pathlib import Path
import flint
from flint import arb, acb, ctx

# The explicit y-tail is about exp(-pi*exp(8)); its exact dyadic
# denominator legitimately exceeds Python's default 4300-digit limit.
sys.set_int_max_str_digits(100000)


def exact_dyadic(x):
    m, e = x.man_exp()
    m, e = int(m), int(e)
    return {"numerator": str(m << e) if e >= 0 else str(m),
            "denominator": "1" if e >= 0 else str(1 << -e)}


def enclosure(x):
    if not x.is_finite():
        raise ArithmeticError("Nonfinite real enclosure")
    return {"lower": exact_dyadic(x.lower()), "upper": exact_dyadic(x.upper()),
            "display": x.str(35), "relative_accuracy_bits": x.rel_accuracy_bits()}


def from_enclosure(d):
    lo = arb(d["lower"]["numerator"]) / arb(d["lower"]["denominator"])
    hi = arb(d["upper"]["numerator"]) / arb(d["upper"]["denominator"])
    return lo.union(hi)


def positive_tails(J, N, length):
    pi, L = arb.pi(), arb(length)
    ratio_n = (arb(4)/N - 2*pi*N).exp()
    ratio_y = (4-2*pi).exp()
    decay = 2*pi*(2*L).exp() - arb(9)/2 - arb(J)/L
    if not (1-ratio_n > 0 and 1-ratio_y > 0 and decay > 0):
        raise ArithmeticError("Unproved tail denominator sign")
    tn = 16*pi*pi*L**(J+1)*(arb(9)*L/2).exp()*N**4*(-pi*N*N).exp()/(1-ratio_n)
    ty = 16*pi*pi*L**J*(arb(9)*L/2-pi*(2*L).exp()).exp()/((1-ratio_y)*decay)
    return tn, ty, decay


def compute_moment(J, N, length, target_bits):
    pi = arb.pi()
    evaluations = 0
    def integrand(y, analytic):
        # Integer powers, sums, products and exponentials are entire. Thus
        # the function is analytic on every ball, including analytic=True.
        nonlocal evaluations
        evaluations += 1
        e2 = (2*y).exp()
        ehalf = (y/2).exp()
        theta = acb(0)
        for n in range(1, N):
            x = pi*n*n*e2
            theta += (16*x*x-24*x)*(-x).exp()
        return y**J * ehalf * theta
    tol = arb(2)**(-target_bits)
    start = time.monotonic()
    # Short exact rational subintervals reduce analytic-ball overestimation.
    pieces = []
    total = acb(0)
    for j in range(2*length):
        value = acb.integral(integrand, arb(j)/2, arb(j+1)/2,
                             rel_tol=tol, abs_tol=tol,
                             eval_limit=200000, depth_limit=50)
        if not value.is_finite() or not value.imag.contains(0):
            raise ArithmeticError("Nonfinite integral or imaginary exclusion of zero")
        pieces.append({"left": f"{j}/2", "right": f"{j+1}/2",
                       "real": enclosure(value.real), "imag": enclosure(value.imag)})
        total += value
    tn, ty, decay = positive_tails(J, N, length)
    tail_upper = (tn+ty).upper()
    tail_interval = arb(0).union(tail_upper)
    result = total.real + tail_interval
    if not result > 0:
        raise ArithmeticError("Moment positivity not certified")
    return result, {"J": J, "finite_integral": enclosure(total.real),
                    "finite_imaginary": enclosure(total.imag), "pieces": pieces,
                    "omitted_n_bound": enclosure(tn), "omitted_y_bound": enclosure(ty),
                    "decay_denominator": enclosure(decay),
                    "tail_interval": enclosure(tail_interval), "moment": enclosure(result),
                    "evaluations": evaluations, "seconds": time.monotonic()-start}


def logarithmic_coefficients(moments):
    a = [((-1)**j)*v/math.factorial(2*j) for j,v in enumerate(moments)]
    if not a[0] > 0:
        raise ArithmeticError("Original a0 is not certified positive")
    b = []
    for n in range(len(a)-1):
        b.append((-(n+1)*a[n+1]-sum((a[j]*b[n-j] for j in range(1,n+1)), arb(0)))/a[0])
    return a, b


def ldlt(b, dimension, shift):
    matrix = [[b[i+j+shift] for j in range(dimension)] for i in range(dimension)]
    lower = [[arb(int(i==j)) for j in range(dimension)] for i in range(dimension)]
    diag, rows, determinant = [], [], arb(1)
    for j in range(dimension):
        pivot = matrix[j][j]-sum((lower[j][k]**2*diag[k] for k in range(j)), arb(0))
        if not pivot > 0:
            return {"status":"positivity_not_certified", "failed_pivot_index":j,
                    "failed_pivot":enclosure(pivot), "rows":rows}
        diag.append(pivot)
        determinant *= pivot
        rows.append({"dimension":j+1,"pivot":enclosure(pivot),
                     "leading_determinant":enclosure(determinant)})
        for i in range(j+1,dimension):
            lower[i][j]=(matrix[i][j]-sum((lower[i][k]*lower[j][k]*diag[k] for k in range(j)),arb(0)))/pivot
    return {"status":"positive_definite_certified","rows":rows,
            "L":[[enclosure(v) for v in row] for row in lower]}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--dimension",type=int,default=16)
    p.add_argument("--precision",type=int,default=1024)
    p.add_argument("--target-bits",type=int,default=850)
    p.add_argument("--first-omitted-n",type=int,default=20)
    p.add_argument("--length",type=int,default=4)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    if args.dimension<1 or args.precision<128 or args.target_bits<64 or args.target_bits>args.precision-32:
        p.error("Invalid dimension or precision")
    if args.first_omitted_n<1 or args.length<1:
        p.error("Invalid truncation")
    ctx.prec=args.precision
    args.output.parent.mkdir(parents=True,exist_ok=True)
    result={"status":"running","python_version":sys.version,"platform":platform.platform(),
            "python_flint_version":flint.__version__,"precision_bits":ctx.prec,
            "target_bits":args.target_bits,"dimension":args.dimension,
            "first_omitted_n":args.first_omitted_n,"length":args.length,
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "method":"Arb acb.integral with entire combined theta integrand and explicit positive tails",
            "moments":[]}
    moments=[]
    started=time.monotonic()
    for J in range(0,4*args.dimension+1,2):
        moment,row=compute_moment(J,args.first_omitted_n,args.length,args.target_bits)
        moments.append(moment); result["moments"].append(row)
        args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        print(f"M_{J}: {moment.str(20)}; bits={moment.rel_accuracy_bits()}; seconds={row['seconds']:.2f}",flush=True)
    a,b=logarithmic_coefficients(moments)
    result["a"]=[enclosure(v) for v in a]
    result["b"]=[enclosure(v) for v in b]
    result["matrices"]={str(shift):ldlt(b,args.dimension,shift) for shift in (0,1)}
    result["status"]="positive_definite_certified" if all(v["status"]=="positive_definite_certified" for v in result["matrices"].values()) else "moments_certified_matrix_positivity_unresolved"
    result["seconds"]=time.monotonic()-started
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(result["status"],flush=True)
    for shift,mat in result["matrices"].items():
        print("shift",shift,"positive pivots",len(mat["rows"]),"of",args.dimension,flush=True)


if __name__=="__main__":
    main()
