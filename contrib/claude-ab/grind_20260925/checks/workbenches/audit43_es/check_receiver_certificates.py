#!/usr/bin/env python3
"""Independent recomputation of the polynomial certificates behind README items 22-23
(es-turn07-global-receiver-determinant-20260921/core.tex, es-turn07-sharp-receiver-growth-20260921/core.tex)
and an exact census of the global sign on actual witnesses. My own code (sympy + exact integers;
mpmath only for singular values of the complex receiver)."""
import sys, time
from fractions import Fraction
from math import gcd
import sympy as sp
from sympy import primerange, divisors
import mpmath

T0 = time.time()
def log(*a):
    print(*a); sys.stdout.flush()

A, B, C, D, T, S = sp.symbols('A B C D T S')
e1, e2, e3, e4 = sp.symbols('e1 e2 e3 e4')
F = (20 * (3 * C - B**2) + A * (87 * B**3 - 282 * B * C - 51 * D)
     + A**2 * (-28 * B**4 + 22 * B**2 * C + 431 * C**2 + 204 * B * D)
     + A**3 * (224 * B**2 * D - 168 * B * C**2 - 856 * C * D) - 448 * A**4 * D**2)
def Nfun(E2, E3, E4, SS):
    return (60*E3*SS**5 - 20*E2**2*SS**4 + 87*E2**3*SS**2 - 282*E2*E3*SS**3 - 51*E4*SS**4
            - 28*E2**4 + 22*E2**2*E3*SS + 431*E3**2*SS**2 + 204*E2*E4*SS**2
            + 224*E2**2*E4 - 168*E2*E3**2 - 856*E3*E4*SS - 448*E4**2)
Nsym = Nfun(e2, e3, e4, S)
sub = {A: -1 / S, B: -e2 / S, C: e3 / S, D: -e4 / S}
log("[22] S^6 F(A=-1/S,B=-e2/S,C=e3/S,D=-e4/S) == N :", sp.simplify(sp.expand(S**6 * F.subs(sub)) - Nsym) == 0)

H = A * T**4 + T**3 + B * T**2 + C * T + D
Hp = sp.diff(H, T)
polys = [sp.Integer(1), Hp, A * Hp**2 + 2 * T * Hp, 7 * T**2 * Hp - 13 * Hp**2]
MH_src = sp.Matrix([
    [1, 0, 0, 0],
    [C, 2*B, 3, 4*A],
    [A*C**2 - 9*D, 4*A*B*C - 8*A*D - 7*C, 4*A*B**2 - 16*A**2*D - 2*A*C - 5*B, 4*A*B - 8*A**2*C - 3],
    [20*D/A - 13*C**2, 20*C/A + 76*D - 52*B*C, 20*B/A + 5*C - 52*B**2 + 208*A*D, 20/A - 66*B + 104*A*C]])
rows = []
for P in polys:
    r = sp.rem(sp.expand(P), H, T)          # remainder mod H in T (field of fractions)
    r = sp.Poly(sp.expand(r), T)
    rows.append([sp.simplify(r.coeff_monomial(T**k)) for k in range(4)])
MH = sp.Matrix(rows)
log("[22] reduction matrix of (1, H', AH'^2+2TH', 7T^2H'-13H'^2) mod H equals the source M_H:", sp.simplify(MH - MH_src) == sp.zeros(4, 4))
log("[22] det M_H == 4F/A:", sp.simplify(MH_src.det() - 4 * F / A) == 0)

# ---- exterior certificate
u, w, X, Y = sp.symbols('u w X Y', positive=True)
def N_of_roots(r):
    s = sum(r)
    E2 = sum(r[i] * r[j] for i in range(4) for j in range(i + 1, 4))
    E3 = sum(r[i] * r[j] * r[k] for i in range(4) for j in range(i + 1, 4) for k in range(j + 1, 4))
    E4 = r[0] * r[1] * r[2] * r[3]
    return sp.expand(Nfun(E2, E3, E4, s))
rootsE = [16*w*u, 4*u*(w + 1), (w + 1)*(4*w*u + w + 1), 4*w*u*(w + 1 + 4*w*u)]
NE = N_of_roots(rootsE)
q, r_ = sp.div(sp.Poly(-NE, u, w), sp.Poly(64 * u**2, u, w))
log("[22] -N(E roots) divisible by 64u^2 in Z[u,w]:", r_.is_zero)
PE = sp.expand(q.as_expr())
PEp = sp.Poly(PE, u, w)
log("[22] bidegree of P_E:", PEp.degree(u), PEp.degree(w), "(src (12,16))")
def translated_coeffs(expr):
    P = sp.Poly(sp.expand(expr.subs({u: 1 + X, w: 1 + Y}, simultaneous=True)), X, Y)
    return P.terms()
for name, ex in [("P_E", PE), ("u dP_E/du - 6P_E", sp.expand(u * sp.diff(PE, u) - 6 * PE)),
                 ("w dP_E/dw - 8P_E", sp.expand(w * sp.diff(PE, w) - 8 * PE))]:
    tc = translated_coeffs(ex)
    log(f"[22] {name} at (1+X,1+Y): {len(tc)} coefficients, all positive integers: {all(c > 0 and c.is_integer for _, c in tc)}, min {min(c for _, c in tc)} (src 221 positive)")
Phi = sp.simplify(PE.subs(w, 1) / (2**26 * u**6))
V = 5120*u**10 + 14592*u**9 + 7232*u**8 - 6400*u**7 + 1728*u**6 + 3904*u**5 + 432*u**4 - 400*u**3 + 113*u**2 + 57*u + 5
log("[22] Phi(u) == (2u-1)^2 V(u)/(4096u^6):", sp.simplify(Phi - (2*u - 1)**2 * V / (4096 * u**6)) == 0)
c12 = sp.Rational(125873811, 262144); c24 = sp.Rational(327448292668, 47045881)
log("[22] Phi(2) == c12:", Phi.subs(u, 2) == c12, "; Phi(5) =", Phi.subs(u, 5), "> c24 =", c24, ":", Phi.subs(u, 5) > c24)

# ---- middle certificate
b = 2 + X; c = 3 + X + Y
L = sp.expand(4 * b * c - b - c)
LM = 4*X**2 + 4*X*Y + 18*X + 7*Y + 19
log("[22] L(2+X,3+X+Y) == L_M:", sp.expand(L - LM) == 0)
NM = N_of_roots([L, sp.expand(b * c), sp.expand(b * L), sp.expand(c * L)])
qm, rm = sp.div(sp.Poly(-NM, X, Y), sp.Poly(sp.expand(L**2), X, Y))
log("[22] -N(L,bc,bL,cL) divisible by L^2:", rm.is_zero)
HM = sp.expand(qm.as_expr())
tH = sp.Poly(HM, X, Y).terms()
log(f"[22] H_M: {len(tH)} nonzero coefficients, all positive: {all(c_ > 0 for _, c_ in tH)} (src 192 positive)")
cert = sp.Poly(sp.expand(47045881 * HM - 327448292668 * LM**6), X, Y)
tc = cert.terms()
const = cert.coeff_monomial(1)
log(f"[22] 47045881 H_M - 327448292668 L_M^6: constant term {const}, nonzero coefficients {len([1 for _, c_ in tc if c_ != 0])}, all nonzero positive: {all(c_ > 0 for _, c_ in tc if c_ != 0)} (src 0, 191, positive)")

# ---- item 23 certificates
JE = 16*w**2*u**2 + 8*w**2*u + 28*w*u + 4*u + w**2 + 2*w + 1
log("[23] S/p == J_E/(16wu) on E roots:", sp.simplify(sum(rootsE) - JE) == 0)
resE = sp.expand(449**6 * PE - 1310720 * 4 * w**4 * JE**6)
tE = translated_coeffs(resE)
log(f"[23] 449^6 P_E - 1310720*4w^4J_E^6 at (1+X,1+Y): {len(tE)} coefficients, all positive: {all(c_ > 0 for _, c_ in tE)} (src 221 positive)")
JM = 8*X**3 + 12*X**2*Y + 4*X*Y**2 + 61*X**2 + 57*X*Y + 7*Y**2 + 151*X + 63*Y + 120
log("[23] (1+b+c)L + bc == J_M (so S/p = J_M/L_M):", sp.expand((1 + b + c) * L + b * c - JM) == 0)
r1 = sp.Poly(sp.expand(483**6 * HM - 81920 * JM**6), X, Y).terms()
log(f"[23] 483^6 H_M - 81920 J_M^6: {len(r1)} nonzero coefficients, all positive: {all(c_ > 0 for _, c_ in r1)}")
r2 = sp.Poly(sp.expand(4 * 52**4 * 483**4 * (b + c)**2 * HM - 81920 * LM**4 * (Y + 1)**2 * JM**4), X, Y).terms()
log(f"[23] 4*52^4*483^4 (b+c)^2 H_M - 81920 L_M^4 (Y+1)^2 J_M^4: {len(r2)} nonzero coefficients, all positive: {all(c_ > 0 for _, c_ in r2)}")
log("[23] c = 80/6279^4 == 81920/(4*52^4*483^4):", sp.Rational(80, 6279**4) == sp.Rational(81920, 4 * 52**4 * 483**4))
log("time so far %.0fs" % (time.time() - T0))

# ---- exact census on actual witnesses
def all_witnesses(p):
    h = (p - 1) // 12
    sols = set()
    for a in range(3 * h + 1, 9 * h + 1):
        R, Sa = 4 * a - p, p * a
        for d in divisors(Sa * Sa):
            if (d + Sa) % R == 0:
                y = (Sa + d) // R; z = (Sa + Sa * Sa // d) // R
                sols.add(tuple(sorted((a, y, z))))
    return sols
def Nint(roots):
    s = sum(roots)
    E2 = sum(roots[i] * roots[j] for i in range(4) for j in range(i + 1, 4))
    E3 = sum(roots[i] * roots[j] * roots[k] for i in range(4) for j in range(i + 1, 4) for k in range(j + 1, 4))
    E4 = roots[0] * roots[1] * roots[2] * roots[3]
    return Nfun(E2, E3, E4, s)
c12f = Fraction(125873811, 262144); c24f = Fraction(327448292668, 47045881)
nw = 0; viol = 0; worst = None; minhalf_ok = True; distinct_ok = True
for p in primerange(13, 1300):
    if p % 12 != 1: continue
    for sol in all_witnesses(p):
        nw += 1
        roots = (p,) + sol
        if len(set(roots)) != 4: distinct_ok = False
        if not (p < 4 * sol[0] and 2 * sol[0] < p and sol[0] < sol[1]): minhalf_ok = False
        Nv = Nint(roots)
        ratio = Fraction(-Nv, p**8)
        cc = c24f if p % 24 == 1 else c12f
        if not ratio > cc: viol += 1
        if worst is None or ratio / cc < worst[0]:
            worst = (ratio / cc, p, sol, float(ratio))
log(f"[22] witnesses at primes p=1 mod 12 below 1300: {nw}; four distinct roots always: {distinct_ok}; unique smallest denominator in (p/4,p/2): {minhalf_ok}; violations of N < -c p^8: {viol}")
log(f"[22] tightest case: (-N/p^8)/c = {float(worst[0]):.4f} at p={worst[1]}, witness {worst[2]}")

# ---- numeric receiver norms (item 22/23 bounds) on small witnesses
mpmath.mp.dps = 60
cc = mpmath.mpf(80) / mpmath.mpf(6279)**4
nchk = 0; bad = 0; mx = [0, 0, 0]; mins3 = mpmath.inf
for p in primerange(13, 200):
    if p % 12 != 1: continue
    for sol in all_witnesses(p):
        roots = [mpmath.mpf(x) for x in (p,) + sol]
        Ssum = sum(roots); Av = -1 / Ssum
        dj = []
        for j in range(4):
            prodv = Av
            for k in range(4):
                if k != j: prodv *= (roots[j] - roots[k])
            dj.append(prodv)
        O = mpmath.matrix(4, 4)
        for j in range(4):
            xi = 1 / mpmath.sqrt(mpmath.mpc(dj[j]))
            col = [1, -1j * dj[j], Av * dj[j]**2 + 2 * roots[j] * dj[j], 1j * (7 * roots[j]**2 * dj[j] - 13 * dj[j]**2)]
            for i in range(4): O[i, j] = xi * col[i]
        sv = sorted(mpmath.svd_c(O, compute_uv=False), reverse=True)
        s1, s2, s3, s4 = sv
        R = 4 * sol[0] - p
        wv = mpmath.mpf(p) / R
        inv = 1 / s4; w2 = 1 / (s3 * s4); w3 = 1 / (s2 * s3 * s4)
        Nv = Nint((p,) + sol)
        detabs = abs(mpmath.det(O))
        ok = (inv < 360 / cc * p * mpmath.sqrt(wv)) and (w2 < 180 / cc) and (w3 < 41 / (4 * cc * p**2)) and s3 > mpmath.sqrt(cc / 180)
        ok = ok and abs(detabs - 4 * abs(Nv) / Ssum**3) < mpmath.mpf(10)**-30 * detabs
        cg = mpmath.mpf(125873811) / 262144
        ok = ok and detabs > 4 * cg * mpmath.mpf(p)**8 / Ssum**3
        nchk += 1; bad += (not ok)
        mx[0] = max(mx[0], inv / (p * mpmath.sqrt(wv))); mx[1] = max(mx[1], w2); mx[2] = max(mx[2], w3 * p**2)
        mins3 = min(mins3, s3)
log(f"[22/23] numeric receiver checks on {nchk} witnesses (p<200): failures {bad}; |det O| = 4|N|/S^3 checked; "
    f"max ||O^-1||/(p sqrt w) = {mpmath.nstr(mx[0], 5)}, max ||wedge2 O^-1|| = {mpmath.nstr(mx[1], 5)}, max p^2||wedge3 O^-1|| = {mpmath.nstr(mx[2], 5)}, min s3 = {mpmath.nstr(mins3, 5)}")
log("time %.0fs" % (time.time() - T0))
