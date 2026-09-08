"""Exact replay for localized Boussinesq residuals and finite viscous grading.

The arbitrary-profile checks use unevaluated smooth P(s), g(a,t), general
symmetric material metric, original lambda and both diffusion coefficients.
The separate grading audit uses a nonconstant determinant-one shear chart
and polynomial profiles at three levels; it verifies the finite algebraic
decomposition, not a limiting blowup construction or analytic estimates.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    records = []

    def check(name, expr, scope="arbitrary-profile exact differential identity"):
        entries = list(expr) if isinstance(expr, sp.MatrixBase) else [expr]
        residuals = [sp.cancel(sp.expand(e.doit())) for e in entries]
        assert all(e == 0 for e in residuals), (name, residuals)
        records.append({"name": name, "scope": scope, "passed": True,
                        "residual": [str(e) for e in residuals]})

    s, a1, a2, t = sp.symbols("s a1 a2 t", real=True)
    lam = sp.symbols("lambda", positive=True)
    kappa, nu = sp.symbols("kappa nu", nonnegative=True)
    p1, p2 = sp.symbols("p1 p2", real=True)
    C11, C12, C22 = [sp.Function(n)(t) for n in ("C11", "C12", "C22")]
    C = sp.Matrix([[C11, C12], [C12, C22]])
    p = sp.Matrix([p1, p2])
    J = sp.Matrix([[0, -1], [1, 0]])
    q = p.dot(C*p)
    Q, T = sp.Function("Q")(t), sp.Function("T")(t)
    P = sp.Function("P")(s)
    F = sp.diff(P, s)
    g = sp.Function("g")(a1, a2, t)

    def grad(f):
        return sp.Matrix([sp.diff(f, a1), sp.diff(f, a2)])

    def perp(f):
        return (J*p).dot(grad(f))

    def B(f):
        return (C*p).dot(grad(f))

    def slowlap(f):
        cg = C*grad(f)
        return sp.diff(cg[0], a1)+sp.diff(cg[1], a2)

    def D1(f):
        return 2*B(sp.diff(f, s))

    def lap(f):
        return lam**2*q*sp.diff(f, s, 2)+lam*D1(f)+slowlap(f)

    def fastbr(f, h):
        return sp.diff(f, s)*perp(h)-sp.diff(h, s)*perp(f)

    def slowbr(f, h):
        return (J*grad(f)).dot(grad(h))

    h, d = B(g), slowlap(g)
    V, Psi = T*F*g, Q*P*g
    O = lam**2*q*Q
    lapv = T*(lam**2*q*sp.diff(F, s, 2)*g+2*lam*sp.diff(F, s)*h+F*d)
    z = O*sp.diff(F, s)*g+2*lam*Q*F*h+Q*P*d
    bilap = Q*(lam**4*q**2*sp.diff(F, s, 3)*g
               +4*lam**3*q*sp.diff(F, s, 2)*h
               +lam**2*sp.diff(F, s)*(2*q*d+4*B(h))
               +4*lam*F*B(d)+P*slowlap(d))
    check("localized_temperature_laplacian", lap(V)-lapv)
    check("localized_streamfunction_laplacian", lap(Psi)-z)
    check("localized_streamfunction_bilaplacian", lap(lap(Psi))-bilap)
    nonlinear_theta = lam*Q*T*(F**2-P*sp.diff(F,s))*g*perp(g)
    check("complete_scalar_self_advection", lam*fastbr(Psi,V)+slowbr(Psi,V)-nonlinear_theta)
    nonlinear_omega = (lam**3*q*Q**2*(F*sp.diff(F,s)-P*sp.diff(F,s,2))*g*perp(g)
        +2*lam**2*Q**2*(F**2*g*perp(h)-P*sp.diff(F,s)*h*perp(g))
        +2*lam*Q**2*P*F*slowbr(g,h)
        +lam*Q**2*P*F*(g*perp(d)-d*perp(g))
        +Q**2*P**2*slowbr(g,d))
    check("complete_vorticity_self_advection", lam*fastbr(Psi,z)+slowbr(Psi,z)-nonlinear_omega)
    e1, e2, c1, c2, b, zeta1 = sp.symbols("Gtilde1 Gtilde2 c1 c2 b zeta1", real=True)
    e = sp.Matrix([e1,e2]); c = sp.Matrix([c1,c2])
    direct_theta = (sp.diff(V,t)+lam*b*sp.diff(Psi,s)+(J*grad(Psi)).dot(e)
                    +lam*fastbr(Psi,V)+slowbr(Psi,V)-kappa*lap(V))
    expanded_theta = ((sp.diff(T,t)+lam*b*Q)*F*g+T*F*sp.diff(g,t)
        +Q*P*(J*grad(g)).dot(e)+nonlinear_theta-kappa*lapv)
    check("full_scalar_residual_moving_envelope", direct_theta-expanded_theta)
    direct_omega = (sp.diff(z,t)+lam*fastbr(Psi,z)+slowbr(Psi,z)
                    -lam*zeta1*sp.diff(V,s)-c.dot(grad(V))-nu*lap(z))
    expanded_omega = ((sp.diff(O,t)-lam*zeta1*T)*sp.diff(F,s)*g
        +O*sp.diff(F,s)*sp.diff(g,t)+sp.diff(2*lam*Q*F*h+Q*P*d,t)
        -T*F*c.dot(grad(g))+nonlinear_omega-nu*bilap)
    check("full_vorticity_residual_moving_metric_and_envelope", direct_omega-expanded_omega)
    check("time_derivative_h_retains_metric_derivative",
          sp.diff(h,t)-(sp.diff(C,t)*p).dot(grad(g))-B(sp.diff(g,t)))
    check("time_derivative_d_retains_metric_derivative",
          sp.diff(d,t)-sum(sp.diff((sp.diff(C,t)*grad(g))[j],a)
          for j,a in enumerate((a1,a2)))-slowlap(sp.diff(g,t)))

    # Independent exact harmonic replay of the integration-by-parts means.
    Fh=sp.sin(s)+sp.Rational(3,7)*sp.sin(2*s)
    Ph=-sp.cos(s)-sp.Rational(3,14)*sp.cos(2*s)
    def mean(f):
        return sp.integrate(sp.expand_trig(f),(s,0,2*sp.pi))/(2*sp.pi)
    mh=sp.Rational(29,49)
    mp=sp.Rational(205,392)
    check("two_harmonic_primitive",sp.diff(Ph,s)-Fh,"exact two-harmonic phase sample")
    check("two_harmonic_mu2",mean(Fh**2)-mh,"exact two-harmonic phase sample")
    check("two_harmonic_muP",mean(Ph**2)-mp,"exact two-harmonic phase sample")
    for name, val in [("F",Fh),("P",Ph),("PF",Ph*Fh),
                     ("FFprime",Fh*sp.diff(Fh,s)),("PFsecond",Ph*sp.diff(Fh,s,2))]:
        check("phase_zero_mean_"+name,mean(val),"exact two-harmonic phase sample")
    check("phase_PFprime_mean",mean(Ph*sp.diff(Fh,s))+mh,"exact two-harmonic phase sample")

    # Full finite grading with three independent levels in a time-dependent chart.
    # Polynomial phases test a local differential identity; periodicity is not used.
    M=sp.Matrix([[1,t],[0,1]])
    D=sp.Matrix([[0,1],[0,0]])
    p=sp.Matrix([2,3])
    C=M.inv()*M.inv().T
    zeta=M.inv().T*p
    q=p.dot(C*p)
    K=lam**2*q
    G=sp.Matrix([1+t,2-t])
    e=M.T*G
    c=M.inv()*sp.Matrix([1,0])
    b=(J*zeta).dot(G)
    check("shear_material_matrix_ODE",sp.diff(M,t)-D*M,"exact time-dependent determinant-one chart")
    check("shear_material_determinant",M.det()-1,"exact time-dependent determinant-one chart")
    check("shear_phase_ODE",sp.diff(zeta,t)+D.T*zeta,"exact time-dependent determinant-one chart")

    def physicalgrad(f):
        return lam*zeta*sp.diff(f,s)+M.inv().T*grad(f)
    A=sp.Function("A")(s,a1,a2)
    H=sp.Function("H")(s,a1,a2)
    check("material_bracket_signs",(J*physicalgrad(A)).dot(physicalgrad(H))
          -lam*fastbr(A,H)-slowbr(A,H),"arbitrary profiles in a nonconstant shear chart")
    check("transformed_background_gradient",(J*physicalgrad(A)).dot(G)
          -lam*b*sp.diff(A,s)-(J*grad(A)).dot(e),"arbitrary profile in a nonconstant shear chart")

    psis=[(1+t)*(s**3+a1*s+a2**2),
          (2+t**2)*(a1*s**2+a2*s),
          (1+t**3)*(a1*a2*s+s**2)]
    vs=[(1+t**2)*(s*a1+s**2+a2),
        (2+t)*(s**2*a2+s*a1),
        (3+t**2)*(s*a1*a2+s**3)]
    N=2
    def at(values,i):
        return values[i] if 0<=i<len(values) else sp.S.Zero
    ws=[K*sp.diff(Psi,s) for Psi in psis]
    zs=[sp.diff(at(ws,j),s)+lam*D1(at(psis,j-1))+slowlap(at(psis,j-2))
        for j in range(N+3)]
    def source_theta(n):
        return ((J*grad(at(psis,n-1))).dot(e)
            +lam*sum(fastbr(at(psis,i),at(vs,n-1-i)) for i in range(n))
            +sum(slowbr(at(psis,i),at(vs,n-2-i)) for i in range(n-1))
            -kappa*(lam*D1(at(vs,n-1))+slowlap(at(vs,n-2))))
    def source_omega(n):
        flat=lam*D1(at(psis,n-1))+slowlap(at(psis,n-2))
        return (sp.diff(flat,t)-c.dot(grad(at(vs,n-1)))
            +lam*sum(fastbr(at(psis,i),at(zs,n-1-i)) for i in range(n))
            +sum(slowbr(at(psis,i),at(zs,n-2-i)) for i in range(n-1))
            -nu*(K*sp.diff(flat,s,2)+lam*D1(at(zs,n-1))+slowlap(at(zs,n-2))))
    V=sum(vs); Psi=sum(psis); Z=lap(Psi)
    check("finite_graded_vorticity_includes_shifted_final_terms",Z-sum(zs),
          "three-level polynomial grading audit with lambda, kappa, nu symbolic")
    direct_theta=(sp.diff(V,t)+lam*b*sp.diff(Psi,s)+(J*grad(Psi)).dot(e)
        +lam*fastbr(Psi,V)+slowbr(Psi,V)-kappa*lap(V))
    principal_theta=sum(sp.diff(vs[j],t)+b/(lam*q)*ws[j]
        -kappa*K*sp.diff(vs[j],s,2) for j in range(N+1))
    check("finite_scalar_grade_decomposition_including_diffusion",direct_theta-principal_theta
        -sum(source_theta(n) for n in range(1,2*N+3)),
        "three-level polynomial grading audit with lambda, kappa, nu symbolic")
    direct_omega=(sp.diff(Z,t)+lam*fastbr(Psi,Z)+slowbr(Psi,Z)
        -lam*zeta[0]*sp.diff(V,s)-c.dot(grad(V))-nu*lap(Z))
    principal_omega=sum(sp.diff(sp.diff(ws[j],t)-lam*zeta[0]*vs[j]
        -nu*K*sp.diff(ws[j],s,2),s) for j in range(N+1))
    check("finite_vorticity_grade_decomposition_including_diffusion",direct_omega-principal_omega
        -sum(source_omega(n) for n in range(1,2*N+5)),
        "three-level polynomial grading audit with lambda, kappa, nu symbolic")
    check("scalar_grades_above_2Nplus2_vanish",source_theta(2*N+3),"finite index audit")
    check("vorticity_grades_above_2Nplus4_vanish",source_omega(2*N+5),"finite index audit")

    # Full momentum lift in physical coordinates for the same moving chart.
    x1,x2=sp.symbols("x1 x2",real=True)
    x=sp.Matrix([x1,x2])
    def evaluate(f):
        aa=M.inv()*x
        return f.subs({s:lam*zeta.dot(x),a1:aa[0],a2:aa[1]},simultaneous=True)
    def gradx(f):
        return sp.Matrix([sp.diff(f,x1),sp.diff(f,x2)])
    def lapx(f):
        return sp.diff(f,x1,2)+sp.diff(f,x2,2)
    def advx(v,f):
        return v.dot(gradx(f))
    testpsi=(t+1)*(s**3+a1**2*s+a2**3)
    testv=(t**2+1)*(s**2+a1*a2)
    vprof=J*physicalgrad(testpsi)
    vel=J*gradx(evaluate(testpsi))
    ub=D*x
    physical_force=sp.diff(vel,t)+sp.Matrix([advx(ub,vel[j]) for j in range(2)])
    physical_force+=D*vel+sp.Matrix([advx(vel,vel[j]) for j in range(2)])
    physical_force-=nu*sp.Matrix([lapx(vel[j]) for j in range(2)])+evaluate(testv)*sp.Matrix([0,1])
    forceprofile=(2*D*vprof+J*physicalgrad(sp.diff(testpsi,t))
        +sp.Matrix([vprof.dot(physicalgrad(vprof[j])) for j in range(2)])
        -nu*J*physicalgrad(lap(testpsi))-testv*sp.Matrix([0,1]))
    check("full_compact_momentum_force_lift",physical_force-forceprofile.applyfunc(evaluate),
          "exact polynomial vector lift in time-dependent shear chart")
    ztest=lap(testpsi)
    residual_curl=(sp.diff(ztest,t)+lam*fastbr(testpsi,ztest)+slowbr(testpsi,ztest)
        -lam*zeta[0]*sp.diff(testv,s)-c.dot(grad(testv))-nu*lap(ztest))
    check("curl_of_full_vector_force",sp.diff(physical_force[1],x1)-sp.diff(physical_force[0],x2)
          -evaluate(residual_curl),"exact polynomial vector lift in time-dependent shear chart")

    payload={"sympy_version":sp.__version__,"all_passed":True,"check_count":len(records),
        "scope":"Exact finite localized identities, moving metric/envelope, and viscous finite grading; no limiting cascade or blowup claim.",
        "checks":records,
        "proof_sha256":hashlib.sha256((root/"tex/localized_layer.tex").read_bytes()).hexdigest()}
    target=root/"checks/localized_layer_checks.json"
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(f"{len(records)} exact localized-layer checks passed; wrote {target}")


if __name__=="__main__":
    main()
