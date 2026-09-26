#!/usr/bin/env python3
"""Checks for the finding on reader Lemma 3.13 (positive transfer-adjoint forms).

Claim.  On l^2(Z, m), a bounded Hermitian form B with B(T_n x, T_n y) = n B(x, y) for n = 2 and n = 3
(no other n needed) is exactly  B(x, y) = sum_rho b_rho m_rho x_rho conj(y_{rho#}),  rho# = 1 - conj(rho),
with (b_rho) bounded and b_{rho#} = conj(b_rho).  Such a form satisfies the relation for every real n > 0.
It is positive semidefinite iff b_rho = 0 at every off-line rho and b_rho >= 0 on the line.
Weil's pairing is b = 1.  One value of n does not suffice (counterexample below).

Finite synthetic check: an index set closed under rho -> rho# and rho -> conj(rho), containing real
zeta zeros, a hypothetical off-line quartet and a pair of line points differing by 2 pi i / log 2.
"""
import numpy as np, mpmath as mp, itertools
rng = np.random.default_rng(1)

g = [float(mp.zetazero(k).imag) for k in (1, 2, 3)]
pts = []
for y in g:                                   # line zeros and conjugates
    pts += [complex(0.5, y), complex(0.5, -y)]
pts += [complex(0.7, 10.0), complex(0.3, 10.0), complex(0.7, -10.0), complex(0.3, -10.0)]   # off-line quartet (hypothetical)
d = 2*np.pi/np.log(2)
pts += [complex(0.5, 50.0), complex(0.5, 50.0 + d), complex(0.5, -50.0), complex(0.5, -50.0 - d)]  # line pair with gap 2 pi/log 2
m = np.array([1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1])   # multiplicities, # and conj invariant
P = np.array(pts); N = len(P)
sharp = lambda z: 1 - np.conj(z)
idx = {complex(round(z.real, 12), round(z.imag, 12)): i for i, z in enumerate(P)}
def index(z): return idx[complex(round(z.real, 12), round(z.imag, 12))]
perm = np.array([index(sharp(z)) for z in P])
assert all(m[perm] == m)

def allowed_entries(ns):
    """entries (i,j) left free by the conditions (n^{rho_i + conj(rho_j)} - n) B_ij = 0 for n in ns"""
    free = np.zeros((N, N), bool)
    for i in range(N):
        for j in range(N):
            e = P[i] + np.conj(P[j]) - 1
            free[i, j] = all(abs(np.exp(e*np.log(n)) - 1) < 1e-9 for n in ns)
    return free

ok = True
F23 = allowed_entries([2, 3])
Fall = allowed_entries(range(2, 60))
F2 = allowed_entries([2])
target = np.zeros((N, N), bool)
for i in range(N):
    target[i, perm[i]] = True
print("free entries with n in {2,3}      :", int(F23.sum()), " (expected N =", N, ", one per rho, at (rho, rho#))")
print("free entries with n in {2,...,59} :", int(Fall.sum()))
print("free entries with n = 2 only      :", int(F2.sum()), " (extra entries = forms not of Weil type)")
ok &= np.array_equal(F23, target) and np.array_equal(Fall, target)
extra = [(i, j) for i in range(N) for j in range(N) if F2[i, j] and not target[i, j]]
print("   extra free entries for n = 2 only:", [(complex(np.round(P[i],3)), complex(np.round(P[j],3))) for i, j in extra])
ok &= len(extra) > 0

def weil_type(b):
    B = np.zeros((N, N), complex)
    for i in range(N):
        B[i, perm[i]] = b[i]*m[i]
    return B

# Hermitian condition b_{rho#} = conj(b_rho); transfer identity for random real n > 0 (non-integer too)
for trial in range(200):
    b = rng.normal(size=N) + 1j*rng.normal(size=N)
    b = (b + np.conj(b[perm]))/2                 # enforce b_{rho#} = conj b_rho
    B = weil_type(b)
    ok &= np.allclose(B, B.conj().T)
    n = rng.uniform(0.1, 30)
    Tn = np.diag(np.exp(P*np.log(n)))
    ok &= np.allclose(Tn.T @ B @ Tn.conj(), n*B)          # B(T_n x, T_n y) = x^T Tn^T B conj(Tn) conj(y)
print("Weil-type forms: Hermitian and transfer-compatible for random real n:", ok)

# positivity criterion
on = np.array([abs(z.real - 0.5) < 1e-12 for z in P])
cnt_psd = cnt_pred = 0; agree = True
for trial in range(4000):
    b = rng.normal(size=N) + 1j*rng.normal(size=N)
    mode = trial % 4
    if mode == 0:      # generic
        pass
    elif mode == 1:    # zero off line, arbitrary real on line
        b[~on] = 0; b[on] = rng.normal(size=on.sum())
    elif mode == 2:    # zero off line, nonnegative on line
        b[~on] = 0; b[on] = np.abs(rng.normal(size=on.sum()))
    else:              # nonnegative on line, small off-line
        b[on] = np.abs(rng.normal(size=on.sum())); b[~on] *= 1e-3
    b = (b + np.conj(b[perm]))/2
    B = weil_type(b)
    ev = np.linalg.eigvalsh((B + B.conj().T)/2)
    psd = ev.min() > -1e-12
    pred = np.allclose(b[~on], 0) and np.all(b[on].real > -1e-12) and np.allclose(b[on].imag, 0)
    agree &= (psd == pred)
    cnt_psd += psd; cnt_pred += pred
print(f"positivity iff (b = 0 off line, b >= 0 on line): agreement on 4000 random forms: {agree}  (psd cases: {cnt_psd})")
ok &= agree
# off-line pair block is hyperbolic: eigenvalues +-|b| m
b = np.zeros(N, complex); i0 = 6; b[i0] = 0.8+0.3j; b[perm[i0]] = np.conj(b[i0])
ev = np.linalg.eigvalsh(weil_type(b))
print("off-line pair block eigenvalues (nonzero):", np.round(ev[np.abs(ev) > 1e-12], 6), " = +-|b| m =", round(abs(b[i0])*m[i0], 6))
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
