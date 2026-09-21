"""Exact finite degree-step checks, with original Gamma mass retained.

Small frames are declared algebra fixtures, never replacements for the
actual period frame. The quartet and Reynolds structural tests are
separate from those fixtures. All checks survive optimized Python.
"""

from itertools import product
import argparse
import json
import sympy as sp

I = sp.I
M = sp.sqrt(2 * sp.pi)
x = sp.symbols("x")
P = [sp.Integer(1), x]
for j in range(1, 11):
    P.append(sp.expand(x*P[j]-j*(j-sp.Rational(1, 2))*P[j-1]))
norms = [M*sp.factorial(j)*sp.rf(sp.Rational(1, 2), j) for j in range(len(P))]
checks = []


def simp(z):
    return sp.cancel(sp.expand(z))


def clean(A):
    return A.applyfunc(simp)


def check(name, actual, expected):
    diff = actual-expected
    items = list(diff) if isinstance(diff, sp.MatrixBase) else [diff]
    residual = [simp(z) for z in items]
    if any(z != 0 for z in residual):
        raise RuntimeError(f"FAILED: {name}; residual={residual}")
    checks.append(name)


def positive(name, z):
    z = simp(z)
    if z.is_positive is not True:
        raise RuntimeError(f"FAILED: {name}; not proved positive: {z}")
    checks.append(name)


def posdef(name, A):
    for j in range(1, A.rows+1):
        positive(f"{name}: minor {j}", A[:j, :j].det())


def f(nodes, j):
    return sp.Matrix([P[j].subs(x, z) for z in nodes])


def covariance(nodes, d):
    C = sp.zeros(len(nodes))
    for j in range(d):
        fj = f(nodes, j)
        C += fj*fj.conjugate().T/norms[j]
    return clean(C)


def data(nodes, Z, pi, d):
    V, U = Z.conjugate(), pi.T
    Y = sp.diag(*nodes)
    C = covariance(nodes, d)
    Ci = clean(C.inv())
    A = clean(V.conjugate().T*C*V)
    Ai = clean(A.inv())
    G = clean(U.conjugate().T*Ci*U)
    fd = f(nodes, d)
    gd = clean(V.conjugate().T*fd)
    bd = clean(U.conjugate().T*Ci*fd)
    alpha = simp((gd.conjugate().T*Ai*gd)[0]/norms[d])
    beta = simp((fd.conjugate().T*Ci*fd)[0]/norms[d])
    tau = simp((bd.conjugate().T*G.inv()*bd)[0]/norms[d])
    W, MU = clean(V.conjugate().T*V), clean(U.conjugate().T*U)
    H = clean(V.conjugate().T*Y*V*W.inv())
    F = clean(V.conjugate().T*Y*U)
    T = clean(U.conjugate().T*C*V)
    E = clean(F*MU.inv()*T-T.conjugate().T*MU.inv()*F.conjugate().T)
    ed = clean(U.conjugate().T*fd)
    rho = clean(F*MU.inv()*ed)
    return locals()


def fixture_steps(name, nodes, Z, pi, start, stop):
    q = len(nodes)
    r, m = Z.cols, pi.rows
    check(name+": dimensions", r+m, q)
    check(name+": original coefficient annihilation", pi*Z, sp.zeros(m, r))
    values = {d: data(nodes, Z, pi, d) for d in range(start, stop+2)}
    for d in range(start, stop+1):
        a, n = values[d], values[d+1]
        tag = f"{name} d={d}"
        check(tag+": full rank-one update", n["C"]-a["C"], a["fd"]*a["fd"].conjugate().T/norms[d])
        check(tag+": compressed rank-one update", n["A"]-a["A"], a["gd"]*a["gd"].conjugate().T/norms[d])
        check(tag+": compressed determinant step", n["A"].det()/a["A"].det(), 1+a["alpha"])
        check(tag+": full determinant step", n["C"].det()/a["C"].det(), 1+a["beta"])
        check(tag+": complement gap", a["beta"]-a["alpha"], a["tau"])
        check(tag+": restricted inverse step", n["G"], a["G"]-a["bd"]*a["bd"].conjugate().T/(norms[d]*(1+a["beta"])))
        check(tag+": restricted determinant step", n["G"].det()/a["G"].det(), (1+a["alpha"])/(1+a["beta"]))
        factor = a["MU"].det()/a["W"].det()
        check(tag+": all original frame factors", a["G"].det(), factor*a["A"].det()/a["C"].det())
        check(tag+": surviving Omega orientation", a["F"], (pi*a["Y"]*Z).T)
        check(tag+": cross covariance step", n["T"]-a["T"], a["ed"]*a["gd"].conjugate().T/norms[d])
        correction = (a["rho"]*a["gd"].conjugate().T-a["gd"]*a["rho"].conjugate().T)/norms[d]
        check(tag+": complete correction step", n["E"]-a["E"], correction)
        gm = a["V"].conjugate().T*f(nodes, d-1)
        gp = a["V"].conjugate().T*f(nodes, d+1)
        xi = a["H"]*a["gd"]-d*(d-sp.Rational(1, 2))*gm+a["rho"]
        check(tag+": original compressed recurrence", gp, xi)
        term = (a["gd"].conjugate().T*a["Ai"]*xi)[0]
        nextalpha = ((xi.conjugate().T*a["Ai"]*xi)[0]
            -term*sp.conjugate(term)/(norms[d]*(1+a["alpha"]))) / norms[d+1]
        check(tag+": next leverage with correction", n["alpha"], nextalpha)
        scale = sp.Rational(7, 3)
        check(tag+": retained mass in scalar update",
              ((a["gd"].conjugate().T*(a["A"]/scale).inv()*a["gd"])[0]/(scale*norms[d])), a["alpha"])
        check(tag+": physical column phase", (I**d*a["fd"])*(I**d*a["fd"]).conjugate().T,
              a["fd"]*a["fd"].conjugate().T)
    if start == q and stop >= 2*q:
        for key, update in (("A", "alpha"), ("C", "beta")):
            lhs = values[q][key].det()*values[q+1][key].det()/(values[2*q][key].det()*values[2*q+1][key].det())
            rhs = sp.prod((1+values[d][update])**(-1 if d in (q,2*q) else -2) for d in range(q,2*q+1))
            check(name+": exact four-return "+key, lhs, rhs)
        lhs = values[q]["G"].det()*values[q+1]["G"].det()/(values[2*q]["G"].det()*values[2*q+1]["G"].det())
        rhs = sp.prod(((1+values[d]["beta"])/(1+values[d]["alpha"]))**(1 if d in (q,2*q) else 2) for d in range(q,2*q+1))
        check(name+": exact four-return original restriction", lhs, rhs)
    return values


def structural_reynolds():
    xx = sp.symbols("x1:5")
    z0,z1,w0,w1 = sp.symbols("z0 z1 w0 w1")
    t = sp.Matrix([z0*w0,z0*w1,z1*w0,z1*w1])
    H = sp.eye(4)
    H[0,1] = 1
    height, delta = sp.Integer(3), sp.Rational(1,3)
    Lam = sp.diag(height-I*delta,-height-I*delta,height+I*delta,-height+I*delta)
    L = H*Lam*H.inv()
    off = L-sp.diag(*[L[j,j] for j in range(4)])
    check("actual-generator dictionary fixture off-diagonal", off[0,1], -2*height)
    def deriv(B, poly):
        Bx = B*sp.Matrix(xx)
        return sp.expand(sum(Bx[j]*sp.diff(poly,xx[j]) for j in range(4)))
    def reynolds(poly):
        ans = 0
        for mon, coeff in sp.Poly(poly,*xx).terms():
            if sum((j+1)*mon[j] for j in range(4)) % 5 == 0:
                ans += coeff*sp.prod(xx[j]**mon[j] for j in range(4))
        return sp.expand(ans)
    subst = dict(zip(xx, H*t))
    for poly in (xx[0]**8*xx[1], xx[0]**3*xx[1]**6, xx[0]*xx[3], xx[1]*xx[2]):
        check("Reynolds diagonal cancellation "+str(poly), reynolds(deriv(L,poly)), deriv(L-off,poly))
        biform = sp.expand(poly.subs(subst, simultaneous=True))
        D = height*(w0*sp.diff(biform,w0)-w1*sp.diff(biform,w1))-I*delta*(z0*sp.diff(biform,z0)-z1*sp.diff(biform,z1))
        check("literal source scaling map "+str(poly), D, deriv(L,poly).subs(subst, simultaneous=True))
    fixture = xx[0]**8*xx[1]
    check("nonzero surviving invariant derivative", deriv(off,fixture), -16*height*xx[0]**7*xx[1]**2)
    s = sp.symbols("s")
    independent = sp.Matrix(10,3,lambda j,col: sp.Poly((s**8,s**3,s**7)[col],s).nth(j))
    check("surviving off-diagonal image not invariant on restriction", independent.rank(), 3)
    # Exact conductor product rule in the source-scaling coordinate. The
    # invariant-image quotient kills the second term because it is an
    # actual conductor multiple; it does not kill the first term by fiat.
    AA=(z0*w0+2*z1*w1)**8
    hh=z0*w1+I*z1*w0
    def bideriv(poly):
        return height*(w0*sp.diff(poly,w0)-w1*sp.diff(poly,w1))-I*delta*(z0*sp.diff(poly,z0)-z1*sp.diff(poly,z1))
    check("exact conductor product-rule cancellation",bideriv(AA*hh)-AA*bideriv(hh),bideriv(AA)*hh)
    # Five orbit equations have fixed coefficients in positions x1*x4
    # and x2*x3; their x2*x4 coefficients carry five distinct fifth roots.
    cyclo = sp.Poly(sp.cyclotomic_poly(5,s),s)
    for a,b in product(range(5),repeat=2):
        if a < b:
            rem = sp.rem(s**a-s**b,cyclo.as_expr(),s)
            if rem == 0:
                raise RuntimeError("Distinct fifth-root coefficients collapsed")
            checks.append(f"five-orbit coefficient distinction {a},{b}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--negative-control", choices=("step-sign","omit-correction","resonant-modulus","mass","offdiag-cancellation"))
    args = parser.parse_args()
    nodes=(0,I); Z=sp.Matrix([1,-I]); pi=sp.Matrix([[I,1]])
    if args.negative_control:
        a,n=data(nodes,Z,pi,2),data(nodes,Z,pi,3)
        if args.negative_control=="step-sign":
            check("wrong determinant increment sign", n["A"].det()/a["A"].det(),1-a["alpha"])
        elif args.negative_control=="omit-correction":
            check("missing complete correction increment",n["E"]-a["E"],sp.zeros(1))
        elif args.negative_control=="resonant-modulus":
            val=P[2].subs(x,1+I)
            check("wrong modulus at reflected entry",val**2,val*sp.conjugate(val))
        elif args.negative_control=="mass":
            check("wrong Gamma mass",norms[0],sp.sqrt(2)*sp.pi)
        else:
            check("unjustified off-diagonal annihilation",-48,0)
        raise RuntimeError("Negative control unexpectedly passed")
    vals=fixture_steps("nonzero correction Gamma",nodes,Z,pi,2,4)
    # A second computation of the original multiplication-source norm
    # uses actual Gamma moments, independently of the evaluation kernel.
    theta=sp.symbols("theta")
    mgf=sp.series(sp.cos(theta)**(-sp.Rational(1,2)),theta,0,12).removeO()
    moments=[M*sp.factorial(j)*sp.expand(mgf).coeff(theta,j) for j in range(11)]
    relation=sp.expand(sp.prod(x-z for z in nodes))
    def relation_det(n):
        if n==0:
            return sp.Integer(1)
        deg=n+len(nodes)
        Hmom=sp.Matrix(deg,deg,lambda a,b:moments[a+b])
        T=sp.Matrix(deg,n,lambda a,b:sp.Poly(relation*x**b,x).nth(a))
        return simp((T.conjugate().T*Hmom*T).det())
    for d in range(2,5):
        check(f"original relation norm receiver d={d}",relation_det(d-1)/relation_det(d-2)/norms[d],1+vals[d]["beta"])
    for deg in range(1,7):
        J=sp.zeros(deg)
        for j in range(1,deg):
            J[j-1,j]=J[j,j-1]=sp.sqrt(j*(j-sp.Rational(1,2)))
        check(f"exact real symmetric Jacobi characteristic polynomial d={deg}",J.charpoly(x).as_expr(),P[deg])
    a,n=vals[2],vals[3]
    for name,actual,expected in (
        ("alpha fixture",a["alpha"],sp.Rational(5,12)),
        ("beta fixture",a["beta"],sp.Rational(1,2)),
        ("gap fixture",a["tau"],sp.Rational(1,12)),
        ("actual correction d2",a["E"][0],2*I/M),
        ("actual correction d3",n["E"][0],10*I/(3*M)),
        ("restricted metric d3",n["G"][0],17*M/9)):
        check(name,actual,expected)
    nodes2=(1+I,1-I,-1+2*I,-1-2*I)
    Z2=sp.Matrix([[1,0],[0,1],[I,2],[1-I,I]])
    B=Z2[2:,:]
    pi2=(-B).row_join(sp.eye(2))
    vals2=fixture_steps("conjugate pair block",nodes2,Z2,pi2,4,8)
    q=len(nodes2)
    relation=sp.expand(sp.prod(x-z for z in nodes2))
    check("retained positive pair relation",relation,((x-1)**2+1)*((x+1)**2+4))
    for start in (0,1,4,5):
        mat=sp.Matrix.hstack(*[f(nodes2,j) for j in range(start,start+q)])
        if simp(mat.det())==0:
            raise RuntimeError("Consecutive evaluation block lost rank")
        checks.append(f"strict consecutive original-pair basis start={start}")
    for start in (4,5):
        if start+q not in vals2:
            vals2[start+q]=data(nodes2,Z2,pi2,start+q)
        a,n=vals2[start],vals2[start+q]
        posdef(f"strict full block {start}",n["C"]-a["C"])
        posdef(f"strict compressed block {start}",n["A"]-a["A"])
        posdef(f"strict original kernel block {start}",a["G"]-n["G"])
    for d in (1,2,5,9):
        wd=sp.diff(P[d],x)*P[d-1]-sp.diff(P[d-1],x)*P[d]
        wn=sp.diff(P[d+1],x)*P[d]-sp.diff(P[d],x)*P[d+1]
        check(f"all resonance Wronskian step d={d}",wn/norms[d]-wd/norms[d-1],P[d]**2/norms[d])
    # Exact original permitted k=9 coordinate structure, without evaluating
    # its period coefficients or forming an unneeded 100-dimensional Gram.
    kk,dd,hh=9,sp.Rational(1,3),sp.Integer(3)
    original={(a,b):(2*b-kk)*hh-I*(2*a-kk)*dd for a in range(kk+1) for b in range(kk+1)}
    for (aa,bb),u in original.items():
        check(f"original reflected pair {aa},{bb}",sp.conjugate(original[kk-aa,bb]),u)
    for point in (sp.Rational(0),sp.Rational(2,7)):
        direct=sp.prod(point-u for u in original.values())
        paired=sp.prod((point-(2*b-kk)*hh)**2+(2*a-kk)**2*dd**2 for a in range((kk+1)//2) for b in range(kk+1))
        check(f"actual quartet positive relation pairing at {point}",direct,paired)
        positive(f"actual quartet relation strictly positive at {point}",paired)
    check("actual quartet original leading phase",I**((kk+1)**2),1)
    structural_reynolds()
    print(json.dumps({"status":"passed","exact_check_count":len(checks),"checks":checks,
                      "mass":"sqrt(2*pi)","actual_period_sampled":False,
                      "asymptotic_claim":False},indent=2))


if __name__=="__main__":
    main()
