"""Exact finite regressions for the complete source-axis/Mellin proof.

This is not a certificate of the imported source existence theorem or RH.
All-order statements have standard proofs in the bound TeX. No asserts are
used: optimized Python executes every check. Noncritical cap: 5e9 bytes.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import sys
import psutil
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
N = 14
records = []
peak_rss = 0

def check(name, actual, expected):
    global peak_rss
    peak_rss = max(peak_rss, psutil.Process().memory_info().rss)
    if peak_rss > 5_000_000_000:
        raise MemoryError('noncritical memory cap exceeded')
    ok = actual == expected
    if not ok:
        raise RuntimeError(f'{name}: {actual!s} != {expected!s}')
    records.append({'check': name, 'status': 'pass'})

def poly(*a):
    return [Q(x) for x in a] + [Q(0)] * (N + 1 - len(a))

def add(a, b):
    return [x+y for x, y in zip(a, b)]

def scale(a, c):
    return [c*x for x in a]

def mul(a, b):
    c = poly()
    for i in range(N+1):
        for j in range(N+1-i):
            c[i+j] += a[i]*b[j]
    return c

def choose(a, j):
    c = Q(1)
    for k in range(j):
        c *= (a-k)/(k+1)
    return c

def power_one_minus(v, a):
    if v[0] != 0:
        raise ValueError('nonzero constant in series power')
    out, vj = poly(), poly(1)
    for j in range(N+1):
        out = add(out, scale(vj, (-1)**j*choose(a, j)))
        vj = mul(vj, v)
    return out

def inverse(a):
    if a[0] == 0:
        raise ValueError('zero denominator constant')
    out = poly(1/a[0])
    for n in range(1, N+1):
        out[n] = -sum(a[k]*out[n-k] for k in range(1, n+1))/a[0]
    return out

def compose(a, v):
    if v[0] != 0:
        raise ValueError('nonzero composition constant')
    out = poly()
    for c in reversed(a):
        out = mul(out, v)
        out[0] += c
    return out

for h in (Q(1, 113), Q(1, 257), Q(1, 1000)):
    A, D, k = Q(1,2)+h, Q(1,2)-h, 1+h
    j0, sigma_star, lam = Q(1,37), Q(1,7), Q(3)
    eta = poly()
    # Independent coefficient fixed-point iteration; not the closed formulas.
    for _ in range(N+1):
        eta = [Q(0)] + power_one_minus(mul(eta, eta), D)[:N]
    eta2 = mul(eta, eta)
    forward = mul(eta, power_one_minus(eta2, -D))
    axial = mul(power_one_minus(eta2, A), add(scale(eta, 4), poly(j0)))
    u, d, L = poly(0,1), poly(1,0,-1), poly(1,0,-2*h)
    H = add(scale(u,D), mul(d,poly(j0,4)))
    zet = scale(mul(mul(L,H), inverse(add(mul(H,H),poly(sigma_star**2)))), -1)
    phi = poly(1)
    for m in range(N):
        phi[m+1] = lam*sum(zet[l]*phi[m-l] for l in range(m+1))/(m+1)
    angular = compose(mul(power_one_minus(poly(0,0,1),k),phi), eta)
    bracket = add(scale(mul(d,zet),lam),scale(u,-2*k))
    for n in range(N+1):
        check(f'inverse:h={h}:n={n}', forward[n], int(n==1))
        if n == 0:
            ew, eg = j0, Q(1)
        else:
            if n == 1:
                ew = Q(4)
            elif n % 2 == 0:
                j = n//2
                ew = j0*(-1)**j*A/j*choose((2*j-1)*D,j-1)
            else:
                j = (n-1)//2
                ew = Q(4*(-1)**j,j)*choose(2*j*D,j-1)
            eg = mul(mul(phi,power_one_minus(poly(0,0,1),k-1+n*D)),bracket)[n-1]/n
        check(f'axial:h={h}:n={n}', axial[n], ew)
        check(f'angular:h={h}:n={n}', angular[n], eg)
        if n % 2 == 0 and n > 0:
            j = n//2
            highest = Q((-1)**j*factorial(n),2**j*factorial(j)**2)*axial[n]
            formula = j0*A*Q(factorial(n),2**j*factorial(j)**2*j)*choose((2*j-1)*D,j-1)
            check(f'highest:h={h}:j={j}', highest, formula)

z, x, sigma = s.symbols('z x sigma')
c = s.Function('c')(sigma)
B = s.Function('B')(sigma,z)
for a in (0,1):
    def L(f):
        return 2*sigma*s.diff(f,sigma,2)+2*(a+1)*s.diff(f,sigma)+s.diff(f,z,2)
    rhs = 4*sigma*s.diff(c,sigma)*s.diff(B,sigma)+(2*sigma*s.diff(c,sigma,2)+2*(a+1)*s.diff(c,sigma))*B
    check(f'localization-L{a}', s.expand(L(c*B)-c*L(B)-rhs), 0)
    for degree in range(9):
        f=z**degree
        H=sum((-1)**j*sigma**j*s.diff(f,z,2*j)/(2**j*factorial(j)*factorial(j+a)) for j in range(degree//2+1))
        check(f'kernel-PDE:a={a}:degree={degree}',s.expand(L(H)),0)
        check(f'kernel-axis:a={a}:degree={degree}',H.subs(sigma,0),f)
        # n-th Mellin coefficient of sigma H1 is shifted, including n=1.
        if a == 1:
            for n in range(1,degree//2+2):
                check(f'angular-shift:degree={degree}:n={n}',s.expand(sigma*H).coeff(sigma,n),s.expand(H).coeff(sigma,n-1))
LB=lambda f: 2*sigma*s.diff(f,sigma,2)+s.diff(f,z,2)
check('localization-LB', s.expand(LB(c*B)-c*LB(B)-4*sigma*s.diff(c,sigma)*s.diff(B,sigma)-2*sigma*s.diff(c,sigma,2)*B),0)

power_h, a0 = s.symbols('power_h a0')
psi0 = (1-power_h)*a0/2
c0 = (power_h-1)/4
check('EM-nonzero-axis',s.expand(-psi0/2-c0*a0),0)
check('zeta-zero-multiplier',s.expand(s.zeta(0)*(1-s.Rational(1,2))*(1-power_h)-c0),0)
w, an, wn, wnext, hol = s.symbols('w an wn wnext hol')
check('even-regular-value',s.expand((w*wn+w**2*wnext)*(an/w+hol)).subs(w,0),wn*an)
check('nonzero-residue',s.expand(w*(wn+w*wnext)*(an/w+hol)).subs(w,0),wn*an)
for n in range(15):
    for a in (0,1):
        monomial=sigma**(n+1)
        value=2*sigma*s.diff(monomial,sigma,2)+2*(a+1)*s.diff(monomial,sigma)
        check(f'nonzero-domain-diffusion:a={a}:n={n}',s.expand(value).coeff(sigma,n),2*(n+1)*(n+a+1))

paths=[ROOT/'tex/satellites/29q_ns_diagonal_generator.tex',ROOT/'tex/satellites/29r_ns_all_axis_mellin.tex',Path(__file__).resolve()]
bindings=[{'path':str(p.relative_to(ROOT)).replace('\\','/'),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]
result={'status':'pass','checks':len(records),'exact_rational_and_symbolic':True,'python_optimized':sys.flags.optimize,
        'max_degree':N,'sampled_peak_rss_bytes':peak_rss,'noncritical_memory_cap_bytes':5_000_000_000,
        'source_existence_imported':True,'lean_used':False,'rh_certificate':False,'bindings':bindings,'records':records}
suffix='_optimized' if sys.flags.optimize else ''
(HERE/('ns_axis_mellin_checks'+suffix+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'NS_AXIS_MELLIN_OK checks={len(records)} exact=true optimized={sys.flags.optimize} rss={peak_rss}')
