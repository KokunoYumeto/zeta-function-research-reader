"""Exact auxiliary algebra and numerical diagnostics; neither replaces the proofs."""
from pathlib import Path
import json, runpy
import sympy as s
import mpmath as mp
P=Path(__file__).parent
checks=[]
def eq(name,expr):
    val=s.simplify(s.expand_complex(expr))
    if val!=0: raise AssertionError((name,val))
    checks.append({'name':name,'kind':'exact','passed':True})
# Independently retain the complete confluent inverse, not a 2x2 surrogate.
d=s.Rational(1,4);g=s.Rational(7,3)
for m in range(1,5):
    roots=[d+s.I*g,d-s.I*g];inds=[(a,j) for a in range(2) for j in range(m)]
    G=s.Matrix(2*m,2*m,lambda i,j:s.expand_complex((-1)**(inds[i][1]+inds[j][1])*s.binomial(inds[i][1]+inds[j][1],inds[i][1])/(s.conjugate(roots[inds[i][0]])+roots[inds[j][0]])**(inds[i][1]+inds[j][1]+1)))
    GI=G.inv()
    eq('SK21 diagonal m='+str(m),GI[m-1,m-1]-(2*d)**(2*m-1)*((d*d+g*g)/(g*g))**m)
    eq('SK21 phase m='+str(m),GI[m-1,2*m-1]-(2*d)**(2*m)*(2*d+2*s.I*g)**(2*m-1)/(2*s.I*g)**(2*m))
t=s.symbols('t',real=True)
fourier=s.sqrt(2)/4*(s.diff(s.cosh(t)**s.Rational(-1,2),t,4)-s.diff(s.cosh(t)**s.Rational(-1,2),t,2)/2+s.cosh(t)**s.Rational(-1,2)/16)
nums=[s.Rational(33,64),s.Rational(585,128),s.Rational(22455,256),s.Rational(1452915,512),s.Rational(141390945,1024)]
for j,c in enumerate(nums): eq('SK29 full physical moment '+str(2*j),(-1)**j*s.diff(fourier,t,2*j).subs(t,0)-c*s.sqrt(2))
eq('SK29 leading mass ratio',nums[0]/nums[1]-s.Rational(22,195))
eq('SK29 constant mass ratio',nums[2]/nums[1]-s.Rational(499,26))
# Full first variation from the original finite PCL formula.
b,h=s.symbols('b h',positive=True)
R1=s.zeros(4)
for a in range(1,5):
 for r in range(4):
    power=6+r-a
    for hh in range(power//4+1):
      pp=(power-4*hh)//2
      if 2*pp+4*hh != power:continue
      L=pp+hh-1
      R1[a-1,r]+=b**pp*h**hh/(3**pp*s.factorial(pp)*s.factorial(hh))*(-1)**L*5**L*s.rf(s.Rational(a,5),L)
J=s.eye(4);J[0,2]=-b/3;J[1,3]=-2*b/3;K=R1*J.inv()
eq('CP12 K23',K[1,2]-b*(4*b*b-27*h)/81)
eq('CP12 K14',K[0,3]+(b**4-12*b*b*h+54*h*h)/108)
R,T=s.symbols('R T',real=True);u=(2*R-T)/3;v=(2*T-R)/3
eq('CP9 full line gate',T*u*u-R*v*v+(R-T)*(R*R-7*R*T+T*T)/9)
eq('CP14 exceptional polynomial',T*(2*R-T)**4-R*(2*T-R)**4+(R-T)*((R+T)**4-27*(R+T)**2*R*T+81*(R*T)**2))
bb=s.symbols('bb',real=True)
remainder=s.rem(-(bb**4-12*bb*bb+54)/108-bb*(4*bb*bb-27)/81-(108-45*bb)/324,bb**2+3*bb-9,bb)
eq('CP14 exact negative branch remainder',remainder)
# Finite analytic diagnostics: original physical source, full cutoff and resonance.
mp.mp.dps=40
phi=lambda x:(4*mp.pi**2*x**4-6*mp.pi*x*x)*mp.exp(-mp.pi*x*x)
Phi=lambda z:z*(z-1)*mp.pi**(-z/2)*mp.gamma(z/2)/2
Z=lambda z:(z*(z-1))**2*mp.betainc((1-z)/2,z/2,0,mp.mpf('.5'))/4+mp.sqrt(2)*(z**3-mp.mpf('1.5')*z*z-z/4+mp.mpf('.375'))/4
f=lambda z,x:x**(-z)*mp.pi**(-z/2)*(2*mp.gammainc(z/2+2,mp.pi*x*x,mp.inf)-3*mp.gammainc(z/2+1,mp.pi*x*x,mp.inf))
def close(name,a,b,tol=mp.mpf('1e-27')):
 err=abs(a-b)/max(1,abs(a),abs(b))
 if err>tol:raise AssertionError((name,err))
 checks.append({'name':name,'kind':'40-digit numerical diagnostic','relative_error':str(err),'passed':True})
z=mp.mpc('.31','1.7')
close('SK3 original cross integral',Z(z),mp.quad(lambda x:phi(x)*f(z,x),[0,1,mp.inf]))
close('SK4 reflection',Z(z)+Z(1-z),Phi(z)*Phi(1-z))
cut=mp.mpf('1.1');eps=mp.exp(-cut);L=30
cn=lambda n:2*n*(2*n+1)*(-mp.pi)**n/mp.factorial(n)
for w in [mp.mpc('.42','-.6'),1-z]:
 a=z+w-1
 F=(Phi(z)*mp.diff(Phi,1-z)-mp.diff(Z,1-z))/(Phi(z)*Phi(1-z)) if abs(a)<mp.mpf('1e-35') else (Phi(z)*Phi(w)-Z(z)-Z(w))/(a*Phi(z)*Phi(w))
 B=-Phi(z)*sum(cn(n)*eps**(2*n+1-z)/((w+2*n)*(2*n+1-z)) for n in range(1,L+1))-Phi(w)*sum(cn(n)*eps**(2*n+1-w)/((z+2*n)*(2*n+1-w)) for n in range(1,L+1))+sum(cn(n)*cn(mm)*eps**(2*n+2*mm+1)/((z+2*n)*(w+2*mm)*(2*n+2*mm+1)) for n in range(1,L+1) for mm in range(1,L+1))
 val=(cut if abs(a)<mp.mpf('1e-35') else mp.expm1(a*cut)/a)+F-B/(Phi(z)*Phi(w))
 direct=mp.quad(lambda x:f(z,x)*f(w,x)/(Phi(z)*Phi(w)),[eps,1,mp.inf])
 close('SK9 cutoff '+('resonance' if abs(a)<mp.mpf('1e-35') else 'nonresonance'),val,direct)
out={'status':'passed','count':len(checks),'checks':checks,'scope':'finite diagnostics supplement the complete symbolic and analytic proofs; no hypothetical zeta zeros or asymptotic uniform estimates certified numerically'}
(P/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'count':out['count']},indent=2))
