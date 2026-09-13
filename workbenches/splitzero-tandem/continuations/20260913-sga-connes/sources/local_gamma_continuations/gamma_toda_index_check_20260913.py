import sympy as s
u,S=s.symbols('u S', real=True)
Z=s.symbols('Z', positive=True)
x=s.symbols('x',real=True)
beta=s.Rational(3,2); c=s.Rational(3,2)
P=[s.Integer(1)]
for n in range(10): P.append(s.expand((1+x*x)*s.diff(P[-1],x)+beta*x*P[-1]))
checks=[]
chi=S*S+(1+2*s.I)*S+(3-s.I)
for t in [s.Rational(0),s.Rational(1,2)]:
    moms=[Z*p.subs(x,t) for p in P]
    def integral(p):
        pp=s.Poly(s.expand(p),u)
        return s.expand(sum(a*moms[j[0]] for j,a in pp.terms()))
    for n in range(1,5):
        M=s.Matrix(n,n,lambda i,j:integral((c-s.I*u)**i*(c+s.I*u)**j))
        expected=Z**n*s.prod(s.factorial(j)*s.rf(beta,j) for j in range(n))*(1+t*t)**(n*(n-1)//2)
        assert s.simplify(M.det()-expected)==0
        checks.append(('reference source determinant',str(t),n))
    for N in [1,2,3]:
        m=N-1; n=N+1
        M=s.Matrix(n,n,lambda i,j:integral((c-s.I*u)**i*(c+s.I*u)**j))
        B=s.Matrix(n,m,lambda i,j:s.expand(chi*S**j).coeff(S,i))
        J=s.Matrix(2,n,lambda i,j:s.rem(S**j,chi,S).coeff(S,i))
        R=M.inv()*J.conjugate().T*(J*M.inv()*J.conjugate().T).inv()
        C=R.row_join(B)
        assert s.simplify(C.det()-1)==0
        G=(J*M.inv()*J.conjugate().T).inv()
        Br=B.conjugate().T*M*B
        assert s.simplify(G.det()*Br.det()-M.det())==0
        relation_weight=s.expand(s.conjugate(chi.subs(S,c+s.I*u))*chi.subs(S,c+s.I*u))
        Hrel=s.Matrix(m,m,lambda i,j:integral(u**(i+j)*relation_weight))
        assert s.simplify(Hrel.det()-Br.det())==0
        checks.extend([('quotient-first determinant one',str(t),N),('source-relation-quotient determinant',str(t),N),('original S versus u relation determinant',str(t),N)])
    # h=1: the quotient matrix is empty and the relation columns are the identity.
    for N in [0,1,2]:
        M=s.Matrix(N+1,N+1,lambda i,j:integral((c-s.I*u)**i*(c+s.I*u)**j))
        B=s.eye(N+1)
        assert (B.conjugate().T*M*B).det()==M.det()
        checks.append(('empty packet source equals relation',str(t),N))
print('PASS',len(checks),'exact finite checks')
print('Parameters: k=3, lambda=1/4, beta=k*2*lambda=3/2, c=k/2=3/2; tan(theta)=0 and 1/2.')
print('Retained Z=c_lambda^k*(cos(theta))^(-beta) is symbolic positive; no mass discarded.')
print('Independent complex relation fixture chi(S)=S^2+(1+2i)S+(3-i); not asserted to be an actual zero packet.')
print('Source sizes 1..4; quotient source degrees N=1,2,3; empty-packet N=0,1,2.')
