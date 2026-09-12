#!/usr/bin/env python3
"""Exact finite Gaussian calibration of the retained Stieltjes pair.

The source moment matrix is computed directly in powers of s=1/2+i*t.
Its constrained minimum is compared with two independently constructed
orthogonal-polynomial kernels on x=t^2.  The measures here are explicitly
Gaussian polynomial models, not enclosures of the arithmetic theta measure.
The Gaussian measure and the residue unit are independent finite inputs;
the formal polynomial g_model=h*v does not generate that Gaussian density.
All conditions use explicit exceptions/records and survive python -O.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
s, z, x, t = sp.symbols("s z x t", real=True)
HALF = sp.Rational(1, 2)
RECORDS = []


def equal(a, b):
    if isinstance(a, sp.MatrixBase) or isinstance(b, sp.MatrixBase):
        if a.shape != b.shape:
            return False
        return all(sp.cancel(v) == 0 for v in (a-b))
    return sp.cancel(sp.expand(a-b)) == 0


def check(name, passed, kind="exact", **evidence):
    ok = bool(passed)
    RECORDS.append(dict(name=name, kind=kind, passed=ok, **evidence))
    if not ok:
        raise ArithmeticError(name)


def expect(name, a, b, **evidence):
    check(name, equal(a, b), **evidence)


def reject(name, a, b):
    check(name, not equal(a, b), kind="negative_control")


@lru_cache(None)
def gaussian_moment(j):
    if j % 2:
        return sp.S.Zero
    return sp.S.One if j == 0 else sp.factorial2(j-1)


def integrate_t(poly, mass=sp.S.One):
    return mass*sum(c*gaussian_moment(j) for (j,), c in sp.Poly(sp.expand(poly), t).terms())


def source_pair(f, g, mass):
    fv = sp.expand(f.subs(s, HALF+sp.I*t))
    gv = sp.expand(g.subs(s, HALF+sp.I*t))
    return sp.expand(integrate_t(sp.conjugate(fv)*gv, mass))


def stieltjes_pair(f, g, mass, power=0):
    poly = sp.Poly(sp.expand(sp.conjugate(f)*g*x**power), x)
    return mass*sum(c*gaussian_moment(2*j) for (j,), c in poly.terms())


def monic_family(variable, maximum, pairing):
    polys, norms = [], []
    for n in range(maximum+1):
        p = variable**n
        for q, norm in zip(polys, norms):
            p -= q*pairing(q, variable**n)/norm
        p = sp.expand(p)
        norm = sp.expand(pairing(p, p))
        if not (norm.is_Rational and norm > 0):
            raise ArithmeticError("Nonpositive model norm")
        polys.append(p)
        norms.append(norm)
    return polys, norms


def rem(poly, modulus, variable):
    return sp.rem(sp.Poly(poly, variable), sp.Poly(modulus, variable)).as_expr().expand()


def vector(poly, variable, degree):
    p = sp.Poly(sp.expand(poly), variable)
    return sp.Matrix([p.nth(j) for j in range(degree)])


def multiplication(poly, modulus, variable):
    degree = sp.degree(modulus, variable)
    return sp.Matrix.hstack(*[vector(rem(poly*variable**j, modulus, variable), variable, degree)
                              for j in range(degree)])


def original_to_pair(poly, H):
    D = int(sp.degree(H, x))
    p = sp.Poly(sp.expand(poly.subs(s, z+HALF)), z)
    even = sum(c*(-1)**(j//2)*x**(j//2) for (j,), c in p.terms() if j % 2 == 0)
    odd = sum(c*(-1)**((j-1)//2)*x**((j-1)//2) for (j,), c in p.terms() if j % 2)
    return vector(rem(even, H, x), x, D).col_join(vector(rem(odd, H, x), x, D))


def pair_to_original(v, h):
    D = v.rows//2
    p = sum(v[j]*(-(s-HALF)**2)**j for j in range(D))
    p += (s-HALF)*sum(v[D+j]*(-(s-HALF)**2)**j for j in range(D))
    return rem(p, h, s)


def run_model(name, H, V, mass, stages, frontier=None):
    prefix = name+":"
    H, V = sp.expand(H), sp.expand(V)
    D = int(sp.degree(H, x)); d = 2*D
    h = sp.expand((-1)**D*H.subs(x, -(s-HALF)**2))
    unit = sp.expand(V.subs(x, -(s-HALF)**2))
    check(prefix+"monic_original_h", sp.Poly(h, s).LC() == 1)
    # Formal polynomial g=h*v retains the sign relating H to h. This polynomial
    # supplies the unit algebra test only; its modulus is not the Gaussian density.
    F = sp.expand((-1)**D*H*V)
    expect(prefix+"full_g_model", F.subs(x,-(s-HALF)**2), h*unit)
    expect(prefix+"original_unit_from_F_over_H", (-1)**D*sp.cancel(F/H), V)
    if D % 2:
        reject(prefix+"reject_h_global_sign", h, H.subs(x,-(s-HALF)**2))
        reject(prefix+"reject_unit_global_sign", sp.cancel(F/H), V)
    check(prefix+"unit_coprime", sp.gcd(H, V) == 1)
    T = sp.Matrix.hstack(*[original_to_pair(s**j, H) for j in range(d)])
    Ti = T.inv()
    expect(prefix+"coordinate_determinant", T.det(), (-1)**(D*(D-1)//2), determinant=str(T.det()))
    for j in range(d):
        expect(prefix+f"inverse_coordinate_{j}", pair_to_original(T[:, j], h), s**j)
    A = multiplication(s, h, s)
    X = multiplication(x, H, x)
    B = sp.zeros(d)
    B[:D, D:] = -X
    B[D:, :D] = sp.eye(D)
    Ap = HALF*sp.eye(d)+B
    expect(prefix+"original_generator", T*A*Ti, Ap)
    cp = A.charpoly()
    expect(prefix+"original_characteristic_polynomial", cp.as_expr().subs(cp.gen,s), h)
    reject(prefix+"reject_positive_X_block", T*A*Ti, HALF*sp.eye(d)+sp.BlockMatrix([[sp.zeros(D), X], [sp.eye(D), sp.zeros(D)]]).as_explicit())
    reject(prefix+"reject_missing_half", T*A*Ti, B)
    VM = multiplication(V, H, x)
    UV = multiplication(unit, h, s)
    V2 = sp.diag(VM, VM)
    expect(prefix+"complete_even_unit", T*UV*Ti, V2)
    expected_det_v = sp.resultant(H, V, x)
    expect(prefix+"unit_determinant", VM.det(), expected_det_v)
    expect(prefix+"original_unit_determinant", UV.det(), expected_det_v**2)

    maxN = max(stages)
    P, pn = monic_family(x, maxN//2+1, lambda f,g: stieltjes_pair(f,g,mass))
    R, rn = monic_family(x, (maxN-1)//2+1, lambda f,g: stieltjes_pair(f,g,mass,1))
    Q, qn = monic_family(s, maxN+1, lambda f,g: source_pair(f,g,mass))
    for n in range(maxN//2+1):
        expect(prefix+f"even_polynomial_{n}", Q[2*n], (-1)**n*P[n].subs(x, -(s-HALF)**2))
        expect(prefix+f"even_norm_{n}", qn[2*n], pn[n])
        expect(prefix+f"Gaussian_even_norm_{n}", pn[n], mass*sp.factorial(2*n))
    for n in range((maxN-1)//2+1):
        expect(prefix+f"odd_polynomial_{n}", Q[2*n+1], (-1)**n*(s-HALF)*R[n].subs(x, -(s-HALF)**2))
        expect(prefix+f"odd_norm_{n}", qn[2*n+1], rn[n])
        ratio = sp.cancel(P[n+1].subs(x,0)/P[n].subs(x,0))
        expect(prefix+f"Christoffel_polynomial_{n}", x*R[n], P[n+1]-ratio*P[n])
        reject(prefix+f"reject_Christoffel_numerator_sign_{n}", x*R[n], P[n+1]+ratio*P[n])
        expect(prefix+f"Christoffel_norm_{n}", rn[n], -ratio*pn[n])
        reject(prefix+f"reject_Christoffel_norm_sign_{n}", rn[n], ratio*pn[n])
        expect(prefix+f"Gaussian_odd_norm_{n}", rn[n], mass*sp.factorial(2*n+1))
    reject(prefix+"reject_even_sign", Q[2], P[1].subs(x, -(s-HALF)**2))
    reject(prefix+"reject_odd_sign", Q[3], (s-HALF)*R[1].subs(x, -(s-HALF)**2))
    expect(prefix+"odd_weight_orthogonality", stieltjes_pair(R[0],R[1],mass,1),0)
    reject(prefix+"reject_omitted_odd_weight", stieltjes_pair(R[0],R[1],mass,0),0)

    # Local value-and-derivative data are checked without dropping repeated jets.
    sqh = sp.Poly(h,s).sqf_part().as_expr()
    h_degree = int(sp.degree(h,s)); sq_degree = int(sp.degree(sqh,s))
    if sq_degree < h_degree:
        hsquare_matrix = sum((c*A**j for (j,),c in sp.Poly(sqh,s).terms()), sp.zeros(d))
        reject(prefix+"reject_squarefree_annihilator", hsquare_matrix, sp.zeros(d))
        actual_annihilator = sum((c*A**j for (j,),c in sp.Poly(h,s).terms()), sp.zeros(d))
        expect(prefix+"complete_annihilator", actual_annihilator, sp.zeros(d))

    source_kernels = {}; pair_kernels = {}
    for N in stages:
        pfx = prefix+f"N{N}:"
        check(pfx+"full_surjection_threshold", N >= d-1)
        M = sp.Matrix(N+1,N+1,lambda i,j: source_pair(s**i,s**j,mass))
        J = sp.Matrix.hstack(*[vector(rem(unit*s**j,h,s),s,d) for j in range(N+1)])
        K = J*M.inv()*J.conjugate().T
        G = K.inv()
        rep = M.inv()*J.conjugate().T*G
        expect(pfx+"source_jet_identity", J*rep, sp.eye(d))
        expect(pfx+"source_minimum_Gram", rep.conjugate().T*M*rep, G)
        for no, kernel_vector in enumerate(J.nullspace()):
            expect(pfx+f"source_minimum_orthogonal_{no}", kernel_vector.conjugate().T*M*rep, sp.zeros(1,d))
        expect(pfx+"source_moment_determinant", M.det(), sp.prod(qn[j] for j in range(N+1)))
        check(pfx+"source_positive_pivots", all(M[:j,:j].det()>0 for j in range(1,N+2)))
        Kp_direct = T*K*T.conjugate().T
        Gp_direct = Ti.conjugate().T*G*Ti
        ke, ko, ke0, ko0 = (sp.zeros(D) for _ in range(4))
        for n in range(N//2+1):
            pe=vector(rem(P[n],H,x),x,D)
            ve=vector(rem(V*P[n],H,x),x,D)
            ke+=ve*ve.conjugate().T/pn[n]
            ke0+=pe*pe.conjugate().T/pn[n]
        for n in range((N-1)//2+1):
            po=vector(rem(R[n],H,x),x,D)
            vo=vector(rem(V*R[n],H,x),x,D)
            ko+=vo*vo.conjugate().T/rn[n]
            ko0+=po*po.conjugate().T/rn[n]
        Kp=sp.diag(ke,ko)
        expect(pfx+"independent_pair_kernels", Kp_direct, Kp)
        expect(pfx+"inverse_metric_transport", Gp_direct, sp.diag(ke.inv(),ko.inv()))
        expect(pfx+"complete_unit_kernel", Kp, V2*sp.diag(ke0,ko0)*V2.conjugate().T)
        reject(pfx+"reject_omitted_unit", Kp, sp.diag(ke0,ko0))
        expect(pfx+"kernel_determinant_pair", K.det(), ke.det()*ko.det())
        expect(pfx+"metric_determinant_pair", G.det(), 1/(ke.det()*ko.det()))
        expect(pfx+"unit_determinant_kernel", Kp.det(), expected_det_v**4*ke0.det()*ko0.det())
        expect(pfx+"T_determinant_transport", Kp.det(), T.det()*sp.conjugate(T.det())*K.det())
        W=A.conjugate().T*G+G*A-G
        Wp=Ti.conjugate().T*W*Ti
        ge,go=ke.inv(),ko.inv()
        off=go-ge*X
        expectedW=sp.BlockMatrix([[sp.zeros(D),off],[off.conjugate().T,sp.zeros(D)]]).as_explicit()
        expect(pfx+"weight_offblock", Wp, expectedW)
        expect(pfx+"original_weight_transport", W, T.conjugate().T*expectedW*T)
        expect(pfx+"weight_determinant", Wp.det(), (-1)**D*off.det()*sp.conjugate(off.det()))
        expect(pfx+"weight_determinant_original", W.det(), Wp.det())
        relative=G.inv()*W
        squared_pair=ge.inv()*off*go.inv()*off.conjugate().T
        expect(pfx+"relative_square_trace",sp.trace(relative**2),2*sp.trace(squared_pair))
        rr=relative.charpoly(); pr=squared_pair.charpoly()
        expect(pfx+"complete_relative_eigenvalue_pairing",rr.as_expr(),pr.as_expr().subs(pr.gen,rr.gen**2))
        # SP.32--35: compare the full kernel discrepancy and a directly computed
        # original-source derivative cost, including both zero-frontier cases.
        ni=N//2
        ei=vector(rem(V*R[ni],H,x),x,D)
        if N % 2==0:
            fi=vector(rem(V*P[ni],H,x),x,D)
            denom=pn[ni]; endpoint=fi*ei.conjugate().T/denom
            cost=(rn[ni]+(ei.conjugate().T*go*ei)[0])*(fi.conjugate().T*ge*fi)[0]/denom**2
            allowance=(ei.conjugate().T*go*ei)[0]/rn[ni]
        else:
            fi=vector(rem(V*P[ni+1],H,x),x,D)
            denom=rn[ni]; endpoint=-fi*ei.conjugate().T/denom
            cost=(pn[ni+1]+(fi.conjugate().T*ge*fi)[0])*(ei.conjugate().T*go*ei)[0]/denom**2
            allowance=(fi.conjugate().T*ge*fi)[0]/pn[ni+1]
        expect(pfx+"SP32_full_kernel_compatibility",ke-X*ko,endpoint)
        if not equal(endpoint,sp.zeros(D)):
            reject(pfx+"reject_SP32_parity_sign",ke-X*ko,-endpoint)
        eps2=(fi.conjugate().T*ge*fi)[0]*(ei.conjugate().T*go*ei)[0]/denom**2
        expect(pfx+"SP33_full_squared_singular_trace",sp.trace(squared_pair),eps2)
        check(pfx+"SP33_rank_two_weight",W.rank()<=2)
        expect(pfx+"SP33_all_remaining_zero_eigenvalues",rr.as_expr(),rr.gen**(d-2)*(rr.gen**2-eps2))
        Mplus=sp.Matrix(N+2,N+2,lambda i,j:source_pair(s**i,s**j,mass))
        shifted=sp.zeros(1,d).col_join(rep)
        padded=rep.col_join(sp.zeros(1,d))
        boundary=shifted-padded*A
        Jplus=sp.Matrix.hstack(*[vector(rem(unit*s**j,h,s),s,d) for j in range(N+2)])
        expect(pfx+"SP34_original_boundary_full_zero_jet",Jplus*boundary,sp.zeros(d))
        relation_vectors=J.nullspace()
        if relation_vectors:
            relations=sp.Matrix.hstack(*relation_vectors).col_join(sp.zeros(1,len(relation_vectors)))
            layer_boundary=boundary-relations*(relations.conjugate().T*Mplus*relations).inv()*relations.conjugate().T*Mplus*boundary
        else:
            layer_boundary=boundary
        original_cost=sp.trace(G.inv()*layer_boundary.conjugate().T*Mplus*layer_boundary)
        expect(pfx+"SP34_direct_original_derivative_cost",original_cost,cost)
        newcol=vector(rem(unit*Q[N+1],h,s),s,d)
        Knext_direct=Jplus*Mplus.inv()*Jplus.conjugate().T
        pi_direct=K.det()/Knext_direct.det()
        expect(pfx+"SP35_direct_determinant_ratio",pi_direct,1/(1+allowance))
        expect(pfx+"SP35_exact_energy_identity",eps2,(1-pi_direct)*original_cost)
        if equal(newcol,sp.zeros(d,1)):
            expect(pfx+"SP35_new_zero_frontier_pi",pi_direct,1)
            check(pfx+"SP35_new_zero_cost_retained",original_cost>0)
        oldcol=vector(rem(unit*Q[N],h,s),s,d)
        if equal(oldcol,sp.zeros(d,1)):
            expect(pfx+"SP35_predecessor_zero_cost",original_cost,0)
            check(pfx+"SP35_predecessor_zero_contraction_retained",pi_direct<1)
        if D > 1:
            reject(pfx+"reject_wrong_metric_transport", T.conjugate().T*G*T, Gp_direct)
            reject(pfx+"reject_wrong_kernel_transport", Ti*K*Ti.conjugate().T, Kp_direct)
        # The source mass is retained: multiplying all norms by mass is not erased.
        Mmass1 = M/mass
        Kmass1=J*Mmass1.inv()*J.conjugate().T
        expect(pfx+"mass_scaling_kernel", Kmass1, mass*K)
        expect(pfx+"mass_scaling_metric", Kmass1.inv(), G/mass)
        expect(pfx+"mass_scaling_determinant", Kmass1.det(), mass**d*K.det())
        if mass != 1:
            reject(pfx+"reject_mass_erasure", Kmass1, K)
        if sq_degree < h_degree:
            Jdeleted=sp.Matrix.hstack(*[vector(rem(unit*s**j,sqh,s),s,d) for j in range(N+1)])
            Kdeleted=Jdeleted*M.inv()*Jdeleted.conjugate().T
            reject(pfx+"reject_deleted_nilpotents", Kdeleted, K)
            check(pfx+"deleted_nilpotent_rank_loss", Kdeleted.rank()==sq_degree and K.rank()==d)
        source_kernels[N]=K
        pair_kernels[N]=(ke,ko)

    for N in stages:
        if N+1 not in source_kernels:
            continue
        pfx=prefix+f"update_{N}_{N+1}:"
        v=vector(rem(unit*Q[N+1],h,s),s,d)
        Kprev,Knext=source_kernels[N],source_kernels[N+1]
        expect(pfx+"original_rank_one_update",Knext,Kprev+v*v.conjugate().T/qn[N+1])
        scalar=(v.conjugate().T*Kprev.inv()*v)[0]/qn[N+1]
        expect(pfx+"original_determinant_update",Kprev.det()/Knext.det(),1/(1+scalar))
        ke,ko=pair_kernels[N]; ken,kon=pair_kernels[N+1]
        vp=T*v
        if N % 2:
            expect(pfx+"odd_stage_odd_block_fixed",kon,ko)
            expect(pfx+"odd_stage_even_block_update",ken,ke+vp[:D,:]*vp[:D,:].conjugate().T/qn[N+1])
        else:
            expect(pfx+"even_stage_even_block_fixed",ken,ke)
            expect(pfx+"even_stage_odd_block_update",kon,ko+vp[D:,:]*vp[D:,:].conjugate().T/qn[N+1])

    if frontier is not None:
        qj = rem(Q[frontier],h,s)
        expect(prefix+"zero_frontier_residue", qj, 0, frontier=frontier)
        expect(prefix+"zero_frontier_kernel_update", source_kernels[frontier],source_kernels[frontier-1])
        Km=source_kernels[frontier]
        Gm=Km.inv()
        expect(prefix+"zero_frontier_full_weight", A.conjugate().T*Gm+Gm*A-Gm,sp.zeros(d))

    return dict(name=name,H=str(H),V=str(V),mass=str(mass),h=str(h),
                dimension=d,stages=stages,zero_frontier=frontier,
                original_coordinate_order=[f"s^{j}" for j in range(d)],
                pair_coordinate_order=[f"x^{j}" for j in range(D)]+[f"z*x^{j}" for j in range(D)])


def run_local_branches():
    eta,w=sp.symbols("eta w")
    for m in range(1,5):
        for alpha in (sp.S.One,sp.I/2,sp.Rational(3,5)+sp.I*sp.Rational(4,5)):
            pfx=f"local_m{m}_alpha{alpha}:"
            Z=sp.expand(alpha*sum(sp.binomial(HALF,j)*(-eta/alpha**2)**j for j in range(m)))
            Zinv=sp.invert(Z,eta**m,eta)
            expect(pfx+"truncated_root_square",rem(Z**2,eta**m,eta),rem(alpha**2-eta,eta**m,eta))
            expect(pfx+"truncated_root_inverse",rem(Z*Zinv,eta**m,eta),1)
            for sign in (1,-1):
                a=sign*alpha
                eta_of_w=-2*a*w-w**2
                w_of_eta=sign*Z-a
                expect(pfx+f"branch{sign}_forward_inverse",rem(eta_of_w.subs(w,w_of_eta),eta**m,eta),rem(eta,eta**m,eta))
                expect(pfx+f"branch{sign}_inverse_forward",rem(w_of_eta.subs(eta,eta_of_w),w**m,w),rem(w,w**m,w))
                for j in range(m):
                    expect(pfx+f"branch{sign}_jet_power{j}",rem((w_of_eta.subs(eta,eta_of_w))**j,w**m,w),w**j)
                if m>1:
                    reject(pfx+f"branch{sign}_reject_deleted_jet",rem(w_of_eta,eta**m,eta),0)
                    reject(pfx+f"branch{sign}_reject_wrong_inverse_sign",rem(eta_of_w.subs(w,-w_of_eta),eta**m,eta),eta)
            ZM=multiplication(Z,eta**m,eta)
            branch=sp.BlockMatrix([[sp.eye(m),ZM],[sp.eye(m),-ZM]]).as_explicit()
            inverse=HALF*sp.BlockMatrix([[sp.eye(m),sp.eye(m)],[ZM.inv(),-ZM.inv()]]).as_explicit()
            expect(pfx+"two_branch_matrix_inverse",branch*inverse,sp.eye(2*m))
            expect(pfx+"two_branch_determinant",branch.det(),(-2*alpha)**m)
            def multiply_pair(left,right):
                a,b=left; c,e=right
                return (rem(a*c+(alpha**2-eta)*b*e,eta**m,eta),rem(a*e+b*c,eta**m,eta))
            ep=(HALF, Zinv/2); em=(HALF,-Zinv/2)
            for label,e in (("plus",ep),("minus",em)):
                ee=multiply_pair(e,e)
                expect(pfx+label+"_idempotent_even",ee[0],rem(e[0],eta**m,eta))
                expect(pfx+label+"_idempotent_odd",ee[1],rem(e[1],eta**m,eta))
            prod=multiply_pair(ep,em)
            expect(pfx+"opposite_idempotents_even",prod[0],0)
            expect(pfx+"opposite_idempotents_odd",prod[1],0)
            expect(pfx+"idempotent_sum",sp.Matrix(ep)+sp.Matrix(em),sp.Matrix([1,0]))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--self-test-failure",action="store_true")
    args=parser.parse_args()
    models=[]; error=None
    try:
        # D=4 checks the general orientation formula beyond the model dimensions.
        for D in range(1,5):
            H=(x+1)**D
            T=sp.Matrix.hstack(*[original_to_pair(s**j,H) for j in range(2*D)])
            expect(f"orientation_D{D}",T.det(),(-1)**(D*(D-1)//2))
        run_local_branches()
        models.append(run_model("double_off_line",(x+1)**2,1+x/2,sp.Rational(7,3),[3,4,5]))
        models.append(run_model("double_and_critical",(x+1)**2*(x-sp.Rational(1,4)),1+x/2,sp.S.One,[5,6]))
        models.append(run_model("even_zero_frontier",x-1,1+x/2,sp.Rational(7,3),[1,2,3],2))
        models.append(run_model("odd_zero_frontier",x-3,1+x/2,sp.S.One,[2,3,4],3))
        if args.self_test_failure:
            check("intentional_false_identity",sp.Rational(1,2)==1,kind="harness_negative_control")
    except Exception as exc:
        error=f"{type(exc).__name__}: {exc}"
    source=ROOT/"tex"/"theta_stieltjes_pair.tex"
    output=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                scope="Exact rational Gaussian polynomial models; no actual theta-moment enclosure, analytic proof, RH proof, or Lean execution.",
                independent_constructions="Original s-monomial Hermitian moment constrained minimum versus two x-Stieltjes Gram-Schmidt kernels, retaining full remainder algebras and original arithmetic-unit model.",
                model_coupling_scope="The Gaussian measure and residue unit are separately prescribed finite inputs. Formal g_model=h*v checks the sign/unit algebra and does not generate the Gaussian density; analytic coupling of the actual theta density and unit is not calibrated here.",
                python_version=sys.version,optimization_level=sys.flags.optimize,sympy_version=sp.__version__,
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None,
                models=models,total=len(RECORDS),passed=sum(r["passed"] for r in RECORDS),
                exact_checks=sum(r["kind"]=="exact" for r in RECORDS),
                negative_controls=sum(r["kind"]=="negative_control" for r in RECORDS),
                all_passed=error is None and all(r["passed"] for r in RECORDS),error=error,records=RECORDS)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:output[k] for k in ("total","passed","exact_checks","negative_controls","all_passed","error")},sort_keys=True))
    return 0 if output["all_passed"] else 1


if __name__=="__main__":
    raise SystemExit(main())
