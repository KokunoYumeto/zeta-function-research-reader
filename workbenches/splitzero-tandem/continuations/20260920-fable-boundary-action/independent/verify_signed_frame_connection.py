"""Full polynomial numerator certificate for the displayed native connection."""
import sympy as s
from signed_frame_connection_expressions import delta, gamma, Omega

i = s.I
t, g = s.symbols("t g")
Q, F = t+g, g+(2*g-1)*t
B = s.zeros(4)
B[0, 0] = -224*(5*t**2*g-2*t**2+t*g**2+3*t*g+g**2)
B[0, 1] = -28*i
B[0, 2] = 28
B[1, 0] = 2880*i*t*g*Q**2
B[1, 1] = 4*(280*t**2*g-140*t**2+56*t*g**2-82*t*g+7*t+28*g**2-7*g)
B[1, 2] = -8*i*(104*t*g-7*t+7*g)
B[1, 3] = 16*F
B[2, 0] = 64*t*g*Q**2*(84*t*g-56*Q+39)
B[2, 1] = -4*i*(224*t**2*g-84*t**2+448*t*g**2-86*t*g-7*t+28*g**2+7*g)
B[2, 2] = 8*(252*t**2*g-112*t**2+252*t*g**2+20*t*g-7*t+28*g**2+7*g)
B[2, 3] = 16*i*F
B[3, 0] = 112*i*t*g*Q**2*(1248*t*g-1012*t+68*g+123)
B[3, 1] = -7*(1120*t**3*g-560*t**3+2240*t**2*g**2-2336*t**2*g+112*t**2
               +1120*t*g**3-1440*t*g**2+254*t*g+7*t+560*g**3+112*g**2-7*g)
B[3, 2] = 14*i*(832*t**2*g-28*t**2+832*t*g**2-64*t*g-7*t-140*g**2+7*g)
B[3, 3] = 28*F*(28*Q-1)
displayed = (B/(448*delta*Q*F)).subs({t: delta**2, g: gamma**2})

def zero(expr, variables):
    numerator = s.together(expr).as_numer_denom()[0]
    return s.Poly(s.expand(numerator), *variables, extension=i).is_zero

assert all(zero(entry, [delta, gamma]) for entry in displayed-Omega)
print("All16 displayed original-coordinate connection entries verified.")

labels = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
columns, logarithmic = [], []
for eps, eta in labels:
    r = s.Rational(1, 2)+eps*delta+i*eta*gamma
    d = 4*delta*gamma*(eps*gamma-i*eta*delta)
    columns.append(s.Matrix([1, -i*d, -d**2/2+2*r*d, 7*i*r**2*d-13*i*d**2]))
    logarithmic.append(-1/(2*delta)+i*eta/(2*(eps*gamma-i*eta*delta)))
N = s.Matrix.hstack(*columns)
assert all(zero(entry, [delta, gamma]) for entry in
           displayed*N-s.diff(N, delta)-N*s.diag(*logarithmic))
print("Omega N=N'+N diag(a'/a): all16 polynomial numerator identities verified.")
assert zero(N.det()+28672*delta**4*gamma**4*(delta**2+gamma**2)
            *(gamma**2+(2*gamma**2-1)*delta**2), [delta, gamma])

R = B.subs(t, 0)/(448*g**2)
lam = s.symbols("lam")
assert zero(R.charpoly(lam).as_expr()
            -(lam+s.Rational(1,2))*(lam-s.Rational(1,2))**2*(lam-s.Rational(3,2)), [lam, g])
cubic = (2*R+s.eye(4))*(2*R-s.eye(4))*(2*R-3*s.eye(4))
assert all(zero(entry, [g]) for entry in cubic)
ea = s.Matrix([1, 0, 0, 0])
xp = s.Matrix([0, 1, i, 35*g-s.Rational(7,4)])
assert all(zero(entry, [g]) for entry in R*ea+ea/2)
assert all(zero(entry, [g]) for entry in R*xp-3*xp/2)
print("Exact residue characteristic polynomial, square-free annihilator, and both eigenvectors verified.")

assert zero(s.trace(displayed)-2/delta
            -2*delta*(2*gamma**2-1)/(gamma**2+(2*gamma**2-1)*delta**2), [delta, gamma])
remainder_numerator = g**2*B-Q*F*B.subs(t, 0)
assert all(s.Poly(entry, t, g, extension=i).coeff_monomial(t**0*g**j) == 0
           for entry in remainder_numerator for j in range(10))
print("Trace identity and exact division by delta^2 in Laurent remainder verified.")
print("All signed-frame connection checks passed.")
