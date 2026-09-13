#!/usr/bin/env python3
"""Replay the review's singular relation-block calibration exactly.

This is its declared mass-one Gaussian example, not a rescaling of an
arithmetic measure. Zero generalized eigenvalues remain in all products.
"""
import argparse
import json
import sympy as sp

parser=argparse.ArgumentParser()
parser.add_argument('--negative',action='store_true')
args=parser.parse_args()
checks=0
def ck(value,label):
    global checks
    checks+=1
    if not value:
        raise AssertionError(label)
if args.negative:
    ck(False,'intentional zero-mode negative control')
R=sp.Rational
F=sp.Matrix([[0,3,0],[-4,0,26],[0,-7,0]])
G=sp.Matrix([[1,0,1],[0,1,0],[1,0,3]])
O=sp.diag(6,24,120)
v=sp.Matrix([13,0,2])
ck(F*v==sp.zeros(3,1),'source kernel vector')
ck(F.rank()==2,'source column rank')
ck(all(G[:j,:j].det()>0 for j in range(1,4)),'original quotient Gram positive')
ck(all(O[j,j]>0 for j in range(3)),'source monic norms positive')
B=O.inv()*F.T*G*F
x=sp.symbols('x')
ck(sp.expand(B.charpoly(x).as_expr()-x*(x-R(19,4))*(x-R(83,10)))==0,'full generalized characteristic polynomial')
ck((sp.eye(3)+B).det()==R(2139,40),'determinant includes zero mode')
ck(sp.prod([1,1+R(19,4),1+R(83,10)])==(sp.eye(3)+B).det(),'three-factor product')
ck(((3+sp.trace(B))/3)**3 >= (sp.eye(3)+B).det(),'mean retains all three multiplicities')
K=G.inv()
Gj=(K+F*O.inv()*F.T).inv()
T=K*Gj
H=sp.eye(3)-T
ck(sp.expand(T.charpoly(x).as_expr()-(x-1)*(x-R(4,23))*(x-R(10,93)))==0,'unit restriction factor retained')
ck(T.det()==R(40,2139),'original volume ratio')
ck(T*sp.Matrix([9,0,-2])==sp.Matrix([9,0,-2]),'actual target isometric direction')
ck(H*sp.Matrix([9,0,-2])==sp.zeros(3,1),'loss zero direction retained')
ck(G.det()/Gj.det()==R(2139,40),'source quotient determinant comparison')
print(json.dumps({'status':'PASS','exact_checks':checks,
    'generalized_spectrum':['0','19/4','83/10'],
    'return_spectrum':['1','4/23','10/93'],
    'source_kernel_vector':[13,0,2],
    'target_unit_eigenvector':[9,0,-2],
    'source_mass':1,'arithmetic_packet':False},sort_keys=True))
