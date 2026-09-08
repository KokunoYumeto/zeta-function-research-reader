"""Certified finite-periodic BC numerators and Gaussian cooling error bounds."""
from pathlib import Path
import hashlib
import json
from fractions import Fraction
from flint import arb, acb, ctx

ctx.prec=192
ctx.threads=1


def main():
    q,N=256,1024
    points=[("0.25","14"),("0.5","14"),("0.75","40"),("0.25","100")]
    rows=[]
    for real,imag in points:
        s=acb(arb(real),arb(imag))
        partial=acb(1)
        for k in range(1,N+1):
            partial+=(-(s)*arb(q*k+1).log()).exp()-(-s*arb(q*k).log()).exp()
        bound=abs(s)*arb(q)**(-s.real-1)/(s.real*arb(N)**s.real)
        exact=(-s*arb(q).log()).exp()*(s.zeta(acb(arb(1)/q))-s.zeta())
        assert abs(exact-partial) < bound
        global_bound=abs(s)*arb(q)**(-s.real-1)*(s.real+1).zeta()
        assert abs(exact-1) < global_bound and global_bound < 1
        rows.append({"s":[real,imag],"N":N,
                     "Dq_real":str(exact.real),"Dq_imag":str(exact.imag),
                     "partial_real":str(partial.real),"partial_imag":str(partial.imag),
                     "series_tail_bound":str(bound),
                     "distance_to_one_upper":str(global_bound),
                     "numerator_nonzero":True,"independent_series_vs_Hurwitz_check":True})
    # A region certificate with rational constants only.
    # sigma>=1/4, |s|<=101, zeta(5/4)<=5, 256^(5/4)=1024.
    eta=Fraction(505,1024)
    assert eta<1
    a=arb(1)/4
    b2=a.exp()*(1+1/a+(1+1/(2*a)).sqrt())
    eps=arb(1)/16
    R=arb(64)
    sigma=arb(1)/2
    b=arb(3)
    n=1024
    small=b2*eps**(sigma+1)/(4*(sigma+1))
    large=(1+1/(b-1))*(a*b*b).exp()*R**(sigma-b)
    omitted=(a.exp()/(2*eps)
             *((arb(n)*eps).log()-2*a).__truediv__(2*a.sqrt()).erfc())
    middle=omitted*(R**sigma-eps**sigma)/sigma
    result={
        "id":"RH-BC-PERIODIC-20260908-002","status":"pass",
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "q":q,"numerator_definition":"D_q(s)=1+sum_{k>=1}[(q*k+1)^(-s)-(q*k)^(-s)]",
        "points":rows,"whole_region":{"sigma_min":"1/4","modulus_max":"101",
            "distance_to_one_max":str(eta),"absolute_value_lower":str(1-eta),
            "proof":"zeta(1+sigma)<=1+1/sigma; q^(5/4)=1024; all exact",
            "nonvanishing_certified":True},
        "gaussian_mellin_error_example":{"a":"1/4","sigma":"1/2",
            "epsilon":"1/16","R":"64","b":"3","N":n,
            "lower_tail_bound":str(small),"upper_tail_bound":str(large),
            "omitted_middle_summands_bound":str(middle),
            "middle_quadrature_performed":False,
            "scope":"explicit truncation bounds only, not a computed Mellin value"},
        "RH_counterexample_found":False}
    Path(__file__).with_name("bc_periodic_results.json").write_text(
        json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print("BC_PERIODIC_CHECK_OK",str(1-eta),len(rows))


if __name__=="__main__":
    main()
