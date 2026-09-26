# Order-N truncations of the YM-01 analytic core, from the F26 rationals (exact where possible).
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 50
MT = [(Fr(64,3),Fr(16,3)),
      (Fr(5834,39),Fr(137,6)),
      (Fr(336572872,208845),Fr(225985217,1253070)),
      (Fr(17270702970768271,341697152160),Fr(110695177857394584026401,18025447358750832000)),
      (Fr(1638684),Fr(190128))]
def polys(N, MT=MT):
    m=[None]+[MT[i][0] for i in range(N)]; t=[None]+[MT[i][1] for i in range(N)]
    ell={i:m[i]+4*t[i] for i in range(1,N+1)}
    delta={}
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i+j>=N+1:
                delta[i+j]=delta.get(i+j,0)+3*(m[i]*t[j]+m[j]*t[i])
    p={i:Fr(3,2)*m[i]-6*t[i] for i in range(1,N+1)}
    return ell,delta,p
def ev(poly,x): return sum(mp.mpf(c.numerator)/c.denominator*x**k for k,c in poly.items())
def D(N,x,MT=MT):
    ell,delta,_=polys(N,MT); return (1-ev(ell,x))**2-mp.mpf(8)/3*ev(delta,x)
def alpha(N,MT=MT):
    # first positive root: D decreasing while ell<1; bisection
    lo=mp.mpf(0); hi=mp.mpf('0.05')
    ell,_,_=polys(N,MT)
    # shrink hi until ell<1 there
    while ev(ell,hi)>=1: hi/=2
    while D(N,hi,MT)>0: hi*=1.1
    for _ in range(200):
        mid=(lo+hi)/2
        if D(N,mid,MT)>0 and ev(ell,mid)<1: lo=mid
        else: hi=mid
    return lo
def d(N,x,MT=MT):
    _,_,p=polys(N,MT); return mp.mpf(3)/2*(1+mp.sqrt(D(N,x,MT)))+ev(p,x)
print("N  alpha_N  threshold g^2  d_N(alpha_N)  d_N(1/64)[g2=4]  d_N(4/225)[g2=15/4]  d_N(1/100)[g2=5]  signs of (3/2)m_i-6t_i")
for N in range(1,6):
    a=alpha(N); thr=1/(2*mp.sqrt(a))
    _,_,p=polys(N)
    row=[N, mp.nstr(a,15), mp.nstr(thr,15), mp.nstr(d(N,a),10)]
    for x in (mp.mpf(1)/64, mp.mpf(4)/225, mp.mpf(1)/100):
        row.append(mp.nstr(d(N,x),10) if x<=a else 'n/a (xi>alpha)')
    row.append([float(v) for v in p.values()])
    print(*row)
# exact order-1 closed form
ell,delta,p=polys(1)
print("order 1: ell =",ell," delta =",delta," p =",p)
print("order 1: D_1(x) = (1-128x/3)^2 - (8/3)(2048/3) x^2 ; check equals 1-256x/3:", all(abs(D(1,x)-(1-mp.mpf(256)/3*x))<mp.mpf(10)**-40 for x in (mp.mpf('0.001'),mp.mpf('0.005'),mp.mpf('0.0117'))))
print("alpha_1 == 3/256:", mp.nstr(alpha(1),30), mp.nstr(mp.mpf(3)/256,30), " threshold 8/sqrt(3) =", mp.nstr(8/mp.sqrt(3),20))
# order 2 with the first pass's exact (smaller) m2,t2 values would be better; the F26 values are upper bounds
# monotonicity of d_N on [0,alpha_N]
for N in range(1,6):
    a=alpha(N); xs=[a*k/400 for k in range(401)]
    vals=[d(N,x) for x in xs]
    print(f"N={N}: d_N decreasing on [0,alpha_N] (401-pt grid):", all(vals[i]>=vals[i+1] for i in range(400)), " d_N(0)=",mp.nstr(vals[0],6))
# sensitivity: orders 3,4 (and 5) doubled
import copy
for fac in (2,4,10):
    MT2=[MT[0],MT[1]]+[(m*fac,t*fac) for (m,t) in MT[2:]]
    a=alpha(5,MT2); print(f"orders 3-5 multiplied by {fac}: alpha5={mp.nstr(a,10)} threshold g^2={mp.nstr(1/(2*mp.sqrt(a)),8)} d5(1/64)={mp.nstr(d(5,mp.mpf(1)/64,MT2),8) if mp.mpf(1)/64<=a else 'n/a'}")
