from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
import json
P=Path(__file__).parent
iv=mp.iv
iv.dps=35
def I(x):
    if isinstance(x,F):return iv.mpf(x.numerator)/x.denominator
    return iv.mpf(x)
def atan_bounds(t,N):
    t=F(1,t)
    a=sum(((-1)**j)*t**(2*j+1)/F(2*j+1) for j in range(N))
    b=a+((-1)**N)*t**(2*N+1)/F(2*N+1)
    return min(a,b),max(a,b)
a,b=atan_bounds(5,64);c,d=atan_bounds(239,20)
pi=iv.mpf([str(float(16*a-4*d)),str(float(16*b-4*c))]) if False else 16*I(a)-4*I(d)
# Form interval endpoints by interval hull of exact rational bounds.
def hull(a,b):return iv.mpf([a.a,b.b])
pi=hull(16*I(a)-4*I(d),16*I(b)-4*I(c))
def KE(r,J=2048):
    z=1-I(r)**2
    cj=iv.mpf(1);zn=iv.mpf(1);ks=iv.mpf(1);es=iv.mpf(1)
    for j in range(1,J+1):
        cj*=I(F(2*j-1,2*j))**2;zn*=z
        ks+=cj*zn;es-=cj*zn/(2*j-1)
    cnext=cj*I(F(2*J+1,2*J+2))**2
    tail=cnext*zn*z/(1-z)
    ks=hull(ks,ks+tail)
    es=hull(es-tail/(2*J+1),es)
    return pi*ks/2,pi*es/2
lo=F(15,100);hi=F(17,100)
for _ in range(43):
    mid=(lo+hi)/2
    K,E=KE(mid)
    test=I(mid)*K/E-I(F(1,2))
    if test.b<0:lo=mid
    elif test.a>0:hi=mid
    else:raise RuntimeError('Insufficient interval precision for root')
r=hull(I(lo),I(hi));K,E=KE(r)
u=2/K;v=4/E
rr=(v-u)/(v+u);D=(v*v-u*u)/2;m=(v*v+u*u)/2;A=(u+v)**2/4
def f(t):
    tt=I(t)**2
    rt=D/(m+tt+iv.sqrt((u*u+tt)*(v*v+tt)))
    return iv.ln(1-rr*rt)
lower=iv.mpf(0);upper=iv.mpf(0)
intervals=[(0,1)]+[(2**j,2**(j+1)) for j in range(16)]
for start,end in intervals:
    step=F(end-start,4096)
    first=f(F(start));last=first
    for j in range(1,4097):
        new=f(F(start)+step*j)
        lower+=I(step)*last
        upper+=I(step)*new
        last=new
T=F(65536)
tail=-rr*D/(2*I(T)*(1-rr*D/(2*I(T)**2)))
integral=hull(lower+tail,upper)
logmoment=iv.ln(A)-2*iv.ln(1-rr**2)+integral
J1=2*(iv.ln(2)-1)-logmoment/2
psi0=iv.ln(4/pi);psi1=iv.ln(iv.sqrt(1-r*r)*(1+r)/(E*E))
cmax=4*(psi0-psi1);cmid=-4*(J1+1);cmin=-cmax-cmid
def rational_enclosure(x,n=10**6):
    # mpmath interval endpoints are exact dyadic tuples.
    def frac(t):
        sign,man,ex,bc=t
        return F((-1 if sign else 1)*man)*F(2)**ex
    a=frac(x._mpi_[0]);b=frac(x._mpi_[1])
    return [int(a.numerator*n//a.denominator), int(-((-b.numerator*n)//b.denominator)),n]
def prove_between(x,a,b,label):
    if not (x.a>I(a) and x.b<I(b)):raise RuntimeError(label+': '+str(x))
prove_between(cmin,F(-1354751,10**6),F(-1353893,10**6),'cmin reported enclosure')
prove_between(cmax,F(700182,10**6),F(700183,10**6),'cmax reported enclosure')
prove_between(cmid,F(653711,10**6),F(654569,10**6),'cmid reported enclosure')
prove_between(J1,F(-1163643,10**6),F(-1163427,10**6),'J1 reported enclosure')
if not (psi1+J1<-1 and psi0-1>-1):raise RuntimeError('late heat common-time endpoint signs')
receipt={'method':'Directed elementary interval arithmetic; Machin rational pi bounds;2048 elliptic terms plus full tails;43 rational bisections;4096 bins on17 intervals;explicit infinite tail.',
'mpmath':mp.__version__,'rational_root_interval':[str(lo),str(hi)],'integral_endpoint':int(T),
'rational_enclosures':{key:rational_enclosure(val) for key,val in [('log_moment',logmoment),('J1',J1),('cmax',cmax),('cmid',cmid),('cmin',cmin)]},
'status':'all incoming rational enclosures reproduced','scope':'Endpoint constants only; actual native asymptotics depend on the proved original profile and zero-law providers.'}
(P/'ROOT_SMALLEST_INTERVAL_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
