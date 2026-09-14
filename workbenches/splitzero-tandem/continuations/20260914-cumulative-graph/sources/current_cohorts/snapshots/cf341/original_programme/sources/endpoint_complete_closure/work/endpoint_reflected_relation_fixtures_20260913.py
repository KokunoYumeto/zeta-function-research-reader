"""Exact finite polynomial-map fixtures for RF.1--RF.17; no zero-location claim."""
from pathlib import Path
import hashlib
import json
import sys

W=Path(__file__).resolve().parent
dependency=W/'kernel_layer_replay_dependencies_20260912'
if dependency.is_dir(): sys.path.insert(0,str(dependency))
import sympy as sp
if sp.__version__!='1.14.0': raise RuntimeError('Require SymPy 1.14.0')
S,u=sp.symbols('S u')
ii=sp.I

def rem(f,m,x=S): return sp.rem(sp.Poly(f,x,extension=ii),sp.Poly(m,x,extension=ii)).as_expr().expand()
def degree(f,x=S): return sp.degree(f,x)
def bar(f,x=S):
    p=sp.Poly(f,x)
    return sum(sp.conjugate(p.nth(j))*x**j for j in range(int(p.degree())+1)).expand()
def star(f): return bar(f).subs(S,2-S).expand()
def dagger(f): return ((-1)**degree(f)*star(f)).expand()
def vec(f,m,x=S):
    p=sp.Poly(rem(f,m,x),x)
    return sp.Matrix([p.nth(j) for j in range(degree(m,x))])
def residue(m,n): return sp.Matrix.hstack(*(vec(S**j,n) for j in range(degree(m))))
def mult(f,m,x=S): return sp.Matrix.hstack(*(vec(f*x**j,m,x) for j in range(degree(m,x))))
def equal(a,b):
    if isinstance(a,sp.MatrixBase) or isinstance(b,sp.MatrixBase):
        return a.shape==b.shape and all(sp.expand(x-y)==0 for x,y in zip(a,b))
    return sp.expand(a-b)==0
def pstr(f): return str(sp.expand(f))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(case,name,condition):
    ok=bool(condition)
    checks.append({'fixture':case,'name':name,'passed':ok})
    if not ok: raise RuntimeError(case+': '+name)

A=S-(2+ii); B=S-ii; F=S-(1+3*ii)
fixtures=[
 ('mixed',A**2*B,[(2+ii,2,1),(ii,1,2)],3),
 ('disjoint',A**2,[(2+ii,2,0),(ii,0,2)],None),
 ('stable_pair',A**2*B**2,[(2+ii,2,2),(ii,2,2)],2),
 ('stable_fixed_root',F**3,[(1+3*ii,3,3)],2),
]
rows=[]
for name,chi,rootdata,nilpotence in fixtures:
    chi=sp.expand(chi); q=int(degree(chi)); dag=dagger(chi)
    g=sp.Poly(sp.gcd(chi,dag),S).monic().as_expr()
    N=sp.expand(chi*dag); chi2=sp.expand(chi**2)
    d=sp.expand(chi*g); ell=sp.div(chi2*dag,g,S)[0].expand()
    check(name,'dagger root multiplicities',equal(dag,sp.prod((S-lam)**b for lam,a,b in rootdata)))
    check(name,'dagger involution and monicity',equal(dagger(dag),chi) and sp.LC(sp.Poly(dag,S))==1)
    check(name,'star fixes norm polynomial',equal(star(N),N))
    check(name,'gcd and lcm at every original root order',equal(d,sp.prod((S-lam)**(a+min(a,b)) for lam,a,b in rootdata)) and equal(ell,sp.prod((S-lam)**(a+max(a,b)) for lam,a,b in rootdata)))
    psi=sp.expand(ii**(-q)*chi.subs(S,1+ii*u)); Pi=sp.expand(psi*bar(psi,u))
    check(name,'original leading phases',equal(dag.subs(S,1+ii*u),ii**q*bar(psi,u)) and equal(N.subs(S,1+ii*u),ii**(2*q)*Pi))
    check(name,'real monic norm polynomial',equal(Pi,bar(Pi,u)) and sp.LC(sp.Poly(Pi,u))==1)
    Q=S**2+(2-3*ii)*S+(1+ii)
    Qtilde=sp.expand(Q.subs(S,1+ii*u)); relation=sp.expand((chi*Q).subs(S,1+ii*u))
    check(name,'pointwise norm identity for nonreal test polynomial',equal(relation*bar(relation,u),Pi*Qtilde*bar(Qtilde,u)))
    coord=sp.Matrix.hstack(*(vec((1+ii*u)**j,Pi,u) for j in range(2*q)))
    inv=sp.Matrix.hstack(*(vec(((S-1)/ii)**j,N) for j in range(2*q)))
    check(name,'full quotient coordinate maps are mutual inverses',equal(coord*inv,sp.eye(2*q)) and equal(inv*coord,sp.eye(2*q)))
    check(name,'original S action under coordinate change',equal(coord*mult(S,N),(sp.eye(2*q)+ii*mult(u,Pi,u))*coord))
    jetrows=[]; uprows=[]; multip=[]; signperm=sp.zeros(2*q); rowindices={}
    for lam,a,b in rootdata:
        r=a+b
        for j in range(r):
            rowindices[(lam,j)]=len(jetrows)
            jetrows.append([sp.diff(S**n,S,j).subs(S,lam) for n in range(2*q)])
            uprows.append([sp.diff(u**n,u,j).subs(u,(lam-1)/ii) for n in range(2*q)])
            multip.append((lam,j))
    jets=sp.Matrix(jetrows); jetsu=sp.Matrix(uprows); block=sp.zeros(2*q)
    for i,(lam,j) in enumerate(multip):
        block[i,i]=lam
        if j: block[i,i-1]=j
        signperm[i,rowindices[(2-sp.conjugate(lam),j)]]=(-1)**j
    phases=sp.diag(*[ii**j for lam,j in multip])
    det_expected=sp.prod(sp.factorial(j) for lam,a,b in rootdata for j in range(a+b))
    det_expected*=sp.prod((rootdata[b][0]-rootdata[a][0])**((rootdata[a][1]+rootdata[a][2])*(rootdata[b][1]+rootdata[b][2])) for a in range(len(rootdata)) for b in range(a+1,len(rootdata)))
    check(name,'raw-derivative determinant with factorials and root order',equal(jets.det(),det_expected) and det_expected!=0)
    check(name,'raw-jet S action with derivative coefficient',equal(jets*mult(S,N),block*jets))
    check(name,'all raw coordinate derivative phases',equal(jetsu*coord,phases*jets))
    reflect=sp.Matrix.hstack(*(vec((2-S)**j,N) for j in range(2*q)))
    check(name,'semilinear reflected raw jets and derivative signs',equal(jets*reflect,signperm*sp.conjugate(jets)))
    check(name,'semilinear reflection squares to identity',equal(reflect*sp.conjugate(reflect),sp.eye(2*q)))
    # One polynomial product with nonzero high jets checks the stated raw product.
    P=S**(2*q-1)+(1+ii)*S+3; T=S**(2*q-2)+(2-ii)*S+5
    vp=jets*vec(P,N); vt=jets*vec(T,N); product=[]
    for lam,a,b in rootdata:
        start=rowindices[(lam,0)]
        for j in range(a+b): product.append(sum(sp.binomial(j,h)*vp[start+h]*vt[start+j-h] for h in range(j+1)))
    check(name,'raw-jet Leibniz algebra product',equal(jets*vec(P*T,N),sp.Matrix(product)))
    injection=sp.Matrix.hstack(*(vec(chi*S**j,N) for j in range(q)))
    projection=residue(N,chi)
    check(name,'RF10 complete module exactness',injection.rank()==q and projection.rank()==q and equal(projection*injection,sp.zeros(q,q)))
    check(name,'RF10 exact original S-module intertwining',equal(mult(S,N)*injection,injection*mult(S,dag)))
    check(name,'RF10 exact annihilator generator',equal(mult(dag,N)*injection,sp.zeros(2*q,q)) and injection.rank()==q)
    J=residue(ell,chi2).col_join(residue(ell,N)); Tmap=residue(chi2,d).row_join(-residue(N,d))
    check(name,'RF13 fibre-product exactness and dimensions',J.rank()==degree(ell) and Tmap.rank()==degree(d) and equal(Tmap*J,sp.zeros(degree(d),degree(ell))) and degree(ell)+degree(d)==4*q)
    check(name,'RF14 unit and S-generated algebra map',equal(J*mult(S,ell),sp.diag(mult(S,chi2),mult(S,N))*J) and equal(J[:,0],sp.eye(2*q)[:,0].col_join(sp.eye(2*q)[:,0])))
    common=residue(d,chi)
    check(name,'two reductions agree at original arithmetic quotient',equal(common*residue(chi2,d),residue(chi2,chi)) and equal(common*residue(N,d),projection))
    left=sp.Matrix.hstack(*(vec(chi*S**j,chi2) for j in range(q)))
    mid=sp.Matrix.hstack(*(vec(chi*S**j,d) for j in range(int(degree(g))))) if degree(g)>0 else sp.zeros(degree(d),0)
    leftres=residue(chi,g) if degree(g)>0 else sp.zeros(0,q)
    rightres=residue(dag,g) if degree(g)>0 else sp.zeros(0,q)
    check(name,'RF15 literal multiplication-by-chi kernel diagram',equal(residue(chi2,d)*left,mid*leftres) and equal(residue(N,d)*injection,mid*rightres))
    square=rem(chi**2,N); stable=equal(chi,dag)
    check(name,'norm kernel square-zero iff dagger-stable',equal(square,0)==stable)
    check(name,'A_chi scalar action exists iff dagger-stable',equal(mult(chi,N)*injection,sp.zeros(2*q,q))==stable)
    # Transported multiplication on C[S]/dagger is [f] diamond [g]=[chi*f*g].
    f=1+(2+ii)*S; h=S**2+3
    check(name,'literal kernel module parametrization carries twisted algebra product',equal(rem(chi*f*chi*h,N),rem(chi*rem(chi*f*h,dag),N)))
    if nilpotence is not None:
        check(name,'exact kernel nilpotence index',equal(rem(chi**nilpotence,N),0) and not equal(rem(chi**(nilpotence-1),N),0))
    details={'fixture':name,'chi':pstr(chi),'dagger':pstr(dag),'g':pstr(g),'d':pstr(d),'N':pstr(N),'ell':pstr(ell),
      'root_orders':[{'root':str(lam),'a':a,'b':b,'g':min(a,b),'d':a+min(a,b),'N':a+b,'ell':a+max(a,b)} for lam,a,b in rootdata],
      'dimensions':{'A_chi':q,'A_N':2*q,'A_2':2*q,'base':int(degree(d)),'fibre_product':int(degree(ell))},
      'raw_jet_determinant':str(sp.expand(det_expected)),'chi_squared_residue_mod_N':pstr(square),'kernel_nilpotence_index':nilpotence,
      'source_annihilator_for_norm_kernel':pstr(dag),'dagger_stable':stable}
    if degree(g)==0:
        bez_u,bez_v,one=sp.gcdex(chi,dag,S)
        check(name,'literal Bezout identity',equal(bez_u*chi+bez_v*dag,1))
        eref=rem(bez_u*chi,N)
        check(name,'reflected idempotent and original supported-zero amplitude',equal(rem(eref**2-eref,N),0) and equal(rem(eref,chi),0) and equal(rem(eref,dag),1) and not equal(eref,0))
        a=S+3*ii; b=S**2+(1-ii)
        inverse=rem(a*bez_v*dag+b*bez_u*chi,N)
        check(name,'explicit coprime CRT inverse with original residues',equal(rem(inverse-a,chi),0) and equal(rem(inverse-b,dag),0))
        details.update({'bezout_u':pstr(bez_u),'bezout_v':pstr(bez_v),'reflected_idempotent':pstr(eref)})
    rows.append(details)

source=W/'endpoint_reflected_relation_fibre_product_20260913.tex'
out={'scope':'Exact rational-complex polynomial fixtures for finite algebra/module/jet maps only; no numerical approximation, arithmetic packet realization or zero-location claim.',
     'sympy':sp.__version__,'source_path':source.name,'source_sha256':sha(source),'checker_sha256':sha(Path(__file__)),
     'passed':len(checks),'failed':0,'fixtures':rows,'checks':checks}
target=W/'endpoint_reflected_relation_fixtures_20260913.json'
target.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'failed':0,'result_sha256':sha(target),'fixtures':rows},indent=2))
