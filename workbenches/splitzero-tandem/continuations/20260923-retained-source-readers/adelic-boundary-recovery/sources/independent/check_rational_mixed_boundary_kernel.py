"""Exact checks of original rational progressions and their retained support map."""
from pathlib import Path
from itertools import product
import json
import sympy as s

z=s.symbols('z')
R=s.Rational
families=[
 ('single_original',[(1,1,1)]),
 ('half_original',[(R(1,2),1,1)]),
 ('thirds_reflection',[(R(1,3),1,1),(R(2,3),1,1)]),
 ('fifths_reflection_nonprincipal',[(R(1,5),1,1),(R(4,5),1,1)]),
 ('mixed_scale_zero',[(1,2,1),(1,1,-1),(R(1,2),1,-1)]),
 ('mixed_scale_initial_cancel',[(R(3,2),1,1),(R(1,2),1,-1),(1,2,1),(2,2,-1),(1,1,1)]),
 ('supported_duplicate_initial_cancel',[(R(3,2),1,1),(R(3,2),1,-1),(1,1,1)]),
 ('nonintegral_scales',[(R(7,3),R(2,3),R(2,5)),(R(1,2),R(1,2),-3),(R(5,4),1,R(7,2))]),
 ('first_coefficient_conceals_defect',[(R(1,3),R(1,3),1),(1,1,R(1,9)),(2,1,-R(1,9))]),
 ('zero_weight_retained',[(R(5,2),R(3,2),0),(1,1,1)])
]
receipts=[]
for name,raw in families:
    terms=[tuple(map(s.sympify,row)) for row in raw]
    denoms=[x.q for a,r,al in terms for x in [1/r,a/r]]
    D=int(s.ilcm(*denoms)) if len(denoms)>1 else int(denoms[0])
    p=[int(D*a/r) for a,r,al in terms]
    q=[int(D/r) for a,r,al in terms]
    alpha=[al for a,r,al in terms]
    Q=int(s.ilcm(*q)) if len(q)>1 else q[0]
    K=max([0]+[pj-qj for pj,qj in zip(p,q)])
    M=K+(Q-1)//2
    v=lambda k:sum(al for pj,qj,al in zip(p,q,alpha) if (k-pj)%qj==0)
    d=lambda k:-sum(al for pj,qj,al in zip(p,q,alpha) if 1<=k<pj and (k-pj)%qj==0)
    w=lambda k:sum(al for pj,qj,al in zip(p,q,alpha) if k>=pj and (k-pj)%qj==0)
    W=sum(al*z**pj/(1-z**qj) for pj,qj,al in zip(p,q,alpha))
    P=sum(v(r)*z**r for r in range(1,Q+1))
    Delta=sum(d(k)*z**k for k in range(1,K+1))
    assert s.cancel(W-P/(1-z**Q)-Delta)==0
    for k in range(1,K+3*Q+1):
        assert w(k)==v(k)+d(k)
    criterion=all(d(k)==0 for k in range(1,K+1)) and all(v(k)==v(-k) for k in range(Q))
    betas=[]
    # A small early range checks the original/comparison identity in each
    # presentation. The general matrix certificate is separately checked.
    for m in range(1,min(M+2,8)+1):
        beta=sum(al*qj**(2*m)*s.bernoulli(2*m+1,R(pj,qj)) for pj,qj,al in zip(p,q,alpha))
        other=Q**(2*m)*sum(v(r)*s.bernoulli(2*m+1,R(r,Q)) for r in range(1,Q+1))-(2*m+1)*sum(d(k)*k**(2*m) for k in range(1,K+1))
        assert s.cancel(beta-other)==0
        betas.append(beta)
    C=sum(al*(1-2*a) for a,r,al in terms)
    rational_zero=s.cancel(W+W.subs(z,1/z)-C)==0
    assert rational_zero==criterion
    if M<=8:
        assert all(vv==0 for vv in betas[:M])==criterion
    if criterion:
        assert C==-v(0)
        assert sum(al*(a/R(2)-R(1,4)) for a,r,al in terms)==v(0)/4
    assert sum(alpha[j]/q[j] for j in range(len(q)))==sum(v(r) for r in range(Q))/Q
    receipts.append({'name':name,'D':D,'p':p,'q':q,'Q':Q,'K':K,'M':M,
                     'full_boundary_zero':criterion,'initial_beta':[str(t) for t in betas]})

# Original separate labels: structural absence, supported zeros, and
# omitted-initial incidences are all retained. Chain3 and Boolean4.
support_checks=0
for lattice,labels,join,top in [('chain3',range(3),max,2),('boolean4',range(4),lambda a,b:a|b,3)]:
    scalars=[(0,lam) for lam in labels]+[(-1,top),(1,top)]
    p=[3,3,2]; q=[2,2,2]
    def add(items):
        amp=0; label=0
        for a,l in items:
            amp+=a;label=join(label,l)
        return amp,label
    for coeffs in product(scalars,repeat=3):
        for k in range(1,7):
            original=add([c for pj,qj,c in zip(p,q,coeffs) if k>=pj and (k-pj)%qj==0])
            periodic=add([c for pj,qj,c in zip(p,q,coeffs) if (k-pj)%qj==0])
            omitted=add([c for pj,qj,c in zip(p,q,coeffs) if k<pj and (k-pj)%qj==0])
            neg=(-omitted[0],omitted[1])
            left=add([periodic,neg])
            right=add([original,(0,omitted[1])])
            assert left==right
            support_checks+=1

out=Path(__file__).with_suffix('.json')
result={'status':'passed','original_parameter_families':len(receipts),'support_checks':support_checks,
        'scope':'Exact original progression, rational generating-function and support checks supplement RMK proofs.',
        'families':receipts}
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','original_parameter_families':len(receipts),'support_checks':support_checks,'output':str(out)}))
