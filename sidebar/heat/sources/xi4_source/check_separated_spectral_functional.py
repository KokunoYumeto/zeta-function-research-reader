"""Exact rational checks of the derived separated-link spectral functional.

The all-box incidence proof is in the companion independent calculation.
This checker tests the spin-channel subtraction and spectral moment identities;
it does not turn a fixed Taylor coefficient into a full quantum measure.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def main():
    vacuum_zero = F(4, 27)
    vacuum_one = F(4, 39)
    adjacent = F(3, 4) ** 2 * (
        vacuum_zero ** 2 * F(1, 4) + vacuum_one ** 2 * F(3, 4)
    )
    disconnected = F(1, 144)
    connected = adjacent - disconnected
    assert connected == F(127, 219024)
    # Each source link is an outer edge of a different face, so s=1/4,w=0.
    s, w = F(1, 4), F(0)
    out_zero = (4 * s - 2 * w) / 9 - 2 * s / 3
    out_one = (12 * s + 2 * w) / 39 - 2 * s / 7
    assert out_zero == -F(1, 18)
    assert out_one == F(1, 182)
    high_zero = out_zero ** 2 / 4
    high_one = out_one ** 2 * F(3, 4)
    assert high_zero == F(1, 1296)
    assert high_one == F(3, 132496)
    band_mass = connected - high_zero - high_one
    assert band_mass == -F(59, 275184)
    band_energy_derivative = -F(1, 4) * F(1, 21) * F(1, 4)
    assert band_energy_derivative == -F(1, 336)

    def monomial_moment(degree):
        derivative = F(0) if degree == 0 else degree * F(3) ** (degree - 1)
        return (
            band_mass * F(3) ** degree
            + band_energy_derivative * derivative
            + high_zero * F(9, 2) ** degree
            + high_one * F(13, 2) ** degree
        )

    assert monomial_moment(0) == connected
    assert monomial_moment(1) == 0
    # Direct derivatives at tau=0 of the retained dimensionless heat kernel.
    heat_at_zero = band_mass + high_zero + high_one
    heat_derivative_at_zero = (
        -3 * band_mass - band_energy_derivative
        - F(9, 2) * high_zero - F(13, 2) * high_one
    )
    assert heat_at_zero == connected
    assert heat_derivative_at_zero == 0
    assert connected / 256 == F(127, 56070144)
    receipt = {
        "status": "PASS",
        "scope": "exact fourth Taylor-coefficient algebra, not a continuum claim",
        "connected_covariance": str(connected),
        "band_mass": str(band_mass),
        "band_energy_derivative": str(band_energy_derivative),
        "higher_9_over_2_mass": str(high_zero),
        "higher_13_over_2_mass": str(high_one),
        "moments_degree_0_through_6": {
            str(k): str(monomial_moment(k)) for k in range(7)
        },
        "heat_derivative_at_zero": str(heat_derivative_at_zero),
    }
    result = Path(__file__).with_name("SEPARATED_SPECTRAL_FUNCTIONAL_CHECKS.json")
    result.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
