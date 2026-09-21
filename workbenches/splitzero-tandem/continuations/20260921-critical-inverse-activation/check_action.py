"""Exact and numerical fixtures for ACTION_PROOFS.md.

Small finite polynomial fixtures test identities, not the large-k guards or
native arithmetic asymptotics. All positive sources retain their actual masses.
"""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh
import sympy as sp

ROOT = Path(__file__).resolve().parent
y = sp.symbols("y")
SEED = 20260921
rng = np.random.default_rng(SEED)
receipt = {"seed": SEED, "exact_assertions": 0, "numerical_assertions": 0,
           "exact_fixtures": [], "numerical_fixtures": [],
           "versions": {"numpy": np.__version__, "scipy": scipy.__version__,
                        "sympy": sp.__version__}}


def eq(left, right, label):
    difference = left-right
    if isinstance(difference, sp.MatrixBase):
        okay = all(sp.cancel(t) == 0 for t in difference)
    else:
        okay = sp.cancel(difference) == 0
    if not okay:
        raise AssertionError(label)
    receipt["exact_assertions"] += 1


def truth(condition, label, exact=True):
    if not condition:
        raise AssertionError(label)
    receipt["exact_assertions" if exact else "numerical_assertions"] += 1


def arr(a):
    return np.array(a.evalf(), dtype=np.complex128)


def singular_squared(A, G):
    return eigh(arr(A.T*G*A), arr(G), eigvals_only=True)


def metric_op_norm(A, G):
    return math.sqrt(max(singular_squared(A, G)))


def remainder_column(poly, relation, degree):
    rem = sp.Poly(sp.rem(poly, relation, y), y)
    return sp.Matrix([rem.nth(i) for i in range(degree)])


def schur(H, common, rest):
    if not rest:
        return sp.zeros(0)
    RR = H.extract(rest, rest)
    if not common:
        return RR
    return RR-H.extract(rest, common)*H.extract(common, common).inv()*H.extract(common, rest)


def det_empty(H):
    return H.det() if H.rows else sp.S.One


def original_polynomial_fixtures():
    delta, gamma = sp.Rational(1,4), sp.Integer(3)
    roots = [b*gamma + a*sp.I*delta for a in [-1,1] for b in [-1,1]]
    Q = sp.Poly(sp.expand(sp.prod(y-z for z in roots)), y)
    q = Q.degree()
    M = sp.Matrix.hstack(*[remainder_column(y**(j+1),Q.as_expr(),q) for j in range(q)])
    T = M.inv()
    one = sp.eye(q)[:,0]
    inv = T*one
    source_rows = []
    for N in [q-1,q]:
        nodes = [sp.Integer(t) for t in [-3,-2,-1,0,1,2,3]]
        weights = [sp.Integer(t) for t in [1,2,4,3,2,1,5]]
        source_mass = sum(weights)
        moment = sp.Matrix(N+1,N+1,lambda i,j:sum(w*x**(i+j) for x,w in zip(nodes,weights)))
        J = sp.Matrix.hstack(*[remainder_column(y**j,Q.as_expr(),q) for j in range(N+1)])
        G0 = (J*moment.inv()*J.T).inv()
        R = moment.inv()*J.T*G0
        Div = sp.zeros(N+1)
        for j in range(1,N+1):
            Div[j-1,j] = 1
        B = J*Div*R
        ell = R[0,:]
        eq(J*R,sp.eye(q),"actual minimum section")
        eq(R.T*moment*R,G0,"section isometry retaining source mass")
        eq(T,B+inv*ell,"original polynomial inverse")
        rel_vector = remainder_column((Q.as_expr()-Q.nth(0))/y,Q.as_expr(),q)
        eq(rel_vector,-Q.nth(0)*inv,"original relation-vector factor")
        Omega = sp.Matrix([[1,0],[0,1],[1,1],[2,-1]])
        G1 = (G0.inv()+Omega*Omega.T).inv()
        Lmb = sp.Matrix([[1,0,1,0],[0,1,0,0],[0,0,0,1]])
        numerical_residual_bound = max(metric_op_norm(B,G0),metric_op_norm(T,G1))
        for alpha in [sp.S.Zero,sp.Rational(1,3),sp.S.One]:
            G = ((1-alpha)*G0.inv()+alpha*G1.inv()).inv()
            Ba = (1-alpha)*B*G0.inv()*G+alpha*T*G1.inv()*G
            row = (1-alpha)*ell*G0.inv()*G
            eq(T,Ba+inv*row,"exact activated inverse row")
            JJ = (sp.sqrt(1-alpha)*sp.eye(q)).row_join(sp.sqrt(alpha)*sp.eye(q))
            Jadj = (sp.sqrt(1-alpha)*G0.inv()*G).col_join(sp.sqrt(alpha)*G1.inv()*G)
            eq(JJ*Jadj,sp.eye(q),"covariance coisometry")
            eq(Jadj.T*sp.diag(G0,G1)*Jadj,G,"coisometry adjoint isometry")
            eq(JJ*sp.diag(B,T)*Jadj,Ba,"bounded residual is literal compression")
            truth(metric_op_norm(Ba,G)<=numerical_residual_bound*(1+3e-9),
                  "residual norm coisometry bound",exact=False)
            sig = np.sqrt(np.maximum(singular_squared(T,G),0))[::-1]
            truth(sig[1]<=numerical_residual_bound*(1+3e-9),
                  "all remaining inverse singular directions",exact=False)
            QB = (Lmb*G.inv()*Lmb.T).inv()
            LB = G.inv()*Lmb.T*QB
            eq(Lmb*LB,sp.eye(3),"full original observation minimum")
            eq(LB.T*G*LB,QB,"observed section isometry")
            PB = LB*Lmb
            eq(PB*PB,PB,"original observed projection")
            # Literal r=2, v=1 inverse source: [y^-1], [y^-3].
            W = inv.row_join(T**3*one)
            Y = (M*one).row_join(inv)
            eq(M**2*W,Y,"actual M^(v+1) arithmetic columns")
            Fs, Ft = Lmb*W, Lmb*Y
            truth(Fs.rank()==2 and Ft.rank()==2,"actual observed source and target injective")
            S, V = Fs.T*QB*Fs, Ft.T*QB*Ft
            K, cross = V[1:,1:],V[1:,0]
            cc = K.inv()*cross
            rho = (V[0,0]-(cross.T*K.inv()*cross)[0])
            shear = sp.eye(2)
            shear[1,0] = cc[0]
            eq(V,shear.T*sp.diag(rho,K)*shear,"full observed shear congruence")
            eq(V.det()/S.det(),rho*K.det()/S.det(),"actual exterior-volume ratio")
            a = sp.Rational(2,7)
            C = G.inv()
            P = G0.det()*(a*C+M*C*M.T).det()
            Pzero = G0.det()*(M*C*M.T).det()
            Mdag = G.inv()*M.T*G
            Tdag = G.inv()*T.T*G
            D = G0.det()/G.det()
            eq(P/D,(a*sp.eye(q)+Mdag*M).det(),"complete dual spectral pencil")
            eq(Pzero,T.det()**(-2)*D,"zero polynomial keeps source determinant")
            eq(P/Pzero,(sp.eye(q)+a*Tdag*T).det(),"small-regularizer inverse edge")
            Pcanonical = G0.det()*(a*G0.inv()+M*G0.inv()*M.T).det()
            edgecanonical = (sp.eye(q)+a*G0.inv()*T.T*G0*T).det()
            eq(P/Pcanonical/D,
               (sp.eye(q)+a*Tdag*T).det()/edgecanonical,
               "full two-metric source-cost receiver")
            vals = singular_squared(T,G)
            exactlog = sum(math.log1p(float(a)*x) for x in vals)
            lead = math.log1p(float(a)*max(vals))
            truth(-1e-10<=exactlog-lead <= (q-1)*float(a)*numerical_residual_bound**2+1e-8,
                  "finite small-regularizer remainder",exact=False)
        source_rows.append({"N":N,"q":q,"source_mass":str(source_mass),
                            "cutoffs_checked":[0,"1/3",1]})
    receipt["exact_fixtures"].append({"original_polynomial_quotient":source_rows,
        "scope":"Quartet k=1 polynomial identities with a positive rational discrete source and a selected onto 3-by-4 observation matrix. These are finite algebra fixtures, not a native tensor observation, original-Gamma moment calculation, or asymptotic claim."})


def conductor_fixtures():
    delta,gamma = sp.Rational(1,4),sp.Integer(3)
    k = 13
    lowk = k-8
    lower = [(2*b-lowk)*gamma-sp.I*(2*a-lowk)*delta
             for a in range(lowk+1) for b in range(lowk+1)]
    upper = {(2*b-k)*gamma-sp.I*(2*a-k)*delta for a in range(k+1) for b in range(k+1)}
    rows = []
    for v in range(4):
        coeff = [(-1)**(v-j)*sp.binomial(v,j) for j in range(v+1)]
        shifts = [4+(2*j-8)*delta-sp.I*8*gamma for j in range(v+1)]
        poles = [sp.I*(bj-4) for bj in shifts]
        moments = [sp.expand(sum(aa*bb**m for aa,bb in zip(coeff,shifts))) for m in range(v+1)]
        for m in range(v):
            eq(moments[m],0,"actual first symbol moment")
        truth(moments[v]!=0,"selected moment is nonzero")
        CApoly = sp.expand(sum(aa*(y-zz)**v for aa,zz in zip(coeff,poles)))
        eq(CApoly,sp.I**(-v)*moments[v],"original coordinate phase")
        for node in lower:
            for zz in poles:
                truth(sp.expand(node-zz) in upper,"shifted lower root is original upper root")
        r = 2
        L = (v+1)*(r-1)
        B = sp.Poly(sp.prod((y-zz)**(r-1) for zz in poles),y)
        numerator = sp.Poly(CApoly*B.as_expr()+
                    sum(aa*sp.div(B.as_expr(),y-zz,y)[0] for aa,zz in zip(coeff,poles)),y)
        eq(numerator.LC(),sp.I**(-v)*moments[v],"proper rational terms preserve leading coefficient")
        selected = lower[:L+1]
        recovered = sum(numerator.eval(z)/sp.prod(z-w for w in selected if w!=z) for z in selected)
        eq(recovered,sp.I**(-v)*moments[v],"exact lower-root leading-coefficient recovery")
        truth(all(B.eval(z)!=0 for z in selected),"period/pole guard")
        rows.append({"v":v,"J":v+1,"L":L,"lower_dimension":len(lower),"moment":str(moments[v])})
    receipt["exact_fixtures"].append({"conductor_phase_and_original_grid":rows})


def common_subspace_and_shear():
    rows = []
    for v,r in [(0,4),(1,5),(3,3),(2,1)]:
        dim = r+v
        X = sp.Matrix(dim,dim,lambda i,j:sp.Integer(((i+2)*(j+3)+i-j)%7-3))
        H = 100*(X.T*X+sp.eye(dim))
        I = list(range(r-1))
        J = [0]+list(range(v+1,v+r))
        C = sorted(set(I)&set(J))
        Ri = [j for j in I if j not in C]
        Rj = [j for j in J if j not in C]
        HI,HJ,HC = H.extract(I,I),H.extract(J,J),H.extract(C,C)
        SI,SJ = schur(H,C,Ri),schur(H,C,Rj)
        eq(det_empty(HI),det_empty(HC)*det_empty(SI),"first common-subspace determinant")
        eq(det_empty(HJ),det_empty(HC)*det_empty(SJ),"second common-subspace determinant")
        truth(len(Rj)==len(Ri)+1 and len(Rj)+len(Ri)<=2*v+1,
              "exact complementary-dimension count")
        rho = sp.Rational(3,2)
        c = sp.Matrix([sp.Rational(j+1,1000) for j in range(r-1)])
        sh = sp.eye(r)
        for j in range(r-1):
            sh[j+1,0]=c[j]
        target = sh.T*sp.diag(rho,HI)*sh
        eq(target.det()/HJ.det(),
           rho*det_empty(SI)/det_empty(SJ),"full action determinant cancels common part")
        if r>1:
            aa=target[0,0]
            checkval=(c.T*c)[0]
            lowerK=min(eigh(arr(HI),eigvals_only=True))
            truth(float(checkval)<=float(aa)/lowerK+1e-14,"whole-column shear bound",exact=False)
        rows.append({"v":v,"r":r,"common_dimension":len(C),
                     "complementary_dimension_sum":len(Ri)+len(Rj)})
    h=sp.Integer(10)
    S=h*sp.eye(2)
    V=sp.Matrix([[1+h**3,h**2],[h**2,h]])
    eq(V.det()/S.det(),1/h,"counterexample retains same exterior ratio")
    eq(V[0,0]-V[0,1]**2/V[1,1],1,"counterexample retains Schur remainder")
    eq(V[1,0]/V[1,1],h,"counterexample amplified shear")
    eq(sp.trace(S.inv()*V),h**2+1+1/h,"counterexample complete squared singular sum")
    truth(sp.trace(S.inv()*V)>h**2,"counterexample cannot have both remaining scales bounded")
    receipt["exact_fixtures"].append({"common_subspace_cases":rows,
         "omitted_whole_column_counterexample":{"h":10,"squared_singular_product":"1/10",
                                              "squared_singular_sum":str(sp.trace(S.inv()*V))}})


def numerical_generalized_singular_bounds():
    worst_ratio = 0.0
    worst_heat_remainder = 0.0
    for r in [2,3,5,8]:
        for sample in range(12):
            h=10.0**rng.uniform(2,7)
            E=0.6
            low,up=math.exp(-E),math.exp(E)
            X=rng.normal(size=(r,r))
            O=np.linalg.qr(X)[0]
            S=h*(O*np.linspace(low,up,r))@O.T
            X=rng.normal(size=(r-1,r-1))
            O=np.linalg.qr(X)[0]
            K=h*(O*np.linspace(low,up,r-1))@O.T
            c=rng.normal(size=r-1)
            c=c/np.linalg.norm(c)*math.sqrt(0.8/h)
            rho=1.0
            sh=np.eye(r)
            sh[1:,0]=c
            block=np.zeros((r,r))
            block[0,0]=rho
            block[1:,1:]=K
            V=sh.T@block@sh
            dplus=V[0,0]
            chi=(math.sqrt(4+np.dot(c,c))+np.linalg.norm(c))/2
            vals=eigh(V,S,eigvals_only=True)
            dvals=eigh(block,eigvals_only=True)
            lower=dvals/(up*h*chi**2)
            upper=chi**2*dvals/(low*h)
            truth(np.all(vals>=lower*(1-1e-7)) and np.all(vals<=upper*(1+1e-7)),
                  "every generalized singular value with full shear",exact=False)
            truth(np.dot(c,c)<=dplus/(low*h)+1e-12,"shear from full low-column norm",exact=False)
            truth(vals[0]<=dplus/(low*h)*(1+1e-9),"sharper first singular upper bound",exact=False)
            truth(np.all(vals[1:]>=low/(up*chi**2)*(1-1e-9)),
                  "all r-1 inverse columns retained",exact=False)
            for tau in [0.01,1.0,h**0.5]:
                heat_sum=float(np.exp(-tau*vals).sum())
                first=math.exp(-tau*vals[0])
                remainder=(r-1)*math.exp(-tau*low/(up*chi**2))
                truth(-1e-12<=heat_sum-first<=remainder+1e-10,
                      "complete observed arithmetic heat remainder",exact=False)
                worst_heat_remainder=max(worst_heat_remainder,heat_sum-first-remainder)
            worst_ratio=max(worst_ratio,float(max(vals/upper)),float(max(lower/vals)))
    receipt["numerical_fixtures"].append({"generalized_action_samples":48,
       "bound_ratio_max":worst_ratio,"heat_remainder_violation_max":worst_heat_remainder})


def numerical_guarded_relative_heat():
    cases = 0
    smallest_guard_ratio = float("inf")
    for q in [3,4,6]:
        B=np.diag(np.linspace(0.5,1.0,q))
        u=np.eye(q)[:,0]
        row=np.zeros(q)
        row[1:]=np.linspace(40,100,q-1)
        T=B+np.outer(u,row)
        Z=rng.normal(size=(q,q))
        G=Z.T@Z+np.eye(q)
        w,O=eigh(G)
        F=(O*np.sqrt(w))@O.T
        Fi=(O/np.sqrt(w))@O.T
        Tiso=F@T@Fi
        Biso=F@B@Fi
        D=np.linalg.norm(Biso,2)
        left,sing,_=np.linalg.svd(Tiso)
        L=sing[0]
        truth(L>D,"relative heat finite guard",exact=False)
        smallest_guard_ratio=min(smallest_guard_ratio,L/D)
        ui=F@u
        Pu=np.outer(ui,ui)/np.dot(ui,ui)
        Pmin=np.outer(left[:,0],left[:,0])
        trace_norm=float(np.linalg.svd(Pmin-Pu,compute_uv=False).sum())
        truth(trace_norm<=2*D/L+1e-12,"minimum singular projector angle",exact=False)
        Lambda=np.eye(q)[:-1,:]
        Lambda[0,-1]=1
        QB=np.linalg.inv(Lambda@np.linalg.inv(G)@Lambda.T)
        PB=np.linalg.inv(G)@Lambda.T@QB@Lambda
        PBi=F@PB@Fi
        theta=float(np.trace(PBi@Pu))
        Mi=np.linalg.inv(Tiso)
        vals,V=eigh(Mi.T@Mi)
        small=1/(L*L)
        for tau in [0.01,1.0,20.0]:
            heat=(V*np.exp(-tau*vals))@V.T
            observed=float(np.trace(PBi@heat))
            relative=abs(observed/(theta*math.exp(-tau*small))-1)
            bound=2*D*math.sqrt(small)/theta+(q-1)/theta*math.exp(-tau*(D**-2-small))
            truth(relative<=bound+1e-8,"retained measured full-heat estimate",exact=False)
            cases+=1
    receipt["numerical_fixtures"].append({"guarded_relative_full_heat_cases":cases,
        "smallest_inverse_norm_over_residual_bound":smallest_guard_ratio,
        "scope":"Nonnormal finite rank-one inverse fixtures in nonidentity metrics, with the full observed projection."})


if __name__=="__main__":
    original_polynomial_fixtures()
    conductor_fixtures()
    common_subspace_and_shear()
    numerical_generalized_singular_bounds()
    numerical_guarded_relative_heat()
    receipt["status"]="PASS"
    receipt["scope"]="Exact finite identities and numerical inequalities; no new native moment asymptotic or large-k numerical certificate."
    (ROOT/"ACTION_CHECK_RESULTS.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(receipt,indent=2))
