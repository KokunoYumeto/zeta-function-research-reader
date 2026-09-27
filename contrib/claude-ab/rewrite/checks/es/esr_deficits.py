# Replays the strict-record deficit data of the Erdos-Straus archive (619 pp.), section 19
# (satellite 13_record_shell_deficit_box_conjecture.tex), from the definitions only.
#
# For p = 1 mod 4 with least occupied shell a = (p+R)/4, R = 2m+1 a safe prime, and
# a = l0 * prod l_j^{e_j} with l0 the unique quadratic non-residue prime factor mod R (exponent 1):
#   l0 = g^(2u+1), l_j = g^(2 alpha_j) mod R;  A = { sum beta_j alpha_j : |beta_j| <= e_j } in Z/m;
#   D = Z/m \ A;  odd offsets u and v = -u-1;  cover  (A+u) u (A+v) = Z/m  <=>  (D+u) n (D+v) = {}.
# Prepared by Claude (Opus 5.5) for the Erdos-Straus reader.  Needs sympy.
from sympy import factorint, isprime, primitive_root, n_order
from itertools import product

def least_shell(p):
    """least occupied shell a in (p/4, p/2) and its residual R (Theorem 3.1 of the reader)."""
    from sympy import divisors
    a = p // 4 + 1
    while 2 * a < p:
        R = 4 * a - p
        if any((4 * u + 1) % R == 0 or (u + a) % R == 0 for u in divisors(a * a)):
            return a, R
        a += 1
    return None

def dlog(x, g, R):
    y, k = 1, 0
    while y != x % R:
        y = y * g % R; k += 1
        if k > R: raise ValueError
    return k

def deficit(p, g=None):
    a, R = least_shell(p)
    assert (R - 1) % 2 == 0
    m = (R - 1) // 2
    assert isprime(R) and isprime(m), (p, R)
    if g is None:  # the archive uses g = 2 where 2 is a primitive root (R = 59, 107); else the least one
        g = 2 if n_order(2, R) == R - 1 else primitive_root(R)
    assert n_order(g, R) == R - 1, "g is not a primitive root"
    f = factorint(a)
    nonres = [l for l in f if dlog(l, g, R) % 2 == 1]
    assert len(nonres) == 1 and f[nonres[0]] == 1, (p, f, nonres)
    l0 = nonres[0]
    u = (dlog(l0, g, R) - 1) // 2
    others = [(dlog(l, g, R) // 2, e) for l, e in f.items() if l != l0]
    A = set()
    for betas in product(*[range(-e, e + 1) for _, e in others]):
        A.add(sum(b * al for b, (al, _) in zip(betas, others)) % m)
    D = sorted(set(range(m)) - A)
    v = (-u - 1) % m
    cover_missed = sorted(set(range(m)) - ({(x + u) % m for x in A} | {(x + v) % m for x in A}))
    DD = sorted({(x - y) % m for x in D for y in D})
    return dict(p=p, a=a, R=R, m=m, fac=f, l0=l0, u=u, v=v, A=sorted(A), D=D, DD=DD, missed=cover_missed)

ok = True
def check(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

rows = {}
for p in (73, 1129, 1201, 118801, 8803369, 806521):
    rows[p] = deficit(p)
for p in (73, 1129, 1201):
    check(f"p={p}: R={rows[p]['R']} safe prime, one non-residue factor {rows[p]['l0']} to exponent 1, deficit empty", rows[p]['D'] == [])
# R = 31 (p = 21169): m = 15 is composite, outside the safe-prime domain
a, R = least_shell(21169); check("p=21169: R=31, m=15 composite (outside the domain)", R == 31 and not isprime(15))

r = rows[118801]
check("p=118801: a=29715=3*5*7*283, R=59, g=2 primitive, logs (50,6,18,23)",
      r['a'] == 29715 and r['R'] == 59 and [dlog(x, 2, 59) for x in (3, 5, 7, 283)] == [50, 6, 18, 23])
check("p=118801: D={11,14,15,18}=11+{0,3}+{0,4}", r['D'] == [11, 14, 15, 18] and
      sorted({(11 + 3 * i + 4 * j) % 29 for i in (0, 1) for j in (0, 1)}) == r['D'])
check("p=118801: difference box {3r+4s: |r|,|s|<=1} injective mod 29 (9 values) and equal to D-D",
      len({(3 * i + 4 * j) % 29 for i in (-1, 0, 1) for j in (-1, 0, 1)}) == 9 and
      sorted({(3 * i + 4 * j) % 29 for i in (-1, 0, 1) for j in (-1, 0, 1)}) == r['DD'])
check("p=118801: offsets u=11, v=17, odd sheets cover Z/29", r['u'] == 11 and r['v'] == 17 and r['missed'] == [])

r = rows[8803369]
check("p=8803369: a=2200869=3^2*11^2*43*47, R=107, logs (70,22,59,66)",
      r['a'] == 2200869 and r['fac'] == {3: 2, 11: 2, 43: 1, 47: 1} and [dlog(x, 2, 107) for x in (3, 11, 43, 47)] == [70, 22, 59, 66])
check("p=8803369: D={23+42j: 0<=j<=9} in Z/53", r['D'] == sorted({(23 + 42 * j) % 53 for j in range(10)}))
check("p=8803369: D-D={42k: |k|<=9}, 19 elements (difference-proper rank one)",
      r['DD'] == sorted({(42 * k) % 53 for k in range(-9, 10)}) and len(r['DD']) == 19)
check("p=8803369: offsets {29,23}, odd sheets cover Z/53", {r['u'], r['v']} == {29, 23} and r['missed'] == [])

r = rows[806521]
check("p=806521: a=201645=3^2*5*4481, R=59, logs (50,6,21)",
      r['a'] == 201645 and r['R'] == 59 and r['fac'] == {3: 2, 5: 1, 4481: 1} and [dlog(x, 2, 59) for x in (3, 5, 4481)] == [50, 6, 21])
check("p=806521: D = {2,6,9,10,12,13,14,15,16,17,19,20,23,27} (14 points)",
      r['D'] == [2, 6, 9, 10, 12, 13, 14, 15, 16, 17, 19, 20, 23, 27])
check("p=806521: D-D = Z/29 (so no difference-proper GAP of rank <= 2: rank one needs 27 differences, "
      "rank two needs L1*L2=14, i.e. {2,7}, and 3*13=39 > 29)", len(r['DD']) == 29 and 2 * 14 - 1 == 27 and 3 * 13 > 29)
check("p=806521: offsets u=10, v=18; the odd sheets miss exactly {1,4,8,12,16,20,24,27}",
      r['u'] == 10 and r['v'] == 18 and r['missed'] == [1, 4, 8, 12, 16, 20, 24, 27])
# coordinate change: another primitive root multiplies D by a unit; emptiness, sizes and cover are invariant
for p in (118801, 8803369, 806521):
    R = rows[p]['R']
    g2 = primitive_root(R, smallest=True)
    alt = [g for g in range(2, R) if n_order(g, R) == R - 1][1]
    s = deficit(p, alt)
    check(f"p={p}: with primitive root {alt} instead of 2, |D|={len(s['D'])}, |D-D|={len(s['DD'])}, missed={len(s['missed'])} unchanged",
          len(s['D']) == len(rows[p]['D']) and len(s['DD']) == len(rows[p]['DD']) and len(s['missed']) == len(rows[p]['missed']))

# archive section 16 (satellite 07), corollary "full support and the two local targets" at p* = 8803369, R = 107
from sympy import divisors
B = {}
for r_ in range(-2, 3):
    for s_ in range(-2, 3):
        for u_ in (-1, 0, 1):
            for t_ in (-1, 0, 1):
                B.setdefault((70 * r_ + 22 * s_ + 59 * u_ + 66 * t_) % 106, []).append((r_, s_, u_, t_))
D107 = rows[8803369]['D']
check("p=8803369: |B|=96 and Z/106 \\ B = 2D = {2,20,24,42,46,60,64,82,86,104}",
      len(B) == 96 and sorted(set(range(106)) - set(B)) == sorted(2 * d for d in D107) == [2, 20, 24, 42, 46, 60, 64, 82, 86, 104])
p_, a_ = 8803369, 2200869
check("p=8803369: log_2(-1)=53 has exactly the fibres (-2,0,-1,-1),(2,0,1,1); log_2(-1/p)=60 is not in B",
      dlog(106, 2, 107) == 53 and sorted(B.get(53, [])) == [(-2, 0, -1, -1), (2, 0, 1, 1)] and
      dlog((-pow(p_, -1, 107)) % 107, 2, 107) == 60 and 60 not in B)
Dv = divisors(a_ * a_)
check("p=8803369, a=2200869, R=107: |E_a|=0 and |M_a|=2 by direct divisor count",
      sum((4 * u + 1) % 107 == 0 for u in Dv) == 0 and sum((u + a_) % 107 == 0 for u in Dv) == 2)
print("ALL PASS" if ok else "SOME CHECK FAILED")
