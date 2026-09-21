from pathlib import Path
import sympy as s,json
P=Path(__file__).parent
y=s.symbols('y');checks=[]
def ck(v,name):
 if not v:raise AssertionError(name)
 checks.append(name)
def Z(M):return M.applyfunc(s.cancel)==s.zeros(*M.shape)
def remmat(p,M):
 d=s.degree(p,y)
 return s.Matrix(d,M+1,lambda i,j:s.Poly(s.rem(y**j,p,y),y).nth(i))
def gram(M):
 # Shared original Gamma mass sqrt(2*pi) is factored from both sides.
 ps=[s.Integer(1),y]
 for j in range(1,2*M+4):ps.append(s.expand(y*ps[-1]-j*s.Rational(2*j-1,2)*ps[-2]))
 moms=[s.Integer(1)]
 for j in range(1,2*M+5):
  f=s.Poly(ps[j],y)
  moms.append(-sum(f.nth(i)*moms[i] for i in range(j)))
 return s.Matrix(M+1,M+1,lambda i,j:moms[i+j+4]+2*moms[i+j+2]+moms[i+j])
for repeated in [False,True]:
 pg=(y-1-s.I)**(2 if repeated else 1)*(y+2)
 pf=(y-5*s.I)**2
 p=s.expand(pg*pf);a=s.degree(pg,y);b=s.degree(pf,y);g=a+b
 Rb=remmat(pg,g-1);Rf=remmat(pf,g-1);CRT=Rb.col_join(Rf)
 ib=s.Poly(s.rem(s.invert(pf,pg,y)*pf,p,y),y)
 I_b=s.Matrix(g,a,lambda i,j:s.Poly(s.rem(ib.as_expr()*y**j,p,y),y).nth(i))
 iff=s.rem(s.invert(pg,pf,y)*pg,p,y)
 I_f=s.Matrix(g,b,lambda i,j:s.Poly(s.rem(iff*y**j,p,y),y).nth(i))
 ck(Z(Rb*I_b-s.eye(a)) and Z(Rf*I_b),'exact original CRT good section')
 ck(Z(Rf*I_f-s.eye(b)) and Z(Rb*I_f),'exact original CRT distant section')
 ck(Z(I_b*Rb+I_f*Rf-s.eye(g)),'full primary decomposition including multiplicities')
 r=a
 mix=s.zeros(r,g)
 for i in range(a):mix[i,i]=1
 mix[0,a]=1
 AR=mix*CRT
 # Only the first row sees the distant component; h=1.
 B0=s.eye(r)[1:,:];Ab=B0*AR*I_b
 ck((AR*I_f).rank()==1 and B0.rows==r-1,'DCR6 exact row codimension')
 ck(Z(B0*AR-Ab*Rb),'DCR7 fixed coefficient factorization')
 vals=[]
 for M in [g-1,g,2*g-1,2*g]:
  H=gram(M);Hi=H.inv()
  Rd=remmat(p,M);Rg=remmat(pg,M)
  C=(AR*Rd*Hi*Rd.H*AR.H).applyfunc(s.cancel)
  Qd=(Rd*Hi*Rd.H).inv()
  JK=s.Matrix.hstack(*AR.nullspace())
  JR=AR.H*(AR*AR.H).inv()
  TT=JK.row_join(JR)
  HK=JK.H*Qd*JK
  ck(s.cancel(HK.det()-TT.det()*s.conjugate(TT.det())*Qd.det()*C.det())==0,'DCR25 complete fixed-frame determinant M%d'%M)
  Cg=(Ab*Rg*Hi*Rg.H*Ab.H).applyfunc(s.cancel)
  ck(Z(B0*C*B0.H-Cg),'DCR8 complete original-source covariance M%d'%M)
  # Put the retained rows first; complete determinant contains a Schur factor.
  U=s.eye(r)[1:,:].col_join(s.eye(r)[:1,:])
  CC=U*C*U.T; A=CC[:-1,:-1];F=CC[-1,-1]-(CC[-1,:-1]*A.inv()*CC[:-1,-1])[0]
  ck(s.cancel(CC.det()-A.det()*F)==0,'DCR20 exact Schur determinant M%d'%M)
  ck(s.cancel(F)>0,'DCR20 positive complementary full metric M%d'%M)
  vals.append((C,F))
 for j in [0,1]:
  dif=vals[j+2][0]-vals[j][0]
  ck(all(s.cancel(dif[:t,:t].det())>0 for t in range(1,r+1)),'source enlargement positive covariance')
  ck(s.cancel(vals[j+2][1]-vals[j][1])>=0,'complementary Schur monotonicity')
 # Exact analytic-remainder construction with a polynomial denominator invertible at all roots.
 rn=(1-y*y/100)*(1-y*y/121)*(1-y*y/144)
 v=1+2*y
 av=s.rem(v*s.invert(rn,pg,y),pg,y)
 lift=s.expand(rn*av)
 ck(s.rem(lift-v,pg,y)==0,'DCR12 full Hermite jet lift')
 ck(s.degree(lift,y)<=6+a-1,'DCR12 source degree retained')
 if repeated:
  rad=(y-1-s.I)*(y+2)
  wrong=s.rem(v*s.invert(rn,rad,y),rad,y)
  ck(s.rem(rn*wrong-v,pg,y)!=0,'negative control simple-value lift loses repeated-root derivative')
 # Original S'=c'+iy conversion: same full coefficient map, not an inferred isometry.
 cp=s.Rational(5,2);Sp=s.symbols('Sp')
 T=s.Matrix(g,g,lambda i,j:s.Poly((cp+s.I*y)**j,y).nth(i))
 physical=s.Matrix(g,g,lambda i,j:s.Poly(((Sp-cp)/s.I)**j,Sp).nth(i))
 ck(Z(T*physical-s.eye(g)),'DCR1 exact original physical coordinate inverse')
 # A row that sees the distant factor cannot be replaced by its good part.
 ck(not Z(AR-AR*I_b*Rb),'negative control distant component cannot be silently erased')
# Receiver sign identity before estimates, with independent source factors.
lo0,lo1,hi0,hi1,d0,d1,c=s.symbols('lo0 lo1 hi0 hi1 d0 d1 c')
G=(lo0+c+d0-hi0)+(lo1+c+d1-hi1)
ck(s.expand(G-(2*c+lo0+lo1-hi0-hi1+d0+d1))==0,'DCR22 all four original signs')
rec={'status':'passed','checks':len(checks),'details':checks,'scope':'Exact auxiliary simple/repeated-root CRT, complete weighted Gamma source minima at four cutoffs, original coordinate maps, complete fixed-frame determinant, Schur monotonicity, Hermite reconstruction, two negative controls. Fixtures do not evaluate original-period asymptotics; analytic estimates have full proofs in DCR1-27.'}
(P/'CONDUCTOR_DIVISOR_EXACT_CHECKS.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps({'status':'passed','checks':len(checks)}))
