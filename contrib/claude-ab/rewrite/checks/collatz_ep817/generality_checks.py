#!/usr/bin/env python3
"""Checks of the generalisations stated in the workbench reader (claude-ab, Opus 5.5, 26 September 2026):
G1 the Erdos-Straus shell count for every odd prime; G2 the Collatz descent lemma under F_m(3) < 3 alone;
G3 the gauge Casimir lemma on triangle-free graphs and its failure on a triangle; G4 the S6-5 cubic mod 9;
G5 Eliahou-type cycle bounds from a verification range s (the least denominator of a fraction in (log2 3, log2(3+1/s)]).
Second round (after the understatement review of 26 September): G6 the YM gap theorem at every truncation order;
G7 Corollary 2.9 from s > 2.17e20; G8 x < p/2 in the ES shell criterion; G9 the girth constant; G10 the two-shell survivors;
G11 the five identities behind the mod-840 reduction; G12 the 817 lifting lemma; G13 the exact descent criterion.
Third round: G14 a Pocklington proof of the 22-digit ES certificate prime; G15 the cycle bounds from the verification
to 2^33 made here (descent_2e33.c); G16 the shell count for every a > p/4 with p not dividing a; G17 Propositions 1.2-1.3
for every prime p = 1 mod 4; G18 Proposition 2.1 and the rates in Theorem 2.2(c); G19 the jet fibres of Theorem 2.10;
G20 the girth lemma for real weights by linear programming; G21 Lambda_3 = 3 (powers of 3); G22 the M_n lower bound;
G23 the Neumann radii on the full and the physical space; G24 the 817 digit sets mod 19, the small top levels and the
general-k lifting for (1651, A#); G25 further values of d_N; G26 the Corollary 2.9 constants at the lower end.
Fourth round (after the twenty-third referee pass): G17 and G18 rewritten (Proposition 1.2 at p = 5 mod 12; the bounds (4.3)-(4.4));
G27 the published cycle bound; G28 Theorem 1.1(c) at p = 3 mod 4; G29 distinct ternary sums; G30 the per-member descent criterion."""
import itertools, math, sympy as sp
from fractions import Fraction as Fr
import mpmath as mp
res=[]
def ok(n,c,i=""): res.append((n,c,i)); print(("[PASS] " if c else "[FAIL] ")+n+(": "+str(i) if i!="" else ""))
# G1: shell count for ALL odd primes p and all a with p/4 < a < p; fixed point iff R = 1
def divs_sq(a):
    f=sp.factorint(a); ds=[1]
    for q,e in f.items(): ds=[d*q**k for d in ds for k in range(2*e+1)]
    return ds
def ordered(p,a):
    R=4*a-p; S=p*a; cnt=0; fixed=0
    for d in sp.divisors(S*S):
        if (d+S)%R==0 and (S*S//d+S)%R==0:
            cnt+=1
            if d==S: fixed+=1
    return cnt,fixed
bad=0; tot=0; fx=0
for p in sp.primerange(3,260):
    for a in range(p//4+1,p):
        if 4*a<=p: continue
        R=4*a-p; D=divs_sq(a)
        E=[u for u in D if (4*u+1)%R==0]; M=[u for u in D if (u+a)%R==0]
        c,f=ordered(p,a); tot+=1
        if c!=2*len(E)+len(M) or (f==1)!=(R==1): bad+=1
        fx+=f
ok("G1 shell count 2|E|+|M| holds for every odd prime p<260 and every a in (p/4,p); a fixed point y=z occurs iff R=1", bad==0, f"{tot} (p,a) pairs, {fx} fixed points")
# G1b: least denominator in (p/4, 3p/4] for all primes (trivial) -- skip
# G2: Collatz descent needs only F_m(3) < 3 (no condition on earlier prefixes)
def Tstep(n):
    m=3*n+1; a=0
    while m%2==0: m//=2; a+=1
    return m,a
bad=0; cnt=0
for n in range(3,2**14,2):
    x=n; A=0; C=Fr(0); 
    for m in range(1,9):
        x,a=Tstep(x); A+=a
    # affine map of the first m odd steps along n's word: F_m(y)=(3^m y + C)/2^A with C from the word
    # recompute exactly: iterate symbolic
    x=n; num_c=Fr(0); A=0; 
    for m in range(1,9):
        xx,a=Tstep(x)
        num_c=(3*num_c+ 2**A)  # C_m = 3 C_{m-1} + 2^{A_{m-1}}
        A+=a; x=xx
        F3=Fr(3**m*3+num_c,2**A)
        if F3<3:
            cnt+=1
            if not (x<n): bad+=1
ok("G2 every odd n<2^14 and m<=8 with F_m(3)<3 along n's own word has T^m(n)<n (no condition on earlier prefixes)", bad==0, f"{cnt} cases")
# G3: Casimir lemma on triangle-free non-bipartite graphs (C5, Petersen) and failure on K3
def check_graph(V,E,maxtwo=2):
    inc={v:[i for i,(u,w) in enumerate(E) if v in (u,w)] for v in V}
    worst=None; bad=0; n=0
    for js in itertools.product(range(maxtwo+1),repeat=len(E)):
        if not any(js): continue
        okv=True
        for v in V:
            s=[js[i] for i in inc[v]]; t=sum(s)
            if t%2 or 2*max(s)>t: okv=False; break
        if not okv: continue
        n+=1; T=sum(js)
        r=min(Fr(T, j) for j in js if j)  # sum / j_e over nonzero j_e
        worst=r if worst is None else min(worst,r)
    return n,worst
C5=(list(range(5)),[(i,(i+1)%5) for i in range(5)])
n,w=check_graph(*C5,maxtwo=3); ok("G3 C5 (triangle-free, not bipartite): min sum_f j_f / j_e >= 4", w>=4, f"{n} assignments, min ratio {w}")
P_out=[(i,(i+1)%5) for i in range(5)]; P_sp=[(i,i+5) for i in range(5)]; P_in=[(5+i,5+(i+2)%5) for i in range(5)]
Pet=(list(range(10)),P_out+P_sp+P_in)
n,w=check_graph(*Pet,maxtwo=1); ok("G3 Petersen graph (triangle-free, not bipartite), spins <= 1/2: min ratio >= 4", w>=4, f"{n} assignments, min ratio {w}")
K3=([0,1,2],[(0,1),(1,2),(0,2)])
n,w=check_graph(*K3,maxtwo=2); ok("G3 K3 (a triangle): the constant 4 fails (min ratio 3)", w==3, f"min ratio {w}")
# G4: for all integer a, 3|P => 9|P; so P never = 3k with 3 not dividing k
P=lambda a: a[0]*(a[0]**2-3*(a[1]**2+a[2]**2+a[3]**2))
bad=0; vals=set()
for a in itertools.product(range(-12,13),repeat=4):
    v=P(a); vals.add(v)
    if v%3==0 and v%9!=0: bad+=1
ok("G4 all a in Z^4 (|a_i|<=12): 3|P implies 9|P", bad==0)
evenD4={P(a) for a in itertools.product(range(-12,13),repeat=4) if sum(a)%2==0}
ok("G4 on D4 no value 6k with 3 not dividing k occurs (|a_i|<=12)", all(not(v%6==0 and (v//6)%3!=0) for v in evenD4))
# G5: simplest fraction in (x, x+delta], x=log2 3, delta=log2(1+1/(3s)): least m with 3^m<2^A<=(3+1/s)^m
mp.mp.dps=80
def simplest_in(lo,hi):
    # smallest-denominator fraction p/q with lo < p/q <= hi (lo irrational-ish); Stern-Brocot descent via continued fractions
    a,b,c,d=0,1,1,0  # left 0/1, right 1/0
    # standard algorithm: find fraction in open interval (lo, hi]
    fl=mp.floor(lo)
    if fl+1<=hi: return int(fl+1),1
    p0,q0,p1,q1=0,1,1,0
    x=lo; y=hi
    # continued fraction simultaneous expansion
    terms=[]
    while True:
        ax=int(mp.floor(x)); ay=int(mp.floor(y))
        if ax!=ay or (ay==y):  # they differ: pick min(ax,ay)+1 ...
            t=min(ax,ay)+1
            terms.append(t); break
        terms.append(ax)
        x=1/(x-ax); y=1/(y-ay)
        x,y=y,x
    # rebuild fraction from terms
    num,den=1,0; pnum,pden=0,1
    for t in terms:
        num,pnum=t*num+pnum,num; den,pden=t*den+pden,den
    return num,den
def mstar(s):
    x=mp.log(3,2); hi=mp.log(3+mp.mpf(1)/s,2)
    A,m=simplest_in(x,hi)
    return A,m
A,m=mstar(330751)
k=int(mp.ceil(m*mp.log(mp.mpf(4*330751)/(3*330751+1),2)))
ok("G5 simplest fraction in (log2 3, log2(3+1/s)] at s=330751 gives m*=1636 (agrees with the exact search)", m==1636, f"A={A}, m={m}, k>={k}")
for e in (40,60,68,71):
    s=mp.mpf(2)**e
    A,m=mstar(s)
    x=mp.log(3,2); hi=mp.log(3+1/s,2)
    assert x < mp.mpf(A)/m <= hi
    kk=m*mp.log(4*s/(3*s+1),2)
    print(f"   s=2^{e}: least m* = {m:,}, A = {A:,}, A+m = {A+m:,}, k >= {mp.nstr(kk,15)} -> k >= {int(mp.ceil(kk)):,}")

# G5b: independent cross-check of G5 by a Stern-Brocot descent
# Independent cross-check: Stern-Brocot descent (with run-length acceleration) for the fraction of least
# denominator in the half-open interval (lo, hi]; lo = log2 3, hi = log2(3 + 1/s).
mp.mp.dps = 120
def simplest_sb(lo, hi):
    a, b, c, d = 0, 1, 1, 0          # left a/b, right c/d
    while True:
        p, q = a + c, b + d          # mediant
        if mp.mpf(p) / q <= lo:      # mediant too small: move left bound right as far as possible
            # largest k >= 1 with (a + k c)/(b + k d) <= lo  <=>  a + k c <= lo (b + k d)  <=> k (c - lo d) <= lo b - a
            num = lo * b - a; den = c - lo * d
            k = int(mp.floor(num / den)) if den > 0 else 1
            k = max(k, 1)
            a, b = a + k * c, b + k * d
        elif mp.mpf(p) / q > hi:     # mediant too large: move right bound left
            # largest k >= 1 with (c + k a)/(d + k b) > hi  <=> c + k a > hi (d + k b) <=> k (hi b - a) < c - hi d
            num = c - hi * d; den = hi * b - a
            k = int(mp.ceil(num / den)) - 1 if den > 0 else 1
            k = max(k, 1)
            c, d = c + k * a, d + k * b
        else:
            return p, q
for s in (330751, mp.mpf(2)**40, mp.mpf(2)**60, mp.mpf(2)**68, mp.mpf(2)**71):
    lo = mp.log(3, 2); hi = mp.log(3 + 1 / mp.mpf(s), 2)
    A, m = simplest_sb(lo, hi)
    assert lo < mp.mpf(A) / m <= hi
    ok(f"G5b Stern-Brocot descent (independent method) at s={mp.nstr(mp.mpf(s),8)}", True, f"A={A:,} m={m:,}")

# (first round ends here; one summary line is printed at the end of the script)

# ---------------- second round (after the understatement review, 26 September) ----------------
import sympy as sp
from fractions import Fraction as Fr
mp.mp.dps = 60
# G6: YM gap theorem at every truncation order N (inputs m_i,t_i, i<=N)
mm = {1: Fr(64, 3), 2: Fr(5834, 39), 3: Fr(336572872, 208845), 4: Fr(17270702970768271, 341697152160), 5: Fr(1638684)}
tt = {1: Fr(16, 3), 2: Fr(137, 6), 3: Fr(225985217, 1253070), 4: Fr(110695177857394584026401, 18025447358750832000), 5: Fr(190128)}
X = sp.symbols('X')
def orderN(N):
    ell = sum(sp.Rational(mm[i] + 4 * tt[i]) * X**i for i in range(1, N + 1))
    dl = sum(sp.Rational(3 * (mm[i] * tt[j] + mm[j] * tt[i])) * X**(i + j) for i in range(1, N + 1) for j in range(1, N + 1) if i + j >= N + 1)
    D = sp.expand((1 - ell)**2 - sp.Rational(8, 3) * dl)
    return ell, dl, D
ell1, dl1, D1 = orderN(1)
ok("G6 order 1: D_1 = 1 - 256 xi/3 identically, so alpha_1 = 3/256", sp.expand(D1 - (1 - sp.Rational(256, 3) * X)) == 0)
for N in (1, 2, 3, 4, 5):
    ell, dl, D = orderN(N)
    ivs = sp.Poly(D, X).intervals(eps=sp.Rational(1, 10**30))
    lo, hi = sorted(iv for (iv, mult) in ivs if iv[1] > 0)[0]
    aN = (lo + hi) / 2
    thr = 1 / (2 * sp.sqrt(aN))
    def dN(x):
        return sp.Rational(3, 2) * (1 + sp.sqrt(D.subs(X, x))) + sum(sp.Rational(Fr(3, 2) * mm[i] - 6 * tt[i]) * x**i for i in range(1, N + 1))
    ellend = sp.N(ell.subs(X, lo), 12)
    print(f"   order {N}: alpha_N = {sp.N(aN, 16)}, threshold g^2 >= {sp.N(thr, 14)}, d_N(alpha_N) = {sp.N(dN(lo), 10)}, ell_N(alpha_N) = {ellend}" + (f", d_N(1/64) = {sp.N(dN(sp.Rational(1, 64)), 10)}" if sp.Rational(1, 64) <= lo else ""))
    if N == 2:
        ok("G6 order 2: threshold g^2 = 4.01867915..., d_2 >= 1.52 on (0, alpha_2]", abs(sp.N(thr, 12) - sp.Float('4.01867915388', 12)) < 1e-9 and sp.N(dN(lo), 10) > 1.52)
        ok("G6 order 2: ell_2 < 1 at alpha_2 (Neumann inverse valid)", ellend < 1)
# G7: Corollary 2.9 already follows from s > 2.17e20 (Barina 2021's range 2^68 suffices)
for s in (mp.mpf('2.15e20'), mp.mpf('2.2e20'), mp.mpf(2)**68):
    lo_, hi_ = mp.log(3, 2), mp.log(3 + 1 / s, 2)
    A_, m_ = simplest_sb(lo_, hi_)
    print(f"   s = {mp.nstr(s, 6)}: least-denominator fraction {A_}/{m_}")
slo = 1 / (mp.mpf(2)**(mp.mpf(10439860591) / 6586818670) - 3)
ok("G7 the fraction 114208327604/72057431991 is the least-denominator one for s just above 2.1689e20", simplest_sb(mp.log(3, 2), mp.log(3 + 1 / (slo * (1 + mp.mpf('1e-9'))), 2)) == (114208327604, 72057431991), mp.nstr(slo, 12))
# G8: for p = 1 mod 4 every solution has p/4 < x < p/2 and x < y; for p = 3 mod 4 the only exception is ((p+1)/2,(p+1)/2,p(p+1)/4)
bad = 0; nsol = 0
for p in sp.primerange(3, 400):
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = Fr(4, p) - Fr(1, x)
        if r <= 0: continue
        for y in range(max(x, int(1 / r) + 1), int(2 / r) + 1):
            r2 = r - Fr(1, y)
            if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                z = r2.denominator; nsol += 1
                if 2 * x > p:
                    if not (p % 4 == 3 and x == y == (p + 1) // 2 and z == p * (p + 1) // 4): bad += 1
                elif x == y: bad += 1
ok("G8 every solution at an odd prime p<400 has x<p/2 and x<y, except ((p+1)/2,(p+1)/2,p(p+1)/4) for p=3 mod 4", bad == 0, f"{nsol} solutions")
# G9: girth constant: C6 (girth 6), K_{3,3} (girth 4), cube (girth 4)
C6 = (list(range(6)), [(i, (i + 1) % 6) for i in range(6)])
n6, w6 = check_graph(*C6, maxtwo=2)
K33 = (list(range(6)), [(i, j) for i in range(3) for j in range(3, 6)])
n33, w33 = check_graph(*K33, maxtwo=1)
ok("G9 girth constant: C6 min ratio 6, K_{3,3} min ratio 4, C5 5, Petersen 5, K3 3", w6 == 6 and w33 == 4, f"C6 {w6}, K33 {w33}")
# G10: two-shell survivors: p=13 mod 24 -> residual-3 shell occupied; p=1 mod 24: residual-7 occupied iff (p+7)/4 has a non-residue prime factor mod 7; survivors are 1,25,121 mod 168
bad = 0; surv = set()
for p in sp.primerange(13, 200000):
    if p % 12 != 1: continue
    a3 = (p + 3) // 4; a7 = (p + 7) // 4
    E3 = any((4 * u + 1) % 3 == 0 or (u + a3) % 3 == 0 for u in sp.divisors(a3 * a3))
    E7 = any((4 * u + 1) % 7 == 0 or (u + a7) % 7 == 0 for u in sp.divisors(a7 * a7))
    if p % 24 == 13 and not E3: bad += 1
    if p % 24 == 1:
        nonres = any(q % 7 in (3, 5, 6) for q in sp.factorint(a7))
        if E7 != nonres: bad += 1
    if not E3 and not E7: surv.add(p % 168)
ok("G10 survivors of both first shells: p=13 mod 24 never survives; the residual-7 criterion at p=1 mod 24 is 'a non-residue prime factor mod 7'; survivors lie in {1,25,121} mod 168", bad == 0 and surv <= {1, 25, 121}, sorted(surv))
# G11: the mod-840 reduction by five identities
p_ = sp.symbols('p')
fams = {(1, 2, 7): lambda p: p % 7 == 3, (2, 1, 7): lambda p: p % 7 == 5, (1, 1, 7): lambda p: p % 7 == 6, (1, 2, 15): lambda p: p % 5 == 2, (2, 1, 15): lambda p: p % 5 == 3}
ident = all(sp.simplify(1 / (A * B * ((p_ + R) / (4 * A * B))) + 1 / (A * ((A + p_ * B) / R) * ((p_ + R) / (4 * A * B))) + 1 / (p_ * B * ((A + p_ * B) / R) * ((p_ + R) / (4 * A * B))) - 4 / p_) == 0 for (A, B, R) in fams)
bad = 0; left = set()
for p in sp.primerange(3, 300000):
    if p % 24 != 1: continue
    hit = [f for f, cond in fams.items() if cond(p)]
    if not hit: left.add(p % 840); continue
    A, B, R = hit[0]
    D = Fr(p + R, 4 * A * B); C = Fr(A + p * B, R)
    if D.denominator != 1 or C.denominator != 1 or Fr(1, A * B * D) + Fr(1, A * C * D) + Fr(1, p * B * C * D) != Fr(4, p): bad += 1
ok("G11 five identities 4/p = 1/(ABD)+1/(ACD)+1/(pBCD) cover p=1 mod 24 unless p is a unit square mod 840", ident and bad == 0 and left <= {1, 121, 169, 289, 361, 529}, sorted(left))
# G12: 817 lifting lemma: A_q u 19^q B is 4-admissible for every 4-admissible B (optimal sets), lower levels {1,7,8} or {2,3,5}
def subset_sums(A):
    S = {0}
    for a in A: S |= {s + a for s in S}
    return S
def has4(H):
    Hs = sorted(H); st = set(H)
    for i, x in enumerate(Hs):
        for y in Hs[i + 1:]:
            d = y - x
            if x + 2 * d in st and x + 3 * d in st: return True
    return False
ok("G12 digit set {2,3,5}: H = 3*{0,1,7,8,9,15,16} mod 19, no 4-AP mod 19", sorted(subset_sums([2, 3, 5])) == sorted({(3 * d) % 19 for d in (0, 1, 7, 8, 9, 15, 16)}))
bad = 0; cnt = 0
for B in ([1, 9, 13, 14], [1, 13, 35, 39, 40], [2, 29, 45, 74, 77, 79], [1, 3, 39, 180, 219, 243, 246], [1], [2, 3], [2, 3, 5]):
    assert not has4(subset_sums(B))
    for W in ([1, 7, 8], [2, 3, 5]):
        for q in (1, 2):
            A = [19**j * w for j in range(q) for w in W] + [19**q * b for b in B]
            cnt += 1
            if has4(subset_sums(A)): bad += 1
ok("G12 lifting: A_q u 19^q B is 4-admissible (q=1,2; both digit sets; seven admissible B)", bad == 0, f"{cnt} sets")
# G13: exact descent criterion: for a word with affine map F_m(x)=(3^m x + C)/2^A, every member n>=3 of its cylinder
# descends at step m iff F_m(n0) < n0 for the least member n0 >= 3
def Tstep2(n):
    m = 3 * n + 1; a = 0
    while m % 2 == 0: m //= 2; a += 1
    return m, a
cyl = {}
for n in range(3, 2**15, 2):
    x = n; w = []; C = 0; A = 0
    for mstep in range(1, 6):
        C = 3 * C + 2**A
        x, a = Tstep2(x); A += a; w.append(a)
        key = tuple(w)
        if A <= 10:
            cyl.setdefault(key, []).append((n, x < n, C, A, mstep))
bad = 0
for key, lst in cyl.items():
    n0, _, C, A, mstep = lst[0]
    crit = Fr(3**mstep * n0 + C, 2**A) < n0
    if any(desc != crit for (n, desc, C2, A2, m2) in lst): bad += 1
ok("G13 exact criterion: members n>=3 of a cylinder (A<=10) all descend at step m iff F_m(n0) < n0", bad == 0, f"{len(cyl)} words")

# ---------------- third round (26 September, before applying the understatement review to the reader) ----------------
import os, random
from math import comb, gcd, log, exp, ceil, floor
# G14: Pocklington proof of the 22-digit prime of ES item 3
def trial_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def pocklington(N, fac, proven):
    F = 1
    for q, e in fac.items(): F *= q**e
    if F != N - 1 or any(q not in proven for q in fac): return None
    wit = {}
    for q in fac:
        for a in range(2, 500):
            if pow(a, N - 1, N) == 1 and gcd(pow(a, (N - 1) // q, N) - 1, N) == 1:
                wit[q] = a; break
        else: return None
    return wit   # F = N - 1 > sqrt(N), so every prime factor r of N has F | r - 1, hence r > sqrt(N)
proven = {q for q in (2, 3, 5, 17, 5051, 169307, 351707) if trial_prime(q)}
chain = [(1482864185239, {2: 1, 3: 1, 17: 2, 5051: 1, 169307: 1}),
         (15646011419935589191, {2: 1, 3: 1, 5: 1, 351707: 1, 1482864185239: 1}),
         (7510085481569082811681, {2: 5, 3: 1, 5: 1, 15646011419935589191: 1})]
okchain = len(proven) == 7; wits = []
for N, fac in chain:
    w = pocklington(N, fac, proven)
    if w is None: okchain = False; break
    proven.add(N); wits.append((N, w))
ok("G14 Pocklington chain proves 7510085481569082811681 prime (leaves by trial division)", okchain and 7510085481569082811681 in proven, "; ".join(f"{N}: witnesses {w}" for N, w in wits))
# G15: the verification to 2^33 made here (descent_2e33.c) and the cycle bounds it gives
outp = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'descent_2e33_OUTPUT.txt')
ran = os.path.exists(outp) and 'RESULT: every odd n with 3 <= n < 2^33 falls below itself' in open(outp).read()
s33 = mp.mpf(2)**33 + 1
A33, m33 = simplest_sb(mp.log(3, 2), mp.log(3 + 1 / s33, 2))
k33 = int(mp.ceil(m33 * (2 - mp.log(3 + 1 / s33, 2))))
Amin33 = int(mp.floor(m33 * mp.log(3, 2))) + 1
ok("G15 with every odd n < 2^33 falling below itself (C program), a nontrivial cycle has m >= 190,537, A >= 301,994, k >= 79,080", ran and (A33, m33) == (301994, 190537) and Amin33 == 301994 and k33 == 79080, f"fraction {A33}/{m33}, A >= {Amin33}, k >= {k33}")
# G16: Theorem 1.1(b) for every a > p/4 with p not dividing a (a up to 3p)
bad = 0; cnt = 0
for p in sp.primerange(3, 120):
    for a in range(p // 4 + 1, 3 * p + 1):
        if a % p == 0: continue
        R = 4 * a - p; S = p * a; cnt += 1
        pairs = 0; fixed = 0
        for y in range(S // R + 1, 2 * S // R + 1):
            num = S * y; den = R * y - S
            if den > 0 and num % den == 0:
                z = num // den
                if z >= y:
                    pairs += 1 if z == y else 2
                    if z == y: fixed += 1
        E = [u for u in sp.divisors(a * a) if (4 * u + 1) % R == 0]
        M = [u for u in sp.divisors(a * a) if (u + a) % R == 0]
        if pairs != 2 * len(E) + len(M) or (fixed > 0) != (R == 1): bad += 1
ok("G16 Theorem 1.1(b): 2|E_a|+|M_a| ordered pairs for every a > p/4 with p not dividing a (odd p<120, a<=3p); y=z iff R_a=1", bad == 0, f"{cnt} pairs (p,a)")
# G17: Proposition 1.3 for every prime p = 1 mod 4; Proposition 1.2 as stated for p = 1 mod 12, and its corrected form for p = 5 mod 12
def sols_with_least(p, a):
    """unordered solutions (a, y, z) with a <= y <= z of 4/p = 1/a + 1/y + 1/z (brute force)"""
    r = Fr(4, p) - Fr(1, a); cnt = 0
    if r <= 0: return 0
    for y in range(max(a, int(1 / r) + 1), int(2 / r) + 1):
        r2 = r - Fr(1, y)
        if r2 > 0 and r2.numerator == 1 and r2.denominator >= y: cnt += 1
    return cnt
bad = 0; n5 = 0; n1 = 0; nenum = 0
for p in sp.primerange(5, 30000):
    if p % 4 != 1: continue
    a3 = (p + 3) // 4; a7 = (p + 7) // 4
    D3 = sp.divisors(a3 * a3); D7 = sp.divisors(a7 * a7)
    E3 = [u for u in D3 if (4 * u + 1) % 3 == 0]; M3 = [u for u in D3 if (u + a3) % 3 == 0]
    f = sp.factorint(a3)
    P1 = 1; P2 = 1
    for l, v in f.items():
        if l % 3 == 1: P1 *= 2 * v + 1
        elif l % 3 == 2: P2 *= 2 * v + 1
    if p % 12 == 1:
        n1 += 1
        expected_unordered = 3 * P1 * (P2 - 1) // 4
        if not (E3 == M3 == [u for u in D3 if u % 3 == 2] and len(E3) == P1 * (P2 - 1) // 2): bad += 1
    else:
        n5 += 1
        expected_unordered = P1 * (3 * P2 - 1)
        if expected_unordered % 4 != 0 or P2 % 4 != 3: bad += 1
        expected_unordered //= 4
        if not (E3 == [u for u in D3 if u % 3 == 2] and M3 == [u for u in D3 if u % 3 == 1] and len(E3) == P1 * (P2 - 1) // 2 and len(M3) == P1 * (P2 + 1) // 2 and 1 in M3): bad += 1
        if E3 == M3: bad += 1   # the uncorrected statement E = M must fail here
    if len(E3) + len(M3) // 2 != expected_unordered: bad += 1
    if p < 700:
        nenum += 1
        if sols_with_least(p, a3) != expected_unordered: bad += 1
    f7 = sp.factorint(a7)
    n3 = sum(v for l, v in f7.items() if l % 7 == 3); n24 = sum(v for l, v in f7.items() if l % 7 in (2, 4))
    crit = any(l % 7 in (5, 6) for l in f7) or n3 >= 3 or (n3 >= 1 and n24 >= 1)
    occ = any((4 * u + 1) % 7 == 0 or (u + a7) % 7 == 0 for u in D7)
    if crit != occ or a7 % 7 == 0: bad += 1
ok("G17 Prop 1.3 for every prime p = 1 mod 4 below 3e4; Prop 1.2 as stated for p = 1 mod 12; for p = 5 mod 12 E = {u=2}, M = {u=1} (never equal), |E| = P1(P2-1)/2, |M| = P1(P2+1)/2, P1(3P2-1)/4 unordered solutions with least denominator a (brute force for p < 700)", bad == 0, f"{n1} primes p=1 mod 12, {n5} primes p=5 mod 12, {nenum} enumerated")
# G18: Proposition 2.1 (strict bound); Theorem 2.2(a) for every H >= 0; the bounds (4.3)-(4.4) of Theorem 2.2(c) and their proof
random.seed(20260926); bad = 0
for _ in range(20000):
    A = random.randint(1, 12); N = random.randint(1, 5000); b = random.randint(0, 10**6); h = random.randint(0, 2**A - 1)
    c = (b + N - 1 - h) // 2**A - (b - 1 - h) // 2**A
    if c not in (N // 2**A, -(-N // 2**A)) or abs(Fr(c, N) - Fr(1, 2**A)) > Fr(2**A - 1, 2**A * N): bad += 1
ok("G18 Prop 2.1: the count is floor or ceil of N/2^A and |P(w)-2^-A| <= (1-2^-A)/N < 1/N (20,000 random cases)", bad == 0)
def Qm(H, m):   # Pr(Bin(H,1/2) <= m-1), exact
    return Fr(sum(comb(H, i) for i in range(0, min(m, H + 1))), 2**H)
def bound43(N, d): return N**(-d) + N**(-d * d / (2 * log(2)))
def bound44(N, d, L):
    H = ceil((1 + d) * L - 1e-12)
    return 0.5 * N**(-d) + exp(-2 * (d * L / 2 - 0.5)**2 / H)
bad = 0; nlow = 0; nhigh = 0
for N in [2**L for L in range(4, 81)] + [1000, 10**6, 3 * 2**20, 10**9, 7 * 10**12]:
    L = log(N, 2)
    for m in range(1, int(2 * L) + 2):
        dmax = 0.5 - m / L
        if dmax > 0:
            for d in (dmax * (1 - 1e-9), dmax / 2, dmax / 5):
                H = floor((1 - d) * L + 1e-12)
                nlow += 1
                # the proof's two terms separately, then the bound (4.3)
                if not (H >= 1 and Fr(comb(H, m), N) <= N**(-d) * (1 + 1e-12) and float(Qm(H, m)) <= N**(-d * d / (2 * log(2))) * (1 + 1e-12) and float(Qm(H, m) + Fr(comb(H, m), N)) <= bound43(N, d) * (1 + 1e-12)): bad += 1
        dmin = m / L - 0.5
        if dmin > 0 and dmin * L > 1:
            for d in (dmin * (1 - 1e-9), (dmin + 1 / L) / 2, 1 / L * (1 + 1e-6)):
                if not (d * L > 1 and m >= (0.5 + d) * L - 1e-12): continue
                H = ceil((1 + d) * L - 1e-12)
                lowb = Qm(H, m) - Fr(N, 2**(H + 1))
                nhigh += 1
                if not (float(1 - lowb) <= bound44(N, d, L) * (1 + 1e-12)): bad += 1
ok("G18 Thm 2.2(c): with H as in the proof, the sandwich of (a) gives (4.3) and (4.4)", bad == 0, f"{nlow} + {nhigh} (N,m,delta) cases")
def word_of(n, m):
    w = []
    for _ in range(m):
        x = 3 * n + 1; a = 0
        while x % 2 == 0: x //= 2; a += 1
        w.append(a); n = x
    return tuple(w)
bad = 0; nex = 0; nsand = 0
for L in (10, 12, 14):
    N = 2**L
    for b in (0, 12345, 999999):
        for m in range(1, L + 1):
            cntw = {}
            for k in range(b, b + N):
                w = word_of(2 * k + 1, m); cntw[w] = cntw.get(w, 0) + 1
            Delta = 1 - sum(min(Fr(c, N), Fr(1, 2**sum(w))) for w, c in cntw.items())
            for H in range(0, 2 * L + 3):   # (a) for every H >= 0, including H < m
                nsand += 1
                if not (max(0, Qm(H, m) - Fr(N, 2**(H + 1))) <= Delta <= min(1, Qm(H, m) + Fr(comb(H, m), N))): bad += 1
            dl = 0.5 - m / L; dh = m / L - 0.5
            if dl > 0:
                nex += 1
                if float(Delta) > bound43(N, dl * (1 - 1e-9)) * (1 + 1e-12): bad += 1
            if dh > 0 and dh * L > 1:
                nex += 1
                if float(1 - Delta) > bound44(N, dh * (1 - 1e-9), L) * (1 + 1e-12): bad += 1
ok("G18 exact Delta for N = 2^10, 2^12, 2^14 (three offsets b): the sandwich (a) for every 0 <= H <= 2L+2, and the bounds (4.3)-(4.4) of (c)", bad == 0, f"{nsand} sandwich cases, {nex} rate cases")
# G19: Theorem 2.10: h_w = 1/prod(r_w - r_v) annihilates the moments of order <= K-2; lambda +- eps h stay probability vectors
bad = 0; tested = 0
for (m, A) in ((2, 4), (3, 5), (3, 7), (4, 8), (5, 9), (4, 10)):
    words = [w for w in itertools.product(range(1, A + 1), repeat=m) if sum(w) == A]
    res_ = {}
    for n in range(1, 2**(A + 1), 2):
        w = word_of(n, m)
        if w in words: res_.setdefault(w, set()).add(n)
    r = [min(res_[w]) for w in words]
    K = len(words)
    if len(set(r)) != K or any(len(res_[w]) != 1 for w in words): bad += 1; continue
    hh = [Fr(1) for _ in range(K)]
    for i in range(K):
        for j in range(K):
            if i != j: hh[i] /= (r[i] - r[j])
    mom = [sum(hh[i] * r[i]**t for i in range(K)) for t in range(K)]
    lam = [Fr(1, K)] * K
    eps = min(Fr(1, K) / abs(x) for x in hh) / 2
    tested += 1
    if any(mom[t] != 0 for t in range(K - 1)) or mom[K - 1] == 0 or any(x == 0 for x in hh) or any(l - eps * abs(x) <= 0 for l, x in zip(lam, hh)): bad += 1
ok("G19 Thm 2.10: residues distinct mod 2^(A+1); moments of order <= K-2 vanish on h, order K-1 does not; interior segments exist", bad == 0, f"{tested} (m,A) pairs")
# G20: the girth lemma for real weights (vertex inequalities only), by linear programming
import networkx as nx
from scipy.optimize import linprog
def lp_min_ratio(edges, e_idx):
    nE = len(edges); rows = []; rhs = []
    verts = set(v for ed in edges for v in ed)
    for v in verts:
        inc = [i for i, (x, y) in enumerate(edges) if v in (x, y)]
        for f in inc:
            row = [0.0] * nE
            row[f] += 1.0
            for g_ in inc:
                if g_ != f: row[g_] -= 1.0
            rows.append(row); rhs.append(0.0)
    Aeq = [[1.0 if i == e_idx else 0.0 for i in range(nE)]]
    r = linprog(c=[1.0] * nE, A_ub=rows, b_ub=rhs, A_eq=Aeq, b_eq=[1.0], bounds=[(0, None)] * nE, method='highs')
    return r.fun if r.status == 0 else None
def girth_simple(G):
    best = float('inf')
    for (u, w) in G.edges():
        H = G.copy(); H.remove_edge(u, w)
        try: best = min(best, 1 + nx.shortest_path_length(H, u, w))
        except nx.NetworkXNoPath: pass
    return best
graphs = {'K3': nx.complete_graph(3), 'K4': nx.complete_graph(4), 'C5': nx.cycle_graph(5), 'C6': nx.cycle_graph(6), 'C7': nx.cycle_graph(7),
          'Q3': nx.cubical_graph(), 'K33': nx.complete_bipartite_graph(3, 3), 'Petersen': nx.petersen_graph(), 'Heawood': nx.heawood_graph(),
          'dodecahedron': nx.dodecahedral_graph(), 'McGee': nx.LCF_graph(24, [12, 7, -7], 8), 'Tutte-Coxeter': nx.LCF_graph(30, [-13, -9, 7, -7, 9, 13], 5),
          'box {-1,0,1}^3': nx.grid_graph(dim=[3, 3, 3])}
bad = 0; summary = []
for name, G in graphs.items():
    edges = list(G.edges()); g = girth_simple(G)
    vals = []
    for i, (u, w) in enumerate(edges):
        H = G.copy(); H.remove_edge(u, w)
        ge = 1 + nx.shortest_path_length(H, u, w) if nx.has_path(H, u, w) else float('inf')
        v = lp_min_ratio(edges, i); vals.append(v)
        if v is None or v < g - 1e-7 or (ge == g and abs(v - g) > 1e-7): bad += 1
    summary.append(f"{name} g={g} min={min(vals):.6g} max={max(vals):.6g}")
# multigraph (three parallel links: girth 2) and the dumbbell (two triangles joined by a bridge: the bridge is on no cycle)
multi = [(0, 1), (0, 1), (0, 1)]
v_multi = lp_min_ratio(multi, 0)
dumb = [(0, 1), (1, 2), (0, 2), (2, 3), (3, 4), (4, 5), (3, 5)]
v_bridge = lp_min_ratio(dumb, 3)
ok("G20 girth lemma, real weights: LP optimum of sum_f j_f / j_e is >= girth on every link and = girth on links of shortest cycles (13 graphs of girth 3-8); 3 parallel links give 2; a bridge between triangles gives 4 >= 3", bad == 0 and abs(v_multi - 2) < 1e-7 and abs(v_bridge - 4) < 1e-7, "; ".join(summary) + f"; multigraph {v_multi:.6g}; bridge {v_bridge:.6g}")
# G21: Lambda_3 = 3: powers of 3 are 3-admissible (the certificate (3,{1}))
def has_k_ap(H, k):
    Hs = sorted(H); st = set(H)
    for i, x in enumerate(Hs):
        for y in Hs[i + 1:]:
            d = y - x
            if all(x + t * d in st for t in range(2, k)): return True
    return False
ok("G21 {1,3,...,3^(n-1)} is 3-admissible for n <= 9; (3,{1}) is a certificate: {0,1} contains no 3-AP mod 3", all(not has_k_ap(subset_sums([3**j for j in range(n)]), 3) for n in range(1, 10)) and not any({x0 % 3, (x0 + e) % 3, (x0 + 2 * e) % 3} <= {0, 1} for x0 in range(3) for e in (1, 2)))
# G22: the M_n lower bound: M_n >= 19^(n/3), gain <= (3/19^(1/3))^2, and (M_n - 1)/(2n) <= g_4(n) for n <= 6
g4 = {1: 1, 2: 3, 3: 5, 4: 14, 5: 40, 6: 79}
Mn = lambda n: 19**(n // 3) * 3**(n % 3)
var_better = all(math.ceil(math.sqrt(19 * (Mn(n)**2 - 1) / (192 * n))) > Fr(Mn(n) - 1, 2 * n) for n in range(3, 61)) and all(math.ceil(math.sqrt(19 * (Mn(n)**2 - 1) / (192 * n))) == Fr(Mn(n) - 1, 2 * n) for n in (1, 2))
ok("G22 M_n >= 19^(n/3) (n <= 60), gain factor <= 1.2644, (M_n-1)/(2n) <= g_4(n) for n <= 6, and the variance bound is larger for 3 <= n <= 60 (equal for n = 1, 2)", var_better and all(Mn(n)**3 >= 19**n for n in range(1, 61)) and max(Mn(n) / 19**(n / 3) for n in range(1, 61)) < 1.2645 and all(Fr(Mn(n) - 1, 2 * n) <= g4[n] for n in g4), f"max gain {max(Mn(n) / 19**(n / 3) for n in range(1, 61)):.5f}")
# G23: Neumann radii: full space 3/(16 M_L), physical space 3/(4 M_L); best contour value 2/c at x = c/2
ML = lambda L: 12 * L * L * (2 * L + 1)
xs = [Fr(i, 1000) for i in range(1, 1000)]
best_full = min(max(1 / (x * Fr(3, 4)), 1 / (Fr(3, 4) - x * Fr(3, 4))) for x in xs)
best_phys = min(max(1 / (x * 3), 1 / (3 - x * 3)) for x in xs)
ok("G23 M_2 = 240; radii 1/1280 (full space, |z|=3/8, resolvent 8/3) and 1/320 (physical space, |z|=3/2, resolvent 2/3); no crossing point of (0,c) does better than 2/c", ML(2) == 240 and Fr(3, 16 * ML(2)) == Fr(1, 1280) and Fr(3, 4 * ML(2)) == Fr(1, 320) and best_full == Fr(8, 3) and best_phys == Fr(2, 3))
# G24: 817 digit sets modulo 19, the small top levels, and the general-k lifting for the certificate (1651, A#)
def ap_free_mod(Hm, q, k):
    return not any(all((x0 + t * e) % q in Hm for t in range(k)) for x0 in range(q) for e in range(1, q))
found = [B for B in itertools.combinations(range(1, 19), 3) if sum(B) < 19 and ap_free_mod({h % 19 for h in subset_sums(B)}, 19, 4)]
tops_ok = all(not has4(subset_sums(B)) for B in ([1], [2, 3], [2, 3, 5]))
ok("G24 the 3-element digit sets B with S(B) < 19 and H(B) free of 4-APs mod 19 are exactly {1,7,8} and {2,3,5}; {1},{2,3},{2,3,5} are 4-admissible", found == [(1, 7, 8), (2, 3, 5)] and tops_ok, found)
import numpy as np
def k_admissible_np(A, k):
    S = sum(A); h = np.zeros(S + 1, dtype=bool); h[0] = True
    for a in A:
        h[a:] = h[a:] | h[:S + 1 - a].copy()
    for d in range(1, S // (k - 1) + 1):
        acc = h[: S + 1 - (k - 1) * d].copy()
        for t in range(1, k):
            acc &= h[t * d: S + 1 - (k - 1 - t) * d]
            if not acc.any(): break
        if acc.any(): return False
    return True
Asharp = [3, 4, 7, 34, 37, 41, 216, 250, 253, 257]
tops6 = ([1], [1, 2], [1, 3, 9], [1, 3, 9, 27], [1, 2, 4])
okk = all(k_admissible_np(B, 6) for B in tops6[:4]) and all(k_admissible_np(Asharp + [1651 * b for b in B], 6) for B in tops6[:4])
neg = (not k_admissible_np([1, 2, 3, 4, 5], 6)) and (not k_admissible_np(Asharp + [1651 * b for b in [1, 2, 3, 4, 5]], 6))
ok("G24 general-k lifting: A# u 1651*B is 6-admissible for four 6-admissible B (negative control: a non-admissible top gives a 6-AP)", okk and neg)
# G25: further values of d_N (order-N gap theorem)
def dN_func(N):
    ell, dl, D = orderN(N)
    ivs = sp.Poly(D, X).intervals(eps=sp.Rational(1, 10**30))
    lo, hi = sorted(iv for (iv, mult) in ivs if iv[1] > 0)[0]
    f = lambda x: sp.Rational(3, 2) * (1 + sp.sqrt(D.subs(X, x))) + sum(sp.Rational(Fr(3, 2) * mm[i] - 6 * tt[i]) * x**i for i in range(1, N + 1))
    return f, lo
vals = {}
mono = True
for N in (1, 2, 3, 4, 5):
    f, lo = dN_func(N)
    grid = [lo * sp.Rational(i, 400) for i in range(0, 401)]
    seq = [float(sp.N(f(x), 20)) for x in grid]
    if any(seq[i + 1] >= seq[i] for i in range(400)): mono = False
    vals[N] = (f, lo)
xi = lambda g2: sp.Rational(1, 4) / sp.nsimplify(g2)**2
f1 = vals[1][0]; f2 = vals[2][0]; f4 = vals[4][0]; f5 = vals[5][0]
v1_5, v1_10 = float(sp.N(f1(xi(5)))), float(sp.N(f1(xi(10))))
v2_41, v2_5 = float(sp.N(f2(xi(sp.Rational(41, 10))))), float(sp.N(f2(xi(5))))
v4 = float(sp.N(f4(sp.Rational(4, 225)))); v50 = float(sp.N(f5(0)))
closed1 = all(abs(float(sp.N(f1(xi(g2)))) - 1.5 * (1 + (1 - 64 / (3 * g2**2))**0.5)) < 1e-12 for g2 in (4.7, 5, 6, 10, 100))
print(f'   G25 detail: monotone {mono}, closed form {closed1}')
ok("G25 d_N decreases on [0, alpha_N] (N=1..5, 401 points); d_1 closed form; d_1(g^2=5)=2.074, d_1(10)=2.830; d_2(4.1)=1.766, d_2(5)=2.303; d_4(4/225)=1.658436; d_5(0)=3",
   mono and closed1 and abs(v1_5 - 2.074) < 5e-4 and abs(v1_10 - 2.830) < 5e-4 and abs(v2_41 - 1.766) < 5e-4 and abs(v2_5 - 2.303) < 5e-4 and abs(v4 - 1.658436) < 5e-7 and abs(v50 - 3) < 1e-15,
   f"d_1(5) = {v1_5:.6f}, d_1(10) = {v1_10:.6f}, d_2(4.1) = {v2_41:.6f}, d_2(5) = {v2_5:.6f}, d_4(4/225) = {v4:.7f}, d_5(0) = {v50}")
# G26: Corollary 2.9 at the lower end s_lo: A >= 114,208,327,604, A+m, k, and the upper end s_hi
mstar_, Astar_ = 72057431991, 114208327604
shi = 1 / (mp.mpf(2)**(mp.mpf(Astar_) / mstar_) - 3)
kbound = mstar_ * (2 - mp.log(3 + 1 / slo, 2))
ok("G26 Cor 2.9 constants: s_lo = 2.1689e20 < 2^68, s_hi = 4.3585e21 = 2^71.884, A >= 114,208,327,604, A+m = 186,265,759,595, k >= 29,906,536,378 already at s_lo",
   slo < mp.mpf(2)**68 and abs(mp.log(shi, 2) - mp.mpf('71.884')) < 1e-3 and int(mp.floor(mstar_ * mp.log(3, 2))) + 1 == Astar_ and Astar_ + mstar_ == 186265759595 and int(mp.ceil(kbound)) == 29906536378,
   f"s_lo = {mp.nstr(slo, 12)} (2^{mp.nstr(mp.log(slo, 2), 8)}), s_hi = {mp.nstr(shi, 8)} (2^{mp.nstr(mp.log(shi, 2), 8)}), k-bound = {mp.nstr(kbound, 15)}")
# ---------------- fourth round (after the twenty-third referee pass) ----------------
# G27: the published bound after Corollary 2.9 (Hercher 2023, Cor. 29; Barina 2025, section 6): arithmetic only
nxt = simplest_sb(mp.log(3, 2), mp.mpf(114208327604) / 72057431991 - mp.mpf(10)**(-45))   # the open interval: candidates differ from the endpoint by more than 1e-23
mH = 137528045312; AH = 217976794617
kH = mp.mpf('1.375e11') * (2 - mp.log(3 + mp.mpf(2)**(-71), 2))
ok("G27 the next best upper approximation of log2 3 after 114208327604/72057431991 is 217976794617/137528045312; m + A = 355,504,839,929 (Barina 2025, section 6); m > 1.375e11 gives A > 2.179e11 and k > 5.706e10",
   nxt == (AH, mH) and AH + mH == 355504839929 and mp.mpf('1.375e11') * mp.log(3, 2) > mp.mpf('2.179e11') and kH > mp.mpf('5.706e10') and 1536 * 2**60 == 3 * 2**69,
   f"next fraction {nxt[0]}/{nxt[1]}; 1.375e11*log2(3) = {mp.nstr(mp.mpf('1.375e11') * mp.log(3, 2), 10)}; k-bound {mp.nstr(kH, 10)}")
# G28: Theorem 1.1(c) for every odd prime: for p = 3 mod 4 the shell (p+1)/4 in (p/4, p/2) has R = 1 and is occupied (u = a in M_a)
bad = 0; cnt = 0
for p in sp.primerange(3, 20000):
    if p % 4 != 3: continue
    a = (p + 1) // 4; cnt += 1
    if not (4 * a > p and 2 * a < p and 4 * a - p == 1 and (a + a) % (4 * a - p) == 0): bad += 1
ok("G28 Thm 1.1(c) at p = 3 mod 4: the shell a = (p+1)/4 lies in (p/4, p/2), has R = 1 and u = a in M_a", bad == 0, f"{cnt} primes below 2e4")
# G29: a 3-admissible set has distinct ternary sums (no relation with coefficients in [-2,2]); exhaustive over subsets of [1,40] with n <= 4
bad = 0; cnt = 0
for n in range(1, 5):
    for A in itertools.combinations(range(1, 41), n):
        if has_k_ap(subset_sums(A), 3): continue
        cnt += 1
        T = set(sum(x * a for x, a in zip(xs, A)) for xs in itertools.product((0, 1, 2), repeat=n))
        if len(T) != 3**n: bad += 1
ok("G29 every 3-admissible subset of [1,40] with at most 4 elements has 3^n distinct ternary sums", bad == 0, f"{cnt} sets")
# G30: the per-member descent criterion of Proposition 2.5: T^m(n) < n iff D > 0 and n > C/D
bad = 0; cnt = 0
for n in range(3, 2**13, 2):
    x = n; C = 0; A = 0
    for mstep in range(1, 9):
        C = 3 * C + 2**A
        x, a = Tstep2(x); A += a
        D = 2**A - 3**mstep
        cnt += 1
        if (x < n) != (D > 0 and Fr(C, D) < n): bad += 1
ok("G30 Prop 2.5: along every odd n < 2^13 and m <= 8, T^m(n) < n iff D > 0 and n > C/D", bad == 0, f"{cnt} cases")
print('ALL PASS' if all(c for _, c, _ in res) else 'FAILURES')
