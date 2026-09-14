from pathlib import Path
import json, hashlib
import sympy as S
BASE=Path(__file__).resolve().parent
A,N=7,4
G=S.Symbol('gamma_0',positive=True)
z=S.Symbol('z')
series=S.series(S.cos(z)**S.Rational(-1,2),z,0,2*(A+2*N)+1).removeO()
mu=[G*S.factorial(2*j)*series.coeff(z,2*j) for j in range(A+2*N+1)]
H={(a,0):S.Integer(1) for a in range(A+1)}
for a in range(A+1):
 for n in range(1,N+1):
  H[a,n]=S.factor(S.det(S.Matrix(n,n,lambda i,j:mu[a+i+j])))
# Every H carries its exact original mass G**n.
assert all(S.simplify(h/G**n).is_positive for (a,n),h in H.items())
c=[S.Rational(2*j+1)*S.Rational(4*j+1,2) for j in range(N+A+1)]
d=[S.Rational(2*j)*S.Rational(4*j-1,2) for j in range(N+A+1)]
C={0:c[:]} ; D={0:d[:]}
for a in range(A):
 newc=[];newd=[]; e=c[0]
 for n in range(len(c)-1):
  if n==0: dd=S.Integer(0)
  else:
   den=e+d[n]
   ee=S.cancel(c[n]*e/den)
   dd=S.cancel(c[n]*d[n]/den)
   e=ee
  newc.append(S.cancel(e+d[n+1]));newd.append(dd)
 assert all(v>0 for v in newc)
 assert newd[0]==0 and all(v>0 for v in newd[1:])
 c,d=newc,newd; C[a+1]=c[:];D[a+1]=d[:]
checks={}
checks['christoffel_norm_ratios']=0
checks['inverse_connection_norm_ratios']=0
for a in range(A):
 for n in range(N):
  expected=H[a+1,n+1]*H[a,n]/(H[a,n+1]*H[a+1,n])
  assert S.cancel(C[a][n]-expected)==0
  checks['christoffel_norm_ratios']+=1
 for n in range(1,N):
  expected=H[a,n+1]*H[a+1,n-1]/(H[a,n]*H[a+1,n])
  assert S.cancel(D[a][n]-expected)==0
  checks['inverse_connection_norm_ratios']+=1
checks['original_determinant_reconstruction']=0
for a in range(A+1):
 for n in range(N+1):
  val=H[0,n]*S.prod(C[s][j] for s in range(a) for j in range(n))
  assert S.cancel(val-H[a,n])==0
  checks['original_determinant_reconstruction']+=1
checks['positive_desnanot_jacobi']=0
for a in range(A-1):
 for n in range(1,N):
  difference=H[a,n]*H[a+2,n]-H[a+1,n]**2
  right=H[a,n+1]*H[a+2,n-1]
  assert S.cancel(difference-right)==0 and right.is_positive
  checks['positive_desnanot_jacobi']+=1
checks['full_matrix_parity']=0
for a in range(A):
 for r in range(1,2*N):
  if a+(r-1)>A+2*N: continue
  M=S.Matrix(r,r,lambda i,j:0 if (i+j)%2 else mu[a+(i+j)//2])
  expected=H[a,(r+1)//2]*H[a+1,r//2]
  assert S.cancel(S.det(M)-expected)==0
  checks['full_matrix_parity']+=1
n,q,l=2,4,2
Z=lambda a:H[a,n]*H[a,n+1]*H[a+1,n]**2
ratio=S.cancel(Z(q+l)/Z(q))
product=S.prod(S.prod(C[q+s][j] for j in range(n))*S.prod(C[q+s][j] for j in range(n+1))*S.prod(C[q+s+1][j] for j in range(n))**2 for s in range(l))
assert S.cancel(ratio-product)==0
checks['paired_original_rank_ratio']=1
receipt={'status':'passed','kind':'finite exact rational identities supplementing the complete analytic proof','original_mass_symbol':'gamma_0=sqrt(2*pi), preserved as gamma_0**n in H_n^(a)','a_range':[0,A],'max_hankel_size':N,'checks':checks,'source_sha256':hashlib.sha256((BASE/'independent_contiguous.tex').read_bytes()).hexdigest(),'first_even_moments':[str(v) for v in mu[:5]],'first_shift_c':[str(v) for v in C[1][:3]],'no_asymptotic_claim':True}
(BASE/'CONTIGUOUS_EXACT_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
