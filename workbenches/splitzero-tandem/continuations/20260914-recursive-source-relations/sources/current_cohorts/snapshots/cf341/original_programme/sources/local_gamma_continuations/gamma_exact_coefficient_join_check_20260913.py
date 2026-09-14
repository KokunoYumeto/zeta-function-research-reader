"""Exact finite regressions for GC.14--GC.59; no analytic/zero certificate.

The original scalar mass remains symbolic. Generating coefficients are checked
against generic moment polynomials; the independent tensor calculation uses
multinomial convolution moments. Mutants perturb one named formula per run.
"""
from __future__ import annotations
import argparse
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as sp

x,z,S,theta=sp.symbols("x z S theta",real=True)
mass=sp.Symbol("c_lambda",positive=True)
mu=sp.symbols("mu0:9",real=True)
records=[]

def check(name,actual,expected,mutant):
    if isinstance(actual,sp.MatrixBase) or isinstance(expected,sp.MatrixBase):
        difference=sp.Matrix(actual)-sp.Matrix(expected)
        passed=all(sp.cancel(sp.expand(t))==0 for t in difference)
    else:
        passed=sp.cancel(sp.expand(actual-expected))==0
    records.append({"name":name,"passed":bool(passed),"mutant":mutant})

@lru_cache(None)
def b(alpha,n):
    if n==0:return sp.Integer(1)
    if n==1:return x
    return sp.expand(x*b(alpha,n-1)-(n-1)*(n+alpha-2)*b(alpha,n-2))

def one_moment(polynomial):
    return sp.expand(sum(c*mu[p[0]] for p,c in sp.Poly(polynomial,x).terms()))

def compositions(n,k):
    if k==1:yield (n,)
    else:
        for j in range(n+1):
            for tail in compositions(n-j,k-1):yield (j,)+tail

@lru_cache(None)
def convolution_moment(k,n):
    return sp.expand(sum(sp.factorial(n)*sp.prod(mu[j]/sp.factorial(j) for j in a)
                         for a in compositions(n,k)))

def direct_sum_moment(polynomial,k):
    return sp.expand(sum(c*convolution_moment(k,p[0])
                         for p,c in sp.Poly(polynomial,x).terms()))

def basis_coefficients(polynomial,alpha):
    residual=sp.Poly(sp.expand(polynomial),x)
    output={}
    while not residual.is_zero:
        n=residual.degree();coefficient=residual.LC()
        output[n]=coefficient
        residual=sp.Poly(sp.expand(residual.as_expr()-coefficient*b(alpha,n)),x)
    return output

def truncated(polynomial,degree):
    return sp.series(polynomial,z,0,degree+1).removeO().expand()

def original_quotient(chi,N):
    q=sp.degree(chi,S)
    J=sp.Matrix(q,N+1,lambda i,j:sp.Poly(sp.rem(S**j,chi,S),S).nth(i))
    B=sp.Matrix(N+1,max(0,N-q+1),lambda i,j:sp.Poly(chi*S**j,S).nth(i))
    return J,B

def run(mutant):
    # Closed analytic generating expression versus recurrence-polynomial moments.
    arctangent=truncated(sp.atan(z),7)
    for alpha in [sp.Rational(1,2),sp.Rational(3,2),sp.Rational(13,2)]:
        composition=truncated(sum(mu[j]*arctangent**j/sp.factorial(j)
                                  for j in range(8)),7)
        prefactor=sum(sp.rf(alpha/2,j)*(-1)**j*z**(2*j)/sp.factorial(j)
                      for j in range(4))
        closed=sp.Poly(truncated(prefactor*composition/mass,7),z)
        for n in range(8):
            name=f"generating-alpha-{alpha}-degree-{n}"
            claimed=one_moment(b(alpha,n))/(mass*sp.factorial(n))
            selected=mutant=="coefficient-factorial" and alpha==sp.Rational(1,2) and n==4
            if selected:claimed*=sp.factorial(n)
            check(name,claimed,closed.nth(n),selected)
        claimed=mu[0]/mass
        selected=mutant=="initial-mass" and alpha==sp.Rational(13,2)
        if selected:claimed=mu[0]
        check(f"literal-mass-alpha-{alpha}",claimed,closed.nth(0),selected)

    # A synthetic exact analytic input M(theta)=c sec(theta)^alpha (1+2 tan(theta)+3 tan(theta)^2).
    # Direct substitution in the owner join recovers the specified polynomial.
    for alpha in [sp.Integer(1),sp.Integer(2)]:
        input_m=mass*sp.cos(theta)**(-alpha)*(1+2*sp.tan(theta)+3*sp.tan(theta)**2)
        input_series=sp.series(input_m,theta,0,7).removeO()
        closed=truncated((1+z*z)**(-alpha/2)*input_series.subs(theta,arctangent)/mass,6)
        check(f"owner-analytic-inverse-alpha-{alpha}",closed,1+2*z+3*z*z,False)

    # Original S coordinates versus direct Hankel moments, retaining all phases.
    for k in [1,3]:
        c=sp.Rational(k,2)
        for n in range(1,5):
            L=sp.Matrix(n,n,lambda a,j:sp.binomial(j,a)*c**(j-a)*sp.I**a if a<=j else 0)
            H=sp.Matrix(n,n,lambda i,j:mu[i+j])
            direct=sp.Matrix(n,n,lambda i,j:one_moment((c-sp.I*x)**i*(c+sp.I*x)**j))
            candidate=L
            selected=mutant=="coordinate-sign" and k==3 and n==3
            if selected:
                candidate=sp.Matrix(n,n,lambda a,j:sp.binomial(j,a)*c**(j-a)*(-sp.I)**a if a<=j else 0)
            check(f"original-S-congruence-k-{k}-n-{n}",candidate.conjugate().T*H*candidate,direct,selected)
            claimed=sp.I**(n*(n-1)//2)
            selected=mutant=="determinant-phase" and k==1 and n==3
            if selected:claimed=-claimed
            check(f"original-S-determinant-k-{k}-n-{n}",L.det(),claimed,selected)

    # Generic original moment tensor power versus the exact finite gamma coefficient map.
    alpha=sp.Rational(3,2)
    onecoeff=[one_moment(b(alpha,j))/(mass*sp.factorial(j)) for j in range(7)]
    for k in [1,2,3]:
        dpoly=sp.Poly(truncated(sum(onecoeff[j]*z**j for j in range(7))**k,6),z)
        c=sp.Rational(k,2)
        for i,j,r in itertools.product(range(3),range(3),range(3)):
            polynomial=x**r*(c-sp.I*x)**i*(c+sp.I*x)**j
            e=basis_coefficients(polynomial,k*alpha)
            selected=mutant=="derivative-degree" and k==2 and i==2 and j==2 and r==2
            cutoff=i+j+r-(1 if selected else 0)
            claimed=mass**k*sum(coefficient*sp.factorial(n)*dpoly.nth(n)
                                for n,coefficient in e.items() if n<=cutoff)
            check(f"finite-Gram-k-{k}-i-{i}-j-{j}-derivative-{r}",
                  claimed,direct_sum_moment(polynomial,k),selected)

    # Cochain signs in the full k-factor relative primitive, on a declared nilpotent algebra fixture.
    for k in range(1,5):
        variables=sp.symbols("s1:"+str(k+1))
        total=sum(variables);chi=total**(k+1)
        remainder=chi;quotients=[]
        for v in variables:
            q,remainder=sp.div(remainder,v**2,v)
            quotients.append(q)
        check(f"ordered-monic-division-k-{k}",remainder,0,False)
        P=total**2+(1+sp.I)*total+3
        boundary=0
        for index,(v,Q) in enumerate(zip(variables,quotients)):
            primitive_sign=-(-1)**index
            selected=mutant=="cochain-sign" and k==3 and index==1
            if selected:primitive_sign=-primitive_sign
            differential_sign=(-1)**index
            boundary+=primitive_sign*differential_sign*v**2*Q*P
        check(f"negative-section-cochain-k-{k}",boundary,-chi*P,
              mutant=="cochain-sign" and k==3)

    # The section correction has independent original complex relation coefficients.
    chi=S**2-(1+sp.I)*S+(2-sp.I)
    for N in [1,2,3]:
        J,B=original_quotient(chi,N)
        T=sp.eye(N+1)
        for j in range(N):T[j,j+1]=sp.Rational(1,3)+sp.I/5
        M=T.conjugate().T*sp.diag(*range(2,N+3))*T
        Mr=sp.diag(*range(3,N+4))
        G=(J*M.inv()*J.conjugate().T).inv()
        Gr=(J*Mr.inv()*J.conjugate().T).inv()
        R=M.inv()*J.conjugate().T*G
        Rr=Mr.inv()*J.conjugate().T*Gr
        K=(B.conjugate().T*M*B).inv()*B.conjugate().T*M*Rr if B.cols else sp.zeros(0,J.rows)
        check(f"exact-section-N-{N}",Rr-B*K,R,False)
        check(f"section-original-quotient-N-{N}",J*R,sp.eye(J.rows),False)
        check(f"source-relation-volume-N-{N}",M.det(),G.det()*(B.conjugate().T*M*B).det(),False)

    # Full theta domains are proved analytically in the TeX, not by finite sampling.
    return records

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--json",type=Path,required=True)
    parser.add_argument("--mutant",choices=["coefficient-factorial","initial-mass",
      "coordinate-sign","determinant-phase","derivative-degree","cochain-sign"])
    args=parser.parse_args()
    result=run(args.mutant)
    failed=[r["name"] for r in result if not r["passed"]]
    record={"status":"passed" if not failed else "failed","checks":len(result),
      "failed_checks":failed,"mutant":args.mutant,"sympy":sp.__version__,
      "scope":"Exact finite coefficient, original-coordinate, derivative, cochain and section identities; no analytic, interval, Lean or zero certificate.",
      "records":result}
    args.json.write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in record.items() if k!="records"},indent=2))
    return 0 if not failed else 1

if __name__=="__main__":raise SystemExit(main())
