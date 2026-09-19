"""Symbolic checks of the complete native Gram/current identities.

No original period or arithmetic coefficient is assigned a numerical value.
The finite matrices below are algebraic test variables, not substitutes for
the native weight.  All checks are exact symbolic polynomial identities.
"""
import sympy as s

x, y, h = s.symbols("x y h", real=True)
zr, zi, ar, ai, br, bi = s.symbols("zr zi ar ai br bi", real=True)
z, a, b = zr + s.I * zi, ar + s.I * ai, br + s.I * bi
star = s.conjugate
abs2 = lambda w: s.expand(w * star(w))
re = lambda w: s.expand((w + star(w)) / 2)
gram = s.Matrix([[x, z, a], [star(z), y, b], [star(a), star(b), h]])
det_formula = x*y*h + 2*re(z*b*star(a)) - x*abs2(b) - y*abs2(a) - h*abs2(z)
assert s.expand(gram.det() - det_formula) == 0
disk_difference = (h*x-abs2(a))*(h*y-abs2(b)) - abs2(star(a)*b-h*star(z))
assert s.expand(disk_difference - h*gram.det()) == 0
eps = s.symbols("eps", real=True)
second_minors = sum(gram.extract(ids, ids).det() for ids in ((0, 1), (0, 2), (1, 2)))
assert s.expand((gram+eps*s.eye(3)).det() - gram.det() - eps*second_minors - eps**2*s.trace(gram) - eps**3) == 0
print("Exact full Hermitian determinant, complex Schur disk, and shifted-minor sufficiency identities passed.")

f1, f2, b10, b20, r1, r2 = s.symbols("F1 F2 B10 B20 r1 r2", complex=True)
k10, k20 = f1-b10, f2-b20
B1, B2 = b10+r1, b20+r2
K1, K2 = k10-r1, k20-r2
expanded_B = star(b10)*b20 + star(b10)*r2 + star(r1)*b20 + star(r1)*r2
expanded_K = star(k10)*k20 - star(k10)*r2 - star(r1)*k20 + star(r1)*r2
expanded_cross = (star(k10)*b20+star(b10)*k20 +
                  (star(k10)-star(b10))*r2 + star(r1)*(k20-b20) - 2*star(r1)*r2)
assert s.expand(star(B1)*B2-expanded_B) == 0
assert s.expand(star(K1)*K2-expanded_K) == 0
assert s.expand(star(K1)*B2+star(B1)*K2-expanded_cross) == 0
assert s.expand(expanded_B+expanded_K+expanded_cross-star(f1)*f2) == 0
print("Exact B, K, and both complementary current products passed with every linear and quadratic remainder.")

d1, d2, E, D1, D2, e = s.symbols("d1 d2 E D1 D2 e", real=True)
source = s.Matrix([[d1, 0, f1], [0, d2, f2], [star(f1), star(f2), E]])
observed = s.Matrix([[D1, z, B1], [star(z), D2, B2], [star(B1), star(B2), e]])
kernel = s.Matrix([[d1-D1, -z, K1], [-star(z), d2-D2, K2], [star(K1), star(K2), E-e]])
assert (source-observed-kernel).applyfunc(s.expand) == s.zeros(3)
kernel_det_formula = ((d1-D1)*(d2-D2)*(E-e) - 2*re(z*K2*star(K1))
                      -(d1-D1)*abs2(K2)-(d2-D2)*abs2(K1)-(E-e)*abs2(z))
assert s.expand(kernel.det()-kernel_det_formula) == 0
print("Exact native source=observed+kernel Gram and signed kernel triple-product identities passed.")
