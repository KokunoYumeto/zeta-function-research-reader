"""Exact replay of retained fibre, projective completion, and determinant encodings.
Run: python check_fibre_complexity.py
Needs Python 3 and SymPy; no network, Lean, mutable sibling imports or floats.
"""
from pathlib import Path
import datetime, hashlib, json, platform
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def zero(name,expr):
    num=s.fraction(s.cancel(expr))[0]
    ok=s.Poly(num,*sorted(num.free_symbols,key=str)).is_zero if num.free_symbols else num==0
    if not ok: raise AssertionError((name,s.factor(num)))
    checks.append({'id':name,'status':'pass','method':'exact rational-polynomial identity'})
def equal(name,left,right):
    if isinstance(left,s.MatrixBase):
        if left.shape!=right.shape: raise AssertionError(name+' shape')
        for i,expr in enumerate(left-right): zero(name+':'+str(i),expr)
    else: zero(name,left-right)
x,y,w,a,b,c,r,alpha,h,z,t=s.symbols('x y w a b c r alpha h z t')
F=s.Matrix([(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
 y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),2*x-3*x*x*y-x**3*w])
P=c*r**3-2*r**2+b*r-2*a; Pd=s.diff(P,r)
D=4*(b*b-c*b**3+18*a*b*c-16*a-27*a*a*c*c)
equal('original_jacobian',F.jacobian((x,y,w)).det(),-2)
H={x:1/alpha,y:r-alpha,w:5*alpha**2-3*r*alpha-c*alpha**3}
equal('first_chart',F.subs(H,simultaneous=True),s.Matrix([r*r+r*alpha-c*r**3,4*r+2*alpha-3*c*r*r,c]))
equal('chart_target_a',2*(F[0].subs(H,simultaneous=True).subs(alpha,Pd/2)-a),P)
equal('chart_target_b',F[1].subs(H,simultaneous=True).subs(alpha,Pd/2),b)
equal('source_P',P.subs({a:F[0],b:F[1],c:F[2],r:y+1/x},simultaneous=True),0)
equal('source_Pprime',Pd.subs({a:F[0],b:F[1],c:F[2],r:y+1/x},simultaneous=True),2/x)
equal('boundary',F.subs(x,0),s.Matrix([w+4*y*y,y,0]))
for i,pnt in enumerate([(1,s.Rational(-3,2),s.Rational(13,2)),(-1,s.Rational(3,2),s.Rational(13,2)),(0,0,s.Rational(-1,4))]):
 equal('collision_'+str(i),F.subs(dict(zip((x,y,w),pnt))),s.Matrix([s.Rational(-1,4),0,0]))
S=s.Matrix([[c,-2,b,-2*a,0],[0,c,-2,b,-2*a],[3*c,-4,b,0,0],[0,3*c,-4,b,0],[0,0,3*c,-4,b]])
equal('resultant_matrix',S.det(),-c*D)
equal('discriminant',s.discriminant(P,r),D)
C=s.Matrix([[0,0,2*a/c],[1,0,-b/c],[0,1,2/c]])
N=3*c*C*C-4*C+b*s.eye(3)
equal('multiplication_Pprime_determinant',N.det(),-D/c)
equal('multiplication_Pprime_adjugate',N*(-c/D)*N.adjugate(),s.eye(3))
equal('triple_root',P.subs({a:4/(27*c*c),b:4/(3*c)}),c*(r-2/(3*c))**3)
equal('nonfinite_arc',F.subs({x:1/t,y:-3*t/2,w:13*t*t/2},simultaneous=True),s.Matrix([-t*t/4,0,0]))
v=1+x*y
binary=F[2]*v**3-2*v*v*x+F[1]*v*x*x-2*F[0]*x**3
zero('projective_forward_binary',binary)
Q=c-2*h+b*h*h-2*a*h**3; d=s.diff(Q,h)
xx=-2*h/d; yy=b-3*a*h; ww=-a*d**3/8-yy**2*d*d/4+3*yy**2*d/2
second={x:xx,y:yy,w:ww}
equal('second_chart_v',1+xx*yy,-2/d)
equal('second_chart_targets',F.subs(second,simultaneous=True),s.Matrix([a,b,c-Q]))
equal('second_chart_source_d',d.subs({a:F[0],b:F[1],h:x/v},simultaneous=True),-2/v)
equal('second_chart_source_y',F[1]-3*F[0]*x/v,y)
equal('root_chart_polynomial_overlap',Q,h**3*P.subs(r,1/h))
equal('root_chart_derivative_overlap',d+h*Pd.subs(r,1/h),3*Q/h)
equal('second_chart_boundary',s.Matrix([xx,yy,ww]).subs(h,0),s.Matrix([0,b,a-4*b*b]))
lam=s.symbols('lambda')
Hlam=c*(1+lam*z)**3-2*(1+lam*z)**2*z+b*(1+lam*z)*z*z-2*a*z**3
expanded=P.subs(r,lam)*z**3+(3*c*lam**2-4*lam+b)*z*z+(3*c*lam-2)*z+c
equal('projective_chart_full_coefficients',Hlam,expanded)
equal('projective_chart_discriminant',s.discriminant(Hlam,z),D)
equal('projective_base_cover',P.subs(r,1)+P.subs(r,-1)-2*P.subs(r,0),-4)
M=s.Matrix([[r,-1,0,0],[0,r,-1,0],[0,0,r,-1],[-2*a,b,-2,c]])
equal('single_determinant',M.det(),P)
Mh=s.Matrix([[r,-z,0,0],[0,r,-z,0],[0,0,r,-z],[-2*a,b,-2*z,c]])
Ph=c*r**3-2*z*z*r*r+b*r*z*z-2*a*z**3
equal('single_homogeneous_determinant',Mh.det(),Ph)
equal('single_homogenization_map',Ph,z**4*P.subs({a:a/z,b:b/z,c:c/z,r:r/z},simultaneous=True))
for n in (1,2):
 aa=s.symbols('a1:'+str(n+1));bb=s.symbols('b1:'+str(n+1));cc=s.symbols('c1:'+str(n+1));rr=s.symbols('r1:'+str(n+1));tt=s.symbols('t1:'+str(n+1))
 for homogeneous in (False,True):
  one=z if homogeneous else s.Integer(1)
  blocks=[s.Matrix([[one,-rr[i],0,0],[0,one,-rr[i],0],[0,0,one,-rr[i]],[0,0,0,one]]) for i in range(n)]
  T=s.diag(*blocks);V=s.Matrix([e for i in range(n) for e in (-2*aa[i],bb[i],-2*one,cc[i])]);U=s.Matrix([[e for i in range(n) for e in (tt[i],0,0,0)]])
  big=T.row_join(V).col_join((-U).row_join(s.zeros(1,1)))
  expected=sum(tt[i]*(cc[i]*rr[i]**3-2*rr[i]**2*one**2+bb[i]*rr[i]*one**2-2*aa[i]*one**3) for i in range(n))
  if homogeneous:expected=z**(4*n-4)*expected
  equal('selector_det_n'+str(n)+'_hom'+str(homogeneous),big.det(method='domain-ge'),expected)
  if not homogeneous:
   for i in range(n):equal('selector_recovery_n'+str(n)+'_i'+str(i),s.diff(expected,tt[i]),cc[i]*rr[i]**3-2*rr[i]**2+bb[i]*rr[i]-2*aa[i])
# Reconstruct every gate independently and compare original outputs.
g=[None]
def gate(expr):g.append(expr);return len(g)-1
gate(x*y);gate(1+g[1]);gate(g[2]*g[2]);gate(g[3]*g[2]);gate(3*g[1]);gate(4+g[5]);gate(y*y);gate(g[7]*g[6]);gate(g[2]*g[8]);gate(g[4]*w);gate(g[10]+g[9]);gate(x*g[3]);gate(g[12]*w);gate(3*g[13]);gate(x*g[8]);gate(3*g[15]);gate(y+g[14]);gate(g[17]+g[16]);gate(x*x);gate(g[19]*x);gate(g[19]*y);gate(3*g[21]);gate(g[20]*w);gate(2*x);gate(g[24]-g[22]);gate(g[25]-g[23])
assert len(g)-1==26
equal('26_gate_original_outputs',s.Matrix([g[11],g[18],g[26]]),F)
assert [s.Poly(f,x,y,w).total_degree() for f in F]==[7,6,4]
checks.append({'id':'original_total_degrees','status':'pass','degrees':[7,6,4]})
artifacts=['fibre_complexity.tex','standalone.tex','check_fibre_complexity.py','source_hashes.json','raw_user_directives.md','LOGBOOK.md']
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':platform.python_version(),'sympy':s.__version__,'scope':'Exact rational symbolic replay; written proofs establish the scheme, field, and asymptotic statements. No Lean certification and no complexity lower bound claimed.','checks':checks,'all_pass':True,'check_count':len(checks),'artifacts':[{'path':name,'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in artifacts]}
(ROOT/'check_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_pass':True,'check_count':len(checks),'receipt':str(ROOT/'check_receipt.json')}))
