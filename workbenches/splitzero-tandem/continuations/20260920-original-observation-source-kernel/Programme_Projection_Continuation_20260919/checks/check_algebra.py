"""Exact finite-field and rational diagnostics; not zeta-zero or period evaluations."""
from random import Random
from math import factorial
from pathlib import Path
import json
import sympy as s

checks=0
def require(v,msg):
    global checks
    if not v: raise RuntimeError(msg)
    checks+=1

# Basic scalar algebra responsible for the beta representation and reflection.
z,v=s.symbols('z v')
R=z**3-s.Rational(3,2)*z**2-z/4+s.Rational(3,8)
require(s.expand(R+R.subs(z,1-z))==0,'reflection polynomial')
P=z**2*(z-1)**2
q=s.div(v**2*(v-1)**2-P,v-z,v)[0]
mom={0:1,1:s.Rational(1,2),2:-s.Rational(1,4),3:-s.Rational(5,8)}
require(s.expand(sum(q.coeff(v,j)*mom[j] for j in mom)-R)==0,'monic division moments')
for m in range(1,9):
    H=s.Matrix(m,m,lambda i,j:s.Rational(1,factorial(i)*factorial(j)*(i+j+1)))
    Hi=H.inv()
    require(Hi[0,0]==m*m,'Hilbert inverse corner')
    if m>1:
        require(Hi[0,1]==-s.Rational(m*m*(m*m-1),2),'Hilbert inverse first cross')
    # Reversed resonant block; every nilpotent slot is retained.
    for i in range(m):
        for j in range(m):
            a=sum(s.Rational((-1)**(i-l),factorial(i-l)*factorial(l)*factorial(j)*(l+j+1)) for l in range(i+1))
            require(a==s.Rational((-1)**i,factorial(i+j+1)),'resonant beta coefficient')

# Highest-jet 2x2 inverse block in the full conjugate Cauchy Gram.
delta=s.Rational(2,7); gamma=s.Rational(17,5)
for m in range(1,5):
    roots=[delta+s.I*gamma,delta-s.I*gamma]
    inds=[(a,j) for a in range(2) for j in range(m)]
    G=s.Matrix(2*m,2*m,lambda i,j:(-1)**(inds[i][1]+inds[j][1])*s.binomial(inds[i][1]+inds[j][1],inds[i][1])/(s.conjugate(roots[inds[i][0]])+roots[inds[j][0]])**(inds[i][1]+inds[j][1]+1))
    inv=G.inv(); am=(2*delta)**(2*m-1)*((delta**2+gamma**2)/gamma**2)**m
    tm=(2*delta)**(2*m)*(2*delta+2*s.I*gamma)**(2*m-1)/(2*s.I*gamma)**(2*m)
    require(s.simplify(inv[m-1,m-1]-am)==0,'highest inverse diagonal')
    require(s.simplify(inv[m-1,2*m-1]-tm)==0,'highest inverse cross phase')

# A direct implementation of constant-depth reconstruction.
p=1000000007
rng=Random(181909)
def add_poly(a,b):
    out=[0]*max(len(a),len(b))
    for j,x in enumerate(a): out[j]=(out[j]+x)%p
    for j,x in enumerate(b): out[j]=(out[j]+x)%p
    return out

def mul_linear(a,root):
    out=[0]*(len(a)+1)
    for j,x in enumerate(a):
        out[j]=(out[j]-root*x)%p; out[j+1]=(out[j+1]+x)%p
    return out

def lagrange(nodes,j):
    a=[1]; den=1
    for l,root in enumerate(nodes):
        if l!=j: a=mul_linear(a,root); den=den*(nodes[j]-root)%p
    return [x*pow(den,-1,p)%p for x in a]

for k,support in [(17,[(0,4),(8,4),(4,0),(4,8)]),(21,[(0,0),(8,0),(0,8),(8,8),(3,5)]),(25,[(0,8),(8,0)])]:
    grid=[(a,b) for a in range(k+1) for b in range(k+1)]
    lower=[(a,b) for a in range(k-7) for b in range(k-7)]
    coeff=[j+2 for j in range(len(support))]
    first={}
    for b in lower:
        for j,t in enumerate(support): first.setdefault((b[0]+t[0],b[1]+t[1]),(b,j))
    missing=[g for g in grid if g not in first]
    require(len(missing)<=128,'fixed corner count')
    d=max(len(support)-1,len(missing)-1,1)
    require(d<=127,'fixed depth bound')
    # An injective root labelling and one nonzero output on each missing root.
    lam={g:(5+3*g[0]+(3*k+11)*g[1])%p for g in grid}
    require(len(set(lam.values()))==len(grid),'distinct diagnostic roots')
    x={g:rng.randrange(p) for g in grid}
    # Outputs contain literal conductor rows plus a full mixed row (not separate missing values).
    weights={g:rng.randrange(1,p) for g in grid}
    observations=[]
    for n in range(d+1):
        ob={}
        for b in lower:
            ob[b]=sum(coeff[j]*pow(lam[(b[0]+t[0],b[1]+t[1])],n,p)*x[(b[0]+t[0],b[1]+t[1])] for j,t in enumerate(support))%p
        ob['mixed']=sum(weights[g]*pow(lam[g],n,p)*x[g] for g in grid)%p
        observations.append(ob)
    recovered={}
    for g,(b,j) in first.items():
        nodes=[lam[(b[0]+t[0],b[1]+t[1])] for t in support]
        pol=lagrange(nodes,j)
        recovered[g]=sum(c*observations[n][b] for n,c in enumerate(pol))*pow(coeff[j],-1,p)%p
        require(recovered[g]==x[g],'conductor coordinate reconstruction')
        if g==next(iter(first)):
            omitted=sum(c*observations[n][b] for n,c in enumerate(pol))%p
            require(omitted!=x[g],'omitting the actual conductor coefficient is rejected')
    residual=[(observations[n]['mixed']-sum(weights[g]*pow(lam[g],n,p)*recovered[g] for g in first))%p for n in range(d+1)]
    nodes=[lam[g] for g in missing]
    for j,g in enumerate(missing):
        pol=lagrange(nodes,j)
        val=sum(c*residual[n] for n,c in enumerate(pol))*pow(weights[g],-1,p)%p
        require(val==x[g],'missing-corner reconstruction')
    require(len(first)+len(missing)==(k+1)**2,'complete grid recovered')


# All four edge selections: exact joint-corner bound used for the 81-observation theorem.
import itertools
for a0,a1,b0,b1 in itertools.product(range(9), repeat=4):
    hs=[a0*b0,a1*(8-b0),(8-a0)*b1,(8-a1)*(8-b1)]
    require(sum(hs)-max(hs)<=64,'three-corner bound')

# Joint-corner recovery, with output rows that mix all corners.
for k,support in [(17,[(0,4),(8,4),(4,0),(4,8)]),(25,[(0,8),(8,0)])]:
    grid=[(a,b) for a in range(k+1) for b in range(k+1)]
    lower=[(a,b) for a in range(k-7) for b in range(k-7)]
    coeff=[j+2 for j in range(len(support))]
    first={}
    for beta in lower:
        for j,t in enumerate(support): first.setdefault((beta[0]+t[0],beta[1]+t[1]),(beta,j))
    missing=[g for g in grid if g not in first]
    corner=[[],[],[],[]]
    for a,b in missing:
        idx=(0 if a<8 else 2)+(0 if b<8 else 1)
        corner[idx].append((a,b))
    corner.sort(key=len,reverse=True);corner=[c for c in corner if c]
    hmax=max([len(c) for c in corner],default=0)
    d=max(len(support)-1,len(missing)-hmax,1)
    require(d<=80,'81-observation cutoff')
    lam={g:(5+3*g[0]+(3*k+11)*g[1])%p for g in grid}
    x={g:rng.randrange(1,p) for g in grid}
    powers={g:[pow(lam[g],n,p) for n in range(d+hmax+1)] for g in grid}
    # Original-style conductor rows, enough to recover F.
    obs=[]
    for n in range(d+1):
        obs.append({b:sum(coeff[j]*powers[(b[0]+t[0],b[1]+t[1])][n]*x[(b[0]+t[0],b[1]+t[1])] for j,t in enumerate(support))%p for b in lower})
    rec={}
    for g,(b,j) in first.items():
        nodes=[lam[(b[0]+t[0],b[1]+t[1])] for t in support]
        pol=lagrange(nodes,j)
        rec[g]=sum(c*obs[n][b] for n,c in enumerate(pol))*pow(coeff[j],-1,p)%p
        require(rec[g]==x[g],'joint-recovery conductor step')
    # Output has only hmax mixed moment rows, not one row per missing coordinate.
    residual=[[sum(powers[g][n+j]*x[g] for g in grid)%p for j in range(hmax)] for n in range(d+1)]
    for n in range(d+1):
        for j in range(hmax): residual[n][j]=(residual[n][j]-sum(powers[g][n+j]*rec[g] for g in first))%p
    remaining=set(missing)
    for C in corner:
        outside=remaining.difference(C); pol=[1]
        for g in sorted(outside):pol=mul_linear(pol,lam[g])
        require(len(pol)-1<=64,'corner annihilator degree')
        filtered=[sum(c*residual[n][j] for n,c in enumerate(pol))%p for j in range(len(C))]
        nodes=[lam[g] for g in C]
        for i,g in enumerate(C):
            dual=lagrange(nodes,i)
            value=sum(c*filtered[j] for j,c in enumerate(dual))%p
            evalp=sum(c*powers[g][n] for n,c in enumerate(pol))%p
            rec[g]=value*pow(evalp,-1,p)%p
            require(rec[g]==x[g],'joint-corner recovery')
        for n in range(d+1):
            for j in range(hmax): residual[n][j]=(residual[n][j]-sum(powers[g][n+j]*rec[g] for g in C))%p
        remaining.difference_update(C)
    require(len(rec)==len(grid),'complete constant-depth recovery')
    require(all(v==0 for row in residual for v in row),'all mixed residual rows vanish')

# Negative controls: omitted original coefficient, and omitted source cross term.
t=s.symbols('t',positive=True)
require(s.expand((1+t)**2-(1+t*t))==2*t,'cross-term deletion rejected')
result={'exact_checks':checks,'status':'passed','scope':'rational and finite-field auxiliary identities; not actual zeta or period evaluations'}
print(json.dumps(result,indent=2))
Path(__file__).with_name('exact_receipt.json').write_text(json.dumps(result,indent=2)+'\n')
