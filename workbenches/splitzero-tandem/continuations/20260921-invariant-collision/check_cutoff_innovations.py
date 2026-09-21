"""Exact finite complete-relation tests, all observation rows retained.

This auxiliary complex-shift packet is not an actual zeta-zero packet.
Its common Gamma mass is retained as the symbol M_sigma in the proof;
the checker evaluates the rational matrix factor of that same mass.
"""
from pathlib import Path
import json
import sympy as s
from exact_reference import moments

P=Path(__file__).parent
x,w=s.symbols('x w');I=s.I;checks=[]
def zero(v): return all(s.cancel(z)==0 for z in v)
def ok(name,v):
    assert bool(v),name
    checks.append(name)
def simp(A):return A.applyfunc(s.cancel)

q=6;v=1;qp=2;gap=3;maxL=q;maxM=gap+maxL
chi=s.prod(x-r for r in [0,1,2,3,4*I,1+4*I]);chip=x*(x-1)
mu=moments(qp+maxM)
def moment(n):return s.Rational(int(mu[n//2]),2**(n//2)) if n%2==0 else s.Integer(0)
def ip(f,g):
    f=s.Poly(f,x);g=s.Poly(g,x)
    return s.cancel(sum(s.conjugate(f.nth(i))*g.nth(j)*s.conjugate(I)**i*I**j*moment(i+j)
                    for i in range(f.degree()+1) for j in range(g.degree()+1)))
H=s.Matrix(maxM+1,maxM+1,lambda i,j:ip(chip*x**i,chip*x**j))
nums=[s.exp(w)-1,s.exp(3*w)-s.exp(2*w)]
Gseries=[s.series(F/(s.exp(4*I*w)-1),w,0,maxM+qp+1).removeO().expand() for F in nums]
B=s.Matrix(2,maxM+1,lambda i,j:sum(s.Poly(chip*x**j,x).nth(a)*s.factorial(a)*Gseries[i].coeff(w,a)
                                for a in range(j+qp+1)))
U=s.Matrix(maxM+1,maxL+1,lambda i,j:s.Poly(s.cancel(((chi*x**j).subs(x,x+4*I)-chi*x**j)/chip),x).nth(i))
ok('all rows annihilate every complete nonideal relation',zero(B*U))
A=B[:,:gap];K=s.Matrix.hstack(*A.nullspace());ok('entire two-row observation rank',A.rank()==2)
Cs={};Qs={};Ks={};source_pivots={};relation_pivots={};innovation_values={};retention={}
for L in range(-1,maxL+1):
    n=gap+L;HH=H[:n+1,:n+1];BB=B[:,:n+1];HHinv=HH.inv()
    CC=simp(BB*HHinv*BB.conjugate().T);Cs[n]=CC
    low=s.eye(n+1)[:,:gap]
    if L>=0:
        uu=U[:n+1,:L+1];RR=simp(uu.conjugate().T*HH*uu)
        Q=simp(low.conjugate().T*HH*low-low.conjugate().T*HH*uu*RR.inv()*uu.conjugate().T*HH*low)
        if L==0: r=RR[0,0]
        else:
            row=RR[:L,L:];r=s.cancel(RR[L,L]-(row.conjugate().T*RR[:L,:L].inv()*row)[0])
        relation_pivots[L]=r
        tau=s.prod(4*I*s.binomial(q+j,v) for j in range(L+1))
        ok(f'full graph determinant L={L}',s.cancel(Q.det()-s.conjugate(tau)*tau*HH.det()/RR.det())==0)
    else:Q=HH
    Qs[n]=Q;Ks[n]=s.cancel((K.conjugate().T*Q*K).det())
    ok(f'complete observation covariance L={L}',zero(CC-A*Q.inv()*A.conjugate().T))
    if L<0:
        constant=s.cancel(Ks[n]/(Q.det()*CC.det()))
    ok(f'fixed frame complementary identity L={L}',s.cancel(Ks[n]-constant*Q.det()*CC.det())==0)
    if L>=0:
        hp=HH[:n,n:];nu=s.cancel(HH[n,n]-(hp.conjugate().T*HH[:n,:n].inv()*hp)[0]);source_pivots[n]=nu
        f=simp(BB[:,n:]-BB[:,:n]*HH[:n,:n].inv()*hp)
        ok(f'full covariance rank-one innovation L={L}',zero(CC-Cs[n-1]-f*f.conjugate().T/nu))
        lam=s.cancel((f.conjugate().T*Cs[n-1].inv()*f)[0]/nu)
        innovation_values[n]=lam;ok(f'nonnegative complete covariance gain L={L}',lam>=0)
        ok(f'exact covariance determinant ratio L={L}',s.cancel(CC.det()/Cs[n-1].det()-(1+lam))==0)
        a=4*I*s.binomial(q+L,v)
        rho=s.cancel(relation_pivots[L]/(s.conjugate(a)*a*nu*(1+lam)))
        retention[L]=rho
        ok(f'original kernel loss positive L={L}',rho>=1)
        ok(f'original kernel exact reciprocal change L={L}',s.cancel(Ks[n-1]/Ks[n]-rho)==0)
        # Keep the old quotient coordinate of u_L after its new source direction.
        oldframe=s.eye(n)[:,:gap].row_join(U[:n,:L])
        v_old=U[:n,L:L+1]+a*HH[:n,:n].inv()*hp
        r_old=simp((oldframe.inv()*v_old)[:gap,:])
        Qprev=Qs[n-1]
        total=s.cancel((r_old.conjugate().T*Qprev*r_old)[0])
        observed=s.cancel(((A*r_old).conjugate().T*Cs[n-1].inv()*(A*r_old))[0])
        kerproj=simp(K*(K.conjugate().T*Qprev*K).inv()*K.conjugate().T*Qprev)
        kp=simp(kerproj*r_old);kernel=s.cancel((kp.conjugate().T*Qprev*kp)[0])
        ok(f'new observed coefficient keeps complex leading phase L={L}',zero(f+A*r_old/a))
        ok(f'complete relation innovation decomposition L={L}',s.cancel(relation_pivots[L]-s.conjugate(a)*a*nu-total)==0)
        ok(f'actual quotient rank-one downdate L={L}',zero(Q-Qprev+Qprev*r_old*r_old.conjugate().T*Qprev/relation_pivots[L]))
        ok(f'observed and kernel energies add L={L}',s.cancel(total-observed-kernel)==0)
        ok(f'observed energy is the exact covariance gain L={L}',s.cancel(observed-s.conjugate(a)*a*nu*lam)==0)
        ok(f'positive loss is original kernel energy L={L}',s.cancel(rho-1-kernel/(s.conjugate(a)*a*nu+observed))==0)
        ok(f'kernel energy nonnegative L={L}',kernel>=0)
ns=[gap-1,gap,gap+q-1,gap+q]
left=s.cancel(Ks[ns[0]]*Ks[ns[1]]/(Ks[ns[2]]*Ks[ns[3]]))
right=s.cancel(retention[0]*retention[q]*s.prod(retention[j]**2 for j in range(1,q)))
ok('four prescribed cutoffs weighted positive product',s.cancel(left-right)==0)
cleft=s.cancel(Cs[ns[0]].det()*Cs[ns[1]].det()/(Cs[ns[2]].det()*Cs[ns[3]].det()))
cright=s.cancel(1/((1+innovation_values[gap])*(1+innovation_values[gap+q])*s.prod((1+innovation_values[j])**2 for j in range(gap+1,gap+q))))
ok('full projected covariance four-cutoff product',s.cancel(cleft-cright)==0)
out=dict(status='passed',checks=len(checks),details=checks,scope='Auxiliary complex-shift packet; full physical i phase, two observation rows, all relation columns and original cutoffs. No actual zero or period chosen.',
         kernel_return_exponential=str(left),covariance_return_exponential=str(cleft),
         original_kernel_return_log=str(s.N(s.log(left),35)),
         full_projected_covariance_return_log=str(s.N(s.log(cleft),35)),
         retention_factors={str(k):str(v) for k,v in retention.items()},
         covariance_increments={str(k):str(v) for k,v in innovation_values.items()})
(P/'CUTOFF_INNOVATION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k in ['status','checks','original_kernel_return_log','full_projected_covariance_return_log','scope']}))
