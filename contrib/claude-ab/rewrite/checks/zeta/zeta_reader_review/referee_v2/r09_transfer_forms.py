#!/usr/bin/env python3
"""Referee v2, script r09.  Lemma 3.13 (transfer-compatible Hermitian forms), version 2.

Synthetic configuration, stable under # (rho -> 1 - conj rho) AND under conjugation, with multiplicities:
  on-line 1/2 +- 14.134725 i (m=1), 1/2 +- 21.022040 i (m=2),
  on-line 1/2 +- 40 i and 1/2 +- (40 + 2 pi/log 2) i (m=1): a line pair 2 pi/log 2 apart,
  off-line quartet 0.7 +- 30 i, 0.3 +- 30 i (m=1),
  off-line quartet 0.8 +- 60 i, 0.2 +- 60 i and its companion 0.8 +- (60 + 2 pi/log2) i, 0.2 +- (60 + 2pi/log 2) i (m=3).
For B(x, y) = sum x_rho conj(y_eta) B_{rho,eta}, B(T_n x, T_n y) = n B(x, y) reads (n^{rho + conj eta - 1} - 1) B_{rho,eta} = 0.
 1. n in {2, 3}: the admissible entries are exactly (rho, rho#).
 2. n = 2 alone admits exactly the entries with eta - rho# in (2 pi i/log 2) Z (strictly more here);
    {2, 4} (rational log-ratio) admits the same as {2}; {2, 3} = {3, 5} = {2, 3, 5, 7} (irrational ratios).
 3. Converse: B = sum b_rho m_rho x_rho conj(y_rho#) with b_{rho#} = conj(b_rho) satisfies the relation for random real n > 0.
 4. Positivity (as a form on l^2(Z, m)) holds iff b = 0 off the line and b >= 0 on it (2000 random b, eigenvalues);
    an off-line block has eigenvalues +- m|b| as a form on C^2.
"""
import numpy as np, random, math
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))
d2 = 2 * math.pi / math.log(2)
base = [(0.5, 14.134725, 1), (0.5, 21.022040, 2), (0.5, 40.0, 1), (0.5, 40.0 + d2, 1),
        (0.7, 30.0, 1), (0.3, 30.0, 1), (0.8, 60.0, 3), (0.2, 60.0, 3), (0.8, 60.0 + d2, 3), (0.2, 60.0 + d2, 3)]
Z, m = [], []
for b, g, mm in base:
    Z += [complex(b, g), complex(b, -g)]; m += [mm, mm]
n = len(Z)
sharp = lambda z: 1 - z.conjugate()
def find(z):
    for i, y in enumerate(Z):
        if abs(y - z) < 1e-9: return i
    return None
rep("0  configuration is #-stable and conjugation-stable with m(rho#) = m(rho)",
    all(find(sharp(z)) is not None and m[find(sharp(z))] == m[i] and find(z.conjugate()) is not None for i, z in enumerate(Z)), f"{n} points")
def admissible(ns, tol=1e-9):
    A = set()
    for i, r in enumerate(Z):
        for j, e in enumerate(Z):
            z = r + e.conjugate() - 1
            if all(abs(np.exp(z * math.log(k)) - 1) < tol for k in ns): A.add((i, j))
    return A
pairs = {(i, find(sharp(z))) for i, z in enumerate(Z)}
A23 = admissible((2, 3)); A2 = admissible((2,)); A24 = admissible((2, 4)); A35 = admissible((3, 5)); A2357 = admissible((2, 3, 5, 7))
rep("1  n in {2,3}: admissible entries = {(rho, rho#)}", A23 == pairs, f"{len(A23)} entries, {sum(1 for (i,j) in A23 if i != j)} off the diagonal")
alias = set()
for i, r in enumerate(Z):
    for j, e in enumerate(Z):
        q = (e - sharp(r)) / (1j * d2)
        if abs(q.imag) < 1e-9 and abs(q.real - round(q.real)) < 1e-9: alias.add((i, j))
rep("2  n = 2 alone: admissible iff eta - rho# in (2 pi i/log 2)Z; {2,4} same as {2}; {3,5} and {2,3,5,7} same as {2,3}",
    A2 == alias and len(A2) > len(A23) and A24 == A2 and A35 == A23 and A2357 == A23, f"{len(A2)} entries for n = 2")
random.seed(11)
def form_matrix(bvals):
    # f* M f = B(f, f) = sum_rho b_rho m_rho f_rho conj(f_rho#)  ->  M[rho#, rho] = b_rho m_rho
    M = np.zeros((n, n), complex)
    for i, z in enumerate(Z):
        M[find(sharp(z)), i] += bvals[i] * m[i]
    return M
def random_b(online_real_nonneg, offline_zero):
    b = [None] * n
    for i, z in enumerate(Z):
        j = find(sharp(z))
        if b[i] is not None: continue
        if i == j:
            b[i] = abs(random.gauss(0, 1)) if online_real_nonneg else random.gauss(0, 1)
        else:
            v = 0 if offline_zero else complex(random.gauss(0, 1), random.gauss(0, 1))
            b[i] = v; b[j] = np.conj(v)
    return b
okc = True
for _ in range(50):
    b = random_b(False, False); M = form_matrix(b)
    for nn in (random.uniform(0.1, 10) for _ in range(5)):
        T = np.diag([nn**z for z in Z])
        okc &= np.allclose(T.conj().T @ M @ T, nn * M, atol=1e-8 * nn * (1 + abs(M).max()))
rep("3  converse: Weil-type forms satisfy B(T_n x, T_n y) = n B(x, y) for random real n > 0 (Hermitian: M = M*)", okc and np.allclose(M, M.conj().T))
agree = 0; trials = 0
for _ in range(2000):
    online_nonneg = random.random() < 0.5; offline_zero = random.random() < 0.5
    b = random_b(online_nonneg, offline_zero)
    # evaluate positivity relative to the weighted inner product: B(x,x) >= 0 for all x <=> M PSD
    ev = np.linalg.eigvalsh((form_matrix(b) + form_matrix(b).conj().T) / 2)
    psd = ev.min() > -1e-10
    crit = all((abs(b[i]) < 1e-15) if find(sharp(z)) != i else (b[i].real >= 0) for i, z in enumerate(Z))
    agree += (psd == crit); trials += 1
rep("4  positivity <=> b = 0 off the line and b >= 0 on it", agree == trials, f"{agree}/{trials} random forms agree")
bb, mm = 0.8 - 0.6j, 3
blk = np.array([[0, np.conj(bb) * mm], [bb * mm, 0]])
rep("4' an off-line block 2m Re(b x conj(x#)) has eigenvalues +- m|b| on C^2", np.allclose(sorted(np.linalg.eigvalsh(blk)), [-mm * abs(bb), mm * abs(bb)]))
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
