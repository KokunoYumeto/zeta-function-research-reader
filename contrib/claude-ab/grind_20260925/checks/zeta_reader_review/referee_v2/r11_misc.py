#!/usr/bin/env python3
"""Referee v2, script r11: smaller numerical claims of version 2.
 a. Lemma 3.6: (1+x)/(1/2+x) at x = gamma_1 = 14.1347... equals 1.034165 < 1.0342, but the reader's
    intermediate bound '15.14/14.64' = 1.034153 is SMALLER than the true maximum (a slip, not affecting 1.0342).
 b. Residue duality: zeta(2)(1/pi + 8 pi/5) = 8.79194, zeta(2)(1+4pi^2)/pi = 21.19445; int (1+|t|)^{-7/2} = 4/5;
    |1/zeta(-1+it)| <= 4 pi^2 zeta(2) (1+|t|)^{-3/2} on a grid of t in [0, 300].
 c. Cor 2.2: (1/2)^s zeta(s, 1/2) = (1 - 2^{-s}) zeta(s) (the odd-prime Euler product); zeta(s,1/2) = 2^s(1-2^{-s})zeta(s).
 d. Thm 4.1 on several sheets: d/da zeta(s,a) = -s zeta(s+1,a); s zeta(s+1,a) -> 1 at s = 0; the m = 3 jet
    -(s)_3 zeta(s+3,a) vanishes at 0 and -1 and equals -(m-1)! = -2 at 1-m = -2; the first jet vanishes at s0 - 1
    for the zero s0 of zeta(., 2) near 1.4078 + 23.328i.
 e. The remark after Thm 4.1: |zeta(1 - conj(s1), 1/2)| = |zeta(1 + 2 pi i/log 2)| != 0 for s1 = 2 pi i/log 2
    (so the zero set of zeta(., 1/2) is not #-symmetric).  But part (d) itself HOLDS at a = 1/2:
    zeta(z - 1, 1/2) != 0 for the zeros z = 2 pi i k/log 2 (k = 0..6), z = -2, -4, -6 and the first ten rho.
 f. Platt-Trudgian: theta(T)/pi + 1 at T = 3 000 175 332 800 is 1.2363e13 >= 1.2e13 (Theorem D bullet).
 g. Prop 3.12 (a = 2, F = {3, 5}, J = 3): the evaluation combinations at s_j = 2 pi i j/log 2, j <= J + |F|,
    killing g_t h_n (n in F) form a space of dimension J, and they kill g_t h_{2^k}, k <= 20.
 h. Prop 2.6 without Dirichlet: q = 7, H = {1,2,4} (d = 2, p = 3, r = 5) and H = {1,6} (d = 3, p = 3, r = 11):
    A_j = p^{d-j} r^j are atoms of M_H and A_0 A_2 = A_1^2.
"""
import mpmath as mp, math, itertools
mp.mp.dps = 40
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))

g1 = mp.im(mp.zetazero(1))
true_max = (1 + g1) / (mp.mpf(1) / 2 + g1)
stated = mp.mpf('15.14') / mp.mpf('14.64')
rep("a  Lemma 3.6: max of (1+x)/(1/2+x) over x >= gamma_1 is 1.034165 < 1.0342; the stated '15.14/14.64' is smaller than it",
    true_max < mp.mpf('1.0342') and stated < true_max, f"true max {mp.nstr(true_max, 8)}, stated 15.14/14.64 = {mp.nstr(stated, 8)}")

z2 = mp.zeta(2)
c_new, c_old = z2 * (1 / mp.pi + 8 * mp.pi / 5), z2 * (1 + 4 * mp.pi**2) / mp.pi
I = mp.quad(lambda t: (1 + abs(t))**(-mp.mpf(7) / 2), [-mp.inf, 0, mp.inf])
worst = max(abs(1 / mp.zeta(mp.mpc(-1, t))) / (4 * mp.pi**2 * z2 * (1 + t)**(-mp.mpf(3) / 2)) for t in [mp.mpf(k) / 4 for k in range(0, 1201)])
rep("b  residue duality constants and the edge bound on Re s = -1",
    abs(c_new - mp.mpf('8.79194')) < 1e-5 and abs(c_old - mp.mpf('21.19445')) < 1e-5 and abs(I - mp.mpf(4) / 5) < 1e-25 and worst <= 1,
    f"new {mp.nstr(c_new, 8)}, old {mp.nstr(c_old, 8)}, int = {mp.nstr(I, 10)}, max ratio {mp.nstr(worst, 6)}")

w = 0
for s in (mp.mpc(2, 3), mp.mpc('0.3', 17), mp.mpc(-1.5, 2)):
    w = max(w, abs(mp.power(mp.mpf(1) / 2, s) * mp.zeta(s, mp.mpf(1) / 2) - (1 - mp.power(2, -s)) * mp.zeta(s)))
p = mp.nprod(lambda k: 1, [1, 1])  # placeholder
ep = mp.fprod([1 / (1 - mp.power(q, -3)) for q in [x for x in range(3, 20000) if all(x % d for d in range(2, int(x**0.5) + 1))]])
rep("c  Cor 2.2: (1/2)^s zeta(s,1/2) = (1-2^-s) zeta(s); at s = 3 it matches the product over odd primes",
    w < 1e-30 and abs(ep - (1 - mp.power(2, -3)) * mp.zeta(3)) < 1e-8, f"max identity error {mp.nstr(w, 3)}, Euler product error {mp.nstr(abs(ep - (1 - mp.power(2, -3)) * mp.zeta(3)), 3)}")

werr = 0
for a in (mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf(2), mp.mpf('3.7')):
    for s in (mp.mpc('0.25', 4), mp.mpc('-2.3', '1.1'), mp.mpc('0.6', -9)):
        lhs = mp.diff(lambda aa: mp.zeta(s, aa), a)
        werr = max(werr, abs(lhs + s * mp.zeta(s + 1, a)) / abs(lhs))
lim0 = [mp.limit(lambda s: s * mp.zeta(s + 1, a), 0) for a in (mp.mpf('0.3'), mp.mpf(2), mp.mpf('3.7'))]
a = mp.mpf('0.3')
jet3 = lambda s: -mp.rf(s, 3) * mp.zeta(s + 3, a)
s0 = mp.findroot(lambda s: mp.zeta(s, 2), mp.mpc('1.40779', '23.328'))
jet_at = abs(-(s0 - 1) * mp.zeta(s0, 2))
rep("d  Thm 4.1: identity on four sheets; value 1 at s = 0; m = 3 jet zeros at 0, -1 and value -2 at -2; first jet at s0 - 1",
    werr < 1e-20 and all(abs(v - 1) < 1e-20 for v in lim0) and abs(jet3(mp.mpf(0))) < 1e-30 and abs(jet3(mp.mpf(-1))) < 1e-30
    and abs(mp.limit(jet3, -2) + 2) < 1e-15 and jet_at < 1e-30,
    f"max rel. err {mp.nstr(werr, 3)}, s0 = {mp.nstr(s0, 12)}, jet(-2) = {mp.nstr(mp.limit(jet3, -2), 10)}")

s1 = 2j * mp.pi / mp.log(2)
val = mp.zeta(1 - mp.conj(s1), mp.mpf(1) / 2)
zs = [2j * mp.pi * k / mp.log(2) for k in range(0, 7)] + [-2, -4, -6] + [mp.zetazero(k) for k in range(1, 11)]
mins = min(abs(mp.zeta(z - 1, mp.mpf(1) / 2)) for z in zs)
zero_check = max(abs(mp.zeta(z, mp.mpf(1) / 2)) for z in zs[1:])   # the listed z are zeros of zeta(., 1/2) (k >= 1, trivial, rho)
# note: mpmath's default zeta(s) is ill-conditioned exactly at s = 1 + 2 pi i k/log 2 (it divides by 1 - 2^{1-s}); use Euler-Maclaurin
rep("e  a = 1/2: not #-symmetric (|zeta(1+2 pi i/log2)| = 1.351), yet zeta(., 1/2) has no zero at z - 1 for these zeros z (part (d) holds here)",
    abs(val - mp.zeta(1 + s1, 1, method='euler-maclaurin')) < 1e-30 and abs(val) > 1 and mins > 1e-3 and zero_check < 1e-25,
    f"|zeta(1 - conj s1, 1/2)| = {mp.nstr(abs(val), 6)}, min |zeta(z-1, 1/2)| = {mp.nstr(mins, 5)}, max |zeta(z,1/2)| at listed zeros {mp.nstr(zero_check, 3)}")

T = mp.mpf(3000175332800)
NT = mp.siegeltheta(T) / mp.pi + 1
rep("f  Riemann-von Mangoldt main term at Platt-Trudgian's height: >= 1.2e13", NT > mp.mpf('1.2e13'), mp.nstr(NT, 10))

aa, F, J, t = 2, (3, 5), 3, mp.mpf('0.2')
sj = [2j * mp.pi * j / mp.log(aa) for j in range(1, J + len(F) + 1)]
h = lambda n, s: mp.exp(t * s * s) * n * (1 - mp.power(n, -s)) / s
h0 = lambda n, s: n * (1 - mp.power(n, -s)) / s     # g_t(s_j) != 0 only rescales columns
A = mp.matrix([[h0(n, s) for s in sj] for n in F])          # |F| x (J+|F|) conditions
import numpy as np
An = np.array([[complex(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
U, Sv, Vh = np.linalg.svd(An)
null = Vh[len(F):].conj().T                                   # basis of the null space
dimnull = null.shape[1]
kill = max(abs(sum(null[j, c] * complex(h0(aa**k, sj[j])) for j in range(len(sj)))) for c in range(dimnull) for k in range(1, 21))
killF = max(abs(sum(null[j, c] * complex(h0(n, sj[j])) for j in range(len(sj)))) for c in range(dimnull) for n in F)
rep("g  Prop 3.12: annihilating combinations of evaluations form a space of dimension J; they kill g_t h_{2^k}",
    dimnull == J and min(Sv) > 1e-3 and kill < 1e-12 and killF < 1e-12, f"null dimension {dimnull} (singular values {[round(x, 4) for x in Sv]}), max residual on 2^k {kill:.2e}, on F {killF:.2e}")

def is_atom(x, member):
    return not any(x % d == 0 and member(d) and member(x // d) for d in range(2, x) )
ok_h = True
for H, (pp, rr, d) in (({1, 2, 4}, (3, 5, 2)), ({1, 6}, (3, 11, 3))):
    member = lambda x, H=H: x % 7 != 0 and (x % 7) in H
    Aj = [pp**(d - j) * rr**j for j in range(d + 1)]
    ok_h &= all(member(x) and is_atom(x, member) for x in Aj) and Aj[0] * Aj[2] == Aj[1]**2
rep("h  Prop 2.6 without Dirichlet: atoms A_j = p^{d-j} r^j with A_0 A_2 = A_1^2 (q = 7, two subgroups)", ok_h)
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
