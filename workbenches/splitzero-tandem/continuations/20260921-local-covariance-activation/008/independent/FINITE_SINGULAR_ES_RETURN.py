"""Exact singular-period ES kernel, full obstruction, marked slice and restored return."""
from pathlib import Path
from hashlib import sha256
import itertools
import json
import argparse
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
I=s.I;rt=s.sqrt(2)
a,y,z,w,lam=s.symbols('a y z w lambda')
q=s.Matrix([a,y,z,w])
P=s.Matrix([
 a**3*z+2*a**2*y-I*a,
 -a**3*y**2*z-2*I*a**2*y*z+a**2*w-2*a**2*y**3-10*I*a*y**2+3*a*z+y,
 2*a**3*y**3*z+6*I*a**2*y**2*z+2*a**2*w*y+4*a**2*y**4+2*I*a*w-4*I*a*y**3-2*a*y*z+2*I*z+7*y**2,
 2*a**3*y**4*z+8*I*a**2*y**3*z+a**2*w*y**2+4*a**2*y**5+2*I*a*w*y+7*I*a*y**4-10*a*y**2*z-4*I*y*z-w-3*y**3])
K=s.Matrix([[0,I,1/rt,1/rt],[0,-1,-1-rt*I,1-rt*I],
 [I/2,-3*I,2*rt+6*I,-2*rt+6*I],[0,13,-34-19*rt*I,34-19*rt*I]])
one=s.ones(4,1);E=s.eye(4)-one*one.T/4
Ki=K.inv().applyfunc(lambda u:s.simplify(s.expand_complex(u)))
n=K*one;ell=one.T*Ki/4;ew=s.eye(4)[:,3]
checks=[];entries=0
def ck(name,values):
    global entries
    def flatten(value):
        if isinstance(value,(s.MatrixBase,list,tuple)):
            return [entry for item in value for entry in flatten(item)]
        return [value]
    vv=flatten(values)
    for value in vv:
        result=s.cancel(s.expand(value),extension=rt)
        assert result==0,(name,result)
    checks.append({'name':name,'entries':len(vv),'passed':True})
    entries+=len(vv)
    print(name,'passed',len(vv),flush=True)

ck('full original K inverse',K*Ki-s.eye(4))
ck('literal K determinant',K.det()-77*rt*I/2)
ck('full original kernel vector',n-s.Matrix([rt+I,-1-2*rt*I,19*I/2,13-38*rt*I]))
ck('complete four-label projection',[E*E-E,E*one,(ell*n)[0]-1])
ck('quotient and scalar exact inverse',K*(E+one*one.T/4)*Ki-s.eye(4))
Jp=P.jacobian(q)
# Full universal determinant, not evaluations at selected points.
ck('full universal original polynomial Jacobian determinant',s.expand(Jp.det(method='domain-ge'))+2)
target=s.Matrix([0,0,-1,0])
for j,label in enumerate(['M','N','T','E']):
    ck('original four-point collision '+label,P.subs(dict(zip(q,K[:,j])))-target)
ck('original target marking',target-2*I*K[:,0])

delta,gamma,S=s.symbols('delta gamma S',real=True)
rho=[s.Rational(1,2)+delta+I*gamma,s.Rational(1,2)+delta-I*gamma,
     s.Rational(1,2)-delta+I*gamma,s.Rational(1,2)-delta-I*gamma]
V=s.Matrix([[r**k for r in rho] for k in range(4)])
ck('unchanged quartet determinant',V.det()+64*delta**2*gamma**2*(delta**2+gamma**2))
ells=[s.prod((S-rho[b])/(rho[j]-rho[b]) for b in range(4) if b!=j) for j in range(4)]
ck('original interpolation constant direction',sum(ells)-1)
ck('original interpolation all marked coordinates',
   [s.cancel(ells[j].subs(S,rho[k]))-s.Integer(j==k) for j in range(4) for k in range(4)])
kw=s.Matrix([s.Rational(6,77),s.Rational(1,77),-(3+I*rt)/154,(3-I*rt)/154])
ck('actual fourth coordinate interpolation values',Ki*ew-kw)
vlead=s.Matrix([17+I*rt,-3+I*rt,-13-I*rt,-1-I*rt])/308
ck('all four leading obstruction coordinates',E*Ki*ew-vlead)
bw3=sum(kw[j]/s.prod(rho[j]-rho[k] for k in range(4) if k!=j) for j in range(4))
claimed_bw3=-(7*gamma+I*(2*delta+rt*gamma))/(616*delta*gamma*(delta**2+gamma**2))
ck('exact physical leading cubic coefficient',bw3-claimed_bw3)

# Whole kernel-line polynomial, with every lambda coefficient retained.
shifted=P.subs(dict(zip(q,q+lam*n)),simultaneous=True).applyfunc(s.expand)-P
directional=P
coeffs=[];obstructions=[]
for r in range(1,9):
    directional=directional.jacobian(q)*n
    directional=directional.applyfunc(s.expand)
    coefficient=s.Matrix([s.expand(p).coeff(lam,r) for p in shifted])
    ck('full directional coefficient '+str(r),coefficient-directional/s.factorial(r))
    coeffs.append(coefficient)
    obstructions.append((E*Ki*coefficient).applyfunc(s.expand))
Lambda=2*n[0]**3*n[1]**4*n[2]
ck('entire universal degree-eight coefficient',coeffs[-1]-Lambda*ew)
ck('entire universal degree-eight obstruction',obstructions[-1]-Lambda*vlead)
assert s.expand(Lambda)!=0
assert s.expand(vlead[0])!=0

mu1=s.symbols('mu1',nonzero=True)
mu2,mu3,mu4=s.symbols('mu2 mu3 mu4')
L=s.Matrix([[0,mu1,mu2,mu3],[0,0,2*mu1,3*mu2],[0,0,0,3*mu1]])
ck('fixed old rank3 nonzero minor',L[:,1:].det()-6*mu1**3)
Y0,Y1,Y2,t=s.symbols('Y0 Y1 Y2 t')
YY=s.Matrix([Y0,Y1,Y2])
c3=Y2/(3*mu1);c2=(Y1-3*mu2*c3)/(2*mu1);c1=(Y0-mu2*c2-mu3*c3)/mu1
sigma=s.Matrix([[1,s.Rational(1,2),s.Rational(1,4)+delta**2-gamma**2,
                s.Rational(1,8)+s.Rational(3,2)*(delta**2-gamma**2)]])
ck('all four exact original quartet means',[sum(r**j for r in rho)/4-sigma[j] for j in range(4)])
c0=-sigma[1]*c1-sigma[2]*c2-sigma[3]*c3
pp=s.Matrix([c0,c1,c2,c3]);section=pp.jacobian(YY)
ck('entire original finite-period section forward inverse',L*section-s.eye(3))
ck('entire section label-mean equation',sigma*section)
e0=s.eye(4)[:,0]
ck('entire augmented inverse in coefficient coordinates',section*L+e0*sigma-s.eye(4))
ck('physical obstruction quadratic coefficient',3*mu1*Lambda*bw3-3*mu1*Lambda*claimed_bw3)

# A fixed, complete quotient basis makes the slice computations independent
# of any unspecified inverse or period-coordinate change.
label_basis=s.Matrix([[-1,-1,-1,1],[1,0,0,1],[0,1,0,1],[0,0,1,1]])
Bfull=K*label_basis
Bi=Bfull.inv().applyfunc(lambda u:s.simplify(s.expand_complex(u)))
ck('entire four-coordinate slice basis inverse',Bfull*Bi-s.eye(4))
ck('lost-coordinate row of the slice basis',Bi.row(3)-ell)
values=[(3580+8830*I-4*rt*(549+1003*I))/616,
 (-80720-12413*I-8*rt*(1247+746*I))/616,
 (-39134+21326*I+rt*(3107-124144*I))/616,
 (-108226+40740*I+rt*(-2587+216544*I))/616]
for j,label in enumerate(['M','N','T','E']):
    JJ=Jp.subs(dict(zip(q,K[:,j]))).applyfunc(s.expand)
    transported=Bi*JJ*Bfull
    direct=s.expand(transported[:3,:3].det())
    cofactor=s.expand(-2*(ell*JJ.inv()*n)[0])
    ck('marked slice Jacobian '+label,[direct-values[j],direct-cofactor])
    assert s.simplify(values[j])!=0
    ck('marked quotient coordinates '+label,Bi*K[:,j]-label_basis.inv()*s.eye(4)[:,j])
assert s.simplify(values[0]-values[1])!=0

# Complete Gamma square completion, with conjugation retaining cross terms.
tr,ti,ur,ui,M0,N0=s.symbols('t_R t_I chi_R chi_I M N',real=True)
tt=tr+I*ti;chi=ur+I*ui
ck('entire original Gamma norm completion',
   N0+M0*(tt*s.conjugate(chi)+s.conjugate(tt)*chi+tt*s.conjugate(tt))
   -(N0-M0*chi*s.conjugate(chi)+M0*(tt+chi)*s.conjugate(tt+chi)))
G1=s.Matrix([[mu1,mu2,mu3,mu4],[0,2*mu1,3*mu2,4*mu3],
             [0,0,3*mu1,6*mu2],[0,0,0,4*mu1]])
Dprime=s.Matrix([[mu1,mu2,mu3,mu4],[0,mu1,2*mu2,3*mu3],
                 [0,0,mu1,3*mu2],[0,0,0,mu1]])
shiftout=s.Matrix([[0,0,0],[1,0,0],[0,1,0],[0,0,1]])
ck('full original actual-order matrix determinant',G1.det()-24*mu1**4)
ck('all entries of the exact original commutator correction',G1-shiftout*L-Dprime)
ck('actual correction restores the original kernel',G1*e0-mu1*e0)

parser=argparse.ArgumentParser()
parser.add_argument('--reader-source',type=Path,help='Optional original version-69 TeX for a fresh source-hash verification. All polynomial identities are checked independently of this option.')
args=parser.parse_args()
reader_hash='678b3f70ee7d2a6d00f6c588d7778e390118ab4743a5759612dbba6430984c78'
if args.reader_source is not None:
    assert sha256(args.reader_source.read_bytes()).hexdigest()==reader_hash
proof=HERE/'FINITE_SINGULAR_ES_RETURN.tex'
files=[proof,Path(__file__),ROOT/'FINITE_PERIOD_ZERO_CERTIFICATE.json',ROOT/'certify_finite_period_zero.py',
       ROOT/'FABLE_TO_ORIGINAL_CONDUCTOR.tex',ROOT/'source_dependencies/WEIGHTED_CONDUCTOR_FORWARD.tex']
receipt={'status':'passed','groups':len(checks),'entries':entries,'checks':checks,
 'kernel_n':[str(z) for z in n],'mean_row':[str(z) for z in ell],
 'full_obstruction_coefficients':[
     {'lambda_degree':r+1,'P_difference_coefficient':[str(z) for z in coeffs[r]],
      'zero_mean_label_obstruction':[str(z) for z in obstructions[r]]} for r in range(8)],
 'physical_cubic_coefficient':str(claimed_bw3),
 'slice_jacobians':{j:str(values[k]) for k,j in enumerate(['M','N','T','E'])},
 'sources':[{'name':p.name,'sha256':sha256(p.read_bytes()).hexdigest()} for p in files]
          +[{'name':'erdos_straus_project_reader.tex','sha256':reader_hash,
             'source_hash_verified_in_this_run':args.reader_source is not None,
             'read_coverage':'Lines19461–19640: literal four-dimensional polynomial, four marked coordinates, Jacobian assertion and proof. Independently exact-checked here.'}],
 'scope':'Exact old singular-conductor ES transport. The companion finite-period interval certificate is an imported source and was read, not rerun by this checker. No zeta-zero quartet or arithmetic-unit phase is asserted.'}
(HERE/'FINITE_SINGULAR_ES_RETURN.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','groups':len(checks),'entries':entries}),flush=True)
