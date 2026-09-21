"""Exact global residue, both infinity states and weighted original deck map."""
from pathlib import Path
import hashlib,json
import sympy as s
B0=Path(__file__).resolve().parent
A,B,C,D,r=s.symbols('A B C D r')
h=A*r**4+r**3+B*r**2+C*r+D
rem=lambda f:s.rem(f,h,r)
coeff=lambda f:s.Matrix([s.Poly(rem(f),r).nth(j) for j in range(4)])
mul=lambda f:s.Matrix.hstack(*[coeff(f*r**j) for j in range(4)])
lam=lambda f:s.Poly(rem(f),r).nth(3)/A
E=s.Matrix([[1,0,0,0],[0,A,1,B],[0,0,A,1],[0,0,0,A]])
O=s.Matrix([[A,1,B,C],[0,A,1,B],[0,0,A,1],[0,0,0,A]])
T=s.diag(E,O);H=s.Matrix(4,4,lambda i,j:lam(r**(i+j)))
K=s.Matrix([[0,0,0,1],[0,0,A,0],[0,A,1,0],[A,1,B,0]])
Z=s.zeros(4);BG=Z.row_join(K).col_join(K.T.row_join(Z))
checks=[]
def zero(name,value):
    data=list(value) if isinstance(value,s.MatrixBase) else [value]
    reduced=[s.cancel(s.expand(x)) for x in data]
    bad=[x for x in reduced if x!=0]
    if bad:raise ArithmeticError((name,bad[:3]))
    checks.append({'name':name,'entries':len(data),'passed':True})
    print(name+': PASS',flush=True)
zero('Complete global cross pairing',E.T*H*O-K)
zero('Global functional on all odd generators',s.Matrix([[lam(sum(O[k,j]*r**k for k in range(4))) for j in range(4)]])-s.Matrix([[0,0,0,1]]))
zero('Exact determinant A6',BG.det()-A**6)
Ki=s.Matrix([[0,A**-3-B/A**2,-A**-2,A**-1],[0,-A**-2,A**-1,0],[0,A**-1,0,0],[1,0,0,0]])
zero('Full cross inverse',K*Ki-s.eye(4))
zero('Full reverse inverse',Ki*K-s.eye(4))
zero('Boundary adjugate',K.subs(A,0).adjugate()-s.eye(4)[:,0]*s.eye(4)[:,1].T)
E_inv=s.Matrix([[1,0,0,0],[0,1/A,-1/A**2,1/A**3-B/A**2],[0,0,1/A,-1/A**2],[0,0,0,1/A]])
O_inv=s.Matrix([[1/A,-1/A**2,1/A**3-B/A**2,-1/A**4+2*B/A**3-C/A**2],
                [0,1/A,-1/A**2,1/A**3-B/A**2],[0,0,1/A,-1/A**2],[0,0,0,1/A]])
zero('Complete even inverse',E*E_inv-s.eye(4))
zero('Complete odd inverse',O*O_inv-s.eye(4))
g0,w0=s.symbols('g_circ w_circ')
reference={A:-s.Rational(1,2),B:-s.Rational(3,4)-g0+w0,
 C:s.Rational(1,4)+g0-w0,D:-s.Rational(1,32)-(g0-w0)/4-(g0+w0)**2/2}
zero('Full reference quartic',h.subs(reference)+((r-s.Rational(1,2))**4+2*(g0-w0)*(r-s.Rational(1,2))**2+(g0+w0)**2)/2)
ei=E.inv();oi=O.inv()
e=[sum(E[k,j]*r**k for k in range(4)) for j in range(4)]
o=[sum(O[k,j]*r**k for k in range(4)) for j in range(4)]
hp=s.diff(h,r)
def pairmul(x,y):
    fe=sum(x[j]*e[j] for j in range(4));fo=sum(x[4+j]*o[j] for j in range(4))
    ge=sum(y[j]*e[j] for j in range(4));go=sum(y[4+j]*o[j] for j in range(4))
    return (ei*coeff(fe*ge+hp*fo*go)).col_join(oi*coeff(fe*go+fo*ge)).applyfunc(s.cancel)
I=s.eye(8)
# Compute before specializing: the actual global multiplication tensor has no A pole.
products={(i,j):pairmul(I[:,i],I[:,j]) for i in range(8) for j in range(i,8)}
for ij,vec in products.items():
    if any(s.denom(z)!=1 for z in vec):raise ArithmeticError(('Nonpolynomial product',ij))
def pm0(x,y):
    out=s.zeros(8,1)
    for i in range(8):
        for j in range(8):
            out+=x[i]*y[j]*products[tuple(sorted((i,j)))].subs(A,0)
    return out.applyfunc(s.expand)
ep=-I[:,1];op=I[:,4]
inc=(ep+s.I*op)/2;omit=(ep-s.I*op)/2
zero('Infinity unit projector',pm0(ep,ep)-ep)
zero('Infinity odd square',pm0(op,op)+ep)
zero('Included projector',pm0(inc,inc)-inc)
zero('Omitted projector',pm0(omit,omit)-omit)
zero('Both infinity signs disjoint',pm0(inc,omit))
zero('Included sign value',pm0(op,inc)+s.I*inc)
zero('Omitted sign value',pm0(op,omit)-s.I*omit)
zero('Both infinity states in residue radical',BG.subs(A,0)*s.Matrix.hstack(inc,omit))
if BG.subs(A,0).rank()!=6:raise ArithmeticError('Wrong global boundary rank')
M=[s.Matrix.hstack(*[products[tuple(sorted((j,k)))] for k in range(8)]) for j in range(8)]
TR=s.Matrix(8,8,lambda i,j:s.trace(M[i]*M[j])).applyfunc(s.expand)
zero('Original target trace determinant',TR.subs({A:0,B:0,C:-1,D:0}).det()-2**14)
zero('Original target residue rank six',s.Integer(BG.subs({A:0,B:0,C:-1,D:0}).rank()-6))
zero('Global trace cross block',TR[:4,4:])
q=s.symbols('a y z w');a,y,z,w=q
deck=s.Matrix([-a,y+2*s.I/a,-z+6*s.I/a**2,w-14*s.I*y**2/a+28*y/a**2+40*s.I/a**3])
weighted=s.Matrix([-a**4/2,a**3*y/2+s.I*a**2,-a**3*z/2+3*s.I*a,
                   a**3*w/2-7*s.I*a**2*y**2+14*a*y+20*s.I])
zero('Full weighted original deck identity',a**3*deck/2-weighted)
zero('Complete boundary vector',weighted.subs(a,0)-s.Matrix([0,0,0,20*s.I]))
zero('Weighted deck Jacobian determinant',weighted.jacobian(q).det()-a**12/4)
zero('Full weighted boundary Jacobian',weighted.jacobian(q).subs(a,0)-s.Matrix([0,0,3*s.I,14*y])*s.Matrix([[1,0,0,0]]))
# Exact dense complex positive metrics test the dual-transpose convention.
# H^*H plus the identity retains all off-diagonal terms and is positive.
for j in range(1,4):
    He=s.Matrix([[1,j*s.I,0,1],[0,2,1-s.I,0],[1,0,3,j],[0,1,0,2]])
    Ho=s.Matrix([[2,0,j,1+s.I],[s.I,1,0,0],[0,1,2,1],[j,0,0,3]])
    Ge=He.conjugate().T*He+s.eye(4)
    Go=Ho.conjugate().T*Ho+s.eye(4)
    Cb=K.subs({A:0,B:s.Rational(j,3)})
    L=Go.inv()*Cb.conjugate().T*Ge.inv().T*Cb
    cp=L.charpoly().all_coeffs()
    zero(f'Dense complex metric {j}: positive cubic product',-cp[3]-Go[0,0]*Ge[1,1]/(Ge.det()*Go.det()))
    zero(f'Dense complex metric {j}: one zero eigenvalue',cp[4])
    zero(f'Dense complex metric {j}: cubic trace',cp[1]+s.trace(L))
    zero(f'Dense complex metric {j}: second elementary coefficient',cp[2]-(s.trace(L)**2-s.trace(L*L))/2)
record={'checks':checks,'groups':len(checks),'entries':sum(x['entries'] for x in checks),
        'global_cross_gram':s.latex(K),'global_boundary_rank':6,
        'original_target_trace_gram':[[str(v) for v in row] for row in TR.subs({A:0,B:0,C:-1,D:0}).tolist()],
        'source_sha256':hashlib.sha256((B0/'GLOBAL_RESIDUE_DUALITY_BODY.tex').read_bytes()).hexdigest()
        if (B0/'GLOBAL_RESIDUE_DUALITY_BODY.tex').exists() else None}
(B0/'GLOBAL_RESIDUE_DUALITY_CERTIFICATE.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))
