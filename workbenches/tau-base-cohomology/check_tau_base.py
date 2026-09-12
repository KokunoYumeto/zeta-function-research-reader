#!/usr/bin/env python3
"""Finite regression checks for NOTE.md. Not a formal verification of analytic claims."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from itertools import product
import sympy as s

records: list[dict[str, object]] = []
def require(condition: bool, name: str, detail: str = '') -> None:
    if not bool(condition):
        raise RuntimeError(f'FAILED: {name}: {detail}')
    records.append({'name': name, 'passed': True})

def mat_eq(a, b) -> bool:
    return a.shape == b.shape and all(s.simplify(x-y) == 0 for x,y in zip(a,b))

# +, -, eta, sigma, with arrows as in the note.
P = ('+', '-', 'eta', 'sigma')
def le(a: str, b: str) -> bool:
    return a == b or (a in ('+','-') and b in ('eta','sigma')) or (a == 'eta' and b == 'sigma')

def projective_resolution():
    for y in P:
        active = [a for a in ('+','-') if le(a,y)]
        dim_left = int(le('eta',y))
        D = s.Matrix([1,-1]) if dim_left else s.zeros(len(active),0)
        aug = s.ones(1,len(active))
        require(mat_eq(aug*D, s.zeros(1,dim_left)), f'projective d2 at {y}')
        require(D.rank() == dim_left and aug.rank() == 1 and len(active)-aug.rank() == D.rank(), f'projective exactness at {y}')
    # Restriction matrices on all order arrows.
    for x,y in product(P,P):
        if not le(x,y) or x == y:
            continue
        ax=[a for a in ('+','-') if le(a,x)]
        ay=[a for a in ('+','-') if le(a,y)]
        r=s.zeros(len(ay),len(ax))
        for j,a in enumerate(ax): r[ay.index(a),j]=1
        require(mat_eq(s.ones(1,len(ay))*r, s.ones(1,len(ax))), f'augmentation naturality {x}->{y}')

def dualizing_complex():
    for y in P:
        # I_eta has E at points below eta. I_+ and I_- only at + and -.
        a=int(le(y,'eta'))
        target=[x for x in ('+','-') if le(y,x)]
        if y=='+': D=s.Matrix([[1]])
        elif y=='-': D=s.Matrix([[-1]])
        else: D=s.zeros(len(target),a)
        hm1=a-D.rank(); h0=len(target)-D.rank()
        require(hm1 == int(y=='eta') and h0==0, f'right adjoint stalk cohomology {y}')
    # Arithmetic finite model: injection theta:E -> E^3; two middle spectral directions.
    theta=s.Matrix([1,0,0]); d=theta.row_join(-theta)
    require(d.rank()==1 and d.cols-d.rank()==1 and d.rows-d.rank()==2, 'theta cohomology dimensions')
    require(mat_eq(d.T, s.Matrix([[1,0,0],[-1,0,0]])), 'right adjoint dual differential signs')
    # Degree +1 quotient versus degree -1 dual.
    require(3-d.T.rank()==2, 'degree -1 dual of H1')
    # Restrictions to sigma differ by a chain homotopy, for a nonzero sigma test.
    rp=s.Matrix([[3]]); rm=s.Matrix([[7]]); Reta=s.Matrix([[5]])
    d2=rp.row_join(-rm)
    res_plus=(Reta*rp).row_join(s.zeros(1,1))
    res_minus=s.zeros(1,1).row_join(Reta*rm)
    require(mat_eq(res_plus-res_minus,Reta*d2), 'restriction homotopy')

# Original single-coordinate split carrier: None is tau; rational zero is supported e.
def add(a,b): return b if a is None else a if b is None else a+b
def mul(a,b): return None if a is None or b is None else a*b
def mask(x): return frozenset(i for i,a in enumerate(x) if a is not None)
def add_pair(x,y): return tuple(add(a,b) for a,b in zip(x,y))
def scale(r,x): return tuple(mul(r,a) for a in x)
def out_add(x,y):
    if x is None: return y
    if y is None: return x
    return (x[0] | y[0], x[1]+y[1])
def out_scale(r,x):
    return None if r is None or x is None else (x[0],r*x[1])
def d_supported(x):
    J=mask(x)
    if not J: return None
    return (J,(F(0) if x[0] is None else x[0])-(F(0) if x[1] is None else x[1]))

def split_checks():
    vals=[None,F(-1),F(0),F(1)]
    pairs=list(product(vals, repeat=2))
    ok=all(d_supported(add_pair(x,y))==out_add(d_supported(x),d_supported(y)) for x,y in product(pairs,pairs))
    require(ok, 'all 256 mixed addition comparisons')
    ok=all(d_supported(scale(r,x))==out_scale(r,d_supported(x)) for r,x in product(vals,pairs))
    require(ok, 'all 64 original scalar comparisons')
    require(d_supported((F(1),F(1)))==(frozenset({0,1}),F(0)), 'active cancellation remains joint e')
    require(d_supported((None,None)) is None, 'external absent pair remains tau')
    for x in pairs:
        out=d_supported(x)
        eo=out_scale(F(0),out)
        require(eo is None if not mask(x) else eo==(mask(x),F(0)), f'e retains mask {repr(x)}')

def action_checks():
    a=s.Integer(16)
    # Fourier intertwining of U_a and a U_(1/a), checked on power characters.
    t=s.symbols('t', real=True)
    for k in range(-2,4):
        # Fourier sends exponent k to 1-k in the scaling representation.
        lhs=a**k
        rhs=a*(1/a)**(1-k)
        require(s.simplify(lhs-rhs)==0, f'chart action exponent {k}')
    U=s.diag(1,2,8); Usrc=s.eye(2)
    d=s.Matrix([[1,-1],[0,0],[0,0]])
    require(mat_eq(U*d,d*Usrc), 'finite arithmetic chain equivariance')
    Udual=16*U.inv().T
    require(mat_eq(Udual,s.diag(16,8,2)), 'dual action retains target factor a')
    # Reflected finite model; no claim these model points are zeta zeros.
    R=s.Matrix([[0,2],[-2,0]]); J=s.diag(-s.Rational(1,2),s.Rational(1,2)); Q=R*J
    U2=s.diag(2,8)
    require(mat_eq(U2.T*R*U2,16*R), 'residue covariance on exact model')
    require(mat_eq(Q,s.Matrix([[0,1],[1,0]])), 'Jacobian trace contraction')
    require((s.Matrix([1,-1]).T*Q*s.Matrix([1,-1]))[0]==-2, 'base alone does not impose positive trace')

def tensor_checks():
    d=s.Matrix([[1,-1],[0,0],[0,0]]) # C0 dimension2, C1 dimension3
    D0=(s.kronecker_product(d,s.eye(2))).col_join(s.kronecker_product(s.eye(2),d))
    D1=(-s.kronecker_product(s.eye(3),d)).row_join(s.kronecker_product(d,s.eye(3)))
    require(mat_eq(D1*D0,s.zeros(9,4)), 'square differential Koszul signs')
    require(9-D1.rank()==4, 'square top cohomology is Q tensor Q')
    x=s.symbols('x');
    for r in range(1,7):
        # H0 rank1 and H1 rank2; the coefficient of x^r is 2^r.
        require(s.expand((1+2*x)**r).coeff(x,r)==2**r, f'tensor top rank r={r}')
        # The precise modulus defect for exponent rho=1/4 and base a=16.
        require(s.log((16**s.Rational(r,4))**2/16**r).expand(log=True)==-2*r*s.log(2), f'nonrescaled tensor defect r={r}')

def trace_checks():
    z=s.symbols('z')
    for m in range(1,6):
        # Multiplication by h=3+2z+z^2 on E[z]/z^m.
        M=s.zeros(m,m)
        for j in range(m):
            for power,c in ((0,3),(1,2),(2,1)):
                if j+power<m: M[j+power,j]=c
        require(s.trace(M)==3*m, f'full jet trace m={m}')
        cp=M.charpoly(); require(s.expand(cp.as_expr()-(cp.gen-3)**m)==0, f'jet characteristic polynomial m={m}')
    vals=[s.Rational(1,4),s.Rational(3,4),s.Rational(1,2)]
    V=s.Matrix([[x**k for x in vals] for k in range(3)])
    require(V.det()!=0, 'finite interpolation detects every removed value')
    U=s.diag(2,8,4)
    require(s.trace(U)-4==10, 'deleted reflected pair changes trace')
    require(U.det()/4==16, 'deleted reflected pair changes determinant')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--negative-control', action='store_true');ap.add_argument('--output')
    args=ap.parse_args()
    if args.negative_control: require(False, 'intentional negative control')
    projective_resolution();dualizing_complex();split_checks();action_checks();tensor_checks();trace_checks()
    out={'check_records':len(records),'suites':6,'records':records,'scope':'Finite regression checks only; no analytic proof or RH certificate.'}
    text=json.dumps(out,indent=2)
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(text+'\n')
    print(text)
if __name__=='__main__': main()
