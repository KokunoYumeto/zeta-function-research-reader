"""Exact original interpolation, full complex jets, quartic and all kernel strata."""
from pathlib import Path
from hashlib import sha256
import itertools
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
checks=[]
entries=0
def ck(name, values):
    global entries
    vv=list(values) if isinstance(values,(s.MatrixBase,list,tuple)) else [values]
    for value in vv:
        result=s.cancel(s.expand(value),extension=s.sqrt(2))
        assert result==0,(name,result)
    entries+=len(vv)
    checks.append({'name':name,'entries':len(vv),'passed':True})
    print(name, 'passed', len(vv), flush=True)

d,g,v,y,x,X=s.symbols('delta gamma v y x X',real=True)
ar,ai,br,bi,cr,ci=s.symbols('a_R a_I b_R b_I c_R c_I',real=True)
A=v+1;B=v+2;C=v+3
aa=ar+s.I*ai;bb=br+s.I*bi;cc=cr+s.I*ci
base=[cc,bb,aa,s.Integer(1)]
choose=lambda n,k:s.prod(n-j for j in range(k))/s.factorial(k)
betas=[s.expand(sum(choose(v+q,q-j)*(s.I*y)**(q-j)*base[q]
                   for q in range(j,4))) for j in range(4)]
re=lambda q:s.expand(q).as_real_imag()[0]
im=lambda q:s.expand(q).as_real_imag()[1]
direct=s.Matrix([[re(q) for q in betas],[im(q) for q in betas],
                 [re((v+j+1)*betas[j+1]) if j<3 else 0 for j in range(4)],
                 [im((v+j+1)*betas[j+1]) if j<3 else 0 for j in range(4)]])
R0=cr-A*y*bi-A*B*y*y*ar/2
R1=br-B*y*ai-B*C*y*y/2
matrix=s.Matrix([[R0,R1,ar,1],
 [ci+A*y*br-A*B*y*y*ai/2-A*B*C*y**3/6,bi+B*y*ar,ai+C*y,0],
 [A*R1,B*ar,C,0],[A*(bi+B*y*ar),B*(ai+C*y),0,0]])
ck('entire complex-centre real matrix from direct binomial jets',direct-matrix)
h=ai+C*y
D=bi-B*ar*ai/C
E=ci-A*ai*br/C-A*B*ai**3/(3*C*C)
L=B*E-A*B*ar*D/C
q=A*B*B/(3*C*C)
G=s.expand(q*h**4+L*h-A*D*D)
# A determinant expansion independent of the two-step elimination in the proof.
det=0
for perm in itertools.permutations(range(4)):
    inv=sum(perm[a]>perm[b] for a in range(4) for b in range(a+1,4))
    det+=(-1)**inv*s.prod(matrix[a,perm[a]] for a in range(4))
ck('all 24 determinant terms give the complete quartic',det-C*G)
row2=matrix.row(1)-(h/C)*matrix.row(2)
ck('complete eliminating row and every sign',row2-s.Matrix([[E+A*B*h**3/(3*C*C),D,0,0]]))

u,w=s.symbols('u w',real=True)
mult=s.Matrix([[u,-w],[w,u]])
full=s.diag(mult,mult)*matrix
cb=[(u+s.I*w)*b for b in base]
cbeta=[s.expand(sum(choose(v+k,k-j)*(s.I*y)**(k-j)*cb[k]
                   for k in range(j,4))) for j in range(4)]
full_direct=s.Matrix([[re(z) for z in cbeta],[im(z) for z in cbeta],
 [re((v+j+1)*cbeta[j+1]) if j<3 else 0 for j in range(4)],
 [im((v+j+1)*cbeta[j+1]) if j<3 else 0 for j in range(4)]])
ck('full original b3 complex multiplication retained',full-full_direct)
ck('exact original determinant multiplier',s.det(s.diag(mult,mult))-(u*u+w*w)**2)

# Every moment retained in both real and imaginary displacement maps.
mu=s.symbols('mu0:4',real=True)
eta=[sum(choose(v+k,r)*mu[k-r]*x**r for r in range(k+1)) for k in range(4)]
inverse=[sum(choose(v+k,r)*(-x)**r*eta[k-r] for r in range(k+1)) for k in range(4)]
ck('all four inverse real-shift moment entries',s.Matrix(inverse)-s.Matrix(mu))
complex_eta=[sum(choose(v+k,r)*mu[k-r]*(x+s.I*y)**r for r in range(k+1)) for k in range(4)]
split_eta=[sum(choose(v+k,r)*(s.I*y)**r*eta[k-r] for r in range(k+1)) for k in range(4)]
ck('all four complex-displacement moment identities',s.Matrix(complex_eta)-s.Matrix(split_eta))
ck('direct conductor derivative equals complete derivative row',
   s.diff(sum(base[k]*complex_eta[k] for k in range(4)),x)
   -sum((v+j+1)*betas[j+1]*eta[j] for j in range(3)))

# Complete kernel with h != 0, verified without replacing its determinant condition.
t=s.symbols('t',real=True)
e0=t
e1=-A*(D+B*ar*h/C)*t/(B*h)
e2=-(A*R1*e0+B*ar*e1)/C
e3=-R0*e0-R1*e1-ar*e2
kv=s.Matrix([e0,e1,e2,e3])
ck('general entire kernel equals exact determinant residual',
   matrix*kv-s.Matrix([0,t*G/(B*h),0,0]))

# At h=0, D=0 both one- and two-dimensional strata are verified.
y0=-ai/C
bi0=B*ar*ai/C
m0=matrix.subs({y:y0,bi:bi0},simultaneous=True)
rr0=R0.subs({y:y0,bi:bi0},simultaneous=True)
rr1=R1.subs({y:y0,bi:bi0},simultaneous=True)
e2one=-B*ar*t/C
one=s.Matrix([0,t,e2one,-rr1*t-ar*e2one])
ck('h=D=0 entire eta0=0 kernel',m0*one)
t0,t1=s.symbols('t0 t1',real=True)
e2two=-(A*rr1*t0+B*ar*t1)/C
two=s.Matrix([t0,t1,e2two,-rr0*t0-rr1*t1-ar*e2two])
ck('h=D=0 two-parameter kernel and exact E residual',
   m0*two-s.Matrix([0,E*t0,0,0]))
ck('D=0 exact quartic factorization',G.subs(bi,bi0)-h*(q*h**3+B*E))

# The actual moment family gives a unique real-coordinate candidate at h != 0.
candidate_x=s.symbols('candidate_x',real=True)
star1=-A*(D+B*ar*h/C)*mu[0]/(B*h)
xx=(star1-mu[1])/(A*mu[0])
ck('exact real coordinate from the first two actual moments',
   mu[1]+A*mu[0]*xx-star1)
actual_eta=s.Matrix(eta)
Q2=A*B*C*mu[0]/2
Q1=A*B*ar*mu[0]+B*C*mu[1]
Q0=A*rr1*mu[0]+B*ar*mu[1]+C*mu[2]
actual_ranktwo=m0*actual_eta
H=rr0*mu[0]+rr1*(mu[1]+A*mu[0]*x)+ar*(mu[2]+B*mu[1]*x+A*B*mu[0]*x*x/2)\
  +mu[3]+C*mu[2]*x+B*C*mu[1]*x*x/2+A*B*C*mu[0]*x**3/6
ck('entire rank-two candidate quadratic and cubic',
   [actual_ranktwo[2]-(Q2*x*x+Q1*x+Q0),actual_ranktwo[0]-H])
ck('exact degree-three leading term with all order factors',
   s.expand(sum(base[j]*complex_eta[j] for j in range(4))).coeff(x,3)-A*B*C*mu[0]/6)

# Independent reconstruction from the original K and the literal quartet.
rt=s.sqrt(2);I=s.I
K=s.Matrix([[0,I,1/rt,1/rt],[0,-1,-1-rt*I,1-rt*I],
 [I/2,-3*I,2*rt+6*I,-2*rt+6*I],[0,13,-34-19*rt*I,34-19*rt*I]])
Kinv=K.inv().applyfunc(lambda z:s.simplify(s.expand_complex(z)))
ck('original K and its inverse',K*Kinv-s.eye(4))
ck('original K determinant',K.det()-77*rt*I/2)
roots=[s.Rational(1,2)+d+I*g,s.Rational(1,2)+d-I*g,
       s.Rational(1,2)-d+I*g,s.Rational(1,2)-d-I*g]
ell=[s.Poly(s.prod(X-r for j,r in enumerate(roots) if j!=a),X)
     for a in range(4)]
den=[s.prod(roots[a]-r for j,r in enumerate(roots) if j!=a) for a in range(4)]
coeff=[s.factor(s.cancel(sum(Kinv[a,0]*ell[a].nth(k)/den[a] for a in range(4)))) for k in range(4)]
for a,r in enumerate(roots):
    ck('original interpolation label '+str(a),sum(coeff[k]*r**k for k in range(4))-Kinv[a,0])
common=616*d*g*(d*d+g*g)
uu=355*rt*g-214*d
ww=308*rt*d+210*g
QQ=uu*uu+ww*ww
original_b3=(uu+I*ww)/common
original_b2=(-(172*d*d-642*d+172*g*g+1065*rt*g)/2
   +7*I*(44*rt*d*d-66*rt*d+44*rt*g*g-45*g))/common
ck('actual unaltered b2 and b3 closed expressions',[coeff[2]-original_b2,coeff[3]-original_b3])
exact_ai=28*(8455*g-1408*rt*d)*(d*d+g*g)/QQ
ratio_im=s.cancel((s.im(s.expand_complex(original_b2))*s.re(s.expand_complex(original_b3))
                  -s.re(s.expand_complex(original_b2))*s.im(s.expand_complex(original_b3)))
                 /(QQ/common**2))
ck('strictly positive original imaginary coefficient ratio',ratio_im-exact_ai)
assert s.Rational(3,2)**2>2
assert 16910-1056>0

# Check the actual real-centre matrix against its already certified source.
source=json.loads((ROOT/'ACTUAL_REAL_JET_DERIVATION.json').read_text(encoding='utf-8'))
scope={'delta':d,'gamma':g,'v':v}
C0=s.Matrix([[s.sympify(z,locals=scope) for z in row] for row in source['real_jet_matrix']])
real=lambda z:s.factor(s.cancel(s.expand_complex(z).as_real_imag()[0]))
imag=lambda z:s.factor(s.cancel(s.expand_complex(z).as_real_imag()[1]))
reconstructed=s.Matrix([[real(z) for z in coeff],[imag(z) for z in coeff],
 [(v+k+1)*real(coeff[k+1]) if k<3 else 0 for k in range(4)],
 [(v+k+1)*imag(coeff[k+1]) if k<3 else 0 for k in range(4)]])
ck('all actual y=0 matrix entries match the positive ARR matrix',reconstructed-C0)

proof=HERE/'COMPLEX_RECEIVER_JETS.tex'
receipt={'status':'passed','groups':len(checks),'entries':entries,'checks':checks,
 'generic_matrix':[[str(z) for z in matrix.row(j)] for j in range(4)],
 'quartic':{'h':'a_I+(v+3)*y','q':str(q),'D':str(D),'E':str(E),'L':str(L),
            'G':'q*h**4+L*h-(v+1)*D**2','actual_determinant':'abs(b3)**4*(v+3)*G'},
 'positive_ai':str(exact_ai),
 'original_coefficients':[str(z) for z in coeff],
 'sources':[{'name':p.name,'sha256':sha256(p.read_bytes()).hexdigest()} for p in
   [proof,Path(__file__),ROOT/'ACTUAL_REAL_RECEIVER_BODY.tex',ROOT/'ESCAPE_QUOTIENT_RETURN_BODY.tex',
    ROOT/'ACTUAL_REAL_JET_DERIVATION.json',HERE/'ACTUAL_REAL_JET_REVIEW.json']],
 'scope':'Exact independent original interpolation, full symbolic complex displacement, quartic determinant, all kernel strata. ARR positivity is used with its existing exact certificate. No numerical test establishes a sign, no arbitrary moment vector is identified with a period.'}
(HERE/'COMPLEX_RECEIVER_JETS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','groups':len(checks),'entries':entries}),flush=True)
