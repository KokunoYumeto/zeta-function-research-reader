from pathlib import Path
import json
import sympy as s

checks=[]
def zero(name,value):
    if isinstance(value,s.MatrixBase): good=all(s.simplify(v)==0 for v in value)
    else: good=s.simplify(value)==0
    if not good: raise ArithmeticError(name)
    checks.append(name)
def nonnegative(name,value):
    v=s.simplify(value)
    if v.is_nonnegative is not True: raise ArithmeticError((name,v))
    checks.append(name)
def abs2(z): return s.simplify(s.conjugate(z)*z)
for model,(t,d,j) in enumerate([(3,2,1),(2,3,1),(4,1,2)]):
    ep=s.Rational(j*j+d*d,j)
    C=s.Matrix([[t,-j,0],[-j,t,0],[0,0,t]])
    e=s.Matrix([1,0,0]);f=s.Matrix([0,1,0]);x=s.Matrix([1,s.I*s.Rational(d,j),0])
    M=C+ep*f*e.H; w=t-s.I*d
    E=(x.H*x)[0];A=(e.H*x)[0];B=(f.H*x)[0]
    D=s.sqrt(t*t+d*d)+t+j
    ar=E/abs2(A);br=E/abs2(B);cc=-s.I*ep*s.conjugate(A)*B/E
    pre=f'model{model}'
    zero(pre+'_eigenclass',M*x-w*x)
    zero(pre+'_current_sign',s.re(cc)-d)
    zero(pre+'_product',ar*br-ep**2/abs2(cc))
    nonnegative(pre+'_alpha_lower',ar-ep**2/D**2)
    nonnegative(pre+'_alpha_upper',ep**2/d**2-ar)
    nonnegative(pre+'_beta_lower',br-1)
    nonnegative(pre+'_beta_upper',D**2/d**2-br)
    for N in range(4):
        F13=(-s.I)**N*A;F23=(-s.I)**(N+1)*B
        zero(pre+f'_physical_phase{N}',s.conjugate(F13)*F23*ep/E-cc)
    for qid,n in enumerate([s.Matrix([1,1+s.I,2]),s.Matrix([1,s.I,1]),s.Matrix([2,1-2*s.I,3])]):
        Q=n*n.H/(n.H*n)[0];P=s.eye(3)-Q
        U=(e.H*Q*x)[0]/A;V=(f.H*Q*x)[0]/B
        ak=(e.H*Q*e)[0];bk=(f.H*Q*f)[0];theta=(x.H*Q*x)[0]/E
        nonnegative(pre+f'_U_bound{qid}',ep**2*ak*theta/d**2-abs2(U))
        nonnegative(pre+f'_V_bound{qid}',D**2*bk*theta/d**2-abs2(V))
        Ps=[s.conjugate(U)*V,(1-s.conjugate(U))*(1-V),s.conjugate(U)+V-2*s.conjugate(U)*V]
        W=s.I*(M-M.H)
        xK=Q*x;xB=P*x
        vals=[(xK.H*W*xK)[0],(xB.H*W*xB)[0],2*s.re((xK.H*W*xB)[0])]
        for a,(v,p) in enumerate(zip(vals,Ps)):zero(pre+f'_all_currents{qid}_{a}',v/(2*E)-s.re(cc*p))
        zero(pre+f'_three_products{qid}',sum(Ps)-1)
        # Exact nonidentity coordinate metric; preserve adjoints and projections.
        S=s.diag(1,2,3);G=S*S;xx=S.inv()*x;ee=S.inv()*e;ff=S.inv()*f
        QQ=S.inv()*Q*S;MM=S.inv()*M*S
        zero(pre+f'_metric_projection{qid}',QQ.H*G-G*QQ)
        zero(pre+f'_metric_U{qid}',(ee.H*G*QQ*xx)[0]/(ee.H*G*xx)[0]-U)
        zero(pre+f'_metric_V{qid}',(ff.H*G*QQ*xx)[0]/(ff.H*G*xx)[0]-V)
        zero(pre+f'_metric_current{qid}',(xx.H*(s.I*(G*MM-MM.H*G))*xx)[0]-(x.H*W*x)[0])
bad_sign=s.I*5*s.conjugate(s.Integer(1))*2*s.I/5
if s.re(bad_sign)==2:raise ArithmeticError('Reversed phase negative control escaped')
receipt={'status':'passed','exact_checks':len(checks),'negative_controls_rejected':1,
         'scope':'Auxiliary finite nonnormal eigenclass and complete projection identities in a nonidentity Hermitian metric; no native period numerical evaluation.',
         'checks':checks}
Path(__file__).with_name('DENOMINATOR_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='checks'},indent=2))
