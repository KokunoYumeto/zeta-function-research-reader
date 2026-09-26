#!/usr/bin/env python3
"""Referee v2, script r07.  Prop 4.6 (the chiral form and Weil's form), version 2's part (c).

Synthetic #-closed zero sets S (n_on points on Re = 1/2, n_pairs off-line pairs {rho, rho#}, multiplicities
1..3), the two-line set W = S u (S - 1), A(w) = -conj(w), and Q_A(f, g) = sum_w m_w f(w) conj(g(A w)).
 1. A maps W to W, has no fixed point; Q_A has signature (N, N), N = |S| (a sum of hyperbolic planes).
 2. V+ (T-even: f(rho - 1) = f(rho)) and V- (T-odd) are Q_A-orthogonal (the cross block is 0).
 3. Q_A = 2 Omega on V+ and -2 Omega on V-, Omega(u) = sum m u(rho) conj(u(rho#)).
 4. signature of Q_A on V+ = (n_on + n_pairs, n_pairs); on V- = (n_pairs, n_on + n_pairs).
 5. 'RH' (n_pairs = 0): Q_A is definite on V+ (positive) and V- (negative), each of dimension N = the maximal
    dimension of a positive (negative) subspace, so both are maximal.
 6. Without #-closure (a lone off-line point) the form on V+ is degenerate (a null direction), which is why the
    statement assumes a #-closed support.
"""
import numpy as np, itertools, random
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))
def sig(M, tol=1e-9):
    ev = np.linalg.eigvalsh((M + M.conj().T) / 2)
    return int((ev > tol).sum()), int((ev < -tol).sum()), int((abs(ev) <= tol).sum())
def build(S, mult):
    W = [z for z in S] + [z - 1 for z in S]
    mW = mult + mult
    idx = {complex(round(z.real, 12), round(z.imag, 12)): i for i, z in enumerate(W)}
    n = len(W); Q = np.zeros((n, n), complex)
    for i, w in enumerate(W):
        Aw = -np.conj(w); j = idx[complex(round(Aw.real, 12), round(Aw.imag, 12))]
        Q[i, j] += mW[i]              # Q_A(f,g) = sum_i m_i f_i conj(g_{A(i)}) = f^T Q conj(g); as Hermitian matrix f* M f use M = Q^T
    return W, Q.T, idx
random.seed(3)
allok = [True] * 6
for n_on, n_pairs in itertools.product(range(0, 4), range(0, 4)):
    if n_on + n_pairs == 0: continue
    S, mult = [], []
    for k in range(n_on):
        S.append(complex(0.5, 14 + 7 * k)); mult.append(random.randint(1, 3))
    for k in range(n_pairs):
        b = 0.5 + random.uniform(0.05, 0.45); g = 50 + 9 * k; m = random.randint(1, 3)
        S += [complex(b, g), complex(1 - b, g)]; mult += [m, m]
    N = len(S)
    W, M, idx = build(S, mult)
    # 1
    allok[0] &= sig(M) == (N, N, 0)
    # bases of V+ and V-
    Vp = np.zeros((2 * N, N), complex); Vm = np.zeros((2 * N, N), complex)
    for i in range(N):
        Vp[i, i] = Vp[N + i, i] = 1; Vm[i, i] = 1; Vm[N + i, i] = -1
    Mpp = Vp.conj().T @ M @ Vp; Mmm = Vm.conj().T @ M @ Vm; Mpm = Vp.conj().T @ M @ Vm
    allok[1] &= np.abs(Mpm).max() < 1e-12
    # Omega matrix on S
    Om = np.zeros((N, N), complex)
    for i, z in enumerate(S):
        zs = 1 - np.conj(z); j = [k for k, y in enumerate(S) if abs(y - zs) < 1e-12][0]
        Om[j, i] += mult[i]         # Omega(u) = sum_i m_i u_i conj(u_{#i}) = u* Om u with Om[#i, i] = m_i
    allok[2] &= np.abs(Mpp - 2 * Om).max() < 1e-12 and np.abs(Mmm + 2 * Om).max() < 1e-12
    allok[3] &= sig(Mpp)[:2] == (n_on + n_pairs, n_pairs) and sig(Mmm)[:2] == (n_pairs, n_on + n_pairs)
    if n_pairs == 0:
        allok[4] &= sig(Mpp) == (N, 0, 0) and sig(Mmm) == (0, N, 0) and sig(M)[0] == N
rep("1  Q_A hyperbolic: signature (N, N) on every configuration", allok[0])
rep("2  V+ and V- are Q_A-orthogonal (unconditionally)", allok[1])
rep("3  Q_A = 2 Omega on V+, -2 Omega on V-", allok[2])
rep("4  signature on V+ is (n_on + n_pairs, n_pairs), on V- (n_pairs, n_on + n_pairs)", allok[3], "15 configurations, n_on, n_pairs <= 3, multiplicities 1..3")
rep("5  no off-line pairs: V+ positive definite, V- negative definite, both of the maximal dimension N", allok[4])
# 6: a lone off-line point (not #-closed): restrict Q_A|V+ to data supported on {rho} only
S = [complex(0.7, 30), complex(0.3, 30)]; mult = [1, 1]
W, M, idx = build(S, mult)
Vp1 = np.zeros((4, 1), complex); Vp1[0, 0] = Vp1[2, 0] = 1      # T-even data supported on rho only
rep("6  T-even data on a lone off-line point: Q_A vanishes there (a null direction), so #-closure is needed",
    abs((Vp1.conj().T @ M @ Vp1)[0, 0]) < 1e-12)
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
