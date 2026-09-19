"""Exact labelled-evaluation derivation of O'(delta) O(delta)^(-1)."""
import sympy as s
from pathlib import Path

delta, gamma = s.symbols("delta gamma", positive=True)
i = s.I
labels = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
columns, logarithmic = [], []
for eps, eta in labels:
    r = s.Rational(1, 2)+eps*delta+i*eta*gamma
    d = 4*delta*gamma*(eps*gamma-i*eta*delta)
    columns.append(s.Matrix([1, -i*d, -s.Rational(1, 2)*d**2+2*r*d,
                             7*i*r**2*d-13*i*d**2]))
    logarithmic.append(-1/(2*delta)+i*eta/(2*(eps*gamma-i*eta*delta)))
N = s.Matrix.hstack(*columns)
K = (s.diff(N, delta)+N*s.diag(*logarithmic)).applyfunc(s.factor)
print("det N =", s.factor(N.det()), flush=True)
Omega = (K*N.inv()).applyfunc(s.factor)
out = Path(__file__).with_name("signed_frame_connection_exact.txt")
with out.open("w", encoding="utf-8") as f:
    for j in range(4):
        for k in range(4):
            f.write(f"Omega[{j+1},{k+1}] = {Omega[j,k]}\n")
    f.write("trace = "+str(s.factor(s.trace(Omega)))+"\n")
print(Omega, flush=True)
print("trace =", s.factor(s.trace(Omega)), flush=True)
for residual in Omega*N-K:
    numerator = s.together(residual).as_numer_denom()[0]
    assert s.Poly(s.expand(numerator), delta, gamma, extension=i).is_zero
print("Exact original-coordinate connection identity passed.", flush=True)

# Save exact machine-readable expressions as source literals, not decimal fits.
expr = Path(__file__).with_name("signed_frame_connection_expressions.py")
expr.write_text("import sympy as s\ndelta, gamma = s.symbols('delta gamma', positive=True)\nI=s.I\n"
                +"Omega=s.Matrix("+repr(Omega.tolist())+")\n", encoding="utf-8")
