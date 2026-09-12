#!/usr/bin/env python3
"""Independent finite frame calibration for FC.1--20.

Every frame, amplitude, coordinate and Jacobian is specified below. Exact
rational/complex arithmetic and Gaussian moments compare the original
derivative with the transported one. These are finite model calibrations,
not estimates for the arithmetic theta density or a verification of RH.
No Python assert, numerical quadrature or Lean execution is used.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
u, v, x, y, s = sp.symbols("u v x y s", real=True)
v = sp.Symbol("v", positive=True)
x = sp.Symbol("x", positive=True)
I = sp.I
RECORDS = []
E = sp.eye(2)
O = sp.zeros(2)


def same(a, b):
    if isinstance(a, sp.MatrixBase) or isinstance(b, sp.MatrixBase):
        return a.shape == b.shape and all(sp.cancel(sp.expand(z)) == 0 for z in a-b)
    return sp.cancel(sp.expand(a-b)) == 0


def record(name, passed, kind="exact", **evidence):
    passed = bool(passed)
    RECORDS.append(dict(name=name, passed=passed, kind=kind, **evidence))
    if not passed:
        raise ArithmeticError(name)


def eq(name, a, b, **evidence):
    record(name, same(a, b), **evidence)


def reject(name, a, b):
    record(name, not same(a, b), kind="negative_control")


def block(a, b, c, d):
    return a.row_join(b).col_join(c.row_join(d))


def frame(even=False):
    # The top I makes every frame injective for every real u. The two
    # nonorthogonal row directions produce noncommuting positive weights.
    a = 1+u**2 if even else 1+u
    b = 1+u**4 if even else 1+u**2
    return sp.Matrix([[1, 0], [0, 1], [a, a], [b, 2*b]])


def jet(j, point):
    jp = j.diff(u)
    jv, jpv = j.subs(u, point), jp.subs(u, point)
    w = jv.H*jv
    b = jv.H*jpv
    wp = jpv.H*jv+jv.H*jpv
    gamma = w.inv()*b
    proj = jv*w.inv()*jv.H
    normal = (sp.eye(j.rows)-proj)*jpv
    ng = normal.H*normal
    return dict(j=jv, jp=jpv, w=w, b=b, wp=wp, gamma=gamma,
                proj=proj, normal=normal, ng=ng)


def pair(p, m, vv):
    xx = vv**2
    mat = block(E, I*vv*E, E, -I*vv*E)
    mp = block(O, I/(2*vv)*E, O, -I/(2*vv)*E)
    mi = mat.inv()
    d = sp.diag(p["w"], m["w"])/(2*vv)
    dp = sp.diag(p["wp"]/(2*vv), -m["wp"]/(2*vv))/(2*vv)-d/(2*xx)
    gb = sp.diag(p["gamma"]/(2*vv), -m["gamma"]/(2*vv))
    h = mat.H*d*mat
    hp = mp.H*d*mat+mat.H*dp*mat+mat.H*d*mp
    a = mi*gb*mat+mi*mp
    qn = mat.H*sp.diag(p["ng"], m["ng"])*mat/(2*vv)
    k = sp.diag(2*vv*E, -2*vv*E)
    jj = block(O, 2*I*xx*E, -2*I*E, O)
    return dict(mat=mat, mp=mp, mi=mi, h=h, hp=hp, a=a, qn=qn,
                jj=jj, k=k, gb=gb, d=d)


def polynomial_pair(f, center):
    a, b = [], []
    for ff in f:
        terms = sp.Poly(ff, s)
        aa = sum(cc*sp.binomial(n, 2*j)*center**(n-2*j)*(-x)**j
                 for (n,), cc in terms.terms() for j in range(n//2+1))
        bb = sum(cc*sp.binomial(n, 2*j+1)*center**(n-2*j-1)*(-x)**j
                 for (n,), cc in terms.terms() for j in range((n-1)//2+1))
        a.append(sp.expand(aa))
        b.append(sp.expand(bb))
    return sp.Matrix(a+b)


def check_frame(even):
    label = "even" if even else "non_even"
    j = frame(even)
    w = j.H*j
    b = j.H*j.diff(u)
    eq(label+"/fixed_phase_B", b, w.diff(u)/2)
    reject(label+"/noncommuting_weights", w.subs(u, 0)*w.subs(u, 2),
           w.subs(u, 2)*w.subs(u, 0))
    if even:
        eq(label+"/frame_parity", j.subs(u, -u), j)
    else:
        reject(label+"/weight_not_even", w.subs(u, -u), w)
    centers = [sp.Rational(1, 2), sp.Rational(3, 2), sp.Integer(2)]
    f = sp.Matrix([2+(1+I)*s-3*s**2+s**4, 1-I+2*s**2-I*s**3+s**5])
    for center in centers:
        q = polynomial_pair(f, center)
        c = f.subs(s, center+I*u)
        rebuilt = q[:2, :].subs(x, -(s-center)**2)+(s-center)*q[2:, :].subs(x, -(s-center)**2)
        eq(f"{label}/center_{center}/polynomial_inverse", rebuilt, f)
        eq(f"{label}/center_{center}/degree_bounds", sp.Matrix([sp.degree(z, x) for z in q]),
           sp.Matrix([2, 2, 1, 2]))
        for vv in [sp.Rational(1, 3), sp.Rational(1, 2), sp.Integer(1), sp.Rational(3, 2), sp.Integer(2)]:
            name = f"{label}/center_{center}/v_{vv}"
            p, m = jet(j, vv), jet(j, -vv)
            z = pair(p, m, vv)
            mat, mi, h, a, jj = (z[k] for k in ["mat", "mi", "h", "a", "jj"])
            qq, qp = q.subs(x, vv**2), q.diff(x).subs(x, vv**2)
            cp, cm = c.subs(u, vv), c.subs(u, -vv)
            cpp, cmp = c.diff(u).subs(u, vv), c.diff(u).subs(u, -vv)
            nabla = qp+a*qq
            eq(name+"/branch_inverse", mat*qq, cp.col_join(cm))
            eq(name+"/signed_chain_rule", z["k"]*(z["mp"]*qq+mat*qp), cpp.col_join(cmp))
            eq(name+"/original_density", (cp.H*p["w"]*cp+cm.H*m["w"]*cm)[0]/(2*vv), (qq.H*h*qq)[0])
            eq(name+"/M_inverse_derivative", mi*z["mp"], sp.diag(O, E/(2*vv**2)))
            eq(name+"/J_from_signed_branches", mi*z["k"]*mat, jj)
            eq(name+"/J_squared", jj*jj, 4*vv**2*sp.eye(4))
            eq(name+"/J_metric", jj.H*h*jj, 4*vv**2*h)
            eq(name+"/density_drift", a.H*h+h*a, z["hp"]+h/(2*vv**2))
            eq(name+"/density_compatible_connection", (a-sp.eye(4)/(4*vv**2)).H*h+h*(a-sp.eye(4)/(4*vv**2)), z["hp"])
            eq(name+"/full_covariant_derivative", mi*(cpp+p["gamma"]*cp).col_join(cmp+m["gamma"]*cm), jj*nabla)
            original_p = p["jp"]*cp+p["j"]*cpp
            original_m = m["jp"]*cm+m["j"]*cmp
            direct_energy = (original_p.H*original_p+original_m.H*original_m)[0]/(2*vv)
            pair_energy = (4*vv**2*nabla.H*h*nabla+qq.H*z["qn"]*qq)[0]
            eq(name+"/direct_original_energy", direct_energy, pair_energy)
            eq(name+"/normal_congruence", (qq.H*z["qn"]*qq)[0],
               (cp.H*p["ng"]*cp+cm.H*m["ng"]*cm)[0]/(2*vv))
            smat = center*sp.eye(4)+block(O, -vv**2*E, E, O)
            sprime = block(O, -E, O, O)
            eq(name+"/spectral_multiplication", mi*sp.diag((center+I*vv)*E, (center-I*vv)*E)*mat, smat)
            eq(name+"/commutator_derivative_coefficient", jj*smat, smat*jj)
            eq(name+"/commutator_constant", jj*sprime+jj*a*smat-smat*jj*a, I*sp.eye(4))
            for branch, ob in [("positive", p), ("negative", m)]:
                eq(name+"/"+branch+"/normal_orthogonal", ob["j"].H*ob["normal"], sp.zeros(2))
                eq(name+"/"+branch+"/normal_Gram", ob["ng"],
                   ob["jp"].H*ob["jp"]-ob["b"].H*ob["w"].inv()*ob["b"])
                record(name+"/"+branch+"/positive_weight", ob["w"][0, 0]>0 and ob["w"].det()>0)
                record(name+"/"+branch+"/positive_normal", ob["ng"][0, 0]>0 and ob["ng"].det()>0)
            if even:
                ll, ln = p["w"]/vv, p["ng"]/vv
                gx = p["gamma"]/(2*vv)
                eq(name+"/even_pair_density", h, sp.diag(ll, vv**2*ll))
                eq(name+"/even_normal_density", z["qn"], sp.diag(ln, vv**2*ln))
                eq(name+"/even_pair_connection", a, sp.diag(gx, gx+E/(2*vv**2)))
                aa, bb = qq[:2, :], qq[2:, :]
                ad, bd = qp[:2, :], qp[2:, :]
                ev = 4*vv**2*(ad+gx*aa).H*ll*(ad+gx*aa)
                ev += (bb+2*vv**2*(bd+gx*bb)).H*ll*(bb+2*vv**2*(bd+gx*bb))
                ev += aa.H*ln*aa+vv**2*bb.H*ln*bb
                eq(name+"/even_original_energy", direct_energy, ev[0])
            if center == centers[0] and vv == 1:
                reject(name+"/reject_missing_density_drift", a.H*h+h*a, z["hp"])
                badgb = sp.diag(p["gamma"]/(2*vv), m["gamma"]/(2*vv))
                bada = mi*badgb*mat+mi*z["mp"]
                reject(name+"/reject_unsigned_negative_branch", bada, a)
                reject(name+"/reject_normal_energy_omission", direct_energy,
                       (4*vv**2*nabla.H*h*nabla)[0])
                reject(name+"/reject_moving_basis_omission", a, mi*z["gb"]*mat)


def check_gauge():
    original = frame(False)
    c = sp.Matrix([[1, u+I], [0, 1]])
    changed = original*c
    for vv in [sp.Rational(-3, 2), sp.Integer(0), sp.Rational(2, 3), sp.Integer(2)]:
        a, b = jet(original, vv), jet(changed, vv)
        cv, cd = c.subs(u, vv), c.diff(u).subs(u, vv)
        pre = f"variable_complex_frame/u_{vv}"
        eq(pre+"/weight", b["w"], cv.H*a["w"]*cv)
        eq(pre+"/B", b["b"], cv.H*a["b"]*cv+cv.H*a["w"]*cd)
        eq(pre+"/connection", b["gamma"], cv.inv()*a["gamma"]*cv+cv.inv()*cd)
        eq(pre+"/normal", b["normal"], a["normal"]*cv)
        eq(pre+"/normal_Gram", b["ng"], cv.H*a["ng"]*cv)
        eq(pre+"/projection", b["proj"], a["proj"])
        reject(pre+"/reject_B_half_derivative_after_gauge", b["b"], b["wp"]/2)
        radius = abs(vv) if vv else sp.Rational(1, 2)
        p, m = jet(changed, radius), jet(changed, -radius)
        z = pair(p, m, radius)
        eq(pre+"/pair_full_gauge_drift", z["a"].H*z["h"]+z["h"]*z["a"],
           z["hp"]+z["h"]/(2*radius**2))


def gaussian_moment(poly, var, beta):
    total = 0
    for (n,), coefficient in sp.Poly(sp.expand(poly), var).terms():
        if n % 2 == 0:
            total += coefficient*sp.gamma(sp.Rational(n+1, 2))/beta**sp.Rational(n+1, 2)
    return sp.expand(total)


def check_scalar_original_amplitude():
    # Full amplitude a(t)=t exp(-t^2/2), with its unscaled total mass.
    mass = gaussian_moment(u**2, u, sp.Integer(1))
    fisher = 4*gaussian_moment((1-u**2)**2, u, sp.Integer(1))
    eq("Gaussian_polynomial/mass", mass, sp.sqrt(sp.pi)/2)
    eq("Gaussian_polynomial/fisher", fisher, 3*sp.sqrt(sp.pi))
    eq("Gaussian_polynomial/cross_integral", gaussian_moment(u*(1-u**2), u, sp.Integer(1)), 0)
    pp = u**2/4-y**2
    derivative_poly = sp.diff(pp, u)-u*pp/2
    m_poly = gaussian_moment(pp**2, y, sp.Integer(2))
    t_poly = gaussian_moment(derivative_poly**2, y, sp.Integer(2))
    cross_poly = gaussian_moment(pp*derivative_poly, y, sp.Integer(2))
    eq("Gaussian_polynomial/fibre_mass_polynomial", m_poly, sp.sqrt(sp.pi/2)*(u**4-2*u**2+3)/16)
    eq("Gaussian_polynomial/line_cross", cross_poly, (m_poly.diff(u)-u*m_poly)/2)
    total_derivative = gaussian_moment(t_poly, u, sp.Rational(1, 2))
    eq("Gaussian_polynomial/full_derivative_mass", total_derivative, mass*fisher/8)
    for uu in [sp.Rational(-2), sp.Rational(-1, 2), 0, sp.Rational(2, 3), 3]:
        mm, tt, bb = [expr.subs(u, uu) for expr in [m_poly, t_poly, cross_poly]]
        nn = sp.cancel(tt-bb**2/mm)
        eq(f"Gaussian_polynomial/u_{uu}/line_normal_identity", 4*tt, 4*bb**2/mm+4*nn)
        record(f"Gaussian_polynomial/u_{uu}/normal_sign", nn>0 if uu else nn==0)
    mfun = m_poly*sp.exp(-u**2/2)
    rho = mfun.subs(u, sp.sqrt(x))/sp.sqrt(x)
    eq("Gaussian_polynomial/radial_drift", (rho.diff(x)+rho/(2*x))*2*x,
       mfun.diff(u).subs(u, sp.sqrt(x)))
    eq("Gaussian_polynomial/radial_Fisher_density",
       4*x*(rho.diff(x)+rho/(2*x))**2/rho,
       (mfun.diff(u)**2/mfun).subs(u, sp.sqrt(x))/sp.sqrt(x))
    reject("Gaussian_polynomial/reject_unscaled_mass", total_derivative, fisher/8)
    reject("Gaussian_polynomial/reject_radial_drift_omission", rho.diff(x), rho.diff(x)+rho/(2*x))


def exponential_moment(poly):
    return sum(c*sp.factorial(n)/2**(n+1) for (n,), c in sp.Poly(sp.expand(poly), v).terms())


def check_joining_domain():
    j = frame(False)
    e = sp.Matrix([1, 0])
    # c(v)=exp(-v)e, c(-v)=2 exp(-v)e. Remove the common scalar
    # only while forming its explicitly recorded polynomial coefficient.
    plus, minus = j.subs(u, v)*e, 2*j.subs(u, -v)*e
    norm_poly = (plus.H*plus+minus.H*minus)[0]
    dp = (j.diff(u)-j).subs(u, v)*e
    dm = 2*(j.diff(u)+j).subs(u, -v)*e
    energy_poly = (dp.H*dp+dm.H*dm)[0]
    norm = exponential_moment(norm_poly)
    energy = exponential_moment(energy_poly)
    record("joining/open_branch_norm_finite", norm.is_Rational and norm>0, value=str(norm))
    record("joining/open_branch_energy_finite", energy.is_Rational and energy>0, value=str(energy))
    jump = (plus-minus).subs(v, 0)
    eq("joining/original_vector_jump", jump, -j.subs(u, 0)*e)
    reject("joining/reject_false_H1_membership", jump, sp.zeros(4, 1))
    q_coefficient = sp.Matrix([sp.Rational(3, 2), 0, I/(2*v), 0])
    # q(x)=exp(-sqrt(x))*q_coefficient(sqrt(x)); dx derivative:
    qp_coefficient = (q_coefficient.diff(v)-q_coefficient)/(2*v)
    for vv in [sp.Rational(1, 3), sp.Rational(1, 2), 1, 2]:
        p, m = jet(j, vv), jet(j, -vv)
        z = pair(p, m, vv)
        qq, qd = q_coefficient.subs(v, vv), qp_coefficient.subs(v, vv)
        eq(f"joining/v_{vv}/both_branches", z["mat"]*qq, e.col_join(2*e))
        nn = qd+z["a"]*qq
        eq(f"joining/v_{vv}/finite_open_energy_density",
           (4*vv**2*nn.H*z["h"]*nn+qq.H*z["qn"]*qq)[0],
           energy_poly.subs(v, vv)/(2*vv))
        eq(f"joining/v_{vv}/finite_open_norm_density", (qq.H*z["h"]*qq)[0], norm_poly.subs(v, vv)/(2*vv))
    eq("joining/right_trace", sp.limit(q_coefficient[:2, :]+I*v*q_coefficient[2:, :], v, 0, dir="+"), e)
    eq("joining/left_trace", sp.limit(q_coefficient[:2, :]-I*v*q_coefficient[2:, :], v, 0, dir="+"), 2*e)
    # Integration by parts contributes (right-left)*test(0). This
    # nonzero delta coefficient cannot be represented by an L2 function.
    eq("joining/distribution_delta_coefficient", jump, sp.Matrix([-1, 0, -1, -1]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--inject-failure", action="store_true")
    args = parser.parse_args()
    error = None
    try:
        check_frame(False)
        check_frame(True)
        check_gauge()
        check_scalar_original_amplitude()
        check_joining_domain()
        if args.inject_failure:
            eq("deliberate_failure/missing_signed_branch", -sp.Rational(1, 2), sp.Rational(1, 2))
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
    receipt = dict(
        schema="split-zero-sum-connection-stieltjes-calibration-v1",
        generated_utc=datetime.now(timezone.utc).isoformat(),
        script="scripts/check_sum_connection_stieltjes.py",
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        python_version=sys.version.split()[0], sympy_version=sp.__version__,
        optimized=bool(sys.flags.optimize), injected_failure=args.inject_failure,
        passed=error is None, error=error, count=len(RECORDS),
        exact_count=sum(r["kind"]=="exact" for r in RECORDS),
        negative_control_count=sum(r["kind"]=="negative_control" for r in RECORDS),
        scope="Exact specified finite polynomial frames and unscaled Gaussian-polynomial amplitude; no arithmetic theta asymptotic or RH claim.",
        records=RECORDS,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: receipt[k] for k in ["passed", "count", "exact_count", "negative_control_count", "error"]}))
    return 0 if error is None else 1


if __name__ == "__main__":
    raise SystemExit(main())
