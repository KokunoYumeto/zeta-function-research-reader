"""Rebuild actual period jets and verify characteristic-zero and finite-field certificates."""
from pathlib import Path
import hashlib
import json
import sympy as s
from sympy.polys.rings import ring
from sympy.polys.matrices import DomainMatrix
HERE=Path(__file__).resolve().parent
x,y,q=s.symbols('x y q');rt=s.sqrt(5);phi=1+q+q**2+q**3+q**4
K=s.QQ.algebraic_field(rt);prime=101
source=json.loads((HERE/'ARBITRARY_UNIT_COEFFICIENT_DERIVATION.json').read_text(encoding='utf-8'))
cert=json.loads((HERE/'ARBITRARY_UNIT_MOD101_CERTIFICATE.json').read_text(encoding='utf-8'))
elim=json.loads((HERE/'ARBITRARY_UNIT_NONCONSTANCY_ELIMINATION.json').read_text(encoding='utf-8'))
checks=[]

def test(name,ok,entries=1):
    assert ok,name
    checks.append({'name':name,'entries':entries})

def red(v):return s.rem(s.expand(v),phi,q)

def Rn(n):
    out=s.zeros(4)
    for a in range(1,5):
        for r in range(4):
            total=5*n+r+1-a
            for h in range(max(-1,total//4)+1):
                if (total-4*h)%2:continue
                p=(total-4*h)//2;L=p+h-n
                assert L>=0
                out[a-1,r]+=x**h/(3**p*s.factorial(p)*s.factorial(h))*(-1)**L*5**L*s.rf(s.Rational(a,5),L)
    return out

R=[Rn(n) for n in range(5)];Ri=[R[0].inv()]
for n in range(1,5):Ri.append(s.expand(-Ri[0]*sum((R[a]*Ri[n-a] for a in range(1,n+1)),s.zeros(4))))
D=s.diag(q,q**2,q**3,q**4)
G=[sum((Ri[a]*D*R[n-a] for a in range(n+1)),s.zeros(4)).applyfunc(red) for n in range(5)]
T=s.Matrix([[0,0,0,-x],[1,0,0,0],[0,1,0,-1],[0,0,1,0]])
Q=s.Matrix([[0,0,1,0],[0,-1,0,1],[1,0,-1,0],[0,1,0,x-1]])
W=y*s.eye(4)+T**2;Wbar=(y-1)*s.eye(4)-T**2;e0=s.eye(4)[:,0]
v=[(Wbar*gn*W*e0).applyfunc(red) for gn in G]
H={}
for n in [2,4]:
    actual=red(sum((v[a].dot(Q*v[n-a]) for a in range(n+1)),s.S.Zero))
    saved=s.sympify(source['polynomials'][str(n)],locals={'x':x,'y':y,'q':q})
    test(f'full original-derived coefficient {n}',s.expand(actual-saved)==0)
    table=sum(s.sympify(source['coefficients'][str(n)][r],locals={'x':x,'q':q})*y**r for r in range(5))
    test(f'complete homogeneous table {n}',s.expand(actual-table)==0,5)
    H[n]=actual

# Restore the original parameters symbolically for R0,R1,R2 and the full phase map.
beta,eta,alpha,chi,k,p,b,scale=s.symbols('beta eta alpha chi k p b scale',nonzero=True)
Ts=s.Matrix([[0,0,0,-eta],[1,0,0,0],[0,1,0,-beta],[0,0,1,0]])
Qs=s.Matrix([[0,0,1,0],[0,-1,0,beta],[1,0,-beta,0],[0,beta,0,eta-beta**2]])
S=s.diag(1,scale,scale**2,scale**3)
test('exact original root-scale matrix identity',all(s.expand(z)==0 for z in Ts.subs({beta:scale**2,eta:scale**4*x})**2-scale**2*S.inv()*T**2*S),16)
test('exact original quadratic scale matrix identity',all(s.expand(z)==0 for z in Qs.subs({beta:scale**2,eta:scale**4*x})-scale**-2*S.T*Q*S),16)
den=s.expand((p-b/2)**2+(k*b/beta)**2-(p*p-p*b+x*b*b))
test('full original unit denominator restoration',s.expand(den.subs(k**2,beta**2*(x-s.Rational(1,4))))==0)

def pair(expr):
    A=[s.expand(expr).coeff(q,r) for r in range(4)]
    return (4*A[0]+(rt-1)*A[1]-(rt+1)*(A[2]+A[3]),2*A[1]+(rt-1)*(A[2]-A[3]))
P2,J2=pair(H[2]);P4,J4=pair(H[4])
RR,Y,X=ring('y,x',K)
sub=RR.from_expr(P2).subresultants(RR.from_expr(J2))
resultant=s.Poly(sub[-1].as_expr(),x,domain=K)
constant=-s.Rational(492160000000,59049)+s.Rational(24448000000,6561)*rt
geom=(x-s.Rational(1,4))*(x-s.Rational(1,9))**2
F=s.Poly(s.sympify(elim['residual_polynomial'],locals={'x':x}),x,domain=K)
test('full characteristic-zero resultant factorization',resultant==s.Poly(constant*geom*F.as_expr(),x,domain=K))
test('residual is monic degree19',F.degree()==19 and F.LC()==1)
linear_y=s.Poly(sub[-2].as_expr(),y,domain=K.poly_ring(x))
A=s.Poly(linear_y.nth(1),x,domain=K);B=s.Poly(linear_y.nth(0),x,domain=K)
rows=[s.Poly(y**r*f,y) for f in [P2,J2] for r in [2,1,0]]
M=s.Matrix([[row.nth(r) for r in range(6,-1,-1)] for row in rows])
for name,column,target in [('A',5,A),('B',6,B)]:
    determinant=DomainMatrix.from_Matrix(M[:,[0,1,2,3,4,column]]).convert_to(K.poly_ring(x)).det().as_expr()
    test(f'exact cofactor determinant {name}',s.Poly(determinant,x,domain=K)==target)
test('cofactor degrees retained',A.degree()==14 and B.degree()==15,2)

def modc(c):
    c=s.expand(c)
    rational=c.coeff(rt,0);radical=c.coeff(rt,1)
    test_value=s.expand(c-rational-radical*rt)
    assert test_value==0
    for part in [rational,radical]:
        assert s.denom(part)%prime!=0
    value=s.cancel(rational+45*radical);num,den=s.fraction(value)
    return int(num)*pow(int(den),-1,prime)%prime

def modp(expr):
    poly=s.Poly(expr,x,domain=K)
    return s.Poly.from_dict({(r,):modc(poly.nth(r)) for r in range(poly.degree()+1)},x,modulus=prime)

def fromarr(a):return s.Poly(sum(value*x**r for r,value in enumerate(a)),x,modulus=prime)

Fm,Am,Bm=modp(F.as_expr()),modp(A.as_expr()),modp(B.as_expr())
for name,value in [('residual',Fm),('linear_A',Am),('linear_B',Bm)]:
    test(f'printed reduction {name}',value==fromarr(cert[name]))
test('leading resultant coefficient survives',modc(constant)==37)
test('monic residual degree survives',Fm.degree()==19 and Fm.LC()==1)
test('linear degrees survive reduction',Am.degree()==14 and Bm.degree()==15,2)
ai=fromarr(cert['linear_A_inverse']);phase=fromarr(cert['phase_root'])
test('first multiplication inverse', (Am*ai).rem(Fm)==s.Poly(1,x,modulus=prime))
test('exact residual phase root',(phase+Bm*ai).rem(Fm).is_zero)
E=s.Poly(0,x,modulus=prime)
py=s.Poly(P4,y,domain=K.poly_ring(x))
for coefficient in py.all_coeffs(): E=(E*phase+modp(coefficient)).rem(Fm)
test('printed fourth coefficient residue',E==fromarr(cert['fourth_real_at_root']))
test('second multiplication inverse',(E*fromarr(cert['fourth_real_inverse'])).rem(Fm)==s.Poly(1,x,modulus=prime))

for n in [2,4]:
    aa=[s.expand(H[n]).coeff(q,r) for r in range(4)]
    pp,jj=pair(H[n]);Pother=4*aa[0]-(rt+1)*aa[1]+(rt-1)*(aa[2]+aa[3]);Jother=(rt-1)*aa[1]-2*aa[2]+2*aa[3]
    test(f'conjugate field embedding real {n}',s.expand(pp.xreplace({rt:-rt})-Pother)==0)
    test(f'conjugate field embedding imaginary {n}',s.expand(jj.xreplace({rt:-rt})-(rt+1)*Jother/2)==0)

endpoint=red(s.expand(H[2]).coeff(y,4)+q**4*(1-9*x)*(q-1)*(q*q+3*q+1)/81)
test('full phase endpoint coefficient',endpoint==0)
geometry=s.Poly(x-s.Rational(1,9),x,domain=K)
Pr=s.Poly(P4.subs(y,s.Rational(1,3)),x,domain=K).exquo(geometry)
Jr=s.Poly(J4.subs(y,s.Rational(1,3)),x,domain=K).exquo(geometry)
Pm,Jm=modp(Pr.as_expr()),modp(Jr.as_expr())
test('second phase degree preservation',Pr.degree()==Jr.degree()==Pm.degree()==Jm.degree()==5,4)
test('second phase real reduction',Pm==fromarr(cert['second_phase_real_quotient']))
test('second phase imaginary reduction',Jm==fromarr(cert['second_phase_imag_quotient']))
test('second phase exact Bezout identity',Pm*fromarr(cert['second_phase_bezout_real'])+Jm*fromarr(cert['second_phase_bezout_imag'])==s.Poly(1,x,modulus=prime))

proof=HERE/'ARBITRARY_UNIT_NONCONSTANCY.tex'
out={'status':'pass','groups':len(checks),'scalar_entries':sum(t['entries'] for t in checks),'checks':checks,
     'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'All original real unit phases; exact z2/z4 nonconstancy and second exceptional phase z4 nonvanishing. No numerical sampling or finite-zero orbit assertion.'}
(HERE/'ARBITRARY_UNIT_NONCONSTANCY_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','groups':out['groups'],'scalar_entries':out['scalar_entries']}),flush=True)
