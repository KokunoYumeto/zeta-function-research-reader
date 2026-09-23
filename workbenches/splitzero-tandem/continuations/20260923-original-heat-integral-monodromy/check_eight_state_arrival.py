from pathlib import Path
from itertools import permutations,product
import sympy as s,json,hashlib,shutil
d=Path(__file__).resolve().parent
checks=[]
def check(name,ok):
    assert ok,name
    checks.append(name)
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
group=[]
for p in permutations(range(4)):
    for eps in product([1,-1],repeat=4):
        if s.prod(eps)!=parity(p):continue
        image=[2*p[i]+(b if eps[i]==1 else 1-b) for i in range(4) for b in range(2)]
        group.append((p,eps,image))
check('determinant-one signed group order',len(group)==192)
k=[0,1,5,4,3,2,7,6]
K=s.zeros(8)
for j,i in enumerate(k):K[i,j]=1
sumK=s.zeros(8)
for p,eps,img in group:
    for i in range(8):
        for j in range(8):sumK[i,j]+=K[img[i],img[j]]
avg=sumK/192
E=s.zeros(8)
for a in range(4):
    for i in range(2):
        for j in range(2):E[2*a+i,2*a+j]=s.Rational(1,2)
P0=s.ones(8)/8
check('exact order192 average',avg==P0+(E-P0)/3)
check('native inertia',K.eigenvals()=={s.Integer(1):5,s.Integer(-1):3})
check('averaged spectrum',avg.eigenvals()=={s.Integer(1):1,s.Rational(1,3):3,s.Integer(0):4})
H=[]
for p,eps,img in group:
    if p==tuple(range(4)) and eps[0]==eps[3] and eps[1]==eps[2]:H.append(img)
check('arithmetic subgroup order',len(H)==4)
check('arithmetic action preserves native form',all(s.Matrix(8,8,lambda i,j:K[im[i],im[j]])==K for im in H))
vinf=s.zeros(8,1);vinf[6]=1;vinf[7]=-1
veven=s.Matrix([0,0,1,1,-1,-1,0,0])
check('literal infinity native value',(vinf.T*K*vinf)[0]==-2)
check('literal infinity averaged value',(vinf.T*avg*vinf)[0]==0)
check('even-root native value including half-density',(veven.T*K*veven)[0]/2==-2)
check('even-root averaged value including half-density',(veven.T*avg*veven)[0]/2==s.Rational(2,3))
check('native permutation lies in group',any(img==k for p,eps,img in group))
check('native sign character',all(parity(p)==-1 for p,eps,img in group if img==k))
# The universal positive lift has coefficient Fix(p)/192, because
# e_triv+e_std/3=(1+(Fix(p)-1))/192 in the group basis.
check('positive lift sign-character image',sum(s.Rational(sum(p[i]==i for i in range(4)),192)*parity(p) for p,eps,img in group)==0)
class_character=0
for p,eps,img in group:
    inv=[0]*8
    for j,i in enumerate(img):inv[i]=j
    conjugate=[inv[k[img[j]]] for j in range(8)]
    class_character+=parity(tuple(conjugate[2*j]//2 for j in range(4)))
check('class-average sign-character image',s.Rational(class_character,192)==-1)
record={'scope':'Exact finite checks of equations1-17 in the supplied eight-state continuation; not a certification of its complete manuscript or a global Weil-sign conclusion.','count':len(checks),'all_passed':True,'checks':checks,'native_matrix':[[int(x) for x in row] for row in K.tolist()],'average_matrix':[[str(x) for x in row] for row in avg.tolist()]}
(d/'EIGHT_STATE_ARRIVAL_CHECKS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')

print(json.dumps({'count':len(checks),'all_passed':True}))
