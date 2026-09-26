#!/usr/bin/env python3
"""Supplement to check_all_even.py: Theorem 3 finite search vs brute-force backward
search on large sources, including members of e=6,8,10,12 families (all selectors)."""
import random, time, sys
sys.setrecursionlimit(10000)
exec(open('check_all_even.py').read().split('# ---- Theorem 3')[0].split('# ---- Lemma 1')[0])
src = open('check_all_even.py').read()
start = src.index('E_MAX = 60'); end = src.index('N3 = 400000')
exec(src[src.index('def amin'):src.index('npairs = 0')])
exec(src[start:end])
random.seed(12345)
t0=time.time(); tested=0; hit=0; es=set()
cands=[]
for s in (0,1):
    for e in (6,8,10,12):
        for b in (1,2,3):
            f=family(b,e,s)
            for v in range(0,6):
                cands.append(f['n0']+f['d']*f['Q']*v)
# random odd multiples of 3 with n=3 mod 4 in [1e7,1e12]
for _ in range(3000):
    n=random.randrange(10**7,10**12); n-= n%12; n+=3   # n=3 mod 12
    cands.append(n)
for n in cands:
    A=brute_templates(n); B=note_templates(n)
    if A!=B:
        print('MISMATCH',n,sorted(A),sorted(B)); sys.exit(1)
    tested+=1
    if A: hit+=1; es|={z[2] for z in A}
print('Theorem 3 on %d large sources (family members for e in {6,8,10,12}, b in {1,2,3}, both selectors, plus 3000 random n=3 mod 12 in [1e7,1e12]): finite search == brute force (e<=60); %d sources with templates; interior exponents seen %s; PASS; %.1fs'%(tested,hit,sorted(es),time.time()-t0))
