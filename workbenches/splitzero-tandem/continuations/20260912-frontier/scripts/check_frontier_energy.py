"""Exact Gaussian calibration of frontier energy/determinant identities.

Uses the untouched supplied source model with original mass, nonconstant unit,
imaginary recurrence diagonal and full repeated jets. No arithmetic zeros or
infinite arithmetic moment integrals are asserted.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys
import sympy as sp

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'sources/web_symmetric_frontier_delivery/Tau_Symmetric_Frontier_Control/check_frontier_control.py'
spec=importlib.util.spec_from_file_location('symmetric_frontier_original',SOURCE)
src=importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)
rows=[]

def check(name,value):
    rows.append(dict(name=name,passed=bool(value)))

def eq(name,left,right):
    difference=sp.Matrix(left)-sp.Matrix(right)
    check(name,all(sp.cancel(sp.expand(x))==0 for x in difference))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--json',type=Path,required=True)
    parser.add_argument('--negative-control',action='store_true')
    args=parser.parse_args()
    x=src.s-sp.Rational(1,2)
    repeated=src.Model(x*x,1+sp.I*x,mass=7,mean=sp.Rational(1,3),variance=2)
    off=src.Model((src.s-sp.Rational(1,4))*(src.s-sp.Rational(3,4)),1+src.s,mass=11,mean=0,variance=1)
    for name,model,k,M in [('repeat-one',repeated,1,3),('repeat-two',repeated,2,2),('off-two',off,2,3)]:
        K=model.kernel(k,M);G=K.inv();Kn=model.kernel(k,M+1);Gn=Kn.inv()
        high,F,E,Omega=model.frontier(k,M);Oi=Omega.inv();H=Omega+F.H*G*F
        low=[a for deg in range(M+1) for a in src.comp(deg,k)]
        Z=sp.Matrix.hstack(*(model.z(a) for a in low))
        Ol=sp.diag(*(model.weight(a) for a in low))
        R=Ol.inv()*Z.H*G
        b=(-R*F).col_join(sp.eye(len(high)))
        Htot=sp.diag(Ol,Omega)
        Y=-b*H.inv()*F.H*G
        C=b*Oi*E.H*G
        Delta=sp.simplify(G-Gn)
        A=model.action(k);W=sp.simplify(A.H*G+G*A-k*G)
        P=sp.simplify(G*F*Oi*F.H)
        eq(name+'-relation-Gram',b.H*Htot*b,H)
        eq(name+'-relative-loss',G.inv()*Delta, G.inv()*P*(sp.eye(P.rows)+P).inv()*G)
        eq(name+'-positive-loss',Delta,Y.H*Htot*Y)
        eq(name+'-boundary-factorization',W,-Y.H*Htot*C-C.H*Htot*Y)
        check(name+'-rank-loss',Delta.rank()==F.rank()==Y.rank())
        check(name+'-rank-derivative',C.rank()==E.rank())
        tau=sp.cancel(sp.trace(G.inv()*Delta))
        eq(name+'-trace-loss',[[tau]],[[sp.trace(P*(sp.eye(P.rows)+P).inv())]])
        pi=sp.cancel(Gn.det()/G.det())
        check(name+'-determinant-spectrum',sp.cancel(pi*(sp.eye(P.rows)+P).det())==1)
        chi=sp.cancel(sp.trace(G.inv()*C.H*Htot*C))
        expected=sp.trace(Oi*E.H*G*E)+sp.trace(Oi*F.H*G*F*Oi*E.H*G*E)
        check(name+'-complete-derivative-energy',sp.cancel(chi-expected)==0)
        check(name+'-retained-mass',model.mass in (7,11))
        check(name+'-relative-positive',tau>=0 and chi>=0 and pi>0 and pi<=1)
        if name=='off-two':
            Gamma=k*(M+1)*model.variance
            delta=sp.Rational(1,4)
            check(name+'-determinant-spectral-lower',1/pi>=1+k*k*delta*delta/Gamma)
    if args.negative_control:
        check('intentional-false-control',False)
    failed=[r['name'] for r in rows if not r['passed']]
    result=dict(all_passed=not failed,passed=len(rows)-len(failed),total=len(rows),failed=failed,
                negative_control=args.negative_control,python_optimization=sys.flags.optimize,
                source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),sympy=sp.__version__,
                records=rows,scope=__doc__.strip())
    args.json.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(all_passed=result['all_passed'],passed=result['passed'],total=result['total'],failed=failed)))
    return 0 if not failed else 1

if __name__=='__main__':sys.exit(main())
