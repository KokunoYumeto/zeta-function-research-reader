"""Exact finite algebra fixtures for MR1--23; not arithmetic moment values."""
import argparse
import itertools as it
import json
from pathlib import Path
import sympy as s

BASE = Path(__file__).resolve().parent
checks = []
def equal(name, a, b):
    diff = a-b
    entries = list(diff) if isinstance(diff, s.MatrixBase) else [diff]
    if any(s.cancel(s.expand_complex(x)) != 0 for x in entries):
        raise ArithmeticError(name)
    checks.append(name)

def det(a):
    return s.cancel(a.det(method='domain-ge'))

x = s.Symbol('x')
def boundary(roots1, roots2, n, nodes, weights):
    if n == 0:
        return s.Integer(1)
    p = s.prod(x-r for r in roots1)
    q = s.prod(x-r for r in roots2)
    pv = [s.expand(p).subs(x,z) for z in nodes]
    qv = [s.expand(q).subs(x,z) for z in nodes]
    # Literal linear-first orientation of MR14, not the opposite cross Gram.
    return det(s.Matrix(n,n,lambda i,j:sum(
        w*z**i*a*s.conjugate(z**j*b)
        for z,w,a,b in zip(nodes,weights,pv,qv))))

def fixture(q, m, d, mass, control=None, integral=False):
    r=q-m
    nodes=[s.Rational(3,2)+s.I*j for j in range(-4,5)]
    weights=[mass*s.Rational(j+2,j+3) for j in range(len(nodes))]
    roots=[s.Rational(j+1,3)+s.I*s.Rational(j*j+2,5) for j in range(q)]
    H=s.Matrix(d,d,lambda i,j:sum(w*s.conjugate(z)**i*z**j for z,w in zip(nodes,weights)))
    E=s.Matrix(q,d,lambda i,j:roots[i]**j)
    C=(E*H.inv()*E.conjugate().T).applyfunc(s.cancel)
    # A nonreal, full-rank invariant image and its exact ordinary annihilator.
    B=s.Matrix(m,r,lambda i,j:s.Rational(i+j+1,3)+s.I*s.Rational(2*i-j+1,4))
    Z=s.eye(r).col_join(B)
    pi=(-B).row_join(s.eye(m))
    U=pi.T
    equal('pi Z',pi*Z,s.zeros(m,r))
    HK=(U.conjugate().T*C.inv()*U).applyfunc(s.cancel)
    reduced=(Z.T*C*Z.conjugate()).applyfunc(s.cancel)
    g=det(U.conjugate().T*U)/det(Z.T*Z.conjugate())
    if control == 'adjoint':
        U=pi.conjugate().T
        bad=(U.conjugate().T*C.inv()*U).applyfunc(s.cancel)
        equal('negative adjoint instead of ordinary dual',det(bad),det(HK))
    equal('complementary determinant',det(HK),g*det(reduced)/det(C))
    border=C.row_join(pi.T).col_join(pi.conjugate().row_join(s.zeros(m)))
    equal('bordered sign',det(border),(-1)**m*det(C)*det(HK))
    D=det(H)
    V=s.prod(roots[j]-roots[i] for i in range(q) for j in range(i+1,q))
    fullB=boundary(roots,roots,d-q,nodes,weights)
    equal('full AV determinant',det(C),V*s.conjugate(V)*fullB/D)
    subsets=list(it.combinations(range(q),r))
    coeff={I:det(Z.extract(I,range(r)))*s.prod(roots[j]-roots[i] for i,j in it.combinations(I,2)) for I in subsets}
    numerator=0
    diagonal=0
    t=d-r
    for I,J in it.product(subsets,repeat=2):
        ri=[roots[i] for i in I]; rj=[roots[j] for j in J]
        b=boundary(ri,rj,t,nodes,weights)
        VI=s.prod(roots[j]-roots[i] for i,j in it.combinations(I,2))
        VJ=s.prod(roots[j]-roots[i] for i,j in it.combinations(J,2))
        equal('mixed AV minor',det(C.extract(I,J)),VI*s.conjugate(VJ)*b/D)
        term=coeff[I]*s.conjugate(coeff[J])*b
        numerator += term
        if I==J:
            diagonal += term
    numerator=s.cancel(s.expand_complex(numerator))
    equal('entire mixed sum',numerator,D*det(reduced))
    equal('original kernel mixed ratio',det(HK),g*numerator/(V*s.conjugate(V)*fullB))
    if control == 'diagonal':
        equal('negative discarded off diagonal',s.cancel(diagonal),numerator)
    if control == 'degree':
        bad=sum(coeff[I]*s.conjugate(coeff[J])*boundary([roots[i] for i in I],[roots[j] for j in J],d-q,nodes,weights) for I,J in it.product(subsets,repeat=2))
        equal('negative wrong relation degree',s.cancel(s.expand_complex(bad)),numerator)
    if integral:
        # The full ordered t-tuple integral is exactly t! times its strictly
        # increasing tuples: repeated nodes have zero Vandermonde and the
        # squared integrand is permutation invariant. No probability scaling.
        value=0
        pvals={I:[s.prod(z-roots[i] for i in I) for z in nodes] for I in subsets}
        for ids in it.combinations(range(len(nodes)),t):
            vand=s.prod(nodes[j]-nodes[i] for i,j in it.combinations(ids,2))
            phi=sum(coeff[I]*s.prod(pvals[I][j] for j in ids) for I in subsets)
            value += vand*s.conjugate(vand)*phi*s.conjugate(phi)*s.prod(weights[j] for j in ids)
        equal('positive full integral',s.cancel(s.expand_complex(value)),numerator)
    return det(HK),numerator,fullB,g,s.cancel(V*s.conjugate(V))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--control',choices=['adjoint','diagonal','degree','mass','four-sign'])
    ap.add_argument('--output')
    args=ap.parse_args()
    if args.control in ('adjoint','diagonal','degree'):
        fixture(2,1,3,s.Rational(3,2),args.control)
        raise RuntimeError('negative control failed to fail')
    values=[]
    for q,m,d in [(2,1,2),(2,1,3),(2,1,4),(2,1,5),(3,1,3),(3,2,4)]:
        values.append(fixture(q,m,d,s.Rational(3,2),integral=(q==2 and d==3)))
    a=values[1]
    b=fixture(2,1,3,s.Rational(9,2))
    equal('mass restricted determinant',b[0],3*a[0])
    equal('mass numerator degree',b[1],3**2*a[1])
    equal('mass denominator degree',b[2],3*a[2])
    if args.control=='mass':
        equal('negative discarded mass',b[0],a[0])
    h=[v[0] for v in values[:4]]
    A=[v[1] for v in values[:4]]
    B=[v[2] for v in values[:4]]
    ratio=h[0]*h[1]/(h[2]*h[3])
    rhs=A[0]*A[1]*B[2]*B[3]/(A[2]*A[3]*B[0]*B[1])
    equal('four cutoff frame cancellation',ratio,rhs)
    if args.control=='four-sign':
        equal('negative wrong cutoff sign',ratio,A[0]*A[2]*B[1]*B[3]/(A[1]*A[3]*B[0]*B[2]))
    report={'status':'passed','checks':len(checks),'names':checks,
      'scope':'Exact rational complex finite fixtures; no arithmetic moment evaluation, actual period test or asymptotic coefficient.',
      'python_optimized':not __debug__}
    if args.output:
        Path(args.output).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='names'}))
if __name__=='__main__':
    main()
