#!/usr/bin/env python3
"""Checks for note 22_ (the owner's anomaly-cancellation picture, M17-M20, made exact).

claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.

 1. G(s) = xi(s) xi(s+1)/16 (the programme's F0(s)F0(s+1), F0 = xi/4): G(-conj s) = conj G(s), and
    G(it) = |xi(1+it)|^2/16 > 0 on the line Re s = 0 through the pole at 0.
 2. The two lines as the two sheets of a connected double cover on the Clifford torus:
    s -> (s, s-1)/(sqrt2 |s|) on Re s = 1/2 and s -> (s, s+1)/(sqrt2 |s|) on Re s = -1/2 land on
    Gamma(phi) = (e^{i phi}, -e^{-i phi})/sqrt2; the base point w = z1/z2 runs once round the unit circle along each line;
    Gamma(phi + pi) = -Gamma(phi) (the central element -1 of SU(2) is the deck transformation).
 3. Chirality: D(phi) = (e^{i phi}, e^{i phi})/sqrt2 (the owner's Hopf fibre, pairing (s, 1 - conj s)) is an orbit of the left
    U(1) action q -> e^{i a} q, Gamma an orbit of the right action q -> q e^{i a} (q = z1 + z2 j); the reflection
    (z1, z2) -> (z1, -conj z2) maps Gamma onto D and has determinant -1 on R^4.
 4. Connes-Consani's twistor real structure z -> -1/conj z lifts to sigma(z1, z2) = (-conj z2, conj z1) = left multiplication
    by the quaternion j; sigma^2 = -1 (quaternionic, as for the SU(2) doublet); on |z| = 1 it is z -> -z; it has no fixed
    point on CP^1; on two copies, sigma (x) sigma squares to +1 (a real structure).
 5. The Bombelli generator: J^2 = eps, J^4 = 1 (J -> i); the odd Frobenius z -> z^n (n = 1 mod 4), -1/z^n (n = 3 mod 4) has
    winding number chi_{-4}(n) n on the unit circle.
 6. The Klein four-group {id, A, P, T = AP} on the two-line zero system; orbit sizes 2 (on-line) and 4 (off-line);
    the partner-loop holonomy T^{-1} A equals the reflection # on copy 0.
 7. Parity matching for zeta: sign Z(T) = -(-1)^{N(T)} (Hardy's Z, Riemann-von Mangoldt N), which holds with or without
    off-line zeros because they come in pairs at the same height; the counting hierarchy n_G = 2 N_0 + 4 N_pairs.
 8. The bulk between the two lines: the zeros of G in -1/2 < Re s < 1/2 are the off-line zeros left of 1/2 and their mirrors.
 9. The same structure for the Davenport-Heilbronn function f (no Euler product, zeros off the line):
    Lambda_f(s) = (5/pi)^{(s+1)/2} Gamma((s+1)/2) f(s) (the character is odd) satisfies Lambda_f(s) = Lambda_f(1-s) and Lambda_f(conj s) = conj Lambda_f(s);
    G_f(s) = Lambda_f(s) Lambda_f(s+1) is A-real and >= 0 on Re s = 0; its off-line zero has a V4-orbit of size 4.
 10. The 0-centred pairing of the two-line system, Q_A(f) = sum over zeros w of G of f(w) conj f(-conj w), is real but
    indefinite even when every zero used is on the line (first 30 zeros of zeta and their conjugates).
 4d. sigma commutes with SU(2): sigma(U z) = U sigma(z).
 11. The anti-number involution on the clock u (M21-M23): g -> conj g(1/u) (Haar normalisation) has Mellin shadow s -> -conj s
    (the mirror A); g -> conj g(1/u)/u (Lebesgue normalisation) has shadow s -> 1 - conj s (#); the two differ by the factor u.
    Number and anti-number annihilate into a norm: (g * g*)(1) = int |g|^2 du/u. The Cartan involution theta(g) = (g*)^{-1}
    acts on the characters u^{s - 1/2} by s -> 1 - conj s and fixes exactly Re s = 1/2.
 12. Knots and root numbers: for every primitive character mod 5 and mod 7, Lambda(s, chi) = W(chi) Lambda(1-s, conj chi),
    |W| = 1, W(chi) W(conj chi) = 1; real characters have W = 1.
 13. The Davenport-Heilbronn function is a superposition of the particle sector L(s, chi) and the antiparticle sector
    L(s, conj chi), with conjugate coefficients; each sector alone crosses tau with the phase W(chi), W(conj chi).
"""
import os, math, cmath
import numpy as np
import mpmath as mp

mp.mp.dps = 30
out = []
def say(s=""):
    print(s); out.append(s)

def xi(s):
    s = mp.mpc(s)
    if s == 0 or s == 1:
        return mp.mpf(1) / 2      # xi(0) = xi(1) = 1/2 (the removable singularities)
    return mp.mpf(1) / 2 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def G(s):
    return xi(s) * xi(s + 1) / 16

# 1
rng = np.random.default_rng(3)
err = 0
for _ in range(12):
    s = mp.mpc(rng.uniform(-1.5, 1.5), rng.uniform(-40, 40))
    err = max(err, abs(G(-mp.conj(s)) - mp.conj(G(s))) / abs(G(s)))
say("1a max relative |G(-conj s) - conj G(s)| over 12 random s in |Re s| <= 1.5, |Im s| <= 40: %.2e" % float(err))
vals = []
for t in [0, 0.5, 3, 14.134725, 21.022, 50, 100, 250]:
    g = G(mp.mpc(0, t)); ref = abs(xi(mp.mpc(1, t))) ** 2 / 16
    vals.append((t, float(g.real), float(abs(g.imag)), float(abs(g - ref) / ref)))
say("1b G(it) at t = 0, .5, 3, gamma_1, 21.022, 50, 100, 250: (t, Re G, |Im G|, rel. diff from |xi(1+it)|^2/16):")
for v in vals:
    say("    %s" % (tuple(round(x, 12) if isinstance(x, float) else x for x in v),))
say("1c min Re G(it) on the grid t in [0, 300], step 0.25: %.3e (positive)" % min(float(G(mp.mpc(0, t)).real) for t in np.arange(0, 300.01, 0.25)))

# 2
def Gam(phi):
    return np.array([np.exp(1j * phi), -np.exp(-1j * phi)]) / np.sqrt(2)
worst = 0; ws = []
for t in [-50, -3, -0.2, 0.0, 0.7, 4, 60]:
    s = 0.5 + 1j * t
    p = np.array([s, s - 1]) / (np.sqrt(2) * abs(s))
    worst = max(worst, np.abs(p - Gam(cmath.phase(s))).max())
    s2 = -0.5 + 1j * t
    q = np.array([s2, s2 + 1]) / (np.sqrt(2) * abs(s2))
    worst = max(worst, np.abs(q - Gam(cmath.phase(s2))).max())
say("2a (s, s-1)/(sqrt2|s|) on Re s = 1/2 and (s, s+1)/(sqrt2|s|) on Re s = -1/2 equal Gamma(arg s): max error %.1e" % worst)
ts = np.linspace(-2000, 2000, 400001)
w = (0.5 + 1j * ts) / (-0.5 + 1j * ts)
wind = np.sum(np.diff(np.unwrap(np.angle(w)))) / (2 * np.pi)
say("2b along the critical line (t from -2000 to 2000) the base point w = s/(s-1) winds %.4f times (-> 1 as t -> infinity); |w| = 1 exactly: %s"
    % (wind, bool(np.allclose(np.abs(w), 1))))
ph = np.linspace(0, 2 * np.pi, 13)
say("2c Gamma(phi + pi) + Gamma(phi) = 0 for 13 values of phi: %s ; the two points have the same base w: %s"
    % (bool(np.allclose([Gam(a + np.pi) + Gam(a) for a in ph], 0)),
       bool(np.allclose([Gam(a)[0] / Gam(a)[1] - Gam(a + np.pi)[0] / Gam(a + np.pi)[1] for a in ph], 0))))
# lift of the base loop: start on the critical line at t = -T (phi ~ -pi/2), follow Gamma continuously while w goes once round
phis = np.linspace(-np.pi / 2, np.pi / 2, 1001)
say("2d following the lift over one full turn of w, starting at Gamma(-pi/2 + 0) on the critical-line half, ends at Gamma(pi/2) = -Gamma(-pi/2): %s ; "
    "the next full turn traverses phi in (pi/2, 3pi/2), which is the line at -1/2 (arg of -1/2 + it lies in (pi/2, 3pi/2)): %s"
    % (bool(np.allclose(Gam(phis[-1]), -Gam(phis[0]))),
       all(np.pi / 2 < (cmath.phase(-0.5 + 1j * t) % (2 * np.pi)) < 3 * np.pi / 2 for t in [-100, -1, 0, 1, 100])))

# 3
def D(phi):
    return np.array([np.exp(1j * phi), np.exp(1j * phi)]) / np.sqrt(2)
worst = 0
for t in [-30, -1, 0.3, 5, 70]:
    s = 0.5 + 1j * t
    p = np.array([s, 1 - np.conj(s)]) / (np.sqrt(2) * abs(s))
    worst = max(worst, np.abs(p - D(cmath.phase(s))).max())
say("3a (s, 1 - conj s)/(sqrt2|s|) on the critical line equals D(arg s): max error %.1e" % worst)
a = 0.73
left = lambda z: np.exp(1j * a) * z
right = lambda z: np.array([np.exp(1j * a) * z[0], np.exp(-1j * a) * z[1]])
say("3b left action maps D(phi) to D(phi + a): %s ; right action maps Gamma(phi) to Gamma(phi + a): %s"
    % (bool(np.allclose(left(D(0.4)), D(0.4 + a))), bool(np.allclose(right(Gam(0.4)), Gam(0.4 + a)))))
# quaternion check: q = z1 + z2 j, with j z = conj(z) j
def qmul(p, q):   # p = (p1, p2), q = (q1, q2) representing p1 + p2 j
    return np.array([p[0] * q[0] - p[1] * np.conj(q[1]), p[0] * q[1] + p[1] * np.conj(q[0])])
e = np.array([np.exp(1j * a), 0]); jq = np.array([0, 1])
say("3c with q = z1 + z2 j: e^{ia} q = left action (%s); q e^{ia} = right action (%s)"
    % (bool(np.allclose(qmul(e, Gam(0.4)), left(Gam(0.4)))), bool(np.allclose(qmul(Gam(0.4), e), right(Gam(0.4))))))
Mref = lambda z: np.array([z[0], -np.conj(z[1])])
Rmat = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])   # (x1, y1, x2, y2) -> (x1, y1, -x2, y2)
say("3d the reflection (z1, z2) -> (z1, -conj z2) maps Gamma(phi) to D(phi): %s ; its determinant on R^4 = %d"
    % (bool(all(np.allclose(Mref(Gam(p_)), D(p_)) for p_ in ph)), int(round(np.linalg.det(Rmat)))))

# 4
sigma = lambda z: np.array([-np.conj(z[1]), np.conj(z[0])])
z0 = np.array([0.3 + 0.8j, -1.1 + 0.2j])
say("4a sigma^2 = -1: %s ; sigma = left multiplication by j: %s"
    % (bool(np.allclose(sigma(sigma(z0)), -z0)), bool(np.allclose(sigma(z0), qmul(jq, z0)))))
zz = [0.4 + 1.3j, -2 + 0.5j, 1j, np.exp(0.9j)]
say("4b induced map on z = z1/z2 is z -> -1/conj z: %s ; fixed points would need |z|^2 = -1 (none); on |z| = 1 it is z -> -z: %s"
    % (bool(all(np.isclose(sigma(np.array([z, 1]))[0] / sigma(np.array([z, 1]))[1], -1 / np.conj(z)) for z in zz)),
       bool(np.isclose(-1 / np.conj(np.exp(0.9j)), -np.exp(0.9j)))))
def sig2(v):   # sigma (x) sigma on C^2 (x) C^2, v a 2x2 array v[a, b]
    S = np.array([[0, -1], [1, 0]])        # sigma(z) = S conj(z)
    return S @ np.conj(v) @ S.T
v0 = np.array([[0.2 + 0.1j, 1 - 0.5j], [-0.7j, 0.3 + 0.9j]])
say("4c (sigma (x) sigma)^2 = +1 on C^2 (x) C^2: %s" % bool(np.allclose(sig2(sig2(v0)), v0)))

# 5
J = 1j
say("5a J^2 = eps = -1: %s ; J^4 = 1: %s ; the four directions {1, J, eps, eps J} = %s" % (J ** 2 == -1, J ** 4 == 1, [1, J, -1, -J]))
res = []
for n in [1, 3, 5, 7, 9, 11, 13, 15]:
    th = np.linspace(0, 2 * np.pi, 20001)
    z = np.exp(1j * th)
    img = z ** n if n % 4 == 1 else -1 / z ** n
    wnd = int(round(np.sum(np.diff(np.unwrap(np.angle(img)))) / (2 * np.pi)))
    chi = 1 if n % 4 == 1 else -1
    res.append((n, wnd, chi * n))
say("5b odd Frobenius winding on |z| = 1 vs chi_{-4}(n) n: %s ; all equal: %s" % (res, all(r[1] == r[2] for r in res)))

# 6
A = lambda s: -np.conj(s)
def P(s):   # internal reflection on each copy: about 1/2 on copy 0 (Re s > 0), about -1/2 on copy -1 (Re s < 0)
    return 1 - np.conj(s) if s.real > 0 else -1 - np.conj(s)
Tm = lambda s: A(P(s))
on = [0.5 + 14.1347j, 0.5 + 21.022j]
off = [0.7 + 30.0j]
zeros0 = on + off + [1 - np.conj(r) for r in off]
system = zeros0 + [r - 1 for r in zeros0]
def orbit(x):
    orb = {complex(round(x.real, 9), round(x.imag, 9))}
    for g in [A, P, Tm, lambda s: A(P(A(s)))]:
        y = g(x); orb.add(complex(round(y.real, 9), round(y.imag, 9)))
    return orb
closed = all(complex(round(g(x).real, 9), round(g(x).imag, 9)) in {complex(round(y.real, 9), round(y.imag, 9)) for y in system}
             for x in system for g in [A, P, Tm])
say("6a the synthetic two-line zero system is closed under A, P, T: %s ; A^2 = P^2 = id and AP = PA on it: %s"
    % (closed, all(np.isclose(A(A(x)), x) and np.isclose(P(P(x)), x) and np.isclose(A(P(x)), P(A(x))) for x in system)))
say("6b orbit sizes: on-line zeros %s ; off-line zero %s" % ([len(orbit(r)) for r in on], [len(orbit(r)) for r in off]))
say("6c T = AP is s -> s - 1 on copy 0 and s -> s + 1 on copy -1: %s ; holonomy T^{-1} A (go across by A, back by T^{-1}) on copy 0 equals # : %s ; trivial exactly on on-line zeros: %s"
    % (bool(all(np.isclose(Tm(x), x - 1) for x in zeros0) and all(np.isclose(Tm(x - 1), x) for x in zeros0)),
       bool(all(np.isclose(A(x) + 1, 1 - np.conj(x)) for x in zeros0)),
       [bool(np.isclose(A(x) + 1, x)) for x in zeros0]))

# 7
rows = []
for T in [10, 20, 30, 50, 100, 200, 500, 1000]:
    N = int(mp.nzeros(T)); Zt = mp.siegelz(T)
    rows.append((T, N, int(mp.sign(Zt)), -(-1) ** N))
say("7a (T, N(T), sign Z(T), -(-1)^N(T)): %s ; all match: %s" % (rows, all(r[2] == r[3] for r in rows)))
rng = np.random.default_rng(5)
ok = True
for _ in range(1000):
    N0, Np = int(rng.integers(0, 50)), int(rng.integers(0, 50))
    nz, nG = N0 + 2 * Np, 2 * N0 + 4 * Np
    ok &= (nz - N0) % 2 == 0 and (nG - 2 * N0) % 4 == 0 and (nG - 2 * N0) % 8 == 4 * (Np % 2)
say("7b counting hierarchy on 1000 random symmetric configurations: one line n - N0 = 2 N_pairs (blind mod 2); two lines n_G - 2 N0 = 4 N_pairs (blind mod 2 and mod 4, sees N_pairs mod 2 at mod 8): %s" % ok)

# 8
bulk = [x for x in system if -0.5 < x.real < 0.5]
pred = [r for r in zeros0 if r.real < 0.5] + [A(r) for r in zeros0 if r.real < 0.5]
say("8 zeros of the synthetic system in the open strip -1/2 < Re s < 1/2: %s ; = off-line zeros left of 1/2 and their mirrors: %s ; on-line zeros lie on the two boundary lines: %s"
    % ([complex(round(x.real, 4), round(x.imag, 4)) for x in bulk],
       sorted(map(lambda c: (round(c.real, 6), round(c.imag, 6)), bulk)) == sorted(map(lambda c: (round(c.real, 6), round(c.imag, 6)), pred)),
       all(abs(abs(x.real) - 0.5) < 1e-12 for x in system if x not in bulk and abs(abs(x.real) - 0.5) < 0.05)))

# 4d
okc = True
for _ in range(20):
    a_, b_ = rng.normal(size=2) + 1j * rng.normal(size=2)
    nrm = np.sqrt(abs(a_) ** 2 + abs(b_) ** 2); a_, b_ = a_ / nrm, b_ / nrm
    U = np.array([[a_, -np.conj(b_)], [b_, np.conj(a_)]])
    zr = rng.normal(size=2) + 1j * rng.normal(size=2)
    okc &= bool(np.allclose(sigma(U @ zr), U @ sigma(zr)))
say("4d sigma(Uz) = U sigma(z) for 20 random U in SU(2): %s (sigma is the quaternionic structure of the doublet)" % okc)

# 9
chi5 = [0, 1, 1j, -1j, -1]; chi5b = [mp.conj(c) for c in chi5]
kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
fDH = lambda s: (1 - 1j * kap) / 2 * mp.dirichlet(s, chi5) + (1 + 1j * kap) / 2 * mp.dirichlet(s, chi5b)
LamDH = lambda s: (mp.mpf(5) / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * fDH(s)   # chi(-1) = chi(4) = -1: odd, so Gamma((s+1)/2)
GDH = lambda s: LamDH(s) * LamDH(s + 1)
e1 = e2 = e3 = 0
for _ in range(6):
    s_ = mp.mpc(rng.uniform(-0.8, 1.8), rng.uniform(1, 40))
    e1 = max(e1, abs(LamDH(s_) - LamDH(1 - s_)) / abs(LamDH(s_)))
    e2 = max(e2, abs(LamDH(mp.conj(s_)) - mp.conj(LamDH(s_))) / abs(LamDH(s_)))
    e3 = max(e3, abs(GDH(-mp.conj(s_)) - mp.conj(GDH(s_))) / abs(GDH(s_)))
gvals = [GDH(mp.mpc(0, t)) for t in [0.5, 2, 10, 30, 85.7]]
say("9a Davenport-Heilbronn: max rel |Lambda_f(s) - Lambda_f(1-s)| = %.1e, |Lambda_f(conj s) - conj Lambda_f(s)| = %.1e, |G_f(-conj s) - conj G_f(s)| = %.1e"
    % (float(e1), float(e2), float(e3)))
say("9b G_f(it) at t = 0.5, 2, 10, 30, 85.7: max |Im|/|Re| = %.1e, all Re > 0: %s"
    % (float(max(abs(g.imag) / abs(g.real) for g in gvals)), all(g.real > 0 for g in gvals)))
zDH = mp.findroot(fDH, mp.mpc(0.808517, 85.699348))
sysDH = [zDH, 1 - mp.conj(zDH), zDH - 1, -mp.conj(zDH)]
say("9c DH off-line zero %s: |f| at its #-partner %.1e; the four points {z, 1 - conj z, z - 1, -conj z} are zeros of G_f: max |G_f| = %.1e; they are distinct (V4-orbit of size 4)"
    % (mp.nstr(zDH, 12), float(abs(fDH(1 - mp.conj(zDH)))), float(max(abs(GDH(w)) for w in sysDH))))

# 10
gam = [mp.im(mp.zetazero(n)) for n in range(1, 31)]
rhos = [mp.mpc(0.5, g) for g in gam] + [mp.mpc(0.5, -g) for g in gam]
def QA(alpha):
    fq = lambda s: mp.exp(1j * alpha * s) * mp.exp(1j * mp.pi * s) * mp.exp((s + mp.mpf(1) / 4) ** 2)
    tot = 0
    for r in rhos:     # on-line zeros: A(r) = r - 1 and A(r - 1) = r
        tot += fq(r) * mp.conj(fq(r - 1)) + fq(r - 1) * mp.conj(fq(r))
    return tot
qs = [(a_, QA(a_)) for a_ in [0, 1.5, 3.1416, 4.7]]
say("10 Q_A for f_alpha(s) = e^{i alpha s} e^{i pi s} e^{(s+1/4)^2}, first 30 zeros and conjugates (all on the line): %s ; max |Im|: %.1e ; both signs occur: %s"
    % ([(a_, mp.nstr(mp.re(q), 5)) for a_, q in qs], float(max(abs(mp.im(q)) for _, q in qs)),
       any(mp.re(q) > 0 for _, q in qs) and any(mp.re(q) < 0 for _, q in qs)))

# 11
gfun = lambda u: (1 + 0.5j) * mp.e ** (-(mp.log(u) - 0.3) ** 2) * u ** 0.2
Mel = lambda f, z: mp.quad(lambda u: f(u) * u ** (z - 1), [0, 1, mp.inf])
z = mp.mpc(0.37, 2.1)
g_haar = lambda u: mp.conj(gfun(1 / u))
g_leb = lambda u: mp.conj(gfun(1 / u)) / u
e_haar = abs(Mel(g_haar, z) - mp.conj(Mel(gfun, -mp.conj(z))))
e_leb = abs(Mel(g_leb, z) - mp.conj(Mel(gfun, 1 - mp.conj(z))))
e_tw = abs(Mel(lambda u: g_leb(u) * u, z) - Mel(g_haar, z))
say("11a Mellin shadows: Haar g*(u) = conj g(1/u) -> s -> -conj s (err %.1e); Lebesgue g*(u) = conj g(1/u)/u -> s -> 1 - conj s (err %.1e); they differ by the factor u (err %.1e)"
    % (float(e_haar), float(e_leb), float(e_tw)))
conv_h = mp.quad(lambda v: gfun(v) * g_haar(1 / v) / v, [0, 1, mp.inf])
nrm_h = mp.quad(lambda v: abs(gfun(v)) ** 2 / v, [0, 1, mp.inf])
conv_l = mp.quad(lambda v: gfun(v) * g_leb(1 / v) / v, [0, 1, mp.inf])
nrm_l = mp.quad(lambda v: abs(gfun(v)) ** 2, [0, 1, mp.inf])
say("11b annihilation into a norm: (g * g*_Haar)(1) = %s vs int|g|^2 du/u = %s ; (g * g*_Leb)(1) = %s vs int|g|^2 du = %s"
    % (mp.nstr(conv_h, 12), mp.nstr(nrm_h, 12), mp.nstr(conv_l, 12), mp.nstr(nrm_l, 12)))
thetas = []
for sv in [mp.mpc(0.5, 14.1347), mp.mpc(0.8085, 85.699), mp.mpc(0.2, -3)]:
    # theta(chi_s) = (chi_s^*)^{-1}: conj of u^{s-1/2} is u^{conj(s)-1/2}; its inverse is u^{-(conj(s)-1/2)} = u^{(1-conj s)-1/2}
    img = 1 - mp.conj(sv)
    uu = mp.mpf(2.7)
    lhs = 1 / mp.conj(uu ** (sv - 0.5)); rhs = uu ** (img - 0.5)
    thetas.append((mp.nstr(sv, 6), bool(mp.almosteq(lhs, rhs)), bool(mp.almosteq(img, sv)), mp.nstr(abs(uu ** (sv - 0.5)), 6)))
say("11c Cartan involution on characters u^{s-1/2}: (s, theta = s -> 1 - conj s verified, fixed by theta, |character at u = 2.7|): %s" % thetas)

# 12
def prim_chars(q):
    # all Dirichlet characters mod prime q via a primitive root
    g0 = next(r for r in range(2, q) if all(pow(r, (q - 1) // f, q) != 1 for f in range(2, q) if (q - 1) % f == 0 and all(f % d for d in range(2, f))))
    chars = []
    for e in range(1, q - 1):
        v = [mp.mpc(0)] * q
        for k in range(q - 1):
            v[pow(g0, k, q)] = mp.exp(2j * mp.pi * e * k / (q - 1))
        chars.append(v)
    return chars
def Wroot(chi, q):
    a = 0 if mp.almosteq(chi[q - 1], 1) else 1
    tau_ = mp.fsum(chi[x] * mp.exp(2j * mp.pi * x / q) for x in range(1, q))
    return tau_ / ((1j) ** a * mp.sqrt(q)), a
def LamC(sv, chi, q, a):
    return (mp.mpf(q) / mp.pi) ** ((sv + a) / 2) * mp.gamma((sv + a) / 2) * mp.dirichlet(sv, chi)
rows = []; allok = True
for q in [5, 7]:
    for chi in prim_chars(q):
        chib = [mp.conj(c) for c in chi]
        W, a = Wroot(chi, q); Wb, _ = Wroot(chib, q)
        sv = mp.mpc(0.31, 7.7)
        fe = abs(LamC(sv, chi, q, a) - W * LamC(1 - sv, chib, q, a)) / abs(LamC(sv, chi, q, a))
        real = all(abs(mp.im(c)) < 1e-25 for c in chi)
        rows.append((q, a, real, mp.nstr(W, 6), mp.nstr(abs(W), 12), mp.nstr(W * Wb, 12), float(fe)))
        allok &= bool(mp.almosteq(abs(W), 1) and mp.almosteq(W * Wb, 1) and fe < 1e-25 and ((not real) or mp.almosteq(W, 1)))
say("12 (q, parity a, real character, W, |W|, W(chi) W(conj chi), FE residual):")
for r in rows:
    say("    %s" % (r,))
say("12 all |W| = 1, all W W-bar = 1, all FE residuals < 1e-25, real characters have W = 1: %s" % allok)

# 13
Wchi, _ = Wroot(chi5, 5); Wchib, _ = Wroot(chi5b, 5)
cA, cB = (1 - 1j * kap) / 2, (1 + 1j * kap) / 2
say("13 DH = cA L(s, chi) + cB L(s, conj chi) with chi(2) = i mod 5: cB = conj cA: %s ; W(chi) = %s (phase %.2f degrees), W(conj chi) = %s ; the superposition has root number 1 (its functional equation f = X f(1-s) is checked in 9a)"
    % (bool(mp.almosteq(cB, mp.conj(cA))), mp.nstr(Wchi, 8), float(mp.degrees(mp.arg(Wchi))), mp.nstr(Wchib, 8)))

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "anomaly_two_line_model_checks_OUTPUT.txt"), "w") as fh:
    fh.write("\n".join(out) + "\n")
