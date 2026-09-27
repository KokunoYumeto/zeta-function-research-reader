#!/usr/bin/env python3
"""ver52_referee_claims.py -- author's independent verification of the referee findings on note 52_ that are adopted
(F1 G = ker Phi; F4 non-split; F5 H' = <c, c'>; F6 classification of Levi-normal subgroups; F7 ES-09 orbits for all D;
F3 the S6 peripheral character; F2/F8 the standard Heisenberg subgroup and v_H; F10 the normal form on {F3 != 0};
F11 the mu_2 structure; F12 fibres over F_p and R; F14 the Section 2.3 examples; F16 distinct fibre values).
Written independently of the referee's scripts (different implementations)."""
import itertools, random, time, math
import numpy as np, sympy as sp
T0t = time.time(); random.seed(20260927)
res = []
def check(name, cond):
    ok = bool(cond); res.append((name, ok)); print(("PASS" if ok else "FAIL") + "  " + name, flush=True)

# ---------------- Part B: exact integer matrices (sympy) ----------------
T1 = sp.Matrix([[1, 0, -6, 2], [0, -1, 1, 1], [0, -1, 0, 1], [0, 0, 0, 1]])
T2 = sp.Matrix([[1, 6, 0, -3], [0, 0, -1, 1], [0, 1, 0, 0], [0, 0, 0, 1]])
Q0 = sp.Matrix([[0, 0, 0, 1], [0, 0, 6, 0], [0, -6, 0, 0], [-1, 0, 0, 0]])
def h(p, r, s): return sp.Matrix([[1, -6*r, 6*p, s], [0, 1, 0, p], [0, 0, 1, r], [0, 0, 0, 1]])
def L(M): X = sp.eye(4); X[1:3, 1:3] = sp.Matrix(M); return X
R = sp.Matrix([[-1, 1], [-1, 0]]); S = sp.Matrix([[0, -1], [1, 0]]); T = sp.Matrix([[1, 1], [0, 1]])
T0 = (T1*T2).inv()
check("(V2) T1 = L_R h(-1,0,2), T2 = L_S h(0,-1,-3), T0 = L_{T^-1} h(0,0,1) (= L_{T^-1} t_gamma)",
      T1 == L(R)*h(-1, 0, 2) and T2 == L(S)*h(0, -1, -3) and T0 == L(T.inv())*h(0, 0, 1))

# ab: SL2(Z/12) -> Z/12 by BFS with values S -> 9, T -> 1; conflict-free => well-defined homomorphism
def key2(M): return tuple(int(v) % 12 for v in M)
gens2 = [(np.array([[0, -1], [1, 0]]), 9), (np.array([[1, 1], [0, 1]]), 1), (np.array([[0, 1], [-1, 0]]), 3), (np.array([[1, -1], [0, 1]]), 11)]
val = {key2(np.eye(2, dtype=int).flatten()): 0}; front = [np.eye(2, dtype=int)]; conflict = False
while front:
    nxt = []
    for X in front:
        vx = val[key2(X.flatten())]
        for g, vg in gens2:
            Y = (X @ g) % 12; k = key2(Y.flatten()); vy = (vx + vg) % 12
            if k in val:
                if val[k] != vy: conflict = True
            else:
                val[k] = vy; nxt.append(Y)
    front = nxt
def ab(M): return val[key2(np.array(M.tolist(), dtype=int).flatten())]
check(f"(V1) S -> 9, T -> 1 extends to a homomorphism ab: SL2(Z/12) -> Z/12 (BFS over {len(val)} elements, no conflict); ab(R) = {ab(R)}, ab(-I) = {ab(-sp.eye(2))}",
      not conflict and len(val) == 1152 and ab(R) == 4 and ab(-sp.eye(2)) == 6 and ab(S) == 9 and ab(T) == 1)

def decompose(g):
    """g in G_Z (fixes gamma, preserves Q0) -> (M, (p, r, s)) with g = L_M h(p,r,s)."""
    M = g[1:3, 1:3]; hh = L(M).inv()*g
    p, r, s = hh[1, 3], hh[2, 3], hh[0, 3]
    assert hh == h(p, r, s), hh
    return M, (int(p), int(r), int(s))
def q(p, r): return (p*p + p*r + r*r) % 2
def Phi(g):
    M, (p, r, s) = decompose(g); return (s - 6*q(p, r) + ab(M)) % 12
check("(V3) Phi(T1) = Phi(T2) = 0, Phi(t_gamma) = Phi(L_T) = 1", Phi(T1) == 0 and Phi(T2) == 0 and Phi(h(0, 0, 1)) == 1 and Phi(L(T)) == 1)
GZgens = [L(S), L(T), h(1, 0, 0), h(0, 1, 0), h(0, 0, 1)]
def rand_word(gens, n):
    X = sp.eye(4)
    for _ in range(n):
        g = random.choice(gens); X = X*(g if random.random() < 0.5 else g.inv())
    return X
okhom = True
for _ in range(150):
    a1, a2 = rand_word(GZgens, random.randint(1, 12)), rand_word(GZgens, random.randint(1, 12))
    if (Phi(a1*a2) - Phi(a1) - Phi(a2)) % 12 != 0: okhom = False
check("(V3) Phi is a homomorphism on 150 random pairs of words in the G_Z generators", okhom)
okG = all(Phi(rand_word([T1, T2], random.randint(1, 30))) == 0 for _ in range(200))
check("(V3) Phi vanishes on 200 random words in T1, T2", okG)

# (V4) G mod 12 = {Phi = 0} mod 12, by BFS (numpy)
def npm(M): return np.array(M.tolist(), dtype=np.int64)
def closure(gens, D):
    gl = [npm(g) % D for g in gens] + [npm(g.inv()) % D for g in gens]
    start = np.eye(4, dtype=np.int64); seen = {start.tobytes()}; front = [start]
    while front:
        nxt = []
        for X in front:
            for g in gl:
                Y = (X @ g) % D; k = Y.tobytes()
                if k not in seen: seen.add(k); nxt.append(Y)
        front = nxt
    return seen
G12 = closure([T1, T2], 12)
def Phi_mod12(Xb):
    X = np.frombuffer(Xb, dtype=np.int64).reshape(4, 4)
    M = X[1:3, 1:3] % 12
    # h = L_M^{-1} X mod 12: L_M^{-1} acts on rows 1..2 by M^{-1} (adj mod 12, det = 1)
    Minv = np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]]) % 12
    Hm = X.copy(); Hm[1:3, :] = (Minv @ X[1:3, :]) % 12
    p, r, s = int(Hm[1, 3]), int(Hm[2, 3]), int(Hm[0, 3])
    return (s - 6*q(p, r) + val[tuple(int(v) for v in M.flatten())]) % 12
check(f"(V4) every element of G mod 12 has Phi = 0 ({len(G12)} elements = 1152*1728/12 = {1152*1728//12})",
      len(G12) == 1152*1728//12 and all(Phi_mod12(kb) == 0 for kb in G12))

# (V5) H' = <c, c'>
c = T1*T2**2*T1.inv()*(T2**2).inv(); c2 = T2*c*T2.inv()
def inHp(p, r, s): return s % 6 == 0 and (s//6 - (p*p + p*r + r*r)) % 2 == 0
cover = {(p, r, (-6*p + 6*r + 6*p*r + 12*m)) for p in range(-4, 5) for r in range(-4, 5) for m in range(-20, 21)}
box = {(p, r, s) for p in range(-4, 5) for r in range(-4, 5) for s in range(-20, 21) if inHp(p, r, s)}
check("(V5) c = h(1,0,-6), c' = h(0,1,6), c^p c'^r = h(p, r, -6p + 6r + 6pr), [c,c'] = h(0,0,12), and these words exhaust H' (box)",
      c == h(1, 0, -6) and c2 == h(0, 1, 6) and all(c**p*c2**r == h(p, r, -6*p + 6*r + 6*p*r) for p in range(0, 4) for r in range(0, 4))
      and c*c2*c.inv()*c2.inv() == h(0, 0, 12) and box <= cover and all(inHp(*t) for t in cover))

# (V6) the N_k, k | 12: subgroups, Levi-invariant, full projection, index k
def inN(k, p, r, s): return (s - 6*q(p, r)) % k == 0
okN = True
for k in (1, 2, 3, 4, 6, 12):
    for (p1, r1, p2, r2) in itertools.product(range(-2, 3), repeat=4):
        for s1 in range(-12, 13):
            if not inN(k, p1, r1, s1): continue
            for s2 in (-k, 0, k, 2*k):
                s2v = s2 + 6*q(p2, r2)
                if not inN(k, p2, r2, s2v): okN = False
                if not inN(k, p1 + p2, r1 + r2, s1 + s2v + 6*(p1*r2 - p2*r1)): okN = False
    for M in (R, S, T):
        for (p, r) in itertools.product(range(-3, 4), repeat=2):
            v = M*sp.Matrix([p, r])
            for s in range(-12, 13):
                if inN(k, p, r, s) != inN(k, int(v[0]), int(v[1]), s): okN = False
    cnt = sum(1 for p in range(12) for r in range(12) for s in range(12) if inN(k, p, r, s))
    if cnt*k != 12**3: okN = False
check("(V6) N_k = {h : s = 6(p^2+pr+r^2) mod k}, k | 12, are Levi-invariant subgroups with full projection and index k (N_12 = H', N_6 = {6 | s})", okN)

# (V7) non-split: conjugation formula
x1, x2, y1, y2, t_ = sp.symbols('x1 x2 y1 y2 t')
g_R = L(R)*h(y1, y2, t_); inv_mI = L(-sp.eye(2))*h(x1, x2, 0)
lhs = sp.expand(g_R*inv_mI*g_R.inv())
Rx = R*sp.Matrix([x1 - 2*y1, x2 - 2*y2])
check("(V7) L_R h(y,t) . L_{-I} h(x,0) . (L_R h(y,t))^-1 = L_{-I} h(R(x - 2y), 0); R mod 2 fixes no nonzero vector of F_2^2",
      sp.expand(lhs - L(-sp.eye(2))*h(Rx[0], Rx[1], 0)) == sp.zeros(4)
      and all(((R*sp.Matrix(v)) % 2) != sp.Matrix(v) for v in [(1, 0), (0, 1), (1, 1)]))
check("(V7) elements of G over -I of order 2 are exactly L_{-I} h(x, 0) with q(x) = 1 (box |x| <= 3, |s| <= 12)",
      all(((L(-sp.eye(2))*h(p, r, s))**2 == sp.eye(4) and Phi(L(-sp.eye(2))*h(p, r, s)) == 0) == (s == 0 and q(p, r) == 1)
          for p in range(-3, 4) for r in range(-3, 4) for s in range(-12, 13)))

# (V8)-(V9) ES-09: dual action and orbits for all D (checked D = 2..14)
p_, r_, s_ = sp.symbols('p r s'); b_, c_, d_ = sp.symbols('b c d')
Ah = (h(p_, r_, s_).inv()).T
img = Ah*sp.Matrix([1, b_, c_, d_])
check("(V9) the dual action of h(p,r,s) on (1, b, c, d): (b, c, d) -> (b + 6r, c - 6p, d - s - pb - rc) (as the referee states)",
      sp.expand(img - sp.Matrix([1, b_ + 6*r_, c_ - 6*p_, d_ - s_ - p_*b_ - r_*c_])) == sp.zeros(4, 1))
def orbit_partition(gens, D):
    pts = list(itertools.product(range(D), repeat=3)); idx = {pt: i for i, pt in enumerate(pts)}
    parent = list(range(len(pts)))
    def find(i):
        while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
        return i
    A = [npm((g.inv()).T) % D for g in gens]
    for i, (b, cc, d) in enumerate(pts):
        v = np.array([1, b, cc, d], dtype=np.int64)
        for Ag in A:
            wv = (Ag @ v) % D; j = idx[(int(wv[1]), int(wv[2]), int(wv[3]))]
            ri, rj = find(i), find(j)
            if ri != rj: parent[ri] = rj
    cls = {}
    for i, pt in enumerate(pts): cls.setdefault(find(i), []).append(pt)
    return sorted(sorted(v) for v in cls.values())
okorb = True; sizes = {}
for D in range(2, 15):
    PG = orbit_partition([T1, T2], D)
    e = math.gcd(D, 6)
    pred = {}
    for (b, cc, d) in itertools.product(range(D), repeat=3):
        pred.setdefault(math.gcd(math.gcd(b, cc), e), []).append((b, cc, d))
    if PG != sorted(sorted(v) for v in pred.values()): okorb = False
    sizes[D] = sorted(len(v) for v in PG)
check(f"(V8) for D = 2..14 the G-orbits on the hyperplane are exactly the classes of gcd(b, c, gcd(D,6)); sizes {sizes}", okorb)

# (V10) the S6 peripheral character: chi(M^T) = ab(M) where chi = -ab (normalization chi(C0) = chi(T) = -1)
C1 = sp.Matrix([[-1, -1], [1, 0]]); C2p = sp.Matrix([[0, 1], [-1, 0]]); C0 = sp.Matrix([[1, 1], [0, 1]])
chi = lambda M: (-ab(M)) % 12
rnd = [sp.Matrix(np.array(M, dtype=int).reshape(2, 2)) for M in random.sample(sorted(val.keys()), 40)]
check("(V10) 15_ (27)/(88): C1 = R^T, C2' = S^T, C0 = T, (chi(C0), chi(C1), chi(C2')) = (-1, 4, -3) = (ab pi T0, ab pi T1, ab pi T2); chi(M^T) = ab(M) (40 random M mod 12)",
      C1 == R.T and C2p == S.T and C0 == T and (chi(C0), chi(C1), chi(C2p)) == (11, 4, 9)
      and (ab(T0[1:3, 1:3]), ab(T1[1:3, 1:3]), ab(T2[1:3, 1:3])) == (11, 4, 9)
      and all(chi((M.T).applyfunc(lambda z: z % 12)) == ab(M) for M in rnd))

# (V11) standard Heisenberg subgroup H(Z) = {h(p,r,6k)} and v_H
okH = all(h(p1, r1, 6*k1)*h(p2, r2, 6*k2) == h(p1 + p2, r1 + r2, 6*(k1 + k2 + p1*r2 - p2*r1))
          for p1, r1, k1, p2, r2, k2 in itertools.product(range(-1, 2), repeat=6))
okv = all(inHp(p, r, 6*k) == ((p + r + p*r + k) % 2 == 0) for p in range(-4, 5) for r in range(-4, 5) for k in range(-4, 5))
check("(V11) {h(p,r,6k)} has the standard Heisenberg law k1 + k2 + (p1 r2 - p2 r1), and H' = ker v_H, v_H = (-1)^(p+r+pr+k)", okH and okv)

# ---------------- Part A ----------------
x, y, w = sp.symbols('x y w')
F1 = (1+x*y)**3*w + y**2*(1+x*y)*(4+3*x*y); F2 = y + 3*x*(1+x*y)**2*w + 3*x*y**2*(4+3*x*y); F3 = 2*x - 3*x**2*y - x**3*w
n = 2 - 3*x*y - x**2*w; m = (1 + x*y)*n
check("(V13) F3 = x n, F1 F3^2 = m(n + m - m^2), F2 F3 = 2n + 4m - 3m^2 (n = 2 - 3xy - x^2 w, m = (1+xy) n)",
      sp.expand(F3 - x*n) == 0 and sp.expand(F1*F3**2 - m*(n + m - m**2)) == 0 and sp.expand(F2*F3 - (2*n + 4*m - 3*m**2)) == 0)
cc, mm, nn = sp.symbols('c m n')
xi, yi = cc/nn, (mm - nn)/cc; wi = (2 - 3*(mm/nn - 1) - nn)*nn**2/cc**2
check("(V13) (x,y,w) -> (F3, m, n) has inverse x = c/n, y = (m - n)/c, w = (2 - 3(m/n - 1) - n) n^2/c^2 (both composites identity)",
      sp.simplify(F3.subs({x: xi, y: yi, w: wi}) - cc) == 0 and sp.simplify(m.subs({x: xi, y: yi, w: wi}) - mm) == 0
      and sp.simplify(n.subs({x: xi, y: yi, w: wi}) - nn) == 0
      and all(sp.simplify(e.subs({cc: F3, mm: m, nn: n}) - v0) == 0 for e, v0 in ((xi, x), (yi, y), (wi, w))))
g1 = mm*(nn + mm - mm**2); g2 = 2*nn + 4*mm - 3*mm**2
P_, Q_, M_ = sp.symbols('P Q M')
hM = M_**3 - 2*M_**2 + Q_*M_ - 2*P_
gcurve = 27*P_**2 - 18*P_*Q_ + 16*P_ + Q_**3 - Q_**2
al, be = Q_ - sp.Rational(4, 3), 2*Q_/3 - 2*P_ - sp.Rational(16, 27)
Sv = sp.symbols('S'); av, bv, cv = sp.symbols('a b c')
check("(V13) det D(g1,g2)/D(m,n) = 2n; g = (P,Q) iff h(m) = 0 and n = h'(m)/2; Disc h = -4 g(P,Q); h(m'+2/3) = m'^3 + alpha m' + beta, 4 g = 4 alpha^3 + 27 beta^2",
      sp.expand(sp.Matrix([[sp.diff(g1, mm), sp.diff(g1, nn)], [sp.diff(g2, mm), sp.diff(g2, nn)]]).det() - 2*nn) == 0
      and sp.expand((mm**3 - 2*mm**2 + g2*mm - 2*g1)) == 0
      and sp.expand(sp.diff(hM, M_).subs({M_: mm, Q_: g2})/2 - nn) == 0
      and sp.expand(sp.discriminant(hM, M_) + 4*gcurve) == 0
      and sp.expand(hM.subs(M_, M_ + sp.Rational(2, 3)) - (M_**3 + al*M_ + be)) == 0
      and sp.expand(4*gcurve - (4*al**3 + 27*be**2)) == 0)
check("(V13) with P = a c^2, Q = b c and m = -2c/S: f(S,1) = a S^3 + b S^2 + 4S + 4c = (4c/m^3) h(m)",
      sp.simplify((av*Sv**3 + bv*Sv**2 + 4*Sv + 4*cv) - (4*cv/M_**3*hM).subs({P_: av*cv**2, Q_: bv*cv}).subs(M_, -2*cv/Sv)) == 0)
check("(V14) mu_2: (-1).(1,-3/2,13/2) = (-1,3/2,13/2); the fixed locus of -1 is the w-axis, and F(0,0,w) = (w,0,0)",
      (sp.Integer(-1)**-1*1, -1*sp.Rational(-3, 2), sp.Rational(13, 2)) == (-1, sp.Rational(3, 2), sp.Rational(13, 2))
      and [sp.expand(e.subs({x: 0, y: 0})) for e in (F1, F2, F3)] == [w, 0, 0])
# (V15) fibres over F_p by brute force
def Fmod(X, Y, W, p):
    a = ((1+X*Y)**3*W + Y*Y*(1+X*Y)*(4+3*X*Y)) % p
    b = (Y + 3*X*(1+X*Y)**2*W + 3*X*Y*Y*(4+3*X*Y)) % p
    c3 = (2*X - 3*X*X*Y - X**3*W) % p
    return a, b, c3
def simple_roots(a, b, c3, p):
    cnt = 0
    for s0, t0 in [(1, 0)] + [(s0, 1) for s0 in range(p)]:
        f = (a*s0**3 + b*s0**2*t0 + 4*s0*t0**2 + 4*c3*t0**3) % p
        if f: continue
        if (s0, t0) == (1, 0):   # root at infinity: a = 0; simple iff b != 0
            cnt += 1 if b % p else 0
        else:
            df = (3*a*s0**2 + 2*b*s0 + 4) % p   # d/ds f(s,1) (t0 = 1)
            cnt += 1 if df else 0
    return cnt
okp = True; hist = {}
for p in (3, 5, 7, 11):
    fib = {}
    for X, Y, W in itertools.product(range(p), repeat=3):
        fib[Fmod(X, Y, W, p)] = fib.get(Fmod(X, Y, W, p), 0) + 1
    hh = {}
    for tgt in itertools.product(range(p), repeat=3):
        k = fib.get(tgt, 0); hh[k] = hh.get(k, 0) + 1
        if k != simple_roots(*tgt, p): okp = False
    hist[p] = dict(sorted(hh.items()))
    if not set(hh) <= {0, 1, 3}: okp = False
check(f"(V15) over F_p (p = 3,5,7,11) every fibre has as many points as the slice cubic has F_p-rational simple roots; sizes only 0,1,3: {hist}", okp)
# (V16) the Section 2.3 examples
def ABC(X, Y, W):
    return ((1+X*Y)**2*W + Y*Y*(4+3*X*Y), X*(1+X*Y)*W + Y*(1+3*X*Y), 2*(2 - 3*X*Y - X*X*W))
check("(V16) (1,-2,8): (A,B,C) = (0,2,0); (0,4,-63): B^2 - 4AC = 0", ABC(1, -2, 8) == (0, 2, 0) and (lambda A, B, C: B*B - 4*A*C)(*ABC(0, 4, -63)) == 0)
# (V17) the fibre over (1,2,3): three distinct values of x, y and w (mpmath, 50 digits)
import mpmath as mp
mp.mp.dps = 50
a0, b0, c0 = 1, 2, 3
roots = mp.polyroots([a0, b0, 4, 4*c0], maxsteps=200, extraprec=200)
pts = []
for S0 in roots:
    u0, v0 = S0, mp.mpf(1)
    # quotient Q0 = f / (v0 s - u0 t) at the scaled root: normalization Q(u,v) = 4 with (u,v) = mu (u0, v0)
    # coefficients of Q from division: f = (v s - u t)(A s^2 + B s t + C t^2)
    A0 = a0/v0; B0 = (b0 + u0*A0)/v0; C0v = (4 + u0*B0)/v0
    qv = A0*u0**2 + B0*u0*v0 + C0v*v0**2
    mu = 4/qv
    u1, v1 = mu*u0, mu*v0; A1, B1, C1v = A0/mu, B0/mu, C0v/mu
    xx = -u1/2; yy = (A1*u1 + 2*B1*v1)/2
    ww = ((C1v**3*v1 - 3*B1*C1v**2*u1)*(A1 - yy**2*(4 + 3*xx*yy)) + (3*B1**2*C1v*v1 - B1**3*u1)*(4*(2 - 3*xx*yy - C1v/2)))/64
    pts.append((xx, yy, ww))
def Fn(X, Y, W): return ((1+X*Y)**3*W + Y**2*(1+X*Y)*(4+3*X*Y), Y + 3*X*(1+X*Y)**2*W + 3*X*Y**2*(4+3*X*Y), 2*X - 3*X**2*Y - X**3*W)
err = max(abs(e1 - e2) for P0 in pts for e1, e2 in zip(Fn(*P0), (a0, b0, c0)))
sep = min(min(abs(P0[k] - P1[k]) for P0, P1 in itertools.combinations(pts, 2)) for k in range(3))
check(f"(V17) over (1,2,3): the three fibre points (from the roots via iota^-1) map back (error {mp.nstr(err, 3)}), and x, y, w each take three distinct values (min separation {mp.nstr(sep, 5)})",
      err < mp.mpf(10)**-40 and sep > mp.mpf(10)**-3)
print(f"\nsummary: {len(res)} checks, {sum(o for _, o in res)} PASS, {len(res) - sum(o for _, o in res)} FAIL; {time.time()-T0t:.0f}s")
