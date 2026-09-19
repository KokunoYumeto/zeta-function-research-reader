"""Independent finite moment/quotient checks; not an evaluation of xi zeros."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=100
A=Path(__file__).resolve().parent
checks=[]
def close(name,a,b,tol=mp.mpf('1e-70')):
    err=abs(a-b)/max(1,abs(a),abs(b))
    checks.append(dict(name=name,relative_error=str(err),passed=bool(err<tol)))
    assert err<tol,(name,str(err))
def bound(name,a,b):
    checks.append(dict(name=name,passed=bool(a<=b),left=str(a),right=str(b)))
    assert a<=b,name
nodes=[mp.mpf(s*j) for j in range(100,341,20) for s in (-1,1)]
base=[mp.mpf(1+(i//2)%5) for i in range(len(nodes))]
alt=[w*(1+mp.mpf(i//2)/13) for i,w in enumerate(base)]
Q=lambda y:y**4-6*y**2+25
q=4; z=mp.mpc(2,-1); d=-z.imag; R=abs(z); Y=mp.mpf(99)
weights=[w*Q(y)**2 for y,w in zip(nodes,base)]
def integ(f,ws=weights): return mp.fsum(w*f(y) for y,w in zip(nodes,ws))
def poly(cs,y): return mp.fsum(c*y**j for j,c in enumerate(cs))
def gram(n,ws,shift=0,xmap=lambda y:y):
    return mp.matrix([[mp.fsum(w*xmap(y)**(i+j+shift) for y,w in zip(nodes,ws)) for j in range(n)] for i in range(n)])
def op(n,ws):
    if n==0: cs=[mp.mpf(1)]
    else:
        G=gram(n,ws); h=mp.matrix([mp.fsum(w*y**(j+n) for y,w in zip(nodes,ws)) for j in range(n)])
        cs=list(mp.lu_solve(G,-h))+[mp.mpf(1)]
    nu=mp.fsum(w*abs(poly(cs,y))**2 for y,w in zip(nodes,ws))
    return cs,nu
ops=[op(j,weights) for j in range(q+3)]
C=[integ(lambda y,cs=cs:poly(cs,y)/(z-y)) for cs,nu in ops]
H=[]
for r in range(q+3):
    def res(y): return 1/(z-y)-mp.fsum(C[j]/ops[j][1]*poly(ops[j][0],y) for j in range(r))
    H.append(integ(lambda y:abs(res(y))**2))
    if r:
        close(f'Wronskian r={r}',H[r],mp.im(C[r]*mp.conj(C[r-1]))/(d*ops[r-1][1]))
        close(f'original attained residual drop r={r-1}',H[r-1]-H[r],abs(C[r-1])**2/ops[r-1][1])
M=[integ(lambda y,cs=cs:poly(cs,y)**2/y**2) for cs,nu in ops]
bs=[]
for r in range(q+2):
    b=R**2*M[r]/ops[r][1] if r%2==0 else ops[r-1][1]**2/(ops[r][1]*M[r-1])
    bs.append(b)
    T=(H[r]-H[r+1])/H[r]
    allowance=32*(1+R/d)*(R/Y)**2
    bound(f'finite amplitude error r={r}',abs(T/b-1),allowance)
    if r%2==0:
        zero_res=[-poly(ops[r][0],y)/(y*ops[r][0][0]) for y in nodes]
        Hzero=mp.fsum(w*abs(v)**2 for w,v in zip(weights,zero_res))
        close(f'zero argument norm r={r}',Hzero,M[r]/ops[r][0][0]**2)
        for j in range(r):
            close(f'zero argument orthogonality r={r},j={j}',mp.fsum(w*v*y**j for y,w,v in zip(nodes,weights,zero_res))/mp.sqrt(Hzero*integ(lambda y:y**(2*j))),0)
    else:
        even=ops[r-1]; odd=ops[r]
        close(f'paired inverse moment cancellation r={r}',bs[r-1]*bs[r],R**2*even[1]/odd[1])
        close(f'constant recurrence r={r}',ops[r+1][0][0],-odd[1]/even[1]*even[0][0])
ws=[1]+[2]*(q-1)+[1]
lhs=mp.fsum(w*mp.log(bs[r]) for r,w in enumerate(ws))
rhs=2*q*mp.log(R)-2*mp.log(abs(ops[q][0][0]))+mp.log((M[q]/ops[q][1])/(M[0]/ops[0][1]))
close('complete trapezoidal paired product',lhs,rhs)
# Independent full finite minimum in coefficient coordinates, including every cross block.
N=q-1
source_ops=[op(n,base) for n in range(2*q+2)]
qcoeff=[mp.mpf(25),0,mp.mpf(-6),0,mp.mpf(1)]
def remainder(cs):
    cs=list(cs)
    for j in range(len(cs)-1,q-1,-1):
        top=cs[j]
        for t in range(q+1): cs[j-q+t]-=top*qcoeff[t]
    return mp.matrix((cs+[mp.mpf(0)]*q)[:q])
# Q/(z-y) coefficient vector obtained by synthetic division (sign irrelevant to p2).
vq=[mp.mpc(0)]*q; vq[-1]=1
for j in range(q-2,-1,-1): vq[j]=qcoeff[j+1]+z*vq[j+1]
v=mp.matrix(vq)
allG=[]
for r in range(q+2):
    N=q-1+r; Cinv=mp.zeros(q)
    for n in range(N+1):
        b=remainder(source_ops[n][0]); Cinv+=b*b.H/source_ops[n][1]
    G=Cinv**-1; b=remainder(source_ops[N+1][0]); En=(v.H*G*v)[0]; beta=(b.H*G*b)[0]; pairing=(b.H*G*v)[0]
    p2=abs(pairing)**2/(En*beta)
    Delta=source_ops[N+1][1]/ops[r][1]
    close(f'full coefficient attained norm r={r}',En,H[r])
    close(f'full coefficient p2 r={r}',p2,(H[r]-H[r+1])/((1-Delta)*H[r]))
    close(f'full relation boundary norm r={r}',beta,ops[r][1]-source_ops[N+1][1])
    allG.append(G)
    if r==0: Gfirst=G
# Positive and rational negative determinant slopes versus distinct comparable measures.
n=q//2; l=mp.mpf(1); u=max(a/b for a,b in zip(alt,base))
wa=[w*Q(y)**2 for y,w in zip(nodes,alt)]
xmap=lambda y:(y/q)**2
def fd(a,weights): return mp.log(mp.det(gram(n,weights,a,xmap)))
for lo,hi in [(0,2),(-2,0)]:
    difference=(fd(hi,wa)-fd(lo,wa))-(fd(hi,weights)-fd(lo,weights))
    bound(f'two quotient determinant slope {lo},{hi}',abs(difference),mp.log(u/l))
val=mp.log(abs(ops[q][0][0]))-q*mp.log(q)
close('constant coefficient determinant ratio',val,fd(1,weights)-fd(0,weights))
bound('convex lower endpoint',(fd(0,weights)-fd(-2,weights))/2,val)
bound('convex upper endpoint',val,(fd(2,weights)-fd(0,weights))/2)
# Same observation, independently calculate quotient norm and projection identity.
Lam=mp.matrix([[1,0,1,0],[0,1,0,2]])
I=mp.matrix([[-1,0],[0,-2],[1,0],[0,1]])
K=I*(I.H*Gfirst*I)**-1*I.H*Gfirst
QB=(Lam*Gfirst**-1*Lam.H)**-1
close('typed original quotient metric',mp.norm(Gfirst*(mp.eye(q)-K)-Lam.H*QB*Lam)/mp.norm(Gfirst),0)
close('original observed class energy',(v.H*Gfirst*(mp.eye(q)-K)*v)[0],((Lam*v).H*QB*(Lam*v))[0])
for r in range(q+1):
    G=allG[r]; Gnext=allG[r+1]; N=q-1+r
    P=I*(I.H*G*I)**-1*I.H*G
    Pnext=I*(I.H*Gnext*I)**-1*I.H*Gnext
    b=remainder(source_ops[N+1][0]); beta=(b.H*G*b)[0]
    Delta=source_ops[N+1][1]/ops[r][1]
    dK=mp.det(I.H*Gnext*I)/mp.det(I.H*G*I)
    pi1next=(b.H*Gnext*Pnext*b)[0]/(b.H*Gnext*b)[0]
    close(f'future boundary to original kernel determinant r={r}',dK,Delta/(Delta+(1-Delta)*pi1next))
    eb=(v.H*G*(mp.eye(q)-P)*v)[0]; ebnext=(v.H*Gnext*(mp.eye(q)-Pnext)*v)[0]
    En=(v.H*G*v)[0]; theta=(v.H*G*P*v)[0]/En
    V=(b.H*G*P*v)[0]/(b.H*G*v)[0]; T=(H[r]-H[r+1])/H[r]
    close(f'actual observation residual return r={r}',ebnext/eb,1-T*abs(1-V)**2/(dK*(1-theta)))
out=dict(scope='Finite symmetric positive moment fixtures; complete coefficient minima independently checked. These are diagnostics for exact identities, not a xi-packet numerical evaluation or proof of asymptotic estimates.',precision_digits=mp.mp.dps,checks=checks,passed=all(c['passed'] for c in checks))
(A/'FINITE_RECEIVER_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'passed':out['passed'],'checks':len(checks),'max_relative_error':max([float(c.get('relative_error',0)) for c in checks])}))
