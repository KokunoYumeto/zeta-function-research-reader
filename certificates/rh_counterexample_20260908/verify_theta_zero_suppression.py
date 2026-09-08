"""Full Weil Gram for the actual source input and its first-zero suppression.

No RH assumption or zero ordinates enter the quadrature.
q0 = w*g0; q1 = q0 + q0''/A, A=19979/100 exactly.
This explicit new operator does not rescale or replace the original source w.
All pole, gamma, prime, cross and infinite-tail terms are retained.
One numerical worker, using the existing 5,000,000,000-byte job ceiling.
"""
from pathlib import Path
import sys, json, hashlib, time, argparse
from fractions import Fraction
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "agents/connes_actual_input_review/actual_theta_weil"))
import verify_actual_theta_weil as base
from flint import arb, acb, ctx

ctx.prec = 224
ctx.threads = 1
ctx.cap = 4
A = arb(19979) / 100
D = arb(1) / 16
PI = arb.pi()
TOL = arb(2) ** -100
T = 64
N = 8
U = arb(3)
M = 16


def P_coeff(alpha, order):
    p = [Fraction(1)]
    for _ in range(order):
        out = [Fraction(0)] * (len(p) + 1)
        for k, c in enumerate(p):
            out[k] += (alpha + 2*k)*c
            out[k+1] -= 2*c
        p = out
    return p


POLYS = {(alpha, k): P_coeff(alpha, k)
         for alpha in (Fraction(9, 2), Fraction(5, 2)) for k in range(3)}


def poly_eval(coeff, z):
    out = acb(0)
    for c in reversed(coeff):
        out = out*z + arb(c.numerator)/c.denominator
    return out


def theta_derivative(v, k):
    e2 = (2*v).exp()
    e5 = (arb(5)/2*v).exp()
    e9 = e5*e2
    out = acb(0)
    for n in range(1, N+1):
        z = PI*n*n*e2
        out += (4*PI*PI*n**4*e9*poly_eval(POLYS[Fraction(9, 2), k], z)
                - 6*PI*n*n*e5*poly_eval(POLYS[Fraction(5, 2), k], z)) * (-z).exp()
    return out


def w_derivative(v, k):
    b = -acb(0, 3)
    out = (b*v).exp() * (b**k*(base.C0+acb(0, 1)*v/336)
            + (k*b**(k-1)*acb(0, 1)/336 if k else 0))
    for c, a in [(base.C1, arb(9)/2), (base.C2, arb(13)/2)]:
        d = -acb(0, a)
        out += c*d**k*(d*v).exp()
    return out


def q(v, reflection, index):
    g = [theta_derivative(reflection*v, k)*reflection**k for k in range(3 if index else 1)]
    result = w_derivative(v, 0)*g[0]
    if index:
        result += (w_derivative(v, 2)*g[0]+2*w_derivative(v, 1)*g[1]
                   + w_derivative(v, 0)*g[2])/A
    return result


def filter_symbol(z):
    return 1-z*z/A


def gamma_tail(order):
    _, d = base.gamma_tail()
    ck = arb(d["K_exponential_constant"])
    # |(1-t^2/A)^order| <= (1+t^2/A)^order on the real tail.
    coeff = [arb(0)]*(2*order+1)
    if order == 0:
        coeff[0] = arb(1)
    elif order == 1:
        coeff[0], coeff[2] = arb(1), 1/A
    else:
        coeff[0], coeff[2], coeff[4] = arb(1), 2/A, 1/(A*A)
    t = arb(T)
    # I_k = integral_T^infinity t^k e^-t dt by exact recurrence.
    moments = [(-t).exp()]
    for k in range(1, len(coeff)+1):
        moments.append(t**k*(-t).exp()+k*moments[-1])
    c = arb.const_euler()+8+PI.log()+(1+2*t).log()
    upper = sum((b*(c*moments[k]+(moments[k+1]-t*moments[k])/(t+arb(1)/2))
                 for k, b in enumerate(coeff)), arb(0))
    return ck*ck/PI*upper


def constants():
    # Cauchy disk of radius D for q and q''; this also controls theta truncation.
    a = PI*(-2*D).exp()*(2*D).cos()
    assert a > arb(9)/4
    c = (4*PI*PI/(1-16*(-3*a).exp())
         + 6*PI/(1-4*(-3*a).exp()))*(11*D).exp()
    ell = [arb(1), 1+2/(A*D*D)]
    m = arb(N+1)
    r4 = (1+1/m)**4*(-a*(2*m+1)).exp()
    r2 = (1+1/m)**2*(-a*(2*m+1)).exp()
    error = (arb(9)/2*D).exp()*(4*PI*PI*m**4*(-a*m*m).exp()/(1-r4)
                 + 6*PI*m*m*(-a*m*m).exp()/(1-r2))
    return a, c, ell, error


def correlation(n, i, j):
    x = arb(n).log()
    cells = []
    for lo, hi, sv, sq in [(-U, arb(0), -1, 1), (arb(0), x, 1, 1), (x, x+U, 1, -1)]:
        val = acb.integral(lambda v, analytic: q(v, sv, i)*q(x-v, sq, j),
                           lo, hi, abs_tol=TOL, rel_tol=TOL,
                           eval_limit=35000, depth_limit=24)
        assert val.is_finite(), (n, i, j, val)
        cells.append(val)
    a, c, ell, error = constants()
    wm = base.B+(x+U+D)/336
    sup = c*(-a).exp()*wm
    delta = (arb(13)/2*D).exp()*wm*error
    trunc = ell[i]*ell[j]*(x+2*U)*(2*sup*delta+delta*delta)
    denom = 2*a*(2*U).exp()-arb(9)/2-1/(168*wm)
    assert denom > 0
    exterior = (2*ell[i]*ell[j]*c*c*(-a).exp()
                *(arb(9)/2*U-a*(2*U).exp()).exp()*wm*wm/denom)
    central = sum(cells, acb(0))
    total_error = trunc+exterior
    return central+acb(arb(0,total_error.upper()),arb(0,total_error.upper())), {
        "n": n, "i": i, "j": j, "central": str(central),
        "truncation_error": str(trunc), "exterior_error": str(exterior)}


def prime_tail(i, j):
    a, c, ell, _ = constants()
    n = arb(M+1)
    b = base.B+D/336
    aa = b+n.log()/672
    # The Gaussian integral is sqrt(pi/(2*a*n)), not 1/sqrt(2*n).
    # See SUPPRESSION_BOUND_REVIEW.md, equations (13)--(17).
    coeff = c*c*(2*PI/a).sqrt()*ell[i]*ell[j]*(81/(8*a*n)).exp()*(1+1/(4*a*n*336**2*aa**2))
    first = n**(arb(7)/2)*n.log()*aa**2*(-2*a*n).exp()
    next_a = b+(n+1).log()/672
    ratio = (-2*a).exp()*(1+1/n)**(arb(7)/2)*(n+1).log()/n.log()*(next_a/aa)**2
    assert ratio < 1
    return 2*coeff*first/(1-ratio)


def smoke():
    # Exact polynomial coefficients; analytic-series regression for derivatives.
    from flint import acb_series
    u = acb(arb(37)/100)
    z = acb_series([u, 1], prec=3)
    e2 = (2*z).exp()
    value = sum(((4*PI*PI*n**4*(arb(9)/2*z).exp()
                 - 6*PI*n*n*(arb(5)/2*z).exp())*(-PI*n*n*e2).exp()
                 for n in range(1, N+1)), acb_series([0], prec=3))
    tests = []
    for k, fact in [(0,1),(1,1),(2,2)]:
        residual = theta_derivative(u,k)-fact*value[k]
        assert residual.contains(0), residual
        tests.append({"theta_derivative_order":k,"residual":str(residual)})
    for i in range(2):
        for j in range(i,2):
            assert prime_tail(i,j)>0 and gamma_tail(i+j)>0
    return tests


def run():
    start = time.time()
    tests = smoke()
    rows = {}
    grams = {}
    for i,j in [(0,0),(0,1),(1,1)]:
        order = i+j
        z = acb(0,arb(1)/2)
        pole = 2*(base.K(z)**2*filter_symbol(z)**order).real
        gcells = []
        for k in range(-T,T):
            val = acb.integral(lambda z, analytic: base.K(z)**2*filter_symbol(z)**order*base.gamma_weight(z),
                               k,k+1,abs_tol=TOL,rel_tol=TOL,eval_limit=20000,depth_limit=22)
            assert val.is_finite() and val.imag.contains(0), (i,j,k,val)
            gcells.append(val.real)
            if k % 16 == 0:
                print("GAMMA",i,j,k,flush=True)
        gcentral = sum(gcells, arb(0))
        gt = gamma_tail(order)
        prime = arb(0)
        prows = []
        for n,p,power in base.prime_powers(M):
            corr,row = correlation(n,i,j)
            term = 2*arb(p).log()/arb(n).sqrt()*corr.real
            prime += term
            row.update({"prime":p,"power":power,"weighted_term":str(term)})
            prows.append(row)
        pt = prime_tail(i,j)
        value = pole+gcentral-prime+arb(0,(gt+pt).upper())
        grams[i,j] = value
        rows[f"{i}{j}"] = {"pole":str(pole),"gamma_central":str(gcentral),"gamma_cells":[str(v) for v in gcells],
            "gamma_tail":str(gt),"prime_central":str(prime),"prime_rows":prows,"prime_tail":str(pt),"value":str(value)}
        print("GRAM",i,j,str(value),flush=True)
    determinant = grams[0,0]*grams[1,1]-grams[0,1]**2
    schur = grams[1,1]-grams[0,1]**2/grams[0,0]
    result = {"schema_version":1,"utc":datetime.now(timezone.utc).isoformat(),
        "status":"full_expression_ball_calculation_requires_written_bound_review",
        "input":"q0=w*g0; q1=q0+q0''/(19979/100)",
        "basis_coefficients_exact":{"A":"19979/100","fourier_filter":"1-100*s^2/19979"},
        "precision_bits":ctx.prec,"resource":base.RESOURCE,"workers":1,
        "RH_assumed":False,"zero_ordinates_used_in_evaluation":False,
        "source_directed_choice":"rational differential filter chosen to suppress the previously certified first real zero pair; source w unchanged",
        "parameters":{"theta_terms":N,"gamma_cutoff":T,"prime_cutoff":M,"margin":"3","cauchy_radius":"1/16","tolerance":"2^-100"},
        "derivative_regressions":tests,"gram":rows,"determinant":str(determinant),
        "schur":str(schur),"positive_definite":bool(grams[0,0]>0 and determinant>0),
        "negative_witness_found":bool(grams[0,0]<0 or grams[1,1]<0 or (grams[0,0]>0 and schur<0)),
        "seconds":time.time()-start,
        "source_hashes":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [Path(__file__),Path(base.__file__),ROOT/"certificates/rh_counterexample_20260908/resource_ceiling.py"]}}
    return result


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke",action="store_true")
    ap.add_argument("--write",action="store_true")
    args = ap.parse_args()
    result = {"smoke":smoke()} if args.smoke else run()
    print(json.dumps(result,indent=2) if args.smoke else json.dumps({k:result[k] for k in ["determinant","schur","positive_definite","negative_witness_found","seconds"]}))
    if args.write:
        Path(__file__).with_name("theta_zero_suppression_results.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
