"""Exact independent algebra checks for the complete EF family.

The accompanying review gives the algebraic and metric proofs. No source
discovery, rendering, packaging or publication is performed by this script.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
A,k,d,x,m=s.symbols('A k d x m')
p,g=s.symbols('p gamma',positive=True)
z=s.symbols('z',real=True)
eps=s.symbols('epsilon')
i=s.I
checks=[]

def zero(name,value):
    seq=list(value) if isinstance(value,(s.MatrixBase,list,tuple)) else [value]
    bad=[str(s.factor(v)) for v in seq if s.factor(v)!=0]
    checks.append({'name':name,'entries':len(seq),'passed':not bad})
    if bad: raise AssertionError((name,bad))

kap=k*k-d*d
a0=k*k+d*d
q=(x-k)**2*(x*x-d*d)
eu=(x*x-d*d)*(3*k*k-d*d-2*k*x)/kap**2
el=(x-k)**2*(a0+2*k*x)/kap**2

def rem(f): return s.cancel(s.rem(f,q,x))
def col(f):
    pp=s.Poly(rem(f),x)
    return s.Matrix([pp.nth(j) for j in range(4)])

zero('projector polynomial sum',eu+el-1)
zero('all projector algebra identities',[rem(eu*eu-eu),rem(el*el-el),rem(eu*el)])
PU=s.Matrix([[d*d*(d*d-3*k*k),k*d*d*kap],
             [2*k*d*d,-d*d*kap],[3*k*k-d*d,-k*kap],[-2*k,kap]])/kap**2
PL=s.Matrix([[k*k*a0,2*k**3*d*d],[-2*k*d*d,k*k*(k*k-3*d*d)],
             [d*d-3*k*k,-2*k**3],[2*k,a0]])/kap**2
P=PU.row_join(PL)
Pinv=s.Matrix([[1,k,k*k,k**3],[0,1,2*k,3*k*k],
               [1,0,d*d,0],[0,1,0,d*d]])
zero('all primary inclusion coefficients',P-s.Matrix.hstack(col(eu),col(eu*(x-k)),col(el),col(el*x)))
zero('both full primary inverse products',list(P*Pinv-s.eye(4))+list(Pinv*P-s.eye(4)))
zero('primary determinant',P.det()-kap**-2)
Cm=s.Matrix(4,4,lambda row,cl: s.binomial(cl,row)*m**(cl-row) if cl>=row else 0)
Cminus=Cm.subs(m,-m)
zero('full centre shift inverse',Cm*Cminus-s.eye(4))
zero('original-coordinate full primary inverse',Pinv*Cm*Cminus*P-s.eye(4))

u=2*A*a0; v=-4*A*k*d*d
hp=s.diff(A*q,x)
upper=s.Poly(hp.subs(x,k+eps).expand(),eps)
zero('upper derivative with original coefficient',s.rem(upper.as_expr(),eps**2,eps)-2*A*kap*eps)
zero('lower derivative with original coefficient',s.rem(hp,x*x-d*d,x)-u*x-v)

# Full residue in the quartic basis, then all 64 primary Gram entries.
def res_odd(f): return s.cancel(s.Poly(rem(f),x).nth(3)/A)
pe=[eu,eu*(x-k),el,el*x]
cross=s.Matrix([[res_odd(f*h) for h in pe] for f in pe])
JU=s.Matrix([[-2*k/(A*kap**2),1/(A*kap)],[1/(A*kap),0]])
JL=s.Matrix([[2*k,a0],[a0,2*k*d*d]])/(A*kap**2)
zero('complete primary residue cross blocks',cross-s.diag(JU,JL))
BL=s.BlockMatrix([[s.zeros(2),JL],[JL,s.zeros(2)]]).as_explicit()
zero('lower residue determinant',BL.det()-1/(A**4*kap**4))
BP=s.BlockMatrix([[s.zeros(4),cross],[cross,s.zeros(4)]]).as_explicit()
zero('whole eight-state residue determinant',BP.det()-1/(A**8*kap**8))

X=s.Matrix([[0,d*d],[1,0]])
H=u*X+v*s.eye(2)
DD=v*v-u*u*d*d
HI=(v*s.eye(2)-u*X)/DD
HII=((v*v+u*u*d*d)*s.eye(2)-2*u*v*X)/DD**2
zero('exact lower determinant',DD+4*A*A*d*d*kap*kap)
zero('all first inverse products',list(H*HI-s.eye(2))+list(HI*H-s.eye(2)))
zero('all second inverse products',list(H*H*HII-s.eye(2))+list(HII*H*H-s.eye(2)))
Theta=2*s.BlockMatrix([[s.zeros(2),H*H],[H,s.zeros(2)]]).as_explicit()
ThetaInv=s.BlockMatrix([[s.zeros(2),HI],[HII,s.zeros(2)]]).as_explicit()/2
zero('full lower inverse products',list(Theta*ThetaInv-s.eye(4))+list(ThetaInv*Theta-s.eye(4)))
zero('lower trace-multiplier determinant',Theta.det()+1024*A**6*d**6*kap**6)
TL=s.diag(s.diag(4,4*d*d),s.Matrix([[4*v,4*u*d*d],[4*u*d*d,4*v*d*d]]))
zero('full residue-to-trace factorization',BL*Theta-TL)
zero('lower trace determinant',TL.det()+1024*A*A*d**6*kap**2)
def trace_poly(f):
    return s.factor(4*f.subs(x,k)+2*f.subs(x,d)+2*f.subs(x,-d))
Tee=s.Matrix([[trace_poly(f*h) for h in pe] for f in pe])
Too=s.Matrix([[trace_poly(hp*f*h) for h in pe] for f in pe])
Tfull=s.diag(Tee,Too)
Tfull_expected=s.diag(4,0,4,4*d*d,0,0,s.Matrix([[4*v,4*u*d*d],[4*u*d*d,4*v*d*d]]))
zero('all eight-state trace entries in exact primary order',Tfull-Tfull_expected)

# The limiting expressions below are polynomial/rational before endpoint
# substitution. No derivative of a moving parameter is discarded.
Kgeneric=(d*d*ThetaInv).applyfunc(s.cancel)
Kendpoint=Kgeneric.subs(d,0).subs({A:-s.Rational(1,2),k:2*i*g}).applyfunc(s.simplify)
N=s.Matrix([[0,0],[1,0]])
K=s.BlockMatrix([[s.zeros(2),N/(4*g*g)],
                 [(s.eye(2)-2*i*N/g)/(16*g**4),s.zeros(2)]]).as_explicit()/2
zero('complete phase-retaining inverse endpoint',Kendpoint-K)
assert K.rank()==3
checks.append({'name':'inverse endpoint rank exactly three','entries':1,'passed':True})
endTheta=Theta.subs({A:-s.Rational(1,2),k:2*i*g,d:0})
zero('complete forward endpoint',endTheta-8*g*g*s.BlockMatrix([[s.zeros(2),s.zeros(2)],[N,s.zeros(2)]]).as_explicit())
zero('signed determinant endpoint',s.cancel(Theta.det()/d**6).subs({A:-s.Rational(1,2),k:2*i*g,d:0})+65536*g**12)
Adj=s.zeros(4);Adj[3,0]=-1/(8192*g**10)
zero('complete rank-three endpoint adjugate',K.adjugate()-Adj)

# Exact original interpolation and both endpoints.
tau=1-z
alpha=p*tau+z*(s.Rational(1,2)+i*g)
beta=2*p*tau/5+z*(s.Rational(1,2)-i*g)
chi=2*p*tau+z*(s.Rational(1,2)-i*g)
SS=2*alpha+beta+chi
mm=(beta+chi)/2
dd=4*p*tau/5
kk=alpha-mm
Az=-1/SS
rr=s.symbols('r')
hz=Az*(rr-alpha)**2*(rr-beta)*(rr-chi)
zero('exact ES reciprocal identity',4/p-1/p-1/(2*p/5)-1/(2*p))
zero('sum and centre',[SS-(22*p*tau/5+2*z),mm-(6*p*tau/5+z*(s.Rational(1,2)-i*g)),kk-(-p*tau/5+2*i*g*z)])
zero('original cubic coefficient',s.Poly(hz,rr).nth(3)-1)
zero('original quartic endpoints',[hz.subs(z,0)+5*(rr-p)**2*(rr-2*p/5)*(rr-2*p)/(22*p),
                                 hz.subs(z,1)+((rr-s.Rational(1,2))**2+g*g)**2/2])
zero('both lower roots with derivative signs',[
    s.diff(hz,rr).subs(rr,beta)-2*Az*(-dd)*(-dd-kk)**2,
    s.diff(hz,rr).subs(rr,chi)-2*Az*dd*(dd-kk)**2])
gE=3*p/22
g1E=s.Rational(1,11)
zero('ES upper cofactor constants',[(Az*(kk*kk-dd*dd)).subs(z,0)-gE,(2*Az*kk).subs(z,0)-g1E])
cscale=s.symbols('cscale',nonzero=True)
# Divide each residue identity by cscale and substitute cscale^2=gE/g0.
g0=A*kap; g1=2*A*k
c2=gE/g0
bracket=2/(3*p)-2*k/kap
zero('full local residue correction on both odd basis vectors',[
    -g1/g0**2-c2*(-g1E/gE**2+bracket/gE),1/g0-c2/gE])
zero('endpoint residue correction',bracket.subs(k,2*i*g).subs(d,0)-(2/(3*p)+i/g))

# Verify the exact original affine receiver for an arbitrary finite signed
# root. This one identity covers all four branches, without choosing a sign.
aa0,yy0,zz0,ww0=s.symbols('a_source y_source z_source w_source')
bb0=i+aa0*yy0;cc0=-i+2*aa0*yy0+aa0**2*zz0
dd0=-i*yy0-aa0*(i*zz0+2*yy0**2)-aa0**2*yy0*zz0
ee0=2*zz0-7*i*yy0**2+aa0*ww0
ff0=i*ww0+3*i*yy0**3-4*yy0*zz0+aa0*(6*i*yy0**2*zz0+ww0*yy0+4*yy0**4)+2*aa0**2*yy0**3*zz0
Poriginal=s.Matrix([aa0*cc0,aa0*ee0+bb0*dd0,aa0*ff0+bb0*ee0,bb0*ff0])
tt,BB=s.symbols('t B')
qoriginal=s.Matrix([1/tt,-rr-i*tt,A*tt**3+2*rr*tt+3*i*tt**2,
                    7*i*rr**2*tt+(BB-17*rr+A*rr**2)*tt**2-13*i*tt**3-2*A*tt**4])
expected_target=s.Matrix([A,BB,tt**2-4*A*rr**3-3*rr**2-2*BB*rr,
                         3*A*rr**4+2*rr**3+BB*rr**2-rr*tt**2])
zero('all original affine branch receiver coordinates',Poriginal.subs(dict(zip([aa0,yy0,zz0,ww0],qoriginal)),simultaneous=True)-expected_target)
zero('full lower endpoint trace',TL.subs({A:-s.Rational(1,2),k:2*i*g,d:0})-s.diag(4,0,0,0))

# A general Hermitian two-dimensional original metric. Positivity means
# ga>0, gd>0, ga*gd-gb^2-gc^2>0; identities hold before imposing it.
ga,gd=s.symbols('ga gd',positive=True)
gb,gc=s.symbols('gb gc',real=True)
G=s.Matrix([[ga,gb+i*gc],[gb-i*gc,gd]])
Ginv=G.inv()
rho2=s.cancel(G[1,1]*Ginv[0,0])
J=s.eye(2)-2*i*N/g
LJ=Ginv*J.H*G*J
zero('general original-metric shear trace',s.trace(LJ)-2-4*rho2/g**2)
zero('general original-metric shear determinant',LJ.det()-1)
zero('general original-metric rank-one square',s.trace(Ginv*N.H*G*N)-rho2)
GG=s.diag(G,G)
pseudodet=s.trace(GG.inv()*Adj.H*GG*Adj)
zero('general original-metric endpoint cubic product',pseudodet-rho2/(2**26*g**20))
zero('complete spectral endpoint determinant constant',pseudodet/(64*g**4*rho2)-1/(65536**2*g**24))
R=s.symbols('R',positive=True)
cN=R/(8*g*g)
cp=(s.sqrt(1+R*R/(g*g))+R/g)/(32*g**4)
cm=(s.sqrt(1+R*R/(g*g))-R/g)/(32*g**4)
zero('explicit two shear constants product',cp*cm-1/(1024*g**8))
zero('explicit two shear constants squared sum',cp*cp+cm*cm-(2+4*R*R/g**2)/(1024*g**8))
zero('explicit three constants and finite endpoint',cN*cp*cm/(8*g*g*R)-1/(65536*g**12))

# Finite-parameter four-value formula checked at an exact interior member
# with a dense complex Hermitian metric, without approximate roots.
fixture={p:s.Integer(5),g:s.Integer(2),z:s.Rational(2,3)}
sub={A:s.simplify(Az.subs(fixture)),k:s.simplify(kk.subs(fixture)),d:s.simplify(dd.subs(fixture))}
Hf=H.subs(sub)
THf=ThetaInv.subs(sub)
Gf=s.Matrix([[5,1+2*i],[1-2*i,7]])
GGf=s.diag(Gf,Gf)
LH=Gf.inv()*Hf.H*Gf*Hf
LH2=Gf.inv()*(Hf*Hf).H*Gf*(Hf*Hf)
aa=s.simplify(s.trace(LH));bb=s.simplify(LH.det())
aa2=s.simplify(s.trace(LH2));bb2=s.simplify(LH2.det())
zero('finite metric determinant invariants',[bb-s.simplify(s.conjugate(Hf.det())*Hf.det()),bb2-bb*bb])
Lin=(GGf.inv()*THf.H*GGf*THf).applyfunc(s.simplify)
lam=s.symbols('lam')
expected=(lam**2-aa*lam/(4*bb)+1/(16*bb))*(lam**2-aa2*lam/(4*bb2)+1/(16*bb2))
zero('all finite inverse spectral polynomial coefficients',s.Poly(Lin.charpoly(lam).as_expr()-expected,lam).all_coeffs())

sources={}
for rel in ['ES_RH_TOTAL_FAMILY_ROOT_BODY.tex','FINITE_COMPLETION_ACCEPTED_BODY.tex',
            'RESIDUE_DUALITY_BODY.tex','independent/ES_RH_TOTAL_FAMILY_REVIEW.md']:
    path=BASE/rel
    if path.exists(): sources[rel]=hashlib.sha256(path.read_bytes()).hexdigest()
report={'status':'PASS','check_groups':len(checks),
        'scalar_entries':sum(c['entries'] for c in checks),
        'checks':checks,'source_sha256':sources,
        'scope':'Exact polynomial, rational, endpoint and complex Hermitian metric identities. Freeness, positivity, interval noncollision and limiting interpretation are proved in the independent review.'}
(HERE/'ES_RH_TOTAL_FAMILY_REVIEW.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','check_groups':len(checks),'scalar_entries':report['scalar_entries']}))
