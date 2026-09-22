"""Exact finite checks of ESHL; infinite extension is proved by coordinate sums."""

import json
from pathlib import Path
import sympy as sp

h = sp.symbols('h', real=True)
t = -1+8*h
ah = -sp.Rational(1,4)+2*h
checks = []


def check(name, lhs, rhs):
    difference=lhs-rhs
    if isinstance(difference, sp.MatrixBase):
        ok=all(sp.simplify(x)==0 for x in difference)
    else:
        ok=sp.simplify(difference)==0
    if not ok:
        raise AssertionError((name,difference))
    checks.append(name)


rawplus=sp.diag(1,1,0,1)
rawminus=sp.diag(0,0,1,0)
A0=(rawplus-rawminus)/4
check('raw positive projector recovered',2*A0+sp.eye(4)/2,rawplus)
check('raw negative projector recovered',-2*A0+sp.eye(4)/2,rawminus)
check('raw quarter multiplicities',sp.trace(rawplus),3)
check('raw negative multiplicity',sp.trace(rawminus),1)
P2=sp.eye(3)-sp.ones(3)/3
check('original triangle support idempotent',P2*P2,P2)
check('original triangle ambient kernel',P2*sp.ones(3,1),sp.zeros(3,1))

# The original forced raw metric is not replaced by the HS metric.
G=sp.Matrix([[sp.Rational(1,16),0,0,-sp.Rational(7,144)],
             [0,sp.Rational(2,9),0,0], [0,0,1,0],
             [-sp.Rational(7,144),0,0,sp.Rational(1,16)]])
vplus=sp.Matrix([1,0,0,1])/sp.sqrt(2)
vminus=sp.Matrix([1,0,0,-1])/sp.sqrt(2)
metricT=(vplus*vplus.T/(6*sp.sqrt(2))+vminus*vminus.T/3
         +sp.diag(0,sp.sqrt(2)/3,1,0))
rawAh=rawplus/4+ah*rawminus
check('forced metric square root',metricT.T*metricT,G)
check('metric isometry commutes negative projector',metricT*rawminus,rawminus*metricT)
check('metric isometry commutes whole heat family',metricT*rawAh,rawAh*metricT)
check('original heat form metric transport',metricT.T*rawAh*metricT,G*rawAh)
check('metric map retains its nonunital raw action',metricT*sp.Matrix([1,0,0,1]),
      sp.Matrix([1,0,0,1])/(6*sp.sqrt(2)))

for q in (1,2,3):
    Qlow=sp.kronecker_product(sp.eye(q),sp.diag(1,0),sp.eye(3))
    Qhigh=sp.kronecker_product(sp.eye(q),sp.diag(0,1),sp.eye(3))
    D=sp.kronecker_product(sp.eye(q),sp.Matrix([[0,0],[2,0]]),sp.eye(3))
    U=D.T
    weight=16*Qlow+4*Qhigh
    psiA=Qlow/4+ah*Qhigh
    H=4*Qlow+t*Qhigh
    K=H-(4+t)*sp.eye(6*q)/2
    check(f'q={q} actual weighted lift',weight*psiA,H)
    check(f'q={q} blade forward product',U*D,4*Qlow)
    check(f'q={q} blade reverse product',D*U,4*Qhigh)
    check(f'q={q} retained blade nilpotent',D*D,sp.zeros(6*q))
    check(f'q={q} original directed carrier',U*D+t*Qhigh,H)
    check(f'q={q} full mixed commutator',H*D-D*H,(t-4)*D)
    check(f'q={q} trace',sp.trace(H),3*q*(4+t))
    check(f'q={q} Hilbert Schmidt square',sp.trace(H*H),3*q*(16+t*t))
    check(f'q={q} determinant',H.det(),4**(3*q)*t**(3*q))
    check(f'q={q} traceless square',sp.trace(K*K),sp.Rational(3*q,2)*(4-t)**2)
    check(f'q={q} source HS length at zero',sp.trace(H*H).subs(h,0),51*q)
    check(f'q={q} source traceless length at zero',sp.trace(K*K).subs(h,0),sp.Rational(75*q,2))
    ambientP=sp.kronecker_product(sp.eye(q),P2,sp.eye(3))
    check(f'q={q} retained ambient kernel dimension',9*q-sp.trace(ambientP),3*q)
    H0inv=Qlow/4-Qhigh
    check(f'q={q} relative operator',H*H0inv,sp.eye(6*q)-8*h*Qhigh)
    nilpotent=D/2
    critical=4*Qlow
    check(f'q={q} collision infinitesimal nilpotence',nilpotent**2,sp.zeros(6*q))
    check(f'q={q} collision initial projection',nilpotent.T*nilpotent,Qlow)
    check(f'q={q} collision final projection',nilpotent*nilpotent.T,Qhigh)
    check(f'q={q} collision carrier kills image',critical*nilpotent,sp.zeros(6*q))
    check(f'q={q} collision reverse product survives',nilpotent*critical,4*nilpotent)
    check(f'q={q} complete infinitesimal pairing',nilpotent.T*H*nilpotent,t*Qlow)
    check(f'q={q} regular infinitesimal trace',sp.trace(nilpotent),0)
    marked=sp.symbols('marked')
    check(f'q={q} nilpotent determinant',(sp.eye(6*q)-marked*nilpotent).det(),1)

# One actual local inclusion retains entire orbit blocks, including rotations.
big=sp.kronecker_product(sp.eye(3),sp.diag(4,t),sp.eye(3))
small=sp.kronecker_product(sp.eye(2),sp.diag(4,t),sp.eye(3))
inclusion=sp.eye(18)[:,:12]
check('finite orbit inclusion intertwines heat',big*inclusion,inclusion*small)
check('finite orbit compression recovers actual lift',inclusion.T*big*inclusion,small)

# Exact full raw matrix algebra map, quarter corner, and quadratic receiver.
rawsymbols=sp.symbols('x11 x12 x21 x22')
X=sp.Matrix(2,2,rawsymbols)
Y=sp.Matrix([[1+sp.I,2-sp.I],[3+2*sp.I,5-sp.I]])
R=lambda matrix:sp.kronecker_product(matrix,sp.eye(3))
low=R(sp.diag(1,0)); high=R(sp.diag(0,1))
down=R(sp.Matrix([[0,0],[2,0]])); up=down.T
corner=sp.Matrix([[0,0],[rawsymbols[2],0]])
check('raw algebra multiplication is retained',R(X)*R(Y),R(X*Y))
check('raw algebra adjoint is retained',R(X).conjugate().T,R(X.conjugate().T))
check('raw quarter negative corner is two-sided',R(corner),high*R(X)*low)
check('raw heat action is exact corner superoperator',R(X/4+(ah-sp.Rational(1,4))*corner),
      R(X)/4+(ah-sp.Rational(1,4))*high*R(X)*low)
rawY=sp.Matrix([Y[0,0],Y[0,1],Y[1,0],Y[1,1]])
rawX=sp.Matrix(rawsymbols)
TX=sp.Matrix(2,2,metricT*rawX); TY=sp.Matrix(2,2,metricT*rawY)
check('forced metric original coefficient pairing in shell trace',
      sp.trace(R(TX).conjugate().T*R(TY)),3*(rawX.conjugate().T*G*rawY)[0])
ca,da,ce,df=sp.symbols('ca da ce df')
param=sp.symbols('a',real=True)
K=(down-param*up)/2
Jsheet=low-high
rp=ca*sp.eye(6)+da*K
rq=ce*sp.eye(6)+df*K
rp_sharp=sp.conjugate(ca)*sp.eye(6)-sp.conjugate(da)*K
check('quadratic relation in original sheet matrix embedding',K*K,-param*sp.eye(6))
check('quadratic algebra product in sheet representation',rp*rq,
      (ca*ce-param*da*df)*sp.eye(6)+(ca*df+da*ce)*K)
check('original reflected involution is coefficient conjugation and sheet sign',
      Jsheet*rp.conjugate()*Jsheet,rp_sharp)
check('full reflected regular trace keeps all three rotations',sp.trace(rp_sharp*rq),
      6*(sp.conjugate(ca)*ce+param*sp.conjugate(da)*df))
check('quadratic generator collision is exact original blade half',K.subs(param,0),down/2)

# Original displayed segment/triangle/tetrahedron synthesis coordinates,
# as retained by the ES source verification script and Figure 10.
figureS={
    1:sp.Matrix([[1,-1]]),
    2:sp.Matrix([[1,-sp.Rational(1,2),-sp.Rational(1,2)],
                 [0,sp.sqrt(3)/2,-sp.sqrt(3)/2]]),
    3:sp.Matrix([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/sp.sqrt(3)
}
unitaries={}; projections={}
density={1:sp.diag(1),2:sp.diag(2,3),3:sp.diag(5,7,11)}
pull_density={}; inverse_density={}
for n in (1,2,3):
    pn=sp.eye(n+1)-sp.ones(n+1)/(n+1)
    un=sp.simplify(sp.sqrt(sp.Rational(n,n+1))*figureS[n]*pn)
    projections[n]=pn; unitaries[n]=un
    pull_density[n]=sp.simplify(un.T*density[n]*un)
    inverse_density[n]=sp.simplify(un.T*density[n].inv()*un)
    check(f'Fig10 n={n} original simplex synthesis Gram',figureS[n].T*figureS[n],
          sp.Rational(n+1,n)*pn)
    check(f'Fig10 n={n} support unitary initial projection',un.T*un,pn)
    check(f'Fig10 n={n} support unitary final projection',un*un.T,sp.eye(n))
    check(f'Fig10 n={n} density support inverse',pull_density[n]*inverse_density[n],pn)

U123=sp.diag(*[unitaries[n] for n in (1,2,3)])
P123=sp.diag(*[projections[n] for n in (1,2,3)])
d123=sp.diag(1,2,3,5,7,11)
b123=sp.simplify(U123.T*d123*U123)
binv123=sp.simplify(U123.T*d123.inv()*U123)
check('Fig10 complete support rank',sp.trace(P123),6)
check('Fig10 complete initial projection',U123.T*U123,P123)
check('Fig10 complete final projection',U123*U123.T,sp.eye(6))
check('Fig10 all three ambient constant lines retained',9-sp.trace(P123),3)
# The explicit sector table orders the target basis exactly as these six rows.
fullX=sp.Matrix(6,6,lambda i,j:(i+1)*(j+2)+sp.I*(i-j))
fullY=sp.Matrix(6,6,lambda i,j:(i-j)**2+sp.I*(i+j+1))
sourceX=sp.simplify(U123.T*fullX*U123)
sourceY=sp.simplify(U123.T*fullY*U123)
check('Fig10 full corner map inverse',U123*sourceX*U123.T,fullX)
check('Fig10 full supported product',U123*sourceX*sourceY*U123.T,fullX*fullY)
check('Fig10 full supported adjoint',U123*sourceX.conjugate().T*U123.T,fullX.conjugate().T)
check('Fig10 full Hilbert Schmidt isometry',sp.trace(sourceX.conjugate().T*sourceY),
      sp.trace(fullX.conjugate().T*fullY))
check('Fig10 full density modular transport',U123*b123*sourceX*binv123*U123.T,
      d123*fullX*d123.inv())
for n in (1,2,3):
    for m in (1,2,3):
        rect=sp.Matrix(n,m,lambda i,j:i+2*j+1+sp.I*(i-j+1))
        pulled=sp.simplify(unitaries[n].T*rect*unitaries[m])
        check(f'Fig10 {n}x{m} rectangular inverse',unitaries[n]*pulled*unitaries[m].T,rect)
        check(f'Fig10 {n}x{m} rectangular adjoint',
              unitaries[m]*pulled.conjugate().T*unitaries[n].T,rect.conjugate().T)
        check(f'Fig10 {n}x{m} rectangular modular density',
              unitaries[n]*pull_density[n]*pulled*inverse_density[m]*unitaries[m].T,
              density[n]*rect*density[m].inv())
        check(f'Fig10 {n}x{m} cross sector trace-density ratio',
              (projections[n]/n)*pulled*(m*projections[m]),sp.Rational(m,n)*pulled)
        for k in (1,2,3):
            nextrect=sp.Matrix(m,k,lambda i,j:2*i-j+1+sp.I*(i+j))
            nextpulled=sp.simplify(unitaries[m].T*nextrect*unitaries[k])
            check(f'Fig10 typed composition {n}x{m}x{k}',
                  unitaries[n]*pulled*nextpulled*unitaries[k].T,rect*nextrect)

# Every density ratio, with the exact logarithmic intertwiner on the same unit.
for i in range(6):
    for j in range(6):
        unit=sp.zeros(6); unit[i,j]=1
        sourceunit=sp.simplify(U123.T*unit*U123)
        ratio=d123[i,i]/d123[j,j]
        check(f'Fig10 full matrix unit modular ratio ({i},{j})',
              b123*sourceunit*binv123,ratio*sourceunit)

Vtriangle=sp.kronecker_product(unitaries[2].T,sp.eye(3))
ambient_bridge=sp.simplify(Vtriangle*U123)
check('two ambient presentations exact initial support',ambient_bridge.T*ambient_bridge,P123)
check('two ambient presentations exact final support',ambient_bridge*ambient_bridge.T,
      sp.kronecker_product(P2,sp.eye(3)))
sourceunit=U123.T[:,0]
kernelunit=sp.Matrix([1,1,0,0,0,0,0,0,0])/sp.sqrt(2)
through_out=sourceunit*kernelunit.T
through_back=kernelunit*sourceunit.T
shellunit=sp.zeros(6); shellunit[0,0]=1
check('ambient to kernel factor has zero image',U123*through_out*U123.T,sp.zeros(6))
check('ambient from kernel factor has zero image',U123*through_back*U123.T,sp.zeros(6))
check('ambient kernel composition has retained nonzero return',
      U123*through_out*through_back*U123.T,shellunit)
check('ambient exact multiplicativity defect',
      U123*through_out*through_back*U123.T-(U123*through_out*U123.T)*(U123*through_back*U123.T),
      U123*through_out*(sp.eye(9)-P123)*through_back*U123.T)
# Full inter-orbit corner transport, including off-diagonal orbit blocks.
orbitunit=sp.Matrix([[0,1],[0,0]])
orbitL=sp.kronecker_product(sp.eye(2),U123)
check('Fig10 full inter-orbit matrix map',
      orbitL*sp.kronecker_product(orbitunit,sourceX)*orbitL.T,
      sp.kronecker_product(orbitunit,fullX))
check('Fig10 inter-orbit adjunction reverses orbit labels',
      sp.kronecker_product(orbitunit,fullX).conjugate().T,
      sp.kronecker_product(orbitunit.T,fullX.conjugate().T))

report={'status':'passed','exact_checks':len(checks),'checks':checks,
        'scope':'Exact finite spectral, original metric, full raw algebra, quadratic receiver, reflected involution, collision pairing, blade, ambient-kernel, trace, determinant, Fig10 full and rectangular modular corner, ambient multiplicativity defect, and inclusion checks. Infinite boundedness and strong limits are proved in ESHL34--42 and ESHL62--63.'}
Path(__file__).with_name('ES_SHELL_HEAT_LIFT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'exact_checks':report['exact_checks'],'scope':report['scope']},indent=2))
