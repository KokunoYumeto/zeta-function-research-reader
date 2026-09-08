"""Independent exact audit of FABEL_TENSOR_TRANSFER (102), (104), (105).

All derived matrices begin at the unchanged three original polynomials F.
The local source snapshot is byte-bound; --observe-source additionally checks
the original file without making the standalone replay depend on that file.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source" / "FABEL_TENSOR_TRANSFER.md"
ORIGINAL = Path("[local]/Documents/math/agent_work/ym_quantum_coarse_graining_astra_20260908/FABEL_TENSOR_TRANSFER.md")
SOURCE_SHA = "c0bdfe683d3f620858a74654406e30c02b3242d0b6cfb012432cac173d98d9fc"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--observe-source", action="store_true")
    args = parser.parse_args()
    assert sha(SOURCE) == SOURCE_SHA, "source snapshot changed"
    if args.observe_source:
        assert sha(ORIGINAL) == SOURCE_SHA, "original source changed"

    x, y, w = s.symbols("x y w", real=True)
    z = s.symbols("z", positive=True)
    R = s.Rational
    I = s.eye(3)
    zero_checks = []

    def scalar(label, expr):
        result = s.cancel(s.expand(expr))
        assert result == 0, (label, result)
        zero_checks.append(label)

    def matrix(label, actual, expected):
        assert actual.shape == expected.shape
        for i in range(actual.rows):
            for j in range(actual.cols):
                scalar(f"{label}[{i+1},{j+1}]", actual[i, j] - expected[i, j])

    F = s.Matrix([
        (1+x*y)**3*w+y**2*(1+x*y)*(4+3*x*y),
        y+3*x*(1+x*y)**2*w+3*x*y**2*(4+3*x*y),
        2*x-3*x**2*y-x**3*w,
    ])
    J = F.jacobian([x, y, w])
    scalar("original det DF=-2", J.det()+2)
    q0 = {x: 1, y: R(-3,2), w: R(13,2)}
    gamma = {x: 1/z, y: -3*z/2, w: 13*z**2/2}
    J0 = J.subs(q0)
    Jg = J.subs(gamma)
    J0_displayed = s.Matrix([
        [R(-9,16), R(-3,8), R(-1,8)],
        [R(3,8), R(25,4), R(3,4)],
        [R(-17,2), -3, -1],
    ])
    Jg_displayed = s.Matrix([
        [-9*z**3/16, -3*z/8, R(-1,8)],
        [3*z**2/8, R(25,4), 3/(4*z)],
        [R(-17,2), -3/z**2, -1/z**3],
    ])
    matrix("J0=DF(q0)", J0, J0_displayed)
    matrix("Jgamma=DF(gamma)", Jg, Jg_displayed)
    scalar("det J0=-2", J0.det()+2)
    scalar("det Jgamma=-2", Jg.det()+2)

    tau = (1-z**2)/8
    E23 = s.zeros(3)
    E23[1, 2] = 1
    B = I+6*tau*E23
    Bi = I-6*tau*E23
    matrix("B inverse left", Bi*B, I)
    matrix("B inverse right", B*Bi, I)
    scalar("det B=1", B.det()-1)

    C = (J0.inv()*Bi*Jg).applyfunc(s.cancel)
    C_displayed = s.Matrix([
        [(17-9*z**3)/8, (3-3*z**3)/(4*z**2), (1-z**3)/(4*z**3)],
        [(51-24*z**2-27*z**3)/16, (9+8*z**2-9*z**3)/(8*z**2), (3-3*z**3)/(8*z**3)],
        [(-153+36*z**2+117*z**3)/8, (-27-12*z**2+39*z**3)/(4*z**2), (-9+13*z**3)/(4*z**3)],
    ])
    matrix("all entries of (102)", C, C_displayed)
    A = (Jg.inv()*B*J0).applyfunc(s.cancel)
    matrix("A C=I", A*C, I)
    matrix("C A=I", C*A, I)
    scalar("det C=1", C.det()-1)
    scalar("det A=1", A.det()-1)
    matrix("C at original time", C.subs(z, 1), I)
    matrix("A at original time", A.subs(z, 1), I)

    # M keeps all nine exact entries at a common denominator; no term is dropped.
    M = (16*z**3*C).applyfunc(s.expand)
    assert all(v.is_polynomial(z) for v in M)
    assert all(c.is_Integer for v in M for c in s.Poly(v, z).all_coeffs())
    K = (C*C.T).applyfunc(s.cancel)
    K_numerator = (M*M.T).applyfunc(s.expand)
    matrix("all entries K=C C^T", K, K_numerator/(256*z**6))
    matrix("K symmetric", K, K.T)
    scalar("det K=1", K.det()-1)
    matrix("K at original time", K.subs(z, 1), I)

    eta = s.Matrix([R(1,4), R(3,8), R(-9,4)])
    e3 = s.Matrix([0, 0, 1])
    C_endpoint = C.applyfunc(lambda v: s.limit(z**3*v, z, 0, dir="+"))
    matrix("all entries lim z^3 C", C_endpoint, eta*e3.T)
    Sstar = eta*eta.T
    Sstar_displayed = s.Matrix([[4, 6, -36], [6, 9, -54], [-36, -54, 324]])/64
    matrix("Sstar exact", Sstar, Sstar_displayed)
    K_endpoint = K.applyfunc(lambda v: s.limit(z**6*v, z, 0, dir="+"))
    matrix("all entries lim z^6 K", K_endpoint, Sstar)

    zeta = C.T*e3
    Q = (zeta.T*zeta)[0]
    Q_displayed = ((-153+36*z**2+117*z**3)**2/64
        +(-27-12*z**2+39*z**3)**2/(16*z**4)
        +(-9+13*z**3)**2/(16*z**6))
    scalar("unmodified Q full row", Q-Q_displayed)
    scalar("Q=K33", Q-K[2, 2])
    scalar("lim z^6 Q=81/16", s.limit(z**6*Q, z, 0, dir="+")-R(81,16))

    def weights(S):
        trace = s.trace(S)
        return [trace**2/9,
                sum((S[i,i]-trace/3)**2 for i in range(3))/2,
                sum(S[i,j]**2 for i in range(3) for j in range(i+1,3))]

    ss = s.symbols("S11 S22 S33 S12 S13 S23", real=True)
    S = s.Matrix([[ss[0],ss[3],ss[4]], [ss[3],ss[1],ss[5]], [ss[4],ss[5],ss[2]]])
    d, h, o = s.symbols("d h o", real=True)
    gram_value = d*sum(v**2 for v in ss[:3])+2*h*(ss[0]*ss[1]+ss[0]*ss[2]+ss[1]*ss[2])+o*sum(v**2 for v in ss[3:])
    symbolic_weights = weights(S)
    formula104 = symbolic_weights[0]*(3*d+6*h)+symbolic_weights[1]*(2*d-2*h)+symbolic_weights[2]*o
    scalar("full arbitrary cubic Gram polynomial (104)", gram_value-formula104)
    scale = s.symbols("scale", real=True)
    for j,(left,right) in enumerate(zip(weights(scale*S), symbolic_weights)):
        scalar(f"weight {j} degree two", left-scale**2*right)
    expected = [R(113569,36864), R(100825,12288), R(531,512)]
    endpoint_weights = weights(Sstar)
    actual_weights = [s.cancel(v) for v in weights(K)]
    scaled_weight_numerators = [s.cancel(z**12*v) for v in actual_weights]
    for j,(value,wanted) in enumerate(zip(endpoint_weights,expected)):
        scalar(f"endpoint constant (105) channel {j}",value-wanted)
        scalar(f"full z-weight endpoint channel {j}",s.limit(z**12*actual_weights[j],z,0,dir="+")-wanted)
        assert wanted > 0

    def entries(S):
        return [[str(v) for v in list(S.row(i))] for i in range(S.rows)]

    result = {
        "status":"pass",
        "source_sha256":SOURCE_SHA,
        "source_snapshot":str(SOURCE.relative_to(ROOT)).replace("\\","/"),
        "original_source_observed":args.observe_source,
        "checker_sha256":sha(Path(__file__)),
        "sympy_version":s.__version__,
        "exact_scalar_zero_checks":len(zero_checks),
        "checks":zero_checks,
        "domain":"x,y,w real; z>0; tau=(1-z^2)/8; original material endpoint z down to 0",
        "F_original":entries(F),
        "DF_original":entries(J),
        "J0":entries(J0),
        "Jgamma":entries(Jg),
        "B":entries(B),
        "C":entries(C),
        "A_inverse":entries(A),
        "M_16z3C":entries(M),
        "K_denominator":"256*z**6",
        "K_numerator":entries(K_numerator),
        "Sstar":entries(Sstar),
        "weights_K":list(map(str,actual_weights)),
        "z12_weights_K":list(map(str,scaled_weight_numerators)),
        "endpoint_weights":list(map(str,endpoint_weights)),
        "findings":[],
        "scope":"Exact coefficients and finite-regulator measure decomposition only; no infinite-volume or gap conclusion.",
    }
    (ROOT/"verification.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("status","source_sha256","exact_scalar_zero_checks","endpoint_weights","original_source_observed")}))


if __name__ == "__main__":
    main()
