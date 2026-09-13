"""Independent-formula fixtures for OW.1--40, with explicit changed formulas."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse
import hashlib
import importlib.util
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('weight_optimizer',ROOT/'au_weight_optimizer_20260913.py')
opt=importlib.util.module_from_spec(spec)
spec.loader.exec_module(opt)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    parser.add_argument('--fault',choices=['minor-sign','factorial','stationarity-sign',
                                           'moment-product','cosh-factor'])
    args=parser.parse_args()
    checks=[]
    failures=[]
    def check(name,truth):
        checks.append(name)
        if not bool(truth):
            failures.append(name)

    u,S=s.symbols('u S')
    for roots in ([(s.I,3),(-s.I,3)],[(1+s.I,2),(-2*s.I,1)]):
        q=sum(order for _,order in roots)
        psi=s.Poly(s.prod((u-z)**order for z,order in roots),u)
        E=s.Matrix([[s.diff(u**j,u,d).subs(u,z) for j in range(q+1)]
                    for z,order in roots for d in range(order)])
        Z=E[:,:q]
        coeff=s.Matrix([psi.nth(j) for j in range(q+1)])
        check(f'q{q}-raw-full-jet-nullvector',all(s.expand(x)==0 for x in E*coeff))
        for j in range(q+1):
            minor=E[:,[l for l in range(q+1) if l!=j]].det()
            sign=(-1)**(q-j+(args.fault=='minor-sign'))
            check(f'q{q}-signed-omitted-minor-{j}',s.expand(minor-sign*psi.nth(j)*Z.det())==0)
        c=s.Rational(3,2)
        chi=s.Poly(s.expand(s.I**q*psi.as_expr().subs(u,(S-c)/s.I)),S)
        for j in range(q+1):
            expected=s.I**(j-q)*s.diff(chi.as_expr(),S,j).subs(S,c)/s.factorial(j)
            check(f'q{q}-original-coefficient-phase-{j}',s.expand(psi.nth(j)-expected)==0)
        b=s.Rational(3,5)
        beta=[b**(2*j)/s.factorial(2*j) for j in range(q+1)]
        proposed=[b**(2*j)/s.factorial(j if args.fault=='factorial' else 2*j)
                  for j in range(q+1)]
        eta=[s.simplify(psi.nth(j)*s.conjugate(psi.nth(j))/proposed[j]) for j in range(q+1)]
        tau=[s.Rational(j+1,(q+1)*(q+2)//2) for j in range(q+1)]
        rawdet=(E*s.diag(*[tau[j]*beta[j] for j in range(q+1)])*E.adjoint()).det()
        Da=sum(eta[j]*s.prod(tau[l] for l in range(q+1) if l!=j) for j in range(q+1))
        factor=Z.det()*s.conjugate(Z.det())*s.prod(proposed)*Da
        check(f'q{q}-factorial-weighted-determinant',s.simplify(rawdet-factor)==0)
        K=Z.inv()*E
        check(f'q{q}-exact-last-remainder-column',
              all(s.simplify(x)==0 for x in K[:,:q]-s.eye(q)) and
              all(s.simplify(x)==0 for x in K[:,q]+coeff[:q,0]))

        # An actual unnormalized auxiliary density du on [-1,1] supplies
        # all mixed moments. It is a finite identity fixture, not zero data.
        moment=lambda degree: s.Rational(2,degree+1) if degree%2==0 else s.Integer(0)
        H=s.Matrix([[moment(i+j) for j in range(q+1)] for i in range(q+1)])
        mu=[moment(2*j) for j in range(q+1)]
        r=[s.Rational(j+2,j+1) for j in range(q+1)]
        sr=sum(r[j]*mu[j] for j in range(q+1))
        t=[r[j]*mu[j]/sr for j in range(q+1)]
        check(f'q{q}-moment-cone-map',sum(t)==1 and all(sr*t[j]/mu[j]==r[j] for j in range(q+1)))
        check(f'q{q}-literal-zero-moment-mass',mu[0]==2)
        gap=sr*s.diag(*[1/x for x in r])-H
        # Sum of integrated two-coordinate Cauchy--Schwarz squares.
        pair_sum=s.zeros(q+1)
        for i in range(q+1):
            for j in range(i+1,q+1):
                pair_sum[i,i]+=r[j]*mu[j]/r[i]
                pair_sum[j,j]+=r[i]*mu[i]/r[j]
                pair_sum[i,j]-=moment(i+j)
                pair_sum[j,i]-=moment(i+j)
                check(f'q{q}-joint-moment-pair-positive-{i}-{j}',
                      mu[i]*mu[j]-moment(i+j)**2>=0)
        check(f'q{q}-full-joint-moment-matrix',gap==pair_sum)
        kappa=[s.simplify(coeff[j]*s.conjugate(coeff[j])*mu[j]) for j in range(q+1)]
        Dk=sum(kappa[j]*s.prod(t[l] for l in range(q+1) if l!=j) for j in range(q+1))
        inverse_product=1/s.prod(mu[1:] if args.fault=='moment-product' else mu)
        matrixdet=(E*s.diag(*r)*E.adjoint()).det()/sr**q
        expected=Z.det()*s.conjugate(Z.det())*inverse_product*Dk
        check(f'q{q}-full-q-plus-one-moment-determinant',s.simplify(matrixdet-expected)==0)
        Sq=sum(beta[j]*mu[j] for j in range(q+1))
        tb=[beta[j]*mu[j]/Sq for j in range(q+1)]
        Dkb=sum(kappa[j]*s.prod(tb[l] for l in range(q+1) if l!=j) for j in range(q+1))
        exact_eta=[s.simplify(coeff[j]*s.conjugate(coeff[j])/beta[j]) for j in range(q+1)]
        check(f'q{q}-finite-cosh-ray-map',
              s.simplify(Dkb-s.prod(mu)*s.prod(beta)*sum(exact_eta)/Sq**q)==0)
        cosh_integral=s.integrate(s.cosh(b*u),(u,-1,1))
        Mk=s.integrate(s.exp(b*u)+s.exp(-b*u),(u,-1,1))
        denominator=1 if args.fault=='cosh-factor' else 2
        check(f'q{q}-two-laplace-cosh-half-factor',
              s.simplify(cosh_integral-Mk/denominator)==0)
        check(f'q{q}-finite-even-tail-next-term-positive',
              b**(2*q+2)*moment(2*q+2)/s.factorial(2*q+2)>0)
        quotient_gram=(K*H.inv()*K.adjoint()).inv()
        psi_norm=s.simplify((coeff.adjoint()*H*coeff)[0])
        check(f'q{q}-full-source-quotient-determinant',
              s.simplify(quotient_gram.det()-H.det()/psi_norm)==0)
        actual_raw=E*H.inv()*E.adjoint()
        new_raw=E*s.diag(*[t[j]/mu[j] for j in range(q+1)])*E.adjoint()
        rawgap=actual_raw-new_raw
        for size in range(1,q+1):
            check(f'q{q}-full-raw-kernel-positive-minor-{size}',
                  s.simplify(rawgap[:size,:size].det())>0)
        kr=[F(int(x.p),int(x.q)) for x in kappa]
        result=opt.optimize(kr,F(1,10**16))
        true_capacity=s.simplify(s.prod(mu)*actual_raw.det()/(Z.det()*s.conjugate(Z.det())))
        check(f'q{q}-optimized-moment-loss-positive',
              true_capacity>s.Rational(result['upper'].numerator,result['upper'].denominator))

    boundary_cases=[([F(0),F(5)],'linear-endpoint'),
                    ([F(3),F(3)],'linear-tie'),
                    ([F(0),F(0),F(0),F(0),F(5)],'boundary'),
                    ([F(1),F(0),F(0),F(0),F(4)],'boundary'),
                    ([F(1),F(0),F(2),F(0),F(3)],'boundary'),
                    ([F(0),F(7),F(0),F(0),F(7)],'two-equal-positive-segment')]
    for number,(a,case) in enumerate(boundary_cases):
        q=len(a)-1
        result=opt.optimize(a,F(1,10**18))
        check(f'boundary-{number}-classification',result['case']==case)
        check(f'boundary-{number}-exact-value',result['lower']==result['upper']==max(a)/q**q)
        check(f'boundary-{number}-polynomial-gradient-certificate',result['h']==0)
        check(f'boundary-{number}-full-simplex',sum(result['weights'])==1 and min(result['weights'])>=0)
        for j,x in enumerate(a):
            if x==0:
                check(f'boundary-{number}-zero-coefficient-{j}',result['weights'][j]==F(1,q))

    # All points of the exceptional maximizing segment retain the same value.
    a=[F(0),F(7),F(0),F(0),F(7)]
    q=4
    for j,z in enumerate([F(0),F(1,20),F(1,8),F(1,4)]):
        tau=[F(1,q),z,F(1,q),F(1,q),F(1,q)-z]
        cert=opt.certificate(a,tau)
        check(f'tied-segment-{j}',cert['h']==0 and cert['lower']==F(7,q**q))

    # Construct exact interior solutions from rational y and c; this supplies
    # expected values independently of the solver and exercises both branches.
    constructed=[
        (3,[0,1,2,3],[F(2,5),F(3,10),F(1,5),F(1,10)],F(1),'all-small'),
        (5,[0,2,4,5],[F(3,5),F(1,5),F(3,20),F(1,20)],F(1),'one-large'),
        (4,[0,2,4],[F(3,5),F(1,4),F(3,20)],F(7),'three-positive-closed-form'),
        (6,[1,3,6],[F(1,3)]*3,F(9),'three-positive-closed-form'),
    ]
    for number,(q,ids,y,c,case) in enumerate(constructed):
        a=[F(0) for _ in range(q+1)]
        tau=[F(1,q) for _ in a]
        for i,yi in zip(ids,y):
            a[i]=c*yi*(1-yi)
            tau[i]=(1-yi)/q
        expected=c*opt.prod(1-yi for yi in y)/q**q
        cert=opt.certificate(a,tau)
        check(f'interior-{number}-known-exact-simplex',sum(tau)==1 and min(tau)>0)
        check(f'interior-{number}-known-exact-value',cert['lower']==cert['upper']==expected)
        check(f'interior-{number}-known-exact-gradient',cert['h']==0)
        D,g=opt.value_gradient(a,tau)
        P=opt.prod(tau)
        St=sum((a[i]/tau[i] for i in range(q+1)),F(0))
        for i in range(q+1):
            sign=1 if args.fault=='stationarity-sign' else -1
            check(f'interior-{number}-full-stationarity-{i}',
                  a[i]==St*tau[i]*(1+sign*q*tau[i]))
        result=opt.optimize(a,F(1,10**18))
        check(f'interior-{number}-solver-branch',result['case']==case)
        check(f'interior-{number}-certified-exact-value',result['lower']<=expected<=result['upper'])
        check(f'interior-{number}-certified-width',result['upper']-result['lower']<=F(1,10**18))
        check(f'interior-{number}-candidate-euler',
              sum(result['weights'][i]*result['gradient'][i] for i in range(q+1))==q*result['value'])
        for i in range(q+1):
            if a[i]==0:
                check(f'interior-{number}-zero-coordinate-retained-{i}',result['weights'][i]==F(1,q))
        # Exact uniform-to-optimum gain ratio, with no numerical logarithms.
        uniform=sum(a)/F((q+1)**q)
        check(f'interior-{number}-gain-ratio-upper',expected/uniform<=F((q+1)**q,q**q))
        check(f'interior-{number}-gain-positive',expected>=uniform)

    for q,a in [(4,[F(1)]*5),(5,[F(2),F(0),F(2),F(0),F(2),F(2)])]:
        result=opt.optimize(a)
        p=sum(x>0 for x in a)
        expected=F((p-1)**(p-1),q**q)*sum(a)/p**(p-1)
        check(f'equal-positive-q{q}-closed-value',result['lower']==result['upper']==expected)
        check(f'equal-positive-q{q}-full-gradient',result['h']==0)

    # An exact branch-transition endpoint: y_max=1/2; no algebraic sign must
    # be guessed to certify the optimizer.
    q=3
    ys=[F(1,2),F(1,4),F(1,8),F(1,8)]
    aa=[y*(1-y) for y in ys]
    expected=opt.prod(1-y for y in ys)/q**q
    result=opt.optimize(aa,F(1,10**18))
    check('branch-transition-certified',result['lower']<=expected<=result['upper'])
    check('branch-transition-width',result['upper']-result['lower']<=F(1,10**18))

    # Gradient upper certificates at points that are deliberately not maxima.
    aa=[F(1),F(2),F(2)]
    optimum=F(4,7)
    for j,tt in enumerate([[F(2,5),F(3,10),F(3,10)],
                           [F(1,2),F(1,4),F(1,4)]]):
        cert=opt.certificate(aa,tt)
        check(f'nonstationary-gradient-certificate-{j}',cert is not None and
              cert['lower']<=optimum<=cert['upper'])

    # Rational square-root brackets are checked by exact squared endpoints.
    for j,x in enumerate([F(0),F(1),F(1,9),F(17,29),F(10**12-1,10**12)]):
        lo,hi=opt.sqrt_bracket(x,64)
        check(f'radical-{j}-squared-certificate',lo*lo<=x<=hi*hi)
        check(f'radical-{j}-width',hi-lo<=F(1,2**64))

    payload={'schema':'au-weight-optimizer-exact-checks-v1',
             'status':'pass' if not failures else 'rejected',
             'check_count':len(checks),'checks':checks,'failures':failures,
             'fault':args.fault,'optimized':not __debug__,
             'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'solver_sha256':hashlib.sha256((ROOT/'au_weight_optimizer_20260913.py').read_bytes()).hexdigest(),
             'scope':'Exact raw-jet cofactors, phases and factorial determinants; complete boundary cases; rationally constructed interior maxima, both scalar branches, exact root-transition equality, zero coordinates, rational polynomial-gradient value certificates; joint-moment source matrices, cone maps and all q+1 moment factors, full low-kernel quotient determinants and two-sided Laplace factor. The explicit auxiliary density du on [-1,1] tests finite identities only. No arithmetic-source asymptotic or zero data are sampled.'}
    Path(args.output).write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':payload['status'],'checks':len(checks),'failures':failures}))
    return 0 if not failures else 1


if __name__=='__main__':
    raise SystemExit(main())
