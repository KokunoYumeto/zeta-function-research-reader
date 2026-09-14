"""Exact rational fixtures of UG1--19; no actual zero or analytic certification."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

s, u, t = sp.symbols("s u t")


def zero(expression, label):
    if sp.cancel(expression) != 0:
        raise RuntimeError("nonzero exact residual: " + label)


def proper(expression):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    _, remainder = sp.div(numerator, denominator, s)
    return sp.cancel(remainder / denominator)


def hinverse(expression, h):
    expression = proper(expression)
    if expression == 0:
        return sp.S.Zero
    numerator, denominator = sp.fraction(expression)
    inverse = sp.invert(h, denominator, s)
    return proper(inverse*numerator/denominator)


def add(left, right):
    result = dict(left)
    for key, value in right.items():
        result[key] = sp.cancel(result.get(key, 0)+value)
    return {key:value for key,value in result.items() if value != 0}


def neg(series):
    return {key:-value for key,value in series.items()}


def map_coefficients(series, operation):
    return {key:operation(value) for key,value in series.items()}


def perturbation(series, order):
    result = {}
    for (a,b), value in series.items():
        if a+b < order:
            result = add(result, {(a+1,b):sp.diff(value,s), (a,b+1):-value})
    return result


def differential(series, h, order):
    return add(map_coefficients(series, lambda value: h*value), perturbation(series,order))


def inverse_pole(series, h, order, wrong_order=False):
    term = map_coefficients(series,lambda value:hinverse(value,h))
    result = term
    for _ in range(order):
        if wrong_order:
            term = perturbation(map_coefficients(term,lambda value:hinverse(value,h)),order)
            term = map_coefficients(term,proper)
        else:
            term = map_coefficients(perturbation(term,order),lambda value:hinverse(value,h))
        term = neg(term)
        result = add(result,term)
    return result


def series_zero(series,label,quotient=False):
    for key,value in series.items():
        zero(proper(value) if quotient else value, label+" coefficient "+str(key))


def check(h,nu,order=3):
    h,nu=sp.expand(h),sp.expand(nu)
    if sp.degree(sp.gcd(h,nu),s) != 0:
        raise RuntimeError("actual unit guard failed: h and nu are not coprime")
    P=s**3+u*s+t
    D=lambda value:u*sp.diff(value,s)+(h-t)*value
    Dg=lambda value:D(value)-u*sp.diff(nu,s)/nu*value
    L=lambda value:u*sp.diff(value,t)-s*value
    zero(Dg(nu*P)-nu*D(P),"UG12 gauge")
    zero(L(nu*P)-nu*L(P),"UG17 unit commutation")
    zero(Dg(L(P))-L(Dg(P)),"UG17 differential commutation")
    nu_inverse=sp.invert(nu,h,s)
    zero(sp.rem(nu*nu_inverse-1,h,s),"UG15 full inverse unit")
    if sp.degree(nu,s)==0:
        return {"h":str(h),"nu":str(nu),"pole_module":"zero","status":"PASS"}
    pole={(0,0):proper((s+2)/nu**2),(1,0):proper(3/nu),(0,1):proper(s/nu**3)}
    inverse=inverse_pole(pole,h,order)
    series_zero(add(differential(inverse,h,order),neg(pole)),"UG8 right inverse",True)
    derivative=map_coefficients(differential(pole,h,order),proper)
    series_zero(add(inverse_pole(derivative,h,order),neg(pole)),"UG8 left inverse",True)
    localized=add(pole,{(0,0):s**4+1,(1,0):s**2,(0,1):s})
    K=lambda value:inverse_pole(map_coefficients(value,proper),h,order)
    r0=lambda value:add(value,neg(map_coefficients(value,proper)))
    r1=lambda value:add(value,neg(differential(K(value),h,order)))
    series_zero(map_coefficients(r1(localized),proper),"UG10 image polynomial")
    series_zero(add(r1(differential(localized,h,order)),neg(differential(r0(localized),h,order))),"UG11 chain map")
    series_zero(add(K(differential(localized,h,order)),neg(map_coefficients(localized,proper))),"UG11 degree zero homotopy")
    series_zero(add(add(r1(localized),differential(K(localized),h,order)),neg(localized)),"UG11 degree one homotopy")
    polynomials={(0,0):s**3,(1,1):s**2+5}
    series_zero(K(polynomials),"UG11 K i zero")
    series_zero(add(r1(polynomials),neg(polynomials)),"UG11 r i identity")
    return {"h":str(h),"nu":str(nu),"total_formal_order":order,"status":"PASS"}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--mutant",choices=["wrong_gauge_sign","wrong_inverse_order","nonunit"])
    args=parser.parse_args()
    if args.mutant=="wrong_gauge_sign":
        h,nu=s**2+1,s+2
        D=lambda value:u*sp.diff(value,s)+(h-t)*value
        zero(D(nu*s)+u*sp.diff(nu,s)*s-nu*D(s),"wrong gauge sign")
    if args.mutant=="wrong_inverse_order":
        h=s**2+1
        pole={(0,0):1/(s-1)}
        inverse=inverse_pole(pole,h,1,wrong_order=True)
        series_zero(add(differential(inverse,h,1),neg(pole)),"wrong inverse order",True)
    if args.mutant=="nonunit":
        check(s,s)
    y=s-sp.Rational(1,2)
    fixtures=[check(s**2+1,s+2),check((s**2+1)**2,1+s+s**2),
              check(y**3,2+3*y+5*y**2),check(s-sp.Rational(3,4),sp.Integer(5))]
    receipt={"status":"PASS","scope":"4 exact rational fixtures, formal order3; not actual zeta-zero data",
             "fixtures":fixtures,"sympy":sp.__version__,
             "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    body=json.dumps(receipt,indent=2)+"\n"
    if args.output:
        Path(args.output).write_text(body,encoding="utf-8")
    print(body)


if __name__=="__main__":
    main()
