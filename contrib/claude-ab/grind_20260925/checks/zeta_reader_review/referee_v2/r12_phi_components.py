#!/usr/bin/env python3
"""Referee v2, script r12.  Prop 2.8 (zeros of Z_{1/q} on both sides of the line), left side beyond prime q.

Phi_{1/q}(s) = 2 sum_k cos(2 pi k/q) k^{-s} and Z_{1/q}(1-s) = 2 Gamma(s)(2 pi)^{-s} cos(pi s/2) Phi_{1/q}(s).
Grouping k by d = gcd(k, q), e = q/d:  Phi_{1/q}(s) = sum_{d|q} d^{-s} sum_{chi mod e} c_{d,chi} L(s, chi),
c_{d,chi} = phi(e)^{-1} sum_{x mod e, (x,e)=1} 2 cos(2 pi x/e) conj(chi(x)); writing each chi mod e through the
primitive psi inducing it gives Phi_{1/q} = sum_psi P_psi(s) L(s, psi) with Dirichlet polynomials P_psi, and this
representation is unique.  Saias-Weingartner's hypothesis ('not P(s) L(s, chi)') holds as soon as two components
are nonzero.
 1. The decomposition reproduces Phi_{1/q}(s) at a test point (numerical, via mpmath's dirichlet L-series).
 2. For every q in 3..40: the zeta component P_1 is nonzero, and some nontrivial primitive component is nonzero
    exactly when phi(q) > 2.  So the left-side conclusion of Prop 2.8 holds for every q with phi(q) > 2,
    not only for prime q >= 5.
 3. The reflection formula for composite q (8, 9, 10, 12) at test points.
"""
import cmath, math, itertools
from math import gcd
import mpmath as mp
from sympy import factorint, primitive_root, totient
mp.mp.dps = 30
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))

def characters(e):
    """All Dirichlet characters mod e as lists of values on 0..e-1 (0 off the units)."""
    if e == 1: return [[1]]
    comps = []
    for p, k in ((int(a), int(b)) for a, b in factorint(e).items()):
        pk = p**k
        units = [x for x in range(pk) if x % p]
        gens = []
        if p == 2 and k >= 3:
            gens = [(pk - 1, 2), (5, 2**(k - 2))]
        elif p == 2 and k == 2:
            gens = [(3, 2)]
        elif p == 2 and k == 1:
            gens = []
        else:
            gens = [(int(primitive_root(pk)), (p - 1) * p**(k - 1))]
        # discrete logs: exponents of each unit in the generators
        table = {}
        for exps in itertools.product(*[range(o) for _, o in gens]):
            x = 1
            for (g, _), a in zip(gens, exps): x = x * pow(g, a, pk) % pk
            table[x] = exps
        chars = []
        for js in itertools.product(*[range(o) for _, o in gens]):
            vals = {}
            for x in units:
                ph = sum(j * a / o for j, a, (_, o) in zip(js, table[x], gens))
                vals[x] = cmath.exp(2j * math.pi * ph)
            chars.append((pk, vals))
        comps.append(chars)
    out = []
    for combo in itertools.product(*comps):
        v = []
        for x in range(e):
            if gcd(x, e) != 1: v.append(0); continue
            val = 1
            for pk, vals in combo: val *= vals[x % pk]
            v.append(val)
        out.append(v)
    return out

def primitive_of(chi, e):
    """(f, values mod f) of the primitive character inducing chi mod e."""
    for f in sorted(d for d in range(1, e + 1) if e % d == 0):
        good = all(abs(chi[x] - 1) < 1e-9 for x in range(e) if gcd(x, e) == 1 and x % f == 1 % f)
        if good:
            vals = []
            for y in range(f):
                if gcd(y, f) != 1: vals.append(0); continue
                x = next(x for x in range(y, e * f + y + 1, f) if gcd(x, e) == 1)
                vals.append(chi[x % e])
            return f, tuple(vals)
    raise ValueError

def key(f, vals): return (f, tuple((round(v.real, 8), round(v.imag, 8)) if v != 0 else (0.0, 0.0) for v in vals))

def decompose(q):
    comps = {}     # key(psi) -> {'f':, 'vals':, 'P': {n: coeff}}
    for d in [d for d in range(1, q + 1) if q % d == 0]:
        e = q // d
        for chi in characters(e):
            c = sum(2 * math.cos(2 * math.pi * x / e) * chi[x].conjugate() for x in range(e) if gcd(x, e) == 1) / int(totient(e)) if e > 1 else 2.0
            if e == 1: c = 2.0   # k divisible by q: cos = 1, coefficient 2, L(s, chi_0 mod 1) = zeta
            if abs(c) < 1e-12: continue
            f, vals = primitive_of(chi, e)
            kk = key(f, vals)
            ent = comps.setdefault(kk, {'f': f, 'vals': vals, 'P': {}})
            poly = {d: c}                                  # d^{-s} * c * prod_{p | e} (1 - psi(p) p^{-s})
            for p in (int(x) for x in factorint(e)):
                psip = vals[p % f] if gcd(p, f) == 1 else 0
                new = dict(poly)
                for n, a in poly.items():
                    new[n * p] = new.get(n * p, 0) - a * psip
                poly = new
            for n, a in poly.items(): ent['P'][n] = ent['P'].get(n, 0) + a
    for ent in comps.values():
        ent['P'] = {n: a for n, a in ent['P'].items() if abs(a) > 1e-10}
    return comps

def Phi(q, s, N=None):
    return 2 * mp.fsum(mp.cos(2 * mp.pi * k / q) * mp.power(k, -s) for k in range(1, 40001))

def L(s, f, vals):
    if f == 1: return mp.zeta(s)
    return mp.dirichlet(s, [mp.mpc(v.real, v.imag) if v != 0 else 0 for v in vals])

s_test = mp.mpc(2, 3)
worst = 0
for q in (8, 9, 12, 15):
    comps = decompose(q)
    val = mp.fsum(mp.fsum(a * mp.power(n, -s_test) for n, a in ent['P'].items()) * L(s_test, ent['f'], ent['vals']) for ent in comps.values())
    ref = 2 * mp.fsum(mp.cos(2 * mp.pi * k / q) * mp.power(k, -s_test) for k in range(1, 200001))
    worst = max(worst, abs(val - ref) / abs(ref))
rep("1  primitive-component decomposition reproduces Phi_{1/q}(2+3i) for q = 8, 9, 12, 15", worst < 1e-8, f"max rel. diff {mp.nstr(worst, 3)} (truncation 2e5 terms)")

table = []
ok2 = True
for q in range(3, 41):
    comps = decompose(q)
    triv = [ent for ent in comps.values() if ent['f'] == 1]
    nontriv = [ent for ent in comps.values() if ent['f'] > 1 and ent['P']]
    has_triv = bool(triv and triv[0]['P'])
    ph = int(totient(q))
    cond = has_triv and ((len(nontriv) > 0) == (ph > 2))
    ok2 &= cond
    table.append((q, ph, has_triv, len(nontriv)))
rep("2  q = 3..40: zeta component nonzero; a nontrivial primitive component exists iff phi(q) > 2", ok2,
    "; ".join(f"q={q}: phi={ph}, zeta-comp={'y' if t else 'n'}, #nontrivial={n}" for q, ph, t, n in table if q in (3, 4, 6, 5, 7, 8, 9, 10, 12, 16, 18, 30)))

w3 = 0
for q in (8, 9, 10, 12):
    a = mp.mpf(1) / q
    for s in (mp.mpc('1.7', '4.2'), mp.mpc('2.5', '-11')):
        lhs = mp.zeta(1 - s, a) + mp.zeta(1 - s, 1 - a)
        rhs = 2 * mp.gamma(s) * (2 * mp.pi)**(-s) * mp.cos(mp.pi * s / 2) * 2 * mp.fsum(mp.cos(2 * mp.pi * k * a) * mp.power(k, -s) for k in range(1, 100001))
        w3 = max(w3, abs(lhs - rhs) / abs(lhs))
rep("3  Z_a(1-s) = 2 Gamma(s)(2 pi)^{-s} cos(pi s/2) Phi_a(s) for a = 1/q, q = 8, 9, 10, 12", w3 < 1e-5, f"max rel. diff {mp.nstr(w3, 3)} (series truncated at 1e5)")
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
