# Portable adaptation of extracted/fluid_blowup_reconstruction/symbolic_checks.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('incoming')
# BEGIN UNCHANGED MATHEMATICAL BODY
RESULTS: list[str] = []

def check(label: str, expression: sp.Expr | sp.MatrixBase) -> None:
    """Assert a scalar or matrix expression vanishes identically."""
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    residuals = [sp.simplify(sp.expand(e)) for e in entries]
    failures = [r for r in residuals if r != 0]
    if failures:
        raise AssertionError(f"{label}: nonzero residual(s): {failures}")
    RESULTS.append(f"PASS  {label}")


def run_checks() -> None:
    k1, k2 = sp.symbols('k1 k2', real=True)
    ksq = k1**2+k2**2
    m = sp.Matrix([k1*k2/ksq, -k1**2/ksq])
    check('IPM Fourier symbol is transverse', (m.T*sp.Matrix([k1,k2]))[0])

    x1, x2, lam = sp.symbols('x1 x2 lam', real=True, nonzero=True)
    z1, z2, Om, Th, g1, g2 = sp.symbols('z1 z2 Om Th g1 g2', real=True)
    aa, bb, cc = sp.symbols('aa bb cc', real=True)
    D = sp.Matrix([[aa,bb],[cc,-aa]])
    z = sp.Matrix([z1,z2]); x=sp.Matrix([x1,x2]); U=D*x
    J = sp.Matrix([[0,-1],[1,0]]); zdot=-D.T*z
    phase=lam*(z.T*x)[0]; kap=z1**2+z2**2
    material_phase=lam*(zdot.T*x)[0]+sum(U[i]*sp.diff(phase,x[i]) for i in range(2))
    check('Affine material phase is transported', material_phase)
    theta=Th*sp.sin(phase)
    v=Om/(lam*kap)*(J*z)*sp.sin(phase)
    vort=Om*sp.cos(phase)
    psi=-Om/(lam**2*kap)*sp.cos(phase)
    check('Wave streamfunction generates the stated velocity',
          J*sp.Matrix([sp.diff(psi,xx) for xx in x])-v)
    check('Wave streamfunction generates the stated vorticity',
          sum(sp.diff(psi,xx,2) for xx in x)-vort)
    check('Wave self-advection of scalar vanishes',
          sum(v[i]*sp.diff(theta,x[i]) for i in range(2)))
    check('Wave self-advection of vorticity vanishes',
          sum(v[i]*sp.diff(vort,x[i]) for i in range(2)))
    thdot=-((J*z).T*sp.Matrix([g1,g2]))[0]*Om/(lam*kap)
    omdot=lam*z1*Th
    check('Exact Boussinesq scalar residual cancels',
          thdot*sp.sin(phase)+(v.T*sp.Matrix([g1,g2]))[0])
    check('Exact Boussinesq vorticity residual cancels',
          omdot*sp.cos(phase)-sp.diff(theta,x1))
    shear=Om*(J*z)*z.T/kap
    check('Affine-core shear is trace free', sp.trace(shear))
    check('Affine-core shear is nilpotent', shear*shear)

    A, rr, ph, eta = sp.symbols('A rr ph eta', real=True, nonzero=True)
    B=sp.Matrix([[0,A*sp.sin(ph)/(lam*rr)],[lam*rr*sp.sin(ph),0]])
    check('Frozen Boussinesq characteristic polynomial',
          (eta*sp.eye(2)-B).det()-(eta**2-A*sp.sin(ph)**2))
    tau, L=sp.symbols('tau L', real=True)
    P=sp.exp(L)*(sp.cos(tau)+sp.sin(tau))
    Q=sp.exp(L)*(sp.cos(tau)-sp.sin(tau))
    check('Return control satisfies P prime equals Q', sp.diff(P,tau)-Q)
    check('Return control satisfies Q prime equals minus P', sp.diff(Q,tau)+P)
    check('Return endpoint retains amplified scalar', P.subs(tau,sp.pi/4)-sp.sqrt(2)*sp.exp(L))
    check('Return endpoint resets vorticity variable', Q.subs(tau,sp.pi/4))

    # Nontrivial determinant-one material map tests of the two-scale identities.
    t,s,a1,a2,p1,p2=sp.symbols('t s a1 a2 p1 p2', real=True)
    M=sp.Matrix([[1,t],[0,1]]); Mi=M.inv(); C=Mi*Mi.T
    pp=sp.Matrix([p1,p2]); zz=Mi.T*pp; kk=(pp.T*C*pp)[0]
    AP=s**2*a1+s*a2**2+a1*a2
    PS=s**3+s*a1+s*a2**2
    av=Mi*sp.Matrix([x1,x2])
    substitution={s:lam*(pp.T*av)[0],a1:av[0],a2:av[1]}
    sharp=lambda expr: sp.expand(expr.subs(substitution, simultaneous=True))
    grad_a=lambda expr:sp.Matrix([sp.diff(expr,a1),sp.diff(expr,a2)])
    grad_x=lambda expr:sp.Matrix([sp.diff(expr,x1),sp.diff(expr,x2)])
    lap_M=lambda expr:sum(C[i,j]*sp.diff(expr,[a1,a2][i],[a1,a2][j]) for i in range(2) for j in range(2))
    D1=lambda expr:2*((C*pp).T*grad_a(sp.diff(expr,s)))[0]
    lhs=sum(sp.diff(sharp(AP),xx,2) for xx in (x1,x2))
    rhs=sharp(lam**2*kk*sp.diff(AP,s,2)+lam*D1(AP)+lap_M(AP))
    check('Two-scale Laplacian chain rule under a shear map', lhs-rhs)
    perp=lambda expr:((J*pp).T*grad_a(expr))[0]
    fast=sp.diff(PS,s)*perp(AP)-sp.diff(AP,s)*perp(PS)
    slow=((J*grad_a(PS)).T*grad_a(AP))[0]
    lhs=((J*grad_x(sharp(PS))).T*grad_x(sharp(AP)))[0]
    check('Two-scale Jacobian has no quadratic-frequency term', lhs-sharp(lam*fast+slow))
    check('Material derivative chain rule under the shear map',
          sp.diff(sharp(AP),t)+x2*sp.diff(sharp(AP),x1))

    # Test the volume-coordinate identities on a general smooth function.
    zc,r,y=sp.symbols('z r y', real=True, positive=True)
    fun=sp.Function('F')(zc,y)
    fphys=fun.subs(y,r**2/2)
    Dgamma=sp.diff(fphys,zc,2)+sp.diff(fphys,r,2)-sp.diff(fphys,r)/r
    Dxi=sp.diff(fphys,zc,2)+sp.diff(fphys,r,2)+3*sp.diff(fphys,r)/r
    check('Angular-momentum diffusion in volume coordinates',
          Dgamma-(sp.diff(fun,zc,2)+2*y*sp.diff(fun,y,2)).subs(y,r**2/2))
    check('Normalized-vorticity diffusion in volume coordinates',
          Dxi-(sp.diff(fun,zc,2)+2*y*sp.diff(fun,y,2)+4*sp.diff(fun,y)).subs(y,r**2/2))
    ur=sp.diff(fphys,zc)/r; uz=-sp.diff(fphys,r)/r
    curl_phi=sp.diff(ur,zc)-sp.diff(uz,r)
    expected=sp.diff(fun,y,2)+sp.diff(fun,zc,2)/(2*y)
    check('Axisymmetric streamfunction elliptic operator', curl_phi/r-expected.subs(y,r**2/2))

    nu,N,q,d,c,sigma,kappa=sp.symbols('nu N q d c sigma kappa', nonzero=True)
    visc=sp.Matrix([[-nu*N**2*q,-d/(sigma*kappa)],[sigma*c*z1,-nu*N**2*q]])
    check('Viscous principal characteristic polynomial',
          (eta*sp.eye(2)-visc).det()-((eta+nu*N**2*q)**2+c*d*z1/kappa))
    rate,k0=sp.symbols('rate k0', positive=True)
    kelvin=sp.exp(rate*t-nu*k0**2*(sp.exp(2*rate*t)-1)/(2*rate))
    check('Kelvin stretched-wave formula solves its damped ODE',
          sp.diff(kelvin,t)-(rate-nu*k0**2*sp.exp(2*rate*t))*kelvin)

    xx,vv,ww=sp.symbols('xx vv ww')
    ansatz=(vv+xx*ww)/(1+xx**2)**2
    check('Tao 2024 rational ansatz yields coefficient minus four',
          sp.diff(ansatz,xx)-(ww-4*xx*vv-3*xx**2*ww)/(1+xx**2)**3)
    incorrect=(ww-2*xx*vv-3*xx**2*ww)/(1+xx**2)**3
    discrepancy=sp.simplify(sp.diff(ansatz,xx)-incorrect)
    if discrepancy==0:
        raise AssertionError('Expected coefficient discrepancy disappeared')
    RESULTS.append('CHECK Tao 2024 displayed minus-two coefficient differs by '
                   +str(discrepancy))

    shells=sp.symbols('a0:5'); coeff=sp.symbols('c0:4'); waves=sp.symbols('k0:5')
    energy=sp.S(0)
    for n in range(5):
        incoming=coeff[n-1]*shells[n-1]**2 if n>0 else sp.S(0)
        outgoing=coeff[n]*shells[n]*shells[n+1] if n<4 else sp.S(0)
        energy+=shells[n]*(incoming-outgoing-nu*waves[n]**2*shells[n])
    check('Finite shell nonlinear energy transfer cancels',
          energy+nu*sum(waves[n]**2*shells[n]**2 for n in range(5)))
    kkq=sp.symbols('kq')
    check('Published seed and gain exponents leave amplitude minus seven eighths',
          (-kkq-6)+(kkq+5+sp.Rational(1,8))+sp.Rational(7,8))
    threshold=(22-8*sp.sqrt(7))/9
    RESULTS.append('VALUE Hypodissipation threshold alpha0 = '+str(sp.N(threshold,16)))
    RESULTS.append('VALUE Alternative exponent s0=alpha0/2 = '+str(sp.N(threshold/2,16)))


# END UNCHANGED MATHEMATICAL BODY
run_checks()
finish('incoming', [{"label": value[6:], "passed": True} for value in RESULTS if value.startswith("PASS  ")], auxiliary=[value for value in RESULTS if not value.startswith("PASS  ")])
