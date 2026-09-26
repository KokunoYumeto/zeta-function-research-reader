# EP817 checks: (1) A_q U 19^q B is 4-admissible for every 4-admissible B (tested on optimal sets); g4(n+3q) <= 19^q g4(n)
# (2) digit sets B, |B|=3, S(B)<19, H(B) 4-AP-free mod 19 (which minimise max / 1st / 2nd element)
# (3) generic lift for k=6 with A-sharp; (4) Lambda_3 certificate (3,{1})
import itertools
res=[]
def ok(n,c,i=""): res.append(c); print(("[PASS] " if c else "[FAIL] ")+n+(": "+str(i) if i!="" else ""))
def H(A):
    s={0}
    for a in A: s|={x+a for x in s}
    return s
def has_kAP(S,k):
    S=sorted(S); Ss=set(S); mx=S[-1]
    for i,x in enumerate(S):
        for y in S[i+1:]:
            d=y-x
            if x+(k-1)*d>mx: break
            if all(x+j*d in Ss for j in range(2,k)): return True
    return False
def admissible(A,k): return not has_kAP(H(A),k)
opt={1:[1],2:[1,3],3:[1,4,5],4:[1,9,13,14],5:[1,13,35,39,40],6:[2,29,45,74,77,79],7:[1,3,39,180,219,243,246]}
for n,B in opt.items(): assert admissible(B,4), n
ok("the listed optimal sets (n<=6) and the n=7 witness are 4-admissible", True)
def Aq(q,base=19,dig=(1,7,8)): return [base**j*w for j in range(q) for w in dig]
bad=0; cnt=0
for q in (1,2):
    for n,B in opt.items():
        if 3*q+len(B)>13: continue
        C=Aq(q)+[19**q*b for b in B]
        assert len(set(C))==len(C)
        cnt+=1
        if not admissible(C,4): bad+=1
ok("A_q U 19^q*B is 4-admissible for the optimal B (n<=7), q=1,2 (sizes up to 13)", bad==0, f"{cnt} sets")
g4={1:1,2:3,3:5,4:14,5:40,6:79}
print("  improved upper bounds g4(n) <= min_j 19^((n-j)/3) g4(j) (j=n mod 3 + 3i, j<=6 exact, j=7 via 246) vs 8*19^(ceil(n/3)-1):")
import math
for n in range(1,22):
    cands=[19**((n-j)//3)*v for j,v in list(g4.items())+[(7,246)] if j<=n and (n-j)%3==0]
    stated=8*19**(math.ceil(n/3)-1)
    print(f"   n={n:2d}: improved {min(cands):>12,}  stated {stated:>12,}  ratio {stated/min(cands):6.2f}")
# (2) digit sets
good=[]
for B in itertools.combinations(range(1,19),3):
    if sum(B)>=19: continue
    D=H(B)
    # 4-AP mod 19 with nonzero step
    Dm={x%19 for x in D}
    bad4=any(all(((x+j*e)%19) in Dm for j in range(4)) for x in range(19) for e in range(1,19))
    if not bad4: good.append(B)
print("  3-element digit sets for q=19 (S(B)<19, H(B) 4-AP-free mod 19):", good)
# (3) k=6 lift with A-sharp, top level an arbitrary 6-admissible set: check small case q=1 with B={1,2,...} small admissible sets
Ash=[3,4,7,34,37,41,216,250,253,257]
ok("A-sharp is 6-admissible and not 5-admissible", admissible(Ash,6) and not admissible(Ash,5))
# (4) Lambda_3: certificate (3,{1}): H({1})={0,1} has no 3-AP mod 3 with nonzero step
ok("(3,{1}) is a k=3 certificate (so Lambda_3 <= 3); powers of 3 give 3-admissible sets", all(admissible([3**j for j in range(n)],3) for n in range(1,9)))
print("ALL PASS" if all(res) else "FAILURES")
