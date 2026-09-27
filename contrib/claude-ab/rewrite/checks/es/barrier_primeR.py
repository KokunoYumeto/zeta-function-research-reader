# For prime R = 3 mod 4 the group barrier (Result B) and the Jacobi barrier (reader Prop. 3.6) have the same hypothesis.
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
def factor(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=1
    return f
def subgroup(gens,R):
    G={1}; fr=[1]
    while fr:
        x=fr.pop()
        for g in gens:
            y=(x*g)%R
            if y not in G: G.add(y); fr.append(y)
    return G
n=diff=0
for p in range(5,1500):
    if not isprime(p) or p%4!=1: continue
    for a in range(p//4+1,p):
        R=4*a-p
        if not isprime(R): continue
        fa=factor(a); n+=1
        B=(R-1) not in subgroup([4%R]+[q%R for q in fa],R)
        J=all(pow(q,(R-1)//2,R)==1 for q in fa)
        if B!=J: diff+=1
print("prime R = 3 mod 4, shells of primes p = 1 mod 4 below 1500:",n,"; hypotheses differ:",diff)
