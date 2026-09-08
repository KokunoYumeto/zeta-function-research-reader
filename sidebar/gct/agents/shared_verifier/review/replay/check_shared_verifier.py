"""Reproduce exact bounded checks independently of the TeX and external sources.

Python >=3.10 and SymPy are the only dependencies. Run from any directory.
The unbounded assertions are proved in shared_verifier.tex; sampled matrix
identities here are explicitly distinguished from symbolic polynomial checks.
No Lean process, network call, or repository-root write is performed.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import platform
import time

import sympy as sp

ROOT = Path(__file__).resolve().parent
COUNTS = Counter()
EVIDENCE = {}


def check(group, condition, context=""):
    if not bool(condition):
        raise AssertionError(f"{group}: {context}")
    COUNTS[group] += 1


def source_checks():
    x, y, w, X, B, r, a, b, c = sp.symbols("x y w X B r a b c")
    F1 = (1+x*y)**3*w + y*y*(1+x*y)*(4+3*x*y)
    F2 = y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y)
    F3 = 2*x-3*x*x*y-x**3*w
    check("original Jacobian", sp.expand(sp.det(sp.Matrix([F1,F2,F3]).jacobian([x,y,w]))) == -2)
    original = [F1+sp.Rational(1,4), F2, F3]
    triangular = [y+3*x/2, w-(27*x*x-1)/4, x**3-x]
    g_original = sp.groebner(original, w,y,x, domain=sp.QQ)
    g_triangular = sp.groebner(triangular, w,y,x, domain=sp.QQ)
    for f in triangular:
        check("full original fibre ideals", g_original.reduce(f)[1] == 0)
    for f in original:
        check("full original fibre ideals", g_triangular.reduce(f)[1] == 0)
    EVIDENCE["original_fibre_groebner_basis"] = [str(f) for f in g_original.polys]
    for z in (-1,0,1):
        source = {x:z, y:sp.Rational(-3*z,2), w:sp.Rational(27*z*z-1,4)}
        check("retained source points", [sp.expand(f.subs(source)) for f in (F1,F2,F3)] == [-sp.Rational(1,4),0,0])
    ids = [(X*X-X)/2,1-X*X,(X*X+X)/2]
    for i,j in product(range(3),repeat=2):
        check("rational CRT idempotents", sp.rem(ids[i]*ids[j]-(ids[i] if i==j else 0),X**3-X,X)==0)
    check("rational CRT identity", sp.expand(sum(ids))==1)
    evaluation = sp.Matrix([[1,-1,1],[1,0,0],[1,1,1]])
    check("integral evaluation index", abs(evaluation.det()) == 2)
    for u,v,z in product(range(-2,3),repeat=3):
        coeffs = evaluation.inv()*sp.Matrix([u,v,z])
        check("integral image parity", all(t.q==1 for t in coeffs) == ((u-z)%2==0))
        in_conductor = all((u*du-z*dz)%2==0 for du,dv,dz in product((0,1),repeat=3))
        check("integral conductor", in_conductor == (u%2==0 and z%2==0))
    P = c*r**3-2*r*r+b*r-2*a
    Pprime = sp.diff(P,r)
    subst = {a:-sp.Rational(1,4), b:0, c:0, r:(1-2*B)/2}
    relation = B*B-B
    check("incidence original cubic", sp.expand(P.subs(subst)) == -2*relation)
    dp = sp.expand(Pprime.subs(subst))
    check("incidence derivative", dp == 4*B-2)
    check("incidence localization inverse", sp.expand(dp*(B-sp.Rational(1,2))-1)==4*relation)
    alpha=dp/2
    source_image = [2*B-1, sp.expand(subst[r]-alpha), sp.expand(5*alpha**2-3*subst[r]*alpha)]
    for f,want in zip(source_image,[2*B-1,sp.Rational(3,2)-3*B,sp.Rational(13,2)]):
        check("incidence source recovery",sp.rem(f-want,relation,B)==0)
    for f in original:
        check("incidence original target recovery",sp.rem(sp.expand(f.subs(dict(zip((x,y,w),source_image)), simultaneous=True)),relation,B)==0)
    check("incidence Boolean inverse",sp.expand((source_image[0]+1)/2)==B)


class Fibre:
    """Exact monomial quotient Q[X_i]/(X_i^3-X_i), no CRT evaluation."""
    def __init__(self,n):
        self.n=n
        self.basis=list(product(range(3),repeat=n))
        self.zero=(0,)*n
        self.one={self.zero:F(1)}

    def add(self,*polys):
        d=defaultdict(F)
        for p in polys:
            for e,v in p.items():
                d[e]+=v
        return {e:v for e,v in d.items() if v}

    def scale(self,p,c):
        return {e:v*c for e,v in p.items() if v*c}

    def mul(self,p,q):
        d=defaultdict(F)
        for u,a in p.items():
            for v,b in q.items():
                e=tuple(0 if i+j==0 else (1 if (i+j)%2 else 2) for i,j in zip(u,v))
                d[e]+=a*b
        return {e:v for e,v in d.items() if v}

    def prod(self,ps):
        ans=self.one
        for p in ps:
            ans=self.mul(ans,p)
        return ans

    def var(self,i,power):
        e=list(self.zero);e[i]=power
        return {tuple(e):F(1)}

    def beta(self,i):
        return self.scale(self.add(self.var(i,1),self.var(i,2)),F(1,2))

    def trace(self,p):
        # Literally form each multiplication column and read its diagonal.
        return sum(self.mul(p,{e:F(1)}).get(e,F(0)) for e in self.basis)

    def value(self,p,point):
        return sum(c*product_number(z**e for z,e in zip(point,es)) for es,c in p.items())


def product_number(items):
    ans=1
    for i in items: ans*=i
    return ans


def clause_poly(algebra,clause):
    false=[]
    for i,sign in clause:
        literal=algebra.beta(i)
        if sign==-1: literal=algebra.add(algebra.one,algebra.scale(literal,-1))
        false.append(algebra.add(algebra.one,algebra.scale(literal,-1)))
    return algebra.add(algebra.one,algebra.scale(algebra.prod(false),-1))


def true_literal(bits,lit):
    i,sign=lit
    return bits[i] if sign==1 else 1-bits[i]


def true_formula(bits,clauses):
    return all(any(true_literal(bits,lit) for lit in clause) for clause in clauses)


def trace_checks():
    cases=[]
    for n in (1,2):
        algebra=Fibre(n)
        corner=algebra.prod(algebra.var(i,2) for i in range(n))
        literals=list(product(range(n),(-1,1)))
        clauses=list(product(literals,repeat=3))
        polys=[clause_poly(algebra,c) for c in clauses]
        assignments=list(product((0,1),repeat=n))
        truth=[[true_formula(bits,[c]) for bits in assignments] for c in clauses]
        # Exhaustive ordered two-clause formulas, including repeated variables,
        # repeated clauses, opposite signs, tautologies and contradictions.
        counts=Counter()
        for i,j in product(range(len(clauses)),repeat=2):
            u=algebra.prod([corner,polys[i],polys[j]])
            expected=sum(a and b for a,b in zip(truth[i],truth[j]))
            tr=algebra.trace(u)
            check("exhaustive shared two-clause trace",tr==expected,(n,i,j))
            check("exhaustive shared projection",algebra.mul(u,u)==u,(n,i,j))
            counts[expected]+=1
            if i==j or (i*len(clauses)+j)%43==0:
                for point in product((-1,0,1),repeat=n):
                    wanted=0 if 0 in point else int(true_formula(tuple((x+1)//2 for x in point),[clauses[i],clauses[j]]))
                    check("full boundary and Boolean eigenvalues",algebra.value(u,point)==wanted)
        cases.append({"n":n,"ordered_two_clause_cases":len(clauses)**2,"count_histogram":dict(sorted(counts.items()))})
    # Shared clauses on three variables: their joint count is 6, whereas
    # replacing shared occurrences by independent witnesses counts differently.
    algebra=Fibre(3)
    clauses=[((0,1),(1,1),(2,1)),((0,-1),(1,1),(2,-1))]
    u=algebra.prod([*(algebra.var(i,2) for i in range(3)),*(clause_poly(algebra,c) for c in clauses)])
    expected=sum(true_formula(bits,clauses) for bits in product((0,1),repeat=3))
    check("three-variable genuinely coupled trace",algebra.trace(u)==expected==6)
    check("three-variable projection",algebra.mul(u,u)==u)
    EVIDENCE["exhaustive_clause_cases"]=cases
    # Independent all-parameter polynomial identities: multiplication matrices
    # use monomial coordinates; the comparison uses Boolean evaluation.
    X=sp.Matrix([[0,0,0],[1,0,1],[0,1,0]])
    for n,m in ((1,2),(2,1)):
        dim=3**n; I=sp.eye(dim)
        xs=[]
        for i in range(n):
            mats=[X if h==i else sp.eye(3) for h in range(n)]
            mat=mats[0]
            for a in mats[1:]:mat=sp.kronecker_product(mat,a)
            xs.append(mat)
        betas=[(x*x+x)/2 for x in xs]
        es=I
        for x in xs:es=es*x*x
        params=sp.symbols(f"E0:{6*n*m}")
        mat=I; scalar_values=[]
        for j in range(m):
            false=I
            for k in range(3):
                lit=sp.zeros(dim)
                for i in range(n):
                    offset=((j*3+k)*n+i)*2
                    lit+=params[offset]*betas[i]+params[offset+1]*(I-betas[i])
                false=false*(I-lit)
            mat=mat*(I-false)
        for bits in product((0,1),repeat=n):
            val=1
            for j in range(m):
                false=1
                for k in range(3):
                    lit=sum(params[((j*3+k)*n+i)*2]*bits[i]+params[((j*3+k)*n+i)*2+1]*(1-bits[i]) for i in range(n))
                    false*=1-lit
                val*=1-false
            scalar_values.append(val)
        difference=sp.expand(sp.trace(es*mat)-sum(scalar_values))
        check("all-parameter symbolic counting trace",difference==0,(n,m))
    EVIDENCE["symbolic_trace_cases"]=[[1,2],[2,1]]


# Arithmetic formulas deliberately retain all leaves, including repeated
# witnesses and constants, before any evaluation or matrix construction.
def leaf(x):return ("leaf",x)
def plus(*nodes):
    ans=nodes[0]
    for node in nodes[1:]:ans=("add",ans,node)
    return ans
def times(*nodes):
    ans=nodes[0]
    for node in nodes[1:]:ans=("mul",ans,node)
    return ans


def formula(n,m):
    v=lambda name:leaf(name)
    z=lambda num:leaf(F(num))
    terms=[]
    for i in range(n):
        a,b,c,r,B=[v(f"{s}{i}") for s in ("a","b","c","r","B")]
        P=plus(times(c,r,r,r),times(z(-2),r,r),times(b,r),times(z(-2),a))
        terms.extend([times(v(f"t{i}"),P),times(v(f"lambda{i}"),plus(a,z(F(1,4)))),times(v(f"mu{i}"),b),times(v(f"nu{i}"),c),times(v(f"rho{i}"),plus(times(B,B),times(z(-1),B))),times(v(f"tau{i}"),plus(times(z(2),r),times(z(2),B),z(-1)))])
    for j in range(m):
        negatives=[]
        for k in range(3):
            lits=[]
            for i in range(n):
                B=v(f"B{i}")
                lits.append(times(v(f"E{j}_{k}_{i}_p"),B))
                lits.append(times(v(f"E{j}_{k}_{i}_m"),plus(z(1),times(z(-1),B))))
            negatives.append(plus(z(1),times(z(-1),plus(*lits))))
        terms.append(times(v(f"s{j}"),*negatives))
    return plus(*terms)


def stats(node):
    if node[0]=="leaf":return (1,0,0 if isinstance(node[1],F) else 1)
    a=stats(node[1]);b=stats(node[2])
    return (a[0]+b[0],a[1]+b[1]+(node[0]=="mul"),max(a[2],b[2]) if node[0]=="add" else a[2]+b[2])


def evaluate(node,env):
    if node[0]=="leaf":return node[1] if isinstance(node[1],F) else env[node[1]]
    a=evaluate(node[1],env);b=evaluate(node[2],env)
    return a+b if node[0]=="add" else a*b


def all_leaves(node):
    if node[0]=="leaf":return [node[1]]
    return all_leaves(node[1])+all_leaves(node[2])


def direct_constraints(n,m,env):
    output={}
    for i in range(n):
        a,b,c,r,B=[env[f"{s}{i}"] for s in ("a","b","c","r","B")]
        vals=[c*r**3-2*r**2+b*r-2*a,a+F(1,4),b,c,B**2-B,2*r+2*B-1]
        for s,value in zip(("t","lambda","mu","nu","rho","tau"),vals):output[f"{s}{i}"]=value
    for j in range(m):
        val=1
        for k in range(3):
            L=sum(env[f"E{j}_{k}_{i}_p"]*env[f"B{i}"]+env[f"E{j}_{k}_{i}_m"]*(1-env[f"B{i}"]) for i in range(n))
            val*=1-L
        output[f"s{j}"]=val
    return output


def graph(node):
    nextv=2;edges=[]
    def fresh():
        nonlocal nextv
        v=nextv;nextv+=1;return v
    def emit(expr,s,t):
        if expr[0]=="leaf":
            middle=fresh();edges.extend([(s,middle,expr[1]),(middle,t,F(1))])
        elif expr[0]=="add":
            emit(expr[1],s,t);emit(expr[2],s,t)
        else:
            middle=fresh();emit(expr[1],s,middle);emit(expr[2],middle,t)
    emit(node,0,1)
    incoming=[0]*nextv;adj=defaultdict(list)
    for a,b,z in edges:incoming[b]+=1;adj[a].append(b)
    todo=[i for i,x in enumerate(incoming) if x==0];ordered=[]
    while todo:
        v=todo.pop();ordered.append(v)
        for w in adj[v]:
            incoming[w]-=1
            if incoming[w]==0:todo.append(w)
    check("acyclic formula graph",len(ordered)==nextv)
    index={v:i for i,v in enumerate(ordered)}
    edges=[(index[a],index[b],z) for a,b,z in edges]
    return nextv,edges,index[0],index[1]


def bordered_matrix(vertices,edges,source,sink,env,Z=F(1)):
    size=vertices+1
    mat=[[F(0) for _ in range(size)] for _ in range(size)]
    for i in range(vertices):mat[i][i]=Z
    for a,b,z in edges:
        mat[a][b]-=z*Z if isinstance(z,F) else env[z]
    mat[sink][vertices]=Z
    mat[vertices][source]=-Z
    return mat


def exact_determinant(rows):
    """Generic rational Gaussian elimination, no path or Schur formula."""
    mat=[list(row) for row in rows];sign=1;det=F(1);n=len(mat)
    for col in range(n):
        pivot=next((r for r in range(col,n) if mat[r][col]),None)
        if pivot is None:return F(0)
        if pivot!=col:mat[col],mat[pivot]=mat[pivot],mat[col];sign=-sign
        d=mat[col][col];det*=d
        nonzero=[j for j in range(col+1,n) if mat[col][j]]
        for row in range(col+1,n):
            if not mat[row][col]:continue
            scale=mat[row][col]/d;mat[row][col]=F(0)
            for j in nonzero:mat[row][j]-=scale*mat[col][j]
    return sign*det


def determinant_checks():
    cases=[]
    for n,m in ((1,1),(1,2),(2,1),(2,2),(3,2),(2,3)):
        node=formula(n,m);ell,M,degree=stats(node)
        check("formula exact leaf count",ell==30*n+(18*n+7)*m,(n,m,ell))
        check("formula exact multiplication count",M==17*n+(9*n+6)*m,(n,m,M))
        check("formula syntactic degree bound",degree==7)
        leaves=all_leaves(node);variables=sorted(set(x for x in leaves if isinstance(x,str)))
        # Retain a specific highest-degree coefficient rather than infer
        # polynomial degree from the formula's syntactic upper bound.
        sel,E1,E2,E3,B0=sp.symbols("sel E1 E2 E3 B0")
        witness={name:F(0) for name in variables}
        witness.update({"s0":sel,"E0_0_0_p":E1,"E0_1_0_p":E2,"E0_2_0_p":E3,"B0":B0})
        witness_poly=sp.Poly(sp.expand(evaluate(node,witness)),sel,E1,E2,E3,B0)
        check("retained degree-seven coefficient",witness_poly.coeff_monomial(sel*E1*E2*E3*B0**3)==-1)
        check("independent variable count",len(variables)==11*n+6*m*n+m)
        v,edges,s,t=graph(node);d=v+1
        check("graph vertex count",v==2+ell+M)
        check("exact determinant dimension",d==3+47*n+(27*n+13)*m)
        check("graph edge count",len(edges)==2*ell)
        check("graph no merged leaf edges",len({(a,b) for a,b,z in edges})==len(edges))
        check("graph strict triangularity",all(a<b for a,b,z in edges))
        check("determinant size bound",d<=2*ell+2)
        check("strict ambient coordinate kernel",len(variables)+1<d*d)
        check("matrix constant set",set([-z for a,b,z in edges if isinstance(z,F)])|{F(0),F(1),F(-1)} <= {F(0),F(1),F(-1),F(2),F(-2),F(1,4),F(-1,4)})
        check("matrix negative quarter retained",F(-1,4) in [-z for a,b,z in edges if isinstance(z,F)])
        # Each original variable has its own entry, independently verifying
        # the linear coordinate map's right inverse/rank, including Z.
        entries={}
        for a,b,z in edges:
            if isinstance(z,str):entries.setdefault(z,(a,b))
        check("linear coordinate map generator recovery",set(entries)==set(variables))
        check("linear coordinate map entry independence",len(set(entries.values()))==len(variables))
        rank_check=sp.zeros(len(variables)+1)
        for i in range(len(variables)):rank_check[i,i]=-1
        rank_check[-1,-1]=1
        check("linear coordinate map rank",rank_check.det()==(-1)**len(variables))
        for seed,Z in ((3,F(1)),(7,F(2)),(13,F(-1))):
            env={z:F(((i+2)*(seed+1))%17-8, 1+(i+seed)%3) for i,z in enumerate(variables)}
            direct=direct_constraints(n,m,env)
            expected=sum(env[s]*f for s,f in direct.items())
            check("formula retains original constraints",evaluate(node,env)==expected)
            for selector,value in direct.items():
                chosen={**env,**{s:F(s==selector) for s in direct}}
                check("reversible selector coefficient map",evaluate(node,chosen)==value,(n,m,selector))
            actual=exact_determinant(bordered_matrix(v,edges,s,t,env,Z))
            want=Z**d*evaluate(node,{key:value/Z for key,value in env.items()})
            check("independent rational determinant elimination",actual==want,(n,m,seed,str(Z)))
            check("evaluated matrix rational entry types",all(isinstance(a,F) for row in bordered_matrix(v,edges,s,t,env,Z) for a in row))
        env={z:F(1) for z in variables}
        check("homogeneous added zero component",exact_determinant(bordered_matrix(v,edges,s,t,env,F(0)))==0)
        cases.append({"n":n,"m":m,"leaves":ell,"multiplication_nodes":M,"matrix_size":d,"affine_variables":len(variables),"rational_determinant_samples":3})
    EVIDENCE["formula_determinant_cases"]=cases


def encoding_checks():
    encode=lambda n,m:(n+m-2)*(n+m-1)//2+n
    def decode(t):
        total=2
        while t>total*(total-1)//2:total+=1
        n=t-(total-2)*(total-1)//2
        return n,total-n
    for n,m in product(range(1,31),repeat=2):
        t=encode(n,m)
        check("one-index pair encoding",decode(t)==(n,m))
        check("one-index polynomial bounds",n<=t and m<=t)
    for t in range(1,2001):check("one-index surjectivity",encode(*decode(t))==t)
    # Literal integer-circuit evaluation with oversized signed intermediate
    # integers, then reduction gate by gate, including subtraction.
    for n in range(1,10):
        modulus=2**(n+1)
        for count in range(2**n+1):
            huge=2**(8*n+31)+19
            nodes=[("const",huge),("const",-huge),("mul",0,0),("mul",1,1),("sub",2,3),("const",count),("add",4,5)]
            exact=[];modular=[]
            for op,*args in nodes:
                if op=="const":value=args[0];residue=value%modulus
                else:
                    a,b=args
                    if op=="mul":value=exact[a]*exact[b];residue=modular[a]*modular[b]
                    elif op=="sub":value=exact[a]-exact[b];residue=modular[a]-modular[b]
                    else:value=exact[a]+exact[b];residue=modular[a]+modular[b]
                    residue%=modulus
                exact.append(value);modular.append(residue)
                check("integer gate modular homomorphism",value%modulus==residue)
            check("exact count modular recovery",modular[-1]==exact[-1]==count)
    EVIDENCE["encoding_scope"]={"pair_roundtrips":900,"first_indices":2000,"modular_witness_sizes":list(range(1,10)),"modulus":"2^(n+1)","counts":"every integer 0 <= count <= 2^n"}


def main():
    start=time.monotonic()
    source_checks();trace_checks();determinant_checks();encoding_checks()
    receipt={"status":"passed","check_count":sum(COUNTS.values()),"groups":dict(COUNTS),"evidence":EVIDENCE,"scope":"Exact symbolic polynomial identities and explicitly bounded exhaustive/sampled cases. General theorems are proved in shared_verifier.tex. The trace algebra remains dimension 3^n; no polynomial-size counting circuit or separation is certified.","dependencies":{"python":platform.python_version(),"sympy":sp.__version__},"inputs_sha256":{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in ("check_shared_verifier.py","shared_verifier.tex")},"elapsed_seconds":round(time.monotonic()-start,3)}
    (ROOT/"check_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"passed","checks":receipt["check_count"],"elapsed_seconds":receipt["elapsed_seconds"],"receipt":"check_receipt.json"}))


if __name__=="__main__":main()
