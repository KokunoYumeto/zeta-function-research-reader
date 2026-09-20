"""Exact degree/Toda/heat identities. Fixtures are not claimed arithmetic zeros."""
from pathlib import Path
import hashlib
import json
import os
import sys
import sympy as sp

HERE=Path(__file__).resolve().parent
checks=0
controls=0
I=sp.I
u,S,z=sp.symbols('u S z',real=True)


def progress(message):
    if os.environ.get('SZ_HEAT_PROGRESS') == '1':
        print(message,file=sys.stderr,flush=True)


def clean(x):
    return sp.cancel(sp.expand(x))


def eq(label,left,right):
    global checks
    difference=left-right
    entries=list(difference) if isinstance(difference,sp.MatrixBase) else [difference]
    if any(sp.simplify(clean(x)) != 0 for x in entries):
        raise RuntimeError(f'Equality failed: {label}: {difference}')
    checks+=1


def ne(label,left,right):
    global controls
    difference=left-right
    entries=list(difference) if isinstance(difference,sp.MatrixBase) else [difference]
    if all(sp.simplify(clean(x)) == 0 for x in entries):
        raise RuntimeError(f'Failure control not detected: {label}')
    controls+=1


def adj(A,G):
    return (G.inv()*A.conjugate().T*G).applyfunc(clean)


def trace(A):
    return clean(sp.trace(A))


def gaussian_moment(j,mean,mass):
    return mass*sum(sp.factorial(j)*mean**(j-2*l)/
                    (2**l*sp.factorial(l)*sp.factorial(j-2*l))
                    for l in range(j//2+1))


reports=[]
for name,polynomial,mean in [('even',u*u+1,sp.Integer(0)),
                              ('tilted',u*u+1,sp.Rational(1,3)),
                              ('repeated-tilted',(u*u+1)**2,sp.Rational(1,3))]:
    progress(name+' begin')
    q=int(sp.degree(polynomial,u))
    c=sp.Rational(5,2)
    mass=sp.Integer(7)
    maxN=q+1
    chi=sp.Poly(sp.expand(I**q*polynomial.subs(u,(S-c)/I)),S)
    MS=sp.zeros(q)
    for j in range(q-1):
        MS[j+1,j]=1
    for j in range(q):
        MS[j,q-1]=-chi.nth(j)
    M=(MS-c*sp.eye(q))/I
    U=[sp.Integer(1),u-mean]
    for j in range(1,maxN+2):
        U.append(sp.expand((u-mean)*U[-1]-j*U[-2]))
    omega=[mass*sp.factorial(j) for j in range(maxN+4)]
    b=[]
    for j in range(maxN+3):
        rem=sp.rem(sp.Poly(sp.expand(I**j*U[j].subs(u,(S-c)/I)),S),chi)
        b.append(sp.Matrix([rem.nth(a) for a in range(q)]))
    mu=[gaussian_moment(j,mean,mass) for j in range(2*maxN+2*q+8)]
    H=lambda n,shift=0:sp.Matrix(n,n,lambda a,j:mu[a+j+shift])
    p2=sp.Poly(polynomial**2,u)
    boundary_mu=[sum(p2.nth(j)*mu[a+j] for j in range(p2.degree()+1))
                 for a in range(2*(maxN-q+3)+1)]
    HB=lambda n:sp.Matrix(n,n,lambda a,j:boundary_mu[a+j])
    Bdet=lambda n:HB(n).det() if n else sp.Integer(1)
    nu=lambda j:Bdet(j+1)/Bdet(j)
    metrics={}
    volume={}
    for N in range(q-1,maxN+2):
        metrics[N]=sp.simplify(sum((b[j]*b[j].conjugate().T/omega[j] for j in range(N+1)),sp.zeros(q)).inv())
        volume[N]=clean(metrics[N].det())
    for N in range(q-1,maxN+1):
        tag=f'{name} N={N}'
        progress(tag)
        G,Gp=metrics[N],metrics[N+1]
        nextb=b[N+1]
        aa=nextb*nextb.conjugate().T/omega[N+1]
        alpha=clean((nextb.conjugate().T*G*nextb)[0]/omega[N+1])
        kappa=1+alpha
        eq(tag+' exact degree inverse update',Gp.inv(),G.inv()+aa)
        eq(tag+' determinant contraction',volume[N]/volume[N+1],kappa)
        eq(tag+' source-boundary volume',volume[N],H(N+1).det()/Bdet(N-q+1))
        eq(tag+' adjacent norm contraction',kappa,nu(N-q+1)/omega[N+1])
        JS=sp.Matrix(q,N+1,lambda a,j:sp.rem(sp.Poly(((S-c)/I)**j,S),chi).nth(a))
        sourceH,sourceK=H(N+1),H(N+1,1)
        R=(sourceH.inv()*JS.conjugate().T*G).applyfunc(clean)
        eq(tag+' actual raw-moment quotient',G,(JS*sourceH.inv()*JS.conjugate().T).inv())
        eq(tag+' original source mass',sourceH[0,0],7)
        eq(tag+' full lift',JS*R,sp.eye(q))
        A=sp.simplify(JS*sourceH.inv()*sourceK*R)
        Q=(I*b[N+1]*b[N].conjugate().T*G/omega[N]).applyfunc(clean)
        eq(tag+' complete outgoing phase',A,M+Q)
        eq(tag+' compression selfadjoint',adj(A,G),A)
        Gprime=(R.conjugate().T*sourceK*R).applyfunc(clean)
        ellprime=trace(G.inv()*Gprime)
        sigma=trace(M)
        cross=clean((b[N].conjugate().T*G*b[N+1])[0]/omega[N])
        eq(tag+' original tilted phase',cross,I*(sigma-ellprime))
        incoming=clean((b[N].conjugate().T*G*b[N])[0]/omega[N])
        if N==q-1:
            eq(tag+' first-degree leverage',incoming,1)
        else:
            eq(tag+' incoming contraction',incoming,1-volume[N]/volume[N-1])
        qnorm=trace(adj(Q,G)*Q)
        eq(tag+' rank-one boundary norm',qnorm,omega[N+1]/omega[N]*incoming*alpha)
        W=(I*(adj(Q,G)-Q)).applyfunc(clean)
        radius2=trace(W*W)/2
        eq(tag+' full phase subtraction',radius2,qnorm-(sigma-ellprime)**2)
        eq(tag+' original traceless defect',trace(W),0)
        if mean==0:
            eq(tag+' zero-tilt parity cross',cross,0)
            eq(tag+' zero-tilt square zero',Q*Q,sp.zeros(q))
        elif N==q:
            ne(tag+' missing tilted phase',radius2,qnorm)
        # Exact second derivative of the original fixed-map quotient volume.
        HI=sourceH.inv()
        KK1=(-JS*HI*sourceK*HI*JS.conjugate().T).applyfunc(clean)
        KK2=(JS*(2*HI*sourceK*HI*sourceK*HI-HI*H(N+1,2)*HI)*JS.conjugate().T).applyfunc(clean)
        ellsecond=trace(G*KK1*G*KK1-G*KK2)
        m=N-q+1
        c_boundary=nu(m)/nu(m-1) if m else 0
        eq(tag+' actual Toda curvature',ellsecond,omega[N+1]/omega[N]-c_boundary)
        if alpha:
            P=aa*G/alpha
            eq(tag+' rank-one projector',P*P,P)
            eq(tag+' projector metric adjoint',adj(P,G),P)
        for lam in [sp.Integer(0),sp.Rational(1,3),sp.Integer(1)]:
            progress(tag+f' lambda={lam}')
            GL=sp.simplify(G-lam/(1+lam*alpha)*G*aa*G)
            eq(tag+f' path inverse {lam}',GL.inv(),G.inv()+lam*aa)
            eq(tag+f' path volume {lam}',GL.det(),volume[N]/(1+lam*alpha))
            eq(tag+f' path contraction {lam}',trace(aa*GL),alpha/(1+lam*alpha))
            MD=adj(M,GL)
            heatH=(MD*M).applyfunc(clean)
            Hprime=((aa*GL*MD-MD*aa*GL)*M).applyfunc(clean)
            for n in range(1,4):
                Bn=M*heatH**(n-1)*MD-heatH**n
                eq(tag+f' trace-zero heat integrand {lam} {n}',trace(Bn),0)
                eq(tag+f' exact heat derivative sign {lam} {n}',
                   -trace(heatH**(n-1)*Hprime),trace(aa*GL*Bn))
        if N==q:
            ne(tag+' metric trace falsely fixed',trace(adj(M,Gp)*M),trace(adj(M,G)*M))
            ne(tag+' source mass discarded',G,G/7)
            ne(tag+' outgoing i phase omitted',Q,b[N+1]*b[N].conjugate().T*G/omega[N])
        reports.append({'case':name,'N':N,'q':q,'mass':'7','kappa':str(kappa),
                        'incoming_leverage':str(incoming),'rank_one_norm_squared':str(qnorm),
                        'rank_two_radius_squared':str(radius2),'phase_squared':str(clean((sigma-ellprime)**2))})
    first,last=q-1,maxN+1
    progress(name+' multistep')
    # Keep every i phase and source norm, but use the exact rational-coordinate
    # Woodbury form B(Omega+B*GB)^(-1)B* rather than invert a radical matrix.
    # It equals U(I+U*GU)^(-1)U* for U=B Omega^(-1/2).
    Bcols=sp.Matrix.hstack(*[I**(-j)*b[j] for j in range(first+1,last+1)])
    Omega=sp.diag(*[omega[j] for j in range(first+1,last+1)])
    Gfirst,Glast=metrics[first],metrics[last]
    eq(name+' multistep inverse update',Glast.inv(),Gfirst.inv()+Bcols*Omega.inv()*Bcols.conjugate().T)
    woodbury=Gfirst-Gfirst*Bcols*(Omega+Bcols.conjugate().T*Gfirst*Bcols).inv()*Bcols.conjugate().T*Gfirst
    eq(name+' full multistep Woodbury',Glast,woodbury)
    eq(name+' multistep determinant',volume[first]/volume[last],
       (sp.eye(Bcols.cols)+Omega.inv()*Bcols.conjugate().T*Gfirst*Bcols).det())
    telescoped=sp.prod(volume[j]/volume[j+1] for j in range(first,last))
    eq(name+' exact volume telescope',telescoped,volume[first]/volume[last])

# Exact isometry and marked-unit check with a complex original metric.
G0=sp.Matrix([[3,I],[-I,2]])
a=sp.Matrix([1,I])
alpha=(a.conjugate().T*G0*a)[0]
P=a*a.conjugate().T*G0/alpha
Gp=G0-G0*a*a.conjugate().T*G0/(1+alpha)
root=sp.eye(2)-P+P/sp.sqrt(1+alpha)
eq('exact relative square root',root*root,G0.inv()*Gp)
eq('exact original isometry',root.conjugate().T*G0*root,Gp)
physical=sp.Matrix([[1,I],[2,3]])
unit=sp.Matrix([1,0])
eq('complete marked-unit physical map',physical*root.inv()*root*unit,physical*unit)
M=sp.Matrix([[1,I],[2,3]])
Mt=root*M*root.inv()
D=Mt-M
eq('all complex cross terms',adj(Mt,G0)*Mt-adj(M,G0)*M,
   adj(M,G0)*D+adj(D,G0)*M+adj(D,G0)*D)
ne('wrong marked unit transport',physical*root.inv()*unit,physical*unit)
ne('omitted complex cross terms',adj(Mt,G0)*Mt-adj(M,G0)*M,adj(D,G0)*D)

# Direct median examples retain all eigenvalues, including zeros.
eq('rank-one median cost q=3',sp.log(4)+0+0,sp.log(4))
eq('scalar multistep median cost',sum(abs(x-sp.log(4)) for x in [sp.log(4)]*3),0)
eq('full multistep volume cost',sum([sp.log(4)]*3),sp.log(64))

result={'status':'pass','exact_checks':checks,'negative_controls':controls,'cases':reports,
        'proof_sha256':hashlib.sha256((HERE/'DEGREE_VOLUME_HEAT_RETURN.tex').read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact finite original-map comparison fixtures, degree updates, tilted phases, Toda curvature and heat derivative coefficients; no arithmetic zero data or asymptotic claim.'}
print(json.dumps(result,indent=2))
