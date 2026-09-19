"""Exact finite checks with arbitrary symbolic moments and untouched mass."""
import sympy as sp

y, t, center = sp.symbols("y t c", real=True)
mass = sp.symbols("M", positive=True)
max_n = 3
max_degree = 2 * max_n + 2
moments = sp.symbols(f"v0:{max_degree + 1}", real=True)

p = [sp.Integer(1), y]
for n in range(1, max_degree):
    p.append(sp.expand(y * p[n] - n * (sp.Rational(2*n-1, 2)) * p[n-1]))
norm = [sp.factorial(n) * sp.rf(sp.Rational(1, 2), n) for n in range(max_degree + 1)]
r = [p[n] / sp.sqrt(norm[n]) for n in range(max_degree + 1)]

def moment(poly):
    return sum(
        coefficient * moments[power[0]]
        for power, coefficient in sp.Poly(sp.expand(poly), y).terms()
    )

def scalar_zero(value):
    assert sp.simplify(value) == 0, sp.simplify(value)

def matrix_zero(value):
    for entry in value:
        scalar_zero(entry)

size = max_degree + 1
jac = sp.zeros(size)
for n in range(size-1):
    jac[n,n+1] = jac[n+1,n] = sp.sqrt((n+1)*(sp.Rational(2*n+1, 2)))
matrix_r = [sp.eye(size), jac / sp.sqrt(sp.Rational(1, 2))]
for n in range(1, max_degree):
    b_prev = sp.sqrt(n * sp.Rational(2*n-1, 2))
    b_next = sp.sqrt((n+1) * sp.Rational(2*n+1, 2))
    matrix_r.append((jac * matrix_r[n] - b_prev * matrix_r[n-1]) / b_next)

alpha = [sp.simplify(moment(poly) / mass) for poly in r]
entries_checked = 0
for m in range(max_n + 2):
    for n in range(max_n + 2):
        if m+n > max_degree:
            continue
        c_mn = moment(r[m]*r[n])/mass
        reconstructed = sum(alpha[j]*matrix_r[j][m,n] for j in range(abs(m-n), m+n+1))
        scalar_zero(c_mn-reconstructed)
        entries_checked += 1

for cutoff in range(max_n+1):
    cn = sp.Matrix(cutoff+1, cutoff+1, lambda i,j: moment(r[i]*r[j])/mass)
    jn = jac[:cutoff+1,:cutoff+1]
    boundary = sp.Matrix([moment(r[i]*r[cutoff+1])/mass for i in range(cutoff+1)])
    terminal = sp.eye(cutoff+1)[:,cutoff]
    b = sp.sqrt((cutoff+1)*sp.Rational(2*cutoff+1,2))
    matrix_zero(jn*cn-cn*jn-b*(boundary*terminal.T-terminal*boundary.T))

gen = (1+t*t)**(-sp.Rational(1,4))*sp.exp(y*sp.atan(t))
gen_series = sp.series(gen, t, 0, 7).removeO().expand()
for n in range(7):
    scalar_zero(sp.factorial(n)*gen_series.coeff(t,n)-p[n])

cutoff = 2
bmat = sp.Matrix(cutoff+1, cutoff+1,
    lambda i,j: sp.expand(r[j]/sp.sqrt(mass)).coeff(y,i))
tmat = sp.Matrix(cutoff+1, cutoff+1,
    lambda i,j: sp.binomial(j,i)*center**(j-i)*sp.I**i if i <= j else 0)
dmat = sp.simplify(bmat.inv()*tmat)
cn = sp.Matrix(cutoff+1,cutoff+1,lambda i,j: moment(r[i]*r[j])/mass)
h_actual = sp.Matrix(cutoff+1,cutoff+1,
    lambda i,j: moment((center-sp.I*y)**i*(center+sp.I*y)**j))
# The declared positive mass is the unchanged original M_sigma.
d_star = dmat.conjugate().T
matrix_zero((d_star*cn*dmat-h_actual).applyfunc(sp.simplify))

print(f"PASS: {entries_checked} first-column entries with arbitrary symbolic moments.")
print("PASS: exact cutoff commutators N=0,1,2,3, including odd moments.")
print("PASS: generating polynomial coefficients through degree 6.")
print("PASS: source coordinate and full Gram congruence through degree 2.")
print("p_0,...,p_6 =", p[:7])
print("D_2 / sqrt(M) =", sp.simplify(dmat/sp.sqrt(mass)))
print("No numerical weight, probability renormalization, or phase estimate used.")
