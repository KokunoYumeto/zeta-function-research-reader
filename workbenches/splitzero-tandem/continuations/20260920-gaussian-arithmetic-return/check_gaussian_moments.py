"""Exact identities and certified Legendre-series endpoint enclosures."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb
import hashlib
import json
import sys
import sympy as sp
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parent
ctx.prec = 240
checks = []
controls = []

def check(name, condition):
    if not bool(condition):
        raise RuntimeError(name)
    checks.append(name)

def negative(name, condition):
    if bool(condition):
        raise RuntimeError('Negative control unexpectedly passed: ' + name)
    controls.append(name)

def A(q):
    q = Q(q)
    return arb(str(q.numerator) + '/' + str(q.denominator))

def hull(lo, hi):
    return A((lo + hi) / 2) + arb(0, A((hi - lo) / 2))

def atan_bounds(q, terms):
    partial = sum(((-1)**n * q**(2*n+1) / (2*n+1)
                   for n in range(terms)), Q(0))
    following = partial + (-1)**terms*q**(2*terms+1)/(2*terms+1)
    return min(partial, following), max(partial, following)

p5 = atan_bounds(Q(1, 5), 24)
p239 = atan_bounds(Q(1, 239), 8)
pi_lo = 16*p5[0] - 4*p239[1]
pi_hi = 16*p5[1] - 4*p239[0]
PI = hull(pi_lo, pi_hi)
check('Machin tangent identity', (Q(120,119)-Q(1,239))/(1+Q(120,119)*Q(1,239)) == 1)
check('Machin interval contains independent Arb pi', PI.contains(arb.pi()))
check('Machin pi lower bound', PI > A(Q(3141592653589793, 10**15)))
check('Machin pi upper bound', PI < A(Q(3141592653589794, 10**15)))

def elliptic_series(r, J=2048):
    z = 1-r*r
    a = arb(1)
    term = arb(1)
    sk = arb(1)
    se = arb(1)
    for n in range(1, J+1):
        a *= (arb(2*n-1)/arb(2*n))**2
        term = a * z**n
        sk += term
        se -= term/(2*n-1)
    tail = z**(J+1)/(1-z)
    # Positive tails occupy [0, upper]. Including a symmetric radius is
    # conservative; no endpoint of an approximate interval is rounded in.
    rk = arb(0, tail.abs_upper())
    re = arb(0, (tail/(2*J+1)).abs_upper())
    return sk + rk, se + re, tail

rlo = Q(16010167095, 10**11)
rhi = Q(16010167096, 10**11)
sklo, selo, tail_lo = elliptic_series(A(rlo))
skhi, sehi, tail_hi = elliptic_series(A(rhi))
flow = A(rlo)*sklo/selo-A(Q(1,2))
fhigh = A(rhi)*skhi/sehi-A(Q(1,2))
check('Endpoint equation below at rational left endpoint', flow < 0)
check('Endpoint equation above at rational right endpoint', fhigh > 0)
check('Legendre tail below 1e-20 at left endpoint', tail_lo < A(Q(1,10**20)))
check('Legendre tail below 1e-20 at right endpoint', tail_hi < A(Q(1,10**20)))
RB = hull(rlo,rhi)
sk,se,tail = elliptic_series(RB)
K, E = PI*sk/2, PI*se/2
u,v = 2/K,4/E
moment = (16-u*u-v*v+u*v)/3
check('Certified moment exceeds 10249/10000', moment > A(Q(10249,10000)))
check('Certified moment below 102497/100000', moment < A(Q(102497,100000)))
check('Certified moment exceeds one', moment > 1)
check('Elliptic K overlap with independent Arb evaluation', K.overlaps(acb(1-RB*RB).elliptic_k().real))
check('Elliptic E overlap with independent Arb evaluation', E.overlaps(acb(1-RB*RB).elliptic_e().real))

# Algebraic identities are independent of the endpoint enclosure.
x,p,s,U,V,T = sp.symbols('x p s U V T', positive=True)
total_derivative = 1-(2+2*p)*x+3*p*x*x
reduce_numerator = 3*(1-p*x)**2-2*(2-p)*(1-p*x)+(1-p)
check('Elliptic J3 identity is an exact endpoint derivative',
      sp.expand(reduce_numerator-p*total_derivative)==0)
J3 = (2*(1+(U/V)**2)*(2*(1+s)/V) - (U/V)**2*(2/U))/3
first = sp.expand(V**3*J3/(2*s) - (1/s+1)*(U*U+V*V)/2)
target = ((1+s)*(U*U+V*V)-2*U*V)/(6*s)
check('Original relation first moment substitution', sp.factor(first-target)==0)
m = sp.Rational(2,3)*T**3-(T*(U*U+V*V)-2*U*V)/6
check('Uniform positive bound identity',
      sp.expand(6*m-U*V-(T*(4*T*T-V*V)+U*(V-T*U)))==0)
for j in range(13):
    arcsine_moment = sp.integrate(sp.cos(x)**(2*j),(x,0,sp.pi))/sp.pi
    check(f'Original ordinary moment {2*j}',
          sp.simplify(4**j*arcsine_moment/(2*j+1)-sp.Rational(comb(2*j,j),2*j+1))==0)

check('sqrt2 rational upper bound', Q(99,70)**2 > 2)
check('exp(9/10) finite lower bound',
      sum((Q(9,10)**j/factorial(j) for j in range(6)),Q(0)) > 1+Q(99,70))
check('exp(7/10) finite lower bound',
      sum((Q(7,10)**j/factorial(j) for j in range(6)),Q(0)) > 2)
check('K elementary bound is below four', Q(39,10) < 4)
check('Low-r case exact comparison', Q(57,4)*Q(313,320)**2 < Q(349,25))
check('Original heat threshold arithmetic', Q(4,3)-Q(63,32)*Q(17,25) == -Q(13,2400))
strong = Q(4,3)-Q(63,32)*Q(10249,10000)
check('Strengthened heat threshold arithmetic', strong == -Q(657061,960000))
check('Certificate heat bound is stronger', strong < -Q(13,2400))
negative('Delete the relation subtraction in second moment',
         sp.expand(first-target+2*U*V/(6*s))==0)
negative('Replace both-sign pushforward mass by half', Q(2)-Q(1,2)==1)
negative('Claim the endpoint moment is below one', moment < 1)
negative('Reverse the four-cutoff sign', strong > 0)

receipt = {
    'result':'PASS', 'checks':len(checks), 'negative_controls':len(controls),
    'arithmetic':'python-flint Arb, 240-bit midpoint precision; all tails explicit',
    'series_terms':2048,
    'scope':'Exact equilibrium identities and finite candidate-density constants; no native spectral-limit claim.',
    'bounds':{'r_left':str(rlo),'r_right':str(rhi),'f_left':str(flow),'f_right':str(fhigh),
              'K':str(K),'E':str(E),'u':str(u),'v':str(v),'moment':str(moment),
              'tail_left':str(tail_lo),'tail_right':str(tail_hi),'pi':str(PI),
              'strong_heat_upper':str(strong)},
    'check_names':checks,'negative_control_names':controls,
    'python_optimized':bool(sys.flags.optimize),
    'proof_sha256':hashlib.sha256((ROOT/'GAUSSIAN_EQUILIBRIUM_MOMENTS.tex').read_bytes()).hexdigest(),
}
(ROOT/'GAUSSIAN_MOMENT_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
