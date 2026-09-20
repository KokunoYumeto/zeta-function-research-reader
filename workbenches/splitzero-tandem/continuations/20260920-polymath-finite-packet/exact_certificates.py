"""Exact rational certificates for the independently checked RTN remainder.

Uses only integer arithmetic, fractions, and factorial. No floating-point
comparison participates in any certificate. See INDEPENDENT_DERIVATION.tex
for the series remainder proofs and the analytic argument.
"""

from fractions import Fraction as Q
from math import factorial


def atan_bounds(z, n):
    s = sum(((-1) ** j * z ** (2*j+1) / (2*j+1)
             for j in range(n+1)), Q(0))
    following = (-1) ** (n+1) * z ** (2*n+3) / (2*n+3)
    return min(s, s + following), max(s, s + following)


def log_bounds(x, n):
    z = (x-1)/(x+1)
    if not 0 < z < 1:
        raise ValueError('log series requires 0 < (x-1)/(x+1) < 1')
    s = 2*sum((z ** (2*j+1)/(2*j+1) for j in range(n+1)), Q(0))
    tail = 2*z ** (2*n+3)/((2*n+3)*(1-z*z))
    return s, s + tail


def exp_bounds(x, n):
    if not 0 <= x < n+2:
        raise ValueError('exponential series requires 0 <= x < n+2')
    s = sum((x ** j/factorial(j) for j in range(n+1)), Q(0))
    first_tail = x ** (n+1)/factorial(n+1)
    return s, s + first_tail/(1-x/(n+2))


def certify(name, comparison):
    if not comparison:
        raise ArithmeticError(name)
    print('PASS:', name)


p1l, p1u = atan_bounds(Q(1, 5), 40)
p2l, p2u = atan_bounds(Q(1, 239), 10)
pi_l, pi_u = 16*p1l - 4*p2u, 16*p1u - 4*p2l
l2_l, l2_u = log_bounds(Q(2), 60)
l3_l, l3_u = log_bounds(Q(3), 60)
sqrt_pi_u = Q(1772453851, 10**9)
certify('3.1415926535 < pi < 3.1415926536',
        Q(31415926535, 10**10) < pi_l < pi_u < Q(31415926536, 10**10))
certify('sqrt(pi) < 1.772453851', pi_u < sqrt_pi_u**2)
certify('1.0986122886 < log(3) < 1.0986122887',
        Q(10986122886, 10**10) < l3_l < l3_u < Q(10986122887, 10**10))
certify('0 < log(2) < 1', 0 < l2_l < l2_u < 1)
certify('sqrt(2)/(4 pi^2) < .036', 2 < Q(36, 1000)**2*16*pi_l**4)
certify('1/sqrt((3-2 log(2)) pi) < .445',
        1 < Q(445, 1000)**2 * (3-2*l2_u)*pi_l)
certify('sqrt(2*pi)/(4*pi) < .2', Q(1, 8) < Q(1, 5)**2*pi_l)
certify('1.21/7 < .173', Q(121, 700) < Q(173, 1000))

q = Q(445, 1000)
certify('q^2/(1-q^2) < .247', q*q/(1-q*q) < Q(247, 1000))
certify('q^3 sqrt(pi)/(2(1-q^2)) < .098',
        q**3*sqrt_pi_u/(2*(1-q*q)) < Q(98, 1000))
certify('low coefficient 1 fits .0285', Q(36, 1000)*q*sqrt_pi_u < Q(285, 10000))
certify('low coefficient 2 fits .0285*.353',
        Q(36, 1000)*Q(247, 1000) < Q(285, 10000)*Q(353, 1000))
certify('low coefficient 3 fits .0285*.353^2',
        Q(36, 1000)*Q(98, 1000) < Q(285, 10000)*Q(353, 1000)**2)

v32_squared = Q(1, 4)*Q(11, 10)**64*factorial(15)**2*Q(2, 31)**31
v33_squared_u = (Q(1, 4)*Q(11, 10)**66
                 *Q(factorial(32), 4**16*factorial(16))**2*pi_u/Q(16)**32)
certify('v32 < 4.897e-6', v32_squared < Q(4897, 10**9)**2)
certify('v33 < 3.268e-6', v33_squared_u < Q(3268, 10**9)**2)
certify('1.21 exp(-31/33) < 1', Q(121, 100) < 1 + Q(31, 33))

A_l = Q(11, 12)+(1+l3_l/2)**2+Q(1, 4)
A_u = Q(11, 12)+(1+l3_u/2)**2+Q(1, 4)
certify('3.5670161955 < A < 3.5670161956',
        Q(35670161955, 10**10) < A_l < A_u < Q(35670161956, 10**10))
absorption_exp_u = exp_bounds(l3_u*l3_u/2+(A_u-Q(349, 100))/96, 40)[1]
certify('.2 exp(log(3)^2/2+(A-3.49)/96) < .365986',
        Q(1, 5)*absorption_exp_u < Q(365986, 10**6))
certify('.029 exp(log(sqrt(2))^2/2) < .031',
        Q(29, 1000)*exp_bounds(l2_u*l2_u/8, 40)[1] < Q(31, 1000))

f14_u = Q(11, 10)**14*factorial(6)*2**10/exp_bounds(Q(100), 300)[0]
f15_u = (Q(11, 10)**15*Q(factorial(14), 4**7*factorial(7))
         *sqrt_pi_u*2**11/exp_bounds(Q(121), 330)[0])
certify('f14 < 1.042e-37', f14_u < Q(1042, 10**40))
certify('f15 < 4.516e-46', f15_u < Q(4516, 10**49))
certify('2.42*14 exp(-44) < 1', Q(242, 100)*14 < 1+44)
certify('tail slack exceeds tail bound at a=3',
        Q(7936, 10**6)*3**12 > Q(2, 10**30))
print('All exact rational certificates passed.')
