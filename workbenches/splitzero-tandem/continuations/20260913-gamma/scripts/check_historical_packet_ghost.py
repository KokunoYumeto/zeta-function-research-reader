"""Exact finite calibrations of the complete-jet historical ghost formulas.

This does not certify arithmetic zero locations. Test packets are explicit
rational complex calibrations; the accompanying manuscript supplies proofs.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

checks = []


def require(label, condition):
    ok = bool(condition)
    checks.append({"label": label, "passed": ok})
    if not ok:
        raise RuntimeError(label)


def packet(roots, multiplicity):
    basis = [(rho, k) for rho in roots for k in range(multiplicity)]
    d = len(basis)
    zero = s.zeros(d)
    eye = s.eye(d)

    def matrix(action):
        result = s.zeros(d)
        for column, (rho, k) in enumerate(basis):
            target, factor = action(rho, k)
            if target is not None:
                result[basis.index(target), column] = factor
        return result

    C0 = matrix(lambda rho, k: ((s.conjugate(rho), k), 1))
    S0 = matrix(lambda rho, k: ((1-rho, k), 1))
    H = s.diag(*[(-1)**k for rho, k in basis])
    N = matrix(lambda rho, k: ((rho, k+1), 1) if k+1 < multiplicity else (None, 0))
    Ass = s.diag(*[rho for rho, k in basis])
    A = Ass+N
    B = s.diag(*[s.re(rho)-s.Rational(1, 2) for rho, k in basis])
    R = C0*S0
    Gamma = C0-S0
    Pminus = (eye-R)/2
    Pplus = (eye+R)/2
    label = f"roots={roots}; m={multiplicity}"
    require(label+": commuting involutions", C0*C0 == eye and S0*S0 == eye and C0*S0 == S0*C0)
    require(label+": gamma square", Gamma*Gamma == 4*Pminus)
    require(label+": all nilpotent jets", N**multiplicity == zero and N**(multiplicity-1) != zero)
    require(label+": natural reflection", H*S0*A*H*S0 == eye-A)
    require(label+": natural anti-linear conjugation", C0*s.conjugate(A) == A*C0)
    require(label+": parity retained", H*N == -N*H)
    require(label+": mixed block", Pplus*A*Pminus == B*Pminus)
    W = s.conjugate(A.T)+A-eye
    require(label+": displacement component", (W-R*W*R)/2 == 2*B)
    require(label+": nilpotent component", (W+R*W*R)/2 == N+s.conjugate(N.T))
    if B != zero:
        require(label+": no generator descent to half quotient", Pplus*A*Pminus != zero)
        require(label+": exact one-step saturation", Pminus.row_join(A*Pminus).rank() == d)
        require(label+": ghost half-rank", Pminus.rank()*2 == d)
        require(label+": full squared energy", s.trace(Gamma.T*Gamma) == 2*d)
    else:
        require(label+": supported cancellation on all jets", Gamma == zero and Pminus == zero)
        require(label+": generator quotient unchanged", Pminus.row_join(A*Pminus).rank() == 0)

    # Preserve original s coordinate by explicit Hermite-CRT matrix.
    x = s.Symbol('s')
    h = s.prod((x-rho)**multiplicity for rho in roots).expand()
    T = s.Matrix([[s.diff(x**j, x, k).subs(x, rho)/s.factorial(k)
                   for j in range(d)] for rho, k in basis])
    Amid = s.zeros(d)
    for j in range(d):
        r = s.Poly(s.rem(x**(j+1), h, x), x)
        for i in range(d):
            Amid[i, j] = r.nth(i)
    require(label+": exact CRT bijection", T.det() != 0)
    require(label+": original generator intertwining", s.simplify(T*Amid-A*T) == zero)


packet([s.Rational(3, 4)+2*s.I, s.Rational(3, 4)-2*s.I,
        s.Rational(1, 4)-2*s.I, s.Rational(1, 4)+2*s.I], 2)
packet([s.Rational(1, 2)+3*s.I, s.Rational(1, 2)-3*s.I], 3)
packet([s.Rational(1, 3), s.Rational(2, 3)], 2)

root = Path(__file__).resolve().parent
tex = root.parent/'tex/historical_packet_ghost.tex'
receipt = {"scope": "Exact finite calibration packets only; complete proofs are in the TeX.",
           "checks": checks, "passed": sum(c['passed'] for c in checks),
           "total": len(checks), "tex_sha256": hashlib.sha256(tex.read_bytes()).hexdigest()}
out = root.parent/'checks/check_historical_packet_ghost_20260912.json'
out.write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(f"{receipt['passed']}/{receipt['total']} exact calibration checks; {out}")
