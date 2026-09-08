"""Full arithmetic Weil matrices for modulated, translated cubic B-splines.

One worker, bounded sizes; no zero ordinates are used as computation inputs.
g_j(u)=exp(-i*T*(u-j*h))*b4(u-j*h). Exact h is rational.
Every correlation polynomial and integration endpoint is retained.
Outputs are Arb enclosure certificates, not proof-assistant verification.
"""
from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

import flint
from flint import acb, arb, ctx
import verify_weil_bspline as base

ctx.prec = 384
ctx.threads = 1
TOL = 240


def ball(q):
    q = F(q)
    return arb(q.numerator) / q.denominator


def shifted_coeff(shift, midpoint):
    """Ascending polynomial coefficients of b8(x+shift) on a knot cell."""
    return [sum((F((-1)**k*math.comb(8,k)*math.comb(7,r), math.factorial(7))
                 *(4+shift-k)**(7-r)
                 for k in range(9) if midpoint+shift+4-k > 0), F(0))
            for r in range(8)]

def odd_shifted_coeff(shift, midpoint):
    """h(x+shift), h=-(u*b4)*(u*b4), exact degree-nine pieces."""
    out = [F(0) for _ in range(10)]
    for k in range(5):
        for l in range(5):
            a,b = 2-k,2-l
            offset = F(a+b)+shift
            if midpoint+offset <= 0:
                continue
            c = -F((-1)**(k+l)*math.comb(4,k)*math.comb(4,l),36)
            for power,factor in (
                (9,F(math.factorial(4)**2,math.factorial(9))),
                (8,-F((a+b)*math.factorial(4)*math.factorial(3),math.factorial(8))),
                (7,F(a*b*math.factorial(3)**2,math.factorial(7)))):
                for r in range(power+1):
                    out[r] += c*factor*math.comb(power,r)*offset**(power-r)
    return out


def moment(w, kind):
    if kind == "b4":
        return base.sinhc(w/2)**8
    z = w/2
    if kind == "cross":
        return 2*base.sinhc(z)**7*(z*z.cosh()-z.sinh())/z**2
    kp = 2*base.sinhc(z)**3*(z*z.cosh()-z.sinh())/z**2
    return -kp**2


def correlation_cells(d, kind="b4"):
    endpoint = 4+d
    knots = sorted({F(0), endpoint} |
                   {F(k-4)+s*d for k in range(9) for s in (-1,1)
                    if 0 < F(k-4)+s*d < endpoint})
    if kind == "cross":
        def coeff(s,m):
            p = shifted_coeff(s,m)
            result = [(s*p[r] if r<len(p) else F(0))/2
                      +(p[r-1]/2 if r>0 else F(0)) for r in range(9)]
            assert all(isinstance(v,F) for v in result)
            return result
        return [(l,r,coeff(-d,(l+r)/2),[-v for v in coeff(d,(l+r)/2)])
                for l,r in zip(knots,knots[1:])]
    coeff = shifted_coeff if kind == "b4" else odd_shifted_coeff
    return [(l,r,coeff(-d,(l+r)/2),coeff(d,(l+r)/2))
            for l,r in zip(knots,knots[1:])]


def full_entry(d, T, kind="b4"):
    """G_ij for d=(j-i)h >=0; the reverse entry is its conjugate."""
    d = F(d)
    t = arb(T)
    db = ball(d)
    endpoint = 4+d
    phase = (acb(0,t)*db).exp()
    am = acb(arb(1)/2,-t)
    ap = acb(arb(1)/2,t)
    cells = correlation_cells(d,kind)
    assert cells[0][2][0] == cells[0][3][0]
    b0 = ball(cells[0][2][0])
    c0 = phase*b0
    integral = acb(0)
    segment_balls = []
    for l,r,pm,pp in cells:
        assert all(isinstance(v,F) for v in pm+pp)
        cm,cp = ([ball(v) for v in row] for row in (pm,pp))
        def integrand(x, analytic, l=l,cm=cm,cp=cp):
            if l == 0:
                # (P(x)*exp(a*x)-P(0))/x as an analytic function.
                vm = (base.polynomial(x,cm[1:])*(am*x).exp()
                      +b0*am*(am*x/2).exp()*base.sinhc(am*x/2))
                vp = (base.polynomial(x,cp[1:])*(ap*x).exp()
                      +b0*ap*(ap*x/2).exp()*base.sinhc(ap*x/2))
                return phase*(vm+vp)/(2*base.sinhc(x))
            return (phase*(base.polynomial(x,cm)*(am*x).exp()
                           +base.polynomial(x,cp)*(ap*x).exp())/2-c0)/x.sinh()
        value = acb.integral(integrand,ball(l),ball(r),
                             abs_tol=arb(2)**(-TOL),rel_tol=arb(2)**(-TOL),
                             eval_limit=200000,depth_limit=35)
        assert value.is_finite(), (d,T,l,r)
        integral += value
        segment_balls.append(str(value))
    ppowers = base.prime_powers(float(endpoint))
    prime = acb(0)
    for n,p,k in ppowers:
        x = arb(n).log()
        for l,r,pm,pp in cells:
            if x > ball(l) and x < ball(r):
                vm = base.polynomial(x,[ball(v) for v in pm])
                vp = base.polynomial(x,[ball(v) for v in pp])
                cx = phase*((-acb(0,t)*x).exp()*vm
                            +(acb(0,t)*x).exp()*vp)/2
                break
        else:
            raise ArithmeticError("No certified prime-power cell")
        prime += 2*arb(p).log()/arb(n).sqrt()*cx
    pole = ((db/2).exp()*moment(am,kind)
            +(-1 if kind=="cross" else 1)*(-db/2).exp()*moment(ap,kind))
    constant = -(arb.const_euler()+(4*arb.pi()).log())*c0
    tail = c0*(1/(ball(endpoint)/2).tanh()).log()
    answer = pole+constant-integral+tail-prime
    if d == 0 and kind != "cross":
        assert answer.imag.contains(0)
        answer = acb(answer.real)
    if T == 0:
        assert answer.imag.contains(0)
        answer = acb(answer.real)
    return answer, {
        "d":str(d),"T":T,"kind":kind,"value":str(answer),
        "real":str(answer.real),"imag":str(answer.imag),
        "pole":str(pole),"constant":str(constant),"tail":str(tail),
        "integral_segments":segment_balls,"prime_sum":str(prime),
        "prime_power_count":len(ppowers),
        "endpoint":str(endpoint),
    }


def ldl(matrix):
    n = len(matrix)
    lower = [[acb(int(i==j)) for j in range(n)] for i in range(n)]
    pivots = []
    for j in range(n):
        value = matrix[j][j]-sum(lower[j][k]*lower[j][k].conjugate()*pivots[k]
                                 for k in range(j))
        assert value.imag.contains(0)
        dj = value.real
        pivots.append(dj)
        if not dj > 0:
            return False,pivots
        for i in range(j+1,n):
            lower[i][j] = (matrix[i][j]-sum(
                lower[i][k]*lower[j][k].conjugate()*pivots[k] for k in range(j)))/dj
    return True,pivots


def run_case(n,h,T,kind="b4"):
    started = time.time()
    entries,records = [],[]
    for k in range(n):
        value,record = full_entry(k*h,T,kind)
        entries.append(value)
        records.append(record)
        if k % 8 == 0:
            print("ENTRY",n,str(h),T,k,flush=True)
    matrix = [[entries[j-i] if j>=i else entries[i-j].conjugate()
               for j in range(n)] for i in range(n)]
    positive,pivots = ldl(matrix)
    # Each column has coefficients of (z-exp(h/2))*(z-exp(-h/2)).
    # For T!=0, polynomial roots are exp(+-h/2), since translating g0
    # still multiplies its transform by exp(-ijhz).
    c = [arb(1),-2*(ball(h)/2).cosh(),arb(1)]
    filtered = [[sum(c[a]*c[b]*matrix[i+a][j+b]
                     for a in range(3) for b in range(3))
                 for j in range(n-2)] for i in range(n-2)]
    filter_positive,filter_pivots = ldl(filtered)
    # Independently check direct scalar code at d=0 (different routine).
    if kind == "b4":
        reference = arb(base.q_arb(T)["value_ball"])
        assert entries[0].real.overlaps(reference)
    print("MATRIX",n,"T",T,"positive",positive,"pivots",len(pivots),
          "filter_positive",filter_positive,"last",str(pivots[-1]),flush=True)
    return {
        "n":n,"h":str(h),"T":T,"kind":kind,"entries":records,
        "basis":"g_j(u)=exp(-i*T*(u-j*h))*b(u-j*h), j=0,...,n-1; b=b4 or u*b4 as specified",
        "support_union":[-2,str(2+(n-1)*h)],
        "max_correlation_support":str(4+(n-1)*h),
        "hermitian_toeplitz_positive_certified":positive,
        "LDL_pivots":[str(p) for p in pivots],
        "pole_annihilator":["1","-2*cosh(h/2)","1"],
        "filtered_dimension":n-2,
        "filtered_positive_certified":filter_positive,
        "filtered_LDL_pivots":[str(p) for p in filter_pivots],
        "independent_scalar_overlap":True if kind == "b4" else None,
        "elapsed_seconds":time.time()-started,
        "no_negative_witness_in_this_space":positive,
    }

def mixed_case(even,odd):
    n,T = even["n"],even["T"]
    h=F(even["h"])
    decode=lambda r: acb(arb(r["real"]),arb(r["imag"]))
    e=[decode(r) for r in even["entries"]]
    o=[decode(r) for r in odd["entries"]]
    cross,records=[],[]
    for k in range(n):
        v,r=full_entry(k*h,T,"cross")
        cross.append(v)
        records.append(r)
    A=[[e[j-i] if j>=i else e[i-j].conjugate() for j in range(n)] for i in range(n)]
    D=[[o[j-i] if j>=i else o[i-j].conjugate() for j in range(n)] for i in range(n)]
    R=[[cross[j-i] if j>=i else -cross[i-j].conjugate() for j in range(n)] for i in range(n)]
    G=[A[i]+R[i] for i in range(n)]+[
        [R[j][i].conjugate() for j in range(n)]+D[i] for i in range(n)]
    positive,pivots=ldl(G)
    print("MIXED_MATRIX",2*n,T,positive,len(pivots),str(pivots[-1]),flush=True)
    return {"dimension":2*n,"T":T,"h":str(h),"cross_entries":records,
            "positive_certified":positive,"LDL_pivots":[str(p) for p in pivots],
            "block_convention":"G=[[A,R],[R*,D]], R_ij=K((j-i)h), K(-d)=-conjugate(K(d))",
            "correlation_cross":"h01(x)=x*b8(x)/2; h10=-h01; modulate and translate retaining parity"}


def main():
    start = time.time()
    cases = [run_case(33,F(1,8),T,kind) for kind in ("b4","u_b4") for T in (0,14,40,100)]
    mixed=[mixed_case(cases[i],cases[i+4]) for i in range(4)]
    source = Path(__file__)
    data = {
        "id":"RH-WEIL-TRANSLATIONS-20260908-002",
        "status":"finite_search_not_RH_resolution",
        "precision_bits":ctx.prec,"integration_tolerance_bits":TOL,"threads":1,
        "resource_class":"noncritical; bounded 33x33 matrices and at most 8 units log support; <5GB by construction",
        "prime_enumeration":"all prime powers with log n < endpoint; strict Arb comparisons",
        "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
        "dependency_sha256":hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest(),
        "software":{"python_flint":flint.__version__},
        "zero_ordinates_used":False,
        "formula":"full complex evenized correlation explicit formula; pole, gamma, prime powers, exact tail",
        "cases":cases,"mixed_cases":mixed,"elapsed_seconds":time.time()-start,
        "nonclaims":["No RH proof or counterexample","No claim about mixed-frequency spaces or infinite-dimensional positivity"],
    }
    source.with_name("weil_translations_results.json").write_text(
        json.dumps(data,indent=2)+"\n",encoding="utf-8")
    print("SEARCH_COMPLETE",data["elapsed_seconds"],flush=True)


if __name__ == "__main__":
    main()
