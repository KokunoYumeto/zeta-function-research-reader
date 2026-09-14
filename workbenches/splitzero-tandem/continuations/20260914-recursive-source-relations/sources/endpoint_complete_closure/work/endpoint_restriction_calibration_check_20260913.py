"""Exact enclosure of the delivered mass-seven nilpotent calibration."""
from pathlib import Path
from fractions import Fraction as F
import argparse, importlib.util, json

def require(c,m):
    if not c: raise ArithmeticError(m)

def logarithm(x,terms=48):
    x=F(x);require(x>0,'positive log argument')
    if x<1:
        a,b=logarithm(1/x,terms);return -b,-a
    e=0
    while x>=2: x/=2;e+=1
    def interval(y):
        t=(y-1)/(y+1)
        lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
        return lo,lo+2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    a,b=interval(x);c,d=interval(F(2));return a+e*c,b+e*d

def main():
    p=argparse.ArgumentParser();p.add_argument('--source-checker',type=Path,required=True);p.add_argument('--json',type=Path,required=True);a=p.parse_args()
    spec=importlib.util.spec_from_file_location('retained_restriction_source',a.source_checker)
    source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
    s=source.s;S=source.S;fixture=source.fixture((S-1)**2,8)
    C=s.Matrix([[1,-1],[0,1]]);Ci=C.inv();N=Ci*fixture['A']*C-s.eye(2)
    require(N==s.Matrix([[0,0],[1,0]]) and N*N==s.zeros(2),'literal nilpotent action')
    expect={1:[F(1,7),F(1,7)],2:[F(3,14),F(1,7)],3:[F(3,14),F(5,14)],4:[F(15,56),F(5,14)]}
    for n,v in expect.items():
        shifted=Ci*source.level(fixture,n)['K']*Ci.conjugate().T
        require(shifted==s.diag(*[s.Rational(x.numerator,x.denominator) for x in v]),'original kernel at degree '+str(n))
    rows=[];total_lower=F(0);total_upper=F(0);direct=F(0)
    for i,j in [(1,3),(2,4)]:
        g=[expect[i][a]/expect[j][a] for a in range(2)]
        require(all(F(2,5)<=x<=1 for x in g),'exact nonstrict gap')
        h=[1-x for x in g];r=F(3,5)
        moments=[sum((x**m for x in h),F(0)) for m in [1,2,3]]
        lower=moments[0]+moments[1]/2
        lnlo,lnhi=logarithm(F(5,2))
        certlo=lower+(lnlo-r-r*r/2)*moments[2]/r**3
        certhi=lower+(lnhi-r-r*r/2)*moments[2]/r**3
        ratio=1/(g[0]*g[1]);loglo,loghi=logarithm(ratio)
        require(lower<=loglo and loghi<=certhi,'rigorous trace enclosure')
        W=source.window(fixture,i,j)
        for m,v in enumerate(moments,1):require(s.trace(W['H']**m)==s.Rational(v.numerator,v.denominator),'actual trace moment')
        total_lower+=certlo;total_upper+=certhi
        direct+=sum((1/x-1 for x in g),F(0))
        rows.append({'i':i,'j':j,'restriction_eigenvalues':list(map(str,g)),'loss_eigenvalues':list(map(str,h)),'trace_moments_1_2_3':list(map(str,moments)),'volume_ratio':str(ratio),'log_volume_interval':list(map(str,[loglo,loghi])),'p2_certificate_interval':list(map(str,[certlo,certhi]))})
    threshold=F('2.469887624578038')
    require(total_upper<threshold,'published strict decimal upper bound')
    require(direct==F(15,4) and total_upper<direct,'strict improvement over same direct trace')
    payload={'status':'PASS','scope':'exact mass-seven Gaussian nilpotent fixture; no arithmetic zeta certificate','normalization_changed':False,'source_checker_sha256':__import__('hashlib').sha256(a.source_checker.read_bytes()).hexdigest(),'nilpotent_matrix':[['0','0'],['1','0']],'kernel_degrees_verified':[1,2,3,4],'rows':rows,'combined_p2_certificate_interval':list(map(str,[total_lower,total_upper])),'strict_upper_threshold':str(threshold),'strict_upper_threshold_decimal':'2.469887624578038','strict_threshold_verified':True,'direct_trace_bound':str(direct),'strict_improvement_verified':True}
    a.json.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print('PASS: four literal kernels, nilpotent action, two spectra, six moments, exact logarithm intervals and strict combined upper bound.')

if __name__=='__main__': main()
