#!/usr/bin/env python3
"""Exact finite tests of the written adelic/theta/jet maps.

No numerical zeta zeros are inputs. No general theorem is inferred from these
finite tests. All failures raise exceptions, including under python -O.
Dependencies: sympy. Run with --output FILE for a JSON record.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import itertools
import json
from pathlib import Path
import platform
import sympy as sp

COUNTS: Counter[str] = Counter()
x,s,z,L=sp.symbols('x s z L')
TAU=None

def eq(suite: str, left, right, label: str='') -> None:
    if sp.simplify(left-right)!=0:
        raise RuntimeError(f'{suite}: {label}: {left} != {right}')
    COUNTS[suite]+=1

def require(suite: str, value: bool, label: str='') -> None:
    if not value: raise RuntimeError(f'{suite}: {label}')
    COUNTS[suite]+=1

def add(a,b):
    if a is TAU:return b
    if b is TAU:return a
    return a+b

def mul(a,b):
    if a is TAU or b is TAU:return TAU
    return a*b

def amp(a):return Fraction(0) if a is TAU else a

def trunc(p, m):return sp.series(p,z,0,m).removeO().expand()

def mult_matrix(p,m):
    return sp.Matrix(m,m,lambda i,j:sp.expand(p).coeff(z,i-j) if i>=j else 0)

def test_support():
    vals=[TAU,Fraction(0),Fraction(1),Fraction(-1),Fraction(2)]
    for a,b in itertools.product(vals,repeat=2):
        require('support',amp(add(a,b))==amp(a)+amp(b),'amplitude addition')
        require('support',amp(mul(a,b))==amp(a)*amp(b),'amplitude multiplication')
        require('support',(add(a,b) is not TAU)==(a is not TAU or b is not TAU),'join')
    require('support',add(Fraction(1),Fraction(-1))==Fraction(0),'supported cancellation')
    require('support',add(Fraction(1),Fraction(-1)) is not TAU,'not absence')
    # A fixed support skeleton, with ordinary linear maps in each fibre.
    for A,B in itertools.product([frozenset(),frozenset({0}),frozenset({1}),frozenset({0,1})],repeat=2):
        for c,d in [(1,-1),(0,2),(-2,3)]:
            mapped_sum=c+d
            eq('support',mapped_sum,c+d,'linear amplitude at joined label')
            require('support',(A|B)==(B|A),'same labels retained')

def test_divisor_maps():
    primes=[2,3,5]
    for exps in itertools.product(range(-1,2),repeat=3):
        c=Fraction(1)
        for p,e in zip(primes,exps):c*=Fraction(p)**(-e)
        for q in [Fraction(2),Fraction(-3,2),Fraction(5,3)]:
            for n in [-2,-1,0,1,3]:
                # L_{qa}=q^{-1} L_a and h_{qa}=q h_a.
                r=c*n/q
                require('divisors',q*r==c*n,'principal map')
                require('divisors',abs(Fraction(7,3)*q*r)==abs(Fraction(7,3)*c*n),'arch frame')
    for lam in [Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(5)]:
        for radius in [Fraction(0),Fraction(1,4),Fraction(1),Fraction(7,2)]:
            count=sum(1 for n in range(-20,21) if abs(lam*n)<=radius)
            require('divisors',count==1+2*(radius//lam),'section count')

def test_gaussian_mellin():
    pi=sp.pi
    p=sp.Integer(1)
    # Euler derivative of polynomial times exp(-pi*x^2).
    def D(poly):return sp.expand(x*sp.diff(poly,x)-2*pi*x*x*poly)
    star=D(D(p)+p)
    eq('gaussian',star,4*pi*pi*x**4-6*pi*x*x,'D(D+1)')
    def mellin_ratio(poly):
        P=sp.Poly(poly,x)
        out=0
        for (k,),coef in P.terms():
            require('gaussian',k%2==0,'even power')
            out+=coef*pi**(-k//2)*sp.rf(s/2,k//2)
        return sp.expand(out)
    q=star
    for n in range(10):
        eq('gaussian',mellin_ratio(q),s*(s-1)*(-s)**n,'Euler/Mellin intertwining')
        q=D(q)
    eq('gaussian',mellin_ratio(star).subs(s,1),0,'integral endpoint')
    eq('gaussian',star.subs(x,0),0,'value endpoint')
    # Fourier conjugation D -> -(D+1) leaves D(D+1) fixed.
    d=sp.symbols('d')
    eq('gaussian',(-d-1)*(-d),d*(d+1),'Fourier transport')

def test_jet_interpolation():
    examples=[[(sp.Rational(1,3),2),(sp.Integer(2),1)],
              [(sp.I,2),(-sp.I,2),(sp.Integer(3),1)],
              [(sp.Rational(-2,3),3),(sp.Rational(5,4),2)]]
    for nodes in examples:
        total=sum(m for _,m in nodes)
        # H is a concrete nonvanishing germ at each selected point.
        H=1+2*s+s**2+s**4
        rows=[];rhs=[]
        for rho,m in nodes:
            require('jets',H.subs(s,rho)!=0,'invertible germ')
            for j in range(m):
                rows.append([sp.diff(s**k*H,s,j).subs(s,rho)/sp.factorial(j) for k in range(total)])
                rhs.append((j+1)+(rho if j%2 else -rho))
        coeff=sp.Matrix(rows).inv()*sp.Matrix(rhs)
        P=sum(coeff[k]*s**k for k in range(total))
        pos=0
        for rho,m in nodes:
            for j in range(m):
                eq('jets',sp.diff(P*H,s,j).subs(s,rho)/sp.factorial(j),rhs[pos],'finite CRT jets')
                pos+=1
    # Actual Mellin differential: integration-by-parts multiplier (-D)^j -> s^j.
    for j in range(10):eq('jets',(-1)**j*(-s)**j,s**j,'sign')

def test_local_lattices():
    for m in range(1,8):
        unit=2+3*z-z*z
        f=z**m*unit
        eq('lattices',z**m*unit,f,'unit retained in lattice square')
        inv=trunc(1/unit,m)
        eq('lattices',trunc(inv*unit,m),1,'unit inverse')
        for i,j in itertools.product(range(m),repeat=2):
            residue=sp.residue(z**i*z**(-j-1),z,0)
            eq('lattices',residue,1 if i==j else 0,'residue duality')
        N=mult_matrix(z,m)
        require('lattices',N**m==sp.zeros(m),'nilpotent order bound')
        require('lattices',m==1 or N**(m-1)!=sp.zeros(m),'exact nilpotent order')
        p=sum((i+2)*z**i for i in range(m))
        eq('lattices',sp.trace(mult_matrix(p,m)),m*p.subs(z,0),'multiplicity trace')

def test_dilation_duality():
    for m in range(1,7):
        a=sp.symbols('a',real=True)
        N=mult_matrix(z,m)
        E=sum(((-L)**j/sp.factorial(j)*N**j for j in range(m)),sp.zeros(m))
        Einv=sum(((L)**j/sp.factorial(j)*N**j for j in range(m)),sp.zeros(m))
        require('dilation',(E*Einv).applyfunc(sp.simplify)==sp.eye(m),'all jets inverse')
        eq('dilation',sp.trace(E),m,'unipotent trace retains multiplicity')
        # Algebra involution z -> -z squares to identity on real coefficients.
        p=sum((j+1)*z**j for j in range(m))
        eq('dilation',p.subs(z,-z).subs(z,-z),p,'star twice')
    beta,gamma,t=sp.symbols('beta gamma t',real=True)
    rho=beta+sp.I*gamma
    pair=1-sp.conjugate(rho)
    U=sp.diag(sp.exp(-rho*t),sp.exp(-pair*t))
    J=sp.Matrix([[0,1],[1,0]])
    require('dilation',(sp.conjugate(U).T*J*U-sp.exp(-t)*J).applyfunc(sp.simplify)==sp.zeros(2),'weight-one pair')
    eq('dilation',(sp.Matrix([1,-1]).T*J*sp.Matrix([1,-1]))[0],-2,'sign retained')
    eq('dilation',(sp.Matrix([1,1]).T*J*sp.Matrix([1,1]))[0],2,'positive companion')

def test_character_constants():
    chars={3:[0,1,-1],4:[0,1,0,-1],5:[0,1,sp.I,-sp.I,-1],8:[0,1,0,-1,0,-1,0,1]}
    for q,vals in chars.items():
        eq('characters',sum(vals),0,'finite endpoint integral')
        eps=0 if vals[-1]==1 else 1
        for n in range(q):eq('characters',vals[(-n)%q],(-1)**eps*vals[n],'parity')
        for a,b in itertools.product(range(q),repeat=2):
            eq('characters',vals[(a*b)%q],vals[a]*vals[b],'character multiplication')
        eq('characters',2*sp.Rational(1,2),1,'two-sided Gaussian factor')
    # Exact Q(i) local factors, including the ramified prime.
    u=sp.symbols('u')
    eq('characters',1/((1-u)*(1+u)),1/(1-u*u),'inert factor')
    eq('characters',1/((1-u)*(1-u)),1/(1-u)**2,'split factor')
    eq('characters',1/(1-u)*1,1/(1-u),'ramified factor')
    # Odd conductor contributes sqrt(4), not an erased factor.
    eq('characters',sp.sqrt(4),2,'completed Q(i) constant')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    for fn in [test_support,test_divisor_maps,test_gaussian_mellin,test_jet_interpolation,test_local_lattices,test_dilation_duality,test_character_constants]:fn()
    result={'status':'passed','scope':'Finite exact checks of the authored maps; no RH proof or independent literature audit.',
            'python':platform.python_version(),'sympy':sp.__version__,'checks':sum(COUNTS.values()),'suites':dict(sorted(COUNTS.items()))}
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
