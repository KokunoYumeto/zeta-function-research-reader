"""Independent outward integer certificate for the original cutoff profile."""
from pathlib import Path
from math import isqrt
from fractions import Fraction
import json
S=10**90
class IV:
    def __init__(self,lo,hi=None):self.lo=lo;self.hi=lo if hi is None else hi
    @staticmethod
    def rat(n,d=1):return IV(n*S//d,-((-n*S)//d))
    @staticmethod
    def dec(x):
        f=Fraction(x);return IV.rat(f.numerator,f.denominator)
    def __add__(a,b):return IV(a.lo+b.lo,a.hi+b.hi)
    def __sub__(a,b):return IV(a.lo-b.hi,a.hi-b.lo)
    def __mul__(a,b):
        v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi]
        return IV(min(v)//S,-((-max(v))//S))
    def __truediv__(a,b):
        if b.lo<=0:raise ArithmeticError('Positive denominator required')
        v=[(a.lo*S,b.lo),(a.lo*S,b.hi),(a.hi*S,b.lo),(a.hi*S,b.hi)]
        return IV(min(n//d for n,d in v),max(-((-n)//d) for n,d in v))
    def sqrt(a):
        if a.lo<0:raise ArithmeticError('Negative square root')
        lo=isqrt(a.lo*S);hi=isqrt(a.hi*S)
        return IV(lo,hi+(hi*hi<a.hi*S))
    def out(a):
        def fmt(n):
            sign='-' if n<0 else '';v=str(abs(n)).zfill(91)
            return sign+v[:-90]+'.'+v[-90:]
        return [fmt(a.lo),fmt(a.hi)]
ONE=IV.rat(1);TWO=IV.rat(2)
def elliptic(mu,N=512):
    term=ONE;K=ONE;E=ONE
    for n in range(1,N+1):
        term=term*mu*IV.rat((2*n-1)**2,(2*n)**2)
        K=K+term;E=E-term/IV.rat(2*n-1)
    nxt=term*mu*IV.rat((2*N+1)**2,(2*N+2)**2)
    tail=nxt/(ONE-mu)
    return IV(K.lo,K.hi+tail.hi),IV(E.lo-(tail/IV.rat(2*N+1)).hi,E.hi)
def log_ge_one(x,N=1024):
    if x.lo<S:raise ArithmeticError('Logarithm argument below one')
    z=(x-ONE)/(x+ONE);z2=z*z;term=z;sm=z
    for n in range(1,N):term=term*z2;sm=sm+term/IV.rat(2*n+1)
    tail=term*z2/(IV.rat(2*N+1)*(ONE-z2))
    return IV(2*sm.lo,2*(sm.hi+tail.hi))
def profile(mu,t=None):
    K,E=elliptic(mu)
    T=TWO*(E/((ONE-mu)*K)-ONE)
    density=log_ge_one(ONE/mu)/TWO
    J=(t if t is not None else T)*density+TWO*log_ge_one(K)
    w=mu.sqrt();r=(ONE-w)/(ONE+w)
    return T,J,density,r
def bracket(fn,lo=IV.rat(1,20).lo,hi=IV.rat(13,20).hi,width=10**35):
    start=[fn(IV(lo)).out(),fn(IV(hi)).out()]
    if not (fn(IV(lo)).hi<0 and fn(IV(hi)).lo>0):raise ArithmeticError('Initial signs')
    count=0
    while hi-lo>width:
        mid=(lo+hi)//2;v=fn(IV(mid));count+=1
        if v.hi<0:lo=mid
        elif v.lo>0:hi=mid
        else:raise ArithmeticError('Insufficient precision')
    return IV(lo,hi),count,start
P=Path(__file__).parent;D=P
incoming={'arithmetic': 'outward integer intervals, scale 10**90', 'elliptic_terms': 4096, 'log_terms': 320, 'root_sign_checks': 368, 'scope': 'universal equilibrium scalar; no native-period computation', 'profile': [{'t': '1/4', 'r_interval': ['0.3770115807295605701119299', '0.3770115807295605701119300'], 'J_interval': ['0.3111554260107038160603', '0.3111554260107038160604'], '8J_interval': ['2.48924340808563052848', '2.48924340808563052849'], 'density_interval': ['0.79314297884546354299', '0.79314297884546354300']}, {'t': '1/2', 'r_interval': ['0.2596037039315343555759644', '0.2596037039315343555759645'], 'J_interval': ['0.4720241388256574465761', '0.4720241388256574465762'], '8J_interval': ['3.77619311060525957260', '3.77619311060525957261'], 'density_interval': ['0.53136685170620172644', '0.53136685170620172645']}, {'t': '3/4', 'r_interval': ['0.1983851021302619283951793', '0.1983851021302619283951794'], 'J_interval': ['0.5872053089379657105107', '0.5872053089379657105108'], '8J_interval': ['4.69764247150372568408', '4.69764247150372568409'], 'density_interval': ['0.40210186589420914230', '0.40210186589420914231']}, {'t': '1', 'r_interval': ['0.1601016709577183558845674', '0.1601016709577183558845675'], 'J_interval': ['0.6771409939126460664419', '0.6771409939126460664420'], '8J_interval': ['5.41712795130116853153', '5.41712795130116853154'], 'density_interval': ['0.32298207997956527877', '0.32298207997956527878']}], 'initial_bracket_checks': 8, 'initial_bracket_details': [{'t': '1/4', 'endpoint': '1/10', 'required_sign': 1, 'sign_enclosure': ['0.352712102263', '0.352712102264'], 'passed': True}, {'t': '1/4', 'endpoint': '999/1000', 'required_sign': -1, 'sign_enclosure': ['-0.249874702977', '-0.249874702976'], 'passed': True}, {'t': '1/2', 'endpoint': '1/10', 'required_sign': 1, 'sign_enclosure': ['0.293894206843', '0.293894206844'], 'passed': True}, {'t': '1/2', 'endpoint': '999/1000', 'required_sign': -1, 'sign_enclosure': ['-0.499749656079', '-0.499749656078'], 'passed': True}, {'t': '3/4', 'endpoint': '1/10', 'required_sign': 1, 'sign_enclosure': ['0.235076311424', '0.235076311425'], 'passed': True}, {'t': '3/4', 'endpoint': '999/1000', 'required_sign': -1, 'sign_enclosure': ['-0.749624609180', '-0.749624609179'], 'passed': True}, {'t': '1', 'endpoint': '1/10', 'required_sign': 1, 'sign_enclosure': ['0.176258416004', '0.176258416005'], 'passed': True}, {'t': '1', 'endpoint': '999/1000', 'required_sign': -1, 'sign_enclosure': ['-0.999499562282', '-0.999499562281'], 'passed': True}]}
rows=[];tested=0
def contained(val,lo,hi):
    if not (IV.dec(lo).hi<=val.lo and val.hi<=IV.dec(hi).lo):raise ArithmeticError((val.out(),lo,hi))
for row in incoming['profile']:
    f=Fraction(row['t']);t=IV.rat(f.numerator,f.denominator)
    mu,count,signs=bracket(lambda z:TWO*(elliptic(z)[1]/((ONE-z)*elliptic(z)[0])-ONE)-t)
    _,J,density,r=profile(mu,t)
    for key,val in [('r_interval',r),('J_interval',J),('8J_interval',IV.rat(8)*J),('density_interval',density)]:
        contained(val,*row[key]);tested+=1
    rows.append({'t':row['t'],'mu':mu.out(),'r':r.out(),'J':J.out(),'density':density.out(),'bisections':count,'initial_signs':signs,'all_four_incoming_enclosures_confirmed':True})
    if f==1:J1=J
    print('Certified profile',row['t'],flush=True)
half=J1/TWO
mu,count,signs=bracket(lambda z:profile(z)[1]-half,width=10**48)
t,_,_,_=profile(mu)
contained(t,'0.28581630680480845015','0.28581630680480845016')
result={'all_passed':True,'arithmetic':'Outward integer intervals, scale10^90,512 elliptic terms and1024 logarithm terms. Landen coordinate preserves the exact original profile.','scope':'Universal elliptic profile only; no original-period numeric matrices evaluated.','incoming_enclosures_confirmed':tested,'profile':rows,'half_volume_cutoff':{'mu':mu.out(),'t':t.out(),'bisections':count,'initial_signs':signs,'certified_bracket':['0.28581630680480845015','0.28581630680480845016']}}
(D/'profile_intervals_verified.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('All',tested,'incoming enclosures confirmed; half-volume cutoff:',t.out())
