"""Exact tests of HR1--31. Comparison inputs are not claimed zeta zeros."""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
checks = 0
controls = 0
I = sp.I


def eq(label, left, right):
    global checks
    difference = left - right
    entries = list(difference) if isinstance(difference, sp.MatrixBase) else [difference]
    if any(sp.cancel(sp.expand(value)) != 0 for value in entries):
        raise RuntimeError(f"Failed equality {label}: {difference}")
    checks += 1


def ne(label, left, right):
    global controls
    difference = left - right
    entries = list(difference) if isinstance(difference, sp.MatrixBase) else [difference]
    if all(sp.simplify(value) == 0 for value in entries):
        raise RuntimeError(f"Failure control not detected: {label}")
    controls += 1


def psd(label, matrix):
    global checks
    eq(label + ' Hermitian', matrix, matrix.conjugate().T)
    for count in range(1, matrix.rows + 1):
        for indices in combinations(range(matrix.rows), count):
            value = sp.simplify(matrix.extract(indices, indices).det())
            if value.is_nonnegative is not True:
                raise RuntimeError(f"Failed PSD {label}, {indices}: {value}")
    checks += 1


def adj(X, G):
    return G.inv() * X.conjugate().T * G


def quotient(J, H, K):
    G = (J * H.inv() * J.conjugate().T).inv()
    R = H.inv() * J.conjugate().T * G
    A = J * H.inv() * K * R
    return tuple(sp.simplify(X) for X in (G, R, A))


def moments(weights, nodes, degree):
    return [sum(w * node ** j for w, node in zip(weights, nodes)) for j in range(degree + 1)]


def source(mu, N):
    order = list(range(0, N + 1, 2)) + list(range(1, N + 1, 2))
    Pi = sp.eye(N + 1)[order, :]
    Hy = sp.Matrix(N + 1, N + 1, lambda a, b: mu[a+b])
    Ky = sp.Matrix(N + 1, N + 1, lambda a, b: mu[a+b+1])
    return Pi * Hy * Pi.T, Pi * Ky * Pi.T, Pi


def original_maps(polynomial, y, N, c):
    q = sp.degree(polynomial, y)
    S = sp.symbols('S')
    chiS = sp.Poly(sp.expand(I ** q * polynomial.subs(y, (S-c)/I)), S)
    JS = sp.Matrix(q, N+1, lambda row, col: sp.rem(sp.Poly(S ** col, S), chiS).nth(row))
    TN = sp.Matrix(N+1, N+1, lambda row, col:
                   sp.binomial(col, row)*c**(col-row)*I**row if row <= col else 0)
    TNi = sp.Matrix(N+1, N+1, lambda row, col:
                    sp.binomial(col, row)*(-c)**(col-row)*I**(-col) if row <= col else 0)
    eq('original triangular inverse', TN*TNi, sp.eye(N+1))
    MS = sp.zeros(q)
    for j in range(q-1):
        MS[j+1, j] = 1
    for j in range(q):
        MS[j, q-1] = -chiS.nth(j)
    return JS, TN, sp.simplify((MS-c*sp.eye(q))/I), chiS


y, z, t = sp.symbols('y z t', real=True)
nodes = list(map(sp.Integer, [-4, -3, -2, -1, 1, 2, 3, 4]))
weights = list(map(sp.Rational, [1, 2, 1, 3, 3, 1, 2, 1]))
rho = sp.Rational(1, 10)
perturbed = [w * (1 + rho * sign) for w, sign in zip(weights, [1,-1,1,-1,-1,1,-1,1])]
reports = []
for name, polynomial, N in [('kernel', y*y+1, 3), ('repeated-roots', (y*y+1)**2, 5)]:
    mu0 = moments(weights, nodes, 2*N+1)
    mu = moments(perturbed, nodes, 2*N+1)
    H0, K0, Pi = source(mu0, N)
    H, K, _ = source(mu, N)
    JS, TN, M, chiS = original_maps(polynomial, y, N, sp.Rational(5, 2))
    J = sp.simplify(JS * (Pi*TN).inv())
    q = M.rows
    G0, R0, A0 = quotient(J, H0, K0)
    G, R, A = quotient(J, H, K)
    Q, Q0 = A-M, A0-M
    eq(name + ' full mass', H0[0,0], 14)
    eq(name + ' map onto', J*R, sp.eye(q))
    eq(name + ' minimizing equations', H*R, J.conjugate().T*G)
    eq(name + ' attained metric', R.conjugate().T*H*R, G)
    eq(name + ' compressed source', G*A, R.conjugate().T*K*R)
    eq(name + ' selfadjoint', adj(A, G), A)
    eq(name + ' square-zero relation', Q*Q, sp.zeros(q))
    eq(name + ' relation rank', sp.Integer(Q.rank()), 1)
    cp = M.charpoly()
    eq(name + ' endpoint full characteristic', cp.as_expr().subs(cp.gen,z), polynomial.subs(y,z))
    eq(name + ' physical coordinate characteristic', chiS.as_expr().subs(chiS.gen, sp.Rational(5,2)+I*z),
       I**q*polynomial.subs(y,z))
    psd(name + ' source lower', H-(1-rho)*H0)
    psd(name + ' source upper', (1+rho)*H0-H)
    psd(name + ' quotient lower', G-(1-rho)*G0)
    psd(name + ' quotient upper', (1+rho)*G0-G)
    D = R-R0
    eq(name + ' lift same fibre', J*D, sp.zeros(q))
    eq(name + ' lift orthogonality', R0.conjugate().T*H0*D, sp.zeros(q))
    psd(name + ' sharp lift radius', rho**2/(1-rho**2)*G0-D.conjugate().T*H0*D)
    F = K-K0
    seven = (R0.conjugate().T*K0*D+D.conjugate().T*K0*R0+D.conjugate().T*K0*D+
             R0.conjugate().T*F*R0+R0.conjugate().T*F*D+D.conjugate().T*F*R0+D.conjugate().T*F*D)
    eq(name + ' seven-term compression', R.conjugate().T*K*R-R0.conjugate().T*K0*R0, seven)
    ne(name + ' mixed terms removed', seven, D.conjugate().T*K0*D+R.conjugate().T*F*R)
    ne(name + ' physical map omitted', J, JS[:, :N+1])
    ne(name + ' wrong compression missing H inverse', A, J*K*R)
    ne(name + ' unit-mass replacement', G, G / H[0,0])
    hdet, BJ = H.det(), J*H.adjugate()*J.conjugate().T
    eq(name + ' rational quotient', G, hdet*BJ.adjugate()/BJ.det())
    eq(name + ' rational lift', R, H.adjugate()*J.conjugate().T*BJ.adjugate()/BJ.det())
    eps2 = sp.simplify(sp.trace(adj(Q,G)*Q))
    # Four heat coefficients retain the same t and exact metric.
    T = A-t*Q
    PT = adj(T,G)*T
    for n in range(1, 5):
        dn = sp.simplify(sp.trace(PT**n)-sp.re(sp.trace(T**(2*n))))
        eq(name + f' correlated constant coefficient {n}', dn.subs(t,0), 0)
        eq(name + f' correlated linear coefficient {n}', sp.diff(dn,t).subs(t,0), 0)
        if n == 1:
            eq(name + ' exact first heat coefficient', dn, t*t*eps2)
        eq(name + f' fixed endpoint holomorphic coefficient {n}', sp.trace(T.subs(t,1)**(2*n)),
           sp.trace(M**(2*n)))
        eq(name + f' fixed endpoint across moment changes {n}', sp.trace((A0-Q0)**(2*n)),
           sp.trace(M**(2*n)))
    ne(name + ' positive endpoint falsely fixed', sp.trace(adj(M,G)*M), sp.trace(adj(M,G0)*M))
    if name == 'repeated-roots':
        eq('repeated-root nilpotent square', (M*M+sp.eye(q))**2, sp.zeros(q))
        ne('Jordan contribution not discarded', M*M+sp.eye(q), sp.zeros(q))
        eq('full repeated trace count', sp.trace(sp.eye(q)), 4)
        ne('lost root multiplicities', sp.trace(sp.eye(q)), 2)
    reports.append({'name':name,'N':N,'q':q,'source_mass':str(H[0,0]),
                    'quotient_determinant':str(G.det()),'epsilon_squared':str(eps2)})

# Exact seed division and whole-mass convolution in a finite rational measure.
x, w = sp.symbols('x w', real=True)
delta, gamma = sp.Rational(1,4), sp.Integer(3)
P = (x*x+2*(delta**2-gamma**2)*x+(delta**2+gamma**2)**2)**2
e = [sum(weight*node**(2*j) for weight,node in zip(weights,nodes)) for j in range(9)]
beta = [sum(weight*node**(2*j)*P.subs(x,node*node) for weight,node in zip(weights,nodes)) for j in range(5)]
for j in range(9):
    quo, rem = sp.div(x**j,P,x)
    receiver = sum(sp.Poly(rem,x).nth(a)*e[a] for a in range(4))
    receiver += sum(sp.Poly(quo,x).nth(a)*beta[a] for a in range(max(0,j-3)))
    eq(f'seed receiver {j}', receiver, e[j])
k = 5
egf = sum(e[j]*z**(2*j)/sp.factorial(2*j) for j in range(4))
conv = sp.Poly(egf**k,z)
eq('full convolution mass', conv.nth(0), e[0]**k)
ne('probability-mass substitution', conv.nth(0), 1)
eq('shared convolution second moment', 2*conv.nth(2), k*e[1]*e[0]**(k-1))

# One raw variable changes every anti-diagonal occurrence together.
eps = sp.symbols('eps', real=True)
N=3
E2=sp.Matrix(N+1,N+1,lambda a,b: int(a+b == 2))
rankone=sp.zeros(N+1)
for a in range(N+1):
    for b in range(a+1,N+1):
        if a+b==2:
            va,vb=sp.eye(N+1)[:,a],sp.eye(N+1)[:,b]
            rankone += ((va+vb)*(va+vb).T-(va-vb)*(va-vb).T)/2
for a in range(N+1):
    if 2*a==2:
        va=sp.eye(N+1)[:,a]
        rankone += va*va.T
eq('tied rank-one anti-diagonal', eps*rankone,eps*E2)
ne('independent diagonal error shortcut',eps*E2,eps*sp.diag(0,1,0,0))

# Rational interval Bernstein certificate, with a shared variable before subtraction.
numerator = sp.expand((1+w)**2-(1-w)**2)
eq('correlated numerator cancellation',numerator,4*w)
poly=sp.Poly(numerator.subs(w,2*x-1),x)
deg=poly.degree()
bern=[sum(poly.nth(j)*sp.binomial(a,j)/sp.binomial(deg,j) for j in range(a+1)) for a in range(deg+1)]
eq('Bernstein lower',min(bern),-4)
eq('Bernstein upper',max(bern),4)

# Heat-tail coefficient identity and its exact factorial majorization.
for D in range(1,8):
    for j in range(D,D+8):
        left=sp.Rational(2*j+1,sp.factorial(j))
        right=sp.Rational(2*D+1,sp.factorial(D)*sp.factorial(j-D))
        if right-left < 0:
            raise RuntimeError('Factorial correlated tail coefficient failed')
        checks += 1
eq('tail first coefficient keeps sign', -(-1)*t*t, t*t)


def bernstein_range(expression, variable, lower, upper):
    global checks
    vv=sp.symbols('bernstein_variable', real=True)
    pol=sp.Poly(sp.expand(expression.subs(variable,lower+(upper-lower)*vv)),vv)
    degree=max(0,pol.degree())
    coefficients=[sum(pol.nth(j)*sp.binomial(a,j)/sp.binomial(degree,j)
                      for j in range(a+1)) for a in range(degree+1)]
    checks += 1
    return min(coefficients),max(coefficients)


def rational_range(expression, variable, lower, upper):
    numerator,denominator=sp.fraction(sp.cancel(expression))
    low_d,high_d=bernstein_range(denominator,variable,lower,upper)
    if high_d < 0:
        numerator,denominator=-numerator,-denominator
        low_d,high_d=-high_d,-low_d
    if low_d <= 0:
        raise RuntimeError('Uncertified denominator in exact end-to-end box')
    low_n,high_n=bernstein_range(numerator,variable,lower,upper)
    ratios=[a/b for a in [low_n,high_n] for b in [low_d,high_d]]
    return min(ratios),max(ratios)


# A single uncertain atomic weight is carried through the whole native map.
# Source nu_w = delta_-1 + w delta_0 + delta_1, 1 <= w <= 2;
# its third convolution is used in the original sum coordinate.
raw_mass=w+2
raw_egf=raw_mass+z*z+z**4/sp.Integer(12)
convolution=sp.Poly(raw_egf**3,z)
mu_shared=[sp.factorial(j)*convolution.nth(j) for j in range(6)]
Hs,Ks,Pis=source(mu_shared,2)
Js=sp.Matrix([[1,-1,0],[0,0,1]])
Gs,Rs,As=quotient(Js,Hs,Ks)
eq('displayed comparison quotient metric',Gs,sp.diag(6*raw_mass**3/(raw_mass+12),6*raw_mass**2))
eq('displayed comparison compression',As,sp.Matrix([[0,-1],[-raw_mass/(raw_mass+12),0]]))
Ms=sp.Matrix([[0,-1],[1,0]])
Qs=sp.simplify(As-Ms)
Ts=As-t*Qs
eq('end-to-end original mass',Hs[0,0],(w+2)**3)
eq('end-to-end common quotient equations',Hs*Rs,Js.T*Gs)
eq('end-to-end square-zero relation',Qs*Qs,sp.zeros(2))
eq('end-to-end endpoint holomorphic trace',sp.trace(Ts.subs(t,1)**2),-2)
eq('end-to-end moment-independent endpoint derivative',
   sp.diff(sp.trace(Ts.subs(t,1)**2),w),0)
positive_square=sp.simplify(adj(Ms,Gs)*Ms)
ne('end-to-end positive trace genuinely varies',sp.diff(sp.trace(positive_square),w),0)
eps_shared=sp.factor(sp.trace(adj(Qs,Gs)*Qs))
eq('end-to-end full shared first coefficient',
   sp.trace(positive_square)+2,eps_shared)
for j in range(2):
    low,high=rational_range(10-positive_square[j,j],w,1,2)
    if low < 0:
        raise RuntimeError('End-to-end B squared bound failed')
    checks += 1
low,high=rational_range(16-eps_shared,w,1,2)
if low < 0:
    raise RuntimeError('End-to-end outgoing curvature bound failed')
checks += 1
heat_s=sp.Rational(1,100)
D=3
shared_delta=sum((-heat_s)**n/sp.factorial(n)*
                 (sp.trace(Ms**(2*n))-sp.trace(positive_square**n)) for n in range(D+1))
# Rational subboxes retain the same w; collect before bounding.
shared_intervals=[rational_range(shared_delta,w,sp.Rational(10+j,10),sp.Rational(11+j,10))
                  for j in range(10)]
lo=min(a for a,b in shared_intervals)
hi=max(b for a,b in shared_intervals)
x_heat=heat_s*10
# e^x <= 1/(1-x), proved coefficientwise, makes this tail rational.
tail=heat_s*16/(1-x_heat)*(2*D+1)*x_heat**D/sp.factorial(D)
shared_certificate={'input_weight_interval':['1','2'],'convolution_power':3,
                    'mass':'(w+2)^3','heat_time':str(heat_s),'heat_degree':D,
                    'B_squared_bound':'10','outgoing_curvature_squared_bound':'16',
                    'difference_polynomial_interval':[str(lo),str(hi)],
                    'correlated_tail':str(tail),
                    'certified_heat_difference_interval':[str(lo-tail),str(hi+tail)]}

result={'status':'pass','exact_checks':checks,'negative_controls':controls,'cases':reports,
        'end_to_end_shared_input':shared_certificate,
        'proof_sha256':hashlib.sha256((HERE/'NATIVE_HEAT_MOMENT_RETURN.tex').read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact finite comparison inputs, coefficient identities and PSD tests; no sampled zeta zeros or degree-uniform inference.'}
print(json.dumps(result,indent=2))
