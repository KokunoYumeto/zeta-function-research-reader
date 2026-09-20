from pathlib import Path
import sympy as s
import json,math,hashlib
P=Path(__file__).parent
count=0
def check(v,label):
    global count
    if not bool(v): raise RuntimeError(label)
    count+=1
y=s.Symbol('y')
def coeff(poly,N):
    po=s.Poly(poly,y)
    return s.Matrix([po.nth(i) for i in range(N+1)])
def fixture(q,N):
    # Exact even positive atomic measure, enough atoms for all source degrees.
    nodes=list(range(-2*q-4,2*q+5))
    moments=[sum(s.Rational(1+j*j,3)*s.Integer(j)**t for j in nodes) for t in range(2*N+5)]
    H=s.Matrix(N+1,N+1,lambda i,j:moments[i+j])
    Q=s.prod(y*y+(j+1)**2 for j in range(q//2))
    def rem(f): return coeff(s.rem(f,Q,y),q-1)
    J=s.Matrix.hstack(*[rem(y**j) for j in range(N+1)])
    G=(J*H.inv()*J.T).inv()
    L=H.inv()*J.T*G
    Hp=s.Matrix(N+2,N+2,lambda i,j:moments[i+j])
    mp=s.Matrix([moments[N+1+j] for j in range(N+1)])
    pp=y**(N+1)-sum(x*y**i for i,x in enumerate(H.inv()*mp))
    omega=(coeff(pp,N+1).T*Hp*coeff(pp,N+1))[0]
    r=rem(pp)
    ell=L[N,:]
    M=s.Matrix.hstack(*[rem(y**(j+1)) for j in range(q)])
    R=r*ell
    C=M-R
    check(C.T*G==G*C,'selfadjoint compression')
    check((ell*r)[0]==0,'boundary square zero')
    check(C.det()!=0,'all cutoffs compression invertible')
    D=s.zeros(N+1,N+1)
    for i in range(1,N+1):D[i-1,i]=1
    u=rem(s.cancel((Q-Q.subs(y,0))/y))
    phi=L[0,:]
    check(M.inv()==J*D*L-u*phi/Q.subs(y,0),'S11 division inverse')
    if N%2==1:
        d=N+1-q
        if d==0: Ud=s.Integer(1)
        else:
            HQ=s.Matrix(d,d,lambda i,j:sum(s.Poly(s.expand(Q**2),y).nth(t)*moments[t+i+j] for t in range(2*q+1)))
            mq=s.Matrix([sum(s.Poly(s.expand(Q**2),y).nth(t)*moments[t+d+i] for t in range(2*q+1)) for i in range(d)])
            Ud=y**d-sum(x*y**i for i,x in enumerate(HQ.inv()*mq))
        check(abs(C.det())==abs(pp.subs(y,0)/Ud.subs(y,0)),'S20 odd determinant')
        v=G.inv()*ell.T;a=C.inv()*r;b=C.inv()*v
        z=1+(ell*a)[0]
        A=a*b.T*G/z
        check(M.inv()==C.inv()-A,'S31 inverse boundary')
        check(A*A==s.zeros(q),'S31 square zero inverse correction')
        rr=(r.T*G*r)[0];dd=omega/(omega+rr)
        Gnext=G-G*r*r.T*G/(omega+rr)
        Jnext=s.Matrix.hstack(J,rem(y**(N+1)))
        Lnext=Hp.inv()*Jnext.T*Gnext
        check(Gnext==(Jnext*Hp.inv()*Jnext.T).inv(),'S36 complete source update')
        # operator HS equals operator norm for a rank-one map, no square root needed
        old=(G.inv()*A.T*G*A).trace()
        new=(Gnext.inv()*A.T*Gnext*A).trace()
        bb=(b.T*G*b)[0]
        check(s.cancel(new/old)==1+(z-1)**2/(omega*bb),'S37 exact adjacent correction')
        pnextmom=s.Matrix([moments[N+2+j] for j in range(N+2)])
        pnext=y**(N+2)-sum(x*y**i for i,x in enumerate(Hp.inv()*pnextmom))
        Cnext=M-rem(pnext)*Lnext[N+1,:]
        check(abs(Cnext.det())==abs(Q.subs(y,0))**2*dd/abs(C.det()),'S38 even determinant reciprocity')
    return {'q':q,'N':N}
fixtures=[fixture(q,N) for q in [2,4,6] for N in [q-1,q,2*q-1,2*q]]
# The hard-gap prefactor, exact upper bound using pi<4, e<3.
check(s.Rational(1600*81,512**2)<s.Rational(1,2),'S25 exponential factor')
check(s.Rational((1+16*16**2)*(16+1)**2,256*2**16)<=1,'S25 starting integer')
n=s.Symbol('n',positive=True)
# successive ratio is below 1 for n>=16 by expanding in t=n-16
num=s.expand(2*(1+16*n**2)*(n+1)**2-(1+16*(n+1)**2)*(n+2)**2)
check(all(c>=0 for c in s.Poly(num.subs(n,s.Symbol('t')+16),s.Symbol('t')).all_coeffs()),'S25 all larger integers')
# root-integral differentiation and reciprocal formula on exact finite grids
for k in [9,13]:
    delta=s.Rational(1,4); gamma=s.Integer(3);q=(k+1)**2;c=s.Rational(k,2);cp=c-4
    roots=[c+(2*a-k)*delta+s.I*(2*b-k)*gamma for a in range(k+1) for b in range(k+1)]
    low=[cp+(2*a-k+8)*delta+s.I*(2*b-k+8)*gamma for a in range(k-7) for b in range(k-7)]
    shifts=[(0,4,1),(1,4,-2),(2,4,1)]
    bs=[4+(2*r-8)*delta+s.I*(2*t-8)*gamma for r,t,_ in shifts]
    mu=[s.expand(sum(a*b**j for (_,_,a),b in zip(shifts,bs))) for j in range(3)]
    check(mu[0]==mu[1]==0 and mu[2]!=0,'OR2 actual shift fixture order')
    for z in [s.Rational(1,10),s.Rational(1,7)+s.I/s.Integer(11)]:
        S=cp+s.I*q/z
        chi=s.prod(S-a for a in roots); chilo=s.prod(S-a for a in low)
        left=0;right=0;prodexpr=0
        for (r,t,a),b in zip(shifts,bs):
            full=s.prod(S+b-x for x in roots)
            outer=s.prod(S+b-roots[ia*(k+1)+ib] for ia in range(k+1) for ib in range(k+1)
                         if not (r<=ia<=r+k-8 and t<=ib<=t+k-8))
            check(s.cancel(full/chilo-outer)==0,'OR3 whole lower-root divisibility')
            left+=a*full;right+=a*outer
            prodexpr+=a*s.prod(1+(-s.I*b*z)/(q-((x-cp)/s.I)*z) for x in roots)
        check(s.cancel(left/chilo-right)==0,'OR3 sum no deleted interference')
        check(s.cancel(left/chi-prodexpr)==0,'OR5 exact reciprocal map')
receipt={'exact_checks':count,'finite_positive_measure_fixtures':fixtures,
         'scope':'S11,S18,S20,S31,S36–38 and S25; OR2–5 rational finite-shift fixtures. No native xi moments or asymptotic test claimed.',
         'status':'passed'}
(P/'ROOT_NEW_EXACT_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))

