#!/usr/bin/env python3
"""Independent numerical check of FGR2.3 and FGR4.2 (programme, 25 September 2026):
the compressed translation trace over the full zero-jet constraint space on [-T, T] tends to
    sum_rho m_rho exp(-|beta - 1/2| |t|) exp(i gamma t),
although same-side unit vectors do NOT become orthogonal (FGR2.3).
Synthetic exponents only (no zeta zeros are claimed off the line).
claude-ab, model claude-opus-5-5 (Opus 5.5, max effort), 25 September 2026.
"""
import mpmath as mp
mp.mp.dps = 60

# (beta, gamma, multiplicity): two right-side exponents (one double), one left, one critical
OMEGA = [(mp.mpf("0.70"), mp.mpf("3.0"), 1),
         (mp.mpf("0.60"), mp.mpf("5.0"), 2),
         (mp.mpf("0.35"), mp.mpf("4.0"), 1),
         (mp.mpf("0.50"), mp.mpf("7.0"), 1)]

def cols():
    out = []
    for beta, gamma, m in OMEGA:
        z = (beta - mp.mpf(1) / 2) + 1j * gamma
        for j in range(m):
            out.append((z, j))
    return out

def prim_int(p, c, lo, hi):
    """exact int_lo^hi x^p e^{c x} dx"""
    if c == 0:
        return (hi ** (p + 1) - lo ** (p + 1)) / (p + 1)
    def F(x):
        return mp.exp(c * x) * sum((-1) ** k * mp.factorial(p) / mp.factorial(p - k) * x ** (p - k) / c ** (k + 1)
                                  for k in range(p + 1))
    return F(hi) - F(lo)

def inner(za, ja, zb, jb, T, t=0):
    """<v_a, V(t) v_b> = int conj(v_a(x)) v_b(x - t) dx over the common window,
    v_(z,j)(x) = 1_[-T,T](x) x^j exp(conj(z) x); conj-linear in the first argument.
    Exact closed form: expand (x - t)^jb binomially."""
    lo, hi = max(-T, -T + t), min(T, T + t)
    if hi <= lo:
        return mp.mpc(0)
    c = za + mp.conj(zb)
    tot = mp.mpc(0)
    for q in range(jb + 1):
        tot += mp.binomial(jb, q) * (-t) ** (jb - q) * prim_int(ja + q, c, lo, hi)
    return tot * mp.exp(-mp.conj(zb) * t)

def trace(T, t):
    C = cols()
    n = len(C)
    G = mp.matrix(n, n); A = mp.matrix(n, n)
    for a, (za, ja) in enumerate(C):
        for b, (zb, jb) in enumerate(C):
            G[a, b] = inner(za, ja, zb, jb, T, 0)
            A[a, b] = inner(za, ja, zb, jb, T, t)
    X = mp.inverse(G) * A
    return sum(X[i, i] for i in range(n))

def limit(t):
    return sum(m * mp.exp(-abs(beta - mp.mpf(1) / 2) * abs(t)) * mp.exp(1j * gamma * t)
               for beta, gamma, m in OMEGA)

lines = []
def say(s):
    print(s); lines.append(s)

for t in (mp.mpf("0.7"), mp.mpf("-1.3")):
    L = limit(t)
    say("t = %s: predicted limit (FGR4.2) = %s" % (mp.nstr(t, 3), mp.nstr(L, 12)))
    for T in (10, 20, 40, 80):
        v = trace(mp.mpf(T), t)
        say("   T = %3d: Tr(P V(t)) = %s   |difference| = %s" % (T, mp.nstr(v, 12), mp.nstr(abs(v - L), 3)))

# FGR2.3: limiting inner product of the two simple right-side unit vectors
za = (OMEGA[0][0] - mp.mpf(1) / 2) + 1j * OMEGA[0][1]
zb = (OMEGA[1][0] - mp.mpf(1) / 2) + 1j * OMEGA[1][1]
pred = 2 * mp.sqrt((OMEGA[0][0] - 0.5) * (OMEGA[1][0] - 0.5)) / (za + mp.conj(zb))
for T in (20, 40, 80):
    T = mp.mpf(T)
    g = inner(za, 0, zb, 0, T) / mp.sqrt(inner(za, 0, za, 0, T).real * inner(zb, 0, zb, 0, T).real)
    # remove the common phase exp(i(gamma_a - gamma_b)T) coming from the endpoint normalization
    ph = mp.exp(1j * (OMEGA[0][1] - OMEGA[1][1]) * T)
    say("FGR2.3: T = %d: |<u_a,u_b>| = %s ; predicted |limit| = %s" % (int(T), mp.nstr(abs(g), 12), mp.nstr(abs(pred), 12)))
# discrete example of FGR2.3: 2^n, 3^n on -N..N
for N in (10, 20, 40):
    s = sum(mp.mpf(6) ** k for k in range(-N, N + 1))
    n2 = sum(mp.mpf(4) ** k for k in range(-N, N + 1)); n3 = sum(mp.mpf(9) ** k for k in range(-N, N + 1))
    say("discrete 2^n, 3^n, N = %d: normalized inner product %s ; sqrt(24)/5 = %s" % (N, mp.nstr(s / mp.sqrt(n2 * n3), 15), mp.nstr(mp.sqrt(24) / 5, 15)))
