"""Exact auxiliary source/matrix/transfer checks for EP.1--53.

No assertion statements: all mathematics executes under python -O.
This checker does not evaluate arithmetic zero data or C_h.
"""
import argparse
import hashlib
import json
import sys
from functools import lru_cache
from pathlib import Path
import sympy as sp

u, S = sp.symbols('u S')
I = sp.I
Q = sp.Rational

def canon(x):
    return sp.cancel(sp.expand(x))

def matrix_equal(A, B):
    return A.shape == B.shape and all(canon(x-y) == 0 for x,y in zip(A,B))

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    p.add_argument('--mutant', default='none', choices=['none','mass','interior','beta','schur','phase','raw_factorial'])
    args = p.parse_args()
    checks = []
    certificates = []
    def check(name, ok, **detail):
        checks.append({'name': name, 'passed': bool(ok), **detail})
    def eq(name, a, b):
        check(name, matrix_equal(a,b) if isinstance(a,sp.MatrixBase) else canon(a-b)==0)

    class Source:
        def __init__(self, name, moments, psi, centre, maxN):
            self.name,self.mu,self.psi,self.c,self.maxN=name,moments,sp.Poly(psi,u),centre,maxN
            self.q=self.psi.degree()
            self.chi=sp.Poly(sp.expand(I**self.q*psi.subs(u,(S-centre)/I)),S)
            self.polys=[];self.norms=[]
            for n in range(maxN+5):
                P=u**n
                for Pj,wj in zip(self.polys,self.norms):
                    P-=self.integral(Pj*u**n)/wj*Pj
                P=sp.expand(P)
                self.polys.append(P);self.norms.append(self.integral(P*P))
        def integral(self,P):
            return canon(sum(c*self.mu[int(e[0])] for e,c in sp.Poly(sp.expand(P),u).terms()))
        @lru_cache(None)
        def H(self,N,shift=0):
            return sp.Matrix(N+1,N+1,lambda a,b:self.integral((self.c-I*u)**a*(self.c+I*u)**b*u**shift))
        @lru_cache(None)
        def J(self,N):
            return sp.Matrix(self.q,N+1,lambda a,b:sp.rem(sp.Poly(S**b,S),self.chi).nth(a))
        @lru_cache(None)
        def G(self,N):
            J=self.J(N)
            return (J*self.H(N).inv()*J.conjugate().T).inv().applyfunc(canon)
        def V(self,N):return canon(self.G(N).det())
        @lru_cache(None)
        def radius(self,N):
            G=self.G(N);J=self.J(N);H=self.H(N)
            A=sp.Matrix(self.q,self.q,lambda a,b:sp.rem(sp.Poly(S**(b+1),S),self.chi).nth(a))
            D=A.conjugate().T*G+G*A-2*self.c*G
            Z=G.inv()*D
            eps2=canon(sp.trace(Z*Z)/2)
            R=H.inv()*J.conjugate().T*G
            Gp=R.conjugate().T*self.H(N,1)*R
            sigma=canon((sp.trace(A)-self.c*self.q)/I)
            phase=canon(sigma-sp.trace(G.inv()*Gp))
            return eps2,phase

    mass=Q(1) if args.mutant=='mass' else Q(7)
    gaussian=[mass*(sp.factorial2(j-1) if j else 1) if j%2==0 else 0 for j in range(36)]
    atomic=[sum(Q((10+t)*(2+((t+9)**2+3*(t+9))%7))*Q(t)**j for t in range(-9,10)) for j in range(36)]
    sources=[Source('gaussian-q2',gaussian,u*u+1,Q(1,2),8),
             Source('gaussian-q1',gaussian,u-1,Q(1),5),
             Source('asymmetric-q2',atomic,u*u+1,Q(1,2),5)]
    eq('literal-gaussian-mass',sources[0].norms[0],7)
    for src in sources:
        for j,w in enumerate(src.norms[:src.maxN+1]):
            check(f'{src.name}:positive-norm-{j}',w>0)
            eq(f'{src.name}:norm-source-determinant-{j}',w,src.H(j).det()/(src.H(j-1).det() if j else 1))
        for N in range(src.q,src.maxN):
            eps2,phase=src.radius(N)
            delta=src.V(N)/src.V(N-1)
            delta1=src.V(N+1)/src.V(N)
            rhs=src.norms[N+1]/src.norms[N]*(1-delta)*(1/delta1-1)
            eq(f'{src.name}:exact-radius-{N}',eps2+(0 if args.mutant=='phase' else phase**2),rhs)
            check(f'{src.name}:radius-nonnegative-{N}',eps2>=0)
            if src.name=='asymmetric-q2':check(f'{src.name}:nonzero-phase-{N}',phase!=0)
        for n in range(src.q,min(src.maxN-1,src.q+3)):
            for r in range(1,min(4,src.maxN-n)+1):
                m=n+r
                ds=[canon(src.V(n+j)/src.V(n+j-1)) for j in range(r+1)]
                U=canon(src.norms[m]/src.norms[n])
                K=canon(sp.prod(src.radius(n+j)[0]+src.radius(n+j)[1]**2 for j in range(r)))
                F=(1-ds[0])*(1-ds[-1])*sp.prod((1-ds[j])**(1 if args.mutant=='interior' else 2) for j in range(1,r))/sp.prod(ds[1:])
                eq(f'{src.name}:{n},{r}:window-product',K,U*F)
                H=src.H(m);H0=src.H(n-1);CD=H[:n,n:];DD=H[n:,n:]
                W=(DD-CD.conjugate().T*H0.inv()*CD).applyfunc(canon)
                J=src.J(m);Fmat=(J[:,n:]-src.J(n-1)*H0.inv()*CD).applyfunc(canon)
                G0=src.G(n-1)
                R=[Q(1)]
                for j in range(1,r+2):
                    Wj=W[:j,:j];Fj=Fmat[:,:j];Zj=Fj.conjugate().T*G0*Fj
                    R.append(canon((Wj+Zj).det()/Wj.det()))
                    eq(f'{src.name}:{n},{r}:prefix-{j}',R[-1],src.V(n-1)/src.V(n+j-1))
                w=W[0,0];pdet=W[:r,:r].det();sdet=W.det();Z=Fmat.conjugate().T*G0*Fmat
                e=w+Z[0,0];hp=(W+Z).det();hm=(W[:r,:r]+Z[:r,:r]).det()
                alpha=w/e
                beta=(pdet*hp/(hm*sdet)) if args.mutant=='beta' else hm*sdet/(pdet*hp)
                t=e*pdet/(w*hm)
                eq(f'{src.name}:{n},{r}:alpha',alpha,ds[0]);eq(f'{src.name}:{n},{r}:beta',beta,ds[-1])
                eq(f'{src.name}:{n},{r}:interior-t',t,sp.prod(ds[1:-1]))
                eq(f'{src.name}:{n},{r}:norm-U',sdet/(pdet*w),U)
                schur=hp/(pdet*e)*(sdet if args.mutant=='schur' else 1)
                eq(f'{src.name}:{n},{r}:reduced-schur',schur,U*src.V(n)/src.V(m))
                def rel_det(N):
                    B=sp.Matrix(N+1,N-src.q+1,lambda a,b:(src.chi*sp.Poly(S**b,S)).nth(a))
                    return canon((B.conjugate().T*src.H(N)*B).det())
                ratio=rel_det(m)*src.H(n-1).det()/(src.H(m-1).det()*rel_det(n))
                eq(f'{src.name}:{n},{r}:source-relation-ratio',ratio,U*src.V(n)/src.V(m))
                eq(f'{src.name}:{n},{r}:signed-boundary-budget',R[r]*R[r+1]/R[1],(src.V(n)/src.V(m))**2*ds[-1]/ds[0])
                if src.name=='gaussian-q2' and (n,r)==(2,3):
                    certificates.append({'fixture':src.name,'n':n,'r':r,'U':str(U),'alpha':str(alpha),'beta':str(beta),'t':str(t),'K':str(K),'source_relation_ratio':str(canon(ratio)),'R':str(canon(R[r]*R[r+1]/R[1]))})

    src=sources[0]
    for N,v in zip(range(1,6),[49,Q(49,3),Q(49,11),Q(882,473),Q(980,1333)]):
        eq(f'fixture-volume-{N}',src.V(N),v)
    for N,e2 in zip(range(2,5),[Q(16,3),Q(400,99),Q(4225,946)]):eq(f'fixture-radius-{N}',src.radius(N)[0],e2)
    for src in [sources[0],sources[2]]:
        nodes=[(-I,2),(I,2)];d=4;Pi=(u*u+1)**2
        def jets(P):
            return sp.Matrix([canon(sp.diff(P,u,e).subs(u,z)/(sp.factorial(e) if args.mutant=='raw_factorial' else 1)) for z,length in nodes for e in range(length)])
        V=sp.Matrix.hstack(*(jets(u**j) for j in range(d)))
        # Derivative order 2 fixture separately detects removal of raw factorial.
        jet2=sp.diff(u**3,u,2).subs(u,2)/(sp.factorial(2) if args.mutant=='raw_factorial' else 1)
        eq(f'{src.name}:raw-second-derivative',jet2,12)
        expectedV=sp.prod(sp.factorial(e) for z,length in nodes for e in range(length))*(2*I)**4
        eq(f'{src.name}:raw-vandermonde',V.det(),expectedV)
        transfer=[];nu=[]
        for a in range(4):
            F=sp.Matrix.hstack(*(jets(src.polys[a+j]) for j in range(d)))
            z=F.inv()*jets(src.polys[a+d])
            numer=sp.expand(src.polys[a+d]-sum(z[j]*src.polys[a+j] for j in range(d)))
            Phat,rem=sp.div(numer,Pi,u)
            eq(f'{src.name}:transfer-divisibility-{a}',rem,0)
            nua=src.integral(Pi*Phat*sp.conjugate(Phat).subs(sp.conjugate(u),u))
            eq(f'{src.name}:transfer-norm-{a}',nua,-z[0]*src.norms[a])
            check(f'{src.name}:transfer-positive-{a}',nua>0)
            eq(f'{src.name}:transfer-determinant-{a}',F.det()/V.det(),sp.prod(nu)/sp.prod(src.norms[:a]))
            transfer.append(canon(F.det()));nu.append(nua)
        for n,r in [(2,1),(2,2),(3,1)]:
            a=n-src.q+1
            ratio=transfer[a+r]/transfer[a]*sp.prod(src.norms[a+j]/src.norms[a+r+j] for j in range(src.q-1))
            eq(f'{src.name}:two-transfer-window-{n},{r}',ratio,src.norms[n+r]/src.norms[n]*src.V(n)/src.V(n+r))

    def root_interval(val,power,bits=90):
        lo=Q(0);hi=Q(1)
        while hi**power<val:hi*=2
        for _ in range(bits):
            mid=(lo+hi)/2
            if mid**power<=val:lo=mid
            else:hi=mid
        return lo,hi
    fixture=certificates[0];r=3;R=Q(fixture['R']);lo=Q(0);hi=Q(1,2)
    for _ in range(90):
        mid=(lo+hi)/2
        ratio=(1+2*mid)*(1+mid)**(2*(r-1))/((1-2*mid)*(1-mid)**(2*(r-1)))
        if ratio<=R:lo=mid
        else:hi=mid
    def budget_ratio(x):return (1+2*x)*(1+x)**(2*(r-1))/((1-2*x)*(1-x)**(2*(r-1)))
    check('optimizer-certified-bracket',budget_ratio(lo)<=R<=budget_ratio(hi))
    def fmax(x):return (2*x)**(2*r)/((1-4*x*x)*(1-x*x)**(r-1))
    ulo,_=root_interval(Q(fixture['U'])*fmax(lo),2*r)
    _,uhi=root_interval(Q(fixture['U'])*fmax(hi),2*r)
    certificates.append({'fixture':'gaussian-q2-sharp-budget','x_lower':str(lo),'x_upper':str(hi),'bound_lower':str(ulo),'bound_upper':str(uhi),'decimal_for_orientation':str(sp.N((ulo+uhi)/2,16))})
    report={'schema':'endpoint-product-exact-check-v1','checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':sys.version,'sympy':sp.__version__,'optimized':not __debug__,'mutant':args.mutant,'checks_executed':len(checks),'failed_count':sum(not c['passed'] for c in checks),'checks':checks,'certificates':certificates,'scope':'Exact auxiliary source Grams, phases, windows, Schur and relation determinants, confluent transfer and rational root brackets; no arithmetic data or analytic constant certificate.'}
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks_executed':len(checks),'failed_count':report['failed_count'],'mutant':args.mutant,'output':args.output}))
    return 1 if report['failed_count'] else 0

if __name__=='__main__':raise SystemExit(main())
