# Checks for 30_ (audit of GDE0-GDE13 with GDR0-GDR5, and ABH0-ABH8 with AHR0-AHR9,
# in the programme's working folder quantum_tau_programme_bridge_20260924).
# claude-ab (Opus 5.5, max effort), 25 September 2026.
import math
import random

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 30
ok_all = True


def report(name, ok, detail=''):
    global ok_all
    ok_all &= bool(ok)
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))


random.seed(30)
np.random.seed(30)

# A synthetic finite "divisor": reflected off-line pairs (rho, rho#), line points, multiplicities.
# The identities of GDE2-GDE7 are algebraic in the coordinates, so a synthetic set tests them exactly.
pts = []
mult = []
for _ in range(4):
    s_ = random.uniform(0.55, 0.9)
    g_ = random.uniform(5, 40) * random.choice([1, -1])
    m_ = random.randint(1, 3)
    pts += [complex(s_, g_), complex(1 - s_, g_)]  # rho and rho# = 1 - conj(rho)
    mult += [m_, m_]
for _ in range(3):
    pts.append(complex(0.5, random.uniform(5, 40)))
    mult.append(random.randint(1, 2))
Npt = len(pts)
idx = {p: i for i, p in enumerate(pts)}
Jperm = np.zeros((Npt, Npt))
for i, p in enumerate(pts):
    ps = 1 - p.conjugate()
    j = min(range(Npt), key=lambda k: abs(pts[k] - ps))
    assert abs(pts[j] - ps) < 1e-12
    Jperm[i, j] = 1.0  # (Jx)_rho = x_{rho#}
Mw = np.diag(np.array(mult, dtype=float))


def adj(A):
    """Adjoint for <x,y> = sum m x conj(y): A^* = M^{-1} A^H M."""
    return np.linalg.inv(Mw) @ A.conj().T @ Mw


r, t = 3.0, 0.02
sig = np.array([p.real for p in pts])
gam = np.array([p.imag for p in pts])
Delta = r ** sig - r ** (1 - sig)
d = np.exp(-1j * gam * math.log(r)) * Delta
D = np.diag(d)
G = np.diag(np.exp(t * np.array(pts) ** 2))
B = adj(D) @ Jperm @ G
A = adj(B) @ B
a = Delta ** 2 * np.exp(2 * t * (sig ** 2 - gam ** 2))
a_ref = np.array([a[idx[1 - p.conjugate()]] if True else 0 for p in pts])
c = np.conj(d) ** 2 * np.exp(t * np.array(pts) ** 2) * np.exp(t * (1 - np.conj(np.array(pts))) ** 2)
err1 = max(
    np.abs(A - np.diag(a)).max(),
    np.abs(B @ adj(B) - Jperm @ A @ Jperm).max(),
    np.abs(B @ B + np.diag(c)).max(),
    np.abs(adj(B) @ Jperm @ B + adj(G) @ adj(D) @ D @ Jperm @ G).max(),
    np.abs(Jperm @ D @ Jperm + D).max(),
)
# GDE6.1 closed form of c, and c(rho#) = c(rho)
c_closed = Delta ** 2 * np.exp(t * (sig ** 2 + (1 - sig) ** 2 - 2 * gam ** 2)) * np.exp(2j * gam * (math.log(r) + t))
err1 = max(err1, np.abs(c - c_closed).max(), np.abs(Jperm @ c - c).max())
# GDE6.3 block determinant, GDE6.4 product, GDE5.1 traces (ordinary = trace in the orthonormal basis e/sqrt(m))
S = np.diag(np.sqrt(mult))
Bon = S @ B @ np.linalg.inv(S)  # matrix in the orthonormal basis
z = 0.37 + 0.2j
detB = np.linalg.det(np.eye(Npt) + z * Bon)
prod_pairs = 1
for i, p in enumerate(pts):
    if p.real > 0.5:
        prod_pairs *= (1 + z ** 2 * c[i])
err1 = max(err1, abs(detB - prod_pairs), abs(np.trace(Bon)), abs(np.trace(Mw @ Bon)))
report('1  GDE2.1-2.3, GDE5.5, GDE6.1-6.4: B*B = diag(a), BB* = JAJ, B^2 = -M_c, B*JB = -G*P_r J G, det(I+zB) = prod(1+z^2 c), Tr B = 0',
       err1 < 1e-9 * max(1, np.abs(a).max()), 'max err %.1e' % err1)

# 2. GDE7.2 covariance, GDE7.3 degree identity, GDE7.6 closed form of the reflected-pair contribution.
n = 5
Tn = np.diag(n ** np.array(pts))
Un = np.diag(n ** (1 - np.array(pts)))
Tr_ = np.diag(r ** np.array(pts))
Ur_ = np.diag(r ** (1 - np.array(pts)))
Pr = adj(D) @ D
err2 = max(np.abs(B @ Tn - adj(Un) @ B).max() / np.abs(B @ Tn).max(),
           np.abs(B @ Un - adj(Tn) @ B).max() / np.abs(B @ Un).max(),
           np.abs(Pr - (Tr_ @ adj(Tr_) + adj(Ur_) @ Ur_ - 2 * r * np.eye(Npt))).max(),
           np.abs(Pr - (Tr_ - adj(Ur_)) @ (adj(Tr_) - Ur_)).max())
# GDE7.2a traces (divisor-weighted): source coefficient n^{2 sigma} a, target n^{2(1-sigma)} a(rho#)
arefl = Jperm @ a
src = np.sum(np.array(mult) * n ** (2 * sig) * a)
tgt = np.sum(np.array(mult) * n ** (2 * (1 - sig)) * arefl)
err2 = max(err2, abs(src - tgt) / abs(src))
# GDE7.6 symbolic
m_, Dl, tt, gg, de, nn = sp.symbols('m Delta t gamma delta n', positive=True)
lhs = m_ * Dl ** 2 * sp.exp(-2 * tt * gg ** 2) * (sp.exp(2 * tt * (sp.Rational(1, 2) + de) ** 2) * (nn ** (1 + 2 * de) - nn)
                                                + sp.exp(2 * tt * (sp.Rational(1, 2) - de) ** 2) * (nn ** (1 - 2 * de) - nn))
rhs = 2 * m_ * nn * Dl ** 2 * sp.exp(-2 * tt * gg ** 2 + tt / 2 + 2 * tt * de ** 2) * (sp.cosh(2 * de * (tt + sp.log(nn))) - sp.cosh(2 * tt * de))
vals = {m_: 2, Dl: sp.Rational(7, 10), tt: sp.Rational(13, 100), gg: sp.Rational(31, 10), de: sp.Rational(21, 100), nn: 7}
e27 = abs(sp.N((lhs - rhs).subs(vals), 30)) / abs(sp.N(rhs.subs(vals), 30))
report('2  GDE7.2-7.3: B T_n = U_n* B, B U_n = T_n* B, P_r = T T* + U* U - 2r; GDE7.2a source = target trace; GDE7.6 closed form',
       err2 < 1e-9 and e27 < 1e-25, 'max rel err %.1e; GDE7.6 rel err %.1e' % (err2, e27))

# 3. GDE8.3 / ABH0.2: F_0 = s(s-1)/8 pi^{-s/2} Gamma(s/2) zeta(s) = xi(s)/4; special values; "2k!" must be read as 2 * k!.
def F0(s):
    return s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


e3 = 0
for k in range(1, 6):
    s0 = -2 * k
    true = mp.limit(F0, s0) if False else (F0(s0 + mp.mpf('1e-20')) + F0(s0 - mp.mpf('1e-20'))) / 2
    formula_2kfact = k * (2 * k + 1) * (-1) ** k * mp.pi ** k / (2 * mp.factorial(k)) * mp.zeta(s0, derivative=1)
    formula_2k_fact = k * (2 * k + 1) * (-1) ** k * mp.pi ** k / mp.factorial(2 * k) * mp.zeta(s0, derivative=1)
    e3 = max(e3, abs(true - formula_2kfact) / abs(true))
    if k == 2:
        wrong = abs(true - formula_2k_fact) / abs(true)
e3b = max(abs(F0(mp.mpf('1e-25')) - mp.mpf(1) / 8), abs(F0(1 + mp.mpf('1e-25')) - mp.mpf(1) / 8), abs(F0(mp.mpf(2)) - mp.pi / 24), abs(F0(mp.mpf(-1)) - mp.pi / 24))
report('3  GDE8.3: F_0(0)=F_0(1)=1/8, F_0(-1)=F_0(2)=pi/24, F_0(-2k) = k(2k+1)(-1)^k pi^k zeta\'(-2k)/(2 k!), k = 1..5',
       e3 < 1e-15 and e3b < 1e-15 and wrong > 0.5, 'rel err %.1e; reading (2k)! instead fails at k = 2 by %.2f' % (e3, wrong))

# 4. GDE11.2 bounds against the exact range of kappa_{r,q} (24_ Lemma 24.5): kappa = sqrt(r/q) sinh(delta log r)/sinh(delta log q).
ok4 = True
for (rr, qq) in [(3, 2), (2, 3), (10, 1.5), (1.2, 7)]:
    deltas = np.linspace(-0.5, 0.5, 2001)
    deltas = deltas[np.abs(deltas) > 1e-9]
    kap = (rr ** (0.5 + deltas) - rr ** (0.5 - deltas)) / (qq ** (0.5 + deltas) - qq ** (0.5 - deltas))
    kap_exact = math.sqrt(rr / qq) * np.sinh(deltas * math.log(rr)) / np.sinh(deltas * math.log(qq))
    lo = 2 * math.sqrt(rr) * math.log(rr) / ((qq + 1) * math.log(qq))
    hi = (rr + 1) * math.log(rr) / (2 * math.sqrt(qq) * math.log(qq))
    ends = sorted([math.sqrt(rr / qq) * math.log(rr) / math.log(qq), (rr - 1) / (qq - 1)])
    ok4 &= np.allclose(kap, kap_exact) and kap.min() >= lo - 1e-12 and kap.max() <= hi + 1e-12
    # the grid approaches the delta -> 0 end only to O(delta^2) ~ 1e-7 relative
    ok4 &= abs(kap.min() - ends[0]) < 1e-6 * ends[0] and abs(kap.max() - ends[1]) < 1e-6 * ends[1]
    ok4 &= kap.min() >= ends[0] * (1 - 1e-12) and kap.max() <= ends[1] * (1 + 1e-12)
report('4  GDE11.1-11.2: kappa_{r,q} = sqrt(r/q) sinh(d log r)/sinh(d log q); GDE11.2 bounds hold and are implied by the exact range [sqrt(r/q) log r/log q, (r-1)/(q-1)]', ok4)

# 5. GDE11.5 and GDE11.6 limits; GDE9.2-9.3 inequalities on a grid.
ok5 = True
for s_, g_ in [(0.7, 3.0), (0.2, 11.0), (0.9, 0.5)]:
    for tt_ in [1e-4, 1e-6]:
        DD = (r ** s_ - r ** (1 - s_)) ** 2
        q = DD * np.exp(-2 * tt_ * g_ ** 2) * (np.exp(2 * tt_ * (1 - s_) ** 2) - np.exp(2 * tt_ * s_ ** 2)) / tt_
        lim = 2 * DD * (1 - 2 * s_)
        ok5 &= abs(q - lim) < 50 * tt_ * (1 + g_) ** 4 * DD
for de_ in [0.01, 0.2, 0.5, -0.3]:
    for rr in [1.001, 1.0001]:
        v = (rr ** (0.5 + de_) - rr ** (0.5 - de_)) ** 2 / (rr * math.log(rr) ** 2)
        ok5 &= abs(v - 4 * (math.sinh(de_ * math.log(rr)) / math.log(rr)) ** 2) < 1e-9 and abs(v - 4 * de_ ** 2) < 1e-3
for _ in range(2000):
    s_ = random.uniform(0.001, 0.999)
    g_ = random.uniform(-100, 100)
    tt_ = random.uniform(1e-6, 1)
    rho = complex(s_, g_)
    ok5 &= abs(np.exp(tt_ * rho ** 2) - 1) <= tt_ * math.e * (1 + g_ ** 2) * (1 + 1e-12)
    ok5 &= abs(np.exp(2 * tt_ * (s_ ** 2 - g_ ** 2)) - 1) <= 2 * tt_ * math.e ** 2 * (1 + g_ ** 2) * (1 + 1e-12)
report('5  GDE11.5 commutator limit 2 Delta^2 (1 - 2 sigma); GDE11.6 limit 4 delta^2; GDE9.2-9.3 / GDR4.1 inequalities (2000 random points)', ok5)

# 6. ABH1.2 / AHR1.2: ||g_s||^2 = sum |phi_j(s)|^2 <= 1/(2 Re s - 1); AHR1 coefficient identity (j+1)q(j) - j q(j+1) = a_s(j).
ok6 = True
det6 = []
Jmax = 2 * 10 ** 6
jj = np.arange(1, Jmax + 1, dtype=float)
for s in [0.75 + 5j, 0.55 + 14.1j, 0.95 + 0.3j, 0.6 + 100j]:
    phi = (jj ** (1 - s) - (jj + 1) ** (1 - s)) / s
    tot = abs(1 / s) ** 2 + np.sum(np.abs(phi) ** 2)
    # tail bound: |phi_j| <= |1-s| j^{-sigma}/|s|, so the tail is <= |1-s|^2/|s|^2 * Jmax^{1-2 sigma}/(2 sigma - 1)
    tail = abs(1 - s) ** 2 / abs(s) ** 2 * Jmax ** (1 - 2 * s.real) / (2 * s.real - 1)
    bound = 1 / (2 * s.real - 1)
    ok6 &= tot + tail <= bound * (1 + 1e-9)
    det6.append('%.4f<=%.4f' % (tot, bound))
alpha, jv = sp.symbols('alpha j', positive=True)
q_ = lambda x: x ** (1 - alpha) / alpha
a_s = jv * (jv + 1) / alpha * (jv ** (-alpha) - (jv + 1) ** (-alpha))
ok6 &= sp.simplify(sp.expand((jv + 1) * q_(jv) - jv * q_(jv + 1) - a_s)) == 0
# the step from T to g_s: with c_j the coefficients of g_s, T g_s = ((1-z) g_s)'/(1-z) has z^{j-1}-coefficient a_s(j) (numerical, j <= 150)
err6T = 0.0
for s in [0.75 + 5j, 0.6 - 2j]:
    al = np.conj(s)
    Nc = 200
    q_num = np.array([0.0] + [jn ** (1 - al) / al for jn in range(1, Nc + 2)], dtype=complex)
    c_ = q_num[:Nc + 1] - q_num[1:Nc + 2]            # c_j = q(j) - q(j+1), j = 0..Nc
    one_minus_z = np.concatenate(([c_[0]], c_[1:] - c_[:-1]))   # coefficients of (1 - z) g_s
    deriv = np.arange(1, Nc + 1) * one_minus_z[1:]              # z^{j-1} coefficient j * [z^j]
    Tg = np.cumsum(deriv)                                        # divide by (1 - z)
    for jn in range(1, 151):
        a_num = jn * (jn + 1) / al * (jn ** (-al) - (jn + 1) ** (-al))
        err6T = max(err6T, abs(Tg[jn - 1] - a_num) / abs(a_num))
ok6 &= err6T < 1e-9
report('6  ABH1.2 / AHR1.2: sum |phi_j(s)|^2 <= 1/(2 Re s - 1) (with tail bound), four s; AHR1: (j+1)q(j) - j q(j+1) = a_s(j) (symbolic) and the coefficients of T g_s = ((1-z) g_s)\'/(1-z) equal a_s(j) (numerical, j <= 150)',
       ok6, ', '.join(det6) + '; T-step rel err %.1e' % err6T)

# 7. ABH1.4 / AHR1.4: W_n^* g_s = n^{1 - conj s} g_s (block sums of the coefficient sequence, exact telescoping).
ok7 = True
for s in [0.75 + 5j, 0.6 - 3j]:
    Jm = 3000
    coef = np.empty(Jm, dtype=complex)
    coef[0] = np.conj(-1 / s)
    j_ = np.arange(1, Jm, dtype=float)
    coef[1:] = np.conj((j_ ** (1 - s) - (j_ + 1) ** (1 - s)) / s)
    for nn_ in [2, 3, 7]:
        Wstar = np.array([coef[nn_ * k: nn_ * k + nn_].sum() for k in range(Jm // nn_ - 1)])
        # double-precision differences of nearly equal powers give relative rounding of order 1e-12
        ok7 &= np.allclose(Wstar, nn_ ** (1 - np.conj(s)) * coef[:len(Wstar)], rtol=1e-9, atol=1e-14)
report('7  ABH1.4: W_n^* g_s = n^{1 - conj(s)} g_s, n = 2, 3, 7 (first coefficient block included)', ok7)

# 8. ABH0.3 / AHR1.5 (Noor): <h_k, g_s> = (1 - k^{1-s}) zeta(s)/s, h_k = (1-z)^{-1} log((1 + ... + z^{k-1})/k).
ok8 = True
det8 = []
Nn = 4 * 10 ** 6
Nidx = np.arange(0, Nn, dtype=np.int64)
H = np.concatenate(([0.0], np.cumsum(1.0 / np.arange(1, Nn, dtype=float))))
for k in [2, 3]:
    hk = -math.log(k) + H[Nidx] - H[Nidx // k]  # partial sums of (1 - k[k|n])/n, minus log k
    for s in [0.7 + 3j, 0.8 + 21.0j]:
        phi = np.empty(Nn, dtype=complex)
        phi[0] = -1 / s
        j_ = np.arange(1, Nn, dtype=float)
        phi[1:] = (j_ ** (1 - s) - (j_ + 1) ** (1 - s)) / s
        inner = np.sum(hk * phi)  # <h_k, g_s> = sum h_j conj(conj(phi_j))
        target = complex((1 - mp.power(k, 1 - s)) * mp.zeta(s) / s)
        err = abs(inner - target) / abs(target)
        ok8 &= err < 1e-9
        det8.append('k=%d,s=%s: %.1e' % (k, s, err))
report('8  ABH0.3 (Noor): <h_k, g_s> = (1 - k^{1-s}) zeta(s)/s, truncated at 4e6 coefficients (tolerance 1e-9)', ok8, '; '.join(det8))

# 9. ABH2.1-2.5: residue cancellation (8 F_0(0) = 1), the telescoped sum, and the w-derivative identity.
ok9 = True
for s in [mp.mpc('0.3', '2.2'), mp.mpc('-1.7', '0.4'), mp.mpc('2.5', '-6')]:
    nn_ = 6
    lhs9 = mp.fsum([(-1 / s if j == 0 else (mp.power(j, 1 - s) - mp.power(j + 1, 1 - s)) / s) + 8 * F0(s) / s for j in range(nn_)])
    rhs9 = (8 * nn_ * F0(s) - mp.power(nn_, 1 - s)) / s
    ok9 &= abs(lhs9 - rhs9) < 1e-25
eps = mp.mpf('1e-12')
for j in [0, 1, 5]:
    psi = lambda s: ((-1 / s) if j == 0 else (mp.power(j, 1 - s) - mp.power(j + 1, 1 - s)) / s) + 8 * F0(s) / s
    ok9 &= abs(psi(eps) - psi(-eps)) < 1e-6  # no pole at 0
ss, ww = sp.symbols('s w')
F0s = sp.Function('F0')(ss)
Lint = (sp.exp((1 - ss) * ww) - 8 * sp.exp(ww) * F0s) / ss
ok9 &= sp.simplify(sp.diff(Lint, ww) - Lint + sp.exp((1 - ss) * ww)) == 0
report('9  ABH2.1-2.5: psi_j entire (8 F_0(0) = 1), sum_{j<n} psi_j = (8n F_0 - n^{1-s})/s, (d/dw - 1) L = -Lambda(g_t e^{(1-s)w})', ok9)

# 10. ABH3.3: Delta_r(sigma)^2 ||g_lambda||^2 <= (r+1)^2 (log r)^2/4 via ||g||^2 <= 1/(2 sigma - 1), for sigma in (1/2, 1).
ok10 = True
for rr in [1.1, 2, 3, 10, 100]:
    for s_ in np.linspace(0.5001, 0.9999, 500):
        lhs10 = (rr ** s_ - rr ** (1 - s_)) ** 2 / (2 * s_ - 1)
        ok10 &= lhs10 <= (rr + 1) ** 2 * math.log(rr) ** 2 / 4 * (1 + 1e-12)
        ok10 &= (rr ** s_ - rr ** (1 - s_)) <= (rr + 1) * math.log(rr) * (s_ - 0.5) * (1 + 1e-12)
report('10 ABH3.3: Delta_r(sigma) <= (r+1) log r (sigma - 1/2) and Delta^2/(2 sigma - 1) <= (r+1)^2 (log r)^2 / 4 on (1/2, 1)', ok10)

# 11. ABH6.3 / AHR7.5 with W_n built explicitly as a matrix: W_n^* W_n = n I, W_n W_n^* = n P_n, the operators
# Q_j = n^{-j} W^j (I - P_n) (W^*)^j are orthogonal idempotents and sum_{j<J} Q_j = I - n^{-J} W^J (W^*)^J (window n^K).
ok11 = True
nn_, K = 3, 5
Nw = nn_ ** K
def Wmat(L):
    """W_n from C^L to C^{nL}: (W f)_{n k + a} = f_k."""
    M_ = np.zeros((nn_ * L, L))
    for k_ in range(L):
        M_[nn_ * k_: nn_ * k_ + nn_, k_] = 1.0
    return M_
def Wpow(j, N_):
    """W^j from C^{N_/n^j} to C^{N_}."""
    M_ = np.eye(N_ // nn_ ** j) if j == 0 else None
    M_ = np.eye(N_ // nn_ ** j)
    L = N_ // nn_ ** j
    for _ in range(j):
        M_ = Wmat(L) @ M_
        L *= nn_
    return M_
for L in [nn_ ** 2, nn_ ** 3]:
    W_ = Wmat(L)
    Pn = np.kron(np.eye(L), np.ones((nn_, nn_)) / nn_)
    ok11 &= np.allclose(W_.T @ W_, nn_ * np.eye(L)) and np.allclose(W_ @ W_.T, nn_ * Pn)
Qs = []
for j in range(K):
    Wj = Wpow(j, Nw)
    L = Nw // nn_ ** j
    Pn = np.kron(np.eye(L // nn_), np.ones((nn_, nn_)) / nn_)
    Qs.append(nn_ ** (-j) * Wj @ (np.eye(L) - Pn) @ Wj.T)
for i in range(K):
    ok11 &= np.allclose(Qs[i] @ Qs[i], Qs[i]) and np.allclose(Qs[i], Qs[i].T)
    for j in range(K):
        if i != j:
            ok11 &= np.allclose(Qs[i] @ Qs[j], 0)
for J in range(1, K + 1):
    WJ = Wpow(J, Nw)
    ok11 &= np.allclose(sum(Qs[:J]), np.eye(Nw) - nn_ ** (-J) * WJ @ WJ.T)
report('11 ABH6.3 / AHR7.5 with W_n as an explicit matrix: W*W = nI, WW* = nP_n; Q_j orthogonal idempotents; sum_{j<J} Q_j = I - n^{-J} W^J W^{*J} (n = 3, window 3^5)', ok11)

# 12. ABH5.3 and AHR7.2: the diagonal value (n - n^{2(1 - sigma)}) > 0 and the remainder factor n^{J(1 - 2 sigma)} -> 0 for sigma > 1/2.
ok12 = all((nn_ - nn_ ** (2 * (1 - s_))) > 0 and nn_ ** (40 * (1 - 2 * s_)) < 1 for nn_ in [2, 3, 10] for s_ in np.linspace(0.501, 0.999, 50))
report('12 ABH5.3 sign and AHR7.2 decay factor for sigma in (1/2, 1) (elementary inequalities)', ok12)

print('ALL PASS' if ok_all else 'SOME CHECK FAILED')
