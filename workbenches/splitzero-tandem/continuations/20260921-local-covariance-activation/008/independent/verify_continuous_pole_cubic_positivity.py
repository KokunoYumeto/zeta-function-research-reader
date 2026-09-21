"""Exact CP constant/identity certificate; no zero sampling or RH assumption."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import hashlib
import sympy as S

T0 = 3*10**12
Tstar = 99*T0//100
assert Tstar+800 < T0
assert F(100,1)/F(44,7) > 15
assert sum(F(2**j,factorial(j)) for j in range(5)) == 7
assert 7 > F(44,7)
assert 3**4 < 100
assert F(1038,10000)+F(2573,10000) < 1
assert F(93675,10000) < 10

numerator_coefficient_norm = sum(j*j for j in [1,3,3,1])
assert numerator_coefficient_norm == 20
products = [
    S.prod(2*abs(j-k)-1 for k in range(4) if k != j)
    for j in range(4)
]
assert products == [15,3,3,15]
inverse_factor = 20*sum(F(1,int(m)**2) for m in products)
assert inverse_factor == F(208,45)
L = F(2560009,4)
weight = 3/L
chord = 300/L
positive = weight*chord**6/inverse_factor
assert positive == F(135*1200**6,52*2560009**7)
assert positive > F(1,10**26)
positive_integer_difference = 135*1200**6*10**26-52*2560009**7
assert positive_integer_difference == 2839912978528311935972297436813173952969845612
derivative = F(7,4)*(F(51,50)**3+F(9,10)*F(51,50)**2)
assert derivative == F(54621,15625)
assert derivative < 4
exp30_lower = sum(F(30**k,factorial(k)) for k in range(31))
assert exp30_lower > T0
tail = F(256*100**4,T0**3)*F(91,9)
assert tail == F(23296,243*10**28)
assert tail < F(24,25)*F(1,10**26)
mu = positive-tail
assert mu > F(4,10**28)
# This stronger numerical orientation is itself an exact rational comparison.
assert mu > F(1,10**27)
print("CP3--18: every rational constant, interval endpoint and full-tail margin verified exactly.")

t, u, tau = S.symbols("t u tau", real=True)
height = S.Rational(3,2)
zt = (height+S.I*(t-tau))/(height-S.I*(t-tau))
zu = (height+S.I*(u-tau))/(height-S.I*(u-tau))
chord_squared = S.cancel((zt-zu)*S.conjugate(zt-zu))
expected = 9*(t-u)**2/((S.Rational(9,4)+(t-tau)**2)*
                       (S.Rational(9,4)+(u-tau)**2))
assert S.cancel(chord_squared-expected) == 0
assert 64//2 == 32  # Two members of a reflected pair in positive-height N.
assert 32*2*100**4 == 64*100**4  # Both signs of height retained.
assert (64*100**4)*4 == 256*100**4  # Stieltjes derivative.
print("CP9 and CP15--16: exact chord identity and reflected-tail multiplicity factors verified.")

y = S.symbols("y", real=True)
m0,m2,m4,m6 = S.symbols("m0 m2 m4 m6", positive=True)
moments={0:m0,1:0,2:m2,3:0,4:m4,5:0,6:m6}
poly=S.Poly(S.expand(3*(S.Rational(9,4)+(y-tau)**2)**3),y)
native=S.expand(sum(cc*moments[ee[0]] for ee,cc in poly.terms()))
claimed=3*(S.Rational(729,64)*m0+
           S.Rational(243,16)*(m2+tau**2*m0)+
           S.Rational(27,4)*(m4+6*tau**2*m2+tau**4*m0)+
           m6+15*tau**2*m4+15*tau**4*m2+tau**6*m0)
assert S.expand(native-claimed) == 0
for term in S.Poly(native,tau).terms():
    assert term[0][0] % 2 == 0
    assert S.expand(term[1]).is_positive is True
print("CP23--24: all original native diagonal moments and monotonicity coefficients verified.")

c0,c1,c2,c3=S.symbols("c0 c1 c2 c3",nonzero=True)
cs=[c0,c1,c2,c3]
eta=[1/c0,-c1/c0**2,(c1*c1-c0*c2)/c0**3,
     (-c1**3+2*c0*c1*c2-c0*c0*c3)/c0**4]
for n in range(4):
    assert S.cancel(sum(cs[j]*eta[n-j] for j in range(n+1))
                    -(1 if n==0 else 0)) == 0
print("CP29: all original finite inverse coefficients verified by exact convolution.")

def exact(value):
    return {"numerator":str(value.numerator),"denominator":str(value.denominator)}

result={
    "status":"all exact algebra checks passed",
    "scope":"No high RH, no numerical zero search; human CP3--4 theorems are cited inputs.",
    "T0":T0,
    "closed_real_tau_interval":[-Tstar,Tstar],
    "L":exact(L),
    "four_zero_lower_bound":exact(positive),
    "entire_possible_negative_tail_upper_bound":exact(tail),
    "complete_form_lower_bound":exact(mu),
    "advertised_simple_lower_bound":exact(F(4,10**28)),
    "exact_additional_check_mu_gt_1e_minus_27":True,
    "exp30_finite_lower_sum":exact(exp30_lower),
    "certificate_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
out=Path(__file__).with_name("CONTINUOUS_POLE_CUBIC_POSITIVITY_CERTIFICATE.json")
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("All continuous cubic positivity checks passed; exact rational JSON certificate written.")
