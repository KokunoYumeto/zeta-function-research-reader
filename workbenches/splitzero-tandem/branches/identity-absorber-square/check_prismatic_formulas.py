"""Exact finite checks of the polynomial identities; general proofs are in the paper."""
from pathlib import Path
import json
from math import comb
import sympy as s

out=Path(__file__).resolve().parent
x,y=s.symbols("x y")
records=[]
for p in (2,3,5,7):
    correction=s.Poly((x**p+y**p-(x+y)**p)/p,x,y)
    assert all(c.q==1 for c in correction.coeffs())
    obstruction=s.Poly((x**p-p-(x-p)**p)/p,x)
    assert all(c.q==1 for c in obstruction.coeffs())
    quotient,remainder=s.div(obstruction,s.Poly(x-p,x))
    assert remainder.as_expr()==p**(p-1)-1
    assert int(remainder.as_expr())%p==p-1
    for ell in (2,3,5,7,11):
        image=x**p+ell-ell**p
        assert image.subs(x,ell)==ell
        assert (ell-ell**p)%p==0
    sample_count=0
    for a in range(-4,5):
        for b in range(-4,5):
            carry=(a**p+b**p-(a+b)**p)//p
            assert (a+b)**p+p*carry==a**p+b**p
            sample_count+=1
    records.append({"p":p,"addition_correction_integral":True,
                    "single_relation_delta_obstruction":str(remainder.as_expr()),
                    "corrected_prime_lifts_checked":[2,3,5,7,11],
                    "length_two_witt_addition_samples":sample_count})

def ghosts(coords,p):
    return [sum(p**i*coords[i]**(p**(n-i)) for i in range(n+1)) for n in range(len(coords))]
def from_ghost(g,p):
    coords=[]
    for n,gn in enumerate(g):
        v=gn-sum(p**i*coords[i]**(p**(n-i)) for i in range(n))
        assert v%(p**n)==0
        coords.append(v//(p**n))
    return coords
for p in (2,3,5):
    a=ghosts([2,-1,3,1],p); b=ghosts([-3,2,1,-1],p)
    for g in ([x+y for x,y in zip(a,b)],[x*y for x,y in zip(a,b)]):
        c=from_ghost(g,p)
        assert ghosts(c,p)==g
        assert all((g[n]-g[n-1])%(p**n)==0 for n in range(1,len(g)))
    delta=[(a[n+1]-a[n]**p)//p for n in range(len(a)-1)]
    assert all((delta[n]-delta[n-1])%(p**n)==0 for n in range(1,len(delta)))
assert from_ghost([2,2,2],2)==[2,-1,-4]

# Detect the need to prove cross-prime commutation separately: these selected
# arithmetic-compatible lifts do not commute on the prime-2 variable.
f2=x*x-2
f3=x*x*x-6
commutator=s.expand(f3.subs(x,f2)-f2.subs(x,f3))
assert commutator== -6*x**4+12*x**3+12*x**2-48
for ell in (2,3,5):
    for p,q in ((2,3),(2,5),(3,5)):
        fp=(x-ell)**p+ell
        fq=(x-ell)**q+ell
        assert s.expand(fq.subs(x,fp)-fp.subs(x,fq))==0
        assert fp.subs(x,ell)==ell

report={"scope":"Exact polynomial checks at stated primes and finite integer samples; not substitutes for the general proofs.",
        "prime_checks":records,"witt_ghost_roundtrips":"passed",
        "p2_sum_of_two_teichmuller_ones_first_three_coordinates":[2,-1,-4],
        "selected_lifts_cross_prime_commutator":str(commutator),
        "translated_lifts_cross_prime_commutation":"passed for ell=2,3,5 and pairs (2,3),(2,5),(3,5)",
        "all_passed":True}
(out/"PRISMATIC_CHECKS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2))
