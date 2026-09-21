"""Exact integer evaluation of the complete finite Gamma reference factor.

Human source: Christian Krattenthaler, Advanced Determinant Calculus,
arXiv:math/9902004v3, sec:cond, prop:cond, eq:cond.
No original period or hypothetical zero is selected by this calculation.
"""
from pathlib import Path
from math import comb
import argparse, hashlib, json, time
import gmpy2 as g
import sympy as sp

def moments(jmax):
    tangent=[g.mpz(1)]
    for n in range(1,jmax):
        tangent.append(sum((g.mpz(comb(2*n,2*j+1))*tangent[j]*tangent[n-j-1]
                            for j in range(n)),g.mpz(0)))
    mu=[g.mpz(1)]
    for n in range(1,jmax+1):
        mu.append(sum((g.mpz(comb(2*n-1,2*j+1))*tangent[j]*(1<<j)*mu[n-j-1]
                       for j in range(n)),g.mpz(0)))
    return mu

def hankels(mu, wanted):
    """Desnanot--Jacobi with every integer division and positivity checked."""
    ans={key:g.mpz(1) for key in wanted if key[0]==0}
    nmax=max(n for n,a in wanted)
    prev2=[g.mpz(1)]*(len(mu)+2)
    prev=list(mu)
    ans.update({(1,a):prev[a] for n,a in wanted if n==1})
    divisions=0
    for n in range(2,nmax+1):
        row=[]
        for a in range(len(prev)-2):
            numerator=prev[a]*prev[a+2]-prev[a+1]**2
            q,r=divmod(numerator,prev2[a+2])
            if r or q<=0: raise ArithmeticError((n,a,'failed exact positive condensation'))
            row.append(q);divisions+=1
        for size,a in wanted:
            if size==n: ans[n,a]=row[a]
        prev2,prev=prev,row
    return ans,divisions

def delta_keys(n,a):
    N=n+1;r=(N+1)//2;s=N//2
    return ((r,a),(s,a+1))

def delta(n,a,H):
    if n<0:return g.mpq(1)
    x,y=delta_keys(n,a)
    power=(n+1)*a+n*(n+1)//2
    return g.mpq(H[x]*H[y],g.mpz(1)<<power)

def reference(k,v=0):
    q=(k+1)**2;qp=(k-7)**2;gap=q-qp-v
    if k<9 or k%4!=1 or gap<=0 or v<0: raise ValueError('original discrete domain')
    terms=[(gap-1,qp,1),(gap,qp,1),(q-1,q-v,1),(q,q-v,1),
           (q+gap-1,qp,-1),(q+gap,qp,-1),(0,q-v,-1)]
    keys={key for n,a,s in terms for key in delta_keys(n,a)}
    order=max(a+2*(n-1) for n,a in keys if n)
    mu=moments(order);H,divisions=hankels(mu,keys)
    value=g.mpq(1)
    for n,a,sign in terms:
        d=delta(n,a,H);value=value*d if sign==1 else value/d
    with g.context(g.get_context(),precision=256,round=g.RoundDown):
        lower=g.log(g.mpfr(value))/g.mpfr(k*q)
    with g.context(g.get_context(),precision=256,round=g.RoundUp):
        upper=g.log(g.mpfr(value))/g.mpfr(k*q)
    def outward(x,up):
        scaled=g.mpq(x)*10**60
        z,rem=divmod(scaled.numerator,scaled.denominator)
        if up and rem: z+=1
        z=int(z)
        return ('-' if z<0 else '')+str(abs(z)//10**60)+'.'+str(abs(z)%10**60).zfill(60)
    return value,dict(k=k,v=v,q=q,q_prime=qp,g=gap,moment_max_even_order=2*order,
       exact_condensation_divisions=divisions,all_divisions_exact=True,
       numerator_bits=value.numerator.bit_length(),denominator_bits=value.denominator.bit_length(),
       log_reference_over_kq_lower=outward(lower,False),log_reference_over_kq_upper=outward(upper,True),
       interpretation='Scalar reference only; no invariant covariance or canonical kernel coefficient evaluated.')

def small_checks():
    mu=moments(20);details=[]
    assert list(map(int,mu[:5]))==[1,1,7,139,5473]
    details.append('first five integer moments')
    keys={(n,a) for n in range(1,6) for a in range(6)}|{(0,0)}
    H,_=hankels(mu,keys)
    for n,a in sorted(keys):
        direct=sp.Matrix(n,n,lambda i,j:int(mu[a+i+j])).det() if n else 1
        assert int(H[n,a])==int(direct);details.append(f'positive Hankel n={n},a={a}')
    for n in range(8):
        for a in range(4):
            keys2=set(delta_keys(n,a)); hh,_=hankels(mu,keys2)
            direct=sp.Matrix(n+1,n+1,lambda i,j:sp.Rational(int(mu[a+(i+j)//2]),2**(a+(i+j)//2)) if (i+j)%2==0 else 0).det()
            assert sp.Rational(str(delta(n,a,hh)))==direct
            details.append(f'full parity Gram n={n},a={a}')
    return details

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--k',type=int,default=9);ap.add_argument('--v',type=int,default=0)
    args=ap.parse_args();P=Path(__file__).parent;started=time.monotonic()
    checks=small_checks();value,report=reference(args.k,args.v)
    stem=f'REFERENCE_k{args.k}_v{args.v}'
    exact=('{"numerator":"'+str(value.numerator)+'","denominator":"'+str(value.denominator)+'"}\n').encode()
    (P/(stem+'_EXACT.json')).write_bytes(exact)
    report.update(checks=len(checks),check_details=checks,seconds=time.monotonic()-started,
                  exact_file=stem+'_EXACT.json',exact_sha256=hashlib.sha256(exact).hexdigest())
    (P/(stem+'.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:val for key,val in report.items() if key!='check_details'}))
