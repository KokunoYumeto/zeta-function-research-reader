# Eliahou-type bounds: least denominator m* of a fraction A/m in (log2 3, log2(3+1/s)].
# Staircase of best upper approximations of log2 3, with the exact s-range where each is the least-denominator fraction.
import mpmath as mp
mp.mp.dps=150
x=mp.log(3,2)
# best upper approximations = fractions p/q > x with no fraction of smaller denominator in (x, p/q].
# Generate via Stern-Brocot descent toward x, recording right endpoints (upper fractions) as they are created.
a,b,c,d=0,1,1,0
uppers=[]
for _ in range(2000):
    p,q=a+c,b+d
    if mp.mpf(p)/q < x: a,b=p,q
    else: c,d=p,q; uppers.append((p,q))
    if q>10**15: break
# keep only best upper approximations (decreasing value with increasing denominator is automatic in SB descent)
def s_max(p,q):  # fraction admissible iff p/q <= log2(3+1/s) iff s <= 1/(2^(p/q)-3)
    return 1/(mp.power(2,mp.mpf(p)/q)-3)
rows=[]
for i,(p,q) in enumerate(uppers):
    smax=s_max(p,q)
    smin=s_max(*uppers[i-1]) if i>0 else mp.mpf(0)   # least denominator for s in (smin, smax]
    rows.append((p,q,smin,smax))
print("A/m (best upper approx of log2 3)   least-denominator for s in (s_lo, s_hi]   log2 s_lo .. log2 s_hi")
for p,q,lo,hi in rows:
    if hi>2**30 and lo<2**80:
        print(f"{p}/{q}   s in ({mp.nstr(lo,8)}, {mp.nstr(hi,8)}]   log2: {mp.nstr(mp.log(lo,2) if lo>0 else 0,8)} .. {mp.nstr(mp.log(hi,2),8)}")
# Specific verification ranges
for name,s in [("Theorem 2.8 (330,751)",mp.mpf(330751)),("2^32",mp.mpf(2)**32),("2^40 (Eliahou)",mp.mpf(2)**40),("2^60",mp.mpf(2)**60),
               ("5*2^60 (Oliveira e Silva)",5*mp.mpf(2)**60),("2^68 (Barina 2021)",mp.mpf(2)**68),("2^71 (Barina 2025)",mp.mpf(2)**71)]:
    for p,q,lo,hi in rows:
        if lo< s <=hi:
            k=q*mp.log(4*s/(3*s+1),2)
            print(f"{name}: m >= {q:,}, A >= {p:,}, A+m >= {p+q:,}, 2m-A = {2*q-p:,}, k >= {int(mp.ceil(k)):,}")
            break
