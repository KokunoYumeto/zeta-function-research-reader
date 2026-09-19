"""Independent finite diagnostics for HM8, HM10--24; not xi-packet numerics."""
from pathlib import Path
import json, math
import numpy as np
from scipy.linalg import eigh
import mpmath as mp

OUT=Path(__file__).resolve().parent
rng=np.random.default_rng(20260919)
checks=[]
def add(name,error,tolerance=1e-10,**data):
    checks.append(dict(name=name,error=float(error),tolerance=tolerance,
                       passed=bool(error<=tolerance),**data))
def rand(m,n): return rng.normal(size=(m,n))+1j*rng.normal(size=(m,n))
def gram(a): return a.conj().T@a
def quotient(g,j): return np.linalg.inv(j@np.linalg.solve(g,j.conj().T))
def schur(g,d):
    return g[:d,:d]-g[:d,d:]@np.linalg.solve(g[d:,d:],g[d:,:d])
def cmp(name,a,b,lo,hi):
    ev=eigh(a,b,eigvals_only=True)
    add(name,max(0.,lo-ev[0],ev[-1]-hi),min_eigenvalue=float(ev[0]),max_eigenvalue=float(ev[-1]))
for case,(m,n,d,k) in enumerate([(7,4,2,2),(9,5,2,2),(6,3,1,3),(8,4,3,2)]):
    r=rand(m,n); p=r.copy();p[:,:d]=0
    g=gram(r);s=g[d:,d:];c=g[:d,d:];h=schur(g,d)
    # Compare the block formula with an independently formed full generalized eigenproblem.
    c2=1+eigh(c.conj().T@np.linalg.solve(h,c),s,eigvals_only=True)[-1]
    ce=eigh(gram(p),g,eigvals_only=True)[-1]
    add(f'{case}: full constant vs Schur block',abs(c2-ce)/max(1,ce))
    eps=.031;rank_budget=17
    target=min(.25,eps/(4*k*rank_budget))
    depth=max(0,math.ceil(2*math.log2(math.sqrt(c2)/target))-1)
    scale=2.**(-(depth+1)/2);delta=scale*math.sqrt(c2)
    # A finite unitary fixture satisfies exactly the dilation isometry relation.
    unitary,_=np.linalg.qr(rand(m,m)); t=scale*unitary
    rj=r-t@p;gj=gram(rj)
    exact=-r.conj().T@t@p-p.conj().T@t.conj().T@r+scale**2*gram(p)
    add(f'{case}: both cross terms',np.linalg.norm((gj-g)-exact)/np.linalg.norm(g))
    cmp(f'{case}: prequotient',gj,g,(1-delta)**2,(1+delta)**2)
    hj=schur(gj,d)
    cmp(f'{case}: actual relation minimum',hj,h,(1-delta)**2,(1+delta)**2)
    tg=g.copy();tj=gj.copy()
    for _ in range(k-1): tg=np.kron(tg,g);tj=np.kron(tj,gj)
    # Pull back the tensor metric through an injective coefficient map, then
    # compare a separately computed constrained inverse and kernel restriction.
    coeff=rand(n**k,6);a=coeff.conj().T@tg@coeff;aj=coeff.conj().T@tj@coeff
    lo=(1-delta)**(2*k);hi=(1+delta)**(2*k)
    cmp(f'{case}: tensor coefficient pullback',aj,a,lo,hi)
    j=rand(3,6);q=quotient(a,j);qj=quotient(aj,j)
    cmp(f'{case}: tensor quotient',qj,q,lo,hi)
    _,_,vh=np.linalg.svd(j,full_matrices=True);frame=vh.conj().T[:,3:]
    ker=frame.conj().T@a@frame;kerj=frame.conj().T@aj@frame
    cmp(f'{case}: original fixed kernel',kerj,ker,lo,hi)
    lift=np.linalg.solve(a,j.conj().T)@q
    add(f'{case}: original minimum-norm lift',np.linalg.norm(gram(np.linalg.cholesky(a).conj().T@lift)-q)/np.linalg.norm(q))
    error=abs(np.linalg.slogdet(qj)[1]-np.linalg.slogdet(q)[1])
    bound=2*k*3*(-math.log1p(-delta))
    add(f'{case}: determinant rank bound',max(0.,error-bound),actual_error=error,bound=bound)
    budget=2*k*rank_budget*(-math.log1p(-delta))
    add(f'{case}: finite chosen budget',max(0.,budget-eps),depth=depth,delta=delta,budget=budget,target_error=eps)

# Full confluent frame and nilpotent grade receivers, including mixed-grade
# cross terms, repeated primary states, and sorted singular values.
roots=[-2-1j,-.4+.7j,.8+.4j,2.1-.6j]; mult=[2,2,3,3]
pairs=[(a,j) for a,m in enumerate(mult) for j in range(m)]
q=sum(mult)
v=np.array([[math.comb(n,j)*roots[a]**(n-j) if n>=j else 0 for n in range(q)] for a,j in pairs])
weights=[mult[a]-1-2*j for a,j in pairs]
order=sorted(range(q),key=lambda i:weights[i]);cm=np.linalg.inv(v)[:,order]
r=rand(q+4,q);p=r.copy();p[:,:4]=0;g=gram(r)
ce=eigh(gram(p),g,eigvals_only=True)[-1]
delta=.003;sc=delta/math.sqrt(ce)
unitary,_=np.linalg.qr(rand(q+4,q+4));gj=gram(r-sc*unitary@p)
bm=cm.conj().T@g@cm;bmj=cm.conj().T@gj@cm
grades={};gradesj={};prod=1.;prodj=1.
for a in sorted(set(weights)):
    low=[i for i,z in enumerate(order) if weights[z]<a]
    cur=[i for i,z in enumerate(order) if weights[z]==a]
    def grade(b):
        out=b[np.ix_(cur,cur)]
        if low:out=out-b[np.ix_(cur,low)]@np.linalg.solve(b[np.ix_(low,low)],b[np.ix_(low,cur)])
        return (out+out.conj().T)/2
    ga=grade(bm);gaj=grade(bmj);grades[a]=ga;gradesj[a]=gaj
    cmp(f'grade {a}: full original Schur minimum',gaj,ga,(1-delta)**2,(1+delta)**2)
    prod*=np.linalg.det(ga).real;prodj*=np.linalg.det(gaj).real
for a in [0,1,2]:
    source=[pairs[z] for z in order if weights[z]==a]
    target=[pairs[z] for z in order if weights[z]==-a]
    ta=np.zeros((len(target),len(source)))
    for j,(root,degree) in enumerate(source):ta[target.index((root,degree+a)),j]=1
    eig=eigh(ta.T@grades[-a]@ta,grades[a],eigvals_only=True)
    eigj=eigh(ta.T@gradesj[-a]@ta,gradesj[a],eigvals_only=True)
    error=float(np.max(np.abs(np.log(eigj/eig))))
    bound=2*math.log((1+delta)/(1-delta))
    add(f'grade {a}: sorted induced singular values',max(0.,error-bound),actual_error=error,bound=bound)
# The confluent frame makes repeated double-precision Schur subtraction lose
# digits. Recompute the complete determinant identity from the original columns
# at 100 digits, rather than weakening its tolerance.
mp.mp.dps=100
def to_mp(z): return mp.mpc(str(complex(z).real),str(complex(z).imag))
vm=mp.matrix([[mp.binomial(n,j)*to_mp(roots[a])**(n-j) if n>=j else 0 for n in range(q)] for a,j in pairs])
vi=vm**-1; cmm=mp.matrix([[vi[i,j] for j in order] for i in range(q)])
for name,rr in [('full original',r),('heat',r-sc*unitary@p)]:
    rm=mp.matrix([[to_mp(x) for x in row] for row in rr]);gm=rm.H*rm;bb=cmm.H*gm*cmm;pp=mp.mpf(1)
    for a in sorted(set(weights)):
        low=[i for i,z in enumerate(order) if weights[z]<a];cur=[i for i,z in enumerate(order) if weights[z]==a]
        sub=lambda rows,cols:mp.matrix([[bb[i,j] for j in cols] for i in rows])
        ga=sub(cur,cur)
        if low:ga=ga-sub(cur,low)*(sub(low,low)**-1)*sub(low,cur)
        pp*=mp.det(ga)
    err=abs(abs(mp.det(vm))**2*pp/mp.det(gm)-1)
    add(name+' root-difference determinant (100 digits)',err,1e-80)

# Direct old-circle finite telescope, independent positive theta and odd sums.
mp.mp.dps=60
for xs in ['0.23','0.7','1.5']:
    x=mp.mpf(xs)
    for depth in range(3):
        s=mp.mpf(2)**(depth+1)
        theta=lambda a:1+2*mp.fsum(mp.exp(-mp.pi*n*n*a*a) for n in range(1,121))
        heat=mp.fsum(2*mp.fsum(mp.exp(-mp.pi*(2**j*x)**2*n*n) for n in range(1,241,2)) for j in range(depth+1))
        diff=theta(x)-theta(s*x)
        add(f'heat telescope x={xs}, J={depth}',abs(heat-diff),1e-50)
        # Source HM9 by independently summing all integers and dyadic odd integers.
        phi=lambda a:(4*mp.pi**2*a**4-6*mp.pi*a*a)*mp.exp(-mp.pi*a*a)
        f=lambda a:2*mp.fsum(phi(n*a) for n in range(1,121))
        heat_phi=2*mp.fsum(mp.fsum(phi((2**j)*n*x) for n in range(1,241,2)) for j in range(depth+1))
        add(f'original source x={xs}, J={depth}',abs(f(x)-f(s*x)-heat_phi),1e-49)

receipt=dict(scope='Finite complex Hilbert-space fixtures for full-Gram, cross-term, minimum, tensor and determinant maps; direct theta/odd heat sums. Not actual numerical xi-packet evaluations and not formal verification.',
             seed=20260919,checks=checks,passed=sum(c['passed'] for c in checks),total=len(checks))
(OUT/'FINITE_HEAT_RECEIVER_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['passed','total','scope']}))
assert receipt['passed']==receipt['total']
