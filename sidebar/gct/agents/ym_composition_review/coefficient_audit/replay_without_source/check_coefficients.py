"""Independent exact audit of FABEL_TENSOR_TRANSFER (102), (104), (105).

All derived matrices begin at the unchanged three original polynomials F.
The compact equation transcript is byte-bound; --observe-source additionally
checks the original full hash and literal equation excerpts. Default replay
requires no original-source file or source directory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s
from audit_inputs import load_inputs, TRANSCRIPT, TRANSCRIPT_SHA, SOURCE_SHA

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--observe-source", action="store_true")
    parser.add_argument("--source-path", type=Path, help="Explicit original file for optional observation.")
    args = parser.parse_args()
    inputs = load_inputs(args.observe_source,args.source_path)
    equations = inputs["equations"]

    x, y, w = s.symbols("x y w", real=True)
    z = s.symbols("z", positive=True)
    R = s.Rational
    I = s.eye(3)
    zero_checks = []
    symbols = {"x":x, "y":y, "w":w, "z":z}

    def expression(text):
        return s.sympify(text, locals=symbols)

    def recorded_matrix(name):
        return s.Matrix([[expression(v) for v in row] for row in equations[name]])

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
    matrix("transcribed original F", F, s.Matrix(list(map(expression,equations["F"]))))
    J = F.jacobian([x, y, w])
    scalar("original det DF=-2", J.det()+2)
    q0 = {x: 1, y: R(-3,2), w: R(13,2)}
    gamma = {x: 1/z, y: -3*z/2, w: 13*z**2/2}
    for i,v in enumerate([x,y,w]):
        scalar(f"transcribed q0 coordinate {i}",q0[v]-expression(equations["q0"][i]))
        scalar(f"transcribed gamma coordinate {i}",gamma[v]-expression(equations["gamma"][i]))
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
    matrix("transcribed J0",J0_displayed,recorded_matrix("J0"))
    matrix("transcribed Jgamma",Jg_displayed,recorded_matrix("Jgamma"))
    scalar("det J0=-2", J0.det()+2)
    scalar("det Jgamma=-2", Jg.det()+2)

    tau = (1-z**2)/8
    scalar("transcribed parameter",tau-expression(equations["tau"]))
    assert equations["B_rule"] == "I+6*tau*E23"
    assert equations["C_rule"] == "J0.inv()*B.inv()*Jgamma"
    assert equations["A_rule"] == "Jgamma.inv()*B*J0"
    assert equations["K_rule"] == "C*C.T"
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
    matrix("transcribed C",C_displayed,recorded_matrix("C"))
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
    matrix("transcribed eta",eta,s.Matrix(list(map(expression,equations["eta"]))))
    e3 = s.Matrix([0, 0, 1])
    C_endpoint = C.applyfunc(lambda v: s.limit(z**3*v, z, 0, dir="+"))
    matrix("all entries lim z^3 C", C_endpoint, eta*e3.T)
    Sstar = eta*eta.T
    Sstar_displayed = s.Matrix([[4, 6, -36], [6, 9, -54], [-36, -54, 324]])/64
    matrix("Sstar exact", Sstar, Sstar_displayed)
    matrix("transcribed Sstar",Sstar_displayed,recorded_matrix("Sstar"))
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

    assert equations["weight_formulas"] == ["trace(S)**2/9", "sum((S[i,i]-trace(S)/3)**2 for i in range(3))/2", "sum(S[i,j]**2 for i in range(3) for j in range(i+1,3))"]
    assert equations["scales"] == {"C":3,"K":6,"spectral_measure":12}
    assert equations["domains"] == {"spatial_variables":["x","y","w"],"spatial_field":"real","parameter":"z>0","endpoint":"z down to 0","matrix_weights":"real symmetric 3 by 3","regulator":"fixed L>=2, a>0, g>0","spectral_sets":"Borel B subset (0,infinity)"}

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
    for j,wanted in enumerate(expected):
        scalar(f"transcribed endpoint weight {j}",wanted-expression(equations["endpoint_weights"][j]))
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
        "input_transcript":str(TRANSCRIPT.relative_to(ROOT)).replace("\\","/"),
        "transcript_sha256":TRANSCRIPT_SHA,
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
