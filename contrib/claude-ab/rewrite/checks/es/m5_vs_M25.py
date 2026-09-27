# Same comparison for the m=30, K={1,6,10,15} block (labels 1,7) and the Yang-Lee model M(2,5).
import mpmath as mp, itertools
mp.mp.dps = 40
e = lambda x: mp.expjpi(2*x)
W = {1: {1:1,11:1,19:1,29:1,31:-1,41:-1,49:-1,59:-1},
     7: {7:1,13:1,17:1,23:1,37:-1,43:-1,47:-1,53:-1}}
labels=[1,7]
def G(a,tau,L=600):
    s=mp.mpc(0)
    for l in range(-L,L+1):
        c=W[a].get(l%60,0)
        if c: s+=c*l*mp.exp(2j*mp.pi*tau*mp.mpf(l*l)/120)
    return s
def eta(tau,L=400):
    s=mp.mpc(0)
    for n in range(1,L):
        c={1:1,11:1,5:-1,7:-1}.get(n%12,0)
        if c: s+=c*mp.exp(2j*mp.pi*tau*mp.mpf(n*n)/24)
    return s
def chiM25(s_,tau,L=200):
    acc=mp.mpc(0)
    for n in range(-L,L+1):
        a=20*n+5-2*s_; b=20*n+5+2*s_
        acc+=mp.exp(2j*mp.pi*tau*mp.mpf(a*a)/40)-mp.exp(2j*mp.pi*tau*mp.mpf(b*b)/40)
    return acc/eta(tau)
def rhoS(F,k,taus,n):
    rows=[];rhs=[]
    for t in taus:
        rows.append([F(j,t) for j in range(n)])
        fac=mp.power(-1j*t,k); rhs.append([F(j,-1/t)/fac for j in range(n)])
    A=mp.matrix(rows);B=mp.matrix(rhs);AH=A.H;N=AH*A
    MT=mp.zeros(n)
    for c in range(n):
        col=mp.lu_solve(N,AH*B.column(c))
        for r_ in range(n): MT[r_,c]=col[r_]
    return MT.T, mp.mnorm(A*MT-B,1)
taus=[mp.mpc('0.11','1.02'),mp.mpc('-0.23','0.97'),mp.mpc('0.31','0.95'),mp.mpc('-0.05','1.1')]
SG,rG=rhoS(lambda j,t:G(labels[j],t),mp.mpf(3)/2,taus,2)
SC,rC=rhoS(lambda j,t:chiM25(j+1,t),0,taus,2)
print('fit residuals',mp.nstr(rG,4),mp.nstr(rC,4))
print('rho_shadow(S)=',[[mp.nstr(SG[i,j],10) for j in range(2)] for i in range(2)])
print('rho_M25(S)  =',[[mp.nstr(SC[i,j],10) for j in range(2)] for i in range(2)])
TG=[mp.mpf(r*r)/120 for r in labels]; TC=[mp.mpf((5-2*s)**2)/40-mp.mpf(1)/24 for s in (1,2)]
print('T exponents shadow',[mp.nstr(x,8) for x in TG],' M(2,5)',[mp.nstr(x,8) for x in TC])
# Galois conjugates of the M(2,5) data: sigma_a acts on the 120th roots of unity (a coprime to 120)
# S entries are in Q(sqrt5)-multiples; test conj(rho_shadow) vs sigma_a(rho_M25) twisted by a scalar pair
from fractions import Fraction as Fr
def T_after(a): return [ (Fr(int(round(x*120)),120)*a) % 1 for x in TC]
best=[]
import math
for a in [x for x in range(1,120) if math.gcd(x,120)==1]:
    for perm in itertools.permutations(range(2)):
        for conj in (False,True):
            tg=[(-Fr(int(round(x*120)),120) if conj else Fr(int(round(x*120)),120))%1 for x in TG]
            tc=T_after(a)
            d=[(tg[i]-tc[perm[i]])%1 for i in range(2)]
            if d[0]==d[1]: best.append((a,perm,conj,d[0]))
print('T-level matches (a, perm, conj, twist):', best[:12], '... total', len(best))
