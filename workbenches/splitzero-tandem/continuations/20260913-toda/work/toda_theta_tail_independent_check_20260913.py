"""Targeted independent theta-tail review checks; no new seed-value certificate."""
from __future__ import annotations
from pathlib import Path
import hashlib
import json
import sys

import sympy as sp
from flint import arb, acb, fmpq, ctx


def main():
    checks = []
    def require(value, name):
        if not value:
            raise RuntimeError(name)
        checks.append(name)

    # Derive the weighted geometric series by applying its differential
    # operator, independently of the author's binomial/Stirling evaluation.
    a, rho = sp.symbols('a rho')
    reference = 1 / (1-rho)
    for p in range(7):
        from sympy.functions.combinatorial.numbers import stirling
        candidate = sum(sp.binomial(p,j)*a**(p-j)*stirling(j,b,kind=2)
                        *sp.factorial(b)*rho**b/(1-rho)**(b+1)
                        for j in range(p+1) for b in range(j+1))
        require(sp.cancel(candidate-reference) == 0,
                f'H_{p}: exact differential generating-function identity')
        reference = a*reference + rho*sp.diff(reference,rho)

    # On Re C>0, Gamma(1/2,C)=sqrt(pi)*erfc(sqrt(C));
    # integration by parts gives Gamma(a+1,C)=a Gamma(a,C)+C^a exp(-C).
    # This checks the incomplete-gamma argument order and branch against
    # a different special-function evaluation, at all half orders used.
    ctx.prec = 128
    ctx.threads = 1
    theta = arb(fmpq(1,10))
    samples = [(1,1,arb(0)), (1,2,theta), (2,1,theta)]
    sample_records=[]
    for m,n,t in samples:
        C=arb.pi()*(m*m*acb(0,t).exp()+n*n*acb(0,-t).exp())
        require(C.real>0, f'C right half-plane m={m},n={n}')
        current = acb(arb.pi().sqrt())*C.sqrt().erfc()
        alpha=arb(fmpq(1,2))
        for order_step in range(7):
            if order_step >= 2:
                direct=C.gamma_upper(alpha)
                require(direct.overlaps(current),
                        f'half-gamma erfc recurrence m={m},n={n},step={order_step}')
            current=alpha*current+C**alpha*(-C).exp()
            alpha+=1
        sample_records.append({'m':m,'n':n,'theta':t.str(30,more=True)})
    C=acb(arb.pi()*5)
    alpha=acb(arb(fmpq(5,2)))
    require(not C.gamma_upper(alpha).overlaps(alpha.gamma_upper(C)),
            'swapped incomplete-gamma arguments rejected by disjoint balls')

    # Exercise directed endpoint and radius semantics with an exact dyadic.
    epsilon=arb(fmpq(1,2**120))
    inflation=arb(0,epsilon.upper())
    require(inflation.contains(epsilon) and inflation.contains(-epsilon),
            'radius constructor includes both exact dyadic error endpoints')
    payload={'schema':'theta-tail-independent-targeted-check-v1',
             'status':'passed','optimization_flag':sys.flags.optimize,
             'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'checks':checks,'count':len(checks),'samples':sample_records,
             'scope':'Exact generating-function identities, independent half-gamma branch/argument checks, and directed radius semantics. Ball overlap checks are diagnostic checks, not proofs of an exact identity or standalone infinite-value certificates.'}
    output=Path(__file__).with_name('toda_theta_tail_independent_check_result_20260913.json')
    output.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'output':str(output)}))


if __name__=='__main__':
    main()
