# claude-ab: check of YM referee Finding 1 (27 Sep 2026).
# (1) closed forms of m(v2), t(v2) against the first pass's values; (2) the N=2 threshold with rational upper bounds.
from fractions import Fraction as Fr
from math import sqrt
import sympy as sp
m2c=6+Fr(11200,117)+Fr(112,9); m2r=Fr(448,39)   # m = m2c + m2r*sqrt(3)
t2c=Fr(3,2)+Fr(80,9)+Fr(256,39); t2r=Fr(64,39)
m2=float(m2c)+float(m2r)*sqrt(3); t2=float(t2c)+float(t2r)*sqrt(3)
print("closed forms: m(v2) = %.10f (first pass 134.0673186784), t(v2) = %.10f (first pass 19.7953312398)"%(m2,t2))
# rational upper bounds with sqrt(3) < 1.7321
M2=m2c+m2r*Fr(17320509,10**7); T2=t2c+t2r*Fr(17320509,10**7)
assert Fr(17320509,10**7)**2>3
print("upper bounds with sqrt3<1.7320509: m2 <= %.7f, t2 <= %.7f; referee's 1340674/10^4, 197954/10^4 are >= these:"%(float(M2),float(T2)), Fr(1340674,10**4)>=M2, Fr(197954,10**4)>=T2)
m=[None,Fr(64,3),Fr(1340674,10**4)]; t=[None,Fr(16,3),Fr(197954,10**4)]
x=sp.symbols('x')
N=2
ell=sum((m[i]+4*t[i])*x**i for i in range(1,N+1))
delta=sum(3*(m[i]*t[j]+m[j]*t[i])*x**(i+j) for i in range(1,N+1) for j in range(1,N+1) if i+j>=N+1)
D=sp.expand((1-ell)**2-sp.Rational(8,3)*delta)
roots=[r for r in sp.Poly(D,x).real_roots() if r>0]
a2=min(roots); a2f=float(a2.evalf(30))
print("alpha_2 = %.10f ; threshold g^2 >= 1/(2 sqrt(alpha_2)) = %.6f"%(a2f,1/(2*sqrt(a2f))))
def dN(xv):
    Dv=float(sp.N(D.subs(x,xv),40)); Dv=max(Dv,0.0)
    return 1.5*(1+Dv**0.5)+sum(float(sp.Rational(3,2)*m[i]-6*t[i])*float(sp.N(xv,40))**i for i in range(1,N+1))
print("d_2(alpha_2) = %.6f ; d_2(1/64) = %.6f (g^2 = 4)"%(dN(a2),dN(sp.Rational(1,64))))
# the workbench pair for comparison
m=[None,Fr(64,3),Fr(5834,39)]; t=[None,Fr(16,3),Fr(137,6)]
ell=sum((m[i]+4*t[i])*x**i for i in range(1,N+1))
delta=sum(3*(m[i]*t[j]+m[j]*t[i])*x**(i+j) for i in range(1,N+1) for j in range(1,N+1) if i+j>=N+1)
D=sp.expand((1-ell)**2-sp.Rational(8,3)*delta)
a2w=min(r for r in sp.Poly(D,x).real_roots() if r>0); print("workbench pair: alpha_2 = %.10f, threshold %.6f"%(float(a2w),1/(2*sqrt(float(a2w)))))
