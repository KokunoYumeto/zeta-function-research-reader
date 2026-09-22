from pathlib import Path
import json
import sympy as s
import mpmath as mp
mp.mp.dps=55
checks=[]
def check(label,test):
    if not test:raise ArithmeticError(label)
    checks.append(label)
def zero(A):return all(s.cancel(x)==0 for x in A)
def mm(x):return mp.mpf(str(s.N(x,58)))
z=s.symbols('z',positive=True)
T0=s.diag(0,2,3,0)
L0=s.Matrix([[1,1,1,0],[0,1,1,1]])
I0=s.Matrix([[-1,-1],[1,0],[0,1],[-1,-1]])
S=s.Matrix([[1,s.I,0,0],[0,1,0,0],[0,0,1,s.I/2],[0,0,0,2]])
O=s.Matrix([[1,s.I],[0,2]])
T=S.inv()*T0*S;Lam=O*L0*S;IK=S.inv()*I0
Gs=[(211,19,23,409),(201,17,19,401),(113,11,13,211),(101,7,11,199)]
angles=[];energies=[];HKs=[];Fs=[]
for ni,g in enumerate(Gs):
    G=S.H*s.diag(*g)*S
    H=G.inv()*T.H*G*T
    HK=IK.H*G*IK;F=IK.H*T.H*G*T*IK
    Q=(Lam*G.inv()*Lam.H).inv();L=G.inv()*Lam.H*Q
    check(f'{ni} original kernel',zero(Lam*IK))
    check(f'{ni} exact attained section',zero(Lam*L-s.eye(2)))
    Y=Lam*z*(z*s.eye(4)+H).inv()*L
    rhs=(s.eye(2)+HK.inv()*F/z).det()/(s.eye(4)+H/z).det()
    check(f'{ni} complete determinant',s.cancel(Y.det()-rhs)==0)
    Y0=L0*z*(z*s.eye(4)+T0.T*T0).inv()*s.diag(*g).inv()*L0.T*(L0*s.diag(*g).inv()*L0.T).inv()
    check(f'{ni} original observation coordinate transport',zero(Y-O*Y0*O.inv()))
    sig=s.Integer(4)
    Z=12*(2*s.eye(2)+Y.subs(z,2*sig/3)).inv()-4*(s.eye(2)+Y.subs(z,sig/2)).inv()-2*s.eye(2)
    # Derive the same secant from the original rational filtered response.
    x=s.symbols('x',positive=True)
    Yfilter=(x*s.eye(2)+Y.subs(z,sig*x/(1+x)))/(1+x)
    Zfilter=2*(2*Yfilter.subs(x,2).inv()-Yfilter.subs(x,1).inv()-s.eye(2))
    check(f'{ni} two-response positive secant identity',zero(Z-Zfilter))
    HZ=(Q*Z).applyfunc(s.simplify)
    check(f'{ni} secant physical Hermiticity',zero(HZ-HZ.H))
    check(f'{ni} secant physical positivity',HZ[0,0]>=0 and HZ[1,1]>=0 and HZ.det()>=0)
    vals=sorted([mm(e) for e,m in (HK.inv()*F).eigenvals().items() for _ in range(m)])
    energies.append(vals);HKs.append(HK);Fs.append(F)
    check(f'{ni} all original compressed energies retained',len(vals)==2 and min(vals)>0)

sgn=[1,1,-1,-1]
alpha_logs=[[mp.log(x) for x in a] for a in energies]
D=sum(abs(alpha_logs[i][j]-alpha_logs[i+2][j]) for i in range(2) for j in range(2))
f=lambda t:mp.atan(mp.exp(t))
def phase(x):return sum(sgn[i]*(mp.atan(4*mp.exp(-x))+mp.atan(9*mp.exp(-x))-sum(f(a-x) for a in alpha_logs[i])) for i in range(4))
knots=sorted(set([-mp.mpf(100),mp.mpf(100)]+[a for row in alpha_logs for a in row]))
area=mp.quad(phase,knots)
absolute=mp.quad(lambda x:abs(phase(x)),knots)
expected=-mp.pi/2*sum(sgn[i]*sum(alpha_logs[i]) for i in range(4))
check('phase area numerical55-digit check',abs(area-expected)<mp.mpf('1e-38'))
check('whole curve L1 bound numerical check',absolute<=mp.pi*D/2+mp.mpf('1e-30'))
Kret=sum(sgn[i]*mp.log(mm(HKs[i].det())) for i in range(4))
Fret=sum(sgn[i]*mp.log(mm(Fs[i].det())) for i in range(4))
check('original kernel determinant phase receiver',abs(Kret-(2*area/mp.pi+Fret))<mp.mpf('1e-38'))
for a,b in [(mp.mpf(-3),mp.mpf(2)),(mp.mpf(1),mp.mpf('1.001')),(mp.mpf(8),mp.mpf(-4))]:
    knots=[min(a,b)-100,min(a,b),max(a,b),max(a,b)+100]
    value=mp.quad(lambda x:abs(f(a-x)-f(b-x)),knots)
    check('scalar exact area numerical '+str((a,b)),abs(value-mp.pi*abs(a-b)/2)<mp.mpf('1e-38'))
for q in [1,7,31]:
    smooth=2*mp.quad(lambda x:mp.atan(mp.exp(-q*x)),[0,1,mp.inf])
    check('Catalan smoothing '+str(q),abs(smooth-2*mp.catalan/q)<mp.mpf('1e-48'))
check('negative control: independent kernel metric deletion',abs(Kret)>mp.mpf('1e-5'))
check('negative control: secant is not raw-coordinate Hermitian',not zero(Z-Z.H))
check('negative control: secant explanatory factor two is necessary',not zero(Z-Zfilter/2))
record={'all_passed':True,'exact_checks':32,'numeric_checks':9,'negative_controls':3,'labels':checks,
 'phase_area':mp.nstr(area,45),'kernel_return':mp.nstr(Kret,45),'L1_phase':mp.nstr(absolute,45),'L1_upper':mp.nstr(mp.pi*D/2,45),
 'scope':'Specified finite auxiliary original maps and complex metric transport. No native arithmetic period evaluated; numerical integrals are distinguished from exact algebra.'}
# Counts are verified from the actual labels, rather than inferred from a receipt.
if len(checks)!=44:raise ArithmeticError('check count: '+str(len(checks)))
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k!='labels'},indent=2))
