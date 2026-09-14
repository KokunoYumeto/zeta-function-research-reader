"""Certified finite maximization of sum a_j prod_{i!=j} tau_i.

All arithmetic is Fraction/integer arithmetic. The scalar roots only propose
candidates; every returned enclosure has the exact polynomial-gradient
certificate OW.22a. No arithmetic density or asymptotic is sampled.
"""
from fractions import Fraction as F
from math import isqrt, prod
import argparse
import json


def value_gradient(a, tau):
    q = len(a)-1
    zeros = [i for i,x in enumerate(tau) if x == 0]
    if not zeros:
        P = prod(tau)
        S = sum((a[i]/tau[i] for i in range(q+1)), F(0))
        D = P*S
        return D, [P*(S/tau[i]-a[i]/tau[i]**2) for i in range(q+1)]
    if len(zeros) == 1:
        j = zeros[0]
        P = prod(tau[i] for i in range(q+1) if i != j)
        D = a[j]*P
        gradient = [D/tau[i] if i != j else
                    P*sum((a[l]/tau[l] for l in range(q+1) if l != j),F(0))
                    for i in range(q+1)]
        return D, gradient
    # Used for arbitrary finite fixture points; candidates have positive D.
    D = sum((a[j]*prod(tau[l] for l in range(q+1) if l != j)
             for j in range(q+1)),F(0))
    gradient = [sum((a[j]*prod(tau[l] for l in range(q+1) if l not in (i,j))
                    for j in range(q+1) if j != i),F(0))
                for i in range(q+1)]
    return D, gradient


def certificate(a, tau):
    if sum(tau) != 1 or min(tau) < 0:
        raise ValueError('Candidate is outside the specified simplex')
    q = len(a)-1
    D,g = value_gradient(a,tau)
    if D <= 0:
        return None
    h = max(g)-q*D
    if h < 0 or sum(tau[i]*g[i] for i in range(q+1)) != q*D:
        raise ArithmeticError('Polynomial gradient failed its Euler identity')
    if h >= D:
        return None
    return {'lower':D,'upper':D*D/(D-h),'value':D,'gradient':g,'h':h,
            'weights':tau}


def sqrt_bracket(x,bits):
    if x < 0:
        raise ValueError('Negative radicand')
    scale = 1 << bits
    n = isqrt((x.numerator*scale*scale)//x.denominator)
    low = F(n,scale)
    if n*n*x.denominator == x.numerator*scale*scale:
        return low,low
    high = F(n+1,scale)
    if not low*low <= x <= high*high:
        raise ArithmeticError('Square-root certificate failed')
    return low,high


def small_roots(a, support, t, bits):
    roots = {}
    for i in support:
        low,high = sqrt_bracket(1-a[i]*t,bits)
        roots[i] = ((1-high)/2,(1-low)/2)
    return roots


def candidate_from_roots(a,roots,large=None):
    q = len(a)-1
    tau = [F(1,q) for _ in a]
    for i,(low,high) in roots.items():
        y = (low+high)/2
        if i == large:
            y = 1-y
        tau[i] = (1-y)/q
    total = sum(tau[i] for i in roots)
    if total <= 0:
        raise ArithmeticError('Nonpositive auxiliary weight sum')
    # Exact positive-index map OW.20 keeps all zero-coefficient weights 1/q.
    budget=F(len(roots)-1,q)
    return [x*budget/total if i in roots else x for i,x in enumerate(tau)]


def optimize(coefficients,tolerance=F(1,10**12),max_rounds=10):
    a = [F(x) for x in coefficients]
    if len(a)<2 or min(a)<0 or max(a)<=0 or tolerance<=0:
        raise ValueError('Require q>=1, nonnegative nonzero coefficients and tolerance>0')
    q = len(a)-1
    support = [i for i,x in enumerate(a) if x>0]
    A,S = max(a),sum(a)
    dominant = [i for i in support if a[i] == A]
    if q == 1:
        tau = [F(1,2),F(1,2)] if a[0]==a[1] else [F(0),F(0)]
        if a[0] != a[1]:
            tau[1-dominant[0]] = F(1)
        result = certificate(a,tau)
        result.update(case='linear-tie' if a[0]==a[1] else 'linear-endpoint',
                      unique=a[0]!=a[1],root_interval=None)
        return result
    if 2*A >= S:
        tau = [F(1,q) for _ in a]
        if len(support)==2 and a[support[0]]==a[support[1]]:
            for i in support:
                tau[i] = F(1,2*q)
            case,unique = 'two-equal-positive-segment',False
        else:
            tau[dominant[0]]=F(0)
            case,unique = 'boundary',True
        result=certificate(a,tau)
        if result is None or result['h']!=0 or result['lower']!=A/F(q**q):
            raise ArithmeticError('Boundary optimizer certificate failed')
        result.update(case=case,unique=unique,root_interval=None)
        return result
    if len(support)==3:
        aa,bb,dd = [a[i] for i in support]
        Delta = 2*aa*bb+2*aa*dd+2*bb*dd-aa*aa-bb*bb-dd*dd
        tau = [F(1,q) for _ in a]
        for i in support:
            tau[i]=2*a[i]*(S-2*a[i])/(q*Delta)
        result=certificate(a,tau)
        if result is None or result['h']!=0:
            raise ArithmeticError('Three-support closed form failed')
        result.update(case='three-positive-closed-form',unique=True,root_interval=None)
        return result
    if all(a[i]==a[support[0]] for i in support):
        p=len(support)
        tau=[F(p-1,q*p) if i in support else F(1,q) for i in range(q+1)]
        result=certificate(a,tau)
        if result is None or result['h']!=0:
            raise ArithmeticError('Equal-support closed form failed')
        result.update(case='equal-positive-closed-form',unique=True,root_interval=None)
        return result

    endpoint=1/A
    for round_index in range(max_rounds):
        bits=16*(2**round_index)
        end_roots=small_roots(a,support,endpoint,bits)
        Flo=sum(v[0] for v in end_roots.values())
        Fhi=sum(v[1] for v in end_roots.values())
        if Flo>=1:
            branch,large='all-small',None
        elif Fhi<1:
            if len(dominant)!=1:
                raise ArithmeticError('A large branch has no unique maximum')
            branch,large='one-large',dominant[0]
        else:
            result=certificate(a,candidate_from_roots(a,end_roots))
            if result is not None and result['upper']-result['lower']<=tolerance:
                result.update(case='endpoint-certified-without-equality-decision',unique=True,
                              root_interval=None,radical_bits=bits)
                return result
            continue
        left,right=F(0),endpoint
        for _ in range(2*bits):
            t=(left+right)/2
            roots=small_roots(a,support,t,bits)
            result=certificate(a,candidate_from_roots(a,roots,large))
            if result is not None and result['upper']-result['lower']<=tolerance:
                result.update(case=branch,unique=True,root_interval=[left,right],
                              radical_bits=bits)
                return result
            if large is None:
                low=sum(v[0] for v in roots.values())-1
                high=sum(v[1] for v in roots.values())-1
                if low>0:
                    right=t
                elif high<0:
                    left=t
                else:
                    break
            else:
                low=sum(roots[i][0] for i in support if i!=large)-roots[large][1]
                high=sum(roots[i][1] for i in support if i!=large)-roots[large][0]
                if low>0:
                    left=t
                elif high<0:
                    right=t
                else:
                    break
    raise RuntimeError('No certificate within the explicit round limit; increase --max-rounds')


def serial(value):
    if isinstance(value,F):
        return str(value)
    if isinstance(value,list):
        return [serial(x) for x in value]
    if isinstance(value,dict):
        return {k:serial(v) for k,v in value.items()}
    return value


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--weights',required=True,help='Comma-separated exact fractions in original order')
    parser.add_argument('--tolerance',default='1/1000000000000')
    parser.add_argument('--max-rounds',type=int,default=10)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    weights=[F(x.strip()) for x in args.weights.split(',')]
    result=optimize(weights,F(args.tolerance),args.max_rounds)
    payload={'schema':'au-weight-optimizer-rational-certificate-v1',
             'coefficients':[str(x) for x in weights],
             'result':serial(result),'proof':'OW.8-22a'}
    from pathlib import Path
    Path(args.output).write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'case':result['case'],'lower':str(result['lower']),
                      'upper':str(result['upper'])}))
