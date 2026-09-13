#!/usr/bin/env python3
"""Exact finite regressions for the marked-product/four-endpoint note.
These fixtures are not asserted zeta packets and are not Lean certificates.
"""
import argparse, json, sys, unittest
from pathlib import Path
import sympy as s
I=s.I

def zero(X):
    if isinstance(X,s.MatrixBase): return all(s.simplify(v)==0 for v in X)
    return s.simplify(X)==0

def require(condition, text):
    if not condition: raise AssertionError(text)

def gram(nodes,weights,N,c=s.Rational(1,2)):
    V=s.Matrix([[(c+I*x)**j for j in range(N+1)] for x in nodes])
    return s.simplify(s.conjugate(V.T)*s.diag(*weights)*V)

def quotient_matrices(M,chi,z):
    N=M.rows-1; q=s.degree(chi,z)
    J=s.Matrix([[s.Poly(s.rem(z**j,chi,z),z).nth(i) for j in range(N+1)] for i in range(q)])
    cols=[]
    for j in range(N-q+1):
        P=s.Poly(s.expand(chi*z**j),z)
        cols.append(s.Matrix([P.nth(i) for i in range(N+1)]))
    B=s.Matrix.hstack(*cols) if cols else s.zeros(N+1,0)
    G=s.simplify((J*M.inv()*s.conjugate(J.T)).inv())
    C=s.simplify(M.inv()*s.conjugate(J.T)*G)
    return J,B,G,C

def trace_derivative(M,Delta,chi,z):
    J,B,G,C=quotient_matrices(M,chi,z)
    value=s.trace(G.inv()*s.conjugate(C.T)*Delta*C)
    return s.simplify(value)

class ExactTests(unittest.TestCase):
    def test_split_pair_observations(self):
        for modulus in (5,7):
            vals=[None]+list(range(modulus))
            def obs(x): return (0,0) if x is None else (x,1)
            def add(x,y): return y if x is None else x if y is None else (x+y)%modulus
            def mul(x,y): return None if x is None or y is None else (x*y)%modulus
            require(len({obs(x) for x in vals})==len(vals),'joint observations must be injective')
            for x in vals:
                for y in vals:
                    ax,bx=obs(x); ay,by=obs(y)
                    require(obs(add(x,y))==((ax+ay)%modulus,int(bool(bx or by))),'addition observation')
                    require(obs(mul(x,y))==((ax*ay)%modulus,bx*by),'multiplication observation')
            require(None!=0,'supported zero remains distinct')
    def test_base_word_relations(self):
        require(sum([1,1])!=sum([1]),'base must not acquire Boolean addition')
        require(sum([])==sum([0]),'empty word relation')
    def test_original_theta_seed(self):
        x=s.symbols('x',positive=True)
        f=s.exp(-s.pi*x*x); D=lambda g:-x*s.diff(g,x)
        expected=(4*s.pi**2*x**4-6*s.pi*x*x)*f
        require(zero(D(D(f))-D(f)-expected),'seed and Laplacian sign')
    def test_logarithmic_commutator(self):
        x=s.symbols('x',positive=True); f=s.Function('f')(x)
        D=lambda g:-x*s.diff(g,x)
        require(zero(s.log(x)*D(f)-D(s.log(x)*f)-f),'[log x,D]=1')
    def test_external_differential_commutes(self):
        x,y,u,t1,t2=s.symbols('x y u t1 t2')
        h=lambda x:x*x+x+2
        D1=lambda P:u*s.diff(P,x)+(h(x)-t1)*P
        D2=lambda P:u*s.diff(P,y)+(h(y)-t2)*P
        for P in (1,x*y,x*x+y**3):
            require(zero(D1(D2(P))-D2(D1(P))),'commuting coefficient operators')
    def test_product_relation_and_parameter_defect(self):
        x,y,u,t1,t2=s.symbols('x y u t1 t2')
        h1=x*x+1; h2=y*y+1; S=x+y
        P=s.expand(S*(S*S+4))
        qs,rem=s.reduced(P,[h1,h2],x,y)
        require(rem==0,'actual cyclic relation')
        Q1,Q2=qs
        full=u*(s.diff(Q1,x)+s.diff(Q2,y))+(h1-t1)*Q1+(h2-t2)*Q2
        require(zero(full-P-u*(s.diff(Q1,x)+s.diff(Q2,y))+t1*Q1+t2*Q2),'parameter correction')
    def test_repeated_product_fibre(self):
        N=s.Matrix([[0,0],[1,0]])
        A=s.eye(2)+N
        Ak=s.kronecker_product(A,s.eye(2))+s.kronecker_product(s.eye(2),A)
        require(zero((Ak-2*s.eye(4))**3),'full maximal nilpotent length')
        require(not zero((Ak-2*s.eye(4))**2),'second jet must survive')
    def test_nilpotent_exponential_product(self):
        z=s.symbols('z'); N=s.Matrix([[0,0,0],[1,0,0],[0,1,0]])
        E=s.eye(3)+z*N+z*z*N*N/2
        NN=s.kronecker_product(N,s.eye(3))+s.kronecker_product(s.eye(3),N)
        EE=s.zeros(9)
        for j in range(5): EE+=z**j*NN**j/s.factorial(j)
        require(zero(s.kronecker_product(E,E)-EE),'all nilpotent exponential factors')
    def test_mixed_source_quotient_and_relation_derivative(self):
        z=s.symbols('z'); chi=z*z-z+2
        nodes=list(range(-3,4)); w0=[s.Integer(2)]*7; w1=[s.Integer(2+x*x) for x in nodes]
        M0=gram(nodes,w0,3); M1=gram(nodes,w1,3); Delta=M1-M0
        M=M0+Delta/3
        J,B,G,C=quotient_matrices(M,chi,z)
        Cp=-B*(s.conjugate(B.T)*M*B).inv()*s.conjugate(B.T)*Delta*C
        require(zero(J*C-s.eye(2)),'same full remainder')
        require(zero(J*Cp),'derivative is an original relation')
        require(zero(s.conjugate(B.T)*M*C),'canonical orthogonality')
        require(zero(s.conjugate(B.T)*M*Cp+s.conjugate(B.T)*Delta*C),'differentiated orthogonality')
        Gp=s.conjugate(C.T)*Delta*C
        require(zero(s.conjugate(Cp.T)*M*C+s.conjugate(C.T)*M*Cp),'discarded terms are exactly zero')
        Gpp=s.conjugate(Cp.T)*Delta*C+s.conjugate(C.T)*Delta*Cp
        target=-2*s.conjugate(C.T)*Delta*B*(s.conjugate(B.T)*M*B).inv()*s.conjugate(B.T)*Delta*C
        require(zero(Gpp-target),'complete negative relation Gram')
    def test_signed_kernel_mass(self):
        z=s.symbols('z'); chi=z*z-z+2
        nodes=list(range(-3,4)); w=[s.Integer(x*x+3) for x in nodes]
        data={}
        for N in (1,2,3,4):
            M=gram(nodes,w,N); J,B,G,C=quotient_matrices(M,chi,z)
            residual=M.inv()-(B*(s.conjugate(B.T)*M*B).inv()*s.conjugate(B.T) if B.cols else s.zeros(N+1))
            require(zero(residual-C*G.inv()*s.conjugate(C.T)),'kernel subtraction')
            vals=[]
            for node in nodes:
                v=s.Matrix([[(s.Rational(1,2)+I*node)**j for j in range(N+1)]])
                vals.append(s.simplify((v*residual*s.conjugate(v.T))[0]))
            require(zero(sum(wt*value for wt,value in zip(w,vals))-2),'residual mass is original q')
            data[N]=vals
        require(zero(sum(w[j]*(data[1][j]+data[2][j]-data[3][j]-data[4][j]) for j in range(7))),'signed mass cancellation')
    def test_signed_derivative_schur(self):
        z=s.symbols('z'); chi=z*z-z+2
        nodes=list(range(-3,4)); w0=[s.Integer(1)]*7; w1=[s.Integer(2+x*x) for x in nodes]
        signed=s.Integer(0); signed_other=s.Integer(0)
        for N,sgn in ((1,1),(2,1),(3,-1),(4,-1)):
            M0=gram(nodes,w0,N); M1=gram(nodes,w1,N); Delta=M1-M0; M=M0+Delta*s.Rational(2,5)
            J,B,G,C=quotient_matrices(M,chi,z)
            a=s.trace(G.inv()*s.conjugate(C.T)*Delta*C)
            b=s.trace(M.inv()*Delta)
            if B.cols: b-=s.trace((s.conjugate(B.T)*M*B).inv()*s.conjugate(B.T)*Delta*B)
            require(zero(a-b),'source/relation trace equals original quotient derivative')
            signed+=sgn*a; signed_other+=sgn*b
        require(zero(signed-signed_other),'all endpoint signs retained')
    def test_gamma_moments_and_pair_formula(self):
        x=s.symbols('x'); ser=s.series(s.cos(x)**s.Rational(-1,2),x,0,10).removeO().expand()
        moments=[s.factorial(2*j)*ser.coeff(x,2*j) for j in range(5)]
        require(moments==[1,s.Rational(1,2),s.Rational(7,4),s.Rational(139,8),s.Rational(5473,16)],'literal Gamma moment ratios')
        a=s.symbols('a0:5'); b=s.symbols('b0:3'); E3=s.Matrix([[a[0],a[1],a[2]],[a[1],a[2],a[3]],[a[2],a[3],a[4]]]).det()
        v1=a[0]*a[1]
        v2=a[1]*(a[0]*a[2]-a[1]**2)/b[0]
        v3=(a[0]*a[2]-a[1]**2)*(a[1]*a[3]-a[2]**2)/(b[0]*b[1])
        v4=E3*(a[1]*a[3]-a[2]**2)/(b[1]*(b[0]*b[2]-b[1]**2))
        ratio=a[0]*a[1]**2*b[1]**2*(b[0]*b[2]-b[1]**2)/(E3*(a[1]*a[3]-a[2]**2)**2)
        require(zero(v1*v2/(v3*v4)-ratio),'pair four-volume formula')
    def test_holonomy_relation_variance(self):
        e=s.Rational(2,5); M=7*s.eye(2); J=s.Matrix([[1,0]])
        G=(J*M.inv()*J.T).inv(); C=M.inv()*J.T*G
        gs=[]; defects=[]
        for sign in (-1,1):
            Mt=7*s.Matrix([[1,sign*e],[sign*e,1]])
            Gt=(J*Mt.inv()*J.T).inv(); Ct=Mt.inv()*J.T*Gt
            gs.append(Gt); defects.append((C-Ct).T*Mt*(C-Ct))
        require(zero(G-(gs[0]+gs[1])/2-(defects[0]+defects[1])/2),'retained gluing norm')
        require(zero((gs[0]+gs[1])/2-(1-e*e)*G),'quadratic sharpness')
    def test_period_metric_transport(self):
        G=s.Matrix([[7,1+I],[1-I,5]])
        P=s.Matrix([[1,1+I],[I,2]])
        A=s.Matrix([[0,-2],[1,1]])
        W=s.conjugate(A.T)*G+G*A-G
        Gt=s.conjugate(P.inv().T)*G*P.inv()
        Wt=s.conjugate(P.inv().T)*W*P.inv()
        require(zero(Gt.inv()*Wt-P*G.inv()*W*P.inv()),'metric and action transported together')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--negative',action='store_true');parser.add_argument('--receipt')
    args=parser.parse_args()
    if args.negative:
        # A represented zero is not absence. This fails at the claimed equality,
        # not because of an unavailable dependency.
        require(('supported',0)==('absent',None),'deliberate false identification e=tau rejected')
        return
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactTests)
    result=unittest.TextTestRunner(stream=sys.stderr,verbosity=2).run(suite)
    payload={'scope':'exact finite symbolic regressions; not zeta samples, interval proofs, or Lean checks',
             'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
             'successful':result.wasSuccessful()}
    text=json.dumps(payload,sort_keys=True,indent=2)
    print(text)
    if args.receipt: Path(args.receipt).write_text(text+'\n')
    if not result.wasSuccessful(): sys.exit(1)
if __name__=='__main__':main()
