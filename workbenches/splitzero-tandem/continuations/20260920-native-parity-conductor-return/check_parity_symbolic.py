"""Exact finite checks; all recurrence parameters and even moments remain symbolic."""
import sympy as sp

x, y, c = sp.symbols("x y c", real=True)
beta = [sp.Integer(0)] + list(sp.symbols("b1:10", positive=True))
p = [sp.Integer(1), y]
for d in range(1, 8):
    p.append(sp.expand(y*p[d] - beta[d]*p[d-1]))

def even_to_x(poly):
    out = 0
    for (degree,), coeff in sp.Poly(sp.expand(poly), y).terms():
        assert degree % 2 == 0
        out += coeff*x**(degree//2)
    return sp.expand(out)

e = [even_to_x(p[2*n]) for n in range(5)]
o = [even_to_x(sp.cancel(p[2*n+1]/y)) for n in range(4)]
a = [beta[2*n+1] for n in range(4)]
d = [sp.Integer(0)] + [beta[2*n] for n in range(1, 5)]

def zero(expr):
    assert sp.expand(expr) == 0, sp.factor(expr)

for n in range(4):
    zero(x*o[n] - e[n+1] - a[n]*e[n])
    zero(e[n] - o[n] - (d[n]*o[n-1] if n else 0))
    zero(e[n].subs(x,0) - (-1)**n*sp.prod(a[j] for j in range(n)))
    zero(o[n].subs(x,0) - (-1)**n*sum(
        sp.prod(d[r] for r in range(j+1,n+1))*sp.prod(a[r] for r in range(j))
        for j in range(n+1)))
    zero(o[n].subs(x,0) - sp.diff(e[n+1],x).subs(x,0)
         - a[n]*sp.diff(e[n],x).subs(x,0))
for n in range(3):
    zero(x*e[n]-e[n+1]-(a[n]+d[n])*e[n]
         -(a[n-1]*d[n]*e[n-1] if n else 0))
    zero(x*o[n]-o[n+1]-(a[n]+d[n+1])*o[n]
         -(a[n]*d[n]*o[n-1] if n else 0))

cutoff = 4
nu = sp.symbols("v0:5", real=True)

def moment(poly):
    return sum(coeff*nu[degree//2] for (degree,),coeff in sp.Poly(sp.expand(poly),y).terms()
               if degree % 2 == 0)

t = sp.Matrix(cutoff+1,cutoff+1,
    lambda r,j: sp.binomial(j,r)*c**(j-r)*sp.I**r if r <= j else 0)
order = [0,2,4,1,3]
perm = sp.zeros(cutoff+1)
for row,column in enumerate(order):
    perm[row,column] = 1
source = perm*t
he = sp.Matrix(3,3,lambda i,j:nu[i+j])
ho = sp.Matrix(2,2,lambda i,j:nu[i+j+1])
hblock = sp.diag(he,ho)
h_original = sp.Matrix(cutoff+1,cutoff+1,
    lambda i,j:moment((c-sp.I*y)**i*(c+sp.I*y)**j))
for entry in source.conjugate().T*hblock*source-h_original:
    zero(entry)

z, aa = sp.symbols("z aa", real=True)
for degree in range(1,9):
    assert sp.cancel(z**degree/(z+aa) - sum((-aa)**r*z**(degree-1-r) for r in range(degree))
                     -(-aa)**degree/(z+aa)) == 0

# Pairing one opposite-root pair retains its minus sign; an even number
# of such pairs (as in q divisible by four) has total sign plus.
u1,u2,v1,v2 = sp.symbols("u1 u2 v1 v2", real=True)
paired = sp.expand((sp.I*y-u1-sp.I*v1)*(sp.I*y+u1+sp.I*v1)
                   *(sp.I*y-u2-sp.I*v2)*(sp.I*y+u2+sp.I*v2))
square = sp.expand((y*y-(v1-sp.I*u1)**2)*(y*y-(v2-sp.I*u2)**2))
zero(paired-square)

source_s = sp.symbols("S")
source_polys = [sp.expand(sp.I**degree*p[degree].subs(y,(source_s-c)/sp.I))
                for degree in range(7)]
for degree in range(1,6):
    zero((source_s-c)*source_polys[degree]-source_polys[degree+1]
         +beta[degree]*source_polys[degree-1])

print("PASS: both Christoffel maps and both zero-value formulas through parity degree 3.")
print("PASS: both complete parity recurrences through parity degree 2.")
print("PASS: exact original S-coordinate/parity Gram congruence through source degree 4.")
print("PASS: all rational moment division signs through degree 8.")
print("PASS: opposite-root pairing and full square-quotient sign.")
print("PASS: original S-monic phase factors and negative recurrence sign through degree 5.")
print("No numerical arithmetic weight, unit-mass substitution, or phase estimate used.")
