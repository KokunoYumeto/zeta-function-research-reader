"""Exact product enumeration for the separated sheet; no RH test."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json
import sympy as sp

root=Path(__file__).resolve().parent
limit=Fraction(4)
# The coefficient stored at R is the rational multiplier of log(R).
coeff=defaultdict(Fraction)
tuples=defaultdict(list)
def visit(product,word):
    k=len(word)
    if k:
        c=Fraction((-1)**(k+1),k)
        coeff[product]+=c
        tuples[product].append([list(word),str(c)])
    n=2
    while product*Fraction(n+1,2)<=limit:
        visit(product*Fraction(n+1,2),word+(n,))
        n+=1
visit(Fraction(1),())
assert coeff[Fraction(3,2)]==1
assert coeff[Fraction(9,4)]==Fraction(-1,2)
assert tuples[Fraction(9,4)]==[[[2,2],'-1/2']]
assert Fraction(32,81)<1
r,a,z,lam=sp.symbols('r a z lam')
assert sp.expand((r*r+a).subs({r:z-lam/2,a:-lam**2/4}))==z*z-lam*z
gram=sp.diag(2,-2*a)
change=sp.Matrix([[1,lam/2],[0,1]])
assert sp.simplify(change.T*gram.subs(a,-lam**2/4)*change-sp.Matrix([[2,lam],[lam,lam**2]]))==sp.zeros(2)
def alpha(n):
    f=sp.factorint(n)
    return Fraction((-1)**len(f)*int(sp.prod(p-1 for p in f)),n)
assert alpha(6)==Fraction(1,3)
assert alpha(10)==Fraction(2,5)
assert alpha(30)==Fraction(-4,15)
result={
 'scope':'Exact finite rational products at t=1 up to product 4, and displayed symbolic quadratic coordinate and trace identities. No analytic tails or RH assertion.',
 'negative_atom':{'product':'9/4','coefficient':'-log(3/2)','contributors':tuples[Fraction(9,4)]},
 'atoms':[{'product':str(p),'log_multiplier':str(c)} for p,c in sorted(coeff.items()) if c],
 'first_jet_alpha':{str(n):str(alpha(n)) for n in range(1,17)},
 'quadratic_pullback_and_trace':'exact symbolic identities passed'
}
(root/'NON_EULERIAN_LENGTH_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('Exact length atoms and quadratic pullback checks passed; '+str(len(result['atoms']))+' nonzero atoms retained through product 4.')
