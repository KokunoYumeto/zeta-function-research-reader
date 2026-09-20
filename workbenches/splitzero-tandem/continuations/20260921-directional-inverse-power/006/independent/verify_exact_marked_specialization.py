"""Exact polynomial certificate for the two-leg marked specialization."""
import sympy as s

a, y, z, w, x, eps, t, b = s.symbols("a y z w x eps t b")
i = s.I
P = s.Matrix([
    a**3*z+2*a**2*y-i*a,
    -a**3*y**2*z-2*i*a**2*y*z+a**2*w-2*a**2*y**3-10*i*a*y**2+3*a*z+y,
    2*a**3*y**3*z+6*i*a**2*y**2*z+2*a**2*w*y+4*a**2*y**4
    +2*i*a*w-4*i*a*y**3-2*a*y*z+2*i*z+7*y**2,
    2*a**3*y**4*z+8*i*a**2*y**3*z+a**2*w*y**2+4*a**2*y**5
    +2*i*a*w*y+7*i*a*y**4-10*a*y**2*z-4*i*y*z-w-3*y**3,
])

def peval(q):
    return P.subs(dict(zip([a, y, z, w], q)), simultaneous=True)

def zero(expr, vars):
    numerator = s.together(expr).as_numer_denom()[0]
    return s.Poly(s.expand(numerator), *vars, extension=i).is_zero

u1 = s.Matrix([-i*eps+i*eps**3/2, 3*i*eps/2, -1, 0])
qm = s.Matrix([eps, 0, i/2, 0])
qm_lost = s.Matrix([-eps, 2*i/eps, 6*i/eps**2-i/2, 40*i/eps**3])
for q in [qm, qm_lost]:
    assert all(zero(entry, [eps]) for entry in peval(q)-u1)
h1 = u1[0]*x**4+x**3+u1[1]*x**2-x
assert s.expand(s.discriminant(h1, x)-(4-9*eps**2/4)) == 0
assert zero(h1-(eps*x+i)*x*(-i*(1-eps**2/2)*x**2+eps*x/2+i), [x, eps])
print("First leg: exact eight-state target, root-factorization and discriminant verified.")

# Use t=sqrt(tau)>0 and b=sqrt(1+tau)>0; reduce by b^2-t^2-1.
u2 = s.Matrix([0, 1-t**2, -t**2, 0])
for sign in [-1, 1]:
    n = s.Matrix([sign*i/t, -sign*t, -3*i*t**2,
                  -t**2+t**4+13*sign*t**3])
    root_t = s.Matrix([sign/(t*b), -t**2-i*sign*t*b,
                       2*sign*t**3*b+3*i*t**2*b**2,
                       t**2*b**2*(1-18*t**2)-i*sign*t**3*b*(13+6*t**2)])
    root_e = s.Matrix([sign/b, 1-i*sign*b,
                       -2*sign*b+3*i*b**2,
                       (18-t**2)*b**2-i*sign*b*(6+13*t**2)])
    for label, q in [("N", n), ("T", root_t), ("E", root_e)]:
        residual = peval(q)-u2
        for entry in residual:
            numerator = s.together(entry).as_numer_denom()[0]
            remainder = s.rem(s.Poly(s.expand(numerator), b), s.Poly(b**2-t**2-1, b))
            assert zero(remainder.as_expr(), [t]), (label, sign, remainder)
qinf = s.Matrix([0, 1-t**2, i*(7*(1-t**2)**2+t**2)/2,
                 11*(1-t**2)**3+2*t**2*(1-t**2)])
assert all(zero(entry, [t]) for entry in peval(qinf)-u2)
h2 = x*(x-t**2)*(x+1)
assert s.expand(s.discriminant(h2, x)-t**4*(1+t**2)**2) == 0
print("Second leg: all7 complete original-coordinate branches verified, both signs each.")
print("All exact two-leg specialization checks passed.")
