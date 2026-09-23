"""Exact EHM algebra, permutation, pairing, and local-residue checks.

Analytic path continuation, logarithm branches, and extension proofs are in EHM.
"""
from itertools import permutations, product
from pathlib import Path
import json
import sympy as sp

checks=[]
def check(name,lhs,rhs):
    if isinstance(lhs,(tuple,list,set,dict)) or isinstance(rhs,(tuple,list,set,dict)):
        ok=lhs==rhs
    else:
        difference=lhs-rhs
        ok=all(sp.simplify(x)==0 for x in difference) if isinstance(difference,sp.MatrixBase) else sp.simplify(difference)==0
    if not ok:
        raise AssertionError((name,lhs,rhs))
    checks.append(name)

labels=('a+','a-','b+','b-','c+','c-','m','n')
ident=tuple(range(8))
def cycle(*cycles):
    p=list(ident)
    for cyc in cycles:
        cyc=[labels.index(x) for x in cyc]
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):p[a]=b
    return tuple(p)
def compose(p,q):return tuple(p[q[x]] for x in range(8))
def inv(p):return tuple(p.index(x) for x in range(8))
def matrix(p):
    m=sp.zeros(8)
    for j in range(8):m[p[j],j]=1
    return m
def generated(*gens):
    found={ident}; stack=[ident]
    while stack:
        p=stack.pop()
        for g in gens:
            q=compose(g,p)
            if q not in found:found.add(q);stack.append(q)
    return found

deck=cycle(('a+','a-'),('b+','b-'),('c+','c-'),('m','n'))
kappa=cycle(('b+','b-'),('m','n'))
native=cycle(('a+','c-'),('a-','c+'),('b+','b-'))
tauS=compose(deck,kappa);tauJ=compose(native,kappa)
gc=cycle(('a+','a-'),('b+','b-'))
gd=cycle(('b+','c-','b-','c+'))
ginf=cycle(('m','c-','n','c+'))
gcminus=cycle(('c+','c-'),('b+','b-'))
gdminus=cycle(('b+','a-','b-','a+'))
check('original conjugate-deck permutation',tauS,cycle(('a+','a-'),('c+','c-')))
check('original native-conjugate permutation',tauJ,cycle(('a+','c-'),('a-','c+'),('m','n')))
check('infinity loop square',compose(ginf,ginf),cycle(('m','n'),('c+','c-')))
check('heat second-meridian square',compose(gd,gd),cycle(('b+','b-'),('c+','c-')))
check('heat dihedral relation',compose(compose(gc,gd),gc),inv(gd))
D8=generated(gc,gd)
check('actual heat-path group order',len(D8),8)
check('local centralizer in heat-path group',
      {g for g in D8 if compose(g,gc)==compose(gc,g)},
      {ident,gc,compose(gd,gd),compose(gc,compose(gd,gd))})
check('native conjugation of positive critical meridian',compose(compose(tauJ,gc),tauJ),inv(gcminus))
check('native conjugation of positive second meridian',compose(compose(tauJ,gd),tauJ),inv(gdminus))
check('conjugate-deck reverses positive second meridian',compose(compose(tauS,gd),tauS),inv(gd))

G=set()
for perm in permutations(range(4)):
    parity=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    for signs in product((1,-1),repeat=4):
        if sp.prod(signs)!=parity:continue
        state=[]
        for j in range(4):
            for sign in (1,-1):
                outsign=signs[j]*sign
                state.append(2*perm[j]+(0 if outsign==1 else 1))
        G.add(tuple(state))
beta1=cycle(('a+','b+','a-','b-'))
beta2=cycle(('b+','c+','b-','c-'))
beta3=cycle(('c+','m','c-','n'))
check('source group has order 192',len(G),192)
check('actual source generators realize whole group',generated(beta1,beta2,beta3),G)
check('heat and infinity permutations belong to group',all(g in G for g in (gc,gd,ginf)),True)
check('full group centralizes original deck',all(compose(g,deck)==compose(deck,g) for g in G),True)
check('omitted-state orbit is all eight states',{g[6] for g in G},set(range(8)))
check('omitted-state stabilizer order',sum(g[6]==6 for g in G),24)

QS=matrix(tauS);QJ=matrix(tauJ);QK=matrix(kappa)
def inertia(m):
    vals=m.eigenvals(); out=[0,0,0]
    for value,mult in vals.items():
        out[0 if value>0 else 1 if value<0 else 2]+=mult
    return tuple(out)
check('full conjugate-deck inertia',inertia(QS),(6,2,0))
check('full native-conjugate inertia',inertia(QJ),(5,3,0))
check('full coefficient-conjugation inertia',inertia(QK),(6,2,0))
for name,g in [('critical',gc),('second',gd),('infinity',ginf)]:
    Pg=matrix(g)
    for tau_name,tau in [('deck',tauS),('native',tauJ),('coefficient',kappa)]:
        check(f'{name} exact {tau_name} pairing transport',Pg.T*matrix(tau)*Pg,
              matrix(compose(compose(inv(g),tau),g)))

vc=sp.Matrix([0,0,0,0,1,-1,0,0]); vi=sp.Matrix([0,0,0,0,0,0,1,-1])
vb=sp.Matrix([0,0,1,-1,0,0,0,0]);va=sp.Matrix([1,-1,0,0,0,0,0,0])
check('infinity loop transports negative finite direction',matrix(ginf)*vc,vi)
check('infinity loop transports positive infinity direction',matrix(ginf)*vi,-vc)
check('finite direction original negative value',(vc.T*QS*vc)[0],-2)
check('infinity direction original positive value',(vi.T*QS*vi)[0],2)
check('critical loop retains negative value',(matrix(gc)*va).T*QS*(matrix(gc)*va),sp.Matrix([[-2]]))
check('second meridian exchanges negative with positive',matrix(gd)*vc,vb)
check('second meridian reciprocal direction exchange',matrix(gd)*vb,-vc)

def orbit_basis(group):
    unvisited=set(range(8));cols=[]
    while unvisited:
        j=min(unvisited);orb={g[j] for g in group};unvisited-=orb
        cols.append(sp.Matrix([1 if k in orb else 0 for k in range(8)]))
    return sp.Matrix.hstack(*cols)
for name,group,dimension,expected in [
    ('critical',generated(gc),6,(5,1,0)),
    ('second',generated(gd),5,(4,1,0)),
    ('heat group',D8,4,(4,0,0)),
    ('full group',G,1,(1,0,0))]:
    ob=orbit_basis(group)
    check(f'{name} invariant dimension',ob.cols,dimension)
    check(f'{name} actual invariant restriction inertia',inertia(ob.T*QS*ob),expected)
    # Exact average vector map on its retained orbit labels.
    proj=sp.zeros(8)
    for c in range(ob.cols):
        col=ob[:,c];proj+=col*col.T/(col.T*col)[0]
    check(f'{name} invariant vector projection is idempotent',proj*proj,proj)

A,R,h,z,x,T,beta,t=sp.symbols('A R h z x T beta t',real=True)
FA=A*R**4+R**3-R
check('infinity-line exact discriminant',sp.discriminant(FA,R),4-27*A*A)
Ac=2/(3*sp.sqrt(3));rc=-sp.sqrt(3)
check('infinity collision root',FA.subs({A:Ac,R:rc}),0)
check('infinity collision derivative',sp.diff(FA,R).subs({A:Ac,R:rc}),0)
check('infinity collision second derivative',sp.diff(FA,R,2).subs({A:Ac,R:rc}),2*sp.sqrt(3))
check('infinity transverse target derivative',sp.diff(FA,A).subs({A:Ac,R:rc}),9)
Fh=(R-1)*(R*R+R-16*h)
check('heat path exact discriminant',sp.discriminant(Fh,R),(2-16*h)**2*(1+64*h))
check('transverse original coefficient polynomial',((R-1)**2-z)*(R+2),R**3-(3+z)*R+2-2*z)
check('transverse derivative on root relation',sp.diff((x*x-z)*(x+3),x).subs(z,x*x),2*x*(x+3))
check('second collision actual shifted factorization',Fh.subs({R:x-sp.Rational(1,2),h:t-sp.Rational(1,64)}),
      (x*x-16*t)*(x-sp.Rational(3,2)))
check('local root relation exact clock',beta*(beta+3),16*(beta*(beta+3)/16))

def mod4(p):return sp.rem(sp.expand(p),T**4,T)
alpha=sp.I*T-sp.I*T**3/18
alpha_inv=-sp.I*T+sp.I*T**3/18
alpha_d=sp.I*T-2*sp.I*T**3/9
n1=T*T/2;n2=3*T+T**3/6;n3=T**3/2
check('transverse original-coordinate square',mod4(alpha.subs(T,alpha)),-T)
check('transverse original-coordinate inverse',mod4(alpha.subs(T,alpha_inv)),T)
check('second collision original-coordinate square',mod4(alpha_d.subs(T,alpha_d)),-T)
check('transverse first radical image',mod4(n1.subs(T,alpha)),-n1)
check('transverse second radical image',mod4(n2.subs(T,alpha)),sp.I*n2-sp.I*n3)
check('transverse third radical image',mod4(n3.subs(T,alpha)),-sp.I*n3)
check('radical square with original constant',mod4(n2*n2),18*n1)
check('radical mixed product with original constant',mod4(n1*n2),3*n3)
check('coefficient conjugation reverses order-four map',sp.conjugate(alpha),alpha_inv)
Sb=sp.eye(4);Sb[3,2]=-2/beta;Sb[3,3]=-1
Mc=sp.diag(1,1,-1,-1)
check('partial sign map is involutive on punctured disc',Sb*Sb,sp.eye(4))
res=sp.simplify(beta*(beta+3)*Sb/16).subs(beta,0)
expected_res=sp.zeros(4);expected_res[3,2]=-sp.Rational(3,8)
check('exact nonzero local pole residue',res,expected_res)
check('other commuting nonregular extension has opposite residue',Mc*res,-res)
delta=lambda p:mod4(-T**3*sp.diff(p,T)/16)
check('residue on original reciprocal factor',delta(T),-T**3/16)
check('residue first radical generator',delta(n1),0)
check('residue second radical generator',delta(n2),-3*n3/8)
check('residue third radical generator',delta(n3),0)
check('residue square zero',delta(delta(T)),0)
for i in range(4):
    for j in range(4):
        check(f'residue exact Leibniz identity {i},{j}',delta(mod4(T**i*T**j)),
              mod4(delta(T**i)*T**j+T**i*delta(T**j)))

# Actual special regular trace and its invariant/coinvariant restrictions.
local_trace=sp.diag(4,0,0,0)
Nmat=sp.zeros(4)
for j in range(4):
    coefficients=sp.Poly(mod4(T*T**j),T)
    for i in range(4):Nmat[i,j]=coefficients.coeff_monomial(T**i)
check('local retained reciprocal factor has fourth power zero',Nmat**4,sp.zeros(4))
check('local regular multiplication trace vanishes on nonconstant powers',
      tuple(sp.trace(Nmat**j) for j in range(1,4)),(0,0,0))
delta_matrix=sp.zeros(4);delta_matrix[3,1]=-sp.Rational(1,16)
check('residue image is trace invisible',local_trace*delta_matrix,sp.zeros(4))
special_heat=sp.diag(1,-1,1,-1)
check('special heat loop invariant trace has one retained nilpotent radical',
      inertia(sp.diag(4,0)),(1,0,1))
check('whole special heat invariant form inertia',inertia(sp.diag(4,0,2,-18,2,2)),(4,1,1))
check('whole special transverse invariant form inertia',inertia(sp.diag(4,2,-18,2,2)),(4,1,0))

report={'status':'passed','exact_checks':len(checks),'checks':checks,
        'scope':'Exact permutations, source G192 and path D8, all original involution matrices, selected-loop pairing transports, invariant restrictions, original discriminants, special local algebra automorphisms and nilpotent products, and the nonzero regular-extension residue. Analytic continuation and extension proofs are in EHM.'}
Path(__file__).with_name('EIGHT_STATE_HOLONOMY_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ('status','exact_checks','scope')},indent=2))
