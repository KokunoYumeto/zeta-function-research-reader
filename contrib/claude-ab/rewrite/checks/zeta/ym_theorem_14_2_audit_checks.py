#!/usr/bin/env python3
# Checks for 34_ (audit of the proof of Theorem 14.2 of the YM workbench file FABEL_LOW_MODE_TRANSFER.md).
# Written by a Claude subagent of claude-ab (Opus 5.5, max effort), 25 September 2026, and copied here unchanged
# apart from this header.
"""Independent audit checks for Theorem 14.2 of FABEL_LOW_MODE_TRANSFER.md.

Everything is recomputed from the definitions in that file (open box
{-L..L}^3, SU(2), H = kappa*sum E_e + b*sum(2-W_p), kappa=2g^2/a, b=1/(2g^2a)).
No numbers are taken from the workbench's own checkers.
Scope: finite algebra, the lattice/oscillator identities, a one-plaquette SU(2)
weak-coupling test, and the j-asymptotics.  The g->0 spectral convergence on the
full boxes (the analytic core) is NOT computable here and is not claimed.
"""
import itertools, math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.linalg import expm

RESULTS = []


def report(tag, title, ok, err, detail=""):
    RESULTS.append((tag, bool(ok)))
    print(f"[{tag}] {'PASS' if ok else 'FAIL'} | {title}")
    print(f"      error/margin = {err:.3e}" + (f" | {detail}" if detail else ""))


# ----------------------------------------------------------------------------
# open box complex, tree, T, G, C, R, O
# ----------------------------------------------------------------------------
def sh(n, i, d=1):
    t = list(n); t[i] += d; return tuple(t)


def build(L):
    verts = list(itertools.product(range(-L, L + 1), repeat=3))
    vidx = {v: k for k, v in enumerate(verts)}
    E = [(n, i) for n in verts for i in range(3) if n[i] <= L - 1]
    eidx = {e: k for k, e in enumerate(E)}
    F = [(n, i, j) for n in verts for i in range(3) for j in range(i + 1, 3)
         if n[i] <= L - 1 and n[j] <= L - 1]
    nV, nE, nF = len(verts), len(E), len(F)
    d0 = np.zeros((nE, nV))
    for k, (n, i) in enumerate(E):
        d0[k, vidx[sh(n, i)]] += 1.0
        d0[k, vidx[n]] -= 1.0
    d1 = np.zeros((nF, nE))
    for k, (n, i, j) in enumerate(F):          # W_p = tr U_i(n)U_j(n+e_i)U_i(n+e_j)^-1 U_j(n)^-1
        d1[k, eidx[(n, i)]] += 1.0
        d1[k, eidx[(sh(n, i), j)]] += 1.0
        d1[k, eidx[(sh(n, j), i)]] -= 1.0
        d1[k, eidx[(n, j)]] -= 1.0
    root = (-L, -L, -L)
    pedge = {}
    for v in verts:                              # parent: first coordinate (1,2,3) exceeding -L
        if v == root:
            continue
        k = next(i for i in range(3) if v[i] > -L)
        pedge[v] = (sh(v, k, -1), k)
    tree = set(pedge.values())
    P = {root: np.zeros(nE)}                     # additive tree integral p_v as a row vector
    for v in sorted(verts, key=sum):
        if v == root:
            continue
        pe = pedge[v]
        P[v] = P[pe[0]].copy(); P[v][eidx[pe]] += 1.0
    chords = [e for e in E if e not in tree]
    r = len(chords)
    T = np.zeros((r, nE))                        # (Tx)_c = p_s(x) + x_c - p_t(x)
    for c, (n, i) in enumerate(chords):
        T[c] = P[n] - P[sh(n, i)]
        T[c, eidx[(n, i)]] += 1.0
    iota = np.zeros((nE, r))
    for c, e in enumerate(chords):
        iota[eidx[e], c] = 1.0
    G = T @ T.T
    gev, gU = np.linalg.eigh(G)
    Gh = (gU * np.sqrt(gev)) @ gU.T
    Gmh = (gU / np.sqrt(gev)) @ gU.T
    C = d1 @ iota
    R = T.T @ Gmh
    K = Gh @ C.T @ C @ Gh
    K = 0.5 * (K + K.T)
    lam, O = np.linalg.eigh(K)
    return dict(L=L, N=2 * L + 1, verts=verts, E=E, F=F, eidx=eidx, nV=nV, nE=nE, nF=nF,
                d0=d0, d1=d1, T=T, iota=iota, r=r, G=G, Gh=Gh, C=C, R=R, lam=lam, O=O,
                sig=np.sqrt(np.clip(lam, 0, None)))


def oned(L):
    N = 2 * L + 1
    n = np.arange(-L, L + 1); ne = np.arange(-L, L)
    v0 = np.ones(N) / np.sqrt(N)
    v1 = -np.sqrt(2 / N) * np.sin(np.pi * n / N)
    w1 = -np.sqrt(2 / N) * np.cos(np.pi * (ne + 0.5) / N)
    return v0, v1, w1


def modes_117(cx):
    """V_1,V_2,V_3 of (117); index i (0-based) = normal direction."""
    L = cx['L']; v0, v1, w1 = oned(L)
    Vs = []
    for (i, p, q) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        V = np.zeros(cx['nE'])
        for k, (n, d) in enumerate(cx['E']):
            if d == p:
                V[k] = v0[n[i] + L] * w1[n[p] + L] * v1[n[q] + L] / np.sqrt(2)
            elif d == q:
                V[k] = -v0[n[i] + L] * v1[n[p] + L] * w1[n[q] + L] / np.sqrt(2)
        Vs.append(V)
    return np.array(Vs).T          # nE x 3


def consts(L):
    N = 2 * L + 1; h = math.pi / (2 * N); s = 2 * math.sin(h); sig = math.sqrt(2) * s
    delta = (1 - 1 / math.tan(h) ** 2) / 8
    m2 = math.cos(h) ** 2 / (2 * N ** 2 * math.sin(h) ** 4)
    return N, h, s, sig, delta, m2


def midpoints(cx):
    return np.array([np.array(n, float) + 0.5 * np.eye(3)[i] for (n, i) in cx['E']])


def f_edges(cx, S):
    m = midpoints(cx)
    return np.einsum('ei,ij,ej->e', m, S, m)


def f_faces(cx, fe):
    return 0.25 * np.abs(cx['d1']) @ fe


def rand_sym(rng):
    X = rng.normal(size=(3, 3)); return 0.5 * (X + X.T)


rng = np.random.default_rng(20260925)
BOX = {L: build(L) for L in (2, 3, 4)}

# ----------------------------------------------------------------------------
# Y1  cochain / tree identities
# ----------------------------------------------------------------------------
errs, info = [], []
ok = True
for L, cx in BOX.items():
    T, d0, d1, io, R, C, Gh = cx['T'], cx['d0'], cx['d1'], cx['iota'], cx['R'], cx['C'], cx['Gh']
    r = cx['r']
    e = [np.abs(T @ io - np.eye(r)).max(), np.abs(T @ d0).max(), np.abs(d1 - C @ T).max(),
         np.abs(d1 @ d0).max(), np.abs(R.T @ R - np.eye(r)).max(), np.abs(d0.T @ R).max(),
         np.abs(d1 @ R - C @ Gh).max()]
    errs += e
    rk_T = np.linalg.matrix_rank(T); rk_d1 = np.linalg.matrix_rank(d1); rk_d0 = np.linalg.matrix_rank(d0)
    ok &= (r == 4 * L * L * (4 * L + 3) == cx['nE'] - cx['nV'] + 1 and rk_T == r and rk_d1 == r
           and rk_d0 == cx['nV'] - 1 and cx['nE'] == 3 * 2 * L * (2 * L + 1) ** 2
           and cx['nF'] == 3 * (2 * L) ** 2 * (2 * L + 1))
    info.append(f"L={L}: |V|={cx['nV']} |E|={cx['nE']} |F|={cx['nF']} r={r}=4L^2(4L+3)")
report("Y1", "T iota=I, T d0=0, d1=CT, ker T=ker d1=im d0 (ranks), R^TR=I, d0^T R=0, d1R=CG^{1/2}",
       ok and max(errs) < 1e-9, max(errs), "; ".join(info))

# ----------------------------------------------------------------------------
# Y2  transverse spectrum = sum_i 4 sin^2(pi j_i/2N), multiplicity k-1
# ----------------------------------------------------------------------------
def formula_spectrum(N):
    s1 = [4 * math.sin(math.pi * j / (2 * N)) ** 2 for j in range(N)]
    vals = []
    for jj in itertools.product(range(N), repeat=3):
        k = sum(1 for x in jj if x > 0)
        if k >= 2:
            vals += [s1[jj[0]] + s1[jj[1]] + s1[jj[2]]] * (k - 1)
    return np.sort(np.array(vals))


errs, ok, info = [], True, []
for L, cx in BOX.items():
    N, h, s, sig, _, _ = consts(L)
    fs = formula_spectrum(N)
    lam = np.sort(cx['lam'])
    ok &= len(fs) == len(lam)
    errs.append(np.abs(fs - lam).max())
    low = lam[:3]; nxt = lam[3:5]; third = lam[5]
    errs += [np.abs(low - 2 * s * s).max(), np.abs(nxt - 3 * s * s).max()]
    ok &= lam[2] < 3 * s * s - 1e-9 and third >= (1 + 4 * math.cos(h) ** 2) * s * s - 1e-9
    info.append(f"L={L}: lowest 3 = 2s^2, next 2 = 3s^2, 6th/s^2={third/(s*s):.4f}>=1+4cos^2h={1+4*math.cos(h)**2:.4f}")
report("Y2", "full transverse curl spectrum equals the tensor formula; 3 lowest modes sigma=sqrt2 s, next sqrt3 s",
       ok and max(errs) < 1e-9, max(errs), "; ".join(info))

# ----------------------------------------------------------------------------
# Y3  1D functions and the three modes (117)
# ----------------------------------------------------------------------------
errs, ok, signs = [], True, []
for L in range(2, 41):
    v0, v1, w1 = oned(L); N, h, s, sig, _, _ = consts(L)
    dv1 = v1[1:] - v1[:-1]
    dTw1 = np.concatenate([[0.0], w1]) - np.concatenate([w1, [0.0]])
    errs += [abs(v0 @ v0 - 1), abs(v1 @ v1 - 1), abs(w1 @ w1 - 1), abs(v0 @ v1),
             np.abs(dv1 - s * w1).max(), np.abs(dTw1 - s * v1).max()]
for L, cx in BOX.items():
    N, h, s, sig, _, _ = consts(L); v0, v1, w1 = oned(L)
    V = modes_117(cx); d1 = cx['d1']
    errs += [np.abs(V.T @ V - np.eye(3)).max(), np.abs(cx['d0'].T @ V).max(),
             np.abs(d1.T @ d1 @ V - sig ** 2 * V).max()]
    for col, (i, p, q) in enumerate([(0, 1, 2), (1, 2, 0), (2, 0, 1)]):
        cv = d1 @ V[:, col]
        pl = (min(p, q), max(p, q))
        target = np.array([sig * v0[n[i] + L] * w1[n[p] + L] * w1[n[q] + L] if (a, b) == pl else 0.0
                           for (n, a, b) in cx['F']])
        sg = np.sign(cv @ target)
        errs += [np.abs(cv - sg * target).max(), abs(cv @ cv - sig ** 2)]
        if L == 2:
            signs.append(f"V{i+1}:{'-' if sg < 0 else '+'}")
    # least-squares check that span(V_i) is the whole lowest eigenspace
    Vlow = cx['R'] @ cx['O'][:, :3]
    errs.append(np.abs(Vlow @ Vlow.T - V @ V.T).max())
report("Y3", "(117): unit norms, dv1=s w1, d^Tw1=s v1, <V_i,V_j>=delta, div V_i=0, curl on one plane, d1^Td1V_i=sigma^2 V_i",
       max(errs) < 1e-9, max(errs), "curl signs on own plane: " + ",".join(signs) + " (file: V1 has '-')")

# ----------------------------------------------------------------------------
# Y4  the exact endpoint sums (121) and the intermediate Dirichlet-kernel identities
# ----------------------------------------------------------------------------
mp.mp.dps = 40
errs = []
for L in list(range(2, 60)) + [100, 257, 1000]:
    N = 2 * L + 1; h = mp.pi / (2 * N)
    ns = range(-L, L + 1); nes = range(-L, L)
    A = sum(mp.mpf(n) ** 2 * (2 / mp.mpf(N)) * mp.sin(mp.pi * n / N) ** 2 for n in ns)
    B = sum((n + mp.mpf(1) / 2) ** 2 * (2 / mp.mpf(N)) * mp.cos(mp.pi * (n + mp.mpf(1) / 2) / N) ** 2 for n in nes)
    M = sum(mp.mpf(n) * (-mp.sqrt(2 / mp.mpf(N)) * mp.sin(mp.pi * n / N)) / mp.sqrt(N) for n in ns)
    t = 2 * mp.pi / N
    DN2 = -sum(mp.mpf(n) ** 2 * mp.cos(n * t) for n in ns)
    DN12 = -sum((n + mp.mpf(1) / 2) ** 2 * mp.cos((n + mp.mpf(1) / 2) * t) for n in nes)
    DN1p = -sum(mp.mpf(n) * mp.sin(n * mp.pi / N) for n in ns)
    tt = mp.mpf('0.7310')
    DNt = mp.sin(N * tt / 2) / mp.sin(tt / 2)
    DN1t = sum(mp.e ** (1j * (n + mp.mpf(1) / 2) * tt) for n in nes)
    errs += [abs((B - A) + mp.cot(h) ** 2 / 4) / (mp.cot(h) ** 2),
             abs(M + mp.sqrt(2) * mp.cos(h) / (2 * N * mp.sin(h) ** 2)) / abs(M),
             abs(M ** 2 - mp.cos(h) ** 2 / (2 * N ** 2 * mp.sin(h) ** 4)) / M ** 2,
             abs((B - A) - (-mp.mpf(N) * (N - 1) / 4 - DN2 - DN12) / N) / mp.cot(h) ** 2,
             abs(DN2 + DN12 - (N / (4 * mp.sin(h) ** 2) - mp.mpf(N) ** 2 / 4)) / N ** 2,
             abs(DN1p + mp.cos(h) / (2 * mp.sin(h) ** 2)) / N,
             abs(DN1t - (DNt * mp.cos(tt / 2) - mp.cos(N * tt / 2))),
             abs(((B - A) / 2 + mp.mpf(1) / 8) - (1 - mp.cot(h) ** 2) / 8) / mp.cot(h) ** 2]
report("Y4", "(121): B-A=-cot^2h/4, M=-sqrt2 cos h/(2N sin^2h), M^2=m_L^2, D''_N+D''_{N-1} identity, D'_N(pi/N)",
       max(errs) < mp.mpf('1e-30'), float(max(errs)), "L=2..59,100,257,1000 at 40 digits (relative errors)")

# ----------------------------------------------------------------------------
# Y5  face average f_p = c^T S c + (S_pp+S_qq)/8
# ----------------------------------------------------------------------------
errs = []
for L in (2, 3):
    cx = BOX[L]
    for _ in range(3):
        S = rand_sym(rng); fe = f_edges(cx, S); fp = f_faces(cx, fe)
        tgt = np.array([(np.array(n, float) + 0.5 * (np.eye(3)[i] + np.eye(3)[j])) @ S @
                        (np.array(n, float) + 0.5 * (np.eye(3)[i] + np.eye(3)[j])) + (S[i, i] + S[j, j]) / 8
                        for (n, i, j) in cx['F']])
        errs.append(np.abs(fp - tgt).max())
report("Y5", "face weight f_p=(1/4)sum_{dp} f_e equals c^TSc+(S_pp+S_qq)/8 on every face", max(errs) < 1e-10, max(errs))

# ----------------------------------------------------------------------------
# Y6  Theorem 14.1 block (119): direct, and basis-free via the numerically diagonalised O
# ----------------------------------------------------------------------------
def Rf_full(cx, fe):
    R, O, d1, lam = cx['R'], cx['O'], cx['d1'], cx['lam']
    V = R @ O
    fp = f_faces(cx, fe)
    Af = V.T @ (fe[:, None] * V)
    Mf = (d1 @ V).T @ (fp[:, None] * (d1 @ V))
    sg = np.sqrt(lam)
    return Mf / np.sqrt(np.outer(sg, sg)) - np.sqrt(np.outer(sg, sg)) * Af, Af, Mf


def R119(L, S):
    N, h, s, sig, dl, m2 = consts(L)
    B = np.zeros((3, 3)); tr = np.trace(S)
    for i in range(3):
        for j in range(3):
            B[i, j] = sig * dl * (tr - S[i, i]) if i == j else sig * m2 * S[i, j]
    return B


errs, info = [], []
for L, cx in BOX.items():
    N, h, s, sig, dl, m2 = consts(L)
    V = modes_117(cx); d1 = cx['d1']
    for _ in range(3):
        S = rand_sym(rng); fe = f_edges(cx, S); fp = f_faces(cx, fe)
        Amin = V.T @ (fe[:, None] * V); Mmin = (d1 @ V).T @ (fp[:, None] * (d1 @ V))
        Rdir = Mmin / sig - sig * Amin
        Rform = R119(L, S)
        scale = np.abs(Rform).max()
        errs.append(np.abs(Rdir - Rform).max() / scale)
        Rf, _, _ = Rf_full(cx, fe)
        blk = Rf[:3, :3]
        errs.append(np.abs(np.sort(np.linalg.eigvalsh(blk)) - np.sort(np.linalg.eigvalsh(Rform))).max() / scale)
        errs.append(abs(np.trace(blk @ blk) - np.trace(Rform @ Rform)) / scale ** 2)
    Rc, _, _ = Rf_full(cx, np.ones(cx['nE']) * 1.7)
    errs.append(np.abs(Rc).max())
    info.append(f"L={L}: delta_L={dl:.4f}, m_L^2={m2:.4f}")
report("Y6", "Thm 14.1 (119): lowest block of R_f equals sigma*delta_L(trS-S_ii) / sigma*m_L^2 S_ij; constant f gives R_f=0",
       max(errs) < 1e-8, max(errs), "; ".join(info))

# ----------------------------------------------------------------------------
# Y7  injectivity: delta_L<0, m_L^2/|delta_L| formula > 16/pi^2, explicit inverse
# ----------------------------------------------------------------------------
errs, ok = [], True
for L in list(range(2, 200)) + [10 ** 3, 10 ** 4, 10 ** 6]:
    N, h, s, sig, dl, m2 = consts(L)
    ratio = m2 / abs(dl)
    alt = 4 * math.cos(h) ** 2 / (N ** 2 * math.sin(h) ** 2 * math.cos(2 * h))
    errs.append(abs(ratio - alt) / alt)
    ok &= dl < 0 and ratio > 16 / math.pi ** 2 > 1 and h <= math.pi / 10
for L in (2, 5, 17):
    N, h, s, sig, dl, m2 = consts(L)
    S = rand_sym(rng); Bm = R119(L, S) / sig; trS = np.trace(Bm) / (2 * dl)
    Srec = np.array([[trS - Bm[i, i] / dl if i == j else Bm[i, j] / m2 for j in range(3)] for i in range(3)])
    errs.append(np.abs(Srec - S).max())
report("Y7", "delta_L<0<m_L^2, m_L^2/|delta_L|=4cos^2h/(N^2 sin^2h cos2h)>16/pi^2, explicit inverse S(R^min)",
       ok and max(errs) < 1e-9, max(errs), "L=2..199,1e3,1e4,1e6")

# ----------------------------------------------------------------------------
# Y8  (120) band mass and (124): tr R_f^2 <= 432 r L^4 |S|^2, rho >= sigma^2 delta^2/(432 r L^4)
# ----------------------------------------------------------------------------
errs, ok, info = [], True, []
a = 0.37
for L, cx in BOX.items():
    N, h, s, sig, dl, m2 = consts(L); r = cx['r']
    Vt = cx['R'] @ cx['O']; lam = cx['lam']; Sg = np.sqrt(lam)
    Y = cx['d1'] @ Vt / Sg
    errs.append(np.abs(Y.T @ Y - np.eye(r)).max())
    rhos = []
    for S in [rand_sym(rng), np.diag([1.0, 2.0, 3.0]), np.eye(3)]:
        fe = f_edges(cx, S); fp = f_faces(cx, fe)
        Rf, _, _ = Rf_full(cx, fe)
        Rfact = np.sqrt(Sg)[:, None] * (Y.T @ (fp[:, None] * Y) - Vt.T @ (fe[:, None] * Vt)) * np.sqrt(Sg)[None, :]
        errs.append(np.abs(Rf - Rfact).max() / np.abs(Rf).max())
        dform = 3 * sig ** 2 / (8 * a ** 2) * (dl ** 2 * sum((np.trace(S) - S[i, i]) ** 2 for i in range(3))
                                             + 2 * m2 ** 2 * sum(S[i, j] ** 2 for i in range(3) for j in range(i + 1, 3)))
        dband = 3 / (8 * a ** 2) * np.sum(Rf[:3, :3] ** 2)
        errs.append(abs(dband - dform) / dform)
        trR2 = np.trace(Rf @ Rf); opS = np.abs(np.linalg.eigvalsh(S)).max()
        rho = np.sum(Rf[:3, :3] ** 2) / trR2
        lb = sig ** 2 * dl ** 2 / (432 * r * L ** 4)
        ok &= trR2 <= 432 * r * L ** 4 * opS ** 2 and 1 >= rho >= lb
        rhos.append(rho)
    info.append(f"L={L}: rho in [{min(rhos):.3e},{max(rhos):.3e}] vs bound {lb:.2e}")
report("Y8", "(120) = (3/8a^2)*sum_low R^2; R_f = Sigma^{1/2}[Y^TF_pY - V^TF_eV]Sigma^{1/2}; (124) both inequalities",
       ok and max(errs) < 1e-8, max(errs), "; ".join(info))

# ----------------------------------------------------------------------------
# Y9  oscillator coefficient (115) and colour-contraction norms (116)
# ----------------------------------------------------------------------------
z1, z2, aa = sp.symbols('z1 z2 a', positive=True)
s1, s2 = sp.symbols('s1 s2', positive=True)
A11, A12, A22, M11, M12, M22 = sp.symbols('A11 A12 A22 M11 M12 M22', real=True)
zs, ss = [z1, z2], [s1, s2]
Am = sp.Matrix([[A11, A12], [A12, A22]]); Mm = sp.Matrix([[M11, M12], [M12, M22]])
Phi = sp.exp(-(s1 * z1 ** 2 + s2 * z2 ** 2) / 8)            # ground state of (1/a)(-2d^2 + s^2 z^2/8)
Hosc = lambda f: sum((-2 * sp.diff(f, zz, 2) + sg ** 2 * zz ** 2 / 8 * f) / aa for zz, sg in zip(zs, ss))
e_ground = sp.simplify(Hosc(Phi) / Phi)
Fx = (-(2 / aa) * sum(Am[i, j] * sp.diff(Phi, zs[i], zs[j]) for i in range(2) for j in range(2))
      + sum(Mm[i, j] * zs[i] * zs[j] for i in range(2) for j in range(2)) * Phi / (8 * aa))
Pz = sp.expand(sp.simplify(Fx / Phi))
poly = sp.Poly(Pz, z1, z2)
mean = poly.coeff_monomial(1) + poly.coeff_monomial(z1 ** 2) * 2 / s1 + poly.coeff_monomial(z2 ** 2) * 2 / s2
Pc = sp.expand(Pz - mean)
adag = lambda f, i: sp.Rational(1, 2) * (sp.sqrt(ss[i] / 2) * zs[i] * f - 2 * sp.sqrt(2) / sp.sqrt(ss[i]) * sp.diff(f, zs[i]))
Sh = sp.diag(sp.sqrt(s1), sp.sqrt(s2)); Shi = sp.diag(1 / sp.sqrt(s1), 1 / sp.sqrt(s2))
Rm = Shi * Mm * Shi - Sh * Am * Sh
Gx = sum(Rm[i, j] * adag(adag(Phi, j), i) for i in range(2) for j in range(2)) / (4 * aa)
diff115 = sp.simplify(sp.expand(sp.simplify(Gx / Phi)) - Pc)
ok_sym = diff115 == 0 and sp.simplify(e_ground - (s1 + s2) / (2 * aa)) == 0


# small Fock algebra: 3 colours x m modes
def create(state, mode):
    out = {}
    for occ, c in state.items():
        o = list(occ); o[mode] += 1
        out[tuple(o)] = out.get(tuple(o), 0) + c * math.sqrt(o[mode])
    return out


def add(x, y, cy=1.0):
    out = dict(x)
    for k, v in y.items():
        out[k] = out.get(k, 0) + cy * v
    return out


def inner(x, y):
    return sum(v * y.get(k, 0) for k, v in x.items())


m_modes = 4
idx = lambda nu, al: 3 * nu + al
vac = {tuple([0] * (3 * m_modes)): 1.0}
diagc = {}
for al in range(3):
    diagc = add(diagc, create(create(vac, idx(0, al)), idx(0, al)))
offc = {}
for al in range(3):
    offc = add(offc, create(create(vac, idx(0, al)), idx(1, al)))
off2 = {}
for al in range(3):
    off2 = add(off2, create(create(vac, idx(0, al)), idx(2, al)))
errs = [abs(inner(diagc, diagc) - 6), abs(inner(offc, offc) - 3), abs(inner(diagc, offc)), abs(inner(offc, off2))]
# (116) masses and first moment for random R, sigma
sgm = np.sort(rng.uniform(0.3, 2.0, m_modes))
X = rng.normal(size=(m_modes, m_modes)); Rr = 0.5 * (X + X.T); aF = 0.61
Vf = {}
for nu in range(m_modes):
    for eta in range(m_modes):
        for al in range(3):
            Vf = add(Vf, create(create(vac, idx(eta, al)), idx(nu, al)), Rr[nu, eta] / (4 * aF))
mass = inner(Vf, Vf)
energy = sum(v * v * sum(o[idx(nu, al)] * sgm[nu] for nu in range(m_modes) for al in range(3)) / aF
             for o, v in Vf.items())
errs += [abs(mass - 3 * np.trace(Rr @ Rr) / (8 * aF ** 2)) / mass,
         abs(energy - 3 * np.trace(np.diag(sgm) @ Rr @ Rr) / (4 * aF ** 3)) / energy]
report("Y9", "(115) centred creation coefficient (symbolic, both terms); colour norms 6,3; (116) mass 3trR^2/8a^2, moment 3tr(Sigma R^2)/4a^3",
       ok_sym and max(errs) < 1e-12, max(errs), f"symbolic residual={diff115}, per-mode ground energy=sigma/(2a) verified")

# ----------------------------------------------------------------------------
# Y10 physical band isolation from the actual transverse spectra
# ----------------------------------------------------------------------------
errs, ok, info = [], True, []
for L, cx in BOX.items():
    N, h, s, sig, dl, m2 = consts(L)
    sg = np.sort(cx['sig'])
    two = np.sort([sg[i] + sg[j] for i in range(len(sg)) for j in range(i, min(len(sg), 12))])
    Delta = 2 * sg[0]
    mult = int(np.sum(np.abs(two - Delta) < 1e-9))
    nxt = two[mult]
    three = sg[0] + sg[1] + sg[2]            # epsilon-contraction needs 3 distinct modes
    ok &= mult == 6 and nxt / Delta > 1.1 and three / Delta >= 1.5 - 1e-12
    errs.append(abs(Delta - 2 * sig))
    info.append(f"L={L}: mult={mult}, next/Delta={nxt/Delta:.5f}, 3-quanta/Delta={three/Delta:.3f}")
ratio = (math.sqrt(2) + math.sqrt(3)) / (2 * math.sqrt(2))
ok &= ratio > 1.1
report("Y10", "singlet 2-quanta levels: Delta=2sigma/a with multiplicity 6; next=(sqrt2+sqrt3)s/a>1.1 Delta; >=3 quanta >=1.5 Delta",
       ok and max(errs) < 1e-12, max(errs), "; ".join(info) + f"; (sqrt2+sqrt3)/(2sqrt2)={ratio:.5f}")

# ----------------------------------------------------------------------------
# Y11 plaquette derivative identity and sum_{e,a}|X_{e,a}W|^2 <= 16 W
# ----------------------------------------------------------------------------
sig_p = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
Tg = [-0.5j * sp_ for sp_ in sig_p]


def su2(qv):
    qv = qv / np.linalg.norm(qv)
    return qv[0] * np.eye(2) + 1j * (qv[1] * sig_p[0] + qv[2] * sig_p[1] + qv[3] * sig_p[2])


errs = []
for _ in range(200):
    U = su2(rng.normal(size=4)); w = 2 - np.trace(U).real
    xs = [-np.trace(Tg[al] @ U) for al in range(3)]     # X_a (2 - tr U), left translation e^{tT_a}U
    errs.append(abs(sum(abs(x) ** 2 for x in xs) - (w - w * w / 4)))
    # finite-difference confirmation of the derivative convention
    t = 1e-5
    fd = [-(np.trace(expm(t * Tg[al]) @ U) - np.trace(expm(-t * Tg[al]) @ U)).real / (2 * t) for al in range(3)]
    errs.append(max(abs(fd[al] - xs[al].real) for al in range(3)))   # central difference, error ~1e-10
cx = BOX[2]
worst = 0.0
for trial in range(6):
    eps = [3.0, 1.0, 0.3, 0.1, 0.03, 0.01][trial]
    Ul = {e: su2(np.concatenate([[1.0], eps * rng.normal(size=3)])) if eps < 3 else su2(rng.normal(size=4)) for e in cx['E']}
    XW = {e: np.zeros(3) for e in cx['E']}
    Wtot = 0.0
    for (n, i, j) in cx['F']:
        e1, e2, e3, e4 = (n, i), (sh(n, i), j), (sh(n, j), i), (n, j)
        U1, U2, U3, U4 = Ul[e1], Ul[e2], Ul[e3], Ul[e4]
        Up = U1 @ U2 @ U3.conj().T @ U4.conj().T
        Wtot += 2 - np.trace(Up).real
        for al in range(3):
            T_ = Tg[al]
            XW[e1][al] -= np.trace(T_ @ Up).real
            XW[e2][al] -= np.trace(U1 @ T_ @ U2 @ U3.conj().T @ U4.conj().T).real
            XW[e3][al] -= -np.trace(U1 @ U2 @ U3.conj().T @ T_ @ U4.conj().T).real
            XW[e4][al] -= -np.trace(Up @ T_).real
    lhs = sum(np.sum(v ** 2) for v in XW.values())
    worst = max(worst, lhs / (16 * Wtot))
report("Y11", "sum_a|X_a w_p|^2 = w_p - w_p^2/4 (200 random U); sum_{e,a}|X_{e,a}W|^2 <= 16W on L=2 configurations",
       max(errs) < 1e-8 and worst <= 1.0, max(errs), f"max ratio (sum|XW|^2)/(16W) over 6 configs = {worst:.4f}")

# ----------------------------------------------------------------------------
# Y12 one-plaquette SU(2) Hamiltonian (r=1): weak-coupling gap -> 2sigma/a, sigma=sqrt(G)|C|=2
# ----------------------------------------------------------------------------
def plaquette(g, a=1.0, K=700):
    kap, b = 2 * g * g / a, 1 / (2 * g * g * a)
    js = np.arange(K) / 2.0
    H = np.diag(4 * kap * js * (js + 1) + 2 * b) - b * (np.eye(K, k=1) + np.eye(K, k=-1))
    ev, vec = np.linalg.eigh(H)
    return ev, vec, kap, b


phi = (np.arange(40000) + 0.5) * np.pi / 40000
lines, errs, ok = [], [], True
for g in [1.0, 0.5, 0.2, 0.1, 0.05, 0.03]:
    ev, vec, kap, b = plaquette(g)
    gap, E0 = ev[1] - ev[0], ev[0]
    c = vec[:, 0] * np.sign(vec[0, 0])
    amp = sum(c[k] * np.sin((k + 1) * phi) for k in range(len(c)) if abs(c[k]) > 1e-18)
    dens = (2 / np.pi) * amp ** 2 * (np.pi / len(phi))          # psi^2 * Haar class density
    Wp = 2 - 2 * np.cos(phi)
    mom = [np.sum(dens * Wp ** k) for k in range(6)]
    for k in range(1, 5):
        ok &= b * mom[k + 1] <= E0 * mom[k] + 4 * kap * k * k * mom[k - 1] + 1e-9 * max(1, b * mom[k + 1])
    lines.append(f"g={g}: gap={gap:.4f}, E0={E0:.4f}, <W/g^2>={mom[1]/g**2:.4f}")
    if g <= 0.05:
        errs += [abs(gap - 4.0) / 4.0]
ok &= abs(mom[0] - 1) < 1e-8
report("Y12", "single plaquette (a=1): gap -> 2sigma/a = 4, E0 -> 3sigma/(2a) = 3, <W/g^2> -> 3; moment inequality k=1..4",
       ok and max(errs) < 0.05, max(errs), "; ".join(lines))

# ----------------------------------------------------------------------------
# Y13 material tensor inputs (102), S_*, the two sums, C_*
# ----------------------------------------------------------------------------
x, y, w, z = sp.symbols('x y w z', positive=True)
Fp = sp.Matrix([(1 + x * y) ** 3 * w + y ** 2 * (1 + x * y) * (4 + 3 * x * y),
                y + 3 * x * (1 + x * y) ** 2 * w + 3 * x * y ** 2 * (4 + 3 * x * y),
                2 * x - 3 * x ** 2 * y - x ** 3 * w])
J = Fp.jacobian([x, y, w])
J0 = J.subs({x: 1, y: sp.Rational(-3, 2), w: sp.Rational(13, 2)})
Jg = J.subs({x: 1 / z, y: -sp.Rational(3, 2) * z, w: sp.Rational(13, 2) * z ** 2})
tau = (1 - z ** 2) / 8
Bt = sp.eye(3); Bt[1, 2] = 6 * tau
Cfac = sp.simplify(J0.inv() * Bt.inv() * Jg)
C102 = sp.Matrix([[(17 - 9 * z ** 3) / 8, (3 - 3 * z ** 3) / (4 * z ** 2), (1 - z ** 3) / (4 * z ** 3)],
                  [(51 - 24 * z ** 2 - 27 * z ** 3) / 16, (9 + 8 * z ** 2 - 9 * z ** 3) / (8 * z ** 2), (3 - 3 * z ** 3) / (8 * z ** 3)],
                  [(-153 + 36 * z ** 2 + 117 * z ** 3) / 8, (-27 - 12 * z ** 2 + 39 * z ** 3) / (4 * z ** 2), (-9 + 13 * z ** 3) / (4 * z ** 3)]])
eta = sp.Matrix([sp.Rational(1, 4), sp.Rational(3, 8), sp.Rational(-9, 4)])
Sstar = eta * eta.T
K6 = sp.simplify(z ** 6 * C102 * C102.T)
lim0 = K6.subs(z, 0)
lin = sp.simplify(sp.diff(K6, z).subs(z, 0))
sum1 = sum((Sstar.trace() - Sstar[i, i]) ** 2 for i in range(3))
sum2 = sum(Sstar[i, j] ** 2 for i in range(3) for j in range(i + 1, 3))
Cst = sp.nsimplify(7500) / sp.pi ** 2 * sum1 + sp.nsimplify(3840000) / sp.pi ** 6 * sum2
Cst_file = sp.Rational(204976875, 512) / sp.pi ** 2 + sp.Rational(3982500) / sp.pi ** 6
okm = (sp.simplify(Cfac - C102) == sp.zeros(3, 3) and sp.simplify(C102.det() - 1) == 0
       and sp.simplify(lim0 - Sstar) == sp.zeros(3, 3) and lin == sp.zeros(3, 3)
       and sum1 == sp.Rational(109321, 2048) and sum2 == sp.Rational(531, 512)
       and sp.simplify(Cst - Cst_file) == 0)
report("Y13", "(102)=J0^-1 B^-1 J_gamma, det C=1, z^6K -> S_*=eta eta^T with zero O(z) term, sums 109321/2048 & 531/512, C_* closed form",
       okm, 0.0, f"C_* = {float(Cst_file):.6f}")

# ----------------------------------------------------------------------------
# Y14 asymptotics along L_j=j^2, a_j=1/(100j), z_j=1/j, and the physical scale
# ----------------------------------------------------------------------------
mp.mp.dps = 60
Cfun = sp.lambdify(z, C102, 'mpmath')
Cst_num = mp.mpf(204976875) / (512 * mp.pi ** 2) + mp.mpf(3982500) / mp.pi ** 6
lines, rel = [], {}
for jj in [2, 10, 100, 1000, 10000]:
    jm = mp.mpf(jj); Lj = jj * jj; Nj = 2 * Lj + 1; aj = 1 / (100 * jm)
    hj = mp.pi / (2 * Nj); sj = 2 * mp.sin(hj); sgj = mp.sqrt(2) * sj
    dl = (1 - mp.cot(hj) ** 2) / 8; m2 = mp.cos(hj) ** 2 / (2 * Nj ** 2 * mp.sin(hj) ** 4)
    Cm = mp.matrix(Cfun(1 / jm)); Sm = Cm * Cm.T
    trS = Sm[0, 0] + Sm[1, 1] + Sm[2, 2]
    dj = 3 * sgj ** 2 / (8 * aj ** 2) * (dl ** 2 * sum((trS - Sm[i, i]) ** 2 for i in range(3))
                                        + 2 * m2 ** 2 * sum(Sm[i, k] ** 2 for i in range(3) for k in range(i + 1, 3)))
    Dj = 2 * sgj / aj
    rj = 4 * Lj ** 2 * (4 * Lj + 3)
    fb = (jm - 1) / (jm + 1) * sgj ** 2 * dl ** 2 / (432 * rj * mp.mpf(Lj) ** 4)
    rel[jj] = (float(dj / jm ** 18 / Cst_num - 1), float(jm * Dj / (100 * mp.sqrt(2) * mp.pi) - 1),
               float(fb / (jm ** -10 / (3456 * mp.pi ** 2)) - 1))
    box_half = Lj * aj; box_side = 2 * Lj * aj; box_N = Nj * aj
    qlo, qhi = Dj * (1 - 1 / (10 * jm)), Dj * (1 + 1 / (10 * jm))
    lines.append(f"j={jj}: L_ja_j={float(box_half):.4g} (=j/100), 2L_ja_j={float(box_side):.4g}, "
                 f"Q_j in ({float(qlo):.6g},{float(qhi):.6g}), Delta_j*L_ja_j/(sqrt2 pi)={float(Dj*box_half/(mp.sqrt(2)*mp.pi)):.8f}, "
                 f"Delta_j/(2pi/(L_ja_j))={float(Dj/(2*mp.pi/box_half)):.8f}, Delta_j/(2sqrt2 pi/(N_ja_j))={float(Dj/(2*mp.sqrt(2)*mp.pi/box_N)):.10f}, "
                 f"rel.err: d_j/(j^18C_*)-1={rel[jj][0]:.2e}, jDelta_j/(100sqrt2pi)-1={rel[jj][1]:.2e}, fraction bound/(j^-10/3456pi^2)-1={rel[jj][2]:.2e}")
# d_j and j*Delta_j converge at rate O(j^-2); the fraction bound carries (j-1)/(j+1)=1-2/j+..., rate O(j^-1)
ok = abs(rel[10000][0]) < 1e-6 and abs(rel[10000][1]) < 1e-6 and abs(rel[10000][2] * 10000 + 2) < 1e-2
ok &= all(abs(rel[j2][k]) > abs(rel[j3][k]) for k in range(3) for j2, j3 in [(10, 100), (100, 1000), (1000, 10000)])
report("Y14", "j^-18 d_j -> C_*, j*Delta_j -> 100 sqrt2 pi (both O(j^-2)), fraction bound ~ j^-10/(3456 pi^2) (O(1/j)); physical scale",
       ok, max(abs(rel[10000][0]), abs(rel[10000][1])),
       f"j*(fraction-bound rel.err) at j=1e4: {rel[10000][2]*10000:.4f} (expected -2)\n      " + "\n      ".join(lines))

print()
npass = sum(1 for _, o in RESULTS if o)
print(f"SUMMARY: {npass}/{len(RESULTS)} PASS")
