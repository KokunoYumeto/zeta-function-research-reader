"""Exact finite identities and numerical checks for explicit BC observables.

Single worker. No RH assumptions and no zero search. The analytic identities
and convergence proofs are in the companion TeX. Floating-point checks do not
certify the meromorphic continuation or a zero of zeta.
"""
from pathlib import Path
import hashlib
import json
import platform
import mpmath as mp
import sympy as sp


def main():
    mp.mp.dps = 60
    s, q = sp.symbols("s q")
    # q=3^-s: solve the two residue-class series exactly.
    S, L = sp.symbols("S L")
    a, b, c = (S*(1-q)+L)/2, (S*(1-q)-L)/2, q*S
    E = sp.expand(-a/2-b/2+c+sp.I*sp.sqrt(3)*(a-b)/2)
    assert sp.simplify(E-((3*q-1)*S/2+sp.I*sp.sqrt(3)*L/2)) == 0
    # Arithmetic observable A3 has the three exact residue eigenvalues.
    residue_values = [sp.simplify(2*sp.sin(2*sp.pi*r/3)/sp.sqrt(3)) for r in range(3)]
    assert residue_values == [0, 1, -1]
    m, n, beta, u = sp.symbols("m n beta u", positive=True)
    # The logarithm of the modular matrix-unit multiplier is linear in time.
    modular_exponent = sp.expand(-sp.I*u*(-beta*sp.log(m)+beta*sp.log(n)))
    assert sp.simplify(modular_exponent-sp.I*beta*u*(sp.log(m)-sp.log(n))) == 0
    checks = []
    for beta_value in (2, 3, 5):
        beta_mp = mp.mpf(beta_value)
        zeta = mp.zeta(beta_mp)
        l3 = mp.dirichlet(beta_mp, [0, 1, -1])
        e3 = mp.polylog(beta_mp, mp.exp(2j*mp.pi/3))/zeta
        formula = (mp.power(3, 1-beta_mp)-1)/2 + 1j*mp.sqrt(3)*l3/(2*zeta)
        parity = mp.polylog(beta_mp, -1)/zeta
        err = abs(e3-formula)
        assert err < mp.mpf("1e-50")
        assert abs(parity-(mp.power(2, 1-beta_mp)-1)) < mp.mpf("1e-50")
        checks.append({"beta": beta_value, "A3_expectation": mp.nstr(l3/zeta, 50),
                       "e_one_third_residual": mp.nstr(err, 8),
                       "classification": "high_precision_numerical_crosscheck_not_interval_certificate"})
    target = Path(__file__).with_name("bc_observables_results.json")
    receipt = {"schema_version": 1, "id": "BC-OBSERVABLES-20260908-001", "status": "pass",
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "python": platform.python_version(), "sympy": sp.__version__,
               "mpmath": mp.__version__, "digits": 60, "workers": 1,
               "exact_checks": {"A3_residue_eigenvalues": [0, 1, -1],
                                "residue_series_decomposition": True,
                                "modular_matrix_unit_exponent": True},
               "numerical_checks": checks,
               "claim": "Checks explicit BC observables and trace formula algebra; finds no RH counterexample.",
               "proof_text": "tex/satellites/22_rh_counterexample_routes.tex"}
    target.write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
