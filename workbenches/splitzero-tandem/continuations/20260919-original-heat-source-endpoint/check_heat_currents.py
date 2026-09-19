"""Finite diagnostics, independent of the analytic growth proof."""
from pathlib import Path
import json, math
import numpy as np
import sympy as s
rng=np.random.default_rng(19092026); passed=[]
def ck(name,v):
 if not bool(v):raise AssertionError(name)
 passed.append(name)
def forms(G,Lam):
 Om=Lam.conj().T@np.linalg.inv(Lam@np.linalg.solve(G,Lam.conj().T))@Lam
 return G-Om,Om
def vals(G,Lam,a1,a2,v,w):
 L,Om=forms(G,Lam); E=(v.conj()@G@v).real
 F=np.array([a.conj()@G@v for a in [a1,a2]])
 K=np.array([a.conj()@L@v for a in [a1,a2]])
 B=F-K
 cur=2/w*np.real([K[0].conjugate()*K[1],B[0].conjugate()*B[1],K[0].conjugate()*B[1]+B[0].conjugate()*K[1]])
 return E,F,K,B,cur
for case in range(30):
 n=5; b=2
 X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
 G=X.conj().T@X+np.eye(n)
 eig,U=np.linalg.eigh(G); rt=(U*np.sqrt(eig))@U.conj().T
 X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));Z=X+X.conj().T; Z/=np.linalg.norm(Z,2)
 eta=.01+.24*case/29; Gp=rt@(np.eye(n)+eta*Z)@rt
 Lam=rng.normal(size=(b,n))+1j*rng.normal(size=(b,n))
 a1,a2,v=rng.normal(size=(3,n))+1j*rng.normal(size=(3,n));w=.7
 E,F,K,B,cur=vals(G,Lam,a1,a2,v,w);Ep,Fp,Kp,Bp,cp=vals(Gp,Lam,a1,a2,v,w)
 p=K/F;prod=np.array([p[0].conjugate()*p[1],(1-p[0].conjugate())*(1-p[1]),p[0].conjugate()*(1-p[1])+(1-p[0].conjugate())*p[1]])
 c=F[0].conjugate()*F[1]/(w*E)
 ck(f'{case}: exact three polynomial currents',np.allclose(cur,2*E*np.real(c*prod),rtol=1e-10,atol=1e-10))
 d1=(a1.conj()@G@a1).real; d2=(a2.conj()@G@a2).real; kap=math.sqrt(d1*d2)/w
 ck(f'{case}: normalized error including cross current',np.max(np.abs(cp/(2*Ep)-cur/(2*E)))<=12*kap*eta*(1+1e-10))
 ck(f'{case}: total pairing identity',abs(cur.sum()-2/w*(F[0].conjugate()*F[1]).real)<1e-9)
 pp=Kp/Fp;prod_p=np.array([pp[0].conjugate()*pp[1],(1-pp[0].conjugate())*(1-pp[1]),pp[0].conjugate()*(1-pp[1])+(1-pp[0].conjugate())*pp[1]])
 cprime=Fp[0].conjugate()*Fp[1]/(w*Ep)
 ck(f'{case}: fixed-arithmetic-coefficient receiver',np.allclose(cp-2*Ep*np.real(c*prod_p),2*Ep*np.real((cprime-c)*prod_p)))
# An approximate denominator vanishes exactly: the polynomial currents survive.
eta=.125;G=np.eye(2);Gp=np.array([[1,eta],[eta,1]])
Lam=np.array([[1,1j]]);a1=np.array([eta,-1]);a2=np.array([1,1]);v=np.array([1,0]);w=1
E,F,K,B,cur=vals(G,Lam,a1,a2,v,w);Ep,Fp,Kp,Bp,cp=vals(Gp,Lam,a1,a2,v,w)
ck('zero approximate denominator', Fp[0]==0 and F[0]!=0 and np.isfinite(cp).all())
ck('zero-denominator total identity',abs(cp.sum()-2*(Fp[0].conjugate()*Fp[1]).real)<1e-15)
# Exact Euclidean remainder identity, including repeated full roots.
t=s.symbols('t');h=s.Poly((t-1-s.I)**2*(t-2+s.I)**3,t)
for degree in range(1,12):
 P=s.Poly(sum((j+1+s.I*j)*t**j for j in range(degree+1)),t)
 rem=P.rem(h); ell=rem.nth(h.degree()-1)
 ck(f'original action remainder {degree}',s.Poly(t*rem.as_expr(),t)-s.Poly(t*P.as_expr(),t).rem(h)==h.mul_ground(ell))
# Strict and non-strict guards differ only in their integer endpoint.
for k in [9,101,1001]:
 q=(k+1)**2;a0=math.log(4/math.pi);logp=-2*a0*q;logc=math.sqrt(q)
 # Asymptotic expression is evaluated in logs to avoid p underflow.
 threshold=2*logc/math.log(2)+2*math.log2(2*k)-logp/math.log(2)
 ck(f'guard leading cost {k}',threshold/q>2*a0/math.log(2))
Path(__file__).with_name('HEAT_CURRENT_CHECKS.json').write_text(json.dumps({'scope':'Finite synthetic matrix/identity tests only; no zeta-zero or asymptotic simulation.','passed':len(passed),'checks':passed},indent=2))
print(json.dumps({'passed':len(passed)}))
