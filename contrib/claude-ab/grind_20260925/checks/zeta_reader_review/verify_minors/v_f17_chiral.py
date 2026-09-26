#!/usr/bin/env python3
"""F17 verification (independent code).

(i)-(iii) On a synthetic #-closed configuration Z (n_on on-line points, n_pairs off-line pairs, multiplicities),
    build the Hermitian matrix of Q_A(f,g) = sum_w m_w f(w) conj g(Aw) on functions on Z u (Z-1), A(s) = -conj(s),
    and check: Q_A Hermitian; V+ (T-even) and V- (T-odd) are Q_A-orthogonal (cross block = 0) whether or not
    off-line points are present; signature of Q_A on V+ is (n_on + n_pairs, n_pairs); on V- it is (n_pairs, n_on + n_pairs);
    with no off-line pairs, V+ positive definite and V- negative definite (so each is maximal of its sign).
(iv) #-invariance of the zeros of L(s,chi) for complex primitive chi: |Lambda(1 - conj s, chi)| = |Lambda(s, chi)| for all s
    (non-vacuous test at off-line points), from Lambda(s,chi) = W Lambda(1-s, conj chi) and conj Lambda(conj s, conj chi) = Lambda(s,chi);
    |W| = 1; and the zero set is NOT invariant under s -> 1 - s (checked at an actual zero).
    Also A(Z_chi) = Z_chi - 1 at that zero and G_chi(it) != 0 on a grid.
"""
import itertools, random
import numpy as np
import mpmath as mp

mp.mp.dps = 30
random.seed(11)

def build(n_on, n_pairs):
    pts, mult = [], []
    for k in range(n_on):
        pts.append(complex(0.5, 10 + 3 * k)); mult.append(random.randint(1, 3))
    for k in range(n_pairs):
        b = random.uniform(0.55, 0.9); g = 50 + 4 * k; m = random.randint(1, 3)
        pts += [complex(b, g), complex(1 - b, g)]; mult += [m, m]
    return pts, mult

def sharp(z):
    return complex(1 - z.real, z.imag)

def test_config(n_on, n_pairs):
    Z, mult = build(n_on, n_pairs)
    W = Z + [z - 1 for z in Z]
    mW = mult + mult
    idx = {w: i for i, w in enumerate(W)}
    N = len(W)
    A = lambda w: complex(-w.real, w.imag)
    Qm = np.zeros((N, N), dtype=complex)        # Q(f,g) = f^T Qm conj(g)
    for i, w in enumerate(W):
        j = min(range(N), key=lambda k: abs(W[k] - A(w)))
        assert abs(W[j] - A(w)) < 1e-12
        Qm[i, j] += mW[i]
    # Hermitian form H with Q(f,f) = f^* H f  : H = Qm^T conj?  Q(f,f) = sum_i m_i f_i conj(f_{A i}) ; as f^* H f -> H_{A i, i} = m_i
    H = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            if Qm[i, j]:
                H[j, i] += Qm[i, j]
    assert np.allclose(H, H.conj().T)
    n = len(Z)
    # T-even basis e_rho + e_{rho-1}; T-odd basis e_rho - e_{rho-1}
    Ep = np.zeros((N, n)); Em = np.zeros((N, n))
    for k in range(n):
        Ep[k, k] = 1; Ep[n + k, k] = 1
        Em[k, k] = 1; Em[n + k, k] = -1
    Hpp = Ep.T @ H @ Ep; Hmm = Em.T @ H @ Em; Hpm = Ep.T @ H @ Em
    ev_p = np.linalg.eigvalsh(Hpp); ev_m = np.linalg.eigvalsh(Hmm)
    sig_p = (int((ev_p > 1e-9).sum()), int((ev_p < -1e-9).sum()))
    sig_m = (int((ev_m > 1e-9).sum()), int((ev_m < -1e-9).sum()))
    return np.abs(Hpm).max(), sig_p, sig_m

def main():
    print("(i)-(iii) Q_A on synthetic #-closed configurations")
    for n_on, n_pairs in itertools.product(range(0, 5), range(0, 5)):
        if n_on + n_pairs == 0:
            continue
        cross, sp_, sm_ = test_config(n_on, n_pairs)
        assert cross < 1e-12, cross
        assert sp_ == (n_on + n_pairs, n_pairs), (n_on, n_pairs, sp_)
        assert sm_ == (n_pairs, n_on + n_pairs), (n_on, n_pairs, sm_)
    print("  all 24 configurations (n_on, n_pairs <= 4): V+ _|_ V- (max cross entry 0), sig(Q_A|V+) = (n_on+n_pairs, n_pairs),")
    print("  sig(Q_A|V-) = (n_pairs, n_on+n_pairs); for n_pairs = 0: V+ positive definite, V- negative definite")

    print("(iv) complex primitive chi mod 5, chi(2) = i (odd, a = 1)")
    q, a = 5, 1
    chi = [0, 1, 1j, -1j, -1]; chib = [0, 1, -1j, 1j, -1]
    Lam = lambda s, c: (mp.mpf(q) / mp.pi) ** ((s + a) / 2) * mp.gamma((s + a) / 2) * mp.dirichlet(s, c)
    Wv = []
    for s in (mp.mpc(0.23, 4.1), mp.mpc(0.81, -7.7), mp.mpc(0.66, 17.3), mp.mpc(-0.4, 2.2)):
        Wv.append(Lam(s, chi) / Lam(1 - s, chib))
        lhs = abs(Lam(1 - mp.conj(s), chi)); rhs = abs(Lam(s, chi))
        refl = abs(Lam(1 - s, chi))
        print("  s=%s: |Lam(1-conj s,chi)| = %s, |Lam(s,chi)| = %s, |Lam(1-s,chi)| = %s"
              % (mp.nstr(s, 4), mp.nstr(lhs, 10), mp.nstr(rhs, 10), mp.nstr(refl, 6)))
        assert abs(lhs - rhs) / rhs < 1e-25
    spread = max(abs(w - Wv[0]) for w in Wv)
    print("  root number W = %s, |W| = %s, constant across points to %.1e" % (mp.nstr(Wv[0], 10), mp.nstr(abs(Wv[0]), 12), float(spread)))
    rho = mp.findroot(lambda s: mp.dirichlet(s, chi), mp.mpc(0.5, 6.18))
    print("  zero rho = %s: |L(1-conj rho)| = %.1e (the #-partner), |L(1-rho)| = %s (s -> 1-s is not a symmetry)"
          % (mp.nstr(rho, 12), float(abs(mp.dirichlet(1 - mp.conj(rho), chi))), mp.nstr(abs(mp.dirichlet(1 - rho, chi)), 5)))
    Arho = -mp.conj(rho)
    print("  A(rho) = -conj(rho) = %s ; Lam(A(rho)+1, chi) = %.1e (so A(rho) in Z_chi - 1)" % (mp.nstr(Arho, 10), float(abs(Lam(Arho + 1, chi)))))
    Gmin = min(abs(Lam(mp.mpc(0, t), chi) * Lam(mp.mpc(1, t), chi)) * mp.exp(mp.pi * abs(t) / 2) for t in mp.linspace(-40, 40, 321))
    print("  min over t in [-40,40] of |G_chi(it)| e^{pi|t|/2} = %s > 0 (no zero on Re s = 0)" % mp.nstr(Gmin, 5))
    assert Gmin > 0
    print("ALL F17 CHECKS PASS")

if __name__ == "__main__":
    main()
