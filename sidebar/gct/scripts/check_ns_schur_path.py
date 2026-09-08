"""Exact coefficient, weight, exponent and path checks; no source shelves."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
t,z,h=s.symbols('t z h')
B=-42+196*t-280*t**2+160*t**3-32*t**4
H=21-98*t+140*t**2-80*t**3+16*t**4
profile=[27,81,162,270,300,252,126,42]
count=0
def check(value):
    global count
    assert value
    count+=1
check(s.expand(B+2*H)==0)
check(s.expand(H-(3-2*t)*(7-28*t+28*t**2-8*t**3))==0)
poly=sum(s.Rational((a-b+1)*(b-c+1)*(a-c+2),2)*z**(15-a-b-c)
         for a in range(5,8) for b in range(3,6) for c in range(4))
check(s.expand(poly-sum(v*z**k for k,v in enumerate(profile)))==0)
check(sum(profile)==1260)
check(sum(k*v for k,v in enumerate(profile))==4725)
check(sum(profile[::2])==615)
check(sum(profile[1::2])==645)
for k in range(8):
    check(s.expand((t*B)**k-(-2*t)**k*H**k)==0)
    check(s.expand(B**k).subs(t,0)==(-42)**k)
    check((s.Rational(7,1)-15*(s.Rational(1,2)+h)).expand()==-s.Rational(1,2)-15*h)
    check(s.expand(k-15*(s.Rational(1,2)+h)-(k-s.Rational(15,2)-15*h))==0)
check(s.expand(4725-18900*(s.Rational(1,2)+h))==-4725-18900*h)
for tau in [s.Rational(1,100),s.Rational(1,10),s.Rational(1,4)]:
    check(B.subs(t,tau)<0)
    check(H.subs(t,tau)>0)
    for k in range(8):
        check(s.sign((tau*B.subs(t,tau))**k)==(-1)**k)
result={'status':'passed','checks':count,'profile':profile,
        'proof_sha256':hashlib.sha256((ROOT/'tex/ns_schur_path.tex').read_bytes()).hexdigest(),
        'scope':'Finite exact identities supplement the complete interval and asymptotic proofs in TeX.'}
(ROOT/'checks/ns_schur_path.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
