"""Small independent regressions; interval/all-order proof is in the note.

No source corpus writes, index builds, subprocesses, or network calls.
Uses explicit checks (not assert), so python -O keeps every check active.
"""
from fractions import Fraction as F
from math import factorial, ceil
from pathlib import Path
import hashlib
import json
import sys
import mpmath as mp
import sympy as sp

mp.mp.dps = 90
ROWS = []


def check(name, condition, **data):
    if not condition:
        raise RuntimeError(f"FAILED {name}: {data}")
    ROWS.append({"name": name, "pass": True, **data})


def m(x):
    return mp.mpf(x.numerator)/x.denominator if isinstance(x, F) else mp.mpf(x)


def close(a, b, tol=mp.mpf("1e-70")):
    return abs(a-b) <= tol * max(mp.mpf(1), abs(a), abs(b))


def choose(b, n):
    out = F(1)
    for k in range(n):
        out *= (b-k)/F(k+1)
    return out


def rgamma_exact_head(arg):
    if arg.denominator == 1 and arg <= 0:
        return mp.mpf(0)
    return mp.rgamma(m(arg))


def sinpi_exact(arg):
    if arg.denominator == 1:
        return mp.mpf(0)
    return mp.sinpi(m(arg))


def finite_coefficient(h, j, even):
    D, A, j0 = F(1, 2)-h, F(1, 2)+h, F(1, 20)
    return ((j0*A if even else F(4)) * (-1)**j / F(j)
            * choose((2*j-1)*D if even else 2*j*D, j-1))


def run():
    hs = (F(1, 200), F(1, 202), F(3, 500), F(1, 1000))
    js = (1, 2, 3, 9, 25, 51, 99, 100, 101, 199, 200, 201, 300, 500, 1000)
    for h in hs:
        D, A, q, p, j0 = F(1,2)-h, F(1,2)+h, 2*h, 1-2*h, F(1,20)
        for j in js:
            for even in (True, False):
                exact = finite_coefficient(h, j, even)
                head = 2-q*j-D if even else 2-q*j
                numerator = p*j+A if even else p*j+1
                prefactor = j0*A if even else F(4)
                gamma = (-1)**j*m(prefactor)*mp.gamma(m(numerator))/mp.gamma(j+1)
                gamma *= rgamma_exact_head(head)
                check("finite_product_vs_reciprocal_gamma", close(m(exact), gamma),
                      h=str(h), j=j, parity="even" if even else "odd")
                zero_parameter = q*j+D if even else q*j
                is_zero = zero_parameter.denominator == 1 and zero_parameter >= 2
                check("exact_zero_classification", (exact == 0) == is_zero,
                      h=str(h), j=j, parity="even" if even else "odd")
                threshold_argument = q*j-A if even else q*j-1
                if threshold_argument > 0:
                    reflected = (-1)**(j+1)*m(prefactor)/mp.pi
                    reflected *= mp.gamma(m(numerator))*mp.gamma(m(threshold_argument))/mp.gamma(j+1)
                    reflected *= sinpi_exact(zero_parameter)
                    check("finite_product_vs_pole_free_reflection", close(m(exact), reflected),
                          h=str(h), j=j, parity="even" if even else "odd")

        B = m(p)**m(p)*m(q)**m(q)
        R = 1/mp.sqrt(B)
        check("radius_equal_original_parameters", close(R, m(p)**(-m(D))*m(q)**(-m(h))), h=str(h))
        check("radius_greater_than_one", R > 1, h=str(h))
        # Test the positive envelopes only: zero phases are never divided out.
        for even in (True, False):
            ce = (11-2*m(q)-7*m(q)**2)/(24*m(p)*m(q))
            co = (13-13*m(q)+m(q)**2)/(12*m(p)*m(q))
            c1 = ce if even else co
            b, c = (A, -A) if even else (F(1), F(-1))
            pref = m(j0*A if even else F(4))/mp.pi
            C = pref*mp.sqrt(2*mp.pi)*m(p)**(m(b)-F(1,2))*m(q)**(m(c)-F(1,2))
            errors = []
            for mult in (200, 400, 800):
                j = ceil(F(mult)/q)
                log_envelope = mp.log(pref)+mp.loggamma(m(p*j+b))+mp.loggamma(m(q*j+c))-mp.loggamma(j+1)
                ratio = mp.exp(log_envelope-mp.log(C)-j*mp.log(B)+mp.mpf("1.5")*mp.log(j))
                err = abs(ratio-1-c1/j)
                errors.append(err)
                check("positive_envelope_first_correction", err < mp.mpf("0.0001"),
                      h=str(h), parity="even" if even else "odd", j=j, error=mp.nstr(err,20))
            check("envelope_remainder_quadratic_decay", errors[1] < errors[0]/3 and errors[2] < errors[1]/3,
                  h=str(h), parity="even" if even else "odd")

        r = 1/mp.sqrt(m(q))
        for eps in (-1,1):
            for sig in (-1,1):
                uc = eps*r
                dc = -m(p)/m(q)
                logdc = mp.log(m(p)/m(q))+sig*mp.pi*1j
                def logd(u):
                    return logdc+mp.log((1-u*u)/dc)
                def fm(u):
                    return u*mp.exp(-m(D)*logd(u))
                def wm(u):
                    return mp.exp(m(A)*logd(u))*(4*u+m(j0))
                xc = eps*R*mp.exp(-sig*mp.pi*1j*m(D))
                check("critical_value_and_phase", close(fm(uc),xc), h=str(h), epsilon=eps, sigma=sig)
                check("critical_derivative_zero", abs(mp.diff(fm,uc)) < mp.mpf("1e-75"), h=str(h), epsilon=eps, sigma=sig)
                check("critical_second_derivative", close(mp.diff(fm,uc,2)/xc,2*m(q)**2/m(p)), h=str(h), epsilon=eps, sigma=sig)
                fp = mp.exp(-m(D)*logdc)*(-8/m(q)-2*m(A)*m(j0)*uc)
                check("source_trace_derivative_no_cancellation", close(mp.diff(wm,uc),fp) and abs(fp)>0,
                      h=str(h), epsilon=eps, sigma=sig)
                theta = mp.mpf("1e-12")
                u = uc*mp.exp(-sig*1j*theta)
                delta = 1-fm(u)/xc
                kappa = -1j*eps*sig*mp.sqrt(m(p))/m(q)
                check("accessible_puiseux_sign", close((u-uc)/mp.sqrt(delta),kappa,mp.mpf("1e-8")),
                      h=str(h), epsilon=eps, sigma=sig)
        for k in range(1,16):
            theta = mp.pi*k/16
            u = r*mp.exp(1j*theta)
            val = abs(u)/abs(1-u*u)**m(D)
            check("circle_access_path_strictly_inside_radius", val < R, h=str(h), sample=k)
        for k in range(17):
            v=r*k/16
            check("imaginary_access_path_inside_radius", v/(1+v*v)**m(D) < R, h=str(h), sample=k)

    # Deliberate resonance tests: trigonometric zero times gamma pole is NOT zero.
    odd_cancel=finite_coefficient(F(1,200),100,False)
    even_cancel=finite_coefficient(F(1,202),51,True)
    check("odd_gamma_pole_cancellation_nonzero", odd_cancel == F(1,25), exact=str(odd_cancel))
    check("even_gamma_pole_cancellation_nonzero", even_cancel != 0, exact=str(even_cancel))
    check("odd_later_sine_zero_is_genuine", finite_coefficient(F(1,200),200,False)==0)
    check("even_later_sine_zero_is_genuine", finite_coefficient(F(1,202),152,True)==0)

    # Symbolic differentiated identity, independent of numerical h samples.
    u,q,j0=sp.symbols("u q j0", real=True)
    D=(1-q)/2
    A=(1+q)/2
    d=1-u*u
    # Cancelling powers algebraically as local analytic expressions.
    fprime_factored=(1-q*u*u)
    fprime_from_product=sp.expand(d+2*D*u*u)
    check("symbolic_fprime_factor",sp.expand(fprime_factored-fprime_from_product)==0)
    Wprime_factored=4*d-2*A*u*(4*u+j0)
    critical_remainder=sp.rem(sp.expand(Wprime_factored-(-8/q-2*A*j0*u)),u*u-1/q,u)
    check("symbolic_Wprime_critical_factor",critical_remainder==0)
    check("symbolic_kappa_square",sp.simplify((-sp.I*sp.sqrt(1-q)/q)**2+(1-q)/q**2)==0)
    h,n,nu,tau=sp.symbols("h n nu tau",positive=True)
    n=sp.symbols("n",integer=True,nonnegative=True)
    check("physical_derivative_scaling",sp.simplify(sp.sqrt(nu)*tau**(-(sp.Rational(1,2)+h))
        /(sp.sqrt(nu)*tau**(sp.Rational(1,2)-h))**n
        -nu**((1-n)/2)*tau**(-(sp.Rational(1,2)+h)-n*(sp.Rational(1,2)-h)))==0)

    root=Path(__file__).resolve().parent
    source=root.parent/"ns_axis_lagrange_20260909"/"AXIAL_COEFFICIENTS.md"
    source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
    check("source_hash_unchanged",source_hash=="a17d1d4266dc965f2789a9e4080f0a8789c2537f62bace585b50eecbca087bad")
    result={"schema_version":1,"status":"pass","checks":len(ROWS),"assertions_disabled":not __debug__,
            "scope":"finite exact/symbolic and high-precision regressions; all-real-h theorem proved in note",
            "memory_policy_bytes":5000000000,"subprocesses":False,"mpmath_dps":mp.mp.dps,
            "source_sha256":source_hash,"records":ROWS}
    target=root/("CHECKS_OPTIMIZED.json" if not __debug__ else "CHECKS.json")
    target.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(f"AXIAL_SINGULARITIES_CHECK_OK checks={len(ROWS)} optimized={not __debug__}")


if __name__=="__main__":
    run()
