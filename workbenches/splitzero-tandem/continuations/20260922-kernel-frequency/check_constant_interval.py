"""Integer outward intervals for the original elliptic coefficient.

Every interval is [lo/S, hi/S], S=10**90. All elementary operations
round outward by integer division. No floating-point value is a proof.
The elliptic series coefficients obey c_(n+1)/c_n=((2n+1)/(2n+2))**2.
Since these coefficients decrease, the remaining positive K tail is
at most the next term/(1-z); the E tail is at most this/(2N+1).
"""
from math import isqrt
from pathlib import Path
import json
S=10**90
class IV:
    def __init__(self,lo,hi=None): self.lo=lo; self.hi=lo if hi is None else hi
    @staticmethod
    def rat(n,d=1): return IV(n*S//d,-((-n*S)//d))
    @staticmethod
    def dec(t):
        a,b=t.split('.')
        return IV.rat(int(a+b),10**len(b))
    def __add__(a,b): return IV(a.lo+b.lo,a.hi+b.hi)
    def __sub__(a,b): return IV(a.lo-b.hi,a.hi-b.lo)
    def __mul__(a,b):
        v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi]
        return IV(min(v)//S,-((-max(v))//S))
    def __truediv__(a,b):
        if b.lo<=0: raise ValueError('Positive denominator required')
        v=[(a.lo*S,b.lo),(a.lo*S,b.hi),(a.hi*S,b.lo),(a.hi*S,b.hi)]
        return IV(min(n//d for n,d in v),max(-((-n)//d) for n,d in v))
    def sqrt(a):
        if a.lo<0: raise ValueError('Nonnegative radicand required')
        lo=isqrt(a.lo*S); h=isqrt(a.hi*S)
        return IV(lo,h+(h*h<a.hi*S))
    def out(a):
        def fmt(n):
            sign='-' if n<0 else ''; s=str(abs(n)).zfill(91)
            return sign+s[:-90]+'.'+s[-90:]
        return [fmt(a.lo),fmt(a.hi)]

ONE=IV.rat(1)
def elliptic(r,N=4096):
    z=ONE-r*r
    term=ONE; ks=ONE; es=ONE
    for n in range(1,N+1):
        term=term*z*IV.rat((2*n-1)**2,(2*n)**2)
        ks=ks+term
        es=es-term/IV.rat(2*n-1)
    nxt=term*z*IV.rat((2*N+1)**2,(2*N+2)**2)
    kt=nxt/(ONE-z); et=kt/IV.rat(2*N+1)
    return IV(ks.lo,ks.hi+kt.hi),IV(es.lo-et.hi,es.hi)

def log_positive(x,N=110):
    if x.lo<S: raise ValueError('This receiver uses x>=1')
    t=(x-ONE)/(x+ONE); t2=t*t
    term=t; sm=t
    for n in range(1,N):
        term=term*t2;sm=sm+term/IV.rat(2*n+1)
    nxt=term*t2
    tail=nxt/(IV.rat(2*N+1)*(ONE-t2))
    return IV(2*sm.lo,2*(sm.hi+tail.hi))

def root_sign(r):
    k,e=elliptic(r)
    return e-IV.rat(2)*r*k

lo=IV.dec('0.16010167095771835588').lo
hi=IV.dec('0.16010167095771835589').hi
low_test=root_sign(IV(lo));high_test=root_sign(IV(hi))
assert low_test.lo>0 and high_test.hi<0
iterations=0
while hi-lo>10**43:
    mid=(lo+hi)//2; value=root_sign(IV(mid));iterations+=1
    if value.lo>0: lo=mid
    elif value.hi<0: hi=mid
    else: raise ArithmeticError('Increase series length or precision')
r=IV(lo,hi);ks,es=elliptic(r)
# E_actual=(pi/2)*es, so the pi in the coefficient cancels exactly.
kappa=(ONE-r*r).sqrt()
ratio=es*(ONE+r)*(ONE+r)/(IV.rat(4)*r*kappa)
C=IV.rat(4)*log_positive(ratio)
eight=IV.rat(8)*C
assert IV.dec('10.83425590260233706').hi<eight.lo
assert eight.hi<IV.dec('10.83425590260233707').lo
record={'all_passed':True,'arithmetic':'Outward integer intervals with denominator10^90;4096 elliptic terms;110 logarithm terms; integer square root.',
 'starting_root_sign_low':low_test.out(),'starting_root_sign_high':high_test.out(),
 'bisection_steps':iterations,'r':r.out(),'C_boundary':C.out(),'eight_C_boundary':eight.out(),
 'proved_loose_bracket':['10.83425590260233706','10.83425590260233707'],
 'scope':'Original universal elliptic coefficient; no hypothetical zeta zero or native period evaluated.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
