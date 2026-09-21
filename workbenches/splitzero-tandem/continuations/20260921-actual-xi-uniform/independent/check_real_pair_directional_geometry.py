"""Exact algebra and certified original-coordinate directional geometry.

This does not repeat the root search. It reads the full-series certificate,
checks its script identity and enclosing derivative inequalities, and uses
those enclosures for the exact derivative morphism proved in RPD3--4.
Finite symbolic checks support, rather than replace, the all-degree proof.
"""
from pathlib import Path
import hashlib
import json
import math
import platform

import sympy as S
import flint
from flint import arb, acb

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
checks = []


def check(name, expression):
    values = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
    for value in values:
        assert S.cancel(S.expand(value)) == 0, (name, value)
    checks.append({"name": name, "scalar_entries": len(values)})


azr, azi, axr, axi, qr, qi = S.symbols("azr azi axr axi qr qi", real=True)
JG = S.Matrix([[azr, axr], [azi, axi]])
det = azr*axi-azi*axr
inverse_q = S.Matrix([axi*qr-axr*qi, azr*qi-azi*qr])/det
check("exact original-coordinate inverse signs", JG*inverse_q-S.Matrix([qr, qi]))
Q = JG.T*JG
check("quadratic determinant retains real Jacobian", Q.det()-det**2)
br, bi, jr, ji, kr, ki = S.symbols("br bi jr ji kr ki", real=True)
multiply_b = S.Matrix([[br, -bi], [bi, br]])
check("factor product Jacobian determinant",
      (multiply_b*S.Matrix([[jr, kr], [ji, ki]])).det()
      -(br**2+bi**2)*(jr*ki-ji*kr))

# All complex conjugates below are independent formal variables. The check
# is a polynomial identity and hence remains valid for their actual values.
t, tau, xi = S.symbols("t tau xi")
A, Ab, B, Bb, C, Cb, H, Hb, F, Fb = S.symbols("A Ab B Bb C Cb H Hb F Fb")
G = A*tau+B*xi+C*tau**2/2+H*tau*xi+F*xi**2/2
Gb = Ab*tau+Bb*xi+Cb*tau**2/2+Hb*tau*xi+Fb*xi**2/2
E = S.expand(G*Gb)
mu = [S.expand(S.diff(E, xi, n).subs(xi, 0)) for n in range(4)]
coeff = [mu[0], -S.I*(mu[1]-4*mu[0]),
         -mu[2]/2+4*mu[1]-8*mu[0],
         S.I*(mu[3]/6-2*mu[2]+S.Rational(25, 3)*mu[1]-12*mu[0])]
coeff = [S.expand(value) for value in coeff]
u0, u1, u2, u3 = S.symbols("mu0 mu1 mu2 mu3")
omega = -S.I*t+S.I*t**3/3
exp_center = 1-4*omega+8*omega**2-S.Rational(32, 3)*omega**3
symbol_direct = S.expand(exp_center*(u0+u1*omega+u2*omega**2/2+u3*omega**3/6))
for n, expected in enumerate([u0, -S.I*(u1-4*u0),
        -u2/2+4*u1-8*u0,
        S.I*(u3/6-2*u2+S.Rational(25, 3)*u1-12*u0)]):
    check(f"original arctangent and exponential coefficient {n}",
          symbol_direct.coeff(t, n)-expected)
c_actual, R_actual, b_actual = A*Ab, A*Bb+B*Ab, B*Bb
actual = [c_actual, -S.I*R_actual, -b_actual,
          (C*Ab+Cb*A)/2,
          -S.I*((B*Cb+Bb*C)/2+H*Ab+Hb*A-4*c_actual),
          -(F*Ab+Fb*A)/2-H*Bb-Hb*B+4*R_actual,
          S.I*((F*Bb+Fb*B)/2-4*b_actual)]
for name, got, expected in [
        ("g0 quadratic", coeff[0].coeff(tau, 2), actual[0]),
        ("g1 linear", coeff[1].coeff(tau, 1), actual[1]),
        ("g2 constant", coeff[2].coeff(tau, 0), actual[2]),
        ("g0 cubic", coeff[0].coeff(tau, 3), actual[3]),
        ("g1 quadratic", coeff[1].coeff(tau, 2), actual[4]),
        ("g2 linear", coeff[2].coeff(tau, 1), actual[5]),
        ("g3 constant", coeff[3].coeff(tau, 0), actual[6])]:
    check("full original center correction "+name, S.expand(got)-expected)

c, d, e, c3, d2, e1, f, ell = S.symbols("c d e c3 d2 e1 f ell", nonzero=True)
dc, dd = S.symbols("dc dd")
lam, theta, R, b = S.symbols("lambda theta R b")


def hh(n):
    if n < 0:
        return S.Integer(0)
    return S.Add(*[(-1)**(n-j)*S.binomial(n-j, j)*d**(n-2*j)*e**j/c**(n-j+1)
                  for j in range(n//2+1)])


def square_h(n):
    return sum((hh(j)*hh(n-j) for j in range(n+1)), S.Integer(0)) if n >= 0 else S.Integer(0)


def kk(n):
    return -sum(a*square_h(n-j) for j, a in enumerate([c3, d2, e1, f]))


scale = {c: ell**2*c, d: ell*d, c3: ell**3*c3,
         d2: ell**2*d2, e1: ell*e1}
for n in range(9):
    check(f"all-direction reciprocal coefficient {n}",
          c*hh(n)+d*hh(n-1)+e*hh(n-2)-int(n == 0))
    check(f"actual derivative Chebyshev coefficient {n}",
          hh(n).subs({d: -2*S.I*c*lam*theta, e: -c*lam**2})
          -(S.I*lam)**n*S.chebyshevu(n, theta)/c)
    check(f"signed scaling of leading coefficient {n}",
          hh(n).subs(scale, simultaneous=True)-ell**(-n-2)*hh(n))
    check(f"signed scaling of full correction {n}",
          kk(n).subs(scale, simultaneous=True)-ell**(-n-1)*kk(n))
    check(f"curvature correction identity {n}",
          kk(n).subs({c3: c3+dc/2, d2: d2+dd/2}, simultaneous=True)-kk(n)
          -(dc*S.diff(hh(n), c)+dd*S.diff(hh(n), d))/2)

h3 = S.I*R*(2*c*b-R**2)/c**4
check("degree-three leading term", hh(3).subs({d: -S.I*R, e: -b})-h3)
dcv, drv = S.symbols("Dc DR")
derivative = dcv*S.diff(h3, c)+drv*S.diff(h3, R)
root_derivative = S.I*((2*c*b-3*R**2)*drv+2*b*R*dcv)/c**4
check("degree-three derivative remainder equals root multiple",
      derivative-root_derivative+4*dcv*h3/c)
k3root = (2*c*d*e1+2*c3*d*e+(2*c*e-3*d*d)*d2-c*c*f)/c**4
check("degree-three next coefficient remainder equals root multiple",
      kk(3)-k3root+4*c3*hh(3)/c)
for theta0, sin0, expected in [
        (S.sqrt(2)/2, S.sqrt(2)/2, 4*S.sqrt(2)*S.I/b),
        (S.Integer(0), S.Integer(1), -4*S.I/b),
        (-S.sqrt(2)/2, S.sqrt(2)/2, 4*S.sqrt(2)*S.I/b)]:
    check("exact degree-three angular transverse derivative "+str(theta0),
          root_derivative.subs({c: b, R: 2*b*theta0, dcv: 0, drv: -2*b*sin0})-expected)

# Direct finite matrix computation retains each independent Gamma weight.
# B^{-1}'s coefficients are reconstructed by multiplication, not by a
# fitted pole order. Leading corner positions and rank-two products are
# checked at the exactly resonant derivative values theta=0 (odd D).
for D in [1, 3, 5, 7]:
    rho = S.symbols(f"rho0:{D+1}", positive=True)
    L = hh(D-1).subs(d, 0)
    corner_det = L**2*rho[D-1]*rho[D]/rho[0]/rho[1]
    expected_det = e**(D-1)/c**(D+1)*rho[D-1]*rho[D]/rho[0]/rho[1]
    check(f"full weighted resonant corner determinant D{D}", corner_det-expected_det)
    check(f"resonant diagonal nonzero polynomial D{D}",
          L**2-e**(D-1)/c**(D+1))

# Rational-angle overlap counts are exact rational sets, not floats.
overlap_checks = []
for D in range(1, 21):
    first = {S.Rational(k, D+1) for k in range(1, D+1)}
    for Ecut in range(1, 21):
        second = {S.Rational(k, Ecut+1) for k in range(1, Ecut+1)}
        assert len(first & second) == math.gcd(D+1, Ecut+1)-1
        overlap_checks.append([D, Ecut, len(first & second)])

# Bounds are read as outward balls. Their short printed decimals are never
# treated as exact root coordinates or exact derivatives.
flint.ctx.prec = 256
flint.ctx.threads = 1
cert_path = ROOT / "REAL_PAIR_CERTIFICATE.json"
cert = json.loads(cert_path.read_text(encoding="utf-8"))
assert cert["status"] == "CERTIFIED" and all(cert["checks"].values())
script_hash = hashlib.sha256((ROOT/"certify_real_pair.py").read_bytes()).hexdigest()
assert script_hash == cert["script_sha256"]
assert all(arb(row) < 1 for row in cert["weighted_contraction_rows"])


def complex_ball(text):
    if " + " in text and text.endswith("j"):
        re, im = text[:-1].split(" + ")
        return acb(arb(re), arb(im))
    return acb(arb(text))


f1 = {key: complex_ball(value) for key, value in cert["full_factor_enclosures"][0].items()}
f2 = {key: complex_ball(value) for key, value in cert["full_factor_enclosures"][1].items()}
Az, Ax, Bxi = f2["d"]*f1["dz"], f2["d"]*f1["dx"], f2["d"]*f1["f_xi"]
Delta = (Az.conjugate()*Ax).imag
det_j = (f1["dz"].conjugate()*f1["dx"]).imag
assert det_j < 0 and Delta < 0
absB2 = Bxi.real**2+Bxi.imag**2
assert absB2 > 0
q00, q01, q11 = Az.real**2+Az.imag**2, (Az*Ax.conjugate()).real, Ax.real**2+Ax.imag**2
assert q00*q11-q01**2 > 0
eval_plus = (q00+q11+((q00-q11)**2+4*q01**2).sqrt())/2
# Quotient avoids dependency cancellation in the tiny lower eigenvalue.
eval_minus = Delta**2/eval_plus
assert eval_minus > 0


def inverse_L(q):
    return ((Ax*q.conjugate()).imag/Delta, (Az.conjugate()*q).imag/Delta)


def prod1(key, vx):
    return f1[key[0]]*vx[0]+f1[key[1]]*vx[1]


jets1 = [complex_ball(value) for value in cert["all_original_factor_jets"][0]]
jets2 = [complex_ball(value) for value in cert["all_original_factor_jets"][1]]
Fxi = f2["d"]*jets1[2]+2*f1["f_xi"]*f2["f_xi"]
ray_rows = []
half_sqrt2 = arb(2).sqrt()/2
for k, cosine, sine in [(1, half_sqrt2, half_sqrt2), (2, arb(0), arb(1)),
                         (3, -half_sqrt2, half_sqrt2)]:
    for sign in [1, -1]:
        phase = acb(cosine, sign*sine)
        Av = Bxi*phase
        vector = inverse_L(Av)
        transverse = inverse_L(acb(0, 1)*Av)
        # The following products enclose the exact root-defined vectors.
        f1v = f1["dz"]*vector[0]+f1["dx"]*vector[1]
        f2v = f2["dz"]*vector[0]+f2["dx"]*vector[1]
        f1vv = f1["dzz"]*vector[0]**2+2*f1["dzx"]*vector[0]*vector[1]+f1["dxx"]*vector[1]**2
        Cv = f2["d"]*f1vv+2*f1v*f2v
        Hv = f2["d"]*(f1["f_xi_z"]*vector[0]+f1["f_xi_x"]*vector[1])
        Hv += f1v*f2["f_xi"]+f1["f_xi"]*f2v
        cb = absB2  # Exact identity |Av|^2=|B|^2 for this displayed representative.
        Rb = 2*absB2*cosine
        db, eb = acb(0, -Rb), -absB2
        c3b = (Cv*Av.conjugate()).real
        d2b = acb(0, -((Bxi*Cv.conjugate()).real+2*(Hv*Av.conjugate()).real-4*cb))
        e1b = -(Fxi*Av.conjugate()).real-2*(Hv*Bxi.conjugate()).real+4*Rb
        fb = acb(0, (Fxi*Bxi.conjugate()).real-4*absB2)
        K3b = (2*cb*db*e1b+2*c3b*db*eb+(2*cb*eb-3*db**2)*d2b-cb**2*fb)/cb**4
        H2b = (db**2-cb*eb)/cb**3
        derivative_b = acb(0, -4*sign*sine*(1-6*cosine**2)/absB2)
        assert H2b.abs_lower() > 0 and derivative_b.abs_lower() > 0
        det_vectors = vector[0]*transverse[1]-vector[1]*transverse[0]
        assert det_vectors.abs_lower() > 0
        ray_rows.append({
            "D": 3, "k": k, "epsilon": sign,
            "exact_definition": "Lambda^{-1}(B exp(i epsilon k pi/4)); r=1",
            "v_z": vector[0].str(40), "v_x": vector[1].str(40),
            "angular_transverse_z": transverse[0].str(40),
            "angular_transverse_x": transverse[1].str(40),
            "H2": H2b.str(40), "full_K3": K3b.str(40),
            "angular_DH3": derivative_b.str(40),
            "direction_transverse_determinant": det_vectors.str(40)})

source_names = ["REAL_PAIR_DIRECTIONAL_GEOMETRY.tex", "REAL_PAIR_COLLISION.tex",
                "REAL_PAIR_ALL_CUTOFFS.tex"]
out = {
    "status": "PASS",
    "scope": "Exact directional and curvature identities; original full-series certificate propagation; six original D3 resonance rays. All-cutoff and path-limit statements are proved in RPD1--30, not inferred from finite symbolic checks.",
    "symbolic_groups": len(checks),
    "symbolic_scalar_entries": sum(row["scalar_entries"] for row in checks),
    "checks": checks,
    "exact_rational_overlap_checks": len(overlap_checks),
    "overlap_receipts": overlap_checks,
    "interval_precision_bits": flint.ctx.prec,
    "original_derivative_enclosures": {"G_z": Az.str(40), "G_x": Ax.str(40),
        "G_xi": Bxi.str(40), "det_real_d1_Jacobian": det_j.str(40),
        "det_Lambda": Delta.str(40), "abs_B_squared": absB2.str(40),
        "Q00": q00.str(40), "Q01": q01.str(40), "Q11": q11.str(40),
        "lambda_min_Q": eval_minus.str(40), "lambda_max_Q": eval_plus.str(40)},
    "D3_resonance_rays": ray_rows,
    "source_sha256": {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                      for name in source_names},
    "root_certificate_sha256": hashlib.sha256(cert_path.read_bytes()).hexdigest(),
    "root_certificate_script_sha256": script_hash,
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "versions": {"python": platform.python_version(), "sympy": S.__version__,
                 "python_flint": flint.__version__},
    "arithmetic_provenance": "Fredrik Johansson, Arb, arXiv:1611.02831v1; interval source retained and read by the RPZ root calculation. This checker uses its certified output and does not claim a new reading of that paper."}
output_path = HERE / "REAL_PAIR_DIRECTIONAL_GEOMETRY_CHECK.json"
output_path.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
source_use = []
for source_id, relative, coverage, receiving in [
        ("programme:PCLOriginal", "source_dependencies/PCL_COMPLETE.tex", "PCL1--11, full text and proof", "RPD1 original complete family"),
        ("programme:WCF", "source_dependencies/WEIGHTED_CONDUCTOR_FORWARD.tex", "WCF1--6, full text and proof", "RPD11--12a original metric and both domains"),
        ("programme:RPZ", "REAL_PAIR_ZERO_BODY.tex", "RPZ1--19, full text and proof", "RPD3--7 actual root and invertible derivative"),
        ("programme:RPCJ", "independent/REAL_PAIR_COLLISION.tex", "RPCJ1--23, full text and proof", "RPD8--19 full directional jets and inverse constants"),
        ("programme:RPAC", "independent/REAL_PAIR_ALL_CUTOFFS.tex", "RPAC1--15, full text and proof", "RPD13--28 all-cutoff resonance and transition"),
        ("programme:RPZ-certificate", "certify_real_pair.py", "Complete executable, including full tails, Jacobian, root-specific factor substitution and output", "RPD3--4 actual Jacobian; checker interval propagation"),
        ("programme:real-pair-corpus-route", "REAL_PAIR_TOPIC_ROUTE.json", "Topic, queries, and existing source route; no search hit treated as reading", "Same-topic continuation; no new literature theorem imported")]:
    source_use.append({"source_id": source_id, "file": relative,
        "sha256": hashlib.sha256((ROOT/relative).read_bytes()).hexdigest(),
        "coverage": coverage, "receiving_calculation": receiving,
        "authorship": "Programme derivation; the complete upstream source and its existing attribution are retained."})
source_use.append({"source_id": "arXiv:1611.02831v1", "authors": ["Fredrik Johansson"],
    "file": "literature/1611.02831v1/arb.tex",
    "sha256": "1a74f00b81c59af5ba48454a89d2939528c60d37e1c79543367bb699779a6876",
    "coverage": "No fresh reading in this directional derivation. Original author TeX reading and arithmetic use are recorded by the RPZ root calculation; this calculation consumes its certified output.",
    "receiving_calculation": "Outward interval propagation of the complete saved certificate"})
(HERE/"REAL_PAIR_DIRECTIONAL_SOURCE_USE.json").write_text(json.dumps({
    "scope": "Actual reading coverage for RPD1--30 and RPD12a. Source identities are not claims of reading beyond the displayed coverage.",
    "sources": source_use}, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key: out[key] for key in ["status", "symbolic_groups", "symbolic_scalar_entries",
    "exact_rational_overlap_checks", "original_derivative_enclosures", "D3_resonance_rays"]}, indent=2))
