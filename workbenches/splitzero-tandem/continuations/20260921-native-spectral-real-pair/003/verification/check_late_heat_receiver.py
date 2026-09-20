from pathlib import Path
import sympy as s,json
P=Path(__file__).parent
checks=0
def ck(v,label):
 global checks
 if not v:raise RuntimeError(label)
 checks+=1
for seed in range(1,5):
 F=s.Matrix([[2,1,s.I,0],[0,3,1,s.I],[0,0,seed+1,1],[1,0,0,2]])
 G=F.H*F+s.eye(4)
 M=s.Matrix([[1,3+seed,s.I,0],[0,2,1,1],[1,0,3,2*s.I],[0,1,0,4]])
 La=s.Matrix([[0,0,1,0],[0,0,0,1]])
 IK=s.eye(4)[:,:2]
 Q=(La*G.inv()*La.H).inv()
 L=G.inv()*La.H*Q
 PK=IK*(IK.H*G*IK).inv()*IK.H*G
 PB=L*La
 ck(s.simplify(PK+PB)==s.eye(4),'full complementary projections')
 ck(s.simplify(L.H*G*L)==Q,'minimum section exact isometry')
 u=s.Matrix([1,s.I,2,1-seed])
 th=(u.H*G*PK*u)[0]/(u.H*G*u)[0]
 ck(s.simplify(th-1+(u.H*La.H*Q*La*u)[0]/(u.H*G*u)[0])==0,'LS7 fraction equality')
 H=G.inv()*M.H*G*M
 W=IK.row_join(L)
 T=s.simplify(W.inv()*H*W)
 Hkk,Hkb,Hbk,Hbb=T[:2,:2],T[:2,2:],T[2:,:2],T[2:,2:]
 z=s.Integer(seed)
 direct=s.simplify(La*(z*s.eye(4)+H).inv()*L)
 schur=s.simplify((z*s.eye(2)+Hbb-Hbk*(z*s.eye(2)+Hkk).inv()*Hkb).inv())
 ck(s.simplify(direct-schur)==s.zeros(2),'LS11 exact resolvent')
 # First three derivatives of LS12 at zero:
 # T'(0)=-Hbb; T''(0)=Hbb^2+Hbk Hkb; T''' obtained by full matrix powers.
 ck(s.simplify(La*H**2*L-Hbb**2-Hbk*Hkb)==s.zeros(2),'LS12 second derivative')
 ck(s.simplify(-La*H**3*L+Hbb**3+Hbb*Hbk*Hkb+Hbk*Hkk*Hkb+Hbk*Hkb*Hbb)==s.zeros(2),'LS12 third derivative')
 # Full compressed heat is not replaced by the observed action's own heat.
 AB=La*M*L
 leakage=PK*M*L
 ck(s.simplify(Hbb-Q.inv()*AB.H*Q*AB-Q.inv()*leakage.H*G*leakage)==s.zeros(2),'LS10 retained direct leakage')
 ck(s.simplify(Hbb-Q.inv()*AB.H*Q*AB)!=s.zeros(2),'negative control deletes leakage')
out={'exact_checks':checks,'fixtures':4,'scope':'Actual metric orthogonal kernel/observation splitting, explicit surviving-class allocation, complete Schur resolvent and memory equation; four negative controls reject deletion of leakage. No native period estimate claimed.','status':'passed'}
(P/'LATE_HEAT_RECEIVER_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))

