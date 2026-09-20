"""Exact boundary/current diagnostics. Fixtures do not assert native period data."""
from pathlib import Path
import json
import sympy as s

ROOT=Path(__file__).parent
count=0
controls=0
def require(value,label):
    global count
    count+=1
    if value != True: raise ArithmeticError(label+': '+str(value))
def zero(value,label):
    if isinstance(value,s.MatrixBase): value=all(s.cancel(x)==0 for x in value)
    else: value=s.cancel(value)==0
    require(value,label)
def reject(value,label):
    global controls
    controls+=1
    if value != False: raise ArithmeticError('negative control: '+label)

# Closed root sums, all labels, and complete multiplicities.
for k in range(1,30,2):
    for e in [1,2,5]:
        total=e*(k+1)*sum(2*(2*a-k) for a in range((k+1)//2,k+1))
        require(total==e*(k+1)**3//2,'full positive root sum')
        if k>=9:
            for a in range(k+1):
                d=abs(2*a-k)
                require(d*(e*(k+1)**3-4*d)>0,'every actual label residual lower bound')

# A declared four-root finite fixture on the original S=c+i y line.
# The probability Gaussian is multiplied by 7: the source mass is retained.
S=s.symbols('S'); c=s.Rational(1,2); delta=s.Rational(1,4); gamma=3
roots=[c+(2*a-1)*delta+s.I*(2*b-1)*gamma for a in range(2) for b in range(2)]
chi=s.Poly(s.prod(S-z for z in roots),S); q=chi.degree()
A=s.zeros(q)
for j in range(q-1):A[j+1,j]=1
for j in range(q):A[j,q-1]=-chi.nth(j)
def moment(j):
    if j%2:return s.Integer(0)
    return 7*(s.factorial2(j-1) if j else s.Integer(1))
def gram(N):
    return s.Matrix(N+1,N+1,lambda m,n:sum(
        s.binomial(m,r)*s.binomial(n,t)*c**(m+n-r-t)*(-s.I)**r*s.I**t*moment(r+t)
        for r in range(m+1) for t in range(n+1)))
vectors=[]
for lam in roots:
    quot=s.div(chi,s.Poly(S-lam,S))[0].as_expr()/chi.diff().eval(lam)
    vectors.append(s.Matrix([s.expand(quot).coeff(S,j) for j in range(q)]))

for N in [q-1,q,2*q-1,2*q]:
    Hplus=gram(N+1); H=Hplus[:N+1,:N+1]
    E=s.eye(N+1)[:,:q]
    W=s.Matrix(N+1,N-q+1,lambda row,col:chi.nth(row-col)) if N>=q else s.zeros(N+1,0)
    T=E-W*(W.H*H*W).inv()*W.H*H*E if W.cols else E
    G=s.simplify(T.H*H*T); Ginv=G.inv(); ell=T[N:N+1,:]
    b=s.Matrix([chi.nth(j-(N+1-q)) for j in range(N+2)])
    TT=T.col_join(s.zeros(1,q)); xi=TT.H*Hplus*b
    D=A.H*G+G*A-G
    zero(D+xi*ell+ell.H*xi.H,'full original source boundary')
    B=Ginv*D; kap2=s.cancel(s.trace(B*B)/2)
    require(D.rank()==2,'rank exactly two')
    zero(s.trace(B),'full trace cancellation')
    zero(B**3-kap2*B,'boundary cubic identity')
    Pb=B*B/kap2
    zero(Pb*Pb-Pb,'boundary support projection')
    require(kap2>=(4*delta)**2,'whole positive half trace bound')
    Ip=s.Matrix.hstack(*[vectors[j] for j in range(q) if s.re(roots[j])>c])
    Pp=Ip*(Ip.H*G*Ip).inv()*Ip.H*G
    zero(s.trace(Pp*B)-4*delta,'positive-half invariant trace')
    I=s.eye(q)[:,:2]; P=I*(I.H*G*I).inv()*I.H*G
    for lam,v in zip(roots,vectors):
        Evalue=s.cancel((v.H*G*v)[0]); bv=2*s.re(lam)-1
        rr=Ginv*A.H*G*v-s.conjugate(lam)*v
        rn=s.cancel((rr.H*G*rr)[0]/Evalue)
        eta=s.cancel((v.H*G*Pb*v)[0]/Evalue)
        zero(rn-kap2*eta+bv**2,'exact eigenclass residual')
        require(rn>=abs(bv)*(4*delta-abs(bv)),'finite residual lower bound')
        zero((rr.H*G*v)[0],'adjoint residual perpendicular')
        p=P*v; theta=s.cancel((p.H*G*p)[0]/Evalue)
        z=(p.H*G*A*(v-p))[0]; w=((v-p).H*G*A*p)[0]
        cross=(v.H*D*p)[0]/Evalue-bv*theta
        phase=s.cancel(s.re(s.conjugate(z)*w))
        mid=s.cancel(abs((z+w)/2)**2)
        zero(phase-mid+Evalue**2*abs(cross)**2/4,'native-coordinate phase receiver')
        rowcross=(-(v.H*xi)[0]*(ell*p)[0]-s.conjugate((ell*v)[0])*(xi.H*p)[0])/Evalue-bv*theta
        zero(rowcross-cross,'two original boundary rows')
        require(phase>=-Evalue**2*rn*theta*(1-theta)/4,'fixed-projection negative bound')

# Exact construction from the supplied all-projections criterion.
# A has eigenvector x=e1; this is a separate declared matrix diagnostic.
AA=s.Matrix([[2,-4],[0,-1]]); x=s.Matrix([1,0]); u=s.Matrix([0,1])
t=s.Rational(1,5); g=3; eps=4
P=s.Matrix([[t,s.Rational(2,5)],[s.Rational(2,5),1-t]])
z=((P*x).H*AA*(x-P*x))[0]; w=((x-P*x).H*AA*P*x)[0]
zero(P*P-P,'constructed projection')
zero(z+w,'vanishing phase midpoint')
zero(s.re(s.conjugate(z)*w)+s.Rational(eps**4,16*(g*g+eps*eps)),'evaluated negative phase')
reject(s.re(s.conjugate(z)*w)>=0,'all projections nonnegative for nonreducing eigenline')
reject(s.Rational(1,4)*10**3/2 == 2*9*s.Rational(1,4),'single extreme root equals full trace bound')
reject(s.Rational(1,4)**2*9*(10**3-4*9)<=0,'terminal residual can vanish')
receipt={'status':'PASS','exact_checks':count,'negative_controls':controls,
 'scope':'Exact closed root sums and finite scalar-source boundary/current identities. Four-root Gaussian fixture is outside the native k>=9 period domain and is explicitly auxiliary. No actual xi moments or period coefficients evaluated.'}
(ROOT/'NATIVE_BOUNDARY_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
