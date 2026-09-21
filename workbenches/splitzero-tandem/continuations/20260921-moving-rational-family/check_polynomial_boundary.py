from pathlib import Path
import json, sympy as s
P=Path(__file__).parent;y,z=s.symbols('y z');I=s.I
checks=[]
def eq(a,b,name):
    v=a-b
    ok=all(s.simplify(x)==0 for x in v) if isinstance(v,s.MatrixBase) else s.simplify(v)==0
    assert ok,name
    checks.append(name)
def coeff(p,n):return s.Matrix([s.expand(p).coeff(y,j) for j in range(n)])
def frame(Q,D):
    q=s.degree(Q,y);d=s.degree(D,y)
    rem=lambda p:s.rem(p,Q,y)
    M=s.Matrix.hstack(*[coeff(rem(y**(j+1)),q) for j in range(q)])
    pi=s.Matrix.hstack(*[coeff(s.div(rem(D*y**j),D,y)[0],q-d) for j in range(q)]) if d<q else s.zeros(0,q)
    lo=s.eye(q)[:,:q-d]
    F=s.eye(q)[:,q-d:]-lo*pi[:,q-d:]
    B=s.Matrix.hstack(*[coeff(s.rem(rem(D*y**(q-d+j)),D,y),d) for j in range(d)])
    DM=s.Matrix.hstack(*[coeff(rem(D*y**j),q) for j in range(q)])
    return M,pi,lo,F,B,DM
cases=[((y*y+1)**2,(y-I)**2),((y*y+1)**2,(y-I)**3),((y*y+1)**2,y*y+2),((y-1)**3*(y+2),(y-1)**2),((y-1)**3*(y+2),(y-1)**3),((y-1)**3*(y+2),(y-1)*(y+2)),(y*y+1,y-z),((y*y+1)**2,(y-z)**2),(y*y+1,y*y+1)]
for ci,(Q,D) in enumerate(cases):
    q=int(s.degree(Q));d=int(s.degree(D,y));M,pi,lo,F,B,DM=frame(Q,D)
    eq(pi*lo,s.eye(q-d),f'{ci}: low right inverse')
    eq(pi*F,s.zeros(q-d,d),f'{ci}: sector kernel')
    eq(DM*F,s.eye(q)[:,:d]*B,f'{ci}: full numerator map')
    eq(B.det(),(-1)**(d*(q-d))*s.resultant(Q,D,y),f'{ci}: resultant with sign')
    g=s.gcd(Q,D);e=int(s.degree(g,y))
    assert B.rank()==d-e;checks.append(f'{ci}: boundary rank')
    if e:
        Z=s.Matrix.hstack(*[coeff(s.cancel(Q/g)*y**j,q) for j in range(e)])
        eq(DM*Z,s.zeros(q,e),f'{ci}: full primary kernel')
        eq(pi*Z,s.zeros(q-d,e),f'{ci}: primary kernel retained in sector')
    if d>e:
        Q1=s.cancel(Q/g);D1=s.cancel(D/g);T=s.invert(D1,Q1,y)
        for j in range(d-e):
            x=coeff(s.rem(T*y**j,Q1,y),q)
            eq(DM*x,coeff(g*y**j,q),f'{ci}: explicit Bezout lift {j}')
    if s.simplify(B.det())!=0:
        eq(DM*F*B.inv(),s.eye(q)[:,:d],f'{ci}: original rational map')

Q=(y*y+1)**2;D=(y-I)**2;q=4;d=2
M,pi,lo,F,B,DM=frame(Q,D)
N=6
def moment(t):return s.gamma(s.Rational(t+1,2)) if t%2==0 else s.Integer(0)
S=s.Matrix(N+1,N+1,lambda i,j:moment(i+j))
R=s.Matrix.hstack(*[coeff(s.rem(y**j,Q,y),q) for j in range(N+1)])
G=(R*S.inv()*R.T).inv()
assert all(s.simplify(G[:j,:j].det())>0 for j in range(1,q+1))
checks.append('full attained Gaussian source is positive with every source column')
C=F.row_join(lo)
for rank in [2,1,0]:
    A=s.eye(2) if rank==2 else (s.Matrix([[0,1],[0,0]]) if rank==1 else s.zeros(2))
    Lam=A.row_join(s.eye(2))*C.inv()
    QB=(Lam*G.inv()*Lam.conjugate().T).inv()
    L=G.inv()*Lam.conjugate().T*QB
    eq(Lam*L,s.eye(2),f'r{rank}: original minimum section')
    Qpi=(pi*G.inv()*pi.conjugate().T).inv()
    Lpi=G.inv()*pi.conjugate().T*Qpi
    if rank==2:V0=F;Z=s.zeros(q,0)
    elif rank==1:
        Z=F[:,0:1];V0=F[:,1:2]-Z*(Z.conjugate().T*G*Z).inv()*Z.conjugate().T*G*F[:,1:2]
    else:Z=F;V0=s.zeros(q,0)
    AV=Lam*V0
    h=V0*(AV.conjugate().T*QB*AV).inv()*AV.conjugate().T*QB if rank else s.zeros(q,2)
    rho=s.zeros(0,2) if rank==2 else (s.Matrix([[0,1]]) if rank==1 else s.eye(2))
    Lrho=QB.inv()*rho.conjugate().T*(rho*QB.inv()*rho.conjugate().T).inv() if rank<2 else s.zeros(2,0)
    j0=(s.eye(q)-h*Lam)*Lpi
    zp=(s.eye(q)-h*Lam)*(s.eye(q)-Lpi*pi)
    eq(zp*j0,s.zeros(q,q-d),f'r{rank}: corrected quotient does not acquire residual kernel')
    eq(Lam*zp,s.zeros(2,q),f'r{rank}: residual kernel is original kernel')
    eq(pi*zp,s.zeros(q-d,q),f'r{rank}: residual kernel retained in sector')
    eq(zp*Z,Z,f'r{rank}: full rank-loss subspace retained')
    eq(Lam*j0,Lrho*rho*Lam*lo,f'r{rank}: corrected chain section')
    eq(zp+j0*pi,s.eye(q)-h*Lam,f'r{rank}: degree-zero homotopy')
    eq(Lrho*rho,s.eye(2)-Lam*h,f'r{rank}: degree-one homotopy')
    eq(j0.conjugate().T*G*j0,Qpi+(h*Lam*Lpi).conjugate().T*G*(h*Lam*Lpi),f'r{rank}: full corrected metric')
    eq(Z.conjugate().T*G*j0,s.zeros(2-rank,q-d),f'r{rank}: retained kernel orthogonal to corrected section')
    if rank==2:
        assert any(s.simplify(x)!=0 for x in Lam*Lpi)
        checks.append('negative control: uncorrected source minimum section fails chain equality')
    assert (Lam*F).rank()==rank
    checks.append(f'r{rank}: actual observation rank')
    K=s.Matrix.hstack(*Lam.nullspace())
    PZ=Z*(Z.conjugate().T*G*Z).inv()*Z.conjugate().T*G if Z.cols else s.zeros(q)
    candidates=((s.eye(q)-PZ)*K).columnspace()
    if candidates:
        K0=s.Matrix.hstack(*candidates)
        ratio=s.simplify(((pi*K0).conjugate().T*Qpi*(pi*K0)).det()/(K0.conjugate().T*G*K0).det())
        observed=s.simplify((AV.conjugate().T*QB*AV).det()/(V0.conjugate().T*G*V0).det())
        eq(ratio,observed,f'r{rank}: boundary kernel determinant identity PC32')
        eq(j0*pi*K0,K0,f'r{rank}: corrected section is exact inverse on original reduced kernel PC34')
    else:
        eq(AV.cols,0,f'r{rank}: empty determinant and entire retained kernel')

out=dict(status='passed',exact_checks=len(checks),checks=checks,scope='Exact algebra over symbolic moving poles and full repeated arithmetic factors; complete attained Gaussian source metric and complex observations at all three observation ranks. Auxiliary finite fixtures, not an arithmetic zero-packet computation.')
(P/'POLYNOMIAL_BOUNDARY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))
