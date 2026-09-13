"""Exact finite Gamma metric transfer checks; no analytic/Lean certificate.

The positive calibration has lambda=1, k=2, B(t)=1+t^2/4,
and chi(S)=(S-1)^2-2.  It is explicitly an algebraic calibration,
not a packet of actual zeros.  Both reference and arithmetic masses remain.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import sympy as sp

u, t, z, S = sp.symbols("u t z S", real=True)
I = sp.I


def polynomials(alpha, degree, variable):
    out = [sp.Integer(1)]
    if degree:
        out.append(variable)
    for n in range(1, degree):
        out.append(sp.expand(variable*out[n]-n*(n+alpha-1)*out[n-1]))
    return out


def coefficients(p, basis, variable):
    rest = sp.Poly(sp.expand(p), variable)
    answer = [sp.Integer(0)]*len(basis)
    for j in range(len(basis)-1, -1, -1):
        answer[j] = rest.nth(j)
        rest = sp.Poly(rest.as_expr()-answer[j]*basis[j], variable)
    if rest.as_expr() != 0:
        raise RuntimeError("Incomplete exact monic expansion")
    return answer


def gamma_moments(alpha, mass, degree):
    # Independent Jacobi walk: multiply u repeatedly in the monic basis.
    state = {0: sp.Integer(1)}
    out = []
    for power in range(degree+1):
        out.append(sp.expand(mass*state.get(0, 0)))
        nxt = {}
        for j, v in state.items():
            nxt[j+1] = nxt.get(j+1, 0)+v
            if j:
                nxt[j-1] = nxt.get(j-1, 0)+v*j*(j+alpha-1)
        state = nxt
    return out


def moment(p, moments, variable=u):
    p = sp.Poly(sp.expand(p), variable)
    return sp.expand(sum(v*moments[m[0]] for m, v in p.terms()))


def eq(a, b):
    if isinstance(a, sp.MatrixBase) or isinstance(b, sp.MatrixBase):
        a, b = sp.Matrix(a), sp.Matrix(b)
        return a.shape == b.shape and all(sp.cancel(x-y) == 0 for x, y in zip(a, b))
    return sp.cancel(a-b) == 0


def quotient(H, chi, degree):
    q = sp.degree(chi, S)
    J = sp.zeros(q, degree+1)
    for j in range(degree+1):
        rem = sp.Poly(sp.rem(S**j, chi, S), S)
        for i in range(q):
            J[i, j] = rem.nth(i)
    B = sp.zeros(degree+1, degree-q+1)
    for j in range(degree-q+1):
        col = sp.Poly(sp.expand(chi*S**j), S)
        for i in range(degree+1):
            B[i, j] = col.nth(i)
    G = (J*H.inv()*J.H).inv().applyfunc(sp.cancel)
    R = (H.inv()*J.H*G).applyfunc(sp.cancel)
    return J, B, G, R


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fault", choices=["mass", "tensor-cross", "boundary-sign", "conjugation", "schur-denominator"])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = []
    def check(name, value):
        checks.append({"name": name, "passed": bool(value)})

    mass = sp.Rational(1, 2)
    tensor_mass = mass**2
    alpha = sp.Integer(2)
    beta = sp.Integer(4)
    bs = polynomials(alpha, 12, t)
    bk = polynomials(beta, 12, u)
    one_ref = gamma_moments(alpha, mass, 14)
    sum_ref = gamma_moments(beta, tensor_mass, 12)
    for j in range(7):
        for l in range(7):
            check(f"monic_reference_pair_{j}_{l}", eq(moment(bk[j]*bk[l], sum_ref), tensor_mass*sp.factorial(j)*sp.rf(beta,j) if j == l else 0))
    B1 = 1+t*t/4
    one_arith = [moment(B1*t**j, one_ref, t) for j in range(11)]
    direct = [sp.expand(sum(sp.binomial(n,j)*one_arith[j]*one_arith[n-j] for j in range(n+1))) for n in range(9)]
    c = [sp.cancel(moment(B1*bs[j], one_ref, t)/(mass*sp.factorial(j)*sp.rf(alpha,j))) for j in range(9)]
    A = sp.expand(sum(sp.rf(alpha,j)*c[j]*z**j for j in range(9)))
    d = [sp.expand(A*A).coeff(z,j) for j in range(9)]
    Bsum = sp.expand(sum(d[j]*bk[j]/sp.rf(beta,j) for j in range(9)))
    check("one_factor_mass", eq(one_arith[0], sp.Rational(3,4)))
    check("two_factor_mass", eq(direct[0], sp.Rational(9,16)))
    check("finite_sum_multiplier", eq(Bsum, sp.Rational(54,35)+sp.Rational(39,280)*u**2+sp.Rational(3,1120)*u**4))
    observed_d4 = sp.Integer(0) if args.fault == "tensor-cross" else d[4]
    check("retained_tensor_cross_coefficient", eq(observed_d4, sp.Rational(9,4)))
    for n in range(9):
        check(f"independent_tensor_moment_{n}", eq(moment(Bsum*u**n, sum_ref), direct[n]))
    M = sp.Matrix(4,4,lambda a,b: moment((1-I*u)**a*(1+I*u)**b,direct))
    Mref = sp.Matrix(4,4,lambda a,b: moment((1-I*u)**a*(1+I*u)**b,sum_ref))
    for a in range(4):
        for b in range(4):
            L = coefficients((1-I*u)**a*(1+I*u)**b, bk, u)
            value = tensor_mass*sum(sp.factorial(n)*L[n]*d[n] for n in range(7))
            check(f"finite_gram_entry_{a}_{b}", eq(value,M[a,b]))
    observed_mass = sp.Integer(1) if args.fault == "mass" else tensor_mass
    check("finite_gram_mass_factor", eq(observed_mass*d[0],M[0,0]))
    check("original_coordinate_hermitian", M == M.H)
    wrong_pair = moment((1+I*u)**2,direct) if args.fault == "conjugation" else moment((1-I*u)*(1+I*u),direct)
    check("original_coordinate_conjugation", eq(wrong_pair,M[1,1]))
    chi = (S-1)**2-2
    J,B,G,R = quotient(M,chi,3)
    J0,B0,G0,R0 = quotient(Mref,chi,3)
    check("same_original_relation", J == J0 and B == B0)
    check("relation_kernel", J*B == sp.zeros(2,2))
    check("least_lift_right_inverse", eq(J*R,sp.eye(2)))
    check("least_lift_boundary_orthogonality", eq(B.H*M*R,sp.zeros(2,2)))
    check("least_lift_gram", eq(R.H*M*R,G))
    E = M-Mref
    F = B.H*E*B
    C = B.H*E*R0
    D0 = B.H*Mref*B
    exact_R = R0-B*(D0+F).inv()*C
    check("boundary_resolvent_lift", eq(R,exact_R))
    sign = 1 if args.fault == "boundary-sign" else -1
    exact_G = G0+R0.H*E*R0+sign*C.H*(D0+F).inv()*C
    check("boundary_resolvent_quadratic_loss", eq(G,exact_G))
    check("boundary_resolvent_loss_nonzero", not eq(C.H*(D0+F).inv()*C,sp.zeros(2,2)))
    for numer in range(5):
        a = sp.Rational(numer,4)
        H = Mref+a*E
        _,_,Ga,Ra = quotient(H,chi,3)
        check(f"resolvent_path_metric_{numer}",eq(Ga,G0+a*R0.H*E*R0-a*a*C.H*(D0+a*F).inv()*C))
        check(f"resolvent_path_lift_{numer}",eq(Ra,R0-a*B*(D0+a*F).inv()*C))
    Hminus = M[:2,:2]
    Cdeg = M[:2,2:]
    W = (M[2:,2:]-Cdeg.H*Hminus.inv()*Cdeg).applyfunc(sp.cancel)
    Edeg = (J[:,2:]-J[:,:2]*Hminus.inv()*Cdeg).applyfunc(sp.cancel)
    Kminus = J[:,:2]*Hminus.inv()*J[:,:2].H
    Gminus = Kminus.inv()
    Z = (Edeg.H*Gminus*Edeg).applyfunc(sp.cancel)
    check("two_degree_kernel_update",eq(G.inv(),Kminus+Edeg*W.inv()*Edeg.H))
    check("two_degree_volume_ratio",eq(Gminus.det()/G.det(),(W+Z).det()/W.det()))
    check("two_degree_ratio_expansion",eq((W+Z).det()/W.det(),1+sp.trace(W.inv()*Z)+Z.det()/W.det()))
    alpha3 = M.det()*M[:2,:2].det()/M[:3,:3].det()**2
    denom = W[0,0] if args.fault == "schur-denominator" else W[0,0]**2
    check("two_degree_source_recurrence",eq(alpha3,W.det()/denom))
    check("two_degree_positive_W_pivots",W[0,0]>0 and W.det()>0)
    check("determinant_line_original_orientation",eq(sp.eye(4)[:,:2].row_join(B).det(),1))
    check("source_relation_quotient_volume",eq(G.det(),M.det()/(B.H*M*B).det()))
    # Exact entrywise envelope and quotient propagation, without density infimum.
    error = sp.Rational(1,10000)
    Delta = error*sp.eye(4)
    low, high = M-Delta, M+Delta
    check("envelope_low_LDL_positive", all(low[:j,:j].det()>0 for j in range(1,5)))
    _,_,Glow,_ = quotient(low,chi,3)
    _,_,Ghigh,_ = quotient(high,chi,3)
    check("quotient_lower_envelope", all((G-Glow)[:j,:j].det()>0 for j in range(1,3)))
    check("quotient_upper_envelope", all((Ghigh-G)[:j,:j].det()>0 for j in range(1,3)))
    low_ratio = low[:2,:2].det()/Ghigh.det()
    high_ratio = high[:2,:2].det()/Glow.det()
    ratio = Gminus.det()/G.det()
    check("consecutive_ratio_enclosed",low_ratio<ratio<high_ratio)
    gamma_ratio = Mref[:2,:2].det()/G0.det()
    check("relative_correction_exact",eq(ratio/gamma_ratio,sp.Rational(100955,111834)))
    check("bounded_calibration_tail_entry_radius",8192*sp.Rational(4515,4)*sp.factorial(8)/2**92 < sp.Rational(1,40000))
    check("bounded_calibration_upper_below_reference",high_ratio<gamma_ratio)
    check("bounded_calibration_lower_above_one",low_ratio>1)
    # Explicit representative-coefficient and quotient-loss enclosure GMT.29a/b.
    Htest=M+error*sp.eye(4)/2
    _,_,Gtest,Rtest=quotient(Htest,chi,3)
    Alo=B.H*low*B
    smat=abs(B).T*(error*sp.eye(4)/2)*abs(R)
    ki=sp.Matrix(2,2,lambda a,b:(Alo.inv()[a,a]+Alo.inv()[b,b])/2)
    er=abs(B)*ki*smat
    diff=Rtest-R
    actual_Ainv=(B.H*Htest*B).inv()
    tau=smat.T*abs(Alo.inv())*smat
    Dq=sp.diag(*[sum(tau[i,j] for j in range(2)) for i in range(2)])
    loss=(R.H*Htest*R-Gtest).applyfunc(sp.cancel)
    SE=B.H*(Htest-M)*R
    check("representative_coefficients_enclosed",all(abs(diff[i,j])<=er[i,j] for i in range(4) for j in range(2)))
    check("representative_loss_exact",eq(loss,diff.H*Htest*diff))
    check("representative_loss_boundary_inverse",eq(loss,SE.H*actual_Ainv*SE))
    check("representative_loss_upper_enclosed",all((Dq-loss)[:j,:j].det()>0 for j in range(1,3)))
    check("representative_boundary_inverse_entries",all(abs(actual_Ainv[a,b])<=ki[a,b] for a in range(2) for b in range(2)))
    check("representative_error_original_zero_jet",eq(J*diff,sp.zeros(2,2)))
    # Every tested original source has positive full rational pivots.
    check("arithmetic_source_pivots",all(M[:j,:j].det()>0 for j in range(1,5)))
    payload = {
        "schema":"gamma-finite-metric-transfer-exact-check-v1",
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_optimized":bool(sys.flags.optimize),
        "sympy_version":sp.__version__,
        "fault":args.fault,
        "scope":"Exact rational algebraic calibration; no actual zero-packet inference, no numerical analytic certificate, no Lean.",
        "fixture":{key:str(value) for key,value in {
            "lambda":1,"k":2,"gamma_one_mass":mass,"gamma_sum_mass":tensor_mass,
            "arithmetic_one_mass":one_arith[0],"arithmetic_sum_mass":direct[0],
            "chi_original_S":chi,"A_coefficient_series":A,"sum_multiplier":Bsum,
            "sum_moments_0_to_8":direct,"M_original_S":M,"M_reference_original_S":Mref,
            "G_degree_1":Gminus,"G_degree_3":G,"R_degree_3":R,
            "G_reference_degree_3":G0,"W_two_degree":W,"E_two_degree":Edeg,
            "Z_two_degree":Z,"volume_ratio_1_to_3":ratio,
            "source_recurrence_a3":alpha3,"ratio_lower":low_ratio,"ratio_upper":high_ratio,
            "gamma_volume_ratio_1_to_3":gamma_ratio,"relative_correction_ratio":ratio/gamma_ratio,
            "bounded_calibration_entry_error_upper":8192*sp.Rational(4515,4)*sp.factorial(8)/2**92,
            "representative_error_matrix_upper":er,"representative_loss_matrix_upper":Dq,
            "boundary_quadratic_loss":C.H*(D0+F).inv()*C,
        }.items()},
        "check_count":len(checks),"failed_count":sum(not c["passed"] for c in checks),"checks":checks,
    }
    output=json.dumps(payload,indent=2)+"\n"
    if args.output:
        args.output.write_text(output,encoding="utf-8")
    print(json.dumps({"checks":len(checks),"failed":payload["failed_count"],"fault":args.fault,"output":str(args.output) if args.output else None}))
    return 1 if payload["failed_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
