"""Exact finite coefficient replay in Q(i)[N]/(N^m), m=1,...,8.

lambda=1+2i is a formal algebraic parameter, not a claimed zeta zero.
The full symbolic proof is outside this bounded computational check.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
import json


@dataclass(frozen=True)
class Gaussian:
    real: Q = Q(0)
    imag: Q = Q(0)

    def __add__(self, other):
        return Gaussian(self.real + other.real, self.imag + other.imag)

    def __neg__(self):
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Gaussian(self.real * other.real - self.imag * other.imag,
                        self.real * other.imag + self.imag * other.real)

    def inverse(self):
        norm = self.real ** 2 + self.imag ** 2
        if norm == 0:
            raise ZeroDivisionError('Zero Gaussian rational')
        return Gaussian(self.real / norm, -self.imag / norm)

    def __truediv__(self, other):
        return self * other.inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = ONE
        for _ in range(exponent):
            out = out * self
        return out

    def json(self):
        return {'real': str(self.real), 'imaginary': str(self.imag)}


ZERO, ONE = Gaussian(), Gaussian(Q(1))


def multiply(left, right):
    m = len(left)
    out = [ZERO for _ in range(m)]
    for i in range(m):
        for j in range(m - i):
            out[i + j] = out[i + j] + left[i] * right[j]
    return out


def binomial(alpha, j):
    out = Q(1)
    for k in range(j):
        out *= (alpha - k) / (k + 1)
    return out


def main():
    lam = Gaussian(Q(1), Q(2))
    beta = -(lam ** -2)
    checks = []
    for m in range(1, 9):
        # Exact geometric inverse of lambda+N, with every original coefficient.
        inverse = [Gaussian(Q((-1) ** k)) * lam ** (-k - 1) for k in range(m)]
        original = [lam] + ([ONE] if m > 1 else []) + [ZERO] * max(0, m - 2)
        identity = [ONE] + [ZERO] * (m - 1)
        inverse_valid = multiply(original, inverse) == identity
        eta = [-x for x in multiply(inverse, inverse)]
        eta[0] = eta[0] - beta
        ratio = [x / beta for x in eta]
        power = identity
        reconstructed = [ZERO for _ in range(m)]
        for j in range(1, m):
            power = multiply(power, ratio)
            factor = lam * Gaussian(binomial(Q(-1, 2), j))
            reconstructed = [x + factor * y for x, y in zip(reconstructed, power)]
        expected = [ZERO] + ([ONE] if m > 1 else []) + [ZERO] * max(0, m - 2)
        check = {
            'm': m,
            'lambda_plus_N_inverse_verified': inverse_valid,
            'eta_coefficients': [x.json() for x in eta],
            'reconstructed_N_coefficients': [x.json() for x in reconstructed],
            'expected_N_coefficients': [x.json() for x in expected],
            'identity_verified': reconstructed == expected,
        }
        checks.append(check)
    report = {
        'ring': 'Q(i)[N]/(N^m)', 'lambda': lam.json(), 'beta': beta.json(),
        'eta_definition': '-(lambda+N)^(-2)-beta',
        'formula': 'N=lambda*sum(binomial(-1/2,j)*(eta/beta)^j,j=1,...,m-1)',
        'not_a_claim_about_actual_zeta_zeros': True,
        'checks': checks,
        'all_passed': all(c['lambda_plus_N_inverse_verified'] and c['identity_verified'] for c in checks),
    }
    destination = Path(__file__).with_name('FINITE_REPLAY_NILPOTENT_RECEIPT.json')
    destination.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'all_passed': report['all_passed'], 'm': [c['m'] for c in checks]}, indent=2))
    if not report['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
