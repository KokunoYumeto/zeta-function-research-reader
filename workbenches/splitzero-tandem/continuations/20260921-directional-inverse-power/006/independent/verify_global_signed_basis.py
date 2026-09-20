"""Exact global signed-basis tensor, chart maps and trace certificates."""
from pathlib import Path
import hashlib
import json
from itertools import permutations
import sympy as s
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

HERE=Path(__file__).resolve().parent
A,B,C,D,r,p=s.symbols('A B C D r p')
h=A*r**4+r**3+B*r**2+C*r+D
de=s.diff(h,r)
ep=[s.Integer(1),A*r,A*r*r+r,A*r**3+r*r+B*r]
qp=[A,A*r+1,A*r*r+r+B,A*r**3+r*r+B*r+C]
E=s.Matrix(4,4,lambda i,j:s.expand(ep[j]).coeff(r,i))
Q=s.Matrix(4,4,lambda i,j:s.expand(qp[j]).coeff(r,i))
Ei=E.inv(); Qi=Q.inv()
checks=[]
PR,*unused_generators=ring('A,B,C,D,p',QQ)
def polynomial_determinant(M):
    n=M.rows
    PM=[[PR.from_expr(M[i,j]) for j in range(n)] for i in range(n)]
    total=PR.zero
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=PR.one
        for i in range(n):term*=PM[i][perm[i]]
        total+=(-1 if inversions%2 else 1)*term
    return total.as_expr()
def check(name,expr):
    if isinstance(expr,s.MatrixBase): ok=all(s.cancel(z)==0 for z in expr)
    else: ok=s.cancel(expr)==0
    assert ok,(name,expr)
    checks.append(name)
def remvec(poly):
    v=s.rem(s.expand(poly),h,r)
    return s.Matrix([s.expand(v).coeff(r,i) for i in range(4)])
tensor=[[[s.Integer(0) for k in range(8)] for j in range(8)] for i in range(8)]
for i in range(8):
    for j in range(i,8):
        if i<4 and j<4:
            coeff=(Ei*remvec(ep[i]*ep[j])).applyfunc(s.cancel)
            full=list(coeff)+[s.Integer(0)]*4
        elif i<4<=j:
            coeff=(Qi*remvec(ep[i]*qp[j-4])).applyfunc(s.cancel)
            full=[s.Integer(0)]*4+list(coeff)
        else:
            coeff=(Ei*remvec(de*qp[i-4]*qp[j-4])).applyfunc(s.cancel)
            full=list(coeff)+[s.Integer(0)]*4
        for f in full:
            assert s.denom(f)==1, (i,j,f)
        tensor[i][j]=full
        tensor[j][i]=full
matrices=[s.Matrix(8,8,lambda k,j:tensor[i][j][k]) for i in range(8)]
check('Multiplicative unit',matrices[0]-s.eye(8))
for i in range(8):
    for j in range(i,8):
        check(f'Associativity via multiplication operators {i},{j}',
              matrices[i]*matrices[j]-sum((tensor[i][j][k]*matrices[k] for k in range(8)),s.zeros(8)))
print('Full multiplication tensor and associativity checked.',flush=True)
T=s.Matrix(8,8,lambda i,j:s.trace(matrices[i]*matrices[j])).applyfunc(s.expand)
disc=s.discriminant(h,r)
check('Even trace determinant',polynomial_determinant(T[:4,:4])-16*disc)
check('Odd trace determinant',polynomial_determinant(T[4:,4:])-16*disc**2)
print('Both full trace determinants checked.',flush=True)
check('Mixed trace block',T[:4,4:])
check('Finite even determinant',E.det()-A**3)
check('Finite odd determinant',Q.det()-A**4)

aa=h.subs(r,p); bb=-s.diff(h,r).subs(r,p)
cc=s.diff(h,r,2).subs(r,p)/2
dd=-s.diff(h,r,3).subs(r,p)/6
RR=s.symbols('R')
hp=s.expand(RR**4*h.subs(r,p-1/RR))
k1=A*p+dd
k2=A*p*p+p-cc-2*p*dd
k3=A*p**3+p*p+B*p+bb+p*cc+p*p*dd
Ep=s.Matrix([[1,k1,k2,k3],
             [0,cc,-bb-2*p*cc,aa+p*bb+p*p*cc],
             [0,bb,-aa-2*p*bb,p*aa+p*p*bb],
             [0,aa,-2*p*aa,p*p*aa]])
Qp=s.Matrix([[-dd,cc+3*p*dd,-bb-2*p*cc-3*p*p*dd,aa+p*bb+p*p*cc+p**3*dd],
             [-cc,bb+3*p*cc,-aa-2*p*bb-3*p*p*cc,p*aa+p*p*bb+p**3*cc],
             [-bb,aa+3*p*bb,-2*p*aa-3*p*p*bb,p*p*aa+p**3*bb],
             [-aa,3*p*aa,-3*p*p*aa,p**3*aa]])
check('Chart polynomial coefficients',hp-(aa*RR**4+bb*RR**3+cc*RR**2+dd*RR+A))
check('Chart even determinant',polynomial_determinant(Ep)-aa**3)
check('Chart odd determinant',polynomial_determinant(Qp)-aa**4)
print('Both generic chart determinants checked.',flush=True)
I4=s.eye(4)
q1=3*A*p+1
q2=3*A*p*p+2*p+B
q3=A*p**3+p*p+B*p+C
ev0=I4[:,0]
ev1=(q3*I4[:,0]+p*p*I4[:,1]+p*I4[:,2]+I4[:,3])/aa
ev2=-(q2*I4[:,0]+2*p*I4[:,1]+I4[:,2]+bb*ev1)/aa
ev3=(q1*I4[:,0]+I4[:,1]-cc*ev1-bb*ev2)/aa
Epinv=s.Matrix.hstack(ev0,ev1,ev2,ev3)
ov0=(p**3*I4[:,0]+p*p*I4[:,1]+p*I4[:,2]+I4[:,3])/aa
ov1=-(3*p*p*I4[:,0]+2*p*I4[:,1]+I4[:,2]+bb*ov0)/aa
ov2=(3*p*I4[:,0]+I4[:,1]-cc*ov0-bb*ov1)/aa
ov3=-(I4[:,0]+dd*ov0+cc*ov1+bb*ov2)/aa
# Check the full inverse identities in the exact polynomial ring after
# multiplying by the stated common denominators. This avoids symbolic
# expression swell from nested quotients, without omitting any coefficient.
ap,bp,cp,dp=[PR.from_expr(s.expand(v)) for v in (aa,bb,cc,dd)]
qq1,qq2,qq3,pp=[PR.from_expr(v) for v in (q1,q2,q3,p)]
vv=[[PR.one if i==j else PR.zero for i in range(4)] for j in range(4)]
add=lambda x,y:[a+b for a,b in zip(x,y)]
scale=lambda c,x:[c*a for a in x]
en1=add(add(scale(qq3,vv[0]),scale(pp**2,vv[1])),add(scale(pp,vv[2]),vv[3]))
en2=scale(-1,add(scale(ap,add(add(scale(qq2,vv[0]),scale(2*pp,vv[1])),vv[2])),scale(bp,en1)))
en3=add(scale(ap**2,add(scale(qq1,vv[0]),vv[1])),scale(-1,add(scale(cp*ap,en1),scale(bp,en2))))
on0=add(add(scale(pp**3,vv[0]),scale(pp**2,vv[1])),add(scale(pp,vv[2]),vv[3]))
on1=scale(-1,add(scale(ap,add(add(scale(3*pp**2,vv[0]),scale(2*pp,vv[1])),vv[2])),scale(bp,on0)))
on2=add(scale(ap**2,add(scale(3*pp,vv[0]),vv[1])),scale(-1,add(scale(cp*ap,on0),scale(bp,on1))))
on3=scale(-1,add(add(scale(ap**3,vv[0]),scale(dp*ap**2,on0)),add(scale(cp*ap,on1),scale(bp,on2))))
def ring_matrix(M):return [[PR.from_expr(s.expand(M[i,j])) for j in range(4)] for i in range(4)]
def from_columns(cols):return [[cols[j][i] for j in range(4)] for i in range(4)]
def ring_product(X,Y):return [[sum((X[i][k]*Y[k][j] for k in range(4)),PR.zero) for j in range(4)] for i in range(4)]
for name,forward,numer,denom in [
 ('even',ring_matrix(Ep),from_columns([scale(ap**3,vv[0]),scale(ap**2,en1),scale(ap,en2),en3]),ap**3),
 ('odd',ring_matrix(Qp),from_columns([scale(ap**3,on0),scale(ap**2,on1),scale(ap,on2),on3]),ap**4)]:
    for side,X0,Y0 in [('left',numer,forward),('right',forward,numer)]:
        product=ring_product(X0,Y0)
        assert all(product[i][j]==(denom if i==j else PR.zero) for i in range(4) for j in range(4)),(name,side)
        checks.append(f'Chart {name} inverse {side}')
print('All four chart inverse products checked.',flush=True)
# Multiply the rational chart identities by powers of R, then reduce
# modulo h_p. This checks all entries without discarding R=0.
chart_domain=QQ.frac_field(A,B,C,D,p)
chart_poly=s.Poly(hp,RR,domain=chart_domain)
for j in range(4):
    eforward=sum(Ep[i,j]*RR**i for i in range(4))
    oforward=sum(Qp[i,j]*RR**i for i in range(4))
    erational=ep[j].subs(r,p-1/RR)
    orational=qp[j].subs(r,p-1/RR)/RR
    check(f'Even chart coordinate identity {j}',s.Poly(s.expand(RR**3*(eforward-erational)),RR,domain=chart_domain).rem(chart_poly).as_expr())
    check(f'Odd chart coordinate identity {j}',s.Poly(s.expand(RR**4*(oforward-orational)),RR,domain=chart_domain).rem(chart_poly).as_expr())
check('Five-open cover',h.subs(r,0)/2-h.subs(r,1)/2-h.subs(r,-1)/6+h.subs(r,2)/6-2*A-1)
print('Every chart determinant, inverse and coordinate identity checked.',flush=True)

original={A:0,B:0,C:-1,D:0,p:2}
Eoriginal=Ep.subs(original)
Qoriginal=Qp.subs(original)
Toriginal=T.subs({A:0,B:0,C:-1,D:0})
check('Original even determinant',Eoriginal.det()-6**3)
check('Original odd determinant',Qoriginal.det()-6**4)
check('Original full trace determinant',Toriginal.det()-2**14)
assert Toriginal.rank()==8
checks.append('Original full trace rank eight')

def matlist(m):return [[str(s.expand(m[i,j])) for j in range(m.cols)] for i in range(m.rows)]
labels=['e0','e1','e2','e3','o0','o1','o2','o3']
record={'result':'PASS','exact_check_count':len(checks),'checks':checks,
        'basis':labels,'coefficient_variables':['A','B','C','D'],
        'discriminant':str(s.expand(disc)),
        'multiplication_tensor':[[[str(s.expand(f)) for f in tensor[i][j]] for j in range(8)] for i in range(8)],
        'multiplication_matrices':{labels[i]:matlist(matrices[i]) for i in range(8)},
        'trace_even':matlist(T[:4,:4]),'trace_odd':matlist(T[4:,4:]),
        'chart_even_at_original_target_p2':matlist(Eoriginal),
        'chart_odd_at_original_target_p2':matlist(Qoriginal),
        'trace_at_original_target':matlist(Toriginal)}
src=HERE/'GLOBAL_SIGNED_BASIS_INDEPENDENT.tex'
if src.exists():record['source_sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
(HERE/'GLOBAL_SIGNED_BASIS_EXACT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')

def expression(coeff):
    z=s.symbols('e_0 e_1 e_2 e_3 o_0 o_1 o_2 o_3')
    return s.latex(s.Add(*[coeff[i]*z[i] for i in range(8) if coeff[i]!=0]))
tex=[]
tex.append(r'\subsection{Every multiplication coefficient}')
tex.append('The following table gives every product other than multiplication by $e_0=1$.')
tex.append('Commutativity gives the entries below the diagonal; each right-hand side is in the unchanged eight-section basis.')
for category,tag,pairs in [
    ('Even products','GB13',[(i,j) for i in range(1,4) for j in range(i,4)]),
    ('Even--odd products','GB14',[(i,j) for i in range(1,4) for j in range(4,8)]),
    ('Odd products','GB15',[(i,j) for i in range(4,8) for j in range(i,8)])]:
    tex.append(r'\paragraph{'+category+'}')
    tex.append(r'\begin{align}')
    for n,(i,j) in enumerate(pairs):
        tex.append(labels[i][0]+'_'+labels[i][1]+' '+labels[j][0]+'_'+labels[j][1]+' &='+expression(tensor[i][j])+r'\tag{'+tag+chr(97+n)+'}'+(r'\\' if n<len(pairs)-1 else ''))
    tex.append(r'\end{align}')
tex.append(r'\subsection{The complete trace blocks}')
tex.append(r'\begin{equation}T_{ee}='+s.latex(T[:4,:4])+r',\qquad T_{eo}=0.\tag{GB16}\end{equation}')
tex.append(r'The symmetric odd block has the following ten entries; $T_{ji}=T_{ij}$ supplies the other six.')
tex.append(r'\begin{align}')
for n,(i,j) in enumerate([(i,j) for i in range(4) for j in range(i,4)]):
    tex.append(r'(T_{oo})_{'+str(i)+str(j)+'}&='+s.latex(T[i+4,j+4])+r'\tag{GB17'+chr(97+n)+'}'+(r'\\' if n<9 else ''))
tex.append(r'\end{align}')
(HERE/'GLOBAL_SIGNED_BASIS_TABLES.tex').write_text('\n'.join(tex)+'\n',encoding='utf-8')
print(json.dumps({'result':'PASS','checks':len(checks),'trace_even':matlist(T[:4,:4]),'original_even':matlist(Eoriginal),'original_odd':matlist(Qoriginal)},indent=2))
