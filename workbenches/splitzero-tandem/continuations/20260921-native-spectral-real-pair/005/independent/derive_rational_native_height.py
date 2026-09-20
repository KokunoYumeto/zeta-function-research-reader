"""Exact original rational numerator coefficient and native compound calculation."""
from pathlib import Path
import itertools
import json
import sympy as s
y,t,d,b,M=s.symbols('y tau d beta M', real=True, nonzero=True)
i=s.I
Q=s.Matrix([[s.expand((d+i*(y-t))**j*(d-i*(y-t))**(3-j)).coeff(y,k) for j in range(4)] for k in range(4)])
moment=[M,0,M*b,0,M*(3*b*b+2*b),0,M*(15*b**3+30*b*b+16*b)]
K=s.Matrix([[moment[j+k] for k in range(4)] for j in range(4)])
detK=s.factor(K.det())
assert s.expand(detK-12*M**4*b**3*(b+1)**2*(b+2))==0
assert s.factor(Q.det())==-64*d**6
T=s.Matrix([[s.binomial(j,k)*(-t)**(j-k) if k<=j else 0 for j in range(4)] for k in range(4)])
assert (Q-T*Q.subs(t,0)).applyfunc(s.expand)==s.zeros(4)
vectors=s.Matrix([[1,3,1,1],[-1,-1,1,3],[1,-1,-1,3],[-1,3,-1,1]])
assert vectors.T*vectors==s.diag(4,20,4,20)
U=s.Matrix([[1,0,-b,0],[0,1,0,-(3*b+2)],[0,0,1,0],[0,0,0,1]])
expected_norms=s.diag(M,M*b,2*M*b*(b+1),6*M*b*(b+1)*(b+2))
assert (U.T*K*U-expected_norms).applyfunc(s.expand)==s.zeros(4)
H=(2*d*Q.conjugate().T*K*Q).applyfunc(s.expand)
for row in range(4):
 for col in range(4):
  p=s.expand(2*d*(d+i*(y-t))**(3+col-row)*(d-i*(y-t))**(3-col+row))
  via_moments=s.expand(sum(p.coeff(y,k)*moment[k] for k in range(7)))
  assert s.expand(H[row,col]-via_moments)==0
  if row<3 and col<3: assert s.expand(H[row,col]-H[row+1,col+1])==0

def comp(C,r):
 ix=list(itertools.combinations(range(4),r))
 return ix,s.Matrix([[s.expand(C.extract(I,J).det()) for J in ix] for I in ix])
def degree(v):return s.degree(v,t) if v!=0 else -s.oo
def matstr(A):return [[str(z) for z in row] for row in A.tolist()]
out={'coefficient_Q':matstr(Q),'moment_Gram':matstr(K),'moment_determinant':str(detK),'Q_determinant':str(s.factor(Q.det())),'translation_factorization_checked':True,'original_Toeplitz_integral_checked_all_16_entries':True,'limiting_coefficient_vectors':matstr(vectors),'limiting_native_polynomials':matstr(U),'native_polynomial_orthogonal_norms':matstr(expected_norms),'compounds':[]}
for r in range(1,5):
 labels,C=comp(Q,r)
 order=max(degree(v) for v in C)
 lead=C.applyfunc(lambda v:s.expand(v).coeff(t,order))
 _,Kg=comp(K,r)
 gram=(lead.conjugate().T*Kg*lead).applyfunc(s.expand)
 # A rank-one positive limit has unique nonzero eigenvalue equal to trace.
 trace=s.factor(s.trace(gram))
 assert lead.rank()==1
 assert (gram*gram-trace*gram).applyfunc(s.expand)==s.zeros(gram.rows)
 out['compounds'].append({'r':r,'input_output_subsets_zero_based':[list(I) for I in labels],'leading_degree':int(order),'leading_coefficient':matstr(lead),'leading_native_Gram':matstr(gram),'leading_squared_native_norm':str(trace),'rank_one_verified':True,'entry_degrees':[[str(degree(v)) for v in row] for row in C.tolist()]})
 print('r',r,'degree',order,'lead',lead,'native norm squared',trace)
out['all_assertions_passed']=True
Path(__file__).with_name('rational_native_height_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Q',Q)
print('Moment determinant',detK)
print('All assertions passed.')

# Exact original FC24 source return; no unspecified source Gram remains.
x0,x1,x2,x3=s.symbols('xi0 xi1 xi2 xi3')
k0,k1,k2,k3=s.symbols('k0 k1 k2 k3',positive=True)
ks=[k0,k1,k2,k3]
F=s.Matrix([[x0,x1,b*x0+2*x2,(3*b+2)*x1+6*x3],
 [0,x0,2*x1,(3*b+2)*x0+6*x2],[0,0,2*x0,6*x1],[0,0,0,6*x0]])
rho=s.symbols('rho0:4',nonzero=True)
invA=s.Matrix([[s.sqrt(ks[r])*[x0,x1,x2,x3][j-r]*rho[j] if r<=j else 0 for j in range(4)] for r in range(4)])
# Target-frame coefficient matrix divided by sqrt(M): multiplication by rho_j
# gives exactly j!, using the original factorial/Pochhammer identity.
Dt=s.Matrix([[1/rho[0],0,b/rho[0],0],[0,1/rho[1],0,(3*b+2)/rho[1]],[0,0,2/rho[2],0],[0,0,0,6/rho[3]]])
assert (invA*Dt-s.diag(*[s.sqrt(k) for k in ks])*F).applyfunc(s.expand)==s.zeros(4)
KU=(M*F.conjugate().T*s.diag(*ks)*F).applyfunc(s.expand)
A2=b*x0+2*x2; A3=(3*b+2)*x1+6*x3; B3=(3*b+2)*x0+6*x2
expected_entries={
 (0,0):k0*s.conjugate(x0)*x0,(0,1):k0*s.conjugate(x0)*x1,
 (0,2):k0*s.conjugate(x0)*A2,(0,3):k0*s.conjugate(x0)*A3,
 (1,1):k0*s.conjugate(x1)*x1+k1*s.conjugate(x0)*x0,
 (1,2):k0*s.conjugate(x1)*A2+2*k1*s.conjugate(x0)*x1,
 (1,3):k0*s.conjugate(x1)*A3+k1*s.conjugate(x0)*B3,
 (2,2):k0*s.conjugate(A2)*A2+4*k1*s.conjugate(x1)*x1+4*k2*s.conjugate(x0)*x0,
 (2,3):k0*s.conjugate(A2)*A3+2*k1*s.conjugate(x1)*B3+12*k2*s.conjugate(x0)*x1,
 (3,3):k0*s.conjugate(A3)*A3+k1*s.conjugate(B3)*B3+36*k2*s.conjugate(x1)*x1+36*k3*s.conjugate(x0)*x0}
for (r,c),value in expected_entries.items():assert s.expand(KU[r,c]-M*value)==0
source_minors=[];source_compounds=[]
for r in range(1,5):
 Fr=F[:r,:r]
 assert F[r:,:r]==s.zeros(4-r,r)
 detFr=s.factor(Fr.det())
 source_minors.append(s.factor(M**r*s.prod(ks[:r])*detFr*s.conjugate(detFr)))
 labels,C=comp(Q,r); degree_r=max(degree(v) for v in C)
 leadQ=C.applyfunc(lambda v:s.expand(v).coeff(t,degree_r))
 _,CF=comp(F,r)
 source_lead=(CF*leadQ).applyfunc(s.expand)
 weights=s.diag(*[s.prod(ks[j] for j in I) for I in labels])
 squared=s.factor((2*d)**r*M**r*s.trace(source_lead.conjugate().T*weights*source_lead))
 expected=[8*d*M*k0,320*d**4*M**2*k0*k1,40960*d**9*M**3*k0*k1*k2,9437184*d**16*M**4*k0*k1*k2*k3][r-1]*(x0*s.conjugate(x0))**r
 assert s.expand(squared-expected)==0
 source_compounds.append({'rank':r,'leading_F_compound_times_Q_compound':matstr(source_lead),'native_squared_compound_constant_h_equals_2d':str(squared)})
g0,g1,g2,g3,tseries=s.symbols('g0 g1 g2 g3 tseries',nonzero=True)
xis=[1/g0,-g1/g0**2,g1**2/g0**3-g2/g0**2,-g1**3/g0**4+2*g1*g2/g0**3-g3/g0**2]
prod=s.expand(sum(xis[j]*tseries**j for j in range(4))*sum([g0,g1,g2,g3][j]*tseries**j for j in range(4)))
assert [s.expand(prod).coeff(tseries,j) for j in range(4)]==[1,0,0,0]
out['original_source_extension']={'FC24_target_frame_multiplication_verified':True,'source_F':matstr(F),'source_Gram_all_entries_verified':True,'source_Gram':matstr(KU),'leading_principal_minors':[str(v) for v in source_minors],'original_inverse_series_verified':True,'source_compounds':source_compounds}
Path(__file__).with_name('rational_native_height_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Exact source leading principal minors:',source_minors)
print('All original-source coefficient, Gram, inverse and compound assertions passed.')
