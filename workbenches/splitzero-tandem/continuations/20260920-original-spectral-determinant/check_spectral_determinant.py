from pathlib import Path
import json, math, hashlib
from datetime import datetime, timezone
import sympy as s
import numpy as np
from scipy.linalg import expm
from scipy.integrate import dblquad

P=Path(__file__).parent
checks=[];controls=[]
def check(name, value):
    if not bool(value): raise AssertionError(name)
    checks.append(name)
def exactzero(M): return all(s.cancel(x)==0 for x in M)

# Synthetic full-fibre algebra examples. The source is the centered
# Gaussian probability, not the programme's zeta measure. Rational
# arithmetic checks every original remainder and attained metric map.
y=s.symbols('y')
for delta,gamma in [(s.Rational(1,3),s.Rational(2)),(s.Rational(1,2),s.Rational(3,2))]:
    Q=s.Poly(y**4+2*(delta**2-gamma**2)*y**2+(gamma**2+delta**2)**2,y)
    def moment(n): return s.Integer(0) if n%2 else s.factorial2(n-1) if n else s.Integer(1)
    def remcol(poly):
        r=s.rem(s.Poly(poly,y),Q).as_expr().expand()
        return s.Matrix([r.coeff(y,j) for j in range(4)])
    M=s.Matrix.hstack(*[remcol(y**(j+1)) for j in range(4)])
    for N in range(3,8):
        H=s.Matrix(N+1,N+1,lambda i,j:moment(i+j))
        Hy=s.Matrix(N+1,N+1,lambda i,j:moment(i+j+1))
        J=s.Matrix.hstack(*[remcol(y**j) for j in range(N+1)])
        G=(J*H.inv()*J.T).inv()
        L=H.inv()*J.T*G
        C=G.inv()*L.T*Hy*L
        pc=-(H.inv()*s.Matrix([moment(N+1+i) for i in range(N+1)]))
        p=y**(N+1)+sum(pc[i]*y**i for i in range(N+1))
        r=remcol(p);ell=L[N,:]; v=G.inv()*ell.T
        tag=f'quartet-{delta}-{gamma}-N{N}'
        check(tag+'-minimum-section',exactzero(J*L-s.eye(4)))
        check(tag+'-metric-isometry',exactzero(L.T*H*L-G))
        check(tag+'-selfadjoint',exactzero(C.T*G-G*C))
        check(tag+'-boundary-sign',exactzero(M-C-r*ell))
        check(tag+'-parity-nilpotence',(ell*r)[0]==0)
        check(tag+'-trace-square',s.cancel(s.trace(M*M)-s.trace(C*C)-2*(ell*C*r)[0])==0)
        kappa2=(r.T*G*r)[0]*(ell*v)[0]
        Madj=G.inv()*M.T*G
        check(tag+'-zero-det',s.cancel((Madj*M).det()-Q.eval(0)**2)==0)
        for a in [s.Rational(1,2),s.Integer(2),s.Integer(5)]:
            D=C*C+a*a*s.eye(4)
            A=(r.T*G*D.inv()*r)[0]
            B=(ell*D.inv()*v)[0]
            lhs=(Madj*M+a*a*s.eye(4)).det()
            first=s.expand_complex(Q.eval(s.I*a)*Q.eval(-s.I*a))
            second=a*a*D.det()*A*B
            check(tag+f'-SD5-a{a}',s.cancel(lhs-first-second)==0)
            check(tag+f'-positive-boundary-a{a}',second>0)
        if N==3:
            controls.append({'name':tag+'-wrong-rank-one-sign','caught':not exactzero(M-C+r*ell)})
            controls.append({'name':tag+'-omitted-boundary-term','caught':s.cancel(lhs-first)!=0})

# General complex parity matrices, including singular C. The identity
# cannot depend on a real-only transpose or invertibility at zero.
rng=np.random.default_rng(530920)
for n in [2,3,4]:
    for repeat in range(5):
        U=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        if repeat==0: U[-1]=0
        C=np.block([[np.zeros((n,n)),U],[U.conj().T,np.zeros((n,n))]])
        r=np.r_[rng.normal(size=n)+1j*rng.normal(size=n),np.zeros(n)]
        v=np.r_[np.zeros(n),rng.normal(size=n)+1j*rng.normal(size=n)]
        M=C+np.outer(r,v.conj())
        for a in [.3,1.2,3.]:
            D=C@C+a*a*np.eye(2*n)
            first=abs(np.linalg.det(1j*a*np.eye(2*n)-M))**2
            second=a*a*np.linalg.det(D)*(r.conj()@np.linalg.solve(D,r))*(v.conj()@np.linalg.solve(D,v))
            lhs=np.linalg.det(M.conj().T@M+a*a*np.eye(2*n))
            check(f'complex-parity-{n}-{repeat}-{a}',np.isclose(lhs,first+second,rtol=2e-9,atol=1e-7))

# Differential and integrated bounds in a moving, noncommuting metric.
for n in [2,3,5]:
    for rep in range(8):
        M=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        K=(Z+Z.conj().T)/4
        l=np.linalg.eigvalsh(K); discrepancy=np.sum(abs(l-np.median(l)))
        def objects(u):
            S=expm(u*K/2); T=S@M@np.linalg.inv(S)
            return T.conj().T@T,T@T.conj().T
        X,Y=objects(.37);dt=1e-5;a=1.3;t=.8
        Xp,_=objects(.37+dt);Xm,_=objects(.37-dt)
        vals=lambda Z:np.linalg.eigvalsh(Z)
        heat=lambda Z:np.exp(-t*vals(Z)).sum()
        ld=lambda Z:np.log(a+vals(Z)).sum()
        resol=lambda Z:(1/(a+vals(Z))).sum()
        I=np.eye(n)
        heatder=np.trace(K@(t*X@expm(-t*X)-t*Y@expm(-t*Y))).real
        logder=np.trace(K@(Y@np.linalg.inv(a*I+Y)-X@np.linalg.inv(a*I+X))).real
        resder=np.trace(K@(X@np.linalg.matrix_power(np.linalg.inv(a*I+X),2)-Y@np.linalg.matrix_power(np.linalg.inv(a*I+Y),2))).real
        for name,fun,der in [('heat',heat,heatder),('log',ld,logder),('resolvent',resol,resder)]:
            check(f'derivative-{n}-{rep}-{name}',np.isclose((fun(Xp)-fun(Xm))/(2*dt),der,rtol=3e-6,atol=2e-8))
        X0,_=objects(0);X1,_=objects(1)
        check(f'heat-bound-{n}-{rep}',abs(heat(X1)-heat(X0))<=discrepancy/math.e+1e-10)
        check(f'log-bound-{n}-{rep}',abs(ld(X1)-ld(X0))<=discrepancy+1e-10)
        check(f'resolvent-bound-{n}-{rep}',abs(resol(X1)-resol(X0))<=discrepancy/(4*a)+1e-10)

# Original complete grid product and its two-dimensional logarithmic
# integral, including repeated roots. These are numerical illustrations
# of the proved Riemann estimate, not enclosures of its asymptotic error.
grid=[]
for delta,gamma in [(.2,3.),(.4,8.)]:
    g=.5*math.log(delta**2+gamma**2)-1.5+.5*(delta/gamma*math.atan(gamma/delta)+gamma/delta*math.atan(delta/gamma))
    integral,err=dblquad(lambda yy,xx:.5*math.log(delta**2*xx**2+gamma**2*yy**2),0,1,lambda _:0,lambda _:1,epsabs=2e-10)
    check(f'root-integral-{delta}-{gamma}',abs(g-integral)<2e-9)
    for k in [5,9,33,129]:
        z=gamma*(2*np.arange(k+1)-k)[None,:]-1j*delta*(2*np.arange(k+1)-k)[:,None]
        for mult in [1,2]:
            e=1+k*(mult-1);q=e*(k+1)**2
            product=e*np.log(abs(z)).sum()
            err=product/q-math.log(k)-g
            grid.append({'delta':delta,'gamma':gamma,'k':k,'m0':mult,'q':q,'root_average_error':float(err)})
            check(f'root-lower-radius-{delta}-{gamma}-{k}-{mult}',abs(z).min()>=math.hypot(delta,gamma)-1e-12)
        check(f'multiplicity-cancel-{delta}-{gamma}-{k}',abs(grid[-1]['root_average_error']-grid[-2]['root_average_error'])<1e-12)

# Median radius is an exact supremum over an entire positive bracket.
for q in range(2,12):
    logupper=np.arange(q,0,-1,dtype=float)/3
    m=q//2; optimum=logupper[:m].sum()
    attained=np.r_[logupper[:m],np.zeros(q-m)]
    check(f'bracket-sharp-{q}',abs(np.sum(abs(attained-np.median(attained)))-optimum)<1e-12)
    for rep in range(5):
        ell=rng.random(q)*logupper
        check(f'bracket-bound-{q}-{rep}',np.sum(abs(ell-np.median(ell)))<=optimum+1e-12)
controls.append({'name':'endpoint-scalar-discrepancy-is-not-bracket-radius','caught':np.sum(abs(np.array([math.log(4),0])-math.log(2)))>0})
controls.append({'name':'root-integral-missing-half-factor','caught':abs(2*integral-g)>.1})
if not all(x['caught'] for x in controls):raise AssertionError('negative control failed')
for item in controls:item['caught']=bool(item['caught'])
receipt={'utc':datetime.now(timezone.utc).isoformat(),'passed':len(checks),'negative_controls':controls,'scope':'Exact rational original-fibre algebra and noncommuting numerical sensitivity checks. No finite sample is used to prove a zeta asymptotic or an effective k threshold.','grid_examples':grid,'checks':checks,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'SPECTRAL_DETERMINANT_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'negative_controls':len(controls)}))
