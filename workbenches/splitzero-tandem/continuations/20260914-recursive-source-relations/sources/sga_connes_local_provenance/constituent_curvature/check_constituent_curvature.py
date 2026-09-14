"""Exact finite review of captured SC1--SC37; no contour or arithmetic evaluation.

The period-frame values are arbitrary invertible complex matrices. Their jets
are supplied by the stated holomorphic ODE, not obtained from contour integrals.
Every fixture keeps an explicit, nonidentity finite source/quotient Gram.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys
import unittest

import sympy as s

S = s.Symbol("S")
IUNIT = s.I
MUTATION = None
EXPECTED_SOURCE_SHA256 = "0aedbaf3481f3a8e88c91ec786a44cd26869f0b0988d927a43ffaf54ad906e20"


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def simp(x):
    return s.simplify(s.expand_complex(x))


def equal(a, b, message):
    if isinstance(a, s.MatrixBase) or isinstance(b, s.MatrixBase):
        require(a.shape == b.shape, message + ": shape")
        require(all(simp(x) == 0 for x in a - b), message)
    else:
        require(simp(a - b) == 0, message)


def coeff(p, q):
    pp = s.Poly(s.expand(p), S)
    return s.Matrix([pp.nth(j) for j in range(q)])


def mod(p, f):
    return s.rem(s.Poly(p, S, extension=IUNIT), s.Poly(f, S, extension=IUNIT)).as_expr()


def mul_matrix(p, f):
    q = s.degree(f, S)
    return s.Matrix.hstack(*(coeff(mod(p * S**j, f), q) for j in range(q)))


def positive_gram(h, message):
    equal(h, h.H, message + ": Hermitian")
    for j in range(1, h.rows + 1):
        value = simp(h[:j, :j].det())
        require(value.is_positive is True, message + ": positive leading minor")


def determinant_jet(h, ht, hb, htb):
    """determinant's four bidegree <= (1,1) coefficients, via permutations.

    Independent of inverse/trace formulas: polynomial multiplication is
    truncated explicitly and includes both cross-term orders.
    """
    n = h.rows
    out = {(0, 0): s.Integer(0), (1, 0): s.Integer(0),
           (0, 1): s.Integer(0), (1, 1): s.Integer(0)}
    if n == 0:
        out[(0, 0)] = s.Integer(1)
        return out
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        acc = {(0, 0): s.Integer((-1)**inversions)}
        for i, j in enumerate(perm):
            factor = {(0, 0): h[i, j], (1, 0): ht[i, j],
                      (0, 1): hb[i, j], (1, 1): htb[i, j]}
            nxt = {}
            for (a, b), x in acc.items():
                for (c, d), y in factor.items():
                    if a + c <= 1 and b + d <= 1:
                        key = (a + c, b + d)
                        nxt[key] = nxt.get(key, 0) + x * y
            acc = nxt
        for key, value in acc.items():
            out[key] += value
    return {key: simp(value) for key, value in out.items()}


def fixture(name, chi, g, t, u):
    chi, g = s.expand(chi), s.expand(g)
    q = int(s.degree(chi, S))
    h = s.cancel(chi / g)
    p = int(s.degree(h, S))
    require(0 < p < q and s.rem(chi, g, S) == 0, "proper exact divisor")
    jg = s.Matrix.hstack(*(coeff(g * S**j, q) for j in range(p)))
    # Non-unit, complex basis change is retained, not quotiented away.
    frame = s.eye(p)
    for j in range(p):
        frame[j, j] = j + 2 + (j % 2) * IUNIT
        if j + 1 < p:
            frame[j, j + 1] = 1 + IUNIT
    inc = jg * frame
    a = mul_matrix(S, chi)
    af = frame.inv() * mul_matrix(S, h) * frame
    e0 = s.eye(q)[:, 0]
    ell = s.eye(q)[q - 1, :]
    rankone = e0 * ell
    pi = s.zeros(q)
    for j in range(q):
        pi[j, j] = j + 1 + IUNIT
        if j + 1 < q:
            pi[j, j + 1] = 1 - IUNIT
        if j + 2 < q:
            pi[j, j + 2] = 2
    c = s.eye(q)
    for j in range(q):
        c[j, j] = j + 2
        if j + 1 < q:
            c[j, j + 1] = 1 + IUNIT
    gram = 7 * c.H * c  # The literal finite fixture's mass 7 stays present.
    y = pi * inc
    hh = y.H * y
    proj = y * hh.inv() * y.H
    normal = s.eye(q) - proj
    z = normal * pi * e0
    lrow = ell * inc
    bt = a + t * rankone
    pi1 = -pi * bt / u
    y1 = pi1 * inc
    return dict(name=name, chi=chi, g=g, h=h, q=q, p=p, jg=jg,
                frame=frame, inc=inc, a=a, af=af, e0=e0, ell=ell,
                rankone=rankone, pi=pi, gram=gram, y=y, hh=hh,
                proj=proj, normal=normal, z=z, lrow=lrow,
                bt=bt, pi1=pi1, y1=y1, t=t, u=u)


FIXTURES = [
    fixture("complex_double_p1", (S - 1 - IUNIT)**2, S - 1 - IUNIT,
            s.Rational(1, 2) + IUNIT, 2 - IUNIT),
    fixture("triple_codimension_one", (S - 1)**3, S - 1,
            -1 + 2 * IUNIT, 1 + IUNIT),
    fixture("two_double_factors_p2", (S - 1)**2 * (S + 2)**2, (S - 1)**2,
            2 - IUNIT, 3 + 2 * IUNIT),
    fixture("two_double_factors_p1", (S - 1)**2 * (S + 2)**2,
            (S - 1)**2 * (S + 2), 1 + IUNIT, 1 - 2 * IUNIT),
    fixture("two_double_factors_codimension_one", (S - 1)**2 * (S + 2)**2,
            S - 1, s.Rational(2, 3) - IUNIT, 2 + IUNIT),
]


class ConstituentCurvatureTests(unittest.TestCase):
    def test_01_source_pin_and_corrected_exponents(self):
        raw = Path(__file__).with_name("SC1_SC37_CAPTURE.tex").read_bytes()
        require(hashlib.sha256(raw).hexdigest() == EXPECTED_SOURCE_SHA256, "captured source SHA")
        require(b"\\tag{SC37}" in raw and b"^{,2}" not in raw, "SC37 edition and corrected powers")

    def test_02_invariant_ideals_and_literal_top_row(self):
        for f in FIXTURES:
            equal(f["a"] * f["inc"], f["inc"] * f["af"], f["name"] + ": invariant")
            require(f["inc"].rank() == f["p"], "inclusion injective")
            require(f["inc"].row_join(f["e0"]).rank() == f["p"] + 1, "unit outside ideal")
            equal(f["ell"] * f["jg"], s.eye(f["p"])[f["p"] - 1, :], "ideal top row")
            equal(f["rankone"] * f["inc"], f["e0"] * f["lrow"], "rank-one factorization")
            require(len(f["lrow"].nullspace()) == f["p"] - 1, "full kernel dimension")

    def test_03_period_projection_and_normal_map(self):
        for f in FIXTURES:
            positive_gram(f["hh"], "period constituent Gram")
            equal(f["proj"]**2, f["proj"], "projection idempotence")
            equal(f["proj"].H, f["proj"], "projection adjoint")
            equal(f["normal"] * f["y"], s.zeros(f["q"], f["p"]), "normal kills Y")
            require(f["z"].rank() == 1, "normal unit nonzero")
            sign = 1 if MUTATION == "normal_sign" else -1
            target = sign * f["t"] / f["u"] * f["z"] * f["lrow"]
            equal(f["normal"] * f["y1"], target, "SC12 complex sign and scale")
            require((f["normal"] * f["y1"]).rank() == 1, "nonzero normal rank")
            for v in f["lrow"].nullspace():
                equal(f["normal"] * f["y1"] * v, s.zeros(f["q"], 1), "normal kernel")

    def test_04_zero_tangent_and_normal_acceleration(self):
        for f in FIXTURES:
            y1zero = -f["pi"] * f["a"] * f["inc"] / f["u"]
            y2zero = f["pi"] * f["a"]**2 * f["inc"] / f["u"]**2 - f["pi"] * f["rankone"] * f["inc"] / f["u"]
            equal(f["normal"] * y1zero, s.zeros(f["q"], f["p"]), "stationary tangent")
            equal(f["normal"] * y2zero, -f["z"] * f["lrow"] / f["u"], "SC13 acceleration")
            require((f["normal"] * y2zero).rank() == 1, "acceleration rank one")

    def test_05_curvature_from_independent_determinant_jets(self):
        for f in FIXTURES:
            y, y1, h = f["y"], f["y1"], f["hh"]
            ht, hb, htb = y.H * y1, y1.H * y, y1.H * y1
            jet = determinant_jet(h, ht, hb, htb)
            direct = jet[(1, 1)] / jet[(0, 0)] - jet[(1, 0)] * jet[(0, 1)] / jet[(0, 0)]**2
            trace = s.trace(h.inv() * y1.H * f["normal"] * y1)
            ccoef = (f["z"].H * f["z"])[0] * (f["lrow"] * h.inv() * f["lrow"].H)[0] / (f["u"] * s.conjugate(f["u"]))
            equal(direct, trace, "SC15 determinant polynomial calculation")
            equal(trace, f["t"] * s.conjugate(f["t"]) * ccoef, "SC16 rank-one curvature")
            require(simp(ccoef).is_positive is True, "strict curvature coefficient")

    def test_06_nonidentity_original_source_gram_and_lift(self):
        for f in FIXTURES:
            q, g = f["q"], f["gram"]
            positive_gram(g, "literal source quotient Gram")
            v = s.Matrix([j + 1 + IUNIT for j in range(q)])
            obs = (g + v * v.H).row_join(v).col_join(v.H.row_join(s.ones(1, 1)))
            b = s.eye(q).row_join(s.zeros(q, 1))
            k = b * obs.inv() * b.H
            r = obs.inv() * b.H * g
            equal(k.inv(), g, "Schur complement recovers original G")
            equal(b * r, s.eye(q), "actual minimum-norm lift")
            ds = f["a"].row_join(s.zeros(q, 1)).col_join(s.zeros(1, q + 1))
            dst = ds + f["t"] * r * f["rankone"] * b
            equal(b * dst, f["bt"] * b, "SC8 actual source action")
            equal(dst * r - r * f["bt"], ds * r - r * f["a"], "SC8 original primitive retained")
            equal(b * (ds * r - r * f["a"]), s.zeros(q), "primitive remains source relation")

    def test_07_theta_congruence_projection_and_schur_norm(self):
        for f in FIXTURES:
            inv = f["pi"].inv()
            g, inc, y = f["gram"], f["inc"], f["y"]
            gf = inc.H * g * inc
            target = inv.H * g * inv
            ptheta = y * gf.inv() * y.H * target
            equal(ptheta**2, ptheta, "SC23 idempotence")
            equal(ptheta.H * target, target * ptheta, "SC23 weighted self-adjointness")
            equal(y.H * target * y, gf, "SC23 original theta congruence")
            ztheta = (s.eye(f["q"]) - ptheta) * f["pi"] * f["e0"]
            schur = f["e0"].H * g * f["e0"] - f["e0"].H * g * inc * gf.inv() * inc.H * g * f["e0"]
            equal(ztheta.H * target * ztheta, schur, "SC24 full Schur norm")
            require(simp(schur[0]).is_positive is True, "SC24 positivity")
            bcomp = gf.inv() * f["hh"]
            equal(bcomp.inv() * gf.inv(), f["hh"].inv(), "SC22 ordered inverse factors")

    def test_08_moving_metric_all_derivative_cancellations(self):
        for f in FIXTURES:
            inv, g, bt, u = f["pi"].inv(), f["gram"], f["bt"], f["u"]
            inv1 = bt * inv / u  # derivative of inverse, from the literal ODE
            target = inv.H * g * inv
            target_t = inv.H * g * inv1
            target_b = inv1.H * g * inv
            target_tb = inv1.H * g * inv1
            ordered = bt * g if MUTATION == "metric_order" else g * bt
            equal(target_t, inv.H * ordered * inv / u, "SC25 metric factor order")
            y, y1 = f["y"], f["y1"]
            equal(y.H * target_t * y + y.H * target * y1, s.zeros(f["p"]), "SC25 t cancellation")
            equal(y1.H * target * y + y.H * target_b * y, s.zeros(f["p"]), "SC25 conjugate cancellation")
            mixed = y1.H * target_t * y + y.H * target_tb * y + y1.H * target * y1 + y.H * target_b * y1
            equal(mixed, s.zeros(f["p"]), "all four mixed moving-metric terms cancel")

    def test_09_neighboring_minors_and_original_basis_scalar(self):
        for f in FIXTURES:
            jg, pi = f["jg"], f["pi"]
            jm, jp = jg[:, :f["p"] - 1], jg.row_join(f["e0"])
            hgmat = (pi * jg).H * pi * jg
            hg, hm, hp = simp(hgmat.det()), simp(((pi * jm).H * pi * jm).det()), simp(((pi * jp).H * pi * jp).det())
            c = (f["inc"].H * f["inc"]).inv() * f["inc"].H * jg
            equal(f["inc"] * c, jg, "SC32 original ideal frame")
            equal(hgmat, c.H * f["hh"] * c, "SC32 congruence")
            equal(hg, s.conjugate(c.det()) * c.det() * f["hh"].det(), "SC32 retained basis determinant")
            equal(hp, hg * (f["z"].H * f["z"])[0], "SC33 Schur factor")
            equal(hm / hg, (f["lrow"] * f["hh"].inv() * f["lrow"].H)[0], "SC34 cofactor")
            factor = s.Integer(1) if MUTATION == "drop_minor_factor" else hm
            curvature = s.trace(f["hh"].inv() * f["y1"].H * f["normal"] * f["y1"])
            equal(curvature, f["t"] * s.conjugate(f["t"]) / (f["u"] * s.conjugate(f["u"])) * hp * factor / hg**2, "SC34 both neighboring minors")
            if f["p"] == 1:
                equal(hm, 1, "empty minor determinant")
            if f["p"] == f["q"] - 1:
                equal(jp.det(), (-1)**(f["q"] - 1), "SC37 determinant sign")
                equal((pi * jp).det(), (-1)**(f["q"] - 1) * pi.det(), "SC37 complex determinant phase")

    def test_10_neighboring_theta_volume_factorization(self):
        for f in FIXTURES:
            js = [f["jg"][:, :f["p"] - 1], f["jg"], f["jg"].row_join(f["e0"])]
            vs, bs, hs = [], [], []
            for j in js:
                gj = j.H * f["gram"] * j
                hj = (f["pi"] * j).H * f["pi"] * j
                v, b, h = simp(gj.det()), simp((gj.inv() * hj).det()), simp(hj.det())
                equal(h, v * b, "SC35 original theta volume times period comparison")
                vs.append(v); bs.append(b); hs.append(h)
            equal(hs[2] * hs[0] / hs[1]**2, vs[2] * vs[0] / vs[1]**2 * bs[2] * bs[0] / bs[1]**2, "SC36 both squared denominators and mass factors")

    def test_11_full_and_empty_constituents(self):
        for f in FIXTURES:
            pi, pi1 = f["pi"], f["pi1"]
            fullh = pi.H * pi
            fulln = s.eye(f["q"]) - pi * fullh.inv() * pi.H
            equal(fulln, s.zeros(f["q"]), "full constituent normal zero")
            equal(s.trace(fullh.inv() * pi1.H * fulln * pi1), 0, "full curvature zero")
            empty = s.zeros(f["q"], 0)
            equal((empty.H * empty).det(), 1, "empty Gram determinant one")

    def test_12_collision_tor_representatives_and_S_equivariance(self):
        for chi, t0 in [((S - 1)**3 + 2, 2), ((S - 1)**2 * (S + 2)**2 + 3, 3)]:
            fpoly, deriv = s.expand(chi - t0), s.diff(chi, S)
            q = int(s.degree(fpoly, S)); mdim = q - 1
            family_kernel = mul_matrix(fpoly, deriv).nullspace()
            fibre_kernel = mul_matrix(deriv, fpoly).nullspace()
            require(len(family_kernel) == len(fibre_kernel) == s.degree(s.gcd(fpoly, deriv), S), "Tor and annihilator dimensions retain repeated factors")
            images = []
            for vv in family_kernel:
                v = sum(vv[j] * S**j for j in range(mdim))
                quotient, remainder = s.div(fpoly * v, deriv, S)
                equal(remainder, 0, "SC30 exact divisibility")
                if MUTATION == "tor_scale":
                    quotient *= 2
                equal(deriv * quotient, fpoly * v, "SC30 retained derivative scale")
                images.append(coeff(mod(quotient, fpoly), q))
                shift = S + 2
                qshift, rshift = s.div(fpoly * (v + deriv * shift), deriv, S)
                equal(rshift, 0, "SC30 representative change divisible")
                equal(qshift - quotient, fpoly * shift, "SC30 well-defined representative change")
                sv = mod(S * v, deriv)
                sq, sr = s.div(fpoly * sv, deriv, S)
                equal(sr, 0, "SC30 S action source kernel")
                equal(mod(sq - S * quotient, fpoly), 0, "SC30 S-equivariant Tor map")
            images = s.Matrix.hstack(*images)
            require(images.rank() == len(family_kernel), "SC30 injective Tor map")
            equal(mul_matrix(deriv, fpoly) * images, s.zeros(q, len(family_kernel)), "SC30 image annihilator")
            require(images.row_join(s.Matrix.hstack(*fibre_kernel)).rank() == images.rank(), "SC30 surjective onto full annihilator")

    def test_13_gamma_product_powers_and_root_unity_gram(self):
        # Algebraic checks of stated finite factors, not Gamma quadrature.
        for d in (2, 3, 4):
            q = d - 1
            roots = [s.expand_complex(s.exp(2 * s.pi * IUNIT * k / d)) for k in range(d)]
            v = s.Matrix([[roots[(j * l) % d] - 1 for l in range(1, d)] for j in range(1, d)])
            equal(v.H * v, d * (s.eye(q) + s.ones(q)), "SC6a root-of-unity Gram")
            equal(s.conjugate(v.det()) * v.det(), d**(q + 1), "SC6a Vandermonde squared factor")
            equal((q + 1) + q - 2 * q - 1, 0, "SC6a complete d exponent")


def main():
    global MUTATION
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=("normal_sign", "metric_order", "drop_minor_factor", "tor_scale"))
    parser.add_argument("--receipt")
    args = parser.parse_args()
    MUTATION = args.mutation
    mutation_targets = {
        "normal_sign": "test_03_period_projection_and_normal_map",
        "metric_order": "test_08_moving_metric_all_derivative_cancellations",
        "drop_minor_factor": "test_09_neighboring_minors_and_original_basis_scalar",
        "tor_scale": "test_12_collision_tor_representatives_and_S_equivariance",
    }
    suite = (unittest.TestSuite([ConstituentCurvatureTests(mutation_targets[MUTATION])])
             if MUTATION else unittest.defaultTestLoader.loadTestsFromTestCase(ConstituentCurvatureTests))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    receipt = dict(schema=1, source_sha256=EXPECTED_SOURCE_SHA256,
                   checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   methods=result.testsRun, failures=len(result.failures), errors=len(result.errors),
                   successful=result.wasSuccessful(), mutation=MUTATION,
                   fixture_names=[f["name"] for f in FIXTURES],
                   fixture_degrees=[[f["q"], f["p"]] for f in FIXTURES],
                   sympy_version=s.__version__,
                   scope="Exact finite symbolic frames and ODE-implied jets; no contour evaluation, arithmetic estimate, or Lean.")
    if args.receipt:
        Path(args.receipt).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
